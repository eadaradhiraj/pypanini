import test from 'node:test';
import assert from 'node:assert/strict';

import { RuleScheduler, scheduled } from '../src/core/scheduler';

/** A tiny counter "derivation" used to demonstrate mutual invisibility. */
interface Ctx {
  /** The live accumulated value. */
  value: number;
  /** History of fired rule ids. */
  log: string[];
}

function snapshot(ctx: Ctx): number {
  return ctx.value;
}
function restore(ctx: Ctx, snap: number): void {
  ctx.value = snap;
}

test('asiddhavat rules with when-conditions see the phase-entry state', () => {
  const scheduler = new RuleScheduler<Ctx>().withSnapshots({ snapshot, restore });

  // Rule A (siddha): sets value to 1.
  scheduler.add(scheduled('a', '1.1.1', 10, (ctx) => { ctx.value = 1; ctx.log.push('a'); }));

  // Rule B (asiddhavat): fires only if value === 0 (i.e. ignores rule A's change).
  // With phase-entry snapshots, B sees the value at the start of the asiddhavat
  // phase, which is still 1 here — so decide the condition against a fixed value.
  scheduler.add(scheduled('b', '6.1.2', 10, (ctx) => { ctx.value += 10; ctx.log.push('b'); }, {
    when: (ctx) => ctx.value === 1, // entry state has value 1 despite any sibling changes
  }));

  // Rule C (asiddhavat): also checks the entry state (value === 1), and adds 20.
  // It must NOT see B's +10.
  scheduler.add(scheduled('c', '6.1.3', 20, (ctx) => { ctx.value += 20; ctx.log.push('c'); }, {
    when: (ctx) => ctx.value === 1,
  }));

  // Mutate B's effect so we can verify C still uses the entry snapshot: if C
  // were seeing accumulated state it would see 11 and be skipped.
  const ctx: Ctx = { value: 0, log: [] };
  const report = scheduler.run(ctx);

  assert.ok(report.fired.includes('a'));
  assert.ok(report.fired.includes('b'));
  assert.ok(report.fired.includes('c'));
  // Accumulated: B adds 10 to live state (1) => 11; C adds 20 to live state => 31.
  assert.equal(ctx.value, 31);
  assert.deepEqual(ctx.log, ['a', 'b', 'c']);
});

test('without snapshots, a later rule sees accumulated state', () => {
  const scheduler = new RuleScheduler<Ctx>(); // no snapshots
  scheduler.add(scheduled('a', '1.1.1', 10, (ctx) => { ctx.value = 1; }));
  scheduler.add(scheduled('b', '6.1.2', 10, (ctx) => { ctx.value += 10; }, {
    when: (ctx) => ctx.value === 1, // sees a's change (value is 1, not 0)
  }));
  const ctx: Ctx = { value: 0, log: [] };
  const report = scheduler.run(ctx);
  assert.ok(report.fired.includes('b'));
  assert.equal(ctx.value, 11);
});
