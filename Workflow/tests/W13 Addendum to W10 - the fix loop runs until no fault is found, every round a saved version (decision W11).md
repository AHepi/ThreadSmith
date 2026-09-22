# W13 Addendum to W10 - the fix loop runs until no fault is found, every round a saved version (decision W11)

*Frozen 22 September 2026, after log W10 and before round 4. Read with W10, W11 and W12. Replaces W11 section 3's "at most three rounds" and section 4's W10.8 consequence; W10.8 stays falsified as written and is not re-read.*

## 1. The owner's rule
Decision W11: keep going until no faults can be found, as long as each completed round is versioned and saved. So:
- **No round cap.** The loop runs until a review returns zero faults of any severity (blocking or wording). A runaway guard of twelve rounds exists in the driver only so that a loop that never converges is reported to the owner rather than run for ever; reaching it is a report, not a stop rule the owner set.
- **One round per run.** Each round is one invocation of the saved workflow `llm-theory-stage-a-fixes.js` (rewritten to run one round from arguments: the round number, the faults per role, the previous review's file); the fixers run in parallel, then the reviewer. Nothing else changes: fixers in the makers' roles, the reviewer verifying by running, the dry run on a corpus document, at most five subagents at a time, no key, nothing sent, writes only under the harness folder.
- **Every completed round is a version.** After each round Claude saves the returns unchanged under `rigs/W10 harness/fix-round returns/round-<n>/`, appends to the tool audit, commits everything under the harness folder with the round in the message, and tags the commit `W10-fix-round-<n>` (rounds 1 to 3, committed together at log W10, carry the tag `W10-fix-rounds-1-3`). A rewind is `git checkout <tag>` of the harness folder.
- **Lessons.** A fault class that recurs across rounds is written into Lessons at the round it is seen recurring (Lesson W6 is the first).

## 2. The rewording count (W3 P3.4)
The count stands as A4 recorded it in the marking plan section 14.4: three fields reworded a second time before any mark existed. It is not re-read. From here: every rewording of any instrument field in the loop is counted per field and per round in the marking plan's addendum sections, so the table is complete when stage B starts; stage B reports agreement on every field reworded twice or more in two ways, over all 96 reports and over the reports no maker or reviewer read while rewording (the file names in the marking plan's sections 13 and 14 and any later section), by program; and A4's stricter rule holds: from the moment stage B begins, any change to any field stops the phase.

## 3. Predictions, as counts that could fail
- **W10.13:** the loop reaches a review with zero faults within twelve rounds. Falsified by the guard being reached; then the owner is told with the per-round fault counts.
- **W10.14:** the per-round count of faults returned does not rise in two consecutive rounds. Falsified if it does; then the round after is a review-only round (no fixer) so the reviewer re-reads its own faults before more code moves, and the owner is told.
- **W10.15:** no round's faults include one the reviewer itself introduced by a forced fix written without a run on the real reports (Lesson W6's class). Falsified by one such fault; it is counted and named.

## 4. Not tested
Nothing is run against a reader. A zero-fault review from one reviewer is one reading; stage B is the first test of the instrument on marks.

## 5. Traps
Stopping at a small fault because it is small; committing a round before its reviewer has returned; a fixer improving what no fault names; a key in the environment.
