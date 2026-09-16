# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-16T18:00:00+05:30
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **1044/1156 100%** (90.3%, raw 1044/1166). Fails: 112 scored (122 with 10 skipped). Net matched tokens improved across 24 roots (0 worsened).
New 100% passes (24 roots unlocked across milestones 1030 and 1040):
- Milestone 1030 (17 roots): `01.0860 BranS` (799 -> 883/883, 100.0%, +84), `01.0596 SmIl` (434 -> 895/895, 100.0%, +461), `01.0597 smIl` (434 -> 895/895, 100.0%, +461), `01.1100 gu` (416 -> 883/883, 100.0%, +467), `01.1101 gA` (796 -> 883/883, 100.0%, +87), `01.1102 u` (388 -> 627/627, 100.0%, +239), `01.1104 Ku` (416 -> 883/883, 100.0%, +467), `01.1105 gu` (416 -> 883/883, 100.0%, +467), `01.1106 Gu` (416 -> 883/883, 100.0%, +467), `01.1107 Nu` (416 -> 883/883, 100.0%, +467), `01.1108 cyu` (416 -> 883/883, 100.0%, +467), `01.1109 jyu` (416 -> 883/883, 100.0%, +467), `01.1110 Cyu` (416 -> 883/883, 100.0%, +467), `01.1111 pru` (416 -> 883/883, 100.0%, +467), `01.1112 plu` (416 -> 883/883, 100.0%, +467), `01.1113 klu` (416 -> 883/883, 100.0%, +467), `01.1114 ru` (416 -> 883/883, 100.0%, +467).
- Milestone 1040 (7 roots): `01.1044 Sri` (876 -> 895/895, 100.0%, +19), `01.1090 sru` (866 -> 895/895, 100.0%, +29), `01.1091 su` (883 -> 895/895, 100.0%, +12), `01.1092 Sru` (835 -> 892/892, 100.0%, +57), `01.1093 Dru` (883 -> 895/895, 100.0%, +12), `01.1094 du` (883 -> 895/895, 100.0%, +12), `01.1095 dru` (866 -> 895/895, 100.0%, +29).
Adjacent improvements: `01.1099 smi` (389 -> 620/883, 70.2%, +231), `01.0269` (+12), `01.1097` (+12), `01.0642` (+12), `01.0919` (+17), `01.1045` (+9), `01.1046` (+9), `01.1047` (+9), `01.1082` (+9), `01.1083` (+12), `01.1085` (+12), `01.1087` (+12), `01.1088` (+12), `01.1096` (+12), `01.1098` (+12).

## Rules (general, pure generative)
- Panini 6.4.25 *akṛtsārvadhātukayor dīrghaḥ* & 7.4.28 *riṅ śayag-liṅkṣu*: In Āśīrliṅ parasmaipada (`yAsuw`) and passive Sānac (`yak` `ya`), ajanta stems take dīrgha before non-kṛt, non-sārvadhātuka y-initial affixes: `u` -> `U` (`sUyAt`, `DrUyAt`, `dUyAt`, `srUyAt`, `drUyAt`, `SrUyAt`, `sUyamAna`, `DrUyamARa`, `drUyamARa`), `i` -> `I` (`jIyAt`, `SrIyAt`, `jrIyAt`), and `ṛ`/`ṝ` stems take `riṅ` (`riyAt`, `kriyamARa`).
- Panini 7.2.13 *kṛ-sṛ-bhṛ-vṛ-stu-dru-sru-śruvo liṭi* & 6.4.77 *aci śnu-dhātu-bhruvāṁ yvo riyaṅ-uvaṅau*: Roots `kf`, `sf`, `Bf`, `vf`, `stu`, `dru`, `sru`, `Sru` are strictly an-iṭ in Liṭ. In Parasmaipada: `thal` takes guṇa without iṭ (`susroTa`, `dudroTa`, `SuSroTa`), uttama dvi/bahu take unaugmented `va`/`ma` (`susruva`, `susruma`, `dudruva`, `dudruma`, `SuSruva`, `SuSruma`), and vowel-initial kit endings take `uvaṅ` (`susruvatuH`, `susruvuH`, `susruvaTuH`, `susruva`, `dudruvatuH`...). In Ātmanepada / Karmani Liṭ: endings take an-iṭ forms without `i` (`SuSruze`, `SuSruQve`, `SuSruvahe`, `SuSrumahe`).
- Panini 8.3.59 & Phonotactics (*sr* Cluster Satva Prohibition): Retroflex `ṣ` (`z`) never precedes `r` in Sanskrit phonology (`ṣr` is phonotactically prohibited). Preserved dental `s` in `sr` clusters during reduplication (`susru-`, not `suzru-`).
- Panini 3.1.74 *śruvaḥ śṛ ca*: After root `śru`, the vikaraṇa `śnu` replaces `śap` and `śru` is replaced by `śṛ` in sārvadhātuka lakāras (`lw`, `low`, `laN`, `viDiliN`), generating `SfRoti`, `SfRutaH`, `SfRvanti`, `aSfRot`, `SfRotu`, `SfRuyAt`.
- Panini 3.1.48 *ṇiś-śri-dru-sru-śrubhyaḥ kartari caṅ*: In Luṅ, roots `śri`, `dru`, `sru`, and `śru` take the reduplicated `caṅ` aorist with 6.4.77 `uvaṅ`/`riyaṅ` glide insertion before vowel affixes (`asusruvat`, `asusruvatAm`, `asusruvan`, `adudruvat`, `adudruvatAm`, `adudruvan`, `aSuSruvat`, `aSiSriyat`).
- Panini 7.4.82 *guṇo yaṅ-lukoḥ*, 7.1.78 *nābhyastācchaturguṇakṛtamanikartuśca*, 6.4.77 *uvaṅ*, & 6.4.82 *er an-ekāco 'saṁyogapūrvasya*: In Yaṅluk Śatṛ for non-idit ajanta roots: abhyāsa takes guṇa (`o` for `u`/`U`, `e` for `i`/`I`), endings take non-num forms (`at`), and vowel roots take `uvaṅ` (`uv`: `boBuvat`, `SoSruvat`, `dodruvat`, `sosruvat`, `sozuvat`) or `yaṇ`/`riyaṅ` (`y` for asaṁyogapūrva multi-syllabic stems: `nenyat`; `iy` for saṁyogapūrva stems: `SeSriyat`).
- Panini 6.4.24 *aniditāṁ hala upadhāyāḥ kṅiti*: In `_yan_stem` and `_yan_sec`, penultimate nasals elide before any hal for non-idit roots (`BranS` -> `bABraSya-`).
- Panini 7.4.61 *śarpūrvāḥ khayaḥ* & 7.4.60 *halādiḥ śeṣaḥ*: Defined `SLP1_KHAY = set(list("kKcCwWtTpP"))`. Initial conjuncts starting with śar (`S, z, s`) retain the following consonant in reduplication if and only if it belongs to khay (`SLP1_KHAY`). Sonorants and nasals (`m, n, y, r, l, v`) do not remain; the initial sibilant remains (`SmIl` -> `SeSmIl-`, `smIl` -> `sesmIl-`).
- Panini 6.4.16 *aj-jhan-gāṁ sani*: Ajanta roots take dīrgha before affix `san`: `u` -> `U` (`cyUza-`, `plUza-`), `i` -> `I`.
- Panini 6.1.73 *che ca*: Insert `tuk` (`c`) after vowel before `ch` in `_sannanta_stem` and `_sannanta_sec` (`Cyu` -> `cucCyUz-`).
- Panini 6.1.71 *hrasvasya piti kṛti tuk*: Short vowel roots taking `lyap` insert `tuk` (`t`) before `ya` (`pracyutya`).

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 679 | 01.0105 krut/SAnac/M:zvazkamARaH |
| ting | 515 | 01.0105 ting/lw/prathama/eka:svazkate |
| san_krut | 83 | 01.0003 san_krut/kta/M:cicyavizitaH |
| yang_krut | 18 | 01.0003 yang_krut/kta/M:cecyavitaH |
| yang | 15 | 01.0003 yang/lw/prathama/eka:cecyavate |
| san | 15 | 01.0003 san/lw/prathama/eka:cicyavizate |
| yak | 10 | 01.1096 yak/liw/prathama/eka:jijie |
| nich | 5 | 01.1074 nich/lw/prathama/eka:pApayati |
| nich_krut | 4 | 01.0105 nich_krut/kta/M:zvazkitaH |
| SKIPPED:ganasutra | 10 | 01.0933 SKIPPED:ganasutra |
| yangluk_krut | 0 | (cleared for ajanta!) |
