import re
with open('pypanini/tinanta.py', 'r') as f:
    content = f.read()

# Fix ASIrliN
old_as = """            if lakara == "ASIrliN":
                cands=[]
                for s in s_stems:
                    cands.append(s + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)])
                    cands.append(s + "iz" + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)])
                    base_iz = s + "iz"
                    endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                    cands.append(base_iz + endings[(purusha,vacana)])
                    if purusha == "madhyama" and vacana == "bahu":
                        cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                return list(dict.fromkeys(cands)), log"""

new_as = """            if lakara == "ASIrliN":
                cands=[]
                for s in s_stems:
                    if pada in ("parasmEpadi", "ubhayapadi"):
                        cands.append(s + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)])
                        cands.append(s + "iz" + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)])
                    if pada in ("Atmanepadi", "ubhayapadi"):
                        base_iz = s + "iz"
                        endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                        cands.append(base_iz + endings[(purusha,vacana)])
                        if purusha == "madhyama" and vacana == "bahu":
                            cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                return list(dict.fromkeys(cands)), log"""
content = content.replace(old_as, new_as)

old_lun = """            if lakara == "luN":
                cands=[]
                for s in s_stems:
                    aug_s = _aug(s)
                    tbl = {("prathama","eka"):"It",("prathama","dvi"):"ItAm",("prathama","bahu"):"IzuH",("madhyama","eka"):"IH",("madhyama","dvi"):"Itam",("madhyama","bahu"):"Ita",("uttama","eka"):"Izam",("uttama","dvi"):"Iva",("uttama","bahu"):"Ima"}
                    cands += [aug_s + tbl[(purusha,vacana)], aug_s + "It"]
                    cands += [aug_s + "iz" + tbl[(purusha,vacana)], aug_s + "izIt"]
                    tbl_a = {("prathama","eka"):"izwa",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iQvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                    cands += [aug_s + tbl_a[(purusha,vacana)], aug_s + "izwa"]
                    cands.append((aug_s + tbl_a[(purusha,vacana)]).replace("iQvam", "iDvam"))
                return list(dict.fromkeys(cands)), log"""

new_lun = """            if lakara == "luN":
                cands=[]
                for s in s_stems:
                    aug_s = _aug(s)
                    if pada in ("parasmEpadi", "ubhayapadi"):
                        tbl = {("prathama","eka"):"It",("prathama","dvi"):"ItAm",("prathama","bahu"):"IzuH",("madhyama","eka"):"IH",("madhyama","dvi"):"Itam",("madhyama","bahu"):"Ita",("uttama","eka"):"Izam",("uttama","dvi"):"Iva",("uttama","bahu"):"Ima"}
                        cands += [aug_s + tbl[(purusha,vacana)], aug_s + "It"]
                        cands += [aug_s + "iz" + tbl[(purusha,vacana)], aug_s + "izIt"]
                    if pada in ("Atmanepadi", "ubhayapadi"):
                        tbl_a = {("prathama","eka"):"izwa",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iQvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                        cands += [aug_s + tbl_a[(purusha,vacana)], aug_s + "izwa"]
                        cands.append((aug_s + tbl_a[(purusha,vacana)]).replace("iQvam", "iDvam"))
                return list(dict.fromkeys(cands)), log"""
content = content.replace(old_lun, new_lun)

with open('pypanini/tinanta.py', 'w') as f:
    f.write(content)
