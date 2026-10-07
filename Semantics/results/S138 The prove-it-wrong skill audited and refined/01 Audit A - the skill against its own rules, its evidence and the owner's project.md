# Audit A: the prove-it-wrong skill against its own rules, its evidence and the owner's project

*What this file is: the first of two independent audits of the owner's "prove-it-wrong" skill (version 5 by its own record), log S138, decision S93 ("And after that, can you audit the the following skill and refine"). This audit reads the skill through one lens: the skill's own rules applied to itself, the evidence it gives for itself, and how faithfully it carries the owner's theory and the owner's later decisions. The second audit (file 02) reads it as a skill; I did not read it. Nothing here edits the owner's files: every run was on a copy in a scratch folder outside git. Written 7 October 2026.*

**How to read it.** Section 1 says what the skill does well and must keep. Section 2 applies the skill to itself, with a full falsifier ledger in its own format, checked by its own script. Section 3 lists the findings, each with what is wrong, the evidence, the effect on a user, the smallest fix, how to test the fix, and a weight (SERIOUS, MODERATE or MINOR). Section 4 judges the five "Proposed for version 6" items. Section 5 lists findings I dropped on re-reading because the skill already covers them. Line numbers are those of the files as received, in `tests/S138 Material - the owner's prove-it-wrong skill, as received/prove-it-wrong/`.

**Words.** Where I speak for the owner I use the owner's words since S133: *handed in* (given to a system by its makers), *found* (kept by trial from a list against answers it was given) and *built* (worked out by the system itself). The skill's own words are quoted as the skill writes them.

---

## 1. What the skill does well, and must keep

A refinement must not lose any of these.

1. **A test is only as good as the result that could have sunk it, and "not run" is never "passed".** SKILL.md line 8: "A claim is worth as much as the tests that could have sunk it"; hard rule 1, line 208: "Not run is never passed." This is the skill's centre, and it is the same lesson the project learned the hard way (the S136 readers found a viability report whose read-me was surer than its report).
2. **Someone else's record is *reported*, not *survived*.** Hard rule 2, line 209: "A record made by anyone else is a claim that a check happened." The status table keeps the two apart (ledger-format.md line 44). In round 4, within the same cases, version 5 stated the fewest unreported facts under both markers (2 and 0 MUST-NOT violations, against 6 and 2 for hard-to-vary; recounted by me from both grade files).
3. **Do not prosecute; a well-tested claim is reported as well tested.** Hard rule 10 (line 219), "A mostly covered ledger is a success" (line 144), and Step 6's rule that a *held if* must be able to overturn the claim (line 180), with worked example 3 showing it. This came from round 3, where the Opus marker found version 4 adding doubts to a well-tested claim (results.md line 130). It matches the theory's Part 0: "A claim that no argument rules out is only not ruled out" (107, line 8): the skill neither inflates nor deflates.
4. **The fact-check pass and "not reported is not not done".** Step 7b, lines 190 to 195, and hard rule 11. Whatever caused the drop (see finding M5), version 5's answers were the most careful about facts within round 4.
5. **Rival explanations written out in full** (line 134 to 139; Q3 at forcing-questions.md lines 63 to 83). This was the fix for round 2's clear loss (results.md lines 96 to 97).
6. **The checker is honest about what it is.** It prints plain words, exits 0 or 1, keeps its rules at the top so they can be applied by hand (check_ledger.py lines 12 to 35; SKILL.md line 202), and its self-test passes. My run: `self-test passed: 14 of 14`; each worked example, cut out alone, printed `PASSED: 0 errors, 0 warning(s)`.
7. **The evaluation's fairness rules, and its honesty about losses.** Marking lists written and fingerprinted first, the agent under test never sees them (run_suite.sh line 17 deletes `evals/` from its copy), neutral names for markers, a rival arm, the model named exactly (README lines 20 to 25). I recomputed every round-4 fingerprint: all 12 case files and `marking.md` match `fingerprints_before_runs.txt`. The results file reports round 2's loss plainly (line 89) and calls round 3 "about even, with different strengths", not a win (line 144). Keep this honesty; finding S1 asks only that round 4's headline be held to the same standard.
8. **The project file's habits.** Map each claim onto the register of claims the project cannot make; separate inherited from new credit; list what was handed in (our-thinking-machine-project.md lines 164 to 166, which matches the theory's inherited provenance, D12.4); engine artefacts, realistic observers and the chance band (lines 197 to 199); one request to the engineer with a pass mark, and the result in plain words for the owner (lines 203 to 205).
9. **Six semantics checks that match the current theory well:** A3 (production is not identification; 107 Part III, "The respect is the query"), A4 (parts as well as whole, F1 and F2), A7's rule that a later copy of a record is not a second witness (107 line 211: "a later record made from the carrier carries that provenance, not a second, independent one"), A8 (a failed test rules out the bundle of theory, background and instrument; 107 Part IX, K3), A10 (a repair must protect what it was meant to protect; "three different attributions", 107 Part XI) and A12 (a finite list of failures does not rule out a bypass; 107 Part XIII).
10. **One next test** at the end of every ledger (line 230).

---

## 2. The skill applied to itself

### 2.1 The claims frozen, and why these

I froze the five claims the results file makes about round 4, the round the skill rests on, and one claim from the worked examples that I could rerun. Each is quoted word for word.

### 2.2 The ledger, in the skill's own format

C1. "Version 5 is the most effective of the three on these 12 cases, by both markers"
C2. "The fact-check pass worked."
C3. "Giving an agent both skills was worst: the most invented results (one invented pilot and its result), the most cost, and no gain in coverage."
C4. "The markers agree on version 5 first for reliability and breadth."
C5. "Hard-to-vary stays close on MUST coverage. It is far cheaper (about 15 times) and pads far less."
C6. "Each ledger passes `scripts/check_ledger.py`."
Source: evals/results.md lines 191, 196, 197, 198 and 208 (C1 to C5); references/worked-examples.md line 8 (C6); the marks themselves are in evals/heldout_round4/grades_opus.md and grades_glm.md.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | Counting MUST items found in full, another arm finds at least as many of the 53 items as version 5 under at least one marker | failed | counted from the totals in both grade files: hard-to-vary 38 against 37 (Opus), 41 against 40 (GLM) | C1 holds on items missed and partly found, not on items found in full |
| F2 | C1 | Scoring each case found = 1 and partly = 1/2, version 5 is ahead of hard-to-vary in no more of the 12 cases than it is behind, under either marker | failed | computed case by case from the summary tables: Opus 3 ahead, 3 behind, 6 level; GLM 3 ahead, 2 behind, 7 level | on MUST coverage the two arms are level case by case; C1 rests on missed items, MUST-NOT, extra credit and rankings |
| F3 | C1 | Version 5 has more missed MUST items, or more MUST-NOT violations, than hard-to-vary under at least one marker | survived | counted from both grade files: missed 5 against 7 (Opus) and 4 against 8 (GLM); MUST-NOT 2 against 6 and 0 against 2 | none |
| F5 | C1, C4 | On the three cases nearest the owner's use (o4 agent self-report, o5 and o6 version reports), version 5 finds fewer MUST items in full than hard-to-vary under both markers | failed | counted from grades_opus.md lines 564 to 566 and grades_glm.md lines 656 to 658: 5 against 7 (Opus), 7 against 8 (GLM) | the lead does not hold on the subgroup nearest the owner's use; C1 must say so before it is used there |
| F12 | C4 | In at least two of the six marking sessions' own overall judgements, an arm other than version 5 is named first or version 5 is named last | failed | read in grades_opus.md line 599, "Set 3 is the strongest on the amended lists"; grades_glm.md line 189, "Set 1 thinnest"; line 685, "Set 2 is the strongest overall" | C4 holds for totals added across sessions, not for the markers' own verdicts: version 5 named first in 3 of 6 |
| F6 | C2 | An arm identical to version 5 without Step 7b, run on the same 12 cases with the same markers, has no more MUST-NOT violations than version 5 | missing | none | credit to the fact-check pass unmeasured: it came with ten other changes (results.md lines 149 to 159), a word limit raised from 700 to 1,000, and new cases |
| F7 | C2 | Hard-to-vary, unchanged between rounds 3 and 4, moves its MUST-NOT violations per case by at least as much as version 4 to version 5 did, under at least one marker | failed | computed from results.md tables: Opus, hard-to-vary 0 of 6 cases to 6 over 12 (+0.5 per case), version 4 to 5: 4 over 6 to 2 over 12 (-0.5 per case) | the drop across rounds cannot be credited to version 5; only the within-round comparison stands |
| F9 | C3 | The violations counted as invented results in the both arm are blocked rows in the skill's own format (who could run it, and its pass mark), and without them "both" has fewer violations than hard-to-vary under at least one marker | failed | read in grades_opus.md lines 69, 184, 404 and grades_glm.md lines 80, 271, 492, for example "HR runs one pilot team before Q3 2026; passes near 0.4", status blocked; without these three rows Opus counts 4 against hard-to-vary's 6 | "the most invented results" and the named "invented pilot" rest on reading a pass mark as a result |
| F10 | C3 | Under at least one marker, the both arm is ranked first in more cases than hard-to-vary | failed | counted from the GLM summary tables: both 4 cases, hard-to-vary 2; results.md line 208 itself says the markers "disagree on hard-to-vary against 'both' for second place" | "worst" holds for cost and violations as counted, not for rankings |
| F11 | C3 | The both arm cost no more than version 5 or hard-to-vary in round 4 | reported | results.md: "both: $26.36, 456 steps, 173 checker runs" against "version 5: $14.13" | none, as reported |
| F21 | C3 | Run with a 2,000-word limit on the same 12 cases, the both arm finds at least as many MUST items as version 5, whose ledger it contains by its wrapper's design | missing | none | "no gain in coverage" held if the 1,000-word limit did not squeeze the combined answer |
| F13 | C5 | Version 5 costs less than 10 times hard-to-vary in round 4, or hard-to-vary pads no less than version 5 under either marker | reported | results.md: "version 5: $14.13" and "hard-to-vary: $0.96"; padding 22 against 10 (Opus), "about 37" against "about 3" (GLM) | none, as reported |
| F14 | C5 | Scoring found = 1 and partly = 1/2, hard-to-vary is more than 2 of the 53 MUST items behind version 5 under either marker | survived | computed from the totals in both grade files: 42 against 42.5 (Opus), 43 against 44.5 (GLM) | none |
| F15 | C6 | Copied alone into a file, at least one of the three worked examples gets an error from the checker | survived | ran python3 -I scripts/check_ledger.py on each example cut out of worked-examples.md; each printed "PASSED: 0 errors, 0 warning(s)" | none |
| F16 | C6 | A worked example that passes the checker still carries a status that contradicts its own receipt | outside the claim | none | C6 claims only that the checker passes; example 1's F5 (survived, with a sign test p = 0.375 for "no more cases than chance would give") lies outside it |
| F17 | C1, C2, C3 | The 36 round-4 answers and the dated round-4 plan, from the test-runs zip, show at least one of six sampled grades misread or a headline measure other than missed items fixed before the runs | blocked | the owner holds the test-runs zip (results.md line 53); pass if 6 of 6 sampled grades match the answers' text and the plan predates the runs | until then every mark rests on the markers' records alone |
| F19 | C1 | Re-marked with all three arms' answers rewritten into one common layout, at least one marker ranks a different arm first | missing | none | C1 held if the markers' choices did not follow the visible format (the Opus marker names "the long 'does not apply' Q-tables in Sets 1 and 2") |
| F20 | C1, C3 | A second run of each arm on the same 12 cases changes the arm ranked first by either marker | missing | none | one session per arm is one draw; C1 held for this draw only |
| F22 | C1, C2, C3 | At least one of the 12 round-4 case files or the marking file differs from its fingerprint taken before the runs | survived | ran sha256sum on cases/*.md and marking.md in heldout_round4; all 13 match fingerprints_before_runs.txt | none |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1, C3, C4, C5 | covered | scoped in the source: "on these 12 cases" and the heading "Round 4: 12 fresh blind cases, three arms" |
| Q1 | C2 | missing | F7: "worked" is stated without a scope, and the measured drop spans two rounds |
| Q1 | C6 | covered | F15: each example checked alone, as line 8 asks: "To check one, copy that example alone into a file" |
| Q2 | C1, C2, C3, C4, C5 | covered | run_suite.sh removes the marking lists from the agent's copy: "the marking lists must never reach the agent under test" |
| Q2 | C6 | does not apply | the failure considered is a pass guaranteed by construction; C6 claims only the checker's printed result, which F15 reran |
| Q3 | C1 | missing | F19: the markers could see which answers were ledgers |
| Q3 | C2 | missing | F6: ten other changes and a new word limit arrived with Step 7b |
| Q3 | C3 | missing | F21: the word limit, not the second skill, could explain the loss |
| Q3 | C4 | missing | F12 |
| Q3 | C5, C6 | does not apply | both are measurements with no cause or credit in them, which is the question's stated exemption |
| Q4 | C1 | covered | worked out: missed = 53 minus found minus partly, so "fewest missed" and "most found or partly" are one measure, counted once here |
| Q4 | C3 | missing | F21: by its wrapper the both arm contains version 5's ledger, so the two arms are not independent |
| Q4 | C2, C4, C5, C6 | does not apply | the failure considered is two measures agreeing by construction; each of these rests on one measure or on markers who worked "blind and apart" |
| Q5 | C1 | missing | F5: the worst subgroup is the owner's own kind of report |
| Q5 | C2 | covered | version 5's worst cases are quoted in the grades: "120 cast cylinders" (g3) and "the load the flakiness was observed under" (o4), both counted in the 2 |
| Q5 | C3 | missing | F9 |
| Q5 | C4 | missing | F12 |
| Q5 | C5 | covered | computed per case: the widest gap is g4, where version 5 leads 3.5 against 1.5 under both markers; overall F14 |
| Q5 | C6 | covered | F15: every example run on its own |
| Q6 | C1 | missing | F19 |
| Q6 | C2 | missing | F7: different cases, lists and word limits across the two rounds |
| Q6 | C3 | missing | F21 |
| Q6 | C4 | missing | F12 |
| Q6 | C5 | covered | same cases, same model: "all on `claude-sonnet-5`, answers up to 1,000 words" |
| Q6 | C6 | covered | F15: the delivered checker; checks/delivered_matches_tested_version5.txt says "(no differences)" |
| Q7 | C1 | missing | F5: the marking lists stand in for the owner's use, and on the owner's kind of report they point the other way |
| Q7 | C2 | missing | F6: "worked" is a claim that the pass produced the drop; the evidence is a before and after |
| Q7 | C3 | missing | F9: a pass mark counted as a result |
| Q7 | C4 | missing | F12: totals added across sessions offered for the markers' verdicts |
| Q7 | C5 | covered | worked out: cost is the dollars each run printed, the claim's own unit |
| Q7 | C6 | covered | worked out: the claim is about the checker's output only, and F15 reads that output |
| Q8 | C1, C2, C3 | covered | F22: the skill, tuned on rounds 1 to 3, met 12 cases fingerprinted before the runs |
| Q8 | C4, C5, C6 | does not apply | the failure considered is a fitted part meeting new cases; these claims report counts and a rerun, nothing fitted |
| Q9 | C1 | missing | F20: one session per arm; computed sign tests on rankings: 7 ahead, 3 behind, p = 0.34 (Opus); 7, 4, p = 0.55 (GLM) |
| Q9 | C2 | missing | F6: 2 and 0 violations against 6 and 2 are small counts |
| Q9 | C3 | missing | F20 |
| Q9 | C4 | missing | F12: two markers, six sessions |
| Q9 | C5 | covered | computed: the cost ratio was about 5 in round 3 ("$2.18" against "$0.41") and 14.7 in round 4, two draws the same way |
| Q9 | C6 | does not apply | the failure considered is luck; a fixed checker on three fixed files prints the same each time |
| Q10 | C1 | missing | F17: the dated plan for the headline measure is not in the folder |
| Q10 | C2, C3, C4, C5 | covered | F22: lists fingerprinted before the runs, and X2 is in the common MUST-NOT written then |
| Q10 | C6 | does not apply | the failure considered is a test chosen after the results; a rerun of a fixed check leaves nothing to choose |
| Q11 | C1 | missing | F17: the answers are not in the folder; the grade files are the only record |
| Q11 | C2 | missing | F17 |
| Q11 | C3 | missing | F17 |
| Q11 | C4 | covered | read in the grade files themselves: grades_opus.md line 599, "Set 3 is the strongest on the amended lists" |
| Q11 | C5 | covered | F13, as reported by each run |
| Q11 | C6 | covered | F15 |
| Q12 | C1 | missing | F5: if C1 is used to adopt version 5 for the owner's project, it should hold on o4 to o6 |
| Q12 | C2 | covered | computed: per case, cost $0.36 (version 4) against $1.18 (version 5), checker runs 4.2 against 7, steps 13 against 20 |
| Q12 | C3 | covered | F11 |
| Q12 | C4 | missing | F5 |
| Q12 | C5 | covered | computed: the 15-fold cost buys 0.5 (Opus) and 1.5 (GLM) of 53 weighted MUST points, F14 |
| Q12 | C6 | covered | F16: passing the checker does not certify a status, outside the claim |
| Q13 | C1 | missing | F1: counting found in full rather than missed reverses the order |
| Q13 | C2 | covered | the grades quote both of version 5's Opus violations as X2, "states a fact the case does not give" |
| Q13 | C3 | missing | F9 |
| Q13 | C4 | missing | F12 |
| Q13 | C5 | covered | the source counts its own artefact: "GLM counted every 'does not apply' row as padding in one of its four parts" |
| Q13 | C6 | covered | F15: all three examples counted |

Well-tested: C5 (on the runs' reported costs) and C6.

Claim as it stands: On these 12 cases, in one run per arm, version 5 missed the fewest MUST items, stated the fewest unreported facts, earned the most extra credit and was ranked first most often, by both markers' totals; hard-to-vary found as many items in full or more, the two were level case by case, and on the three cases nearest the owner's use (o4, o5, o6) version 5 found the fewest. The fact-check pass came with ten other changes; what lowered the violations is not measured. "Both skills" cost the most and gained no coverage; "the most invented results" held if a pass mark is read as a result. The markers' own verdicts named version 5 first in 3 of 6 sessions. Hard-to-vary is about 15 times cheaper and pads less. The worked examples pass the checker.
Next test: ask the owner for the test-runs zip named in results.md line 53, and read the round-4 plan, the three blocked rows in their answers, and six sampled grades against the answers (F17). It costs nothing to run and could settle F9 and F17.

**The checker on this ledger.** `python3 -I scripts/check_ledger.py ledger.md` on a scratch copy. First run: one error (I had cited a failed row for a *covered* answer); second run: `PASSED: 0 errors, 0 warning(s).`; two more runs, after a wording fix and a line-number fix that changed no row's meaning, printed the same. A last run on the ledger as copied into this file also passed. That is more runs than the three SKILL.md line 200 allows; the extra ones checked corrections and the copy, not errors.

**What writing it taught me about the skill.** Two things. First, five of the rows I most needed (F1, F2, F5, F9, F12) are *failed*: the test was run and went against the claim. The question table then forced me to answer those questions *missing*, though nothing was missing: the test was sought and found something. That is finding M2. Second, six claims took 62 question rows. Most of the work went into the table, not the thinking; that is the cost the markers kept counting as padding.

### 2.3 What the skill's evidence does and does not show

**Sizes.** Round 1: 8 practice cases, 31 MUST items, one marker. Round 2: 6 cases, 24 MUST items. Round 3: 6 cases, 24. Round 4: 12 cases, 53. Each arm was run once per round, by one agent session that answered every case in the folder (run_suite.sh line 22), so the 12 answers of an arm are one draw, not twelve. The Opus marker even saw one arm carry one case into another ("Unlike case_o5", grades_opus.md line 550).

**Markers.** From round 2, Opus 5.5 and GLM, working apart. The arms had neutral names, but their formats differ at sight (a falsifier ledger is unmistakable), and the Opus marker names "the long 'does not apply' Q-tables in Sets 1 and 2" (grades_opus.md line 262). So the markers were blind to the names, not to which answers were ledgers.

**What round 4 shows.** Within round 4, by both markers' totals, version 5 missed the fewest MUST items, stated the fewest unreported facts, earned the most extra credit and was ranked first most often. That holds, and I recounted it.

**What it does not show.**
- That version 5 *finds* more: hard-to-vary found more items in full under both markers (38 against 37; 41 against 40).
- A lead case by case on MUST items: scoring found as 1 and partly as ½, version 5 is ahead of hard-to-vary in 3 cases and behind in 3 (Opus), ahead in 3 and behind in 2 (GLM); the rest level.
- A lead that luck could not give: head-to-head rankings are 7 ahead and 3 behind (Opus, two-sided sign test p = 0.34) and 7 ahead and 4 behind (GLM, p = 0.55).
- A lead on the owner's own kind of report: on o4 (an agent's self-report), o5 and o6 (version reports), version 5 found the fewest MUST items in full under both markers (5 against hard-to-vary's 7 under Opus; 7 against 8 under GLM).
- That the fact-check pass caused anything (finding M5).
- That "both skills" invented the most results (finding S2).

**Contamination and fitting.** Round 2 carries a contamination note (results.md line 101). Rounds 3 and 4 carry none. Six round-4 cases were written by Opus 5.5, "two ... in the style of our project's version reports" (line 164), the same reports the project file was drawn from; whether the case writer had seen the skill is not reported. By the README's own rule ("Only the held-out cases, written by someone who had not seen the skill, count", line 23), rounds 1 and 2 are fitted, round 3 became development once version 5 was changed from its findings (results.md line 148), and round 4 becomes development for version 6, since all five proposals come from its marks.

**Records.** The 36 round-4 answers are not in the folder, nor the run reports, nor the fingerprints of rounds 1 and 2 ("All are in the test-runs zip", line 53). The grade files are the only record of what the answers said. Round 3's fingerprint matches `marking.md` only without its amendments section (I hashed the part before "## Amendments adopted before any answers": it matches); the amendments themselves were dated, not fingerprinted.

**Costs.** Round 4: version 5 $14.13 (244 steps, 84 checker runs, 100 edits), hard-to-vary $0.96, both skills $26.36 (lines 184 to 186). About 15 times the cost buys 0.5 (Opus) and 1.5 (GLM) of 53 weighted MUST points. Per case, version 5 cost about three times version 4 ($1.18 against $0.36) and ran the checker 7 times per case against the 3 that SKILL.md line 200 allows.

---

## 3. Findings

### SERIOUS

**S1. The results file's round-4 headline is surer than its own grade files.**
1. *What is wrong.* "Version 5 is the most effective of the three on these 12 cases, by both markers" (results.md line 191) and "The markers agree on version 5 first for reliability and breadth" (line 208) leave out what the grade files say against them.
2. *Evidence.* My ledger above, rows F1, F2, F5, F12. Hard-to-vary found more items in full under both markers (Opus 38 against 37; GLM 41 against 40). Case by case on MUST items the two are level. On o4 to o6, the cases nearest the owner's use, version 5 found the fewest (grades_opus.md lines 564 to 566; grades_glm.md lines 656 to 658). Of the six marking sessions' own overall verdicts, three name version 5 first; the others say "Set 3 is the strongest on the amended lists" (grades_opus.md line 599), "Set 1 thinnest" (grades_glm.md line 189) and "Set 2 is the strongest overall" (line 685).
3. *Effect.* The owner, deciding whether version 5 is worth 15 times the cost for the project's own reports, is told it is the most effective; on exactly those reports it found the fewest items. This is the pattern the S136 readers found in V5's read-me: a summary surer than its report.
4. *Smallest fix.* Replace lines 191 to 195 and 208 with the claim as it stands in my ledger: what version 5 led on (missed items, unreported facts, extra credit, rankings), what it did not (items found in full, case by case, o4 to o6), and that the six session verdicts split 3 to 3.
5. *Testable.* Yes: run the skill's own checker's headline rule by hand (every strength word in the summary must be carried by the claim as it stands), and have one reader who has not seen this audit compare the new paragraph with the grade files.
6. *Weight.* SERIOUS.

**S2. "Both skills ... the most invented results (one invented pilot and its result)" counts the skill's own *blocked* rows as inventions.**
1. *What is wrong.* The rows both markers counted as invented results in the both-skills arm are *blocked* rows written in the skill's own required format: who could run the test, and its pass mark.
2. *Evidence.* grades_opus.md lines 69, 184, 404 and grades_glm.md lines 80, 271, 492. The named "invented pilot" is o3's row: status *blocked*, receipt "HR runs one pilot team before Q3 2026; passes near 0.4", and its effect column says the claim is unmeasured (GLM: it "contradicts its own effect column"). ledger-format.md line 47 asks a *blocked* receipt to hold "who could run it, and its pass mark". Without these three rows the Opus count for "both" falls from 7 to 4, against hard-to-vary's 6; GLM's from 7 to 3, against 2.
3. *Effect.* Two ways, both bad. Either the markers misread the format, and the "worst" verdict and its example rest on that misreading; or the format really does read as a done test ("passes near 0.4" in the present tense), and every reader of a ledger, the owner included, can take a request for a test as a test that ran. That is hard rule 1's harm.
4. *Smallest fix.* In ledger-format.md, make the *blocked* receipt start with the words "Not run. Request:" and state the pass mark as a condition ("it would pass if ..."); in the checker, refuse a *blocked* receipt that does not contain "if". In results.md, narrow line 198 to "the most cost, and no gain in coverage" until the three rows are read in their answers.
5. *Testable.* Yes. Give three readers who have not seen the skill six *blocked* rows, three in the old wording and three in the new, and ask which describe a test that was run; the new wording passes if none is taken as run. The checker change is testable with a probe ledger.
6. *Weight.* SERIOUS.

**S3. The skill has no question and no test for a claim about where something came from: handed in, found or built.**
1. *What is wrong.* The owner's project now turns on claims of origin ("the machine built addition from its own failures", "worked out or only found?", S134 and S135), and the theory tells the three origins apart "by their histories, not their outputs" (107, line 13). The skill credits a part only by comparing outputs with rivals (hard rule 8, line 217; Q3 rung 3, designing-the-test.md line 138), and it has none of the history tests the project has used.
2. *Evidence.* Searching every module for "sham", "restore", "order" as a test of origin, or a last-picture test finds nothing of the kind (my search; the only "order of items" is Q9's stability check, forcing-questions.md line 192). The project's tests since S133 are: the knock-out with a pretend removal and a putting back (S126, S135: "A pretend removal changed nothing. Putting it back restored every answer"); the order shuffle (a found rule changes with the order of the list it was picked from, a built one does not, S134, S135); the try-everything rival (S135: the built way "gives exactly the same answers as a version that tries all 405 rules and keeps whatever fits; only how it got there differs"); the same-final-picture pairs (anything reading only the last picture scored at most 16 of 100, S135); and the copy check (a repair handed over ready-made is not built, S133). The theory's Build (D13.3) asks for a binding prepared inside the system's own history, held, used, and not a chain of copies ("Reconstruction by a learner is construction; relay is not", 107 line 405). The owner's S86, "Knowledge doesn't need to be worked out, explanation does", makes the origin part of what an explanation is.
3. *Effect.* On S135's machine the skill would mark "built" as *missing* or *failed*, because the try-everything rival ties on outputs; by the theory the tie says nothing about origin. And on a found rule that matches its outputs, the skill has no way to say "found, not built". The project's main claims would be judged on the wrong evidence.
4. *Smallest fix.* Add a fourteenth question, or an "Also catches" under Q7, "Where it came from": for any claim that something was learned, built, worked out or repaired by the system, (a) say what was handed in and where the boundary is drawn; (b) run the knock-out with a pretend removal and a putting back; (c) shuffle the order of anything it chose from; (d) compare with try-everything-and-keep-what-fits, and say that a tie on outputs leaves origin open; (e) pairs of cases that end the same but need different answers; (f) check the result is not a copy of something handed in. Put the same list in the project file's table and in its mini ledger (lines 210 to 222), and say that "explanation" there needs *built* (S86).
5. *Testable.* Yes: write two held-out cases with the same outputs, one with a found rule and one with a built one (S135's record can supply both), with marking lists first; the skill passes if its ledger tells them apart by history and does not call the found one built or the built one "unmeasured".
6. *Weight.* SERIOUS.

**S4. The semantics audit states, as the owner's theory, a test the owner took out of it.**
1. *What is wrong.* Check A2 says "The answer must not be supplied (Part V: non-circular dependence; ...). ... It may not sit in an input or in a component labelled 'law'" (semantics-audit.md lines 26 to 28). The owner decided the opposite on 28 September 2026 (S44, S45): "A written-in answer never stops something being an explanation. It only makes it a bad one, through the questions it leaves open." The theory's text since S106 has "Dependence", not "non-circular dependence", and the written-in test is gone (107 Part V; the formal core's D16.XV note: "conclusion-as-premise fails non-circular dependence' deleted").
2. *Evidence.* As quoted. File 11 (revision 1), which the audit names as its source (line 3), still carries "conclusion-as-premise fails non-circular dependence" (file 11 line 528); 107 does not.
3. *Effect.* A reviewer using the skill on the owner's project would rule a candidate out as "not an account" because an answer was handed in, which the owner has said is wrong. The useful part of A2 is still right in the current theory under other names: a handed-in transport is *declared*, and "a candidate meeting (E) whose transport is declared is no explanation" (D16.XV, owner S41); and work handed in from outside the boundary "remains an outside contribution" (107 Part X).
4. *Smallest fix.* Rewrite A2's idea: "A handed-in answer does not stop a candidate being an account; it makes it a bad one, through the questions it leaves open (owner, S45). What a handed-in answer does stop is credit: the result belongs to whoever handed it in (Part X), and a candidate whose link is handed in is no explanation (D16.XV)." Keep A2's audit steps (draw the boundary; delete the claimed block and see whether the answer changes), which match 107's Dependence.
5. *Testable.* Yes, by a reader with the theory: every sentence of A2 is traced to a line of 107 or to a dated owner decision, and none contradicts one.
6. *Weight.* SERIOUS.

### MODERATE

**M1. Worked example 1 marks *survived* a falsifier that its own receipt meets.**
1. *Wrong.* Row F5 (worked-examples.md line 24): falsifier "Case by case, memory beats fixed order in no more cases than chance would give", status *survived*, receipt "4 wins, 1 loss, 3 ties; two-sided sign test p = 0.375". A p of 0.375 is what chance gives; the falsifier fired. The same evidence is filed correctly in ledger-format.md line 24 (F3: "rests on 2 or fewer of the 8 cases", survived with 4 wins). Three other rows of example 1 state facts without quoting them: Q2 for C2, "the guarantee is stated as conditional on it" (line 32), while the frozen C2 has no condition; Q6, "all arms ran on identical lessons, goals and programs, as reported" (line 39); Q13, "all 8 cases counted" (line 51).
2. *Evidence.* As quoted; the checker passes example 1 with no warning.
3. *Effect.* Agents copy worked examples. This one teaches the two habits the skill exists to stop: a reassuring status on a test that went against the claim, and a fact filled in without a quotation (the round-2 and round-3 flaw, results.md lines 98 and 132).
4. *Fix.* F5's status to *failed*, its effect unchanged ("reported as 'on these 8 cases'"); quote the report for Q2, Q6 and Q13, or rewrite them as conditions.
5. *Testable.* Yes: a reader checks every status of the three examples against its own receipt, and every fact against a quotation.
6. *Weight.* MODERATE.

**M2. A test that was run and went against the claim can only be answered *missing*.**
1. *Wrong.* SKILL.md line 30 defines a missing condition as "A falsifier that was not sought". But a *missing* answer must cite "a `missing`, `blocked`, `failed`, `pending` or `planned` row" (ledger-format.md line 70), and a *covered* answer citing a *failed* row is refused (check_ledger.py line 42 puts `failed` in `OPEN`; the error calls it "still open").
2. *Evidence.* My ledger: Q5, Q7 and Q13 for C1, C3 and C4 had to be *missing* while citing failed rows; my probe P11 got "Q2 is 'covered' but every row it cites is still open (failed)".
3. *Effect.* The strongest finding a ledger can hold, a falsifier sought and found, is filed under the word for "nobody looked". A reader of the question table cannot tell "not tested" from "tested and failed".
4. *Fix.* Add a fourth answer, *failed*, citing a *failed* row; the checker accepts it and refuses it for any other status.
5. *Testable.* Yes, with probe ledgers and the self-test.
6. *Weight.* MODERATE.

**M3. "Well-tested" means three different things, and the checker pushes it onto claims resting only on someone else's word.**
1. *Wrong.* SKILL.md line 180: "main falsifiers were sought and survived". ledger-format.md line 15: "sought and survived or were reported". The checker (lines 43, 197 to 201) prompts a `Well-tested:` line whenever every row is survived, reported or outside the claim.
2. *Evidence.* My base probe: a claim whose only row was *reported* ("release note: 'all 412 files matched the reference'") drew "Every falsifier of C2 was sought and survived. If that is right, add a 'Well-tested: C2 ...' line". Probe P7: two claims resting only on *reported* rows, with `Well-tested: C1, C2.`, passed with 0 errors and 0 warnings.
3. *Effect.* In review mode (most of the owner's use), the checker's message invites calling a claim well tested on the claimant's word alone, against hard rule 2 and the trap "Trusting a reported test as if you saw it" (line 243).
4. *Fix.* One meaning: "every main falsifier *survived*". If all are *reported*, the line is `Well-reported:`, and the checker's message says so.
5. *Testable.* Yes, by probe ledgers.
6. *Weight.* MODERATE.

**M4. The checker lets through four things the skill's rules forbid.**
1. *Wrong.* (a) An unquoted fact passes as "your own working" if it contains "ran" or "counted" (the `OWN_WORK` pattern, check_ledger.py line 49). (b) The "never" exemptions are not enforced: forcing-questions.md line 15 says "Where an exemption says 'never', it cannot be used", but any six words pass. The self-test's model ledger (lines 303 to 304) itself answers "does not apply" to Q5 and Q11 for a claim that "guarantees", which Q5's exemption forbids (line 117: "Never when any of these is present"). (c) The headline check skips every line beginning "#" (line 289), that is, every title, though "Any summary, title or message ... quotes the claim as it stands" (SKILL.md line 197). (d) A lone apostrophe, as in "the engineers' release note", counts as a quotation for a *reported* receipt (line 48).
2. *Evidence.* Probes on scratch copies: P1, "| Q13 | all | covered | all 412 files were counted and none were skipped |" and "the team ran every file on the release build", passed with no warning; P2, a "never" claim with "| Q5, Q9, Q11 | all | does not apply | nothing here makes this question a live risk |", passed; P5, the title "# The filter guarantees no malformed record ever gets through" drew no warning while the same sentence as body text drew two; P6 passed.
3. *Effect.* The checker is meant to stop silent skips and unquoted facts; on these four paths it gives a clean pass instead, and a clean pass reads as a check that happened.
4. *Fix.* (a) Count only "worked out", "computed" or "counted by us/me" as own working; (b) when a claim line carries a word from SKILL.md line 99's list, refuse *does not apply* for Q5, Q9 and Q11, and correct the self-test sample; (c) check titles too; (d) require a pair of quotation marks.
5. *Testable.* Yes: add P1, P2, P5 and P6 to the self-test, each expected to fail.
6. *Weight.* MODERATE.

**M5. "The fact-check pass worked" gives credit that was never measured.**
1. *Wrong.* The pass is one of eleven changes in version 5 (results.md lines 149 to 159); the word limit rose from 700 to 1,000; the cases and marking lists changed. No arm ran without it.
2. *Evidence.* Ledger rows F6 and F7. Hard-to-vary, unchanged, moved under Opus from 0 violations in 6 cases (round 3) to 6 in 12 (round 4), as large a move per case as version 4 to version 5 made in the other direction. The skill's own hard rule 8: "If that rival was not run, the claimed part's contribution is unmeasured."
3. *Effect.* Version 6 may keep or drop parts on the strength of a credit no test gave; the within-round result (version 5 fewest unreported facts) is real, its cause is not known.
4. *Fix.* Narrow line 196 to "Within round 4, version 5 stated the fewest unreported facts (2 and 0, against 6 and 2); which of its changes did this is not measured."
5. *Testable.* Yes, at a cost: one extra arm, version 5 without Step 7b, on the next held-out round (about $14 at round 4's rate).
6. *Weight.* MODERATE.

**M6. The semantics audit is pinned to revision 1 (file 11), and several of its references are out of date.**
1. *Wrong.* semantics-audit.md line 3 names "revision 1, file 11". Since then: (a) "Derivation n" became "Argument n" (107 Part XVI); (b) A5 rests on file 11's "Derivation 2. Indistinguishable is identical" (line 62), which the project repaired: 107's Argument 2 is "Same counterparts, one account", and it says that candidates whose counterparts differ "are different candidates with one answer profile" (107 line 566), so arms that agree on outputs are not thereby one thing; (c) A7's "receipt is a derivation from such leaves" and "receipts for and against" (file 11 line 393) became "record leaf" and an argument that "rules out" (107 Part IX), the words the owner asked out of the theory in S23 ("supports", "derived", "established" and the like); (d) A1's "Every physically possible change left out must be left out by a stated scope" (line 18) is file 11's wording; 107 says "admitting a change is not a claim that it can be carried out" (line 159), so what a contract must state is every change the target admits, possible or not; (e) line 14, "The semantics is about explanations: what makes an organization of parts an account", predates S86, by which an account that was found is knowledge, and only one that was built is an explanation.
2. *Evidence.* As quoted, from file 11, 107 and Decisions S23, S45, S86.
3. *Effect.* A reader checking the skill against the theory finds wrong names and two claims the theory no longer makes; A5 in particular would count two arms as one because their outputs agree, where 107 counts them one only when no admitted change separates them.
4. *Fix.* Re-base the file on 107 plus the owner's decisions not yet written in (S83, S84, S86), named as the owner's decisions; rename Derivation to Argument; ground A5 in Part II's "kinds are edit-signatures" and say that same outputs are not same counterparts; replace A7's "for and against".
5. *Testable.* Yes, by a reader with 107 and the Decisions: every cited Part and Argument exists and says what the audit says.
6. *Weight.* MODERATE.

**M7. A6, "Provenance: fitted, built, declared", misreads the theory's three origins and leaves out the owner's later decisions.**
1. *Wrong.* (a) It equates "selected (fitted)" (line 75). The theory's selection (D12.1) needs a population, variation and survival, with no represented target in the history; a fit against a teacher's answers has its target in its history, and the project's present reading is "learning from a teacher's answers constructed ... so an explanation unless the owner says otherwise" (Decisions S86, citing S128), a question still before the owner. (b) "A selected (fitted) correspondence is faithful where it was tested" (line 75): by S84, being copied more counts as surviving, so a selected correspondence may have survived by advantage while failing some of its history. (c) "A constructed (built) correspondence says something definite about unseen changes, so it can be caught out" (line 78) is not in either text. (d) Ownership is given half (A2, line 28: work from outside "remains an outside contribution"); the other half is missing: "a process that runs inside the boundary is the system's own whoever wrote it" (107 line 427), and, by S83 (Reading C), origin is read inside the boundary declared for the claim, so a checker written by people can belong to the world's rules.
2. *Evidence.* As quoted.
3. *Effect.* A reviewer would call a model trained on labels "selected", call a found rule with training errors "not selected", and discount every process its makers wrote, whatever the declared boundary.
4. *Fix.* Use the owner's three words with their definitions: *handed in*, *found* (kept by trial from a list against answers it was given; survival may be graded, S84), *built*; say that a fit to a teacher's answers is an open question for the owner; require the boundary to be declared with the claim, before origins are tagged (S83); give both halves of ownership; drop (c) or mark it as the audit's own gloss.
5. *Testable.* Yes, by a reader with D12.1 to D12.3, D13.3 and the Decisions.
6. *Weight.* MODERATE.

**M8. One thing, many words: the skill does not use the owner's words for origins.**
1. *Wrong.* The same idea appears as supplied, handed in, given by hand, declared (Q2, lines 42 to 61; A2; A6); as fitted, learned, tuned, selected (Q8; A6); as built, constructed (A6). The owner's preference is one word per thing, and since S133 the project says *handed in*, *found*, *built*.
2. *Evidence.* forcing-questions.md line 45: "What did the setup hand in by hand"; line 163: "fitted, learned, tuned or selected"; semantics-audit.md line 72 heading.
3. *Effect.* The owner reads three or four words for one thing and cannot tell whether they differ; agents may treat "learned" and "selected" as different checks.
4. *Fix.* One word each, defined once in SKILL.md: *handed in*, *found*, *built*; keep "fitted" only inside Q8 as an example of found.
5. *Testable.* Yes, by a word count over the files after the change.
6. *Weight.* MODERATE.

**M9. The project file misses three things the S136 readers found in V5.**
1. *Wrong.* (a) A system that recognises a failure and then answers "unknown" for good (V5 "latches and stops") would pass the project file's falsifier "a seen departure not flagged as 'unknown'" (line 216), since it does flag it; nothing asks whether it ever recovers or repairs. (b) A memory that keeps no past observations cannot have a repair checked against what it saw; no question asks what the design throws away. (c) V5 "gave a certified 'yes' at the 18th observation, after the world had already left what it was tracking at the 17th"; the theory's repair keeps protected aims "on every occasion it covers ... not only at ξ'" (107 line 441), but nothing in the project file asks to check certificates against the moment the world changed.
2. *Evidence.* our-thinking-machine-project.md lines 172 to 186 and 213 to 222; plain file 136.
3. *Effect.* The next V5-style report would be read as careful ("refuses when unsure") while its inability to repair, the owner's main concern since S90, goes unasked.
4. *Fix.* Three rows in the project table: under Q12, "after it says 'unknown', does it ever answer again, and from what?"; under Q12 or Q13, "what does the memory discard that a repair would need?"; under Q1 or Q5, "was any certificate issued after the moment the world changed?".
5. *Testable.* Yes: S136's V5 read-me and report as a held-out case for the project file, with a marking list holding these three items written first.
6. *Weight.* MODERATE.

**M10. "Does not apply" has two rules that cannot both hold.**
1. *Wrong.* forcing-questions.md line 15: "'Does not apply' must use the question's own exemption". ledger-format.md line 66 lets one row "list several questions that share one reason". Questions have different exemptions; one shared reason cannot be each one's own.
2. *Evidence.* Probe P2 above: Q5, Q9 and Q11 waved away together on a "never" claim, each against its own "never" rule, passed.
3. *Effect.* The shared row, added to cut padding, is the easiest route to the skip the skill exists to stop ("A skipped question is how missing conditions survive", SKILL.md line 129). Proposal 4 for version 6 would make it the default.
4. *Fix.* Allow a shared row only when its reason names each question's exemption, and never for a question whose "never" condition the claim meets (with M4 (b)).
5. *Testable.* Yes, by probe ledgers.
6. *Weight.* MODERATE.

### MINOR

- **N1. Rule lists drift between copies.** forcing-questions.md line 8 says "Three rules make the answers useful" and lists seven; its "One condition per row" (line 12) lacks version 5's "Rows that would be tested the same way are one row: merge them" (SKILL.md line 133). *Covered* is defined three ways (SKILL.md line 125; ledger-format.md line 69, which adds *outside the claim*; forcing-questions.md line 4). ledger-format.md line 29 says "every claim needs at least one row naming it alone", but line 110 and the checker make it only a warning. *Fix:* keep the answer rules in one place and point to it. *Test:* a diff of the rule texts. MINOR.
- **N2. The flowchart leaves out Step 7b**, the fact-check pass (SKILL.md lines 60 to 75 go from "Steps 6-7" to "Step 8"), though line 77 asks the tables and graph to change together. *Fix:* add the step. MINOR.
- **N3. A status word that is not one.** agent-reports-and-self-checks.md line 34: "Mark anything not run as *not run*"; the checker refuses it. *Fix:* "*missing* or *blocked*". MINOR.
- **N4. The short form is not checked against the table.** Probe P3: "missing: none" while a row is *missing* passed; P4: a *reported* row named as missing passed. *Fix:* the checker compares the two. MINOR (short form is for low-stakes claims).
- **N5. The headline words are a short list, matched as parts of words.** The checker's list (line 47) has 10 of SKILL.md line 99's strength words, and "exact" in a report passes when "exactly" is in the claim as it stands (probe P10). *Fix:* one shared list, whole words. MINOR.
- **N6. Only the last falsifier table is read.** Probe P9: an invalid first table was ignored. *Fix:* refuse two. MINOR.
- **N7. Stale heading.** results.md line 210, "Proposed for version 5 (not applied, not tested)", though line 148 says proposals 1 and 2 were applied. *Fix:* "(as written before version 5; 1 and 2 since applied)". MINOR.
- **N8. A8 feeds the wrong questions.** "What a failed test refutes" feeds "Q4, Q10" (semantics-audit.md line 105); it belongs with Q11 (has the instrument ever caught a planted fault) and designing-the-test.md section 8. MINOR.
- **N9. Plain notes at the top.** The case files, marking files, grade files and `key.txt` have no note saying what they are, against the owner's preference. MINOR.

---

## 4. The "Proposed for version 6" list

All five come from round 4's marks, so round 4 becomes a development set for version 6 by the README's own rule (line 23). Version 6 then needs a fresh held-out round, written by people who have not seen versions 5 or 6, with each arm run in a fresh session per case, and answers rewritten into one layout before marking (ledger rows F19 and F20).

1. **Credit a strong design out loud.** *Supported:* both markers saw it on g3 (Opus: M1 and M4 missed, "it adds doubts instead", grades_opus.md line 267; GLM ranked version 5 last on g3). *Risk:* crediting a design word the source uses without describing it; hard-to-vary's o1 error was exactly that ("randomised-sibling, blinded-genotype", grades_opus.md line 327). *Change:* name each design feature the source describes, quoted, and what it rules out from the reassuring-words table, before any caveat; never credit one the source does not describe. *Test:* the well-tested cases (g3, o5, n3) plus a new pair, one with a described strong design and one with the design word only; MUST credit the first, MUST-NOT credit the second.
2. **Use the named test, not a cousin.** *Weakly supported:* Opus g1 ("novelty instead of seasonality") and GLM o6 ("gesture at the right area without the named test"). *Risk:* "the named test" is the marking list's wording, so this teaches the skill to the markers; the trap "Generic checklists" (SKILL.md line 238) already asks for this case's particular test. *Test:* only on fresh cases; it passes if *partly* marks turn into *found* without more padding.
3. **Self-written records in agent reports.** *Supported as a miss* (o4, both markers), *not as a missing rule*: the rule is already there, three times (agent-reports-and-self-checks.md line 15, "the log is a claim"; hard rule 2; Q11, "who wrote the record"). Adding a fourth copy risks more length and no change. *Change:* find out why it was not applied (the answers and transcripts are in the test-runs zip); if the situation file was not opened, fix the routing. *Test:* new agent-report cases where the only log is the agent's own.
4. **Group the "does not apply" rows by default.** *Not supported as written.* The padding counts that motivate it are partly one marker's way of counting (results.md line 181), and grouping already lets a "never" claim skip Q5, Q9 and Q11 (finding M10, probe P2). *Change instead:* collapse into one line only the questions whose exemptions the case clearly meets, and refuse it for Q3, Q5, Q9 and Q11 when the claim carries their "never" words. *Test:* probe ledgers, then padding counts and MUST-NOT on the next round.
5. **Work in one pass; remove the "no falsifier naming it alone" warning.** *Partly supported:* version 5 ran the checker 84 times for 12 cases, more than twice the three per ledger SKILL.md line 200 allows. But the warning "chased 112 times" was in the both-skills arm (results.md line 186), not version 5's. *Risk:* "one pass" must keep Step 7b, which is a second reading; removing the warning leaves ledger-format.md line 29's rule unchecked, so drop or keep the rule with it. *Test:* rerun version 5 and the changed version on the same fresh cases; compare cost, checker runs, and MUST-NOT violations of the X2 kind.

**Missing from the list:** findings S1 to S4 and M1 to M3. Of these, S2 (the *blocked* wording) and M1 (worked example 1) are the cheapest and touch what agents copy most.

---

## 5. Findings I dropped on re-reading, because the skill covers them

- **"A read-me surer than its report" (S136) as a rule for reviews.** Covered: Step 1, "If the body narrows it, freeze both as separate claims" (SKILL.md line 97), with "The headline follows the ledger" (line 197). Finding S1 is about the skill's own results file breaking that rule, not about a missing rule.
- **Reviewers not named, and earlier runs reused (S136).** Covered by Q11 ("Who wrote the record?", forcing-questions.md line 223) and Q6's "evidence from a different artefact" (line 128).
- **The naming trap (S118, S133, S135).** Covered: Q2 asks for "candidate answers" handed in (line 45), and Step 6's own example narrows a claim to "inside the supplied model list" (SKILL.md line 176). What is missing is only the origin test, kept in S3.
- **A knock-out.** Covered (SKILL.md line 133; Q6, forcing-questions.md line 132). A pretend removal is close to the null control (designing-the-test.md line 159). Only the putting back, and the pairing of all three, are missing; kept inside S3.
- **Order of items as a check.** Q9 has it as a stability check (line 192); kept in S3 only as a test of origin.
- **Drawing the boundary.** A2 asks for it ("Draw the boundary", semantics-audit.md line 30); M7 keeps only the parts that are missing: declaring it with the claim, and the other half of ownership.
- **Self-written logs (version 6 proposal 3).** Covered by three existing rules; see section 4.
