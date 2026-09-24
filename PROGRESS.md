# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1101/1156 100%** (95.2%, raw 1101/1166)

## Done
- Panini 7.1.58 + 8.3.24 kz-num placement:
  - idit `*Akzi~` whose `base_wo_i` ends in `kz` inserts velar `N` before the cluster (`kAkz -> kANkz`), not before `z` (`kAkNz` was wrong, `M` never applies here). Mirrored in `tinanta.py` mUla-num and `krdanta.py`.
  - Surveyed all 7 `*kzi` dataset roots: 6 `*Akzi~` (`01.0760-0765`) take `ANkz`, sole `01.0269 kzi` (aniW, no `~`) keeps `kzay-`. Zero conflicts.
- Harness: `tests/test_dhatu.py` + `tests/sweep_gana.py` score list-valued krdanta `M/F/N` via `hit(cand)` (handles str and list).
- Debug prints removed from `pypanini/tinanta.py` + `pypanini/krdanta.py` (were slowing sweeps 10x).
- Full Sweep Results: **1101/1156 100% passes** (raw 1101/1166, 10 skipped):
  - `01.0760 kAkzi~`: 0 -> **895/895 (100.0%)** (+895) [NEW 100% PASS]
  - `01.0761 vAkzi~`: 0 -> **895/895 (100.0%)** (+895) [NEW 100% PASS]
  - `01.0762 mAkzi~`: 0 -> **895/895 (100.0%)** (+895) [NEW 100% PASS]
  - `01.0763 drAkzi~`: 0 -> **895/895 (100.0%)** (+895) [NEW 100% PASS]
  - `01.0764 DrAkzi~`: 0 -> **895/895 (100.0%)** (+895) [NEW 100% PASS]
  - `01.0765 DvAkzi~`: 0 -> **895/895 (100.0%)** (+895) [NEW 100% PASS]
  - Net matched tokens +5370 across 6 roots.
  - **STRICTLY 0 worsened roots** (`worsened == 0`, fid-diff vs HEAD).
  - All pilot and past milestone roots held strictly at 100.0% (pilots `4/4 OK`, guards `01.1051,1061,1067,1072,1118,0269` hold).

## Next
1. Target remaining 55 failing roots (one single-trait batch per iteration):
   - `Ca~` lw group (`01.0233 mleCa~, 01.0234, 01.0238, 01.0242, 01.0244 uCI~`, ~18/895, `lw 0/9` e.g. got `oCati` vs `ucCati`): survey every `C`-final `~` root for doubling/`Y`-num before coding.
   - Atmane `gup`-cluster (`01.0105, 01.1125-1128, 01.1166`, ~21/883, got `svazkate` vs `zvazkate`): satva/voicing trait.
   - `01.1116 meN`, `01.1117 deN` (~800/883, `yak/lw` + `liT` only): closest to finish.
   - `01.1124 tF` (646/895): 6.4.122 `ter-` in LiT + 7.1.100/8.2.77 (`tIrtvA`, `pratIrya`).
   - `01.0920 dF` (487/895) & `01.0921 nF` (478/895): R-ending roots in LiT/causative.
   - `01.1161 veY`, `01.1162 vyeY`, `01.1163 hveY`: semivowel + ec roots, samprasarana/LiT.
2. NOTE: stash `mixed-iteration WIP incl kz fix` holds unrelated uBayapadi/nitya-san/yan-F experiments that broke `01.0001` yang (`boBUAYcakre` 0/9) — do NOT pop as-is; split into single-trait batches with cheap pilot guard each.
3. Advance GaNa 01 beyond Milestone 1101 towards Milestone 1110+!
