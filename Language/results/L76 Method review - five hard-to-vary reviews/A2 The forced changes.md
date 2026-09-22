# A2 — Do four findings force a change, and what should change?

Reviewer A2. Repository read only; nothing in `/home/user/ThreadSmith` was touched, and no checker was run. Every verdict below is tagged **read** (I read it in a named file), **seen** (a printed output), **worked out** (my reasoning from tagged things), or **assumed**.

---

## 1. The question, frozen

What is under test here is not the language. It is **the orchestrator's verdict at L75 that four findings force a change, and its rule for deciding which layer changes.** (**read**, `Language/records/Language - project story.md:115`.)

Range: the findings raised in logs L65 to L74, the code they were seen in, and the two earlier failures F15 and F09 that stand beside them.

Kind of question: *does it achieve its purpose?* The purpose is to decide, for each finding, whether the record's own rule obliges a change, and where. So the tests that bite are: remove a part of the verdict and see whether the obligation survives; swap the mechanism given for a near neighbour and see whether the prescribed change is still the right one; poke each finding with a change to the world that should move the verdict and one that should not.

Held still for the whole of this report: the four error sources of L64 section 6, K3 as written at file 11 line 391, and the owner's standing position that nothing is built without a word from them.

---

## 2. The verdict in parts, and the jobs it serves

The orchestrator's words, numbered (**read**, project story:115):

- **V1.** "by the record's own rule that a failed test refutes the bundle (file 10 and 11, K3; L64 section 8): four do."
- **V2.** "Which layer failed is never read off a failed run … It is a fresh choice, and the cost of a wrong choice shows at once through the other jobs of the layer changed." (**read**, `L64 …second version.md:147`.)
- **V3.** The list itself: the told-world BECAUSE/SINCE; the P14 what-if; the missing sentence anchor; `consequences.py` and worlds.
- **V4.** The split: "The rest are decisions or instruments, not refutations."
- **V5.** The mechanism given for each finding — in particular F3's, "the driver prints no sentence beside the lines a finding names".
- **V6.** "No change is made here; every one waits on the owner's word."

The jobs the verdict has to do, marked as the skill asks:

| Job | Tag | Where |
| --- | --- | --- |
| Say when error is acceptable, what is given up, what is got, what success is, at each step | given | decision L4, `Language - Decisions.md:12` |
| The four error sources are kept apart; which layer failed is a fresh choice | given, then constructed | decision L4; L64:147 |
| Every finding 38 promises stays in the list until patched, so absence from a report is never read as "checked" | added (Claude's, in L64) | L64:83 |
| A reader given the report alone names the finding and points at the sentence | given/fixed (the owner's read-back layer) | L64:145 |
| Nothing is built without the owner's word | asserted by the orchestrator; the owner's nearest words are about ownership, not about code | decision L3, `Language - Decisions.md:11` |

A part held only by the third job is *held if* that job is real; it is Claude's, not the owner's, and I flag it where it bears.

---

## 3. Finding by finding

### F1 — a BECAUSE or SINCE inside a told world is never tested

**(a) Is it real? Yes, and it is wider than stated.**

- **read**, `rigs/rig 1 - arguments/patched/run_check.py:69`: `WORLD_REMOVED[:] = all_case_lines`. Every line belonging to *any* named case — told world or supposed case — is stripped from the program for checks 1 to 5 and patches 8 to 14. So check 2 (`:97`, BECAUSE) and check 2b (`:143`, SINCE) can never see a case line.
- **read**, `run_check.py:311-320`: patch 12's per-case loop sets the world (`:313`) and then asks exactly one question, `contradiction(F)` (`:315`). Nothing else is asked inside any world, ever.
- **worked out**: the hole therefore covers supposed cases too, not only told worlds. No run in L65–L74 put a BECAUSE inside a SUPPOSED case, so the supposition half is *worked out*, not *seen*. The orchestrator's F1 names only told worlds.
- **seen**, `L72 Return - Astra Ultra/runs/Astra_Ultra/T10D/checker.stdout.txt:3-5`: "NO FAULT FOUND" and "INSIDE 'account_world' (a told world, looked at alone): no contradiction." Against **read**, `ledger_T10D.pl:16-17`, which carries `claim_because(because, stayed_dry(letter), opened(window))`, and **read**, `ledger_T10D.json`, where that line is `case: account_world, case_kind: told`.
- **seen**, `.../T11B/checker.stdout.txt:3-8`: the same for `claim_since(since, returned(visitor), burning(lamp))` at `ledger_T11B.pl:18-19`.
- **read**, the ledger's own `corpus_question` field on T10-D: "Does achieved dryness establish that opening the window caused it?" That is the question the text was chosen to pose, and the checker says nothing about it.
- **read**, `39 Prompt …:30`: "Who believes, wants or concludes what. Send the attribution to the bin, and write the content as TOLD in that person's world." Astra Ultra followed 39 exactly (**read**, `L72 Test results …:31`).

One correction to the framing. **read**, `38 The ledger language …:105` and `:113`: 38 promises, for a told world, only "a contradiction, or one". The driver therefore **conforms to 38**. The clash is between {38 + 39 + patch 12} and **L64's own scope tables**: `L64:65` puts BECAUSE arguments in scope, `L64:72` puts a told story in scope, and `L64:90` cites **T10-D itself** as the text on which JUMP was *seen*. That earlier sighting was on the orchestrator's own ledger (**read**, `rigs/rig 1 - arguments/ledger_T10D.pl:5`, a bare `claim_because` with no world). So the same text yields JUMP under one translation and silence under the translation that follows 39. Real, and the location is `run_check.py:69` and `:311-320`.

**(b) Does it refute the bundle, and is "forces a change" right?**

Yes. A frozen expectation failed: L72's E5, "the same kind of report on at least six" of eight, came out at five (**read**, `L72 Test results …:40`, plan frozen before the run). K3 (**read**, file 11:391) then yields ¬(T∧B∧I) and nothing narrower: the language, the translator's task, the driver and the scope table cannot all stand as they are.

Is a scope declaration available instead? Formally yes. Part V's non-vacuity (**read**, file 11:259) permits an exclusion provided it is *stated*, and this one could be: "an attributed argument gets contradiction only." Two things close that road in practice. First, `L64:83` already fixes the rule that a promised-and-failing finding stays in the list rather than being quietly narrowed — the F15 and F09 rows exist for exactly this. Second, `L64:116` requires every exclusion to carry a gauge, and the gauge here would have to be a count of attributed BECAUSE and SINCE lines never asked about — which no report prints, so building the gauge is itself a driver change. **Either road changes code.** "Forces a change" survives.

What it does *not* force is a change to the language rather than to the contract. K3 is honest about that and the orchestrator's V2 says so. I agree with the word and with the refusal to name the layer from the run.

**(c) Which layer, and what each gives up**

| Layer | The change | What is given up |
| --- | --- | --- |
| 39, the translator's task | Stop sending attributed content to a told world; write it as an actual claim of the reporter | The whole of 38:105 — "the door can stand open in Nora's story while it stays shut in the room where she tells it". T07-B would then raise a contradiction the text does not contain. Also gives up F02's guard (`L64:123`). Reject. |
| 38, the language | Extend "a contradiction inside one told world is still reported" to "every finding is reported inside one told world, looked at alone" | Adds promises to `L64:84`, and `L64:156` says each promise added is a forcing case owed. Worse: a told world does not inherit the actual ledger (**read**, `38:149`), so a reported argument that leans on everyday background will come out as JUMP where the actual ledger would have connected it. That false-alarm class is the bill. |
| the driver (patch 12) | Run checks 2, 2b, 3, 4 and 5 inside the case loop with the world already set | Run time (every check re-run per world) and report length; and the cross-world bookkeeping must be redone — `:91-93` builds `lines_in_contradiction` from the actual world only, `:266` builds `said_lines` across all worlds, so a told-world finding would be measured against the wrong sets. Not a one-liner. |
| the checker rules | Give every predicate a world argument | Gives up the frozen rules file and, with it, `L64:144`'s guarantee that after every patch every earlier ledger reruns unchanged. Reject for now. |
| the tool | Nothing to do here | — |

**Recommend 38 and the driver moved together, as one change.** Moving the driver alone would have the rig do what the language does not promise; moving 38 alone recreates the F15 shape, a promise the rig does not keep. The pair that pulls here is *scope width against the bin* (`L64:156`): every finding newly asked inside a world is a finding that can now be a false alarm inside a world, and there is no gauge for that yet. The line I would draw: report a told-world finding only where every line it needs lies inside that world, and print a separate count of told-world findings that needed an outside line.

**(d) The smallest new version, in words**

> Inside a named world, told or supposed, looked at alone, the checker asks the same questions it asks of the actual ledger. Each finding is printed under the world's name and its first line says which world it belongs to. Nothing found inside a world is reported as a fact of the actual ledger. A finding inside a told world that would need a line from outside that world is not reported as a finding; it is counted, and the count is printed in the gauge.

**One test, expectation written first.** Run the new driver on Astra Ultra's `ledger_T10D.pl`. *Before the run I expect:* under `account_world`, a JUMP on line `because` — nothing in that world produces `stayed_dry(letter)` even granting `opened(window)` — and no other change: the actual-ledger section still reports no fault in the actual lines, and the gauge's counts are the same. **Refuted if** the JUMP is printed as a fact of the actual ledger, or if nothing is printed for line `because`, or if the actual-ledger section changes at all.

**The near miss that must not change.** Astra Ultra's `ledger_T07B.pl`: a told world holding only Thing lines and a fact, with no BECAUSE, SINCE, plan or likeness inside it. Its report must stay word for word as `runs/Astra_Ultra/T07B/checker.stdout.txt` prints it now, timings aside. If T07-B moves, the change has widened something it did not mean to. (A second near miss is ledger A, which has no worlds at all: `L64:144` already owes an unchanged rerun of every earlier ledger.)

---

### F2 — a what-if answered on the strength of a BECAUSE the same run called a JUMP

**(a) Is it real? Yes, and the sharpest version of it is not the one stated.**

- **read**, `run_check.py:276-281`: `results_tied_to(fact)` walks every `claim_because(N,E,C)` whose cause `C` is the changed fact, and collects the lines that alone state the effect `E`. It consults no verdict, no mark, nothing.
- **read**, `run_check.py:295`: those lines are removed from the query that decides the what-if. `:297` prints "Set aside, because your ledger says they came from what was changed: line(s) …". `:298` prints HOLDS or FAILS, unqualified.
- **seen**, `L69 Return …/evidence/rig1/P14_correction1_OpenAI_Codex.report.txt:3-4`: "BECAUSE-claim on line h … JUMP. Even granting the stated cause, nothing in the ledger produces spreads(helping)." Then `:6-9`: the what-if on the same cause sets line `g` aside and prints "Your what-if HOLDS."
- **read**, `L69 Return …/authoring/P14.py:18`: `h` is `claim_because(h, spreads(helping), exists(group_structure))`, marked **filled in** — a line the writer did not write. `:21` is the what-if, `claims=False`.
- **worked out**: take `h` away and `aside` is empty, `g` stays in, `holds(spreads(helping))` succeeds, `result=True ≠ claims=False`, and the report reads FAILS. The verdict turns entirely on `h`. The control is already in the corpus: P11 has the same fact and the same what-if but `denied_because` instead of `claim_because` (**read**, `P11.py:19`), `aside` is empty, and it reads HOLDS with `claims=True` (**seen**, `P11_OpenAI_Codex.report.txt:5-7`).

**The sharper defect, in the same lines, which the orchestrator's F2 does not name.** **read**, `38:113`: "Every report also carries: a note wherever a finding leans on a line the writer did not write." The what-if block (`:282-298`) never calls `guessed_lines`, unlike checks 1, 2, 2b, 3 and patch 12 (`:89`, `:113`, `:154`, `:199`, `:213`, `:325`). So P14's what-if leans on a filled-in line and says nothing — a promise of 38 broken in print, which `L64:128` repeats in its own words ("a finding that leans on a filled-in reading is conditional; the report says so"). This applies to every what-if, not only to P14's.

**(b) Does it refute, and is "forces a change" right?**

Two clauses of the theory bite, independently.

- **read**, file 11:71, Part I: "What cannot count as explanation is an error in the very dependence alleged to do the work." The what-if's answer is carried entirely by `h`, and `h` is the one thing the same run declared not established.
- **read**, file 11:257, Part V, non-circular dependence: the answer must follow from evaluating the organisation under *independent* boundary conditions, and "moving an assertion from an input slot into a component named 'law' does not discharge this". Here the claim under test — group structure produced the spread — is used as the input that decides the test. `:275` names the failure form: "*p* because *p*".
- **read**, file 11:393: "A record reconstructed from the claim it is meant to support is not a receipt for that claim." The printed HOLDS is precisely such a record.

But is "forces a change" the right word, or is a scope declaration available? **Here a declaration genuinely is available, and Astra Pro wrote it out.** **read**, `L74 Return …/L66_AUDIT.md:77` and `:83`: the procedure "can be internally coherent under an assumption-relative policy", and the defensible replacement sentence is "The encoded counterfactual is satisfied after withdrawing the effect using causal dependency h, which the production check above did not establish." Astra Pro also says plainly at `:81` that "This is not a demonstrated implementation bug."

So the mechanism need not change. What must change is **what the report claims**. That still forces a change — the present print is a claim the theory forbids — but it is a change at the read-back layer and in one sentence of 38, not in the what-if rule. The orchestrator's phrasing ("leans on a BECAUSE the checker judged a JUMP and reports HOLDS without saying so") points at the rule; the finding it came from points at the print. I think the orchestrator has over-read its own auditor here, and the over-reading would cost: see the give-up column below.

**(c) Which layer, and what each gives up**

| Layer | The change | What is given up |
| --- | --- | --- |
| 39 | Nothing. `h` is a legitimate filled-in reading of "the group structure produces the spread" (**read**, `P14.py:29`) | — |
| 38 | One sentence saying what a what-if answers: the writer's own BECAUSE lines are taken at their word | The reading of a what-if as a test of the world rather than of the ledger. That reading was never written down, so what is given up is an impression, not a promise |
| the driver, report only | Print every line set aside, the BECAUSE line that tied it, that line's own verdict from the checks above, and a note wherever a line used is one the writer did not write | Two lines of report length. Nothing else |
| the driver, refuse the tie | Set a result aside only where the tying BECAUSE was not judged a JUMP | Nearly every what-if on a bare causal claim. Check 2 calls a BECAUSE a JUMP whenever no general line produces the effect, which is the common case (T10-D, P09 twice, P14). Patch 13 would switch off for the texts it was built for, and the F09 failure would return from the other side. **Reject** |
| the checker rules, the tool | Nothing | — |

**Recommend 38 plus the driver's disclosure.** Note the joint: `results_tied_to` at `:276-281` is the one function that F09 and F2 both run through. F09 is a fact that survives a change it should have been tied to; F2 is a fact set aside on a tie that should not have carried the weight. The record holds them as two separate items awaiting two separate words from the owner (**read**, project story:115, and `L64:147`). They are one joint and should be decided together, or the second decision will undo the first.

**(d) The smallest new version, in words**

> A what-if answers this question: taking the writer's own stated causes at their word, does the asked-about fact survive the change? The report prints the change made; every line set aside, with the BECAUSE line that tied it and that BECAUSE line's own verdict from the checks above (follows, jump, circle, or not reached); a note wherever any line used was not written by the writer; and then holds or fails.

**One test, expectation written first.** Rerun the new driver on P14's ledger. *Before the run I expect:* the verdict stays **HOLDS**; the report gains one block naming `h` as the tie, saying `h` was judged a JUMP above, and noting that `h` is a line the writer did not write. **Refuted if** the verdict changes to FAILS (that would mean I changed the mechanism, which I did not mean to), or if `h` is not named.

**The near miss that must not change.** P13's what-if (**seen**, `P13_OpenAI_Codex.report.txt:5-7`): a MAKE NOT SO where no `claim_because` ties the fact, so `aside` is empty. It must gain no "set aside" block and must still read FAILS. Second near miss: P11, same fact, `denied_because` not `claim_because` — must still read HOLDS with no tie named.

---

### F3 — no sentence to trace a finding to

**(a) Is it real? The failure is real. The mechanism given for it is false, and the fix prescribed from that mechanism would not work.**

The failure, first. **seen**, `L66 Test results …:39` (E7): of seven jumps and no-connections the reader "named all seven findings correctly and traced the sentence for **none** with confidence"; of four what-if and plan findings it traced all four.

Now the mechanism. **read**, `run_check.py:47`:

```
parts.append('  - line %s [%s, sentence %s]: %s' % (line_id, info["mark"], info["sentence"], info["text"]))
```

`describe_lines` **already prints the sentence beside every line it names**, and it is called from CONTRADICTION (`:86`, `:88`), FOLLOWS (`:106`), CIRCLE (`:120`), SINCE-holds (`:151`), PLAN (`:196`, `:212`), DEPARTURE (`:229`), PULL OPPOSITE (`:257`), ADDED LINES (`:272`), what-if-cannot-be-run (`:293`), DENIED BECAUSE with a route (`:307`) and the supposition contradiction (`:324`).

The real defect is the branches that **name no lines at all**: JUMP (`:126-138`), FOLLOWS ONLY IF GRANTED (`:125`), NO CONNECTION (`:157-162`), CANNOT TELL on a plan (`:206`), the chain rows (`:179`, line id and text only), the what-if verdict (`:296-298`, bare line ids at `:297`), the world's "no contradiction" line (`:320`), UNEXPLAINED EXCEPTION (`:231`), EXEMPTION (`:263`), DENIED BECAUSE "fine" (`:308`) and NO FAULT FOUND (`:335`). Those are exactly the seven findings the reader could not trace.

And the four it *could* trace were not traced from the driver's own words:

- **read**, `L69 Return …/authoring/P14.py:21`: `whose='OpenAI Codex, L66, sentence 8 line j'`. The sentence number in the what-if heading is a string the **translator** wrote into the ledger's `whatifs` block, which the driver echoes verbatim at `:296`. It is not the driver's.
- **read**, `L74 Return …/L66_AUDIT.md:41`: "P16's gauge connects plan `b` with **sentence 3**." The plan trace came from a bin entry in the gauge, not from the heading at `:193`, which prints no sentence.

So all three statements of the mechanism in the record are wrong. `L66 Test results …:39`: "the driver prints '[…, sentence 8 line j]' in those headings and nowhere else" — it prints what the translator put there. The brief's F3: "prints the sentence number only in what-if and plan headings" — it prints it in neither, and prints it in eleven other places. L75: "the driver prints no sentence beside the lines a finding names" — it does, wherever `describe_lines` is called.

The consequence matters. The fix prescribed twice from that mechanism (**read**, `L66 Test results …:39` and `:61`, "The fix is one line in the driver: print the sentence beside every line a finding names"; `:68` "a driver change, one line; I ask leave to make it") **would change nothing for the seven failures**, because those findings name no lines through `describe_lines`. It would be built, E7 would be rerun, and E7 would fail again. This belongs in Lessons.

**(b) Does it refute, and is "forces a change" right?**

Yes, and this is the one of the four where the scope-declaration escape is already spent. **read**, `L64:145`, the read-back row, in the owner's own error table: the error that is *not* acceptable is "Any finding a reader cannot trace to a sentence"; success is "A reader given the report alone names the finding and points at the sentence". E7 was frozen before the run and came out against. K3 applies and no declaration is available, because the contract has already declared the opposite. "Forces a change" is exactly right.

But the rule for *what* to change failed here, which is a finding against V2 and V5, not against V1.

**(c) Which layer, and what each gives up**

| Layer | The change | What is given up |
| --- | --- | --- |
| 39 | Make the translator write the sentence into every line's text | Double-recording: the JSON already carries `sentence` per line and `:47` uses it. Two records drift. Reject |
| the driver | Add the sentence to the heading templates (`:99`, `:145`, `:193`, `:306`) and a `describe_lines` block to the JUMP, NO CONNECTION and CANNOT TELL branches | Report length; and for a JUMP the lines to describe must be chosen — the claim line, the cause's lines, the direct lines — a choice that can over-name and make a bare jump look better supported than it is |
| the checker rules | Nothing; sentences do not exist in Prolog | — |
| the tool | `consequences.py:61` and `:69` print line ids with no sentence at all, and the reader traced only two of eight derived consequences (**seen**, `L66 Test results …:39`) | Nothing; the tool has the same `meta` in hand. The orchestrator's F3 does not mention the tool, so a driver-only fix leaves half of E7 failing |

**Recommend the driver and the tool, together.**

**(d) The smallest new version, in words**

> Every finding names at least one line. Every line a finding names is printed in the one fixed form that already exists: line id, mark, sentence number, the line's own words. Headings name their line in that same form. A finding that names no line of the writer's — a jump, a no-connection, a cannot-tell — names the claim line whose test failed, in that form, and separately lists the lines it searched. The consequences program prints the same form for every line it cites.

**One test, expectation written first.** Rerun the new driver on the L66 ledgers for P01, P07, P09 and P14, and give the four reports to a reader who has not seen the passages. *Before the run I expect:* each of the seven jumps and no-connections now carries a sentence number beside its claim line; the reader names the sentence for all seven; and nothing else in the four reports changes but the added `[…, sentence N]` text. **Refuted if** a sentence number is still absent on any of the seven. (If the anchors are present and the reader still refuses to trace, that is a second finding, about wording, not about anchors.)

**The near miss that must not change.** T07-D's contradiction report, where `describe_lines` already prints the sentence. It must come out word for word as before. If it moves, the change has reached into `describe_lines`, which was never the fault.

---

### F4 — `consequences.py` never sets the driver's world list

**(a) Is it real? Yes, plainly.**

- **read**, `run_check.py:11`: `WORLD_REMOVED = []` is a module-level global. `:16` has `run_query` subtract it from every program it builds. `:69`, inside `check()`, is the only place that ever sets it.
- **read**, `tools/consequences.py:21-22`: the driver is loaded as a module; `:41` calls `rig.run_query(...)` directly. `check()` is never called. So `WORLD_REMOVED` stays `[]` and every told and supposed line sits in the program beside the actual ledger.
- **seen**, `runs/Astra_Ultra/T07B/consequences.stdout.txt:4`: `contradiction(open(door))   <- lines actualshut, storyopen`; `:16` and `:23` confirm both lines are needed. Against **seen**, `runs/Astra_Ultra/T07B/checker.stdout.txt:3-5`: "NO FAULT FOUND", "INSIDE 'nora_story' … no contradiction." Same ledger, same rules, two answers.
- **read**, `38:105`, the clause this contradicts, using this very example: "the door can stand open in Nora's story while it stays shut in the room where she tells it".
- Confirmed independently by the orchestrator on its own T07-B (**read**, `L72 Test results …:49`) and logged as Lesson L7.

**(b) Does it refute, and is "forces a change" right?**

"Forces a change" is right; **K3 is the wrong warrant for it, and citing K3 here hides the lesson.** No frozen expectation failed: L72's E6 predicted "0 derived on at least six; never more than 2" and the run met it (**read**, `L72 Test results …:41`). The finding came from Astra Ultra *reading the program*, not from a test (**read**, `L72 Test results …:49`). K3 needs an established ¬O; there is none. What there is, is simpler and more certain: a program whose own docstring says it "Uses the rig-1 driver's own run_query (same rules, flags, time limit)" (**read**, `consequences.py:4-5`) and which does not use the same world list. That sameness claim is what misled, and the claim is in the file.

A declaration is available — "consequences are computed with worlds pooled" — and would be wrong, because `L64:25` puts "Open a told world and look at it alone" in the **contract of admitted changes**, not in the give-ups.

**(c) Which layer, and what each gives up**

| Layer | The change | What is given up |
| --- | --- | --- |
| 39, 38, the rules | Nothing | — |
| the tool alone | Set the world list before each ask | Nothing visible — and that is the objection. It leaves the trap in place, and the give-up that would have to be logged is "the next tool that reuses `run_query` has the same fault", which nobody will read |
| the driver | Make the world an argument of `run_query`, not a module global; refuse to run without one | Every caller changes — there are two, `check()` and `consequences.py`. And the driver file changes, which under `L64:144` owes a rerun of every earlier ledger, report against report. The harness for that already exists: L69 reran 13 and L72 reran 16, all identical (**read**, project story:89, :107) |

**Recommend the driver.** The defect is the shared mutable global, not the tool's forgetfulness. Fixing the tool treats the symptom that was seen and leaves the cause that produced it. The pair that pulls: making the world an argument makes `check()` more explicit and slightly longer, since its forty-odd `ask` calls must inherit it. Where I would draw the line: keep `ask` as the closure that supplies the world, and make `run_query` itself refuse a call with no world given, so that silence is impossible.

**(d) The smallest new version, in words**

> The world a query runs in is an argument of the query, not a setting left lying about. The query function takes the list of lines outside the world, and refuses to run when it is not given one. The driver's `ask` supplies the actual world by default and the case's world inside the case loop. The consequences program takes the world the same way: it reports the actual ledger's consequences under the actual ledger, and each told or supposed world's consequences separately under that world's name.

**One test, expectation written first.** Run the new consequences program on Astra Ultra's `ledger_T07B.pl`. *Before the run I expect:* `contradiction(open(door))` is gone from the actual ledger's derived list; the actual list has no derived facts at all; a separate section for `nora_story` lists the story's own facts and no contradiction; and the checker's report on the same ledger is unchanged. **Refuted if** `contradiction(open(door))` survives anywhere as a consequence of the actual ledger.

**The near miss that must not change.** Ledger A, the tomato ledger of L65, which has no worlds. Its output must match the L65 prototype line for line — ten derived facts on the full ledger, thirty-two delta lines over thirteen removals (**read**, project story:26). If A moves, the fix has reached past worlds.

---

### F15 — a BECAUSE and its exact denial in one ledger raise no contradiction

Briefly, as the task asks.

**(a) Real.** **read**, `45 Test results …:45`: on N18-A the BECAUSE is a JUMP, the NOT[BECAUSE] is reported "Fine", and no contradiction is raised though the two share effect and cause; N18-B, the denial alone, correctly reports nothing. **read**, `checker_rules.pl:18`: `contradiction(F) :- holds(F), denied(F)` relates facts only; nothing relates `claim_because` to `denied_because`. **read**, `run_check.py:300-308`, patch 14: the denial is tested against whether the ledger *produces* the effect from the cause, never against the presence of the matching claim. So the two are invisible to each other. Promised at `38:111` and kept visible at `L64:108` as "promised (38 line 111) and failing".

**(b)** Not a K3 refutation of a live bundle. It is a promise the language makes in print that the rig does not keep, already recorded as failing. That is a stronger obligation than a refutation, not a weaker one: `L64:83` says such a row stays in the promise list until patched precisely so that its absence from a report is never read as "checked". "Forces a change" is right, and it has been right since L62.

**(c)** The rules or the driver. One clause raising a contradiction where a `claim_because` and a `denied_because` share both effect and cause; or patch 14 checking for the matching claim. **Given up either way:** a writer who says "A because B" and later "not A because B, in a different respect" now gets a contradiction they do not mean — which is what Astra Ultra's T07-D line "in the same context and respect as line open" was written for (**read**, `L72 Test results …:39`). The change owes a rule for "respect", or a declared give-up.

A remark on the orchestrator's rule, not on the finding: F15 is the readiest change in the whole record. Its forcing case is written, its control N18-B is written and must stay silent, and the record already names it as the first pile-2 change to make (**read**, `45 Test results …:73`). L75 places it *after* four newer findings whose forcing cases are not yet written. Newness is not a reason.

### F09 — an actual fact rides into a what-if

**(a) Real.** **read**, `45 Test results …:39`: on N25-A, "MAKE NOT SO: pushed(box)"; the actual line "the box moved after the push" is written as a plain Fact, tied to nothing, so it survives the change and the what-if HOLDS. The right answer under 38 is "cannot tell". N25-B, with the source's own no-push account, fails and reports a contradiction.

**(b)** A confirmed failure of the language, reran; "forces a change" right.

**(c)** The orchestrator's own note is the model the skill asks for, and I quote it because it is the pattern (**read**, `L64:147`): "F09 is left open for exactly this reason: the fix in the what-if rule would give up 'after' as a plain fact; the fix in the translator would give up an honest translation of 'after'." That is a pair that pulls, named, with the give-up on each side, and with the reason for leaving the layer open stated. It is the only place in the record where a forced change is held open *for a stated reason* rather than for the owner's diary.

**What that pattern shows about the four.** F09's note names both sides and the cost of each. Of the four in L75, only F1's entry gestures at a layer ("a second standing after F09 that hides a claim from the checker") and none names what the fix gives up. `L64:144`'s checker row and `L72 Test results …:49` do log give-ups elsewhere, so the habit exists; it was not applied to L75's list. Applying it is cheap and would, on my reading above, have moved F2 from the what-if rule to the print, and F4 from the tool to the driver.

**One more thing about F09 and F2 together.** `results_tied_to` (`run_check.py:276-281`) is the single function both failures run through. Deciding them apart risks the second decision undoing the first.

---

## 4. The verdict's parts, marked

Never added up. Provenance in its own column.

| Part | Mark | Provenance |
| --- | --- | --- |
| V1. "A failed test refutes the bundle" as the rule that makes a change forced | **Borrowed** — rests on file 11 Part IX, K3 (file 11:391), which is not tested here and whose rival (a rule that pins failure on one layer) is never set beside it. `L64:163` lists the borrowed parts and K3 is not among them | asserted (quoted into L64:147; nothing in this thread derives or tests it) |
| V2. "Which layer to change is a fresh choice" | **Held** — by the F09 note at L64:147, which shows a real fork with a stated cost on each side; remove the part and F09 would have been patched in the wrong layer | built |
| V3. The list of exactly four | **Loose** — a near neighbour list does the same job as well or better: five, with NO FAULT FOUND added (section 5 below); or three, with F4 moved out of "refutation" since no expectation failed | fitted (assembled from the four most recent returns; newness, not readiness, sets the membership — F15 and F09 sit below it) |
| V4. The split "refutations" against "decisions or instruments" | **Held if** — held only if the things called instruments are working instruments. `L66 Test results …:39` and `L74 …/L66_AUDIT.md:65` say the bin gauge is not one. What would settle it: a gauge that reads differently on Lucretius and on the hardest modern passage | built |
| V5. The mechanism given for F3 | **Loose** — swap "only in what-if and plan headings" for "only where `describe_lines` is called", and the E7 result is explained as well, and the prescribed fix changes. The stated version is contradicted by `run_check.py:47` | fitted (read off four traced cases, not off the code) |
| V6. "Nothing is built without the owner's word" | **Held if** — held if decision L3 (`Language - Decisions.md:11`, "you're still orchestrator, I'm not handing the whole project over") covers code changes as well as project direction. What would settle it: one sentence from the owner | asserted |

---

## 5. Findings in L65 to L74 that force a change and were not listed

L75 puts these outside the four: "the bin threshold and gauge (L66 E6), Thing lines (L72), the told-world wording (L72), the near score and NOT (Lesson L8), stated facts hiding derived ones (L71)". Five of my six below are not in that list either — they are simply absent from L75.

**(1) NO FAULT FOUND printed where the question was never asked.** **read**, `L64:145`: the read-back layer's *unacceptable* error includes "a report that reads NO FAULT FOUND without saying which questions were never asked (Lesson L2)". The owner's own error table names it. **read**, `run_check.py:334-335`: the header is inserted by a keyword search over the report's own text. **seen**: T10-D, T11-B and T07-B all print "NO FAULT FOUND in the lines that were checked" while the only argumentative line in each was never asked about. **seen**, `L74 …/L66_AUDIT.md:51` and `:53`: P16 prints the clean header and then cannot tell; P04 prints it with zero said lines, no facts found and no derived facts. **read**, Lesson L2: 640 of 2,085 raw-log sections are "predicate does not exist" answers counted as "no such claims". This forces a change by the contract's own words, and it is what makes F1 dangerous rather than merely incomplete: F1 alone is a gap; F1 with the clean header is a gap reported as a clean bill. *Related, and unseen:* **worked out**, `run_check.py:334` — "RAN OUT OF TIME" (appended at `:76`) and "CANNOT TELL" are not in the keyword list, so a ledger whose every query timed out would still print NO FAULT FOUND. No run in the record shows this; mark it unknown and check it in one line.

**(2) A sentence that reaches neither a line nor the bin, with the gauge still green.** **read**, `rigs/rig 1 - arguments/ledger_T10B.json`: three sentences; `leftover` is empty; no line carries sentence 3 ("The account gives no reason for its dryness"). **worked out** from `run_check.py:331-333`, which prints `len(meta["leftover"])` of `len(meta["sentences"])`: the gauge reads "0 of 3 sentences went to the leftover bin". The report says nothing was left out while a whole sentence was. Recorded at `L72 Test results …:29` and project story:107 as "my lapse". It is not only a lapse: nothing in the driver, in 39's final checks, or in the gauge makes a sentence account for itself. **read**, `L64:142`: the scope layer's unacceptable error is "A gauge that stays green while the bin, 'cannot tell' or 'not checked' absorbs a job". One line in the driver — every sentence appears in some line's `sentence` field or in the bin — would have caught it, and would catch it in every future translator's return.

**(3) The bin's gauge cannot discriminate, so the one catch-all is unguarded.** The orchestrator files this as an instrument question and the threshold as the owner's; both are true and neither is the point. **read**, the skill: a catch-all is allowed only with a gauge that would show it swallowing a job. **seen**, `L66 Test results …:39` and project story:111: every one of eighteen passages lost something from more than a third of its sentences, ten of eighteen from every sentence, Lucretius included. A gauge that reads the same on the easiest and the hardest passage shows nothing. **read**, `L74 …/L66_AUDIT.md:65`: "'Every sentence has an excluded fragment' and 'no sentence was checked' cannot be treated as equivalent." The change forced is small and is not the threshold: count fully represented, partly represented and unrepresented sentences apart (`L66_AUDIT.md:69`). Until then `L64:134`'s claim that "the bin is the one catch-all" and its gauge "is already printed in every report" is not met.

**(4) A what-if verdict leaning on a filled-in line carries no note.** Given in full under F2 above. `38:113` promises the note; `run_check.py:282-298` never calls `guessed_lines`; P14's `h` is filled in. Strictly a sub-finding of F2, but it is a broken promise in 38's own words — which F2 as stated is not — and it applies to every what-if.

**(5) L64 section 8's own trigger may have fired at L72 and been read away by hand.** **read**, `L64:174`: what would show the scope wrong includes "Two ledgers of one text, by translators who have read no ledger, that differ in said-content on a text inside section 3". **seen**, `L72 Reruns by the orchestrator/sameness/sameness_T10D.txt`: the program lists "line 3 … the letter stayed dry BECAUSE the window was opened" under **ONLY THE FIRST SAYS**. **read**, `L72 Test results …:29` and `:66`: the hand pairing matched all 21 lines by treating a TOLD line as the same content as a CLAIMED one. That is defensible, but it is the reading under test — F1 exists precisely because TOLD and CLAIMED are *not* the same content to the checker. The same fact is scored as "same content, different standing" when marking E1 and E2, and as a hidden claim when reporting F1. One of the two readings has to go, and which one goes decides whether `L64:174`'s trigger has fired.

**(6) `consequences.py` says "nothing changes" where it means "no change in the reported fact set".** **read**, `consequences.py:72`; and `:64-65` removes one line at a time only, so two routes to one fact always print as two idle lines. **read**, `L74 …/L66_AUDIT.md:99-107`: P09's `c` and `y` each cover for the other; P01's `r` and `a`+`b` likewise. Cheap to fix and it is wording, but it is the wording that let L71's result — "a general line whose only work is to derive a fact the writer also states is invisible" (**read**, project story:97) — read as a fact about the ledger rather than about the program.

---

## 6. Whole-explanation checks on the verdict

**Flip.** Had L72 and L66 come back clean, could the verdict have covered it? Yes, and that is fine: the verdict is a reading of particular reports, not a standing theory. The flip does not bite here; I name it rather than leave it out.

**Reverse.** Poke the supposed cause and the effect should move: take `h` out of P14's ledger and the what-if verdict flips from HOLDS to FAILS (**worked out**, `run_check.py:276-281`, `:295`). Poke the effect and the cause should not: change the what-if's `claims` from false to true and `h` is unaffected. F2's causal story survives both. The same run on F3 fails the reverse: poke the stated cause ("no sentence in the headings") by adding sentences to the headings, and six of the eleven `describe_lines` sites already have them — the effect was never there to move.

**The answer in the starting points.** V1 makes a change forced by definition wherever an expectation fails. On F4 no expectation failed and the verdict still reads "forces a change", so the conclusion was reached first and K3 fitted to it afterwards.

**Add a job.** Require the verdict to name, for each finding, what the fix gives up — the job `L64:144` already imposes on every patch. Three of the four give-up columns are empty in L75. The job rules out the version of F2 that changes the what-if rule, because that version's give-up (patch 13 switching off for bare causal claims) is disqualifying, and it rules out the tool-only fix for F4.

**Look inside.** The four verdicts were reached from reports and from two auditors' prose. Three of the four hold up when read against the code; F3's does not. Matching the reports is not matching the workings.

**Pairs that pull.** *More findings asked inside worlds* against *more false alarms inside worlds* (F1). *Setting results aside* against *taking unestablished causes at their word* (F2 and F09, one joint). *Scope width* against *the bin* — widening to told-world arguments adds promises and each is a forcing case owed (`L64:156`). *Computability* against *meaning* (`L64:157`): F1 is this pair in its purest form, since TOLD is a computable standing that changes what is checked, and the translators disagree about what it means.

**Check the patches.** Patch 12 (`:310-327`) was built for F06 and F09 and gave up "a case inside a case" (**read**, project story:40). It also, undeclared, gave up every check but contradiction inside a case — that give-up is not in the give-up list and is F1. Patch 13 gave up "a result with two stated causes is set aside when only one is withdrawn" (project story:41); its second give-up, that the tie is taken on trust from a claim that may be a jump, is not in the list and is F2. **Two of the sixteen logged give-ups are incomplete, and both omissions became findings the record then discovered by other means.**

**Catch-alls and their gauges.** The bin's gauge is saturated (section 5, item 3). "Cannot tell" and "not checked" have counts. NO FAULT FOUND is itself a catch-all with no gauge at all: it absorbs "checked and passed", "no eligible target" and "never asked", and nothing printed tells them apart (`L74 …/L66_AUDIT.md:55`).

**What the change list leaves out.** No hostile text has been run (`L64:171` owes one). No fault-free ledger has been tested for consequences (**read**, project story:97). Rig 2 is untouched by all six findings. No second reader has been run against the same reports, so E7 rests on one reader.

**Rivals.** A rival account of all four findings: *they are four instances of one thing — the rig answers a narrower question than the report's wording claims, and the record checks the answer rather than the wording.* On F1 the narrower question is "does this world contradict itself"; on F2 "does the effect survive, taking the writer's causes at their word"; on F3 "which lines clash", not "which sentences"; on F4 "what follows from all the lines". Every one of the four is a gap between the question computed and the question printed. I cannot tell this rival apart from the orchestrator's four-separate-faults account with anything on the change list, and it changes what one would do: it would put the read-back layer first for all four, and it would make item (1) of section 5 the head of the list rather than an omission from it. **Say it as a rival, and ask the owner which question each check is answering, before patching any of them.**

---

## 7. Lessons

**L(A2)-1. A fix was prescribed twice from a mechanism that the code contradicts.** `L66 Test results …:39`, `:61` and `:68` all say the driver prints the sentence "in those headings and nowhere else" and that the fix is "one line in the driver: print the sentence beside every line a finding names". `run_check.py:47` prints the sentence beside every line `describe_lines` names, in eleven places; the seven failing findings name no lines through `describe_lines` at all; and the sentence numbers in the three traced what-if headings are strings the translator wrote into the ledger (`P14.py:21`), echoed at `:296`. Built as written, the fix would not move E7. Same family as Lessons 51, L6 and L9 — a statement about a thing written from a picture of it rather than from the thing — and this is the fourth time. The earlier three were about plans written from descriptions of cases; this one is about a repair written from a description of code. Fix: before a repair is proposed, print the lines of the file it names and quote them in the proposal.

**L(A2)-2. A give-up list that is not complete turns into a finding later.** Patches 12 and 13 each logged one give-up and left a second undeclared; the two undeclared ones are now F1 and F2, found months later by two outside agents. Fix: a patch's give-up entry names every question the patch stops asking, not only the one that motivated it.

**L(A2)-3. K3 was cited where no expectation failed.** F4 met its expectation (L72 E6) and was found by reading a program. Calling it a refutation of the bundle borrows authority the evidence does not supply, and it buries the actual lesson — shared mutable module state — which Lesson L7 states correctly and L75 does not carry.

---

## 8. What would make the verdict harder to vary

- **Print, beside each of the four, what the fix gives up and what the rival fix gives up.** `L64:144` already requires this of every patch and `L64:147` models it on F09. Three of four are missing it. This single addition would have decided F2's layer and F4's layer on the evidence already in hand.
- **Ask, for every check, "what question does this compute, and what question does the report claim?"** That is the one job that tells the four-separate-faults account apart from the single-gap rival in section 6, and it is a job no run so far has been asked to do.

## 9. Parts that never met a hard case, and findings that fit no part

**Never met a hard case:** patch 12's told-world isolation has been run only on ledgers whose told worlds contain no argument, so its behaviour with F1 fixed is untested. `results_tied_to` has been run on exactly two what-ifs with a live tie (P14, N25-A). The read-back job rests on one reader on one bundle. The bin gauge has never been run on a text built to hide something in the bin (`L64:171`).

**Findings that fit no part:** Astra Pro's finding E (`L66_AUDIT.md:87`), that P10's "derived" `depends_on` is line `g` in a second notation, fits neither the four nor the "instruments" list; the orchestrator added it to the consequences fix list (project story:111) without saying what it is a failure of. My reading: it is the same gap as the rival in section 6 — the program computes "new atom" and the report claims "unstated commitment".

## 10. What this does not show

Nothing here shows that the language is wrong, that any of the four findings is unfixable, or that the orchestrator's four are not worth fixing. Hard to vary is not true. I did not run the checker, the consequences program or the sameness program; every "seen" tag above is on output the returns already contain, and every claim about what a changed program *would* print is **worked out**, not seen. I did not read rig 2, the L65 or L71 raw outputs, the L66 corpus key, or files 10 and 12. I did not test whether the reader's failure to trace was caused by the missing anchors or by the wording around them; E7 rests on one reader and cannot separate those.

## 11. One next step

Before any of the six changes is built, put one question to the owner: **for each of the checks named above, which question is the checker computing, and which is the report claiming?** Write the answer as a table beside `L64:84`. On my reading that table decides F2 (print, not rule), F4 (driver, not tool), F3 (the branches that name no lines, plus the tool) and item (1) of section 5 in one pass, and it is cheaper than any of them.

## 12. What would change my mind

- **On F3:** a run of the present driver in which a JUMP or NO CONNECTION report prints a sentence number. I say it cannot, from `run_check.py:126-138` and `:157-162`. One report would settle it.
- **On F2:** a statement from the owner that a what-if is meant to test the world rather than the ledger. Then the print is not enough, patch 13's tie must be refused, and the give-up I called disqualifying is one the owner has chosen to pay.
- **On F4 and K3:** a frozen expectation from L71 or L72 that the pooled-world contradiction actually failed. I found none — L72's E6 was met — but I read the plans only through the results files, not the plans themselves.
- **On F1's layer:** a run showing that told worlds, looked at alone, produce a flood of jumps from missing everyday background (`38:149`). That is the bill I priced as the main cost of the 38-plus-driver route; if it is large, the driver-only route with findings suppressed where an outside line is needed becomes the better buy.
- **On section 5, item 5:** a ruling that TOLD and CLAIMED content count as the same said-content for the sameness test. Then `L64:174`'s trigger did not fire at L72, and my fifth item falls.
- **On the whole verdict:** if the owner's answer to section 11's question is that every check already computes what its report claims, then my rival in section 6 is dead and the four stand as four separate faults.
