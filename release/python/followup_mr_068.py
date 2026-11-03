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
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(HGate(), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(SwapGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(XGate(), qargs=[qr[2]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(SGate(), qargs=[qr[0]], cargs=[])
qc.append(CZGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(TGate().inverse(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(TGate().inverse(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[2]], cargs=[])
qc.append(TGate(), qargs=[qr[1]], cargs=[])
qc.append(HGate(), qargs=[qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])
qc.append(TGate().inverse(), qargs=[qr[1]], cargs=[])
qc.append(TGate(), qargs=[qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[1]], cargs=[])
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

from qiskit_aer import Aer
backend = Aer.get_backend('aer_simulator')
RESULT = None
