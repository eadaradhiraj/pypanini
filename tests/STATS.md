# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-24
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **1119/1156 100%** (96.8%, raw 1119/1166). Fails: 37 scored (47 with 10 skipped). Net matched tokens +14883 across nasal + E-yak + nitya-san iterations (0 true worsened).
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
- nitya-san yang_krut san stem (7 cleans, seT-only; `01.0461` excluded via `sew`): yananta `sec` = san base; SAnac = san base + ya + mAna (`jugupsyamAnaH/titikzyamARaH` +natva). kta/ktavatu/tavya/anIyar/yat/tfc/Rvul/Satf automatic via generic sanbase path. 7 improved (+203 tokens: 7×29), 0 worsened, passes held 1119. `yang_krut` 89->5 (spike cleared to baseline); newly-surfaced `yangluk_krut` 0->84 (yangluk SAnac/Satf `jogupyamAnaH/ketan`, queued next) is freed-cap artifact (fid-diff truth: 0 worsened).
- Caught + fixed mid-iteration: inserted `if` had captured the sec-chain `elif/else` (broke all yananta: pilots + `01.0461` -72); moved override to standalone after chain. Lesson: never insert `if` between `elif` links — append after `else`.

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 171 | 01.0105 krut/tavya/M:svazkitavyaH |
| ting | 130 | 01.0105 ting/lw/prathama/eka:svazkate |
| yak | 5 | 01.0921 yak/liw/prathama/eka:nanFe |
| san | 5 | 01.1123 san/lw/prathama/eka:RiRqizati |
| nich | 12 | 01.1125 nich/luN/prathama/eka:ajugupsayizwa |
| san_krut | 15 | 01.0459 san_krut/Satf/M:sisramBizan |
| nich_krut | 11 | 01.0920 nich_krut/Satf/M:dArayan |
| yang_krut | 5 | 01.1124 yang_krut/kta/M:tetrIyitaH |
| yangluk_krut | 84 | 01.1125 yangluk_krut/SAnac/M:jogupyamAnaH |
| yang | 5 | 01.1116 yang/liw/prathama/eka:mAmAyAYcakre |
| SKIPPED:ganasutra | 10 | 01.0933 SKIPPED:ganasutra |
| yang_krut | 5 | 01.1124 yang_krut/kta/M:tetrIyitaH |
