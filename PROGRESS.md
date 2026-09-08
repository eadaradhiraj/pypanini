# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-07T00:00:00Z
Sweep: 717/1156 100% (raw 717/1166)

## Done
- Pure generative B/d D-devoicing in SAnac: B-final short-a/e -> C0+ip (`ripsamAnaH`; zmiN/guN R-keepers excluded by vowel gate); d-final -> devoice coda keep rest (`jihatsamAnaH`). yaBa/zada neutral (unscored); skandi/Sada bonus hits.
- Tinanta yak-luw plain-base alongside guna-forms (SunDitA/bukkitA/kUjitA): dataset survey of 1156 yak/alut fids — 1057 plain-itA, 0 guna, 99 sandhi-plain (teptA/kzantA/sedDA); zero conflicts. Sweep: 77 improved (+613 tokens), 0 worsened. Pilots OK.
- Krdanta yat-F short-num stem for i-final vowel-initial idit/Atmane roots (aNkyA/aRwyA/ambyA/fYjyA; M/N keep vriddhi cross-match): surveyed all 15 branch fids, zero conflicts. Sweep: 15 improved, 0 worsened. Pilots OK.
- Krdanta yat vriddhi for a + single non-nasal cons (aqa->Aqya, ata->Atya, aka->Akya; am/nasal-final, clusters, geminates, r-codas, u/i-finals stay short): surveyed 12 fids, zero conflicts. Sweep: 9 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN vowel-initial redup-aorist for a-initial roots (A+[num]+Ci+stem+ata): first attempt reverted (early-return skipped fallback); retry merges fallback. Sweep: 8 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN C-initial num-assimilated ay-less bases + R->n redup (sraki->sraNk, gaqi->gaRq): surveyed 176, additive. Sweep: 120 improved, 0 worsened. Pilots OK.
- Krdanta yat num-short for i-final idit C-initial roots (sraki->sraNkya, gaqi->gaRqya, bahi->baMhya): surveyed 176, zero conflicts. Sweep: 120 improved, 0 worsened. Pilots OK.
- Tinanta idit dental-num R for v-final r/f-onset roots at derive-clean source (rivi->riRv, kfvi->kfR, ravi->raR): first stab in _prim_bases was dead code — moved to source. Sweep: 3 improved (+1900 tokens), 0 worsened. Pilots OK.
- Krdanta idit dental-num R for v-final r/f-onset at derive-clean source (rivi->riRvitaH/riRvan/riRvyamARaH): surveyed shape (only rivi/ravi/kfvi). Sweep: 3 improved (+365 tokens), 0 worsened. Pilots OK.
- Tinanta onset R->n in meta (Ridi->nindati etc, mirrors krdanta; surveyed all 22 R-roots): all 22 improved, 0 worsened. Pilots OK.
- Krdanta lyap R-twins (praRaKya/praRaNKya for all 22 R-roots surveyed; avyaya any-match): 6 fids perfect, 0 worsened. Pilots OK.
- Krdanta yanluganta SAnac keeps -ya- with stem-based Natva (SASlaNkyamAna/sAsraNkyamARa): first cut worsened 7, fixed within iteration. Sweep: 67 improved, 0 worsened. Pilots OK.
- Tinanta+krdanta idit dental-num M for s-final (Sasi->SaMs at derive-clean source, both files; surveyed: sole s-final idit in dataset). Sweep: 1 improved (+883 tokens), 0 worsened. Pilots OK.
- Krdanta mit-denial respected (kamu/ama/camu NOT mit; niC vriddhi Amay-). Sweep: 1 improved, 0 worsened. Pilots OK.
- Krdanta yat never vriddhi on m-final (dramya/yamya/Camya/ramya/gamya; surveyed all m-final yat). Sweep: 7 improved, 0 worsened. Pilots OK.
- Krdanta yat vriddhi on first a for e-final C-initial (kaKe->kAKya; surveyed all 18 e-final yat). Sweep: 14 improved, 0 worsened. Pilots OK.
- E-anubandha strip at meta source in both files (kaKe~->kaK like f/X/R/z strips; cate te~ excluded). Sweep: 14 improved to perfect, 0 worsened. Pilots OK.
- Krdanta niC stem num-Y for ncu-final (ancu->aYcay; surveyed all 9 ncu-files). Sweep: 9 improved, 0 worsened. Pilots OK.
- Krdanta niC stem guna-o for double-u CuCu-roots (kuju->kojay; first cut hit single-u sru-family, gate caught 6 worsened, refined to first-u-not-final). Re-sweep: `717/1156` held, 8 improved (+26/+19), 0 worsened. Pilots OK.

## Next
1. Batch next, ONE narrow rule (survey first): niC-stem guna-e for izu-roots (jizu->jezay ×5) or asu vriddhi (grAsay ×3) or kamu/camu first-vowel niC vriddhi or kfvi laT o-guna (likely SKIP, singleton).
2. Then: suppletive aja (avIvayata) / zwaBi / wunadi singletons (likely SKIP); zw-origin cluster (stA-).
3. Re-sweep, rebuild STATS, overwrite this, commit & push.
