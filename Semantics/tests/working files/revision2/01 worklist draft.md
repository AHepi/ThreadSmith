# 01 Worklist draft for a revision 2 of the theory

23 September 2026. Written by Claude as a draft. It is not a decision. Nothing in the repository was edited.

## What this is

This file lists every known candidate change for a revision 2 of "Claude Fable Semantics". Round S81 is now deciding whether file 11 (revision 1) replaces file 10 (the frozen authority). Until it does, the base for revision 2 is open, so every item gives its place in both files.

## Sources read

- **Theory files, in full:** file 10, file 11 and file 12. File 00 was read at the lines cited below.
- **Records:** the project story in full, and the Decisions list up to S19.
- **Results:** S78 Results; the S81 DeepSeek trial; S75 (by search); S72 Stage 2 return file 05, plus the quoted text of R2 J in its file 01.
- **Claude's S81 determination:** files 01 and 02, their READ ME, and the "genuinely hard" and observations sections of the four raw case readings.
- **Case book:** the S81 case book (situations and fixed verdicts).
- **Scratchpad:** `sources/verify/01 verification of source observations.md` and `source_cases/cases - final candidates.md`.

## Not opened

- Any S81 1C, 1K, 2a or 2b return, reasoning file, receipt, sample or table.
- The `effort controls` folder, the S81 briefs, the S81 plans and the S81 trial folder.
- `sources/pinker/`.

The determination folder contains no file 03. That was checked in the local checkout and on the working branch on GitHub at the time of writing.

## Conventions

- **Line references.** "F10 L270" means file 10, line 270. F11, 12: and 00: refer to files 11, 12 and 00 in the same way.
- **Determination files.** "det 01" and "det 02" are the S81 determination files 01 and 02 in `Semantics/results/S81 File 11 against every case - outputs/determination/`. "Raw 01a" to "raw 01d" are the raw readings held there.
- **"Trial".** The S81 DeepSeek trial results file.
- **"Verify obs n" and "M n".** The observation number and the "missed relation" number in the verification file.
- **Severity levels:**
  - **verdict-changing:** the current text moves an existing case verdict, or the proposed change is meant to move one.
  - **coherence:** a definition, proof, type or consistency defect, or a missing notion. No verdict is meant to move, though some carry a verdict risk, which is named.
  - **attribution-erratum:** a wrong note, pointer or label, a missing attribution, or notation that can be restored word for word.
  - **process:** a prerequisite for the round, not a change to the theory text.
- **Handling types:** erratum; clarification (says what the text already implies, or closes a reading gap); new claim or condition; leave alone (with the reason stated).
- **S81 dependence:**
  - **Independent:** the text is the same in files 10 and 11.
  - **File-11 base only:** the item exists only in file 11's added text. If file 10 stays the base, the item applies only when that sentence is carried over.
  - **File-10 base only:** the item is needed only if file 10 is the base.
  - **Both, differently:** the item is needed either way, in different forms.

### A correction to the brief

- **S78's groups A, B and C repair the two-stage testing pattern, not the theory text.** Story S81 says the group A repairs were applied when round S81 was rebuilt. They were not applied to file 11, which was written at S76 before S78.
- **S78 bears on the theory in two items only:**
  - Item 6: file 11 carries the "occasions" sentence, which file 10 does not. That is W4 and W5 below.
  - Item 10: R2 J's Part VIII qualification, the initial-error term, has no case. That is W31.
- **Groups B and C and the group A leftovers** are listed as process items W51 to W53.

---

## Summary table

| id | title | severity | proposed handling | S81 |
|---|---|---|---|---|
| W1 | File 11's revision note misdescribes the revision (XR1, XR2) | attribution-erratum | erratum | both, differently |
| W2 | Carry Derivation 3's qualification (O48) | verdict-changing | new claim (already in F11) | file-10 base only |
| W3 | Three undeclared sentences move O18, O37, O41 toward the fixed verdict | verdict-changing | declare (F11) or import (F10) | both, differently |
| W4 | O35 moves away from the fixed verdict under file 11 | verdict-changing | leave and record; or a stated default | both, differently |
| W5 | (P)'s formula and the occasions prose disagree | coherence | clarification | file-11 base (or if occasions imported) |
| W6 | The normative relation: primitive or declared input; front-matter claims with no support in the body (XR3, XR5) | attribution-erratum | erratum | file-11 base only |
| W7 | Declared inputs against indices and "everything else is derived"; Derivation 6's proof (XR6) | coherence | clarification | file-11 base only |
| W8 | Part 0's short form of attack (D) is unqualified | attribution-erratum | erratum | file-11 base (F10 via W2) |
| W9 | The "bell and tide" parenthesis names a case (XR4) | attribution-erratum | erratum | file-11 base only |
| W10 | Derivation 10's glosses: on Derivation 3 (XR7) and its citation of Derivation 2 | attribution-erratum | erratum | both, differently |
| W11 | "A table that genuinely encodes … is an account" claims too much | coherence | clarification | file-11 base only |
| W12 | Ownership needs a declared boundary that many cases lack | verdict-changing (risk) | clarification or leave | file-11 base only |
| W13 | The two halves of the Ownership sentence assign different things | coherence | clarification | file-11 base only |
| W14 | "Mostly": a weighting of credit is supplied by neither file | coherence (verdict risk) | clarification | both, differently |
| W15 | Part XV: a case that turns on a missing declared input is not a refutation | coherence | clarification | both (more needed with F11) |
| W16 | Derivation 3 in file 11 has almost no refutable content | coherence | clarification or restatement | both, differently |
| W17 | What "surviving on H" means | coherence | clarification | independent |
| W18 | Whose knowledge a population's fixing is (source point M3) | coherence | clarification or new claim | independent |
| W19 | Derivation 2's proof does not pair the two candidates' components (Mimo M6) | coherence (exposed in Part XV) | restate claim or supply proof | independent |
| W20 | Non-circular dependence has a target edit act on the explanation's commitments (Mimo M3) | coherence (verdict risk) | clarification (retype) | independent |
| W21 | \(\equiv_\ell\) in (N) is undefined (Mimo M4) | coherence | clarification (define) | independent |
| W22 | \(\mathcal E_c\) is undefined in (K1), and \(p\) is unused (Mimo M2, M1) | coherence | erratum and clarification | independent |
| W23 | \(\Delta\), Result(\(\Delta\)) and ProducesVia are undefined | coherence | clarification | both, differently |
| W24 | \(S_a\), \(T_a\) and "generator" are undefined (Atria A3 = Mimo M7) | attribution-erratum | erratum (restore 00:518) | independent |
| W25 | Admit, Cap\(^{q,r}\), the grades \(q,r\), Poss and Enable are undefined (Mimo M8) | coherence | erratum and definition | independent |
| W26 | Tag (I3) is missing (Atria A2) | attribution-erratum | erratum | independent |
| W27 | Attack labels collide with equation tags | attribution-erratum | erratum | independent |
| W28 | "Route" in Part VI against "active route" in Part IX (J-4) | coherence | clarification | both, differently |
| W29 | No rule says when a proxy measure counts as the target's answer (O4) | coherence | clarification | independent |
| W30 | A set-point difference is a state, not a kind (O10) | coherence (low) | clarification | independent |
| W31 | (T2) has no initial-error term (S78 item 10; R2 J) | coherence (mathematical) | erratum | independent |
| W32 | A stated limit that nothing in the account explains (source point 6; row A; O1) | verdict-changing (O1) | clarification plus an optional Part VI measure | both, differently |
| W33 | Idle parts: (E) accepts them; hard-to-vary is a lemma (source point 2, M7) | coherence | clarification; leave as not-a-condition | independent |
| W34 | "Reach" is used once and never defined (source point 5) | coherence | clarification (restore 00:383) | independent |
| W35 | Surprise is narrower than Deutsch's "problem"; "recognized difficulty" is undefined (source point 13, M2; file 12) | coherence | choose (b) define, or (c) adopt file 12 | independent |
| W36 | "Explanation" and "account" are each used in two senses (source point 4; O15) | coherence | clarification | independent |
| W37 | File 11 dropped "blind" from Part 0 (source point 9) | attribution-erratum | erratum and clarification | file-11 base only |
| W38 | Sources and lineage are not named (source points 1, 3, 10) | attribution-erratum | attribution note | independent |
| W39 | Same-form regress: identity of the answer is structural at the grain (source point 12) | coherence | clarification (restore 00:210) | independent |
| W40 | An eliminative explanation must also explain the appearance (M6; source point 15) | coherence | clarification | independent |
| W41 | Inexplicit representation (source point 14; 00:855–861) | coherence | clarification (restore) | independent |
| W42 | Error-correction as a derived lemma (source point 14) | coherence | new claim (lemma); defer | independent |
| W43 | Knowledge as self-preserving information (source point 8) | coherence | leave, with a stated reason | independent |
| W44 | Level of explanation (source point 11) | coherence | clarification; optional derived notion | independent |
| W45 | Interoperability and substrate independence (M4) | coherence | clarification | independent |
| W46 | Realized edits and the two notions of counterfactual (source point 7; 12:491; O22) | coherence | clarification (carry back from 12) | independent |
| W47 | Causal dependence, collateral offered as a cause, common cause and chain, direction as a theorem (file 12) | coherence | new claims; defer | independent |
| W48 | Actual causation (AC); ProducedBy defined through (AC); contrasts as an input (file 12) | coherence | new claim; defer or partial | both, differently |
| W49 | Absence and prevention constructions; attack B widened (file 12) | coherence | new constructions; defer | independent |
| W50 | What a failed intervention refutes (K3; 12:411) | coherence (low) | clarification | independent |
| W51 | S78 group B: the seeded-error round is unfinished | process | finish before trusting revision 2's round | — |
| W52 | S78 group C: cases out of the determiner's hands (N-cases) | process | adopt as O53 onward in a round | — |
| W53 | S78 group A leftovers (D3-T as O53 not entered) | process | enter or drop | — |
| W54 | The FW5 richness audit (S79 method) is only partly done | process | finish the list | — |
| W55 | The first 32 Stage B rows are unrecovered; the R2 file is absent | process | recover or record as unknown | — |
| W56 | Determination files 01 and 02 disagree on O38's file-10 mark | process | settle in the determination | S81 |

**Where the seven XR slips are:** XR1 and XR2 are in W1; XR3 and XR5 in W6; XR4 in W9; XR6 in W7; XR7 in W10.

---

## Group 1. What revision 2 inherits from S81's outcome

### W1. File 11's revision note misdescribes the revision

- **What is wrong.** The note (F11 L5) says the rewrite keeps "the same … definitions, conditions". It also says "One claim changes … Nothing else changes in what is claimed". Neither holds:
  - File 11 adds five definitions: Ownership (L419), ProducedBy (L433), boundary and continuity (L465), the population (L473) and Declared inputs (L514).
  - Det 02 counts 46 CLAIM places inside the theory.
  - Det 01 finds five changed verdicts, not one: O48, O18, O37 and O41 move toward the fixed verdict; O35 moves away.
  - The note's list of restating sentences follows file 10's layout (XR1) and omits the Derivation 3 places C32 (L197), C35 (L225), C64 (L473) and C81 (L616).
  - The note names case O48 and "Semantics results S75", which are outside the document (XR2).
- **Where.** File 10: no note. File 11: front matter, L5.
- **Evidence.**
  - Det 02: C1, XR1, XR2, §5(i) and the counts in §6.
  - Det 01: reconciled counts. Raw 01b "Observations": "The header's 'Nothing else changes in what is claimed' does not hold of the body".
  - S78 item 6 and its correction to S75 point 2: file 11's one-claim count "is under test, not established".
- **Severity.** Attribution-erratum.
- **Handling.** Erratum. Revision 2's own note should:
  - list every CLAIM place by Part, or point to a change table;
  - name every verdict the revision moves, in both directions;
  - name no case identifier and no record file, because those steer testers (XR2).
  If file 11 is not adopted, the same rule applies to revision 2's note.
- **Gained.** A note a reader can trust, with no steering toward O48.
- **Lost.** Nothing in the theory. The note gets longer.
- **Tests.** None; this is a meta item. The cases the note must report are O18, O35, O37, O41 and O48.
- **Depends on.** W2, W3 and W4, since the note must report their outcome.
- **S81.** Both, differently. Its content depends on which base S81 leaves and on which verdict changes S81 confirms.

### W2. Carry Derivation 3's qualification (only if file 10 stays the base)

- **What is wrong.** File 10's Derivation 3 asserts a differing survivor at every unseen pair. That gives the wrong verdict on O48, the forbidden wire.
- **Where.**
  - File 10: L38 (grievance 3), L74 (attack D), L539 (Part XV), L567–573 (Derivation 3).
  - File 11: L43, L197, L225, L473, L534, L560–566, L616.
- **Evidence.**
  - S75 (one amendment changes one verdict).
  - S73: an outside judge reached the same point from file 10 alone.
  - Det 01 O48: DISAGREE becomes AGREE. This is the only passage ruled CHANGED (alteration).
  - Det 02 §5(i): ten CLAIM places in the cluster.
- **Severity.** Verdict-changing.
- **Handling.** New claim. On a file-10 base, carry the whole cluster of ten places (C13, C32, C35, C64, C73, C75–C78, C81), not only the four the note names. Then apply W16 and W17.
- **Gained.** O48 gets the fixed verdict, and the proof matches the claim.
- **Lost.**
  - The blanket guarantee that every untested value is open.
  - Derivation 3's refutable content shrinks (W16).
  - O24 is at risk. It must stay AGREE: a reachable, differing arrangement is given in the case.
- **Tests.** O48 and O24, with O11 as a control (S72 Stage 2, next step). N5, and N18 (Dov's copied bridge).
- **Depends on.** W16, W17, W18.
- **S81.** File-10 base only. On a file-11 base it is already done.

### W3. Three undeclared sentences move O18, O37 and O41 toward the fixed verdict

- **What is wrong.** File 11 moves three verdicts that its note does not declare:
  - O18, the one tooth: SPLIT becomes AGREE, through F11 L401 s5 on a small binding inside received content.
  - O37, the uncited textbook: SPLIT becomes AGREE, through F11 L518, last sentence: "The order is well founded …".
  - O41, the technician's whisper: SPLIT becomes AGREE, through F11 L419: outside work stays an outside contribution.
- **Where.**
  - File 10: Build L414 (O18, O41); dependence order L525, receipts L406 and reason use L394 (O37).
  - File 11: L401, L518 and L419.
- **Evidence.**
  - Det 01, rows O18, O37 and O41. O18 was agreed by both readers. O37 and O41 were disputed and ruled by the reconciler.
  - Det 02: C53, C55 and C67.
- **Severity.** Verdict-changing.
- **Handling.**
  - File-11 base: erratum in the note (W1), and keep the sentences.
  - File-10 base: new claims; import all three.
- **Gained.**
  - Three verdicts move toward the fixed verdicts.
  - File 10's open question closes: what Build credits when received content and one's own binding are mixed.
- **Lost.**
  - C55 brings in the boundary dependence (W12).
  - C67 adds a well-foundedness claim that the dependence order does not yet list (W7).
  - O31, the wrong valve, has O18's structure; the reconciler noted unease with its file-10 AGREE.
  - Also at risk: O40, where Build over the whole reinterpretation is a live contrary; O17 and O49 (C67); O30 and O51 (C55).
- **Tests.**
  - C53: O18, O31, O15, O11.
  - C67: O37, O49, O17.
  - C55: O41, O21, O27, O30, O40, O50, O51.
  - N15 (a small repair inside received content), N21, N13.
- **Depends on.** W7, W12.
- **S81.** Both, differently. If S81's returns show a different set of changed rows, the list changes.

### W4. O35 moves away from the fixed verdict under file 11

- **What is wrong.** F11 L433 adds "each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers". Together with the missing-input rule at F11 L514, this turns file 10's endpoint reading of (P) ("held") into "unsettled".
  - O35 states no occasions: the tap stopped for four seconds and nobody drew from it.
  - This is the only verdict that file 11 moves away from the fixed verdict.
- **Where.**
  - File 10: Part XI, L438–444, with (P) at L441 and L444.
  - File 11: Part XI, L427–433, with (P) at L430 and the prose at L433; Part XIV, L514.
- **Evidence.**
  - Det 01 O35: F10 AGREE, F11 SILENT, CHANGED away. The readers disputed it, and file 10's confidence is low to medium.
  - Det 02 §5(ii).
  - S78 item 6: the occasions sentence came from the other model's clause H65, via W08.
  - Story S70 (H65's origin; O35 has been open since).
  - Trial: O35 is partial for all three blind readers, and Mimo departed from the fixed verdict using an occasion O35 never states.
  - The S75 baseline had file 10 SILENT on O35. Under that baseline the row does not change.
- **Severity.** Verdict-changing.
- **Handling.** Choose one:
  - **(a) Leave the text.** Record O35 as a case whose fixed verdict supplies the missing input ("in every way that mattered" means the occasions of use), and put it to the owner as CASE DISPUTED.
  - **(b) Add a general default, stated in advance:** "A protected condition stated without occasions covers the occasions of the use it protects." O35 then becomes AGREE.
  - **(c) File-10 base.** Import only "a protected condition is lost exactly when it fails on an occasion it covers", for stated occasions, and state the endpoint reading as the default.
  Recommended: (a), with (b) as the owner's call. Use (c) if file 10 is the base.
- **Gained.**
  - (a): no input is chosen from the wanted verdict, and the SILENT is honest.
  - (b) and (c): O35 returns to AGREE.
- **Lost.**
  - (a): one verdict stays away from the fixed verdict.
  - (b): a default input sits uneasily with L514 ("rather than choosing the input from the verdict wanted") and with L465 ("declared before the attribution"). The same move would then be owed for boundaries (W12).
  - O38 is at risk under every option. It must stay AGREE, because its occasions are stated.
- **Tests.** O35 and O38. N19, where the protected obligation is the lyrical passage.
- **Depends on.** W5, W6, W7, W12 (the same "default input" question), W15, W56.
- **S81.** Both, differently. The direction depends on S81's ruling on file 10's O35.

### W5. (P)'s formula and the occasions prose disagree

- **What is wrong.** (P)'s protection clause, \(\forall r\in P[r(\xi)\Rightarrow r(\xi')]\), checks two configurations. F11 L433 defines loss as failure on any covered occasion, and such an occasion can fall between \(\xi\) and \(\xi'\). The formula and the prose agree only if \(r(\xi')\) is read as "held on every covered occasion up to \(\xi'\)".
- **Where.** File 10: L441. File 11: L430 and L433.
- **Evidence.** Det 02 §5(ii) (C56).
- **Severity.** Coherence.
- **Handling.** Clarification. Restate the clause over occasions, for example \(\forall r\in P\ \forall\omega\in\mathrm{Occ}_r\cap[\xi,\xi']\,[r(\xi)\Rightarrow r(\omega)]\), or state the reading in words. On a file-10 base with no occasions imported, state the endpoint reading explicitly.
- **Gained.** The formula and the prose say one thing.
- **Lost.**
  - (P) becomes history-valued.
  - Derivation 8 (equivariance of (P)) must carry occasions along.
  - O35 and O38 are at risk, as in W4.
- **Tests.** O35 and O38. N19: the first draft keeps the pace but loses the protected lyrical passage, so Repair must fail. N18.
- **Depends on.** W4.
- **S81.** File-11 base, or wherever occasions are imported.

### W6. The normative relation: primitive or declared input; front-matter claims the body does not carry (XR3, XR5)

- **What is wrong.**
  - F11 L514's Declared inputs paragraph opens "Besides the two primitives", which excludes \(\mathcal N\). Yet L27 and L447 call \(\mathcal N\) "a declared input" (XR5).
  - L27 also says that a probability of truth, a merit function and a ranking of thinkers are taken as declared inputs "(Parts XI, XIV)". The body carries only worth and aesthetics (XR3).
  - So L37's rule, "the front matter states nothing the body does not state more exactly", is false of L27 (C10).
- **Where.**
  - File 10: L25, L458, L519. File 10 has no conflict, because it only "marks those places as empty".
  - File 11: L27, L37, L447, L510, L514.
- **Evidence.** Det 02: C7, C10, C65, XR3, XR5. Det 01, SILENT table: \(\mathcal N\) is not named in L514 (O12).
- **Severity.** Attribution-erratum.
- **Handling.** Erratum:
  - L514 adds "… and, for a claim of worth, the normative relation (primitive 2), under the same rule".
  - L27's second sentence either narrows to worth, or the other items are named in L514 as "not supplied; a claim that needs one is unsettled".
- **Gained.** O12's SILENT gets a stated rule, and the front matter becomes true.
- **Lost.** Nothing.
- **Risk.** O12 stays SILENT. O50 is touched if "ranking" is read as a weighting of credit (W14).
- **Tests.** O12.
- **Depends on.** W7, W14.
- **S81.** File-11 base only.

### W7. Declared inputs against indices and "everything else is derived"; Derivation 6's proof (XR6)

- **What is wrong.**
  - Boundary, continuity and the contract are "declared indices" (F11 L516) and also declared inputs (L514).
  - L33 and L512 say everything else is derived and do not mention the new category.
  - Derivation 6's claim now includes declared inputs (L586), but the dependence order it cites (L518) lists no input. It also omits Ownership (L419), ProducedBy (L433) and boundary and continuity (L465) (XR6).
- **Where.** File 10: L521–525 and L593–595. File 11: L33, L512–518 and L586–588.
- **Evidence.** Det 02: C66 (four tensions), C80, XR6.
- **Severity.** Coherence.
- **Handling.** Clarification:
  - One sentence: indices are the parameters every claim carries. Declared inputs are the values the semantics records and does not supply: the indices' values, plus O, P and their occasions, and what makes a restriction appropriate.
  - Add Ownership, ProducedBy and boundary to the dependence order.
  - Update Derivation 6's proof to match.
- **Gained.** Derivation 6's proof covers its claim.
- **Lost.** Nothing.
- **Risk.** None on cases.
- **Tests.** O37 and O49 (the well-founded order).
- **Depends on.** W3 (C67), W6.
- **S81.** File-11 base only.

### W8. Part 0's short form of attack (D) is unqualified

- **What is wrong.** F11 L63 lists "(D) the two provenances and the underdetermination of selected transports" with no qualification. This goes against the note's promise that every restatement carries the theorem's own qualification.
- **Where.** File 10: L74 is unqualified throughout, and is fixed by W2. File 11: L63.
- **Evidence.** Det 02: C22 and §5(i). R1 flags it; R2 calls it neutral.
- **Severity.** Attribution-erratum.
- **Handling.** Erratum: add "where the population admits a differing survivor".
- **Gained.** Consistency.
- **Lost.** Nothing.
- **Tests.** O48 (weak).
- **Depends on.** W2, W16.
- **S81.** File-11 base; on a file-10 base, through W2.

### W9. The "bell and tide" parenthesis names a case, not the document (XR4)

- **What is wrong.** F11 L275 ends "(the bell does not explain the tide)". The document contains no bell and no tide; the example is O2's content. The phrase reached the file-11 testers inside the theory text.
- **Where.** File 10: absent. File 11: L275.
- **Evidence.** Det 02: XR4 and C40.
- **Severity.** Attribution-erratum.
- **Handling.** Erratum. Drop the parenthesis, or replace it with an example stated inside the document. Keep the rule itself, C40: packaging a genuine dependence beside a restated answer does not repair the restatement.
- **Gained.** No steering toward O2.
- **Lost.** A vivid example.
- **Tests.** O2.
- **Depends on.** W20.
- **S81.** File-11 base only.

### W10. Derivation 10's glosses

- **What is wrong.**
  - (a) F11 L616 calls the structural failure "Derivation 3's qualification seen from the other side". That holds only if every \(H_0\)-survivor agrees at the occlusion, and Derivation 10 does not state that (XR7).
  - (b) Claude's own observation, which no reader has checked: F10 L627 and F11 L620 cite Derivation 2 for "the two persistence components are of one kind". Derivation 2 is about two candidates. Two components inside one candidate are of one kind by (K) directly.
- **Where.** File 10: L627. File 11: L616 and L620.
- **Evidence.** Det 02: XR7 and C81. Point (b) is Claude's reading.
- **Severity.** Attribution-erratum.
- **Handling.** Erratum. (a): drop the gloss, or add the premise. (b): cite (K) instead.
- **Gained.** Exact pointers.
- **Lost.** Nothing.
- **Tests.** None.
- **Depends on.** W19, for (b).
- **S81.** (a) file-11 base only; (b) independent.

### W11. "A table that genuinely encodes … is an account" claims too much

- **What is wrong.** F11 L271 and L528 assert that the encoding table satisfies (F1) "and it is an account", without checking (A), non-circular dependence or non-vacuity. Part XV then drops the encoding table from what could refute sufficiency.
- **Where.** File 10: L284 ("is not excluded") and L68, the lookup-table sentence of the S70 finding. File 11: L271 and L528 s3.
- **Evidence.** Det 02: C38 and C70. Story S57 and S70: the lookup-table finding.
- **Severity.** Coherence.
- **Handling.** Clarification. It "is not excluded by the table clause, and is an account when the other conditions hold". Keep S70's fix, under which the front matter defers to Part V.
- **Gained.**
  - No Account is granted without checking the other conditions.
  - The sufficiency attack stays honestly open to an encoding table that meets all four conditions and still explains nothing.
- **Lost.** File 11's crisp closing of the lookup-table question.
- **Risk.** O2 and O33 (low); O7.
- **Tests.** O2, O33, O7. N17: the full electron calculation is "thin". Does a complete derivation count as an Account? N16.
- **Depends on.** W33, W44.
- **S81.** File-11 base only.

### W12. Ownership needs a declared boundary that many cases lack

- **What is wrong.** File 11 grounds ownership in a declared boundary (L419, L465, L514). O3, O14, O17 and O21, and weakly O18 and O31, assert "her own", "his own effort" or "hers" with no boundary declared. A strict reader marks them SILENT; the determination readers supplied the evident boundary.
- **Where.**
  - File 10: "owned" is undefined (L414, L476, L488, L493) and read in its ordinary sense.
  - File 11: L419, L465, L467, L514.
- **Evidence.**
  - Raw 01a, genuinely hard cases: "O3, O14, O17, O21 (file 11): … none of these cases declares one … a strict reader could mark 'own' SILENT".
  - Det 01 O3 note. Det 02 §2, point 3; C55; C66.
- **Severity.** Verdict-changing (risk). Six AGREE rows could become SILENT.
- **Handling.** Choose one:
  - (a) Clarification, as a general rule stated in advance: "a boundary may be stated by the situation: where one agent acts and no outside work enters the history, the agent's own processes are the declared boundary".
  - (b) Leave the text, and say that the evident agent is the input given.
  Recommended: (a), then test it.
- **Gained.** Six AGREEs rest on text.
- **Lost.**
  - A default input, in tension with L465 ("declared before the attribution, not chosen after it") and with L514.
  - The rule must not make the casing the boundary: O51 must stay AGREE, because its declared boundary excludes the module.
- **Tests.** O3, O14, O17, O18, O21, O31, O51, O41, O30. N15, N21, N11, N13.
- **Depends on.** W4 (the same default-input question), W6, W7, W13.
- **S81.** File-11 base only. It also arrives on a file-10 base if W3 imports L419.

### W13. The two halves of the Ownership sentence assign different things

- **What is wrong.** F11 L419 says both "remains an outside contribution however it is executed inside" and "a process that runs inside the boundary is the system's own today whoever wrote it". Readers took these as a tension, which produced Atria's split readings on O30 and O40. The first half is about credit for content; the second is about ownership of a process.
- **Where.** File 10: absent. File 11: L419 and L465.
- **Evidence.** Trial §3a A4 (INVALID as a hole, with the drafting note "one clause saying that the two halves assign different things … would stop the misreading"). Trial §2: Atria O30, P x.
- **Severity.** Coherence.
- **Handling.** Clarification: one clause.
- **Gained.** Fewer misreadings.
- **Lost.** Nothing.
- **Risk.** None.
- **Tests.** O30, O40, O41, O50, O21. N13, N11.
- **Depends on.** W12.
- **S81.** File-11 base only.

### W14. "Mostly": neither file supplies a weighting of credit

- **What is wrong.**
  - O50's "the inquiry was mostly the expert's" needs a weighting that both files withhold, and F11 L514 does not name one.
  - O21 and O27 reach "mostly" only by reading it as where the single originative act lies.
- **Where.** File 10: L25 and L424–430 (Origin). File 11: L27 s3, L433 s4 and L514.
- **Evidence.**
  - Det 01: the O21 note, the O50 ruling and the SILENT table.
  - Trial: O50 is partial or a departure for all three readers.
  - S72 Stage 2, file 05: gauge rows I96 and H90.
  - Story S65 and S70: clause I64 says "mostly" needs a stated reason.
- **Severity.** Coherence (verdict risk).
- **Handling.** Choose one:
  - (a) Clarification: locating the single originative act is derivable per content from (G); weighting several originative acts is not supplied, and such a claim is unsettled.
  - (b) Add a weighting of contributions to the declared inputs.
  Recommended: (a).
- **Gained.** O50's SILENT gets its rule, and the AGREEs on O21 and O27 get their reason.
- **Lost.** Under (b), O21 and O27 could fall to SILENT, since readers could treat "mostly" as a weighting.
- **Risk.** O21, O27, O40, O20, O26, O39.
- **Tests.** O21, O27, O40, O50, O20, O26, O39, O32. N11. N14 is set aside, but both of its authors said "no meaningful share" exists, which is the theory's own refusal.
- **Depends on.** W6, W48.
- **S81.** Both, differently.

### W15. Part XV: a case that turns on a missing declared input is not a refutation

- **What is missing.** Neither file says that a case whose verdict turns on an unstated declared input is a SILENT, not a defeat. File 12 says it for its contrasts (12:554).
- **Where.** File 10: Part XV, L531–545. File 11: Part XV, L524–538.
- **Evidence.** 12:554. Det 01 SILENT table (O1, O12, O35, O50).
- **Severity.** Coherence.
- **Handling.** Clarification. Add one sentence to Part XV, restricted to the inputs Part XIV lists.
- **Gained.** The SILENT rows are not read as refutations.
- **Lost.** It could be used to shelter the theory by calling any deciding matter an "input". Restricting it to Part XIV's list prevents that.
- **Tests.** O1, O12, O35, O50.
- **Depends on.** W4, W6, W7.
- **S81.** Both; it is needed more with file 11's L514.

---

## Group 2. Derivation 3 and the population

### W16. Derivation 3 in file 11 has almost no refutable content

- **What is wrong.** Read under the claim's own gloss ("survival on H does not distinguish t from t′ there"), Part XV's first (D) limb is unsatisfiable: "a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there". The only way out is to read "determined by its history" through \(\mu\). The theorem is close to analytic, so its exposure in Part XV is nominal.
- **Where.**
  - File 10: L74, L539, L567–573. These are unconditional and refutable, and O48 refutes them.
  - File 11: L534, L562–566.
- **Evidence.** Det 02 §5(i): both readers call it near-definitional, R1 finds it unsatisfiable, and the reconciler confirms that with the \(\mu\) exception. S72 Stage 2, file 05: the card "establishes a conditional survivor comparison at a specified pair".
- **Severity.** Coherence (claim-level, exposed in Part XV).
- **Handling.** Choose one:
  - Clarification: say openly that Derivation 3 is a conditional bookkeeping result, and move the refutable load to Derivation 4 (surprise).
  - Restatement: adopt the framing of file 12's Derivation 4 (\(\mathcal T\) is what the physics and the stated construction admit), with the refuter "a value fixed at an unseen pair by H alone, through \(\mu\), where \(\mathcal T\) admits a differing survivor".
- **Gained.** The defeat list names something that could happen.
- **Lost.** Re-widening the claim could return O48 to DISAGREE. The text gets longer.
- **Tests.** O48, O24, O11. N5 (both readings of the rule survive the home history), N18, N9.
- **Depends on.** W2, W17, W18.
- **S81.** Both, differently.

### W17. What "surviving on H" means

- **What is wrong.** "Surviving on H" can mean a member of \(\mathcal T\) that survived (the Sel definition), or any transport that meets fidelity on H. The note's claim that file 10's proof "already assumed the qualification" holds only on the first reading, and file 10 leaves both open.
- **Where.** File 10: L210 and L569–571. File 11: L197 and L562–564.
- **Evidence.** Det 02 §5(i), "My addition".
- **Severity.** Coherence.
- **Handling.** Clarification in Part IV: "survives on H" means a member of \(\mathcal T\) that satisfies the survival condition.
- **Gained.** The note's claim becomes true by definition.
- **Lost.** File 10's other reading, an unconditional theorem about admissible alternatives, is dropped openly.
- **Tests.** O48, O24.
- **Depends on.** W2.
- **S81.** Independent.

### W18. Whose knowledge a population's fixing is (source point M3)

- **What is missing.** File 11 lets the population fix untested values (L197, L473, L566) but gives the population no provenance of its own. If the population was constructed or declared, for example a movement language a designer wrote, then its fidelity on unseen changes is inherited from that construction (D pp.159–161).
- **Where.** File 10: L210 and L482. File 11: L197, L473 and L566.
- **Evidence.** Verify M3, the fifth of "the observations most worth acting on".
- **Severity.** Coherence.
- **Handling.** Clarification or new claim: "where \(\mathcal T\) is fixed by a stated construction, what \(\mathcal T\) fixes at an unseen change is owed to that construction and carries its provenance; selection on H contributes only what H decides".
- **Gained.**
  - The theory can say whose knowledge makes the evolved robot walk.
  - The population qualification is not a back door for crediting selection.
- **Lost.**
  - A new claim that complicates Sel, whose history represents nothing.
  - No adopted case tests it yet: N14 is set aside.
- **Risk.** O48's verdict is unaffected.
- **Tests.** O48, O11. N14 (only after a rewrite), N11, N5, N9.
- **Depends on.** W2, W16.
- **S81.** Independent in substance; where it goes depends on the base.

---

## Group 3. Proof, type and definition holes (S81 trial and determination)

### W19. Derivation 2's proof does not pair the two candidates' components (Mimo M6)

- **What is wrong.**
  - The claim: two candidates that both satisfy (F1), (F2) and (A) "are one account … their components are pairwise of one kind".
  - The proof: "Immediate from Derivation 1 and (A)". But Derivation 1 pairs each component only with its own anchor. Two candidates with different \(\lambda\), or different numbers of components, are paired by nothing shown.
  - Part XV lists Derivations 1–3 as refutable. This is therefore a live gap in the theory's own defeat list.
- **Where.**
  - File 10: L559–565, L543, and D10's use of it at L627.
  - File 11: L552–558, L538, L620.
- **Evidence.** Trial M6 (VALID). Its §4 calls M6 and M3 "the most serious".
- **Severity.** Coherence (a proof gap exposed in Part XV).
- **Handling.** Either:
  - restate the claim for candidates whose anchor maps assign the same subnetworks of D up to a bijection of components; or
  - supply the missing step (components anchored to one subnetwork are of one kind, by Derivation 1 and transitivity) and state what holds when the anchors differ: the answer profiles coincide, and the components need not pair.
- **Gained.** The proof matches the claim.
- **Lost.**
  - The slogan "indistinguishable is identical" narrows.
  - The Consequence is weakened as an argument against claims that two candidates "really differ" (grievance 2; attack C).
- **Risk.** O24 (Derivation 2 is not triggered there, since the arrangements differ at a reachable setting), O10, O45, O46.
- **Tests.** O24, O10, O45, O46, O22. N25 (the dog and the turtle: same answers, one account?), N17 (two answers to one question, or two questions?), N23.
- **Depends on.** W10(b). W21 depends on it.
- **S81.** Independent.

### W20. Non-circular dependence has a target edit act on the explanation's commitments (Mimo M3)

- **What is wrong.**
  - The contract \(C\subseteq A\times B\) is made of D's edits, and \(\Gamma\) is a set of commitments in E.
  - The clause "There exists \((a,b)\in C\) that removes or replaces a nonempty block of \(\Gamma\) while preserving the other boundary conditions" has a D-edit act on E's commitments, with no \(\tau\).
  - It also treats blocks of \(\Gamma\) as boundary conditions.
  - Its two halves can pull apart on O2 (det 02, C40).
- **Where.** File 10: L270, with \(\Gamma\) at L246 and Part VI at L304. File 11: L257, L233 and L289.
- **Evidence.** Trial M3 (VALID; it decides O2, O5 and O33). Det 02 C40.
- **Severity.** Coherence. It is a type error in a defining clause of Account, with a verdict risk.
- **Handling.** Clarification, retyping the clause:
  - The witnessing change is an organization edit \(v\in\mathcal V\) on E (Part VI) that removes or replaces a nonempty block of \(\Gamma\) "with the named background fixed", and it is judged by the answer profile on C.
  - Alternatively, link the target-side contrast in C to the E-side edit through \(\tau\).
  - Keep F11 L275: packaging does not repair a restatement.
- **Gained.** A well-typed condition, tied to Part VI.
- **Lost.** The "admitted contrast … may concern a counterfactual law" reading (00:210) must not be lost, because the skew-symmetric construction removes rules.
- **Risk.** O2 (the bell block), O5, O33, O7 (sweeping the salt), O4, O36, and Part VII's skew-symmetric construction.
- **Tests.** O2, O4, O5, O7, O33, O36. N1 (strike the sun-god sentence: the tilt block witnesses and the god does nothing), N3, N16, N25.
- **Depends on.** W29, W39. W9 depends on it.
- **S81.** Independent.

### W21. \(\equiv_\ell\) in (N) is undefined (Mimo M4)

- **What is wrong.** Newness is "\(\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c\)", and \(\equiv_\ell\) is defined nowhere. (G) and (EK) rest on it.
- **Where.** File 10: L418–421. File 11: L405–408.
- **Evidence.** Trial M4 (VALID). Mimo raised it on O3, O11, O18, O27 and O31. 00:746 has a gloss: "The equivalence is structural at the stated grain, not string equality or similarity."
- **Severity.** Coherence.
- **Handling.** Clarification. Restore 00:746, and define \(d\equiv_\ell c\) as: transports between d and c at grain \(\ell\) are faithful in both directions on c's contract.
- **Gained.** New and Origin become checkable.
- **Lost.** Newness is tied to Derivation 2 (W19).
- **Risk.** O11 (Wednesday's reuse), O15, O18, O31, O3, O27.
- **Tests.** O3, O11, O18, O27, O31. N4, N15 (not new to the world, new to her), N10, N21.
- **Depends on.** W19.
- **S81.** Independent.

### W22. \(\mathcal E_c\) is undefined in (K1), and \(p\) is unused (Mimo M2, M1)

- **What is wrong.**
  - \(\mathcal E_c\) occurs once and is never defined.
  - Neither \(p\) nor \(z\) appears on the right-hand side of (K1).
  - M1 (JUDGEMENT): "represents how it bears" sits uneasily with "can exist when (K1) fails".
- **Where.** File 10: L386–392. File 11: L373–379.
- **Evidence.** Trial M2 (VALID) and M1 (JUDGEMENT). 00:620: "\(\mathcal E_c\) is the criticism's interpreted structural account".
- **Severity.** Coherence.
- **Handling.** Erratum and clarification:
  - Restore 00:620.
  - Say that \(p_\delta\) is "the question whether z has \(\delta\) in respect of p".
  - Change "represents how it bears" to "represents its alleged connection".
- **Gained.** (K1) is well typed.
- **Lost.** Nothing.
- **Tests.** No case turns on (K1).
- **Depends on.** Nothing.
- **S81.** Independent.

### W23. \(\Delta\), Result(\(\Delta\)) and ProducesVia are undefined

- **What is wrong.**
  - \(\Delta\) is never typed.
  - Result and ProducesVia each occur once, undefined.
  - File 10 also leaves ProducedBy undefined. File 11 defines it at L433.
- **Where.** File 10: L438–456. File 11: L427–445.
- **Evidence.**
  - Trial §3b, Mimo on O13 (VALID).
  - 00:839: ProducesVia "requires the construction account of the repair to contain the relevant binding of c on its active route".
  - 00:800: ProducedBy is a construction account; "A transport supplies the interpretation of o and r across changed representations".
- **Severity.** Coherence.
- **Handling.** Clarification:
  - Type \(\Delta\) as a contribution: a subhistory with its content changes.
  - Define Result(\(\Delta\)) as the contents at \(\xi'\) that \(\Delta\) prepared.
  - Restore 00:839, and consider 00:800's transport clause.
- **Gained.** (P) and (EK) can be evaluated.
- **Lost.** Nothing.
- **Risk.** O13 must stay: Ana's account produced nothing.
- **Tests.** O13, O20, O32, O39. N10, N19.
- **Depends on.** W48.
- **S81.** Both, differently.

### W24. \(S_a\), \(T_a\) and "generator" are undefined (Atria A3 = Mimo M7)

- **Where.** File 10: L366. File 11: L351.
- **Evidence.** Trial A3 and M7. 00:518: "Suppose a target process \(S_a\) and a represented process \(T_a\)".
- **Severity.** Attribution-erratum.
- **Handling.** Erratum: restore 00:518's sentence.
- **Gained.** A readable theorem.
- **Lost.** Nothing.
- **Tests.** None.
- **S81.** Independent.

### W25. Admit, Cap\(^{q,r}\), the grades \(q,r\), Poss and Enable are undefined (Mimo M8)

- **What is wrong.**
  - Admit\(^{q,r}_\Theta\), Cap\(^{q,r}_\Omega\) and the grades \(q,r\) are defined nowhere.
  - Cap\(^{q,r}\) is never defined from Can.
  - "Enable" in (U1) and (U2) is undefined, in file 00 too (00:1113, 1124).
- **Where.** File 10: L480 and L501–504. File 11: L471 and L492–495.
- **Evidence.** Trial M8 (VALID in part) and §4, "found by no reader". 00:1015–1031 defines Admit, Cap and Poss.
- **Severity.** Coherence.
- **Handling.**
  - Erratum: restore 00:1015–1031.
  - New definition: Enable, for example "\(\chi\) is an admitted, non-question-begging enabling condition", in the Barriers paragraph's terms.
- **Gained.** Part XII and Part XIII become readable.
- **Lost.** Nothing.
- **Tests.** N24 (UU fails over two sealed sorts of matter).
- **S81.** Independent.

### W26. Tag (I3) is missing (Atria A2)

- **What is wrong.** The tags run (I1), (I2), (I4).
- **Where.** File 10: L342. File 11: L327.
- **Evidence.** Trial A2 (VALID). 00:440–447 has (I3), approximate identification.
- **Severity.** Attribution-erratum.
- **Handling.** Erratum. Either restore 00's (I3), which adds a small result, or renumber (I4) as (I3).
- **Gained.** Tidy numbering.
- **Lost.** Nothing.
- **Tests.** None.
- **S81.** Independent.

### W27. Attack labels collide with equation tags

- **What is wrong.** The attack labels (A), (B), (D) and (E) reuse the equation tags (A), (B), (D) and (E).
- **Where.** File 10: L68–76 and L352. File 11: L63, L337 and L528–536.
- **Evidence.** Trial §3a, A1 note ("A stronger collision exists …"), and §4. Det 02 XR8 note.
- **Severity.** Attribution-erratum.
- **Handling.** Erratum. Relabel the attacks, for example "Attack 1" to "Attack 5", and update every pointer (F11 L337, L63).
- **Gained.** No ambiguous references.
- **Lost.** Pointers in the record ("attack (B)") no longer match.
- **Tests.** None.
- **S81.** Independent.

### W28. "Route" in Part VI against "active route" in Part IX (J-4)

- **What is wrong.** Part VI's "route" is undefined and is read by example. Part IX defines only the "active route", in a history. Two readers used the difference to split cases that the fixed verdict settles (DeepSeek on O45; Mimo on O19).
- **Where.** File 10: L324 and L384. File 11: L309 and L371.
- **Evidence.** Trial §3b, J-4 (JUDGEMENT), and §2 on DeepSeek O45.
- **Severity.** Coherence.
- **Handling.** Clarification:
  - A Part VI route is a support of the candidate.
  - A Part IX active route is a subnetwork of actual occurrences.
  - The two meet in ProducedBy.
- **Gained.** Fewer mistaken splits.
- **Lost.** Nothing.
- **Tests.** O45, O19, O39, O52, O25, O20.
- **Depends on.** W48.
- **S81.** Both, differently. The F11 L309 sentence is in file 11 only.

### W29. No rule says when a proxy measure counts as the target's answer (O4)

- **What is wrong.** No text says when a measure of the outcome, taken in another carrier, is "the target's answer" at the declared grain. O4's AGREE holds on L270/L257 and L153, but the coarse-dependence reading (dilution; F11 L279) is also available.
- **Where.** File 10: L141, L168, L270. File 11: L129, L153, L257, L279.
- **Evidence.**
  - Raw 01a, O4 "STRONGEST CONTRARY READING", and its hard-case list: "the text never says when a proxy measure counts as 'the target's answer'".
  - Det 01 O4 (confidence medium).
  - Story S55 and S57: O4 was placed by the Part III distinction.
- **Severity.** Coherence.
- **Handling.** Clarification in non-circular dependence: "a component whose value is defined as the outcome in question, observed through another carrier, is the target's answer at the declared grain; its measurement signature (Part II) shows it". A coarse dependence on something other than the measured outcome, such as the salt, is not caught.
- **Gained.** O4 rests on a sentence and is separated from O7.
- **Lost.** It might catch honest indices that are not defined by the outcome, so the wording must be tight.
- **Risk.** O7 must stay AGREE; O6 and O9.
- **Tests.** O4, O6, O7, O9. N3 (the yearly winter is written into the bargain), N16 (answer A restates what was seen), N2, N25.
- **Depends on.** W20, W39.
- **S81.** Independent.

### W30. A set-point difference is a state, not a kind (O10)

- **What is wrong.** Two readers in the S81 trial got O10's kind mechanics wrong:
  - Atria: a set-point edit "separates" the two thermostats.
  - Mimo: removing edits "separates" them.
  File 11 L121 already states that coarser contracts identify more components.
- **Where.** File 10: L136. File 11: L121.
- **Evidence.** Trial §2: Atria O10, P x; Mimo O10, P x.
- **Severity.** Coherence (low).
- **Handling.** Clarification: whether a difference is a state (a port value) or part of a component's relation is fixed by how the organization is written. A difference in a port value leaves the signatures equal, and an edit that acts alike on both components cannot separate them.
- **Gained.** Fewer misreadings.
- **Lost.** Nothing.
- **Risk.** None; O10 stays AGREE.
- **Tests.** O10, O22.
- **S81.** Independent.

### W31. (T2) has no initial-error term (S78 item 10; R2 J)

- **What is wrong.** The bound "\(e_n\le\varepsilon\sum_{k<n}L^k\)" holds only from matching initial states. With an initial discrepancy \(e_0>0\), the correct bound is \(e_n\le L^n e_0+\varepsilon\sum_{k<n}L^k\). The word "initial" occurs in neither file. Part XV lists (T2) among the results that a counterexample refutes "under their stated assumptions", and those assumptions omit \(e_0=0\).
- **Where.** File 10: L376 and L543. File 11: L361 and L538.
- **Evidence.**
  - S78 item 10, and its last correction to S75.
  - S72 Stage 2, file 01 L494 (R2 J quoted: "the accumulated-error bound without an initial-error term presupposes matching initial states").
  - S72 Stage 2, file 05: "not resolved by this population fix".
  - Story S79: the seeded round planted its second error in (T2) because no case touches it.
- **Severity.** Coherence. It is a mathematical defect that Part XV exposes.
- **Handling.** Erratum: add "from matching initial states (\(e_0=0\)); with initial discrepancy \(e_0\), \(e_n\le L^n e_0+\varepsilon\sum_{k<n}L^k\)".
- **Gained.** The one listed result with a literal counterexample is repaired.
- **Lost.** Nothing.
- **Risk.** No O-case.
- **Tests.** No O-case. N20 (keeping count with string).
- **Depends on.** Nothing. W42 depends on it.
- **S81.** Independent. The S79 seeded file is a copy of file 10, so this change must not be fed into S79's sealed comparison.

---

## Group 4. Points from the verified source observations

### W32. A stated limit that nothing in the account explains (source point 6; gauge row A; O1)

- **What is missing.** Non-vacuity asks only that an exclusion be stated. File 11 records appropriateness as a declared input that it does not certify (L161, L514). Both books treat an unexplained limit as a defect:
  - D pp.27–28 and 118–119;
  - M p.24, where it is "a problem", not a disqualification.
  - The owner's skill word-list credits file 10 with "hard-to-vary over scope", which file 10 does not contain (M11).
  - O1's "the series as a whole is a retreat" is SILENT under both files.
- **Where.** File 10: L41, L272, L378, L456, L330. File 11: L45, L161, L259, L514, L315.
- **Evidence.**
  - Verify obs 6 (PARTLY CONFIRMED; first of "most worth acting on").
  - S72 Stage 2, file 05: row A is homeless.
  - Det 01, O1 and O5. Trial: O1 is partial for all three readers.
  - Story S28–S29: the swap clause A-prime failed because "a swap that works shows a limit is loose, not that it was fitted to failures; and the clause would refuse honest limits that simply say what is being asked about".
- **Severity.** Verdict-changing: O1 would move from SILENT to AGREE if this works.
- **Handling.**
  - (b) Clarification: (E) on a scoped contract does not certify the limit.
  - Optionally, (c) a measure in Part VI, never a condition: variants of a contract's limits form a variation family. A limit whose variants leave every job of the account intact is loose, and a series of loose limits adopted after failures is a retreat on the record. A limit that only names what is asked about is exempt.
- **Gained.** O1 becomes statable, and the books, the skill and the theory agree.
- **Lost.**
  - Story S29's failure must not repeat.
  - N7 must stay "both explain": Maya's limits are unexplained and she still explains the rising. So "loose" must not mean "explains nothing".
- **Risk.** O5, O8 and O33 must stay AGREE.
- **Tests.** O1, O5, O8, O33. N6 (Iras against Leon). N7 is the guard.
- **Depends on.** W6 and W7 (is appropriateness an input, or partly derived?), W15, W33.
- **S81.** Both, differently. File 11 already abstains in words.

### W33. Idle parts: (E) accepts them; hard-to-vary is a lemma (source point 2, M7)

- **What is missing.** D p.25 calls superfluous features bad. (E) accepts an idle commitment (for example one anchored to a deleted subnetwork, whose relation is full). Part VI reports it only as non-critical. The text never says this plainly.
- **Where.** File 10: L260–280 and L302–330. File 11: L247–267 and L287–315.
- **Evidence.**
  - Verify obs 2 (PARTLY CONFIRMED; second of "most worth acting on") and M7.
  - 00:356–384 and 00:1298–1302: file 00 restricted the lemma on purpose.
  - 00:37: no GoodExplanation primitive.
- **Severity.** Coherence.
- **Handling.**
  - Clarification: "(E) is fidelity; an idle commitment passes (E) and (B) reports it as non-critical; hard-to-vary (Part VI) is a separate, non-grading measure".
  - Leave hard-to-vary alone as a condition, for the stated reasons: it would bring back grading, and "counting jobs is not a warrant".
- **Gained.** N1's verdict ("Tomas explains; the sun-god sentence is no part of it") matches the split between (E) and (B) exactly.
- **Lost.** Nothing, as long as it is not made a condition.
- **Risk.** None under the clarification. A condition would put O36, O45 and O47 at risk.
- **Tests.** O36, O45, O47. N1, N25, N2.
- **Depends on.** W34.
- **S81.** Independent.

### W34. "Reach" is used once and never defined (source point 5)

- **Where.** File 10: L330, the only use. File 11: L315. File 00's definition at 00:383 was dropped in file 10.
- **Evidence.** Verify obs 5, fourth of "most worth acting on".
- **Severity.** Coherence.
- **Handling.** Clarification. Either restore 00:383 ("Reach occurs when an unchanged organizational core participates in an account of another question through a stated anchor and additional background"), or define reach from Part VI as the set of jobs f with Account(E, f), fixed by E and the world.
- **Gained.** The lemma's key word has a meaning, and D p.29 ("determined by the content") becomes statable.
- **Lost.** Nothing. No primitive is added.
- **Tests.** N4 (the idea already accounted for the midnight sun, though nobody had explained it: reach against Deploy), N5 (a rule's limited reach), N17 (weak).
- **S81.** Independent.

### W35. Surprise is narrower than Deutsch's "problem"; "recognized difficulty" is undefined (source point 13, M2; file 12)

- **What is wrong.**
  - Surprise exists only for selected transports (F10 L230–238; Derivation 4), so the refutation of a constructed theory is not surprise.
  - Episodes' "recognized difficulty" (F10 L432) is undefined.
  - File 12 widened surprise to any transport checked on a tested history (12:215–225; its Derivation 5 at 12:594–600), with "re-tuning" and "rebuilding" as the two responses.
- **Where.** File 10: L230–240, L432, L575–581, L621. File 11: L217–227, L421, L568–574, L614.
- **Evidence.**
  - Verify obs 13 (PARTLY CONFIRMED; third of "most worth acting on") and M2.
  - 00:754 (an Attempt addresses "a recognized difficulty"), 00:785 ("A newly discovered problem may supply a new obligation"), 00:804.
- **Severity.** Coherence.
- **Handling.** Choose one; the two are mutually exclusive:
  - **(b)** Keep "surprise" as a term for selected transports and say so. Define "recognized difficulty" or "problem" as a represented failure of a claimed obligation, or a represented conflict between a claimed and a protected obligation (Repair's O and P).
  - **(c)** Adopt file 12's tested-history surprise, and keep the selection and construction responses.
  Recommended: (b).
- **Gained.**
  - (b): Deutsch's "problem" gets a home in Repair, including a problem that arises purely in theory (D p.17).
  - (c): refuting a constructed theory counts as surprise.
- **Lost.**
  - (b): "surprise" stays narrower than ordinary use. O3 says Nadia is "often surprised".
  - (c): Derivation 4's "learning versus creating" and Derivation 10 must be rewritten.
- **Risk.** O3's wording; O12's "need recognised only afterwards".
- **Tests.** O3, O27, O12. N18 (Rhea's worked-out theory is contradicted), N19 (a problem before anyone read the chapter).
- **Depends on.** W5, W23.
- **S81.** Independent.

### W36. "Explanation" and "account" are each used in two senses (source point 4; O15)

- **What is wrong.**
  - Part I says "What cannot count as explanation is an error in the very dependence …". Deutsch counts a false myth as an explanation (D p.19); the theory's word for his sense is "explanatory candidate".
  - "Account" is used both for Account (E) and in its ordinary sense. O15's "his account" was a hard case.
- **Where.** File 10: L86, L246, L226, L412. File 11: L71, L233, L213, L399.
- **Evidence.** Verify obs 4 (CONFIRMED as a difference of terms). Raw 01c O15 (hard case). Det 01 O15 (confidence medium-low).
- **Severity.** Coherence.
- **Handling.** Clarification:
  - One sentence in Part I: a candidate may be false and still be an explanation in the ordinary sense; Account (E) is fidelity on a contract; "good" in Deutsch's sense belongs to Part VI.
  - Mark the technical term, for example with a capital A.
- **Gained.** Matches N3's verdict ("an explanation of winter, but only in form … a false one").
- **Lost.** Part I's Fallibility sentence must be reworded carefully.
- **Tests.** O15. N3, N2.
- **S81.** Independent.

### W37. File 11 dropped "blind" from Part 0 (source point 9)

- **What is wrong.** F10 L13 says "blind variation and survival". F11 L15 says "variation and survival on a history of encountered changes". The body keeps the blindness at F11 L197. D p.78 uses "selection" for criticism too, so file 11's wording makes the clash of vocabulary worse.
- **Where.** File 10: L13. File 11: L15.
- **Evidence.** Verify obs 9 (CONFIRMED: "File 11 made the vocabulary clash worse").
- **Severity.** Attribution-erratum.
- **Handling.** Erratum: restore "blind". Clarification: selection here is selection without a represented target, unlike Deutsch's wider usage.
- **Gained.** D p.78 is not read as a Part XV defeater.
- **Lost.** Nothing.
- **Tests.** O11 (Monday's blind fitting). N11 (Jana's teacher chooses among her drafts; Kasia criticizes her own).
- **S81.** File-11 base only.

### W38. Sources and lineage are not named (source points 1, 3, 10)

- **What is missing.**
  - No theory file names Deutsch or Marletto.
  - Part XII's wording is constructor theory, from the 2013 *Synthese* paper cited at 00:910 [R2].
  - Derivation 9, declared provenance, relay and reason use have close parallels in D chapters 7 and 16 that are not attributed.
  - File 00's header links source files that are missing.
- **Where.** Front matter. Part XII: F10 L464 / F11 L453. Derivation 9: F10 L613 / F11 L606. Build: F10 L414 / F11 L401. Reason use: F10 L394 / F11 L381.
- **Evidence.** Verify obs 1 (PARTLY CONFIRMED), obs 3 (CONFIRMED) and obs 10 (CONFIRMED). Decision S19.
- **Severity.** Attribution-erratum.
- **Handling.** An attribution note beside the frozen text, or in revision 2's front matter. It should also list the known departures: source points 4, 6, 9 and 13, and the rejection of "every acquisition is creation" (00:1304–1306 against D pp.94 and 403–406).
- **Gained.** Traceability, and honesty about where the theory departs from the books.
- **Lost.** Readers may hold the theory to the books.
- **Risk.** No verdict risk.
- **Tests.** None directly. N12 and N13 are positive controls for the text that has these parallels.
- **S81.** Independent.

### W39. Same-form regress: identity of the answer is structural at the grain (source point 12)

- **What is missing.** Files 10 and 11 keep "at the declared grain" but dropped 00:210's "Identity of that assertion is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical truths".
- **Where.** File 10: L270. File 11: L257.
- **Evidence.** Verify obs 12: REFUTED as a gap, and at most NOT ESTABLISHED for same-form regress.
- **Severity.** Coherence.
- **Handling.**
  - Clarification: restore 00:210's sentence.
  - Leave out any "no unexplained starting point" condition, which would contradict D p.174 and M p.54.
- **Gained.** The endless turtles of N25 are caught in words, and the rule supports W29.
- **Lost.** Nothing. The second half of the sentence protects the skew-symmetric construction.
- **Tests.** O2, O4. N25, N3.
- **Depends on.** W20, W29.
- **S81.** Independent.

### W40. An eliminative explanation must also explain the appearance (M6; source point 15)

- **What is missing.** D p.154: to deny that a thing exists, one must also explain why it seems to. Part VII's treatment of explanations that remove structure asks nothing of the kind.
- **Where.** File 10: L350–352, L70, L535. File 11: L335–337, L530.
- **Evidence.** Verify M6 and obs 15.
- **Severity.** Coherence (attack B).
- **Handling.** Clarification. Denying a structure that appears answers "is there X?". "Why does X appear?" is a separate question with its own contract, and a bare denial is not an Account of it. This is not a new condition on the first question.
- **Gained.** A sharper attack B, and N22 becomes statable.
- **Lost.** Nothing substantive.
- **Tests.** N22 (Wren against Yuri), N8, N25.
- **Depends on.** W49.
- **S81.** Independent.

### W41. Inexplicit representation (source point 14; 00:855–861)

- **What is missing.** Files 10 and 11 dropped file 00's paragraph "Inexplicit representation is not absent representation". Build's witness must identify "the bindings constructed", which is hard for tacit construction.
- **Where.** Build: F10 L414 / F11 L401. (R): F10 L218–228 / F11 L205–215.
- **Evidence.** Verify obs 14: "inexplicit" is CONFIRMED missing.
- **Severity.** Coherence.
- **Handling.** Clarification. Restore 00:855–861, and say that a witness may identify bindings by their use.
- **Gained.** N21 (a tacit rule she formed herself) can be reached.
- **Lost.** The witness is harder to check. Relay must stay excluded: N13's parrot must not be credited by use alone.
- **Risk.** O14 (the narrow skill).
- **Tests.** N21, N12, N13. O14.
- **S81.** Independent.

### W42. Error-correction as a derived lemma (source point 14)

- **What is missing.** D p.140: without error-correction, all information processing is bounded. The theory has the accumulation half, (T2), but nothing about correction.
- **Where.** File 10: L376, L490–494, L480. File 11: L361, L481–485, L471.
- **Evidence.** Verify obs 14 (error-correction: a derived lemma, low risk).
- **Severity.** Coherence.
- **Handling.** New claim, a derived lemma: unbounded composition at a fixed accuracy grade needs a correction step. It would follow from (T2), (RC) and CT3/CT4. Defer it until W31 is fixed and N20 has been run.
- **Gained.** D p.140 becomes statable, and N20 derivable.
- **Lost.** A new proof obligation, and one more entry in Part XV's list of mathematical results.
- **Tests.** N20.
- **Depends on.** W31.
- **S81.** Independent.

### W43. Knowledge as self-preserving information (source point 8)

- **What is missing.** The books' notion of knowledge as information that keeps itself instantiated (M p.13, p.155) has no home. File 00's conditional bridge was dropped.
- **Where.** (EK): F10 L446–456 / F11 L435–445. Derivation 6: F10 L591–597 / F11 L584–590. 00:995–1011 and 00:1330–1334.
- **Evidence.** Verify obs 8 (CONFIRMED).
- **Severity.** Coherence.
- **Handling.** Leave it out, and state the reason in the front matter: knowledge in the constructor-theoretic sense is a physical attribution outside this class. The alternative is to restore 00's conditional bridge as a derived relation of the physical module.
- **Gained.** No scope creep, and Derivation 6 ("no 'is knowledge' predicate") stays intact.
- **Lost.** N9's "what holds it" and N10's "the knowledge no longer exists" have no predicate. N9 may still be reachable through Sel and (R) at population grain.
- **Tests.** N9, N10.
- **S81.** Independent.

### W44. Level of explanation (source point 11)

- **What is missing.** The theory can say that an answer at another grain answers a different question. It cannot say which grain a question should have.
- **Where.** File 10: L168 and L523. File 11: L153, L516 and L279.
- **Evidence.** Verify obs 11 (PARTLY CONFIRMED).
- **Severity.** Coherence.
- **Handling.** Clarification (a note). Optionally, a derived notion: a quasi-autonomous level exists when an Account whose anchors all lie at grain \(\ell\) exists. This must never become a predicate on grain.
- **Gained.** N16 and N17 become readable.
- **Lost.** Nothing in the text. But N17 ("A explains only thinly") may expose that the theory counts a full fine-grain derivation as a full account.
- **Tests.** N16, N17. O7.
- **Depends on.** W11.
- **S81.** Independent.

### W45. Interoperability and substrate independence (M4)

- **What is missing.** Part I states "Any carrier may bear an organization" as a commitment. Marletto treats interoperability as a contingent law of physics (M p.95), and file 00 cited it (00:912 [R3]).
- **Where.** File 10: L92 and L496. File 11: L77 and L487.
- **Evidence.** Verify M4.
- **Severity.** Coherence.
- **Handling.** Clarification: substrate independence holds relative to the adopted physics' interoperability. A physics without it has barriers in Part XIII's sense.
- **Gained.** N24 can be reached.
- **Lost.** Nothing.
- **Tests.** N24.
- **S81.** Independent.

---

## Group 5. What file 12 changes that a revision 2 might adopt

File 12 is a draft under no round (NOT-IN-BUNDLE; story S77). It removes provenance by the owner's instruction (decision S9). That removal applies to file 12 only, so a revision 2 of file 10 or file 11 must keep Part IV's provenances and (R)'s \(\operatorname{Sel}\lor\operatorname{Con}\) conjunct. Only derived patterns and wording can be carried back. The widened "surprise" is W35 above, and 12:554 is W15.

### W46. Realized edits and the two notions of counterfactual (source point 7; 12:491; O22)

- **What is missing.** The link between admitted edits and physical possibility sits only in "physically admitted" (F10 L41, L272). File 12 states it outright:
  - 12:491: an edit is realized when the physics admits a controlled action that replaces the component; an action that changes two ports realizes a joint edit.
  - 12:77, in Part I: every admitted edit must be one the physics admits.
  - Neither file 10 nor file 11 speaks to joint edits beyond composition.
- **Where.** File 10: L41, L272, L462–482. File 11: L45, L259, L451–473.
- **Evidence.**
  - Verify obs 7 (CONFIRMED; carry back 12's paragraph).
  - Raw 01c, O22 hard case.
  - Trial: Atria O22, D x.
- **Severity.** Coherence.
- **Handling.** Clarification: carry back 12:491 and 12:77.
- **Gained.** O22's "together" becomes a realized joint edit, and N8's "impossible" is kept apart from "never happened".
- **Lost.** A further physical-module obligation on every contract.
- **Risk.** None; O22 stays AGREE.
- **Tests.** O22, O33, O9, O6. N8, N24.
- **S81.** Independent.

### W47. Causal dependence, collateral offered as a cause, common cause and chain, direction as a theorem

- **What file 12 has.**
  - Causal dependence (CD) as a pattern in (O) (12:113–121), carried across by (F1) (12:245).
  - "A collateral effect offered as a cause fails (F1)" (12:273).
  - The fork against the chain (12:337–339).
  - "Direction is derived" as Derivation 3 (12:578–584), which answers the problem of reversibility (M1).
- **Where.** File 10: L138–144, L282–290, L336–338. File 11: L123–129, L269–277, L321–323.
- **Evidence.** File 12. Verify M1.
- **Severity.** Coherence (new claims).
- **Handling.** New derived claims, carried without file 12's removal of provenance. Defer: file 12 is under no round, and the project's rule is that a claim change is earned by a case.
- **Gained.** Grievance 1 made exact; direction becomes a theorem (N23); a fourth classic failure for the sufficiency list.
- **Lost.** Length; untested claims; a new Part XV exposure (the direction attack).
- **Risk.** O6, O9, O22.
- **Tests.** O6, O7, O9, O22. N23, N16.
- **Depends on.** W46.
- **S81.** Independent.

### W48. Actual causation (AC); ProducedBy defined through (AC); contrasts as a declared input

- **What file 12 has.**
  - (AC), read from the active routes of a history (12:385–391).
  - ProducedBy as "(AC) applied to the repair as result" (12:451).
  - The contrasts \(K\) as a declared input (12:532).
  - Selecting "the" cause among several actual causes as an invocation of \(\mathcal N\) (12:465).
  - The pre-emption episode (Derivation 11, 12:634–646).
- **Where.** File 10: L384 and L441 (ProducedBy undefined). File 11: L371, L433 and L514.
- **Evidence.**
  - File 12.
  - Det 02 C58: file 10 leaves ProducedBy undefined.
  - Det 01 O20: file 10's AGREE rests on the undefined word read in its ordinary sense.
  - Trial §3b, Mimo on O20: "sufficient" and "would have" (JUDGEMENT).
- **Severity.** Coherence.
- **Handling.** New claim. Adopt (AC) and define ProducedBy by it. Defer the pre-emption episode.
- **Gained.** O20, O25, O39 and O52 are grounded, and "sufficient" is no longer read by example.
- **Lost.** A new declared input (the contrasts) adds SILENT risk wherever contrasts are left unstated.
- **Risk.** O20, O26.
- **Tests.** O13, O19, O20, O25, O26, O39, O52.
- **Depends on.** W14, W23, W28.
- **S81.** Both, differently. File 11's L433 is the text to extend.

### W49. Absence and prevention constructions; attack B widened

- **What file 12 has.** Causation by absence (12:341–343), prevention and double prevention (12:345–347), and absence and prevention added to attack B (12:548).
- **Where.** File 10: L350–352, L70, L535. File 11: L335–337, L530.
- **Severity.** Coherence.
- **Handling.** New constructions for Part VII. Defer.
- **Gained.** More exact exposure under attack B.
- **Lost.** Length, and more surface for attack.
- **Tests.** N8, N22.
- **Depends on.** W40, W47.
- **S81.** Independent.

### W50. What a failed intervention refutes (K3; 12:411)

- **What file 12 adds.** An intervention whose prediction fails refutes the conjunction that includes "the intervention realized the intended edit".
- **Where.** File 10: L404. File 11: L391.
- **Severity.** Coherence (low).
- **Handling.** Clarification.
- **Gained.** The case where the theory is right but its use is wrong becomes explicit.
- **Lost.** Nothing.
- **Tests.** N18 (Rhea: was it her theory or her use of it?).
- **S81.** Independent.

---

## Group 6. Process prerequisites (no theory text)

- **W51. S78 group B: the seeded-error round is unfinished.**
  - S79 is set up: two planted errors, a sealed list, and the S79-1 pack sent. According to the story's "Next step", it still waits on its Stage 1 return.
  - S80's eight planted errors served only the skill verdict. Marking was not run and the sealed list stays sealed (story S82).
  - So nobody yet knows whether the pattern can fail a wrong theory. Revision 2's own test round relies on that pattern.
- **W52. S78 group C: cases out of the determiner's hands.**
  - N1–N25 have verdicts fixed by Claude instances that never read the theory. That meets the first half of group C.
  - They were not written by an agent outside Claude's model family, and they have not been mixed unmarked into a round.
  - Adoption as O53 onward is pending. N14 is set aside. N6's Leon half is undecided under the low-confidence rule.
- **W53. S78 group A leftovers.**
  - Group A was applied to the S81 rebuild (story S81). It was not checked item by item here.
  - D3-T was not entered as O53: the S81 case book holds O1–O52 only.
- **W54. The FW5 richness audit (the S79 method) is only partly done.**
  - Parts of file 00 absent from files 10 and 11 that this worklist already uses: 00:208, 00:210, 00:383, 00:440–447, 00:518, 00:620, 00:746, 00:754, 00:785, 00:800, 00:839, 00:855–861, 00:912, 00:995–1011, 00:1015–1031.
  - The rest of file 00 has not been listed. The verifier read it by section, and Claude only at the lines above.
- **W55. Unknown candidates.**
  - The first 32 Stage B rows (R2 amendments A, B, C and the first D rows) are unrecovered.
  - The R2 file is not in the repository.
  - Candidates may lie there.
- **W56. Determination files 01 and 02 disagree on O38's file-10 mark.**
  - Det 01 rules O38 AGREE/AGREE: the stated condition ranges over the work period.
  - Det 02 §5(ii) says an end-state reading gives file 10 SPLIT or DISAGREE.
  - If det 02 is right, O38 is a sixth changed verdict, moving toward the fixed verdict. That bears on W1, W4 and W5. It is for the determination to settle, not for this worklist.

---

## N-cases against the worklist

Status: "A1" is AGREED in round 1, "A2" is AGREED in round 2, "SA" is set aside. N14 is set aside and cannot test a verdict until it is rewritten and judged again.

| N | title | status | items it tests | what it would show |
|---|---|---|---|---|
| N1 | Seasons and the sun god | A1 | W33, W20, W36 | the split between (E) and (B): Tomas explains, and the idle sentence is reported, not part of the explanation |
| N2 | The myth amended | A1 | W33, W29, W36; Derivation 7 and the historical index | a patch made to fit a report after the fact is a new index and explains nothing |
| N3 | A myth about winter | A1 | W36, W29, W39, W20 | an explanation "only in form"; the answer is written into the bargain |
| N4 | The tilt and the midnight sun | A2 | W34, W21 | reach is fixed by the content (Account), while "had anyone explained it" is Deploy or Origin |
| N5 | A farmer's rule carried south | A1 | W2, W16, W18, W34 | two readings of the rule survive the home history: underdetermination at an unseen change |
| N6 | Two astronomers | A1 (Leon half low in round 3) | W32 | a stated limit (Iras) against a claim that contradicts its own cause elsewhere (Leon) |
| N7 | Two bakers | A1 | W32 (guard), W33 | an unexplained limit still explains; any scope rule that flips this is wrong |
| N8 | The machine that runs forever | A1 | W40, W46, W49; Barriers (F10 L496) | "a finite list of failures is not a barrier proof"; obstruction by an invariant |
| N9 | Dark moths | A2 | W43, W18, W16 | a selected correspondence at population grain, and whether "knowledge" is needed |
| N10 | The burned notebook | A1 | W43, W23, W21 | (EK) is indexed to an event; the knowledge is created, then lost |
| N11 | Two students, ten drafts | A1 | W37, W18, W12, W14 | selection by an outside chooser against construction by one's own criticism |
| N12 | Consent by rephrasing | A1 | reason use (F10 L394); W41 | positive control: understanding shown through use |
| N13 | The parrot | A1 | Build, "relay is not" (F10 L414); Derivation 9; W41 guard | positive control: a carrier is not a constructor |
| N14 | The walking robot | SA | W18, W14 | only after a rewrite ("Can the credit be divided?") |
| N15 | The miscopied notes | A1 | W3 (C53), W21, W12 | a small repair of her own inside received content; new to her, not to the world |
| N16 | The domino that never falls | A1 | W44, W29, W20, W47 | answer A restates what was seen; B answers at a quasi-autonomous level |
| N17 | The transistor | A2 | W44, W11, W19 | whether a full fine-grain derivation is a full Account (a possible disagreement with the fixed verdict) |
| N18 | Two footbridges | A2 | W35, W50, W2/W16 | a constructed theory contradicted (Rhea); an expectation from an incomplete history (Dov) |
| N19 | The novelist's two demands | A1 | W35, W5 | a problem as a clash of obligations before any observation; a draft that drops P is not a Repair |
| N20 | Keeping count with string | A1 | W31, W42 | accumulated error without a correction step |
| N21 | The order of adjectives | A2 | W41, W12, W21 | tacit knowledge; she formed it herself with no explicit binding |
| N22 | Denying the inner experience | A2 | W40, W49 | a bare denial against a denial that explains the appearance |
| N23 | The planets tonight | A1 | W47, W19; Part V reversed calculation (F10 L286) | direction comes from admitted edits; "because" as evidence is not "because" as cause |
| N24 | Two sealed sorts of matter | A1 | W45, W25; Part XIII | universality and barriers under failed interoperability |
| N25 | What holds the universe up | A1 | W39, W19, W33, W29 | same-form regress; dog and turtle as one account at the grain; an idle difference |

---

## Ordering proposal

**Before drafting.**

1. Let S81 finish and decide the base.
2. Settle W56 (O38) inside the determination.
3. Read determination file 03 if one appears.

**Stage 1: errata.** These carry no verdict risk and apply to either base.

- W24, W26, W27, W22, W25 (the notation half), W31, W10, W9, W8, W37 and W6.
- W1 comes last, because it reports on everything else.
- These are cheap and restore text file 00 already had. W31 also removes the one literal counterexample to a result that Part XV lists.

**Stage 2: defects in claims that Part XV exposes.** Run cases on each.

| item | cases to run |
|---|---|
| W19 | O24, O10, O45, O46; N25 |
| W20, with W39 and W29 | O2, O4, O5, O7, O33, O36; N1, N3, N16, N25 |
| W16 and W17, plus W2 on a file-10 base | O48, O24, O11; N5 |
| W21 | O3, O11, O18, O27, O31; N4, N15 |

These go first among the substantive items. The theory's own defeat list names these derivations and conditions, so the text itself has earned the repair; no new case is needed to justify it.

**Stage 3: the verdict-bearing text of file 11.**

- W4, W5 and W15 together, because they share the default-input question with W12.
- W12 and W13.
- W14.
- W7.
- W11.
- W3: declare the sentences on a file-11 base, or import them on a file-10 base.

**Stage 4: clarifications with no verdict risk.** W36, W33, W34, W38, W41, W28, W30 and W23.

**Stage 5: choices with a real cost,** each run with its guard case:

| item | guard cases |
|---|---|
| W32 | N7, O8, O5 |
| W35, option (b) | O3, O12 |
| W40 | N22 |
| W18 | O48 |

**What revision 2 should leave out, and why.**

- **W43, the knowledge bridge.** It is scope creep and puts Derivation 6 at risk. State the reason instead.
- **W42.** Wait until W31 is fixed and N20 has been run.
- **W47, W48 (beyond defining ProducedBy), W49 and W50.** File 12 is under no round. Adopting untested new claims would break the project's rule that a claim change is earned by a case. Test them in file 12 first. From file 12, carry back only W46's wording and W15's sentence.
- **Making scope (W32) or hard-to-vary (W33) a fifth condition.** It would flip N7 and O8 and bring back grading, which files 00 and 10 reject on purpose.
- **W44's derived level notion.** Keep only the note. A predicate on grain would break "indices, not primitives".
- **Objective aesthetics and universality claims.** The theory abstains from both on purpose (F10 L25, L510; M10).

---

## Items that conflict with one another

1. **Default inputs.** W4(b), a default for occasions, and W12(a), an evident boundary, both add default inputs. That conflicts with F11 L514 ("rather than choosing the input from the verdict wanted") and L465 ("declared before … not chosen after"), which W6, W7 and W15 would reinforce. A revision takes both defaults or neither, and each must be stated in advance as a general rule.
2. **Weighting.** W14(b), a weighting as a declared input, conflicts with the AGREEs on O21 and O27, and with W48, since (AC) supplies no ranking. W14(a) does not conflict.
3. **Scope.**
   - W32(c), a scope measure in Part VI, conflicts with W6 and W7's reading, in which appropriateness is a declared input (F11 L161, L514). It would make appropriateness partly derived.
   - Read as a condition, it also conflicts with N7, O8 and story S29's failed A-prime.
4. **Surprise.** W35(b) and W35(c) exclude each other. (c) also conflicts with Derivation 4's "learning versus creating" and with Derivation 10.
5. **Tables.** W11, which weakens "the table is an account", must keep S70's fix, under which the front matter defers to Part V. Otherwise the lookup-table gap of S57 and S70 reopens.
6. **Derivation 3.** W16, which gives Derivation 3 refutable content, pulls against W2 and O48. Re-widening the claim can return O48 to DISAGREE. W18 must use the same notion of population as W16 and W17.
7. **Derivation 2 and \(\equiv_\ell\).**
   - W19 narrows Derivation 2 to shared anchors. If W21 defines \(\equiv_\ell\) through Derivation 2, a reconstruction with a different decomposition counts as new, which puts O11, N15 and O18 at risk. W21 must be written after W19 and independently of its narrowing.
   - W19 also weakens Derivation 2's Consequence, which grievance 2 and attack C use against claims that two candidates "really differ".
8. **Non-circular dependence.** W20, which retypes the condition, must keep F11 L275's packaging rule (O2) and 00:210's counterfactual-law contrasts (W39). A retyping written from Part VI alone could drop both.
9. **File 12 and provenance.** W46–W50 are imported from a file that removes provenance. File 12's (R) (12:205–211) and 12:201 ("Nothing about how a transport came to be written enters its assessment") contradict Part IV and (R)'s \(\operatorname{Sel}\lor\operatorname{Con}\). Only derived patterns can be imported.
10. **Explanation and Part I.** W36 rewords Part I's Fallibility commitment (F10 L86 / F11 L71), a commitment sentence, not a gloss.
11. **Inexplicit witnesses.** W41, a witness identified by use, pulls against "relay is not" construction (F10 L414). N13's parrot must stay a carrier.
12. **Idle parts.** W33 (idle parts are reported, not rejected) is a deliberate departure from D p.25 and should be recorded in W38's note of departures. It conflicts with any reading of W32 as a condition.
13. **The occasions sentence on a file-10 base.** On a file-10 base, W3 (import C55, the Ownership definition) brings W12's cost. W4(c) (do not import L433 wholesale) must then be squared with W5.

---

## What could not be verified

- **Determination file 03** does not exist, locally or on the working branch `claude/semantics-folder-work-9rtd5s` on GitHub, as of this writing. Remote `main` holds no S80 or S81 results at all.
- **Book pages.** Every book page and quotation comes from the verification file. Claude did not reread the books. `sources/pinker/` was not opened.
- **S78 group A.** Whether each group A item was applied to S81 was not checked, because the S81 plans were not opened. Only the story's statement was used.
- **R2 J's Part VIII sentence** is known only as quoted in the S72 Stage 2 return. The R2 file is not in the repository.
- **The 32 unrecovered Stage B rows** may hold further candidates.
- **S79's Stage 1 return.** The story says it is still awaited. This was not checked beyond the story.
- **W10(b)**, Derivation 10's citation of Derivation 2, is Claude's own reading, checked by no other reader.
- **The O38 discrepancy (W56)** between det 01 and det 02 is recorded here, not resolved.
- **File 00 line numbers.** The verifier cited them. Claude spot-checked 00:208, 210, 383, 440–447, 518, 606–622, 742–746, 754, 785, 800, 804, 839, 855–861, 895–915, 993–1031, 1104–1128, 1296–1308 and 1328–1336. All match.
- **Every O-case at risk named here comes from the texts and determination files 01 and 02.** No S81 return was read, so none of these risks has been run against a return.
