# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-07T00:00:00Z
Sweep: 580/1156 100% (raw 580/1166)

## Done
- Pure generative B/d D-devoicing in SAnac: B-final short-a/e -> C0+ip (`ripsamAnaH`; zmiN/guN R-keepers excluded by vowel gate); d-final -> devoice coda keep rest (`jihatsamAnaH`). yaBa/zada neutral (unscored); skandi/Sada bonus hits.
- Tinanta yak-luw plain-base alongside guna-forms (SunDitA/bukkitA/kUjitA): dataset survey of 1156 yak/alut fids — 1057 plain-itA, 0 guna, 99 sandhi-plain (teptA/kzantA/sedDA); zero conflicts. Sweep: 77 improved (+613 tokens), 0 worsened. Pilots OK.
- Krdanta yat-F short-num stem for i-final vowel-initial idit/Atmane roots (aNkyA/aRwyA/ambyA/fYjyA; M/N keep vriddhi cross-match): surveyed all 15 branch fids, zero conflicts. Sweep: 15 improved, 0 worsened. Pilots OK.
- Krdanta yat vriddhi for a + single non-nasal cons (aqa->Aqya, ata->Atya, aka->Akya; am/nasal-final, clusters, geminates, r-codas, u/i-finals stay short): surveyed 12 fids, zero conflicts. Sweep: 9 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN vowel-initial redup-aorist for a-initial roots (A+[num]+Ci+stem+ata): first attempt reverted (early-return skipped fallback); retry merges fallback. Sweep: 8 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN C-initial num-assimilated ay-less bases + R->n redup (sraki->sraNk, gaqi->gaRq; T->n, R->R append, v->n/R, h->M; i-final idit only): surveyed all 176 i-final-idit C-initial nich fids (long-A hrasva, f->a redup handled by over-gen). Re-sweep: `580/1156` held, 120 improved, 0 worsened. Pilots OK.

## Next
1. Batch next (krdanta yat of i-final parasmE num-R short stems, gap-3/4): 01.0068 (gaRqya M/F/N) — survey i-final parasmE roots expecting short yat (gaqi vs Aqya-class already fixed) dataset-wide first.
2. Then: suppletive aja (avIvayata) / zwaBi-tw / wunadi singletons (likely SKIP — no general shape); ama-Satf leftovers (01.0536).
3. Re-sweep, rebuild STATS, overwrite this, commit & push.
