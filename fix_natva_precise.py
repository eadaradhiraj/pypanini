import re

with open("pypanini/phonetics.py", "r") as f:
    content = f.read()

# Replace apply_natva
old_func = """def apply_natva(word: str) -> str:
    # 8.4.1 - 8.4.2: r/z/f/F followed by n -> R, even if separated by 
    # vowels (aT), gutturals (ku), labials (pu), A, num, visarga.
    # SLP1 vowels: aAiIuUfFeEoO
    # ku: k K g G N
    # pu: p P b B m
    # y, v, r, l, h
    # A simple regex can do this.
    import re
    # We want to find r, z, f, F followed by any combination of allowed interveners, then n.
    # Allowed interveners: [aAiIuUfFeEoOyvrhHkKgGNpPbBm]*
    # Wait, 'r' is in aT/yav. 
    # Let's just implement a left-to-right pass.
    out = []
    cause_seen = False
    allowed_interveners = set("aAiIuUfFeEoOyvhHkKgGNpPbBm" + "M") # M = anusvara (num)
    
    for i, c in enumerate(word):
        if c in ("r", "z", "f", "F"):
            cause_seen = True
            out.append(c)
        elif c == "n" and cause_seen:
            # check if we should apply natva
            # wait, 'n' becomes 'R' only if followed by a vowel or n/m/y/v? 
            # 8.4.1 applies to 'n'. The 'n' must be part of the same pada.
            # Upasarga + root is often treated as same pada for this rule (upasargAd... kftyAcaH etc).
            out.append("R")
            cause_seen = False # reset after applying? No, "pramARAni" -> wait, one cause can trigger multiple? Usually yes, but let's reset for safety or just keep it.
        elif c in allowed_interveners:
            out.append(c)
        else:
            cause_seen = False
            out.append(c)
    return "".join(out)"""

new_func = """def apply_natva(word: str) -> str:
    out = []
    cause_seen = False
    allowed_interveners = set("aAiIuUfFeEoOyvhHkKgGNpPbBm" + "M")
    
    for i, c in enumerate(word):
        if c in ("r", "z", "f", "F"):
            cause_seen = True
            out.append(c)
        elif c == "n" and cause_seen:
            # Prevent natva on padanta 'n' (word-final) and 'nt' (tiNanta endings like anti, antu, SAnac antI)
            is_padanta = (i == len(word) - 1)
            is_nt = (i + 1 < len(word) and word[i+1] == "t")
            if is_padanta or is_nt:
                out.append("n")
            else:
                out.append("R")
        elif c in allowed_interveners:
            out.append(c)
        else:
            cause_seen = False
            out.append(c)
    return "".join(out)"""

content = content.replace(old_func, new_func)

with open("pypanini/phonetics.py", "w") as f:
    f.write(content)
print("Patched Natva precision")
