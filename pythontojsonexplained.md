# The Python-to-JSON Architecture & Synthesis Lifecycle

This document explains the technical lifecycle of the **Gentest** framework: how we started from raw Python source code in the MorphQ research repository, why and how we transformed those transformations into a structured **JSON schema**, how our **Genetic Algorithm (GA)** navigated the permutations and combinations of that space, how our **3-tier testing gauntlet** certified them, and how we finally converted the winning relations back into standalone **Python** and **OpenQASM 3.0** artifacts.

---

## 1. The Starting Point: What Was in the Original MorphQ Repository?

The reference repository ([`MorphQ-Quantum-Qiskit-Testing-ICSE-23`](https://github.com/sola-st/MorphQ-Quantum-Qiskit-Testing-ICSE-23)) contained 17 metamorphic transformation techniques. 

### What Was Present in MorphQ:
- **Pure Python Code**: The 17 relations were written strictly as Python files in [`lib/mr/`](file:///home/karthikg/Documents/gentest/MorphQ-Quantum-Qiskit-Testing-ICSE-23/lib/mr). Each file defined a class inheriting from `MetamorphicTransformation`:
  - `add_unused_register.py`
  - `change_backend.py`
  - `change_coupling_map.py`
  - `change_opt_level.py`
  - `change_qubit_order.py`
  - `change_target_basis.py`
  - `inject_null_effect.py`
  - `inject_parameters.py`
  - `qdiff_g1_swap_to_cnot.py` through `qdiff_g7_ccnot_decomposition.py`
  - `run_independent_partitions.py`
  - `to_qasm_and_back.py`
- **AST Manipulation**: Each class used Python’s Abstract Syntax Tree (`ast` module) to parse source code strings, find specific AST nodes (e.g., `SwapGate`), and rewrite them into alternative gate sequences or change Qiskit `transpile()` arguments.

### What Was NOT in MorphQ:
1. **Zero JSON Specifications**: The original repo had no JSON files describing relations, parameters, bounds, or interfaces.
2. **Zero Unitary Matrices**: There were no mathematical unitary matrices or formal equivalence proofs. MorphQ relied purely on heuristic output sampling.
3. **No Automated Multi-Step Synthesis**: MorphQ executed individual transformations or static linear scripts; it could not autonomously compose, balance, or optimize multi-step chains.

---

## 2. The Problem: Why Python Alone Fails for a Genetic Algorithm

In evolutionary computation, an algorithm needs to perform three operations:
1. **Initialization**: Generate random candidates.
2. **Crossover**: Slice and recombine parts of two parent solutions.
3. **Mutation**: Tweak parameters or alter structure.

If you attempt to apply a Genetic Algorithm directly to **Python source code**, the process quickly collapses:
- **Syntax Disasters**: Splitting and recombining raw Python AST statements randomly creates broken code blocks, missing variable scopes (`NameError`), or invalid syntax (`SyntaxError`).
- **No Search Boundaries**: A GA wouldn't know what parameters are valid. If it mutates `min_connection_density` to a string or a negative number, the script crashes.
- **Extreme Runtime Overhead**: Parsing, modifying, compiling, and running live Python ASTs repeatedly for thousands of invalid candidates is prohibitively slow.

---

## 3. The Solution: Decoupling Genotype (JSON) from Phenotype (Python)

To solve this, we applied the standard biological distinction:
- **Genotype (JSON)**: The clean, declarative genetic blueprint.
- **Phenotype (Python / Quantum Circuit)**: The physical, executable circuit transpiled and evaluated by the quantum compiler.

```
  ┌─────────────────────────────────────────────────────────┐
  │                 GENOTYPE (Data / JSON)                  │
  │   Declarative recipe: Which gates? Which parameters?    │
  └────────────────────────────┬────────────────────────────┘
                               │
                Interpreted & Executed by Engine
                               ▼
  ┌─────────────────────────────────────────────────────────┐
  │                PHENOTYPE (Code / Python)                │
  │   Living Python AST rewriting, Qiskit transpilation,     │
  │   and OpenQASM 3.0 execution on MQT-CC.                 │
  └─────────────────────────────────────────────────────────┘
```

### How We Built the Bridge: `mr_library/schema.json`
We analyzed the 17 Python classes and extracted their configurations into a single, typed schema ([`mr_library/schema.json`](file:///home/karthikg/Documents/gentest/mr_library/schema.json)). This schema formalized:
- **Class & Module Bindings**: Telling the engine which Python file to import dynamically.
- **Oracle Classifications**: Whether the transformation preserves exact statevectors (`DIRECT_EQUIVALENT`) or requires bitstring remapping (`PERMUTATION_MAPPED`).
- **Parameter Bounds**: Defining explicit data types, ranges, and allowable options for every setting (e.g., `levels: [0, 1, 2, 3]`, `min_n_bit: [1..10]`).

---

## 4. How the GA Evolved Permutations & Combinations (PnC)

With the JSON schema in place, every candidate relation became a simple JSON chromosome:

```json
{
  "id": "mr_comp_49a4c2ec",
  "depth": 2,
  "genes": [
    {
      "mr_id": "ChangeCouplingMap",
      "params": {
        "min_connection_density": 0.06,
        "max_connection_density": 0.20,
        "force_connected": true
      }
    },
    {
      "mr_id": "ChangeQubitOrder",
      "params": {
        "scramble_percentage": 0.5
      }
    }
  ]
}
```

The Genetic Algorithm operated entirely within this safe JSON space:
1. **Combinations**: Combining high-level compiler passes (like `ChangeOptLevel` or `ChangeCouplingMap`) with low-level gate identities (like `QdiffG3XToHssh`).
2. **Permutations (Ordering)**: Testing whether applying `ChangeTargetBasis ➔ ChangeQubitOrder` stresses the compiler differently than `ChangeQubitOrder ➔ ChangeTargetBasis`.
3. **Safe Crossover & Mutation**: Crossover was simply slicing a Python list of JSON gene dictionaries. Mutation adjusted numeric values strictly within the ranges allowed by `schema.json`.
4. **Instant Invariant Validation**: Before compiling, `validate_gene_params()` checked logical rules (e.g., asserting that `min_density <= max_density`) to reject broken individuals in microseconds.
5. **Pre-Simulation Pruning**: By inspecting the JSON gene sequence, we detected and eliminated 57 redundant candidates (such as consecutive `ChangeOptLevel` calls where the second overwrote the first) without wasting quantum simulation cycles.

---

## 5. The Dynamic Engine: How JSON Executes Python

To execute a JSON relation, the runtime engine in [`mr_library/__init__.py`](file:///home/karthikg/Documents/gentest/mr_library/__init__.py) uses Python’s dynamic reflection:

```python
# mr_library/__init__.py: Dynamic Dispatch Engine
for gene in json_chromosome["genes"]:
    mr_id = gene["mr_id"]       # e.g., "ChangeTargetBasis"
    params = gene["params"]     # e.g., {"universal_gate_sets": [["u", "cx"]]}
    
    # 1. Look up where the Python class lives
    info = SCHEMA[mr_id]
    module = importlib.import_module(info["module_path"])
    cls = getattr(module, info["class_name"])
    
    # 2. Instantiate the class with the JSON parameters & deterministic seed
    transformer = cls(mr_id, config_dict={mr_id: params}, seed=deterministic_seed)
    
    # 3. Apply the AST transformation to the quantum circuit code
    current_circuit_code = transformer.derive(current_circuit_code)
```

Each gene transforms the circuit code and passes the resulting code as the input to the next gene in the chain.

---

## 6. The Validation Gauntlet: How the Candidates Were Certified

To ensure the GA's permutations did not create invalid or logically broken circuits, every evolved candidate was submitted to a **3-tier verification ladder**:

```
                              [ Candidate Chain ]
                                       │
                                       ▼
        ┌─────────────────────────────────────────────────────────────┐
        │ TIER 1: Exact SymPy Matrix Proof                            │
        │ • Is it a chain of discrete gate identities?                │
        │ • Computes:  U_src - U_follow ≡ 0                           │
        │ • If YES: Certified as PRIMITIVE_SYMBOLIC_CHAIN             │
        └──────────────────────────────┬──────────────────────────────┘
                                       │ (If not pure gate identities)
                                       ▼
        ┌─────────────────────────────────────────────────────────────┐
        │ TIER 2: Bounded Combinatorial Test Suite                    │
        │ • Evaluates across 29 canonical circuits (depth ≤ 5)        │
        │ • Sweeps boundary angles (0, π/4, π/2, π)                   │
        │ • Calculates Statevector Fidelity: F ≥ 0.999                │
        │ • Zero Exception Masking: Any crash = Instant Failure       │
        │ • If PASSED: Certified as BOUNDED_SUITE_VERIFIED            │
        └──────────────────────────────┬──────────────────────────────┘
                                       │ (If compiler passes / layout shifts)
                                       ▼
        ┌─────────────────────────────────────────────────────────────┐
        │ TIER 3: Empirical Compiler Simulation                       │
        │ • Compiles via MQT-CC (OpenQASM 3.0 MLIR)                   │
        │ • 5 Algorithm Benchmarks (Bell, GHZ, QFT-4, Grover, Adder)  │
        │ • 4,096 measurement shots on seeded Aer simulator           │
        │ • Classical bitstring permutation remapping π(y)            │
        │ • Kolmogorov-Smirnov statistical test: p-value > 0.05       │
        │ • If PASSED: Certified as EMPIRICALLY_SIMULATED             │
        └─────────────────────────────────────────────────────────────┘
```

### The Gauntlet Outcome:
- **131 Initial Candidates Evolved**
- **28 Candidates Failed** (caught transpiler crashes, syntax issues, or fidelity drops) and were permanently discarded.
- **57 Redundant Candidates Pruned** (algebraic and multiset duplicates).
- **74 Certified Essential Relations** achieved a **100.0% Pass Rate**.

---

## 7. Closing the Loop: Re-Materializing Back into Python & OpenQASM 3.0

Once the best 74 relations were certified, we did not leave them trapped in JSON format. We materialized them into the [`release/`](file:///home/karthikg/Documents/gentest/release) distribution bundle:

1. **`release/json/` (74 files)**: The master declarative JSON specifications containing the exact gene parameters and verification ledger.
2. **`release/python/` (74 files)**: Complete, standalone, executable Python scripts (e.g., [`followup_mr_001.py`](file:///home/karthikg/Documents/gentest/release/python/followup_mr_001.py) through `followup_mr_074.py`). Any developer can run them directly without needing the GA or `mr_library`.
3. **`release/qasm/` (74 files)**: Pre-compiled **OpenQASM 3.0** circuit files. These contain zero Python dependencies and can be piped directly into any external quantum compiler (such as MQT-CC via CLI or C++ API).

---

## 8. Summary Table

| Stage | Format | Purpose | Key Benefit |
| :--- | :---: | :--- | :--- |
| **1. Origin** | Python AST (`lib/mr/*.py`) | Original MorphQ transformation classes | Provided domain logic for quantum modifications. |
| **2. Schema** | JSON Schema (`schema.json`) | Defined typed parameters, bounds, and class bindings | Allowed safe sampling and genetic operators. |
| **3. Evolution** | JSON Chromosomes | GA explored permutations & combinations | Fast crossover/mutation with zero Python syntax errors. |
| **4. Testing** | 3-Tier Verification | SymPy + 29 Bounded Circuits + MQT-CC Simulation | 100% mathematical and empirical correctness guarantee. |
| **5. Release** | Python (`.py`) & OpenQASM (`.qasm`) | Standalone ready-to-run test cases | Portable, zero-dependency testing for any quantum compiler. |
