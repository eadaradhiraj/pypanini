# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1106/1156 100%** (95.7%, raw 1106/1166)

## Done
- krdanta mUla yat/ktvA nasal (Panini 8.4.58/8.3.23, same 14-root `n`+labial/s survey; extends mUla rule to `yat`+`ktvA`):
  - `krdanta.py`: added `yat`+`ktvA` to mUla/san/nich nasal replacement list. Surveyed `yat` 14/14 `m/M`, `ktvA` m-variant 14/14, zero conflicts (`kta/ktavatu/lyap` still loss).
  - Full Sweep Results: passes held **1106/1156** (raw 1106/1166, 10 skipped):
    - 14 improved, +56 matched tokens, **0 worsened** (fid-diff vs HEAD): each nasal fid +4 (`yat` M/F/N + `ktvA`), e.g. `01.0458` 875->879, `01.0471` 869->873, `01.0857` 875->879.
    - `krut` capped misses 276->220; `yangluk_krut` 44->56 and `san_krut` 12->15 are freed-cap artifacts (fid-diff truth: 0 worsened; newly-surfaced `01.0459 san_krut/Satf/M:sisramBizan` queued below).
    - All pilots (01.0001/01.0002/01.0003) and past milestones held at 100%.
- Prior nasal iterations (same batch): stems +7349, liw-redup +243, san-stem +308, nich-stem +230, yak-luN +126, yangluk-lw +198, yangluk redup +210. Combined nasal work: +8720 tokens.

## Next
1. Remaining nasal gaps (single trait each):
   - san-stem `Satf` for nasal roots (`01.0459 san_krut/Satf/M:sisramBizan` newly surfaced; check `_sannanta_sec` head vs `Satf` formation).
   - krdanta nijanta kta (`tupita` vs `tumpita`), nich SAnac ay-retention (`tumpyamAna` vs `tumpayamAna`), ASIrliN nasal loss (`tunpyAt` vs `tupyAt`).
   - krdanta yangluk `ktvA`/`Satf` loss+redup (`SASrabDvA/SASasat`); yangluk_krut `yat` has no true expected — leave as known miss unless suppressing.
2. Then next single-trait batch:
   - Atmane `gup`-cluster (`01.0105 zvazka~` satva-pratizedha per DAtuviSezaH 6.1.64 + `01.1125-1128` nitya-san 3.1.5/3.1.6 + `01.1166 fti`).
   - `01.1116 meN`, `01.1117 deN` (~800/883): closest to finish.
   - `01.1123 qIN` (378/883), `01.1124 tF` (646/895).
   - `01.0920 dF`/`01.0921 nF`, `01.1161 veY`/`01.1162 vyeY`/`01.1163 hveY`.
3. NOTE: stash `mixed-iteration WIP incl kz fix` still holds unrelated experiments — do NOT pop as-is; split into single-trait batches with cheap pilot guard each.
4. Advance GaNa 01 beyond Milestone 1106 towards Milestone 1115+!
