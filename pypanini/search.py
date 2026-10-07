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

from typing import Dict, List, Tuple

from .subanta import SubantaEngine, SLP1_VOWELS

# ---------------------------------------------------------------------------
# shared root data (from the krdanta dhātu cache - read-only cross-check)
# ---------------------------------------------------------------------------

_ROOTS: Dict[str, dict] = {}
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


def _len_variants(s: str) -> List[str]:
    out = [s]
    if s and s[-1] in "iIuUfFxXaA":
        swap = {"i": "I", "I": "i", "u": "U", "U": "u", "f": "F", "F": "f",
                "x": "X", "X": "x", "a": "A", "A": "a"}
        out.append(s[:-1] + swap[s[-1]])
    return out


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
_ABHYASA_GRADE = {"a": "A", "i": "I", "u": "U"}


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


def _lookup_root(cand: str):
    """Exact + graded root lookup. Returns (clean, meta, via) or None."""
    for _c in _len_variants(cand):
        if _c in _ROOTS:
            return _c, _ROOTS[_c], "exact"
    # Natva reversal (praRamati -> nam): R could hide dental n
    if "R" in cand:
        _hit = _lookup_root(cand.replace("R", "n"))
        if _hit is not None:
            return _hit[0], _hit[1], "natva+" + _hit[2]
    for _c in _len_variants(cand):
        if _c in _ROOTS:
            return _c, _ROOTS[_c], "exact"
    _g = _deglide(cand)
    for _c in _len_variants(_g):
        if _c in _ROOTS:
            return _c, _ROOTS[_c], "glide"
    _g = _deguna(_g)
    for _c in _len_variants(_g):
        if _c in _ROOTS:
            return _c, _ROOTS[_c], "guna"
    _g = _devrddhi(cand)
    for _c in _len_variants(_g):
        if _c in _ROOTS:
            return _c, _ROOTS[_c], "vrddhi"
    return None


def _root_details(meta: dict) -> dict:
    return {"dhatu": meta.get("clean"), "dhAtu_pada": meta.get("pada"),
            "sew": meta.get("sew"), "gana": meta.get("gana")}


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
    for _f, _li in [("i", None), ("u", None)]:
        pass
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
    # bare at-final nominatives: abhyasta (dadat, 7.1.78, no num) + neuter
    _add("", "", {"t"}, None, "puM", 1, "eka", {"abhyasta": True})
    _add("", "", {"t"}, None, "napuMsaka", 1, "eka")


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
    # tavya / anIyar / yat via graded lookup
    if stem.endswith("tavya"):
        _hit = _lookup_root(stem[:-5]) or (
            _lookup_root(stem[:-6] + stem[-5]) if stem.endswith("itavya") else None)
        # sew iT: ...itavya -> strip the i, retry graded
        if _hit is None and stem.endswith("itavya"):
            _hit = _lookup_root(_deguna(_deglide(stem[:-6])))
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("tavya", _rt, _m, 0.85, f"root via {_via}")
        else:
            _emit("tavya", None, None, 0.5, "root unresolved")
    if stem.endswith("anIya"):
        _hit = _lookup_root(_deguna(_deglide(stem[:-5])))
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("anIyar", _rt, _m, 0.85, f"root via {_via}")
        else:
            _emit("anIyar", None, None, 0.5, "root unresolved")
    if stem.endswith("ya") and len(stem) > 3:
        _hit = _lookup_root(_devrddhi(stem[:-2]))
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("yat", _rt, _m, 0.85, f"root via {_via}")
    # SAnac
    if stem.endswith("mAna"):
        _b = stem[:-4]
        _hit = _lookup_root(_b[:-1] if _b.endswith("a") else _b)
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("SAnac", _rt, _m, 0.8, f"root via {_via}")
        else:
            _emit("SAnac", None, None, 0.5, "present stem; root unresolved")
    elif stem.endswith("Ana"):
        _b = stem[:-3]
        _hit = _lookup_root(_b[:-1] if _b.endswith("a") else _b)
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("SAnac", _rt, _m, 0.8, f"root via {_via}")
        else:
            _emit("SAnac", None, None, 0.5, "present stem; root unresolved")
    # Rvul / tfc
    if stem.endswith("aka") or stem.endswith("ikA"):
        _b = stem[:-3]
        _hit = _lookup_root(_devrddhi(_b))
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("Rvul", _rt, _m, 0.85, f"root via {_via}")
    if stem.endswith("tf") or stem.endswith("trI"):
        _b = stem[:-2] if stem.endswith("tf") else stem[:-3]
        _hit = _lookup_root(_deguna(_b))
        if _hit is not None:
            _rt, _m, _via = _hit
            _emit("tfc", _rt, _m, 0.85, f"root via {_via}")
    # Satf present stem (abhyasa-reversible class-3 links; rest unresolved).
    # Guard excludes ktavatu (-tavat); juhvat-type (-hvat) stays eligible.
    if stem.endswith("ant") or (stem.endswith("at") and not stem.endswith("tavat")):
        _core = stem[:-3] if stem.endswith("ant") else stem[:-2]
        for _cand in _abhyasa_reverse(_core):
            _hit = _lookup_root(_cand)
            if _hit is not None:
                _rt, _m, _via = _hit
                _emit("Satf", _rt, _m, 0.7, "root via abhyasa")
                break
        else:
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
    ("Ava", "low", "uttama", "dvi"), ("Ama", "low", "uttama", "bahu"),
    ("eyuH", "viDiliN", "prathama", "bahu"), ("etAm", "viDiliN", "prathama", "dvi"),
    ("et", "viDiliN", "prathama", "eka"), ("eH", "viDiliN", "madhyama", "eka"),
    ("etam", "viDiliN", "madhyama", "dvi"), ("eta", "viDiliN", "madhyama", "bahu"),
    ("eyam", "viDiliN", "uttama", "eka"), ("eva", "viDiliN", "uttama", "dvi"),
    ("ema", "viDiliN", "uttama", "bahu"),
]
_TIN_A: List[tuple] = [
    ("ante", "lw", "prathama", "bahu"), ("ete", "lw", "prathama", "dvi"),
    ("te", "lw", "prathama", "eka"), ("se", "lw", "madhyama", "eka"),
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
]


def _tin_candidates(core: str, lakara: str, aug: bool) -> List[str]:
    cands = [core]
    if core.endswith("a") and len(core) > 1:
        cands.append(core[:-1])  # thematic -a-
    if aug:
        _stripped = []
        for _c in cands:
            if _c.startswith("a") and len(_c) > 1:
                _stripped.append(_c[1:])  # laN augment a-
            elif _c.startswith("A") and len(_c) > 1:
                _stripped.append(_c[1:])
        cands += _stripped
    return cands


def _tinanta_analyze(word: str, upasarga: str | None = None) -> List[dict]:
    out: List[dict] = []
    for _table, _pada in ((_TIN_P, "parasmaipada"), (_TIN_A, "Atmanepada")):
        for (_end, _lak, _pur, _vac) in _table:
            if not word.endswith(_end) or len(word) <= len(_end):
                continue
            _core = word[:-len(_end)]
            _aug = (_lak == "laN")
            _hit = None
            _via_extra = ""
            for _cand in _tin_candidates(_core, _lak, _aug):
                _hit = _lookup_root(_cand)
                if _hit is not None:
                    break
                # class-3 reduplicated stems (dadA/juhu/biBar + ti)
                for _ab in _abhyasa_reverse(_cand):
                    _hit = _lookup_root(_ab)
                    if _hit is not None:
                        _via_extra = "abhyasa"
                        break
                if _hit is not None:
                    break
            # classical laN needs the a- augment (adadat, not *dadan)
            _no_aug = _aug and _core[:1] not in ("a", "A")
            if _hit is not None:
                _rt, _m, _via = _hit
                # thematic grade-reversal is the regular BvAdi formation,
                # so guna is near-deterministic (outranks coincidental nouns)
                _conf = {"exact": 1.0, "glide": 0.95, "guna": 0.92,
                         "vrddhi": 0.8}.get(_via, 0.6)
                if _via_extra == "abhyasa":
                    _via = "abhyasa"
                    _conf = 0.7
                if _no_aug:
                    _conf *= 0.6
                _d = {"kind": "tinanta", "purusha": _pur, "vacana": _vac,
                      "pada": _pada, "prayoga": "kartari", "lakara": _lak,
                      "confidence": _conf, "ending": _end}
                _d.update(_root_details(_m))
                if _via != "exact":
                    _d["note"] = f"root via {_via} from stem '{_core}'"
                if _no_aug:
                    _d["note"] = (_d.get("note", "") + "; augment a- missing").strip("; ")
                if upasarga:
                    _d["upasarga"] = upasarga
                out.append(_d)
            else:
                _d = {"kind": "tinanta", "dhatu": None, "purusha": _pur,
                      "vacana": _vac, "pada": _pada, "prayoga": "kartari",
                      "lakara": _lak, "confidence": 0.4,
                      "ending": _end,
                      "note": f"stem '{_core}' matched no known root"}
                if upasarga:
                    _d["upasarga"] = upasarga
                out.append(_d)
    return out


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
    _stems.sort(key=lambda t: (not t[0], t[1]))
    _from_stems(_stems)
    if with_upasarga:
        # prati + sTira -> pratizWira: prefix sandhi voices s->z/S and
        # retroflexes the following stop, so retry reversed variants
        for _p in sorted(_UPASARGAS, key=len, reverse=True):
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
        for _p in sorted(_UPASARGAS, key=len, reverse=True):
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
