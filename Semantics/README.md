# Semantics

The audit of the authority document, **"Claude Fable Semantics - standalone theory"**: a theory of meaning that says what it takes for something to count as an explanation, with four conditions (component fidelity, question fidelity, non-circular dependence, non-vacuity) and a definition of a kind by the changes it responds to. The theory is the fixed point the other two projects quote.

## Current state
- **Authority under audit:** the revised theory (file 20), held by the other model; Claude holds and quotes the original (file 10). Neither is in this repository; see [authority/](authority/).
- **The audit** is run by a second language model under a workflow written for it ([24](<tests/24 Workflow - audit the semantics - give this to the other model.md>)). Its first pass produced ten proposed amendments, A to J ("R2"). Rounds 3 and 4 ([27](<tests/27 Next instruction for the other model - round 3, outside cases.md>), [28](<tests/28 Next instruction for the other model - round 4, two change-based clauses.md>)) pressed on two of them with outside cases. [30](<tests/30 Next instruction for the other model - workflow update and re-audit.md>) had the model update its own audit workflow (Stage A, done) and run a judgement-phrase pass over every amendment (Stage B, part done: 32 rows, A to the start of D).
- **Live instruction:** [41](<tests/41 Next instruction for the other model - finish Stage B and near cases.md>). Finish the Stage B table for D to J; hold each pair against a near case. Not yet sent, or not yet returned, as of the last log entry.
- **Open question the record raises:** the gauge read zero on first use (Lesson 35). Whether the judgement-phrase pass measures anything is what 41 tests.

## Where to start
[INDEX.md](INDEX.md) for the timeline with links. [ORIGIN.md](ORIGIN.md) for what the theory is and how it entered the project. For the method behind the audit, the [Owner's guide](<tests/24 Owner's guide - running the audit workflow.md>).

## What is in this folder
```
ORIGIN.md      what the authority document is; the fact that it is not here
INDEX.md       the audit as a timeline, with what is and is not in the repository
authority/     NOT-IN-BUNDLE.md - the theory files 10 and 20 are not in either bundle
tests/         the audit workflow pair (24) and the four instruction rounds (27, 28, 30, 41)
results/       NOT-IN-BUNDLE.md - the other model's returns are quoted in the log, not held here
```

## Traps
- Handing the other model the hard-to-vary skill. It reinterprets "never" and "may not". Hand it file 24.
- Reading the R2 amendments as Claude's. They are the other model's, against a revised theory Claude has not seen (log 26).
- Treating rounds 27 and 28 as still open. They ran; the owner paused the clause rounds at log 30 to return to the audit itself.
