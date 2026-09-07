# Generative Validation Stats (compact)

Engine: wholly generative (NO per-dhatu, NO JSON import, pure shape/class).
Date: 2026-09-06T00:00:00Z
Run: unittest pilots + sweep_gana.py --all --workers 8 --out tests/sweep_all.csv.
Passes: **565/1156 100%** (raw 565/1166, 10 skipped). Fails: 591 scored. See tests/sweep_all.csv (grep).

## Rules (general, pure generative)
- Anubandha, redup 7.4.62, yan e/o, kta I~ block (yatI->yatta) + assimilated num for idit-i (agi->aNgita via op i~ gate), Nic aorist, krdanta guna, Satf stem decision tree (urv-lengthen; long-U/I keep; geminate keep; NC assimilate palatal/labial; short-u/i single-C guna; R-final blocked), liw Pit/Kit+e+final-cons + redup primaries for every variant (luWi->luluRWa) + urv o/u-redup + a+r n-redup + idit-i num redups (An on numclean, redup(numclean)) + z-base restore via op-derived unmapped clean (ziDa->sizeDiTa), yak e+final + yak-liw vriddhi-Atmane finite (ata->Ate, a+single-C minus j, 12 roots surveyed), yak-ASIrliN sannanta alt stems, luN at/guNa + seT Urv-base (atUrvIt) + num-base (ENgIt), ASIrliN D/Q + urv-lengthening (tUrvyAt) + num-base (iNgyAt), yat vriddhi (kr-onset no-vriddhi krapya, kr+T blocks yat, ts/km/kz-onset blocks yat), yang_krut/yat palatal+Ay->Iy, Nic mit/GawAdi hrasva except kr+T + single-r allows vriddhi, liw satva blocked s+stop/final-k, liw periphrastic Am+AYcakre + on numclean/numay (igi->iNgAYcakAra, agi->aNgayAYcakre), liw i-redup, kta i-guna m+i+d, kta w-final w+ta->wwa, yat I~ except w-final, Natva `_natva_applies` (z-final always R; h-final R iff r/R; s/S-final never R; else R iff r/R + velar/labial/sonorant final; R-final blocked), loT ni->Ri (r/R + velar/labial/sonorant/h/z/S final, or z-final always; s-final always dental; R-final blocked), sannanta Ci-copy stem with velar/h palatalization in redup + W-deaspiration (UWa->UwiWiz) + i-final velar/palatal Y-insertion + mUla/yak/san/nich/yang/yanluganta assimilated-num, sannanta voicing ti/di + redup-vowel o/O->u, sannanta devoiced-no-iz alt for Du/dx-final, sannanta kta-family always-iT, krdanta nijanta numclean+ay sec (agi->aNgay), krdanta yanluganta Y-class sec, yang z-restore for high-vowel onsets, krdanta mUla idit-i numclean remaining forms (tumun/ktvA/lyap/Rvul/GaY/Satf), krdanta yan-sec nasal trio (maTya/kUya/vaMvanya), krdanta/tinanta yan nasal trio, yan redup-M (n/R/m + prefinal-a; japa/Pala/zev/pat/kas singletons skipped), krdanta yan-sec Y-num mirror, mUla-yat Y-gate single-vowel (ANkayaH), tinanta yak-luN Y-num over-gen (ANkayizAtAm + ay-variant), sannanta Ci-branch C2-reduplication for C1+stop tails (andidiz/antitiz; sibilant-tails keep full), sannanta redup-vowel follows FIRST vowel (yuyuNg-/cicam-), sannanta-Satf aniT-cons desiderative-s (titapsat; sew_raw cache), sannanta-Satf U+p-coda opAy-base (jugopAyizat; post-redup u->o), sannanta r-strip only if more follows (oRiRiz/aRiRiz), sannanta ends-i retroflex/labial num-only (aRwiwiz/ambiBiz), sannanta-SAnac aniT-D s-form+dental (titipsamAnaH), N-final D-reductions (eN->C0+it mitsamAnaH; EN/AN->A jigAsamAnaH), harness keeps "-" as token; skipped sutra-headers unscored.

## Fails (617 scored)
| anta | n | example |
|---|---|---|
| krut | 3174 | 01.0690 krut/SAnac/M:BikzamARaH |
| ting | 1958 | 01.0374 ting/liw/prathama/eka:leluWAyva |
| yak | 230 | 01.0640 yak/liw/prathama/eka:cacare |
| yang_krut | 78 | 01.0048 yang_krut/kta/M:mAmanTitaH |
| yang | 20 | 01.0048 yang/lw/prathama/eka:mAmanwIti |
| san_krut | 82 | 01.0840 san_krut/kta/M:ujihizitaH |
| san | 17 | 01.0512 san/lw/prathama/eka:atiRizati |
| nich_krut | 179 | 01.0050 nich_krut/kta/M:seDayitaH |
| nich | 134 | 01.0559 nich/lw/prathama/eka:kzmAyayati |
| yangluk_krut | 147 | 01.0068 yangluk_krut/kta/M:ganqitaH |
