# S81 step 4, alignment of the difference readings

**What this is.** The alignment step 4 rules from. It maps every place on the two 1D lists and in the two 2D audits to the places of Claude's pre-reading (C1–C81, XR1–XR12), and builds the master list of places step 4 must rule CLAIM or WORDING. Written by Claude, 23 September 2026. No ruling is made here.

**Step 4 (plan, second version).** "every CLAIM place on either 1D list, and every place in either 2D's "Surviving differences in claim" or "Differences in claim that both lists missed", read against both files and ruled CLAIM or WORDING."

**Opened.**
- File 10 and file 11 (`Semantics/authority/10 …md`, `11 …, revision 1.md`), by line and by `grep`.
- Claude's pre-reading, `Semantics/results/S81 File 11 against every case - outputs/determination/02 Claude's reading of the differences between file 10 and file 11, written before opening the 1D lists.md`, in full.
- The four returns in full: `returns/s81_1D_A.response.txt`, `returns/s81_1D_B.response.txt`, `returns/s81_2D_atria.response.txt`, `returns/s81_2D_mimo.response.txt`.
- The instruction heads of `briefs/s81_1D_A.txt` (lines 1–56) and `briefs/s81_2D_atria.txt` (lines 1–62), and the section markers of both briefs. Brief 2D Atria's list under audit (lines 1317–1904) was compared by `diff` with `s81_1D_A.response.txt` and is identical. `grep -c "Revision 1"` on both briefs gave 0.
- The S81 plan, second version: the lines on 2D, P3, E1 and the determination steps. The third version: a `grep` for step 4, P3, E1 and 2D.
- Seen, names only: an `ls` of `outputs/`, `determination/`, `raw readings/`, `briefs/` and a filtered `ls` of `returns/` (1D and 2D names); a final `git status` of the repository showed the names of untracked files in `returns/effort controls/`. None of these was opened.
- Not opened: any 1C, 1K, 2a or 2b return, any reasoning file, any receipt, the pass-2 void files, the effort-controls folder, the sample JSONs, `stage1/`, any table, the briefs for tester B and for Mimo, the raw readings 02a and 02b, and Claude's case rulings 01.

---

## 0. How each return is built

**1D (brief `s81_1D_A.txt`).** One record per place, "### D1" onward, each with PART, A (the file-10 sentence, or NONE), B (the file-11 sentence, or DROPPED), MARK (CLAIM or WORDING), WHY, TEST. The brief has no ORDER mark on a record; "## ORDER" is a per-Part count of moved sentences. Then "## Cross-references in Text B" (CHECKED, WRONG, one bullet per wrong pointer), "## Counts", "## Noticed beyond the differences". Text A is file 10. Text B is file 11 without its revision note (L5).

**2D (brief `s81_2D_atria.txt`).** "## Part 1 - Every CLAIM record on either list" (per record: AT, IN THE OTHER LIST, ON THE QUOTES, ON THE MARK, YOUR MARK); "## Part 2 - WORDING records you would mark CLAIM"; "## Differences in claim that both lists missed" (COUNT, NEW records); "## Cross-references" (COUNT, bullets CONFIRMED or DISPUTED); "## Surviving differences in claim" (COUNT, one bullet each with record numbers).

**Which list each auditor audits.** Atria: AUDIT = tester A's list, SECOND = tester B's (checked by `diff`, above). Mimo: AUDIT = B's, SECOND = A's (plan, second version, line 58: "`s81_2D_mimo` (under audit: B's; second: A's)"; Mimo's cross-numbers agree with this throughout).

**Claude-pre.** Rulings CLAIM, WORDING, ORDER at 81 places; 48 CLAIM (two meta: C1, C10), 22 WORDING, 11 ORDER. Cross-references XR1–XR12: XR1–XR7 SLIP, XR8–XR12 CORRECT, none CLAIM-CHANGING.

---

## 1. The 1D lists

Line numbers are file 11's unless marked f10. "M" is the master id (section 3). A C-id with a part letter or sentence number marks a place Claude-pre holds as one row and the master list splits.

### 1.1 Tester A: 68 records, 55 CLAIM, 13 WORDING

| A id | Part (A's label) | f11 place | mark | C-id | M |
|---|---|---|---|---|---|
| D1 | 0, What this document claims | L15 s3 | CLAIM | C3 | M2 |
| D2 | 0, What this document claims | L13 s2 | WORDING | C2 | — |
| D3 | 0, does not claim | L27 s1–s2 | CLAIM | C7 | M3 |
| D4 | 0, does not claim | L27 s3 | CLAIM | C8 | M4 |
| D5 | 0, What is primitive… (A text: f10 L519) | L33 s1 | CLAIM | C9 part a | M5 |
| D6 | 0, What is primitive… (A text: f10 L525) | L33 s4 | CLAIM | C9 part b | M6 |
| D7 | 0, Grievances, anticipated | L37 | CLAIM | C10 | M7 |
| D8 | 0, Grievance 1 | L39 | WORDING | C11 | — |
| D9 | 0, Grievance 3 | L43 | CLAIM | C13 | M8 |
| D10 | 0, Grievance 5 | L47 | CLAIM | C15 | M9 |
| D11 | 0, Grievance 6 | L49 | WORDING | C16 | — |
| D12 | 0, Grievance 8 | L53 | WORDING | C18 | — |
| D13 | 0, Grievance 9 | L55 | CLAIM | C19 | M10 |
| D14 | 0, Grievance 10 | L57 | CLAIM | C20 | M11 |
| D15 | 0, Where to attack this | L63 s1 | WORDING | C22 | M12 (listed as WORDING) |
| D16 | 0, What this document claims | L19 last | WORDING | C5 | — |
| D17 | II, Kinds are edit-signatures | L121 | WORDING | C24 | — |
| D18 | II, Kinds are edit-signatures | L129 s4–s5 | CLAIM | C25 | M13 |
| D19 | III, The respect is the query | L153 last | CLAIM | C26 | M14 |
| D20 | III, Scope… (A text: f10 L272) | L161 s1 | CLAIM | C28 | M15 |
| D21 | III, Scope… (A text: f10 L456) | L161 s2 | CLAIM | C29 | M16 |
| D22 | III, Scope… | L161 s3 | CLAIM | C30 | M17 |
| D23 | III, Scope… | L163 last | CLAIM | C31 | M18 |
| D24 | IV, Three provenances | L197 last | CLAIM | C32 | M19 |
| D25 | IV, Representation is derived | L213 last | CLAIM | C33 | M20 |
| D26 | IV, Expectation, surprise, violation | L225 s3 | WORDING | C34 | — |
| D27 | IV, Expectation, surprise, violation | L225 last | CLAIM | C35 | M21 |
| D28 | V, What (E) excludes… | L271 s2–s3 | CLAIM | C38 | M22 |
| D29 | V, What (E) excludes… (A text: f10 L338) | L273 s2 | WORDING | C39 | — |
| D30 | V, What (E) excludes… | L275 s2 | CLAIM | C40 | M23 |
| D31 | V, What (E) excludes… | L279 s2 | WORDING | C41 s2 | — |
| D32 | V, What (E) excludes… | L279 s3 | CLAIM | C42 | M25 |
| D33 | VI | L301 s2 | CLAIM | C43 | M26 |
| D34 | VI | L307 last | CLAIM | C44 | M27 |
| D35 | VI, Redundant routes | L309 s3 | CLAIM | C45 | M28 |
| D36 | VII, Explanations that remove structure | L337 | WORDING | C46 | — |
| D37 | VIII | L363 s1 | CLAIM | C47 | M29 |
| D38 | VIII | L363 s2 | CLAIM | C48 | M30 |
| D39 | IX, Histories | L371 last | CLAIM | C49 | M31 |
| D40 | IX, Receipts | L393 last | CLAIM | C50 | M32 |
| D41 | X, Deployment | L399 last | CLAIM | C51 | M33 |
| D42 | X, Construction | L401 s4 | CLAIM | C52 | M34 |
| D43 | X, Construction | L401 s5 | CLAIM | C53 | M35 |
| D44 | X, Origin | L417 last | CLAIM | C54 | M36 |
| D45 | X, Ownership | L419 s1–s2 | CLAIM | C55 | M37 |
| D46 | X, Ownership | L419 s3 | CLAIM | C55 | M37 |
| D47 | XI, Repair | L433 s1–s2 | CLAIM | C56 + C57 | M38, M39 |
| D48 | XI, Repair | L433 s4 | CLAIM | C58 | M40 |
| D49 | XI, Repair | L433 s5 | CLAIM | C59 | M41 |
| D50 | XI, Worth… | L447 s1 | CLAIM | C60 | M42 |
| D51 | XI, Worth… | L447 s2–s3 | CLAIM | C60 | M42 |
| D52 | XI, Worth… | L447 last | CLAIM | C61 | M43 |
| D53 | XII, System boundary and continuity | L465 | CLAIM | C62 | M44 |
| D54 | XII, Owned capability | L467 last | CLAIM | C63 | M45 |
| D55 | XII, Selection in the physical module | L473 last | CLAIM | C64 | M46 |
| D56 | XIV, Primitives | L510 | CLAIM | C65 | M47 |
| D57 | XIV, Declared inputs | L514 | CLAIM | C66 | M48 |
| D58 | XIV, Dependence order | L518 last | CLAIM | C67 | M49 |
| D59 | XV (A) | L528 s2–s3 | CLAIM | C70 (quote spans C69 s2) | M50 |
| D60 | XV (D) (A text joins f10 L74 and L539) | L534 | CLAIM | C73 | M52 |
| D61 | XV (B) (A text: f10 L70 s2) | L530 s2 | WORDING | C71 | M51 (listed as WORDING) |
| D62 | XV (C) (A text: f10 L72) | L532 | WORDING | C72 | — |
| D63 | XVI, 3 (title in PART line) | L562 (L560) | CLAIM | C76 (C75 in PART line) | M54 (M53) |
| D64 | XVI, 3 | L564 | CLAIM | C77 | M55 |
| D65 | XVI, 3 | L566 | CLAIM | C78 | M56 |
| D66 | XVI, 5 | L582 last | CLAIM | C79 | M57 |
| D67 | XVI, 6 | L586 | CLAIM | C80 | M58 |
| D68 | XVI, 10 | L616 | CLAIM | C81 | M59 |

- **Counts:** A's own count line reads "CLAIM: 55" and "WORDING: 13"; both match its records. The 55 CLAIM records fall on 54 master places (D45 and D46 on M37; D50 and D51 on M42; D47 on M38 and M39).
- **CLAIM records on Claude-pre WORDING or ORDER places:** D1 (C3), D5 (C9a), D6 (C9b), D10 (C15), D13 (C19), D14 (C20), D20 (C28), D21 (C29). Eight.
- **Claude-pre CLAIM places A does not mark CLAIM:** C1 (not in A's text), C75 (only in D63's PART line). None is marked WORDING by A.
- **"## ORDER":** "COUNT: 1", Part XV: "A's closing sentence "None of these is protected by notation, by the availability of this document, or by any version label." moves to the opening paragraph of B's Part XV". This is C68 (f10 L545, f11 L526), ORDER in Claude-pre.
- **"## Cross-references in Text B":** "CHECKED: 169", "WRONG: 0". No bullets.
- **"## Noticed beyond the differences" (COUNT 12), mapped:** (1) "four" conditions vs five conjuncts, both texts: XR8-related. (2) non-vacuity's last sentence grounds its verdict in non-circular dependence, both texts: no place. (3) f10 L68 against f10 L284: C70. (4) f10 Derivation 3 proof assumes membership in \(\mathcal T\): C77, and C1's "already assumed". (5) f11 L271 "is an account" needs more than (F1): C38. (6) f11 L562 near-tautology: C76. (7) f11 L616 inexact: XR7. (8) "(Derivation 2)", both texts: NEW-XR1. (9) f11 L33 "Everything else is derived" against L514: XR10, C66 tension. (10) f11 L33 indices against L514 inputs: C66 tension. (11) f11 L37 against Grievance 5: C10. (12) f11 L301 "actually written" against (S): C43; "today" at L419: C55.

### 1.2 Tester B: 72 records, 52 CLAIM, 20 WORDING

| B id | Part (B's label) | f11 place | mark | C-id | M |
|---|---|---|---|---|---|
| D1 | 0, What this document claims | L15 s3 | CLAIM | C3 | M2 |
| D2 | 0, does not claim | L27 s1–s2 | CLAIM | C7 | M3 |
| D3 | 0, does not claim | L27 s3 | CLAIM | C8 | M4 |
| D4 | 0, What is primitive… (A: NONE) | L33 s1 | CLAIM | C9 part a | M5 |
| D5 | 0, What is primitive… (A: NONE) | L33 s2–s4 | WORDING | C9 part b | M6 |
| D6 | 0, Grievances, anticipated | L37 | CLAIM | C10 | M7 |
| D7 | 0, Grievance 1 | L39 s4–s5 | WORDING | C11 | — |
| D8 | 0, Grievance 3 | L43 | CLAIM | C13 | M8 |
| D9 | 0, Grievance 4 | L45 | WORDING | C14 | — |
| D10 | 0, Grievance 5 | L47 | WORDING | C15 | M9 |
| D11 | 0, Grievance 6 | L49 | WORDING | C16 | — |
| D12 | 0, Grievance 9 | L55 | WORDING | C19 | M10 |
| D13 | 0, Grievance 10 | L57 | CLAIM | C20 | M11 |
| D14 | 0, Where to attack this | L63 s1 | WORDING | C22 | M12 |
| D15 | 0 Where to attack (B) / XV (B) (A text: f10 L70 s2) | L530 s2 | WORDING | C71 | M51 |
| D16 | II, Kinds are edit-signatures | L121 | WORDING | C24 | — |
| D17 | II, Kinds are edit-signatures | L129 s4–s5 | CLAIM | C25 | M13 |
| D18 | III, The respect is the query | L153 last | CLAIM | C26 | M14 |
| D19 | III, Scope… (A: NONE) | L161 s1 | WORDING | C28 | M15 |
| D20 | III, Scope… | L161 s2 | CLAIM | C29 | M16 |
| D21 | III, Scope… | L161 s3 | CLAIM | C30 | M17 |
| D22 | III, Scope… | L163 last | CLAIM | C31 | M18 |
| D23 | IV, Three provenances | L197 last | CLAIM | C32 | M19 |
| D24 | IV, Representation is derived | L213 last | CLAIM | C33 | M20 |
| D25 | IV, Expectation, surprise, violation | L225 s3 | WORDING | C34 | — |
| D26 | IV, Expectation, surprise, violation | L225 last | CLAIM | C35 | M21 |
| D27 | V | L271 s2–s3 | CLAIM | C38 | M22 |
| D28 | V (A: NONE) | L273 s2 | WORDING | C39 | — |
| D29 | V | L275 s2 | CLAIM | C40 | M23 |
| D30 | V | L279 s1 | CLAIM | C41 s1 | M24 |
| D31 | V | L279 s2 | WORDING | C41 s2 | — |
| D32 | V | L279 s3 | CLAIM | C42 | M25 |
| D33 | VI | L301 s2 | CLAIM | C43 | M26 |
| D34 | VI, Finite monotone theorem | L307 last | WORDING | C44 | M27 |
| D35 | VI, Redundant routes | L309 s3 | CLAIM | C45 | M28 |
| D36 | VII | L337 | WORDING | C46 | — |
| D37 | VIII, Recoding | L363 s1 | CLAIM | C47 | M29 |
| D38 | VIII, Recoding | L363 s2 | CLAIM | C48 | M30 |
| D39 | IX, Histories | L371 last | CLAIM | C49 | M31 |
| D40 | IX, Receipts | L393 last | CLAIM | C50 | M32 |
| D41 | X, Deployment | L399 last | CLAIM | C51 | M33 |
| D42 | X, Construction | L401 s4 | CLAIM | C52 | M34 |
| D43 | X, Construction | L401 s5 | CLAIM | C53 | M35 |
| D44 | X, Origin | L417 last | CLAIM | C54 | M36 |
| D45 | X, Ownership | L419 s1–s2 | CLAIM | C55 | M37 |
| D46 | X, Ownership | L419 s3 | CLAIM | C55 | M37 |
| D47 | XI, Repair | L433 s1 | CLAIM | C56 | M38 |
| D48 | XI, Repair | L433 s2 | CLAIM | C57 | M39 |
| D49 | XI, Repair | L433 s4 | CLAIM | C58 | M40 |
| D50 | XI, Repair | L433 s5 | CLAIM | C59 | M41 |
| D51 | XI, Worth… | L447 s1 | CLAIM | C60 | M42 |
| D52 | XI, Worth… | L447 s2 | CLAIM | C60 | M42 |
| D53 | XI, Worth… | L447 s3 | WORDING | C60 (s3) | M42 |
| D54 | XI, Worth… | L447 last | CLAIM | C61 | M43 |
| D55 | XII, System boundary and continuity | L465 | CLAIM | C62 | M44 |
| D56 | XII, Owned capability | L467 last | CLAIM | C63 | M45 |
| D57 | XII, Selection in the physical module | L473 last | CLAIM | C64 | M46 |
| D58 | XIV, Primitives | L510 | CLAIM | C65 | M47 |
| D59 | XIV, Declared inputs | L514 | CLAIM | C66 | M48 |
| D60 | XIV, Dependence order | L518 last | CLAIM | C67 | M49 |
| D61 | XV (A) | L528 s3 | CLAIM | C70 | M50 |
| D62 | XV (A) (A text: f10 L533) | L528 s1 | WORDING | C69 | — |
| D63 | XV (D) (A text: f10 L539) | L534 | CLAIM | C73 | M52 |
| D64 | XV (E) (A text: f10 L76) | L536 | WORDING | C74 | — |
| D65 | XVI, 3 (both titles in PART line) | L562 (L560) | CLAIM | C76 (C75 in PART line) | M54 (M53) |
| D66 | XVI, 3 | L564 | CLAIM | C77 | M55 |
| D67 | XVI, 3 | L566 | CLAIM | C78 | M56 |
| D68 | XVI, 5 | L582 last | CLAIM | C79 | M57 |
| D69 | XVI, 6 | L586 | CLAIM | C80 | M58 |
| D70 | XVI, 10 | L616 | CLAIM | C81 | M59 |
| D71 | 0, What this document claims | L19 last | WORDING | C5 | — |
| D72 | 0, Grievance 2 | L41 | WORDING | C12 | — |

- **Counts:** B's own count line reads "CLAIM: 52" and "WORDING: 20"; both match its records. The 52 CLAIM records fall on 50 master places (D45 and D46 on M37; D51 and D52 on M42).
- **CLAIM records on Claude-pre WORDING or ORDER places:** D1 (C3), D4 (C9a), D13 (C20), D20 (C29), D30 (C41 s1). Five.
- **WORDING records on Claude-pre CLAIM places:** D34 (C44), D53 (C60, the aesthetic-case sentence only).
- **Claude-pre CLAIM places B does not mark CLAIM:** C1 (not in B's text), C44 (WORDING), C75 (only in D65's PART line).
- **"## ORDER":** "COUNT: 1", Part XV, the same sentence as A's. C68, ORDER in Claude-pre.
- **"## Cross-references in Text B":** "CHECKED: 178", "WRONG: 0". No bullets.
- **"## Noticed beyond the differences" (COUNT 10), mapped:** (1) f11 L27 "(Parts XI, XIV)" covers only worth: XR3. (2) f11 L33 "Everything else is derived" against L514: XR10, C66 tension. (3) "today" at L419: C55. (4) f11 L616 inexact: XR7. (5) "(Derivation 2)", both texts: NEW-XR1. (6) f10 Derivation 3 proof assumes membership: C77, C1. (7) f10 L68 against L284: C70. (8) "pair" of a quadruple; four conditions vs five conjuncts, both texts: XR8-related. (9) surprise and constructed-only systems, both texts: no place. (10) no (I3) label, both texts: a label gap (master XR.md, remarks).

### 1.3 Places both lists hold, and places one list alone holds
- **A alone (3 records):** D2 (C2), D12 (C18), D62 (C72). All WORDING.
- **B alone (5 records):** D9 (C14), D30 (C41 s1), D62 (C69), D64 (C74), D72 (C12). All WORDING except D30 (CLAIM).
- **Overlapping cuts:** A's D6 (L33 s4) lies inside B's D5 (L33 s2–s4); A's D47 covers B's D47 and D48 (C56, C57); A's D51 (L447 s2–s3) covers B's D52 and D53. Every other record pairs one to one with a record on the other list.
- **Marks differ on the same place:** C9 part b (A CLAIM, B WORDING), C15 (A CLAIM, B WORDING), C19 (A CLAIM, B WORDING), C28 (A CLAIM, B WORDING), C44 (A CLAIM, B WORDING), C60 s3 (A CLAIM inside D51, B WORDING in D53). C41 s1 is B CLAIM with no A record.
- Neither list has a record for C1 (the note is not in their text) or a record of its own for C75.

### 1.4 E1: the Part XI Repair occasions clause (C56, f11 L433 s1)

E1 (plan, second version, read with its "model reads tester" line): "at least one model marks the occasions clause CLAIM in 1D", scored on the 1D lists of A and B.

- **Tester A, D47.** PART: "Part XI — Progress, knowledge, and the normative ("Repair")". A: "(P) does not rank alternatives." B: "The obligations are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers. Their declaration makes no claim that the aims are worth pursuing, and (P) does not rank alternatives." **MARK: CLAIM.** WHY: "B makes \(O\) and \(P\) declared inputs with stated occasions, gives an exact loss condition, and denies any worth claim; A has only "(P) does not rank alternatives"." TEST: "A protected condition fails on an occasion it does not cover: B says it is not lost; A gives no rule." The record joins the occasions clause (C56) with the next sentence (C57). Its WHY and TEST name the occasions and the loss condition.
- **Tester B, D47.** PART: "Part XI — Progress, knowledge, and the normative (Repair)". A: NONE. B: the occasions sentence alone, from "The obligations are declared inputs:" to "fails on an occasion it covers." **MARK: CLAIM.** WHY: "B makes the obligations declared inputs over stated occasions and defines loss exactly; A only says they are "fixed for the comparison"." TEST: "A protected condition fails on an occasion outside its stated coverage: B says it is not lost; A gives no criterion." B marks C57 separately (D48, CLAIM).
- **Facts for E1:** both testers mark the occasions clause CLAIM on their 1D lists. Neither marks it WORDING. Both TESTs use the same direction of the "exactly when" (a failure on an uncovered occasion is not a loss).
- **The 2D audits on the same place:** Atria AUDIT D47 (AGREE, CLAIM; other list "SECOND D47 and SECOND D48") and SECOND D47 (AGREE, CLAIM); Mimo AUDIT D47 (AGREE, CLAIM) and SECOND D47 (AGREE, CLAIM). Both 2D surviving lists carry it.

---

## 2. The 2D returns

### 2.1 Atria (AUDIT = A's list, SECOND = B's list)

- **Part 1:** 107 records (AUDIT 55, SECOND 52), one for every CLAIM record on either list. 104 YOUR MARK CLAIM, 3 WORDING. The three WORDING: AUDIT D34 (C44, DISAGREE), AUDIT D52 (C61, DISAGREE), SECOND D54 (C61, DISAGREE). ON THE QUOTES: MATCH on every record.
- **Part 2, WORDING records it would mark CLAIM:** SECOND D5 (C9b, "its last sentence asserts no such predicate appears anywhere"), SECOND D10 (C15), SECOND D12 (C19), SECOND D19 (C28). None from A's WORDING records.
- **"## Differences in claim that both lists missed":** "COUNT: 0", with the line "No further difference in claim survives a section-by-section check of the two texts; every claim-level change from A to B is recorded on at least one of the two lists."
- **"## Cross-references":** "COUNT: 0", with one prose line naming re-checked pointers as correct: XR3, XR9, XR11 or NEW-XR5, XR8 and XR12 and NEW-XR6 ("the Part XV pointers"), NEW-XR2, NEW-XR3, NEW-XR4 (master XR.md).
- **"## Surviving differences in claim": "COUNT: 54".** Item by item, with Atria's record numbers:

| # | Atria's place (short) | records | C-id | M |
|---|---|---|---|---|
| 1 | 0, claims: selection no longer blind on predictions | AUDIT D1, SECOND D1 | C3 | M2 |
| 2 | 0, does not claim: empty places become declared inputs | AUDIT D3, SECOND D2 | C7 | M3 |
| 3 | 0, does not claim: credit disclaimer | AUDIT D4, SECOND D3 | C8 | M4 |
| 4 | 0, primitive: \(\mathcal N\) for worth | AUDIT D5, SECOND D4 | C9 part a | M5 |
| 5 | 0, primitive: no predicate appears anywhere | AUDIT D6, SECOND D5 | C9 part b | M6 |
| 6 | 0, grievances: front matter subordinate to body | AUDIT D7, SECOND D6 | C10 | M7 |
| 7 | 0, Grievance 3 | AUDIT D9, SECOND D8 | C13 | M8 |
| 8 | 0, Grievance 5 | AUDIT D10, SECOND D10 | C15 | M9 |
| 9 | 0, Grievance 9 | AUDIT D13, SECOND D12 | C19 | M10 |
| 10 | 0, Grievance 10 | AUDIT D14, SECOND D13 | C20 | M11 |
| 11 | II, reading part is a measurement | AUDIT D18, SECOND D17 | C25 | M13 |
| 12 | III, measure answers identification | AUDIT D19, SECOND D18 | C26 | M14 |
| 13 | III, stated scope makes a contract | AUDIT D20, SECOND D19 | C28 | M15 |
| 14 | III, new-index rule generalized | AUDIT D21, SECOND D20 | C29 | M16 |
| 15 | III, appropriateness criticizable | AUDIT D22, SECOND D21 | C30 | M17 |
| 16 | III, replacement query | AUDIT D23, SECOND D22 | C31 | M18 |
| 17 | IV, population part of the claim | AUDIT D24, SECOND D23 | C32 | M19 |
| 18 | IV, provenance and derived record | AUDIT D25, SECOND D24 | C33 | M20 |
| 19 | IV, counterfactual openness | AUDIT D27, SECOND D26 | C35 | M21 |
| 20 | V, table is an account | AUDIT D28, SECOND D27 | C38 | M22 |
| 21 | V, packaging fails non-circularity | AUDIT D30, SECOND D29 | C40 | M23 |
| 22 | V, bad reasons: "not excluded" | SECOND D30 | C41 s1 | M24 |
| 23 | V, coarse account | AUDIT D32, SECOND D32 | C42 | M25 |
| 24 | VI, supports actually written | AUDIT D33, SECOND D33 | C43 | M26 |
| 25 | VI, redundant routes | AUDIT D35, SECOND D35 | C45 | M28 |
| 26 | VIII, reader-based recoding | AUDIT D37, SECOND D37 | C47 | M29 |
| 27 | VIII, section filled from another source | AUDIT D38, SECOND D38 | C48 | M30 |
| 28 | IX, active routes | AUDIT D39, SECOND D39 | C49 | M31 |
| 29 | IX, receipts | AUDIT D40, SECOND D40 | C50 | M32 |
| 30 | X, narrow retained use | AUDIT D41, SECOND D41 | C51 | M33 |
| 31 | X, construction without observation | AUDIT D42, SECOND D42 | C52 | M34 |
| 32 | X, small binding | AUDIT D43, SECOND D43 | C53 | M35 |
| 33 | X, port | AUDIT D44, SECOND D44 | C54 | M36 |
| 34 | X, ownership by boundary | AUDIT D45, SECOND D45 | C55 | M37 |
| 35 | X, ownership not by capability | AUDIT D46, SECOND D46 | C55 | M37 |
| 36 | XI, obligations declared inputs, occasions, loss, no worth claim | AUDIT D47, SECOND D47 and SECOND D48 | C56 + C57 | M38, M39 |
| 37 | XI, ProducedBy | AUDIT D48, SECOND D49 | C58 | M40 |
| 38 | XI, three attributions | AUDIT D49, SECOND D50 | C59 | M41 |
| 39 | XI, repair establishes nothing about worth | AUDIT D50, SECOND D51 | C60 (s1) | M42 |
| 40 | XI, \(\mathcal N\) for any worth | AUDIT D51, SECOND D52 | C60 (s2) | M42 |
| 41 | XII, boundary and continuity | AUDIT D53, SECOND D55 | C62 | M44 |
| 42 | XII, owned capability | AUDIT D54, SECOND D56 | C63 | M45 |
| 43 | XII, population defined | AUDIT D55, SECOND D57 | C64 | M46 |
| 44 | XIV, Primitives | AUDIT D56, SECOND D58 | C65 | M47 |
| 45 | XIV, Declared inputs | AUDIT D57, SECOND D59 | C66 | M48 |
| 46 | XIV, well founded | AUDIT D58, SECOND D60 | C67 | M49 |
| 47 | XV (A) | AUDIT D59, SECOND D61 | C70 | M50 |
| 48 | XV (D) | AUDIT D60, SECOND D63 | C73 | M52 |
| 49 | XVI 3, claim | AUDIT D63, SECOND D65 | C76 | M54 |
| 50 | XVI 3, proof | AUDIT D64, SECOND D66 | C77 | M55 |
| 51 | XVI 3, consequence | AUDIT D65, SECOND D67 | C78 | M56 |
| 52 | XVI 5 | AUDIT D66, SECOND D68 | C79 | M57 |
| 53 | XVI 6 | AUDIT D67, SECOND D69 | C80 | M58 |
| 54 | XVI 10 | AUDIT D68, SECOND D70 | C81 | M59 |

- The 54 items fall on 53 master places. Not surviving: C44 (M27) and C61 (M43), both ruled WORDING in Part 1. No item for C75 alone; C1 is not in its text.

### 2.2 Mimo (AUDIT = B's list, SECOND = A's list)

- **Part 1:** 107 records (AUDIT 52, SECOND 55). 105 YOUR MARK CLAIM, 2 WORDING. The two WORDING: SECOND D13 (A's D13, C19, DISAGREE) and SECOND D34 (A's D34, C44, DISAGREE). ON THE QUOTES: MATCH on every record.
- **Part 2, WORDING records it would mark CLAIM:** AUDIT D5 (C9b, for the last sentence), AUDIT D10 (C15), AUDIT D19 (C28). None from A's WORDING records.
- **"## Differences in claim that both lists missed": "COUNT: 1".** NEW1: PART "Part 0 — Where to attack this (B) / Part XV — What defeats this class (B) Necessity"; A: "Produce a genuine explanation whose organization cannot be captured by *any* transport satisfying component fidelity under *any* physically admitted contract." (f10 L70 s1); B: "A genuine explanation whose organization no transport can preserve under any physically admitted contract." (f11 L530 s1). WHY: "… B's refutation condition is weaker than A's front-matter one even though A's Part XV uses B's wording." This is C71 (Claude-pre ORDER; f10 L535 carries B's words). Master M51.
- **"## Cross-references": "COUNT: 3",** all CONFIRMED: "(Parts XI, XIV)" = XR3; Derivation 10's "Derivation 3's qualification seen from the other side" = XR7; Derivation 10's "(Derivation 2)" = NEW-XR1 ("the error is in both texts").
- **"## Surviving differences in claim": "COUNT: 54".** Item by item, with Mimo's record numbers (AUDIT is B's, SECOND is A's):

| # | Mimo's place (short) | records | C-id | M |
|---|---|---|---|---|
| 1 | 0, claims: selection loses blindness | AUDIT D1 / SECOND D1 | C3 | M2 |
| 2 | 0, does not claim: declared inputs, worth | AUDIT D2 / SECOND D3 | C7 | M3 |
| 3 | 0, does not claim: credit | AUDIT D3 / SECOND D4 | C8 | M4 |
| 4 | 0, primitive: \(\mathcal N\) for worth | AUDIT D4 / SECOND D5 | C9 part a | M5 |
| 5 | 0, primitive: no predicate appears | AUDIT D5 / SECOND D6 | C9 part b | M6 |
| 6 | 0, grievances intro: body governs | AUDIT D6 / SECOND D7 | C10 | M7 |
| 7 | 0, Grievance 3 | AUDIT D8 / SECOND D9 | C13 | M8 |
| 8 | 0, Grievance 5 | AUDIT D10 / SECOND D10 | C15 | M9 |
| 9 | 0, Grievance 10 | AUDIT D13 / SECOND D14 | C20 | M11 |
| 10 | 0 attack (B) / XV (B): capture vs preservation | "(no record on either list)" = NEW1 | C71 | M51 |
| 11 | II, reading part | AUDIT D17 / SECOND D18 | C25 | M13 |
| 12 | III, measure | AUDIT D18 / SECOND D19 | C26 | M14 |
| 13 | III, scope constitutive of a contract | AUDIT D19 / SECOND D20 | C28 | M15 |
| 14 | III, broader question; narrowing general | AUDIT D20 / SECOND D21 | C29 | M16 |
| 15 | III, appropriateness | AUDIT D21 / SECOND D22 | C30 | M17 |
| 16 | III, replacement query | AUDIT D22 / SECOND D23 | C31 | M18 |
| 17 | IV, population part of claim | AUDIT D23 / SECOND D24 | C32 | M19 |
| 18 | IV, provenance | AUDIT D24 / SECOND D25 | C33 | M20 |
| 19 | IV, counterfactual population-relative | AUDIT D26 / SECOND D27 | C35 | M21 |
| 20 | V, table is an account | AUDIT D27 / SECOND D28 | C38 | M22 |
| 21 | V, packaging | AUDIT D29 / SECOND D30 | C40 | M23 |
| 22 | V, bad reasons | AUDIT D30 / ABSENT | C41 s1 | M24 |
| 23 | V, coarse accounts | AUDIT D32 / SECOND D32 | C42 | M25 |
| 24 | VI, supports actually written | AUDIT D33 / SECOND D33 | C43 | M26 |
| 25 | VI, redundant routes | AUDIT D35 / SECOND D35 | C45 | M28 |
| 26 | VIII, recoding | AUDIT D37 / SECOND D37 | C47 | M29 |
| 27 | VIII, filled section | AUDIT D38 / SECOND D38 | C48 | M30 |
| 28 | IX, histories | AUDIT D39 / SECOND D39 | C49 | M31 |
| 29 | IX, receipts | AUDIT D40 / SECOND D40 | C50 | M32 |
| 30 | X, deployment | AUDIT D41 / SECOND D41 | C51 | M33 |
| 31 | X, construction without observation | AUDIT D42 / SECOND D42 | C52 | M34 |
| 32 | X, small binding | AUDIT D43 / SECOND D43 | C53 | M35 |
| 33 | X, origin: port | AUDIT D44 / SECOND D44 | C54 | M36 |
| 34 | X, ownership by boundary | AUDIT D45 / SECOND D45 | C55 | M37 |
| 35 | X, ownership not by capability | AUDIT D46 / SECOND D46 | C55 | M37 |
| 36 | XI, \(O\), \(P\) declared inputs over occasions, exact loss | AUDIT D47 / SECOND D47 | C56 | M38 |
| 37 | XI, declaration carries no worth claim | AUDIT D48 / SECOND D47 | C57 | M39 |
| 38 | XI, ProducedBy | AUDIT D49 / SECOND D48 | C58 | M40 |
| 39 | XI, three attributions | AUDIT D50 / SECOND D49 | C59 | M41 |
| 40 | XI, repair establishes nothing about worth | AUDIT D51 / SECOND D50 | C60 (s1) | M42 |
| 41 | XI, \(\mathcal N\) for any worth claim | AUDIT D52 / SECOND D51 | C60 (s2) | M42 |
| 42 | XI, no aesthetics from achievement | AUDIT D54 / SECOND D52 | C61 | M43 |
| 43 | XII, boundary and continuity | AUDIT D55 / SECOND D53 | C62 | M44 |
| 44 | XII, owned capability | AUDIT D56 / SECOND D54 | C63 | M45 |
| 45 | XII, population defined | AUDIT D57 / SECOND D55 | C64 | M46 |
| 46 | XIV, Primitives | AUDIT D58 / SECOND D56 | C65 | M47 |
| 47 | XIV, Declared inputs | AUDIT D59 / SECOND D57 | C66 | M48 |
| 48 | XIV, well founded | AUDIT D60 / SECOND D58 | C67 | M49 |
| 49 | XV (A) | AUDIT D61 / SECOND D59 | C70 | M50 |
| 50 | XV (D) | AUDIT D63 / SECOND D60 | C73 | M52 |
| 51 | XVI 3: claim, proof and consequence together | AUDIT D65, D66, D67 / SECOND D63, D64, D65 | C76, C77, C78 | M54, M55, M56 |
| 52 | XVI 5 | AUDIT D68 / SECOND D66 | C79 | M57 |
| 53 | XVI 6 | AUDIT D69 / SECOND D67 | C80 | M58 |
| 54 | XVI 10 | AUDIT D70 / SECOND D68 | C81 | M59 |

- The 54 items fall on 54 master places (two items on M37, two on M42, one item on M54–M56). Not surviving: C19 (M10) and C44 (M27), both ruled WORDING in Part 1. No item for C75 alone; C1 is not in its text.

---

## 3. The master list

**Rule.** The union of every 1D CLAIM place (A, B), every place in either 2D's "Surviving differences in claim" or "Differences in claim that both lists missed", every Claude-pre CLAIM place, and the P3 named places: Derivation 3 with its three restated sentences (C13, C73, C75–C78, and the L63 short form C22 as the other possible referent of "attack point (D)"), C56 and C66.

**How places are cut.** One master place per Claude-pre place, with three exceptions: C9 is split into part a (L33 s1, the worth phrase) and part b (L33 s2–s4, the predicate sentence), because the readers mark them separately; C41 enters as sentence 1 only (sentence 2 has no CLAIM mark anywhere); C22 enters as the (D) short form at L63 only.

**Size.** 59 places: the 48 Claude-pre CLAIM places, 10 places Claude-pre rules WORDING or ORDER and a reader marks CLAIM (C3, C9a, C9b, C15, C19, C20, C28, C29, C41 s1, C71), and C22's (D) short form, which no reader marks CLAIM.

**Ranges.** R1 = M1–M21 (21 places; before Part 0 to Part IV) in `master R1.md`. R2 = M22–M41 (20; Part V to Part XI, Repair) in `master R2.md`. R3 = M42–M59 (18; Part XI, Worth, to Part XVI) in `master R3.md`. Each file is self-contained.

"all" in the CLAIM column means A, B, Atria-2D, Mimo-2D and Claude-pre.

| M | C | f11 Part | f10 | f11 | CLAIM by | WORDING / ORDER by | flags |
|---|---|---|---|---|---|---|---|
| **R1** | | | | | | | |
| M1 | C1 | before Part 0 | absent | L5 | Claude-pre (meta) | — (unseen by A, B, Atria, Mimo) | the note |
| M2 | C3 | 0 | L13 s3 | L15 s3 | A, B, Atria, Mimo | Claude-pre W (borderline) | |
| M3 | C7 | 0 | L25 | L27 s1–s2 | all | — | XR3 |
| M4 | C8 | 0 | absent | L27 s3 | all | — | |
| M5 | C9 part a | 0 | L519 (L516–519) | L33 s1 | A, B, Atria, Mimo | Claude-pre O | ruled at C65 in Claude-pre |
| M6 | C9 part b | 0 | L521, L523, L525 last, L597 | L33 s2–s4 | A, Atria, Mimo | B W; Claude-pre O | XR10 |
| M7 | C10 | 0 | absent | L37 | all | — | meta |
| M8 | C13 | 0 | L38 | L43 | all | — | named (i); declared |
| M9 | C15 | 0 | L44 | L47 | A, Atria, Mimo | B W; Claude-pre W | |
| M10 | C19 | 0 | L56 | L55 | A, Atria | B W; Mimo W; Claude-pre W | |
| M11 | C20 | 0 | L59 | L57 | A, B, Atria, Mimo | Claude-pre W | |
| M12 | C22, (D) short form | 0 | L66, L74 | L63 s2 | none | A W, B W (on L63 s1); Claude-pre O | named (i) on one reading of XR1 |
| M13 | C25 | II | absent (after L144) | L129 s4–s5 | all | — | |
| M14 | C26 | III | L168 | L153 last | all | — | |
| M15 | C28 | III | L41, L272 | L161 s1 | A, Atria, Mimo | B W; Claude-pre O | |
| M16 | C29 | III | L41, L168, L268, L378, L456 | L161 s2 | A, B, Atria, Mimo | Claude-pre O | |
| M17 | C30 | III | absent | L161 s3 | all | — | input of C66 |
| M18 | C31 | III | L176 | L163 last | all | — | |
| M19 | C32 | IV | L210 | L197 last | all | — | D3 cluster, undeclared |
| M20 | C33 | IV | L226 | L213 last | all | — | |
| M21 | C35 | IV | L238 | L225 last | all | — | D3 cluster, undeclared |
| **R2** | | | | | | | |
| M22 | C38 | V | L284 s2 | L271 s2–s3 | all | — | |
| M23 | C40 | V | L288 | L275 s2 | all | — | XR4 |
| M24 | C41 s1 | V | L294 s1 | L279 s1 | B, Atria, Mimo | Claude-pre W; A no record | |
| M25 | C42 | V | absent | L279 s3 | all | — | |
| M26 | C43 | VI | L316 | L301 s2 | all | — | |
| M27 | C44 | VI | L322 | L307 last | A (hedged), Claude-pre | B W; Atria W; Mimo W | |
| M28 | C45 | VI | L324 | L309 s3 | all | — | |
| M29 | C47 | VIII | absent | L363 s1 | all | — | XR9 |
| M30 | C48 | VIII | absent | L363 s2 | all | — | |
| M31 | C49 | IX | L384 | L371 last | all | — | |
| M32 | C50 | IX | L406 | L393 last | all | — | |
| M33 | C51 | X | L412 | L399 last | all | — | |
| M34 | C52 | X | L414 | L401 s4 | all | — | |
| M35 | C53 | X | L414 | L401 s5 | all | — | |
| M36 | C54 | X | L430 | L417 last | all | — | |
| M37 | C55 | X | absent | L419 | all | — | |
| M38 | C56 | XI | L438–444 | L433 s1 | all (A inside D47 with C57) | — | named (ii); E1 |
| M39 | C57 | XI | L444 | L433 s2 | all (A inside D47; Atria inside a joined item) | — | |
| M40 | C58 | XI | absent (L441) | L433 s4 | all | — | |
| M41 | C59 | XI | absent | L433 s5 | all | — | |
| **R3** | | | | | | | |
| M42 | C60 | XI | L458 | L447 heading, s1–s2 (s3) | all | B W on s3 only | XR5 |
| M43 | C61 | XI | L458 last | L447 last clause | A (hedged), B, Mimo, Claude-pre | Atria W | |
| M44 | C62 | XII | absent | L465 | all | — | input of C66 |
| M45 | C63 | XII | L476 | L467 last | all | — | |
| M46 | C64 | XII | L482 | L473 last | all | — | D3 cluster, undeclared |
| M47 | C65 | XIV | L519 | L510 | all | — | |
| M48 | C66 | XIV | absent | L514 | all | — | named (iii) |
| M49 | C67 | XIV | L525 | L518 last | all | — | |
| M50 | C70 | XV | L68 (and L284) | L528 s3 | all | — | |
| M51 | C71 | XV | L70, L535 | L530 | Mimo (NEW1, s1) | A W, B W (s2); Claude-pre O | |
| M52 | C73 | XV | L74, L539, L541 | L534 | all (Claude-pre: limb 1; limbs 2–3 O) | — | named (i); declared; XR11 |
| M53 | C75 | XVI | L567 | L560 | Claude-pre | — (A, B: PART line only; no 2D item) | named (i); declared |
| M54 | C76 | XVI | L569 | L562 | all | — | named (i); declared |
| M55 | C77 | XVI | L571 | L564 | all | — | named (i); declared |
| M56 | C78 | XVI | L573 | L566 | all | — | named (i); declared |
| M57 | C79 | XVI | L589 | L582 last | all | — | |
| M58 | C80 | XVI | L593 | L586 | all | — | XR6 |
| M59 | C81 | XVI | L623 | L616 | all | — | D3 cluster, undeclared; XR7 |

**Agreement on the master list.**
- CLAIM from every reader who saw it: 44 places (M3, M4, M7, M8, M13, M14, M17–M23, M25, M26, M28–M42, M44–M50, M52, M54–M59).
- CLAIM from Claude-pre alone, the others having no mark of their own: M1 (unseen), M53 (title, PART lines only).
- Claude-pre CLAIM, some reader WORDING: M27 (C44), M43 (C61).
- Claude-pre WORDING or ORDER, some reader CLAIM: M2, M5, M6, M9, M10, M11, M15, M16, M24, M51. Of these, all four other readers mark CLAIM at M2, M5, M11 and M16.
- No reader CLAIM, included as a named-place referent: M12.
- Distinct master places marked CLAIM: A 54, B 50, Atria-2D 53 (surviving), Mimo-2D 54 (surviving), Claude-pre 48.

**P3's two candidate places.** C56 (M38) and C66 (M48) are marked CLAIM by A, B, Atria-2D, Mimo-2D and Claude-pre. No reader marks either WORDING.

**Places the note declares.** C13, C73, C75, C76, C77, C78 (and C22's L63 short form on the other reading of "attack point (D)"). Every other CLAIM-marked place is undeclared; the harm question applies to each.

---

## 4. Cross-references

The master list is `master XR.md`: 18 pointers (XR1–XR12, NEW-XR1–NEW-XR6), each with every reader's ruling.
- A and B list none under "Cross-references in Text B" (WRONG: 0 each). Their pointer remarks sit under "Noticed beyond the differences": XR3 (B), XR7 (A, B), XR8-related (A, B), XR10 (A, B), NEW-XR1 (A, B).
- Atria lists none wrong and names several as correct, XR3 among them.
- Mimo confirms three wrong: XR3, XR7, NEW-XR1.
- Claude-pre: XR1–XR7 SLIP, none CLAIM-CHANGING. NEW-XR1 (L620 "(Derivation 2)", the same in file 10 at L627) is not in Claude-pre's table.
- No reader rules any pointer wrong in a way that changes a claim.

---

## 5. Counts

- **Claude-pre:** 81 places; 48 CLAIM, 22 WORDING, 11 ORDER; 12 XR rows, 7 SLIP.
- **Tester A (1D):** 68 records; 55 CLAIM, 13 WORDING; on 54 distinct master places; ORDER count 1; Cross-references CHECKED 169, WRONG 0; Noticed 12.
- **Tester B (1D):** 72 records; 52 CLAIM, 20 WORDING; on 50 distinct master places; ORDER count 1; Cross-references CHECKED 178, WRONG 0; Noticed 10.
- **Atria (2D):** Part 1, 107 records (104 CLAIM, 3 WORDING); Part 2, 4 (all CLAIM); missed, 0; Cross-references, 0; Surviving, 54 items on 53 master places.
- **Mimo (2D):** Part 1, 107 records (105 CLAIM, 2 WORDING); Part 2, 3 (all CLAIM); missed, 1 (NEW1 = C71); Cross-references, 3; Surviving, 54 items on 54 master places.
- **Master list:** 59 places. R1 21, R2 20, R3 18.
- **Master cross-references:** 18.
- **E1:** tester A marks the occasions clause CLAIM (D47, joined with C57); tester B marks it CLAIM (D47, alone). Two of two.

---

## 6. Malformed or ambiguous in the returns

1. **Joined and split records.** A's D47 joins C56 and C57 in one record, so A's CLAIM on the occasions clause is a CLAIM on a two-sentence record; its WHY and TEST name the occasions and the loss condition. A's D59 quote spans L528 s2–s3 (C69 s2 and C70); its WHY is about C70. A's D60 A-quote joins f10 L74 and L539 (Atria notes it: "A's quote joins its Part 0 and Part XV sentences, both verbatim"). A's D51 B-quote spans L447 s2–s3, where B splits s2 (D52, CLAIM) from s3 (D53, WORDING).
2. **"A: NONE" on relocated sentences.** B gives "A: NONE" for D4, D5, D19 and D28, though its own WHY for each names where file 10 states the matter (Part XIV for D4 and D5, Part V for D19, Part VII for D28). The brief reserves NONE for "the place is in B alone". The 1D brief has no ORDER mark on a record, so a moved sentence can only be CLAIM or WORDING; the two testers resolve this differently (A quotes the file-10 sentence from its other place).
3. **Record order.** B's D71 and D72 (Part 0) come after D70 (Part XVI).
4. **The Derivation 3 title.** Neither tester gives the title change (C75) a record of its own; both state it only in the PART line of their Derivation 3 claim record. Neither 2D has an item for it.
5. **Cross-reference sections.** Both testers report WRONG: 0 with different CHECKED counts (169, 178) and no list of what was checked. Pointer problems both testers noticed (XR7, NEW-XR1; XR3 for B) sit under "Noticed", not under "Cross-references".
6. **Atria's "IN THE OTHER LIST: ABSENT (…)".** On AUDIT D6, D10, D13 and D20, Atria writes ABSENT and then names the other list's WORDING record for the same place. The brief asks for "the other list's record number for the same place, or the word ABSENT". Atria's ABSENT reads as "no CLAIM record there".
7. **Atria's cross-reference line.** "COUNT: 0" is followed by prose, not the bullet form, and names "(Parts XI, XIV)" as correct, against Mimo (CONFIRMED wrong), Claude-pre (SLIP) and B's Noticed item. Its "(Derivation 3)" and "the Part XV pointers" do not say which occurrences (L197, L225, L534; L19, L49, L63, L337, L528).
8. **Mimo's form.** Top-level headings are "# Part 1", "# Part 2" (the brief uses "##"); the sections the plan names keep the brief's exact headings ("## Differences in claim that both lists missed", "## Surviving differences in claim", "## Cross-references"). "IN THE OTHER LIST" gives bare numbers ("D1") without AUDIT or SECOND.
9. **Mimo's surviving list.** One item covers Derivation 3's claim, proof and consequence together (six records). NEW1 appears as "(no record on either list)". So Mimo's 54 items do not map one to one onto records.
10. **Mimo's NEW1.** Its A-quote is file 10's Part 0 attack (B) (L70), while file 10's Part XV (L535) carries B's words exactly, as Mimo says. It is "missed" only in that no list paired L530 s1 with L70 s1; both lists recorded L530 s2 (A D61, B D15, WORDING).
11. **Mimo's cross-reference NEW-XR1** is a pointer identical in both files, so it is not a difference between them. Mimo's form carries no field for whether a wrong pointer changes a claim.
12. **Paraphrase in quotation marks.** Mimo SECOND D13 quotes B as ""fallible but checkable claim""; file 11 L55 reads "fallible but checkable in principle". Atria's surviving item 2 lists "aesthetics, probability, truth, merit, worth and ranking", splitting "probability of truth". Mimo AUDIT D4 says A triggers \(\mathcal N\) "only when a question invokes a normative relation of the aesthetic kind"; file 10 L519 says "when a question invokes one".
13. **Hedged CLAIM marks.** A marks D34 (C44) and D52 (C61) CLAIM while writing "the mark could be WORDING" and "this may be WORDING", as the brief directs for close calls. B marks D1, D13, D30, D54 and D70 CLAIM as close calls.
14. **The revision note.** It is absent from the 1D and 2D briefs checked, so C1, XR1 and XR2 have no reader but Claude-pre. The B and Mimo briefs were not opened.
