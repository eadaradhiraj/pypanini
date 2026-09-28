import glob, json
import tests.sweep_gana as S
import pypanini.tinanta as T

TE = T.TinantaDerivationEngine()

roots = []
for jf in sorted(glob.glob('skt-morph-data/05/*.json')):
    d = json.load(open(jf))
    fid = d.get('id')
    op = ''
    for it in d.get('info', []):
        if it.get('name') == 'OpadeSikasvarUpam': op = it.get('value')
    clean = T.clean_dhatu_op(op)
    pada = [x['value'] for x in d.get('info', []) if x['name'] == 'padam'][0]
    roots.append((fid, clean, op, pada))

print(f"Loaded {len(roots)} roots in Gana 05:")
for r in roots[:10]:
    print(" ", r)
