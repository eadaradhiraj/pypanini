# pypanini — Project Instructions

## 1. Core Principle — Wholly Generative
- **No per-dhātu hardcoded dictionaries.** Engine must derive from `pada` / `sew` / `gaNa` / `vowel-initial` only.
- Auto-load `OpadeSikasvarUpam` / `padam` / `iqAgamayogyatA` / `gaRaH` from `skt-morph-data/data/01/*.json` (absolute `SKT_MORPH_DATA` or relative `../skt-morph-data`). Fallback inference: vowel-initial → `Atmanepadi`, else `parasmEpadi`, `sew=True`, `BvAdiH`.
- `skt-morph-data` JSON is **read-only cross-check**, never imported for generation. All `SLP1` internal (no Devanagari).
- Keep `phonetics`/`pratyahara` pure, typed, unit-testable (no `I/O`, no `dhatu` logic).

## 2. Engine Scope — Focus: tinanta / subanta / krdanta ONLY

> No Devanagari, no extra features. Only the three generative nominal/verbal systems.

### Māheśvara Sūtras & Pratyāhāra (`pratyahara.py`) — support only
- 14 Śiva Sūtras in `SLP1`, dynamic `Pratyāhāra` (`ac`/`hal` etc.) for `tinanta`/`subanta`/`krdanta` only.

### Phonetics (`phonetics.py`) — support only
- `7.3.84`, `7.2.115`, `6.1.78`, `8.3.59`, `8.2.66/8.3.15` — used by the three engines, no independent feature.

### Tiṅanta (`tinanta.py`) — Generative
- **10 lakāras**: `lw (laT)`, `liw (liT, redup + Ām+cakre)`, `luw (luT, tāsi)`, `lfw (lṚT, sya+iT)`, `low (loT, tātaṅ)`, `laN (laṄ, aT/ĀT)`, `viDiliN`, `ASIrliN (yāsuT/sīyuT)`, `luN ( sic/luk)`, `lfN (lṚṄ, augment+ sya)`
- **Prayoga**: `kartari` / `karmaṇi-bhāve` (`yak` 3.1.67 + Ātmanepada)
- **Sanādyanta (10 antas)**: `ting (mūla)`, `yak`, `san/san_yak (sannanta, desiderative)`, `nich/nich_yak (ṇijanta, causative)`, `yang/yang_yak (yaṅanta, intensive Ā)`, `yangluk (yaṅluganta, intensive P, vikalpa 7.3.94)`
- **Vikalpa**: `7.1.35 tAtaṅ`, `7.3.94 yaṅo vā`
- **BvAdi (Class 1) both padas**, generative reduplication (`de-aspirate`, `ku→cu`, `s+cons`).

### Kṛdanta (`krdanta.py`) — Generative
- **14 pratyayas** tri-liṅga + avyaya: `kta`, `ktavatu`, `Satf` (P only), `SAnac`, `tavya`, `anIyar`, `yat/Ryat`, `Rvul→u` (3.2.168 san), `tfc`, `lyuw`, `GaY→a+Ṭāp` (3.3.102 san), `tumun`, `ktvA`, `lyap`
- Overrides: `8.4.1 Natva` (`buBUzaRIya`), `1.3.12` yaṅ strict Ātmanepada.

### Subanta (`subanta.py`) — Generative (NEXT)
- **Sup declension**: `sU`/`au`/`jas`/`am`/`auT`/`Sas`/`TA`/`ByAm`/`Bis`/`Ne`/`ByAm`/`Byas`/`Nasi`/`os`/`Am`/`Ni`/`os`/`sup` — all 8 vibhaktis × 3 vacanas × 3 liṅgas, `a/i/u/f/n` stems, `sarvanāman` etc. — wholly generative, `SLP1` only, no Devanagari.

## 3. Validation — Expanded 10-anta

- **Single entry**: `tests/test_dhatu.py`
  ```bash
  python tests/test_dhatu.py 01.0001          # by ID
  python tests/test_dhatu.py eD               # by SLP1
  DHATU=01.0002 python -m unittest tests.test_dhatu -v
  python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v
  ```
- **What it checks**: For each `anta` present in JSON (`ting/yak/san/...`), all **10 lakaras × 9 (prathama/madhyama/uttama × eka/dvi/bahu)** via `TinantaDerivationEngine.derive()` + all **5 krdanta antas** (`krut/san_krut/nich_krut/yang_krut`) via `KrdantaEngine.derive_all_krdantas()` — any generated `SLP1` in `extract_all_text_tokens(JSON)` counts as matched. Must be `100%`.

- **Progress — tinanta/krdanta (expanded 10 antas, SLP1-only)**:
  - `tinanta` + `krdanta` **done (100% expanded)**: `8/1166` BvAdi — `01.0001 BU (895/895)`, `01.0002 eD (627/627)`, `01.0003 sparD (883/883)`, `01.0004 gAD (883/883)`, `01.0005 bAD (883/883)`, `01.0006 nAD (883/883)`, `01.0007 nAT (883/883)`, `01.0008 daD (883/883)`
  - `tinanta`/`krdanta` **pending**: `1158/1166` BvAdi (`01.0009 skudi~ 9/883` nasal, `01.0010 Svidi~` etc. — `~`/`i`-ending special)
  - `subanta` **not started (0/—)**: `0` `sup` forms done, `subanta.py` to be created next for `a/i/u/f/n` stems
  - Sweep target: all `1166` `01.*` BvAdi at `100%` expanded for `tinanta`+`krdanta`, then `subanta` for nominal declension.

- **Stats**: `tests/STATS.md` — `Engine: wholly generative` + `Run: ...` + per-dhātu `GRAND` blocks, updated after each sweep (`-W ignore::ResourceWarning`).

## 4. Workflow

1. After **every dhātu/sanādi fix**: 
   ```bash
   python -W ignore::ResourceWarning tests/test_dhatu.py <id>  # e.g., 01.0008
   python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v  # pilots 01.0001-01.0003 must stay 100%
   ```
2. **Always commit & push**: `git add -A && git commit -m "GEN: ..." && git push` — no uncommitted diff left.
3. Keep `phonetics/pratyahara` documented (exhaustive docstrings, pure fns) and `tinanta/krdanta` without legacy validators.
4. Next sweep: `01.0009 skudi~` (`skundate` nasal `~`), `01.0010 Svidi~`, etc., isolated per-dhātu (e.g., `if clean == "daD": return "dADay"`) so pilots don’t regress.

## 5. Repo Layout — Only the three
```
pypanini/
  pypanini/{pratyahara,phonetics,tinanta,subanta,krdanta}.py  # subanta is next, tinanta/krdanta done expanded
  tests/{test_dhatu.py (tinanta+krdanta), test_subanta.py (subanta), STATS.md}
  demo.py  # tinanta/subanta/krdanta demo only
  instructions.MD
```

## 6. Definition of Done
- `python -W ignore -m unittest tests.test_dhatu -v` → `OK 4/4` and `python tests/test_dhatu.py 01.0001` → `GRAND 895/895 100%` for all BvAdi pilots, expanded 10 antas, no hardcoded dicts.

## 7. Update Instructions
Update this instructions with progress
