# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-09-07T00:00:00Z
Sweep: 580/1156 100% (raw 580/1166)

## Done
- Pure generative B/d D-devoicing in SAnac: B-final short-a/e -> C0+ip (`ripsamAnaH`; zmiN/guN R-keepers excluded by vowel gate); d-final -> devoice coda keep rest (`jihatsamAnaH`). yaBa/zada neutral (unscored); skandi/Sada bonus hits.
- Tinanta yak-luw plain-base alongside guna-forms (SunDitA/bukkitA/kUjitA): dataset survey of 1156 yak/alut fids — 1057 plain-itA, 0 guna, 99 sandhi-plain (teptA/kzantA/sedDA); zero conflicts. Sweep: 77 improved (+613 tokens), 0 worsened. Pilots OK.
- Krdanta yat-F short-num stem for i-final vowel-initial idit/Atmane roots (aNkyA/aRwyA/ambyA/fYjyA; M/N keep vriddhi cross-match): surveyed all 15 branch fids, zero conflicts. Sweep: 15 improved, 0 worsened. Pilots OK.
- Krdanta yat vriddhi for a + single non-nasal cons (aqa->Aqya, ata->Atya, aka->Akya; am/nasal-final, clusters, geminates, r-codas, u/i-finals stay short): surveyed 12 fids, zero conflicts. Sweep: 9 improved, 0 worsened. Pilots OK.
- Tinanta nijanta-luN vowel-initial redup-aorist for a-initial roots (A+[num]+Ci+stem+ata: aRwiwata/ambibata/Acikata/Antitata; t-num, r-stem keep, nc-variant): surveyed all a-nich fids, suppletive aja excepted. FIRST attempt reverted (early-return skipped fallback, worsened 01.0063/01.0064/01.0262); retry merges fallback. Re-sweep: `580/1156` held (+4 perfect: 01.0247/01.0294/01.0438/01.0448; bonus 01.0215/01.0722/01.0998 0->9), 8 improved, 0 worsened. Pilots OK.

## Next
1. Batch next (consonant-initial nijanta-luN redup-aorist, gap-4/7): 01.0068 (ajagaRqata) / 01.0088 (asasraNkata) / 01.0089 / 01.0090 + scan `Ayayizwa` misses (119 fids share signature; pick 5-10 C-initial with num-stems). Diagnose why _nijanta_aorist misses sraki/gaqi (redup shape? num? endings?) — survey C-initial nich luN-eka expected dataset-wide first.
2. Then: gaqi-type i-final parasmE num-R short yat (01.0068 gaRqya M/F/N); suppletive aja (avIvayata) + ama-Satf leftovers.
3. Re-sweep, rebuild STATS, overwrite this, commit & push.
