import { Prakriya } from './prakriya';
import { RuleScheduler, phaseFromCode } from './scheduler';
import { applyNatva } from './slp1';
import type { TinantaArgs } from './types';

/** One data-driven transformation of the tiṅ suffix label → surface form. */
export interface SuffixStep {
  code: string;
  from: string;
  to: string;
}

/** Context passed to every rule in the tiṅanta pipeline. */
export interface RuleContext {
  prakriya: Prakriya;
  args: TinantaArgs;
  /** ashtadhyayi.com-style label for the lakāra, e.g. "la~w". */
  lakaraLabel: string;
  /** Label of the tiṅ pratyaya, e.g. "tip". */
  suffixLabel: string;
  /** Label of the vikaraṇa/pratyaya to insert, e.g. "Sap" or "yak". */
  vikaranaLabel: string;
  /** Surface form of the vikaraṇa after it-lopa, e.g. "a" or "ya". */
  vikaranaSurface: string;
  /** Whether to apply guṇa to the root (bhvadi-style sārvadhātuka). */
  doGuna: boolean;
  /** Whether to apply `o + a → av + a` at the root/vikaraṇa boundary. */
  doOAtoAv: boolean;
  /** Whether to apply 7.3.101 dīrgha before m/v-initial suffixes. */
  doDirgha: boolean;
  /** Augment inserted before the root (e.g. `a` for laṅ / lṛṅ). */
  prefix?: string;
  /** Code recorded for the prefix augment. */
  prefixCode?: string;
  /** Material inserted after the root but before the vikaraṇa (e.g. `i` for lṛṭ). */
  postRoot?: string;
  /** Code recorded for the post-root material. */
  postRootCode?: string;
  /** Root transform for perfect-tense reduplication; overrides the default root. */
  rootOverride?: string;
  /** Code recorded for the root transform. */
  rootOverrideCode?: string;
}

/** A rule: optional condition, then mutation of the Prakriya + history step. */
export interface Rule {
  code: string;
  description: string;
  /** Condition evaluated by the scheduler (possibly against a snapshot). */
  when?(ctx: RuleContext): boolean;
  apply(ctx: RuleContext): void;
}

function rule(
  code: string,
  description: string,
  apply: Rule['apply'],
  when?: Rule['when'],
): Rule {
  return { code, description, apply, when };
}

/** Head of the tiṅanta pipeline: root → lakāra → tiṅ suffix. */
export const TINANTA_HEAD_RULES: Rule[] = [
  rule('1.3.1', 'bhūvādayo dhātavaḥ — mark the root as a dhātu', (ctx) => {
    ctx.prakriya.tag(0, 'dhatu');
    ctx.prakriya.record('1.3.1');
  }),

  rule('3.1.1', 'pratyayaḥ paraś ca — affixes are placed after the root', (ctx) => {
    ctx.prakriya.record('3.1.1/3.1.2 (pratyayaḥ paraś ca), 3.1.93 (kṛdatiṅ)');
  }),

  rule('6.4.71 (a-āgama)', 'augment before the root for laṅ / lṛṅ', (ctx) => {
    if (ctx.prefix) {
      ctx.prakriya.insert(0, ctx.prefix, ['augment']);
      ctx.prakriya.record(ctx.prefixCode ?? '6.4.71 (a-āgama)');
    }
  }),

  rule('6.1.8 (abhyāsa)', 'root transform / reduplication for liṭ', (ctx) => {
    if (ctx.rootOverride) {
      const i = ctx.prakriya.findTag('dhatu');
      ctx.prakriya.setText(i, ctx.rootOverride);
      ctx.prakriya.record(ctx.rootOverrideCode ?? '6.1.8 (abhyāsa)');
    }
  }),

  rule('3.2.123', 'lakaara vidhāna — append the lakāra pratyaya', (ctx) => {
    ctx.prakriya.insert(ctx.prakriya.length, ctx.lakaraLabel, ['lakara']);
    ctx.prakriya.record('3.2.123');
  }),

  rule('1.3.2', 'mark the lakāra as an it-affix (no surface change)', (ctx) => {
    ctx.prakriya.record('1.3.2');
  }),

  rule('1.3.3', 'it-saṃjñā on the lakāra (no surface change)', (ctx) => {
    ctx.prakriya.record('1.3.3');
  }),

  rule('1.3.9', 'tasya lopaḥ — drop the it portion of la~w → l', (ctx) => {
    const i = ctx.prakriya.findTag('lakara');
    ctx.prakriya.setText(i, 'l');
    ctx.prakriya.record('1.3.9');
  }, (ctx) => ctx.prakriya.findTag('lakara') >= 0),

  rule('1.3.78', 'l → sārvadhātuka', (ctx) => {
    const i = ctx.prakriya.findTag('lakara');
    ctx.prakriya.tag(i, 'sarvadhatuka');
    ctx.prakriya.record('1.3.78');
  }, (ctx) => ctx.prakriya.findTag('lakara') >= 0),

  rule('3.4.78', 'tiṅ-pratyayas replace the lakāra', (ctx) => {
    const i = ctx.prakriya.findTag('lakara');
    ctx.prakriya.setText(i, ctx.suffixLabel);
    ctx.prakriya.tag(i, 'tin', 'lakara');
    ctx.prakriya.record('3.4.78');
  }, (ctx) => ctx.prakriya.findTag('lakara') >= 0),
];

/** Tail of the pipeline: suffix it-lopa, vikaraṇa, sandhi, consolidation. */
export const TINANTA_TAIL_RULES: Rule[] = [
  rule('3.4.113', 'sārvadhātuka-mark the tiṅ suffix', (ctx) => {
    const i = ctx.prakriya.findTag('tin');
    ctx.prakriya.tag(i, 'sarvadhatuka');
    ctx.prakriya.record('3.4.113');
  }, (ctx) => ctx.prakriya.findTag('tin') >= 0),

  rule('3.1.68', 'insert the vikaraṇa (Sap/yak) before the tiṅ suffix', (ctx) => {
    const i = ctx.prakriya.findTag('tin');
    if (ctx.vikaranaLabel) {
      ctx.prakriya.insert(i, ctx.vikaranaLabel, ['vikarana']);
    }
    ctx.prakriya.record('3.1.68');
  }, (ctx) => ctx.prakriya.findTag('tin') >= 0),

  rule('1.3.9', 'it-lopa on the vikaraṇa', (ctx) => {
    const i = ctx.prakriya.findTag('vikarana');
    ctx.prakriya.setText(i, ctx.vikaranaSurface);
    ctx.prakriya.record('1.3.9');
  }, (ctx) => ctx.prakriya.findTag('vikarana') >= 0),

  rule('3.4.113', 'sārvadhātuka-mark the vikaraṇa', (ctx) => {
    const i = ctx.prakriya.findTag('vikarana');
    ctx.prakriya.tag(i, 'sarvadhatuka');
    ctx.prakriya.record('3.4.113');
  }, (ctx) => ctx.prakriya.findTag('vikarana') >= 0),

  rule('7.3.84', 'sārvadhātukārdhadhātukayoḥ guṇaḥ — guṇa of the root vowel', (ctx) => {
    if (!ctx.doGuna) {
      ctx.prakriya.record('7.3.84');
      return;
    }
    const rootIdx = ctx.prakriya.findTag('dhatu');
    const root = ctx.prakriya.textAt(rootIdx);
    const c = root.slice(-1);
    const gunas: Record<string, string> = {
      i: 'e', I: 'e', u: 'o', U: 'o', f: 'ar', F: 'ar', x: 'al', X: 'al',
    };
    if (gunas[c]) ctx.prakriya.setText(rootIdx, root.slice(0, -1) + gunas[c]);
    ctx.prakriya.record('7.3.84');
  }),

  rule('1.4.14', 'mark the result as an aṅga (no surface change)', (ctx) => {
    const rootIdx = ctx.prakriya.findTag('dhatu');
    if (rootIdx >= 0) ctx.prakriya.tag(rootIdx, 'anga');
    ctx.prakriya.record('1.4.14');
  }),

  rule('6.1.78', 'o + a → av + a (ekādeśa at the root/vikaraṇa boundary)', (ctx) => {
    if (ctx.doOAtoAv) {
      const rootIdx = ctx.prakriya.findTag('dhatu');
      const root = ctx.prakriya.textAt(rootIdx);
      if (root.endsWith('o')) ctx.prakriya.setText(rootIdx, root.slice(0, -1) + 'av');
    }
    ctx.prakriya.record('6.1.78');
  }),

  rule('7.2.35 (iṭ)', 'post-root material (e.g. iṭ before the future vikaraṇa)', (ctx) => {
    if (ctx.postRoot) {
      const rootIdx = ctx.prakriya.findTag('dhatu');
      ctx.prakriya.insert(rootIdx + 1, ctx.postRoot, ['it']);
      ctx.prakriya.record(ctx.postRootCode ?? '7.2.35 (iṭ)');
    }
  }),

  rule('7.3.101', 'ato dīrgho yañi — lengthen final a before m/v-initial suffix', (ctx) => {
    if (ctx.doDirgha) {
      const tinIdx = ctx.prakriya.findTag('tin');
      const stemIdx = tinIdx > 0 ? tinIdx - 1 : 0;
      const stem = ctx.prakriya.textAt(stemIdx);
      const suffix = ctx.prakriya.textAt(tinIdx);
      if (stem.endsWith('a') && /^[mv]/.test(suffix)) {
        ctx.prakriya.setText(stemIdx, stem.slice(0, -1) + 'A');
      }
    }
    ctx.prakriya.record('7.3.101');
  }),

  rule('6.1.84 (ekaḥ pūrvaparayoḥ — ekādeśa)', 'vowel coalescence at the vikaraṇa/suffix boundary', (ctx) => {
    const tinIdx = ctx.prakriya.findTag('tin');
    if (tinIdx > 0) {
      const stem = ctx.prakriya.textAt(tinIdx - 1);
      const suffix = ctx.prakriya.textAt(tinIdx);
      // a + a → a, a + e → e
      if (stem.endsWith('a') && /^[aeA]/.test(suffix)) {
        ctx.prakriya.setText(tinIdx - 1, stem.slice(0, -1));
      }
    }
    ctx.prakriya.record('6.1.84 (ekādeśa: a + a/e/A → a/e/A)');
  }),

  rule('8.4.1', 'raṣābhyāṃ no ṇaḥ — ṇatva after r/ṣ/ṛ within a pada', (ctx) => {
    // Applied at consolidation (8.4.68) where the whole pada is visible — here
    // we only handle ṇatva within a single already-collapsed term.
    let applied = false;
    if (ctx.prakriya.length === 1) {
      const t = ctx.prakriya.terms[0];
      const changed = applyNatva(t.text);
      if (changed !== t.text) { t.text = changed; applied = true; }
    }
    if (applied) ctx.prakriya.record('8.4.1 (ṇatva: n → ṇ after r/ṣ/ṛ)');
  }),

  rule('8.4.68', 'final consolidation', (ctx) => {
    ctx.prakriya.collapse(); // join terms into one pada
    // ṇatva must see the whole pada (may span what were separate terms).
    const t = ctx.prakriya.terms[0];
    const changed = applyNatva(t.text);
    if (changed !== t.text) {
      t.text = changed;
      ctx.prakriya.record('8.4.1 (ṇatva: n → ṇ after r/ṣ/ṛ)');
      ctx.prakriya.collapse();
    }
    ctx.prakriya.record('8.4.68');
  }),
];

/** Apply a data-driven suffix-surface step and record it. */
export function applySuffixStep(prakriya: Prakriya, step: SuffixStep): void {
  const i = prakriya.findTag('tin');
  if (i >= 0 && prakriya.textAt(i) === step.from) {
    prakriya.setText(i, step.to);
  }
  prakriya.record(step.code);
}

/**
 * Run the standard tiṅanta derivation through the condition-based scheduler.
 * Rules are sorted into siddha / asiddha phases (8.2.1 `pūrvatrāsiddham`) and
 * then by priority. The phase split moves the visarga rule (8.3.15) and the
 * final consolidation (8.4.68) to the asiddha phase, which is the Pāṇinian
 * ordering; all other rules remain siddha.
 */
export function runTinantaPipeline(
  prakriya: Prakriya,
  ctx: RuleContext,
  suffixSteps: SuffixStep[],
): Prakriya {
  const scheduler = new RuleScheduler<RuleContext>();

  TINANTA_HEAD_RULES.forEach((r, i) => scheduler.add({
    id: `head-${i}`,
    code: r.code,
    description: r.description,
    phase: phaseFromCode(r.code),
    priority: 10 + i * 10,
    when: r.when,
    apply: r.apply,
  }));

  suffixSteps.forEach((step, i) => scheduler.add({
    id: `suffix-${i}`,
    code: step.code,
    description: `suffix ${step.from} → ${step.to}`,
    phase: phaseFromCode(step.code),
    priority: 100 + i * 10,
    apply: () => applySuffixStep(prakriya, step),
  }));

  TINANTA_TAIL_RULES.forEach((r, i) => scheduler.add({
    id: `tail-${i}`,
    code: r.code,
    description: r.description,
    phase: phaseFromCode(r.code),
    priority: 200 + i * 10,
    when: r.when,
    apply: r.apply,
  }));

  // Enable phase-entry snapshots so that any asiddha/asiddhavat rule's `when`
  // condition sees the state at the start of its phase, not sibling changes.
  scheduler.withSnapshots({
    snapshot: (c) => c.prakriya.snapshot(),
    restore: (c, snap) => c.prakriya.restore(snap),
  });

  scheduler.run(ctx);
  return prakriya;
}
