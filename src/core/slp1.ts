/**
 * SLP1 (Sanskrit Library Phonetic, basic) utilities.
 *
 * SLP1 maps each Devanagari letter to exactly one ASCII character. All strings
 * that flow through this engine are SLP1 unless stated otherwise.
 *
 * Reference: https://en.wikipedia.org/wiki/SLP1
 */

/** All SLP1 vowels (including anusvāra/visarga/anunāsika markers). */
export const VOWELS = 'aAiIuUfFxXeEoO';
export const VOWEL_MARKERS = 'MH~';

/** Simple (non-diphthong) vowels. */
export const SIMPLE_VOWELS = 'aAiIuUfFxX';

/** Diphthongs. */
export const DIPHTHONGS = 'eEoO';

/** Consonants in traditional varga order. */
export const CONSONANT_VARGIS: readonly string[] = [
  'kKgGN', // velar
  'cCjJY', // palatal
  'wWqQR', // retroflex
  'tTdDn', // dental
  'pPbBm', // labial
];

export const SEMIVOWELS = 'yrlv';
export const FRICATIVES = 'Szsh';
export const CONSONANTS =
  CONSONANT_VARGIS.join('') + SEMIVOWELS + FRICATIVES + 'L';

/** All valid SLP1 characters used by the engine. */
export const SLP1_CHARS = VOWELS + VOWEL_MARKERS + CONSONANTS + "'";

/** Devanagari equivalents (useful for pretty-printing). */
export const SLP1_TO_DEVANAGARI: Readonly<Record<string, string>> = {
  a: 'अ', A: 'आ', i: 'इ', I: 'ई', u: 'उ', U: 'ऊ',
  f: 'ऋ', F: 'ॠ', x: 'ऌ', X: 'ॡ', e: 'ए', E: 'ऐ', o: 'ओ', O: 'औ',
  M: 'ं', H: 'ः', '~': 'ँ', "'": 'ऽ',
  k: 'क', K: 'ख', g: 'ग', G: 'घ', N: 'ङ',
  c: 'च', C: 'छ', j: 'ज', J: 'झ', Y: 'ञ',
  w: 'ट', W: 'ठ', q: 'ड', Q: 'ढ', R: 'ण',
  t: 'त', T: 'थ', d: 'द', D: 'ध', n: 'न',
  p: 'प', P: 'फ', b: 'ब', B: 'भ', m: 'म',
  y: 'य', r: 'र', l: 'ल', v: 'व',
  S: 'श', z: 'ष', s: 'स', h: 'ह', L: 'ळ',
};

export function isVowel(c: string): boolean {
  return c.length === 1 && VOWELS.includes(c);
}

export function isConsonant(c: string): boolean {
  return c.length === 1 && CONSONANTS.includes(c);
}

export function isDiphthong(c: string): boolean {
  return c.length === 1 && DIPHTHONGS.includes(c);
}

/** Guṇa substitutes (Aṣṭādhyāyī 1.1.2 `aṇudīdhṛtasya guṇaḥ`). */
export const GUNA: Readonly<Record<string, string>> = {
  a: 'a', A: 'A',
  i: 'e', I: 'e',
  u: 'o', U: 'o',
  f: 'ar', F: 'ar',
  x: 'al', X: 'al',
  e: 'e', E: 'e',
  o: 'o', O: 'o',
};

/** Vṛddhi substitutes (Aṣṭādhyāyī 1.1.3 `īrāṇau ca vṛddhiḥ`). */
export const VRDDHI: Readonly<Record<string, string>> = {
  a: 'A', A: 'A',
  i: 'E', I: 'E',
  u: 'O', U: 'O',
  f: 'Ar', F: 'Ar',
  x: 'Al', X: 'Al',
  e: 'E', E: 'E',
  o: 'O', O: 'O',
};

/** Last character of a string. */
export function last(s: string): string {
  return s.length ? s[s.length - 1] : '';
}

/** First character of a string. */
export function first(s: string): string {
  return s.length ? s[0] : '';
}

/**
 * Apply guṇa to the final vowel of an SLP1 string.
 * Returns `{ text, changed }`.
 */
export function gunafy(s: string): { text: string; changed: boolean } {
  const c = last(s);
  if (!isVowel(c)) return { text: s, changed: false };
  const g = GUNA[c];
  if (!g || g === c) return { text: s, changed: false };
  return { text: s.slice(0, -1) + g, changed: true };
}

/** Apply vṛddhi to the final vowel of an SLP1 string. */
export function vrddhify(s: string): { text: string; changed: boolean } {
  const c = last(s);
  if (!isVowel(c)) return { text: s, changed: false };
  const v = VRDDHI[c];
  if (!v || v === c) return { text: s, changed: false };
  return { text: s.slice(0, -1) + v, changed: true };
}

/** Lengthen a final short `a` to `A` (7.3.101 `ato dīrgho yañi`). */
export function lengthenFinalA(s: string): { text: string; changed: boolean } {
  if (last(s) === 'a') return { text: s.slice(0, -1) + 'A', changed: true };
  return { text: s, changed: false };
}

/** 6.1.78-style `o + a → av + a` (handled on the final vowel of the left term). */
export function oAtoAv(s: string): string {
  if (last(s) === 'o') return s.slice(0, -1) + 'av';
  return s;
}

/** Dependent vowel signs, used when a vowel follows a consonant. */
const DEPENDENT_VOWEL: Readonly<Record<string, string>> = {
  a: '', A: 'ा', i: 'ि', I: 'ी', u: 'ु', U: 'ू',
  f: 'ृ', F: 'ॄ', x: 'ॢ', X: 'ॣ', e: 'े', E: 'ै', o: 'ो', O: 'ौ',
};

/** Convert SLP1 to Devanagari, handling independent vs dependent vowels. */
export function toDevanagari(s: string): string {
  let out = '';
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (isConsonant(c)) {
      out += SLP1_TO_DEVANAGARI[c] ?? c;
      const next = s[i + 1];
      if (next && VOWELS.includes(next)) {
        out += DEPENDENT_VOWEL[next];
        i++;
      } else if (i === s.length - 1 || (next && CONSONANTS.includes(next))) {
        out += '्'; // virama for a bare final consonant
      }
    } else {
      out += SLP1_TO_DEVANAGARI[c] ?? c;
    }
  }
  return out;
}

/** Validate that a string contains only known SLP1 characters. */
export function isSLP1(s: string): boolean {
  return [...s].every((c) => SLP1_CHARS.includes(c));
}

/**
 * 8.4.1 `raṣābhyāṃ no ṇaḥ samānapade`: within a pada, `n` → `ṇ` (SLP1 `R`)
 * after `r`, `ṣ` (z), or vocalic `ṛ` (f). 8.4.2 allows certain sounds to
 * intervene, but we keep the simple adjacent trigger here.
 */
/**
 * 8.3.23 `mo'nusvāraḥ`: final `m` → anusvāra (M) before a consonant.
 */
export function applyAnusvara(s: string): string {
  return s.replace(/m(?=[kKgGNcCjJYwWqQRtTdDnpPbBmyrlvSzsh])/g, 'M');
}

export function applyNatva(s: string): string {
  // 8.4.2: vowels, h/y/v, gutturals (kKgGN), labials (pPbBm), and anusvāra (M)
  // may intervene between the trigger (r/ṣ/ṛ) and the n.
  const between = '[aAiIuUfFxXeEoOhYyvkKgGNpPbBmM]*'; // y = semivowel ya
  // Do not retroflex an `n` that is followed by `dh` (rundhat, bhinDati):
  // the dh cluster blocks ṇatva in these present-participle stems.
  return s.replace(new RegExp('([rfz])(' + between + ')n(?!dh)', 'g'),
    (_m: string, trigger: string, mid: string) => trigger + mid + 'R');
}
