# 03 Step 4: every difference between file 10 and file 11 ruled, after reading both 1D lists and both 2D audits

**What this is.** Claude's step-4 determination for S81. Every place where file 11 (`Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md`) differs from file 10 (`Semantics/authority/10 Claude Fable Semantics - standalone theory.md`) that any reader marked CLAIM, or that the plan names, is ruled CLAIM, WORDING or ORDER here. P3, E1 and test (d) are scored from those rulings. Written by Claude, 23 September 2026.

**Step 4, in the plan's words** (`Semantics/tests/S81 Plan - second version, Sonnet testers and API auditors.md`, "How Claude determines the result", item 4): "**The differences:** every CLAIM place on either 1D list, and every place in either 2D's "Surviving differences in claim" or "Differences in claim that both lists missed", read against both files and ruled CLAIM or WORDING." The third version of the plan changes nothing in step 4.

**Where it starts.** Claude's pre-reading, `02 Claude's reading of the differences between file 10 and file 11, written before opening the 1D lists.md` in this folder, committed in 2788a77 before any 1D list was opened. It rules 81 places: 48 CLAIM (two of them meta, C1 and C10), 22 WORDING and 11 ORDER, with cross-references XR1–XR12. Step 4 starts from those rulings and records each one it changes (section 7).

**How it was made.**
1. **Alignment** (`raw readings/03a alignment.md`). Every record on the two 1D lists and every item in the two 2D audits was mapped to the pre-reading's places. This gives the master list of 59 places, M1–M59, and 18 cross-references. No ruling is made there.
2. **Rulings**, in three ranges (`03b rulings R1.md`, M1–M21; `03c rulings R2.md`, M22–M41; `03d rulings R3.md`, M42–M59 and every cross-reference). Each place was read against both files at the lines given, with its paragraph, and each whole file was searched for related qualifications.
3. **Adversarial verification** (`03e verification.md`). 28 rulings were selected and tested: every ruling that differs from the pre-reading, every WORDING or ORDER ruling on a place some reader marked CLAIM, every named place, and every pointer not ruled CORRECT, plus NEW-XR1. Result: **28 UPHELD, 0 OVERTURNED, 0 UNCERTAIN.** Five rulings are upheld with a correction to their reasoning (section 7.4). No ruling changes, so the table below carries the range rulings as they stand.

**Inputs read, across the five working files and this assembly.**
- File 10 and file 11, in full, with term searches of both.
- Claude's pre-reading (02), in full. Its raw readings 02a and 02b, in the parts named in 03b–03d.
- Claude's case rulings (01): the header, the reconciled table, every case record, the baseline comparison and the SILENT table.
- The case book (`Semantics/tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`), in full.
- The 1D returns `returns/s81_1D_A.response.txt` and `returns/s81_1D_B.response.txt`: every record and every closing section.
- The 2D returns `returns/s81_2D_atria.response.txt` and `returns/s81_2D_mimo.response.txt`, in full.
- The instruction heads of `briefs/s81_1D_A.txt` (lines 1–70) and `briefs/s81_2D_atria.txt` (lines 1–90), and `grep -c` counts on both for "Revision 1", "O48", "S75" and "bell does not explain the tide".
- The S81 plan: the second version, lines 100–170; the third version, a `grep` for step 4, 1D, 2D, P3, E1 and ORDER, and its sections e to l.
- For this assembly: the five working files in full; plan second version lines 105–166; the pre-reading's merged table and counts; f11 L5, L433 and L514 and f10 L438; the count lines and D47 records of both 1D returns; the section counts of both 2D returns.

**Not opened for this step.** Any 1C, 1K, 2a or 2b return; any reasoning file; any receipt's content; the effort-controls folder; the sample JSONs; `stage1/`; any table; the briefs of tester B and of Mimo.

**Seen, names only.** Listings of `determination/`, `raw readings/`, `briefs/`, `outputs/` and parts of `returns/`, and `git status`, showed the names of untracked 2b and effort-control files in `returns/`. None was opened.

**Words used.**
- **CLAIM**: a reader can conclude from one text something the other leaves unconcluded. This covers file 11 asserting what file 10 leaves unasserted; dropping, narrowing, widening or qualifying what file 10 asserts; and adding or removing a requirement, condition, exception, quantifier or outside input. The grade in brackets (*changed*, *new*, *application*, *narrowed*, *meta*) is for the reader only. *Application* means derivable from file 10 but first stated in file 11. Under the pre-reading's policy, kept here, that is CLAIM.
- **WORDING**: both texts assert the same thing, and every conclusion drawn from one can be drawn from the other.
- **ORDER**: the same claim, moved or copied to another place. File 10 states it somewhere at the same or wider scope. P3 counts ORDER with WORDING.
- **Declared**: named in file 11's revision note (f11 L5): "One claim changes: Derivation 3 … The three sentences that restated it (the answer to grievance 3, attack point (D), the Part XV entry) change with it. Nothing else changes in what is claimed."
- **Harmful**: a case's verdict moves away from the thoughtful person because of the place. The evidence is Claude's case rulings (01), written before any return was opened. "01 marks" are file 10 → file 11. Step 3 fixes the marks that count. Under the plan the file-10 mark is S75's baseline unless both 1K returns agree on a different mark and Claude confirms it. The baseline is DISAGREE on O48; SILENT on O1, O12, O20, O21, O27, O35, O40 and O50; AGREE on the rest.
- **Readers**: tester A and tester B (1D lists); Atria and Mimo (2D audits; Atria audits A's list with B's as second, Mimo the reverse). "Pre" is Claude's pre-reading. "All five" means A, B, Atria, Mimo and pre. A 2D auditor "said CLAIM" when the place is in its "Surviving differences in claim" or its "Differences in claim that both lists missed".

---

## 1. The ruled master table

Line numbers are each file's own. "—" means not applicable. "None shown" means no case shows the place harmful on 01. "Verified" names the verification's verdict; "spot" marks a spot check outside its selection.

| M | C | f10 / f11 | final ruling | who said CLAIM | declared by note? | cases touched (01 marks) | harmful? | changed from pre-reading? and why | verified |
|---|---|---|---|---|---|---|---|---|---|
| M1 | C1 | absent / L5, the revision note | CLAIM (meta) | pre only (the note was withheld from every brief) | it is the note | O48 named; the note reached no reader | none shown | no | — |
| M2 | C3 | L13 s3 / L15 s3 | WORDING (borderline) | A, B, Atria, Mimo | — | O11 (weak), AGREE→AGREE | — | no. The body (f10 L210, L216, L416 = f11 L197, L203, L403) states "blind" as no represented target, in both files | UPHELD |
| M3 | C7 | L25 / L27 s1–s2 | CLAIM (changed) | all five | no | O12, O50 SILENT→SILENT; O40 AGREE→AGREE; O35, O38 (weak) | none shown; flag O35 | no | — |
| M4 | C8 | absent / L27 s3 | CLAIM (new) | all five | no | O20, O26, O32, O39, O40, O21, O27 AGREE→AGREE; O50 SILENT→SILENT | none shown; flag O21, O27 | no | — |
| M5 | C9 part a | L519 (L458, L593, L597) / L33 s1 | CLAIM (changed); the same change as M47, counted once | A, B, Atria, Mimo | no | O12 SILENT→SILENT; O35 (weak) | none shown; flag O35 | in form only: pre ruled the C9 section ORDER and this phrase at C65 | UPHELD |
| M6 | C9 part b | L521, L523, L525, L597 / L33 s2–s4 | ORDER | A, Atria, Mimo (on s4) | — | none | — | no. f10 L597, kept at f11 L590, already says no residual predicate exists | UPHELD |
| M7 | C10 | absent / L37 | CLAIM (meta) | all five | no | none directly | none shown | no | — |
| M8 | C13 | L38 / L43 | CLAIM (changed) | all five | **yes** (the answer to grievance 3) | O48 DISAGREE→AGREE, toward; O24 AGREE→AGREE | no | no | UPHELD |
| M9 | C15 | L44 / L47 | WORDING | A, Atria, Mimo | — | none | — | no. Both files' Part XV lists and "Anything else is a detail" (f10 L78, f11 L63) leave novelty out | UPHELD |
| M10 | C19 | L56 / L55 | WORDING | A, Atria | — | none | — | no. f11 L39, L157 and L473 keep "label is stipulated" and "selection is checkable" | UPHELD |
| M11 | C20 | L59 / L57 | WORDING | A, B, Atria, Mimo | — | none | — | no. Generic sentence; f11 L199, L578 and L594 presuppose episodes without a contract change | UPHELD |
| M12 | C22, the (D) short form | L66–L78 / L63 | ORDER | none | moot (one reading of "attack point (D)") | O48 (weak) | — | no | UPHELD |
| M13 | C25 | absent (L126, L138–L144) / L129 s4–s5 | CLAIM (application; close call with ORDER) | all five | no | O4, O6, O9 AGREE→AGREE | none shown | no | — |
| M14 | C26 | absent (L168) / L153 last | CLAIM (application) | all five | no | O4, O6, O9 (weak) AGREE→AGREE | none shown | no | — |
| M15 | C28 | L41, L272 / L161 s1 | ORDER | A, Atria, Mimo | — | O1, O5, O8, O33 (claim unchanged) | — | no. f10 L272 and L41 say it; f11 L277 keeps "silently narrowed contract" | UPHELD |
| M16 | C29 | L41, L168, L268, L378, L456, L603 / L161 s2 | ORDER | A, B, Atria, Mimo | — | O1, O5, O8 (claim unchanged) | — | no. The readers cite only f10 L456; f10 L168, L378 and L603 state the general rule | UPHELD |
| M17 | C30 | absent / L161 s3 | CLAIM (new) | all five | no | O1 SILENT→SILENT; O5, O8 AGREE→AGREE | none shown; flag O1, O5 | no | — |
| M18 | C31 | absent (L168, L176, L268) / L163 last | CLAIM (application) | all five | no | O34 AGREE→AGREE | none shown | no | — |
| M19 | C32 | L210 / L197 last | CLAIM (changed; Derivation 3 cluster) | all five | no: carries the declared change at a place the note does not list | O48 toward; O24 AGREE→AGREE | no | no | spot |
| M20 | C33 | absent (L208, L226, L342) / L213 last | CLAIM (new in its second clause) | all five | no | O28, O16, O29 AGREE→AGREE | none shown | no | — |
| M21 | C35 | L238 / L225 last | CLAIM (changed; Derivation 3 cluster) | all five | no, as M19 | O48 toward; O24, O3 (weak) AGREE→AGREE | no | no | spot |
| M22 | C38 | L284 s2 / L271 s2–s3 | CLAIM (changed) | all five | no | O33, O2 AGREE→AGREE | none shown | no | — |
| M23 | C40 | L288 / L275 s2 | CLAIM (application) | all five | no | O2 AGREE→AGREE | none shown | grade only (pre "new") | — |
| M24 | C41 s1 | L294 s1 / L279 s1 | CLAIM (narrowed; close call) | B, Atria, Mimo | no | none | no case touches it | **yes**: pre WORDING. "Satisfies (E)" asserted all five conjuncts; "does not exclude" withdraws that | UPHELD |
| M25 | C42 | absent / L279 s3 | CLAIM (application) | all five | no | O7 AGREE→AGREE; O4 (as a contrary only) | none shown | no | — |
| M26 | C43 | L316 / L301 s2 | CLAIM (application; the second clause also has a narrowing reading) | all five | no | O36 AGREE→AGREE | none shown | grade only (pre "new") | — |
| M27 | C44 | L322, L310, L326 / L307 last | ORDER | A (hedged), pre | — | O47 AGREE→AGREE | — | **yes**: pre CLAIM (application). f10 L326 states the subset/whole failure in general form | UPHELD |
| M28 | C45 | L324 / L309 s3 | CLAIM (new) | all five | no | O45, O46 AGREE→AGREE | none shown | no | — |
| M29 | C47 | absent (L609) / L363 s1 | CLAIM (new) | all five | no | O43, O28 (weak) AGREE→AGREE | none shown | no | — |
| M30 | C48 | absent / L363 s2 | CLAIM (application) | all five | no | O44, O15 AGREE→AGREE | none shown | grade only (pre "new") | — |
| M31 | C49 | L384 / L371 last | CLAIM (application and new) | all five | no | O52, O25, O19 AGREE→AGREE; O13 (weak) | none shown | no | — |
| M32 | C50 | L406 / L393 last | CLAIM (new) | all five | no | O16 AGREE→AGREE, passage CHANGED; O29; O37 (weak) | none shown | grade only (pre "application") | — |
| M33 | C51 | L412 / L399 last | CLAIM (application) | all five | no | O14 AGREE→AGREE | none shown | grade only (pre "new") | — |
| M34 | C52 | L414 / L401 s4 | CLAIM (application) | all five | no | O3 AGREE→AGREE | none shown | grade only (pre "new") | — |
| M35 | C53 | L414 / L401 s5 | CLAIM (new) | all five | no | O18 SPLIT→AGREE, toward; O31 passage CHANGED; O15, O11 (weak) | none shown | no | — |
| M36 | C54 | L430 / L417 last | CLAIM (new) | all five | no | O23, O33 (weak) AGREE→AGREE | none shown | no | — |
| M37 | C55 | absent / L419 | CLAIM (new definition) | all five | no | O41 SPLIT→AGREE, toward; O17, O21, O30, O40, O49, O51 passage CHANGED; O27; O50 SILENT→SILENT; O3, O14, O18, O31 (weak) | none shown; boundary rows flagged | no | — |
| M38 | C56 | L438–L444 / L433 s1 | **CLAIM (changed). P3 named place (ii), the occasions clause** | all five | no | **O35 AGREE→SILENT, away**; O38 AGREE→AGREE, passage CHANGED | **yes on 01 (O35, jointly with M48), pending step 3's file-10 mark** | no | UPHELD |
| M39 | C57 | L444 / L433 s2 | CLAIM (application) | all five | no | O12 SILENT→SILENT; O35, O38 (weak) | none shown; flag O35 | no | — |
| M40 | C58 | absent (L441) / L433 s4 | CLAIM (new definition) | all five | no | O20, O26, O39 passage CHANGED; O13, O25, O32, O52, O21, O27, O40 AGREE→AGREE; O50 SILENT→SILENT | none shown; flag O21, O27 | no | — |
| M41 | C59 | absent / L433 s5 | CLAIM (application) | all five | no | O13 AGREE→AGREE | none shown | no | — |
| M42 | C60 | L458 / L447 heading, s1–s2 (s3 alone WORDING) | CLAIM (changed) | all five (B WORDING on s3 alone) | no | O12 SILENT→SILENT; O38 (weak); O35 (weak, its change traced to M38, M48) | none shown | no | — |
| M43 | C61 | L458, last two sentences / L447, last clause | CLAIM (application; close call) | A (hedged), B, Mimo, pre | no | none | no case touches it | no | spot |
| M44 | C62 | absent (L523) / L465 | CLAIM (new) | all five | no | O41 toward; O42, O30, O51 passage CHANGED; O17 (weak) | none shown; flag O17, O30 | no | — |
| M45 | C63 | L476 / L467 last | CLAIM (new) | all five | no | O49, O17 passage CHANGED | none shown | no | — |
| M46 | C64 | L482 / L473 last | CLAIM (new definition; Derivation 3 cluster) | all five | no | O48 toward | no | no | spot |
| M47 | C65 | L519 / L510 | CLAIM (changed) | all five | no | O12 SILENT→SILENT | none shown | no | — |
| M48 | C66 | absent (L521–L523) / L514 | **CLAIM (new). P3 named place (iii), Declared inputs** | all five | no | **O35 AGREE→SILENT, away**; O41 toward; O1, O50 SILENT→SILENT; O5, O8, O17, O21, O27, O30, O38, O40, O42, O51 AGREE→AGREE; O3, O14, O31, O18 (weak) | **yes on 01 (O35, jointly with M38), pending step 3's file-10 mark** | no | UPHELD |
| M49 | C67 | L525 / L518 last | CLAIM (new) | all five | no | O37 SPLIT→AGREE, toward; O49, O17 AGREE→AGREE | none shown | no | — |
| M50 | C70 | L68 (L284, L533) / L528 s3 | CLAIM (changed) | all five | no | O2, O33 AGREE→AGREE | none shown | no | — |
| M51 | C71 | L70, L535 / L530 | ORDER | Mimo (its NEW1) | — | none | — | no. f10 L535 already carries f11 L530; Mimo's NEW1 is not followed | UPHELD |
| M52 | C73 | L74, L539, L541 / L534 | CLAIM (changed) in limb 1; limbs 2–3 ORDER | all five | **yes** (attack point (D), the Part XV entry) | O48 toward; O24 AGREE→AGREE | no | no | UPHELD |
| M53 | C75 | L567 / L560, the Derivation 3 title | CLAIM (changed) | pre (A and B name it only in a PART line; no 2D item) | **yes** | O48 toward | no | no | UPHELD |
| M54 | C76 | L569 / L562, Derivation 3 Claim | CLAIM (changed) | all five | **yes** | O48 toward; O24 AGREE→AGREE | no | no | UPHELD |
| M55 | C77 | L571 / L564, Derivation 3 Proof | CLAIM (changed) | all five | **yes** | O48 toward | no | no | UPHELD |
| M56 | C78 | L573 / L566, Derivation 3 Consequence | CLAIM (changed) | all five | **yes** | O48 toward; O24, O3 (weak) AGREE→AGREE | no | no | UPHELD |
| M57 | C79 | L589 / L582 last | CLAIM (application) | all five | no | O12 SILENT→SILENT | none shown | no | — |
| M58 | C80 | L593 / L586 | CLAIM (changed) | all five | no | only through M48 | not on its own | no | — |
| M59 | C81 | L623 / L616 | CLAIM (new interpretive clause; Derivation 3 cluster) | all five | no | none | no case touches it | no | spot |

**Close calls.** The verification left no ruling UNCERTAIN. The rulers named these places as close: M2 (ordinary-sense "blind"), M13 (the ORDER/CLAIM line at "In particular"), M24 (file 10's heading "What (E) does not exclude"), M43 (Atria's WORDING rests on derivability, which is the *application* grade). M5's ruling follows M47's. Of the pointers, NEW-XR1 was marked uncertain by its ruler and upheld by the verification (section 5).

---

## 2. Counts

**The master list (59 places).**

| | CLAIM | WORDING | ORDER |
|---|---|---|---|
| R1, M1–M21 | 13 | 4 | 4 |
| R2, M22–M41 | 19 | 0 | 1 |
| R3, M42–M59 | 17 | 0 | 1 |
| **all** | **49** | **4** | **6** |

- WORDING: M2, M9, M10, M11. ORDER: M6, M12, M15, M16, M27, M51.
- The 49 CLAIM places include two meta places (M1, M7), and M5, which is the same change as M47. That gives 48 distinct CLAIM changes, 46 of them inside the theory.

**Every place where the files differ.** The pre-reading's 81 places, with C9 and C41 each split in two, make 83. CLAIM 49, WORDING 22, ORDER 12.
- The 24 places off the master list keep their pre-reading rulings, since no reader marked any of them CLAIM:
  - WORDING: C2, C4, C5, C6, C11, C12, C14, C16, C17, C18, C21, C23, C24, C27, C34, C36, C46, and C41 sentence 2;
  - ORDER: C37, C39, C68, C69, C72, C74.
- Every tester record on an off-list place is marked WORDING, and neither 2D audit moves one of them to CLAIM. The pre-reading's WORDING or ORDER stands on each.

**Declared and undeclared CLAIM.**
- **Declared by the note: 6.** M8, M52, M53, M54, M55, M56. M1 is the note itself.
- **Undeclared: 42.** 41 inside the theory, and M7 (meta). By range: R1 10 and M7; R2 19; R3 12. Counting M5 with M47, 40 distinct undeclared changes inside the theory.
- Four undeclared places carry the declared Derivation 3 change at places the note does not list: M19 (L197), M21 (L225), M46 (L473) and M59 (L616).

**Each tester's 1D list.**

| | records | CLAIM | WORDING | master places marked CLAIM | of those, ruled CLAIM | ruled WORDING or ORDER |
|---|---|---|---|---|---|---|
| Tester A | 68 | 55 | 13 | 54 | 46 | 8: M2, M6, M9, M10, M11, M15, M16, M27 |
| Tester B | 72 | 52 | 20 | 50 | 47 | 3: M2, M11, M16 |

- A's 55 CLAIM records fall on 54 places: D45 and D46 share M37, D50 and D51 share M42, and D47 covers M38 and M39.
- B's 52 fall on 50: D45 and D46 share M37, D51 and D52 share M42.
- Each list has an ORDER count of 1 (C68, ORDER in the pre-reading) and "Cross-references in Text B: WRONG 0" (A CHECKED 169, B CHECKED 178).
- Ruled CLAIM but not marked CLAIM by the tester: A, M1, M24 and M53; B, M1 and M53.

**Each 2D audit.**

| | Part 1 records (CLAIM / WORDING) | Part 2: WORDING records it would mark CLAIM | places it added ("both lists missed") | surviving items (master places) | of those, ruled CLAIM |
|---|---|---|---|---|---|
| Atria | 107 (104 / 3) | 4, B's D5, D10, D12, D19 (M6, M9, M10, M15), all on places A's list already marks CLAIM | **0** (COUNT 0) | 54 (53) | 46; not CLAIM: M2, M6, M9, M10, M11, M15, M16 |
| Mimo | 107 (105 / 2) | 3, B's D5, D10, D19 (M6, M9, M15), all on places A's list already marks CLAIM | **1** (COUNT 1): NEW1 = C71, M51, ruled ORDER | 54 (54) | 47; not CLAIM: M2, M6, M9, M11, M15, M16, M51 |

- Atria's surviving list leaves out M27 (C44) and M43 (C61), which it ruled WORDING in Part 1. Step 4 rules M27 ORDER and M43 CLAIM.
- Mimo's surviving list leaves out M10 (C19) and M27 (C44), which it ruled WORDING in Part 1. Step 4 rules both not CLAIM.

**The pre-reading.** Of its 48 CLAIM places, 47 are ruled CLAIM. M27 is ruled ORDER. M24 is added, and M5 is counted as a place of its own, which gives 49.

**The verification.** 28 rulings checked: 20 master places and 8 pointers. UPHELD 28, OVERTURNED 0, UNCERTAIN 0.

---

## 3. P3: FAILS

**P3** (plan, second version): "Of the places where file 10 and file 11 differ, the ones Claude rules CLAIM after reading both 1D lists and both 2D audits are Derivation 3 and the three sentences restated with it. Every other place is WORDING or ORDER. … P3 stands only if Claude rules both WORDING."

**The two named places.**
- **The Part XI Repair occasions clause (M38, f11 L433 s1): CLAIM.** "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers" adds three things file 10 does not have:
  - a requirement: every obligation is a condition over stated occasions;
  - an outside input: the occasions;
  - a loss criterion. A failure on a covered occasion is a loss, and a failure on an uncovered occasion is not. f10 L438–L444 evaluates \(r\) only at \(\xi\) and \(\xi'\) and has no occasions.
  - All five readers say CLAIM, and no reader says WORDING.
- **The Part XIV Declared inputs paragraph (M48, f11 L514): CLAIM.** It adds a category of stated inputs "that the semantics records and does not supply". Two of its members are new inputs: the occasions each obligation covers, and what makes a restriction appropriate. It also adds a verdict rule: "where the input is missing, the verdict is unsettled and the semantics says so". File 10 has instances of the thought (f10 L344, L406) but not the rule. All five readers say CLAIM, and no reader says WORDING.

**Derivation 3 and its three sentences.** M53–M56 (the derivation), M8 (the answer to grievance 3) and M52 (attack point (D) and the Part XV entry, one passage in file 11) are CLAIM, as P3 expects. M12, the L63 short form and the other possible referent of "attack point (D)", is ORDER: it names the claim and defers to Part XV.

**CLAIM places beyond Derivation 3 and its three sentences: 43.** They are 41 inside the theory and 2 meta; with M5 counted with M47, 40 distinct theory changes. Grouped for reading:
- **Derivation 3 cluster, not in the note's list (4):** M19, M21, M46, M59.
- **Worth (7):** M3, M5, M39, M42, M43, M47, M57.
- **Repair, credit, ownership and boundary (7):** M4, M37, M38, M40, M41, M44, M45.
- **Declared inputs and the primitive layer (4):** M17, M48, M49, M58.
- **Other additions and changes (19):** M13, M14, M18, M20, M22, M23, M24, M25, M26, M28, M29, M30, M31, M32, M33, M34, M35, M36, M50.
- **Meta (2):** M1 (the note; its "Nothing else changes in what is claimed" is false against the 41 places above), M7 (the front-matter reading rule).

**Result.** P3 fails at named place (ii), at named place (iii), and at 39 further places inside the theory, besides the two meta places. None of them is WORDING or ORDER. Under the standing rule, file 11 can still stand with these findings recorded against its note when P3 fails "only by a theory change toward the thoughtful person or by an undeclared CLAIM that no case shows harmful" and (a) to (d) hold. Section 6 gives the one undeclared pair that a case shows harmful on 01, conditionally.

---

## 4. E1: HOLDS

**E1** (plan, second version): "at least one model marks the occasions clause CLAIM in 1D". Scored on the 1D lists of testers A and B, as the second version's reading rule fixes ("E1 on the 1D lists of A and B").

| tester | record | what it quotes | MARK |
|---|---|---|---|
| A | D47 | the occasions sentence joined with the next ("Their declaration makes no claim …"). WHY: "B makes \(O\) and \(P\) declared inputs with stated occasions, gives an exact loss condition, and denies any worth claim" | CLAIM |
| B | D47 | the occasions sentence alone, "The obligations are declared inputs: …" to "… fails on an occasion it covers." B marks the next sentence separately (D48, CLAIM) | CLAIM |

- **Count: 2 of 2 testers**, one record each. Neither marks the clause WORDING.
- Both TESTs take the same direction: "A protected condition fails on an occasion it does not cover: B says it is not lost; A gives no rule" (A); "… outside its stated coverage: B says it is not lost; A gives no criterion" (B).
- Both 2D audits agree CLAIM on both testers' records, and both surviving lists carry the clause.

---

## 5. Cross-references, test (d): HOLDS

**Test (d)** (plan, second version): "No cross-reference in file 11 is ruled to point wrong in a way that changes what a sentence claims. A pointer that is only a slip is recorded as an erratum for a later revision."

- 18 pointers were ruled: XR1–XR12 from the pre-reading, and NEW-XR1–NEW-XR6 from the returns. **CORRECT 11, SLIP 7, CLAIM-CHANGING 0.**
- The verification upheld all seven SLIPs and NEW-XR1.
- Tester A and tester B each report "WRONG: 0". Their pointer remarks sit under "Noticed": XR3 (B), XR7 (A, B), NEW-XR1 (A, B). Mimo confirms XR3, XR7 and NEW-XR1 as wrong. Atria reports none wrong and names XR3 as correct; that is not followed.

**Each pointer not ruled CORRECT: all SLIP, recorded as errata for a later revision.**

| id | f11 line | pointer | ruling | why it does not change a claim |
|---|---|---|---|---|
| XR1 | L5 | "(the answer to grievance 3, attack point (D), the Part XV entry)" | SLIP | The list follows file 10's layout. In file 11, attack point (D) and the Part XV entry are one passage (L534). The L63 short form carries no qualification. The note also omits L197, L225, L473 and L616. The note is meta (M1), and no theory sentence depends on the list |
| XR2 | L5 | "the audit's case O48", "(Semantics results S75)" | SLIP, with a steering flag | Points outside the document. The note's statement about Derivation 3 stands without it. The 1D and 2D briefs checked carry "Revision 1", "O48" and "S75" zero times |
| XR3 | L27 | "(Parts XI, XIV)" | SLIP (the closest to CLAIM-CHANGING) | Parts XI and XIV carry only worth and aesthetics through \(\mathcal N\). A probability of truth is marked nowhere. L27's claim is set by its own words; the overreach is ruled at M3 |
| XR4 | L275 | "(the bell does not explain the tide)" | SLIP, with a steering flag | Case O2's content inside the theory, with no referent in the document. The rule stands without it. It reached the readers inside the theory text |
| XR5 | L447 | "(Part XIV)" | SLIP (arguably CORRECT) | Lands on L510, but L514 excludes \(\mathcal N\) from the declared inputs. Either way \(\mathcal N\) is an input the semantics does not supply |
| XR6 | L588 | "By the dependence order of Part XIV" | SLIP | The order at L518 lists no declared input and none of the definitions that rest on one (L419, L433, L465). A gap in the proof; the claim at L586 is set by its words |
| XR7 | L616 | "Derivation 3's qualification seen from the other side" | SLIP | Misdescribes the qualification: no *differing* survivor, not no survivor at all. Derivation 10's conclusions do not rest on the clause. The clause is the CLAIM place M59 |

**CORRECT, noted.**
- NEW-XR1, L620 "(Derivation 2)": CORRECT (loose). Its ruler marked it uncertain, and the verification upheld it. A, B and Mimo call it wrong, because the direct basis is (K) with Derivation 1. Derivation 2's claim and Consequence (L554, L558) still carry the sentence and the one after it. The words are the same in file 10 (L627), so it is not a difference between the files. At worst it is an erratum both files share.
- XR8, XR9 (loose), XR10, XR11, XR12 and NEW-XR2 to NEW-XR6 are CORRECT.

**Test (d) HOLDS on this evidence.** No pointer is ruled CLAIM-CHANGING. XR1–XR7 go on the errata list for a later revision.

---

## 6. Undeclared CLAIMs that a case shows harmful, and the rows step 3 must examine

**Shown harmful on Claude's case rulings (01), conditionally: M38 and M48 together, on O35.**
- **O35, "Four seconds":** AGREE under file 10 → SILENT under file 11 on 01, away from the thoughtful person, a theory change. 01 traces it to f11 L433 s1 (M38) and L514 (M48) together:
  - under file 10, (P) checks \(r\) at \(\xi\) and \(\xi'\); the tap "then runs as before", so there is no loss (AGREE on the endpoint reading);
  - under file 11, the protected tap's occasions are not stated, and L514 leaves the verdict unsettled (SILENT).
- **Condition.** The file-10 mark that counts is S75's baseline, SILENT on O35, unless both 1K returns agree on a different mark and Claude confirms it.
  - If the file-10 mark is SILENT, O35 is SILENT→SILENT on the same point (the reach of the protected condition), and no case shows M38 or M48 harmful.
  - If it is AGREE, O35 is a theory change away from the thoughtful person. Test (b) then fails. The standing rule's saving clause ("an undeclared CLAIM that no case shows harmful") covers neither M38 nor M48.
- **No other undeclared CLAIM is shown harmful.** Every other case these places touch is SAME on 01, or moves toward the thoughtful person: O18 (M35), O37 (M49), O41 (M37, M44), and O48 (M19, M21, M46, beside the declared places).

**Rows step 3 must examine.**

| row | places | what to check | what it can show |
|---|---|---|---|
| **O35** | M38, M48 (decisive); M3, M5, M39, M42 (weak, through "in every way that mattered") | The file-10 mark: S75's baseline SILENT against 01's AGREE. Also whether any file-11 SILENT rests on the worth clause (L27, L33, L447, L510) rather than on occasions | Harm, and test (b) |
| **O48** | M8, M52–M56 (declared); M19, M21, M46 (undeclared); M12 (weak) | P1: that each file-11 AGREE rests on L562, L534 or L43 (declared), not only on L473, L197 or L225. Any reading that cites L63 | P1 |
| **O24** | M52–M56 | That no file-11 reading turns it SILENT through L562's "admitted, realizable, a member of \(\mathcal T\)" or L473 | Harm |
| **O1, O5, O8** | M17, M48 | Any file-11 SILENT for want of a ground of appropriateness, against a file-10 AGREE | Harm |
| **O17, O21, O27, O30, O40**; weakly **O3, O14, O18, O31** | M37, M44, M48 | Any file-11 SILENT for want of a declared boundary, against a file-10 AGREE | Harm |
| **O21, O27** | M4, M40 | Any file-11 SILENT or DISAGREE on "mostly" under L27 s3 or L433 s4 ("no division of credit that it does not contain") | Harm |
| **O12** | M42, M47, M57 | Any file-11 DISAGREE on "its merit is real". Claude's reading is SILENT: file 11 says finding a question establishes nothing about its worth, which is not a denial | Harm |
| **O18, O41, O37, O38, O16, O2, O20, O40** | M35; M37, M44; M49; M38; M32; M23; M40 | The file-10 mark: the baseline against 01 (O18, O41, O37 baseline AGREE, 01 SPLIT; O20, O40 baseline SILENT, 01 AGREE; O16 disputed between the case readers; O38 and O2 differ from the pre-reading's expectations) | Toward, or no change |
| any row | M7 | Any file-11 reading that uses L37 to set aside L27 or L63 | Reading note |

---

## 7. Where Claude's pre-reading changed after reading the returns

Lesson S2: every change is recorded with its reason.

**7.1 Rulings changed.**
1. **M24 (C41 sentence 1), WORDING → CLAIM (narrowed).** f10 L294: "A true mechanism guessed for bad reasons satisfies (E)". f11 L279: "(E) does not exclude a true mechanism guessed for bad reasons".
   - File 10's sentence asserts all five conjuncts of (E) of every such mechanism. Truth gives at most fidelity, not non-vacuity's stated scope. So file 10 licenses B's TEST conclusion and file 11 does not.
   - The same section's mirror change, M22 ("not excluded" → "is an account"), is CLAIM by every reader. The same file-11 paragraph keeps "satisfies (E)" for the proof (L279 s4).
   - The pre-reading relied on file 10's heading "What (E) does not exclude". Raised by B, Atria and Mimo.
2. **M27 (C44), CLAIM (application) → ORDER.** The pre-reading's reason was that file 10 "never says that an addition is that case". That fails on f10 L326: "the full candidate fails although a subset succeeds. Success of a subset does not imply success of the whole", stated in general form. f10 L310 already says upward closure is not assumed. "Applies only where its assumptions hold" is what the conditional theorem means. Raised by B, Atria and Mimo; A hedged.
3. **M5 (C9 part a), in form only.** The pre-reading ruled the C9 section ORDER and ruled the "invokes worth" phrase at C65. Step 4 splits the phrase out and rules it CLAIM, because file 10 does not state the worth trigger anywhere. It is counted once with M47, so the ruling on the change is unchanged.

**7.2 Places split.**
- C9 becomes M5 (s1) and M6 (s2–s4), because the readers mark them separately.
- C41 becomes sentence 1 (M24, CLAIM) and sentence 2 (WORDING, unchanged).
- C22 enters the master list as its (D) short form only (M12, ORDER, unchanged).

**7.3 Grades changed (rulings unchanged).**
- M23 (C40), M26 (C43), M30 (C48), M33 (C51) and M34 (C52): *new* → *application*. Claude's case rulings (01) hold each derivable from file 10, but file 10 does not state it.
- M32 (C50): *application* → *new*. File 10's leaf definition does not exclude a reconstructed record (01, O16).

**7.4 Reasoning corrected by the verification (no ruling changes).**
1. **M5.** R1 counts it among its 13 CLAIM places and R3 counts M47. The change is counted once in section 2.
2. **M11.** f11 L421 defines complete and creative critical episodes, not "episode". The WORDING ruling rests on the generic reading and on f11 L199, L578 and L594.
3. **M48.** \(O\) and \(P\) are already supplied data in file 10 (f10 L164, L438). The CLAIM rests on the occasions, the appropriateness input and the unsettled-verdict rule.
4. **M51.** L63's "(B) their necessity" does not tell the reader what "preserve" means; read that way it would widen the refuter. The support is f11 L191, where faithfulness is the fidelity conditions. L63's label is loose (an erratum candidate).
5. **XR1.** "L63 did not change" should read "L63's claim did not change". L63 is new wording, ruled ORDER at M12.

**7.5 Cross-references added.** NEW-XR1 to NEW-XR6 were not in the pre-reading's table. All six are ruled CORRECT. NEW-XR1 was raised as wrong by A, B and Mimo (section 5). XR1–XR12 keep the pre-reading's rulings: XR1–XR7 SLIP, XR8–XR12 CORRECT.

**7.6 Held against readers, with the reason.**
- **M2 (C3), M11 (C20), M16 (C29).** All four readers say CLAIM; the pre-reading is kept.
  - M2: the body states "blind" as no represented target in both files, and B concedes "a close call".
  - M11: file 11's body presupposes episodes without a contract change.
  - M16: file 10 states the general rule at L168, L378 and L603, which no reader cites.
- **M6, M9, M10, M15.** Some readers say CLAIM; the pre-reading is kept.
  - M6: f10 L597.
  - M9: Part XV and "Anything else is a detail".
  - M10: f11 L39 and L157.
  - M15: f10 L272, L41 and f11 L277.
- **M51.** Mimo's NEW1 is not followed: f10 L535 already carries f11 L530, as Mimo itself notes.
- **M43.** Atria's WORDING is not followed. Its derivability point is the *application* grade.
- **XR3.** Atria's CORRECT is not followed: no place carries a probability of truth.

**7.7 Case expectations the pre-reading made that 01 does not bear out.** These are for step 3, not step 4. On O2 the pre-reading expected SPLIT under file 10, and on O38 SPLIT or DISAGREE; 01 has AGREE on both. Both are in the step-3 rows above.

---

## 8. Also recorded for a later revision (not pointers, outside test (d))

These are unclear wordings and tensions inside file 11. None changes a ruling above.
1. **Membership of the population.** L473 has "realized" and "admit"; L562 has "admitted, realizable, a member of \(\mathcal T\)". (M46, M54)
2. **"Everything else is derived"** at L33 and L512 stands against the declared inputs of L514. (M48, XR10)
3. **Boundary, continuity and the contract** are declared indices at L33 and L516, and declared inputs at L514. (M48)
4. **\(\mathcal N\)** is a "declared input" at L27 and L447, but L514 excludes it as a primitive. (M42, M48, XR3, XR5)
5. **Derivation 6.** Its claim (L586) includes declared inputs; the order its proof cites (L518) lists none. (M58, XR6)
6. **The Derivation 10 gloss** at L616 describes Derivation 3's qualification inexactly. (M59, XR7)
7. **"The right question"** (L536, L582) stands beside "says nothing about its worth" (L582), a mild strain. (M57)
8. **Labels.** The labels (A)–(E) of Part XV share letters with the body tags (A), (B), (D) and (E), and L63's "(B) their necessity" is loose. (XR8, M12, M51)
9. **"today"** in L419, "the system's own today whoever wrote it", has no counterpart in L465. (M37)
10. **"the supports actually written"** at L301 has two readings, one of which narrows (S). (M26)
11. **"appears anywhere"** at L33 s4 must mean L590's "no residual predicate"; file 11 itself mentions "is a cause" at L55, L123 and L129. (M6)
12. **The note's own claims.** "the same … definitions" is false against L419, L433, L465, L473 and L514, and "Nothing else changes in what is claimed" is false against 41 places. (M1)

---

## 9. Files

The working files are kept in `raw readings/` as written:

| committed as | working name | content |
|---|---|---|
| `03a alignment.md` | `alignment.md` | the mapping of every 1D record and 2D item to the pre-reading's places; the master list (its section 3) |
| `03b rulings R1.md` | `rulings R1.md` | rulings on M1–M21 |
| `03c rulings R2.md` | `rulings R2.md` | rulings on M22–M41 |
| `03d rulings R3.md` | `rulings R3.md` | rulings on M42–M59 and on every cross-reference |
| `03e verification.md` | `verification.md` | the adversarial verification of 28 rulings |

The rulings refer to the working files `master R1.md`, `master R2.md`, `master R3.md` and `master XR.md`, and to each other by their working names. The master files are not kept. The place list they held is section 3 of 03a. The cross-reference list, with every reader's ruling, is the table in 03d.
