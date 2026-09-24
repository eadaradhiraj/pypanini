# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1106/1156 100%** (95.7%, raw 1106/1166)

## Done
- krdanta nich-stem nasal (Panini 8.4.58, `_nijanta_sec` head: `np/nP/nB->m`; surveyed 10 labial cleans via nich_krut/kta — `tumpita/trumpita/tumPita/trumPita/SramBita/sramBita/sfmBita/simBita/SumBita` unanimous `m`, zero conflicts; `ns` excluded, already handled by mu/su-branch; `nd` excluded):
  - Repairs nich_krut tavya/tfc/tumun/ktvA/anIyar/yat/Rvul/lyuw; kta (mUla-based `tupita` vs `tumpita`) and SAnac (ay-retention `tumpyamAna` vs `tumpayamAna`) left as own traits.
  - Full Sweep Results: passes held **1106/1156** (raw 1106/1166, 10 skipped):
    - 10 improved, +230 matched tokens, **0 worsened** (fid-diff vs HEAD): `01.0458` 810->833, `01.0459` 732->755, `01.0471/0473/0475/0477/0497/0499/0501` 804->827, `01.0861` 810->833 (`ns`-roots 0829/0857-59 unchanged by design).
    - `nich_krut` capped misses 38->11; `yangluk_krut` rise is freed-cap artifact (fid-diff truth: 0 worsened; top example `01.0458 yangluk_krut/tavya/M:SranBitavyaH` wants `SramB...` — queued next).
    - All pilots (01.0001/01.0002/01.0003) and past milestones held at 100%.
- Prior nasal iterations (same batch): stems +7349, liw-redup +243, san-stem +308. Combined nasal work: +8130 tokens.

## Next
1. Remaining gaps in the nasal batch (one trait per iteration):
   - krdanta yanluk-stem nasal (`01.0458 yangluk_krut/tavya/M:SranBitavyaH` vs `SramB...`, `01.0829 yangluk_krut/Satf/M:Sansan` vs `SaMsan`).
   - krdanta nijanta kta sec-vs-mUla (`tupita` vs `tumpita`, `srasta` vs `sraMsita`): nijanta kta intentionally uses mUla stem — needs sec-based variant for nasal roots.
   - nich SAnac ay-retention (`tumpyamAna` vs `tumpayamAna`): check whether general or nasal-specific.
   - ASIrliN nasal loss before `y` (`tunpyAt` vs `tupyAt`, `SansyAt` vs `SasyAt`?) + luN futures.
   - yak-luN with `n` (`asransi` vs `asraMsi`, `aSranBi` vs `aSramBi`): yak-luN augment path uses raw clean.
2. Then next single-trait batch:
   - Atmane `gup`-cluster (`01.0105 zvazka~` satva-pratizedha per DAtuviSezaH 6.1.64 + `01.1125-1128` nitya-san 3.1.5/3.1.6 `jugupsate/titikzate/mImAMsate/bIBatsate` + `01.1166 fti`).
   - `01.1116 meN`, `01.1117 deN` (~800/883, `yak/lw` + `liT` only): closest to finish.
   - `01.1123 qIN` (378/883, san `qiqayz` vs `RiRqiz`), `01.1124 tF` (646/895, 6.4.122 `ter-` + 7.1.100/8.2.77).
   - `01.0920 dF`/`01.0921 nF` (R-roots LiT/causative), `01.1161 veY`/`01.1162 vyeY`/`01.1163 hveY` (samprasAraNa/LiT).
3. NOTE: stash `mixed-iteration WIP incl kz fix` still holds unrelated uBayapadi/nitya-san/yan-F experiments — do NOT pop as-is; split into single-trait batches with cheap pilot guard each.
4. Advance GaNa 01 beyond Milestone 1106 towards Milestone 1115+!
