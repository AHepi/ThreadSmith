# Language - relations to the other projects

A hypothesis ledger of this project's connections to the other projects in the repository. Each entry is a claim, its current status in the record's own terms, where the evidence is, and what is still open. A claim lives in the project that makes it; entries are added, updated or marked rejected, never removed. Numbers R1 to R5 were given when the ledger was one file at the root; they are kept.

Status words used: **stated** (written in a file as a claim, not tested), **seen** (watched to happen in a recorded run), **open** (a question the record itself raises).

---

## R1. The semantics is the authority for the language
**Claim.** The ledger language's core meaning comes from the authority document: "a line means the difference it makes to what follows and what clashes when the checker removes it or changes what fills a slot; this is the authority document's definition of a kind, used as the whole semantics."
**Current status.** Stated (log 18). The mapping from the theory's terms to the language's properties is written out in the project story ("Words from the authority document, and the plain words used here"): Contract -> the question frozen; Transport -> what the translator does; Provenance -> source marks; Kinds as edit-signatures -> property 2; Non-vacuity -> the leftover bin; Indistinguishable is identical -> the sameness test.
**Evidence.** [project story](<records/Checked reasoning language - project story.md>), sections "Word list" and "Log" 18, 20. Every test plan names the authority document at its head.
**Open question, now closed on one side.** The language was built against file 10 (in the repository since log 56); the other model audited file 20, a revised theory Claude has not been given (log 26). The owner set 20 aside as a regression (Semantics decision S4), so the language answers to 10. Still open: which of the audit's findings against 20 bear on 10 (Semantics S64 asks for the sort). First concrete evidence of what 20 changed (log 57, from the other model's quotations checked against 10): 20 has anchors with properness and resolution conditions and lists an attack on them, where 10's Part V argues there is no anchoring condition; 20 has a merit condition for question-finding with its own refutation entry. File 57 asks for both passages in full.
**Related items.** `Language/authority/38 ...`, `Semantics/ORIGIN.md`.

## R3. The skill built and kept improving the language
**Claim.** The language's twelve properties were worked out with the hard-to-vary skill (log 01), and the skill was improved from what each stage of the language work taught (logs 02, 05, 08, 14, 21, 22, 30).
**Current status.** Seen, in the sense that each improvement is logged with the case that prompted it and log 05 tests the additions by asking "what would have gone differently without it?".
**Evidence.** Log entries 01, 02, 05, 08, 14; "What each patch gave up" for the rigs; [Lessons](<records/Checked reasoning language - Lessons.md>) 4 and 6.
**Open question.** The building module of the skill was "not exercised" by the research stage (log 05) and first used for real at log 30. How much of the skill is tested versus fitted.

## R5. The audit of the semantics fed back into the language
**Claim.** The other model, set up to audit the semantics, also audited Claude's rulebook (file 23) and found 25 real faults, which drove the second and third piles of rig changes and the clean language file (logs 32 to 36). Its literary stress test supplied the first outside texts the language was run on (log 37).
**Current status.** Seen. Five of its cases were run through the rigs to sort the findings by evidence (log 33); seven of eight blind-sample texts matched its keys (log 37).
**Evidence.** Logs 32 to 38; [35 Test plan](<tests/35 Test plan - the third pile.md>); [37 Test results](<results/37 Test results - blind sample from the literary stress test.md>); ledgers `K..` and `T..` in `Language/rigs/`.
**Open question.** The other model now has 38 and 39 and has audited both (log 45; the package is in `Language/results/`). It translated six of its own texts and none of Claude's, so the line-by-line comparison still has no shared text; plan 45 makes the overlap from Claude's side and predicts the same facts with a different standing throughout. Whether a fixture is written as the actual ledger or as a TOLD world is a decision for the owner.

## Not claimed
- That the three projects form one system. The folder tree keeps them side by side on purpose.
- That the ledger language is "checker-friendly representation" for any purpose beyond fault-finding in reasoning. Other purposes, if they come, would be new artifacts inside Language/ until evidence says otherwise.
