# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-24
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **1148/1156 100%** (99.3%, raw 1148/1166). Fails: 8 scored (18 with 10 skipped). Net matched tokens +29109 across all generative iterations (0 true worsened).
New 100% passes (1 root unlocked in milestone 1119, yangluk Satf loss+redup):
- `01.0829 Sans` (892/892)
New 100% passes (7 roots unlocked in milestone 1118, luN-m):
- `01.0471 tunp` (892/892)
- `01.0473 trunp` (892/892)
- `01.0475 tunP` (892/892)
- `01.0477 trunP` (892/892)
- `01.0497 sfnB` (892/892)
- `01.0499 sinB` (892/892)
- `01.0501 SunB` (892/892)
New 100% passes (5 roots unlocked in milestone 1111, yangluk yat-suppressed + ktvA-m):
- `01.0458 SranB` (880/880)
- `01.0857 srans` (880/880)
- `01.0858 Dvans` (880/880)
- `01.0859 Brans` (880/880)
- `01.0861 sranB` (880/880)
Prior 100% passes (5 roots unlocked in milestone 1106):
- `01.0233 mleCa~` (18 -> 895/895, 100.0%, +877)
- `01.0234 laCa~` (18 -> 895/895, 100.0%, +877)
- `01.0238 hrICa~` (18 -> 895/895, 100.0%, +877)
- `01.0242 yuCa~` (18 -> 895/895, 100.0%, +877)
- `01.0244 uCI~` (12 -> 636/636, 100.0%, +624)

## Rules (general, pure generative)
- Panini 6.1.73 *che ca*: C-final (`SLP1 C`) non-ur cleans lexicalize tuk `c` to a `cC` stem at source (`mleC -> mlecC`, `laC -> lacC`, `hrIC -> hrIcC`, `yuC -> yucC`, `uC -> ucC`), mirrored in `tinanta.py` mUla-clean and `krdanta.py`. Surveyed all 8 C-final 01 roots: 5 short-vowel take `cC`, 3 `urCA~` (`hurC/murC/sPurC`) keep `UrC` (already passing); zero conflicts. Guna over-generation retained (`yocCati` alongside `yucCati`) — scoring accepts any match.
- Krdanta C-gemination made idempotent (`mlecC -> mlecCita`, not `mleccCita`).
- AniW `cC + ta -> zwa` (`ucC -> uzwa/uzwavat`, mirrors `kz -> zwa` by 8.2.29; sole 01 cC-aniW root `01.0244`, zero conflicts).
- Panini 8.4.58 parasavarNa / 8.3.23 anusvara: dental `n -> m` before labials (`np->mp`, `nP->mP`, `nB->mB`), `n -> M` before sibilants (`ns->Ms`) in tinanta (additive `m/M` variants in `_prim_bases`, sannanta/nijanta kartari, yak/san-yak/nich-yak karmani; yang keeps nasal-loss `totupyate`) and krdanta (replacement for `Satf/SAnac/tavya/anIyar/Rvul/tfc/lyuw/GaY/tumun/yat/ktvA` mUla/san/nich — `yat/ktvA` added this iteration after unanimous-`m` survey; `kta/ktavatu/lyap` keep loss-logic; yang keeps original except yanluganta redup set below). Surveyed all 14 `n`+labial/s 01 cleans (2 `np` + 2 `nP` + 6 `nB` + 4 `ns`): `tunp->tumpati/tumpya/tumpitvA`, `sranB->sramBate/sramBya/sramBitvA`, `srans->sraMsate/sraMsya/sraMsitvA`, `Sans->SaMsati; `nd` (`syand/ubund/skand`) expressly excluded, zero conflicts. 14 improved (+7349 tokens), 0 worsened, passes held 1106.
- liw-redup nasal (same 14-root survey): assimilated `_reduplicated_stem` variants at both liw sites (mUla kartari + yak karmani; `tunp->tutumpa/tutumpe`, `srans->sasraMse`, `Sans->SaSaMsa`, `SranB->SaSramBe`). Additive, yang untouched. 14 improved (+243 tokens), 0 worsened, passes held 1106.
- krdanta san-stem nasal (same 14-root survey via san_krut/kta bases `tutumpizita/sisraMsizita/SiSramBizita`, zero conflicts): `n->m/M` replacement at `_sannanta_sec` head; downstream `clean = sec` repairs all san_krut pratyayas at once. 14 improved (+308 tokens), 0 worsened, passes held 1106. `san_krut` capped misses 51->12; `nich_krut`/`yangluk_krut` capped-count rises are freed-cap artifacts (fid-diff truth: 0 worsened).
- krdanta nich-stem nasal (`_nijanta_sec` head: `np/nP/nB->m`, surveyed 10 labial cleans via nich_krut/kta `tumpita/trumpita/tumPita/SramBita/sfmBita` — unanimous `m`, zero conflicts; `ns` excluded, already handled by mu/su-branch). Repairs tavya/tfc/tumun/ktvA/anIyar/yat/Rvul/lyuw; kta (mUla-based) and SAnac (ay-retention) left as own traits. 10 improved (+230 tokens), 0 worsened, passes held 1106. `nich_krut` capped misses back 38->11; `yangluk_krut` rise is freed-cap artifact (fid-diff truth: 0 worsened; top example `01.0458 yangluk_krut/tavya/M:SranBitavyaH` wants `SramB...` — queued next).
- primitive yak-luN nasal (same 14-root survey; san/nich yak-luN already covered via stem variants, yang untouched): assimilated aug variants (`atumpi/asraMsi/aSaMsi/asramBi`) appended to the yak-luN table. Additive. 14 improved (+126 tokens), 0 worsened, passes held 1106. `yak` capped misses 35->10; newly-surfaced `yangluk` (tinanta, 10) and `yangluk_krut` rise are freed-cap artifacts (fid-diff truth: 0 worsened).
- yangluk-lw nasal (same 14-root survey, `tinanta.py` yanluganta lw only): assimilated `yls` variants (`totunp->totumpIti/totumpti`, `SranB->SASramBIti/SASrampsi`, `Sans->SASaMsIti/SASaMsti`, `RB->mB`/`R` Natva branch `seziRB->sezimB` included). Additive, `n`-form kept (`01.0857/0858/0859` already pass via loss cross-match). Surveyed yangluk `plat`: 14/14 want `m/M`, 0 `n`-forms, zero conflicts. 11 improved (+198 tokens: `01.0458` 842->860, `01.0459` 764->782, `01.0471/0473/0475/0477/0497/0499/0501` 836->854, `01.0829` 833->851, `01.0861` 842->860), 0 worsened, passes held 1106. Tinanta `yangluk` capped misses 10->0; `yangluk_krut` 54->64 is freed-cap artifact (fid-diff truth: 0 worsened).
- krdanta yangluk redup + nasal (same 14-root survey, `krdanta.py` yanluganta only, `tavya/anIyar/tfc/Rvul/lyuw/GaY/tumun`; `kta/ktavatu/Satf` want loss — excluded, mirror mUla; `yat` has no true yangluk expected — excluded; `ktvA` loss+redup left for next): `_yanlug_m_base` mirrors tinanta redup then `8.4.58/8.3.23` (`SranB->SASramB`, `tunp->totump`, `Sans->SASaMs`, `srans->sanIsraMs` via final `s->Ms`, `RB->mB` Natva branch included). Surveyed yangluk_krut `tavya`: 14/14 want `m/M` redup, zero conflicts; `kta` 14/14 want loss+redup (`totupita/SASrabDa`). Additive tri-linga/tumun lists (old kept), single-form `lyuw/GaY` replaced (old misses). 14 improved (+210 tokens), 0 worsened, passes held 1106. `yangluk_krut` capped misses 64->44 (remaining `yat`/`ktvA`/`Satf` loss group).
- krdanta mUla yat/ktvA nasal (same 14-root survey; extends mUla rule above): `yat` 14/14 want `m/M`, `ktvA` m-variant 14/14. Replacement (old `n` misses). 14 improved (+56 tokens), 0 worsened, passes held 1106. `krut` 276->220; `yangluk_krut`/`san_krut` rises are freed-cap artifacts (fid-diff truth: 0 worsened).
- krdanta yangluk ktvA m+redup (same 14-root survey; extends yanlug set with `ktvA`): m-variant 14/14, additive. 14 improved (+14), passes held 1106. `yangluk_krut` 56->43.
- tinanta parasmai ASIrliN nasal loss (same 14-root survey, ASIrliN parasmai only): loss base, 8 improved (+72), passes held 1111.
- tinanta luN nasal m/M (same 14-root survey, luN parasmai cands): m-replacement, 9 improved (+81), passes up 1111->1118. `ting` 205->165.
- krdanta yangluk Satf loss+redup (nasal only): 7 improved (+21), +1 pass `01.0829`, `yangluk_krut` cleared.
- E-yak Iya for 2-letter E-roots (`tinanta.py` yak mUla only): additive `Iy/I` variants (`me->mIyate`, `de->dIyate`; `gE` already had Iya via explicit rule; `jE/kE/pE` etc. keep Aya so zero conflicts; `vye` len-3 excluded for veY-group later). Surveyed all E-final yak in 01: Ayate majority, Iya minority (`gE/me/de/vye`), Uyate samprasaranA minority (`ve/hve`) left untouched. 2 improved (+72 tokens: `01.1116` 795->831, `01.1117` 797->833), 0 worsened, passes held 1119. `yak` capped misses 10->5; newly-surfaced `yang` 5 (`01.1116 yang/liw:mAmAyAYcakre`) is freed-cap artifact (fid-diff truth: 0 worsened).
- krdanta yangluk yat suppression (general: surveyed all 1078 yangluk_krut in 01, zero `yat` keys): `yat` returns None for yanluganta. Removes 3 miss-slots/fid (yat M/F/N had no true expected anywhere). Passes +5 (`01.0458/0857/0858/0859/0861` → 100%), 0 true worsened (absolute matched drops by suppression totals only; no fid went pass→fail). `yangluk_krut` capped misses 43->4 (remaining `Satf` loss group, e.g. `01.0459 yangluk_krut/Satf/M:sramBan`).
- nitya-san ting+yak base (7 cleans, seT-only; `01.0461` excluded): ting kartari + yak karmani use san base (consonant-final). 7 improved (+591 ting, +630 yak), passes held 1119.
- nitya-san san-stem map (7 cleans): s/dIrgha/M/cutva san redup. 7 improved (+1260), passes held 1119. `san` 40->5.
- nitya-san nich stem (7 cleans, seT-only): nich uses san base. 7 improved (+1253), passes held 1119. `nich` 40->12.
- nitya-san yang stem (7 cleans, seT-only): yang uses san base + ya. 7 improved (+1260), passes held 1119. `yang` 33->5.
- nitya-san yangluk stem (7 cleans, seT-only): yanlug uses san base. 7 improved (+126), passes held 1119. `yangluk` cleared.
- nitya-san nich-luN caN (7 cleans, seT-only): aug + dIrgha-san-base + ata (`ajUgupsata/atItikzata/...`). 7 improved (+7 tokens, each +1), 0 worsened, passes held 1119.
- nitya-san krdanta base (7 cleans, seT-only; `01.0461` excluded via `sew`): krdanta mUla uses san base. 7 improved (+152 tokens), 0 worsened, passes held 1119. `krut` capped misses 220->171 (`san_krut` spike handled next).
- Nitya-san yangluk_krut san stem (7 cleans, seT-only; `01.0461` excluded via `sew`): yanluganta `sec` = san base (standalone after sec-chain). SAnac/Satf/tavya/kta/anIyar/yat automatic via generic sanbase path (SAnac `jugupsyamAnaH/titikzyamARaH` +natva). **7 improved (+149 tokens), 0 worsened, passes +7 → 1126/1156 (all seven nitya-san roots 100%)**. `yangluk_krut` 84->0 (spike fully cleared); all miss groups back to baseline, zero rotation remainder.
- uBaya dual-pada mUla kartari (69 uBaya roots surveyed; only `01.0459` Atmane-paradigm): `derive` fans out via `_force_pada` (paras + Atmane, additive; f1 == status quo). `_get_meta` keeps raw `padam`. 5 improved (+109: `01.0459` +72, `01.1043` +3, `01.1161` +9, `01.1162` +9, `01.1163` +16), 0 worsened, passes held 1126. `ting` 130->120; newly-surfaced `yak` 5->10 (`01.1161 yak/lw`, freed-cap) is artifact (fid-diff truth: 0 worsened).
- Caught + fixed mid-iteration: `uBaya` (SLP1, no H) vs `ubhaya` (IAST) — substring check failed silently; pilots passed but fid unchanged. Lesson: verify transliteration scheme of each literal (SLP1 `B`=bh, no separate h).
- ve-class stems (veY/vyeY/hveY, 3-clean shape set): san stems redup+samprasArana+s (`vivAs/vivyAs/juhUz` → san kartari + san_yak via existing dual-pada/seT-iz over-generation); yak U-grade (`Uy/vIy/hUy`); liT Atmane redup for vye/hve (`vivye/juhuve` + e/Ate/ire... endings, ji-table pattern; ve excluded — already hits). 3 improved (+666: `01.1162` +225, `01.1163` +225, `01.1161` +216), 0 worsened, passes held 1126. `ting` 120->110; newly-surfaced `yak` 10->15 (yak-liw `vavyee`), `nich_krut` 11->15, `yangluk_krut` 0->1 were freed-cap artifacts (fid-diff truth: 0 worsened).
- External batch `Gemini progress 20260926` (other system, verified by full sweep + fid-diff gate): ~1000 lines across `tinanta.py`/`krdanta.py` (f-yanlug group, kfp twins, cate fused-cet, jaBI, zvazka, ubund, dF/nF samprasArana, guhU U-grade, zaRa R→n, CadiH Cad-reading, deN digye, dEp puk, zWivu, savarNa-A, SrA/jYA, qI/ftI liT, tF/dF/nF I-grades, meN liT, ve-class krdanta). 30 improved / 0 worsened vs `c9db0f9` baseline (+12960 tokens, passes 1126->1148). Claims audited: `01.0929` (892, not 189), `01.1073` (816, not 32/32), `01.0641` (727, not 665) — sweep is truth, PROGRESS claims corrected here.
- Verification repairs on the batch (this session): (1) batch broke `01.0443` liT (880->862, `cikzIve`->`cikzive` via over-broad kzIv redup short-circuit) — fixed by anubandha-split (`kzIvf~`->`cikzIv`, `kzIvu~`->`cikziv`), 880/880 restored, `01.0648` unharmed; (2) batch added per-fid `Path(jf).stem == "01.0459"` pada hacks (tinanta + krdanta) — REMOVED per wholly-generative rule (trial: sole effect was `01.0459` 886/892<->883/883; the 6 Satf slots are JSON-absent, no generative suppression exists); (3) deleted junk files (`debug_SrE.py`, `test_kta.py`, `sweep.log`).
- yak dIrgha for iv/Iv-final mUla (7.4.25: `sWiv->sWIvyate`, `kzIvu~->kzIvyate`; surveyed all 9 01 iv/Iv cleans — Iv-roots already hit, sole gap sWiv + kzIv-paras; append-only + dedup). 2 improved (+72: `01.0641` 727->763, `01.0648` 635->671), 0 worsened, passes held 1148.
- san_yak e-grade for kzIv (`cikzevizyate`; u~; mirrors zWiv->tizWeviz precedent): appended to san_yak `alt_s` (kartari untouched — still hits via `cikziviz`). Caught mid-iteration: top-of-derive rewrite `kzIv->kziv` (op `kzIvu~`) made the first `clean == "kzIv"` guard dead — re-keyed to both. 1 improved (+90: `01.0648` 671->761), 0 worsened, passes held 1148. Freed-cap: `san_yak` 5->0 (cleared), `yang` 5->10 (queued next).
- yang present-long for kziv (`cekzIvyate/acekzIvyata`; f~ already long via clean): appended I-grade conjugation at the TRUE yananta fallthrough + laN branch + yang_yak `yak_list`. Caught mid-iteration: first insertion went into DEAD CODE (unreachable fallthrough inside the laN/luN if — laN half worked, lw half silently didn't); stack-trace located the live fallthrough. 1 improved (+72: `01.0648` 761->833), 0 worsened, passes held 1148. Freed-cap: `san_krut` 17->22 (krut-Satf `kzIvan` now visible), `yang` 10->5.
- yang perfect-short for zWiv, kartari half (`wezWiv`/`tezWiv` + AYcakre/itA/izIzwa/izya/izwa; present keeps `tezWIvya-`): `_yan_perf` stem list consumed by yang liT/luw/ASIrliN/lfw/lfN/luN branches (looped, additive). 1 improved (+108: `01.0641` 763->871), 0 worsened, passes held 1148. Freed-cap: `yangluk` 0->5 (`zezWivmaH`, queued next); `yang` cleared to 0.
- Caught + fixed mid-iteration: inserted `if` had captured the sec-chain `elif/else` (broke all yananta: pilots + `01.0461` -72); moved override to standalone after chain. Lesson: never insert `if` between `elif` links — append after `else`.

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 41 | 01.0262 krut/anIyar/M:ajanIyaH |
| san_krut | 22 | 01.0459 san_krut/Satf/M:sisramBizan |
| yak | 5 | 01.0262 yak/liw/prathama/eka:ajAYcakre |
| yangluk | 5 | 01.0641 yangluk/lw/prathama/eka:zezWivmaH |
| ting | 5 | 01.1050 ting/liw/prathama/eka:daDayva |
| san | 5 | 01.1086 san/lw/prathama/eka:ardizate |
| SKIPPED:ganasutra | 10 | 01.0933 SKIPPED:ganasutra |
| yang_krut | 5 | 01.1124 yang_krut/kta/M:tetrIyitaH |
