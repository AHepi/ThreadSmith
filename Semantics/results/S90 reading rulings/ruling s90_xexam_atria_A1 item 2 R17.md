# Ruling: R17 (W20.2), contested by Atria's reply to part A1

*Fresh Claude checker. It did not draft, assemble or check the change list, and did not write the part briefs. Read under the S90 rule (rules 2, 3, 7, 8), the S90 Parts rule (rules 1–4) and the rerun note (item 4: the pass-2 reply stands where pass 1's would have; item 5 does not apply, because pass 2 was accepted).*

*File name.* The name the task gave, "ruling s90_xexam_atria_A1 (part A1, Atria). Pass 2, accepted on attempt 5 of 5. … 1,103 words. item 2 R17.md", is 427 bytes. That is over the filesystem's 255-byte limit. This file uses the short form of the other rulings in this folder.

**The reply.** `results/S90 Cross-examination - revision 2 draft - returns/parts/s90_xexam_atria_A1.response.txt`.
- Pass 2. sha256 3a6d34137f78… equals the receipt's `response_sha256`.
- Finish stop, 0 bad chunks, 1,103 words by `wc -w`, END OF REPORT on its last line.
- The receipt's attempt history:
  - attempts 1 and 2: status 0;
  - attempts 3 and 4: status 200, finish length, 0 content characters, rejected;
  - attempt 5: accepted.

  That makes two rejects, within `max_rejects` 3. The `pass2.a3.*` and `pass2.a4.*` files were not opened.

**Why it is contested.** The reply's line is `R17: STANDS`. Its point 2 names a moved verdict on R17, on O33, toward the fixed verdict. Under S90 rule 2 and Parts rule 2, that makes the change contested whatever line the reply gives. Point 3 (task (c)) names no claim change and no move, so it would not make R17 contested on its own. It is dealt with in section 5.

## 1. The entry

- **Entry.** W20.2 (R17 = R2-17). Group A, item W20, drafted from the settled S88 positions (F3, block 1). File-11 line 257, revised-text line 255. Part V, "Non-circular dependence", sentence 3 (S3), the whole sentence.
- **OLD:** `There exists \((a,b)\in C\) that removes or replaces a nonempty block of \(\Gamma\) while preserving the other boundary conditions, under which the answer profile changes or ceases to be determined in the claimed way.`
- **NEW:** `There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer profile at \((a,b)\) differs from its value at \((1,b_0)\), or is not determined there in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\) (a deleted component imposes the full relation on its ports, Part II): evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.`
- **KIND:** CLAIM. **REASON WORD:** change of claim.
- **DECLARATION:** "Non-circular dependence now requires a pair of the contract and a nonempty block of the commitments such that the answer profile at the pair differs from its value at the baseline, or is not determined there in the claimed way, and this contrast is lost when the block's components are deleted from the organization: at the translated pair and the translated baseline, the answers of the organization with the block deleted are determined and equal, or an answer it determined there is no longer determined. It no longer asks for a pair of the contract that itself removes or replaces a block of the commitments."
- **CHECK (the checkers' verdict).** "Not put to check 1 or check 2. … Checked by its drafter as W19.1 was." The rider was never put to an outside reply, and X1 must test it (plan 1.3.4). The field also holds the settled fallback, which applies "if X1 finds that the rider breaks a worked case".
- **CASES AT RISK, on the point raised:** "O33 holds AGREE. "The table is faithful" is a verdict of fidelity, which S3 does not touch; model 6a holds under B." The GAIN says: "O5, O7, O33 and Part VII's production case are secured on the text."
- **REASON, on the point raised:** "L341 still reads true: … The pair "remove skewness" with \(G\) the skewness commitment is a witness, since with skewness deleted the family contains an invertible matrix at both points".
- **Earlier rulings.** None on R17.
  - Batch 1 (Mimo A1) records `R17: STANDS`. It noted Mimo's point 4 (the letter \(G\), task (c)) as not contested, and passed it to the orchestrator unruled. Batch 2 carries that note forward.
  - The R15 ruling (batch 1) cites W20.2 only as agreeing with R15's new clause.
  - This is the first reply that contests R17. There is nothing to reconcile.

## 2. The reply's argument

Point 2, quoted whole:

> "**2. R17 — (a), (d): the declaration is accurate and the change does real work.** The declaration says the new condition requires "a pair of the contract and a nonempty block" and "no longer asks for a pair of the contract that itself removes or replaces a block of the commitments." That is exactly what line 255 now says: "There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer profile at \((a,b)\) differs from its value at \((1,b_0)\) … and this contrast is lost when the components of \(G\) are deleted from \(E\)." The repair was needed. Under the old wording ("There exists \((a,b)\in C\) that removes or replaces a nonempty block of \(\Gamma\) …"), an account whose contract contains only interventions on the world — the normal case — could not satisfy non-circular dependence at all. O33 is the fixed case: the paired-knob table is faithful, and the verdict is that "a form that could ask more has not asked more." The old condition would have excluded that table (no paired-turn edit removes a row); the new one admits it, with the deletion test carrying the work. That is a move toward the fixed verdict, and the declaration accounts for it. I checked the new condition for over-permissiveness: "\(p\) because \(p\)" still fails, but through the earlier clause "The target's answer does not appear … as a component," since the existential clause alone would be satisfied by deleting the single restating component. The conjuncts are complementary, not contradictory."

Point 3 (task (c)): Part VII's unchanged sentence "Non-circular dependence is witnessed by \(I_3\) under removal of skewness and by … under removal of oddness" names the pair and the matrix, not the block \(G\). It is "not false … This survives scrutiny as a blemish rather than a defect; the repair would be to name the block."

## 3. The texts, and the quotations checked (S90 rule 8)

- **The declaration's quoted phrases.** Both are found verbatim: "a pair of the contract and a nonempty block", and "no longer asks for a pair of the contract that itself removes or replaces a block of the commitments".
- **Revised L255.** The quotation is found. The reply's "…" stands for "or is not determined there in the claimed way,". Its closing period cuts the sentence before "(a deleted component imposes the full relation on its ports, Part II): …". The line number is right.
- **File 11 L257 (OLD).** The quotation is found verbatim, up to the ellipsis.
- **"'p because p' … through the earlier clause".** The words "The target's answer does not appear … as a component" are found (S2, revised L255 = file 11 L257). The argument is right. Take a single component that installs the answer. At a pair where the answer differs from the baseline, deleting that component leaves the answer undetermined at both translated points. So S3 alone is met, and S2 fails the candidate. This agrees with S88's own check of option B ("S3 can hold through the installed answer. S2 still fails the candidate").
- **O33's words.** "The table is faithful" and "A form that could ask more has not asked more" are in the S81 book's verdict. "No paired-turn edit removes a row" is the reply's own gloss, not a quotation.
- **"Could not satisfy non-circular dependence at all".** This is too strong as stated.
  - File 11's Γ was untyped, and S88 settled the gap as holding on the mechanism-only reading R-τ-mech. On the reading where the components that assign inputs are in Γ, an intervention on an input replaces a block of Γ and witnesses the old S3.
  - The entry's REASON puts it exactly: "a pair that only sets inputs witnesses it on one identification and not on another."
  - The reply's direction is right. Its "at all" holds on R-τ-mech only.
- **Part VII (point 3).** Revised L339 = file 11 L341. The sentence is found verbatim and is unchanged.

## 4. The cases worked

- **O33, "The table with empty columns"** (S81 book, md5 4f488d14…).
  - **The case.** "Lea's question is what happens when the two freezer knobs are turned together. A colleague rewrites it as a table with one column for each knob. Every row moves both knobs together; no row moves one alone."
  - **Its verdict.** "The table is faithful. Its columns could have carried single-knob rows, and none was added. A form that could ask more has not asked more."
  - **The ruled mark does not move.** S81's determination (04, row O33) ruled file 11 AGREE, on f11 L153 s1: what a question asks is fixed by \(\mathcal Q\) and the shape of \(C\). Claude's pre-ruling (01) also cites F11 L161 on declared scope. The verdict's "faithful" is L189's definition, "faithful on \(C\)", which is the fidelity conditions (F1) and (F2). Revised L151, L189 and (F1)/(F2) are unchanged by R17. Non-circular dependence is not a fidelity condition, so S3, old or new, bears on none of the verdict's words.
  - **The reply's premise misreads the case.**
    - In O33 the table is Lea's question rewritten: its rows are pairs of the contract, the paired turns. It is not a candidate organization whose commitments are rows.
    - An edit of \(C\) does not "remove a row" on either S3.
    - This is the point S88 settled. Atria's S88 reading withdrew "the O33 flip" ("O33's verdict asserts faithfulness (L204) and sameness of question (L168), and S3 bears on neither"). Mimo agreed, and the settled finding says "O33's fixed verdict does not flip".
  - **What the reply's "toward" does name correctly.**
    - S88 recorded one consequence the case does not address. On R-τ-mech, under the old S3, no account of Lea's joint question could be claimed at all, because the knob turns set inputs and replace no mechanism commitment.
    - Under the new S3, deleting the freezer's mechanism commitment loses the paired-turn contrast, so such an account can witness (S88's model 6a).
    - That change is stated by the declaration's second sentence, and the GAIN already records it ("O33 … secured on the text").
    - So the move is toward, and it is declared. It is a gain for an account the case does not claim, not a change of the ruled mark. The entry's "O33 holds AGREE" is accurate.
- **O5 and O7** (the reply's "the normal case"). S88 found that on R-τ-mech, O5 flips on a narrowed contract that has no edit removing a mechanism commitment. It found that O7's contract (spread the salt, or sweep it off at once) only sets the salt port. Under the new S3, deleting the yeast's action (O5) or the salt's action on the ice (O7) loses the contrast. The entry records O5 "on firmer text" and O7 "toward". The reply's general point agrees with both, and neither moves away.
- **Part VII's odd-order skew-symmetric case** (point 3).
  - The contract is "remove skewness; remove oddness; remove both". With \(G\) the skewness commitment, deleting it leaves the family containing an invertible matrix (\(I_3\)) at the translated pair and at the baseline. The answers are then determined and equal, so the contrast is lost.
  - For the pair "remove oddness", the same block \(G\) serves, with \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) at both points after deletion. This holds whether or not oddness is a commitment or a boundary value in the named background (W20.1).
  - So L339 stays true, and "under removal of skewness" also names the removed commitment. The entry's REASON had already checked this. The reply itself calls it "not false" and "a blemish rather than a defect".
- **D3-T** (`tests/S89 Case book - candidate case D3-T, the controller that failed the test/final.md`). The discarded controller fails the test at a setting the tester uses. The case turns on selection and on which designs survive on \(H\) (Derivation 3), not on non-circular dependence. Its verdict, No, is unaffected on both texts.
- **The fallback.** The reply finds no worked case that the rider breaks, and its over-permissiveness check passes. So the fallback in W20.2's CHECK is not triggered.

## 5. Ruling: KEEP

- **Why.**
  - The only contest is a move the reply itself calls toward the fixed verdict and declared. On the texts, O33's ruled mark is AGREE on both file 11 and the draft. It rests on L151/L153 and L189, which R17 does not touch.
  - The "toward" the reply sees is the gain S88 recorded and the entry's GAIN names: accounts of paired-knob (input-only) contracts can now witness. The declaration's second sentence states that change.
  - The reply's premise, that the table's rows are commitments an edit could remove, misreads O33. The case's table is the question's form. S88 had already withdrawn the O33 flip on this point.
  - The reply's "at all" overstates the old defect. It holds on the mechanism-only reading, as the entry's REASON says.
  - The reply's check that "\(p\) because \(p\)" fails through S2 is right, and matches S88.
  - No fixed verdict is disputed (S90 rule 7).
- **KIND stays CLAIM.** The logical form of a defining clause changes, and that change is declared.
- **OLD, NEW, KIND, REASON WORD and the DECLARATION stand as drafted.**
- **Point 3 is not ruled as an edit.**
  - It names no claim change and no move. The sentence it concerns (revised L339) is unchanged, stays true, and was read by the entry's REASON.
  - It is passed to the orchestrator as an optional notation point. A possible wording: "witnessed by \(I_3\) under removal of skewness, with the skewness commitment as the deleted block, …". If adopted, it would be a new entry.
- **Mimo A1's point 4, the letter \(G\).** Nothing in Atria's reply bears on it, and this ruling does not take it up.
  - It stays with the orchestrator as batches 1 and 2 left it.
  - If the orchestrator adopts it, the new letter must also replace \(G\) in the fallback text in W20.2's CHECK. Neither \(\mathcal G\) nor \(g_0\) occurs elsewhere in the revised text. The DECLARATION says "block" and uses no letter.
- **For the CHECK field.** "After the cross-examination (S90, part A1): Atria's reply (pass 2, attempt 5) gave STANDS and named a move on O33, toward and declared; kept. O33's ruled mark rests on L151 and L189 ("faithful"), which S3 does not touch, and its table is the question's form, not a candidate (the O33 flip was withdrawn in S88). The move the reply names is the entry's GAIN, that accounts of input-only contracts can now witness. The reply's "'p because p' fails through S2" agrees with S88. Its point 3 (L339 names no block) is a notation point, passed on. Mimo's reply gave STANDS and did not contest the change."
- **Optional, for CASES AT RISK, O33.** Beside "holds AGREE", record the reply's "toward" reading: "toward for accounts of the joint question on the mechanism-only reading, which the case does not claim".
