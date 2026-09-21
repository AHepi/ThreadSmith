# Reading a result

**TERM: Raw result** and **interpretation.** The untouched record of what happened during a run; and, separately, what a person thinks it shows.

## Plain-language meaning
A run produces something as it came: a raw log, an output file, a return from another model. Separately, someone reads it and says what it shows. The two are kept in different places and never mixed: the raw result is never edited, and the reading never goes inside it.

## What to open
- **Raw result.** In `rigs/` or `results/`: the run exactly as it happened, under a name that identifies the case (the project's rigs read-me decodes the names). Every question put and every answer returned, with nothing removed.
- **What was expected, before.** The test plan in `tests/` with the same number.
- **Interpretation.** The results file in `results/` with the same number: its table has a row per case (what was predicted, what happened, whether they match), then what a miss means and what was done, then what was not tested.
- **The short account.** The log entry of the same number in `records/`.

## Contrast
- **Raw result is not interpretation.** The raw line says what the apparatus returned. Only the results file says whether that is right, a miss, or a false alarm, and why.
- **A match is not a pass.** The results file names what it did not test; read those lines before the ticks.
- **The apparatus now is not the apparatus then.** A miss often forces a patch. Rerunning the same case on the current apparatus can give a different answer from the one in the results file; the raw log keeps both if both were run.

## Follow the chain
Authority -> Test (NN plan) -> Raw result (the run) -> Interpretation (NN results) -> Lesson (the miss, predicted or not, and the fix that became part of the next authority).
