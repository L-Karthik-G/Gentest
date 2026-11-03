import numpy as np
import sympy as sp
from typing import Dict, Any, Tuple


def prove_swap_to_cnot() -> Tuple[bool, float, str]:
    """Exact symbolic proof in SymPy: SWAP == CX(0,1) @ CX(1,0) @ CX(0,1)."""
    swap_sym = sp.Matrix([
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1]
    ])
    cx01_sym = sp.Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])
    cx10_sym = sp.Matrix([
        [1, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
        [0, 1, 0, 0]
    ])

    composed = cx01_sym * cx10_sym * cx01_sym
    diff = (swap_sym - composed).applyfunc(sp.simplify)
    is_zero = (diff == sp.zeros(4, 4))
    return is_zero, 0.0 if is_zero else 1.0, "SWAP == CX(0,1) @ CX(1,0) @ CX(0,1)"


def prove_two_h_to_id() -> Tuple[bool, float, str]:
    """Exact symbolic proof in SymPy: H @ H == I_2."""
    h = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    identity = sp.eye(2)
    composed = h * h
    diff = (identity - composed).applyfunc(sp.simplify)
    is_zero = (diff == sp.zeros(2, 2))
    return is_zero, 0.0 if is_zero else 1.0, "H @ H == I_2"


def prove_x_to_hssh() -> Tuple[bool, float, str]:
    """Exact symbolic proof in SymPy: X == H @ S @ S @ H."""
    x = sp.Matrix([[0, 1], [1, 0]])
    h = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    s = sp.Matrix([[1, 0], [0, sp.I]])
    composed = h * s * s * h
    diff = (x - composed).applyfunc(sp.simplify)
    is_zero = (diff == sp.zeros(2, 2))
    return is_zero, 0.0 if is_zero else 1.0, "X == H @ S @ S @ H"


def prove_z_to_ss() -> Tuple[bool, float, str]:
    """Exact symbolic proof in SymPy: Z == S @ S."""
    z = sp.Matrix([[1, 0], [0, -1]])
    s = sp.Matrix([[1, 0], [0, sp.I]])
    composed = s * s
    diff = (z - composed).applyfunc(sp.simplify)
    is_zero = (diff == sp.zeros(2, 2))
    return is_zero, 0.0 if is_zero else 1.0, "Z == S @ S"


def prove_cz_to_h_cnot_h() -> Tuple[bool, float, str]:
    """Exact symbolic proof in SymPy: CZ == (I (x) H) @ CX @ (I (x) H)."""
    cz = sp.diag(1, 1, 1, -1)
    h = sp.Matrix([[1, 1], [1, -1]]) / sp.sqrt(2)
    i2 = sp.eye(2)
    i_x_h = sp.kronecker_product(i2, h)
    cx01 = sp.Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0]
    ])
    composed = i_x_h * cx01 * i_x_h
    diff = (cz - composed).applyfunc(sp.simplify)
    is_zero = (diff == sp.zeros(4, 4))
    return is_zero, 0.0 if is_zero else 1.0, "CZ == (I x H) @ CX @ (I x H)"


def prove_two_cz_to_id() -> Tuple[bool, float, str]:
    """Exact symbolic proof in SymPy: CZ @ CZ == I_4."""
    cz = sp.diag(1, 1, 1, -1)
    identity4 = sp.eye(4)
    composed = cz * cz
    diff = (identity4 - composed).applyfunc(sp.simplify)
    is_zero = (diff == sp.zeros(4, 4))
    return is_zero, 0.0 if is_zero else 1.0, "CZ @ CZ == I_4"


PROOF_REGISTRY = {
    "QdiffG1SwapToCnot": prove_swap_to_cnot,
    "QdiffG2TwoHToId": prove_two_h_to_id,
    "QdiffG3XToHSSH": prove_x_to_hssh,
    "QdiffG4ZtoSS": prove_z_to_ss,
    "QdiffG5CZtoHCnotH": prove_cz_to_h_cnot_h,
    "QdiffG6TwoCzToId": prove_two_cz_to_id
}


def verify_algebraic_proofs() -> Dict[str, Any]:
    """Runs all exact symbolic proofs in SymPy and verifies identically zero difference."""
    results = {}
    for rule_name, proof_func in PROOF_REGISTRY.items():
        is_proven, norm_err, formula = proof_func()
        results[rule_name] = {
            "tier": "EXACT_SYMBOLIC_PROOF",
            "is_proven": is_proven,
            "symbolic_zero": is_proven,
            "error_bound": norm_err,
            "frobenius_error": norm_err,
            "formula": formula
        }
    return results


if __name__ == "__main__":
    res = verify_algebraic_proofs()
    print("Exact Symbolic Unitary Proof Results (SymPy):")
    for k, v in res.items():
        status = "PASSED (Exact Zero Matrix)" if v["is_proven"] else "FAILED"
        print(f"  {k}: {status} -> {v['formula']}")
