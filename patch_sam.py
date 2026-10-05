with open("pypanini/phonetics.py", "r") as f:
    content = f.read()

old_sam = """    if p_end == "m" and prefix == "sam":
        if f_start in "kKgG": return prefix[:-1] + "N" + form
        if f_start in "cCjJ": return prefix[:-1] + "Y" + form
        if f_start in "wWqQ": return prefix[:-1] + "R" + form
        if f_start in "tTdD": return prefix[:-1] + "n" + form
        if f_start in "pPbB": return prefix[:-1] + "m" + form
        if f_start in "yrlvSzsh": return prefix[:-1] + "M" + form"""

new_sam = """    if p_end == "m" and prefix == "sam":
        base_M = prefix[:-1] + "M" + form
        if f_start in "kKgG": return [base_M, prefix[:-1] + "N" + form]
        if f_start in "cCjJ": return [base_M, prefix[:-1] + "Y" + form]
        if f_start in "wWqQ": return [base_M, prefix[:-1] + "R" + form]
        if f_start in "tTdD": return [base_M, prefix[:-1] + "n" + form]
        if f_start in "pPbB": return [base_M, prefix[:-1] + "m" + form]
        if f_start in "yrlvSzsh": return base_M"""

content = content.replace(old_sam, new_sam)

with open("pypanini/phonetics.py", "w") as f:
    f.write(content)
print("Patched sam!")
