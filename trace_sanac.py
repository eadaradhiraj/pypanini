import sys
import pypanini.krdanta

def trace_lines(frame, event, arg):
    if frame.f_code.co_name == "_derive_krdanta_inner" and frame.f_locals.get("pratyaya") == "SAnac":
        if event == "return":
            print(f"RETURN at {frame.f_lineno} with value {arg}")
    return trace_lines

sys.settrace(trace_lines)
ke = pypanini.krdanta.KrdantaEngine()
ke.derive_krdanta('ji', pratyaya='SAnac', sanadi=None, upasarga='', dhatu_id='01.1096')
