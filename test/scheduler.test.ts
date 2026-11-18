import test from 'node:test';
import assert from 'node:assert/strict';

import { RuleScheduler, phaseFromCode, scheduled } from '../src/core/scheduler';

test('phaseFromCode implements pūrvatrāsiddham (8.2.1)', () => {
  assert.equal(phaseFromCode('1.3.1'), 'siddha');
  assert.equal(phaseFromCode('7.3.84'), 'siddha');
  assert.equal(phaseFromCode('8.1.68'), 'siddha');
  assert.equal(phaseFromCode('8.2.1'), 'asiddha');
  assert.equal(phaseFromCode('8.3.15'), 'asiddha');
  assert.equal(phaseFromCode('8.4.68'), 'asiddha');
  assert.equal(phaseFromCode('6.1.2'), 'asiddhavat'); // asiddhavat section
  assert.equal(phaseFromCode('6.1.8'), 'siddha'); // just outside it
});

test('scheduler orders by phase then priority, and honours when-conditions', () => {
  const order: string[] = [];
  const scheduler = new RuleScheduler<{ enabled: boolean }>();

  scheduler.add(scheduled('asiddha-low', '8.4.68', 10, () => order.push('asiddha-low')));
  scheduler.add(scheduled('siddha-high', '1.3.1', 20, () => order.push('siddha-high')));
  scheduler.add(scheduled('siddha-low', '3.1.68', 10, () => order.push('siddha-low')));
  scheduler.add(scheduled('conditional', '3.2.123', 15, () => order.push('conditional'), {
    when: (ctx) => ctx.enabled,
  }));

  const report = scheduler.run({ enabled: false });
  assert.deepEqual(order, ['siddha-low', 'siddha-high', 'asiddha-low']);
  assert.ok(report.skipped.includes('conditional'));
  assert.ok(!report.fired.includes('conditional'));

  order.length = 0;
  scheduler.run({ enabled: true });
  assert.deepEqual(order, ['siddha-low', 'conditional', 'siddha-high', 'asiddha-low']);
});
