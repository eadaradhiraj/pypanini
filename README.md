# PyPanini

A computational Sanskrit grammar engine implemented in Python, modeling Pāṇinian morphophonemics using the **SLP1** (Sanskrit Library Phonetic Basic) encoding scheme.

---

## Features Implemented

### 1. Māheśvara Sūtras & Pratyāhāra Generator (`pypanini/pratyahara.py`)
- Full representation of the 14 Śiva Sūtras.
- Dynamic generation of any valid Pāṇinian *Pratyāhāra* (`ac`, `hal`, `al`, `ik`, `yaR`, `jaS`, etc.).
- Disambiguation logic for repeated markers (e.g., handling the two occurrences of `R` in Sutra 1 vs Sutra 6 for `aR` and `iR`).

### 2. Phonetics & Morphophonemic Operations (`pypanini/phonetics.py`)
- **Guṇa & Vṛddhi**: 7.3.84 (*sārvadhātukārdhadhātukayoḥ*) and 7.2.115 (*aco ñṇiti*).
- **Vowel Sandhi**: 6.1.78 (*eco 'yavāyāvaḥ*).
- **Ṣatva**: 8.3.59 (*ādeśapratyayayoḥ* — dental `s` to retroflex `z` after `iR` or `ku`).
- **Pada-kārya**: 8.2.66 (*sasajuṣo ruḥ*) and 8.3.15 (*kharavasānayor visarjanīyaḥ* — Rutva and Visarga transformation).

### 3. Tiṅanta Engine (`pypanini/tinanta.py`)
Covers verbal conjugations across both **Parasmaipada** and **Ātmanepada**:

- **All 10 Lakāras (*Daśa-lakārāḥ*)**:
  1. `lw` (लट् - Present)
  2. `liw` (लिट् - Perfect / Remote Past, including reduplication and periphrastic *ām*-formation)
  3. `luw` (लुट् - First Future / Periphrastic Future with *tāsi*)
  4. `lfw` (लृट् - Simple Future with *sya* and *iṭ*)
  5. `low` (लोट् - Imperative, with *tātaṅ* optionality)
  6. `laN` (लङ् - Imperfect Past with *aṭ* and *āṭ* augments)
  7. `viDiliN` (विधिलिङ् - Optative / Potential)
  8. `ASIrliN` (आशीर्लिङ् - Benedictive / Precative with *yāsuṭ/sīyuṭ*)
  9. `luN` (लुङ् - Aorist Past with *sic* and *sic-luk*)
  10. `lfN` (लृङ् - Conditional / Past-Future)

- **Voices (*Prayoga*)**:
  - *Kartari* (Active)
  - *Karmaṇi / Bhāve* (Passive / Impersonal with 3.1.67 *yak* and Ātmanepada inflection)

- **Secondary Stems (*Sanādyanta*)**:
  - **Ṇijanta (णिजन्त - Causative)**: `BAvayati` (Active), `BAvyate` (Passive).
  - **Sannanta (सन्नन्त - Desiderative)**: `buBUzati` (Active), `buBUzyate` (Passive).
  - **Yaṅanta (यङन्त - Intensive Ātmanepada)**: `boBUyate`.
  - **Yaṅluganta (यङ्लुगन्त - Intensive Parasmaipada)**: `boBavIti / boBoti`.

- **Pāṇinian Optionality (*Vikalpa*)**:
  - 7.1.35 *tātaṅ* in `low`: `Bavatu / BavatAt`, `Bava / BavatAt`.
  - 7.3.94 *yaṅo vā* in `yaNluk`: `boBavIti / boBoti`, `boBavIzi / boBozi`, `boBavImi / boBomi`.

- **Verified Root Paradigms**:
  - `01.0001` — **भू सत्तायाम् (`BU`)**: Parasmaipada, Class 1.
  - `01.0002` — **एध् वृद्धौ (`eD`)**: Ātmanepada, Seṭ, vowel-initial (*āṭ*-āgama, *ām*-pratyaya).

### 4. Kṛdanta Engine (`pypanini/krdanta.py`)
Generates 14 primary verbal affixes across all 4 stem types (Primitive, Ṇijanta, Sannanta, Yaṅanta):

- **Participles & Gerundives (inflected in Masculine, Feminine, Neuter)**:
  - `kta` (Past Passive Participle)
  - `ktavatu` (Past Active Participle)
  - `Satf` (Present Active Participle)
  - `SAnac` (Present Middle/Passive Participle)
  - `tavya` (Obligation Gerundive)
  - `anIyar` (Fitness Gerundive)
  - `yat` / `Ryat` (Potential Gerundive)
  - `Rvul` / `u` (Agent Noun)
  - `tfc` (Agent Noun in `-tṛ`)
- **Action & Verbal Nouns**:
  - `lyuw` (Neuter action noun in `-ana`)
  - `GaY` / `a + wAp` (Masculine/Feminine action noun)
- **Avyayas (Indeclinables)**:
  - `tumun` (Infinitive)
  - `ktvA` (Absolutive without prefix)
  - `lyap` (Absolutive with prefix)
- **Anta-Specific Overrides**:
  - 3.2.168 (*sanāśaṁsabhikṣa uḥ*): Sannanta takes `u` (`buBUzu`), overriding `Rvul`.
  - 3.3.102 (*a pratyayāt*): Sannanta action noun takes `a + ṭāp` (`buBUzA`), overriding `GaY`.
  - 8.4.1/8.4.2: Retroflex Ṇatva in `buBUzaRIya` and `buBUzaRa`.
  - 1.3.12: Strict Ātmanepada compliance for Yaṅanta (excludes `Satf`, applies `SAnac`).

---

## Project Structure

```text
pypanini/
├── pypanini/
│   ├── __init__.py           # Package exports
│   ├── pratyahara.py         # Māheśvara Sūtras & Pratyāhāra expansion
│   ├── phonetics.py          # Guṇa, Vṛddhi, Sandhi, Ṣatva, Visarga rules
│   ├── tinanta.py            # Verbal derivation engine (10 Lakāras, Sanādi, Voices)
│   └── krdanta.py            # Primary verbal affixes across genders and antas
├── tests/
│   ├── test_pratyahara.py    # Unit tests for Shiva Sutras
│   ├── test_tinanta.py       # Unit tests for verbal derivations
│   └── test_krdanta.py       # Unit tests for participles and overrides
├── test_ashtadhyayi.py       # Validation test against scraped 01.0001 (BU) data
├── test_01_0002.py           # Validation test against scraped 01.0002 (eD) data
├── demo.py                   # Interactive showcase script
├── LICENSE                   # MIT License
└── README.md
```

---

## Running Tests & Demo

### 1. Run Unit Tests
```bash
python3 -m unittest discover tests
```

### 2. Run the Demo
```bash
python3 demo.py
```

### 3. Run Validation Against Scraped Ashtadhyayi.com Data
```bash
# Validate root 01.0001 (BU)
python3 test_ashtadhyayi.py

# Validate root 01.0002 (eD)
python3 test_01_0002.py
```

---

## License

This project is licensed under the [MIT License](LICENSE).
