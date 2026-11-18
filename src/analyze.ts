import { SLP1, Vibhakti, Vacana } from './core/types';
import { ALL_STEM_CLASSES, VACANA_INDEX, deriveSubantas } from './subanta';

/** A reverse-lookup result: declined word → prātipadika + case/number/gender. */
export interface SubantaAnalysis {
  word: SLP1;
  /** The reconstructed prātipadika, e.g. "Wrampa" or "agni". */
  pratipadika: SLP1;
  /** The prātipadika without its final vowel, e.g. "Wramp" or "agn". */
  base: SLP1;
  linga: string;
  stemClass: string;
  vibhakti: Vibhakti;
  vacana: Vacana;
  /** The sup-pratyaya that was used. */
  ending: SLP1;
}

const VIBHAKTIS: Vibhakti[] = [
  Vibhakti.Prathama, Vibhakti.Dvitiya, Vibhakti.Trtiya, Vibhakti.Caturthi,
  Vibhakti.Pancami, Vibhakti.Sasti, Vibhakti.Saptami, Vibhakti.Sambodhana,
];
const VACANAS: Vacana[] = [Vacana.Eka, Vacana.Dvi, Vacana.Bahu];
const VOWELS = 'aAiIuUfFxXeEoO';

/** Some SLP1 users write `N` where strict SLP1 uses `n`/`R`. */
function normalize(s: SLP1): SLP1 {
  return s.replace(/N/g, 'n');
}

/**
 * Analyse a declined SLP1 word and reconstruct its base form.
 *
 * Enumerates every stem class and ending, proposes a prātipadika, and verifies it
 * by re-synthesising the word with `deriveSubantas`. Analysis and generation can
 * therefore never disagree. Supported: a-, i-, u-, ā-, ī-stems.
 */
export function analyzeSubanta(word: SLP1): SubantaAnalysis[] {
  const results: SubantaAnalysis[] = [];
  const probe = normalize(word);

  for (const cls of ALL_STEM_CLASSES) {
    for (const vibhakti of VIBHAKTIS) {
      for (const vacana of VACANAS) {
        const ending = cls.endings[vibhakti][VACANA_INDEX[vacana]] ?? '';

        if (ending === '' && !cls.id.startsWith('cons-')) continue; // bare stem too weak; consonant nom/voc sg is valid

        if (!probe.endsWith(ending)) continue;
        const prefix = word.slice(0, word.length - ending.length);
        if (!prefix) continue;

        // Reconstruct the base first (reverse a+vowel ekādeśa if applicable),
        // then re-attach the class terminal to get the prātipadika.
        let base: SLP1;
        if (cls.sandhi && VOWELS.includes(ending[0]) && !prefix.endsWith('a')) {
          base = prefix + 'a';
        } else {
          base = prefix;
        }
        const pratipadika = cls.terminal ? base + cls.terminal : base;

        if (!verify(pratipadika, cls.linga, vibhakti, vacana, word)) continue;

        const reportedBase = cls.terminal
          ? base
          : base.endsWith('a') ? base.slice(0, -1) : base;
        const candidate: SubantaAnalysis = {
          word, pratipadika, base: reportedBase,
          linga: cls.linga, stemClass: cls.id,
          vibhakti, vacana, ending,
        };
        // Keep the strongest (longest) ending per prātipadika+linga+case+number.
        // A weak `H` from a-m must not shadow the strong `iH` from i-m.
        const dupIdx = results.findIndex((r) =>
          r.pratipadika === pratipadika && r.linga === cls.linga &&
          r.vibhakti === vibhakti && r.vacana === vacana);
        if (dupIdx >= 0) {
          if (ending.length > results[dupIdx].ending.length) results[dupIdx] = candidate;
        } else {
          results.push(candidate);
        }
      }
    }
  }

  const strong = results.filter((r) => r.ending.length >= 2);
  const candidates = strong.length > 0 ? strong : results;
  candidates.sort((a, b) =>
    b.ending.length - a.ending.length ||
    a.vibhakti - b.vibhakti ||
    a.pratipadika.length - b.pratipadika.length ||
    a.stemClass.localeCompare(b.stemClass));
  return candidates;
}

function verify(
  pratipadika: SLP1,
  linga: string,
  vibhakti: Vibhakti,
  vacana: Vacana,
  word: SLP1,
): boolean {
  try {
    const generated = deriveSubantas({
      pratipadika,
      linga: linga as import('./core/types').Linga,
      vibhakti,
      vacana,
    })[0].text();
    return normalize(generated) === normalize(word);
  } catch {
    return false;
  }
}

const VIBHAKTI_NAMES: Record<Vibhakti, { sanskrit: string; english: string }> = {
  [Vibhakti.Prathama]: { sanskrit: 'prathamā', english: 'nominative' },
  [Vibhakti.Dvitiya]: { sanskrit: 'dvitīyā', english: 'accusative' },
  [Vibhakti.Trtiya]: { sanskrit: 'tṛtīyā', english: 'instrumental' },
  [Vibhakti.Caturthi]: { sanskrit: 'caturthī', english: 'dative' },
  [Vibhakti.Pancami]: { sanskrit: 'pañcamī', english: 'ablative' },
  [Vibhakti.Sasti]: { sanskrit: 'ṣaṣṭhī', english: 'genitive' },
  [Vibhakti.Saptami]: { sanskrit: 'saptamī', english: 'locative' },
  [Vibhakti.Sambodhana]: { sanskrit: 'sambodhana', english: 'vocative' },
};

const VACANA_NAMES: Record<Vacana, string> = {
  [Vacana.Eka]: 'singular (eka)',
  [Vacana.Dvi]: 'dual (dvi)',
  [Vacana.Bahu]: 'plural (bahu)',
};

/** Human-readable one-line description of an analysis result. */
export function describeAnalysis(a: SubantaAnalysis): string {
  const v = VIBHAKTI_NAMES[a.vibhakti];
  return `base ${a.base}  |  prātipadika ${a.pratipadika}  |  ${v.sanskrit} (${v.english}), ${VACANA_NAMES[a.vacana]}, ${a.linga} (${a.stemClass})  |  ending ${a.ending}`;
}
