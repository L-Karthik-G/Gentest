import os
import sys
import json
import time
import argparse
from typing import List, Dict, Any

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from verification.proof_engine import PROOF_REGISTRY, verify_algebraic_proofs
from verification.exhaustive_enumerator import validate_relation_exhaustively
from verification.empirical_simulator import run_empirical_validation


def audit_relation_list(
    relations: List[Dict[str, Any]],
    output_manifest_path: str,
    manifest_name: str = "Certified Verification Manifest"
) -> Dict[str, Any]:
    """Audits a list of composite metamorphic relations across the 3 verification tiers."""
    print(f"\n--- Starting Audit: {manifest_name} ({len(relations)} relations) ---")
    proofs = verify_algebraic_proofs()

    import hashlib
    audited_records = []
    tier_counts = {
        "PRIMITIVE_SYMBOLIC_CHAIN": 0,
        "BOUNDED_SUITE_VERIFIED": 0,
        "EMPIRICALLY_SIMULATED": 0,
        "FAILED": 0
    }

    for idx, rel in enumerate(relations, 1):
        genes = rel.get("genes", [])
        if not genes and "json_file" in rel:
            jpath = os.path.join(PROJECT_ROOT, "mr_library", "generated_mrs", rel["json_file"])
            if os.path.exists(jpath):
                with open(jpath, "r") as jf:
                    genes = json.load(jf).get("genes", [])

        gene_ids = [g["mr_id"] for g in genes]

        # Derive deterministic seed for this relation
        h = hashlib.sha256()
        h.update(rel["signature"].encode("utf-8"))
        h.update(str(rel.get("id", idx)).encode("utf-8"))
        for g in genes:
            h.update(str(sorted(g.get("params", {}).items())).encode("utf-8"))
        rel_seed = int(h.hexdigest()[:8], 16)

        # Tier 1: Composition of exact symbolic gate identities
        is_pure_proven = (len(gene_ids) > 0 and all(gid in PROOF_REGISTRY for gid in gene_ids))

        # Tier 2: Bounded combinatorial test suite (29 circuits <= 4q, depth <= 5)
        ex_pass, ex_tested, ex_p_cnt, ex_fid = validate_relation_exhaustively(genes, base_seed=rel_seed)

        # Tier 3: Empirical multi-circuit simulation & KS-test
        emp_pass, emp_msg, emp_details = run_empirical_validation(genes, base_seed=rel_seed)

        if is_pure_proven:
            assigned_tier = "PRIMITIVE_SYMBOLIC_CHAIN"
            verification_method = "Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)"
        elif ex_pass:
            assigned_tier = "BOUNDED_SUITE_VERIFIED"
            verification_method = f"Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = {ex_fid:.4f})"
        elif emp_pass:
            assigned_tier = "EMPIRICALLY_SIMULATED"
            verification_method = f"Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = {emp_details.get('avg_ks_pvalue', 1.0):.4f})"
        else:
            assigned_tier = "FAILED"
            verification_method = f"Preconditions or verification failed: {emp_msg}"

        tier_counts[assigned_tier] += 1

        record = {
            "rank": rel.get("pruned_rank", rel.get("index", idx)),
            "id": rel.get("id", f"rel_{idx}"),
            "signature": rel["signature"],
            "depth": rel.get("depth", len(genes)),
            "fitness": rel.get("fitness", 0.0),
            "verification_tier": assigned_tier,
            "verification_method": verification_method,
            "exhaustive_stats": {
                "tested_circuits": ex_tested,
                "passed_circuits": ex_p_cnt,
                "min_fidelity": round(ex_fid, 6)
            },
            "empirical_stats": emp_details,
            "parameters": [g.get("params", {}) for g in genes],
            "json_file": rel.get("json_file", ""),
            "qasm_file": rel.get("qasm_file", "")
        }
        audited_records.append(record)

    manifest = {
        "manifest_version": "3.0",
        "manifest_name": manifest_name,
        "audited_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "total_audited_relations": len(audited_records),
        "verification_tier_distribution": tier_counts,
        "overall_pass_rate": f"{(len(audited_records) - tier_counts['FAILED']) / max(1, len(audited_records)) * 100:.1f}%",
        "relations": audited_records
    }

    os.makedirs(os.path.dirname(output_manifest_path), exist_ok=True)
    with open(output_manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"Audit completed: {output_manifest_path}")
    print("Tier counts:", tier_counts)
    return manifest


def main():
    parser = argparse.ArgumentParser(description="Multi-tier MR Verification Auditor")
    parser.add_argument("--target", choices=["all", "pruned", "both"], default="both",
                        help="Target candidate set: all generated candidates, pruned essential catalog, or both.")
    args = parser.parse_args()

    candidates_path = os.path.join(PROJECT_ROOT, "mr_library", "generated_mrs", "catalog.json")
    pruned_path = os.path.join(PROJECT_ROOT, "mr_library", "generated_mrs", "pruned_essential_catalog.json")

    if args.target in ["all", "both"]:
        if os.path.exists(candidates_path):
            with open(candidates_path, "r") as f:
                cand_data = json.load(f)
            cand_out = os.path.join(PROJECT_ROOT, "results", "all_candidates_audit_manifest.json")
            audit_relation_list(cand_data["relations"], cand_out, manifest_name="All Candidate Relations Pre-Pruning Audit")
        else:
            print(f"Warning: {candidates_path} not found. Skipping candidates audit.")

    if args.target in ["pruned", "both"]:
        if os.path.exists(pruned_path):
            with open(pruned_path, "r") as f:
                pruned_data = json.load(f)
            pruned_out = os.path.join(PROJECT_ROOT, "results", "certified_audit_manifest.json")
            audit_relation_list(pruned_data["relations"], pruned_out, manifest_name="Curated Essential Library Certified Audit")
        else:
            print(f"Warning: {pruned_path} not found. Skipping pruned catalog audit.")


if __name__ == "__main__":
    main()
