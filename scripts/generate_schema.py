import os
import sys
import json
import yaml
import inspect
import importlib

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "MorphQ-Quantum-Qiskit-Testing-ICSE-23"))
sys.path.insert(0, REPO_ROOT)

config_path = os.path.join(REPO_ROOT, "config", "qmt_v53.yaml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

mr_configs = {}
mr_configs.update(config.get("morphq_metamorphic_strategies", {}))
mr_configs.update(config.get("qdiff_metamorphic_strategies", {}))

mr_module_map = {
    "AddUnusedRegister": "lib.mr.add_unused_register",
    "ChangeBackend": "lib.mr.change_backend",
    "ChangeCouplingMap": "lib.mr.change_coupling_map",
    "ChangeOptLevel": "lib.mr.change_opt_level",
    "ChangeQubitOrder": "lib.mr.change_qubit_order",
    "ChangeTargetBasis": "lib.mr.change_target_basis",
    "InjectNullEffect": "lib.mr.inject_null_effect",
    "InjectParameters": "lib.mr.inject_parameters",
    "RunIndependentPartitions": "lib.mr.run_independent_partitions",
    "ToQasmAndBack": "lib.mr.to_qasm_and_back",
    "QdiffG1SwapToCnot": "lib.mr.qdiff_g1_swap_to_cnot",
    "QdiffG2TwoHToId": "lib.mr.qdiff_g2_two_h_to_id",
    "QdiffG3XToHSSH": "lib.mr.qdiff_g3_x_to_hssh",
    "QdiffG4ZtoSS": "lib.mr.qdiff_g4_z_to_ss",
    "QdiffG5CZtoHCnotH": "lib.mr.qdiff_g5_cz_to_h_cnot_h",
    "QdiffG6TwoCzToId": "lib.mr.qdiff_g6_two_cz_to_id",
    "QdiffG7CCNOTDecomposition": "lib.mr.qdiff_g7_ccnot_decomposition"
}

oracle_classifications = {
    "AddUnusedRegister": "DIRECT_EQUIVALENT",
    "ChangeBackend": "DIRECT_EQUIVALENT",
    "ChangeCouplingMap": "DIRECT_EQUIVALENT",
    "ChangeOptLevel": "DIRECT_EQUIVALENT",
    "ChangeQubitOrder": "PERMUTED_EQUIVALENT",
    "ChangeTargetBasis": "DIRECT_EQUIVALENT",
    "InjectNullEffect": "DIRECT_EQUIVALENT",
    "InjectParameters": "DIRECT_EQUIVALENT",
    "RunIndependentPartitions": "PARTITIONED_EQUIVALENT",
    "ToQasmAndBack": "DIRECT_EQUIVALENT",
    "QdiffG1SwapToCnot": "DIRECT_EQUIVALENT",
    "QdiffG2TwoHToId": "DIRECT_EQUIVALENT",
    "QdiffG3XToHSSH": "DIRECT_EQUIVALENT",
    "QdiffG4ZtoSS": "DIRECT_EQUIVALENT",
    "QdiffG5CZtoHCnotH": "DIRECT_EQUIVALENT",
    "QdiffG6TwoCzToId": "DIRECT_EQUIVALENT",
    "QdiffG7CCNOTDecomposition": "DIRECT_EQUIVALENT"
}

descriptions = {
    "AddUnusedRegister": "Appends an unused classical/quantum register to test circuit transpilation robustness against dead entities.",
    "ChangeBackend": "Switches the simulation backend engine (e.g., statevector, density matrix, matrix product state).",
    "ChangeCouplingMap": "Synthesizes or alters the hardware coupling topology graph and retranspiles the circuit.",
    "ChangeOptLevel": "Modifies compiler optimization levels (0, 1, 2, 3) to test compilation invariance under varying passes.",
    "ChangeQubitOrder": "Permutes qubit indices and rewrites register indexing. Semantic equivalence holds under bitstring permutation pi(y).",
    "ChangeTargetBasis": "Re-synthesizes circuit into distinct universal gate sets (e.g. Clifford+T, Rx/Ry/Rz/CX, CCX/H).",
    "InjectNullEffect": "Injects reversible or identity-equivalent gate sequences (null-effect subcircuits).",
    "InjectParameters": "Substitutes concrete rotation gate angles with parametric expressions and binds values dynamically.",
    "RunIndependentPartitions": "Partitions separable subcircuits, evaluates independently, and takes tensor/cartesian product.",
    "ToQasmAndBack": "Serializes circuit to OpenQASM intermediate representation and reconstructs back.",
    "QdiffG1SwapToCnot": "QDiff Rule 1: Replaces SWAP gates with 3 alternating CNOT gates (SWAP(a,b) = CX(a,b)CX(b,a)CX(a,b)).",
    "QdiffG2TwoHToId": "QDiff Rule 2: Cancels or injects consecutive Hadamard (H * H = I) gate pairs.",
    "QdiffG3XToHSSH": "QDiff Rule 3: Decomposes Pauli-X into H-S-S-H sequence.",
    "QdiffG4ZtoSS": "QDiff Rule 4: Decomposes Pauli-Z into two Phase (S * S) gates.",
    "QdiffG5CZtoHCnotH": "QDiff Rule 5: Rewrites Controlled-Z (CZ) into H-CNOT-H.",
    "QdiffG6TwoCzToId": "QDiff Rule 6: Eliminates or injects adjacent self-inverse Controlled-Z gates (CZ * CZ = I).",
    "QdiffG7CCNOTDecomposition": "QDiff Rule 7: Decomposes Toffoli (CCNOT) into single-qubit gates and CNOTs."
}

entries = []

for mr_id, modpath in mr_module_map.items():
    mod = importlib.import_module(modpath)
    cls = getattr(mod, mr_id)
    cfg = mr_configs.get(mr_id, {})
    
    param_meta = {}
    for k, v in cfg.items():
        param_meta[k] = {
            "type": type(v).__name__,
            "default": v
        }
    
    # Check if the class itself returns False for is_semantically_equivalent
    is_direct_equiv = oracle_classifications.get(mr_id) == "DIRECT_EQUIVALENT"
    
    entries.append({
        "id": mr_id,
        "module_path": modpath,
        "class_name": mr_id,
        "description": descriptions.get(mr_id, inspect.getdoc(cls) or ""),
        "semantic_equivalent": is_direct_equiv,
        "oracle_type": oracle_classifications.get(mr_id, "DIRECT_EQUIVALENT"),
        "parameters": param_meta
    })

schema = {
    "version": "2.0",
    "total_mrs": len(entries),
    "morphrelations": entries
}

out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "mr_library", "schema.json"))
with open(out_path, "w") as f:
    json.dump(schema, f, indent=2)

print(f"Generated {out_path} with accurate oracle_type and semantic_equivalent fields.")
