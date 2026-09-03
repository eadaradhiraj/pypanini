"""
Tiṅanta Derivation Engine supporting 'lw', 'laN', and 'low' in SLP1.
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

        # --- 1. Sārvadhātuka Stem Formation (Bhvādi - Class 1) ---
        guna_v = apply_guna(dhatu[-1])
        av = apply_sandhi_eco_ayavayavah(guna_v)
        stem = dhatu[:-1] + av + "a"  # 'Bava'

        # --- 2. 'laN' Prefix (aw-Agama: 6.4.71) ---
        if lakara == "laN":
            stem = "a" + stem
            log.append(f"6.4.71 (aw-Agama)        : Prefix 'a' -> {stem}")

        # --- 3. Derivations by Lakāra ---
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
            # 3.4.101 tasTasTamipAM tAntantAmaH
            lan_replacements = {"tas": "tAm", "Tas": "tam", "Ta": "ta", "mip": "am"}
            if raw in lan_replacements:
                prat = lan_replacements[raw]
            elif raw == "Ji":
                prat = "an"
            elif raw in ["tip", "sip"]:
                prat = raw[:-2] if raw.endswith("p") else raw[:-1]  # 3.4.100 itas ca
            elif raw in ["vas", "mas"]:
                prat = raw[:-1]  # 3.4.99 nityaM RitaH

            if prat.startswith("a"):
                final_form = stem[:-1] + prat
            elif prat[0] in self.yan_set:
                final_form = stem[:-1] + "A" + prat
            else:
                final_form = stem + prat
            final_form = apply_rutva_visarga(final_form)

        elif lakara == "low":
            # 3.4.85 lowo laNvat (Loṭ behaves like Laṅ for duals/plurals)
            if raw == "tip":
                # 3.4.86 eruH: 'i' -> 'u'
                prat = "tu"
                final_form = stem + prat
            elif raw == "tas":
                # 3.4.85 laṅvat + 3.4.101
                prat = "tAm"
                final_form = stem + prat
            elif raw == "Ji":
                # 7.1.7 Jho'ntaH + 3.4.86 eruH ('anti' -> 'antu')
                prat = "antu"
                final_form = stem[:-1] + prat  # 6.1.97 ato guṇe
            elif raw == "sip":
                # 3.4.87 ser hyapiccāvaḥ (si -> hi) & 6.4.105 ato heḥ (drop 'hi' after 'a')
                prat = ""
                final_form = stem
            elif raw == "Tas":
                prat = "tam"
                final_form = stem + prat
            elif raw == "Ta":
                prat = "ta"
                final_form = stem + prat
            elif purusha == "uttama":
                # 3.4.92 Aquttamasya pic ca (Augment 'A' for 1st person)
                if raw == "mip":
                    # 3.4.89 mer niH: mi -> ni
                    prat = "ni"
                elif raw in ["vas", "mas"]:
                    # 3.4.85 laṅvat (drops 's')
                    prat = raw[:-1]
                final_form = stem[:-1] + "A" + prat

        log.append(f"Result: {dhatu} + {lakara} + {raw} -> {final_form}")
        return final_form, log

    def derive_all(self, dhatu: str = "BU", lakara: str = "lw") -> Dict[Tuple[str, str], str]:
        table = {}
        for p in ["prathama", "madhyama", "uttama"]:
            for v in ["eka", "dvi", "bahu"]:
                form, _ = self.derive(dhatu, lakara, p, v)
                table[(p, v)] = form
        return table
