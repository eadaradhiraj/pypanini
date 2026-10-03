import sys
sys.settrace(lambda frame, event, arg: print(frame.f_locals.get('clean')) if event == "return" and frame.f_code.co_name == "_yan_stem" else None)
from pypanini import TinantaDerivationEngine
te = TinantaDerivationEngine()
res, _ = te.derive('ji', sanadi='yananta', _force_pada='Atmanepadi', dhatu_id='01.1096')
print(res)
