# Ruling: s90_xexam_mimo_C, item 5, R25 (W40.1)

*A fresh Claude checker, 24 September 2026. It works under the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rules 1–3), and under the rerun note "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (ruling 4: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list, and did not write the part briefs.*

*The call.* The reply is `parts/s90_xexam_mimo_C.response.txt`. The file name the task gives, with the call description in place of the tag, does not exist; this is the one reply of this tag. Pass 2, attempt 1 of 1: status 200, finish "stop", 0 bad chunks, accepted. END OF REPORT is on the last line. The sha256 is 9ea0342fa8d813c269086400a6be74deaa4cecfdc372c9857faaabe1c954eb90, which matches the receipt. It is 1,321 words by `wc -w`. Pass 1 of this tag ended on the dead proxy with no reply (rerun note §1), and none of it was read. No reasoning file was opened.

*Why R25 is here.* The reply's closing line is "R25: STANDS". Its point 5, under task (a), says the declaration leaves out part of what the new wording claims. That is a claim that the change includes an undeclared part, so R25 is contested under S90 Parts rule 2. The orchestrator also pointed to Atria C's point 3, which names a declared move toward the fixed verdict on N22 through R25. That point is read below as another reader's view and does not count toward the ruling (Parts rule 1).

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e (as at 587eebf; no later commit touches it);*
- *the revised text, `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`, md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923, read only;*
- *the part C brief, md5 2183faa5005b112347f484b6c8ace196 (its R25 block and tasks (a)–(d));*
- *the S81 book (md5 4f488d149e44669240d5db546c8e946a), the S89 candidate book (md5 b2e535777976a511935430bd089ba500) and D3-T's `final.md`;*
- *the revision note draft (row R2-25 and the note's line for L337), and the plan and worklist rows for W40.*

*The S87 rules (05, 05b and 05c) govern S87 rows, not S90 parts, so they are not applied here.*

*Map (part-rule table): "R25 | W40.1 | C21 | C | 337 | 335 | CLAIM | N22".*

## 1. The entry and its checkers' history

W40.1, "Part VII: why the absent structure appears is a separate question".
- **Group** C. **Item** W40 (M6; source point 15).
- **Place.** Part VII, "Explanations that remove structure". File-11 L337, revised L335. One sentence is added after the paragraph's last sentence, which is kept byte for byte, attack pointer included (D9).
- **REASON WORD** clarification. **KIND** CLAIM.
- **OLD:** `This is the semantics' treatment of eliminative explanation; it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be.`
- **NEW:** `This is the semantics' treatment of eliminative explanation; it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be. Where the absent structure appears to be present, the question why it appears is a separate question with its own target and contract (Part III): an account of the absence neither answers that question nor needs to, and a bare denial, which offers no component that responds to a change in what produces the appearance, is not an account of it.`
- **DECLARATION:** "Part VII now says that where an absent structure appears to be present, why it appears is a separate question with its own target and contract, which an account of the absence neither answers nor needs to answer, and of which a bare denial is not an account."
- **CHECK (the checkers' verdict):** "check 2, FIX. "Why does X appear?" used a bare X where the paragraph defines only "X-effect"; NEW reads "the question why it appears". Inserted before "This is the semantics' treatment …", the new sentence took over the antecedent of "This"; the entry is now anchored on the paragraph's last sentence, which it keeps byte for byte, attack pointer included (D9)." The fix changed placement and wording. It did not change the declaration or the relative clause.
- **REASON (not sent):** "A bare denial has no component that answers to changes in what produces the appearance, so it cannot meet (F1) or non-circular dependence on that second question." So the drafters meant the clause as the ground of the declared verdict, drawn from (E).
- **CASES AT RISK:** "N22: toward. Wren offers no component for the appearance question. Yuri offers one …; the question does not ask whether that candidate is adequate." N8 holds, and N25 holds. O34 was checked and does not move. Part C gave N22 only.
- **Record.** Revision note row R2-25: W40.1, C21, L337, clarification, CLAIM, declared "yes". The note's line for L337 is the declaration word for word. Plan row W40: "Take: "why does X appear?" is a separate question with its own contract, and a bare denial is not an account of it". Worklist W40, Handling: "Clarification … This is not a new condition on the first question." The sources note's "Elimination" line rests on this entry, and its fallback is "drop the sentence".
- **Earlier rulings.** Batch 1 and batch 2 make no ruling on R25, W40.1 or C21. No other ruling file names it. The single S90 call (C21) failed and supports nothing. There is nothing to reconcile.

## 2. The reply's argument

The closing line is "R25: STANDS". Point 5, headed "R25 — (a): the declaration drops the text's characterisation of "bare denial."":

> "The new text (line 335) reads: "a bare denial, **which offers no component that responds to a change in what produces the appearance**, is not an account of it." The bracketed clause is what makes the denial "bare" — it is a structural criterion (no component with the right edit-signature for the appearance-producing mechanism, cf. Part II's "measurement's signature"). The declaration says only "a bare denial is not an account," leaving "bare denial" uncharacterised. A reader of the declaration alone could not tell which denials are excluded. Minor, but the characterisation is part of the claim."

> "**Repair.** Change "of which a bare denial is not an account" to "of which a denial that offers no component responsive to changes in what produces the appearance is not an account.""

The reply names no case for R25.

**Quotations checked (S90 rule 8).**
- The quotation of the new wording matches revised L335 byte for byte, apart from the bold.
- "a bare denial is not an account" is the reply's shortening of the declaration's "of which a bare denial is not an account". The repair quotes the declaration exactly.
- "measurement's signature" occurs at revised L127 (file-11 L129): "a part that reads or reports another part has a measurement's signature".

All the quotations are found.

**Atria C (another reader's view, not counted).** Point 3, under (d), says: "R25 (line 335) on N22: Wren's bare denial "offers no component that responds to a change in what produces the appearance," so it is not an account of the appearance; Yuri's memory machinery supplies one, whether or not it is true — which is all the verdict asks." Atria counts this as a declared move toward the fixed verdict and closes "R25: STANDS".

## 3. Reading

**What the reply gets right.**
- The relative clause is part of the new wording, and the declaration does not repeat it.
- "Bare denial" is a new phrase. It occurs nowhere else in the revised text or in file 11.
- Task (b) asks, of every part of a CLAIM change that its declaration does not mention, whether it changes a claim. So the question is whether a reader can conclude, from "which offers no component that responds to a change in what produces the appearance", anything that neither the declared sentence nor file 11 already gives. They cannot, for the reasons below.

**1. The clause is the ground of the declared verdict, and the ground is file 11's (E).**
- The appearance question is "why it appears". By Part III (revised L151, file-11 L153) it is a production question: "A production question has a \(\mathcal Q\) that reads an output port and a \(C\) containing interventions on upstream ports." So its contract contains changes to what produces the appearance.
- A candidate with no component that responds to those changes cannot meet (E) on that contract, and file 11 already says so:
  - Non-circular dependence (revised L255, file-11 L257) requires "a nonempty block \(G\subseteq\Gamma\)" whose deletion loses a contrast in the answer. A candidate with no component that responds to the contract's changes has no such block.
  - (F2) and (A) fail too: the target's answer varies under the contract's changes while the candidate's stays fixed.
  - Part V's own parallels already state the pattern:
    - "A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing one" (file-11 L271, revised L269);
    - "So does an account whose only substantive component restates the answer it was asked for" (file-11 L275, revised L273). Wren's "People are mistaken about this" restates the answer.
  - Part 0 (file-11 L39, revised L37) uses the clause's own idiom: "A correlation has no component that responds to an intervention on its supposed input; a cause does."
- So "offers no component that responds to a change in what produces the appearance" puts in (E)'s terms why a bare denial "is not an account of it". The declaration states that conclusion. A declaration says what changes in what is claimed; why the change holds belongs to the REASON field, and here the REASON field says it.

**2. The clause does not change the reach of the declared claim.**
- Grammar. The clause is set off by commas, so it is non-restrictive. It describes bare denials; it does not define a new class that "bare" alone would miss. "Bare denial" keeps its ordinary sense: a denial and nothing more. The clause says what such a denial lacks in the theory's terms.
- The cases where the reply fears a declaration-only reader "could not tell which denials are excluded":
  - *A denial with nothing more.* It is bare in the ordinary sense and on the clause alike, and it is not an account. The declaration and the new wording agree.
  - *A denial with an argued account of the absence and nothing about the appearance.* Under the new wording the first limb decides it: "an account of the absence neither answers that question". The declaration carries that limb word for word. Same verdict.
  - *A denial that offers some component for the appearance.* This is Yuri. It is not bare in either sense, and neither the declaration nor the new wording says it is or is not an account; that is left to (E). Same verdict.
- So on every kind of denial, a reader of the declaration and a reader of the new wording reach the same conclusions. Nothing the new wording claims goes beyond the declaration. The clause adds only the (E)-ground of point 1.

**3. The proposed repair would make the declaration less exact.** It replaces "a bare denial" with "a denial that offers no component responsive to changes in what produces the appearance". That turns the new wording's non-restrictive description into a restrictive condition that the new wording does not state. It would also drop "bare", which is the new wording's own subject. The resulting general claim (any denial with no such component is not an account of the appearance) is true, but it is true by (E) together with the declared first limb. The declaration would then describe a sentence the text does not contain. The reply itself rates the point "Minor" and gives STANDS.

**4. Coherence (task (c)).**
- The pointer "(Part III)" says what the change says it says: "Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other" (revised L151).
- "Component" and "responds to a change" are the text's own terms (Part II, "Kinds are edit-signatures", revised L111–127).
- The added sentence follows the attack pointer, so "This is …" keeps its antecedent (check 2's fix).
- Attack (B) at revised L532 is unchanged, and it still names eliminative explanation as the exposed case.
- No unchanged sentence becomes false.

**Cases worked.**
- **N22** (the only case part C gave; the fixed verdict is "Wren gives none; Yuri gives one").
  - *Wren* says only "People are mistaken about this". That is a bare denial in the ordinary sense, in the verdict's own words ("with nothing about where the mistake comes from"), and on the clause (no component). The declared "a bare denial is not an account" gives the theory's verdict: Wren offers nothing on the appearance question. That is the move toward, and the declaration accounts for it.
  - *Yuri* offers a component: the machinery that reads memories and produces reports. Change it, and the reports change. Nothing in R25 says his candidate is or is not an account, and the verdict does not ask ("Whether it is good or true is another matter"). His standing as the giver of an explanatory candidate (Part V, revised L231, file-11 L233) is file 11's and is unchanged.
  - So the clause separates Wren from Yuri exactly as the ordinary sense of "bare" already does. There is no undeclared move and no move away. Atria's reading gives the same result by the same route.
- **N8** (named by the entry, not given in part C): Pia and Quentin answer "why is there no such machine", an obstruction question. No appearance is to be explained, so no move.
- **N25** (named, not given): none of the cosmologies denies an appearance, so no move.
- **O34** (checked by the drafters): the colleague supplies a meaning for a changed question (Part III). That is not an eliminative account and not an appearance question. No move.
- **No other O-case is eliminative.** A search of the S81 book for appearance and denial finds none beyond O34 and incidental uses of "appear".
- **D3-T:** two controller designs and a tester. There is no denial and no appearance. Not touched.

## 4. Ruling

**KEEP.** W40.1 stands as drafted. OLD, NEW, KIND (CLAIM) and DECLARATION are unchanged.

**Reason.**
- The relative clause "which offers no component that responds to a change in what produces the appearance" changes no claim. It describes the bare denial, and it gives in (E)'s terms why such a denial is not an account of the appearance question. File 11 already supplies that ground:
  - non-circular dependence needs a block whose deletion loses a contrast (file-11 L257);
  - a table with no component that responds to an intervention fails under any contract containing one (L271);
  - an account whose only component restates the answer fails (L275);
  - a production question's contract contains interventions on upstream ports (L153).
- On every kind of denial the declaration and the new wording give the same verdicts: its first limb covers argued denials that are silent on the appearance.
- The proposed repair would make the new wording's non-restrictive description into a restrictive condition it does not state.
- N22 moves toward its fixed verdict as declared, and no case moves away.

**For the CHECK field (S90 rule 3):** "Cross-examination of revision 2 (S90 part C): Mimo gave STANDS but said under (a) that the declaration omits the new wording's description of a bare denial ("which offers no component that responds to a change in what produces the appearance"); Atria gave STANDS and named the declared move toward N22. Ruled KEEP after the cross-examination: the clause gives the ground of the declared verdict in (E)'s terms, which file 11 already supplies (non-circular dependence L257; L271; L275; Part III L153), and on every kind of denial the declaration and the new wording agree, so the declaration is exact."
