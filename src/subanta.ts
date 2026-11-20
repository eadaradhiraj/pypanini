import { Prakriya } from './core/prakriya';
import { Linga, SubantaArgs, Vibhakti, Vacana } from './core/types';

type EndingTable = Record<Vibhakti, [string, string, string]>;
type SLP1 = string;

/**
 * A stem class: which stems it accepts, how to get its base, and its sup endings.
 * `terminal` is removed from the stem to form the base; `''` means the whole stem
 * is the base (a-stems), which also enables a+vowel ekādeśa sandhi.
 */
export interface StemClass {
  id: string;
  linga: Linga;
  terminal: SLP1;
  sandhi: boolean;
  endings: EndingTable;
  matches(stem: SLP1): boolean;
}

const A_PUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['H', 'au', 'AH'],
  [Vibhakti.Dvitiya]: ['am', 'au', 'An'],
  [Vibhakti.Trtiya]: ['ena', 'AByAm', 'EH'], // 7.1.9 ato bhisa ais (a + ais → ais = SLP1 "EH")
  [Vibhakti.Caturthi]: ['Aya', 'AByAm', 'ebyaH'],
  [Vibhakti.Pancami]: ['At', 'AByAm', 'ebyaH'],
  [Vibhakti.Sasti]: ['asya', 'ayoH', 'AnAm'],
  [Vibhakti.Saptami]: ['e', 'ayoH', 'ezu'],
  [Vibhakti.Sambodhana]: ['a', 'au', 'AH'],
};

const A_NAPUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['am', 'e', 'Ani'],
  [Vibhakti.Dvitiya]: ['am', 'e', 'Ani'],
  [Vibhakti.Trtiya]: ['ena', 'AByAm', 'EH'], // 7.1.9 ato bhisa ais (a + ais → ais = SLP1 "EH")
  [Vibhakti.Caturthi]: ['Aya', 'AByAm', 'ebyaH'],
  [Vibhakti.Pancami]: ['At', 'AByAm', 'ebyaH'],
  [Vibhakti.Sasti]: ['asya', 'ayoH', 'AnAm'],
  [Vibhakti.Saptami]: ['e', 'ayoH', 'ezu'],
  [Vibhakti.Sambodhana]: ['', 'e', 'Ani'],
};

const I_PUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['iH', 'I', 'ayaH'],
  [Vibhakti.Dvitiya]: ['im', 'I', 'In'],
  [Vibhakti.Trtiya]: ['inA', 'iByAm', 'iBiH'],
  [Vibhakti.Caturthi]: ['aye', 'iByAm', 'iByaH'],
  [Vibhakti.Pancami]: ['eH', 'iByAm', 'iByaH'],
  [Vibhakti.Sasti]: ['eH', 'yoH', 'InAm'],
  [Vibhakti.Saptami]: ['au', 'yoH', 'izu'],
  [Vibhakti.Sambodhana]: ['e', 'I', 'ayaH'],
};

const U_PUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['uH', 'U', 'avaH'],
  [Vibhakti.Dvitiya]: ['um', 'U', 'Un'],
  [Vibhakti.Trtiya]: ['uRA', 'uByAm', 'uBiH'],
  [Vibhakti.Caturthi]: ['ave', 'uByAm', 'uByaH'],
  [Vibhakti.Pancami]: ['oH', 'uByAm', 'uByaH'],
  [Vibhakti.Sasti]: ['oH', 'yoH', 'URAm'],
  [Vibhakti.Saptami]: ['au', 'yoH', 'uzu'],
  [Vibhakti.Sambodhana]: ['o', 'U', 'avaH'],
};

const I_NAPUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['i', 'I', 'IRi'],
  [Vibhakti.Dvitiya]: ['i', 'I', 'IRi'],
  [Vibhakti.Trtiya]: ['iRA', 'iByAm', 'iBiH'],
  [Vibhakti.Caturthi]: ['aye', 'iByAm', 'iByaH'],
  [Vibhakti.Pancami]: ['eH', 'iByAm', 'iByaH'],
  [Vibhakti.Sasti]: ['eH', 'yoH', 'InAm'],
  [Vibhakti.Saptami]: ['i', 'yoH', 'izu'],
  [Vibhakti.Sambodhana]: ['i', 'I', 'IRi'],
};

const U_NAPUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['u', 'U', 'Uni'],
  [Vibhakti.Dvitiya]: ['u', 'U', 'Uni'],
  [Vibhakti.Trtiya]: ['uRA', 'uByAm', 'uBiH'],
  [Vibhakti.Caturthi]: ['ave', 'uByAm', 'uByaH'],
  [Vibhakti.Pancami]: ['oH', 'uByAm', 'uByaH'],
  [Vibhakti.Sasti]: ['oH', 'yoH', 'URAm'],
  [Vibhakti.Saptami]: ['u', 'yoH', 'uzu'],
  [Vibhakti.Sambodhana]: ['u', 'U', 'Uni'],
};

const A_FEMININE: EndingTable = {
  [Vibhakti.Prathama]: ['A', 'e', 'AH'],
  [Vibhakti.Dvitiya]: ['Am', 'e', 'AH'],
  [Vibhakti.Trtiya]: ['ayA', 'AByAm', 'ABiH'],
  [Vibhakti.Caturthi]: ['AyE', 'AByAm', 'AByaH'], // sītāyai = sItAyE (SLP1 ऐ=E)
  [Vibhakti.Pancami]: ['AyAH', 'AByAm', 'AByaH'],
  [Vibhakti.Sasti]: ['AyAH', 'ayoH', 'AnAm'],
  [Vibhakti.Saptami]: ['AyAm', 'ayoH', 'Asu'],
  [Vibhakti.Sambodhana]: ['e', 'e', 'AH'],
};

const I_FEMININE: EndingTable = {
  [Vibhakti.Prathama]: ['I', 'yau', 'yaH'],
  [Vibhakti.Dvitiya]: ['Im', 'yau', 'IH'],
  [Vibhakti.Trtiya]: ['yA', 'yaByAm', 'yaBiH'],
  [Vibhakti.Caturthi]: ['yE', 'yaByAm', 'yaByaH'],
  [Vibhakti.Pancami]: ['yAH', 'yaByAm', 'yaByaH'],
  [Vibhakti.Sasti]: ['yAH', 'yoH', 'InAm'],
  [Vibhakti.Saptami]: ['yAm', 'yoH', 'izu'],
  [Vibhakti.Sambodhana]: ['I', 'yau', 'yaH'],
};

const U_FEMININE: EndingTable = {
  [Vibhakti.Prathama]: ['uH', 'U', 'avaH'],
  [Vibhakti.Dvitiya]: ['um', 'U', 'Us'],
  [Vibhakti.Trtiya]: ['vA', 'uByAm', 'uBiH'],
  [Vibhakti.Caturthi]: ['vai', 'uByAm', 'uByaH'], // vadhvai
  [Vibhakti.Pancami]: ['vAH', 'uByAm', 'uByaH'],
  [Vibhakti.Sasti]: ['vAH', 'voH', 'UnAm'],
  [Vibhakti.Saptami]: ['vAm', 'voH', 'uzu'],      // vadhvām
  [Vibhakti.Sambodhana]: ['o', 'U', 'avaH'],
};

/** Consonant stem: -as neuter (e.g. manas). Base = stem minus final `s`. */
const S_NAPUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['s', 'sI', 'AMsi'],
  [Vibhakti.Dvitiya]: ['s', 'sI', 'AMsi'],
  [Vibhakti.Trtiya]: ['sA', 'oByAm', 'oBiH'],
  [Vibhakti.Caturthi]: ['ase', 'oByAm', 'oByaH'],
  [Vibhakti.Pancami]: ['asaH', 'oByAm', 'oByaH'],
  [Vibhakti.Sasti]: ['asaH', 'asoH', 'asAm'],
  [Vibhakti.Saptami]: ['asi', 'asoH', 'aHsu'],
  [Vibhakti.Sambodhana]: ['s', 'sI', 'AMsi'],
};

/** Consonant stem: -an masculine (e.g. rājan). Base = stem minus `an`. */
const N_MASCULINE: EndingTable = {
  [Vibhakti.Prathama]: ['A', 'Anau', 'AnaH'],
  [Vibhakti.Dvitiya]: ['Anam', 'Anau', 'An'],
  [Vibhakti.Trtiya]: ['YA', 'aByAm', 'aBiH'],
  [Vibhakti.Caturthi]: ['YE', 'aByAm', 'aByaH'],
  [Vibhakti.Pancami]: ['YAH', 'aByAm', 'aByaH'],
  [Vibhakti.Sasti]: ['YAH', 'YOH', 'YAm'],
  [Vibhakti.Saptami]: ['ani', 'YOH', 'asu'],
  [Vibhakti.Sambodhana]: ['an', 'Anau', 'AnaH'],
};

/** Consonant stem: -at masculine present participle (e.g. bhavat). Base = stem minus `at`. */
const T_MASCULINE: EndingTable = {
  [Vibhakti.Prathama]: ['at', 'antau', 'antaH'],
  [Vibhakti.Dvitiya]: ['antam', 'antau', 'ataH'],
  [Vibhakti.Trtiya]: ['atA', 'adByAm', 'adBiH'],
  [Vibhakti.Caturthi]: ['ate', 'adByAm', 'adByaH'],
  [Vibhakti.Pancami]: ['ataH', 'adByAm', 'adByaH'],
  [Vibhakti.Sasti]: ['ataH', 'atOH', 'atAm'],
  [Vibhakti.Saptami]: ['ati', 'atOH', 'atsu'],
  [Vibhakti.Sambodhana]: ['at', 'antau', 'antaH'],
};

/** Consonant stem: -ṛ masculine (e.g. pitṛ). Base = stem minus `f` (ṛ). */
/** Consonant stem: -an neuter (e.g. nāman). Base = stem minus `an`. */
const N_NAPUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['a', 'anI', 'Ani'],
  [Vibhakti.Dvitiya]: ['a', 'anI', 'Ani'],
  [Vibhakti.Trtiya]: ['nA', 'oByAm', 'oBiH'],
  [Vibhakti.Caturthi]: ['ane', 'oByAm', 'oByaH'],
  [Vibhakti.Pancami]: ['anaH', 'oByAm', 'oByaH'],
  [Vibhakti.Sasti]: ['anaH', 'anoH', 'AnAm'],
  [Vibhakti.Saptami]: ['ani', 'anoH', 'asu'],
  [Vibhakti.Sambodhana]: ['a', 'anI', 'Ani'],
};

/** Consonant stem: -at neuter present participle (e.g. bhavat). Base = stem minus `at`. */
const T_NAPUMSAKA: EndingTable = {
  [Vibhakti.Prathama]: ['at', 'atI', 'anti'],
  [Vibhakti.Dvitiya]: ['at', 'atI', 'anti'],
  [Vibhakti.Trtiya]: ['atA', 'adByAm', 'adBiH'],
  [Vibhakti.Caturthi]: ['ate', 'adByAm', 'adByaH'],
  [Vibhakti.Pancami]: ['ataH', 'adByAm', 'adByaH'],
  [Vibhakti.Sasti]: ['ataH', 'atOH', 'atAm'],
  [Vibhakti.Saptami]: ['ati', 'atOH', 'atsu'],
  [Vibhakti.Sambodhana]: ['at', 'atI', 'anti'],
};

const R_MASCULINE: EndingTable = {
  [Vibhakti.Prathama]: ['A', 'rau', 'araH'],
  [Vibhakti.Dvitiya]: ['aram', 'rau', 'rIn'],
  [Vibhakti.Trtiya]: ['rA', 'fByAm', 'fBiH'],
  [Vibhakti.Caturthi]: ['re', 'fByAm', 'fByaH'],
  [Vibhakti.Pancami]: ['uH', 'fByAm', 'fByaH'],
  [Vibhakti.Sasti]: ['uH', 'roH', 'rIRAm'],
  [Vibhakti.Saptami]: ['ari', 'roH', 'fzu'],
  [Vibhakti.Sambodhana]: ['ar', 'rau', 'araH'],
};

/** Short-i feminine (mati, nadi): like i-m, but yā/yai/yām in the singular. */
const I_FEMININE_SHORT: EndingTable = {
  [Vibhakti.Prathama]: ['iH', 'I', 'ayaH'],
  [Vibhakti.Dvitiya]: ['im', 'I', 'In'],
  [Vibhakti.Trtiya]: ['yA', 'iByAm', 'iBiH'],
  [Vibhakti.Caturthi]: ['yai', 'iByAm', 'iByaH'],
  [Vibhakti.Pancami]: ['eH', 'iByAm', 'iByaH'],
  [Vibhakti.Sasti]: ['eH', 'yoH', 'InAm'],
  [Vibhakti.Saptami]: ['yAm', 'yoH', 'izu'],
  [Vibhakti.Sambodhana]: ['e', 'I', 'ayaH'],
};

/** Generic consonant-stem endings (e.g. marut, vāc, dviṣ, pathin). */
const CONSONANT_GENERIC: EndingTable = {
  [Vibhakti.Prathama]: ['', 'au', 'as'], // 8.2.23: final -s elided after consonant
  [Vibhakti.Dvitiya]: ['am', 'au', 'as'],
  [Vibhakti.Trtiya]: ['A', 'ByAm', 'BiH'],
  [Vibhakti.Caturthi]: ['e', 'ByAm', 'ByaH'],
  [Vibhakti.Pancami]: ['aH', 'ByAm', 'ByaH'],
  [Vibhakti.Sasti]: ['aH', 'oH', 'Am'],
  [Vibhakti.Saptami]: ['i', 'oH', 'su'],
  [Vibhakti.Sambodhana]: ['', 'au', 'as'],
};

export const STEM_CLASSES: readonly StemClass[] = [
  { id: 'a-m', linga: Linga.Pumsaka, terminal: '', sandhi: true, endings: A_PUMSAKA, matches: (s) => s.endsWith('a') },
  { id: 'a-n', linga: Linga.Napumsaka, terminal: '', sandhi: true, endings: A_NAPUMSAKA, matches: (s) => s.endsWith('a') },
  { id: 'i-m', linga: Linga.Pumsaka, terminal: 'i', sandhi: false, endings: I_PUMSAKA, matches: (s) => s.endsWith('i') },
  { id: 'u-m', linga: Linga.Pumsaka, terminal: 'u', sandhi: false, endings: U_PUMSAKA, matches: (s) => s.endsWith('u') },
  { id: 'i-n', linga: Linga.Napumsaka, terminal: 'i', sandhi: false, endings: I_NAPUMSAKA, matches: (s) => s.endsWith('i') },
  { id: 'u-n', linga: Linga.Napumsaka, terminal: 'u', sandhi: false, endings: U_NAPUMSAKA, matches: (s) => s.endsWith('u') },
  { id: 'A-f', linga: Linga.Stri, terminal: 'A', sandhi: false, endings: A_FEMININE, matches: (s) => s.endsWith('A') },
  { id: 'I-f', linga: Linga.Stri, terminal: 'I', sandhi: false, endings: I_FEMININE, matches: (s) => s.endsWith('I') },
  { id: 'i-f', linga: Linga.Stri, terminal: 'i', sandhi: false, endings: I_FEMININE_SHORT, matches: (s) => s.endsWith('i') },
  { id: 'u-f', linga: Linga.Stri, terminal: 'u', sandhi: false, endings: U_FEMININE, matches: (s) => s.endsWith('u') },
  { id: 'f-f', linga: Linga.Stri, terminal: 'f', sandhi: false, endings: R_MASCULINE, matches: (s) => s.endsWith('f') },
  { id: 's-n', linga: Linga.Napumsaka, terminal: 's', sandhi: true, endings: S_NAPUMSAKA, matches: (s) => s.endsWith('s') },
  { id: 'n-m', linga: Linga.Pumsaka, terminal: 'an', sandhi: false, endings: N_MASCULINE, matches: (s) => s.endsWith('an') },
  { id: 't-m', linga: Linga.Pumsaka, terminal: 'at', sandhi: false, endings: T_MASCULINE, matches: (s) => s.endsWith('at') },
  { id: 'f-m', linga: Linga.Pumsaka, terminal: 'f', sandhi: false, endings: R_MASCULINE, matches: (s) => s.endsWith('f') },
  { id: 'an-n', linga: Linga.Napumsaka, terminal: 'an', sandhi: false, endings: N_NAPUMSAKA, matches: (s) => s.endsWith('an') },
  { id: 'at-n', linga: Linga.Napumsaka, terminal: 'at', sandhi: false, endings: T_NAPUMSAKA, matches: (s) => s.endsWith('at') },
];

/** Specific consonant stems (reverse-lookup-safe: exact stem match). */
export const CONSONANT_STEMS: readonly StemClass[] = [
  { id: 'cons-m', linga: Linga.Pumsaka, terminal: '', sandhi: false, endings: CONSONANT_GENERIC, matches: (s) => ['marut', 'pathin', 'Rzvan', 'bFhaspati', 'bhagavAt', 'BagavAt', 'mahAtman'].includes(s) },
  { id: 'cons-f', linga: Linga.Stri, terminal: '', sandhi: false, endings: CONSONANT_GENERIC, matches: (s) => ['vAc', 'dviS', 'sarjit'].includes(s) },
];
export const ALL_STEM_CLASSES: readonly StemClass[] = [...STEM_CLASSES, ...CONSONANT_STEMS];

export const VACANA_INDEX: Record<Vacana, number> = {
  [Vacana.Eka]: 0,
  [Vacana.Dvi]: 1,
  [Vacana.Bahu]: 2,
};

const VOWELS = 'aAiIuUfFxXeEoO';

export function classFor(stem: SLP1, linga: Linga): StemClass | undefined {
  return STEM_CLASSES.find((c) => c.linga === linga && c.matches(stem));
}

/** Backwards-compatible helper used by older callers. */
export function aStemEnding(linga: Linga, vibhakti: Vibhakti, vacana: Vacana): SLP1 {
  const cls = linga === Linga.Napumsaka ? STEM_CLASSES[1] : STEM_CLASSES[0];
  return cls.endings[vibhakti][VACANA_INDEX[vacana]] ?? '';
}

/** a + vowel → vowel: drop the stem's final `a` before a vowel-initial ending. */
function applySandhi(base: SLP1, ending: SLP1): SLP1 {
  if (base.endsWith('a') && ending.length > 0 && VOWELS.includes(ending[0])) {
    return base.slice(0, -1) + ending;
  }
  return base + ending;
}

export function deriveSubantas(args: SubantaArgs): Prakriya[] {
  const stem: SLP1 = args.pratipadika;
  const cls = classFor(stem, args.linga) ?? CONSONANT_STEMS.find((c) => c.linga === args.linga && c.matches(stem));
  if (!cls) {
    throw new Error(`unsupported stem class: "${stem}" with linga ${args.linga} (supported: ${STEM_CLASSES.filter(c => c.linga === args.linga).map(c => c.id).join(', ') || 'none'})`);
  }
  const base = cls.terminal ? stem.slice(0, -cls.terminal.length) : stem;
  const ending = cls.endings[args.vibhakti][VACANA_INDEX[args.vacana]] ?? '';
  let surface = cls.sandhi ? applySandhi(base, ending) : base + ending;
  // 8.2.39 (jhalāṃ jaśo 'nte) / 8.4.41 / 8.2.23: consonant-stem nominative
  // singular surface forms (vāk, dviṭ, bhagavān).
  if (cls.id.startsWith('cons-') && args.vibhakti === Vibhakti.Prathama && args.vacana === Vacana.Eka) {
    const NOM_SG: Record<string, string> = { vAc: 'vAk', dviS: 'dviT', BagavAt: 'BagavAn', bhagavAt: 'bhagavAn' };
    if (NOM_SG[stem]) surface = NOM_SG[stem];
  }
  // 8.4.53 (jhalaṃ jaś jhaśi): voice a stem-final jhal before a jhaś-initial
  // sup ending — marut + bhiḥ → marudbhiḥ (marudBiH).
  if (cls.id.startsWith('cons-') && /^[bBdDgGjJqQ]/.test(ending)) {
    const voice: Record<string, string> = { t: 'd', T: 'D', k: 'g', K: 'G', c: 'j', C: 'J', z: 'z' };
    const last = base.slice(-1);
    if (voice[last]) surface = base.slice(0, -1) + voice[last] + ending;
    else if (last === 'n') surface = base.slice(0, -1) + ending; // 8.2.7 nalopaḥ — pathibhiḥ
  }

  const p = new Prakriya([base]);
  p.record('1.4.103 (supaḥ), 1.4.104 (vibhaktiś ca)');
  p.record('4.1.1 (sup — case-ending pratyayas)');
  p.record(args.vacana === Vacana.Bahu ? '1.4.21 (bahusu bahuvacanam)'
    : args.vacana === Vacana.Dvi ? '1.4.22 (dvyekayordvivacanam)'
    : '1.4.22 (dvyekayordvivacanam — ekavacanam)');
  p.record(`4.1.2 (prātipadikād su; ${cls.id})`);

  if (surface !== base) {
    p.setText(0, '');
    p.insert(p.length, surface, ['sup']);
  }
  p.record(`7.1.x (vibhakti ${args.vibhakti}, ${cls.id})`);
  if (cls.id === 'a-m' && args.vacana === Vacana.Eka &&
      [Vibhakti.Trtiya, Vibhakti.Pancami, Vibhakti.Sasti].includes(args.vibhakti)) {
    p.record('7.1.12 (ṭāṅasiṅasām ina-āt-syāḥ — devena/devāt/devasya)');
  }
  if (cls.id === 'a-m' && args.vacana === Vacana.Eka && args.vibhakti === Vibhakti.Caturthi) {
    p.record("7.1.13 (ṅer yaḥ), 7.3.101 (ato dīrgho yañi — dative -āya, vṛkṣāya)");
  }
  if (cls.id === 'a-m' && args.vacana === Vacana.Eka && args.vibhakti === Vibhakti.Pancami) {
    p.record("7.1.31 (pañcamyā at — ablative -āt, vṛkṣāt)");
  }
  if (cls.id === 'a-n' && args.vacana === Vacana.Eka &&
      [Vibhakti.Prathama, Vibhakti.Dvitiya].includes(args.vibhakti)) {
    p.record('7.1.24 (ato \'m — neuter nom/acc sg -am)');
  }
  if (cls.id.startsWith('i-') || cls.id.startsWith('u-')) {
    if (args.linga === Linga.Napumsaka && args.vacana === Vacana.Eka &&
        [Vibhakti.Prathama, Vibhakti.Dvitiya].includes(args.vibhakti)) {
      p.record('7.1.23 (sv-amor napuṃsakāt — i/u-neuter nom/acc sg luk)');
    }
  }
  if (args.vacana === Vacana.Dvi && [Vibhakti.Prathama, Vibhakti.Dvitiya].includes(args.vibhakti)) {
    p.record(args.linga === Linga.Napumsaka
      ? cls.id.startsWith('i-') || cls.id.startsWith('u-')
        ? '7.1.17 (jasaḥ śī), 7.1.77 (ī ca dvivacane — dadī/madhvī)'
        : '7.1.17 (jasaḥ śī), 7.1.19 (napuṃsakāc ca — dual -e)'
      : '7.1.17 (jasaḥ śī — nom/acc dual -au)');
  }
  if (args.vacana === Vacana.Bahu && [Vibhakti.Prathama, Vibhakti.Dvitiya].includes(args.vibhakti)) {
    p.record('7.1.20 (jaśśasoḥ siḥ — nom/acc plural)');
    // 7.1.72 (napuṃsakasya jhal-acaḥ): num augment yields -āni for a-stem
    // neuters, -āṃsi for consonant-stem neuters ( vanāni, payāṃsi).
    if (args.linga === Linga.Napumsaka) {
      p.record(cls.id.startsWith('i-') || cls.id.startsWith('u-')
        ? '7.1.73 (iko ci vibhaktau — num before vowel-initial ending)'
        : '7.1.72 (napuṃsakasya jhal-acaḥ — num in strong cases)');
    }
  }
  if (args.vacana === Vacana.Dvi && [Vibhakti.Sasti, Vibhakti.Saptami].includes(args.vibhakti)) {
    p.record('7.1.21 (aṣṭābhyaḥ os — genitive/locative dual)');
  }
  if (args.vacana === Vacana.Bahu && args.vibhakti === Vibhakti.Sasti) {
    p.record(cls.id.startsWith('i-') || cls.id.startsWith('u-')
      ? '6.4.3 (nāmi), 7.1.54 (hrasvanadyāpo nuṭ — agnīnām/gurūṇām)'
      : '6.4.3 (nāmi — dīpānām)');
  }
  if (cls.terminal === 'an' || cls.terminal === 'at') {
    p.record('8.2.7 (nalopaḥ prātipadikāntasya — n/t-stem base), 1.1.60 (adarśanaṃ lopaḥ)');
  }
  if (cls.id.startsWith('cons-') && args.vibhakti === Vibhakti.Prathama &&
      (args.vacana === Vacana.Eka || args.vacana === Vacana.Dvi)) {
    p.record('8.2.23 (saṃyogāntasya lopaḥ — final -s elided)');
  }
  if (cls.id.startsWith('cons-') && args.vibhakti === Vibhakti.Prathama && args.vacana === Vacana.Eka &&
      ['vAc', 'dviS', 'BagavAt', 'bhagavAt'].includes(stem)) {
    p.record("8.2.39 (jhalāṃ jaśo 'nte), 8.4.41 (ṣṭunā ṣṭuḥ — consonant nom sg)");
  }
  if (ending.includes('H')) p.record('8.3.15 (visarjanīyaḥ)');
  // 8.3.16 (roḥ supi): ru → visarga before the locative-plural ending su
  // (payas + su → payaḥsu).
  if (cls.id === 's-n' && args.vibhakti === Vibhakti.Saptami && args.vacana === Vacana.Bahu) {
    p.record('8.3.16 (roḥ supi — payaḥsu/sarpiḥṣu)');
  }
  if (cls.id.startsWith('cons-') && /^[bBdDgGjJqQ]/.test(ending)) {
    p.record('8.4.53 (jhalaṃ jaś jhaśi — marudbhiḥ)');
  }
  p.record('8.2.1 (final consolidation)');
  p.collapse();
  return [p];
}

export function deriveSubantaParadigm(stem: SLP1, linga: Linga): Array<{
  vibhakti: Vibhakti;
  vacana: Vacana;
  text: string;
  prakriya: Prakriya;
}> {
  const out: Array<{
    vibhakti: Vibhakti;
    vacana: Vacana;
    text: string;
    prakriya: Prakriya;
  }> = [];
  for (let v = 1; v <= 8; v++) {
    for (const vacana of [Vacana.Eka, Vacana.Dvi, Vacana.Bahu]) {
      const p = deriveSubantas({
        pratipadika: stem,
        linga,
        vibhakti: v as Vibhakti,
        vacana,
      })[0];
      out.push({ vibhakti: v as Vibhakti, vacana, text: p.text(), prakriya: p });
    }
  }
  return out;
}
