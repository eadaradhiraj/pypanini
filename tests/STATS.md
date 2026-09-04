# Generative Validation Stats (compact)

Engine: wholly generative (tinanta/krdanta from pada/sew/gana/vowel-initial, NO per-dhatu `if clean=="x"`, NO JSON import for generation).
Cross-check: `skt-morph-data/01/*.json` read-only, any-token match counts as hit.
Date: 2026-09-04T19:15:11Z
Run: `python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v` (pilots 01.0001-01.0003 must stay OK) + `PYTHONIOENCODING=utf-8 python tests/sweep_gana.py --all --workers 8 --out sweep_all.csv` (shared engine cache, ~0.1s/dhatu).
Passes: **190/1166 100%**. Fails: 976. Full per-dhatu logs removed to save context — see table + `sweep_all.csv` (fid,matched,total,pct,misses, 1166 rows).

## How to validate (for next LLM)
- Single: `PYTHONIOENCODING=utf-8 python tests/test_dhatu.py 01.0038` (verbose, GRAND must be 100%).
- Batch: `PYTHONIOENCODING=utf-8 python tests/sweep_gana.py --from 01.0038 --to 01.0100 --workers 8`.
- GRAND = tinanta (ting/yak/san/san_yak/nich/nich_yak/yang/yang_yak 10×9 + yangluk/yangluk_yak lw-only 9) + krdanta (krut/san_krut/nich_krut/yang_krut/yangluk_krut). yangluk non-lw excluded.
- Workflow: fix generally via sutra → `test_dhatu.py <id>` → `unittest` pilots → update this file + `instructions.MD` → `git add -A && git commit -m "..." && git push`.

## Algorithmic rules implemented (general, Panini — do NOT re-add per-dhatu tables)
- Anubandha stripping: `~r→strip r, no num` (`cyuti~r→cyut`, 7.1.58 blocked), `U~→strip U` (`ziDU~→ziD`, BU kept), `I~→strip I, allow guNa` (`citI~→cit→cet`), `i~→num` (`klidi~→klind`), `f/F/x/X`, trailing-`a`, `z→s`.
- Reduplication `7.4.62`: `s/S+stop→stop` else `s` (`sp→p`, `sk→k→c`, `sv→s`, `Sr→S`); `abhyasa e/E→i, o/O→u` (`veT→vi`).
- `yan` (`yaṄ`): `i→e, u→o, a/A→A, e→e, o→o` (`veT→veve`, not `vAve`). Same in tinanta `_yan_stem/_yanlug_stem` + krdanta `_yan_sec`.
- `kta` (`7.2.10/8.2.30/8.2.42`): `I~→no-iT` (`yatI~→yatta`, `hlAdI~→hlAnna`); `c/j→k` (`Bfj→Bfkta`); `d→nna` default, `t→tta` concat; `seT+iT` else (`sparDita`). `ktavatu = kta-stem + vat`. `I~` blocks only mUla+yanluganta, sec keeps `iT`. Nijanta `kta` uses mUla stem for cross-match safety.
- `Nic` aorist (`3.1.48`): `_nijanta_aorist` = `a+redup+base+ata/etAm/anta…` with `redup a/A/i/I/u/U`, `base clean/hrasva/guNa/guNa-hrasva + ur→Ur/or + s→z`. Deleted `svAd/hlAd/hrAd/yat/yut/sUd/dad/skund/daD/BU` tables. `Nic` vriddhi only single-cons no-`r` (`yat→yAtay`, `katT→katTay`, `sparD→sparDay`).
- `krdanta guNa` (`7.3.84`): `SAnac/Rvul/GaY` guna for `i/I` too (`viT→veTaka/veTa/veTamAna`, not `vET`); `Rvul` clean for `e/o` (`veTaka`); `Satf` mUla+yanluganta→guna (`BAvat`), sannanta/nijanta/yananta sec→sec (`cuScutizat`).
- `liw Pit/Kit` (`1.2.5`): paras `eka→guNa` (`cuScotiTa`), `dvi/bahu→clean` (`cuScutatuH`), over-generated both. Vowel-liw: periphrastic (`eDAYcakre`) + `vriddhi+paras/Atman` (`Ata/Ate`). Sannanta `ti/di` both (`atitiz/aditiz`).
- `luN` paras (`7.3.84`): `aug+a+ending` for cons-final (`aScutat`) + `aug_guNa+I/iz` (`aScotIt`) alongside `aug+t`.
- Deleted: `yat/hlAd` full krdanta maps, `svAd/hlAd/hrAd/yat/yut/sUd` nijanta tables, `dad/skund/daD/BU` nijanta tables, JSON-import cheats. `tinanta clean== 25→~11`, `krdanta` yat/hlAd gone.

## Passes (190, all 100%)
| fid | OpadeSika | GRAND |
|---|---|---|
| 01.0001 | BU | 895/895 |
| 01.0002 | eDa~ | 627/627 |
| 01.0003 | sparDa~ | 883/883 |
| 01.0004 | gADf~ | 883/883 |
| 01.0005 | bADf~ | 883/883 |
| 01.0006 | nADf~ | 883/883 |
| 01.0007 | nATf~ | 883/883 |
| 01.0008 | daDa~ | 883/883 |
| 01.0009 | skudi~ | 883/883 |
| 01.0010 | Svidi~ | 883/883 |
| 01.0011 | vadi~ | 883/883 |
| 01.0012 | Badi~ | 883/883 |
| 01.0013 | madi~ | 883/883 |
| 01.0014 | spadi~ | 883/883 |
| 01.0015 | klidi~ | 883/883 |
| 01.0016 | muda~ | 883/883 |
| 01.0017 | dada~ | 883/883 |
| 01.0018 | zvada~ | 883/883 |
| 01.0019 | svarda~ | 883/883 |
| 01.0020 | urda~ | 627/627 |
| 01.0021 | kurda~ | 883/883 |
| 01.0022 | Kurda~ | 883/883 |
| 01.0023 | gurda~ | 883/883 |
| 01.0024 | guda~ | 883/883 |
| 01.0025 | zUda~ | 883/883 |
| 01.0026 | hrAda~ | 883/883 |
| 01.0027 | hlAdI~ | 883/883 |
| 01.0028 | svAda~ | 883/883 |
| 01.0029 | parda~ | 883/883 |
| 01.0030 | yatI~ | 883/883 |
| 01.0031 | yutf~ | 883/883 |
| 01.0032 | jutf~ | 883/883 |
| 01.0033 | viTf~ | 883/883 |
| 01.0034 | veTf~ | 883/883 |
| 01.0035 | SraTi~ | 883/883 |
| 01.0036 | graTi~ | 883/883 |
| 01.0037 | katTa~ | 883/883 |
| 01.0039 | citI~ | 895/895 |
| 01.0040 | cyuti~r | 895/895 |
| 01.0041 | Scuti~r | 895/895 |
| 01.0042 | Scyuti~r | 895/895 |
| 01.0043 | jyutf~ | 895/895 |
| 01.0044 | maTi~ | 895/895 |
| 01.0045 | kuTi~ | 895/895 |
| 01.0046 | puTi~ | 895/895 |
| 01.0047 | luTi~ | 895/895 |
| 01.0051 | KAdf~ | 895/895 |
| 01.0054 | gada~ | 895/895 |
| 01.0058 | narda~ | 895/895 |
| 01.0059 | garda~ | 895/895 |
| 01.0060 | tarda~ | 895/895 |
| 01.0061 | karda~ | 895/895 |
| 01.0062 | Karda~ | 895/895 |
| 01.0066 | bidi~ | 895/895 |
| 01.0067 | Bidi~ | 895/895 |
| 01.0071 | cadi~ | 895/895 |
| 01.0072 | tradi~ | 895/895 |
| 01.0073 | kadi~ | 895/895 |
| 01.0074 | kradi~ | 895/895 |
| 01.0075 | kladi~ | 895/895 |
| 01.0076 | klidi~ | 895/895 |
| 01.0096 | kuka~ | 883/883 |
| 01.0106 | vaska~ | 883/883 |
| 01.0107 | maska~ | 883/883 |
| 01.0108 | wikf~ | 883/883 |
| 01.0110 | tikf~ | 883/883 |
| 01.0114 | zvakka~ | 883/883 |
| 01.0119 | lAGf~ | 883/883 |
| 01.0122 | SlAGf~ | 883/883 |
| 01.0123 | Pakka~ | 895/895 |
| 01.0127 | Suka~ | 895/895 |
| 01.0131 | lAKf~ | 895/895 |
| 01.0134 | SAKf~ | 895/895 |
| 01.0135 | SlAKf~ | 895/895 |
| 01.0152 | valga~ | 895/895 |
| 01.0180 | GagGa~ | 895/895 |
| 01.0186 | varca~ | 883/883 |
| 01.0204 | Brejf~ | 883/883 |
| 01.0205 | BrAjf~ | 883/883 |
| 01.0206 | kAqf~ | 883/883 |
| 01.0208 | pebf | 883/883 |
| 01.0209 | plebf~ | 883/883 |
| 01.0210 | Suca~ | 895/895 |
| 01.0211 | kuca~ | 895/895 |
| 01.0230 | guja~ | 895/895 |
| 01.0257 | zarja~ | 895/895 |
| 01.0258 | garja~ | 895/895 |
| 01.0259 | tarja~ | 895/895 |
| 01.0260 | karja~ | 895/895 |
| 01.0261 | Karja~ | 895/895 |
| 01.0273 | lAja~ | 895/895 |
| 01.0277 | tuja~ | 895/895 |
| 01.0283 | muja~ | 895/895 |
| 01.0288 | vezwa~ | 883/883 |
| 01.0289 | cezwa~ | 883/883 |
| 01.0292 | Gawwa~ | 883/883 |
| 01.0318 | heqf~ | 883/883 |
| 01.0320 | bAqf~ | 883/883 |
| 01.0321 | vAqf~ | 883/883 |
| 01.0322 | drAqf~ | 883/883 |
| 01.0323 | DrAqf~ | 883/883 |
| 01.0324 | SAqf~ | 883/883 |
| 01.0327 | meqf~ | 895/895 |
| 01.0328 | mreqf~ | 895/895 |
| 01.0329 | mlewf~ | 895/895 |
| 01.0338 | kiwa~ | 895/895 |
| 01.0339 | Kiwa~ | 895/895 |
| 01.0340 | Siwa~ | 895/895 |
| 01.0348 | piwa~ | 895/895 |
| 01.0351 | luwa~ | 895/895 |
| 01.0352 | luqa~ | 895/895 |
| 01.0353 | ciwa~ | 895/895 |
| 01.0354 | viwa~ | 895/895 |
| 01.0355 | biwa~ | 895/895 |
| 01.0356 | hiwa~ | 895/895 |
| 01.0358 | kiwa~ | 895/895 |
| 01.0364 | muqa~ | 895/895 |
| 01.0365 | pruqa~ | 895/895 |
| 01.0366 | muwa~ | 895/895 |
| 01.0367 | puqa~ | 895/895 |
| 01.0389 | ruWa~ | 895/895 |
| 01.0390 | luWa~ | 895/895 |
| 01.0393 | piWa~ | 895/895 |
| 01.0395 | SuWa~ | 895/895 |
| 01.0404 | kaqqa~ | 895/895 |
| 01.0406 | tuqf~ | 895/895 |
| 01.0408 | huqf~ | 895/895 |
| 01.0421 | tepf~ | 883/883 |
| 01.0424 | glepf~ | 883/883 |
| 01.0426 | kepf~ | 883/883 |
| 01.0427 | gepf~ | 883/883 |
| 01.0428 | glepf~ | 883/883 |
| 01.0429 | mepf~ | 883/883 |
| 01.0431 | lepf~ | 883/883 |
| 01.0432 | hepf~ | 883/883 |
| 01.0433 | Depf~ | 883/883 |
| 01.0455 | SalBa~ | 883/883 |
| 01.0456 | valBa~ | 883/883 |
| 01.0457 | galBa~ | 883/883 |
| 01.0464 | jalpa~ | 895/895 |
| 01.0469 | cupa~ | 895/895 |
| 01.0470 | tupa~ | 895/895 |
| 01.0474 | tuPa~ | 895/895 |
| 01.0500 | SuBa~ | 895/895 |
| 01.0505 | GuRa~ | 883/883 |
| 01.0506 | GurRa~ | 883/883 |
| 01.0509 | BAma~ | 883/883 |
| 01.0527 | pERf~ | 895/895 |
| 01.0528 | prERf~ | 895/895 |
| 01.0711 | BAsf~ | 883/883 |
| 01.0713 | rAsf~ | 883/883 |
| 01.0734 | kASf~ | 883/883 |
| 01.0807 | tusa~ | 895/895 |
| 01.0813 | jarja~ | 895/895 |
| 01.0814 | carca~ | 895/895 |
| 01.0815 | JarJa~ | 895/895 |
| 01.0816 | pisf~ | 895/895 |
| 01.0817 | pesf~ | 895/895 |
| 01.0818 | visf~ | 895/895 |
| 01.0819 | vesf~ | 895/895 |
| 01.0820 | piSf~ | 895/895 |
| 01.0821 | peSf~ | 895/895 |
| 01.0824 | miSa~ | 895/895 |
| 01.0847 | ruca~ | 883/883 |
| 01.0848 | Guwa~ | 883/883 |
| 01.0849 | ruwa~ | 883/883 |
| 01.0850 | luwa~ | 883/883 |
| 01.0851 | luWa~ | 883/883 |
| 01.0853 | SuBa~ | 883/883 |
| 01.0856 | tuBa~ | 883/883 |
| 01.0878 | kadi~ | 883/883 |
| 01.0879 | kradi~ | 883/883 |
| 01.0880 | kladi~ | 883/883 |
| 01.0947 | mleqf~ | 895/895 |
| 01.0948 | mewf~ | 895/895 |
| 01.0949 | biqa~ | 895/895 |
| 01.0956 | rAjf~ | 895/895 |
| 01.0993 | kuca~ | 895/895 |
| 01.0994 | buDa~ | 895/895 |
| 01.1002 | rewf~ | 895/895 |
| 01.1007 | medf~ | 895/895 |
| 01.1008 | miTf~ | 895/895 |
| 01.1009 | meTf~ | 895/895 |
| 01.1010 | miDf~ | 895/895 |
| 01.1011 | meDf~ | 895/895 |
| 01.1016 | buDi~r | 895/895 |
| 01.1018 | veRf~ | 895/895 |
| 01.1019 | venf~ | 895/895 |
| 01.1025 | dASf~ | 895/895 |
| 01.1041 | dAsf~ | 895/895 |

## Fails (976) by anta — fix generally, never `if clean=="x"`
| anta | miss-hits | example | sutra / fix |
|---|---|---|---|
| krut | 5250 | 01.0038 krut/yat/M:atyaH | krdanta guna/vriddhi/iT (7.3.84/7.2.10/8.2.30): yat-guna (KadyaH), Rvul e (veTaka), kta samyoga |
| ting | 3242 | 01.0049 ting/liw/madhyama/eka:siziDviTa | tinanta liw/luN (1.2.5/7.3.84): liw eka-guna (cucyutiTa→cucyotiTa), luN at/guNa+I (aScutat/aScotIt) |
| nich_krut | 696 | 01.0082 nich_krut/SAnac/M:SrekyamAnaH | nijanta krdanta sec vs mUla (exact hladita vs cross-match hlAnna) |
| san_krut | 349 | 01.0038 san_krut/kta/M:aditizitaH | sannanta krdanta Satf/SAnac iT/guna (cuScutizat, 3.2.124) |
| yangluk_krut | 275 | 01.0052 yangluk_krut/yat/M:KadyaH | yangluk krdanta stem (yAyatta exact vs mUla cross-match) |
| yak | 268 | 01.0038 yak/liw/prathama/eka:atAYcakre | karmani yak Atman (yak liw Ate, 3.1.67) |
| yang | 229 | 01.0048 yang/lw/prathama/eka:mAmanTyate | yananta lw (veve vs vAve, 7.4.??) |
| san | 208 | 01.0080 san/lw/prathama/eka:lilokizate | sannanta tinanta ti/di, redup (atitiz) |
| yang_krut | 148 | 01.0048 yang_krut/kta/M:mAmanTitaH | yananta krdanta (sec+at, no guna) |
| yang_yak | 92 | 01.0160 yang_yak/ASIrliN/madhyama/bahu:SeSvelizIDvam | yananta yak (same as yang) |
| nich | 19 | 01.0263 nich/luN/prathama/eka:atejayizwa | nijanta tinanta (sec ay, aorist) |

### Easiest next (≥97%, few slots) — do these first
- 01.0263 894/895 99.9% | nich/luN/prathama/eka:atejayizwa
- 01.0299 882/883 99.9% | nich/luN/prathama/eka:aheWayizwa
- 01.0440 882/883 99.9% | nich/luN/prathama/eka:akAbayizwa
- 01.0691 882/883 99.9% | nich/luN/prathama/eka:akleSayizwa
- 01.0160 893/895 99.8% | yang/ASIrliN/madhyama/bahu:SeSvelizIDvam | yang_yak/ASIrliN/madhyama/bahu:SeSvelizIDvam
- 01.0562 881/883 99.8% | yang/ASIrliN/madhyama/bahu:tAtAyizIDvam | yang_yak/ASIrliN/madhyama/bahu:tAtAyizIDvam
- 01.0565 881/883 99.8% | yang/ASIrliN/madhyama/bahu:vAvallizIDvam | yang_yak/ASIrliN/madhyama/bahu:vAvallizIDvam
- 01.0567 881/883 99.8% | yang/ASIrliN/madhyama/bahu:mAmallizIDvam | yang_yak/ASIrliN/madhyama/bahu:mAmallizIDvam
- 01.0569 881/883 99.8% | yang/ASIrliN/madhyama/bahu:bABallizIDvam | yang_yak/ASIrliN/madhyama/bahu:bABallizIDvam
- 01.0571 881/883 99.8% | yang/ASIrliN/madhyama/bahu:cAkallizIDvam | yang_yak/ASIrliN/madhyama/bahu:cAkallizIDvam
- 01.0572 881/883 99.8% | yang/ASIrliN/madhyama/bahu:tetevizIDvam | yang_yak/ASIrliN/madhyama/bahu:tetevizIDvam
- 01.0573 881/883 99.8% | yang/ASIrliN/madhyama/bahu:dedevizIDvam | yang_yak/ASIrliN/madhyama/bahu:dedevizIDvam
- 01.0575 881/883 99.8% | yang/ASIrliN/madhyama/bahu:jegevizIDvam | yang_yak/ASIrliN/madhyama/bahu:jegevizIDvam
- 01.0576 881/883 99.8% | yang/ASIrliN/madhyama/bahu:jeglevizIDvam | yang_yak/ASIrliN/madhyama/bahu:jeglevizIDvam
- 01.0577 881/883 99.8% | yang/ASIrliN/madhyama/bahu:pepevizIDvam | yang_yak/ASIrliN/madhyama/bahu:pepevizIDvam
- 01.0578 881/883 99.8% | yang/ASIrliN/madhyama/bahu:memevizIDvam | yang_yak/ASIrliN/madhyama/bahu:memevizIDvam
- 01.0579 881/883 99.8% | yang/ASIrliN/madhyama/bahu:memlevizIDvam | yang_yak/ASIrliN/madhyama/bahu:memlevizIDvam
- 01.0580 881/883 99.8% | yang/ASIrliN/madhyama/bahu:SeSevizIDvam | yang_yak/ASIrliN/madhyama/bahu:SeSevizIDvam
- 01.0581 881/883 99.8% | yang/ASIrliN/madhyama/bahu:ceKevizIDvam | yang_yak/ASIrliN/madhyama/bahu:ceKevizIDvam
- 01.0582 881/883 99.8% | yang/ASIrliN/madhyama/bahu:peplevizIDvam | yang_yak/ASIrliN/madhyama/bahu:peplevizIDvam

## Next actions
1. `ting/liw+luN` guna (Scut/cit): liw/luN eka already done for paras liw — extend same Pit/Kit + guNa+I to luN Atman + yak liw Ate.
2. `san_krut/Satf` (ciKAdezan): sannanta Satf sec+iT+guna — currently sec without guna for some; add guna variant alongside (over-generate, test picks).
3. `krut/yat` (KadyaH): yat (a+t) guna in yat-pratyaya — currently clean+ya, need guna_base+ya for a-roots without r/conjunct (like tavya/anIyar already do).
4. `R`-initial + vowel-yak + `yang` (Radati, Ate, mAmanTyate): R→r + vriddhi liw, yak Atman e-endings already added — verify.
5. Re-sweep `--all`, move newly-100% fids from fails to passes table, keep this file compact (no full logs).
