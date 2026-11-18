/** Sūtra coverage tracking: classify all 3,984 sūtras and report implementation status. */
import { SUTRAS } from './data/sutras';

export type Topic =
  | 'definitions' | 'subanta' | 'krdanta' | 'tinanta'
  | 'namadhatu' | 'upasarga' | 'sandhi'
  | 'taddhita' | 'samasa' | 'accent' | 'other';

export function topicOf(code: string): Topic {
  const [a, p] = code.split('.').map(Number);
  if (a === 1) return 'definitions';
  if (a === 2) return 'samasa';
  if (a === 3 && p === 1) return 'namadhatu';
  if (a === 3 && (p === 2 || p === 3 || p === 4)) return 'krdanta';
  if (a === 4 && p === 1) return 'subanta';
  if (a === 4 || a === 5) return 'taddhita';
  if (a === 6 || a === 8) return 'sandhi';
  if (a === 7) return 'subanta';
  return 'other';
}

/** Topics in the user's declared focus. */
export const FOCUS_TOPICS: readonly Topic[] = [
  'definitions', 'subanta', 'krdanta', 'tinanta', 'namadhatu', 'upasarga', 'sandhi',
];

export interface CoverageReport {
  byTopic: Map<Topic, { total: number; implemented: number }>;
  implemented: Set<string>;
  total: number;
  focusTotal: number;
  focusImplemented: number;
}

/**
 * Build a coverage report. `usedCodes` is the set of sūtra codes the engine
 * actually emits/recognises (caller supplies it from source scanning or a registry).
 */
export function buildCoverage(usedCodes: ReadonlySet<string>): CoverageReport {
  const byTopic = new Map<Topic, { total: number; implemented: number }>();
  let focusTotal = 0, focusImplemented = 0;
  for (const [code] of SUTRAS) {
    if (code === 'code') continue;
    const t = topicOf(code);
    const e = byTopic.get(t) ?? { total: 0, implemented: 0 };
    e.total++;
    const hit = usedCodes.has(code);
    if (hit) e.implemented++;
    byTopic.set(t, e);
    if (FOCUS_TOPICS.includes(t)) {
      focusTotal++;
      if (hit) focusImplemented++;
    }
  }
  return {
    byTopic,
    implemented: new Set(usedCodes),
    total: SUTRAS.length - 1,
    focusTotal,
    focusImplemented,
  };
}

export function formatCoverage(r: CoverageReport): string {
  const lines: string[] = ['Sūtra coverage by topic (implemented / total):'];
  for (const [t, e] of [...r.byTopic].sort((a, b) => a[0].localeCompare(b[0]))) {
    const focus = FOCUS_TOPICS.includes(t) ? '*' : ' ';
    lines.push(` ${focus}${t.padEnd(12)} ${String(e.implemented).padStart(4)} / ${String(e.total).padEnd(4)}  ${(100 * e.implemented / e.total).toFixed(1)}%`);
  }
  lines.push(`\nFocus topics: ${r.focusImplemented} / ${r.focusTotal}`);
  lines.push(`All sūtras:   ${r.implemented.size} / ${r.total}`);
  lines.push('(* = in declared focus)');
  return lines.join('\n');
}
