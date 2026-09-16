# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-16T13:05:00+05:30
Sweep: **1011/1156 100%** (87.5%, raw 1011/1166)

## Done
- Panini 8.2.41 *ṣaḍhoḥ kaḥ si*:
  - In `pypanini/tinanta.py` line 870: added unstrengthened `kfkz` to s-stems for `kfz`/`karz`/`kArz` (`kfkzIzwa` in yak Āśīrliṅ). Unlocked `01.1145 kfza~` to 100.0%.
- Panini 1.3.92 *vṛdbhyaḥ syasanoḥ*:
  - In `tinanta.py` (`lfw` and `lfN`): roots of *vṛt-ādi* (`vft`, `vfD`, `SfD`, `syand`, `kfp`) optionally take Parasmaipada in *sya* alongside their natural Ātmanepada, allowing both padas in kartari. Unlocked `01.1014 SfDu~` to 100.0%.
- Panini 7.4.67 *dyutisvāpyoḥ saṁprasāraṇam*:
  - In `tinanta.py` (`_yan_stem`, `_yanlug_stem`) and `krdanta.py` (`_yan_sec`): `dyut` takes saṁprasāraṇa `i` + guṇa `e` in abhyāsa (`dedyut-`). Unlocked `01.0842 dyuta~` to 100.0%.
- Panini 8.3.59 *ādeśapratyayayoḥ* & Anubandha Stripping:
  - Roots with upadeśa initial `z` (`zvida~`, `zfBu~`, etc.) undergo ṣatva after an *iṇ* vowel in the abhyāsa (`sezvid-`, `sarIzfB-`).
  - `_op0` strips initial anubandhas (`wuo`, `quo`, `wu`, `qu`, `Yi`, `o`) before testing initial `z` and allows `zv` clusters.
  - Fixed primitive Liṭ madhyama eka (`sizvediTa`) and all Yaṅ/Yaṅluk stems.
  - Unlocked `01.0845 zvida~`, `01.1133 zvida~`, and `01.0496 sfB (zfBu~)` to 100.0%.
- Panini 7.4.87 *cara-phaloś ca* & 7.4.88 *ut parasyātaḥ* & 8.2.77 *hali ca*:
  - In yaṅanta and yaṅluk, `Pal` and `car` take augment `nuṅ` in abhyāsa, and root vowel `a` becomes `u`.
  - Before consonant `ya`, `cur` is lengthened to `cUr` by 8.2.77 *hali ca* (`caMcUrya-`), whereas before vowel/iṭ affixes where `ya` is elided (`liw`, `luw`, `lfw`, `luN`, `lfN`, `ASIrliN`, and non-ya krdantas), `u` remains short (`caMcur-`, `paMPul-`).
  - Restricted check strictly to `clean == "car"` (preventing false matching on `carb`, `carv`, `carc`).
  - Unlocked `01.0594 Pala~`, `01.0608 Pala~`, and `01.0640 cara~` to 100.0%.
- Panini 6.1.2 *ajāder dvitīyasya*:
  - For vowel-initial root `aw`, second syllable reduplication produces `awAwya-` in yaṅ and `awew`/`awAw` in yaṅluk. Allowed `sec` in `yang_krut` `ktvA` (`awAwya`). Unlocked `01.0332 awa~` to 100.0%.
- Panini 6.1.73 *che ca*:
  - In `_yan_stem`, `_yanlug_stem`, and `krdanta.py` `_yan_sec`: `_ybase` starting with `C` takes `tuk` (`c`) after an abhyāsa vowel that doesn't end in `M` (`cAcCazya-`). Placed after `yan_vowel` determination to prevent false insertion on nasal roots like `Cam`. Unlocked `01.1035 Caz` to 100.0%.
- Full Sweep Results: **1011/1156 100% passes** (raw 1011/1166, 10 skipped):
  - `01.0332 awa~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0496 sfB (zfBu~)`: 669 -> **895/895 (100.0%)** (+226 tokens) [NEW 100% PASS]
  - `01.0594 Pala~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0608 Pala~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0640 cara~`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0842 dyuta~`: 656 -> **883/883 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.0845 zvida~`: 656 -> **883/883 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.1014 SfDu~`: 878 -> **895/895 (100.0%)** (+17 tokens) [NEW 100% PASS]
  - `01.1035 Caz (Caza~)`: 668 -> **895/895 (100.0%)** (+227 tokens) [NEW 100% PASS]
  - `01.1133 zvida~`: 667 -> **895/895 (100.0%)** (+228 tokens) [NEW 100% PASS]
  - `01.1145 kfza~`: 886 -> **895/895 (100.0%)** (+9 tokens) [NEW 100% PASS]
  - 14 other roots improved (`01.0105`, `01.0504`, `01.0674`, `01.0857`-`01.0859`, `01.1131`, `01.1144`, etc.).
  - `yak` misses dropped to **0** (cleared!), joining `yangluk_krut` at **0**!
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All 36 Pilot and Milestone roots held strictly at 100.0%.

## Next
1. Target next closest failing roots from `tests/sweep_all.csv`:
   - `01.0674 sivi~` (gap=228): `sisinva` / `sisinvvatuH` in liṭ.
   - `01.1102 uN` (gap=239): `uAYcakre` am-anta liṭ / `avizwAm`.
   - `01.0504 GfRu~` (gap=256): `jarIGfRRyate` in yaṅ / `jarIGfRRitaH`.
   - `01.0648 kzvinkA~` / `kzvikA~` (gap=271): liṭ reduplication / sandhi.
   - `01.1131 zvanja~` (gap=336): nasal drop in kartari `svajate`.
   - `01.1144 danSa~` (gap=337): kartari nasal drop `daSati`.
2. Advance Gaṇa 01 beyond 1011/1156 towards 1020+/1156!
