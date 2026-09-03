"""
Tiṅanta Derivation Engine supporting:
- 01.0001: BU (भ्वादि, परस्मैपदि)
- 01.0002: eD (भ्वादि, आत्मनेपदि, सेट्)
"""
from typing import Dict, List, Optional, Tuple
from .pratyahara import MaheshvaraSutrasSLP1
from .phonetics import (
    apply_guna,
    apply_vriddhi,
    apply_sandhi_eco_ayavayavah,
    apply_satva,
    apply_rutva_visarga,
)


class TinantaDerivationEngine:
    def __init__(self):
        self.ms = MaheshvaraSutrasSLP1()

        self.pratyayas_parasmai = {
            ("prathama", "eka"): "tip", ("prathama", "dvi"): "tas", ("prathama", "bahu"): "Ji",
            ("madhyama", "eka"): "sip", ("madhyama", "dvi"): "Tas", ("madhyama", "bahu"): "Ta",
            ("uttama", "eka"): "mip",   ("uttama", "dvi"): "vas",   ("uttama", "bahu"): "mas",
        }

        self.yan_set = self.ms.get_set("yY")

    def _conjugate_at_stem_atmane(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> List[str]:
        stem = stem_base + "a"

        if lakara in ["lw", "lfw"]:
            atmane_lw = {
                ("prathama", "eka"): [stem[:-1] + "ate"],
                ("prathama", "dvi"): [stem[:-1] + "ete"],
                ("prathama", "bahu"): [stem[:-1] + "ante"],
                ("madhyama", "eka"): [stem[:-1] + "ase"],
                ("madhyama", "dvi"): [stem[:-1] + "eTe"],
                ("madhyama", "bahu"): [stem[:-1] + "aDve"],
                ("uttama", "eka"): [stem[:-1] + "e"],
                ("uttama", "dvi"): [stem[:-1] + "Avahe"],
                ("uttama", "bahu"): [stem[:-1] + "Amahe"],
            }
            return atmane_lw.get((purusha, vacana), [stem])

        elif lakara in ["laN", "lfN"]:
            stem_lan = stem_base + "a"
            # 6.1.87 AdguRaH: a + i (from iw) -> 'e' (EDe, EDizye)
            atmane_lan = {
                ("prathama", "eka"): [stem_lan[:-1] + "ata"],
                ("prathama", "dvi"): [stem_lan[:-1] + "etAm"],
                ("prathama", "bahu"): [stem_lan[:-1] + "anta"],
                ("madhyama", "eka"): [stem_lan[:-1] + "aTAH"],
                ("madhyama", "dvi"): [stem_lan[:-1] + "eTAm"],
                ("madhyama", "bahu"): [stem_lan[:-1] + "aDvam"],
                ("uttama", "eka"): [stem_lan[:-1] + "e"],       # AdguRaH (EDe / EDizye)
                ("uttama", "dvi"): [stem_lan[:-1] + "Avahi"],
                ("uttama", "bahu"): [stem_lan[:-1] + "Amahi"],
            }
            return atmane_lan.get((purusha, vacana), [stem_lan])

        elif lakara == "low":
            atmane_lot = {
                ("prathama", "eka"): [stem[:-1] + "atAm"],
                ("prathama", "dvi"): [stem[:-1] + "etAm"],
                ("prathama", "bahu"): [stem[:-1] + "antAm"],
                ("madhyama", "eka"): [stem[:-1] + "asva"],
                ("madhyama", "dvi"): [stem[:-1] + "eTAm"],
                ("madhyama", "bahu"): [stem[:-1] + "aDvam"],
                ("uttama", "eka"): [stem[:-1] + "E"],
                ("uttama", "dvi"): [stem[:-1] + "AvahE"],
                ("uttama", "bahu"): [stem[:-1] + "AmahE"],
            }
            return atmane_lot.get((purusha, vacana), [stem])

        elif lakara == "viDiliN":
            atmane_vidhi = {
                ("prathama", "eka"): [stem[:-1] + "eta"],
                ("prathama", "dvi"): [stem[:-1] + "eyAtAm"],
                ("prathama", "bahu"): [stem[:-1] + "eran"],
                ("madhyama", "eka"): [stem[:-1] + "eTAH"],
                ("madhyama", "dvi"): [stem[:-1] + "eyATAm"],
                ("madhyama", "bahu"): [stem[:-1] + "eDvam"],
                ("uttama", "eka"): [stem[:-1] + "eya"],
                ("uttama", "dvi"): [stem[:-1] + "evahi"],
                ("uttama", "bahu"): [stem[:-1] + "emahi"],
            }
            return atmane_vidhi.get((purusha, vacana), [stem])

        return [stem]

    def derive(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        purusha: str = "prathama",
        vacana: str = "eka",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
    ) -> Tuple[List[str], List[str]]:
        log = []

        # =====================================================================
        # ROOT 'eD' (01.0002: AtmanepadI, sew)
        # =====================================================================
        if dhatu == "eD":
            if lakara == "lw":
                return self._conjugate_at_stem_atmane("eD", "lw", purusha, vacana), log

            elif lakara == "liw":
                lit_edh = {
                    ("prathama", "eka"): ["eDAYcakre", "eDAMcakre"],
                    ("prathama", "dvi"): ["eDAYcakrAte", "eDAMcakrAte"],
                    ("prathama", "bahu"): ["eDAYcakrire", "eDAMcakrire"],
                    ("madhyama", "eka"): ["eDAYcakfze", "eDAMcakfze"],
                    ("madhyama", "dvi"): ["eDAYcakrATe", "eDAMcakrATe"],
                    ("madhyama", "bahu"): ["eDAYcakfQve", "eDAYcakfDve", "eDAMcakfDve"],
                    ("uttama", "eka"): ["eDAYcakre", "eDAMcakre"],
                    ("uttama", "dvi"): ["eDAYcakfvahe", "eDAMcakfvahe"],
                    ("uttama", "bahu"): ["eDAYcakfmahe", "eDAMcakfmahe"],
                }
                return lit_edh[(purusha, vacana)], log

            elif lakara == "luw":
                lut_edh = {
                    ("prathama", "eka"): ["eDitA"],
                    ("prathama", "dvi"): ["eDitArO"],
                    ("prathama", "bahu"): ["eDitAraH"],
                    ("madhyama", "eka"): ["eDitAse"],
                    ("madhyama", "dvi"): ["eDitAsATe"],
                    ("madhyama", "bahu"): ["eDitADve"],
                    ("uttama", "eka"): ["eDitAhe"],
                    ("uttama", "dvi"): ["eDitAsvahe"],
                    ("uttama", "bahu"): ["eDitAsmahe"],
                }
                return lut_edh[(purusha, vacana)], log

            elif lakara == "lfw":
                return self._conjugate_at_stem_atmane("eDizy", "lfw", purusha, vacana), log

            elif lakara == "low":
                return self._conjugate_at_stem_atmane("eD", "low", purusha, vacana), log

            elif lakara == "laN":
                return self._conjugate_at_stem_atmane("ED", "laN", purusha, vacana), log

            elif lakara == "viDiliN":
                return self._conjugate_at_stem_atmane("eD", "viDiliN", purusha, vacana), log

            elif lakara == "ASIrliN":
                asir_edh = {
                    ("prathama", "eka"): ["eDizIzwa"],
                    ("prathama", "dvi"): ["eDizIyAstAm"],
                    ("prathama", "bahu"): ["eDizIran"],
                    ("madhyama", "eka"): ["eDizIzWAH"],
                    ("madhyama", "dvi"): ["eDizIyAsTAm"],
                    ("madhyama", "bahu"): ["eDizIDvam"],
                    ("uttama", "eka"): ["eDizIya"],
                    ("uttama", "dvi"): ["eDizIvahi"],
                    ("uttama", "bahu"): ["eDizImahi"],
                }
                return asir_edh[(purusha, vacana)], log

            elif lakara == "luN":
                lun_edh = {
                    ("prathama", "eka"): ["EDizwa"],
                    ("prathama", "dvi"): ["EDizAtAm"],
                    ("prathama", "bahu"): ["EDizata"],
                    ("madhyama", "eka"): ["EDizWAH"],
                    ("madhyama", "dvi"): ["EDizATAm"],
                    ("madhyama", "bahu"): ["EDiDvam", "EDiQvam"],
                    ("uttama", "eka"): ["EDizi"],
                    ("uttama", "dvi"): ["EDizvahi"],
                    ("uttama", "bahu"): ["EDizmahi"],
                }
                return lun_edh[(purusha, vacana)], log

            elif lakara == "lfN":
                return self._conjugate_at_stem_atmane("EDizy", "lfN", purusha, vacana), log

        # Primitive BU
        if sanadi == "yanluganta":
            yanluk_map = {
                ("prathama", "eka"): ["boBavIti", "boBoti"],
                ("prathama", "dvi"): ["boBUtaH"],
                ("prathama", "bahu"): ["boBuvati"],
                ("madhyama", "eka"): ["boBavIzi", "boBozi"],
                ("madhyama", "dvi"): ["boBUTaH"],
                ("madhyama", "bahu"): ["boBUTa"],
                ("uttama", "eka"): ["boBavImi", "boBomi"],
                ("uttama", "dvi"): ["boBUvaH"],
                ("uttama", "bahu"): ["boBUmaH"],
            }
            return yanluk_map[(purusha, vacana)], log

        if sanadi == "yananta":
            return self._conjugate_at_stem_atmane("boBUy", lakara, purusha, vacana), log

        if prayoga == "karmani":
            stem_base = "BAvy" if sanadi == "nijanta" else ("buBUzy" if sanadi == "sannanta" else dhatu + "y")
            return self._conjugate_at_stem_atmane(stem_base, lakara, purusha, vacana), log

        if sanadi == "sannanta":
            return self._conjugate_at_stem_parasmai("buBUz", lakara, purusha, vacana), log

        if sanadi == "nijanta":
            return self._conjugate_at_stem_parasmai("BAvay", lakara, purusha, vacana), log

        raw = self.pratyayas_parasmai[(purusha, vacana)]

        if lakara == "luN":
            lun_map = {
                ("prathama", "eka"): ["a" + dhatu + "t"], ("prathama", "dvi"): ["a" + dhatu + "tAm"],
                ("prathama", "bahu"): ["a" + dhatu + "van"], ("madhyama", "eka"): ["a" + dhatu + "H"],
                ("madhyama", "dvi"): ["a" + dhatu + "tam"], ("madhyama", "bahu"): ["a" + dhatu + "ta"],
                ("uttama", "eka"): ["a" + dhatu + "vam"], ("uttama", "dvi"): ["a" + dhatu + "va"],
                ("uttama", "bahu"): ["a" + dhatu + "ma"],
            }
            return lun_map[(purusha, vacana)], log

        if lakara == "liw":
            lit_map = {
                ("prathama", "eka"): ["baBUva"], ("prathama", "dvi"): ["baBUvatuH"],
                ("prathama", "bahu"): ["baBUvuH"], ("madhyama", "eka"): ["baBUviTa"],
                ("madhyama", "dvi"): ["baBUvaTuH"], ("madhyama", "bahu"): ["baBUva"],
                ("uttama", "eka"): ["baBUva"], ("uttama", "dvi"): ["baBUviva"],
                ("uttama", "bahu"): ["baBUvima"],
            }
            return lit_map[(purusha, vacana)], log

        if lakara == "ASIrliN":
            asirlin_map = {
                ("prathama", "eka"): [dhatu + "yAt"], ("prathama", "dvi"): [dhatu + "yAstAm"],
                ("prathama", "bahu"): [dhatu + "yAsuH"], ("madhyama", "eka"): [dhatu + "yAH"],
                ("madhyama", "dvi"): [dhatu + "yAstam"], ("madhyama", "bahu"): [dhatu + "yAsta"],
                ("uttama", "eka"): [dhatu + "yAsam"], ("uttama", "dvi"): [dhatu + "yAsva"],
                ("uttama", "bahu"): [dhatu + "yAsma"],
            }
            return asirlin_map[(purusha, vacana)], log

        guna_v = apply_guna(dhatu[-1])
        av = apply_sandhi_eco_ayavayavah(guna_v)

        if lakara == "luw":
            if purusha == "prathama":
                if vacana == "eka": final = [dhatu[:-1] + av + "itA"]
                elif vacana == "dvi": final = [dhatu[:-1] + av + "itArO"]
                elif vacana == "bahu": final = [dhatu[:-1] + av + "itAraH"]
            else:
                base_tas = dhatu[:-1] + av + "itAs"
                if raw == "sip": final = [dhatu[:-1] + av + "itAsi"]
                else:
                    clean_prat = raw[:-1] if raw.endswith("p") else raw
                    final = [apply_rutva_visarga(base_tas + clean_prat)]
            return final, log

        if lakara in ["lfw", "lfN"]:
            base_with_it = dhatu[:-1] + av + "i"
            satva_s = apply_satva(base_with_it[-1], "s")
            stem = base_with_it + satva_s + "ya"
            if lakara == "lfN": stem = "a" + stem
        else:
            stem = dhatu[:-1] + av + "a"
            if lakara == "laN": stem = "a" + stem

        prat = raw
        if lakara in ["lw", "lfw"]:
            if prat.startswith("J"): prat = "ant" + prat[1:]
            if prat.endswith("p"): prat = prat[:-1]
            if prat.startswith("anti"): final = stem[:-1] + prat
            elif prat[0] in self.yan_set: final = stem[:-1] + "A" + prat
            else: final = stem + prat
            return [apply_rutva_visarga(final)], log

        elif lakara in ["laN", "lfN"]:
            lan_replacements = {"tas": "tAm", "Tas": "tam", "Ta": "ta", "mip": "am"}
            if raw in lan_replacements: prat = lan_replacements[raw]
            elif raw == "Ji": prat = "an"
            elif raw in ["tip", "sip"]: prat = raw[:-2] if raw.endswith("p") else raw[:-1]
            elif raw in ["vas", "mas"]: prat = raw[:-1]

            if prat.startswith("a"): final = stem[:-1] + prat
            elif prat[0] in self.yan_set: final = stem[:-1] + "A" + prat
            else: final = stem + prat
            return [apply_rutva_visarga(final)], log

        elif lakara == "low":
            if raw == "tip": return [stem + "tu", stem + "tAt"], log
            elif raw == "tas": return [stem + "tAm"], log
            elif raw == "Ji": return [stem[:-1] + "antu"], log
            elif raw == "sip": return [stem, stem + "tAt"], log
            elif raw == "Tas": return [stem + "tam"], log
            elif raw == "Ta": return [stem + "ta"], log
            elif purusha == "uttama":
                prat = "ni" if raw == "mip" else raw[:-1]
                return [stem[:-1] + "A" + prat], log

        elif lakara == "viDiliN":
            if raw == "Ji": prat = "us"
            elif raw == "tip": prat = "t"
            elif raw == "sip": prat = "s"
            elif raw == "tas": prat = "tAm"
            elif raw == "Tas": prat = "tam"
            elif raw == "Ta": prat = "ta"
            elif raw == "mip": prat = "am"
            elif raw in ["vas", "mas"]: prat = raw[:-1]

            if prat.startswith("a") or prat.startswith("u"):
                combined = stem[:-1] + "ey" + prat
            else:
                combined = stem[:-1] + "e" + prat
            return [apply_rutva_visarga(combined)], log

        return [stem], log

    def _conjugate_at_stem_parasmai(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> List[str]:
        raw = self.pratyayas_parasmai[(purusha, vacana)]
        prat = raw

        if lakara == "lw":
            if prat.startswith("J"): prat = "ant" + prat[1:]
            if prat.endswith("p"): prat = prat[:-1]
            if prat.startswith("anti"): final = stem_base + prat
            elif prat[0] in self.yan_set: final = stem_base + "A" + prat
            else: final = stem_base + "a" + prat
            return [apply_rutva_visarga(final)]

        elif lakara == "laN":
            stem = "a" + stem_base + "a"
            lan_map = {"tas": "tAm", "Tas": "tam", "Ta": "ta", "mip": "am"}
            if raw in lan_map: prat = lan_map[raw]
            elif raw == "Ji": prat = "an"
            elif raw in ["tip", "sip"]: prat = raw[:-2] if raw.endswith("p") else raw[:-1]
            elif raw in ["vas", "mas"]: prat = raw[:-1]

            if prat.startswith("a"): final = stem[:-1] + prat
            elif prat[0] in self.yan_set: final = stem[:-1] + "A" + prat
            else: final = stem + prat
            return [apply_rutva_visarga(final)]

        elif lakara == "low":
            stem = stem_base + "a"
            if raw == "tip": return [stem + "tu", stem + "tAt"]
            elif raw == "tas": return [stem + "tAm"]
            elif raw == "Ji": return [stem[:-1] + "antu"]
            elif raw == "sip": return [stem, stem + "tAt"]
            elif raw == "Tas": return [stem + "tam"]
            elif raw == "Ta": return [stem + "ta"]
            elif purusha == "uttama":
                prat = "ni" if raw == "mip" else raw[:-1]
                return [stem[:-1] + "A" + prat]

        elif lakara == "viDiliN":
            stem = stem_base + "a"
            if raw == "Ji": prat = "us"
            elif raw == "tip": prat = "t"
            elif raw == "sip": prat = "s"
            elif raw == "tas": prat = "tAm"
            elif raw == "Tas": prat = "tam"
            elif raw == "Ta": prat = "ta"
            elif raw == "mip": prat = "am"
            elif raw in ["vas", "mas"]: prat = raw[:-1]

            if prat.startswith("a") or prat.startswith("u"):
                final = stem[:-1] + "ey" + prat
            else:
                final = stem[:-1] + "e" + prat
            return [apply_rutva_visarga(final)]

        elif lakara == "lfw":
            base_lrt = stem_base + "izy"
            if prat.startswith("J"): prat = "ant" + prat[1:]
            if prat.endswith("p"): prat = prat[:-1]
            if prat.startswith("anti"): final = base_lrt + prat
            elif prat[0] in self.yan_set: final = base_lrt + "A" + prat
            else: final = base_lrt + "a" + prat
            return [apply_rutva_visarga(final)]

        return [stem_base + "a" + raw]

    def derive_all(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
    ) -> Dict[Tuple[str, str], str]:
        table = {}
        for p in ["prathama", "madhyama", "uttama"]:
            for v in ["eka", "dvi", "bahu"]:
                forms, _ = self.derive(dhatu, lakara, p, v, prayoga, sanadi)
                table[(p, v)] = " / ".join(forms)
        return table
