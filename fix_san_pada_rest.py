import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

# Fix liw
old_liw = """            if lakara == "liw":
                # periphrastic AYcakAra / AYcakre (over-generate for Ur variants)
                cands=[]
                for s in s_stems:
                    cands += [s + "AYcakAra", s + "AYcakre", s + "AmAsa", s + "AmAse", s + "AmbaBUva", s + "AmbaBUve"]
                return list(dict.fromkeys(cands)), log"""

new_liw = """            if lakara == "liw":
                cands=[]
                for s in s_stems:
                    if pada in ("parasmEpadi", "ubhayapadi"):
                        cands += [s + "AYcakAra", s + "AmAsa", s + "AmbaBUva"]
                    if pada in ("Atmanepadi", "ubhayapadi"):
                        cands += [s + "AYcakre", s + "AmAse", s + "AmbaBUve"]
                return list(dict.fromkeys(cands)), log"""
content = content.replace(old_liw, new_liw)

# Fix luw
old_luw = """            if lakara == "luw":
                cands=[]
                for s in s_stems:
                    tbl_p = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAsi"],("madhyama","dvi"):[s+"itAsTaH"],("madhyama","bahu"):[s+"itAsTa"],("uttama","eka"):[s+"itAsmi"],("uttama","dvi"):[s+"itAsvaH"],("uttama","bahu"):[s+"itAsmaH"]}
                    tbl_a = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAse"],("madhyama","dvi"):[s+"itAsATe"],("madhyama","bahu"):[s+"itADve"],("uttama","eka"):[s+"itAhe"],("uttama","dvi"):[s+"itAsvahe"],("uttama","bahu"):[s+"itAsmahe"]}
                    cands += tbl_p.get((purusha, vacana), [s+"itA"])
                    cands += tbl_a.get((purusha, vacana), [s+"itA"])
                return list(dict.fromkeys(cands)), log"""

new_luw = """            if lakara == "luw":
                cands=[]
                for s in s_stems:
                    tbl_p = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAsi"],("madhyama","dvi"):[s+"itAsTaH"],("madhyama","bahu"):[s+"itAsTa"],("uttama","eka"):[s+"itAsmi"],("uttama","dvi"):[s+"itAsvaH"],("uttama","bahu"):[s+"itAsmaH"]}
                    tbl_a = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAse"],("madhyama","dvi"):[s+"itAsATe"],("madhyama","bahu"):[s+"itADve"],("uttama","eka"):[s+"itAhe"],("uttama","dvi"):[s+"itAsvahe"],("uttama","bahu"):[s+"itAsmahe"]}
                    if pada in ("parasmEpadi", "ubhayapadi"):
                        cands += tbl_p.get((purusha, vacana), [s+"itA"])
                    if pada in ("Atmanepadi", "ubhayapadi"):
                        cands += tbl_a.get((purusha, vacana), [s+"itA"])
                return list(dict.fromkeys(cands)), log"""
content = content.replace(old_luw, new_luw)

with open('pypanini/tinanta.py', 'w') as f:
    f.write(content)
