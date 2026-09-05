# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import).
Date: 2026-09-05T05:07:23Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **370/1166 100%**. Fails: 796. See tests/sweep_all.csv (grep).

## Rules (general)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist, krdanta guna, liw Pit/Kit+e+final-cons, yak e+final, luN at/guNa, ASIrliN D/Q, yat vriddhi, yang_krut/yat palatal+Ay->Iy (cAy->cekIyya, 7.3.52), Nic mit/GawAdi hrasva (valaya, mit flag) except kr+T (kraTa), liw satva blocked for s+stop cluster (sk->cus, sP->pus) and final velar stop k (sek->siseke).

## Fails (796)
| anta | n | example |
|---|---|---|
| krut | 4906 | 01.0038 krut/yat/M:atyaH |
| ting | 2815 | 01.0049 ting/liw/madhyama/eka:siziDsiDviTa |
| nich_krut | 499 | 01.1006 krut/kta/M:miditaH |
| san_krut | 354 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 272 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| yang_krut | 242 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| san | 210 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang | 197 | 01.0048 yang/lw/prathama/eka:mAmanTyate |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayate |

### Next >=97%
- 01.1006 877/895 98.0% | krut/kta/M:miditaH | krut/kta/F:miditA | krut/kta/N:miditam | krut/ktavatu/M:miditavAn | krut/ktavatu/F:miditavatI | krut/ktavatu/N:miditavat | nich_krut/kta/M:miditaH |
- 01.0553 865/883 98.0% | ting/liw/prathama/eka:dadaye | ting/liw/prathama/dvi:dadayAte | ting/liw/prathama/bahu:dadayire | ting/liw/madhyama/eka:dadayize | ting/liw/madhyama/dvi:dadayATe
- 01.0710 865/883 98.0% | ting/liw/prathama/eka:cakAse | ting/liw/prathama/dvi:cakAsAte | ting/liw/prathama/bahu:cakAsire | ting/liw/madhyama/eka:cakAsize | ting/liw/madhyama/dvi:cakAsATe
- 01.0868 865/883 98.0% | ting/liw/prathama/eka:vavyaTe | ting/liw/prathama/dvi:vavyaTAte | ting/liw/prathama/bahu:vavyaTire | ting/liw/madhyama/eka:vavyaTize | ting/liw/madhyama/dvi:vavyaTATe
