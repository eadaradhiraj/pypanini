# Generative Validation Stats (compact)

Engine: wholly generative (tinanta/krdanta from pada/sew/gana/vowel-initial, NO per-dhatu `if clean=="x"`, NO JSON import for generation).
Cross-check: `skt-morph-data/01/*.json` read-only, any-token match counts as hit.
Date: 2026-09-04T19:48:53Z
Run: `python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v` (pilots 01.0001-01.0003 must stay OK) + `PYTHONIOENCODING=utf-8 python tests/sweep_gana.py --all --workers 8 --out tests/sweep_all.csv` (shared engine cache, ~0.1s/dhatu).
Passes: **248/1166 100%**. Fails: 918. Full per-dhatu logs removed to save context — see table + `tests/sweep_all.csv` (fid,matched,total,pct,misses, 1166 rows, query via `grep`, do not dump).

## How to validate (for next LLM)
- Single: `PYTHONIOENCODING=utf-8 python tests/test_dhatu.py 01.0038` (verbose, GRAND must be 100%).
- Batch: `PYTHONIOENCODING=utf-8 python tests/sweep_gana.py --from 01.0038 --to 01.0100 --workers 8`.
- GRAND = tinanta + krdanta. yangluk non-lw excluded.
- Workflow: fix generally via sutra -> `test_dhatu.py <id>` -> `unittest` pilots -> update this file + `git add -A && git commit -m "..." && git push`.

## Algorithmic rules (general, do NOT re-add per-dhatu tables)
- Anubandha: `~r/U~/I~/i~`, `f/F/x/X`, trailing-`a`, `z→s`. `I~` strips allow-guNa, `i~` num blocks guNa.
- Redup `7.4.62`: `s/S+stop→stop` else `s`; `abhyasa e→i o→u`; `yan e/o`; `sannanta ti/di` both.
- `kta`/`yat` (`7.2.10/3.1.124`): `I~→no-iT` (yatta), `yat` vriddhi unless `I~` (KAdya vs yatya); `c/j→k`, `d→nna/t→tta`.
- `Nic` aorist: `a+redup+base+ata…`, `e→i/o→u`, `ur→Ur/or`; Nic vriddhi single-cons no-r.
- `krdanta guNa`: `SAnac/Rvul/GaY` guna `i`; `Rvul` clean `e/o`; `Satf` mUla+yanluganta→guna else sec.
- `liw Pit/Kit`, vowel-liw periphrastic+vriddhi, `luN at/guNa+I`, `ASIrliN IDvam+IQvam`.

## Passes (248, all 100%)
| fid | OpadeSika | GRAND |
|---|---|---|
| 01.0001 | BU | 895/895 |
| 01.0002 | eDa~ | 627/627 |
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
| 01.0020 | urda~ | 627/627 |
| 01.0021 | kurda~ | 883/883 |
| 01.0022 | Kurda~ | 883/883 |
| 01.0023 | gurda~ | 883/883 |
| 01.0024 | guda~ | 883/883 |
| 01.0025 | zUda~ | 883/883 |
| 01.0026 | hrAda~ | 883/883 |
| 01.0027 | hlAdI~ | 883/883 |
| 01.0028 | svAda~ | 883/883 |
| 01.0030 | yatI~ | 883/883 |
| 01.0031 | yutf~ | 883/883 |
| 01.0032 | jutf~ | 883/883 |
| 01.0033 | viTf~ | 883/883 |
| 01.0034 | veTf~ | 883/883 |
| 01.0035 | SraTi~ | 883/883 |
| 01.0036 | graTi~ | 883/883 |
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
| 01.0052 | Kada~ | 895/895 |
| 01.0054 | gada~ | 895/895 |
| 01.0066 | bidi~ | 895/895 |
| 01.0067 | Bidi~ | 895/895 |
| 01.0071 | cadi~ | 895/895 |
| 01.0072 | tradi~ | 895/895 |
| 01.0073 | kadi~ | 895/895 |
| 01.0074 | kradi~ | 895/895 |
| 01.0075 | kladi~ | 895/895 |
| 01.0076 | klidi~ | 895/895 |
| 01.0095 | kaka~ | 883/883 |
| 01.0096 | kuka~ | 883/883 |
| 01.0108 | wikf~ | 883/883 |
| 01.0110 | tikf~ | 883/883 |
| 01.0119 | lAGf~ | 883/883 |
| 01.0122 | SlAGf~ | 883/883 |
| 01.0127 | Suka~ | 895/895 |
| 01.0128 | kaKa~ | 895/895 |
| 01.0131 | lAKf~ | 895/895 |
| 01.0134 | SAKf~ | 895/895 |
| 01.0135 | SlAKf~ | 895/895 |
| 01.0138 | vaKa~ | 895/895 |
| 01.0160 | Svelf~ | 895/895 |
| 01.0179 | GaGa~ | 895/895 |
| 01.0190 | Svaca~ | 883/883 |
| 01.0192 | kaca~ | 883/883 |
| 01.0204 | Brejf~ | 883/883 |
| 01.0205 | BrAjf~ | 883/883 |
| 01.0206 | kAqf~ | 883/883 |
| 01.0208 | pebf | 883/883 |
| 01.0209 | plebf~ | 883/883 |
| 01.0210 | Suca~ | 895/895 |
| 01.0211 | kuca~ | 895/895 |
| 01.0230 | guja~ | 895/895 |
| 01.0245 | Draja~ | 895/895 |
| 01.0251 | Dvaja~ | 895/895 |
| 01.0263 | teja~ | 895/895 |
| 01.0264 | Kaja~ | 895/895 |
| 01.0265 | kava~ | 895/895 |
| 01.0273 | lAja~ | 895/895 |
| 01.0277 | tuja~ | 895/895 |
| 01.0279 | gaja~ | 895/895 |
| 01.0283 | muja~ | 895/895 |
| 01.0285 | vaja~ | 895/895 |
| 01.0286 | vraja~ | 895/895 |
| 01.0288 | vezwa~ | 883/883 |
| 01.0289 | cezwa~ | 883/883 |
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
| 01.0337 | vawa~ | 895/895 |
| 01.0338 | kiwa~ | 895/895 |
| 01.0339 | Kiwa~ | 895/895 |
| 01.0340 | Siwa~ | 895/895 |
| 01.0343 | Jawa~ | 895/895 |
| 01.0344 | Bawa~ | 895/895 |
| 01.0346 | Kawa~ | 895/895 |
| 01.0348 | piwa~ | 895/895 |
| 01.0349 | hawa~ | 895/895 |
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
| 01.0382 | vaWa~ | 895/895 |
| 01.0385 | kaWa~ | 895/895 |
| 01.0388 | haWa~ | 895/895 |
| 01.0389 | ruWa~ | 895/895 |
| 01.0390 | luWa~ | 895/895 |
| 01.0393 | piWa~ | 895/895 |
| 01.0395 | SuWa~ | 895/895 |
| 01.0406 | tuqf~ | 895/895 |
| 01.0408 | huqf~ | 895/895 |
| 01.0417 | kaqa~ | 895/895 |
| 01.0421 | tepf~ | 883/883 |
| 01.0424 | glepf~ | 883/883 |
| 01.0426 | kepf~ | 883/883 |
| 01.0427 | gepf~ | 883/883 |
| 01.0428 | glepf~ | 883/883 |
| 01.0429 | mepf~ | 883/883 |
| 01.0431 | lepf~ | 883/883 |
| 01.0432 | hepf~ | 883/883 |
| 01.0433 | Depf~ | 883/883 |
| 01.0469 | cupa~ | 895/895 |
| 01.0470 | tupa~ | 895/895 |
| 01.0474 | tuPa~ | 895/895 |
| 01.0500 | SuBa~ | 895/895 |
| 01.0505 | GuRa~ | 883/883 |
| 01.0506 | GurRa~ | 883/883 |
| 01.0509 | BAma~ | 883/883 |
| 01.0527 | pERf~ | 895/895 |
| 01.0528 | prERf~ | 895/895 |
| 01.0547 | vaya~ | 883/883 |
| 01.0562 | tAyf~ | 883/883 |
| 01.0568 | Bala~ | 883/883 |
| 01.0570 | kala~ | 883/883 |
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
| 01.0589 | haya~ | 895/895 |
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
| 01.0626 | Kala~ | 895/895 |
| 01.0627 | gala~ | 895/895 |
| 01.0630 | Svala~ | 895/895 |
| 01.0671 | pivi~ | 895/895 |
| 01.0672 | mivi~ | 895/895 |
| 01.0675 | hivi~ | 895/895 |
| 01.0676 | divi~ | 895/895 |
| 01.0678 | jivi~ | 895/895 |
| 01.0681 | Davi~ | 895/895 |
| 01.0691 | kleSa~ | 883/883 |
| 01.0711 | BAsf~ | 883/883 |
| 01.0713 | rAsf~ | 883/883 |
| 01.0715 | Byasa~ | 883/883 |
| 01.0729 | pliha~ | 883/883 |
| 01.0730 | vehf~ | 883/883 |
| 01.0731 | jehf~ | 883/883 |
| 01.0732 | bAhf~ | 883/883 |
| 01.0734 | kASf~ | 883/883 |
| 01.0738 | glaha~ | 883/883 |
| 01.0807 | tusa~ | 895/895 |
| 01.0808 | hrasa~ | 895/895 |
| 01.0809 | hlasa~ | 895/895 |
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
| 01.0912 | kraTa~ | 895/895 |
| 01.0916 | jvala~ | 895/895 |
| 01.0917 | hvala~ | 895/895 |
| 01.0918 | hmala~ | 895/895 |
| 01.0947 | mleqf~ | 895/895 |
| 01.0948 | mewf~ | 895/895 |
| 01.0949 | biqa~ | 895/895 |
| 01.0952 | vAhf~ | 883/883 |
| 01.0956 | rAjf~ | 895/895 |
| 01.0965 | jvala~ | 895/895 |
| 01.0969 | wvala~ | 895/895 |
| 01.0971 | hala~ | 895/895 |
| 01.0975 | pula~ | 895/895 |
| 01.0976 | kula~ | 895/895 |
| 01.0978 | hula~ | 895/895 |
| 01.0980 | kzala~ | 895/895 |
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
| 01.1024 | vyaya~ | 895/895 |
| 01.1025 | dASf~ | 895/895 |
| 01.1032 | spaSa~ | 895/895 |
| 01.1041 | dAsf~ | 895/895 |
| 01.1042 | mAhf~ | 895/895 |

## Fails (918) by anta
| anta | miss-hits | example |
|---|---|---|
| krut | 5164 | 01.0003 krut/yat/M:spArDyaH |
| ting | 3242 | 01.0049 ting/liw/madhyama/eka:siziDiTa |
| nich_krut | 625 | 01.0082 nich_krut/SAnac/M:SrekyamAnaH |
| san_krut | 354 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 268 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| san | 208 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang_krut | 193 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| yang | 137 | 01.0048 yang/lw/prathama/eka:mAmanTyate |
| yangluk_krut | 117 | 01.0003 yangluk_krut/yat/M:spArDyaH |
| nich | 16 | 01.0440 nich/luN/prathama/eka:akAbayizwa |

### Easiest next (>=97%)
- 01.0440 882/883 99.9% | nich/luN/prathama/eka:akAbayizwa
- 01.1023 892/895 99.7% | yang_krut/yat/M:cAcAyyaH | yang_krut/yat/F:cAcAyyA | yang_krut/yat/N:cAcAyyam
- 01.0003 877/883 99.3% | krut/yat/M:spArDyaH | krut/yat/F:spArDyA | krut/yat/N:spArDyam | yangluk_krut/yat/M:spArDyaH | yangluk_krut/yat/F:spArDyA | yangluk_krut/yat/N:spArDya
- 01.0019 877/883 99.3% | krut/yat/M:svArdyaH | krut/yat/F:svArdyA | krut/yat/N:svArdyam | yangluk_krut/yat/M:svArdyaH | yangluk_krut/yat/F:svArdyA | yangluk_krut/yat/N:svArdya
- 01.0029 877/883 99.3% | krut/yat/M:pArdyaH | krut/yat/F:pArdyA | krut/yat/N:pArdyam | yangluk_krut/yat/M:pArdyaH | yangluk_krut/yat/F:pArdyA | yangluk_krut/yat/N:pArdyam
- 01.0037 877/883 99.3% | krut/yat/M:kAtTyaH | krut/yat/F:kAtTyA | krut/yat/N:kAtTyam | yangluk_krut/yat/M:kAtTyaH | yangluk_krut/yat/F:kAtTyA | yangluk_krut/yat/N:kAtTyam
- 01.0058 889/895 99.3% | krut/yat/M:nArdyaH | krut/yat/F:nArdyA | krut/yat/N:nArdyam | yangluk_krut/yat/M:nArdyaH | yangluk_krut/yat/F:nArdyA | yangluk_krut/yat/N:nArdyam
- 01.0059 889/895 99.3% | krut/yat/M:gArdyaH | krut/yat/F:gArdyA | krut/yat/N:gArdyam | yangluk_krut/yat/M:gArdyaH | yangluk_krut/yat/F:gArdyA | yangluk_krut/yat/N:gArdyam
- 01.0060 889/895 99.3% | krut/yat/M:tArdyaH | krut/yat/F:tArdyA | krut/yat/N:tArdyam | yangluk_krut/yat/M:tArdyaH | yangluk_krut/yat/F:tArdyA | yangluk_krut/yat/N:tArdyam
- 01.0061 889/895 99.3% | krut/yat/M:kArdyaH | krut/yat/F:kArdyA | krut/yat/N:kArdyam | yangluk_krut/yat/M:kArdyaH | yangluk_krut/yat/F:kArdyA | yangluk_krut/yat/N:kArdyam
- 01.0062 889/895 99.3% | krut/yat/M:KArdyaH | krut/yat/F:KArdyA | krut/yat/N:KArdyam | yangluk_krut/yat/M:KArdyaH | yangluk_krut/yat/F:KArdyA | yangluk_krut/yat/N:KArdyam
- 01.0106 877/883 99.3% | krut/yat/M:vAskyaH | krut/yat/F:vAskyA | krut/yat/N:vAskyam | yangluk_krut/yat/M:vAskyaH | yangluk_krut/yat/F:vAskyA | yangluk_krut/yat/N:vAskyam
- 01.0107 877/883 99.3% | krut/yat/M:mAskyaH | krut/yat/F:mAskyA | krut/yat/N:mAskyam | yangluk_krut/yat/M:mAskyaH | yangluk_krut/yat/F:mAskyA | yangluk_krut/yat/N:mAskyam
- 01.0114 877/883 99.3% | krut/yat/M:svAkkyaH | krut/yat/F:svAkkyA | krut/yat/N:svAkkyam | yangluk_krut/yat/M:svAkkyaH | yangluk_krut/yat/F:svAkkyA | yangluk_krut/yat/N:svAkkya
- 01.0123 889/895 99.3% | krut/yat/M:PAkkyaH | krut/yat/F:PAkkyA | krut/yat/N:PAkkyam | yangluk_krut/yat/M:PAkkyaH | yangluk_krut/yat/F:PAkkyA | yangluk_krut/yat/N:PAkkyam
- 01.0152 889/895 99.3% | krut/yat/M:vAlgyaH | krut/yat/F:vAlgyA | krut/yat/N:vAlgyam | yangluk_krut/yat/M:vAlgyaH | yangluk_krut/yat/F:vAlgyA | yangluk_krut/yat/N:vAlgyam
- 01.0180 889/895 99.3% | krut/yat/M:GAgGyaH | krut/yat/F:GAgGyA | krut/yat/N:GAgGyam | yangluk_krut/yat/M:GAgGyaH | yangluk_krut/yat/F:GAgGyA | yangluk_krut/yat/N:GAgGyam
- 01.0186 877/883 99.3% | krut/yat/M:vArcyaH | krut/yat/F:vArcyA | krut/yat/N:vArcyam | yangluk_krut/yat/M:vArcyaH | yangluk_krut/yat/F:vArcyA | yangluk_krut/yat/N:vArcyam
- 01.0257 889/895 99.3% | krut/yat/M:sArjyaH | krut/yat/F:sArjyA | krut/yat/N:sArjyam | yangluk_krut/yat/M:sArjyaH | yangluk_krut/yat/F:sArjyA | yangluk_krut/yat/N:sArjyam
- 01.0258 889/895 99.3% | krut/yat/M:gArjyaH | krut/yat/F:gArjyA | krut/yat/N:gArjyam | yangluk_krut/yat/M:gArjyaH | yangluk_krut/yat/F:gArjyA | yangluk_krut/yat/N:gArjyam
