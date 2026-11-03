import os
import sys
import re
import numpy as np
from typing import List, Dict, Any, Tuple
from scipy.stats import ks_2samp

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import mr_library
from benchmarks.seed_circuits import BENCHMARKS, extract_circuit_and_qasm3
from mqt.core.mlir import compile_program
from mqt.core.qdmi import ProgramFormat, open_device
from qiskit_aer import Aer
from qiskit import transpile

_DEVICE = open_device("mqt.ddsim.default")
_AER_BACKEND = Aer.get_backend("aer_simulator")

BOUNDARY_ANGLES = [0.0, np.pi / 2.0, np.pi, 2.0 * np.pi, -np.pi / 2.0]


def map_bitstring_permutation(bitstring: str, mapping: Dict[int, int]) -> str:
    """Remaps a measurement bitstring under qubit permutation (Qiskit little-endian)."""
    n_bits = len(bitstring)
    rev = bitstring[::-1]
    mapped_rev = "".join([rev[mapping.get(i, i)] for i in range(n_bits)])
    return mapped_rev[::-1]


def run_empirical_validation(
    gene_dicts: List[Dict[str, Any]],
    shots: int = 4096,
    base_seed: int = None
) -> Tuple[bool, str, Dict[str, Any]]:
    """Runs empirical multi-circuit simulation validation.
    Checks:
    1. Precondition and transformation execution across all seed benchmarks
    2. Boundary angle stress-testing for parameterized transformations
    3. OpenQASM 3.0 compilation through MQT-CC MLIR
    4. Output distribution statistical consistency via Kolmogorov-Smirnov test (p > 0.05)
    Zero exception masking: Any runtime exception causes validation failure.
    Deterministic seed propagation ensures reproducible evaluations.
    """
    benchmarks_tested = 0
    benchmarks_passed = 0
    mqt_compiled_count = 0
    ks_pvalues = []
    failure_reasons = []

    for b_name, source_code in BENCHMARKS.items():
        success, transformed_code, logs = mr_library.apply_mr_chain(source_code, gene_dicts, base_seed=base_seed)
        if not success:
            continue

        benchmarks_tested += 1

        # 1. MQT-CC Compilation
        try:
            qc_trans, qasm3_trans = extract_circuit_and_qasm3(transformed_code)
            _ = compile_program(qasm3_trans, target=_DEVICE, program_format=ProgramFormat.QASM3)
            mqt_compiled_count += 1
        except Exception as e:
            failure_reasons.append(f"MQT-CC compilation failed on {b_name}: {e}")
            continue

        # 2. Simulation and Distribution Comparison
        try:
            qc_orig, _ = extract_circuit_and_qasm3(source_code)
            sim_seed = base_seed if base_seed is not None else 42
            counts_orig = _AER_BACKEND.run(transpile(qc_orig, _AER_BACKEND), shots=shots, seed_simulator=sim_seed).result().get_counts()
            counts_trans = _AER_BACKEND.run(transpile(qc_trans, _AER_BACKEND), shots=shots, seed_simulator=sim_seed).result().get_counts()

            # Bitstring permutation handling for ChangeQubitOrder
            combined_mapping = {}
            for log in logs:
                meta = log.get("meta", {})
                if "full_mapping" in meta:
                    combined_mapping.update(meta["full_mapping"])

            if combined_mapping:
                remapped_counts_trans = {}
                for bitstr, cnt in counts_trans.items():
                    orig_key = map_bitstring_permutation(bitstr, combined_mapping)
                    remapped_counts_trans[orig_key] = cnt
                eval_counts_trans = remapped_counts_trans
            else:
                eval_counts_trans = counts_trans

            # Convert counts to integer samples for Kolmogorov-Smirnov test
            samples_a = []
            for bitstr, cnt in counts_orig.items():
                samples_a.extend([int(bitstr, 2)] * cnt)

            samples_b = []
            for bitstr, cnt in eval_counts_trans.items():
                samples_b.extend([int(bitstr, 2)] * cnt)

            if samples_a and samples_b:
                ks_stat, p_val = ks_2samp(samples_a, samples_b)
                ks_pvalues.append(p_val)
                # Enforce KS-test threshold: p > 0.05 required for identical distribution
                if p_val <= 0.05:
                    failure_reasons.append(f"KS-test failed on {b_name} (p-value={p_val:.4e} <= 0.05)")
                    continue

            # 3. Continuous boundary angle validation if circuit is parameterized
            if "PhaseGate" in source_code:
                boundary_fail = False
                for angle in BOUNDARY_ANGLES:
                    param_source = re.sub(r"PhaseGate\([^\)]+\)", f"PhaseGate({angle})", source_code)
                    s_ok, s_trans, _ = mr_library.apply_mr_chain(param_source, gene_dicts, base_seed=base_seed)
                    if s_ok:
                        try:
                            _, qasm_param = extract_circuit_and_qasm3(s_trans)
                            _ = compile_program(qasm_param, target=_DEVICE, program_format=ProgramFormat.QASM3)
                        except Exception as e_angle:
                            failure_reasons.append(f"Boundary angle {angle:.2f} compilation failed on {b_name}: {e_angle}")
                            boundary_fail = True
                            break
                if boundary_fail:
                    continue

            benchmarks_passed += 1
        except Exception as e:
            # Zero-exception masking: an error is an immediate failure
            failure_reasons.append(f"Simulation failed on {b_name}: {e}")

    passed_all = (
        benchmarks_tested > 0 and
        benchmarks_passed == benchmarks_tested and
        mqt_compiled_count == benchmarks_tested and
        len(failure_reasons) == 0
    )
    details = {
        "benchmarks_tested": benchmarks_tested,
        "benchmarks_passed": benchmarks_passed,
        "mqt_compiled_count": mqt_compiled_count,
        "avg_ks_pvalue": float(np.mean(ks_pvalues)) if ks_pvalues else 1.0,
        "failure_reasons": failure_reasons
    }
    msg = "PASS" if passed_all else f"FAILED: {'; '.join(failure_reasons) if failure_reasons else 'Precondition not met on suite'}"
    return passed_all, msg, details


if __name__ == "__main__":
    test_genes = [{"mr_id": "ChangeOptLevel", "params": {"levels": [0, 2, 3]}}]
    ok, msg, det = run_empirical_validation(test_genes)
    print(f"Empirical validation: {ok} -> {msg}, details: {det}")
