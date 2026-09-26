from pypanini.krdanta import KrdantaEngine
import sys

def trace_calls(frame, event, arg):
    if event == "call" and frame.f_code.co_name == "_kta_stem":
        print(f"Calling _kta_stem with: {frame.f_locals}")
    elif event == "return" and frame.f_code.co_name == "_kta_stem":
        print(f"Returning from _kta_stem: {arg}")
    return trace_calls

sys.settrace(trace_calls)
KE = KrdantaEngine()
print(KE.derive_krdanta('SrE', 'kta', None, 'saM', '01.1067'))
sys.settrace(None)
