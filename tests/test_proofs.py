import pytest
from verification.proof_engine import verify_algebraic_proofs


def test_algebraic_proofs_zero_error():
    """Verify that all formal gate identities hold with exact symbolic zero difference."""
    proofs = verify_algebraic_proofs()
    assert len(proofs) == 6, "Expected 6 proven gate identities"
    for rule_name, res in proofs.items():
        assert res["is_proven"], f"Proof failed for {rule_name}"
        assert res["symbolic_zero"] is True, f"SymPy matrix difference not zero for {rule_name}"
        assert res["frobenius_error"] == 0.0, f"Error not exactly zero for {rule_name}: {res['frobenius_error']}"
        assert res["tier"] == "EXACT_SYMBOLIC_PROOF"
