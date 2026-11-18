import type { Prakriya } from './prakriya';
import type { KrdantaArgs, SubantaArgs, TinantaArgs } from './types';
import { deriveTinantas } from '../tinanta';
import { deriveKrdantas } from '../krdanta';
import { deriveSubantas } from '../subanta';

/**
 * Public facade, modelled on Vidyut's `Vyakarana`. All textual I/O is SLP1.
 */
export class Vyakarana {
  deriveTinantas(args: TinantaArgs): Prakriya[] {
    return deriveTinantas(args);
  }

  deriveKrdantas(args: KrdantaArgs): Prakriya[] {
    return deriveKrdantas(args);
  }

  deriveSubantas(args: SubantaArgs): Prakriya[] {
    return deriveSubantas(args);
  }
}
