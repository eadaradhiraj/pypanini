# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1106/1156 100%** (95.7%, raw 1106/1166)

## Done
- primitive yak-luN nasal (Panini 8.4.58/8.3.23, same 14-root `n`+labial/s survey; san/nich yak-luN already covered via stem variants, yang untouched):
  - `tinanta.py`: assimilated aug variants (`atumpi/asraMsi/aSaMsi/asramBi`) appended to the primitive yak-luN table. Additive.
  - Full Sweep Results: passes held **1106/1156** (raw 1106/1166, 10 skipped):
    - 14 improved, +126 matched tokens, **0 worsened** (fid-diff vs HEAD): `01.0458` 833->842, `01.0459` 755->764, `01.0471/0473/0475/0477/0497/0499/0501` 827->836, `01.0829` 824->833, `01.0857/0858/0859` 851->860, `01.0861` 833->842.
    - `yak` capped misses 35->10; newly-surfaced tinanta `yangluk` (10, e.g. `01.0458 yangluk/lw:SASranBaH`) and `yangluk_krut` 39->54 are freed-cap artifacts (fid-diff truth: 0 worsened) — yangluk redup+nasal queued next.
    - All pilots (01.0001/01.0002/01.0003) and past milestones held at 100%.
- Prior nasal iterations (same batch): stems +7349, liw-redup +243, san-stem +308, nich-stem +230. Combined nasal work: +8256 tokens.

## Next
1. Yangluk redup + nasal (one trait per iteration):
   - krdanta yangluk-stem nasal (`01.0458 yangluk_krut/tavya/M:SranBitavyaH` vs `SASramBitavya`, `01.0829 yangluk_krut/Satf/M:Sansan` vs `SASaMsan`): yangluk tavya unanimous `m/M` per survey, kta wants loss (`totupita/SASrabDa`) — mirror the mUla pattern (exclude kta/ktavatu). Needs yangluk redup (`to-/SA-/sanI-` with dIrgha) + nasal.
   - tinanta yangluk lw (`01.0861 yangluk/lw:sAsranBsi` vs `sAsramBsi`, `01.0471 totunpTaH` vs `totump...`): additive redup-nasal variant; note `01.0857` yangluk lw already passes (keep `n`-form too).
2. Then remaining nasal gaps: krdanta nijanta kta (`tupita` vs `tumpita`), nich SAnac ay-retention (`tumpyamAna` vs `tumpayamAna`), ASIrliN nasal loss (`tunpyAt` vs `tupyAt`), krut/yat nasal (`sransya` vs `sraMsya`), krut/ktvA variants.
3. Then next single-trait batch:
   - Atmane `gup`-cluster (`01.0105 zvazka~` satva-pratizedha per DAtuviSezaH 6.1.64 + `01.1125-1128` nitya-san 3.1.5/3.1.6 `jugupsate/titikzate/mImAMsate/bIBatsate` + `01.1166 fti`).
   - `01.1116 meN`, `01.1117 deN` (~800/883, `yak/lw` + `liT` only): closest to finish.
   - `01.1123 qIN` (378/883, san `qiqayz` vs `RiRqiz`), `01.1124 tF` (646/895, 6.4.122 `ter-` + 7.1.100/8.2.77).
   - `01.0920 dF`/`01.0921 nF` (R-roots LiT/causative), `01.1161 veY`/`01.1162 vyeY`/`01.1163 hveY` (samprasAraNa/LiT).
4. NOTE: stash `mixed-iteration WIP incl kz fix` still holds unrelated uBayapadi/nitya-san/yan-F experiments — do NOT pop as-is; split into single-trait batches with cheap pilot guard each.
5. Advance GaNa 01 beyond Milestone 1106 towards Milestone 1115+!
