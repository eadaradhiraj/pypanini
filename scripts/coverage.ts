/**
 * Sūtra coverage report: classify all 3,984 Aṣṭādhyāyī sūtras by focus topic
 * and check which are represented in the engine (emitted as trace codes) or
 * backed by bundled auxiliary data.
 *
 * Run: npx ts-node scripts/coverage.ts  (or compile then node dist/scripts/coverage.js)
 */
import { SUTRAS } from '../src/data/sutras';
import { DHATUPATHA_GANASUTRAS_TSV } from '../src/data/dhatupatha_ganasutras';
import { UNADIPATHA_TSV } from '../src/data/unadipatha';
import { VARTTIKAS_TSV } from '../src/data/varttikas';
import * as fs from 'fs';
import * as path from 'path';

type Topic = 'definitions' | 'subanta' | 'krdanta' | 'tinanta' | 'namadhatu' | 'upasarga' | 'sandhi' | 'taddhita' | 'samasa' | 'accent' | 'other';

function topic(code: string): Topic {
  const c = code.split('.').map(Number);
  const [a, p] = c;
  if (a === 1) return 'definitions';
  if (a === 3 && p === 1) return 'namadhatu';
  if (a === 3 && (p === 2 || p === 3 || p === 4)) return 'krdanta';
  if (a === 3 && p >= 2) return 'tinanta';
  if (a === 4 && p === 1) return 'subanta';
  if (a === 4 || a === 5) return 'taddhita';
  if (a === 6 || a === 8) return 'sandhi';
  if (a === 7) return 'subanta'; // vibhakti-sthāne-guna etc.
  if (a === 2) return 'samasa';
  return 'other';
}

// Codes actually emitted in engine logic (grep of src excluding data/).
function collectUsedCodes(): Set<string> {
  const used = new Set<string>();
  const dirs = [path.join(process.cwd(), 'src')];
  const walk = (d: string) => {
    for (const f of fs.readdirSync(d)) {
      const fp = path.join(d, f);
      const st = fs.statSync(fp);
      if (st.isDirectory()) {
        if (f === 'data') continue;
        walk(fp);
      } else if (f.endsWith('.ts')) {
        const txt = fs.readFileSync(fp, 'utf8');
        for (const m of txt.matchAll(/\b([1-8]\.[1-4]\.\d+)\b/g)) used.add(m[1]);
      }
    }
  };
  dirs.forEach(walk);
  return used;
}

const used = collectUsedCodes();
const byTopic = new Map<Topic, { total: number; used: number }>();
for (const [code] of SUTRAS) {
  if (code === 'code') continue;
  const t = topic(code);
  const e = byTopic.get(t) ?? { total: 0, used: 0 };
  e.total++;
  if (used.has(code)) e.used++;
  byTopic.set(t, e);
}

console.log('Sūtra coverage by topic (used codes / total sūtras in topic):');
for (const [t, e] of [...byTopic].sort((a, b) => a[0].localeCompare(b[0]))) {
  console.log(`  ${t.padEnd(12)} ${String(e.used).padStart(4)} / ${String(e.total).padEnd(4)}  ${(100 * e.used / e.total).toFixed(1)}%`);
}
console.log(`\nTotal used codes: ${used.size}`);
console.log(`Auxiliary data: ${DHATUPATHA_GANASUTRAS_TSV.length - 1} gaṇasūtras, ${UNADIPATHA_TSV.length - 1} uṇādi, ${VARTTIKAS_TSV.length - 1} vārttikas bundled`);
