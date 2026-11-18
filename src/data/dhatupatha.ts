import { Dhatu, Gana, Pada } from '../core/types';
import { DHATUPATHA_FULL } from './dhatupatha.full';

/**
 * Full Dhātupāṭha: 2,229 roots sourced from ashtadhyayi.com and shared under
 * an MIT license (via https://github.com/ambuda-org/vidyut).
 *
 * Each row is [code, root (SLP1, svara markers stripped), gana, artha].
 * The code uses the ashtadhyayi.com convention (e.g. "01.0001" = bhū).
 */
const FULL: readonly Dhatu[] = DHATUPATHA_FULL.map(([code, text, gana, artha]) => ({
  text,
  gana: gana as Gana,
  pada: Pada.Parasmai, // overridden by an explicit --pada; see PROGRESS.md
  artha,
  code,
}));

export const DHATUPATHA: readonly Dhatu[] = FULL;

/** Quick index: SLP1 root → entries (some roots occur more than once). */
const BY_TEXT = new Map<string, Dhatu[]>();
for (const d of FULL) {
  const list = BY_TEXT.get(d.text) ?? [];
  list.push(d);
  BY_TEXT.set(d.text, list);
}

/** Look up all dhātus with the given SLP1 text. */
export function findDhatus(text: string): readonly Dhatu[] {
  return BY_TEXT.get(text) ?? [];
}

/** Look up the first dhātu with the given SLP1 text. */
export function findDhatu(text: string): Dhatu | undefined {
  return findDhatus(text)[0];
}

/** Search by SLP1 prefix or code (case-sensitive). */
export function searchDhatus(query: string, limit = 50): readonly Dhatu[] {
  return FULL.filter((d) => d.text.startsWith(query) || (d.code ?? '').includes(query)).slice(0, limit);
}

/** Resolve a dhātu argument: a Dhatu object, a known SLP1 root, or a raw root string. */
export function resolveDhatu(input: Dhatu | string, fallbackGana = Gana.Bhvadi): Dhatu {
  if (typeof input !== 'string') return input;
  return (
    findDhatu(input) ?? {
      text: input,
      gana: fallbackGana,
      pada: Pada.Parasmai,
      artha: undefined,
    }
  );
}
