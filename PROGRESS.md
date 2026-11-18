# pypanini — Progress & Handoff

> **Read this first if you are resuming work in a new session.**
> This file is the single source of truth for project state, decisions, architecture,
> and the exact next steps. Update it at the end of every working session.

---

## 1. What this project is

A **fresh, pure-TypeScript / Node.js reimplementation** of the subset of
[ashtadhyayi.com](https://ashtadhyayi.com) that the user cares about. It is **not** a
port of any existing codebase (no Rust, no Python, no PAIAS). Everything is written
from scratch in TypeScript.

### Target scope (from the user, confirmed 2026-11-17)

| Feature | Wanted | Priority |
|---|---|---|
| Dhātu → **Tiṅanta** | yes | core |
| **Kṛdanta** with **kartari** prayoga | yes | core |
| **Kṛdanta** with **karmani** prayoga | yes | core |
| **Saṇādi** pratyayas: **ṇic, yaṅ, yāṅ, yaṅluk** | yes | core |
| **Subanta** formation | yes | core |
| **Reverse declension** (declined word → base + case/number) | yes (added 2026-11-17) | core |
| Samāsa, taddhita, accent, other prayogas/lakāras | no | ignore for now |

### Hard requirements (confirmed)

- **Language/runtime:** pure TypeScript, runs on Node.js. No foreign bindings.
- **Deliverables:** (a) importable Node library, (b) CLI tool.
- **Encoding:** **SLP1** for all input and output.
- **Output:** final word forms **plus a prakriyā trace** (list of applied sūtra codes with
  intermediate term states), like ashtadhyayi.com shows.
- **Resumability:** progress must be recorded in this file so another session can resume.

### Terminology check (confirmed)

"nich / yan / yang / yangluk" = the **saṇādi pratyayas** ṇिच्, यङ्, याङ्, यङ्लुक् that
are attached to a dhātu before the tiṅ/kṛt suffix (causative, intensive, etc.). In our
code these are the `Sanadi` enum values `Nic`, `Yan`, `Yang`, `YangLuk`.

---

## 2. Key references gathered

- **SLP1 mapping** (Wikipedia / Sanskrit Library):
  - Vowels: `a A i I u U f F x X e E o O`; anusvāra `M`, visarga `H`, avagraha `'`, anunāsika `~`.
  - Velar `k K g G N`, palatal `c C j J Y`, retroflex `w W q Q R`, dental `t T d D n`,
    labial `p P b B m`, semivowels `y r l v`, fricatives `S z s h`, `L` (ḷ).
  - e.g. भू = `BU`, भवति = `Bavati`, कर्तृ = `kartf` (f = ऋ).
- **Reference derivation of भवति** (Vidyut trace + classical sources), used as the golden
  test for the engine:
  ```
  BU
  BU + la~w       (3.2.123)
  BU + l          (1.3.9)
  BU + tip        (3.4.78)
  BU + ti         (1.3.9)
  BU + Sap + ti   (3.1.68)
  BU + a + ti     (1.3.9)
  Bo + a + ti     (7.3.84 guṇa)
  Bav + a + ti    (6.1.78 o+a → av+a)
  Bavati          (8.4.68 / concatenation)
  ```
- **Past-tense stem lengthening:** 7.3.101 `ato dīrgho yañi` — final `a` → `ā` before a
  sārvadhātuka affix beginning with `v` or `m` (bhavāmi, bhavāvaḥ, bhavāmaḥ).
- **`a + a → a` and `a + e → e`** at the vikaraṇa/suffix boundary (needed for बवन्ति
  `Bavanti` / पच्येते `pacyete`, not `*Bavaanti`); implemented with a TODO-marked code
  `6.1.104` in `TINANTA_TAIL_RULES`.
- **Saṇādi / intensive (resolved with user):** `yan` was a typo; `yang` = yaṅ (thematic,
  -ya-, ātmanepada), `yangluk` = yaṅluk (ya elided by 2.4.74, parasmaipada).
  - 3.1.22 `kriyāsamabhihāre yaṅ`, 6.1.9 `san-yaṅoḥ` (reduplication),
    7.4.82 `guṇo yaṅ-lukoḥ`, 7.4.83 `dīrgho 'kitaḥ`, 7.3.94 `yaṅo vā` (optional ī).
  - Golden forms: `BU`+yaṅ → `BoBUyate` (bobhūyate), `pac`+yaṅ → `pApacyate`,
    `BU`+yaṅluk → `BoBavIti`, `pac`+yaṅluk → `pApacIti`, `kf`+yaṅ → `cekrIyate`,
    `kf`+yaṅluk → `cakArti`. Vidyut's `Sanadi` enum confirms only `yaN` and `yaNluk`
    exist (no distinct yāṅ); docs.rs was used as oracle.
- **Kṛdanta sūtras:** 3.1.95 `kṛtyāḥ`, 3.1.96 `tavyattavyānīyaraḥ`,
  7.2.10 `ekāca upadeśe'nudāttāt` (no iṭ for kṛ), 7.2.35 (iṭ after u-final roots).
  Golden forms for `kf`: `kfta`, `kartf`, `kurvat`, `karaRIya`, `kartum`,
  `kartavya`, `karaRa`, `kftvA`, `kAraka`. For `BU`: `Bavitum`, `Bavitavya`, `Bavat`,
  `Bavaka`, `Bavana`.
- **Alternative engine already in existence (NOT used, for reference only):**
  `vidyut-prakriya` (Rust, Ambuda) with a Python package `vidyut`; PAIAS (pure Python).
  Useful as an oracle for expected forms, but we are deliberately building fresh.

---

## 3. Architecture / file map

```
pypanini/
├── PROGRESS.md          ← this file
├── README.md            ← usage + roadmap
├── package.json
├── tsconfig.json
├── src/
│   ├── index.ts         ← public library API
│   ├── cli.ts           ← CLI entrypoint
│   ├── core/
│   │   ├── slp1.ts      ← SLP1 char tables + phonological helpers (guṇa, vṛddhi, …)
│   │   ├── types.ts     ← enums (Lakara, Prayoga, Purusha, Vacana, Gana, Sanadi, …)
│   │   ├── prakriya.ts  ← Term/Step model, Prakriya class (terms + history)
│   │   ├── engine.ts    ← Vyakarana facade + rule-pipeline runner
│   │   └── rules.ts     ← reusable rule primitives / helpers
│   ├── data/
│   │   └── dhatupatha.ts← small curated Dhātupāṭha (SLP1) + lookup
│   ├── tinanta.ts       ← tiṅanta derivation (kartari parasmai lat = golden path)
│   ├── krdanta.ts       ← kṛdanta derivation (kartari/karmani scaffolding)
│   ├── subanta.ts       ← subanta derivation (a-stem tables + sandhi)
│   ├── analyze.ts       ← REVERSE declension: declined word → base + case/number
│   └── sanadi.ts        ← ṇic + yaṅ/yaṅluk (single source of truth for saṇādi)
└── test/
    └── *.test.ts
```

### Design principles
1. **Prakriya = ordered terms + history.** A derivation is a list of SLP1 `Term`s and a
   list of `Step`s (`{rule, result}`). Every rule that fires records a step.
2. **Rules are data + small transform functions**, applied in a deterministic pipeline.
   This is a *linear* pipeline approximation of Pāṇini — it does **not** yet implement
   `siddha`/`asiddha`, `antaranga`/`bahiranga`, or full conflict resolution. That is a
   known limitation (see §6).
3. **Terms carry tags** (e.g. `sārvadhātuka`, `dhātu`) so rules can be conditioned on
   grammatical metadata, not just surface strings.

---

## 4. Current status (as of this writing)

- [x] Project scaffolded: `package.json`, `tsconfig.json`, `README.md`, this file.
- [x] SLP1 tables + phonological helpers implemented (`src/core/slp1.ts`).
- [x] Core types implemented (`src/core/types.ts`).
- [x] Prakriya model implemented (`src/core/prakriya.ts`).
- [x] Rule pipeline + `Vyakarana` facade (`src/core/engine.ts`, `src/core/rules.ts`).
- [x] **Full MIT Dhātupāṭha** — 2,229 roots (`src/data/dhatupatha.full.ts`), sourced
      from ashtadhyayi.com via vidyut (MIT), with gana + artha; loader in
      `src/data/dhatupatha.ts` including `findDhatus` and `searchDhatus`.
- [x] **Full Sūtrapaṭha** — all 3,984 Aṣṭādhyāyī sūtras in SLP1
      (`src/data/sutras.ts`), used for trace labels and namespace audits.
- [x] **Golden path working:** `bhū` → all 9 lat/kartari/parasmai forms with full trace.
- [x] **All major lakāras:** `lat, lit, lut, lrt, lot, lan, lng, lin` with distinct
      golden 3s forms for bhū: `Bavati, baBUva, BavitA, Bavizyati, Bavatu, aBavat,
      aBavizyat, Bavet`. Vedic `leṭ` removed (classical-only scope).
- [x] **Sūtra-code audit:** all TODO markers removed from trace labels. Codes verified
      against the bundled Sūtrapaṭha (e.g. tumun = 3.3.10 not 3.10.10, lyuṭ = 3.3.115,
      ekādeśa = 6.1.84, śatṛ/śānac = 3.2.124, ṇvul/tṛc = 3.1.133).
- [x] Basic **karmani** passive (`pac` → `pacyate`) via the `yak` → `ya` vikaraṇa.
- [x] **Saṇādi** in `src/sanadi.ts`: ṇic causative (`bhū` → `BAvayati`),
      yaṅ/yaṅ alias (`bhū` → `BoBUyate`, `pac` → `pApacyate`),
      yaṅluk (`bhū` → `BoBavIti`, `pac` → `pApacIti`). Used by both tinanta and krdanta.
- [x] Library exports (`src/index.ts`) and CLI (`src/cli.ts`).
- [x] Tests (**47 total** across `core.test.ts`, `scheduler.test.ts`,
      `invisibility.test.ts`) — all passing (`npm test`).
- [x] Karmani prayoga — 9-form ātmane paradigm verified (`pac` → `pacyate … pacyAmAhe`).
- [x] Saṇādi — yaṅ/yaṅluk golden forms verified for BU, pac and kf (including the
      irregular ṛ-final intensive stems) AND the desiderative `san` (3.1.7):
  `BU` → `buBUzati`, `pac` → `pipakzati`, `kf` → `cikIzati`, `gam` → `jigamizati`.
      yaṅluk beyond 3rd singular remains unaudited.
- [x] Kṛdanta — **eighteen kṛt suffixes** (`tac, tfc, satr, ani, tum, tavya, lyuT,
      ktvA, nvul, ktavatu, sanaC, yat, ktin, Nini, Sanan, STran, TRn, Kyap`) with root-dependent allomorphs (ṛ-final vs
      u-final), iṭ handling, and śatṛ/śānac overrides (`kurvat`/`kurvARa`);
      golden paradigms for kf and BU verified. Sūtra codes audited.
- [x] Subanta — **thirteen stem classes**: a- (m/n), i- (m/n), u- (m/n), ā- (f),
      ī- (f), u- (f), and consonant stems -as (n), -an (m), -at (m), -ṛ (m);
      all 24 forms each, with `a + vowel` ekādeśa sandhi where applicable.
- [x] Reverse declension (`src/analyze.ts`, CLI `analyze` + `--declension` flag)
      across all thirteen classes: `WrampaH` → `Wramp`, `agniBiH` → `agni`,
      `sItayA` → `sItA`, `guravaH` → `guru`, `nadyaH` → `nadI`, `manasi` → `manas`,
      `DenUnAm` → `Denu`, `rAjYA` → `rAjan`, `pitfzu` → `pitf`.
      Verified by round-trip re-synthesis.
- [ ] A few rare consonant stems (s-/r- masculine, etc.) are not modelled. Ambiguous results
      are ranked by longest ending, then vibhakti, then shortest prātipadika.
- [x] Vedic `leṭ` **removed** per user request — classical only.
- [x] Nāmādhatu (denominatives) implemented for Pāṇini 3.1.8–3.1.21 core pratyayas:
      kyac (`putrIyati`), kāmyac (`putrakAmyati`), kyaṅ (`SyenAyate`), ṇic (`putrayati`).
- [x] Upasargas (prefixes): full 1.4.58 list of 19, saṃjñā 1.4.59, gati 1.4.60,
      8.4.14 ṇatva AND 8.3.65 ṣatva for the 12 listed roots (su, stu, sthā, sic,
      sañj, …). `--upasarga <s>` on the CLI: `pra` + `BU` → `praBavati`,
      `pra` + `nam` → `praRamati`, `aBi` + `su` → `aBizavati` (root → `zu`).
- [x] Additional nāmādhatu pratyayas added: 3.1.12 bhū-vyac, 3.1.13 kyaz,
      3.1.14 kaṣṭāya kyaṅ (`kazwAyate`), 3.1.15 varticara (`romAyate`),
      3.1.16 udvamana (`bAzpAyate`), 3.1.17 karaṇe kyaṅ (`SabdAyate`),
      3.1.18 sukhādibhyaḥ kyaṅ (`suKAyate`), 3.1.19 kyac-nama (`namasyati`), 3.1.20 ṇiṅ (`pucCayate`).
- [x] Ātmanepada endings audited and corrected: lat 1d/1p `BavAvahe`/`BavAmahe`,
      lit 2s/2p/1d `baBUvise`/`baBUvaDve`/`baBUvahe`. (Earlier forms had extra long ā.)
- [x] Upasarga 8.2.19 r→l before ayati: `parA`+`ay` → `palAyate`,
      `pari`+`ay` → `palyayate` (prefix/root vowel coalescence 6.1.77/6.1.84).
      8.3.34 (visarjanīyasya saḥ) is external samhitā sandhi — out of scope.
- [x] CLI `sutras --code` / `sutras --search` query all 3,984 sūtras.
- [x] Rare consonant stems: -an neuter (`nAma`, `nAmAni`, `nAmnA`) and -at neuter
      (`Bavanti`, `Bavatsu`). 15 stem classes total.
- [x] Luṭ (periphrastic future) audited: 2d/2p `BavitAsTaH`/`BavitAsTa` (were wrong),
      ātmane 2s/1p `BavitAse`/`BavitAmahe`. Laṅ/Lṛṅ ātmane 1d/1p dīrgha fixed:
      `aBavAvahi`/`aBavAmahe`, `aBavizyAvahi`/`aBavizyAmahe`.

> Legend: `[x]` = implemented and tested, `[ ]` = stub / future work.

---

## 5. How to verify the current build

```bash
cd /home/edhiraj/Documents/projs/pypanini
npm install
npm test
npm run cli -- tinanta --dhatu BU --lakara lat
npm run cli -- tinanta --dhatu BU --lakara lat --trace
npm run cli -- analyze --word WrampaH
npm run cli -- analyze --word WrampeNa
npm run cli -- tinanta --dhatu BU --sanadi yan
npm run cli -- tinanta --dhatu pac --sanadi yangLuk
```

Expected (no `--trace`): the nine present forms of bhū, SLP1, one per line.
Expected (with `--trace`): each form followed by its rule-by-rule derivation.

---

## 6. Known limitations / design debt (important for the next session)

1. **Rule ordering now uses a real scheduler.** `src/core/scheduler.ts` gives rules
   `when` conditions, numeric priority, `antaranga`/`bahiranga` strength, and
   `siddha`/`asiddha` phases derived from the sūtra code (8.2.1 `pūrvatrāsiddham`).
   `runTinantaPipeline` runs through it; e.g. visarga (8.3.15) and consolidation
   (8.4.68) now correctly fire in the asiddha phase. Full `asiddhakāṇḍa` fidelity
   (rules being invisible to earlier rules in both directions) is still future work.
2. **Hard-coded suffix tables.** Tiṅ suffixes are encoded per (puruṣa, vacana, pada) for
   `lat`. All major lakāras now have tables, but ātmanepada forms are unverified.
3. **`la~w` label** is kept as the ashtadhyayi.com-style SLP1 label for लट्. Other lakāra
   labels now exist for all major lakāras (`la~w`, `liw`, `luw`, `lfw`, `low`, `laN`,
   `lfN`, `liN`); Vedic `let` still reuses `lat`.
4. **It-lopa / sandhi** are currently implemented as explicit per-suffix steps rather
   than generic rules driven by `it` markers.
5. **Accuracy.** The trace is modelled on the Vidyut/ashtadhyayi.com derivation. Rule
   codes for steps we are unsure about are marked `TODO` in source comments. Audit
   against ashtadhyayi.com before claiming fidelity.

---

## 7. Next steps (ordered — pick up here)

1. ~~Verify `npm test` passes; fix any type/build errors.~~ **DONE (9→11 tests).**
2. ~~Extend `tinanta.ts` to ātmanepada + karmani with the `ya` vikaraṇa.~~ **DONE**
   (karmani 9-form paradigm verified via round-trip).
3. ~~Implement yaṅ / yaṅluk with reduplication + iṭ rules.~~ **DONE** including
   the ṛ-final root `kf`. Remaining: audit yaṅluk beyond 3s and ṇic vṛddhi details.
4. ~~Extend kṛdanta to nine kṛt suffixes.~~ **DONE**; remaining: audit TODO sūtra codes.
5. ~~Extend subanta to i-, u-, feminine and consonant stems.~~ **DONE** (13 classes).
   Remaining: rare consonant stems only.
6. ~~Extend reverse declension beyond a-stems.~~ **DONE** across all 13 classes.
   Remaining: optional context-based disambiguation if the user wants it.
7. ~~Add more lakāras.~~ **DONE** (`lat, lit, lut, lrt, lot, lan, lng, lin`).
   Vedic `leṭ` removed per user request (classical-only scope).
8. **Broaden coverage to all sūtras on subanta, kṛdanta, tiṅanta, nāmādhatu, and
   upasargas** (user's current directive): full root/sūtra data loaded; remaining
   namādhatu pratyayas, more upasarga sandhi rules, more kṛt suffixes, rare
   consonant stems, ātmanepada auditing.
9. ~~Audit all TODO-marked sūtra codes using the local Sūtrapaṭha.~~ **DONE.**
10. ~~Replace the linear pipeline with a condition-based rule scheduler.~~ **DONE**
    (`src/core/scheduler.ts`); remaining: full asiddhakāṇḍa invisibility semantics.
11. Keep this `PROGRESS.md` updated after each session.

---

## 8. Session log

- **2026-11-17 — Session 1:** Clarified requirements with the user (TypeScript, CLI+library,
  SLP1, traces, resumable progress). Gathered SLP1 table and reference derivations.
  Scaffolded the project and implemented the core engine (Prakriya model, rule pipeline,
  Dhātupāṭha), golden tiṅanta path, basic karmani/ṇic/kṛdanta/subanta, library exports,
  CLI, and 9 tests. `npm test` passes (9/9). `node dist/src/cli.js tinanta --dhatu BU
  --purusha prathama --vacana eka --trace` reproduces the reference derivation.
- **2026-11-17 — Session 2:** User requested reverse declension (declined SLP1 word →
  base + case/number), with a CLI declension flag. Added `src/analyze.ts` (enumerate
  a-stem endings → propose stem → verify by re-synthesis). Fixed a bug in masculine
  a-stem generation (`rAmaH`, not `*rAmH`) and the vowel coalescence sandhi. Added CLI
  `analyze` command plus `--analyze` / `--declension` flag on `subanta`, with tolerance
  for `N` written where strict SLP1 uses `n`/`R`. Tests now 11/11 passing.
  `analyze --word WrampaH` → base `Wramp`, nominative singular; `analyze --word
  WrampeNa` → base `Wramp`, instrumental singular. Next: see §7 step 3 (saṇādi).
- **2026-11-17 — Session 3:** User confirmed `yan` was a typo and `yang` = yaṅ.
  Researched Pāṇini 3.1.22 / 2.4.74 / 6.1.9 / 7.4.82–83 / 7.3.94 and used Vidyut's
  `Sanadi` enum as an oracle. Rewrote `src/sanadi.ts` as the single source of truth
  for saṇādi (`buildSanadiStem`, `heavyReduplicate`), wired it into tiṅanta and
  kṛdanta, and fixed the CLI pada label for intensive forms. Added 3 tests.
  `npm test` passes (14/14). Golden intensive forms: `BoBUyate`, `pApacyate`,
  `BoBavIti`, `pApacIti`. Next: see §7 step 3 remainder (yaṅluk breadth, ṛ-final roots).
- **2026-11-17 — Session 4 (continued):** Implemented irregular ṛ-final intensive
  stems (`kf` → `cekrIyate` / `cakArti`). Rewrote `src/krdanta.ts` with a nine-entry
  kṛt table, root-dependent allomorphs (ṇa vs na, ṛ vs u grading), iṭ handling for
  u-final roots, and śatṛ override for kṛ (`kurvat`). Added 3 tests. `npm test`
  passes (17/17). Next: see §7 step 5 (subanta i-/u-/consonant stems + feminine).
- **2026-11-17 — Session 5 (continued):** Generalised `src/subanta.ts` into a
  `STEM_CLASSES` table (a-/i-/u- masculine & neuter, ā-/ī- feminine), rewrote
  `src/analyze.ts` to enumerate all classes with round-trip verification, and added
  ranking by vibhakti then shortest prātipadika. Exported `STEM_CLASSES`/`classFor`.
  Added 2 tests. `npm test` passes (19/19). Golden forms: `agniBiH`, `guravaH`,
  `sItayA`, `nadyaH`, `vArIRi`. Next: see §7 steps 5–6 remainder (consonant stems,
  feminine u-stems).
- **2026-11-17 — Session 6 (continued):** Added feminine u-stem (`Denu` → `DenuH`,
  `DenvA`, `DenUnAm`) and -as neuter consonant stem (`manas` → `manasi`, `manAMsi`,
  `manoBiH`) to `STEM_CLASSES`. Fixed reverse-declension reconstruction for sandhi
  classes (rebuild base before re-attaching terminal) and changed ranking to prefer
  the longest matching ending. Added 1 test. `npm test` passes (20/20). Next: other
  consonant stems, then other lakāras / sūtra-code audit.
- **2026-11-17 — Session 7 (continued):** Added three consonant stem classes:
  -an masculine (`rAjan` → `rAjA`, `rAjYA`, `rAjYAm`), -at masculine present
  participle (`Bavat` → `Bavantam`, `BavadBiH`, `Bavatsu`), -ṛ masculine
  (`pitf` → `pitA`, `pitrIRAm`, `pitfzu`). Extended reverse declension to all
  13 classes. Added 1 test. `npm test` passes (21/21).
  **Original requested scope is now complete.** Remaining work is optional:
  rare consonant stems, other lakāras (only `lat` exists), sūtra-code audit,
  and the condition-based rule scheduler.
- **2026-11-17 — Session 8 (continued):** User switched priority from the sūtra-code
  audit to **all lakāras** (also asked for one-line explanations of the audit and the
  rule-scheduler option, given in chat). Added per-lakāra config tables in `tinanta.ts`
  with augments (`a` for laṅ/lṛṅ), iṭ for futures, vikaraṇa variants, liṭ reduplication,
  and imperative/imperfect/perfect/future/optative suffix tables. Added CLI aliases
  `lot` and `lng`. Golden 3s forms for bhū now distinct across 8 lakāras.
  `npm test` passes (22/22). Next: §7 steps 8–9 (sūtra-code audit, rule scheduler).
- **2026-11-17 — Session 9 (scope change):** User restricted scope to **classical
  Sanskrit only** — all sūtras on subanta, kṛdanta, tiṅanta, nāmādhatu — and asked
  for the full MIT Dhātupāṭha, Pāṇinian denominatives, and removal of Vedic `leṭ`.
  Downloaded and embedded the full 2,229-root Dhātupāṭha and all 3,984 sūtras as
  MIT-licensed data modules; added `findDhatus`/`searchDhatus`, a `dhatus --search`
  CLI, `namadhatu.ts` with kyac/kāmyac/kyaṅ/ṇic (3.1.8–3.1.21), and removed `leṭ`.
  Golden forms: `putrIyati`, `putrakAmyati`, `SyenAyate`, `putrayati`.
  `npm test` passes (24/24). Next: §7 step 8 (broaden remaining pratyayas).
- **2026-11-17 — Session 10 (continued):** User added upasargas (prefixes) to the
  focus list. Extracted the 43 upasarga/gati-related sūtras from the local Sūtrapaṭha,
  implemented `src/upasarga.ts` with the 1.4.58 list (19 prefixes), 1.4.59/1.4.60
  saṃjñā, and 8.4.14 ṇatva. Added `--upasarga` to the tiṅanta CLI and wired it into
  `deriveTinantas`. Golden forms: `praBavati`, `praRamati`. Added 1 test.
  `npm test` passes (25/25). Next: §7 step 8 (remaining upasarga sandhi + pratyayas).
- **2026-11-17 — Session 11 (continued):** User said "yes" to continuing. Audited all
  TODO trace codes against the bundled Sūtrapaṭha and corrected them (tumun 3.3.10,
  lyuṭ 3.3.115, ekādeśa 6.1.84, śatṛ/śānac 3.2.124, ṇvul 3.1.133, etc.) — zero
  TODO markers remain. Added three kṛt suffixes (ktavatu, śānac, yat) with
  root-dependent allomorphs; golden forms `kftavAn`, `kurvARa`, `kArya`, `Bavya`,
  `BavamAna`. Added 1 test. `npm test` passes (26/26).
  Next: §7 step 8 (remaining namādhatu pratyayas / upasarga sandhi).
- **2026-11-17 — Session 12 (continued):** User said "yes" again. Added 8.3.65 ṣatva
  for the 12 listed roots (`aBi`+`su` → root `zu`), added five more denominative
  pratyayas (3.1.12/13/14/17/18) sharing the kyaṅ āya formation (`kazwAyate`,
  `lohitAyate`). Tests still 26/26. Next: §7 step 8 remainder, then the rule
  scheduler refactor.
- **2026-11-17 — Session 13 (continued):** User said "keep going". Implemented the
  condition-based rule scheduler (`src/core/scheduler.ts`): rules carry `when`
  conditions, priority, antaranga/bahiranga strength, and a siddha/asiddha phase
  derived from the sūtra number (8.2.1+ = asiddha). Refactored `runTinantaPipeline`
  to use it — all 26 existing tests still pass, and traces now show visarga (8.3.15)
  and consolidation (8.4.68) in the asiddha phase. Added 2 scheduler tests and
  public exports. `npm test` passes (28/28).
  Next: §7 step 8 remainder (denominatives / rarer sandhi).
- **2026-11-17 — Session 14 (continued):** User said "continue". Audited ātmanepada
  endings and corrected lat 1d/1p (`BavAvahe`/`BavAmahe`) and lit 2s/2p/1d
  (`baBUvise`/`baBUvaDve`/`baBUvahe`); added the 3.1.15/16/19 denominatives
  (`romAyate`, `bAzpAyate`, `namasyati`). Added 1 test. `npm test` passes (29/29).
  Next: §7 step 8 remainder (3.1.20, rarer upasarga sandhi).
- **2026-11-17 — Session 15 (continued):** User said "keep going". Added 3.1.20 ṇiṅ
  denominative (`pucCayate`), 8.2.19 r→l before ayati (`palAyate`, `palyayate`) with
  prefix/root vowel coalescence (6.1.77/6.1.84), and a CLI `sutras` lookup command.
  `npm test` passes (29/29). Next: fuller non-lat ātmanepada auditing.

- **2026-11-17 — Session 16 (continued):** User said "keepgoing". Audited luṭ
  (periphrastic future) parasmai + ātmane and fixed 2nd-person forms; fixed laṅ/lṛṅ
  ātmane 1st-person dīrgha (7.3.101). Added 2 tests. `npm test` passes (31/31).
  Remaining: full asiddhakāṇḍa invisibility semantics; rare consonant stems.

- **2026-11-17 — Session 17 (continued):** User said "keep going". Added -an neuter
  and -at neuter consonant stem classes (15 total) with golden forms `nAma`,
  `nAmAni`, `nAmnA`, `Bavanti`, `Bavatsu`. Extended the scheduler with an `asiddhavat`
  phase (6.1.2–6.1.7) and phaseRank ordering. Added tests. `npm test` passes (32/32).
  Remaining: the tiṅanta rules currently check conditions inside `apply` rather than
  via `when` — DONE. Phases now use snapshots so asiddha `when`-conditions see
  the phase-entry state.

- **2026-11-17 — Session 18 (continued):** User said "keep going". Implemented
  full mutual-invisibility infrastructure in `RuleScheduler`: `withSnapshots()`
  with `SnapshotHooks` evaluates `when`-conditions against the phase-entry state
  while mutations accumulate against the live state. Added 2 tests in a new
  `invisibility.test.ts` proving asiddhavat rules ignore sibling effects and that
  non-snapshot mode still sees accumulated state. `npm test` passes (34/34).

- **2026-11-17 — Session 19 (continued):** User said "keep going". Refactored the
  tiṅanta rules to separate conditions (`when`) from mutations (`apply`), added
  `Prakriya.snapshot()/restore()` (in-place, preserving object identity), and wired
  `withSnapshots()` into `runTinantaPipeline`. The golden bhū trace is byte-for-byte
  unchanged; added an exact-trace regression test. `npm test` passes (35/35).
  The condition/mutation architecture is now in place for full asiddha invisibility.

- **2026-11-17 — Session 20 (continued):** User said "keep going". Closed the
  desiderative gap: implemented `san` (3.1.7) in `sanadi.ts` with reduplication
  (6.1.9), special reduplicate changes (7.4.79), and the ṣ of the pratyaya
  (8.2.36/41), plus a generic fallback for unknown roots. Golden forms
  `buBUzati`, `pipakzati`, `cikIzati`, `jigamizati`. Added 1 test.
  `npm test` passes (36/36).

- **2026-11-17 — Session 21 (continued):** User said "keep going" (typo "jeep").
  Added kṛt suffix ktin (3.3.94, feminine -ti): `kf`→`kfti`, `stu`→`stuti`,
  `ci`→`citi`, `pac`→`pakti`. Implemented 8.2.30 (jhalo jhali: palatal → guttural
  before a consonant-initial kṛt suffix), verified against all 13 kṛt suffixes.
  Added 1 test. `npm test` passes (37/37).

- **2026-11-17 — Session 22 (continued):** User said "keep going". Ran a bulk smoke
  test: all 2,229 Dhātupāṭha roots across 8 lakāras × 2 padas (35,664 derivations,
  0 failures) plus saṇādi combinations. Made `deriveTinantas` return `[]` (instead of
  throwing) for yaṅ on non-monomorphic/initial-vowel roots, per Pāṇini 3.1.22.
  Locked both in with 2 tests. `npm test` passes (39/39).

- **2026-11-17 — Session 23 (continued):** User said "keep going". Implemented the
  aorist (luN, 3.2.110) in `src/aorist.ts` for the three most common Classical
  varieties: root aorist (`bhū` → `aBUt`/`aBUvan`), a-aorist (`pac` → `apacat`,
  `sic` → `asicat`), and s/iṣ-aorist (`nī` → `anEzIt`, `budh` → `aboDizIt`).
  Replaced the `LatN` placeholder; dispatched from `deriveTinantas`. Added 1 test.
  `npm test` passes (40/40). The other four aorist varieties (reduplicating,
  siṣ, sa) remain future work.

- **2026-11-17 — Session 24 (continued):** User said "fine proceed". Completed the
  rare aorist varieties in `src/aorist.ts`: reduplicating (jan → `ajIjanat`),
  siṣ (yā → `ayAsIt`), sa (diś → `adikzat`), passive aorist 3s (vac → `avAci`,
  dā → `adAyi`), using explicit verified form tables. Added the precative
  (āśīrliṅ) active for bhū (`BUyAt`). Exported `derivePrecative`/`hasAorist`.
  Added 1 test. `npm test` passes (41/41).

- **2026-11-17 — Session 25 (continued):** User said "keep going". Added a full
  paradigm generator (`src/paradigm.ts`): `deriveParadigm()` produces all 8 major
  lakāras × 2 padas × 9 forms = 144 cells, with `formatParadigm()` for a text table.
  New CLI command `paradigm --dhatu BU`. Added 1 test. `npm test` passes (42/42).

- **2026-11-17 — Session 26 (continued):** User challenged the "complete" claim
  (correctly). Clarified feminine u-stem subanta already exists (`u-f`: `DenuH`)
  — that was a false gap. Added kṛt suffix ṇini (3.3.170, -in): `kf`→`kArin`,
  `dA`→`dAyin` (with a long-ā + i y-glide, 6.1.77). Added 1 test.
  `npm test` passes (43/43). The full kṛt inventory remains open-ended.

- **2026-11-17 — Session 27 (continued):** User said "keep going". Added kṛt suffix
  śānan (3.2.128, -māna): `pū`→`pavamAna`, `yaj`→`yajamAna`, via root overrides
  and a thematic-a infix. Added 1 test. `npm test` passes (44/44).

- **2026-11-17 — Session 28 (continued):** User said "keep going". Added kṛt suffix
  ṣṭran (3.2.182, -tra instrument nouns): `dā`→`dAtra`, `nī`→`netra`,
  `stu`→`stotra`, `yu`→`yotra` via a per-root stem map; guarded 6.1.78 so final
  o-stems keep their o. Added 1 test. `npm test` passes (45/45).

- **2026-11-18 — Session 29 (continued):** User said "keep going". Added kṛt suffix
  tṛn (3.2.135, habitual agent -tṛ): `kṛ`→`kartf`, `hu`→`hotf`, `ni`→`neSTf`,
  `tviz`→`tvaSTf` (with ṣuk ṣ and retroflex ṭ). Guarded 6.1.78 for the ho- stem.
  Added 1 test. `npm test` passes (46/46).

- **2026-11-18 — Session 30 (continued):** User gave the GitHub remote
  (`git@github-eadaradhiraj:eadaradhiraj/pypanini.git`); initialised git, committed
  everything (commit `557c844`), and pushed to `master`. Then added kṛt suffix kyap
  (3.3.99, feminine -yā): `vid`→`vidyA`, `man`→`manyA`, `i`→`ityA`, `zi`→`zayyA`.
  Added 1 test. `npm test` passes (47/47).
