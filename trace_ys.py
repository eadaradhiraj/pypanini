import sys
from pypanini import TinantaDerivationEngine
te = TinantaDerivationEngine()

def trace_calls(frame, event, arg):
    if event == "return" and frame.f_code.co_name == "_derive_inner":
        print("RETURNING:", arg)
    return trace_calls

sys.settrace(trace_calls)
res, _ = te.derive('ji', sanadi='yananta', _force_pada='Atmanepadi', dhatu_id='01.1096')
print("FINAL", res)
