# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-17T09:55:00+05:30
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **1095/1156 100%** (94.7%, raw 1095/1166). Fails: 61 scored (71 with 10 skipped). Net matched tokens improved across 32 roots (0 worsened).
New 100% passes (25 roots unlocked in milestone 1095):
- `01.1051 glE` (326 -> 895/895, 100.0%, +569)
- `01.1052 mlE` (326 -> 895/895, 100.0%, +569)
- `01.1053 dyE` (326 -> 895/895, 100.0%, +569)
- `01.1054 drE` (326 -> 895/895, 100.0%, +569)
- `01.1055 DrE` (326 -> 895/895, 100.0%, +569)
- `01.1056 DyE` (326 -> 895/895, 100.0%, +569)
- `01.1057 rE` (326 -> 895/895, 100.0%, +569)
- `01.1058 styE` (326 -> 895/895, 100.0%, +569)
- `01.1059 zwyE` (114 -> 895/895, 100.0%, +781)
- `01.1060 KE` (326 -> 895/895, 100.0%, +569)
- `01.1061 kzE` (326 -> 895/895, 100.0%, +569)
- `01.1062 jE` (326 -> 895/895, 100.0%, +569)
- `01.1063 zE` (297 -> 895/895, 100.0%, +598)
- `01.1064 kE` (326 -> 895/895, 100.0%, +569)
- `01.1065 gE` (551 -> 895/895, 100.0%, +344)
- `01.1066 SE` (509 -> 895/895, 100.0%, +386)
- `01.1067 SrE` (326 -> 895/895, 100.0%, +569)
- `01.1068 srE` (326 -> 895/895, 100.0%, +569)
- `01.1069 pE` (509 -> 895/895, 100.0%, +386)
- `01.1070 vE` (326 -> 895/895, 100.0%, +569)
- `01.1071 zwE` (114 -> 895/895, 100.0%, +781)
- `01.1072 zRE` (18 -> 895/895, 100.0%, +877)
- `01.1118 SyEN` (328 -> 883/883, 100.0%, +555)
- `01.1119 pyEN` (328 -> 883/883, 100.0%, +555)
- `01.1120 trEN` (328 -> 883/883, 100.0%, +555)

## Rules (general, pure generative)
- Panini 6.1.45 *ādeca upadeśe 'śiti*: Upadeśa roots ending in *ec* (`E`, `e`, `o`) substitute *āt* (`A`) before *aśit* affixes in tiṅanta and kṛdanta (yielding `glA-`, `mlA-`, `trA-`, `drA-`, `PrA-`, `klA-`, `styA-`, `KA-`, `kzA-`, `jA-`, `sA-`, `kA-`, `gA-`, `SA-`, `SrA-`, `srA-`, `pA-`, `vA-`, `stA-`, `snA-`).
- Panini 7.3.34 *ātaḥ* & 7.3.36 *arti-hrī-vlī-rī-knūyī-kṣmāyyātāṁ puk ṇau*: `āt` bases take `au` in Liṭ parasmaipada singular (`jaglO`, `mamlO`), and `puk` augment before `ṇi` (`glApay-`, `mlApay-`).
- Panini 7.3.37 *śā-chā-sā-hvā-vyā-veñ-pā-damāṁ yuk*: Roots `śā`, `sā` (from `ṣai`), `pā` (from `pai`), and `śo` take `yuk` (`y`) before `ṇi` (`sAyay-`, `pAyay-`, `SAyay-`).
- Panini 6.4.64 *āto lopa iṭi ca*: `āt` bases lose final `ā` before `iṭ` in kṛdanta yanlukanta (`jAglitavya-`, `jAglitum-`, `jAglit-`, `jAglita-`).
- Panini 6.4.65 *īd yati*: `āt` roots replace `ā` with `ī` -> `e` before `yat`, forming `gleya-`, `mleya-`, `geya-`, `peya-`.
- Panini 7.4.61 *śarpūrvāḥ khayaḥ*: In reduplication of s/ṣ-initial clusters before stops (*khay* = `k, kh, c, ch, ṭ, ṭh, t, th, p, ph`), the second consonant is retained (`st- -> ta-`, `sk- -> ka-`, `sp- -> pa-`), but before nasals/semivowels (not in *khay*), `s/ṣ` is retained (`snE -> sAsn-`, `sAsnA-`).
- Panini 8.2.43 *kṣāmo maḥ*: Root `kṣai` (`01.1061 kzE`) forms kta `kzAma-` and ktavatu `kzAmavAn-` with `m` replacement.
- Panini 8.2.42 *saṁyogāder āto dhātor yaṇvataḥ*: `SrA` (`01.1067 SrE`) forms kta `SrARa-` and ktavatu `SrARavAn-` with `ṇa` replacement.
- Panini 8.3.59 *ādeśapratyayayoḥ* & 8.4.40 *ṣṭunā ṣṭuḥ*: Retroflexion and ṣṭutva in sannanta: `zwyE -> tizwyAs-`, `zwE -> tizwAs-`, `zE -> sizAs-`, `zRE -> sizRAs-`; dantya preserved in `styE -> tistyAs-` (*"styāyaty ekasya so na ṣaḥ"*) and `srE -> sisrAs-` (blocked by `r`).

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 392 | 01.0105 krut/tavya/M:svazkitavyaH |
| ting | 285 | 01.0105 ting/lw/prathama/eka:svazkate |
| san_krut | 12 | 01.0648 san_krut/kta/M:cikzIvizitaH |
| nich_krut | 11 | 01.0920 nich_krut/Satf/M:dArayan |
| yak | 10 | 01.0921 yak/liw/prathama/eka:nanFe |
| SKIPPED:ganasutra | 10 | 01.0933 SKIPPED:ganasutra |
| nich | 5 | 01.0920 nich/lw/prathama/eka:dArayati |
| san | 5 | 01.1123 san/lw/prathama/eka:qiqayzati |
| yang_krut | 5 | 01.1124 yang_krut/kta/M:tetrIyitaH |
