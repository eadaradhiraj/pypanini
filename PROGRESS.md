# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-16T22:30:00+05:30
Sweep: **1055/1156 100%** (91.3%, raw 1055/1166)

## Done
- Panini 7.3.57 *san-liṭor jeḥ*:
  - In `san` and `liṭ`, root `ji` replaces `j` with kavarga `g`: `jigIz-` in `san`, and liṭ karmani reduplication `jigi-`.
- Panini 6.1.48 *krīñ-jināṁ ṇau* & 7.3.36 *arti-hrī-vlī-rī-knū-kṣmāyyātāṁ pug ṇau*:
  - Root `ji` takes ātvam before `ṇi` followed by `puk` augment (`jApay-`), generating correct causative forms across kartari and karmani.
- Panini 7.2.74 *smi-pūṅ-rañj-vyañcaḥ sani*:
  - Root `smi` (`zmiN`) takes guṇa with obligatory `iṭ` before `san` (`sismayiz-`).
- Panini 7.1.100 *ṛta iddhoḥ* & 8.2.77 *hali ca*:
  - In `_sannanta_stem` and `_sannanta_sec`, ṛ/ṝ-ending roots lengthen to `Ir` before `sa` (`jijIrz-`, `didIrz-`).
- Panini 7.4.30 *rīṅ ṛtaḥ*:
  - In `_yan_stem` and `_yan_sec`, ṛ/ṝ-ending roots substitute `rīṅ` (`_ybase[:-1] + "rI"`), generating intensive stems (`jejrIya-`).
- Panini 7.4.28 *riṅ śayag-liṅkṣu*:
  - Before `yak`, ṛ/ṝ-ending roots substitute `riṅ` (`clean[:-1] + "riy"`).
- Panini 7.2.35 *ṛddhanoḥ sye*:
  - ṛ/ṝ-ending roots take obligatory `iṭ` in `sya` (`lfw`, `lfN`).
- Panini 6.1.77 *iko yaṇ aci* in Liṭ:
  - In perfect tense before vowel endings, ṛ/ṝ-ending roots substitute `r` (e.g. `jajratuH`, `jajruH`, and ātmanepada `jajre`, `jajrAte`, `jajrire`).
- Panini 3.1.97 *ṛhalor ṇyat* & 7.2.115 *aco ñṇiti*:
  - Roots ending in `ṛ`/`ṝ` take `ṇyat` with vṛddhi `ār` (`clean[:-1] + "Arya"` -> `kAryaH`, `jAryaH`, `sAryaH`, `dAryaH`).
- Panini 6.4.65 *īdyati* & 6.4.66 *e ca*:
  - Roots ending in `e`/`ai` (ādeca) before `yat` substitute `e` (`clean[:-1] + "e" + "ya"` -> `geya`, `peya`, `kzeya`).
- Panini 3.3.56 *er ac*:
  - Roots ending in short `i` take affix `ac` (with guṇa) instead of `ghañ` (`jayaH`, `kzayaH`, `cayaH`), whereas long `I` roots take `ghañ` with vṛddhi (`nAyaH`).
- Fixed `is_genuine_vowel_root` definition in `tinanta.py` and `krdanta.py`:
  - Properly recognizes monosyllabic vowel roots without preceding vowels (`ji`, `kzi`, `jri`, `smi`, etc.), ensuring yaṅanta keep-y-in-yaṅ behavior is correctly activated.
- Full Sweep Results: **1055/1156 100% passes** (raw 1055/1166, 10 skipped):
  - `01.0269 kzi`: 760 -> **895/895 (100.0%)** (+135 tokens) [NEW 100% PASS]
  - `01.0642 ji`: 358 -> **895/895 (100.0%)** (+537 tokens) [NEW 100% PASS]
  - `01.1046 ri`: 360 -> **895/895 (100.0%)** (+535 tokens) [NEW 100% PASS]
  - `01.1047 knU`: 360 -> **895/895 (100.0%)** (+535 tokens) [NEW 100% PASS]
  - `01.1085 df`: 360 -> **895/895 (100.0%)** (+535 tokens) [NEW 100% PASS]
  - `01.1087 stf`: 360 -> **895/895 (100.0%)** (+535 tokens) [NEW 100% PASS]
  - `01.1088 stF`: 360 -> **895/895 (100.0%)** (+535 tokens) [NEW 100% PASS]
  - `01.1096 ji`: 358 -> **895/895 (100.0%)** (+537 tokens) [NEW 100% PASS]
  - `01.1097 jri`: 766 -> **895/895 (100.0%)** (+129 tokens) [NEW 100% PASS]
  - `01.1098 jf`: 360 -> **895/895 (100.0%)** (+535 tokens) [NEW 100% PASS]
  - `01.1099 smi`: 620 -> **883/883 (100.0%)** (+263 tokens) [NEW 100% PASS]
  - Net matched tokens improved across 49 roots.
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All pilot and milestone roots held strictly at 100.0%.

## Next
1. Target remaining failing roots:
   - `01.1074 pA` (703/895, 78.5%): causative / ṇijanta forms.
   - `01.1077 sTA` (683/895, 76.3%): sannanta / ṇijanta forms.
   - `01.1079 dA` (642/895, 71.7%): sannanta forms.
   - `01.1083 vF` (683/895, 76.3%): sannanta forms.
   - `01.1115 DmA` (674/883, 76.3%): sannanta forms.
   - `01.1123 gup/tij/kit` (guptijkidbhyaḥ san 3.1.5): desiderative roots.
2. Advance Gaṇa 01 beyond 1055/1156 towards 1070+/1156!
