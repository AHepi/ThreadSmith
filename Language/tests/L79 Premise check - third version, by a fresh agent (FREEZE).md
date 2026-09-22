# PREMISE CHECK - L79 Test plan, Arm A, third version

Checked against the working tree at /home/user/ThreadSmith. Nothing in the repository was modified; `git status` is clean. Both hashes in the covering note are right this time: the plan is 2e97300690dc39f7 and `tools/L79_normalise.py` is ca62f449cef91a3b.

All seventeen premises are FOUND. All eight expectations are markable and bracketed. The instrument now does what A1 says it does, and I confirmed that by running it rather than by reading it.

---

## Part 1. Premises

**P1. FOUND.** Hash 1e8b31f213443ff9. Lines 3 and 5 match character for character. `because` is absent from the report; the ledger has a line named `because`.

**P2. FOUND.** Hash f084b71881f81781. Lines 3, 5, 6 and 8 all match character for character. `since` is absent; the ledger has a line named `since`.

**P3. FOUND.** Hash ddd1088f0f4be5fa. Lines 3 and 5 match. My `ledger_T07B.json` names its case `Nora's story`.

**P4. FOUND.** Hash 0927cc618307b822. Line 3 matches. All three lines carry `case_kind: told`.

**P5. FOUND.** Hash ac5ae5a397592101. Line 4 matches including its two leading spaces.

**P6. FOUND.** Hash 3be0a3dc9517e8ca. Lines 4, 8 and 9 match. Line h of `ledger_P14_correction1.json` is marked `filled in`.

**P7. FOUND.** Hashes 0a56e3233352b4bc and ae011f2f69614182. Line 7 of each matches; neither holds a `Set aside` line.

**P8. FOUND.** The count is now right and the fifth file is correctly folded in. All five hashes match. NO CONNECTION at lines 4 and 8 in P01 correction 1 and again in P07 correction 1; JUMP at lines 4 and 7 in P09; JUMP at line 4 in P14 correction 1; CANNOT TELL at line 6 in P16. I counted the findings in the five files: 2, 2, 2, 1, 1, which is eight, exactly as the premise now breaks it down. None of the five contains a line beginning `  - line`, P14 correction 1 included.

**P9. FOUND.** Hash 4d83b8c3f3dc34be. Lines 3 and 5 match; line 28 begins with the quoted text.

**P10. FOUND.** I re-ran the old driver on `ledger_T10B.pl` for this version and it printed the gauge line word for word. Both ledgers are as described, including my T05-B's three sentences, lines on 2 and 3, one free-text `leftover` and no `bin`.

**P11. FOUND.** Hashes f4d5c39567c12d03 and f5e4747a450c43b3. All six line quotations match; the ledger facts about `claim_because` and `denied_because` hold.

**P12. FOUND.** Hashes 7f4e387a1915f9b3 and 2b41d3d1a965f2eb. All four line quotations match; N25-A's ledger has no `claim_because`.

**P13. FOUND.** Both hashes match. `WORLD_REMOVED` is declared at line 11, read at line 16, assigned at 69, 313 and 327; `check()` opens at line 62 and the premise's span of 62 to 336 is right. Line 41 of `consequences.py` is the call as quoted.

**P14. FOUND.** 36, 8, 23, 9. That is 76. The two copies of `ledger_A.pl` are byte-identical, so the instruction that the duplicate is run twice and must agree with itself is a real check, and A1's "against" cell carries it.

**P15. FOUND.** Hash 1d8028f13dd7f225. Ten derived facts, exactly two of them twinned across `depends` and `depends_on`, and they are the two named.

**P16. FOUND.** All five ledger hashes match. No line in any of the five carries ALWAYS or USUALLY anywhere, let alone outside a case; all five carry a structured `bin`; Ultra's T05B has lines on sentences 1, 2 and 3.

**P17. FOUND.** I ran both halves myself.
- `tests/L79 Normaliser mocks/run_mock_suite.sh` printed `ok` on all 22 pairs and `wrong: 0`, exit 0. That is HOLDS on the five hand-built new-form reports and on the three lacking one D7 gauge line, and FAILS on all fourteen negatives, exactly as the premise states.
- All 40 old reports compared with themselves printed "A1 HOLDS".
- I also checked that the suite tests what I tested: all 28 mock files in the repository are byte-identical to the ones I built in the second check.

---

## The instrument

My three edits are applied verbatim; I diffed the shipped file against my tested copy and the only difference is the coordinator's own addition. That addition is sound, and I checked it rather than taking it on trust.

The new line makes a WORLD finding carry the contradiction's fact. I ran it over every world heading in the 40 reports: six headings, and it gets all six right. T07-D yields `open(door,described_moment)` and N25-B yields `moved(box)`; the four no-contradiction headings yield an empty fact, because the match is case-sensitive and `no contradiction` never matches `CONTRADICTION about`. I then pushed it on constructed headings: with and without a trailing period, with nested parentheses in the fact, and on `no new contradiction` followed by the trailing sentence the old driver prints. It behaves correctly in each. Most important, the told wording and the supposition wording of the same contradiction still reduce to the same tuple, so D6's rewording does not make A1 fire, while a changed fact now does. `T07D_new_wrongfact` fails, as intended, and this closes the last gap I reported: A5's "naming other lines" and "contradiction moved" now both have an instrument.

---

## Part 2. Expectations

**A1 regression. MARKABLE AND BRACKETED.** The instrument now matches the claim. I verified by running that it catches a changed verdict word, a changed head line id, a changed described line id, a dropped described line, a deleted prose line, a deleted not-written note, changed gauge marks, an unlisted addition, a new finding outside a world, a dropped finding, text after the gauge on both a world-bearing and a world-free ledger, and a changed world fact. It correctly passes the exempted removals and every listed addition, on five new-form reports built from the D2 to D7 wordings. It rests on P17, which is FOUND.

**A2 sentences. MARKABLE AND BRACKETED.** "The five reports of P8" and "each of the eight" now agree with each other and with the files: 2 + 2 + 2 + 1 + 1. I confirmed every claim line named carries a `sentence` field, so the prediction is reachable, and D4 fixes the block names `Claim line:` and `Plan line:` that A2 asks for.

**A3 the tie. MARKABLE AND BRACKETED.** Unchanged from the second version and sound. The P14 mock with D3's exact wording passes the normaliser, so A1 and A3 agree on that ledger.

**A4 worlds in consequences. MARKABLE AND BRACKETED.** Both case names are right, the ledger A baseline is pinned by P15 at exactly eight, and a missing world section counts against. The Charges column names D1 as the alternative layer, which P13 supports.

**A5 inside worlds. MARKABLE AND BRACKETED.** Both positive predictions are bracketed, and the outside count is honestly framed with P16 behind it. I traced both predictions through the old driver's logic again and both follow. One point worth recording: check 1 already ran inside cases under PATCH 12, so D2 does not change whether a world shows a contradiction; it only adds the other checks beneath. That is why T07-B's world can be required to stay finding-free while T10-D and T11-B gain findings under headings that still read "no contradiction".

**A6 F15 and F09. MARKABLE AND BRACKETED.** Unchanged and sound; the N18-A mock with D8's exact wording passes.

**A7 outcomes and gauge. MARKABLE AND BRACKETED.** The four counts are right, and the T10-D outcomes prediction is mechanically supported by the `existence_error(scasp_predicate, ...)` message, which D5 now quotes. See the note below on what A7 does *not* cover.

**A8 time. MARKABLE AND BRACKETED.** The figures now match what I measured: SWI-Prolog 9.0.4, s(CASP) 1.1.4, 0.8 to 4.4 s per ledger, 100 s for all 76. Under 10 minutes against over 10 minutes, with no dead band and ample headroom.

---

## Part 3. The build spec

D1 through D8 are now tight enough that two builders would build the same thing, with three residual points. **None of them changes the outcome of A1 to A8**, and I tested that rather than assuming it.

**1. D5 lists four permitted line forms and then requires a fifth.** The sentence fixing the block says each line is `asked, nothing found`, `asked, N found`, `not asked, no line of that kind` or `ran out of time`. The new sentence then requires `not asked, nothing to ask` for the chain, two usually lines, added lines and what-ifs. A builder reading the first sentence literally has no form to print for those four. I built a report using the fifth form and A1 still holds, because the normaliser absorbs every indented line after `OUTCOMES:` whatever it says, so no expectation moves. This is the one I would fold in: add `not asked, nothing to ask` to D5's list of forms, so a builder is not told they built it wrong.

**2. Three of D7's four counts are named by no expectation.** This is the direct answer to the question in the covering note. HOLDS on the three `*_nofix` mocks is right, and it is what I meant: A1 is a regression test, and a missing gauge count is neither an old finding lost nor an unlisted addition. But the stated reason, that a missing count is A7's business, holds for only one of the four. A7 names `sentences with no line` and nothing else. I built a report dropping `bin sentences`, `sentences with no line and no bin entry` and `filled in against said` and A1 holds; I then dropped all four and A1 still holds, with only the fourth being caught, by A7. So the line the `*_nofix` mocks drop is A7's business under no reading of A7, and a build could omit three of D7's four counts and pass every expectation. If you want each change to have an expectation that could fire, one clause on one ledger covers it: on Ultra's T10-D the three read `bin sentences: 1`, `sentences with no line and no bin entry: 0` and `filled in against said: 0/6`, and on my T10-B the first and third read `not recorded (free-text bin)` and `not recorded`. I computed all of those from the ledgers.

**3. Two of D5's "input is empty" tests are approximate.** For the chain, "no SINCE claim" is exactly right, since the chain is built from what check 2b accumulates. For added lines, "no conclusion line" stands for the real test, which is that patch 10 loops over both BECAUSE and SINCE claims. For two usually lines, "no USUALLY line" stands for patch 8, which opens on `holds(F)` and needs unstated assumptions on both sides. The proxies are reasonable and no ledger in hand turns on the difference, but a builder implementing them literally would write a slightly different test.

**A caveat on the mocks, not a fault.** The five new-form mocks were built against the second version's D5, so their `the chain`, `two usually lines`, `added lines` and `what-ifs` lines use the older wording. No suite verdict changes, because the normaliser absorbs the block wholesale, and I confirmed that. But the mocks are a specimen of the instrument's behaviour, not of D5's exact text, and P17 is right to describe them as the instrument's test rather than as model reports.

---

## Verdict

**FREEZE.**

Every premise is FOUND at its hash, with every quotation exact to the character. Every expectation is markable, bracketed on both sides, correctly instanced, and charged to the layer that would have moved. The instrument is frozen with the plan, its mock suite passes 22 of 22 under my own run, the 40 self-comparisons hold, and the one edit I had not tested has now been checked against every world heading in the corpus and against constructed edge cases.

Three things are worth folding in if the file is being touched anyway. None voids a premise, unbrackets an expectation, or changes a mark, and I verified each of those claims by running the instrument:

1. Add `not asked, nothing to ask` to D5's list of permitted line forms, so D5 stops contradicting itself.
2. Extend A7 by one clause to name D7's other three counts on one ledger each, or accept in writing that three of D7's four counts ship untested. The values are given above.
3. Optionally tighten D5's "input is empty" wording for added lines and two usually lines to match what those patches actually loop over.

If the plan is frozen as it stands, item 1 is the only one that could cause a builder dispute, and it is a dispute about wording rather than about any mark.
