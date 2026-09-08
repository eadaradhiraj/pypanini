# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-08T20:33:00Z
Sweep: 756/1156 100% (raw 756/1166)

## Done
- Pure generative B/d D-devoicing in SAnac: B-final short-a/e -> C0+ip (`ripsamAnaH`; zmiN/guN R-keepers excluded by vowel gate); d-final -> devoice coda keep rest (`jihatsamAnaH`). yaBa/zada neutral (unscored); skandi/Sada bonus hits.
- Tinanta yak-luw plain-base alongside guna-forms (SunDitA/bukkitA/kUjitA): dataset survey of 1156 yak/alut fids — 1057 plain-itA, 0 guna, 99 sandhi-plain (teptA/kzantA/sedDA); zero conflicts. Sweep: 77 improved (+613 tokens), 0 worsened. Pilots OK.
- Krdanta yat-F short-num stem for i-final vowel-initial idit/Atmane roots (aNkyA/aRwyA/ambyA/fYjyA; M/N keep vriddhi cross-match): surveyed all 15 branch fids, zero conflicts. Sweep: 15 improved, 0 worsened. Pilots OK.
- Krdanta yat vriddhi for a + single non-nasal cons (aqa->Aqya, ata->Atya, aka->Akya; am/nasal-final, clusters, geminates, r-codas, u/i-finals stay short): surveyed 12 fids, zero conflicts. Sweep: 9 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN vowel-initial redup-aorist for a-initial roots (A+[num]+Ci+stem+ata): first attempt reverted (early-return skipped fallback); retry merges fallback. Sweep: 8 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN C-initial num-assimilated ay-less bases + R->n redup (sraki->sraNk, gaqi->gaRq): surveyed 176, additive. Sweep: 120 improved, 0 worsened. Pilots OK.
- Krdanta yat num-short for i-final idit C-initial roots (sraki->sraNkya, gaqi->gaRqya, bahi->baMhya): surveyed 176, zero conflicts. Sweep: 120 improved, 0 worsened. Pilots OK.
- Tinanta idit dental-num R for v-final r/f-onset roots at derive-clean source (rivi->riRv, kfvi->kfR, ravi->raR): first stab in _prim_bases was dead code — moved to source. Sweep: 3 improved (+1900 tokens), 0 worsened. Pilots OK.
- Krdanta idit dental-num R for v-final r/f-onset at derive-clean source (rivi->riRvitaH/riRvan/riRvyamARaH): surveyed shape (only rivi/ravi/kfvi match). Sweep: 3 improved (+365 tokens), 0 worsened. Pilots OK.
- Tinanta onset R->n in meta (Ridi->nindati etc, mirrors krdanta; surveyed all 22 R-roots): all 22 improved, 0 worsened. Pilots OK.
- Krdanta lyap R-twins (praRaKya/praRaNKya for all 22 R-roots surveyed; avyaya any-match): 6 fids perfect, 0 worsened. Pilots OK.
- Krdanta yanluganta SAnac keeps -ya- with stem-based Natva (SASlaNkyamAna/sAsraNkyamARa): first cut worsened 7, fixed within iteration. Sweep: 67 improved, 0 worsened. Pilots OK.
- Tinanta+krdanta idit dental-num M for s-final (Sasi->SaMs at derive-clean source, both files; surveyed: sole s-final idit in dataset). Sweep: 1 improved (+883 tokens), 0 worsened. Pilots OK.
- Krdanta mit-denial respected (kamu/ama/camu NOT mit; niC vriddhi Amay-). Sweep: 1 improved, 0 worsened. Pilots OK.
- Krdanta yat never vriddhi on m-final (dramya/yamya/Camya/ramya/gamya; surveyed all m-final yat). Sweep: 7 improved, 0 worsened. Pilots OK.
- Krdanta yat vriddhi on first a for e-final C-initial (kaKe->kAKya; surveyed all e-final yat). Sweep: 14 improved, 0 worsened. Pilots OK.
- E-anubandha strip at meta source in both files (kaKe~->kaK like f/X/R/z strips; cate te~ excluded). Sweep: 14 improved to perfect, 0 worsened. Pilots OK.
- Krdanta niC stem num-Y for ncu-final (ancu->aYcay; surveyed all 9 ncu-files). Sweep: 9 improved, 0 worsened. Pilots OK.
- Krdanta niC stem guna-o for double-u CuCu-roots (kuju->kojay; gate refined after 6 worsened). Sweep: 8 improved, 0 worsened. Pilots OK.
- Krdanta niC stem guna-e for i..u-roots (jizu->jezay + bonus). Sweep: 8 improved, 0 worsened. Pilots OK.
- Krdanta niC stem mu/su first-vowel strengthening (camu->cAmay etc; jamu-mit excluded). Sweep: 10 improved, 0 worsened. Pilots OK.
- Tinanta mula-luN sic-aorist t/d-num + vocalic augment (ati->AntIt). Sweep: 12 improved, 0 worsened. Pilots OK.
- Tinanta liT redup num completion t/d/T->n + h->M (ati->Ananta; survived a bad-revert incident). Sweep: 7 improved, 0 worsened. Pilots OK.
- Tinanta yak-liT An-redup for a/f-initial (ati->Anante, fja->Anfje, arda->Anarde; idit num via op-recovery; caught an edit eating the next subsection's first line that broke 2 pilots, fixed pre-sweep). Re-sweep: `726/1156` held (+2 perfect: 01.0063/01.0064), 7 improved, 0 worsened. Pilots OK.
- Krdanta `_natva_applies` base-check on len>2 i-final roots (sraki->srak, 13 new 100% passes: 01.0088, 01.0089, 01.0102, 01.0112, 01.0145, 01.0153, 01.0161, 01.0164, 01.0173, 01.0436, 01.0449, 01.0480, 01.0945; surveyed all 35 i-roots, zero conflicts; sweep: 15 improved, 0 worsened, passes 726->739). Pilots OK.
- Tinanta vowel-initial velar/palatal Y-aorist de-aspirates palatals and includes thematic and atmanepada endings (ACi->AYcicCata, uCi->OYcicCata; 2 new 100% passes: 01.0237, 01.0243; 2 improved, 0 worsened, passes 739->741). Pilots OK.
- Generalized Paninian anubandha stripping in `clean_dhatu_op` across both engines and test runner: 1.3.5 ādirñiṭuḍavaḥ (wu/qu/Yi/wuo/quo/o), 1.3.3 halantyam (~z), 1.3.2 upadeśe'janunāsika it (udit u~/U~, A~ on idit/anubandha tails) alongside existing f/F/x/X/~r/I~/a/e~ anubandhas; updated krdanta `_nijanta_sec` for nc/ns codas without surface u. Sweep: 14 new 100% passes: 01.0070 (wunadi~), 01.0425 (wuvepf~), 01.0542 (jamu~), 01.0543 (Jamu~), 01.0685 (DAvu~), 01.0844 (YimidA~), 01.0884 (YitvarA~), 01.0951 (vanu~), 01.0954 (quyAcf~), 01.0957 (wuBrAjf~), 01.0959 (wuBlASf~), 01.0984 (wuvama~), 01.0985 (Bramu~), 01.1001 (wuyAcf~); 88 improved, 0 worsened, passes 741->755. Pilots OK.
- Krdanta yananta/yanluganta `_natva_applies` stem-level z-trigger with l-coda block (sevf->sezevyamARa; surveyed: avoids breaking kzvelf/zelf/kzala): 01.0574 100% perfect (883/883); sweep: 19 improved, 0 worsened, passes 755->756. Pilots OK.

## Next
1. Consonant cluster assimilation for Gaṇa 01:
   - `c/j` before `s/t` (e.g. `tyaj` -> `tyaktA`, `pac` -> `paktA`).
   - Periphrastic Liṭ for heavy clusters (`01.0287 awwAYcakre`, `01.0403 aqqAYcakre`).
   - NiC Satṛ for Gawādi roots (`kARayan`, `rARayan`, `SrARayan`).
2. Investigate closest-to-100% failing dhātus (e.g. misses <= 5 in `tests/sweep_all.csv`).
3. Re-sweep, rebuild STATS, overwrite this, commit & push.
