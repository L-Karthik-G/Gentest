# Gentest: Evolutionary Metamorphic Testing for Quantum Compilers

[![Tests](https://img.shields.io/badge/pytest-9%20passed-brightgreen.svg)]()
[![Target](https://img.shields.io/badge/Target-MQT--CC%20(OpenQASM%203.0%20MLIR)-blue.svg)]()
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

**Gentest** is an automated quality assurance pipeline for quantum software compilers, specifically targeting the **Munich Quantum Toolkit Compiler Collection (MQT-CC)** via OpenQASM 3.0 MLIR compilation down to DDSIM.

To bypass the quantum *Test Oracle Problem*, Gentest uses a **Genetic Algorithm (GA)** to synthesize multi-step **Metamorphic Relations (MRs)** from 17 MorphQ and QDiff primitives, certifying them across a 3-tier mathematical, bounded, and empirical verification hierarchy.

---

## Key Highlights

- **74 Certified Essential Relations**: Curated from 131 evolved candidates with 100.0% pass rate.
- **Three-Tier Verification Ladder**:
  - `PRIMITIVE_SYMBOLIC_CHAIN` (9 relations): Proven identically zero in SymPy ($U_1 - U_2 \equiv 0$).
  - `BOUNDED_SUITE_VERIFIED` (30 relations): Evaluated on 29 canonical circuits ($\le 4$q, depth $\le 5$) with Statevector fidelity $\ge 0.999$.
  - `EMPIRICALLY_SIMULATED` (35 relations): MQT-CC MLIR compilation + Kolmogorov-Smirnov test ($p > 0.05, shots = 4096$) across 5 quantum algorithm benchmarks.
- **100% Reproducible**: Order-independent deterministic evaluation seeded via SHA-256 chromosome hashing.
- **Zero Exception Masking**: Strict validation where any crash, syntax error, or fidelity drop immediately fails the check.

---

## Project Structure

```text
├── release/                      # Curated essential distribution bundle
│   ├── pruned_essential_catalog.json  # 74 certified master relations
│   ├── certified_audit_manifest.json  # Full verification proof ledger
│   ├── json/                          # 74 individual relation parameter specs
│   ├── qasm/                          # 74 ready-to-run OpenQASM 3.0 circuits
│   └── python/                        # 74 executable Python test scripts
├── ga/                           # Genetic algorithm engine (operators, fitness, individual)
├── mr_library/                   # 17 primitive MR definitions and schema
├── verification/                 # 3-tier verification suite (proofs, bounded, empirical, audit)
├── benchmarks/                   # Seed circuits (Bell, GHZ, QFT-4, Grover-3, Adder-3)
├── tests/                        # 9 automated regression tests (pytest)
└── results/                      # Audit manifests and GA run metadata
```

---

## Quick Start

### 1. Installation

#### Using `uv` (Recommended — 10-100x faster)

If you don't have `uv` installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Create environment and install dependencies:
```bash
git clone https://github.com/L-Karthik-G/Gentest.git
cd Gentest

# Create Python 3.12 venv and install dependencies
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e ".[dev]"
```

*Alternatively, run commands directly without activation using `uv run`:*
```bash
uv run pytest tests/
```

#### Using standard `pip`

```bash
git clone https://github.com/L-Karthik-G/Gentest.git
cd Gentest

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Run the Automated Test Suite

```bash
pytest tests/
```

### 3. Run the Multi-Tier Certified Audit

```bash
# Verify the curated essential library
python3 verification/audit_library.py --target pruned
```

### 4. Synthesize New Relations with the Genetic Algorithm

```bash
python3 ga/run_ga.py --seed 42 --max_gens 10 --pop_size 80
```

---

## Documentation

- **[EXPLAINER_FOR_BEGINNERS.md](EXPLAINER_FOR_BEGINNERS.md)**: A non-technical, conceptual guide with diagrams and analogies explaining quantum compiler testing and the genetic algorithm.
- **[CORE_METHODOLOGY_AND_SCOPE.md](CORE_METHODOLOGY_AND_SCOPE.md)**: Complete breakdown of what this project does and explicit non-goals / boundaries.
- **[TECHNICAL_APPROACH_AND_TESTS.md](TECHNICAL_APPROACH_AND_TESTS.md)**: Mathematical formulas, hyperparameter rationale, and test battery specifications.
- **[METAMORPHIC_RELATIONS_REPORT.md](METAMORPHIC_RELATIONS_REPORT.md)**: Executive certification report of the 74 release relations.
- **[DETAILED_RELATIONS_REPORT.md](DETAILED_RELATIONS_REPORT.md)**: Complete technical specification for every individual relation.

---

## License

This project is licensed under the MIT License.
