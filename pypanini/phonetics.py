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
            is_nt = (i + 1 < len(word) and word[i+1] == "t")
            if is_padanta or is_nt:
                out.append("n")
            else:
                out.append("R")
        elif c in allowed_interveners:
            out.append(c)
        else:
            cause_seen = False
            out.append(c)
    return "".join(out)

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
        return prefix + form
        
    if p_end == "d" and prefix == "ud":
        if form.startswith("sT"): return "utT" + form[2:]
        if form.startswith("sw"): return "uww" + form[2:] 
        if f_start in "cC": return "uc" + form
        if f_start in "jJ": return "uj" + form
        if f_start in "wW": return "uw" + form
        if f_start in "qQ": return "uq" + form
        if f_start in "lL": return "ul" + form
        if f_start in "kKpPtTsS": return "ut" + form
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
        if f_start in "aAiIuUfFeEoOAyvrlh": return prefix[:-1] + "r" + form
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


def apply_upasargas(prefix_str: str, form: str) -> str:
    """
    Applies one or more upasargas (separated by ';') to a given word form.
    It recursively handles inner-to-outer sandhi. 
    It also applies basic Natva and Satva on the boundary.
    """
    if not prefix_str:
        return form
        
    if "/" in form:
        return "/".join(apply_upasargas(prefix_str, f.strip()) for f in form.split("/"))


    # Phase 3: Phonological Rules (Natva & Satva)
    # Pāṇinian satva: i/u-ending prefixes change s -> z
    # Since prefixes can be chained, we just check the innermost prefix that attaches to the root.
    prefixes = prefix_str.split(";")
    
    # Pre-sandhi Satva check (very simplified: if root form starts with 's' followed by vowel/y/v/r and inner prefix ends in i/u)
    # e.g., vi + sIdati -> vizIdati. 
    # But wait, it shouldn't apply to aT augment! vi + a + sIdat -> vyasIdat.
    # So if the form starts with 's' (i.e. no augment):
    inner = prefixes[-1]
    if inner.endswith(("i", "u", "I", "U")) and form.startswith("s") and len(form) > 1 and form[1] in "aAiIuUfFeEoOyvr":
        # Some roots resist this (e.g. sfp, sfj, etc.) but we apply a broad approximation first.
        # Let's skip 'sf' roots for now, they are notoriously complex. 
        if not form.startswith("sf"):
            form = "z" + form[1:]
            
    # Pre-sandhi Natva check: r/f in prefix changes n -> R
    # e.g. pra + namati -> praRamati.
    if inner in ("pra", "parA", "nir", "antar", "pari") and form.startswith("n"):
        form = "R" + form[1:]

    # Apply external sandhi from inner to outer
    for p in reversed(prefixes):
        form = apply_single_upasarga_sandhi(p, form)
        
    # Post-sandhi general Natva (8.4.1 - 8.4.2)
    # Applies if the prefix has r/z/f (pra, parA, nir, antar, pari, dur, dus, nis).
    # We just pass the whole fused form through the natva engine.
    form = apply_natva(form)
            
    return form
