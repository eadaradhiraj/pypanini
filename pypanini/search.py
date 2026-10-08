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
_KTA_MAP: Dict[str, List[str]] = {}
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
        if _kta:
            _KTA_MAP.setdefault(_kta, [])
            if _clean not in _KTA_MAP[_kta]:
                _KTA_MAP[_kta].append(_clean)
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


def _dekhari(s: str) -> str:
    """Reverse khari ca devoicing before t (yukta <- yuj + ta,
    Bhokzyati <- Buz + sya): final k/K -> j/J."""
    if s.endswith("k"):
        return s[:-1] + "j"
    if s.endswith("K"):
        return s[:-1] + "J"
    return s


def _deinfix(s: str) -> str:
    """Reverse class-7 nasal infix (runD <- rundh + ...: infix n/N/Y/M/R
    between vowel-or-fricative and following consonant drops; Danv <-
    Davi + tum needs n before v too)."""
    import re as _re
    _v = _re.sub(r"([aAiIuUfFxX])([nNYMR])(?=[aA]?[kKgGcCjJtTwWqQdDNpPbBsSzZvy])",
                 r"\1", s, count=1)
    return _v


def _denu(s: str) -> str:
    """Reverse class-5 -nu- vikaraNa (sun <- su + nu)."""
    if s.endswith(("nu", "no")) and len(s) > 2:
        return s[:-2]
    return s


def _dethem(s: str) -> str:
    """Reverse medial thematic -a- (yuaj <- yuYaj + ...: class-7 stem
    after infix-strip leaves root + thematic fused mid-string;
    Cfad <- Cfd + a, unad <- und + a)."""
    import re as _re
    return _re.sub(r"([iIuUfFxXnN])a(?=[kKgGcCjJtTwWqQdDNpPbBsSzZ])", r"\1",
                   s, count=1)


def _deriF(s: str) -> str:
    """Reverse ri-grade (pf <- priya + ...: ri hides vocalic F)."""
    if len(s) > 1 and s.endswith("ri"):
        return s[:-2] + "F"
    return s


def _deit(s: str) -> str:
    """Reverse lost iT/i-grade (pij <- piji + ...: pik <- pij + te needs
    +i; bfha <- bfhi + a needs +i after thematic strip; mida <- midi;
    ci <- cap + aya via ap-strip; dIDI <- dID + ya). Lookup-gated."""
    if len(s) >= 1 and s[-1] not in SLP1_VOWELS:
        return s + "i"
    return s


def _dea(s: str) -> str:
    """Reverse dropped root vowel (as <- s + ...: single-consonant
    remainder regains a-)."""
    if len(s) == 1 and s not in SLP1_VOWELS:
        return "a" + s
    return s


def _deGhn(s: str) -> str:
    """Reverse Ghn-cluster (han <- Gnan/Ghnanti + ...: Gh onset with
    following n reduces to han)."""
    import re as _re
    _v = _re.sub(r"^Gn$", "Ghn", s, count=1)
    if _v != s:
        return _v
    return _re.sub(r"^Ghn(an)?$", "han", s, count=1)


def _demeta9(s: str) -> str:
    """Reverse class-9 n-metathesis (stunB <- stuBn + A, skanB <- skaBn):
    stop + n flips back to n + stop."""
    import re as _re
    return _re.sub(r"([aAiIuU])([kKgGcCjJtTwWqQdDNpPbB])(n)$", r"\1n\2",
                   s, count=1)


def _deap(s: str) -> str:
    """Reverse ap-pratyaya (ci <- cap + aya <- capayati: strip -ap-)."""
    if len(s) > 2 and (s.endswith("ap") or s.endswith("Ap")):
        return s[:-2]
    return s


def _depagama(s: str) -> str:
    """Reverse p-agama (lI <- lApay + ...: Ap/Apay/Apaya hide I)."""
    import re as _re
    return _re.sub(r"Ap(ay|aya)?$", "I", s, count=1)


def _demrestore(s: str) -> str:
    """Reverse M-loss before sibilants (BraMS <- BraS + ya: M dropped)."""
    if len(s) > 1 and s[-1] in ("s", "S", "z"):
        return s[:-1] + "M" + s[-1:]
    return s


def _desam_y(s: str) -> str:
    """Reverse y-grade samprasarana with z-coda (jFz <- jIrya + ...:
    Iry/iry/Ury/ury hide F + z)."""
    import re as _re
    return _re.sub(r"(Iry|iry|Ury|ury)$", "Fz", s, count=1)


def _desam_u(s: str) -> str:
    """Reverse y-grade samprasarana, z-less roots (pF <- pUrya + ...)."""
    import re as _re
    return _re.sub(r"(Iry|iry|Ury|ury)$", "F", s, count=1)


def _denalo(s: str) -> str:
    """Reverse na-lopa (tan <- tA + yak, van <- va + ta: vowel-final
    base regains -n-)."""
    if len(s) > 1 and s[-1] == "A":
        return s[:-1] + "an"
    if len(s) > 1 and s[-1] == "I":
        return s[:-1] + "in"
    if len(s) > 1 and s[-1] == "U":
        return s[:-1] + "un"
    if len(s) > 1 and s[-1] == "a":
        return s + "n"
    return s


def _denaloR(s: str) -> str:
    """Reverse R-loss with lengthening (saR <- sA + ta: A regains aR)."""
    if len(s) > 1 and s[-1] == "A":
        return s[:-1] + "aR"
    return s


def _deM(s: str) -> str:
    """Reverse M-epenthesis/agama (sasanya <- saMsanya: drop M)."""
    import re as _re
    return _re.sub(r"M(?=[hHkKgGcCjJtTwWqQdDpPbBsSzZ])", "", s, count=1)


def _deMplace(s: str) -> str:
    """Reverse M-assimilation (saNgacCati <- saMgacCati: M regains N
    before velars, Y before palatals)."""
    import re as _re
    _v = _re.sub(r"M(?=[kKgGN])", "N", s, count=1)
    if _v != s:
        return _v
    return _re.sub(r"M(?=[cCjJY])", "Y", s, count=1)


def _demlabial(s: str) -> str:
    """Reverse m-assimilation (trunp <- trump + itum: m regains n
    before labials)."""
    import re as _re
    return _re.sub(r"m(?=[pPbB])", "n", s, count=1)


def _deY(s: str) -> str:
    """Reverse Y-coalescence (piYjaya <- pij + ya: j + y -> Y)."""
    import re as _re
    return _re.sub(r"Y(?=[kKgGcCjJtTwWqQdDNpPbBsSzZ])", "", s, count=1)


def _derot(s: str) -> str:
    """Reverse R-uttva (jfR <- jF + ...: drop epenthetic R)."""
    import re as _re
    return _re.sub(r"([fFxXuU])R", r"\1", s, count=1)


def _denfin(s: str) -> str:
    """Reverse final-n stems (lU <- lun + Ana: strip stem-final n)."""
    if len(s) > 2 and s[-1] in ("n", "N"):
        return s[:-1]
    return s


def _deks_z(s: str) -> str:
    """Reverse kSaya fusion keeping sibilant (Sikz <- Siz + sa: kz -> z)."""
    import re as _re
    return _re.sub(r"([kKgG])z$", "z", s, count=1)


def _deks_k(s: str) -> str:
    """Reverse kSaya fusion keeping stop (vakz <- vac + sya: kz -> k)."""
    import re as _re
    return _re.sub(r"([kKgG])z$", r"\1", s, count=1)


def _dena(s: str) -> str:
    """Reverse class-9 -nA- vikaraNa (krI <- krI + nA)."""
    if s.endswith(("nA", "nI")) and len(s) > 2:
        return s[:-2]
    return s


def _deaspire(s: str) -> str:
    """Reverse final aspiration loss (lab <- laB + ...): final stop
    regains aspiration."""
    _map = {"b": "B", "d": "D", "g": "G", "j": "J", "c": "C", "k": "K",
            "t": "T", "p": "P"}
    if len(s) > 1 and s[-1] in _map:
        return s[:-1] + _map[s[-1]]
    return s


def _deaspire_init(s: str) -> str:
    """Reverse initial aspiration loss (Bas <- bs + ita <- Bhas)."""
    _map = {"b": "B", "d": "D", "g": "G", "j": "J", "c": "C", "k": "K",
            "t": "T", "p": "P"}
    if len(s) > 1 and s[0] in _map:
        return _map[s[0]] + s[1:]
    return s


def _len_variants(s: str) -> List[str]:
    out = [s]
    if s and s[-1] in "iIuUfFxXaA":
        swap = {"i": "I", "I": "i", "u": "U", "U": "u", "f": "F", "F": "f",
                "x": "X", "X": "x", "a": "A", "A": "a"}
        out.append(s[:-1] + swap[s[-1]])
    if s and s[-1] == "n":
        # nasal-coda roots (saR <- sano + ...: dental n hides N/R)
        out.append(s[:-1] + "N")
        out.append(s[:-1] + "R")
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
# root-final deaspiration/devoicing before san-s (dh + s -> ts):
# full-type middles (rut <- rudh + sa) regain voiced/aspirate codas
_SAN_CODA = {
    "t": ["t", "d", "D", "dh", "Dh"], "T": ["T", "D", "Dh"],
    "p": ["p", "b", "B", "bh", "Bh"], "k": ["k", "g", "G", "gh", "Gh"],
    "c": ["c", "j", "J", "jh", "Jh"], "C": ["C", "J", "Jh"],
    "s": ["s"],
}


def _san_reverse(core: str) -> List[str]:
    """Undo desiderative formation (ditsa <- dA, vividiza <- vid).
    Full type keeps the root (vi-vid-i-za); contracted type fuses it
    (di-tsa <- dA + sa, d devoiced before san-s). Returns root candidates."""
    _w = core[:-1] if core.endswith("a") and len(core) > 1 else core
    out: List[str] = []
    if len(_w) >= 6 and _w[0] in SLP1_VOWELS and _w[2] in SLP1_VOWELS:
        # vowel-initial roots reduplicate VCV (asisiz <- as + san):
        # reduplicant V + C + V, remainder follows (si -> s -> as)
        _body = _w[:-1] if _w[-1] in ("s", "z", "S") else None
        if _body is not None:
            _mid = _body[3:]
            if len(_mid) >= 1:
                _mids = [_mid]
                if _mid.endswith("i") and len(_mid) > 1:
                    _mids.append(_mid[:-1])
                for _m in _mids:
                    if _m and _m not in out:
                        out.append(_m)
                return out
        return []
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
    if _mid.endswith(("si", "zi", "Si", "sI", "zI", "SI")) and len(_mid) > 3:
        # iT + san-s fusion (buBUziz <- bu + BU + i + sa): the trailing
        # sibilant is the desiderative -sa-, so strip both to reach BU
        _mids.append(_mid[:-2])
    for _m in _mids:
        if not _m:
            continue
        # contracted fusion: bare onset (dits-a <- dA + sa).
        if len(_m) == 1 and _m not in SLP1_VOWELS:
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
            # full-coda twin (cits <- Cid + sa: reduplicant + voiced coda)
            for _cc in _SAN_CODA.get(_m, [_m])[1:]:
                _c2 = _red + _cc
                if _c2 not in out:
                    out.append(_c2)
        else:
            # full type: root preserved (vivid <- vid; tik <- tij via kuH)
            if _m not in out:
                out.append(_m)
            if _m.endswith("k"):
                _j = _m[:-1] + "j"
                if _j not in out:
                    out.append(_j)
            # root-final stop devoiced/deaspirated before san-s
            # (rut <- rudh + sa, lips <- laB + sa)
            if len(_m) > 1 and _m[-1] in _SAN_CODA:
                for _cc in _SAN_CODA[_m[-1]][1:]:
                    _c2 = _m[:-1] + _cc
                    if _c2 not in out:
                        out.append(_c2)
    return out


def _yanluk_reverse(core: str) -> List[str]:
    """Undo yaNluganta reduplication (varivar <- vf + yaNluk: CVCV +
    onset-kept remainder; devdev <- div + ...: exact-copy halves).
    Grading is left to lookup."""
    out: List[str] = []
    if len(core) >= 6:
        _red, _rest = core[:4], core[4:]
        _onsets = _ABHYASA_ONSET.get(_red[0], [_red[0]])
        if _rest and _rest[0] in _onsets and _red[0] not in SLP1_VOWELS:
            if _red[1] in "aAiIeEoO" and _red[3] in "aAiIeEoO":
                if _rest not in out:
                    out.append(_rest)
    if len(core) >= 6:
        # exact-copy halves (devdev <- div + ... intensive doubling)
        _k = len(core) // 2
        if len(core) == 2 * _k and core[:_k] == core[_k:]:
            if core[_k:] not in out:
                out.append(core[_k:])
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
    # yaN infix after the reduplicant (panIpad <- pad + yaN:
    # reduplicant pa + infix nI + pad)
    if len(_rest) > 3 and _rest[:2] in (
            "nI", "ni", "nU", "nu", "rI", "ri", "rU", "ru"):
        _stripped = _rest[2:]
        if _stripped not in out:
            out.append(_stripped)
    return out


_sentinel = object()


def _acc_hits(acc: list, revs: list, label: str, extra=_sentinel) -> None:
    """Append every distinct root from reversal candidates (collect-all
    graded homographs: rod -> rud + ruD, devi -> dev + div)."""
    for _r in revs:
        for (_rc, _rm, _rv) in _lookup_all(_r):
            if all(_rc != _h[0] for _h in acc):
                acc.append((_rc, _rm, label) if extra is _sentinel
                           else (_rc, _rm, label, extra))


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
    """Reverse stop gemination (tott <- tod + tf, rudD <- rundh + ...,
    cCits <- Cid + san + ...)."""
    for _gem, _sg in (("tt", "d"), ("nn", "n"), ("cc", "c"), ("YY", "Y"),
                      ("dD", "D"), ("DD", "D"), ("bB", "B"), ("gG", "G"),
                      ("jJ", "J"), ("tT", "T"), ("cC", "c"), ("CC", "C")):
        if _gem in s:
            return s.replace(_gem, _sg, 1)
    return s


def _delong(s: str) -> str:
    """Reverse vrddhi-length grades (dIv <- div + ya, class-4 -ya-)."""
    _v = s.replace("I", "i").replace("U", "u").replace("F", "f").replace(
        "X", "x")
    return _v


_VOICE = {"t": "d", "T": "D", "p": "b", "P": "B", "k": "g", "K": "G",
          "c": "j", "C": "J", "w": "q", "W": "Q"}


def _devoice(s: str) -> str:
    """Reverse final devoicing (tot <- tod + tavya): final tenuis -> media."""
    if len(s) > 1 and s[-1] in _VOICE:
        return s[:-1] + _VOICE[s[-1]]
    return s


def _devoice_onset(s: str) -> str:
    """Reverse onset devoicing (bsita <- Bhas + ita: khari devoices
    the root onset before voiceless affixes)."""
    import re as _re
    return _re.sub(r"^([ptkc])", lambda m: _VOICE[m.group(1)], s, count=1)


def _deasyncope(s: str) -> str:
    """Reverse a-syncope in khari clusters (Bas <- bs + ita <- Bhas)."""
    import re as _re
    return _re.sub(r"^([pPbB])(s)$", r"\1as", s, count=1)


def _dental_n(s: str) -> str:
    """Reverse nd-amalgam (und <- ut + ta <- ud + ta: restore lost n)."""
    import re as _re
    return _re.sub(r"([aAiIuU])d$", r"\1nd", s, count=1)


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
        ("devoice", _devoice), ("khari", _dekhari), ("infix", _deinfix),
        ("nu", _denu), ("na", _dena), ("them", _dethem), ("long", _delong),
        ("it", _deit), ("meta9", _demeta9), ("mrest", _demrestore),
        ("samy", _desam_y), ("samu", _desam_u), ("ks_z", _deks_z),
        ("ks_k", _deks_k), ("deY", _deY), ("nalo", _denalo),
        ("naloR", _denaloR), ("deM", _deM), ("deMplace", _deMplace),
        ("demlab", _demlabial), ("derot", _derot),
        ("denfin", _denfin), ("deGhn", _deGhn), ("dea", _dea),
        ("depagama", _depagama),
        ("ap", _deap), ("riF", _deriF), ("vonset", _devoice_onset),
        ("async", _deasyncope), ("dentn", _dental_n),
        ("aspire", _deaspire), ("aspire0", _deaspire_init)]
_OP_CONF = {"exact": 1.0, "glide": 0.95, "guna": 0.92, "thematic": 0.9,
            "irreg": 0.95, "vrddhi": 0.8, "cha": 0.8, "cutva": 0.75,
            "ur": 0.7, "urv": 0.7, "double": 0.7, "nasal": 0.7, "nasaln": 0.65,
            "ovo": 0.7, "uv": 0.6, "yan": 0.75, "devoice": 0.6,
            "khari": 0.6, "infix": 0.65, "nu": 0.65, "na": 0.65,
            "them": 0.6, "long": 0.65, "it": 0.6, "meta9": 0.65,
            "mrest": 0.6, "samy": 0.65, "samu": 0.65, "ks_z": 0.6,
            "ks_k": 0.6, "deY": 0.6, "nalo": 0.6, "naloR": 0.6, "deM": 0.6,
            "deMplace": 0.6, "demlab": 0.6, "derot": 0.6, "denfin": 0.6,
            "deGhn": 0.65, "dea": 0.6,
            "depagama": 0.6,
            "ap": 0.6, "riF": 0.65, "vonset": 0.55, "async": 0.55,
            "dentn": 0.6, "aspire": 0.55, "aspire0": 0.55}


def _via_conf(via: str) -> float:
    _parts = [p for p in via.split("+") if p in _OP_CONF]
    if not _parts:
        return 0.6
    return min(_OP_CONF[p] for p in _parts)


_LOOKUP_CACHE: Dict[str, object] = {}


def _lookup_all(cand: str) -> list:
    """Graded-closure root lookup, all distinct roots.

    Same BFS as :func:`_lookup_root` but collects every reachable root
    (graded homographs: rod -> rud via guna and ruD via aspire+guna,
    devi -> dev via uv and div via uv+guna). Ordered by (depth,
    discovery), so element 0 always equals :func:`_lookup_root`.
    Each entry is (clean, meta, via)."""
    if not cand or len(cand) > 12:
        return []
    if cand in _LOOKUP_ALL_CACHE:
        return _LOOKUP_ALL_CACHE[cand]

    def _try(_s: str):
        for _c in _len_variants(_s):
            if _c in _ROOTS:
                return _c
        return None

    out = []
    _seen_roots = set()

    def _add(_hit, _via):
        if _hit not in _seen_roots:
            _seen_roots.add(_hit)
            out.append((_hit, _ROOTS[_hit], _via))

    _seen = {cand}
    for _c in _len_variants(cand):
        if _c in _ROOTS:
            _add(_c, "exact")
    # Natva reversal (praRamati -> nam): R could hide dental n
    if "R" in cand:
        for (_rc, _rm, _rv) in _lookup_all(cand.replace("R", "n")):
            if _rc not in _seen_roots:
                _seen_roots.add(_rc)
                out.append((_rc, _rm, "natva+" + _rv))
    # irregular presents (gacCha <- gam, yacCha <- yam/dA)
    _irr = _irreg_pres(cand)
    if _irr is not None:
        for (_m, _c) in _irr:
            if _c not in _seen_roots:
                _seen_roots.add(_c)
                out.append((_c, _m, "irreg"))
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
            for _c in _len_variants(_s):
                if _c in _ROOTS and _c not in _seen_roots:
                    _seen_roots.add(_c)
                    out.append((_c, _ROOTS[_c], _vv))
        _level = _nxt
        if not _level:
            break
    # -cCha- presents (gacCati <- gam, yacCati <- yam)
    if cand.endswith("cC") and len(cand) > 2:
        for _c in _len_variants(cand[:-2] + "m"):
            if _c in _ROOTS and _c not in _seen_roots:
                _seen_roots.add(_c)
                out.append((_c, _ROOTS[_c], "cha"))
    _LOOKUP_ALL_CACHE[cand] = out
    return out


_LOOKUP_ALL_CACHE: Dict[str, list] = {}


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

# periphrastic-kvasu auxiliaries: kvasu nominatives of the three universal
# auxiliaries kf/as/BU (cakfvAn/cakruzI, AsivAn/AsyuzI, baBUvAn/baBUzI +
# neuters). Closed inventory like the liT aux table; the lexical stem
# side stays fully generative (buBUzAmbaBUvAn <- BU + sannanta).
_KVASU_AUX = ("cakfvAn", "cakfvad", "cakfvas", "cakfvat", "cakruzI",
              "AsivAn", "Asivad", "Asivas", "Asivat", "AsyuzI",
              "baBUvAn", "baBUvad", "baBUvas", "baBUvat", "baBUzI")


def _krd_hits(base: str) -> list:
    """Root candidates for a krdanta stem-base: graded closure first, then
    abhyasa (yaN/class-3: boBUy -> BU) and san (buBUz -> BU) reversals,
    every distinct root kept (rod -> rud + ruD)."""
    out = []

    def _try(_b: str) -> None:
        for (_rc, _rm, _rv) in _lookup_all(_b):
            if all(_rc != o[0] for o in out):
                out.append((_rc, _rm, _rv))
        for _ab in _abhyasa_reverse(_b):
            for (_rc, _rm, _rv) in _lookup_all(_ab):
                if all(_rc != o[0] for o in out):
                    out.append((_rc, _rm, "abhyasa"))
        for _yl in _yanluk_reverse(_b):
            for (_rc, _rm, _rv) in _lookup_all(_yl):
                if all(_rc != o[0] for o in out):
                    out.append((_rc, _rm, "yanluk"))
        for _sn in _san_reverse(_b):
            for (_rc, _rm, _rv) in _lookup_all(_sn):
                if all(_rc != o[0] for o in out):
                    out.append((_rc, _rm, "san"))

    _try(base)
    if base.endswith(("i", "I")) and len(base) > 2:
        _try(base[:-1])  # sew-iT before the affix (buBUzi -> buBUz -> BU)
    return out


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

    # kta / ktavatu via exact kta-stem map (handles all sandhi irregulars;
    # one stem can serve several roots: BfzwaH is Brajj + BfS at once)
    _core = stem[:-1] + "a" if stem.endswith("A") else stem
    for _rt in _KTA_MAP.get(_core, []):
        _emit("kta", _rt, _ROOTS[_rt], 0.95)
    if stem.endswith("vat"):
        for _rt in _KTA_MAP.get(stem[:-3], []):
            _emit("ktavatu", _rt, _ROOTS[_rt], 0.95)
    if stem.endswith("vAn"):
        for _rt in _KTA_MAP.get(stem[:-3], []):
            _emit("ktavatu", _rt, _ROOTS[_rt], 0.95)
    # secondary stems always run too (exact map misses alternate kta
    # allomorphs: sAtaH is saR + ta but maps only to sE; dedup keeps
    # exact winners on ties)
    # kta/ktavatu of secondary stems (san/nich/yang: buBUzita,
    # BAvita, boBUyita <- BU): strip the -ta- and reverse the stem
    _kb = None
    if _core.endswith("ita") and len(_core) > 4:
        _kb = _core[:-3]
    elif _core.endswith("ta") and len(_core) > 3:
        _kb = _core[:-2]
    elif _core.endswith("na") and len(_core) > 3:
        _kb = _core[:-2]
    if _kb is not None:
        for (_rt, _m, _via) in _krd_hits(_kb):
            _emit("kta", _rt, _m, 0.8, f"root via {_via}")
    _kv = None
    if stem.endswith("vat") and len(stem) > 5:
        _kv = stem[:-3]
    elif stem.endswith("vAn") and len(stem) > 5:
        _kv = stem[:-3]
    if _kv is not None:
        _kvb = _kv[:-3] if _kv.endswith("ita") and len(_kv) > 4 \
            else (_kv[:-2] if _kv.endswith("ta") and len(_kv) > 3
                  else None)
        if _kvb is not None:
            for (_rt, _m, _via) in _krd_hits(_kvb):
                _emit("ktavatu", _rt, _m, 0.8, f"root via {_via}")
    # tavya / anIyar / yat via graded closure (iT, natva, geminates inside)
    if stem.endswith("tavya"):
        _tb = stem[:-5]
        _hits = _krd_hits(_tb)
        if not _hits and stem.endswith("itavya"):
            _hits = _krd_hits(stem[:-6])  # sew iT (Bavi -> Bav)
        if _hits:
            for (_rt, _m, _via) in _hits:
                _emit("tavya", _rt, _m,
                      0.85 if _via not in ("abhyasa", "san") else 0.7,
                      f"root via {_via}")
        else:
            _emit("tavya", None, None, 0.5, "root unresolved")
    for _suf, _restore in (("anIya", ""), ("RIya", ""), ("AnIya", "A")):
        if stem.endswith(_suf):
            # natva/vrddhi sit inside the suffix (karaRIya, dAnIya)
            _hits = _krd_hits(stem[:-len(_suf)] + _restore)
            if _hits:
                for (_rt, _m, _via) in _hits:
                    _emit("anIyar", _rt, _m,
                          0.85 if _via not in ("abhyasa", "san") else 0.7,
                          f"root via {_via}")
            else:
                _emit("anIyar", None, None, 0.5, "root unresolved")
            break
    if stem.endswith("ya") and len(stem) > 3:
        for (_rt, _m, _via) in _krd_hits(_devrddhi(stem[:-2])):
            _emit("yat", _rt, _m,
                  0.85 if _via not in ("abhyasa", "san") else 0.7,
                  f"root via {_via}")
    # SAnac (muk -mAna-, plain -Ana, natva -ARa-, passive -yak-,
    # future -sya- + muk: BAvizyamaRa <- BU + i + sya)
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
            if _b.endswith(("sya", "zya")) and len(_b) > 4:
                _cands.append(_b[:-3])  # future -sya- (BAvizya -> BAviz)
                _t = _b[:-3]
                # iT + san-s fusion (BAviz <- BAv + i + sa)
                if _t.endswith(("si", "zi", "Si", "sI", "zI", "SI")) \
                        and len(_t) > 3:
                    _cands.append(_t[:-2])
                elif _t.endswith(("i", "I")) and len(_t) > 2:
                    _cands.append(_t[:-1])
            _hits = []
            _seen_rt = set()
            for _c in _cands:
                for (_rt, _m, _via) in _krd_hits(_c):
                    if _rt not in _seen_rt:
                        _seen_rt.add(_rt)
                        _hits.append((_rt, _m, _via))
            if _hits:
                for (_rt, _m, _via) in _hits:
                    _emit("SAnac", _rt, _m,
                          0.8 if _via not in ("abhyasa", "san") else 0.7,
                          f"root via {_via}")
            else:
                _emit("SAnac", None, None, 0.5, "present stem; root unresolved")
            break
    # lyuw action noun (-ana): Bavana <- BU; Natva-R twin (-aRa): vidaRa <- vid
    if (stem.endswith("ana") or stem.endswith("aRa")) and len(stem) > 4:
        for (_rt, _m, _via) in _krd_hits(stem[:-3]):
            _emit("lyuw", _rt, _m,
                  0.8 if _via not in ("abhyasa", "san") else 0.7,
                  f"root via {_via}")
    # GaY (vrddhi + a: BAva <- BU) vs ac (guNa + a: toda <- tud);
    # feminine -A forms take the "a" label (todA)
    if (stem.endswith("a") and len(stem) > 2) or \
            (stem.endswith("A") and len(stem) > 2):
        _fem = stem.endswith("A")
        _b = stem[:-1]
        _hits = _krd_hits(_b)
        if not _hits and _b.endswith("R") and len(_b) > 2:
            # Natva-R stem (vidaRa <- vid + lyuw): R hides the root
            # coda, so retry without it (vida -> vid via thematic)
            _hits = _krd_hits(_b[:-1])
        for (_rt, _m, _via) in _hits:
            _vrddhi = ("A" in _b or "Ay" in _b or "Av" in _b or "E" in _b
                       or "O" in _b)
            _secondary = _via in ("abhyasa", "san")
            _conf = 0.7 if _fem or _vrddhi else 0.6
            if _secondary:
                _conf = min(_conf, 0.6)
            if _fem:
                _emit("a", _rt, _m, _conf, f"root via {_via}")
            elif _vrddhi:
                # GaY and ac share the vrddhi-a surface across antas
                # (BAvaH is krut-GaY but nich_krut-ac): list both
                _emit("GaY", _rt, _m, _conf, f"root via {_via}")
                _emit("ac", _rt, _m, max(0.1, _conf - 0.05),
                      f"root via {_via}; ac/GaY same surface")
            else:
                _emit("ac", _rt, _m, _conf, f"root via {_via}")
                _emit("ap", _rt, _m, max(0.1, _conf - 0.05),
                      f"root via {_via}; ap/ac same surface")
            if _secondary:
                # reduplicated/desiderative action nouns (buBUza) carry no
                # vrddhi grade, but the data files them under GaY as well
                _emit("GaY", _rt, _m, 0.6,
                      f"root via {_via}; secondary-stem GaY twin")
    # Rvul / tfc (+ ukaY agent noun: BAvuka <- BU)
    if stem.endswith("aka") or stem.endswith("ikA"):
        _b = stem[:-3]
        for (_rt, _m, _via) in _krd_hits(_devrddhi(_b)):
            _emit("Rvul", _rt, _m,
                  0.85 if _via not in ("abhyasa", "san") else 0.7,
                  f"root via {_via}")
    if stem.endswith("uka") or stem.endswith("ukA"):
        _b = stem[:-3]
        for (_rt, _m, _via) in _krd_hits(_devrddhi(_b)):
            _emit("ukaY", _rt, _m,
                  0.8 if _via not in ("abhyasa", "san") else 0.7,
                  f"root via {_via}")
    if stem.endswith("tf") or stem.endswith("trI"):
        # vowel base (Bavi + tf) vs consonant base (tott + f, d devoiced+geminated)
        _b = stem[:-2] if stem.endswith("tf") else stem[:-3]
        _cands = [_b, stem[:-1]]
        if _b.endswith("i") and len(_b) > 1:
            _cands.append(_b[:-1])  # sew iT (Bavi -> Bav)
        _tseen = set()
        for _c in _cands:
            for (_rt, _m, _via) in _krd_hits(_c):
                if _rt in _tseen:
                    continue
                _tseen.add(_rt)
                _emit("tfc", _rt, _m,
                      0.85 if _via not in ("abhyasa", "san") else 0.7,
                      f"root via {_via}")
    # Satf present stem: irregulars (multi-root) first, then graded
    # closure (Bav/tud regulars, gacCh via cha, Bavizya via sya-strip),
    # abhyasa (dadat <- dA) and san (buBUzat <- BU) secondaries.
    # Guard excludes ktavatu (-tavat); juhvat-type (-hvat) stays eligible.
    if stem.endswith("ant") or (stem.endswith("at") and not stem.endswith("tavat")):
        _core = stem[:-3] if stem.endswith("ant") else stem[:-2]
        _done = False
        _seen_rt = set()
        _satf_bases = [_core]
        if _core.endswith(("sy", "zy")) and len(_core) > 3:
            # future stem (Bavizyat <- Bav + i + sya + t: the Satf -t-
            # split above ate sya's vowel, leaving -sy-): strip sya + iT
            _satf_bases.append(_core[:-2])
            if _core[:-2].endswith("i") and len(_core[:-2]) > 1:
                _satf_bases.append(_core[:-3])
        for _base in _satf_bases:
            _irr = _irreg_pres(_base)
            if _irr is not None:
                for (_m, _c) in _irr:
                    if _c not in _seen_rt:
                        _emit("Satf", _c, _m, 0.9, "irregular present stem")
                        _seen_rt.add(_c)
                _done = True
            # plain closure AND secondaries: dadat is genuinely dad-Satf
            # and dA-Satf at once
            for (_rt, _m, _via) in _krd_hits(_base):
                if _rt not in _seen_rt:
                    _emit("Satf", _rt, _m,
                          0.85 if _via not in ("abhyasa", "san") else 0.7,
                          f"root via {_via}")
                    _seen_rt.add(_rt)
                _done = True
            for _cand in _abhyasa_reverse(_base):
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
    # ktin action noun, strI-only (BUtiH <- BU, BAtiH <- BU + Ric
    # with ay-lopa): base + ti, plus Ava-restored base for Rejanta loss
    if linga == "strI" and stem.endswith("ti") and len(stem) > 3:
        _ktb = [stem[:-2]]
        if stem[:-2].endswith("A") and len(stem[:-2]) > 1:
            _ktb.append(stem[:-3] + "Ava")
        for _kb in _ktb:
            for (_rt, _m, _via) in _krd_hits(_kb):
                _emit("ktin", _rt, _m,
                      0.7 if _via not in ("abhyasa", "san") else 0.6,
                      f"root via {_via}")
    # u-pratyaya agent noun (buBUzu <- BU + san): only via secondary
    # stems, so plain u-final nouns (guru) stay silent
    if stem.endswith("zu") and len(stem) > 3:
        _ub = stem[:-2] if stem.endswith("uzu") and len(stem) > 4 else stem[:-1]
        _uhits = []
        for _ab in _abhyasa_reverse(_ub):
            _acc_hits(_uhits, [_ab], "abhyasa")
        for _yl in _yanluk_reverse(_ub):
            _acc_hits(_uhits, [_yl], "yanluk")
        for _sn in _san_reverse(_ub):
            _acc_hits(_uhits, [_sn], "san")
        for (_rt, _m, _via) in _uhits:
            _emit("u", _rt, _m, 0.65, f"root via {_via}")
    # kvasu perfect participle: weak -uz- stem + strong -vas- stem.
    # Resolve the root via samprasarana/v-strip + abhyasa/san
    # (baBUvAn/baBUzI/baBUvat <- BU); keep the unresolved tail.
    _kvasu_done = False
    _kvbases = []
    if stem.endswith("uzI") or stem.endswith("UzI"):
        _kvbases.append(stem[:-3])
    elif stem.endswith("uz"):
        _kvbases.append(stem[:-2])
    elif stem.endswith("Uz"):
        _kvbases.append(stem)  # weak stem proper (baBUz)
    if stem.endswith("vas") or stem.endswith("vAMs"):
        _kvbases.append(stem[:-3] if stem.endswith("vas") else stem[:-4])
    if (stem.endswith("at") or stem.endswith("ad")) and "v" in stem \
            and len(stem) > 4:
        # strong neuter kvasu (baBUvat) collides with Satf: only admit
        # perfect-reduplicated bases (abhyasa/san), never plain ones
        _kvbases.append(("neuter-at", stem[:-2]))
    for _kb in _kvbases:
        _neuter_at = isinstance(_kb, tuple)
        if _neuter_at:
            _kb = _kb[1]
        _kc = [_kb]
        if _kb.endswith("v") and len(_kb) > 2:
            _kc.append(_kb[:-1])  # perfect -va- (baBUva -> baBU)
        if _kb.endswith(("z", "Z")) and len(_kb) > 3:
            _kc.append(_kb[:-1])  # weak -z- (baBUz -> baBU)
        for _c in _kc:
            _khits = _krd_hits(_c)
            if _neuter_at:
                # plain-lookup hits are Satf, not kvasu: keep only
                # reduplication-derived (abhyasa/san) roots
                _khits = [h for h in _khits if h[2] in ("abhyasa", "san")]
            for (_rt, _m, _via) in _khits:
                _emit("kvasu", _rt, _m,
                      0.75 if _via not in ("abhyasa", "san") else 0.65,
                      f"root via {_via}")
                _kvasu_done = True
        if _kvasu_done:
            break
    if stem.endswith(("uz", "Uz", "uzI", "UzI")) and not _kvasu_done:
        out.append({"kind": "krdanta", "pratyaya": "kvasu", "stem": stem,
                    "dhatu": None, "linga": linga, "vibhakti": vib,
                    "vacana": vac, "confidence": 0.45,
                    "note": "samprasarana stem; root unresolved in v1"})
    # gsnu desiderative adjective (BUzRuH <- BU + snu: snu -s- voices to
    # -z- by zatva, -nu- retroflexes to -Ru by natva): strip -Ru, undo
    # zatva (z->s), drop the snu -s-
    if stem.endswith("Ru") and len(stem) > 3:
        _gb = stem[:-2]
        if _gb.endswith("z"):
            _gb = _gb[:-1] + "s"
        if _gb.endswith("s") and len(_gb) > 2:
            for (_rt, _m, _via) in _krd_hits(_gb[:-1]):
                _emit("gsnu", _rt, _m,
                      0.7 if _via not in ("abhyasa", "san") else 0.6,
                      f"root via {_via}")
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
    ("Am", "laN", "uttama", "eka"),
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
    # z-fused athematic variants (Sinazwi <- Siz + na + z + ti,
    # Sinakzi <- ... + kzi): strip to the z-ful stem below
    ("wi", "lw", "prathama", "eka"),
    ("kzi", "lw", "prathama", "bahu"),
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
    ("Qve", "lw", "madhyama", "bahu"),
    ("e", "lw", "uttama", "eka"), ("vahe", "lw", "uttama", "dvi"),
    ("Avahe", "lw", "uttama", "dvi"),
    ("mahe", "lw", "uttama", "bahu"),
    ("Amahe", "lw", "uttama", "bahu"),
    ("anta", "laN", "prathama", "bahu"), ("etAm", "laN", "prathama", "dvi"),
    ("ta", "laN", "prathama", "eka"), ("TAH", "laN", "madhyama", "eka"),
    ("eTAm", "laN", "madhyama", "dvi"), ("Dvam", "laN", "madhyama", "bahu"),
    ("i", "laN", "uttama", "eka"), ("vahi", "laN", "uttama", "dvi"),
    ("Avahi", "laN", "uttama", "dvi"),
    ("mahi", "laN", "uttama", "bahu"),
    ("Amahi", "laN", "uttama", "bahu"),
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
# t/d voicing twins (BavatAt/BavatAd, aBavat/aBavad: final -t voices to -d)
# plus systematic zwutva twins (8.4.41: dental -> retroflex) and zatva
# twins (s -> z after i/u: tanuzva <- tanu + sva): every tin ending
# fans out over dental/retroflex/sibilant spellings. Matching is
# endswith-based, so twins only fire on words that actually show the
# surface; lookup + forward-verify gate.
_DENT_MAP = {"t": ("t", "T", "w"), "T": ("T", "W"), "d": ("d", "D", "q"),
             "D": ("D", "Q"), "n": ("n", "N", "R"), "s": ("s", "z", "S")}


def _dent_variants(end: str) -> set:
    out = {end}
    for _i, _ch in enumerate(end):
        if _ch in _DENT_MAP:
            # s-twins only initially (zatva: tanuzva <- tanu + sva);
            # medial s stays put
            _alts = _DENT_MAP[_ch] if (_ch != "s" or _i == 0) else (_ch,)
            out |= {_v[:_i] + _alt + _v[_i + 1:]
                    for _v in list(out) for _alt in _alts}
    return out


for _t, _pada in ((_TIN_P, None), (_TIN_A, None)):
    for (_end, _lak, _pur, _vac) in list(_t):
        if _end.endswith("t"):
            _t.append((_end[:-1] + "d", _lak, _pur, _vac))
    _have = set(e for (e, _, _, _) in _t)
    for (_end, _lak, _pur, _vac) in list(_t):
        for _re in _dent_variants(_end):
            if _re != _end and _re not in _have:
                _t.append((_re, _lak, _pur, _vac))
                _have.add(_re)
if ("THAH", "laN", "madhyama", "eka") not in _TIN_A:
    _TIN_A.append(("THAH", "laN", "madhyama", "eka"))
    _TIN_A.append(("WAH", "laN", "madhyama", "eka"))


def _stem_desandhi(word: str) -> List[str]:
    """Stem-final t-absorption variants (analysis-only extra surfaces).

    dh/j + tin-t fuse (rundDAm <- rundh + tAm, yuYakti <- yuYaj + ti):
    restore the absorbed t (and voice the palatal) so ending tables
    match. Regex-gated: only fires on infix/amalgam signatures.
    """
    import re as _re
    out = []
    for _m in _re.finditer(r"([nNY])([dD]?)([DT])(?=A)", word):
        _v = word[:_m.start()] + _m.group(1) + _m.group(3) + "t" \
            + word[_m.end():]
        if _v != word and _v not in out:
            out.append(_v)
    for _m in _re.finditer(r"([bdgGjJcC])([DT])(?=A)", word):
        _v = word[:_m.start()] + _m.group(1) + "t" + word[_m.end():]
        if _v != word and _v not in out:
            out.append(_v)
    return out


def _tin_candidates(core: str, lakara: str, aug: bool) -> List[str]:
    # stripped variants first: exact hits on them outrank longer paths
    cands = []
    if core.endswith("a") and len(core) > 1:
        cands.append(core[:-1])  # thematic -a-
    if core.endswith("A") and len(core) > 1:
        cands.append(core[:-1])  # thematic -A- (uttama Ami/AvaH/AmaH twins)
    cands.append(core)
    if len(core) == 1 and core not in SLP1_VOWELS:
        # athematic elision (santi <- as + anti, 2.4.52 asor allopa):
        # restore the dropped root vowel
        cands.append("a" + core)
    if core.endswith("y") and len(core) > 2:
        # buried yak/thematic vowel (BAvy <- BAva + yak + e, buBUzy <-
        # buBUz + yak + a): restore -a- so the yak strip below can fire
        _plus = core + "a"
        if _plus not in cands:
            cands.append(_plus)
    for _c in list(cands):
        # karmani/passive -ya- (BUyate <- BU + yak)
        if _c.endswith("ya") and len(_c) > 2 and _c[:-2] not in cands:
            cands.append(_c[:-2])
    for _c in list(cands):
        # Rejanta causative -aya- (BAvayati <- BU + Ric): strip the
        # affix so graded closure (Av -> o -> u) can reach the root
        if _c.endswith("aya") and len(_c) > 3 and _c[:-3] not in cands:
            cands.append(_c[:-3])
        elif _c.endswith("Aya") and len(_c) > 3 and _c[:-3] not in cands:
            cands.append(_c[:-3])
        elif _c.endswith(("ay", "Ay")) and len(_c) > 3 \
                and _c[:-2] not in cands:
            cands.append(_c[:-2])  # nichay without thematic (BAvay)
    for _c in list(cands):
        # short thematic vowel (boBavI <- yangluk boBav + I): strip so
        # abhyasa reversal can reach the root
        if _c.endswith(("i", "I")) and len(_c) > 2 \
                and _c[:-1] not in cands:
            cands.append(_c[:-1])
    if aug:
        _stripped = []
        for _c in cands:
            if _c.startswith("a") and len(_c) > 1:
                _stripped.append(_c[1:])  # laN augment a-
            elif _c.startswith("A") and len(_c) > 1:
                _stripped.append(_c[1:])
            elif _c.startswith("E") and len(_c) > 2:
                # augment fused with a-initial root vowel (a + eD -> ED):
                # restore a + e, the plain strip eats the root vowel
                _stripped.append("ae" + _c[1:])
                _stripped.append("e" + _c[1:])
            elif _c.startswith("O") and len(_c) > 2:
                _stripped.append("ao" + _c[1:])
                _stripped.append("o" + _c[1:])
        cands += _stripped
    for _c in list(cands):
        # v-loss in reduplicated stems (dede <- devdev + ...: yangluk
        # laN adedet): restore v after each e-grade vowel
        import re as _re
        _vr = _re.sub(r"^([^aAiIuUeEoO])e([^aAiIuUeEoO])e$",
                      r"\1ev\2ev", _c)
        if _vr != _c and _vr not in cands:
            cands.append(_vr)
    for _c in list(cands):
        # R-uttva before semivowel/grade (puRwati <- puwi + ...,
        # DfRAti <- DF + ...): drop the epenthetic R
        import re as _re
        _nor = _re.sub(r"([fFxXuU])R(?=[Aawy]|$)", r"\1", _c)
        if _nor != _c and _nor not in cands:
            cands.append(_nor)
    for _c in list(cands):
        # M-agama / epenthesis (bfMhati <- bfhi + M, saMsanya <- sasanya):
        # drop M before consonants
        import re as _re
        for _m in _re.finditer(r"M(?=[hHkKgGcCjJtTwWqQdDpPbBsSzZ])", _c):
            _v = _c[:_m.start()] + _c[_m.end():]
            if _v not in cands:
                cands.append(_v)
    for _c in list(cands):
        # z-less class-7 stems (Sina <- Siz + na + ...: root coda lost
        # before dental endings): restore z/s
        import re as _re
        if _re.search(r"[iIuU](na|Na)$", _c) and len(_c) > 3:
            for _sib in ("z", "s"):
                if _c + _sib not in cands:
                    cands.append(_c + _sib)
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

    # luT periphrastic future (-tA-): BavitA, vaktA, kartA.
    # tA voices/aspirates after root-final voiced/aspirate
    # (roDDA <- ruD + tA): d/DA twins share each slot.
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
    _LUT = _LUT + [(_suf, _pur, _vac, _pada)
                   for (_suf, _pur, _vac, _pada) in
                   [(s.replace("t", "d", 1), p, v, pa) for (s, p, v, pa) in _LUT]
                   + [(s.replace("t", "D", 1), p, v, pa) for (s, p, v, pa) in _LUT]]
    for _suf, _pur, _vac, _pada in _LUT:
        if word.endswith(_suf) and len(word) > len(_suf) + 1:
            _core = word[:-len(_suf)]
            _cands = [_core]
            if _core.endswith("i") and len(_core) > 1:
                _cands.append(_core[:-1])  # sew iT (Bavi -> Bav)
            _mstrip = _deM(_core)
            if _mstrip != _core and _mstrip not in _cands:
                _cands.append(_mstrip)  # M-epenthesis (titAMsi)
            _luw_hits: list = []
            for _c in _cands:
                for (_rc, _rm, _rv) in _lookup_all(_c):
                    if _rc not in [h[0] for h in _luw_hits]:
                        _luw_hits.append((_rc, _rm, _rv, None))
                # secondary future stems (buBUzitA <- BU + sannanta)
                for _ab in _abhyasa_reverse(_c):
                    _acc_hits(_luw_hits, [_ab], "abhyasa", None)
                for _yl in _yanluk_reverse(_c):
                    _acc_hits(_luw_hits, [_yl], "yanluk", None)
                for _sn in _san_reverse(_c):
                    _acc_hits(_luw_hits, [_sn], "san", "sannanta")
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
            _lfthits: list = []
            for _c in _cands:
                _try = [_c]
                if _aug and len(_c) > 1:
                    _try.append(_c[1:])  # lfN augment
                for _t in _try:
                    for (_rc, _rm, _rv) in _lookup_all(_t):
                        if _rc not in [h[0] for h in _lfthits]:
                            _lfthits.append((_rc, _rm, _rv))
                    # secondary future stems (buBUzizyati <- BU + sannanta):
                    # undo reduplication / desiderative formation first
                    for _ab in _abhyasa_reverse(_t):
                        _acc_hits(_lfthits, [_ab], "abhyasa")
                    for _yl in _yanluk_reverse(_t):
                        _acc_hits(_lfthits, [_yl], "yanluk")
                    for _sn in _san_reverse(_t):
                        _acc_hits(_lfthits, [_sn], "san")
            _hit = _lfthits[0] if _lfthits else None
            # every non-primary root rides along (abhyasa hits can shadow
            # san twins: buBUz -> BUz hides buBUz -> BU)
            if _hit is None:
                continue
            _aug = _stem[:1] in ("a", "A")
            _all_hits = _lfthits
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
    # ASIrliN parasmaipada (-yA-): BUyAt, kuryAt.
    # The same -yA- formation fills yangluk/san/nich viDiliN slots in
    # the data (boBUyAt is yangluk pvidhiling): emit the viDiliN twin
    # alongside every ASIrliN reading.
    _ASI = [("yAstAm", "prathama", "dvi"), ("yAsuH", "prathama", "bahu"),
            ("yAstam", "madhyama", "dvi"), ("yAsta", "madhyama", "bahu"),
            ("yAsam", "uttama", "eka"), ("yAsva", "uttama", "dvi"),
            ("yAsma", "uttama", "bahu"), ("yAt", "prathama", "eka"),
            ("yAd", "prathama", "eka"),
            ("yAH", "madhyama", "eka")]
    # yangluk viDiliN uttama triple without -s- (boBUyAm/yAva/yAma)
    # plus s-less dvi/bahu (yAtAm/yuH/yAtam/yAta): viDiliN-only
    # formations, never ASIrliN
    _ASI_VIDHI = [("yAm", "uttama", "eka"), ("yAva", "uttama", "dvi"),
                  ("yAma", "uttama", "bahu"), ("yAtAm", "prathama", "dvi"),
                  ("yuH", "prathama", "bahu"),
                  ("yAtam", "madhyama", "dvi"),
                  ("yAta", "madhyama", "bahu")]
    # ASIrliN Atmanepada s-forms (-sIy-): vedizIzwa, vedizIran (+z twins)
    for _suf, _pur, _vac in _ASI:
        if word.endswith(_suf) and len(word) > len(_suf):
            _core = word[:-len(_suf)]
            # stem candidates: plain, thematic, restored yak vowel
            # (BAvy <- BAva + yak), yak-strip, Rejanta-strip
            _ascc = [_core]
            if _core.endswith(("a", "A")) and len(_core) > 1:
                _ascc.append(_core[:-1])
            if _core.endswith("y") and len(_core) > 2:
                _ascc.append(_core + "a")
            _asi_hits: list = []
            _seen_as = set()
            for _ac in _ascc:
                _ac2 = [_ac]
                if _ac.endswith("ya") and len(_ac) > 2:
                    _ac2.append(_ac[:-2])
                if _ac.endswith(("aya", "Aya")) and len(_ac) > 4:
                    _ac2.append(_ac[:-3])
                for _c in _ac2:
                    if _c in _seen_as:
                        continue
                    _seen_as.add(_c)
                    for (_rc, _rm, _rv) in _lookup_all(_c):
                        if _rc not in [h[0] for h in _asi_hits]:
                            _asi_hits.append((_rc, _rm, "exact", None))
                    if _c.endswith("ur") and len(_c) > 2:
                        # kur <- kf via u-samprasarana (kuryAt)
                        for (_rc, _rm, _rv) in _lookup_all(_c[:-2] + "f"):
                            if _rc not in [h[0] for h in _asi_hits]:
                                _asi_hits.append((_rc, _rm, "exact", None))
            # secondary benedictive stems (buBUzyAt <- BU + sannanta)
            for _ab in _abhyasa_reverse(_core):
                _acc_hits(_asi_hits, [_ab], "abhyasa", None)
            for _yl in _yanluk_reverse(_core):
                _acc_hits(_asi_hits, [_yl], "yanluk", None)
            for _sn in _san_reverse(_core):
                _acc_hits(_asi_hits, [_sn], "san", "sannanta")
            for (_rt, _m, _via, _sd) in _asi_hits:
                _emit(_rt, _m, "ASIrliN", _pur, _vac, _via, 0.8, _core,
                      _sanadi=_sd)
                _emit(_rt, _m, "viDiliN", _pur, _vac, _via, 0.7,
                      _core + " (vidhi-twin of -yA- formation)",
                      _sanadi=_sd)
            if _asi_hits:
                break
    for (_suf, _pur, _vac) in _ASI_VIDHI:
        if word.endswith(_suf) and len(word) > len(_suf) + 1:
            _core = word[:-len(_suf)]
            _vhits: list = []
            for _c in _tin_candidates(_core, "viDiliN", False):
                for (_rc, _rm, _rv) in _lookup_all(_c):
                    if _rc not in [h[0] for h in _vhits]:
                        _vhits.append((_rc, _rm, "exact", None))
                for _ab in _abhyasa_reverse(_c):
                    _acc_hits(_vhits, [_ab], "abhyasa", None)
                for _yl in _yanluk_reverse(_c):
                    _acc_hits(_vhits, [_yl], "yanluk", None)
                for _sn in _san_reverse(_c):
                    _acc_hits(_vhits, [_sn], "san", "sannanta")
            for (_rt, _m, _via, _sd) in _vhits:
                _emit(_rt, _m, "viDiliN", _pur, _vac, _via, 0.75, _core,
                      _sanadi=_sd)
            if _vhits:
                break
    _ASI_ATM = [("IzWam", "madhyama", "dvi"), ("IDvam", "madhyama", "bahu"),
                ("IyA", "uttama", "eka"), ("Iya", "uttama", "eka"),
                ("Ivahi", "uttama", "dvi"), ("Imahi", "uttama", "bahu"),
                ("Iran", "prathama", "bahu"), ("IyAstAm", "prathama", "dvi"),
                ("IyAsTAm", "madhyama", "dvi"), ("Izwa", "prathama", "eka"),
                ("IzWAH", "madhyama", "eka")]
    # two-phase: literal suffixes first (an exact dental match always
    # outranks a twin: IyAsTAm is madhyama-dvi, not the IyAstAm twin),
    # then z/s + dental twins
    _atm_cands: list = []
    for (_suf, _pur, _vac) in _ASI_ATM:
        _atm_cands.append((_suf, _pur, _vac, True))
    for (_suf, _pur, _vac) in _ASI_ATM:
        # z/s twins (satva after i, dental elsewhere: vedizI- vs dasI-)
        # plus dental twins (zwutva: IDvam/IQvam, iDve/iQve, IzWAH)
        _twins = {_suf.replace("z", "s"), _suf.replace("s", "z")}
        _twins |= _dent_variants(_suf)
        for _base in list(_twins):
            _twins |= {_base.replace("z", "s"), _base.replace("s", "z")}
        for _zsuf in sorted(_twins, key=lambda s: (len(s), s), reverse=True):
            if _zsuf != _suf:
                _atm_cands.append((_zsuf, _pur, _vac, False))
    for (_zsuf, _pur, _vac, _lit) in _atm_cands:
        if word.endswith(_zsuf) and len(word) > len(_zsuf) + 2:
            _stem = word[:-len(_zsuf)]
            _seen2, _front = set(), [_stem]
            _hit = None
            _hit_base = None
            _bfsextra: list = []
            while _front:
                _b = _front.pop(0)
                if _b in _seen2:
                    continue
                _seen2.add(_b)
                _bvars = [_b]
                if _b.endswith(("i", "I")) and len(_b) > 1:
                    _bvars.append(_b[:-1])  # sew-iT / thematic
                if _b.endswith(("aya", "Aya")) and len(_b) > 4:
                    _bvars.append(_b[:-3])  # Rejanta -aya-
                elif _b.endswith(("ay", "Ay")) and len(_b) > 3:
                    _bvars.append(_b[:-2])
                _mstrip = _deM(_b)
                if _mstrip != _b and _mstrip not in _bvars:
                    _bvars.append(_mstrip)  # M-epenthesis (titAMs)
                for _c in _bvars:
                    for (_rc, _rm, _rv) in _lookup_all(_c):
                        if _hit is None:
                            _hit = (_rc, _rm, _rv)
                            _hit_base = _c
                        elif _rc != _hit[0] and _rc not in \
                                [h[0] for h in _bfsextra]:
                            _bfsextra.append((_rc, _rm, "exact", None))
                if _b.endswith(("s", "z")) and len(_b) > 1:
                    _front.append(_b[:-1])
                # queue stripped variants for deeper peeling (tAnayizIzwa:
                # tAnayiz -> tAnay -> tAn -> tan)
                for _bv in _bvars[1:]:
                    if _bv not in _seen2 and _bv not in _front:
                        _front.append(_bv)
            _atm_hits: list = []
            if _hit is not None:
                _atm_hits.append((_hit[0], _hit[1], "exact", None))
                # graded alternates anywhere in the peel (devayizIzwa hits
                # divi early via devayi but div via dev hides deeper)
                for (_rc, _rm, _rv, _sd) in _bfsextra:
                    if _rc != _hit[0] and _rc not in \
                            [h[0] for h in _atm_hits]:
                        _atm_hits.append((_rc, _rm, "exact", None))
                # graded alternates at the primary base (rod -> rud + ruD)
                for (_rc, _rm, _rv) in _lookup_all(_hit_base):
                    if _rc != _hit[0] and _rc not in \
                            [h[0] for h in _atm_hits]:
                        _atm_hits.append((_rc, _rm, "exact", None))
            # secondary stems (san/nich/yang benedictives: buBUzizwa,
            # boBUyizIzwa <- BU): reversals over every BFS-visited
            # base, not just the raw stem (boBUyiz -> boBUy -> BU)
            _bfsbases = list(_seen2)
            if _stem.endswith(("i", "I")) and len(_stem) > 1 and \
                    _stem[:-1] not in _bfsbases:
                _bfsbases.append(_stem[:-1])
            for _c in _bfsbases:
                for _ab in _abhyasa_reverse(_c):
                    _acc_hits(_atm_hits, [_ab], "abhyasa", None)
                for _yl in _yanluk_reverse(_c):
                    _acc_hits(_atm_hits, [_yl], "yanluk", None)
                for _sn in _san_reverse(_c):
                    _acc_hits(_atm_hits, [_sn], "san", "sannanta")
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
    _LUN_ENDS = ["It", "TAm", "uH", "IH", "oH", "Tam", "ta", "izam", "Ava",
                 "Ama", "t", "d", "tAm", "an", "am", "Am", "Im", "Um", "va",
                 "ma", "s", "a", "tam", "ad", "wam", "Id", "H", "sva", "sma"]
    # Atmanepada aorist twins (gam Atm: agAMsTAm, agAMsizwa...)
    _LUN_ATM = ["zwA", "zwa", "zuH", "wAm", "zWAH", "zWam", "Dvam", "Qvam",
                "zi", "zvahi", "zmahi", "AtAm", "TAm", "WAm", "swa"]
    _LUN_SLOTS = {
        "It": [("prathama", "eka", "parasmaipada")],
        "TAm": [("prathama", "dvi", "parasmaipada")],
        "uH": [("prathama", "bahu", "parasmaipada")],
        "IH": [("madhyama", "eka", "parasmaipada")],
        "oH": [("madhyama", "dvi", "parasmaipada")],
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
        "Qvam": [("madhyama", "bahu", "Atmanepada")],
        "zi": [("uttama", "eka", "Atmanepada")],
        "zvahi": [("uttama", "dvi", "Atmanepada")],
        "zmahi": [("uttama", "bahu", "Atmanepada")],
        "AtAm": [("prathama", "dvi", "Atmanepada")],
        "TAm": [("madhyama", "dvi", "Atmanepada")],
        "WAm": [("madhyama", "dvi", "Atmanepada")],
        "swa": [("madhyama", "bahu", "parasmaipada")],
    }
    if word[:1] in ("a", "A", "E", "O") and len(word) > 3:
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
                if _stem[:1] in ("E", "O") and len(_stem) > 2:
                    # fused augment (a + eD -> ED): restore the root vowel
                    _frontier.append(("e" if _stem[:1] == "E" else "o")
                                     + _stem[1:])
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
                        for (_rc, _rm, _rv) in _lookup_all(_c):
                            if _rc not in [x[0] for x in _hits]:
                                _hits.append((_rc, _rm, _rv))
                    # secondary stems in the aorist (san/nich reduplicated
                    # stems: buBUzizwa <- BU + sannanta): try reversals
                    for _c in _cands:
                        for _ab in _abhyasa_reverse(_c):
                            _acc_hits(_hits, [_ab], "abhyasa")
                        for _yl in _yanluk_reverse(_c):
                            _acc_hits(_hits, [_yl], "yanluk")
                        for _sn in _san_reverse(_c):
                            _acc_hits(_hits, [_sn], "san")
                    # queue stripped forms for deeper peeling (sic-s/z,
                    # iT, thematic, reduplicated -v-, aorist -t-, Rejanta -aya-,
                    # M-epenthesis)
                    for _sfx in ("s", "z", "i", "I", "a", "A", "v", "t", "T"):
                        if _b.endswith(_sfx) and len(_b) > 2 and \
                                _b[:-1] not in _seen_bases:
                            _frontier.append(_b[:-1])
                    _mstrip = _deM(_b)
                    if _mstrip != _b and _mstrip not in _seen_bases:
                        _frontier.append(_mstrip)
                    if _b.endswith(("aya", "Aya")) and len(_b) > 4 and \
                            _b[:-3] not in _seen_bases:
                        _frontier.append(_b[:-3])
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
                        if _via in ("abhyasa", "san", "infix", "nu", "na"):
                            # reduplicated/infixed/secondary stems fill
                            # yangluk/class-7/san laN slots in the data
                            # (aboBavIt, rundDAm, abuBUzat are also plang):
                            # the same sic-looking formation doubles as laN
                            _d2 = {"kind": "tinanta", "purusha": _pur,
                                   "vacana": _vac, "pada": _pada,
                                   "prayoga": "kartari", "lakara": "laN",
                                   "confidence": 0.65, "ending": _suf,
                                   "note": f"root via {_via} from stem "
                                   f"'{_stem}' (laN-twin of aorist shape)"}
                            _d2.update(_root_details(_m))
                            _d2["pada"] = _pada
                            if upasarga:
                                _d2["upasarga"] = upasarga
                                _d2["confidence"] = max(
                                    0.1, _d2["confidence"] - 0.1)
                            out.append(_d2)
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
            _lit_hits: list = []
            if _core in ("ah", "Ah"):
                # brU perfect suppletion (Aha <- brU, 2.4.53): stem ah
                for (_rc, _rm, _rv) in _lookup_all("brU"):
                    _lit_hits.append((_rc, _rm, "suppletion", None))
            for (_rc, _rm, _rv) in _lookup_all(_core):
                _lit_hits.append((_rc, _rm, _rv, None))
            if not _lit_hits:
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
                        for (_rc, _rm, _rv) in _lookup_all(_cand):
                            if _rc not in [h[0] for h in _lit_hits]:
                                _lit_hits.append(
                                    (_rc, _rm, "samprasarana", None))
                        if _lit_hits:
                            break
            if not _lit_hits:
                _acc_hits(_lit_hits, _abhyasa_reverse(_core), "abhyasa",
                          None)
            if not _lit_hits and _core.endswith("v"):
                # -va- augment stems (baBUva): strip v, retry abhyasa
                _acc_hits(_lit_hits, _abhyasa_reverse(_core[:-1]),
                          "abhyasa", None)
            if not _lit_hits:
                # secondary perfect stems (san/nich reduplication)
                for _sn in _san_reverse(_core):
                    _acc_hits(_lit_hits, [_sn], "san", "sannanta")
            for (_rt, _m, _via, _sd) in _lit_hits:
                _emit(_rt, _m, "liw", _pur, _vac, _via, 0.7, _core,
                      _sanadi=_sd)
            if _lit_hits:
                break
    # periphrastic perfect (stem + Am + auxiliary perfect: buBUzAYcakAra
    # <- BU + sannanta, ditsAYcakre <- dA): split the auxiliary, analyse
    # the stem side for the lexical root (aux table built from the engine)
    _ensure_peri_aux()
    for _aux, _apur, _avac, _apada in _PERI_AUX:
        if word.endswith(_aux) and len(word) > len(_aux) + 3:
            _pre = word[:-len(_aux)]
            # periphrastic connector Am/AY (buBUzAmAsa, buBUzAYcakAra;
            # short stems: eD + AY + cakre needs pre len 4, not 5)
            if not (_pre.endswith("Am") or _pre.endswith("AY")) or len(_pre) < 4:
                continue
            _stem = _pre[:-2]
            _lex = [_stem]
            if _stem.endswith(("i", "I", "a", "A")) and len(_stem) > 1:
                _lex.append(_stem[:-1])  # sew-iT / thematic
            if _stem.endswith(("aya", "Aya")) and len(_stem) > 4:
                _lex.append(_stem[:-3])  # Rejanta -aya- (tAnay)
            elif _stem.endswith(("ay", "Ay")) and len(_stem) > 3:
                _lex.append(_stem[:-2])
            _preadings: list = []
            for _c in _lex:
                for (_rc, _rm, _rv) in _lookup_all(_c):
                    if _rc not in [r[0] for r in _preadings]:
                        _preadings.append((_rc, _rm, _rv or "exact"))
                _ablista: list = []
                for _ab in _abhyasa_reverse(_c):
                    _acc_hits(_preadings, [_ab], "abhyasa")
                    _ablista.append(_ab)
                for _yl in _yanluk_reverse(_c):
                    _acc_hits(_preadings, [_yl], "yanluk")
                _snlista: list = []
                for _sn in _san_reverse(_c):
                    _acc_hits(_preadings, [_sn], "san")
                    _snlista.append(_sn)
                # composed reversals (cicCits <- Cid + san: abhyasa gives
                # cCits whose san-mid cid still hides Cid)
                for _ab in _ablista:
                    for _sn2 in _san_reverse(_ab):
                        _acc_hits(_preadings, [_sn2], "san")
                for _sn in _snlista:
                    for _ab2 in _abhyasa_reverse(_sn):
                        _acc_hits(_preadings, [_ab2], "abhyasa")
            _readings = []
            if _preadings:
                _readings.extend(_preadings)
            # every slot sharing this aux string counts (cakAra is both
            # prathama eka and uttama eka): cross product, then stop —
            # longest aux wins, but all its slots emit
            _aux_slots = [(p, v, pa) for (a, p, v, pa) in _PERI_AUX
                          if a == _aux]
            for (_rt, _m, _via) in _readings:
                for (_apur2, _avac2, _apada2) in _aux_slots:
                    _d = {"kind": "tinanta", "purusha": _apur2,
                          "vacana": _avac2, "pada": _apada2,
                          "prayoga": "kartari", "lakara": "liw",
                          "confidence": 0.7, "ending": _aux,
                          "note": f"periphrastic liw: root via {_via} "
                          f"from stem '{_stem}' + aux '{_aux}'"}
                    _d.update(_root_details(_m))
                    if upasarga:
                        _d["upasarga"] = upasarga
                        _d["confidence"] = max(0.1, _d["confidence"] - 0.1)
                    out.append(_d)
            if _preadings:
                break
    return out


_PERI_AUX: list = []


def _ensure_peri_aux() -> None:
    """Build (auxform, purusha, vacana, pada) table from engine perfects.

    One aux string can serve several slots (cakAra is both prathama eka
    and uttama eka of kf): keep every slot so periphrastic search emits
    the full collision set instead of the first slot only.
    """
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
                        _k = (_f, _pur, _vac, _pada)
                        if _k not in _seen:
                            _seen.add(_k)
                            _PERI_AUX.append(_k)
                        # retroflex aux twins (cakfQve <- cakfDve, zwutva):
                        # same slots, retroflex surface
                        for _twin in _dent_variants(_f):
                            if _twin != _f:
                                _kt = (_twin, _pur, _vac, _pada)
                                if _kt not in _seen:
                                    _seen.add(_kt)
                                    _PERI_AUX.append(_kt)
    # data-attested aux outside engine liT inventory (buBUzAmAhe is
    # san_yak alit utt eka): Ahe fills Ase's slots
    for (_f, _pur, _vac, _pada) in list(_PERI_AUX):
        if _f == "Ase":
            _kt = ("Ahe", _pur, _vac, _pada)
            if _kt not in _seen:
                _seen.add(_kt)
                _PERI_AUX.append(_kt)
    _PERI_AUX.sort(key=lambda t: -len(t[0]))


_TIN_ENG = None
_VERIFY_CACHE: Dict[tuple, bool] = {}


def _verify_tin(word: str, dhatu: str, lak: str, pur: str, vac: str,
                prayoga: str, sanadi, dhatu_id, upasarga) -> bool:
    """Forward-verify a tinanta reading with the generative engine."""
    global _TIN_ENG
    _ck = (word, dhatu, lak, pur, vac, prayoga, sanadi, dhatu_id, upasarga)
    if _ck in _VERIFY_CACHE:
        return _VERIFY_CACHE[_ck]
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
            _VERIFY_CACHE[_ck] = True
            return True
        # t/d voicing twins (BavatAd <- BavatAt): the engine emits -t, so
        # confirm a -d surface against its -t twin (same formation)
        if word.endswith("d"):
            _r = _gen(word[:-1] + "t")
            _VERIFY_CACHE[_ck] = _r
            return _r
        _VERIFY_CACHE[_ck] = False
        return False
    except Exception:
        return True  # engine gap: never punish on errors


def _tinanta_analyze(word: str, upasarga: str | None = None) -> List[dict]:
    out: List[dict] = []
    for _ww in [word] + _stem_desandhi(word):
            out += _infix_reverse(_ww, upasarga)
            for _table, _pada in ((_TIN_P, "parasmaipada"), (_TIN_A, "Atmanepada")):
                for (_end, _lak, _pur, _vac) in _table:
                    if not _ww.endswith(_end) or len(_ww) <= len(_end):
                        continue
                    _core = _ww[:-len(_end)] if _end else _ww
                    _aug = (_lak == "laN")
                    # Collect hits across ALL stem candidates (no early break):
                    # an early stripped variant may hit an incidental root while a
                    # later one carries the true analysis (abuBUzya: 'buBUzy' hits
                    # BUz via abhyasa before 'buBUz' yields the BU san twin).
                    # Emission stays in candidate order so stripped-exact readings
                    # keep their ranking; flat-level dedup collapses repeats.
                    _found: List[tuple] = []  # (via_extra, hit, extra_hits, multi)
                    for _cand in _tin_candidates(_core, _lak, _aug):
                        _hit = None
                        _via_extra = ""
                        _multi = None
                        _extra_hits: List[tuple] = []
                        # irregular presents first (multi-root: yacCa <- yam + dA)
                        _irr = _irreg_pres(_cand)
                        if _irr is not None:
                            _found.append(("", None, [], _irr))
                            continue
                        _hit = _lookup_root(_cand)
                        if _hit is not None:
                            # also keep abhyasa twin (dadati is dad + dA at once)
                            for _ab in _abhyasa_reverse(_cand):
                                _acc_hits(_extra_hits, [_ab], "abhyasa")
                            for _yl in _yanluk_reverse(_cand):
                                _acc_hits(_extra_hits, [_yl], "yanluk")
                            # also keep desiderative twin (buBUzati is BUz + BU:
                            # exact lookup finds only the san-shaped root BUz)
                            for _sn in _san_reverse(_cand):
                                _acc_hits(_extra_hits, [_sn], "san")
                            # graded alternates of the primary itself
                            # (rod -> rud + ruD)
                            for (_rc, _rm, _rv) in _lookup_all(_cand)[1:]:
                                if _rc != _hit[0] and _rc not in \
                                        [h[0] for h in _extra_hits]:
                                    _extra_hits.append((_rc, _rm, _rv))
                            _found.append(("", _hit, _extra_hits, None))
                            continue
                        # class-3 reduplicated stems (dadA/juhu/biBar + ti)
                        for _ab in _abhyasa_reverse(_cand):
                            _acc_hits(_extra_hits, [_ab], "abhyasa")
                        for _yl in _yanluk_reverse(_cand):
                            _acc_hits(_extra_hits, [_yl], "yanluk")
                        if _extra_hits:
                            _rt0, _m0, _vx0 = _extra_hits.pop(0)
                            _hit = (_rt0, _m0, "abhyasa")
                            _via_extra = "abhyasa"
                        if _hit is not None:
                            # primary came via abhyasa (buBUz -> BUz): san twins
                            # (buBUz -> BU) still count as extra readings
                            for _sn in _san_reverse(_cand):
                                _acc_hits(_extra_hits, [_sn], "san")
                            _found.append((_via_extra, _hit, _extra_hits, None))
                            continue
                        # desiderative stems (ditsa/vividiza + ti)
                        for _sn in _san_reverse(_cand):
                            _acc_hits(_extra_hits, [_sn], "san")
                        if _extra_hits:
                            _rt0, _m0, _vx0 = _extra_hits.pop(0)
                            _hit = (_rt0, _m0, "san")
                            _via_extra = "san"
                        if _hit is not None:
                            # primary came via san: abhyasa twins still count
                            for _ab in _abhyasa_reverse(_cand):
                                _acc_hits(_extra_hits, [_ab], "abhyasa")
                            for _yl in _yanluk_reverse(_cand):
                                _acc_hits(_extra_hits, [_yl], "yanluk")
                            _found.append((_via_extra, _hit, _extra_hits, None))
                            continue
                        # viDiliN e-grade of A-final roots (det <- dA: the ending
                        # table segments d+et, swallowing the stem vowel, while
                        # exact lookup finds only the e-final root deN)
                        if _lak == "viDiliN" and _cand.endswith("e"):
                            _hit = _lookup_root(_cand[:-1] + "A")
                            if _hit is not None:
                                _found.append(("egrade", _hit, [], None))
                                continue
                        if (_lak == "viDiliN" and len(_cand) == 1
                                and _cand not in SLP1_VOWELS):
                            _hit = _lookup_root(_cand + "A")
                            if _hit is not None:
                                _found.append(("egrade", _hit, [], None))
                                continue
                    _multi = None
                    _hit = None
                    _via_extra = ""
                    _extra_hits = []
                    _emit_queue: List[tuple] = []
                    for (_vx, _h, _eh, _mu) in _found:
                        if _mu is not None:
                            _multi = _mu  # last multi wins below (same slot anyway)
                        if _h is not None:
                            _emit_queue.append((_vx, _h, _eh))
                    # classical laN needs the a- augment (adadat, not *dadan)
                    _no_aug = _aug and _core[:1] not in ("a", "A")
                    # liT always reduplicates (Asa-type a-initial stems excepted):
                    # plain grade-hits on bare-a endings (rAma) are nouns, not verbs.
                    # (Unresolved fallbacks still emit below.)
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
                            if not _verify_tin(_ww, _c, _lak, _pur, _vac, "kartari",
                                               None, _ids[0], upasarga):
                                _d["confidence"] = max(0.1, _d["confidence"] * 0.5)
                                _d["note"] += "; unverified"
                            out.append(_d)
                    _liw_plain_base = (_lak == "liw" and _multi is None
                                       and _core[:1] not in ("a", "A"))
                    def _emit_extra(_ert, _em, _evia) -> None:
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
                        _eok = _verify_tin(_ww, _ert, _lak, _pur, _vac,
                                           "kartari",
                                           "sannanta" if _evia == "san" else None,
                                           _eids[0], upasarga)
                        if not _eok:
                            _ed["confidence"] = max(0.1, _ed["confidence"] * 0.5)
                            _ed["note"] += "; unverified"
                        out.append(_ed)

                    _emitted_primary = False
                    for (_via_extra, _hit, _extra_hits) in _emit_queue:
                        _plain = _liw_plain_base and not _via_extra
                        if _plain:
                            # liw plain-grade hits are noun-coincidences (rAma),
                            # but reduplication-derived twins (dad -> dA) are
                            # genuine verbs
                            for (_ert, _em, _evia) in _extra_hits:
                                _emit_extra(_ert, _em, _evia)
                            continue
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
                        # regenerates the _ww (kills e.g. augmentless-laN ghosts);
                        # Atmanepada forms fall back to karmani before demotion
                        _ids = _d.get("ids") or [None]
                        _ok = _verify_tin(_ww, _rt, _lak, _pur, _vac, "kartari",
                                          "sannanta" if _via == "san" else None,
                                          _ids[0], upasarga)
                        if not _ok and _pada == "Atmanepada":
                            _ok = _verify_tin(_ww, _rt, _lak, _pur, _vac, "karmani",
                                              "sannanta" if _via == "san" else None,
                                              _ids[0], upasarga)
                            if _ok:
                                _d["prayoga"] = "karmani"
                                _d["note"] = (_d.get("note", "") + "; karmani").strip("; ")
                        if not _ok:
                            _d["confidence"] = max(0.1, _d["confidence"] * 0.5)
                            _d["note"] = (_d.get("note", "") + "; unverified").strip("; ")
                        out.append(_d)
                        _emitted_primary = True
                        for (_ert, _em, _evia) in _extra_hits:
                            _emit_extra(_ert, _em, _evia)
                    if not _emitted_primary:
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

def _prefix_splits(word: str) -> List[tuple]:
    """Longest-first (upasarga, rest) splits incl. sandhi rules.

    AN (AN) surfaces as A before vowels but Am/An before consonants
    (AmbuBUz <- AN + buBUz): the nasal belongs to the prefix, so the
    rest drops it. sam + consonant -> saM likewise.
    Prefix-stem sandhi: yaN (vi + ati -> vyati: i/u + vowel -> y/v +
    vowel) and guNa (A + i/u/e/o -> E/O) fuse the boundary, so desandhied
    rests are offered alongside literal splits.
    """
    from .subanta import SLP1_VOWELS as _V
    cands = []
    if len(word) > 4 and word[:2] in ("Am", "An") and word[2] not in _V:
        cands.append(("AN", word[2:]))
    if len(word) > 4 and word[:2] in ("am", "an") and word[2] not in _V:
        # inner-AN with shortened vowel (aDyan- <- aDi + AN + ...):
        # the nasal still marks the prefix boundary
        cands.append(("AN", word[2:]))
    if len(word) > 5 and word[:3] == "saM" and word[3] not in _V:
        # sam + consonant -> saM (anusvara): the nasal is the prefix
        # coda (saMboBavitA <- sam + boBavitA)
        cands.append(("sam", word[3:]))
    for _p in sorted(_UPASARGAS, key=lambda s: (len(s), s), reverse=True):
        if word.startswith(_p) and len(word) - len(_p) >= 3:
            cands.append((_p, word[len(_p):]))
            # no break: nirX can be nir + X or ni + rX (ruruts- stems);
            # pratiX can be prati + X or pra + tiX. Garbage rests fail
            # lookup; dedup collapses repeats.
    # augment fusion: prefix + laN/luN/lfN augment a- fuse
    # (pra + aBavata -> prABavata: a + a -> A; parA + a -> parA,
    # invisible). The rest restores the augment vowel for table matching.
    for _p in sorted(_UPASARGAS, key=lambda s: (len(s), s), reverse=True):
        if _p.endswith("A"):
            _fused = _p
        elif _p.endswith("a"):
            _fused = _p[:-1] + "A"
        else:
            _fused = _p + "A"
        if len(word) <= len(_fused) + 2:
            continue
        if word.startswith(_fused):
            _rest = "a" + word[len(_fused):]
            if all(_r != _rest for (_, _r) in cands):
                cands.append((_p, _rest))
            break
    # bare-A split is ambiguous A/AN (data writes bare A for AN +
    # consonant too): analyse the rest under both chains
    for (_p, _rest) in list(cands):
        if _p == "A" and ("AN", _rest) not in cands:
            cands.append(("AN", _rest))
    # prefix-coda sandhi (mirror of _rev_prefix_sandhi, which handles
    # remainder-onset): ud + piY... -> utpiY... (d devoices before
    # voiceless), dus + pra -> duzpra... (s voices before voiced).
    # The coda belongs to the prefix; the rest starts after it.
    _CADA_TWIN = {"d": ("t",), "b": ("p",), "g": ("k",), "j": ("c",),
                  "D": ("T",), "B": ("P",), "G": ("K",), "J": ("C",),
                  "s": ("z", "S")}
    for _p in _UPASARGAS:
        if not _p or _p[-1] not in _CADA_TWIN or len(word) <= len(_p) + 2:
            continue
        if word[:len(_p) - 1] == _p[:-1] and \
                word[len(_p) - 1] in _CADA_TWIN[_p[-1]]:
            _rest = word[len(_p):]
            if _rest and all(_r != _rest for (_, _r) in cands):
                cands.append((_p, _rest))
    # y/v + vowel (vyati <- vi + ati). Only when no literal split fired
    # on the same span (literal 'vi' never matches surface 'vya').
    for _p in _UPASARGAS:
        if _p[-1] in ("i", "I", "u", "U") and len(word) > len(_p) + 2:
            _glide = "y" if _p[-1] in ("i", "I") else "v"
            if word.startswith(_p[:-1] + _glide) and word[len(_p)] in _V:
                _rest = word[len(_p):]
                if all(_r != _rest for (_, _r) in cands):
                    cands.append((_p, _rest))
    # guNa boundary: A-final prefix + i/u/e/o -> E/O. Rest restores the
    # stem-initial vowel (E <- A + i/e, O <- A + u/o).
    if word[:1] in ("E", "O") and len(word) > 4:
        _vows = ("i", "e") if word[:1] == "E" else ("u", "o")
        for _p in [p for p in _UPASARGAS if p.endswith("A")]:
            for _vw in _vows:
                _rest = _vw + word[1:]
                if len(_rest) >= 3 and \
                        all(_r != _rest for (_, _r) in cands):
                    cands.append((_p, _rest))
    return cands


def _chain(pre: str | None, p: str) -> str:
    return p if not pre else pre + ";" + p


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

def _subanta_flat(word: str, limit: int = 50) -> List[dict]:
    """Flat subanta readings (internal; public subanta_search groups these)."""
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
    return out[:limit] if limit is not None else out


def _group_subanta(flat: List[dict]) -> List[dict]:
    """One entry per stem with a readings list (linga/vibhakti/vacana)."""
    _groups: Dict[tuple, dict] = {}
    for _a in flat:
        _k = (_a.get("stem"),)
        _g = _groups.get(_k)
        if _g is None:
            _g = {"kind": "subanta", "stem": _a.get("stem"), "readings": [],
                  "_conf": 0.0}
            _groups[_k] = _g
        _g["readings"].append({"linga": _a.get("linga"),
                               "vibhakti": _a.get("vibhakti"),
                               "vacana": _a.get("vacana"),
                               "confidence": _a.get("confidence", 0.0),
                               "lexicon": _a.get("lexicon", False)})
        _g["_conf"] = max(_g["_conf"], _a.get("confidence", 0.0))
    out = list(_groups.values())
    for _g in out:
        _g["readings"].sort(key=lambda d: d["confidence"], reverse=True)
        _g["confidence"] = _g.pop("_conf")
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out


def subanta_search(word: str, limit: int | None = None) -> List[dict]:
    """Subanta-only search: one entry per stem with a readings list."""
    return (_group_subanta(_subanta_flat(word, limit=500))[:limit]
            if limit is not None
            else _group_subanta(_subanta_flat(word, limit=500)))


def _krdanta_flat(word: str, limit: int = 50,
                  with_upasarga: bool = True) -> List[dict]:
    """Flat krdanta readings (internal; public krdanta_search groups these)."""
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

    def _level(_w: str, _ch: str | None, _pen: float) -> list:
        """All stem + word-level krdanta analyses of one word-slice."""
        def _penal(_c: float) -> float:
            return max(0.1, _c - _pen)

        _stems = []
        for _a in _subanta_flat(_w, limit=50):
            _stems.append((_a.get("lexicon", False),
                           _a["stem"], _a["linga"], _a["vibhakti"], _a["vacana"]))
        if _w.endswith("d") and len(_w) > 3:
            # padAnta voicing twin (BUtavad <- BUtavat, baBUvad, Bavad):
            # the engine emits -t, so recover stems from the -t surface
            for _a in _subanta_flat(_w[:-1] + "t", limit=50):
                _stems.append((_a.get("lexicon", False),
                               _a["stem"], _a["linga"], _a["vibhakti"],
                               _a["vacana"]))
        # indeclinable krdanta forms ride masculine stems (BavitavyA <- Bavitavya)
        _more = []
        for (_lex, _st, _li, _vib, _vac) in _stems:
            if _st.endswith("A") and len(_st) > 2:
                _more.append((False, _st[:-1] + "a", _li, _vib, _vac))
            if _st.endswith("ntI") and len(_st) > 3:
                _more.append((False, _st[:-3] + "t", _li, _vib, _vac))
            if _st.endswith("vatI") and len(_st) > 4:
                _more.append((False, _st[:-1], _li, _vib, _vac))
        _stems += _more
        _stems.sort(key=lambda t: (not t[0], t[1]))
        _from_stems(_stems, penalty=_pen, upasarga=_ch)
        # feminine krdanta forms ride masculine stems (BavitavyA <- Bavitavya,
        # BavantI <- Bavat, BUtavatI <- BUtavat, cakruzI <- cakfuz weak,
        # BavizyatI <- Bavizyat): recover the masculine word, analyse it,
        # keep the feminine slot
        _mw = None
        if _w.endswith("A") and len(_w) > 2:
            _mw = _w[:-1] + "a"
        elif _w.endswith("ntI") and len(_w) > 3:
            _mw = _w[:-3] + "t"
        elif _w.endswith("vatI") and len(_w) > 4:
            _mw = _w[:-1]
        elif _w.endswith("trI") and len(_w) > 3:
            _mw = _w[:-3] + "tf"
        elif _w.endswith("tI") and len(_w) > 3:
            _mw = _w[:-1]
        elif _w.endswith("zI") and len(_w) > 2:
            _mw = _w[:-1]
        if _mw:
            for _k in _krdanta_from_stem(_mw, "strI", 1, "eka"):
                _kk = (_k.get("dhatu"), _k["pratyaya"], _mw, "strI", 1,
                       "eka", _ch)
                if _kk in seen:
                    continue
                seen.add(_kk)
                _k = dict(_k)
                _k["confidence"] = _penal(_k.get("confidence", 0.5))
                if _ch:
                    _k["upasarga"] = _ch
                out.append(_k)
        # ktin word-level recovery (BUtiH/buBUzwiH): short-i feminines
        # have no subanta paradigm, so analyse the nominative directly
        # (stem-level branch in _krdanta_from_stem covers forms that inflect)
        if (_w.endswith("tiH") or _w.endswith("wiH")) and len(_w) > 3:
            _wktb = [_w[:-3]]
            if _w[:-3].endswith("A") and len(_w[:-3]) > 1:
                _wktb.append(_w[:-4] + "Ava")
            _wkhits = []
            _seenkt = set()
            for _wkb in _wktb:
                for (_rt, _m, _via) in _krd_hits(_wkb):
                    if _rt not in _seenkt:
                        _seenkt.add(_rt)
                        _wkhits.append((_rt, _m, _via))
            for (_rt, _m, _via) in _wkhits:
                _kk = (_rt, "ktin", _w[:-3] + "ti", "strI", 1, "eka", _ch)
                if _kk in seen:
                    continue
                seen.add(_kk)
                _k = {"kind": "krdanta", "pratyaya": "ktin",
                      "stem": _w[:-3] + "ti", "linga": "strI",
                      "vibhakti": 1, "vacana": "eka",
                      "confidence": _penal(0.65),
                      "note": f"root via {_via}",
                      **_root_details(_m)}
                if _ch:
                    _k["upasarga"] = _ch
                out.append(_k)
        # bare-stem word-level recovery for consonant-final krdantas whose
        # stems never surface in subanta (u: buBUzu, gsnu: BUzRu)
        if _w.endswith("zu") and len(_w) > 3:
            _uw = _w[:-1] if not _w.endswith("uzu") else _w[:-2]
            _uhits: list = []
            for _ab in _abhyasa_reverse(_uw):
                _acc_hits(_uhits, [_ab], "abhyasa")
            for _yl in _yanluk_reverse(_uw):
                _acc_hits(_uhits, [_yl], "yanluk")
            for _sn in _san_reverse(_uw):
                _acc_hits(_uhits, [_sn], "san")
            for (_ah0, _ahm, _ahv) in _uhits:
                _kk = (_ah0, "u", _uw + "u", None, None, None, _ch)
                if _kk not in seen:
                    seen.add(_kk)
                    _k = {"kind": "krdanta", "pratyaya": "u",
                          "stem": _uw + "u", "linga": None,
                          "vibhakti": None, "vacana": None,
                          "confidence": _penal(0.6),
                          "note": f"root via {_ahv}",
                          **_root_details(_ahm)}
                    if _ch:
                        _k["upasarga"] = _ch
                    out.append(_k)
        if _w.endswith(("Ru", "RuH")) and len(_w) > 4:
            _stemw = _w[:-1] if _w.endswith("RuH") else _w
            _gb = _stemw[:-2]
            if _gb.endswith("z"):
                _gb = _gb[:-1] + "s"
            if _gb.endswith("s") and len(_gb) > 2:
                for (_rt, _m, _via) in _krd_hits(_gb[:-1]):
                    _kk = (_rt, "gsnu", _stemw, None, None, None, _ch)
                    if _kk in seen:
                        continue
                    seen.add(_kk)
                    _k = {"kind": "krdanta", "pratyaya": "gsnu",
                          "stem": _stemw, "linga": None,
                          "vibhakti": None, "vacana": None,
                          "confidence": _penal(0.65),
                          "note": f"root via {_via}",
                          **_root_details(_m)}
                    if _ch:
                        _k["upasarga"] = _ch
                    out.append(_k)
        # indeclinable krdantas have no sup stem: tumun (-tum), ktvA (-tvA),
        # Ramul (-am, low confidence: -am is usually the accusative ending)
        for _suf, _prat, _conf in (("tum", "tumun", 0.85),
                                   ("tvA", "ktvA", 0.85),
                                   ("am", "Ramul", 0.5)):
            if _w.endswith(_suf) and len(_w) > len(_suf) + 1:
                _core = _w[:-len(_suf)]
                _cands = [_core]
                if _core.endswith("i") and len(_core) > 1:
                    _cands.append(_core[:-1])  # sew iT (Bavi -> Bav)
                    if _core.endswith("it") and len(_core) > 2:
                        _cands.append(_core[:-2])  # buried iT (trumpit -> trump)
                if _prat == "ktvA" and _core[:1] in ("u", "i") \
                        and len(_core) > 1:
                    # samprasarana absolutives (uktvA <- vac): va/ya + cutva
                    _rest = _core[1:]
                    _cut = _decutva(_rest)
                    _cands.append(("va" if _core[:1] == "u" else "ya") + _cut)
                for _c in _cands:
                    _hits = _krd_hits(_c)
                    if _hits:
                        break
                if _hits:
                    for (_rt, _m, _via) in _hits:
                        _kk = (_rt, _prat, _w, "avyaya", None, None, _ch)
                        if _kk in seen:
                            continue
                        seen.add(_kk)
                        _k = {"kind": "krdanta", "pratyaya": _prat,
                              "stem": _w, "linga": "avyaya",
                              "vibhakti": None, "vacana": None,
                              "confidence": _penal(_conf) if _via not in
                              ("abhyasa", "san") else max(
                                  0.1, _penal(_conf) - 0.1),
                              "note": f"root via {_via} from '{_core}'",
                              **_root_details(_m)}
                        if _ch:
                            _k["upasarga"] = _ch
                        out.append(_k)
                    break
        # periphrastic kvasu (stem + Am/AY + kvasu-aux: buBUzAmbaBUvAn
        # <- BU + sannanta): split the auxiliary, reverse the stem side
        for _aux in sorted(_KVASU_AUX, key=len, reverse=True):
            if _w.endswith(_aux) and len(_w) > len(_aux) + 3:
                _pre = _w[:-len(_aux)]
                if not (_pre.endswith("Am") or _pre.endswith("AY")) \
                        or len(_pre) < 4:
                    continue
                _pstem = _pre[:-2]
                _plex = [_pstem]
                if _pstem.endswith(("i", "I", "a", "A")) and len(_pstem) > 1:
                    _plex.append(_pstem[:-1])
                _preadings = []
                for _c in _plex:
                    for (_rt, _m, _via) in _krd_hits(_c):
                        if _rt not in [r[0] for r in _preadings]:
                            _preadings.append((_rt, _m, _via))
                for (_rt, _m, _via) in _preadings:
                    _kk = (_rt, "kvasu", _pstem + "Am" + _aux, None, None,
                           None, _ch)
                    if _kk in seen:
                        continue
                    seen.add(_kk)
                    _k = {"kind": "krdanta", "pratyaya": "kvasu",
                          "stem": _pstem + "Am" + _aux, "linga": None,
                          "vibhakti": None, "vacana": None,
                          "confidence": _penal(0.7),
                          "note": f"periphrastic kvasu: root via {_via} "
                          f"from stem '{_pstem}' + aux '{_aux}'",
                          **_root_details(_m)}
                    if _ch:
                        _k["upasarga"] = _ch
                    out.append(_k)
                if _preadings:
                    break
        # -ya absolutive: lyap needs an upasarga (prefixless reading is
        # weak — but the engine overgenerates unprefixed twins).
        # -tya- allomorph (kutya <- ku + tya) strips one more.
        if _w.endswith("ya") and len(_w) > 3:
            _lyb = [_devrddhi(_w[:-2])]
            if _w.endswith("tya") and len(_w) > 4:
                _lyb.append(_w[:-3])
            for _lb in _lyb:
                for (_rt, _m, _via) in _krd_hits(_lb):
                    if _ch:
                        _kk = (_rt, "lyap", _w, _ch)
                        _lyconf, _lynote = max(0.1, 0.75 - _pen + 0.1), \
                            f"root via {_via}"
                    else:
                        _kk = (_rt, "lyap", _w, None)
                        _lyconf, _lynote = 0.45, f"root via {_via}; prefix missing"
                    if _kk not in seen:
                        seen.add(_kk)
                        _k = {"kind": "krdanta", "pratyaya": "lyap",
                              "stem": _w, "linga": "avyaya",
                              "vibhakti": None, "vacana": None,
                              "confidence": _lyconf, "note": _lynote,
                              **_root_details(_m)}
                        if _ch:
                            _k["upasarga"] = _ch
                        out.append(_k)
        return _stems

    _level(word, None, 0.0)
    if with_upasarga:
        # prati + sTira -> pratizWira: prefix sandhi voices s->z/S and
        # retroflexes the following stop, so retry reversed variants.
        # Recursive: compounds (sam;pari) split outer-first, then inner.
        def _rec(_w: str, _pre: str | None, _depth: int) -> None:
            if _depth > 3:
                return
            for (_p, _rest) in _prefix_splits(_w):
                _ch = _chain(_pre, _p)
                _pen = 0.1 * len(_ch.split(";"))
                for _v in _rev_prefix_sandhi(_rest):
                    _vstems = _level(_v, _ch, _pen)
                    # lyap on remainder stems (feminine -yA forms differ
                    # from the remainder word itself)
                    for (_lex, _st, _li, _vib, _vac) in _vstems:
                        if _st.endswith("ya") and len(_st) > 3:
                            for (_rt, _m, _via) in _krd_hits(
                                    _devrddhi(_st[:-2])):
                                _kk = (_rt, "lyap", _st, _li, _vib, _vac,
                                       _ch)
                                if _kk in seen:
                                    continue
                                seen.add(_kk)
                                _k = {"kind": "krdanta", "pratyaya": "lyap",
                                      "stem": _st, "linga": "avyaya",
                                      "vibhakti": None, "vacana": None,
                                      "confidence": max(0.1, 0.75 - _pen),
                                      "upasarga": _ch,
                                      "note": f"root via {_via}",
                                      **_root_details(_m)}
                                out.append(_k)
                                break
                    _rec(_v, _ch, _depth + 1)
        _rec(word, None, 0)
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out[:limit] if limit is not None else out


def _group_krdanta(flat: List[dict]) -> List[dict]:
    """One entry per dhatu (+upasarga) with a readings list incl. pratyaya."""
    _groups: Dict[tuple, dict] = {}
    for _k in flat:
        _key = (_k.get("dhatu"), _k.get("upasarga"))
        _g = _groups.get(_key)
        if _g is None:
            _g = {"kind": "krdanta", "dhatu": _k.get("dhatu"),
                  "upasarga": _k.get("upasarga"), "readings": [],
                  "_conf": 0.0}
            for _f in ("ids", "dhAtu_pada", "sew", "gana"):
                if _f in _k:
                    _g[_f] = _k[_f]
            _groups[_key] = _g
        _g["readings"].append({"pratyaya": _k.get("pratyaya"),
                               "stem": _k.get("stem"),
                               "linga": _k.get("linga"),
                               "vibhakti": _k.get("vibhakti"),
                               "vacana": _k.get("vacana"),
                               "confidence": _k.get("confidence", 0.0),
                               "note": _k.get("note", "")})
        _g["_conf"] = max(_g["_conf"], _k.get("confidence", 0.0))
    out = list(_groups.values())
    for _g in out:
        _g["readings"].sort(key=lambda d: d["confidence"], reverse=True)
        _g["confidence"] = _g.pop("_conf")
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out


def krdanta_search(word: str, limit: int | None = None,
                   with_upasarga: bool = True) -> List[dict]:
    """Krdanta-only search: one entry per dhatu with a readings list."""
    _flat = _krdanta_flat(word, limit=500, with_upasarga=with_upasarga)
    _g = _group_krdanta(_flat)
    return _g[:limit] if limit is not None else _g


def _tinanta_flat(word: str, limit: int = 500,
                 with_upasarga: bool = True) -> List[dict]:
    """Flat tinanta readings (internal; public tinanta_search groups these)."""
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
        # recursive compound splitting (sam;pari + BavatI): outer split
        # first, then inner splits on the remainder; chains join with ';'
        def _rec(_w: str, _pre: str | None, _depth: int) -> None:
            if _depth > 3:
                return
            for (_p, _rest) in _prefix_splits(_w):
                _ch = _chain(_pre, _p)
                for _v in _rev_prefix_sandhi(_rest):
                    for _t in _tinanta_analyze(_v, upasarga=_ch):
                        _add(_t, _penalty=0.1 * len(_ch.split(";")))
                    _rec(_v, _ch, _depth + 1)
        _rec(word, None, 0)
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out[:limit] if limit is not None else out


def _group_tinanta(flat: List[dict]) -> List[dict]:
    """One entry per dhatu (+upasarga) with a list of lakara-readings."""
    _groups: Dict[tuple, dict] = {}
    for _t in flat:
        _key = (_t.get("dhatu"), _t.get("upasarga"))
        _g = _groups.get(_key)
        if _g is None:
            _g = {"kind": "tinanta", "dhatu": _t.get("dhatu"),
                  "upasarga": _t.get("upasarga"), "readings": [],
                  "_conf": 0.0}
            for _f in ("ids", "dhAtu_pada", "sew", "gana"):
                if _f in _t:
                    _g[_f] = _t[_f]
            _groups[_key] = _g
        _g["readings"].append({"lakara": _t.get("lakara"),
                               "purusha": _t.get("purusha"),
                               "vacana": _t.get("vacana"),
                               "pada": _t.get("pada"),
                               "prayoga": _t.get("prayoga"),
                               "sanadi": _t.get("sanadi"),
                               "ending": _t.get("ending"),
                               "confidence": _t.get("confidence", 0.0),
                               "note": _t.get("note", "")})
        _g["_conf"] = max(_g["_conf"], _t.get("confidence", 0.0))
    out = list(_groups.values())
    for _g in out:
        _g["readings"].sort(key=lambda d: d["confidence"], reverse=True)
        _g["confidence"] = _g.pop("_conf")
    out.sort(key=lambda d: d["confidence"], reverse=True)
    return out


def tinanta_search(word: str, limit: int | None = None,
                   with_upasarga: bool = True) -> List[dict]:
    """Tinanta-only search: one entry per dhatu with lakara-readings list."""
    _flat = _tinanta_flat(word, limit=500, with_upasarga=with_upasarga)
    _g = _group_tinanta(_flat)
    return _g[:limit] if limit is not None else _g


def analyze(word: str, limit: int | None = None) -> List[dict]:
    """Global search: grouped per-dhatu/per-stem entries, best first.

    Tinanta groups carry ``readings`` (lakara list), krdanta groups carry
    ``readings`` (pratyaya list), subanta groups carry ``readings``
    (vibhakti list). No truncation by default; ``limit`` slices groups.
    """
    _ensure_ready()
    word = (word or "").strip()
    if not word:
        return []
    out: List[dict] = []
    out.extend(_group_subanta(_subanta_flat(word, limit=500)))
    out.extend(_group_krdanta(_krdanta_flat(word, limit=500)))
    out.extend(_group_tinanta(_tinanta_flat(word, limit=500)))
    out.sort(key=lambda d: d.get("confidence", 0.0), reverse=True)
    return out[:limit] if limit is not None else out


def best(word: str) -> dict | None:
    """Top-ranked grouped analysis, or None."""
    _r = analyze(word, limit=1)
    return _r[0] if _r else None
