# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import).
Date: 2026-09-05T04:33:34Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **344/1166 100%**. Fails: 822. See tests/sweep_all.csv (grep).

## Rules (general)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist, krdanta guna, liw Pit/Kit+e+final-cons, yak e+final, luN at/guNa, ASIrliN D/Q, yat vriddhi, yang_krut/yat palatal+Ay->Iy (cAy->cekIyya, 7.3.52 coH kuH).

## Fails (822)
| anta | n | example |
|---|---|---|
| krut | 4906 | 01.0038 krut/yat/M:atyaH |
| ting | 2835 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| nich_krut | 823 | 01.0082 nich_krut/SAnac/M:SrekyamAnaH |
| san_krut | 354 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 272 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| san | 210 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang | 197 | 01.0048 yang/lw/prathama/eka:mAmanTyate |
| yang_krut | 196 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayate |

### Next >=97%
- 01.0564 868/883 98.3% | nich_krut/SAnac/M:vAlyamAnaH | nich_krut/SAnac/F:vAlyamAnA | nich_krut/SAnac/N:vAlyamAnam | nich_krut/tavya/M:vAlayitavyaH | nich_krut/tavya/F:vAlayitavyA | nic
- 01.0867 868/883 98.3% | nich_krut/SAnac/M:GAwyamAnaH | nich_krut/SAnac/F:GAwyamAnA | nich_krut/SAnac/N:GAwyamAnam | nich_krut/tavya/M:GAwayitavyaH | nich_krut/tavya/F:GAwayitavyA | nic
- 01.0869 868/883 98.3% | nich_krut/SAnac/M:prATyamAnaH | nich_krut/SAnac/F:prATyamAnA | nich_krut/SAnac/N:prATyamAnam | nich_krut/tavya/M:prATayitavyaH | nich_krut/tavya/F:prATayitavyA
- 01.0867 868/883 98.3% | nich_krut/SAnac/M:GAwyamAnaH | nich_krut/SAnac/F:GAwyamAnA | nich_krut/SAnac/N:GAwyamAnam | nich_krut/tavya/M:GAwayitavyaH | nich_krut/tavya/F:GAwayitavyA | nic
- 01.0869 868/883 98.3% | nich_krut/SAnac/M:prATyamAnaH | nich_krut/SAnac/F:prATyamAnA | nich_krut/SAnac/N:prATyamAnam | nich_krut/tavya/M:prATayitavyaH | nich_krut/tavya/F:prATayitavyA
- 01.0870 868/883 98.3% | nich_krut/SAnac/M:prAsyamAnaH | nich_krut/SAnac/F:prAsyamAnA | nich_krut/SAnac/N:prAsyamAnam | nich_krut/tavya/M:prAsayitavyaH | nich_krut/tavya/F:prAsayitavyA
- 01.0871 868/883 98.3% | nich_krut/SAnac/M:mrAdyamAnaH | nich_krut/SAnac/F:mrAdyamAnA | nich_krut/SAnac/N:mrAdyamAnam | nich_krut/tavya/M:mrAdayitavyaH | nich_krut/tavya/F:mrAdayitavyA
- 01.0872 868/883 98.3% | nich_krut/SAnac/M:sKAdyamAnaH | nich_krut/SAnac/F:sKAdyamAnA | nich_krut/SAnac/N:sKAdyamAnam | nich_krut/tavya/M:sKAdayitavyaH | nich_krut/tavya/F:sKAdayitavyA
- 01.0881 868/883 98.3% | nich_krut/SAnac/M:kAdyamAnaH | nich_krut/SAnac/F:kAdyamAnA | nich_krut/SAnac/N:kAdyamAnam | nich_krut/tavya/M:kAdayitavyaH | nich_krut/tavya/F:kAdayitavyA | nic
- 01.0882 868/883 98.3% | nich_krut/SAnac/M:krAdyamAnaH | nich_krut/SAnac/F:krAdyamAnA | nich_krut/SAnac/N:krAdyamAnam | nich_krut/tavya/M:krAdayitavyaH | nich_krut/tavya/F:krAdayitavyA
- 01.0883 868/883 98.3% | nich_krut/SAnac/M:klAdyamAnaH | nich_krut/SAnac/F:klAdyamAnA | nich_krut/SAnac/N:klAdyamAnam | nich_krut/tavya/M:klAdayitavyaH | nich_krut/tavya/F:klAdayitavyA
- 01.0931 868/883 98.3% | nich_krut/SAnac/M:sKAdyamAnaH | nich_krut/SAnac/F:sKAdyamAnA | nich_krut/SAnac/N:sKAdyamAnam | nich_krut/tavya/M:sKAdayitavyaH | nich_krut/tavya/F:sKAdayitavyA
