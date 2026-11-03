# SECTION
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
# NAME: OPTIMIZATION_PASSES

passmanager = None
# SECTION
# NAME: OPTIMIZATION_LEVEL
from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2)# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: EXECUTION

from qiskit_aer import Aer
backend = Aer.get_backend('aer_simulator')
RESULT = None
