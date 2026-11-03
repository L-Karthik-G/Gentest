import pytest
from collections import defaultdict


def test_overwrite_detection():
    state_passes = {'ChangeOptLevel', 'ChangeCouplingMap', 'ChangeBackend'}
    
    # Overwriting signature: two ChangeOptLevel passes
    sig_overwrite = "ChangeOptLevel(['levels']) -> QdiffG1SwapToCnot([]) -> ChangeOptLevel(['levels'])"
    prims = [p.split('(')[0].strip() for p in sig_overwrite.split('->')]
    seen = set()
    is_overwriting = False
    for p in prims:
        if p in state_passes:
            if p in seen:
                is_overwriting = True
                break
            seen.add(p)
    assert is_overwriting is True

    # Non-overwriting signature: distinct passes
    sig_valid = "ChangeOptLevel(['levels']) -> QdiffG1SwapToCnot([]) -> ChangeBackend(['available_backends'])"
    prims_val = [p.split('(')[0].strip() for p in sig_valid.split('->')]
    seen_val = set()
    is_overwriting_val = False
    for p in prims_val:
        if p in state_passes:
            if p in seen_val:
                is_overwriting_val = True
                break
            seen_val.add(p)
    assert is_overwriting_val is False


def test_multiset_deduplication():
    # Two relations with commutative multiset of components
    rel1 = {
        "index": 1,
        "signature": "QdiffG1SwapToCnot([]) -> QdiffG4ZtoSS([])",
        "fitness": 0.72,
        "genes": [{"mr_id": "QdiffG1SwapToCnot"}, {"mr_id": "QdiffG4ZtoSS"}]
    }
    rel2 = {
        "index": 2,
        "signature": "QdiffG4ZtoSS([]) -> QdiffG1SwapToCnot([])",
        "fitness": 0.85,
        "genes": [{"mr_id": "QdiffG4ZtoSS"}, {"mr_id": "QdiffG1SwapToCnot"}]
    }

    rels = [rel1, rel2]
    multiset_groups = defaultdict(list)
    for r in rels:
        prims = tuple(sorted(p.split('(')[0].strip() for p in r['signature'].split('->')))
        multiset_groups[prims].append(r)

    assert len(multiset_groups) == 1
    best_rep = max(multiset_groups[list(multiset_groups.keys())[0]], key=lambda x: x['fitness'])
    assert best_rep["index"] == 2
    assert best_rep["fitness"] == 0.85
