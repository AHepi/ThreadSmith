# Semantics

The audit of the authority document, **"Claude Fable Semantics - standalone theory"**: a theory of meaning that says what it takes for something to count as an explanation, with four conditions (component fidelity, question fidelity, non-circular dependence, non-vacuity) and a definition of a kind by the changes it responds to. The theory is the fixed point the other two projects quote.

## Current state

Reconciled on 21 September 2026 in [log S68](<records/Semantics - project story.md#s68-status-reconciliation-21-september-2026>). The authority remains frozen [file 10](<authority/10 Claude Fable Semantics - standalone theory.md>); file 20 remains set aside under decision S4. S64 returned its requested earlier-version sort. No new theory version or amendment adoption is recorded.

| Step | Verified state | Evidence and limit |
| --- | --- | --- |
| Stage B and Stage C | Returned and recorded in logs 55 and 57. | [Stage B return](<results/55 Stage B return - the other model's finished table, near cases and tighter pairs.md>) and [Stage C return](<results/57 Stage C return - the other model's seven case cards, O4 placed, phrases sorted.md>), unchanged. The original first 32 Stage B rows remain unrecovered. |
| S62: Stage D and report | Returned; already imported and read at S63. | [Ten-file return](<results/S62 Stage D and report - return/>). Its 56 clause comparisons were all SAME; its coverage was 24/80 recovered rows. This is a completed round, not an unsent instruction. |
| S63 instruction | Superseded without being sent. | Replaced by [S64](<tests/S64 Next instruction for the other model - ten near cases, verdicts under the earlier version, returned as a zip.md>) after the authority decision. |
| S64: ten near cases and version sort | Returned and imported at S65. | [Eight-file return](<results/S64 Near cases - return/>) and [saved session messages](<results/S65 Saved page - the other model's chat, S62 and S64 manifests and timings.md>). All eight files match the saved ZIP byte for byte; [S68](<records/Semantics - project story.md#s68-status-reconciliation-21-september-2026>) records that check. |

S64 places five of O15–O24 directly and three more by tighter pairs. O20/H90 and O21/I96 remain BORROWED: JUDGEMENT. Its six clause groups record 144 SAME comparisons; that preserves the case verdicts without establishing the proposed clauses as sufficient. Coverage is now 34/80 recovered rows, 46 without a case, plus 32 unavailable rows. Its version sort marks six rows wholly REVISED ONLY and three mixed. The grouped judgement inventory grows from four to six: one declared input, four stated open points and one homeless requirement. H64 and I64 remain proposals.

**Current next step:** [S65, thirteen near cases](<tests/S65 Next instruction for the other model - thirteen near cases, two attribution tests, returned as a zip.md>), is prepared: O25/O26 test H64 on explicit operating histories, O27 tests I64 on a recipient's reinterpretation, and O28–O37 strain the next ten rows. No S65 return or verified dispatch is present in the checked evidence. Send S65 if it has not already been sent, otherwise receive its return; recover the original 32 rows alongside that work. S62 and S64 need no repeat dispatch, and file 20 is not a prerequisite.

## Where to start
[INDEX.md](INDEX.md) for the timeline with links. [ORIGIN.md](ORIGIN.md) for what the theory is and how it entered the project. This project keeps its own record in [records/](records/) from 21 September 2026: [project story](<records/Semantics - project story.md>) (the log), [Decisions](<records/Semantics - Decisions.md>) (the owner's words), [Lessons](<records/Semantics - Lessons.md>) (failures only), [Status](<records/Semantics - Status.md>) (the summary); its [READ ME FIRST](<records/READ ME FIRST.md>) says how it relates to the shared record the projects began with. Its claims about the other projects are in [RELATIONS.md](RELATIONS.md); a worked example on its files is in [tutorials/](tutorials/). For the method behind the audit, the [Owner's guide](<tests/24 Owner's guide - running the audit workflow.md>).

## What is in this folder
```
ORIGIN.md      what the authority document is and how it entered the project
records/       this thread's own log, Decisions, Lessons and Status, from 21 September 2026
RELATIONS.md   this project's claims about its connections to the other two, with status and evidence
tutorials/     one worked example: tracing a lesson through this project's files
INDEX.md       the audit as a timeline, with what is and is not in the repository
authority/     10 Claude Fable Semantics - standalone theory.md (frozen); NOT-IN-BUNDLE.md - file 20 is not here
tests/         the audit workflow pair (24) and the instruction rounds (27, 28, 30, 41, 55, 57 superseded unsent, S62, S63 superseded unsent, S64 returned, S65 prepared)
results/       55 Stage B return, 57 Stage C return, S62 and S64 return folders (unchanged), S65 saved session messages; verification receipt in log S68
```

## Rules of this project
- **Each instruction travels as a pack** (decision S5): one zip built by `tests/S65 Instruction pack - build.py` holding the read-me for the agent, the instruction's paste part, file 10, files 24 and 30, the earlier instructions and every return. A fresh agent reads the read-me first. The R2 amendments in full are the owner's to add.
- **Handing things to the other model:** it reinterprets negative instructions and follows positive ones. Give it file 24 in place of the hard-to-vary skill. Every instruction's paste part is searched by program for negative wording before it goes.
- **Every return is kept as it came** in `results/`, named by the log entry that received it; the reading goes in the log, never inside the return.
- **The authority is frozen.** File 10 is not edited; a revision is a new numbered file in `authority/`.

## Words used in this project
Short form; the theory's own terms are in the authority document, and their plain-word mapping is in the shared project story's "Words from the authority document" (in `../Language/records/`) and the skill's word list.
- **Case (audit).** A short described situation about ordinary things, with a thoughtful person's verdict and the theory's verdict, condition by condition. A **break** is where the two differ and the difference survives the best reply on the theory's behalf.
- **Pair, near case, gauge (audit).** For a phrase that asks the reader to judge: two picturable changes, one showing it met and one unmet; a case that sits close to the line between them; the list of phrases still marked BORROWED: JUDGEMENT.

## Traps
- Reading the R2 amendments as Claude's. They are the other model's, against a revised theory Claude has not seen (log 26).
- Treating rounds 27 and 28 as still open. They ran; the owner paused the clause rounds at log 30 to return to the audit itself.
- Reading the returns in `results/55` and `results/57` as Claude's. They are the other model's, word for word; Claude's readings are logs 55 and 57 and are kept out of the files.
- Taking the other model's quotations as quotations of file 10. It audits the revised theory (file 20). Log 57 checked its Stage C quotations against file 10: one matches, one continues past file 10's sentence, two are absent from file 10.
