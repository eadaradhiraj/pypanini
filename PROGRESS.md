# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-16T17:00:00+05:30
Sweep: **1020/1156 100%** (88.2%, raw 1020/1166)

## Done
- Panini 6.4.66 *ghu-mā-sthā-gā-pā-jahāti-sāṁ hali* & Vārttika *ghrā-dhmayoś ca*:
  - In Yaṅanta, roots ending in `A` (`pA`, `GrA`, `DmA`, `sTA`, `gA`, `gE`) replace `A` with `ī` (`I`) before the halādi kṅit affix `yaṅ` (`ya`), with abhyāsa guṇa `e` by Panini 7.4.82 *guṇo yaṅ-lukoḥ*, producing `pepIya-`, `jeGrIya-`, `deDmIya-`, `tezWIya-`, `jegIya-` across all 10 lakāras in kartari/karmani and all yaṅanta kṛdantas (`jeGrIyaRIyaH`, `jeGrIyakaH`, `deDmIyaRIyaH`, `deDmIyakaH`...). Roots not in 6.4.66 like `mnA` retain `A` (`mAmnAya-`). Unlocked `01.1075 GrA` and `01.1076 DmA` to 100.0%.
- Panini 6.4.24 *aniditāṁ hala upadhāyāḥ kṅiti*, 6.4.25 *daṁśa-svañja-ṣvañjāṁ śapi*, & 6.4.26 *rañjeś ca*:
  - Penultimate nasal is elided before `śap` (`lw`, `low`, `laN`, `viDiliN` in kartari tinanta, and `SAnac` / `cAnaS` in kṛdanta) for `danS` -> `daS` (`daSati`, `daSamAnaH`), `svaYj` / `zvaYj` -> `svaj` (`svajate`, `svajamAnaH`), `saYj` / `zaYj` -> `saj` (`sajati`, `sajamAnaH`), and `raYj` -> `raj` (`rajati`, `rajate`, `rajamAnaH`).
  - In yaṅluk Śatṛ, penultimate nasal drops by 6.4.24, yielding non-num abhyasta forms by 7.1.78 *nābhyastāc chatuḥ*: `daMdaSat`/`dandaSat` (`01.1144`), `sAsvajat` (`01.1131`), `sAsajat` (`01.1142`), `rArajat` (`01.1154`).
  - Unlocked `01.1131 zvanja~`, `01.1142 zaYja~`, `01.1144 danSa~`, and `01.1154 raYja~` to 100.0%.
- Panini 8.4.58 *anusvārasya yayi parasavarṇaḥ* & 8.3.24 *naś cāpadāntasya jhali*:
  - In sannanta stems before `kz` (`k` $\in yay$), penultimate nasals (`n`, `Y`, `M`) assimilate to velar nasal `N` (`danS` -> `didaNkzati`, `svaYj` -> `sisvaNkzate`, `saYj` -> `sisaNkzati`, `raYj` -> `riraNkzati`/`riraNkzate`).
  - Penultimate nasal elision in `_kta_stem` protects sannanta stems ending in `s` (`ninaMsita`, `riraMsita`, `yiyAMsita`, `jigAMsita`).
- Panini 6.1.101 *akaḥ savarṇe dīrghaḥ* & 7.3.33 *āto yuk ciṇ-kṛtoḥ*:
  - In kṛdanta, `A`-ending roots take savarṇa dīrgha in `anIyar` (`mnAnIyaH`, `GrARIyaH`, `DmAnIyaH`, `pAnIyaH`, `sTAnIyaH`) and `lyuw` (`mnAnam`, `GrARam`, `DmAnam`, `pAnam`, `sTAnam`).
  - Before vowel-initial kṛt affixes (`Rvul`, `GaY`), `A`-ending roots take augment `yuk` (`y`) by 7.3.33, yielding `mnAyakaH`, `GrAyakaH`, `DmAyakaH`, `pAyakaH`, `sTAyakaH` in `Rvul` and `mnAyaH`, `GrAyaH`, `DmAyaH`, `pAyaH`, `sTAyaH` in `GaY`.
  - In yaṅluk Śatṛ, `A`-ending abhyasta stems drop `A` by 6.4.112 *śnābhyastayor ātaḥ*, taking non-num endings by 7.1.78 (`mAmnat`, `jAGrat`, `dADmat`, `tAsTat`).
  - Unlocked `01.1078 mnA` to 100.0%.
- Panini 8.4.1 *raṣābhyāṁ no ṇaḥ samānapade* & 8.4.2 *aṭkupvāṅnumvyavāye 'pi*:
  - Root-final vowels belong to `aṭ` and do not block ṇatva across the stem to suffix `n`. Vowel-final roots containing trigger `r`/`z`/`f` undergo ṇatva (`GrA` -> `GrARIyaH`, `GrARam`).
  - When root-initial `s` undergoes ṣatva to `z` in the abhyāsa, internal `n` across intervening vowels/velars/labials undergoes ṇatva to `R` (`zivi~` -> `siziRv-`, `seziRv-`).
  - Unlocked `01.0674 zivi~` to 100.0%.
- Panini 7.4.85 & 7.4.86 *nuṅ* augment in Yaṅ/Yaṅluk:
  - Nasal-coda roots (`n`, `R`, `m`) with vowel `a` or `ṛ` receive `yan_vowel = "aM"`, correctly preventing false `rīk` insertion on antepenultimate `ṛ` (`GfRi~` -> `jaMGfRRyate` / `jaNGfRRyate`).
  - Unlocked `01.0504 GfRi~` to 100.0%.
- Full Sweep Results: **1020/1156 100% passes** (raw 1020/1166, 10 skipped):
  - `01.0504 GfRi~`: 627 -> **883/883 (100.0%)** (+256 tokens) [NEW 100% PASS]
  - `01.0674 zivi~`: 667 -> **895/895 (100.0%)** (+228 tokens) [NEW 100% PASS]
  - `01.1075 GrA`: 454 -> **895/895 (100.0%)** (+441 tokens) [NEW 100% PASS]
  - `01.1076 DmA`: 463 -> **895/895 (100.0%)** (+432 tokens) [NEW 100% PASS]
  - `01.1078 mnA`: 501 -> **895/895 (100.0%)** (+394 tokens) [NEW 100% PASS]
  - `01.1131 zvanja~`: 547 -> **883/883 (100.0%)** (+336 tokens) [NEW 100% PASS]
  - `01.1142 zaYja~`: 451 -> **895/895 (100.0%)** (+444 tokens) [NEW 100% PASS]
  - `01.1144 danSa~`: 558 -> **895/895 (100.0%)** (+337 tokens) [NEW 100% PASS]
  - `01.1154 raYja~`: 541 -> **895/895 (100.0%)** (+354 tokens) [NEW 100% PASS]
  - 61 other roots improved.
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 36 Pilot and Milestone roots held strictly at 100.0%.

## Next
1. Target next closest failing roots from `tests/sweep_all.csv`:
   - `01.1101 gA` (85.8% -> 90.1%, gap=87): `gAate` -> `gAte` (Panini 6.1.101).
   - `01.1077 sTA` (574 -> 631/895, 70.5%): Āśīrliṅ `sTEyAt` (Panini 6.4.67).
   - `01.1079 dA` (590/895, 65.9%): Āśīrliṅ `deyAt` (Panini 6.4.67).
   - `01.1102 uN` (388/627, 61.9%): `uAYcakre` am-anta liṭ.
2. Advance Gaṇa 01 beyond 1020/1156 towards 1030+/1156!
