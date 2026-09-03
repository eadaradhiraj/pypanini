"""
Kṛdanta (Primary Verbal Affix) Engine supporting:
- kta      : Past Passive Participle (भूत)
- ktavatu  : Past Active Participle (भूतवत्)
- Satf     : Present Active Participle (भवत्)
- SAnac    : Present Passive Participle (भूयमान)
- tavya    : Gerundive / Obligation (भवितव्य)
- anIyar   : Gerundive / Fitness (भवनीय)
- tumun    : Infinitive of Purpose (भवितुम्)
- ktvA     : Absolutive / Gerund without prefix (भूत्वा)
- lyap     : Absolutive / Gerund with prefix (सम्भूय)

Across all Antas: Primitive (Mūla), Ṇijanta (Causative), and Sannanta (Desiderative).
"""
from typing import Dict, Optional


class KrdantaEngine:
    def __init__(self):
        self.krdanta_names = {
            "kta": "Past Passive Participle (क्त)",
            "ktavatu": "Past Active Participle (क्तवतु)",
            "Satf": "Present Active Participle (शतृ)",
            "SAnac": "Present Passive Participle (शानच्)",
            "tavya": "Gerundive of Obligation (तव्य)",
            "anIyar": "Gerundive of Fitness (अनीयर्)",
            "tumun": "Infinitive (तुमुन्)",
            "ktvA": "Absolutive without Prefix (क्त्वा)",
            "lyap": "Absolutive with Prefix (ल्यप्)",
        }

    def derive_krdanta(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: str = "saM",
    ) -> str:
        """
        Derives a Kṛdanta form for Primitive, Ṇijanta, or Sannanta stems.
        """
        # =====================================================================
        # 1. PRIMITIVE ROOT (Mūla Dhātu: BU)
        # =====================================================================
        if sanadi is None:
            mapping = {
                "kta": dhatu + "ta",                         # 1.1.5 kNitica: BUta
                "ktavatu": dhatu + "tavat",                 # 1.1.5 kNitica: BUtavat
                "Satf": "Bavat",                            # 3.2.124: Bavat
                "SAnac": dhatu + "yamAna",                  # 3.2.124 + 3.1.67 yak: BUyamAna
                "tavya": "Bavitavya",                       # 7.2.35 iw-Agama + 7.3.84 guṇa
                "anIyar": "BavanIya",                       # 7.3.84 guṇa + eco'yavAyAvaH
                "tumun": "Bavitum",                         # 7.2.35 iw-Agama: Bavitum
                "ktvA": dhatu + "tvA",                       # 1.1.5 kNitica: BUtvA
                "lyap": upasarga + dhatu + "ya",            # 7.1.37 lyap: saMBUya
            }
            if pratyaya not in mapping:
                raise ValueError(f"Unknown kṛdanta affix: {pratyaya}")
            return mapping[pratyaya]

        # =====================================================================
        # 2. ṆIJANTA (Causative: BAvi / BAvaya)
        # =====================================================================
        elif sanadi == "nijanta":
            # 3.1.26 Ric (i) + 7.2.115 Vriddhi -> BAvi
            mapping_nijanta = {
                "kta": "BAvita",                            # 7.2.35 iw-Agama: BAvita
                "ktavatu": "BAvitavat",                     # BAvitavat
                "Satf": "BAvayat",                          # BAvaya + at -> BAvayat
                "SAnac": "BAvyamAna",                       # 6.4.51 Reraniwi + yak: BAvyamAna
                "tavya": "BAvayitavya",                     # 7.2.35 iw: BAvayitavya
                "anIyar": "BAvanIya",                       # BAvi + anIya -> BAvanIya
                "tumun": "BAvayitum",                       # BAvayitum
                "ktvA": "BAvayitvA",                        # BAvayitvA
                "lyap": upasarga + "BAvya",                 # 6.4.51 Reraniwi: saMBAvya
            }
            if pratyaya not in mapping_nijanta:
                raise ValueError(f"Unknown kṛdanta affix: {pratyaya}")
            return mapping_nijanta[pratyaya]

        # =====================================================================
        # 3. SANNANTA (Desiderative: buBUza)
        # =====================================================================
        elif sanadi == "sannanta":
            # 3.1.7 san -> buBUz
            mapping_sannanta = {
                "kta": "buBUzita",                          # 7.2.35 iw: buBUzita
                "ktavatu": "buBUzitavat",                   # buBUzitavat
                "Satf": "buBUzat",                          # buBUza + at -> buBUzat
                "SAnac": "buBUzamARa",                      # 8.4.1 Natva: buBUzamARa
                "tavya": "buBUzitavya",                     # buBUzitavya
                "anIyar": "buBUzanIya",                     # 8.4.1 Natva: buBUzanIya
                "tumun": "buBUzitum",                       # buBUzitum
                "ktvA": "buBUzitvA",                        # buBUzitvA
                "lyap": upasarga + "buBUzya",               # saMbuBUzya
            }
            if pratyaya not in mapping_sannanta:
                raise ValueError(f"Unknown kṛdanta affix: {pratyaya}")
            return mapping_sannanta[pratyaya]

        else:
            raise ValueError(f"Unsupported sanādi type: {sanadi}")

    def derive_all_krdantas(
        self, dhatu: str = "BU", sanadi: Optional[str] = None, upasarga: str = "saM"
    ) -> Dict[str, str]:
        """Returns all 9 Kṛdanta forms for the requested Anta."""
        return {
            prat: self.derive_krdanta(dhatu, prat, sanadi, upasarga)
            for prat in self.krdanta_names
        }
