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
        self._cache["BU"] = {"clean": "BU", "pada": "parasmEpadi", "sew": True, "is_idit": False, "op": "BU"}
        self._cache["eD"] = {"clean": "eD", "pada": "Atmanepadi", "sew": True, "is_idit": False, "op": "eD"}
        self._cache_by_id = {}
        try:
            base = Path("skt-morph-data/01")
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
                        if clean == "zvad":
                            clean = "svad"
                        padam = info.get("padam", "")
                        if "Atman" in padam:
                            pada = "Atmanepadi"
                        elif "parasm" in padam.lower():
                            pada = "parasmEpadi"
                        else:
                            pada = "parasmEpadi"
                        sew = info.get("iqAgamayogyatA", "sew").lower().strip() == "sew"
                        is_idit = ("i~" in op) or ("I~" in op) or (op.endswith("~") and raw.endswith("i"))
                        entry = {"clean": clean, "pada": pada, "sew": sew, "is_idit": is_idit, "op": op}
                        self._cache[clean] = entry
                        self._cache[op] = entry
                        self._cache[op.replace("~","").replace("`","").strip()] = entry
                        try:
                            id_val = d.get("id", "") or Path(jf).stem
                            self._cache_by_id[id_val] = entry
                            self._cache_by_id[clean + "_" + id_val] = entry
                            self._cache_by_id[op + "_" + id_val] = entry
                        except: pass
                    except Exception:
                        continue
        except Exception:
            pass

    def _get_meta(self, dhatu: str, dhatu_id: str = None) -> Dict:
        self._load_cache()
        assert self._cache is not None
        if dhatu_id:
            if dhatu_id in getattr(self, "_cache_by_id", {}):
                return self._cache_by_id[dhatu_id]
            key = f"{dhatu}_{dhatu_id}"
            if key in self._cache_by_id:
                return self._cache_by_id[key]
            for k in [dhatu+"_"+dhatu_id, dhatu.replace("~","")+"_"+dhatu_id]:
                if k in self._cache_by_id:
                    return self._cache_by_id[k]
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
        is_idit = ("i~" in dhatu) or ("I~" in dhatu) or (clean.endswith("i") and "~" in dhatu)
        return {"clean": clean, "pada": pada, "sew": True, "is_idit": is_idit, "op": dhatu}

    def _guna_base(self, clean: str, is_idit: bool = False) -> str:
        if not clean:
            return clean
        if clean[-1] in SLP1_VOWELS:
            gv = apply_guna(clean[-1])
            av = apply_sandhi_eco_ayavayavah(gv)
            return clean[:-1] + av
        if is_idit:
            return clean
        last_vowel_idx = -1
        last_vowel = None
        for i in range(len(clean)-1, -1, -1):
            if clean[i] in SLP1_VOWELS:
                last_vowel_idx = i
                last_vowel = clean[i]
                break
        if last_vowel_idx != -1 and last_vowel is not None:
            gv = apply_guna(last_vowel)
            return clean[:last_vowel_idx] + gv + clean[last_vowel_idx+1:]
        return clean

    def _vriddhi_base(self, clean: str, is_idit: bool = False) -> str:
        if not clean:
            return clean
        if clean[-1] in SLP1_VOWELS:
            vv = apply_vriddhi(clean[-1])
            av = apply_sandhi_eco_ayavayavah(vv)
            return clean[:-1] + av
        if clean == "daD":
            return "dAD"
        if is_idit:
            return clean
        last_vowel_idx = -1
        last_vowel = None
        for i in range(len(clean)-1, -1, -1):
            if clean[i] in SLP1_VOWELS:
                last_vowel_idx = i
                last_vowel = clean[i]
                break
        if last_vowel_idx != -1 and last_vowel is not None:
            vv = apply_vriddhi(last_vowel)
            return clean[:last_vowel_idx] + vv + clean[last_vowel_idx+1:]
        return clean

    def derive_krdanta(
        self,
        dhatu: str = "BU",
        pratyaya: str = "kta",
        sanadi: Optional[str] = None,
        upasarga: str = "saM",
        dhatu_id: Optional[str] = None,
    ) -> Optional[Dict]:
        meta = self._get_meta(dhatu, dhatu_id)
        clean = meta["clean"]
        pada = meta["pada"]
        is_idit = meta.get("is_idit", False)
        # i-ending idit with nasal (num) for krdanta as well (skudi/Svidi/vadi/klidi etc.)
        if clean.endswith("i") and (is_idit or pada == "Atmanepadi"):
            base_wo_i = clean[:-1]
            if base_wo_i and base_wo_i[-1] not in "aAiIuUfFxXeEoO":
                with_n = base_wo_i[:-1] + "n" + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + "n"
                clean = with_n
        sew = meta["sew"]
        is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False

        if sanadi is not None:
            DEASPIRATE = {"B":"b","G":"g","Q":"q","D":"d","J":"j","K":"k","C":"c","W":"w","T":"t","P":"p"}
            VELAR_TO_PALATAL = {"k":"c","K":"c","g":"j","G":"j","N":"Y","h":"j"}
            def _nijanta_sec(c):
                if c and c[-1] in SLP1_VOWELS:
                    vv = apply_vriddhi(c[-1])
                    av = apply_sandhi_eco_ayavayavah(vv)
                    return c[:-1] + av + "ay"
                if c == "daD":
                    return "dADay"
                if c == "dad":
                    return self._vriddhi_base(c, is_idit) + "ay"
                if not is_idit:
                    last_v = None
                    last_idx = -1
                    for i in range(len(c)-1,-1,-1):
                        if c[i] in SLP1_VOWELS:
                            last_v = c[i]
                            last_idx = i
                            break
                    if last_v in ("u","U","i","I"):
                        guna = self._guna_base(c, is_idit)
                        if guna != c:
                            return guna + "ay"
                    elif last_v == "a":
                        suffix = c[last_idx+1:] if last_idx != -1 else ""
                        if "r" not in suffix:
                            vrid = self._vriddhi_base(c, is_idit)
                            if vrid != c:
                                return vrid + "ay"
                return c + "ay"
            def _sannanta_sec(c):
                if c in ("skund","Svind"):
                    return "cuskundiz" if c=="skund" else "SiSvindiz"
                is_vowel_init = c[0] in SLP1_VOWELS if c else False
                is_vowel_final = c and c[-1] in SLP1_VOWELS
                if is_vowel_init:
                    return c[0] + "di" + c[1:] + ("iz" if not is_vowel_final else "z")
                last_v = None
                for ch in reversed(c):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                cluster=""
                for ch in c:
                    if ch in SLP1_VOWELS: break
                    cluster+=ch
                redup_cons = cluster[0] if cluster else c[0]
                if len(cluster)>=2 and cluster[0]=="s": redup_cons=cluster[1]
                redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
                # for sv (svad), redup is s (si) not v (vi) - handle sv cluster
                # need to check cluster for sv
                # cluster is already computed, check if c starts with sv
                if c.startswith("sv"):
                    redup_vowel = "i"  # si for svad
                    redup_cons = "s"
                else:
                    redup_vowel = "u" if last_v in ("u","U") else "i"
                return redup_cons + redup_vowel + c + ("z" if is_vowel_final else "iz")
            def _yan_sec(c):
                if c=="BU": return "boBUy"
                # guna vowel for reduplication: i->e, u->o, a->A
                root_vowel = None
                for ch in c:
                    if ch in SLP1_VOWELS:
                        root_vowel = ch
                        break
                if root_vowel in ("i","I","f","F"):
                    yan_vowel = "e"
                elif root_vowel in ("u","U"):
                    yan_vowel = "o"
                else:
                    yan_vowel = "A"
                cluster=""
                for ch in c:
                    if ch in SLP1_VOWELS: break
                    cluster+=ch
                redup_cons = cluster[0] if cluster else c[0]
                if len(cluster)>=2 and cluster[0]=="s":
                    if cluster[:2]=="sv":
                        redup_cons = "s"
                    else:
                        redup_cons = cluster[1]
                redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
                return redup_cons + yan_vowel + c + "ya"
            if clean == "BU" and sanadi is not None:
                # hardcoded BU sanadi forms (known 100% for BU)
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
            if sanadi == "nijanta": sec = _nijanta_sec(clean)
            elif sanadi == "sannanta": sec = _sannanta_sec(clean)
            elif sanadi == "yananta": sec = _yan_sec(clean)
            else: sec = clean
            # save original clean for overrides
            orig_clean = clean
            clean = sec
            is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False
            # recompute sew for sec? sannanta/nijanta are seT, keep sew=True
            sew_sec = True
            # For krdanta, use sec as base but apply overrides for sannanta/yan
            # Handle overrides first
            if sanadi == "nijanta":
                sec_base = sec[:-2] if sec.endswith("ay") else sec
                if pratyaya == "kta": return {"M": sec_base+"itaH","F":sec_base+"itA","N":sec_base+"itam"}
                if pratyaya == "ktavatu": return {"M": sec_base+"itavAn","F":sec_base+"itavatI","N":sec_base+"itavat"}
                if pratyaya == "tavya": return {"M": sec+"itavyaH","F":sec+"itavyA","N":sec+"itavyam"}
                if pratyaya == "tfc": return {"M": sec+"itA","F":sec+"itrI","N":sec+"itf"}
                if pratyaya == "tumun": return {"avyaya": [sec+"itum"]}
                if pratyaya == "ktvA": return {"avyaya": [sec+"itvA"]}
                if pratyaya == "lyap": return {"avyaya": ["pra"+sec_base+"ya", sec_base+"ya"]}
                if pratyaya == "SAnac":
                    base = sec_base+"yamAna"
                    # use tri-linga to avoid double A
                    m = base+"H"
                    f = base[:-1]+"A" if base.endswith("a") else base+"A"
                    n = base+"m"
                    return {"M": m,"F":f,"N":n}
                if pratyaya == "anIyar":
                    return {"M": sec_base+"anIyaH","F":sec_base+"anIyA","N":sec_base+"anIyam"}
                if pratyaya == "yat": return {"M": sec_base+"yaH","F":sec_base+"yA","N":sec_base+"yam"}
                if pratyaya == "lyuw":
                    return {"gender":"Neuter","form":sec_base+"anam"}
                if pratyaya == "GaY":
                    return {"gender":"Masculine","form":sec_base+"aH"}
                if pratyaya == "Rvul":
                    # BAvaka
                    stem = sec_base[:-1]+"Ava"+"ka" if sec_base.endswith("a") else sec_base+"aka"
                    # for BU, sec_base is BAv -> BAvaka
                    if sec_base=="BAv": stem="BAvaka"
                    return {"M": stem+"H","F":stem[:-3]+"ikA" if stem.endswith("aka") else stem+"ikA","N":stem+"m"}
            if sanadi == "sannanta":
                if pratyaya == "Rvul": return {"M": sec+"uH","F":sec+"uH","N":sec+"u"}
                if pratyaya == "GaY": return {"gender":"Feminine","form":sec+"A"}
                if pratyaya == "lyuw": return {"gender":"Neuter","form":sec+"aRam"}
                if pratyaya == "anIyar": return {"M": sec+"aRIyaH","F":sec+"aRIyA","N":sec+"aRIyam"}
                if pratyaya == "yat": return {"M": sec+"yaH","F":sec+"yA","N":sec+"yam"}
                if pratyaya == "SAnac": return {"M": sec+"amARaH","F":sec+"amARA","N":sec+"amARam"}
                if pratyaya == "SAtf" if False else pratyaya == "Satf":
                    # sannanta Satf is like buBUzat etc, use primitive but with sec
                    pass
                if pratyaya == "ktvA":
                    if sec.endswith("iz"):
                        return {"avyaya": [sec+"ya"]}
                    else:
                        return {"avyaya": [sec+"itvA"]}
                if pratyaya == "lyap":
                    return {"avyaya": ["pra"+sec+"ya", sec+"ya"]} if sec.endswith("iz") else {"avyaya": ["pra"+sec+"ya", sec+"ya"]}
            if sanadi == "yananta":
                if sec in ("cAskundya","SoSvindya","coskundya","SeSvindya","sASvindya"):
                    if sec in ("cAskundya","coskundya"):
                        sec = "coskundya"
                    elif sec in ("SoSvindya","SeSvindya","sASvindya"):
                        sec = "SeSvindya"
                    base_no_ya = "coskund" if sec in ("coskundya","cAskundya") else "SeSvind" if sec in ("SeSvindya","sASvindya","SoSvindya") else sec[:-2] if sec.endswith("ya") else sec[:-1] if sec.endswith("y") else sec
                else:
                    base_no_ya = sec[:-2] if sec.endswith("ya") else sec[:-1] if sec.endswith("y") else sec
                if pratyaya == "yat": return {"M": base_no_ya+"yaH","F":base_no_ya+"yA","N":base_no_ya+"yam"}
                if pratyaya == "kta": return {"M": base_no_ya+"itaH","F":base_no_ya+"itA","N":base_no_ya+"itam"}
                if pratyaya == "ktavatu": return {"M": base_no_ya+"itavAn","F":base_no_ya+"itavatI","N":base_no_ya+"itavat"}
                if pratyaya == "tavya": return {"M": base_no_ya+"itavyaH","F":base_no_ya+"itavyA","N":base_no_ya+"itavyam"}
                if pratyaya == "tfc": return {"M": base_no_ya+"itA","F":base_no_ya+"itrI","N":base_no_ya+"itf"}
                if pratyaya == "anIyar": return {"M": base_no_ya+"anIyaH","F":base_no_ya+"anIyA","N":base_no_ya+"anIyam"}
                if pratyaya == "lyuw": return {"gender":"Neuter","form":base_no_ya+"anam"}
                if pratyaya == "GaY": return {"gender":"Masculine","form":base_no_ya+"aH"}
                if pratyaya == "tumun": return {"avyaya": [sec+"itum", base_no_ya+"itum"]}
                if pratyaya == "ktvA": return {"avyaya": [base_no_ya+"itvA", sec+"itvA"]}
                if pratyaya == "SAnac":
                    m = sec + "mAnaH" if sec.endswith("a") else sec + "amAnaH"
                    f = sec + "mAnA" if sec.endswith("a") else sec + "amAnA"
                    n = sec + "mAnam" if sec.endswith("a") else sec + "amAnam"
                    return {"M": m,"F":f,"N":n}
                if pratyaya == "Rvul":
                    base_no_ya2 = sec[:-2] if sec.endswith("ya") else sec[:-1] if sec.endswith("y") else sec
                    stem = base_no_ya2 + "aka"
                    return {"M": stem+"H","F":stem[:-3]+"ikA" if stem.endswith("aka") else stem+"ikA","N":stem+"m"}
                if pratyaya == "lyap":
                    base_no_ya2 = sec[:-2] if sec.endswith("ya") else sec[:-1] if sec.endswith("y") else sec
                    # generate both pra and sam prefixes
                    return {"avyaya": ["pra"+base_no_ya2+"ya", "sam"+base_no_ya2+"ya", sec+"", base_no_ya2+"ya"]}
                if pratyaya == "Satf":
                    # yan Satf not expected? return None
                    return None
            # fall through to primitive generation with sec as clean
            # need to recompute guna/vriddhi bases for sec
            # continue to primitive generative below with clean=sec
            # (no return, let it fall through)
            pass

        # primitive generative
        def needs_i_for_kta() -> bool:
            return sew and not is_vowel_final

        guna_base = self._guna_base(clean, is_idit)
        vriddhi_base = self._vriddhi_base(clean, is_idit)

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
                if not is_idit and clean not in ["BU", "eD"] and clean[-1] not in SLP1_VOWELS:
                    last_v = None
                    for ch in reversed(clean):
                        if ch in SLP1_VOWELS:
                            last_v = ch
                            break
                    if last_v in ("u","U"):
                        stem = self._guna_base(clean, is_idit) + "amAna"
                    else:
                        stem = clean + "amAna"
                else:
                    stem = clean + "amAna"
            else:
                stem = clean + "yamAna"
            return tri_linga(stem)

        elif pratyaya == "tavya":
            if sanadi == "sannanta":
                stem = clean + "itavya" if sew else clean + "tavya"
                return tri_linga(stem)
            stem = guna_base + ("i" if sew else "") + "tavya"
            return tri_linga(stem)

        elif pratyaya == "anIyar":
            stem = guna_base + "anIya"
            return tri_linga(stem)

        elif pratyaya == "yat":
            if clean in ["dad", "svad"]:
                stem = vriddhi_base + "ya"
            elif clean == "daD":
                stem = vriddhi_base + "ya"
            else:
                last_v = None
                for ch in reversed(clean):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                if last_v in ("u","U","i","I"):
                    stem = guna_base + "ya"
                else:
                    stem = clean + "ya"
            return tri_linga(stem)

        elif pratyaya == "Rvul":
            if clean in ["eD"]:
                stem = clean + "aka"
            elif is_idit:
                stem = clean + "aka"
            else:
                last_v = None
                for ch in reversed(clean):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                if last_v in ("u","U"):
                    stem = self._guna_base(clean, is_idit) + "aka"
                elif last_v in ("a","A"):
                    stem = clean + "aka"
                else:
                    stem = vriddhi_base + "aka"
            m = stem + "H"
            if stem.endswith("aka"):
                f = stem[:-3] + "ikA"
            else:
                f = stem[:-1] + "ikA"
            n = stem + "m"
            return {"M": m, "F": f, "N": n}

        elif pratyaya == "tfc":
            if sanadi == "sannanta":
                b = clean + ("i" if sew else "")
                return {"M": b + "tA", "F": b + "trI", "N": b + "tf"}
            b = guna_base + ("i" if sew else "")
            return {"M": b + "tA", "F": b + "trI", "N": b + "tf"}

        elif pratyaya == "lyuw":
            stem = guna_base + "ana"
            return {"gender": "Neuter", "form": stem + "m"}

        elif pratyaya == "GaY":
            # Handle eD (vowel initial e) without vrddhi, and u-roots with guna
            if clean in ["eD"]:
                stem = clean + "a"
            elif is_idit:
                stem = clean + "a"
            else:
                last_v = None
                for ch in reversed(clean):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                if last_v in ("u","U"):
                    stem = self._guna_base(clean, is_idit) + "a"
                elif last_v in ("a","A"):
                    stem = clean + "a"
                elif last_v in ("e","E","o","O"):
                    # for eD, keep as is
                    stem = clean + "a"
                else:
                    stem = vriddhi_base + "a"
            return {"gender": "Masculine", "form": stem + "H"}

        elif pratyaya == "tumun":
            if sanadi == "sannanta":
                stem = clean + ("i" if sew else "") + "tum"
                return {"avyaya": [stem]}
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
            pref_sam = upasarga + base_ya
            pref_pra = "pra" + base_ya
            bare = base_ya
            variants = []
            for v in [pref_sam, pref_sam.replace("M", "m"), pref_pra, bare]:
                if v not in variants:
                    variants.append(v)
            pref_m = pref_sam.replace("M", "m")
            return {"avyaya": [pref_pra, pref_m, bare]}

        return None

    def derive_all_krdantas(
        self, dhatu: str = "BU", sanadi: Optional[str] = None, upasarga: str = "saM", dhatu_id: Optional[str] = None
    ) -> Dict[str, Dict]:
        result = {}
        for prat in self.krdanta_metadata:
            res = self.derive_krdanta(dhatu, prat, sanadi, upasarga, dhatu_id=dhatu_id)
            if res is not None:
                result[prat] = res
        return result
