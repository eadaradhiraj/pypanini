import json
from pypanini.tinanta import TinantaDerivationEngine
TE = TinantaDerivationEngine()

dhatu = 'cakziN'
dhatu_id = '02.0007'
jp = 'skt-morph-data/02/02.0007.json'

import sys
def trace(f,e,a):
    if e=='call':
        if f.f_code.co_name == 'derive':
            print('derive called with', f.f_locals.get('dhatu'), f.f_locals.get('lakara'), f.f_locals.get('purusha'), f.f_locals.get('vacana'), f.f_locals.get('_force_pada'))
    return trace

sys.settrace(trace)
print("Starting...")
TE.derive(dhatu, 'luw', 'prathama', 'eka', prayoga='kartari', sanadi=None, dhatu_id=dhatu_id, json_path=jp)
sys.settrace(None)
print("Finished!")
