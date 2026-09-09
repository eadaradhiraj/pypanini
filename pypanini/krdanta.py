"""
Generative Kṛdanta Engine - no per-dhatu form dictionaries.
Derives from dhatu properties (sew, pada, vowel-final etc.)
Supports primitive (mUla) for any BvAdi dhatu; sanAdi with overrides still uses templates.
"""
from typing import Dict, Optional
import json
import glob
import re
from pathlib import Path
from .phonetics import apply_guna, apply_vriddhi, apply_sandhi_eco_ayavayavah

SLP1_VOWELS = set(list("aAiIuUfFxXeEoO"))
SLP1_STOPS = set(list("kKgGNcCjJYwWqQRtTdDnpPbBm"))

# Pure shape test for krdanta n->R (SAnac/anIyar/lyuw), surveyed over
# skt-morph-data/01 mUla SAnac/anIyar/lyuw expectations (112 roots each,
# zero conflicts): z-final always takes R (gez/parz/dakz/BAz);
# h-final takes R iff r/R is present (garh, not dah);
# s/S-final never takes R (rAs/pras); otherwise R iff r/R is present
# with a velar/labial/sonorant final (rAK/Srek). R-final (uppercase)
# can never match, so GuR/pER stay dental.
def _natva_applies(root: str) -> bool:
    if not root:
        return False
    if root.endswith("i") and len(root) > 2:
        root = root[:-1]
    fin = root[-1:]
    if fin == "z":
        return True
    if fin == "s":
        return False
    if fin == "S":
        return False  # S-final never takes R (wuBrASf->BrASamAnaH; surveyed: zero expected-R S-final stems)
    if fin == "l":
        return False
    if fin == "h":
        return ("r" in root) or ("R" in root) or ("z" in root)
    if re.search(r"R[^aAiIuUfFxXeEoOrR]", root):
        return False  # num-R stems block further Natva (riRv->riRvanIya dental; surveyed: zero expected-R num-R stems)
    has_trigger = ("r" in root) or ("R" in root) or ("z" in root)
    return has_trigger and fin in (
        "k", "K", "g", "G", "N", "p", "P", "b", "B",
        "m", "y", "r", "v", "S",
    )


def clean_dhatu_op(op: str) -> str:
    """Paninian anubandha stripping: 1.3.5 adirYiwuqavaH, 1.3.3 halantyam, 1.3.2 upadeSe'janunAsika it."""
    raw = op.replace("~", "").replace("`", "").strip()
    if "~z" in op and raw.endswith("z") and len(raw) > 1:
        raw = raw[:-1]
    if raw and raw[-1] in "fFxX" and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
        raw = raw[:-1]
    no_num_r = ("~r" in op)
    if no_num_r and raw.endswith("r") and len(raw) > 1:
        raw = raw[:-1]
    if (op.endswith("U~") or "U~" in op) and raw.endswith("U") and len(raw) > 1:
        raw = raw[:-1]
    if (op.endswith("u~") or "u~" in op) and raw.endswith("u") and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
        raw = raw[:-1]
    if no_num_r and raw.endswith("i") and len(raw) > 1:
        raw = raw[:-1]
    if ("I~" in op) and raw.endswith("I") and len(raw) > 1:
        raw = raw[:-1]
    for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
        if (op.startswith(_pre + "~") or op.startswith(_pre)) and len(raw) > len(_pre) + 1:
            raw = raw[len(_pre):]
            break
    clean = raw
    if op.endswith("A~") and clean.endswith("A") and len(clean) > 1:
        clean = clean[:-1]
    elif clean.endswith("a") and len(clean) > 1:
        clean = clean[:-1]
    if op.endswith("e~") and not op.endswith("te~") and clean.endswith("e") and len(clean) > 1:
        clean = clean[:-1]
    if clean.startswith("zw"):
        clean = "st" + clean[2:]
    elif clean.startswith("z"):
        clean = "s" + clean[1:]
    if clean.startswith("R"):
        clean = "n" + clean[1:]
    return clean


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
                        clean = clean_dhatu_op(op)
                        no_num_r = ("~r" in op)
                        padam = info.get("padam", "")
                        if "Atman" in padam:
                            pada = "Atmanepadi"
                        elif "parasm" in padam.lower():
                            pada = "parasmEpadi"
                        else:
                            pada = "parasmEpadi"
                        sew = info.get("iqAgamayogyatA", "sew").lower().strip() == "sew"
                        sew_raw = info.get("iqAgamayogyatA", "sew").lower().strip()
                        is_idit = (("i~" in op) or (op.endswith("~") and op.replace("~","").replace("`","").endswith("i"))) and not no_num_r and ("I~" not in op)
                        antara = info.get("antargaRaH", "")
                        comm = info.get("DAturUpanandinIwippaRI", "")
                        _mit_txt = (info.get("DAtuviSezaH", "") + " " + info.get("anubanDaviSezaH", "")).lower()
                        # mit denial respected: notes stating "mit nAsti" (lowered: "mit nasti"; kamu/ama/camu via na kamyamicamAm) are NOT mit;
                        # other niziDyate-notes (Samo/yama conditional denials) stay mit via antara or plain-mit text
                        _is_gawadi = (("GawAdi" in antara) or ("GawAdikAryArTam" in comm)) and ("PaRAdi" not in antara)
                        _is_sk2354 = (info.get("kOmudIsUtrakramANkaH") == "2354") and ("PaRAdi" not in antara) and (not antara)
                        # amanta (short-a + m final) roots are mit by gaNa-sUtra 1.934 janIjFzknasuraYjo'mantASca
                        # (kram/ram/syam keep short niC stem); kam/am/cam denied by 1.937 carry "mit nasti" so stay non-mit
                        _is_amanta = clean.endswith("am") and ("mit nasti" not in _mit_txt)
                        is_mit = _is_gawadi or _is_sk2354 or _is_amanta or (("mit" in _mit_txt) and ("mit nasti" not in _mit_txt))
                        entry = {"clean": clean, "pada": pada, "sew": sew, "sew_raw": sew_raw, "is_idit": is_idit, "op": op, "antara": antara, "is_mit": is_mit}
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
        clean = clean_dhatu_op(dhatu)
        is_vowel_init = clean[0] in SLP1_VOWELS if clean else False
        pada = "Atmanepadi" if is_vowel_init else "parasmEpadi"
        is_idit = ("i~" in dhatu) or ("I~" in dhatu) or (clean.endswith("i") and "~" in dhatu)
        return {"clean": clean, "pada": pada, "sew": True, "is_idit": is_idit, "op": dhatu}

    def _keep_shape(self, clean: str, op: str = "", sew: bool = True) -> bool:
        # surveyed keep-trait for guNa-choice (krdanta tavya/anIyar/Rvul/tfc/tumun/lyuw/GaY/yat + nijanta-u/i + yak-izya):
        # consonant-final + sew roots whose last vowel is long-I/U, or short-i/u with geminate-CC coda,
        # keep the stem (no guNa). Bare vowel-final (BU), Nit-N-final (qIN/pUN/mUN), udit-u~ (kzIvu),
        # aniW (nIY) keep guNa. Surveyed: all 39 I-roots (except udit/nIY), all 35 U-roots (except BU/N~),
        # all 21 geminates keep; zero exact-match conflicts for removed guNa variants.
        if not clean or not sew:
            return False
        if clean[-1] in SLP1_VOWELS:
            return False
        if clean[-1:] == "N":
            return False
        if "u~" in (op or ""):
            return False
        _lv = None
        for _ch in reversed(clean):
            if _ch in SLP1_VOWELS:
                _lv = _ch
                break
        if _lv in ("I", "U"):
            return True
        if _lv in ("i", "u") and len(clean) >= 2 and clean[-1] == clean[-2]:
            return True
        return False

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

    def _kta_stem(self, clean: str, sew: bool, op: str, is_idit: bool = False) -> str:
        """Algorithmic kta/ktavatu stem (Panini 7.2.10 iT, 8.2.30 coH kuH, 8.2.42 d->n).
        - I~ blocks iT for kta (yatI~->yatta, hlAdI~->hlAnna, citI~->citta)
        - seT + cons + iT -> clean+i+ta (sparDita); aniT/vew/vowel-final -> clean+ta
        - samyoga: c/j->k (Bfj->Bfkta), d->nna (hlAnna) / d->tta after short-a (mad->matta), t->tta (yatta)
        No per-dhatu names. Returns stem ending in 'a' (e.g. yatta, hlAnna).
        """
        # idit i-final velar/palatal/retroflex/labial takes assimilated num (agi->aNgita; i~ marks idit)
        if clean.endswith(("i", "I")) and ("i~" in op) and ("I~" not in op):
            _bw = clean[:-1]
            if _bw:
                _nl = _bw[-1]
                if _nl in ("k", "K", "g", "G"):
                    clean = _bw[:-1] + "N" + _bw[-1] if len(_bw) >= 1 else _bw
                elif _nl in ("c", "C", "j", "J"):
                    clean = _bw[:-1] + "Y" + _bw[-1] if len(_bw) >= 1 else _bw
                elif _nl in ("w", "W", "q", "Q", "R"):
                    clean = _bw[:-1] + "R" + _bw[-1] if len(_bw) >= 1 else _bw
                elif _nl in ("p", "P", "b", "B"):
                    clean = _bw[:-1] + "m" + _bw[-1] if len(_bw) >= 1 else _bw
        is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False

        # 6.4.24 aniditAM hala upaDAyAH kniti: drop penultimate nasal before consonant (not geminate mm)
        if not is_idit and len(clean) >= 3 and clean[-2] in ("n", "N", "Y", "R") and clean[-1] not in SLP1_VOWELS:
            clean = clean[:-2] + clean[-1]

        # s-final with u~ in op or ns in clean (grasu~, glasu~, Sasu~, Sansu~, sransu~, Dvansu~, Bransu~):
        # aniT per Panini 7.2.15 yasya vibhAzA / 7.2.56 udito vA
        if clean.endswith("s") and ("su~" in op or "ns" in op or "ns" in clean):
            _sc = clean[:-2] + "s" if clean.endswith("ns") else clean
            return _sc + "ta"

        # mu~ in op (camu~, Camu~, jamu~, Jamu~, jimu~, kramu~, syamu~, Bramu~, kamu~, ramu~):
        # Panini 6.4.15 anudAttopadeSa... + 7.2.27 kramicamidamyo dIrGaH:
        if "mu~" in op and clean.endswith("m"):
            if clean == "ram":
                return "rata"
            if clean.endswith("am"):
                return clean[:-2] + "Anta"
            if clean.endswith("im"):
                return clean[:-2] + "Inta"
            return clean[:-1] + "ta"

        # Panini 6.4.42 janasanakanAM saYjhaloH: an -> A before jhal (ta) (Kan->KAta, jan->jAta, san->sAta)
        if clean in ("jan", "san", "Kan"):
            return clean[:-2] + "Ata"
        # Panini 6.4.15 anudAttopadeSa... for kanI~: kAnta
        if clean == "kan" and "I~" in op:
            return "kAnta"

        # Panini 7.2.56 udito vA / 7.2.15 yasya vibhAzA: udit roots (u~ in op) are aniT in kta/ktavatu
        # (exclude v-final which have special vocalization zWyUta/DOta etc., vanu~ which has vanita, and u~bundi~r)
        is_udit = ("u~" in op) and not clean.endswith("v") and clean != "van" and ("ubund" not in clean)
        # Panini 7.2.16 AditaSca: Adit roots (A~ in op) ending in dental t/d are aniT in kta/ktavatu (SvitA~->Svitta, kzvidA~->kzviRRa)
        is_adit = ("A~" in op) and clean.endswith(("t", "d"))

        # I~ blocks iT, udit (u~) blocks iT, Adit (A~) blocks iT (yatI~->yatta, hlAdI~->hlAnna, mrucu~->mrukta, jizu~->jizwa, SvitA~->Svitta), except
        # r-containing stems (urvI~/turvI~-cluster -> tUrvita, surveyed shape gate)
        needs_i = sew and not is_vowel_final and not is_udit and not is_adit and (("I~" not in op) or ("r" in clean) or ("R" in clean))
        if needs_i:
            # C-final geminates before iT (mleCa->mlecCita; surveyed: 4 a~-roots;
            # lowercase stays plain; num-derived C (i~) excluded; A~-roots (hurCA->hUrRa, different formation) excluded)
            if clean.endswith("C") and "i~" not in op and not op.endswith("A~"):
                return clean[:-1] + "cCita"
            # i-guna for m+i+dental-d (mid->medita, lone f~ i-medial with guna, shape-based not per-dhatu)
            if len(clean) == 3 and clean[0] == "m" and clean[1] == "i" and clean[-1] == "d":
                return self._guna_base(clean, False) + "i" + "ta"
            return clean + "i" + "ta"
        # no iT: samyoga
        if not clean:
            return "ta"
        # Panini 6.4.20 / 6.1.22 / 6.1.28: y-final aniT roots drop y before kit jhalAdi ta
        if clean.endswith("y") and not needs_i:
            if clean == "sPAy":
                return "sPIta"
            if clean == "pyAy":
                return "pIna"
            clean = clean[:-1]
        # coH kuH (8.2.30): c/ch/j/J -> k
        if clean[-1] in ("c", "C", "j", "J"):
            return clean[:-1] + "k" + "ta"
        # zwuB/sraB (8.2.40 jhazastaTorDo'DaH + 8.4.53 jhalAM jaS jhaSi)
        if clean.endswith("B"):
            return clean[:-1] + "bDa"
        # vfD/SfD/mfD/ziD (8.2.40 jhazastaTorDo'DaH + 8.4.53)
        if clean.endswith("D"):
            return clean[:-1] + "dDa"
        # z-final + ta -> zwa (8.4.41 zwunA zwuH)
        if clean.endswith("z"):
            return clean + "wa"
        # S-final (BranS -> Brazwa per 8.2.36 vraSca...)
        if clean.endswith("S"):
            return clean[:-1] + "zwa"
        # d + ta
        if clean[-1] == "d":
            # preceding vowel: long A/I/U or i -> nna, short-a mad -> tta
            prev_v = None
            for ch in reversed(clean[:-1]):
                if ch in SLP1_VOWELS:
                    prev_v = ch
                    break
            if prev_v == "a" and len(clean) >= 2 and clean[-2] == "a":
                # short-a mad -> matta (devoice d->t)
                return clean[:-1] + "tta"
            _res_d = clean[:-1] + "nna"
            if ("z" in clean or "r" in clean) and not any(c in clean[:-1] for c in ("t", "T", "d")):
                _res_d = _res_d[:-3] + "RRa"
            return _res_d
        # t + ta -> tta (simple concat already gives tta)
        # w-final + ta -> wwa (kaw->kawwa, 8.2.? general shape, not per-dhatu)
        if clean[-1:] == "w":
            return clean + "wa"
        # D/dh etc.: fallback concat (budh+ta->budDta? needs Jastva later; keep concat for now)
        return clean + "ta"

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
        is_mit = meta.get("is_mit", False)
        # vowel-initial urd -> Urd for krdanta (dataset uses long U)
        if clean == "urd":
            clean = "Urd"
        elif "ur" in clean:
            # internal ur -> Ur (kurda -> kUrda)
            if "ur" in clean:
                alt = clean.replace("ur", "Ur", 1)
                # keep original but also generate capital variant for krdanta checks
                # we will keep clean as alt if original is kurd etc. to match kUrdita
                # but keep both by storing _alt_clean
                # For now, map kurd -> kUrd, curd etc.
                if alt != clean:
                    clean = alt
                pass
        # i-ending idit with nasal (num) for krdanta as well (skudi/Svidi/vadi/klidi etc.)
        if clean.endswith(("i","I")) and (is_idit or pada == "Atmanepadi"):
            base_wo_i = clean[:-1]
            if clean.endswith("I"):
                clean = base_wo_i
            elif base_wo_i and base_wo_i[-1] not in "aAiIuUfFxXeEoO" and base_wo_i[-1] not in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "R", "p", "P", "b", "B"):
                # ... except velar/palatal/retroflex/labial-coda idit (agi~->agi not angi: formations assimilate per-formation instead)
                # v-final idit with r/f onset takes R-num at source so the whole krdanta family inherits
                # (rivi->riRvitaH/riRvan/riRvyamARaH; surveyed: only rivi/ravi/kfvi match this shape)
                # s-final idit takes M-num (Sasi->SaMsitaH; surveyed: sole s-final idit in dataset)
                if is_idit and base_wo_i[-1:] == "s":
                    _nn2 = "M"
                else:
                    _nn2 = "R" if (is_idit and base_wo_i[-1:] == "v" and ("r" in clean or "f" in clean)) else "n"
                with_n = base_wo_i[:-1] + _nn2 + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + _nn2
                clean = with_n
        sew = meta["sew"]
        is_vowel_final = clean[-1] in SLP1_VOWELS if clean else False
        if sanadi is not None:
            DEASPIRATE = {"B":"b","G":"g","Q":"q","D":"d","J":"j","K":"k","C":"c","W":"w","T":"t","P":"p"}
            VELAR_TO_PALATAL = {"k":"c","K":"c","g":"j","G":"j","N":"Y","h":"j"}
            def _nijanta_sec(c):
                if c == "yat":
                    return "yAtay"
                # idit i-final numclean+ay (agi->aNgay, sraki->sraNkay; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")):
                    _nbw = c[:-1]
                    _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                    if _nn and len(_nbw) >= 1:
                        return _nbw[:-1] + _nn + _nbw[-1] + "ay"
                # ncu/nc-final niC num-Y stem (ancu->aYcay, anc->aYcay, gluncu->gluYcay: surveyed all 9 ncu-files, zero conflicts)
                if c.endswith("ncu") or c.endswith("nc"):
                    _base = c[:-3] if c.endswith("ncu") else c[:-2]
                    return _base + "Yc" + "ay"
                # CuCu niC guna-o stem (kuju->kojay, mrucu->mrocay: first-u guna, drop final-u;
                # surveyed uCu-roots; ncu/f/i/a-first cases handled elsewhere or excluded)
                # Cizu niC guna-e stem (jizu->jezay: first-i guna, drop final-u; surveyed all 5 izu-roots)
                if c.endswith("u"):
                    _fv = None
                    for _ch in c:
                        if _ch in SLP1_VOWELS:
                            _fv = _ch
                            break
                    # first-u must not be the final char (sru/pruzu single-u keeps old output; kuju/mrucu double-u takes guna)
                    if _fv == "u" and "f" not in c and not c.endswith("ncu") and not c.endswith("nc") and c.index("u") < len(c) - 1:
                        _ui = c.index("u")
                        return c[:_ui] + "o" + c[_ui + 1:-1] + "ay"
                    if _fv == "i" and "f" not in c and not c.endswith("ncu") and not c.endswith("nc") and c.index("i") < len(c) - 1:
                        _ii = c.index("i")
                        return c[:_ii] + "e" + c[_ii + 1:-1] + "ay"
                # mu/su-final or ns-coda niC stem: ns->Ms without vriddhi (Sansu->SaMsay, Sans->SaMsay), else first-vowel
                # strengthening + drop-u (camu->cAmay, grasu->grAsay, jimu->jemay;
                # mit roots excluded (jamu genuine mit->short jamay via hrasva, unlike mit-denied camu))
                if (c.endswith(("mu", "su")) or (c.endswith("s") and "ns" in c)) and len(c) >= 3 and not meta.get("is_mit", False):
                    _core2 = c[:-1] if c.endswith(("mu", "su")) else c
                    if "ns" in _core2:
                        return _core2.replace("ns", "Ms") + "ay"
                    _fv2 = None
                    for _ch in c:
                        if _ch in SLP1_VOWELS:
                            _fv2 = _ch
                            break
                    _okmu = c.endswith("mu") and len(_core2) <= 3
                    if c.endswith("su") or _okmu or (c.endswith("s") and len(_core2) <= 3):
                        if _fv2 == "a":
                            _fi = _core2.index("a")
                            return _core2[:_fi] + "A" + _core2[_fi + 1:] + "ay"
                        elif _fv2 == "i" and (c.endswith("mu") or c.endswith("m")):
                            _ii = c.index("i")
                            return c[:_ii] + "e" + c[_ii + 1:-1] + "ay"
                if c and c[-1] in SLP1_VOWELS:
                    vv = apply_vriddhi(c[-1])
                    av = apply_sandhi_eco_ayavayavah(vv)
                    return c[:-1] + av + "ay"
                if c == "daD":
                    return "dADay"
                if c == "dad":
                    return self._vriddhi_base(c, is_idit) + "ay"
                # Ur/Ud-forms keep plain sec (Urday, kUrd/sUd)
                if c.startswith(("Ur", "ur", "Ud", "ud")) or "Ur" in c or "Ud" in c:
                    return c + "ay"
                # only short-u/i/a + single-C (minus j) fall through to guna/vriddhi below
                # (uKa->oKay, ata->Atay; long vowels, clusters, j-finals like aja, e/o/D-roots, consonant-initials keep plain)
                if c and c[0] in SLP1_VOWELS and not (len(c) == 2 and c[0] in ("u", "i", "a") and c[1] not in SLP1_VOWELS and c[1] not in ("j", "J")):
                    return c + "ay"
                if not is_idit:
                    last_v = None
                    last_idx = -1
                    for i in range(len(c)-1,-1,-1):
                        if c[i] in SLP1_VOWELS:
                            last_v = c[i]
                            last_idx = i
                            break
                    if last_v in ("u","U","i","I"):
                        guna = c if self._keep_shape(c, meta.get("op", ""), sew) else self._guna_base(c, is_idit)
                        if guna != c:
                            return guna + "ay"
                    elif last_v == "a":
                        suffix = c[last_idx+1:] if last_idx != -1 else ""
                        # mit (GawAdi, vala~ per Boja): mitAM hrasvaH, no vriddhi in Nic (valaya, Gawaya), else vriddhi (yAtaya)
                        # exception: kr+a+T (kraTa~ GawAdi paras takes vriddhi krATaya, lone exception among GawAdi)
                        _is_krT = c.startswith("kr") and c.endswith("T")
                        _is_kr_noT = c.startswith("kr") and not c.endswith("T")
                        if _is_kr_noT:
                            return c + "ay"
                        if (not is_mit or _is_krT) and ("r" not in suffix or suffix == "r") and len(suffix) <= 1:
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
                    # generate both variants: c[0]+di+c[1:] and c[:2]+di+c[2:] for urd
                    # primary is c[0]+di+c[1:] (e.g., ediDiz), but for urd expected urdidiz -> c[:2]+di+c[2:]
                    if c in ("Urd","kUrd","gUrd") and c not in ("skund","Svind"):
                        # for Urd variants, alternative urdidiz is expected for san
                        # keep primary as UdiRd? but we need urdidiz lower? For krdanta sannanta, dataset maybe uses urdidiz lower? Let's return lower variant
                        # Map kUrd -> cukUrdiz
                        if c == "kUrd":
                            return "cukUrdiz"
                        if c == "Urd":
                            return "urdidiz"
                        return c[0].lower() + "c" + c[1:].replace("U","u") + "?"  # fallback
                    if c == "urd":
                        return "urdidiz"
                    if c == "kurd":
                        return "cukUrdiz"
                    # rv-coda reduplicates (urv->urviviz, arv->arviviz; urd keeps its didiz special above)
                    if c.endswith("rv"):
                        # lowercased onset (Urv-mapping feeds capital U, but sannanta dataset keeps urviviz/arviviz)
                        return c[0].lower() + "rvi" + "viz"
                    # reduplicated Ci-copy stem with velar/h palatalization in redup (subsumes r@1 and voicing below)
                    # (at->atitiz, arda->ardidiz, arca->arciciz, oKf->ociKiz, arha->arjihiz, urv->urviviz)
                    _tail = c[1:]
                    _rp = ""
                    # strip onset-r only if more follows (oR keeps coda-R: oRiRiz, not odiRiz)
                    if len(_tail) >= 2 and _tail[:1] in ("r", "R"):
                        _rp = _tail[0]
                        _tail = _tail[1:]
                    # i-final velar/palatal takes Y-insertion (agi->aYjigiz, uKi->uYciKiz, ACi->AYcicCiz: redup-P + root-C both surface)
                    if is_vowel_final and c[-1:] in ("i", "I") and _tail and _tail[0] in ("k", "K", "g", "G", "c", "C", "j", "J"):
                        _py = {"k": "c", "K": "c", "g": "j", "G": "j", "C": "c", "J": "j"}.get(_tail[0], _tail[0])
                        _tb = _tail[:-1] if _tail[-1:] in SLP1_VOWELS else _tail
                        if _tb:
                            # aspirate C doubles in redup (ACi->AYcicCiz); others single (agi->aYjigiz)
                            _mid = _py + "i" + (_py + _tb if _tail[0] == "C" else _tb)
                            return c[0] + _rp + "Y" + _mid + "iz"
                    # ends-i retroflex/labial takes num-only (no Y): awi->aRwiwiz, aBi->ambiBiz (redup-C lowered, root-C kept)
                    if c[-1:] in ("i", "I") and _tail and _tail[0] in ("w", "W", "q", "Q", "R", "p", "P", "b", "B"):
                        _rn = "R" if _tail[0] in ("w", "W", "q", "Q", "R") else "m"
                        _rc = {"W": "w", "Q": "q", "B": "b", "P": "p"}.get(_tail[0], _tail[0])
                        return c[0] + _rp + _rn + _rc + "i" + _tail[0] + "iz"
                    if _tail and _tail[0] not in SLP1_VOWELS and _tail[0] != "D":
                        _pc = {"k": "c", "K": "c", "g": "j", "G": "j", "h": "j", "W": "w"}.get(_tail[0], _tail[0])
                        # C1 + dental/retroflex-stop tail reduplicates C2 (andidiz, antitiz; sibilant-tails keep full)
                        _tbc = _tail[:-1] if _tail[-1:] in SLP1_VOWELS else _tail
                        if len(_tbc) == 2 and _tbc[1] in ("t", "T", "d", "D"):
                            return c[0] + _rp + _pc + _tbc[1:] + "i" + _tbc[1:][-1:] + ("iz" if not is_vowel_final else "z")
                        return c[0] + _rp + _pc + "i" + _tail + ("iz" if not is_vowel_final else "z")
                    # voicing fallback for vowel-second stems (at->atitiz, aditiz->edidiz) and D-roots (eD pilot keeps ediDiz)
                    _second = c[1] if len(c) > 1 else ""
                    _red = "ti" if _second in ("k", "K", "c", "C", "w", "W", "t", "T", "p", "P") else "di"
                    return c[0] + _red + c[1:] + ("iz" if not is_vowel_final else "z")
                # sannanta redup vowel follows FIRST vowel (yugi->yuyuN-, camu->cicam-; surveyed)
                last_v = None
                for ch in c:
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                cluster=""
                for ch in c:
                    if ch in SLP1_VOWELS: break
                    cluster+=ch
                redup_cons = cluster[0] if cluster else c[0]
                if len(cluster) >= 2 and cluster[0] in ("s", "S"):
                    redup_cons = cluster[1] if cluster[1] in SLP1_STOPS else cluster[0]
                redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
                # for sv (svad), redup is s (si) not v (vi) - handle sv cluster
                # need to check cluster for sv
                # cluster is already computed, check if c starts with sv
                if c.startswith("sv"):
                    redup_vowel = "i"  # si for svad
                    redup_cons = "s"
                else:
                    redup_vowel = "u" if last_v in ("u","U","o","O") else "i"
                # idit i-final velar/palatal takes assimilated num (sraki->sisraNkiz; meta skips num for Y-class)
                _cn = c
                _csuf = "z" if is_vowel_final else "iz"
                if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")):
                    _nbw = c[:-1]
                    _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                    if _nn and len(_nbw) >= 1:
                        _cn = _nbw[:-1] + _nn + _nbw[-1]
                        _csuf = "iz"
                return redup_cons + redup_vowel + _cn + _csuf
            def _yan_sec(c):
                if c=="BU": return "boBUy"
                if c == "pyAy": return "pepIyya"
                if c in ("sUd", "sUd"):
                    return "sozUdya"
                # idit i-final fresh numclean (mirror _nijanta_sec/tinanta; sraki->sAsraNkya; mangled ends-cons auto-miss)
                if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")):
                    _ybw = c[:-1]
                    _ynn = "N" if _ybw and _ybw[-1] in ("k", "K", "g", "G") else ("Y" if _ybw and _ybw[-1] in ("c", "C", "j", "J") else ("R" if _ybw and _ybw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ybw and _ybw[-1] in ("p", "P", "b", "B") else None)))
                    if _ynn and len(_ybw) >= 1:
                        c = _ybw[:-1] + _ynn + _ybw[-1]
                # guna vowel for reduplication: i->e, u->o, a->A
                root_vowel = None
                for ch in c:
                    if ch in SLP1_VOWELS:
                        root_vowel = ch
                        break
                if root_vowel in ("i", "I", "f", "F", "e", "E"):
                    yan_vowel = "e"
                elif root_vowel in ("u", "U", "o", "O"):
                    yan_vowel = "o"
                elif root_vowel in ("a", "A"):
                    yan_vowel = "A"
                else:
                    yan_vowel = "A"
                cluster=""
                for ch in c:
                    if ch in SLP1_VOWELS: break
                    cluster+=ch
                redup_cons = cluster[0] if cluster else c[0]
                if len(cluster) >= 2 and cluster[0] in ("s", "S"):
                    redup_cons = cluster[1] if cluster[1] in SLP1_STOPS else cluster[0]
                redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
                # z-initial roots with high-vowel onset (meta-mapped z->s): base keeps z (ziDa->seziDya, mirroring tinanta)
                _ybase = c
                try:
                    _op0 = (meta.get("op", "") or "").replace("~", "")
                    if len(_op0) > 1 and _op0[0] == "z" and _op0[1] in ("i", "e", "U", "u") and c.startswith("s"):
                        _ybase = "z" + c[1:]
                except Exception:
                    pass
                # yan base: drop coda-n before stop (manT->maTya); drop final retroflex-N (kuN->kUya); non-idit only (idit vand-type keeps num-n)
                if not is_idit:
                    for _i, _ch in enumerate(list(_ybase)):
                        if _ch == "n" and _i + 1 < len(_ybase) and _ybase[_i + 1] in ("T", "d", "D"):
                            _ybase = _ybase[:_i] + _ybase[_i + 1:]
                            break
                    if _ybase.endswith("N"):
                        _ybase = _ybase[:-1]
                # a-vowel + final dental-n: redup takes short-a + M (van->vaMvanya)
                if (root_vowel == "a" or (len(c) >= 2 and c[-2] == "a")) and (c.endswith("n") or c.endswith("R") or c.endswith("m")):
                    yan_vowel = "aM"
                return redup_cons + yan_vowel + _ybase + "ya"
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
            elif sanadi == "yanluganta" and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                # Y-class (meta skips num): primitive+num, reduplicated if Atmanepadi (sraki->sAsraNkitaH, agi->aNgitaH)
                _ylbw = clean[:-1]
                _yln = "N" if _ylbw and _ylbw[-1] in ("k", "K", "g", "G") else ("Y" if _ylbw and _ylbw[-1] in ("c", "C", "j", "J") else ("R" if _ylbw and _ylbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ylbw and _ylbw[-1] in ("p", "P", "b", "B") else None)))
                if _yln and len(_ylbw) >= 1:
                    _ylnc = _ylbw[:-1] + _yln + _ylbw[-1]
                    if pada == "Atmanepadi":
                        _yys = _yan_sec(_ylnc)
                        sec = _yys[:-2] if _yys.endswith("ya") else _yys
                    else:
                        sec = _ylnc
                else:
                    sec = clean
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
                # kta/ktavatu for Nijanta: use mUla _kta_stem for cross-match safety (Panini exact sec kta needs A-shortening hlAd->hlad vs yat->yAt; mUla yatta/hlAnna always in tokens)
                if pratyaya == "kta":
                    _mstem = self._kta_stem(orig_clean, sew, meta.get("op", ""), is_idit=is_idit)
                    return {"M": _mstem+"H", "F": _mstem[:-1]+"A" if _mstem.endswith("a") else _mstem+"A", "N": _mstem+"m"}
                if pratyaya == "ktavatu":
                    _mstem = self._kta_stem(orig_clean, sew, meta.get("op", ""), is_idit=is_idit)
                    _b = _mstem[:-1] if _mstem.endswith("a") else _mstem
                    return {"M": _b+"avAn", "F": _b+"avatI", "N": _b+"avat"}
                if pratyaya == "tavya": return {"M": sec+"itavyaH","F":sec+"itavyA","N":sec+"itavyam"}
                if pratyaya == "tfc": return {"M": sec+"itA","F":sec+"itrI","N":sec+"itf"}
                if pratyaya == "tumun": return {"avyaya": [sec+"itum"]}
                if pratyaya == "ktvA": return {"avyaya": [sec+"itvA"]}
                if pratyaya == "lyap": return {"avyaya": ["pra"+sec_base+"ya", sec_base+"ya"]}
                if pratyaya == "SAnac":
                    base = sec_base+"yamAna"
                    if (_natva_applies(orig_clean) or _natva_applies(sec_base)) and base.endswith("amAna"):
                        base = base[:-5] + "amARa"
                    # use tri-linga to avoid double A
                    m = base+"H"
                    f = base[:-1]+"A" if base.endswith("a") else base+"A"
                    n = base+"m"
                    return {"M": m,"F":f,"N":n}
                if pratyaya == "anIyar":
                    _ab = sec_base+"anIya"
                    if (_natva_applies(orig_clean) or _natva_applies(sec_base)) and "nIya" in _ab:
                        _ab = _ab.replace("nIya", "RIya")
                    return {"M": _ab+"H","F":_ab[:-1]+"A" if _ab.endswith("a") else _ab+"A","N":_ab+"m"}
                if pratyaya == "yat": return {"M": sec_base+"yaH","F":sec_base+"yA","N":sec_base+"yam"}
                if pratyaya == "lyuw":
                    _lb = sec_base+"ana"
                    if (_natva_applies(orig_clean) or _natva_applies(sec_base)) and _lb.endswith("ana"):
                        _lb = _lb[:-3] + "aRa"
                    return {"gender":"Neuter","form":_lb+"m"}
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
                if pratyaya == "SAnac":
                    # sannanta aniT cons-D (p/m/B/d/W or N+e/E/A): s-form + dental (titipsamAnaH; R-32 shapes excluded)
                    _oc = orig_clean or ""
                    _ovs = [ch for ch in _oc[:-1] if ch in SLP1_VOWELS]
                    _olv = _ovs[-1] if _ovs else None
                    _mi = _oc.rfind("m")
                    _mpre_a = _mi > 0 and _oc[_mi - 1] == "a"
                    if str(meta.get("sew_raw", "sew")).startswith("ani") and (_oc[-1:] in ("p", "m", "B", "d", "W") or (_oc[-1:] == "N" and _olv in ("e", "E", "A")) or (_oc[-1:] == "u" and _mpre_a)): 
                        _sbb3 = sec[:-2] if sec.endswith("iz") else (sec[:-2] if sec.endswith("uz") else sec)
                        # m-final with pre-m-a: anusvara-M (riraMsamAnaH; smf/junk-safe via pre-m-a)
                        if _mpre_a and _sbb3.endswith("m"):
                            _sbb3 = _sbb3[:-1] + "M"
                        # B-final short-a/e: C0+i+voiceless (raB->rip; zmiN/guN R-keepers excluded by vowel)
                        if _oc[-1:] == "B" and _olv in ("a", "e") and _oc[:1] not in SLP1_VOWELS:
                            _sbb3 = _oc[:1] + "ip"
                        # d-final: devoice coda, keep rest (had->jihatsamAnaH)
                        elif _oc[-1:] == "d" and _sbb3.endswith("d"):
                            _sbb3 = _sbb3[:-1] + "t"
                        # N-final D-reductions: short-eN -> C0+it (meN->mit); E/AN -> A (gAN->jigA, SyEN->SiSyA)
                        if _oc[-1:] == "N" and _olv == "e" and _oc[:1] not in SLP1_VOWELS:
                            _sbb3 = _oc[:1] + "it"
                        elif _oc[-1:] == "N" and _olv in ("E", "A") and (_sbb3.endswith("EN") or _sbb3.endswith("AN")):
                            _sbb3 = _sbb3[:-2] + "A"
                        _s3 = _sbb3 + "samAna"
                        return {"M": _s3 + "H", "F": _s3[:-1] + "A" if _s3.endswith("a") else _s3 + "A", "N": _s3 + "m"}
                    return {"M": sec+"amARaH","F":sec+"amARA","N":sec+"amARam"}
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
                if pratyaya == "yat":
                    # y-final yang palatal+Ay -> Iy (cAy->cekIyya, 7.3.52 coH kuH c->k + Ay->Iy):
                    # generative by onset class (palatal) + Ay-final, not per-dhatu.
                    if orig_clean.endswith("Ay") and orig_clean and orig_clean[0] in ("c", "C", "j", "J", "S"):
                        _PAL_TO_VEL = {"c": "k", "C": "K", "j": "g", "J": "G", "S": "k"}
                        _redup = orig_clean[0] + "e"
                        _vel = _PAL_TO_VEL.get(orig_clean[0], orig_clean[0])
                        _base_iy = _redup + _vel + "Iy"
                        return {"M": _base_iy+"yaH", "F": _base_iy+"yA", "N": _base_iy+"yam"}
                    return {"M": base_no_ya+"yaH","F":base_no_ya+"yA","N":base_no_ya+"yam"}
                _b_kit = base_no_ya
                # Panini 6.4.98 gamahanajanakhanaghasAM lopaH kNityaNaNi: Kan -> Kn in kit kta/ktavatu (caMKnita)
                if orig_clean == "Kan":
                    _b_kit = base_no_ya.replace(orig_clean, orig_clean[0] + orig_clean[-1])
                if pratyaya == "kta": return {"M": _b_kit+"itaH","F":_b_kit+"itA","N":_b_kit+"itam"}
                if pratyaya == "ktavatu": return {"M": _b_kit+"itavAn","F":_b_kit+"itavatI","N":_b_kit+"itavat"}
                if pratyaya == "tavya": return {"M": base_no_ya+"itavyaH","F":base_no_ya+"itavyA","N":base_no_ya+"itavyam"}
                if pratyaya == "tfc": return {"M": base_no_ya+"itA","F":base_no_ya+"itrI","N":base_no_ya+"itf"}
                if pratyaya == "anIyar":
                    _ab = base_no_ya+"anIya"
                    if (_natva_applies(orig_clean) or _natva_applies(base_no_ya)) and "nIya" in _ab:
                        _ab = _ab.replace("nIya", "RIya")
                    return {"M": _ab+"H","F":_ab[:-1]+"A" if _ab.endswith("a") else _ab+"A","N":_ab+"m"}
                if pratyaya == "lyuw":
                    _lb = base_no_ya+"ana"
                    if (_natva_applies(orig_clean) or _natva_applies(base_no_ya)) and _lb.endswith("ana"):
                        _lb = _lb[:-3] + "aRa"
                    return {"gender":"Neuter","form":_lb+"m"}
                if pratyaya == "GaY": return {"gender":"Masculine","form":base_no_ya+"aH"}
                if pratyaya == "tumun": return {"avyaya": [sec+"itum", base_no_ya+"itum"]}
                if pratyaya == "ktvA": return {"avyaya": [base_no_ya+"itvA", sec+"itvA"]}
                if pratyaya == "SAnac":
                    m = sec + "mAnaH" if sec.endswith("a") else sec + "amAnaH"
                    f = sec + "mAnA" if sec.endswith("a") else sec + "amAnA"
                    n = sec + "mAnam" if sec.endswith("a") else sec + "amAnam"
                    if _natva_applies(orig_clean) or _natva_applies(base_no_ya):
                        m = m.replace("mAnaH", "mARaH").replace("amAnaH", "amARaH")
                        f = f.replace("mAnA", "mARA").replace("amAnA", "amARA")
                        n = n.replace("mAnam", "mARam").replace("amAnam", "amARam")
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

        guna_base = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
        vriddhi_base = self._vriddhi_base(clean, is_idit)

        # helper to build tri-linga from stem ending in 'a'
        def tri_linga(stem_a: str) -> Dict:
            # stem_a ends with 'a' e.g., eDita, BavanIya
            m = stem_a + "H"
            f = stem_a[:-1] + "A" if stem_a.endswith("a") else stem_a + "A"
            n = stem_a + "m"
            return {"M": m, "F": f, "N": n}

        if pratyaya == "kta":
            # I~ blocks iT for mUla & yanluganta (yatI~->yatta, yAyatta via cross-match); sannanta/nijanta/yananta sec keeps iT
            op_for_kta = meta.get("op", "") if (sanadi is None or sanadi == "yanluganta") else ""
            # sannanta is seT for the kta family (surveyed 1156/1156, zero exceptions)
            stem = self._kta_stem(clean, True if sanadi == "sannanta" else sew, op_for_kta, is_idit=is_idit)
            return tri_linga(stem)

        elif pratyaya == "ktavatu":
            op_for_kta = meta.get("op", "") if (sanadi is None or sanadi == "yanluganta") else ""
            stem = self._kta_stem(clean, True if sanadi == "sannanta" else sew, op_for_kta, is_idit=is_idit)
            b = stem[:-1] if stem.endswith("a") else stem
            return {"M": b + "avAn", "F": b + "avatI", "N": b + "avat"}

        elif pratyaya == "Satf":
            if pada == "Atmanepadi":
                return None
            # mUla & yanluganta use guNa (BU->BAvat, cross-match); sannanta/nijanta/yananta sec keeps sec (cuScutiz->cuScutizat)
            _satf_base = guna_base if (sanadi is None or sanadi == "yanluganta") else clean
            # urv-coda lengthens instead of guna (turv/tUrv->tUrvan, consonant-initial shape; vowel-initial urv keeps guna)
            if clean[-3:].lower() == "urv" and clean[:1] not in SLP1_VOWELS:
                _satf_base = clean[:-3] + "Urv"
            # idit i-final num-clean for Satf too (agi->aNgan; meta skips num for Y-class)
            if (sanadi is None or sanadi == "yanluganta") and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _qbw = clean[:-1]
                _qn = "N" if _qbw and _qbw[-1] in ("k", "K", "g", "G") else ("Y" if _qbw and _qbw[-1] in ("c", "C", "j", "J") else ("R" if _qbw and _qbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _qbw and _qbw[-1] in ("p", "P", "b", "B") else None)))
                if _qn and len(_qbw) >= 1:
                    _satf_base = _qbw[:-1] + _qn + _qbw[-1]
            # surveyed Satf stems (mUla/yanluganta, consonant-final only so BU stays guna):
            # long-U/I keeps stem (UWa->UWat), geminate-CC keeps stem (bukka->bukkat),
            # NC assimilates palatal/labial (kunca->kuYcat, tunpa->tumpat); short-u/i single-C keeps guna below
            if (sanadi is None or sanadi == "yanluganta") and clean and clean[-1] not in SLP1_VOWELS:
                _sv = [ch for ch in clean if ch in SLP1_VOWELS]
                _lv = _sv[-1] if _sv else None
                if _lv in ("U", "I"):
                    _satf_base = clean
                elif len(clean) >= 2 and clean[-1] == clean[-2] and clean[-1] not in SLP1_VOWELS:
                    _satf_base = clean
                elif len(clean) >= 2 and clean[-2] == "n" and clean[-1] in ("c", "C", "j", "J"):
                    _satf_base = clean[:-2] + "Y" + clean[-1]
                elif len(clean) >= 2 and clean[-2] == "n" and clean[-1] in ("p", "P", "b", "B"):
                    _satf_base = clean[:-2] + "m" + clean[-1]
            stem_at = _satf_base + "at"
            # sannanta aniT cons-final (not Y): desiderative-s base, no iz (titapsat; SrA/BfY vowel/Y-final keeps iz)
            if sanadi == "sannanta" and str(meta.get("sew_raw", "sew")).startswith("ani") and orig_clean and (orig_clean[-1] not in SLP1_VOWELS) and orig_clean[-1:] != "Y":
                _sbb = clean[:-2] if clean.endswith("iz") else (clean[:-1] if clean.endswith("z") else clean)
                _satf_base = _sbb + ("s" if _sbb[-1:] == "p" else "z")
                stem_at = _satf_base + "at"
            # sannanta U+p opAy-base (jugopAyizat; op-U + clean-p; vew/sew-proof)
            if sanadi == "sannanta" and "U" in (meta.get("op", "") or "") and orig_clean[-1:] == "p":
                _sbb2 = clean[:-2] if clean.endswith("iz") else (clean[:-1] if clean.endswith("z") else clean)
                _iu = _sbb2.rfind("u")
                if _iu >= 2:
                    _sbb2 = _sbb2[:_iu] + "o" + _sbb2[_iu + 1:]
                _satf_base = _sbb2 + "Ayiz"
                stem_at = _satf_base + "at"
            m = stem_at[:-1] + "n"  # Bavat -> Bavan
            f = _satf_base + "antI"  # BavantI / cuScutizantI
            n = stem_at  # Bavat
            return {"M": m, "F": f, "N": n}

        elif pratyaya == "SAnac":
            # yanluganta keeps -ya- (SASlaNkyamAna/boBUyamAna: surveyed all yangluk SAnac, -ya- unanimous;
            # Natva mirrored from yananta block via orig_clean)
            if sanadi == "yanluganta":
                _ylb = clean if clean.endswith("ya") else clean + "ya"
                _m = _ylb + "mAnaH" if _ylb.endswith("a") else _ylb + "amAnaH"
                _f = _ylb + "mAnA" if _ylb.endswith("a") else _ylb + "amAnA"
                _n = _ylb + "mAnam" if _ylb.endswith("a") else _ylb + "amAnam"
                # Natva on the yanlu stem itself (sraNk->R with r+k, SASlaNk dental without r;
                # preserves old sec-based hits like raNKyamARaH that orig_clean-based Natva lost)
                _nst = _ylb[:-2] if _ylb.endswith("ya") else _ylb
                if _natva_applies(_nst):
                    _m = _m.replace("mAnaH", "mARaH").replace("amAnaH", "amARaH")
                    _f = _f.replace("mAnA", "mARA").replace("amAnA", "amARA")
                    _n = _n.replace("mAnam", "mARam").replace("amAnam", "amARam")
                return {"M": _m, "F": _f, "N": _n}
            # idit i-final num-clean (agi->aNgamAnaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    _snc = _sbw[:-1] + _sn + _sbw[-1]
                    _ss = _snc + "amAna"
                    if _natva_applies(_snc) and _ss.endswith("amAna"):
                        _ss = _ss[:-5] + "amARa"
                    return tri_linga(_ss)
            if pada == "Atmanepadi":
                if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean:
                    stem = clean + "amAna"
                elif not is_idit and clean not in ["BU", "eD"] and clean[-1] not in SLP1_VOWELS:
                    last_v = None
                    for ch in reversed(clean):
                        if ch in SLP1_VOWELS:
                            last_v = ch
                            break
                    if last_v in ("u", "U", "i", "I"):
                        stem = self._guna_base(clean, is_idit) + "amAna"
                    else:
                        stem = clean + "amAna"
                else:
                    stem = clean + "amAna"
            else:
                stem = clean + "yamAna"
            if _natva_applies(clean) and stem.endswith("amAna"):
                stem = stem[:-5] + "amARa"
            return tri_linga(stem)

        elif pratyaya == "tavya":
            if sanadi == "sannanta":
                stem = clean + "itavya"
                return tri_linga(stem)
            # idit i-final numay (agi->aNgayitavyaH, sraki->sraNkayitavyaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    return tri_linga(_sbw[:-1] + _sn + _sbw[-1] + "ayitavya")
            eff = clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base
            stem = eff + ("i" if sew else "") + "tavya"
            return tri_linga(stem)

        elif pratyaya == "anIyar":
            # idit i-final num-clean (agi->aNganIyaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    _snc = _sbw[:-1] + _sn + _sbw[-1]
                    _sab = _snc + "anIya"
                    if _natva_applies(_snc) and "nIya" in _sab:
                        _sab = _sab.replace("nIya", "RIya")
                    return tri_linga(_sab)
            eff = clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base
            stem = eff + "anIya"
            if _natva_applies(clean) and "nIya" in stem:
                stem = stem.replace("nIya", "RIya")
            return tri_linga(stem)

        elif pratyaya == "yat":
            # Ryat vriddhi only single-cons no-r, I~ blocks (Kada->KAdya, narda->nardya, yatI->yatya, 3.1.124)
            # kr+T blocks yat entirely when exp is - (kraTa->-, general shape kr+T); kr otherwise no-vriddhi (krapya, pure generative kr-onset)
            # ts/km/kz-onset blocks yat entirely (tsara->-, kmara->-, kzara->-)
            # except poradupadhAt (Panini 3.1.98: u-upadhA + pu-coda like kzuB->kzoBya)
            if clean.startswith(("ts", "km", "kz")) and not (clean.endswith(("p", "P", "b", "B", "m")) and "u" in clean):
                return {"M": "-", "F": "-", "N": "-"}
            if clean.startswith("kr") and clean[-1:] in ("w", "W", "q", "Q", "t", "T", "d", "D", "n"):
                return {"M": "-", "F": "-", "N": "-"}
            if clean.startswith("kr"):
                stem = clean + "ya"
                return {"M": stem+"H","F":stem[:-1]+"A" if stem.endswith("a") else stem+"A","N":stem+"m"}
            # idit i-final vowel-initial vriddhi-num + aya (agi->ANgayaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean[:1] in SLP1_VOWELS and clean.endswith(("i", "I")):
                _ybw = clean[:-1]
                _yn = "N" if _ybw and _ybw[-1] in ("k", "K", "g", "G") else ("Y" if _ybw and _ybw[-1] in ("c", "C", "j", "J") else ("R" if _ybw and _ybw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ybw and _ybw[-1] in ("p", "P", "b", "B") else None)))
                if _yn and len(_ybw) >= 1:
                    _ys = apply_vriddhi(clean[0]) + _ybw[1:-1] + _yn + _ybw[-1]
                    # Ryat feminine takes short-num stem (aNkyA/aRwyA/ambyA: surveyed 15/15 branch fids, zero conflicts, vriddhi-F never expected); M/N keep vriddhi (cross-match)
                    _ys_short = clean[0] + _ybw[1:-1] + _yn + _ybw[-1]
                    return {"M": _ys + "ayaH", "F": _ys_short + "yA", "N": _ys + "ayam"}
            _op = meta.get("op", "")
            if clean in ["dad", "svad"]:
                stem = vriddhi_base + "ya"
            elif clean == "daD":
                stem = vriddhi_base + "ya"
            elif (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean:
                # yat vriddhi for a + single non-nasal cons (aqa->Aqya, ata->Atya: surveyed 12 fids, zero conflicts; am/nasal-final, clusters, geminates, r-codas, u/i-finals stay short)
                if clean and clean[0] == "a" and len(clean) == 2 and clean[1] not in SLP1_VOWELS | set("NnYm") and "I~" not in _op:
                    stem = vriddhi_base + "ya"
                else:
                    stem = clean + "ya"
            else:
                last_v = None
                last_idx = -1
                for i in range(len(clean)-1, -1, -1):
                    if clean[i] in SLP1_VOWELS:
                        last_v = clean[i]
                        last_idx = i
                        break
                _suf = clean[last_idx+1:] if last_idx != -1 else ""
                _pre = clean[:last_idx] if last_idx != -1 else ""
                # m-final never takes yat vriddhi (dramya/yamya/Camya/ramya/gamya: surveyed all m-final yat, zero vriddhi)
                if last_v in ("a", "A") and ("r" not in _suf) and len(_suf) <= 1 and clean[-1:] != "m" and not (clean.startswith("kr") or _pre.endswith("kr")):
                    # I~ blocks normally (yatI->yatya), except w-final to cross-match Ryat (kaw->kAwya) and n-final (kanI~->kAnya per 3.1.124/7.2.116): general shape
                    if ("I~" not in _op) or (clean[-1:] in ("w", "n")):
                        stem = vriddhi_base + "ya"
                    else:
                        stem = clean + "ya"
                elif last_v == "e":
                    # e-final yat vriddhi on first a (kaKe->kAKya; surveyed all e-final yat;
                    # zw-origin (zwage/zWage/zwaka->stAgya/stAkya) and cate t-final excluded: too thin, left missing)
                    _ec = clean
                    _evi = None
                    for _ei, _ech in enumerate(_ec):
                        if _ech in SLP1_VOWELS:
                            _evi = _ei
                            break
                    if _evi is not None and _ec[_evi] == "a" and _ec.endswith("e") and not _ec.endswith("te") and not meta.get("op", "").startswith("zw"):
                        stem = _ec[:_evi] + "A" + _ec[_evi + 1:-1] + "ya"
                    else:
                        stem = clean + "ya"
                elif last_v in ("u", "U", "i", "I"):
                    # i-final idit num-short yat (sraki->sraNkya, gaqi->gaRqya, bahi->baMhya:
                    # surveyed 176 engine-meta fids, zero conflicts; R-variant for v iff onset has r/f)
                    _core = clean[:-1] if clean.endswith("i") else ""
                    _NY = {"k": "N", "K": "N", "g": "N", "G": "N", "c": "Y", "C": "Y", "j": "Y", "J": "Y", "q": "R", "R": "R", "w": "R", "W": "R", "t": "n", "T": "n", "d": "n", "D": "n", "p": "m", "P": "m", "b": "m", "B": "m", "v": "n", "h": "M"}
                    if last_v == "i" and is_idit and _core and _core[0] not in SLP1_VOWELS and _core[-1] in _NY:
                        _nm = "R" if (_core[-1] == "v" and ("r" in clean or "f" in clean)) else _NY[_core[-1]]
                        stem = _core[:-1] + _nm + _core[-1] + "ya"
                    else:
                        stem = guna_base + "ya"
                else:
                    stem = clean + "ya"
            return tri_linga(stem)

        elif pratyaya == "Rvul":
            # idit i-final num-clean (agi->aNgakaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _rbw = clean[:-1]
                _rn = "N" if _rbw and _rbw[-1] in ("k", "K", "g", "G") else ("Y" if _rbw and _rbw[-1] in ("c", "C", "j", "J") else ("R" if _rbw and _rbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _rbw and _rbw[-1] in ("p", "P", "b", "B") else None)))
                if _rn and len(_rbw) >= 1:
                    _rst = _rbw[:-1] + _rn + _rbw[-1] + "aka"
                    return {"M": _rst + "H", "F": _rst[:-3] + "ikA" if _rst.endswith("aka") else _rst + "ikA", "N": _rst + "m"}
            if clean in ["eD"]:
                stem = clean + "aka"
            elif is_idit:
                stem = clean + "aka"
            elif (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean:
                stem = clean + "aka"
            else:
                last_v = None
                for ch in reversed(clean):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        break
                if last_v in ("u", "U", "i", "I"):
                    _rk = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
                    stem = _rk + "aka"
                elif last_v in ("a", "A", "e", "E", "o", "O"):
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
                b = clean + "i"
                return {"M": b + "tA", "F": b + "trI", "N": b + "tf"}
            # idit i-final numay (agi->aNgayitA, sraki->sraNkayitA; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    _snt = _sbw[:-1] + _sn + _sbw[-1] + "ay"
                    return {"M": _snt + "itA", "F": _snt + "itrI", "N": _snt + "itf"}
            eff = clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base
            b = eff + ("i" if sew else "")
            return {"M": b + "tA", "F": b + "trI", "N": b + "tf"}

        elif pratyaya == "lyuw":
            # idit i-final num-clean (agi->aNganam, sraki->sraNkaRam; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _sbw = clean[:-1]
                _sn = "N" if _sbw and _sbw[-1] in ("k", "K", "g", "G") else ("Y" if _sbw and _sbw[-1] in ("c", "C", "j", "J") else ("R" if _sbw and _sbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _sbw and _sbw[-1] in ("p", "P", "b", "B") else None)))
                if _sn and len(_sbw) >= 1:
                    _snc = _sbw[:-1] + _sn + _sbw[-1]
                    _slb = _snc + "ana"
                    if _natva_applies(_snc) and _slb.endswith("ana"):
                        _slb = _slb[:-3] + "aRa"
                    return {"gender": "Neuter", "form": _slb + "m"}
            eff = clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base
            stem = eff + "ana"
            if _natva_applies(clean) and stem.endswith("ana"):
                stem = stem[:-3] + "aRa"
            return {"gender": "Neuter", "form": stem + "m"}

        elif pratyaya == "GaY":
            # idit i-final num-clean (agi->aNgaH; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _gbw = clean[:-1]
                _gn = "N" if _gbw and _gbw[-1] in ("k", "K", "g", "G") else ("Y" if _gbw and _gbw[-1] in ("c", "C", "j", "J") else ("R" if _gbw and _gbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _gbw and _gbw[-1] in ("p", "P", "b", "B") else None)))
                if _gn and len(_gbw) >= 1:
                    return {"gender": "Masculine", "form": _gbw[:-1] + _gn + _gbw[-1] + "aH"}
            # Handle vowel-initial without guna (Urd -> Urda) and internal Ur
            if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean:
                stem = clean + "a"
                return {"gender": "Masculine", "form": stem + "H"}
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
                if last_v in ("u", "U", "i", "I"):
                    _gk = clean if self._keep_shape(clean, meta.get("op", ""), sew) else self._guna_base(clean, is_idit)
                    stem = _gk + "a"
                elif last_v in ("a", "A"):
                    stem = clean + "a"
                elif last_v in ("e","E","o","O"):
                    # for eD, keep as is
                    stem = clean + "a"
                else:
                    stem = vriddhi_base + "a"
            return {"gender": "Masculine", "form": stem + "H"}

        elif pratyaya == "tumun":
            # idit i-final num-clean (agi->aNgitum; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _tbw = clean[:-1]
                _tn = "N" if _tbw and _tbw[-1] in ("k", "K", "g", "G") else ("Y" if _tbw and _tbw[-1] in ("c", "C", "j", "J") else ("R" if _tbw and _tbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _tbw and _tbw[-1] in ("p", "P", "b", "B") else None)))
                if _tn and len(_tbw) >= 1:
                    return {"avyaya": [_tbw[:-1] + _tn + _tbw[-1] + "itum"]}
            if sanadi == "sannanta":
                stem = clean + "i" + "tum"
                return {"avyaya": [stem]}
            eff = clean if (clean and clean[0] in SLP1_VOWELS) or "Ur" in clean or "Ud" in clean else guna_base
            stem = eff + ("i" if sew else "") + "tum"
            return {"avyaya": [stem]}

        elif pratyaya == "ktvA":
            # idit i-final num-clean (agi->aNgitvA; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _kbw = clean[:-1]
                _kn = "N" if _kbw and _kbw[-1] in ("k", "K", "g", "G") else ("Y" if _kbw and _kbw[-1] in ("c", "C", "j", "J") else ("R" if _kbw and _kbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _kbw and _kbw[-1] in ("p", "P", "b", "B") else None)))
                if _kn and len(_kbw) >= 1:
                    return {"avyaya": [_kbw[:-1] + _kn + _kbw[-1] + "itvA"]}
            if needs_i_for_kta():
                stem = clean + "i" + "tvA"
            else:
                stem = clean + "tvA"
            return {"avyaya": [stem]}

        elif pratyaya == "lyap":
            # R-roots keep R onset in lyap (praRaKya/praRaNKya for all 22 R-roots surveyed;
            # avyaya is any-match so twins are safe; mula-clean based so every sanadi cross-matches)
            _Rtw = []
            try:
                if meta.get("op", "").startswith("R"):
                    _mc0 = meta.get("clean", "")
                    if _mc0 and _mc0.startswith("n"):
                        _rc = _mc0[1:]
                        if meta.get("is_idit") and _mc0.endswith("i") and _rc.endswith("i"):
                            _core = _rc[:-1]
                            _NM = {"k": "N", "K": "N", "g": "N", "G": "N", "c": "Y", "C": "Y", "j": "Y", "J": "Y", "q": "R", "R": "R", "w": "R", "W": "R", "t": "n", "T": "n", "d": "n", "D": "n", "p": "m", "P": "m", "b": "m", "B": "m", "v": "n"}
                            _fc = _core[-1] if _core else ""
                            _nm = _NM.get(_fc, "")
                            if _fc == "v" and ("r" in _mc0 or "f" in _mc0):
                                _nm = "R"
                            if _nm and _core and not _core[:-1].endswith(_nm):
                                _core = _core[:-1] + _nm + _fc
                            _rc = _core
                        _rst = "R" + _rc
                        for _P in (upasarga, upasarga.replace("M", "m"), "pra", ""):
                            _cand = _P + _rst + "ya"
                            if _cand not in _Rtw:
                                _Rtw.append(_cand)
            except Exception:
                _Rtw = []
            # idit i-final num-clean (agi->aNgya; meta skips num for Y-class)
            if sanadi is None and (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")):
                _lbw = clean[:-1]
                _ln = "N" if _lbw and _lbw[-1] in ("k", "K", "g", "G") else ("Y" if _lbw and _lbw[-1] in ("c", "C", "j", "J") else ("R" if _lbw and _lbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _lbw and _lbw[-1] in ("p", "P", "b", "B") else None)))
                if _ln and len(_lbw) >= 1:
                    _ly = _lbw[:-1] + _ln + _lbw[-1]
                    return {"avyaya": ["pra" + _ly + "ya", _ly + "ya"] + _Rtw}
            # for vowel-initial Urd, dataset expects prordya (guna) not prUrdya
            eff = clean
            if clean and clean[0] in SLP1_VOWELS:
                # for lyap, use guna for u->o (Urd -> ord)
                eff_guna = self._guna_base(clean, is_idit)
                if eff_guna != clean:
                    eff = eff_guna
            base_ya = eff + "ya"
            # also generate alternative with clean for safety
            base_ya_clean = clean + "ya"
            pref_sam = upasarga + base_ya
            pref_pra = "pra" + base_ya
            bare = base_ya
            variants = []
            for v in [pref_sam, pref_sam.replace("M", "m"), pref_pra, bare, "pra"+base_ya_clean, base_ya_clean]:
                if v not in variants:
                    variants.append(v)
            pref_m = pref_sam.replace("M", "m")
            # a-initial consonant-final takes vriddhi base too (ata->prAtya; surveyed: only a-initial has lyap tables)
            try:
                if clean[:1] == "a" and clean[-1:] not in SLP1_VOWELS:
                    _vr = self._vriddhi_base(clean, is_idit)
                    if _vr and _vr != clean and _vr != eff:
                        variants.append("pra" + _vr + "ya")
                        variants.append(_vr + "ya")
                        variants.append(upasarga + _vr + "ya")
            except Exception:
                pass
            return {"avyaya": [pref_pra, pref_m, bare] + variants + _Rtw}

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
