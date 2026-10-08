# Progress — Done / Next (overwritten each iteration, not appended)

Date: 2026-10-07
Subanta: **21/21 (~2000 goldens)** — engine + audits + pipeline (see instructions.MD).
Search: **10/10 + round-trip perfect** — `pypanini/search.py` (subanta/krdanta/tinanta/analyze) + demo §4.
  Round-trips: tinanta slot 540/540 + root 540/540; krdanta 185/185 (was 539/172).
  Tests: test_subanta + test_subanta_full (GOLDENS–GOLDENS7) + test_krdanta_subanta pipeline.
Lint: **strict gate green** (`tests.test_lint` 2/2); F-class smells removed from helpers
  (test_dhatu dead accumulators, sweep_gana/sweep_upasargas_fast/test_gana05 unused imports).
  Engines stay grandfathered (tinanta ~1925 + krdanta ~1290 E501s, deliberate per test_lint.py).
Sweeps (unprefixed, regenerated 2026-10-07): **2229/2229 100% all ganas**
  (01:1156/1156, 02:76/76, 03:26/26, 04:161/161, 05:38/38,
  06:174/174, 07:25/25, 08:10/10, 09:71/71, 10:492/492; 30 skipped-dataless).
Sweeps (prefixed, regenerated 2026-10-07): **4860/4860 tasks,
  4146964/4146964 tokens 100%** (01:2198, 02:522, 03:198, 04:511, 05:140,
  06:501, 07:160, 08:67, 09:240, 10:323). Fid-diff vs HEAD: 150 up, 0 worsened.

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
- Scoring review (this turn): honest-scorer probe (unattested slots as misses)
  on 03/05/07/08 reads 98.9-99.2% vs 100% attested-only; gap is unattested data
  only, engine still generates the forms. Primary gate stays attested-only.
- Single-scan loader (this turn): new `pypanini/dhatu_meta.py` parses the ~2.3k
  JSONs once; both engines build entries verbatim from pre-parsed rows. Fresh-
  process startup ~10.2s -> ~5.2s; all four caches byte-identical (keys + order
  + values) vs pre-change pickle. Dropped now-unused `glob` imports.
- CI (this turn): `.github/workflows/ci.yml` runs lint gate + 49-test gate on
  push/PR (sweeps stay loop-driver: too slow for CI).
- JSON->analyze audit (this turn, 20 fids x ting/yak/san/nich/yang, 5220 forms):
  root+lakara 33.9% -> 38.2% (+d-twin endings et/d/tAd/yAd/luN-d, san twin
  emission incl. abhyasa-primary branch, sanadi-aware twin verify, t-twin
  verify fallback). Remainder: periphrastic multi-pada liT (design boundary)
  + per-root san/nich stem variety (open grammar work). Round-trips perfect.
- Triage: 10.0014/0105/0028/0021/0038/0242/0190 + 06.0159 all PASS live;
  04.0162/163 correctly skipped (0/0). Gana-04 full refresh: 161/161, fid-diff
  0/0 vs HEAD (perfect hold, CSV not rewritten).
- Subanta: `_infer_h_class` dedup, `_an_stem` dead-branch removal (behavior-identical).
- Krdanta: duplicate `sya-SAnac`/`sya-BAvakarma-SAnac` dict keys removed.
- Full gate green: lint 2/2 + search/subanta/krdanta/dhatu suites (43 + 4 tests) OK.

## Next
1. Loop driver: sweeps are freshly green (2026-10-07 refresh above); next engine
   change re-runs the same two commands + fid-diff gate before commit.
2. Gana-10 residuals + gana-04 ceiling audit per prior landscape (now unblocked:
   unprefixed already 100% in fresh CSVs; prefixed fails clear on live tree).
   Queued irregulars: sad Asad-suppletion (Asanna/Asatta/AsIda), ci-cap extras.
   Failed hypotheses, do not retry: (a) lyap pra+V sandhi twins; (b) tavya bare
   e-grade twins; (c) tumun/lyap jYAp twins; (d) san jYAp grade;
   (e) nich-Atmane ciY cayay-twin (0124 already passes). All zero-gain, reverted.
3. Cross-gana guards (01 + all-100% ganas) before every commit; PYTHONHASHSEED=0.

## Search 100% — user Q&A (2026-10-08, for future LLMs)
- Q: Which JSON should reach 100% search recall?
  A: All skt-morph-data (all 2259 JSONs).
- Q: Which JSON entries must search hit for 100%?
  A: All JSON tokens — every slash-split single-word token from
  conjugations + participles + upasarga_forms, as audit_search_full does.
- Q: What counts as search working on an entry?
  A: Provenance present — correct dhatu/fid + lakara/pratyaya +
  slot/upasarga present anywhere in analyze() groups (current audit rule).
- Q: How should results be delivered?
  A: Fix them (miss CSV); generally the CLI should deliver results to the
  end user as part of the grand plan. Ignore subanta search for now
  (tinanta/krdanta only).
