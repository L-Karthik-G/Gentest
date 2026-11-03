import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import json
import csv
import time
import random
import argparse
import numpy as np
from typing import List, Dict, Any, Set

from ga.individual import Chromosome
from ga.operators import (
    initialize_population,
    tournament_selection,
    crossover,
    mutate,
    select_elites
)
from ga.fitness import FitnessEvaluator


def run_ga(
    pop_size: int = 80,
    max_gens: int = 40,
    tourn_size: int = 4,
    elite_cnt: int = 4,
    p_mut_gene: float = 0.25,
    stagnation_patience: int = 8,
    depth_min: int = 2,
    depth_max: int = 3,
    seed: int = 42,
    output_dir: str = "mr_library/generated_mrs",
    generated_code_dir: str = "generated",
    results_dir: str = "results"
):
    # Set explicit random seeds for reproducible execution
    random.seed(seed)
    np.random.seed(seed)

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(generated_code_dir, exist_ok=True)
    os.makedirs(results_dir, exist_ok=True)

    print("=" * 70)
    print("STARTING REPRODUCIBLE METAMORPHIC RELATION GENETIC ALGORITHM")
    print(f"Random seed: {seed}")
    print(f"Population size: {pop_size} | Max generations: {max_gens}")
    print(f"Tournament size: {tourn_size} | Elitism: {elite_cnt}")
    print(f"Mutation probability: {p_mut_gene} | Depth range: [{depth_min}, {depth_max}]")
    print(f"Stagnation patience: {stagnation_patience}")
    print("=" * 70)

    evaluator = FitnessEvaluator()
    population = initialize_population(pop_size, depth_min, depth_max)

    archive_signatures: Set[str] = set()
    mr_usage_count: Dict[str, int] = {}

    # Initial generational evaluation (deterministic & order-independent)
    evaluator.assign_population_fitness(population, archive_signatures, mr_usage_count)
    for ind in population:
        ind.generation = 0

    best_fitness_history = []
    stagnation_counter = 0
    history_records = []
    all_valid_chromosomes: Dict[str, Chromosome] = {}

    for gen in range(max_gens):
        # Update archive with valid individuals from this generation
        valid_pop = [ind for ind in population if ind.is_valid]
        for ind in valid_pop:
            sig = ind.signature()
            archive_signatures.add(sig)
            if sig not in all_valid_chromosomes or ind.fitness > all_valid_chromosomes[sig].fitness:
                all_valid_chromosomes[sig] = ind
            for g in ind.genes:
                mr_usage_count[g.mr_id] = mr_usage_count.get(g.mr_id, 0) + 1

        fitnesses = [ind.fitness for ind in valid_pop] if valid_pop else [-float("inf")]
        best_ind = max(population, key=lambda ind: ind.fitness)
        avg_fitness = sum(fitnesses) / len(fitnesses) if valid_pop else -float("inf")
        best_fit = best_ind.fitness

        print(f"[Gen {gen:02d}] Best: {best_fit:.4f} | Avg(Valid): {avg_fitness:.4f} | Valid: {len(valid_pop)}/{len(population)} | Unique MRs stored: {len(all_valid_chromosomes)}")
        if best_ind.is_valid:
            print(f"       Top Chain: {best_ind.signature()}")
            print(f"       Objectives: {best_ind.objectives}")

        history_records.append({
            "generation": gen,
            "best_fitness": best_fit,
            "avg_valid_fitness": round(avg_fitness, 4),
            "valid_count": len(valid_pop),
            "total_count": len(population),
            "unique_valid_total": len(all_valid_chromosomes)
        })

        # Check early stopping / stagnation
        if gen > 0:
            if abs(best_fit - best_fitness_history[-1]) < 1e-4:
                stagnation_counter += 1
            else:
                stagnation_counter = 0
            if stagnation_counter >= stagnation_patience:
                print(f"\n[Termination] Early stopping triggered: fitness stagnated for {stagnation_patience} generations.")
                break
        best_fitness_history.append(best_fit)

        if gen == max_gens - 1:
            break

        # Reproduce next generation
        elites = select_elites(population, elite_cnt)
        offspring: List[Chromosome] = []

        selection_pool = valid_pop if len(valid_pop) >= tourn_size else population

        while len(offspring) < (pop_size - elite_cnt):
            p1 = tournament_selection(selection_pool, tourn_size)
            p2 = tournament_selection(selection_pool, tourn_size)
            c1, c2 = crossover(p1, p2, depth_min, depth_max)
            c1 = mutate(c1, p_mut_gene)
            c2 = mutate(c2, p_mut_gene)
            c1.generation = gen + 1
            c2.generation = gen + 1
            offspring.append(c1)
            if len(offspring) < (pop_size - elite_cnt):
                offspring.append(c2)

        # Batch evaluate offspring with frozen archive (deterministic)
        evaluator.assign_population_fitness(offspring, archive_signatures, mr_usage_count)
        population = elites + offspring

    # Save fitness history CSV
    csv_path = os.path.join(results_dir, "fitness_history.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=history_records[0].keys())
        writer.writeheader()
        writer.writerows(history_records)

    # Export all unique valid MR chromosomes to output_dir
    catalog = []
    sorted_chroms = sorted(all_valid_chromosomes.values(), key=lambda c: c.fitness, reverse=True)

    for idx, chrom in enumerate(sorted_chroms, 1):
        mr_json_name = f"composite_mr_{idx:03d}_{chrom.id}.json"
        mr_file_path = os.path.join(output_dir, mr_json_name)
        
        chrom_dict = chrom.to_dict()
        chrom_dict["index"] = idx
        with open(mr_file_path, "w") as f:
            json.dump(chrom_dict, f, indent=2)

        if chrom.generated_code:
            py_file_path = os.path.join(generated_code_dir, f"followup_mr_{idx:03d}.py")
            with open(py_file_path, "w") as f:
                f.write(chrom.generated_code)

        if chrom.qasm3:
            qasm_file_path = os.path.join(generated_code_dir, f"circuit_mr_{idx:03d}.qasm")
            with open(qasm_file_path, "w") as f:
                f.write(chrom.qasm3)

        catalog.append({
            "index": idx,
            "id": chrom.id,
            "signature": chrom.signature(),
            "depth": chrom.depth,
            "fitness": chrom.fitness,
            "objectives": chrom.objectives,
            "genes": [g.to_dict() for g in chrom.genes],
            "json_file": mr_json_name,
            "py_file": f"followup_mr_{idx:03d}.py",
            "qasm_file": f"circuit_mr_{idx:03d}.qasm"
        })

    catalog_path = os.path.join(output_dir, "catalog.json")
    with open(catalog_path, "w") as f:
        json.dump({
            "total_composite_mrs": len(catalog),
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "seed": seed,
            "relations": catalog
        }, f, indent=2)

    # Export Reproducibility Manifest
    import qiskit
    import mqt.core
    manifest_data = {
        "execution_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "random_seed": seed,
        "environment": {
            "python_version": sys.version,
            "qiskit_version": qiskit.__version__,
            "mqt_core_version": mqt.core.__version__
        },
        "ga_parameters": {
            "population_size": pop_size,
            "max_generations": max_gens,
            "tournament_size": tourn_size,
            "elitism_count": elite_cnt,
            "mutation_rate": p_mut_gene,
            "depth_range": [depth_min, depth_max],
            "stagnation_patience": stagnation_patience
        },
        "results_summary": {
            "unique_valid_relations": len(catalog),
            "best_fitness": best_fitness_history[-1] if best_fitness_history else -float("inf")
        }
    }
    manifest_path = os.path.join(results_dir, "run_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest_data, f, indent=2)

    print(f"\nReproducibility manifest written to {manifest_path}")
    print(f"Catalog of composite relations exported to {catalog_path}")
    print("=" * 70)
    print("GA COMPLETED SUCCESSFULLY!")
    print(f"Total new MR relations synthesized: {len(catalog)}")
    print("=" * 70)
    return catalog


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Reproducible Genetic Algorithm for Metamorphic Relations")
    parser.add_argument("--pop_size", type=int, default=80)
    parser.add_argument("--max_gens", type=int, default=15)
    parser.add_argument("--tourn_size", type=int, default=4)
    parser.add_argument("--elite_cnt", type=int, default=4)
    parser.add_argument("--p_mut", type=float, default=0.25)
    parser.add_argument("--stagnation", type=int, default=8)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    run_ga(
        pop_size=args.pop_size,
        max_gens=args.max_gens,
        tourn_size=args.tourn_size,
        elite_cnt=args.elite_cnt,
        p_mut_gene=args.p_mut,
        stagnation_patience=args.stagnation,
        seed=args.seed
    )
