# A4 - The test regime as a method

Reviewer A4. Written under the hard-to-vary skill (SKILL.md, with `building.md`, `testing-against-cases.md`, `reporting.md`). Nothing in the repository was changed; nothing was run except read-only `grep`, `cat` and `find` over files already in the repository.

How I know each thing is tagged: **read** (a line of a file, named), **seen** (an output I looked at, named), **worked out** (my own reasoning from tagged things), **assumed**.

Read whole: the four plans (`Language/tests/L65`, `L66 Test plan`, `L71`, `L72`), the two handoffs (`L66 Handoff ... second version`, `L72 Handoff ...`), `L66 Reader brief`, the four results files, `Language/authority/L64`, `Language/records/Language - project story.md` (L60 to L75), Decisions, Lessons, Status. Also **seen**: `rigs/rig 1 - arguments/patched/run_check.py`, `tools/consequences.py`, `tools/smoke_expected_report_A.txt`, the eighteen rig-1 reports in `results/L69 Return .../evidence/rig1/`, `results/L69 .../evidence/corrections_OpenAI_Codex.json`, `results/L74 .../audit_protocol.md`.

---

## 1. The question, frozen

What is being judged: **the test regime** of the Language project as a method - plan frozen before any run, numbered expectations with a "would count against" column, a sealed key, a worker who translates and runs and returns a zip, a reader who sees reports only, an orchestrator who checks hashes, reruns and marks.

Over what range: the four runs L65, L66, L71, L72 and the record entries L60 to L75. Not the language (38), not the theory (11), not the checker's rules, except where a run's result turns on them.

What is asked: does the regime do the jobs it is meant to do, and is it built so that a run could come out against the thing being tested? Kind of question: **does it achieve its purpose?**

---

## 2. (a) The jobs the regime is meant to do

From the plans, the handoffs, L64 section 8, and the owner's Decisions. Tagged **given** (the owner named it), **fixed** (the owner made it a requirement, not up for test), **added** (Claude's).

| # | Job | Tag | Where (read) |
|---|---|---|---|
| J1 | Tell the four sources of error apart: scope, translator, checker, read-back | given | Decisions L4 ("Four sources of potential error..."), carried into L64 section 6 |
| J2 | At each step say when error is acceptable, what is given up, what is got, what success is | given | Decisions L4; L64 line 45 |
| J3 | Make deductions, many, and test consequences | given | Decisions L4; L64 line 44; the object of L65 and L71 |
| J4 | Run the test blind, on a deliberately difficult but consistent corpus and on a contested science | given | Decisions L8 |
| J5 | Split the work: one agent runs, one reads and audits, both fresh every time | given from L9; added before that | Decisions L9; first used at L66 plan lines 10-12, where it was Claude's proposal |
| J6 | The orchestrator stays, checks every return (manifest, identity, runtime, reruns) and decides what enters the repository | given (the role) / added (the procedure) | Decisions L3; procedure at L72 plan lines 26-29 |
| J7 | Test the read-back on a reader who is not Claude | given (the error source) / added (the form) | Decisions L4; `L66 Reader brief` lines 3-10 |
| J8 | Freeze the plan before any run and never edit it | added | no owner decision; the plans' own first lines (e.g. L65 line 3, L71 line 3); the skill's rule |
| J9 | Write a "would count against" column for every expectation | added | L66 plan line 23; L71 line 8; L72 line 9; from the skill (`testing-against-cases.md` section 1) |
| J10 | Say which layer a failure refutes, without reading it off the run | added, resting on the theory | L64 line 147 |
| J11 | Be able to show the scope wrong: the five conditions | added (accepted without strikes) | L64 lines 169-175; acceptance at Decisions L7 |
| J12 | Append-only record, numbered files never overwritten, nothing changes without the owner's word | fixed | Decisions L1, L3; L75 line 114 ("every one waits on the owner's word") |

Two notes on the tags. J11 is Claude's wording that the owner accepted without strikes; acceptance is not authorship, and Lesson L3 (Lessons line 30) is the case where an owner's aside became a "given" job that said the opposite of what the owner meant. I keep J11 **added**. J8 and J9, the two parts most people would call "the regime", are nobody's requirement: they are Claude's, taken from the skill. A part held only by an added job is held *if* that job is real (skill, Step 2).

---

## 3. The regime in parts, with marks

One mark and one provenance each. Marks are never added up.

| # | Part (the regime's own words) | Mark | What holds it, or what would | Provenance |
|---|---|---|---|---|
| P1 | The plan is frozen before any run and not edited afterwards | held, jointly with P8 | J8: the misses stay on the record as misses - L71 results line 30 marks E4 "not met, on the low side"; L66 results line 34 keeps an ill-formed prediction rather than tidying it | built |
| P2 | Each expectation carries a "would count against" cell | held if | Held only if the cell excludes the prediction on **both** sides. In three rows it did not, and the miss fell outside it: L66 E1 (expect 2 of 6, against "5 or 6... or 0", found 1), L66 E4 (expect 3-5, against "fewer than 2", found 2), L71 E4 (expect 40-120, against "over 150", found 28). In those rows a plan with no cell would have given the same marks. Settled by: a plan whose every cell brackets the prediction | fitted |
| P3 | A "what would count as failure", sorted by layer | idle | Present at L65 lines 28-31 and L66 lines 34-38; absent from L71 and L72 with no change to any mark. When it did fire (L66's "of the language: ... E6 with Lucretius over a third") the layer it named was not charged; the failure was moved to the instrument (L66 results line 38) | built |
| P4 | The sealed key, opened after both returns | held (for the worker) | J4: the key was not in the worker's return (record line 89). It holds nothing for the predictor: the same hand sealed the key and wrote the predictions (L66 plan line 13), and the prediction contradicted the key (Lesson L9) | built |
| P5 | A worker agent that translates, runs and returns one zip | held | The removal test was run by accident at L68: an agent with repository access wrote a record entry and translated nothing (record lines 83-85) | built |
| P6 | The brief's first paragraph forbidding the repository | held | Same pair: L68 without it, L69 with it (`L66 Handoff ... second version` line 3) | built (forced by a failure) |
| P7 | A reader agent that sees printed reports only | held | J7: it produced the only criterion that bit against the read-back job (L66 results line 39) and the finding the orchestrator calls the most useful (finding D, line 49) | built |
| P8 | Append-only record, numbered files, a Lessons file | held | It is what makes the repeated mistake countable at all: Lessons lines 25, 33, 36 | built |
| P9 | The return check: manifest hashes, source identity, runtime, reruns | unknown | No return has ever failed one (8 of 8 at L62; 13 of 18 at L69, record line 89; 16 of 16 at L72). Settled by: one salted return - a file altered after the manifest is written - to see whether the check fires | built |
| P10 | "A failed test refutes the bundle", the layer is not read off the run | borrowed | Rests on file 10/11 K3, named at L64 line 147; K3's rival is never set beside it | asserted |
| P11 | "...and which layer to change is a fresh choice" | loose | A near neighbour does the same job and more: each cell names in advance the layer its firing charges, plus a second run that separates that layer from its neighbour. As written it let a language-failing cell be re-read as an instrument fault after the fact (L66 results line 38) | built |
| P12 | Gauges with thresholds (bin per sentence, cannot-tell, unshaped verbs) | held if | Held only if the gauge counts what the scope job needs and the threshold exists. It counts fragments lost, not sentences unchecked (L66 results line 38), and no threshold is set (L64 lines 134, 179). Settled by: the hostile text L64 line 171 says is owed and has never been run | built |
| P13 | The sameness program, with a hand reading of what it leaves | two routes | Program and hand. The program did 4 of 21 at L72 (results line 36) and scored a line against its own negation 0.50 (line 43); the hand did 21 of 21 - but the hand is one of the two translators being compared (results line 69), so the second route is not independent | fitted (its near score was tuned on cases with no negation, Lesson L8) |
| P14 | The worker both translates and runs | loose | Replaceable by: hand-written probe ledgers run beside the worker's, so the checker's arm is never empty. At L66 three of six plants never became lines and "the checker had nothing to check" (results line 76), so the checker's arm was empty and nobody could tell that from the marks | built |
| P15 | One agent is corpus maker, predictor, marker and layer-chooser | loose | Replaceable by: the predictor sees class counts, not the map; a second agent checks premises before freezing. All three memory lessons run through this part (Lessons 51, L6, L9) | fitted (this is how the project has always worked) |
| P16 | Nothing changes without the owner's word | fixed | The owner put it outside the test (Decisions L1, L3). Not tested here | - |

---

## 4. (b) What each run actually tested, against what it claimed

### L65, consequences on the tomato ledger
Claimed (plan line 7): find out whether the pull between *many consequences* and *exact read-back* is real.
Actually tested (**worked out** from plan and results): how many facts a new program printed on one 13-line ledger that the orchestrator had built, patched the checker on, and run many times before - written by the same hand, in the same session, with the program, the rig, the ledger and the expectations all on one side. Only one arm of the pull was measured. The read-back arm was not: the plan's own "Not tested" says "Reading by anyone but Claude" (line 36), and E5 is a prediction about a sentence that could be built, marked "Right; no rule change needed" (results line 13) - an expectation about an artefact nobody built. So the conclusion "the pull is not real at this size" (results line 21) rests on a count plus an assertion about usability.
Worth keeping: E3's bound was wrong and was recorded wrong (results line 11), and the program's first run was caught by reading its output against the ledger (Lesson L4). That is the regime working.

### L66, the blind corpus
Claimed (plan lines 16-20): plants, consistency, the dispute, scope, read-back.
Actually tested:
- **Plants.** What one translator does with crude program-made alterations. Three of the four unfound plants never became lines (results line 76). So the run measured the translator's refusal to repair, which the results say themselves: "The blind test as designed measures the translator more than the checker" (line 59). The plan foresaw the risk and wrote the trap against itself (plan line 51) but built no arm that could isolate the checker.
- **Consistency (E2, E3).** Marked "met" on silence. Silence here is not a result: Lesson L2 (Lessons line 29) already says the driver's NO FAULT FOUND cannot tell a question answered from a question it could not ask, and the record's own L69 entry says three passages had no said line at all (record line 89). An expectation that a passage raises no contradiction is unmarkable on a ledger with nothing to contradict, and the plan had no precondition requiring said lines.
- **The dispute (E4).** The two modern passages were written by the hand that predicted what they would share. "3 to 5 facts both say" is a prediction about the predictor's own prose. The result (2 shared facts, in unrelated wording, results line 36) is a fact about one writer's paraphrasing.
- **Scope (E6).** Tested a gauge against a threshold that L64 itself leaves to the owner (line 179). An expectation whose pass line is not fixed before the run can absorb any result.
- **Read-back (E7).** The one arm genuinely tested, by an agent with nothing but the reports. It bit.

### L71, consequences on C and H
Claimed (title): a fault-free ledger and the longest.
Actually tested: two faulty ledgers. The premise on C was wrong (results line 6). Half the plan tested nothing it claimed. E1's wording "none surprises" was marked "not a fair test of anything" (results line 27) - honestly. What it did test was size growth on H, and it produced a finding nobody asked for (stated facts hide derived ones, results line 37).

### L72, two translators
Claimed (plan line 6): how much of a ledger is the translator rather than the text.
Actually tested: that, plus - unplanned - the consequence of 39's attribution rule meeting patch 12. But the measure of translator spread is confounded three ways: one of the two "translators" is the orchestrator who built and patched the rig and had run these texts before; its ledgers were not made under the blind conditions the other worked under, and one of them silently dropped a sentence (results line 53); and the instrument that was supposed to make the comparison failed, so the comparison was made by hand by one of the two parties compared (results lines 36, 69). The plan's "against" cells here were the tightest of the four and two of them fired (E3, E8, results lines 38, 43). That is the best-built of the four plans.

### The three expectations that could not be marked
- **L66 E7, no contradictions to trace.** Plan-writing in form: the criterion was conditioned on an event the run need not produce, and its occurrence depended on another expectation (E2's predicted false alarm) coming true. Regime at root: nothing in the regime requires an expectation to be markable under the outcomes the run can produce, nothing requires a **positive control** (the corpus maker could have sealed in one passage known to raise a contradiction), and nothing says what the regime owes when a row is unmarkable. **Regime.**
- **L71's premise on C.** **Regime.** The rule is "freeze before the run"; there is no step between drafting and freezing at which a premise is checked against the artefact. Freezing without verification converts an unchecked memory into an immutable premise, which is worse than not freezing. Lesson L6 proposes the right check but addresses it to the same agent, at the same moment, as the mistake.
- **L66 E2 naming a planted passage.** Plan-writing by the letter - the writer had sealed the key an hour earlier (record L66 entry). **Regime** by the pattern: the regime lets one agent seal the key and write predictions that name instances, when predictions over **classes** ("on planted passages X; on unplanted Y") would have been markable and could not have named the wrong passage.

### A fourth case, not yet on the record
Forced finding 3 (L75; L66 results line 39; Status line 59) says the driver prints the sentence number only in what-if and plan headings, and that the fix is "one line in the driver: print the sentence beside every line a finding names". **Seen**, in the code and in the project's own files:
- `rigs/rig 1 - arguments/patched/run_check.py` line 43-48, `describe_lines`, prints `  - line X [mark, sentence N]: text`, and is called from eleven branches, including CONTRADICTION (line 86), FOLLOWS (106), CIRCLE (120), PLAN both ways (196, 212), DEPARTURE (229), TWO USUALLY (257), ADDED LINES (272), WHAT-IF CANNOT BE RUN (293), DENY A CAUSE (307), SUPPOSITION (324).
- The project's own smoke file `Language/tools/smoke_expected_report_A.txt`, made at L72 (record L72), prints sentence numbers at its lines 5-8, 12-14 and 21-24, inside a CONTRADICTION, a FOLLOWS and a KIND MISTAKE.
- JUMP (line 126) and NO CONNECTION (line 157) print no sentence, and neither do the head lines of BECAUSE-claim (99), SINCE-claim (145) or PLAN (193).
- In the eighteen L66 reports there is not one `  - line ...` entry (**seen**: `grep -c "  - line" *.report.txt` over `L69 .../evidence/rig1/` returns zero everywhere), because no branch that calls `describe_lines` ever fired in that run.
- The sentence anchors the reader *did* use in what-ifs came from the ledger's `whose` field, which the translator wrote: `WHAT-IF [OpenAI Codex, L66, sentence 2 line f]` in `P13_OpenAI_Codex.report.txt` line 5. The driver prints `w.get("whose")` verbatim (run_check.py line 292). P16's plan anchor is in the gauge's bin list, also the translator's text.

So: the finding generalises from the reports that happened to occur to a claim about the driver, and it is wrong in both directions - the driver does print sentences elsewhere, and where the reader succeeded it was reading the translator's label, not the driver. The proposed fix would not repair the observed failure, because JUMP and NO CONNECTION name no supporting lines to hang a sentence on; the sentence has to go in the **head**, which is a different change. This is the same error as Lessons 51, L6 and L9, made a fourth time, inside one of the four findings that are about to force a change.

---

## 5. (c) Is the layer choice constrained, and can the regime ever refute the language?

**What constrains it now.** Three things, read:
1. L64 section 6's per-layer lists of "error that is not acceptable" (lines 142-145). These do real work: they say in advance what would be a failure *of that layer*.
2. The cost argument at L64 line 147: a wrong layer choice shows at once through the other jobs of the layer changed, and F09 is left open for exactly that reason.
3. The plans' own failure sections (P3), where they exist.
And, in practice, a fourth: the owner decides (L75 line 114). That is authority, not evidence - it means no run by itself refutes anything; runs produce a docket.

**What is not constrained.** Nothing requires a cell to name its layer before the run; nothing stops an instrument being challenged after a cell fires. L66 E6 fired against the language by the plan's own failure list (plan line 35: "Of the language: E2 or E3 against it, or E6 with Lucretius over a third"), and was marked "**against, on its face** ... The instrument L64 proposed does not measure what E6 meant" (results line 38). Here the rescue is probably right - the worker and the reader said the same thing independently - but the regime as written could not have stopped a wrong one. Per the skill, a patch that narrows the claim after failure needs its own gauge; this one has none.

**Can it refute the language?** Yes, but by one route only, and the route is not in any plan's cells by accident. The shape that forces it: **both translators, each quoting a rule of 38/39, produce ledgers on which the checker is silent about, or disagrees about, a claim the text makes.** Translator variance is excluded because both cite the rule; rig variance is excluded by the rerun; so the rule is what is left. That is exactly forced finding 1, and it is why the orchestrator could write "a finding about the language, not about either translator" (L72 results line 48). Of the four forced findings, that is the only one that lands on the language; 2 and 3 land on the driver and 4 on a tool.

**The flip, named.** The one cell in the four plans whose firing would have had to be read as "the language is wrong" is **L72 E1's against cell**: "Any text with no matched line: the two translators read it as different texts" (plan line 11). It is the instance of L64 section 8's fifth condition - "Two ledgers of one text, by translators who have read no ledger, that differ in said-content on a text inside section 3" (line 174) - which is the record's own written statement of what would show the scope wrong. It did not fire: by hand, 21 of 21 lines matched. One clause has to be added to make the firing binding, though: the differences must each be licensed by a rule of 38/39 that the ledgers cite, or else L64's own translator row (line 143) charges the difference to the model instead.

A second, weaker one did exist and could have fired: L66 E2's "3 or more: the language misreads lyrical argument as contradiction" (plan line 26). It could not fire on the corpus as translated, because passages with no said lines cannot contradict.

**Worked out:** three of the four forced findings (1, 2, 4) came from agents going past their briefs - Astra Ultra reading `consequences.py`, Astra Pro auditing the reports beyond its four questions - and not from any expectation. The regime has no part whose job is to produce those, and no gauge that would show if they stopped coming.

---

## 6. (d) Independence

### L72: the examples, and the scope file
**Read** (L72 results line 57): "Astra Ultra's line form copies the bundle's examples (the L62 return, by the same harness), so the two 'independent' translators are not independent of the examples." **Seen** in the same file, line 26: 25 of Astra Ultra's 50 lines are Thing lines taken from those examples.

What it undercuts, and what it does not:
- E2, E3 and E8 turn on line form and line count. E3 landed in the "against" column purely because of the Thing lines (results line 38). Those three marks carry nothing about the translator layer; they measure a convention 38 leaves open (finding 5, line 52).
- The decisive finding is *not* undercut, and is strengthened by the exposure. The exposure would push the two translators together; the finding came from them coming apart, over a rule one of them quoted. Further: L64 names T10-D beside "jump" (line 90), so the worker had been told a jump was once found there - and still produced no jump, because 39 sent the claim into a told world. A disclosed exposure that would have biased towards agreement cannot explain disagreement.
- The exposure the plan did **not** name: the same harness had, two days earlier, a bundle containing `results 37` - which states, per text, what the checker found on all eight of these texts (**read**: `37 Test results ...` lines 13-20) - plus "every earlier ledger" and rig 1's raw log (`L66 Handoff ... second version` lines 17, 21). L72's bundle carefully removed all of that (L72 handoff line 21). So L72's blindness rests on the premise that a fresh session of Astra Ultra carries nothing from the L66 session. That premise is **assumed**, from Decisions L9 ("Both are always fresh from now on"), and has never been checked.
- The clean design: examples of the ledger form built from a text outside every corpus, by neither harness, with the Thing-line convention decided in 38 or 39 rather than left to examples (which is finding 5's own proposal); and the scope file supplied with section 3 and section 4's "Seen on" column redacted and the redaction hashed - those columns are evidence citations, not contract terms, so removing them does not remove the contract the translation is made under.

### L66: the corpus maker wrote the plan and two of the passages
**Read** (L66 plan line 13): "the corpus maker also wrote the two modern passages and this plan. The predictions below were written knowing the plants."
- For E4 (the dispute) it undercuts the result completely. The prediction, the object and the marking are one hand. "Same facts, different point" cannot be told apart from "one writer wrote two passages that share some facts". The source check at abstract level (results line 56) tells us the passages are fair statements of two positions; it does not make the prediction independent of the text.
- For E1 and E2 (the plants) it undercuts differently: knowing the plants did not even help, since E2 named a planted passage as its unplanted false alarm. Knowledge without a check is not an advantage; it is a third way to be wrong.
- What it does *not* undercut: E7, the read-back. The reader had none of it.
- The clean design: passages that nobody in the loop wrote (the published prose the sources name is the natural corpus for a dispute); a predictor who is given the **counts by class** but not the map, so predictions must be written as rules over classes and become markable when the key opens; the key sealed by, and checked against the plan by, an agent that is not the predictor.

### Two smaller ones, not in the question but in the files
- **The reader fixed its criteria after four passages** (`audit_protocol.md` line 5), and disclosed it: "P01-P04 were read before fixing the following expectations." Honest, and the right instinct; but it means the read-back criteria were tuned on a fifth of the material they were then applied to.
- **The marking used ledgers the worker revised after seeing the run.** `corrections_OpenAI_Codex.json` gives five corrections (P01, P03, P07, P10, P14), one of them reasoned as "the original tested positive propositions despite negative ledger wording"; the draft's header says the per-passage table uses correction 1 for those five. Those five are exactly the passages carrying E4, E5 and Astra Pro's finding E. The handoff permits it (line 46: "a correction is a new file beside the old") and the originals are kept, so this is repairable by marking the frozen originals as a first arm and the corrections as a labelled second. As it stands, the marks are on a revised object.

---

## 7. (e) The same mistake three times - is the proposed fix enough?

The three (**read**, Lessons lines 25, 33, 36):
- 51: plan 45's predictions written from the audit report's descriptions, not from the case texts. Fix: "a forcing case's prediction quotes the text it will be run on".
- L6: plan L71's premise on C written from memory of a phrase. Fix: "before a plan names an earlier result, print that result again with one command and quote the report's first line in the plan".
- L9: plan L66's E2 written from a picture of the corpus, not the key. Fix: "a prediction that names a passage is checked against the key's table before the plan is frozen, by reading the table, not by memory (the same rule as Lessons 51 and L6, now three times)".

The fix is insufficient, and the record itself half-says so. Each fix is a rule addressed to the same agent, at the same moment, in the same act in which the mistake is made; the rule's own text notes it is the third time. L9 was made *after* 51 and L6 were written down. And section 4 above shows a fourth instance, about the driver, in a finding that is now in the forced list - so the count is four, not three, and the rule has not held once.

It is a method defect, and the structural fix is small. Two changes:

1. **A premise block, in a form a machine can check.** Every plan carries a numbered Premises section. Each premise is a **quotation** from a named artefact with its path and hash: "C's recorded report reads `CONTRADICTION about got_inside(fox)` - `rigs/rig 1 - arguments/checker_report_C.txt`, sha ...". A premise that cannot be written as a quotation is not a premise; it is a guess, and is written into the expectations as one. This makes most of the error class mechanically catchable - a script can verify that each quoted string is in the named file at the named hash - and it removes memory from the loop rather than exhorting it.
2. **A second agent freezes the plan.** Astra Pro already exists in the split (Decisions L9), already cannot execute, and already does this work well but too late. Before freezing, it receives the draft plan, the artefacts and the key, and returns a PREMISE CHECK: for each premise, the quotation found or not found; for each expectation, whether it names an instance the key contradicts, whether its criterion can be marked under outcomes the run can produce, and whether its "against" cell excludes the prediction on both sides. The plan is frozen only after that, and the freeze records both hashes.

The cost is one extra short pass by an agent already in the split. The pull it creates is real and should be named: freezing early against tidying, versus checking first against freezing an error. The line goes after the premise check, because a frozen wrong premise is not merely useless - it silently converts half a test into nothing, which is what L71 did.

---

## 8. Whole-explanation checks

- **Flip.** Could the regime have reported "the language works" whatever the world was like? On the L66 arm, yes: on ledgers with no said lines, NO FAULT FOUND everywhere marks E2 and E3 "met" (results lines 34-35), and the same reports would come from a checker that asked nothing - which the record already knows is possible (Lesson L2). Silence is being read as a pass in the one place a pass matters most. Gauge that would stop it: Lesson L2's own fix (the report lists the kinds of claim the ledger had none of), plus a said-line precondition on any silence expectation. Neither is built.
- **Reverse (poke the cause, then the effect).** The regime has never poked the language. In all four runs, 38 and 39 are held fixed and the texts and translators vary. Poking the effect (rerunning ledgers) is done every time and is thorough. So the one poke that would tell a language fault from a rig fault - change 38 or 39 and see whether the reports move as the change predicts - has never been run. L64 line 143 names it (the variation test) and calls it what success looks like for the translator layer; no plan runs it.
- **The answer in the starting points.** Several expectations are predictions by the person who built the rig about the rig's known behaviour (L65 E3 and E5; L71 E5). Their being "met" holds nothing in place.
- **Add a job.** The job that would rule out most rivals is J1, telling the four layers apart. No run has ever isolated one layer; L72 came closest, by accident.
- **Look inside.** The regime checks outputs (reruns, hashes) and never workings. The two findings that came from reading code (Astra Ultra on `consequences.py`; my own reading of `run_check.py` in section 4) show how much is sitting there. I confirmed the `consequences.py` fault myself: the driver keeps world membership in a module-level `WORLD_REMOVED` (run_check.py lines 11, 16, 69, 313, 327), and `consequences.py` calls `rig.run_query` (line 41) without ever setting it (**seen**).
- **Pairs that pull.** (i) Freeze early against check first - section 7; the line goes after the check. (ii) Blindness against cheapness: the only agent with the texts and the rig is the one that must not predict; the split in section 9 draws the line at prediction, not at corpus-making. (iii) One worker translating *and* running against isolating the checker: at L66 the translator absorbed four of six plants and the checker's arm was empty; the line goes at adding a hand-written probe arm, not at splitting the worker.
- **Check the patches.** The one rescue after a failure is E6's instrument challenge (section 5). It was supported independently, it is on the record with its reason, and the instrument it challenges is a catch-all's gauge - the very thing the skill says must be able to show the catch-all swallowing a job. Until the gauge counts unchecked sentences and the owner sets the line, the bin is a catch-all whose gauge cannot bite.
- **The change list, and what it leaves out.** The regime varies texts, translators, ledgers and readers. It does not vary: 38, 39, the rig's patches, the s(CASP) engine (L64 line 163 names it borrowed with its rival never set beside it), or the harness of the agents. Rig 2 is in none of the four plans ("Not tested" in L65, L71, L72).
- **Rivals.** The nearest rival regime - hand-written forcing cases run against the rig, with no translator in the loop - already exists in this project (the K and N cases of plan 45). It isolates the checker, which the blind-corpus design cannot. The two are not rivals but arms, and the regime currently runs only one of them at a time.

---

## 9. (f) The next regime, as small as will do the job

For a new version of the bundle answering the four forced findings: (1) test BECAUSE and SINCE inside a told world; (2) say when a what-if leans on an unestablished BECAUSE; (3) put the sentence where a reader can reach it; (4) set the world list in `consequences.py`.

### Shape: two arms, because they charge different layers
- **Arm A - no translator.** The ledgers already in hand, frozen, run on the old rig and the new one. This answers findings 2, 3 and 4 and every regression, with the translator held constant, so a difference is the change and nothing else. **No new text is needed for three of the four findings.**
- **Arm B - new text.** Finding 1 changes what gets checked, so it needs prose nobody in the loop has seen. The eight L72 texts are burned (both translators and the orchestrator know their answers).

### Who does what, and what each is blind to
| Role | Agent | Does | Blind to |
|---|---|---|---|
| Corpus maker | orchestrator | writes/collects Arm B texts, seals the map of which text of a pair carries the fault | - (and therefore does not predict) |
| Predictor | Astra Pro, fresh | writes the expectations and the "against" column, each cell naming the layer its firing charges | the map; the texts themselves (gets counts by class and the Arm A ledgers' current reports) |
| Premise checker | Astra Pro, second fresh session | checks every quoted premise against artefact and hash, and every cell for instance-naming, markability and two-sided bracketing; returns PREMISE CHECK | nothing; must not brief the worker |
| Translator 1 | Astra Ultra, fresh | translates the Arm B texts. **Does not run anything** | the plan, the map, the earlier ledgers, the rig version |
| Translator 2 | a second fresh session | translates the four decisive Arm B texts only | the same, plus translator 1's work |
| Runner | orchestrator | runs every ledger on both rig versions; diffs mechanically | - |
| Reader | Astra Pro, third fresh session | traces findings to sentences, on old and new reports shuffled and unlabelled | which report came from which version; ledgers; texts |
| Marker | mechanical where possible; orchestrator for the rest, against the frozen table | | - |

Two changes carry most of the weight: the worker no longer runs what it translates (so a translation cannot quietly empty the checker's arm), and the reader is given old and new reports unlabelled (so "the fix worked" has to show as a difference, not as a good score).

### Expectations, with the "against" column and the layer charged
Arm A (ledgers frozen; old rig vs new):
| | Expectation | Would count against | Charges |
|---|---|---|---|
| A1 | On every ledger in hand, old and new reports are identical once the added sentence tokens are stripped | Any other difference on any ledger | the rig change: it did more than it says |
| A2 | On the L66 reports, the reader traces the seven jumps and no-connections to a sentence (it traced none: L66 results line 39), and traces everything it already traced | The reader traces no more than before | the rig change - and the second run that tells it from a wording fault: the reader is asked which token it used |
| A3 | On P14 the what-if now prints that the dependency was not established; on P11 and P13 the wording is unchanged (premise: P11's dependency *was* established - to be quoted from the report before freezing, not remembered) | The caveat on P11 or P13, or missing on P14 | the rig change |
| A4 | On T07-B the derived contradiction disappears; on every ledger with no told or supposed line the derived list is byte-identical | Any change on a world-free ledger | the tool change |
| A5 | On T10-D and T11-B the reported BECAUSE and SINCE are now tested inside the world and named; T07-B's told world stays clean; T07-D's contradiction stays inside the world | A finding in the actual ledger that names a told line; or T07-B gaining a finding | the rig change |
| A6 | N18-A (F15) and N25-A (F09) report exactly as before: this version does not touch them | Any change | the change reached past its statement |

Arm B (new texts):
| | Expectation | Would count against | Charges |
|---|---|---|---|
| B1 | On each fault-carrying reported-argument text, the checker names the reported BECAUSE or SINCE, on **both** translators' ledgers, where both cite 39's attribution rule | Silence on a text where both ledgers cite the rule | **the language** (39 plus patch 12 still hide the claim). Silence on one ledger only charges the translator, and that text is run again with the rule quoted |
| B2 | On the sound counterparts (a report whose argument connects) nothing is found | A finding | the rig change: it fires on sound reported arguments |
| B3 | On the two texts whose report contains no argument, silence, and the report says which kinds of claim were absent | A finding | the rig change fires on nothing |
| B4 | Every Arm B text yields at least three said lines on both sides | Fewer, on any text | that text's silence is unmarkable and is not counted anywhere (this is the rule L66 lacked) |
| B5 | At least one decisive text has both ledgers citing the rule | None does | B1 is unmarkable; the regime owes another run, and says so rather than marking B1 "met" |

Rules carried over from what went wrong: no cell whose criterion depends on an event the run may not produce, without a positive control (Arm A supplies one: the ledgers in hand include contradictions); no gauge expectation without a threshold fixed before the run (so the bin gauge stays out of this plan until the owner sets the line); marks are computed on the frozen ledgers, and any post-run correction is a labelled second arm, marked separately.

### The near-miss cases that must not change
T07-B (told world clean), T07-D (contradiction inside the world, not outside), P11 and P13's what-if verdicts, every world-free ledger's derived list, N18-A and N25-A, the sound counterparts of Arm B, the no-argument controls, and the whole of Arm A's report text apart from the added tokens. Each is a half of a poke: the change must move the case that forced it and leave its nearest innocent neighbour alone.

### How many texts
**Ten new short texts: four matched pairs (report with a BECAUSE that does not connect / one that does; report with a SINCE that does not connect / one that does) plus two with no argument in the report.** Four of them - one from each pair's fault side - are translated twice. Everything else is a rerun of what is already in hand.

The reason for ten rather than more: nothing in this regime carries an error model, so extra texts of the same kind buy confirmations, not constraint. What buys constraint is the pair: a case that must fire beside its nearest neighbour that must not. If the owner wants a claim about length or about how error grows, that is a separate plan with a stated growth rule - L64 line 13 says none has been measured.

### One thing this plan should also do, cheaply
Salt one file in one return (with the worker's knowledge, after the fact) to see whether the manifest-and-rerun check fires. P9 is the regime's only guard against a bad return and has never met a hard case.

---

## 10. What would make the regime harder to vary

1. **Poke the language.** Run the frozen ledgers under a deliberately wrong 39 (the attribution rule reversed) and check that the reports move exactly where the rule says and nowhere else. That is L64's own variation test (line 143), never run, and it is the only poke that separates the language layer from the rig by itself.
2. **Pre-register the layer charge per cell**, with the second run that separates it from its neighbour. This is what would replace P11 and end the fresh-choice loophole.
3. **The premise block and the second agent's freeze** (section 7). Cheapest of the three, and it addresses the only error the record has made four times.

---

## 11. Lessons (failures only)

- A claim about an artefact was again written from outputs rather than from the artefact, this time about the driver, and it is now one of the four findings said to force a change: L66 results line 39 and Status line 59 say the sentence is printed only in what-if and plan headings and the fix is one driver line. `run_check.py` line 43-48 prints it in eleven branches; `tools/smoke_expected_report_A.txt` lines 5-8 show it in a contradiction report made by this project at L72; and the what-if anchor the reader used is the translator's `whose` field (`P13_OpenAI_Codex.report.txt` line 5), not the driver's. Acting on the finding as written would add sentences where they already are and leave JUMP and NO CONNECTION - the two findings the reader could not trace - untouched, because those branches name no supporting lines.
- Silence was marked as a pass. L66 E2 and E3 are marked met (results lines 34-35) on a run where three passages had no said line at all (record line 89) and where Lesson L2 (Lessons line 29) already said a clean report cannot be read as clean.
- An expectation was marked against a threshold nobody had set: L66 E6 against L64's proposed bin line, which L64 line 179 leaves to the owner.
- Three "would count against" cells did not bracket their predictions, so three misses fell outside them: L66 E1 and E4, L71 E4.
- The marking of L66 E4, E5 and Astra Pro's finding E rests on ledgers the worker revised after seeing the run (`corrections_OpenAI_Codex.json`), while the frozen originals sit unmarked beside them.
- L72's independence rests on an unchecked premise about the agents' harness: the same harness held `results 37` and the earlier ledgers of those eight texts in its L66 bundle (`L66 Handoff ... second version` lines 17, 21; `37 Test results` lines 13-20).

---

## 12. What this does not show

Hard to vary is not true. Nothing here says the four forced findings are wrong (three of them I could check against the code and they hold; the third does not hold as stated). Nothing here says the language is worse or better than the record says. I ran no test, translated nothing, and read the returns partly through the record's own summaries of them. A regime with loose parts can still be producing correct findings - and this one has produced several.

---

## 13. One next step

Before any change is built from forced finding 3, re-read the driver and rewrite the finding from the code: the failure is in the head lines of BECAUSE-claim, SINCE-claim and PLAN and in the JUMP and NO CONNECTION texts, not in "every line a finding names". Then put the premise block and the second agent's freeze into the next plan, and let that plan be the first one that tests the fix.

---

## The three lists

**Parts that never met a hard case.** P9, the return check (no return has ever failed; 13 of 18 rerun at L69). P16, the owner's word. The variation test of L64 line 143. The hostile text L64 line 171 says is owed. Rig 2 (absent from all four plans). The `sameness.py` program on any pair whose forms agree.

**Findings that fit no part.** Three of the four forced findings came from agents going past their briefs, and no part of the regime produces them or would notice their absence. The worker's post-run corrections were used in the marking, and no part says which arm a mark belongs to. The claim that fresh sessions carry nothing between bundles is load-bearing for L72's independence and belongs to no part at all.

**What I did not look at.** Files 38, 39 and 11. `checker_rules.pl` and `check2.py`. The raw s(CASP) logs. Astra Pro's answers file and audit in full (I read its protocol and the orchestrator's check of its seven findings). The eighteen passages and the key. `sameness.py`'s code. Records 01 to 58 except the Decisions file. Whether the reruns at L62, L69 and L72 were byte comparisons or readings.

---

## What would change my mind

- On section 4's fourth case: a report in the L66 return containing a `  - line X [mark, sentence N]` entry, or a line of `run_check.py` that suppresses `describe_lines` for JUMP and NO CONNECTION by design. I grepped all eighteen and found none, and read the two branches; a counter-example would overturn the finding.
- On P11 being loose: a run where a failed cell was charged to a layer against the orchestrator's prior preference, and the charge stuck. I found none in L60 to L75.
- On the regime being unable to refute the language: a plan cell, written before a run, whose firing the record then read as "the language is wrong" without an instrument challenge. L72 E1 is the shape; it has not fired.
- On silence being read as a pass: a marking anywhere that refuses to mark a no-contradiction expectation on a ledger with too few said lines.
- On the premise fix being insufficient: a fifth premise error would settle it further, but so would a clean plan - one where every premise is a quotation with a path, checked by another agent, and the run still loses half its question.
