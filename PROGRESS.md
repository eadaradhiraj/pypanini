# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1106/1156 100%** (95.7%, raw 1106/1166)

## Done
- Panini 6.1.73 *che ca* (C-final tuk, lexicalized `cC` stem):
  - `tinanta.py` mUla-clean + `krdanta.py`: `clean.endswith("C")` without `ur/Ur` maps `clean[:-1] + "cC"` (`mleC->mlecC`, `hrIC->hrIcC`, `uC->ucC`); `urCA~` (`hurC/murC/sPurC`) excluded, already `UrC` and passing.
  - Surveyed all 8 C-final 01 roots: 5 short-vowel take `cC`, 3 `urCA~` keep `UrC`. Zero conflicts. `01.0269 kzi` unaffected (not C-final).
  - Krdanta gemination made idempotent (`mlecC->mlecCita`); aniW `cC+ta->zwa` (`ucC->uzwa`, sole root `01.0244`).
- Full Sweep Results: **1106/1156 100% passes** (raw 1106/1166, 10 skipped):
  - `01.0233 mleCa~`: 18 -> **895/895 (100.0%)** (+877) [NEW 100% PASS]
  - `01.0234 laCa~`: 18 -> **895/895 (100.0%)** (+877) [NEW 100% PASS]
  - `01.0238 hrICa~`: 18 -> **895/895 (100.0%)** (+877) [NEW 100% PASS]
  - `01.0242 yuCa~`: 18 -> **895/895 (100.0%)** (+877) [NEW 100% PASS]
  - `01.0244 uCI~`: 12 -> **636/636 (100.0%)** (+624) [NEW 100% PASS]
  - Net matched tokens +4132 across 5 roots.
  - **STRICTLY 0 worsened roots** (`worsened == 0`, fid-diff vs HEAD).
  - All pilot and past milestone roots held strictly at 100.0% (kz-batch `01.0760-0765`, `urCA~` `01.0239-0241`, `01.1051-1072` guards hold).

## Next
1. Target remaining 50 failing roots (one single-trait batch per iteration):
   - Atmane `gup`-cluster (`01.0105, 01.1125-1128, 01.1166`, ~21/883, got `svazkate` vs `zvazkate`): satva/voicing trait.
   - `01.1116 meN`, `01.1117 deN` (~800/883, `yak/lw` + `liT` only): closest to finish.
   - `01.1123 qIN` (378/883, san `qiqayiz` vs `RiRqiz`): `qI` exclusion recently added for num — revisit san stem.
   - `01.1124 tF` (646/895): 6.4.122 `ter-` in LiT + 7.1.100/8.2.77 (`tIrtvA`, `pratIrya`).
   - `01.0920 dF` (487/895) & `01.0921 nF` (478/895): R-ending roots in LiT/causative.
   - `01.1161 veY`, `01.1162 vyeY`, `01.1163 hveY`: semivowel + ec roots, samprasarana/LiT.
2. NOTE: stash `mixed-iteration WIP incl kz fix` still holds unrelated uBayapadi/nitya-san/yan-F experiments — do NOT pop as-is; split into single-trait batches with cheap pilot guard each.
3. Advance GaNa 01 beyond Milestone 1106 towards Milestone 1115+!
