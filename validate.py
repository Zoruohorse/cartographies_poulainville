import json
from pathlib import Path
root=Path(__file__).resolve().parent
def read(path):return json.loads((root/path).read_text(encoding='utf-8'))
a=read('data/actors.json');c=read('data/claims.json');e=read('data/evidence.json');r=read('data/relations.json');s=read('data/sources.json');t=read('config/taxonomy.json');sy=read('data/synthesis.json');d=read('data/content.json');m=read('data/meta.json')
def unique(rows,label):
    ids=[x['id'] for x in rows];assert len(ids)==len(set(ids)),f'IDs dupliqués dans {label}';return set(ids)
A=unique(a,'acteurs');C=unique(c,'positions');E=unique(e,'preuves');R=unique(r,'relations');S=unique(s,'sources')
assert m['id']=='project_poulainville' and m['id'] in A
for x in a:assert x['categories'] and all(k in t['categories'] for k in x['categories']),x['id']
for x in c:
    assert x['subject_id'] in A and x['project_id'] in A and x['value'] in t['stances'] and x['certainty'] in t['certainty_levels'],x['id']
    assert x['evidence_ids'] and set(x['evidence_ids'])<=E,x['id']
for x in e:
    assert x['source_id'] in S and isinstance(x['text'],str) and x['text'],x['id']
for x in r:
    assert x['source_id'] in A and x['target_id'] in A and x['type'] in t['relation_types'] and x['certainty'] in t['certainty_levels'],x['id']
    assert x['evidence_ids'] and set(x['evidence_ids'])<=E,x['id']
assert all(x['url'].startswith(('https://','http://')) for x in s)
for key in ('griefs','vigilance'):
    assert sy[key] and all(row.get('evidence_ids') and set(row['evidence_ids'])<=E for row in sy[key])
for key in ('fact_sheet','milestones'):
    assert d[key] and all(row.get('evidence_ids') and set(row['evidence_ids'])<=E for row in d[key])
assert len(a)==44 and len(c)==20 and len(r)==51 and len(e)==43 and len(s)==20
print(f'VALIDATION OK : {len(a)} nœuds ; {sum(x.get("display_in_cards",True) for x in a)} cartes affichées ; {len(c)} positions ; {len(r)} relations ; {len(e)} preuves ; {len(s)} sources URL ; aucune référence cassée.')
