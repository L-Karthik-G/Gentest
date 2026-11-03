import json
import os
from collections import defaultdict

with open('mr_library/generated_mrs/catalog.json') as f:
    catalog = json.load(f)

rels = catalog['relations']

# Identify overwrites
overwriting_indices = set()
for r in rels:
    prims = [p.split('(')[0].strip() for p in r['signature'].split('->')]
    state_passes = ['ChangeOptLevel', 'ChangeCouplingMap', 'ChangeBackend']
    seen_passes = set()
    for p in prims:
        if p in state_passes:
            if p in seen_passes:
                overwriting_indices.add(r['index'])
                break
            seen_passes.add(p)

# Group by commutative multiset
multiset_groups = defaultdict(list)
for r in rels:
    prims = tuple(sorted(p.split('(')[0].strip() for p in r['signature'].split('->')))
    multiset_groups[prims].append(r)

# Identify failed relations from candidate and certified audit manifests
failed_indices = set()
for m_path in ['results/all_candidates_audit_manifest.json', 'results/certified_audit_manifest.json']:
    if os.path.exists(m_path):
        with open(m_path) as mf:
            c_manifest = json.load(mf)
        for r_entry in c_manifest.get('relations', []):
            if r_entry.get('verification_tier') == 'FAILED':
                failed_indices.add(r_entry.get('rank'))

# Select best non-redundant representative per group
pruned_relations = []
for mset, items in multiset_groups.items():
    clean_items = [it for it in items if it['index'] not in overwriting_indices and it['index'] not in failed_indices]
    if clean_items:
        best_rep = max(clean_items, key=lambda x: x['fitness'])
        if 'genes' not in best_rep or not best_rep['genes']:
            json_path = os.path.join('mr_library', 'generated_mrs', best_rep['json_file'])
            if os.path.exists(json_path):
                with open(json_path) as jf:
                    detail = json.load(jf)
                best_rep['genes'] = detail.get('genes', [])
        pruned_relations.append(best_rep)

pruned_relations.sort(key=lambda x: x['fitness'], reverse=True)
for i, r in enumerate(pruned_relations, 1):
    r['pruned_rank'] = i

pruned_catalog = {
    'total_essential_relations': len(pruned_relations),
    'original_count': len(rels),
    'redundant_filtered_out': len(rels) - len(pruned_relations),
    'description': 'Curated, non-redundant composite metamorphic relations library optimized for MQT-CC testing.',
    'relations': pruned_relations
}

out_path = 'mr_library/generated_mrs/pruned_essential_catalog.json'
with open(out_path, 'w') as f:
    json.dump(pruned_catalog, f, indent=2)

print(f"Exported {len(pruned_relations)} essential relations to {out_path}")
