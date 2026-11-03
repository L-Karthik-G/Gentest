import os
import sys
import json
from mqt.core.mlir import compile_program
from mqt.core.qdmi import ProgramFormat, open_device

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import mr_library
from benchmarks.seed_circuits import BENCHMARKS, extract_circuit_and_qasm3

device = open_device("mqt.ddsim.default")

# 1. Test Initial Primitive MRs
schema_path = os.path.join(PROJECT_ROOT, "mr_library", "schema.json")
with open(schema_path, "r") as f:
    schema = json.load(f)

seed_code = BENCHMARKS["ghz_state"]
primitive_results = []

for mr_meta in schema.get("morphrelations", []):
    mr_id = mr_meta["id"]
    success, derived_code, meta = mr_library.apply_mr(mr_id, seed_code)
    
    mqt_ok = False
    qasm_str = ""
    err_str = ""
    
    if success:
        try:
            qc, qasm_str = extract_circuit_and_qasm3(derived_code)
            _ = compile_program(qasm_str, target=device, program_format=ProgramFormat.QASM3)
            mqt_ok = True
        except Exception as e:
            err_str = str(e)
    else:
        err_str = meta.get("error", "precondition_unmet_on_template")

    primitive_results.append({
        "id": mr_id,
        "description": mr_meta["description"],
        "parameters": mr_meta["parameters"],
        "applied_on_ghz": success,
        "mqt_cc_compiled": mqt_ok,
        "error": err_str
    })

# 2. Test Generated Composite MRs
catalog_path = os.path.join(PROJECT_ROOT, "mr_library", "generated_mrs", "catalog.json")
with open(catalog_path, "r") as f:
    catalog = json.load(f)

composite_results = []
for rel in catalog.get("relations", [])[:30]:  # Top 30 composite MRs
    qasm_file = os.path.join(PROJECT_ROOT, "generated", rel["qasm_file"])
    with open(qasm_file, "r") as f:
        qasm_code = f.read()
    
    mqt_valid = False
    try:
        _ = compile_program(qasm_code, target=device, program_format=ProgramFormat.QASM3)
        mqt_valid = True
    except Exception as e:
        mqt_valid = False

    composite_results.append({
        "index": rel["index"],
        "id": rel["id"],
        "signature": rel["signature"],
        "depth": rel["depth"],
        "fitness": rel["fitness"],
        "objectives": rel["objectives"],
        "mqt_cc_compiled": mqt_valid
    })

verification_summary = {
    "primitive_mrs_count": len(primitive_results),
    "primitive_results": primitive_results,
    "composite_mrs_count": len(catalog.get("relations", [])),
    "top_composite_samples": composite_results
}

out_summary_path = os.path.join(PROJECT_ROOT, "results", "verification_summary.json")
with open(out_summary_path, "w") as f:
    json.dump(verification_summary, f, indent=2)

print(f"Verified {len(primitive_results)} primitive MRs and composite MR catalog.")
print(f"Summary written to {out_summary_path}")
