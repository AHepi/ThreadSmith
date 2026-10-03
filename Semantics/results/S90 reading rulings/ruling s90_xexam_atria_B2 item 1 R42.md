# Ruling: R42 (W17.2), contested by Atria's reply to part B2

*Fresh Claude checker. It did not draft, assemble or check the change list, and did not write the part briefs. Read under the S90 rule (rules 2, 3, 7, 8), the S90 Parts rule (rules 1–3) and the rerun note (item 4: the pass-2 reply stands where pass 1's would have).*

*File name.* The name the task gave, "ruling s90_xexam_atria_B2 (part B2, Atria). Pass 2, accepted on attempt 4 of 4: … 1,375 words. item 1 R42.md", is 304 bytes, and the filesystem refuses it ("File name too long"). This file uses the short form of the other rulings in this folder.

**The reply.** `results/S90 Cross-examination - revision 2 draft - returns/parts/s90_xexam_atria_B2.response.txt`. Pass 2, sha256 f965836a9b2f… (equal to the receipt's `response_sha256`), finish stop, 0 bad chunks, 1,375 words by `wc -w`, END OF REPORT on its last line. The receipt's history gives attempts 1–3 status 0 and attempt 4 status 200.

**Why it is contested.** The reply's line is `R42: STANDS`, but its point 1 names moved verdicts on R42 (O24 and N5). Under S90 rule 2 and Parts rule 2, that makes the change contested whatever line the reply gives.

## 1. The entry

- **Entry.** W17.2, R42 (= R2-42; C37 in the first S90 brief). Group B2, item W17. File-11 line 473, revised-text line 475. Part XII, "Selection in the physical module", sentence 1.
- **OLD:** `a population of realized transports`
- **NEW:** `a population of candidate transports`
- **KIND:** CLAIM. **REASON WORD:** clarification.
- **DECLARATION:** "Part XII now describes the population of a selection history as candidate transports, as Part IV does, not realized ones. The population is the set its own last sentence gives: the transports the physics and the stated construction admit."
- **CHECK (the checkers' verdict):** "check 1, FIX. "Realizable" alone suggests physics alone, the reading under which O48's wired arrangement is a member. NEW uses L197's word, "candidate", and the paragraph's last sentence stays the one wording of membership." The list's table "What the checks changed" records the same fix: "W17.2 | 473 | 1 | "candidate transports", not "realizable transports"". Check 2 left no note on the entry.
- **CASES AT RISK (the drafters' expectation):**
  - O48 stays AGREE.
  - O24 stays AGREE: "The second arrangement need not have been realized to be a member".
  - N5 (O57) "stays AGREE, or moves toward it". The entry points to conflict 1, because the plan's P2(d) predicts no change on O57.
  - D3-T is unaffected.
  - O11 is not reached.
- **Earlier rulings.** There are none.
  - Neither `S90 Reading of the replies - batch 1 (Mimo A1, Mimo A2, Atria B1).md` nor `… batch 2 (Atria A2, Mimo B1).md` names R42 or W17.2.
  - The single Atria call on the first S90 brief (C37) failed, so it supports nothing (S90 rule 4).
  - Mimo's reply to B2 gives `R42: STANDS` and does not contest the change. The reading of Mimo B2 on R52 (item 2) cites R42's declaration as the place where "realized" gives way to "admitted".
- **A housekeeping note, not part of the ruling.** The entry's heading still reads "L473 s1: the population is of realizable transports". That is the drafter's wording from before check 1's fix. OLD, NEW, the declaration and the fixes table all say "candidate". The heading does not appear in the revision note's R2-42 row or in the B2 brief's layer-1 label ("Part XII, Selection in the physical module"), so nothing in the record or the draft is wrong. The heading can be brought into line when the KEEP is written into CHECK.

## 2. The reply's argument

Point 1, quoted whole on R42:

> "**1. R42 (c, d) — the one change that moves a verdict, and it moves it toward the fixed verdict.** Part XII, line 475, now reads "a population of **candidate** transports", and its own next sentence already said: "The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it." Part IV independently says "There is a population \(\mathcal T\) of **candidate** transports". So the current text's "realized transports" contradicted both Part IV and Part XII's own last sentence, leaving the population's membership split. This matters for **O24**: the differing arrangement is "reachable by hand" but never used, so on the "realized" reading it is outside the population, Derivation 3's condition fails, and the record would have *settled* the question — against the fixed verdict ("the record has not chosen between them"). On the candidate reading the arrangement is in the population, survives on \(H\), and the record has not chosen. The same bears on **N5**: the months-reading and the seasons-reading coincide on the village's history, so as candidates both survive on \(H\) and the rule "cannot tell him which reading to trust"; on a realized-only reading they are not separately realizable and the population would fix one. Both moves are toward the fixed verdicts, and the declaration states exactly the change ("candidate transports, as Part IV does, not realized ones") that produces them. R42 also repairs an internal contradiction in the current text."

The closing lines are `R42: STANDS` and `OVERALL: SOUND`. The reply names no undeclared change and no move away.

## 3. The texts, and the quotations checked (S90 rule 8)

- **Revised L475 (Part XII)** reads: "a population of candidate transports, a physically admitted variation operator, and a survival condition enacted by the environment. … The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it." The quotation is found as given.
- **File 11 L473** is the same paragraph with "a population of realized transports". The last sentence is byte-identical in both texts.
- **Part IV.** File 11 L197 and revised L195 both read "There is a population \(\mathcal T\) of candidate transports". The quotation is found (the bold is the reply's). Revised L195 also adds R11's definition: "A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\)".
- **Derivation 3** (revised L566–570; file 11 L562–566) needs members that were never realized:
  - the proof: "Where \(\mathcal T\) contains a transport with \(L_{j}(a,b)\) altered to another admitted relation for one \((a,b)\notin H\), that transport survives on \(H\)";
  - the consequence: "wherever its population admits an alternative".

  R52's NEW (L566) now reads "a member of \(\mathcal T\), a transport the physics and the stated construction admit (Part XII)", which points to L475's last sentence.
- **The other places that speak of the population** (revised L53, L155, L195, L223, L225, L536 and L620) say nothing about realization. After the change, no sentence of the revised text describes the population as realized, so Parts IV, XII and XVI give one notion of membership.
- **"Contradiction" or "tension".** The reply calls the old L473 a contradiction. The change list calls it the tension that 03 §8 item 1 records. Either way, the entry closes it. An admitted transport need not have been realized, so file 11's first sentence and its last sentence gave the population two different extents.
- **O24's quotation.** "the record has not chosen between them" is in O24's verdict. But the case says "reachable by hand" of **the setting** ("The setting is reachable by hand"), not of the arrangement. The situation does not say whether the second arrangement was ever built. So the reply's claim, that on the "realized" reading the arrangement is outside the population, holds only if that arrangement was never built, which the case leaves open. The point is ruled on what the texts say (section 4).
- **N5's quotation.** "cannot tell him which reading to trust" is found in N5's verdict ("The rule itself cannot tell him which reading to trust"). The reply's "coincide on the village's history" matches the verdict's "At home, "after the first autumn rains" and "in October" were one instruction".

## 4. The cases worked

- **O24** (S81 book).
  - S81's determination (04, row O24) ruled file 11 AGREE, resting on L558 and L259 s2. 03 listed O24 as a row to watch for harm "through L562's "admitted, realizable, a member of \(\mathcal T\)" or L473".
  - On the old L473, a reader could take "realized" literally and hold that the second arrangement was never built. That reader would put it outside \(\mathcal T\). Derivation 3's condition would then fail, and the last clause of its proof ("the population fixes it") would give a verdict against "the record has not chosen".
  - On the new L475, the second arrangement is a member if the physics and the stated construction admit it, which the case gives ("One reachable setting is enough").
  - So the change closes a reading that could have moved O24 away, and the ruled mark stays AGREE. That is what the entry says ("O24 stays AGREE"). The reply's "toward" describes the same fact from the side of the harmful reading. It is not a move away.
- **N5** (S89 book).
  - The months reading and the seasons reading agree in every season at home. So they are two transports that both meet fidelity on \(H\) and differ in the new land.
  - On the old wording, only one reading was ever practised. A strict "realized" reading leaves no differing survivor, and Derivation 3's proof then says the population fixes the value, against the verdict.
  - On the new wording, both readings are candidates the physics admits, and both survive on \(H\). Derivation 3 then gives underdetermination: "the rule itself cannot tell him which reading to trust".
  - N5 stays AGREE or moves toward it, as the entry records. Conflict 1 and the note on P2(d) under "Findings carried forward" already mark O57 as a row that may move toward. It is not a move away.
- **O48** (S81 book): "every device in the stated population is built without that wire".
  - L475's unchanged last sentence keeps the wired arrangement out: "a transport that would need a part every member of the population is built without is not in it". So there is no differing member, and the verdict ("The premise is not met") holds.
  - "Candidate" is Part IV's word, and it does not widen membership beyond that sentence. Check 1 chose "candidate" over "realizable" to protect this reading.
  - AGREE, unchanged.
- **D3-T** (`tests/S89 Case book - candidate case D3-T, the controller that failed the test/final.md`).
  - The case says "Only two controller designs exist; there are no others. Both can be built." Both were built, so both are members on either wording.
  - The discarded design fails the test at a setting the tester uses. So it does not survive on \(H\), and it is not a differing survivor.
  - The verdict is No on both texts. Unaffected.
- **O11** (S81 book). The apprentice at three locks, Monday to Wednesday. The case turns on blind fitting, construction and reuse, not on what belongs to a selection population. Not reached.
- **N9** (not named in the entry; checked because it uses the word "population"). There, "the population" means the moths that actually carry the wing colour. The surviving transport is realized on either wording. Only the status of the alternatives that did not survive changes, and N9's verdict does not rest on them. Not reached.

## 5. Ruling: KEEP

- **Why.**
  - The reply contests nothing in the entry. It names two moves, both toward the fixed verdicts or holding them, and the declaration states the change that produces both ("as candidate transports, as Part IV does, not realized ones").
  - The O24 quotation puts "reachable by hand" on the wrong thing: the case says it of the setting. Once that is corrected, the O24 point is conditional. It then matches the entry's "O24 stays AGREE": the change removes a reading that could have turned the row.
  - N5 stays AGREE or moves toward it, as the entry and conflict 1 already record. O48, D3-T and O11 are unchanged.
  - No fixed verdict is disputed (S90 rule 7).
  - The new wording removes the tension between the paragraph's first and last sentences, and makes Part XII agree with Part IV and with R52's pointer.
- **KIND stays CLAIM.** The set a selection claim quantifies over changes from realized alternatives to admitted ones. The entry's LOSS says so. The change also lets members that were never realized satisfy Derivation 3's hypothesis. That is a change of claim, and it is declared.
- **OLD, NEW and the DECLARATION stand as drafted.**
- **For the CHECK field:** "After the cross-examination (S90, part B2): Atria's reply (pass 2) gave STANDS and named moves on O24 and N5, both toward and both declared; kept. The reply's O24 quotation "reachable by hand" is said of the setting, not the arrangement; on the texts O24 stays AGREE, and the change closes the "realized" reading that 03 watched for harm. Mimo's reply gave STANDS and did not contest it." The entry's heading could also be brought into line with NEW ("the population is of candidate transports").
