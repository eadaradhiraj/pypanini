# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1106/1156 100%** (95.7%, raw 1106/1166)

## Done
- krdanta san-stem nasal (Panini 8.4.58/8.3.23, same 14-root `n`+labial/s survey via san_krut/kta bases — `tutumpizita/sisraMsizita/SiSramBizita/SiSaMsizita` unanimous `m/M`, zero conflicts):
  - `krdanta.py`: `n->m/M` replacement at `_sannanta_sec` head; downstream `clean = sec` repairs all san_krut pratyayas (kta/ktavatu/tavya/...) at once.
  - Full Sweep Results: passes held **1106/1156** (raw 1106/1166, 10 skipped):
    - 14 improved, +308 matched tokens, **0 worsened** (fid-diff vs HEAD): `01.0458` 788->810, `01.0459` 710->732, `01.0471/0473/0475/0477/0497/0499/0501` 782->804, `01.0829` 802->824, `01.0857/0858/0859` 829->851, `01.0861` 788->810.
    - `san_krut` capped misses 51->12; `nich_krut` 11->38 and `yangluk_krut` 12 are freed-cap artifacts (fid-diff truth: 0 worsened; precedent PROGRESS #52/#53). Top newly-surfaced examples are nasal too (`01.0458 nich_krut/SAnac/M:SranByamAnaH` wants `SramByamAnaH`, `01.0829 yangluk_krut/Satf/M:Sansan` wants `SaMsan`) — queued next.
    - All pilots (01.0001/01.0002/01.0003) and past milestones held at 100%.
- Prior nasal iterations (same batch): stems +7349, liw-redup +243. Combined nasal work: +7900 tokens.

## Next
1. Remaining gaps in the nasal batch (one trait per iteration):
   - krdanta nich-stem nasal (`01.0458 nich_krut/SAnac/M:SranByamAnaH` vs `SramByamAnaH`, `_nijanta_sec` head; survey nich_krut bases for m/M unanimity first).
   - krdanta yanluk-stem nasal (`01.0829 yangluk_krut/Satf/M:Sansan` vs `SaMsan`).
   - ASIrliN nasal loss before `y` (`tunpyAt` vs `tupyAt`, `SansyAt` vs `SasyAt`?) + luN futures.
   - yak-luN with `n` (`asransi` vs `asraMsi`, `aSranBi` vs `aSramBi`): yak-luN augment path uses raw clean.
2. Then next single-trait batch:
   - Atmane `gup`-cluster (`01.0105 zvazka~` satva-pratizedha per DAtuviSezaH 6.1.64 + `01.1125-1128` nitya-san 3.1.5/3.1.6 `jugupsate/titikzate/mImAMsate/bIBatsate` + `01.1166 fti`).
   - `01.1116 meN`, `01.1117 deN` (~800/883, `yak/lw` + `liT` only): closest to finish.
   - `01.1123 qIN` (378/883, san `qiqayz` vs `RiRqiz`), `01.1124 tF` (646/895, 6.4.122 `ter-` + 7.1.100/8.2.77).
   - `01.0920 dF`/`01.0921 nF` (R-roots LiT/causative), `01.1161 veY`/`01.1162 vyeY`/`01.1163 hveY` (samprasAraNa/LiT).
3. NOTE: stash `mixed-iteration WIP incl kz fix` still holds unrelated uBayapadi/nitya-san/yan-F experiments — do NOT pop as-is; split into single-trait batches with cheap pilot guard each.
4. Advance GaNa 01 beyond Milestone 1106 towards Milestone 1115+!
