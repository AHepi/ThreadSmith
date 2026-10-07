# Agent reports, self-checks and your own write-ups

Use this file whenever an agent (including you) says it checked, verified, fixed, tested or completed something. That covers multi-agent reviews, audit logs, and any report you are about to send.

## Typical claims

- "All 40 files verified."
- "Tests pass."
- "Checked by a reviewer."
- "Done."
- "No errors found."

## Where the falsifiers usually are

- **Q11 Receipts: the log is a claim.** A log line saying "verified" was written by the agent that did the work. It is not evidence the check happened or that it could have failed.
  - Ask for the command and its output.
  - Rerun a sample independently.
  - Check timestamps against when the work was claimed done.
- **Q11 Receipts: claims made before the check finishes.** Never write "checked by X" until X's result is in hand. Then quote it.
- **Q2 Supplied answer: the check that cannot fail.** A test that compares a file with itself, a schema check of output the agent generated from that same schema, a grader shown the expected answer. Run the check on a planted fault, and confirm it catches it.
- **Q5 Worst single case: "all".** Was every item checked, or a sample? Which ones were skipped, timed out or errored and were counted as passing?
- **Q3 Rival: an independent reviewer.** A different agent or person, who did not make the work, with its own access to the raw output.
- **Q10 Order of events: the report written first.** A summary drafted before the results, then filled in, tends to keep its first wording. Compare the summary's claims line by line with the results.
- **Q12 Consequences: what the change touched.** Files, settings or records changed besides the ones reported.
- **Q13 What is counted: what "all" means.** Items that errored, timed out or were skipped and silently dropped from the total. Compare the count checked with the count that exists.

## Your own write-ups

Before a report leaves you, run this:
1. List every sentence that says something was run, checked, fixed or shown.
2. Point each one at its receipt: what was run, and what it printed.
3. Mark anything still running as *pending*.
4. Mark anything not run as *not run*.
5. Remove or soften every strength word that its worst case does not support.

## Mini example

**Claim:** "The agent verified all 40 migration files; the log shows 'OK' for each."

**Missing:**
- The log was written by the migrating agent (Q11).
- Did 'OK' ever print for a broken file (Q2)?
- Were all 40 present in the log (Q5)?

**Next test:** plant one broken file, rerun the check, and see whether it reports a failure. Then have a second agent spot-check 5 files against the source.
