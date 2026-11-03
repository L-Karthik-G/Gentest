import pytest
from verification.exhaustive_enumerator import validate_relation_bounded_suite
from verification.empirical_simulator import run_empirical_validation


def test_audit_evaluations_are_deterministic():
    test_genes = [
        {"mr_id": "QdiffG4ZtoSS", "params": {"min_to_change": 1, "max_to_change": 1}},
        {"mr_id": "ChangeOptLevel", "params": {"levels": [0, 2, 3]}}
    ]
    seed = 12345

    # Run bounded suite validation twice with the same seed
    pass1, test1, p_cnt1, fid1 = validate_relation_bounded_suite(test_genes, base_seed=seed)
    pass2, test2, p_cnt2, fid2 = validate_relation_bounded_suite(test_genes, base_seed=seed)

    assert pass1 == pass2
    assert test1 == test2
    assert p_cnt1 == p_cnt2
    assert fid1 == fid2, f"Statevector fidelities must be strictly identical: {fid1} vs {fid2}"

    # Run empirical multi-circuit simulation twice with the same seed
    emp_ok1, msg1, det1 = run_empirical_validation(test_genes, shots=2048, base_seed=seed)
    emp_ok2, msg2, det2 = run_empirical_validation(test_genes, shots=2048, base_seed=seed)

    assert emp_ok1 == emp_ok2
    assert msg1 == msg2
    assert det1["benchmarks_tested"] == det2["benchmarks_tested"]
    assert det1["benchmarks_passed"] == det2["benchmarks_passed"]
