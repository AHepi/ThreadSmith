# PREMISE CHECK - L79 Test plan, Arm A, second version

Checked against the working tree at /home/user/ThreadSmith. Nothing in the repository was modified; `git status` is clean. All runs and all patched copies of the normaliser were made under the scratchpad.

**A note on the two hashes in the brief.** They are transposed. The plan file hashes to **e152f1ce1991b189** and `tools/L79_normalise.py` to **8a32ed65df50f3d5**; the brief gave them the other way round. Both files are present and carry those two values, so this is a swap in the covering note, not a mismatch in the plan. The plan's own premises do not quote either hash, so nothing downstream rests on it. Worth correcting in the log entry that records the freeze.

Seventeen of the eighteen items from the first check are answered. Fifteen premises are FOUND, two carry a difference, and six of the eight expectations are now markable and bracketed. The remaining problem is the new instrument: it does not do what A1 says it does.

---

## Part 1. Premises

**P1. FOUND.** Hash 1e8b31f213443ff9. Line 3 and line 5 match character for character. The string `because` is absent from the report. The ledger holds a line named `because`.

**P2. FOUND.** Hash f084b71881f81781. Lines 3, 5, 6 and 8 all match character for character. This fixes the gap I raised last time: the DENIED BECAUSE block that A5 requires to stay unchanged is now quoted at lines 5 and 6, so A5 no longer leans on unpinned text. The string `since` is absent; the ledger holds a line named `since`.

**P3. FOUND.** Hash ddd1088f0f4be5fa. Lines 3 and 5 match. The added clause is right: my `ledger_T07B.json` names its case `Nora's story`.

**P4. FOUND.** Hash 0927cc618307b822. Line 3 matches. All three lines of the ledger carry `case_kind: told`.

**P5. FOUND.** Hash ac5ae5a397592101. Line 4 matches including its two leading spaces, which the second version now reproduces.

**P6. FOUND.** Hash 3be0a3dc9517e8ca. Lines 4, 8 and 9 match, including the two-space indents. Line h of `ledger_P14_correction1.json` is marked `filled in`.

**P7. FOUND.** Hashes 0a56e3233352b4bc and ae011f2f69614182. Line 7 of each matches; neither file contains a `Set aside` line.

**P8. FOUND WITH A DIFFERENCE.** All four hashes match, including the newly added `P07_correction1_OpenAI_Codex.report.txt` at f985ad3b523d47e7. Every line number is right: NO CONNECTION at lines 4 and 8 in both P01 correction 1 and P07 correction 1, JUMP at lines 4 and 7 in P09, CANNOT TELL at line 6 in P16. None of the four files contains a line beginning `  - line`.
**The count is wrong.** Those four files hold **seven** such findings, not eight: 2 + 2 + 2 + 1. The eighth finding I counted last time was P14 correction 1's JUMP, and P14 correction 1 is named by P6, not by P8. The file list was corrected by dropping P14 and adding P07 correction 1, but the number eight was carried over from my first report, where it counted five files. Either say seven, or add P14 correction 1 to P8's list and keep eight.

**P9. FOUND.** Hash 4d83b8c3f3dc34be. Lines 3 and 5 match exactly. Line 28 begins with the quoted text, and the premise now says "begins", which fixes the prefix point I raised.

**P10. FOUND.** I re-ran the old driver on `ledger_T10B.pl` and it printed the gauge line word for word. Both ledgers are as described: `ledger_T10B.json` has three sentences, lines on sentences 1, 1 and 2, an empty `leftover` and no `bin`; `ledger_T05B.json` has three sentences, lines on sentences 2 and 3, one free-text `leftover` entry and no `bin`. The added T05-B clause is the one that makes A7 markable, and it is right.

**P11. FOUND.** Hashes f4d5c39567c12d03 and f5e4747a450c43b3. Lines 4, 6 and 7 of N18-A and lines 3, 5 and 6 of N18-B match. `ledger_N18A.pl` carries `claim_because(3, opening_happened, fleaming_happened)` and `denied_because(4, ...)` on the same pair; `ledger_N18B.pl` has no `claim_because`.

**P12. FOUND.** Hashes 7f4e387a1915f9b3 and 2b41d3d1a965f2eb. Lines 3 and 7 of N25-A and lines 5 and 7 of N25-B match. `ledger_N25A.pl` has no `claim_because`, so nothing can be tied to its changed fact.

**P13. FOUND.** Both hashes match. The restatement is now exact: `WORLD_REMOVED` is declared at line 11, read at line 16, assigned at lines 69, 313 and 327, and `check()` spans lines 62 to 336, so all three assignments are inside it. Line 41 of `consequences.py` is the call as quoted, with nothing set beforehand.

**P14. FOUND.** 36 at the top level of `rigs/rig 1 - arguments/`, 8 in results 45, 23 in the L69 folder with correction 1 for exactly P01, P03, P07, P10 and P14, and 9 in the Ultra folder. That is 76. `ledger_A.pl` in the Ultra folder is byte-identical to the main copy, as stated, and the plan now says the duplicate is run twice and must agree with itself, which A1's "against" cell picks up.

**P15. FOUND.** Hash 1d8028f13dd7f225. The file prints ten derived facts. Exactly two appear under both `depends` and `depends_on`, and they are the two named. The third `depends_on` fact, about the thermometer's reading, has no `depends` twin, which is why the merge leaves eight and not nine.

**P16. FOUND.** All five ledger hashes match. I checked every line of all five: none carries ALWAYS or USUALLY anywhere, let alone outside a case, so there are no general lines to restore and D2's count must be 0 on all of them. All five carry a structured `bin`. Ultra's T05B has lines on sentences 1, 2 and 3.

**P17. FOUND WITH A DIFFERENCE.** The premise makes two claims. The second is true; the first is not.
- **True:** I ran `L79_normalise.py OLD OLD` on all 40 old reports. The set of 40 is determinate: the 23 L69 Codex reports, Ultra's 8 `checker.stdout.txt`, the 8 of results 45, and `smoke_expected_report_A.txt`. All 40 printed "A1 HOLDS" and exited 0. (The phrase "P6 to P12's files" names only twelve of them, but the total of 40 pins the set uniquely.)
- **Not true:** "compares an old report and a new one as A1 states". It does not, in three respects, set out in Part 3 below. The self-comparison is passed by construction and cannot detect any of them, because comparing a file with itself exercises no difference at all.

---

## Part 2. Expectations

**A1 regression. WILL FIRE AGAINST A CORRECT BUILD, on 66 of the 76 files.**
- (d) It rests on P17, which carries a difference.
- (b) I built a new-form report for my T10-B by hand from the D2 to D7 wordings and ran the frozen normaliser old-against-new. It printed **A1 FAILS**, on this line and nothing else: `unlisted text in new: ('text', 'sentences with no line and no bin entry: not recorded')`. That line is required by D7. Removing it alone makes the same mock pass. 66 of the 76 ledgers have no world, and on every one of them a correct build will fail A1 for this reason.
- (b) The instrument also does not compare what A1 promises. A1 says every old finding must be in the new "with the same kind, line ids, verdict word and world". On ledger A I changed a line id under the CONTRADICTION from 7 to 99, and separately dropped one of its four lines: **A1 HOLDS both times.** I deleted an old prose sentence and the "leans on lines you did not write" note: **A1 HOLDS both times.** On T07-D I changed the fact of the world contradiction and a line id beneath it: **A1 HOLDS both times.** The near-miss list requires "T07-D's two lines" and "the text of every old finding" to be unchanged, and neither is checked.
- (a) The bracketing of the row itself is sound, and adding "the two copies of ledger A disagreeing" is a good catch.
- (e) The layer is right.
- What does work, and I confirmed it: a changed verdict word, a changed head line id, a changed gauge marks prefix, an unlisted prose line, a new finding outside a world, and a dropped old finding head all produce "A1 FAILS". The D6 rewording of T07-D's heading correctly maps to the same canonical finding on both sides, so A1 holds there as intended. The exempted removals (D5's NO FAULT FOUND line) and the listed additions (D2 world findings, D2 outside count, D3 tie block and note, D4 blocks, D5 outcomes block, D7 gauge counts, D8 claim-and-deny) all pass, on mocks for T10-D, T07-D, P14 correction 1 and N18-A.
- Fix: three lines in the normaliser, all of which I wrote and tested in a scratch copy. (1) In `EXTRA_KINDS`, change the D7 pattern to `r"^\s*(?:bin sentences|sentences with no line(?: and no bin entry)?|filled in against said|bin entries):"`. (2) In the `GAUGE:` branch of `parse`, set `world = ""` before appending, so the gauge closes the world section. (3) In `compare`, also require that old extras of kind `text`, `D4 described lines` and `D3 not-written note` reappear in the new report, exempting the one string D6 replaces. With all three, the four clean mocks hold, all 40 self-comparisons still hold, and every case listed above is caught.

**A2 sentences. MARKABLE, but it inherits P8's count.** It says "each of the eight"; there are seven across P8's four reports. Everything else is sound: the bracketing catches a missing block, a missing number and a wrong number; I checked that every claim line named carries a `sentence` field, so the prediction can be met; D4 fixes the exact block names `Claim line:` and `Plan line:`, which match what A2 asks for. Fix: say seven, or add P14 correction 1 to P8.

**A3 the tie. MARKABLE AND BRACKETED.** All four of my open items are closed: g named as set aside, h's verdict pinned to JUMP, the NOTE required, and a `Set aside:` or NOTE line on P11 or P13 now counts against. I built a P14 mock with D3's exact wording and the normaliser classified the tie line and the note as listed additions, so A1 and A3 agree on this ledger. D3's verdict list is now the right one: it adds FOLLOWS ONLY IF THE CAUSE IS GRANTED and drops IDLE, which was a modifier and not a verdict.

**A4 worlds in consequences. MARKABLE AND BRACKETED.** Both instances are now named correctly, `nora_story` for Ultra's and `Nora's story` for mine, which was the error that would have marked a correct build against. The ledger A baseline is pinned by P15 and the prediction is now exactly eight rather than "10 or fewer". A missing world section and a contradiction inside a world section both count against. The Charges column now names D1 as the alternative layer, which is right: P13 shows the cause is the unset world argument.

**A5 inside worlds. MARKABLE AND BRACKETED, with one clause the instrument cannot check.**
- Both positive predictions are now bracketed: the T10-D JUMP or the T11-B NO CONNECTION going absent counts against. That was the largest hole last time.
- The outside count is now honest. P16 establishes that no general line exists outside a case on any of the four, so 0 is the right answer and the plan says so, and frames a nonzero as a bug in the count rather than as evidence. That is the right way to keep the clause.
- I traced both predictions through the old driver's logic and both follow: inside `account_world` the only route to `stayed_dry(letter)` is the line that states it, so check 2 reaches JUMP; inside `inspector_world` nothing leads from `burning(lamp)` to `returned(visitor)` once the stating line is held back, so check 2b reaches NO CONNECTION.
- The one soft spot: "T07-D's contradiction moved, missing, or naming other lines". The normaliser's world finding carries neither the fact nor the lines, so "naming other lines" has no instrument and the marker must do it by eye. Trap 2 forbids eye-marking for A1 only, so this is allowed, but fix (3) above would give A5 an instrument too.

**A6 F15 and F09. MARKABLE AND BRACKETED.** Both holes are closed: flagging N18-A while naming other lines, and a `Set aside:` line appearing on N25-A, now both count against, and losing the `Fine.` line is named too. I confirmed from the ledgers that N18-A must fire, N18-B cannot, and N25-A has nothing to tie. I built an N18-A mock with D8's exact wording and the normaliser classified the new line as a listed addition and kept the `Fine.` line as an old finding.

**A7 outcomes and gauge. MARKABLE, and all four numbers are right.** I computed them under D7's own definition: my T10-B 1, my T05-B 1, Ultra's T05-B 0, both copies of ledger A 0. Naming whose T05-B is meant was the fix that mattered, and it is made. The T10-D outcomes prediction is mechanically supported: I confirmed from a raw log that s(CASP) returns `existence_error(scasp_predicate, ...)` for `claim_because` on a ledger with no such line, and does not for rule-defined predicates such as `contradiction`, so "not asked, no line of that kind" for the actual ledger and "asked, 1 found" inside `account_world` are both reachable and distinguishable. D7's free-text fallback (`bin sentences: not recorded (free-text bin)`) removes the ambiguity that made this unmarkable last time.

**A8 time. MARKABLE AND BRACKETED, and comfortably so.** Under 10 minutes against over 10 minutes leaves no dead band, and the container is now identified. I verified the versions: SWI-Prolog 9.0.4 and s(CASP) 1.1.4, exactly as stated. I then ran the old driver over all 76 files: **100 seconds in total**, mean 1.32 s, median 1.18 s, no failures. Since only 10 of the 76 ledgers have a world, and D2 doubles the work only inside those, old and new together should finish in a few minutes. One small correction: the parenthetical "0.8 to 2.6 s per ledger as the checker timed it" quotes my nine-ledger sample from the first check; across all 76 the range is 0.8 to 4.4 s, the slowest being `ledger_H.pl`. This does not change the row, which is bracketed on total time.

---

## Part 3. The build spec

The eight items I raised are answered. D1 now names the signature and says `smallest_set` and every helper take and forward `world_removed`, and gives the default for the actual world and the complement for each case, matching lines 69 and 313 of the old driver. D2 now names checks 1, 2, 2b, 3, 4, 5, the chain and patches 8, 9, 10 and 14 explicitly, and excludes what-ifs; 2b is the one that produces NO CONNECTION, so A5's T11-B prediction no longer depends on a reading. D2 also defines the outside count as a second run with the general lines restored, which makes it computable. D3 gives the exact line, the right verdict list and the two-tie rule. D4 pins "the cause's lines" to the set check 2 already collects, and gives the empty-case wordings. D5 names twelve checks in order with exact strings and says the block appears inside each world. D6 gives the replacement wording and rules out all three supposition phrases. D7 names the fields and the free-text fallback. D8 says `claim_because` only, keeps `Fine.`, and fixes the wording.

Three things remain, none of which changes A1 to A8.

**D5's decision rule does not reach four of its twelve names.** "No line of that kind" is decided by the check's first query returning the s(CASP) missing-predicate message. That works for because claims, since claims, plans, likeness, exemptions and denied because, which I confirmed empirically. It cannot discriminate for contradictions and exceptions, whose predicates are defined in `checker_rules.pl` and so always exist; those will always read "asked, nothing found". And four names have no first query of their own: the chain is built from what check 2b accumulates, two usually lines opens on `holds(F)`, added lines re-uses check 2's query, and what-ifs are driven by the ledger's `whatifs` list and ask nothing when it is empty. Two builders would fill those four lines differently. No expectation reads them: A7 pins only the because-claims line, and A1 treats every outcomes line as a listed addition whatever it says. Worth one sentence in D5 saying what those four print when there is nothing to ask.

**D4's what-if clause is dead this round.** The head changes "when the ledger's whatifs entry carries a `line` naming a ledger line". Across all 76 ledgers there are 11 whatif entries and **none** carries a `line` key, so every what-if head stays unchanged and the clause is never exercised. Harmless, since D4 says "else unchanged", but a builder will write code no ledger reaches, and A3's P14 head will not gain a sentence number.

**D2's outside count will be exercised on two ledgers no expectation covers.** Only `ledger_H.pl` and `ledger_P18.pl` have both a world and general lines outside every case, so those are the only two where the second run can add anything and N can be nonzero. A5 covers the four Ultra ledgers, where P16 establishes N must be 0. A nonzero N on H or P18 is neither predicted nor bracketed, and the normaliser accepts the line whatever the number. That is acceptable, since N is a count and not a claim, but it means the false-alarm diagnostic D2's give-up line promises ships without any expectation testing it at a nonzero value.

---

## Verdict

**DO NOT FREEZE YET.**

Three things must change first. The first is the only substantial one.

1. **Fix the normaliser, or A1 fails on 66 of the 76 files.** Three edits, all tested in a scratch copy, all of which keep the 40 self-comparisons passing and the four new-form mocks passing:
   a. The D7 pattern in `EXTRA_KINDS` does not match D7's own third gauge line. Change it to `r"^\s*(?:bin sentences|sentences with no line(?: and no bin entry)?|filled in against said|bin entries):"`.
   b. The `GAUGE:` branch of `parse` does not close the world section, so anything indented after the gauge on a world-bearing ledger is swallowed as a world finding and never flagged. Set `world = ""` in that branch.
   c. `compare` only flags new extras of kind `text`; it never checks that old ones survived, and never compares described line ids at all. Require old extras of kind `text`, `D4 described lines` and `D3 not-written note` to reappear, exempting the one string D6 replaces. Without this, A1 cannot see a changed or dropped line id under any finding, a deleted prose sentence, or a deleted not-written note, and the near-miss list's "T07-D's two lines" and "the text of every old finding" go unchecked.
2. **P8's count and A2's count.** The four reports P8 names hold seven JUMP, NO CONNECTION and CANNOT TELL findings, not eight. Either change both numbers to seven, or add `P14_correction1_OpenAI_Codex.report.txt` to P8's list and keep eight.
3. **P17's first clause.** It says the normaliser "compares an old report and a new one as A1 states". Until item 1 is done that is not so, and the 40 self-comparisons cannot show it either way, since a file compared with itself exercises no difference. Once item 1 is done, re-run the 40 and add to P17 the four new-form mocks and the negative cases, so the premise rests on a test that could have failed.

Three smaller notes, none blocking: correct the transposed hashes in the covering note and the log entry (plan e152f1ce1991b189, normaliser 8a32ed65df50f3d5); add a sentence to D5 for the four outcome names whose check has no query of its own; and note in A8 that the per-ledger range across all 76 is 0.8 to 4.4 s, not 0.8 to 2.6 s.

Everything else is sound. Fifteen premises are FOUND at their hashes with every quotation exact to the character, and A3, A4, A5, A6, A7 and A8 are markable, bracketed on both sides, correctly instanced and charged to the layer that would have moved.
