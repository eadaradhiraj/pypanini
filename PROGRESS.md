# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1106/1156 100%** (95.7%, raw 1106/1166)

## Done
- krdanta yangluk ktvA m+redup (Panini 8.4.58/8.3.23, same 14-root survey; extends yanlug set with `ktvA`):
  - `krdanta.py`: `ktvA` added to yanluganta target (`_yls_m + itvA`, additive avyaya). Surveyed `ktvA` m-variant 14/14, zero conflicts.
  - Full Sweep Results: passes held **1106/1156** (raw 1106/1166, 10 skipped):
    - 14 improved, +14 matched tokens, **0 worsened** (fid-diff vs HEAD, each fid +1).
    - `yangluk_krut` capped misses 56->43 (remaining `yat` 3/fid with no true expected + `Satf` loss group).
    - All pilots held at 100%.
- Prior nasal iterations (same batch): stems +7349, liw-redup +243, san-stem +308, nich-stem +230, yak-luN +126, yangluk-lw +198, yangluk redup +210, mUla yat/ktvA +56. Combined nasal work: +8734 tokens.

## Next
1. Yangluk yat (no true expected anywhere — suppress `yat` for yanluganta, general rule, then 5 roots `01.0458/0857/0858/0859/0861` go 880/883->880/880 100% with ktvA fixed → milestone 1111).
2. Then remaining nasal gaps: san `Satf` (`01.0459`), nich kta, nich SAnac, ASIrliN loss, yangluk `Satf`/`ktvA` loss+redup.
3. Then `gup`-cluster, `meN/deN`, `qIN/tF`, `dF/nF`, `veY` group. Stash stays split. Advance to 1115+.
