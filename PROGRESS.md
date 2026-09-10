# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T15:25:00+05:30
Sweep: 958/1156 100% (raw 958/1166)

## Done
- Panini 8.3.57 *iṇkoḥ*, 8.3.59 *ādeśapratyayayoḥ*, & 8.4.41 *ṣṭunā ṣṭuḥ*:
  - In Yaṅ and Yaṅluk stems, dental `st` / `sT` clusters of `zw` / `zW` upadeśa roots undergo ṣatva and ṣṭutva to `zw` / `zW` after an `iṇ` vowel in the abhyāsa (`e`, `o`), generating `tozwucya-` (`01.0199 zwuca~`), `tezwipya-` (`01.0422 zwipf`), `tezwepya-` (`01.0423 zwepf`), and `tozwuBya-` (`01.0460 zwuBu`).
  - Roots with non-`iṇ` abhyāsa vowels (`A`, `aM` such as `staBi`, `stan`, `stak`, `stam`, `sTal`) strictly retain dental `st`/`sT` per 8.3.57 *iṇkoḥ*, eliminating cross-root regressions across athematic stems.
- Panini 7.3.52 *cajoḥ ku ghiṇyatoḥ*, 7.3.59 *na kvādeḥ*, 7.3.60 *aji-vrajyoś ca*, & 8.4.58 *anusvārasya yayi parasavarṇaḥ*:
  - In `GaY` for yaṅanta kṛdantas, root-final `c`/`j` undergo kutva to `k`/`g` (`tozwukaH` for `zwuc`), with parasavarṇa assimilation of preceding palatal nasal `Y` before velars (`Yk`/`Yg` -> `Nk`/`Ng` as in `SASvaNkaH`, `momuNkaH`, `mAmaNkaH`, `pApaNkaH`, `lAlaNgaH`, `totuNgaH`).
  - kavarga-initial roots are barred from kutva by 7.3.59 *na kvādeḥ* (`cAkacaH`, `cokucaH`, `cokujaH`, `jAgarjaH`, etc.), and `vraj` is barred by 7.3.60 *aji-vrajyoś ca* (`vAvrajaH`).
- Panini 8.2.30 *coḥ kuḥ*:
  - Included `c` -> `k` devoicing and athematic endings in `yanluganta` fallback (`tozwuk` / `tozwukti`).
- Full Sweep Results: **958/1156 100% passes** (raw 958/1166, 10 skipped):
  - `01.0199 zwuca~`: 656 -> **883/883 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - Substantial improvements on adjacent roots:
    - `01.0422 zwipf`: 655 -> **875/883 (99.1%)** (+220 tokens)
    - `01.0423 zwepf`: 656 -> **876/883 (99.2%)** (+220 tokens, 100/100 tinanta)
    - `01.0460 zwuBu`: 656 -> **876/883 (99.2%)** (+220 tokens)
    - `01.0648 hveY`: 603 -> **621/895 (69.4%)** (+18 tokens)
    - `01.1165 wuo~Svi`: 405 -> **423/895 (47.3%)** (+18 tokens)
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 4 Pilot roots (`BU`, `eD`, `sparD`, `sev`) and all previous milestone roots held strictly at 100.0%.

## Next
1. Target remaining closest roots to 100%:
   - `01.0463 japa~` (668/895, gap=227): Panini 7.4.86 *nuś ca* -> `jaYjapyate` in yaṅ / yaṅ_yak / yaṅ_krut.
   - `01.1146 daha~` (668/895, gap=227): Panini 7.4.86 *nuś ca* -> `dandahyate` / `daMdahyate`.
   - `01.0979 pata~` (668/895, gap=227): Panini 7.4.87 *carfalaghoḥ* -> `panIpatyate`.
   - `01.0423 zwepf` (876/883, gap=7): yaṅ_krut SAnac/anIyar/lyuw natva adjustment.
2. Advance Gaṇa 01 passes from 958 to 959+/1156.
