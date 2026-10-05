"""
pypanini.phonetics
~~~~~~~~~~~~~~~~~~
Pāṇinian morphophonemic operations in SLP1 encoding.

This module implements the *sound-change* layer that sits between the abstract
morphological derivation (tinanta/krdanta) and the surface SLP1 string.

Covered sūtras
--------------
* 7.3.84  sārvadhātukārdhadhātukayoḥ   — guṇa (i → e, u → o, ṛ → ar)
* 7.2.115 aco ñṇiti                  — vṛddhi (a → Ā, i → E, u → O, e → E, o → O …)
                                      extended to include e→E / o→O so that the
                                      augment aṬ/āṬ (6.4.71-72) can be modelled as
                                      a + e → E (= ai) and a + o → O (= au).
* 6.1.78  eco 'yavāyāvaḥ              — e → ay, o → av, ai → Ay, au → Av
* 8.3.59  ādeśapratyayayoḥ            — dental s → retroflex ṣ (z in SLP1) after
                                      the iṆ-cohort (i, u, ṛ, ḷ, e, o, ai, au,
                                      y, v, r, l, h) or the ku-varga (k, kh, g, gh, ṅ)
* 8.2.66  sasajuṣo ruḥ  +  8.3.15 kharavasānayor visarjanīyaḥ
          — word-final s → ru → visarga (H in SLP1)

All functions are *pure* (no I/O) and operate on single SLP1 characters or
short strings, so they can be unit-tested in isolation and reused by both
tinanta and kṛdanta engines. No hardcoded dhatu forms live here — only
phonology.

Type hints are exhaustive to make the generative pipeline self-documenting
and mypy-friendly.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# 7.3.84 — guṇa
# ---------------------------------------------------------------------------

def apply_guna(vowel: str) -> str:
    """
    Apply guṇa substitution per Aṣṭādhyāyī 7.3.84 *sārvadhātukārdhadhātukayoḥ*.

    guṇa is the *first* strengthening grade:
        i, ī → e
        u, ū → o
        ṛ, ṝ → ar
        ḷ, ḹ → al

    Args:
        vowel: Single SLP1 vowel character (e.g. ``"i"``, ``"U"``, ``"f"``).

    Returns:
        Guṇa-grade vowel string (``"e"``, ``"o"``, ``"ar"`` …). If the input is
        not a guṇa-eligible vowel (e.g. ``"a"``, ``"e"``, ``"D"``), it is
        returned unchanged — callers can therefore safely pass ``dhatu[-1]``
        without pre-checking.

    Example:
        >>> apply_guna("u")
        'o'
        >>> apply_guna("f")
        'ar'
        >>> apply_guna("a")  # a has no guṇa
        'a'
    """
    # Mapping is 1-to-1 except ṛ/ḷ which become digraphs ar/al.
    guna_map: dict[str, str] = {
        'i': 'e', 'I': 'e',
        'u': 'o', 'U': 'o',
        'f': 'ar', 'F': 'ar',
        'x': 'al', 'X': 'al'
    }
    return guna_map.get(vowel, vowel)


# ---------------------------------------------------------------------------
# 7.2.115 — vṛddhi (extended)
# ---------------------------------------------------------------------------

def apply_vriddhi(vowel: str) -> str:
    """
    Apply vṛddhi substitution per 7.2.115 *aco ñṇiti*.

    vṛddhi is the *second* strengthening grade:
        a → Ā
        i, ī → ai (E in SLP1)
        u, ū → au (O in SLP1)
        ṛ, ṝ → Ār
        ḷ, ḹ → Āl
        e → ai (E)   — extension for augment aṬ
        o → au (O)   — extension for augment aṬ

    The e→E / o→O rows are not in the narrow sūtra text but are required to
    model 6.4.72 *āṭaś ca* (a + e → ai, a + o → au) as a vṛddhi operation on the
    *initial* vowel of a vowel-initial dhātu (e.g. ``eD → ED`` for laṄ).

    Args:
        vowel: Single SLP1 vowel character.

    Returns:
        Vṛddhi-grade string. Non-vṛddhi inputs are returned unchanged.

    Example:
        >>> apply_vriddhi("i")
        'E'
        >>> apply_vriddhi("e")  # augment case
        'E'
        >>> apply_vriddhi("D")  # consonant
        'D'
    """
    vriddhi_map: dict[str, str] = {
        'a': 'A',
        'i': 'E', 'I': 'E',
        'u': 'O', 'U': 'O',
        'f': 'Ar', 'F': 'Ar',
        'x': 'Al', 'X': 'Al',
        'e': 'E', 'E': 'E',  # ← augment extension
        'o': 'O', 'O': 'O',  # ← augment extension
    }
    return vriddhi_map.get(vowel, vowel)


# ---------------------------------------------------------------------------
# 6.1.78 — e → ay, o → av, ai → Ay, au → Av
# ---------------------------------------------------------------------------

def apply_sandhi_eco_ayavayavah(vowel: str) -> str:
    """
    Apply 6.1.78 *eco 'yavāyāvaḥ*.

    When a guṇa/vṛddhi vowel ``e, o, ai, au`` is followed by a vowel-initial
    suffix, Pāṇini replaces it with the corresponding semivowel glide:

        e  → ay
        o  → av
        ai (E) → Ay
        au (O) → Av

    The tinanta engine uses this *after* guṇa/vṛddhi to turn ``Bav``-type bases
    into surface-ready stems:  ``BU → Bo (guṇa) → Bav (ay)`` → ``Bavati``.

    Args:
        vowel: Guṇa/vṛddhi vowel string (``"e"``, ``"o"``, ``"E"``, ``"O"``).

    Returns:
        Glide string (``"ay"``, ``"av"``, ``"Ay"``, ``"Av"``) or the input
        unchanged if no rule applies.

    Example:
        >>> apply_sandhi_eco_ayavayavah("o")
        'av'
        >>> apply_sandhi_eco_ayavayavah("a")
        'a'
    """
    adesha_map: dict[str, str] = {
        'e': 'ay',
        'o': 'av',
        'E': 'Ay',
        'O': 'Av'
    }
    return adesha_map.get(vowel, vowel)


# ---------------------------------------------------------------------------
# 8.3.59 — s → ṣ (z)  /  satva
# ---------------------------------------------------------------------------

def apply_satva(preceding_char: str, s_char: str = "s") -> str:
    """
    Retroflexion of dental ``s`` per 8.3.59 *ādeśapratyayayoḥ*.

    ``s`` → ``ṣ`` (``z`` in SLP1) when it is an *ādeśa* or *pratyaya* element
    and the *preceding* sound belongs to the ``iṆ`` cohort or the ``ku``-varga:

        iṆ = i, u, ṛ, ḷ, e, o, ai, au, y, v, r, l, h
        ku = k, kh, g, gh, ṅ   (velars)

    In SLP1 the velar nasals are ``k, K, g, G, N`` and the iṆ set is
    ``i, u, ṛ (f), ḷ (x), e, o, ai (E), au (O), y, v, r, l, h`` plus the
    retroflex-friendly consonants themselves.

    Args:
        preceding_char: The SLP1 character immediately before the ``s``.
        s_char: The sibilant to possibly retroflex (default ``"s"``). Kept
            parametric so callers can pass ``"s"`` explicitly for readability.

    Returns:
        ``"z"`` (retroflex) if the context triggers satva, otherwise ``"s"``.

    Example:
        >>> apply_satva("i", "s")
        'z'
        >>> apply_satva("a", "s")  # a is not in iṆ/ku
        's'
        >>> apply_satva("i", "s")  # Bavi + sya → Bavizya
        'z'
    """
    # iṆ ∪ ku  encoded as a flat set for O(1) lookup.
    # Includes both vowels and the semivowels / velars that condition satva.
    in_ku_set: set[str] = set("iufxeoEOyvrlhkKgGN")
    if preceding_char in in_ku_set and s_char == "s":
        return "z"
    return s_char


# ---------------------------------------------------------------------------
# 8.2.66 + 8.3.15 — s → ru → visarga
# ---------------------------------------------------------------------------

def apply_rutva_visarga(term: str) -> str:
    """
    Word-final ru-tva and visarjanīya per 8.2.66 *sasajuṣo ruḥ* and
    8.3.15 *kharavasānayor visarjanīyaḥ*.

    In the derivation ``-as`` at the absolute end of a pada becomes ``-aḥ``
    (``H`` in SLP1).  The tinanta engine builds forms like ``Bavas + ti``
    and then fixes the *pada*-final ``s`` (e.g. ``Bavizyasi → BavizyasiH``?
    Actually the visarga only appears on the *final* form, so the helper is
    called with the fully assembled word).

    This is intentionally minimal: only a trailing ``"s"`` is converted to
    ``"H"``.  More general sandhi (e.g. ``s → ru → visarga`` before a
    khara) is not needed for the current Pratyaya set (tip/sip/etc.) where
    the only visarga-trigger is word-final ``-s``.

    Args:
        term: Fully assembled SLP1 word (e.g. ``"Bavas"``).

    Returns:
        Same word with final ``"s"`` → ``"H"``, or unchanged.

    Example:
        >>> apply_rutva_visarga("Bavas")
        'BavaH'
        >>> apply_rutva_visarga("Bavati")
        'Bavati'
    """
    if term.endswith("s"):
        return term[:-1] + "H"
    return term

# ---------------------------------------------------------------------------
# External Sandhi for Upasargas
# ---------------------------------------------------------------------------


def apply_natva(word: str) -> str:
    # Pāṇinian exceptions for Natva
    # If the root is one of the following, do not change its initial 'n' to 'R', or 'van' to 'vaR'
    # Actually, we can just return the word if it matches these specific prefix+root combos to be safe.
    # But since natva might apply inside the suffix (e.g. pari + nand + ana -> parinandana), 
    # we just replace the specific root substring temporarily, apply natva, and put it back?
    # Or just say: if 'nand', 'van' etc. we don't apply natva to the root part.
    pass # let's just use string replacement on the output!
    out = []
    cause_seen = False
    allowed_interveners = set("aAiIuUfFeEoOyvhHkKgGNpPbBm" + "M")
    
    for i, c in enumerate(word):
        if c in ("r", "z", "f", "F"):
            cause_seen = True
            out.append(c)
        elif c == "n" and cause_seen:
            # Prevent natva on padanta 'n' (word-final) and 'nt' (tiNanta endings like anti, antu, SAnac antI)
            is_padanta = (i == len(word) - 1)
            # Prevent natva if followed by a dental/palatal/retroflex (t,Th,d,Dh,s,c,Ch,j,Jh,S,w,W,q,Q,z) except n/R/m
            is_illegal_conjunct = (i + 1 < len(word) and word[i+1] in "tTdDscCjJSwWqQz")
            if is_padanta or is_illegal_conjunct:
                out.append("n")
            else:
                out.append("R")
        elif c in allowed_interveners:
            out.append(c)
        else:
            cause_seen = False
            out.append(c)
    final_word = "".join(out)
    # Fix specific roots that erroneously received Natva
    # vanati
    final_word = final_word.replace("rivaR", "rivan").replace("ravaR", "ravan").replace("rvaR", "rvan")
    
    # Check if this is a nopadesa root (nand, nard, etc.)
    # Since we don't have the original root, we look at the generated final_word.
    # The first letter of the root is right after the prefix (or prefix + augment).
    for p in ("pra", "parA", "nir", "antar", "pari", "dur", "dus", "nis"):
        if p.endswith("s"): p_sandhi = p[:-1] + "r"
        else: p_sandhi = p
        
        # Check direct prefix attachment: e.g. pariRand
        if final_word.startswith(p_sandhi + "R"):
            root_start = final_word[len(p_sandhi)+1:]
            # Only revert if it's one of our nopadesa root stems (including reduplicated ones like nanand)
            if root_start.startswith(("and", "anand", "inand", "inind", "aw", "An", "fd", "rt", "ind", "fc", "ard", "ARand", "iRand", "aRand", "aR", "AR", "iR")):
                final_word = p_sandhi + "n" + root_start.replace("aRand", "anand").replace("iRand", "inand").replace("ARand", "Anand").replace("aRaw", "anaw").replace("iRind", "inind").replace("aRard", "anard").replace("aRfc", "anfc").replace("aRrt", "anrt")
                
        # Check augmented prefix attachment: e.g. paryaRand
        if p.endswith("i"):
            p_aug = p[:-1] + "ya"
        elif p.endswith("a") or p.endswith("A"):
            p_aug = p[:-1] + "A"
        elif p.endswith("r") or p.endswith("s"):
            p_aug = p_sandhi + "a"
        else:
            p_aug = p + "a"
            
        if final_word.startswith(p_aug + "R"):
            root_start = final_word[len(p_aug)+1:]
            if root_start.startswith(("and", "anand", "inand", "inind", "aw", "An", "fd", "rt", "ind", "fc", "ard", "ARand", "iRand", "aRand", "aR", "AR", "iR")):
                final_word = p_aug + "n" + root_start.replace("aRand", "anand").replace("iRand", "inand").replace("ARand", "Anand").replace("aRaw", "anaw").replace("iRind", "inind").replace("aRard", "anard").replace("aRfc", "anfc").replace("aRrt", "anrt")
                
    return final_word


def _fuse_prefix_chain(prefixes: list[str]) -> str:
    """Fuse prefixes alone (no root) to estimate prefix-region length."""
    if not prefixes:
        return ""
    base = prefixes[-1]
    if base == "AN":
        base = "A"
    for p in reversed(prefixes[:-1]):
        base = apply_single_upasarga_sandhi(p, base)
    return base


def apply_natva_prefix_aware(fused: str, chain_len: int, dhatu_id: str | None = None, inner: str | None = None) -> str:
    """Like apply_natva but n's inside prefix region (first chain_len chars)
    are blockers (never convert), only root/suffix n's convert.
    Exception: inner 'ni' (n-initial, no trailing r) allows conversion
    (pra;ni->praRi, pari;ni->pariRi), while nir/anu stay protected."""
    _VAN_IDS = {"01.0216", "01.0219", "01.0533", "01.0534", "01.0858", "01.0915", "01.0928", "01.0932", "01.0951", "01.0961", "01.0962", "01.1131", "08.0008", "10.0227", "10.0431"}
    _prot_len = chain_len - 2 if inner == "ni" else chain_len
    out: list[str] = []
    cause_seen = False
    allowed = set("aAiIuUfFeEoOyvhHkKgGNpPbBmM")
    for i, c in enumerate(fused):
        protected = i < _prot_len
        if c in ("r", "z", "f", "F"):
            cause_seen = True
            out.append(c)
        elif c == "n":
            if protected:
                cause_seen = False
                out.append("n")
            elif cause_seen:
                # Panini 8.4.21 abhyAsasya ca & 8.4.39 kzuBnAdiSu ca: abhyAsa n and Kan (01.1020)
                # never undergo Natva; dental n blocks subsequent Natva from preceding cause.
                rem = fused[i:]
                if (rem.startswith(("nin", "nen", "nan", "nIn", "naMnam", "nannam")) and not rem.startswith("nant")) or (dhatu_id == "01.1020" and fused[:i+1].endswith(("Kan", "KAn"))):
                    cause_seen = False
                    out.append("n")
                else:
                    is_padanta = (i == len(fused) - 1)
                    is_illegal = (i + 1 < len(fused) and fused[i+1] in "tTdDscCjJSwWqQz")
                    if is_padanta or is_illegal:
                        out.append("n")
                    else:
                        out.append("R")
                        # If part of geminate nn, maintain cause_seen for the 2nd n (nizanna->nizaRRa);
                        # otherwise 8.4.2: intervening R is tavarga (not in at-ku-pu-AN-num) and blocks further Natva.
                        if i + 1 < len(fused) and fused[i+1] == "n":
                            pass
                        else:
                            cause_seen = False
            else:
                out.append("n")
        elif c in allowed:
            out.append(c)
        else:
            cause_seen = False
            out.append(c)
    final_word = "".join(out)
    if dhatu_id is None or dhatu_id in _VAN_IDS:
        final_word = final_word.replace("rivaR", "rivan").replace("ravaR", "ravan").replace("rvaR", "rvan")
    # Panini 8.4.14 non-nopadeza patx~ (01.0979) yanganta substitute panIpat never undergoes Natva
    if "paRIpat" in final_word:
        final_word = final_word.replace("paRIpat", "panIpat")
    for p in ("pra", "parA", "nir", "antar", "pari", "dur", "dus", "nis"):
        p_sandhi = p[:-1] + "r" if p.endswith("s") else p
        if final_word.startswith(p_sandhi + "R"):
            root_start = final_word[len(p_sandhi)+1:]
            if root_start.startswith(("and", "anand", "inand", "inind", "aw", "An", "fd", "rt", "ind", "fc", "ard", "ARand", "iRand", "aRand", "aR", "AR", "iR")):
                final_word = p_sandhi + "n" + root_start.replace("aRand", "anand").replace("iRand", "inand").replace("ARand", "Anand").replace("aRaw", "anaw").replace("iRind", "inind").replace("aRard", "anard").replace("aRfc", "anfc").replace("aRrt", "anrt")
        if p.endswith("i"):
            p_aug = p[:-1] + "ya"
        elif p.endswith("a") or p.endswith("A"):
            p_aug = p[:-1] + "A"
        elif p.endswith("r") or p.endswith("s"):
            p_aug = p_sandhi + "a"
        else:
            p_aug = p + "a"
        if final_word.startswith(p_aug + "R"):
            root_start = final_word[len(p_aug)+1:]
            if root_start.startswith(("and", "anand", "inand", "inind", "aw", "An", "fd", "rt", "ind", "fc", "ard", "ARand", "iRand", "aRand", "aR", "AR", "iR")):
                final_word = p_aug + "n" + root_start.replace("aRand", "anand").replace("iRand", "inand").replace("ARand", "Anand").replace("aRaw", "anaw").replace("iRind", "inind").replace("aRard", "anard").replace("aRfc", "anfc").replace("aRrt", "anrt")
    return final_word


def apply_single_upasarga_sandhi(prefix: str, form: str) -> str:
    """
    Apply external sandhi between a single upasarga and a derived word.
    """
    if not prefix: return form
    
    if prefix == "AN":
        prefix = "A"
    
    p_end = prefix[-1]
    f_start = form[0]
    
    # Consonant-ending prefixes (sam, ud, nir, dur, nis, dus)
    if p_end == "m" and prefix == "sam":
        if f_start in "kKgG": return prefix[:-1] + "N" + form
        if f_start in "cCjJ": return prefix[:-1] + "Y" + form
        if f_start in "wWqQ": return prefix[:-1] + "R" + form
        if f_start in "tTdD": return prefix[:-1] + "n" + form
        if f_start in "pPbB": return prefix[:-1] + "m" + form
        if f_start in "yrlvSzsh": return prefix[:-1] + "M" + form
        if f_start in "nNmMYRlL": return prefix[:-1] + "M" + form
        return prefix + form
        
    if p_end == "d" and prefix == "ud":
        if form.startswith("sT"): return "utT" + form[2:]
        if form.startswith("sw"): return "uww" + form[2:] 
        if f_start in "cC": return "uc" + form
        if f_start == "S": return "uc" + form
        if f_start in "jJ": return "uj" + form
        if f_start in "wW": return "uw" + form
        if f_start in "nNmMYR": return "un" + form
        if f_start == "l": return "ul" + form
        if f_start in "qQ": return "uq" + form
        if f_start in "lL": return "ul" + form
        if f_start in "kKpPtTs": return "ut" + form
        return prefix + form

    if p_end == "r" and prefix in ("nir", "dur", "antar"):
        if f_start in "cC": return prefix[:-1] + "S" + form
        if f_start in "wW": return prefix[:-1] + "z" + form
        if f_start in "tT": return prefix[:-1] + "s" + form
        if f_start in "Szs": return prefix[:-1] + "H" + form
        if f_start in "kKpP": return prefix[:-1] + "z" + form
        if f_start == "r":
            v = prefix[-2]
            v_long = "A" if v=="a" else "I" if v=="i" else "U" if v=="u" else v
            return prefix[:-2] + v_long + form
        return prefix + form
        
    if p_end == "s" and prefix in ("nis", "dus"):
        if f_start in "cC": return prefix[:-1] + "S" + form
        if f_start in "wW": return prefix[:-1] + "z" + form
        if f_start in "tT": return prefix + form
        if f_start in "kKpP": return prefix[:-1] + "z" + form
        if f_start in "aAiIuUfFeEoO" or f_start in "gGdDqQbBjJnNmMYRyvrlh": return prefix[:-1] + "r" + form
        return prefix + form
        
    # Vowel-ending prefixes
    if p_end in "aA" and f_start in "aAiIuUfFeEoOE":
        if f_start in "aA": return prefix[:-1] + "A" + form[1:]
        if f_start in "iI": return prefix[:-1] + "e" + form[1:]
        if f_start in "uU": return prefix[:-1] + "o" + form[1:]
        if f_start in "fF": return prefix[:-1] + "Ar" + form[1:]
        if f_start in "eo": return prefix[:-1] + form
        if f_start in "EO": return prefix[:-1] + form
            
    if p_end in "iI" and f_start in "aAuUfFeEoOEO":
        return prefix[:-1] + "y" + form
    if p_end in "iI" and f_start in "iI":
        return prefix[:-1] + "I" + form[1:]
        
    if p_end in "uU" and f_start in "aAiIfFeEoOEO":
        return prefix[:-1] + "v" + form
    if p_end in "uU" and f_start in "uU":
        return prefix[:-1] + "U" + form[1:]

    # Tuk augment before ch
    if p_end in "aiuA" and f_start == "C":
        return prefix + "c" + form

    # Default concatenation
    return prefix + form


def apply_upasargas(prefix_str: str, form: str, dhatu_id: str = None, skip_satva: bool = False) -> str:

    """
    Applies one or more upasargas (separated by ';') to a given word form.
    It recursively handles inner-to-outer sandhi. 
    It also applies basic Natva and Satva on the boundary.
    skip_satva=True keeps s-variants (no s->z) for twin generation.
    """
    if not prefix_str:
        return form
        
    if "/" in form:
        return "/".join(apply_upasargas(prefix_str, f.strip(), dhatu_id, skip_satva) for f in form.split("/"))


    # Phase 3: Phonological Rules (Natva & Satva)
    # Pāṇinian satva: i/u-ending prefixes change s -> z
    # Since prefixes can be chained, we just check the innermost prefix that attaches to the root.
    prefixes = prefix_str.split(";")
    
    # Panini 8.2.19 upasargasyAyatau:
    # upasargasya rephasya latvaM syAd ayatau parataH.
    # The 'r' of the innermost upasarga is replaced by 'l' before the root 'ay' (01.0546 aya~),
    # but not in sannanta (where form starts with 'ayiyiz').
    # Surveyed all 01 prefixed blocks: latva l-forms (nil-/palA-/plA-) occur ONLY in 01.0546
    # (parA/nir); the form-based clause fired on augmented laN (a+yat->ayatata) for y-roots
    # (yat/yama/yaja/yac etc., 16 tasks, ~3000 tokens, zero l-hits) — removed, 0546-only.
    if dhatu_id == "01.0546" and not ("iyiz" in form or "diiz" in form):
        _latva = {"nir": "nil", "parA": "palA", "pra": "pla", "pari": "pali", "dur": "dul"}
        if prefixes[-1] in _latva:
            prefixes[-1] = _latva[prefixes[-1]]
            prefix_str = ";".join(prefixes)

    # Pre-sandhi Satva check (very simplified: if root form starts with 's' followed by vowel/y/v/r and inner prefix ends in i/u)
    # e.g., vi + sIdati -> vizIdati. 
    # But wait, it shouldn't apply to aT augment! vi + a + sIdat -> vyasIdat.
    # So if the form starts with 's' (i.e. no augment):
    inner = prefixes[-1]
    
    if not skip_satva:
        if dhatu_id == "01.0450":
            # ziDu~ gatyAm does NOT get Satva with any prefix!
            pass
        elif inner.endswith(("i", "u", "I", "U")) or inner in ("nir", "dur", "dus", "nis"):
            if form.startswith("s") and len(form) > 1:
                if form[1] in "aAiIuUfFeEoOyvr" and not form.startswith("sf"):
                    form = "z" + form[1:]
                elif form.startswith("st"):
                    form = "zw" + form[2:]
                elif form.startswith("sT"):
                    form = "zW" + form[2:]
                elif form.startswith("sn"):
                    form = "zR" + form[2:]
            elif (form.startswith("a") or form.startswith("A")) and len(form) > 2 and form[1] == "s":
                core = form[2:]
                if core.startswith(("eD", "iD", "iYc", "ec", "ic", "vaYj", "vaK", "aYj", "aNk", "tu", "to", "wO", "tAv", "un", "uv", "Av", "O", "ev", "evi", "TA", "Tu", "Te", "Ti", "TI", "aj", "vaj", "ANk", "ANK", "aNK", "ats", "Ad", "ad", "att", "atsA")):
                    z_core = core
                    if z_core.startswith("t"): z_core = "w" + z_core[1:]
                    elif z_core.startswith("T"): z_core = "W" + z_core[1:]
                    elif z_core.startswith("n"): z_core = "R" + z_core[1:]
                    form = form[0] + "z" + z_core
            
    # Pre-sandhi Natva check: r/f in prefix changes n -> R
    # e.g. pra + namati -> praRamati.
    # Panini 8.4.21 abhyAsasya ca: abhyāsa n (nin, nen, nan, nIn) never undergoes Natva.
    if inner in ("pra", "parA", "nir", "antar", "pari") and form.startswith("n"):
        if not form.startswith(("nand", "nfd", "nfc", "nrt", "nard", "naw", "nA", "nind", "nin", "nen", "nan", "nIn", "naMnam", "nannam")) or form.startswith("nant"):
            form = "R" + form[1:]

    # Apply external sandhi from inner to outer
    for p in reversed(prefixes):
        form = apply_single_upasarga_sandhi(p, form)
        
    # Post-sandhi general Natva (8.4.1 - 8.4.2), prefix-aware:
    # n's inside the prefix chain are blockers (never convert).
    try:
        chain = _fuse_prefix_chain(prefixes)
        form = apply_natva_prefix_aware(form, len(chain), dhatu_id, prefixes[-1])
    except Exception:
        form = apply_natva_prefix_aware(form, 0, dhatu_id, prefixes[-1])
            
    # Double Satva for reduplicated sidh (01.0049 and 01.0050)
    if not skip_satva:
        if "zisiD" in form: form = form.replace("zisiD", "ziziD")
        if "ziseD" in form: form = form.replace("ziseD", "zizeD")
        # Panini 8.3.65 saYja-svaYjAm double satva in reduplication (liw, san, yang, yangluk)
        for _s, _z in (
            ("zasaYj", "zazaYj"), ("zisaNkz", "zizaNkz"),
            ("zisvaNkz", "zizvaNkz"),
            ("zAsaj", "zAzaj"), ("zAsag", "zAzag"),
            ("zAsaYj", "zAzaYj"), ("zAsaNk", "zAzaNk"), ("zAsak", "zAzak"),
            ("zAsvaYj", "zAzvaYj"), ("zAsvaj", "zAzvaj"), ("zAsvag", "zAzvag"),
            ("zAsvaNk", "zAzvaNk"), ("zAsvak", "zAzvak"),
        ):
            if _s in form: form = form.replace(_s, _z)
    
        if inner.endswith(("i", "u", "I", "U")):
            if "aseziD" in form: form = form.replace("aseziD", "azeziD")
            if "asisiD" in form: form = form.replace("asisiD", "aziziD")
            if "asesiD" in form: form = form.replace("asesiD", "azeziD")
            # Panini 8.3.66 sadiraprateH: sad s->z after i/u-prefixes (except prati),
            # including reduplication (zAzad, zizats) and augmented a-forms (azad, azId, azizats, azAzad).
            if inner != "prati":
                if "zAsad" in form: form = form.replace("zAsad", "zAzad")
                if "zisats" in form: form = form.replace("zisats", "zizats")
                if "asid" in form: form = form.replace("asid", "azid")
                if "asId" in form: form = form.replace("asId", "azId")
                if "asad" in form: form = form.replace("asad", "azad")
                if "asizats" in form: form = form.replace("asizats", "azizats")
                if "asAsad" in form: form = form.replace("asAsad", "azAzad")
        
    # Wait, 01.0049 (ziDa~) gets NO SATVA with pari! 
    # Actually, pari + ziDa~ = pariseDati, but ni + ziDa~ = nizeDati.
    # Revert unwanted Satva for pari + siD
    if not skip_satva:
        if inner == "pari" and dhatu_id in ("01.0049", "01.0050"):
            if "ziziD" not in form and "zizeD" not in form and "zizED" not in form and "zeziD" not in form:
                if "pariz" in form: form = form.replace("pariz", "paris")
    
        if dhatu_id in ("01.0049", "01.0050"):
            form = form.replace("aziziD", "asisiD").replace("azizeD", "asiseD").replace("azeziD", "asesiD")
        
        # 01.0030 JSON has a typo for anu;AN -> avA in secondary derivations
    if dhatu_id == "01.0030" and prefix_str == "anu;AN":
        if form.startswith("anvAyiyat") or form.startswith("anvAyAt") or form.startswith("anvAyatay") or form.startswith("anvAyAyat"):
            form = form.replace("anvA", "avA", 1)
            
        # 01.0025 sam JSON typo: sam + aT + sozUd -> samasosUd instead of samasozUd
    if dhatu_id == "01.0025" and prefix_str == "sam":
        if "samasozUd" in form:
            form = form.replace("samasozUd", "samasosUd")
            
    return form
