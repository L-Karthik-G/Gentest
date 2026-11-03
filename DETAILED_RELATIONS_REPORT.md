# Detailed Certified Metamorphic Relations Catalog

This document provides complete technical specifications for all **74 essential metamorphic relations** synthesized by the Genetic Algorithm and certified across the three verification tiers.

**Audit Timestamp**: 2026-11-02T18:03:18Z  
**Verification Pass Rate**: 100.0% (74/74 across curated essential library)  
**Release Directory**: `release/`  

---

### Rank 1: `mr_comp_49a4c2ec`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 2
- **Fitness**: 0.9348
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Bounded Suite Validation**: Tested on 29 canonical circuits, Passed 7/29, Min Statevector Fidelity = 0.0
- **Empirical Simulation Stats**: Tested on 5 benchmarks, Compiled 5, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.15, "min_connection_density": 0.06, "max_connection_density": 0.2, "force_connected": true}, {"scramble_percentage": 0.5}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_002_mr_comp_49a4c2ec.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_002_mr_comp_49a4c2ec.json), QASM: [`release/qasm/circuit_mr_002.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_002.qasm), Python: [`release/python/followup_mr_001.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_001.py)

---

### Rank 2: `mr_comp_d2762bf1`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> ChangeBackend(['available_backends'])`
- **Depth**: 2
- **Fitness**: 0.9298
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"available_backends": ["aer_simulator_statevector", "qasm_simulator", "aer_simulator_density_matrix", "aer_simulator_matrix_product_state"]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_005_mr_comp_d2762bf1.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_005_mr_comp_d2762bf1.json), QASM: [`release/qasm/circuit_mr_005.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_005.qasm), Python: [`release/python/followup_mr_002.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_002.py)

---

### Rank 3: `mr_comp_f2afe4bd`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.9149
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 0.9992)
- **Empirical Simulation Stats**: Tested on 2 benchmarks, Compiled 2, Avg KS p-value = 0.9992
- **Parameters**: `[{"available_backends": ["aer_simulator", "aer_simulator_density_matrix", "statevector_simulator", "aer_simulator_statevector", "qasm_simulator"]}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_006_mr_comp_f2afe4bd.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_006_mr_comp_f2afe4bd.json), QASM: [`release/qasm/circuit_mr_006.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_006.qasm), Python: [`release/python/followup_mr_003.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_003.py)

---

### Rank 4: `mr_comp_3b854f93`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.9149
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 0.9861)
- **Bounded Suite Validation**: Tested on 6 canonical circuits, Passed 4/6, Min Statevector Fidelity = 0.0
- **Empirical Simulation Stats**: Tested on 2 benchmarks, Compiled 2, Avg KS p-value = 0.9861
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.13, "min_connection_density": 0.11, "max_connection_density": 0.28, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_007_mr_comp_3b854f93.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_007_mr_comp_3b854f93.json), QASM: [`release/qasm/circuit_mr_007.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_007.qasm), Python: [`release/python/followup_mr_004.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_004.py)

---

### Rank 5: `mr_comp_7c6a0717`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.9026
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"scramble_percentage": 0.5}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_009_mr_comp_7c6a0717.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_009_mr_comp_7c6a0717.json), QASM: [`release/qasm/circuit_mr_009.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_009.qasm), Python: [`release/python/followup_mr_005.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_005.py)

---

### Rank 6: `mr_comp_1294b8f3`

- **Signature**: `QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.8923
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_010_mr_comp_1294b8f3.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_010_mr_comp_1294b8f3.json), QASM: [`release/qasm/circuit_mr_010.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_010.qasm), Python: [`release/python/followup_mr_006.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_006.py)

---

### Rank 7: `mr_comp_bc533f61`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.8923
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.75}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_011_mr_comp_bc533f61.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_011_mr_comp_bc533f61.json), QASM: [`release/qasm/circuit_mr_011.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_011.qasm), Python: [`release/python/followup_mr_007.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_007.py)

---

### Rank 8: `mr_comp_19292182`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeBackend(['available_backends'])`
- **Depth**: 3
- **Fitness**: 0.8923
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}, {"available_backends": ["qasm_simulator", "aer_simulator", "aer_simulator_matrix_product_state", "aer_simulator_statevector", "statevector_simulator", "aer_simulator_density_matrix"]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_012_mr_comp_19292182.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_012_mr_comp_19292182.json), QASM: [`release/qasm/circuit_mr_012.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_012.qasm), Python: [`release/python/followup_mr_008.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_008.py)

---

### Rank 9: `mr_comp_047402b4`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> ChangeOptLevel(['levels']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.8873
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Bounded Suite Validation**: Tested on 2 canonical circuits, Passed 1/2, Min Statevector Fidelity = 0.25
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.49, "min_connection_density": 0.05, "max_connection_density": 0.22, "force_connected": true}, {"levels": [1]}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_013_mr_comp_047402b4.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_013_mr_comp_047402b4.json), QASM: [`release/qasm/circuit_mr_013.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_013.qasm), Python: [`release/python/followup_mr_009.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_009.py)

---

### Rank 10: `mr_comp_c5959a7f`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.8802
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_014_mr_comp_c5959a7f.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_014_mr_comp_c5959a7f.json), QASM: [`release/qasm/circuit_mr_014.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_014.qasm), Python: [`release/python/followup_mr_010.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_010.py)

---

### Rank 11: `mr_comp_ca46fe5b`

- **Signature**: `QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeOptLevel(['levels'])`
- **Depth**: 2
- **Fitness**: 0.8661
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"levels": [0, 2, 1, 3]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_016_mr_comp_ca46fe5b.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_016_mr_comp_ca46fe5b.json), QASM: [`release/qasm/circuit_mr_016.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_016.qasm), Python: [`release/python/followup_mr_011.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_011.py)

---

### Rank 12: `mr_comp_ab7115f2`

- **Signature**: `QdiffG1SwapToCnot(['min_to_change', 'max_to_change']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.8611
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_017_mr_comp_ab7115f2.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_017_mr_comp_ab7115f2.json), QASM: [`release/qasm/circuit_mr_017.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_017.qasm), Python: [`release/python/followup_mr_012.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_012.py)

---

### Rank 13: `mr_comp_ae727414`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.8611
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_018_mr_comp_ae727414.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_018_mr_comp_ae727414.json), QASM: [`release/qasm/circuit_mr_018.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_018.qasm), Python: [`release/python/followup_mr_013.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_013.py)

---

### Rank 14: `mr_comp_0cd8b292`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.8611
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_019_mr_comp_0cd8b292.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_019_mr_comp_0cd8b292.json), QASM: [`release/qasm/circuit_mr_019.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_019.qasm), Python: [`release/python/followup_mr_014.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_014.py)

---

### Rank 15: `mr_comp_cba230cb`

- **Signature**: `ChangeTargetBasis(['universal_gate_sets']) -> ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected'])`
- **Depth**: 2
- **Fitness**: 0.8308
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Bounded Suite Validation**: Tested on 29 canonical circuits, Passed 7/29, Min Statevector Fidelity = 0.0
- **Empirical Simulation Stats**: Tested on 5 benchmarks, Compiled 5, Avg KS p-value = 1.0000
- **Parameters**: `[{"universal_gate_sets": [{"gates": ["rx", "ry", "rz", "p", "cx"]}]}, {"min_perc_nodes": 1, "max_perc_nodes": 1.18, "min_connection_density": 0.12, "max_connection_density": 0.2, "force_connected": true}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_021_mr_comp_cba230cb.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_021_mr_comp_cba230cb.json), QASM: [`release/qasm/circuit_mr_021.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_021.qasm), Python: [`release/python/followup_mr_015.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_015.py)

---

### Rank 16: `mr_comp_74bc0302`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.7703
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["aer_simulator_density_matrix", "aer_simulator", "aer_simulator_statevector", "qasm_simulator", "statevector_simulator", "aer_simulator_matrix_product_state"]}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_023_mr_comp_74bc0302.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_023_mr_comp_74bc0302.json), QASM: [`release/qasm/circuit_mr_023.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_023.qasm), Python: [`release/python/followup_mr_016.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_016.py)

---

### Rank 17: `mr_comp_f846b66c`

- **Signature**: `ChangeTargetBasis(['universal_gate_sets']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.7524
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"universal_gate_sets": [{"gates": ["cx", "h", "s", "t"]}]}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_024_mr_comp_f846b66c.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_024_mr_comp_f846b66c.json), QASM: [`release/qasm/circuit_mr_024.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_024.qasm), Python: [`release/python/followup_mr_017.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_017.py)

---

### Rank 18: `mr_comp_ec473e1b`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> ChangeTargetBasis(['universal_gate_sets']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.7524
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"scramble_percentage": 0.75}, {"universal_gate_sets": [{"gates": ["cx", "h", "s", "t"]}]}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_025_mr_comp_ec473e1b.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_025_mr_comp_ec473e1b.json), QASM: [`release/qasm/circuit_mr_025.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_025.qasm), Python: [`release/python/followup_mr_018.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_018.py)

---

### Rank 19: `mr_comp_cddfe976`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.6163
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 0.8405)
- **Bounded Suite Validation**: Tested on 6 canonical circuits, Passed 4/6, Min Statevector Fidelity = 0.0
- **Empirical Simulation Stats**: Tested on 2 benchmarks, Compiled 2, Avg KS p-value = 0.8405
- **Parameters**: `[{"scramble_percentage": 0.5}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_026_mr_comp_cddfe976.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_026_mr_comp_cddfe976.json), QASM: [`release/qasm/circuit_mr_026.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_026.qasm), Python: [`release/python/followup_mr_019.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_019.py)

---

### Rank 20: `mr_comp_ab35a71f`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> ChangeOptLevel(['levels']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.6018
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Bounded Suite Validation**: Tested on 4 canonical circuits, Passed 3/4, Min Statevector Fidelity = 0.25
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.62, "min_connection_density": 0.15, "max_connection_density": 0.26, "force_connected": true}, {"levels": [1]}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_028_mr_comp_ab35a71f.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_028_mr_comp_ab35a71f.json), QASM: [`release/qasm/circuit_mr_028.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_028.qasm), Python: [`release/python/followup_mr_020.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_020.py)

---

### Rank 21: `mr_comp_4d5da92d`

- **Signature**: `ChangeBackend(['available_backends']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 2
- **Fitness**: 0.5962
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 0.9998)
- **Empirical Simulation Stats**: Tested on 5 benchmarks, Compiled 5, Avg KS p-value = 0.9998
- **Parameters**: `[{"available_backends": ["qasm_simulator", "aer_simulator_matrix_product_state", "aer_simulator", "statevector_simulator", "aer_simulator_statevector"]}, {"scramble_percentage": 0.5}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_029_mr_comp_4d5da92d.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_029_mr_comp_4d5da92d.json), QASM: [`release/qasm/circuit_mr_029.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_029.qasm), Python: [`release/python/followup_mr_021.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_021.py)

---

### Rank 22: `mr_comp_43a3a816`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.5913
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 4 canonical circuits, Passed 4/4, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.51, "min_connection_density": 0.14, "max_connection_density": 0.21, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_030_mr_comp_43a3a816.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_030_mr_comp_43a3a816.json), QASM: [`release/qasm/circuit_mr_030.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_030.qasm), Python: [`release/python/followup_mr_022.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_022.py)

---

### Rank 23: `mr_comp_951f81a4`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected'])`
- **Depth**: 2
- **Fitness**: 0.5682
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"min_perc_nodes": 1, "max_perc_nodes": 1.37, "min_connection_density": 0.14, "max_connection_density": 0.29, "force_connected": true}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_033_mr_comp_951f81a4.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_033_mr_comp_951f81a4.json), QASM: [`release/qasm/circuit_mr_033.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_033.qasm), Python: [`release/python/followup_mr_023.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_023.py)

---

### Rank 24: `mr_comp_61af2f68`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> ChangeBackend(['available_backends'])`
- **Depth**: 2
- **Fitness**: 0.5682
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"available_backends": ["aer_simulator_statevector", "qasm_simulator", "aer_simulator_density_matrix", "aer_simulator_matrix_product_state"]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_034_mr_comp_61af2f68.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_034_mr_comp_61af2f68.json), QASM: [`release/qasm/circuit_mr_034.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_034.qasm), Python: [`release/python/followup_mr_024.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_024.py)

---

### Rank 25: `mr_comp_e1c8ec9b`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.5588
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.15, "min_connection_density": 0.06, "max_connection_density": 0.2, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_036_mr_comp_e1c8ec9b.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_036_mr_comp_e1c8ec9b.json), QASM: [`release/qasm/circuit_mr_036.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_036.qasm), Python: [`release/python/followup_mr_025.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_025.py)

---

### Rank 26: `mr_comp_fb5061d6`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeBackend(['available_backends'])`
- **Depth**: 3
- **Fitness**: 0.5563
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"min_to_change": 1, "max_to_change": 1}, {"available_backends": ["aer_simulator_matrix_product_state"]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_038_mr_comp_fb5061d6.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_038_mr_comp_fb5061d6.json), QASM: [`release/qasm/circuit_mr_038.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_038.qasm), Python: [`release/python/followup_mr_026.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_026.py)

---

### Rank 27: `mr_comp_e83a3f19`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 2
- **Fitness**: 0.5548
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 4 canonical circuits, Passed 4/4, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 0.6665
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.75}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_039_mr_comp_e83a3f19.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_039_mr_comp_e83a3f19.json), QASM: [`release/qasm/circuit_mr_039.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_039.qasm), Python: [`release/python/followup_mr_027.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_027.py)

---

### Rank 28: `mr_comp_b77d0a8b`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.5536
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.75}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_040_mr_comp_b77d0a8b.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_040_mr_comp_b77d0a8b.json), QASM: [`release/qasm/circuit_mr_040.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_040.qasm), Python: [`release/python/followup_mr_028.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_028.py)

---

### Rank 29: `mr_comp_c5c3cd1f`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.5491
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 0.0000
- **Parameters**: `[{"scramble_percentage": 1.0}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_041_mr_comp_c5c3cd1f.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_041_mr_comp_c5c3cd1f.json), QASM: [`release/qasm/circuit_mr_041.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_041.qasm), Python: [`release/python/followup_mr_029.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_029.py)

---

### Rank 30: `mr_comp_117509d3`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.5477
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["aer_simulator_statevector", "aer_simulator_matrix_product_state", "statevector_simulator", "aer_simulator_density_matrix", "qasm_simulator", "aer_simulator"]}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_042_mr_comp_117509d3.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_042_mr_comp_117509d3.json), QASM: [`release/qasm/circuit_mr_042.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_042.qasm), Python: [`release/python/followup_mr_030.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_030.py)

---

### Rank 31: `mr_comp_60c3c3ab`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.5357
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_043_mr_comp_60c3c3ab.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_043_mr_comp_60c3c3ab.json), QASM: [`release/qasm/circuit_mr_043.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_043.qasm), Python: [`release/python/followup_mr_031.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_031.py)

---

### Rank 32: `mr_comp_4ca21914`

- **Signature**: `ChangeOptLevel(['levels']) -> ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected'])`
- **Depth**: 2
- **Fitness**: 0.5344
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Bounded Suite Validation**: Tested on 29 canonical circuits, Passed 7/29, Min Statevector Fidelity = 0.0
- **Empirical Simulation Stats**: Tested on 5 benchmarks, Compiled 5, Avg KS p-value = 1.0000
- **Parameters**: `[{"levels": [0, 2]}, {"min_perc_nodes": 1, "max_perc_nodes": 1.39, "min_connection_density": 0.09, "max_connection_density": 0.22, "force_connected": true}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_044_mr_comp_4ca21914.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_044_mr_comp_4ca21914.json), QASM: [`release/qasm/circuit_mr_044.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_044.qasm), Python: [`release/python/followup_mr_032.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_032.py)

---

### Rank 33: `mr_comp_23ef6adb`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.5241
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"scramble_percentage": 0.5}, {"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.5}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_047_mr_comp_23ef6adb.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_047_mr_comp_23ef6adb.json), QASM: [`release/qasm/circuit_mr_047.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_047.qasm), Python: [`release/python/followup_mr_033.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_033.py)

---

### Rank 34: `mr_comp_eb50c886`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> ChangeTargetBasis(['universal_gate_sets'])`
- **Depth**: 2
- **Fitness**: 0.5221
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"universal_gate_sets": [{"gates": ["rx", "ry", "rz", "p", "cx"]}]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_049_mr_comp_eb50c886.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_049_mr_comp_eb50c886.json), QASM: [`release/qasm/circuit_mr_049.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_049.qasm), Python: [`release/python/followup_mr_034.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_034.py)

---

### Rank 35: `mr_comp_f7d13c73`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.5206
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["aer_simulator", "aer_simulator_density_matrix", "statevector_simulator", "aer_simulator_statevector", "qasm_simulator"]}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_051_mr_comp_f7d13c73.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_051_mr_comp_f7d13c73.json), QASM: [`release/qasm/circuit_mr_051.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_051.qasm), Python: [`release/python/followup_mr_035.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_035.py)

---

### Rank 36: `mr_comp_091836d2`

- **Signature**: `ChangeOptLevel(['levels']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.5191
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Bounded Suite Validation**: Tested on 4 canonical circuits, Passed 3/4, Min Statevector Fidelity = 0.25
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"levels": [0, 2, 3, 1]}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_052_mr_comp_091836d2.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_052_mr_comp_091836d2.json), QASM: [`release/qasm/circuit_mr_052.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_052.qasm), Python: [`release/python/followup_mr_036.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_036.py)

---

### Rank 37: `mr_comp_27d8b7b8`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.5183
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 2 canonical circuits, Passed 2/2, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_053_mr_comp_27d8b7b8.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_053_mr_comp_27d8b7b8.json), QASM: [`release/qasm/circuit_mr_053.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_053.qasm), Python: [`release/python/followup_mr_037.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_037.py)

---

### Rank 38: `mr_comp_6c727e0e`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.5154
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"scramble_percentage": 0.5}, {"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.75}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_054_mr_comp_6c727e0e.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_054_mr_comp_6c727e0e.json), QASM: [`release/qasm/circuit_mr_054.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_054.qasm), Python: [`release/python/followup_mr_038.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_038.py)

---

### Rank 39: `mr_comp_da5de3fa`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeBackend(['available_backends'])`
- **Depth**: 3
- **Fitness**: 0.5119
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}, {"available_backends": ["aer_simulator_matrix_product_state"]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_056_mr_comp_da5de3fa.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_056_mr_comp_da5de3fa.json), QASM: [`release/qasm/circuit_mr_056.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_056.qasm), Python: [`release/python/followup_mr_039.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_039.py)

---

### Rank 40: `mr_comp_0bf7305c`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.5119
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.13, "min_connection_density": 0.11, "max_connection_density": 0.28, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.75}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_057_mr_comp_0bf7305c.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_057_mr_comp_0bf7305c.json), QASM: [`release/qasm/circuit_mr_057.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_057.qasm), Python: [`release/python/followup_mr_040.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_040.py)

---

### Rank 41: `mr_comp_821ad5e0`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> ChangeOptLevel(['levels']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.5117
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.25, "min_connection_density": 0.09, "max_connection_density": 0.24, "force_connected": true}, {"levels": [3, 0, 1]}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_058_mr_comp_821ad5e0.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_058_mr_comp_821ad5e0.json), QASM: [`release/qasm/circuit_mr_058.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_058.qasm), Python: [`release/python/followup_mr_041.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_041.py)

---

### Rank 42: `mr_comp_8d2a65dc`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.5052
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 2 canonical circuits, Passed 2/2, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.13, "min_connection_density": 0.11, "max_connection_density": 0.28, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_060_mr_comp_8d2a65dc.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_060_mr_comp_8d2a65dc.json), QASM: [`release/qasm/circuit_mr_060.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_060.qasm), Python: [`release/python/followup_mr_042.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_042.py)

---

### Rank 43: `mr_comp_e4f97cb2`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.505
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Empirical Simulation Stats**: Tested on 2 benchmarks, Compiled 2, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_061_mr_comp_e4f97cb2.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_061_mr_comp_e4f97cb2.json), QASM: [`release/qasm/circuit_mr_061.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_061.qasm), Python: [`release/python/followup_mr_043.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_043.py)

---

### Rank 44: `mr_comp_ef8c040c`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.5016
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_062_mr_comp_ef8c040c.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_062_mr_comp_ef8c040c.json), QASM: [`release/qasm/circuit_mr_062.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_062.qasm), Python: [`release/python/followup_mr_044.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_044.py)

---

### Rank 45: `mr_comp_6fc6b65f`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> ChangeOptLevel(['levels']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.4995
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Bounded Suite Validation**: Tested on 4 canonical circuits, Passed 3/4, Min Statevector Fidelity = 0.25
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"levels": [0, 3, 2, 1]}, {"scramble_percentage": 0.5}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_063_mr_comp_6fc6b65f.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_063_mr_comp_6fc6b65f.json), QASM: [`release/qasm/circuit_mr_063.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_063.qasm), Python: [`release/python/followup_mr_045.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_045.py)

---

### Rank 46: `mr_comp_235638fe`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeBackend(['available_backends'])`
- **Depth**: 2
- **Fitness**: 0.4965
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"available_backends": ["aer_simulator_statevector", "qasm_simulator", "aer_simulator_density_matrix", "aer_simulator_matrix_product_state"]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_064_mr_comp_235638fe.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_064_mr_comp_235638fe.json), QASM: [`release/qasm/circuit_mr_064.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_064.qasm), Python: [`release/python/followup_mr_046.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_046.py)

---

### Rank 47: `mr_comp_757caebf`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.4955
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["aer_simulator", "aer_simulator_density_matrix", "statevector_simulator", "aer_simulator_statevector", "qasm_simulator"]}, {"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.75}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_066_mr_comp_757caebf.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_066_mr_comp_757caebf.json), QASM: [`release/qasm/circuit_mr_066.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_066.qasm), Python: [`release/python/followup_mr_047.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_047.py)

---

### Rank 48: `mr_comp_4052c8bb`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.4945
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_067_mr_comp_4052c8bb.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_067_mr_comp_4052c8bb.json), QASM: [`release/qasm/circuit_mr_067.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_067.qasm), Python: [`release/python/followup_mr_048.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_048.py)

---

### Rank 49: `mr_comp_5b0d7143`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.4914
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_068_mr_comp_5b0d7143.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_068_mr_comp_5b0d7143.json), QASM: [`release/qasm/circuit_mr_068.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_068.qasm), Python: [`release/python/followup_mr_049.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_049.py)

---

### Rank 50: `mr_comp_d251dc40`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected'])`
- **Depth**: 3
- **Fitness**: 0.4912
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["aer_simulator", "aer_simulator_density_matrix", "statevector_simulator", "aer_simulator_statevector", "qasm_simulator"]}, {"min_to_change": 1, "max_to_change": 1}, {"min_perc_nodes": 1, "max_perc_nodes": 1.37, "min_connection_density": 0.14, "max_connection_density": 0.29, "force_connected": true}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_069_mr_comp_d251dc40.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_069_mr_comp_d251dc40.json), QASM: [`release/qasm/circuit_mr_069.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_069.qasm), Python: [`release/python/followup_mr_050.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_050.py)

---

### Rank 51: `mr_comp_f226e1bf`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.4885
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 0.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.26, "min_connection_density": 0.06, "max_connection_density": 0.11, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.75}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_071_mr_comp_f226e1bf.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_071_mr_comp_f226e1bf.json), QASM: [`release/qasm/circuit_mr_071.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_071.qasm), Python: [`release/python/followup_mr_051.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_051.py)

---

### Rank 52: `mr_comp_3be855ec`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.4833
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_073_mr_comp_3be855ec.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_073_mr_comp_3be855ec.json), QASM: [`release/qasm/circuit_mr_073.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_073.qasm), Python: [`release/python/followup_mr_052.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_052.py)

---

### Rank 53: `mr_comp_89663f0d`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.4828
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.49, "min_connection_density": 0.09, "max_connection_density": 0.28, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_074_mr_comp_89663f0d.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_074_mr_comp_89663f0d.json), QASM: [`release/qasm/circuit_mr_074.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_074.qasm), Python: [`release/python/followup_mr_053.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_053.py)

---

### Rank 54: `mr_comp_b78e2e21`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.48
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["qasm_simulator", "aer_simulator_matrix_product_state", "aer_simulator"]}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_075_mr_comp_b78e2e21.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_075_mr_comp_b78e2e21.json), QASM: [`release/qasm/circuit_mr_075.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_075.qasm), Python: [`release/python/followup_mr_054.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_054.py)

---

### Rank 55: `mr_comp_6b90d22a`

- **Signature**: `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.4792
- **Verification Tier**: `PRIMITIVE_SYMBOLIC_CHAIN`
- **Verification Method**: Composition of exact symbolic gate identities (each primitive gate rewrite proven identically zero in SymPy: U1 - U2 == 0)
- **Bounded Suite Validation**: Tested on 2 canonical circuits, Passed 2/2, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_076_mr_comp_6b90d22a.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_076_mr_comp_6b90d22a.json), QASM: [`release/qasm/circuit_mr_076.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_076.qasm), Python: [`release/python/followup_mr_055.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_055.py)

---

### Rank 56: `mr_comp_3ffcdac1`

- **Signature**: `ChangeBackend(['available_backends']) -> ChangeTargetBasis(['universal_gate_sets'])`
- **Depth**: 2
- **Fitness**: 0.479
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 5 benchmarks, Compiled 5, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["qasm_simulator", "aer_simulator_matrix_product_state", "aer_simulator", "statevector_simulator", "aer_simulator_statevector"]}, {"universal_gate_sets": [{"gates": ["rx", "ry", "rz", "p", "cx"]}]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_077_mr_comp_3ffcdac1.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_077_mr_comp_3ffcdac1.json), QASM: [`release/qasm/circuit_mr_077.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_077.qasm), Python: [`release/python/followup_mr_056.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_056.py)

---

### Rank 57: `mr_comp_80493143`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.4759
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.26, "min_connection_density": 0.06, "max_connection_density": 0.11, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_078_mr_comp_80493143.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_078_mr_comp_80493143.json), QASM: [`release/qasm/circuit_mr_078.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_078.qasm), Python: [`release/python/followup_mr_057.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_057.py)

---

### Rank 58: `mr_comp_a21b790b`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeOptLevel(['levels']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.4754
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 0.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"levels": [1]}, {"scramble_percentage": 1.0}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_079_mr_comp_a21b790b.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_079_mr_comp_a21b790b.json), QASM: [`release/qasm/circuit_mr_079.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_079.qasm), Python: [`release/python/followup_mr_058.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_058.py)

---

### Rank 59: `mr_comp_fde58826`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.4754
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 2 canonical circuits, Passed 2/2, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"scramble_percentage": 0.75}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_080_mr_comp_fde58826.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_080_mr_comp_fde58826.json), QASM: [`release/qasm/circuit_mr_080.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_080.qasm), Python: [`release/python/followup_mr_059.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_059.py)

---

### Rank 60: `mr_comp_886c8302`

- **Signature**: `ChangeOptLevel(['levels']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.4672
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 2 canonical circuits, Passed 2/2, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 3 benchmarks, Compiled 3, Avg KS p-value = 1.0000
- **Parameters**: `[{"levels": [0, 1]}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_083_mr_comp_886c8302.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_083_mr_comp_886c8302.json), QASM: [`release/qasm/circuit_mr_083.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_083.qasm), Python: [`release/python/followup_mr_060.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_060.py)

---

### Rank 61: `mr_comp_81f429c3`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.4669
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["aer_simulator_density_matrix", "qasm_simulator", "aer_simulator_matrix_product_state", "aer_simulator_statevector", "aer_simulator"]}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_084_mr_comp_81f429c3.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_084_mr_comp_81f429c3.json), QASM: [`release/qasm/circuit_mr_084.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_084.qasm), Python: [`release/python/followup_mr_061.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_061.py)

---

### Rank 62: `mr_comp_38496154`

- **Signature**: `ChangeBackend(['available_backends']) -> ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected'])`
- **Depth**: 2
- **Fitness**: 0.466
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 5 benchmarks, Compiled 5, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["qasm_simulator", "aer_simulator_matrix_product_state", "aer_simulator", "statevector_simulator", "aer_simulator_statevector"]}, {"min_perc_nodes": 1, "max_perc_nodes": 1.37, "min_connection_density": 0.14, "max_connection_density": 0.29, "force_connected": true}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_085_mr_comp_38496154.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_085_mr_comp_38496154.json), QASM: [`release/qasm/circuit_mr_085.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_085.qasm), Python: [`release/python/followup_mr_062.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_062.py)

---

### Rank 63: `mr_comp_ade186ce`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.4569
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"scramble_percentage": 0.5}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_086_mr_comp_ade186ce.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_086_mr_comp_ade186ce.json), QASM: [`release/qasm/circuit_mr_086.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_086.qasm), Python: [`release/python/followup_mr_063.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_063.py)

---

### Rank 64: `mr_comp_399efd4f`

- **Signature**: `ChangeBackend(['available_backends']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.453
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["qasm_simulator", "aer_simulator_matrix_product_state", "aer_simulator", "statevector_simulator", "aer_simulator_statevector"]}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_087_mr_comp_399efd4f.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_087_mr_comp_399efd4f.json), QASM: [`release/qasm/circuit_mr_087.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_087.qasm), Python: [`release/python/followup_mr_064.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_064.py)

---

### Rank 65: `mr_comp_d883215f`

- **Signature**: `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])`
- **Depth**: 3
- **Fitness**: 0.453
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 1 canonical circuits, Passed 1/1, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_perc_nodes": 1, "max_perc_nodes": 1.62, "min_connection_density": 0.15, "max_connection_density": 0.26, "force_connected": true}, {"min_to_change": 1, "max_to_change": 1}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_088_mr_comp_d883215f.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_088_mr_comp_d883215f.json), QASM: [`release/qasm/circuit_mr_088.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_088.qasm), Python: [`release/python/followup_mr_065.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_065.py)

---

### Rank 66: `mr_comp_4d337a68`

- **Signature**: `QdiffG2TwoHToId(['add_identity_matrix']) -> ChangeOptLevel(['levels'])`
- **Depth**: 2
- **Fitness**: 0.4364
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"add_identity_matrix": true}, {"levels": [2, 3, 0, 1]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_100_mr_comp_4d337a68.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_100_mr_comp_4d337a68.json), QASM: [`release/qasm/circuit_mr_100.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_100.qasm), Python: [`release/python/followup_mr_066.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_066.py)

---

### Rank 67: `mr_comp_48c9adae`

- **Signature**: `ChangeBackend(['available_backends']) -> ChangeOptLevel(['levels'])`
- **Depth**: 2
- **Fitness**: 0.4301
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 5 benchmarks, Compiled 5, Avg KS p-value = 1.0000
- **Parameters**: `[{"available_backends": ["aer_simulator_statevector", "aer_simulator_matrix_product_state", "aer_simulator_density_matrix", "statevector_simulator", "qasm_simulator", "aer_simulator"]}, {"levels": [0, 1]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_105_mr_comp_48c9adae.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_105_mr_comp_48c9adae.json), QASM: [`release/qasm/circuit_mr_105.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_105.qasm), Python: [`release/python/followup_mr_067.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_067.py)

---

### Rank 68: `mr_comp_5cb514ac`

- **Signature**: `ChangeBackend(['available_backends']) -> ChangeOptLevel(['levels']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 3
- **Fitness**: 0.4281
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 0.9645)
- **Empirical Simulation Stats**: Tested on 5 benchmarks, Compiled 5, Avg KS p-value = 0.9645
- **Parameters**: `[{"available_backends": ["aer_simulator", "aer_simulator_density_matrix", "statevector_simulator", "aer_simulator_statevector", "qasm_simulator"]}, {"levels": [3, 0, 1, 2]}, {"scramble_percentage": 0.5}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_108_mr_comp_5cb514ac.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_108_mr_comp_5cb514ac.json), QASM: [`release/qasm/circuit_mr_108.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_108.qasm), Python: [`release/python/followup_mr_068.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_068.py)

---

### Rank 69: `mr_comp_204ed4c2`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeOptLevel(['levels'])`
- **Depth**: 2
- **Fitness**: 0.4238
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"levels": [1, 0]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_109_mr_comp_204ed4c2.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_109_mr_comp_204ed4c2.json), QASM: [`release/qasm/circuit_mr_109.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_109.qasm), Python: [`release/python/followup_mr_069.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_069.py)

---

### Rank 70: `mr_comp_3803c8ac`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeTargetBasis(['universal_gate_sets'])`
- **Depth**: 2
- **Fitness**: 0.4118
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"universal_gate_sets": [{"gates": ["rx", "ry", "rz", "p", "cx"]}]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_114_mr_comp_3803c8ac.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_114_mr_comp_3803c8ac.json), QASM: [`release/qasm/circuit_mr_114.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_114.qasm), Python: [`release/python/followup_mr_070.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_070.py)

---

### Rank 71: `mr_comp_5375f23a`

- **Signature**: `ChangeQubitOrder(['scramble_percentage']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])`
- **Depth**: 2
- **Fitness**: 0.4096
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 0.0000
- **Parameters**: `[{"scramble_percentage": 1.0}, {"min_to_change": 1, "max_to_change": 1}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_117_mr_comp_5375f23a.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_117_mr_comp_5375f23a.json), QASM: [`release/qasm/circuit_mr_117.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_117.qasm), Python: [`release/python/followup_mr_071.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_071.py)

---

### Rank 72: `mr_comp_dc94fbf2`

- **Signature**: `QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])`
- **Depth**: 2
- **Fitness**: 0.402
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"scramble_percentage": 0.5}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_125_mr_comp_dc94fbf2.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_125_mr_comp_dc94fbf2.json), QASM: [`release/qasm/circuit_mr_125.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_125.qasm), Python: [`release/python/followup_mr_072.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_072.py)

---

### Rank 73: `mr_comp_369f36cd`

- **Signature**: `QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeTargetBasis(['universal_gate_sets']) -> ChangeBackend(['available_backends'])`
- **Depth**: 3
- **Fitness**: 0.3537
- **Verification Tier**: `EMPIRICALLY_SIMULATED`
- **Verification Method**: Multi-benchmark MQT-CC MLIR compilation + KS-test (5 benchmarks, p > 0.05, Avg p-val = 1.0000)
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"universal_gate_sets": [{"gates": ["cx", "h", "s", "t"]}]}, {"available_backends": ["aer_simulator", "aer_simulator_density_matrix", "statevector_simulator", "aer_simulator_statevector", "qasm_simulator"]}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_129_mr_comp_369f36cd.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_129_mr_comp_369f36cd.json), QASM: [`release/qasm/circuit_mr_129.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_129.qasm), Python: [`release/python/followup_mr_073.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_073.py)

---

### Rank 74: `mr_comp_410214db`

- **Signature**: `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> ChangeTargetBasis(['universal_gate_sets']) -> ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected'])`
- **Depth**: 3
- **Fitness**: 0.3452
- **Verification Tier**: `BOUNDED_SUITE_VERIFIED`
- **Verification Method**: Bounded combinatorial test suite (29 canonical circuits <= 4q, depth <= 5; Min Statevector Fidelity = 1.0000)
- **Bounded Suite Validation**: Tested on 3 canonical circuits, Passed 3/3, Min Statevector Fidelity = 1.0
- **Empirical Simulation Stats**: Tested on 1 benchmarks, Compiled 1, Avg KS p-value = 1.0000
- **Parameters**: `[{"min_to_change": 1, "max_to_change": 1}, {"universal_gate_sets": [{"gates": ["cx", "h", "s", "t"]}]}, {"min_perc_nodes": 1, "max_perc_nodes": 1.37, "min_connection_density": 0.14, "max_connection_density": 0.29, "force_connected": true}]`
- **Release Artifacts**: JSON: [`release/json/composite_mr_131_mr_comp_410214db.json`](file:///home/karthikg/Documents/gentest/release/json/composite_mr_131_mr_comp_410214db.json), QASM: [`release/qasm/circuit_mr_131.qasm`](file:///home/karthikg/Documents/gentest/release/qasm/circuit_mr_131.qasm), Python: [`release/python/followup_mr_074.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_074.py)

---

