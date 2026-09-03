"""
pypanini.transliteration
~~~~~~~~~~~~~~~~~~~~~~~~~
Bidirectional SLP1 ↔ Devanagari converter.

Motivation
----------
All internal derivation works in **SLP1** (Sanskrit Library Phonetic) — a
lossless, ASCII-only encoding where every phoneme is one character (``k, K,
g, G, a, A, i, U, f, x, e, E, o, O, M, H`` …).  Devanagari is only needed
for human-readable output and for matching the scraped ``ashtadhyayi.com``
JSON, which mixes both scripts.

This module is therefore a *pure* transliterator with no grammatical logic.
It handles:

* Independent vowels (``a → अ``, ``A → आ`` …)
* Consonant + vowel signs (mātrās) — ``k + i → कि`` (``k`` carries an
  implicit virāma that is replaced by the mātrā)
* Virāma (halanta) ``्`` for consonant clusters and word-final consonants
* Anusvāra / visarga / candrabindu (``M → ं``, ``H → ः``, ``~ → ँ``)
* Avagraha ``' → ऽ``

Design
------
Two parallel dictionaries drive both directions:

``SLP1_TO_DEV_*`` — forward (SLP1 → Deva)
``DEV_TO_SLP1_*`` — reverse (Deva → SLP1), built by inverting the forward
                    tables at import time.

The algorithms are linear scans with one-character look-ahead for the
Deva→SLP1 direction (to detect ``C + virāma`` vs ``C + mātrā``).

Heavy commenting below walks through the state machine so that future
Anta-specific sandhi can be added without breaking the virāma logic.

Type hints are exhaustive; the module has no external dependencies.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Forward tables: SLP1 → Devanagari
# ---------------------------------------------------------------------------

# Independent vowels — used when a vowel is syllable-initial or follows
# another vowel (no preceding consonant to attach a mātrā to).
SLP1_TO_DEV_VOWEL: dict[str, str] = {
    'a': 'अ', 'A': 'आ', 'i': 'इ', 'I': 'ई', 'u': 'उ', 'U': 'ऊ',
    'f': 'ऋ', 'F': 'ॠ', 'x': 'ऌ', 'X': 'ॡ', 'e': 'ए', 'E': 'ऐ',
    'o': 'ओ', 'O': 'औ',
}

# Vowel signs (mātrās) — used when a vowel follows a consonant.
# ``a`` has no sign (inherent ``-a``), so it maps to the empty string and
# the virāma added for the consonant is simply kept.
SLP1_TO_DEV_MATRA: dict[str, str] = {
    'a': '', 'A': 'ा', 'i': 'ि', 'I': 'ी', 'u': 'ु', 'U': 'ू',
    'f': 'ृ', 'F': 'ॄ', 'x': 'ॢ', 'X': 'ॣ', 'e': 'े', 'E': 'ै',
    'o': 'ो', 'O': 'ौ',
}

# Consonants — each is emitted as ``C + virāma``; the virāma is later
# overwritten by a mātrā if the next character is a vowel.
SLP1_TO_DEV_CONS: dict[str, str] = {
    'k': 'क', 'K': 'ख', 'g': 'ग', 'G': 'घ', 'N': 'ङ',
    'c': 'च', 'C': 'छ', 'j': 'ज', 'J': 'झ', 'Y': 'ञ',
    'w': 'ट', 'W': 'ठ', 'q': 'ड', 'Q': 'ढ', 'R': 'ण',
    't': 'त', 'T': 'थ', 'd': 'द', 'D': 'ध', 'n': 'न',
    'p': 'प', 'P': 'फ', 'b': 'ब', 'B': 'भ', 'm': 'म',
    'y': 'य', 'r': 'र', 'l': 'ल', 'v': 'व',
    'S': 'श', 'z': 'ष', 's': 'स', 'h': 'ह',
}

# Miscellaneous signs (anusvāra, visarga, etc.).
SLP1_TO_DEV_MISC: dict[str, str] = {'M': 'ं', 'H': 'ः', '~': 'ँ', "'": 'ऽ'}

# ---------------------------------------------------------------------------
# Reverse tables: Devanagari → SLP1
# ---------------------------------------------------------------------------
# Built by inversion at import time so the two directions can never drift.

DEV_TO_SLP1_VOWEL: dict[str, str] = {v: k for k, v in SLP1_TO_DEV_VOWEL.items()}
DEV_TO_SLP1_MATRA: dict[str, str] = {v: k for k, v in SLP1_TO_DEV_MATRA.items() if v}  # skip 'a' → ''
DEV_TO_SLP1_CONS: dict[str, str] = {v: k for k, v in SLP1_TO_DEV_CONS.items()}
DEV_TO_SLP1_MISC: dict[str, str] = {v: k for k, v in SLP1_TO_DEV_MISC.items()}

# Halanta that terminates a consonant conjunct.
VIRAMA: str = '्'


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def slp1_to_devanagari(text: str) -> str:
    """
    Transliterate SLP1 → Devanagari.

    This is a *stateful* scan that tracks whether the previous character was a
    consonant (hence still carries a virāma that can be replaced by a mātrā).

    Algorithm (per character ``ch`` in ``text``):
        1. If ``ch`` is a vowel:
           - If ``prev_was_cons`` is True, the previous output ends with
             ``virāma`` — replace that virāma with the appropriate mātrā
             (or nothing for ``a``).
           - Otherwise emit the independent vowel.
        2. If ``ch`` is a consonant: emit ``C + virāma`` and set the flag.
        3. If ``ch`` is misc (``M/H``): emit the sign, clear the flag.
        4. Otherwise (punctuation, ``/``, ``|`` …): pass through.

    Args:
        text: SLP1 string (e.g. ``"Bavati"``, ``"eDizIzwa"``, ``"BUtvA"``).

    Returns:
        Devanagari string (e.g. ``"भवति"``, ``"एधिषीष्ट"``).

    Example:
        >>> slp1_to_devanagari("Bavati")
        'भवति'
        >>> slp1_to_devanagari("eDitaH")
        'एधितः'
    """
    res: list[str] = []
    prev_was_cons: bool = False

    for ch in text:
        if ch in SLP1_TO_DEV_VOWEL:
            # Vowel: either attach a mātrā to the preceding consonant or emit
            # an independent vowel.
            if prev_was_cons:
                # The last element in res is "C + virāma" (e.g. "भ्").
                # Replace the trailing virāma with the mātrā.
                # For 'a' the mātrā is '' so we just strip the virāma.
                res[-1] = res[-1][:-1] + SLP1_TO_DEV_MATRA[ch]
            else:
                res.append(SLP1_TO_DEV_VOWEL[ch])
            prev_was_cons = False

        elif ch in SLP1_TO_DEV_CONS:
            # Consonant: emit with virāma; it may be overwritten by the next vowel.
            res.append(SLP1_TO_DEV_CONS[ch] + VIRAMA)
            prev_was_cons = True

        elif ch in SLP1_TO_DEV_MISC:
            # Anusvāra / visarga: standalone, no virāma interaction.
            res.append(SLP1_TO_DEV_MISC[ch])
            prev_was_cons = False

        else:
            # Punctuation, digits, slash, etc. — preserve verbatim.
            res.append(ch)
            prev_was_cons = False

    return "".join(res)


def devanagari_to_slp1(text: str) -> str:
    """
    Transliterate Devanagari → SLP1.

    This is the inverse of :func:`slp1_to_devanagari` and must round-trip:

        ``devanagari_to_slp1(slp1_to_devanagari(x)) == x``  for all SLP1 ``x``.

    The scan is a 1-character look-ahead state machine:

        * ``C + virāma`` → ``C`` (bare consonant, e.g. ``भ् → B``)
        * ``C + mātrā`` → ``C + vowel`` (e.g. ``भि → Bi``)
        * ``C`` at end-of-string or before a non-mātrā → ``C + a`` (inherent a)
        * Independent vowel → ``vowel``
        * ``M/H`` → ``M/H``

    Args:
        text: Devanagari string.

    Returns:
        SLP1 string.

    Example:
        >>> devanagari_to_slp1("भवति")
        'Bavati'
        >>> devanagari_to_slp1("एधितः")
        'eDitaH'
    """
    res: list[str] = []
    i: int = 0
    n: int = len(text)

    while i < n:
        c: str = text[i]

        if c in DEV_TO_SLP1_VOWEL:
            # Independent vowel at syllable start.
            res.append(DEV_TO_SLP1_VOWEL[c])
            i += 1

        elif c in DEV_TO_SLP1_CONS:
            # Consonant: look ahead to decide virāma vs mātrā vs inherent a.
            if i + 1 < n and text[i + 1] == VIRAMA:
                # C + virāma → bare C (e.g. "भ्" → "B")
                res.append(DEV_TO_SLP1_CONS[c])
                i += 2
            elif i + 1 < n and text[i + 1] in DEV_TO_SLP1_MATRA:
                # C + mātrā → C + vowel (e.g. "भि" → "Bi")
                res.append(DEV_TO_SLP1_CONS[c] + DEV_TO_SLP1_MATRA[text[i + 1]])
                i += 2
            else:
                # C with inherent 'a' (word-final or before another C without virāma)
                res.append(DEV_TO_SLP1_CONS[c] + "a")
                i += 1

        elif c in DEV_TO_SLP1_MISC:
            res.append(DEV_TO_SLP1_MISC[c])
            i += 1

        else:
            # Punctuation / space — preserve.
            res.append(c)
            i += 1

    return "".join(res)
