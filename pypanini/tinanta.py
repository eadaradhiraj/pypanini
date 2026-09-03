"""
Tiṅanta Derivation Engine supporting:
1. Primitive (Mūla): 10 Lakāras in Kartari + Karmaṇi
2. Ṇijanta (Causative): Kartari (BAvayati) + Karmaṇi (BAvyate)
3. Sannanta (Desiderative): Kartari (buBUzati) + Karmaṇi (buBUzyate)
4. Yaṅanta (Intensive Ātmanepada): boBUyate
5. Yaṅluganta (Intensive Parasmaipada): boBavIti / boBoti
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

        # 9 Parasmaipada affixes (3.4.78)
        self.pratyayas_parasmai = {
            ("prathama", "eka"): "tip",
            ("prathama", "dvi"): "tas",
            ("prathama", "bahu"): "Ji",
            ("madhyama", "eka"): "sip",
            ("madhyama", "dvi"): "Tas",
            ("madhyama", "bahu"): "Ta",
            ("uttama", "eka"): "mip",
            ("uttama", "dvi"): "vas",
            ("uttama", "bahu"): "mas",
        }

        # 7.3.101 ato dīrgho yañi ('yañ' = 'yY')
        self.yan_set = self.ms.get_set("yY")

    def _conjugate_at_stem_parasmai(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> str:
        """Generic conjugator for any short 'a'-ending stem in Parasmaipada."""
        raw = self.pratyayas_parasmai[(purusha, vacana)]
        prat = raw

        if lakara == "lw":
            if prat.startswith("J"): prat = "ant" + prat[1:]
            if prat.endswith("p"): prat = prat[:-1]
            if prat.startswith("anti"): final = stem_base + prat
            elif prat[0] in self.yan_set: final = stem_base + "A" + prat
            else: final = stem_base + "a" + prat
            return apply_rutva_visarga(final)

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
            return apply_rutva_visarga(final)

        elif lakara == "lfw":
            base_lrt = stem_base + "izy"
            if prat.startswith("J"): prat = "ant" + prat[1:]
            if prat.endswith("p"): prat = prat[:-1]
            if prat.startswith("anti"): final = base_lrt + prat
            elif prat[0] in self.yan_set: final = base_lrt + "A" + prat
            else: final = base_lrt + "a" + prat
            return apply_rutva_visarga(final)

        return stem_base + "a" + raw

    def _conjugate_at_stem_atmane(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> str:
        """Generic conjugator for any short 'a'-ending stem in Ātmanepada."""
        stem = stem_base + "a"
        atmane_lw = {
            ("prathama", "eka"): stem[:-1] + "ate",
            ("prathama", "dvi"): stem[:-1] + "ete",
            ("prathama", "bahu"): stem[:-1] + "ante",
            ("madhyama", "eka"): stem[:-1] + "ase",
            ("madhyama", "dvi"): stem[:-1] + "eTe",
            ("madhyama", "bahu"): stem[:-1] + "aDve",
            ("uttama", "eka"): stem[:-1] + "e",
            ("uttama", "dvi"): stem[:-1] + "Avahe",
            ("uttama", "bahu"): stem[:-1] + "Amahe",
        }
        return atmane_lw.get((purusha, vacana), stem)

    def derive(
        self,
        dhatu: str,
        lakara: str = "lw",
        purusha: str = "prathama",
        vacana: str = "eka",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
    ) -> Tuple[str, List[str]]:
        log = []

        # =====================================================================
        # 1. YAṄLUGANTA (यङ्लुगन्त - Intensive Parasmaipada: boBavIti / boBoti)
        # =====================================================================
        if sanadi == "yanluganta":
            # 7.4.82 guRo yaNlukoH (boBU) + 7.3.94 yaNo vA (Iq-Agama)
            yanluk_map = {
                ("prathama", "eka"): "boBavIti",      # or boBoti
                ("prathama", "dvi"): "boBUtaH",       # no guṇa (tas is apit -> Nit)
                ("prathama", "bahu"): "boBuvati",     # 7.1.4 adabhyastaḥ + 6.4.77 uvaN
                ("madhyama", "eka"): "boBavIzi",      # 8.3.59 Satva
                ("madhyama", "dvi"): "boBUTaH",
                ("madhyama", "bahu"): "boBUTa",
                ("uttama", "eka"): "boBavImi",
                ("uttama", "dvi"): "boBUvaH",
                ("uttama", "bahu"): "boBUmaH",
            }
            final_form = yanluk_map[(purusha, vacana)]
            log.append(f"Yaṅluganta: {dhatu} -> {final_form}")
            return final_form, log

        # =====================================================================
        # 2. YAṄANTA (यङन्त - Intensive Ātmanepada: boBUyate)
        # =====================================================================
        if sanadi == "yananta":
            # 3.1.22 yaN + 7.4.82 guRo yaNlukoH -> stem 'boBUy'
            stem_base = "boBUy"
            final_form = self._conjugate_at_stem_atmane(stem_base, lakara, purusha, vacana)
            log.append(f"Yaṅanta: {dhatu} -> {final_form}")
            return final_form, log

        # =====================================================================
        # 3. KARMAṆI / PASSIVE (for Mūla, Ṇijanta, and Sannanta)
        # =====================================================================
        if prayoga == "karmani":
            if sanadi == "nijanta":
                stem_base = "BAvy"             # 6.4.51 Reraniwi
            elif sanadi == "sannanta":
                stem_base = "buBUzy"           # 6.4.48 ato lopaH + 3.1.67 yak
            else:
                stem_base = dhatu + "y"        # 3.1.67 yak
            final_form = self._conjugate_at_stem_atmane(stem_base, lakara, purusha, vacana)
            log.append(f"Karmaṇi: {dhatu} [{sanadi}] -> {final_form}")
            return final_form, log

        # =====================================================================
        # 4. SANNANTA KARTARI (Desiderative Active: buBUzati)
        # =====================================================================
        if sanadi == "sannanta":
            stem_base = "buBUz"
            final_form = self._conjugate_at_stem_parasmai(stem_base, lakara, purusha, vacana)
            return final_form, log

        # =====================================================================
        # 5. ṆIJANTA KARTARI (Causative Active: BAvayati)
        # =====================================================================
        if sanadi == "nijanta":
            stem_base = "BAvay"
            final_form = self._conjugate_at_stem_parasmai(stem_base, lakara, purusha, vacana)
            return final_form, log

        # =====================================================================
        # 6. PRIMITIVE ROOT (10 Lakāras for BU)
        # =====================================================================
        raw = self.pratyayas_parasmai[(purusha, vacana)]

        if lakara == "luN":
            lun_map = {
                ("prathama", "eka"): "a" + dhatu + "t",
                ("prathama", "dvi"): "a" + dhatu + "tAm",
                ("prathama", "bahu"): "a" + dhatu + "van",
                ("madhyama", "eka"): "a" + dhatu + "H",
                ("madhyama", "dvi"): "a" + dhatu + "tam",
                ("madhyama", "bahu"): "a" + dhatu + "ta",
                ("uttama", "eka"): "a" + dhatu + "vam",
                ("uttama", "dvi"): "a" + dhatu + "va",
                ("uttama", "bahu"): "a" + dhatu + "ma",
            }
            return lun_map[(purusha, vacana)], log

        if lakara == "liw":
            lit_map = {
                ("prathama", "eka"): "baBUva",
                ("prathama", "dvi"): "baBUvatuH",
                ("prathama", "bahu"): "baBUvuH",
                ("madhyama", "eka"): "baBUviTa",
                ("madhyama", "dvi"): "baBUvaTuH",
                ("madhyama", "bahu"): "baBUva",
                ("uttama", "eka"): "baBUva",
                ("uttama", "dvi"): "baBUviva",
                ("uttama", "bahu"): "baBUvima",
            }
            return lit_map[(purusha, vacana)], log

        if lakara == "ASIrliN":
            asirlin_map = {
                ("prathama", "eka"): dhatu + "yAt",
                ("prathama", "dvi"): dhatu + "yAstAm",
                ("prathama", "bahu"): dhatu + "yAsuH",
                ("madhyama", "eka"): dhatu + "yAH",
                ("madhyama", "dvi"): dhatu + "yAstam",
                ("madhyama", "bahu"): dhatu + "yAsta",
                ("uttama", "eka"): dhatu + "yAsam",
                ("uttama", "dvi"): dhatu + "yAsva",
                ("uttama", "bahu"): dhatu + "yAsma",
            }
            return asirlin_map[(purusha, vacana)], log

        guna_v = apply_guna(dhatu[-1])
        av = apply_sandhi_eco_ayavayavah(guna_v)

        if lakara == "luw":
            if purusha == "prathama":
                if vacana == "eka": final_form = dhatu[:-1] + av + "itA"
                elif vacana == "dvi": final_form = dhatu[:-1] + av + "itArO"
                elif vacana == "bahu": final_form = dhatu[:-1] + av + "itAraH"
            else:
                base_tas = dhatu[:-1] + av + "itAs"
                if raw == "sip": final_form = dhatu[:-1] + av + "itAsi"
                else:
                    clean_prat = raw[:-1] if raw.endswith("p") else raw
                    final_form = apply_rutva_visarga(base_tas + clean_prat)
            return final_form, log

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
            if prat.startswith("anti"): final_form = stem[:-1] + prat
            elif prat[0] in self.yan_set: final_form = stem[:-1] + "A" + prat
            else: final_form = stem + prat
            final_form = apply_rutva_visarga(final_form)

        elif lakara in ["laN", "lfN"]:
            lan_replacements = {"tas": "tAm", "Tas": "tam", "Ta": "ta", "mip": "am"}
            if raw in lan_replacements: prat = lan_replacements[raw]
            elif raw == "Ji": prat = "an"
            elif raw in ["tip", "sip"]: prat = raw[:-2] if raw.endswith("p") else raw[:-1]
            elif raw in ["vas", "mas"]: prat = raw[:-1]

            if prat.startswith("a"): final_form = stem[:-1] + prat
            elif prat[0] in self.yan_set: final_form = stem[:-1] + "A" + prat
            else: final_form = stem + prat
            final_form = apply_rutva_visarga(final_form)

        elif lakara == "low":
            if raw == "tip": prat = "tu"; final_form = stem + prat
            elif raw == "tas": prat = "tAm"; final_form = stem + prat
            elif raw == "Ji": prat = "antu"; final_form = stem[:-1] + prat
            elif raw == "sip": final_form = stem
            elif raw == "Tas": prat = "tam"; final_form = stem + prat
            elif raw == "Ta": prat = "ta"; final_form = stem + prat
            elif purusha == "uttama":
                prat = "ni" if raw == "mip" else raw[:-1]
                final_form = stem[:-1] + "A" + prat

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
            final_form = apply_rutva_visarga(combined)

        return final_form, log

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
                form, _ = self.derive(dhatu, lakara, p, v, prayoga, sanadi)
                table[(p, v)] = form
        return table
