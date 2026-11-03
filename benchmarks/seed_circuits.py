import re
from typing import Dict
from qiskit import QuantumCircuit
from qiskit.qasm3 import dumps

BENCHMARKS: Dict[str, str] = {}

BENCHMARKS["bell_state"] = """# SECTION
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
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: EXECUTION
from qiskit_aer import Aer
backend = Aer.get_backend('aer_simulator')
RESULT = None
"""

BENCHMARKS["ghz_state"] = """# SECTION
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
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(ZGate(), qargs=[qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: EXECUTION
from qiskit_aer import Aer
backend = Aer.get_backend('aer_simulator')
RESULT = None
"""

BENCHMARKS["qft_4qubit"] = """# SECTION
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
qc.append(PhaseGate(1.5707963267948966), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[3]], cargs=[])
qc.append(HGate(), qargs=[qr[3]], cargs=[])
qc.append(SwapGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[2]], cargs=[])

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2)

# SECTION
# NAME: EXECUTION
from qiskit_aer import Aer
backend = Aer.get_backend('aer_simulator')
RESULT = None
"""

BENCHMARKS["grover_3qubit"] = """# SECTION
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
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: EXECUTION
from qiskit_aer import Aer
backend = Aer.get_backend('aer_simulator')
RESULT = None
"""

BENCHMARKS["adder_3qubit"] = """# SECTION
# NAME: PROLOGUE
import qiskit
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.circuit.library.standard_gates import *

# SECTION
# NAME: CIRCUIT
qr = QuantumRegister(3, name='qr')
cr = ClassicalRegister(3, name='cr')
qc = QuantumCircuit(qr, cr, name='qc')
qc.append(XGate(), qargs=[qr[0]], cargs=[])
qc.append(XGate(), qargs=[qr[1]], cargs=[])
qc.append(CCXGate(), qargs=[qr[0], qr[1], qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])

# SECTION
# NAME: MEASUREMENT
qc.measure(qr, cr)

# SECTION
# NAME: OPTIMIZATION_PASSES
passmanager = None

# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=1)

# SECTION
# NAME: EXECUTION
from qiskit_aer import Aer
backend = Aer.get_backend('aer_simulator')
RESULT = None
"""


def get_benchmark(name: str) -> str:
    """Return benchmark Python source code by name."""
    if name not in BENCHMARKS:
        raise KeyError(f"Unknown benchmark: {name}. Available: {list(BENCHMARKS.keys())}")
    return BENCHMARKS[name]


def extract_circuit_and_qasm3(program_code: str):
    """Executes code up to the EXECUTION section and exports the QuantumCircuit to OpenQASM 3.0."""
    code_to_exec = program_code.split("# SECTION\n# NAME: EXECUTION")[0]
    loc = {}
    exec(code_to_exec, loc)
    qc = loc.get("qc")
    if not isinstance(qc, QuantumCircuit):
        raise ValueError("Code did not produce a QuantumCircuit named 'qc'")
    qasm3_str = dumps(qc)
    return qc, qasm3_str
