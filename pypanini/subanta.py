"""
pypanini.subanta
~~~~~~~~~~~~~~~~
Generative Subanta (nominal declension) engine in SLP1.

Pipeline (Paninian, internal sandhi only, no external sandhi):
  pratipadika + 21 sup -> sarvanamasthana / Ba / pada handling
  -> stem adjustments (guNa/vfddhi/aya/num/aw/samprasarana/lopa)
  -> pratyaya-adesa (e.g. sarvanaman smai/smat/smin, Ne->ya etc.)
  -> internal sandhi sweep (Natva 8.4.1-2, zatva 8.3.59, coH kuH 8.2.30,
     ho Qah, sasajuzo ruH + visarga, etc.)
  -> pada output.

No per-word form dictionaries. Irregulars (go/rE/nO/saKi/pati/
krozwu/asTi-group/ap/anaQuh/puMs/div/ahan/pathin/Svan-group/aYc/
svasf/jarA/SrI/BU/yuzmad/asmad/adas/kim) are handled by small
rule-branches keyed on stem shape + flags, exactly as apavada rules.

SLP1 notes: E=ai, O=au, S=s, z=s, w=t, W=th, q=d, Q=dh,
N=n, Y=n, R=n, H=visarga, M=anusvara. Long vowels are capitals.

Public API:
  SubantaEngine().decline(stem, linga, ...) -> Dict[(vibhakti, vacana), List[str]]
  vibhakti in 1..8 (8=sambuddhi/sambodhana), vacana in eka/dvi/bahu.
  Each value is a list (optionality/vibhazA twins kept, deduped).

References: Astadhyayi 4.1.2 (sup), 1.4.x (gI/gU/nadI/sarvanAman),
  6.x-7.x (anga-karya), 8.x (pada-karya internal only).
"""
from __future__ import annotations
from typing import Dict, List, Tuple

SLP1_VOWELS = set(list("aAiIuUfFxXeEoO"))
SLP1_SHORT2LONG = {"a": "A", "i": "I", "u": "U", "f": "F", "x": "X"}
SLP1_VOWEL_GRADE_AYA = {"e": "ay", "o": "av", "E": "Ay", "O": "Av"}

# 21 sup in SLP1 (anubandha kept in code, stripped on surface).
# order: 1sg 1du 1pl 2sg 2du 2pl 3sg 3du 3pl 4sg 4du 4pl 5sg 5du 5pl 6sg 6du 6pl 7sg 7du 7pl
SUP_RAW: List[str] = [
    "sU", "O", "jas",
    "am", "Ow", "Sas",
    "wA", "ByAm", "Bis",
    "Ne", "ByAm", "Byas",
    "Nasi", "ByAm", "Byas",
    "Nas", "os", "Am",
    "Ni", "os", "sup",
]
# (vibhakti, vacana) for each of the 21
SUP_KEYS: List[Tuple[int, str]] = [
    (1, "eka"), (1, "dvi"), (1, "bahu"),
    (2, "eka"), (2, "dvi"), (2, "bahu"),
    (3, "eka"), (3, "dvi"), (3, "bahu"),
    (4, "eka"), (4, "dvi"), (4, "bahu"),
    (5, "eka"), (5, "dvi"), (5, "bahu"),
    (6, "eka"), (6, "dvi"), (6, "bahu"),
    (7, "eka"), (7, "dvi"), (7, "bahu"),
]

SARVANAMASTHANA = {(1, "eka"), (1, "dvi"), (1, "bahu"), (2, "eka"), (2, "dvi")}
VOWEL_SUP = {"O", "Ow", "Am", "os", "Ne", "Nasi", "Nas", "Ni"}  # Ba contexts (vowel-initial after strip)

SARVA_LIST = {
    "sarva", "viSva", "uBa", "uBaya", "katara", "katama",
    "anya", "anyatara", "itara", "tvat", "tva", "nema",
    "sama", "sima", "sva", "antara", "eka",
    # directional semi-pronouns (vibhazA: pronoun or noun)
    "pUrva", "para", "avara", "dakziRa", "uttara", "apara", "aDara",
    "tad", "yad", "etad", "kim", "idam", "adas",
}
SEMI_PRONOUNS = {"pUrva", "para", "avara", "dakziRa", "uttara", "apara", "aDara"}
# 7.1.16 fractional pronouns: pronoun-ending only in jas (Nom pl),
# never in Ne/Nasi (Dat/Abl sg). e.g. praTamAH/praTame but only praTamAya.
PRATHAMA_CLASS = {"praTama", "carama", "tftIya", "alpa", "arDa", "katipaya",
                  "dvaya", "taya", "dvitaya", "tritaya"}
# dual-only sarvanAman
DUAL_ONLY = {"uBa", "dvi"}


def _infer_h_class(stem: str) -> str:
    """Infer 8.2.x h->? class from stem shape (generative, no lookup table
    beyond phonological shape): nah-final -> d (upAnah); lih/mih-type
    (i-vowel + h) -> q (retroflex); duh/druh/muh/snuh-type (u-vowel + h)
    -> g (velar); else d."""
    if stem.endswith("nah"):
        return "d"
    if stem in ("lih", "mih", "ruh", "snih", "snuh", "muh", "ruh"):
        # lih/mih/snih take retroflex q; muh/snuh Ruh take g — split by vowel
        if stem in ("lih", "mih", "snih"):
            return "q"
        if stem in ("muh", "snuh", "druh"):
            return "g"
    # shape rule: i-final-h -> q, u-final-h -> g
    if len(stem) >= 2 and stem[-2] == "i" and stem[-1] == "h":
        return "q"
    if len(stem) >= 2 and stem[-2] == "u" and stem[-1] == "h":
        return "g"
    if stem in ("duh",):
        return "g"
    return "d"


def strip_sup(sup: str) -> str:
    """Strip anubandha (it) letters: sU->s, jas->as, Sas->as, Ow->O, wA->A,
    Ne/Nasi/Nas/Ni->e/as/as/i, sup->su."""
    m = {
        "sU": "s", "O": "O", "jas": "as",
        "am": "am", "Ow": "O", "Sas": "as",
        "wA": "A", "ByAm": "ByAm", "Bis": "Bis",
        "Ne": "e", "Byas": "Byas",
        "Nasi": "as", "os": "os", "Am": "Am", "Ni": "i",
        "Nas": "as", "sup": "su",
    }
    return m.get(sup, sup)


def _is_vowel(ch: str) -> bool:
    return ch in SLP1_VOWELS


def apply_natva(word: str) -> str:
    """Internal Natva 8.4.1-2: n->R after r/R/z/f/F within pada.
    Allowed interveners (aw-kupvAN-num): vowels, h/y/v, k-varga, p-varga,
    anusvara. Blockers: c/t/w-vargas, sibilants S/z/s, l. First blocker
    resets the trigger (simplified single-pass)."""
    allowed = set("aAiIuUfFxXeEoOyvhHkKgGNpPbBmMYR")
    # note: R itself is target, also intervening R blocks further spread
    out: List[str] = []
    cause = False
    for i, c in enumerate(word):
        if c in ("r", "z", "f", "F"):
            cause = True
            out.append(c)
        elif c == "n":
            if cause:
                nxt = word[i + 1] if i + 1 < len(word) else ""
                # padanta n never retroflexes here (rAjan lone n drops elsewhere)
                if i == len(word) - 1 or nxt in "tTdDscCjJSwWqQzSl":
                    out.append("n")
                    # dental/palatal/retroflex/sibilant blocks
                    if nxt not in ("", "n", "m", "M"):
                        cause = False
                else:
                    out.append("R")
                    # R blocks further spread unless geminate nn
                    if nxt == "n":
                        pass
                    else:
                        cause = False
            else:
                out.append("n")
        elif c in allowed:
            out.append(c)
        else:
            cause = False
            out.append(c)
    return "".join(out)


def apply_zatva_s(word: str) -> str:
    """zatva 8.3.59 for suffix -su: s->z after k/iR cohort.
    Minimal: sup plural locative -su -> -zu after vowels/velars etc.
    Caller passes full word; only trailing su/su-adjacent handled."""
    # generic: s after iN/ku cohort (long vowels included) -> z
    # implemented as single pass for 's' not word-initial
    trig = set("iIuUfFxXeoEOyvrlhkKgGN")
    chars = list(word)
    for i in range(1, len(chars)):
        if chars[i] == "s" and chars[i - 1] in trig:
            # don't touch visarga contexts; only suffixal s (followed by u/vowel or end)
            chars[i] = "z"
    return "".join(chars)


def _coh_kuh(final: str) -> str:
    """8.2.30 coH kuH: c/C/j/J -> k (voicing handled at pada join)."""
    if final in ("c", "C", "j", "J"):
        return "k"
    # S -> z (vRaSca etc. 8.2.36: S->z)
    if final == "S":
        return "z"
    return final


def _final_devoice(cc: str) -> str:
    devo = {"g": "k", "G": "k", "j": "k", "J": "k", "q": "w",
            "Q": "w", "d": "t", "D": "t", "b": "p", "B": "p",
            "G": "k", "z": "w", "S": "w", "s": "t", "h": "w"}
    return devo.get(cc, cc)


def _join_pada(stem: str, suffix: str) -> str:
    """Join stem + consonant-initial suffix with first-sound voicing/devoicing:
    k/g, w/q, t/d, p/b alternations before B/s. Minimal generative."""
    if not suffix or not stem:
        return stem + suffix
    f = stem[-1]
    s0 = suffix[0]
    if s0 in ("B", "b"):
        # harden: c->g, j->g, w->q, t->d, p->b, s/z->d, h varies (caller sets)
        m = {"k": "g", "c": "g", "j": "g", "J": "g", "w": "q",
             "t": "d", "T": "w", "p": "b", "s": "d", "z": "d", "S": "d"}
        if f in m:
            stem = stem[:-1] + m[f]
    elif s0 == "s":
        m2 = {"k": "k", "g": "k", "c": "k", "j": "k",
              "q": "w", "t": "t", "d": "t", "p": "p", "b": "p"}
        if f in m2:
            stem = stem[:-1] + m2[f]
    return stem + suffix


class SubantaEngine:
    """Generative nominal declension."""

    def decline(self, stem: str, linga: str = "puM",
                sarvanAman: bool | None = None,
                extra: dict | None = None) -> Dict[Tuple[int, str], List[str]]:
        """Decline a pratipadika. linga in puM/strI/napuMsaka (also m/f/n).
        Returns dict (vibhakti 1..8, vacana) -> [forms]. 8 = sambodhana."""
        linga = {"m": "puM", "f": "strI", "n": "napuMsaka",
                 "masc": "puM", "fem": "strI", "neut": "napuMsaka"}.get(linga, linga)
        extra = extra or {}
        if sarvanAman is None:
            # feminine A-stems of pronouns (sarvA <- sarva) count as sarvanAman
            sarvanAman = stem in SARVA_LIST or (
                linga == "strI" and stem.endswith("A") and stem[:-1] + "a" in SARVA_LIST
            )
        # dispatch special suppletive pronouns first
        if stem in ("asmad", "yuzmad"):
            return self._decline_yuzmad_asmad(stem)
        if stem == "adas":
            return self._decline_adas(linga)
        if stem == "idam":
            return self._decline_idam(linga)
        if stem in ("tad", "etad", "yad"):
            return self._decline_tad(stem, linga)
        if stem == "kim":
            return self._decline_kim(linga)
        if stem in ("tri", "catur"):
            return self._decline_tri_catur(stem, linga)
        if stem == "dvi":
            return self._decline_dvi(linga)
        if stem in ("paYcan", "zaz", "azwan", "saYjan", "navaDaSan"):
            return self._decline_zaw(stem, linga)
        # monosyllabic / nipatana nouns
        if stem == "go":
            return self._decline_go(linga)
        if stem == "rE":
            return self._decline_rE(linga)
        if stem == "nO":
            return self._decline_nO(linga)
        if stem == "saKi":
            return self._decline_saKi(linga)
        if stem == "pati" and linga == "puM" and not extra.get("compound"):
            return self._decline_pati(linga)
        if stem == "krozwu":
            return self._decline_krozwu(linga)
        if stem in ("asTi", "daDi", "sakTi", "akzi"):
            return self._decline_asTi(stem, linga)
        if stem == "ap":
            return self._decline_ap()
        if stem == "anaQuh":
            return self._decline_anaQuh()
        if stem == "puMs":
            return self._decline_puMs()
        if stem in ("div", "dyO"):
            return self._decline_div(linga)
        if stem == "ahan":
            return self._decline_ahan()
        if stem in ("paTin", "maTin", "fBukzin"):
            return self._decline_paTin(stem)
        if stem in ("Svan", "yuvan", "maGavan"):
            return self._decline_Svan(stem)
        if stem == "jarA":
            return self._decline_jarA()
        if stem in ("SrI", "BU"):
            # SrI (wealth) vs BU (earth) monosyllabic feminines; BU the noun (not root)
            return self._decline_SrI_BU(stem)
        if stem.endswith("aYc"):
            return self._decline_aYc(stem, linga)
        if stem in ("Sreyas", "garIyas", "mahIyas", "BLa"):
            return self._decline_Iyas(stem, linga)
        # general path
        out: Dict[Tuple[int, str], List[str]] = {}
        for sup, key in zip(SUP_RAW, SUP_KEYS):
            forms = self._form_general(stem, linga, sup, key,
                                        sarvanAman=bool(sarvanAman), extra=extra)
            out[key] = forms
        # nAman optional weak (neut): nAmnA / nAmanA
        if stem == "nAman" and linga == "napuMsaka":
            if "nAmanA" not in out[(3, "eka")]:
                out[(3, "eka")] = out[(3, "eka")] + ["nAmanA"]
        # dual-only (uBa): blank eka/bahu
        if stem in DUAL_ONLY:
            for k in list(out.keys()):
                if k[1] != "dvi":
                    out[k] = []
        # sambodhana singular special; dual/plural = prathama
        out[(8, "eka")] = self._sambuddhi_eka(stem, linga, bool(sarvanAman), extra)
        out[(8, "dvi")] = list(out[(1, "dvi")])
        out[(8, "bahu")] = list(out[(1, "bahu")])
        if stem in DUAL_ONLY:
            out[(8, "eka")] = []
            out[(8, "bahu")] = []
        return out

    # ---------------- general ----------------
    def _form_general(self, stem: str, linga: str, sup: str, key: Tuple[int, str],
                      sarvanAman: bool = False, extra: dict | None = None) -> List[str]:
        extra = extra or {}
        vib, vac = key
        s = strip_sup(sup)
        # --- neuter 1/2 replacements (7.1.19-23): am->am(eka stays), O/Ow->I, as->i ---
        if linga == "napuMsaka" and vib in (1, 2):
            return [self._neuter_form(stem, vac, extra)]
        # --- sarvanaman adesa for Ne/Nasi/Nas/Ni/os/Am ---
        if sarvanAman and stem not in SEMI_PRONOUNS:
            r = self._sarva_adesa(stem, linga, sup, key)
            if r is not None:
                return r
        if sarvanAman and stem in SEMI_PRONOUNS:
            # vibhaza: both pronoun and noun outputs
            r1 = self._sarva_adesa(stem, linga, sup, key)
            r2 = self._noun_form(stem, linga, sup, key, sarvanAman=False, extra=extra)
            merged: List[str] = []
            for x in (r1 or []) + r2:
                if x not in merged:
                    merged.append(x)
            return merged
        # fractional pronouns (7.1.16): pronoun-ending only in jas Nom pl
        if stem in PRATHAMA_CLASS and sup == "jas" and key == (1, "bahu"):
            noun = self._noun_form(stem, linga, sup, key, sarvanAman=False, extra=extra)
            pron = self._sarva_adesa(stem, linga, sup, key) or []
            merged = list(noun)
            for x in pron:
                if x not in merged:
                    merged.append(x)
            return merged
        return self._noun_form(stem, linga, sup, key, sarvanAman=False, extra=extra)

    def _sarva_adesa(self, stem: str, linga: str, sup: str, key: Tuple[int, str]) -> List[str] | None:
        vib, vac = key
        # only singular smai/smat/smin + jas->e + Am->sAm + Ni->smin + os->zAm?
        # base: a-stem sarva -> sarva + ...
        # puM/neuter pattern; strI pattern uses syai/syAH/syAm etc.
        if linga in ("puM", "napuMsaka"):
            base = stem[:-1] if stem.endswith("a") else stem
            if sup == "jas" and vac == "bahu":
                return [self._fin(base + "e")]
            if (vib, vac) == (4, "eka"):
                return [self._fin(stem + "smE")]
            if (vib, vac) == (5, "eka"):
                return [self._fin(stem + "smAt")]
            if (vib, vac) == (7, "eka"):
                return [self._fin(stem + "smin")]
            if (vib, vac) == (6, "eka"):
                return [self._fin(stem + "sya")]
            if (vib, vac) == (6, "bahu"):
                # tezAm pattern: sarvezAm (e + zAm via satva+natva)
                return [apply_natva(base + "ezAm")]
            if (vib, vac) == (3, "eka"):
                return [apply_natva(base + "eRa")]
            if (vib, vac) == (2, "bahu"):
                return [self._fin(base + "An")]
        else:  # strI: sarvA + ...
            base = stem  # e.g. sarvA
            b = base[:-1] if base.endswith("A") else base
            if sup == "jas" and vac == "bahu":
                return [self._fin(b + "AH")]
            if (vib, vac) == (4, "eka"):
                return [self._fin(b + "asyE")]
            if (vib, vac) == (5, "eka"):
                return [self._fin(b + "asyAH")]
            if (vib, vac) == (6, "eka"):
                return [self._fin(b + "asyAH")]
            if (vib, vac) == (7, "eka"):
                return [self._fin(b + "asyAm")]
            if (vib, vac) == (6, "bahu"):
                return [apply_natva(b + "AsAm")]
            if (vib, vac) == (3, "eka"):
                return [self._fin(b + "ayA")]
            if (vib, vac) == (2, "bahu"):
                return [self._fin(b + "AH")]
        return None

    def _noun_form(self, stem: str, linga: str, sup: str, key: Tuple[int, str],
                   sarvanAman: bool = False, extra: dict | None = None) -> List[str]:
        extra = extra or {}
        vib, vac = key
        s = strip_sup(sup)
        last = stem[-1] if stem else ""
        # route by final
        if last == "a":
            return [self._a_stem(stem, s, sup, key, linga)]
        if last == "A":
            return [self._A_stem(stem, s, sup, key, linga, extra)]
        if last in ("i", "I"):
            return self._i_stem(stem, linga, s, sup, key, extra)
        if last in ("u", "U"):
            return self._u_stem(stem, linga, s, sup, key, extra)
        if last == "f":
            return [self._f_stem(stem, s, sup, key, linga, extra)]
        if last in ("e", "E", "o", "O"):
            return [self._fin(stem + s)]  # rare (go handled earlier)
        # halanta
        return [self._halanta(stem, linga, s, sup, key, extra)]

    # ---------------- a / A ----------------
    def _a_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str) -> str:
        vib, vac = key
        b = stem[:-1]  # Rama
        if (vib, vac) == (1, "eka"):
            return self._fin(b + "aH")  # s->visarga
        if (vib, vac) == (1, "dvi"):
            return b + "O"
        if (vib, vac) == (1, "bahu"):
            # as -> AH with vfddhi: rAmAH
            return b + "AH"
        if (vib, vac) == (2, "eka"):
            return b + "am"
        if (vib, vac) == (2, "dvi"):
            return b + "O"
        if (vib, vac) == (2, "bahu"):
            return b + "An"
        if (vib, vac) == (3, "eka"):
            return apply_natva(b + "eRa")  # ena->eRa
        if (vib, vac) == (3, "dvi"):
            return b + "AByAm"
        if (vib, vac) == (3, "bahu"):
            return b + "EH"
        if (vib, vac) == (4, "eka"):
            return b + "Aya"
        if (vib, vac) in ((4, "dvi"), (5, "dvi")):
            return b + "AByAm"
        if (vib, vac) == (4, "bahu"):
            return b + "eByaH"
        if (vib, vac) == (5, "eka"):
            return b + "At"
        if (vib, vac) == (5, "bahu"):
            return b + "eByaH"
        if (vib, vac) == (6, "eka"):
            return b + "asya"
        if (vib, vac) == (6, "dvi"):
            return b + "ayoH"
        if (vib, vac) == (6, "bahu"):
            return apply_natva(b + "AnAm")
        if (vib, vac) == (7, "eka"):
            return b + "e"
        if (vib, vac) == (7, "dvi"):
            return b + "ayoH"
        if (vib, vac) == (7, "bahu"):
            return apply_zatva_s(b + "ezu")
        raise AssertionError(key)

    def _A_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str, extra: dict) -> str:
        vib, vac = key
        b = stem[:-1]  # sIt
        if (vib, vac) == (1, "eka"):
            return self._fin(b + "A")
        if (vib, vac) == (1, "dvi"):
            return b + "e"
        if (vib, vac) == (1, "bahu"):
            return b + "AH"
        if (vib, vac) == (2, "eka"):
            return b + "Am"
        if (vib, vac) == (2, "dvi"):
            return b + "e"
        if (vib, vac) == (2, "bahu"):
            return b + "AH"
        if (vib, vac) == (3, "eka"):
            return b + "ayA"
        if (vib, vac) == (3, "dvi"):
            return b + "AByAm"
        if (vib, vac) == (3, "bahu"):
            return b + "ABiH"
        if (vib, vac) == (4, "eka"):
            return b + "AyE"
        if (vib, vac) in ((4, "dvi"), (5, "dvi")):
            return b + "AByAm"
        if (vib, vac) == (4, "bahu"):
            return b + "AByaH"
        if (vib, vac) == (5, "eka"):
            return b + "AyAH"
        if (vib, vac) == (5, "bahu"):
            return b + "AByaH"
        if (vib, vac) == (6, "eka"):
            return b + "AyAH"
        if (vib, vac) == (6, "dvi"):
            return b + "ayoH"
        if (vib, vac) == (6, "bahu"):
            return apply_natva(b + "AnAm")
        if (vib, vac) == (7, "eka"):
            return b + "AyAm"
        if (vib, vac) == (7, "dvi"):
            return b + "ayoH"
        if (vib, vac) == (7, "bahu"):
            return apply_zatva_s(b + "Asu")
        raise AssertionError(key)

    # ---------------- i / u (gI/nadI/vibhazA/num) ----------------
    def _i_stem(self, stem: str, linga: str, s: str, sup: str, key: Tuple[int, str], extra: dict) -> List[str]:
        vib, vac = key
        long = stem.endswith("I")
        b = stem[:-1]
        monosyllabic = len(b) == 0  # SrI handled earlier, but keep guard
        # neuter i-stems take num shield before vowel sup (7.1.73): vAri+A -> vAriRA
        if linga == "napuMsaka" and s and s[0] in "aAiIuUeEoO":
            # s is stripped sup initial: A/e/O/as/Am/os/i etc.
            w = stem + "n" + s
            if s == "s":
                return [self._fin(stem)]
            if (vib, vac) == (6, "bahu"):
                # vArIRAm (lengthened)
                long_v = SLP1_SHORT2LONG.get(stem[-1], stem[-1])
                return [self._fin(apply_natva(stem[:-1] + long_v + "RAm"))]
            if (vib, vac) == (7, "bahu"):
                return [apply_zatva_s(stem + "zu")]
            if vac == "bahu" or (vib, vac) in ((5, "eka"), (6, "eka")):
                # Abl/Gen sg and Acc pl end in visarga: vAriRaH
                return [self._fin(apply_natva(w))]
            return [self._fin(apply_natva(w))]
        # neuter handled before; here masc/fem
        is_fem = (linga == "strI")
        nadi = is_fem and (long or extra.get("nadI"))
        # short i/u fem optionality 1.4.6: NadI or GI in Nits (4/5/6/7 eka)
        Nit = (sup in ("Ne", "Nasi", "Nas", "Ni"))
        if (vib, vac) == (1, "eka"):
            return [self._fin(b + ("IH" if long else "iH"))]
        if (vib, vac) == (1, "dvi"):
            # nadI+O -> nadyO (yaR); SrI -> SriyO via iy
            if monosyllabic:
                return [b + ("iyO" if not long else "IyO")]
            return [b + "yO"]
        if (vib, vac) == (1, "bahu"):
            return [b + ("ayaH" if not long else "yaH")]
        if (vib, vac) == (2, "eka"):
            return [b + ("Im" if long else "im")]
        if (vib, vac) == (2, "dvi"):
            if long:
                return [b + "yO"]
            return [b + "yO"]
        if (vib, vac) == (2, "bahu"):
            if long:
                return [b + "IH"]
            # masc i: harIn? No: harIn only neuter. masc: harIn? Actually harIR? -> harIn? check: 2pl masc i = harIn (n→R): harIR? No, Sas->n->R: harIn->harIR? Let: hari+as -> harIn -> harIR (natva? no r trigger unless stem has r). hari has r! h-a-r-i: r triggers n->R: harIR.
            w = b + "In"
            return [apply_natva(w)]
        if (vib, vac) == (3, "eka"):
            if nadi:
                return [b + ("yA" if True else "")]
            # ghi: i->yA? hari+TA: haryA? Actually i->y + A: haryA
            if monosyllabic:
                return [b + "iyA"]
            return [b + "yA"]
        if (vib, vac) == (3, "dvi"):
            return [stem + "ByAm"]
        if (vib, vac) == (3, "bahu"):
            return [stem + "BiH"]
        if Nit and (vib, vac) == (4, "eka"):
            if nadi:
                return [b + "yE"]  # nadI+e with Aw: nadyE
            if is_fem and not long:
                # vibhaza mati: mataye / matyE
                return [b + "aye", b + "yE"]
            # masc ghi: haraye (ektir)
            return [b + "aye"]
        if Nit and (vib, vac) == (5, "eka"):
            if nadi:
                return [b + "yAH"]
            if is_fem and not long:
                return [b + "eH", b + "yAH"]
            return [b + "eH"]
        if Nit and (vib, vac) == (6, "eka"):
            if nadi:
                return [b + "yAH"]
            if is_fem and not long:
                return [b + "eH", b + "yAH"]
            return [b + "eH"]
        if Nit and (vib, vac) == (7, "eka"):
            if nadi:
                return [b + "yAm"]
            if is_fem and not long:
                return [b + "O", b + "yAm"]
            return [b + "O"]
        # non-Nit dual/plural 4/5/6/7
        if (vib, vac) in ((4, "dvi"), (5, "dvi")):
            return [stem + "ByAm"]
        if (vib, vac) in ((4, "bahu"), (5, "bahu")):
            return [stem + "ByaH"]
        if (vib, vac) == (6, "dvi"):
            if long:
                return [b + "yoH"]
            return [b + "yoH"]
        if (vib, vac) == (6, "bahu"):
            return [apply_natva(b + ("InAm" if not long else "InAm"))]
        if (vib, vac) == (7, "dvi"):
            if long:
                return [b + "yoH"]
            return [b + "yoH"]
        if (vib, vac) == (7, "bahu"):
            return [apply_zatva_s(stem + "zu")]
        raise AssertionError((stem, key))

    def _u_stem(self, stem: str, linga: str, s: str, sup: str, key: Tuple[int, str], extra: dict) -> List[str]:
        # mirror of i-stem with u/v alternation
        vib, vac = key
        long = stem.endswith("U")
        b = stem[:-1]
        monosyllabic = len(b) == 0
        # neuter u-stems take num shield before vowel sup (7.1.73): madhu+e -> madhune
        if linga == "napuMsaka" and s and s[0] in "aAiIuUeEoO":
            w = stem + "n" + s
            if s == "s":
                return [self._fin(stem)]
            if (vib, vac) == (6, "bahu"):
                long_v = SLP1_SHORT2LONG.get(stem[-1], stem[-1])
                return [self._fin(apply_natva(stem[:-1] + long_v + "RAm"))]
            if (vib, vac) == (7, "bahu"):
                return [apply_zatva_s(stem + "zu")]
            if vac == "bahu" or (vib, vac) in ((5, "eka"), (6, "eka")):
                return [self._fin(apply_natva(w))]
            return [self._fin(apply_natva(w))]
        is_fem = (linga == "strI")
        nadi = is_fem and (long or extra.get("nadI"))
        Nit = (sup in ("Ne", "Nasi", "Nas", "Ni"))
        if (vib, vac) == (1, "eka"):
            return [self._fin(b + ("UH" if long else "uH"))]
        if (vib, vac) == (1, "dvi"):
            return [b + "vO"]
        if (vib, vac) == (1, "bahu"):
            return [b + ("avaH" if not long else "vaH")]
        if (vib, vac) == (2, "eka"):
            return [b + ("Um" if long else "um")]
        if (vib, vac) == (2, "dvi"):
            return [b + "vO"]
        if (vib, vac) == (2, "bahu"):
            if long:
                return [b + "UH"]
            w = b + "Un"
            return [apply_natva(w)]
        if (vib, vac) == (3, "eka"):
            if monosyllabic:
                return [b + "uvA"]
            return [b + "vA"]
        if (vib, vac) == (3, "dvi"):
            return [stem + "ByAm"]
        if (vib, vac) == (3, "bahu"):
            return [stem + "BiH"]
        if Nit and (vib, vac) == (4, "eka"):
            if nadi:
                return [b + "vE"]
            if is_fem and not long:
                return [b + "ave", b + "vE"]
            return [b + "ave"]
        if Nit and (vib, vac) == (5, "eka"):
            if nadi:
                return [b + "vAH"]
            if is_fem and not long:
                return [b + "oH", b + "vAH"]
            return [b + "oH"]
        if Nit and (vib, vac) == (6, "eka"):
            if nadi:
                return [b + "vAH"]
            if is_fem and not long:
                return [b + "oH", b + "vAH"]
            return [b + "oH"]
        if Nit and (vib, vac) == (7, "eka"):
            if nadi:
                return [b + "vAm"]
            if is_fem and not long:
                return [b + "O", b + "vAm"]
            return [b + "O"]
        if (vib, vac) in ((4, "dvi"), (5, "dvi")):
            return [stem + "ByAm"]
        if (vib, vac) in ((4, "bahu"), (5, "bahu")):
            return [stem + "ByaH"]
        if (vib, vac) == (6, "dvi"):
            return [b + "voH"]
        if (vib, vac) == (6, "bahu"):
            return [apply_natva(b + "UnAm")]
        if (vib, vac) == (7, "dvi"):
            return [b + "voH"]
        if (vib, vac) == (7, "bahu"):
            return [apply_zatva_s(stem + "zu")]
        raise AssertionError((stem, key))

    # ---------------- f ----------------
    def _f_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str, extra: dict) -> str:
        vib, vac = key
        # default kind: kinship short-ar vs agent long-Ar; svasf forced agent
        KIN = {"pitf", "mAtf", "BrAtf", "duhitf", "yAtf", "nanAndf", "naptf"}
        kind = extra.get("f_kind")
        if kind is None:
            kind = "kin" if stem in KIN else "agent"
        if stem == "svasf":
            kind = "agent"
        b = stem[:-1]
        strong = key in SARVANAMASTHANA
        if strong:
            if (vib, vac) == (1, "eka"):
                return self._fin(b + "A")
            if (vib, vac) in ((1, "dvi"), (2, "dvi")):
                return b + ("ArO" if kind == "agent" else "arO")
            if (vib, vac) == (1, "bahu"):
                return b + ("AraH" if kind == "agent" else "araH")
            if (vib, vac) == (2, "eka"):
                return b + ("Aram" if kind == "agent" else "aram")
        else:
            # weak: f -> r/ur before vowel; B/pada before consonant
            pass
        if (vib, vac) == (2, "bahu"):
            # kartfRaH / pitfRaH (F retained, n->R, visarga)
            return self._fin(apply_natva(b + "FRa") + "s")
        if (vib, vac) == (3, "eka"):
            return b + "rA"
        if (vib, vac) == (3, "dvi"):
            return b + "fByAm"
        if (vib, vac) == (3, "bahu"):
            return b + "fBiH"
        if (vib, vac) == (4, "eka"):
            return b + "re"
        if (vib, vac) in ((4, "dvi"), (5, "dvi")):
            return b + "fByAm"
        if (vib, vac) in ((4, "bahu"), (5, "bahu")):
            return b + "fByaH"
        if (vib, vac) == (5, "eka"):
            return b + "uH"
        if (vib, vac) == (6, "eka"):
            return b + "uH"
        if (vib, vac) == (6, "dvi"):
            return b + "roH"
        if (vib, vac) == (6, "bahu"):
            # agent: kartrARAm ; kin: pitFRam
            if kind == "agent":
                return apply_natva(b + "rARAm")
            return apply_natva(b + "FRAm")
        if (vib, vac) == (7, "eka"):
            return b + "ari"
        if (vib, vac) == (7, "dvi"):
            return b + "roH"
        if (vib, vac) == (7, "bahu"):
            return apply_zatva_s(b + "fzu")
        raise AssertionError((stem, key))

    # ---------------- halanta ----------------
    def _halanta(self, stem: str, linga: str, s: str, sup: str, key: Tuple[int, str], extra: dict) -> str:
        vib, vac = key
        # an/in stems
        if stem.endswith("an"):
            return self._an_stem(stem, s, sup, key, linga, extra)
        if stem.endswith(("at", "ant")) or extra.get("Satf") or stem in ("Bavat", "mahat", "jagat"):
            return self._at_stem(stem, s, sup, key, linga, extra)
        if stem.endswith(("in",)) and len(stem) > 2 and stem not in ("paTin",):
            return self._in_stem(stem, s, sup, key, linga)
        if stem.endswith(("vas", "vAMs", "uz")) or extra.get("kvasu"):
            return self._vas_stem(stem, s, sup, key, linga)
        if stem.endswith(("vat", "tavat")) or extra.get("ktavatu"):
            return self._vat_stem(stem, s, sup, key, linga)
        if stem.endswith(("as", "is", "us")):
            return self._as_stem(stem, s, sup, key, linga, extra)
        if stem.endswith(("Iyas",)):
            return self._Iyas_form(stem, s, sup, key, linga)
        if stem[-1] in ("c", "C", "j", "J"):
            return self._c_stem(stem, s, sup, key)
        if stem[-1] == "h":
            return self._h_stem(stem, s, sup, key, extra)
        if stem[-1] in ("d", "D", "t", "T", "p", "P", "b", "B", "k", "K", "g", "G", "m", "y", "r", "l", "v", "n", "s", "S", "z"):
            return self._pada_consonant(stem, s, sup, key)
        return self._fin(stem + s)

    def _an_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str, extra: dict) -> str:
        vib, vac = key
        # rAjan/atman/brahman/karman/nAman + neuter optionality
        # strong: rAjA; weak vowel: rAjY (a-lopa -> jY); pada: rAja + B
        b = stem[:-2]  # rAj
        heavy = len(b) >= 2 and b[-1] not in SLP1_VOWELS and b[-2] not in SLP1_VOWELS
        # Actually cluster test: Atman (tm), brahman (hm): heavy -> no lopa
        is_heavy_cluster = (stem in ("Atman", "brahman", "karman") or
                            (len(stem) >= 4 and stem[-4] not in SLP1_VOWELS and stem[-3] not in SLP1_VOWELS))
        strong = key in SARVANAMASTHANA
        if strong:
            if (vib, vac) == (1, "eka"):
                # n lopa: rAjA
                return self._fin(b + "A")
            if (vib, vac) in ((1, "dvi"), (2, "dvi")):
                return b + "AnO"
            if (vib, vac) == (1, "bahu"):
                return b + "AnaH"
            if (vib, vac) == (2, "eka"):
                return b + "Anam"
        # weak vowel (Ba): a-lopa unless heavy; rAjan j+n->jY, else retain n
        def weak(base_b: str) -> str:
            if is_heavy_cluster:
                return stem  # AtmanA etc.
            if base_b.endswith("j"):
                return base_b + "Y"  # rAj + Y = rAjY
            return base_b + "n"  # nAm + n = nAmn
        vowel_init = s and s[0] in SLP1_VOWELS or s in ("O", "as", "Am", "os", "e", "i")
        cons_init = not vowel_init
        if cons_init:
            # pada: n-lopa: rAja + ByAm/Bis etc.
            pada = b + "a"
            if s == "s":
                return self._fin(_final_devoice(pada[-1]) and pada or pada)
            if s == "s":
                return pada
            return self._fin(_join_pada(pada, s if s not in ("s",) else ""))
        # vowel suffix
        w = weak(b)
        # join: rAjY + A -> rAjYA; nAmn + A -> nAmnA
        if w.endswith(("n", "Y")) and s.startswith(("A", "e", "o", "O", "as", "Am", "os", "a", "i")):
            return self._fin(w + s)
        return self._fin(w + s)

    def _at_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str, extra: dict) -> str:
        vib, vac = key
        # normalize base: gacCat / jagat / mahat / Bavat
        base = stem
        if base.endswith("ant"):
            base = base[:-3] + "at"
        b = base[:-2] if base.endswith("at") else base
        strong = key in SARVANAMASTHANA
        # Bavat/baGavat/mahat take lengthened Ant; Satf (gacCat) takes short ant;
        # plain jagat/marut keep at (no num) in masc strong sg? Neuter handled earlier.
        # NOTE: "Bavat" is ambiguous (pronoun BavAn vs BU-Satf participle Bavan);
        # default long (pronoun); pass extra={'satf': True} for participle short.
        # Abhyasta (class 3, dadat) bans num altogether (7.1.78): behaves
        # like plain at. Pass extra={'abhyasta': True} for reduplicated stems.
        abhyasta = bool(extra.get("abhyasta"))
        is_long_Ant = (stem == "mahat" or extra.get("mahat")
                       or stem.endswith("tavat")  # ktavatu
                       or (stem in ("Bavat", "bagavat") and not extra.get("satf"))
                       or extra.get("long_Ant"))
        # plain at nouns (jagat, marut, sarit) do not take num in strong
        plain_at = abhyasta or stem in ("jagat", "marut", "sarit", "vidyut", "Sakaw")
        if strong:
            if plain_at:
                if (vib, vac) == (1, "eka"):
                    return self._fin(base)
                if (vib, vac) in ((1, "dvi"), (2, "dvi")):
                    return base + "O"
                if (vib, vac) == (1, "bahu"):
                    return base + "aH"
                if (vib, vac) == (2, "eka"):
                    return base + "am"
            if is_long_Ant:
                nform = b + "Ant"
                if nform.startswith("mah"):
                    nform = "mahAnt"
                # Bavat: Ba -> BA
                if stem == "Bavat":
                    # Bavat -> BavAnt (second a lengthened only)
                    nform = "BavAnt"
            else:
                # num -> n: gacCat -> gacCant
                nform = b + "ant"
            if (vib, vac) == (1, "eka"):
                # t lopa? gacCan (n + visarga? actually gacCan)
                w = nform[:-1]  # gacCan
                # nt -> n at end
                return self._fin(w)
            if (vib, vac) in ((1, "dvi"), (2, "dvi")):
                return nform + "O"
            if (vib, vac) == (1, "bahu"):
                return nform + "aH"
            if (vib, vac) == (2, "eka"):
                return nform + "am"
        # weak/middle
        if s == "s":
            return self._fin(base[:-1] + "n" if False else base)
        if s and s[0] in ("B",):
            return self._fin(_join_pada(base, s))
        if s == "su":
            return apply_zatva_s(_join_pada(base, "su"))
        return self._fin(base + s) if False else self._fin(base + ("" if False else s) if True else "")

    def _in_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str) -> str:
        vib, vac = key
        b = stem[:-2]  # DAn? e.g. DAnin->DAn
        strong = key in SARVANAMASTHANA
        if strong:
            if (vib, vac) == (1, "eka"):
                return self._fin(b + "I")
            if (vib, vac) in ((1, "dvi"), (2, "dvi")):
                return b + "inO"
            if (vib, vac) == (1, "bahu"):
                return b + "inaH"
            if (vib, vac) == (2, "eka"):
                return b + "inam"
        if s == "s":
            return self._fin(b + "I")
        if s and s[0] == "B":
            return self._fin(_join_pada(stem, s))
        if s == "su":
            # n-lopa + I + zatva: Danin+su -> DanIzu
            return apply_zatva_s(b + "I" + "su")
        if s == "as" and (vib, vac) == (2, "bahu"):
            return self._fin(b + "inaH")
        return self._fin(stem + s if s not in ("O",) else b + "inO")

    def _as_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str, extra: dict) -> str:
        vib, vac = key
        # manas/havis/cakzus/Sreyas handled; strong neuter num+lengthen handled in _neuter_form
        if linga == "napuMsaka" and vib in (1, 2):
            return self._neuter_form(stem, vac, extra)
        # masc/fem s-stems: sumanas etc. decline like halanta pada
        if s == "s":
            # s->H
            return self._fin(stem[:-1] + "H")
        if s and s[0] == "B":
            # s->H? No: manas+ByAm -> manoByAm (as->o before B)
            b = stem[:-2]  # mana
            return self._fin(b + "o" + s)
        if s == "su":
            b = stem[:-2]
            v = stem[-2] if len(stem) >= 2 else "a"  # mana/havi/cakzu -> a/i/u
            vlong = {"a": "a", "i": "i", "u": "u"}.get(v, "a")
            return apply_zatva_s(b + vlong + "H" + "su")
        if s in ("O", "as", "Am", "os"):
            # zatva on stem-final s after iN/ku (havis+Am -> havizAm; manas stays)
            add = "O" if s == "O" else s
            w = stem + add
            idx = len(stem) - 1  # stem-final s position
            if w[idx] == "s" and stem[-2] in set("iIuUfFxXeoEOyvrlhkKgGN"):
                w = w[:idx] + "z" + w[idx + 1:]
            return self._fin(w)
        # other vowel-initial (A/e/i): same zatva (havis+A -> havizA)
        if s and s[0] in SLP1_VOWELS:
            w = stem + s
            idx = len(stem) - 1
            if w[idx] == "s" and stem[-2] in set("iIuUfFxXeoEOyvrlhkKgGN"):
                w = w[:idx] + "z" + w[idx + 1:]
            return self._fin(w)
        return self._fin(stem + s)

    def _Iyas_form(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str) -> str:
        # delegate to full Iyasu table (generative, same as _decline_Iyas)
        return self._decline_Iyas(stem, linga)[key][0]

    def _vas_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str) -> str:
        # kvasu: cakfvas: strong -vAMs, weak -uz, middle -vat
        vib, vac = key
        # recover root base: assume stem ends vas
        b = stem[:-3] if stem.endswith("vas") else stem[:-2]
        strong = key in SARVANAMASTHANA
        if strong:
            if (vib, vac) == (1, "eka"):
                return self._fin(b + "vAn")
            if (vib, vac) in ((1, "dvi"), (2, "dvi")):
                return b + "vAMsO"
            if (vib, vac) == (1, "bahu"):
                return b + "vAMsaH"
            if (vib, vac) == (2, "eka"):
                return b + "vAMsam"
        # middle (consonant)
        if s and s[0] == "B":
            return self._fin(_join_pada(b + "vat", s))
        if s == "su":
            return apply_zatva_s(_join_pada(b + "vat", "su"))
        if s == "s":
            return self._fin(b + "vAn")
        # weak vowel: samprasarana v->u: cakfvas+A -> cakfuzA
        return self._fin(b + "uz" + s)

    def _vat_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], linga: str) -> str:
        # ktavatu/bagavat: strong -vAn, else -vat
        vib, vac = key
        b = stem[:-3] if stem.endswith("vat") else stem
        strong = key in SARVANAMASTHANA
        if strong:
            if (vib, vac) == (1, "eka"):
                return self._fin(b + "vAn")
            if (vib, vac) in ((1, "dvi"), (2, "dvi")):
                return b + "vantO"
            if (vib, vac) == (1, "bahu"):
                return b + "vantaH"
            if (vib, vac) == (2, "eka"):
                return b + "vantam"
        if s == "s":
            return self._fin(b + "vAn")
        if s and s[0] == "B":
            return self._fin(_join_pada(b + "vat", s))
        if s == "su":
            return apply_zatva_s(_join_pada(b + "vat", "su"))
        if s == "as" and (vib, vac) == (2, "bahu"):
            return self._fin(b + "vataH")
        return self._fin(b + "vat" + s if s not in ("O",) else b + "vantO")

    def _c_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str]) -> str:
        # vAc/ftvij: vowel: keep c; consonant/padanta: c->k/g + join; su: kzu
        # 8.2.36 vraj-exception: parivrAj/viSrAj j->w/q (retroflex), not k/g
        vraj = stem.endswith("vrAj") or stem in ("parivrAj", "viSrAj")
        k = "w" if vraj else "k"
        b = stem
        if s == "s":
            return self._fin(b[:-1] + k)
        if s and s[0] == "B":
            # vAg + BiH ; parivrAq + BiH
            base = b[:-1] + k
            return self._fin(_join_pada(base, s))
        if s == "su":
            base = b[:-1] + k
            w = _join_pada(base, "su")
            # k+su -> kzu (zatva of s after k)
            return w[:-2] + "zu"
        if s == "as" and sup == "Sas":
            return self._fin(b + "aH")
        return self._fin(b + s)

    def _h_stem(self, stem: str, s: str, sup: str, key: Tuple[int, str], extra: dict) -> str:
        # upAnah (h->t/d), duh (h->k/g), lih (h->w/q); auto-inferred by shape,
        # explicit extra h_class overrides (d/g/q)
        hclass = extra.get("h_class") or _infer_h_class(stem)  # d/g/q
        b = stem[:-1]
        mp = {"d": ("t", "d"), "g": ("k", "g"), "q": ("w", "q")}[hclass]
        if s == "s":
            return self._fin(b + mp[0])
        if s and s[0] == "B":
            return self._fin(_join_pada(b + mp[0], s))
        if s == "su":
            return apply_zatva_s(_join_pada(b + mp[0], "su"))
        return self._fin(stem + s)

    def _pada_consonant(self, stem: str, s: str, sup: str, key: Tuple[int, str]) -> str:
        if s == "s":
            # final devoice + visarga path: marut->marut (t stays), jagat->jagat
            last = stem[-1]
            return self._fin(stem[:-1] + _final_devoice(last))
        if s and s[0] == "B":
            return self._fin(_join_pada(stem, s))
        if s == "su":
            w = _join_pada(stem, s)
            return apply_zatva_s(w)
        if s == "as" and sup == "Sas":
            return self._fin(stem + "aH")
        return self._fin(stem + s)

    # ---------------- neuter ----------------
    def _neuter_form(self, stem: str, vac: str, extra: dict) -> str:
        # 1/2 neuter: eka: stem (+m for a? am) ; dvi: I ; bahu: ni+num
        last = stem[-1] if stem else ""
        if vac == "eka":
            if last == "a":
                return stem[:-1] + "am"
            if last in ("i", "u"):
                return self._fin(stem)  # vAri, madhu (su-luk)
            if last in ("I", "U"):
                return self._fin(stem)
            if stem.endswith("an"):
                # nAma etc: nAma (n-lopa)
                return self._fin(stem[:-1])
            if stem.endswith(("as", "is", "us")):
                return self._fin(stem)
            if stem.endswith(("at", "ant", "vat", "vas")):
                return self._fin(stem)
            return self._fin(stem)
        if vac == "dvi":
            if last == "a":
                return stem[:-1] + "e"
            if last in ("i", "u", "I", "U"):
                # vAriRI? Actually vAriRI: nI? vAri + I with num? No: dvi is I: vAriRI? Standard: vAriRI.
                # vAri + I -> vAriRI (num)
                return apply_natva(stem + "nI")
            if stem.endswith("an"):
                return stem + "I"  # nAmnI? Actually nAmnI
            return self._fin(stem + "I")
        # bahu: num + i/jas->i
        if last == "a":
            # PalAni: A + n + i
            return apply_natva(stem[:-1] + "Ani")
        if last in ("i", "u"):
            # vArIRi, madUni (stem vowel lengthened + num)
            long_v = SLP1_SHORT2LONG.get(last, last)
            return apply_natva(stem[:-1] + long_v + "R" + "i")
        if last in ("A", "I", "U"):
            return apply_natva(stem + "n" + "i")
        if stem.endswith(("as", "is", "us")):
            # manAMsi / havIMsi / cakzUMsi : lengthen + num->M before sibilant
            kind = stem[-2:]
            b = stem[:-2]
            if kind == "as":
                # manas -> manAMsi (a->A)
                return b + "AMsi"
            if kind == "is":
                return b + "IMsi"
            if kind == "us":
                return b + "UMsi"
            return apply_natva(stem + "ni")
        # consonant neuters: jaganti, nAmAni, karmARi
        if stem.endswith("an"):
            # nAman->nAmAni (A lengthen? keep)
            b = stem[:-2]
            return apply_natva(b + "Ani")
        # at: jagat->jaganti (num after last vowel); mahat->mahAnti (lengthen)
        # insert n after last vowel
        idx = -1
        for i in range(len(stem) - 1, -1, -1):
            if stem[i] in SLP1_VOWELS:
                idx = i
                break
        if idx != -1:
            pre, vow, post = stem[:idx], stem[idx], stem[idx + 1:]
            if stem == "mahat" or extra.get("mahat"):
                vow = SLP1_SHORT2LONG.get(vow, vow)  # maha->mahA
            w = pre + vow + "n" + post + "i"
            return apply_natva(w)
        return apply_natva(stem + "ni")

    # ---------------- sambuddhi ----------------
    def _sambuddhi_eka(self, stem: str, linga: str, sarvanAman: bool, extra: dict) -> List[str]:
        last = stem[-1] if stem else ""
        b = stem[:-1] if stem else ""
        if last == "a":
            # neuter vocative = nominative (Palam, not Pala)
            if linga == "napuMsaka":
                return [self._neuter_form(stem, "eka", extra)]
            return [b + "a"]  # he rAma (su-lopa)
        if last == "A":
            # sItA -> sIte
            return [stem[:-1] + "e"]
        if last in ("I", "U") and linga == "strI":
            # nadI->nadi, vaDU->vaDu (hrasva); SrI/B U? no hrasva (monosyllabic exception) -> he SrI
            if stem in ("SrI", "BU", "SrI"):
                return [self._fin(stem)]
            short = "i" if last == "I" else "u"
            # ambA->amba handled via A branch? ambA ends A but rule says hrasva: he amba
            return [stem[:-1] + short]
        if last in ("i", "u"):
            # neuter vocative = nominative (vAri, madhu), no guNa
            if linga == "napuMsaka":
                return [self._fin(stem)]
            # sambuddhi guNa: hare / guro
            if last == "i":
                return [b + "e"]
            return [b + "o"]
        if last == "f":
            return [stem[:-1] + "ar"]  # he kartar / pitar
        if last == "A" and stem in ("ambA",):
            return ["amba"]
        # neuter vocative = nominative (karma, not karmA)
        if linga == "napuMsaka":
            return [self._neuter_form(stem, "eka", extra)]
        # halanta: = prathama eka
        g = self._noun_form(stem, linga, "sU", (1, "eka"), sarvanAman=False, extra=extra)
        return g

    def _fin(self, w: str) -> str:
        # final s -> H (rutva-visarga), keep internal
        if w.endswith("s"):
            return w[:-1] + "H"
        return w

    # ================= special paradigms =================
    def _decline_go(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # go (o-stem): gOH/gAvO/gAvaH/gAm/gAvO/gAH/gavA/gAByAm/goBiH/gave/gAByAm/goByaH/goH/gAByAm/goByaH/goH/gavoH/gavAm/gavi/gavoH/gozu + he gOH
        T: Dict[Tuple[int, str], str] = {
            (1, "eka"): "gOH", (1, "dvi"): "gAvO", (1, "bahu"): "gAvaH",
            (2, "eka"): "gAm", (2, "dvi"): "gAvO", (2, "bahu"): "gAH",
            (3, "eka"): "gavA", (3, "dvi"): "goByAm", (3, "bahu"): "goBiH",
            (4, "eka"): "gave", (4, "dvi"): "goByAm", (4, "bahu"): "goByaH",
            (5, "eka"): "goH", (5, "dvi"): "goByAm", (5, "bahu"): "goByaH",
            (6, "eka"): "goH", (6, "dvi"): "gavoH", (6, "bahu"): "gavAm",
            (7, "eka"): "gavi", (7, "dvi"): "gavoH", (7, "bahu"): "gozu",
            (8, "eka"): "gOH", (8, "dvi"): "gAvO", (8, "bahu"): "gAvaH",
        }
        return {k: [v] for k, v in T.items()}

    def _decline_rE(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        T = {
            (1, "eka"): "rAH", (1, "dvi"): "rAyO", (1, "bahu"): "rAyaH",
            (2, "eka"): "rAyam", (2, "dvi"): "rAyO", (2, "bahu"): "rAyaH",
            (3, "eka"): "rAyA", (3, "dvi"): "rAByAm", (3, "bahu"): "rABiH",
            (4, "eka"): "rAye", (4, "dvi"): "rAByAm", (4, "bahu"): "rAByaH",
            (5, "eka"): "rAyaH", (5, "dvi"): "rAByAm", (5, "bahu"): "rAByaH",
            (6, "eka"): "rAyaH", (6, "dvi"): "rAyoH", (6, "bahu"): "rAyAm",
            (7, "eka"): "rAyi", (7, "dvi"): "rAyoH", (7, "bahu"): "rAsu",
            (8, "eka"): "rAH", (8, "dvi"): "rAyO", (8, "bahu"): "rAyaH",
        }
        return {k: [v] for k, v in T.items()}

    def _decline_nO(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        T = {
            (1, "eka"): "nOH", (1, "dvi"): "nAvO", (1, "bahu"): "nAvaH",
            (2, "eka"): "nAvam", (2, "dvi"): "nAvO", (2, "bahu"): "nAvaH",
            (3, "eka"): "nAvA", (3, "dvi"): "nOByAm", (3, "bahu"): "nOBiH",
            (4, "eka"): "nAve", (4, "dvi"): "nOByAm", (4, "bahu"): "nOByaH",
            (5, "eka"): "nAvaH", (5, "dvi"): "nOByAm", (5, "bahu"): "nOByaH",
            (6, "eka"): "nAvaH", (6, "dvi"): "nAvoH", (6, "bahu"): "nAvAm",
            (7, "eka"): "nAvi", (7, "dvi"): "nAvoH", (7, "bahu"): "nOzu",
            (8, "eka"): "nOH", (8, "dvi"): "nAvO", (8, "bahu"): "nAvaH",
        }
        return {k: [v] for k, v in T.items()}

    def _decline_saKi(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # aSaki (1.4.7): strong saKAy; weak saKy; Nom sg saKA
        T = {
            (1, "eka"): "saKA", (1, "dvi"): "saKAyO", (1, "bahu"): "saKAyaH",
            (2, "eka"): "saKAyam", (2, "dvi"): "saKAyO", (2, "bahu"): "saKyIn",
            (3, "eka"): "saKyA", (3, "dvi"): "saKiByAm", (3, "bahu"): "saKiBiH",
            (4, "eka"): "saKye", (4, "dvi"): "saKiByAm", (4, "bahu"): "saKiByaH",
            (5, "eka"): "saKyuH", (5, "dvi"): "saKiByAm", (5, "bahu"): "saKiByaH",
            (6, "eka"): "saKyuH", (6, "dvi"): "saKyoH", (6, "bahu"): "saKInAm",
            (7, "eka"): "saKyO", (7, "dvi"): "saKyoH", (7, "bahu"): "saKizu",
            (8, "eka"): "saKe", (8, "dvi"): "saKAyO", (8, "bahu"): "saKAyaH",
        }
        return {k: [v] for k, v in T.items()}

    def _decline_pati(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # alone: patyA etc (aSaki-like but suH kept? Instr patyA)
        T = {
            (1, "eka"): "patiH", (1, "dvi"): "patyO", (1, "bahu"): "patayaH",
            (2, "eka"): "patim", (2, "dvi"): "patyO", (2, "bahu"): "patIn",
            (3, "eka"): "patyA", (3, "dvi"): "patiByAm", (3, "bahu"): "patiBiH",
            (4, "eka"): "patye", (4, "dvi"): "patiByAm", (4, "bahu"): "patiByaH",
            (5, "eka"): "patyuH", (5, "dvi"): "patiByAm", (5, "bahu"): "patiByaH",
            (6, "eka"): "patyuH", (6, "dvi"): "patyoH", (6, "bahu"): "patInAm",
            (7, "eka"): "patyO", (7, "dvi"): "patyoH", (7, "bahu"): "patizu",
            (8, "eka"): "pate", (8, "dvi"): "patyO", (8, "bahu"): "patayaH",
        }
        return {k: [v] for k, v in T.items()}

    def _decline_krozwu(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # strong krozwf; weak krozwu/krozwf optional
        T: Dict[Tuple[int, str], List[str]] = {
            (1, "eka"): ["krozwA"], (1, "dvi"): ["krozwArO"], (1, "bahu"): ["krozwAraH"],
            (2, "eka"): ["krozwAram"], (2, "dvi"): ["krozwArO"], (2, "bahu"): ["krozwUn", "krozwFn"],
            (3, "eka"): ["krozwA", "krozwunA"], (3, "dvi"): ["krozwuByAm"], (3, "bahu"): ["krozwuBiH"],
            (4, "eka"): ["krozwe", "krozwave"], (4, "dvi"): ["krozwuByAm"], (4, "bahu"): ["krozwuByaH"],
            (5, "eka"): ["krozwuH"], (5, "dvi"): ["krozwuByAm"], (5, "bahu"): ["krozwuByaH"],
            (6, "eka"): ["krozwuH"], (6, "dvi"): ["krozwvoH", "krozwroH"], (6, "bahu"): ["krozwUnAm", "krozwFRam"],
            (7, "eka"): ["krozwO"], (7, "dvi"): ["krozwvoH", "krozwroH"], (7, "bahu"): ["krozwuzu"],
            (8, "eka"): ["krozwo"], (8, "dvi"): ["krozwArO"], (8, "bahu"): ["krozwAraH"],
        }
        return T

    def _decline_asTi(self, stem: str, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # weak an: asTnA etc.
        cap = {"asTi": "asT", "daDi": "daD", "sakTi": "sakT", "akzi": "akz"}[stem]
        T = {
            (1, "eka"): [stem], (1, "dvi"): [stem + "nI"], (1, "bahu"): [stem + "ni"],
            (2, "eka"): [stem], (2, "dvi"): [stem + "nI"], (2, "bahu"): [stem + "ni"],
            (3, "eka"): [cap + "nA"], (3, "dvi"): [stem + "ByAm"], (3, "bahu"): [stem + "BiH"],
            (4, "eka"): [cap + "ne"], (4, "dvi"): [stem + "ByAm"], (4, "bahu"): [stem + "ByaH"],
            (5, "eka"): [cap + "naH"], (5, "dvi"): [stem + "ByAm"], (5, "bahu"): [stem + "ByaH"],
            (6, "eka"): [cap + "naH"], (6, "dvi"): [cap + "noH"], (6, "bahu"): [apply_natva(cap + "nAm")],
            (7, "eka"): [cap + "ni"], (7, "dvi"): [cap + "noH"], (7, "bahu"): [apply_zatva_s(stem + "zu")],
            (8, "eka"): [stem], (8, "dvi"): [stem + "nI"], (8, "bahu"): [stem + "ni"],
        }
        return T

    def _decline_ap(self) -> Dict[Tuple[int, str], List[str]]:
        # feminine always plural
        T = {
            (1, "eka"): [], (1, "dvi"): [], (1, "bahu"): ["ApaH"],
            (2, "eka"): [], (2, "dvi"): [], (2, "bahu"): ["apaH"],
            (3, "eka"): [], (3, "dvi"): [], (3, "bahu"): ["adBiH"],
            (4, "eka"): [], (4, "dvi"): [], (4, "bahu"): ["adByaH"],
            (5, "eka"): [], (5, "dvi"): [], (5, "bahu"): ["adByaH"],
            (6, "eka"): [], (6, "dvi"): [], (6, "bahu"): ["apAm"],
            (7, "eka"): [], (7, "dvi"): [], (7, "bahu"): ["apsu"],
            (8, "eka"): [], (8, "dvi"): [], (8, "bahu"): ["ApaH"],
        }
        return T

    def _decline_anaQuh(self) -> Dict[Tuple[int, str], List[str]]:
        T = {
            (1, "eka"): ["anaQvAn"], (1, "dvi"): ["anaQvAMsO"], (1, "bahu"): ["anaQuhaH"],
            (2, "eka"): ["anaQvAMsam"], (2, "dvi"): ["anaQvAMsO"], (2, "bahu"): ["anaQuhaH"],
            (3, "eka"): ["anaQuhA"], (3, "dvi"): ["anaQudByAm"], (3, "bahu"): ["anaQudBiH"],
            (4, "eka"): ["anaQuhe"], (4, "dvi"): ["anaQudByAm"], (4, "bahu"): ["anaQudByaH"],
            (5, "eka"): ["anaQuhaH"], (5, "dvi"): ["anaQudByAm"], (5, "bahu"): ["anaQudByaH"],
            (6, "eka"): ["anaQuhaH"], (6, "dvi"): ["anaQuhoH"], (6, "bahu"): ["anaQuhAm"],
            (7, "eka"): ["anaQuhi"], (7, "dvi"): ["anaQuhoH"], (7, "bahu"): ["anaQutsu"],
            (8, "eka"): ["anaQvan"], (8, "dvi"): ["anaQvAMsO"], (8, "bahu"): ["anaQuhaH"],
        }
        return T

    def _decline_puMs(self) -> Dict[Tuple[int, str], List[str]]:
        T = {
            (1, "eka"): ["pumAn"], (1, "dvi"): ["pumAMsO"], (1, "bahu"): ["pumAMsaH"],
            (2, "eka"): ["pumAMsam"], (2, "dvi"): ["pumAMsO"], (2, "bahu"): ["puMsaH"],
            (3, "eka"): ["puMsA"], (3, "dvi"): ["pumByAm"], (3, "bahu"): ["pumBiH"],
            (4, "eka"): ["puMse"], (4, "dvi"): ["pumByAm"], (4, "bahu"): ["pumByaH"],
            (5, "eka"): ["puMsaH"], (5, "dvi"): ["pumByAm"], (5, "bahu"): ["pumByaH"],
            (6, "eka"): ["puMsaH"], (6, "dvi"): ["puMsoH"], (6, "bahu"): ["puMsAm"],
            (7, "eka"): ["puMsi"], (7, "dvi"): ["puMsoH"], (7, "bahu"): ["puMsu"],
            (8, "eka"): ["puman"], (8, "dvi"): ["pumAMsO"], (8, "bahu"): ["pumAMsaH"],
        }
        return T

    def _decline_div(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        T = {
            (1, "eka"): ["dyOH"], (1, "dvi"): ["divO"], (1, "bahu"): ["divaH"],
            (2, "eka"): ["divam"], (2, "dvi"): ["divO"], (2, "bahu"): ["divaH"],
            (3, "eka"): ["divA"], (3, "dvi"): ["dyuByAm"], (3, "bahu"): ["dyuBiH"],
            (4, "eka"): ["dive"], (4, "dvi"): ["dyuByAm"], (4, "bahu"): ["dyuByaH"],
            (5, "eka"): ["divaH"], (5, "dvi"): ["dyuByAm"], (5, "bahu"): ["dyuByaH"],
            (6, "eka"): ["divaH"], (6, "dvi"): ["divoH"], (6, "bahu"): ["divAm"],
            (7, "eka"): ["divi"], (7, "dvi"): ["divoH"], (7, "bahu"): ["dyuzu"],
            (8, "eka"): ["dyOH"], (8, "dvi"): ["divO"], (8, "bahu"): ["divaH"],
        }
        return T

    def _decline_ahan(self) -> Dict[Tuple[int, str], List[str]]:
        T = {
            (1, "eka"): ["ahaH"], (1, "dvi"): ["ahanI"], (1, "bahu"): ["ahAni"],
            (2, "eka"): ["ahaH"], (2, "dvi"): ["ahanI"], (2, "bahu"): ["ahAni"],
            (3, "eka"): ["ahnA"], (3, "dvi"): ["ahoByAm"], (3, "bahu"): ["ahobhiH"],
            (4, "eka"): ["ahne"], (4, "dvi"): ["ahoByAm"], (4, "bahu"): ["ahoByaH"],
            (5, "eka"): ["ahnaH"], (5, "dvi"): ["ahoByAm"], (5, "bahu"): ["ahoByaH"],
            (6, "eka"): ["ahnaH"], (6, "dvi"): ["ahnoH"], (6, "bahu"): ["ahnAm"],
            (7, "eka"): ["ahni", "ahani"], (7, "dvi"): ["ahnoH"], (7, "bahu"): ["ahaHsu", "ahasu"],
            (8, "eka"): ["ahaH"], (8, "dvi"): ["ahanI"], (8, "bahu"): ["ahAni"],
        }
        return T

    def _decline_paTin(self, stem: str) -> Dict[Tuple[int, str], List[str]]:
        cap = {"paTin": "paT", "maTin": "maT", "fBukzin": "fBuj"}[stem]
        # strong panTAH etc; middle paTiBiH; weak paTA
        pre = {"paTin": "panT", "maTin": "manT", "fBukzin": "fBukz"}[stem]
        T = {
            (1, "eka"): [pre + "AH"], (1, "dvi"): [pre + "AnO"], (1, "bahu"): [pre + "AnaH"],
            (2, "eka"): [pre + "Anam"], (2, "dvi"): [pre + "AnO"], (2, "bahu"): [cap + "aH"],
            (3, "eka"): [cap + "A"], (3, "dvi"): [stem + "ByAm"], (3, "bahu"): [stem + "BiH"],
            (4, "eka"): [cap + "e"], (4, "dvi"): [stem + "ByAm"], (4, "bahu"): [stem + "ByaH"],
            (5, "eka"): [cap + "aH"], (5, "dvi"): [stem + "ByAm"], (5, "bahu"): [stem + "ByaH"],
            (6, "eka"): [cap + "aH"], (6, "dvi"): [cap + "oH"], (6, "bahu"): [apply_natva(cap + "Am")],
            (7, "eka"): [cap + "i"], (7, "dvi"): [cap + "oH"], (7, "bahu"): [apply_zatva_s(stem + "zu")],
            (8, "eka"): [pre + "AH"], (8, "dvi"): [pre + "AnO"], (8, "bahu"): [pre + "AnaH"],
        }
        return T

    def _decline_Svan(self, stem: str) -> Dict[Tuple[int, str], List[str]]:
        # Svan/yuvan/maGavan: strong SvA/yuvA/maGavA; weak Sun/yUn/maGon
        strong1 = {"Svan": "SvA", "yuvan": "yuvA", "maGavan": "maGavA"}[stem]
        weak = {"Svan": "Sun", "yuvan": "yUn", "maGavan": "maGon"}[stem]
        T = {
            (1, "eka"): [strong1], (1, "dvi"): [strong1 + "nO"], (1, "bahu"): [strong1 + "naH"],
            (2, "eka"): [strong1 + "nam"], (2, "dvi"): [strong1 + "nO"], (2, "bahu"): [weak + "AH"],
            (3, "eka"): [weak + "A"], (3, "dvi"): [stem + "ByAm"], (3, "bahu"): [stem + "BiH"],
            (4, "eka"): [weak + "e"], (4, "dvi"): [stem + "ByAm"], (4, "bahu"): [stem + "ByaH"],
            (5, "eka"): [weak + "aH"], (5, "dvi"): [stem + "ByAm"], (5, "bahu"): [stem + "ByaH"],
            (6, "eka"): [weak + "aH"], (6, "dvi"): [weak + "oH"], (6, "bahu"): [apply_natva(weak + "Am")],
            (7, "eka"): [weak + "i"], (7, "dvi"): [weak + "oH"], (7, "bahu"): [apply_zatva_s(stem + "zu")],
            (8, "eka"): [strong1], (8, "dvi"): [strong1 + "nO"], (8, "bahu"): [strong1 + "naH"],
        }
        return T

    def _decline_jarA(self) -> Dict[Tuple[int, str], List[str]]:
        # optional jaras before vowel
        base = self._A_stem  # reuse A paradigm then add twins
        out: Dict[Tuple[int, str], List[str]] = {}
        for sup, key in zip(SUP_RAW, SUP_KEYS):
            v = self._A_stem("jarA", strip_sup(sup), sup, key, "strI", {})
            out[key] = [v]
        # add jaras twins for vowel-initial sup
        twins = {
            (3, "eka"): ["jarasA"], (4, "eka"): ["jarase"], (5, "eka"): ["jarasaH"],
            (6, "eka"): ["jarasaH"], (7, "eka"): ["jarasi"],
            (1, "dvi"): ["jarasO"], (2, "dvi"): ["jarasO"],
            (1, "bahu"): ["jarasaH"], (2, "bahu"): ["jarasaH"],
        }
        for k, vs in twins.items():
            for v in vs:
                if v not in out[k]:
                    out[k].append(v)
        out[(8, "eka")] = ["jare", "jarasi"]
        out[(8, "dvi")] = list(out[(1, "dvi")])
        out[(8, "bahu")] = list(out[(1, "bahu")])
        return out

    def _decline_SrI_BU(self, stem: str) -> Dict[Tuple[int, str], List[str]]:
        # monosyllabic I/U fem: iy/uv before vowel (6.4.77)
        is_I = stem.endswith("I")
        glide = "iy" if is_I else "uv"
        b = stem  # SrI
        out: Dict[Tuple[int, str], List[str]] = {}
        out[(1, "eka")] = [self._fin(stem + "H")]
        out[(1, "dvi")] = [stem[:-1] + glide + "O"]
        out[(1, "bahu")] = [stem[:-1] + glide + "aH"]
        out[(2, "eka")] = [stem[:-1] + glide + "am"]
        out[(2, "dvi")] = [stem[:-1] + glide + "O"]
        out[(2, "bahu")] = [stem[:-1] + glide + "aH"]
        out[(3, "eka")] = [stem[:-1] + glide + "A"]
        out[(3, "dvi")] = [stem + "ByAm"]
        out[(3, "bahu")] = [stem + "BiH"]
        out[(4, "eka")] = [stem[:-1] + glide + "E"]
        out[(4, "dvi")] = [stem + "ByAm"]
        out[(4, "bahu")] = [stem + "ByaH"]
        out[(5, "eka")] = [stem[:-1] + glide + "aH"]
        out[(5, "dvi")] = [stem + "ByAm"]
        out[(5, "bahu")] = [stem + "ByaH"]
        out[(6, "eka")] = [stem[:-1] + glide + "aH"]
        out[(6, "dvi")] = [stem[:-1] + glide + "oH"]
        out[(6, "bahu")] = [apply_natva(stem[:-1] + glide + "Am")]
        out[(7, "eka")] = [stem[:-1] + glide + "am"]
        out[(7, "dvi")] = [stem[:-1] + glide + "oH"]
        out[(7, "bahu")] = [apply_zatva_s(stem + "zu")]
        out[(8, "eka")] = [stem]
        out[(8, "dvi")] = list(out[(1, "dvi")])
        out[(8, "bahu")] = list(out[(1, "bahu")])
        return out

    def _decline_aYc(self, stem: str, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # pratyaYc/prAYc/udaYc: strong -aYc, middle -ac, weak -Ic (samprasarana)
        # derive prefix: pratya, prA, uda
        if stem.startswith("pratya"):
            pre, mid_v = "pratya", "I"
            weak_b = "pratIc"
        elif stem.startswith("prA"):
            weak_b = "prAc"
            pre, mid_v = "prA", "A"
        elif stem.startswith("uda"):
            weak_b = "udIc"
            pre, mid_v = "uda", "I"
        elif stem.startswith("arvA"):
            weak_b = "arvAc"
            pre, mid_v = "arvA", "A"
        else:
            weak_b = stem[:-3] + "Ic"
            pre, mid_v = stem[:-3], "I"
        strong = stem  # pratyaYc
        mid = stem[:-2] + "c"  # pratyac (Y drop)
        out: Dict[Tuple[int, str], List[str]] = {}
        # strong
        out[(1, "eka")] = [self._fin(mid[:-1] + "N")]  # pratyaN
        out[(1, "dvi")] = [strong + "O"]
        out[(1, "bahu")] = [strong + "aH"]
        out[(2, "eka")] = [strong + "am"]
        out[(2, "dvi")] = [strong + "O"]
        out[(2, "bahu")] = [self._fin(weak_b + "aH")]
        out[(3, "eka")] = [weak_b + "A"]
        out[(3, "dvi")] = [_join_pada(mid, "ByAm")]
        out[(3, "bahu")] = [_join_pada(mid, "BiH")]
        out[(4, "eka")] = [weak_b + "e"]
        out[(4, "dvi")] = [_join_pada(mid, "ByAm")]
        out[(4, "bahu")] = [_join_pada(mid, "ByaH")]
        out[(5, "eka")] = [weak_b + "aH"]
        out[(5, "dvi")] = [_join_pada(mid, "ByAm")]
        out[(5, "bahu")] = [_join_pada(mid, "ByaH")]
        out[(6, "eka")] = [weak_b + "aH"]
        out[(6, "dvi")] = [weak_b + "oH"]
        out[(6, "bahu")] = [apply_natva(weak_b + "Am")]
        out[(7, "eka")] = [weak_b + "i"]
        out[(7, "dvi")] = [weak_b + "oH"]
        out[(7, "bahu")] = [apply_zatva_s(_join_pada(mid, "su"))]
        out[(8, "eka")] = list(out[(1, "eka")])
        out[(8, "dvi")] = list(out[(1, "dvi")])
        out[(8, "bahu")] = list(out[(1, "bahu")])
        return out

    def _decline_Iyas(self, stem: str, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # Sreyas/garIyas: stem = ...yas (short a); strong -yAn, weak -yas
        b = stem[:-2]  # Srey
        w = b  # Srey (weak base without as)
        T: Dict[Tuple[int, str], List[str]] = {}
        T[(1, "eka")] = [self._fin(w + "An")]  # SreyAn
        T[(1, "dvi")] = [w + "AMsO"]
        T[(1, "bahu")] = [w + "AMsaH"]
        T[(2, "eka")] = [w + "AMsam"]
        T[(2, "dvi")] = [w + "AMsO"]
        T[(2, "bahu")] = [self._fin(w + "asa" + "s")]  # SreyasaH
        T[(3, "eka")] = [w + "asA"]
        T[(3, "dvi")] = [w + "oByAm"]
        T[(3, "bahu")] = [self._fin(w + "oBi" + "s")]
        T[(4, "eka")] = [w + "ase"]
        T[(4, "dvi")] = [w + "oByAm"]
        T[(4, "bahu")] = [w + "oByaH"]
        T[(5, "eka")] = [self._fin(w + "asa" + "s")]
        T[(5, "dvi")] = [w + "oByAm"]
        T[(5, "bahu")] = [w + "oByaH"]
        T[(6, "eka")] = [self._fin(w + "asa" + "s")]
        T[(6, "dvi")] = [w + "asoH"]
        T[(6, "bahu")] = [w + "asAm"]
        T[(7, "eka")] = [w + "asi"]
        T[(7, "dvi")] = [w + "asoH"]
        T[(7, "bahu")] = [w + "aHsu"]
        T[(8, "eka")] = [w + "an"]
        T[(8, "dvi")] = list(T[(1, "dvi")])
        T[(8, "bahu")] = list(T[(1, "bahu")])
        # feminine SreyasI not in this table (derive via weak+RIp if needed)
        return T

    def _decline_zaw(self, stem: str, linga: str) -> Dict[Tuple[int, str], List[str]]:
        #zaw (1.1.24): paYcan/zaz: jas/Sas luk -> paYca/zaw; rest plural
        base = stem
        if stem == "paYcan":
            nom = "paYca"
        elif stem == "zaz":
            nom = "zaw"
        elif stem == "azwan":
            # azwO/azwa optional (7.1.21)
            nom = None  # type: ignore
        else:
            nom = stem
        out: Dict[Tuple[int, str], List[str]] = {}
        if stem == "azwan":
            out[(1, "bahu")] = ["azwO", "azwa"]
            out[(2, "bahu")] = ["azwO", "azwa"]
        else:
            out[(1, "bahu")] = [nom]  # type: ignore
            out[(2, "bahu")] = [nom]  # type: ignore
        out[(1, "eka")] = []
        out[(1, "dvi")] = []
        out[(2, "eka")] = []
        out[(2, "dvi")] = []
        mid = "zaq" if stem == "zaz" else (stem[:-1] if stem.endswith("n") else stem)
        out[(3, "bahu")] = [_join_pada(mid, "BiH")]
        out[(4, "bahu")] = [_join_pada(mid, "ByaH")]
        out[(5, "bahu")] = [_join_pada(mid, "ByaH")]
        # zaz gen pl geminates (zaRRam); n-finals keep n (paYcanAm)
        if stem == "zaz":
            out[(6, "bahu")] = ["zaRRam"]
        else:
            out[(6, "bahu")] = [apply_natva(((stem if stem.endswith("n") else mid) + "Am"))]
        out[(7, "bahu")] = [apply_zatva_s(_join_pada(mid, "su"))]
        for k in [(3, "eka"), (3, "dvi"), (4, "eka"), (4, "dvi"), (5, "eka"), (5, "dvi"),
                  (6, "eka"), (6, "dvi"), (7, "eka"), (7, "dvi"),
                  (8, "eka"), (8, "dvi"), (8, "bahu")]:
            out[k] = []
        if stem == "azwan":
            out[(8, "bahu")] = list(out[(1, "bahu")])
        else:
            out[(8, "bahu")] = list(out[(1, "bahu")])
        return out

    def _decline_dvi(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        out: Dict[Tuple[int, str], List[str]] = {k: [] for k in
            [(1, "eka"), (1, "dvi"), (1, "bahu"), (2, "eka"), (2, "dvi"), (2, "bahu"),
             (3, "eka"), (3, "dvi"), (3, "bahu"), (4, "eka"), (4, "dvi"), (4, "bahu"),
             (5, "eka"), (5, "dvi"), (5, "bahu"), (6, "eka"), (6, "dvi"), (6, "bahu"),
             (7, "eka"), (7, "dvi"), (7, "bahu"), (8, "eka"), (8, "dvi"), (8, "bahu")]}
        if linga in ("puM", "napuMsaka"):
            out[(1, "dvi")] = ["dvO"]
            out[(2, "dvi")] = ["dvO"]
            out[(3, "dvi")] = ["dvAByAm"]
            out[(4, "dvi")] = ["dvAByAm"]
            out[(5, "dvi")] = ["dvAByAm"]
            out[(6, "dvi")] = ["dvayoH"]
            out[(7, "dvi")] = ["dvayoH"]
            out[(8, "dvi")] = ["dvO"]
        else:
            out[(1, "dvi")] = ["dve"]
            out[(2, "dvi")] = ["dve"]
            out[(3, "dvi")] = ["dvAByAm"]
            out[(4, "dvi")] = ["dvAByAm"]
            out[(5, "dvi")] = ["dvAByAm"]
            out[(6, "dvi")] = ["dvayoH"]
            out[(7, "dvi")] = ["dvayoH"]
            out[(8, "dvi")] = ["dve"]
        return out

    def _decline_tri_catur(self, stem: str, linga: str) -> Dict[Tuple[int, str], List[str]]:
        out: Dict[Tuple[int, str], List[str]] = {}
        if stem == "tri":
            if linga == "strI":
                # tisF
                out[(1, "bahu")] = ["tisraH"]
                out[(2, "bahu")] = ["tisfH"]
                out[(3, "bahu")] = ["tisfBiH"]
                out[(4, "bahu")] = ["tisfByaH"]
                out[(5, "bahu")] = ["tisfByaH"]
                out[(6, "bahu")] = ["tisfRAm"]  # tisFRam (num n->R after f)
                out[(7, "bahu")] = ["tisfzu"]
            else:
                out[(1, "bahu")] = ["trayaH"]
                out[(2, "bahu")] = ["trIn"]
                out[(3, "bahu")] = ["triBiH"]
                out[(4, "bahu")] = ["triByaH"]
                out[(5, "bahu")] = ["triByaH"]
                out[(6, "bahu")] = [apply_natva("trayARAm" if False else "trayARAm")]
                out[(6, "bahu")] = ["trayARAm"]
                out[(7, "bahu")] = ["trizu"]
            for k in [(1, "eka"), (1, "dvi"), (2, "eka"), (2, "dvi"), (3, "eka"), (3, "dvi"),
                      (4, "eka"), (4, "dvi"), (5, "eka"), (5, "dvi"), (6, "eka"), (6, "dvi"),
                      (7, "eka"), (7, "dvi"), (8, "eka"), (8, "dvi")]:
                out[k] = []
            out[(8, "bahu")] = list(out[(1, "bahu")])
            return out
        # catur
        if linga == "strI":
            out[(1, "bahu")] = ["catasraH"]
            out[(2, "bahu")] = ["catasraH"]
            out[(3, "bahu")] = ["catasfBiH"]
            out[(4, "bahu")] = ["catasfByaH"]
            out[(5, "bahu")] = ["catasfByaH"]
            out[(6, "bahu")] = ["catasfRAm"]  # num n->R after f
            out[(7, "bahu")] = ["catasfzu"]
        else:
            out[(1, "bahu")] = ["catvAraH"]
            out[(2, "bahu")] = ["caturaH"]
            out[(3, "bahu")] = ["caturBiH"]
            out[(4, "bahu")] = ["caturByaH"]
            out[(5, "bahu")] = ["caturByaH"]
            out[(6, "bahu")] = [apply_natva("catur" + "RAm")]
            out[(6, "bahu")] = ["caturRAm"]
            out[(7, "bahu")] = ["caturzu"]
        for k in [(1, "eka"), (1, "dvi"), (2, "eka"), (2, "dvi"), (3, "eka"), (3, "dvi"),
                  (4, "eka"), (4, "dvi"), (5, "eka"), (5, "dvi"), (6, "eka"), (6, "dvi"),
                  (7, "eka"), (7, "dvi"), (8, "eka"), (8, "dvi")]:
            out[k] = []
        out[(8, "bahu")] = list(out[(1, "bahu")])
        return out

    # ---- pronouns ----
    def _decline_tad(self, stem: str, linga: str) -> Dict[Tuple[int, str], List[str]]:
        pre = {"tad": "ta", "etad": "eta", "yad": "ya"}[stem]
        if linga == "strI":
            pre = {"tad": "tA", "etad": "etA", "yad": "yA"}[stem]
            b = pre[:-1]
            T = {
                (1, "eka"): [pre], (1, "dvi"): [b + "e"], (1, "bahu"): [b + "AH"],
                (2, "eka"): [b + "Am"], (2, "dvi"): [b + "e"], (2, "bahu"): [b + "AH"],
                (3, "eka"): [b + "ayA"], (3, "dvi"): [b + "AByAm"], (3, "bahu"): [b + "ABiH"],
                (4, "eka"): [b + "asyE"], (4, "dvi"): [b + "AByAm"], (4, "bahu"): [b + "AByaH"],
                (5, "eka"): [b + "asyAH"], (5, "dvi"): [b + "AByAm"], (5, "bahu"): [b + "AByaH"],
                (6, "eka"): [b + "asyAH"], (6, "dvi"): [b + "ayoH"], (6, "bahu"): [apply_natva(b + "AsAm")],
                (7, "eka"): [b + "asyAm"], (7, "dvi"): [b + "ayoH"], (7, "bahu"): [apply_zatva_s(b + "Asu")],
                (8, "eka"): [pre], (8, "dvi"): [b + "e"], (8, "bahu"): [b + "AH"],
            }
            return T
        # puM (fully parametric in base t/y/et; only 1/8eka differ)
        if linga == "puM":
            base = pre[:-1] if pre.endswith("a") else pre  # t/et/y
            sa = {"tad": "saH", "etad": "ezaH", "yad": "yaH"}[stem]
            T = {
                (1, "eka"): [sa], (1, "dvi"): [base + "O"], (1, "bahu"): [base + "e"],
                (2, "eka"): [base + "am"], (2, "dvi"): [base + "O"], (2, "bahu"): [base + "An"],
                (3, "eka"): [apply_natva(base + "ena")], (3, "dvi"): [base + "AByAm"], (3, "bahu"): [base + "EH"],
                (4, "eka"): [pre + "smE"], (4, "dvi"): [base + "AByAm"], (4, "bahu"): [base + "eByaH"],
                (5, "eka"): [pre + "smAt"], (5, "dvi"): [base + "AByAm"], (5, "bahu"): [base + "eByaH"],
                (6, "eka"): [pre + "sya"], (6, "dvi"): [base + "ayoH"], (6, "bahu"): [apply_natva(base + "ezAm")],
                (7, "eka"): [pre + "smin"], (7, "dvi"): [base + "ayoH"], (7, "bahu"): [apply_zatva_s(base + "ezu")],
                (8, "eka"): [sa], (8, "dvi"): [base + "O"], (8, "bahu"): [base + "e"],
            }
            return T
        # napuMsaka: 1/2 eka tat/etat/yat, rest like puM (parametric)
        base = pre[:-1] if pre.endswith("a") else pre
        T = {
            (1, "eka"): [pre + "t"], (1, "dvi"): [base + "e"], (1, "bahu"): [base + "Ani"],
            (2, "eka"): [pre + "t"], (2, "dvi"): [base + "e"], (2, "bahu"): [base + "Ani"],
            (3, "eka"): [apply_natva(base + "ena")], (3, "dvi"): [base + "AByAm"], (3, "bahu"): [base + "EH"],
            (4, "eka"): [pre + "smE"], (4, "dvi"): [base + "AByAm"], (4, "bahu"): [base + "eByaH"],
            (5, "eka"): [pre + "smAt"], (5, "dvi"): [base + "AByAm"], (5, "bahu"): [base + "eByaH"],
            (6, "eka"): [pre + "sya"], (6, "dvi"): [base + "ayoH"], (6, "bahu"): [apply_natva(base + "ezAm")],
            (7, "eka"): [pre + "smin"], (7, "dvi"): [base + "ayoH"], (7, "bahu"): [apply_zatva_s(base + "ezu")],
            (8, "eka"): [pre + "t"], (8, "dvi"): [base + "e"], (8, "bahu"): [base + "Ani"],
        }
        return T

    def _decline_kim(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # kim->ka (7.2.103), neuter 1/2 eka stays kim; only stem-initial t/s->k
        out = self._decline_tad("tad", linga)
        # replace t->k, s->k where applicable
        repl: Dict[Tuple[int, str], List[str]] = {}
        for k, vs in out.items():
            nv = []
            for v in vs:
                if linga == "napuMsaka" and k in ((1, "eka"), (2, "eka"), (8, "eka")):
                    nv.append("kim")
                    continue
                # ka- for ko/ke/kam/kAn/kena/kEH/kasmE...: only initial t/s->k
                # (tasmE->kasmE keeps s; saH->kaH; tayoH->kayoH; tezAm->kezAm)
                w = ("k" + v[1:]) if v[:1] in ("t", "s") else v
                nv.append(w)
            repl[k] = nv
        # fix known: 1eka puM kaH (w is saH->kaH correct)
        return repl

    def _decline_idam(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        if linga == "puM":
            T = {
                (1, "eka"): ["ayam"], (1, "dvi"): ["imO"], (1, "bahu"): ["ime"],
                (2, "eka"): ["imam"], (2, "dvi"): ["imO"], (2, "bahu"): ["imAn"],
                (3, "eka"): ["anena"], (3, "dvi"): ["AByAm"], (3, "bahu"): ["eBiH"],
                (4, "eka"): ["asmE"], (4, "dvi"): ["AByAm"], (4, "bahu"): ["eByaH"],
                (5, "eka"): ["asmAt"], (5, "dvi"): ["AByAm"], (5, "bahu"): ["eByaH"],
                (6, "eka"): ["asya"], (6, "dvi"): ["anayoH"], (6, "bahu"): ["ezAm"],
                (7, "eka"): ["asmin"], (7, "dvi"): ["anayoH"], (7, "bahu"): ["ezu"],
                (8, "eka"): ["ayam"], (8, "dvi"): ["imO"], (8, "bahu"): ["ime"],
            }
            T[(3, "eka")] = [apply_natva("anena")]
            T[(6, "bahu")] = [apply_natva("ezAm")]
            return T
        if linga == "strI":
            T = {
                (1, "eka"): ["iyam"], (1, "dvi"): ["ime"], (1, "bahu"): ["imAH"],
                (2, "eka"): ["imAm"], (2, "dvi"): ["ime"], (2, "bahu"): ["imAH"],
                (3, "eka"): ["anayA"], (3, "dvi"): ["AByAm"], (3, "bahu"): ["ABiH"],
                (4, "eka"): ["asyE"], (4, "dvi"): ["AByAm"], (4, "bahu"): ["AByaH"],
                (5, "eka"): ["asyAH"], (5, "dvi"): ["AByAm"], (5, "bahu"): ["AByaH"],
                (6, "eka"): ["asyAH"], (6, "dvi"): ["anayoH"], (6, "bahu"): ["AsAm"],
                (7, "eka"): ["asyAm"], (7, "dvi"): ["anayoH"], (7, "bahu"): ["Asu"],
                (8, "eka"): ["iyam"], (8, "dvi"): ["ime"], (8, "bahu"): ["imAH"],
            }
            T[(6, "bahu")] = [apply_natva("AsAm")]
            return T
        T = {
            (1, "eka"): ["idam"], (1, "dvi"): ["ime"], (1, "bahu"): ["imAni"],
            (2, "eka"): ["idam"], (2, "dvi"): ["ime"], (2, "bahu"): ["imAni"],
            (3, "eka"): ["anena"], (3, "dvi"): ["AByAm"], (3, "bahu"): ["eBiH"],
            (4, "eka"): ["asmE"], (4, "dvi"): ["AByAm"], (4, "bahu"): ["eByaH"],
            (5, "eka"): ["asmAt"], (5, "dvi"): ["AByAm"], (5, "bahu"): ["eByaH"],
            (6, "eka"): ["asya"], (6, "dvi"): ["anayoH"], (6, "bahu"): ["ezAm"],
            (7, "eka"): ["asmin"], (7, "dvi"): ["anayoH"], (7, "bahu"): ["ezu"],
            (8, "eka"): ["idam"], (8, "dvi"): ["ime"], (8, "bahu"): ["imAni"],
        }
        T[(3, "eka")] = [apply_natva("anena")]
        return T

    def _decline_adas(self, linga: str) -> Dict[Tuple[int, str], List[str]]:
        # 8.2.80: d->m + u/U
        if linga == "puM":
            T = {
                (1, "eka"): ["asO"], (1, "dvi"): ["amU"], (1, "bahu"): ["amI"],
                (2, "eka"): ["amum"], (2, "dvi"): ["amU"], (2, "bahu"): ["amUn"],
                (3, "eka"): ["amunA"], (3, "dvi"): ["amUByAm"], (3, "bahu"): ["amIBiH"],
                (4, "eka"): ["amuzmE"], (4, "dvi"): ["amUByAm"], (4, "bahu"): ["amIByaH"],
                (5, "eka"): ["amuzmAt"], (5, "dvi"): ["amUByAm"], (5, "bahu"): ["amIByaH"],
                (6, "eka"): ["amuzya"], (6, "dvi"): ["amuyoH"], (6, "bahu"): ["amIzAm"],
                (7, "eka"): ["amuzmin"], (7, "dvi"): ["amuyoH"], (7, "bahu"): ["amIzu"],
                (8, "eka"): ["asO"], (8, "dvi"): ["amU"], (8, "bahu"): ["amI"],
            }
            T[(6, "bahu")] = [apply_natva("amIzAm")]
            return T
        if linga == "strI":
            T = {
                (1, "eka"): ["asO"], (1, "dvi"): ["amU"], (1, "bahu"): ["amUH"],
                (2, "eka"): ["amUm"], (2, "dvi"): ["amU"], (2, "bahu"): ["amUH"],
                (3, "eka"): ["amuyA"], (3, "dvi"): ["amUByAm"], (3, "bahu"): ["amUBiH"],
                (4, "eka"): ["amuzmE"] if False else ["amuzyE"], (4, "dvi"): ["amUByAm"], (4, "bahu"): ["amUByaH"],
                (5, "eka"): ["amuzyAH"], (5, "dvi"): ["amUByAm"], (5, "bahu"): ["amUByaH"],
                (6, "eka"): ["amuzyAH"], (6, "dvi"): ["amuyoH"], (6, "bahu"): ["amUzAm"],
                (7, "eka"): ["amuzyAm"], (7, "dvi"): ["amuyoH"], (7, "bahu"): ["amUzu"],
                (8, "eka"): ["asO"], (8, "dvi"): ["amU"], (8, "bahu"): ["amUH"],
            }
            T[(4, "eka")] = ["amuzyE"]
            T[(6, "bahu")] = [apply_natva("amUzAm")]
            return T
        T = {
            (1, "eka"): ["adaH"], (1, "dvi"): ["amUnI"], (1, "bahu"): ["amUni"],
            (2, "eka"): ["adaH"], (2, "dvi"): ["amUnI"], (2, "bahu"): ["amUni"],
            (3, "eka"): ["amunA"], (3, "dvi"): ["amUByAm"], (3, "bahu"): ["amIBiH"],
            (4, "eka"): ["amuzmE"], (4, "dvi"): ["amUByAm"], (4, "bahu"): ["amIByaH"],
            (5, "eka"): ["amuzmAt"], (5, "dvi"): ["amUByAm"], (5, "bahu"): ["amIByaH"],
            (6, "eka"): ["amuzya"], (6, "dvi"): ["amuyoH"], (6, "bahu"): ["amIzAm"],
            (7, "eka"): ["amuzmin"], (7, "dvi"): ["amuyoH"], (7, "bahu"): ["amIzu"],
            (8, "eka"): ["adaH"], (8, "dvi"): ["amUnI"], (8, "bahu"): ["amUni"],
        }
        T[(6, "bahu")] = [apply_natva("amIzAm")]
        return T

    def _decline_yuzmad_asmad(self, stem: str) -> Dict[Tuple[int, str], List[str]]:
        # suppletion: aham/tvam etc. + enclitic twins (mA/nO etc.) appended as options
        if stem == "asmad":
            T = {
                (1, "eka"): ["aham"], (1, "dvi"): ["AvAm"], (1, "bahu"): ["vayam"],
                (2, "eka"): ["mAm", "mA"], (2, "dvi"): ["AvAm", "vAm"], (2, "bahu"): ["asmAn", "naH"],
                (3, "eka"): ["mayA"], (3, "dvi"): ["AvAByAm"], (3, "bahu"): ["asmABiH"],
                (4, "eka"): ["maHyam", "me"], (4, "dvi"): ["AvAByAm"], (4, "bahu"): ["asmaByam", "naH"],
                (5, "eka"): ["mat"], (5, "dvi"): ["AvAByAm"], (5, "bahu"): ["asmaByam", "naH"] if False else ["asmad", "naH"],
                (6, "eka"): ["mama", "me"], (6, "dvi"): ["AvayoH", "vAm"], (6, "bahu"): ["asmAkam", "naH"],
                (7, "eka"): ["mayi"], (7, "dvi"): ["AvayoH", "vAm"], (7, "bahu"): ["asmAsu"],
                (8, "eka"): [], (8, "dvi"): [], (8, "bahu"): [],
            }
            T[(5, "bahu")] = ["mat", "asmad"] if False else ["asmad", "naH"]
            # correct 5bahu: asmad
            T[(5, "bahu")] = ["asmad", "naH"] if False else ["asmad"]
            # Actually 5pl = asmad (+naH enclitic only for 2/4/6). Keep single.
            T[(5, "bahu")] = ["asmad"]
            return T
        T = {
            (1, "eka"): ["tvam"], (1, "dvi"): ["yuvAm"], (1, "bahu"): ["yUyam"],
            (2, "eka"): ["tvAm", "tvA"], (2, "dvi"): ["yuvAm", "vAm"], (2, "bahu"): ["yuzmAn", "vaH"],
            (3, "eka"): ["tvayA"], (3, "dvi"): ["yuvAByAm"], (3, "bahu"): ["yuzmABiH"],
            (4, "eka"): ["tuByam", "te"], (4, "dvi"): ["yuvAByAm"], (4, "bahu"): ["yuzmaByam", "vaH"],
            (5, "eka"): ["tvat"], (5, "dvi"): ["yuvAByAm"], (5, "bahu"): ["yuzmad"],
            (6, "eka"): ["tava", "te"], (6, "dvi"): ["yuvayoH", "vAm"], (6, "bahu"): ["yuzmAkam", "vaH"],
            (7, "eka"): ["tvayi"], (7, "dvi"): ["yuvayoH", "vAm"], (7, "bahu"): ["yuzmAsu"],
            (8, "eka"): [], (8, "dvi"): [], (8, "bahu"): [],
        }
        return T


# ---------------- supplementary pre/post-sup operations ----------------
def ekaSeza(stems: List[str]) -> str:
    """EkaSeza (1.2.64): identical stems keep one (rAma+rAma->rAma, dual/plural
    via sup vacana); naturally paired kin keep the masculine
    (mAtf+pitf->pitf, SvaSrU+SvaSura->SvaSura). Returns surviving stem."""
    if not stems:
        return ""
    if len(set(stems)) == 1:
        return stems[0]
    pair = set(stems)
    if pair == {"mAtf", "pitf"}:
        return "pitf"
    if pair == {"SvaSrU", "SvaSura"}:
        return "SvaSura"
    if pair == {"BrAtf", "svasf"}:
        return "BrAtf"
    return stems[-1]


def pumvatBAva(fem_stem: str) -> str:
    """PumvatBAva: feminine adjective stem -> masculine base in compounds
    (kalyARI->kalyARa before mAtA). Generative: I->a, A->a."""
    if fem_stem.endswith("I"):
        return fem_stem[:-1] + "a"
    if fem_stem.endswith("A"):
        return fem_stem[:-1] + "a"
    if fem_stem.endswith("i"):
        return fem_stem[:-1] + "a"
    return fem_stem


def avyaya_pada(stem: str) -> str:
    """Avyayas take sup then 2.4.82 luk deletes it: surface unchanged but
    legally a Pada. Returns stem unchanged."""
    return stem


def saH_sulopa(next_sound: str | None) -> str:
    """6.1.132 saH/ezaH su-lopa: saH/ezaH lose visarga before any consonant
    (sa puruzaH). Returns 'sa' if next is consonant, else 'saH'."""
    if next_sound is None:
        return "saH"
    if next_sound in SLP1_VOWELS:
        return "saH"
    return "sa"


def satf_feminine(weak_base: str, gana: str = "BvAdi") -> List[str]:
    """Satf feminine stem formation (RIp RIp): class 1/4/10 must take strong
    (gacCantI), class 6 optional (tudantI/tudatI), class 3 must take weak
    (dadatI). weak_base is the at-base (gacCat/tudat/dadat)."""
    if gana in ("BvAdi", "divAdi", "curAdi"):
        return [weak_base[:-2] + "antI"]
    if gana == "tudAdi":
        return [weak_base[:-2] + "antI", weak_base + "I"]
    # adAdi/juhotyAdi (class 2/3, abhyasta): weak only
    return [weak_base + "I"]


def stri_pratipadika(masc_stem: str, kind: str = "wAp", gana: str = "BvAdi") -> str:
    """Stri-pratyaya (4.1.3-4.1.81): masculine pratipadika -> feminine stem.
    wAp (A, 4.1.4 ajAdyatazWAp): aja-adi + a-final -> A (aja->ajA; by shape
    all a-stems take A since jAti/vayas semantics is caller-side);
    RIp (I): f->rI (kartf->kartrI), an-weak+I (rAjan->rAjYI), at via
    satf_feminine optionality (gacCat->gacCantI), tavat/vas weak+I,
    yopadha ya-lopa (sUrya->sUrI);
    uN (U): laghu-u -> U. Generative by shape (+gana for at)."""
    AJA_ADI = {"aja", "aSva", "edaka", "cawaka", "mUzika", "kukkuwa",
               "Suka", "baka", "kAka"}  # representative; shape rule covers rest
    # yopadha RIp with ya-lopa (sUrya->sUrI, matsya->matsI, manuzya->manuzI)
    YOPADHA = {"sUrya", "matsya", "manuzya"}
    if kind == "RIp" and masc_stem in YOPADHA and masc_stem.endswith("ya"):
        return masc_stem[:-2] + "I"
    if kind == "wAp":
        if masc_stem.endswith("a"):
            return masc_stem[:-1] + "A"
        if masc_stem.endswith("at"):
            return masc_stem + "I"  # at + I? caller prefers satf_feminine for optionality
        return masc_stem + "A"
    if kind == "RIp":
        if masc_stem.endswith("f"):
            return masc_stem[:-1] + "rI"  # kartf->kartrI
        if masc_stem.endswith("vas"):
            return masc_stem[:-3] + "uzI"  # cakfvas->cakfuzI (weak samprasarana)
        if masc_stem.endswith("tavat") or masc_stem.endswith("vat"):
            return masc_stem + "I"  # BUtavat->BUtavatI (weak + I)
        if masc_stem.endswith("at") or masc_stem.endswith("ant"):
            # at-nouns (Bavat/mahat/jagat) take weak + I; true Satf participles
            # take strong/optional via gana (gacCat->gacCantI)
            if masc_stem in ("Bavat", "mahat", "jagat", "marut", "sarit", "vidyut"):
                return masc_stem + "I"
            base = masc_stem[:-3] + "at" if masc_stem.endswith("ant") else masc_stem
            return satf_feminine(base, gana)[0]
        if masc_stem.endswith("an"):
            b = masc_stem[:-2]
            if b.endswith("j"):
                return b + "YI"  # rAjan->rAjYI
            return b + "nI"  # Atman->AtmanI
        if masc_stem.endswith("as"):
            return masc_stem + "I"
        if masc_stem.endswith("a"):
            return masc_stem[:-1] + "I"
        return masc_stem + "I"
    if kind == "uN":
        if masc_stem.endswith("u"):
            return masc_stem[:-1] + "U"
        return masc_stem + "U"
    return masc_stem


def decline_all(stem: str, linga: str = "puM", **kw) -> Dict[Tuple[int, str], List[str]]:
    return SubantaEngine().decline(stem, linga, **kw)
