# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-17T09:55:00+05:30
Sweep: **1095/1156 100%** (94.7%, raw 1095/1166)

## Done
- Panini 6.1.45 *ādeca upadeśe 'śiti*:
  - Fully implemented across tiṅanta and kṛdanta engines using rigorous `is_adeca(c)` helper function: upadeśa roots ending in *ec* (`E`, `e`, `o`) substitute *āt* (`A`) before all *aśit* affixes (unlocked entire 22-root cluster `01.1051` through `01.1072` plus `01.1118` through `01.1120`).
- Panini 7.3.34 *ātaḥ* & 7.3.36 *arti-hrī-vlī-rī-knūyī-kṣmāyyātāṁ puk ṇau*:
  - `āt` bases take `au` in Liṭ parasmaipada singular (`jaglO`, `mamlO`, `tatrO`, etc.) and `puk` augment in causative (`glApay-`, `mlApay-`, etc.).
- Panini 7.3.37 *śā-chā-sā-hvā-vyā-veñ-pā-damāṁ yuk*:
  - Roots `śā`, `sā` (from `ṣai` 01.1063), `pā` (from `pai` 01.1069), and `śo` take augment `yuk` (`y`) before `ṇi` (`sAyay-`, `pAyay-`, `SAyay-`).
- Panini 6.4.64 *āto lopa iṭi ca*:
  - In `krdanta.py` for yaṅlukanta of `ā`-bases: `ā` is deleted before `iṭ`, yielding `_get_yanluk_a_base() + "ita"` (kta), `+ "it"` (ktavatu), `+ "itavya"` (tavya), `+ "i"` (tṛc), `+ "itum"` (tumun).
- Panini 6.4.65 *īd yati*:
  - In `krdanta.py` for `yat`: `āt` roots replace `ā` with `ī` -> `e` before `yat`, correctly generating `gleya-`, `mleya-`, `geya-`, `peya-`, `steya-`.
- Panini 7.4.61 *śarpūrvāḥ khayaḥ*:
  - Fixed reduplication for s/ṣ-initial conjuncts: roots with s/ṣ followed by a stop (*khay* = `k, kh, c, ch, ṭ, ṭh, t, th, p, ph`) retain the second consonant (`st- -> ta-`, `sk- -> ka-`, `sp- -> pa-`), but roots with s/ṣ followed by nasals/semivowels (not *khay*) retain `s/ṣ` (`snE -> sAsn-`, `sAsnA-` for `01.1072 zRE`).
- Panini 8.2.43 *kṣāmo maḥ*:
  - In `_kta_stem`: `clean in ("kzE", "kzA")` replaces `ta` with `ma`, yielding `kzAma-` (kta) and `kzAmavAn-` (ktavatu).
- Panini 8.2.42 *saṁyogāder āto dhātor yaṇvataḥ*:
  - `SrE` (`01.1067 SrE`) forms kta `SrARa-` and ktavatu `SrARavAn-` with `ṇa` replacement, and removes obsolete `SritvA` from `ktvā` to correctly generate `SrAtvA`.
- Panini 8.3.59 *in-koḥ* & 8.4.40 *ṣṭunā ṣṭuḥ*:
  - Sannanta retroflexion and ṣṭutva: `zwyE -> tizwyAs-`, `zwE -> tizwAs-`, `zE -> sizAs-`, `zRE -> sizRAs-`.
  - Dantya preserved in `styE -> tistyAs-` per *"śabdasaṅghātayor dhātvoḥ: styāyaty ekasya so na ṣaḥ"*.
  - Preserved `sr` without ṣatva (`sisrAs-` for 01.1068 `srE`) as `r` blocks retroflexion.
- Full Sweep Results: **1095/1156 100% passes** (raw 1095/1166, 10 skipped):
  - `01.1051 glE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1052 mlE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1053 dyE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1054 drE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1055 DrE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1056 DyE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1057 rE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1058 styE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1059 zwyE`: 114 -> **895/895 (100.0%)** (+781 tokens) [NEW 100% PASS]
  - `01.1060 KE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1061 kzE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1062 jE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1063 zE`: 297 -> **895/895 (100.0%)** (+598 tokens) [NEW 100% PASS]
  - `01.1064 kE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1065 gE`: 551 -> **895/895 (100.0%)** (+344 tokens) [NEW 100% PASS]
  - `01.1066 SE`: 509 -> **895/895 (100.0%)** (+386 tokens) [NEW 100% PASS]
  - `01.1067 SrE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1068 srE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1069 pE`: 509 -> **895/895 (100.0%)** (+386 tokens) [NEW 100% PASS]
  - `01.1070 vE`: 326 -> **895/895 (100.0%)** (+569 tokens) [NEW 100% PASS]
  - `01.1071 zwE`: 114 -> **895/895 (100.0%)** (+781 tokens) [NEW 100% PASS]
  - `01.1072 zRE`: 18 -> **895/895 (100.0%)** (+877 tokens) [NEW 100% PASS]
  - `01.1118 SyEN`: 328 -> **883/883 (100.0%)** (+555 tokens) [NEW 100% PASS]
  - `01.1119 pyEN`: 328 -> **883/883 (100.0%)** (+555 tokens) [NEW 100% PASS]
  - `01.1120 trEN`: 328 -> **883/883 (100.0%)** (+555 tokens) [NEW 100% PASS]
  - Net matched tokens improved across 32 roots (+13,763 tokens total).
  - **STRICTLY 0 worsened roots** (`worsened == 0`).
  - All pilot and past milestone roots held strictly at 100.0%.

## Next
1. Target remaining 61 failing roots:
   - `01.1161 veY`, `01.1162 vyeY`, `01.1163 hveY`: Semivowel + ec roots taking samprasāraṇa / special Liṭ.
   - `01.1116 meN`, `01.1117 deN`: ātmanepada ec roots in Liṭ and yak.
   - `01.1124 tF` (646/895, 72.2%): Panini 6.4.122 *tṛphalabhajatratraphāṁ cedyataḥ* (`ter-` in Liṭ) + 7.1.100 / 8.2.77 (`tIrtvA`, `pratIrya`).
   - `01.1123` - `01.1128` (Panini 3.1.5 *gup-tij-kidbhyaḥ san* and 3.1.6 *māna-badha-śān-dānbhyaḥ dīrghaś ca*).
   - `01.0920 dF` (487/895, 54.4%) & `01.0921 nF` (478/895, 53.4%): ṝ-ending roots in Liṭ and causative.
2. Advance Gaṇa 01 beyond Milestone 1095 towards Milestone 1110+!
