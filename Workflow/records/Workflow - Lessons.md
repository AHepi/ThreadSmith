# Workflow - Lessons

*Only things that failed while being built or tested, and how each was fixed. Numbered W1 onward.*

W1. The program that checked draft W1's quotations against file 10 was run and its output not kept, so the check could not be re-run or audited (found by the record judge, log W2). Fixed: the program and its output are kept under `rigs/W3 quote check/`, and the program now reports the Part each quotation sits under, which the first version did not.

W2. The judging round of log W2 ran without a frozen prediction file, against the root convention that predictions are frozen before research. Fixed for the next round: W3's P1.1 to P1.4 are the predictions for phase 1's judging, frozen before it runs.

W3. The quote-checking program paired quotation marks inside its length filter, so a short quotation could shift the pairing; it then reported the gap between two quotations as a quotation, skipped three of W3's rows, and labelled every check "file 10" whatever file it read (found by the W5 file-11 judge). Fixed: a second version pairs the marks in order over the whole text before filtering, names the file it checked, and ends with what it does not reach; kept with its outputs in `rigs/W5 quote check/`, and W3 re-checked against both files.
