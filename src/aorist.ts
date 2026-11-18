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
  // root aorist
  BU: { kind: 'root', stem: 'BU' },
  // a-aorist
  pac: { kind: 'a', stem: 'pac' },
  sic: { kind: 'a', stem: 'sic' },
  gam: { kind: 'a', stem: 'gam' },
  // s-aorist of kṛ: akārṣīt (a + kār + ṣ + īt)
  kf: { kind: 's', stem: 'kAr' },
  // a-aorist of bhid: abhidat (3.1.57 vārttika)
  bhid: { kind: 'a', stem: 'bhid', code: '3.1.57 (iritaḥ vā — bhid a-aorist)' },
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
  [Purusha.Uttama]: ['m', 'vaH', 'maH'],
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
    p.record(`3.2.110 (luN; ${kind}-aorist)`);
    p.record(`3.4.101 (${kind} endings)`);
    p.collapse();
    return p;
  }

  p.record(entry.code ?? `3.2.110 (luN; ${kind}-aorist)`);
  p.insert(p.length, 'a', ['augment']); // 6.4.71 a-āgama
  p.record('6.4.71 (a-āgama)');

  if (kind === 'a') {
    p.insert(p.length, stem, ['dhatu']);
    const ending = THEMATIC_PARASMAI[args.purusha][idx];
    if (!/^[aA]/.test(ending)) {
      p.insert(p.length, 'a', ['vikarana']); // thematic a (drop before vowel-initial ending)
      p.record('3.1.68 (Sap)');
    } else {
      p.record('6.1.84 (ekādeśa: a+a → a)');
    }
    p.insert(p.length, ending, ['tin']);
    p.record(`3.4.101 (secondary ending ${ending})`);
  } else {
    p.insert(p.length, stem, ['dhatu']);
    const sibilant = kind === 's' ? 'z' : kind === 'is' ? 'iz' : '';
    if (sibilant) {
      p.insert(p.length, sibilant, ['sibilant']);
      p.record(kind === 's' ? '8.2.36 (s → ṣ)' : '3.1.44 (iṣ)');
    }
    const table = args.pada === Pada.Atmane ? SEC_ATMANE : SEC_PARASMAI;
    let ending = table[args.purusha][idx];
    // Root aorist of u-final roots: ū → uv before a vowel-initial ending (3pl -an).
    if (kind === 'root' && /[uU]/.test(stem.slice(-1)) && /^[aA]/.test(ending)) {
      ending = 'v' + ending;
    }
    // sibilant aorists: -īt / -īḥ in 3s/2s active
    if (sibilant && args.pada === Pada.Parasmai && idx === 0 &&
        (args.purusha === Purusha.Prathama || args.purusha === Purusha.Madhyama)) {
      ending = args.purusha === Purusha.Prathama ? 'It' : 'Ih';
    }
    p.insert(p.length, ending, ['tin']);
    p.record(`3.4.101 (secondary ending ${ending})`);
  }

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
  p.record('3.4.116 (liṇ-āśiṣi / āśīrliṅ precative)');
  p.collapse();
  return p;
}
