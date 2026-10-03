import sys
import pypanini.tinanta

def trace_lines(frame, event, arg):
    if frame.f_code.co_name == "_yan_stem":
        if "c" in frame.f_locals and frame.f_locals["c"] == "ji":
            if event == "return":
                print({k: v for k, v in frame.f_locals.items() if isinstance(v, (str, bool, int))})
    return trace_lines

sys.settrace(trace_lines)
te = pypanini.TinantaDerivationEngine()
te.derive('ji', sanadi='yananta', _force_pada='Atmanepadi', dhatu_id='01.1096')
