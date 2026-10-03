# Let's draft the sandhi logic and test it standalone first.

def apply_single_upasarga_sandhi(prefix: str, form: str) -> str:
    if not prefix: return form
    
    # Handle "AN" -> "A"
    if prefix == "AN":
        prefix = "A"
    # Actually, some prefixes in json are like "sam", "ud", "nir", "dur"
    # The JSON might have them as "sam", "nir", etc.
    
    p_end = prefix[-1]
    f_start = form[0]
    
    # Consonant-ending prefixes (sam, ud, nir, dur, nis, dus)
    if p_end == "m" and prefix == "sam":
        if f_start in "kKgG": return prefix[:-1] + "N" + form
        if f_start in "cCjJ": return prefix[:-1] + "Y" + form
        if f_start in "wWqQ": return prefix[:-1] + "R" + form
        if f_start in "tTdD": return prefix[:-1] + "n" + form
        if f_start in "pPbB": return prefix[:-1] + "m" + form
        if f_start in "yrlvSzsh": return prefix[:-1] + "M" + form
        return prefix + form
        
    if p_end == "d" and prefix == "ud":
        # ud + sthA -> utthA (dropping s, d->t)
        if form.startswith("sT"): return "utT" + form[2:]
        if form.startswith("sw"): return "uww" + form[2:] # e.g. ud + stambh?
        # char sandhi
        if f_start in "cC": return "uc" + form
        if f_start in "jJ": return "uj" + form
        if f_start in "wW": return "uw" + form
        if f_start in "qQ": return "uq" + form
        if f_start in "lL": return "ul" + form
        if f_start in "kKpPtTsS": return "ut" + form
        return prefix + form

    if p_end == "r" and prefix in ("nir", "dur", "antar"):
        if f_start in "cC": return prefix[:-1] + "S" + form
        if f_start in "wW": return prefix[:-1] + "z" + form
        if f_start in "tT": return prefix[:-1] + "s" + form
        if f_start in "Szs": return prefix[:-1] + "H" + form
        if f_start in "kKpP": return prefix[:-1] + "z" + form # simple approximation, nis/nir before k/p usually becomes z
        if f_start == "r":
            # lengthen previous vowel and drop r
            v = prefix[-2]
            v_long = "A" if v=="a" else "I" if v=="i" else "U" if v=="u" else v
            return prefix[:-2] + v_long + form
        return prefix + form
        
    if p_end in "s" and prefix in ("nis", "dus"):
        if f_start in "cC": return prefix[:-1] + "S" + form
        if f_start in "wW": return prefix[:-1] + "z" + form
        if f_start in "tT": return prefix + form
        if f_start in "kKpP": return prefix[:-1] + "z" + form
        if f_start in "aAiIuUfFeEoOAyvrlh": return prefix[:-1] + "r" + form
        return prefix + form
        
    # Vowel-ending prefixes
    if p_end in "aA" and f_start in "aAiIuUfFeEoOE":
        # Savarna
        if f_start in "aA": return prefix[:-1] + "A" + form[1:]
        # Guna
        if f_start in "iI": return prefix[:-1] + "e" + form[1:]
        if f_start in "uU": return prefix[:-1] + "o" + form[1:]
        # Vriddhi exception for r
        if f_start in "fF": return prefix[:-1] + "Ar" + form[1:]
        # Pararupa for e/o
        if f_start in "eo":
            # If the root is iN/eD and we have augment, the form has E/O.
            # 6.1.94 eNi pararUpam (pra + ejate = prejate).
            return prefix[:-1] + form
        if f_start in "EO":
            # Vriddhi applies (e.g. pra + EData = prEData)
            return prefix[:-1] + form
            
    if p_end in "iI" and f_start in "aAuUfFeEoOEO":
        return prefix[:-1] + "y" + form
    if p_end in "iI" and f_start in "iI":
        return prefix[:-1] + "I" + form[1:]
        
    if p_end in "uU" and f_start in "aAiIfFeEoOEO":
        return prefix[:-1] + "v" + form
    if p_end in "uU" and f_start in "uU":
        return prefix[:-1] + "U" + form[1:]

    # Tuk augment before ch
    if p_end in "aiuA" and f_start == "C":
        # hrasva takes tuk (c) unconditionally. A/mAA takes tuk too.
        return prefix + "c" + form

    # Default concatenation
    return prefix + form

def apply_upasargas(prefix_str: str, form: str) -> str:
    # Handle composite prefixes separated by ';' e.g. "vi;ati" -> ["vi", "ati"]
    # They apply inside-out (right-to-left)
    prefixes = prefix_str.split(";")
    for p in reversed(prefixes):
        form = apply_single_upasarga_sandhi(p, form)
    return form

tests = [
    ("pra", "Bavati"),
    ("pra", "aBavat"),
    ("pra", "EData"),
    ("pra", "ejate"),
    ("vi", "aBavat"),
    ("vi;ati", "eti"),
    ("sam", "gacCati"),
    ("sam", "carati"),
    ("ud", "sTAna"),
    ("nir", "gacCati"),
    ("nir", "roka"),
    ("anu", "eti"),
    ("A", "CAdyate"),
    ("vi", "Cidyate"),
]

for p, f in tests:
    print(f"{p} + {f} -> {apply_upasargas(p, f)}")
