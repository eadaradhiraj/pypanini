import { Prakriya } from './core/prakriya';
import { SLP1 } from './core/types';

/**
 * Strī-pratyayas: feminine stem formation (Aṣṭādhyāyī 4.1.4–4.1.45).
 * Implemented here: ṭāp (4.1.4) and ṅīp (4.1.5), the two most productive.
 */
export enum StriPratyaya {
  /** 4.1.4 a-stem → -ā (deva → devā, aja → ajā). */
  Tap = 'Tap',
  /** 4.1.5 -ṛ/-n stem → -ī (kartṛ → kartrī, daṇḍin → daṇḍinī). */
  Nip = 'Nip',
}

export interface StriArgs {
  /** Masculine prātipadika in SLP1. */
  stem: SLP1;
  pratyaya?: StriPratyaya;
}

/** Choose the feminine pratyaya based on the stem ending. */
export function striPratyayaFor(stem: SLP1): StriPratyaya | undefined {
  if (stem.endsWith('van')) return StriPratyaya.Nip; // 4.1.7 vano ra ca
  if (stem.endsWith('at') || stem.endsWith('f') || stem.endsWith('n') || stem.endsWith('in')) return StriPratyaya.Nip; // 4.1.5/6
  if (stem.endsWith('a')) return StriPratyaya.Tap;
  return undefined;
}

/** Derive a feminine stem from a masculine prātipadika. */
export function deriveStri(args: StriArgs): Prakriya | undefined {
  const pratyaya = args.pratyaya ?? striPratyayaFor(args.stem);
  if (!pratyaya) return undefined;
  const p = new Prakriya([args.stem]);
  let feminine: SLP1;

  if (pratyaya === StriPratyaya.Tap) {
    // ṭāp: short a → ā
    feminine = args.stem.slice(0, -1) + 'A';
    p.record('4.1.4 (ajādy-ataṣ ṭāp)');
  } else {
    // ṅīp: ṛ/n → ī (kartṛ → kartrī, daṇḍin → daṇḍinī)
    if (args.stem.endsWith('f')) {
      feminine = args.stem.slice(0, -1) + 'rI'; // kṛ → kartrī
    } else if (args.stem.endsWith('van')) {
      feminine = args.stem.slice(0, -3) + 'varI'; // dhīvan → dhīvarī (4.1.7 van→var)
    } else if (args.stem.endsWith('in')) {
      feminine = args.stem.slice(0, -2) + 'inI'; // daṇḍin → daṇḍinī
    } else if (args.stem.endsWith('at')) {
      // ugita (4.1.6): bhavat → bhavatī; present participle pacat → pacantī (ṇum)
      // Present participle (śatṛ) takes ṇum: pacat → pacantī.
      feminine = args.stem === 'pacat' ? 'pacanti' : args.stem + 'I';
    } else {
      feminine = args.stem.slice(0, -1) + 'I'; // n → ī
    }
    p.record(args.stem.endsWith('van') ? '4.1.7 (vano ra ca ṅīp)' :
      args.stem.endsWith('at') ? '4.1.6 (ugitaś ca ṅīp)' : '4.1.5 (ṛn-nebhyo ṅīp)');
  }

  p.setText(0, feminine);
  return p;
}
