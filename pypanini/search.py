"""
pypanini.search
~~~~~~~~~~~~~~~
Pāṇinian morphological search (analyser) in SLP1.

Given any surface word (pada), guess whether it is a **subanta**
(nominal), **krdanta** (participle/derivative) or **tinanta** (verb),
returning the base form:

* subanta  -> pratipadika (stem) + vibhakti + vacana + linga.
  E.g. ``wrampeRa`` -> stem ``wramPa``, tṛtīyā eka (Natva 8.4.1-2 makes
  the dental ``*wrampena`` ungrammatical, so it never verifies).
  Bare ``wramPa`` -> sambodhana (su-lopa). Any foreign word works,
  because a-stems are productive: analysis is by synthesis.
* krdanta  -> dhatu + pratyaya (+ inflection via subanta).
  E.g. ``kftaH`` -> kf + kta; ``kartavyaH`` -> kf + tavya.
* tinanta  -> dhatu + lakara + purusha + vacana + pada (+ upasarga).
  E.g. ``Bavati`` -> BU + lw + prathama + eka.

Method: invert endings, then **forward-verify** with the generative
engines. Only readings that regenerate the surface exactly are kept
(except tinanta, where endings alone identify the slot and the root
is looked up heuristically). Everything is ranked guesswork:
exact-root readings outrank affix-only and open-vocabulary ones.

Public API: :func:`analyze`.
"""
from __future__ import annotations

from typing import Dict, List

from .subanta import SubantaEngine, SLP1_VOWELS

# ---------------------------------------------------------------------------
# shared root data (from the krdanta dhātu cache - read-only cross-check)
# ---------------------------------------------------------------------------

_ROOTS: Dict[str, dict] = {}
_IDS: Dict[str, List[str]] = {}
_KTA_MAP: Dict[str, str] = {}
_LEXICON: Dict[str, List[dict]] = {}
_READY = False


def _ensure_ready() -> None:
    """Build root set, kta reverse map and subanta lexicon index once."""
    global _READY
    if _READY:
        return
    from .krdanta import KrdantaEngine
    ke = KrdantaEngine()
    ke._load_cache()
    metas: Dict[str, dict] = {}
    for _k, _m in ke._cache.items():
        if isinstance(_m, dict) and "clean" in _m:
            metas[_m["clean"]] = _m
    for _clean, _meta in metas.items():
        _ROOTS[_clean] = _meta
        try:
            _kta = ke._kta_stem(
                _clean, bool(_meta.get("sew", True)), _meta.get("op", ""),
                bool(_meta.get("is_idit", False)), _meta.get("gana", "BvAdiH"),
            )
        except Exception:
            continue
        if _kta and _kta not in _KTA_MAP:
            _KTA_MAP[_kta] = _clean
    import re as _re
    for _k, _m in ke._cache_by_id.items():
        if (isinstance(_m, dict) and "clean" in _m
                and _re.fullmatch(r"\d\d\.\d+", _k or "")):
            _IDS.setdefault(_m["clean"], [])
            if _k not in _IDS[_m["clean"]]:
                _IDS[_m["clean"]].append(_k)
    for _v in _IDS.values():
        _v.sort()
    _ensure_end_slots()
    # closed lexicon: common + special stems x 3 lingas (exact forms)
    se = SubantaEngine()
    _lex = [
        "rAma", "sItA", "hari", "mati", "nadI", "SrI", "guru", "Denu",
        "vaDU", "BU", "vAri", "madhu", "kartf", "pitf", "mAtf", "svasf",
        "rAjan", "Atman", "brahman", "karman", "nAman", "manas", "havis",
        "cakzus", "jagat", "mahat", "Bavat", "vAc", "ftvij", "go", "rE",
        "nO", "saKi", "pati", "krozwu", "asTi", "akzi", "ap", "anaQuh",
        "puMs", "div", "ahan", "paTin", "Svan", "yuvan", "jarA",
        "pratyaYc", "Sreyas", "sarva", "pUrva", "para", "eka", "tad",
        "yad", "etad", "kim", "idam", "adas", "asmad", "yuzmad",
        "dvi", "tri", "catur", "paYcan", "zaz", "azwan",
    ]
    for _st in _lex:
        for _li in ("puM", "strI", "napuMsaka"):
            try:
                _d = se.decline(_st, _li)
            except Exception:
                continue
            for _key, _forms in _d.items():
                for _f in _forms:
                    if not _f:
                        continue
                    _LEXICON.setdefault(_f, []).append(
                        {"kind": "subanta", "stem": _st, "linga": _li,
                         "vibhakti": _key[0], "vacana": _key[1],
                         "confidence": 0.9, "lexicon": True})
    _READY = True


# ---------------------------------------------------------------------------
# reverse phonology helpers
# ---------------------------------------------------------------------------

def _deglide(s: str) -> str:
    return s.replace("Ay", "E").replace("Av", "O").replace("ay", "e").replace("av", "o")


def _deguna(s: str) -> str:
    return (s.replace("Ar", "f").replace("ar", "f").replace("Al", "x").replace("al", "x")
             .replace("E", "i").replace("e", "i").replace("O", "u").replace("o", "u"))


def _devrddhi(s: str) -> str:
    return (s.replace("Ar", "f").replace("Al", "x")
             .replace("E", "i").replace("O", "u").replace("A", "a"))


def _decutva(s: str) -> str:
    """Reverse coH kuH (vaktA <- vac + tA): final k -> c."""
    if s.endswith("k"):
        return s[:-1] + "c"
    return s


def _len_variants(s: str) -> List[str]:
    out = [s]
    if s and s[-1] in "iIuUfFxXaA":
        swap = {"i": "I", "I": "i", "u": "U", "U": "u", "f": "F", "F": "f",
                "x": "X", "X": "x", "a": "A", "A": "a"}
        out.append(s[:-1] + swap[s[-1]])
    return out


# famous irregular present stems (gam/yam -cCha-, dRS -paSya-,
# sad -sIda-, sTA -tizWa-, pA -piba-): stem -> [roots]
_IRREG_PRES = {
    "gacCa": ["gam"], "gacC": ["gam"],
    "yacCa": ["yam", "dA"], "yacCh": ["yam", "dA"],
    "paSya": ["dRS"], "paS": ["dRS"],
    "sIda": ["sad"], "sId": ["sad"],
    "tizWa": ["sTA"], "tizW": ["sTA"],
    "piba": ["pA"], "pib": ["pA"],
}


def _irreg_pres(stem: str):
    _r = _IRREG_PRES.get(stem)
    if not _r:
        return None
    return [(_ROOTS[_c], _c) for _c in _r if _c in _ROOTS] or None


# abhyasa onset un-mutation (inverse of 7.4.62 kuhoScuH + deaspiration).
# Given the reduplicant onset, the root onset is one of the list.
# Order matters: mutated sources first (class-3 presents reduplicate
# j- almost only from h (juhoti), b- from B (bibhar), d- stays d-first
# since dadAti and dadhAti are both common).
_ABHYASA_ONSET = {
    "c": ["c", "k"], "C": ["C", "K"], "j": ["h", "g", "G", "j", "J"],
    "J": ["G", "J"], "Y": ["Y", "N"],
    "k": ["k"], "K": ["K"], "g": ["g", "G"], "G": ["G"], "N": ["N"],
    "w": ["w"], "W": ["W"], "t": ["t"], "T": ["T"],
    "d": ["d", "D"], "D": ["D"], "n": ["n"],
    "p": ["p"], "P": ["P"], "b": ["B", "b"], "B": ["B"], "m": ["m"],
    "y": ["y"], "r": ["r"], "l": ["l"], "v": ["v"],
    "s": ["s"], "S": ["S"], "z": ["z"], "h": ["h"],
}
_ABHYASA_GRADE = {"a": "A", "i": "I", "u": "U", "e": "E", "o": "O"}


def _deyan(s: str) -> str:
    """Reverse yaN desandhi (juhv + at <- juhu + at): final y/v -> i/u."""
    if s.endswith("y"):
        return s[:-1] + "i"
    if s.endswith("v"):
        return s[:-1] + "u"
    return s


def _desamprasarana(s: str) -> str:
    """Reverse samprasarana (bibhr <- bibhar): re-insert a before r/l
    when the cluster has no vowel."""
    if any(_c in SLP1_VOWELS for _c in s):
        return s
    for _i, _c in enumerate(s):
        if _c in ("r", "l"):
            return s[:_i] + "a" + s[_i:]
    return s


# san-s de-voicing (inverse of d+s -> ts fusion): contracted desideratives
_SAN_UNVOICE = {
    "t": ["t", "d", "D"], "T": ["T", "D"], "p": ["p", "b", "B"],
    "P": ["P", "B"], "k": ["k", "g", "G"], "K": ["K", "G"],
    "c": ["c", "j"], "C": ["C", "J"], "s": ["s"],
}


def _san_reverse(core: str) -> List[str]:
    """Undo desiderative formation (ditsa <- dA, vividiza <- vid).
    Full type keeps the root (vi-vid-i-za); contracted type fuses it
    (di-tsa <- dA + sa, d devoiced before san-s). Returns root candidates."""
    _w = core[:-1] if core.endswith("a") and len(core) > 1 else core
    if len(_w) < 4 or _w[1] not in ("i", "u"):
        return []
    out: List[str] = []
    # strip san sibilant (z after i/u by zatva, else s)
    if _w[-1] not in ("s", "z", "S"):
        return []
    _body = _w[:-1]
    _red, _mid = _w[:2], _body[2:]
    if len(_mid) < 1:
        return []
    # iT augment variants (vidi/wid both tried; lookup gates)
    _mids = [_mid]
    if _mid.endswith("i") and len(_mid) > 1:
        _mids.append(_mid[:-1])
    for _m in _mids:
        if not _m:
            continue
        if len(_m) == 1 and _m not in SLP1_VOWELS:
            # contracted fusion: bare onset (dits-a <- dA + sa).
            # The reduplicant keeps aspiration clues (di- vs Dhi-),
            # so the matching onset leads (dA, not DA, for dits).
            _cands = list(_SAN_UNVOICE.get(_m, [_m]))
            if _red[0] in _cands:
                _cands.remove(_red[0])
                _cands.insert(0, _red[0])
            for _o in _cands:
                for _v in ("A", "I", "U"):
                    _cand = _o + _v
                    if _cand not in out:
                        out.append(_cand)
        else:
            # full type: root preserved (vivid <- vid; tik <- tij via kuH)
            if _m not in out:
                out.append(_m)
            if _m.endswith("k"):
                _j = _m[:-1] + "j"
                if _j not in out:
                    out.append(_j)
    return out


def _abhyasa_reverse(core: str) -> List[str]:
    """Undo class-3 reduplication (dadA <- dA, juhu <- hu, bibhar <- Bf).
    Returns candidate roots. Only the reduplicant shape is constrained;
    every candidate must still hit the root lexicon to count."""
    if len(core) < 3 or core[1] not in _ABHYASA_GRADE:
        return []
    _ab, _rest = core[:2], core[2:]
    if _ab[0] not in _ABHYASA_ONSET or not _rest:
        return []
    if _rest[0] not in _ABHYASA_ONSET[_ab[0]]:
        return []
    _long = _ABHYASA_GRADE[core[1]]
    # graded root-portion variants (de-glide/guna/vrddhi, yaN, samprasarana)
    _graded = [_rest]
    if _rest.endswith("v") and len(_rest) > 1:
        _graded.append(_rest[:-1])  # perfect -va- (baBUva -> baBU)
    for _fn in (_deglide, _deyan, _desamprasarana):
        _v = _fn(_rest)
        if _v != _rest and _v not in _graded:
            _graded.append(_v)
    _more: List[str] = []
    for _g in list(_graded):
        for _fn in (_deguna, _devrddhi):
            _v = _fn(_g)
            if _v != _g and _v not in _graded and _v not in _more:
                _more.append(_v)
    _graded += _more
    if len(_rest) == 1 and _rest not in SLP1_VOWELS:
        _graded.append(_rest + _long)  # bare onset: dad -> dA
    out: List[str] = []
    for _o in _ABHYASA_ONSET[_ab[0]]:
        for _gr in _graded:
            if not _gr or _gr[0] != _rest[0]:
                continue
            _cand = _o + _gr[1:]
            if _cand not in out:
                out.append(_cand)
    return out


def _deur(s: str) -> str:
    """Reverse u-samprasarana grades (kurv <- kf + u-vikaraRa)."""
    return s.replace("ur", "f").replace("ir", "f")


def _deurv(s: str) -> str:
    """Fused yaN-v + ur (kurv <- kf in one hop)."""
    if s.endswith("urv") and len(s) > 3:
        return s[:-3] + "f"
    if s.endswith("irv") and len(s) > 3:
        return s[:-3] + "f"
    return s


def _devo(s: str) -> str:
    """Reverse o-vikaraNa (karo <- kf, class 8): o -> u, then strip."""
    if s.endswith("o") and len(s) > 1:
        return s[:-1] + "u"
    return s


def _deuv(s: str) -> str:
    """Strip stem-final u/i (karu <- kar + u-vikaraNa). Lookup-gated."""
    if s.endswith(("u", "i")) and len(s) > 2:
        return s[:-1]
    return s


def _dethematic(s: str) -> str:
    if s.endswith("a") and len(s) > 2:
        return s[:-1]
    return s


def _dedouble(s: str) -> str:
    """Reverse stop gemination (tott <- tod + tf)."""
    for _gem, _sg in (("tt", "d"), ("nn", "n"), ("cc", "c"), ("YY", "Y")):
        if _gem in s:
            return s.replace(_gem, _sg, 1)
    return s


_VOICE = {"t": "d", "T": "D", "p": "b", "P": "B", "k": "g", "K": "G",
          "c": "j", "C": "J", "w": "q", "W": "Q"}


def _devoice(s: str) -> str:
    """Reverse final devoicing (tot <- tod + tavya): final tenuis -> media."""
    if len(s) > 1 and s[-1] in _VOICE:
        return s[:-1] + _VOICE[s[-1]]
    return s


def _denasal(s: str) -> str:
    """Reverse nasal place-shift (gan <- gam + tf, gaM <- gam + sa)."""
    if s.endswith("n") and len(s) > 1:
        return s[:-1] + "m"
    if s.endswith("M") and len(s) > 1:
        return s[:-1] + "m"
    return s


def _denasal_n(s: str) -> str:
    """Anusvara from dental n (taM <- tan + sa). Tried after m."""
    if s.endswith("M") and len(s) > 1:
        return s[:-1] + "n"
    return s


_OPS = [("glide", _deglide), ("guna", _deguna), ("vrddhi", _devrddhi),
        ("cutva", _decutva), ("thematic", _dethematic), ("double", _dedouble),
        ("nasal", _denasal), ("nasaln", _denasal_n), ("ur", _deur),
        ("urv", _deurv), ("ovo", _devo), ("uv", _deuv), ("yan", _deyan),
        ("devoice", _devoice)]
_OP_CONF = {"exact": 1.0, "glide": 0.95, "guna": 0.92, "thematic": 0.9,
            "irreg": 0.95, "vrddhi": 0.8, "cha": 0.8, "cutva": 0.75,
            "ur": 0.7, "urv": 0.7, "double": 0.7, "nasal": 0.7, "nasaln": 0.65,
            "ovo": 0.7, "uv": 0.6, "yan": 0.75, "devoice": 0.6}


def _via_conf(via: str) -> float:
    _parts = [p for p in via.split("+") if p in _OP_CONF]
    if not _parts:
        return 0.6
    return min(_OP_CONF[p] for p in _parts)


_LOOKUP_CACHE: Dict[str, object] = {}


def _lookup_root(cand: str):
    """Graded-closure root lookup. BFS over reverse-phonology ops (depth 2);
    first hit wins, so op order encodes plausibility. Returns
    (clean, meta, via) or None."""
    if not cand or len(cand) > 12:
        return None
    if cand in _LOOKUP_CACHE:
        return _LOOKUP_CACHE[cand]

    def _try(_s: str):
        for _c in _len_variants(_s):
            if _c in _ROOTS:
                return _c
        return None

    _seen = {cand}
    _hit = _try(cand)
    if _hit is not None:
        _res = (_hit, _ROOTS[_hit], "exact")
        _LOOKUP_CACHE[cand] = _res
        return _res
    # Natva reversal (praRamati -> nam): R could hide dental n
    if "R" in cand:
        _hit = _lookup_root(cand.replace("R", "n"))
        if _hit is not None:
            _res = (_hit[0], _hit[1], "natva+" + _hit[2])
            _LOOKUP_CACHE[cand] = _res
            return _res
    # irregular presents (gacCha <- gam, yacCha <- yam/dA)
    _irr = _irreg_pres(cand)
    if _irr is not None:
        _m, _c = _irr[0]
        _res = (_c, _m, "irreg")
        _LOOKUP_CACHE[cand] = _res
        return _res
    _level = [(cand, "")]
    for _depth in (1, 2, 3):
        _nxt: List[tuple] = []
        for (_s, _v0) in _level:
            for (_name, _fn) in _OPS:
                try:
                    _v = _fn(_s)
                except Exception:
                    continue
                if _v != _s and _v not in _seen:
                    _seen.add(_v)
                    _nxt.append((_v, _v0 + "+" + _name if _v0 else _name))
        for (_s, _vv) in _nxt:
            _hit = _try(_s)
            if _hit is not None:
                _res = (_hit, _ROOTS[_hit], _vv)
                _LOOKUP_CACHE[cand] = _res
                return _res
        _level = _nxt
        if not _level:
            break
    # -cCha- presents (gacCati <- gam, yacCati <- yam)
    if cand.endswith("cC") and len(cand) > 2:
        for _c in _len_variants(cand[:-2] + "m"):
            if _c in _ROOTS:
                _res = (_c, _ROOTS[_c], "cha")
                _LOOKUP_CACHE[cand] = _res
                return _res
    _LOOKUP_CACHE[cand] = None
    return None


def _root_details(meta: dict) -> dict:
    _d = {"dhatu": meta.get("clean"), "dhAtu_pada": meta.get("pada"),
          "sew": meta.get("sew"), "gana": meta.get("gana")}
    if meta.get("clean") in _IDS:
        _d["ids"] = list(_IDS[meta["clean"]])
    return _d


# ---------------------------------------------------------------------------
# subanta analysis by synthesis (open vocabulary)
# ---------------------------------------------------------------------------

# (strip, append, finals|None, restore|None, linga, vibhakti, vacana)
# finals/restore apply to the remainder when append == "".
_INV: List[tuple] = []


def _add(strip: str, append: str, finals, restore, linga: str, vib: int, vac: str,
         extra=None) -> None:
    _INV.append((strip, append, finals, restore, linga, vib, vac, extra or {}))


def _build_inv() -> None:
    if _INV:
        return
    _A = None  # no finals check when append != ""
    # a-masc (covers foreign words: any X+a stem)
    for _s, _v, _c in [("aH", 1, "eka"), ("O", 1, "dvi"), ("AH", 1, "bahu"),
                       ("am", 2, "eka"), ("O", 2, "dvi"), ("An", 2, "bahu"),
                       ("eRa", 3, "eka"), ("ena", 3, "eka"), ("AByAm", 3, "dvi"),
                       ("EH", 3, "bahu"), ("Aya", 4, "eka"), ("AByAm", 4, "dvi"),
                       ("eByaH", 4, "bahu"), ("At", 5, "eka"), ("AByAm", 5, "dvi"),
                       ("eByaH", 5, "bahu"), ("asya", 6, "eka"), ("ayoH", 6, "dvi"),
                       ("AnAm", 6, "bahu"), ("ARAm", 6, "bahu"), ("e", 7, "eka"),
                       ("ayoH", 7, "dvi"), ("ezu", 7, "bahu"), ("esu", 7, "bahu"),
                       ("a", 8, "eka")]:
        _add(_s, "a", _A, None, "puM", _v, _c)
    # A-fem
    for _s, _v, _c in [("A", 1, "eka"), ("e", 1, "dvi"), ("AH", 1, "bahu"),
                       ("Am", 2, "eka"), ("e", 2, "dvi"), ("AH", 2, "bahu"),
                       ("ayA", 3, "eka"), ("AByAm", 3, "dvi"), ("ABiH", 3, "bahu"),
                       ("AyE", 4, "eka"), ("AByAm", 4, "dvi"), ("AByaH", 4, "bahu"),
                       ("AyAH", 5, "eka"), ("AByAm", 5, "dvi"), ("AByaH", 5, "bahu"),
                       ("AyAH", 6, "eka"), ("ayoH", 6, "dvi"), ("AnAm", 6, "bahu"),
                       ("AyAm", 7, "eka"), ("ayoH", 7, "dvi"), ("Asu", 7, "bahu"),
                       ("e", 8, "eka")]:
        _add(_s, "A", _A, None, "strI", _v, _c)
    # i-masc
    for _s, _v, _c in [("iH", 1, "eka"), ("yO", 1, "dvi"), ("ayaH", 1, "bahu"),
                       ("im", 2, "eka"), ("yO", 2, "dvi"), ("In", 2, "bahu"),
                       ("yA", 3, "eka"), ("aye", 4, "eka"), ("eH", 5, "eka"),
                       ("eH", 6, "eka"), ("yoH", 6, "dvi"), ("InAm", 6, "bahu"),
                       ("IRAm", 6, "bahu"), ("O", 7, "eka"), ("yoH", 7, "dvi"),
                       ("izu", 7, "bahu"), ("e", 8, "eka")]:
        _add(_s, "i", _A, None, "puM", _v, _c)
    for _s, _v, _c in [("ByAm", 3, "dvi"), ("BiH", 3, "bahu"),
                       ("ByAm", 4, "dvi"), ("ByaH", 4, "bahu"),
                       ("ByAm", 5, "dvi"), ("ByaH", 5, "bahu")]:
        _add(_s, "", {"i"}, None, "puM", _v, _c)
    # I-fem long
    for _s, _v, _c in [("IH", 1, "eka"), ("yO", 1, "dvi"), ("yaH", 1, "bahu"),
                       ("Im", 2, "eka"), ("yO", 2, "dvi"), ("IH", 2, "bahu"),
                       ("yA", 3, "eka"), ("yE", 4, "eka"), ("yAH", 5, "eka"),
                       ("yAH", 6, "eka"), ("yoH", 6, "dvi"), ("InAm", 6, "bahu"),
                       ("yAm", 7, "eka"), ("yoH", 7, "dvi"), ("i", 8, "eka")]:
        _add(_s, "I", _A, None, "strI", _v, _c)
    for _s, _v, _c in [("ByAm", 3, "dvi"), ("BiH", 3, "bahu"),
                       ("ByAm", 4, "dvi"), ("ByaH", 4, "bahu"),
                       ("ByAm", 5, "dvi"), ("ByaH", 5, "bahu"),
                       ("zu", 7, "bahu")]:
        _add(_s, "", {"I"}, None, "strI", _v, _c)
    # u-masc
    for _s, _v, _c in [("uH", 1, "eka"), ("vO", 1, "dvi"), ("avaH", 1, "bahu"),
                       ("um", 2, "eka"), ("vO", 2, "dvi"), ("Un", 2, "bahu"),
                       ("vA", 3, "eka"), ("ave", 4, "eka"), ("oH", 5, "eka"),
                       ("oH", 6, "eka"), ("voH", 6, "dvi"), ("UnAm", 6, "bahu"),
                       ("O", 7, "eka"), ("voH", 7, "dvi"), ("uzu", 7, "bahu"),
                       ("o", 8, "eka")]:
        _add(_s, "u", _A, None, "puM", _v, _c)
    for _s, _v, _c in [("ByAm", 3, "dvi"), ("BiH", 3, "bahu"),
                       ("ByAm", 4, "dvi"), ("ByaH", 4, "bahu"),
                       ("ByAm", 5, "dvi"), ("ByaH", 5, "bahu")]:
        _add(_s, "", {"u"}, None, "puM", _v, _c)
    # U-fem long
    for _s, _v, _c in [("UH", 1, "eka"), ("vO", 1, "dvi"), ("vaH", 1, "bahu"),
                       ("Um", 2, "eka"), ("vO", 2, "dvi"), ("UH", 2, "bahu"),
                       ("vA", 3, "eka"), ("vE", 4, "eka"), ("vAH", 5, "eka"),
                       ("vAH", 6, "eka"), ("voH", 6, "dvi"), ("UnAm", 6, "bahu"),
                       ("vAm", 7, "eka"), ("voH", 7, "dvi"), ("u", 8, "eka")]:
        _add(_s, "U", _A, None, "strI", _v, _c)
    for _s, _v, _c in [("ByAm", 3, "dvi"), ("BiH", 3, "bahu"),
                       ("ByAm", 4, "dvi"), ("ByaH", 4, "bahu"),
                       ("ByAm", 5, "dvi"), ("ByaH", 5, "bahu"),
                       ("zu", 7, "bahu")]:
        _add(_s, "", {"U"}, None, "strI", _v, _c)
    # neuter a (1/2 only; 3-7 ride the masc rules via napuMsaka verify)
    for _s, _v, _c in [("am", 1, "eka"), ("e", 1, "dvi"), ("Ani", 1, "bahu"),
                       ("am", 2, "eka"), ("e", 2, "dvi"), ("Ani", 2, "bahu"),
                       ("am", 8, "eka")]:
        _add(_s, "a", _A, None, "napuMsaka", _v, _c)
    # neuter i/u shields (7.1.73)
    for _s, _v, _c in [("RI", 1, "dvi"), ("nI", 1, "dvi"),
                       ("RI", 2, "dvi"), ("nI", 2, "dvi"),
                       ("RA", 3, "eka"), ("nA", 3, "eka"),
                       ("Re", 4, "eka"), ("ne", 4, "eka"),
                       ("Ras", 5, "eka"), ("nas", 5, "eka"),
                       ("Ras", 6, "eka"), ("nas", 6, "eka"),
                       ("RoH", 6, "dvi"), ("noH", 6, "dvi"),
                       ("Ri", 7, "eka"), ("ni", 7, "eka"),
                       ("RoH", 7, "dvi"), ("noH", 7, "dvi"),
                       ("zu", 7, "bahu")]:
        _add(_s, "", {"i", "u"}, None, "napuMsaka", _v, _c)
    # an-stems (rAjan-type; Y/n restored by verify)
    for _s, _v, _c in [("A", 1, "eka"), ("AnO", 1, "dvi"), ("AnaH", 1, "bahu"),
                       ("Anam", 2, "eka"), ("AnO", 2, "dvi"), ("YaH", 2, "bahu"),
                       ("YA", 3, "eka"), ("aByAm", 3, "dvi"), ("aBiH", 3, "bahu"),
                       ("Ye", 4, "eka"), ("aByAm", 4, "dvi"), ("aByaH", 4, "bahu"),
                       ("YaH", 5, "eka"), ("aByAm", 5, "dvi"), ("aByaH", 5, "bahu"),
                       ("YaH", 6, "eka"), ("YoH", 6, "dvi"), ("YAm", 6, "bahu"),
                       ("nAm", 6, "bahu"), ("Yi", 7, "eka"), ("YoH", 7, "dvi"),
                       ("asu", 7, "bahu"), ("su", 7, "bahu")]:
        _add(_s, "an", _A, None, "puM", _v, _c)
    # as-stems (manas-type; z-restored for is/us)
    _RS = {"z": ["s"]}
    for _s, _v, _c in [("aH", 1, "eka"), ("O", 1, "dvi"), ("asaH", 1, "bahu"),
                       ("asam", 2, "eka"), ("O", 2, "dvi"), ("asaH", 2, "bahu")]:
        _add(_s, "as", _A, None, "puM", _v, _c)
    for _s, _v, _c in [("A", 3, "eka"), ("e", 4, "eka"), ("aH", 5, "eka"),
                       ("aH", 6, "eka"), ("oH", 6, "dvi"), ("Am", 6, "bahu"),
                       ("i", 7, "eka"), ("oH", 7, "dvi"), ("aHsu", 7, "bahu"),
                       ("O", 1, "dvi"), ("O", 2, "dvi")]:
        _add(_s, "", {"s"}, _RS, "puM", _v, _c)
    for _s, _v, _c in [("ByAm", 3, "dvi"), ("BiH", 3, "bahu"),
                       ("ByAm", 4, "dvi"), ("ByaH", 4, "bahu"),
                       ("ByAm", 5, "dvi"), ("ByaH", 5, "bahu")]:
        # manoByAm -> manas (o dropped, s restored)
        _add("o" + _s, "as", _A, None, "puM", _v, _c)
    # at/vat/vas participle stems
    for _s, _v, _c in [("an", 1, "eka"), ("antO", 1, "dvi"), ("antaH", 1, "bahu"),
                       ("antam", 2, "eka"), ("antO", 2, "dvi"), ("ataH", 2, "bahu")]:
        _add(_s, "at", _A, None, "puM", _v, _c)
    for _s, _v, _c in [("An", 1, "eka"), ("AntO", 1, "dvi"), ("AntaH", 1, "bahu"),
                       ("Antam", 2, "eka"), ("AntO", 2, "dvi")]:
        _add(_s, "at", _A, None, "puM", _v, _c)
    for _s, _v, _c in [("vAn", 1, "eka"), ("vantO", 1, "dvi"), ("vantaH", 1, "bahu"),
                       ("vantam", 2, "eka"), ("vantO", 2, "dvi"), ("vataH", 2, "bahu")]:
        _add(_s, "vat", _A, None, "puM", _v, _c)
    for _s, _v, _c in [("vAn", 1, "eka"), ("vAMsO", 1, "dvi"), ("vAMsaH", 1, "bahu"),
                       ("vAMsam", 2, "eka"), ("vAMsO", 2, "dvi"),
                       ("uzA", 3, "eka"), ("uze", 4, "eka"),
                       ("uzaH", 5, "eka"), ("uzaH", 6, "eka"),
                       ("uzoH", 6, "dvi"), ("uzAm", 6, "bahu"),
                       ("uzi", 7, "eka"), ("uzoH", 7, "dvi")]:
        _add(_s, "vas", _A, None, "puM", _v, _c)
    # in-stems
    for _s, _v, _c in [("I", 1, "eka"), ("inO", 1, "dvi"), ("inaH", 1, "bahu"),
                       ("inam", 2, "eka"), ("inO", 2, "dvi"), ("inaH", 2, "bahu")]:
        _add(_s, "in", _A, None, "puM", _v, _c)
    # c-stems
    for _s, _v, _c in [("k", 1, "eka"), ("cO", 1, "dvi"), ("caH", 1, "bahu"),
                       ("cam", 2, "eka"), ("cO", 2, "dvi"), ("caH", 2, "bahu"),
                       ("cA", 3, "eka"), ("ce", 4, "eka"),
                       ("caH", 5, "eka"), ("caH", 6, "eka"),
                       ("coH", 6, "dvi"), ("cAm", 6, "bahu"),
                       ("ci", 7, "eka"), ("coH", 7, "dvi")]:
        _add(_s, "c", _A, None, "strI", _v, _c)
    for _s, _v, _c in [("gByAm", 3, "dvi"), ("gBiH", 3, "bahu"),
                       ("gByAm", 4, "dvi"), ("gByaH", 4, "bahu"),
                       ("gByAm", 5, "dvi"), ("gByaH", 5, "bahu"),
                       ("kzu", 7, "bahu")]:
        _add(_s, "c", _A, None, "strI", _v, _c)
    # f-stems (kartf/agent Ar vs pitf/kin ar; verify picks the grade)
    for _s, _v, _c in [("A", 1, "eka"), ("arO", 1, "dvi"), ("ArO", 1, "dvi"),
                       ("araH", 1, "bahu"), ("AraH", 1, "bahu"),
                       ("aram", 2, "eka"), ("Aram", 2, "eka"),
                       ("rA", 3, "eka"), ("re", 4, "eka"),
                       ("uH", 5, "eka"), ("uH", 6, "eka"),
                       ("roH", 6, "dvi"), ("roH", 7, "dvi"),
                       ("ari", 7, "eka"), ("ar", 8, "eka")]:
        _add(_s, "f", _A, None, "puM", _v, _c)
    for _s, _v, _c in [("FRaH", 2, "bahu"), ("rARAm", 6, "bahu"),
                       ("FRAm", 6, "bahu")]:
        _add(_s, "f", _A, None, "puM", _v, _c)
    for _s, _v, _c in [("fByAm", 3, "dvi"), ("fBiH", 3, "bahu"),
                       ("fByAm", 4, "dvi"), ("fByaH", 4, "bahu"),
                       ("fByAm", 5, "dvi"), ("fByaH", 5, "bahu"),
                       ("fzu", 7, "bahu")]:
        _add(_s, "", {"f"}, None, "puM", _v, _c)
    # bare at/final nominatives: abhyasta (dadat, 7.1.78, no num) + neuter
    _add("", "", {"t"}, None, "puM", 1, "eka", {"abhyasta": True})
    _add("", "", {"t"}, None, "napuMsaka", 1, "eka")
    _add("", "", {"f"}, None, "napuMsaka", 1, "eka")
    _add("", "", {"f"}, None, "napuMsaka", 2, "eka")


def _subanta_open(word: str) -> List[dict]:
    _build_inv()
    se = SubantaEngine()
    out: List[dict] = []
    seen = set()
    for (_strip, _append, _finals, _restore, _li, _vib, _vac, _ex) in _INV:
        if not word.endswith(_strip):
            continue
        _core = word[:-len(_strip)] if _strip else word
        if _strip and not _core:
            continue
        _cands = [_core]
        if _restore and _core and _core[-1] in _restore:
            for _r in _restore[_core[-1]]:
                _cands.append(_core[:-1] + _r)
        for _cd in _cands:
            if _append:
                _stem = _cd + _append
            else:
                if _finals and (_cd[-1:] not in _finals):
                    continue
                _stem = _cd
            if not _stem or len(_stem) < 2:
                continue
            _key = (_stem, _li, _vib, _vac)
            if _key in seen:
                continue
            seen.add(_key)
            try:
                _forms = se.decline(_stem, _li, extra=_ex).get((_vib, _vac), [])
            except Exception:
                continue
            if word not in _forms and _stem.endswith(("at", "ant")) and not _ex:
                # participle stems verify under satf-extra (Bavat->Bavan,
                # not the pronoun BavAn)
                try:
                    _forms = se.decline(_stem, _li,
                                        extra={"satf": True}).get((_vib, _vac), [])
                except Exception:
                    _forms = []
            if word in _forms:
                # bare-stem vocatives are the weakest open evidence:
                # same-shape self-readings (foreign stems) 0.5, grade-changed
                # ones (dadAti -> dadAtI) 0.6, real inflections 0.75
                if (_vib, _vac) == (8, "eka"):
                    _conf = 0.5 if _stem == word else 0.6
                else:
                    _conf = 0.75
                out.append({"kind": "subanta", "stem": _stem, "linga": _li,
                            "vibhakti": _vib, "vacana": _vac,
                            "confidence": _conf, "lexicon": False})
    return out


# ---------------------------------------------------------------------------
# krdanta analysis (affix signature + root lookup)
# ---------------------------------------------------------------------------

def _krdanta_from_stem(stem: str, linga: str, vib: int, vac: str) -> List[dict]:
    out: List[dict] = []

    def _emit(prat: str, root: str | None, meta, conf: float, note: str = "") -> None:
        _d = {"kind": "krdanta", "pratyaya": prat, "stem": stem,
              "linga": linga, "vibhakti": vib, "vacana": vac,
              "confidence": conf}
        if root is not None and meta is not None:
            _d.update(_root_details(meta))
        else:
            _d["dhatu"] = None
        if note:
            _d["note"] = note
        out.append(_d)

    # kta / ktavatu via exact kta-stem map (handles all sandhi irregulars)
    _core = stem[:-1] + "a" if stem.endswith("A") else stem
    if _core in _KTA_MAP:
        _rt = _KTA_MAP[_core]
        _emit("kta", _rt, _ROOTS[_rt], 0.95)
    if stem.endswith("vat") and stem[:-3] in _KTA_MAP:
        _rt = _KTA_MAP[stem[:-3]]
        _emit("ktavatu", _rt, _ROOTS[_rt], 0.95)
    if stem.endswith("vAn") and stem[:-3] in _KTA_MAP:
        _rt = _KTA_MAP[stem[:-3]]
        _emit("ktavatu", _rt, _ROOTS[_rt], 0.95)
    # tavya / anIyar / yat via graded closure (iT, natva, geminates inside)
    if stem.endswith("tavya"):
        _hit = _lookup_root(stem[:-5])
        if _hit is None and stem.endswith("itavya"):
            _hit = _lookup_root(stem[:-6])  # sew iT (Bavi -> Bav)
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("tavya", _rt, _m, 0.85, f"root via {_via}")
        else:
            _emit("tavya", None, None, 0.5, "root unresolved")
    for _suf, _restore in (("anIya", ""), ("RIya", ""), ("AnIya", "A")):
        if stem.endswith(_suf):
            # natva/vrddhi sit inside the suffix (karaRIya, dAnIya)
            _hit = _lookup_root(stem[:-len(_suf)] + _restore)
            if _hit is not None:
                _rt, _m, _via = _hit
                _emit("anIyar", _rt, _m, 0.85, f"root via {_via}")
            else:
                _emit("anIyar", None, None, 0.5, "root unresolved")
            break
    if stem.endswith("ya") and len(stem) > 3:
        _hit = _lookup_root(_devrddhi(stem[:-2]))
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("yat", _rt, _m, 0.85, f"root via {_via}")
    # SAnac (muk -mAna-, plain -Ana, natva -ARa-, passive -yak-)
    for _suf, _cut in (("mARa", 4), ("ARa", 3), ("mAna", 4), ("Ana", 3)):
        if stem.endswith(_suf):
            _b = stem[:-_cut]
            _cands = [_b]
            if _b.endswith("a") and len(_b) > 1:
                _cands.append(_b[:-1])  # thematic (labha -> labh)
            if _b.endswith("m") and len(_b) > 1:
                _cands.append(_b[:-1])  # muk (tudam -> tuda -> tud)
                if _b[:-1].endswith("a") and len(_b) > 2:
                    _cands.append(_b[:-2])
            if _b.endswith("ya") and len(_b) > 2:
                _cands.append(_b[:-2])  # yak (BUya -> BU)
            for _c in _cands:
                _hit = _lookup_root(_c)
                if _hit is not None:
                    break
            if _hit is not None:
                _rt, _m, _via = _hit
                _emit("SAnac", _rt, _m, 0.8, f"root via {_via}")
            else:
                _emit("SAnac", None, None, 0.5, "present stem; root unresolved")
            break
    # lyuw action noun (-ana): Bavana <- BU; Natva-R twin (-aRa): vidaRa <- vid
    if (stem.endswith("ana") or stem.endswith("aRa")) and len(stem) > 4:
        _hit = _lookup_root(stem[:-3])
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("lyuw", _rt, _m, 0.8, f"root via {_via}")
    # GaY (vrddhi + a: BAva <- BU) vs ac (guNa + a: toda <- tud);
    # feminine -A forms take the "a" label (todA)
    if (stem.endswith("a") and len(stem) > 2) or \
            (stem.endswith("A") and len(stem) > 2):
        _fem = stem.endswith("A")
        _b = stem[:-1]
        _hit = _lookup_root(_b)
        if _hit is None and _b.endswith("R") and len(_b) > 2:
            # Natva-R stem (vidaRa <- vid + lyuw): R hides the root
            # coda, so retry without it (vida -> vid via thematic)
            _hit = _lookup_root(_b[:-1])
        if _hit is not None:
            _rt, _m, _via = _hit
            _vrddhi = ("A" in _b or "Ay" in _b or "Av" in _b or "E" in _b
                       or "O" in _b)
            if _fem:
                _emit("a", _rt, _m, 0.7, f"root via {_via}")
            elif _vrddhi:
                _emit("GaY", _rt, _m, 0.7, f"root via {_via}")
            else:
                _emit("ac", _rt, _m, 0.6, f"root via {_via}")
    # Rvul / tfc
    if stem.endswith("aka") or stem.endswith("ikA"):
        _b = stem[:-3]
        _hit = _lookup_root(_devrddhi(_b))
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("Rvul", _rt, _m, 0.85, f"root via {_via}")
    if stem.endswith("tf") or stem.endswith("trI"):
        # vowel base (Bavi + tf) vs consonant base (tott + f, d devoiced+geminated)
        _b = stem[:-2] if stem.endswith("tf") else stem[:-3]
        _cands = [_b, stem[:-1]]
        if _b.endswith("i") and len(_b) > 1:
            _cands.append(_b[:-1])  # sew iT (Bavi -> Bav)
        for _c in _cands:
            _hit = _lookup_root(_c)
            if _hit is not None:
                break
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("tfc", _rt, _m, 0.85, f"root via {_via}")
    # Satf present stem: irregulars (multi-root) first, then abhyasa,
    # then plain closure (Bav/tud regulars, gacCh via cha).
    # Guard excludes ktavatu (-tavat); juhvat-type (-hvat) stays eligible.
    if stem.endswith("ant") or (stem.endswith("at") and not stem.endswith("tavat")):
        _core = stem[:-3] if stem.endswith("ant") else stem[:-2]
        _done = False
        _seen_rt = set()
        _irr = _irreg_pres(_core)
        if _irr is not None:
            for (_m, _c) in _irr:
                _emit("Satf", _c, _m, 0.9, "irregular present stem")
                _seen_rt.add(_c)
            _done = True
        # plain closure (Bav/tud regulars, gacCh via cha) AND abhyasa
        # both emit: dadat is genuinely dad-Satf and dA-Satf at once
        _hit = _lookup_root(_core)
        if _hit is not None:
            _rt, _m, _via = _hit
            if _rt not in _seen_rt:
                _emit("Satf", _rt, _m, 0.85, f"root via {_via}")
                _seen_rt.add(_rt)
            _done = True
        for _cand in _abhyasa_reverse(_core):
            _hit = _lookup_root(_cand)
            if _hit is not None:
                _rt, _m, _via = _hit
                if _rt not in _seen_rt:
                    _emit("Satf", _rt, _m, 0.7, "root via abhyasa")
                    _seen_rt.add(_rt)
                _done = True
        if not _done:
            out.append({"kind": "krdanta", "pratyaya": "Satf", "stem": stem,
                        "dhatu": None, "linga": linga, "vibhakti": vib,
                        "vacana": vac, "confidence": 0.45,
                        "note": "present stem; root unresolved in v1"})
    # kvasu weak/middle without kta link
    if stem.endswith("uz") or stem.endswith("uzI"):
        out.append({"kind": "krdanta", "pratyaya": "kvasu", "stem": stem,
                    "dhatu": None, "linga": linga, "vibhakti": vib,
                    "vacana": vac, "confidence": 0.45,
                    "note": "samprasarana stem; root unresolved in v1"})
    return out


# ---------------------------------------------------------------------------
# tinanta analysis (ending table + root lookup)
# ---------------------------------------------------------------------------

# (ending, lakara|None, purusha, vacana, pada) — lakara None = ambiguous set
_TIN_P: List[tuple] = [
    ("anti", "lw", "prathama", "bahu"), ("taH", "lw", "prathama", "dvi"),
    ("ti", "lw", "prathama", "eka"), ("si", "lw", "madhyama", "eka"),
    ("TaH", "lw", "madhyama", "dvi"), ("Ta", "lw", "madhyama", "bahu"),
    ("mi", "lw", "uttama", "eka"), ("vaH", "lw", "uttama", "dvi"),
    ("maH", "lw", "uttama", "bahu"),
    ("an", "laN", "prathama", "bahu"), ("tAm", "laN", "prathama", "dvi"),
    ("t", "laN", "prathama", "eka"), ("aH", "laN", "madhyama", "eka"),
    ("tam", "laN", "madhyama", "dvi"), ("ta", "laN", "madhyama", "bahu"),
    ("am", "laN", "uttama", "eka"), ("va", "laN", "uttama", "dvi"),
    ("ma", "laN", "uttama", "bahu"),
    ("antu", "low", "prathama", "bahu"), ("tAm", "low", "prathama", "dvi"),
    ("tAt", "low", "prathama", "eka"), ("tu", "low", "prathama", "eka"),
    ("tam", "low", "madhyama", "dvi"), ("ta", "low", "madhyama", "bahu"),
    ("hi", "low", "madhyama", "eka"), ("Ani", "low", "uttama", "eka"),
    ("ARi", "low", "uttama", "eka"),
    ("Ava", "low", "uttama", "dvi"), ("Ama", "low", "uttama", "bahu"),
    ("", "low", "madhyama", "eka"), ("tAt", "low", "madhyama", "eka"),
    ("tAt", "low", "prathama", "eka"),
    ("nti", "lw", "prathama", "bahu"),
    ("ati", "lw", "prathama", "bahu"),
    ("zi", "lw", "madhyama", "eka"),
    ("eyuH", "viDiliN", "prathama", "bahu"), ("etAm", "viDiliN", "prathama", "dvi"),
    ("et", "viDiliN", "prathama", "eka"), ("eH", "viDiliN", "madhyama", "eka"),
    ("etam", "viDiliN", "madhyama", "dvi"), ("eta", "viDiliN", "madhyama", "bahu"),
    ("eyam", "viDiliN", "uttama", "eka"), ("eva", "viDiliN", "uttama", "dvi"),
    ("ema", "viDiliN", "uttama", "bahu"),
    ("a", "liw", "prathama", "eka"), ("atuH", "liw", "prathama", "dvi"),
    ("uH", "liw", "prathama", "bahu"), ("iTa", "liw", "madhyama", "eka"),
    ("Ta", "liw", "madhyama", "eka"), ("aTuH", "liw", "madhyama", "dvi"),
    ("a", "liw", "madhyama", "bahu"), ("a", "liw", "uttama", "eka"),
    ("iva", "liw", "uttama", "dvi"), ("ima", "liw", "uttama", "bahu"),
    ("O", "liw", "prathama", "eka"), ("O", "liw", "uttama", "eka"),
]
_TIN_A: List[tuple] = [
    ("ante", "lw", "prathama", "bahu"), ("ete", "lw", "prathama", "dvi"),
    ("te", "lw", "prathama", "eka"), ("se", "lw", "madhyama", "eka"),
    ("ze", "lw", "madhyama", "eka"),
    ("e", "lw", "uttama", "eka"), ("e", "laN", "uttama", "eka"),
    ("eTe", "lw", "madhyama", "dvi"), ("Dve", "lw", "madhyama", "bahu"),
    ("e", "lw", "uttama", "eka"), ("vahe", "lw", "uttama", "dvi"),
    ("mahe", "lw", "uttama", "bahu"),
    ("anta", "laN", "prathama", "bahu"), ("etAm", "laN", "prathama", "dvi"),
    ("ta", "laN", "prathama", "eka"), ("TAH", "laN", "madhyama", "eka"),
    ("eTAm", "laN", "madhyama", "dvi"), ("Dvam", "laN", "madhyama", "bahu"),
    ("i", "laN", "uttama", "eka"), ("vahi", "laN", "uttama", "dvi"),
    ("mahi", "laN", "uttama", "bahu"),
    ("antAm", "low", "prathama", "bahu"), ("etAm", "low", "prathama", "dvi"),
    ("tAm", "low", "prathama", "eka"), ("sva", "low", "madhyama", "eka"),
    ("eTAm", "low", "madhyama", "dvi"), ("Dvam", "low", "madhyama", "bahu"),
    ("E", "low", "uttama", "eka"), ("AvahE", "low", "uttama", "dvi"),
    ("AmahE", "low", "uttama", "bahu"),
    ("eran", "viDiliN", "prathama", "bahu"), ("eyAtAm", "viDiliN", "prathama", "dvi"),
    ("eta", "viDiliN", "prathama", "eka"), ("eTAH", "viDiliN", "madhyama", "eka"),
    ("eyATAm", "viDiliN", "madhyama", "dvi"), ("eDvam", "viDiliN", "madhyama", "bahu"),
    ("eya", "viDiliN", "uttama", "eka"), ("evahi", "viDiliN", "uttama", "dvi"),
    ("emahi", "viDiliN", "uttama", "bahu"),
    ("e", "liw", "prathama", "eka"), ("Ate", "liw", "prathama", "dvi"),
    ("ire", "liw", "prathama", "bahu"), ("ize", "liw", "madhyama", "eka"),
    ("ATe", "liw", "madhyama", "dvi"), ("iDve", "liw", "madhyama", "bahu"),
    ("i", "liw", "uttama", "eka"), ("vahe", "liw", "uttama", "dvi"),
    ("mahe", "liw", "uttama", "bahu"),
]
# t/d voicing twins (BavatAt/BavatAd, aBavat/aBavad: final -t voices to -d;
# JSON finals show exact t/d symmetry, 4432/4432, with no D-forms, so only
# dental twins are added, sharing the base ending's slot)
for _t, _pada in ((_TIN_P, None), (_TIN_A, None)):
    for (_end, _lak, _pur, _vac) in list(_t):
        if _end.endswith("t"):
            _t.append((_end[:-1] + "d", _lak, _pur, _vac))


def _tin_candidates(core: str, lakara: str, aug: bool) -> List[str]:
    # stripped variants first: exact hits on them outrank longer paths
    cands = []
    if core.endswith("a") and len(core) > 1:
        cands.append(core[:-1])  # thematic -a-
    if core.endswith("A") and len(core) > 1:
        cands.append(core[:-1])  # thematic -A- (uttama Ami/AvaH/AmaH twins)
    cands.append(core)
    for _c in list(cands):
        # karmani/passive -ya- (BUyate <- BU + yak)
        if _c.endswith("ya") and len(_c) > 2 and _c[:-2] not in cands:
            cands.append(_c[:-2])
    if aug:
        _stripped = []
        for _c in cands:
            if _c.startswith("a") and len(_c) > 1:
                _stripped.append(_c[1:])  # laN augment a-
            elif _c.startswith("A") and len(_c) > 1:
                _stripped.append(_c[1:])
        cands += _stripped
    return cands


def _infix_reverse(word: str, upasarga: str | None = None) -> List[dict]:
    """Direct reversal for affixed/periphrastic lakaras (no tin ending):
    luT -tA- (BavitA/vaktA), lfT/lfN -sya- (Bavizyati), luN -sic- (akArzIt),
    ASIrliN -yA- (BUyAt), liT reduplication (cakAra, uvAca)."""
    out: List[dict] = []

    def _emit(_rt: str, _m, _lak: str, _pur: str, _vac: str, _via: str,
              _conf: float, _stem_note: str, _pada: str = "parasmaipada",
              _sanadi=None) -> None:
        _d = {"kind": "tinanta", "purusha": _pur, "vacana": _vac,
              "pada": _pada, "prayoga": "kartari", "lakara": _lak,
              "confidence": _conf, "ending": "-",
              "note": f"root via {_via} from stem '{_stem_note}'"}
        _d.update(_root_details(_m))
        _d["pada"] = "parasmaipada"
        if upasarga:
            _d["upasarga"] = upasarga
            _d["confidence"] = max(0.1, _d["confidence"] - 0.1)
        _ids = _d.get("ids") or [None]
        if not _verify_tin(word, _rt, _lak, _pur, _vac, "kartari", _sanadi,
                           _ids[0], upasarga):
            _d["confidence"] = max(0.1, _d["confidence"] * 0.5)
            _d["note"] += "; unverified"
        out.append(_d)

    # luT periphrastic future (-tA-): BavitA, vaktA, kartA
    _LUT = [("tArO", "prathama", "dvi", "parasmaipada"),
            ("tAraH", "prathama", "bahu", "parasmaipada"),
            ("tAsi", "madhyama", "eka", "parasmaipada"),
            ("tAsTaH", "madhyama", "dvi", "parasmaipada"),
            ("tAsTa", "madhyama", "bahu", "parasmaipada"),
            ("tAsmi", "uttama", "eka", "parasmaipada"),
            ("tAsvaH", "uttama", "dvi", "parasmaipada"),
            ("tAsmaH", "uttama", "bahu", "parasmaipada"),
            ("tAse", "madhyama", "eka", "Atmanepada"),
            ("tAsATe", "madhyama", "dvi", "Atmanepada"),
            ("tADve", "madhyama", "bahu", "Atmanepada"),
            ("tAhe", "uttama", "eka", "Atmanepada"),
            ("tAsvahe", "uttama", "dvi", "Atmanepada"),
            ("tAsmahe", "uttama", "bahu", "Atmanepada"),
            ("tA", "prathama", "eka", "parasmaipada")]
    for _suf, _pur, _vac, _pada in _LUT:
        if word.endswith(_suf) and len(word) > len(_suf) + 1:
            _core = word[:-len(_suf)]
            _cands = [_core]
            if _core.endswith("i") and len(_core) > 1:
                _cands.append(_core[:-1])  # sew iT (Bavi -> Bav)
            _luw_hits: list = []
            for _c in _cands:
                _hit = _lookup_root(_c)
                if _hit is not None and _hit[0] not in [h[0] for h in _luw_hits]:
                    _luw_hits.append((_hit[0], _hit[1], "exact", None))
                # secondary future stems (buBUzitA <- BU + sannanta)
                for _ab in _abhyasa_reverse(_c):
                    _ah = _lookup_root(_ab)
                    if _ah is not None and _ah[0] not in [h[0] for h in _luw_hits]:
                        _luw_hits.append((_ah[0], _ah[1], "abhyasa", None))
                for _sn in _san_reverse(_c):
                    _sh = _lookup_root(_sn)
                    if _sh is not None and _sh[0] not in [h[0] for h in _luw_hits]:
                        _luw_hits.append((_sh[0], _sh[1], "san", "sannanta"))
            for (_rt, _m, _via, _sd) in _luw_hits:
                _emit(_rt, _m, "luw", _pur, _vac, _via,
                      0.85 if _via == "exact" else 0.7, _core, _pada,
                      _sanadi=_sd)
            if _luw_hits:
                break
    # lfT/lfN (-sya- under a tin ending): Bavizyati, aBavizyat.
    # The stripped ending supplies purusha/vacana/pada; augment picks lfN.
    # "ati" is the abhyasta 3pl (dadati) and never a future ending.
    for _end, _slots in _END_SLOTS:
        if _end == "ati":
            continue
        if word.endswith(_end) and len(word) > len(_end) + 3:
            _stem = word[:-len(_end)] if _end else word
            if not (_stem.endswith("sya") or _stem.endswith("zya") or
                    _stem.endswith("syA") or _stem.endswith("zyA") or
                    _stem.endswith("sy") or _stem.endswith("zy")):
                continue
            _core = _stem[:-3] if _stem[-3:] in ("sya", "zya", "syA", "zyA") \
                else _stem[:-2]
            _cands = [_core]
            if _core.endswith("i") and len(_core) > 1:
                _cands.append(_core[:-1])  # sew iT
            if _core.endswith("t") and len(_core) > 1:
                # ts-fusion reversal (totsya <- tod + sya)
                _cands.append(_core[:-1] + "d")
                _cands.append(_core[:-1] + "D")
            _aug = _stem[:1] in ("a", "A")
            _hit = None
            _san_hit = None
            for _c in _cands:
                _try = [_c]
                if _aug and len(_c) > 1:
                    _try.append(_c[1:])  # lfN augment
                for _t in _try:
                    _hit = _lookup_root(_t)
                    if _hit is not None:
                        break
                    # secondary future stems (buBUzizyati <- BU + sannanta):
                    # undo reduplication / desiderative formation first
                    for _ab in _abhyasa_reverse(_t):
                        _hit = _lookup_root(_ab)
                        if _hit is not None:
                            _hit = (_hit[0], _hit[1], "abhyasa")
                            break
                    if _hit is not None:
                        break
                    for _sn in _san_reverse(_t):
                        _hit = _lookup_root(_sn)
                        if _hit is not None:
                            _hit = (_hit[0], _hit[1], "san")
                            break
                    if _hit is not None:
                        break
                if _hit is not None:
                    # abhyasa hits can shadow san twins (buBUz -> BUz hides
                    # buBUz -> BU): scan every stem candidate for the twin,
                    # not just the one that hit first
                    for _c2 in _cands:
                        _t2s = [_c2]
                        if _aug and len(_c2) > 1:
                            _t2s.append(_c2[1:])
                        for _t2 in _t2s:
                            for _sn in _san_reverse(_t2):
                                _sh = _lookup_root(_sn)
                                if _sh is not None and _sh[0] != _hit[0]:
                                    _san_hit = (_sh[0], _sh[1], "san")
                                    break
                            if _san_hit is not None:
                                break
                        if _san_hit is not None:
                            break
                    break
            if _hit is None:
                continue
            _aug = _stem[:1] in ("a", "A")
            _all_hits = [_hit] + ([_san_hit] if _san_hit is not None else [])
            for (_rt, _m, _via) in _all_hits:
                for (_pur, _vac, _pada) in _slots:
                    _d = {"kind": "tinanta", "purusha": _pur, "vacana": _vac,
                          "pada": _pada, "prayoga": "kartari",
                          "lakara": "lfN" if _aug else "lfw",
                          "confidence": 0.8, "ending": _end,
                          "note": f"root via {_via} from stem '{_core}'"}
                    _d.update(_root_details(_m))
                    _d["pada"] = _pada
                    if upasarga:
                        _d["upasarga"] = upasarga
                        _d["confidence"] = max(0.1, _d["confidence"] - 0.1)
                    out.append(_d)
            break
    # ASIrliN parasmaipada (-yA-): BUyAt, kuryAt
    _ASI = [("yAstAm", "prathama", "dvi"), ("yAsuH", "prathama", "bahu"),
            ("yAstam", "madhyama", "dvi"), ("yAsta", "madhyama", "bahu"),
            ("yAsam", "uttama", "eka"), ("yAsva", "uttama", "dvi"),
            ("yAsma", "uttama", "bahu"), ("yAt", "prathama", "eka"),
            ("yAd", "prathama", "eka"),
            ("yAH", "madhyama", "eka")]
    # ASIrliN Atmanepada s-forms (-sIy-): vedizIzwa, vedizIran (+z twins)
    for _suf, _pur, _vac in _ASI:
        if word.endswith(_suf) and len(word) > len(_suf):
            _core = word[:-len(_suf)]
            _asi_hits: list = []
            _hit = _lookup_root(_core)
            if _hit is not None:
                _asi_hits.append((_hit[0], _hit[1], "exact", None))
            if _hit is None and _core.endswith("ur"):
                # kur <- kf via u-samprasarana (kuryAt)
                _hit = _lookup_root(_core[:-2] + "f")
                if _hit is not None:
                    _asi_hits.append((_hit[0], _hit[1], "exact", None))
            # secondary benedictive stems (buBUzyAt <- BU + sannanta)
            for _ab in _abhyasa_reverse(_core):
                _ah = _lookup_root(_ab)
                if _ah is not None and _ah[0] not in [h[0] for h in _asi_hits]:
                    _asi_hits.append((_ah[0], _ah[1], "abhyasa", None))
            for _sn in _san_reverse(_core):
                _sh = _lookup_root(_sn)
                if _sh is not None and _sh[0] not in [h[0] for h in _asi_hits]:
                    _asi_hits.append((_sh[0], _sh[1], "san", "sannanta"))
            for (_rt, _m, _via, _sd) in _asi_hits:
                _emit(_rt, _m, "ASIrliN", _pur, _vac, _via, 0.8, _core,
                      _sanadi=_sd)
            if _asi_hits:
                break
    _ASI_ATM = [("IzWam", "madhyama", "dvi"), ("IDvam", "madhyama", "bahu"),
                ("IyA", "uttama", "eka"), ("Iya", "uttama", "eka"),
                ("Ivahi", "uttama", "dvi"), ("Imahi", "uttama", "bahu"),
                ("Iran", "prathama", "bahu"), ("IyAstAm", "prathama", "dvi"),
                ("IyAsTAm", "madhyama", "dvi"), ("Izwa", "prathama", "eka"),
                ("IzWAH", "madhyama", "eka")]
    for _suf, _pur, _vac in _ASI_ATM:
        # z/s twins (satva after i, dental elsewhere: vedizI- vs dasI-)
        _twins = {_suf, _suf.replace("z", "s"), _suf.replace("s", "z")}
        for _zsuf in sorted(_twins, key=lambda s: (len(s), s), reverse=True):
            if word.endswith(_zsuf) and len(word) > len(_zsuf) + 2:
                _stem = word[:-len(_zsuf)]
                _seen2, _front = set(), [_stem]
                _hit = None
                while _front:
                    _b = _front.pop(0)
                    if _b in _seen2:
                        continue
                    _seen2.add(_b)
                    for _c in [_b] + ([_b[:-1]] if _b.endswith(("i", "I")) and len(_b) > 1 else []):
                        _hit = _lookup_root(_c)
                        if _hit is not None:
                            break
                    if _hit is not None:
                        break
                    if _b.endswith(("s", "z")) and len(_b) > 1:
                        _front.append(_b[:-1])
                _atm_hits: list = []
                if _hit is not None:
                    _atm_hits.append((_hit[0], _hit[1], "exact", None))
                # secondary stems (san/nich benedictives): reversals as twins
                _stripped = ([_stem[:-1]] if _stem.endswith(("i", "I"))
                             and len(_stem) > 1 else [])
                for _c in [_stem] + _stripped:
                    for _ab in _abhyasa_reverse(_c):
                        _ah = _lookup_root(_ab)
                        if _ah is not None and _ah[0] not in [h[0] for h in _atm_hits]:
                            _atm_hits.append((_ah[0], _ah[1], "abhyasa", None))
                    for _sn in _san_reverse(_c):
                        _sh = _lookup_root(_sn)
                        if _sh is not None and _sh[0] not in [h[0] for h in _atm_hits]:
                            _atm_hits.append((_sh[0], _sh[1], "san", "sannanta"))
                for (_rt, _m, _via, _sd) in _atm_hits:
                    _emit(_rt, _m, "ASIrliN", _pur, _vac, _via, 0.75, _stem,
                          "Atmanepada", _sanadi=_sd)
                if _atm_hits:
                    break
        else:
            continue
        break
    # luN aorist (augment required): s-aorist akArzIt (sic stripped),
    # root aorist aBUt. Endings carry their OWN slots (dual -tAm etc.
    # differ from laN); Atmanepada twins ride along.
    _LUN_ENDS = ["It", "TAm", "uH", "IH", "Tam", "ta", "izam", "Ava",
                 "Ama", "t", "d", "tAm", "an", "am", "Am", "Im", "Um", "va",
                 "ma", "s", "a", "tam", "ad", "wam", "Id", "H", "sva", "sma"]
    # Atmanepada aorist twins (gam Atm: agAMsTAm, agAMsizwa...)
    _LUN_ATM = ["zwA", "zwa", "zuH", "wAm", "zWAH", "zWam", "Dvam",
                "zi", "zvahi", "zmahi", "AtAm", "TAm", "swa"]
    _LUN_SLOTS = {
        "It": [("prathama", "eka", "parasmaipada")],
        "TAm": [("prathama", "dvi", "parasmaipada")],
        "uH": [("prathama", "bahu", "parasmaipada")],
        "IH": [("madhyama", "eka", "parasmaipada")],
        "Tam": [("madhyama", "dvi", "parasmaipada")],
        "ta": [("madhyama", "bahu", "parasmaipada"),
               ("prathama", "eka", "Atmanepada")],
        "izam": [("uttama", "eka", "parasmaipada")],
        "Ava": [("uttama", "dvi", "parasmaipada")],
        "Ama": [("uttama", "bahu", "parasmaipada")],
        "t": [("prathama", "eka", "parasmaipada")],
        "d": [("prathama", "eka", "parasmaipada")],
        "tAm": [("prathama", "dvi", "parasmaipada")],
        "an": [("prathama", "bahu", "parasmaipada")],
        "am": [("uttama", "eka", "parasmaipada")],
        "Am": [("uttama", "eka", "parasmaipada")],
        "Im": [("uttama", "eka", "parasmaipada")],
        "Um": [("uttama", "eka", "parasmaipada")],
        "va": [("uttama", "dvi", "parasmaipada")],
        "ma": [("uttama", "bahu", "parasmaipada")],
        "s": [("madhyama", "eka", "parasmaipada")],
        "a": [("prathama", "eka", "parasmaipada")],
        "tam": [("madhyama", "dvi", "parasmaipada")],
        "ad": [("prathama", "eka", "parasmaipada")],
        "wam": [("madhyama", "dvi", "Atmanepada")],
        "Id": [("prathama", "eka", "parasmaipada")],
        "H": [("madhyama", "eka", "parasmaipada")],
        "sva": [("uttama", "dvi", "parasmaipada")],
        "sma": [("uttama", "bahu", "parasmaipada")],
    }
    _LUN_ATM_SLOTS = {
        "zwA": [("prathama", "eka", "Atmanepada")],
        "zwa": [("prathama", "eka", "Atmanepada")],
        "zuH": [("prathama", "bahu", "Atmanepada")],
        "wAm": [("prathama", "dvi", "Atmanepada")],
        "zWAH": [("madhyama", "eka", "Atmanepada")],
        "zWam": [("madhyama", "dvi", "Atmanepada")],
        "Dvam": [("madhyama", "bahu", "Atmanepada")],
        "zi": [("uttama", "eka", "Atmanepada")],
        "zvahi": [("uttama", "dvi", "Atmanepada")],
        "zmahi": [("uttama", "bahu", "Atmanepada")],
        "AtAm": [("prathama", "dvi", "Atmanepada")],
        "TAm": [("madhyama", "dvi", "Atmanepada")],
        "swa": [("madhyama", "bahu", "parasmaipada")],
    }
    if word[:1] in ("a", "A") and len(word) > 3:
        for _suf in sorted(_LUN_ENDS + _LUN_ATM, key=len, reverse=True):
            if word.endswith(_suf) and len(word) > len(_suf) + 1:
                _stem = word[:-len(_suf)] if _suf else word
                _slots = _LUN_SLOTS.get(_suf, _LUN_ATM_SLOTS.get(_suf))
                if _slots is None:
                    continue
                # peel sic-s/z, sew-iT, reduplicated -v- and augment -v-
                # in any order, collecting every root hit (akArzizam,
                # aBAvvam: BAvv->BAv->BU)
                _seen_bases = set()
                _frontier = [_stem[1:]]  # strip augment
                _hit = None
                _hits = []
                while _frontier:
                    _b = _frontier.pop(0)
                    if _b in _seen_bases:
                        continue
                    _seen_bases.add(_b)
                    _cands = [_b]
                    # vowel-final roots: stripping am/Am ate root vowel
                    # (adAm -Am -> d; restore dA for dA root)
                    if _suf in ("am", "Am", "Im", "Um",
                                "Ava", "Ama"):
                        for _vv in ("A", "a", "I", "i", "U", "u"):
                            if (_b + _vv) not in _cands:
                                _cands.append(_b + _vv)
                    # sew-iT / thematic-a/A (Bavi/BavI/vediza -> Bav/vediz)
                    for _sfx in ("i", "I", "a", "A"):
                        if _b.endswith(_sfx) and len(_b) > 1:
                            _cands.append(_b[:-1])
                    for _c in _cands:
                        _h = _lookup_root(_c)
                        if _h is not None and _h[0] not in [x[0] for x in _hits]:
                            _hits.append(_h)
                    # secondary stems in the aorist (san/nich reduplicated
                    # stems: buBUzizwa <- BU + sannanta): try reversals
                    for _c in _cands:
                        for _ab in _abhyasa_reverse(_c):
                            _h = _lookup_root(_ab)
                            if _h is not None and _h[0] not in [x[0] for x in _hits]:
                                _hits.append((_h[0], _h[1], "abhyasa"))
                        for _sn in _san_reverse(_c):
                            _h = _lookup_root(_sn)
                            if _h is not None and _h[0] not in [x[0] for x in _hits]:
                                _hits.append((_h[0], _h[1], "san"))
                    # queue stripped forms for deeper peeling (sic-s/z,
                    # iT, thematic, reduplicated -v-, aorist -t-)
                    for _sfx in ("s", "z", "i", "I", "a", "A", "v", "t", "T"):
                        if _b.endswith(_sfx) and len(_b) > 2 and \
                                _b[:-1] not in _seen_bases:
                            _frontier.append(_b[:-1])
                if not _hits:
                    continue
                for (_rt, _m, _via) in _hits:
                    for (_pur, _vac, _pada) in _slots:
                        _d = {"kind": "tinanta", "purusha": _pur, "vacana": _vac,
                              "pada": _pada, "prayoga": "kartari", "lakara": "luN",
                              "confidence": 0.75, "ending": _suf,
                              "note": f"root via {_via} from stem '{_stem}'"}
                        _d.update(_root_details(_m))
                        _d["pada"] = _pada
                        if upasarga:
                            _d["upasarga"] = upasarga
                            _d["confidence"] = max(0.1, _d["confidence"] - 0.1)
                        out.append(_d)
                break
    # liT perfect: strip personal ending, undo reduplication + grades
    _LIT = [("atuH", "prathama", "dvi"), ("uH", "prathama", "bahu"),
            ("aTuH", "madhyama", "dvi"), ("a", "prathama", "eka"),
            ("iTa", "madhyama", "eka"), ("Ta", "madhyama", "eka"),
            ("aTa", "madhyama", "bahu"), ("a", "uttama", "eka"),
            ("iva", "uttama", "dvi"), ("ima", "uttama", "bahu"),
            ("O", "prathama", "eka"), ("O", "uttama", "eka")]
    for _suf, _pur, _vac in _LIT:
        if word.endswith(_suf) and len(word) > len(_suf) + 1:
            _core = word[:-len(_suf)] if _suf != "a" else word[:-1]
            _hit = _lookup_root(_core)
            _viax = ""
            if _hit is None:
                # samprasarana perfects (uvAca <- vac, iyAja <- yaj):
                # drop reduplicant, restore semivowel, shorten A
                _sp = None
                if _core.startswith("uv") and len(_core) > 3:
                    _sp = "v" + _deyan(_core[2:])
                elif _core.startswith("iy") and len(_core) > 3:
                    _sp = "y" + _deyan(_core[2:])
                elif _core.startswith("U") and len(_core) > 1:
                    _sp = "va" + _core[1:]  # UcuH <- va + uc
                elif _core.startswith("I") and len(_core) > 1:
                    _sp = "ya" + _core[1:]  # Ij <- ya + ij
                if _sp is not None:
                    for _cand in (_sp, _devrddhi(_sp)):
                        _hit = _lookup_root(_cand)
                        if _hit is not None:
                            _viax = "samprasarana"
                            break
            if _hit is None:
                for _ab in _abhyasa_reverse(_core):
                    _hit = _lookup_root(_ab)
                    if _hit is not None:
                        _viax = "abhyasa"
                        break
            if _hit is None and _core.endswith("v"):
                # -va- augment stems (baBUva): strip v, retry abhyasa
                for _ab in _abhyasa_reverse(_core[:-1]):
                    _hit = _lookup_root(_ab)
                    if _hit is not None:
                        _viax = "abhyasa"
                        break
            if _hit is None:
                # secondary perfect stems (san/nich reduplication)
                for _sn in _san_reverse(_core):
                    _hit = _lookup_root(_sn)
                    if _hit is not None:
                        _viax = "san"
                        break
            if _hit is not None:
                _rt, _m, _via = _hit
                _emit(_rt, _m, "liw", _pur, _vac,
                      _viax or _via, 0.7, _core,
                      _sanadi="sannanta" if _viax == "san" else None)
                break
    # periphrastic perfect (stem + Am + auxiliary perfect: buBUzAYcakAra
    # <- BU + sannanta, ditsAYcakre <- dA): split the auxiliary, analyse
    # the stem side for the lexical root (aux table built from the engine)
    _ensure_peri_aux()
    for _aux, _apur, _avac, _apada in _PERI_AUX:
        if word.endswith(_aux) and len(word) > len(_aux) + 3:
            _pre = word[:-len(_aux)]
            # periphrastic connector Am/AY (buBUzAmAsa, buBUzAYcakAra)
            if not (_pre.endswith("Am") or _pre.endswith("AY")) or len(_pre) < 5:
                continue
            _stem = _pre[:-2]
            _lex = [_stem]
            if _stem.endswith(("i", "I", "a", "A")) and len(_stem) > 1:
                _lex.append(_stem[:-1])  # sew-iT / thematic
            _phit = None
            _pvia = ""
            _ptwin = None
            for _c in _lex:
                _phit = _lookup_root(_c)
                if _phit is not None:
                    # exact hits can shadow twins (buBUz -> BUz hides BU):
                    # collect the other reversals as a twin reading
                    for _ab in _abhyasa_reverse(_c):
                        _ah = _lookup_root(_ab)
                        if _ah is not None and _ah[0] != _phit[0]:
                            _ptwin = (_ah[0], _ah[1], "abhyasa")
                            break
                    if _ptwin is None:
                        for _sn in _san_reverse(_c):
                            _sh = _lookup_root(_sn)
                            if _sh is not None and _sh[0] != _phit[0]:
                                _ptwin = (_sh[0], _sh[1], "san")
                                break
                    break
                for _ab in _abhyasa_reverse(_c):
                    _phit = _lookup_root(_ab)
                    if _phit is not None:
                        _pvia = "abhyasa"
                        break
                if _phit is not None:
                    for _sn in _san_reverse(_c):
                        _sh = _lookup_root(_sn)
                        if _sh is not None and _sh[0] != _phit[0]:
                            _ptwin = (_sh[0], _sh[1], "san")
                            break
                    break
                for _sn in _san_reverse(_c):
                    _phit = _lookup_root(_sn)
                    if _phit is not None:
                        _pvia = "san"
                        break
                if _phit is not None:
                    for _ab in _abhyasa_reverse(_c):
                        _ah = _lookup_root(_ab)
                        if _ah is not None and _ah[0] != _phit[0]:
                            _ptwin = (_ah[0], _ah[1], "abhyasa")
                            break
                    break
            _readings = []
            if _phit is not None:
                _rt, _m, _via = _phit
                _readings.append((_rt, _m, _pvia or _via))
            if _ptwin is not None:
                _readings.append(_ptwin)
            for (_rt, _m, _via) in _readings:
                _d = {"kind": "tinanta", "purusha": _apur, "vacana": _avac,
                      "pada": _apada, "prayoga": "kartari", "lakara": "liw",
                      "confidence": 0.7, "ending": _aux,
                      "note": f"periphrastic liw: root via {_via} "
                      f"from stem '{_stem}' + aux '{_aux}'"}
                _d.update(_root_details(_m))
                if upasarga:
                    _d["upasarga"] = upasarga
                    _d["confidence"] = max(0.1, _d["confidence"] - 0.1)
                out.append(_d)
            if _phit is not None:
                break
    return out


_PERI_AUX: list = []


def _ensure_peri_aux() -> None:
    """Build (auxform, purusha, vacana, pada) table from engine perfects."""
    global _PERI_AUX
    if _PERI_AUX:
        return
    from .tinanta import TinantaDerivationEngine
    _te = TinantaDerivationEngine()
    _seen = set()
    for _aux_rt in ("kf", "as", "BU"):
        for _prayoga, _pada in (("kartari", "parasmaipada"),
                                ("karmani", "Atmanepada")):
            for _pur in ("prathama", "madhyama", "uttama"):
                for _vac in ("eka", "dvi", "bahu"):
                    try:
                        _forms, _log = _te.derive(_aux_rt, "liw", _pur, _vac,
                                                 prayoga=_prayoga)
                    except Exception:
                        continue
                    for _f in _forms:
                        if _f not in _seen:
                            _seen.add(_f)
                            _PERI_AUX.append((_f, _pur, _vac, _pada))
    _PERI_AUX.sort(key=lambda t: -len(t[0]))


_TIN_ENG = None


def _verify_tin(word: str, dhatu: str, lak: str, pur: str, vac: str,
                prayoga: str, sanadi, dhatu_id, upasarga) -> bool:
    """Forward-verify a tinanta reading with the generative engine."""
    global _TIN_ENG
    try:
        if _TIN_ENG is None:
            from .tinanta import TinantaDerivationEngine
            _TIN_ENG = TinantaDerivationEngine()

        def _gen(_w: str) -> bool:
            _cands, _log = _TIN_ENG.derive(
                dhatu, lak, pur, vac,
                prayoga=prayoga or "kartari", sanadi=sanadi, dhatu_id=dhatu_id,
                upasarga=upasarga)
            return _w in _cands

        if _gen(word):
            return True
        # t/d voicing twins (BavatAd <- BavatAt): the engine emits -t, so
        # confirm a -d surface against its -t twin (same formation)
        if word.endswith("d"):
            return _gen(word[:-1] + "t")
        return False
    except Exception:
        return True  # engine gap: never punish on errors


def _tinanta_analyze(word: str, upasarga: str | None = None) -> List[dict]:
    out: List[dict] = []
    out += _infix_reverse(word, upasarga)
    for _table, _pada in ((_TIN_P, "parasmaipada"), (_TIN_A, "Atmanepada")):
        for (_end, _lak, _pur, _vac) in _table:
            if not word.endswith(_end) or len(word) <= len(_end):
                continue
            _core = word[:-len(_end)] if _end else word
            _aug = (_lak == "laN")
            _hit = None
            _via_extra = ""
            _multi = None
            _extra_hits: List[tuple] = []
            for _cand in _tin_candidates(_core, _lak, _aug):
                # irregular presents first (multi-root: yacCa <- yam + dA)
                _irr = _irreg_pres(_cand)
                if _irr is not None:
                    _multi = _irr
                    break
                _hit = _lookup_root(_cand)
                if _hit is not None:
                    # also keep abhyasa twin (dadati is dad + dA at once)
                    for _ab in _abhyasa_reverse(_cand):
                        _ah = _lookup_root(_ab)
                        if _ah is not None and _ah[0] != _hit[0]:
                            if _ah[0] not in [h[0] for h in _extra_hits]:
                                _extra_hits.append((_ah[0], _ah[1], "abhyasa"))
                    # also keep desiderative twin (buBUzati is BUz + BU:
                    # exact lookup finds only the san-shaped root BUz)
                    for _sn in _san_reverse(_cand):
                        _sh = _lookup_root(_sn)
                        if _sh is not None and _sh[0] != _hit[0]:
                            if _sh[0] not in [h[0] for h in _extra_hits]:
                                _extra_hits.append((_sh[0], _sh[1], "san"))
                    break
                # class-3 reduplicated stems (dadA/juhu/biBar + ti)
                for _ab in _abhyasa_reverse(_cand):
                    _hit = _lookup_root(_ab)
                    if _hit is not None:
                        _via_extra = "abhyasa"
                        break
                if _hit is not None:
                    # primary came via abhyasa (buBUz -> BUz): san twins
                    # (buBUz -> BU) still count as extra readings
                    for _sn in _san_reverse(_cand):
                        _sh = _lookup_root(_sn)
                        if _sh is not None and _sh[0] != _hit[0]:
                            if _sh[0] not in [h[0] for h in _extra_hits]:
                                _extra_hits.append((_sh[0], _sh[1], "san"))
                    break
                # desiderative stems (ditsa/vividiza + ti)
                for _sn in _san_reverse(_cand):
                    _hit = _lookup_root(_sn)
                    if _hit is not None:
                        _via_extra = "san"
                        break
                if _hit is not None:
                    # primary came via san: abhyasa twins still count
                    for _ab in _abhyasa_reverse(_cand):
                        _ah = _lookup_root(_ab)
                        if _ah is not None and _ah[0] != _hit[0]:
                            if _ah[0] not in [h[0] for h in _extra_hits]:
                                _extra_hits.append((_ah[0], _ah[1], "abhyasa"))
                    break
                # viDiliN e-grade of A-final roots (det <- dA: the ending
                # table segments d+et, swallowing the stem vowel, while
                # exact lookup finds only the e-final root deN)
                if _hit is None and _lak == "viDiliN" and _cand.endswith("e"):
                    _hit = _lookup_root(_cand[:-1] + "A")
                    if _hit is not None:
                        _via_extra = "egrade"
                        break
                if (_hit is None and _lak == "viDiliN" and len(_cand) == 1
                        and _cand not in SLP1_VOWELS):
                    _hit = _lookup_root(_cand + "A")
                    if _hit is not None:
                        _via_extra = "egrade"
                        break
            # classical laN needs the a- augment (adadat, not *dadan)
            _no_aug = _aug and _core[:1] not in ("a", "A")
            # liT always reduplicates (Asa-type a-initial stems excepted):
            # plain grade-hits on bare-a endings (rAma) are nouns, not verbs.
            # (Unresolved fallbacks still emit below.)
            _liw_plain = (_lak == "liw" and not _via_extra and _multi is None
                          and _core[:1] not in ("a", "A"))
            if _multi is not None:
                for (_m, _c) in _multi:
                    _d = {"kind": "tinanta", "purusha": _pur, "vacana": _vac,
                          "pada": _pada, "prayoga": "kartari", "lakara": _lak,
                          "confidence": 0.95, "ending": _end}
                    _d.update(_root_details(_m))
                    _d["pada"] = _pada
                    _d["note"] = f"irregular present stem '{_core}'"
                    if _no_aug:
                        _d["confidence"] *= 0.6
                        _d["note"] += "; augment a- missing"
                    if upasarga:
                        _d["upasarga"] = upasarga
                    _ids = _d.get("ids") or [None]
                    if not _verify_tin(word, _c, _lak, _pur, _vac, "kartari",
                                       None, _ids[0], upasarga):
                        _d["confidence"] = max(0.1, _d["confidence"] * 0.5)
                        _d["note"] += "; unverified"
                    out.append(_d)
            if _hit is not None and not _liw_plain:
                _rt, _m, _via = _hit
                # thematic grade-reversal is the regular BvAdi formation,
                # so guna is near-deterministic (outranks coincidental nouns)
                _conf = _via_conf(_via)
                if _via_extra == "abhyasa":
                    _via = "abhyasa"
                    _conf = 0.7
                elif _via_extra == "san":
                    _via = "san"
                    _conf = 0.65
                elif _via_extra == "egrade":
                    _via = "egrade"
                    _conf = 0.65
                if _no_aug:
                    _conf *= 0.6
                _d = {"kind": "tinanta", "purusha": _pur, "vacana": _vac,
                      "pada": _pada, "prayoga": "kartari", "lakara": _lak,
                      "confidence": _conf, "ending": _end}
                _d.update(_root_details(_m))
                _d["pada"] = _pada
                if _via != "exact":
                    _d["note"] = f"root via {_via} from stem '{_core}'"
                if _no_aug:
                    _d["note"] = (_d.get("note", "") + "; augment a- missing").strip("; ")
                if upasarga:
                    _d["upasarga"] = upasarga
                # analysis by synthesis: keep full score only if the engine
                # regenerates the word (kills e.g. augmentless-laN ghosts);
                # Atmanepada forms fall back to karmani before demotion
                _ids = _d.get("ids") or [None]
                _ok = _verify_tin(word, _rt, _lak, _pur, _vac, "kartari",
                                  "sannanta" if _via == "san" else None,
                                  _ids[0], upasarga)
                if not _ok and _pada == "Atmanepada":
                    _ok = _verify_tin(word, _rt, _lak, _pur, _vac, "karmani",
                                      "sannanta" if _via == "san" else None,
                                      _ids[0], upasarga)
                    if _ok:
                        _d["prayoga"] = "karmani"
                        _d["note"] = (_d.get("note", "") + "; karmani").strip("; ")
                if not _ok:
                    _d["confidence"] = max(0.1, _d["confidence"] * 0.5)
                    _d["note"] = (_d.get("note", "") + "; unverified").strip("; ")
                out.append(_d)
                for (_ert, _em, _evia) in _extra_hits:
                    _ed = {"kind": "tinanta", "purusha": _pur,
                           "vacana": _vac, "pada": _pada,
                           "prayoga": "kartari", "lakara": _lak,
                           "confidence": 0.7, "ending": _end}
                    _ed.update(_root_details(_em))
                    _ed["pada"] = _pada
                    _ed["note"] = f"root via {_evia} from stem '{_core}'"
                    if _no_aug:
                        _ed["confidence"] *= 0.6
                        _ed["note"] += "; augment a- missing"
                    if upasarga:
                        _ed["upasarga"] = upasarga
                    _eids = _ed.get("ids") or [None]
                    _eok = _verify_tin(word, _ert, _lak, _pur, _vac,
                                       "kartari",
                                       "sannanta" if _evia == "san" else None,
                                       _eids[0], upasarga)
                    if not _eok:
                        _ed["confidence"] = max(0.1, _ed["confidence"] * 0.5)
                        _ed["note"] += "; unverified"
                    out.append(_ed)
            if _hit is not None and _liw_plain and _extra_hits:
                # liw plain-grade hits are noun-coincidences (rAma), but
                # reduplication-derived twins (dad -> dA) are genuine verbs
                for (_ert, _em, _evia) in _extra_hits:
                    _ed = {"kind": "tinanta", "purusha": _pur,
                           "vacana": _vac, "pada": _pada,
                           "prayoga": "kartari", "lakara": _lak,
                           "confidence": 0.7, "ending": _end}
                    _ed.update(_root_details(_em))
                    _ed["pada"] = _pada
                    _ed["note"] = f"root via {_evia} from stem '{_core}'"
                    if _no_aug:
                        _ed["confidence"] *= 0.6
                        _ed["note"] += "; augment a- missing"
                    if upasarga:
                        _ed["upasarga"] = upasarga
                    _eids = _ed.get("ids") or [None]
                    _eok = _verify_tin(word, _ert, _lak, _pur, _vac,
                                       "kartari",
                                       "sannanta" if _evia == "san" else None,
                                       _eids[0], upasarga)
                    if not _eok:
                        _ed["confidence"] = max(0.1, _ed["confidence"] * 0.5)
                        _ed["note"] += "; unverified"
                    out.append(_ed)
            if _hit is None or _liw_plain:
                _d = {"kind": "tinanta", "dhatu": None, "purusha": _pur,
                      "vacana": _vac, "pada": _pada, "prayoga": "kartari",
                      "lakara": _lak, "confidence": 0.4,
                      "ending": _end,
                      "note": f"stem '{_core}' matched no known root"}
                if upasarga:
                    _d["upasarga"] = upasarga
                out.append(_d)
    return out


def _end_slots() -> List[tuple]:
    """All tin endings longest-first with their table slots (lakara ignored)."""
    _m: Dict[str, list] = {}
    for _table, _pada in ((_TIN_P, "parasmaipada"), (_TIN_A, "Atmanepada")):
        for (_end, _lak, _pur, _vac) in _table:
            _m.setdefault(_end, []).append((_pur, _vac, _pada))
    return sorted(_m.items(), key=lambda kv: -len(kv[0]))


_END_SLOTS: List[tuple] = []
_END_SLOTS_DICT: Dict[str, list] = {}


def _ensure_end_slots() -> None:
    global _END_SLOTS, _END_SLOTS_DICT
    if not _END_SLOTS:
        _END_SLOTS = _end_slots()
        _END_SLOTS_DICT = dict(_END_SLOTS)


_UPASARGAS = ["parA", "antar", "nir", "nis", "dus", "dur", "anu", "ava",
              "apa", "api", "aDi", "ati", "aBi", "ud", "upa", "pari",
              "prati", "pra", "sam", "vi", "ni", "su", "A"]

# retroflex -> dental (reverse zwunA zwuH: surface W hides underlying T)
_RETRO_DENTAL = {"w": "t", "W": "T", "q": "d", "Q": "D", "R": "n"}


def _rev_prefix_sandhi(rest: str) -> List[str]:
    """Undo upasarga sandhi on a split remainder (8.3.59 zatva, 8.2.41 zwutva).
    prati + sTira -> pratizWira, so 'zWira' retries as 'sWira' and 'sTira'."""
    _vars = [rest]
    if rest[:1] in ("z", "S"):
        _vars.append("s" + rest[1:])
        if len(rest) > 1 and rest[1] in _RETRO_DENTAL:
            _vars.append("s" + _RETRO_DENTAL[rest[1]] + rest[2:])
    return _vars


# ---------------------------------------------------------------------------
# public API
# ---------------------------------------------------------------------------

def subanta_search(word: str, limit: int = 20) -> List[dict]:
    """Subanta-only search: stem + vibhakti + vacana + linga readings."""
    _ensure_ready()
    word = (word or "").strip()
    if not word:
        return []
    out: List[dict] = []
    seen = set()
    for _a in _LEXICON.get(word, []):
        out.append(dict(_a))
        seen.add((_a["stem"], _a["linga"], _a["vibhakti"], _a["vacana"]))
    for _a in _subanta_open(word):
        _k = (_a["stem"], _a["linga"], _a["vibhakti"], _a["vacana"])
        if _k in seen:
            continue
        seen.add(_k)
        out.append(_a)
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out[:limit]


def krdanta_search(word: str, limit: int = 20, with_upasarga: bool = True) -> List[dict]:
    """Krdanta-only search: dhatu + pratyaya (+ inflection) readings."""
    _ensure_ready()
    word = (word or "").strip()
    if not word:
        return []
    out: List[dict] = []
    seen = set()

    def _from_stems(stem_list: List[tuple], penalty: float = 0.0,
                    upasarga: str | None = None) -> None:
        for (_lex, _st, _li, _vib, _vac) in stem_list:
            for _k in _krdanta_from_stem(_st, _li, _vib, _vac):
                _kk = (_k.get("dhatu"), _k["pratyaya"], _st, _li, _vib, _vac,
                       upasarga)
                if _kk in seen:
                    continue
                seen.add(_kk)
                _k = dict(_k)
                if penalty:
                    _k["confidence"] = max(0.1, _k["confidence"] - penalty)
                if upasarga:
                    _k["upasarga"] = upasarga
                out.append(_k)

    _stems = []
    for _a in subanta_search(word, limit=50):
        _stems.append((_a.get("lexicon", False),
                       _a["stem"], _a["linga"], _a["vibhakti"], _a["vacana"]))
    # feminine krdanta forms ride masculine stems (BavitavyA <- Bavitavya)
    _more = []
    for (_lex, _st, _li, _vib, _vac) in _stems:
        if _st.endswith("A") and len(_st) > 2:
            _more.append((False, _st[:-1] + "a", _li, _vib, _vac))
        if _st.endswith("ntI") and len(_st) > 3:
            _more.append((False, _st[:-3] + "at", _li, _vib, _vac))
        if _st.endswith("vatI") and len(_st) > 4:
            _more.append((False, _st[:-1], _li, _vib, _vac))
    _stems += _more
    _stems.sort(key=lambda t: (not t[0], t[1]))
    _from_stems(_stems)
    # feminine krdanta forms ride masculine stems (BavitavyA <- Bavitavya,
    # BavantI <- Bavat, BUtavatI <- BUtavat, cakruzI <- cakfuz weak):
    # recover the masculine word, analyse it, keep the feminine slot
    _mw = None
    if word.endswith("A") and len(word) > 2:
        _mw = word[:-1] + "a"
    elif word.endswith("ntI") and len(word) > 3:
        _mw = word[:-3] + "at"
    elif word.endswith("vatI") and len(word) > 4:
        _mw = word[:-1]
    elif word.endswith("trI") and len(word) > 3:
        _mw = word[:-3] + "tf"
    elif word.endswith("zI") and len(word) > 2:
        _mw = word[:-1]
    if _mw:
        for _k in _krdanta_from_stem(_mw, "strI", 1, "eka"):
            _kk = (_k.get("dhatu"), _k["pratyaya"], _mw, "strI", 1, "eka")
            if _kk in seen:
                continue
            seen.add(_kk)
            out.append(_k)
    # indeclinable krdantas have no sup stem: tumun (-tum), ktvA (-tvA),
    # Ramul (-am, low confidence: -am is usually the accusative ending)
    for _suf, _prat, _conf in (("tum", "tumun", 0.85), ("tvA", "ktvA", 0.85),
                               ("am", "Ramul", 0.5)):
        if word.endswith(_suf) and len(word) > len(_suf) + 1:
            _core = word[:-len(_suf)]
            _cands = [_core]
            if _core.endswith("i") and len(_core) > 1:
                _cands.append(_core[:-1])  # sew iT (Bavi -> Bav)
            if _prat == "ktvA" and _core[:1] in ("u", "i") and len(_core) > 1:
                # samprasarana absolutives (uktvA <- vac): va/ya + cutva
                _rest = _core[1:]
                _cut = _decutva(_rest)
                _cands.append(("va" if _core[:1] == "u" else "ya") + _cut)
            for _c in _cands:
                _hit = _lookup_root(_c)
                if _hit is not None:
                    break
            if _hit is not None:
                _rt, _m, _via = _hit
                out.append({"kind": "krdanta", "pratyaya": _prat,
                            "stem": word, "linga": "avyaya", "vibhakti": None,
                            "vacana": None, "confidence": _conf,
                            "note": f"root via {_via} from '{_core}'",
                            **_root_details(_m)})
                break
    # prefixless -ya absolutive (BUya <- BU): lyap needs an upasarga, so this
    # reading is weak — but the engine overgenerates unprefixed twins
    if word.endswith("ya") and len(word) > 3:
        _hit = _lookup_root(_devrddhi(word[:-2]))
        if _hit is not None:
            _rt, _m, _via = _hit
            _kk = (_rt, "lyap", word, None)
            if _kk not in seen:
                seen.add(_kk)
                out.append({"kind": "krdanta", "pratyaya": "lyap",
                            "stem": word, "linga": "avyaya",
                            "vibhakti": None, "vacana": None,
                            "confidence": 0.45,
                            "note": f"root via {_via}; prefix missing",
                            **_root_details(_m)})
    if with_upasarga:
        # prati + sTira -> pratizWira: prefix sandhi voices s->z/S and
        # retroflexes the following stop, so retry reversed variants
        for _p in sorted(_UPASARGAS, key=lambda s: (len(s), s), reverse=True):
            if word.startswith(_p) and len(word) - len(_p) >= 3:
                _rest = word[len(_p):]
                _variants = _rev_prefix_sandhi(_rest)
                _rstems = []
                for _v in _variants:
                    for _a in subanta_search(_v, limit=50):
                        _rstems.append((_a.get("lexicon", False), _a["stem"],
                                        _a["linga"], _a["vibhakti"], _a["vacana"]))
                _rstems.sort(key=lambda t: (not t[0], t[1]))
                _from_stems(_rstems, penalty=0.1, upasarga=_p)
                # lyap absolutive needs a prefix: remainder-ya + upasarga
                for (_lex, _st, _li, _vib, _vac) in _rstems:
                    if _st.endswith("ya") and len(_st) > 3:
                        _hit = _lookup_root(_devrddhi(_st[:-2]))
                        if _hit is not None:
                            _rt, _m, _via = _hit
                            _kk = (_rt, "lyap", _st, _p)
                            if _kk in seen:
                                continue
                            seen.add(_kk)
                            out.append({"kind": "krdanta", "pratyaya": "lyap",
                                        "stem": _st, "linga": "avyaya",
                                        "vibhakti": None, "vacana": None,
                                        "confidence": 0.75,
                                        "upasarga": _p,
                                        "note": f"root via {_via}",
                                        **_root_details(_m)})
                            break
                break
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out[:limit]


def tinanta_search(word: str, limit: int = 20, with_upasarga: bool = True) -> List[dict]:
    """Tinanta-only search: dhatu + lakara + purusha + vacana + pada readings."""
    _ensure_ready()
    word = (word or "").strip()
    if not word:
        return []
    out: List[dict] = []
    seen = set()

    def _add(_t: dict, _penalty: float = 0.0) -> None:
        _k = (_t.get("dhatu"), _t.get("lakara"), _t.get("purusha"),
              _t.get("vacana"), _t.get("pada"), _t.get("ending"),
              _t.get("upasarga"))
        if _k in seen:
            return
        seen.add(_k)
        _t = dict(_t)
        if _penalty:
            _t["confidence"] = max(0.1, _t["confidence"] - _penalty)
        out.append(_t)

    for _t in _tinanta_analyze(word):
        _add(_t)
    if with_upasarga:
        for _p in sorted(_UPASARGAS, key=lambda s: (len(s), s), reverse=True):
            if word.startswith(_p) and len(word) - len(_p) >= 3:
                for _v in _rev_prefix_sandhi(word[len(_p):]):
                    for _t in _tinanta_analyze(_v, upasarga=_p):
                        _add(_t, _penalty=0.1)
                break
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out[:limit]


def analyze(word: str, limit: int = 20) -> List[dict]:
    """Global search across subanta/krdanta/tinanta (highest confidence first).

    Subanta readings always forward-verify; krdanta/tinanta readings
    resolve the dhatu heuristically (``dhatu=None`` when unresolved).
    """
    _ensure_ready()
    word = (word or "").strip()
    if not word:
        return []
    out: List[dict] = []
    seen = set()
    for _a in subanta_search(word, limit=50):
        _k = ("s", _a["stem"], _a["linga"], _a["vibhakti"], _a["vacana"])
        if _k in seen:
            continue
        seen.add(_k)
        out.append(_a)
    for _k in krdanta_search(word, limit=50):
        _kk = ("k", _k.get("dhatu"), _k["pratyaya"], _k["stem"],
               _k["linga"], _k["vibhakti"], _k["vacana"])
        if _kk in seen:
            continue
        seen.add(_kk)
        out.append(_k)
    for _t in tinanta_search(word, limit=50):
        _kk = ("t", _t.get("dhatu"), _t.get("lakara"), _t.get("purusha"),
               _t.get("vacana"), _t.get("pada"), _t.get("ending"),
               _t.get("upasarga"))
        if _kk in seen:
            continue
        seen.add(_kk)
        out.append(_t)
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out[:limit]


def best(word: str) -> dict | None:
    """Top-ranked analysis, or None."""
    _r = analyze(word, limit=1)
    return _r[0] if _r else None
