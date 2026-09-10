# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T19:08:00+05:30
Sweep: 967/1156 100% (raw 967/1166)

## Done
- Panini 8.4.2 *aṭkupvāṅnumvyavāye 'pi*:
  - In `krdanta.py`, implemented rigorous Paninian intervener blocking in `_natva_applies`: non-*aṭkupvāṅnum* consonants (cavarga, ṭavarga, tavarga, sibilants, `l`) intervening between the trigger (`r`, `ṣ`, `ṛ`, `ṝ`) and suffix correctly block ṇatva (*ṭavargavyavāye tu na*).
  - Stems with `w` following `z` (`tezwep-`, `tozwuB-`, `tezwip-`) correctly retain dental `n` in `SAnac`, `anIyar`, and `lyuw` (`tezwepyamAnaH`, `tezwepanIyaH`, `tezwepanam`, `tozwuByamAnaH`, `tozwuBanIyaH`, `tozwuBanam`, `tezwipyamAnaH`, `tezwipanIyaH`, `tezwipanam`).
- Panini 7.4.1 *ṇau caṅy upadhāyā hrasvaḥ* / 7.4.2 *nau caṅi*:
  - In `tinanta.py`, added guṇa and parasmaipada caṅ aorist variants for `zw`/`zW`-initial roots in ṇijanta luṅ, completing `atizwepata` for `01.0422 zwipf~`.
- Full Sweep Results: **967/1156 100% passes** (raw 967/1166, 10 skipped):
  - `01.0423 zwepf~`: 876 -> **883/883 (100.0%)** (+7 tokens) [NEW 100% PASS]
  - `01.0460 zwuBu~`: 876 -> **883/883 (100.0%)** (+7 tokens) [NEW 100% PASS]
  - `01.0422 zwipf~`: 875 -> **883/883 (100.0%)** (+8 tokens) [NEW 100% PASS]
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 21 Pilot and Milestone roots held strictly at 100.0%.

## Next
1. Target next cluster of roots with gap=227:
   - Panini 7.4.90 *rīk ca* & 7.4.91 *rīgṛdupadhasya ca*: `01.0250 Dfji~` (`dArDfjyate`), `01.0282 gfji~` (`jAgfjyate`).
   - Panini 7.4.87 *carphalagoḥ*: `01.0594 YiPalA~` / `01.0608 Pala~` (`pamPalyate`, `pamPal-`).
   - Panini 7.4.85 *nug ato 'nupadhāyāś ca*: `01.0835 dfhi~` (`dandfhyate`).
2. Advance Gaṇa 01 passes from 967 to 969+/1156.
