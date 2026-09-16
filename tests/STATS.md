# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-16T22:30:00+05:30
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **1055/1156 100%** (91.3%, raw 1055/1166). Fails: 101 scored (111 with 10 skipped). Net matched tokens improved across 49 roots (0 worsened).
New 100% passes (11 roots unlocked in milestone 1050):
- `01.0269 kzi` (760 -> 895/895, 100.0%, +135)
- `01.0642 ji` (358 -> 895/895, 100.0%, +537)
- `01.1046 ri` (360 -> 895/895, 100.0%, +535)
- `01.1047 knU` (360 -> 895/895, 100.0%, +535)
- `01.1085 df` (360 -> 895/895, 100.0%, +535)
- `01.1087 stf` (360 -> 895/895, 100.0%, +535)
- `01.1088 stF` (360 -> 895/895, 100.0%, +535)
- `01.1096 ji` (358 -> 895/895, 100.0%, +537)
- `01.1097 jri` (766 -> 895/895, 100.0%, +129)
- `01.1098 jf` (360 -> 895/895, 100.0%, +535)
- `01.1099 smi` (620 -> 883/883, 100.0%, +263)

## Rules (general, pure generative)
- Panini 7.3.57 *san-liṭor jeḥ*: In `san` and `liṭ`, root `ji` replaces its palatal affricate `j` with guttural `g` (`jigIz-`, and liṭ karmani reduplication `jigi-`).
- Panini 6.1.48 *krīñ-jināṁ ṇau* & 7.3.36 *arti-hrī-vlī-rī-knū-kṣmāyyātāṁ pug ṇau*: Root `ji` takes ātvam before `ṇi` followed by `puk` augment (`jApay-`), yielding correct causative stems across all kartari and karmani derivations.
- Panini 7.2.74 *smi-pūṅ-rañj-vyañcaḥ sani*: Root `smi` (`zmiN`) takes guṇa with obligatory `iṭ` before `san` (`sismayiz-`).
- Panini 7.1.100 *ṛta iddhoḥ* & 8.2.77 *hali ca*: In `_sannanta_stem` and `_sannanta_sec`, ṛ/ṝ-ending roots lengthen to `Ir` before `sa` (`jijIrz-`, `didIrz-`).
- Panini 7.4.30 *rīṅ ṛtaḥ*: In `_yan_stem` and `_yan_sec`, ṛ/ṝ-ending roots substitute `rīṅ` (`_ybase[:-1] + "rI"`), unlocking intensive forms (`jejrIya-`).
- Panini 7.4.28 *riṅ śayag-liṅkṣu*: Before `yak`, ṛ/ṝ-ending roots substitute `riṅ` (`clean[:-1] + "riy"`).
- Panini 7.2.35 *ṛddhanoḥ sye*: ṛ/ṝ-ending roots take obligatory `iṭ` in `sya` (`lfw`, `lfN`).
- Panini 6.1.77 *iko yaṇ aci* in Liṭ: In perfect tense before vowel endings, ṛ/ṝ-ending roots substitute `r` (e.g. `jajratuH`, `jajruH`, and ātmanepada `jajre`, `jajrAte`, `jajrire`).
- Panini 3.1.97 *ṛhalor ṇyat* & 7.2.115 *aco ñṇiti*: Roots ending in `ṛ`/`ṝ` take `ṇyat` with vṛddhi `ār` (`clean[:-1] + "Arya"` -> `kAryaH`, `jAryaH`, `sAryaH`, `dAryaH`).
- Panini 6.4.65 *īdyati* & 6.4.66 *e ca*: Roots ending in `e`/`ai` (ādeca) before `yat` substitute `e` (`clean[:-1] + "e" + "ya"` -> `geya`, `peya`, `kzeya`).
- Panini 3.3.56 *er ac*: Roots ending in short `i` take affix `ac` (with guṇa) instead of `ghañ` (`jayaH`, `kzayaH`, `cayaH`), whereas long `I` roots take `ghañ` with vṛddhi (`nAyaH`).

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 622 | 01.0105 krut/tavya/M:svazkitavyaH |
| ting | 465 | 01.0105 ting/lw/prathama/eka:svazkate |
| san_krut | 70 | 01.0648 san_krut/kta/M:cikzIvizitaH |
| san | 30 | 01.1045 san/lw/prathama/eka:biBIrzati |
| yang_krut | 9 | 01.1103 yang_krut/kta/M:cokUyitaH |
| nich_krut | 6 | 01.0920 nich_krut/Satf/M:dArayan |
| nich | 5 | 01.1074 nich/lw/prathama/eka:pAayati |
| yang | 5 | 01.1103 yang/lw/prathama/eka:cokUyate |
| SKIPPED:ganasutra | 10 | 01.0933 SKIPPED:ganasutra |
