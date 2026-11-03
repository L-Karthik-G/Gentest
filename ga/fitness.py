import re
import copy
from typing import Dict, Any, List, Set, Optional
from ga.individual import Chromosome
from ga.operators import validate_gene_params
import mr_library
from benchmarks.seed_circuits import BENCHMARKS, extract_circuit_and_qasm3
from mqt.core.mlir import compile_program
from mqt.core.qdmi import ProgramFormat, open_device
from qiskit.quantum_info import Statevector, state_fidelity

_MQT_DEVICE = open_device("mqt.ddsim.default")


class FitnessEvaluator:
    def __init__(
        self,
        benchmarks: Optional[List[str]] = None,
        w_cov: float = 0.25,
        w_nov: float = 0.25,
        w_cost: float = 0.25,
        w_bonus: float = 0.25,
    ):
        self.benchmarks = benchmarks or list(BENCHMARKS.keys())
        self.w_cov = w_cov
        self.w_nov = w_nov
        self.w_cost = w_cost
        self.w_bonus = w_bonus

    def evaluate_individual_stateless(self, chrom: Chromosome) -> Chromosome:
        """Evaluates an individual statelessly across the benchmark battery."""
        if not chrom.genes:
            chrom.is_valid = False
            chrom.fitness = -float("inf")
            chrom.error_msg = "empty_genes"
            return chrom

        # Parameter invariant verification
        for gene in chrom.genes:
            if not validate_gene_params(gene):
                chrom.is_valid = False
                chrom.fitness = -float("inf")
                chrom.error_msg = f"parameter_invariant_violation in {gene.mr_id}: {gene.params}"
                return chrom

        gene_dicts = [g.to_dict() for g in chrom.genes]
        passed_benchmarks = 0
        total_cov = 0.0
        total_cost = 0.0
        last_transformed_code = None
        last_qasm3 = None
        gate_types_all = set()

        # Deterministic chromosome seed for reproducibility across all evaluations
        import hashlib
        h = hashlib.sha256()
        h.update(chrom.signature().encode("utf-8"))
        for g in chrom.genes:
            h.update(str(sorted(g.params.items())).encode("utf-8"))
        chrom_seed = int(h.hexdigest()[:8], 16)

        # Multi-benchmark evaluation
        for b_name in self.benchmarks:
            seed_code = BENCHMARKS[b_name]
            success, transformed_code, logs = mr_library.apply_mr_chain(seed_code, gene_dicts, base_seed=chrom_seed)
            if not success:
                continue

            try:
                qc, qasm3_str = extract_circuit_and_qasm3(transformed_code)
            except Exception as e:
                continue

            # MQT-CC Compilation check
            try:
                _ = compile_program(qasm3_str, target=_MQT_DEVICE, program_format=ProgramFormat.QASM3)
            except Exception as e:
                continue

            passed_benchmarks += 1
            last_transformed_code = transformed_code
            last_qasm3 = qasm3_str

            # Gate coverage
            for op in qc.data:
                gate_types_all.add(op.name)

            num_ops = qc.num_ops if hasattr(qc, "num_ops") else len(qc.data)
            cost = 1.0 / (1.0 + 0.04 * num_ops)
            total_cost += cost

        if passed_benchmarks == 0:
            chrom.is_valid = False
            chrom.fitness = -float("inf")
            chrom.error_msg = "Failed preconditions or compilation across all benchmarks"
            return chrom

        chrom.is_valid = True
        chrom.generated_code = last_transformed_code
        chrom.qasm3 = last_qasm3

        avg_cov = min(1.0, len(gate_types_all) / 8.0)
        avg_cost = total_cost / passed_benchmarks

        chrom.objectives = {
            "coverage": round(avg_cov, 4),
            "cost_efficiency": round(avg_cost, 4),
            "unique_gates": len(gate_types_all),
            "passed_benchmarks": passed_benchmarks,
            "novelty": 0.0,
            "diversity_bonus": 0.0
        }
        return chrom

    def assign_population_fitness(
        self,
        population: List[Chromosome],
        archive_signatures: Set[str],
        mr_usage_count: Dict[str, int]
    ) -> None:
        """Computes novelty and diversity bonuses at generation boundaries (pure & order-independent)."""
        # Step 1: Stateless evaluation
        for ind in population:
            self.evaluate_individual_stateless(ind)

        # Step 2: Compute novelty against the frozen previous-generation archive
        for chrom in population:
            if not chrom.is_valid:
                chrom.fitness = -float("inf")
                continue

            sig = chrom.signature()
            if not archive_signatures:
                nov = 1.0
            else:
                chrom_set = set([g.mr_id for g in chrom.genes])
                max_sim = 0.0
                for prev_sig in archive_signatures:
                    prev_set = set(re.findall(r"([A-Za-z0-9_]+)\(", prev_sig))
                    if chrom_set and prev_set:
                        jaccard = len(chrom_set & prev_set) / len(chrom_set | prev_set)
                        if jaccard > max_sim:
                            max_sim = jaccard
                nov = 1.0 - max_sim

            # Diversity bonus
            bonus_sum = 0.0
            for g in chrom.genes:
                cnt = mr_usage_count.get(g.mr_id, 0)
                bonus_sum += 1.0 / (1.0 + cnt)
            bonus = min(1.0, bonus_sum / max(1, len(chrom.genes)))

            chrom.objectives["novelty"] = round(nov, 4)
            chrom.objectives["diversity_bonus"] = round(bonus, 4)

            total_fitness = (
                self.w_cov * chrom.objectives["coverage"] +
                self.w_nov * nov +
                self.w_cost * chrom.objectives["cost_efficiency"] +
                self.w_bonus * bonus
            )
            chrom.fitness = round(total_fitness, 4)
