# 02 Reconciled difference reading: file 10 against file 11

**What this is.** The determiner's reconciliation of two independent Claude readings of how file 11 (`Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md`, the candidate) differs from file 10 (`Semantics/authority/10 Claude Fable Semantics - standalone theory.md`, the frozen authority). Reader 1 (R1) is `diffreader1.md`; reader 2 (R2) is `diffreader2.md`. Both are in this folder. Every place and every quotation was checked against the two files, and each disputed ruling was made from the texts.

**Written from the texts only.** Sources: file 10, file 11, the case book (`Semantics/tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`), the two readings, and the instruction head of briefs `s81_1C_A.txt` and `s81_1K_A.txt`. This was written before any 1D list or 2D audit was opened. Written by Claude, 23 September 2026.

**Blindness report.**
- Opened: file 10 and file 11 in full; the case book in full; diffreader1.md and diffreader2.md in full.
- Briefs, opened by exact path only:
  - Brief 1C, lines 1–80. Lines 1–75 are the instructions. Lines 76–80 are the first heading lines of the embedded theory.
  - Brief 1K, lines 1–84. Lines 1–75 are identical to 1C's, checked by `diff`. Lines 76–84 are the heading lines of its embedded theory.
  - One `grep -c` on each brief counted three strings: "Revision 1", "O48" and "bell does not explain the tide". I used the counts to check what the testers' copies contain (see XR2 and XR4). I read no returns.
- Seen, names only:
  - `ls` of `Semantics/authority/` showed files 00, 10, 11, 12 and NOT-IN-BUNDLE.md.
  - `ls Semantics/tests/ | grep S81` showed the names of the case book, the case-book provenance file, three S81 plan files, "S81 Stage 1 testing - file 11 against every case.md" and "S81 Stage 2 audit - check the Stage 1 return.md". None of these was opened.
  - `ls -la` of this folder showed reader1_O1-O26.md, reader1_O27-O52.md, reader2_O1-O26.md, reader2_O27-O52.md and wdiff.txt. None was opened. I made my own diffs instead, in `det_work/`.
  - A harness reminder displayed the parent session's task-list titles, with no content from any file.
- Nothing else under `Semantics/results/` was listed, opened or grepped. The project story, Status, README, INDEX, the S81 plans, the provenance file and the S76/S72 instruction files were not opened, and no git history was read.

**Method.**
1. I made a word-level diff (`git diff --no-index --word-diff`) and a sentence-level diff of scratch copies of the two files (`det_work/f10.md`, `det_work/f11.md`, `det_work/wd.txt`, `det_work/sdiff.txt`). Every changed sentence in the diff falls in one of the places below.
2. I aligned the two readings place by place.
3. A script checked every quotation in both readings against the files, with notation normalised. All matched. The only mismatches were LaTeX shown as Unicode, the capitalisation of fragments, bracketed glosses, and the readers' own paraphrases in quotation marks.

**Rulings.**
- **CLAIM**: file 11 asserts something file 10 does not state, or drops, re-scopes or re-conditions something file 10 states.
- **WORDING**: the same claim in different words, at the same place.
- **ORDER**: the same claim, moved or copied to another place.

The policy on restatements:
- A new sentence of file 11 that states a claim file 10 already states somewhere, at the same or wider scope, is ORDER. It is not CLAIM.
- A new sentence stating something file 10 leaves to inference is CLAIM, even when it is derivable. File 10 does not say it, and a tester reading file 10 must derive it.

In the CLAIM details a grade is added for the reader: *changed*, *new*, *application* (derivable, but first stated in file 11) or *meta* (about the document). The grade does not change the ruling.

**Granularity.** One place is one changed sentence or tight cluster. Punctuation-only changes form one group (C23).
- R1's D9 and D66 are folded into that group, and R1's D48 is split in two.
- R2's D22, D28, D32, D57 and D64 are split to R1's size.
- In this granularity R1 has 82 − 2 + 1 = 81 places and R2 has 81. The two cover the same 81 places.

---

## 1. Merged table

Line numbers are each file's own. "s2" means the second sentence on a line. "(weak)" marks a case the place bears on only indirectly. "—" means no case.

| id | file 10 location | file 11 location | ruling | found by | cases it could touch |
|---|---|---|---|---|---|
| C1 | absent | L5 revision note | CLAIM (meta) | both (R1 D1; R2 D1) | O48 named (the note is absent from the tester brief; XR2) |
| C2 | L11 | L13 | WORDING | both (D2; D2) | — |
| C3 | L13 | L15 | WORDING (borderline) | both (D3; D3) | O11 (weak: "blind") |
| C4 | L15 | L17 | WORDING | both (D4; D4) | — |
| C5 | L17 | L19 | WORDING | both (D5; D5) | — |
| C6 | L23 | L25 | WORDING | both (D6; D6) | — |
| C7 | L25 | L27 s1–s2 | CLAIM | both (D7; D7) | O12; O35, O38 (weak) |
| C8 | absent | L27 s3 | CLAIM | both (D8; D8) | O20, O21, O26, O27, O32, O39, O40, O50 |
| C9 | L516–525, L593–597 | L31–33 new section | ORDER | both (D10; D9) | O12 only through "invokes worth", ruled at C65 |
| C10 | absent | L37 | CLAIM (meta) | both (D11; D10) | none directly |
| C11 | L31–32 (G1) | L39 | WORDING | both (D12; D11) | — |
| C12 | L34–35 (G2) | L41 | WORDING | both (D13; D12) | O10 (no change) |
| C13 | L37–38 (G3) | L43 | CLAIM | both (D14; D13) | O48, O24 |
| C14 | L40–41 (G4) | L45 | WORDING | both (D15; D14) | — |
| C15 | L43–44 (G5) | L47 | WORDING | both (D16; D15) | — |
| C16 | L46–47 (G6) | L49 | WORDING | both (D17; D16) | — |
| C17 | L49–50 (G7) | L51 | WORDING | both (D18; D17) | — |
| C18 | L52–53 (G8) | L53 | WORDING | both (D19; D18) | — |
| C19 | L55–56 (G9) | L55 | WORDING | both (D20; D19) | — |
| C20 | L58–59 (G10) | L57 | WORDING | both (D21; D20) | — |
| C21 | L61–62 (G11) | L59 | WORDING | both (D22; D21) | — |
| C22 | L64–78 attack list | L61–63 summary | ORDER | both (D23; D22) | O48 (weak: the L63 short form is unqualified) |
| C23 | L27, 84, 90, 122, 138, 158, 168, 190, 284, 286, 298, 412, 521, 581, 617, 623, 625; grievance layout | L29, 69, 75, 107, 123, 143, 153, 177, 271, 273, 283, 399, 512, 574, 610, 616, 618; L39–59 | WORDING (punctuation and markup group) | both (R1 D9, D24, D66; R2 D68) | — |
| C24 | L136 | L121 | WORDING | both (D25; D25) | O10 (no change) |
| C25 | absent (after L144) | L129 s4–s5 | CLAIM | both (D26; D26) | O4, O6, O9 |
| C26 | absent (L168) | L153 last | CLAIM | both (D27; D27) | O4, O6; O9 (weak) |
| C27 | L174 heading | L159 heading | WORDING | both (D28; in D28) | — |
| C28 | L41, L272 | L161 s1 | ORDER (disputed: R2 CLAIM) | both (D29; D28 s1) | O1, O5, O8 (claim unchanged) |
| C29 | L41, L168, L268, L378, L456 | L161 s2 | ORDER (disputed: R2 CLAIM) | both (D30; D28 s2) | O1, O5, O8 (claim unchanged) |
| C30 | absent | L161 s3 | CLAIM | both (D31; D28 s3) | O1, O5, O8 |
| C31 | absent (L176) | L163 last | CLAIM | both (D32; D29) | O34 |
| C32 | L210 | L197 last | CLAIM | both (D33; D30) | O48, O24 |
| C33 | absent (L226) | L213 last | CLAIM | both (D34; D31) | O28, O16, O29 |
| C34 | L238 s3–s4 | L225 s3 | WORDING | both (D35; in D32) | O3 (no change) |
| C35 | absent | L225 last | CLAIM | both (D36; D32 last) | O48, O24; O3 (weak) |
| C36 | L260 | L247 | WORDING | both (D37; D33) | — |
| C37 | L282, L292 headings | L269 heading | ORDER | both (D38; D34) | — |
| C38 | L284 s2 | L271 s2–s3 | CLAIM | both (D39; D35) | O33, O2 (low) |
| C39 | L286 (content from L338) | L273 s2 | ORDER (disputed: R2 WORDING) | both (D40; D36) | O4, O6 (claim unchanged) |
| C40 | L288 | L275 s2 | CLAIM | both (D41; D37) | O2 |
| C41 | L294 s1–s2 | L279 s1–s2 | WORDING | both (D42; D38) | — |
| C42 | absent | L279 s3 | CLAIM | both (D43; D39) | O7 |
| C43 | L316 | L301 s2 | CLAIM | both (D44; D40) | O36 |
| C44 | L322 | L307 last | CLAIM | both (D45; D41) | O47 |
| C45 | L324 | L309 s3 (pointer at s2) | CLAIM | both (D46; D42) | O45, O46 |
| C46 | L352 | L337 | WORDING | both (D47; D43) | — |
| C47 | absent | L363 s1 | CLAIM | both (D48; D44) | O43; O28 (weak) |
| C48 | absent | L363 s2 | CLAIM | both (D48; D45) | O44 |
| C49 | L384 | L371 last | CLAIM | both (D49; D46) | O52, O25, O19; O13 (weak) |
| C50 | L406 | L393 last | CLAIM | both (D50; D47) | O16, O29; O37 (weak) |
| C51 | L412 | L399 last | CLAIM | both (D51; D48) | O14 |
| C52 | L414 | L401 s4 | CLAIM | both (D52; D49) | O3 |
| C53 | L414 | L401 s5 | CLAIM | both (D53; D50) | O18, O31; O15, O11 (weak) |
| C54 | L430 | L417 last | CLAIM | both (D54; D51) | O23; O33 (weak) |
| C55 | absent | L419 Ownership | CLAIM | both (D55; D52) | O17, O21, O27, O30, O40, O41, O49, O50, O51; O3, O14, O18, O31 (weak) |
| C56 | L438–444 | L433 s1 | CLAIM (named place ii) | both (D56; D53) | O35, O38 |
| C57 | L444 | L433 s2 | CLAIM | both (D57; D54) | O12; O35, O38 (weak) |
| C58 | absent (ProducedBy undefined, L441) | L433 s4 | CLAIM | both (D58; D55) | O13, O20, O25, O26, O32, O39, O52; O21, O27, O40, O50 |
| C59 | absent | L433 s5 | CLAIM | both (D59; D56) | O13 |
| C60 | L458 (heading and N) | L447 heading, s1–s2 | CLAIM | both (D60; D57) | O12; O35, O38 (weak) |
| C61 | L458 last | L447 last clause | CLAIM | both (D61; quoted inside R2 D57) | — |
| C62 | absent | L465 | CLAIM | both (D62; D58) | O42, O30, O41, O51; O17 (weak) |
| C63 | L476 | L467 last | CLAIM | both (D63; D59) | O49, O17 |
| C64 | L482 | L473 last | CLAIM | both (D64; D60) | O48 |
| C65 | L519 | L510 | CLAIM | both (D65; D61) | O12 |
| C66 | absent | L514 Declared inputs | CLAIM (named place iii) | both (D67; D62) | O35, O38, O1, O5, O8, O17, O21, O27, O30, O40, O50, O41, O42, O51; O3, O14, O18, O31 (weak) |
| C67 | L525 | L518 last | CLAIM | both (D68; D63) | O37, O49, O17 |
| C68 | L66, L545 | L526 | ORDER | both (D69; in D22) | — |
| C69 | L68, L533 | L528 s1–s2 | ORDER | both (D70; in D22) | — |
| C70 | L68 (and L284) | L528 s3 | CLAIM | both (D71; D24) | O2, O33 (low) |
| C71 | L70, L535 | L530 | ORDER | both (D72; in D22) | — |
| C72 | L72, L537 | L532 | ORDER | both (D73; in D22) | — |
| C73 | L74, L539, L541 | L534 | CLAIM (limb 1; limbs 2–3 ORDER) | both (D74; D23) | O48, O24 |
| C74 | L76 | L536 | ORDER | both (D75; in D22) | O12 (no change) |
| C75 | L567 D3 title | L560 | CLAIM | both (D76; in D64) | O48 |
| C76 | L569 D3 Claim | L562 | CLAIM | both (D77; in D64) | O48, O24 |
| C77 | L571 D3 Proof | L564 | CLAIM | both (D78; in D64) | O48 |
| C78 | L573 D3 Consequence | L566 | CLAIM | both (D79; in D64) | O48, O24; O3 (weak) |
| C79 | L589 | L582 last | CLAIM | both (D80; D65) | O12 |
| C80 | L593 | L586 | CLAIM | both (D81; D66) | only through C66 |
| C81 | L623 | L616 | CLAIM | both (D82; D67) | — |

Cases touched by no CLAIM place: O10 and O22. O11 is touched only weakly (C3 wording; C53).

---

## 2. Where the readers differ, and single-reader places

**Found by only one reader: none.** All 81 places are in both readings, R2 at a coarser grain.

**Disputed rulings: three places.** In all three I rule with R1, for the reasons below. Both readings are kept.

**C28** (f11 L161 s1): "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one."
- R1: ORDER, a restatement of non-vacuity. R2: CLAIM (X), a restatement of F10 272.
- File 10 states this twice. G4, L41: "A contract is a declared subset of those." Non-vacuity, L272: "The contract \(C\) is a declared subset of the physically admitted edits, and every physically admitted edit excluded from \(C\) is excluded by a stated scope, not silently."
- "A stated scope is what makes it one" is the same requirement as "excluded by a stated scope", seen from the declaration side. No scope, condition or quantifier changes.
- **Ruling: ORDER**, a copy into Part III. R2's grading key counts restatements from another place as X, and so as CLAIM. That is a policy difference, not a difference in how the text is read.

**C29** (f11 L161 s2): "An account at a stated scope answers the question asked at that scope; it does not answer a broader question that failed, and a narrowing adopted after a failure is a new claim at a new index (Part VIII)."
- R1: ORDER. R2: CLAIM (X), generalising F10 456 and Part VIII.
- File 10 states each part at equal or wider scope:
  - G4, L41: "An account is scoped to its contract and says so."
  - L168: "Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other." A broader question is a different \(C\).
  - L268: "an account of a different query is not an account of this one."
  - L378: "A new index is a new claim." This is general.
  - L456: "A later narrowing of that contract to rescue adequacy is a new claim at a new index". This is the (EK) instance.
- Widening L456 beyond (EK) needs only L378 together with "the contract \(C\) [is a] declared ind[ex]" (L523). File 10 therefore asserts the general proposition.
- **Ruling: ORDER.** Bearing on O1, O5 and O8: none beyond file 10. That bearing comes from C30 and C66.

**C39** (f11 L273 s2): "It may be faithful under the identification contract, which is a different question (Part III)."
- R1: ORDER. R2: WORDING.
- File 10's Part V sentence at L286 had no such clause. The content comes from Part VII, L338: "It is faithful under the identification contract, whose edits alter the observed \(L\)." File 11 keeps that sentence at L323.
- The hedged general "may be" is witnessed by that example, so nothing new is asserted. The claim is copied to a new place, not reworded in place.
- **Ruling: ORDER.**

**Grade differences inside agreed CLAIM rulings.** These are informational only. R1 grades as application what R2 grades as S at C42 and C49. R1 grades as new what R2 grades as X at C50, C57, C59 and C79. R1 grades C81 as changed; R2 grades it X. My grades are in section 3.

**Quotation and description checks.**
- Every line number both readers give was checked and is right.
- One descriptive slip, R2 D53: "'Fixed for the comparison' becomes 'declared inputs'". File 11 keeps "fixed for the comparison" at L427 and adds "declared inputs" at L433, so both phrases stand. The slip does not affect R2's ruling.
- R1's D24 group omits two markup spots that R2's D68 lists: the bold at L271 and the dashes at L273. Both are WORDING, inside C23.

**Points in neither reading, added by me.**
1. **C1 / named place i.** The note says the old proof "already assumed the qualification". Whether that is true depends on how file 10's "surviving on \(H\)" is read (see section 5 (i)).
2. **C78.** R1 sees a tension in the unqualified "This is why the primitive layer is fallible". I find no tension. A value the population fixes can still be wrong, as Derivation 10 shows, so fallibility does not need underdetermination.
3. **C55 / C66.** Weak touches on O3 ("it is her own"), O14 ("by his own effort"), O18 ("The one tooth is hers") and O31 ("The correction is hers"). Ownership now needs a declared boundary, and none is declared in these cases.
4. **C47.** A weak touch on O28. The reader-convention criterion bears on retraining a reader from the copy.
5. **XR2, XR4.** A check of what the testers' copies contain. The revision note is absent from the file-11 brief. The bell-and-tide phrase is present in the file-11 brief and absent from the file-10 brief.

---

## 3. Details per CLAIM place

**C1. Revision note (f11 L5). CLAIM, meta.**
- Quoted: "*Revision 1 (file 11), 22 September 2026. A rewrite of file 10 for coherence: the same primitives, definitions, conditions, constructions and derivations … One claim changes: Derivation 3, whose unqualified form gave the wrong verdict on the audit's case O48 and whose proof already assumed the qualification (Semantics results S75). The three sentences that restated it (the answer to grievance 3, attack point (D), the Part XV entry) change with it. Nothing else changes in what is claimed.*"
- These are new assertions about the document, and three of them are false or incomplete against the texts:
  - (a) "the same … definitions, conditions". File 11 adds definitions that file 10 lacks: Ownership (L419), ProducedBy (L433), System boundary and continuity (L465), the population (L473) and Declared inputs (L514).
  - (b) "One claim changes" and "Nothing else changes". There are 46 CLAIM places inside the theory.
  - (c) The list of restating sentences follows file 10's layout (XR1) and leaves out C32, C35, C64 and C81.
- On "already assumed the qualification", see section 5 (i).
- Cases: O48 is named. The note is not in the tester brief for file 11 ("Revision 1" occurs 0 times in s81_1C_A), so the naming did not reach testers.

**C7. Front matter, "does not claim" (f10 L25 / f11 L27 s1–s2). CLAIM, changed.**
- f10: "It does not supply an objective aesthetics, a probability of truth, a merit function, or a ranking of thinkers. It supplies places where such things would go if anyone had them, and marks those places as empty."
- f11: "It does not supply an objective aesthetics, a probability of truth, a merit function, a measure of worth, or a ranking of thinkers. Where a claim needs one of these, the semantics takes it as a **declared input** and marks the place (Parts XI, XIV)."
- There are three changes:
  - "a measure of worth" is added to the list.
  - The empty place becomes a declared input. Under L514, a missing declared input makes the verdict "unsettled".
  - The body carries this only for worth and aesthetics, through \(\mathcal N\). It does not carry it for a probability of truth, a merit function or a ranking (XR3).
- Cases: O12 ("its merit is real"). O35 and O38 weakly ("in every way that mattered", "Whether four seconds mattered").

**C8. Division of credit (f11 L27 s3). CLAIM, new.**
- f11: "It does not supply a division of credit among contributors beyond what a history establishes (Part XI)."
- File 10 has no statement on credit anywhere.
- It supports the fixed verdicts of O20, O26, O32, O39 and O40 ("Neither can say "mostly"").
- It bears against "mostly" in O21, O27 and O50 unless the history establishes the division.

**C10. Reading rule (f11 L37). CLAIM, meta.**
- f11: "Each answer points at the part of the document that carries it; the front matter states nothing the body does not state more exactly."
- A new rule that gives the body precedence. It is not true of L27 (C7, XR3).
- It can decide which sentence a tester follows where the front matter and the body differ. No case directly.

**C13. Grievance 3 (f10 L38 / f11 L43). CLAIM, changed.**
- f10: "There is a theorem below (Derivation 3) that selected transports are *always* underdetermined on unseen changes."
- f11: "Derivation 3 says that a selected transport is underdetermined by its history on an unseen change wherever its population admits a differing survivor there."
- The quantifier changes from every unseen change to only those where the population admits a differing survivor.
- Cases: O48, O24. See section 5 (i).

**C25. Reading part (f11 L129). CLAIM, application.**
- f11: "In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording."
- Grounds in file 10: L141 (measurement signature), L126 (observation role) and L338 (direction from edits).
- The rule for reporting parts, and "not by the account's wording", are first stated here.
- Cases: O4 (recalibration), O6 (the thermometer warmed in the hand), O9 (the bent needle). All can move from SPLIT to AGREE.

**C26. Measure against production (f11 L153 last). CLAIM, application.**
- f11: "A measure that identifies an outcome, with a reliable prediction from it, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second."
- It applies f10 L168. The wording tracks O4's verdict closely ("a useful measure and a reliable prediction").
- Cases: O4, O6; O9 weakly.

**C30. Appropriateness of a restriction (f11 L161 s3). CLAIM, new.**
- f11: "What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it."
- File 10 has no such abstention. With C66, appropriateness becomes a declared input, and a missing input makes the verdict unsettled.
- Cases: O5 ("This is a legitimate narrowing") and O1 ("the series as a whole is a retreat") can move toward SILENT. O8 is weak ("an honest scope" may rest on scope stated from the start).

**C31. Replacement query (f11 L163 last). CLAIM, application.**
- f11: "Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one."
- It applies f10 L168 and L268. "Can make a coherent new question" is first stated here.
- Case: O34 ("A meaning has been supplied … It is not what Lea asked").

**C32. Selected: the population is part of the claim (f11 L197). CLAIM, changed (Derivation 3 cluster).**
- f11: "The population \(\mathcal T\) is part of the claim: what \(H\) leaves open about \(t\) is what \(\mathcal T\) leaves open (Derivation 3)."
- In file 10 the population is only a component of Sel. Here it is made to bound what is open. The revision note does not name this place.
- Cases: O48, O24.

**C33. Provenance without access (f11 L213 last). CLAIM, new.**
- f11: "A carrier keeps its provenance when present access to it is lost, and a later record derived from the carrier is not a second, independent witness to its history."
- Cases: O28 ("The provenance is intact; the access is not"), O16 ("the diary is a second copy of the first"), O29.

**C35. Surprise and the population (f11 L225 last). CLAIM (Derivation 3 cluster).**
- f11: "Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3)."
- New, and not named in the revision note.
- Cases: O48, O24; O3 weakly (surprise).

**C38. The encoding table "is an account" (f10 L284 / f11 L271). CLAIM, changed.**
- f10: "A table that genuinely encodes an organization's response to every admitted change is not a table in that sense and is not excluded."
- f11: "A table that genuinely encodes an organization's response to every admitted change is not a table in that sense: it satisfies (F1) as a decomposition does, and it is an account. The word "table" settles nothing; the response under the admitted changes does."
- File 10 says only that the table clause does not exclude it. File 11 asserts (F1) and Account, which means all of (E), without checking (A), non-circular dependence or non-vacuity.
- Cases: O33 ("The table is faithful") and O2 (the almanac stays a table of observed answers). Both low.

**C40. Restated answer packaged with a real dependence (f11 L275 s2). CLAIM, new.**
- f10 L288: ""\(p\) because \(p\)" fails non-circular dependence."
- f11 adds: "So does an account whose only substantive component restates the answer it was asked for; packaging a genuine dependence that answers a different question beside it does not repair this (the bell does not explain the tide)."
- File 10's non-circular condition (L270) has two clauses that can pull apart here. "does not appear … as a component" excludes such an account. "There exists \((a,b)\in C\) that removes or replaces a nonempty block of \(\Gamma\) … under which the answer profile changes" can be met by removing the packaged block. File 11 closes this.
- The parenthesis names O2's content (XR4).
- Case: O2, which can move from SPLIT to AGREE.

**C42. Coarse dependence (f11 L279 s3). CLAIM, application (R2: S).**
- f11: "It does not reject a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question, and its strength is fixed by its contract, not by what a finer contract would add."
- Grounds in file 10: level-indexing (L35) and "depth is question-relative" (L294). "Or an instrument" tracks O7.
- Case: O7.

**C43. Criticality relative to the support written (f11 L301 s2). CLAIM, new.**
- f11: "Criticality is relative to the support \(W\) it is assessed in: a commitment critical in one successful support need not be critical in the full candidate, and the supports assessed are the ones actually written, not a support someone could write in their place."
- The first clause follows from (B). The second is new.
- Case: O36.

**C44. The monotone theorem's reach (f11 L307 last). CLAIM, application.**
- f11: "The theorem applies only where its assumptions hold; an addition to \(\Gamma\) that destroys a support is the interference case below, and there upward closure fails."
- File 10's Interference paragraph shows the failure. It never says that an addition is that case.
- Case: O47 ("additions could not always be made without loss").

**C45. A route present from the start, and reassignment (f11 L309 s3). CLAIM, new.**
- f11: "A route already present in the candidate is a route whether or not anyone has described its work; a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment, and the new candidate's success is not the old one's."
- The added pointer "(Derivation 9)" is WORDING.
- Cases: O45, O46.

**C47. Recoding, sentence 1 (f11 L363 s1). CLAIM, new.**
- f11: "A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing (Derivation 8)."
- Derivation 8 covers structure-preserving bijections of all data. The reader-convention criterion is new.
- Cases: O43; O28 weakly.

**C48. Recoding, sentence 2 (f11 L363 s2). CLAIM, new.**
- f11: "A section of a carrier filled from another source keeps that other source's history, whatever it happens to match."
- Case: O44.

**C49. Inactive routes (f11 L371 last). CLAIM, application and new.**
- f11: "A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result."
- The first clause is near f10's "nonconstant dependence … joining a represented input to an operative result". "Already at rest" and "read from the history" are new.
- Cases: O52, O25, O19; O13 weakly.

**C50. Reconstructed record (f11 L393 last). CLAIM, application.**
- f11: "A record reconstructed from the claim it is meant to support is not a receipt for that claim."
- It is near f10's rule that a leaf references an event.
- Cases: O16, O29; O37 weakly.

**C51. Narrow retained use (f11 L399 last). CLAIM, new.**
- f11: "A narrow retained use is what it is: it establishes neither the wider understanding it falls short of nor a permanent inability to reach it."
- Case: O14 ("has yet to understand").

**C52. First representation without observation (f11 L401 s4). CLAIM, new.**
- f11: "A first representation may be constructed from an available problem without prior observation of what it represents."
- Case: O3.

**C53. Small binding in received content (f11 L401 s5). CLAIM, new.**
- f11: "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance."
- File 10's Build (L414) requires a "nontrivial binding construction" and says nothing about the rest.
- Cases: O18, O31; O15 and O11 weakly.

**C54. A dimension mentioned in passing (f11 L417 last). CLAIM, new.**
- f11: "A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction."
- Cases: O23; O33 weakly.

**C55. Ownership (f11 L419). CLAIM, new definition.**
- f11: "The subhistory in Build is owned by \(s\) when its processes run inside the system boundary and resource contract declared for \(s\) (Part XII). Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing. Ownership is not defined by the capability it is meant to ground (Part XII)."
- File 10 uses "owned" (L414, L476, L488, L493) without defining it.
- The wording tracks particular cases: "decisive question" (O21), "instruction about what to read" (O41), "whoever wrote it" (O30), "casing" (O51).
- Cases: O17, O21, O27, O30, O40, O41, O49, O50, O51. Weakly O3, O14, O18 and O31, where "her own", "his own effort" and "hers" are asserted with no declared boundary.

**C56. Repair occasions clause (f11 L433 s1). CLAIM, changed. Named place ii; see section 5.**

**C57. Declaration makes no claim of worth (f11 L433 s2). CLAIM, application or new.**
- f11: "Their declaration makes no claim that the aims are worth pursuing, and (P) does not rank alternatives."
- File 10 has only the second clause.
- Cases: O12; O35 and O38 weakly ("mattered").

**C58. ProducedBy and credit (f11 L433 s4). CLAIM, new definition.**
- f11: "\(\operatorname{ProducedBy}\) holds when an active route (Part IX) runs from \(\Delta\) to the repair; it credits each contribution the history establishes, and where two sufficient contributions both ran, both are credited and the history supplies no division of credit that it does not contain."
- In file 10, ProducedBy occurs only inside (P) (L441) and is never defined.
- Cases: O13, O20, O25, O26, O32, O39, O52. O21, O27, O40 and O50 wherever "mostly" is claimed.

**C59. Three attributions (f11 L433 s5). CLAIM, application.**
- f11: "A correct account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions."
- It is implicit in the separate Account and ProducesVia conjuncts of (EK).
- Case: O13.

**C60. Worth, and the normative relation (f10 L458 / f11 L447). CLAIM, changed.**
- f10 heading: "**Artistic effect, purpose, and aesthetic reason.**" f10 text: "a normative relation \(\mathcal N\subseteq A\times K\times\mathcal Rsn\times\mathcal V_A\) declared as a substantive input when aesthetic value is claimed."
- f11: "**Worth, and the normative relation.** Repairing an obligation establishes that it was repaired; it establishes nothing about whether the obligation, or the question that led to it, was worth having. Where a claim invokes worth, the semantics takes a **normative relation** \(\mathcal N\) as a declared input and marks the place (Part XIV)."
- \(\mathcal N\) is widened from aesthetic value to any claim of worth, and repair is separated from worth.
- Cases: O12 (toward SILENT without \(\mathcal N\)); O35 and O38 weakly.

**C61. No aesthetics from achievement (f11 L447 last clause). CLAIM, application.**
- f11: "…, and no aesthetics follows from achieving a stated effect."
- File 10 says "None is defined as another", meaning not defined. File 11 says nothing follows, which is stronger.
- No case.

**C62. System boundary and continuity (f11 L465). CLAIM, new.**
- f11: "A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change). A replaced part that preserves the declared continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it; a process run outside it is not the system's however close it sits. Both are declared before the attribution, not chosen after it."
- File 10 has \(\beta\) and \(\Omega\) only as indices (L523).
- Cases: O42, O30, O41, O51; O17 weakly.

**C63. The ground of ownership (f11 L467 last). CLAIM, new.**
- f11: "Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed: "owned because it can, and can because owned" grounds neither."
- Cases: O49, O17.

**C64. The population defined (f11 L473 last). CLAIM, new (Derivation 3 cluster).**
- f11: "The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it."
- This is a new definition, not named in the revision note. It decides O48 nearly word for word ("every device in the stated population is built without that wire").
- Case: O48.

**C65. Primitive 2 (f10 L519 / f11 L510). CLAIM, changed.**
- f10: "The **normative relation** \(\mathcal N\), when a question invokes one."
- f11: "The **normative relation** \(\mathcal N\), when a question invokes worth. It is taken as an input and never derived; the aesthetic relation of Part XI is one instance."
- The scope changes from "invokes a normative relation" to "invokes worth". "Never derived" restates f10 L458.
- Case: O12.

**C66. Declared inputs (f11 L514). CLAIM, new. Named place iii; see section 5.**

**C67. Well-founded order (f11 L518 last). CLAIM, new.**
- f11: "The order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply it counts only when the account uses it."
- Cases: O37 ("The textbook proof would break the circle, and the account has not used it"), O49, O17.

**C70. Sufficiency: the encoding table is not a counterexample (f11 L528 s3). CLAIM, changed.**
- f10 L68: "The classic attempts — lookup tables, reversed calculations, conclusion-as-premise — all fail one of the four; a new one must fail none."
- f11: "A table that encodes the response to every admitted change fails none and is an account, so it is not a counterexample; a new attempt must fail none and still explain nothing."
- This is the Part XV copy of C38, with one further effect. Under file 10, such a table was "not excluded", and so it stayed open as a possible counterexample to sufficiency (L533). File 11 declares it an account and removes it from what could refute (A).
- Cases: O2, O33. Both low.

**C73. (D) Genesis, first limb (f10 L74, L539 / f11 L534). CLAIM, changed. See section 5 (i).**
- The second and third limbs are ORDER:
  - Construction reduced to selection: f10 L541 and L74.
  - The primitive layer: f10 L74.

**C75–C78. Derivation 3: title, Claim, Proof, Consequence (f10 L567–573 / f11 L560–566). CLAIM, changed. See section 5 (i).**

**C79. Derivation 5 consequence (f11 L582 last). CLAIM, application of C60.**
- f11: "That a question was found says nothing about its worth (Part XI)."
- Case: O12. "Noor found a better question" is supported; "its merit is real" needs \(\mathcal N\).

**C80. Derivation 6 claim (f10 L593 / f11 L586). CLAIM, changed.**
- f10: "…together with declared indices."
- f11: "…together with declared indices and declared inputs."
- The base of every definition widens. The proof is unchanged (XR6). Cases: only through C66.

**C81. Derivation 10 gloss (f10 L623 / f11 L616). CLAIM, new interpretive clause (Derivation 3 cluster).**
- f11: "…the fidelity failure is structural, not parametric, and this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change."
- Not named in the revision note. The gloss is inexact (XR7). No case.

---

## 4. Cross-references

Both readers listed every internal pointer in file 11. My own pass (grep of every "Part", "Derivation", "attack" and "grievance" pointer, and each bracketed tag) agrees with them. Every pointer carried over from file 10 still lands. The rows below are every pointer that either reader ruled other than plainly CORRECT, or remarked on.

| id | f11 line | pointer | R1 | R2 | reconciled |
|---|---|---|---|---|---|
| XR1 | L5 | "(the answer to grievance 3, attack point (D), the Part XV entry)" | SLIP | SLIP | **SLIP** |
| XR2 | L5 | "the audit's case O48", "(Semantics results S75)" | flagged as external, no ruling | not listed as a pointer (O48 naming noted at D1) | **SLIP**, dangling outside the document, with a steering flag |
| XR3 | L27 | "(Parts XI, XIV)" | SLIP | SLIP | **SLIP** |
| XR4 | L275 | "(the bell does not explain the tide)" | SLIP | not listed as a pointer (noted in D37) | **SLIP**, dangling example, with a steering flag |
| XR5 | L447 | "as a declared input and marks the place (Part XIV)" | CORRECT, with a note | SLIP | **SLIP** |
| XR6 | L588 | "By the dependence order of Part XIV" | CORRECT, with a note | SLIP | **SLIP** |
| XR7 | L616 | "Derivation 3's qualification seen from the other side" | CORRECT (loose) | SLIP | **SLIP** |
| XR8 | L528 | "(E)" beside the "(E) Question-finding" heading; "four conditions of (E)" | CORRECT, with a note | CORRECT | **CORRECT** |
| XR9 | L363 | "(Derivation 8)" | CORRECT (loose) | CORRECT | **CORRECT** |
| XR10 | L33 | "in the order Part XIV states" | CORRECT | CORRECT, with a note | **CORRECT** |
| XR11 | L534 | "(against Derivation 3; …)" | CORRECT | CORRECT | **CORRECT** (the claim-level issue is at C73) |
| XR12 | L63 | "stated exactly in Part XV"; "(A)–(E)" | CORRECT | CORRECT | **CORRECT** (the (D) short form is unqualified, noted at C22) |

**Checks of the rows that are not CORRECT.**

- **XR1, SLIP.** The list follows file 10's layout, where the three sentences were separate: L38, L74 and L539.
  - In file 11, attack point (D) and the Part XV entry are one passage (L534). If "attack point (D)" means the Part 0 short form at L63 instead, that sentence did not change: it still says "the underdetermination of selected transports" without the qualification.
  - Either way the pointers do not fit file 11. The note's statement (a meta claim, C1) is not changed by that.

- **XR2, SLIP with a steering flag.** Both references point outside the theory. "Audit" is not defined in the theory, and S75 is not part of it.
  - For a tester, "case O48" would land on the case book's O48, and the note tells the tester which way the old theorem erred there.
  - A grep shows the note is absent from the file-11 brief ("Revision 1": 0 occurrences in s81_1C_A). The steering therefore did not reach testers.
  - The pointer does not change what the note claims.

- **XR3, SLIP.** Checked against Part XI (L447) and Part XIV (L510, L514):
  - Worth, the aesthetic case and \(\mathcal N\) are carried.
  - A probability of truth is carried nowhere.
  - A merit function and a ranking of thinkers are carried only if read as claims of worth.
  - The pointer covers less than the sentence. The sentence's claim is set by its own words (C7).
  - Read with L37 ("the front matter states nothing the body does not state more exactly"), the uncovered items are left without body support. That effect comes through L37, not through the pointer.

- **XR4, SLIP with a steering flag.** The document contains no bell and no tide. The parenthesis is O2's content: "the harbour bell rings".
  - A grep finds the phrase once in the file-11 brief and not at all in the file-10 brief. It therefore reached the file-11 testers inside the theory text.
  - The rule in the sentence stands without the parenthesis, so this is not claim-changing. The substantive change is ruled at C40.

- **XR5, SLIP.** Part XIV's own terms put \(\mathcal N\) among the two primitives (L510). "Declared inputs" (L514) opens "Besides the two primitives", which excludes \(\mathcal N\). Part XI (L447) and Part 0 (L27) nevertheless call \(\mathcal N\) "a declared input".
  - The pointer lands on the right place, but the target classifies differently from the sentence.
  - It is not claim-changing. Either way \(\mathcal N\) is an input the semantics does not supply, and no worth verdict follows without it. For O12 the practical effect is the same whether or not L514's "unsettled" rule formally covers \(\mathcal N\).

- **XR6, SLIP.** The Derivation 6 claim (L586) now includes "declared inputs". The dependence order the proof cites (L518) lists no declared input. It also lists none of the new definitions that rest on declared inputs: Ownership (L419), ProducedBy (L433), System boundary and continuity (L465).
  - The pointer lands on the paragraph it names, but that paragraph no longer covers the widened claim. The gap is a proof gap, and the claim is set by its words.
  - R1's CORRECT-with-gap reading records the same fact under the other ruling.

- **XR7, SLIP.** Derivation 3's qualification (L562–564) is the case where \(\mathcal T\) holds no survivor of \(H\) that differs from \(t\) at the unseen pair. Then "\(H\) is silent … and the population fixes it".
  - Derivation 10's case is that no member survives the extended history, meaning none is faithful at the occlusion.
  - The two coincide only if every \(H_0\)-survivor agrees at the occlusion, and Derivation 10 does not state that. Occupancy-only predictors that differ among themselves at the occlusion fall under Derivation 3's main clause, and all of them still fail.
  - R1's "CORRECT (loose)" reading holds that the population fixes the untested value and fixes it wrongly. That reading is available, but it needs the unstated premise.
  - Derivation 10's conclusions do not depend on the gloss, so it is not claim-changing.

- **XR8, CORRECT.** "Four conditions" is Part V's own count at L233: component fidelity, which is (F1) and (F2); question fidelity; non-circular dependence; non-vacuity.
  - The labels (A)–(E) collide with the body tags (A), (B), (D) and (E). That collision existed in file 10's Part 0 attack list; in file 11 it has moved into Part XV.
  - "attack (B) in Part XV" (L337) resolves it.

**Pointers in file 10 dropped or retargeted by file 11.** Both readers agree, and I confirm:
- "listed under attack (B)" (f10 L352) is retargeted to "attack (B) in Part XV" (f11 L337). CORRECT.
- The attack pointers move into Part XV with their targets: Part V, Part VII, Derivation 1, Derivation 3 and Part IV.
- (E) gains "(against Derivation 5)" (L536).
- The only sentence dropped outright is "Derivation 1 says this is impossible" (f10 L72). Its content survives as "This refutes Derivation 1" (L532), so nothing is lost.

**CLAIM-CHANGING pointers: none.**

---

## 5. The three named places

**(i) Derivation 3 and the three sentences restated with it. Reconciled ruling: CLAIM at every location.** Both readers agree.

The theorem itself:
- **Title** (C75). "Selected transports are underdetermined on unseen changes" becomes "… on unseen changes their population leaves open".
- **Claim** (C76).
  - f10 L569: "For every \((a,b)\in C\setminus H\) there exists a transport \(t'\), also surviving on \(H\), with a different value at \((a,b)\)."
  - f11 L562: "For every \((a,b)\in C\setminus H\) at which some \(t'\in\mathcal T\), also surviving on \(H\), has a different value from \(t\), the value of \(t\) at \((a,b)\) is underdetermined by \(H\): survival on \(H\) does not distinguish \(t\) from \(t'\) there. The presence of an unseen pair alone does not establish that such a \(t'\) exists; it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\)."
  - An unconditional existence theorem becomes a conditional one. Under the colon's gloss the conditional is close to analytic.
- **Proof** (C77). There is a new branch: "Where \(\mathcal T\) contains no such transport, \(H\) is silent on the value at \((a,b)\) and the population fixes it."
- **Consequence** (C78). It adds "wherever its population admits an alternative" and a sentence that gives up "the blanket claim that every untested value is unconstrained".

The three restated sentences:
- **Grievance 3** (C13). "*always* underdetermined" becomes "wherever its population admits a differing survivor there".
- **Attack point (D) and the Part XV entry** are one passage in file 11 (C73, L534). Its first limb is CLAIM:
  - f10: "A selection history \(H\subsetneq C\) whose survivor is determined on \(C\setminus H\). This refutes Derivation 3." (L539), and "a selected transport can be non-underdetermined on unseen changes" (L74).
  - f11: "a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Derivation 3; a population with no such survivor is the theorem's own qualification, not a refutation)".
  - Under the Claim's gloss ("underdetermined" means "survival on \(H\) does not distinguish \(t\) from \(t'\)"), this refuter is unsatisfiable. The one exception is reading "determined by its history" as more than survival, for example through \(\mu\).
  - Derivation 3 thereby loses almost all refutable content under (D). Both readers note the near-definitional status. R1 notes the unsatisfiability, and I confirm it with that exception.
  - The quantifier also becomes pointwise: from all of \(C\setminus H\) to one unseen change (R2).
- **The Part 0 short form at L63** ("(D) the two provenances and the underdetermination of selected transports") is ORDER, as part of C22. It is a label for the Part XV entry. But it carries no qualification, contrary to the note's promise that "every restatement of a theorem carries the theorem's own qualification". R1 flags this; R2 calls it neutral.

Places the note does not name. Both readers found all four; all are CLAIM:
- C32 (L197): the population is part of the claim.
- C35 (L225): surprise and the population.
- C64 (L473): the population defined. This alone decides O48.
- C81 (L616): the Derivation 10 gloss, inexact (XR7).

The note says "One claim changes". That understates even the Derivation 3 change.

My addition: the note says the proof "already assumed the qualification". Whether that holds depends on how file 10's "surviving on \(H\)" is read.
- If it means "a member of \(\mathcal T\) that survived" (the definition of Sel at L210), file 10's proof ("Alter \(L_{j}(a,b)\) … the result survives on \(H\)") silently needed the altered transport to be in \(\mathcal T\). The note is then right.
- If it means "satisfies the survival condition, fidelity on \(H\)", file 10's theorem held as stated and needed no population. File 11 then changes what the theorem is about, from admissible alternatives to population members.
- File 10 leaves both readings open.

Cases:
- **O48** moves from DISAGREE or SPLIT under file 10 toward AGREE under file 11. File 10's "always" and "there exists a transport \(t'\)" go against "there is no alternative in that population". File 11's L562 and L473 give the verdict nearly verbatim.
- **O24** is AGREE under both: a reachable differing arrangement is given.

**(ii) Part XI Repair: "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers". Reconciled ruling: CLAIM (changed).** Both readers agree.

- File 10 (L438–444): "For claimed obligations \(O\) and protected obligations \(P\), fixed for the comparison," then (P), whose protection clause is \(\forall r\in P[r(\xi)\Rightarrow r(\xi')]\), then "(P) does not rank alternatives." There are no occasions, and loss is read only at the compared states \(\xi\), \(\xi'\).
- File 11 keeps the same opening (L427) and the same formula, and adds at L433: "The obligations are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers."
- There are three changes:
  1. O and P become declared inputs. That ties them to L514: a missing input makes the verdict unsettled.
  2. Every obligation becomes a condition over stated occasions.
  3. Loss is defined as failure on any covered occasion. The "exactly when" makes it both necessary and sufficient, and a failure between \(\xi\) and \(\xi'\) counts.
- Because (P) is unchanged, the formula and the prose agree only if \(r(\xi')\) is read as "\(r\) held on every covered occasion up to \(\xi'\)".
- Quote note: R2's "'Fixed for the comparison' becomes 'declared inputs'" is inexact, because both phrases stand in file 11.
- The rest of the paragraph is also CLAIM: C57 (worth), C58 (ProducedBy and credit) and C59 (three attributions).

Cases:
- **O38** ("the kitchen tap runs at all times during the work"; a four-second stop). Under file 10, an end-state reading of (P) gives "held", which is a DISAGREE with "it was broken". A history reading gives "broken", so file 10 yields SPLIT or DISAGREE. Under file 11, the occasions are stated and one covered occasion failed, which is an AGREE.
- **O35** (occasions not stated; nobody drew). Under file 10, the end state gives no loss, an AGREE with "not a loss". Under file 11, the occasions are a missing declared input, so the verdict is unsettled (SILENT). It is AGREE if the occasions are read as draws and DISAGREE if they are read as all times.

**(iii) Part XIV "Declared inputs" (f11 L514; nothing in file 10 between L521 and L523). Reconciled ruling: CLAIM (new).** Both readers agree.

- Text: "**Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII). A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."
- It adds a category beside the primitives, the indices and the derived. It adds a verdict rule: a missing input leaves the verdict unsettled. It also bars choosing the input from the verdict wanted.
- The rule reads almost word for word as the briefs' SILENT mark: "it takes the deciding matter as an input the case leaves unstated".
- It carries four tensions inside file 11:
  - Boundary, continuity and the contract stay "declared indices" at L516 and are now inputs as well.
  - "Besides the two primitives" excludes \(\mathcal N\), which L27 and L447 call a declared input (XR3, XR5).
  - "Everything else is derived" at L33 and at L512, just above this paragraph, does not mention the category.
  - Derivation 6's claim is widened to include it (C80), but its proof's dependence order does not list it (XR6).

Cases:
- It pulls toward SILENT wherever the named input is missing:
  - O35: occasions.
  - O1, O5 and, weakly, O8: what makes the restriction appropriate.
  - O17, O21, O27, O30, O40, O50: no declared boundary, where ownership or credit is at issue.
  - Weakly O3, O14, O18, O31: "own" or "hers" with no declared boundary.
- It decides where the input is stated: O38 (occasions), O41 (robot-only boundary), O42 (continuity), O51 (boundary).

---

## 6. Counts

- **Places:** 81 in all.
  - CLAIM: 48. Two are meta (C1, C10); 46 are inside the theory.
  - WORDING: 22. ORDER: 11.
- **Found by:** both readers, 81; one reader only, 0.
- **Disputed rulings:** 3.
  - C28 and C29: ORDER by R1 and by me; CLAIM by R2.
  - C39: ORDER by R1 and by me; WORDING by R2.
- **In this granularity:** R1's rulings coincide with mine on all 81 places. R2's coincide on 78, giving 50 CLAIM, 23 WORDING and 8 ORDER.
- **Derivation 3 cluster:** 10 CLAIM places (C13, C32, C35, C64, C73, C75, C76, C77, C78, C81). The note names the theorem (C75–C78) and "three sentences", which in file 11 are two passages (C13, C73).
- **Worth cluster:** C7, C57, C60, C61, C65, C79, plus the "invokes worth" phrase inside C9.
- **Cross-references:** 7 are SLIP (XR1–XR7) and none is CLAIM-CHANGING.
  - Both readers ruled XR1 and XR3 SLIP.
  - R1 alone raised XR2 and XR4 as pointers.
  - R2 ruled XR5, XR6 and XR7 SLIP, where R1 ruled them CORRECT with a note.
