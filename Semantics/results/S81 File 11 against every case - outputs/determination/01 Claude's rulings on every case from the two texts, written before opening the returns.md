# S81 — reconciled case rulings, file 10 against file 11, cases O1 to O52

**What this is.** Claude (the reconciler) reconciles two independent Claude readings of round S81's 52 cases. Each reader marked every case twice, once under file 10 (the frozen authority) and once under file 11 (revision 1, the candidate), and compared the two. For each case this record gives the reconciled file-10 mark, file-11 mark, verdict (SAME/CHANGED), passage (SAME/CHANGED), direction and kind. Where the readers differ, both readings are kept and a ruling is made from the texts.

**Sources.** Both readers and the reconciler worked from the texts only. They did not open any Stage 1 or Stage 2 return. The texts are: `Semantics/authority/10 Claude Fable Semantics - standalone theory.md` (file 10, 629 lines); `Semantics/authority/11 Claude Fable Semantics - standalone theory, revision 1.md` (file 11, 622 lines); `Semantics/tests/S81 Case book - the 52 cases, situations and fixed verdicts, as the tested agent sees them.md`; and, for the marks and "Same finding", the instruction sections of the two Stage 1 briefs `s81_1C_A.txt` and `s81_1K_A.txt`. The reader inputs are `reader1_O1-O26.md`, `reader1_O27-O52.md`, `reader2_O1-O26.md` and `reader2_O27-O52.md`, all in this folder.

**Date.** 23 September 2026.

**Reconciler's blindness record.**
- `ls` of `Semantics/authority/` and `Semantics/tests/` showed file *names* only. Among them were the S81 plans, the S81 case-book provenance file, the S81 Stage 1 and Stage 2 instruction files and the S76/S72 instruction files. None was opened.
- From the briefs I read lines 1 to 90 of `s81_1C_A.txt` and diffed them against lines 1 to 90 of `s81_1K_A.txt`. The instructions are identical. The two differ only from line 86 on, inside the embedded theory: 1C carries file 11 and 1K carries file 10. A heading grep of `s81_1K_A.txt` printed only its instruction and theory headings. The briefs hold no returns. Nothing else under `Semantics/results/` was listed or opened.
- This folder also holds three files that are not inputs: `diffreader1.md`, `diffreader2.md` and `wdiff.txt`. I saw their first few lines in one `head` call, a heading and a diff header. I did not otherwise read or use them.
- A harness reminder showed the calling session's task titles, for example "Finish the three pending S81 Stage 2 audit calls". It held no returns or results.
- The S81 plan's baseline paragraph was read only after steps 1 to 3 below were written (see "Baseline comparison").

**Marks** (brief, lines 7–17; first rule that fits): CASE DISPUTED, DISAGREE, SPLIT, SILENT, AGREE. "Same finding": a theory verdict that reaches the fixed finding and adds a qualification, limit or more exact wording reaches the same finding. A word the theory leaves undefined is read in its ordinary sense.

**Passage convention used for the reconciled record.**
- **SAME:** the file-11 sentence(s) the file-11 mark rests on claim nothing that file 10 does not already state or entail through its own definitions. This includes a file-11 sentence that only states outright what file 10 entails; reader 1 labels these "SAME (added, explicit)".
- **CHANGED (additive):** file 11 claims something that file 10 neither states nor entails. This includes a definition of a word file 10 leaves to ordinary sense, such as "owned", ProducedBy or continuity.
- **CHANGED (alteration):** file 11 contradicts a file-10 claim.
- Three of the four reader files use this convention. Reader 2's file for O27–O52 labels "(addition, consistent)" a case where "the new sentence states outright what file 10 already gives through the file-10 sentences cited". This label difference is the source of most passage-only disputes below. Each is ruled on the merits, and consistency with the agreed rows is noted.

**"Readers agreed?"** is "yes" only when all six fields match: file-10 mark, file-11 mark, verdict, passage label, direction and kind. Confidence is not compared.

---

## Step 1 — completeness

Each reader's two files hold every case O1–O52 exactly once, both as a `### O<n>` record and as a summary-table row. No gaps and no duplicates.

## Step 2 — quotation check

Every double-quoted span in the four reader files was checked by program against file 10, file 11 and the case book. Asterisks were stripped and "..." omissions allowed. Where a line number stands next to the quotation, the quotation was checked at that line of the file the context names.

| | reader 1 | reader 2 |
|---|---|---|
| theory quotations with an adjacent line number, found at that line | 212 | 204 |
| theory quotations without an adjacent line number, found verbatim in the file the context names | 55 | 58 |
| case-book quotations (verdict or situation), found | 38 | 39 |
| quoted spans matching no text | 9 | 4 |
| **misquotes of the theory (wrong words, or wrong line)** | **0** | **0** |

All 13 non-matching spans were checked by hand. None is a quotation of the theory. Each is one of the following:
- the reader's own phrase in quotation marks. Reader 1: "syrup strength produces sleep" (O4); "as written, a circle" and "an uncited proof is not in the candidate" (O37). Reader 2: "a series of honest new claims" (O1); "a series of honest post-failure narrowings" (O1 summary).
- a hypothetical protected condition: "the tap runs during the work" and "the tap runs at all times during the work" (reader 1, O35).
- a case-book or theory sentence quoted from mid-sentence with a lower-case first letter: "a small binding newly prepared" (reader 1, O11, file 11 L401); "both did something that would have stopped it" (reader 1, O20); "the robot compares the pressures itself" (reader 1, O30); "the module produces today's diagnosis" (reader 1, O51); "the expert framed the choice" (reader 2, O27); "work supplied from outside" (reader 2, O30, file 11 L419).
- a bracketed edit: "retain[s] the commitments in \(W\) with the named background fixed" (reader 1, O46, file 10 L304).

Citation slips, which are not misquotes:
- Reader 1, O22 writes "L163 adds: 'What is prohibited is changing \(C\) or \(\mathcal Q\) during an assessment without recording that the claim has changed.'" The quotation is exact at file 11 L163. But the sentence is not an addition: file 10 has it word for word at L176. Reader 1's PASSAGE SAME is unaffected.
- Reader 1, O14 mixes a file-11 number (L399) with file-10 numbers (L496, L510) in one PASSAGE line without prefixes. The file-10 numbers are correct.

---

## Reconciled table

| case | file-10 | file-11 | verdict | passage | direction | kind | confidence (f10 / f11) | readers agreed? |
|---|---|---|---|---|---|---|---|---|
| O1 | SILENT | SILENT | SAME | CHANGED (additive) | — | no change | medium-low | **no** — marks in both files, passage (DISPUTED-BETWEEN-READERS) |
| O2 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O3 | AGREE | AGREE | SAME | SAME | — | no change | medium-high | yes |
| O4 | AGREE | AGREE | SAME | SAME | — | no change | medium | yes |
| O5 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium | yes |
| O6 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O7 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O8 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O9 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O10 | AGREE | AGREE | SAME | SAME | — | no change | medium | yes |
| O11 | AGREE | AGREE | SAME | SAME | — | no change | medium | yes |
| O12 | SILENT | SILENT | SAME | SAME | — | no change | medium | yes |
| O13 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O14 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O15 | AGREE | AGREE | SAME | SAME | — | no change | medium-low / medium | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O16 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium / high | **no** — file-10 mark, verdict, direction, kind (DISPUTED-BETWEEN-READERS) |
| O17 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium / medium-high | yes |
| O18 | SPLIT | AGREE | CHANGED | CHANGED (additive) | toward | theory change | medium | yes |
| O19 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O20 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | low-medium / high | yes |
| O21 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | low-medium / medium | yes |
| O22 | AGREE | AGREE | SAME | SAME | — | no change | medium | yes |
| O23 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O24 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O25 | AGREE | AGREE | SAME | SAME | — | no change | medium / high | yes |
| O26 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium / high | yes |
| O27 | AGREE | AGREE | SAME | SAME | — | no change | medium-low | yes |
| O28 | AGREE | AGREE | SAME | SAME | — | no change | medium-high / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O29 | AGREE | AGREE | SAME | SAME | — | no change | medium | yes |
| O30 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium | yes |
| O31 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O32 | AGREE | AGREE | SAME | SAME | — | no change | medium | yes |
| O33 | AGREE | AGREE | SAME | SAME | — | no change | medium-high | yes |
| O34 | AGREE | AGREE | SAME | SAME | — | no change | medium-high / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O35 | AGREE | SILENT | CHANGED | CHANGED (additive) | away | theory change | low-medium / medium-high | **no** — file-10 mark, verdict, direction, kind (DISPUTED-BETWEEN-READERS) |
| O36 | AGREE | AGREE | SAME | SAME | — | no change | medium-high / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O37 | SPLIT | AGREE | CHANGED | CHANGED (additive) | toward | theory change | medium-low / high | **no** — file-10 mark SILENT vs SPLIT (DISPUTED-BETWEEN-READERS) |
| O38 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium / high | yes |
| O39 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O40 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium-low / medium-high | yes |
| O41 | SPLIT | AGREE | CHANGED | CHANGED (additive) | toward | theory change | low-medium / high | **no** — file-10 mark, verdict, direction, kind (DISPUTED-BETWEEN-READERS) |
| O42 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium-high / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O43 | AGREE | AGREE | SAME | SAME | — | no change | medium-high / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O44 | AGREE | AGREE | SAME | SAME | — | no change | medium-high / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O45 | AGREE | AGREE | SAME | SAME | — | no change | medium / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O46 | AGREE | AGREE | SAME | SAME | — | no change | medium-high / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |
| O47 | AGREE | AGREE | SAME | SAME | — | no change | high | yes |
| O48 | DISAGREE | AGREE | CHANGED | CHANGED (alteration) | toward | theory change | high | yes |
| O49 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium / high | yes |
| O50 | SILENT | SILENT | SAME | SAME | — | no change | medium-low | **no** — marks in both files, passage (DISPUTED-BETWEEN-READERS) |
| O51 | AGREE | AGREE | SAME | CHANGED (additive) | — | no change | medium / medium-high | yes |
| O52 | AGREE | AGREE | SAME | SAME | — | no change | medium-high / high | **no** — passage only (DISPUTED-BETWEEN-READERS) |

**Counts.**
- Readers agreed on 34 rows and disagreed on 18. Six of the 18 differ on a mark: O1 and O50 in both files; O16, O35 and O41 in file 10; O37 in file 10, SILENT against SPLIT. The other twelve differ on the passage label only: O15, O28, O31, O34, O36, O39, O42, O43, O44, O45, O46, O52.
- On the 18 disputed rows, the reconciler follows reader 1 on O1, O28, O34, O35, O36, O41, O43, O44, O45, O46 and O52, and reader 2 on O15, O16, O31, O37, O39, O42 and O50.
- Reconciled file 10: AGREE 45; SILENT 3 (O1, O12, O50); SPLIT 3 (O18, O37, O41); DISAGREE 1 (O48); CASE DISPUTED 0.
- Reconciled file 11: AGREE 48; SILENT 4 (O1, O12, O35, O50); SPLIT, DISAGREE and CASE DISPUTED 0.
- Verdicts CHANGED: 5. Four move toward the thoughtful person (O18, O37, O41, O48) and one moves away (O35). All five are theory changes.
- Passages: 20 CHANGED (19 additive, one alteration, O48) and 32 SAME.

---

## Case records

Line numbers are those of the files as they stand: F10 is file 10 and F11 is file 11. R1 is reader 1 and R2 is reader 2.

### O1 — The forecaster who keeps finding honest limits — DISPUTED-BETWEEN-READERS
- Fixed verdict: Bruno has no explanation of the floods. Each limit is honest taken alone, and the series as a whole is a retreat.
- **R1:** F10 SILENT, F11 SILENT, verdict SAME, passage CHANGED (additive), confidence medium. The theory reaches "no explanation" and "honest", but not the series-level judgment "retreat". File 11 declines to certify appropriateness and makes it a declared input (L161, L514).
- **R2:** F10 AGREE, F11 AGREE, verdict SAME, passage SAME, confidence medium-low. Each post-failure narrowing is a new claim that leaves the failed question unanswered, and nothing in Bruno's claim grounds his limits, which is the retreat. R2 rates its own SILENT contrary as failing "narrowly".
- **Ruling: F10 SILENT, F11 SILENT, verdict SAME, passage CHANGED (additive). Follows R1.**
  - *File 10.* It reaches the first two points:
    - F10 L23: "It does not say prediction is explanation."
    - F10 L378: "A new index is a new claim."
    - F10 L41: "A contract that quietly excludes physically possible changes to protect an account is not caught by a rule about intentions; it is caught by the requirement that the exclusion be stated, and then by any criticism that supplies the excluded change."

    Statedness is all file 10 asks of a narrowing. The only illegitimate move it names is F10 L605: "Goalpost-moving is the act of changing the index without recording the change, and it is a failure of the record, not a licensed operation of the semantics." Bruno records every change. No file-10 sentence judges a recorded series. The verdict's contrast between "honest taken alone" and "retreat as a whole" is exactly the series-level judgment the text stops short of.
  - *File 11.* F11 L161: "What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it." F11 L514: "A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."

    Bruno's claim contains no ground for appropriateness, so the input is missing and the verdict on appropriateness is unsettled. R2's step from "no ground" to "retreat" chooses the input from the verdict wanted. This is also what separates O1 from O5, where the case supplies the ground.
  - *Passage.* The file-11 SILENT rests on L161's last sentence and on L514, and file 10 has neither. So the passage is CHANGED (additive).
- Confidence: medium-low. R2's reading is close.

### O2 — The tide table with a real bell attached
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L270: "The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this." F10 L268: "The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one."
- F11 L275: "So does an account whose only substantive component restates the answer it was asked for; packaging a genuine dependence that answers a different question beside it does not repair this (the bell does not explain the tide)." F11 L257 repeats F10 L270.
- Passage SAME: L275 applies L270 to this case. Confidence: high.

### O3 — Nadia and the cards she has never seen
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L240: "A **construction response** introduces a new organization or a new transport with a construction witness." F10 L414: "\(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) holds when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers."
- F11 L401: "A first representation may be constructed from an available problem without prior observation of what it represents."
- Passage SAME: file 10's Derivation 10 (L623) already constructs components for what is not observed.
- Both readers noted a live contrary: "her own" under file 11's boundary-relative ownership, with no boundary declared. Confidence: medium-high.

### O4 — Dormitive power, with a meter
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L141: "a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;" F10 L168: "Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other."
- F11 L153: "A measure that identifies an outcome, with a reliable prediction from it, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second."
- The coarse-dependence contrary (F11 L279) is noted by both readers. Confidence: medium.

### O5 — Greta's dough
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L41: "An account is scoped to its contract and says so." F10 L272: "The contract \(C\) is a declared subset of the physically admitted edits, and every physically admitted edit excluded from \(C\) is excluded by a stated scope, not silently."
- F11 L161: "What makes a restriction appropriate to the question asked is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that certifies it." F11 L514: "A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted." The case supplies the input: her account says why cold matters.
- Confidence: medium.

### O6 — The fever and the thermometer
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L126: "A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports." F10 L168: "An identification question has a \(\mathcal Q\) that computes a fibre and a \(C\) containing edits to the observed value."
- F11 L129: "In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows."
- Confidence: high.

### O7 — Salt on the icy step
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L32: "A correlation has no component that responds to an intervention on its supposed input; a cause does." F10 L523: "Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices."
- F11 L279: "It does not reject a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question, and its strength is fixed by its contract, not by what a finer contract would add."
- Confidence: high.

### O8 — Petra's own ovens
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L41: "An account is scoped to its contract and says so." F10 L158: "\(D\) is the target. The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over; it contains the baseline \((1,b_0)\)."
- F11 L161: "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one."
- Confidence: high.

### O9 — The float that does two jobs
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L140: "a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;" F10 L144: "The semantics never asks whether a component "is" a cause. It asks what its signature is."
- F11 L129: "Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording."
- Confidence: high.

### O10 — Two thermostats
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L126: "A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly." F10 L136: "Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide."
- F11 L121: "Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract."
- Confidence: medium.

### O11 — The apprentice and the third lock
- Both readers: AGREE / AGREE, SAME, SAME. The passages are identical.
- F10 L414 (Build, as at O3). F10 L421: "\operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c." F10 L216: "Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both."
- File 11 has the same sentences at L401, L408 and L203.
- Confidence: medium.

### O12 — The rota
- Both readers: SILENT / SILENT, SAME (same point: whether the question was better and its merit real), passage SAME.
- F10 L25: "It does not supply an objective aesthetics, a probability of truth, a merit function, or a ranking of thinkers. It supplies places where such things would go if anyone had them, and marks those places as empty." F10 L444: "(P) does not rank alternatives."
- F11 L447: "Repairing an obligation establishes that it was repaired; it establishes nothing about whether the obligation, or the question that led to it, was worth having." F11 L582: "That a question was found says nothing about its worth (Part XI)."
- Declared inputs: not named in F11 L514 (see the SILENT list). Confidence: medium.

### O13 — Two plumbers
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L446: "An epistemic obligation requires a correct account, or the correction of a use through one, to be deployable." The conjuncts Account and ProducesVia of (EK) are separate (F10 L452).
- F11 L433: "A correct account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions."
- Confidence: high.

### O14 — The phrasebook
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L476: "\(\operatorname{Can}_{\Omega,\beta}(\xi,T;\chi)\) requires an owned retained realization or an owned, physically admitted, finite construction of one under the same continuity and resource contract." F10 L496: "A finite list of failures is not a barrier proof; a bypass refutes a proposed barrier."
- F11 L399: "A narrow retained use is what it is: it establishes neither the wider understanding it falls short of nor a permanent inability to reach it."
- Confidence: high.

### O15 — Sam's inherited marks — DISPUTED-BETWEEN-READERS (passage only)
- Fixed verdict: Sam's account of his own work is complete. Where the arrows came from is a hole in the history of the diagrams, and it is a hole in his account, because his cut followed them.
- Both readers: F10 AGREE, F11 AGREE, verdict SAME. Both read "complete" and "a hole in his account" as not contradictory, so the case is not CASE DISPUTED.
- **R1:** passage CHANGED (additive). L401's last clause, on how provenance divides inside received content, is new. File 10 reaches the point through receipts.
- **R2:** passage SAME. The decisive sentence, "missing evidence stays missing", is identical in both files. L363 and L401 add support.
- **Ruling: passage SAME. Follows R2.**
  - Both files' AGREE rests on sentences file 11 keeps unchanged. F10 L406: "Negation exchanges them; missing evidence stays missing." F11 L393 has the same words. The active-route definition (F10 L384, F11 L371) places the arrows on the route to the cut.
  - F11 L401 ("A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.") and F11 L363 ("A section of a carrier filled from another source keeps that other source's history, whatever it happens to match.") are new claims, but the file-11 verdict does not depend on them.
  - R1 itself says file 10 reaches the same point through receipts. Contrast O17, O20, O21 and O26, where file 10 had to lean on an undefined word and file 11's new definition carries the verdict.
- Confidence: medium-low for file 10, which turns on reading "his account" as the history of his cut; medium for file 11.

### O16 — The worn key and the diary — DISPUTED-BETWEEN-READERS
- Fixed verdict: the worn key is evidence on its own; the diary is the diagram talking about itself; one independent witness, and the diary is a second copy of the first.
- **R1:** F10 SILENT, F11 AGREE, verdict CHANGED (SILENT to AGREE), passage CHANGED (additive), toward the thoughtful person, theory change, confidence medium.
  - No file-10 sentence says that a record derived from the carrier is no independent witness.
  - The diary even meets the literal leaf definition. A contrary AGREE through derivation trees "partly holds".
- **R2:** F10 AGREE, F11 AGREE, verdict SAME, passage CHANGED (addition), no change. File-10 confidence medium.
  - F10 L342, (I4): "Repeating rows changes no kernel; an independent calibration can."
  - The diary's derivation tree bottoms out in the diagram.
- **Ruling: F10 AGREE, F11 AGREE, verdict SAME, passage CHANGED (additive), no change. Follows R2.**
  - *File 10 reaches the independence point from its own definitions.* Part VII's identification construction (F10 L342: "The fibre at \(y\) is \(Z_y=g^{-1}(y)\).") applies to dating the key, which is an identification question. By F10 L168: "An identification question has a \(\mathcal Q\) that computes a fibre and a \(C\) containing edits to the observed value."
  - A record computed wholly from the diagram is a function of a measurement already held, so adding it leaves every fibre unchanged. That is the general form of "Repeating rows changes no kernel; an independent calibration can." (F10 L342). The worn key is the independent calibration; the diary is the diagram again.
  - *The leaf definition does not pull the other way.* F10 L406: "An evidence leaf is a reference to an event with an interpreted claim. A receipt is a derivation tree over leaves." It makes the diary a leaf, but says nothing about independence, so it gives no different finding. Hence neither SPLIT nor SILENT.
  - *File 11 states the finding outright.* F11 L213: "A carrier keeps its provenance when present access to it is lost, and a later record derived from the carrier is not a second, independent witness to its history." F11 L393: "A record reconstructed from the claim it is meant to support is not a receipt for that claim." These are new text, so the passage is CHANGED (additive). Both readers agree on that.
- Confidence: medium for file 10, since applying Part VII to witnesses is a step the text does not take in words; high for file 11.

### O17 — The robot's log and the maker's manual
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L476: "A theorist's description of a protocol is not the system's possession of it." "Owned" is read in its ordinary sense.
- F11 L467: "Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed: "owned because it can, and can because owned" grounds neither." F11 L419: "Ownership is not defined by the capability it is meant to ground (Part XII)."
- Confidence: medium / medium-high.

### O18 — The one tooth
- Both readers: SPLIT / AGREE, CHANGED, CHANGED (additive), toward the thoughtful person, theory change.
- F10 SPLIT has two readings:
  - Reading A: Build is stated of the whole content, so she built the key. F10 L414: "\(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) holds when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers."
  - Reading B: only the tooth is hers. F10 L414: "A construction witness identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation. Reconstruction by a learner is construction; relay is not."
- F11 L401: "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance."
- Confidence: medium.

### O19 — The diagram in his hand
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L384: "An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components satisfy the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts."
- F11 L371: "A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result."
- Confidence: high.

### O20 — Two valves in one second
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L324: "**Redundant routes.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\},\{b\},\{a,b\}\}\): each is contributory, neither indispensable." F10 L406: "Negation exchanges them; missing evidence stays missing."
- F11 L433: "\(\operatorname{ProducedBy}\) holds when an active route (Part IX) runs from \(\Delta\) to the repair; it credits each contribution the history establishes, and where two sufficient contributions both ran, both are credited and the history supplies no division of credit that it does not contain."
- ProducedBy is undefined in file 10. Confidence: low-medium / high.

### O21 — The expert's question
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L414: "Reconstruction by a learner is construction; relay is not." New fails for a received candidate (F10 L421).
- F11 L419: "Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own today whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing."
- Confidence: low-medium / medium.
- Reconciler's note (O21, O27 and O50 together). "Mostly" is reached in O21 and O27 but not in O50. In O21 the only construction is the expert's and the robot's choice originates nothing. In O27 the answer is one content whose Origin is the robot's. So "mostly" names where the originative act lies. In O50 the inquiry is made of several contents with different originators, and "mostly" needs a weighting (see O50).

### O22 — Two knobs, one linkage
- Both readers: AGREE / AGREE, SAME, SAME. The passages are identical.
- F10 L168: "Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other." F10 L126: "The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read."
- File 11 has the same sentences at L153 and L111.
- Confidence: medium.

### O23 — "The seal was tight"
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L126: "No role assignment is supplied. A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly."
- F11 L417: "A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction."
- Confidence: high.

### O24 — The unused joint setting
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L565: "Underdetermination of an account by a contract is not a failure of the semantics to decide; it is the semantics reporting that the contract does not contain the distinction." and "A claim that two such candidates "really" differ is a claim that some admitted change separates them, and must supply it."
- File 11 has the same at L558. Derivation 3's new qualification (F11 L562) is met.
- Confidence: high.

### O25 — One second apart
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L384: "A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) and a physical interpretation supplying process occurrences, their ports, and the connections actually instantiated." The active-route sentence is as at O19.
- F11 L371: "A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result."
- Confidence: medium / high.

### O26 — Two feeds, one moment
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L384 (active route). F10 L316: "A block may be critical while no singleton in it is."
- F11 L433: "it credits each contribution the history establishes".
- Confidence: medium / high.

### O27 — The test that fitted neither
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L432: "A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response. A creative critical episode contains an instance of (G) connected to its inquiry." F10 L414 (Build, as at O3).
- The same definitions are in F11 at L421 and L401. F11 L27 adds: "It does not supply a division of credit among contributors beyond what a history establishes (Part XI)."
- "Mostly the robot's" is read as the robot's Origin of the answer (see the note at O21). Confidence: medium-low.

### O28 — The card nobody can read — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). F11 L213 states what F10 L208 and L226 already entail.
- **R2:** passage CHANGED (addition, consistent). R2 gives the same reason: file 11 "states outright what file 10 lines 208 and 226 already give".
- **Ruling: passage SAME. Follows R1.**
  - F10 L208: "A transport \(t\) between organizations of a physical system has exactly one of three provenances, determined by its history in the physical module:"
  - F10 L226: "The carrier–content relation is thus a fidelity fact with a history."
  - Losing present access changes no history, so F11 L213's first clause ("A carrier keeps its provenance when present access to it is lost") is entailed. Its second clause is not needed here.
  - The readers agree on the substance; they differ only in convention.
- Confidence: medium-high / high.

### O29 — The margin note
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L406: "An evidence leaf is a reference to an event with an interpreted claim. A receipt is a derivation tree over leaves." and "Negation exchanges them; missing evidence stays missing."
- File 11 has the same at L393. F11 L213 is consistent.
- Confidence: medium.

### O30 — The routine uploaded that morning
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L414: "Reconstruction by a learner is construction; relay is not." "Owned" is read in its ordinary sense.
- F11 L419: "a process that runs inside the boundary is the system's own today whoever wrote it". F11 L465: "a process run inside the boundary is the system's whoever wrote it".
- Confidence: medium.

### O31 — The wrong valve — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). F11 L401 states the partition that F10 L414's witness clause already draws.
- **R2:** passage CHANGED (addition, consistent). File 10 never says that the rest keeps its inherited provenance.
- **Ruling: passage CHANGED (additive). Follows R2.**
  - F11 L401: "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance."
  - This is the sentence both readers, R1 included, treat at O18 as a new claim, the one that turns file 10's SPLIT into AGREE. It cannot be entailed by file 10 in O31 and new in O18.
- Reconciler's note: the agreed file-10 AGREE here sits uneasily with the agreed file-10 SPLIT at O18. The structure is the same: received content plus one small binding of one's own. The readers separate the two cases by the verdict's wording. O18 says "exactly the tooth"; O31's "one relation was supplied by her" does not exclude her having assembled the corrected whole. The agreed marks are recorded as agreed.
- Confidence: medium / high.

### O32 — Found aloud, drawn later
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L430: "The content \(c\) may be an organization, a transport, or a contract." F10 L613: "The same holds for attribution from emitted text and for use inferred from delivery logs."
- File 11 has the same at L417 and L606. F11 L433 adds: "it credits each contribution the history establishes".
- Confidence: medium.

### O33 — The table with empty columns
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L168: "What a question asks — production, identification, obstruction, rule-status, purpose-achievement — is fixed by the type of \(\mathcal Q\) and the shape of \(C\), not by a label."
- F11 L161: "A contract is a declared subset of the physically admitted changes, and a stated scope is what makes it one."
- Confidence: medium-high.

### O34 — Where the second compartment used to be — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). F11 L163 spells out F10 L168 and L268.
- **R2:** passage CHANGED (addition, consistent with F10 L168 and L268).
- **Ruling: passage SAME. Follows R1.**
  - F11 L163: "Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one."
  - That is entailed by F10 L168 ("Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other.") and F10 L268 ("The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one."), together with F10 L176 on recorded changes of \(\mathcal Q\).
  - The difference is one of convention only.
- Confidence: medium-high / high.

### O35 — Four seconds — DISPUTED-BETWEEN-READERS
- Fixed verdict: The protected condition held in every way that mattered: nobody was without water. The interruption is on the record and is not a loss.
- **R1:** F10 AGREE, F11 SILENT, verdict CHANGED (AGREE to SILENT), passage CHANGED, away from the thoughtful person, theory change. Confidence medium for file 10.
- **R2:** F10 SILENT, F11 SILENT, verdict SAME (same point), passage CHANGED, no change. Confidence low-medium for file 10. R2 states that if file 10 AGREE is preferred, the row becomes CHANGED, away, a theory change traced to F11 L433 and L514.
- Both agree on F11 SILENT.
- **Ruling: F10 AGREE, F11 SILENT, verdict CHANGED, away, theory change. Follows R1.**
  - *File 10.* F10 L438: "**Repair.** For claimed obligations \(O\) and protected obligations \(P\), fixed for the comparison," with F10 L441, whose protected clause is \(\forall r\in P[r(\xi)\Rightarrow r(\xi')]\). F10 L444: "(P) does not rank alternatives. Losses outside \(P\) must be exposed."

    As written, file 10 checks a protected obligation at the two compared configurations only. The tap "then runs as before", so every state-reading of the protected condition holds at \(\xi'\). The interruption lies between the two configurations and is on the record, which is all L444 asks.

    R2's alternative needs a protected condition that ranges over the whole work interval. File 10 allows one (F10 L122: "Values of ports may be paths, functions, fields, proofs, or histories."), but this case does not state one, unlike O38. File 10 has no sentence that makes the scope of an unstated protected condition an open input. Reading r as a condition on the configuration, as the formula is written, is the text's own default, not a choice made from the wanted verdict.
  - *File 11.* F11 L433: "The obligations are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers." F11 L514: "A verdict that depends on one of these is a verdict given the input; where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted."

    The occasions are not stated: every moment of the work, or only the moments when someone draws water. So the verdict is unsettled. The change traces to these two new sentences, and the file-10 endpoint check that gave "held" can no longer stand without a stated input.
- Confidence: low-medium for file 10, where R2's reading is live; medium-high for file 11.

### O36 — A premise both routes use — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). **R2:** passage CHANGED (addition, consistent with file 10's (S) over subsets of \(\Gamma\)).
- **Ruling: passage SAME. Follows R1.**
  - F10 L304: "For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed." (S) and (B) (F10 L313) range only over subsets of the written \(\Gamma\).
  - So F11 L301 is entailed: "Criticality is relative to the support \(W\) it is assessed in: a commitment critical in one successful support need not be critical in the full candidate, and the supports assessed are the ones actually written, not a support someone could write in their place."
  - R2's own reason for its label is this same entailment.
- Confidence: medium-high / high.

### O37 — The uncited textbook — DISPUTED-BETWEEN-READERS (file-10 mark only)
- Fixed verdict: As written, the order has a circle in it. The textbook proof would break the circle, and the account has not used it. The order is not settled until it does.
- Both readers: F11 AGREE, verdict CHANGED, passage CHANGED, toward the thoughtful person, theory change.
- **R1:** F10 SILENT. File 10 states no well-foundedness requirement and says nothing on uncited proofs, so its sentences stop short.
- **R2:** F10 SPLIT on the third point.
  - Reading A agrees, from F10 L344 (circular support) and F10 L394 (a reason is used only when it "lands on an active route").
  - Reading B disagrees, from F10 L406: "For \(\phi\), \(P_j(\phi)\) and \(N_j(\phi)\) are the usable receipts for and against." Standing comes from usable receipts, and (K2) sets no condition of citation, so the textbook proof already supplies the place.
- **Ruling: F10 SPLIT. Follows R2.**
  - Both of R2's readings apply file-10 sentences directly to the point at issue, and they reach different findings on "the order is not settled until it does".
  - Reading A: F10 L344, "its support is circular though its content might be true." And F10 L394: "A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route."
  - Reading B: the usable-receipts sentence of F10 L406, with (K2) requiring only license, scope and live premises.
  - The text leaves the choice open. SPLIT comes before SILENT in the order of rules.
  - File 11 closes the question in words that reject Reading B. F11 L518: "The order is well founded: a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it, and a separate proof that would supply it counts only when the account uses it."
  - R1's SILENT gives the same verdict change and direction.
- Confidence: medium-low for file 10; high for file 11.

### O38 — Written on the job sheet
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L438: "**Repair.** For claimed obligations \(O\) and protected obligations \(P\), fixed for the comparison,". The condition was stated over the whole work period, "runs at all times during the work". F10 L444: "(P) does not rank alternatives."
- F11 L433: "a protected condition is lost exactly when it fails on an occasion it covers."
- Confidence: medium / high.

### O39 — Two routes, both running — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). F10 L324 carries the finding, and F11 L433 is a new explicit statement that agrees with it.
- **R2:** passage CHANGED. File 10 leaves ProducedBy undefined; file 11 defines it and adds the credit rule.
- **Ruling: passage CHANGED (additive). Follows R2.**
  - The verdict's "the leak was stopped by both, and neither can claim it alone" is an attribution of producing a repair. In file 11 that rests on F11 L433: "\(\operatorname{ProducedBy}\) holds when an active route (Part IX) runs from \(\Delta\) to the repair; it credits each contribution the history establishes, and where two sufficient contributions both ran, both are credited and the history supplies no division of credit that it does not contain."
  - File 10 has no definition of ProducedBy. O39 has the same structure as O20, where both readers, R1 included, agreed the passage is CHANGED (additive).
- Confidence: medium / high.

### O40 — Two hands on the test
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L25: "It does not supply an objective aesthetics, a probability of truth, a merit function, or a ranking of thinkers." F10 L414: "Reconstruction by a learner is construction; relay is not."
- F11 L27: "It does not supply a division of credit among contributors beyond what a history establishes (Part XI)." F11 L433: "it credits each contribution the history establishes".
- Reconciler's note: both readers weighed a file-10 SPLIT contrary. Build over the whole reinterpretation, with the expert's proposal as an incoming carrier, would make the reinterpretation the robot's. That is the same mechanism that decides O41 below. Both readers rejected it here because the expert's own subhistory also holds a nontrivial binding, so the reading still ends in "both". The agreed mark is recorded.
- Confidence: medium-low / medium-high.

### O41 — The technician's whisper — DISPUTED-BETWEEN-READERS
- Fixed verdict: The boundary was robot-only, and the instruction crossed it. The diagnosis is a team result under a boundary nobody restated. Robot-only credit is not available for it.
- Both readers: F11 AGREE, passage CHANGED.
- **R1:** F10 SPLIT, verdict CHANGED (SPLIT to AGREE), toward the thoughtful person, theory change.
  - Reading A: the instruction is one of "the incoming carriers", and the robot's own subhistory holds Build under β = robot-only, so robot-only credit is available (F10 L414).
  - Reading B: the instruction was relayed from outside the declared boundary and resource contract. That rests on L414 ("relay is not"), L476 and L523.
- **R2:** F10 AGREE, verdict SAME, no change. Every claim is relative to the declared robot-only boundary (F10 L523), and the instruction came from outside it. R2 rates its own SPLIT contrary as failing "narrowly" and notes that "file 10 never says that instructions from outside differ from other incoming carriers".
- **Ruling: F10 SPLIT, verdict CHANGED (SPLIT to AGREE), toward the thoughtful person, theory change. Follows R1.**
  - Build is indexed by β and needs only "an actual subhistory owned by \(s\)", which the robot's reading and completing are. F10 L414: "A construction witness identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation." Incoming carriers come from outside s by nature.
  - File 10 has no sentence that makes an outside instruction different from any other incoming carrier. The robot-only index (F10 L523: "Every claim is relative to them; none is a predicate that could be true or false.") says what the claim is relative to. It does not say that an incoming carrier from outside β voids the robot's Build.
  - Against that, "Reconstruction by a learner is construction; relay is not." (F10 L414) and the "resource contract" of F10 L476 support Reading B.
  - This is the same unresolved question as O18, which both readers rule SPLIT: what Build credits when received material and one's own binding are mixed.
  - File 11 settles it. F11 L419: "Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside;". F11 L465: "Both are declared before the attribution, not chosen after it."
- Confidence: low-medium for file 10; high for file 11.

### O42 — New board, old memory — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). What Ω means already gives F11 L465.
- **R2:** passage CHANGED (addition, consistent).
- **Ruling: passage CHANGED (additive). Follows R2.**
  - File 10 names continuity only as an index. F10 L523: "Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices." F10 L476 adds: "under the same continuity and resource contract". File 10 never says what Ω is or what preserving it does.
  - File 11 defines both. F11 L465: "A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change). A replaced part that preserves the declared continuity leaves the same system;".
  - A definition of a word file 10 leaves to ordinary sense is an addition. The readers agreed on the parallel case of ownership at O17, O30, O49 and O51, all CHANGED.
- Confidence: medium-high / high.

### O43 — Mirrored marks — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit); F11 L363 applies Derivation 8. **R2:** passage CHANGED (addition, consistent with Derivation 8).
- **Ruling: passage SAME. Follows R1.**
  - F10 L609: "**Claim.** Transporting all carriers, relations, transports, histories, and contracts along structure-preserving bijections preserves (E), (G), (P), (EK)." F10 L394 already speaks of "content-preserving recodings".
  - An invertible recoding whose reader recovers every pairing is such a bijection. So F11 L363 ("A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing (Derivation 8).") is entailed.
  - The difference is one of convention.
- Confidence: medium-high / high.

### O44 — Half from the source, half from the shelf — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). **R2:** passage CHANGED (addition, consistent).
- **Ruling: passage SAME. Follows R1.**
  - F10 L208 fixes provenance by history. F10 L13: "The three are distinguished by their histories, not their outputs, and the semantics keeps them apart." F10 L184: "Occurrences are not identified by carrying the same words; contents are not identified by having the same outputs."
  - These entail F11 L363: "A section of a carrier filled from another source keeps that other source's history, whatever it happens to match."
- Confidence: medium-high / high.

### O45 — The spring nobody mentioned — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). F11 L309 states what F10 L280, L324 and L613 give together.
- **R2:** passage CHANGED (addition, consistent).
- **Ruling: passage SAME. Follows R1.**
  - F10 L280: "Every conjunct is a condition on how supplied relations behave under the changes in \(C\). None inspects a label." F10 L324 has the redundant-routes pattern.
  - The account "contains two springs, both connected", so the second is among the account's commitments from the start, and whether anyone described its work is a label.
  - F11 L309 ("A route already present in the candidate is a route whether or not anyone has described its work;") therefore adds nothing file 10 does not give. Both readers' strongest contrary, that the spring is outside the identified \(\Gamma\) (F10 L246), fails on the case's own statement.
- Confidence: medium / high.

### O46 — The cable that used to be a spring — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). **R2:** passage CHANGED (addition, consistent).
- **Ruling: passage SAME. Follows R1.**
  - F10 L246: "An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\)." F10 L120: "A changed rule is a changed component." F10 L304 keeps "the named background fixed".
  - Re-anchoring a component changes \(t\) and so the candidate. That entails F11 L309: "a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment, and the new candidate's success is not the old one's."
- Confidence: medium-high / high.

### O47 — One more commitment
- Both readers: AGREE / AGREE, SAME, SAME.
- F10 L310: "No upward closure and no minimal member are assumed." F10 L326: "Success of a subset does not imply success of the whole; \(b\) is not made "not a commitment" to repair this."
- F11 L307: "The theorem applies only where its assumptions hold; an addition to \(\Gamma\) that destroys a support is the interference case below, and there upward closure fails."
- Confidence: high.

### O48 — The forbidden wire
- Both readers: DISAGREE / AGREE, CHANGED, CHANGED, toward the thoughtful person, theory change. This is the one change file 11's header (L5) declares.
- F10 L569: "**Claim.** Let \(t\) be selected on a finite history \(H\subsetneq C\). For every \((a,b)\in C\setminus H\) there exists a transport \(t'\), also surviving on \(H\), with a different value at \((a,b)\)." F10 L38: "There is a theorem below (Derivation 3) that selected transports are *always* underdetermined on unseen changes." F10 L539: "A selection history \(H\subsetneq C\) whose survivor is determined on \(C\setminus H\). This refutes Derivation 3."
- F11 L562: "The presence of an unseen pair alone does not establish that such a \(t'\) exists; it must be admitted, realizable, a member of \(\mathcal T\), and a survivor of \(H\)." F11 L473: "The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it."
- Passage labelled CHANGED (alteration) by the reconciler: file 11 withdraws file 10's unqualified claim. Both readers said CHANGED without a sub-label. Confidence: high.

### O49 — Owned means capable
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L414: "Reconstruction by a learner is construction; relay is not." F10 L416: "A physical system may exhibit both; the witnesses differ."
- F11 L467: "Ownership is grounded in the processes and resources the boundary includes, never in the capability being attributed: "owned because it can, and can because owned" grounds neither."
- Confidence: medium / high.

### O50 — The same afternoon, three achievements — DISPUTED-BETWEEN-READERS
- Fixed verdict:
  - Credit each achievement on its own.
  - The reinterpretation was theirs together.
  - The discovery was the robot's: it ran the test and found the fault.
  - The inquiry was mostly the expert's: the expert framed it, supplied the candidates and the test, and supplied the fix.
  - One word for all three would be wrong for at least two of them.
- **R1:** F10 AGREE, F11 AGREE, verdict SAME, passage CHANGED. The verdict grounds "mostly" in the list of the expert's contributions, which both theories reproduce contribution by contribution. Confidence medium-low / medium.
- **R2:** F10 SILENT, F11 SILENT, verdict SAME (same point), passage SAME. Neither file turns a list of contributions to one composite achievement into "mostly". Confidence medium-low.
- **Ruling: F10 SILENT, F11 SILENT, verdict SAME, passage SAME. Follows R2.**
  - Every other point is reached. Origin is per content (F10 L430: "The content \(c\) may be an organization, a transport, or a contract.").
  - "The inquiry was mostly the expert's" is different. Both theories credit, for the inquiry, the expert's framing, candidates, test and fix, and also the robot's objection, its running of the test and its discovery. The discovery is the robot's answer to the inquiry's question.
  - Turning that list into "mostly" needs a weighting, and both files mark that place empty. F10 L25: "It supplies places where such things would go if anyone had them, and marks those places as empty." F11 L27: "It does not supply an objective aesthetics, a probability of truth, a merit function, a measure of worth, or a ranking of thinkers. Where a claim needs one of these, the semantics takes it as a **declared input** and marks the place (Parts XI, XIV). It does not supply a division of credit among contributors beyond what a history establishes (Part XI)."
  - *Consistency.* O40's agreed AGREE rests on this same absence: "neither can say 'mostly'" is reached because no weighting exists. The same absence leaves "mostly the expert's" open here.
  - *Why O21 and O27 differ.* In both, "mostly" names where the single originative act lies (note at O21). In O50 the inquiry holds originative acts by both parties.
  - *Passage.* The deciding sentence is the disclaimer, present in both files. F11 L27 adds "a measure of worth", the pointer to a declared input and the clause on credit. These sharpen the silence but claim nothing file 10's L25 does not already leave empty. So SAME, following R2.
- Confidence: medium-low for both files.

### O51 — The module in the casing
- Both readers: AGREE / AGREE, SAME, CHANGED (additive).
- F10 L523: "Every claim is relative to them; none is a predicate that could be true or false." Build requires "an actual subhistory owned by \(s\)" (F10 L414).
- F11 L419: "and where the boundary is drawn decides, not where the process sits in the casing." F11 L465: "a process run outside it is not the system's however close it sits."
- Confidence: medium / medium-high.

### O52 — The route that started and was stopped — DISPUTED-BETWEEN-READERS (passage only)
- Both readers: AGREE / AGREE, verdict SAME.
- **R1:** passage SAME (added, explicit). F11 L371 applies the unchanged active-route definition. **R2:** passage CHANGED (addition, consistent).
- **Ruling: passage SAME. Follows R1.**
  - F10 L384: "An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components satisfy the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts." A jammed bypass that took nothing joins nothing to the result.
  - So F11 L371 ("A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result.") spells out the definition.
  - Both readers agreed on exactly this at O19 and O25, PASSAGE SAME, and R2's CHANGED here departs from its own O19 and O25.
- Confidence: medium-high / high.

---

## Baseline comparison (step 4, written after steps 1 to 3)

The only part of the S81 plan (second version, in `Semantics/tests/`) that was read is the paragraph found by exact match:

> The baseline is S75's determination on file 10 (from the S72 table as audited): **DISAGREE** on O48; **SILENT** on O1, O12, O20, O21, O27, O35, O40 and O50; **AGREE** on the other forty-three, O24 among them.

The table below lists every row where the reconciled **file-10** mark differs from that baseline. Rulings were not changed after reading it.

| row | baseline (S75, file 10) | reconciled file-10 | readers (R1 / R2) | note |
|---|---|---|---|---|
| O18 | AGREE | SPLIT | SPLIT / SPLIT (agreed) | Build of the whole key against the witness clause and "relay is not" |
| O20 | SILENT | AGREE | AGREE / AGREE (agreed) | both readers rated file 10 low or medium; R1 called SILENT "a live alternative" |
| O21 | SILENT | AGREE | AGREE / AGREE (agreed) | both readers rated file 10 low or medium-low; the SILENT contrary on "mostly" was held to fail |
| O27 | SILENT | AGREE | AGREE / AGREE (agreed) | "mostly" read as the robot's Origin of the answer |
| O35 | SILENT | AGREE | AGREE / SILENT (disputed) | the baseline matches R2; the reconciler followed R1 (endpoint reading of (P)) |
| O37 | AGREE | SPLIT | SILENT / SPLIT (disputed) | neither reader marked AGREE; R1 thought AGREE "partly holds" |
| O40 | SILENT | AGREE | AGREE / AGREE (agreed) | both readers rated file 10 medium-low |
| O41 | AGREE | SPLIT | SPLIT / AGREE (disputed) | the baseline matches R2; the reconciler followed R1 |

**8 rows differ:** O18, O20, O21, O27, O35, O37, O40, O41.
- Four of them (O20, O21, O27, O40) are baseline SILENT against a reconciled AGREE on which both readers agreed.
- Three (O18, O37, O41) are baseline AGREE against a reconciled SPLIT.
- One (O35) is baseline SILENT against a reconciled AGREE on a disputed row.
- The baseline has no SPLIT.
- It matches the reconciled file-10 mark on the other 44 rows: O1, O12 and O50 SILENT, O48 DISAGREE, O24 and the rest AGREE. Among these are three disputed rows where the reconciler's ruling coincides with the baseline: O1 (R2 had AGREE), O16 (R1 had SILENT) and O50 (R1 had AGREE).

## Rows ruled SILENT, with the Declared-inputs answer

For each SILENT, the answer to "does file 11's Declared-inputs paragraph (F11 L514) name the missing input?". F11 L514: "**Declared inputs.** Besides the two primitives, some claims take stated inputs that the semantics records and does not supply: the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and what makes a restriction appropriate (Part III); the system boundary and continuity of an attribution (Part XII)."

| row | file(s) | point left open | missing input | named in F11 L514? |
|---|---|---|---|---|
| O1 | file 10 and file 11 | "the series as a whole is a retreat" | what makes Bruno's restrictions appropriate: a ground tying each limit to an account, or a criterion for a legitimate series | **Yes**: "the scope of a contract and what makes a restriction appropriate (Part III)". In file 10 the gap is in the sentences, since file 10 has no notion of appropriateness. |
| O12 | file 10 and file 11 | "a better question, and its merit is real" | a normative relation \(\mathcal N\) (a standard of worth) | **No.** \(\mathcal N\) is primitive 2 (F11 L510: "The **normative relation** \(\mathcal N\), when a question invokes worth."). The paragraph opens "Besides the two primitives", so it excludes \(\mathcal N\). F11 L447 and L27 call it a declared input elsewhere. |
| O35 | file 11 only | "the protected condition held"; "is not a loss" | the protected condition \(P\) as stated, and the occasions it covers: every moment of the work, or only the moments water is drawn | **Yes**: "the obligations \(O\) and \(P\) of a repair, with the occasions each covers (Part XI)". |
| O50 | file 10 and file 11 | "The inquiry was mostly the expert's" | a weighting of contributions to a composite achievement, that is, a division of credit beyond what the history establishes | **No.** The paragraph names boundary and continuity but no weighting of credit. Only Part 0 (F11 L27) sends such measures to declared inputs in general terms and denies any "division of credit among contributors beyond what a history establishes". |

The readers' SILENT readings that the reconciler did not adopt:
- R1 F10 SILENT at O16. The reconciler rules AGREE.
- R1 F10 SILENT at O37. The reconciler rules SPLIT. R1 found no missing case input: the sentences stop short. F11 L514 names no such input.
- R2 F10 SILENT at O35. The reconciler rules AGREE. R2's input was the same as file 11's, the protected condition and its occasions, which F11 L514 names.
- R2 F10 and F11 AGREE at O1 rejected R1's SILENT. The reconciler follows R1.
- R1 AGREE at O50 rejected R2's SILENT. The reconciler follows R2.
