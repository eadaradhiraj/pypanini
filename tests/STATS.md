# Generative Validation Stats (compact)

Engine: wholly generative (tinanta/krdanta from pada/sew/gana/vowel-initial, NO per-dhatu `if clean=="x"`, NO JSON import for generation).
Cross-check: `skt-morph-data/01/*.json` read-only, any-token match counts as hit.
Date: 2026-09-04T19:29:49Z
Run: `python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v` (pilots 01.0001-01.0003 must stay OK) + `PYTHONIOENCODING=utf-8 python tests/sweep_gana.py --all --workers 8 --out tests/sweep_all.csv` (shared engine cache, ~0.1s/dhatu).
Passes: **247/1166 100%**. Fails: 919. Full per-dhatu logs removed to save context — see table + `tests/sweep_all.csv` (fid,matched,total,pct,misses, 1166 rows, query via `grep`, do not dump).

## How to validate (for next LLM)
- Single: `PYTHONIOENCODING=utf-8 python tests/test_dhatu.py 01.0038` (verbose, GRAND must be 100%).
- Batch: `PYTHONIOENCODING=utf-8 python tests/sweep_gana.py --from 01.0038 --to 01.0100 --workers 8`.
- GRAND = tinanta (ting/yak/san/san_yak/nich/nich_yak/yang/yang_yak 10x9 + yangluk/yangluk_yak lw-only 9) + krdanta (krut/san_krut/nich_krut/yang_krut/yangluk_krut). yangluk non-lw excluded.
- Workflow: fix generally via sutra -> `test_dhatu.py <id>` -> `unittest` pilots -> update this file + `git add -A && git commit -m "..." && git push`.

## Algorithmic rules implemented (general, Panini — do NOT re-add per-dhatu tables)
- Anubandha: `~r→strip r no-num` (7.1.58 blocked), `U~→strip U`, `I~→strip I allow-guNa`, `i~→num`, `f/F/x/X`, trailing-`a`, `z→s`.
- Redup `7.4.62`: `s/S+stop→stop` else `s` (`Sr→S`); `abhyasa e/E→i o/O→u`; `sibilant` handling in tinanta+krdanta.
- `yan`: `i→e u→o a/A→A e→e o→o` (`veT→veve`).
- `kta` (`7.2.10/8.2.30/8.2.42`): `I~→no-iT`, `c/j→k`, `d→nna/t→tta`, `seT+iT`; `ktavatu=stem+vat`; `I~` blocks mUla+yanluganta only; nijanta kta uses mUla for cross-match.
- `Nic` aorist (`3.1.48`): `a+redup+base+ata…`, `redup a/A/i/I/u/U`, `base clean/hrasva/guNa + ur→Ur/or + s→z + e→i/o→u samprasArana (tej→tij)`. Nic vriddhi single-cons no-r.
- `krdanta guNa` (`7.3.84`): `SAnac/Rvul/GaY` guna `i/I` too; `Rvul` clean `e/o`; `Satf` mUla+yanluganta→guna else sec.
- `liw Pit/Kit` (`1.2.5`): paras `eka→guNa` over-generated both; vowel-liw periphrastic + `vriddhi+paras/Atman`; sannanta `ti/di` both.
- `luN` paras: `aug+a+ending` cons-final + `aug_guNa+I/iz`; `ASIrliN` madhyama-bahu `IDvam+IQvam` both (D/Q).
- Deleted: yat/hlAd maps, svAd tables, dad/skund/daD/BU tables, JSON cheats.

## Passes (247, all 100%)
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
| 01.0160 | Svelf~ | 895/895 |
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
| 01.0263 | teja~ | 895/895 |
| 01.0273 | lAja~ | 895/895 |
| 01.0277 | tuja~ | 895/895 |
| 01.0283 | muja~ | 895/895 |
| 01.0288 | vezwa~ | 883/883 |
| 01.0289 | cezwa~ | 883/883 |
| 01.0292 | Gawwa~ | 883/883 |
| 01.0299 | heWa~ | 883/883 |
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
| 01.0562 | tAyf~ | 883/883 |
| 01.0565 | valla~ | 883/883 |
| 01.0567 | malla~ | 883/883 |
| 01.0569 | Balla~ | 883/883 |
| 01.0571 | kalla~ | 883/883 |
| 01.0572 | tevf~ | 883/883 |
| 01.0573 | devf~ | 883/883 |
| 01.0575 | gevf~ | 883/883 |
| 01.0576 | glevf~ | 883/883 |
| 01.0577 | pevf~ | 883/883 |
| 01.0578 | mevf~ | 883/883 |
| 01.0579 | mlevf~ | 883/883 |
| 01.0580 | Sevf~ | 883/883 |
| 01.0581 | Kevf~ | 883/883 |
| 01.0582 | plevf~ | 883/883 |
| 01.0583 | kevf~ | 883/883 |
| 01.0585 | mavya~ | 895/895 |
| 01.0612 | tila~ | 895/895 |
| 01.0614 | velf~ | 895/895 |
| 01.0615 | celf~ | 895/895 |
| 01.0616 | kelf~ | 895/895 |
| 01.0617 | Kelf~ | 895/895 |
| 01.0618 | kzvelf~ | 895/895 |
| 01.0619 | vella~ | 895/895 |
| 01.0620 | cella~ | 895/895 |
| 01.0621 | pelf~ | 895/895 |
| 01.0622 | Pelf~ | 895/895 |
| 01.0623 | Self~ | 895/895 |
| 01.0631 | Svalla~ | 895/895 |
| 01.0671 | pivi~ | 895/895 |
| 01.0672 | mivi~ | 895/895 |
| 01.0675 | hivi~ | 895/895 |
| 01.0676 | divi~ | 895/895 |
| 01.0678 | jivi~ | 895/895 |
| 01.0681 | Davi~ | 895/895 |
| 01.0691 | kleSa~ | 883/883 |
| 01.0711 | BAsf~ | 883/883 |
| 01.0713 | rAsf~ | 883/883 |
| 01.0724 | galha~ | 883/883 |
| 01.0726 | balha~ | 883/883 |
| 01.0728 | valha~ | 883/883 |
| 01.0729 | pliha~ | 883/883 |
| 01.0730 | vehf~ | 883/883 |
| 01.0731 | jehf~ | 883/883 |
| 01.0732 | bAhf~ | 883/883 |
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
| 01.0838 | tuhi~r | 895/895 |
| 01.0839 | duhi~r | 895/895 |
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
| 01.0916 | jvala~ | 895/895 |
| 01.0917 | hvala~ | 895/895 |
| 01.0918 | hmala~ | 895/895 |
| 01.0947 | mleqf~ | 895/895 |
| 01.0948 | mewf~ | 895/895 |
| 01.0949 | biqa~ | 895/895 |
| 01.0952 | vAhf~ | 883/883 |
| 01.0956 | rAjf~ | 895/895 |
| 01.0965 | jvala~ | 895/895 |
| 01.0975 | pula~ | 895/895 |
| 01.0976 | kula~ | 895/895 |
| 01.0978 | hula~ | 895/895 |
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
| 01.1042 | mAhf~ | 895/895 |

## Fails (919) by anta
| anta | miss-hits | example | sutra / fix |
|---|---|---|---|
| krut | 5253 | 01.0038 krut/yat/M:atyaH | krdanta guna/vriddhi/iT (7.3.84/7.2.10/8.2.30) |
| ting | 3242 | 01.0049 ting/liw/madhyama/eka:siziDiTa | tinanta liw/luN (1.2.5/7.3.84) |
| nich_krut | 741 | 01.0082 nich_krut/SAnac/M:SrekyamAnaH | nijanta sec vs mUla |
| san_krut | 349 | 01.0038 san_krut/kta/M:aditizitaH | sannanta Satf/SAnac (3.2.124) |
| yangluk_krut | 275 | 01.0052 yangluk_krut/yat/M:KadyaH | yangluk stem |
| yak | 268 | 01.0038 yak/liw/prathama/eka:atAYcakre | karmani yak Atman (3.1.67) |
| san | 208 | 01.0080 san/lw/prathama/eka:lilokizate | sannanta ti/di |
| yang_krut | 148 | 01.0048 yang_krut/kta/M:mAmanTitaH | yananta krdanta |
| yang | 137 | 01.0048 yang/lw/prathama/eka:mAmanTyate | yananta lw |
| nich | 16 | 01.0440 nich/luN/prathama/eka:akAbayizwa | nijanta tinanta |

### Easiest next (>=97%)
- 01.0440 882/883 99.9% | nich/luN/prathama/eka:akAbayizwa
- 01.1023 892/895 99.7% | yang_krut/yat/M:cAcAyyaH | yang_krut/yat/F:cAcAyyA | yang_krut/yat/N:cAcAyyam
- 01.0286 891/895 99.6% | krut/yat/M:vrajyaH | krut/yat/N:vrajyam | yangluk_krut/yat/M:vrajyaH | yangluk_krut/yat/N:vrajyam
- 01.0052 889/895 99.3% | krut/yat/M:KadyaH | krut/yat/F:KadyA | krut/yat/N:Kadyam | yangluk_krut/yat/M:KadyaH | yangluk_krut/yat/F:KadyA | yangluk_krut/yat/N:Kadyam
- 01.0095 877/883 99.3% | krut/yat/M:kakyaH | krut/yat/F:kakyA | krut/yat/N:kakyam | yangluk_krut/yat/M:kakyaH | yangluk_krut/yat/F:kakyA | yangluk_krut/yat/N:kakyam
- 01.0128 889/895 99.3% | krut/yat/M:kaKyaH | krut/yat/F:kaKyA | krut/yat/N:kaKyam | yangluk_krut/yat/M:kaKyaH | yangluk_krut/yat/F:kaKyA | yangluk_krut/yat/N:kaKyam
- 01.0138 889/895 99.3% | krut/yat/M:vaKyaH | krut/yat/F:vaKyA | krut/yat/N:vaKyam | yangluk_krut/yat/M:vaKyaH | yangluk_krut/yat/F:vaKyA | yangluk_krut/yat/N:vaKyam
- 01.0179 889/895 99.3% | krut/yat/M:GaGyaH | krut/yat/F:GaGyA | krut/yat/N:GaGyam | yangluk_krut/yat/M:GaGyaH | yangluk_krut/yat/F:GaGyA | yangluk_krut/yat/N:GaGyam
- 01.0190 877/883 99.3% | krut/yat/M:SvacyaH | krut/yat/F:SvacyA | krut/yat/N:Svacyam | yangluk_krut/yat/M:SvacyaH | yangluk_krut/yat/F:SvacyA | yangluk_krut/yat/N:Svacyam
- 01.0192 877/883 99.3% | krut/yat/M:kacyaH | krut/yat/F:kacyA | krut/yat/N:kacyam | yangluk_krut/yat/M:kacyaH | yangluk_krut/yat/F:kacyA | yangluk_krut/yat/N:kacyam
- 01.0245 889/895 99.3% | krut/yat/M:DrajyaH | krut/yat/F:DrajyA | krut/yat/N:Drajyam | yangluk_krut/yat/M:DrajyaH | yangluk_krut/yat/F:DrajyA | yangluk_krut/yat/N:Drajyam
- 01.0251 889/895 99.3% | krut/yat/M:DvajyaH | krut/yat/F:DvajyA | krut/yat/N:Dvajyam | yangluk_krut/yat/M:DvajyaH | yangluk_krut/yat/F:DvajyA | yangluk_krut/yat/N:Dvajyam
- 01.0264 889/895 99.3% | krut/yat/M:KajyaH | krut/yat/F:KajyA | krut/yat/N:Kajyam | yangluk_krut/yat/M:KajyaH | yangluk_krut/yat/F:KajyA | yangluk_krut/yat/N:Kajyam
- 01.0265 889/895 99.3% | krut/yat/M:kavyaH | krut/yat/F:kavyA | krut/yat/N:kavyam | yangluk_krut/yat/M:kavyaH | yangluk_krut/yat/F:kavyA | yangluk_krut/yat/N:kavyam
- 01.0279 889/895 99.3% | krut/yat/M:gajyaH | krut/yat/F:gajyA | krut/yat/N:gajyam | yangluk_krut/yat/M:gajyaH | yangluk_krut/yat/F:gajyA | yangluk_krut/yat/N:gajyam
- 01.0285 889/895 99.3% | krut/yat/M:vajyaH | krut/yat/F:vajyA | krut/yat/N:vajyam | yangluk_krut/yat/M:vajyaH | yangluk_krut/yat/F:vajyA | yangluk_krut/yat/N:vajyam
- 01.0337 889/895 99.3% | krut/yat/M:vawyaH | krut/yat/F:vawyA | krut/yat/N:vawyam | yangluk_krut/yat/M:vawyaH | yangluk_krut/yat/F:vawyA | yangluk_krut/yat/N:vawyam
- 01.0343 889/895 99.3% | krut/yat/M:JawyaH | krut/yat/F:JawyA | krut/yat/N:Jawyam | yangluk_krut/yat/M:JawyaH | yangluk_krut/yat/F:JawyA | yangluk_krut/yat/N:Jawyam
- 01.0344 889/895 99.3% | krut/yat/M:BawyaH | krut/yat/F:BawyA | krut/yat/N:Bawyam | yangluk_krut/yat/M:BawyaH | yangluk_krut/yat/F:BawyA | yangluk_krut/yat/N:Bawyam
- 01.0346 889/895 99.3% | krut/yat/M:KawyaH | krut/yat/F:KawyA | krut/yat/N:Kawyam | yangluk_krut/yat/M:KawyaH | yangluk_krut/yat/F:KawyA | yangluk_krut/yat/N:Kawyam

## Next actions
1. ting/liw+luN guna + sannanta Satf (same Pit/Kit pattern).
2. krut/yat guna (KadyaH).
3. R-initial + vowel-yak + yang.
4. Re-sweep --all, move newly-100% to passes table, keep compact.
