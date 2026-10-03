with open("pypanini/phonetics.py", "r") as f:
    content = f.read()

natva_func = """
def apply_natva(word: str) -> str:
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
    return "".join(out)
"""

if "def apply_natva" not in content:
    content = content.replace("def apply_single_upasarga_sandhi", natva_func + "\ndef apply_single_upasarga_sandhi")

old_return = """    # Post-sandhi Natva check for augmented forms (pra + anamat -> prARamat)
    if prefix_str in ("pra", "parA", "nir", "antar", "pari"):
        # If it's something like prAna...
        if form.startswith("prA") and len(form) > 3 and form[3] == "n":
            form = form[:3] + "R" + form[4:]
            
    return form"""

new_return = """    # Post-sandhi general Natva (8.4.1 - 8.4.2)
    # Applies if the prefix has r/z/f (pra, parA, nir, antar, pari, dur, dus, nis).
    # We just pass the whole fused form through the natva engine.
    form = apply_natva(form)
            
    return form"""

content = content.replace(old_return, new_return)

with open("pypanini/phonetics.py", "w") as f:
    f.write(content)
print("Patched Natva")
