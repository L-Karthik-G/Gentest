import pytest
import random
from ga.operators import sample_random_gene, validate_gene_params, crossover, mutate, ALL_MR_IDS
from ga.individual import Gene, Chromosome


def test_coupling_density_invariants():
    """Verify that ChangeCouplingMap never samples min_density > max_density."""
    for _ in range(100):
        gene = sample_random_gene("ChangeCouplingMap")
        assert validate_gene_params(gene), f"Invariant violated: {gene.params}"
        min_d = gene.params["min_connection_density"]
        max_d = gene.params["max_connection_density"]
        assert min_d <= max_d, f"Density violation: min={min_d} > max={max_d}"
        assert gene.params["min_perc_nodes"] <= gene.params["max_perc_nodes"]


def test_validate_gene_params_catches_violation():
    """Verify that the validator rejects illegal parameters."""
    bad_gene = Gene(mr_id="ChangeCouplingMap", params={
        "min_connection_density": 0.25,
        "max_connection_density": 0.10
    })
    assert not validate_gene_params(bad_gene)


def test_crossover_depth_bounds():
    """Verify crossover strictly preserves depth in [2, 3]."""
    p1 = Chromosome(genes=[sample_random_gene() for _ in range(3)])
    p2 = Chromosome(genes=[sample_random_gene() for _ in range(2)])
    for _ in range(50):
        c1, c2 = crossover(p1, p2, depth_min=2, depth_max=3)
        assert 2 <= c1.depth <= 3, f"Child 1 depth out of bounds: {c1.depth}"
        assert 2 <= c2.depth <= 3, f"Child 2 depth out of bounds: {c2.depth}"
