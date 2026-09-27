import sys
from pypanini.tinanta import TinantaDerivationEngine
def trace(f,e,a):
    if e=='line' and f.f_code.co_name == 'derive' and 3480 <= f.f_lineno <= 5466:
        r = f.f_locals.get('redup')
        c = f.f_locals.get('clean')
        print(f.f_lineno, 'clean=', c, 'redup=', r)
    return trace
sys.settrace(trace)
TE = TinantaDerivationEngine()
TE.derive('zas', 'liw', 'prathama', 'eka', None, '', '02.0074')
sys.settrace(None)
