# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-16T12:10:00+05:30
Sweep: **1000/1156 100%** (raw 1000/1166)

## Done
- Panini 1.2.18 *na ktvā seṭ*, 7.3.86 *puganta-laghūpadhasya ca*, 1.2.26 *ralo vyupadhād dhalādeḥ saṁś ca*, & 7.2.56 *uditto vā*:
  - In `krdanta.py` (`pratyaya == "ktvA"`), implemented laghūpadha guṇa for seṭ *ktvā* and optional aniw kit forms for udit roots:
    - Under 1.2.18 *na ktvā seṭ*, an affix *ktvā* that takes augment *iṭ* is *na kit*.
    - Bases with a penultimate short *ik* vowel (`i`, `u`, `ṛ`, `ḷ` followed by a single consonant) undergo guṇa by 7.3.86: `varkitvA`, `BarjitvA`, `DarjitvA`, `BarzitvA`, `garjitvA`, `parzitvA`, `varzitvA`, `GarzitvA`, `harzitvA`, `darhitvA`, `barhitvA`, `varhitvA`, `vartitvA`, `tarhitvA`.
    - Under 7.2.56 *uditto vā*, roots with `u~`/`U~` anubandha optionally omit *iṭ*, yielding kit aniw forms `BfzwvA`, `pfzwvA`, `vfzwvA`, `GfzwvA`, `hfzwvA`, `vfttvA`.
- Panini 1.3.57 *jñā-śru-smṛ-dṛśāṁ sanaḥ* & 7.4.91 *rīgṛdupadhasya ca*:
  - In `krdanta.py` (`pratyaya == "Satf"`), roots *jñā*, *śru*, *smṛ*, and *dṛś* in sannanta are strictly Ātmanepada, taking Śānac (`didfkzamARa`) rather than Śatṛ (`None`).
  - In yaṅluk, *ṛd-upadha* root `dfS` takes *rīk* augment (`arI`) in the abhyāsa, generating `darIdfSan`, `darIdfSatI`, `darIdfSat`.
- Full Sweep Results: **1000/1156 100% passes** (raw 1000/1166, 10 skipped):
  - `01.0097 vfka~`: 881 -> **883/883 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0202 BfjI~`: 881 -> **883/883 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0249 Dfja~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0255 Bfzu~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0281 gfja~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0802 pfzu~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0803 vfzu~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0805 Gfzu~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0806 hfzu~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0834 dfha~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0836 bfha~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0852 vfha~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0862 vftu~`: 881 -> **883/883 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.0942 tfha~`: 893 -> **895/895 (100.0%)** (+2 tokens) [NEW 100% PASS]
  - `01.1143 dfSi~r`: 889 -> **892/892 (100.0%)** (+3 tokens) [NEW 100% PASS]
  - 6 other roots improved (`01.0496`, `01.0648`, `01.0919`, `01.0923`, `01.1082`, `01.1092`).
  - `yangluk_krut` misses dropped to **0**!
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 36 Pilot and Milestone roots held strictly at 100.0%.

## Next
1. Investigate remaining close roots:
   - `01.1145 kfza~`: gap=9 (99.0%) failing on yak/ASIrliN (`krakzIzwa`).
   - `01.1014 SfDu~`: gap=17 (98.1%) failing on ting/lfw.
2. Advance Gaṇa 01 beyond 1000/1156 towards 1010+!
