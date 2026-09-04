# Generative Validation Stats (compact)

Engine: wholly generative (tinanta/krdanta from pada/sew/gana/vowel-initial, NO per-dhatu, NO JSON import).
Cross-check: skt-morph-data read-only.
Date: 2026-09-04T20:05:27Z
Run: unittest pilots + sweep_gana --all --workers 8 --out tests/sweep_all.csv.
Passes: **331/1166 100%**. Fails: 835. See table + tests/sweep_all.csv (grep, do not dump).

## How to validate
- Single: python tests/test_dhatu.py 01.0038
- Batch: sweep_gana --from/--to
- GRAND = tinanta + krdanta.
- Workflow: fix generally -> test -> unittest -> update STATS+PROGRESS -> commit & push.

## Algorithmic rules (general)
- Anubandha, redup 7.4.62, yan e/o, kta I~, Nic aorist+vriddhi, krdanta guna, liw Pit/Kit+vriddhi+e-abhyasa+final-cons, yak liw e+final-cons, luN at/guNa, ASIrliN IDvam/IQvam, yat vriddhi.

## Fails (835) by anta
| anta | n | example |
|---|---|---|
| krut | 4906 | 01.0038 krut/yat/M:atyaH |
| ting | 2905 | 01.0049 ting/liw/madhyama/eka:siziDseDviTa |
| nich_krut | 818 | 01.0082 nich_krut/SAnac/M:SrekyamAnaH |
| san_krut | 354 | 01.0038 san_krut/kta/M:aditizitaH |
| yak | 272 | 01.0038 yak/liw/prathama/eka:atAYcakre |
| san | 210 | 01.0080 san/lw/prathama/eka:lilokizate |
| yang_krut | 199 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| yang | 192 | 01.0048 yang/lw/prathama/eka:mAmanTyate |
| nich | 15 | 01.0559 nich/lw/prathama/eka:kzmAyayati |

### Easiest next (>=97%)
- 01.1023 892/895 99.7% | yang_krut/yat/M:cAcAyyaH | yang_krut/yat/F:cAcAyyA | yang_krut/yat/N:cAcAyyam
- 01.0098 874/883 99.0% | ting/liw/prathama/eka:cacake | ting/liw/prathama/dvi:cacakAte | ting/liw/prathama/bahu:cacakire | ting/liw/madhyama/eka:cacakize | ting/liw/madhyama/d
- 01.0187 874/883 99.0% | ting/liw/prathama/eka:sasace | ting/liw/prathama/dvi:sasacAte | ting/liw/prathama/bahu:sasacire | ting/liw/madhyama/eka:sasacize | ting/liw/madhyama/d
- 01.0189 874/883 99.0% | ting/liw/prathama/eka:SaSace | ting/liw/prathama/dvi:SaSacAte | ting/liw/prathama/bahu:SaSacire | ting/liw/madhyama/eka:SaSacize | ting/liw/madhyama/d
- 01.0195 874/883 99.0% | ting/liw/prathama/eka:mamace | ting/liw/prathama/dvi:mamacAte | ting/liw/prathama/bahu:mamacire | ting/liw/madhyama/eka:mamacize | ting/liw/madhyama/d
- 01.0548 874/883 99.0% | ting/liw/prathama/eka:papaye | ting/liw/prathama/dvi:papayAte | ting/liw/prathama/bahu:papayire | ting/liw/madhyama/eka:papayize | ting/liw/madhyama/d
- 01.0549 874/883 99.0% | ting/liw/prathama/eka:mamaye | ting/liw/prathama/dvi:mamayAte | ting/liw/prathama/bahu:mamayire | ting/liw/madhyama/eka:mamayize | ting/liw/madhyama/d
- 01.0550 874/883 99.0% | ting/liw/prathama/eka:cacaye | ting/liw/prathama/dvi:cacayAte | ting/liw/prathama/bahu:cacayire | ting/liw/madhyama/eka:cacayize | ting/liw/madhyama/d
- 01.0551 874/883 99.0% | ting/liw/prathama/eka:tataye | ting/liw/prathama/dvi:tatayAte | ting/liw/prathama/bahu:tatayire | ting/liw/madhyama/eka:tatayize | ting/liw/madhyama/d
- 01.0555 874/883 99.0% | ting/liw/prathama/eka:yayaye | ting/liw/prathama/dvi:yayayAte | ting/liw/prathama/bahu:yayayire | ting/liw/madhyama/eka:yayayize | ting/liw/madhyama/d
- 01.0563 874/883 99.0% | ting/liw/prathama/eka:SaSale | ting/liw/prathama/dvi:SaSalAte | ting/liw/prathama/bahu:SaSalire | ting/liw/madhyama/eka:SaSalize | ting/liw/madhyama/d
- 01.0566 874/883 99.0% | ting/liw/prathama/eka:mamale | ting/liw/prathama/dvi:mamalAte | ting/liw/prathama/bahu:mamalire | ting/liw/madhyama/eka:mamalize | ting/liw/madhyama/d
- 01.0988 874/883 99.0% | ting/liw/prathama/eka:sasahe | ting/liw/prathama/dvi:sasahAte | ting/liw/prathama/bahu:sasahire | ting/liw/madhyama/eka:sasahize | ting/liw/madhyama/d
- 01.0564 868/883 98.3% | nich_krut/SAnac/M:vAlyamAnaH | nich_krut/SAnac/F:vAlyamAnA | nich_krut/SAnac/N:vAlyamAnam | nich_krut/tavya/M:vAlayitavyaH | nich_krut/tavya/F:vAlayit
- 01.0867 868/883 98.3% | nich_krut/SAnac/M:GAwyamAnaH | nich_krut/SAnac/F:GAwyamAnA | nich_krut/SAnac/N:GAwyamAnam | nich_krut/tavya/M:GAwayitavyaH | nich_krut/tavya/F:GAwayit
