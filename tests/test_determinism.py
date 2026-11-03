import pytest
from ga.individual import Chromosome, Gene
from ga.fitness import FitnessEvaluator


def test_chromosome_evaluation_determinism():
    evaluator = FitnessEvaluator(benchmarks=["bell_state", "ghz_state"])

    # Define a chromosome with deterministic gene parameters
    genes1 = [
        Gene(mr_id="QdiffG4ZtoSS", params={}),
        Gene(mr_id="ChangeOptLevel", params={"levels": [0, 2, 3]})
    ]
    chrom1 = Chromosome(genes=genes1)

    evaluator.evaluate_individual_stateless(chrom1)
    assert chrom1.is_valid is True
    first_code = chrom1.generated_code
    first_objs = dict(chrom1.objectives)

    # Re-evaluate a fresh chromosome with identical genes
    genes2 = [
        Gene(mr_id="QdiffG4ZtoSS", params={}),
        Gene(mr_id="ChangeOptLevel", params={"levels": [0, 2, 3]})
    ]
    chrom2 = Chromosome(genes=genes2)
    evaluator.evaluate_individual_stateless(chrom2)

    assert chrom2.is_valid is True
    assert chrom2.generated_code == first_code, "Generated code must be strictly identical across runs"
    assert chrom2.objectives["cost_efficiency"] == first_objs["cost_efficiency"]
    assert chrom2.objectives["coverage"] == first_objs["coverage"]
    assert chrom2.objectives["unique_gates"] == first_objs["unique_gates"]
