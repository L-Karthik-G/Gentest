# SECTION
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
qc.append(CXGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CXGate(), qargs=[qr[3], qr[0]], cargs=[])
qc.append(CXGate(), qargs=[qr[0], qr[3]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])
qc.append(CXGate(), qargs=[qr[2], qr[1]], cargs=[])
qc.append(CXGate(), qargs=[qr[1], qr[2]], cargs=[])# SECTION
# NAME: OPTIMIZATION_PASSES

passmanager = None
# SECTION
# NAME: OPTIMIZATION_LEVEL

from qiskit import transpile
qc = transpile(qc, basis_gates=None, optimization_level=2)
# SECTION
# NAME: MEASUREMENT

qc.measure(qr, cr)
# SECTION
# NAME: EXECUTION

from qiskit_aer import Aer
backend = Aer.get_backend(np.str_('statevector_simulator'))
RESULT = None
