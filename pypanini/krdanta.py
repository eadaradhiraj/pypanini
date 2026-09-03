"""
Complete Kṛdanta Engine supporting 'BU' (01.0001) and 'eD' (01.0002).
"""
from typing import Dict, Optional


class KrdantaEngine:
    def __init__(self):
        self.krdanta_metadata = {
            "kta": ("Past Passive Participle (क्त)", "participle"),
            "ktavatu": ("Past Active Participle (क्तवतु)", "participle"),
            "Satf": ("Present Active Participle (शतृ)", "participle"),
            "SAnac": ("Present Passive Participle (शानच्)", "participle"),
            "tavya": ("Gerundive of Obligation (तव्य)", "participle"),
            "anIyar": ("Gerundive of Fitness (अनीयर्)", "participle"),
            "yat": ("Gerundive of Potential (यत्/ण्यत्)", "participle"),
            "Rvul": ("Agent Noun in -aka / -u (ण्वुल् / उः)", "agent_noun"),
            "tfc": ("Agent Noun in -tṛ (तृच्)", "participle"),
            "lyuw": ("Verbal Noun in -ana (ल्युट्)", "neuter_noun"),
            "GaY": ("Action Noun with Vṛddhi / -ā (घञ् / अ+टाप्)", "action_noun"),
            "tumun": ("Infinitive of Purpose (तुमुन्)", "avyaya"),
            "ktvA": ("Absolutive without Prefix (क्त्वा)", "avyaya"),
            "lyap": ("Absolutive with Prefix (ल्यप्)", "avyaya"),
        }

    def derive_krdanta(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: str = "saM",
    ) -> Optional[Dict]:
        # =====================================================================
        # ROOT 'eD' (01.0002: sew, AtmanepadI)
        # =====================================================================
        if dhatu == "eD":
            forms_edh = {
                "kta": {"M": "eDitaH", "F": "eDitA", "N": "eDitam"},
                "ktavatu": {"M": "eDitavAn", "F": "eDitavatI", "N": "eDitavat"},
                "SAnac": {"M": "eDamAnaH", "F": "eDamAnA", "N": "eDamAnam"},
                "tavya": {"M": "eDitavyaH", "F": "eDitavyA", "N": "eDitavyam"},
                "anIyar": {"M": "eDanIyaH", "F": "eDanIyA", "N": "eDanIyam"},
                "yat": {"M": "eDyaH", "F": "eDyA", "N": "eDyam"},
                "Rvul": {"M": "eDakaH", "F": "eDikA", "N": "eDakam"},
                "tfc": {"M": "eDitA", "F": "eDitrI", "N": "eDitf"},
                "lyuw": {"gender": "Neuter", "form": "eDanam"},
                "GaY": {"gender": "Masculine", "form": "eDaH"},
                "tumun": {"avyaya": ["eDitum"]},
                "ktvA": {"avyaya": ["eDitvA"]},
                # Both classical prefixed 'sameDya' and bare base 'eDya'
                "lyap": {"avyaya": ["sameDya", "eDya"]},
            }
            return forms_edh.get(pratyaya)

        # =====================================================================
        # ROOT 'BU' (01.0001)
        # =====================================================================
        if sanadi is None:
            forms = {
                "kta": {"M": "BUtaH", "F": "BUtA", "N": "BUtam"},
                "ktavatu": {"M": "BUtavAn", "F": "BUtavatI", "N": "BUtavat"},
                "Satf": {"M": "Bavan", "F": "BavantI", "N": "Bavat"},
                "SAnac": {"M": "BUyamAnaH", "F": "BUyamAnA", "N": "BUyamAnam"},
                "tavya": {"M": "BavitavyaH", "F": "BavitavyA", "N": "Bavitavyam"},
                "anIyar": {"M": "BavanIyaH", "F": "BavanIyA", "N": "BavanIyam"},
                "yat": {"M": "BavyaH", "F": "BavyA", "N": "Bavyam"},
                "Rvul": {"M": "BAvakaH", "F": "BAvikA", "N": "BAvakam"},
                "tfc": {"M": "BavitA", "F": "BavitrI", "N": "Bavitf"},
                "lyuw": {"gender": "Neuter", "form": "Bavanam"},
                "GaY": {"gender": "Masculine", "form": "BAvaH"},
                "tumun": {"avyaya": ["Bavitum"]},
                "ktvA": {"avyaya": ["BUtvA"]},
                "lyap": {"avyaya": [upasarga + dhatu + "ya", "BUya"]},
            }
            return forms.get(pratyaya)

        elif sanadi == "nijanta":
            forms = {
                "kta": {"M": "BAvitaH", "F": "BAvitA", "N": "BAvitam"},
                "ktavatu": {"M": "BAvitavAn", "F": "BAvitavatI", "N": "BAvitavat"},
                "Satf": {"M": "BAvayan", "F": "BAvayantI", "N": "BAvayat"},
                "SAnac": {"M": "BAvyamAnaH", "F": "BAvyamAnA", "N": "BAvyamAnam"},
                "tavya": {"M": "BAvayitavyaH", "F": "BAvayitavyA", "N": "BAvayitavyam"},
                "anIyar": {"M": "BAvanIyaH", "F": "BAvanIyA", "N": "BAvanIyam"},
                "yat": {"M": "BAvyaH", "F": "BAvyA", "N": "BAvyam"},
                "Rvul": {"M": "BAvakaH", "F": "BAvikA", "N": "BAvakam"},
                "tfc": {"M": "BAvayitA", "F": "BAvayitrI", "N": "BAvayitf"},
                "lyuw": {"gender": "Neuter", "form": "BAvanam"},
                "GaY": {"gender": "Masculine", "form": "BAvaH"},
                "tumun": {"avyaya": ["BAvayitum"]},
                "ktvA": {"avyaya": ["BAvayitvA"]},
                "lyap": {"avyaya": [upasarga + "BAvya", "BAvya"]},
            }
            return forms.get(pratyaya)

        elif sanadi == "sannanta":
            forms = {
                "kta": {"M": "buBUzitaH", "F": "buBUzitA", "N": "buBUzitam"},
                "ktavatu": {"M": "buBUzitavAn", "F": "buBUzitavatI", "N": "buBUzitavat"},
                "Satf": {"M": "buBUzan", "F": "buBUzantI", "N": "buBUzat"},
                "SAnac": {"M": "buBUzamARaH", "F": "buBUzamARA", "N": "buBUzamARam"},
                "tavya": {"M": "buBUzitavyaH", "F": "buBUzitavyA", "N": "buBUzitavyam"},
                "anIyar": {"M": "buBUzaRIyaH", "F": "buBUzaRIyA", "N": "buBUzaRIyam"},
                "yat": {"M": "buBUzyaH", "F": "buBUzyA", "N": "buBUzyam"},
                "Rvul": {"M": "buBUzuH", "F": "buBUzuH", "N": "buBUzu"},
                "tfc": {"M": "buBUzitA", "F": "buBUzitrI", "N": "buBUzitf"},
                "lyuw": {"gender": "Neuter", "form": "buBUzaRam"},
                "GaY": {"gender": "Feminine", "form": "buBUzA"},
                "tumun": {"avyaya": ["buBUzitum"]},
                "ktvA": {"avyaya": ["buBUzitvA"]},
                "lyap": {"avyaya": [upasarga + "buBUzya", "buBUzya"]},
            }
            return forms.get(pratyaya)

        elif sanadi == "yananta":
            forms = {
                "kta": {"M": "boBUyitaH", "F": "boBUyitA", "N": "boBUyitam"},
                "ktavatu": {"M": "boBUyitavAn", "F": "boBUyitavatI", "N": "boBUyitavat"},
                "SAnac": {"M": "boBUyamAnaH", "F": "boBUyamAnA", "N": "boBUyamAnam"},
                "tavya": {"M": "boBUyitavyaH", "F": "boBUyitavyA", "N": "boBUyitavyam"},
                "anIyar": {"M": "boBUyanIyaH", "F": "boBUyanIyA", "N": "boBUyanIyam"},
                "yat": {"M": "boBUyyaH", "F": "boBUyyA", "N": "boBUyyam"},
                "Rvul": {"M": "boBUyakaH", "F": "boBUyikA", "N": "boBUyakam"},
                "tfc": {"M": "boBUyitA", "F": "boBUyitrI", "N": "boBUyitf"},
                "lyuw": {"gender": "Neuter", "form": "boBUyanam"},
                "GaY": {"gender": "Masculine", "form": "boBUyaH"},
                "tumun": {"avyaya": ["boBUyitum"]},
                "ktvA": {"avyaya": ["boBUyitvA"]},
                "lyap": {"avyaya": [upasarga + "boBUya", "boBUya"]},
            }
            return forms.get(pratyaya)

        return None

    def derive_all_krdantas(
        self, dhatu: str = "BU", sanadi: Optional[str] = None, upasarga: str = "saM"
    ) -> Dict[str, Dict]:
        result = {}
        for prat in self.krdanta_metadata:
            res = self.derive_krdanta(dhatu, prat, sanadi, upasarga)
            if res is not None:
                result[prat] = res
        return result
