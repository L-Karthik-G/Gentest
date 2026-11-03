# Metamorphic Relations Verification & Synthesis Report

## Executive Summary
This report documents the synthesis, verification, and certification pipeline for composite Metamorphic Relations (MRs) targeting the **Munich Quantum Toolkit Compiler Collection (MQT-CC)** via OpenQASM 3.0 MLIR compilation (`mqt.core.mlir.compile_program` targeting `mqt.ddsim.default`).

The pipeline synthesizes compositions of 17 primitive metamorphic transformations derived from MorphQ and QDiff. Following rigorous peer review, all evaluation steps operate with deterministic seeding, zero exception masking, and a three-tier verification ledger that strictly delineates algebraic gate equivalence from bounded and empirical compiler testing.

---

## Hardening & Methodological Refinements

1. **Deterministic Seeding & Reproducibility**:
   - SHA-256 chromosome hashing ensures order-independent, reproducible seed derivation (`base_seed`).
   - Seeds are propagated explicitly to both `random` and `numpy.random`, as well as to `AerSimulator` (`seed_simulator=sim_seed`).
2. **Strict Verification Rigor**:
   - Zero exception masking: silent fallback handlers have been eliminated; any runtime exception, dimension mismatch, or fidelity drop below threshold results in immediate failure.
   - Enforced two-sample Kolmogorov-Smirnov test threshold ($p > 0.05, shots = 4096$) for empirical validation.
   - Exact little-endian bitstring permutation remapping ($\pi(y)$) applied for `ChangeQubitOrder`.
3. **Calibrated Verification Scope**:
   - **`PRIMITIVE_SYMBOLIC_CHAIN`**: Applies strictly to chains composed of discrete unitary gate rewrites proven identically zero difference in SymPy ($U_1 - U_2 \equiv 0$). Does not claim algebraic proof over non-unitary compiler heuristics.
   - **`BOUNDED_SUITE_VERIFIED`**: Validated across a bounded combinatorial suite of 29 canonical circuits ($\le 4$ qubits, depth $\le 5$) with Statevector fidelity $\ge 0.999$.
   - **`EMPIRICALLY_SIMULATED`**: Validated across 5 standard algorithm benchmarks (GHZ 3q, Bell 2q, QFT 4q, Grover 3q, Adder 3q) with MQT-CC MLIR compilation and boundary angle sweeps ($0, \pi/2, \pi, 2\pi, -\pi/2$).
4. **Release Staging & Workspace Hygiene**:
   - Unpruned raw candidates (57 relations) archived to `archive/raw_candidates/`.
   - Clean, self-contained release bundle created in `release/` containing exactly the 74 essential relations and their corresponding JSON, QASM, and Python artifacts.

---

## Synthesis & Pruning Funnel

| Stage | Count | Description |
| :--- | :---: | :--- |
| **Initial Candidate Synthesis** | 131 | Raw composite relations synthesized by Genetic Algorithm (Pop=80, Gens=10, Seed=42) |
| **Pre-Pruning Filtered** | 28 | Rejected during pre-pruning audit due to precondition failure or KS threshold violation |
| **Multiset & Overwrite Pruning** | 29 | Redundant commutative multisets and redundant compiler-state overwrites eliminated |
| **Curated Essential Library** | **74** | **Verified, non-redundant composite relations staged for release** |

---

## Multi-Tier Verification Certification

| Tier | Verified Count | Share | Verification Criteria & Scope |
| :--- | :---: | :---: | :--- |
| **`PRIMITIVE_SYMBOLIC_CHAIN`** | **9** | **12.2%** | Composed solely of discrete gate identities proven identically zero in SymPy ($U_1 - U_2 \equiv 0$) |
| **`BOUNDED_SUITE_VERIFIED`** | **30** | **40.5%** | Statevector fidelity $\ge 0.999$ across the 29-circuit bounded combinatorial suite ($\le 4$q, depth $\le 5$) |
| **`EMPIRICALLY_SIMULATED`** | **35** | **47.3%** | MQT-CC MLIR compilation + KS-test ($p > 0.05$) across GHZ, Bell, QFT-4, Grover-3, and Adder-3 |
| **FAILED** | **0** | **0.0%** | **100.0% Pass Rate across Curated Essential Library (74/74)** |

---

## Top 15 Certified Relations by Fitness

| Rank | MR ID | Signature | Depth | Fitness | Verification Tier |
| :---: | :--- | :--- | :---: | :---: | :--- |
| 1 | `mr_comp_49a4c2ec` | `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> ChangeQubitOrder(['scramble_percentage'])` | 2 | **0.9348** | `EMPIRICALLY_SIMULATED` |
| 2 | `mr_comp_d2762bf1` | `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> ChangeBackend(['available_backends'])` | 2 | **0.9298** | `EMPIRICALLY_SIMULATED` |
| 3 | `mr_comp_f2afe4bd` | `ChangeBackend(['available_backends']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])` | 2 | **0.9149** | `EMPIRICALLY_SIMULATED` |
| 4 | `mr_comp_3b854f93` | `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change'])` | 2 | **0.9149** | `EMPIRICALLY_SIMULATED` |
| 5 | `mr_comp_7c6a0717` | `ChangeQubitOrder(['scramble_percentage']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])` | 3 | **0.9026** | `BOUNDED_SUITE_VERIFIED` |
| 6 | `mr_comp_1294b8f3` | `QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])` | 2 | **0.8923** | `PRIMITIVE_SYMBOLIC_CHAIN` |
| 7 | `mr_comp_bc533f61` | `QdiffG3XToHSSH(['min_to_change', 'max_to_change']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeQubitOrder(['scramble_percentage'])` | 3 | **0.8923** | `BOUNDED_SUITE_VERIFIED` |
| 8 | `mr_comp_19292182` | `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeBackend(['available_backends'])` | 3 | **0.8923** | `EMPIRICALLY_SIMULATED` |
| 9 | `mr_comp_047402b4` | `ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected']) -> ChangeOptLevel(['levels']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])` | 3 | **0.8873** | `EMPIRICALLY_SIMULATED` |
| 10 | `mr_comp_c5959a7f` | `QdiffG2TwoHToId(['add_identity_matrix']) -> QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> QdiffG7CCNOTDecomposition(['min_to_change', 'max_to_change'])` | 3 | **0.8802** | `EMPIRICALLY_SIMULATED` |
| 11 | `mr_comp_ca46fe5b` | `QdiffG5CZtoHCnotH(['min_to_change', 'max_to_change']) -> ChangeOptLevel(['levels'])` | 2 | **0.8661** | `BOUNDED_SUITE_VERIFIED` |
| 12 | `mr_comp_ab7115f2` | `QdiffG1SwapToCnot(['min_to_change', 'max_to_change']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])` | 2 | **0.8611** | `PRIMITIVE_SYMBOLIC_CHAIN` |
| 13 | `mr_comp_ae727414` | `QdiffG2TwoHToId(['add_identity_matrix']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change']) -> QdiffG4ZtoSS(['min_to_change', 'max_to_change'])` | 3 | **0.8611** | `PRIMITIVE_SYMBOLIC_CHAIN` |
| 14 | `mr_comp_0cd8b292` | `QdiffG4ZtoSS(['min_to_change', 'max_to_change']) -> QdiffG1SwapToCnot(['min_to_change', 'max_to_change']) -> QdiffG3XToHSSH(['min_to_change', 'max_to_change'])` | 3 | **0.8611** | `PRIMITIVE_SYMBOLIC_CHAIN` |
| 15 | `mr_comp_cba230cb` | `ChangeTargetBasis(['universal_gate_sets']) -> ChangeCouplingMap(['min_perc_nodes', 'max_perc_nodes', 'min_connection_density', 'max_connection_density', 'force_connected'])` | 2 | **0.8308** | `EMPIRICALLY_SIMULATED` |

---

## Execution Environment & Reproducibility Metadata
- **Random Seed**: `42`
- **Execution Timestamp**: `2026-11-02T18:03:18Z`
- **Python Version**: `3.12.13 (main, Jun 23 2026, 15:18:55) [Clang 22.1.3 ]`
- **Qiskit Version**: `2.6.1`
- **MQT Core Version**: `4.1.1`
- **Target Device**: `mqt.ddsim.default` (Decision Diagram Simulator)
- **Manifest Location**: `results/certified_audit_manifest.json`
- **Release Bundle Directory**: `release/`
