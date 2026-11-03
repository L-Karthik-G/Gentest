import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import itertools
from typing import List, Dict, Any, Tuple
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import (
    HGate, XGate, ZGate, SGate, TGate, CXGate, CZGate, SwapGate, CCXGate
)
from qiskit.quantum_info import Statevector, state_fidelity
import mr_library


def generate_bounded_circuits() -> List[str]:
    """Generates an exhaustive combinatorial test suite of small quantum circuits (<= 4 qubits, depth <= 5)."""
    circuits = []
    
    # 1. Single-qubit canonical sequences (depth 2)
    for g1 in [HGate(), XGate(), ZGate(), SGate(), TGate()]:
        for g2 in [HGate(), XGate(), ZGate(), SGate()]:
            code = f"""# SECTION
# NAME: PROLOGUE
import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append({g1.__class__.__name__}(), qargs=[qr[0]], cargs=[])
qc.append({g2.__class__.__name__}(), qargs=[qr[0]], cargs=[])

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: EXECUTION
RESULT = None
"""
            circuits.append(code)

    # 2. Two-qubit entangling sequences with SWAP, CZ, CX (depth 3 to 4)
    two_q_patterns = [
        ("SwapGate", "HGate", "XGate"),
        ("CZGate", "ZGate", "HGate"),
        ("CXGate", "XGate", "SGate"),
        ("SwapGate", "CZGate", "HGate"),
        ("CXGate", "CZGate", "SwapGate")
    ]
    for g_ent, g_single, g_tail in two_q_patterns:
        ent_stmt = f"qc.append({g_ent}(), qargs=[qr[0], qr[1]], cargs=[])" if g_ent in ["CXGate", "CZGate", "SwapGate"] else f"qc.append({g_ent}(), qargs=[qr[0]], cargs=[])"
        tail_stmt = f"qc.append({g_tail}(), qargs=[qr[0], qr[1]], cargs=[])" if g_tail in ["CXGate", "CZGate", "SwapGate"] else f"qc.append({g_tail}(), qargs=[qr[1]], cargs=[])"
        code = f"""# SECTION
# NAME: PROLOGUE
import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(2, name='qr')
cr = ClassicalRegister(2, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append({g_single}(), qargs=[qr[1]], cargs=[])
{ent_stmt}
{tail_stmt}

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: EXECUTION
RESULT = None
"""
        circuits.append(code)

    # 3. Three-qubit Toffoli / multi-qubit sequences (depth up to 5)
    code_3q_1 = """# SECTION
# NAME: PROLOGUE
import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CZGate(), qargs=[qr[1], qr[2]], cargs=[])

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: EXECUTION
RESULT = None
"""
    circuits.append(code_3q_1)

    code_3q_2 = """# SECTION
# NAME: PROLOGUE
import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[2]], cargs=[])

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: EXECUTION
RESULT = None
"""
    circuits.append(code_3q_2)

    # 4. Four-qubit combinatorial circuits (depth up to 5)
    code_4q_1 = """# SECTION
# NAME: PROLOGUE
import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CZGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[3]], cargs=[])

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: EXECUTION
RESULT = None
"""
    circuits.append(code_4q_1)

    code_4q_2 = """# SECTION
# NAME: PROLOGUE
import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(4, name='qr')
cr = ClassicalRegister(4, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(ZGate(), qargs=[qr[3]], cargs=[])

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: EXECUTION
RESULT = None
"""
    circuits.append(code_4q_2)

    return circuits


BOUNDED_SUITE = generate_bounded_circuits()


def validate_relation_bounded_suite(
    gene_dicts: List[Dict[str, Any]],
    base_seed: int = None
) -> Tuple[bool, int, int, float]:
    """Tests a composite relation on the bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5).
    Returns (passed_bool, tested_count, passed_count, min_fidelity).
    Deterministic seed propagation ensures reproducible evaluations.
    Strict zero-exception masking: any exception or fidelity < 0.999 is counted as failure.
    """
    tested = 0
    passed = 0
    min_fid = 1.0

    for source_code in BOUNDED_SUITE:
        success, transformed_code, logs = mr_library.apply_mr_chain(source_code, gene_dicts, base_seed=base_seed)
        if not success:
            continue  # Precondition does not match this small circuit

        tested += 1
        try:
            loc_orig = {}
            exec(source_code.split("# SECTION\n# NAME: MEASUREMENT")[0], loc_orig)
            qc_orig = loc_orig["qc"]
            sv_orig = Statevector.from_instruction(qc_orig)

            loc_trans = {}
            exec(transformed_code.split("# SECTION\n# NAME: MEASUREMENT")[0], loc_trans)
            qc_trans = loc_trans["qc"]
            
            # Remove classical bits for pure statevector fidelity
            qc_trans_pure = qc_trans.remove_final_measurements(inplace=False) if hasattr(qc_trans, "remove_final_measurements") else qc_trans
            sv_trans = Statevector.from_instruction(qc_trans_pure)

            fid = float(state_fidelity(sv_orig, sv_trans))
            if fid < min_fid:
                min_fid = fid

            if fid >= 0.999:
                passed += 1
        except Exception:
            # Zero-exception masking: an error or dimension mismatch fails statevector check
            min_fid = min(min_fid, 0.0)

    is_suite_pass = (tested > 0 and passed == tested and min_fid >= 0.999)
    return is_suite_pass, tested, passed, min_fid


# Alias for backward compatibility
validate_relation_exhaustively = validate_relation_bounded_suite


if __name__ == "__main__":
    print(f"Loaded {len(BOUNDED_SUITE)} bounded combinatorial test circuits (<= 4 qubits, depth <= 5).")
    test_genes = [{"mr_id": "QdiffG4ZtoSS", "params": {}}]
    passed, tested, p_cnt, fid = validate_relation_bounded_suite(test_genes, base_seed=42)
    print(f"Test QdiffG4ZtoSS: tested on {tested} applicable circuits, passed {p_cnt}/{tested}, min fidelity: {fid:.6f}")
