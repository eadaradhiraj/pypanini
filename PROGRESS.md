# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-16T11:55:00+05:30
Sweep: 985/1156 100% (raw 985/1166)

## Done
- Panini 7.2.115 *aco ñṇiti*, 7.3.86 *puganta-laghūpadhasya ca*, & 1.4.11 *saṁyoge guru*:
  - In `krdanta.py` (`pratyaya == "Rvul"`), refined Ṇvul base derivation for ṛ-roots:
    - Root-ending vowels (*acaḥ*) take vṛddhi `Ar` by 7.2.115 (`Bf` -> `BArakaH`, `hf` -> `hArakaH`, `Df` -> `DArakaH`).
    - Consonant-ending roots with penultimate `ṛ` followed by a conjunct consonant (e.g. `kz` as in `vfkz`, `tfkz`, `stfkz`, `mfkz`) are *guru* by 1.4.11 *saṁyoge guru*, blocking laghūpadha guṇa (7.3.86) $\implies$ root vowel remains `ṛ` (`vfkzakaH`, `tfkzakaH`, `stfkzakaH`, `mfkzakaH`).
    - Consonant-ending roots with penultimate `ṛ` followed by a single consonant are *laghu*, taking **guṇa** `ar` (not vṛddhi) by 7.3.86 (`garhakaH`, `marzakaH`, `varDakaH`, `SarDakaH`, `marDakaH`, `sarpakaH`, `varkakaH`, `BarjakaH`, `DarjakaH`, `barhakaH`, `GarzakaH`, `harzakaH`, `vartakaH`, `tarhakaH`).
- Full Sweep Results: **985/1156 100% passes** (raw 985/1166, 10 skipped):
  - `01.0688 vfkza~`: 877 -> **883/883 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.0737 gfhU~`: 877 -> **883/883 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.0750 tfkza~`: 889 -> **895/895 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.0751 zwfkza~`: 889 -> **895/895 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.0754 mfkza~`: 889 -> **895/895 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.0804 mfzu~`: 889 -> **895/895 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.0863 vfDu~`: 877 -> **883/883 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.0864 SfDu~`: 877 -> **883/883 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.1015 mfDu~`: 889 -> **895/895 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - `01.1138 sfpx~`: 889 -> **895/895 (100.0%)** (+6 tokens) [NEW 100% PASS]
  - 18 other roots improved by +6 tokens each (net **+168 tokens** across 28 improved roots).
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 36 Pilot and Milestone roots held strictly at 100.0%.

## Next
1. Target next cluster of 14 roots with gap=2 (99.8%):
   - Panini 1.2.18 *na ktvā seṭ*: kit `ktvA` retains `f` without guṇa or with authentic sandhi: `01.0097 vfka~` (`vfkitvA`), `01.0202 BfjI~` (`BfjitvA`), `01.0249 Dfja~` (`DfjitvA`), `01.0255 Bfzu~` (`BfzitvA`), `01.0281 gfja~` (`gfjitvA`), `01.0802 pfzu~` (`pfzitvA`), `01.0803 vfzu~` (`vfzitvA`), `01.0805 Gfzu~` (`GfzitvA`), `01.0806 hfzu~` (`hfzitvA`), `01.0834 dfha~` (`dfQvA`), `01.0836 bfha~` (`bfQvA`), `01.0852 vfha~` (`vfQvA`), `01.0862 vftu~` (`vftitvA`), `01.0942 tfha~` (`tfQvA`).
2. Advance Gaṇa 01 passes from 985 towards 999+/1156!
