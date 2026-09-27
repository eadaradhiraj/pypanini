import sys
from pypanini.krdanta import clean_dhatu_op

def trace_calls(frame, event, arg):
    if event == 'line' and frame.f_code.co_name == 'clean_dhatu_op':
        clean = frame.f_locals.get('clean')
        raw = frame.f_locals.get('raw')
        print(f"Line {frame.f_lineno}: raw={raw}, clean={clean}")
    return trace_calls

sys.settrace(trace_calls)
clean_dhatu_op('jAgf')
sys.settrace(None)
