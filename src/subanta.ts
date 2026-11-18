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
  [Vibhakti.Caturthi]: ['Ayai', 'AByAm', 'AByaH'],
  [Vibhakti.Pancami]: ['AyAH', 'AByAm', 'AByaH'],
  [Vibhakti.Sasti]: ['AyAH', 'ayoH', 'AnAm'],
  [Vibhakti.Saptami]: ['AyAm', 'ayoH', 'Asu'],
  [Vibhakti.Sambodhana]: ['e', 'e', 'AH'],
};

const I_FEMININE: EndingTable = {
  [Vibhakti.Prathama]: ['I', 'yau', 'yaH'],
  [Vibhakti.Dvitiya]: ['Im', 'yau', 'yIH'],
  [Vibhakti.Trtiya]: ['yA', 'yaByAm', 'yaBiH'],
  [Vibhakti.Caturthi]: ['yAyai', 'yaByAm', 'yaByaH'],
  [Vibhakti.Pancami]: ['yAyAH', 'yaByAm', 'yaByaH'],
  [Vibhakti.Sasti]: ['yAyAH', 'yoH', 'InAm'],
  [Vibhakti.Saptami]: ['yAyAm', 'yoH', 'yAsu'],
  [Vibhakti.Sambodhana]: ['I', 'yau', 'yaH'],
};

const U_FEMININE: EndingTable = {
  [Vibhakti.Prathama]: ['uH', 'U', 'avaH'],
  [Vibhakti.Dvitiya]: ['um', 'U', 'Us'],
  [Vibhakti.Trtiya]: ['vA', 'uByAm', 'uBiH'],
  [Vibhakti.Caturthi]: ['ave', 'uByAm', 'uByaH'],
  [Vibhakti.Pancami]: ['oH', 'uByAm', 'uByaH'],
  [Vibhakti.Sasti]: ['oH', 'voH', 'UnAm'],
  [Vibhakti.Saptami]: ['au', 'voH', 'uzu'],
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

export const STEM_CLASSES: readonly StemClass[] = [
  { id: 'a-m', linga: Linga.Pumsaka, terminal: '', sandhi: true, endings: A_PUMSAKA, matches: (s) => s.endsWith('a') },
  { id: 'a-n', linga: Linga.Napumsaka, terminal: '', sandhi: true, endings: A_NAPUMSAKA, matches: (s) => s.endsWith('a') },
  { id: 'i-m', linga: Linga.Pumsaka, terminal: 'i', sandhi: false, endings: I_PUMSAKA, matches: (s) => s.endsWith('i') },
  { id: 'u-m', linga: Linga.Pumsaka, terminal: 'u', sandhi: false, endings: U_PUMSAKA, matches: (s) => s.endsWith('u') },
  { id: 'i-n', linga: Linga.Napumsaka, terminal: 'i', sandhi: false, endings: I_NAPUMSAKA, matches: (s) => s.endsWith('i') },
  { id: 'u-n', linga: Linga.Napumsaka, terminal: 'u', sandhi: false, endings: U_NAPUMSAKA, matches: (s) => s.endsWith('u') },
  { id: 'A-f', linga: Linga.Stri, terminal: 'A', sandhi: false, endings: A_FEMININE, matches: (s) => s.endsWith('A') },
  { id: 'I-f', linga: Linga.Stri, terminal: 'I', sandhi: false, endings: I_FEMININE, matches: (s) => s.endsWith('I') },
  { id: 'u-f', linga: Linga.Stri, terminal: 'u', sandhi: false, endings: U_FEMININE, matches: (s) => s.endsWith('u') },
  { id: 's-n', linga: Linga.Napumsaka, terminal: 's', sandhi: true, endings: S_NAPUMSAKA, matches: (s) => s.endsWith('s') },
  { id: 'n-m', linga: Linga.Pumsaka, terminal: 'an', sandhi: false, endings: N_MASCULINE, matches: (s) => s.endsWith('an') },
  { id: 't-m', linga: Linga.Pumsaka, terminal: 'at', sandhi: false, endings: T_MASCULINE, matches: (s) => s.endsWith('at') },
  { id: 'f-m', linga: Linga.Pumsaka, terminal: 'f', sandhi: false, endings: R_MASCULINE, matches: (s) => s.endsWith('f') },
  { id: 'an-n', linga: Linga.Napumsaka, terminal: 'an', sandhi: false, endings: N_NAPUMSAKA, matches: (s) => s.endsWith('an') },
  { id: 'at-n', linga: Linga.Napumsaka, terminal: 'at', sandhi: false, endings: T_NAPUMSAKA, matches: (s) => s.endsWith('at') },
];

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
  const cls = classFor(stem, args.linga);
  if (!cls) {
    throw new Error(`unsupported stem class: "${stem}" with linga ${args.linga} (supported: ${STEM_CLASSES.filter(c => c.linga === args.linga).map(c => c.id).join(', ') || 'none'})`);
  }
  const base = cls.terminal ? stem.slice(0, -cls.terminal.length) : stem;
  const ending = cls.endings[args.vibhakti][VACANA_INDEX[args.vacana]] ?? '';
  const surface = cls.sandhi ? applySandhi(base, ending) : base + ending;

  const p = new Prakriya([base]);
  p.record(`4.1.2 (prātipadikād su; ${cls.id})`);

  if (surface !== base) {
    p.setText(0, '');
    p.insert(p.length, surface, ['sup']);
  }
  p.record(`7.1.x (vibhakti ${args.vibhakti}, ${cls.id})`);
  if (ending.includes('H')) p.record('8.3.15 (visarjanīyaḥ)');
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
