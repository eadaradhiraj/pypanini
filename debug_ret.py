import sys
sys.settrace(lambda frame, event, arg: print(event, frame.f_code.co_name, frame.f_lineno) if event == "return" and frame.f_code.co_name == "_derive_inner" else None)
from pypanini import TinantaDerivationEngine
te = TinantaDerivationEngine()
te.derive('ji', sanadi='yananta', _force_pada='Atmanepadi', dhatu_id='01.1096')
