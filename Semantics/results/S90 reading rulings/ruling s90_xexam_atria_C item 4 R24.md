# Ruling: s90_xexam_atria_C, item 4, R24 (W33.1)

*By a fresh Claude checker, 24 September 2026. The checker works under the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rules 1–3 and 5), and under the rerun note "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (ruling 4: the pass-2 reply stands where the pass-1 reply would have stood). It did not draft, assemble or check the change list, and it did not write the part briefs.*

*File name.* The task asked for "ruling s90_xexam_atria_C (part C, Atria). Pass 2, accepted on attempt 6 of 6: … 1,227 words. item 4 R24.md". That name is 287 bytes, and the filesystem refused it ("File name too long"; the limit is 255). This file uses the short form of the other rulings in this folder, as "ruling s90_xexam_atria_C item 2 R06.md" does.

*The call.* The reply is `parts/s90_xexam_atria_C.response.txt`. The task's path puts the call description where the tag belongs, and no file of that name exists.
- The receipt shows pass 2 accepted on attempt 6 of 6. Attempts 1–5 had status 0 and brought nothing back.
- Attempt 6 returned status 200 with finish "stop" and 0 bad chunks. END OF REPORT is on the last line.
- The sha256 is bd51b78593b3ac9e7d194d7f0b62e43e223f8c487d6e611a6118999d50d7a72f, recomputed here, and it equals the receipt's `response_sha256`. The reply is 1,227 words by `wc -w`.
- The `user_sha256` is a94c8ef9ead3…, which is the part C brief.
- No reasoning file and no pass-1 file was read.

*Why R24 is here.* The reply's closing line is "R24: STANDS". Its point 3, under (d), names a move of the theory's verdict on N1 that R24 causes, and says the move is toward the fixed verdict and declared. S90 Parts rule 2 counts a change as contested when a reply names a moved verdict on it, "whatever line it gives the change". The same bullet also claims an equivalence, which is checked in §3.

*Sources, each checked by md5:*
- the change list, a5c92adc9f1e3806c0f9c6394cffde1e, last touched at 587eebf;
- the revised text, `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`, 9aecf2f30ce0b4523606b2b8409fdf37;
- file 11, 5e494c1095d920d128b9a79de378f923, read only;
- the part C brief, 2183faa5005b112347f484b6c8ace196: its R24 block, its task (d) and its N1;
- the S81 book, 4f488d149e44669240d5db546c8e946a;
- the S89 candidate book, b2e535777976a511935430bd089ba500.

*Other rulings and rules.* The batch 1 and batch 2 readings have no ruling on R24, W33.1 or C20, and neither does the committed folder `S90 reading rulings/`. Mimo's reply to part C gives "R24: STANDS" with no point on R24, so only Atria contests the change. D3-T is not named by the reply or by the entry, and it is not worked here. The S87 rules (05, 05b and 05c) govern S87 rows, so they are not applied.

*The map (part-rule table):* "R24 | W33.1 | C20 | C | 315 | 313 | CLAIM | O8, O45, N1, N2". The revision note's row is "R2-24 | W33.1 | C20 | 315 | clarification | CLAIM | yes".

## 1. The entry and its checkers' history

**W33.1, "Part VI: (E) tolerates a commitment that does no work; (B) marks it".** It is applied, in group C, at file-11 line 315 (revised line 313). KIND is CLAIM and the reason word is "clarification".

**OLD:**
````text
More reach constrains variation; the containment need not be strict; counting jobs is not a warrant.
````

**NEW:**
````text
More reach constrains variation; the containment need not be strict; counting jobs is not a warrant. (E) has no condition that each commitment do work. A commitment \(d\) does no work by itself in the candidate when every support stays a support after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no support (B). When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary support). How hard an account is to vary is a separate matter, shown by \(\operatorname{Pres}\), and it grades nothing.
````

**DECLARATION:** "Part VI now says that (E) has no condition that each commitment do work; that a commitment such that every support stays a support when it is added and when it is removed does no work by itself in the candidate, leaves the candidate's standing under (E) unchanged and is critical in no support; that when the commitments are infinitely many a block of such commitments can still be critical; and that how hard an account is to vary is a separate matter, shown by Pres, which grades nothing."

**CHECK, the checkers' history:** "check 2, FIX. Four defects: under the drafted test every commitment of L313's infinitary support "does no work"; "any support" could be read as "some support"; the declaration's "or" let one half of the test suffice; and "measure", as in W36.1. NEW scopes the label ("does no work by itself in the candidate"), states both halves for every support, says what happens when Γ is infinite, and reads "a separate matter, shown by Pres". Cases: O2's "this derives L275 s2's rule" is struck (circular); O19 is added, watched."

**What the entry says about N1 (CASES AT RISK):** "N1: toward if the sun-god sentence constrains nothing, or is not among the active commitments. Watched: if it is read as a second component that keeps the tilt steady, it is either a redundant route or an unfaithful component. As a redundant route it fails the removal test, and the verdict "not part of what explains" moves to DISAGREE. As an unfaithful component it fails the addition test; that is interference, and "Tomas explains" is at risk. Which reading applies turns on how Γ is typed (W20, held)."
- W20.1's entry later settled the membership question: "Tomas offers the sun-god sentence as keeping the tilt steady, so under this sentence it is a commitment wherever it is a component. The membership question that W33.1 left to W20 is settled, and the watch moves to fidelity."
- The list's closing check records "N1, as W33.1 records, now on fidelity rather than membership" as watched, with a risk away.

## 2. The reply's argument

The argument is in point 3, headed "R06, R21, R24, R25, R30, R34 · (d) — declared moves toward the fixed verdicts; none away." The R24 bullet reads:

> R24 (line 313) on N1: "Strike it out and the account works exactly as before" is R24's no-work commitment — every support stays a support with and without \(d\), so \(\{d\}\) is critical in no support by (B). The equivalence between the two characterizations holds: closure of \(\mathsf S\) under adding and removing \(d\) just is the absence of any critical block \(\{d\}\).

The closing line is "R24: STANDS".

**The quotations were checked (S90 rule 8).**
- "Strike it out and the account works exactly as before" is word for word in N1's verdict. It appears in the part C brief (line 971) and in the S89 book.
- The reply's paraphrase of NEW is accurate: "every support stays a support", both halves, and "\(\{d\}\) is critical in no support (B)".
- The line is right: NEW is on revised-text line 313.

## 3. Reading and working

**What (B) says.** It reads \(\operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S\land W\setminus B\notin\mathsf S\), for nonempty \(B\subseteq W\).
- "\(\{d\}\) is critical in no support" therefore says that \(W\setminus\{d\}\in\mathsf S\) for every support \(W\ni d\). That is the removal half of R24's test, and only that half.

**The text's claims hold.** Take a commitment that passes both halves.
- For any \(W\subseteq\Gamma\) with \(d\in W\), the removal half gives \(W\in\mathsf S\Rightarrow W\setminus\{d\}\in\mathsf S\). The addition half gives the converse. So the candidate carrying \(d\) meets (E) exactly when it meets (E) without \(d\).
- The removal half alone gives "\(\{d\}\) critical in no support".
- "Infinitary support" (L311) bears out the infinite case. Every \(d_n\) passes both halves, because adding or removing one index leaves an unbounded set unbounded. But the block "\(W\) minus finitely many of its indices" leaves a bounded set, and so it is critical.
- When \(\Gamma\) is finite, no block of such commitments is critical, since removing them one at a time keeps a support. The text's "When \(\Gamma\) is infinite" is therefore exact.

**The reply's equivalence is false, but NEW does not assert it.** The reply says that closure of \(\mathsf S\) under adding and removing \(d\) "just is" the absence of a critical \(\{d\}\).
- Part VI's own Interference paragraph (L309) refutes it. There \(\Gamma=\{a,b\}\) and \(\mathsf S=\{\{a\}\}\).
  - \(\{b\}\) is critical in no support: \(\{b\}\not\subseteq\{a\}\), and \(\{a,b\}\notin\mathsf S\).
  - Yet adding \(b\) to the support \(\{a\}\) leaves no support.
- A brute-force check agrees (scratch `fin/r24_check.py`). It runs over all 256 families \(\mathsf S\) on a three-element \(\Gamma\).
  - All 16 families that pass the test satisfy both of NEW's consequences.
  - In 65 families \(\{d\}\) is critical in no support while the test fails. "Critical in no support" coincides with the removal half in every family.
  - Read over every candidate \(E|W\) that carries \(d\), "meets (E) exactly when … without \(d\)" is equivalent to the test. There are 0 counterexamples.
- NEW states consequences ("then"), not an equivalence with (B). The definition names both halves outright ("after \(d\) is added … and after \(d\) is removed"). The entry's REASON gives the addition half its job ("excludes an interfering commitment").
- So the reply's gloss is its own error. It is no defect of the text, and nothing in NEW invites a reader to drop the addition half.

**N1, worked on the current text and on the revised text.**
- *The toward reading: the sun-god sentence constrains nothing.* The verdict says "Nothing about the seasons, and nothing anyone could check, depends on whether the god exists or approves".
  - On that reading the god component imposes no constraint that differs from its absence. It passes both halves in every support, \(\{d\}\) is critical in no support, and Tomas's candidate meets (E) exactly as it does without the sentence.
  - R24 now says this in words: "(E) has no condition that each commitment do work", and the sentence "does no work by itself". That gives "Yes, Tomas explains" and "not part of what explains", which is the fixed verdict.
  - On file 11 the same answers could be derived from (S), (B) and the absence of any such condition in (E), but the text did not state them. The move is toward, or AGREE on firmer text.
  - The declaration accounts for it. It names "(E) has no condition", the test, "leaves the candidate's standing under (E) unchanged" and "critical in no support". So the move is not an undeclared change of claim, and the reply is right to call it declared.
- *The reply reads the verdict too narrowly.* "Strike it out and the account works exactly as before" matches only the consequence for the full candidate, \(\Gamma\in\mathsf S\iff\Gamma\setminus\{d\}\in\mathsf S\). It does not match the whole test over every support.
  - The verdict's next sentence, "The steady tilt is already accounted for by the point about spinning bodies", and the book's open note ("the god is given the job the spinning-top point already does") leave the redundant-route reading open.
  - *Redundant route.* On that reading a faithful god component is a second route. It fails the removal test at \(\{\text{god},\dots\}\) without the spin component, which is away on "not part of what explains".
  - *Unfaithful component.* On that reading (F1) fails with the god in \(\Gamma\). That is the addition half, or interference, and it puts "Tomas explains" at risk.
  - Neither risk is R24's. File 11 already has both: L307's "each is contributory" and (B) for the route, and (F1)'s "every active component" for the unfaithful component. R24 names these outcomes. It does not produce them.
  - So the reply's "none away" is right about R24. It does not close N1's watch, which the entry and W20.1 record, now on fidelity.
- *The other cases.*
  - **O45 holds.** Removing the second spring from the support in which it is the only spring leaves no support. So it fails the removal test and does work: "It was already a route".
  - **N2 holds.** The "No" rests on the patch restating the sailor's report, which fails non-circular dependence. "It grades nothing" removes no failing conjunct.
  - **O8 holds.** Scope is untouched.

## 4. Ruling

**KEEP.** W33.1 stands as drafted.
- The move the reply names on N1 is toward the fixed verdict, and the declaration accounts for it. The reply names no move away, and none comes from R24.
- The reply's equivalence ("closure … just is the absence of any critical block \(\{d\}\)") is false. Interference at L309 is a counterexample. NEW does not claim it: it states that the two-halved test entails both consequences, and it does.
- OLD, NEW, KIND and DECLARATION are unchanged.

**For the CHECK field (S90 rule 3):** "Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on N1 ("Strike it out and the account works exactly as before" read as the no-work test, with \(\{d\}\) critical in no support), and claimed that the test is equivalent to "\(\{d\}\) critical in no support". Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. The move on N1 is toward, on the reading where the sentence constrains nothing, and the declaration accounts for it. The claimed equivalence is false (Interference, L309: \(\{b\}\) is critical in no support but fails the addition half), and NEW does not assert it; NEW's "then" consequences follow from the two-halved test. N1's watch on the redundant-route and unfaithful readings stays as recorded. It comes from (B), L307 and (F1), not from this entry. O45, N2 and O8 hold."

**A record point, outside the ruling.** The entry's CHECK says "O2's 'this derives L275 s2's rule' is struck (circular); O19 is added, watched". But its CASES AT RISK still ends the O2 item with "This derives L275 s2's rule." and does not name O19. The two fields should be reconciled when this CHECK line is added. That is housekeeping in the change list, and the theory text is unaffected.
