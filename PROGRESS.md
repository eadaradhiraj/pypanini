# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-16T11:43:00+05:30
Sweep: 975/1156 100% (raw 975/1166)

## Done
- Panini 7.4.91 *rīgṛdupadhasya ca* & 8.2.18 *kṛpo ro laḥ*:
  - In `tinanta.py` (`_yan_stem` and `_yanlug_stem`) and `krdanta.py` (`_yan_sec`), implemented augment *rīk* (`arI`) in the abhyāsa for roots having penultimate `ṛ` (*ṛd-upadha*, i.e. short `ṛ` followed by a consonant).
  - For `kfp`, implemented Panini 8.2.18 *kṛpo ro laḥ* to generate augment *līk* (`alI`) and root base `kxp` (`calIkxpyate`).
  - Extended ṣatva and ṣṭutva rule (*iṇkoḥ* 8.3.57 + *ādeśapratyayayoḥ* 8.3.59 + *ṣṭunā ṣṭuḥ* 8.4.41) so that `zw`-upadeśa roots like `01.0751 zwfkza~` undergo ṣṭutva after `arI`/`alI` (`tarIzwfkzyate`).
  - Combined with Panini 8.4.1 / 8.4.2 intervener rules, correctly produced retroflex participles where permitted (`varIvfkyamARaH`, `darIdfMhyamARaH`) and dental participles where non-aṭkupv consonants intervene (`darIDfYjyamAnaH`, `jarIgfYjyamAnaH`, `varIvftyamAnaH`).
- Full Sweep Results: **975/1156 100% passes** (raw 975/1166, 10 skipped):
  - `01.0250 Dfji~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0282 gfji~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0454 jfBi~`: 627 -> **883/883 (100.0%)** (+256 tokens) [NEW 100% PASS]
  - `01.0682 kfvi~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0835 dfhi~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0837 bfhi~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0877 vfhi~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0943 tfhi~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - 31 other roots improved by +1 to +227 tokens each (net **+8,416 tokens** across 39 improved roots).
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 28 Pilot and Milestone roots held strictly at 100.0%.

## Next
1. Target next high-leverage generative improvements:
   - Panini 7.2.115 *aco ñṇiti* & 7.2.116 *ata upadhāyāḥ* (vṛddhi `ar` -> `Ar` in ṇvul) and 1.2.18 *na ktvā seṭ* (kit ktvA retaining `f` without guṇa `vfkitvA`, `BfjitvA`, `DfjitvA`...): unlocks 20+ roots currently at gap 6–8 to 100.0% (`01.0688`, `01.0737`, `01.0750`, `01.0751`, `01.0754`, `01.0804`, `01.0863`, `01.0864`, `01.1015`, `01.1138`, `01.0097`, `01.0202`, `01.0249`, `01.0255`, `01.0281`, `01.0802`, `01.0803`, `01.0805`, `01.0806`, `01.0834`, `01.0836`, `01.0852`, `01.0862`, `01.0942`).
   - Panini 7.4.87 *carphalagoḥ*: `01.0594 YiPalA~` & `01.0608 Pala~` (`paMPulyate`).
2. Advance Gaṇa 01 passes from 975 towards 985+/1156.
