"""
Tiṅanta Derivation Engine for all 4 Sārvadhātuka Lakāras:
'lw' (Present), 'laN' (Past), 'low' (Imperative), and 'viDiliN' (Optative).
"""
from typing import Dict, List, Tuple
from .pratyahara import MaheshvaraSutrasSLP1
from .phonetics import apply_guna, apply_sandhi_eco_ayavayavah, apply_rutva_visarga


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

        # 7.3.101 ato dīrgho yañi (Pratyāhāra 'yañ' = 'yY')
        self.yan_set = self.ms.get_set("yY")

    def derive(self, dhatu: str, lakara: str, purusha: str, vacana: str) -> Tuple[str, List[str]]:
        log = []
        raw = self.pratyayas[(purusha, vacana)]
        prat = raw

        # --- 1. Sārvadhātuka Base Stem (Bhvādi - Class 1) ---
        guna_v = apply_guna(dhatu[-1])
        av = apply_sandhi_eco_ayavayavah(guna_v)
        stem = dhatu[:-1] + av + "a"  # 'Bava'

        # --- 2. 'laN' Prefix (6.4.71 aw-Agama) ---
        if lakara == "laN":
            stem = "a" + stem

        # --- 3. Lakāra-Specific Rules ---
        if lakara == "lw":
            if prat.startswith("J"): prat = "ant" + prat[1:]
            if prat.endswith("p"): prat = prat[:-1]

            if prat.startswith("anti"):
                final_form = stem[:-1] + prat
            elif prat[0] in self.yan_set:
                final_form = stem[:-1] + "A" + prat
            else:
                final_form = stem + prat
            final_form = apply_rutva_visarga(final_form)

        elif lakara == "laN":
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
                final_form = stem  # 6.4.105 ato heḥ
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
            # 3.4.108 Jher jus
            if raw == "Ji":
                prat = "us"
            # 3.4.100 itas ca
            elif raw == "tip":
                prat = "t"
            elif raw == "sip":
                prat = "s"
            # 3.4.101 tAntantAmaH
            elif raw == "tas":
                prat = "tAm"
            elif raw == "Tas":
                prat = "tam"
            elif raw == "Ta":
                prat = "ta"
            elif raw == "mip":
                prat = "am"
            # 3.4.99 nityaM RitaH
            elif raw in ["vas", "mas"]:
                prat = raw[:-1]

            # 3.4.106 ato yeyaH ('iy' after 'a') & 6.1.66 lopo vyorvali (drop 'y' before consonants)
            # 6.1.87 AdguRaH: 'Bava' + 'i'/'iy' -> 'Bave' / 'Bavey'
            if prat.startswith("a") or prat.startswith("u"):
                combined = stem[:-1] + "ey" + prat  # e.g., 'Baveyam', 'Baveyus'
            else:
                combined = stem[:-1] + "e" + prat   # e.g., 'Bavet', 'BavetAm', 'Baveva'

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
