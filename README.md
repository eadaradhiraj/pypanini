# pypanini

A **pure TypeScript / Node.js** Pāṇinian word generator, with **SLP1** I/O and
step-by-step **prakriyā traces**. Inspired by ashtadhyayi.com, written from scratch.
Scope: **classical Sanskrit** — sūtras on subanta, kṛdanta, tiṅanta and nāmādhatu.
Bundles the full MIT-licensed Dhātupāṭha (2,229 roots) and Sūtrapaṭha (3,984 sūtras).

> **Resuming work?** Read [`PROGRESS.md`](./PROGRESS.md) first. It records architecture,
> decisions, current status, known limitations, and the exact next steps.

## Install & build

```bash
npm install
npm test
```

## CLI

```bash
# all nine present forms of bhū (parasmai, kartari)
npm run cli -- tinanta --dhatu BU

# every lakāra, 3rd singular parasmai
for l in lat lit lut lrt lot lan lng lin; do
  npm run cli -- tinanta --dhatu BU --lakara "$l" --purusha prathama --vacana eka
done

# one form with its prakriyā trace
npm run cli -- tinanta --dhatu BU --purusha prathama --vacana eka --trace

# passive (karmani): pac → pacyate
npm run cli -- tinanta --dhatu pac --prayoga karmani --pada atmane

# aorist (luN): bhū → abhūt, pac → apacat, nī → anaiṣīt
npm run cli -- tinanta --dhatu BU --lakara latN

# desiderative (san): bhū → bubhūṣati
npm run cli -- tinanta --dhatu BU --sanadi san

# causative (ṇic): bhū → bhāvayati
npm run cli -- tinanta --dhatu BU --sanadi nic

# intensive (yaṅ / "yang"): bhū → bobhūyate; pac → pāpacyate
npm run cli -- tinanta --dhatu BU --sanadi yan
npm run cli -- tinanta --dhatu pac --sanadi yang

# intensive without -ya- (yaṅluk): bhū → bobhavīti; pac → pāpacīti
npm run cli -- tinanta --dhatu BU --sanadi yangLuk
npm run cli -- tinanta --dhatu pac --sanadi yangLuk

# kṛdanta (12 kṛt suffixes: tac, tfc, satr, ani, tum, tavya, lyuT, ktvA, nvul, ktavatu, sanaC, yat, ktin, Nini, Sanan, STran, TRn, Kyap, Sa, uH, ghaH, raH, kru, AruH, varac, kvip, Du, knu, kSnu, izNuc, yuc, ruH2, kurac, ghurac, kvarap, vuN, ghinuN)
npm run cli -- krdanta --dhatu kf --krt tac     # kfta  (past passive participle)
npm run cli -- krdanta --dhatu kf --krt tfc     # kartf (agent noun)
npm run cli -- krdanta --dhatu kf --krt tavya   # kartavya (gerundive)
npm run cli -- krdanta --dhatu BU --krt tum     # Bavitum (infinitive)
npm run cli -- subanta --pratipadika bala --linga napumsaka --vibhakti 3 --vacana bahu

# other stem classes: i-, u- (m/n), ā-, ī- (f)
npm run cli -- subanta --pratipadika agni --linga pumsaka --vibhakti 3 --vacana bahu  # agniBiH
npm run cli -- subanta --pratipadika guru --linga pumsaka --vibhakti 1 --vacana bahu  # guravaH
npm run cli -- subanta --pratipadika sItA --linga stri --vibhakti 3 --vacana eka      # sItayA
npm run cli -- subanta --pratipadika nadI --linga stri --vibhakti 1 --vacana bahu     # nadyaH
npm run cli -- subanta --pratipadika Denu --linga stri --vibhakti 1 --vacana eka      # DenuH
npm run cli -- subanta --pratipadika manas --linga napumsaka --vibhakti 7 --vacana eka # manasi
npm run cli -- subanta --pratipadika rAjan --linga pumsaka --vibhakti 3 --vacana eka  # rAjYA
npm run cli -- subanta --pratipadika pitf --linga pumsaka --vibhakti 7 --vacana bahu   # pitfzu

# full conjugation table (all lakāras × both padas)
npm run cli -- paradigm --dhatu BU

# denominative verbs (nāmādhatu, Pāṇini 3.1.8–3.1.21)
npm run cli -- namadhatu --pratipadika putra --pratyaya kyac    # putrIyati
npm run cli -- namadhatu --pratipadika putra --pratyaya kAmyac  # putrakAmyati
npm run cli -- namadhatu --pratipadika Syena --pratyaya kyaN    # SyenAyate

# search the full 2,229-root Dhātupāṭha
npm run cli -- dhatus --search BU --limit 5

# look up any of the 3,984 sūtras by code or text
npm run cli -- sutras --code 3.1.20
npm run cli -- sutras --search upasarga --limit 5

# prefixes (upasargas, 1.4.58–1.4.60)
npm run cli -- tinanta --dhatu BU --upasarga pra   # praBavati
npm run cli -- tinanta --dhatu nam --upasarga pra  # praRamati (ṇatva, 8.4.14)

# reverse declension: declined word → base + case/number/gender
npm run cli -- analyze --word WrampaH
npm run cli -- analyze --word WrampeNa
npm run cli -- subanta --word WrampeNa --declension   # --analyze also works
```

### Example trace

```
$ npm run cli -- tinanta --dhatu BU --purusha prathama --vacana eka --trace
BU lat kartari parasmai prathama eka  =>  Bavati
  1.4.99 (laḥ parasmaipadam — parasmai-pada), 1.4.101 (tiṇas trīṇi), 1.4.102 (ekavacanādi) | BU
  1.3.1                                            | BU
  3.1.1/3.1.2 (pratyayaḥ paraś ca), 3.1.91 (dhātoḥ), 3.1.93 (kṛdatiṅ) | BU
  3.2.123                                          | BU + la~w
  1.3.2                                            | BU + la~w
  1.3.3                                            | BU + la~w
  1.3.9                                            | BU + l
  1.3.78                                           | BU + l
  3.4.78                                           | BU + tip
  1.3.3                                            | BU + tip
  1.3.9                                            | BU + ti
  3.4.113                                          | BU + ti
  3.1.68                                           | BU + Sap + ti
  1.3.9                                            | BU + a + ti
  3.4.113                                          | BU + a + ti
  7.3.84                                           | Bo + a + ti
  1.4.14                                           | Bo + a + ti
  6.1.78                                           | Bav + a + ti
  7.3.101                                          | Bav + a + ti
  6.1.84 (ekādeśa: a + a/e/A → a/e/A)              | Bav + a + ti
  8.4.68                                           | Bavati
```

## Library

```ts
import { Vyakarana, Lakara, Prayoga, Purusha, Vacana, Pada } from 'pypanini';

const v = new Vyakarana();
const [p] = v.deriveTinantas({
  dhatu: 'BU',              // SLP1 for भू; or a Dhatu object
  lakara: Lakara.Lat,
  prayoga: Prayoga.Kartari,
  purusha: Purusha.Prathama,
  vacana: Vacana.Eka,
  pada: Pada.Parasmai,
});

console.log(p.text());      // "Bavati"
console.log(p.history);     // [{ rule: '1.3.1', result: 'BU' }, ...]
```

### Reverse declension (find the base word)

```ts
import { analyzeSubanta, describeAnalysis } from 'pypanini';

const results = analyzeSubanta('WrampeNa');
// [{ word: 'WrampeNa', base: 'Wramp', pratipadika: 'Wrampa',
//    vibhakti: Vibhakti.Trtiya, vacana: Vacana.Eka, linga: Linga.Pumsaka, ... }]
console.log(describeAnalysis(results[0]));
// base Wramp | prātipadika Wrampa | tṛtīyā (instrumental), singular (eka), masculine ...
```

Analysis works by enumerating every stem class and ending, proposing a prātipadika, and
verifying it by re-synthesising the word — so analysis and generation can never disagree.
Supported classes: **a- / i- / u-** (m/n), **ā- / ī- / u-** (f), and consonant stems
**-as** (n), **-an / -at / -ṛ** (m).
The matcher tolerates `N` written where strict SLP1 uses `n`/`R`, while preserving your
original spelling in the reported base.

## Scope

- **Scope:** classical Sanskrit only — all sūtras on subanta, kṛdanta, tiṅanta,
  nāmādhatu, and upasargas (prefixes). Vedic `leṭ` is intentionally excluded.
  Full MIT Dhātupāṭha (2,229 roots) and Sūtrapaṭha (3,984 sūtras) bundled.
  Derivations run through a condition-based rule scheduler with siddha/asiddha
  phases (8.2.1 `pūrvatrāsiddham`, incl. the asiddhavat section 6.1.2–6.1.7),
  priorities and antaranga/bahiranga strength, and optional phase-entry snapshots
  for mutual invisibility of asiddha `when`-conditions. Ātmanepada audited for
  lat/lit/luṭ/laṅ/lṛṅ + aorist (luN, all varieties); 15 subanta stem classes.
- **Implemented:** tiṅanta for all major lakāras, parasmai + karmani; saṇādi
  (san/ṇic/yaṅ/yaṅluk); thirty-seven kṛdanta suffixes; subanta for 15 stem classes; nāmādhatu
  (kyac/kāmyac/kyaṅ/ṇic + 3.1.12–18 kyaṅ types); upasargas (19 prefixes, 8.4.14
  ṇatva + 8.3.65 ṣatva); reverse declension.
  Each with prakriyā traces.
- `yan` is accepted as an alias for `yang` (they are the same thematic yaṅ intensive).

## SLP1 cheat sheet

| Devanāgarī | SLP1 | Devanāgarī | SLP1 |
|---|---|---|---|
| अ आ इ ई | a A i I | उ ऊ ऋ ॠ | u U f F |
| ए ऐ ओ औ | e E o O | क ख ग घ ङ | k K g G N |
| च छ ज झ ञ | c C j J Y | ट ठ ड ढ ण | w W q Q R |
| त थ द ध न | t T d D n | प फ ब भ म | p P b B m |
| य र ल व | y r l v | श ष स ह | S z s h |

## License

MIT. Dhātupāṭha data format informed by the MIT-licensed data shared by ashtadhyayi.com.
