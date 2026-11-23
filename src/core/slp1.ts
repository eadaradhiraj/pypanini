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

/**
 * 6.1.65 (ṇo naḥ): a dhātupāṭha root-initial ṇ (SLP1 `R`) is pronounced n.
 * ṇam → namati. Called on the root stem at the start of derivation.
 */
export function initialNati(root: string): string {
  return root.startsWith('R') ? 'n' + root.slice(1) : root;
}

/**
 * 6.1.64 (dhātvādeḥ ṣaḥ saḥ): a dhātupāṭha root-initial ṣ (SLP1 `z`) becomes s.
 * Applies when z is followed by a vowel or a dental (t/T/d/D/n), or on the
 * five roots smi/svad/svid/svij/svap (the commentary's explicit additions).
 * Exceptions such as ṣṭhiv (zWivu) and ṣvaṣka (zvazka) are left untouched.
 */
export function initialShatva(root: string): string {
  if (!root.startsWith('z')) return root;
  const c = root[1] ?? '';
  const convert = 'aAiIuUfFxXeEoO'.includes(c) || 'tTdDn'.includes(c) ||
    ['zmi', 'zvada', 'zvidA', 'zvija', 'zvap'].includes(root);
  return convert ? 's' + root.slice(1) : root;
}

export function applyNatva(s: string): string {
  // 8.4.2 (aṭkupvāṃ numvyavāye 'pi): vowels (aṭ), gutturals (ku = kKgGN),
  // labial p, nasal m, semivowel v, h/ñ/ya, and anusvāra (M) may intervene
  // between the trigger (r/ṣ/ṛ) and the n. The labial b is NOT on the list,
  // so prabhu + nā → prabhunā, but karman + nā → karmaṇā and guru → guruṇā.
  // 8.4.2 (aṭkupvāṃ numvyavāye 'pi): vowels, gutturals (incl. h), p/v and n/m
  // may intervene between the r/ṣ/ṛ trigger and n.
  const between = '[aAiIuUfFxXeEoOhYyvkKgGNpmvM]*'; // y = semivowel ya
  // Do not retroflex an `n` that is followed by `dh` (rundhat, bhinDati):
  // the dh cluster blocks ṇatva in these present-participle stems.
  return s.replace(new RegExp('([rfz])(' + between + ')n(?!dh)', 'g'),
    (_m: string, trigger: string, mid: string, offset: number, whole: string) => {
      // The `r` of the optative middle 3s/3p ending -ran is part of the tiṅ
      // affix itself, so it does not trigger ṇatva on its own n (bhaveran,
      // paceraṇ → bhaveran; cf. Wiktionary bháveran).
      if (trigger === 'r' && mid === 'a' && offset + _m.length === whole.length) return _m;
      // ṇin (3.1.134 grahādiṣu) has a hard dental n after a root-final r+h
      // cluster: grAh+in → grāhin, never *grāhiṇ (cf. krdanta code note).
      if (trigger === 'r' && mid.includes('h') && offset + _m.length === whole.length) return _m;
      // The n of a following tiṅ ending stays dental after the theme vowel
      // even when a root-final r precedes it: bháranti, smáranti, bhárante
      // (not *bháraṇti / *smáraṇti).  Unlike karman + ā → karmaṇā, the n here
      // begins a tiṅ affix, so 8.4.1 does not cross the vikaraṇa boundary.
      if ((trigger === 'r' || trigger === 'z') &&
          /^[tTdDmvyH]/.test(whole.slice(offset + _m.length))) return _m;
      // ṇatva is blocked when a ṣya- / śya- future marker intervenes (e.g.
      // bhaviṣyanti, kariṣyanti keep the dental n of -nti).
      if (trigger === 'z' && mid.startsWith('y')) return _m;
      // 8.2.1 pūrvatrāsiddham: in a desiderative the ṣ of -ṣa- is produced by
      // a LATER rule (8.4.41 ṣṭunā ṣṭuḥ), so 8.4.1 cannot see it and the n of
      // the following tiṅ ending stays dental: bubhūṣanti, cikīrṣanti,
      // jigamiṣanti, dviṣanti (not *bubhūṣaṇti). The intervening `a` is the
      // theme vowel, and the n begins a tiṅ ending (nti/nta/nth/…).
      if (trigger === 'z' && mid === 'a' &&
          /^[tTdDmvyH]/.test(whole.slice(offset + _m.length))) return _m;
      return trigger + mid + 'R';
    });
}
