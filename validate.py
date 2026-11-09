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
assert len(a)==45 and len(c)==21 and len(r)==52 and len(e)==44 and len(s)==21
print(f'VALIDATION OK : {len(a)} nœuds ; {sum(x.get("display_in_cards",True) for x in a)} cartes affichées ; {len(c)} positions ; {len(r)} relations ; {len(e)} preuves ; {len(s)} sources URL ; aucune référence cassée.')


# Extension du 9 novembre 2026 : 5e onglet et distinction opposition régionale / locale.
from datetime import date
from urllib.parse import urlsplit
import re
timeline=read('data/timeline.json')
audit=read('data/evolution-audit-20261109.json')
T=unique(timeline,'timeline')
assert len(T)==26 and len({x['actor_id'] for x in timeline})==26
assert t['timeline']['default_scope']=='direct'
category_names={x['id'] for x in t['timeline']['categories']}
stance_names={x['id'] for x in t['timeline']['stances']}
claims_by_actor={x['subject_id']:x for x in c}
sources_by_id={x['id']:x for x in s}
ev_by_id={x['id']:x for x in e}
dated=undated=direct=context=0
for x in timeline:
    assert x['actor_id'] in A and x['event_type']=='first_documented_appearance',x['id']
    assert x['category'] in category_names and x['stance'] in stance_names,x['id']
    assert x['stance']==claims_by_actor.get(x['actor_id'],{}).get('value','unknown'),x['id']
    assert x['scope'] in ('direct','context'),x['id']
    assert x['source_ids'] and x['evidence_ids'],x['id']
    for eid in x['evidence_ids']:
        assert eid in E,x['id']
    for sid in x['source_ids']:
        assert sid in S and urlsplit(sources_by_id[sid]['url']).scheme=='https',x['id']
    if x['status']=='confirmed':
        dated+=1
        assert x['date_precision']=='day' and re.fullmatch(r'\d{4}-\d{2}-\d{2}',x['date']),x['id']
        assert date.fromisoformat(x['date'])<=date(2026,11,9),x['id']
        if x['scope']=='direct':direct+=1
        else:context+=1
    else:
        undated+=1
        assert x['status']=='undated' and x['date'] is None and x['date_precision']=='unknown',x['id']

assert (dated,undated,direct,context)==(25,1,15,10)
assert sum(x['stance']=='opposed' and x['scope']=='direct' for x in timeline)==0
regional=[x for x in timeline if x['stance']=='opposed' and x['scope']=='context']
assert len(regional)==1 and regional[0]['actor_id']=='actor_0044'
assert claims_by_actor['actor_0044']['position_scope']=='regional_policy_including_poulainville_not_site_specific'
assert ev_by_id['evidence_0044']['source_id']=='source_0021'
assert sy['opposition_status']['local_collectives_identified']==0
assert sy['opposition_status']['regional_critical_groups_identified']==1
for group in (sy['griefs'],sy['vigilance'],d['milestones'],d['fact_sheet']):
    for item in group:
        assert item['evidence_ids'],item.get('title',item.get('label'))
        for eid in item['evidence_ids']:
            assert eid in E and urlsplit(sources_by_id[ev_by_id[eid]['source_id']]['url']).scheme=='https',eid
for m in d['milestones']:
    if m['period_precision']=='year':assert re.fullmatch(r'\d{4}',m['date'])
    elif m['period_precision']=='month':assert re.fullmatch(r'\d{4}-(0[1-9]|1[0-2])',m['date'])
    else:date.fromisoformat(m['date'])
assert len(d['milestones'])==10 and len(sy['griefs'])==9
page=(root/'apps/cards/index.html').read_text(encoding='utf-8')
for tab in ('carto','griefs','watch','timeline','evolution'):
    assert f'data-tab="{tab}"' in page and f'id="tab-{tab}"' in page,tab
assert len(re.findall(r'data-tab="[^"]+"',page))==5
for name in ('assets/js/evolution.js','assets/css/evolution.css'):
    assert (root/name).is_file(),name
evo=(root/'assets/js/evolution.js').read_text(encoding='utf-8')
for mode in ('new','cumulative','stance'):
    assert f'data-mode="{mode}"' in evo,mode
assert "timeline:'data/timeline.json'" in (root/'assets/js/data-loader.js').read_text(encoding='utf-8')
print(f'EXTENSION OK : {dated} acteurs datés, {undated} sans date, {direct} locaux, {context} de contexte, 9 thèmes, 10 jalons et 5 onglets.')
