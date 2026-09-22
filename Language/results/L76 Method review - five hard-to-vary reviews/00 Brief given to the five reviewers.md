# Shared brief for the five method reviewers (read this first)

You are one of five independent reviewers. You are checking whether the METHOD of the "Language" project makes sense, before its orchestrator changes anything. You are not asked to fix the language, run the checker, or edit any file in the repository. Your only output is one report file at the path your task names. Do not write anywhere else. Do not use git.

## The skill you work with
Read, whole, before anything else: `hard-to-vary/SKILL.md` in this folder, then `hard-to-vary/references/building.md`, `testing-against-cases.md` and `reporting.md`. Apply the skill exactly as it says: jobs marked given/fixed/added; parts; the swap, flip, poke tests; the eight marks (held, held if, two routes, loose, idle, borrowed, fixed, unknown) with what holds each part; provenance (fitted, built, asserted) in its own column; catch-alls need gauges; whole-explanation checks; never add marks up; no scores. Use the report form in `reporting.md`.

## The project, in one paragraph
The Language project builds a "ledger language" into which prose is translated by a language model (file 39 is the translator's task, file 38 the language), so that an external logic checker (s(CASP), driven by `run_check.py` in rig 1 and `check2.py` in rig 2) can find contradictions, jumps, circles, unconnected steps, plans that cannot work, and now also derive consequences (`tools/consequences.py`) and compare two translations (`tools/sameness.py`). The theory it rests on is file 11 (revision of file 10), "Claude Fable Semantics". The method: a numbered test plan is frozen before any run; results are written against the plan; the record (project story, Decisions, Lessons, Status) is appended only; numbered files are never overwritten (a new version is a new number); nothing in the language or rigs changes without the owner's word; a failed test refutes the bundle (theory K3) and which layer to change is a fresh choice; four sources of error are named (the text, the translator, the language, the checker). The scope contract is L64. Recent tests: L65 (consequences prototype), L66 (a blind corpus with a sealed key, a worker agent translating, a reader agent reading reports only), L71 (consequences on two ledgers), L72 (two translators on the same eight texts, blind to each other). Two outside agents do work: "Astra Ultra" (executes, returns zips) and "Astra Pro" (reads and audits, cannot execute). The orchestrator (Claude, a different session from you) checks returns (hashes, reruns) and marks expectations.

## Where things are (repository root: /home/user/ThreadSmith; read only)
- Record: `Language/records/Language - project story.md` (entries L60 to L75 are the recent ones; earlier entries 01 to 58 are in `Language/records/Checked reasoning language - project story.md`), `Language - Decisions.md` (the owner's words), `Language - Lessons.md`, `Language - Status.md`.
- Scope contract: `Language/authority/L64 Scope - the contract the language claims, second version.md`.
- Language and translator task: `Language/authority/38 ...md`, `39 ...md`.
- Theory: `Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md` (Parts I, III, V, VI, IX, XV are the ones the method leans on).
- Plans: `Language/tests/L65 ...`, `L66 Test plan ...`, `L66 Reader brief ...`, `L71 Test plan ...`, `L72 Test plan ...`, handoffs `L66 Handoff ... second version.md`, `L72 Handoff ...`.
- Results: `Language/results/L65 Test results ...`, `L66 Test results ...`, `L71 Test results ...`, `L72 Test results ...`, `45 Test results ...`; returns `L69 Return - L66 run by OpenAI Codex/` (the worker's L66 return: its draft `DRAFT L66 - what the run showed_correction1.md`, gauge, `evidence/`), `L72 Return - Astra Ultra/` (its `DRAFT L72 ...` and `translations/`), `L74 Return - L66 read-back by Astra Pro/` (`ANSWERS_ChatGPT.md`, `L66_AUDIT.md`, `audit_protocol.md`).
- Tools: `Language/tools/consequences.py`, `sameness.py`; the driver `Language/rigs/rig 1 - arguments/patched/run_check.py` and rules `checker_rules.pl`.

## The four findings the orchestrator says force a change (log L75)
1. Under file 39's attribution rule (content that someone says, believes or concludes goes into a "told world") plus the driver's patch 12 (a told world is asked only for contradictions), a BECAUSE or SINCE inside a report is never tested. Seen at L72 on texts T10-D and T11-B.
2. The driver's what-if bookkeeping sets an effect aside on the strength of a BECAUSE claim that the same run judged a JUMP (not established), and reports the what-if HOLDS without saying so. Seen at L66 on passage P14; found by Astra Pro from the reports alone.
3. The driver prints the sentence number only in what-if and plan headings, so a reader given the reports alone can trace findings to sentences only there. Seen at L66 (E7).
4. `tools/consequences.py` never sets the driver's world list, so told and supposed lines pool with the actual ledger and a contradiction is derived that the checker rightly refuses. Seen at L72 on T07-B.
Two earlier confirmed failures stand: F15 (a BECAUSE and its exact denial in one ledger raise no contradiction) and F09 (an actual fact rides into a what-if), from plan 45 / results L62.

## Rules for your report
- Say how you know each thing: **read** (you read it in a file, name it), **seen** (a printed output), **worked out** (your own reasoning), **assumed**.
- Quote the file and line for anything you hold against the method. A criticism without a location is not a finding.
- No scores, no percentages, no grades. Marks and provenance as the skill says.
- Failures only in a "Lessons" section, if any; do not praise.
- Close with the three lists the skill asks for and a section "What would change my mind".
- Length: what the findings need, no more. Plain English, short sentences.
- Do not write to any file except your report path. Do not modify the repository.
