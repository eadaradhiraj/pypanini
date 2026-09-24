# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-24
Sweep: **1106/1156 100%** (95.7%, raw 1106/1166)

## Done
- Panini 8.4.58 parasavarNa / 8.3.23 anusvara (dental `n -> m` before labials, `M` before sibilants):
  - Surveyed all 14 `n`+labial/s 01 cleans: 2 `np` (`tunp/trunp`), 2 `nP` (`tunP/trunP`), 6 `nB` (`SranB/sranB x2/sfnB/sinB/SunB`), 4 `ns` (`Sans/srans/Dvans/Brans`) — unanimously expect `m/M` (`tumpati`, `sramBate`, `sraMsate`, `SaMsati`). `nd` (`syand/ubund/skand`) expressly excluded (`syand`/`skand` still 100%). Zero conflicts.
  - `tinanta.py`: additive `m/M` variants in `_prim_bases` (mUla), sannanta/nijanta kartari stems, yak + san-yak + nich-yak karmani. Yang untouched (wants nasal loss: `totupyate`, `sanIsrasyate`).
  - `krdanta.py`: replacement for `Satf/SAnac/tavya/anIyar/Rvul/tfc/lyuw/GaY/tumun` (mUla/san/nich only); `kta/ktavatu/ktvA/lyap/yat` keep nasal-loss logic (`tupita/srasta/Sasta/srabDa`); yang keeps original. Extended SAnac `npa/nPa` replaces alongside existing `nsa/nSa/nBa`.
  - Also fixed `List` import breakage in `krdanta.py` (`_assimilate_t_stems -> List[str]`).
  - Full Sweep Results: passes held **1106/1156** (raw 1106/1166, 10 skipped):
    - 14 improved, +7349 matched tokens, **0 worsened** (fid-diff vs HEAD): `01.0458` 235->770, `01.0459` 235->701, `01.0471/0473/0475/0477/0497/0499/0501` 238->764, `01.0829` 258->784, `01.0857/0858/0859` 276->811, `01.0861` 235->770.
    - No new 100% passes yet (remaining gaps: liw-redup nasal `tutumpa`, ASIrliN/luN nasal loss `tupyAt`, san_krut/nich_krut/yangluk krdanta).
    - All pilots (01.0001/01.0002/01.0003) and past milestones (kz-batch 01.0760-0765, urCA 01.0239-0241, cC-batch 01.0233/34/38/42/44, 01.0865, 01.1134) held at 100%.

## Next
1. Target remaining gaps in the nasal batch (same 14 roots, one trait per iteration):
   - liw-redup nasal (`tutunpva` vs `tutumpa`, `sasranse` vs `sasraMse`): redup path uses raw clean, not `_prim_bases`.
   - ASIrliN/luN nasal loss before `y/s` (`tunpyAt` vs `tupyAt`, `atunpsIt` vs `atumpIt`?).
   - san_krut (10-51 misses) / nich_krut / yangluk krdanta for these roots.
2. Then next single-trait batch:
   - Atmane `gup`-cluster (`01.0105 zvazka~` satva-pratizedha per DAtuviSezaH 6.1.64 + `01.1125-1128` nitya-san 3.1.5/3.1.6 `jugupsate/titikzate/mImAMsate/bIBatsate` + `01.1166 fti`).
   - `01.1116 meN`, `01.1117 deN` (~800/883, `yak/lw` + `liT` only): closest to finish.
   - `01.1123 qIN` (378/883, san `qiqayz` vs `RiRqiz`), `01.1124 tF` (646/895, 6.4.122 `ter-` + 7.1.100/8.2.77).
   - `01.0920 dF`/`01.0921 nF` (R-roots LiT/causative), `01.1161 veY`/`01.1162 vyeY`/`01.1163 hveY` (samprasAraNa/LiT).
3. NOTE: stash `mixed-iteration WIP incl kz fix` still holds unrelated uBayapadi/nitya-san/yan-F experiments — do NOT pop as-is; split into single-trait batches with cheap pilot guard each.
4. Advance GaNa 01 beyond Milestone 1106 towards Milestone 1115+!
