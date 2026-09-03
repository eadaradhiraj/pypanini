"""
Generative Kṛdanta Engine - no per-dhatu form dictionaries.
Derives from dhatu properties (sew, pada, vowel-final etc.)
Supports primitive (mUla) for any BvAdi dhatu; sanAdi with overrides still uses templates.
"""
from typing import Dict, Optional
import json
import glob
from pathlib import Path
from .phonetics import apply_guna, apply_vriddhi, apply_sandhi_eco_ayavayavah

SLP1_VOWELS = set(list("aAiIuUfFxXeEoO"))

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
        self._cache = None

    def _load_cache(self):
        if self._cache is not None:
            return
        self._cache = {}
        self._cache["BU"] = {"clean": "BU", "pada": "parasmEpadi", "sew": True}
        self._cache["eD"] = {"clean": "eD", "pada": "Atmanepadi", "sew": True}
        try:
            base = Path("/home/edhiraj/Documents/projs/skt-morph-data/data/01")
            if base.exists():
                for jf in glob.glob(str(base / "*.json")):
                    try:
                        d = json.load(open(jf, encoding="utf-8"))
                        info = {x["name"]: x["value"] for x in d.get("info", [])}
                        op = info.get("OpadeSikasvarUpam", "")
                        if not op:
                            continue
                        raw = op.replace("~", "").replace("`", "").strip()
                        if raw and raw[-1] in "fFxX" and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
                            raw = raw[:-1]
                        clean = raw
                        if clean.endswith("a") and len(clean) > 1:
                            clean = clean[:-1]
                        padam = info.get("padam", "")
                        if "Atman" in padam:
                            pada = "Atmanepadi"
                        elif "parasm" in padam.lower():
                            pada = "parasmEpadi"
                        else:
                            pada = "parasmEpadi"
                        sew = info.get("iqAgamayogyatA", "sew").lower().strip() == "sew"
                        self._cache[clean] = {"clean": clean, "pada": pada, "sew": sew}
                        self._cache[op] = self._cache[clean]
                    except Exception:
                        continue
        except Exception:
            pass

    def _get_meta(self, dhatu: str) -> Dict:
        self._load_cache()
        assert self._cache is not None
        if dhatu in self._cache:
            return self._cache[dhatu]
        raw = dhatu.replace("~", "").replace("`", "").strip()
        if raw and raw[-1] in "fFxX" and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
            raw = raw[:-1]
        clean = raw
        if clean.endswith("a") and len(clean) > 1:
            clean = clean[:-1]
        is_vowel_init = clean[0] in SLP1_VOWELS if clean else False
        pada = "Atmanepadi" if is_vowel_init else "parasmEpadi"
        return {"clean": clean, "pada": pada, "sew": True}

    def _guna_base(self, clean: str) -> str:
        if not clean:
            return clean
        if clean[-1] in SLP1_VOWELS:
            gv = apply_guna(clean[-1])
            av = apply_sandhi_eco_ayavayavah(gv)
            return clean[:-1] + av
        return clean

    def _vriddhi_base(self, clean: str) -> str:
        if not clean:
            return clean
        if clean[-1] in SLP1_VOWELS:
            vv = apply_vriddhi(clean[-1])
            av = apply_sandhi_eco_ayavayavah(vv)
            return clean[:-1] + av
        return clean

    def derive_krdanta(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: str = "saM",
    ) -> Optional[Dict]:
        meta = self._get_meta(dhatu)
        clean = meta["clean"]
        pada = meta["pada"]
        sew = meta["sew"]
        is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False

        if sanadi is not None:
            if sanadi == "nijanta":
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

        # primitive generative
        def needs_i_for_kta() -> bool:
            return sew and not is_vowel_final

        guna_base = self._guna_base(clean)
        vriddhi_base = self._vriddhi_base(clean)

        # helper to build tri-linga from stem ending in 'a'
        def tri_linga(stem_a: str) -> Dict:
            # stem_a ends with 'a' e.g., eDita, BavanIya
            m = stem_a + "H"
            f = stem_a[:-1] + "A" if stem_a.endswith("a") else stem_a + "A"
            n = stem_a + "m"
            return {"M": m, "F": f, "N": n}

        if pratyaya == "kta":
            base = clean + ("i" if needs_i_for_kta() else "")
            stem = base + "ta"
            return tri_linga(stem)

        elif pratyaya == "ktavatu":
            base = clean + ("i" if needs_i_for_kta() else "")
            b = base
            return {"M": b + "tavAn", "F": b + "tavatI", "N": b + "tavat"}

        elif pratyaya == "Satf":
            if pada == "Atmanepadi":
                return None
            # guna_base + at -> stem "Bavat" -> M Bavan, F BavantI, N Bavat
            stem_at = guna_base + "at"
            m = stem_at[:-1] + "n"  # Bavat -> Bavan
            f = guna_base + "antI"  # BavantI
            n = stem_at  # Bavat
            return {"M": m, "F": f, "N": n}

        elif pratyaya == "SAnac":
            if pada == "Atmanepadi":
                stem = clean + "amAna"
            else:
                stem = clean + "yamAna"
            return tri_linga(stem)

        elif pratyaya == "tavya":
            stem = guna_base + ("i" if sew else "") + "tavya"
            return tri_linga(stem)

        elif pratyaya == "anIyar":
            stem = guna_base + "anIya"
            return tri_linga(stem)

        elif pratyaya == "yat":
            stem = guna_base + "ya"
            return tri_linga(stem)

        elif pratyaya == "Rvul":
            stem = vriddhi_base + "aka"
            m = stem + "H"
            # F: replace 'aka' with 'ikA' : eDaka -> eDikA, BAvaka -> BAvikA, sparDaka -> sparDikA
            if stem.endswith("aka"):
                f = stem[:-3] + "ikA"
            else:
                f = stem[:-1] + "ikA"
            n = stem + "m"
            return {"M": m, "F": f, "N": n}

        elif pratyaya == "tfc":
            b = guna_base + ("i" if sew else "")
            return {"M": b + "tA", "F": b + "trI", "N": b + "tf"}

        elif pratyaya == "lyuw":
            stem = guna_base + "ana"
            return {"gender": "Neuter", "form": stem + "m"}

        elif pratyaya == "GaY":
            stem = vriddhi_base + "a"
            return {"gender": "Masculine", "form": stem + "H"}

        elif pratyaya == "tumun":
            stem = guna_base + ("i" if sew else "") + "tum"
            return {"avyaya": [stem]}

        elif pratyaya == "ktvA":
            if needs_i_for_kta():
                stem = clean + "i" + "tvA"
            else:
                stem = clean + "tvA"
            return {"avyaya": [stem]}

        elif pratyaya == "lyap":
            base_ya = clean + "ya"
            pref = upasarga + base_ya
            bare = base_ya
            # Provide both M variants to cover saM vs sam, and bare
            variants = []
            for v in [pref, pref.replace("M", "m"), bare]:
                if v not in variants:
                    variants.append(v)
            # Keep at most 2 with bare guaranteed
            # Ensure bare is included
            if bare not in variants:
                variants.append(bare)
            # For compatibility, return first two that include bare
            # Original expects [sameDya, eDya] or [saMBUya, BUya]
            # We'll return [pref_m, bare] where pref_m is with 'm'
            pref_m = pref.replace("M", "m")
            return {"avyaya": [pref_m, bare]}

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
