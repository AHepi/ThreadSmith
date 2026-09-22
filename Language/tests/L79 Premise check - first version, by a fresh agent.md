# PREMISE CHECK - L79 Test plan, Arm A

Checked against the working tree at /home/user/ThreadSmith. The plan file itself hashes to 8f68177ff96be63c. Nothing in the repository was modified. All runs were made on copies under the scratchpad.

---

## Part 1. Premises

**P1. FOUND.** `results/L72 Return - Astra Ultra/runs/Astra_Ultra/T10D/checker.stdout.txt` hashes to 1e8b31f213443ff9, as stated. Line 3 is "NO FAULT FOUND in the lines that were checked." Line 5 is "INSIDE 'account_world' (a told world, looked at alone): no contradiction." The word "because" does not appear anywhere in the report. The ledger does hold a line named `because`.

**P2. FOUND.** `.../T11B/checker.stdout.txt` hashes to f084b71881f81781. Line 3 is the NO FAULT FOUND line. Line 8 is "INSIDE 'inspector_world' (a told world, looked at alone): no contradiction." The word "since" does not appear anywhere in the report. The ledger does hold a line named `since`.
One thing the premise leaves out. This report also carries a DENIED BECAUSE finding on line `notbecause` at lines 5 and 6. A5 says the actual-ledger findings on this file must stay as before. P2 does not quote those two lines, so that part of A5 rests on text no premise pins.

**P3. FOUND.** `.../T07B/checker.stdout.txt` hashes to ddd1088f0f4be5fa. Line 3 and line 5 read exactly as quoted.

**P4. FOUND.** `.../T07D/checker.stdout.txt` hashes to 0927cc618307b822. Line 3 reads exactly as quoted. The ledger's JSON confirms the case kind. All three lines of that ledger carry `case: nora_description` and `case_kind: told`. So the report does print supposition wording over a told case, which is what D6 is for.

**P5. FOUND.** `.../T07B/consequences.stdout.txt` hashes to ac5ae5a397592101. Line 4 is "  contradiction(open(door))   <- lines actualshut, storyopen". The quotation matches apart from the leading indent, which the plan does not reproduce.

**P6. FOUND.** `results/L69 Return - L66 run by OpenAI Codex/evidence/rig1/P14_correction1_OpenAI_Codex.report.txt` hashes to 3be0a3dc9517e8ca. Line 4, line 8 and line 9 read exactly as quoted.

**P7. FOUND.** `P11_OpenAI_Codex.report.txt` hashes to 0a56e3233352b4bc; line 7 is "  Your what-if HOLDS." and no "Set aside" line appears. `P13_OpenAI_Codex.report.txt` hashes to ae011f2f69614182; line 7 is "  Your what-if FAILS." and no "Set aside" line appears.

**P8. FOUND.** `P01_correction1_OpenAI_Codex.report.txt` hashes to f631f5f1e7873c8d, with NO CONNECTION at lines 4 and 8. `P09_OpenAI_Codex.report.txt` hashes to 8fe573544c01a423, with JUMP at lines 4 and 7. `P16_OpenAI_Codex.report.txt` hashes to 62600e819b893168, with CANNOT TELL at line 6. None of the three files contains a single line beginning "  - line".

**P9. FOUND.** `tools/smoke_expected_report_A.txt` hashes to 4d83b8c3f3dc34be. Line 3 is "CONTRADICTION about dies(door_plant)." Line 5 is "  - line 2 [said, sentence 3]: the plant by the door is a tomato plant". Line 28 opens with the gauge text as quoted and then continues "Slowest question: 0.10 seconds." The quotation is a prefix of the line, not the whole line.

**P10. FOUND.** I copied the rig and ran the old driver. It printed "GAUGE: 3 lines said, 0 filled in, 0 usual case; 0 of 3 sentences went to the leftover bin (not checked)." word for word. `ledger_T10B.json` has three sentences, three lines carrying sentences 1, 1 and 2, and an empty leftover. So sentence 3 reached neither a line nor the bin. The premise is right on every count.

**P11. FOUND.** `results/45 Reruns by the orchestrator/report_ledger_N18A.txt` hashes to f4d5c39567c12d03, with the JUMP at line 4, the DENIED BECAUSE at line 6 and "Fine." at line 7. `report_ledger_N18B.txt` hashes to f5e4747a450c43b3, with NO FAULT FOUND at line 3, DENIED BECAUSE at line 5 and "Fine." at line 6.

**P12. FOUND.** `report_ledger_N25A.txt` hashes to 7f4e387a1915f9b3, with NO FAULT FOUND at line 3 and "  Your what-if HOLDS." at line 7. `report_ledger_N25B.txt` hashes to 2b41d3d1a965f2eb, with "  Your what-if FAILS." at line 5 and the supposition contradiction at line 7.

**P13. FOUND.** `run_check.py` hashes to eff1dee15bebc977 and `consequences.py` to 782047f829cf6b39. `WORLD_REMOVED` appears at exactly five places: the declaration at line 11, the read at line 16, and three assignments at lines 69, 313 and 327. `check()` spans lines 62 to 336, so all three assignments are inside it and there is no other writer. Line 41 of `consequences.py` is `rig.run_query(ledger_text, q, removed_lines=removed)`, with nothing set beforehand. Since `consequences.py` imports the driver as a module and never calls `check()`, `WORLD_REMOVED` stays empty and the tool sees told-world lines mixed into the actual ledger. That is the mechanism behind P5.
One small wording point. Line 11 is the module-level declaration, not a set inside `check()`. The substance of the premise is exactly right; only the phrase "set only inside check()" reaches one line further than it should.

**P14. FOUND WITH A DIFFERENCE.** Two of the four counts are right and one is wrong, so the total is wrong.
- `rigs/rig 1 - arguments/`: 36 `.pl` files at the top level. Correct. Four further `.pl` files sit in subfolders, but they are rule files and a bridge, not ledgers.
- `results/45 Reruns by the orchestrator/`: 8. Correct.
- `results/L69 Return .../rigs/rig 1 - arguments/`: 23, P01 to P18, with exactly five correction-1 files, for P01, P03, P07, P10 and P14. Correct in every particular.
- `results/L72 Return - Astra Ultra/rigs/rig 1 - arguments/`: **9, not 8.** The files are ledger_A, T05B, T05D, T07B, T07D, T10B, T10D, T11B and T11D.
The difference is `ledger_A.pl`, which is byte-identical to `rigs/rig 1 - arguments/ledger_A.pl`. The plan has probably dropped it as a duplicate, but it does not say so. The stated total of **75 should be 76**, or the plan should say that Ultra's copy of ledger A is not run a second time.

---

## Part 2. Expectations

**A1 regression. UNMARKABLE as written, and it rests on a premise with a difference.**
- (d) It rests on P14, which is wrong about the count. "All 75 ledgers" does not name a set anyone can assemble. It is 76 files, or 75 if Ultra's duplicate ledger A is dropped, and the plan does not say which.
- (b) It cannot be marked at all today. The instrument is "a normalising script kept with the results", and no such script exists or is specified. Worse, three of the plan's own changes are exactly the kind of thing A1's "against" cell catches. D5 deletes the NO FAULT FOUND line, which is an old finding going missing. D6 rewrites the heading of T07-D's contradiction, which is a verdict word changing. D7 relabels the gauge line. A1 says additions must be of the kinds D2 to D8 list, but it says nothing about removals and rewordings, which D5, D6 and D7 require. So A1 will fire against changes the plan itself orders.
- (a) Otherwise the bracketing is sound: a missing finding and an unlisted addition are both named.
- (e) The layer is right.
- Fix: "Checked by the normaliser `L79_normalise.py`, written and frozen with this plan, which exempts the NO FAULT FOUND line (D5), the told-world heading (D6) and the gauge relabel (D7), and runs on the 76 ledger files listed in P14."

**A2 sentences. MARKABLE, but the count is wrong and one named report has no premise.**
- (c) It names P07, and no premise covers P07 at all. It also does not say whether "P01" and "P14" mean the base reports or the correction-1 reports that P8 and P6 actually pin.
- The count is wrong. Across P01, P07, P09, P14 and P16 there are eight such findings, not seven: two NO CONNECTION in P01, two in P07, two JUMP in P09, one JUMP in P14, one CANNOT TELL in P16. It is eight whether you take the base reports or the correction-1 ones.
- (a) The bracketing is good. A finding without a line and a sentence number not in the ledger are both named.
- (b) Markable. I checked that every claim line named carries a `sentence` field, so the prediction can be met.
- (e) The layer is right, and splitting it between the rig and the translator's field is well judged.
- Fix: "On the reports for P01 correction 1, P07, P09, P14 correction 1 and P16, each of the eight JUMP, NO CONNECTION and CANNOT TELL findings ...", with a new premise pinning P07's report at its hash.

**A3 the tie. MARKABLE, but only half bracketed.**
- (b) and (c) are sound. I confirmed line h of `ledger_P14_correction1.json` is marked "filled in", so "a line the writer did not write" is a fact the ledger carries and the prediction can be met.
- (a) The "against" cell brackets only two of the four things predicted. It catches a verdict change and h going unnamed. It does not catch g failing to be named as set aside, h's own verdict being printed as anything other than JUMP, or h being named without the not-written note. A build that named h but called it FOLLOWS would pass A3 as written.
- (e) The layer is right.
- Fix: add to the "against" cell "or g not named as set aside, or h's verdict printed as anything but JUMP, or h named without the not-written note".

**A4 worlds in consequences. UNMARKABLE on two of its three parts.**
- (c) "and on mine" names an instance no premise establishes, and names it wrongly. The repo's own `ledger_T07B.json` puts its told line in a case called **`Nora's story`**, not `nora_story`. I ran the old driver on it and the report reads "INSIDE 'Nora's story' (a told world, looked at alone)". A marker reading A4 literally would mark a correct build against.
- (c) "the old ten" on ledger A is pinned by nothing. P9 is a checker report and says nothing about derived facts. I ran `consequences.py` on ledger A and it does derive ten, matching `results/L65 Consequences prototype - the tomato ledger/output_A.txt` (hash 1d8028f13dd7f225). Exactly two facts appear under both `depends` and `depends_on`, so the merge gives eight, not "10 or fewer".
- (a) The "against" cell does not bracket the main positive prediction. If the world section simply fails to appear, neither "contradiction(open(door)) anywhere in an actual section" nor "ledger A's list changed" catches it.
- (b) I confirmed the prediction is reachable on both ledgers: with the world lines held back, the actual section of each loses its contradiction.
- (e) Partly off. The premise P13 shows the cause is that `consequences.py` never sets the world, so a miss could equally be D1's new interface. Charging "the tool change" alone would send the reader to the wrong file.
- Fix: "a section for the ledger's own case name (`nora_story` on Ultra's, `Nora's story` on mine) with the story's facts and no contradiction", add a premise pinning `output_A.txt` at 1d8028f13dd7f225 and its ten derived facts, say "exactly eight after the merge", and add to the "against" cell "or a world section missing, or a contradiction inside a world section".

**A5 inside worlds. UNBRACKETED on its two main predictions, and one clause cannot fail.**
- (a) This is the worst of the bracketing problems. The heart of A5 is that T10-D gains a JUMP inside `account_world` and T11-B gains a NO CONNECTION inside `inspector_world`. Neither miss lands in the "against" cell. The four things listed there are a world finding leaking into the actual ledger, T07-B gaining a finding, T07-D's contradiction moving, and a nonzero outside-line count. A build that printed no world findings at all would pass A5.
- (b) "Outside-line counts: 0 on all four" cannot fail. All four cases are told, and for a told case line 313 of the driver removes every line outside the case, so no finding inside a world can need an outside line. The count is 0 by construction. It marks, but it tests nothing.
- (b) The T11-B prediction depends on a choice D2 does not make. NO CONNECTION comes from check 2b, which the code labels "check 2b (PATCH 6)". D2 says "checks 1 to 5, patches 8 to 11, 13, 14" and names neither 2b nor PATCH 6. Read strictly, check 2b does not run inside cases and T11-B gains nothing.
- (c) The T11-B half of "the actual-ledger findings are as before" leans on the DENIED BECAUSE block at lines 5 and 6, which P2 does not quote.
- (e) The layer is right, and trap 3 reads it correctly.
- Fix: add to the "against" cell "or the T10-D JUMP or the T11-B NO CONNECTION not appearing inside its world", and drop the outside-line clause or redefine it as findings that vanish when the actual ledger's general lines are restored.

**A6 F15 and F09. MARKABLE, but one predicted absence is unbracketed.**
- (b) and (c) are sound, and I checked both ledgers. `ledger_N18A.pl` carries `claim_because(3, opening_happened, fleaming_happened)` and `denied_because(4, ...)` on the same effect and cause, so D8 must fire and "its claim line" is line 3. `ledger_N18B.pl` has no `claim_because` at all, so D8 cannot fire. `ledger_N25A.pl` has no `claim_because` either, so `results_tied_to` returns nothing and "its fact is tied to nothing" is exactly right.
- (a) Two gaps. "N25-A gaining no tie block" has no matching entry in the "against" cell, even though the Charges column anticipates it with "D3 if N25-A gains a block". And a build that flagged N18-A while naming the wrong lines would pass.
- (e) The layer is right, and splitting D8 from D3 is well judged.
- Fix: add to the "against" cell "or a tie block on N25-A; or N18-A flagged without naming both line 3 and line 4".

**A7 the outcomes block and the gauge. UNMARKABLE. It names an instance that gives the opposite answer.**
- (c) "T05-B" does not say whose. There are two, and they disagree. Ultra's `ledger_T05B.json` has every sentence either lined or binned, so it reads 0 as A7 predicts. The repo's own `ledger_T05B.json` has three sentences, lines only on sentences 2 and 3, and a single free-text leftover entry carrying no sentence number. It reads **1**, not 0, under any mechanical rule. So on the repo's own T05-B, A7 predicts the opposite of what will happen. No premise pins either file.
- (b) It depends on a choice D5 does not make. A7 needs the outcomes block to appear inside `account_world` as well as for the actual ledger, and to name check 2 even though the actual ledger has no BECAUSE line at all. D5 says neither.
- (b) It quotes an exact string, "1 sentence reached neither a line nor the bin", that D7 does not specify. A correct build that worded the count differently would be marked against.
- (a) One side only. "T10-B reading 0" is named, but T10-B reading 2 is not, and a block that names a check wrongly rather than missing it is not caught.
- (e) On the repo's own T05-B the charged layer would be wrong. The miss would come from that ledger having no structured bin, which is the translator's format, not the rig.
- I confirmed the two safe numbers: the repo's own T10-B reads 1 (sentence 3 is unreached), and ledger A reads 0, in both copies.
- Fix: "on Ultra's T05-B and on ledger A it prints 0", plus a premise pinning Ultra's `ledger_T05B.json` at its hash, and D7 must say whether the count reads the structured `bin` or the free-text `leftover`.

**A8 time. UNBRACKETED.**
- (a) The prediction is "under 30 minutes" and the miss is "over 60 minutes". Everything between 30 and 60 minutes lands nowhere. A run of 45 minutes neither confirms nor disconfirms.
- (c) "This machine" is not named, so a second marker cannot reproduce it.
- (b) It also looks close to vacuous. I timed the old driver on nine ledgers: 0.8 to 2.6 seconds each, about 1.5 seconds on average. Even if D2 multiplies the work per case, the whole run of 76 ledgers, old and new, should finish in minutes. A 30-minute ceiling will pass whatever D2 costs.
- (e) The layer is right.
- Fix: "Over 30 minutes", and name the machine in the plan; or set the ceiling from a timed baseline of the old rig recorded as a premise.

---

## Part 3. The build spec

**D1. Too loose, and the looseness changes A5.** "The world a query runs in is an argument of `run_query`, required" fixes the signature but not the rest of the call graph. `smallest_set` at lines 53 to 60 calls `run_query` itself and today inherits the world through the global. It is called from inside the case loop at line 318. A builder who changes only `run_query` and `check`'s `ask` helper leaves `smallest_set` running against the full ledger. Its "needed" set would then pick up lines from outside the case, which changes both T07-D's listed lines and the outside-line count that A5 predicts as 0. The spec must say that `smallest_set`, and every helper that reaches `run_query`, takes and forwards the world. It should also say what `consequences_2.py` passes when it wants the whole ledger, since that is now a required argument.

**D2. The loosest item in the spec, and it decides A5 twice.**
- The list of checks is incomplete. The code labels its sections "check 1", "check 2", "check 2b (PATCH 6)", "check 3", "check 4", "check 5", then patches 7 to 14. D2 says "checks 1 to 5, patches 8 to 11, 13, 14". Check 2b is neither "1 to 5" on a strict reading nor among the patches named, and PATCH 7, the chain, is missing too. A5's T11-B prediction is a NO CONNECTION, which only check 2b produces. Two builders will read this two ways and A5 will come out differently. D2 must name check 2b explicitly, and say whether the chain block prints inside a case.
- "Needs a line from outside the case" has no meaning as the driver stands. For a told case line 313 removes every outside line, so a finding cannot use one and the count is always 0. If what is wanted is the false-alarm count the give-up line describes, the spec has to say how it is computed: run the case alone, then run it again with the actual ledger's general lines available, and count the findings that disappear. As written, the count is 0 on every told world and the diagnostic does nothing.

**D3. Tight enough on the main path, loose at the edges.** The 38 line 113 reference is correct; that line does promise a note wherever a finding leans on a line the writer did not write. Two gaps. First, the list of verdicts, "FOLLOWS, JUMP, CIRCLE, IDLE, or not reached", does not match what check 2 can produce. IDLE is not a verdict but a note printed under FOLLOWS at line 109, and "FOLLOWS ONLY IF THE CAUSE IS GRANTED" at line 125 is a real verdict the list omits. Second, `results_tied_to` at lines 276 to 281 returns set-aside lines without recording which BECAUSE tied each one, and the spec does not say what to print when two BECAUSE lines tie the same line. Neither gap changes A3, whose only case is a clean JUMP, but neither would two builders write the same code.

**D4. Not tight enough, and the JUMP case is the worst of it.** "JUMP lists the claim line, the cause's lines and the effect's direct lines" leaves three choices open. What "the cause's lines" means is not fixed: the BECAUSE branch builds that set at line 103 from every route to the cause, while the SINCE branch at line 147 filters to routes of two lines or fewer, so a builder reusing either would list a different set. When the cause has no support at all, which is the common JUMP, that set is empty and the spec does not say whether to print the cause with no line or omit the heading. And the abduced candidates printed under "A single line that would close the jump" are facts with no line id, so a builder told that every finding names a line in the fixed form may try to give them one. The plan's give-up line admits a JUMP "may over-name" but sets no bound. This does not change A2, which only asks for the claim line, but it does change what A1's normaliser sees.

**D5. Silent on the two things A7 needs.** "For each check" does not say which checks, and the driver has six numbered checks and nine patches. More important, the spec never says the block is printed inside a case as well as for the actual ledger, and never says that a check with no lines at all is still named. A7 needs both: it asks the block to say BECAUSE claims were not asked in Ultra's T10-D actual ledger, which has no such line, and were asked inside `account_world`. A builder who prints one block for the actual ledger, listing only the checks that ran, satisfies D5 as written and fails A7. There is a third gap: the header only appears today when nothing was found, so "replaced" could mean the block appears only on clean ledgers or on every ledger, and the two readings give different reports on most of the 76.

**D6. Tight in intent, silent on wording.** The bug is real and sits at line 324, which uses supposition wording unconditionally while the no-contradiction branch at line 320 already switches on `told`. But D6 does not give the replacement wording, and the supposition language runs through three separate places: the heading, the clause "which arises only once the supposed lines are added", and the verdict "THE SUPPOSITION UNDOES ITSELF: every line needed comes from the supposition or from usual-case lines". All three fire on T07-D. D6 says only "a contradiction ... is printed with told-world wording". Two builders will change different subsets, and A1's normaliser has to know which text is expected.

**D7. The gauge counts are not computable as specified on half the ledgers.** The spec says "distinct sentences with a bin entry" and "sentences that reached neither a line nor the bin", but the two ledger families store this differently. Ultra's JSON files carry a structured `bin` array whose entries have a `sentence` field, including a non-numeric value "question". The repo's own ledgers have no `bin` key at all, only a free-text `leftover` list whose entries carry no sentence number. On the repo's own T05-B the single leftover entry is about sentence 1 but says so only in prose. So a builder reading `bin` gets 1 for that ledger and a builder who parses prose gets 0, and that is precisely the number A7 predicts. The spec must name the field. It should also say whether "question" counts as a sentence, what shape "filled-in lines against said" takes, and what the second count's sentence is, since A7 quotes an exact string D7 never fixes.

**D8. The tightest of the eight, with one interaction left open.** The trigger is unambiguous on the ledger in hand, and I confirmed N18-A matches on both effect and cause while N18-B has no BECAUSE claim. Three small things. The spec should say `claim_because` rather than "a BECAUSE claim", because a builder who read SINCE claims in would flag T11-B, which has a `claim_since` and a `denied_because` on the same pair, and that would trip A1. It should say whether "naming both lines" uses D4's fixed form. And it should say what happens to the existing "Fine. Nothing in the ledger makes ... produce ..." text at line 308, which N18-A prints today: leaving it beside the new flag makes the report say both that the denial is fine and that the writer claims and denies the same cause, and removing it is an old finding going missing under A1.

---

## Verdict

**DO NOT FREEZE YET.**

What must change first:

1. P14's counts. Ultra's rig-1 folder holds 9 `.pl` files, not 8, and the total is 76, not 75. Either correct both numbers or say that Ultra's duplicate `ledger_A.pl` is not run again.
2. A1's instrument. Write and freeze the normalising script with the plan, and say in A1 that it exempts the NO FAULT FOUND line (D5), the told-world heading (D6) and the gauge relabel (D7). Until then A1 fires against the plan's own changes and cannot be marked.
3. A2's count. There are eight such findings, not seven. Say which version of P01 and P14 is meant, and add a premise pinning P07's report at its hash.
4. A3's bracket. Add "or g not named as set aside, or h's verdict printed as anything but JUMP, or h named without the not-written note".
5. A4's instance. The repo's own T07-B case is named `Nora's story`, not `nora_story`. Name both spellings.
6. A4's baseline. Add a premise pinning `results/L65 Consequences prototype - the tomato ledger/output_A.txt` at 1d8028f13dd7f225 with its ten derived facts, and say "exactly eight after the merge" rather than "10 or fewer".
7. A4's bracket. Add "or a world section missing, or a contradiction inside a world section".
8. A5's bracket. Add "or the T10-D JUMP or the T11-B NO CONNECTION not appearing inside its world". Without it the expectation passes on a build that prints no world findings at all.
9. A5's outside-line clause. It is 0 by construction on every told world. Drop it, or redefine it as findings that vanish when the actual ledger's general lines are restored, and say so in D2.
10. A6's bracket. Add "or a tie block on N25-A; or N18-A flagged without naming both line 3 and line 4".
11. A7's instance. Say Ultra's T05-B, which reads 0. The repo's own T05-B reads 1 and would mark a correct build against. Add a premise pinning whichever file is meant.
12. A8's bracket. Change "Over 60 minutes" to "Over 30 minutes" and name the machine. As it stands a 45-minute run marks nothing, and the 30-minute ceiling is far above the few minutes the run actually needs.
13. D2 must name check 2b (PATCH 6) in its list, or A5's T11-B prediction rests on a reading the spec does not compel. It must also say whether the chain block prints inside a case.
14. D2 must define "needs a line from outside the case", since the told-world branch removes those lines before any finding can use them.
15. D1 must say that `smallest_set`, and every helper reaching `run_query`, takes and forwards the world. Otherwise A5's line list and outside-line count change silently.
16. D5 must say that the outcomes block is printed inside each case as well as for the actual ledger, and that it names checks with no lines at all. A7 is unmarkable without both.
17. D7 must say whether the counts read the structured `bin` or the free-text `leftover`, and must fix the wording A7 quotes.
18. D4 must fix what "the cause's lines" means for a JUMP, and what to print when the cause has no support. D6 must give the replacement wording for all three supposition phrases. D8 should say `claim_because`, and say what becomes of the "Fine." text on N18-A.
