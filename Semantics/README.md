# Semantics

The audit of the authority document, **"Claude Fable Semantics - standalone theory"**: a theory of meaning that says what it takes for something to count as an explanation, with four conditions (component fidelity, question fidelity, non-circular dependence, non-vacuity) and a definition of a kind by the changes it responds to. The theory is the fixed point the other two projects quote.

## Current state
- **Authority under audit:** the revised theory (file 20), held by the other model and not in this repository; Claude holds and quotes the original, [file 10](<authority/10 Claude Fable Semantics - standalone theory.md>), in the repository since log 56. See [authority/](authority/).
- **The audit** is run by a second language model under a workflow written for it ([24](<tests/24 Workflow - audit the semantics - give this to the other model.md>)). Its first pass produced ten proposed amendments, A to J ("R2"). Rounds 3 and 4 ([27](<tests/27 Next instruction for the other model - round 3, outside cases.md>), [28](<tests/28 Next instruction for the other model - round 4, two change-based clauses.md>)) pressed on two of them with outside cases. [30](<tests/30 Next instruction for the other model - workflow update and re-audit.md>) had the model update its own audit workflow (Stage A, done) and run a judgement-phrase pass over every amendment (Stage B, part done: 32 rows, A to the start of D).
- **41 returned** (log 55): the table finished (112 rows, A to J), seven near cases, five tighter pairs. The return is held as [55 Stage B return](<results/55 Stage B return - the other model's finished table, near cases and tighter pairs.md>), unchanged.
- **55 returned** (log 57): seven case cards, five placed and two on rows already borrowed, every verdict agreeing with the thoughtful person; O4 placed by the theory's own contract distinction; the surviving phrases sorted (H a declared input; G and C stated open points; A homeless). Held as [57 Stage C return](<results/57 Stage C return - the other model's seven case cards, O4 placed, phrases sorted.md>), unchanged. Its "finding for the top", on lookup tables, is about one front-matter sentence the body already qualifies (Lesson 50). It also gives the first concrete sight of what file 20 changed: anchors with properness and resolution conditions, where file 10 argues there is no anchoring condition.
- **Live instruction:** [57](<tests/57 Next instruction for the other model - Stage D fix cards and the report.md>). Stage D's four fix cards (A, C built from the contract distinction, G, H); the top finding restated at its size beside both sentences; the two anchoring passages printed in full; then the report. Not yet sent.
- **What the record now says about the gauge:** it read zero on first use (Lesson 35) and moved once near cases were added (log 55): two table rows and six of seven near cases were marked BORROWED: JUDGEMENT against the original pairs; three near cases were then placed by tighter pairs. Open: A's scope row (O1), C's local-dependence row for O4 and O7. Lesson 49: file 41 left the model to find the theory's own distinction for O4 and it built a mechanism instead.

## Where to start
[INDEX.md](INDEX.md) for the timeline with links. [ORIGIN.md](ORIGIN.md) for what the theory is and how it entered the project. The project's own record is in [records/](records/): [project story](<records/Semantics - project story.md>) (the log), [Decisions](<records/Semantics - Decisions.md>) (the owner's words), [Lessons](<records/Semantics - Lessons.md>) (failures only), [Status](<records/Semantics - Status.md>) (the summary). Entry numbers are the repository's one sequence. For the method behind the audit, the [Owner's guide](<tests/24 Owner's guide - running the audit workflow.md>).

## What is in this folder
```
ORIGIN.md      what the authority document is; the fact that it is not here
INDEX.md       the audit as a timeline, with what is and is not in the repository
authority/     10 Claude Fable Semantics - standalone theory.md (frozen); NOT-IN-BUNDLE.md - file 20 is not here
tests/         the audit workflow pair (24) and the six instruction rounds (27, 28, 30, 41, 55, 57)
results/       55 Stage B return and 57 Stage C return (the other model's returns on 41 and 55, unchanged); NOT-IN-BUNDLE.md for the earlier returns, quoted in the log and not held here
```

## Traps
- Handing the other model the hard-to-vary skill. It reinterprets "never" and "may not". Hand it file 24.
- Reading the R2 amendments as Claude's. They are the other model's, against a revised theory Claude has not seen (log 26).
- Treating rounds 27 and 28 as still open. They ran; the owner paused the clause rounds at log 30 to return to the audit itself.
- Reading the returns in `results/55` and `results/57` as Claude's. They are the other model's, word for word; Claude's readings are logs 55 and 57 and are kept out of the files.
- Taking the other model's quotations as quotations of file 10. It audits the revised theory (file 20). Log 57 checked its Stage C quotations against file 10: one matches, one continues past file 10's sentence, two are absent from file 10.
