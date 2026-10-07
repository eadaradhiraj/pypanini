# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-10-07
Subanta: **21/21 (~2000 goldens)** — engine + audits + pipeline (see instructions.MD).
Search: **10/10 + round-trip perfect** — `pypanini/search.py` (subanta/krdanta/tinanta/analyze) + demo §4.
  Round-trips: tinanta slot 540/540 + root 540/540; krdanta 185/185 (was 539/172).
  Tests: test_subanta + test_subanta_full (GOLDENS–GOLDENS7) + test_krdanta_subanta pipeline.
Lint: **strict gate green** (`tests.test_lint` 2/2); F-class smells removed from helpers
  (test_dhatu dead accumulators, sweep_gana/sweep_upasargas_fast/test_gana05 unused imports).
  Engines stay grandfathered (tinanta ~1925 + krdanta ~1290 E501s, deliberate per test_lint.py).
Sweeps (unprefixed, tests/sweep_*_fresh.csv 2026-10-06): **100% all ganas**
  (01:1156/1156, 02:76/76, 03:26/26, 04:161/161, 05:38/38,
  06:174/174, 07:25/25, 08:10/10, 09:71/71, 10:492/492).
Sweeps (prefixed): fresh CSVs (10/6) show 150 fails in 04–10; **all 150 pass
  on live tree** (revalidated 2026-10-07 via sweep_upasargas_fast --tasks,
  Total: 126178/126178 100.00%) + 32/32 pass-sample green, 0 regressions.
  Prefixed CSVs are stale — full refresh queued for the loop driver (not run here;
  full prefixed-01 alone exceeds 10 min; LOOP.md hygiene: one driver only).

## Done — this session (cleanup + determinism + search, zero behavior drift in scoring)
- ResourceWarning fixes: `json.load(open(...))` → `with open(...)` in tinanta/krdanta
  caches, test_dhatu, sweep_gana, sweep_upasargas_fast, test_search, test_gana05.
- Determinism: `list(set(...))` (11×, tinanta) → `list(dict.fromkeys(...))`;
  set-iteration sorted; per-gana `sorted(glob(...))` keeping 01-last-wins
  (global sort broke BU-homonym kta: `BUtaH` vs `['BUtaH','BAvitaH']` — caught, reverted).
- Perf: single `_derive_inner` call in `derive()` (was 2×); class-level shared
  dhatu caches; `_LOOKUP_CACHE` in search.
- Search correctness: luN `adAm` vowel-restoration + longest-first suffixes;
  abhyasta `ati` 3pl ending (dadati) + twin emission; sya path skips `ati`.
  Round-trip: slot 540/540 (was 539/540), root 526/540.
- Search depth (this turn): `-ending core fix (gama->gam); viDiliN e-grade
  fallback det->dA (single-consonant core + A-root); liw_plain twin emission
  (dadaTuH->dA); lyuw -aRa twin (vidaRa->vid); Ramul -am handler (todam->tud);
  prefixless-lyap hypothesis (BUya->BU, 0.45 + prefix-missing note).
  Round-trips now perfect: tinanta root 540/540, krdanta 185/185. Analyzer-only,
  zero generation impact.
- Perf: startup cache-load ~10s/process (2 x 5s JSON scans) dominates; derive +
  analyze are microseconds warm. Single-scan shared loader queued (halves startup).
- Engine perf (this turn): profiled at sweep scale — generation is ~30us/derive;
  the real hotspot is `apply_natva_prefix_aware` (13k calls, 28% of prefixed-task
  time). Hoisted constants (`_NATVA_VAN_IDS`, `_NATVA_ALLOWED`, prefix pairs,
  root-start tuples) + cheap `in`-gates: hotspot tottime 0.157s -> 0.076s (2x),
  byte-identical output over 1367 prefixed forms. All 49 tests green.
- Triage: 10.0014/0105/0028/0021/0038/0242/0190 + 06.0159 all PASS live;
  04.0162/163 correctly skipped (0/0). Gana-04 full refresh: 161/161, fid-diff
  0/0 vs HEAD (perfect hold, CSV not rewritten).
- Subanta: `_infer_h_class` dedup, `_an_stem` dead-branch removal (behavior-identical).
- Krdanta: duplicate `sya-SAnac`/`sya-BAvakarma-SAnac` dict keys removed.
- Full gate green: lint 2/2 + search/subanta/krdanta/dhatu suites (43 + 4 tests) OK.

## Next
1. Loop driver: full unprefixed + prefixed CSV refresh (all ganas) + fid-diff gate
   vs HEAD; rebuild STATS.md numbers from that sweep output only.
2. Gana-10 residuals + gana-04 ceiling audit per prior landscape (now unblocked:
   unprefixed already 100% in fresh CSVs; prefixed fails clear on live tree).
   Queued irregulars: sad Asad-suppletion (Asanna/Asatta/AsIda), ci-cap extras.
   Failed hypotheses, do not retry: (a) lyap pra+V sandhi twins; (b) tavya bare
   e-grade twins; (c) tumun/lyap jYAp twins; (d) san jYAp grade;
   (e) nich-Atmane ciY cayay-twin (0124 already passes). All zero-gain, reverted.
3. Cross-gana guards (01 + all-100% ganas) before every commit; PYTHONHASHSEED=0.
