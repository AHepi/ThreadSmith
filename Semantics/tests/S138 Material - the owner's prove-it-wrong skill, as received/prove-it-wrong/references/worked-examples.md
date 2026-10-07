# Worked examples

There are three complete runs:
1. Review mode: a planner benchmark, where several conditions were missing.
2. Review mode: a "fixed" flaky test, where the fix was never shown to work.
3. Claimant mode: a well-tested claim, where almost nothing was missing.

Each ledger passes `scripts/check_ledger.py`. To check one, copy that example alone into a file.

---

## Example 1. A planner benchmark (review mode)

C1. "Learned persistent memory makes planning more efficient: 9 exact checks against 12 for fixed order, on our 8-case benchmark."
C2. "The exact check **guarantees** every chosen program reaches the goal."
Source: the engineer's viability report, "Verdict" section.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C2 | In at least one of three scenes whose physics lies outside the supplied model list, the planner answers a confident yes that turns out wrong | missing | none | C2 held only while the world obeys a supplied model |
| F2 | C1 | A ranker using the same two force totals with no learning (plain Newton) also needs 9 or fewer checks on the 8 cases | blocked | the engineer can add it as a sixth arm on the existing benchmark; C1's credit stands if it needs 11 or more | credit to "learned" unmeasured; C1 holds for "the supplied totals", held if F2 loses |
| F3 | C1 | The zero-numbers arm and the least-effort arm order options differently on at least one case | survived | worked out from the stated ranking rule: a zero readout predicts no motion everywhere, so ordering falls to effort then input order; the report's rows are identical | five arms counted as four |
| F4 | C1 | Across 5 fresh draws of the five training lessons, the gain over fixed order falls to 1 check or less | missing | none | C1 held for one lesson draw only |
| F5 | C1 | Case by case, memory beats fixed order in no more cases than chance would give | survived | counted from the report's table: 4 wins, 1 loss, 3 ties; two-sided sign test p = 0.375 | C1 reported as "on these 8 cases", not as general |
| F6 | C2 | Planner forecasts differ from an independent enumeration by the checker on at least one candidate | reported | report: "Every attempted planner forecast exactly matched its independent enumeration"; not rerun by us | none, as reported |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | missing | F4: one benchmark, one lesson draw |
| Q1 | C2 | missing | F1 |
| Q2 | C1 | missing | F2: the totals are momentum and displacement times mass, supplied |
| Q2 | C2 | covered | F6: the checker's family is declared as supplied, and the guarantee is stated as conditional on it |
| Q3 | C1 | missing | F2 |
| Q3 | C2 | does not apply | C2 makes no comparative or credit statement about a rival |
| Q4 | C1 | covered | F3: two arms identical by construction; checks and first-try are one measurement |
| Q4 | C2 | covered | F6: forecasts compared with a separate enumeration, as reported |
| Q5 | C1 | covered | F5: counted case by case; 4 wins, 1 loss, 3 ties, so reported as "on these 8 cases" |
| Q5 | C2 | covered | report: "40/40 supported selections", case by case |
| Q6 | all | covered | all arms ran on identical lessons, goals and programs, as reported |
| Q7 | C1 | covered | worked out: the claim is about ordering efficiency, and the evidence counts checks, so it is the same question |
| Q7 | C2 | missing | F1: "guarantees" is shown only inside the family |
| Q8 | C1 | missing | F4: never met a start not at rest, contact, or varying weight |
| Q8 | C2 | missing | F1 |
| Q9 | C1 | missing | F4, F5: one lesson draw; 8 cases |
| Q9 | C2 | covered | report: "complete physical witnesses for 18/18 trajectories" |
| Q10 | all | covered | report: "The prospective contract was written before the V2 experiment" |
| Q11 | C1 | covered | F3, F5: worked out and counted by us from the report's tables |
| Q11 | C2 | covered | F6: reported, not rerun by us |
| Q12 | C1 | covered | the ordering also decides which workable program is chosen; report table, "Total selected force effort": 88 against 96 |
| Q12 | C2 | missing | F1: a wrong yes would be acted on |
| Q13 | all | covered | all 8 cases counted; error pooled over 672 coordinates, half from a still circle every method gets right, noted |

**Claim as it stands:** on these 8 cases, with one lesson draw, the supplied force totals with 16 learned numbers ordered candidates so that 3 fewer exact checks were needed than fixed order. Every chosen program reaches the goal *held if* the world obeys a supplied model.

**Next test:** run the existing benchmark on three new scenes whose physics lies outside the supplied model list (F1). It needs only new scenes.

---

## Example 2. "The flaky test is fixed" (review mode)

C1. "Fixed the flaky checkout test by adding a retry around the payment mock: it passed 50 times in a row after the change."
Source: pull-request description.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | The old code, run 50 times on the same machine, also passes all 50 runs | missing | none | C1 held if the test failed often enough before the change for 50 passes to mean something |
| F2 | C1 | With the retry present and the payment mock's timing fault injected on purpose, the test still fails at least once in 50 runs | missing | none | C1 narrowed to "the retry hides the fault", not a fix |
| F3 | C1 | A deliberately broken payment call still passes the test with the retry in place | missing | none | C1 held if the retry cannot swallow a real failure |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | missing | F2: only ordinary CI timing was tried |
| Q2 | C1 | does not apply | nothing supplied beyond the code and the test itself |
| Q3 | C1 | missing | F1: the rival "nothing changed" was not run |
| Q4 | C1 | does not apply | only one arm and one measure in this claim |
| Q5 | C1 | covered | description: "CI runs 1 to 50 linked below", each listed individually |
| Q6 | C1 | missing | F1: before and after ran on different days and machines |
| Q7 | C1 | missing | F2: "passes" is shown, "fault removed" is not |
| Q8 | C1 | does not apply | nothing in the claim was fitted, learned or tuned |
| Q9 | C1 | missing | F1: the old failure rate is unknown, so 50 passes cannot be weighed |
| Q10 | C1 | covered | ticket, dated before the change: "close after 50 consecutive passes" |
| Q11 | C1 | covered | description: "CI runs 1 to 50 linked below"; links open to green runs |
| Q12 | C1 | missing | F3: a retry can hide real failures |
| Q13 | C1 | covered | all 50 runs counted, none skipped or retried away, per the CI history |

**Claim as it stands:** after the change, the test passed 50 CI runs in a row. Whether the change removed the fault is unknown.

**Next test:** run the old code 50 times on the same machine (F1). If it also passes 50 times, the 50 passes say nothing.

---

## Example 3. A well-tested claim (claimant mode)

C1. "The new date parser reads every timestamp in our 2023 to 2025 log archive identically to the reference library."
Source: release notes, "Parser" section, written by us.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | At least one timestamp in the archive is read differently by the new parser and the reference library | survived | ran compare_all.py over all 41,207,113 timestamps; printed "0 differences"; output in runs/compare_2025-09-30.txt | none |
| F2 | C1 | At least one of 2,000,000 generated strings in the archive's formats, including leap days and offsets, is read differently | survived | ran fuzz_dates.py with the saved seed list; printed "0 differences" | none |
| F3 | C1 | A colleague who did not write the parser reruns the full comparison on another machine and finds at least one difference | survived | rerun by a second engineer; their output runs/compare_rerun.txt shows 0 differences | none |
| F4 | C1 | Timestamps from sources other than the archive, such as new log formats, are read differently | outside the claim | none | the claim covers the archive only; other sources are a new claim |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | covered | F4: scoped to the archive; other sources are outside the claim |
| Q2 | C1 | does not apply | the reference library is an independent implementation, not a supplied answer |
| Q3 | C1 | covered | F1: the reference library is the rival, run on every item |
| Q4 | C1 | does not apply | one comparison, with no arms that could agree by construction |
| Q5 | C1 | covered | F1: every single timestamp compared, not a sample or an average |
| Q6 | C1 | covered | F1: the same inputs, same build, go to both parsers |
| Q7 | C1 | covered | worked out: the claim, "identically to the reference library", is about outputs only |
| Q8 | C1 | does not apply | nothing in the parser was fitted, learned or tuned |
| Q9 | C1 | covered | F1, F3: the full population, plus an independent rerun |
| Q10 | C1 | covered | design note dated before the run: "compare every archive timestamp against the reference" |
| Q11 | C1 | covered | F3: outputs saved and rerun by someone else |
| Q12 | C1 | covered | release benchmark: "speed within 2%, memory within 1%" |
| Q13 | C1 | covered | every timestamp counted, including malformed lines, which both parsers must reject alike |

Well-tested: C1. Its main falsifiers were sought and survived.

**Claim as it stands:** unchanged. The parser reads every timestamp in the archive as the reference library does. Formats outside the archive are not claimed.

**Next test:** none needed for this claim. If the parser is to be used on other sources, a sample from each new source comes first.

**What to learn from this example:**
- When the falsifiers were sought and survived, say so plainly. Do not invent gaps to look thorough.
- A real limit of scope (F4) is *outside the claim*, not *missing*.
