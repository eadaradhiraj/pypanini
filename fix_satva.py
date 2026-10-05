with open("pypanini/phonetics.py", "r") as f:
    k = f.read()

old_block = """    inner = prefixes[-1]
    if inner.endswith(("i", "u", "I", "U")) and form.startswith("s") and len(form) > 1 and form[1] in "aAiIuUfFeEoOyvr":
        # Additional Paninian blocks (e.g. 8.3.111 sAts-padAdyoH blocks padanta s and sAt)
        # We assume inner sandhi has already handled word-internal satva, this is strictly upasarga-boundary.
        if form.startswith("sAt"):
            pass
        else:
            form = "z" + form[1:]"""

new_block = """    inner = prefixes[-1]
    if inner.endswith(("i", "u", "I", "U")):
        if form.startswith("s") and len(form) > 1 and form[1] in "aAiIuUfFeEoOyvr":
            if not form.startswith("sAt"):
                form = "z" + form[1:]
        elif (form.startswith("a") or form.startswith("A")) and len(form) > 2 and form[1] == "s":
            # Panini 8.3.71: satva applies even with aT augment (a/A) for specific roots (8.3.65)
            # sedha (siD), sica (sic), svaYj (svaYj), saYj (saYj), sthA, stu, su.
            core = form[2:]
            # sedha -> eD, iD; sica -> iYc, ec, ic; svaYj -> vaYj, vaK; saYj -> aYj, aNk
            # stu -> tu, to, tAv; su -> un, uv, O, Av
            if core.startswith(("eD", "iD", "iYc", "ec", "ic", "vaYj", "vaK", "aYj", "aNk", "tu", "to", "wO", "tAv", "un", "uv", "Av", "O")):
                form = form[0] + "z" + form[2:]"""

k = k.replace(old_block, new_block)
with open("pypanini/phonetics.py", "w") as f: f.write(k)
print("Fixed satva!")
