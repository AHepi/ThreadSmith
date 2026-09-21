# Following a test

**TERM: Test.** A frozen plan, written before the run and not edited after, saying what the cases are and what is expected.

## Plain-language meaning
The owner sent four sentences about a man named Markus. Before anything was run, Claude wrote down how it would translate them and what each rig would say. Then it ran them. Then it wrote what happened. The plan and the result are two files with the same number.

## Tiny demonstration
1. Open [21 Test plan - your Markus paragraph.md](<../tests/21 Test plan - your Markus paragraph.md>). First line: "Written before the run. Not edited afterwards." It names the authority (file 10) and the rulebook the translation follows (20). It says what kind of case it is (an argument giving reasons to expect, not what produced something), how each phrase will be translated, and what it expects: rig 1 will call the inference from the habit a JUMP, a false alarm, because of patch 3.
2. Open [21 Test results - your Markus paragraph.html](<../results/21 Test results - your Markus paragraph.html>) in a browser. It reports what the rigs said, ticks each prediction, and names what it did not test.
3. Read log 21 in the [project story](<../records/Checked reasoning language - project story.md>): the JUMP came as predicted; "smash" had no shape in rig 2; patch 6 (SINCE, a reason to expect) was forced. Then read "What each patch gave up": patch 6 "accepts any route. Gives up: it cannot tell a good reason to expect from a backwards one."
4. The ledger is in `Language/rigs/rig 1 - arguments/` as `ledger_G.json` and `ledger_G.pl` (G is the Markus paragraph; the `"paragraph"` field in the json says so). Every question the checker was asked about it, and every answer, is in `raw_log.txt` under a heading that names the paragraph.

## Contrast
- **A test plan is not a result.** The plan's predictions can be wrong, and that is the point: log 05 says the frozen file is what stopped a half-wrong prediction being reported as a confirmation.
- **A test is not the rig as it is now.** The rig bundle holds the checkers after patches 6 to 16. The results file says what the checker said on that day.

## Where to find it
`<project>/tests/` for plans; `<project>/results/` for the results pages; `Language/rigs/` for the ledgers and the raw log.

## Follow the chain
Authority (10; rulebook 20, not in bundle) -> Test (21 plan) -> Raw result (`ledger_G.*`, `raw_log.txt`) -> Interpretation (21 results, log 21) -> Lesson (patch 6 and what it gave up; patch 7 followed at log 22 when the Mondays paragraph broke it in the two ways predicted).
