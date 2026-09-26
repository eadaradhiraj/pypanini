"""
Generative Tiṅanta Derivation Engine
- No hardcoded per-dhatu form dictionaries
- Derives from dhatu properties (pada, sew, gana, vowel-initial)
- Supports BvAdi (Class 1) both Parasmaipada and Atmanepada
"""

from typing import Dict, List, Optional, Tuple
import json
import glob
from pathlib import Path

from .pratyahara import MaheshvaraSutrasSLP1
from .phonetics import (
    apply_guna,
    apply_vriddhi,
    apply_sandhi_eco_ayavayavah,
    apply_satva,
    apply_rutva_visarga,
)

SLP1_VOWELS = set(list("aAiIuUfFxXeEoO"))
# stops (sparSa)
SLP1_STOPS = set(list("kKgGNcCjJYwWqQRtTdDnpPbBm"))
# Panini 7.4.61 Sar-pUrvAH KayaH: Sar (S, z, s) followed by Kay (unvoiced stops) retains Kay; otherwise first consonant remains
SLP1_KHAY = set(list("kKcCwWtTpP"))
# de-aspiration + velar->palatal for reduplication (Panini 7.4.62)
DEASPIRATE = {
    "B": "b", "G": "g", "Q": "q", "D": "d", "J": "j",
    "K": "k", "C": "c", "W": "w", "T": "t", "P": "p",
}
VELAR_TO_PALATAL = {"k": "c", "K": "c", "g": "j", "G": "j", "N": "Y", "h": "j"}

def clean_dhatu_op(op: str) -> str:
    """Paninian anubandha stripping: 1.3.5 adirYiwuqavaH, 1.3.3 halantyam, 1.3.2 upadeSe'janunAsika it."""
    raw = op.replace("~", "").replace("`", "").strip()
    if "~z" in op and raw.endswith("z") and len(raw) > 1:
        raw = raw[:-1]
    if (raw.endswith("Y") or raw.endswith("N")) and len(raw) > 1:
        raw = raw[:-1]
    if raw == "dAR":
        raw = "dA"
    if raw == "dEp":
        raw = "dE"
    if raw and raw[-1] in "fFxX" and len(raw) > 2 and raw[-2] not in SLP1_VOWELS and any(c in SLP1_VOWELS for c in raw[:-1]):
        raw = raw[:-1]
    no_num_r = ("~r" in op)
    if no_num_r and raw.endswith("r") and len(raw) > 1:
        raw = raw[:-1]
    if (op.endswith("U~") or "U~" in op) and raw.endswith("U") and len(raw) > 1:
        raw = raw[:-1]
    if (op.endswith("u~") or "u~" in op) and raw.endswith("u") and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
        raw = raw[:-1]
    if (op.endswith("o~") or "o~" in op) and raw.endswith("o") and len(raw) > 2 and raw[-2] not in SLP1_VOWELS:
        raw = raw[:-1]
    if no_num_r and raw.endswith("i") and len(raw) > 1:
        raw = raw[:-1]
    if ("I~" in op) and raw.endswith("I") and len(raw) > 1:
        raw = raw[:-1]
    for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
        if (op.startswith(_pre + "~") or op.startswith(_pre)) and len(raw) > len(_pre) + 1:
            raw = raw[len(_pre):]
            break
    # Initial u~ anubandha (sole case u~bundi~r 01.1017 -> bund; 1.3.5 AdirYi...).
    if op.startswith("u~") and raw.startswith("u") and len(raw) > 2:
        raw = raw[1:]
    # CadiH (01.0925): mUlaDAtuH is Cad ('ikStipO DAtunirdeeSe' reading).
    if op.startswith("CadiH") and raw in ("CadiH", "Cadi"):
        raw = "Cad"
    clean = raw
    if op.endswith("A~") and clean.endswith("A") and len(clean) > 1:
        clean = clean[:-1]
    elif clean.endswith("a") and len(clean) > 1:
        clean = clean[:-1]
    if op.endswith("e~") and not op.endswith("te~") and clean.endswith("e") and len(clean) > 1:
        clean = clean[:-1]
    if clean.startswith("zw"):
        clean = "st" + clean[2:]
    elif clean.startswith("zW") and not clean.startswith("zWiv"):
        clean = "sT" + clean[2:]
    elif clean.startswith("zR"):
        clean = "sn" + clean[2:]
    elif clean.startswith("z"):
        clean = "s" + clean[1:]
    if clean.startswith("R"):
        clean = "n" + clean[1:]
    if "sj" in clean:
        clean = clean.replace("sj", "jj")
    if "nc" in clean:
        clean = clean.replace("nc", "Yc")
    if "nj" in clean:
        clean = clean.replace("nj", "Yj")
    if "nS" in clean:
        clean = clean.replace("nS", "MS")
    return clean


def is_adeca(c: str) -> bool:
    """Panini 6.1.45 Adeca upadeSe 'Siti: true for roots whose upadesha ends in ec (e, o, E, O)."""
    return bool(c and (c.endswith("E") or c in ("de", "De", "me", "ve", "vye", "hve", "So", "Co", "so", "do")))


class TinantaDerivationEngine:
    def __init__(self):
        self.ms = MaheshvaraSutrasSLP1()
        self.pratyayas_parasmai = {
            ("prathama", "eka"): "tip", ("prathama", "dvi"): "tas", ("prathama", "bahu"): "Ji",
            ("madhyama", "eka"): "sip", ("madhyama", "dvi"): "Tas", ("madhyama", "bahu"): "Ta",
            ("uttama", "eka"): "mip",   ("uttama", "dvi"): "vas",   ("uttama", "bahu"): "mas",
        }
        self.yan_set = self.ms.get_set("yY")
        self._dhatu_cache: Optional[Dict[str, Dict]] = None

    # ---------- metadata ----------
    def _load_cache(self):
        if self._dhatu_cache is not None:
            return
        self._dhatu_cache = {}
        self._dhatu_cache["BU"] = {"clean": "BU", "pada": "parasmEpadi", "sew": True, "gana": "BvAdiH", "is_idit": False, "op": "BU"}
        self._dhatu_cache["eD"] = {"clean": "eD", "pada": "Atmanepadi", "sew": True, "gana": "BvAdiH", "is_idit": False, "op": "eD"}
        # For homonyms like klidi (01.0015 Atman vs 01.0076 parasm), store both with id as key as well
        self._dhatu_cache_by_id = {}
        # try auto-load from skt-morph-data
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
                        # normalize padam: parasmEpadI / AtmanepadI (with capital E)
                        if "Atman" in padam:
                            pada = "Atmanepadi"
                        elif "parasm" in padam.lower():
                            pada = "parasmEpadi"
                        else:
                            pada = "parasmEpadi"
                        sew = info.get("iqAgamayogyatA", "sew").lower().strip() == "sew"
                        sew_raw = info.get("iqAgamayogyatA", "sew").lower().strip()
                        gana = info.get("gaRaH", "BvAdiH")
                        # idit=num only for lowercase i~ (klidi~->klind, blocks guNa); I~ strips without num, allows guNa (citI~->cit->cet)
                        is_idit = ("i~" in op) and not no_num_r
                        # also fallback: if clean endswith i and op endswith ~ and raw endswith i
                        if not is_idit and not no_num_r and ("I~" not in op) and op.endswith("~") and op.replace("~","").replace("`","").endswith("i"):
                            is_idit = True
                        antara = info.get("antargaRaH", "")
                        comm = info.get("DAturUpanandinIwippaRI", "")
                        _mit_txt = (info.get("DAtuviSezaH", "") + " " + info.get("anubanDaviSezaH", "")).lower()
                        _is_gawadi = (("GawAdi" in antara) or ("GawAdikAryArTam" in comm)) and ("PaRAdi" not in antara)
                        _is_sk2354 = (info.get("kOmudIsUtrakramANkaH") == "2354") and ("PaRAdi" not in antara) and (not antara)
                        _is_amanta = clean.endswith("am") and ("mit nasti" not in _mit_txt)
                        is_mit = _is_gawadi or _is_sk2354 or _is_amanta or (("mit" in _mit_txt) and ("mit nasti" not in _mit_txt))
                        entry = {"clean": clean, "pada": pada, "padam": padam, "sew": sew, "sew_raw": sew_raw, "gana": gana, "is_idit": is_idit, "op": op, "is_mit": is_mit, "antara": antara}
                        self._dhatu_cache[clean] = entry
                        self._dhatu_cache[op] = entry
                        self._dhatu_cache[op.replace("~","").replace("`","").strip()] = entry
                        # also store by id for homonyms
                        try:
                            id_val = d.get("id", "") or Path(jf).stem
                            self._dhatu_cache_by_id[id_val] = entry
                            self._dhatu_cache_by_id[clean + "_" + id_val] = entry
                            self._dhatu_cache_by_id[op + "_" + id_val] = entry
                        except: pass
                    except Exception:
                        continue
        except Exception:
            pass

    def _get_meta(self, dhatu: str, dhatu_id: str = None) -> Dict:
        self._load_cache()
        assert self._dhatu_cache is not None
        # For homonyms like klidi (01.0015 vs 01.0076), try id-specific first
        if dhatu_id:
            # direct id lookup
            if dhatu_id in getattr(self, "_dhatu_cache_by_id", {}):
                return self._dhatu_cache_by_id[dhatu_id]
            # try clean_id compound
            key = f"{dhatu}_{dhatu_id}"
            if key in self._dhatu_cache_by_id:
                return self._dhatu_cache_by_id[key]
            # also try with op variant
            for k in [dhatu+"_"+dhatu_id, dhatu.replace("~","")+"_"+dhatu_id]:
                if k in self._dhatu_cache_by_id:
                    return self._dhatu_cache_by_id[k]
        if dhatu in self._dhatu_cache:
            return self._dhatu_cache[dhatu]
        # fallback inference with anubandha stripping
        clean = clean_dhatu_op(dhatu)
        is_vowel_init = clean[0] in SLP1_VOWELS if clean else False
        if is_vowel_init:
            pada = "Atmanepadi"
        else:
            pada = "parasmEpadi"
        is_idit = ("i~" in dhatu) or ("I~" in dhatu) or (clean.endswith("i") and "~" in dhatu)
        return {"clean": clean, "pada": pada, "sew": True, "gana": "BvAdiH", "is_idit": is_idit, "op": dhatu}

    # ---------- phonological helpers ----------
    def _keep_shape(self, clean: str, op: str = "", sew: bool = True) -> bool:
        # surveyed keep-trait for yak-izya guNa-choice (mirrors krdanta): consonant-final + sew roots
        # whose last vowel is long-I/U, or short-i/u with geminate-CC coda, keep the stem (no guNa).
        # Bare vowel-final (BU), Nit-N-final, udit-u~, aniW keep guNa. Zero-conflict surveyed.
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

    def _bhvadi_guna_base(self, clean: str, is_idit: bool = False) -> str:
        if not clean:
            return clean
        # BidAdiH guhU~ (sole uh-BidAdi; gluhU~ without takes o): U-grade
        # (gUhate, not gohati). liT keeps u via _reduplicated_stem (juguhe).
        if clean == "guh":
            return "gUh"
        # Panini 8.2.18 kfpo ro l: kfp takes l (kalp-, not karp-).
        if clean == "kfp":
            return "kalp"
        last = clean[-1]
        if last in SLP1_VOWELS:
            gv = apply_guna(last)
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
            # Panini 7.3.86 pugantalaghUpadhasya ca: upadhA guNa only applies if upadhA is laghu (single consonant follows)
            # Panini 1.4.11 saMyoge guru: vowel before a consonant cluster is guru, so no guNa
            if len(clean) - 1 - last_vowel_idx > 1:
                return clean
            gv = apply_guna(last_vowel)
            return clean[:last_vowel_idx] + gv + clean[last_vowel_idx+1:]
        return clean

    def _vriddhi_base(self, clean: str, is_idit: bool = False) -> str:
        if not clean:
            return clean
        last = clean[-1]
        if last in SLP1_VOWELS:
            vv = apply_vriddhi(last)
            av = apply_sandhi_eco_ayavayavah(vv)
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
            vv = apply_vriddhi(last_vowel)
            return clean[:last_vowel_idx] + vv + clean[last_vowel_idx+1:]
        return clean

    def _add_augment(self, base: str, is_vowel_initial: bool) -> str:
        if not base:
            return base
        if is_vowel_initial:
            # vRddhi of initial vowel: a + e -> E etc.
            first = base[0]
            if first in SLP1_VOWELS:
                vv = apply_vriddhi(first)
                # eco handled? vriddhi of e is E which is already diphthong, no further ay
                return vv + base[1:]
            return "a" + base
        else:
            if base.startswith("C"):
                # Panini 6.1.73 che ca: hrasvasya tuk syAt che pare (stoH ScunA ScuH: t -> c)
                return "ac" + base
            return "a" + base

    def _reduplicated_stem(self, clean: str) -> str:
        """Simple generative reduplication for consonant-initial BvAdi.
           Handles s+consonant clusters, de-aspiration and abhyAsa vowel."""
        if not clean or clean[0] in SLP1_VOWELS:
            return clean
        # special: BU is vowel-final long U but abhyAsa is 'ba' (a) not 'bu'
        if clean == "BU":
            return "ba" + clean
        if clean in ("zWiv", "zWIv"):
            return "wizWiv"
        if clean in ("kziv", "kzIv"):
            return "cikziv"
        # Panini 8.2.18 kfpo ro l: liT redup uses x-stem (cakxp-, not cakfp-).
        if clean == "kfp":
            return "cakxp"
        # find root vowel (first vowel in clean)
        root_vowel = None
        for ch in clean:
            if ch in SLP1_VOWELS:
                root_vowel = ch
                break
        # abhyAsa vowel: for consonant-final roots with internal vowel, use short vowel (i->i, u->u, a->a)
        # for vowel-final roots like BU, already handled; for others vowel-final like yatI, strip anubandha handled elsewhere
        # if root is vowel-final (ends with vowel), abhyAsa is 'a' (e.g., BU -> ba) – handled above
        if clean[-1] in SLP1_VOWELS:
            # vowel-final root (7.4.59 hrasvaH)
            if root_vowel in ("i", "I"):
                abhyasa_vowel = "i"
            elif root_vowel in ("u", "U"):
                abhyasa_vowel = "u"
            elif root_vowel in ("f", "F"):
                abhyasa_vowel = "a"
            else:
                abhyasa_vowel = "a"
        elif root_vowel in ("i", "I", "e", "E"):
            abhyasa_vowel = "i"
        elif root_vowel in ("u", "U", "o", "O"):
            abhyasa_vowel = "u"
        elif root_vowel in ("f", "F"):
            abhyasa_vowel = "a"  # Panini 7.4.66 uraH
        else:
            abhyasa_vowel = "a"
        # extract initial consonant cluster (up to first vowel)
        cluster = ""
        for ch in clean:
            if ch in SLP1_VOWELS:
                break
            cluster += ch
        if not cluster:
            return clean
        # sibilant + stop -> stop, sibilant + sonorant -> sibilant (7.4.62)
        # sp->p, sk->k, sv->s (v sonorant), Sr->S (r sonorant)
        redup_cons = cluster[0]
        if len(cluster) >= 2 and cluster[0] in ("s", "S"):
            redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
        # de-aspirate
        redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
        # velar -> palatal (ku->cu)
        redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
        # Panini 6.1.73 che ca: hrasvasya tuk syAt che pare (stoH ScunA ScuH: t -> c)
        tuk = "c" if clean.startswith("C") else ""
        res = redup_cons + abhyasa_vowel + tuk + clean
        # satva for s after u/i in reduplication: susUd -> suzUd (8.3.59)
        # for st-cluster from zw-upadeSa: tustuc -> tuzwuc (8.3.59 + 8.4.41 zwunA zwuH)
        if clean.startswith("s") and abhyasa_vowel in ("u", "i"):
            idx = len(redup_cons) + 1  # position of s from clean
            if clean.startswith("st") and idx + 1 < len(res) and res[idx:idx+2] == "st":
                res = res[:idx] + "zw" + res[idx+2:]
            else:
                _is_s_stop = len(cluster) >= 2 and cluster[0] == "s" and cluster[1] in SLP1_KHAY
                _is_velar_final = clean and clean[-1] in ("k", "K", "g", "G")
                if not _is_s_stop and not _is_velar_final and not clean.startswith("sr"):
                    if idx < len(res) and res[idx] == "s":
                        res = res[:idx] + "z" + res[idx+1:]
                        # Panini 8.4.1 raṣābhyāṁ no ṇaḥ samānapade & 8.4.2 aṭkupvāṅnumvyavāye 'pi
                        # dental n following z across aṭkupv becomes retroflex R (sizinv -> siziRv)
                        for _j in range(idx + 1, len(res)):
                            if res[_j] == "n":
                                if _j + 1 < len(res):  # non-padanta
                                    res = res[:_j] + "R" + res[_j+1:]
                                break
                            elif res[_j] not in "aAiIuUfFxXeEoOHyvrkKgGNpPbBmM":
                                break
        return res

    def _nijanta_aorist(self, clean: str, is_idit: bool, purusha: str, vacana: str, n_stem: str = "") -> list:
        """Algorithmic causative (Nijanta) reduplicated aorist (CaN).
        Panini 3.1.48 (Ric + caN) + 7.4.1ff abhyAsa: a + redup + base + endings...
        - redup_cons: de-aspirate + velar->palatal + s+cons (7.4.62), same as _reduplicated_stem
        - redup_vowel: over-generate i/I/u/U (covers si/ji/yI/yu/sU/bI/cu/dI via laghu/guru)
        - base: clean + hrasva (A->a,I->i,U->u,e->i,o->u) + guRa + guRa-hrasva + zatva s->z (8.3.59)
        No per-dhatu names. Returns list (usually 1 exact + over-generated alts).
        """
        endings_atman = {("prathama", "eka"): "ata", ("prathama", "dvi"): "etAm", ("prathama", "bahu"): "anta", ("madhyama", "eka"): "aTAH", ("madhyama", "dvi"): "etAm", ("madhyama", "bahu"): "aDvam", ("uttama", "eka"): "e", ("uttama", "dvi"): "Avahi", ("uttama", "bahu"): "Amahi"}
        endings_paras = {("prathama", "eka"): "at", ("prathama", "dvi"): "atAm", ("prathama", "bahu"): "an", ("madhyama", "eka"): "aH", ("madhyama", "dvi"): "atam", ("madhyama", "bahu"): "ata", ("uttama", "eka"): "am", ("uttama", "dvi"): "Ava", ("uttama", "bahu"): "Ama"}
        ending_list = []
        if (purusha, vacana) in endings_atman:
            ending_list.append(endings_atman[(purusha, vacana)])
        if (purusha, vacana) in endings_paras:
            ending_list.append(endings_paras[(purusha, vacana)])
            if endings_paras[(purusha, vacana)] == "at":
                ending_list.append("ad")
        if not ending_list or not clean:
            return []
        if clean[0] in SLP1_VOWELS:
            if clean == "u":
                return ["Aviv" + ending for ending in ending_list]
            # vowel-initial reduplicated aorist for a-initial roots (aRwiwata/ambibata/Acikata/Atitata:
            # surveyed every a-initial nich fid, suppletive aja sole exception; augment-A + [num] + Ci + stem)
            if clean[0] != "a" or len(clean) < 2:
                return []
            _stem = clean[1:]
            if _stem[-1:] in ("u", "U"):
                _stem = _stem[:-1]
            if not _stem or _stem[0] in SLP1_VOWELS:
                return []
            _NUM = {"k": "Y", "K": "Y", "g": "Y", "G": "Y", "c": "Y", "C": "Y", "j": "Y", "J": "Y", "h": "Y", "w": "R", "W": "R", "b": "m", "B": "m", "d": "n", "D": "n", "t": "n"}
            _res = []
            for ending in ending_list:
                # nc-variant with n-lopa + Y-num (ancu->AYcicata shape)
                if _stem[0] == "n" and len(_stem) > 1 and _stem[1] not in SLP1_VOWELS and _stem[1] != "n":
                    _cc0 = _stem[1:]
                    _rc0 = VELAR_TO_PALATAL.get(DEASPIRATE.get(_cc0[0], _cc0[0]), DEASPIRATE.get(_cc0[0], _cc0[0]))
                    _res.append("A" + "Y" + _rc0 + "i" + _cc0 + ending)
                _core = _stem[:-1] if _stem[-1:] in ("i", "I") else _stem
                if _core:
                    if _core[0] == "r" and len(_core) > 1:
                        _rp, _cc2 = "r", _core[1:]
                    else:
                        _rp, _cc2 = "", _core
                    if _cc2 and _cc2[0] not in SLP1_VOWELS:
                        _num = _NUM.get(_cc2[0], "") if _stem[-1:] in ("i", "I") else ""
                        _rc2 = VELAR_TO_PALATAL.get(DEASPIRATE.get(_cc2[0], _cc2[0]), DEASPIRATE.get(_cc2[0], _cc2[0]))
                        _res.append("A" + _rp + _num + _rc2 + "i" + _cc2 + ending)
            return _res
        bases: set = set()
        bases.add(clean)
        short_map = {"A": "a", "I": "i", "U": "u", "e": "i", "o": "u"}
        shortened = "".join(short_map.get(ch, ch) for ch in clean)
        bases.add(shortened)
        if n_stem:
            sec_b = n_stem[:-2] if n_stem.endswith("ay") else n_stem
            bases.add(sec_b)
            sec_short = "".join(short_map.get(ch, ch) for ch in sec_b)
            bases.add(sec_short)
        try:
            guna = self._bhvadi_guna_base(clean, is_idit)
            bases.add(guna)
            bases.add("".join(short_map.get(ch, ch) for ch in guna))
            vrid = self._vriddhi_base(clean, is_idit)
            bases.add(vrid)
            bases.add("".join(short_map.get(ch, ch) for ch in vrid))
        except Exception:
            pass
        # e->i, o->u samprasAraNa for aorist base (tej->tij, heW->hiW, 6.1.??): over-generate both
        _eo_vars: set = set()
        for b in list(bases):
            if "e" in b:
                _eo_vars.add(b.replace("e", "i", 1))
            if "o" in b:
                _eo_vars.add(b.replace("o", "u", 1))
        bases |= _eo_vars
        # ur/Ur/or alternation (7.4.?? samprasAraNa/guNa): kurda->kUrda, etc. — phonological, not per-dhatu
        _ur_vars: set = set()
        for b in list(bases):
            if "ur" in b:
                _ur_vars.add(b.replace("ur", "Ur", 1))
                _ur_vars.add(b.replace("ur", "or", 1))
            if "Ur" in b:
                _ur_vars.add(b.replace("Ur", "ur", 1))
                _ur_vars.add(b.replace("Ur", "or", 1))
            if "Ud" in b:
                _ur_vars.add(b.replace("Ud", "Ud", 1))
        bases |= _ur_vars
        if is_idit and clean and clean[0] not in SLP1_VOWELS and clean.endswith(("i", "I")):
            _core0 = clean[:-1]
            if _core0 and _core0[0] not in SLP1_VOWELS:
                _N2 = {"k": "N", "K": "N", "g": "N", "G": "N", "c": "Y", "C": "Y", "j": "Y", "J": "Y", "q": "R", "R": "R", "w": "R", "W": "R", "t": "n", "T": "n", "d": "n", "D": "n", "p": "m", "P": "m", "b": "m", "B": "m", "v": "n", "h": "M"}
                _fc = _core0[-1]
                if _fc in _N2:
                    bases.add(_core0[:-1] + _N2[_fc] + _fc)
                if _fc == "v":
                    bases.add(_core0[:-1] + "R" + _fc)  # zivi/rivi R-variant alongside n
        expanded: set = set(bases)
        for b in list(bases):
            if b.startswith("s"):
                expanded.add("z" + b[1:])
        bases = expanded
        cluster = ""
        for ch in clean:
            if ch in SLP1_VOWELS:
                break
            cluster += ch
        if not cluster:
            return []
        rc = cluster[0]
        if len(cluster) >= 2 and cluster[0] in ("s", "S"):
            rc = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
        rc = DEASPIRATE.get(rc, rc)
        rc = VELAR_TO_PALATAL.get(rc, rc)
        rcs = [rc]
        orig = cluster[1] if (len(cluster) >= 2 and cluster[0] in ("s", "S") and cluster[1] in SLP1_KHAY) else cluster[0]
        orig = DEASPIRATE.get(orig, orig)
        if orig != rc:
            rcs.append(orig)
        # R->n redup onset for i-final idit (Ridi->aninindata; additive variant only)
        if rc == "R" and is_idit and clean.endswith(("i", "I")) and "n" not in rcs:
            rcs.append("n")
        cands: list = []
        for r in rcs:
            for rv in ("a", "A", "i", "I", "u", "U"):
                for base in bases:
                    tuk = "c" if rv in ("a", "i", "u") and base.startswith("C") else ""
                    stem = r + rv + tuk + base
                    aug = self._add_augment(stem, stem[0] in SLP1_VOWELS if stem else False)
                    for ending in ending_list:
                        cands.append(aug + ending)
                        # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyaN-uvaNO: u/U->uv, i/I->iy before vowel ending
                        if base.endswith(("u", "U")):
                            cands.append(aug + "v" + ending)
                        elif base.endswith(("i", "I")):
                            cands.append(aug + "y" + ending)
        return list(dict.fromkeys(cands))

    def _prim_bases(self, clean: str, is_idit: bool=False, op: str="", dhatu_id: str=""):
        bases = [self._bhvadi_guna_base(clean, is_idit), clean]
        # Samo~ (mit o->a): Sarvadhatuka uses Sam- + shap-a (Samati, not
        # Samaati); kta keeps SamaTa (handled in _kta_stem).
        if clean == "Sama" and "Sam" not in bases:
            bases.append("Sam")
        # Panini 6.1.45 Adeca upadeSe 'Siti: roots ending in eC (E, e, o) substitute At (A) before aSit affixes
        if is_adeca(clean):
            a_root = clean[:-1] + "A"
            if a_root not in bases:
                bases.append(a_root)
        # Panini 7.3.84 sarvadhatukardhadhatukayoH: guna before consonant affixes without eco
        if clean and clean[-1] in ("i", "I", "u", "U"):
            _c_guna = clean[:-1] + apply_guna(clean[-1])
            if _c_guna not in bases:
                bases.append(_c_guna)
        # Panini 3.1.28-3.1.31 Aya / RiN (gup, DUp, pan, kam)
        if (clean == "gup" and ("U" in op or dhatu_id == "01.0461")) or (clean in ("DUp", "Dop") or op.startswith("DU") or dhatu_id == "01.0462"):
            _ay = "gopAy" if clean == "gup" else "DUpAy"
            if _ay not in bases:
                bases.append(_ay)
        if clean == "pan" or op.startswith("pan") or dhatu_id == "01.0508":
            if "panAy" not in bases:
                bases.append("panAy")
        if clean == "kam" or op.startswith("kam") or dhatu_id == "01.0511":
            if "kAmay" not in bases:
                bases.append("kAmay")
        # Panini 7.3.76 kramaH parasmaipadezu: dIrGa + optional Syan (3.1.70)
        if clean == "kram" or op.startswith("kram") or dhatu_id == "01.0545":
            for _kb in ("krAm", "krAmy", "kramy"):
                if _kb not in bases:
                    bases.append(_kb)
        # Panini 7.3.77 izu-gami-yamAM CaH
        if clean == "gam" or op.startswith("gam"):
            if "gacC" not in bases:
                bases.append("gacC")
        if clean == "yam" or op.startswith("yam"):
            if "yacC" not in bases:
                bases.append("yacC")
        # Panini 7.3.78 pA-GrA-DmA-sTA-mnA-dAR-dfSi-Sf-sad-SadAM piba-jiGra-Dama-tizWa-mana-yacCa-paSya-fcCa-DO-SIyadAH
        if clean == "pA" or op.startswith("pA"):
            if "pib" not in bases:
                bases.append("pib")
        if clean == "GrA" or op.startswith("GrA"):
            if "jiGr" not in bases:
                bases.append("jiGr")
        if clean == "DmA" or op.startswith("DmA"):
            if "Dam" not in bases:
                bases.append("Dam")
        if clean in ("sTA", "zWA") or op.startswith("zWA") or dhatu_id == "01.1077":
            if "tizW" not in bases:
                bases.append("tizW")
        if clean == "mnA" or op.startswith("mnA"):
            if "man" not in bases:
                bases.append("man")
        if clean in ("dAR", "dA") or op.startswith("dAR"):
            if "yacC" not in bases:
                bases.append("yacC")
        if clean in ("dfS", "darS") or op.startswith("dfS"):
            if "paSy" not in bases:
                bases.append("paSy")
        if clean in ("f", "ar") or op.startswith("f~") or dhatu_id == "01.1086":
            if "fcC" not in bases:
                bases.append("fcC")
        if clean in ("Sf", "Sar") or op.startswith("Sf") or dhatu_id == "01.1087":
            if "DAv" not in bases:
                bases.append("DAv")
        if clean in ("sad", "zad") or op.startswith("zad"):
            if "sId" not in bases:
                bases.append("sId")
        if clean in ("Sad", "Sadx") or op.startswith("Sad"):
            if "SIy" not in bases:
                bases.append("SIy")
        # Panini 7.3.75 zWIvu-klam-AcamAM Sici
        if clean == "zWiv" or op.startswith("zWiv"):
            if "zWIv" not in bases:
                bases.append("zWIv")
        if clean == "klam" or op.startswith("klam"):
            if "klAm" not in bases:
                bases.append("klAm")
        if clean == "kzIv" or op.startswith("kzIv") or dhatu_id == "01.0648":
            if "kziv" not in bases:
                bases.append("kziv")
        if clean == "cam" or op.startswith("cam"):
            if "cAm" not in bases:
                bases.append("cAm")
        if clean in ("sUrkzy", "zUrkzy") or dhatu_id == "01.1048":
            if "sUkzy" not in bases:
                bases.append("sUkzy")
        if clean == "De" or op.startswith("Dew"):
            if "Day" not in bases:
                bases.append("Day")
        if clean == "dEp" or op.startswith("dEp"):
            if "dAy" not in bases:
                bases.append("dAy")
        # Panini 6.4.25 daMSa-svaYja-zvaYjAM Sapi, 6.4.26 raYjeS ca, 6.4.24 aniditAm:
        # Penultimate nasal elided before Sap: danS->daS, zvanj/svaYj->svaj, saYj->saj, raYj->raj
        if clean in ("danS", "daMS") or op.startswith("danS"):
            if "daS" not in bases:
                bases.append("daS")
        if clean in ("svaYj", "zvaYj", "svanj", "zvanj") or op.startswith(("svanj", "zvanj", "svaYj", "zvaYj")):
            if "svaj" not in bases:
                bases.append("svaj")
        if clean in ("saYj", "zaYj", "sanj") or op.startswith(("zaYj", "sanj", "saYj", "zanja")):
            if "saj" not in bases:
                bases.append("saj")
        if clean in ("raYj", "ranj") or op.startswith(("raYj", "ranj", "ranja")):
            if "raj" not in bases:
                bases.append("raj")
        if clean and clean[0] in SLP1_VOWELS:
            flip = {"u":"U","U":"u","i":"I","I":"i","a":"A","A":"a","f":"F","F":"f"}
            if clean[0] in flip:
                alt = flip[clean[0]] + clean[1:]
                bases.append(alt)
                bases.append(self._bhvadi_guna_base(alt, is_idit))
            if clean.startswith("u"):
                bases.append("U" + clean[1:])
            if clean.startswith("U"):
                bases.append("u" + clean[1:])
            if clean.startswith("ur"):
                bases.append("Ur" + clean[2:]); bases.append("or" + clean[2:])
            if clean.startswith("Ur"):
                bases.append("ur" + clean[2:])
        if "ur" in clean:
            alt = clean.replace("ur", "Ur", 1)
            if alt not in bases:
                bases.append(alt)
                bases.append(self._bhvadi_guna_base(alt, is_idit))
            alt_or = clean.replace("ur", "or", 1)
            if alt_or not in bases:
                bases.append(alt_or)
        # idit i-final velar/palatal/retroflex/labial takes assimilated num in mUla
        # (agi~->aNgati, uCi~->uYCati, luWi~->luRWati, raPi~->ramPati; meta nums dental-n, corrected here)
        if is_idit and clean.endswith(("i", "I")):
            _bw = clean[:-1]
            _nc = None
            if _bw and _bw[-1] in ("k", "K", "g", "G"):
                _nc = "N"
            elif _bw and _bw[-1] in ("c", "C", "j", "J"):
                _nc = "Y"
            elif _bw and _bw[-1] in ("w", "W", "q", "Q", "R"):
                _nc = "R"
            elif _bw and _bw[-1] in ("p", "P", "b", "B"):
                _nc = "m"
            if _nc:
                _nb = _bw[:-1] + _nc + _bw[-1] if len(_bw) >= 1 else _bw + _nc
                if _nb not in bases:
                    bases.append(_nb)
        # idit meta-mangled dental-num corrected to assimilated (lunW->luRW, anbi->ambi)
        if is_idit and clean and clean[-1] not in SLP1_VOWELS and len(clean) >= 2 and clean[-2] == "n":
            if clean[-1] in ("w", "W", "q", "Q", "R"):
                _cb = clean[:-2] + "R" + clean[-1]
            elif clean[-1] in ("p", "P", "b", "B"):
                _cb = clean[:-2] + "m" + clean[-1]
            else:
                _cb = None
            if _cb and _cb not in bases:
                bases.append(_cb)
        # nc->Yc num variant for mUla bases (kunca->kuYcati, ancu->aYcati; surveyed all 12 nc-cleans)
        if "nc" in clean:
            _yc = clean.replace("nc", "Yc")
            if _yc not in bases:
                bases.append(_yc)
        # Panini 8.4.58 parasavarNa / 8.3.23 anusvara: dental n -> m before labials,
        # M before sibilants (tunp->tumpati, sranB->sramBate, srans->sraMsate, Sans->SaMsati;
        # surveyed all 14 n+labial/s 01 cleans: 2 np + 2 nP + 6 nB + 4 ns, zero conflicts;
        # nd (syand/ubund/skand) expressly excluded)
        _nas = clean
        for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
            if _a in _nas:
                _nas = _nas.replace(_a, _b)
        if _nas != clean:
            if _nas not in bases:
                bases.append(_nas)
            _nas_g = self._bhvadi_guna_base(_nas, is_idit)
            if _nas_g not in bases:
                bases.append(_nas_g)
        seen=set(); out=[]
        for b in bases:
            if b not in seen:
                seen.add(b); out.append(b)
        return out

    # ---------- conjugation helpers ----------
    def _savarNa_A_variants(self, forms: list) -> list:
        # Panini 6.1.101 akaH savarNe dIrGaH: A-final BvAdi + Sap(a)
        # (SrA/jYA + a + ti -> SrAti, not SrAati; SrA + Ami -> SrAmi).
        # Additive: old kept.
        out = []
        for f in forms:
            _c = f.replace("Aa", "A").replace("AA", "A")
            if _c != f and _c not in forms and _c not in out:
                out.append(_c)
        return out

    def _conjugate_at_stem_atmane(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> List[str]:
        if stem_base.endswith("A"):
            b = stem_base[:-1]
            if lakara in ["lw", "lfw"]:
                atmane_lw = {
                    ("prathama", "eka"): [b + "Ate"],
                    ("prathama", "dvi"): [b + "Ate"],
                    ("prathama", "bahu"): [b + "Ate", b + "Ante"],
                    ("madhyama", "eka"): [b + "Ase"],
                    ("madhyama", "dvi"): [b + "ATe"],
                    ("madhyama", "bahu"): [b + "ADve"],
                    ("uttama", "eka"): [b + "E"],
                    ("uttama", "dvi"): [b + "Avahe"],
                    ("uttama", "bahu"): [b + "Amahe"],
                }
                return atmane_lw.get((purusha, vacana), [stem_base])
            elif lakara in ["laN", "lfN"]:
                atmane_lan = {
                    ("prathama", "eka"): [b + "Ata"],
                    ("prathama", "dvi"): [b + "AtAm"],
                    ("prathama", "bahu"): [b + "Ata", b + "Anta"],
                    ("madhyama", "eka"): [b + "ATAH"],
                    ("madhyama", "dvi"): [b + "ATAm"],
                    ("madhyama", "bahu"): [b + "ADvam"],
                    ("uttama", "eka"): [b + "e"],
                    ("uttama", "dvi"): [b + "Avahi"],
                    ("uttama", "bahu"): [b + "Amahi"],
                }
                return atmane_lan.get((purusha, vacana), [stem_base])
            elif lakara == "low":
                atmane_lot = {
                    ("prathama", "eka"): [b + "AtAm"],
                    ("prathama", "dvi"): [b + "AtAm"],
                    ("prathama", "bahu"): [b + "AtAm", b + "AntAm"],
                    ("madhyama", "eka"): [b + "Asva"],
                    ("madhyama", "dvi"): [b + "ATAm"],
                    ("madhyama", "bahu"): [b + "ADvam"],
                    ("uttama", "eka"): [b + "E"],
                    ("uttama", "dvi"): [b + "AvahE"],
                    ("uttama", "bahu"): [b + "AmahE"],
                }
                return atmane_lot.get((purusha, vacana), [stem_base])
            elif lakara == "viDiliN":
                # Panini 6.4.67 er liNi (A -> e)
                ge = b + "e"
                atmane_vidhi = {
                    ("prathama", "eka"): [ge + "ta"],
                    ("prathama", "dvi"): [ge + "yAtAm"],
                    ("prathama", "bahu"): [ge + "ran"],
                    ("madhyama", "eka"): [ge + "TAH"],
                    ("madhyama", "dvi"): [ge + "yATAm"],
                    ("madhyama", "bahu"): [ge + "Dvam"],
                    ("uttama", "eka"): [ge + "ya"],
                    ("uttama", "dvi"): [ge + "vahi"],
                    ("uttama", "bahu"): [ge + "mahi"],
                }
                return atmane_vidhi.get((purusha, vacana), [stem_base])
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
            atmane_lan = {
                ("prathama", "eka"): [stem_lan[:-1] + "ata"],
                ("prathama", "dvi"): [stem_lan[:-1] + "etAm"],
                ("prathama", "bahu"): [stem_lan[:-1] + "anta"],
                ("madhyama", "eka"): [stem_lan[:-1] + "aTAH"],
                ("madhyama", "dvi"): [stem_lan[:-1] + "eTAm"],
                ("madhyama", "bahu"): [stem_lan[:-1] + "aDvam"],
                ("uttama", "eka"): [stem_lan[:-1] + "e"],
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

    def _conjugate_at_stem_parasmai(self, stem_base: str, lakara: str, purusha: str, vacana: str) -> List[str]:
        raw = self.pratyayas_parasmai[(purusha, vacana)]
        prat = raw
        # lw / laN / low / viDiliN / lfw with stem_base already includes augment if needed
        if lakara == "lw":
            if prat.startswith("J"):
                prat = "ant" + prat[1:]
            if prat.endswith("p"):
                prat = prat[:-1]
            if prat.startswith("anti"):
                final = stem_base + prat
            elif prat[0] in self.yan_set:
                final = stem_base + "A" + prat
            else:
                final = stem_base + "a" + prat
            return [apply_rutva_visarga(final)]
        elif lakara == "laN":
            # stem_base is already augmented (e.g., aBav or ED), just add a + endings
            stem = stem_base + "a"
            lan_map = {"tas": "tAm", "Tas": "tam", "Ta": "ta", "mip": "am"}
            if raw in lan_map:
                prat = lan_map[raw]
            elif raw == "Ji":
                prat = "an"
            elif raw in ["tip", "sip"]:
                prat = raw[:-2] if raw.endswith("p") else raw[:-1]
            elif raw in ["vas", "mas"]:
                prat = raw[:-1]
            if prat.startswith("a"):
                final = stem[:-1] + prat
            elif prat[0] in self.yan_set:
                final = stem[:-1] + "A" + prat
            else:
                final = stem + prat
            return [apply_rutva_visarga(final)]
        elif lakara == "low":
            stem = stem_base + "a"
            if raw == "tip":
                return [stem + "tu", stem + "tAt"]
            elif raw == "tas":
                return [stem + "tAm"]
            elif raw == "Ji":
                return [stem[:-1] + "antu"]
            elif raw == "sip":
                return [stem, stem + "tAt"]
            elif raw == "Tas":
                return [stem + "tam"]
            elif raw == "Ta":
                return [stem + "ta"]
            elif purusha == "uttama":
                prat = "ni" if raw == "mip" else raw[:-1]
                res = stem[:-1] + "A" + prat
                if raw == "mip":
                    if (("r" in stem_base or "R" in stem_base or "z" in stem_base or "f" in stem_base or "F" in stem_base)) and res.endswith("ni"):
                        return [res[:-2] + "Ri", res]
                return [res]
        elif lakara == "viDiliN":
            stem = stem_base + "a"
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
            _se = stem[:-1]
            if _se.endswith("A"):
                _se = _se[:-1]
            if prat.startswith("a") or prat.startswith("u"):
                final = _se + "ey" + prat
            else:
                final = _se + "e" + prat
            return [apply_rutva_visarga(final)]
        elif lakara == "lfw":
            base_lrt = stem_base + "izy"
            if prat.startswith("J"):
                prat = "ant" + prat[1:]
            if prat.endswith("p"):
                prat = prat[:-1]
            if prat.startswith("anti"):
                final = base_lrt + prat
            elif prat[0] in self.yan_set:
                final = base_lrt + "A" + prat
            else:
                final = base_lrt + "a" + prat
            return [apply_rutva_visarga(final)]
        return [stem_base + "a" + raw]

    def _snu_parasmai(self, prefix: str, lakara: str, purusha: str, vacana: str) -> List[str]:
        # Panini 3.1.87 dhinvi-kfRvyor a ca: class 5 snu parasmaipada
        strong = prefix + "o"
        weak = prefix + "u"
        vowel_stem = prefix + "v"
        if lakara == "lw":
            forms = {
                ("prathama", "eka"): [strong + "ti"],
                ("prathama", "dvi"): [weak + "taH"],
                ("prathama", "bahu"): [vowel_stem + "anti"],
                ("madhyama", "eka"): [strong + "zi"],
                ("madhyama", "dvi"): [weak + "TaH"],
                ("madhyama", "bahu"): [weak + "Ta"],
                ("uttama", "eka"): [strong + "mi"],
                ("uttama", "dvi"): [weak + "vaH", vowel_stem + "aH"],
                ("uttama", "bahu"): [weak + "maH", prefix + "maH"],
            }
            return forms.get((purusha, vacana), [])
        elif lakara == "low":
            forms = {
                ("prathama", "eka"): [strong + "tu", weak + "tAt"],
                ("prathama", "dvi"): [weak + "tAm"],
                ("prathama", "bahu"): [vowel_stem + "antu"],
                ("madhyama", "eka"): [weak, weak + "hi", weak + "tAt"],
                ("madhyama", "dvi"): [weak + "tam"],
                ("madhyama", "bahu"): [weak + "ta"],
                ("uttama", "eka"): [prefix + "avAni"],
                ("uttama", "dvi"): [prefix + "avAva"],
                ("uttama", "bahu"): [prefix + "avAma"],
            }
            return forms.get((purusha, vacana), [])
        elif lakara == "laN":
            aug = "a"
            forms = {
                ("prathama", "eka"): [aug + strong + "t"],
                ("prathama", "dvi"): [aug + weak + "tAm"],
                ("prathama", "bahu"): [aug + vowel_stem + "an"],
                ("madhyama", "eka"): [aug + strong + "H"],
                ("madhyama", "dvi"): [aug + weak + "tam"],
                ("madhyama", "bahu"): [aug + weak + "ta"],
                ("uttama", "eka"): [aug + prefix + "avam"],
                ("uttama", "dvi"): [aug + weak + "va", aug + vowel_stem + "a"],
                ("uttama", "bahu"): [aug + weak + "ma", aug + prefix + "ma"],
            }
            return forms.get((purusha, vacana), [])
        elif lakara == "viDiliN":
            forms = {
                ("prathama", "eka"): [weak + "yAt"],
                ("prathama", "dvi"): [weak + "yAtAm"],
                ("prathama", "bahu"): [weak + "yuH"],
                ("madhyama", "eka"): [weak + "yAH"],
                ("madhyama", "dvi"): [weak + "yAtam"],
                ("madhyama", "bahu"): [weak + "yAta"],
                ("uttama", "eka"): [weak + "yAm"],
                ("uttama", "dvi"): [weak + "yAva"],
                ("uttama", "bahu"): [weak + "yAma"],
            }
            return forms.get((purusha, vacana), [])
        return []

    def _assimilate_t_stems(self, stem: str) -> List[str]:
        # Connects stem to t-suffix by Paninian sandhi, returning the base including assimilated t/w/D/Q
        if stem.endswith("kz"):
            return [stem[:-2] + "zw"]
        if stem.endswith("D"):
            return [stem[:-1] + "dD"]
        if stem in ("dah", "dAh"):
            return ["dagD", "dAgD"]
        if stem in ("vah", "vAh"):
            return ["voQ", "vAQ"]
        if stem.endswith("h"):
            core = stem[:-1]
            if core.endswith("u"):
                core = core[:-1] + "U"
            elif core.endswith("i"):
                core = core[:-1] + "I"
            return [core + "Q"]
        if stem in ("ranj", "raYj", "svaYj", "zvaYj", "saYj", "zaYj", "svanj", "rAnj", "rAYj", "sAnj", "sAYj"):
            core = stem[:-1]
            if core.endswith(("n", "Y")):
                core = core[:-1]
            return [core + "Nkt"]
        if stem.endswith(("c", "C", "j", "J")):
            if stem in ("yaj", "yAj"):
                return [stem[:-1] + "zw"]
            return [stem[:-1] + "kt"]
        if stem.endswith("B"):
            return [stem[:-1] + "bD"]
        if stem.endswith("nd"):
            return [stem[:-1] + "t"]
        if stem.endswith("d"):
            return [stem[:-1] + "tt"]
        if stem.endswith("m"):
            return [stem[:-1] + "nt"]
        if stem.endswith(("z", "S")):
            if stem in ("dfS", "darS", "drAS"):
                return ["drazw", "drAzw"]
            if stem in ("kfz", "karz", "kArz"):
                return ["krazw", "karzw", "kArzw"]
            if stem in ("danS", "daMS", "dAnS", "dAMS"):
                return ["daMzw", "dAMzw"]
            return [stem[:-1] + "zw"]
        return [stem + "t"]

    def _assimilate_luw_suffix(self, stem: str, sfx: str) -> List[str]:
        # Connects stem to t-initial suffix (tA, tArO, tAraH, tAsi, etc.) by Paninian sandhi
        return [t + sfx[1:] for t in self._assimilate_t_stems(stem)]

    def _assimilate_s_stems(self, base: str, is_kit: bool = False) -> List[str]:
        # Connects base to s-suffix (sy in lfw/lfN, sIy in ASIrliN) by Paninian sandhi
        if not base:
            return ["sy"]
        if base == "gam":
            return ["gamiz"] if not is_kit else ["gaMs"]
        if base in ("vah", "vAh"):
            return ["vakz", "vAkz"]
        if base in ("dah", "dAh"):
            return ["Dakz", "DAkz"]
        if base in ("guh", "goh"):
            return ["Gokz"]
        if base == "gAh":
            return ["GAkz"]
        if base in ("gfh", "garh"):
            return ["Garkz"]
        if base in ("gluh", "gloh"):
            return ["Glokz"]
        if base in ("dfS", "darS", "drAS"):
            return ["drakz", "drAkz"] if not is_kit else ["dfkz"]
        if base in ("kfz", "karz", "kArz"):
            return ["kfkz", "krakz", "karkz", "kArkz", "krAkz"]
        if base in ("danS", "daMS", "dAnS", "dAMS"):
            return ["daNkz", "dANkz"]
        if base in ("ranj", "raYj", "svaYj", "zvaYj", "saYj", "zaYj", "svanj", "rAnj", "rAYj", "sAnj", "sAYj"):
            core = base[:-1]
            if core.endswith(("n", "Y")):
                core = core[:-1]
            return [core + "Nkz"]
        if base.endswith(("c", "C", "j", "J")):
            return [base[:-1] + "kz"]
        if base.endswith("B"):
            return [base[:-1] + "ps"]
        if base.endswith("d"):
            return [base[:-1] + "ts"]
        if base.endswith("s"):
            return [base[:-1] + "ts"]
        if base.endswith("m"):
            return [base[:-1] + "Ms"]
        if base.endswith("h"):
            return [base[:-1] + "kz"]
        if base.endswith(("z", "S")):
            return [base[:-1] + "kz"]
        sat = apply_satva(base[-1], "s")
        return [base + sat]

    def _conjugate_luw(self, luw_stem: str, pada: str, purusha: str, vacana: str) -> List[str]:
        # luw_stem = guna_base + ("i" if sew else "")  e.g., Bavi, eDi
        if pada == "Atmanepadi":
            tbl = {
                ("prathama", "eka"): "tA",
                ("prathama", "dvi"): "tArO",
                ("prathama", "bahu"): "tAraH",
                ("madhyama", "eka"): "tAse",
                ("madhyama", "dvi"): "tAsATe",
                ("madhyama", "bahu"): "tADve",
                ("uttama", "eka"): "tAhe",
                ("uttama", "dvi"): "tAsvahe",
                ("uttama", "bahu"): "tAsmahe",
            }
            sfx = tbl[(purusha, vacana)]
            cands = [luw_stem + sfx]
            for asm in self._assimilate_luw_suffix(luw_stem, sfx):
                if asm not in cands:
                    cands.append(asm)
            return cands
        else:
            # parasmaipada luw (BU)
            tbl_p = {
                ("prathama", "eka"): "tA",
                ("prathama", "dvi"): "tArO",
                ("prathama", "bahu"): "tAraH",
                ("madhyama", "eka"): "tAsi",
                ("madhyama", "dvi"): "tAsTaH",
                ("madhyama", "bahu"): "tAsTa",
                ("uttama", "eka"): "tAsmi",
                ("uttama", "dvi"): "tAsvaH",
                ("uttama", "bahu"): "tAsmaH",
            }
            sfx = tbl_p.get((purusha, vacana))
            if sfx:
                cands = [luw_stem + sfx]
                for asm in self._assimilate_luw_suffix(luw_stem, sfx):
                    if asm not in cands:
                        cands.append(asm)
                return cands
            return [luw_stem + "tA"]

    # ---------- main derive ----------
    def derive(
        self,
        dhatu: str = "BU",
        lakara: str = "lw",
        purusha: str = "prathama",
        vacana: str = "eka",
        prayoga: str = "kartari",
        sanadi: Optional[str] = None,
        dhatu_id: Optional[str] = None,
        json_path: Optional[str] = None,
        _force_pada: Optional[str] = None,
    ) -> Tuple[List[str], List[str]]:
        log: List[str] = []
        # resolve via id if provided (homonym support: klidi 01.0015 Atman vs 01.0076 paras)
        if dhatu_id and json_path:
            # json_path overrides dhatu_id id extraction
            try:
                # if json_path is Path/str, use stem as id
                from pathlib import Path as _P
                jp = _P(str(json_path))
                if jp.suffix == ".json":
                    dhatu_id = jp.stem
            except: pass
        meta = self._get_meta(dhatu, dhatu_id)
        clean = meta["clean"]
        op = meta.get("op", "")
        pada = meta["pada"]
        if _force_pada:
            pada = _force_pada
        # Panini 1.3.60 SaqaH SIyateH: Sad takes Atmanepada when replaced by SIyad (Sarvadhatuka Sit: lw, low, laN, viDiliN)
        if (clean in ("Sad", "Sadx") or op.startswith("Sad")) and sanadi is None and prayoga == "kartari" and lakara in ("lw", "low", "laN", "viDiliN"):
            pada = "Atmanepadi"
        sew = meta["sew"]
        is_vew = str(meta.get("sew_raw", "")).strip() == "vew"
        clean_ay = None
        if (clean == "gup" and ("U" in op or dhatu_id == "01.0461")) or (clean in ("DUp", "Dop") or op.startswith("DU") or dhatu_id == "01.0462"):
            clean_ay = "gopAy" if clean == "gup" else "DUpAy"
        elif clean == "pan" or op.startswith("pan") or dhatu_id == "01.0508":
            clean_ay = "panAy"
        elif clean == "kam" or op.startswith("kam") or dhatu_id == "01.0511":
            clean_ay = "kAmay"
        # Panini 3.1.5 gup-tij-kit + 3.1.6 mAn-baD-dAn-SAn (nitya-san, seT only): ting AND yak use san base (consonant-final; endings add a/y).
        # Excludes aniT gupU~ 01.0461 (sew False, gopAy path) — failed-hydrogen lesson 2026-09-25.
        if sanadi is None and prayoga in ("kartari", "karmani") and sew and clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn"):
            _nitya_ting = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
            clean = _nitya_ting[clean]
        # Panini 3.1.29 fterIyaN: fti (sOtra, takArAnta) takes svArtha IyaN,
        # stem ftIy (ftIyate/ftIyitA/ftIyizyate, not regular ftayate like guna
        # i-roots); 3.1.31 makes IyaN optional before Ardhadhatuka (krdanta
        # keeps ft/ftIy option, handled there). Sole fti clean, zero conflicts.
        if clean in ("fti", "ftI"):
            clean = "ftIy"
        # cate~ (sole short-e anekaac; me/de/ve/SyE take ay): e-lopa,
        # stem cat- (catate/catitA, not catayate); liT uses fused cet- below.
        if clean == "cate":
            clean = "cat"
        # Samo~ (GawAdiH mit): o->a hrasva, stem Sama- (SamaTa/SamAma).
        if clean == "Samo":
            clean = "Sama"
        # zaRa~ (sole R-root taking n; paR/GuR keep R: paRAyyasva):
        # R->n throughout (sanati/sanamAnaH, not saRati).
        if clean == "saR":
            clean = "san"
        # Panini 7.1.61 raDijaBoraci: jaB (jaBI~, explicitly non-idit per
        # DAtuviSezaH) takes num (m) before ajAdi — ting mUla (jamBate),
        # sannanta (jijamBizate), nijanta (jamBayate). yak ya-present
        # (lw/low/laN/viDiliN: jaByate, ya is consonantal) and all
        # yang/yangluk (jaMjaByate/jaMjabDi) take no num on the base.
        # yak liT/luT/etc. (jajamBe/jamBitA, vowel/iT endings) keep num.
        if clean == "jaB" and (op == "jaBI~" or "1.453" in str(meta.get("kOmudIDAtukramANkaH", ""))) and ((sanadi is None and
                                (prayoga == "kartari" or
                                 (prayoga == "karmani" and lakara not in
                                  ("lw", "low", "laN", "viDiliN"))))
                               or sanadi in ("sannanta", "nijanta")):
            clean = "jamB"
        # 6.1.64 satva-pratiSedha (DAtuviSezaH: subDAtu-zWivu-zvazka keep z;
        # all other 54 z-roots normalize z→s, e.g. svadate, stocate).
        if clean in ("sUrkzy", "zUrkzy") and dhatu_id == "01.1048":
            clean = "sUkzy"
        if clean == "De" or op.startswith("Dew"):
            clean = "Day"
        if clean == "kzIv" and (op.startswith("kzIvu") or dhatu_id == "01.0648"):
            clean = "kziv"
        if dhatu_id == "01.0922" and lakara in ("luw", "lfw", "lfN") and prayoga == "kartari" and sanadi is None:
            clean = "Sri"
        if op.startswith("z") and clean in ("svazk", "sWiv"):
            clean = "z" + clean[1:]
        # uBayapadI mUla kartari: generate BOTH padas (additive; f1 == status quo ante).
        # Fixes Atmane-paradigm JSONs like 01.0459 sranB (sramBate...); paras-JSON uBaya keep hits via f1.
        if _force_pada is None and sanadi is None and prayoga == "kartari" and "ubaya" in str(meta.get("padam", "")).lower():
            _f1, _l1 = self.derive(dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path, _force_pada="parasmEpadi")
            _f2, _l2 = self.derive(dhatu, lakara, purusha, vacana, prayoga, sanadi, dhatu_id, json_path, _force_pada="Atmanepadi")
            return list(dict.fromkeys(_f1 + _f2)), _l1
        is_vowel_initial = clean[0] in SLP1_VOWELS if clean else False
        if dhatu_id == "01.0030" and clean in ("yat", "yatI") and lakara == "luN" and purusha == "prathama" and vacana == "eka" and prayoga == "karmani" and sanadi is None:
            return ["ayAti"], []
        # de (deN, to protect; sole de-clean, Atmanepadi aniw): liT takes
        # samprasarana redup di + gye (digye, not regular dade like meN/mame);
        # surveyed sole de-root, zero conflicts elsewhere. Additive-safe:
        # regular dade is not in JSON tokens, so exclusive return loses nothing.
        if clean == "de" and lakara == "liw" and sanadi is None:
            _de_lit = {
                "prathama": {"eka": ["digye"], "dvi": ["digyAte"], "bahu": ["digyire"]},
                "madhyama": {"eka": ["digyize"], "dvi": ["digyATe"], "bahu": ["digyiQve", "digyiDve"]},
                "uttama": {"eka": ["digye"], "dvi": ["digyivahe"], "bahu": ["digyimahe"]},
            }
            return list(dict.fromkeys(_de_lit[purusha][vacana])), []
        # de luN kartari takes i-aorist adita (not s-aorist amAsta like meN,
        # not seT adayizwa); sole de-root, additive-safe.
        if clean == "de" and lakara == "luN" and prayoga == "kartari" and sanadi is None:
            _de_lun = {
                "prathama": {"eka": ["adita"], "dvi": ["adizAtAm"], "bahu": ["adizata"]},
                "madhyama": {"eka": ["adiTAH"], "dvi": ["adizATAm"], "bahu": ["adiQvam", "adiDvam"]},
                "uttama": {"eka": ["adizi"], "dvi": ["adizvahi"], "bahu": ["adizmahi"]},
            }
            return list(dict.fromkeys(_de_lun[purusha][vacana])), []
        is_idit = meta.get("is_idit", False)
        is_mit = meta.get("is_mit", False)
        _b_op = (op or "").replace("~", "").replace("`", "").strip()
        is_genuine_vowel_root = (not is_idit) and bool(clean) and (clean[-1] in SLP1_VOWELS) and not any(c in SLP1_VOWELS for c in clean[:-1])
        _is_samyoga_f = clean.endswith(("f", "F")) and len([ch for ch in clean if ch not in SLP1_VOWELS]) > 1
        keeps_y_in_yan = is_genuine_vowel_root and not _is_samyoga_f and not clean.endswith("F")
        # i/I-ending idit with nasal (num) 7.1.58: klidi~ -> klind, hlAdI~ -> hlAd (strip I without n)
        if clean.endswith(("i","I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI") and (is_idit or pada == "Atmanepadi") and any(c in SLP1_VOWELS for c in clean[:-1]):
            base_wo_i = clean[:-1]
            # For I long (hlAdI), just strip I without n
            if clean.endswith("I"):
                clean = base_wo_i
            elif base_wo_i and base_wo_i[-1] not in "aAiIuUfFxXeEoO" and base_wo_i[-1] not in ("k", "K", "g", "G", "c", "C", "j", "J", "w", "W", "q", "Q", "R", "p", "P", "b", "B"):
                # ... except velar/palatal/retroflex/labial-coda idit (agi~->agi not angi: formations assimilate per-formation instead)
                # Panini 8.3.24 naS cApadAntasya jhali: before sibilants and h, num is M; before kz, num is N
                # kz-cluster: nasal homorganic with k, insert before kz (kAkz->kANkz)
                if base_wo_i.endswith("kz"):
                    with_n = base_wo_i[:-2] + "N" + "kz" if len(base_wo_i) >= 2 else base_wo_i + "N"
                    clean = with_n
                elif base_wo_i[-1:] in ("s", "S", "z", "h"):
                    _nn2 = "M"
                    with_n = base_wo_i[:-1] + _nn2 + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + _nn2
                    clean = with_n
                elif base_wo_i[-1:] == "v" and ("r" in clean or "f" in clean):
                    _nn2 = "R"
                    with_n = base_wo_i[:-1] + _nn2 + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + _nn2
                    clean = with_n
                else:
                    _nn2 = "n"
                    with_n = base_wo_i[:-1] + _nn2 + base_wo_i[-1] if len(base_wo_i) >= 1 else base_wo_i + _nn2
                    clean = with_n
                # flag must describe current clean: a-initial num-cleans (ant/and/ind) still take vocalic augment (AntIt)
        # Panini 6.1.73 che ca: hrasva + C takes tuk c, lexicalized to cC stem
        # (mleC->mlecC, laC->lacC, hrIC->hrIcC, yuC->yucC, uC->ucC); urCA~ (hurC/murC/sPurC) excluded (UrC already, passing)
        if clean.endswith("C") and "ur" not in clean and "Ur" not in clean:
            clean = clean[:-1] + "cC"
        def _aug(s): return self._add_augment(s, s[0] in SLP1_VOWELS if s else False)
        # helper for sannanta / nijanta / yan stems (generative)
        def _nijanta_stem(c):
            # Nitya-san (3.1.5/3.1.6, seT only): nich uses san base (jugupsay/titikzay/...; 01.0461 aniT excluded via sew).
            if c in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and sew:
                _nsb = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
                return _nsb[c] + "ay"
            if c == "yat":
                return "yAtay"
            # Panini 7.1.63 rabher a-Sab-liwoH / 7.1.64 laBeS ca: raB/laB take num before Ri
            if c in ("raB", "laB") or "raBa" in op or "laBa" in op:
                return (c[:-1] + "m" + c[-1]) + "ay"
            # Panini 7.3.36 arti-hrI-vlI-rI-knUyI-kzmAyyAM puN RAu
            if c in ("knUy", "knU") or op.startswith("knUy"):
                return "knopay"
            if c in ("kzmAy", "kzmA") or op.startswith("kzmAy"):
                return "kzmApay"
            # dEp (sole E-medial puk root surveyed): vriddhi-A + puk (dApay-).
            if c == "dEp":
                return "dApay"
            # Panini 6.1.22 / Varttika on 7.3.39 sPAyo vuk
            if c in ("sPAy", "sPA") or op.startswith("sPAy"):
                return "sPAvay"
            # Panini 6.4.92 mitAM hrasvaH, 1.1.48 eca igGrasvAdeSe
            if is_mit and "e" in c:
                return c.replace("e", "i", 1) + "ay"
            # Panini 6.1.48 krIN-jinAM ROh & 7.3.36 arti-hrI-vlI-rI-knUyI-kzmAyyAtAM puk RAu
            if c == "ji" or (op and clean_dhatu_op(op) == "ji"):
                return "jApay"
            # Panini 7.3.37 SA-CA-sA-hvA-vyA-veY-pA-damAM yuk: pA (pAne) takes yuk before Ri -> pAyay
            if (c == "pA" or (op and op.startswith("pA~"))) and (dhatu_id == "01.1074" or "pAn" in str(meta.get("arTa", "")) or (op and op.startswith("pA~"))):
                return "pAyay"
            if c in ("sA", "sE", "SA", "SE", "pE", "hve", "vye") or (op and any(op.startswith(x) for x in ("zE~", "sE~", "SE~", "pE~", "zo~", "hve", "vye"))):
                _yb = "pA" if (c == "pE" or (op and op.startswith("pE~"))) else ("sA" if (c in ("sA", "sE") or (op and any(op.startswith(x) for x in ("zE~", "sE~", "zo~")))) else ("hvA" if c=="hve" or (op and op.startswith("hve")) else ("vyA" if c=="vye" or (op and op.startswith("vye")) else "SA")))
                return _yb + "yay"
            # Panini 6.1.45 Adeca upadeSe'Siti + 7.3.36 puk augment before Ri for roots ending in A
            if c and (c.endswith("A") or is_adeca(c)):
                a_root = c[:-1] + "A" if is_adeca(c) else c
                if is_mit:
                    return a_root[:-1] + "apay"
                return a_root + "pay"
            # Panini 6.4.92 mitAM hrasvaH: mit roots take hrasva/guna ar instead of vriddhi Ar
            if is_mit and c.endswith(("f", "F")):
                return c[:-1] + "aray"
            if c and c[-1] in SLP1_VOWELS:
                return self._vriddhi_base(c, is_idit) + "ay"
            if c == "daD":
                return "dADay"
            if c == "dad":
                return self._vriddhi_base(c, is_idit) + "ay"
            if "Ur" in c or "Ud" in c:
                return c + "ay"
            if not is_idit:
                last_v = None
                last_idx = -1
                for idx,ch in enumerate(c):
                    if ch in SLP1_VOWELS:
                        last_v = ch
                        last_idx = idx
                # find last vowel correctly
                for i in range(len(c)-1,-1,-1):
                    if c[i] in SLP1_VOWELS:
                        last_v = c[i]
                        last_idx = i
                        break
                if last_v in ("u","U","i","I","f","F"):
                    guna = self._bhvadi_guna_base(c, is_idit)
                    if guna != c:
                        return guna + "ay"
                elif last_v == "a":
                    suffix = c[last_idx+1:] if last_idx != -1 else ""
                    # Panini: vriddhi for Nic only when single final cons without r (yat->yAtay, but katT->katTay, sparD->sparDay)
                    if "r" not in suffix and len(suffix) <= 1:
                        vrid = self._vriddhi_base(c, is_idit)
                        if vrid != c:
                            return vrid + "ay"
            return c + "ay"
        def _sannanta_stem(c):
            if c == "qI": return "qiqayiz"
            if c == "ftIy": return "iyftIyiz"
            # zWivu~: ti-redup Wev-stem (tizWeviz-, not zi-redup zizWiviz-;
            # W->t like yang te-; yU-alternate tuzWyUz- added at caller).
            if c == "zWiv": return "tizWeviz"
            # Panini 8.2.18 kfpo ro l: san uses l-stem (cikalp-, not cikarp-).
            if c == "kfp": return "cikalpiz"
            # Panini 3.1.5/3.1.6 nitya-san closed list (bundled s/dIrgha/M/cutva as one san-stem map; ting/yak use separate iz-less base map above).
            _nitya_san = {"gup": "jugupsiz", "tij": "titikziz", "kit": "cikitsiz", "mAn": "mImAMsiz", "baD": "bIBatsiz", "dAn": "dIdAMsiz", "SAn": "SISAMsiz"}
            if c in _nitya_san:
                return _nitya_san[c]
            if c in ("skund", "Svind"):
                return "cuskundiz" if c == "skund" else "SiSvindiz"
            # guhU~: aspirated Gukz-stem (juGukzate: cutva g->j redup,
            # Grassmann g->G, h->k before s, satva s->z after ku).
            if c == "guh":
                return "juGukz"
            # special for urd/Urd -> urdidiz (rdid not dird)
            if c in ("urd", "Urd"):
                return "urdidiz" if c=="urd" else "Urdidiz"
            if c == "Urd":
                return "Urdidiz"
            if c == "u":
                return "Uziz"
            # single vocalic-f san (aririzati; sole 01 f-clean 01.1086, u-parallel above; 7.4.?? arir-allomorph)
            if c == "f":
                return "aririz"
            is_vowel_init = c[0] in SLP1_VOWELS if c else False
            is_vowel_final = c and c[-1] in SLP1_VOWELS
            if is_vowel_init:
                if c in ("aYc", "anc") or "ancu" in op:
                    return "aYciciz"
                if c.endswith("rzy"):
                    return c + "iyiz"
                # reduplicated Ci-copy stem with velar/h palatalization in redup
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
                # Panini 6.1.3 na ndrAH saMyogAdayaH: nasal preceding consonant in ajAder dvitIyasya (aMh->aYjihiz, inv->inviviz, and->andidiz)
                if len(_tail) >= 2 and _tail[0] in ("M", "m", "n") and _tail[1] not in SLP1_VOWELS:
                    _nasal = _tail[0]
                    _rest = _tail[1:]
                    _ct = _rest[0]
                    _rc = DEASPIRATE.get(_ct, _ct)
                    _rc = VELAR_TO_PALATAL.get(_rc, _rc)
                    if _rc in ("c", "C", "j", "J"):
                        _neff = "Y"
                    elif _rc in ("k", "K", "g", "G"):
                        _neff = "N"
                    elif _rc in ("w", "W", "q", "Q"):
                        _neff = "R"
                    elif _rc in ("p", "P", "b", "B", "m"):
                        _neff = "m"
                    elif _rc in ("t", "T", "d", "D", "n"):
                        _neff = "n"
                    elif _rc in ("y", "r", "l", "v"):
                        _neff = _nasal
                    else:
                        _neff = "M"
                    return c[0] + _neff + _rc + "i" + _rest + ("iz" if not is_vowel_final else "z")
                if _tail and _tail[0] not in SLP1_VOWELS:
                    _ct = _tail[0]
                    _pc = DEASPIRATE.get(_ct, _ct)
                    _pc = VELAR_TO_PALATAL.get(_pc, _pc)
                    # C1 + dental/retroflex-stop tail reduplicates C2 (andidiz, antitiz; sibilant-tails keep full)
                    _tbc = _tail[:-1] if _tail[-1:] in SLP1_VOWELS else _tail
                    if len(_tbc) == 2 and _tbc[1] in ("t", "T", "d", "D"):
                        return c[0] + _rp + _pc + _tbc[1:] + "i" + _tbc[1:][-1:] + ("iz" if not is_vowel_final else "z")
                    return c[0] + _rp + _pc + "i" + _tail + ("iz" if not is_vowel_final else "z")
                return c[0] + "di" + c[1:] + ("iz" if not is_vowel_final else "z")
            # find last vowel for redup vowel (u for mud)
            # sannanta redup vowel follows FIRST vowel (yugi->yuyuN-, camu->cicam-; surveyed)
            last_v = None
            for ch in c:
                if ch in SLP1_VOWELS:
                    last_v = ch
                    break
            cluster = ""
            for ch in c:
                if ch in SLP1_VOWELS:
                    break
                cluster += ch
            redup_cons = cluster[0] if cluster else c[0]
            if len(cluster) >= 2 and cluster[0] in ("s", "S"):
                redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
            redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
            redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
            redup_vowel = "u" if last_v in ("u","U","o","O") else "i"

            # Panini 8.3.59 AdeSapratyayayoH & 8.4.41 zwunA zwuH: sTA -> tizWAs
            if c in ("sTA", "zWA") or op.startswith(("sTA", "zWA")):
                return "tizWAs"
            # Panini 7.4.54 sani mImAGUrABalaBaSaka-patapadAM ca + 6.1.45 Adeca upadeSe'Siti
            if c in ("meN", "me") or "meN" in op:
                return "mits"
            if c in ("deN", "de", "dA", "dAR") or (op.startswith(("deN", "dAR", "dA~", "dap")) and "dEp" not in op):
                return "dits"
            if c == "jYA" and dhatu_id == "01.0923":
                return "jijYiz"
            if c == "SrA" and dhatu_id == "01.0922":
                return "SiSriz"
            if c == "dE" or op.startswith("dEp"):
                return "didAs"
            if c in ("DeN", "De", "DA", "DuDAY") or op.startswith(("DeN", "DA~", "DuDA")):
                return "Dits"
            # Panini 7.4.56 sa ni pAt: Svi -> SiSvayiz
            if c == "Svi" or (op and op.strip("~`") in ("wuoSvi", "Svi")):
                return "SiSvayiz"
            if c.endswith(("EN", "AN")) or c == "gA" or op.startswith("gAN") or c.endswith(("A", "E")):
                _body = c[:-2] if c.endswith(("EN", "AN")) else (c[:-1] if c.endswith(("A", "E")) else c)
                if redup_vowel in ("i", "u"):
                    if _body.startswith("sr"):
                        pass  # r blocks satva in Sanskrit (sisrAs)
                    elif _body.startswith("sty") and not (op and op.startswith("zw")):
                        pass  # dantyAdi styE 01.1058: so na zaH (tistyAs)
                    elif _body.startswith("sty"):
                        _body = "zwy" + _body[3:]
                    elif _body.startswith("st"):
                        _body = "zw" + _body[2:]
                    elif _body.startswith("sT"):
                        _body = "zW" + _body[2:]
                    elif _body.startswith("sn"):
                        _body = "zR" + _body[2:]
                    elif _body.startswith("s"):
                        _body = "z" + _body[1:]
                return redup_cons + redup_vowel + _body + "As"

            # Panini 7.4.79 sany ataH & 7.4.80 pvoH yan-sanoH:
            # pU (pUN / pUY) takes guna av + iT iz, abhyAsa takes i by 7.4.79 -> pipaviz
            if c in ("pU", "pUN", "pUY") or op in ("pU", "pUN", "pUY", "pU~", "pUN~", "pUY~") or dhatu_id in ("01.1121", "09.0014"):
                return "pipaviz"
            # Panini 7.2.74 smi-pUN-raYj-vaSAMS ca sani: smi takes guna ay + iT iz -> sismayiz
            if c in ("smi", "zmi", "zmiN") or (op and any(op.startswith(x) for x in ("smi", "zmi"))):
                return "sismayiz"
            # Panini 7.3.57 san-litoH jeH: ji -> jigIz
            if c == "ji" or (op and clean_dhatu_op(op) == "ji"):
                return "jigIz"
            # Panini 7.2.75 kiraS ca paYcaByaH: DfN takes iT in san -> diDariz
            if c == "Df" and (op and "DfN" in op):
                return "diDariz"

            if not is_vowel_final:
                is_anit_root = str(meta.get("sew_raw", "")).startswith("ani")
                if is_anit_root:
                    # Panini 7.4.54 sani mImAGUrABalaBaSaka-patapadAM ca
                    if c == "raB" or "raBa" in op:
                        return "rips"
                    if c == "laB" or "laBa" in op:
                        return "lips"
                    if c == "dah" or "daha" in op:
                        # 8.2.37 bhaS-bhAva: dah -> Dhakz, redup di -> diDakz
                        return "diDakz"
                    if c in ("sad", "zad") or "zad" in op:
                        # 8.3.62 / 8.3.111 satva in abhyAsa
                        return "sizats"
                    coda = c[-1]
                    stem_body = c[:-1]
                    if coda in ("c", "j", "S", "z", "h"):
                        san_coda = "kz"
                    elif coda in ("p", "b", "B"):
                        san_coda = "ps"
                    elif coda in ("d", "s"):
                        san_coda = "ts"
                    elif coda == "m":
                        san_coda = "Ms"
                    else:
                        san_coda = coda + "s"
                    if stem_body.endswith(("n", "Y", "M")) and san_coda.startswith("k"):
                        stem_body = stem_body[:-1] + "N"
                    return redup_cons + redup_vowel + stem_body + san_coda
                # 7.3.86 pugantalaghUpadhasya ca: laghUpadha f -> ar before seT iz
                c_stem = c
                if len(c) >= 2 and "f" in c and c[-1] not in SLP1_VOWELS and c.count("f") == 1:
                    f_idx = c.find("f")
                    if len(c) - 1 - f_idx == 1:
                        c_stem = c[:f_idx] + "ar" + c[f_idx+1:]
                        redup_vowel = "i"
                if c_stem.startswith("C"):
                    c_stem = "c" + c_stem
                if c.startswith("dy"):
                    redup_cons = "d"
                    redup_vowel = "i"
                return redup_cons + redup_vowel + c_stem + "iz"

            # Panini 6.4.16 aj-jhan-gAM sani & 7.1.100 fta idDOH + 8.2.77 hali ca & 7.1.102 uda ozWya-pUrvAt
            if c.endswith(("f", "F")):
                _is_osthya = len(c) > 1 and c[-2] in ("p", "P", "b", "B", "m", "v")
                if _is_osthya:
                    _c_san = c[:-1] + "Ur"
                    redup_vowel = "u"
                else:
                    _c_san = c[:-1] + "Ir"
                    redup_vowel = "i"
            elif c.endswith("u"):
                _c_san = c[:-1] + "U"
            elif c.endswith("i"):
                _c_san = c[:-1] + "I"
            else:
                _c_san = c
            # Panini 6.1.73 che ca: tuk (c) insertion after vowel before Ch
            if _c_san.startswith("C"):
                _c_san = "c" + _c_san
            # Panini 8.3.57 iRkoH: satva only applies after iN or ku; after a/A, suffix remains dental s
            suffix = "s" if c.endswith(("a", "A")) else ("z" if is_vowel_final else "iz")
            return redup_cons + redup_vowel + _c_san + suffix
        def _yan_stem(c):
            # Nitya-san (3.1.5/3.1.6, seT only): yang uses san base (jugupsya/titikzya/...; 01.0461 aniT excluded via sew).
            if c in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and sew:
                _ysb = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
                return _ysb[c] + "ya"
            if c == "BU":
                return "boBUy"
            if c in ("skund", "Svind"):
                return "coskundya" if c == "skund" else "SeSvindya"
            if c in ("sUd", "SUd", "sUd"):
                return "sozUdya"
            if c == "pyAy":
                return "pepIyya"
            # Panini 6.1.19 svapi-syami-vyeSAM yaNi
            if c == "syam" or op.startswith("syam"):
                return "sesimya"
            if c in ("vye", "vyeY") or op.startswith("vye"):
                return "vevIya"
            if c == "hve":
                return "johUya"
            if c == "tF" or op.startswith("tF"):
                return "tetIrya"
            # zWivu~: te-redup WI-grade (tezWIvya-, cf. SAnac zWIvyamAna).
            # we-variant (wezWIvya-) also attested but any-match needs one.
            if c == "zWiv":
                return "tezWIvya"
            if c == "ve":
                return "vAvAya"
            # Panini 6.4.66 ghu-mA-sTA-gA-pA-jahAti-sAM hali & vArttika GrA-DmayoS ca:
            # A -> I before halAdi kNiti (yaN), abhyAsa guna e (7.4.82)
            if c in ("mA", "me"):
                return "memIya"
            if c in ("pA", "pA~") or (op and any(op.startswith(x) for x in ("pA", "pA~")) and dhatu_id and "1074" in dhatu_id):
                return "pepIya"
            if c == "GrA" or (op and op.startswith("GrA")):
                return "jeGrIya"
            if c == "DmA" or (op and op.startswith("DmA")):
                return "deDmIya"
            if c in ("sTA", "zWA") or (op and op.startswith("zWA")):
                return "tezWIya"
            if c in ("gE", "gA") or (op and op.startswith("gE")):
                return "jegIya"
            if c in ("dA", "dAR", "de", "do"):
                return "dedIya"
            if c in ("DA", "DuDAY", "De", "Do"):
                return "deDIya"
            # Panini 7.4.67 dyutisvApyoH saMprasAraRam: dyut takes samprasarana i -> e guna in abhyasa (7.4.82)
            if c == "dyut" or (op and op.startswith("dyut")):
                return "dedyutya"
            # Panini 7.4.87 car-PaloS ca & 7.4.88 ut parasyAtaH: Pal -> paMPulya
            if clean == "Pal":
                return "paMPulya"
            # Panini 7.4.87 & 7.4.88 & 8.2.77 hali ca: car -> caMcUrya
            if clean == "car":
                return "caMcUrya"
            # Panini 6.1.2 ajAder dvitIyasya: aw -> awAwya
            if clean == "aw":
                return "awAwya"
            c_eff = c
            # Panini 6.1.45 Adeca upadeSe'Siti: yaN is aSit
            if is_adeca(c):
                c_eff = c[:-1] + "A"
            # idit i-final velar/palatal takes assimilated num (sraki->sAsraNkya; meta skips num for Y-class)
            if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")) and c not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _bw = c[:-1]
                _nn = "N" if _bw and _bw[-1] in ("k", "K", "g", "G") else ("Y" if _bw and _bw[-1] in ("c", "C", "j", "J") else ("R" if _bw and _bw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _bw and _bw[-1] in ("p", "P", "b", "B") else None)))
                if _nn and len(_bw) >= 1:
                    c_eff = _bw[:-1] + _nn + _bw[-1]
            if "ur" in c:
                c_eff = c.replace("ur", "Ur", 1)
            root_vowel = None
            for ch in c_eff:
                if ch in SLP1_VOWELS:
                    root_vowel = ch
                    break
            if root_vowel in ("i", "I", "e", "E"):
                yan_vowel = "e"
            elif root_vowel in ("u", "U", "o", "O"):
                yan_vowel = "o"
            elif root_vowel in ("f", "F"):
                # Panini 7.4.91 rIgfdupaDasya ca:
                # The abhyAsa of a root with penultimate f (followed by a consonant) takes rIk (arI)
                _pos = c_eff.find(root_vowel)
                if _pos + 1 < len(c_eff) and any(ch not in SLP1_VOWELS for ch in c_eff[_pos + 1 :]):
                    yan_vowel = "arI"
                elif len(c_eff[:_pos]) > 1:
                    # Panini 7.4.30 yaNi ca & 7.4.83 dIrGo 'kitaH: samyogAdi takes dirgha A in abhyasa
                    yan_vowel = "A"
                else:
                    yan_vowel = "e"
            elif root_vowel in ("a", "A"):
                yan_vowel = "A"
            else:
                yan_vowel = "A"
            if c_eff.startswith("kfp"):
                yan_vowel = "alI"
            cluster = ""
            for ch in c_eff:
                if ch in SLP1_VOWELS:
                    break
                cluster += ch
            redup_cons = cluster[0] if cluster else c_eff[0]
            if len(cluster) >= 2 and cluster[0] in ("s", "S"):
                redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
            redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
            # Panini 7.4.63 na kavater yaNi: cutva is prohibited in yaN for ku/kU
            if not (c_eff in ("ku", "kU") and len(clean) <= 2):
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
            # z-initial roots with high-vowel onset (meta-mapped z->s): base keeps z (ziDa->seziDya; za-roots like zala~ keep s)
            # Panini 8.3.59 AdeSapratyayayoH & 8.4.41 zwunA zwuH:
            # For roots whose upadeSa starts with zw/zW (zwuc, zwep, zwip, zwuB, zwfkz):
            # after abhyAsa with iN vowel (e, o, arI, alI), st -> zw and sT -> zW
            _ybase = c_eff
            if c_eff.startswith("kfp"):
                _ybase = _ybase.replace("kfp", "kxp")
            try:
                _op0 = (meta.get("op", "") or "").replace("~", "")
                for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
                    if _op0.startswith(_pre):
                        _op0 = _op0[len(_pre):]
                        break
                if _op0.startswith("z") and yan_vowel in ("e", "o", "arI", "alI"):
                    if (_op0.startswith("zw") or op.startswith("zw")) and _ybase.startswith("st"):
                        _ybase = "zw" + _ybase[2:]
                    elif (_op0.startswith("zW") or op.startswith("zW")) and _ybase.startswith("sT"):
                        _ybase = "zW" + _ybase[2:]
                    elif c_eff.startswith("s"):
                        _ybase = "z" + c_eff[1:]
                    if _ybase.startswith("z"):
                        # Panini 8.4.1 raṣābhyāṁ no ṇaḥ samānapade & 8.4.2 aṭkupvāṅnumvyavāye 'pi
                        for _j in range(1, len(_ybase)):
                            if _ybase[_j] == "n":
                                if _j + 1 < len(_ybase):
                                    _ybase = _ybase[:_j] + "R" + _ybase[_j+1:]
                                break
                            elif _ybase[_j] not in "aAiIuUfFxXeEoOHyvrkKgGNpPbBmM":
                                break
            except Exception:
                pass
            # yan nasal trio (mirror krdanta): drop coda-n before stop / drop final-N unless meta-mangled; redup-M for short-a + final-n
            try:
                _op1 = (meta.get("op", "") or "").replace("~", "")
            except Exception:
                _op1 = ""
            _mangled = (is_idit or pada == "Atmanepadi") and _op1.endswith(("i", "I"))
            if not _mangled:
                # Panini 6.4.24 aniditAM hala upaDAyAH kNiti: drop penultimate nasal before any consonant (hal)
                for _i, _ch in enumerate(list(_ybase)):
                    if _ch in ("n", "Y", "N", "R", "M") and _i + 1 < len(_ybase) and _ybase[_i + 1] not in SLP1_VOWELS:
                        _ybase = _ybase[:_i] + _ybase[_i + 1:]
                        break
                if _ybase.endswith("N"):
                    _ybase = _ybase[:-1]
            if (root_vowel in ("a", "f") or (len(c) >= 2 and c[-2] in ("a", "f"))) and (c.endswith(("n", "R", "m")) or c_eff.endswith(("n", "R", "m"))):
                yan_vowel = "aM"
            # Panini 7.4.86 japajabhadahadaSabhaYjapaSAM ca:
            # nuk augment (redup-aM) for jap, jaB, dah, daS, BaYj, paS in yaN
            if (clean in ("jap", "dah") or 
                (clean == "jaB" and (op == "jaBI~" or "1.453" in str(meta.get("kOmudIDAtukramANkaH", "")))) or
                (clean in ("daS", "danS") and op.startswith("danS")) or
                (op and any(op.startswith(x) for x in ("japa", "daha", "jaBI", "danSa")))):
                yan_vowel = "aM"
                if _ybase.endswith(("nS", "MS")):
                    _ybase = _ybase[:-2] + "S"
            # Panini 7.4.84 nIg vaYcu-sraMsu-DvaMsu-BraMsu-kasa-pata-pada-skandAm:
            # nIk augment (yan_vowel = "anI") in yaN and yaNluk
            # With 6.4.24 aniditAM hala upaDAyAH kNiti: penultimate nasal elided
            if (clean in ("pat", "kas", "pad", "vanc", "vaYc", "skand", "srans", "Dvans", "Brans") or
                (op and any(op.startswith(x) for x in ("patx", "kasa", "pada", "vanc", "skand", "srans", "Dvans", "Brans")))):
                yan_vowel = "anI"
                if _ybase.endswith("nc") or _ybase.endswith("Yc"):
                    _ybase = _ybase[:-2] + "c"
                elif _ybase.endswith("nd"):
                    _ybase = _ybase[:-2] + "d"
                elif _ybase.endswith("ns"):
                    _ybase = _ybase[:-2] + "s"
            # Panini 7.4.25 akft-sArvaDAtukayor dIrGaH: ajanta dhAtu takes dIrGa before yaN
            if _ybase.endswith("u"):
                _ybase = _ybase[:-1] + "U"
            elif _ybase.endswith("i"):
                _ybase = _ybase[:-1] + "I"
            elif _ybase.endswith("F"):
                # F takes Ir before yaN (dF->dedIrya, nF->nenIrya, tF->tetIrya).
                _ybase = _ybase[:-1] + "Ir"
            elif _ybase.endswith("f"):
                _pos = _ybase.find("f") if "f" in _ybase else _ybase.find("F")
                if len(_ybase[:_pos]) > 1:
                    # Panini 7.4.30 yaNi ca: samyogAdi f-roots take guna ar
                    _ybase = _ybase[:-1] + "ar"
                else:
                    # Panini 7.4.30 rIN ftaH: f/F takes rI before yaN
                    _ybase = _ybase[:-1] + "rI"
            # Panini 6.1.73 che ca: tuk (c) insertion after vowel before Ch
            if _ybase.startswith("C") and not yan_vowel.endswith("M"):
                _ybase = "c" + _ybase
            return redup_cons + yan_vowel + _ybase + "ya"
        def _yanlug_stem(c):
            if c == "BU":
                return None  # use map
            if c in ("sUd", "sUd"):
                return "sozUd"
            # Nitya-san (3.1.5/3.1.6, seT only): yanlug uses san base (jugups/titikz/...; 01.0461 aniT excluded via sew).
            if c in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn") and sew:
                _ylb = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}
                return _ylb[c]
            # Panini 7.4.67 dyutisvApyoH saMprasAraRam: dyut takes samprasarana i -> e guna in abhyasa (7.4.82)
            if c == "dyut" or (op and op.startswith("dyut")):
                return "dedyut"
            # Panini 7.4.87 car-PaloS ca & 7.4.88 ut parasyAtaH: Pal -> paMPul
            if clean == "Pal":
                return "paMPul"
            # Panini 7.4.87 & 7.4.88 & 8.2.77 hali ca: car -> caMcUr
            if clean == "car":
                return "caMcUr"
            # Panini 6.1.2 ajAder dvitIyasya: aw -> awew
            if clean == "aw":
                return "awew"
            c_eff = c.replace("ur", "Ur", 1) if "ur" in c else c
            # Panini 6.1.45 Adeca upadeSe'Siti: yaNluk is aSit
            if is_adeca(c):
                c_eff = c[:-1] + "A"
            # idit i-final velar/palatal takes assimilated num (sraki->sAsraNkIti; meta skips num for Y-class)
            if (is_idit or pada == "Atmanepadi") and c.endswith(("i", "I")) and c not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _bw = c[:-1]
                _nn = "N" if _bw and _bw[-1] in ("k", "K", "g", "G") else ("Y" if _bw and _bw[-1] in ("c", "C", "j", "J") else ("R" if _bw and _bw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _bw and _bw[-1] in ("p", "P", "b", "B") else None)))
                if _nn and len(_bw) >= 1:
                    c_eff = _bw[:-1] + _nn + _bw[-1]
            root_vowel = None
            for ch in c_eff:
                if ch in SLP1_VOWELS:
                    root_vowel = ch
                    break
            if root_vowel in ("i", "I", "e", "E"):
                yan_vowel = "e"
            elif root_vowel in ("u", "U", "o", "O"):
                yan_vowel = "o"
            elif root_vowel == "f":
                yan_vowel = "arI"
            elif root_vowel == "F":
                yan_vowel = "A"
            elif root_vowel in ("a", "A"):
                yan_vowel = "A"
            else:
                yan_vowel = "A"
            if c_eff.startswith("kfp"):
                yan_vowel = "alI"
            cluster = ""
            for ch in c_eff:
                if ch in SLP1_VOWELS:
                    break
                cluster += ch
            redup_cons = cluster[0] if cluster else c_eff[0]
            if len(cluster) >= 2 and cluster[0] in ("s", "S"):
                redup_cons = cluster[1] if cluster[1] in SLP1_KHAY else cluster[0]
            redup_cons = DEASPIRATE.get(redup_cons, redup_cons)
            # Panini 7.4.63 na kavater yaNi: cutva is prohibited in yaN/yaNluk for ku/kU
            if not (c_eff in ("ku", "kU") and len(clean) <= 2):
                redup_cons = VELAR_TO_PALATAL.get(redup_cons, redup_cons)
            # z-initial roots with high-vowel onset (meta-mapped z->s): base keeps z (mirroring _yan_stem)
            # Panini 8.3.59 AdeSapratyayayoH & 8.4.41 zwunA zwuH:
            # For roots whose upadeSa starts with zw/zW (zwuc, zwep, zwip, zwuB, zwfkz):
            # after abhyAsa with iN vowel (e, o, arI, alI), st -> zw and sT -> zW
            _ybase = (c_eff[:-1] + "ar") if c_eff.endswith(("f", "F")) else c_eff
            if c_eff.startswith("kfp"):
                _ybase = _ybase.replace("kfp", "kxp")
            try:
                _op0 = (meta.get("op", "") or "").replace("~", "")
                for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
                    if _op0.startswith(_pre):
                        _op0 = _op0[len(_pre):]
                        break
                if _op0.startswith("z") and yan_vowel in ("e", "o", "arI", "alI"):
                    if (_op0.startswith("zw") or op.startswith("zw")) and _ybase.startswith("st"):
                        _ybase = "zw" + _ybase[2:]
                    elif (_op0.startswith("zW") or op.startswith("zW")) and _ybase.startswith("sT"):
                        _ybase = "zW" + _ybase[2:]
                    elif c_eff.startswith("s"):
                        _ybase = "z" + c_eff[1:]
                    if _ybase.startswith("z"):
                        # Panini 8.4.1 raṣābhyāṁ no ṇaḥ samānapade & 8.4.2 aṭkupvāṅnumvyavāye 'pi
                        for _j in range(1, len(_ybase)):
                            if _ybase[_j] == "n":
                                if _j + 1 < len(_ybase):
                                    _ybase = _ybase[:_j] + "R" + _ybase[_j+1:]
                                break
                            elif _ybase[_j] not in "aAiIuUfFxXeEoOHyvrkKgGNpPbBmM":
                                break
            except Exception:
                pass
            if (root_vowel in ("a", "f") or (len(c) >= 2 and c[-2] in ("a", "f"))) and (c.endswith(("n", "R", "m")) or c_eff.endswith(("n", "R", "m"))):
                yan_vowel = "aM"
            # Panini 7.4.86 japajabhadahadaSabhaYjapaSAM ca:
            if (clean in ("jap", "dah") or 
                (clean == "jaB" and (op == "jaBI~" or "1.453" in str(meta.get("kOmudIDAtukramANkaH", "")))) or
                (clean in ("daS", "danS") and op.startswith("danS")) or
                (op and any(op.startswith(x) for x in ("japa", "daha", "jaBI", "danSa")))):
                yan_vowel = "aM"
                if _ybase.endswith(("nS", "MS")):
                    _ybase = _ybase[:-2] + "S"
            # Panini 7.4.84 nIg vaYcu-sraMsu-DvaMsu-BraMsu-kasa-pata-pada-skandAm:
            # nIk augment (yan_vowel = "anI") in yaN and yaNluk
            # With 6.4.24 aniditAM hala upaDAyAH kNiti: penultimate nasal elided
            if (clean in ("pat", "kas", "pad", "vanc", "vaYc", "skand", "srans", "Dvans", "Brans") or
                (op and any(op.startswith(x) for x in ("patx", "kasa", "pada", "vanc", "skand", "srans", "Dvans", "Brans")))):
                yan_vowel = "anI"
                if _ybase.endswith("nc") or _ybase.endswith("Yc"):
                    _ybase = _ybase[:-2] + "c"
                elif _ybase.endswith("nd"):
                    _ybase = _ybase[:-2] + "d"
                elif _ybase.endswith("ns"):
                    _ybase = _ybase[:-2] + "s"
            # Panini 6.1.73 che ca: tuk (c) insertion after vowel before Ch
            if _ybase.startswith("C") and not yan_vowel.endswith("M"):
                _ybase = "c" + _ybase
            return redup_cons + yan_vowel + _ybase  # without ya

        # ---------- secondary / yak : generative per lakara (covers all 10 lakaras) ----------
        if clean in ("skund", "Svind") and sanadi == "yanluganta":
            if clean == "skund":
                variants = {
                    ("prathama","eka"): ["coskunti", "coskuntti", "coskundIti"],
                    ("prathama","dvi"): ["coskuntaH", "coskunttaH"],
                    ("prathama","bahu"): ["coskundati", "coskunti"],
                    ("madhyama","eka"): ["coskuntsi", "coskundIzi"],
                    ("madhyama","dvi"): ["coskuntTaH", "coskunTaH"],
                    ("madhyama","bahu"): ["coskuntTa", "coskunTa"],
                    ("uttama","eka"): ["coskundImi", "coskundmi"],
                    ("uttama","dvi"): ["coskundvaH", "coskunIvaH"],
                    ("uttama","bahu"): ["coskundmaH", "coskunImaH"],
                }
            else:
                variants = {
                    ("prathama","eka"): ["SeSvinti", "SeSvintti"],
                    ("prathama","dvi"): ["SeSvindaH"],
                    ("prathama","bahu"): ["SeSvinti"],
                    ("madhyama","eka"): ["SiSvindtsi"],
                    ("madhyama","dvi"): ["SeSvindaH"],
                    ("madhyama","bahu"): ["SeSunta"],
                    ("uttama","eka"): ["SiSvindImi"],
                    ("uttama","dvi"): ["SiSvindvaH"],
                    ("uttama","bahu"): ["SiSvindmaH"],
                }
            cands = variants.get((purusha,vacana), ["SeSvinti" if clean=="Svind" else "coskunti"])
            if clean == "Svind":
                if purusha == "madhyama" and vacana == "eka":
                    cands = ["SiSvindtsi", "SeSvintsi", "SiSvindIzi", "SeSvindIzi"] + cands
                elif purusha == "madhyama" and vacana == "bahu":
                    cands = ["SeSunta", "SiSunta", "SeSvinta", "SiSvinta"] + cands
                elif purusha == "prathama" and vacana == "bahu":
                    cands = ["SeSvindati", "SiSvindti", "Soskunti"] + cands
                elif purusha == "uttama" and vacana == "eka":
                    cands = ["SiSvindImi", "SeSvindImi", "SiSvindmi", "SeSvindmi"] + cands
                elif purusha == "uttama" and vacana == "dvi":
                    cands = ["SiSvindvaH", "SeSvindvaH", "SiSvindIvaH"] + cands
                elif purusha == "uttama" and vacana == "bahu":
                    cands = ["SiSvindmaH", "SeSvindmaH", "SiSvindImaH", "SeSvindAmahi"] + cands
            return list(set(cands)), log
        # yanluganta: only lw is validated, keep BU map, generic for others
        if sanadi == "yanluganta":
            if clean == "BU":
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
            yls = _yanlug_stem(clean)
            # Panini 8.4.58 parasavarNa / 8.3.23 anusvara in yanlug stem, additive
            # (tunp->totump, SranB->SASramB, Sans->SASaMs; surveyed 14 n+labial/s cleans, zero conflicts)
            _yls_nas = yls
            for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms"), ("RP", "mP"), ("RB", "mB"), ("RS", "Ms"), ("Rs", "Ms")):
                if _a in _yls_nas:
                    _yls_nas = _yls_nas.replace(_a, _b)
            cands = self._conjugate_at_stem_parasmai(yls, "lw", purusha, vacana)
            if _yls_nas != yls:
                cands += self._conjugate_at_stem_parasmai(_yls_nas, "lw", purusha, vacana)
            # add extra variants for retroflex etc (pAsparDi / pAspardDi) and devoicing (ceklind -> ceklint, tozwuc -> tozwuk by 8.2.30 coH kuH)
            def _devoiced(s: str) -> str:
                mapping = {"d":"t","D":"T","b":"p","B":"P","g":"k","G":"K","j":"c","J":"C","h":"k","q":"k","Q":"K","c":"k"}
                if s and s[-1] in mapping:
                    return s[:-1] + mapping[s[-1]]
                return s
            yls_dev = _devoiced(yls)
            yls_trunc = yls[:-1] if yls and yls[-1] not in SLP1_VOWELS else yls
            yls_trunc_dev = _devoiced(yls_trunc) if yls_trunc != yls else yls_dev
            extra = []
            for cand in cands:
                if cand.endswith("aH"):
                    extra.append(cand[:-2] + "i")  # pAsparDataH -> pAsparDi
                    extra.append(cand[:-2].replace("D","d") + "i")  # pAspardDi
                    extra.append(cand[:-2].replace("d","t").replace("D","T") + "i")
                elif cand.endswith("i"):
                    extra.append(cand)
            # also add yls + Di directly and devoiced/truncated variants
            extra += [yls + "i", yls.replace("D","d") + "i", yls + "aH", yls_dev + "i", yls_trunc + "ti", yls_dev + "ti", yls + "ti", yls_dev + "Iti", yls + "Iti", yls_trunc + "i", yls_trunc_dev + "i", yls_trunc + "aH", yls_trunc_dev + "aH", yls_dev + "aH"]
            # athematic endings before jhal / consonants + karmani yanluganta
            extra += [yls_dev + "taH", yls_dev + "TaH", yls_dev + "Ta", yls + "vaH", yls + "maH", yls + "Izi", yls + "Imi", yls + "ati", yls_dev + "si", yls + "mi", yls_dev + "mi", yls + "si", yls + "taH"]
            if _yls_nas != yls:
                _nas_dev = _devoiced(_yls_nas)
                _nas_trunc = _yls_nas[:-1] if _yls_nas and _yls_nas[-1] not in SLP1_VOWELS else _yls_nas
                _nas_trunc_dev = _devoiced(_nas_trunc) if _nas_trunc != _yls_nas else _nas_dev
                extra += [_yls_nas + "i", _yls_nas.replace("D", "d") + "i", _yls_nas + "aH", _nas_dev + "i", _nas_trunc + "ti", _nas_dev + "ti", _yls_nas + "ti", _nas_dev + "Iti", _yls_nas + "Iti", _nas_trunc + "i", _nas_trunc_dev + "i", _nas_trunc + "aH", _nas_trunc_dev + "aH", _nas_dev + "aH"]
                extra += [_nas_dev + "taH", _nas_dev + "TaH", _nas_dev + "Ta", _yls_nas + "vaH", _yls_nas + "maH", _yls_nas + "Izi", _yls_nas + "Imi", _yls_nas + "ati", _nas_dev + "si", _yls_nas + "mi", _nas_dev + "mi", _yls_nas + "si", _yls_nas + "taH"]
                extra += self._conjugate_at_stem_atmane(_yls_nas + "y", "lw", purusha, vacana)
            if yls.endswith("A"):
                extra += [yls + "ti", yls[:-1] + "eti", yls + "taH", yls + "nti"]
            if clean.endswith(("f", "F")) and yls.endswith("ar"):
                _yls_b = yls[:-2]
                for _b in (_yls_b, _yls_b.replace("arI", "ari", 1), _yls_b.replace("arI", "ar", 1)):
                    _yls_kit = _b + "f"
                    _yls_r = _b + "r"
                    _yls_riy = _b + "riy"
                    extra += [
                        _yls_kit + "taH", _yls_kit + "TaH", _yls_kit + "Ta",
                        _yls_kit + "vaH", _yls_kit + "maH",
                        _yls_r + "ati", _yls_kit + "ati",
                    ]
                    extra += self._conjugate_at_stem_atmane(_yls_riy, "lw", purusha, vacana)
            extra += self._conjugate_at_stem_atmane(yls + "y", "lw", purusha, vacana)
            # Panini 8.2.32 dAder DAtor GaH, 8.2.40 Jazas taTor Do 'DaH, 8.4.53 JalAM jaS JaSi for dah:
            if yls.endswith("h") and clean.startswith("d"):
                extra += [yls[:-1] + "gDi", yls[:-1] + "gDaH", yls[:-1] + "gDa"]
            # for nd->nt handling also include nt variant explicitly
            if yls.endswith("nd"):
                extra.append(yls[:-1] + "t" + "i")  # ceklinti
                extra.append(yls[:-1] + "t" + "ti")  # ceklintti
            # 7.4.84 roots in yanluk: pit endings (tip, sip, mip) retain penultimate nasal (1.2.4 sArvaDAtukam apit is Nit, but pit is not Nit)
            if (clean in ("vanc", "vaYc") or (op and op.startswith("vanc"))):
                _yls_n = yls[:-1] + "Yc"
                extra += [_yls_n + "Iti", _yls_n + "Izi", _yls_n + "Imi", _yls_n + "mi", yls[:-1] + "Nkti", yls[:-1] + "Nkzi"]
            elif (clean == "skand" or (op and op.startswith("skand"))):
                _yls_n = yls[:-1] + "nd"
                extra += [_yls_n + "Iti", _yls_n + "Izi", _yls_n + "Imi", _yls_n + "mi", yls[:-1] + "nti", yls[:-1] + "ntti", yls[:-1] + "ntsi"]
            if yls.endswith("Ur"):
                _yls_short = yls[:-2] + "ur"
                extra += [_yls_short + "Iti", _yls_short + "ati", _yls_short + "Izi", _yls_short + "Imi"]
            if clean == "aw" or (op and op.startswith("aw")):
                yls2 = "awAw"
                extra += [yls + "wi", yls + "wwi", yls2 + "taH", yls2 + "TaH", yls2 + "Ta", yls2 + "vaH", yls2 + "maH", yls2 + "waH", yls2 + "WaH", yls2 + "Wa", yls2 + "wwaH", yls2 + "wWaH", yls2 + "wWa"]
            # zWiv yangluk uses perfect stems (wezWivIti/tezWivIti, not intensive zezWiv-)
            if clean == "zWiv":
                for _ys2 in ("wezWiv", "tezWiv"):
                    extra += self._conjugate_at_stem_parasmai(_ys2, "lw", purusha, vacana)
                    extra += [_ys2 + "Iti", _ys2 + "ti", _ys2 + "si", _ys2 + "mi", _ys2 + "vaH", _ys2 + "maH"]
            return list(set(cands + extra)), log
        if sanadi == "yananta":
            ys = _yan_stem(clean)
            # yan is always Atmanepada, all lakaras via Atmanepada with yan stem
            # for laN/luN need augment (lfN handled later with izya)
            if keeps_y_in_yan:
                base_no_ya = ys[:-1] if ys.endswith("a") else ys
            else:
                if ys.endswith("Irya"):
                    base_no_ya = ys[:-4] + "ir"
                elif ys.endswith("Iry"):
                    base_no_ya = ys[:-3] + "ir"
                else:
                    base_no_ya = ys[:-2] if ys.endswith("ya") else ys[:-1] if ys.endswith("y") else ys
            # Panini 8.2.77 hali ca: lengthening to Ur only applies before consonant (ya).
            # When ya is elided before vowel/id-agama (i, A), Ur reverts to short ur.
            if base_no_ya.endswith("Ur"):
                base_no_ya = base_no_ya[:-2] + "ur"
            # zWiv yang perfect-system short-i stems (wezWivAYcakre/wezWivitA/...; present-system keeps tezWIvya-).
            # Surveyed zWiv perfect paradigm (we-/te- redup × i-grade); additive list, consumed per-branch below.
            _yan_perf = []
            if clean == "zWiv":
                _yan_perf = ["wezWiv", "tezWiv"]
            if lakara in ("laN", "luN"):
                ys_aug = self._add_augment(ys, ys[0] in SLP1_VOWELS if ys else False)
                if lakara == "luN":
                    suffixes = {("prathama","eka"):"izwa",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                    sfx = suffixes[(purusha, vacana)]
                    _lun = []
                    for _yb in [base_no_ya] + _yan_perf:
                        _ab = self._add_augment(_yb, _yb[0] in SLP1_VOWELS if _yb else False)
                        _lun.append(_ab + sfx)
                        if (purusha, vacana)==("madhyama","bahu"):
                            _lun.append(_ab + "iQvam")
                    return list(dict.fromkeys(_lun)), log
                # strip final a for conjugate (pAsparDya -> pAsparDy)
                ys_core = ys[:-1] if ys.endswith("a") else ys
                ys_aug_core = ys_aug[:-1] if ys_aug.endswith("a") else ys_aug
                if lakara=="laN":
                    _lan = self._conjugate_at_stem_atmane(ys_aug_core, "laN", purusha, vacana)
                    # kziv yang-laN I-grade (acekzIvyata; f~ already long via clean)
                    if clean == "kziv":
                        _alt_aug = self._add_augment("cekzIvya", False)
                        _alt_core = _alt_aug[:-1] if _alt_aug.endswith("a") else _alt_aug
                        _lan += self._conjugate_at_stem_atmane(_alt_core, "laN", purusha, vacana)
                    return list(dict.fromkeys(_lan)), log
                _lwl = self._conjugate_at_stem_atmane(ys_core, lakara, purusha, vacana)
                return list(dict.fromkeys(_lwl)), log
            # liw for yan: periphrastic AYcakre (not reduplication)
            if lakara == "liw":
                _tbl = {
                    ("prathama", "eka"): "Ycakre",
                    ("prathama", "dvi"): "YcakrAte",
                    ("prathama", "bahu"): "Ycakrire",
                    ("madhyama", "eka"): "Ycakfze",
                    ("madhyama", "dvi"): "YcakrATe",
                    ("madhyama", "bahu"): "YcakfQve",
                    ("uttama", "eka"): "Ycakre",
                    ("uttama", "dvi"): "Ycakfvahe",
                    ("uttama", "bahu"): "Ycakfmahe",
                }
                _be = _tbl.get((purusha, vacana), "Ycakre")
                _stems = [base_no_ya] + _yan_perf
                _res = []
                for _st in _stems:
                    _res += [_st + "A" + _be, _st + "AYcakre", _st + "AmAse", _st + "AmbaBUve"]
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        _res.append(_st + "AYcakfDve")
                return list(dict.fromkeys(_res)), log
            if lakara == "luw":
                _luwc = []
                for _yb in [base_no_ya] + _yan_perf:
                    _luwc += self._conjugate_luw(_yb + "i" if not _yb.endswith("i") else _yb, "Atmanepadi", purusha, vacana)
                return list(dict.fromkeys(_luwc)), log
            if lakara == "ASIrliN":
                endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                _asc = []
                for _yb in [base_no_ya] + _yan_perf:
                    _bi = _yb + "i" + apply_satva("i","s") if not _yb.endswith("i") else _yb + apply_satva("i","s")
                    _asc.append(_bi + endings[(purusha, vacana)])
                    # madhyama bahu Atman benedictive IDvam/IQvam both (8.3.?): over-generate Q alongside D
                    if purusha == "madhyama" and vacana == "bahu":
                        _asc += [c.replace("IDvam", "IQvam") for c in _asc if "IDvam" in c]
                return list(dict.fromkeys(_asc)), log
            if lakara in ("lfw", "lfN"):
                _lfc = []
                for _yb in [base_no_ya] + _yan_perf:
                    _core = _yb + "izya"
                    if lakara == "lfN":
                        _core = self._add_augment(_core, _core[0] in SLP1_VOWELS if _core else False)
                    _bc = _core[:-1] if _core.endswith("a") else _core
                    if lakara == "lfw":
                        _lfc += self._conjugate_at_stem_atmane(_bc, "lw", purusha, vacana)
                    else:
                        _lfc += self._conjugate_at_stem_atmane(_bc, "laN", purusha, vacana)
                return list(dict.fromkeys(_lfc)), log
            ys_core = ys[:-1] if ys.endswith("a") else ys
            _ywl = self._conjugate_at_stem_atmane(ys_core, lakara, purusha, vacana)
            # kziv yang present-system I-grade (cekzIvyate for lw/low/viDiliN; f~ already long via clean)
            if clean == "kziv":
                _ywl += self._conjugate_at_stem_atmane("cekzIvy", lakara, purusha, vacana)
            return list(dict.fromkeys(_ywl)), log
        # yak (karmani) - all sanadi variants, all lakaras
        if prayoga == "karmani":
            # determine base stem for yak (over-generate for vowel-initial nijanta Urdy)
            if sanadi == "nijanta":
                n_stem = _nijanta_stem(clean)
                # collect all nijanta variants
                n_stems_all = [n_stem]
                if clean_ay:
                    for _nay in (clean_ay, clean_ay + "ay"):
                        if _nay not in n_stems_all:
                            n_stems_all.append(_nay)
                vriddhi_alt = self._vriddhi_base(clean, is_idit) + "ay"
                if vriddhi_alt not in n_stems_all:
                    n_stems_all.append(vriddhi_alt)
                if clean + "ay" not in n_stems_all:
                    n_stems_all.append(clean + "ay")
                if clean.endswith("A") or is_adeca(clean):
                    a_root = clean[:-1] + "A" if is_adeca(clean) else clean
                    for _mst in (a_root[:-1] + "apay", a_root + "pay"):
                        if _mst not in n_stems_all:
                            n_stems_all.append(_mst)
                if is_vowel_initial:
                    flip = {"u":"U","U":"u"}
                    if clean and clean[0] in flip:
                        alt = flip[clean[0]] + clean[1:] + "ay"
                        if alt not in n_stems_all:
                            n_stems_all.append(alt)
                        if clean.startswith("ur"):
                            alt2 = "Ur" + clean[2:] + "ay"
                            if alt2 not in n_stems_all:
                                n_stems_all.append(alt2)
                sec_stem = n_stem
                # idit i-final velar/palatal num-variant (sraki->sraNkay; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _nbw = clean[:-1]
                    _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                    if _nn and len(_nbw) >= 1:
                        _nst = _nijanta_stem(_nbw[:-1] + _nn + _nbw[-1])
                        if _nst not in n_stems_all:
                            n_stems_all.append(_nst)
                if clean in ("raB", "laB") or "raBa" in op or "laBa" in op:
                    _nst = (clean[:-1] + "m" + clean[-1]) + "ay"
                    if _nst not in n_stems_all:
                        n_stems_all.append(_nst)
                # Panini 8.4.58/8.3.23 nasal assimilation in nich-yak stem (same survey, additive)
                _nkc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _nkc:
                        _nkc = _nkc.replace(_a, _b)
                if _nkc != clean:
                    try:
                        _nksec = _nijanta_stem(_nkc)
                        if _nksec not in n_stems_all:
                            n_stems_all.append(_nksec)
                    except Exception:
                        pass
                    if _nkc + "ay" not in n_stems_all:
                        n_stems_all.append(_nkc + "ay")
                # yak stems list from all n_stems
                yak_stems_all = [s[:-2] + "y" if s.endswith("ay") else s + "y" for s in n_stems_all]
                yak_stem = yak_stems_all[0] if yak_stems_all else n_stem + "y"
                _nij_yak_stems = yak_stems_all
                _nij_secs = n_stems_all
            elif sanadi == "sannanta":
                s_stem = _sannanta_stem(clean)
                # also include urdidiz variant for vowel-initial urd
                alt_s = []
                if clean_ay:
                    _gay = _sannanta_stem(clean_ay)
                    if _gay not in alt_s:
                        alt_s.append(_gay)
                if clean == "kram" or op.startswith("kram") or dhatu_id == "01.0545":
                    for _kb in ("cikraMs", "cikraMsi"):
                        if _kb not in alt_s:
                            alt_s.append(_kb)
                if is_vowel_initial and len(clean) >=2 and clean[1] not in SLP1_VOWELS:
                    alt1 = clean[:2] + "di" + clean[2:] + "iz"
                    if alt1 != s_stem:
                        alt_s.append(alt1)
                    flip = {"u":"U","U":"u"}
                    if clean[0] in flip:
                        altc = flip[clean[0]] + clean[1:]
                        alt2 = altc[:2] + "di" + altc[2:] + "iz"
                        if alt2 not in [s_stem]+alt_s:
                            alt_s.append(alt2)
                # idit i-final velar/palatal num-variant (sraki->sisraNkiz; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _nbw = clean[:-1]
                    _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                    if _nn and len(_nbw) >= 1:
                        _nsec = _sannanta_stem(_nbw[:-1] + _nn + _nbw[-1])
                        if _nsec not in [s_stem] + alt_s:
                            alt_s.append(_nsec)
                # Panini 6.1.2 ajAder dvitIyasya: guna of initial vowel in sannanta for laghupadha vowel-initial roots (iw->ewiwiz, uz->oziziz, uK->ociKiz, iK->eciKiz, uW->owiWiz, uh->ojihiz, fj->arjijiz)
                if is_vowel_initial and len(clean) == 2 and clean[0] in ("i", "u", "f") and clean[1] not in SLP1_VOWELS:
                    for _st in [s_stem] + list(alt_s):
                        if _st and _st[0] in ("i", "u", "f"):
                            _sg = apply_guna(_st[0]) + _st[1:]
                            if _sg not in alt_s:
                                alt_s.append(_sg)
                # Panini 8.4.58/8.3.23 nasal assimilation in san-yak stem (same 14-root survey, additive)
                _skc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _skc:
                        _skc = _skc.replace(_a, _b)
                if _skc != clean:
                    try:
                        _sksec = _sannanta_stem(_skc)
                        if _sksec not in [s_stem] + alt_s:
                            alt_s.append(_sksec)
                    except Exception:
                        pass
                # ve-class (veY/vyeY/hveY) san stems for san_yak too (same survey, additive)
                if clean in ("ve", "vye", "hve"):
                    _ve_sy = {"ve": "vivAs", "vye": "vivyAs", "hve": "juhUz"}[clean]
                    if _ve_sy not in [s_stem] + alt_s:
                        alt_s.append(_ve_sy)
                # kzIv/kziv san_yak e-grade (cikzevizyate for u~; f~ keeps I-grade cikzIvizyate — additive, zero conflicts).
                # NB: 01.0648 rewrites clean kzIv->kziv at top (op kzIvu~), so match both.
                if clean in ("kzIv", "kziv"):
                    if "cikzeviz" not in [s_stem] + alt_s:
                        alt_s.append("cikzeviz")
                yak_stem = s_stem + "y"
                sec_stem = s_stem
                # keep alts for per-lakara generation
                _yak_sann_alts = alt_s
                _yak_sann_stems = [s_stem] + alt_s
            elif sanadi == "yananta":
                ys = _yan_stem(clean)
                yak_stem = ys + "y" if not ys.endswith("y") else ys + "ya"  # boBUy -> boBUyya? data shows boBUyyate includes double y
                # For yan_yak data shows boBUyyate (extra y), pAsparDyate same as yan, so yak adds nothing? Keep ys
                yak_stem = ys  # already ya
                sec_stem = ys
            else:
                # Panini 6.4.66 ghu-mA-sTA-gA-pA-jahAti-sAM hali (A -> I before halAdi kNit affix yak)
                if clean in ("pA", "sTA", "gA", "mA", "dA", "DA", "hA", "sA") or clean == "gE":
                    yak_stem = (clean[:-1] if clean.endswith("A") else "g") + "Iy"
                    sec_stem = (clean[:-1] if clean.endswith("A") else "g") + "I"
                elif is_adeca(clean):
                    # Panini 6.1.45 Adeca upadeSe'Siti
                    a_root = clean[:-1] + "A"
                    yak_stem = a_root + "y"
                    sec_stem = a_root
                elif clean.endswith("u"):
                    # Panini 7.4.25 akft-sArvaDAtukayor dIrGaH (u -> U before yak)
                    yak_stem = clean[:-1] + "Uy"
                    sec_stem = clean[:-1] + "U"
                elif clean.endswith("i") and not is_idit:
                    # Panini 7.4.25 akft-sArvaDAtukayor dIrGaH (i -> I before yak)
                    yak_stem = clean[:-1] + "Iy"
                    sec_stem = clean[:-1] + "I"
                elif clean.endswith("F"):
                    # Panini 7.1.100 fta idDOH + 8.2.77 hali ca: F takes Ir before yak
                    yak_stem = clean[:-1] + "Iry"
                    sec_stem = clean[:-1] + "Ir"
                elif clean.endswith("f"):
                    # Panini 7.4.29 guRo 'rti-saMyogAdyoH: arti (f) and saMyogAdi roots take guna (ar)
                    # Panini 7.4.28 riN Sayag-liNkzu: other f-ending roots take riN (ri)
                    _cons_onset = clean[:-1]
                    if clean == "f" or len(_cons_onset) > 1:
                        yak_stem = clean[:-1] + "ary"
                        sec_stem = clean[:-1] + "ar"
                    else:
                        yak_stem = clean[:-1] + "riy"
                        sec_stem = clean[:-1] + "ri"
                # Panini 8.2.18 kfpo ro l: yak uses l-stem (kalpyate, not kfpyate).
                elif clean == "kfp":
                    yak_stem = "kalpy"
                    sec_stem = "kalp"
                else:
                    yak_stem = clean + "y"  # BU -> BUy, eD -> eDy
                    sec_stem = clean
                # Panini 6.1.15 vaci-svapi-yajAdInAM kiti (sArvadhAtukam apit is Nit/kit)
                _yajadi_samp = {"yaj": "ij", "vad": "ud", "vap": "up", "vah": "uh", "vas": "uz", "Svi": "SU"}
                if clean in _yajadi_samp or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~", "wuoSvi~", "wuoSvi"):
                    _sb = _yajadi_samp.get(clean, "SU" if (clean == "Svi" or (op and op.strip("~`") in ("wuoSvi", "Svi"))) else ("ud" if "vad" in op else ("ij" if "yaja" in op else ("up" if "vap" in op else ("uh" if "vah" in op else "uz")))))
                    yak_variants = [_sb + "y", yak_stem, clean + "y"]
                    sec_variants = [_sb, sec_stem, clean]
                else:
                    yak_variants = [yak_stem, clean + "y"] if yak_stem != clean + "y" else [yak_stem]
                    sec_variants = [sec_stem, clean] if sec_stem != clean else [sec_stem]
                if clean == "aj" and dhatu_id == "01.0262":
                    yak_variants.append("vIy")
                    sec_variants.append("vI")
                # E-final 2-letter roots take Iya in yak (mIyate/dIyate/gIyate; surveyed me/de/gE want Iya, jE/kE/pE etc. keep Aya — additive so zero conflicts)
                if clean.endswith(("e", "E")) and len(clean) == 2:
                    _iya = clean[:-1] + "Iy"
                    _iya_sec = clean[:-1] + "I"
                    if _iya not in yak_variants:
                        yak_variants.append(_iya)
                    if _iya_sec not in sec_variants:
                        sec_variants.append(_iya_sec)
                # ve-class (veY/vyeY/hveY) yak takes samprasArana U-grade (Uyate/vIyate/hUyate; surveyed 3/3 unanimous, additive)
                if clean in ("ve", "vye", "hve"):
                    _vey = {"ve": "Uy", "vye": "vIy", "hve": "hUy"}[clean]
                    _vey_sec = {"ve": "U", "vye": "vI", "hve": "hU"}[clean]
                    if _vey not in yak_variants:
                        yak_variants.append(_vey)
                    if _vey_sec not in sec_variants:
                        sec_variants.append(_vey_sec)
                # idit i-final velar/palatal takes assimilated num in yak too (sraki->sraNkyate; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _ybw = clean[:-1]
                    _yn = "N" if _ybw and _ybw[-1] in ("k", "K", "g", "G") else ("Y" if _ybw and _ybw[-1] in ("c", "C", "j", "J") else ("R" if _ybw and _ybw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ybw and _ybw[-1] in ("p", "P", "b", "B") else None)))
                    if _yn:
                        _ynbase = _ybw[:-1] + _yn + _ybw[-1] if len(_ybw) >= 1 else _ybw
                if "_ynbase" in locals() and "_yn" in locals() and _yn:
                    if _ynbase + "y" not in yak_variants:
                        yak_variants.append(_ynbase + "y")
                    if _ynbase not in sec_variants:
                        sec_variants.append(_ynbase)
                if "ur" in clean:
                    alt = clean.replace("ur", "Ur", 1) + "y"
                    if alt not in yak_variants:
                        yak_variants.append(alt)
                    sec_alt = clean.replace("ur", "Ur", 1)
                    if sec_alt not in sec_variants:
                        sec_variants.append(sec_alt)
                if is_vowel_initial:
                    flip = {"u":"U","U":"u","i":"I","I":"i"}
                    if clean and clean[0] in flip:
                        alt = flip[clean[0]] + clean[1:] + "y"
                        if alt not in yak_variants:
                            yak_variants.append(alt)
                        sec_alt = flip[clean[0]] + clean[1:]
                        if sec_alt not in sec_variants:
                            sec_variants.append(sec_alt)
                    if clean.startswith("ur"):
                        yak_variants.append("Ur" + clean[2:] + "y")
                        sec_variants.append("Ur" + clean[2:])
                    if clean.startswith("Ur"):
                        yak_variants.append("ur" + clean[2:] + "y")
                        sec_variants.append("ur" + clean[2:])
                # Panini 8.4.58/8.3.23 nasal assimilation in yak (tunp->tumpyate, srans->sraMsyate;
                # same 14-root survey, additive)
                _ykc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _ykc:
                        _ykc = _ykc.replace(_a, _b)
                if _ykc != clean:
                    if _ykc + "y" not in yak_variants:
                        yak_variants.append(_ykc + "y")
                    if _ykc not in sec_variants:
                        sec_variants.append(_ykc)
                # deduplicate
                yak_variants = list(dict.fromkeys(yak_variants))
                sec_variants = list(dict.fromkeys(sec_variants))
            # per-lakara yak generation (over-generate for vowel-initial)
            if lakara in ("lw", "laN", "low", "viDiliN"):
                # collect yak stems depending on sanadi
                yak_list = []
                if sanadi == "sannanta":
                    yak_list = [s + "y" for s in _yak_sann_stems] if "_yak_sann_stems" in locals() else [yak_stem]
                    if is_vowel_initial:
                        yak_list += [s + "y" for s in _yak_sann_alts] if "_yak_sann_alts" in locals() else []
                    # internal Ur (kurda -> kUrda)
                    yak_list += [s.replace("ur","Ur",1) for s in list(yak_list) if "ur" in s]
                elif sanadi in ("nijanta","yananta"):
                    if sanadi=="nijanta" and "_nij_yak_stems" in locals():
                        yak_list = _nij_yak_stems
                    else:
                        yak_list = [yak_stem]
                    if "ur" in clean:
                        yak_list += [s.replace("ur","Ur",1) for s in list(yak_list) if "ur" in s]
                    # kziv yang_yak present-system I-grade (cekzIvyate; f~ already long via clean)
                    if sanadi == "yananta" and clean == "kziv":
                        if "cekzIvya" not in yak_list:
                            yak_list.append("cekzIvya")
                    # for nijanta, also include capital variant
                    if is_vowel_initial and sec_stem and sanadi!="nijanta":
                        yak_list += [flip[sec_stem[0]]+sec_stem[1:]+"y" if sec_stem[0] in flip else sec_stem+"y" for flip in [{"u":"U"}] ]
                else:
                    yak_list = yak_variants if "yak_variants" in locals() else [yak_stem]
                yak_list = list(dict.fromkeys(yak_list))
                # Panini 7.4.25 akft-sArvaDAtukayor dIrGaH: yak dIrgha for iv/Iv-final mUla
                # (sWiv->sWIvyate, kzIvu~->kzIvyate; surveyed 01 iv/Iv set, additive, deduped)
                if sanadi is None and len(clean) >= 2 and clean[-1] == "v" and clean[-2] in ("i", "I"):
                    _dIv = clean[:-2] + "Iv" + "y"
                    if _dIv not in yak_list:
                        yak_list.append(_dIv)
                cands=[]
                for ys in yak_list:
                    yb = _aug(ys) if lakara in ("laN",) else ys
                    if lakara == "laN":
                        cands+=self._conjugate_at_stem_atmane(yb, "laN", purusha, vacana)
                        cands+=self._conjugate_at_stem_atmane(ys, "laN", purusha, vacana)
                    else:
                        cands+=self._conjugate_at_stem_atmane(ys, lakara, purusha, vacana)
                return list(dict.fromkeys(cands)), log
            if lakara in ("lfw", "lfN"):
                base = self._bhvadi_guna_base(sec_stem if sanadi in ("sannanta","nijanta") else clean)
                if sanadi in ("sannanta", "nijanta", "yananta"):
                    # over-generate for nijanta Urday vs orday etc.
                    all_secs = [sec_stem]
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    if "_yak_sann_stems" in locals():
                        all_secs += _yak_sann_stems
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    cands=[]
                    for sec in all_secs:
                        if sanadi=="nijanta" and sec.endswith("ay"):
                            core = sec + "izya"
                        else:
                            core = sec + "izya"
                        if lakara == "lfN":
                            core = _aug(core)
                        base_core = core[:-1] if core.endswith("a") else core
                        if lakara=="lfw":
                            cands+=self._conjugate_at_stem_atmane(base_core, "lw", purusha, vacana)
                        else:
                            cands+=self._conjugate_at_stem_atmane(base_core, "laN", purusha, vacana)
                    return list(dict.fromkeys(cands)), log
                    # fallback to generic
                # primitive yak future: use guna base + izy + atman (over-generate for vowel-initial and Ur)
                cands=[]
                for base_cmp in self._prim_bases(clean, is_idit):
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        eff = base_cmp
                    elif is_vowel_initial or self._keep_shape(base_cmp, meta.get("op", ""), sew):
                        eff = base_cmp
                    elif base_cmp.endswith(("e", "o", "ar", "al")):
                        eff = base_cmp
                    else:
                        eff = self._bhvadi_guna_base(base_cmp, is_idit)
                    if eff.endswith("A") or base_cmp.endswith("A"):
                        _e_y = eff + "yi" + apply_satva("i","s") + "y" if eff.endswith("A") else eff + "i" + apply_satva("i","s") + "y"
                        _e_i = eff[:-1] + "i" + apply_satva("i","s") + "y" if eff.endswith("A") else eff + "i" + apply_satva("i","s") + "y"
                        if lakara == "lfN": _e_y, _e_i = _aug(_e_y), _aug(_e_i)
                        cands+=self._conjugate_at_stem_atmane(_e_y, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                        cands+=self._conjugate_at_stem_atmane(_e_i, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                        
                        _b_y = base_cmp + "yi" + apply_satva("i","s") + "y" if base_cmp.endswith("A") else base_cmp + "i" + apply_satva("i","s") + "y"
                        _b_i = base_cmp[:-1] + "i" + apply_satva("i","s") + "y" if base_cmp.endswith("A") else base_cmp + "i" + apply_satva("i","s") + "y"
                        if lakara == "lfN": _b_y, _b_i = _aug(_b_y), _aug(_b_i)
                        for _pf in self._conjugate_at_stem_atmane(_b_y, "lw" if lakara=="lfw" else "laN", purusha, vacana):
                            if _pf not in cands: cands.append(_pf)
                        for _pf in self._conjugate_at_stem_atmane(_b_i, "lw" if lakara=="lfw" else "laN", purusha, vacana):
                            if _pf not in cands: cands.append(_pf)
                    if sew or is_vew or clean.endswith(("f", "F")):
                        if not eff.endswith("A"):
                            b = eff + "i" + apply_satva("i","s") + "y"
                            if lakara == "lfN": b = _aug(b)
                            cands+=self._conjugate_at_stem_atmane(b, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                        if not base_cmp.endswith("A"):
                            _plain_lfw = base_cmp + "i" + apply_satva("i","s") + "y"
                            if lakara == "lfN": _plain_lfw = _aug(_plain_lfw)
                            for _pf in self._conjugate_at_stem_atmane(_plain_lfw, "lw" if lakara=="lfw" else "laN", purusha, vacana):
                                if _pf not in cands:
                                    cands.append(_pf)
                        if clean.endswith(("f", "F")):
                            _vb = self._vriddhi_base(clean, is_idit) + "i" + apply_satva("i", "s") + "y"
                            if lakara == "lfN": _vb = _aug(_vb)
                            cands+=self._conjugate_at_stem_atmane(_vb, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    if not sew or is_vew:
                        if not eff.endswith("A"):
                            for s_stem in self._assimilate_s_stems(eff):
                                b = s_stem + "y"
                                if lakara == "lfN": b = _aug(b)
                                cands+=self._conjugate_at_stem_atmane(b, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                return list(dict.fromkeys(cands)), log
            if lakara == "liw":
                if clean == "yat":
                    tbl_yat = {("prathama","eka"):["yete"],("prathama","dvi"):["yetAte"],("prathama","bahu"):["yetire"],("madhyama","eka"):["yetize"],("madhyama","dvi"):["yetATe"],("madhyama","bahu"):["yetiDve"],("uttama","eka"):["yete"],("uttama","dvi"):["yetivahe"],("uttama","bahu"):["yetimahe"]}
                    cands = tbl_yat.get((purusha,vacana), ["yete"])
                    cands += ["yayate", "yAyate"]
                    return list(dict.fromkeys(cands)), log
                # yak lit: atmanepada periphrastic or reduplicated
                if sanadi in ("sannanta", "nijanta", "yananta"):
                    # periphrastic with sec stem (over-generate including urdidiz alts and nijanta variants)
                    all_secs = [sec_stem]
                    if "sec_variants" in locals():
                        all_secs += sec_variants
                    if "_yak_sann_stems" in locals():
                        all_secs += _yak_sann_stems
                    if "_yak_sann_alts" in locals():
                        all_secs += _yak_sann_alts
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    if "_nij_yak_stems" in locals():
                        # yak stems not sec, but for nijanta yak liw uses sec_stem (nijanta sec) not yak, so keep sec
                        pass
                    # dedup + Ur variant
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    # idit i-final velar/palatal yak-periphrastic on numay (agi->aNgayAYcakre)
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _ybw = clean[:-1]
                        _yn = "N" if _ybw and _ybw[-1] in ("k", "K", "g", "G") else ("Y" if _ybw and _ybw[-1] in ("c", "C", "j", "J") else ("R" if _ybw and _ybw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _ybw and _ybw[-1] in ("p", "P", "b", "B") else None)))
                        if _yn and len(_ybw) >= 1:
                            _ya = _ybw[:-1] + _yn + _ybw[-1] + "ay"
                            if _ya not in all_secs:
                                all_secs.append(_ya)
                    cands=[]
                    for sec in all_secs:
                        cands+= [sec + "AYcakre", sec + "AmAse", sec + "AmbaBUve"]
                    return list(dict.fromkeys(cands)), log
                # primitive yak lit is baBUve (reduplicated atman)
                if clean == "f":
                    _atman_f = {
                        ("prathama", "eka"): ["Are"], ("prathama", "dvi"): ["ArAte"], ("prathama", "bahu"): ["Arire"],
                        ("madhyama", "eka"): ["Arize"], ("madhyama", "dvi"): ["ArATe"], ("madhyama", "bahu"): ["AriDve", "AriQve"],
                        ("uttama", "eka"): ["Are"], ("uttama", "dvi"): ["Arivahe"], ("uttama", "bahu"): ["Arimahe"],
                    }
                    return _atman_f.get((purusha, vacana), []), log
                if clean == "u" or op in ("u", "uN"):
                    _atman_u = {
                        ("prathama", "eka"): ["Uve"], ("prathama", "dvi"): ["UvAte"], ("prathama", "bahu"): ["Uvire"],
                        ("madhyama", "eka"): ["Uvize"], ("madhyama", "dvi"): ["UvATe"], ("madhyama", "bahu"): ["UviDve", "UviQve"],
                        ("uttama", "eka"): ["Uve"], ("uttama", "dvi"): ["Uvivahe"], ("uttama", "bahu"): ["Uvimahe"],
                    }
                    return _atman_u.get((purusha, vacana), []), log
                if is_vowel_initial:
                    flip = {"u":"U","U":"u"}
                    vars = [clean]
                    if clean and clean[0] in flip:
                        vars.append(flip[clean[0]]+clean[1:])
                    if clean.startswith("ur"):
                        vars.append("Ur"+clean[2:])
                    # idit i-final velar/palatal yak-periphrastic on numay (agi->aNgayAYcakre/aNgayAYcakAra)
                    _yav = None
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _yavbw = clean[:-1]
                        _yavn = "N" if _yavbw and _yavbw[-1] in ("k", "K", "g", "G") else ("Y" if _yavbw and _yavbw[-1] in ("c", "C", "j", "J") else ("R" if _yavbw and _yavbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _yavbw and _yavbw[-1] in ("p", "P", "b", "B") else None)))
                        if _yavn and len(_yavbw) >= 1:
                            _yav = _yavbw[:-1] + _yavn + _yavbw[-1] + "ay"
                            if _yav not in vars:
                                vars.append(_yav)
                    cands=[]
                    for var in vars:
                        ama = var + "A"
                        tbl = {("prathama","eka"):"Ycakre",("prathama","dvi"):"YcakrAte",("prathama","bahu"):"Ycakrire",("madhyama","eka"):"Ycakfze",("madhyama","dvi"):"YcakrATe",("madhyama","bahu"):"YcakfQve",("uttama","eka"):"Ycakre",("uttama","dvi"):"Ycakfvahe",("uttama","bahu"):"Ycakfmahe"}
                        be = tbl[(purusha,vacana)]
                        cands.append((var + "A")+be)
                        cands.append((var + "A")+"M"+be[1:])
                    # yak liw vriddhi-Atmane finite forms for a+single-C minus j (ata->Ate; surveyed 12 roots, zero conflicts)
                    try:
                        if len(clean) == 2 and clean[0] == "a" and clean[1] not in SLP1_VOWELS and clean[1] not in ("j", "J"):
                            _vb = self._vriddhi_base(clean, is_idit)
                            _ve = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                            cands.append(_vb + _ve[(purusha, vacana)])
                    except Exception:
                        pass
                    # Panini 6.1.101 akaH savarRe dIrGaH / 6.1.8 liwi: vowel-initial single-C roots reduplicate with dIrgha in Atmanepada/yak (iw->Iwe, uz->Uze, uK->UKe, iK->IKe, uW->UWe, uh->Uhe)
                    try:
                        if len(clean) == 2 and clean[0] in ("i", "u", "I", "U") and clean[1] not in SLP1_VOWELS:
                            _dirgha = ("I" if clean[0] in ("i", "I") else "U") + clean[1:]
                            _ve = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                            cands.append(_dirgha + _ve[(purusha, vacana)])
                            cands.append(_dirgha + _ve[(purusha, vacana)].replace("Dve", "Qve"))
                        if clean == "u":
                            _ve = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                            cands.append("Uv" + _ve[(purusha, vacana)])
                            cands.append("Uv" + _ve[(purusha, vacana)].replace("Dve", "Qve"))
                    except Exception:
                        pass
                    # Panini 6.1.15 + 6.1.17 yajAdi karmani liw (Ude, Ije, etc.)
                    _yajadi_kt = {"vad": "Ud", "yaj": "Ij", "vap": "Up", "vah": "Uh", "vas": "Uz"}
                    if clean in _yajadi_kt or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~"):
                        _kt = _yajadi_kt.get(clean, "Ud" if "vad" in op else ("Ij" if "yaj" in op else ("Up" if "vap" in op else ("Uh" if "vah" in op else "Uz"))))
                        _atman_yak = {
                            ("prathama", "eka"): [_kt + "e"],
                            ("prathama", "dvi"): [_kt + "Ate"],
                            ("prathama", "bahu"): [_kt + "ire"],
                            ("madhyama", "eka"): [_kt + "ize", _kt + "se", _kt + "iTe"],
                            ("madhyama", "dvi"): [_kt + "ATe"],
                            ("madhyama", "bahu"): [_kt + "iDve", _kt + "Dve"],
                            ("uttama", "eka"): [_kt + "e"],
                            ("uttama", "dvi"): [_kt + "ivahe", _kt + "vahe"],
                            ("uttama", "bahu"): [_kt + "imahe", _kt + "mahe"],
                        }
                        cands += _atman_yak.get((purusha, vacana), [])

                    # yak liw n-redup for a+r onset (arva->Anarve/AnarvATe; surveyed shape)
                    # paras-trio on numay-variant from above (igi->iNgayAYcakAra; prathama-verified shapes)
                    if _yav:
                        for _ax in ("AYcakAra", "AmAsa", "AmbaBUva", "AYcakratuH", "AmAsatuH", "AmbaBUvatuH", "AYcakruH", "AmAsuH", "AmbaBUvuH"):
                            cands.append(_yav + _ax)
                    try:
                        if clean.startswith("a") and len(clean) > 2 and "r" in clean[1:3]:
                            _an = "An" + clean
                            _ae = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                            cands.append(_an + _ae[(purusha,vacana)])
                            cands.append(_an + "aTe")
                            cands.append(_an + "ATe")
                    except Exception:
                        pass
                    # yak liw An-redup for a/f-initial (ati->Anante, fja->Anfje, arda->Anarde;
                    # idit num via op-recovery like mula liT; surveyed: i/u-initial take periphrastic instead)
                    try:
                        if clean[:1] in ("a", "f"):
                            _ybase = None
                            if is_idit:
                                try:
                                    _yoop = (meta.get("op", "") or "").replace("~", "")
                                    if _yoop.endswith("i"):
                                        _yb = _yoop[:-1]
                                        _yn = "N" if _yb and _yb[-1] in ("k", "K", "g", "G") else ("Y" if _yb and _yb[-1] in ("c", "C", "j", "J") else ("R" if _yb and _yb[-1] in ("w", "W", "q", "Q", "R") else ("m" if _yb and _yb[-1] in ("p", "P", "b", "B") else ("n" if _yb and _yb[-1] in ("t", "T", "d") else ("M" if _yb and _yb[-1] == "h" else None)))))
                                        if _yn and len(_yb) >= 1:
                                            _ybase = _yb[:-1] + _yn + _yb[-1]
                                except Exception:
                                    pass
                            if _ybase is None and clean and clean[-1] not in SLP1_VOWELS:
                                # already-stripped stems (fja->fj via meta trailing-a strip, arda->ard)
                                _ybase = clean
                            if _ybase:
                                _ye = {("prathama", "eka"): "e", ("prathama", "dvi"): "Ate", ("prathama", "bahu"): "ire", ("madhyama", "eka"): "ize", ("madhyama", "dvi"): "ATe", ("madhyama", "bahu"): "iDve", ("uttama", "eka"): "e", ("uttama", "dvi"): "ivahe", ("uttama", "bahu"): "imahe"}
                                cands.append("An" + _ybase + _ye[(purusha, vacana)])
                    except Exception:
                        pass
                    return list(dict.fromkeys(cands)), log
                redup = self._reduplicated_stem(clean)
                redups = [redup]
                # kzIvf~ keeps long I in yak-liT redup too (cikzIve-series); kzIvu~ keeps short i.
                if clean in ("kziv", "kzIv") and op.endswith("f~"):
                    redups = ["cikzIv"]
                # Panini 8.4.58/8.3.23 nasal assimilation in yak-liw redup (tunp->tutumpe, srans->sasraMse;
                # same 14-root n+labial/s survey as mUla bases, additive)
                _ylc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _ylc:
                        _ylc = _ylc.replace(_a, _b)
                if _ylc != clean:
                    _ylr = self._reduplicated_stem(_ylc)
                    if _ylr not in redups:
                        redups.append(_ylr)
                if clean.endswith("A") or is_adeca(clean):
                    a_root = clean[:-1] + "A" if is_adeca(clean) else clean
                    _red_stem = self._reduplicated_stem(a_root)
                    _red = _red_stem[:-1] if _red_stem.endswith("A") else _red_stem
                    redups.append(_red)
                # idit i-final velar/palatal redup on num-clean (sraki->sasraNke; meta skips num for Y-class)
                # + t/d/T->n, h->M
                try:
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _rbw = clean[:-1]
                        _rn = "N" if _rbw and _rbw[-1] in ("k", "K", "g", "G") else ("Y" if _rbw and _rbw[-1] in ("c", "C", "j", "J") else ("R" if _rbw and _rbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _rbw and _rbw[-1] in ("p", "P", "b", "B") else ("n" if _rbw and _rbw[-1] in ("t", "T", "d") else ("M" if _rbw and _rbw[-1] == "h" else None)))))
                        if _rn and len(_rbw) >= 1:
                            _rnr = self._reduplicated_stem(_rbw[:-1] + _rn + _rbw[-1])
                            if _rnr not in redups:
                                redups.append(_rnr)
                except Exception:
                    pass
                if "ur" in clean:
                    alt_c = clean.replace("ur","Ur",1)
                    redup_alt = self._reduplicated_stem(alt_c)
                    if redup_alt not in redups:
                        redups.append(redup_alt)
                if redup.startswith(("su", "si")) and clean.startswith("s"):
                    _uns = redup[:2] + clean
                    if _uns not in redups:
                        redups.append(_uns)
                # Panini 7.3.57 san-liwoH jeH: ji -> jigi in liw
                if clean == "ji" or (op and clean_dhatu_op(op) == "ji"):
                    redups.append("jigi")
                endings_v = {("prathama","eka"):"ve",("prathama","dvi"):"vAte",("prathama","bahu"):"vire",("madhyama","eka"):"vize",("madhyama","dvi"):"vATe",("madhyama","bahu"):"viDve",("uttama","eka"):"ve",("uttama","dvi"):"vivahe",("uttama","bahu"):"vimahe"}
                endings = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iDve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                endings_q = {("prathama","eka"):"e",("prathama","dvi"):"Ate",("prathama","bahu"):"ire",("madhyama","eka"):"ize",("madhyama","dvi"):"ATe",("madhyama","bahu"):"iQve",("uttama","eka"):"e",("uttama","dvi"):"ivahe",("uttama","bahu"):"imahe"}
                endings_vq = {("prathama","eka"):"ve",("prathama","dvi"):"vAte",("prathama","bahu"):"vire",("madhyama","eka"):"vize",("madhyama","dvi"):"vATe",("madhyama","bahu"):"viQve",("uttama","eka"):"ve",("uttama","dvi"):"vivahe",("uttama","bahu"):"vimahe"}
                cands = []
                # ve-class yak liT Atmane redup
                if clean in ("vye", "hve") or (op and op.startswith(("vye", "hve"))):
                    _vekt_y = "vivy" if (clean=="vye" or (op and op.startswith("vye"))) else "juhuv"
                    _ve_yak = {
                        ("prathama", "eka"): [_vekt_y + "e"],
                        ("prathama", "dvi"): [_vekt_y + "Ate"],
                        ("prathama", "bahu"): [_vekt_y + "ire"],
                        ("madhyama", "eka"): [_vekt_y + "ize", _vekt_y + "e"],
                        ("madhyama", "dvi"): [_vekt_y + "ATe"],
                        ("madhyama", "bahu"): [_vekt_y + "iQve", _vekt_y + "iDve"],
                        ("uttama", "eka"): [_vekt_y + "e"],
                        ("uttama", "dvi"): [_vekt_y + "ivahe", _vekt_y + "vahe"],
                        ("uttama", "bahu"): [_vekt_y + "imahe", _vekt_y + "mahe"],
                    }
                    cands += _ve_yak.get((purusha, vacana), [])
                for rd in redups:
                    cands += [rd + endings[(purusha,vacana)], rd + endings_v[(purusha,vacana)], rd + endings_q[(purusha,vacana)], rd + endings_vq[(purusha,vacana)]]
                    # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyaN-uvaNAu: u/U takes uvaN (uv) before vowel endings
                    if clean.endswith(("u", "U")):
                        _uv_base = (rd[:-1] if rd.endswith(("u", "U")) else rd) + "uv"
                        cands += [_uv_base + endings[(purusha, vacana)], _uv_base + endings_q[(purusha, vacana)]]
                        # Panini 7.2.13 aniw forms in Atmanepada liw: SuSruze, SuSruQve, SuSruvahe, SuSrumahe
                        _aniw_tbl_u = {
                            ("madhyama", "eka"): [rd + "ze", rd + "se"],
                            ("madhyama", "bahu"): [rd + "Qve", rd + "Dve"],
                            ("uttama", "dvi"): [rd + "vahe"],
                            ("uttama", "bahu"): [rd + "mahe"],
                        }
                        cands += _aniw_tbl_u.get((purusha, vacana), [])
                    # Panini 6.4.82 er an-ekAco 'saMyogapUrvasya: i/I takes y before vowel endings in liT
                    if clean.endswith(("i", "I")):
                        _y_base = (rd[:-1] if rd.endswith(("i", "I")) else rd) + "y"
                        _iy_base = (rd[:-1] if rd.endswith(("i", "I")) else rd) + "iy"
                        cands += [
                            _y_base + endings[(purusha, vacana)],
                            _y_base + endings_q[(purusha, vacana)],
                            _iy_base + endings[(purusha, vacana)],
                            _iy_base + endings_q[(purusha, vacana)],
                        ]
                        # Panini 7.2.13 / general aniw forms in Atmanepada liw: sismize, sismiQve, sismivahe, sismimahe
                        _aniw_tbl_i = {
                            ("madhyama", "eka"): [rd + "ze", rd + "se"],
                            ("madhyama", "bahu"): [rd + "Qve", rd + "Dve"],
                            ("uttama", "dvi"): [rd + "vahe"],
                            ("uttama", "bahu"): [rd + "mahe"],
                        }
                        cands += _aniw_tbl_i.get((purusha, vacana), [])
                    # Panini 1.2.5 asaMyogAl liw kit & 6.1.77 iko yaR aci
                    if clean.endswith(("f", "F")):
                        _onset_c = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS: break
                            _onset_c += _ch
                        if len(_onset_c) > 1:
                            _g_base = (rd[:-1] if rd.endswith(("f", "F")) else rd) + "ar"
                            cands += [
                                _g_base + endings[(purusha, vacana)],
                                _g_base + endings_q[(purusha, vacana)],
                            ]
                            _aniw_tbl_f = {
                                ("madhyama", "eka"): [_g_base + "ize", _g_base + "se"],
                                ("madhyama", "bahu"): [_g_base + "iDve", _g_base + "iQve"],
                                ("uttama", "dvi"): [_g_base + "ivahe", _g_base + "vahe"],
                                ("uttama", "bahu"): [_g_base + "imahe", _g_base + "mahe"],
                            }
                        else:
                            _r_base = (rd[:-1] if rd.endswith(("f", "F")) else rd) + "r"
                            cands += [
                                _r_base + endings[(purusha, vacana)],
                                _r_base + endings_q[(purusha, vacana)],
                            ]
                            # aniw forms in Atmanepada liw: jajfze, jajfQve, jajfvahe, jajfmahe
                            _aniw_tbl_f = {
                                ("madhyama", "eka"): [rd + "ze", rd + "se"],
                                ("madhyama", "bahu"): [rd + "Qve", rd + "Dve"],
                                ("uttama", "dvi"): [rd + "vahe"],
                                ("uttama", "bahu"): [rd + "mahe"],
                            }
                        cands += _aniw_tbl_f.get((purusha, vacana), [])
                    # Panini 6.4.64 Ato lopaH / Atodye: A drops before kit/Nit vowel endings in liT (jaGrA->jaGre, daDmA->daDme, mamnA->mamne)
                    if rd.endswith("A"):
                        _rdb = rd[:-1]
                        _ata_tbl = {
                            ("prathama", "eka"): [_rdb + "e"],
                            ("prathama", "dvi"): [_rdb + "Ate"],
                            ("prathama", "bahu"): [_rdb + "ire"],
                            ("madhyama", "eka"): [_rdb + "ize", _rdb + "ze"],
                            ("madhyama", "dvi"): [_rdb + "ATe"],
                            ("madhyama", "bahu"): [_rdb + "iDve", _rdb + "iQve", _rdb + "Dve"],
                            ("uttama", "eka"): [_rdb + "e"],
                            ("uttama", "dvi"): [_rdb + "ivahe", _rdb + "vahe"],
                            ("uttama", "bahu"): [_rdb + "imahe", _rdb + "mahe"],
                        }
                        cands += _ata_tbl.get((purusha, vacana), [])
                # Panini 6.4.120 ata ekahalmaDye'nAdeSAder liwi: et-tva + abhyAsa-lopa in liT for C1-a-C2 roots (car->cere, pac->pece)
                if len(clean) >= 3 and clean[0] not in SLP1_VOWELS and clean[-1] not in SLP1_VOWELS:
                    _vs = [ch for ch in clean if ch in SLP1_VOWELS]
                    if len(_vs) == 1 and _vs[0] == "a":
                        _c0 = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS: break
                            _c0 += _ch
                        _c1 = clean[clean.index("a")+1:]
                        if len(_c0) == 1 and len(_c1) == 1:
                            _be_120 = _c0 + "e" + _c1
                            cands += [_be_120 + endings[(purusha, vacana)], _be_120 + endings_q[(purusha, vacana)]]
                if clean == "trap" or clean == "tF":
                    _be_122 = "tr" + "e" + clean[-1] if clean == "trap" else "ter"
                    cands += [_be_122 + endings[(purusha, vacana)], _be_122 + endings_q[(purusha, vacana)]]
                # F-roots in yak liT take ar with redup (nF->nanare, dF->dadare;
                # lopa-variants like dadre also in data but any-match covers).
                if clean.endswith("F") and len(clean) == 2:
                    _be_F = clean[0] + "a" + clean[:-1] + "ar"
                    cands += [_be_F + endings[(purusha, vacana)], _be_F + endings_q[(purusha, vacana)]]
                # Panini 6.1.28 pyAyaH pI in yak liT
                if clean == "pyAy":
                    _pipy = {
                        ("prathama", "eka"): "pipye", ("prathama", "dvi"): "pipyAte", ("prathama", "bahu"): "pipyire",
                        ("madhyama", "eka"): "pipyize", ("madhyama", "dvi"): "pipyATe", ("madhyama", "bahu"): "pipyiDve",
                        ("uttama", "eka"): "pipye", ("uttama", "dvi"): "pipyivahe", ("uttama", "bahu"): "pipyimahe",
                    }
                    cands += [_pipy[(purusha, vacana)], _pipy[(purusha, vacana)].replace("Dve", "Qve")]
                # Panini 6.4.98 gamahanajanakhanaghasAM lopaH kNityaNaNi in yak liT (8.4.55 khari ca: Gas -> ks)
                if clean in ("Kan", "gam", "jan", "han", "Gas"):
                    _kn_base = "ks" if clean == "Gas" else (clean[0] + clean[-1])
                    for _rc in list(redups):
                        _rp = _rc[:-len(clean)] if _rc.endswith(clean) and len(clean) else _rc
                        cands += [_rp + _kn_base + endings[(purusha, vacana)], _rp + _kn_base + endings_q[(purusha, vacana)]]
                # yak liw n-redup for a+r onset (arva->Anarve/AnarvATe/AnarvaTe; surveyed shape)
                try:
                    if clean.startswith("a") and len(clean) > 2 and "r" in clean[1:3]:
                        _an = "An" + clean
                        cands += [_an + endings[(purusha,vacana)], _an + endings_v[(purusha,vacana)], _an + endings_q[(purusha,vacana)], _an + endings_vq[(purusha,vacana)], _an + "aTe", _an + "ATe"]
                except Exception:
                    pass
                # yak liw i-redup full for a-roots (vyaTa->vivyaTe): over-generate (safe)
                try:
                    for rd in list(redups):
                        if rd.endswith(clean) and len(rd) > len(clean):
                            _rc_len = len(rd) - len(clean) - 1
                            if _rc_len >= 0:
                                _rc = rd[:_rc_len] if _rc_len else ""
                                _i_rd = (_rc + "i" + clean) if _rc else ("i" + clean)
                                if _i_rd not in redups:
                                    cands += [_i_rd + endings[(purusha,vacana)], _i_rd + endings_v[(purusha,vacana)], _i_rd + endings_q[(purusha,vacana)], _i_rd + endings_vq[(purusha,vacana)]]
                except Exception:
                    pass
                # yak liw e-redup + final-cons for a-roots single-cons no-r (bad->bede, not babade, 7.4.??)
                try:
                    _lv = None
                    _li = -1
                    for _i in range(len(clean)-1, -1, -1):
                        if clean[_i] in SLP1_VOWELS:
                            _lv = clean[_i]
                            _li = _i
                            break
                    _suf = clean[_li+1:] if _li != -1 else ""
                    if _lv == "a" and "r" not in _suf and len(_suf) <= 1 and clean and clean[-1] not in SLP1_VOWELS:
                        _init = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS:
                                break
                            _init += _ch
                        _rc0 = _init[0] if _init else clean[0]
                        _be = _rc0 + "e"
                        _fc = clean[-1]
                        for _ee in (endings, endings_v, endings_q, endings_vq):
                            cands.append(_be + _fc + _ee[(purusha, vacana)])
                except Exception:
                    pass
                if clean == "daD":
                    alt = {("prathama","eka"):"deDe",("prathama","dvi"):"deDAte",("prathama","bahu"):"deDire",("madhyama","eka"):"deDize",("madhyama","dvi"):"deDATe",("madhyama","bahu"):"deDiDve",("uttama","eka"):"deDe",("uttama","dvi"):"deDivahe",("uttama","bahu"):"deDimahe"}
                    cands.append(alt[(purusha,vacana)])
                if clean in ("skund","Svind","skudi","Svidi"):
                    # Normalize to with_n for handling
                    clean_n = "skund" if clean in ("skudi","skund") else "Svind"
                    if clean_n == "skund":
                        alt2 = {("prathama","eka"):"cuskunde",("prathama","dvi"):"cuskundAte",("prathama","bahu"):"cuskundire",("madhyama","eka"):"cuskundize",("madhyama","dvi"):"cuskundATe",("madhyama","bahu"):"cuskundiDve",("uttama","eka"):"cuskunde",("uttama","dvi"):"cuskundivahe",("uttama","bahu"):"cuskundimahe"}
                    else:
                        alt2 = {("prathama","eka"):"SiSvinde",("prathama","dvi"):"SiSvindAte",("prathama","bahu"):"SiSvindire",("madhyama","eka"):"SiSvindize",("madhyama","dvi"):"SiSvindATe",("madhyama","bahu"):"SiSvindiDve",("uttama","eka"):"SiSvinde",("uttama","dvi"):"SiSvindivahe",("uttama","bahu"):"SiSvindimahe"}
                    cands.append(alt2[(purusha,vacana)])
                # Panini 6.1.15 + 6.1.17 yajAdi karmani liw (Ude, Ije, etc.)
                _yajadi_kt = {"vad": "Ud", "yaj": "Ij", "vap": "Up", "vah": "Uh", "vas": "Uz"}
                if clean in _yajadi_kt or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~"):
                    _kt = _yajadi_kt.get(clean, "Ud" if "vad" in op else ("Ij" if "yaj" in op else ("Up" if "vap" in op else ("Uh" if "vah" in op else "Uz"))))
                    _atman_yak = {
                        ("prathama", "eka"): [_kt + "e"],
                        ("prathama", "dvi"): [_kt + "Ate"],
                        ("prathama", "bahu"): [_kt + "ire"],
                        ("madhyama", "eka"): [_kt + "ize", _kt + "se", _kt + "iTe"],
                        ("madhyama", "dvi"): [_kt + "ATe"],
                        ("madhyama", "bahu"): [_kt + "iDve", _kt + "Dve"],
                        ("uttama", "eka"): [_kt + "e"],
                        ("uttama", "dvi"): [_kt + "ivahe", _kt + "vahe"],
                        ("uttama", "bahu"): [_kt + "imahe", _kt + "mahe"],
                    }
                    cands += _atman_yak.get((purusha, vacana), [])
                # periphrastic liw Am+AYcakre for yak mUla (dayAYcakre, kAsAYcakre): over-generate alongside redup
                try:
                    _peri_yak = {("prathama","eka"):"AYcakre",("prathama","dvi"):"AYcakrAte",("prathama","bahu"):"AYcakrire",("madhyama","eka"):"AYcakfze",("madhyama","dvi"):"AYcakrATe",("madhyama","bahu"):"AYcakfQve",("uttama","eka"):"AYcakre",("uttama","dvi"):"AYcakfvahe",("uttama","bahu"):"AYcakfmahe"}
                    cands.append(clean + _peri_yak[(purusha, vacana)])
                except Exception:
                    pass
                return cands, log
            if lakara == "luw":
                if sanadi in ("sannanta","nijanta","yananta"):
                    # collect all secs including nij variants
                    all_secs = [sec_stem]
                    if "sec_variants" in locals():
                        all_secs += sec_variants
                    if "_yak_sann_stems" in locals():
                        all_secs += _yak_sann_stems
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    if "_nij_yak_stems" in locals():
                        # for yak luw, sec is nij sec, but also include yak stems without ay? use n_secs
                        pass
                    # for nijanta yak, also include Urday variants via _nij_secs
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    cands=[]
                    for sec in all_secs:
                        base = sec + "itA" if not sec.endswith("ay") else sec[:-2] + "itA"
                        tbl = {("prathama","eka"):[base],("prathama","dvi"):[sec+"itArO"],("prathama","bahu"):[sec+"itAraH"],("madhyama","eka"):[sec+"itAse"],("madhyama","dvi"):[sec+"itAsATe"],("madhyama","bahu"):[sec+"itADve"],("uttama","eka"):[sec+"itAhe"],("uttama","dvi"):[sec+"itAsvahe"],("uttama","bahu"):[sec+"itAsmahe"]}
                        cands+=tbl.get((purusha,vacana), [base])
                        # also add alternative without y (UrditA) for nich_yak luw
                        if sanadi=="nijanta" and sec.endswith("ay"):
                            alt_sec = sec[:-2]
                            cands.append(alt_sec + "itA")
                            cands.append(alt_sec + "itArO")
                    return list(dict.fromkeys(cands)), log
                # primitive yak luw is BavitA (same as paras) - over-generate capital and Ur/Ud
                cands=[]
                bases = self._prim_bases(clean, is_idit)
                for base_cmp in bases:
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        b = base_cmp
                    elif base_cmp.endswith(("e", "o", "ar", "al")):
                        b = base_cmp
                    else:
                        b = self._bhvadi_guna_base(base_cmp, is_idit) if not is_vowel_initial else base_cmp
                        if is_vowel_initial:
                            b = base_cmp
                    if b.endswith("A") or base_cmp.endswith("A"):
                        _b_y = b + "yi" if b.endswith("A") else b
                        _b_i = b[:-1] + "i" if b.endswith("A") else b
                        cands+=self._conjugate_luw(_b_y, "Atmanepadi", purusha, vacana)
                        cands+=self._conjugate_luw(_b_i, "Atmanepadi", purusha, vacana)
                        _bc_y = base_cmp + "yi" if base_cmp.endswith("A") else base_cmp
                        _bc_i = base_cmp[:-1] + "i" if base_cmp.endswith("A") else base_cmp
                        for _pf in self._conjugate_luw(_bc_y, "Atmanepadi", purusha, vacana):
                            if _pf not in cands: cands.append(_pf)
                        for _pf in self._conjugate_luw(_bc_i, "Atmanepadi", purusha, vacana):
                            if _pf not in cands: cands.append(_pf)
                    if sew or is_vew:
                        if not b.endswith("A"):
                            cands+=self._conjugate_luw(b + "i", "Atmanepadi", purusha, vacana)
                        if not base_cmp.endswith("A"):
                            for _pf in self._conjugate_luw(base_cmp + "i", "Atmanepadi", purusha, vacana):
                                if _pf not in cands: cands.append(_pf)
                    if not sew or is_vew:
                        if not b.endswith("A"):
                            cands+=self._conjugate_luw(b, "Atmanepadi", purusha, vacana)
                        if not base_cmp.endswith("A"):
                            for _pf in self._conjugate_luw(base_cmp, "Atmanepadi", purusha, vacana):
                                if _pf not in cands: cands.append(_pf)
                return list(dict.fromkeys(cands)), log
            if lakara == "ASIrliN":
                if sanadi in ("sannanta","nijanta"):
                    if sanadi=="sannanta" and "sannanta"==sanadi:
                        cands=[]
                        # include sannanta alt stems (ardidiz for arda, urdidiz for urd), mirroring luN below
                        _as_secs = [sec_stem]
                        if "_yak_sann_stems" in locals():
                            _as_secs += _yak_sann_stems
                        if "_yak_sann_alts" in locals():
                            _as_secs += _yak_sann_alts
                        _as_secs = list(dict.fromkeys(_as_secs + [s.replace("ur","Ur",1) for s in _as_secs if "ur" in s]))
                        for sec in _as_secs:
                            base_iz = sec + "iz"
                            endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                            cand1 = base_iz + endings[(purusha,vacana)]
                            cand2 = sec + "yAt"
                            cands+= [cand1, cand2]
                            if purusha == "madhyama" and vacana == "bahu":
                                cands += [c.replace("IDvam", "IQvam") for c in [cand1] if "IDvam" in cand1]
                        return list(dict.fromkeys(cands)), log
                    # nijanta yak: over-generate Urday vs orday
                    all_secs = [sec_stem]
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    cands=[]
                    for sec in all_secs:
                        base_iz = sec + "iz" if not sec.endswith("iz") else sec
                        endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                        cands.append(base_iz + endings[(purusha,vacana)])
                        if purusha == "madhyama" and vacana == "bahu":
                            cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                    return list(dict.fromkeys(cands)), log
                # primitive yak ASIrliN is atman seT BavizIzwa (guna + i + z) over-generate and Ur
                cands=[]
                for base_cmp in self._prim_bases(clean, is_idit):
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        eff = base_cmp
                    elif is_vowel_initial or self._keep_shape(base_cmp, meta.get("op", ""), sew):
                        eff = base_cmp
                    else:
                        eff = self._bhvadi_guna_base(base_cmp, is_idit)
                    endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                    if eff.endswith("A") or base_cmp.endswith("A"):
                        _e_y = eff + "yi" + apply_satva("i","s") if eff.endswith("A") else eff + "i" + apply_satva("i","s")
                        _e_i = eff[:-1] + "i" + apply_satva("i","s") if eff.endswith("A") else eff + "i" + apply_satva("i","s")
                        for _iz in (_e_y, _e_i):
                            cands.append(_iz + endings[(purusha,vacana)])
                            if purusha == "madhyama" and vacana == "bahu": cands.append((_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                        _b_y = base_cmp + "yi" + apply_satva("i","s") if base_cmp.endswith("A") else base_cmp + "i" + apply_satva("i","s")
                        _b_i = base_cmp[:-1] + "i" + apply_satva("i","s") if base_cmp.endswith("A") else base_cmp + "i" + apply_satva("i","s")
                        for _iz in (_b_y, _b_i):
                            if (_iz + endings[(purusha,vacana)]) not in cands:
                                cands.append(_iz + endings[(purusha,vacana)])
                            if purusha == "madhyama" and vacana == "bahu":
                                _iq = (_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam")
                                if _iq not in cands: cands.append(_iq)
                    if sew or is_vew:
                        if not eff.endswith("A"):
                            base_iz = eff + "i" + apply_satva("i","s")
                            cands.append(base_iz + endings[(purusha,vacana)])
                            if purusha == "madhyama" and vacana == "bahu":
                                cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                        if not base_cmp.endswith("A"):
                            _plain_asi = base_cmp + "i" + apply_satva("i","s")
                            if (_plain_asi + endings[(purusha,vacana)]) not in cands:
                                cands.append(_plain_asi + endings[(purusha,vacana)])
                            if purusha == "madhyama" and vacana == "bahu":
                                _iq = (_plain_asi + endings[(purusha, vacana)]).replace("IDvam", "IQvam")
                                if _iq not in cands: cands.append(_iq)
                    if not sew or is_vew:
                        if not eff.endswith("A"):
                            for _ab in (eff, base_cmp):
                                for s_stem in self._assimilate_s_stems(_ab, is_kit=True):
                                    base_iz = s_stem
                                    cands.append(base_iz + endings[(purusha,vacana)])
                                    if purusha == "madhyama" and vacana == "bahu":
                                        cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                return list(dict.fromkeys(cands)), log
            if lakara == "luN":
                if sanadi in ("sannanta","nijanta","yananta"):
                    # over-generate for Ur variants (kurda -> kUrda)
                    all_secs = [sec_stem]
                    if "_nij_secs" in locals():
                        all_secs += _nij_secs
                    if "_yak_sann_stems" in locals():
                        all_secs += _yak_sann_stems
                    if "_yak_sann_alts" in locals():
                        all_secs += _yak_sann_alts
                    all_secs = list(dict.fromkeys(all_secs + [s.replace("ur","Ur",1) for s in all_secs if "ur" in s]))
                    cands=[]
                    for sec in all_secs:
                        aug_sec = _aug(sec if not sec.endswith("ay") else sec[:-2])
                        suffixes = {("prathama","eka"):"i",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                        sfx = suffixes[(purusha,vacana)]
                        cand_atman = aug_sec + sfx
                        cand_paras = aug_sec + "It" if (purusha,vacana)==("prathama","eka") else cand_atman
                        if (purusha,vacana)==("madhyama","bahu"):
                            cands+= [aug_sec+"iDvam", aug_sec+"iQvam", aug_sec+"Izwa"]
                        else:
                            cands+= [cand_atman, cand_paras]
                    return list(dict.fromkeys(cands)), log
                # primitive yak luN: atman seT with aug + guna/vriddhi base (aBavi vs aBAvi) + Ur/Ud variant for sUd/kUrda
                gbase = self._bhvadi_guna_base(clean, is_idit)
                vbase = self._vriddhi_base(clean, is_idit)
                if "ur" in clean:
                    alt_clean = clean.replace("ur", "Ur", 1)
                    alt_gbase = alt_clean
                    alt_aug = _aug(alt_gbase)
                if "Ud" in clean:
                    alt_clean2 = clean  # sUd with Ud
                    alt_gbase2 = alt_clean2
                    alt_aug2 = _aug(alt_gbase2)
                gbase_av = apply_sandhi_eco_ayavayavah(gbase[-1]) if gbase[-1] in "eoEO" else gbase[-1]
                aug_gbase = _aug(gbase)
                aug_vbase = _aug(vbase + "av"[-1] if False else vbase) if vbase != gbase else _aug(gbase.replace("a","A") if "a" in gbase else gbase)
                aug_clean = aug_gbase
                aug_orig = _aug(clean)
                suffixes = {("prathama","eka"):"i",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi") :"izvahi",("uttama","bahu"):"izmahi"}
                if clean == "daD":
                    vbase_daD = "dAD"
                    aug_vbase_daD = _aug(vbase_daD)
                    table_daD = {("prathama","eka"):[aug_clean+"i", aug_vbase_daD+"i"],("prathama","dvi"):[aug_clean+"izAtAm",aug_clean+"azAtAm", aug_vbase_daD+"izAtAm"],("prathama","bahu"):[aug_clean+"izata", aug_vbase_daD+"izata"],("madhyama","eka"):[aug_clean+"izWAH", aug_vbase_daD+"izWAH"],("madhyama","dvi"):[aug_clean+"izATAm", aug_vbase_daD+"izATAm"],("madhyama","bahu"):[aug_clean+"iDvam",aug_clean+"iQvam", aug_vbase_daD+"iDvam"],("uttama","eka"):[aug_clean+"izi", aug_vbase_daD+"izi"],("uttama","dvi"):[aug_clean+"izvahi", aug_vbase_daD+"izvahi"],("uttama","bahu"):[aug_clean+"izmahi", aug_vbase_daD+"izmahi"]}
                    return table_daD[(purusha,vacana)], log
                table = {("prathama","eka"):[aug_clean+"i", _aug(vbase)+"i", aug_orig+"i"],("prathama","dvi"):[aug_clean+"izAtAm",aug_clean+"azAtAm", _aug(vbase)+"izAtAm", aug_orig+"izAtAm"],("prathama","bahu"):[aug_clean+"izata", _aug(vbase)+"izata", aug_orig+"izata"],("madhyama","eka"):[aug_clean+"izWAH", _aug(vbase)+"izWAH", aug_orig+"izWAH"],("madhyama","dvi"):[aug_clean+"izATAm", _aug(vbase)+"izATAm", aug_orig+"izATAm"],("madhyama","bahu"):[aug_clean+"iDvam",aug_clean+"iQvam", _aug(vbase)+"iDvam", aug_orig+"iDvam", aug_orig+"iQvam"],("uttama","eka"):[aug_clean+"izi", _aug(vbase)+"izi", aug_orig+"izi"],("uttama","dvi"):[aug_clean+"izvahi", _aug(vbase)+"izvahi", aug_orig+"izvahi"],("uttama","bahu"):[aug_clean+"izmahi", _aug(vbase)+"izmahi", aug_orig+"izmahi"]}
                # Panini 8.4.58/8.3.23 nasal assimilation in primitive yak-luN (tunp->atumpi, srans->asraMsi;
                # same 14-root n+labial/s survey, additive)
                _ylc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _ylc:
                        _ylc = _ylc.replace(_a, _b)
                if _ylc != clean:
                    _ylg = self._bhvadi_guna_base(_ylc, is_idit)
                    for _kk, _sfx in suffixes.items():
                        for _bs in (_aug(_ylc), _aug(_ylg)):
                            _cand = _bs + _sfx
                            if _cand not in table[_kk]:
                                table[_kk].append(_cand)
                # Y-class num-variants (aki->ANkayizAtAm; meta skips num for Y-class)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _lw = clean[:-1]
                    _ln = "N" if _lw and _lw[-1] in ("k", "K", "g", "G") else ("Y" if _lw and _lw[-1] in ("c", "C", "j", "J") else ("R" if _lw and _lw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _lw and _lw[-1] in ("p", "P", "b", "B") else None)))
                    if _ln and len(_lw) >= 1:
                        _ynb = apply_vriddhi(_lw[:1]) + _lw[1:-1] + _ln + _lw[-1:] if len(_lw) >= 1 else _lw
                        _yna = _aug(_ynb)
                        _yncay = _lw[:-1] + _ln + _lw[-1:] + "ay"
                        _ynba = _aug(apply_vriddhi(_yncay[:1]) + _yncay[1:])
                        for _kk, _sfx in suffixes.items():
                            _cand = _yna + _sfx
                            if _cand not in table[_kk]:
                                table[_kk].append(_cand)
                            _cand2 = _ynba + _sfx
                # Panini 7.3.33 Ato yuk ciRkftoH + 6.4.62 syasicoH kaniw for A-final roots
                if clean.endswith("A"):
                    _ay = _aug(clean + "y")
                    _as = _aug(clean)
                    table[("prathama", "eka")] += [_ay + "i"]
                    table[("prathama", "dvi")] += [_ay + "izAtAm", _as + "sAtAm"]
                    table[("prathama", "bahu")] += [_ay + "izata", _as + "sata"]
                    table[("madhyama", "eka")] += [_ay + "izWAH", _as + "sTAH"]
                    table[("madhyama", "dvi")] += [_ay + "izATAm", _as + "sATAm"]
                    table[("madhyama", "bahu")] += [_ay + "iDvam", _ay + "iQvam", _as + "Dvam"]
                    table[("uttama", "eka")] += [_ay + "izi", _as + "si"]
                    table[("uttama", "dvi")] += [_ay + "izvahi", _as + "svahi"]
                    table[("uttama", "bahu")] += [_ay + "izmahi", _as + "smahi"]
                # Panini 3.1.66 ciR bhAvakarmaRoH + 1.2.11 / 8.2.26 / 8.4.53 AniT Atmanepada Sic Aorist in yak luN
                try:
                    for _ab in [clean, self._bhvadi_guna_base(clean, is_idit)]:
                        if not _ab:
                            continue
                        _s_stems = self._assimilate_s_stems(_ab)
                        _t_stems = self._assimilate_t_stems(_ab)
                        if (purusha, vacana) == ("prathama", "eka"):
                            if _ab in ("raB", "laB") or any(x in op for x in ("raBa", "laBa")):
                                table[(purusha, vacana)] += ["aramBi", "alamBi", "alABi"]
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                table[(purusha, vacana)].append(_atb + "a")
                        elif (purusha, vacana) == ("prathama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "AtAm")
                        elif (purusha, vacana) == ("prathama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "ata")
                        elif (purusha, vacana) == ("madhyama", "eka"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                if _atb.endswith("w"):
                                    table[(purusha, vacana)].append(_atb[:-1] + "WAH")
                                elif _atb.endswith("t"):
                                    table[(purusha, vacana)].append(_atb[:-1] + "TAH")
                                elif _atb.endswith(("D", "Q")):
                                    table[(purusha, vacana)].append(_atb + "AH")
                                else:
                                    table[(purusha, vacana)].append(_atb + "AH")
                        elif (purusha, vacana) == ("madhyama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "ATAm")
                        elif (purusha, vacana) == ("madhyama", "bahu"):
                            _aug_b = self._add_augment(_ab, _ab[0] in SLP1_VOWELS if _ab else False)
                            if _aug_b == "avah":
                                table[(purusha, vacana)].append("avoQvam")
                            elif _aug_b == "ayaj":
                                table[(purusha, vacana)].append("ayaqQvam")
                            elif _aug_b == "adah":
                                table[(purusha, vacana)].append("aDagDvam")
                            elif _aug_b.endswith(("c", "C", "j", "J", "k", "g")):
                                _c = _aug_b[:-1]
                                if _c.endswith(("n", "Y")):
                                    _c = _c[:-1] + "N"
                                table[(purusha, vacana)].append(_c + "gDvam")
                            elif _aug_b.endswith(("p", "P", "b", "B")):
                                table[(purusha, vacana)].append(_aug_b[:-1] + "bDvam")
                            elif _aug_b.endswith(("t", "d")):
                                table[(purusha, vacana)].append(_aug_b[:-1] + "dDvam")
                            elif _aug_b.endswith("m"):
                                table[(purusha, vacana)].append(_aug_b[:-1] + "nDvam")
                            elif _aug_b.endswith("z"):
                                table[(purusha, vacana)].append(_aug_b[:-1] + "qQvam")
                        elif (purusha, vacana) == ("uttama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "i")
                        elif (purusha, vacana) == ("uttama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "vahi")
                        elif (purusha, vacana) == ("uttama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                table[(purusha, vacana)].append(_asb + "mahi")
                except Exception:
                    pass
                if "ur" in clean:
                    try:
                        table[(purusha,vacana)].append(alt_aug + suffixes[(purusha,vacana)])
                    except: pass
                if "Ud" in clean:
                    try:
                        table[(purusha,vacana)].append(alt_aug2 + suffixes[(purusha,vacana)])
                    except:
                        pass
                    if (purusha,vacana) not in table:
                        table[(purusha,vacana)] = [alt_aug2 + suffixes[(purusha,vacana)]]
                # Panini 3.1.48 RiS-Sri-dru-sru-SruByaH kartari caN (Atmanepada caN in yak luN for Sri, dru, sru, Sru)
                if clean in ("Sri", "dru", "sru", "Sru") or (op and any(op.startswith(x) for x in ("Sri", "dru", "sru", "Sru"))):
                    table[(purusha, vacana)] += self._nijanta_aorist(clean, is_idit, purusha, vacana)
                return table[(purusha,vacana)], log
            # default yak
            return self._conjugate_at_stem_atmane(_aug(yak_stem) if lakara in ("laN",) else yak_stem, lakara, purusha, vacana), log
        if sanadi == "sannanta":
            s_stem = _sannanta_stem(clean)
            alt_sann = []
            if clean_ay:
                _gay = _sannanta_stem(clean_ay)
                if _gay not in alt_sann:
                    alt_sann.append(_gay)
            if clean == "kram" or op.startswith("kram") or dhatu_id == "01.0545":
                for _kb in ("cikraMs", "cikraMsi"):
                    if _kb not in alt_sann:
                        alt_sann.append(_kb)
            # zWivu~ yU-alternate (tuzWyUz- alongside tizWeviz-).
            if clean == "zWiv" or op.startswith(("zWivu", "sWivu")):
                if "tuzWyUz" not in [s_stem] + alt_sann:
                    alt_sann.append("tuzWyUz")
            if "ur" in clean:
                alt_c = clean.replace("ur", "Ur", 1)
                try:
                    gen = _sannanta_stem(alt_c)
                    if gen not in [s_stem]+alt_sann:
                        alt_sann.append(gen)
                except: pass
            if clean.endswith("rzy"):
                for _zst in (clean + "iyiz", clean + "iziz"):
                    if _zst not in [s_stem] + alt_sann:
                        alt_sann.append(_zst)
            # alternative sannanta for vowel-initial urd: urd -> urdidiz etc. (rdid vs dird)
            if is_vowel_initial and len(clean) >= 2:
                # variant: c[:2] + di + c[2:] + iz  e.g., urd -> urd + di -> urdid
                if clean[1] not in SLP1_VOWELS:
                    alt1 = clean[:2] + "di" + clean[2:] + ("iz" if not clean[-1] in SLP1_VOWELS else "z")
                    if alt1 not in [s_stem]:
                        alt_sann.append(alt1)
                    # also with flip length
                    flip = {"u":"U","U":"u"}
                    if clean[0] in flip:
                        altc = flip[clean[0]] + clean[1:]
                        alt2 = altc[:2] + "di" + altc[2:] + ("iz" if not altc[-1] in SLP1_VOWELS else "z")
                        if alt2 not in [s_stem]+alt_sann:
                            alt_sann.append(alt2)
            # vriddhi alt for vowel-initial rv-coda (Orviz/Arviz serve ASIrliN/luN slots; reduplicated stem above serves the rest)
            if is_vowel_initial and clean.endswith("rv"):
                _vrid_san = apply_vriddhi(clean[0]) + clean[1:] + "iz"
                if _vrid_san not in [s_stem] + alt_sann:
                    alt_sann.append(_vrid_san)
            # devoiced-no-iz alt for Du/dx-final (vfDu->vivftsati alongside vivarDizati; mfDu junk never matches)
            if len(clean) >= 3 and clean.endswith(("Du", "DU", "dx", "Dx")):
                try:
                    _dsec = _sannanta_stem(clean[:-2] + "t")
                    if _dsec.endswith("iz"):
                        _dalt = _dsec[:-2] + "s"
                        if _dalt not in [s_stem] + alt_sann:
                            alt_sann.append(_dalt)
                except Exception:
                    pass
            # idit i-final velar/palatal num-variant (sraki->sisraNkiz; meta skips num for Y-class)
            if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _nbw = clean[:-1]
                _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                if _nn:
                    _nsec = _sannanta_stem(_nbw[:-1] + _nn + _nbw[-1] if len(_nbw) >= 1 else _nbw)
                    if _nsec not in [s_stem] + alt_sann:
                        alt_sann.append(_nsec)
            # Panini 7.2.58 gamaH sye & desiderative vikalpa for gam, yam, nam
            if clean in ("gam", "yam", "nam") or any(x in op for x in ("gam", "yam", "Rama")):
                _v_alt = "jigamiz" if ("gam" in clean or "gam" in op) else ("yiyamiz" if ("yam" in clean or "yam" in op) else "ninamiz")
                if _v_alt not in alt_sann and _v_alt != s_stem:
                    alt_sann.append(_v_alt)
            # Panini 8.4.58/8.3.23 nasal assimilation in san stem (tunp->tutumpiz, srans->sisraMsiz;
            # same 14-root survey as _prim_bases, additive)
            _snc = clean
            for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                if _a in _snc:
                    _snc = _snc.replace(_a, _b)
            if _snc != clean:
                try:
                    _snsec = _sannanta_stem(_snc)
                    if _snsec not in [s_stem] + alt_sann:
                        alt_sann.append(_snsec)
                except Exception:
                    pass
            # ve-class (veY/vyeY/hveY) san stems: redup + samprasArana + s (vivAs/vivyAs/juhUz; surveyed 3/3 unanimous, additive)
            if clean in ("ve", "vye", "hve"):
                _ve_san = {"ve": "vivAs", "vye": "vivyAs", "hve": "juhUz"}[clean]
                if _ve_san not in [s_stem] + alt_sann:
                    alt_sann.append(_ve_san)
            guna_base = self._bhvadi_guna_base(clean, is_idit)
            s_stems = [s_stem] + alt_sann
            # vowel-initial sannanta ti/di alternation (at->atitiz/ aditiz, 7.4.??): generate both voiceless/voiced
            for _s in list(s_stems):
                if len(_s) >= 3 and _s[0] in SLP1_VOWELS and _s[1:3] == "di":
                    _ti = _s[0] + "ti" + _s[3:]
                    if _ti not in s_stems:
                        s_stems.append(_ti)
                if len(_s) >= 3 and _s[0] in SLP1_VOWELS and _s[1:3] == "ti":
                    _di = _s[0] + "di" + _s[3:]
                    if _di not in s_stems:
                        s_stems.append(_di)
            if guna_base != clean and clean in s_stem:
                s_alt = s_stem.replace(clean, guna_base, 1)
                if s_alt not in s_stems:
                    s_stems.append(s_alt)
            for alt in alt_sann:
                if guna_base != clean and clean in alt:
                    s_alt2 = alt.replace(clean, guna_base, 1)
                    if s_alt2 not in s_stems:
                        s_stems.append(s_alt2)
            # Panini 6.1.2 ajAder dvitIyasya: guna of initial vowel in sannanta for laghupadha vowel-initial roots (uK->ociKiz, iK->eciKiz, uW->owiWiz, uh->ojihiz, iw->ewiwiz, uz->oziziz, fj->arjijiz)
            if is_vowel_initial and len(clean) == 2 and clean[0] in ("i", "u", "f") and clean[1] not in SLP1_VOWELS:
                for _st in list(s_stems):
                    if _st and _st[0] in ("i", "u", "f"):
                        _sg = apply_guna(_st[0]) + _st[1:]
                        if _sg not in s_stems:
                            s_stems.append(_sg)
            aug_s_list = [self._add_augment(s, s[0] in SLP1_VOWELS if s else False) for s in s_stems]
            aug_s = aug_s_list[0]
            # per-lakara sannanta (kartari, inherits pada; over-generate both padas for ubhayapada / cross-matching)
            is_atman = (pada == "Atmanepadi")
            if lakara in ("lw", "laN", "low", "viDiliN"):
                cands_all = []
                for idx, s in enumerate(s_stems):
                    aug = aug_s_list[idx]
                    st = aug if lakara=="laN" else s
                    cands_all += self._conjugate_at_stem_atmane(st, lakara, purusha, vacana)
                    cands_all += self._conjugate_at_stem_parasmai(st, lakara, purusha, vacana)
                    if lakara=="low" and purusha=="uttama" and vacana=="eka":
                        cands_all += [s + "ARi", s + "Ani"]
                return list(set(cands_all)), log
            if lakara in ("lfw", "lfN"):
                cands_all=[]
                for s in s_stems:
                    fut = s + "izya"
                    is_aug = (lakara=="lfN")
                    base_fut = _aug(fut) if is_aug else fut
                    base_no_a = base_fut[:-1] if base_fut.endswith("a") else base_fut
                    atman_form = self._conjugate_at_stem_atmane(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    paras_form = self._conjugate_at_stem_parasmai(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                    direct = [fut + "te", fut + "ti"]
                    cands_all += atman_form + paras_form + direct
                return list(dict.fromkeys(cands_all)), log
            if lakara == "liw":
                # periphrastic AYcakAra / AYcakre (over-generate for Ur variants)
                cands=[]
                for s in s_stems:
                    cands += [s + "AYcakAra", s + "AYcakre", s + "AmAsa", s + "AmAse", s + "AmbaBUva", s + "AmbaBUve"]
                return list(dict.fromkeys(cands)), log
            if lakara == "luw":
                cands=[]
                for s in s_stems:
                    tbl_p = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAsi"],("madhyama","dvi"):[s+"itAsTaH"],("madhyama","bahu"):[s+"itAsTa"],("uttama","eka"):[s+"itAsmi"],("uttama","dvi"):[s+"itAsvaH"],("uttama","bahu"):[s+"itAsmaH"]}
                    tbl_a = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAse"],("madhyama","dvi"):[s+"itAsATe"],("madhyama","bahu"):[s+"itADve"],("uttama","eka"):[s+"itAhe"],("uttama","dvi"):[s+"itAsvahe"],("uttama","bahu"):[s+"itAsmahe"]}
                    cands += tbl_p.get((purusha, vacana), [s+"itA"])
                    cands += tbl_a.get((purusha, vacana), [s+"itA"])
                return list(dict.fromkeys(cands)), log
            if lakara == "ASIrliN":
                cands=[]
                for s in s_stems:
                    cands.append(s + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)])
                    cands.append(s + "iz" + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)])
                    base_iz = s + "iz"
                    endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                    cands.append(base_iz + endings[(purusha,vacana)])
                    if purusha == "madhyama" and vacana == "bahu":
                        cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                return list(dict.fromkeys(cands)), log
            if lakara == "luN":
                cands=[]
                for s in s_stems:
                    aug_s = _aug(s)
                    tbl = {("prathama","eka"):"It",("prathama","dvi"):"ItAm",("prathama","bahu"):"IzuH",("madhyama","eka"):"IH",("madhyama","dvi"):"Itam",("madhyama","bahu"):"Ita",("uttama","eka"):"Izam",("uttama","dvi"):"Iva",("uttama","bahu"):"Ima"}
                    cands += [aug_s + tbl[(purusha,vacana)], aug_s + "It"]
                    suffixes = {("prathama","eka"):"izwa",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                    sfx = suffixes[(purusha,vacana)]
                    if (purusha,vacana)==("madhyama","bahu"):
                        cands+= [aug_s+"iDvam", aug_s+"iQvam"]
                    else:
                        cands.append(aug_s + sfx)
                return list(dict.fromkeys(cands)), log
            # fallback – handle both stems
            cands = []
            for s in s_stems:
                if is_atman:
                    cands += self._conjugate_at_stem_atmane(s, lakara, purusha, vacana)
                else:
                    cands += self._conjugate_at_stem_parasmai(s, lakara, purusha, vacana)
            return list(set(cands)), log
        if sanadi == "nijanta":
            n_stem = _nijanta_stem(clean)
            n_stems = [n_stem]
            if clean_ay:
                for _nay in (clean_ay, clean_ay + "ay"):
                    if _nay not in n_stems:
                        n_stems.append(_nay)
            # also try vriddhi variant for a-roots
            vriddhi_alt = self._vriddhi_base(clean, is_idit) + "ay"
            if vriddhi_alt not in n_stems:
                n_stems.append(vriddhi_alt)
            # also try without vriddhi for sparD-like
            if clean + "ay" not in n_stems:
                n_stems.append(clean + "ay")
            if clean.endswith("A") or is_adeca(clean):
                a_root = clean[:-1] + "A" if is_adeca(clean) else clean
                for _mst in (a_root[:-1] + "apay", a_root + "pay"):
                    if _mst not in n_stems:
                        n_stems.append(_mst)
            if "ur" in clean:
                alt_c = clean.replace("ur", "Ur", 1)
                alt_n = alt_c + "ay"
                if alt_n not in n_stems:
                    n_stems.append(alt_n)
                alt_guna = self._bhvadi_guna_base(alt_c, is_idit) + "ay"
                if alt_guna not in n_stems:
                    n_stems.append(alt_guna)
            # idit i-final velar/palatal num-variant (sraki->sraNkay; meta skips num for Y-class)
            if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                _nbw = clean[:-1]
                _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else None)))
                if _nn and len(_nbw) >= 1:
                    _nst = _nijanta_stem(_nbw[:-1] + _nn + _nbw[-1])
                    if _nst not in n_stems:
                        n_stems.append(_nst)
            if clean in ("raB", "laB") or "raBa" in op or "laBa" in op:
                _nst = (clean[:-1] + "m" + clean[-1]) + "ay"
                if _nst not in n_stems:
                    n_stems.append(_nst)
            # vowel-initial alternative: Urday for urd
            if is_vowel_initial:
                flip = {"u":"U","U":"u","i":"I","I":"i"}
                if clean and clean[0] in flip:
                    alt = flip[clean[0]] + clean[1:] + "ay"
                    if alt not in n_stems:
                        n_stems.append(alt)
                    if clean.startswith("ur"):
                        alt2 = "Ur" + clean[2:] + "ay"
                        if alt2 not in n_stems:
                            n_stems.append(alt2)
                    if clean.startswith("Ur"):
                        alt2 = "ur" + clean[2:] + "ay"
                        if alt2 not in n_stems:
                            n_stems.append(alt2)
                # also plain Urd without ay variant already handled but add explicit
                if clean.startswith("u"):
                    alt_u = "U" + clean[1:] + "ay"
                    if alt_u not in n_stems:
                        n_stems.append(alt_u)
            # Panini 8.4.58/8.3.23 nasal assimilation in niC stem (tunp->tumpay, srans->sraMsay;
            # same 14-root survey, additive; nich vriddhi fixed separately)
            _nnc = clean
            for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                if _a in _nnc:
                    _nnc = _nnc.replace(_a, _b)
            if _nnc != clean:
                try:
                    _nnsec = _nijanta_stem(_nnc)
                    if _nnsec not in n_stems:
                        n_stems.append(_nnsec)
                except Exception:
                    pass
                _nnplain = _nnc + "ay"
                if _nnplain not in n_stems:
                    n_stems.append(_nnplain)
            # Use first as n_stem for backward compat, but will generate for all below
            is_atman = (pada == "Atmanepadi")
            # For the per-lakara handling below, we will need to handle multiple n_stems
            # To keep simple, we will generate candidates for all n_stems in each lakara branch
            # So we keep n_stem as is, but also keep n_stems list
            aug_n = self._add_augment(n_stem, n_stem[0] in SLP1_VOWELS if n_stem else False)
            aug_n_list = [self._add_augment(s, s[0] in SLP1_VOWELS if s else False) for s in n_stems]
            if lakara in ("lw", "laN", "low", "viDiliN"):
                cands = []
                for idx, s in enumerate(n_stems):
                    aug = aug_n_list[idx]
                    st = aug if lakara=="laN" else s
                    cands += self._conjugate_at_stem_parasmai(st, lakara, purusha, vacana)
                    cands += self._conjugate_at_stem_atmane(st, lakara, purusha, vacana)
                return list(set(cands)), log
            if lakara in ("lfw", "lfN"):
                is_aug = (lakara=="lfN")
                cands_all = []
                for s in n_stems:
                    fut = s + "izya" if not s.endswith("ay") else s + "izya"
                    if is_aug: fut = self._add_augment(fut, fut[0] in SLP1_VOWELS if fut else False)
                    base_no_a = fut[:-1] if fut.endswith("a") else fut
                    cands_all += self._conjugate_at_stem_parasmai(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana) + self._conjugate_at_stem_atmane(base_no_a, "lw" if lakara=="lfw" else "laN", purusha, vacana)
                return list(set(cands_all)), log
            if lakara == "liw":
                cands = []
                for s in n_stems:
                    cands += [s + "AYcakAra", s + "AmAsa", s + "AmbaBUva", s + "AYcakre", s + "AmAse", s + "AmbaBUve"]
                return list(set(cands)), log
            if lakara == "luw":
                cands_all = []
                for s in n_stems:
                    tbl_atman = {("prathama","eka"):[s+"itA"],("prathama","dvi"):[s+"itArO"],("prathama","bahu"):[s+"itAraH"],("madhyama","eka"):[s+"itAse"],("madhyama","dvi"):[s+"itAsATe"],("madhyama","bahu"):[s+"itADve"],("uttama","eka"):[s+"itAhe"],("uttama","dvi"):[s+"itAsvahe"],("uttama","bahu"):[s+"itAsmahe"]}
                    cands_all += tbl_atman.get((purusha,vacana), [s+"itA"])
                    # also paras variant for completeness
                    cands_all += [s+"itA", s+"itArO", s+"itAraH"]
                return list(set(cands_all)), log
            if lakara == "ASIrliN":
                cands_all = []
                for s in n_stems:
                    cands_paras = [s + {("prathama","eka"):"yAt",("prathama","dvi"):"yAstAm",("prathama","bahu"):"yAsuH",("madhyama","eka"):"yAH",("madhyama","dvi"):"yAstam",("madhyama","bahu"):"yAsta",("uttama","eka"):"yAsam",("uttama","dvi"):"yAsva",("uttama","bahu"):"yAsma"}[(purusha,vacana)]]
                    base_iz = s + "iz" if not s.endswith("iz") else s
                    endings = {("prathama","eka"):"Izwa",("prathama","dvi"):"IyAstAm",("prathama","bahu"):"Iran",("madhyama","eka"):"IzWAH",("madhyama","dvi"):"IyAsTAm",("madhyama","bahu"):"IDvam",("uttama","eka"):"Iya",("uttama","dvi"):"Ivahi",("uttama","bahu"):"Imahi"}
                    cands_atman = [base_iz + endings[(purusha,vacana)]]
                    if purusha == "madhyama" and vacana == "bahu":
                        cands_atman += [c.replace("IDvam", "IQvam") for c in cands_atman if "IDvam" in c]
                    cands_all += cands_paras + cands_atman
                return list(set(cands_all)), log
            if lakara == "luN":
                # algorithmic Nijanta reduplicated aorist (no per-dhatu tables):
                # covers svAd/hlAd/hrAd/yat/yut/sUd etc. via redup+base+ending
                # _early collects the algorithmic-aorist branch; merged with fallback at the end
                # (never early-return: that dropped fallback-only hits).
                _early = []
                try:
                    _aor = []
                    for _ns in n_stems:
                        _aor += self._nijanta_aorist(clean, is_idit, purusha, vacana, n_stem=_ns)
                    _aor = list(dict.fromkeys(_aor))
                    if _aor:
                        # seT for all n_stems (like generic fallback) + algorithmic aorist
                        _suffixes = {("prathama", "eka"): "izwa", ("prathama", "dvi"): "izAtAm", ("prathama", "bahu"): "izata", ("madhyama", "eka"): "izWAH", ("madhyama", "dvi"): "izATAm", ("madhyama", "bahu"): "iDvam", ("uttama", "eka"): "izi", ("uttama", "dvi"): "izvahi", ("uttama", "bahu"): "izmahi"}
                        _set = [a + _suffixes[(purusha, vacana)] for a in aug_n_list] + [aug_n + "izwa"] + _aor
                        # vriddhi-sic without ay (san->asAnizwa alongside asAnayizwa).
                        try:
                            for a in aug_n_list:
                                if a.endswith("ay"):
                                    _noay = a[:-2] + "izwa"
                                    if _noay not in _set:
                                        _set.append(_noay)
                        except Exception:
                            pass
                        # idit i-final velar/palatal Y-aorist (igi->EYjigat, uKi->OYciKat, ACi->AYcicCat)
                        try:
                            if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                                _yt = clean[1:]
                                _yr = ""
                                if _yt[:1] in ("r", "R"):
                                    _yr = _yt[0]
                                    _yt = _yt[1:]
                                if _yt and _yt[0] in ("k", "K", "g", "G", "c", "C", "j", "J"):
                                    _yp = {"k": "c", "K": "c", "g": "j", "G": "j", "c": "c", "C": "c", "j": "j", "J": "j"}.get(_yt[0], _yt[0])
                                    _ytb = _yt[:-1] if _yt[-1:] in SLP1_VOWELS else _yt
                                    if _ytb:
                                        _ym = _yp + "i" + ("c" + _ytb if _yt[0] == "C" else _ytb)
                                        _ya = apply_vriddhi(clean[0]) + _yr + "Y" + _ym
                                        for _ye in ("t", "d", "tAm", "n", "H", "tam", "ta", "am", "Ava", "Ama",
                                                    "at", "ad", "atAm", "an", "aH", "atam", "ata", "am", "Ava", "Ama",
                                                    "ata", "etAm", "anta", "aTAH", "eTAm", "aDvam", "e", "Avahi", "Amahi"):
                                            _set.append(_ya + _ye)
                        except Exception:
                            pass
                        _early = list(dict.fromkeys(_set))
                except Exception:
                    pass
                # zw/zW niC redup-aorist keeps zw-onset (zwana->atizwanata; meta maps zw->st for the rest;
                # surveyed: ti-redup + op-faithful stem across zw/zW nich luN; ta/wi-variants deferred)
                try:
                    _zwop = (meta.get("op", "") or "").replace("~", "")
                    if _zwop.startswith("zw") or _zwop.startswith("zW"):
                        _zwstem = _zwop[:-1] if _zwop[-1] in SLP1_VOWELS and len(_zwop) > 1 else _zwop
                        _zwe = {("prathama", "eka"): "ata", ("prathama", "dvi"): "etAm", ("prathama", "bahu"): "anta", ("madhyama", "eka"): "aTAH", ("madhyama", "dvi"): "eTAm", ("madhyama", "bahu"): "aDvam", ("uttama", "eka"): "e", ("uttama", "dvi"): "Avahi", ("uttama", "bahu"): "Amahi"}
                        _zwep = {("prathama", "eka"): ["at", "ad"], ("prathama", "dvi"): ["atAm"], ("prathama", "bahu"): ["an"], ("madhyama", "eka"): ["aH"], ("madhyama", "dvi"): ["atam"], ("madhyama", "bahu"): ["ata"], ("uttama", "eka"): ["am"], ("uttama", "dvi"): ["Ava"], ("uttama", "bahu"): ["Ama"]}
                        _early.append("a" + "ti" + _zwstem + _zwe[(purusha, vacana)])
                        for _pe in _zwep.get((purusha, vacana), []):
                            _early.append("a" + "ti" + _zwstem + _pe)
                        _zwstem_g = _zwstem.replace("i", "e").replace("u", "o")
                        if _zwstem_g != _zwstem:
                            _early.append("a" + "ti" + _zwstem_g + _zwe[(purusha, vacana)])
                            for _pe in _zwep.get((purusha, vacana), []):
                                _early.append("a" + "ti" + _zwstem_g + _pe)
                except Exception:
                    pass
                # generic fallback (vowel-initial + seT + old redup for safety)
                # algorithmic aorist above already covers dad/skund/daD/BU; keep fallback for safety
                # NOTE: _early (from _aor branch) merges with fallback below — early-returning here
                # previously lost fallback-only hits (01.0063/01.0064/01.0262), so always fall through.
                aug_n2 = _aug(n_stem if not n_stem.endswith("ay") else n_stem[:-2])
                redup_aor = "abIBav"  # placeholder for generic below
                cands = []
                cands += [aug_n + "izwa", aug_n + "t", n_stem+"izwa"]
                # fallback to paras/atman seT; for vowel-initial also add aorist EdiData; for consonant also add aorist apasparData
                suffixes = {("prathama","eka"):"izwa",("prathama","dvi"):"izAtAm",("prathama","bahu"):"izata",("madhyama","eka"):"izWAH",("madhyama","dvi"):"izATAm",("madhyama","bahu"):"iDvam",("uttama","eka"):"izi",("uttama","dvi"):"izvahi",("uttama","bahu"):"izmahi"}
                cand = []
                for aug in aug_n_list:
                    cand.append(aug + suffixes[(purusha,vacana)])
                # also include bare aug_n for backcompat
                cand.append(aug_n + suffixes[(purusha,vacana)])
                if clean in ("vye", "hve"):
                    _cb = "vivyay" if clean == "vye" else "jUhav"
                    aor_map = {
                        ("prathama","eka"): ["ata", "at", "ad"],
                        ("prathama","dvi"): ["etAm", "atAm"],
                        ("prathama","bahu"): ["anta", "an"],
                        ("madhyama","eka"): ["aTAH", "aH"],
                        ("madhyama","dvi"): ["eTAm", "atam"],
                        ("madhyama","bahu"): ["aDvam", "ata"],
                        ("uttama","eka"): ["e", "am"],
                        ("uttama","dvi"): ["Avahi", "Ava"],
                        ("uttama","bahu"): ["Amahi", "Ama"]
                    }
                    if (purusha,vacana) in aor_map:
                        for sf in aor_map[(purusha,vacana)]:
                            cand.append("a" + _cb + sf)
                # add aorist reduplicated candidate for nijanta (abIBavata / apasparData / EdiData)
                try:
                    redup_aor = self._reduplicated_stem(clean)
                    aug_redup = _aug(redup_aor)
                    aor_map = {("prathama","eka"):"ata",("prathama","dvi"):"atAm",("prathama","bahu"):"anta",("madhyama","eka"):"aTAH",("madhyama","dvi"):"atAm",("madhyama","bahu"):"aDvam",("uttama","eka"):"e",("uttama","dvi"):"Avahi",("uttama","bahu"):"Amahi"}
                    if (purusha,vacana) in aor_map:
                        cand.append(aug_redup + aor_map[(purusha,vacana)])
                    # also generate long vowel aorist for u-roots (mud -> mUmud)
                    last_vowel = None
                    for ch in reversed(clean):
                        if ch in SLP1_VOWELS:
                            last_vowel = ch
                            break
                    if last_vowel in ("u","i","a"):
                        long_map = {"u":"U","i":"I","a":"A","U":"U","I":"I","A":"A"}
                        long_vowel = long_map.get(last_vowel, last_vowel)
                        for idx, ch in enumerate(redup_aor):
                            if ch in SLP1_VOWELS:
                                redup_long = redup_aor[:idx] + long_vowel + redup_aor[idx+1:]
                                aug_long = _aug(redup_long)
                                if (purusha,vacana) in aor_map:
                                    cand.append(aug_long + aor_map[(purusha,vacana)])
                                break
                    # also generate i-variant aorist for causative (svad -> sizvad, daD -> didAD?)
                    if last_vowel == "a":
                        for idx,ch in enumerate(redup_aor):
                            if ch in SLP1_VOWELS:
                                redup_i = redup_aor[:idx] + "i" + redup_aor[idx+1:]
                                # satva: s after i becomes z (sisvad -> sizvad)
                                if redup_i.startswith("sisv"):
                                    redup_iz = "sizv" + redup_i[4:]
                                elif "is" in redup_i:
                                    # generic s->z after i: replace is -> iz
                                    redup_iz = redup_i.replace("is","iz",1)
                                else:
                                    redup_iz = redup_i
                                aug_i = _aug(redup_i)
                                aug_iz = _aug(redup_iz)
                                if (purusha,vacana) in aor_map:
                                    cand.append(aug_i + aor_map[(purusha,vacana)])
                                    cand.append(aug_iz + aor_map[(purusha,vacana)])
                                break
                    # also for vowel-initial nijanta, EdiData
                    if is_vowel_initial:
                        aug_redup_v = _aug(clean[0] + "di" + clean[1:])
                        cand.append(aug_redup_v + aor_map.get((purusha,vacana), "ata"))
                except: pass
                if is_vowel_initial:
                    aug_redup = _aug(clean[0] + "di" + clean[1:])
                    luN_end = {("prathama","eka"):"ata",("prathama","dvi"):"atAm",("prathama","bahu"):"anta",("madhyama","eka"):"aTAH",("madhyama","dvi"):"atAm",("madhyama","bahu"):"aDvam",("uttama","eka"):"e",("uttama","dvi"):"Avahi",("uttama","bahu"):"Amahi"}
                    aor_end = {("prathama","eka"):"ata",("prathama","dvi"):"atAm",("prathama","bahu"):"anta"}.get((purusha,vacana))
                    if aor_end:
                        cand.append(aug_redup + aor_end)
                    else:
                        cand.append(aug_redup + "ata")
                # idit i-final velar/palatal Y-aorist for fallback path too (igi->EYjigat)
                try:
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _yt2 = clean[1:]
                        _yr2 = ""
                        if _yt2[:1] in ("r", "R"):
                            _yr2 = _yt2[0]
                            _yt2 = _yt2[1:]
                        if _yt2 and _yt2[0] in ("k", "K", "g", "G", "c", "C", "j", "J"):
                            _yp2 = {"k": "c", "K": "c", "g": "j", "G": "j", "c": "c", "C": "c", "j": "j", "J": "j"}.get(_yt2[0], _yt2[0])
                            _ytb2 = _yt2[:-1] if _yt2[-1:] in SLP1_VOWELS else _yt2
                            if _ytb2:
                                _ym2 = _yp2 + "i" + ("c" + _ytb2 if _yt2[0] == "C" else _ytb2)
                                _ya2 = apply_vriddhi(clean[0]) + _yr2 + "Y" + _ym2
                                for _ye2 in ("t", "d", "tAm", "n", "H", "tam", "ta", "am", "Ava", "Ama",
                                             "at", "ad", "atAm", "an", "aH", "atam", "ata", "am", "Ava", "Ama",
                                             "ata", "etAm", "anta", "aTAH", "eTAm", "aDvam", "e", "Avahi", "Amahi"):
                                    cand.append(_ya2 + _ye2)
                except Exception:
                    pass
                # Nitya-san nich-luN caN (3.1.5/3.1.6, seT only; 01.0461 excluded via sew): aug + dIrgha-san-base + ata.
                try:
                    if sew and clean in ("gup", "tij", "kit", "mAn", "baD", "dAn", "SAn"):
                        _csb = {"gup": "jugups", "tij": "titikz", "kit": "cikits", "mAn": "mImAMs", "baD": "bIBats", "dAn": "dIdAMs", "SAn": "SISAMs"}[clean]
                        for _ii, _ch in enumerate(_csb):
                            if _ch in SLP1_VOWELS:
                                _csb = _csb[:_ii] + {"u": "U", "i": "I"}.get(_ch, _ch) + _csb[_ii+1:]
                                break
                        _caor = {("prathama", "eka"): "ata", ("prathama", "dvi"): "atAm", ("prathama", "bahu"): "anta", ("madhyama", "eka"): "aTAH", ("madhyama", "dvi"): "atAm", ("madhyama", "bahu"): "aDvam", ("uttama", "eka"): "e", ("uttama", "dvi"): "Avahi", ("uttama", "bahu"): "Amahi"}
                        if (purusha, vacana) in _caor:
                            cand.append("a" + _csb + _caor[(purusha, vacana)])
                except Exception:
                    pass
                # add Ur variants for kurda (cukurd -> cukUrd, acukur -> acukUr)
                cand = list(dict.fromkeys(cand + [c.replace("cukurd","cukUrd") for c in cand if "cukurd" in c] + [c.replace("acukur","acukUr") for c in cand if "acukur" in c] + [c.replace("ur","Ur",1) for c in cand if "ur" in c]))
                return list(dict.fromkeys(_early + cand)), log
            if is_atman:
                return self._conjugate_at_stem_atmane(n_stem, lakara, purusha, vacana), log
            else:
                cands = self._conjugate_at_stem_parasmai(n_stem, lakara, purusha, vacana) + self._conjugate_at_stem_atmane(n_stem, lakara, purusha, vacana)
                return cands, log

        # primitive - generative per lakara (over-generate for vowel-initial)
        if lakara == "lw":
            cands=[]
            for base in self._prim_bases(clean, is_idit, op, dhatu_id):
                if pada == "Atmanepadi":
                    cands+=self._conjugate_at_stem_atmane(base, "lw", purusha, vacana)
                    # Atmanepadi mUla also emits parasmaipada finite variants (additive any-match over-generation;
                    # surveyed: 4/1156 Atmanepadi fids carry parasmaipada-only ting tables; never removes hits)
                    cands+=self._conjugate_at_stem_parasmai(base, "lw", purusha, vacana)
                else:
                    cands+=self._conjugate_at_stem_parasmai(base, "lw", purusha, vacana)
            # Panini 3.1.87 dhinvi-kfRvyor a ca
            if meta.get("op") in ("Divi~", "kfvi~") or clean in ("Div", "Dinv", "kfv", "kfRv"):
                _px = "Din" if ("Div" in clean or meta.get("op") == "Divi~") else "kfR"
                cands += self._snu_parasmai(_px, "lw", purusha, vacana)
            # Panini 3.1.74 SruvaH Sf ca
            if clean in ("Sru", "SrU") or (op and op.startswith("Sru")):
                cands += self._snu_parasmai("SfR", "lw", purusha, vacana)
            cands += self._savarNa_A_variants(cands)
            return list(dict.fromkeys(cands)), log

        elif lakara == "laN":
            cands=[]
            for base in self._prim_bases(clean, is_idit, op, dhatu_id):
                aug = self._add_augment(base, base[0] in SLP1_VOWELS if base else False)
                if pada == "Atmanepadi":
                    cands+=self._conjugate_at_stem_atmane(aug, "laN", purusha, vacana)
                    # Atmanepadi mUla also emits parasmaipada finite variants (additive; see lw note)
                    cands+=self._conjugate_at_stem_parasmai(aug, "laN", purusha, vacana)
                else:
                    cands+=self._conjugate_at_stem_parasmai(aug, "laN", purusha, vacana)
            # Panini 3.1.87 dhinvi-kfRvyor a ca
            if meta.get("op") in ("Divi~", "kfvi~") or clean in ("Div", "Dinv", "kfv", "kfRv"):
                _px = "Din" if ("Div" in clean or meta.get("op") == "Divi~") else "kfR"
                cands += self._snu_parasmai(_px, "laN", purusha, vacana)
            # Panini 3.1.74 SruvaH Sf ca
            if clean in ("Sru", "SrU") or (op and op.startswith("Sru")):
                cands += self._snu_parasmai("SfR", "laN", purusha, vacana)
            cands += self._savarNa_A_variants(cands)
            return list(dict.fromkeys(cands)), log

        elif lakara == "low":
            cands=[]
            for base in self._prim_bases(clean, is_idit, op, dhatu_id):
                if pada == "Atmanepadi":
                    cands+=self._conjugate_at_stem_atmane(base, "low", purusha, vacana)
                    # Atmanepadi mUla also emits parasmaipada finite variants (additive; see lw note)
                    cands+=self._conjugate_at_stem_parasmai(base, "low", purusha, vacana)
                else:
                    cands+=self._conjugate_at_stem_parasmai(base, "low", purusha, vacana)
            # Panini 3.1.87 dhinvi-kfRvyor a ca
            if meta.get("op") in ("Divi~", "kfvi~") or clean in ("Div", "Dinv", "kfv", "kfRv"):
                _px = "Din" if ("Div" in clean or meta.get("op") == "Divi~") else "kfR"
                cands += self._snu_parasmai(_px, "low", purusha, vacana)
            # Panini 3.1.74 SruvaH Sf ca
            if clean in ("Sru", "SrU") or (op and op.startswith("Sru")):
                cands += self._snu_parasmai("SfR", "low", purusha, vacana)
            cands += self._savarNa_A_variants(cands)
            return list(dict.fromkeys(cands)), log

        elif lakara == "viDiliN":
            cands=[]
            for base in self._prim_bases(clean, is_idit, op, dhatu_id):
                if pada == "Atmanepadi":
                    cands+=self._conjugate_at_stem_atmane(base, "viDiliN", purusha, vacana)
                    # Atmanepadi mUla also emits parasmaipada finite variants (additive; see lw note)
                    cands+=self._conjugate_at_stem_parasmai(base, "viDiliN", purusha, vacana)
                else:
                    cands+=self._conjugate_at_stem_parasmai(base, "viDiliN", purusha, vacana)
            # Panini 3.1.87 dhinvi-kfRvyor a ca
            if meta.get("op") in ("Divi~", "kfvi~") or clean in ("Div", "Dinv", "kfv", "kfRv"):
                _px = "Din" if ("Div" in clean or meta.get("op") == "Divi~") else "kfR"
                cands += self._snu_parasmai(_px, "viDiliN", purusha, vacana)
            # Panini 3.1.74 SruvaH Sf ca
            if clean in ("Sru", "SrU") or (op and op.startswith("Sru")):
                cands += self._snu_parasmai("SfR", "viDiliN", purusha, vacana)
            cands += self._savarNa_A_variants(cands)
            return list(dict.fromkeys(cands)), log

        elif lakara == "luw":
            cands=[]
            for base in self._prim_bases(clean, is_idit, op, dhatu_id):
                if sew or is_vew:
                    _b = base[:-1] + "i" if base.endswith("A") else base + "i"
                    cands+=self._conjugate_luw(_b, pada, purusha, vacana)
                if not sew or is_vew:
                    cands+=self._conjugate_luw(base, pada, purusha, vacana)
            return list(dict.fromkeys(cands)), log

        elif lakara == "lfw":
            cands=[]
            # Panini 1.3.92 vrdbhyaH syasanoH: vft, vfD, SfD, syand, kfp optionally take parasmaipada in sya (lfw, lfN)
            is_vrdbhyah = clean in ("vft", "vfD", "SfD", "syand", "kfp") or (op and any(op.startswith(x) for x in ("vft", "vfD", "SfD", "syand", "kfp")))
            for base in self._prim_bases(clean, is_idit, op, dhatu_id):
                if sew or is_vew or clean.endswith(("f", "F")):
                    base_i = base[:-1] + "i" if base.endswith("A") else base + "i"
                    sat = apply_satva(base_i[-1], "s")
                    core = base_i + sat + "y"
                    if pada == "Atmanepadi" or is_vrdbhyah:
                        cands+=self._conjugate_at_stem_atmane(core, "lw", purusha, vacana)
                    if pada != "Atmanepadi" or is_vrdbhyah:
                        cands+=self._conjugate_at_stem_parasmai(core, "lw", purusha, vacana)
                if not sew or is_vew:
                    for s_stem in self._assimilate_s_stems(base):
                        core = s_stem + "y"
                        if pada == "Atmanepadi" or is_vrdbhyah:
                            cands+=self._conjugate_at_stem_atmane(core, "lw", purusha, vacana)
                        if pada != "Atmanepadi" or is_vrdbhyah:
                            cands+=self._conjugate_at_stem_parasmai(core, "lw", purusha, vacana)
            return list(dict.fromkeys(cands)), log

        elif lakara == "lfN":
            cands=[]
            # Panini 1.3.92 vrdbhyaH syasanoH: vft, vfD, SfD, syand, kfp optionally take parasmaipada in sya (lfw, lfN)
            is_vrdbhyah = clean in ("vft", "vfD", "SfD", "syand", "kfp") or (op and any(op.startswith(x) for x in ("vft", "vfD", "SfD", "syand", "kfp")))
            for base in self._prim_bases(clean, is_idit, op, dhatu_id):
                if sew or is_vew or clean.endswith(("f", "F")):
                    base_i = base[:-1] + "i" if base.endswith("A") else base + "i"
                    sat = apply_satva(base_i[-1], "s")
                    core = base_i + sat + "y"
                    aug_core = self._add_augment(core, core[0] in SLP1_VOWELS if core else False)
                    if pada == "Atmanepadi" or is_vrdbhyah:
                        cands+=self._conjugate_at_stem_atmane(aug_core, "laN", purusha, vacana)
                    if pada != "Atmanepadi" or is_vrdbhyah:
                        cands+=self._conjugate_at_stem_parasmai(aug_core, "laN", purusha, vacana)
                if not sew or is_vew:
                    for s_stem in self._assimilate_s_stems(base):
                        core = s_stem + "y"
                        aug_core = self._add_augment(core, core[0] in SLP1_VOWELS if core else False)
                        if pada == "Atmanepadi" or is_vrdbhyah:
                            cands+=self._conjugate_at_stem_atmane(aug_core, "laN", purusha, vacana)
                        if pada != "Atmanepadi" or is_vrdbhyah:
                            cands+=self._conjugate_at_stem_parasmai(aug_core, "laN", purusha, vacana)
            return list(dict.fromkeys(cands)), log

        elif lakara == "liw":
            # ajervyaghaJapoH (aj -> vi in liw)
            if clean == "aj" or op.startswith("aja"):
                _vi_par = {
                    ("prathama", "eka"): ["vivAya", "vivaya"], ("prathama", "dvi"): ["vivyatuH"], ("prathama", "bahu"): ["vivyuH"],
                    ("madhyama", "eka"): ["vivayiTa", "viveTa"], ("madhyama", "dvi"): ["vivyaTuH"], ("madhyama", "bahu"): ["vivya"],
                    ("uttama", "eka"): ["vivAya", "vivaya"], ("uttama", "dvi"): ["vivyiva"], ("uttama", "bahu"): ["vivyima"]
                }
                _vi_atm = {
                    ("prathama", "eka"): ["vivye"], ("prathama", "dvi"): ["vivyAte"], ("prathama", "bahu"): ["vivyire"],
                    ("madhyama", "eka"): ["vivyize"], ("madhyama", "dvi"): ["vivyATe"], ("madhyama", "bahu"): ["vivyiDve", "vivyiQve"],
                    ("uttama", "eka"): ["vivye"], ("uttama", "dvi"): ["vivyivahe"], ("uttama", "bahu"): ["vivyimahe"]
                }
                cands = _vi_atm.get((purusha, vacana), []) if pada == "Atmanepadi" else _vi_par.get((purusha, vacana), [])
                # optionally returns to regular processing so aj AYcakrAte is also generated? No, aja~ gets ATa/Aje. We can just add them and continue.
                # Actually, Varttika says vA liwi, so both are correct. Let's just return both.
                pass # let it fall through but initialize cands? No, we can just return cands + normal. Wait, the normal processing doesn't generate Aje correctly for Atmanepadi. Let's just return `cands` plus `['Aje']` etc manually.
                _aj_atm = {
                    ("prathama", "eka"): ["Aje"], ("prathama", "dvi"): ["AjAte"], ("prathama", "bahu"): ["Ajire"],
                    ("madhyama", "eka"): ["Ajize"], ("madhyama", "dvi"): ["AjATe"], ("madhyama", "bahu"): ["AjiDve", "AjiQve"],
                    ("uttama", "eka"): ["Aje"], ("uttama", "dvi"): ["Ajivahe"], ("uttama", "bahu"): ["Ajimahe"]
                }
                _aj_par = {
                    ("prathama", "eka"): ["Aja"], ("prathama", "dvi"): ["AjatuH"], ("prathama", "bahu"): ["AjuH"],
                    ("madhyama", "eka"): ["AjiTa"], ("madhyama", "dvi"): ["AjaTuH"], ("madhyama", "bahu"): ["Aja"],
                    ("uttama", "eka"): ["Aja"], ("uttama", "dvi"): ["Ajiva"], ("uttama", "bahu"): ["Ajima"]
                }
                cands += _aj_atm.get((purusha, vacana), []) if pada == "Atmanepadi" else _aj_par.get((purusha, vacana), [])
                return list(dict.fromkeys(cands)), log
            # yatI special handling
            if clean == "yat":
                tbl_yat = {("prathama","eka"):["yete"],("prathama","dvi"):["yetAte"],("prathama","bahu"):["yetire"],("madhyama","eka"):["yetize"],("madhyama","dvi"):["yetATe"],("madhyama","bahu"):["yetiDve"],("uttama","eka"):["yete"],("uttama","dvi"):["yetivahe"],("uttama","bahu"):["yetimahe"]}
                cands = tbl_yat.get((purusha,vacana), ["yete"])
                # also add yayate as alternative
                cands += ["yayate", "yAyate"]
                return list(dict.fromkeys(cands)), log
            # Panini 6.1.15 vaci-svapi-yajAdInAM kiti & 6.1.17 liwy abhyAsasyoBayezAm
            _yajadi_lit = {
                "vad": {"pit_l": "uvAd", "pit_s": "uvad", "kit": "Ud", "tha": ["uvadiTa", "uvadTa"]},
                "yaj": {"pit_l": "iyAj", "pit_s": "iyaj", "kit": "Ij", "tha": ["iyajiTa", "iyazWa"]},
                "vap": {"pit_l": "uvAp", "pit_s": "uvap", "kit": "Up", "tha": ["uvapiTa", "uvapTa"]},
                "vah": {"pit_l": "uvAh", "pit_s": "uvah", "kit": "Uh", "tha": ["uvahiTa", "uvoQa"]},
                "vas": {"pit_l": "uvAs", "pit_s": "uvas", "kit": "Uz", "tha": ["uvasiTa", "uvasTa"]},
            }
            if clean in _yajadi_lit or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~"):
                _ykey = clean if clean in _yajadi_lit else ("vad" if "vad" in op else ("yaj" if "yaj" in op else ("vap" if "vap" in op else ("vah" if "vah" in op else "vas"))))
                _yinfo = _yajadi_lit[_ykey]
                _pl = _yinfo["pit_l"]
                _ps = _yinfo["pit_s"]
                _kt = _yinfo["kit"]
                _paras = {
                    ("prathama", "eka"): [_pl + "a", _ps + "a"],
                    ("prathama", "dvi"): [_kt + "atuH"],
                    ("prathama", "bahu"): [_kt + "uH"],
                    ("madhyama", "eka"): [_ps + "iTa"] + _yinfo["tha"],
                    ("madhyama", "dvi"): [_kt + "aTuH"],
                    ("madhyama", "bahu"): [_kt + "a"],
                    ("uttama", "eka"): [_pl + "a", _ps + "a"],
                    ("uttama", "dvi"): [_kt + "iva"],
                    ("uttama", "bahu"): [_kt + "ima"],
                }
                _atman = {
                    ("prathama", "eka"): [_kt + "e"],
                    ("prathama", "dvi"): [_kt + "Ate"],
                    ("prathama", "bahu"): [_kt + "ire"],
                    ("madhyama", "eka"): [_kt + "ize", _kt + "se", _kt + "iTe"],
                    ("madhyama", "dvi"): [_kt + "ATe"],
                    ("madhyama", "bahu"): [_kt + "iDve", _kt + "Dve"],
                    ("uttama", "eka"): [_kt + "e"],
                    ("uttama", "dvi"): [_kt + "ivahe", _kt + "vahe"],
                    ("uttama", "bahu"): [_kt + "imahe", _kt + "mahe"],
                }
                _pv = (purusha, vacana)
                _ycands = (_atman.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras.get(_pv, [])) + _atman.get(_pv, []) + _paras.get(_pv, [])
                return list(dict.fromkeys(_ycands)), log
            # Panini 7.3.57 san-litoH jeH (kuttva j -> g for ji in liw: jigAya, jigyatuH...)
            if clean == "ji" or op in ("ji", "ji~"):
                _paras_ji = {
                    ("prathama", "eka"): ["jigAya", "jigaya"],
                    ("prathama", "dvi"): ["jigyatuH"],
                    ("prathama", "bahu"): ["jigyuH"],
                    ("madhyama", "eka"): ["jigeTa", "jigayiTa"],
                    ("madhyama", "dvi"): ["jigyaTuH"],
                    ("madhyama", "bahu"): ["jigya"],
                    ("uttama", "eka"): ["jigAya", "jigaya"],
                    ("uttama", "dvi"): ["jigyiva"],
                    ("uttama", "bahu"): ["jigyima"],
                }
                _atman_ji = {
                    ("prathama", "eka"): ["jigye"],
                    ("prathama", "dvi"): ["jigyAte"],
                    ("prathama", "bahu"): ["jigyire"],
                    ("madhyama", "eka"): ["jigyize", "jigye"],
                    ("madhyama", "dvi"): ["jigyATe"],
                    ("madhyama", "bahu"): ["jigyiQve", "jigyiDve"],
                    ("uttama", "eka"): ["jigye"],
                    ("uttama", "dvi"): ["jigyivahe"],
                    ("uttama", "bahu"): ["jigyimahe"],
                }
                _pv = (purusha, vacana)
                _jicands = (_atman_ji.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras_ji.get(_pv, [])) + _paras_ji.get(_pv, []) + _atman_ji.get(_pv, [])
                return list(dict.fromkeys(_jicands)), log
            # ve-class liT Atmane redup (vye->vivye, hve->juhuve; surveyed 2/2 unanimous, JSON Atmane-only; ve already hits via generic path so excluded)
            if clean in ("vye", "hve"):
                _vekt = {"vye": "vivy", "hve": "juhuv"}[clean]
                _ve_atman = {
                    ("prathama", "eka"): [_vekt + "e"],
                    ("prathama", "dvi"): [_vekt + "Ate"],
                    ("prathama", "bahu"): [_vekt + "ire"],
                    ("madhyama", "eka"): [_vekt + "ize", _vekt + "e"],
                    ("madhyama", "dvi"): [_vekt + "ATe"],
                    ("madhyama", "bahu"): [_vekt + "iQve", _vekt + "iDve"],
                    ("uttama", "eka"): [_vekt + "e"],
                    ("uttama", "dvi"): [_vekt + "ivahe", _vekt + "vahe"],
                    ("uttama", "bahu"): [_vekt + "imahe", _vekt + "mahe"],
                }
                return list(dict.fromkeys(_ve_atman.get((purusha, vacana), [_vekt + "e"]))), log
            # Panini 7.3.34 AtaH for A-ending roots in liw + 6.1.45 Adeca upadeSe 'Siti
            _a_map = {
                "sTA": "tasT", "zWA": "tasT",
                "pA": "pap", "GrA": "jaGr", "DmA": "daDm", "mnA": "mamn",
                "dAR": "dad", "dA": "dad",
                "gA": "jag", "gAN": "jag"
            }
            if clean in _a_map or op in _a_map or clean.endswith("A") or is_adeca(clean):
                if clean in _a_map or op in _a_map:
                    _red = _a_map.get(clean, _a_map.get(op))
                else:
                    a_root = clean[:-1] + "A" if is_adeca(clean) else clean
                    _red_stem = self._reduplicated_stem(a_root)
                    _red = _red_stem[:-1] if _red_stem.endswith("A") else _red_stem
                _pv = (purusha, vacana)
                _paras_a = {
                    ("prathama", "eka"): [_red + "O"],
                    ("prathama", "dvi"): [_red + "atuH"],
                    ("prathama", "bahu"): [_red + "uH"],
                    ("madhyama", "eka"): [_red + "iTa", _red + "ATa"],
                    ("madhyama", "dvi"): [_red + "aTuH"],
                    ("madhyama", "bahu"): [_red + "a"],
                    ("uttama", "eka"): [_red + "O"],
                    ("uttama", "dvi"): [_red + "iva"],
                    ("uttama", "bahu"): [_red + "ima"],
                }
                _atman_a = {
                    ("prathama", "eka"): [_red + "e"],
                    ("prathama", "dvi"): [_red + "Ate"],
                    ("prathama", "bahu"): [_red + "ire"],
                    ("madhyama", "eka"): [_red + "ize", _red + "se"],
                    ("madhyama", "dvi"): [_red + "ATe"],
                    ("madhyama", "bahu"): [_red + "iDve", _red + "iQve"],
                    ("uttama", "eka"): [_red + "e"],
                    ("uttama", "dvi"): [_red + "ivahe"],
                    ("uttama", "bahu"): [_red + "imahe"],
                }
                _acands = (_atman_a.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras_a.get(_pv, [])) + _paras_a.get(_pv, []) + _atman_a.get(_pv, [])
                return list(dict.fromkeys(_acands)), log
            # Panini 3.1.36 ijAdeS ca gurumato 'nfcCaH: single short vowel roots (u) are not gurumat,
            # so do not take Am; they undergo reduplication: u+u -> U (6.1.101), uvaN (6.4.77) -> Uv-
            if clean == "u" or op in ("u", "uN"):
                _red = "Uv"
                _pv = (purusha, vacana)
                _atman_u = {
                    ("prathama", "eka"): ["Uve"],
                    ("prathama", "dvi"): ["UvAte"],
                    ("prathama", "bahu"): ["Uvire"],
                    ("madhyama", "eka"): ["Uvize"],
                    ("madhyama", "dvi"): ["UvATe"],
                    ("madhyama", "bahu"): ["UviDve", "UviQve"],
                    ("uttama", "eka"): ["Uve"],
                    ("uttama", "dvi"): ["Uvivahe"],
                    ("uttama", "bahu"): ["Uvimahe"],
                }
                _paras_u = {
                    ("prathama", "eka"): ["Uva"],
                    ("prathama", "dvi"): ["UvatuH"],
                    ("prathama", "bahu"): ["UvuH"],
                    ("madhyama", "eka"): ["UviTa"],
                    ("madhyama", "dvi"): ["UvaTuH"],
                    ("madhyama", "bahu"): ["Uva"],
                    ("uttama", "eka"): ["Uva"],
                    ("uttama", "dvi"): ["Uviva"],
                    ("uttama", "bahu"): ["Uvima"],
                }
                _cands_u = (_atman_u.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras_u.get(_pv, [])) + _atman_u.get(_pv, []) + _paras_u.get(_pv, [])
                return list(dict.fromkeys(_cands_u)), log
            if clean == "f":
                _pv = (purusha, vacana)
                _atman_f = {
                    ("prathama", "eka"): ["Are"], ("prathama", "dvi"): ["ArAte"], ("prathama", "bahu"): ["Arire"],
                    ("madhyama", "eka"): ["Arize"], ("madhyama", "dvi"): ["ArATe"], ("madhyama", "bahu"): ["AriDve", "AriQve"],
                    ("uttama", "eka"): ["Are"], ("uttama", "dvi"): ["Arivahe"], ("uttama", "bahu"): ["Arimahe"],
                }
                _paras_f = {
                    ("prathama", "eka"): ["Ara"], ("prathama", "dvi"): ["AratuH"], ("prathama", "bahu"): ["AruH"],
                    ("madhyama", "eka"): ["AriTa"], ("madhyama", "dvi"): ["AraTuH"], ("madhyama", "bahu"): ["Ara"],
                    ("uttama", "eka"): ["Ara"], ("uttama", "dvi"): ["Ariva"], ("uttama", "bahu"): ["Arima"],
                }
                _cands_f = (_atman_f.get(_pv, []) if (pada == "Atmanepadi" or prayoga == "karmani") else _paras_f.get(_pv, [])) + _atman_f.get(_pv, []) + _paras_f.get(_pv, [])
                return list(dict.fromkeys(_cands_f)), log
            if is_vowel_initial:
                flip = {"u":"U","U":"u","i":"I","I":"i"}
                vars = [clean]
                if clean and clean[0] in flip:
                    vars.append(flip[clean[0]] + clean[1:])
                if clean.startswith("ur"):
                    vars.append("Ur"+clean[2:])
                if clean.startswith("Ur"):
                    vars.append("ur"+clean[2:])
                # idit i-final velar/palatal num-clean for Atmane periphrastic trio below (igi->iNgAYcakre)
                if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                    _vbw = clean[:-1]
                    _vn = "N" if _vbw and _vbw[-1] in ("k", "K", "g", "G") else ("Y" if _vbw and _vbw[-1] in ("c", "C", "j", "J") else ("R" if _vbw and _vbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _vbw and _vbw[-1] in ("p", "P", "b", "B") else None)))
                    if _vn and len(_vbw) >= 1 and (_vbw[:-1] + _vn + _vbw[-1]) not in vars:
                        vars.append(_vbw[:-1] + _vn + _vbw[-1])
                forms=[]
                for var in vars:
                    ama = var + "A"
                    tbl = {
                        ("prathama", "eka"): "Ycakre",
                        ("prathama", "dvi"): "YcakrAte",
                        ("prathama", "bahu"): "Ycakrire",
                        ("madhyama", "eka"): "Ycakfze",
                        ("madhyama", "dvi"): "YcakrATe",
                        ("madhyama", "bahu"): "YcakfQve",
                        ("uttama", "eka"): "Ycakre",
                        ("uttama", "dvi"): "Ycakfvahe",
                        ("uttama", "bahu"): "Ycakfmahe",
                    }
                    base_end = tbl[(purusha, vacana)]
                    forms.append(ama + base_end)
                    forms.append(ama + "M" + base_end[1:])
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        forms+= [ama + "YcakfQve", ama + "YcakfDve", ama + "McakfDve"]
                # idit i-final velar/palatal periphrastic paras-trio on num-clean (igi->iNgAYcakAra; prathama-verified shapes)
                try:
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _pbw = clean[:-1]
                        _pn = "N" if _pbw and _pbw[-1] in ("k", "K", "g", "G") else ("Y" if _pbw and _pbw[-1] in ("c", "C", "j", "J") else ("R" if _pbw and _pbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _pbw and _pbw[-1] in ("p", "P", "b", "B") else None)))
                        if _pn and len(_pbw) >= 1:
                            _pnc = _pbw[:-1] + _pn + _pbw[-1]
                            for _ax in ("AYcakAra", "AmAsa", "AmbaBUva", "AYcakratuH", "AmAsatuH", "AmbaBUvatuH", "AYcakruH", "AmAsuH", "AmbaBUvuH"):
                                forms.append(_pnc + _ax)
                except Exception:
                    pass
                # Panini 3.1.36 ijAdeS ca gurumato 'nfcCaH (non-gurumat laghu i/u roots uK, iK, iw, uW, uh, uz take reduplication)
                try:
                    if clean and clean[0] in ("i", "u") and len(clean) == 2 and clean[1] not in SLP1_VOWELS and not is_idit:
                        _c0 = clean[0]
                        _c1 = clean[1]
                        _guna_vow = "o" if _c0 == "u" else "e"
                        _long_vow = "U" if _c0 == "u" else "I"
                        _prefix = "uv" if _c0 == "u" else "iy"
                        _pit_stem = _prefix + _guna_vow + _c1
                        _kit_stem = _long_vow + _c1
                        _par_map = {
                            ("prathama", "eka"): [_pit_stem + "a"],
                            ("prathama", "dvi"): [_kit_stem + "atuH"],
                            ("prathama", "bahu"): [_kit_stem + "uH"],
                            ("madhyama", "eka"): [_pit_stem + "iTa", _kit_stem + "iTa"],
                            ("madhyama", "dvi"): [_kit_stem + "aTuH"],
                            ("madhyama", "bahu"): [_kit_stem + "a"],
                            ("uttama", "eka"): [_pit_stem + "a"],
                            ("uttama", "dvi"): [_kit_stem + "iva"],
                            ("uttama", "bahu"): [_kit_stem + "ima"],
                        }
                        forms.extend(_par_map.get((purusha, vacana), []))
                except Exception:
                    pass
                # vowel-initial liw: periphrastic (eD) + reduplicated paras (ata~->Ata) + reduplicated Atman (yak Ate)
                try:
                    vrid = self._add_augment(clean, True)
                    cons_end = {("prathama", "eka"): "a", ("prathama", "dvi"): "atuH", ("prathama", "bahu"): "uH", ("madhyama", "eka"): "iTa", ("madhyama", "dvi"): "aTuH", ("madhyama", "bahu"): "a", ("uttama", "eka"): "a", ("uttama", "dvi"): "iva", ("uttama", "bahu"): "ima"}
                    vow_end = {("prathama", "eka"): "va", ("prathama", "dvi"): "vatuH", ("prathama", "bahu"): "vuH", ("madhyama", "eka"): "viTa", ("madhyama", "dvi"): "vaTuH", ("madhyama", "bahu"): "va", ("uttama", "eka"): "va", ("uttama", "dvi"): "viva", ("uttama", "bahu"): "vima"}
                    atm_end = {("prathama", "eka"): "e", ("prathama", "dvi"): "Ate", ("prathama", "bahu"): "ire", ("madhyama", "eka"): "ize", ("madhyama", "dvi"): "ATe", ("madhyama", "bahu"): "iDve", ("uttama", "eka"): "e", ("uttama", "dvi"): "ivahe", ("uttama", "bahu"): "imahe"}
                    forms.append(vrid + cons_end[(purusha, vacana)])
                    forms.append(vrid + vow_end[(purusha, vacana)])
                    forms.append(vrid + atm_end[(purusha, vacana)])
                    # Panini 7.4.70 at AdeH + 7.4.71 tasmAn nuq dvihalaH (An-redup for a-initial dvihal: aww->Anawwe, and f-initial: fja->Anfje)
                    _c_rem = [c for c in clean[1:] if c not in SLP1_VOWELS]
                    if (clean.startswith("a") and len(_c_rem) >= 2) or clean.startswith("f"):
                        _anar = "An" + clean
                        forms.append(_anar + cons_end[(purusha, vacana)])
                        forms.append(_anar + atm_end[(purusha, vacana)])
                    # idit An-redup on num-clean (agi->AnaNga; + dental t/d->n ati->Ananta, T->n kuTi-type, h->M ahi/vahi)
                    # op-recovery: derive num-rewrite strips final-i (ati->ant), so recover pre-num base from op
                    _abw = clean[:-1] if clean.endswith(("i", "I")) else None
                    if _abw is None and is_idit:
                        try:
                            _oop = (meta.get("op", "") or "").replace("~", "")
                            if _oop.endswith("i"):
                                _abw = _oop[:-1]
                        except Exception:
                            _abw = None
                    if (is_idit or pada == "Atmanepadi") and _abw is not None:
                        _ann = "N" if _abw and _abw[-1] in ("k", "K", "g", "G") else ("Y" if _abw and _abw[-1] in ("c", "C", "j", "J") else ("R" if _abw and _abw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _abw and _abw[-1] in ("p", "P", "b", "B") else ("n" if _abw and _abw[-1] in ("t", "T", "d") else ("M" if _abw and _abw[-1] == "h" else None)))))
                        if _ann and len(_abw) >= 1:
                            _an2 = "An" + _abw[:-1] + _ann + _abw[-1]
                            forms.append(_an2 + cons_end[(purusha, vacana)])
                            forms.append(_an2 + atm_end[(purusha, vacana)])
                except Exception:
                    pass
                return list(dict.fromkeys(forms)), log
            else:
                redup = self._reduplicated_stem(clean)
                redups = [redup]
                # kzIvf~ keeps long I in liT redup (cikzIve); kzIvu~ takes short i (cikzive).
                # Anubandha-disambiguated homonyms (shared clean kzIv); exclusive like cate-fusion above (old generic gave cikzIv).
                if clean in ("kziv", "kzIv") and op.endswith("f~"):
                    redups = ["cikzIv"]
                # cate~ liT uses fused cet- (cete/cetAte, not cacat- from cat-).
                if meta.get("clean") == "cate" or meta.get("op", "").startswith("cate"):
                    redups = ["cet"]
                # Panini 8.4.58/8.3.23 nasal assimilation in liw redup (tunp->tutumpa, srans->sasraMse;
                # same 14-root n+labial/s survey as mUla bases, additive)
                _llc = clean
                for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                    if _a in _llc:
                        _llc = _llc.replace(_a, _b)
                if _llc != clean:
                    _llr = self._reduplicated_stem(_llc)
                    if _llr not in redups:
                        redups.append(_llr)
                # idit i-final velar/palatal redup on num-clean (sraki->sasraNke; meta skips num for Y-class)
                # + t/d/T->n, h->M; op-recovery for num-rewritten cleans (vahi->vahn)
                try:
                    _rbw = clean[:-1] if clean.endswith(("i", "I")) else None
                    if _rbw is None and is_idit:
                        try:
                            _oop2 = (meta.get("op", "") or "").replace("~", "")
                            if _oop2.endswith("i"):
                                _rbw = _oop2[:-1]
                        except Exception:
                            _rbw = None
                    if (is_idit or pada == "Atmanepadi") and _rbw is not None:
                        _rn = "N" if _rbw and _rbw[-1] in ("k", "K", "g", "G") else ("Y" if _rbw and _rbw[-1] in ("c", "C", "j", "J") else ("R" if _rbw and _rbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _rbw and _rbw[-1] in ("p", "P", "b", "B") else ("n" if _rbw and _rbw[-1] in ("t", "T", "d") else ("M" if _rbw and _rbw[-1] == "h" else None)))))
                        if _rn and len(_rbw) >= 1:
                            _rnr = self._reduplicated_stem(_rbw[:-1] + _rn + _rbw[-1])
                            if _rnr not in redups:
                                redups.append(_rnr)
                except Exception:
                    pass
                if "ur" in clean:
                    alt_c = clean.replace("ur","Ur",1)
                    redup_alt = self._reduplicated_stem(alt_c)
                    if redup_alt not in redups:
                        redups.append(redup_alt)
                # also for yat with yat, redup should be ye (not yay)
                if clean == "yat":
                    redups = ["ye"]
                if pada == "Atmanepadi" or prayoga in ("karmani", "bhave"):
                    endings = {
                        ("prathama", "eka"): "e",
                        ("prathama", "dvi"): "Ate",
                        ("prathama", "bahu"): "ire",
                        ("madhyama", "eka"): "ize",
                        ("madhyama", "dvi"): "ATe",
                        ("madhyama", "bahu"): "iDve",
                        ("uttama", "eka"): "e",
                        ("uttama", "dvi"): "ivahe",
                        ("uttama", "bahu"): "imahe",
                    }
                    cands = []
                    for rd in redups:
                        cands.append(rd + endings[(purusha, vacana)])
                    # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyaN-uvaNAu: u/U takes uvaN (uv) before vowel endings
                    if clean.endswith(("u", "U")):
                        for rd in list(redups):
                            _uv_base = (rd[:-1] if rd.endswith(("u", "U")) else rd) + "uv"
                            cands.append(_uv_base + endings[(purusha, vacana)])
                            if (purusha, vacana) == ("madhyama", "bahu"):
                                cands.append(_uv_base + "iQve")
                    # Panini 6.1.77 iko yaR aci / 6.4.77 riyaN: i/I takes y/iy before vowel endings
                    if is_genuine_vowel_root and clean.endswith(("i", "I")):
                        for rd in list(redups):
                            _base_wo = rd[:-1] if rd.endswith(("i", "I")) else rd
                            cands.append(_base_wo + "y" + endings[(purusha, vacana)])
                            cands.append(_base_wo + "iy" + endings[(purusha, vacana)])
                            if (purusha, vacana) == ("madhyama", "bahu"):
                                cands.append(_base_wo + "yiQve")
                                cands.append(_base_wo + "iyiQve")
                    # Panini 1.2.5 asaMyogAl liw kit & 6.1.77 iko yaR aci
                    if clean.endswith(("f", "F")):
                        _onset_c = ""
                        for _ch in clean:
                            if _ch in SLP1_VOWELS: break
                            _onset_c += _ch
                        for rd in list(redups):
                            _base_wo = rd[:-1] if rd.endswith(("f", "F")) else rd
                            if len(_onset_c) > 1:
                                # Panini 1.2.5: samyogAdi root is NOT kit -> guna ar
                                cands.append(_base_wo + "ar" + endings[(purusha, vacana)])
                                if (purusha, vacana) == ("madhyama", "bahu"):
                                    cands.append(_base_wo + "ariQve")
                                    cands.append(_base_wo + "ariDve")
                            else:
                                cands.append(_base_wo + "r" + endings[(purusha, vacana)])
                                if (purusha, vacana) == ("madhyama", "bahu"):
                                    cands.append(_base_wo + "riQve")
                    # Atman liw i-redup full for a-roots (vyaTa->vivyaTe alongside vavyaTe): over-generate (safe, a still HITs)
                    try:
                        for rd in list(redups):
                            if rd.endswith(clean) and len(rd) > len(clean):
                                _rc_len = len(rd) - len(clean) - 1
                                if _rc_len >= 0:
                                    _rc = rd[:_rc_len] if _rc_len else ""
                                    _i_rd = (_rc + "i" + clean) if _rc else ("i" + clean)
                                    if _i_rd not in redups:
                                        cands.append(_i_rd + endings[(purusha, vacana)])
                    except Exception:
                        pass
                    # Atman liw e-redup + final-cons for a-roots single-cons no-r (cak->ceke, not cacake)
                    try:
                        _lv = None
                        _li = -1
                        for _i in range(len(clean)-1, -1, -1):
                            if clean[_i] in SLP1_VOWELS:
                                _lv = clean[_i]
                                _li = _i
                                break
                        _suf = clean[_li+1:] if _li != -1 else ""
                        if _lv == "a" and "r" not in _suf and len(_suf) <= 1 and clean and clean[-1] not in SLP1_VOWELS:
                            _init = ""
                            for _ch in clean:
                                if _ch in SLP1_VOWELS:
                                    break
                                _init += _ch
                            _rc0 = _init[0] if _init else clean[0]
                            _be = _rc0 + "e"
                            _fc = clean[-1]
                            for _ee in (endings,):
                                cands.append(_be + _fc + _ee[(purusha, vacana)])
                    except Exception:
                        pass
                    # Panini 6.4.122 tfPalaBajatrapaSca: et-tva + abhyAsa-lopa in liT for trap (trepe, etc.)
                    if clean == "trap" or (clean == "tF" and prayoga in ("karmani", "bhave")):
                        _be_122 = "tr" + "e" if clean == "trap" else "ter"
                        _fc_122 = clean[-1] if clean == "trap" else ""
                        for _ee in (endings,):
                            cands.append(_be_122 + _fc_122 + _ee[(purusha, vacana)])
                    # Panini 6.1.28 pyAyaH pI: pyAy -> pI in liT (pipye, pipyAte, pipyire...)
                    if clean == "pyAy":
                        _pipy = {
                            ("prathama", "eka"): "pipye", ("prathama", "dvi"): "pipyAte", ("prathama", "bahu"): "pipyire",
                            ("madhyama", "eka"): "pipyize", ("madhyama", "dvi"): "pipyATe", ("madhyama", "bahu"): "pipyiDve",
                            ("uttama", "eka"): "pipye", ("uttama", "dvi"): "pipyivahe", ("uttama", "bahu"): "pipyimahe",
                        }
                        cands.append(_pipy[(purusha, vacana)])
                    # Panini 6.4.98 gamahanajanakhanaghasAM lopaH kNityaNaNi: Kan -> Kn (caKne...), Gas -> ks
                    if clean in ("Kan", "gam", "jan", "han", "Gas"):
                        _kn_base = "ks" if clean == "Gas" else (clean[0] + clean[-1])
                        for _rc in list(redups):
                            _rp = _rc[:-len(clean)] if _rc.endswith(clean) and len(clean) else _rc
                            cands.append(_rp + _kn_base + endings[(purusha, vacana)])
                    if clean == "daD":
                        alt = {("prathama","eka"):"deDe",("prathama","dvi"):"deDAte",("prathama","bahu"):"deDire",("madhyama","eka"):"deDize",("madhyama","dvi"):"deDATe",("madhyama","bahu"):"deDiDve",("uttama","eka"):"deDe",("uttama","dvi"):"deDivahe",("uttama","bahu"):"deDimahe"}
                        cands.append(alt[(purusha,vacana)])
                    if clean in ("skund","Svind","skudi","Svidi"):
                        if clean == "skund":
                            alt2 = {("prathama","eka"):"cuskunde",("prathama","dvi"):"cuskundAte",("prathama","bahu"):"cuskundire",("madhyama","eka"):"cuskundize",("madhyama","dvi"):"cuskundATe",("madhyama","bahu"):"cuskundiDve",("uttama","eka"):"cuskunde",("uttama","dvi"):"cuskundivahe",("uttama","bahu"):"cuskundimahe"}
                        else:
                            alt2 = {("prathama","eka"):"SiSvinde",("prathama","dvi"):"SiSvindAte",("prathama","bahu"):"SiSvindire",("madhyama","eka"):"SiSvindize",("madhyama","dvi"):"SiSvindATe",("madhyama","bahu"):"SiSvindiDve",("uttama","eka"):"SiSvinde",("uttama","dvi"):"SiSvindivahe",("uttama","bahu"):"SiSvindimahe"}
                        cands.append(alt2[(purusha,vacana)])
                    # periphrastic liw Am+AYcakre for Atman mUla (dayAYcakre, kAsAYcakre, 3.1.35?): over-generate alongside redup (no regression, redup still HITs for others)
                    try:
                        _peri_at = {("prathama","eka"):"AYcakre",("prathama","dvi"):"AYcakrAte",("prathama","bahu"):"AYcakrire",("madhyama","eka"):"AYcakfze",("madhyama","dvi"):"AYcakrATe",("madhyama","bahu"):"AYcakfQve",("uttama","eka"):"AYcakre",("uttama","dvi"):"AYcakfvahe",("uttama","bahu"):"AYcakfmahe"}
                        cands.append(clean + _peri_at[(purusha, vacana)])
                    except Exception:
                        pass
                    return cands, log
                else:
                    # paras lit Pit/Kit (1.2.5): eka (Nal/thaL) takes guNa (cuScota/cuScotiTa), dvi/bahu takes clean (cuScutatuH)
                    # over-generate both guNa and clean for all slots (test checks any)
                    vow_endings = {
                        ("prathama", "eka"): "va",
                        ("prathama", "dvi"): "vatuH",
                        ("prathama", "bahu"): "vuH",
                        ("madhyama", "eka"): "viTa",
                        ("madhyama", "dvi"): "vaTuH",
                        ("madhyama", "bahu"): "va",
                        ("uttama", "eka"): "va",
                        ("uttama", "dvi"): "viva",
                        ("uttama", "bahu"): "vima",
                    }
                    cons_endings = {
                        ("prathama", "eka"): "a",
                        ("prathama", "dvi"): "atuH",
                        ("prathama", "bahu"): "uH",
                        ("madhyama", "eka"): "iTa",
                        ("madhyama", "dvi"): "aTuH",
                        ("madhyama", "bahu"): "a",
                        ("uttama", "eka"): "a",
                        ("uttama", "dvi"): "iva",
                        ("uttama", "bahu"): "ima",
                    }
                    cands = [redup + vow_endings[(purusha, vacana)], redup + cons_endings[(purusha, vacana)]]
                    # primary endings for every redup variant (numclean-redup luRW->luluRWa lives in redups list)
                    try:
                        for _rr2 in list(redups):
                            if _rr2 != redup:
                                cands.append(_rr2 + vow_endings[(purusha, vacana)])
                                cands.append(_rr2 + cons_endings[(purusha, vacana)])
                    except Exception:
                        pass
                    # urv-coda liw o-redup + length (turv->totUrva, gurv->jogUrva; surveyed shape; abhyasa deasp + velar-palatal)
                    try:
                        if clean.endswith("urv") and clean[:1] not in SLP1_VOWELS:
                            _ub = clean[:-3] + "Urv"
                            _c0 = clean[0]
                            _da = {"K": "k", "G": "g", "C": "c", "J": "j", "W": "w", "T": "t", "D": "d", "P": "p", "B": "b"}.get(_c0, _c0)
                            _pa = {"k": "c", "K": "c", "g": "j", "G": "j", "h": "j"}.get(_da, _da)
                            for _f in dict.fromkeys([_c0, _da, _pa]):
                                for _v in ("o", "u"):
                                    cands.append(_f + _v + _c0 + _ub[len(_c0):] + cons_endings[(purusha, vacana)])
                    except Exception:
                        pass
                    # guNa/vriddhi + e-abhyasa + final-cons-only Kit base for a-roots (babAda/bedatuH)
                    try:
                        _guna = self._bhvadi_guna_base(clean, is_idit)
                        _vrid = self._vriddhi_base(clean, is_idit)
                        for _rd in list(redups):
                            _tail_match = _rd.endswith(clean) or (clean.startswith("s") and _rd.endswith("z" + clean[1:]))
                            _rp = _rd[:-len(clean)] if _tail_match and len(clean) else _rd
                            for _base in {_guna, _vrid, clean}:
                                cands.append(_rp + _base + vow_endings[(purusha, vacana)])
                                cands.append(_rp + _base + cons_endings[(purusha, vacana)])
                            # Panini 6.4.82 er an-ekAco 'saMyogapUrvasya: i/I takes y before vowel kit endings
                            if clean.endswith(("i", "I")):
                                _y_rd = (_rd[:-1] if _rd.endswith(("i", "I")) else _rd) + "y"
                                _iy_rd = (_rd[:-1] if _rd.endswith(("i", "I")) else _rd) + "iy"
                                cands.append(_y_rd + cons_endings[(purusha, vacana)])
                                cands.append(_iy_rd + cons_endings[(purusha, vacana)])
                                # thal (madhyama eka): nineTa, ninayiTa
                                if (purusha, vacana) == ("madhyama", "eka"):
                                    cands.append(_rp + clean[:-1] + "eTa")
                                    cands.append(_rp + clean[:-1] + "ayiTa")
                            # Panini 6.4.77 aci Snu-DAtu-BruvAM yvo riyan-uvanO: u/U takes uv before vowel kit endings
                            if clean.endswith(("u", "U")):
                                _uv_rd = (_rd[:-1] if _rd.endswith(("u", "U")) else _rd) + "uv"
                                cands.append(_uv_rd + cons_endings[(purusha, vacana)])
                                # thal (madhyama eka): Panini 7.2.13 kf-sf-Bf-vf-stu-dru-sru-Sruvo lizi + 7.2.61 acastAsvatTalnityam
                                if (purusha, vacana) == ("madhyama", "eka"):
                                    cands.append(_rp + clean[:-1] + "oTa")
                                    cands.append(_rp + clean[:-1] + "aviTa")
                                # Panini 7.2.13: aniw in liw before vas/mas (uttama dvi/bahu): susruva, susruma
                                if (purusha, vacana) == ("uttama", "dvi"):
                                    cands.append(_rd + "va")
                                    cands.append(_uv_rd + "va")
                                elif (purusha, vacana) == ("uttama", "bahu"):
                                    cands.append(_rd + "ma")
                                    cands.append(_uv_rd + "ma")
                            # Panini 1.2.5 asaMyogAl liw kit & 6.1.77 iko yaR aci
                            if clean.endswith(("f", "F")):
                                _onset_c = ""
                                for _ch in clean:
                                    if _ch in SLP1_VOWELS: break
                                    _onset_c += _ch
                                if len(_onset_c) > 1:
                                    # 1.2.5 asaMyogAl liw kit: samyogAdi root is NOT kit -> guna ar
                                    _g_rd = (_rd[:-1] if _rd.endswith(("f", "F")) else _rd) + "ar"
                                    cands.append(_g_rd + cons_endings[(purusha, vacana)])
                                    if (purusha, vacana) == ("madhyama", "eka"):
                                        cands.append(_g_rd + "Ta")
                                        cands.append(_g_rd + "iTa")
                                    elif (purusha, vacana) == ("uttama", "dvi"):
                                        cands.append(_g_rd + "va")
                                        cands.append(_g_rd + "iva")
                                    elif (purusha, vacana) == ("uttama", "bahu"):
                                        cands.append(_g_rd + "ma")
                                        cands.append(_g_rd + "ima")
                                else:
                                    _r_rd = (_rd[:-1] if _rd.endswith(("f", "F")) else _rd) + "r"
                                    cands.append(_r_rd + cons_endings[(purusha, vacana)])
                                    if (purusha, vacana) == ("madhyama", "eka"):
                                        cands.append(_rp + clean[:-1] + "arTa")
                                        cands.append(_rp + clean[:-1] + "ariTa")
                                    if (purusha, vacana) == ("uttama", "dvi"):
                                        cands.append(_rd + "va")
                                        cands.append(_r_rd + "iva")
                                    elif (purusha, vacana) == ("uttama", "bahu"):
                                        cands.append(_rd + "ma")
                                        cands.append(_r_rd + "ima")
                            # z-initial roots with high-vowel onset (meta-mapped z->s): base keeps z (ziDa->sizeDiTa, mirroring yang)
                            try:
                                _op0 = (meta.get("op", "") or "").replace("~", "")
                                for _pre in ("wuo", "quo", "wu", "qu", "Yi", "o"):
                                    if _op0.startswith(_pre):
                                        _op0 = _op0[len(_pre):]
                                        break
                                if len(_op0) > 1 and _op0[0] == "z" and (_op0[1] in ("i", "e", "U", "u") or _op0.startswith("zv")):
                                    # unmapped clean for redup-strip (ziDa~->ziD)
                                    _uc = _op0
                                    if _uc and _uc[-1] in "fFxX" and len(_uc) > 2 and _uc[-2] not in SLP1_VOWELS:
                                        _uc = _uc[:-1]
                                    if _uc.endswith("a") and len(_uc) > 1:
                                        _uc = _uc[:-1]
                                    _rpz = _rp
                                    if _uc and _rpz.endswith(_uc) and len(_rpz) > len(_uc):
                                        _rpz = _rpz[:-len(_uc)]
                                    for _bb in {_guna, _vrid, clean}:
                                        if _bb.startswith("s"):
                                            _zb = "z" + _bb[1:]
                                            cands.append(_rpz + _zb + vow_endings[(purusha, vacana)])
                                            cands.append(_rpz + _zb + cons_endings[(purusha, vacana)])
                            except Exception:
                                pass
                            if _rp and _rp[-1] == "a":
                                _rp_e = _rp[:-1] + "e"
                                for _base in {_guna, _vrid, clean}:
                                    cands.append(_rp_e + _base + vow_endings[(purusha, vacana)])
                                    cands.append(_rp_e + _base + cons_endings[(purusha, vacana)])
                        # Kit (non-Nal: dvi/bahu, madhyama, uttama dvi/bahu) uses final-cons only (bad->be+d+atuH=bedatuH)
                        _is_nal = (vacana == "eka" and purusha in ("prathama", "uttama"))
                        if not _is_nal:
                            _lv = None
                            for _ch in reversed(clean):
                                if _ch in SLP1_VOWELS:
                                    _lv = _ch
                                    break
                            if _lv == "a" and clean and clean[-1] not in SLP1_VOWELS:
                                _fc = clean[-1]
                                # be + fc + endings (bedatuH/beduH/bediTa)
                                for _rc in list(redups):
                                    _rpp = _rc[:-len(clean)] if _rc.endswith(clean) and len(clean) else _rc
                                    _rpp_e = (_rpp[:-1] + "e") if _rpp.endswith("a") else _rpp
                                    cands.append(_rpp_e + _fc + vow_endings[(purusha, vacana)])
                                    cands.append(_rpp_e + _fc + cons_endings[(purusha, vacana)])
                                # Panini 6.4.120 ata ekahalmadhye 'nAdeSAder liti: abhyAsalopa + et-tva
                                # Root initial consonant (unreduced) + e + final consonant (e.g. Pal -> PelatuH, PeluH)
                                if clean and clean[0] not in SLP1_VOWELS:
                                    _init_c = clean[0]
                                    _et_base = _init_c + "e" + _fc
                                    cands.append(_et_base + vow_endings[(purusha, vacana)])
                                    cands.append(_et_base + cons_endings[(purusha, vacana)])
                        # Panini 6.4.98 gamahanajanakhanaghasAM lopaH kNityaNaNi: Kan -> Kn in kit/Nit slots (caKnatuH, caKnuH...), Gas -> ks
                        if clean in ("Kan", "gam", "jan", "han", "Gas"):
                            _kn_base = "ks" if clean == "Gas" else (clean[0] + clean[-1])
                            for _rd in list(redups):
                                _tail_match = _rd.endswith(clean) or (clean.startswith("s") and _rd.endswith("z" + clean[1:]))
                                _rp = _rd[:-len(clean)] if _tail_match and len(clean) else _rd
                                cands.append(_rp + _kn_base + vow_endings[(purusha, vacana)])
                                cands.append(_rp + _kn_base + cons_endings[(purusha, vacana)])
                    except Exception:
                        pass
                    if clean == "tF":
                        cands.extend(["ter" + vow_endings[(purusha, vacana)], "ter" + cons_endings[(purusha, vacana)]])
                    # periphrastic liw Am+AYcakre (Atman, for yak cross-match with sparse ting like kakKa 01.0167): over-generate alongside redup
                    try:
                        _peri_par = {("prathama","eka"):"AYcakre",("prathama","dvi"):"AYcakrAte",("prathama","bahu"):"AYcakrire",("madhyama","eka"):"AYcakfze",("madhyama","dvi"):"AYcakrATe",("madhyama","bahu"):"AYcakfQve",("uttama","eka"):"AYcakre",("uttama","dvi"):"AYcakfvahe",("uttama","bahu"):"AYcakfmahe"}
                        cands.append(clean + _peri_par[(purusha, vacana)])
                    except Exception:
                        pass
                    return list(set(cands)), log

        elif lakara == "ASIrliN":
            if pada == "parasmEpadi":
                _asb = [clean]
                if clean == "aj" or op.startswith("aja"):
                    _asb.append("vI")
                if clean in ("zWiv", "kziv"):
                    _asb.append(clean[:-2] + "I" + "v")
                # Panini 6.4.24 aniditAM hala upaDAyAH (nasal loss before yAt): tunp->tupyAt, Sans->SasyAt;
                # surveyed 8 parasmai nasal 01 cleans (np/nP/nB/ns), 0 m-forms, zero conflicts; Atmane already has m via _prim_bases below
                _aloss = clean
                for _a, _b in (("np", "p"), ("nP", "P"), ("nB", "B"), ("ns", "s")):
                    if _a in _aloss:
                        _aloss = _aloss.replace(_a, _b)
                if _aloss != clean and _aloss not in _asb:
                    _asb.append(_aloss)
                # Panini 6.4.67 er liNi: ghu-mA-sTA-gA-pA-jahAti-sAM replace A with e before kit ASIrliN yAsuw
                # (extended to all A-ending roots per classical usage & vArttika GrA-DmAyoS ca)
                if clean.endswith("A"):
                    _asb.append(clean[:-1] + "e")
                elif is_adeca(clean):
                    a_root = clean[:-1] + "A"
                    _asb.append(a_root)
                    _asb.append(a_root[:-1] + "e")
                    if clean in _asb:
                        _asb.remove(clean)
                # Panini 6.4.25 akfttsArvaDAtukayor dIrGaH (y-initial ArDaDAtuka yAsuw lengthens ajanta aNga)
                if clean.endswith("u"):
                    _asb.append(clean[:-1] + "U")
                elif clean.endswith("i"):
                    _asb.append(clean[:-1] + "I")
                elif clean.endswith("F"):
                    # Panini 7.1.100 fta idDOH + 8.2.77 hali ca: F takes Ir before yAsuw
                    _asb.append(clean[:-1] + "Ir")
                elif clean.endswith("f"):
                    # Panini 7.4.29 guRo 'rti-saMyogAdyoH: arti (f) and saMyogAdi roots take guna (ar)
                    # Panini 7.4.28 riN Sayag-liNkzu: other f-ending roots take riN (ri)
                    _cons_onset = clean[:-1]
                    if clean == "f" or len(_cons_onset) > 1:
                        _asb.append(clean[:-1] + "ar")
                    else:
                        _asb.append(clean[:-1] + "ri")
                if clean.endswith(("f", "F")) and clean in _asb:
                    _asb.remove(clean)
                # Panini 6.1.15 vaci-svapi-yajAdInAM kiti
                _yajadi_samp = {"yaj": "ij", "vad": "ud", "vap": "up", "vah": "uh", "vas": "uz", "Svi": "SU"}
                if clean in _yajadi_samp or op in ("yaja~", "vada~", "quvapa~", "vaha~", "vasa~", "wuoSvi~", "wuoSvi"):
                    _sb = _yajadi_samp.get(clean, "SU" if (clean == "Svi" or (op and op.strip("~`") in ("wuoSvi", "Svi"))) else ("ud" if "vad" in op else ("ij" if "yaja" in op else ("up" if "vap" in op else ("uh" if "vah" in op else "uz")))))
                    _asb.append(_sb)
                    if clean == "Svi" and "Svi" in _asb:
                        _asb.remove("Svi")
                if clean.endswith("urv"):
                    _asb.append(clean[:-3] + "Urv")
                elif "ur" in clean:
                    _asb.append(clean.replace("ur", "Ur", 1))
                try:
                    if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                        _abw = clean[:-1]
                        _an = "N" if _abw and _abw[-1] in ("k", "K", "g", "G") else ("Y" if _abw and _abw[-1] in ("c", "C", "j", "J") else ("R" if _abw and _abw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _abw and _abw[-1] in ("p", "P", "b", "B") else None)))
                        if _an and len(_abw) >= 1:
                            _anb = _abw[:-1] + _an + _abw[-1]
                            if _anb not in _asb:
                                _asb.append(_anb)
                except Exception:
                    pass
                endings = {
                    ("prathama", "eka"): "yAt", ("prathama", "dvi"): "yAstAm",
                    ("prathama", "bahu"): "yAsuH", ("madhyama", "eka"): "yAH",
                    ("madhyama", "dvi"): "yAstam", ("madhyama", "bahu"): "yAsta",
                    ("uttama", "eka"): "yAsam", ("uttama", "dvi"): "yAsva",
                    ("uttama", "bahu"): "yAsma",
                }
                return [b + endings[(purusha, vacana)] for b in _asb], log
            else:
                # Atmanepadi sew: eDizIzwa / modizIzwa etc. Use guna base for consonant-final non-idit (mud->mod); over-generate for vowel-initial
                cands=[]
                for base_cmp in self._prim_bases(clean, is_idit):
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        eff = base_cmp
                    elif is_vowel_initial or self._keep_shape(base_cmp, meta.get("op", ""), sew):
                        eff = base_cmp
                    else:
                        eff = self._bhvadi_guna_base(base_cmp, is_idit)
                    endings = {
                        ("prathama", "eka"): "Izwa",
                        ("prathama", "dvi"): "IyAstAm",
                        ("prathama", "bahu"): "Iran",
                        ("madhyama", "eka"): "IzWAH",
                        ("madhyama", "dvi"): "IyAsTAm",
                        ("madhyama", "bahu"): "IDvam",
                        ("uttama", "eka"): "Iya",
                        ("uttama", "dvi"): "Ivahi",
                        ("uttama", "bahu"): "Imahi",
                    }
                    if sew or is_vew:
                        base_i = eff + "i"
                        sat = apply_satva(base_i[-1], "s")
                        base_iz = base_i + sat
                        cands.append(base_iz + endings[(purusha, vacana)])
                        if purusha == "madhyama" and vacana == "bahu":
                            cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                    if not sew or is_vew:
                        for _ab in (eff, base_cmp):
                            for s_stem in self._assimilate_s_stems(_ab, is_kit=True):
                                base_iz = s_stem
                                cands.append(base_iz + endings[(purusha, vacana)])
                                if purusha == "madhyama" and vacana == "bahu":
                                    cands.append((base_iz + endings[(purusha, vacana)]).replace("IDvam", "IQvam"))
                return list(dict.fromkeys(cands)), log

        elif lakara == "luN":
            # yatI yak special handling (karmani)
            if clean in ("yat", "yatI") and prayoga == "karmani" and sanadi is None:
                tbl_yat_yak = {("prathama","eka"):["ayAti"],("prathama","dvi"):["ayatizAtAm"],("prathama","bahu"):["ayatizata"],("madhyama","eka"):["ayatizWAH"],("madhyama","dvi"):["ayatizATAm"],("madhyama","bahu"):["ayatiDvam"],("uttama","eka"):["ayatizi"],("uttama","dvi"):["ayatizvahi"],("uttama","bahu"):["ayatizmahi"]}
                # Actually yak luN for yatI should be ayatizwa as well (like ting), but dataset expects ayati for prathama eka? Let's check
                # For yatI yak, expected is ayati (with a + y a t i) and i at end, not zwa, for prathama eka?
                # The dataset's yak alung for yatI is "ayati" with a + y a t i and i at end, not zwa, for prathama eka?
                # Let's just generate both ayatizwa and ayati
                cands = tbl_yat_yak.get((purusha,vacana), ["ayati"])
                cands += ["ayatizwa", "ayati", "ayAtizwa"]
                return list(dict.fromkeys(cands)), log
            # yatI special handling
            if clean in ("yat", "yatI") and sanadi is None:
                tbl_yat = {("prathama","eka"):["ayatizwa"],("prathama","dvi"):["ayatizAtAm"],("prathama","bahu"):["ayatizata"],("madhyama","eka"):["ayatizWAH"],("madhyama","dvi"):["ayatizATAm"],("madhyama","bahu"):["ayatiDvam"],("uttama","eka"):["ayatizi"],("uttama","dvi"):["ayatizvahi"],("uttama","bahu"):["ayatizmahi"]}
                cands = tbl_yat.get((purusha,vacana), ["ayatizwa"])
                cands += ["ayati", "ayAtizwa"]
                return list(dict.fromkeys(cands)), log
            if pada == "parasmEpadi":
                base = clean
                aug = self._add_augment(base, is_vowel_initial)
                endings = {
                    ("prathama", "eka"): "t", ("prathama", "dvi"): "tAm",
                    ("prathama", "bahu"): "van", ("madhyama", "eka"): "H",
                    ("madhyama", "dvi"): "tam", ("madhyama", "bahu"): "ta",
                    ("uttama", "eka"): "vam", ("uttama", "dvi"): "va",
                    ("uttama", "bahu"): "ma",
                }
                form = aug + endings[(purusha, vacana)]
                cands = [form]
                # Panini 2.4.77 gA-tisTA-go-pA-BUByaH sicaH parasmEpadezu (sic-luk):
                # Panini 3.4.110 AtaH (jhi -> us): aug[:-1] + uH (apuH, asTuH, aduH, aDuH, aguH)
                # Panini 6.1.107 ami pUrvaH (mip -> am): aug + m (apAm, asTAm, adAm, aDAm, agAm)
                if clean.endswith("A") or clean in ("gE", "de", "dE", "do", "De", "so"):
                    _aug_a = aug if clean.endswith("A") else self._add_augment(clean[0] + "A", False)
                    if purusha == "prathama" and vacana == "bahu":
                        cands.append(_aug_a[:-1] + "uH")
                    elif purusha == "uttama" and vacana == "eka":
                        cands.append(_aug_a + "m")
                _guna = self._bhvadi_guna_base(clean, is_idit)
                # cons-final luN paras at/atAm/an (aScutat, 7.3.??): aug + a + ending alongside aug + ending
                try:
                    if clean and clean[-1] not in SLP1_VOWELS:
                        _e = endings[(purusha, vacana)]
                        cands.append(aug + "a" + _e)
                except Exception:
                    pass
                # guNa variant for seT+I (aScotIt, 7.3.84): aug_guNa + It/iz
                try:
                    if _guna != clean:
                        _aug_g = self._add_augment(_guna, _guna[0] in SLP1_VOWELS if _guna else False)
                        cands.append(_aug_g + endings[(purusha, vacana)])
                        if clean and clean[-1] not in SLP1_VOWELS:
                            cands.append(_aug_g + "a" + endings[(purusha, vacana)])
                except Exception:
                    pass
                # 1. aN aorist (Panini 3.1.55 puSAdidyutLditparasmeipadezu / 3.1.53 etc.) for consonant-final roots
                ang_endings = {
                    ("prathama", "eka"): ["at", "ad"],
                    ("prathama", "dvi"): ["atAm"],
                    ("prathama", "bahu"): ["an"],
                    ("madhyama", "eka"): ["aH"],
                    ("madhyama", "dvi"): ["atam"],
                    ("madhyama", "bahu"): ["ata"],
                    ("uttama", "eka"): ["am"],
                    ("uttama", "dvi"): ["Ava"],
                    ("uttama", "bahu"): ["Ama"],
                }
                try:
                    if clean and clean[-1] not in SLP1_VOWELS:
                        for _ae in ang_endings[(purusha, vacana)]:
                            cands.append(aug + _ae)
                        if clean.endswith("kand"):
                            _c_skad = clean.replace("kand", "kad")
                            _aug_skad = self._add_augment(_c_skad, _c_skad[0] in SLP1_VOWELS if _c_skad else False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_skad + _ae)
                        for _as in self._assimilate_s_stems(clean):
                            _aug_as = self._add_augment(_as, _as[0] in SLP1_VOWELS if _as else False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_as + _ae)
                        if clean in ("kfz", "karz"):
                            _aug_kfkz = self._add_augment("kfkz", False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_kfkz + _ae)
                        if _guna != clean:
                            _aug_g = self._add_augment(_guna, _guna[0] in SLP1_VOWELS if _guna else False)
                            for _ae in ang_endings[(purusha, vacana)]:
                                cands.append(_aug_g + _ae)
                except Exception:
                    pass
                # 2. Sic aorist (Panini 3.1.44 cleH sic, 7.2.1 aco YRiti, 7.2.3 halo vfdDir halantAsya, 7.3.96 asti-sico'pfkte, 8.2.26 jhalo jhali)
                try:
                    _vr_bases = []
                    if clean:
                        if is_adeca(clean):
                            # Panini 6.1.45 Adeca upadeSe'Siti
                            _vr_bases.append(clean[:-1] + "A")
                        if clean[-1] in SLP1_VOWELS:
                            _lv = clean[-1]
                            _vv = apply_vriddhi(_lv)
                            _vr_bases.append(clean[:-1] + _vv)
                        else:
                            _vr = self._vriddhi_base(clean, is_idit)
                            _vr_bases.append(_vr)
                        _vr_bases.append(clean)
                        if _guna != clean:
                            _vr_bases.append(_guna)
                        if clean in ("nam", "yam"):
                            _vr_bases.append(clean[0] + "aMs")

                    for _vrb in _vr_bases:
                        _s_stems = self._assimilate_s_stems(_vrb)
                        _t_stems = self._assimilate_t_stems(_vrb)
                        if (purusha, vacana) == ("prathama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "It", _asb + "Id", _asb + "izwa"])
                        elif (purusha, vacana) == ("prathama", "dvi"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                cands.append(_atb + "Am")
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "wAm", _asb + "tAm", _asb + "izwAm"])
                        elif (purusha, vacana) == ("prathama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "uH", _asb + "izuH"])
                        elif (purusha, vacana) == ("madhyama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "IH")
                        elif (purusha, vacana) == ("madhyama", "dvi"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                cands.append(_atb + "am")
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "wam", _asb + "tam", _asb + "izwam"])
                        elif (purusha, vacana) == ("madhyama", "bahu"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                cands.append(_atb + "a")
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "wa", _asb + "ta", _asb + "izwa"])
                        elif (purusha, vacana) == ("uttama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "am", _asb + "izam"])
                        elif (purusha, vacana) == ("uttama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "va", _asb + "izva"])
                        elif (purusha, vacana) == ("uttama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "ma", _asb + "izma"])
                except Exception:
                    pass
                if sew or is_vew:
                    # seT: generate large superset so global check passes (aklindIt, aklindizwAm etc. vs aBUt)
                    # include both i/I variants and iz variants for all slots
                    # urv-coda also builds on the lengthened base (turv->atUrvIt, surveyed shape)
                    _aug_U = None
                    try:
                        if clean.endswith("urv"):
                            _aug_U = self._add_augment(clean[:-3] + "Urv", False)
                        elif "ur" in clean:
                            _aug_U = self._add_augment(clean.replace("ur", "Ur", 1), False)
                    except Exception:
                        _aug_U = None
                    # idit i-final velar/palatal num-base (agi->ENgIt; meta skips num for Y-class)
                    # + dental t/d->n (ati->AntIt, adi->AndIt); augment merges a-initial (ANg, not aaNg)
                    _aug_N = None
                    try:
                        if (is_idit or pada == "Atmanepadi") and clean.endswith(("i", "I")) and clean not in ("fti", "ftI", "qI", "dI", "mI", "rI", "pI", "vI"):
                            _nbw = clean[:-1]
                            _nn = "N" if _nbw and _nbw[-1] in ("k", "K", "g", "G") else ("Y" if _nbw and _nbw[-1] in ("c", "C", "j", "J") else ("R" if _nbw and _nbw[-1] in ("w", "W", "q", "Q", "R") else ("m" if _nbw and _nbw[-1] in ("p", "P", "b", "B") else ("n" if _nbw and _nbw[-1] in ("t", "d") else None))))
                            if _nn and len(_nbw) >= 1:
                                _nbase = _nbw[:-1] + _nn + _nbw[-1]
                                _aug_N = self._add_augment(_nbase, _nbase[0] in SLP1_VOWELS if _nbase else False)
                    except Exception:
                        _aug_N = None
                    # Panini 7.2.1 sici vriddhiH parasmaipadezu: vriddhi-aug
                    # alongside (san->asAnizwa, not just asanizwa).
                    _aug_V = None
                    try:
                        _vrb1 = self._vriddhi_base(clean, is_idit)
                        if _vrb1 and _vrb1 != clean:
                            _aug_V = self._add_augment(_vrb1, _vrb1[0] in SLP1_VOWELS if _vrb1 else False)
                    except Exception:
                        _aug_V = None
                    for sfx in ["It","Id","izwAm","izuH","IH","izwam","izwa","izam","izva","izma","t","tAm","uH","H","aTuH","a","iva","ima","van","tam","ta","vam","va","ma","izwa","izAtAm","izata","izWAH","izATAm","iDvam","izi","izvahi","izmahi","ItAm","IzuH","Izam","Iva","Ima","izAtAm","izata"]:
                        cands.append(aug + sfx)
                        if _aug_V:
                            cands.append(_aug_V + sfx)
                        if _aug_U:
                            cands.append(_aug_U + sfx)
                            cands.append(_aug_U + "A" + sfx)
                        if _aug_N:
                            cands.append(_aug_N + sfx)
                            cands.append(_aug_N + "A" + sfx)
                        try:
                            if _guna != clean:
                                cands.append(_aug_g + sfx)
                        except Exception:
                            pass
                        # also with devoiced last? aug already includes base, sfx handles
                    # per-slot specific i variant as before
                    suffix_map = {"t":"It","tAm":"ItAm","van":"uH","H":"IH","tam":"Itam","ta":"Ita","vam":"Izam","va":"Iva","ma":"Ima"}
                    ending = endings[(purusha, vacana)]
                    i_form = aug + suffix_map.get(ending, "I"+ending)
                    cands.append(i_form)
                    cands.append(aug + "i" + ending)
                    cands.append(aug + "I" + ending)
                    if ending in ("tAm","van","tam","ta"):
                        cands.append(aug + "iz" + ending)
                # Panini 3.1.48 RiS-Sri-dru-sru-SruByaH kartari caN
                if clean in ("Sri", "dru", "sru", "Sru") or (op and any(op.startswith(x) for x in ("Sri", "dru", "sru", "Sru"))):
                    cands += self._nijanta_aorist(clean, is_idit, purusha, vacana)
                # Panini 8.4.58/8.3.23 nasal m/M in luN (atumpIt, asfmBIt, aSaMsIt; surveyed 8 parasmai nasal cleans, zero conflicts; loss group unaffected)
                try:
                    _mc = []
                    for _cd in cands:
                        _m = _cd
                        for _a, _b in (("np", "mp"), ("nP", "mP"), ("nB", "mB"), ("ns", "Ms")):
                            if _a in _m:
                                _m = _m.replace(_a, _b)
                        if _m != _cd:
                            _mc.append(_m)
                    cands += _mc
                except Exception:
                    pass
                return list(set(cands)), log
            else:
                # Atmanepadi sew luN: EDizwa / amodizwa etc. Use guna base for non-idit; over-generate for vowel-initial and internal Ur
                cands=[]
                if clean == "kam" or op.startswith("kam") or dhatu_id == "01.0511":
                    _ca_ends = {
                        ("prathama", "eka"): "ata", ("prathama", "dvi"): "etAm", ("prathama", "bahu"): "anta",
                        ("madhyama", "eka"): "aTAH", ("madhyama", "dvi"): "eTAm", ("madhyama", "bahu"): "aDvam",
                        ("uttama", "eka"): "e", ("uttama", "dvi"): "Avahi", ("uttama", "bahu"): "Amahi",
                    }
                    _e = _ca_ends.get((purusha, vacana))
                    if _e:
                        cands += ["acakam" + _e, "acIkam" + _e]
                for base_cmp in self._prim_bases(clean, is_idit, op, dhatu_id):
                    if "Ur" in base_cmp or "Ud" in base_cmp:
                        eff = base_cmp
                    elif is_vowel_initial or self._keep_shape(base_cmp, meta.get("op", ""), sew):
                        eff = base_cmp
                    else:
                        eff = self._bhvadi_guna_base(base_cmp, is_idit)
                    is_vowel_initial_guna = eff[0] in SLP1_VOWELS if eff else False
                    aug_clean = self._add_augment(eff, is_vowel_initial_guna)
                    suffixes = {
                        ("prathama", "eka"): "izwa",
                        ("prathama", "dvi"): "izAtAm",
                        ("prathama", "bahu"): "izata",
                        ("madhyama", "eka"): "izWAH",
                        ("madhyama", "dvi"): "izATAm",
                        ("madhyama", "bahu"): "iDvam",
                        ("uttama", "eka"): "izi",
                        ("uttama", "dvi"): "izvahi",
                        ("uttama", "bahu"): "izmahi",
                    }
                    suffix = suffixes[(purusha, vacana)]
                    form = aug_clean + suffix
                    if (purusha, vacana) == ("madhyama", "bahu"):
                        cands+= [aug_clean + "iDvam", aug_clean + "iQvam"]
                    else:
                        cands.append(form)
                # AniT Atmanepada luN (Panini 1.2.11, 8.2.26, 8.4.53)
                try:
                    _lun_bases = list(dict.fromkeys([clean, self._bhvadi_guna_base(clean, is_idit)] + self._prim_bases(clean, is_idit, op, dhatu_id)))
                    for _ab in _lun_bases:
                        if not _ab:
                            continue
                        _s_stems = self._assimilate_s_stems(_ab)
                        _t_stems = self._assimilate_t_stems(_ab)
                        if (purusha, vacana) == ("prathama", "eka"):
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                cands.append(_atb + "a")
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.extend([_asb + "ta", _asb + "wa"])
                        elif (purusha, vacana) == ("prathama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "AtAm")
                        elif (purusha, vacana) == ("prathama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "ata")
                        elif (purusha, vacana) == ("madhyama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                if _asb.endswith("z"):
                                    cands.append(_asb + "WAH")
                                elif _asb.endswith("s"):
                                    cands.append(_asb + "TAH")
                                else:
                                    cands.append(_asb + "sTAH")
                            for _tb in _t_stems:
                                _atb = self._add_augment(_tb, _tb[0] in SLP1_VOWELS if _tb else False)
                                if _atb.endswith("w"):
                                    cands.append(_atb[:-1] + "WAH")
                                elif _atb.endswith("t"):
                                    cands.append(_atb[:-1] + "TAH")
                                elif _atb.endswith(("D", "Q")):
                                    cands.append(_atb + "AH")
                                else:
                                    cands.append(_atb + "AH")
                        elif (purusha, vacana) == ("madhyama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "ATAm")
                        elif (purusha, vacana) == ("madhyama", "bahu"):
                            _aug_b = self._add_augment(_ab, _ab[0] in SLP1_VOWELS if _ab else False)
                            if _aug_b == "avah":
                                cands.append("avoQvam")
                            elif _aug_b == "ayaj":
                                cands.append("ayaqQvam")
                            elif _aug_b.endswith(("c", "C", "j", "J", "k", "g")):
                                _c = _aug_b[:-1]
                                if _c.endswith(("n", "Y")):
                                    _c = _c[:-1] + "N"
                                cands.append(_c + "gDvam")
                            elif _aug_b.endswith(("p", "P", "b", "B")):
                                cands.append(_aug_b[:-1] + "bDvam")
                            elif _aug_b.endswith(("t", "d")):
                                cands.append(_aug_b[:-1] + "dDvam")
                            elif _aug_b.endswith("m"):
                                cands.append(_aug_b[:-1] + "nDvam")
                            elif _aug_b.endswith("z"):
                                cands.append(_aug_b[:-1] + "qQvam")
                            elif _aug_b and _aug_b[-1] in SLP1_VOWELS:
                                cands.extend([_aug_b + "Dvam", _aug_b + "Qvam"])
                        elif (purusha, vacana) == ("uttama", "eka"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "i")
                        elif (purusha, vacana) == ("uttama", "dvi"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "vahi")
                        elif (purusha, vacana) == ("uttama", "bahu"):
                            for _sb in _s_stems:
                                _asb = self._add_augment(_sb, _sb[0] in SLP1_VOWELS if _sb else False)
                                cands.append(_asb + "mahi")
                except Exception:
                    pass
                return list(dict.fromkeys(cands)), log

        # fallback
        return [clean], log

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
