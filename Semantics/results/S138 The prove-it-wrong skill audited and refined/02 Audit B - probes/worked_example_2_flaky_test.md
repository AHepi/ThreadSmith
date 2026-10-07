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
