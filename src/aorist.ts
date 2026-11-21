import { Prakriya } from './core/prakriya';
import { Pada, Purusha, SLP1, Vacana } from './core/types';

/**
 * The aorist (luṅ, 3.2.110) has seven varieties in Pāṇini. This module implements
 * the three most common in Classical Sanskrit:
 *   - root aorist (a + bare root + athematic secondary endings), e.g. bhū → abhūt
 *   - a-aorist  (a + weak root + a + thematic secondary endings), e.g. sic → asicat
 *   - s/iṣ-aorist (a + strengthened root + s/iṣ + athematic endings),
 *     e.g. nī → anaiṣīt, budh → abodhīt
 *
 * 3rd-person plural parasmai uses -uḥ / -an; sibilant aorists take -īt/-īḥ in
 * the 3rd/2nd singular active (per the traditional sibilant-aorist endings).
 */

export type AoristKind = 'root' | 'a' | 's' | 'is' | 'redup' | 'sis' | 'sa';

type FormTable = Partial<Record<Purusha, Partial<Record<Vacana, SLP1>>>>;

interface AoristEntry {
  kind: AoristKind;
  /** Augmented, graded stem WITHOUT the augment `a` or the sibilant. */
  stem: SLP1;
  /** Explicit surface forms for rare varieties (parasmai / atmane). */
  formsP?: FormTable;
  formsA?: FormTable;
  /** Override sūtra code for the formation. */
  code?: string;
}

const AORIST: Record<string, AoristEntry> = {
  // root aorist (2.4.77 gāti-sthā-ghu-pā-bhūbhyaḥ sicaḥ — sic-lopa)
  as: { kind: 'root', stem: 'Asth', code: '7.4.17 (asyates thuk — āsthat)', formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'AsTat' } } },
  ad: { kind: 'a', stem: 'Gas', code: '2.4.37 (luṅ-sanor ghasḷ — aghasat)', formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'aGasat' } } },
  BU: { kind: 'root', stem: 'BU' },
  i: { kind: 'root', stem: 'gA', code: '2.4.45 (iRo gA luNi), 2.4.77 (sic-lopa)', formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'agAt' } } },
  sTA: { kind: 'root', stem: 'sTA', code: '2.4.77 (sic-lopa — asthāt)', formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'asTAt' } } },
  pA: { kind: 'root', stem: 'pA', code: '2.4.77 (sic-lopa — apāt)', formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'apAt' } } },
  // √iṣ iṣ-aorist: aiṣīt (EzIt) — source: Wiktionary.
  iS: { kind: 's', stem: 'ez', code: '3.1.44 (cleḥ sic — iṣ iṣ-aorist)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'EzIt' } } },
  // √mṛj s-aorist: amārkṣīt (amArkzIt) — source: Wiktionary.
  mfz: { kind: 's', stem: 'mArkz', code: '3.1.43 (cli luṅi — mṛj s-aorist)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'amArkzIt' } } },
  // √jñā iṣ-aorist: ajñāsīt (ajFAsIt) — source: bhagavadgita.org.in.
  jFnA: { kind: 's', stem: 'jFA', code: '3.1.44 (cleḥ sic — jñā iṣ-aorist)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'ajFAsIt' } } },
  // √grah reduplicating aorist: ajigrahat (ajigrahat) — source: bhagavadgita.org.in.
  grah: { kind: 'redup', stem: 'jigrah', code: '3.1.48 (ṇiśrīdrusṛubhyaḥ kar — jigrahat)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'ajigrahat' } } },
  // √dviṣ kṣ-aorist: adviKṣat (advikzat) — source: bhagavadgita.org.in.
  dviS: { kind: 's', stem: 'dvez', code: '3.1.45 (śal igupadhād anिटḥ kṣaḥ — adviKṣat)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'advikzat' } } },
  // √ṛ root aorist: ārat (ārāt/āran) — 2.4.77 sic-lopa after ṛ-class root.
  fR: { kind: 'root', stem: 'Ar', code: '2.4.77 (sic-lopa — ārat)', formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'Arat' } } },
  // a-aorist
  // √vac: avocat (3.1.52 asatyativaktikhātibhyo ’ṅ), with guṇa o in the stem.
  vac: { kind: 'a', stem: 'voc', code: '3.1.52 (asatyativaktikhātibhyo ’ṅ — avocat)' },
  vach: { kind: 'a', stem: 'voc', code: '3.1.52 (asatyativaktikhātibhyo ’ṅ — avocat)' },
  pac: { kind: 'a', stem: 'pac' },
  rudh: { kind: 'a', stem: 'rudh', code: '3.1.57 (iritaḥ vā — rudh a-aorist)' },
  yuj: { kind: 'a', stem: 'yuj', code: '3.1.56 (sarti-śāsty-artibhyaś ca — yuj a-aorist)' },
  // √ji s-aorist: ajaiṣīt (3s) — vṛddhi i→ai.
  ji: { kind: 's', stem: 'jE', code: '3.1.44 (cleḥ sic — ji s-aorist)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'ajEzIt' } } },
  // √muc root aorist with guṇa: amok (3s) — Whitney §832.
  muc: { kind: 'root', stem: 'mok', code: '3.1.44 (mucaḥ — muc root aorist)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'amok' } } },
  // √nī s-aorist: anaiṣīt (3s), anaiṣṭām (3d), anaiṣuḥ (3p) — 7.2.11 iṭ-naṣi.
  nI: { kind: 's', stem: 'nE', code: '3.1.44 (cleḥ sic — nī s-aorist)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'anEzIt' } } },
  // √śru s-aorist: aśrauṣīt (3s) — vṛddhi of u→au.
  zru: { kind: 's', stem: 'zrO', code: '3.1.44 (cleḥ sic — śru s-aorist)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'azrOzIt' } } },
  // √car iṣ-aorist with vṛddhi: acārīt (3s) — 7.2.35.
  car: { kind: 'is', stem: 'cAri', code: '3.1.44 (cleḥ sic — car iṣ-aorist)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'acArizIt' } } },
  sic: { kind: 'a', stem: 'sic', code: '3.1.44 (cleḥ sic — asicat)' },
  gam: { kind: 'a', stem: 'gam' },
  // s-aorist of kṛ: akārṣīt (a + kār + ṣ + īt)
  kf: { kind: 's', stem: 'kAr' },
  // a-aorist of bhid: abhidat (3.1.57 vārttika)
  bhid: { kind: 'a', stem: 'bhid', code: '3.1.57 (iritaḥ vā — bhid a-aorist)' },
  // a-aorist of vid (3.4.109 jus: aviduḥ)
  vid: { kind: 'a', stem: 'vid', code: '3.4.109 (sij-abhyasta-vidibhyaś ca — jus)' },
  // s-aorist (vṛddhi final vowel + s → ṣ)
  ni: {
    kind: 's', stem: 'nE', // nī → nai + ṣ (active)
    // middle: guṇa (ne), not vṛddhi; ṣṭ→ṣṭ; 3pl -ata
    formsA: {
      [Purusha.Prathama]: { [Vacana.Eka]: 'anezTa', [Vacana.Dvi]: 'anezAtAm', [Vacana.Bahu]: 'anezata' },
      [Purusha.Madhyama]: { [Vacana.Eka]: 'anezthAH', [Vacana.Dvi]: 'anezAthAm', [Vacana.Bahu]: 'aneDvam' },
      [Purusha.Uttama]: { [Vacana.Eka]: 'anezi', [Vacana.Dvi]: 'anezvahi', [Vacana.Bahu]: 'anezmahi' },
    },
  },
  // iṣ-aorist (guṇa medial vowel + iṣ)
  budh: {
    kind: 'is', stem: 'boD', // budh → bodh + iṣ (active)
    formsA: {
      [Purusha.Prathama]: { [Vacana.Eka]: 'abozizTa', [Vacana.Dvi]: 'abozizAtAm', [Vacana.Bahu]: 'abozizata' },
      [Purusha.Madhyama]: { [Vacana.Eka]: 'abozizthAH', [Vacana.Dvi]: 'abozizAthAm', [Vacana.Bahu]: 'abozidhvam' },
      [Purusha.Uttama]: { [Vacana.Eka]: 'abozizi', [Vacana.Dvi]: 'abozizvahi', [Vacana.Bahu]: 'abozizmahi' },
    },
  },
  // reduplicating aorist (class 10 / causatives), e.g. jan → ajījanat
  jan: {
    kind: 'redup', stem: 'jIjan',
    formsP: {
      [Purusha.Prathama]: { [Vacana.Eka]: 'ajIjanat', [Vacana.Dvi]: 'ajIjanatAm', [Vacana.Bahu]: 'ajIjanan' },
      [Purusha.Madhyama]: { [Vacana.Eka]: 'ajIjanaH', [Vacana.Dvi]: 'ajIjanatam', [Vacana.Bahu]: 'ajIjanata' },
      [Purusha.Uttama]: { [Vacana.Eka]: 'ajIjanam', [Vacana.Dvi]: 'ajIjanAva', [Vacana.Bahu]: 'ajIjanAma' },
    },
    formsA: {
      [Purusha.Prathama]: { [Vacana.Eka]: 'ajIjanata', [Vacana.Dvi]: 'ajIjanetAm', [Vacana.Bahu]: 'ajIjananta' },
      [Purusha.Madhyama]: { [Vacana.Eka]: 'ajIjanathAH', [Vacana.Dvi]: 'ajIjanethAm', [Vacana.Bahu]: 'ajIjanadhvam' },
      [Purusha.Uttama]: { [Vacana.Eka]: 'ajIjane', [Vacana.Dvi]: 'ajIjanAvahi', [Vacana.Bahu]: 'ajIjanAmahi' },
    },
  },
  // siṣ-aorist (roots in -ā), e.g. yā → ayāsīt
  yA: {
    kind: 'sis', stem: 'yA',
    formsP: {
      [Purusha.Prathama]: { [Vacana.Eka]: 'ayAsIt', [Vacana.Dvi]: 'ayAsizTAm', [Vacana.Bahu]: 'ayAsizuH' },
      [Purusha.Madhyama]: { [Vacana.Eka]: 'ayAsIH', [Vacana.Dvi]: 'ayAsiztam', [Vacana.Bahu]: 'ayAsizta' },
      [Purusha.Uttama]: { [Vacana.Eka]: 'ayAsizam', [Vacana.Dvi]: 'ayAsizva', [Vacana.Bahu]: 'ayAsizma' },
    },
  },
  // sa-aorist (roots in ś/ṣ/h), e.g. diś → adikṣat
  diS: {
    kind: 'sa', stem: 'dik',
    formsP: {
      [Purusha.Prathama]: { [Vacana.Eka]: 'adikzat', [Vacana.Dvi]: 'adikzatAm', [Vacana.Bahu]: 'adikzan' },
      [Purusha.Madhyama]: { [Vacana.Eka]: 'adikzaH', [Vacana.Dvi]: 'adikzatam', [Vacana.Bahu]: 'adikzata' },
      [Purusha.Uttama]: { [Vacana.Eka]: 'adikzam', [Vacana.Dvi]: 'adikzAva', [Vacana.Bahu]: 'adikzAma' },
    },
    formsA: {
      [Purusha.Prathama]: { [Vacana.Eka]: 'adikzata', [Vacana.Dvi]: 'adikzAtAm', [Vacana.Bahu]: 'adikzanta' },
      [Purusha.Madhyama]: { [Vacana.Eka]: 'adikzathAH', [Vacana.Dvi]: 'adikzAthAm', [Vacana.Bahu]: 'adikzadhvam' },
      [Purusha.Uttama]: { [Vacana.Eka]: 'adikzi', [Vacana.Dvi]: 'adikzAvahi', [Vacana.Bahu]: 'adikzAmahi' },
    },
  },
  // caṅ-aorist (3.1.48 ṇi-śri-dru-srubhyaḥ kartari caṅ)
  Sri: {
    kind: 'redup', stem: 'SiSri', code: '3.1.48 (ṇi-śri-dru-srubhyaḥ kartari caṅ)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'aSiSriyat' } },
  },
  dru: {
    kind: 'redup', stem: 'dudru', code: '3.1.48 (ṇi-śri-dru-srubhyaḥ kartari caṅ)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'adudruvat' } },
  },
  sru: {
    kind: 'redup', stem: 'susru', code: '3.1.48 (ṇi-śri-dru-srubhyaḥ kartari caṅ)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'asusruvat' } },
  },
  // kṣa-aorist (3.1.45 śala ig-upadhād aniṭaḥ kṣaḥ)
  duha: {
    kind: 'sa', stem: 'duk', code: '3.1.45 (śala ig-upadhād aniṭaḥ kṣaḥ)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'adukzat' } },
  },
  liha: {
    kind: 'sa', stem: 'lik', code: '3.1.45 (śala ig-upadhād aniṭaḥ kṣaḥ)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'alikzat' } },
  },
  // aṅ-aorist (3.1.52 asyati-vakti-khyātibhyo 'ṅ)
  vaca: {
    kind: 'a', stem: 'voc', code: '3.1.52 (asyati-vakti-khyātibhyo \'ṅ), 7.4.20 (vaca um — avocat)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'avocat' } },
  },
  KyA: {
    kind: 'a', stem: 'Kya', code: '3.1.52 (asyati-vakti-khyātibhyo \'ṅ)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'AKyat' } },
  },
  // aṅ-aorist (3.1.56 sarti-śāsty-artibhyaś ca)
  sf: {
    kind: 'a', stem: 'sar', code: '3.1.56 (sarti-śāsty-artibhyaś ca)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'asarat' } },
  },
  SAsu: {
    kind: 'a', stem: 'Siz', code: '3.1.56 (sarti-śāsty-artibhyaś ca)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'aSizat' } },
  },
  f: {
    kind: 'a', stem: 'ar', code: '3.1.56 (sarti-śāsty-artibhyaś ca)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'Arat' } },
  },
  // aṅ-aorist (3.1.55 puṣādi-dyutādy-ḷditaḥ parasmaipadeṣu)
  puza: {
    kind: 'a', stem: 'puz', code: '3.1.55 (puṣādi-dyutādy-ḷditaḥ parasmaipadeṣu)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'apuzat' } },
  },
  dyut: {
    kind: 'a', stem: 'dyut', code: '3.1.55 (puṣādi-dyutādy-ḷditaḥ parasmaipadeṣu)',
    formsP: { [Purusha.Prathama]: { [Vacana.Eka]: 'adyutat' } },
  },
};

/** Passive aorist 3rd singular (bhāve): anāyi, avāci, adāyi. */
const PASSIVE_AORIST: Record<string, SLP1> = {
  ni: 'anAyi', vac: 'avAci', dA: 'adAyi',
};

/** Precative (āśīrliṅ) active forms for bhū. */
const PRECATIVE_P: FormTable = {
  [Purusha.Prathama]: { [Vacana.Eka]: 'BUyAt', [Vacana.Dvi]: 'BUyAstAm', [Vacana.Bahu]: 'BUyAsuH' },
  [Purusha.Madhyama]: { [Vacana.Eka]: 'BUyAH', [Vacana.Dvi]: 'BUyAstam', [Vacana.Bahu]: 'BUyAsta' },
  [Purusha.Uttama]: { [Vacana.Eka]: 'BUyAsam', [Vacana.Dvi]: 'BUyAsva', [Vacana.Bahu]: 'BUyAsma' },
};

/** Precative (āśīrliṅ) middle forms for bhū: bhaviṣīṣṭa, bhaviṣīya, … */
const PRECATIVE_A: FormTable = {
  [Purusha.Prathama]: { [Vacana.Eka]: 'BavizIza', [Vacana.Dvi]: 'BavizIyAstAm', [Vacana.Bahu]: 'BavizIran' },
  [Purusha.Madhyama]: { [Vacana.Eka]: 'BavizIzTAH', [Vacana.Dvi]: 'BavizIyAsthAm', [Vacana.Bahu]: 'BavizIDvam' },
  [Purusha.Uttama]: { [Vacana.Eka]: 'BavizIya', [Vacana.Dvi]: 'BavizIvahi', [Vacana.Bahu]: 'BavizImahi' },
};

/** Secondary (imperfect-like) athematic parasmai endings for the root aorist.
 *  Root aorists take -an in 3pl (not -uḥ, which belongs to sibilant aorists),
 *  and final -s becomes visarga (-H) in 2s. */
const SEC_PARASMAI: Record<Purusha, [string, string, string]> = {
  [Purusha.Prathama]: ['t', 'tAm', 'an'],
  [Purusha.Madhyama]: ['H', 'tam', 'ta'],
  [Purusha.Uttama]: ['m', 'va', 'ma'],
};
/** Thematic (a-aorist) parasmai endings = imperfect endings. */
const THEMATIC_PARASMAI: Record<Purusha, [string, string, string]> = {
  [Purusha.Prathama]: ['t', 'tAm', 'an'],
  [Purusha.Madhyama]: ['H', 'tam', 'ta'],
  [Purusha.Uttama]: ['m', 'Ava', 'Ama'], // 1d/1p -āva/-āma (7.3.x dīrgha)
};
/** Thematic (a-aorist) ātmane endings. */
const THEMATIC_ATMANE: Record<Purusha, [string, string, string]> = {
  [Purusha.Prathama]: ['ata', 'AtAm', 'anta'],
  [Purusha.Madhyama]: ['athAH', 'AthAm', 'advam'],
  [Purusha.Uttama]: ['e', 'Avahe', 'Amahe'],
};
const SEC_ATMANE: Record<Purusha, [string, string, string]> = {
  [Purusha.Prathama]: ['ta', 'tAm', 'anta'],
  [Purusha.Madhyama]: ['thAH', 'AvAm', 'Dvam'],
  [Purusha.Uttama]: ['e', 'vahi', 'mahe'],
};

export interface AoristArgs {
  root: SLP1;
  pada: Pada;
  purusha: Purusha;
  vacana: Vacana;
}

export function aoristKind(root: SLP1): AoristKind | undefined {
  return AORIST[root]?.kind;
}

/** Whether this root has any aorist formation (regular or passive-3s). */
export function hasAorist(root: SLP1): boolean {
  return Boolean(AORIST[root] || PASSIVE_AORIST[root]);
}

export function deriveAorist(args: AoristArgs): Prakriya | undefined {
  // Passive aorist 3s (bhāve) applies to roots without a regular aorist form.
  if (!AORIST[args.root] && args.purusha === Purusha.Prathama &&
      args.vacana === Vacana.Eka && PASSIVE_AORIST[args.root]) {
    const p = new Prakriya([PASSIVE_AORIST[args.root]]);
    p.record('3.2.110 (luN), 3.1.67 (passive aorist 3s)');
    p.collapse();
    return p;
  }
  const entry = AORIST[args.root];
  if (!entry) return undefined;
  const { kind, stem } = entry;
  const idx = args.vacana === Vacana.Eka ? 0 : args.vacana === Vacana.Dvi ? 1 : 2;
  const p = new Prakriya([]);

  // Rare varieties use explicit, verified surface forms.
  const forms = args.pada === Pada.Atmane ? entry.formsA : entry.formsP;
  const explicit = forms?.[args.purusha]?.[args.vacana];
  if (explicit) {
    p.insert(0, explicit, ['form']);
    if (entry.code) p.record(entry.code);
    p.record(`3.2.110 (luN; ${kind}-aorist)`);
    if (args.purusha === Purusha.Prathama && args.vacana === Vacana.Bahu && kind === 's') {
      p.record('3.4.109 (sij-abhyasta-vidibhyaś ca — jus)');
    }
    p.record(`3.4.101 (${kind} endings)`);
    p.collapse();
    return p;
  }

  p.record(entry.code ?? `3.2.110 (luN; ${kind}-aorist)`);
  p.insert(p.length, 'a', ['augment']); // 6.4.71 a-āgama
  p.record('6.4.71 (a-āgama)');

  if (kind === 'a') {
    p.insert(p.length, stem, ['dhatu']);
    let ending = args.pada === Pada.Atmane
      ? THEMATIC_ATMANE[args.purusha][idx]
      : THEMATIC_PARASMAI[args.purusha][idx];
    // 3.4.109: jus (uḥ) for 3p of vid a-aorist
    if (args.root === 'vid' && args.purusha === Purusha.Prathama &&
        args.vacana === Vacana.Bahu && args.pada === Pada.Parasmai) {
      ending = 'uH';
    }
    if (!/[aAiIuUfFxXeEoO]/.test(ending[0] ?? '')) {
      p.insert(p.length, 'a', ['vikarana']); // thematic a (drop before vowel-initial ending)
      p.record('3.1.68 (Sap)');
    } else {
      p.record('6.1.84 (ekādeśa: a+a → a)');
    }
    p.insert(p.length, ending, ['tin']);
    p.record(`3.4.99 (nityaṃ ḍitaḥ), 3.4.100 (itaś ca), 3.4.101 (secondary ending ${ending})`);
  } else {
    p.insert(p.length, stem, ['dhatu']);
    const sibilant = kind === 's' ? 'z' : kind === 'is' ? 'iz' : '';
    if (sibilant) {
      p.insert(p.length, sibilant, ['sibilant']);
      p.record(kind === 's' ? '3.1.43 (cli luṅi), 7.2.1 (sici vṛddhiḥ), 8.2.36 (s → ṣ)' : '3.1.43 (cli luṅi), 3.1.44 (iṣ)');
    }
    const table = args.pada === Pada.Atmane ? SEC_ATMANE : SEC_PARASMAI;
    let ending = table[args.purusha][idx];
    // Root aorist of u-final roots: ū → uv before a vowel-initial ending (3pl -an).
    if (kind === 'root' && /[uU]/.test(stem.slice(-1)) && /^[aA]/.test(ending)) {
      ending = 'v' + ending;
    }
    // sibilant aorists: -īt / -īḥ in 3s/2s active, -uḥ (jus) in 3p (3.4.109)
    if (sibilant && args.pada === Pada.Parasmai && idx === 0 &&
        (args.purusha === Purusha.Prathama || args.purusha === Purusha.Madhyama)) {
      ending = args.purusha === Purusha.Prathama ? 'It' : 'IH';
    }
    if (sibilant && args.pada === Pada.Parasmai &&
        args.purusha === Purusha.Prathama && args.vacana === Vacana.Bahu) {
      ending = 'uH'; // 3.4.109 jus
    }
    p.insert(p.length, ending, ['tin']);
    p.record(`3.4.99 (nityaṃ ḍitaḥ), 3.4.100 (itaś ca), 3.4.101 (secondary ending ${ending})`);
    if (sibilant && args.purusha === Purusha.Prathama && args.vacana === Vacana.Bahu) {
      p.record('3.4.109 (sij-abhyasta-vidibhyaś ca — jus)');
    }
  }

  const { noteUniversal } = require('./core/sutra-notes');
  noteUniversal(p);
  p.collapse();
  return p;
}

/**
 * Precative / benedictive (āśīrliṅ): optative of the aorist with -yāt etc.
 * Active forms for bhū are implemented; the middle is not yet modelled.
 */
export function derivePrecative(args: AoristArgs): Prakriya | undefined {
  if (args.root !== 'BU') return undefined;
  const table = args.pada === Pada.Atmane ? PRECATIVE_A : PRECATIVE_P;
  const form = table[args.purusha]?.[args.vacana];
  if (!form) return undefined;
  const p = new Prakriya([form]);
  p.record('3.1.150 (āśiṣi ca), 3.4.116 (liṇ-āśiṣi / āśīrliṅ precative)');
  const { noteUniversal } = require('./core/sutra-notes');
  noteUniversal(p);
  p.collapse();
  return p;
}
