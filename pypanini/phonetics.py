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
