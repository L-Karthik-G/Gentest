import os
import sys
import json
import copy
import importlib
from typing import Dict, Any, List, Optional, Tuple

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "MorphQ-Quantum-Qiskit-Testing-ICSE-23"))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

SCHEMA_PATH = os.path.join(os.path.dirname(__file__), "schema.json")
with open(SCHEMA_PATH, "r") as f:
    SCHEMA = json.load(f)

MR_CATALOG = {entry["id"]: entry for entry in SCHEMA.get("morphrelations", [])}


def list_mrs() -> List[str]:
    """Return all available MR identifiers in the library."""
    return list(MR_CATALOG.keys())


def get_mr_info(mr_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve metadata and parameter definitions for an MR."""
    return MR_CATALOG.get(mr_id)


def create_mr(mr_id: str, seed: Optional[int] = None, **param_overrides) -> Any:
    """Instantiate an MR class with given parameter overrides and deterministic seed."""
    info = MR_CATALOG.get(mr_id)
    if not info:
        raise ValueError(f"Unknown MR ID: {mr_id}")
    
    modpath = info["module_path"]
    clsname = info["class_name"]
    mod = importlib.import_module(modpath)
    cls = getattr(mod, clsname)
    
    # Build default config from schema
    base_config = {}
    for p_name, p_meta in info.get("parameters", {}).items():
        base_config[p_name] = copy.deepcopy(p_meta.get("default"))
    
    # Apply overrides
    for k, v in param_overrides.items():
        base_config[k] = v
        
    config_dict = {mr_id: base_config}
    detectors_dict = {"ks": {"name": "ks"}}
    
    instance = cls(mr_id, config_dict, detectors_dict, seed=seed)
    return instance


def apply_mr(mr_id: str, code_of_source: str, seed: Optional[int] = None, **param_overrides) -> Tuple[bool, str, Dict[str, Any]]:
    """Apply a single MR to source code with deterministic seed. Returns (success, transformed_code, metadata)."""
    mr = create_mr(mr_id, seed=seed, **param_overrides)
    if not mr.check_precondition(code_of_source):
        return False, code_of_source, {"error": "precondition_failed"}
    try:
        new_code = mr.derive(code_of_source)
        return True, new_code, getattr(mr, "metadata", {})
    except Exception as e:
        return False, code_of_source, {"error": str(e)}


def apply_mr_chain(code_of_source: str, genes: List[Dict[str, Any]], base_seed: Optional[int] = None) -> Tuple[bool, str, List[Dict[str, Any]]]:
    """Sequentially apply a chain of MR genes with deterministic local seeds."""
    current_code = code_of_source
    logs = []
    for idx, gene in enumerate(genes):
        mr_id = gene["mr_id"]
        params = gene.get("params", {})
        local_seed = None if base_seed is None else ((base_seed + idx * 7919) % (2**31))
        success, next_code, meta = apply_mr(mr_id, current_code, seed=local_seed, **params)
        logs.append({
            "mr_id": mr_id,
            "params": params,
            "success": success,
            "meta": meta
        })
        if not success:
            return False, current_code, logs
        current_code = next_code
    return True, current_code, logs
