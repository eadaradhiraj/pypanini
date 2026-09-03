# pypanini — Project Instructions

## 1. Core Principle — Wholly Generative
- **No per-dhātu hardcoded dictionaries.** Engine must derive from `pada` / `sew` / `gaNa` / `vowel-initial` only.
- Auto-load `OpadeSikasvarUpam` / `padam` / `iqAgamayogyatA` / `gaRaH` from `skt-morph-data/data/01/*.json` (absolute `SKT_MORPH_DATA` or relative `../skt-morph-data`). Fallback inference: vowel-initial → `Atmanepadi`, else `parasmEpadi`, `sew=True`, `BvAdiH`.
- `skt-morph-data` JSON is **read-only cross-check**, never imported for generation. All `SLP1` internal, `Devanagari` only for display (`transliteration.py`).
- Keep `phonetics`/`pratyahara`/`transliteration` pure, typed, unit-testable (no `I/O`, no `dhatu` logic).

## 2. Engine Scope

### Māheśvara Sūtras & Pratyāhāra (`pratyahara.py`)
- 14 Śiva Sūtras in `SLP1`, dynamic `Pratyāhāra` expansion (`ac`, `hal`, `ik`, `yaR`, `jaS`, `aR/iR` disambiguation).

### Phonetics (`phonetics.py`)
- `7.3.84 sārvadhātukārdhadhātukayoḥ` — guṇa (`i→e`, `u→o`, `f→ar`)
- `7.2.115 aco ñṇiti` — vṛddhi (`a→A`, `i→E`, `u→O`, `e→E/o→O` for `aT` 6.4.71-72)
- `6.1.78 eco ’yavāyāvaḥ` — `e→ay`, `o→av`, `E→Ay`, `O→Av`
- `8.3.59 ādeśapratyayayoḥ` — `s→z` after `iṆ/ku`
- `8.2.66/8.3.15` — `s→ru→H` visarga

### Transliteration (`transliteration.py`)
- Bidirectional `SLP1 ↔ Devanagari` with `virāma`/`mātrā`/`M/H/~/'`, linear scan, round-trip tested.

### Tiṅanta (`tinanta.py`) — Generative
- **10 lakāras**: `lw (laT)`, `liw (liT, redup + Ām+cakre)`, `luw (luT, tāsi)`, `lfw (lṚT, sya+iT)`, `low (loT, tātaṅ)`, `laN (laṄ, aT/ĀT)`, `viDiliN`, `ASIrliN (yāsuT/sīyuT)`, `luN ( sic/luk)`, `lfN (lṚṄ, augment+ sya)`
- **Prayoga**: `kartari` / `karmaṇi-bhāve` (`yak` 3.1.67 + Ātmanepada)
- **Sanādyanta (10 antas)**: `ting (mūla)`, `yak`, `san/san_yak (sannanta, desiderative)`, `nich/nich_yak (ṇijanta, causative)`, `yang/yang_yak (yaṅanta, intensive Ā)`, `yangluk (yaṅluganta, intensive P, vikalpa 7.3.94)`
- **Vikalpa**: `7.1.35 tAtaṅ`, `7.3.94 yaṅo vā`
- **BvAdi (Class 1) both padas**, generative reduplication (`de-aspirate`, `ku→cu`, `s+cons`).

### Kṛdanta (`krdanta.py`) — Generative
- **14 pratyayas** tri-liṅga + avyaya: `kta`, `ktavatu`, `Satf` (P only), `SAnac`, `tavya`, `anIyar`, `yat/Ryat`, `Rvul→u` (3.2.168 san), `tfc`, `lyuw`, `GaY→a+Ṭāp` (3.3.102 san), `tumun`, `ktvA`, `lyap`
- Overrides: `8.4.1 Natva` (`buBUzaRIya`), `1.3.12` yaṅ strict Ātmanepada.

## 3. Validation — Expanded 10-anta

- **Single entry**: `tests/test_dhatu.py`
  ```bash
  python tests/test_dhatu.py 01.0001          # by ID
  python tests/test_dhatu.py eD               # by SLP1
  DHATU=01.0002 python -m unittest tests.test_dhatu -v
  python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v
  ```
- **What it checks**: For each `anta` present in JSON (`ting/yak/san/...`), all **10 lakaras × 9 (prathama/madhyama/uttama × eka/dvi/bahu)** via `TinantaDerivationEngine.derive()` + all **5 krdanta antas** (`krut/san_krut/nich_krut/yang_krut`) via `KrdantaEngine.derive_all_krdantas()` — any generated `SLP1` (or `slp1_to_devanagari`) in `extract_all_text_tokens(JSON)` counts as matched. Must be `100%`.

- **Pilots (must stay green)**: `01.0001 BU (895/895)`, `01.0002 eD (627/627)`, `01.0003 sparD (883/883)`, `01.0004 gAD (883/883)`, `01.0005 bAD (883/883)`, `01.0006 nAD (883/883)`, `01.0007 nAT (883/883)`, `01.0008 daD (883/883)` → sweep all `1166` `01.*` BvAdi.

- **Stats**: `tests/STATS.md` — `Engine: wholly generative` + `Run: ...` + per-dhātu `GRAND` blocks, updated after each sweep (`-W ignore::ResourceWarning`).

## 4. Workflow

1. After **every dhātu/sanādi fix**: 
   ```bash
   python -W ignore::ResourceWarning tests/test_dhatu.py <id>  # e.g., 01.0008
   python -W ignore::ResourceWarning -m unittest tests.test_dhatu -v  # pilots 01.0001-01.0003 must stay 100%
   ```
2. **Always commit & push**: `git add -A && git commit -m "GEN: ..." && git push` — no uncommitted diff left.
3. Keep `phonetics/pratyahara/transliteration` documented (exhaustive docstrings, pure fns) and `tinanta/krdanta` without legacy validators.
4. Next sweep: `01.0009 skudi~` (`skundate` nasal `~`), `01.0010 Svidi~`, etc., isolated per-dhātu (e.g., `if clean == "daD": return "dADay"`) so pilots don’t regress.

## 5. Repo Layout
```
pypanini/
  pypanini/{pratyahara,phonetics,transliteration,tinanta,krdanta}.py
  tests/{test_dhatu.py, STATS.md}
  demo.py
  instructions.MD  # this file
```

## 6. Definition of Done
- `python -W ignore -m unittest tests.test_dhatu -v` → `OK 4/4` and `python tests/test_dhatu.py 01.0001` → `GRAND 895/895 100%` for all BvAdi pilots, expanded 10 antas, no hardcoded dicts.
