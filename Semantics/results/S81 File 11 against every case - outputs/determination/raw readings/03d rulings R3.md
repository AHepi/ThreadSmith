# S81 step 4, rulings, range R3 (M42–M59), and the cross-references

**What this is.** Claude's step-4 rulings on the eighteen master places of range R3 (`master R3.md`), from Part XI (Worth) to Part XVI. It also rules every cross-reference in `master XR.md` for test (d). Each place was read against file 10 and file 11 at the lines given, with its paragraph. Each whole file was searched for related qualifications (lesson 50). Written by Claude, 23 September 2026.

**Opened.**
- File 10 and file 11, in full. A `grep` of file 11 for "probability", "bell", "tide", "worth", "realiz" and "declared input", and of file 10 for "worth" and "merit".
- `master R3.md` and `master XR.md` in full. From `alignment.md`: sections 0, 1.3, 1.4, 3, 4, 5 and 6.
- `rulings R2.md`: its head, its M22–M26 and M38 records and its closing sections. I read these for the format and for consistency on O35. My rulings were made from the texts.
- Claude's pre-reading (determination/02): sections 0 to 2; section 3 on C1, C7 and C60–C81; sections 4, 5 and 6.
- The raw readings. 02a: Parts XI to XVI of step 1, step 2 and step 3. 02b: D22–D24, D56–D67, the step 1 counts and step 2.
- Claude's case rulings (determination/01): the header, the reconciled table, every case record, the baseline comparison and the SILENT table.
- The case book, in full.
- The 1D returns. A: records D50–D68 and every closing section. B: D14–D15, D51–D72 and every closing section.
- The 2D returns. Atria: its format head (lines 1–20), AUDIT D50–D68, SECOND D50–D70, Part 2, the missed differences, the cross-references and the surviving differences. Mimo: AUDIT D51–D70, SECOND D50–D68, and the same closing sections.
- Brief 1D A, lines 1–56, and brief 2D Atria, lines 1–62. A `grep -c` on both briefs for "Revision 1", "O48", "S75" and "bell does not explain the tide".
- The S81 plan. The second version, lines 100–170. The third version, its head and sections e to l.

**Seen, names only.** An `ls` of `step4/`, `authority/`, `tests/` (S81 files), `outputs/`, `determination/` and `raw readings/`. A `wc` listing of the returns folder, which showed the names of receipt, reasoning, request and pass-2 files. A harness reminder showed the parent session's task titles.

**Not opened.** Any 1C, 1K, 2a or 2b return; any reasoning file; any receipt; the effort-controls folder; the sample JSONs; `stage1/`; and any table.

**The rule applied** (as in R2).
- Step 4 rules each place CLAIM or WORDING. ORDER is Claude-pre's label for the same claim moved or copied, and P3 counts ORDER with WORDING.
- The CLAIM test is the brief's: a reader can conclude from one text something the other leaves unconcluded. That includes B adding "an input the theory takes from outside itself".
- Claude-pre's policy on restatements is kept:
  - a sentence that restates what file 10 already states, at the same or wider scope, is ORDER;
  - a sentence that states what file 10 leaves to inference is CLAIM, even when it is derivable.
- Grades are for information only: *changed*, *new*, *application*.

**Harm.**
- A CLAIM place is harmful when it moves a case's verdict away from the thoughtful person.
- The evidence here is Claude's case rulings (01), which were written before any return was opened. Step 3 fixes the marks that count.
- Under the plan, the file-10 mark is S75's baseline unless both 1K returns agree on a different mark and Claude confirms it. The baseline is:
  - DISAGREE on O48;
  - SILENT on O1, O12, O20, O21, O27, O35, O40 and O50;
  - AGREE on the rest.
- Every harm verdict below stands on 01's marks. The rows where the baseline, or a live contrary reading, could change the verdict are flagged for step 3.

---

## Table

"01 marks" are Claude's case rulings, file 10 → file 11. "Pre" is Claude-pre.

| M | C | f10 / f11 | ruling | declared by note? | cases touched (01 marks) | harmful? | differs from pre? |
|---|---|---|---|---|---|---|---|
| M42 | C60 | L458 / L447 heading, s1–s2 (s3) | CLAIM (changed; s1 is an application; s3 alone is WORDING) | no | O12 SILENT→SILENT; O38 (weak) AGREE→AGREE; O35 (weak) AGREE→SILENT, but 01 traces that change to C56 and C66 | no case shows it harmful | no |
| M43 | C61 | L458, last two sentences / L447, last clause | CLAIM (application; close call) | no | none | no case touches it | no |
| M44 | C62 | absent (L523: indices only) / L465 | CLAIM (new) | no | O41 SPLIT→AGREE, toward; O42, O30, O51 AGREE→AGREE, passage CHANGED; O17 (weak) AGREE→AGREE | no case shows it harmful on 01; O17 and O30 flagged | no |
| M45 | C63 | L476 / L467, last sentence | CLAIM (new) | no | O49, O17 AGREE→AGREE, passage CHANGED | no case shows it harmful | no |
| M46 | C64 | L482 / L473, last sentence | CLAIM (new definition; Derivation 3 cluster) | no | O48 DISAGREE→AGREE, toward | no case shows it harmful; its one case moves toward | no |
| M47 | C65 | L519 / L510 | CLAIM (changed) | no | O12 SILENT→SILENT | no case shows it harmful | no |
| M48 | C66 | absent (L521–523) / L514 | **CLAIM (new). P3 named place (iii)** | no | **O35 AGREE→SILENT, away**; O1, O50 SILENT→SILENT; O41 SPLIT→AGREE, toward; O5, O8, O17, O21, O27, O30, O38, O40, O42, O51 AGREE→AGREE; weak: O3, O14, O31 AGREE→AGREE, O18 SPLIT→AGREE | **yes on 01 (O35)**, jointly with M38; pending step 3's file-10 mark (baseline SILENT) | no |
| M49 | C67 | L525 / L518, last sentence | CLAIM (new) | no | O37 SPLIT→AGREE, toward; O49, O17 AGREE→AGREE | no case shows it harmful | no |
| M50 | C70 | L68 (with L284, L533) / L528 s3 | CLAIM (changed) | no | O2, O33 AGREE→AGREE | no case shows it harmful | no |
| M51 | C71 | L70, L535 / L530 | ORDER | n/a | none | n/a | no (Mimo's CLAIM not followed) |
| M52 | C73 | L74, L539, L541 / L534 | CLAIM (changed), limb 1; limbs 2–3 ORDER. P3 named place (i) | yes | O48 DISAGREE→AGREE, toward; O24 AGREE→AGREE | no case shows it harmful | no |
| M53 | C75 | L567 / L560 | CLAIM (changed). P3 named place (i) | yes | O48, toward | no case shows it harmful | no |
| M54 | C76 | L569 / L562 | CLAIM (changed). P3 named place (i) | yes | O48, toward; O24 AGREE→AGREE | no case shows it harmful | no |
| M55 | C77 | L571 / L564 | CLAIM (changed). P3 named place (i) | yes | O48, toward | no case shows it harmful | no |
| M56 | C78 | L573 / L566 | CLAIM (changed). P3 named place (i) | yes | O48, toward; O24 AGREE→AGREE; O3 (weak) AGREE→AGREE | no case shows it harmful | no |
| M57 | C79 | L589 / L582, last sentence | CLAIM (application) | no | O12 SILENT→SILENT | no case shows it harmful | no |
| M58 | C80 | L593 / L586 | CLAIM (changed) | no | only through M48 | not on its own; M48's O35 flag carries over | no |
| M59 | C81 | L623 / L616 | CLAIM (new interpretive clause; Derivation 3 cluster) | no | none | no case touches it | no |

**Counts in R3.** CLAIM 17, WORDING 0, ORDER 1 (M51).
- Declared by the note: 5 of the 17 (M52–M56). The 12 undeclared CLAIM places are M42–M50, M57, M58 and M59.
- No ruling and no grade differs from Claude-pre.
- **P3 named place (iii), Declared inputs (M48), is ruled CLAIM, so P3 fails at (iii).** R2 found it failing at (ii). The 12 undeclared CLAIM places here would fail P3's "Every other place is WORDING or ORDER" without either named place.
- P3 named place (i) is CLAIM at M52–M56, as P3 expects.
- Readers against Claude-pre in this range, and whom I follow:
  - M43: Atria says WORDING. I follow A, B, Mimo and Claude-pre (CLAIM).
  - M51: Mimo says CLAIM (its NEW1). I follow Claude-pre (ORDER), and A and B (WORDING on s2).
  - M42 s3: B says WORDING on that sentence alone. I agree, and it does not touch the place's ruling.
  - M53: no reader gives the title a record of its own. That is not a contrary mark.

---

## Details per place

### M42. C60, "Worth, and the normative relation". CLAIM (changed).

- File 10, L458. Heading: "**Artistic effect, purpose, and aesthetic reason.**" The text includes "a normative relation \(\mathcal N\subseteq A\times K\times\mathcal Rsn\times\mathcal V_A\) declared as a substantive input when aesthetic value is claimed. None is defined as another. The semantics does not derive \(\mathcal N\)."
- File 11, L447. Heading: "**Worth, and the normative relation.**"
  - s1: "Repairing an obligation establishes that it was repaired; it establishes nothing about whether the obligation, or the question that led to it, was worth having."
  - s2: "Where a claim invokes worth, the semantics takes a **normative relation** \(\mathcal N\) as a declared input and marks the place (Part XIV)."
  - s3: "The aesthetic case is one such invocation: …"
- **Ruling: CLAIM (changed).**
  - **s2 widens the place where \(\mathcal N\) is taken,** from a claim of aesthetic value to any claim of worth.
    - In file 10, \(\mathcal N\)'s only typed form is aesthetic (\(\mathcal V_A\), L458).
    - File 10 lists a merit function among the things the semantics does not supply, and it "marks those places as empty" (L25).
    - File 10's Part XIV takes \(\mathcal N\) "when a question invokes one" (L519). It never says that a question of worth is such a question.
    - So a reader of file 11 concludes that a claim that a question was worth asking takes \(\mathcal N\) as a declared input. A reader of file 10 concludes only that the place is empty. That is B's TEST (D52).
  - **s1 is new, grade application.** File 10 gives it by inference, since (P) has no worth conjunct and "does not rank alternatives" (L444), and no merit function is supplied (L25). But file 10 does not state it.
  - **s3 on its own is WORDING.** The three carriers and the condition for \(\mathcal N\) are word for word the same. "One such invocation" belongs to the widening in s2. B's D53 says this, and I agree. A's D51 joins s2 and s3 in one CLAIM record, and its WHY is about s2.
- **Whole-file search.**
  - File 10: L25, L53 (aesthetics sits in Part XI), L444, L519, and L597 ("when a question requires it, a theory of reasons").
  - File 11 carries the same widening at L27 (worth added to the list), L33, L433 s2, L510 and L582. Two strains remain:
    - L447 calls \(\mathcal N\) "a declared input", but L514's "Declared inputs" opens "Besides the two primitives", which excludes \(\mathcal N\) (XR5).
    - L447 speaks of a *claim* that invokes worth, and L510 of a *question*. I read them as the same scope.
- **Readers.** A (D50, D51), B (D51, D52), Atria, Mimo and Claude-pre all say CLAIM. B's D53 marks s3 alone WORDING, which is consistent.
- (i) Not declared by the note.
- (ii) Cases (01):
  - O12: SILENT→SILENT, on the same point, "its merit is real".
  - O38 (weak): AGREE→AGREE. s1 supports the verdict's separation of "mattered" from "held".
  - O35 (weak): 01 has AGREE→SILENT, but traces the change to L433 and L514 (M38, M48), not to L447. Suppose "held in every way that mattered" were read as a worth claim. File 10's L25 would then leave the same place empty, so this place would give SILENT on that phrase under both files, and no change.
- (iii) No case shows it harmful.

### M43. C61, "no aesthetics follows from achieving a stated effect". CLAIM (application), a close call.

- File 10, L458: \(\mathcal N\) is "declared as a substantive input when aesthetic value is claimed. None is defined as another. The semantics does not derive \(\mathcal N\)."
- File 11, L447, last clause: "The semantics does not derive \(\mathcal N\), and no aesthetics follows from achieving a stated effect."
- **Ruling: CLAIM, grade application.**
  - File 10's own paragraph entails the clause. A claim of aesthetic value needs \(\mathcal N\) as a declared input, and the semantics does not derive \(\mathcal N\). So achievement, (AR), yields no aesthetic verdict by itself.
  - "None is defined as another" alone would give less. Not being defined as another is not the same as not following from another. That is Claude-pre's point. The "declared … when aesthetic value is claimed" clause closes the gap.
  - File 10 does not state the conclusion. Under the policy kept from Claude-pre, this is CLAIM, grade application. R2 gives the same treatment to M23, M25, M33, M34 and M41.
  - There is a stronger reading: that no declared \(\mathcal N\) may count achieving an effect as an aesthetic reason. It is not the natural one, because "follows" speaks of what the semantics derives.
- **Why I follow A, B, Mimo and Claude-pre over Atria.**
  - Atria's reason is right about derivability. Its words: "drawable from A's "None is defined as another" and "The semantics does not derive N"".
  - But derivability is exactly the *application* grade. Under the policy, derivability does not make a place WORDING.
  - Atria's reading is why this is a close call. A wrote "this may be WORDING", and B called it "a close call".
- (i) Not declared.
- (ii) No case.
- (iii) No case touches it. The ruling bears on no verdict. It bears only on P3's count, and P3 already fails at (ii) and (iii).

### M44. C62, System boundary and continuity. CLAIM (new).

- **File 10:** no such paragraph. Boundary \(\beta\) and continuity \(\Omega\) are "declared indices" (L523). L476 has "under the same continuity and resource contract". Build needs a subhistory "owned by \(s\)" (L414). No sentence says what a boundary or a continuity is.
- **File 11, L465:** "A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change). A replaced part that preserves the declared continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it; a process run outside it is not the system's however close it sits. Both are declared before the attribution, not chosen after it."
- **Ruling: CLAIM (new).** The paragraph makes four claims file 10 lacks:
  1. definitions of the boundary and of continuity;
  2. a replaced part that preserves the declared continuity leaves the same system;
  3. a process inside the boundary is the system's whoever wrote it, and one outside is not, however close;
  4. both are declared before the attribution, not chosen after it.
- **Claim 4 goes beyond file 10.**
  - File 10 allows any recorded change of an index, as a new claim at a new index: L378, L456, and L605 ("Goalpost-moving is the act of changing the index without recording the change").
  - File 11 forbids choosing the boundary after the attribution.
  - A's TEST: "A boundary chosen after seeing which choice yields the capability: B rejects the attribution; A does not."
- **Whole-file search.**
  - File 11 L419 (Ownership) applies the same rules in Part X and points here.
  - L514 names boundary and continuity as declared inputs. L516 and L33 still call them declared indices; see M48.
  - L365, "A new index is a new claim", is kept. A boundary declared later starts a new attribution, so claim 4 and L365 are compatible.
- **Readers.** All CLAIM.
- (i) Not declared.
- (ii) Cases (01):
  - O41: SPLIT→AGREE, toward the thoughtful person, a theory change traced to L419 and L465.
  - O42: AGREE→AGREE, passage CHANGED; the continuity is stated.
  - O51: AGREE→AGREE, passage CHANGED.
  - O30: AGREE→AGREE, passage CHANGED ("a process run inside the boundary is the system's whoever wrote it").
  - O17 (weak): AGREE→AGREE.
- (iii) **No case shows it harmful on 01. Flag O30 and O17.**
  - Neither case states a boundary.
  - With L514, a strict reader of file 11 could leave "was the robot's work today" (O30) or "the routine running inside the robot" (O17) unsettled for want of a declared boundary. 01 reads "inside the robot" as enough.
  - A file-11 SILENT on either, where file 10 gives AGREE, would be a change away from the thoughtful person, traced to this place together with M48.

### M45. C63, ownership grounded in the boundary, never in the capability. CLAIM (new).

- File 10, L476, ends: "A theorist's description of a protocol is not the system's possession of it."
- File 11, L467, adds: "Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed: "owned because it can, and can because owned" grounds neither."
- **Ruling: CLAIM (new).**
  - File 10 never says what grounds ownership. "Owned" is used without definition at L414, L476, L488 and L493.
  - File 10 has no rule against grounding ownership and capability in each other. The nearest sentence is L344, "its support is circular though its content might be true", which is about one identification.
- **Whole-file search.** File 11 carries the same rule at L419 ("Ownership is not defined by the capability it is meant to ground (Part XII)") and L518. They are consistent.
- **Readers.** All CLAIM.
- (i) Not declared.
- (ii) Cases: O49 and O17, both AGREE→AGREE, passage CHANGED (additive).
- (iii) No case shows it harmful.

### M46. C64, the population defined. CLAIM (new definition; Derivation 3 cluster).

- File 10, L482: "A selected provenance \(\operatorname{Sel}(t;\mathcal T,\mu,H)\) is a claim about a physical history: a population of realized transports, a physically admitted variation operator, and a survival condition enacted by the environment. It is fallible and checkable as any physical claim is."
- File 11, L473, adds: "The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it."
- **Ruling: CLAIM (new definition).**
  - File 10 names the population twice: "a population \(\mathcal T\) of candidate transports" (L210) and "a population of realized transports" (L482). It never says what fixes membership.
  - File 11 fixes it by "the physics and the stated construction". It also excludes any transport that would need a part no member has.
  - The second clause is close to what "realized transports" already gives: a transport that needs a part no realized member has is not realized.
  - But file 10's Derivation 3 never required the alternative to be in the population. Its claim reads "there exists a transport \(t'\), also surviving on \(H\)" (L569). So under file 10 the clause had no bearing on underdetermination. Under file 11, joined with L562 ("a member of \(\mathcal T\)"), it decides it.
- **Whole-file search: a tension inside file 11.**
  - L473 keeps its first sentence's "a population of realized transports" and adds "the set of transports the physics and the stated construction admit". Realized and admitted are not the same set.
  - L562 then says "admitted, realizable, a member of \(\mathcal T\)".
  - That is three words for membership in three sentences. On O48 all three give the same answer, because every device in the stated population lacks the wire. I record it as an erratum candidate.
- **Readers.** All CLAIM.
- (i) Not declared. It is not among the note's sentences. Claude-pre: "a new definition, not named in the revision note."
- (ii) O48: DISAGREE→AGREE, toward the thoughtful person, a theory change. 01 cites L562 and L473.
- (iii) No case shows it harmful. Its one case moves toward the thoughtful person.
  - For P1 (step 3): 01's O48 rests on L562, which the note declares, and on L473, which it does not.
  - L562 alone gives the verdict once the case's own "stated population" is read in. So P1's "rests on the qualified claim of Derivation 3" holds on 01's reading.

### M47. C65, Primitive 2. CLAIM (changed).

- File 10, L519: "2. The **normative relation** \(\mathcal N\), when a question invokes one."
- File 11, L510: "2. The **normative relation** \(\mathcal N\), when a question invokes worth. It is taken as an input and never derived; the aesthetic relation of Part XI is one instance."
- **Ruling: CLAIM (changed).**
  - The trigger changes. File 10 says "when a question invokes one", that is, a normative relation. File 11 says "when a question invokes worth".
  - The relation changes too. In file 10, \(\mathcal N\) is the aesthetic relation typed at L458. In file 11 it covers worth in general, and the aesthetic relation is "one instance".
  - The scope moves both ways:
    - Worth questions outside aesthetics now take \(\mathcal N\), a widening against L458.
    - A normative question that is not about worth is the other direction. An example is "whether it should" at L345 ("Whether the rule governs a practice, and whether it should, are separate questions with separate contracts"; the same words at f10 L360). It takes \(\mathcal N\) under file 10's wording, but under file 11 only if "should" is read as worth.
    - Either way the place is CLAIM.
  - "It is taken as an input and never derived" restates f10 L458 ("The semantics does not derive \(\mathcal N\)") and f10 L516–519 (\(\mathcal N\) is a primitive). That part is ORDER inside the place.
- **Whole-file search.** File 11 L33 copies the worth trigger (M5, range R1), and L447 carries it (M42). They are consistent apart from XR5.
- **Readers.** All CLAIM.
- (i) Not declared.
- (ii) O12: SILENT→SILENT.
- (iii) No case shows it harmful.

### M48. C66, Declared inputs, P3 named place (iii). CLAIM (new).

- **File 10:** nothing between L521 ("Everything else is derived. …") and L523 ("**Indices, not primitives.** Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices. Every claim is relative to them; none is a predicate that could be true or false.").
- **File 11, L514:** "**Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII). A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."
- **Ruling: CLAIM (new).** P3's named place (iii) is CLAIM, so P3 fails here as well as at (ii) (M38, range R2).
- **Three things are new against file 10.**
  1. **A category.** File 10 has primitives, indices and "Everything else is derived" (L521). File 11 adds stated inputs "that the semantics records and does not supply".
  2. **New inputs.** Its members include inputs file 10 does not have: the occasions each obligation covers (new at L433, M38) and what makes a restriction appropriate (new at L161, M17). This is the brief's own case of CLAIM: B adds "an input the theory takes from outside itself".
  3. **A verdict rule:** "where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted". File 10 has instances of the thought, but not the rule:
     - "missing evidence stays missing" (L406), for receipts;
     - ""Set \(b_B=0\) because it gives the mass I favour" is not an inference from the readings" (L344), for one identification;
     - "Every claim is relative to them" (L523), for indices only.
     None of these makes a verdict unsettled for want of an input.
- **What would make it WORDING.** Every item would have to be an input already in file 10, and the rule would have to be stated there. Only the boundary, continuity and scope items meet the first condition, as indices (L523). Nothing meets the second. No reader marks it WORDING.
- **Whole-file search: tensions inside file 11.** All were recorded by Claude-pre or the testers, and I confirm each:
  - L33 and L512 say "Everything else is derived" and do not mention the category (XR10; A's and B's Noticed items).
  - L516 and L33 keep boundary, continuity and the contract as declared indices, while L514 also makes them declared inputs (A's Noticed item).
  - "Besides the two primitives" excludes \(\mathcal N\), which L27 and L447 call a declared input (XR3, XR5).
    - So the unsettled rule does not formally cover \(\mathcal N\).
    - L447's "marks the place" still leaves a worth verdict without \(\mathcal N\) unsupported (O12).
  - L586 widens Derivation 6 to declared inputs (M58), but the order at L518 lists none (XR6).
  - None of these changes what L514 claims. In each, another sentence of file 11 says less than L514.
- **Readers.** A (D57), B (D59), Atria, Mimo and Claude-pre say CLAIM. No reader says WORDING.
- (i) Not declared. The note says "Nothing else changes in what is claimed."
- (ii) Cases (01), by the input each turns on:
  - **Occasions.**
    - **O35: AGREE→SILENT, verdict CHANGED, away from the thoughtful person, a theory change.** 01 traces it to L433 and L514 together.
    - O38: AGREE→AGREE, passage CHANGED. The occasions are stated.
  - **Appropriateness of a restriction.**
    - O1: SILENT→SILENT, passage CHANGED (additive). File 11's SILENT rests on L161 and L514.
    - O5: AGREE→AGREE. The case supplies the ground.
    - O8: AGREE→AGREE. The scope is the question from the start.
  - **Boundary and continuity.**
    - O41: SPLIT→AGREE, toward the thoughtful person.
    - O42 and O51: AGREE→AGREE, passage CHANGED.
    - O17, O21, O27, O30 and O40: AGREE→AGREE.
    - O50: SILENT→SILENT. Its missing input is a weighting of credit, which L514 does not name (01's SILENT table).
    - Weak: O3, O14 and O31 AGREE→AGREE; O18 SPLIT→AGREE.
  - **\(\mathcal N\)**, which L514 does not name: O12 SILENT→SILENT.
- (iii) **Harmful on 01: O35.**
  - My reading agrees with 01 and with R2's M38.
    - *File 11.* The protected tap's occasions are not stated: every moment of the work, or the moments someone draws water. L514 leaves the verdict unsettled, so the mark is SILENT.
    - *File 10.* (P) checks \(r\) at \(\xi\) and \(\xi'\). The tap "then runs as before", so \(r(\xi')\) holds, and the interruption is on the record, as L444 asks. On the endpoint reading the mark is AGREE.
  - The harm is joint. M38 makes the occasions part of the protected condition. This place makes their absence an unsettled verdict.
  - **Flag for step 3, the decisive row.**
    - The file-10 mark that counts is S75's baseline, SILENT, unless both 1K returns agree on AGREE and Claude confirms it.
    - If the file-10 mark is AGREE: O35 is a theory change away from the thoughtful person. Tests (b) and (c) then fail on O35, and the standing rule's saving clause ("an undeclared CLAIM that no case shows harmful") covers neither M48 nor M38.
    - If the baseline SILENT stands: O35 is SILENT→SILENT on the same point, the reach of the protected condition, and no case shows M48 harmful.
  - **Also for step 3.** Look for any file-11 reading of SILENT where file 10 gives AGREE, for want of either input:
    - a declared boundary: O17, O21, O27, O30, O40; weakly O3, O14, O18, O31;
    - a ground of appropriateness: O5, O8.
    Each would be a change away from the thoughtful person traced to this place. On 01 none occurs.

### M49. C67, the dependence order is well founded. CLAIM (new).

- File 10, L525, the dependence order, ends: "Nothing depends on a predicate meaning "really explains," "is a cause," or "is knowledge.""
- File 11, L518, adds: "The order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply it counts only when the account uses it."
- **Ruling: CLAIM (new).**
  - Said of the listed definitions, "The order is well founded" is already shown by file 10's list, which starts from "(O) and (Q) depend on nothing". That part is ORDER inside the place.
  - The rest is new, in two ways:
    - it applies well-foundedness to the justification of instances: a representation justified only by its own construction, and ownership and capability justified by each other;
    - it adds a rule for proofs the account does not use: "a separate proof that would supply it counts only when the account uses it".
  - File 10 has no rule on support the account does not cite. Its receipts (L406) and standing (K2, L399) set no condition of citation. That is reading B of O37 in 01.
- **Whole-file search.** File 11 L467 and L419 carry the ownership half, consistently. No tension found.
- **Readers.** All CLAIM.
- (i) Not declared.
- (ii) Cases (01):
  - O37: SPLIT→AGREE, toward the thoughtful person, a theory change. The baseline is AGREE, so step 3 may find no change.
  - O49 and O17: AGREE→AGREE, passage CHANGED.
- (iii) No case shows it harmful. File 11 states O37's verdict nearly word for word, so this place cannot move O37 away.

### M50. C70, (A) Sufficiency: the encoding table "fails none and is an account". CLAIM (changed).

- File 10:
  - L68: "The classic attempts — lookup tables, reversed calculations, conclusion-as-premise — all fail one of the four; a new one must fail none."
  - L284: "A table that genuinely encodes an organization's response to every admitted change is not a table in that sense and is not excluded."
  - L533: "A candidate meeting (E) on a physically admitted contract with a non-declared transport, which plainly provides no account. This refutes sufficiency."
- File 11, L528 s3: "A table that encodes the response to every admitted change fails none and is an account, so it is not a counterexample; a new attempt must fail none and still explain nothing."
- **Ruling: CLAIM (changed), on the first clause.**
  - File 10 is split on such a table:
    - L68 says lookup tables fail one of the four;
    - L284 says the encoding table is not excluded. With L533 that leaves it open as a possible counterexample to sufficiency: it meets (E), and whether it "plainly provides no account" is left open.
  - File 11 says the encoding table fails none, is an account, and so is not a counterexample.
    - That closes, by assertion, a question file 10 leaves open.
    - It contradicts L68 for tables of this kind.
  - The second clause restates f10 L68 s1 ("… and that plainly explains nothing") and s3 ("a new one must fail none"). That is WORDING inside the place.
- **Whole-file search.**
  - File 11 L271 (M22, range R2) carries the same "is an account", so file 11 is consistent with itself here.
  - A's Noticed item on L271: "Being an account requires (F2), (A), non-circular dependence and non-vacuity as well, not (F1) alone." L528's "fails none" asserts all four conditions outright, so L528 states in full what L271 argues from (F1) alone.
- **Readers.** All CLAIM. A's and B's Noticed items record file 10's own tension between L68 and L284.
- (i) Not declared.
- (ii) Cases:
  - O2: AGREE→AGREE. Under both files the almanac is a table of observed answers and fails (F1).
  - O33: AGREE→AGREE. Its table is a form of the question.
- (iii) No case shows it harmful.

### M51. C71, (B) Necessity. ORDER. Mimo's NEW1 is not followed.

- File 10:
  - L70: "**(B) Necessity.** Produce a genuine explanation whose organization cannot be captured by *any* transport satisfying component fidelity under *any* physically admitted contract. Explanations that work by showing a supposed structure is absent are the hard case; Part VII gives the semantics' treatment, and it may be inadequate."
  - L535: "**An explanation without a faithful transport.** A genuine explanation whose organization no transport can preserve under any physically admitted contract. This refutes necessity. Eliminative explanation (Part VII) is the exposed case."
- File 11, L530: "**(B) Necessity.** A genuine explanation whose organization no transport can preserve under any physically admitted contract. Eliminative explanation (Part VII) is the exposed case."
- **Ruling: ORDER.** File 11's L530 is f10 L535 with two changes:
  - "This refutes necessity" is carried by the heading "(B) Necessity";
  - L535's heading "An explanation without a faithful transport" is dropped. L63 ("(B) their necessity", said of the four conditions of Account) still tells the reader what "preserve" means.
- **Why I do not follow Mimo's NEW1.**
  - Mimo is right that f10 L70 and f10 L535 state two different refuting conditions:
    - L70: no transport satisfying component fidelity, (F1), can capture the organization;
    - L535: no transport can preserve it, which by L535's heading means no faithful transport, (F1) and (F2).
  - Every faithful transport satisfies (F1). So L70's condition implies L535's, and every explanation L70 counts as a refuter, L535 counts too.
  - Mimo's TEST is an explanation captured by some (F1)-only transport and preserved by no faithful one. File 10's own L535 already counts it as refuting necessity, as Mimo itself says: "even though A's Part XV uses B's wording". So a reader of the whole of file 10 can draw the conclusion Mimo gives to file 11 alone.
  - What file 11 drops is L70's narrower condition, every refuter of which file 11 still counts. With it goes file 10's disagreement between its Part 0 and its Part XV.
  - The only thing lost is an exclusive reading of L70, and file 10 itself contradicts that reading at L535.
  - I follow Claude-pre (ORDER), A (D61, WORDING) and B (D15, WORDING) on s2, and Atria, which reports no missed difference.
- **s2.** "Eliminative explanation (Part VII) is the exposed case." is f10 L535's last sentence.
  - File 10 L70's hedge, "it may be inadequate", is kept at f11 L337: "it is offered as adequate and is listed under attack (B) in Part XV as a place where it may not be". File 10 has the same sentence at L352.
  - WORDING, as A's D61 and B's D15 say.
- Cases: none. The place is not CLAIM, so the harm question does not apply.

### M52. C73, (D) Genesis, P3 named place (i). CLAIM (changed) in limb 1; limbs 2–3 ORDER.

- File 10:
  - L74: "Show either that a selected transport can be non-underdetermined on unseen changes (against Derivation 3), or that construction reduces to selection (against Part IV), or that the primitive layer described in Part IV is not in fact what explanation operates on."
  - L539: "A selection history \(H\subsetneq C\) whose survivor is determined on \(C\setminus H\). This refutes Derivation 3."
  - L541: "A demonstration that every construction witness can be rewritten as a selection history without loss. This collapses the two provenances and removes creativity from the semantics."
- File 11, L534: "**(D) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Derivation 3; a population with no such survivor is the theorem's own qualification, not a refutation); a demonstration that every construction witness can be rewritten as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or a showing that the primitive layer of Part IV is not what explanation operates on."
- **Ruling: CLAIM (changed), limb 1.**
  - What file 10 counts as a refutation: any selected transport that is "non-underdetermined on unseen changes" (L74), or "whose survivor is determined on \(C\setminus H\)" (L539).
  - What file 11 counts: only a transport "whose value at an unseen change is determined by its history although its population admits a differing survivor there". A population with no such survivor "is the theorem's own qualification, not a refutation".
  - Two things change:
    - a condition is added: the population admits a differing survivor;
    - the quantifier changes from all of \(C\setminus H\) to one unseen change.
  - Take L562's gloss: "underdetermined by \(H\): survival on \(H\) does not distinguish \(t\) from \(t'\) there".
    - Under that gloss, the new refuter is a transport whose value is determined by \(H\) at a point where survival on \(H\) does not determine it.
    - It can be met only if "determined by its history" means more than survival on \(H\), for example through \(\mu\). I confirm Claude-pre and raw reader 1 on this.
    - Derivation 3 then stays refutable almost only as "A mathematical error" (L538: "Derivations 1–3 under their stated assumptions").
    - The change is large, and the note declares it.
  - Limbs 2 and 3 are ORDER:
    - limb 2 is f10 L541 together with L74's "(against Part IV)";
    - limb 3 is L74's third disjunct, without "in fact".
- **Readers.** A (D60), B (D63), Atria, Mimo and Claude-pre say CLAIM. The testers' records are about limb 1.
- (i) Declared: "attack point (D), the Part XV entry". In file 11 these are one passage (XR1).
- (ii) Cases:
  - O48: DISAGREE→AGREE, toward the thoughtful person.
  - O24: AGREE→AGREE.
- (iii) No case shows it harmful.

### M53. C75, Derivation 3 title, P3 named place (i). CLAIM (changed).

- File 10, L567: "## 3. Selected transports are underdetermined on unseen changes"
- File 11, L560: "## 3. Selected transports are underdetermined on unseen changes their population leaves open"
- **Ruling: CLAIM (changed).**
  - The title states the theorem in short. From file 10's title a reader concludes that selected transports are underdetermined on unseen changes, with no condition. File 11's title restricts that to changes "their population leaves open".
  - The title moves with the claim (M54).
  - No reader gives the title a record of its own:
    - A and B state it in the PART line of their claim records;
    - Mimo's joined item names the same restriction.
  - None of them marks it WORDING, so no reader disagrees.
- (i) Declared (Derivation 3).
- (ii) O48, toward the thoughtful person.
- (iii) No case shows it harmful.

### M54. C76, Derivation 3 Claim, P3 named place (i). CLAIM (changed).

- File 10, L569: "For every \((a,b)\in C\setminus H\) there exists a transport \(t'\), also surviving on \(H\), with a different value at \((a,b)\)."
- File 11, L562: "For every \((a,b)\in C\setminus H\) at which some \(t'\in\mathcal T\), also surviving on \(H\), has a different value from \(t\), the value of \(t\) at \((a,b)\) is underdetermined by \(H\) … The presence of an unseen pair alone does not establish that such a \(t'\) exists; it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\)."
- **Ruling: CLAIM (changed).**
  - An unconditional existence claim becomes a conditional one.
  - File 11 adds a denial: "The presence of an unseen pair alone does not establish that such a \(t'\) exists".
  - It adds four conditions on the alternative: "admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\)".
  - Under the colon's gloss the conditional is close to analytic. A's Noticed item calls it "close to a tautology", and Claude-pre agrees. The theorem's content now lies in the population, which L473 defines (M46).
- **Whole-file search.** "Realizable" here sits beside "realized" (L473, first sentence) and "admit" (L473, last sentence); see M46.
- (i) Declared.
- (ii) Cases:
  - O48, toward the thoughtful person.
  - O24: AGREE→AGREE. The differing arrangement exists and its setting is reachable, so the condition is met.
- (iii) No case shows it harmful.

### M55. C77, Derivation 3 Proof, P3 named place (i). CLAIM (changed).

- **Ruling: CLAIM (changed).**
  - File 10's proof builds the alternative freely: "Alter \(L_{j}(a,b)\) … the result survives on \(H\)".
  - File 11's proof needs the alternative to be in \(\mathcal T\). It adds a branch: "Where \(\mathcal T\) contains no such transport, \(H\) is silent on the value at \((a,b)\) and the population fixes it."
- **On the note's "whose proof already assumed the qualification"** (M1, range R1):
  - A's and B's Noticed items support it on one reading, where "survives" means Sel's "a member of \(\mathcal T\) that survived" (f10 L210).
  - On the other reading, survival means meeting the survival condition, and file 10's proof needs no population.
  - Claude-pre found that both readings are open. I add nothing to that.
- (i) Declared.
- (ii) O48, toward the thoughtful person.
- (iii) No case shows it harmful.

### M56. C78, Derivation 3 Consequence, P3 named place (i). CLAIM (changed).

- **Ruling: CLAIM (changed).**
  - "Unconstrained where it was not" becomes "wherever its population admits an alternative, unconstrained where it was not".
  - The new last sentence gives up "the blanket claim that every untested value is unconstrained". It says a population restriction, a physical relation or another stated constraint may already fix an untested value.
  - A's TEST: an untested value fixed by a physical relation.
- **Whole-file search.**
  - "This is why the primitive layer is fallible" stays unqualified.
  - I agree with Claude-pre that this leaves no tension. A value the population fixes can still be wrong, as Derivation 10's occupancy predictors are (L616).
- (i) Declared.
- (ii) Cases:
  - O48, toward the thoughtful person.
  - O24: AGREE→AGREE.
  - O3 (weak): AGREE→AGREE.
- (iii) No case shows it harmful.

### M57. C79, Derivation 5: a question's being found says nothing about its worth. CLAIM (application).

- File 10, L589, ends: "… the present one does, by giving contracts provenance."
- File 11, L582, adds: "That a question was found says nothing about its worth (Part XI)."
- **Ruling: CLAIM (application).**
  - In file 10 it follows from L25: no merit function is supplied, and its place is empty.
  - In file 11 it follows from L447 s1.
  - File 10 does not state it.
- **Whole-file search.**
  - Both files keep "Finding the right question is a creative act" (f10 L589, f11 L582) and "finding the right question" (f10 L76, f11 L536).
  - "Right" is an evaluative word. Beside the new sentence, it must mean the question the episode needed, not a question worth having. That is a mild strain, not a contradiction.
- **Readers.** All CLAIM.
- (i) Not declared.
- (ii) O12: SILENT→SILENT.
  - The sentence says that finding a question establishes nothing about its worth. It does not deny the worth.
  - So it supports SILENT on "its merit is real", not DISAGREE.
- (iii) No case shows it harmful. Flag O12 for step 3 only if a file-11 reading marks it DISAGREE.

### M58. C80, Derivation 6: "together with declared indices and declared inputs". CLAIM (changed).

- File 10, L593: "Every predicate in Parts II–XIII is defined from \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with declared indices."
- File 11, L586: "… together with declared indices and declared inputs."
- **Ruling: CLAIM (changed).**
  - The base of every predicate widens: from \(\Theta\), \(\mathcal N\) and declared indices, to those and declared inputs.
  - Derivation 6's title is "There are two primitives". Its claim now allows predicates that rest on inputs the semantics does not supply.
  - B's TEST: a repair with its obligations.
- **Whole-file search.**
  - The proof (L588) is unchanged. It cites the dependence order (L518).
  - That order lists no declared input, and none of the new definitions that rest on one (XR6).
  - The claim is set by its own words. The proof has a gap.
- **Readers.** All CLAIM.
- (i) Not declared.
- (ii) Cases: only through M48.
- (iii) Not harmful on its own. The O35 flag at M48 is the category's only effect on a case.

### M59. C81, Derivation 10 gloss: "Derivation 3's qualification seen from the other side". CLAIM (new interpretive clause).

- File 10, L623: "… no member survives the extended history: the fidelity failure is structural, not parametric."
- File 11, L616: "… the fidelity failure is structural, not parametric, and this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change."
- **Ruling: CLAIM (new).** File 11 asserts a link between Derivation 10's structural failure and Derivation 3's qualification. File 10 makes no such link.
- **The link is inexact (XR7).**
  - Derivation 3's qualification is a population with no survivor of \(H\) that differs from \(t\) at the unseen pair. There the population fixes the value (L562, L564).
  - Derivation 10's case is a population none of whose members survives the extended history.
  - The two coincide only if every \(H_0\)-survivor agrees at the occlusion, and Derivation 10 does not say so.
  - Occupancy-only predictors that differ from one another at the occlusion fall under Derivation 3's main clause, and all of them still fail.
  - A, B and Mimo say the same.
- Derivation 10's conclusions do not depend on the clause: (G), (P) and (EK) at L618, and the one-kind point at L620.
- **Readers.** All CLAIM. B: "a close call, since it is interpretive".
- (i) Not declared.
- (ii) No case.
- (iii) No case touches it.

---

## Cross-references (master XR), test (d)

"Lands" means the pointer reaches a place that carries what the sentence attributes to it. A SLIP points wrong without changing what the sentence claims. A pointer is CLAIM-CHANGING when it points wrong in a way that changes what the sentence claims.

| id | f11 line | pointer | ruling | other readers |
|---|---|---|---|---|
| XR1 | L5 | "(the answer to grievance 3, attack point (D), the Part XV entry)" | SLIP | pre SLIP; testers and auditors did not see the note |
| XR2 | L5 | "the audit's case O48", "(Semantics results S75)" | SLIP, with a steering flag | pre SLIP; not seen by the others |
| XR3 | L27 | "(Parts XI, XIV)" | SLIP | pre SLIP; Mimo wrong; **Atria CORRECT, not followed**; B noticed the gap |
| XR4 | L275 | "(the bell does not explain the tide)" | SLIP, with a steering flag | pre SLIP |
| XR5 | L447 | "(Part XIV)" | SLIP | pre SLIP |
| XR6 | L588 | "By the dependence order of Part XIV" | SLIP | pre SLIP |
| XR7 | L616 | "Derivation 3's qualification seen from the other side" | SLIP | pre SLIP; Mimo wrong; A and B noticed it as inexact |
| XR8 | L528 | "(E)" beside "(E) Question-finding"; "four conditions of (E)" | CORRECT | pre and Atria CORRECT |
| XR9 | L363 | "(Derivation 8)" | CORRECT (loose) | pre and Atria CORRECT |
| XR10 | L33 | "in the order Part XIV states" | CORRECT | pre CORRECT; A and B noticed the tension with L514 |
| XR11 | L534 | "(against Derivation 3; …)" | CORRECT | pre and Atria CORRECT |
| XR12 | L63 | "stated exactly in Part XV"; "(A)–(E)" | CORRECT | pre and Atria CORRECT |
| NEW-XR1 | L620 (f10 L627, the same words) | "(Derivation 2)" | **CORRECT (loose); uncertain** | **A and B noticed it as wrong; Mimo CONFIRMED wrong; not followed.** Both raw readers of 02 said CORRECT |
| NEW-XR2 | L13 | "(Part II, Derivation 1)" | CORRECT | Atria CORRECT |
| NEW-XR3 | L17 | "(Part III, Derivation 5)" | CORRECT | Atria CORRECT |
| NEW-XR4 | L45 | "(non-vacuity, Part V)" | CORRECT | Atria CORRECT |
| NEW-XR5 | L197, L225 | "(Derivation 3)" | CORRECT | Atria CORRECT |
| NEW-XR6 | L19, L49, L337 | "Part XV lists what would count"; "Part XV names its refutation"; "attack (B) in Part XV" | CORRECT | pre (L337) and Atria CORRECT |

**Counts.** CORRECT 11, SLIP 7 (XR1–XR7), CLAIM-CHANGING 0. **Test (d) holds on these rulings.** The seven SLIPs go on the errata list for a later revision.

**XR1, L5. SLIP.** "The three sentences that restated it (the answer to grievance 3, attack point (D), the Part XV entry) change with it."
- The list follows file 10's layout, where the three were separate sentences at L38, L74 and L539.
- In file 11:
  - the answer to grievance 3 is L43, changed;
  - attack point (D) and the Part XV entry are one passage, L534, changed;
  - the Part 0 short form at L63 ("(D) the two provenances and the underdetermination of selected transports") did not change and carries no qualification.
- So the pointers name two passages of file 11, or three if L63 is counted, but L63 did not change.
- The note also leaves out L197, L225, L473 and L616 (M19, M21, M46, M59).
- What the note claims, that the restating sentences change, is true of L43 and L534. The pointer does not change that claim.

**XR2, L5. SLIP, with a steering flag.** "the audit's case O48", "(Semantics results S75)".
- Both references point outside the theory. The document has no audit, no case O48 and no S75.
- Brief 1D A and brief 2D Atria each contain "Revision 1", "O48" and "S75" zero times, so the steering did not reach those readers.
- The note's statement about Derivation 3 stands without either reference.

**XR3, L27. SLIP.** "Where a claim needs one of these, the semantics takes it as a **declared input** and marks the place (Parts XI, XIV)." The list is "an objective aesthetics, a probability of truth, a merit function, a measure of worth, or a ranking of thinkers".
- Part XI (L447) and Part XIV (L510, L514) carry aesthetics and worth, through \(\mathcal N\).
- A merit function and a ranking of thinkers are carried only if they are read as claims of worth.
- A probability of truth appears in file 11 only at L27 (checked by `grep`), so its place is marked nowhere.
- Part XIV's own terms also differ from the sentence: L514 opens "Besides the two primitives", so \(\mathcal N\) is not one of its declared inputs.
- **Why I follow Claude-pre and Mimo over Atria.** Atria calls the pointer CORRECT without naming a place that carries a probability of truth, and there is none.
- **Why SLIP and not CLAIM-CHANGING.** L27's claim is set by its own words and would be the same without the pointer. The overreach comes through L37 ("the front matter states nothing the body does not state more exactly"), which is ruled with C7 and C10 in range R1, not through the pointer.

**XR4, L275. SLIP, with a steering flag.** "(the bell does not explain the tide)".
- File 11 has no bell and no tide anywhere else (checked by `grep`). The parenthesis is case O2's content ("the harbour bell rings"; "She has explained nothing about the tide").
- It is in the file-11 text of brief 1D A (1 occurrence) and brief 2D Atria (3 occurrences, counting the lists' quotations), so it reached the readers inside the theory.
- The rule stands without it: packaging a dependence that answers another question beside a restated answer does not repair the account.
- On O2 it can only move the verdict toward the thoughtful person, and 01 has O2 AGREE→AGREE.

**XR5, L447. SLIP.** "the semantics takes a **normative relation** \(\mathcal N\) as a declared input and marks the place (Part XIV)."
- The pointer lands: Part XIV marks \(\mathcal N\)'s place at L510.
- But the place it lands on classifies \(\mathcal N\) as a primitive, and L514's "Declared inputs" excludes it ("Besides the two primitives").
- It does not change the claim. Either way \(\mathcal N\) is an input the semantics does not supply, and no worth verdict follows without it (O12 SILENT under both files).

**XR6, L588. SLIP.** "By the dependence order of Part XIV, following each definition to its base."
- Derivation 6's claim (L586) now includes declared inputs.
- The order at L518 lists none of them. It also lists none of the new definitions that rest on them: Ownership (L419), ProducedBy (L433), and System boundary and continuity (L465).
- The pointer lands on the paragraph it names, but that paragraph no longer covers the widened claim.
- This is a gap in the proof. The claim is set by its words (M58).

**XR7, L616. SLIP.** "this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change".
- The pointer lands on the right derivation, but the description of the qualification is wrong. The qualification is no *differing* survivor at an unseen pair (L562, L564); Derivation 10's case is no survivor at all of the extended history (M59).
- Mimo, A and B say the same.
- It does not change a claim. Derivation 10's conclusions do not rest on the clause.
- The clause itself is the CLAIM place M59. Its content is inexact; the pointer does not misplace it.

**XR8, L528. CORRECT.**
- "Four conditions of (E)" is Part V's own count at L233: component fidelity ((F1) and (F2)), question fidelity, non-circular dependence and non-vacuity. The formula (E) lists five conjuncts, because component fidelity is two of them.
- The tag (E), for Account at L264, sits inside Part XV item (A), while Part XV item (E) is Question-finding (L536). The labels collide, but "four conditions" settles which is meant.
- File 10's Part 0 had the same collision of labels. L337's "attack (B) in Part XV" resolves the attack labels.

**XR9, L363. CORRECT (loose).** "(Derivation 8)".
- Derivation 8 (L602) transports all data along structure-preserving bijections. An invertible recoding is such a bijection.
- The reader-convention condition in the sentence is new (M29, range R2) and is not in Derivation 8. The pointer supports the core of the sentence.

**XR10, L33. CORRECT.** "Everything else is derived, in the order Part XIV states."
- Part XIV states the order at L518, and "(Derivation 6)" lands too.
- The tension with L514 is inside file 11's claims (M48), not in the pointer.

**XR11, L534. CORRECT.** "(against Derivation 3; a population with no such survivor is the theorem's own qualification, not a refutation)". Derivation 3 (L562, L564) carries that qualification: "it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\)", and "the population fixes it".

**XR12, L63. CORRECT.** Part XV (L528–536) carries (A)–(E), each with what would refute it. The (D) short form is unqualified; that is M12 (range R1), not a fault in the pointer.

**NEW-XR1, L620 (f10 L627, the same words). CORRECT (loose); uncertain.** "On any contract containing it, the two persistence components are of one kind (Derivation 2)."
- **The objection.** A, B and Mimo say Derivation 2 is about two candidate accounts, and that the one-kindness of two components inside one organization follows from (K) and Derivation 1. The direct basis is indeed (K) with Derivation 1.
- **Why the pointer still lands.**
  - Derivation 2's claim (L554) itself concludes that "their components are pairwise of one kind on \(C\)".
  - Take the swapped assignment as a second candidate. Both candidates satisfy (F1), (F2) and (A) on a contract containing the swap.
  - Pair each candidate's components by their common anchor. Then Derivation 2 gives that persistence component 1 and persistence component 2 are of one kind.
  - L620's next sentence applies Derivation 2's Consequence almost word for word. That Consequence (L558): "A claim that two such candidates "really" differ is a claim that some admitted change separates them, and must supply it." L620: "A claim that "component 1 is *really* thing 1" is a claim that some admitted change distinguishes them".
- I follow the two raw readers of 02, who ruled it CORRECT, over A, B and Mimo. I mark the ruling uncertain.
- **In no reading is it CLAIM-CHANGING.** The sentence's claim follows from (K) and Derivation 1 either way. The pointer is word for word in file 10, so it is not a difference between the files. At worst it is an erratum both files share.

**NEW-XR2, L13. CORRECT.** "(Part II, Derivation 1)" lands on "Kinds are edit-signatures" (L113–129; (K) defines one-kindness) and on Derivation 1 with its Corollary ("The word "kind" is therefore eliminable").

**NEW-XR3, L17. CORRECT.** "(Part III, Derivation 5)" lands on "Contracts have provenance" (L155–157), which says a found question requires \(\rho_p=\text{constructed}\), and on Derivation 5 ("Question-finding is representable").

**NEW-XR4, L45. CORRECT.** "(non-vacuity, Part V)" lands on L259: "every physically admitted edit excluded from \(C\) is excluded by a stated scope, not silently."

**NEW-XR5, L197 and L225. CORRECT.**
- L197, "what \(H\) leaves open about \(t\) is what \(\mathcal T\) leaves open (Derivation 3)", matches L562 and L564.
- L225, "Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3)", matches the same lines.

**NEW-XR6, L19, L49 and L337. CORRECT.**
- L19, "Part XV lists what would count": Part XV (L526–538) lists the refutations.
  - L19's "these four" and "all four" name the conjecture's four items, while Part XV (A) names Account's four conditions.
  - That looseness is inherited word for word from f10 L17. It is not in the pointer.
- L49, "Part IV forbids the reduction and Part XV names its refutation": the targets are L203 ("Neither provenance is reducible to the other") and the second limb of L534.
- L337, "attack (B) in Part XV": L530 names eliminative explanation as "the exposed case".

---

## Tensions inside file 11 met in this range

These are erratum candidates. None changes a ruling above.
1. **Membership of the population.** L473 has "a population of realized transports" and "the set of transports the physics and the stated construction admit". L562 has "admitted, realizable, a member of \(\mathcal T\)". (M46, M54)
2. **"Everything else is derived"** at L33 and L512, against the declared inputs of L514. (M48, XR10)
3. **Boundary, continuity and the contract** are declared indices at L33 and L516, and declared inputs at L514. (M48)
4. **\(\mathcal N\)** is a "declared input" at L27 and L447, but L514 excludes it as a primitive. (M42, M48, XR3, XR5)
5. **Derivation 6.** Its claim (L586) includes declared inputs; the order its proof cites (L518) lists none. (M58, XR6)
6. **The Derivation 10 gloss** at L616 describes Derivation 3's qualification inexactly. (M59, XR7)
7. **"the right question"** (L536, L582) stands beside "says nothing about its worth" (L582). A mild strain. (M57)
8. **The labels (A)–(E)** of Part XV share letters with the tags (A), (B), (D) and (E) in the body. (XR8)

---

## Rows for step 3

1. **O35** (M48, jointly with M38; weakly M42).
   - The file-10 mark: S75's baseline SILENT, against 01's AGREE.
   - If AGREE stands, O35 is a theory change away from the thoughtful person, traced to L433 and L514. Tests (b) and (c) then fail on O35, and the saving clause for an undeclared CLAIM does not apply.
   - This is the decisive row of the range.
2. **O48** (M46, M52–M56).
   - Check what each 1C and 2b reading rests on. P1 needs the AGREE to rest on L562 or L534 (declared), not only on L473 (undeclared).
   - On 01, L562 alone suffices.
3. **O17, O30** (M44, M48), and O21, O27, O40 (M48). Also, weakly, O3, O14, O18 and O31.
   - Any file-11 reading of SILENT for want of a declared boundary, where file 10 gives AGREE, would be a change away.
4. **O5, O8** (M48). Any file-11 reading of SILENT for want of a ground of appropriateness.
5. **O12** (M42, M47, M57). Any file-11 reading of DISAGREE on "its merit is real". I would rule SILENT: file 11 says finding a question establishes nothing about its worth, which is not a denial.
6. **O37** (M49). The baseline says AGREE and 01 says SPLIT under file 10. The row moves toward the thoughtful person or does not change.
7. **O41** (M44, M48). The baseline says AGREE and 01 says SPLIT under file 10. The row moves toward the thoughtful person or does not change.
8. **O38** (M48). 01 says AGREE under file 10, where Claude-pre expected SPLIT or DISAGREE. The row moves toward the thoughtful person or does not change.
9. **O24** (M52–M56). It should stay AGREE. Check that no file-11 reading turns it SILENT through "admitted, realizable, a member of \(\mathcal T\)" (L562) or L473.
