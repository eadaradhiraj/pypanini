# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-17T08:56:00+05:30
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **1070/1156 100%** (92.6%, raw 1070/1166). Fails: 86 scored (96 with 10 skipped). Net matched tokens improved across 19 roots (0 worsened).
New 100% passes (15 roots unlocked in milestone 1070):
- `01.0919 smf` (243 -> 892/892, 100.0%, +649)
- `01.0987 dvf` (414 -> 895/895, 100.0%, +481)
- `01.1045 Bf` (683 -> 895/895, 100.0%, +212)
- `01.1074 pA` (703 -> 895/895, 100.0%, +192)
- `01.1077 sTA` (683 -> 895/895, 100.0%, +212)
- `01.1079 dA` (642 -> 895/895, 100.0%, +253)
- `01.1080 hvf` (414 -> 895/895, 100.0%, +481)
- `01.1081 svf` (414 -> 895/895, 100.0%, +481)
- `01.1082 smf` (414 -> 892/892, 100.0%, +478)
- `01.1083 vf` (683 -> 895/895, 100.0%, +212)
- `01.1084 hvf` (414 -> 895/895, 100.0%, +481)
- `01.1089 Dvf` (414 -> 895/895, 100.0%, +481)
- `01.1103 kU` (653 -> 883/883, 100.0%, +230)
- `01.1115 Df` (674 -> 883/883, 100.0%, +209)
- `01.1165 Svi` (631 -> 895/895, 100.0%, +264)

## Rules (general, pure generative)
- Panini 7.4.29 *guṇo 'rti-saṁyogādyoḥ* & 7.4.28 *riṅ śayag-liṅkṣu*: In `ASIrliN` (parasmaipada) and `yak` passive, roots ending in `ṛ` that are *saṁyogādi* (e.g. `smf`, `hvf`, `svf`, `Dvf`, `dvf`) and root `ṛ` take GUṆA `ar` (`smaryAt`, `smaryamARaH`, `hvaryAt`, `hvaryamARaH`), whereas single-consonant onset roots take `riṅ` (`BriyAt`, `vriyAt`).
- Panini 7.1.102 *uda oṣṭhyapūrvāt*: In `san` (`_sannanta_stem` / `_sannanta_sec`), `ṛ/ṝ` roots preceded by an oṣṭhya (labial) consonant take `Ur` (not `Ir`), with abhyāsa vowel `u` (`susmUrz-`, `juhvUrz-`, `susvUrz-`, `dudvUrz-`, `duDvUrz-`).
- Panini 1.2.5 *asaṁyogāl liṭ kit*: After a conjunct root (*saṁyoga*), `liṭ` is NOT kit; guṇa `ar` + `iṭ` applies in ātmanepada/karmani and parasmaipada dual/plural (`sasmare`, `sasmarAte`, `sasmarTa`, `sasmariDve`, `sasmaruH`).
- Panini 7.4.30 *yaṅi ca* & 7.4.83 *dīrgho 'kiTaḥ*: *saṁyogādi* `ṛ`-roots take guṇa `ar` with dīrgha `A` in abhyāsa (`sAsmaryate`, `jAhvaryate`, `sAsvaryate`, `dAdvaryate`, `dADvaryate`).
- Panini 7.2.75 *kiraś ca pañcabhyaḥ*: `DfN` takes obligatory `iṭ` in `san`, yielding guṇa `diDariz-`.
- Panini 8.3.59 *ādeśapratyayayoḥ* & 8.4.41 *ṣṭunā ṣṭuḥ*: In `san`, root `sTA` undergoes ṣatva and ṣṭutva after *iṇ*-ending abhyāsa `ti`, producing `tizWAs-`.
- Panini 7.4.54 *sani mīmāghūrabhalaBacakpatapadāṁ ca*: `ghu` roots (`dA`, `DA`, `deN`, `DeN`) take `i` for vowel without `iṭ`, yielding `dits-` and `Dits-`.
- Panini 6.4.66 *ghu-mā-sthā-gā-pā-jahāti-sāṁ hali*: `ghu` roots and `pA` take `A -> I` before halādi kit/ṅit suffixes: `dIyamAna-`, `pIyamAna-`, and in `yaṅ` `dedIya-` (7.4.82 *guṇo yaṅ-lukoḥ*).
- Panini 7.3.37 *śā-chā-sā-hvā-vyā-veñ-pā-damāṁ yuk*: `pA` (pāne) takes augment `yuk` (y) instead of `puk` before `ṇi`, yielding `pAyay-`.
- Panini 7.4.63 *na kavater yaṅi*: Cutva is prohibited in `yaṅ` and `yaṅluk` for root `ku`/`kU`, retaining guttural `k` in abhyāsa (`kokUyate`, `kokuTa`).
- Panini 6.1.15 *vaci-svapi-yajādīnāṁ kiti*: Root `Svi` (*wuoSvi*) takes samprasāraṇa in kit/ṅit environments: `SUyAt` in `ASIrliN`, `SUyamAna` in `yak` (7.4.25), and `praSUya` in `lyap`.
- Panini 1.2.18 *na ktvā seṭ*: `Svi` takes seṭ guṇa `SvayitvA` before `ktvā`.
- Panini 7.4.56 *sa ni pāt*: `Svi` in `san` yields `SiSvayiz-`.
- Panini 6.4.92 *mitāṁ hrasvaḥ*: For Ghaṭādi mit roots ending in `ṛ` (`01.0919 smf ADyAne`), vṛddhi `ār` is replaced by hrasva/guṇa `ar` before `ṇi`, yielding `smarayati` / `smaray-`.

## Fails (capped miss entries — lists capped per dhatu, fid-diff is truth)
| anta | n | example |
|---|---|---|
| krut | 578 | 01.0105 krut/tavya/M:svazkitavyaH |
| ting | 415 | 01.0105 ting/lw/prathama/eka:svazkate |
| san_krut | 11 | 01.0648 san_krut/kta/M:cikzIvizitaH |
| nich_krut | 8 | 01.0920 nich_krut/Satf/M:dArayan |
| nich | 5 | 01.0920 nich/lw/prathama/eka:dFayati |
| yak | 5 | 01.0921 yak/liw/prathama/eka:nanFe |
| san | 5 | 01.1123 san/lw/prathama/eka:RiRqizati |
| yang_krut | 5 | 01.1124 yang_krut/kta/M:tetrIyitaH |
| SKIPPED:ganasutra | 10 | 01.0933 SKIPPED:ganasutra |
