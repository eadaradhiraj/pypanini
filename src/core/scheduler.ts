/**
 * Condition-based rule scheduler.
 *
 * Pāṇini's rules are not a simple flat list: rules from 8.2.1 onward are
 * `asiddha` with respect to earlier rules (`pūrvatrāsiddham`), and within the
 * `siddha` section `antaranga` rules precede `bahiranga` ones. This module
 * gives rules explicit conditions, phases and priorities so that ordering is
 * data rather than a hard-coded call sequence.
 *
 * The existing tiṅanta pipeline is expressed through this scheduler; see
 * `rules.ts` for the concrete rule definitions.
 */

export type RulePhase = 'siddha' | 'asiddhavat' | 'asiddha';
export type RuleStrength = 'antaranga' | 'bahiranga' | 'neutral';

export interface ScheduledRule<C> {
  /** Unique id (used for debugging / test assertions). */
  id: string;
  /** Sūtra code shown in the trace. */
  code: string;
  description: string;
  phase: RulePhase;
  priority: number;
  strength?: RuleStrength;
  /** If present, the rule fires only when this returns true. */
  when?(ctx: C): boolean;
  /** Mutates the derivation context. Expected to record its own history step. */
  apply(ctx: C): void;
}

/**
 * Derive the phase from a sūtra code. Everything from 8.2.1 onward is
 * `asiddha`; earlier rules are `siddha`.
 */
export function phaseFromCode(code: string): RulePhase {
  const m = code.match(/^(\d+)\.(\d+)\.(\d+)/);
  if (!m) return 'siddha';
  const chapter = Number(m[1]);
  const pada = Number(m[2]);
  const rule = Number(m[3]);
  // 6.1.2–6.1.7 form the "asiddhavat" section: mutually asiddha among themselves
  // but siddha relative to rules outside it.
  if (chapter === 6 && pada === 1 && rule >= 2 && rule <= 7) return 'asiddhavat';
  if (chapter < 8) return 'siddha';
  if (chapter > 8) return 'asiddha';
  return pada > 2 || (pada === 2 && rule >= 1) ? 'asiddha' : 'siddha';
}

export interface ScheduleReport {
  fired: string[];
  skipped: string[];
}

/**
 * Optional hooks that let the scheduler evaluate `when` conditions against a
 * phase-entry snapshot (mutual invisibility). Supply these if any rules in an
 * invisible phase (`asiddhavat` / `asiddha`) declare `when` conditions.
 */
export interface SnapshotHooks<C, S> {
  snapshot(ctx: C): S;
  restore(ctx: C, snap: S): void;
  /** Which phases should use phase-entry snapshots for condition evaluation. */
  invisiblePhases?: readonly RulePhase[];
}

/**
 * A minimal deterministic scheduler: siddha rules first (antaranga before
 * bahiranga within the same priority), then asiddha rules. Conditions are
 * re-checked immediately before each rule fires.
 */
export class RuleScheduler<C> {
  private readonly rules: ScheduledRule<C>[] = [];
  private hooks?: SnapshotHooks<C, unknown>;

  add(rule: ScheduledRule<C>): this {
    this.rules.push(rule);
    return this;
  }

  addAll(rules: readonly ScheduledRule<C>[]): this {
    for (const r of rules) this.add(r);
    return this;
  }

  /** Enable phase-entry snapshots for mutual invisibility. */
  withSnapshots<S>(hooks: SnapshotHooks<C, S>): this {
    this.hooks = hooks as SnapshotHooks<C, unknown>;
    return this;
  }

  run(ctx: C): ScheduleReport {
    const phaseRank = (p: RulePhase) =>
      p === 'siddha' ? 0 : p === 'asiddhavat' ? 1 : 2;
    const strengthRank = (s: RuleStrength | undefined) =>
      s === 'antaranga' ? 0 : s === 'bahiranga' ? 2 : 1;

    const ordered = [...this.rules].sort(
      (a, b) =>
        phaseRank(a.phase) - phaseRank(b.phase) ||
        a.priority - b.priority ||
        strengthRank(a.strength) - strengthRank(b.strength),
    );

    const report: ScheduleReport = { fired: [], skipped: [] };
    const invisible = this.hooks?.invisiblePhases ?? ['asiddhavat', 'asiddha'];
    let phase: RulePhase | undefined;
    // entrySnap = state at the start of the current phase (for conditions)
    // liveSnap  = accumulated state after rules in the phase have fired
    let entrySnap: unknown;
    let liveSnap: unknown;

    for (const rule of ordered) {
      if (rule.phase !== phase) {
        phase = rule.phase;
        if (this.hooks && invisible.includes(phase)) {
          entrySnap = this.hooks.snapshot(ctx);
          liveSnap = entrySnap;
        } else {
          entrySnap = undefined;
          liveSnap = undefined;
        }
      }

      const usesSnapshots = this.hooks && invisible.includes(rule.phase);
      let fires = true;
      if (rule.when) {
        if (usesSnapshots) {
          this.hooks!.restore(ctx, entrySnap); // conditions see phase-entry state
        }
        fires = rule.when(ctx);
        if (usesSnapshots) {
          this.hooks!.restore(ctx, liveSnap); // mutations apply to accumulated state
        }
      }

      if (!fires) {
        report.skipped.push(rule.id);
        continue;
      }
      rule.apply(ctx);
      report.fired.push(rule.id);
      if (usesSnapshots) {
        liveSnap = this.hooks!.snapshot(ctx);
      }
    }
    return report;
  }
}

/** Convenience: build a ScheduledRule from a code + apply function. */
export function scheduled<C>(
  id: string,
  code: string,
  priority: number,
  apply: (ctx: C) => void,
  extra: Partial<ScheduledRule<C>> = {},
): ScheduledRule<C> {
  return {
    id,
    code,
    description: '',
    phase: phaseFromCode(code),
    priority,
    apply,
    ...extra,
  };
}
