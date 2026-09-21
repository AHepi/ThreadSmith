# Plan 45: execution attempt and preserved handoff

## Status

BLOCKED BEFORE PART A COMPLETED. This is not a results file claiming completion of plan 45. No native sameness comparisons completed, no Part B forcing cases were adjudicated by a run, no findings were sorted into observed piles, no rig patch was made, and no regression comparison was performed. The original plan, authority documents and prior audit remain unchanged. No remote repository write was made.

The current source snapshot was pinned to AHepi/ThreadSmith commit `ce30053e4369675e989ae4f21103132e5398cbe6`. The plan's retrieved Git blob is `ade01727896779eb2ebbdac67a496074b81305ba`. Its predictions remain predictions.

## What was actually executed

The current patched rig-1 driver and its rules were recovered through the GitHub connector. Because direct network downloads from the execution environment failed, connector-returned text was reconstructed locally and verified against the Git blob hashes before execution. The full driver matched `a883b19297db6dde5fa19bdc572b96215e74ad55`; its rules matched `dce653feb50b3d6a3ca9255b4209c06e2e20f99f`. No semantic alteration was made.

An environment smoke test launched that exact driver on the repository's existing `ledger_T05B.pl` and `.json`, also independently matched to their Git blob hashes. This fixture is a historical Claude translation under file 36. It was used only to exercise the executable path, not substituted for a plan-45 comparison or a new translation under 38/39.

The driver reached its first call to `contradiction(F)` and failed when launching `/home/claude/sCASP/scasp`:

```text
FileNotFoundError: [Errno 2] No such file or directory: '/home/claude/sCASP/scasp'
```

The process exited with code 1. Its standard output was empty. Its `raw_log.txt` is empty because the driver writes a query receipt only after its solver call returns. An empty log is not a no-fault result. The traceback, command, exit status and authenticated source manifest are in `evidence/`.

Neither `swipl` nor `scasp` was found on PATH. The direct Git clone failed with a name-resolution error. Package-repository access also failed with name-resolution errors, so the missing runtime could not be installed through that route. No replacement solver, simulated Prolog answers or replayed historical checker output was used.

## Useful preparation completed

The prior audit's own `validate()` function was executed without calling its file-writing `main()`. It confirmed the original 23 manifest files, 384 input records, 324 inherited receipts and six worked tables. This is structural validation only. The output is stored outside the original audit so its historical validation file is not replaced.

The six existing worked translations were exported as six JSON/Prolog pairs, preserving their original twenty table rows, source marks, sentence anchors and TOLD-world convention. These are exports of the original side, not six new Claude translations. The earlier Markdown sections and the original corpus text are retained alongside them.

Every export names its adapter choices. No physical response class is invented for “not stated.” STRUCK and TOUCHED are not changed to HIT. The two Happenings use the native `did/5` form; rig 1 alone is not represented as having performed rig 2's physical checks. The Prolog exports have not been parsed or executed by s(CASP). They therefore remain candidate transcriptions, not certified complete encodings of meaning.

The old prose bin is retained verbatim as one JSON entry per export. The native GAUGE counts bin entries, so that number must not be mistaken for the original number of source sentences with material in the bin. This limitation is explicit in each export.

All fifteen Part B rows have been registered with separate fields for the plan's predicted pile and the observed pile. Every observed pile is null. Unsuffixed family references were expanded to all supplied family members for preparation only, yielding 48 exact input records with text hashes. This expansion is not a claim that the frozen plan requires all 48 to be run. The plan's own references remain in each record so the selection can be reviewed without changing its prediction.

## Part A is not a completed two-translator comparison

The six archived tables were authored by this assistant in the earlier audit. The inspected repository state describes plan 45 as not yet run. New translations authored here cannot honestly be labelled Claude translations. Neither the plan's predicted line counts nor its proposed Claude readings were converted into fictitious observed outputs.

Plan 45 also calls for the existing “sameness test from rig 1” but does not state a command. The inspected current rig-1 driver has a single-ledger `check(ledger_path, log)` entry point; its joined driver calls the same checker with added laws. No runnable two-ledger comparator was identified in these entry points or the inspected rig-1 directory listing. This is an unresolved location/packaging question, not a claim that no comparator ever existed. A newly written set-difference program would not be silently passed off as that test.

The originals retain TOLD. The owner's later file-46 instruction selects actual-ledger standing for fresh translations. Any later comparison must preserve that standing difference rather than modify the archived side. An actual-ledger projection generated from the old tables is not an independent translation.

## Source discrepancies recorded before an outcome is known

### N17 and the F05 prediction

The plan predicts a LETS report against a stated tendency. N17-A actually says that a handle adjustment “assisted an attempted opening” and explicitly says the gate stayed shut. It does not use LETS and does not separately state the directional tendency anticipated by that prediction. N17-B states an opening.

The eventual transcription must disclose whether the assistance is encoded as HELPS and how any tendency is obtained. It must not insert LETS or an independent tendency merely to match the prediction. This observation is about the supplied input, not an executed result or a change to the language.

### N22 and the F12 prediction

The plan predicts SO THAT returning “cannot tell” because the relevant information is absent. N22-A explicitly supplies both a dependency on a dial setting and an action changing that setting. It withholds which setting preserves coolness and what turning produces.

The current rules define `achieves(A,F)` by `changes(A,X)` and `depends_on(F,X)`. Thus a transcription of the two supplied relations can satisfy the checker's relevance condition without establishing successful cooling. Also, the text itself is not an explicit SO THAT line: adding a test query requires an identified assessment target rather than silently adding a source assertion. The promised “cannot tell” is not safely predicted from this fixture alone. This remains a pre-run source/code observation, not an observed verdict.

### N03-B's metatextual sentence

The plan conditionally predicts an extra line on the archived side if it retained “The text states the contact.” The actual archived worked translation already places that sentence in the bin. No extra held row for that sentence is present in the old table. This does not replace the eventual sameness run; it prevents a conditional prediction being mistaken for an observed difference.

## Why no repair was built

The plan requires Part A first, then forcing/control runs on the baseline, then evidence-based sorting, then the first forced pile-2 change, followed by comparisons against every earlier ledger. The missing runtime does not grant permission to turn the expected piles into results or to install the earlier proposed amendments. No pile-2 change has been made.

In particular, F09 and F15 remain unconfirmed by this attempt. Reading a plausible path through the source code is not the forcing-case run required by the plan. The fifteen-case registry deliberately records no observed pile.

## Resume point

Resume in an environment with the real s(CASP) runtime. Obtain the exact native sameness-test entry point and the six new comparison-side ledgers, with their real authorship and all adapter choices recorded. Complete Part A under original 38 and 39, preserving the old tables unchanged. Only then perform Part B and its controls, sort by those outputs, and consider a patch.

`tools/resume_smoke.py` repeats the authenticated environment check with a supplied s(CASP) path. It is not a full-plan runner and does not silently supply the missing comparison or perform any rig patch. The broader work remains the frozen plan's work, not a substituted experiment.

## Evidence boundaries

The downloadable package contains the native failure evidence, exact authenticated driver/rules and historical smoke fixture, unmodified prior audit, prepared original-side exports, referenced Part B inputs, and preparation tooling. It contains no claim of a successful semantic run, no fabricated Claude output and no simulated sameness report. Hashes establish the identity of recorded bytes, not their semantic adequacy.
