# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import).
Date: 2026-09-04T20:10:56Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **343/1166 100%**. Fails: 823. See tests/sweep_all.csv (grep).

## Rules (general)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist, krdanta guna, liw Pit/Kit+e+final-cons, yak e+final, luN at/guNa, ASIrliN D/Q, yat vriddhi.

## Fails (823)
| anta | n | example |
|---|---|---|
| krut | 4906 | 01.0038 krut/yat/M:atyaH |
| ting | 2835 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| nich_krut | 823 | 01.0082 nich_krut/SAnac/M:SrekyamAnaH |
| san_krut | 354 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 272 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| san | 210 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang_krut | 199 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| yang | 197 | 01.0048 yang/lw/prathama/eka:mAmanTyate |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayate |

### Next >=97%
- 01.1023 892/895 99.7% | yang_krut/yat/M:cAcAyyaH | yang_krut/yat/F:cAcAyyA | yang_krut/yat/N:cAcAyyam
- 01.0564 868/883 98.3% | nich_krut/SAnac/M:vAlyamAnaH | nich_krut/SAnac/F:vAlyamAnA | nich_krut/SAnac/N:vAlyamAnam | nich_krut/tavya/M:vAlayitavyaH | nich_
- 01.0867 868/883 98.3% | nich_krut/SAnac/M:GAwyamAnaH | nich_krut/SAnac/F:GAwyamAnA | nich_krut/SAnac/N:GAwyamAnam | nich_krut/tavya/M:GAwayitavyaH | nich_
- 01.0869 868/883 98.3% | nich_krut/SAnac/M:prATyamAnaH | nich_krut/SAnac/F:prATyamAnA | nich_krut/SAnac/N:prATyamAnam | nich_krut/tavya/M:prATayitavyaH | n
- 01.0870 868/883 98.3% | nich_krut/SAnac/M:prAsyamAnaH | nich_krut/SAnac/F:prAsyamAnA | nich_krut/SAnac/N:prAsyamAnam | nich_krut/tavya/M:prAsayitavyaH | n
- 01.0871 868/883 98.3% | nich_krut/SAnac/M:mrAdyamAnaH | nich_krut/SAnac/F:mrAdyamAnA | nich_krut/SAnac/N:mrAdyamAnam | nich_krut/tavya/M:mrAdayitavyaH | n
- 01.0872 868/883 98.3% | nich_krut/SAnac/M:sKAdyamAnaH | nich_krut/SAnac/F:sKAdyamAnA | nich_krut/SAnac/N:sKAdyamAnam | nich_krut/tavya/M:sKAdayitavyaH | n
- 01.0881 868/883 98.3% | nich_krut/SAnac/M:kAdyamAnaH | nich_krut/SAnac/F:kAdyamAnA | nich_krut/SAnac/N:kAdyamAnam | nich_krut/tavya/M:kAdayitavyaH | nich_
- 01.0882 868/883 98.3% | nich_krut/SAnac/M:krAdyamAnaH | nich_krut/SAnac/F:krAdyamAnA | nich_krut/SAnac/N:krAdyamAnam | nich_krut/tavya/M:krAdayitavyaH | n
- 01.0883 868/883 98.3% | nich_krut/SAnac/M:klAdyamAnaH | nich_krut/SAnac/F:klAdyamAnA | nich_krut/SAnac/N:klAdyamAnam | nich_krut/tavya/M:klAdayitavyaH | n
- 01.0931 868/883 98.3% | nich_krut/SAnac/M:sKAdyamAnaH | nich_krut/SAnac/F:sKAdyamAnA | nich_krut/SAnac/N:sKAdyamAnam | nich_krut/tavya/M:sKAdayitavyaH | n
- 01.0086 865/883 98.0% | ting/liw/prathama/eka:sizeke | ting/liw/prathama/dvi:sizekAte | ting/liw/prathama/bahu:sizekire | ting/liw/madhyama/eka:sizekize |
