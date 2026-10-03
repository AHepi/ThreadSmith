# Ruling: s90_xexam_atria_C, item 7, R34 (W35.3)

*A fresh Claude checker, 24 September 2026. It did not draft, assemble or check the change list, and it did not write the part briefs. It works under three rules:*
- *the S90 rule ("S90 How the cross-examination of the revision 2 draft will be read - written before sending.md");*
- *the parts rule ("S90 Parts - how they will be read, written before sending.md"), rules 1-3 and 5;*
- *the rerun note ("S90 and S87 - seven calls rerun after the container restart - written before sending.md"), section 2, item 4: the pass-2 reply stands where the pass-1 reply would have stood.*

*The S87 rules (05, 05b and 05c) govern S87 rows, not S90 parts, so they are not applied here.*

*File name.* The task names a file with the whole call description in it. That name is 287 bytes, over the file system's 255-byte limit. This file uses the short form of the other Atria C rulings in this folder.

*The call.* The reply is `parts/s90_xexam_atria_C.response.txt`. The task's file name puts the call description where `.response` belongs, and no file of that name exists. This is the only reply with this tag.
- Pass 2 was accepted on attempt 6 of 6. The receipt's attempt history shows attempts 1-5 at status 0 with nothing back (1,802.4, 1,590.3, 497.8, 119.6 and 929.0 s). Attempt 6 returned status 200 and finished "stop" after 1,091.3 s, with 0 bad chunks.
- END OF REPORT is the last line. The reply has 1,227 words by `wc -w`. Its sha256 is bd51b78593b3ac9e7d194d7f0b62e43e223f8c487d6e611a6118999d50d7a72f, which matches the receipt.
- The receipt's `user_sha256` is a94c8ef9ead3…, the part C brief. No reasoning or pass-1 file was opened.

*Why R34 is here.* The reply's closing line is "R34: STANDS". Its point 3, under task (d), names a move of the theory's verdict on N19 that R34 causes, and calls the move declared and toward the fixed verdict. Under parts rule 2, a change is contested when a reply names a moved verdict on it, "whatever line it gives the change". The reply's other points name no move for R34:
- point 3 says only that R34 "also fits" N18 and O27;
- point 2 puts N18 on R12, R13 and R14, and point 1 says no verdict moves there;
- point 4 concerns R23, and point 5 concerns R07.

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e (587eebf; no later commit touches it), entry W35.3;*
- *the revised text, `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`, md5 9aecf2f30ce0b4523606b2b8409fdf37, L140-147, L208, L223, L395-423, L429-449, L516, L580-586 and L612-626, and searched for "difficult", "problem" and "obligation";*
- *file 11, md5 5e494c1095d920d128b9a79de378f923, read only, at L421 and L425-431, and searched for "difficult" and "critical episode";*
- *the part C brief, md5 2183faa5005b112347f484b6c8ace196: its R34 block, tasks (a)-(d), and cases O12, O27, N18 and N19;*
- *the S81 book, md5 4f488d149e44669240d5db546c8e946a, searched;*
- *the S89 candidate book, md5 b2e535777976a511935430bd089ba500: N18 and N19 in full, with confidence and open notes;*
- *D3-T's `final.md`;*
- *S81 determination 04: the rows for O12 and O27;*
- *the revision note draft, row R2-34;*
- *the worklist's W35 and its case-table rows for N18 and N19;*
- *the plan's W35 row;*
- *Mimo C's reply, searched for R34;*
- *the other scratch rulings of this folder that mention R34 or W35.3: Atria C item 1 (R13), and Mimo C items 1 (R12) and 4 (R13).*

## 1. The entry and its checkers' history

W35.3, "Part X: what a recognized difficulty is".
- **Place.** Part X, "Episodes", file-11 L421, revised L423. One sentence is added after s1. s1-s3 are unchanged.
- **Group:** C. **Item:** W35 (b′). **Reason word:** clarification. **KIND:** CLAIM.
- **OLD:** `A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response.`
- **NEW:** `A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response. A **recognized difficulty** is a failure of a claimed obligation, or a conflict in which what the system holds meets a claimed obligation only by failing a protected one (Part XI), when the system represents it.`
- **DECLARATION:** "Part X now defines a recognized difficulty as a represented failure of a claimed obligation, or a represented conflict in which what the system holds meets a claimed obligation only by failing a protected one."
- **CHECK (the checkers' verdict):** "check 2, SOUND. N19 is watched, not simply toward (a reader has to take one demand as claimed and the other as protected); N18 Q1 is watched (L514 lists obligations "of a repair")."
- **CASES AT RISK (the drafters' expectation, not sent):**
  - N19: toward. The clash is a recognized difficulty before anyone reads the chapter. The first draft is not a Repair, and the second is.
  - N18: toward on Q1.
  - O12 stays SILENT on its worth point, and is watched for "the need it met was only recognised afterwards".
  - O27 stays SILENT on "mostly": toward on the episode, with no change of mark. O21, O40 and O50 do not move.
  - O13, O35 and O38 (Repair) are untouched.
- **LOSS:** "A difficulty that the system does not represent as a failure or a conflict of obligations is not a recognized difficulty."
- **Record.**
  - Revision note row: "R2-34 | W35.3 | C29 | 421 | clarification | CLAIM | yes".
  - Parts map: "R34 | W35.3 | C29 | C | 421 | 423 | CLAIM | O12, O27, N18, N19".
  - Worklist case table: N19, "a problem as a clash of obligations before any observation; a draft that drops P is not a Repair". N18, "a constructed theory contradicted (Rhea); an expectation from an incomplete history (Dov)".
- **Earlier rulings.**
  - Batch 1 and batch 2 make no ruling on R34, W35.3 or C29.
  - The single S90 call (C29) failed and supports nothing.
  - Mimo's reply to part C gives "R34: STANDS" and makes no point on R34.
  - No reply to another part cites R34.
  - The scratch rulings on R12 and R13 (Mimo C items 1 and 4) find W35.3 unaffected. The Atria C item 1 ruling on R13 (a FIX) keeps the clause "a violation the system represents can be a recognized difficulty (Part X)" word for word.
  - There is nothing to reconcile.

## 2. The reply's argument

The closing line is "R34: STANDS". Point 3 is headed "R06, R21, R24, R25, R30, R34 · (d) — declared moves toward the fixed verdicts; none away." Its R34 bullet reads:

> "R34 (line 423) on N19: Odile's foreseen clash is "a conflict in which what the system holds meets a claimed obligation only by failing a protected one … when the system represents it" — a recognized difficulty before any reader stumbles. It also fits N18 and O27 (the robot represents the failure of the expert's claimed diagnoses; the expert's framing remains an outside contribution under Part X's Ownership)."

The reply finds no defect in R34. It names a declared move toward the fixed verdict on N19. It says that R34 "fits" N18 and O27, and does not call either a move.

**Quotations checked (S90 rule 8).**
- "a conflict in which what the system holds meets a claimed obligation only by failing a protected one … when the system represents it" is in NEW at revised L423. The ellipsis stands for " (Part XI),". Found.
- "(line 423)" is correct.
- "Odile's foreseen clash" and "before any reader stumbles" are paraphrases, not quotations. They render N19's "A clash one can foresee is already a problem, and no reader needed to run into it."
- "Part X's Ownership" is the **Ownership** paragraph at revised L421, in Part X. Correct.

Every quotation is found.

## 3. Reading

### N19 (given): the reply's named move is real, toward, and declared

**Q1: "Did Odile have a problem before anyone read the chapter?"**
- **The current text is silent.**
  - File 11 uses "recognized difficulty" once (L421) and never defines it.
  - "Problem" is not defined either. It occurs only in "problem-directed activity" (revised L397) and in "an available problem" (L399).
  - L399 lets a first representation be built "from an available problem without prior observation of what it represents". But nothing says what makes something a problem or a difficulty.
  - So the text does not settle whether a foreseen clash between two demands counts.
- **The revised text agrees with the verdict, by the second limb.**
  - Her two demands are declared inputs as L435 describes them: "each as a stated condition over stated occasions". Rich language (L) and pace (T) are stated for the occasion of chapter five.
  - What she holds while planning is the plan with the dawn description.
  - With L claimed and T protected, the plan meets L only by failing T. That is the literal reading of "meets a claimed obligation only by failing a protected one".
  - With T claimed and L protected, what she holds can meet T only by cutting the description, which fails L.
  - With both demands claimed and both protected (nothing in Part XI forbids an overlap), both descriptions hold.
  - She "sees" the clash before writing. That is a representation by (R) (L208): a faithful transport, with constructed provenance, to a clash that is real.
  - No reader and no observation enters the definition. So the text gives "Yes, before anyone read it".
- **The CHECK's watch point does not bite.** The CHECK asks which demand a reader takes as claimed and which as protected.
  - The limb holds under every declaration that puts one demand in O and the other in P, including O = P.
  - The situation supplies such a declaration in substance. She "wants two things from every chapter", and the verdict counts dropping one as "trading one demand for the other".
  - So Q1 does not turn on an unsupplied input, and L516's "where the input is missing, the verdict is unsettled" does not apply.
  - The only declaration that defeats the second limb is P = ∅, and that is not the situation's.
- **One step is a reading, not forced.**
  - The question says "problem", while the text says "recognized difficulty". The text does not equate them: the entry's REASON puts that mapping in the sources note (W38).
  - A careful reader takes the episode's first element as the text's counterpart of the question's "problem". A reader who refuses keeps Q1 SILENT, as under file 11.
  - So Q1 moves toward, or at worst holds SILENT. It cannot move away.
- **The move is declared.** It uses exactly the declaration's second clause, "a represented conflict in which what the system holds meets a claimed obligation only by failing a protected one". The drafters predicted it ("N19: toward"). So it is not an undeclared change of claim under task (d).

**Q2: "Does either draft solve it?"** The reply makes no point on Q2.
- R34 defines the difficulty, not its solution. Repair (P) at L431 is not R34's text.
- In R34's own terms, the first draft leaves the conflict in place: what she then holds meets T only by having failed L. The second draft removes it: what she holds meets both. That fits "The first draft does not solve it … The second draft solves it".
- Through (P), the answer also depends on the declared O and P and their occasions (L435). That is so in file 11 too, and it belongs to (P) and to R36 (W5.1, part B2), not to R34. It is not ruled here.
- So Q2 holds or moves toward. It does not move away.

### N18 (given): "also fits". R34 moves Q1 toward, as declared

- **Q1** asks whether each designer met "a problem, meaning something he or she must now understand and fix".
  - Both designers claimed that the bridge stays steady: Rhea's bridge "would stay steady under any crowd she expected", and Dov expected his "to be as trouble-free as the original".
  - Both see it sway. That is a represented failure of a claimed obligation, the first limb.
  - File 11: SILENT, since the notion was undefined. Revised: "Yes, both met a problem", which agrees.
  - The case book's minority reading on Dov ("only a practical fix, not something to understand") is not taken up by R34. The first limb does not ask whether the fix needs understanding, so Dov's difficulty counts as the verdict says.
  - The move is toward, and the declaration's first clause accounts for it. The entry predicted it ("toward on Q1"). The reply calls it a fit, not a move, which understates it and is not an error.
- **The CHECK's watch point, "L514 lists obligations 'of a repair'" (revised L516), raises no clash.**
  - The obligation that fails, a steady bridge, is the one each designer's repair will address, so it is an obligation of a repair.
  - L516 lists where such obligations are declared, and R34's "(Part XI)" points to the same O and P.
- **Q2 and Q3** turn on expectation, violation and surprise (R12 and R13: the reply's point 2 and the sibling rulings), not on R34.
  - R34 agrees with L223 as the sibling ruling on R13 fixes it: "a violation the system represents can be a recognized difficulty (Part X)".
  - Rhea's represented violation is a recognized difficulty because steadiness under that crowd is her claimed obligation.
  - Dov's failure is surprise, and it is still a recognized difficulty by the first limb.
  - Both fit "A problem for both".

### O27 (given): "also fits". The mark holds

- **The reply's gloss is loose.** It says "the robot represents the failure of the expert's claimed diagnoses".
  - In R34, "claimed" is Part XI's "claimed obligations" (L429): a stated condition to be repaired (L435).
  - The expert's diagnoses are candidate accounts, not obligations.
- **Read correctly, the gloss holds.**
  - The claimed obligation that fails is the diagnostic one: to find the fault, an epistemic obligation (L437). The test was to meet it by separating the candidates.
  - "The result fits neither candidate" is the robot's own represented failure of that obligation. So the robot's episode has a recognized difficulty of its own.
- **"The expert's framing remains an outside contribution"** is true under revised L421 ("Work supplied from outside that boundary, a diagnosis, a decisive question, … remains an outside contribution"). That is unchanged text, not R34.
- **The mark holds.** S81 determination 04 gives O27 SILENT on "mostly" for file 11. "Mostly" turns on Origin and on a weighting of credit, which is a declared input (L516). It does not turn on whether the episode had a recognized difficulty. R34 fills in the episode's first element (the entry: "toward on the episode, with no change of mark"). O27 holds SILENT.

### O12 (given, not raised by the reply): holds SILENT

- **The mark.** S81 04 gives SILENT on "its merit is real". Worth needs the normative relation (L449), and R34 does not touch worth.
- **"The need it met was only recognised afterwards."**
  - The team represented a failure, the work not getting done, which they blamed on laziness. With "the work gets done" as a claimed obligation, that is the recognized difficulty.
  - The obligation Noor's question met, "every task should have an owner", was stated afterwards, which is what the verdict says.
  - R34 asks that the failure be represented. It does not ask that the obligation met be stated in advance.
- **A stricter reader.** A reader who demanded more would find the episode incomplete. The verdict claims no complete episode, though: finding a question is Origin of a contract (Derivation 5, L580-586), which needs no recognized difficulty. The mark is SILENT either way.

### D3-T: not touched

D3-T is selection by a tester. The discarded controller fails the tester's criterion, but no system represents that failure and no episode is claimed. The question concerns what passing leaves open.

### Coherence (task (c)): no defect

- **The pointer is exact.** "(Part XI)" points to L429 ("For claimed obligations \(O\) and protected obligations \(P\)") and L435 (declared inputs). A forward pointer is the text's usual form.
- **"Represents" is (R) at L208,** so a failure that did not occur is not a recognized difficulty. That is within the declaration's "represented".
- **L223 agrees with L423,** both as drafted and as the sibling R13 ruling fixes it. "A violation the system represents *can be* a recognized difficulty (Part X)": it is one when fidelity at that pair is a claimed obligation.
- **L399's "available problem without prior observation"** is supported by the second limb, not contradicted.
- **Derivation 10 (L612-624) is not made false.**
  - In file 11 its (EK) claim already left the episode's four elements implicit.
  - Its violation, together with the obligation "possess a deployable account of re-emergence after occlusion", fits the first limb when the system represents the violation.
- **No second definition.** "Recognized difficulty" occurs only at L223 and L423. "Problem" stays undefined, as the REASON says.
- **The declaration matches NEW.** NEW claims nothing more: the bold marks the definition and "(Part XI)" is a pointer. "When the system represents it" governs both limbs, as the declaration's "represented … or a represented …" says.

## 4. Ruling

**KEEP.** W35.3 stands as drafted: OLD, NEW, KIND (CLAIM) and DECLARATION are unchanged.

**Reason.**
- The reply finds no defect. The move it names on N19 is real, and it is toward the fixed verdict.
  - Q1 goes from SILENT to AGREE: a foreseen clash is a represented conflict in which what she holds meets one demand only by failing the other, and no observation is needed.
  - The move holds under every declaration that puts one demand in O and the other in P, and the situation supplies such a declaration.
  - It follows from the declaration's second clause and was predicted.
- N18 Q1 also moves toward, from SILENT to AGREE for both designers, by the declared first clause.
- Q2 on N19 holds or moves toward. What it turns on through (P) is not R34's.
- O27 and O12 hold SILENT. D3-T is untouched.
- The reply's O27 gloss mistakes the expert's diagnoses for claimed obligations. Read as the robot's diagnostic obligation, the point stands.
- Every quotation checks, and no coherence defect was found.

**For the CHECK field (S90 rule 3):** "Cross-examination of revision 2 (S90 part C): Atria gave STANDS and named, under (d), a declared move toward the fixed verdict on N19 (the foreseen clash is a represented conflict, a recognized difficulty before any reader), and said the change also fits N18 and O27. Mimo gave STANDS with no point. Ruled KEEP after the cross-examination. N19 Q1 moves toward (SILENT to AGREE) by the declaration's second clause, under every declaration that puts one demand in O and the other in P (O = P included), which the situation supplies. It is a reading only in taking the question's "problem" as the recognized difficulty. N19 Q2 holds or moves toward: what it turns on through (P) is (P)'s and W5.1's, not this entry's. N18 Q1 moves toward for both designers by the first clause. L516's "of a repair" names the same O and P. O27 holds SILENT on "mostly": the robot's "fits neither" is a represented failure of its diagnostic obligation, and the expert's diagnoses are candidates, not claimed obligations. O12 holds SILENT: the failure was represented, and the need met was stated afterwards. D3-T is untouched. "(Part XI)" is exact, and L223's "can be a recognized difficulty (Part X)" agrees."
