# Ruling: s90_xexam_atria_C, R25 (W40.1)

*A fresh Claude checker, 24 September 2026. It works under the S90 rule, as extended by "S90 Parts - how they will be read, written before sending.md" (rules 2 and 3) and by "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (ruling 4: a pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list, and it did not write the part briefs.*

*The call.* Pass 2 was accepted on attempt 6 of 6. Attempts 1–5 had status 0 and brought nothing back. Attempt 6 had status 200, finish "stop", 0 bad chunks and END OF REPORT on its last line. The response sha256 bd51b785… matches the receipt, and the reply is 1,227 words by `wc -w`.

*What was read.*
- The whole Atria C reply, and the whole Mimo C reply (its point 5 is the one on R25). Parts rule 3 says each reply's argument is stated separately.
- The change list (md5 a5c92adc9f1e3806c0f9c6394cffde1e, as at 587eebf).
- The revised text (md5 9aecf2f30ce0b4523606b2b8409fdf37).
- File 11 (md5 5e494c1095d920d128b9a79de378f923, read only).
- The part C brief's R25 block and its section 4.
- The S81 book (md5 4f488d149e44669240d5db546c8e946a) and the S89 book (md5 b2e535777976a511935430bd089ba500).
- D3-T's final.md, searched only.

The sibling ruling on Mimo C's point 5 in the scratch folder was **not** opened.

## 1. The entry, its checkers' verdict and earlier rulings

W40.1, "Part VII: why the absent structure appears is a separate question". It is in Part VII, "Explanations that remove structure", at file-11 L337 and revised L335. GROUP C. REASON WORD clarification. **KIND: CLAIM.**

- **OLD:**

````text
This is the semantics' treatment of eliminative explanation; it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be.
````

- **NEW:**

````text
This is the semantics' treatment of eliminative explanation; it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be. Where the absent structure appears to be present, the question why it appears is a separate question with its own target and contract (Part III): an account of the absence neither answers that question nor needs to, and a bare denial, which offers no component that responds to a change in what produces the appearance, is not an account of it.
````

- **DECLARATION:** "Part VII now says that where an absent structure appears to be present, why it appears is a separate question with its own target and contract, which an account of the absence neither answers nor needs to answer, and of which a bare denial is not an account."
- **CHECK (the checkers' history):** "check 2, FIX." Check 2 replaced "Why does X appear?" with "the question why it appears". It also moved the anchor to after the paragraph's last sentence, which is kept byte for byte with its attack pointer (D9). No check 1 verdict is recorded, and no SOUND verdict. The table of check-2 fixes (change list L124) repeats the same two edits.
- **CASES AT RISK:**
  - "N22: toward. Wren offers no component for the appearance question. Yuri offers one …; the question does not ask whether that candidate is adequate."
  - "N8 holds … N25 holds."
  - "O34 was checked … does not move. No other O-case is eliminative."
- **The sources note** has an "Elimination" line that rests on this entry. Its fallback is "drop the sentence".
- **Earlier rulings:** none. Neither the batch-1 reading (Mimo A1, Mimo A2, Atria B1) nor the batch-2 reading (Atria A2, Mimo B1) mentions R25, W40.1 or N22, so there is nothing to reconcile.

## 2. The replies' arguments

**Atria C, point 3, task (d).** Its closing line is "R25: STANDS". It is contested under Parts rule 2 because it names a moved verdict. Point 3 is headed "declared moves toward the fixed verdicts; none away", and says:

> "R25 (line 335) on N22: Wren's bare denial "offers no component that responds to a change in what produces the appearance," so it is not an account of the appearance; Yuri's memory machinery supplies one, whether or not it is true — which is all the verdict asks."

**Mimo C, point 5, task (a).** Its closing line is also "R25: STANDS", but the point says the entry is under-declared:

> "The bracketed clause is what makes the denial "bare" — it is a structural criterion (no component with the right edit-signature for the appearance-producing mechanism, cf. Part II's "measurement's signature"). The declaration says only "a bare denial is not an account," leaving "bare denial" uncharacterised. A reader of the declaration alone could not tell which denials are excluded. Minor, but the characterisation is part of the claim."

Its repair: "Change "of which a bare denial is not an account" to "of which a denial that offers no component responsive to changes in what produces the appearance is not an account.""

## 3. The texts

**Quotations (S90 rule 8).**
- Atria's quotation is found at revised L335, and its line cite is right.
- Mimo's quotation of NEW is found at L335.
- Mimo's "measurement's signature" is found at revised L127, in Part II: "a part that reads or reports another part has a measurement's signature".

**"Bare" is defined only by the clause.**
- "bare" occurs once in the revised text, at L335, and never in file 11.
- "denial" occurs nowhere else in either text.
- So the non-restrictive clause "which offers no component that responds to a change in what produces the appearance" is the theory's only statement of what puts a denial under this exclusion.
- The clause is also a substantive claim in the theory's own terms: a condition on how a candidate's components respond under changes. The theory insists that no condition of (E) "inspects a label" (revised L265). It also says "The word 'table' settles nothing" (L269). The declaration as drafted states the exclusion through the label "bare" alone, and the text does not.

**The clause is true, and it follows from Part V.**
- The appearance question has a contract whose edits act on what produces the appearance.
- A candidate with no component that responds to those edits fails (F1) under that contract, as "a table of observed answers" does (L269).
- Or, where its only content is "people are mistaken", it restates the answer and fails non-circular dependence (L273).
- So "is not an account of it" is right, and the clause is its ground.
- The first half of NEW is Part III at revised L151: "Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other." The appearance question differs from the absence question at least in its query and contract. "Its own target" does not claim that the target differs, so the pointer "(Part III)" is sound.

**The standard of the batch-1 R51 rulings.** Those rulings kept an entry because the omitted phrase "makes no claim of its own": it restated clause (i), which the declaration already stated. That test fails here. The omitted clause is stated nowhere else in the text or in the declaration, and it is what gives the declared claim its reach.

**N22 (S89 book).** The question asks whether either theorist gives any reason why people believe and say they have inner experiences. Fixed verdict: "Wren gives none; Yuri gives one", and whether Yuri's reason is good "is another matter, and the question does not ask".
- **On file 11**, nothing speaks to appearances. At best, a careful reader derives Wren's half from Part III (L153) and Part V's exclusions. Otherwise the text is silent.
- **On the revised text, Wren:** "There are no inner experiences. People are mistaken about this." This offers no component that responds to a change in what produces the reports. By the clause it is a bare denial, and so it is not an account of the appearance. **Toward** the fixed verdict.
- **On the revised text, Yuri:** machinery that reads memories and produces reports is a component with a measurement's signature (L127). It responds to a change in what produces the appearance, so the exclusion does not reach it.
  - R25 does not say that Yuri's candidate is an account, and the verdict does not ask.
  - His standing as a candidate that "ordinary usage may still call an explanation" comes from R06 (L69), not from R25.
  - No move away.
- **What carries each half.** The declared half ("a bare denial is not an account") carries Wren's verdict only through the clause that classes Wren's words as a bare denial. The same clause is what separates Yuri from Wren. The drafters' own CASES AT RISK line argues the same way: "Wren offers no component …; Yuri offers one".
- **So is Atria's "declared move" declared?** It is declared in conclusion but not in ground. With the clause added to the declaration, it is fully declared.

**The other cases the entry names.**
- **N8** holds. It is obstruction (Part VII, "Obstruction", L331), and nobody alleges any appearance of a working machine.
- **N25** holds. Nothing is said to appear.
- **O34** holds. It supplies a meaning for a replacement query, which Part III covers at revised L161 / file-11 L163. It is not eliminative.
- **Other O-cases.** A search of the S81 book for "seem", "appear", "illusion", "mistaken" and "deny" finds no eliminative case.
- **D3-T** is not named, and has no appearance or denial content (searched).

**Mimo's repair is refused as worded.**
- It turns NEW's non-restrictive clause into a restrictive one.
- It paraphrases the clause ("responsive to changes").
- It drops the text's own term, "bare denial".
- A declaration should track NEW's words, so the fix below inserts NEW's clause verbatim into the drafted sentence and changes nothing else.

## 4. Ruling: FIX (declaration only; OLD, NEW and KIND unchanged)

- **OLD:** unchanged.
- **NEW:** unchanged.
- **KIND:** CLAIM, unchanged. **REASON WORD:** clarification, unchanged.
- **DECLARATION (exact):**

````text
Part VII now says that where an absent structure appears to be present, why it appears is a separate question with its own target and contract, which an account of the absence neither answers nor needs to answer, and of which a bare denial, which offers no component that responds to a change in what produces the appearance, is not an account.
````

- **CHECK (append):**

````text
After the cross-examination (S90: Atria C point 3, R25 STANDS, naming a declared move toward N22; Mimo C point 5, R25 STANDS, saying the declaration leaves "bare denial" uncharacterised): FIX, declaration only. The clause "which offers no component that responds to a change in what produces the appearance" is the only place in file 11 or the draft that says what makes a denial bare, and it is what puts N22's Wren under the exclusion and Yuri outside it; the declaration now carries it in NEW's words. OLD, NEW and KIND unchanged.
````

- **CASES AT RISK (append to the N22 line):** "Atria C (point 3) reads the same move toward; with the clause declared, both halves are accounted for."
- **Follows by program when the draft is rebuilt:**
  - the note's line for file-11 L337 takes the new declaration;
  - the counts, N and M are unchanged;
  - the list of what the checks changed gains a row for W40.1, as after the cross-examination (S90, Atria C point 3 and Mimo C point 5).
- **Conflicts:** none.
  - The sources note's "Elimination" line stays true, because it restates only the first half.
  - R06 (L69) agrees: Yuri's is a candidate.
  - No other entry has an OLD in L337.
