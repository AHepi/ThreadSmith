# Relations between the three projects

A hypothesis ledger. Each entry is a claim about how two projects connect, its current status in the record's own terms, where the evidence is, and what is still open. Uncertainty is written here, not into the folder tree. Add an entry when there is reason to discuss a connection; change its status when evidence moves it; do not delete one that is rejected, mark it.

Status words used: **stated** (written in a file as a claim, not tested), **seen** (watched to happen in a recorded run), **open** (a question the record itself raises).

---

## R1. The semantics is the authority for the language
**Claim.** The ledger language's core meaning comes from the authority document: "a line means the difference it makes to what follows and what clashes when the checker removes it or changes what fills a slot; this is the authority document's definition of a kind, used as the whole semantics."
**Current status.** Stated (log 18). The mapping from the theory's terms to the language's properties is written out in the project story ("Words from the authority document, and the plain words used here"): Contract -> the question frozen; Transport -> what the translator does; Provenance -> source marks; Kinds as edit-signatures -> property 2; Non-vacuity -> the leftover bin; Indistinguishable is identical -> the sameness test.
**Evidence.** [project story](<records/Checked reasoning language - project story.md>), sections "Word list" and "Log" 18, 20. Every test plan names the authority document at its head.
**Open question.** The language was built against file 10 (in the repository since log 56); the other model audited file 20, a revised theory Claude has not been given (log 26). Which version the language now answers to is unsettled.
**Related items.** `Language/authority/38 ...`, `Semantics/ORIGIN.md`.

## R2. The hard-to-vary skill is sharpened by the semantics
**Claim.** "This skill sharpens [Deutsch's idea] using a formal theory supplied by the user, 'Claude Fable Semantics'. That theory's terms are mapped to plain words in references/word-list.md."
**Current status.** Stated, in the skill's own front matter; and the skill's words are now **seen** to do work in a reader that never saw the theory (log 54: DeepSeek V4.1 Flash on 49 outside documents, the semantics withheld). What the semantics adds over the skill's plain words was not tested; the reader was never given it.
**Evidence.** [SKILL.md](<HV Skill/authority/hard-to-vary/SKILL.md>); [word-list.md](<HV Skill/authority/hard-to-vary/references/word-list.md>); [49 Plan](<HV Skill/tests/49 Plan - the skill on outside papers, read by DeepSeek V4.1 Flash.md>); [54 Results](<HV Skill/results/54 Results - where the skill breaks, on outside papers read by DeepSeek.md>).
**Open question.** Whether the semantics document, given beside the skill, changes what a reader finds (plan 48 designed that comparison and was stopped). And whether the two breaks found in the skill's wording recur (the repeatability run in file 54).

## R3. The skill built and kept improving the language
**Claim.** The language's twelve properties were worked out with the hard-to-vary skill (log 01), and the skill was improved from what each stage of the language work taught (logs 02, 05, 08, 14, 21, 22, 30).
**Current status.** Seen, in the sense that each improvement is logged with the case that prompted it and log 05 tests the additions by asking "what would have gone differently without it?".
**Evidence.** Log entries 01, 02, 05, 08, 14; "What each patch gave up" for the rigs; [Lessons](<records/Checked reasoning language - Lessons.md>) 4 and 6.
**Open question.** The building module of the skill was "not exercised" by the research stage (log 05) and first used for real at log 30. How much of the skill is tested versus fitted.

## R4. The audit workflow carries the skill's method to the other model
**Claim.** File 24 restates the hard-to-vary method as positive instructions and cards, for a model that reinterprets negative wording; the skill itself is not handed over. Later the rebuilt skill is used as the test for updating that model's audit workflow (log 30).
**Current status.** Seen on one audit (log 30's "record of what worked"). The near-case routine was deliberately kept in the workflow and out of the skill (log 42).
**Evidence.** [24 Owner's guide](<Semantics/tests/24 Owner's guide - running the audit workflow.md>); [30 Next instruction](<Semantics/tests/30 Next instruction for the other model - workflow update and re-audit.md>); [55 Stage B return](<Semantics/results/55 Stage B return - the other model's finished table, near cases and tighter pairs.md>); log 30, 31, 42, 55.
**Open question, part answered.** Whether the judgement-phrase pass added at log 30 does work at all: on first use it produced zero BORROWED: JUDGEMENT marks in 32 rows (Lesson 35). With near cases added (file 41) it moved: two of 80 further rows, and six of seven near cases against the original pairs, were marked BORROWED (log 55). The near case is the part that does the work; the far-apart pair on its own did almost none. Still open: whether the three rows left standing are judgement the theory declares, points it lists as open, or gaps (file 55 asks).

## R5. The audit of the semantics fed back into the language
**Claim.** The other model, set up to audit the semantics, also audited Claude's rulebook (file 23) and found 25 real faults, which drove the second and third piles of rig changes and the clean language file (logs 32 to 36). Its literary stress test supplied the first outside texts the language was run on (log 37).
**Current status.** Seen. Five of its cases were run through the rigs to sort the findings by evidence (log 33); seven of eight blind-sample texts matched its keys (log 37).
**Evidence.** Logs 32 to 38; [35 Test plan](<Language/tests/35 Test plan - the third pile.md>); [37 Test results](<Language/results/37 Test results - blind sample from the literary stress test.md>); ledgers `K..` and `T..` in `Language/rigs/`.
**Open question.** The other model now has 38 and 39 and has audited both (log 45; the package is in `Language/results/`). It translated six of its own texts and none of Claude's, so the line-by-line comparison still has no shared text; plan 45 makes the overlap from Claude's side and predicts the same facts with a different standing throughout. Whether a fixture is written as the actual ledger or as a TOLD world is a decision for the owner.

## Not claimed
- That the three projects form one system. The folder tree keeps them side by side on purpose.
- That the ledger language is "checker-friendly representation" for any purpose beyond fault-finding in reasoning. Other purposes, if they come, would be new artifacts inside Language/ until evidence says otherwise.
