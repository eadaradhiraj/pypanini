# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1106/1156 100%** (95.7%, raw 1106/1166)

## Done
- krdanta yangluk redup + nasal (Panini 8.4.58/8.3.23, same 14-root `n`+labial/s survey; `krdanta.py` yanluganta `tavya/anIyar/tfc/Rvul/lyuw/GaY/tumun`, `kta/ktavatu/Satf` loss-excluded, `yat` no-true-expected-excluded):
  - `krdanta.py`: `_yanlug_m_base` mirrors tinanta redup then assimilates (`SranB->SASramB`, `tunp->totump`, `Sans->SASaMs`, `srans->sanIsraMs`, `RB->mB` included). Surveyed yangluk_krut `tavya` 14/14 `m/M` redup, `kta` 14/14 loss+redup, zero conflicts. Additive lists (old kept), `lyuw/GaY` single-form replaced (old misses).
  - Full Sweep Results: passes held **1106/1156** (raw 1106/1166, 10 skipped):
    - 14 improved, +210 matched tokens, **0 worsened** (fid-diff vs HEAD): `01.0458` 860->875, `01.0459` 782->797, `01.0471/0473/0475/0477/0497/0499/0501` 854->869, `01.0829` 851->866, `01.0857/0858/0859` 860->875, `01.0861` 860->875.
    - `yangluk_krut` capped misses 64->44 (remaining `yat`/`ktvA`/`Satf` loss group, e.g. `01.0458 yangluk_krut/yat/M:SranByaH`).
    - All pilots (01.0001/01.0002/01.0003) and past milestones held at 100%.
- Prior nasal iterations (same batch): stems +7349, liw-redup +243, san-stem +308, nich-stem +230, yak-luN +126, yangluk-lw +198. Combined nasal work: +8664 tokens.

## Next
1. Remaining nasal gaps (single trait each):
   - krdanta yangluk `ktvA`/`Satf` loss+redup (`01.0458 yangluk_krut/ktvA:SranBitvA` vs `SASrabDvA/SASramBitvA`, `01.0829 yangluk_krut/Satf/M:Sansan` vs `SASasat`): mirror `kta` loss+redup (`totupita/SASrabDa`).
   - krdanta nijanta kta (`tupita` vs `tumpita`), nich SAnac ay-retention (`tumpyamAna` vs `tumpayamAna`), ASIrliN nasal loss (`tunpyAt` vs `tupyAt`), krut/yat nasal (`sransya` vs `sraMsya`), krut/ktvA variants (`sranBitvA` vs `sramBitvA`).
   - yangluk_krut `yat` has no true expected (always misses) — consider suppressing `yat` for yanluganta or leaving as known miss (do not force redup `yat`).
2. Then next single-trait batch:
   - Atmane `gup`-cluster (`01.0105 zvazka~` satva-pratizedha per DAtuviSezaH 6.1.64 + `01.1125-1128` nitya-san 3.1.5/3.1.6 `jugupsate/titikzate/mImAMsate/bIBatsate` + `01.1166 fti`).
   - `01.1116 meN`, `01.1117 deN` (~800/883, `yak/lw` + `liT` only): closest to finish.
   - `01.1123 qIN` (378/883, san `qiqayz` vs `RiRqiz`), `01.1124 tF` (646/895, 6.4.122 `ter-` + 7.1.100/8.2.77).
   - `01.0920 dF`/`01.0921 nF` (R-roots LiT/causative), `01.1161 veY`/`01.1162 vyeY`/`01.1163 hveY` (samprasAraNa/LiT).
3. NOTE: stash `mixed-iteration WIP incl kz fix` still holds unrelated uBayapadi/nitya-san/yan-F experiments — do NOT pop as-is; split into single-trait batches with cheap pilot guard each.
4. Advance GaNa 01 beyond Milestone 1106 towards Milestone 1115+!
