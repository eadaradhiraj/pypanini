import { Prakriya } from './core/prakriya';
import {
  Dhatu,
  Lakara,
  Pada,
  Prayoga,
  Purusha,
  Sanadi,
  TinantaArgs,
  Vacana,
} from './core/types';
import { resolveDhatu } from './data/dhatupatha';
import { deriveTinantas } from './tinanta';

/** The major lakāras shown in a full conjugation table. */
export const PARADIGM_LAKARAS: readonly Lakara[] = [
  Lakara.Lat,   // present
  Lakara.Lan,   // imperfect
  Lakara.Lit,   // perfect
  Lakara.LatN,  // aorist
  Lakara.Lrt,   // future
  Lakara.Lut,   // periphrastic future
  Lakara.Lin,   // optative
  Lakara.Lot,   // imperative
];

export const PURUSHAS: readonly Purusha[] = [Purusha.Prathama, Purusha.Madhyama, Purusha.Uttama];
export const VACANAS: readonly Vacana[] = [Vacana.Eka, Vacana.Dvi, Vacana.Bahu];

export interface ParadigmCell {
  lakara: Lakara;
  pada: Pada;
  purusha: Purusha;
  vacana: Vacana;
  text: string;
  prakriya: Prakriya | undefined;
}

export interface Paradigm {
  dhatu: Dhatu;
  sanadi: Sanadi;
  prayoga: Prayoga;
  cells: ParadigmCell[];
}

/**
 * Generate the full finite-verb paradigm for a dhātu: every major lakāra,
 * both padas, 3 persons × 3 numbers. Cells that the grammar does not produce
 * (e.g. aorist forms for roots without an aorist formation) have an empty text.
 */
export function deriveParadigm(options: {
  dhatu: Dhatu | string;
  sanadi?: Sanadi;
  prayoga?: Prayoga;
  lakaras?: readonly Lakara[];
  padas?: readonly Pada[];
}): Paradigm {
  const dhatu = resolveDhatu(options.dhatu);
  const sanadi = options.sanadi ?? Sanadi.None;
  const prayoga = options.prayoga ?? Prayoga.Kartari;
  const lakaras = options.lakaras ?? PARADIGM_LAKARAS;
  const padas = options.padas ?? [Pada.Parasmai, Pada.Atmane];
  const cells: ParadigmCell[] = [];

  for (const lakara of lakaras) {
    for (const pada of padas) {
      for (const purusha of PURUSHAS) {
        for (const vacana of VACANAS) {
          const args: TinantaArgs = {
            dhatu, lakara, prayoga, pada, purusha, vacana, sanadi,
          };
          const forms = deriveTinantas(args);
          const p = forms[0];
          cells.push({
            lakara, pada, purusha, vacana,
            text: p?.text() ?? '',
            prakriya: p,
          });
        }
      }
    }
  }
  return { dhatu, sanadi, prayoga, cells };
}

/** Render a paradigm as a plain-text table. */
export function formatParadigm(paradigm: Paradigm): string {
  const lines: string[] = [];
  lines.push(`# ${paradigm.dhatu.text} — ${paradigm.prayoga}${paradigm.sanadi !== Sanadi.None ? ` (${paradigm.sanadi})` : ''}`);
  lines.push('');
  const padas = [...new Set(paradigm.cells.map((c) => c.pada))];
  const lakaras = [...new Set(paradigm.cells.map((c) => c.lakara))];
  for (const lakara of lakaras) {
    for (const pada of padas) {
      const subset = paradigm.cells.filter((c) => c.lakara === lakara && c.pada === pada);
      if (subset.length === 0) continue;
      lines.push(`## ${lakara} · ${pada}`);
      lines.push('person    singular        dual            plural');
      for (const purusha of PURUSHAS) {
        const row = VACANAS.map((v) => {
          const cell = subset.find((c) => c.purusha === purusha && c.vacana === v);
          return (cell?.text || '—').padEnd(16);
        });
        lines.push(`${purusha.padEnd(10)}${row.join('')}`);
      }
      lines.push('');
    }
  }
  return lines.join('\n');
}
