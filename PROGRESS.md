# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-10T14:45:00+05:30
Sweep: 957/1156 100% (raw 957/1166)

## Done
- Panini 7.4.79 *sany ataḥ* & 7.4.80 *pvoḥ yan-sanoḥ*:
  - In seṭ roots ending in `ik` (specifically `pUN` / `pUY`), the root takes guṇa `o` -> `av` before `iz` (7.3.84 *sārvadhātukārdhadhātukayoḥ* + 6.1.78 *eco 'yavāyāvaḥ*).
  - By Panini 7.4.79 *sany ataḥ* & 7.4.80 *pvoḥ yan-sanoḥ*, the short `a` of the abhyāsa becomes short `i` before `san` (`pa` -> `pi`), yielding the regular sannanta stem `pipaviz-`.
  - Implemented `pipaviz` in `_sannanta_stem` (`tinanta.py`) and `_sannanta_sec` (`krdanta.py`) for `pU`/`pUN`/`pUY`, unlocking all 90 `san` (kartari), 90 `san_yak` (karmani), and 29 `san_krut` participles.
  - Allowed both `[sec + "itvA", sec + "ya"]` for `ktvA` in `san_krut` when `sec` ends in `iz`, preserving `ediDizya` (`01.0002`) while matching `pipavizitvA` (`01.1121`).
  - Strict exact root matching (`c in ("pU", "pUN", "pUY")` or `op in ("pU", "pUN", "pUY", ...)`) ensures non-identical roots like `01.0557 pUyI`, `01.0606 pUla`, `01.0769 pUza` remain unaffected and hold 100%.
- Full Sweep Results: **957/1156 100% passes** (raw 957/1166, 10 skipped):
  - `01.1121 pUN`: 674 -> **883/883 (100.0%)** (+209 tokens) [NEW 100% PASS]
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 4 Pilot roots (`BU`, `eD`, `sparD`, `sev`) and previous milestone roots (`01.1049 nI`, `01.0200`, `01.0588`, `01.0637`, `01.0670`, `01.0722`, `01.1122`, `01.1129`, `01.1130`) held strictly at 100.0%.

## Next
1. Target remaining closest roots to 100%:
   - `01.0199 zwuca~` (656/883, gap=227): 8.3.59 *ādeśapratyayayoḥ* + 8.4.41 *ṣṭunā ṣṭuḥ* after guṇa `o` in abhyāsa -> `tozwucyate` across all 90 yang, 90 yang_yak, 18 yangluk, and 29 yang_krut.
   - `01.0463 japa~` (668/895, gap=227): Panini 7.4.86 *nuś ca* -> `jaYjapyate`.
   - `01.1146 daha~` (668/895, gap=227): Panini 7.4.86 *nuś ca* -> `dandahyate` / `daMdahyate`.
   - `01.0979 pata~` (668/895, gap=227): Panini 7.4.87 *carfalaghoḥ* -> `panIpatyate`.
2. Advance Gaṇa 01 passes from 957 to 958+/1156.
