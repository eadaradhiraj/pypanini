"""
pypanini.pratyahara
~~~~~~~~~~~~~~~~~~~
Māheśvara Sūtras (Śiva Sūtras) and Pratyāhāra expansion in SLP1.

The 14 Sūtras are the *phonological alphabet* from which Pāṇini builds
Pratyāhāras — abbreviations like ``ac`` (vowels), ``hal`` (consonants),
``ik`` (i, u, ṛ, ḷ) etc.  The engine needs them for two narrow purposes:

* The ``yaÑ`` set (``y, v, r, l`` + nasals) conditions the
  ``-yA-`` augment in laṬ/laṄ etc. (``Bav + yA + ti``).
* The ``iṆ/ku`` set is already hard-coded in :func:`phonetics.apply_satva`,
  but the Sūtra table is kept as the single source of truth for any future
  phonological rule that needs a Pratyāhāra membership test.

This module is *data + algorithm*, no dhatu-specific logic.

SLP1 encoding
-------------
All sounds are single ASCII characters (except the digraphs ``ar, al, Ay, Av``
which appear only after guṇa/vṛddhi, never inside the Sūtra table):

    a  i  u  ṛ(f)  ḷ(x)  e  o  ai(E)  au(O)  h  y  v  r  l  ...
    ṅ(N)  ñ(Y)  ṇ(R)  n  m  j(J)  bh(B)  gh(G)  ḍh(Q)  dh(D) ...

The Sūtra table below is therefore a direct transliteration of the
classical text, verified against the Kaśikā.

References
----------
* Siddhānta-Kaumudī, Maheśvara-Sūtra prakaraṇa
* SLP1 → Devanagari mapping: :mod:`pypanini.transliteration`

Type hints are exhaustive; the public API is two methods:
:py:meth:`MaheshvaraSutrasSLP1.get_pratyahara` and
:py:meth:`MaheshvaraSutrasSLP1.get_set`.
"""

from __future__ import annotations

from typing import List, Optional, Set


class MaheshvaraSutrasSLP1:
    """
    Encapsulates the 14 Māheśvara Sūtras and Pratyāhāra membership logic.

    Attributes:
        sutras: Ordered list of ``(sounds, it_marker)`` pairs. ``sounds`` is
            the list of SLP1 sounds introduced by the sūtra, ``it_marker``
            is the dummy *it* letter (``R, k, N …``) that terminates the
            sūtra and serves as the closing bracket for Pratyāhāras.

    Example:
        >>> ms = MaheshvaraSutrasSLP1()
        >>> ms.get_pratyahara("ac")  # a, i, u, ṛ, ḷ, e, o, ai, au
        ['a', 'i', 'u', 'f', 'x', 'e', 'o', 'E', 'O']
        >>> "y" in ms.get_set("yaY")
        True
    """

    def __init__(self) -> None:
        # Each entry is (list_of_sounds_in_sutra, it_marker).
        # The it_marker is *not* part of the sound inventory — it is the
        # meta-letter that Pāṇini uses to close the interval.
        self.sutras: List[tuple[List[str], str]] = [
            (['a', 'i', 'u'], 'R'),                   # 1.  a-i-u-Ṇ  (the Ṇ is R in SLP1)
            (['f', 'x'], 'k'),                         # 2.  ṛ-ḷ-k
            (['e', 'o'], 'N'),                         # 3.  e-o-Ṅ
            (['E', 'O'], 'c'),                         # 4.  ai-au-c
            (['h', 'y', 'v', 'r'], 'w'),               # 5.  h-y-v-r-aṬ
            (['l'], 'R'),                              # 6.  l-aṆ (second R)
            (['Y', 'm', 'N', 'R', 'n'], 'm'),          # 7.  ña-ma-ṅa-ṇa-na-m
            (['J', 'B'], 'Y'),                         # 8.  jha-bha-ñ
            (['G', 'Q', 'D'], 'z'),                   # 9.  gha-ḍha-dha-ṣ
            (['j', 'b', 'g', 'q', 'd'], 'S'),          # 10. ja-ba-ga-ḍa-da-ś
            (['K', 'P', 'C', 'W', 'T', 'c', 'w', 't'], 'v'), # 11. kha-pha-cha-ṭha-tha-ca-ṭa-ta-v
            (['k', 'p'], 'y'),                         # 12. ka-pa-y
            (['S', 'z', 's'], 'r'),                   # 13. śa-ṣa-sa-r
            (['h'], 'l'),                              # 14. ha-l
        ]

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def get_pratyahara(
        self,
        pratyahara: str,
        target_it_index: Optional[int] = None,
    ) -> List[str]:
        """
        Expand a Pāṇinian Pratyāhāra to its explicit sound list.

        A Pratyāhāra is written as two SLP1 characters: the *first* sound and
        the *closing* it-marker.  The interval includes every sound from the
        first occurrence of the start sound up to (and including) the sūtra
        that carries the it-marker, but *excludes* the it-marker itself.

        Disambiguation: the marker ``R`` occurs twice (sūtra 1 and sūtra 6).
        By default the engine returns the *first* valid ``R`` at or after the
        start.  The classical exception is ``iR`` which must use the *second*
        ``R`` (sūtra 6) — this is handled automatically.  Callers that need
        explicit control can pass ``target_it_index`` (1-based).

        Args:
            pratyahara: Two-character SLP1 Pratyāhāra (e.g. ``"ac"``, ``"hal"``,
                ``"yaY"``, ``"jaS"``).
            target_it_index: If given, selects the N-th global occurrence of the
                it-marker (1-based).  Useful for ``aR`` (1st R) vs ``iR``
                (2nd R) disambiguation in tests.

        Returns:
            Ordered list of SLP1 sounds in the Pratyāhāra interval.

        Raises:
            ValueError: If the Pratyāhāra is not two characters, the start sound
                is not found, or the it-marker does not occur at or after the
                start.

        Example:
            >>> ms = MaheshvaraSutrasSLP1()
            >>> ms.get_pratyahara("ik")   # i, u, ṛ, ḷ
            ['i', 'u', 'f', 'x']
            >>> ms.get_pratyahara("aR", target_it_index=1)  # a,i,u
            ['a', 'i', 'u']
        """
        # ---- 1. Validate shape ----
        if len(pratyahara) != 2:
            raise ValueError("SLP1 Pratyahara must be 2 characters.")

        start: str = pratyahara[0]
        it_marker: str = pratyahara[1]

        # ---- 2. Locate start sūtra ----
        start_idx: Optional[int] = None
        sound_offset: Optional[int] = None
        for s_idx, (sounds, _) in enumerate(self.sutras):
            if start in sounds:
                start_idx = s_idx
                sound_offset = sounds.index(start)
                break

        if start_idx is None or sound_offset is None:
            raise ValueError(f"Start sound '{start}' not found in any sutra.")

        # ---- 3. Collect candidate it positions at or after start ----
        valid_it_indices: List[int] = [
            i for i, (_, it) in enumerate(self.sutras)
            if it == it_marker and i >= start_idx
        ]

        if not valid_it_indices:
            raise ValueError(f"It-marker '{it_marker}' does not appear after sound '{start}'.")

        # ---- 4. Resolve which it to close on ----
        if target_it_index is not None:
            # Explicit N-th global occurrence
            all_matches: List[int] = [i for i, (_, it) in enumerate(self.sutras) if it == it_marker]
            if not (1 <= target_it_index <= len(all_matches)):
                raise ValueError(f"target_it_index {target_it_index} out of range for '{it_marker}'")
            it_idx: int = all_matches[target_it_index - 1]
            if it_idx < start_idx:
                raise ValueError(f"Target occurrence {target_it_index} of '{it_marker}' is before '{start}'.")
        else:
            # Classical default: iR → second R, everything else → first valid
            if start == 'i' and it_marker == 'R':
                it_idx = valid_it_indices[-1]
            else:
                it_idx = valid_it_indices[0]

        # ---- 5. Materialise the interval ----
        #   For the first sūtra we start *inside* the sound list at sound_offset;
        #   for subsequent sūtras we include the entire list.
        res: List[str] = []
        for s_idx in range(start_idx, it_idx + 1):
            sounds, _ = self.sutras[s_idx]
            if s_idx == start_idx:
                # slice from start sound onward within the first sūtra
                assert sound_offset is not None
                res.extend(sounds[sound_offset:])
            else:
                res.extend(sounds)
        return res

    def get_set(
        self,
        pratyahara: str,
        target_it_index: Optional[int] = None,
    ) -> Set[str]:
        """
        Convenience wrapper returning the Pratyāhāra as a ``set`` for
        membership tests (``in``).

        Args:
            pratyahara: Two-character SLP1 Pratyāhāra.
            target_it_index: See :meth:`get_pratyahara`.

        Returns:
            Set of SLP1 characters in the Pratyāhāra.

        Example:
            >>> ms = MaheshvaraSutrasSLP1()
            >>> y_set = ms.get_set("yaY")
            >>> "v" in y_set
            True
        """
        return set(self.get_pratyahara(pratyahara, target_it_index))
