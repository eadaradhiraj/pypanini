"""Māheśvara Sūtras (SLP1)"""
from typing import List, Optional, Set

class MaheshvaraSutrasSLP1:
    def __init__(self):
        self.sutras = [
            (['a', 'i', 'u'], 'R'),                   # 1.  a-i-u-R
            (['f', 'x'], 'k'),                         # 2.  f-x-k
            (['e', 'o'], 'N'),                         # 3.  e-o-N
            (['E', 'O'], 'c'),                         # 4.  E-O-c
            (['h', 'y', 'v', 'r'], 'w'),               # 5.  h-y-v-r-w
            (['l'], 'R'),                              # 6.  l-R
            (['Y', 'm', 'N', 'R', 'n'], 'm'),          # 7.  Y-m-N-R-n-m
            (['J', 'B'], 'Y'),                         # 8.  J-B-Y
            (['G', 'Q', 'D'], 'z'),                   # 9.  G-Q-D-z
            (['j', 'b', 'g', 'q', 'd'], 'S'),          # 10. j-b-g-q-d-S
            (['K', 'P', 'C', 'W', 'T', 'c', 'w', 't'], 'v'), # 11. K-P-C-W-T-c-w-t-v
            (['k', 'p'], 'y'),                         # 12. k-p-y
            (['S', 'z', 's'], 'r'),                   # 13. S-z-s-r
            (['h'], 'l'),                              # 14. h-l
        ]

    def get_pratyahara(self, pratyahara: str, target_it_index: Optional[int] = None) -> List[str]:
        if len(pratyahara) != 2:
            raise ValueError("SLP1 Pratyahara must be 2 characters.")
        start, it_marker = pratyahara[0], pratyahara[1]

        # 1. Locate the sutra where the starting sound appears
        start_idx = None
        sound_offset = None
        for s_idx, (sounds, _) in enumerate(self.sutras):
            if start in sounds:
                start_idx = s_idx
                sound_offset = sounds.index(start)
                break

        if start_idx is None:
            raise ValueError(f"Start sound '{start}' not found in any sutra.")

        # 2. Find all occurrences of it_marker that appear at or after start_idx
        valid_it_indices = [
            i for i, (_, it) in enumerate(self.sutras)
            if it == it_marker and i >= start_idx
        ]

        if not valid_it_indices:
            raise ValueError(f"It-marker '{it_marker}' does not appear after sound '{start}'.")

        # 3. Resolve ambiguity
        if target_it_index is not None:
            all_matches = [i for i, (_, it) in enumerate(self.sutras) if it == it_marker]
            it_idx = all_matches[target_it_index - 1]
            if it_idx < start_idx:
                raise ValueError(f"Target occurrence {target_it_index} of '{it_marker}' is before '{start}'.")
        else:
            # Pāṇinian rule: 'iR' always uses the 2nd 'R' (Sutra 6)
            if start == 'i' and it_marker == 'R':
                it_idx = valid_it_indices[-1]
            else:
                it_idx = valid_it_indices[0]

        # 4. Collect sounds
        res = []
        for s_idx in range(start_idx, it_idx + 1):
            sounds, _ = self.sutras[s_idx]
            res.extend(sounds[sound_offset:] if s_idx == start_idx else sounds)
        return res

    def get_set(self, pratyahara: str, target_it_index: Optional[int] = None) -> Set[str]:
        return set(self.get_pratyahara(pratyahara, target_it_index))
