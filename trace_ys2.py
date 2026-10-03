import sys
import pypanini.tinanta

def trace_lines(frame, event, arg):
    if frame.f_code.co_filename.endswith("tinanta.py") and frame.f_code.co_name == "_derive_inner":
        if "ys" in frame.f_locals:
            ys_val = frame.f_locals["ys"]
            if ys_val == "YAYjya":
                print(f"YS is YAYjya at line {frame.f_lineno}")
    return trace_lines

sys.settrace(trace_lines)
te = pypanini.TinantaDerivationEngine()
te.derive('ji', sanadi='yananta', _force_pada='Atmanepadi', dhatu_id='01.1096')
