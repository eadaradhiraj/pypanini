# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-07T00:00:00Z
Sweep: 638/1156 100% (raw 638/1166)

## Done
- Pure generative B/d D-devoicing in SAnac: B-final short-a/e -> C0+ip (`ripsamAnaH`; zmiN/guN R-keepers excluded by vowel gate); d-final -> devoice coda keep rest (`jihatsamAnaH`). yaBa/zada neutral (unscored); skandi/Sada bonus hits.
- Tinanta yak-luw plain-base alongside guna-forms (SunDitA/bukkitA/kUjitA): dataset survey of 1156 yak/alut fids — 1057 plain-itA, 0 guna, 99 sandhi-plain (teptA/kzantA/sedDA); zero conflicts. Sweep: 77 improved (+613 tokens), 0 worsened. Pilots OK.
- Krdanta yat-F short-num stem for i-final vowel-initial idit/Atmane roots (aNkyA/aRwyA/ambyA/fYjyA; M/N keep vriddhi cross-match): surveyed all 15 branch fids, zero conflicts. Sweep: 15 improved, 0 worsened. Pilots OK.
- Krdanta yat vriddhi for a + single non-nasal cons (aqa->Aqya, ata->Atya, aka->Akya; am/nasal-final, clusters, geminates, r-codas, u/i-finals stay short): surveyed 12 fids, zero conflicts. Sweep: 9 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN vowel-initial redup-aorist for a-initial roots (A+[num]+Ci+stem+ata): first attempt reverted (early-return skipped fallback); retry merges fallback. Sweep: 8 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN C-initial num-assimilated ay-less bases + R->n redup (sraki->sraNk, gaqi->gaRq): surveyed 176, additive. Sweep: 120 improved, 0 worsened. Pilots OK.
- Krdanta yat num-short for i-final idit C-initial roots (sraki->sraNkya, gaqi->gaRqya, bahi->baMhya): surveyed 176, zero conflicts. Sweep: 120 improved, 0 worsened. Pilots OK.
- Tinanta idit dental-num R for v-final r/f-onset roots at derive-clean source (rivi->riRv, kfvi->kfR, ravi->raR; all lakaras inherit; surveyed all v-roots, only these three R-dominant): first stab in _prim_bases was dead code (derive uses rewritten clean) — moved to source. Re-sweep: `638/1156` held, 3 improved (+1900 tokens: rivi 18->737, kfvi 0->490, ravi 18->737), 0 worsened. Pilots OK.

## Next
1. Batch next (rivi/kfvi/ravi leftovers, ~160-400 misses each): diagnose top miss families (kfRoti-guna? liT? san?) + Ridi onset R->n (tinanta mirror of krdanta meta) + Sasi M-num (SaMsate) — three candidate micro-rules, take ONE per iteration with survey.
2. Then: suppletive aja (avIvayata) / zwaBi / wunadi singletons (likely SKIP); ama-Satf leftovers (01.0536).
3. Re-sweep, rebuild STATS, overwrite this, commit & push.
