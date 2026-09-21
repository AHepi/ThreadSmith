# Following a test

**TERM: Test.** A frozen plan, written before the run and not edited after, saying what the cases are and what is expected.

## Plain-language meaning
Before anything is run, the plan is written: the cases, how each will be handled, and what each is expected to produce. Then the run. Then a results file that ticks each prediction and names what was not tested. The plan and the result are two files with the same number.

## What to open
1. `tests/NN Test plan - ...`. First line: written before the run, not edited afterwards. It names the authority, says what kind of case each is, and lists the predictions.
2. `results/NN Test results - ...`. It reports what happened, ticks each prediction, and names what it did not test.
3. Log entry NN in the project's `records/`: the short account, and what change the run forced. Where the project keeps "What each patch gave up", read the entry for that change.
4. The raw evidence in `rigs/` or `results/`: the run as it happened, untouched, under a heading that names the case.

## Contrast
- **A test plan is not a result.** The plan's predictions can be wrong, and that is the point: the frozen file is what stops a half-wrong prediction being reported as a confirmation.
- **A test is not the apparatus as it is now.** A `rigs/` folder holds the apparatus after every later patch. The results file says what it said on that day.

## Follow the chain
Authority -> Test (NN plan) -> Raw result (the run) -> Interpretation (NN results, log NN) -> Lesson (the patch and what it gave up; the next plan that broke it).
