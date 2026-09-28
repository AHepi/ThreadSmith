# S108: Part A round 2, who computes. Recorded before any reply was opened

*The orchestrator (Claude), 28 September 2026, after the four replies of round 2 came back (loop ended at 22:40:55Z; all four accepted on pass 1; no key in any output; every sandbox unchanged). No reply had been opened. This record follows the round's rule, "Who does what" and rule 5.*

## Decision

1. **The computing agents are Opus 5.5**, one per section, as the rule sets by default. Sonnet 5.5 takes no computing in this round. The trial of Sonnet 5.5 (decision S53; `results/S108 Part A - Sonnet 5.5 trial/`) has finished its own work, but the Opus review of it had not been written when this was recorded. Giving it analysis before that review would run ahead of the owner's words: "Try Sonnet 5.5 and then review it's output". Whether Sonnet 5.5 computes in later work (Part A round 3, or Part B) is decided once that review is in, and recorded before the replies of that work are opened.
2. **The whole-suite runs are Sonnet harness jobs**, as the rule assigns. The computing agent writes the task spec and does not run the suite itself. The worker and the verifier are Sonnet agents running the harness's scripts. For these mechanical jobs they run as claude-sonnet-5-5, which is reachable here (a probe on 28 September 2026 was served by that model). Any failure or mismatch goes to Opus.
3. **The tabulation, the map and the candidate list, the critical review and the records** are Opus 5.5, as the rule says. Critical reviews go to a fresh Opus agent (decision S42).
