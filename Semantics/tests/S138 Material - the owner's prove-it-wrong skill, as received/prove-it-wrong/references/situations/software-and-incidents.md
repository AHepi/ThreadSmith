# Software, bugs and incidents

Use this file for root causes, fixes, flaky tests, performance claims, post-mortems, "works on my machine", and migrations.

## Typical claims

- "X caused the outage."
- "The fix works."
- "The test is no longer flaky."
- "It is 3× faster."
- "The migration lost no data."

## Where the falsifiers usually are

- **Q6 Premise match: removal changes more than one thing.** Turning off a cache, a flag or a thread pool also changes timing, load and memory. The falsifier: keep the suspect on and remove only the suspected mechanism, or reproduce the mechanism alone (inject the race).
- **Q9 Draws and size: the base rate.** "Zero failures in N runs" means nothing until the same N runs without the change are known to fail. Work out how many runs would be expected to show at least one failure at the old rate.
- **Q3 Rival: other recent changes.** Deploys, dependency bumps, config changes and traffic shifts in the same window. The falsifier: the symptom appears without the suspect, or disappears without the fix.
- **Q12 Consequences: what the fix gives up.** A retry can hide real errors. Removing a cache costs speed. A timeout can hide deadlocks. The falsifier: a deliberately injected real error still passes.
- **Q5 Worst single case: tails, not means.** "Faster on average" can hide a slower worst case, or a slower path for one class of input. Report percentiles and the worst class.
- **Q1 Scope: the test environment against production.** Data size, concurrency, hardware, versions. Name the differences and say which could matter.
- **Q11 Receipts: green ticks.** A CI pass that skipped the test, a log line written by the fix, a dashboard that sampled. Trace each to the run.

## Mini example

**Claim:** "The memory leak is fixed: memory stayed flat for 2 hours after the patch."

**Missing:**
- Did memory grow within 2 hours before the patch, under the same load (Q9)?
- Was the load the same (Q6)?
- Does the leak's path still run (Q7)?

**Next test:** the old build under the same 2-hour load. If its memory also stays flat, the 2 hours show nothing.
