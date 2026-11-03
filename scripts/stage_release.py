import os
import shutil
import json

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CATALOG_PATH = os.path.join(PROJECT_ROOT, "mr_library", "generated_mrs", "pruned_essential_catalog.json")
MANIFEST_PATH = os.path.join(PROJECT_ROOT, "results", "certified_audit_manifest.json")

with open(CATALOG_PATH) as f:
    catalog = json.load(f)

essential_rels = catalog["relations"]
print(f"Staging release for {len(essential_rels)} essential relations...")

RELEASE_DIR = os.path.join(PROJECT_ROOT, "release")
RELEASE_JSON_DIR = os.path.join(RELEASE_DIR, "json")
RELEASE_QASM_DIR = os.path.join(RELEASE_DIR, "qasm")
RELEASE_PY_DIR = os.path.join(RELEASE_DIR, "python")

# Create clean release directories
for d in [RELEASE_JSON_DIR, RELEASE_QASM_DIR, RELEASE_PY_DIR]:
    os.makedirs(d, exist_ok=True)

# Copy release catalogs and manifests
shutil.copy2(CATALOG_PATH, os.path.join(RELEASE_DIR, "pruned_essential_catalog.json"))
shutil.copy2(MANIFEST_PATH, os.path.join(RELEASE_DIR, "certified_audit_manifest.json"))

essential_json_names = set()
essential_qasm_names = set()
essential_py_names = set()

for r in essential_rels:
    # 1. JSON file
    src_json = os.path.join(PROJECT_ROOT, "mr_library", "generated_mrs", r["json_file"])
    dst_json = os.path.join(RELEASE_JSON_DIR, r["json_file"])
    if os.path.exists(src_json):
        shutil.copy2(src_json, dst_json)
        essential_json_names.add(r["json_file"])

    # 2. QASM file
    src_qasm = os.path.join(PROJECT_ROOT, "generated", r["qasm_file"])
    dst_qasm = os.path.join(RELEASE_QASM_DIR, r["qasm_file"])
    if os.path.exists(src_qasm):
        shutil.copy2(src_qasm, dst_qasm)
        essential_qasm_names.add(r["qasm_file"])

    # 3. Python followup file
    src_py = os.path.join(PROJECT_ROOT, "generated", r["py_file"])
    dst_py = os.path.join(RELEASE_PY_DIR, r["py_file"])
    if os.path.exists(src_py):
        shutil.copy2(src_py, dst_py)
        essential_py_names.add(r["py_file"])

print(f"Staged {len(os.listdir(RELEASE_JSON_DIR))} JSON files in {RELEASE_JSON_DIR}")
print(f"Staged {len(os.listdir(RELEASE_QASM_DIR))} QASM files in {RELEASE_QASM_DIR}")
print(f"Staged {len(os.listdir(RELEASE_PY_DIR))} Python files in {RELEASE_PY_DIR}")

# Archive raw candidates (non-essential artifacts)
ARCHIVE_DIR = os.path.join(PROJECT_ROOT, "archive", "raw_candidates")
ARCHIVE_JSON_DIR = os.path.join(ARCHIVE_DIR, "json")
ARCHIVE_GEN_DIR = os.path.join(ARCHIVE_DIR, "generated")
os.makedirs(ARCHIVE_JSON_DIR, exist_ok=True)
os.makedirs(ARCHIVE_GEN_DIR, exist_ok=True)

raw_gen_dir = os.path.join(PROJECT_ROOT, "mr_library", "generated_mrs")
for fname in os.listdir(raw_gen_dir):
    if fname.startswith("composite_mr_") and fname not in essential_json_names:
        shutil.move(os.path.join(raw_gen_dir, fname), os.path.join(ARCHIVE_JSON_DIR, fname))

raw_code_dir = os.path.join(PROJECT_ROOT, "generated")
for fname in os.listdir(raw_code_dir):
    if (fname.startswith("circuit_mr_") and fname not in essential_qasm_names) or \
       (fname.startswith("followup_mr_") and fname not in essential_py_names):
        shutil.move(os.path.join(raw_code_dir, fname), os.path.join(ARCHIVE_GEN_DIR, fname))

print(f"Archived unpruned candidate artifacts to {ARCHIVE_DIR}")
print("Release staging complete and clean!")
