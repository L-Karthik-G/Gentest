import os
import json
import pytest

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "..", "mr_library", "schema.json")


def test_schema_structure_and_types():
    """Verify that schema.json exists, contains 17 MRs, and has correct oracle types."""
    assert os.path.exists(SCHEMA_PATH), "schema.json not found"
    with open(SCHEMA_PATH, "r") as f:
        schema = json.load(f)
    
    assert schema["version"] == "2.0"
    mrs = {entry["id"]: entry for entry in schema["morphrelations"]}
    assert len(mrs) == 17, f"Expected 17 MRs, found {len(mrs)}"
    
    # Check that oracle classifications are correct
    assert mrs["ChangeQubitOrder"]["oracle_type"] == "PERMUTED_EQUIVALENT"
    assert not mrs["ChangeQubitOrder"]["semantic_equivalent"]
    assert mrs["RunIndependentPartitions"]["oracle_type"] == "PARTITIONED_EQUIVALENT"
    assert not mrs["RunIndependentPartitions"]["semantic_equivalent"]
    assert mrs["QdiffG1SwapToCnot"]["oracle_type"] == "DIRECT_EQUIVALENT"
    assert mrs["QdiffG1SwapToCnot"]["semantic_equivalent"]
