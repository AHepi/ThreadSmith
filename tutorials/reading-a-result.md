# Reading a result

**TERM: Raw result** and **interpretation.** The untouched record of what happened during a run; and, separately, what a person thinks it shows.

## Plain-language meaning
The other model built a literary stress test: 324 short texts with answer keys held in separate files. Claude took eight of them, translated them under file 36, ran them, and only then opened the keys. Seven matched. The raw output, the ledgers, and the reading of them are three different things kept in three different places.

## Tiny demonstration
Take one text, T07-B: "Nora's story has the door open; in the room it stayed shut."

- **Raw result, the ledger:** `Language/rigs/rig 1 - arguments/ledger_T07B.json`. The lines as translated, each with its source mark and the sentence it came from.
- **Raw result, the run:** `Language/rigs/rig 1 - arguments/raw_log.txt`. Search for `T07B`. Under it, each query put to s(CASP) and its full answer, with the time taken. This is what actually happened, untouched.
- **Interpretation:** [37 Test results - blind sample from the literary stress test.md](<../Language/results/37 Test results - blind sample from the literary stress test.md>). Its table has a row for T07-B: the key said no contradiction (two contexts); the checker said CONTRADICTION under "Nora's story"; match: "NO, a false alarm, predicted in advance". Then it says what the miss means and what was done.
- **What was expected, before:** [37 Test plan](<../Language/tests/37 Test plan - blind sample from the literary stress test.md>), which predicted this miss.

## Contrast
- **Raw result is not interpretation.** The log line says CONTRADICTION. Only the results file says that is a false alarm, and why.
- **A match is not a pass.** The results file names what it did not test: the translating was still Claude's; the other model's scripts were not run; only the headings of its amendments were read.
- **The rig now is not the rig then.** Patch 15 (a told world stands alone) was made because of this miss. Rerunning T07B on the current rig gives a different answer from the one in the results file; `raw_log.txt` keeps both if both were run.

## Where to find it
`Language/rigs/` for raw runs and ledgers; `Language/results/` for the reading of them; the log entry of the same number for the short account.

## Follow the chain
Authority (36) -> Test (37 plan) -> Raw result (`ledger_T07B.*`, `raw_log.txt`) -> Interpretation (37 results) -> Lesson (log 37: the miss was predicted, then fixed; the fix became part of authority 38).
