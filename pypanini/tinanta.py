"""
Tiṅanta Derivation Engine supporting 7 Lakāras in SLP1:
'lw' (Present), 'lfw' (Simple Future), 'luw' (First Future),
'laN' (Past), 'low' (Imperative), 'viDiliN' (Optative), and 'lfN' (Conditional).
"""
from typing import Dict, List, Tuple
from .pratyahara import MaheshvaraSutrasSLP1
from .phonetics import (
    apply_guna,
    apply_sandhi_eco_ayavayavah,
    apply_satva,
    apply_rutva_visarga,
)


class TinantaDerivationEngine:
    def __init__(self):
        self.ms = MaheshvaraSutrasSLP1()

        # 9 Parasmaipada tiṅ affixes (3.4.78)
        self.pratyayas = {
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

    def derive(self, dhatu: str, lakara: str, purusha: str, vacana: str) -> Tuple[str, List[str]]:
        log = []
        raw = self.pratyayas[(purusha, vacana)]
        prat = raw

        # --- Base Root Guṇa & Sandhi ---
        guna_v = apply_guna(dhatu[-1])
        av = apply_sandhi_eco_ayavayavah(guna_v)

        # ---------------------------------------------------------------------
        # 1. 'luw' (First Future: tAsi affix - 3.1.33)
        # ---------------------------------------------------------------------
        if lakara == "luw":
            # 2.4.85 lutaH prathamasya qArawrasaH
            if purusha == "prathama":
                if vacana == "eka":
                    # 6.4.143 weH: qA deletes 'As' from 'BavitAs' -> 'BavitA'
                    final_form = dhatu[:-1] + av + "itA"
                elif vacana == "dvi":
                    # 7.4.51 tAso ryoH: drop 's' before 'r' -> 'BavitArO'
                    final_form = dhatu[:-1] + av + "itArO"
                elif vacana == "bahu":
                    # 7.4.51 tAso ryoH: drop 's' before 'r' -> 'BavitAraH'
                    final_form = dhatu[:-1] + av + "itAraH"
            else:
                base_tas = dhatu[:-1] + av + "itAs"
                if raw == "sip":
                    # 7.4.50 tAsastyorlopaH: drop 's' of 'tAs' before 's'
                    final_form = dhatu[:-1] + av + "itAsi"
                else:
                    clean_prat = raw[:-1] if raw.endswith("p") else raw
                    final_form = apply_rutva_visarga(base_tas + clean_prat)

            log.append(f"Result: {dhatu} + {lakara} + {raw} -> {final_form}")
            return final_form, log

        # ---------------------------------------------------------------------
        # 2. Stems for other 6 Lakāras
        # ---------------------------------------------------------------------
        if lakara in ["lfw", "lfN"]:
            base_with_it = dhatu[:-1] + av + "i"
            satva_s = apply_satva(base_with_it[-1], "s")
            stem = base_with_it + satva_s + "ya"
            if lakara == "lfN":
                stem = "a" + stem
        else:
            stem = dhatu[:-1] + av + "a"
            if lakara == "laN":
                stem = "a" + stem

        # ---------------------------------------------------------------------
        # 3. Endings application
        # ---------------------------------------------------------------------
        if lakara in ["lw", "lfw"]:
            if prat.startswith("J"): prat = "ant" + prat[1:]
            if prat.endswith("p"): prat = prat[:-1]

            if prat.startswith("anti"):
                final_form = stem[:-1] + prat
            elif prat[0] in self.yan_set:
                final_form = stem[:-1] + "A" + prat
            else:
                final_form = stem + prat
            final_form = apply_rutva_visarga(final_form)

        elif lakara in ["laN", "lfN"]:
            lan_replacements = {"tas": "tAm", "Tas": "tam", "Ta": "ta", "mip": "am"}
            if raw in lan_replacements:
                prat = lan_replacements[raw]
            elif raw == "Ji":
                prat = "an"
            elif raw in ["tip", "sip"]:
                prat = raw[:-2] if raw.endswith("p") else raw[:-1]
            elif raw in ["vas", "mas"]:
                prat = raw[:-1]

            if prat.startswith("a"):
                final_form = stem[:-1] + prat
            elif prat[0] in self.yan_set:
                final_form = stem[:-1] + "A" + prat
            else:
                final_form = stem + prat
            final_form = apply_rutva_visarga(final_form)

        elif lakara == "low":
            if raw == "tip":
                prat = "tu"
                final_form = stem + prat
            elif raw == "tas":
                prat = "tAm"
                final_form = stem + prat
            elif raw == "Ji":
                prat = "antu"
                final_form = stem[:-1] + prat
            elif raw == "sip":
                final_form = stem
            elif raw == "Tas":
                prat = "tam"
                final_form = stem + prat
            elif raw == "Ta":
                prat = "ta"
                final_form = stem + prat
            elif purusha == "uttama":
                prat = "ni" if raw == "mip" else raw[:-1]
                final_form = stem[:-1] + "A" + prat

        elif lakara == "viDiliN":
            if raw == "Ji":
                prat = "us"
            elif raw == "tip":
                prat = "t"
            elif raw == "sip":
                prat = "s"
            elif raw == "tas":
                prat = "tAm"
            elif raw == "Tas":
                prat = "tam"
            elif raw == "Ta":
                prat = "ta"
            elif raw == "mip":
                prat = "am"
            elif raw in ["vas", "mas"]:
                prat = raw[:-1]

            if prat.startswith("a") or prat.startswith("u"):
                combined = stem[:-1] + "ey" + prat
            else:
                combined = stem[:-1] + "e" + prat

            final_form = apply_rutva_visarga(combined)

        log.append(f"Result: {dhatu} + {lakara} + {raw} -> {final_form}")
        return final_form, log

    def derive_all(self, dhatu: str = "BU", lakara: str = "lw") -> Dict[Tuple[str, str], str]:
        table = {}
        for p in ["prathama", "madhyama", "uttama"]:
            for v in ["eka", "dvi", "bahu"]:
                form, _ = self.derive(dhatu, lakara, p, v)
                table[(p, v)] = form
        return table
