# 02 Audit B: the prove-it-wrong skill as a skill (triggering, length, cost, checker and evals)

*Plain note: this file is the second of two independent audits of the owner's "prove-it-wrong" skill, version 5, kept as received in `tests/S138 Material - the owner's prove-it-wrong skill, as received/prove-it-wrong/` (log entry S138, decision S93: "can you audit the the following skill and refine"). Audit A reads the skill's content; this audit, B, reads it as a skill: when it fires, what it costs and why, whether its checker does what it says, whether its test set can judge a refinement, and whether its instructions are clear to the agent using it. It changes nothing in the owner's files. The probe ledgers and the checker's output are in the folder `02 Audit B - probes/` beside this file. I did not read Audit A.*

**How to read a finding.** Each has an ID, a weight (SERIOUS, MODERATE or MINOR) and six parts: (1) what is wrong or missing, (2) the evidence, (3) the effect on someone using the skill, (4) the smallest change that would fix it, (5) whether the change can be tested and how, (6) the weight. "SKILL.md:86" means line 86 of that file in the owner's folder. Paths without a folder are inside `prove-it-wrong/`.

**What I read and ran.** All of `SKILL.md`, every file in `references/` (the ten situation files: one read in full, the others in their opening and routing lines), `scripts/check_ledger.py`, `evals/README.md`, `evals/results.md`, `evals/run_suite.sh`, the round-4 key, fingerprints, wrapper and the marking and grade passages cited below, and the hard-to-vary skill's `SKILL.md` ("/home/user/ThreadSmith/HV Skill/authority/hard-to-vary/SKILL.md"). I ran the checker's self-test (14 of 14 passed), the checker on the three worked examples copied out one per file (all pass, 0 warnings), and on 25 probe ledgers I wrote. I ran `evals/run_suite.sh` once with a stand-in for `claude` that makes no model call, and I read `claude --help` (Claude Code 2.1.292). I made no model call. I had no transcripts of the test runs: the results name a test-runs zip that is not in the folder, so everything I say about what the agents did rests on `evals/results.md` and the grade files, quoted.

---

## 1. The findings at a glance

| ID | Weight | Finding in one line |
|---|---|---|
| T1 | SERIOUS | The description fires on everyday words ("it works", "fixed", "passed") and on "your own summaries", and the depth rule then demands the full procedure for nearly every report, so in real use it would run its most expensive form on routine work. |
| T2 | SERIOUS | Its description overlaps hard-to-vary's on "root cause", "post-mortem" and "why it works", and its own module tells the agent to "Use both", the setup round 4 found worst. |
| L1 | SERIOUS | Three texts disagree on what to do with checker warnings (advice; "dealt with" before stopping; harness "fix until it passes"), and the format states as a rule what the checker only warns about, so agents loop on the checker. |
| L2 | MODERATE | The question table (13 questions for every claim, each first "written" as a way to fail) is the largest writing load and the main source of the padding both markers counted, and the skill does not say where the "think first" text goes. |
| L3 | MODERATE | SKILL.md repeats itself: the answer rules appear twice, the Traps section restates rules already given, and the routing graph restates the steps; about 1,000 of its 3,847 words could go or move without losing a rule. |
| K1 | MODERATE | The checker missed 11 of 14 ledgers that break the skill's stated rules, including two the format says it refuses ("Yes." as evidence; a *reported* row that quotes nothing). |
| K2 | MODERATE | Its warnings fire on honest prose ("was not verified") and on the merged rows the skill asks for, and one tells the agent to label a claim resting only on the claimant's word "Well-tested". |
| K3 | MODERATE | It is brittle: a range "C1-C3", the plain name "Q5 Worst single case", a quoted "F2 score", two falsifier tables or a column headed "ID" each produce floods of errors that do not name the cause. |
| E1 | SERIOUS | The test set is too small, with one run per arm per case, to tell a refined version from version 5 except on cost; the skill's own Q9 applied to its evals. |
| E2 | MODERATE | No clean held-out cases are left; rounds 3 and 4 do not record that the case writers had not seen the skill, two round-4 cases are in the style of the project the skill has a file for, and each marker marked cases it wrote. |
| E3 | MODERATE | The blinding is nominal (one Set mapping for all cases, and the ledger format shows which arm is which), "padding" is not defined in the marking lists, and the headline "by both markers" hides the half where the Opus marker ranked hard-to-vary first. |
| E4 | MODERATE | `run_suite.sh` never tests triggering (`--safe-mode` turns skills off), its prompt itself pushes the checker loop, and a reused work folder carries the last run's answers and a nested second copy of the skill. |
| E5 | MODERATE | The evals folder (55,634 words, with every marking list and key) ships inside the skill, and SKILL.md's routing table points the agent at it. |
| A1 | MODERATE | "missing" means two things: a status ("nobody sought it") and an answer that may cite a *failed* or *planned* row. |
| A2 | MODERATE | "Well-tested" is defined three ways: "sought and survived" (SKILL.md), "survived or were reported" (ledger-format), and the checker's message says "survived" when all rows were only reported. |
| A3 | MODERATE | Two worked examples break the quote-or-condition rule they are meant to model, so the rule is contradicted by example. |
| A4 | MINOR | "Three rules" is followed by seven (forcing-questions.md:8). |
| A5 | MINOR | "F1" and "F2" also name the semantics' fidelity conditions (semantics-audit.md:50-53), and the checker reads any "F2" as a row. |
| A6 | MINOR | One thing has several names: falsifier, missing condition, missing test, test condition, gap, caveat. |
| A7 | MINOR | The ledger shows question numbers only, and the checker refuses the plain names beside them (owner's preference: full plain-word names). |
| A8 | MINOR | "The report always carries one next test" against worked example 3's "Next test: none needed". |
| A9 | MINOR | SKILL.md and `evals/results.md` lack the plain note at the top saying what the file does; the project file cites files the skill does not carry. |
| L4 | MINOR | The flowchart and its upkeep rule cost words in every run and add nothing the step list does not give. |
| K4 | MINOR | The checker's own self-test "good" ledger answers twelve questions "does not apply" with one generic reason, including Q5 for a claim saying "guarantees". |

---

## 2. What the skill does well and must keep

A refinement must not lose any of these.

1. **The falsifier-first ledger.** Each claim is frozen word for word and given an observation that would show it wrong, with a status and a receipt. Evidence: GLM's round-3 verdict, "its falsifier-first format forces engagement with the case-decisive tests" (evals/results.md:85); in round 4, version 5 had the fewest missed items with both markers, 5 and 4 against hard-to-vary's 7 and 8 (results.md:130-134).
2. **The fact-check pass and hard rule 11.** Unquoted statements become "if" conditions or "not reported" (SKILL.md:190-195, 220). Evidence: "Version 4's main flaw (stating guesses as facts) dropped to 0 (GLM) and 2 (Opus) violations. Hard-to-vary had 2 and 6." (results.md:152).
3. **The difference between *reported* and *survived*.** A record made by someone else is a claim that a check happened (SKILL.md:209). The checker enforces a quotation on *reported* rows, and my plain probe without one was refused (probe fail_02).
4. **Rivals written out in full** (SKILL.md:134-139). Evidence: version 3 lost round 2 chiefly for "No question for rival explanations" (results.md:53); the fix is credited in round 3.
5. **The path for a well-tested claim** ("A mostly covered ledger is a success", SKILL.md:144; the *held if* rule, SKILL.md:180; worked example 3). Both rounds 3 and 4 include a well-tested case, and the markers penalise invented doubts there.
6. **Each question's own "Does not apply when" exemption, with its "Never" clauses** (for example forcing-questions.md:117 for Q5). An exemption that names a test can be checked; a bare "n/a" cannot.
7. **"Not run is never passed"** and the *pending* status (SKILL.md:173, 208).
8. **The checker's core errors work**: an unanswered question, a *missing* answer citing nothing or a closed row, a *covered* answer citing only open rows, a short falsifier, a short "does not apply" reason. Self-test 14 of 14; the worked examples pass; probes fail_02 and fail_04 were refused for the right reason.
9. **The evals' discipline**: marking lists fingerprinted before runs, a rival arm on the same cases and model, the model named exactly, costs recorded, practice cases declared not to be evidence, and an honest contamination note (results.md:57).
10. **Plain words and plain notes** in the checker ("What this file does", check_ledger.py:3) and in `run_suite.sh` (lines 4-8); the situation files each open with "Use this file ...".

---

## 3. Triggering (lens 1)

### 3.1 Ten prompts that should trigger it and ten near misses, judged by reading the description

The description is SKILL.md:3 (998 characters by my count). "Fires" below is my reading of whether the description, as written, would make an agent pick this skill. No model was called.

| # | Prompt (should trigger) | Fires? | Why, from the description's words |
|---|---|---|---|
| S1 | "Before I send this to the VP: the new onboarding flow improves 30-day retention by 6 points in a 2-week A/B test. Anything missing?" | yes | "it improves", "A/B results", "before they go to anyone" |
| S2 | "Review our model card: the classifier is 97% accurate and robust to noise." | yes | "97% accurate", "model cards" |
| S3 | "The agent says 'all 40 files verified, tests pass'. Can I merge?" | yes | "verified", "passed" |
| S4 | "Help me design the evaluation for our retrieval system before we run it next week." | yes | "designing a test, benchmark or evaluation plan, before running it" |
| S5 | "The supplier guarantees the sensor never drifts more than 0.1%. Can we drop our calibration step?" | yes | "guarantees", "it never happens" |
| S6 | "Write up my experiment's result for the lab meeting." | yes | "your own summaries before they go to anyone" |
| S7 | "Does this study show the low-emission zone caused the drop in NO2?" | conflict | "it causes", "reviews of someone else's results"; but hard-to-vary fires on "a reason WHY something happened" |
| S8 | "We migrated the database and saw zero errors in staging. Can I say it's done?" | probably | "it works", "passed"; "zero errors" and "done" are not among the listed words |
| S9 | "The post-mortem says the cache was the root cause and removing it fixed the outage. Sign off?" | conflict | "root cause", "post-mortems", "fixed" are in both descriptions |
| S10 | "Stress-test my claim that the new pricing page increased conversions." | conflict, likely lost | "it improves", but "stress-test my thinking" is hard-to-vary's named trigger |

| # | Near miss (should not trigger) | Fires? | Why |
|---|---|---|---|
| N1 | "Why do cats purr?" | no | "Not for looking up facts ... or explaining why something is so" |
| N2 | "Why did churn rise last quarter? My theory is the price rise." | risk | an explanation (hard-to-vary), but "it causes" invites this skill |
| N3 | "Fix the flaky checkout test." | yes, at the end | the agent's closing "fixed" is "your own summaries before they go to anyone"; a routine fix gets the full ledger |
| N4 | "Translate this test report into Spanish." | risk | the report is full of "verified" and "passed"; nothing says translation or editing is out |
| N5 | "How accurate was last year's sales forecast?" | risk | "97% accurate" is a listed trigger; this is a computation, and hard-to-vary also excludes it, so neither skill says whose it is |
| N6 | "Write unit tests for this parser." | risk | "designing a test" |
| N7 | "Is this argument circular?" | no | hard-to-vary's named trigger; nothing here matches |
| N8 | "Which of these two logos is better?" | no | "matters of taste" |
| N9 | "Summarise this paper for me." | risk | "reviews of someone else's results"; the user wants a summary, not a review |
| N10 | "Explain to a new hire how our cache works." | risk | "it works" is a listed trigger word |

**Reading.** It fires correctly on S1 to S6 and probably S8. It is in open conflict with hard-to-vary on S7, S9 and S10. It stays quiet on only three of ten near misses (N1, N7, N8); on six it is at risk because its trigger list is everyday words in quotation marks, and on N3 it would fire by design.

### T1. It fires on everyday words and on every own report, and then requires the full procedure (SERIOUS)

1. **What is wrong.** The description lists common words as triggers and includes "your own summaries before they go to anyone", and the depth rule makes the full procedure compulsory whenever "someone else will read the claim or act on it", which is true of nearly every summary an agent writes.
2. **Evidence.** SKILL.md:3: "Use it whenever a result is about to be stated or accepted - \"it works\", ... \"passed\", \"fixed\" ... and your own summaries before they go to anyone." SKILL.md:86-87: "the full procedure is required when any of these applies: someone else will read the claim or act on it". SKILL.md:89: "the claim is about a learned, simulated or agent-run system" (an agent's own report always is). The short form is allowed only for "a private, reversible, cheap claim" (SKILL.md:92). Round 4 cost: version 5 "$14.13, 244 steps, 84 checker runs, 100 edits" against hard-to-vary's "$0.96, 25 steps" (results.md:140-141).
3. **Effect.** Installed for real, it would run at its round-4 cost (about 15 times hard-to-vary per case) at the end of ordinary coding and writing tasks, for example after every "fixed the test" (N3). Users will either switch it off or pay for ledgers on trivial claims.
4. **Smallest fix.** (a) In the description, replace the bare quoted trigger words with situations and add a stakes condition ("and something rides on it"), and add "Not for ... summarising, translating or editing a report without judging it". (b) In Step 0, make "someone else will read it" alone lead to the short form, and keep the full procedure for money, health, safety, security, anything hard to undo, a claim reused as a premise, or when the user asks. A proposed description is in section 3.2.
5. **Testable?** Yes. A triggering test with 20 to 40 prompts (the twenty above plus more), each run a few times with the skill installed and not in safe mode, counting how often it fires against a should/should-not key (the method of the skill-creator skill's description test). Cost per real task can be measured on a few ordinary tasks (fix a test, write a summary) with and without the change.
6. **Weight: SERIOUS**, because it multiplies the measured cost across routine work.

### T2. Overlap with hard-to-vary, and an instruction to use both (SERIOUS)

1. **What is wrong.** The two descriptions claim the same requests (root causes, post-mortems, why something works), and semantics-audit.md tells the agent to use both skills on one explanation, though the only test of both together found it the worst arm.
2. **Evidence.** This skill: "root cause", "post-mortems" (SKILL.md:3). Hard-to-vary: "Use this whenever someone gives or asks for a reason WHY something happened, works, failed ... root cause, post-mortem, bug hunt". semantics-audit.md:145: "Use both on an explanation that is also offered as a tested result." Round 4: "Giving an agent both skills was worst: the most invented results (one invented pilot and its result), the most cost, and no gain in coverage" (results.md:154); the both arm cost "$26.36, 456 steps, 173 checker runs" (results.md:142). Important limit of that evidence: the wrapper said "Read both SKILL.md files and follow both. For each case, write one answer that contains prove-it-wrong's falsifier ledger, together with what hard-to-vary's report adds" (both_skills_wrapper_SKILL.md:7). So round 4 tested *running both procedures into one answer*; it did not test two installed skills whose descriptions each pick their own requests.
3. **Effect.** With both installed, an agent asked "is this root cause right?" may load both and, following semantics-audit.md:145, merge them: the configuration with the most invented results and the highest cost.
4. **Smallest fix.** (a) Give each description one sentence that hands the other its requests: this skill takes "was the result, fix or benchmark actually tested?"; hard-to-vary takes "does the reason why hold together?". (b) Replace semantics-audit.md:145's last sentence with: "When a report gives both a result and the reason for it, use this skill on the result and hard-to-vary on the reason, one at a time, in separate answers; never run both procedures into one answer (round 4: worst arm)." (c) Remove "root cause, post-mortems" from this skill's list, or qualify it as "a fix or root cause stated as found or fixed".
5. **Testable?** Yes: the triggering test of T1 with both skills installed, scoring which skill fires on S7, S9, S10, N2 and N5; and a small round with both installed normally (not wrapped) to see whether cost and invented results stay at single-skill levels.
6. **Weight: SERIOUS.** The instruction points at the measured worst setup.

### 3.2 What the two descriptions should say

A proposed description for this skill, 970 characters (counted with Python), plain words, no bare trigger words:

> Checks whether a stated result was really tested. For each claim it asks what observation would show it wrong and whether anyone looked, and records the answers in a falsifier ledger that a script checks. Use it when a result is about to be reported, accepted or acted on and something rides on it: a test, experiment, A/B, benchmark or model-card result; a "fixed", "verified", "passed" or "done" report from a person or an agent; a guarantee, a "never" or a "no side effects"; a review of someone else's results; your own report on such work before it goes out; or a test plan before it runs. Not for explaining why something happened or whether a reason holds together (use hard-to-vary), for looking up facts or taste, or for summarising, translating or editing a report without judging it. When a report gives both a result and the reason for it, use this skill on the result and hard-to-vary on the reason, one at a time, never both procedures on the whole report.

For hard-to-vary (not edited here; its file is outside what this audit may change): add "Not for checking whether a reported result, fix or benchmark was actually tested (use prove-it-wrong)." That sentence is 103 characters and the hard-to-vary description in this repository is already 1,022 of the 1,024 allowed, so a phrase of similar length must leave it (for example the clause on building a theory "from nothing", which its own routing table already covers).

---

## 4. Length and cost (lens 2)

### 4.1 Where the cost comes from

What the records show, all from results.md: version 5 took 244 steps for 12 cases (about 20 per case) against hard-to-vary's 25 (about 2 per case); 84 checker runs (7 per ledger, against SKILL.md:200's "Three runs per ledger should be enough"); 100 edits; "it edits row by row and reruns the checker after almost every edit" (results.md:162); in the both arm "One advisory warning was chased 112 times" (results.md:142), named in the version-6 proposals as "the 'no falsifier naming it alone' warning, which agents chased" (results.md:182). The checker's output on all 24 of round 4's ledgers in the two arms that used it shows 0 warnings on 19, 1 on 4, 2 on 1 (evals/checks/checker_on_all_ledgers.txt): the agents cleared almost every warning, though SKILL.md:201 calls warnings "advice".

What I infer, not measured: in a tool-using agent each step re-reads the whole conversation, so the cost grows with the number of steps times the size of what has been read. Reading is about 10,000 words before the first row (SKILL.md 3,847, forcing-questions.md 3,410 "on first use", ledger-format.md 1,309, one or two situation files of about 450 each, often designing-the-test.md 770). Hard-to-vary also has a 3,081-word SKILL.md and modules, so reading alone does not explain a factor of 15. Steps do: 20 against 2. The step count is driven by (a) the checker loop (L1), (b) row-by-row editing of a two-table ledger whose question table must cover 13 questions for every claim (L2), and (c) a separate fact-check pass done after the ledger is written, as a rewrite (SKILL.md:190, "Before checking the ledger, reread the source").

### L1. The warnings: three texts disagree, and the format states a warning as a rule (SERIOUS)

1. **What is wrong.** The skill says both that warnings are advice and that it may not stop until they are dealt with; the test harness says fix until it passes; and ledger-format.md states as a requirement what the checker only warns about, and that requirement pulls against the merge rule.
2. **Evidence.** SKILL.md:201: "Warnings are advice. Act on those that point at a real problem; the rest can stand." SKILL.md:228 (When to stop): "the checker passes, and its warnings are dealt with." run_suite.sh:20: "If the skill has a checking script, run it on each answer and fix the answer until it passes." ledger-format.md:29: "every claim needs at least one row naming it alone", while check_ledger.py:192-193 only warns ("Claim C2 has no falsifier naming it alone"), and SKILL.md:133 says "Rows that would be tested the same way are one row: merge them." Probe pass_04 (one merged row for two claims, as Step 3 asks) draws exactly that warning. Records: 7 checker runs per ledger; one warning chased 112 times.
3. **Effect.** The agent cannot tell when it is allowed to stop, so it reruns the checker after each edit and splits merged rows to silence a warning, costing steps and undoing the merge rule.
4. **Smallest fix.** (a) SKILL.md:228: "the checker shows no errors. Warnings do not stop you: read them once, act on any that names a real problem, and do not rerun the checker for a warning." (b) SKILL.md:200: "Run it once when the ledger is written and once after fixing errors; never more than three times." (c) Delete ledger-format.md:29's "but every claim needs at least one row naming it alone", and delete the warning at check_ledger.py:192-193 (the version-6 proposal, results.md:182, already says so). (d) Make the checker print warnings under a heading "Advice (no rerun needed)". (e) In run_suite.sh:20, say "until it shows no errors".
5. **Testable?** Yes, cheaply: count checker runs, edits and steps per case in the next round (the run's JSON already records cost). A target is at most 2 checker runs per ledger. The wording change can also be probed: the warning text itself can be run on probe pass_04 to confirm it is gone.
6. **Weight: SERIOUS**: the main measured cost driver, and a direct contradiction.

### L2. The question table: the biggest writing load, the padding, and "think first" with no place to write (MODERATE)

1. **What is wrong.** Every question gets a row for every claim (13 x claims), each answer is to be preceded by a written "strongest concrete way this claim could fail", the ledger has no place for that text, and the "does not apply" rows are what both markers counted as padding.
2. **Evidence.** SKILL.md:122: "For each question, first write the strongest concrete way this claim could fail under that question, in this case. Only then answer." The question table has four columns, none for this (ledger-format.md:54). SKILL.md:225: "every question has an answer for every claim". Padding: Opus 22 and GLM "about 37" for version 5 against 10 and "about 3" for hard-to-vary (results.md:130-134); GLM's grades for g1 to g3 give "Padding: ≈12 (the "does not apply" Q-rows ...)" per case (grades_glm.md:16, 68, 117). Version-6 proposals 3 and 4 (results.md:170, 181) already ask to merge tables and group the "does not apply" rows.
3. **Effect.** An answer with three claims needs up to 39 rows; within a 700- or 1,000-word limit the "written" failure modes cannot appear, so either they are skipped (and "think first" is unenforced) or they crowd out case content. Readers see a template.
4. **Smallest fix.** Keep all 13 questions as the thinking checklist (that is where the breadth the markers credited comes from), but change what is written: (a) rows only for *missing* answers, and for *covered* answers that cite evidence; (b) one line for the rest, `Does not apply: Q4 (one arm, one measure), Q8 (nothing fitted)`, each with its exemption in a few words; (c) say where the "think first" text goes: "in the *Where or why* cell of a missing row, as the falsifier itself; elsewhere, in your head". The checker would check the line names every remaining question.
5. **Testable?** Yes: rerun a round's cases with the old and new table, mark padding with a written definition (see E3), and count MUST items found; the checker change is testable with probes.
6. **Weight: MODERATE**: real cost and padding, but the fix is partly already proposed by the owner's version-6 list.

### L3. SKILL.md repeats itself (MODERATE)

1. **What is wrong.** Rules are given two or three times in SKILL.md and again in forcing-questions.md, with small differences of wording.
2. **Evidence.** Section sizes (my count): procedure 1,860 words, routing section 611 (of which the flowchart about 120), hard rules 424, Traps 287. The answer rules at SKILL.md:121-144 are repeated at forcing-questions.md:8-15 (for example "Worries that would fit any claim go in one 'Routine checks' line" against "does not go in the ledger. Put it in one line headed 'Routine checks', or leave it out"). Each Trap restates an earlier rule: "Filling in facts" (SKILL.md:236) is hard rule 11 (220) and Step 7b; "Merging" (240) is SKILL.md:133; "Parking" (244) is Step 5 (171); "Counting confirmations" (246) is hard rule 7 (216); "Trusting a reported test" (243) is hard rule 2 (209). "Not run is never passed" appears at 173 and 208.
3. **Effect.** About 1,000 words read on every use, and two slightly different wordings of one rule to reconcile.
4. **Smallest fix.** Keep in SKILL.md: the rule, Step 0 to Step 8 in short, the 13-question table (it is the checklist used every time), the status words, the hard rules as one line each, the stop rule. Move to forcing-questions.md (which is read anyway): the answer rules in full. Cut: Traps (fold the two not stated elsewhere, "Asking 'is this right?'" and "Letting your own write-up skip the ledger", into the opening), the flowchart (L4). Expected size about 2,700 words.
5. **Testable?** Word count is direct. Whether quality holds needs a round (E1), but no rule is removed, only repeats, which a diff can show line by line.
6. **Weight: MODERATE.**

### L4. The flowchart (MINOR)

1. The mermaid graph (SKILL.md:60-75) restates the step list and adds a maintenance rule (SKILL.md:77).
2. Evidence: every node is a step already listed at SKILL.md:81-202.
3. Effect: about 120 words per run, and one more thing to keep in step with the tables.
4. Fix: move it to a short README for human readers, or drop it. The routing tables do earn their place: the situation table (SKILL.md:47-58) is a one-line decision that saves reading nine of ten files.
5. Testable: by word count; no behaviour should change.
6. **Weight: MINOR.**

### 4.2 What must stay in SKILL.md, what can move, and what to defer

| Part | Where it should be | Why |
|---|---|---|
| The rule, the one example, Step 0 to 8, the 13-question table, status words, hard rules (one line each), stop rule | SKILL.md | used on every run |
| The two routing tables | SKILL.md | cheap; decide what not to read |
| Answer rules in full, reassuring-words table | forcing-questions.md only | already read "on first use" |
| Traps | cut (two kept in the opening) | all but two are repeats |
| Flowchart and its upkeep rule | out of SKILL.md | repeats the steps |
| Worked examples | module (as now) | read only when wanted |
| Design form, short form details | ledger-format.md (as now) | |
| The question table rows for "does not apply" | one line | L2 |
| Fact-check pass | keep, but done before the final write ("reread the source, then write the ledger once") | it is the credited fix (section 2, item 2); doing it as a rewrite after the ledger adds steps |

---

## 5. The checker (lens 3)

**Runs.** Self-test: "self-test passed: 14 of 14". The three worked examples, copied out one per file: all "PASSED: 0 errors, 0 warning(s)". The whole worked-examples.md as one file fails with 14 errors, as its own note expects ("To check one, copy that example alone into a file", worked-examples.md:8): the checker keeps only the last falsifier table and the last question table it finds (check_ledger.py:115-119). All outputs are in `02 Audit B - probes/checker_output.txt`; the table of 29 results is in that folder's README.

**Counts.** Of 15 ledgers that should pass (3 worked examples, 12 probes), 7 passed cleanly, 4 were refused (false alarms) and 4 passed with 6 false warnings. Of 14 ledgers that break a stated rule, 2 were refused for the right reason, 1 was refused with messages that do not name the fault, 1 drew only a warning, and 10 passed silently: 11 misses. Two layout slips drew 10 and 23 error lines that do not name the slip.

### K1. Rules the checker should hold and does not (MODERATE)

1. **What is wrong.** The checker passes ledgers that break rules the skill states, including two that ledger-format.md says it refuses.
2. **Evidence (probe, then the line responsible).**
   - fail_01: a *reported* receipt "the authors' own log summary, section 3" passes. The quotation test `QUOTED` (check_ledger.py:48) accepts an apostrophe after a word as a quotation mark. ledger-format.md:96: "a `reported` receipt must quote the source".
   - fail_11: a *covered* answer "Yes." passes with a warning. check_ledger.py:256 compares the whole cell with `WEAK_EVIDENCE`, so the full stop defeats it. ledger-format.md:72: "'Yes', 'ok', 'fine' and 'n/a' alone are refused."
   - fail_06: Q5 answered "does not apply" for a claim containing "never" passes. forcing-questions.md:117: "Never when any of these is present." No "never" exemption is checked for any question (Q3, Q5, Q9, Q11 have one).
   - fail_05: "this question does not apply here" (six words) passes; only the word count is checked (check_ledger.py:262).
   - fail_03: a *covered* answer citing a *missing* row and another claim's *survived* row passes (check_ledger.py:260 asks only that one cited row be closed).
   - fail_08: a *missing* answer for C1 citing only a row that tests C2 passes; nothing checks that a cited row tests the claim the answer is about.
   - fail_07b: two rows both called F2 pass; `status_of` is a dictionary and the second row overwrites the first (check_ledger.py:161). The checker then warns that "Every falsifier of C1 was sought and survived", which is false.
   - fail_09 and fail_13: the short form may name a *survived* row as missing, or say "missing: none" with two *missing* rows; check_ledger.py:211-217 checks only that the row exists.
   - fail_10 and fail_12: the falsifier "would be shown wrong if the cache did not work in any setting at all" (what SKILL.md:118 calls not a falsifier) passes without a warning, because `MEASURABLE` (check_ledger.py:50) counts "any" as a threshold; a *survived* receipt "ran it" passes, because `RECEIPT_SHAPE` (line 51) counts "ran".
3. **Effect.** "PASSED" is what the agent reports as its receipt for the ledger (run_suite.sh:20 asks for the checker's last line), and the stop rule treats it as completion. By the skill's own question on checks, "has that check ever caught a planted fault?" (SKILL.md:158), these are planted faults it does not catch.
4. **Smallest fix.** Each is a few lines: strip punctuation before the weak-evidence test; require a double quotation mark or matched single quotes for *reported*; refuse a duplicate F-number; require that a cited row name the answer's claim (or `all`); in the short form, require named rows to be open and "none" only when no row is open; refuse "does not apply" for Q5, Q9 and Q11 when a claim line holds a strength word from Step 1's list, and for Q3 when it holds "causes", "improves", "prevents", "reduces"; warn on a *survived* receipt under five words; drop "any", "still", "same" from `MEASURABLE`. Whether a quotation really comes from the source cannot be checked without the source; the docs should say so.
5. **Testable?** Yes, fully: add my fail probes to the self-test as planted faults; each must be refused, and every pass probe must still pass.
6. **Weight: MODERATE.** Each miss is small and the model's judgement does most of the work, but together they make "PASSED" weaker than the skill says it is.

### K2. Warnings that fire on honest text, or advise the wrong thing (MODERATE)

1. **What is wrong.** Three warnings fire where the ledger follows the skill, and one advises labelling a merely reported claim "Well-tested".
2. **Evidence.** pass_05: the sentence "the stale-price claim was not verified by us, and the speed claim is not proven beyond this one week" draws "'verified' while 2 falsifier(s) are open" and two more (check_ledger.py:46, 293-298 ignore negation). pass_06: quoting the dropped word "never" to say it was dropped draws "'never' is in the report but not in 'Claim as it stands'". pass_04: the merged row draws "no falsifier naming it alone" (L1). pass_02c: claim C3, whose only row is *reported* from the claimant ("weekly note: 'cost per answer down 18%'"), draws "Every falsifier of C3 was sought and survived. If that is right, add a 'Well-tested: C3 ...' line" (check_ledger.py:197-201 counts *reported* as survived).
3. **Effect.** An agent clearing warnings (as round-4 agents did, 19 of 24 ledgers at 0 warnings) would delete the honest "not verified", stop quoting the original word, split merged rows, and call the claimant's own report "well-tested", against hard rule 2.
4. **Smallest fix.** Skip lines where the strength word follows "not", "never been", "no longer", or sits inside quotation marks; delete the "naming it alone" warning; in the well-tested warning count only *survived* and *outside the claim*, and word it "Every falsifier of C3 was run and survived".
5. **Testable?** Yes: probes pass_02c, 04, 05 and 06 must then show 0 warnings, and a ledger using "verified" for an open row must still warn.
6. **Weight: MODERATE.**

### K3. Brittle reading of the tables (MODERATE)

1. **What is wrong.** Natural variations of the format produce floods of errors that do not name the cause.
2. **Evidence.** pass_02d and 02e: Claims cell "C1-C3" or "C1 to C3" with three claims gives 13 errors "no answer for C2" (`ids_in`, check_ledger.py:90-91, reads only the two ends; with two claims, pass_02, a range happens to work). pass_08: a *covered* answer quoting "F2 score 0.91" is refused as citing open row F2 (any "F" plus digits is read as a row, line 249; "F1 score" is a standard measure name in model evaluation, one of the skill's own situations). pass_09: question cells "Q5 Worst single case" give 33 errors (line 227 requires the cell to be only Q-numbers). fail_14: rows split into two falsifier tables give 10 errors about rows "not in the falsifier table" (only the last table is kept, lines 115-119). fail_15: a first column headed "ID" gives 23 errors, the first saying each falsifier's text "should look like F1", because `column(header, "f")` matches the first header *starting* with "f", which is then "falsifier" (lines 82-87, 127).
3. **Effect.** Each produces one or more extra checker loops spent finding a cause the message does not give.
4. **Smallest fix.** Expand ranges ("C1-C3", "C1 to C3"); read only `F` followed by digits that is not followed by " score" or "-score", or better, require row citations in the form "F2" at the start of the cell or after "see"; accept "Q5 Worst single case" by reading the leading Q-numbers; merge all tables that have the falsifier columns; match column names exactly (after lower-casing) and, when a column is missing, name the expected header.
5. **Testable?** Yes: the five probes above must pass or give one clear message.
6. **Weight: MODERATE.**

### K4. The self-test's "good" ledger models what the skill forbids (MINOR)

1. The sample ledger that the self-test calls good answers Q2 to Q13 "does not apply" with one generic reason, including Q5 for a claim with "guarantees".
2. check_ledger.py:303: "the failure considered does not arise for this one claim here", for every question 2 to 13; the claim at line 304 says "**guarantees**"; forcing-questions.md:117 forbids "does not apply" for Q5 then.
3. An agent told to "apply the rules listed at the top of the script by hand" (SKILL.md:202) reads this file and its sample.
4. Write the sample with real exemptions, and answer Q5 *missing* or *covered*.
5. Testable: the self-test must still pass 14 of 14 (or more, with K1's additions).
6. **Weight: MINOR.**

---

## 6. The evaluation set (lens 4)

### E1. Too small, with one run per arm, to judge a refinement on quality (SERIOUS)

1. **What is wrong.** Each round has 6 or 12 cases, each arm ran each case once, and the arms' MUST totals differ by one to four items, inside what one more run could change.
2. **Evidence.** Round 4: 53 MUST items, version 5 "37 / 11 / 5" and hard-to-vary "38 / 8 / 7" (Opus), "40 / 9 / 4" and "41 / 4 / 8" (GLM) (results.md:130-134). results.md:164: "12 cases and two markers". The skill's own Q9 asks "How many independent draws ...?" and its designing-the-test.md:56 asks for case-by-case wins and losses with a sign test. The GLM marker on its first part: "the partial/found boundaries ... could shift totals by one or two points either way" (grades_glm.md:189).
3. **Effect.** A refinement that cuts cost (the main aim here, T1, L1, L2) cannot be shown to keep quality: a loss of 2 or 3 MUST items would be invisible.
4. **Smallest fix.** Before running, write a pass mark as a non-inferiority margin (for example "refined finds at least version 5's MUST items minus 3 of 53, and costs at most half"), run each arm 3 times per case on the 12 cases, and report per-case wins, losses and ties with a sign test, as the skill asks of others.
5. **Testable?** It is itself the test; its cost is the main limit (three runs of the cheapest arm, about $3 for hard-to-vary and about $42 for version 5 at round-4 prices).
6. **Weight: SERIOUS** for the question asked here, "fit to test a refinement".

### E2. No clean held-out cases left, and exposure not recorded (MODERATE)

1. **What is wrong.** Every round's cases have now shaped the skill or its proposals, rounds 3 and 4 do not record that the case writers had not seen the skill, two round-4 cases are in the style of the project the skill has its own file for, and each marker marked cases it had written.
2. **Evidence.** README.md:23: "Only the held-out cases, written by someone who had not seen the skill, count." Only round 2 says so (results.md:36); rounds 3 and 4 say "written by GLM" and "6 written by Opus 5.5" (results.md:71, 120) and nothing on exposure; by the skill's own rule (SKILL.md:131, "Cannot tell means missing") that is *missing*. results.md:120: "Two of Opus's cases are in the style of our project's version reports", and the skill carries references/situations/our-thinking-machine-project.md. Round 3 led to version 5 (results.md:102-115), round 4 to the version-6 list (results.md:175-182). Marking: Opus 5.5 and GLM each marked all 12 cases (results.md:126), and each wrote 6 (marking.md:3, 162).
3. **Effect.** A refinement tested on rounds 2 to 4 is tested on cases that helped make it; results on the project-style cases favour this skill for a reason other than its method.
4. **Smallest fix.** A round 5 of fresh cases, written by a writer recorded as not having seen the skill, with no case in the project's style unless reported separately; markers who did not write the cases they mark (or report each marker's own cases apart). Move rounds 2 to 4 to "development".
5. **Testable?** It is a procedure; it can be audited by recording who saw what before writing.
6. **Weight: MODERATE.**

### E3. Blinding, the padding count and the headline (MODERATE)

1. **What is wrong.** The neutral names hide little, padding has no written definition, and the summary sentence on round 4 hides a half where the Opus marker preferred hard-to-vary.
2. **Evidence.** One mapping for all cases and markers: "Set 1 = prove-it-wrong version 5; Set 2 = both skills together; Set 3 = hard-to-vary skill" (heldout_round4/key.txt). The ledger format names its arm: GLM writes of Set 1 that it "buries its real content in generic template rows" (grades_glm.md:189). Padding: the marking lists define only MUST-NOT X3, "more than a third of the points are generic checks" (marking.md:166), not the per-case padding count, and "GLM counted every 'does not apply' row as padding in one of its four parts, and not in the others" (results.md:137); GLM's padding for version 5 is about 9 to 12 per case on g1 to g3 (grades_glm.md:16, 68, 117) and 0 or 1 on the other nine cases (grades_glm.md:205-628). Headline: "Version 5 is the most effective of the three on these 12 cases, by both markers" (results.md:147), while the Opus marker on o1 to o6 wrote "Set 3 is the strongest on the amended lists: 19 of 23 MUSTs found ... Set 1 is a close second: 17 found" (grades_opus.md:599); version 5 won the g-half (grades_opus.md:283).
3. **Effect.** "Padding", the measure most likely to move under a refinement aimed at fewer rows, is the least reliable; and the headline overstates the margin, by the skill's own Q5 (worst subgroup).
4. **Smallest fix.** Shuffle the Set names per case; add a written padding definition to the marking brief ("a row or point that names nothing particular to this case; a 'does not apply' row with a case-specific reason is not padding"); report each half and each marker beside the total.
5. **Testable?** Partly: ask each marker, after marking, to guess which Set is which arm; the guess rate shows how blind the marking was.
6. **Weight: MODERATE.**

### E4. run_suite.sh (MODERATE)

1. **What is wrong.** The harness cannot test triggering, its prompt adds its own push to the checker loop, and it does not make a fresh folder.
2. **Evidence.** Flags, checked with `claude --help` (Claude Code 2.1.292): `-p`, `--model`, `--safe-mode`, `--output-format json` and `--allowedTools` all exist. `--safe-mode`: "Start with all customizations (CLAUDE.md, skills, installed plugins, ...) disabled", so the skill is read as files by instruction (run_suite.sh:20, "Read ./skill/SKILL.md first and follow it") and its description is never used. run_suite.sh:20: "fix the answer until it passes". The prompt frames the task as "review claims before they are accepted or acted on", this skill's own description wording, for both arms. No `--max-budget-usd` (the both arm cost $26.36). Nothing confines the file tools to the work folder ("Use only the files in this folder" is a request). All cases run in one session, so later cases carry earlier ones' context and cost per case is an average. Dry run with a stand-in `claude` (`02 Audit B - probes/run_suite_dry_run.txt`): run twice into the same folder, the second agent sees the first run's `answers/case_g1.md`, a second copy of the skill at `skill/piw_copy/SKILL.md`, and the cases again at `cases/cases/` (`mkdir -p` and `cp -r` into an existing folder, run_suite.sh:15-18), though the header says it "makes a fresh working folder" (line 4).
3. **Effect.** Triggering (T1, T2) has never been tested; the measured checker loop is partly the harness's; a reused folder contaminates an arm silently.
4. **Smallest fix.** Refuse to run if the work folder exists; add `--max-budget-usd`; run one session per case; in the prompt say "until it shows no errors" and use neutral wording ("A skill for reviewing claims is installed ..."); add a separate triggering script that installs the skill normally (no `--safe-mode`) and records which skill loads.
5. **Testable?** Yes, the folder check by a dry run like mine; the rest by reading the run JSON.
6. **Weight: MODERATE.**

### E5. The evals ship inside the skill (MODERATE)

1. **What is wrong.** The installed skill carries its own test set, marking lists and keys, and its main file points the agent to them.
2. **Evidence.** evals/ holds 55,634 words, against 21,180 for SKILL.md, references and script together (my count). evals/README.md:3: "Open it when you test or change the skill, never while using it on a real claim." SKILL.md:43 routes "testing or changing this skill" to `evals/README.md`. run_suite.sh:17 deletes evals/ from its copy, which protects test runs but not an installed copy.
3. **Effect.** Any agent with the installed skill can read every marking list; a future test agent run without the harness is contaminated; the package is more than twice the size it needs.
4. **Smallest fix.** Keep the evals beside the skill, not in it (for example a sibling folder `prove-it-wrong-tests/`), and drop SKILL.md:43's row or point it to that folder by name with "not installed with the skill".
5. **Testable?** Yes: list the installed folder; it must hold no file from evals/.
6. **Weight: MODERATE.**

---

## 7. Clarity for the agent (lens 5)

### A1. "missing" names two things (MODERATE)

1. The status "missing" means "nobody sought it"; the answer "missing" means "not shown" and may cite a *failed*, *blocked*, *pending* or *planned* row.
2. ledger-format.md:46: "`missing` | nobody sought it"; ledger-format.md:70: "`missing`: cite the F-number of a `missing`, `blocked`, `failed`, `pending` or `planned` row".
3. A question whose falsifier was run and *failed* is answered "missing", which a reader takes to mean "not tested"; in design mode every question is "missing" though everything is planned.
4. Rename the answer word "open" (or "not shown"), keeping "missing" for the status only; the checker accepts both for one version.
5. Testable with probes; and by asking a reader what a row means.
6. **Weight: MODERATE** (the owner's "one word per thing").

### A2. "Well-tested" has three definitions (MODERATE)

1. SKILL.md, ledger-format.md and the checker disagree on whether *reported* rows can make a claim well-tested.
2. SKILL.md:180: "a claim whose main falsifiers were sought and survived"; ledger-format.md:15: "all sought and survived or were reported"; check_ledger.py:199-201 counts *reported* and tells the agent "Every falsifier ... was sought and survived" (probe pass_02c). Hard rule 2 (SKILL.md:209): "Mark that falsifier *reported*, not *survived*".
3. In review mode, where "most of what you have is *reported*" (SKILL.md:243), the agent is led to call a claimant's own report well-tested.
4. One definition: "Well-tested: its main falsifiers were run and survived, by you or by someone independent of the claimant". If reported rows are meant to count, say "well-tested as reported" and keep the word apart.
5. Testable with probe pass_02c.
6. **Weight: MODERATE.**

### A3. Worked examples break the rule they model (MODERATE)

1. Examples 1 and 2 state facts about their case that are not quoted, against "Quote it, or it is missing" and Step 7b.
2. worked-examples.md:77 (example 2, Q6): "F1: before and after ran on different days and machines"; :72 (Q1): "only ordinary CI timing was tried"; :84 (Q13): "none skipped or retried away, per the CI history"; the only text quoted from the source is the claim and "CI runs 1 to 50 linked below". worked-examples.md:39 (example 1, Q6, *covered*): "all arms ran on identical lessons, goals and programs, as reported", with no quotation, though ledger-format.md:72 says "A fact from the source is quoted word for word."
3. Agents copy examples; a rule contradicted by its example is learned as optional. Filling in facts was version 4's main flaw (results.md:88).
4. Quote the source in those cells, or rewrite as conditions ("if before and after ran on different machines, ...") or "not reported".
5. Testable: a reread against the rule; a checker warning for *covered* answers with neither a quote nor a cited row already exists (line 258) and fires on none of these because they cite F-rows or say "worked out".
6. **Weight: MODERATE.**

### A4. "Three rules" followed by seven (MINOR)

forcing-questions.md:8 "Three rules make the answers useful:" then seven bullets (lines 9-15). Confusing count left over from version 2 ("the three answer rules", results.md:28). Fix: "These rules make the answers useful:". Testable by reading. **MINOR.**

### A5. "F1" and "F2" mean two things (MINOR)

semantics-audit.md:50-53 calls the fidelity conditions "F1" and "F2"; the ledger's rows are F1, F2. An agent writing "fails F2 (the whole)" in a *Where or why* cell has cited row F2 to the checker (compare probe pass_08). Fix: call them "component fidelity" and "whole fidelity" in that module. Testable by search. **MINOR.**

### A6. Several words for one thing (MINOR)

The thing a claim lacks is called "missing test conditions" (SKILL.md:3), "missing condition" (SKILL.md:30), "gap" (SKILL.md:179), "missing tests" (results.md:97) and, for scope, "caveats" (SKILL.md:180). The owner asks for one word per thing. Fix: "missing condition" throughout, "limit of scope" for the other. Testable by search. **MINOR.**

### A7. Question numbers without names (MINOR)

The ledger shows "Q5" only, and the checker refuses "Q5 Worst single case" in the question cell (probe pass_09, 33 errors; check_ledger.py:227). A reader must look up 13 numbers. Fix: accept and recommend the number plus its short name. Testable with pass_09. **MINOR.**

### A8. "One next test" or none (MINOR)

SKILL.md:224: "the report always carries one next test"; worked-examples.md:124: "Next test: none needed for this claim." Both have a reason; say in SKILL.md that a well-tested claim may write "none needed" with the condition under which a test would be needed. **MINOR.**

### A9. Plain notes at the top, and files the skill does not carry (MINOR)

SKILL.md opens with a slogan, not a note saying what the file is ("A claim is worth as much as the tests that could have sunk it", line 8); evals/results.md opens with fingerprints (line 3). The project file cites "file 05", "file 06" and CANNOT_CLAIMS.md (our-thinking-machine-project.md:5, 32-34), which are not in the skill, and opens for one project ("built from Pinker's ideas"), so it should say so in its first line for any other user. Fix: one plain sentence at the top of each. **MINOR.**

---

## 8. Findings removed after re-reading the skill against this list

- **"SKILL.md sets no limit on checker runs."** Removed: SKILL.md:200 says "Three runs per ledger should be enough." Kept only as the contradiction in L1.
- **"The skill never says warnings are optional."** Removed: SKILL.md:201 says so. Reframed as L1.
- **"Shared 'does not apply' rows are not allowed."** Removed: ledger-format.md:66 allows them, and the self-test checks it. L2 now asks only for one line by default.
- **"There is no path for a well-tested claim."** Removed: Step 6, the `Well-tested:` line and worked example 3 give one. Kept as A2 (its definition) and in section 2 as a strength.
- **"The evals README does not warn against reading the evals."** Removed: evals/README.md:3 does. Reframed as E5 (installed copies).
- **"run_suite.sh uses flags that do not exist."** Removed: all five flags are in `claude --help` for 2.1.292.
- **"The description does not mention hard-to-vary."** Removed: it does ("use hard-to-vary for that, if available"). Reframed as T2 (overlapping words).
- **"A claim range always breaks the checker."** Narrowed: with two claims "C1-C2" passes (probe pass_02); only three or more claims fail (K3).
- **"'n/a' as evidence slips through."** Removed: `WEAK_EVIDENCE` holds "n/a" and it is refused; the gap is only with punctuation (K1, "Yes.").

## 9. Limits of this audit

- No model call was made, so the triggering judgements in section 3 are readings, and the cost diagnosis in section 4 rests on the counts in results.md, not on transcripts (the test-runs zip is not in the folder).
- I read nine of the ten situation files only in their opening and routing lines.
- The probes test the checker against rules as the skill states them; whether those rules are the right ones is Audit A's lens.
