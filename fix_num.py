import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

old_block = """            elif base_wo_i and base_wo_i[-1] not in "aAiIuUfFxXeEoO" and base_wo_i[-1] not in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "R", "p", "P", "b", "B"):
                # ... except velar/palatal/retroflex/labial-coda idit (agi~->agi not angi: formations assimilate per-formation instead)
                # Panini 8.3.24 naS cApadAntasya jhali: before sibilants and h, num is M; before kz, num is N
                # kz-cluster: nasal homorganic with k, insert before kz (kAkz->kANkz)
                if base_wo_i.endswith("kz"):
                    with_n = base_wo_i[:-2] + "N" + "kz" if len(base_wo_i) >= 2 else base_wo_i + "N"
                    clean = with_n
                elif base_wo_i[-1:] in ("s", "S", "z", "h"):
                    _nn2 = "M"
                    with_n = base_wo_i[:-1] + _nn2 + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + _nn2
                    clean = with_n
                elif base_wo_i[-1:] == "v" and ("r" in clean or "f" in clean):
                    _nn2 = "R"
                    with_n = base_wo_i[:-1] + _nn2 + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + _nn2
                    clean = with_n
                else:
                    _nn2 = "n"
                    with_n = base_wo_i[:-1] + _nn2 + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + _nn2
                    clean = with_n"""

new_block = """            elif base_wo_i and base_wo_i[-1] not in "aAiIuUfFxXeEoO" and base_wo_i[-1] not in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "R", "p", "P", "b", "B"):
                # Insert num after the last vowel (midaco 'ntyAt paraH)
                _sv = [i for i, ch in enumerate(base_wo_i) if ch in "aAiIuUfFxXeEoO"]
                if _sv:
                    _lv_idx = _sv[-1]
                    _pre = base_wo_i[:_lv_idx+1]
                    _post = base_wo_i[_lv_idx+1:]
                    _next_c = _post[0] if _post else ""
                    if _next_c in ("k", "K", "g", "G"): _nn2 = "N"
                    elif _next_c in ("c", "C", "j", "J"): _nn2 = "Y"
                    elif _next_c in ("w", "W", "q", "Q", "R"): _nn2 = "R"
                    elif _next_c in ("p", "P", "b", "B"): _nn2 = "m"
                    elif _next_c in ("s", "S", "z", "h"): _nn2 = "M"
                    elif _next_c == "v" and ("r" in base_wo_i or "f" in base_wo_i): _nn2 = "R"
                    else: _nn2 = "n"
                    clean = _pre + _nn2 + _post
                else:
                    clean = base_wo_i"""

content = content.replace(old_block, new_block)
with open('pypanini/tinanta.py', 'w') as f:
    f.write(content)
