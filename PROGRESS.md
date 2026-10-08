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
- No other open questions; scope is locked as above.

## Search 100% session log (2026-10-08, for future LLMs — do not reinvent)
- Baseline sampled recall (seed 2, 80 fids = 8/gana, 8 tokens/fid = 640,
  `fid_expectations(do_engine=False)` + `analyze` + `check_exp`): 70%.
  Current after fixes below: 85.2%. Round-trips perfect throughout
  (tinanta slot+root 540/540, krdanta 185/185). 49 tests + lint green.
- Code (`pypanini/search.py`): `_yang_reverse` (tAtay->tay, beBrI->BrI,
  barIBar->Bar, lAlarb->larb, boBU->BU; long-A/e/o + arI/ar/aM/anI/alI redups,
  ya-strip, vowel-initial fallback) wired into `_krd_hits`, `_tinanta_analyze`
  (lookup/abhyasa/san branches, `via_extra` yang/yanluk 0.7), all
  `_infix_reverse` branches (luT/lfT/ASIrliN/ASI_VIDHI/ASI_ATM/luN/liT/
  periphrastic; yang outside `for _ab` loops — inside never fires when
  `_abhyasa_reverse` is []); `_deIr` (rI/ri/rU/ru/Ur/Ir->f), `_deApE`
  (Ap->E: styAp->styE for 01.1058), `_deSamInit` (U->va, I->ya:
  UcivAn->vac); `_sec_expand` (nijanta -aya-/-ay-, yak -ya-, -p- augment
  arp->ar->f) applied to luT/lfT/liT; confidence tuples extended with
  yang/yanluk; `_KVASU_AUX` += `AsuzI` (pozayAmAsuzI->puz);
  `_prefix_splits` saY/saN->sam (saYcikamp-, saNkamp-); `_emit` no longer
  forces parasmaipada (honors caller pada); `_SKIP_VERIFY` fast flag;
  `analyze_tin_krd()` (no subanta groups; note `_krdanta_flat` still needs
  `_subanta_flat` stems internally); CLI `main()` (`python -m
  pypanini.search WORD [--fast]`, tinanta/krdanta only); `_desatva`
  (z/S->s: zI->si) + `_YANG_ONSET` s/z/S twins (se- + zI- for si yang:
  sezIyamARam->si SAnac).
- Exports (`pypanini/__init__.py`): `analyze_tin_krd`.
- Audit (`tests/audit_search_full.py`): `positional_slots_list` m==18 pairs
  + m==19 pairs+ma.bahu-triple (fixes yak ASIrliN/luw walk-fallback:
  viprAyizIDvam->ma.bahu, GArizIzWAH->ma.eka); `audit_fid(..., fast)` +
  `--fast` (uses `analyze_tin_krd`, sets `_SKIP_VERIFY`).
- Proven fixes (verify before touching): tAtayyAt->tay ASIrliN/viDiliN,
  tAtayizIzwa->tay, barIBarati->Bf lw, lAlarbati->larb, beBrIyate->Bf,
  boBUyate->BU, nAwayitA->naw luw, arpayitAsmaH->f luw (low-ranked 0.35
  unverified, still a hit), SAkayitAsmi->Sak, styApayeta->styE,
  pozayAmAsuzI->puz, UcivAn->vac, saYcikampizitA/saNkampayeta hits,
  sezIyamARam->si SAnac (yang s/z + desatva); kvasu lit `_deEa` (e->a)
  + `_dental_n` D + `_deDeaspireInit` (B->b): beD/Band/Bant->banD
  (beDivAn, beDuzI, biBantsAmbaBUvAn); sam-san (`san`+dental->sam:
  sandehay-), yang velar onset (c/C/j + K/g/G: coKol->Kol), lookup-cache
  clear on ready (stale empty hits), ud-palatal coda (ucc-<-ud+c).
- Known gaps (fix next, do not re-diagnose): nich periphrastic liw
  (sandehayAmbaBUva-type Am+aux with sam), nich low/lw, yang_yak liw,
  san luw, yangluk laN/low; tavya/ac; yangluk non-lw ENGINE gap
  (tAtayyAt not generated; search emits unverified).
- Perf blocker (measured): `_ensure_ready` ~5s/process; fast analyze
  ~0.012-0.018s/surface (Bavati first call 4.6s incl. warmup); one big fid
  (01.0001, 29k unique surfaces) ~7min; full 2259-file audit = hours-days
  even with `--jobs 8`. Use per-gana SAMPLED audits for iteration, not full.
- Repro: `python -m pypanini.search Bavati --fast`;
  `python tests/audit_search_full.py --fid 01.0001 --fast --no-engine`
  (still slow — prefer sampled snippet in session); unit gate:
  `python -W ignore::ResourceWarning -m unittest discover -s tests -p
  "test_*.py"`.
- Commits this session: yang/nich/yak/kvasu fixes (231b6e6), Q&A doc
  (791d4ef), CLI+fast-audit (163adca), satva/yang-onset SAnac (653cc38),
  kvasu lit/deasp (c211253), sam-san/yang-velar/cache/ud (6f97e5e).
