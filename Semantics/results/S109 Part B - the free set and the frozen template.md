# S109 Part B: the free set and the frozen template

*The same template for the four agents of Part B round 1 (decision S52: "Freeze everything except the hard to vary bits to see how explanation changes in meaning and scope."). Built by `tools/s109_build.py` from the text, the formal core and the claims after the fourth review round, from Part A's frozen set (`tools/s108_frozen_set.py`) and from Part A's dependency map after its cross-examination. Part A's frozen set is the drafters' working reading of "the parts that are hard to vary"; the owner has not been asked to approve it. Nothing here changes the text or the maths: Part B varies copies. "Model" here means only a small structure the program builds, never a candidate (S43).*

## 1. How to read it

- Part B is Part A inverted. Every sentence of the text and every definition and encoding of the formal core carries one mark:
  - **B1**, **B2**, **B3**, **B4**: the **free set**, Part A's frozen set (the parts that are hard to vary, in the working reading: put to the readers or checkers at least once, and changed by no round or step), in four sections. Each agent varies its own section only.
  - **FROZEN**: everything else, which is Part A's middle. It stays exactly as it is in every variant.
- After a free mark, ⟨…⟩ says what the item bears on, from Part A's map (section 3): **E** (E), Account; **Dec** the provenance clause; **Expl** being an explanation, Account ∧ ¬Dec(t) (D16.XV); **Suff** and **Nec** the claims (Suff) (L536, L17) and (Nec) (L538); **SC** a strong candidate (a sentence the review rounds tried to vary and left unchanged, on the list of S100, S101); **SCdef** a definition that formalizes a strong candidate.
- A definition bears on a part when it is among the definitions the part is defined by, reads, or has upstream in the program's dependency graph (D18.1), through the parts' nodes in Part A's map. A sentence bears on a part through the definitions that formalize it; which ones is listed in section 3 (and in the `.json`).
- A free sentence formalized by a FROZEN definition: a variant of the sentence may carry the matching change of that definition, marked "changes with (its formalization)"; no other FROZEN item changes. A FROZEN item that cannot stand beside a variant is an edge (blocks), recorded; the variant is still computed. A variant that changes a FROZEN item beyond the formalization of the free words it varies is out of Part B.
- Ids as in Part A: `L<line>.s<k>` (a sentence unchanged since the oldest text the record follows) or `L<line>.n<k>` (newer words); definitions `D§.n`, encodings `En`, as in the formal core.

## 2. The four sections of the free set, and why this split

| section | what it holds | stretch of the text | free sentences | free definitions | all | bear on (E) | on Dec | on Expl, (Suff) or (Nec) | strong candidates |
|---|---|---|---|---|---|---|---|---|---|
| B1, organizations, kinds, questions and contracts | what an account is of: the target organization, its components and admitted edits, roles and kinds, and the question with its contract, query and stated scope; (E) reads all of it | Part 0 to Part III | 41 | 16 | 57 | 27 | 26 | 27 | 14 |
| B2, transports, fidelity, the account, routes and the exact constructions | the account itself: the transport, (E)'s conjuncts (F1), (F2), (A), Dependence and NonVacuous, what (E) excludes, work and routes over the commitments, the exact constructions that exercise it, and the transport results | Part IV's Transports, Part V, Part VI to L313, Part VII, Part VIII | 37 | 20 | 57 | 14 | 9 | 20 | 1 |
| B3, provenance, histories, representation, construction, repair and the physical module | the provenance clause: occurrences and contents, the two layers, selected, constructed and declared, representation, prediction and violation, construction and origin, repair and created explanation, the physical module; Dec reads these | the rest of Part IV, Parts X to XII | 37 | 20 | 57 | 0 | 9 | 13 | 6 |
| B4, rivals, problems, criticism, the class, what would rule it out, and the Arguments | what rules candidates out and what the class claims: rivals, conflict with a claim, problems, criticism and arguments, recursion, the class collected, the defeat conditions and the Arguments; (Suff) and (Nec) read these | Part VI from L315, Part IX, Parts XIII to XVI | 54 | 13 | 67 | 0 | 0 | 8 | 6 |

**Why this split.** Part A's sections were stretches of Parts balanced by middle items; cut the same way, the free set would fall 57 / 95 / 49 / 37. Part B splits it by the explanation definition's own structure: being an explanation is Account(ℰ) ∧ ¬Dec(t), with (Suff) and (Nec) the claims about it, and the text gives the order in which its parts depend on each other (L526: (K) on (O) and a contract; (F1), (F2), (A) on (O), (Q), (K); representation on fidelity and provenance; …). So B1 holds what an account is of (the target and the question), B2 the account itself, B3 the provenance clause Dec reads, and B4 what rules candidates out and what the class claims, which (Suff) and (Nec) read. Two Parts are cut at their own seams: Part IV at its heading "Transports" (the transport goes with the account; occurrences, layers, provenances, representation and prediction with provenance), and Part VI at L315, where work and routes (L287 to L313) end and rivals, conflict and problems begin. A definition goes where the first line it formalizes lies; one that quotes no line goes by its Part. The weights come out 57 / 57 / 57 / 67.

**What the explanation definition rests on, among the free items** (Part A's map after its cross-examination, `part A/the dependency map, after the cross-examination.md`, its §1 and nodes `X:`). In Part B the definitions that compose the parts are FROZEN, since they were Part A's middle: (E)'s D6.7, Dec's D12.3, D16.XV, and Dependence's D6.4, D6.5. What is free is much of what they are built from:

- **(E)** rests on 18 free definitions: D1.1, D1.2, D1.3, D3.1, D3.2, D3.5, D3.7, D4.1, D4.4, D5.1, D5.2, D5.3, D5.4, D5.5, D5.6, D6.1, D6.2, D6.6.
- **Dec** rests on 13 free definitions: D1.1, D1.2, D1.3, D3.1, D3.2, D3.7, D4.1, D4.4, D5.4, D5.5, D11.5, D12.4, D12.5.
- **Expl** rests on 25 free definitions: D1.1, D1.2, D1.3, D3.1, D3.2, D3.5, D3.7, D4.1, D4.4, D5.1, D5.2, D5.3, D5.4, D5.5, D5.6, D6.1, D6.2, D6.6, D6.10, D9.3, D9.5, D11.1, D11.5, D12.4, D12.5.
- **(Suff)** rests on 25 free definitions: D1.1, D1.2, D1.3, D3.1, D3.2, D3.5, D3.7, D4.1, D4.4, D5.1, D5.2, D5.3, D5.4, D5.5, D5.6, D6.1, D6.2, D6.6, D6.10, D9.3, D9.5, D11.1, D11.5, D12.4, D12.5.
- **(Nec)** rests on 22 free definitions: D1.1, D1.2, D1.3, D3.1, D3.2, D3.5, D3.7, D4.1, D4.4, D5.4, D5.5, D5.6, D6.1, D6.2, D6.6, D6.10, D9.3, D9.5, D11.1, D11.5, D12.4, D12.5.

## 3. The free set, by section

Per section: the free items (id, kind, what each bears on, and, for a sentence, the definitions it bears through); the carry-overs from Part A; the Part A variants a free item of the section blocked. Why each item is hard to vary: `template/why each free item is hard to vary.md` (Part A's frozen set). Part A's edges into each free item are in the `.json` (`part_A_edges_in`).

### 3.1 Section B1: organizations, kinds, questions and contracts (Part 0 to Part III)

| id | kind | bears on | through | strong candidate |
|---|---|---|---|---|
| `L27.s2` | sentence | – | – | yes |
| `L41.s4` | sentence | – | – | yes |
| `L47.s2` | sentence | – | – | yes |
| `L51.s1` | sentence | – | – | yes |
| `L57.s1` | sentence | – | – | – |
| `L67.s1` | sentence | – | – | – |
| `L87.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L91.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L91.s2` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L91.s3` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L91.s4` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L91.s5` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L91.s6` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L93.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L99.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.2 | – |
| `L103.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.3 | – |
| `L103.s2` | sentence | – | – | – |
| `L103.s3` | sentence | – | – | – |
| `L105.s2` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L105.s3` | sentence | (E), Dec, Expl, (Suff), (Nec) | D1.1 | – |
| `L109.s1` | sentence | – | – | – |
| `L109.s2` | sentence | – | – | – |
| `L109.s3` | sentence | – | – | – |
| `L109.s5` | sentence | – | – | – |
| `L113.s1` | sentence | – | – | yes |
| `L113.s2` | sentence | – | – | yes |
| `L115.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D4.1 | yes |
| `L124.s1` | sentence | – | – | yes |
| `L125.s1` | sentence | – | – | yes |
| `L127.s2` | sentence | – | – | yes |
| `L127.s3` | sentence | – | – | yes |
| `L137.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D3.1 | – |
| `L141.s2` | sentence | (E), Dec, Expl, (Suff), (Nec) | D3.1 | – |
| `L143.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D3.2 | – |
| `L147.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D3.1 | – |
| `L147.s2` | sentence | (E), Dec, Expl, (Suff), (Nec) | D3.1 | – |
| `L151.s2` | sentence | – | – | – |
| `L155.s6` | sentence | – | – | – |
| `L161.s1` | sentence | – | – | yes |
| `L161.s2` | sentence | – | – | yes |
| `L161.s3` | sentence | – | – | yes |
| `D0.1` | definition | – | – | – |
| `D1.1` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D1.2` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D1.3` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D2.2` | definition | – | – | – |
| `D2.3` | definition | – | – | – |
| `D2.5` | definition | – | – | – |
| `D3.1` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D3.2` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D3.5` | definition | (E), Expl, (Suff), (Nec) | – | – |
| `D3.7` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D4.1` | definition | (E), Dec, Expl, (Suff), (Nec) | – | formalizes one |
| `D4.2` | definition | – | – | – |
| `D4.3` | definition | – | – | – |
| `D4.4` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D4.5` | definition | – | – | – |

**Carry-overs from Part A** (class a: ruled to Part B by Part A's records; class b: flagged by Part A round 2's tabulation as changing a FROZEN item, and not implemented; a class-b item may be taken up as a variant of the free item it rewrites):

- **V1.7** (class a; Part A round 1, section 1 (D0.2)) on `D3.5`. Ruled to Part B by the orchestrator's decision 3 on round 1's critical review; edges e1.48 to e1.51, claimed only. Old: Excl(Σ) a primitive (I27); D3.5: Σ is a declared input naming Excl(Σ) ⊆ A×B; Stated(C,Σ) :⟺ (A×B)∖C ⊆ Excl(Σ). New: Excl(Σ) := (A×B) ∖ C, defined; so Stated(C,Σ) always holds (D0.2's primitive changes with it). The silent narrowing L43.s4 says is caught would no longer be caught; on every question the program builds I85's default scope already equals the formula, so only a question stating a smaller exclusion moves (Acc F → T there); blocks D3.5, L43.s4, L159.s1; constrains D6.6 (NonVacuous's second conjunct becomes vacuous); moves NonVacuous.
- **R2V1.2** (class b; Part A round 2, section 1 (D3.4)) on `L155.s6`. Flagged by the round-2 tabulation (possible, in effect: L155.s6); not implemented. Old: D3.4: constructed :⟺ C results from an episode with a construction trace; Found(p) requires ρ_p = constructed. New: constructed :⟺ ∃h′ [Rec_h′(C→C′) = constructed ∧ Prepares(h′, C′ as a content)]; Found(p′) :⟺ ρ_p′ = constructed. Settles e1.37 in the reply's reading.
- **R2V1.4** (class b; Part A round 2, section 1 (L15.s2 through D3.4)) on `L155.s6`. Flagged by the round-2 tabulation (in effect: L155.s6); not implemented; edge r2e1.30, claimed only. Old: Found(p) requires ρ_p = constructed (D3.4; L155.s6). New: Found(p) :⟺ ρ_p ∈ {selected, constructed}. A question found by selection counts as found.
- **R2V1.7** (class b; Part A round 2, section 1 (L119.s1)) on `D4.2`. Flagged by the round-2 tabulation (in effect: D4.2); not implemented; edge r2e1.34, claimed only. Old: D4.2: j ~_C j′ :⟺ a bijection β: V_j → V_j′ with X_v = X_β(v) and L_j′(a,b) = β_*(L_j(a,b)) ∀(a,b) ∈ C (I10). New: j ~_C j′ :⟺ V_j = V_j′ ∧ sig_C(j) = sig_C(j′) (footprints as ordered tuples; β dropped). Kinds read through the ports themselves, not up to a relabeling.
- **R2V1.8** (class b; Part A round 2, section 1 (L141.n3)) on `D3.2`. Flagged by the round-2 tabulation (possible, in effect: D3.2; E4); not implemented; edge r2e1.37. Old: Q(O,a,b;δ_O) ∈ Y_p ∪ {⊥}, Y_p free (D3.2). New: Y_p := X_δD (⊥ as D3.2). The query answers with values of the designated port only; E4 [B2] would carry no question.
- **R2V1.9** (class b; Part A round 2, section 1 (L159.s3)) on `D3.1`. Flagged by the round-2 tabulation (as written: D3.1); not implemented; edge r2e1.40. Old: D3.1: C ⊆ A×B, (1,b0) ∈ C; L159.s3: admitting a change is not a claim that it can be carried out. New: Question(p) ⇒ ∀(a,b) ∈ C: Θ_admits(a); a C holding an unadmitted pair names no question. Departs from S25 to S27 (the reply names them): physical possibility would enter what a question is.

**Part A variants a free item of this section blocked** (a blocks edge of Part A's map ending at it; a variant of the free item would lift the block):

- e1.00: V1.1 blocks `D4.4` (computed)
- e1.14: V1.2 blocks `L103.s2` (claimed only)
- e1.48: V1.7 blocks `D3.5` (claimed only)
- r2e1.30: R2V1.4 blocks `L155.s6` (claimed only)
- r2e1.34: R2V1.7 blocks `D4.2` (claimed only)

### 3.2 Section B2: transports, fidelity, the account, routes and the exact constructions (Part IV's Transports, Part V, Part VI to L313, Part VII, Part VIII)

| id | kind | bears on | through | strong candidate |
|---|---|---|---|---|
| `L185.s1` | sentence | (E), Expl, (Suff) | D5.1 | – |
| `L189.s1` | sentence | (E), Expl, (Suff) | D5.1 | – |
| `L189.s2` | sentence | Dec, Expl, (Suff), (Nec) | D5.7 | – |
| `L241.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D5.5 | – |
| `L245.s1` | sentence | Dec, Expl, (Suff), (Nec) | D5.7 | – |
| `L245.s2` | sentence | Dec, Expl, (Suff), (Nec) | D5.7 | – |
| `L245.s3` | sentence | Dec, Expl, (Suff), (Nec) | D5.7 | – |
| `L247.s1` | sentence | Dec, Expl, (Suff), (Nec) | D5.7 | – |
| `L249.s1` | sentence | (E), Expl, (Suff), (Nec) | D5.6 | – |
| `L253.s1` | sentence | (E), Dec, Expl, (Suff), (Nec) | D3.2 | – |
| `L265.s2` | sentence | – | – | – |
| `L281.s3` | sentence | – | – | – |
| `L281.s4` | sentence | – | – | – |
| `L287.s1` | sentence | – | – | – |
| `L289.s1` | sentence | – | – | – |
| `L293.s1` | sentence | – | – | – |
| `L295.s1` | sentence | – | – | – |
| `L299.s1` | sentence | – | – | – |
| `L301.s1` | sentence | – | – | – |
| `L307.s1` | sentence | – | – | – |
| `L309.s1` | sentence | – | – | – |
| `L311.s2` | sentence | – | – | yes |
| `L325.s3` | sentence | – | – | – |
| `L325.s4` | sentence | – | – | – |
| `L329.s3` | sentence | – | – | – |
| `L335.s1` | sentence | – | – | – |
| `L335.s2` | sentence | – | – | – |
| `L343.s1` | sentence | – | – | – |
| `L343.s2` | sentence | – | – | – |
| `L343.s3` | sentence | – | – | – |
| `L343.s8` | sentence | – | – | – |
| `L347.s1` | sentence | – | – | – |
| `L347.s2` | sentence | – | – | – |
| `L347.s3` | sentence | – | – | – |
| `L361.s2` | sentence | – | – | – |
| `L369.s1` | sentence | – | – | – |
| `L369.s2` | sentence | – | – | – |
| `D5.1` | definition | (E), Expl, (Suff) | – | – |
| `D5.2` | definition | (E), Expl, (Suff) | – | – |
| `D5.3` | definition | (E), Expl, (Suff) | – | – |
| `D5.4` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D5.5` | definition | (E), Dec, Expl, (Suff), (Nec) | – | – |
| `D5.6` | definition | (E), Expl, (Suff), (Nec) | – | – |
| `D6.1` | definition | (E), Expl, (Suff), (Nec) | – | – |
| `D6.2` | definition | (E), Expl, (Suff), (Nec) | – | – |
| `D6.6` | definition | (E), Expl, (Suff), (Nec) | – | – |
| `D6.10` | definition | Expl, (Suff), (Nec) | – | – |
| `D7.1` | definition | – | – | – |
| `D7.2` | definition | – | – | – |
| `D7.3` | definition | – | – | – |
| `D7.5` | definition | – | – | – |
| `D7.6` | definition | – | – | – |
| `E3` | definition | – | – | – |
| `E4` | definition | – | – | – |
| `E5` | definition | – | – | – |
| `E6` | definition | – | – | – |
| `E7` | definition | – | – | – |

**Carry-overs from Part A** (class a: ruled to Part B by Part A's records; class b: flagged by Part A round 2's tabulation as changing a FROZEN item, and not implemented; a class-b item may be taken up as a variant of the free item it rewrites):

- **R2V2.7** (class a; Part A round 2, section 2 (D5.7)) on `L189.s2`. D5.7's one variant; it rewrites L189.s2, so Part A's settlement gave it to Part B; edge r2e2.14, claimed only. Old: L189.s2: a transport is faithful on C when it meets the component and global fidelity conditions of Part V; D5.7: Faithful_C(t) := F1_C ∧ F2_C; QFid_C := A_C; Viol narrow (D12.7). New: Faithful_C(t) := F1_C ∧ F2_C ∧ A_C (question fidelity inside 'faithful'); Viol := Viol⁺. A selected transport wrong in its answers on its own H is no longer Sel, so Dec (FC104.new1 (a)); Rep harder, so Sel easier where earlier representations exist; (Nec) reads Faithful.

**Part A variants a free item of this section blocked** (a blocks edge of Part A's map ending at it; a variant of the free item would lift the block):

- e1.23: V1.2 blocks `L347.s2` (computed)
- e1.52: V1.8 blocks `L347.s2` (computed)
- e2.03: V2.2 blocks `L311.s2` (computed)
- e2.06a: V2.3 blocks `L329.s3` (contradicted)
- e2.25: V2.2 blocks `L307.s1` (computed)
- r2e2.14: R2V2.7 blocks `L189.s2` (claimed only)

### 3.3 Section B3: provenance, histories, representation, construction, repair and the physical module (the rest of Part IV, Parts X to XII)

| id | kind | bears on | through | strong candidate |
|---|---|---|---|---|
| `L169.s1` | sentence | Expl, (Suff), (Nec) | D11.1 | – |
| `L169.s2` | sentence | Expl, (Suff), (Nec) | D11.1 | – |
| `L169.s3` | sentence | Expl, (Suff), (Nec) | D11.1 | – |
| `L177.s1` | sentence | – | – | – |
| `L195.s1` | sentence | Dec, Expl, (Suff), (Nec) | D12.1 | – |
| `L195.s5` | sentence | Dec, Expl, (Suff), (Nec) | D12.1 | – |
| `L199.s1` | sentence | Dec, Expl, (Suff), (Nec) | D12.3 | – |
| `L199.s3` | sentence | Dec, Expl, (Suff), (Nec) | D12.3 | – |
| `L201.s2` | sentence | – | – | – |
| `L201.s3` | sentence | – | – | – |
| `L207.s1` | sentence | Dec, Expl, (Suff), (Nec) | D12.5 | – |
| `L217.s2` | sentence | Dec, Expl, (Suff), (Nec) | D11.5 | yes |
| `L219.s1` | sentence | – | – | yes |
| `L225.s1` | sentence | – | – | yes |
| `L225.s3` | sentence | – | – | – |
| `L225.s4` | sentence | – | – | yes |
| `L403.s2` | sentence | – | – | – |
| `L403.s3` | sentence | – | – | – |
| `L407.s1` | sentence | – | – | – |
| `L409.s5` | sentence | – | – | – |
| `L409.s6` | sentence | – | – | – |
| `L411.s1` | sentence | – | – | – |
| `L411.s2` | sentence | – | – | – |
| `L415.s1` | sentence | – | – | – |
| `L425.s1` | sentence | – | – | – |
| `L425.s2` | sentence | – | – | – |
| `L427.s3` | sentence | – | – | – |
| `L437.s1` | sentence | – | – | yes |
| `L441.s2` | sentence | – | – | – |
| `L441.s4` | sentence | – | – | yes |
| `L443.s3` | sentence | – | – | – |
| `L453.s1` | sentence | – | – | – |
| `L465.s1` | sentence | – | – | – |
| `L469.s1` | sentence | – | – | – |
| `L475.s1` | sentence | – | – | – |
| `L477.s1` | sentence | – | – | – |
| `L479.s4` | sentence | – | – | – |
| `D11.1` | definition | Expl, (Suff), (Nec) | – | – |
| `D11.5` | definition | Dec, Expl, (Suff), (Nec) | – | formalizes one |
| `D12.4` | definition | Dec, Expl, (Suff), (Nec) | – | – |
| `D12.5` | definition | Dec, Expl, (Suff), (Nec) | – | – |
| `D12.6` | definition | – | – | – |
| `D13.1` | definition | – | – | – |
| `D13.2` | definition | – | – | – |
| `D13.4` | definition | – | – | – |
| `D13.5` | definition | – | – | – |
| `D13.6` | definition | – | – | – |
| `D14.2` | definition | – | – | formalizes one |
| `D14.3` | definition | – | – | – |
| `D14.4` | definition | – | – | formalizes one |
| `D14.5` | definition | – | – | – |
| `D14.6` | definition | – | – | – |
| `D14.8` | definition | – | – | – |
| `D15.3` | definition | – | – | – |
| `D15.4` | definition | – | – | – |
| `D15.6` | definition | – | – | – |
| `D15.7` | definition | – | – | – |

**Carry-overs from Part A** (class a: ruled to Part B by Part A's records; class b: flagged by Part A round 2's tabulation as changing a FROZEN item, and not implemented; a class-b item may be taken up as a variant of the free item it rewrites):

- **R2V2.4** (class b; Part A round 2, section 2 (D12.3)) on `D12.4`. Flagged by the round-2 tabulation (possible, in effect: D12.4); not implemented. Old: D12.4: a holding reached by content-preserving transfers inherits prov part by part (parts = each component with its counterpart binding; a binding newly built gets Con). New: a holding reached by a copy of the carrier's whole content inherits prov(t,o) whole: parts := {t}. The student's copy would inherit its source's provenance and count as an explanation: departs from S41 Q2 (the reply names it).

**Part A variants a free item of this section blocked** (a blocks edge of Part A's map ending at it; a variant of the free item would lift the block):

- e3.19: V3.4 blocks `L403.s3` (computed)
- r2e3.00: R2V3.1 blocks `L403.s3` (computed)

### 3.4 Section B4: rivals, problems, criticism, the class, what would rule it out, and the Arguments (Part VI from L315, Part IX, Parts XIII to XVI)

| id | kind | bears on | through | strong candidate |
|---|---|---|---|---|
| `L315.s1` | sentence | – | – | – |
| `L315.s4` | sentence | – | – | – |
| `L315.s5` | sentence | – | – | – |
| `L315.s7` | sentence | (Suff), (Nec) | D9.8 | – |
| `L315.s8` | sentence | – | – | – |
| `L315.s10` | sentence | (Suff), (Nec) | D9.8 | – |
| `L315.s17` | sentence | (Suff), (Nec) | D9.8 | – |
| `L317.s1` | sentence | – | – | – |
| `L317.s2` | sentence | – | – | – |
| `L317.s3` | sentence | – | – | – |
| `L317.s6` | sentence | – | – | – |
| `L317.s12` | sentence | – | – | – |
| `L317.s15` | sentence | – | – | – |
| `L317.s17` | sentence | – | – | – |
| `L375.s2` | sentence | – | – | yes |
| `L383.s1` | sentence | – | – | yes |
| `L385.s1` | sentence | – | – | yes |
| `L389.s1` | sentence | Expl, (Suff), (Nec) | D9.6 | yes |
| `L397.s5` | sentence | Expl, (Suff), (Nec) | D9.7 | – |
| `L397.s13` | sentence | Expl, (Suff), (Nec) | D9.1, D9.7, D9.8 | – |
| `L487.s1` | sentence | – | – | – |
| `L491.s1` | sentence | – | – | – |
| `L495.s1` | sentence | – | – | – |
| `L499.s1` | sentence | – | – | – |
| `L502.s1` | sentence | – | – | – |
| `L509.s1` | sentence | – | – | – |
| `L517.s1` | sentence | – | – | yes |
| `L520.s3` | sentence | – | – | – |
| `L520.s4` | sentence | – | – | – |
| `L520.s5` | sentence | – | – | – |
| `L526.s2` | sentence | – | – | – |
| `L526.s3` | sentence | – | – | – |
| `L526.s6` | sentence | – | – | – |
| `L526.s9` | sentence | – | – | – |
| `L526.s10` | sentence | – | – | – |
| `L526.s14` | sentence | – | – | – |
| `L528.s1` | sentence | – | – | – |
| `L528.s2` | sentence | – | – | – |
| `L528.s3` | sentence | – | – | – |
| `L528.s4` | sentence | – | – | – |
| `L546.s1` | sentence | – | – | yes |
| `L556.s3` | sentence | – | – | – |
| `L558.s3` | sentence | – | – | – |
| `L562.s2` | sentence | – | – | – |
| `L574.s2` | sentence | – | – | – |
| `L598.s1` | sentence | – | – | – |
| `L604.s1` | sentence | – | – | – |
| `L616.s1` | sentence | – | – | – |
| `L616.s3` | sentence | – | – | – |
| `L622.s2` | sentence | – | – | – |
| `L624.s3` | sentence | – | – | – |
| `L624.s4` | sentence | – | – | – |
| `L626.s5` | sentence | – | – | – |
| `L630.s2` | sentence | – | – | – |
| `D8.1` | definition | – | – | – |
| `D8.4` | definition | – | – | – |
| `D8.6` | definition | – | – | – |
| `D9.3` | definition | Expl, (Suff), (Nec) | – | – |
| `D9.5` | definition | Expl, (Suff), (Nec) | – | – |
| `D9.11` | definition | – | – | formalizes one |
| `D10.1` | definition | – | – | – |
| `D10.2` | definition | – | – | – |
| `D10.4` | definition | – | – | – |
| `D10.5` | definition | – | – | – |
| `D16.1` | definition | – | – | – |
| `D16.2` | definition | – | – | – |
| `E8` | definition | – | – | – |

**Carry-overs from Part A** (class a: ruled to Part B by Part A's records; class b: flagged by Part A round 2's tabulation as changing a FROZEN item, and not implemented; a class-b item may be taken up as a variant of the free item it rewrites):

- **V2.8, its part on L315.s7** (class a; Part A round 1, section 2 (D9.8)) on `L315.s7`. Its part on L315.s7 ruled to Part B by the orchestrator's decision 3; its D16.XV part is round 1's V4.4, computed; edges e2.20, e2.21, claimed only. Old: L315.s7: a candidate is not ruled out for j when no argument usable by j rules it out; X_j(φ) := {α : Usable_j(α) ∧ RO(α,φ)}; ℰ ruled out for j :⟺ X_j('Acc(ℰ)') ≠ ∅. New: ℰ ruled out for j :⟺ ∃α ∈ X_j('Acc(ℰ)') with Acc(ℰ) ∈ Uses(α) (the instance reading, I196). Changes which arguments rule a candidate out; (Suff)'s defeat set grows by arguments reaching ℰ only through another candidate's Acc.

**Part A variants a free item of this section blocked** (a blocks edge of Part A's map ending at it; a variant of the free item would lift the block):

- e2.15: V2.6 blocks `L315.s1`, `L317.s6` (computed)
- e3.33: V3.7 blocks `L375.s2` (computed)
- e4.34: V4.7 blocks `L495.s1` (computed)
- r2e4.11: R2V4.6 blocks `L604.s1` (computed)

## 4. The text, sentence by sentence

Each line: `id | mark | the sentence`, in the order of the text; headings as they stand. A sentence longer than 1,500 characters is cut at a space, the later pieces marked `(cont.)`.


# Claude Fable Semantics


## A structural class of explanatory creativity, with selected and constructed correspondence


# Part 0 — Read this first

`L8.n1` | FROZEN | **Two words, as used here.** An **argument** is reasons why this and not that: something that can be strung together into a coherent structure to decide why this and not another.
`L8.s2` | FROZEN | Each of its steps is of an inference form that the person using it admits (\(\operatorname{Form}_j\), Part IX), and admitting a form, like accepting a claim, is tentative; for that person, while the form stays admitted, the step rules out the case in which its premises are met and its conclusion fails.
`L8.s3` | FROZEN | An argument rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises, in the structural sense of Part IX.
`L8.s4` | FROZEN | An argument is never a reason *for* a claim: what it does is rule out a claim's denial, or a rival, for someone who can use it, and only while it stays usable (K2).
`L8.s5` | FROZEN | A claim that no argument rules out is only not ruled out, and gets nothing from that; a claim whose denial an argument rules out gets nothing more than that ruling out.
`L8.n6` | FROZEN | To **tentatively accept** a claim is a person's choice to go on with it, made for whatever reason; whatever is accepted is accepted tentatively, open to being dropped, and the semantics never defines accepting by the arguments someone holds.
`L8.s7` | FROZEN | A premise of an argument can be a claim tentatively accepted as given, and an argument need not cite a test (Part IX).
`L8.n8` | FROZEN | Nothing in the semantics is settled: whether a candidate meets the conditions of an account depends on the candidate, its question and its target, not on anyone's view of them, and whatever anyone accepts about it is accepted tentatively (Part VI); a theory is never settled.
`L8.n9` | FROZEN | Where a claim taken as given is used to rule out a rival, that ruling out is a choice the person made, not something the claim does by itself.

## What this document claims

`L11.s1` | FROZEN | An explanation is a **question-relevant organization of dependencies**, held to a target by a **transport** that is tested only by **what changes when things are changed**.
`L11.s2` | FROZEN | The definition never asks whether a piece of the explanation "is the same kind of thing" as a piece of the world.
`L11.s3` | FROZEN | That question has no independent content: at any level of detail, a *kind* is nothing over and above how a component responds to the changes that level admits.
`L11.s4` | FROZEN | Two components no admitted change can separate are one kind at that level, whatever labels anyone attaches to them (Part II, Argument 1).
`L13.s1` | FROZEN | Correspondence between a representation and what it represents is not an import here.
`L13.s2` | FROZEN | It is a **relation with a provenance**.
`L13.s3` | FROZEN | A correspondence can be *selected*, produced by variation and survival on a history of encountered changes, with no represented target in that history; or *constructed*, produced by an episode of conjecture and criticism; or merely *declared* by whoever writes the model down.
`L13.s4` | FROZEN | The three are told apart by their histories, not their outputs, and the semantics keeps them apart (Part IV).
`L13.s5` | FROZEN | Creativity lives in construction.
`L13.s6` | FROZEN | Selection produces the raw material construction works on.
`L13.s7` | FROZEN | Declaration is used only as a modelling convenience, and a claim about creativity cannot depend on it.
`L15.s1` | FROZEN | Questions have provenance too.
`L15.s2` | FROZEN | A question, meaning its target, its scope of admitted changes and what it asks, can be found as well as answered, and the semantics represents both (Part III, Argument 5).
`L15.s3` | FROZEN | This is what separates it from any class in which questions are inputs: such a class cannot represent question-finding, and creativity includes finding questions, not only answering them.
`L17.s1` | FROZEN | The **constitutive conjecture** is this: explanatory creativity is fully characterized by (i) organizations and the changes they admit, (ii) transports between organizations tested by change-fidelity alone, (iii) the provenance of those transports and of the questions they serve, and (iv) their physical realization, the instantiation and transformation of these contents in carriers (Part I).
`L17.n2` | FROZEN | A candidate would conflict with the conjecture if an argument not using these four ruled out the claim that it is a non-explanation of its question while these four cannot represent it; so would a candidate that meets \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its question and contract (Part V) when such an argument rules out the claim that it is an explanation there.
`L17.s3` | FROZEN | An argument that exhibits either rules the conjecture out for whoever can use it, while it stays usable.
`L17.s4` | FROZEN | Part XV lists what such an argument would have to exhibit.

## What this document does not claim

`L21.s1` | FROZEN | It does not define reference in terms of uninterpreted matter.
`L21.s2` | FROZEN | It defines reference in terms of matter **plus a selection or construction history**.
`L21.s3` | FROZEN | Physics says what organization a lump of matter instantiates; history says how that organization came to track another.
`L21.s4` | FROZEN | Neither alone yields representation.
`L23.s1` | FROZEN | It does not say prediction is explanation.
`L23.s2` | FROZEN | Fidelity is over **component structure under change**, not over outputs.
`L23.s3` | FROZEN | Two systems with identical outputs and different internal routes are different organizations here, and the semantics says so (Argument 9).
`L25.s1` | FROZEN | It does not supply an aesthetics independent of any declared appraisal, a probability on claims, an appraisal of its own, or a function that orders explanations or thinkers.
`L25.s2` | FROZEN | Where a claim needs one of these, the semantics does not supply it and marks the place: a claim that invokes an appraisal or aesthetic value takes the appraisal relation as an input (Parts XI, XIV), and a claim that needs any of the others is left open (Part XIV).
`L25.s3` | FROZEN | It does not attribute an achievement to contributors beyond what a history contains (Part XI).
`L27.s1` | FROZEN | It does not decide whether any human, machine, institution or lineage belongs to the classes defined.
`L27.s2` | B1 ⟨SC⟩ | It defines the classes.

## What is imported, what is an index, and what is defined

`L31.s1` | FROZEN | The semantics has two imports: the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain, and the **appraisal relation** \(\mathcal N\), taken as an input wherever a question invokes an appraisal.
`L31.s2` | FROZEN | Grain, boundary, continuity and the contract of admitted changes are **declared indices**: every claim is relative to them, and none is a predicate that a case meets or fails.
`L31.s3` | FROZEN | Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the **declared inputs**, in the order Part XIV states.
`L31.s4` | FROZEN | No undefined predicate that says "explains" without a question and a contract, or "is a cause", is taken as an import, and no definition depends on one (Argument 6); (EX) is a defined relation of an episode, not such a predicate.

## Grievances, anticipated

`L35.s1` | FROZEN | Each answer points at the part of the document that carries it; the front matter states nothing the body does not state more exactly.
`L37.s1` | FROZEN | **1. "Without declared kinds you cannot tell a cause from a correlation."** You can, and only this way.
`L37.s2` | FROZEN | A correlation has no component that responds to an intervention on its supposed input; a cause does.
`L37.s3` | FROZEN | That is a difference in edit-response, which is what the semantics asks about (Part II, "Kinds are edit-signatures").
`L37.s4` | FROZEN | A declared label adds no discriminating power: where a separating change exists, fidelity finds it; where none exists, the label asserts a distinction the level does not contain.
`L39.s1` | FROZEN | **2. "So this is operationalism: a thing is what you can do to it."** A *kind* is what a level's admitted changes can distinguish.
`L39.s2` | FROZEN | A *content* is a whole organization, which can contain components that no change at that level separates, and then they are one kind *at that level*, which is what that level contains, not a loss.
`L39.s3` | FROZEN | At a finer level with more admitted changes they may separate.
`L39.s4` | FROZEN | Every kind-claim is indexed to its level.
`L39.s5` | FROZEN | That is scoping, not operationalism.
`L41.s1` | FROZEN | **3. "If correspondences are selected, you have made fidelity a matter of survival."** No. Selection produces a transport.
`L41.s2` | FROZEN | Whether that transport is faithful on changes it was never selected against turns on the transport and the target alone, not on whether it survived.
`L41.s3` | FROZEN | Argument 3 says that a selected transport is underdetermined by its history on an unseen change wherever its population admits a differing survivor there.
`L41.s4` | B1 ⟨SC⟩ | Survival is how the transport got there; fidelity is what it is.
`L43.s1` | FROZEN | **4. "Then everything is relative to a contract of admitted changes, and nothing is independent of the modeller."** A contract is a stated subset of the changes its target admits (Part II), which are changes in whatever the target is, a garden, a mathematical structure or a melody, and not only those anyone could carry out.
`L43.s2` | FROZEN | An account is scoped to its contract and says so.
`L43.s3` | FROZEN | Within any contract, whether a transport is faithful at a pair turns on the transport and the target, and no assessor appears in (E).
`L43.s4` | FROZEN | A contract that quietly excludes changes its target admits to protect an account is not caught by a rule about intentions; it is caught by the requirement that the exclusion be stated (non-vacuity, Part V), and then by any criticism that supplies the excluded change.
`L43.s5` | FROZEN | What is independent of the modeller lies in the target and in fidelity; what the modeller chose to leave out lies in the stated scope, and so in the record.
`L45.s1` | FROZEN | **5. "This is teleosemantics, structural realism or functionalism with new words."** It shares commitments with each and differs from each.
`L45.s2` | FROZEN | From teleosemantics it takes the idea that a correspondence has a history; it differs by distinguishing selected from constructed histories and locating creativity only in the latter.
`L45.s3` | FROZEN | From structural realism it takes structure-preservation; it differs by making preservation change-driven and component-level, and by refusing a global isomorphism requirement.
`L45.s4` | FROZEN | From functionalism it takes substrate-independence; it differs by imposing physical realization conditions at every attribution.
`L45.s5` | FROZEN | Whether the combination is new is a question about the literature.
`L47.s1` | FROZEN | **6. "You have replaced explanation with evolution."** Selection appears at the bottom: in the arrangement Part IV describes, as one possibility and not a requirement, it produces the object layer of persistent things that explanation operates on.
`L47.s2` | B1 ⟨SC⟩ | Construction is a separate provenance with a separate trace, and every creative attribution requires it.
`L47.s3` | FROZEN | Nothing about construction is reduced to selection; Part IV keeps the two apart by what their histories contain, and Part XV names what an argument would have to exhibit to rule that out.
`L49.s1` | FROZEN | **7. "Mathematics has no interventions."** An admitted change need not be a physical intervention.
`L49.s2` | FROZEN | Removing a starting assumption, dropping a constraint or changing a dimension are edits on an organization, and fidelity under them is well defined.
`L49.n3` | FROZEN | A piece of mathematics explains, relative to a question, when \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (Part VII, D16.XV).
`L49.s4` | FROZEN | The same goes for a melody, where changing a note or a chord is an edit, and for a philosophical claim, where dropping a premise or a distinction is one.
`L49.s5` | FROZEN | Whether anyone could carry an edit out in a physical system bears on testing and building (Part XII), not on whether a candidate meets (F1), (F2) and (A) there, or (E) on a contract that contains it.
`L51.s1` | B1 ⟨SC⟩ | **8. "Where is aesthetics?"** In Part XI, as a declared appraisal relation.
`L51.s2` | FROZEN | Artistic effect, artistic purpose and aesthetic reasons get three distinct relations, and none is defined as another.
`L51.s3` | FROZEN | The semantics does not decide between rival aesthetic reasons.
`L53.s1` | FROZEN | **9. "'Selected' is as much a stipulation as 'is a cause'."** Selection is a physical history: a population, a variation operator, a survival condition and a sequence of events (Parts IV, XII).
`L53.s2` | FROZEN | Whether it occurred is a claim about the physical module, fallible as any claim about it is (Part XII).
`L53.s3` | FROZEN | A kind-label is not a claim about anything.
`L55.s1` | FROZEN | **10. "Freezing the question for assessment while letting questions change across episodes is having it both ways."** It is, deliberately, and the two ways are indexed so they cannot be confused.
`L55.s2` | FROZEN | An assessment is an event with a frozen contract.
`L55.n3` | FROZEN | An episode is a history in which every change \(C\to C'\) carries a provenance record (D13.8).
`L55.s4` | FROZEN | Argument 7 rules out a conflict between them, for whoever can use it.
`L57.s1` | B1 | **11. "Kinds exist. A rule is not a cause."** A rule and a cause differ in how they respond to changes: a rule's application changes when the rule is edited and not when the world is intervened on; a cause's assignment changes under intervention.
`L57.s2` | FROZEN | That is a difference in edit-signature (Part II), and the semantics represents it exactly.
`L57.s3` | FROZEN | What it denies is that the difference is available before the admitted changes are fixed, or independently of them.

## Where to attack this

`L61.s1` | FROZEN | The claims the rest depends on, in the order of how much falls if they fail, are stated exactly in Part XV together with what an argument would have to exhibit to rule out each.
`L61.n2` | FROZEN | In short: (Suff) sufficiency of \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (D16.XV); (Nec) necessity (D16.XV); (Elim) the eliminability of kinds; (Prov) the two provenances and the underdetermination of selected transports at unseen changes where their population admits a differing survivor; (QF) the representability of question-finding.
`L61.s3` | FROZEN | Anything else is a detail.

# Part I — Commitments

`L67.s1` | B1 | **Faithfulness without assessors.** Whether a transport is faithful on a contract is independent of whether anyone tentatively accepts it.
`L67.s2` | FROZEN | Systems can be in error about their transports, their observations, their criticisms and their own capacities.
`L69.s1` | FROZEN | **Fallibility without error-as-work.** A theory may contain a faithful scoped dependence together with errors elsewhere.
`L69.s2` | FROZEN | What cannot count as explanation is an error in the very dependence alleged to do the work.
`L69.n3` | FROZEN | "Explanation" in this commitment means an explanatory candidate meeting \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its contract (Part V, D16.XV); a theory in error offered as an answer is an explanatory candidate, which ordinary usage may still call an explanation, and whether an account is easy to vary is a separate matter (Part VI).
`L71.s1` | FROZEN | **Conjecture, criticism, action.** An idea may be entertained with no argument that rules out its rivals.
`L71.s2` | FROZEN | A criticism has a target and is itself conjectural.
`L71.s3` | FROZEN | A thinker may act on an appraisal that no argument has decided.
`L73.s1` | FROZEN | **Recursive scrutiny with operative return.** Any aspect of a system's practice, a question, a contract, a transport, a method, an attention policy, can become a target, and the result must be able to change how the system proceeds.
`L75.s1` | FROZEN | **Substrate independence with physical conditions.** Any carrier may bear an organization.
`L75.s2` | FROZEN | Every attribution of an organization to a physical system is a claim that the system instantiates it, and whether a system can is a matter of physics; here and throughout, to adopt something is to take it tentatively, open to replacement, and an attribution that the adopted physics excludes conflicts with it, as a candidate can conflict with a claim (Part VI).
`L75.s3` | FROZEN | That an organization admits an edit is not a claim that the edit can be carried out or can come about, so an attribution does not conflict with a physics that excludes carrying out an edit the attributed organization admits (Parts II and III).
`L75.s4` | FROZEN | Which organizations a carrier can bear, and whether what carriers of one physical medium bear can pass to carriers of another, are matters of physics as well, and substrate independence reaches as far as contents can pass between media.
`L75.s5` | FROZEN | Where two media cannot exchange what they bear, the contents that only one of them can bear form, for a system built of the other, a barrier in the sense of Part XIII.
`L75.s6` | FROZEN | Physical possibility enters the semantics where a content is instantiated in a carrier or transformed, as when it is held, copied, taught, tested, built or performed (Parts IV and X to XIII), and it also enters as the content of claims that a candidate can conflict with (Part VI).
`L75.s7` | FROZEN | It does not define a question, its range of changes, an account or a conflict between candidates (Parts III, V, VI).
`L77.s1` | FROZEN | **Two provenances, not one.** Selection and construction both produce correspondences.
`L77.s2` | FROZEN | They are distinguished by their histories.
`L77.s3` | FROZEN | Neither is reduced to the other.

# Part II — Organizations and their changes


## Organizations

`L85.s1` | FROZEN | An organization is
`L87.s1` | B1 ⟨E Dec Expl Suff Nec⟩ | \[ D=(V,(X_v)_{v\in V},J,B,A,L). \]
`L91.s1` | B1 ⟨E Dec Expl Suff Nec⟩ | \(V\) is a set of ports, each with a nonempty value domain \(X_v\).
`L91.s2` | B1 ⟨E Dec Expl Suff Nec⟩ | A valuation is an element of \(X_D=\prod_v X_v\).
`L91.s3` | B1 ⟨E Dec Expl Suff Nec⟩ | \(J\) indexes components; each component \(j\) has a footprint \(V_j\subseteq V\).
`L91.s4` | B1 ⟨E Dec Expl Suff Nec⟩ | \(B\) is a set of boundary conditions.
`L91.s5` | B1 ⟨E Dec Expl Suff Nec⟩ | \(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\).
`L91.s6` | B1 ⟨E Dec Expl Suff Nec⟩ | For each \(j\), edit \(a\), and boundary \(b\), the interpretation supplies
`L93.s1` | B1 ⟨E Dec Expl Suff Nec⟩ | \[ L_j(a,b)\subseteq\prod_{v\in V_j}X_v . \]
`L97.s1` | FROZEN | The compatible valuations are
`L99.s1` | B1 ⟨E Dec Expl Suff Nec⟩ | \[ \operatorname{Sol}_D(a,b)=\{z\in X_D:\forall j\in J,\ z|_{V_j}\in L_j(a,b)\}. \tag{O} \]
`L103.s1` | B1 ⟨E Dec Expl Suff Nec⟩ | A deleted component imposes the full relation on its ports.
`L103.s2` | B1 | An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one.
`L103.s3` | B1 | A changed rule is a changed component.
`L105.s1` | FROZEN | Values of ports may be paths, functions, fields, mathematical structures or histories.
`L105.s2` | B1 ⟨E Dec Expl Suff Nec⟩ | Cyclic constraints are admitted.
`L105.s3` | B1 ⟨E Dec Expl Suff Nec⟩ | Several solutions remain several.

## Roles are defined, not supplied

`L109.s1` | B1 | No role assignment is supplied.
`L109.s2` | B1 | A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly.
`L109.s3` | B1 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).
`L109.n4` | FROZEN | A port \(o\) is an **observation** when \(\exists a\in\operatorname{Alt}_j\setminus\operatorname{Slc}_j,\ m\in V_j\setminus\{o\}\) with \(\operatorname{asg}(m)\) defined and \(L_{\operatorname{asg}(m)}(a,\cdot)=L_{\operatorname{asg}(m)}(1,\cdot)\), where \(j=\operatorname{asg}(o)\) (D2.4, D2.6).
`L109.s5` | B1 | The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read.

## Kinds are edit-signatures

`L113.s1` | B1 ⟨SC⟩ | Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).
`L113.s2` | B1 ⟨SC⟩ | The **signature** of component \(j\) on \(C\) is
`L115.s1` | B1 ⟨E Dec Expl Suff Nec SC⟩ | \[ \operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K} \]
`L119.s1` | FROZEN | Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide.
`L119.s2` | FROZEN | A kind is an equivalence class of components under this relation.
`L119.s3` | FROZEN | For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\pi\) translates valuations, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV).
`L119.n4` | FROZEN | A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau,\sigma\) and \(\tau',\sigma'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense.
`L119.n5` | FROZEN | Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau,\sigma\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
`L119.s6` | FROZEN | Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract.
`L119.s7` | FROZEN | A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called.
`L119.n8` | FROZEN | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and \(j\sim_C j'\) by \(\beta\) with \(\beta_*L_j(x)=L_{j'}(x)\) gives \(j\sim_{C\cup\{x\}}j'\) (FC05).
`L121.s1` | FROZEN | What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:
`L123.n1` | FROZEN | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;
`L124.s1` | B1 ⟨SC⟩ | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;
`L125.s1` | B1 ⟨SC⟩ | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.
`L127.n1` | FROZEN | These are functions of \((D,C)\) (D4.6, FC13), not additional data.
`L127.s2` | B1 ⟨SC⟩ | The semantics never asks whether a component "is" a cause.
`L127.s3` | B1 ⟨SC⟩ | It asks what its signature is.
`L127.n4` | FROZEN | In particular, \(m\in V_j\land\operatorname{asg}(m)\notin\{j,\text{undefined}\}\land\operatorname{Changes}_C(j,A\setminus\operatorname{Slc}_j)\Rightarrow\operatorname{Meas}_C(j,m)\) (D4.6, FC4.new1).
`L127.s5` | FROZEN | Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording.

# Part III — Questions


## Contracts

`L135.s1` | FROZEN | A question is
`L137.s1` | B1 ⟨E Dec Expl Suff Nec⟩ | \[ p=(D,\ C,\ b_0,\ \mathcal Q,\ O_p,\ \rho_p). \]
`L141.s1` | FROZEN | \(D\) is the target.
`L141.s2` | B1 ⟨E Dec Expl Suff Nec⟩ | The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over; it contains the baseline \((1,b_0)\).
`L141.n3` | FROZEN | \(\mathcal Q\) is a specified set-theoretic operation on \(D\), its solutions and its component structure, with codomain \(Y_p\cup\{\bot\}\) (D3.2).
`L141.s4` | FROZEN | The answer profile is
`L143.s1` | B1 ⟨E Dec Expl Suff Nec⟩ | \[ \operatorname{Ans}_p(a,b)=\mathcal Q(D,a,b). \tag{Q} \]
`L147.s1` | B1 ⟨E Dec Expl Suff Nec⟩ | \(O_p\) is the set of aims being addressed or protected.
`L147.s2` | B1 ⟨E Dec Expl Suff Nec⟩ | \(\rho_p\) is the **provenance** of the contract (below).

## The respect is the query

`L151.s1` | FROZEN | What a question asks, production, identification, obstruction, rule-status or purpose-achievement, is fixed by the type of \(\mathcal Q\) and the shape of \(C\), not by a label.
`L151.s2` | B1 | A production question has a \(\mathcal Q\) that reads an output port and a \(C\) containing interventions on upstream ports.
`L151.n3` | FROZEN | An identification question has a \(\mathcal Q\) that computes a fibre and \(\exists(a,b),(a',b')\in C:\ \operatorname{obs}(a,b)\neq\operatorname{obs}(a',b')\) (D3.3).
`L151.s4` | FROZEN | An obstruction question has a \(\mathcal Q\) that returns reachable or unreachable.
`L151.s5` | FROZEN | The rule-status and purpose-achievement cases are given with constitutive rules (Part VII) and with achievement, (AR) (Part XI).
`L151.n6` | FROZEN | Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and \(\operatorname{Acc}(\mathcal E,p)\not\Rightarrow\operatorname{Acc}(\mathcal E,p')\) (FC34).
`L151.s7` | FROZEN | A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question; whether the measured part also produces the outcome is the production question, and the first answer is not the second.

## Contracts have provenance

`L155.s1` | FROZEN | \(\rho_p\in\{\text{declared},\ \text{selected},\ \text{constructed}\}\), with the trace required by Part IV.
`L155.s2` | FROZEN | A **declared** contract is stipulated by the modeller, with neither selection nor construction in its history; this is its provenance, and not the sense in which every contract, whatever its provenance, is a declared index of the claims made on it (Part XIV).
`L155.s3` | FROZEN | A **selected** contract is the surviving member of a population under a variation-and-survival history.
`L155.s4` | FROZEN | A **constructed** contract is the result of an episode with a construction trace.
`L155.s5` | FROZEN | Any assessment may use any of the three.
`L155.s6` | B1 | A claim that an episode *found* a question requires \(\rho_p=\text{constructed}\) for the contract in question, with the trace.

## Scope, and a question that can be in error

`L159.s1` | FROZEN | A contract is a stated subset of the changes its target admits (Part II), and a stated scope is what makes it one.
`L159.s2` | FROZEN | Those are the changes the question asks about, in whatever the target is: a garden, a mathematical structure, a melody or a philosophical claim.
`L159.s3` | FROZEN | For a physical target they are changes in what the target itself is and does, as its attributed organization admits them (Part II), and admitting a change is not a claim that it can be carried out or come about; whether anyone could carry a change out, or whether it could come about, is a matter of instantiation and transformation (Part XII), which bears on testing and building and does not by itself put a change in a contract or keep it out.
`L159.s4` | FROZEN | An account at a stated scope answers the question asked at that scope; it does not answer a broader question that failed, and a narrowing adopted after a failure is a new claim at a new index (Part VIII).
`L159.s5` | FROZEN | Why the question asked is answered on this restriction and not on a wider one is a substantive, criticizable part of the claim; the semantics records the restriction and supplies no rule that decides it.
`L159.s6` | FROZEN | Meeting the conditions of an account (Part V) on the restricted contract leaves open why the claim is made on this restriction and not on a wider one.
`L159.s7` | FROZEN | Where the claim states why it restricts the contract as it does, an assessment of the restriction is given with that statement; where it states none and an assessment turns on one, that statement is a missing declared input (Part XIV).
`L161.s1` | B1 ⟨SC⟩ | A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.
`L161.s2` | B1 ⟨SC⟩ | Its formulation is still an event.
`L161.s3` | B1 ⟨SC⟩ | Exposing the defect is another question with its own contract.
`L161.s4` | FROZEN | An assessment is an event with a frozen contract (Part 0, grievance 10): a change to \(C\) or \(\mathcal Q\) during it, left unrecorded, makes the record name a claim other than the one assessed.
`L161.s5` | FROZEN | Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one.

# Part IV — Layers, transports, and provenance


## Occurrences and contents

`L169.s1` | B3 ⟨Expl Suff Nec⟩ | An **occurrence** is a physically located carrier.
`L169.s2` | B3 ⟨Expl Suff Nec⟩ | A **content** is an organization together with its contract-relative commitments.
`L169.s3` | B3 ⟨Expl Suff Nec⟩ | Occurrences are not identified by carrying the same words; contents are not identified by having the same outputs.

## The object layer and the simulation layer

`L173.s1` | FROZEN | A modelled thinker has at least two organizations in play.
`L175.s1` | FROZEN | The **object layer** \(P\) is an organization whose ports are persistent things with boundaries and identity, whose components are their continuity relations, and whose admitted edits include displacement, occlusion and re-identification.
`L175.s2` | FROZEN | It is the layer at which there are *objects* rather than a field of sensation.
`L177.s1` | B3 | The **simulation layer** \(S\) is an organization over \(P\) whose components are dependencies among things and whose queries are predictions: what a port of \(P\) will take under an admitted edit.
`L177.s2` | FROZEN | \(S\) is where prediction lives.
`L179.s1` | FROZEN | Neither layer is presupposed to exist in any particular physical system.
`L179.s2` | FROZEN | The semantics describes what it is for them to exist and to be connected.

## Transports

`L183.s1` | FROZEN | A transport from an organization \(D\) to an organization \(E\) is
`L185.s1` | B2 ⟨E Expl Suff⟩ | \[ t=(\pi,\tau,\sigma,\lambda) \]
`L189.s1` | B2 ⟨E Expl Suff⟩ | where \(\pi:X_D\to X_E\) on the stated scope, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation.
`L189.s2` | B2 ⟨Dec Expl Suff Nec⟩ | A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V.

## Three provenances

`L193.s1` | FROZEN | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:
`L195.s1` | B3 ⟨Dec Expl Suff Nec⟩ | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).
`L195.s2` | FROZEN | The transport \(t\) is a member of \(\mathcal T\) that survived.
`L195.s3` | FROZEN | A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival.
`L195.n4` | FROZEN | \(\neg[\exists o\prec_{h(t)}o_t,\ x\in\{t,\ H,\ \text{survival condition},\ \operatorname{cod}t\}:\ \operatorname{Rep}(o,x)]\land\neg[\exists h'\subseteq h(t):\ \operatorname{CT}(h',t)]\) (D12.1).
`L195.s5` | B3 ⟨Dec Expl Suff Nec⟩ | Write \(\operatorname{Sel}(t;\mathcal T,\mu,H)\).
`L195.s6` | FROZEN | The population \(\mathcal T\) is part of the claim: what \(H\) leaves open about \(t\) is what \(\mathcal T\) leaves open (Argument 3).
`L197.s1` | FROZEN | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target.
`L197.s2` | FROZEN | Write \(\operatorname{Con}(t;h,e)\).
`L199.s1` | B3 ⟨Dec Expl Suff Nec⟩ | **Declared.** Neither of the above.
`L199.s3` | B3 ⟨Dec Expl Suff Nec⟩ | Write \(\operatorname{Dec}(t)\).
`L201.s1` | FROZEN | A physical system may hold selected transports at the object layer and constructed transports at the simulation layer; that is one arrangement, not a requirement.
`L201.s2` | B3 | Construction may operate on selected material.
`L201.s3` | B3 | Selection may continue to operate beneath construction.
`L201.n4` | FROZEN | Neither provenance is reducible to the other: (D12.1, D12.2).

## Representation is defined, not supplied

`L205.s1` | FROZEN | An occurrence \(o\) **represents** content \(c\) at grain \(\ell\) when there is a transport from the organization that \(o\) instantiates under the physical module, at grain \(\ell\), to \(c\), faithful on \(c\)'s contract, whose provenance is selected or constructed; in (R), \(\operatorname{Sel}(t)\) and \(\operatorname{Con}(t)\) abbreviate \(\operatorname{Sel}(t;\mathcal T,\mu,H)\) and \(\operatorname{Con}(t;h,e)\) for some such parameters:
`L207.s1` | B3 ⟨Dec Expl Suff Nec⟩ | \[ \operatorname{Rep}_\ell(o,c)\iff\exists t\,[\operatorname{Faithful}_C(t:\operatorname{Org}_\ell(o)\to c)\land(\operatorname{Sel}(t)\lor\operatorname{Con}(t))]. \tag{R} \]
`L211.s1` | FROZEN | The carrier–content relation is thus a fidelity relation with a history.
`L211.s2` | FROZEN | A system can represent a theory in error: the transport from carrier to content is faithful while the transport from the content's target to the content fails.
`L211.s3` | FROZEN | A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does.
`L211.s4` | FROZEN | A carrier keeps its provenance when present access to it is lost, and a later record made from the carrier carries that provenance, not a second, independent one.
`L213.s1` | FROZEN | The one thing (R) takes from outside is \(\operatorname{Org}_\ell(o)\): which organization a physical occurrence instantiates at a grain.
`L213.s2` | FROZEN | That is supplied by the physical module, not by the semantics.

## Prediction, surprise, violation

`L217.s1` | FROZEN | Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\).
`L217.s2` | B3 ⟨Dec Expl Suff Nec SC⟩ | For an edit–boundary pair \((a,b)\in C\) actually occurring:
`L219.s1` | B3 ⟨SC⟩ | - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
`L220.n1` | FROZEN | - a **violation** occurs when \(\neg(\text{F1 at }(a,b)\land\text{F2eq at }(a,b))\) (D12.7);
`L221.n1` | FROZEN | - **surprise** is a violation of a selected transport at \((a,b)\notin H\).
`L223.s1` | FROZEN | A system with no transport cannot be surprised.
`L223.s2` | FROZEN | A system whose history exhausts its contract cannot be surprised.
`L223.s3` | FROZEN | Surprise requires an incomplete selection history: the contract must contain changes the system's correspondence was never shaped against, and one of them must occur (Argument 4).
`L223.s4` | FROZEN | Whether the correspondence could have been otherwise at such a change turns on its population (Argument 3).
`L223.n5` | FROZEN | Prediction and violation are defined for every transport to the simulation layer, surprise only for a selected one: a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
`L225.s1` | B3 ⟨SC⟩ | Two responses to a violation are distinguished.
`L225.s2` | FROZEN | A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population.
`L225.s3` | B3 | A **construction response** introduces a new organization or a new transport with a construction trace.
`L225.s4` | B3 ⟨SC⟩ | Only the second can be originative under Part X.

# Part V — Account

`L231.s1` | FROZEN | An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\).
`L231.s2` | FROZEN | The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI.
`L231.s3` | FROZEN | The candidate together with its question, \(\mathcal E=(E,p,t,\Gamma)\), meets \(\operatorname{Account}(\mathcal E)\) exactly when the following four conditions are met, each a condition on supplied relations under the changes in \(C\).
`L231.s4` | FROZEN | Where an organization \(E'\) is obtained from \(E\) by a declared operation (Part VI), \(\operatorname{Account}(E',p)\) abbreviates \(\operatorname{Account}\big((E',p,t',\Gamma')\big)\), with \(t'\) the transport the operation carries \(t\) to and \(\Gamma'\) the commitments it leaves; for \(E|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E|W\), and \(\Gamma'\) is \(W\).
`L233.s1` | FROZEN | **Component fidelity.** For every active component \(k\) of \(E\) with counterpart subnetwork \(\lambda(k)\subseteq D\), and every \((a,b)\in C\), the relation obtained by imposing the constraints of \(\lambda(k)\), projecting away its hidden ports and carrying what remains to \(V_k\) by the port translation of \(\lambda\) (write \(\operatorname{proj}^{\lambda}_{V_k}\) for this projection) equals the component relation of \(k\) under the translated edit:
`L235.s1` | FROZEN | \[ \operatorname{proj}^{\lambda}_{V_k}\!\big[\operatorname{Sol}_{\lambda(k)}(a,b)\big]=L_k(\tau(a),\sigma(b)). \tag{F1} \]
`L239.s1` | FROZEN | And the assembled organization agrees:
`L241.s1` | B2 ⟨E Dec Expl Suff Nec⟩ | \[ \pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b)),\qquad \tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1). \tag{F2} \]
`L245.s1` | B2 ⟨Dec Expl Suff Nec⟩ | (F1) prevents an assembled match from hiding a decomposition in error.
`L245.s2` | B2 ⟨Dec Expl Suff Nec⟩ | (F2) prevents a set of pieces each faithful locally from hiding a lost shared constraint.
`L245.s3` | B2 ⟨Dec Expl Suff Nec⟩ | Together they are fidelity at every level the contract reaches.
`L245.s4` | FROZEN | By (K), no component of \(E\) whose signature on \(C\) differs from its counterpart's meets (F1); there is no further condition about kinds to state (Argument 1).
`L247.s1` | B2 ⟨Dec Expl Suff Nec⟩ | **Question fidelity.** For every \((a,b)\in C\),
`L249.s1` | B2 ⟨E Expl Suff Nec⟩ | \[ \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A} \]
`L253.s1` | B2 ⟨E Dec Expl Suff Nec⟩ | The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one.
`L255.n1` | FROZEN | **\(\operatorname{Dependence}\).** The answer follows by evaluating \(E\) under its boundary conditions.
`L255.n2` | FROZEN | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that \(\operatorname{Ans}_E(\tau(a),\sigma(b))\neq\operatorname{Ans}_E(1,\sigma(b_0))\) (D6.4), and this contrast is lost when the components of \(G\) are deleted from \(E\) (a deleted component imposes the full relation on its ports, Part II): evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.
`L257.s1` | FROZEN | **Non-vacuity.** \(\operatorname{Sol}_D(1,b_0)\neq\varnothing\).
`L257.n2` | FROZEN | \(C\subseteq A\times B\) and \((A\times B)\setminus C\subseteq\operatorname{Excl}(\Sigma)\) (D3.5).
`L257.n3` | FROZEN | A contract consisting only of relabelings (D6.9), or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets (F2), (A) and \(\operatorname{Dependence}\) (FC21), and is therefore not a contract on which an account can be claimed.
`L259.s1` | FROZEN | Thus
`L261.n1` | FROZEN | \[ \operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{Dependence}\land\text{NonVacuous}. \tag{E} \]
`L265.n1` | FROZEN | Every conjunct but \(\operatorname{Stated}(C,\Sigma)\) (D3.5, D6.6) is a condition on how supplied relations behave under the changes in \(C\).
`L265.s2` | B2 | None inspects a label.

## What (E) excludes, and what it does not

`L269.n1` | FROZEN | A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under \(C\) when \((1,b),(a,b)\in C\) and \(\operatorname{proj}^{\lambda}_{V_k}[\operatorname{Sol}_{\lambda(k)}(a,b)]\neq\operatorname{proj}^{\lambda}_{V_k}[\operatorname{Sol}_{\lambda(k)}(1,b)]\) for a component \(k\) of it (FC25).
`L269.s2` | FROZEN | A table that encodes an organization's response to every admitted change is not a table in that sense: it meets (F1) as a decomposition does, and it is an account when it meets the other conjuncts of (E).
`L269.s3` | FROZEN | The word "table" fixes nothing; the response under the admitted changes does.
`L271.s1` | FROZEN | A **reversed calculation**, identification presented as production, fails (F2) under the production contract: intervening on the upstream port changes the target's downstream value but not the calculation's.
`L271.s2` | FROZEN | It may be faithful under the identification contract, which is a different question (Part III).
`L273.n1` | FROZEN | (D6.3, FC23, FC24).
`L275.n1` | FROZEN | A candidate whose only substantive contrast is one that no edit the target admits realizes has no pair of \(C\) at which the contrast appears, and fails \(\operatorname{Dependence}\).
`L275.s2` | FROZEN | A contrast that no one could produce, or that could not come about, is still a contrast of its question when the target admits the edit that realizes it; whether it can be produced bears on testing (Part XII), not on (E).
`L277.s1` | FROZEN | (E) has no condition on how a mechanism came to be guessed: a mechanism meets (E) or fails it whatever led anyone to guess it, and how it came to be taken up is assessed elsewhere (Part IX).
`L277.s2` | FROZEN | It draws no line between two candidates with the same fidelity that differ only in elegance: both meet it or both fail it.
`L277.s3` | FROZEN | It does not exclude a coarse dependence for omitting finer workings or an instrument: an account at a coarse grain is an account of the coarse question, and what it answers is fixed by its contract, not by what a finer contract would add.
`L277.s4` | FROZEN | A mathematical argument answering "why does this follow under these rules?" meets (E) for that question without answering "what caused this?"; depth is question-relative and (E) measures none of it.

## Why there is no counterpart-kind condition

`L281.s1` | FROZEN | A separate condition, "each component of \(E\) must be tied to a component of \(D\) *of the same kind*", would be either redundant or unevaluable.
`L281.s2` | FROZEN | Where \(C\) contains a change separating two kinds, (F1) already fails for a component whose counterpart is of the other kind.
`L281.s3` | B2 | Where \(C\) contains no such change, the two are one kind on \(C\) by (K), and the condition would be asserting a distinction that \(C\) does not contain.
`L281.s4` | B2 | There is no third case.
`L281.s5` | FROZEN | Argument 1 makes this exact.

# Part VI — Work, routes, and interference

`L287.s1` | B2 | Fix \(\mathcal E\) and a declared restriction operation.
`L287.s2` | FROZEN | For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).
`L287.s3` | FROZEN | Define
`L289.s1` | B2 | \[ \mathsf S_{E,p}=\{W\subseteq\Gamma:\operatorname{Account}(E|W,p)\}. \tag{S} \]
`L293.s1` | B2 | No upward closure and no minimal member are assumed.
`L293.s2` | FROZEN | For nonempty \(B\subseteq W\),
`L295.s1` | B2 | \[ \operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}. \tag{B} \]
`L299.s1` | B2 | A block may be critical while no singleton in it is.
`L299.s2` | FROZEN | Criticality is relative to the route \(W\) it is assessed in, a **route** of the candidate being a member of \(\mathsf S_{E,p}\) (not an active route of a history, Part IX): a commitment critical in one route need not be critical in the full candidate, and the routes assessed are subsets of the written \(\Gamma\), whether or not anyone has set them out, not a route someone could write with commitments outside \(\Gamma\).
`L299.s3` | FROZEN | For a declared family \(\mathcal V\) of organization edits,
`L301.s1` | B2 | \[ \operatorname{Boundary}_{E,p}=\{(v,w)\in\mathcal V^2:\operatorname{Account}(E_v,p)\neq\operatorname{Account}(E_w,p)\}. \tag{D} \]
`L305.s1` | FROZEN | **Finite monotone claim.** If \(\Gamma\) is finite, \(\mathsf S\) is upward closed, and \(\Gamma\in\mathsf S\), then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\), and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\), exactly when \(d\in\bigcap\min\mathsf S\).
`L305.s2` | FROZEN | *Why this and not its denial.*
`L305.s3` | FROZEN | A member of a minimal route is critical for it.
`L305.s4` | FROZEN | If \(d\) is critical for \(W\), finiteness gives a minimal \(U\subseteq W\); if \(d\notin U\), upward closure makes \(W\setminus\{d\}\) a route.
`L305.s5` | FROZEN | Deletion of \(d\) from \(\Gamma\) leaves \(\Gamma\setminus\{d\}\) a route exactly when a minimal route omits \(d\). ∎ The claim applies only where its assumptions are met; an addition to \(\Gamma\) that stops a route being one is the interference case below, and there upward closure fails.
`L307.s1` | B2 | **Redundant routes.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\},\{b\},\{a,b\}\}\): each is contributory, neither indispensable.
`L307.s2` | FROZEN | Two systems with the same output table may differ in which routes are active; the semantics represents the difference (Argument 9).
`L307.s3` | FROZEN | A route of the candidate is a route whether or not any history runs it; it is active in a system when occurrences that realize it form an active route (Part IX), a subnetwork of actual occurrences in the system's history.
`L307.s4` | FROZEN | The two meet in \(\operatorname{ProducedBy}\) (Part XI), which attributes a repair to the contributions whose active routes ran to it, not to the routes a candidate contains.
`L307.s5` | FROZEN | A route already present in the candidate is a route whether or not anyone has described its work; a component reassigned to a new target after a deletion belongs to a new candidate with its own assessment, and whether the new candidate meets (E) is not whether the old one does.
`L309.s1` | B2 | **Interference.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\}\}\): the full candidate fails (E) although a subset meets it.
`L309.s2` | FROZEN | A subset can meet (E) while the whole fails it; \(b\) is not made "not a commitment" to repair this.
`L311.s1` | FROZEN | **Infinitary routes.** \(\Gamma=\{d_n:n\in\mathbb N\}\), \(d_n\) the constraint \(|x|\le 1/n\): every set of indices unbounded in \(\mathbb N\) determines \(x=0\); no minimal route, and no route of one commitment, exists.
`L311.s2` | B2 ⟨SC⟩ | (B) records the collective contribution.
`L313.s1` | FROZEN | **Commitments that do no work.** (E) has no condition that each commitment do work.
`L313.s2` | FROZEN | A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no route (B).
`L313.n3` | FROZEN | When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary routes; FC40 (c)).
`L315.s1` | B4 | **Rivals.** Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it.
`L315.n2` | FROZEN | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ (D8.2), or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both, as none do when two of their active components with one counterpart have different relations there (D8.new1).
`L315.s3` | FROZEN | Whether two candidates conflict depends on their organizations and transports and on the target's ports and components, not on anyone's view of them; it is found by argument, with no test, and it does not turn on what any physics admits (Part I).
`L315.s4` | B4 | A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\); outside \(C\) it claims nothing on \(p\), but what its organization and transport give there can conflict with what another's give.
`L315.s5` | B4 | Two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are, conflict at no pair (Part VIII, Recoding; Argument 8), and nor do two candidates, however differently they are cut, that some such relations of the target would let both meet (F1), (F2) and (A) at each admitted pair both translate; neither pair is a pair of rivals.
`L315.s6` | FROZEN | A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out, and a candidate is ruled out for \(j\) when the claim that it meets (E) is; by (K3), an argument from a test's record rules out a candidate only together with the background and instruments of that test.
`L315.s7` | B4 ⟨Suff Nec⟩ | A candidate is **not ruled out** for \(j\) when no argument usable by \(j\) rules it out.
`L315.s8` | B4 | No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, and a candidate that nobody has offered is no one's rival.
`L315.s9` | FROZEN | Nor are rivals a selection population: whether a selected transport is underdetermined at an unseen pair is fixed by its population (Argument 3), whatever rivals anyone offers.
`L315.s10` | B4 ⟨Suff Nec⟩ | **Conflict with a claim.** A candidate can conflict with a claim as well as with a rival.
`L315.n11` | FROZEN | A candidate **conflicts with** a claim \(\chi\) at an admitted pair of the target that its transport translates, in \(C\) or outside it, when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there (D8.5).
`L315.s12` | FROZEN | \(\chi\) need not be an explanation or come with one, and it may be a claim about what is possible or impossible: the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion.
`L315.s13` | FROZEN | Such a conflict is found by argument, with no test against the target: an argument that rules out, for whoever can use it, that what the candidate gives there is something \(\chi\) allows (Part IX).
`L315.s14` | FROZEN | Where the pair is in \(C\), that argument rules out that the candidate meets (E) for any assessor \(j\) who can use it, and so who tentatively accepts \(\chi\) (K2); outside \(C\) it rules out that the target gives there what the candidate's organization gives, not the candidate's meeting (E) on \(p\).
`L315.s15` | FROZEN | Either way the argument needs the premise that \(\chi\) speaks of the target under that pair's edit.
`L315.s16` | FROZEN | Where the edit is itself one that \(\chi\) excludes, as when a question asks what a pendulum does with its friction component deleted, the target so edited may itself give a motion that never stops, and without that premise the argument rules out no candidate there; the candidate still conflicts with \(\chi\).
`L315.s17` | B4 ⟨Suff Nec⟩ | The conflict does not by itself say which to drop, the candidate, \(\chi\) or another premise of the argument: which one the person goes on with is the person's choice (Part 0), and using \(\chi\) as a premise gives \(\chi\) nothing.
`L315.n18` | FROZEN | Nor is the conflict enough to do anything about it: ruling the candidate out by \(\chi\) is already doing something about it, and is a choice the person made in taking \(\chi\) as given, not something \(\chi\) does by itself; a response that changes the candidate, the claim or the question is construction and repair (Parts X, XI); and \(\chi\) alone does not say where the candidate is in error.
`L315.s19` | FROZEN | A conflict with a claim that a system represents can be a recognized difficulty (Part X), as when keeping the candidate meets a claimed aim only by dropping the claim, where keeping the claim is among the protected aims (Part XI).
`L315.s20` | FROZEN | Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation, conflict there given \(\chi\): an argument that rules out their both meeting (F1), (F2) and (A) there uses \(\chi\) as a premise and lapses with it.
`L315.s21` | FROZEN | Two candidates offered one in place of the other that conflict at a pair given \(\chi\) are **rivals given \(\chi\)**: for an assessor who tentatively accepts \(\chi\) they pose a problem for \(p\) as rivals do (Problems, below), and for one who does not, they pose none on that account.
`L317.s1` | B4 | **Problems.** Two rivals, neither of them ruled out for an assessor, pose, for that assessor, a **problem for \(p\)**: a conflict between ideas that no argument usable by that assessor has decided.
`L317.s2` | B4 | It is of one of two kinds.
`L317.s3` | B4 | (i) The rivals conflict at some \((a,b)\in C\).
`L317.n4` | FROZEN | Whatever the target does there, at most one of them is an account of \(p\), whether or not anyone records what it does; recording it (D10.3) is a **test**.
`L317.s5` | FROZEN | Whatever it records, an argument from what it records rules out at least one of them for an assessor who can use it, that is, for whom its steps' forms are admitted, its scope is the one declared and its premises about the test's background and instruments are live (K2, K3), while it stays usable; taking those premises as given is that assessor's choice, and so is the ruling out that uses them, which the test does not make by itself (Part 0); an answer that such an argument rules out stays ruled out on \(p\) for as long as the argument stays usable (Part VIII).
`L317.s6` | B4 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict.
`L317.s7` | FROZEN | Their answers then agree at every pair of \(C\), so no argument from an answer recorded in \(C\) rules out one of them without the other; an argument from a test inside \(C\) can rule out one of them without the other only for a failure of its own; and where both meet (E) on \(C\) both are accounts of \(p\).
`L317.n8` | FROZEN | Either kind of problem can also be solved with no test, by an argument usable by that assessor that rules out that one of the rivals meets (E) on \(C\): one that finds, by examining it, that at a pair of \(C\) it gives what a claim the assessor tentatively accepts excludes (conflict with a claim, above; Part IX).
`L317.s9` | FROZEN | Solving a problem so rules one rival out for that assessor while the argument stays usable for that assessor.
`L317.s10` | FROZEN | Where the argument uses a claim the assessor tentatively accepts, that ruling out is a choice the assessor made, in taking the claim as given and going on with it, and not something the claim does by itself; it is already something done about the conflict with the claim, which does not say where the rival is in error, and what the person goes on with stays the person's choice (conflict with a claim, above).
`L317.n11` | FROZEN | A candidate is **easy to vary** (D10.4), in the sense used here, when it and a rival pose a problem of the second kind; the rival is then easy to vary too, and the term says nothing about which of them, and not the other, is an account on a finer contract.
`L317.s12` | B4 | A criticism that a candidate is easy to vary must supply such a rival (Part IX).
`L317.s13` | FROZEN | Two rivals that are both accounts on \(C\) conflict only outside it, and a claim that one of them and not the other meets (E) on a contract with some admitted change outside \(C\) is a claim that such a change separates them, and must supply it, as a claim that the target pairs its components one way and not the other must (Argument 2, Consequence).
`L317.n14` | FROZEN | A finer contract that contains a change at which two rivals conflict makes a new question (Part III), on which, offered for it, they pose a problem of the first kind while neither is ruled out; whether a candidate is an account of a question depends on the candidate, the question and its target, and not on anyone's view of them, on when anyone first asks the question or on whether anyone has tested the candidate on it (Parts I and V); nothing about it is ever settled, and whatever anyone accepts about it, that a candidate is an account or that it is not, is accepted tentatively (Part 0).
`L317.s15` | B4 | A contract narrowed to leave out the pairs at which two rivals conflict also makes a different question; it solves nothing on \(p\), and the problem for \(p\) remains until at least one of them is ruled out for that assessor.
`L317.s16` | FROZEN | Nothing here counts rivals or orders candidates: of one candidate, what is said is whether it meets (E) on a contract and whether it is ruled out for an assessor; of two, whether they conflict; of a candidate and a claim, whether they conflict.
`L317.s17` | B4 | A problem that a system represents can be a recognized difficulty (Part X), as when choosing one of two rivals meets a claimed aim only by dropping the other, which is not ruled out either, where keeping every rival not ruled out is among the protected aims (Part XI).

# Part VII — Exact constructions


## Production and direction

`L325.s1` | FROZEN | Stipulate \(H:=U_H,\ \theta:=U_\theta,\ L:=H\cot\theta\), where \(U_H\) and \(U_\theta\) are exogenous values setting the pole's height \(H\) and the sun's elevation \(\theta\), and \(L\) is the length of the pole's shadow.
`L325.s2` | FROZEN | Under \(A\) containing interventions on \(H\) and \(\theta\), these ports are inputs and \(L\) is an output, by Part II.
`L325.s3` | B2 | An intervention on \(L\) replaces its component and leaves \(H,\theta\) unchanged.
`L325.s4` | B2 | The forward organization is faithful under this contract.
`L325.s5` | FROZEN | The reversed calculation \(H=L\tan\theta\) is not: intervening on \(H\) changes the target's \(L\) but not the calculation's \(L\).
`L325.n6` | FROZEN | It is faithful under the identification contract \(C_{\mathrm{id}}=\{1\}\times B\) (E1).
`L325.s7` | FROZEN | Direction is set by the admitted edits; the nouns "pole" and "shadow" fix nothing.

## Identification

`L329.s1` | FROZEN | Let \(Z\) be the admitted states, \(g:Z\to Y\) the measurement, \(f:Z\to F\) the feature.
`L329.s2` | FROZEN | The fibre at \(y\) is \(Z_y=g^{-1}(y)\).
`L329.s3` | B2 | The feature is identified at \(y\) exactly when \(Z_y\neq\varnothing\land|f[Z_y]|=1\).
`L329.s4` | FROZEN | (I1) It is identified on every attainable \(y\) exactly when \(f=\bar f\circ g\) for some \(\bar f\).
`L329.s5` | FROZEN | (I2) For linear \(g\) and linear feature \(c^\top\), identification is \(\ker g\subseteq\ker c^\top\).
`L329.s6` | FROZEN | (I3) Repeating rows changes no kernel; an independent calibration can.
`L331.s1` | FROZEN | For the two balances \(\begin{pmatrix}1&1&0\\1&0&1\end{pmatrix}\), reading an unknown mass \(x\) with biases \(b_A,b_B\), in that order, the kernel is spanned by \((1,-1,-1)\); the readings identify \(b_B-b_A\) and not \(x\).
`L331.s2` | FROZEN | This is an account of a limitation.
`L331.s3` | FROZEN | "Set \(b_B=0\) because it gives the mass I favour" is not an inference from the readings; it is circular, though the value it sets might be the target's.

## Obstruction

`L335.s1` | B2 | For allowed steps \(R\) and an invariant \(I\) with \(zRz'\Rightarrow I(z)=I(z')\), no allowed path joins states of different invariant value.
`L335.s2` | B2 | (O1) Equal values do not suffice for reachability.
`L335.s3` | FROZEN | Twenty-three indivisible tokens cannot be split equally three ways; permitting division changes the state space and makes a new question (Part III); the scoped result on its own question is as it was.

## Explanations that remove structure

`L339.s1` | FROZEN | A question of the form "why is there no \(X\)-effect?" has a target \(D\) in which the ports and components a rival account would need are absent, and a contract containing the edits that would introduce them.
`L339.s2` | FROZEN | An account is faithful when introducing those components changes the answer in \(E\) as it does in \(D\), and their absence leaves both unchanged.
`L339.s3` | FROZEN | The rival's supposed structure has as its counterpart a *deleted* subnetwork, whose relation is full (Part II).
`L339.s4` | FROZEN | This is the semantics' treatment of eliminative explanation; it is offered as an account, and is listed under attack (Nec) in Part XV as a place where it may not be one.
`L339.s5` | FROZEN | Where the absent structure appears to be present, the question why it appears is a separate question with its own target and contract (Part III): an account of the absence neither answers that question nor needs to, and a bare denial, which offers no component that responds to a change in what produces the appearance, is not an account of it.

## Odd-order skew-symmetric matrices

`L343.s1` | B2 | Question: why is every odd-order real skew-symmetric matrix singular?
`L343.s2` | B2 | Contract: remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed.
`L343.s3` | B2 | The full Leibniz expansion with skewness substituted meets (F1) and (F2): every intermediate product is a determinant suborganization whose hidden ports project away.
`L343.s4` | FROZEN | It meets (A): the answer is the absence of invertible matrices in the family, and under each contrast the family contains one.
`L343.n5` | FROZEN | \(\operatorname{Dependence}\) is met: \(I_3\) is an instance under removal of skewness, and \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) under removal of oddness.
`L343.s6` | FROZEN | Non-vacuity is met: any nonzero odd skew matrix is an instance, and the edits the target admits outside the contract, to the field arithmetic and to the link between determinant and invertibility, are left out by the stated scope.
`L343.s7` | FROZEN | No edit here is a physical one, and none needs to be: the contract is a set of changes to the mathematical target (Part III).
`L343.s8` | B2 | The expansion is an account.
`L343.s9` | FROZEN | That a three-line piece of mathematics is shorter is not a fifth condition.

## Constitutive rules

`L347.s1` | B2 | A rule relation \(C_r\subseteq Z\times S\) answers "which status under this rule?" by its fibre.
`L347.s2` | B2 | Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\).
`L347.s3` | B2 | Whether the rule governs a practice, and whether it should, are separate questions with separate contracts.

# Part VIII — Transport results

`L353.s1` | FROZEN | **Functional transport.** Let \(S_a\) be a target process and \(T_a\) a represented process for each admitted generator \(a\).
`L353.s2` | FROZEN | If \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\), the same equation is met by every admitted finite composition with matching scopes.
`L353.s3` | FROZEN | *Why this and not its denial.*
`L353.s4` | FROZEN | \(\pi S_bS_a=T_b\pi S_a=T_bT_a\pi\); induct. ∎
`L355.s1` | FROZEN | **Relational transport.** For \(R\subseteq Z_D\times Z_E\), forward preservation is
`L357.s1` | FROZEN | \[ zRy\land z\xrightarrow{a}z'\Rightarrow\exists y'[y\xrightarrow{\tau(a)}y'\land z'Ry'], \tag{T1} \]
`L361.s1` | FROZEN | with the backward condition required for equivalence rather than one-sided abstraction.
`L361.s2` | B2 | Composition of relations preserves both directions when intermediate scopes agree.
`L363.s1` | FROZEN | **Approximate transport.** Let \(S\) be a target next-step process and \(T\) a represented next-step process, as \(S_a\) and \(T_a\) are in functional transport, and let \(d\) be a metric on \(X_E\).
`L363.s2` | FROZEN | With one-step discrepancy \(d(\pi Sz,T\pi z)\le\varepsilon\) at every state \(z\) of a stated scope, and with \(T\) \(L\)-Lipschitz for \(d\), the discrepancy after \(n\) steps from one state \(z\), \(e_n=d(\pi S^nz,T^n\pi z)\) (so \(e_0=0\)), meets the bound \(e_n\le\varepsilon\sum_{k<n}L^k\) whenever \(z,Sz,\dots,S^{n-1}z\) lie in that scope.
`L363.s3` | FROZEN | (T2) Without a modulus, no accumulated bound follows.
`L363.s4` | FROZEN | An exact question is not silently replaced by an approximate one.
`L365.s1` | FROZEN | **Recoding.** A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing (Argument 8).
`L365.s2` | FROZEN | A section of a carrier filled from another source keeps that other source's history, whatever it happens to match.
`L367.s1` | FROZEN | **Historical index.** A proposition indexed to a contract remains that proposition when a later theory changes the current contract.
`L367.s2` | FROZEN | A new index is a new claim.
`L369.s1` | B2 | **A failed answer stays failed.** Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\).
`L369.s2` | B2 | By (A), a candidate for \(p\) whose answer at \((a,b)\) is \(y\), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=y\), is not an account of \(p\), whether it is the candidate that gave \(y\) there and failed, that candidate offered again, a rival, or a changed candidate that keeps \(y\) there; and so on every question with the same target and query whose contract contains \((a,b)\).
`L369.s3` | FROZEN | Once an argument usable by an assessor rules out \(y\) as the target's answer at \((a,b)\), every such candidate alike is ruled out for that assessor, from the candidate's own answer there, with no record of which candidates failed before or of how any was changed.
`L369.s4` | FROZEN | Here "ruled out" is meant as in Part VI: the assessor holds an argument usable by that assessor (Part IX) that rules out the claim that \(y\) is the target's answer at \((a,b)\); joined to a candidate's own answer \(y\) there and to (A), it rules out that the candidate meets (E); and by (K3) an argument from the test that records it rules out a candidate only together with the background and instruments the test uses.
`L369.s5` | FROZEN | If a premise about them ceases to be live, the argument is not usable (K2) and those candidates are no longer ruled out by it, every such candidate alike; no candidate becomes an account by that (E).
`L369.s6` | FROZEN | A contract that omits \((a,b)\), or a changed query, makes a different question (Part III): an account on it does not answer \(p\), and it leaves the failure on \(p\) as it was (Historical index).

# Part IX — Criticism, use, and usable arguments

`L375.n1` | FROZEN | **Histories.** A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) (\(\preceq_h\,:=\,\prec_h^{*}\); \(\forall X\subseteq h\,[X\neq\varnothing\Rightarrow\exists x\in X\,\forall y\in X\,\neg\,y\prec_h x]\), D11.3) and a physical interpretation supplying process occurrences, their ports, and the connections actually instantiated.
`L375.s2` | B4 ⟨SC⟩ | An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.
`L375.s3` | FROZEN | A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result.
`L377.s1` | FROZEN | **Bearing.** A criticism has target \(z\), alleged defect \(\delta\), premise \(g\), and a connection.
`L377.s2` | FROZEN | Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments.
`L377.s3` | FROZEN | Then
`L379.s1` | FROZEN | \[ \operatorname{Bearing}(c,z,p)\iff\operatorname{Account}(\mathcal E_c). \tag{K1} \]
`L383.s1` | B4 ⟨SC⟩ | A criticism occurrence can exist when (K1) fails.
`L383.s2` | FROZEN | An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target.
`L385.s1` | B4 ⟨SC⟩ | **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.
`L385.s2` | FROZEN | Using an objection does not give it bearing (K1) or make any argument from it usable (K2).
`L387.s1` | FROZEN | **Usability.** For argument step \(u\) with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:
`L389.s1` | B4 ⟨Expl Suff Nec SC⟩ | \[ \operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u). \tag{K2} \]
`L393.n1` | FROZEN | \(\operatorname{Form}_j(u)\): the inference form of \(u\) is one \(j\) admits.
`L393.n2` | FROZEN | \(\operatorname{Scope}_j(u)\): \(u\) is applied within the contract, grain and boundary \(j\) has declared for it; \(\operatorname{Live}_j(d;u)\): \(d=\operatorname{concl}(u')\) for some \(u'\in\operatorname{Below}(u)\) with \(\operatorname{Usable}_j(u')\) (D9.4), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \(j\) holds an explanation of \(d\); a claim \(j\) has never taken up is not live for \(j\).
`L393.s3` | FROZEN | Admitting a form, like accepting a claim, is tentative (Part 0).
`L393.n4` | FROZEN | For \(d\in\operatorname{Prem}(u)\): \(d\notin\operatorname{Accepted}_j(\xi')\land\neg\exists u'\in\operatorname{Below}(u)\,[\operatorname{concl}(u')=d\land\operatorname{Usable}^{\xi'}_j(u')]\Rightarrow\neg\operatorname{Usable}^{\xi'}_j(u)\); and \(\operatorname{Accepted}_j(\xi')\subseteq\operatorname{Accepted}_j(\xi)\), \(\operatorname{Forms}_j\), \(\operatorname{Scope}_j\) fixed \(\Rightarrow X^{\xi'}_j(\psi)\subseteq X^{\xi}_j(\psi)\) (D9.4, D9.8, FC70, FC56).
`L395.n1` | FROZEN | **What a test rules out.** For \(T\land B\land I\Rightarrow O:\ \alpha\in X_j(O)\land\operatorname{Usable}_j(u^{+})\land\forall l\in\operatorname{leaves}(\alpha)\,[\neg(T\land B\land I)\notin\operatorname{conj}(l)\land\neg\operatorname{MadeFrom}(l,\neg(T\land B\land I))]\Rightarrow\alpha^{+}\in X_j(T\land B\land I);\quad\forall x\in\{T,B,I\}:\neg\operatorname{RO}(\alpha^{+},x)\) (D9.9). (K3)
`L397.s1` | FROZEN | **Arguments.** A record leaf is a reference to an event with an interpreted claim.
`L397.n2` | FROZEN | An argument is an argument tree (D9.2) whose leaves are premises, which are record leaves or stated assumptions and definitions.
`L397.s3` | FROZEN | Each step of an argument rules out the case in which the step's premises are met and its conclusion fails, for someone who admits its inference form (\(\operatorname{Form}_j\)), while that form stays admitted.
`L397.n4` | FROZEN | An argument \(\alpha\) is usable by \(j\) when \(\forall u\in\operatorname{steps}(\alpha)\ \operatorname{Usable}_j(u)\land[\operatorname{steps}(\alpha)=\varnothing\Rightarrow\operatorname{concl}(\alpha)\in\operatorname{Accepted}_j(\xi)]\) (D9.6), and it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below).
`L397.s5` | B4 ⟨Expl Suff Nec⟩ | For \(\psi\), \(X_j(\psi)\) is the set of arguments usable by \(j\) that rule out \(\psi\).
`L397.s6` | FROZEN | Where no argument usable by \(j\) rules out \(\phi\), that absence rules out nothing, neither \(\phi\) nor \(\neg\phi\).
`L397.n7` | FROZEN | An argument need not cite a test: one with no record leaf that finds, by examining a candidate, that it gives what a claim excludes (Part VI, conflict with a claim), rules the candidate out for whoever can use it, on a question about the world as on any other.
`L397.n8` | FROZEN | Where such an argument uses a claim taken as given, the ruling out is a choice the person using it made, not something the claim does by itself (Part 0).
`L397.s9` | FROZEN | **Premises taken as given.** A premise may be a claim taken as given: tentatively accepted, for whatever reason, even with no thought given to it, by someone who holds no explanation of it.
`L397.s10` | FROZEN | As to its premises, (K2) asks only that they be live for the person using the step; neither it nor anything else in the semantics asks that the person represent (R) a premise's explanation, or any part of it, before using the premise to find an error.
`L397.n11` | FROZEN | That a person can use a claim so, without containing its explanation, is a costly gamble for all creative agents; and if this were not possible, error correction could become impossibly costly to perform.
`L397.s12` | FROZEN | The semantics names the gamble and puts no measure on it.
`L397.s13` | B4 ⟨Expl Suff Nec⟩ | A system can be designed that must hold the whole explanation of a premise before using it; that is a detail outside the process the semantics describes, and the semantics does not require it.
`L397.n14` | FROZEN | **A premise that is the denial.** An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally (D9.7) and not by logical equivalence alone; nor does an argument whose record leaf was made from a claim rule out that claim's denial.
`L397.s16` | FROZEN | Such an argument, as one against that claim, has its conclusion among its premises, as in "\(p\) because \(p\)", and does not rule that claim out for anyone.
`L397.s17` | FROZEN | A person may still drop the claim, for whatever reason (Part 0): that is the person's choice, not a ruling out, and it leaves the claim not ruled out and any problem it poses as it was (Part VI).
`L397.n17` | FROZEN | A premise taken as given differs from such a premise: it finds that the candidate gives what the premise excludes.
`L397.s19` | FROZEN | The block catches only a premise that is the claim's denial, read structurally; a premise from which a step leads to the denial, as one does from \(r\) and "if \(r\), this candidate fails (E)", is a premise taken as given, and using it is the gamble above, not a circular argument.
`L397.s20` | FROZEN | Where the premises \(j\) tentatively accepts are inconsistent, arguments from them can rule out, for \(j\), a claim and its denial alike; the semantics then says only that \(j\)'s premises conflict, and which of them \(j\) drops, if any, is \(j\)'s choice (Part 0).

# Part X — Understanding, construction, and origin

`L403.s1` | FROZEN | **Deployment.** \(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi;U)\) is met when \(s\) at \(\xi\) holds a representation of \(c\), by (R) a faithful transport with selected or constructed provenance, integrated into problem-directed activity and serving the declared use task \(U\) as a retained capability (Part XII).
`L403.s2` | B3 | The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect.
`L403.s3` | B3 | A system may understand a theory in error.
`L403.s4` | FROZEN | A narrow retained use is what it is: it suffices neither for the wider understanding it falls short of nor for a permanent inability to reach it.
`L405.n1` | FROZEN | **Construction.** \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares \(\operatorname{Held}_\ell(o,c)\) (D13.3, D18.1) for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.
`L405.s2` | FROZEN | A construction trace identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation.
`L405.s3` | FROZEN | Reconstruction by a learner is construction; relay is not.
`L405.s4` | FROZEN | A first representation may be constructed from an available problem without prior observation of what it represents.
`L405.s5` | FROZEN | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.
`L407.s1` | B3 | An inexplicit representation is not an absent one.
`L407.s2` | FROZEN | A pianist can imagine a passage without playing it.
`L407.s3` | FROZEN | A geometer can manipulate a spatial relation without naming every component.
`L407.s4` | FROZEN | An investigator can notice an inconsistency before articulating its premises.
`L407.s5` | FROZEN | None of (R), Deploy and Build asks whether the relevant distinctions and transformations are written in a particular format: what they ask is whether those distinctions and transformations are instantiated, with the fidelity and provenance (R) requires, and used where use is asked.
`L409.s1` | FROZEN | A system's realization can use a partial, distributed, or temporally extended representation.
`L409.s2` | FROZEN | The relevant bindings can be available through memory, imagery, action rehearsal, or interaction with an artifact.
`L409.s3` | FROZEN | Not every representation must be simultaneously explicit.
`L409.s4` | FROZEN | Retaining a critical target can consist in being able to re-present the relevant distinction, not in storing a complete verbal transcript.
`L409.s5` | B3 | A construction trace may therefore identify a binding constructed in the subhistory by its use rather than by a statement of it: by responses that preserve its role bindings, send content-preserving recodings to the same transition and content changes to the changes the binding specifies, and lie on an active route, as reason use asks of an objection (Part IX).
`L409.s6` | B3 | Use does not by itself construct: received content used as it was received keeps its inherited provenance.
`L409.s7` | FROZEN | A carrier that passes content on without such use has relayed it, and relay is not construction.
`L411.s1` | B3 | Construction is not selection.
`L411.s2` | B3 | A selected transport has no represented target in its history; a constructed one does.
`L411.s3` | FROZEN | A physical system may exhibit both; the traces differ.
`L413.s1` | FROZEN | **Newness.** Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\).
`L413.s2` | FROZEN | The relation is structural at the stated grain, not string equality or similarity; it is read with \(c\) and its contract fixed, and (N) uses it only so, testing each \(d\) against \(c\).
`L413.s3` | FROZEN | With \(R_{<e}(s,h)=\bigcup_{\xi\text{ before }e}R_{\beta,\ell}(s,\xi)\),
`L415.s1` | B3 | \[ \operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c. \tag{N} \]
`L419.s1` | FROZEN | **Origin.** With \(\operatorname{Attempt}(s,c,p,h,e)\) the relation that \(c\) is actually used to address \(p\),
`L421.s1` | FROZEN | \[ \operatorname{Origin}_{\beta,\ell}(s,c,p,h,e)\iff\operatorname{Attempt}(s,c,p,h,e)\land\operatorname{New}(s,c,h,e)\land\operatorname{Build}_{\beta,\ell}(s,c,h,e). \tag{G} \]
`L425.s1` | B3 | The content \(c\) may be an organization, a transport, or a contract.
`L425.s2` | B3 | When it is a contract, the originative act is the finding of a question.
`L425.s3` | FROZEN | A dimension of variation mentioned in passing is not thereby a port of the account; it becomes one when the account admits changes to it, and adding it is construction.
`L427.s1` | FROZEN | **Ownership.** The subhistory in Build is owned by \(s\) when its processes run inside the system boundary and resource contract declared for \(s\) (Part XII).
`L427.s2` | FROZEN | Work supplied from outside that boundary, a diagnosis, a decisive question, an instruction about what to read, remains an outside contribution however it is executed inside; a process that runs inside the boundary is the system's own whoever wrote it; and where the boundary is drawn decides, not where the process sits in the casing.
`L427.s3` | B3 | Contribution of content and ownership of a process are different attributions: a routine written outside the boundary and run inside it is the system's own process, and its content remains its writer's contribution.
`L427.s4` | FROZEN | Ownership is not defined by the capability attributed through it (Part XII).
`L429.s1` | FROZEN | **Episodes.** A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response.
`L429.s2` | FROZEN | A **recognized difficulty** is a failure of a claimed aim, or a conflict in which what the system holds meets a claimed aim only by failing a protected one (Part XI), when the system represents it.
`L429.s3` | FROZEN | A creative critical episode contains an instance of (G) connected to its inquiry.
`L429.n4` | FROZEN | Closing an episode is a choice: an argument can rule out some ways of closing it for the person choosing, and where it leaves one way not ruled out, the person sees no option but that one, which is not to say the person has no option; no argument makes the choice.

# Part XI — Repair, created explanation, and appraisal

`L435.s1` | FROZEN | **Repair.** The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes.
`L435.s2` | FROZEN | For claimed aims \(O\) and protected aims \(P\), fixed for the comparison,
`L437.s1` | B3 ⟨SC⟩ | \[ \operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\iff\exists o\in O[\neg o(\xi)\land o(\xi')]\land\forall r\in P[r(\xi)\Rightarrow r(\xi')]\land\operatorname{ProducedBy}(\Delta,\xi,\xi';O). \tag{P} \]
`L441.n1` | FROZEN | The aims are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and \(\operatorname{Lost}_{\xi,\xi'}(r)\iff r(\xi)\land\neg r(\xi')\) (D14.1).
`L441.s2` | B3 | In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).
`L441.s3` | FROZEN | Their declaration makes no appraisal of the aims, and (P) puts no order on alternatives.
`L441.s4` | B3 ⟨SC⟩ | Losses outside \(P\) must be exposed.
`L441.s5` | FROZEN | \(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair; it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran, the repair is attributed to both and the history supplies no division of the attribution that it does not contain.
`L441.s6` | FROZEN | An account that produced nothing, an act that repaired without an account, and a repair produced through use of an account are three different attributions.
`L443.n1` | FROZEN | **Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one.
`L443.s3` | B3 | With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,
`L445.s1` | FROZEN | \[ \begin{aligned} \operatorname{CreateEx}(s,\Delta,h,e)\iff{}&\operatorname{CreativeCriticalEpisode}(s,\Delta,h,e)\land\exists\xi,\xi'\,\bigl[\operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\\ &\land\exists o\in O_{\mathrm{ex}}\,\exists c,p_c,e_c,t_c,\Gamma_c\,[e_c\preceq_h e\land\neg o(\xi)\land o(\xi')\land\operatorname{Origin}_{\beta,\ell}(s,c,p_c,h,e_c)\\ &\quad\land\operatorname{Account}\big((c,p_c,t_c,\Gamma_c)\big)\land c\in\operatorname{Result}(\Delta)\land\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)\land\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')]\bigr]. \end{aligned}\tag{EX} \]
`L453.s1` | B3 | \(\operatorname{Result}(\Delta)\) is the set of contents at \(\xi'\) that \(\Delta\) prepared.
`L453.n2` | FROZEN | \(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\) (D14.6).
`L453.s3` | FROZEN | In (EX), \(t_c\) and \(\Gamma_c\) are the transport and the identified commitments that make \(c\), with \(p_c\), an explanatory candidate (Part V), and \(U_c\) is the declared use task for \(c\) (Deploy, Part X).
`L453.s4` | FROZEN | The scope of \(\operatorname{Account}((c,p_c,t_c,\Gamma_c))\) is the contract fixed at \(e_c\).
`L453.s5` | FROZEN | A later narrowing of that contract to rescue \(c\)'s meeting (E) is a new claim at a new index, and does not retroactively meet (EX).
`L455.s1` | FROZEN | **Appraisal.** Repairing an aim repairs it and says nothing about how anyone appraises the aim, or the question that led to it.
`L455.s2` | FROZEN | Where a claim invokes an appraisal, the semantics takes the **appraisal relation** \(\mathcal N\) (import 2, Part XIV) as an input and marks the place.
`L455.s3` | FROZEN | The aesthetic case is one such invocation: an effect organization \(\mathcal R\subseteq \mathit{Act}\times\mathit{Occ}\times\mathit{Eff}\); a purpose \(G\subseteq \mathit{Occ}\times\mathit{Eff}\); achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) (AR); and \(\mathcal N\subseteq \mathit{Act}\times\mathit{Occ}\times\mathsf{Rsn}\times\mathcal V_A\) taken as a substantive input when aesthetic value is claimed, where \(\mathit{Act}\) is a set of actions, \(\mathit{Occ}\) of occasions, \(\mathit{Eff}\) of effects, \(\mathsf{Rsn}\) of aesthetic reasons and \(\mathcal V_A\) of aesthetic values, the last two not further specified here.
`L455.s4` | FROZEN | None is defined as another.
`L455.s5` | FROZEN | The semantics does not define \(\mathcal N\), and no aesthetics follows from achieving a stated effect.

# Part XII — The physical module

`L461.s1` | FROZEN | **Tasks.** A substrate is a physical system; an attribute a set of its states; a task a specified input-to-output attribute transformation with explicit resources and side effects.
`L461.s2` | FROZEN | Possibility is the absence of a law-imposed limit, short of exact, on the tolerance to which a task can be performed and retained; it is not one trajectory that performed the task.
`L461.s3` | FROZEN | The physical module adopts a task-based formulation of physics for this purpose.
`L461.s4` | FROZEN | It is where physical possibility enters the semantics as instantiation and transformation; it also enters as the content of claims a candidate can conflict with (Part VI).
`L461.s5` | FROZEN | The module says which organizations a carrier can instantiate, and which transformations of a content, such as holding, copying, teaching, testing, building or performing it, can be carried out.
`L461.s6` | FROZEN | It does not define a question, an account or a conflict between candidates (Parts III, V, VI).
`L463.s1` | FROZEN | **Retained realization.** For protocol \(\pi\), task \(T\), constructor attribute \(C\), and enabling conditions \(\chi\),
`L465.s1` | B3 | \[ \operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C. \tag{CT1} \]
`L469.s1` | B3 | Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task.
`L471.n1` | FROZEN | **Retention fixed point.** \(F(C)=\{z:\forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C\}\).
`L471.n2` | FROZEN | \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)
`L473.s1` | FROZEN | **System boundary and continuity.** A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change).
`L473.s2` | FROZEN | A replaced part that preserves the declared continuity leaves the same system; a process run inside the boundary is the system's whoever wrote it; a process run outside it is not the system's however close it sits.
`L473.s3` | FROZEN | Both are declared before the attribution, not chosen after it.
`L473.s4` | FROZEN | Where the system's boundary is not declared explicitly, a statement that names the system and says whether a process runs inside it or outside it declares the boundary for that process; a statement that the process is the system's own, which does not say where it runs, is the attribution, not its boundary.
`L475.s1` | B3 | **Owned capability.** \(\operatorname{Can}_{\Omega,\beta}(\xi,T;\chi)\) requires an owned retained realization or an owned, physically admitted, finite construction of one under the same continuity and resource contract.
`L475.s2` | FROZEN | A theorist's description of a protocol is not the system's possession of it.
`L475.s3` | FROZEN | Ownership is defined by the processes and resources the boundary includes, never by the capability being attributed: "owned because it can, and can because owned" defines neither.
`L477.s1` | B3 | **Achievement.** \(\operatorname{CanAdv}(\xi,p;\chi,J_p,C_I)\): for each starting configuration in the independently specified \(J_p\), every maximal execution completes with a history meeting the achievement predicate and a continuing organization in \(C_I\).
`L477.s2` | FROZEN | A first discovery is not a repeatable task; retention is applied to the inquiry-enabling organization. (CA)
`L479.s1` | FROZEN | **Tolerances.** The tolerances of the physical module (Part XIV) form a directed preorder \(Q_\Theta\), in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes, and none of them is exact; \(q\in Q_\Theta\) is a tolerance of performance and \(r\in Q_\Theta\) a tolerance of retention.
`L479.s2` | FROZEN | \(\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks physically achievable at tolerances \((q,r)\); \(\mathsf{Cap}^{q,r}_\Omega(\xi)\) is the set of tasks with an owned realization, or an owned construction of one, at those tolerances, as owned capability requires; and \(\mathsf{Poss}_\Theta=\bigcap_{q,r}\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks achievable at every tolerance, which is what possibility means under Tasks.
`L479.s3` | FROZEN | Then \(\mathsf{Cap}^{q,r}_\Omega(\xi)\subseteq\mathsf{Admit}^{q,r}_\Theta\); \(\mathsf{Cap}^\infty=\bigcap_{q,r}\mathsf{Cap}^{q,r}\subseteq\mathsf{Poss}_\Theta\).
`L479.s4` | B3 | (CT3, CT4) Capability at a given tolerance does not imply possibility at every tolerance.
`L481.s1` | FROZEN | **Selection in the physical module.** A selected provenance \(\operatorname{Sel}(t;\mathcal T,\mu,H)\) is a claim about a physical history: a population of candidate transports, a physically admitted variation operator, and a survival condition enacted by the environment.
`L481.s2` | FROZEN | It is fallible and testable as any physical claim is.
`L481.s3` | FROZEN | The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it.

# Part XIII — Recursion and universality

`L487.s1` | B4 | **Scrutinizability.** An aspect \(d\) of a system's practice is scrutinizable at \(\xi\) when there is an owned, admitted continuation in which a description of \(d\) becomes a represented target, criticism can be directed at it, and the result can affect its operative use.
`L487.s2` | FROZEN | Contracts and transports are among the scrutinizable aspects.
`L489.s1` | FROZEN | **Recursive capacity.**
`L491.s1` | B4 | \[ \forall n<\omega\ \forall\text{ admitted target chains of length }n,\ \exists\text{ an owned enabling continuation}. \tag{RC} \]
`L495.s1` | B4 | **Barriers.** An explanatory barrier is an independently characterized domain for which every admitted, non-question-begging enabling condition leaves the relevant capability unavailable.
`L495.s2` | FROZEN | A finite list of failures does not rule out a bypass; an argument that exhibits one bypass rules out a proposed barrier for whoever can use it.
`L495.s3` | FROZEN | \(\operatorname{Enable}(s,T,\chi)\) is met when \(\chi\) is an admitted, non-question-begging enabling condition for \(s\) and the task \(T\), in the sense of (CT1).
`L497.s1` | FROZEN | **Universality.** With \(\mathfrak E_\Theta\) the explanatory contents that some carrier can hold under the physical module (whether a content is explanatory on its question is fixed by (E), Part V; \(\Theta\) says only which of them a carrier can hold) and \(\mathfrak P^{\mathrm{adv}}_\Theta\) the coherently posed advanceable challenges, both specified independently of the candidate, with \(\operatorname{Can}\), \(\operatorname{CanAdv}\), \(J_p\) and \(C_I\) as in Part XII, \(U_c\) the declared use task for \(c\) (Deploy, Part X), \(A_p\) the task for \(p\) that \(\operatorname{CanAdv}\) describes, and \(\xi_0\) the index at which the claim is made,
`L499.s1` | B4 | \[ \operatorname{UU}\iff\forall c\in\mathfrak E_\Theta\ \exists\chi,\ \operatorname{Enable}(s,U_c,\chi)\land\operatorname{Can}(\xi_0,U_c;\chi), \tag{U1} \]
`L502.s1` | B4 | \[ \operatorname{UC}\iff\forall p\in\mathfrak P^{\mathrm{adv}}_\Theta\ \exists\chi,\ \operatorname{Enable}(s,A_p,\chi)\land\operatorname{CanAdv}(\xi_0,p;\chi,J_p,C_I), \tag{U2} \]
`L505.s1` | FROZEN | \[ \mathsf{UECS}=\{(M,s,\xi_0,\Omega,\beta):M\models\operatorname{RC}\land\operatorname{UU}\land\operatorname{UC}\}. \tag{U3} \]
`L509.s1` | B4 | Recursion does not entail universality; a historical extension leaves it open; a finite performance record does not suffice for it.

# Part XIV — The class collected

`L515.s1` | FROZEN | **Imports.** The semantics has two.
`L517.s1` | B4 ⟨SC⟩ | 1. The **physical module** \(\Theta\): substrate state spaces, attributes, admitted processes, controlled-action interpretation, resources, tolerances, and \(\operatorname{Org}_\ell\), the organization a physical occurrence instantiates at a grain.
`L518.s1` | FROZEN | 2. The **appraisal relation** \(\mathcal N\), when a question invokes an appraisal. It is taken as an input and the semantics does not define it; the aesthetic relation of Part XI is one instance.
`L520.s1` | FROZEN | Everything else is defined in terms of the two imports, the structural vocabulary of (O) and (Q), the declared indices and the declared inputs (below).
`L520.s2` | FROZEN | Roles, from admitted edits (Part II).
`L520.s3` | B4 | Kinds, from signatures (K).
`L520.s4` | B4 | The respect of a question, from its query (Part III).
`L520.s5` | B4 | Representation, from fidelity and provenance (R).
`L520.s6` | FROZEN | Provenance, from physical history (Parts IV, XII).
`L520.n7` | FROZEN | Account, from \(\text{(F1)}\land\text{(F2)}\land\text{(A)}\land\operatorname{Dependence}\land\operatorname{NonVacuous}\) (E).
`L520.s8` | FROZEN | Understanding, construction, newness, origin, repair, created explanation, capability, recursion, universality, from those.
`L522.s1` | FROZEN | **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) admits, the scope \(j\) declares and the premises \(j\) tentatively accepts and has not withdrawn (K2, Part IX); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).
`L522.s2` | FROZEN | An assessment that depends on one of these, or on the appraisal relation where a claim invokes an appraisal, is an assessment given the input; where the input is missing, the assessment is left open and the semantics says so rather than choosing the input from the assessment wanted.
`L522.s3` | FROZEN | The semantics supplies no probability on claims and no function that orders explanations or thinkers, and a claim that needs one is left open.
`L524.s1` | FROZEN | **Indices, not imports.** Grain \(\ell\), boundary \(\beta\), continuity \(\Omega\), and the contract \(C\) are declared indices.
`L524.s2` | FROZEN | Every claim is relative to them; none is a predicate that a case meets or fails.
`L524.s3` | FROZEN | An index is what a claim is relative to; a declared input is something a claim takes as stated, which the semantics records and does not supply.
`L524.s4` | FROZEN | The boundary and continuity of an attribution, and the scope a claim states for its contract, are values of indices and are declared inputs (above).
`L526.s1` | FROZEN | **Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined.
`L526.s2` | B4 | (K) depends on (O) and a contract.
`L526.s3` | B4 | (F1), (F2), (A) depend on (O), (Q), (K).
`L526.n4` | FROZEN | (E) depends on those (D18.1).
`L526.s5` | FROZEN | (S), (B), (D) depend on (E).
`L526.s6` | B4 | (R) depends on (F1)–(F2) and physical provenance.
`L526.s7` | FROZEN | (K1) depends on (E).
`L526.s8` | FROZEN | (K2) depends on the assessor's declared inputs (Part XIV, above); (K3) on (K2).
`L526.s9` | B4 | Deploy depends on (R) and (CT1).
`L526.s10` | B4 | Ownership depends on histories and a declared boundary, and owned capability on Ownership, (CT1) and a declared continuity (Part XII).
`L526.s11` | FROZEN | Build depends on histories, Ownership and (E).
`L526.s12` | FROZEN | (N), (G) depend on Deploy and Build.
`L526.s13` | FROZEN | (P), (EX) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared aims with their occasions, (EX) also on (P), and ProducedBy on histories and their active routes.
`L526.s14` | B4 | (RC), (U1)–(U3) depend on all of the above.
`L526.s15` | FROZEN | In Part VI, conflict depends on (F1), (F2), (A) and the target's ports and components (Part II), conflict with a claim on those and on the claim, rivals on conflict and on the offer of one in place of the other, rivals given a claim on conflict given that claim and on the same offer, being ruled out for an assessor on usable arguments (Part IX) and (E), a problem for \(p\) on rivals and on neither being ruled out, and easy to vary on a problem for \(p\).
`L526.s16` | FROZEN | Nothing depends on an undefined predicate that says "explains" without a question and a contract, or "is a cause"; (EX) is a defined relation of an episode, not such a predicate.
`L526.s17` | FROZEN | The order has no cycle and no endless descent.
`L526.s18` | FROZEN | A representation defined only by its own construction, or an ownership and a capability each defined only by the other, has not supplied its place in the order; a separate definition that would supply that place, or a separate argument that rules out the denial of the result the definition goes through without using that result, is part of the account only when the account uses it.
`L528.s1` | B4 | **Membership.** The base class: interpretations supplying these data with typing as declared, meeting physical realization wherever a physical attribution is made.
`L528.s2` | B4 | The creative-episode class: base interpretations with an instance of (G) connected to a critical episode.
`L528.s3` | B4 | The explanation-creation class: an instance of (EX).
`L528.s4` | B4 | The recursive class: (RC).
`L528.n5` | FROZEN | The universal class: \(\{M:\exists s,\xi_0,\Omega,\beta\ (M,s,\xi_0,\Omega,\beta)\in\mathsf{UECS}\}\) (U3).
`L528.s6` | FROZEN | A single originative act does not place its author in the universal class.

# Part XV — What would rule this class out

`L534.s1` | FROZEN | The claims the rest depends on, in the order of how much falls if they fail, each with what would rule it out.
`L534.n2` | FROZEN | None is protected by notation or by the availability of this document.
`L534.s3` | FROZEN | A case whose assessment turns on an input the case does not state, where the input is one of the declared inputs Part XIV lists or the appraisal relation, is a case with a missing input, not an argument that rules a claim out.
`L536.s1` | FROZEN | **(Suff) Sufficiency.** A candidate meeting all four conditions of (E) on a contract of its question, with a transport whose provenance is not declared (Part IV), such that an argument not using (E) rules out the claim that it is an explanation of what its question asks.
`L536.n2` | FROZEN | Part V says which of the four each classic attempt fails: a table of observed answers fails (F1); a reversed calculation fails (F2) under the production contract.
`L536.s3` | FROZEN | A table that encodes the response to every admitted change does not fail (F1); like any new attempt, it is a counterexample only if it fails none of the four and such an argument rules out the claim that it is an explanation.
`L538.s1` | FROZEN | **(Nec) Necessity.** A candidate such that an argument not using (E) rules out the claim that it is a non-explanation, whose organization no transport can preserve under any contract on its target.
`L538.s2` | FROZEN | Eliminative explanation (Part VII) is the exposed case.
`L540.s1` | FROZEN | **(Elim) Reinstatement of kinds.** A case where a kind-label distinguishes two accounts that no admitted change distinguishes, and the distinction does explanatory work.
`L540.s2` | FROZEN | An argument that exhibits such a case would rule out the Consequence of Argument 1, for whoever can use it, and make correspondence an import again.
`L542.s1` | FROZEN | **(Prov) Genesis.** Any of three: a selected transport whose value at an unseen change is determined by its history although its population admits a differing survivor there (against Argument 3; a population with no such survivor is the claim's own qualification, not an argument that rules it out); a method that rewrites every construction trace as a selection history without loss (against Part IV, collapsing the two provenances and removing creativity from the semantics); or an argument that rules out that explanation operates on the object layer of Part IV.
`L544.s1` | FROZEN | **(QF) Question-finding.** A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture; or an episode that is not creative which that treatment counts as creative (against Argument 5).
`L546.s1` | B4 ⟨SC⟩ | **A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions.

# Part XVI — Arguments


## 1. Kind preservation needs no condition of its own

`L554.s1` | FROZEN | **Claim.** If a transport meets (F1) on \(C\), no active component \(k\) of \(E\) has a signature on \(\tau[C]\) that differs from the one its counterpart \(\lambda(k)\) has on \(C\), up to the port translation.
`L556.s1` | FROZEN | *Why this and not its denial.*
`L556.n2` | FROZEN | By (K) (D4.4), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\) and \(\operatorname{sig}_{\tau[C]}(k)=\{(\tau(a),\sigma(b),L_k(\tau(a),\sigma(b)))\}\).
`L556.s3` | B4 | (F1) equates the third coordinates pointwise. ∎
`L558.n1` | FROZEN | **Consequence.** A condition \(\forall k\in\Gamma\ \operatorname{SameKind}_C(k,\lambda(k))\) adds nothing to (F1) on any contract (FC18).
`L558.s2` | FROZEN | Where the contract separates two kinds, (F1) already distinguishes them; where it does not, they are one kind on that contract.
`L558.s3` | B4 | The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case.

## 2. Same counterparts, one account

`L562.s1` | FROZEN | **Claim.** Let \(\mathcal E,\mathcal E'\) be candidates for the same \(p\) that both meet (F1), (F2) and (A) on \(C\).
`L562.s2` | B4 | (i) Their answer profiles coincide on \(C\).
`L562.s3` | FROZEN | (ii) If a bijection \(\varphi\) of their active components gives each \(k\) and \(\varphi(k)\) one counterpart, the same subnetwork of \(D\) with port translations that are bijections onto the same ports of \(D\), then \(k\) and \(\varphi(k)\) are of one kind on \(C\) for every \(k\); so far as (F1), (F2) and (A) reach, the two are one account on \(C\): \(\varphi\) pairs their active components, each pair of one kind on \(C\), and by (i) their answer profiles coincide.
`L564.s1` | FROZEN | *Why this and not its denial.*
`L564.s2` | FROZEN | (i) By (A), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)=\operatorname{Ans}_{E'}(\tau'(a),\sigma'(b))\) for every \((a,b)\in C\).
`L564.s3` | FROZEN | (ii) By Argument 1, \(k\) has the signature of its counterpart on the ports its translation names, and \(\varphi(k)\) the signature of the same counterpart on the same ports; composing the one translation with the inverse of the other gives a footprint bijection under which the two signatures, read on \(C\), coincide. ∎
`L566.s1` | FROZEN | Without the premise of (ii) nothing more follows: candidates whose counterparts are different subnetworks, or cut \(D\) at different places, are different candidates with one answer profile (Argument 9; Part VI, redundant routes).
`L566.s2` | FROZEN | A coarsening is not a recoding (Argument 8).
`L568.s1` | FROZEN | **Consequence.** Where two candidates that meet (F1), (F2) and (A) differ only in which component has which counterpart, the contract does not contain the distinction; a claim that the target pairs its components one way and not the other is a claim that some admitted change separates them, and must supply it.
`L568.s2` | FROZEN | A finer contract that contains such a change is a new question (Part III); whether anyone asks it is that person's choice (Part 0).

## 3. Selected transports are underdetermined on unseen changes their population leaves open

`L572.s1` | FROZEN | **Claim.** Let \(t\) be selected from a population \(\mathcal T\) on a finite history \(H\subsetneq C\).
`L572.s2` | FROZEN | For every \((a,b)\in C\setminus H\) at which some \(t'\in\mathcal T\), also surviving on \(H\), has a different value from \(t\), the value of \(t\) at \((a,b)\) is underdetermined by \(H\): survival on \(H\) does not distinguish \(t\) from \(t'\) there.
`L572.s3` | FROZEN | The presence of an unseen pair alone leaves open whether such a \(t'\) exists; it must be a member of \(\mathcal T\), a transport the physics and the stated construction admit (Part XII), and it must survive on \(H\) (Part IV).
`L574.s1` | FROZEN | *Why this and not its denial.*
`L574.s2` | B4 | The component relations \(L_j(a,b)\) are supplied independently for each \((a,b)\).
`L574.s3` | FROZEN | Survival on \(H\) constrains only \(\{L_j(a,b):(a,b)\in H\}\).
`L574.n4` | FROZEN | Where \(\mathcal T\) contains a transport with \(L_{j}(a,b)\) altered to another admitted relation for one \((a,b)\) with \((\tau(a),\sigma(b))\notin(\tau\times\sigma)[H]\), that transport survives on \(H\) and differs at \((a,b)\), and survival on \(H\) cannot select between the two.
`L574.s5` | FROZEN | Where \(\mathcal T\) contains no such transport, \(H\) is silent on the value at \((a,b)\) and the population fixes it. ∎
`L576.s1` | FROZEN | **Consequence.** A correspondence produced by selection is faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not.
`L576.s2` | FROZEN | This is why the object layer is fallible: it was shaped against the changes its history contained.
`L576.s3` | FROZEN | It is also why surprise is possible.
`L576.s4` | FROZEN | What the qualification gives up is the claim of a differing survivor at every unseen pair, and with it the blanket claim that every untested value is unconstrained; a population restriction, a physical relation, or another stated constraint may already fix a value that the history never tested.

## 4. Surprise requires an incomplete history

`L580.s1` | FROZEN | **Claim.** A system can be surprised only if it holds a transport selected on a history \(H\) strictly smaller than its contract \(C\).
`L582.s1` | FROZEN | *Why this and not its denial.*
`L582.s2` | FROZEN | Surprise is defined (Part IV) as a violation of a selected transport at an occurring \((a,b)\in C\) with \((a,b)\notin H\).
`L582.s3` | FROZEN | If there is no transport there is no prediction and hence no violation.
`L582.s4` | FROZEN | If \(H=C\), every such \((a,b)\) is in \(H\), so no violation at a pair of \(C\) outside \(H\) exists. ∎
`L584.n1` | FROZEN | **Consequence.** Surprise is not a feeling added to the semantics; it is \(\operatorname{Sel}(t;\mathcal T_t,\mu_t,H_t)\land(a,b)\notin H_t\land\operatorname{Viol}(t;a,b)\) (D12.7).
`L584.s2` | FROZEN | The two responses, extend \(H\) and re-tune, or construct a new transport, are the difference between learning and creating, and the semantics distinguishes them by their traces, not by their outcomes.

## 5. Question-finding is representable

`L588.s1` | FROZEN | **Claim.** A contract \(C\), taken with its edits and its query, can be given the structure of an organization in the sense of (O), and can be the content \(c\) in (G).
`L588.s2` | FROZEN | Hence an episode whose originative contribution is a new contract meets (G) and, where the other conjuncts are met, (EX).
`L590.s1` | FROZEN | *Why this and not its denial.*
`L590.s2` | FROZEN | A contract is a subset of \(A\times B\) together with \(\mathcal Q\).
`L590.n3` | FROZEN | Give it ports (the edits and their boundaries, and \(\mathcal Q\)), components (the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits (add or remove a change; alter \(\mathcal Q\)).
`L590.s4` | FROZEN | It is then a \(D\) in the sense of (O).
`L590.s5` | FROZEN | Deploy, Build, and New apply. ∎
`L592.s1` | FROZEN | **Consequence.** Finding a new question, by an owned construction (G), is a creative act, as answering one is.
`L592.s2` | FROZEN | A semantics that takes questions as inputs cannot represent this; the present one does, by giving contracts provenance.
`L592.s3` | FROZEN | That a question was found says nothing about how anyone appraises it (Part XI).

## 6. There are two imports

`L596.s1` | FROZEN | **Claim.** Every predicate in Parts II–XIII is defined in terms of \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with the structural vocabulary of (O) and (Q), declared indices and declared inputs.
`L598.s1` | B4 | *Why this and not its denial.*
`L598.s2` | FROZEN | By the dependence order of Part XIV, which lists the declared indices and the declared inputs with the definitions that use them, following each definition back until it reaches the imports, the indices, the declared inputs, or (O) and (Q), which depend on nothing. ∎
`L600.s1` | FROZEN | **Consequence.** There is no residual, undefined predicate meaning "explains," "represents," or "is a cause"; (EX) is defined (Part XI).
`L600.s2` | FROZEN | The two imports are a theory of matter and, when a question requires it, a theory of appraisal.
`L600.s3` | FROZEN | Neither is a predicate about explanation.

## 7. The frozen assessment and the moving question are consistent

`L604.s1` | B4 | **Claim.** An assessment event with contract \(C\) and an episode in which \(C\) is replaced by \(C'\) with a construction trace are both representable without contradiction.
`L606.s1` | FROZEN | *Why this and not its denial.*
`L606.s2` | FROZEN | The assessment is indexed to \(C\), and whether \(\mathcal E\) meets (E) on \(C\) is a claim at that index (Part VIII, historical index).
`L606.s3` | FROZEN | The episode is a history in which a contract-content \(C'\) is built (Argument 5) and takes over operative use.
`L606.s4` | FROZEN | The claim "\(\mathcal E\) is an account on \(C\)" and the claim "\(\mathcal E\) is not an account on \(C'\)" are claims at different indices, and \(\mathcal E\) can meet (E) on \(C\) and fail it on \(C'\). ∎
`L608.s1` | FROZEN | **Consequence.** The point of contact between an explanation and the world moves across episodes because contracts are constructed; it does not move within an assessment because assessments are indexed.
`L608.s2` | FROZEN | Goalpost-moving is the act of passing off a claim at one index as a claim at another; it is not an operation the semantics admits, since every claim is relative to its declared index (Part XIV).

## 8. Equivariance under structure-preserving recoding

`L612.s1` | FROZEN | **Claim.** Transporting all carriers, relations, transports, histories, contracts and declared inputs along structure-preserving bijections preserves (E), (G), (P), (EX).
`L612.s2` | FROZEN | *Why this and not its denial.*
`L612.s3` | FROZEN | Each is a conjunction of equalities and existence claims over the transported data, the declared aims and occasions of (P) and (EX) among them; bijections preserve them. ∎ The result does not apply to coarsenings, changed boundaries, or lost event identities.

## 9. Output descriptions do not determine accounts

`L616.s1` | B4 | **Claim.** If \(M_0,M_1\) have the same input–output projection and differ on an account claim, no function of the projection agrees with the claim on both.
`L616.s2` | FROZEN | *Why this and not its denial.*
`L616.s3` | B4 | Equal inputs to a function give equal outputs. ∎ Parallel and priority wiring are an instance.
`L616.s4` | FROZEN | The same goes for attribution from emitted text and for use inferred from delivery logs.

## 10. A two-layer episode, in exact form

`L620.s1` | FROZEN | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell, swap the two identities.
`L620.s2` | FROZEN | The sensory field is the occupancy of cells, which cells are filled, without which thing fills them.
`L622.s1` | FROZEN | A simulation layer \(S_0\) with a contract \(C_0\) containing the occlusion edit, and a transport \(t_0\) selected on a history \(H_0\subsetneq C_0\) containing displacements and velocity changes but no occlusions.
`L622.s2` | B4 | \(S_0\) predicts occupancy from recent occupancy.
`L622.s3` | FROZEN | It is faithful on \(H_0\).
`L624.s1` | FROZEN | An occlusion occurs.
`L624.s2` | FROZEN | Under occlusion, the target's thing continues to exist and to move; the occupancy field shows nothing at its cell.
`L624.s3` | B4 | \(S_0\), predicting from occupancy, predicts nothing there and is violated when the thing re-emerges at a cell consistent with its velocity.
`L624.s4` | B4 | This is surprise (Argument 4).
`L626.s1` | FROZEN | Two responses.
`L626.s2` | FROZEN | **Selection:** \(H_0\) is extended to include occlusions; \(\mu\) re-tunes \(t_0\) within its population.
`L626.n3` | FROZEN | If \(\forall t\in\mathcal T:\ \operatorname{Pred}_t(n+1)=f_t(\mathrm{occ}_{n-w+1},\dots,\mathrm{occ}_n),\ w\le L_{\mathrm{occ}}\) (E9, FC102 (b'')), no member survives the extended history: the fidelity failure is structural, not parametric.
`L626.s4` | FROZEN | **Construction:** a new organization \(S_1\) is built with a component per thing carrying position and velocity through occlusion, a persistence component, and a transport \(t_1\) from \(P\) whose \(\lambda\) sends each persistence component to a thing's continuity subnetwork.
`L626.s5` | B4 | Under (F1), \(t_1\) is faithful on the extended contract.
`L626.s6` | FROZEN | By Argument 1, the persistence components have the signature of things on that contract: they respond to displacement and velocity edits as things do, and are invariant under occlusion as things are.
`L626.s7` | FROZEN | No one declared them to be "objects."
`L626.s8` | FROZEN | On this contract the word adds nothing to the signatures they already have (Argument 1).
`L628.n1` | FROZEN | If \(S_1\) was built by an owned subhistory containing a nontrivial binding construction, the binding of a persistence component to a continuity subnetwork, and \(S_1\) is not in the prior repertoire, then, with \(\operatorname{Attempt}(s,S_1,p,h,e)\), (G) is met.
`L628.n2` | FROZEN | If it repairs the aim "possess a deployable account of re-emergence after occlusion" while protecting "predict the displacements that occur," then (P) is met; and with \(\operatorname{CreativeCriticalEpisode}(s,\Delta,h,e)\), \(S_1\in\operatorname{Result}(\Delta)\), \(\operatorname{Deploy}_{\beta,\ell}(s,S_1,\xi';U_{S_1})\), \(\operatorname{ProducesVia}(\Delta,S_1,o;\xi,\xi')\), \(e_c\preceq_h e\) and \(\operatorname{Account}\) for \(S_1\) on its contract, (EX) is met (FC90).
`L630.s1` | FROZEN | The swap edit is invisible in the sensory field and leaves every prediction unchanged.
`L630.s2` | B4 | On any contract containing it that admits each edit for both things alike, composing \(t_1\) with the exchange of the two things gives a second transport, which sends each persistence component to the other thing's continuity subnetwork.
`L630.n3` | FROZEN | The exchange \(\psi\in\operatorname{Aut}(P)\) of the two things has \(\psi[C]=C\) and \(\operatorname{Ans}_p\circ\psi=\operatorname{Ans}_p\), and likewise for the persistence components in \(S_1\) (E9), so the exchange carries the fidelity and the answers of \(t_1\) over to the second transport (Argument 8); so far as (F1), (F2) and (A) reach, the two candidates are one account (Argument 2).
`L630.s4` | FROZEN | A claim that "component 1 is thing 1 and not thing 2" is a claim that some admitted change separates the two pairings of persistence components to things, and on this contract none does.
`L630.s5` | FROZEN | That is not a defect of \(S_1\): the contract contains no change that separates the two things except by their trajectories, so identity, at this grain, is exhausted by trajectory.
`L632.s1` | FROZEN | This episode is a relative-consistency instance for the class.
`L632.s2` | FROZEN | It is not a claim that any actual infant, animal, or program instantiates it.

## 5. The formal core, definition by definition

The formal core after the fourth review round, from its section 0 on, with a mark line `⟦B<n> ⟨…⟩⟧` or `⟦FROZEN⟧` before each definition and encoding. Quotations of the text (`> Lnnn | …`) are as the core has them, of the text as the maths round read it; where a line changed since, section 4 above has its words now. Lines longer than 1,500 characters are cut at a space, the later pieces marked `(cont.)`.

## §0 Conventions and the frame

- A condition holds or fails; a program returns yes or no. ⊥ is the undetermined answer (D3.2), not the value of a condition.
- P(X) is the set of subsets of X; ∏ is the cartesian product; z|U restricts a valuation to the ports U; f[S] is the image of S; R* is the reflexive-transitive closure of a relation; ⇀ marks a partial map.
- D is a target, E a candidate's organization; a subscript or superscript names the organization where needed (A_E, B_E, J_E, L^E_k).
- A pair (a,b) is an edit a and a boundary b. x := (τ(a),σ(b)) and x0 := (1,σ(b0)) in §6.

⟦B1⟧ D0.1
**D0.1 The frame.** Every definition below is relative to a frame Φ: the imports, the declared indices and the declared inputs.

> L31 | The semantics has two imports: the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain, and the **appraisal relation** \(\mathcal N\), taken as an input wherever a question invokes an appraisal. Grain, boundary, continuity and the contract of admitted changes are **declared indices**: every claim is relative to them, and none is a predicate that a case meets or fails.

> L522 | **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) admits, the scope \(j\) declares and the premises \(j\) tentatively accepts and has not withdrawn (K2, Part IX); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).

Φ = (Θ with Org_ℓ; 𝒩 where invoked; ℓ, β, Ω, C; the aims O, P with occasions; the scope statement Σ of each contract; boundary and continuity of each attribution; for each assessor j: Forms_j, the scope declarations Scope_j, Accepted_j(ξ); a weighting where one is used).

⟦FROZEN⟧ D0.2
**D0.2 Primitives this formalization adds.** Beyond Φ, the formal core uses these symbols, which the text names or needs but neither defines nor lists among its imports, indices or declared inputs. Each is an invention, and FC98 asks of each whether it is a claim read through Θ or a primitive the text does not list: the designation δ of a query [I20]; the undetermined answer ⊥ [I21]; Excl(Σ) [I27]; the restriction operation [I29] (the text calls it declared, L287; L522 does not list it); Offered [I33] and Off [I33, r2: A2]; Allow_χ and Applies [I34]; MadeFrom [I39]; the contrast set K of an active route [I46]; Rule, Rec, Chg of reason use [I47]; Integrated and Nontrivial [I55]; Prepares, BindingConstruction, TransferComposite [I56]; Aims* and the exposure record [I58]; O_ex's marking [I59]; Occurs (D11.5) [I130]; Attempt (read through Θ); Qf [I145]; UsesClaim [I178] (ExplUse is defined, D13.3) [r3: A3; S2(iii): was 'ExplUse [I148]']; AtRest [I149]; Org_ℓ(h) [I151]; q(o), the contract operative at an occurrence, and Rec_h', a provenance record in h', both read through Θ [I165] [owner S41: Q6]. Below (D9.2) and subhistory (D11.3, I151) are defined. Contrib is dropped (D13.7). Each is stated, not defined: read through Θ where it is a claim about a history (Occurs, Attempt, Prepares, BindingConstruction, TransferComposite, Integrated, UsesClaim, AtRest, Org_ℓ(h), MadeFrom, Rec, Chg, Rule), a declared input otherwise (FC98 (b)) [r2b: second check; Q4 ruled, no text change]. Held
(cont.) (D18.1) and CT (D12.2) are defined. [r2: A3; D0.2, H20, D13.6, H14, H19; A2: Off] [r3: A3; S-b (F7)] Also used and not listed after round 2 (FC32.new1 (c), computed from the program's D18.1): declared inputs L522 does not list: C_I, J_p (L477), 𝒱 (D7.4), the stated construction (L481, D15.8), Desc (D3.6); read through Θ: surv's Env (D12.1, I177), UsesClaim (D13.3, I178), 𝔓^adv_Θ (D16.4), trans (D9.11); defined: parts (D12.4), Event (D11.1), Expl (an atom, D16.XV), 'immediately after' (D13.8, I173) [r3: A1; B9]. L522's list is not changed (new items would be prose, S40); D18.1's nodes and folds are I181. Used by D16.XV's shapes and defined nowhere (D16.XV says so of each): Work(kl) [(Elim), L540]; 'without loss', 'operates on' [(Prov) (ii), (iii), L542]; 'fails to capture', 'not creative' [(QF), L544]. [r4: A3; S4 (F3): 'subhistory' was among the primitives 'stated, not defined'; D11.3 defines it (I151); the program's DEP['Episode'] loses the sink 'subhistory'] [r4: A3; S6 (F4): D16.XV's five undefined terms were in no list; the program's DEP['DefeatConds'] gains Work, WithoutLoss, OperatesOn, FailsToCapture, NotCreative, classed in D0_2_R4A3 (FC32.new1 (c))]

## §1 Organizations (O)

> L88 | D=(V,(X_v)_{v\in V},J,B,A,L).

> L91 | \(V\) is a set of ports, each with a nonempty value domain \(X_v\). A valuation is an element of \(X_D=\prod_v X_v\). \(J\) indexes components; each component \(j\) has a footprint \(V_j\subseteq V\). \(B\) is a set of boundary conditions. \(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\).

> L94 | L_j(a,b)\subseteq\prod_{v\in V_j}X_v .

⟦B1 ⟨E Dec Expl Suff Nec⟩⟧ D1.1
**D1.1 Organization.** D = (V, (X_v)_{v∈V}, J, (V_j)_{j∈J}, B, A, ·, 1, L) with: V a set (ports), each X_v ≠ ∅; X_D := ∏_{v∈V} X_v (valuations); J a set (components), each with a footprint V_j ⊆ V; B a set (boundaries); A a set (admitted edits) with a partial composition · : A × A ⇀ A, Kleene-associative, with identity 1 ∈ A **[I01]**; L a function from J × A × B with L_j(a,b) ⊆ ∏_{v∈V_j} X_v. No law ties L_j(a2·a1, b) to L_j(a1,b) and L_j(a2,b) **[I02]**. V and J are the same under every edit **[I03]**.

> L105 | Values of ports may be paths, functions, fields, mathematical structures or histories. Cyclic constraints are admitted. Several solutions remain several.

The X_v are arbitrary sets; no order on J is assumed; nothing selects one solution.

> L100 | \operatorname{Sol}_D(a,b)=\{z\in X_D:\forall j\in J,\ z|_{V_j}\in L_j(a,b)\}. \tag{O}

⟦B1 ⟨E Dec Expl Suff Nec⟩⟧ D1.2
**D1.2 Solutions (O).** Sol_D(a,b) := {z ∈ X_D : ∀j ∈ J, z|V_j ∈ L_j(a,b)} — the text's (O).

> L103 | A deleted component imposes the full relation on its ports.

> L339 | has a target \(D\) in which the ports and components a rival account would need are absent

⟦B1 ⟨E Dec Expl Suff Nec⟩⟧ D1.3
**D1.3 Deletion and absence.** j is deleted at (a,b) when L_j(a,b) = ∏_{v∈V_j} X_v. For G ⊆ J, D−G is D with L_j(a,b) := ∏_{v∈V_j} X_v for every j ∈ G and every (a,b). An absent component is a deleted one; an absent port is one on which every component imposes the full relation **[I03]**.

⟦FROZEN⟧ D1.4
**D1.4 Subnetwork.** A subnetwork is a set N ⊆ J (possibly empty), with V_N := ∪_{j∈N} V_j for N ≠ J_D and V_{J_D} := V_D (so Sol_{J_D} = Sol_D) **[I138]**, and Sol_N(a,b) := {z ∈ ∏_{v∈V_N} X_v : ∀j ∈ N, z|V_j ∈ L_j(a,b)}: the constraints of N alone, the rest of D ignored **[I14]**. [r2: A2; D1.4, I14, FC25 (b)]

## §2 Setting edits and roles

> L103 | An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one. A changed rule is a changed component.

> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it

⟦FROZEN⟧ D2.1
**D2.1 Setting edit; the assigning component.** An edit a sets port v through component j at b when L_j(a,b) = {w ∈ ∏_{V_j} X : w_v = x} for some x ∈ X_v and L_k(a,b) = L_k(1,b) for every k ≠ j **[I04]**. Set_v := {a ∈ A∖{1} : ∀b ∃j, a sets v through j at b} **[I122]**. asg(v) := the component through which the edits of Set_v set v, when there is exactly one; undefined otherwise **[I04]**. 'A changed rule is a changed component': an edit that alters L_j is a change of j, and nothing else is added. [r2: A1; D2.1, D2.2, I80 (fixed: 1 ∉ Set_v)]

> L109 | No role assignment is supplied. A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly.

⟦B1⟧ D2.2
**D2.2 Input.** Input_A(v) :⟺ Set_v ≠ ∅.

> L109 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

⟦B1⟧ D2.3
**D2.3 Output.** Out(v, j) :⟺ v ∈ V_j and, for every b ∈ B and all w, w' ∈ L_j(1,b), w|_{V_j∖{v}} = w'|_{V_j∖{v}} ⇒ w_v = w'_v **[I05]**.

> L109 | A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below).

⟦FROZEN⟧ D2.4
**D2.4 Observation edits.** For a port o with j = asg(o) and a port m ∈ V_j ∖ {o} with asg(m) defined ('what it reports'): Obs(o,m) := {a ∈ Alt_j ∖ Slc_j : L_asg(m)(a,b) = L_asg(m)(1,b) ∀b} (Alt_j: D4.6; Slc_j: D2.6) **[I06, fixed: R-ii]**. Obs := ∪_{o,m} Obs(o,m). Observation(o) :⟺ Obs(o,m) ≠ ∅ for some m. Other choice recorded: R-i (any a ∈ Alt_j, setting edits of o included), under which no reader of an assigned port is causal (FC2.new1). [r2: A1; D2.4, I06, H01, FC11; T1]

> L109 | The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read.

⟦B1⟧ D2.5
**D2.5 Direction.** dir(D) := (Input_A, asg): which ports A sets and which component each setting edit replaces. Output status (D2.3) does not use A (FC02). [r2: A1; registered as I123]

⟦FROZEN⟧ D2.6
**D2.6 Interventions on a component.** Slc_j := {a ∈ Alt_j : ∀b [L_j(a,b) ≠ L_j(1,b) ⇒ ∃v ∈ V_j, asg(v) = j, ∃x: L_j(a,b) = {w : w_v = x}]}: the edits that replace j by a slice on a port j assigns, single or composite, whatever else they alter **[I125]**. [r2: A1; new; H01, D4.6]

**Vague.** 'The component assigning that port' (L103, L109, L119) presupposes one assigning component per port; with a relational component (L325's L = H cot θ determines H given L and θ as well as L given H and θ), L109's 'output' does not single one out. D2.1 reads the assigning component off the setting edits, so that 'no role assignment is supplied' stays so [I04]. L109's observation has two readings, and its 'that is' clause equates a condition on A with a signature, which (K) builds on a contract C, not on A [I06]; the families of §4 differ between the readings on the pole's own contract (FC07). [r2: I06 fixed by D2.4 (A1; T1)]

## §3 Questions and contracts

> L138 | p=(D,\ C,\ b_0,\ \mathcal Q,\ O_p,\ \rho_p).

> L141 | The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over; it contains the baseline \((1,b_0)\). \(\mathcal Q\) is a specified set-theoretic operation on \(D\), its solutions and its component structure, with codomain \(Y_p\).

> L147 | \(O_p\) is the set of aims being addressed or protected.

⟦B1 ⟨E Dec Expl Suff Nec⟩⟧ D3.1
**D3.1 Question.** p = (D, C, b0, Q, δ_D, O_p, ρ_p): the text's tuple with the designation δ_D added **[I20]**; C ⊆ A × B with (1, b0) ∈ C; O_p a set of aims (§14); ρ_p the contract's provenance (D3.4).

> L144 | \operatorname{Ans}_p(a,b)=\mathcal Q(D,a,b). \tag{Q}

> L253 | The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one.

⟦B1 ⟨E Dec Expl Suff Nec⟩⟧ D3.2
**D3.2 Query and answers.** Q is an operation on evaluated organizations: Q(O, a, b; δ_O) ∈ Y_p ∪ {⊥}, a function of Sol_O(a,b), of (L^O_j(a,b))_{j∈J_O} and of the ports and components the designation δ_O names **[I20, I21]**. Ans_p(a,b) := Q(D, a, b; δ_D). For a candidate's organization E with designation δ_E (supplied with the transport, D5.3): Ans_E(a',b') := Q(E, a', b'; δ_E). An answer is determined when it is not ⊥ **[I21]**. The port-reading query: Q_w(O, a, b; δ) := the single value of the projection of Sol_O(a,b) on δ(w) if there is exactly one, ⊥ otherwise.

> L151 | A production question has a \(\mathcal Q\) that reads an output port and a \(C\) containing interventions on upstream ports. An identification question has a \(\mathcal Q\) that computes a fibre and a \(C\) containing edits to the observed value. An obstruction question has a \(\mathcal Q\) that returns reachable or unreachable.

⟦FROZEN⟧ D3.3
**D3.3 Respects** **[I72]**. v ⇝ w :⟺ ∃n ≥ 1, j_1…j_n, u_1…u_n: v ∈ V_j1∖{u_1}; Out(u_i, j_i) ∀i ≤ n; u_i ∈ V_j(i+1)∖{u_(i+1)} ∀i < n; u_n = w **[I126]**. Prod(p) :⟺ Q = Q_w with Out(w, j) for some j, and C holds a setting edit of some v ⇝ w. Ident(p) :⟺ Q returns a fibre g⁻¹(obs(a,b)) (E2), obs(a,b) := the one value of g on Sol_D(a,b) if there is one, ⊥ otherwise, with ≠ in X_g ∪ {⊥} (⊥ ≠ x, ⊥ = ⊥, as D3.2, D6.4) **[I172]** [r3: A1; B6: was 'obs(a,b) the observed value g takes on Sol_D(a,b)'; Q15's convention (S41); FC28.new2], and ∃(a,b),(a',b') ∈ C: obs(a,b) ≠ obs(a',b') **[I163]** [r2b: second check; R4: was 'C holds edits to the observed value', which C_id = {1} × B (E1, L325) does not meet; L151 writes it (R4-L151); FC28]. Obst(p) :⟺ Y_p = {reachable, unreachable}. Rule-status: Rule_C (D4.6); purpose-achievement: (AR) (D14.8). Prod, Ident, Obst are L151's conditions (by 'fixed by', both ways); they may overlap (FC36). [r2: A1; D3.3, I72]

> L155 | A claim that an episode *found* a question requires \(\rho_p=\text{constructed}\) for the contract in question, with the trace.

⟦FROZEN⟧ D3.4
**D3.4 Provenance of a contract.** ρ_p ∈ {declared, selected, constructed}, with a trace, the contract as the content (E8): selected :⟺ C survived in a population 𝒞 of contracts under a variation operator and a survival condition in a physical history (read through Θ); constructed :⟺ C results from an episode with a construction trace; declared :⟺ neither (L155) **[I127]**. Found(p) requires ρ_p = constructed. [r2: A1; D3.4, H20]

> L159 | Where the claim states why it restricts the contract as it does, an assessment of the restriction is given with that statement; where it states none and an assessment turns on one, that statement is a missing declared input (Part XIV).

⟦B1 ⟨E Expl Suff Nec⟩⟧ D3.5
**D3.5 Scope statement.** Σ is a declared input naming Excl(Σ) ⊆ A × B **[I27]**; Stated(C, Σ) :⟺ (A × B) ∖ C ⊆ Excl(Σ). Why the question is asked on C and not on a wider contract is a further declared input; no condition below uses it. [r2: A2; L257 now states Stated(C,Σ) (A2-T1); I27 in the text]

> L161 | A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.

> L161 | An assessment is an event with a frozen contract (Part 0, grievance 10): a change to \(C\) or \(\mathcal Q\) during it, left unrecorded, makes the record name a claim other than the one assessed.

> L367 | A proposition indexed to a contract remains that proposition when a later theory changes the current contract. A new index is a new claim.

⟦FROZEN⟧ D3.6
**D3.6 Defects; indexing** **[I76]**. With a description Desc that p answers to: BadTarget :⟺ the organizations meeting Desc are not exactly one; BadBaseline :⟺ Sol_D(1,b0) = ∅ (b0 ∉ B is excluded by D3.1: (1,b0) ∈ C ⊆ A×B) [r2: A1; D3.6]; BadReq :⟺ the conditions Desc puts on (C, Q) have no joint instance. Every claim about a question is indexed by (D, C, b0, Q, δ_D); a claim with another index is another claim.

> L151 | Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other.

⟦B1 ⟨E Dec Expl Suff Nec⟩⟧ D3.7
**D3.7 Different questions.** p ≠ p' when (C, Q) ≠ (C', Q') on the same D. 'An answer to one is not an answer to the other' is read narrowly: Acc on p does not by itself give Acc on p' **[I73]**; the wide reading (no candidate meets (E) on both) is a claim to test (FC34). [r2: A1; narrow reading in the text (T8)]

**Vague.** L141 makes Q an operation 'on D'; (A) at L250 applies it to E, whose ports are not D's. How the one query reads another organization is not said [I20]. 'Determined' (L255) presupposes answers that can fail to be determined; Q's codomain Y_p has no such value [I21]. [r2: codomain Y_p ∪ {⊥} in the text (T7)]

## §4 Signatures, kinds and families

> L116 | \operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K}

⟦B1 ⟨E Dec Expl Suff Nec SCdef⟩⟧ D4.1
**D4.1 Signature (K).** sig_C(j) := {(a, b, L_j(a,b)) : (a,b) ∈ C}; equivalently, the function on C sending (a,b) to L_j(a,b).

> L119 | Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide. A kind is an equivalence class of components under this relation.

⟦B1⟧ D4.2
**D4.2 One kind on C.** j ~_C j' :⟺ there is a bijection β: V_j → V_j' with X_v = X_β(v) for every v, and L_j'(a,b) = β_*(L_j(a,b)) for every (a,b) ∈ C, where β_*(R) := {w∘β⁻¹ : w ∈ R} **[I10]**. Kinds on C are the classes of ~_C. C' is coarser than C when C' ⊆ C, finer when C' ⊇ C **[I11]**.

> L119 | A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection

⟦B1⟧ D4.3
**D4.3 Reading through a transport.** For k ∈ J_E and a transport t = (π,τ,σ,λ): sig^t_C(k) := the function on C sending (a,b) to L^E_k(τ(a),σ(b)) **[I12]**; τ[C] := {(τ(a),σ(b)) : (a,b) ∈ C}. For candidates ℰ, ℰ' of one question, k ∈ J_E and k' ∈ J_E' are of one kind on C when sig^t_C(k) and sig^{t'}_C(k') coincide under a footprint bijection (as in D4.2).

> L119 | Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.

⟦B1 ⟨E Dec Expl Suff Nec⟩⟧ D4.4
**D4.4 Signature of a counterpart.** For k ∈ Γ with λ(k) = (N_k, θ_k, κ_k) (D5.1): sig_C(λ(k)) := the function on C sending (a,b) to proj^λ_{V_k} Sol_{N_k}(a,b) (D5.2). This extends (K) from components to subnetworks **[I13]**.

⟦B1⟧ D4.5
**D4.5 Change and invariance on a contract.** For a set 𝒳 of edits: Changes_C(j, 𝒳) :⟺ some (a,b) ∈ C with a ∈ 𝒳 has L_j(a,b) ≠ L_j(1,b); Inv_C(j, 𝒳) :⟺ every (a,b) ∈ C with a ∈ 𝒳 has L_j(a,b) = L_j(1,b) **[I09]**. 'Variable under' is Changes; invariance holds vacuously when C holds no edit of 𝒳.

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

> L124 | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

> L125 | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

> L347 | Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\).

⟦FROZEN⟧ D4.6
**D4.6 Families.** For a component j, O_j := {v : asg(v) = j}, the ports j assigns, and Set_{O_j} := ∪_{v∈O_j} Set_v **[I04, I124]** [r3: A1; S-D1: was 'o_j is the port j assigns (asg(o_j) = j)', singular; the program already took the union (core.Roles.set_oj); FC13.new1]. Alt_j := {a ∈ A : L_j(a,b) ≠ L_j(1,b) for some b}.
- Causal_C(j) :⟺ Changes_C(j, Set_{O_j}) ∧ Inv_C(j, Obs), Obs as D2.4. [r3: A1; S-D1]
- Meas_C(j, m) :⟺ m ∈ V_j, asg(m) defined, asg(m) ≠ j, Inv_C(j, Set_m) ∧ Changes_C(j, Alt_j ∖ Slc_j) **[I07]**.
- Rule_C(j) :⟺ Inv_C(j, World_j) ∧ Changes_C(j, Alt_j ∖ Slc_j), with World_j := ∪ {Set_v : asg(v) ≠ j} **[I08]**.
- A constitutive status is Rule_C (L347; FC09).
- m ∈ V_j ∧ asg(m) ∉ {j, undefined} ∧ Changes_C(j, A ∖ Slc_j) ⇒ Meas_C(j, m) (FC4.new1).
[r2: A1; D4.6, U5, H01, I102 (2nd clause trimmed), I08; T5, T6]

> L127 | These are descriptions of patterns in (K), not additional data.

Each family predicate is a function of D and C alone (FC13).

**Vague.** 'Observation edits' (L123) and 'the measured port' (L124) rest on L109's observation, which has two readings (D2.4). 'The world' and 'the rule' (L125) are not fixed [I08]. L127's gloss of a measurement's signature ('change the part and the reading follows') is a condition on solutions, which (K) does not record (FC08). L121 names four things and the bullets give three families (FC09). [r2: composites classed by Slc_j (D2.6); L127's gloss replaced by FC4.new1 (T6)]

## §5 Transports and fidelity

> L186 | t=(\pi,\tau,\sigma,\lambda)

> L189 | where \(\pi:X_D\to X_E\) on the stated scope, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation.

⟦B2 ⟨E Expl Suff⟩⟧ D5.1
**D5.1 Transport.** t = (π, τ, σ, λ) from D to E: π: X_D ⇀ X_E, defined at least on Sol_D(a,b) at every pair t translates **[I16]**; τ: A_D ⇀ A_E and σ: B_D ⇀ B_E **[I17]**; λ assigns each k ∈ J_E a triple (N_k, θ_k, κ_k): N_k ⊆ J_D a subnetwork, θ_k: V_k → V_{N_k} injective, and value maps κ_{k,v}: X^D_{θ_k(v)} → X^E_v (the identity where the domains agree) **[I14]**. t translates (a,b) :⟺ a ∈ dom τ, b ∈ dom σ, and π is defined on Sol_D(a,b).

> L233 | the relation obtained by imposing the constraints of \(\lambda(k)\), projecting away its hidden ports and carrying what remains to \(V_k\) by the port translation of \(\lambda\)

⟦B2 ⟨E Expl Suff⟩⟧ D5.2
**D5.2 Projection.** For S ⊆ ∏_{v∈V_{N_k}} X_v: proj^λ_{V_k}(S) := {(κ_{k,v}(z_{θ_k(v)}))_{v∈V_k} : z ∈ S}. The hidden ports are V_{N_k} ∖ θ_k[V_k] **[I14]**.

> L231 | An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI.

⟦B2 ⟨E Expl Suff⟩⟧ D5.3
**D5.3 Candidate.** ℰ = (E, p, t, Γ, δ_E): E an organization, t a transport from p's target to E, Γ ⊆ J_E the commitments, which are the active components **[I15]**, δ_E the designation of Q in E **[I20]**. The background is J_E ∖ Γ with B_E.

> L236 | \operatorname{proj}^{\lambda}_{V_k}\!\big[\operatorname{Sol}_{\lambda(k)}(a,b)\big]=L_k(\tau(a),\sigma(b)). \tag{F1}

⟦B2 ⟨E Dec Expl Suff Nec⟩⟧ D5.4
**D5.4 (F1).** F1_C(ℰ) :⟺ for every k ∈ Γ and every (a,b) ∈ C: proj^λ_{V_k}[Sol_{N_k}(a,b)] = L^E_k(τ(a),σ(b)).

> L242 | \pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b)),\qquad \tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1). \tag{F2}

⟦B2 ⟨E Dec Expl Suff Nec⟩⟧ D5.5
**D5.5 (F2).** F2eq_C(ℰ) :⟺ for every (a,b) ∈ C: π[Sol_D(a,b)] = Sol_E(τ(a),σ(b)). Hom(τ) :⟺ τ(1) = 1, and for all a1, a2 ∈ dom τ with a2·a1 defined, τ(a2)·τ(a1) is defined and equals τ(a2·a1) **[I18]**. F2_C := F2eq_C ∧ Hom(τ).

> L250 | \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A}

⟦B2 ⟨E Expl Suff Nec⟩⟧ D5.6
**D5.6 (A).** A_C(ℰ) :⟺ for every (a,b) ∈ C: Ans_E(τ(a),σ(b)) = Ans_p(a,b), with ⊥ = ⊥ **[I21]**.

> L189 | A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V.

> L245 | Together they are fidelity at every level the contract reaches.

> L247 | **Question fidelity.**

⟦FROZEN⟧ D5.7
**D5.7 Faithful; question fidelity.** Faithful_C(t) := F1_C ∧ F2_C (L189, L245) **[I49]**. QFid_C := A_C (L247's heading, a separate name). Fid⁺_C := F1_C ∧ F2_C ∧ A_C only where L630 is read so (FC104); L220's 'fidelity' is the narrow extent, Viol of D12.7 (Q11; L189; L247 names (A) apart), and only so does Sel ∧ Viol(a,b) ⇒ (a,b) ∉ H hold (FC104.new1 (b)); R3A1-T5 writes it at L220, settling FC104 there [r3: A1; W1/W2: was 'only where L220 or L630 is read so']; L245, L247 and L520 (text 104) need no wide extent. At a pair (a,b): F1 and F2eq at that pair alone; Hom is a condition on τ as a whole, never at a pair **[I18]**. [r2: A2; D5.7, I49, matter 12; L520 by A3 (A3-L520.1)]

**Vague.** One word, two extents: L189 and L245 give the narrow one; L247's heading and L520 (after round 1) the wide one; L630 keeps 'the fidelity and the answers' apart (FC104). The domain of π ('on the stated scope') and which pairs a transport 'translates' (L315) are not fixed [I16, I17]. Port translations carry ports, and nothing in the text carries values between different domains [I14]. [r2: L520 writes (E)'s five conjuncts (A3); Fid⁺ open only for L220, L630]

## §6 Dependence, non-vacuity, Account [S106: was 'Non-circular dependence, non-vacuity, Account']

⟦B2 ⟨E Expl Suff Nec⟩⟧ D6.1
**D6.1 Deletion in a candidate.** For G ⊆ Γ, E−G as in D1.3; Ans_{E−G}(y) := Q(E−G, y; δ_E).

> L255 | **Non-circular dependence.** The answer follows by evaluating \(E\) under its independent boundary conditions.

⟦B2 ⟨E Expl Suff Nec⟩⟧ D6.2
**D6.2 NC0.** Holds of every candidate: every answer is computed by evaluating E at (τ(a),σ(b)), and σ(b) depends on b alone **[I23]**. [S106: L255's 'independent' deleted (S106-T2): under this reading it adds nothing; its registered other reading, I23 (a) (E's boundary data carry nothing of the target's answer), is NC1's boundary clause, the written-in test, out of (E) by S45 (I187)]

> L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements.

⟦FROZEN⟧ D6.3
**D6.3 NC1 (no answer slot).** Det_C := {(a,b) ∈ C : Ans_p(a,b) ≠ ⊥}. Slot_C(ℰ, k) :⟺ δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C [t translates (a,b) ∧ {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}] **[I135; quantifier I136; I184]**; likewise for a boundary coordinate of E whose value at σ(b) is Ans_p(a,b), t translating (a,b) [I79]. NC1(ℰ) :⟺ no k ∈ J_E and no boundary coordinate is a slot, in E as given at grain ℓ **[I24 (b), I83 (b), I28]**. [r2: A2; D6.3, I24, I83, E19; FC23 (c), (d)] [r3: A2; W3: no change; the quantifier ∀ over Det_C (I136) is the owner question R3-Q1 (OQ-R3A2-1); readings computed: every (as here), some, some-exempt, some-exempt-set (core.SLOT_QUANTIFIER, default every; FC23.new1); the exemption's extent is I176; L255 held until the owner answers] [S106: S44, S45: NC1 is not a conjunct of (E) (D6.5, D6.7); Slot_C and NC1 stay defined here, as content a criticism can point at; Slot_C(ℰ,k) ⟺ Det_C ≠ ∅ ∧ Pin(ℰ,k;a,b) at every (a,b) ∈ Det_C (FC23.new3 (a)); the quantifier (I136) and the exemption's extent (I176) now read Slot only, and (E) is the same under all four readings (FC23.new1 (h)); R3-Q1 answered: neither side (S44), the test out (S45); I24 settled by its registered other choice (a), NC1 left out; L255's two sentences deleted (S106-T3); L273 replaced by the pointer (D6.3, FC23, FC24) (S106-T6)] [S106b: Pin(ℰ, k; a, b) :⟺ (a,b) ∈ Det_C ∧ t translates (a,b) ∧ δ_E ∈ V_k ∧ {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)} **[I184]**: Slot's clause at one pair;
(cont.) 'some' is Pin at one pair; was D6.11 (a), withdrawn with D6.11 (objection 1). The owner's sign (S44): the red part pins at Monday, the blue part at Tuesday, neither a slot under 'every'; one part giving both is one (FC23.new2 (a), (b)). S106-T6 was the formula Slot_C(ℰ,k) ⇏ ¬Account(ℰ) (objection 2)] [r4: A2; B8, S3 (F1): was '∀(a,b) ∈ Det_C: {w_δE : …} = {Ans_p(a,b)} [I135; quantifier I136]', with no 't translates (a,b)' (D5.1): where τ(a) or σ(b) is undefined at a determined pair the clause had no value (FC23.new4 (a)); with π undefined on Sol_D(a,b) there it held while Pin failed (FC23.new4 (b)); now inside the ∀, as Pin and core.slot have it, and the [S106b] equivalence Slot ⟺ Det_C ≠ ∅ ∧ Pin at every pair of Det_C holds of D6.3 as written (FC23.new3 (a), FC23.new4 (c)). B9: Pin at a pair whose own edit alters k counts as a pin, I184 as registered **[I194]** (FC23.new4 (d)); (E) reads neither]

> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\)

> L255 | evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.

⟦FROZEN⟧ D6.4
**D6.4 NC2 (a contrast lost under deletion).** With x = (τ(a),σ(b)) and x0 = (1,σ(b0)):
- Contrast(E; x) :⟺ Ans_E(x) ≠ Ans_E(x0) in Y_p ∪ {⊥}, with ⊥ ≠ y for y ∈ Y_p and ⊥ = ⊥, as D8.2 reads 'differ' **[I21]**; that is, [Ans_E(x) ≠ ⊥ ∧ Ans_E(x0) ≠ ⊥ ∧ Ans_E(x) ≠ Ans_E(x0)] ∨ [Ans_E(x) = ⊥ ∧ Ans_E(x0) ≠ ⊥] ∨ [Ans_E(x) ≠ ⊥ ∧ Ans_E(x0) = ⊥] [owner S41: Q15: symmetric; was the first two disjuncts only, a determined baseline asked (I22, asymmetric); L255 writes it (S41-Q15)];
- Lost(E, G; x) :⟺ [Ans_{E−G}(x) ≠ ⊥ ∧ Ans_{E−G}(x0) ≠ ⊥ ∧ Ans_{E−G}(x) = Ans_{E−G}(x0)] ∨ [for some y ∈ {x, x0}: Ans_E(y) ≠ ⊥ ∧ Ans_{E−G}(y) = ⊥];
- NC2(ℰ) :⟺ there are (a,b) ∈ C and G ⊆ Γ, G ≠ ∅, with Contrast(E; x) ∧ Lost(E, G; x).

⟦FROZEN⟧ D6.5
**D6.5 Dependence.** Dependence(ℰ) :⟺ NC0 ∧ NC2 **[I25, I24 (a)]**; NC0 holds of every candidate (D6.2), so Dependence(ℰ) ⟺ NC2(ℰ): some contrast of E's answers at a pair of C is lost when a nonempty block of Γ is deleted. [S106: S44, S45: was 'Non-circular dependence. NonCircular(ℰ) :⟺ NC0 ∧ NC1 ∧ NC2 [I25]'; the name 'non-circular' is the written-in test's and goes with it: L255's heading, L257, L262, L275, L343, L520 write Dependence (S106-T1, T4, T5, T7, T9, T12; I188); a candidate fails Dependence on a contract with no contrast its commitments carry, the written-in one and the mechanism alike (FC21, FC22, FC29)]

> L257 | **Non-vacuity.** \(\operatorname{Sol}_D(1,b_0)\neq\varnothing\). The contract \(C\) is a stated subset of the edits the target admits, and every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently.

⟦B2 ⟨E Expl Suff Nec⟩⟧ D6.6
**D6.6 Non-vacuity.** NonVacuous(ℰ) :⟺ Sol_D(1,b0) ≠ ∅ ∧ Stated(C, Σ) (D3.5) **[I27]**.

> L262 | \operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}. \tag{E}

⟦FROZEN⟧ D6.7
**D6.7 Account (E).** Acc(ℰ) :⟺ F1_C ∧ F2_C ∧ A_C ∧ Dependence ∧ NonVacuous. Its arguments are (D, C, b0, Q, δ_D, E, t, Γ, δ_E, Σ): no assessor, no history, no provenance (FC30), and no grain. [S106: S44, S45: was '… ∧ NonCircular ∧ NonVacuous', with ℓ among the arguments; ℓ entered only through NC1's 'at the declared grain' (I28); L262 and L520 write it (S106-T5, T12). Round 3's (E) is Acc ∧ NC1: every candidate it admitted is still admitted, and those it excluded for a slot alone now meet (E) (`model after S106/s106_cases.py`: nine worked cases move under the reading 'every', five more under another reading only)]

> L231 | meets \(\operatorname{Account}(\mathcal E)\) exactly when the following four conditions are met

⟦FROZEN⟧ D6.8
**D6.8 The four conditions.** The four headings of Part V: Component fidelity = F1 ∧ F2 (L233–L243), Question fidelity = A (L247), Dependence (L255), Non-vacuity (L257). (E) writes them as five conjuncts (FC31). [S106: was 'Non-circular dependence (L255)' (S106-T1)]

> L257 | A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets non-circular dependence

⟦FROZEN⟧ D6.9
**D6.9 Relabeling.** a is a relabeling for p when, at every b with (a,b) ∈ C, Ans_p(a,b) = Ans_p(1,b0), with ⊥ = ⊥ **[I26]** (FC21). [r2: A2; D6.9, I26 ('≠ ⊥' dropped); A2-T2, A2-T3] [r4: A2; W4: the quote is text 103's (preamble); L257 now reads 'admits no candidate that meets (F2), (A) and \(\operatorname{Dependence}\) (FC21)' (A2-T3, S106-T4)]

> L269 | A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing one.

⟦B2 ⟨Expl Suff Nec⟩⟧ D6.10
**D6.10 Tables.** E_tab: one active component k with λ(k) = (J_D, θ, κ) (the whole target, projected on k's ports) and L_k(a',b') := proj^λ_{V_k} Sol_D(1,b0) at every (a',b'); E_enc: the same with L_k(τ(a),σ(b)) := proj^λ_{V_k} Sol_D(a,b) **[I32]** (FC25). [S106: E_enc meets (E) wherever its answer varies over C and Sol_D(1,b0) ≠ ∅ with the scope stated (FC25.new2 (a)); its one component is a slot (FC25.new2 (b)); round 3's (E) excluded it for the slot alone (the pole's C1, C2: FC25.new2 (c)); E_tab is untouched: it fails (F1) where the projection moves (FC25)]

**Vague.** NC1's 'unanalysed', 'at the declared grain' and 'structural' have no definition in (O) or (Q) [I24, I28], and NC2, the one fully formal clause, does not exclude a lookup of the answer (FC23): the exclusion of 'p because p' rests on the least defined sentence. 'In the claimed way' is not fixed [I22] [owner S41: Q15: I22 settled; the contrast is ≠ in Y_p ∪ {⊥}, and L255 no longer has the phrase (S41-Q15)]. NC0 adds no condition as read [I23]. Non-vacuity's second sentence is a condition on a statement, not on relations under the changes in C (FC33). [r2: NC1 rewritten (D6.3; I135); L265 now excepts Stated(C,Σ) (A2-T4); L269 in symbols (A2-T5)] [S106: NC1 is out of (E); its undefined words ('unanalysed', 'at the declared grain', 'structural') now bear on Slot (D6.3) only, which (E) does not read; (E) rests on its formal clauses alone: (F1), (F2), (A), NC2 and non-vacuity; L273's exclusion of 'p because p' is gone (S106-T6), and FC23 computes that the lookup meets (E) where its answer varies (FC23 (e))]

## §7 Routes: (S), (B), (D)

> L287 | Fix \(\mathcal E\) and a declared restriction operation. For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).

> L231 | for \(E|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E|W\), and \(\Gamma'\) is \(W\).

⟦B2⟧ D7.1
**D7.1 Restriction.** E|W := E − (Γ ∖ W), with t restricted to W and commitments W **[I29]**; Acc(E|W, p) := Acc((E|W, p, t|W, W, δ_E)).

> L290 | \mathsf S_{E,p}=\{W\subseteq\Gamma:\operatorname{Account}(E|W,p)\}. \tag{S}

> L293 | No upward closure and no minimal member are assumed. For nonempty \(B\subseteq W\),

⟦B2⟧ D7.2
**D7.2 Routes (S).** S_{E,p} := {W ⊆ Γ : Acc(E|W, p)}. A route is a member of S_{E,p}.

> L296 | \operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}. \tag{B}

⟦B2⟧ D7.3
**D7.3 Critical block (B).** CB(B; W) :⟺ ∅ ≠ B ⊆ W ∧ W ∈ S ∧ W ∖ B ∉ S.

> L302 | \operatorname{Boundary}_{E,p}=\{(v,w)\in\mathcal V^2:\operatorname{Account}(E_v,p)\neq\operatorname{Account}(E_w,p)\}. \tag{D}

⟦FROZEN⟧ D7.4
**D7.4 Boundary (D).** For a declared family 𝒱 of organization edits: Boundary := {(v,w) ∈ 𝒱² : Acc((E_v, p, t_v, Γ_v, δ_v)) ≠ Acc((E_w, p, t_w, Γ_w, δ_w))}, each v ∈ 𝒱 declaring (E_v, t_v, Γ_v, δ_v), t_v the transport the operation carries t to, Γ_v the commitments it leaves and δ_v the designation it carries δ_E to (L231; D5.3, I20) **[I195]**. [r2: A2; D7.4] [r4: A2; N1 (B-N1, W-N1, S-N1, C-N1) (F2): was 'Acc(E_v, p) ≠ Acc(E_w, p)', each v declaring (E_v, t_v, Γ_v): Acc takes δ (D6.7); without δ_v Boundary is no function of the declared data (FC42.new1 (b); FC90.new1 (c)); δ_v carried, not quantified: L253 holds the query fixed (FC42.new1 (d)); core.boundary; L302 unchanged (the text's candidate carries no designation, I20)]

> L305 | then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\), and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\)

⟦B2⟧ D7.5
**D7.5 Contributory; globally indispensable.** Contrib(d) :⟺ CB({d}; W) for some W ∈ S. Indisp(d) :⟺ Γ ∖ {d} ∉ S.

> L313 | A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it

⟦B2⟧ D7.6
**D7.6 No work by itself.** NoWork(d) :⟺ S ≠ ∅ and, for every W ∈ S, W ∪ {d} ∈ S and W ∖ {d} ∈ S.

The worked examples of L307–L311 are read as set systems S ⊆ P(Γ) **[I30]**; the infinitary example's routes are the sets with unbounded index sets **[I31]**.

## §8 Conflict, rivals, conflict with a claim

> L315 | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both

⟦B4⟧ D8.1
**D8.1 Meeting at a pair under hypothetical relations.** For a pair (a,b) and R = (R_j)_{j∈J_D} with R_j ⊆ ∏_{v∈V_j} X_v: D^R is D with L_j(a,b) replaced by R_j; Ans^R_p(a,b) := Q(D^R, a, b; δ_D). Meets_ab(ℰ, R) :⟺ for every k ∈ Γ, proj^λ_{V_k}[Sol^R_{N_k}(a,b)] = L^E_k(τ(a),σ(b)); π[Sol_{D^R}(a,b)] = Sol_E(τ(a),σ(b)); and Ans_E(τ(a),σ(b)) = Ans^R_p(a,b) **[I19]**. BothMeet_ab(R) :⟺ Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R).

⟦FROZEN⟧ D8.2
**D8.2 Conflict.** For (a,b) ∈ A_D × B_D (admitted: D1.1, L141) that both transports translate, in C or outside it: Conf(ℰ, ℰ'; a,b) :⟺ Ans_E(τ(a),σ(b)) ≠ Ans_E'(τ'(a),σ'(b)) in Y_p ∪ {⊥}, with ⊥ ≠ y for y ∈ Y_p and ⊥ = ⊥ **[I21]**, ∨ [∃R Meets_ab(ℰ,R) ∧ ∃R' Meets_ab(ℰ',R') ∧ ¬∃R'' BothMeet_ab(R'')]. [r2: A2; D8.2, H10; A2-T8]

⟦FROZEN⟧ D8.new1
**D8.new1 One counterpart; different relations.** k ∈ Γ and k' ∈ Γ' have one counterpart :⟺ λ(k) = (N, θ, κ), λ'(k') = (N, θ', κ'), θ[V_k] = θ'[V_k'], θ and θ' bijections onto those ports; β := θ'⁻¹∘θ; DiffRel_ab(k,k') :⟺ L^{E'}_{k'}(τ'a,σ'b) ≠ β_*(L^E_k(τa,σb)) (L562, L564); κ as I14. [r2: A2; new; I36 fixed less κ; FC44; A2-T9]

> L315 | Whether two candidates conflict depends on their organizations and transports and on the target's ports and components, not on anyone's view of them; it is found by argument, with no test, and it does not turn on what any physics admits (Part I).

R ranges over every assignment of relations on the footprints; no physical module enters D8.1–D8.2.

> L315 | Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it.

> L315 | No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, and a candidate that nobody has offered is no one's rival.

⟦FROZEN⟧ D8.3
**D8.3 Offer; rivals.** Offered(ℰ, ℰ', p) is a primitive: a record that ℰ was offered for p in place of ℰ' **[I33]**. Off(ℰ, p) is a primitive: ℰ has been offered for p. Riv(ℰ, ℰ'; p) :⟺ Off(ℰ,p) ∧ Off(ℰ',p) ∧ [Offered(ℰ,ℰ',p) ∨ Offered(ℰ',ℰ,p)] ∧ ∃(a,b) ∈ A_D×B_D both translate: Conf(ℰ,ℰ'; a,b). Riv is a two-place relation; nothing here ranges over the rivals of a candidate (S20). [r2: A2; D8.3, I33 amended] [r3: A2; W4: no change; L315's unoffered candidate read with L317: Off(ℰ', p), offered for p; the other reading ∃q Off(ℰ', q) recorded as I175; no claim computes Riv]

> L315 | A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\); outside \(C\) it claims nothing on \(p\)

A candidate offered for p is the claim Acc(ℰ) on p.

> L315 | \(\chi\) need not be an explanation or come with one, and it may be a claim about what is possible or impossible: the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion.

⟦B4⟧ D8.4
**D8.4 A claim at a pair.** A claim χ is given, at each pair, by Allow_χ(a,b), a set of assignments R of relations to the target's components (the behaviours χ allows), and by Applies(χ, a, b) ∈ {yes, no}, the premise that χ speaks of the target under that pair's edit **[I34]**. A claim about what is possible or impossible enters only through Allow_χ: here, and only here in §§1–10, physical possibility is content.

> L315 | A candidate **conflicts with** a claim \(\chi\) at an admitted pair of the target that its transport translates, in \(C\) or outside it, when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there.

⟦FROZEN⟧ D8.5
**D8.5 Conflict with a claim.** With y := Ans_E(τ(a),σ(b)): ConfCl(ℰ, χ; a,b) :⟺ [∃R Ans^R_p(a,b) = y ∧ ∀R (Ans^R_p(a,b) = y ⇒ R ∉ Allow_χ(a,b))] ∨ [∃R Meets_ab(ℰ,R) ∧ ∀R (Meets_ab(ℰ,R) ⇒ R ∉ Allow_χ(a,b))] **[I137]**. [r2: A2; D8.5; FC52; A2-T10]

> L315 | Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation, conflict there given \(\chi\)

⟦B4⟧ D8.6
**D8.6 Conflict given χ; rivals given χ.** ConfG_χ(ℰ, ℰ'; a,b) :⟺ some R has BothMeet_ab(R), and every such R lies outside Allow_χ(a,b) **[I35]**. Riv_χ(ℰ, ℰ'; p) :⟺ one offered in place of the other ∧ ConfG_χ at some pair.

**Vague.** 'One counterpart' is not fixed [I36]. What a claim is, and how it 'excludes', are not given beyond the example [I34]. 'Offered' has no definition and is not a declared input [I33]. [r2: 'one counterpart' fixed by D8.new1; Off added (D8.3)]

## §9 Arguments, usability, ruling out, bearing, reason use

> L397 | **Arguments.** A record leaf is a reference to an event with an interpreted claim. An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions.

⟦FROZEN⟧ D9.1
**D9.1 Claims.** Claims are sentences of a first-order language with ¬ and ∧; Incons(φ, ψ) is classical inconsistency of {φ, ψ} **[I38]**. Forms_cl := the inference forms every instance u of which has Incons(Prem(u) ∪ {¬concl(u)}) [r2b: second check; R15: replaces the gloss 'classically sound' in D9.7, D9.9 (S23)]. The claims used here include 'Acc(ℰ)', 'Ans_p(a,b) = y', records of a test, and conditionals.

⟦FROZEN⟧ D9.2
**D9.2 Argument.** A finite tree α. Each internal node is a step u with an inference form Form(u) and a conclusion concl(u); its children are its premises. Leaves are record leaves (each referring to an event, D11.1, with an interpreted claim) or stated assumptions and definitions. α may be one leaf, a premise alone, with no step; concl(α) := concl(root) where the root is a step, and the leaf's claim where α is a premise alone [owner S41: Q23: reverses I88's 'an argument has a step'; L397 points here (S41-Q23a)]. MadeFrom(leaf, ψ) is a primitive: the record leaf was made from the claim ψ **[I39]**. Below(u) := the steps of the subtree of u other than u. [r2: A3; D9.2, I40]

> L387 | **Usability.** For argument step \(u\) with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:

> L393 | \(\operatorname{Form}_j(u)\): the inference form of \(u\) is one \(j\) admits. \(\operatorname{Scope}_j(u)\): \(u\) is applied within the contract, grain and boundary \(j\) has declared for it; \(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \(j\) holds an explanation of \(d\); a claim \(j\) has never taken up is not live for \(j\).

⟦B4 ⟨Expl Suff Nec⟩⟧ D9.3
**D9.3 Essential premises.** Prem(u) ⊆ children(u): the premises Form(u) uses **[I40]**.

⟦FROZEN⟧ D9.4
**D9.4 Live.** Accepted_j(ξ) is the set of claims j has taken up before ξ and not withdrawn before ξ (a declared input) **[I41]**. Live_j(d; u) :⟺ ∃u' ∈ Below(u) [d = concl(u') ∧ Usable_j(u')] **[I40, fixed]** ∨ d ∈ Accepted_j(ξ). [r2: A3; D9.4, D9.6; A3-L393.1]

⟦B4 ⟨Expl Suff Nec⟩⟧ D9.5
**D9.5 Form and scope.** Form_j(u) :⟺ Form(u) ∈ Forms_j (declared). Scope_j(u) :⟺ C_u ⊆ C_j(u), ℓ_u = ℓ_j(u), β_u = β_j(u), where (C_u, ℓ_u, β_u) is the index u is applied at and (C_j(u), ℓ_j(u), β_j(u)) what j has declared for it **[I42]**.

> L390 | \operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u). \tag{K2}

⟦FROZEN⟧ D9.6
**D9.6 Usability (K2).** Usable_j(u) :⟺ Form_j(u) ∧ Scope_j(u) ∧ ∀d ∈ Prem(u) Live_j(d; u), defined by recursion on the height of u, which D9.4 makes well founded **[I40]**. Usable_j(α) :⟺ every step of α is usable by j, and, where α is a premise alone d, d ∈ Accepted_j(ξ) (Live_j with no step) **[I166]** [owner S41: Q23; L397 points here (S41-Q23b)]. [r3: A3; B-Q23n: L397 now writes Usable_j(α) with the premise-alone clause, ∀u ∈ steps(α) Usable_j(u) ∧ [steps(α) = ∅ ⇒ concl(α) ∈ Accepted_j(ξ)] (R3A3-T1), settling I166 in the text; FC72.new1 (a)]

> L397 | Each step of an argument rules out the case in which the step's premises are met and its conclusion fails, for someone who admits its inference form (\(\operatorname{Form}_j\)), while that form stays admitted. An argument is usable by \(j\) when each of its steps is (K2), and it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below). For \(\psi\), \(X_j(\psi)\) is the set of arguments usable by \(j\) that rule out \(\psi\).

> L397 | An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone; nor does an argument whose record leaf was made from a claim rule out that claim's denial.

⟦FROZEN⟧ D9.7
**D9.7 Rules out.** A step u, for j with Form_j(u), rules out the case Prem(u) ∧ ¬concl(u); forms need not be in Forms_cl **[I38]** [r2b: R15]. RO(α, φ) :⟺ Incons(φ, concl(α)) (D9.2; for a premise alone ψ: Incons(φ, ψ)) [owner S41: Q23]; no leaf of α has ¬φ as a conjunct (flattened, up to renaming and the order of conjuncts) **[I39]**; and no record leaf of α is made from a claim whose denial is φ. [r3: A3; O4, O5 (B-, W-, S-, C-): L397's 'What a stated premise cannot do is stand in for the steps.' and 'in that the argument has steps from it to what it rules out' deleted (R3A3-T2, T3); what tells an argument from the denial is this definition's block (FC72.new1 (b)); O6: no clash (FC72.new1 (c), (d))] [S106: L397's 'read structurally as non-circular dependence reads identity (Part V)' → 'read structurally (D9.7)' (S106-T11): the block's structural reading is this definition's (a conjunct of a leaf, flattened, up to renaming and order, I39), never NC1's; L397's 'that it assumes its own answer, or' deleted (S106-T10): an argument that finds a candidate assumes its own answer no longer rules out that it meets (E); the block on an argument whose premise is the claim's denial is kept: it is about ruling out, not about what makes an explanation] [r4: A3; K1 (addendum): no change; the finding that a candidate assumes its own answer rules nothing out by itself, and taking 'Slot → ¬Acc' as given is the person's choice (L397, S28): computed on the myth about winter (FC72.new2
(cont.) **[I197]**)]

> L315 | A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out, and a candidate is ruled out for \(j\) when the claim that it meets (E) is;

> L315 | A candidate is **not ruled out** for \(j\) when no argument usable by \(j\) rules it out.

⟦FROZEN⟧ D9.8
**D9.8 Ruled out; not ruled out.** X_j(φ) := {α : Usable_j(α) ∧ RO(α, φ)}. Out_j(φ) :⟺ X_j(φ) ≠ ∅; NotOut_j(φ) :⟺ X_j(φ) = ∅. X^ξ_j(φ), Usable^ξ_j: the same with Accepted_j(ξ) (D9.4) at ξ [r2b: second check; R9: L393's pointer names D9.4, D9.8]. A candidate ℰ is ruled out for j :⟺ Out_j('Acc(ℰ)').

> L397 | Where such an argument uses a claim taken as given, the ruling out is a choice the person using it made, not something the claim does by itself (Part 0).

Formally: Out_j depends on Accepted_j and Forms_j, which are declared inputs that no definition sets (FC56). The choice shows as the input; nothing here makes it.

> L395 | **What a test rules out.** For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\) rules out \(T\land B\land I\) together for \(j\), and nothing narrower. (K3)

⟦FROZEN⟧ D9.9
**D9.9 (K3).** **[I43, fixed]** u⁺ := the step with Prem(u⁺) = {concl(α), T∧B∧I ⇒ O} and concl(u⁺) = ¬(T∧B∧I); α⁺ := α under u⁺.
- (i) α ∈ X_j(O) ∧ Usable_j(u⁺) ∧ ∀ leaf l of α [¬(T∧B∧I) ∉ conj(l) ∧ ¬MadeFrom(l, ¬(T∧B∧I))] ⇒ α⁺ ∈ X_j(T∧B∧I), for any Form(u⁺) ∈ Forms_j.
- (ii) ∀x ∈ {T, B, I}: ¬RO(α⁺, x).
- (iii) Forms_j ⊆ Forms_cl ⇒ no α' with leaves ⊆ leaves(α) ∪ {T∧B∧I ⇒ O} has α' ∈ X_j(x) [r2b: R15].
[r2b: second check; R8: L395 now writes (i) with its MadeFrom clause and (ii) in symbols (A3-L395.1 amended); FC71 (i').]
[r2: A3; D9.9, FC71, I43; A3-L395.1]

> L377 | **Bearing.** A criticism has target \(z\), alleged defect \(\delta\), premise \(g\), and a connection. Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments. Then

> L380 | \operatorname{Bearing}(c,z,p)\iff\operatorname{Account}(\mathcal E_c). \tag{K1}

⟦FROZEN⟧ D9.10
**D9.10 Criticism and bearing (K1).** A criticism c = (z, δ, g, Conn, occ): a target, an alleged defect, a premise, a connection (an organization from g to δ) and an occurrence in a history. p_δ := Qf(z, δ, p), the question whether z has δ in respect of p **[I145]**; ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_Conn), with t_c, Γ_c and δ_Conn, the designation of Qf(z,δ,p)'s query in Conn (D5.3, I20), supplied with c **[I147]**; δ alone is the alleged defect (L377). Bearing(c, z, p) :⟺ Acc(ℰ_c). [r2: A3; D9.10, H12, I76 replaced; FC74] [S106: Bearing reads Acc after S106: a criticism whose connection writes its defect in (a slot) has bearing when it meets the rest of (E) (FC107: E8's p_δ, its identity candidate a slot, meets (E) now; round 3's (E) excluded it)] [r4: A3; S-δ (F5): was '(Conn, Qf(z,δ,p), t_c, Γ_c, δ_c), with t_c, Γ_c, δ_c supplied with c': δ_c named ℰ_c's designation with c a criticism, where a subscript elsewhere names the organization (D3.1 δ_D, D5.3 δ_E, D14.7 δ_c with c a content); notation, content unchanged]

> L383 | An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target.

A criticism's premise g is represented (D12.5) by an organization of the system.

> L385 | **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.

⟦B4 ⟨SCdef⟩⟧ D9.11
**D9.11 Reason use** **[I47]**. The represented objection ob is a content with role bindings (a map from role names to its ports); R is the response suborganization; Rec and Chg are declared sets of content-preserving recodings and content changes of ob; Rule: Chg → changes of R is declared. UsesReason(R, ob) :⟺ there is a map m from ob's ports to R's ports preserving role names, with trans(m(ρ·ob)) = trans(m(ob)) for every ρ ∈ Rec, m(γ·ob) = Rule(γ)(m(ob)) for every γ ∈ Chg, and some image port of m on an active route (D11.4). No clause uses Acc or Usable (FC76).

**Vague.** 'Structural map', 'role bindings', 'the same transition' and 'operative deliberative rule' (L385) are defined nowhere [I47]. 'Among its premises … read structurally' is given by pointing at NC1, which is itself not defined [I39, I24]. Whether the step making a premise live lies below the step (L393) is not said; with any step of the argument, (K2) can have two fixed points (FC69) [I40]. [r2: 'below' fixed by Below (D9.2, D9.4)] [S106: L397 now points to D9.7 (S106-T11); nothing in §9 reads NC1]

## §10 Problems and easy to vary

> L317 | **Problems.** Two rivals, neither of them ruled out for an assessor, pose, for that assessor, a **problem for \(p\)**: a conflict between ideas that no argument usable by that assessor has decided.

⟦B4⟧ D10.1
**D10.1 Problem.** Prob_j(ℰ, ℰ'; p) :⟺ Riv(ℰ, ℰ'; p) ∧ NotOut_j('Acc(ℰ)') ∧ NotOut_j('Acc(ℰ')').

> L317 | (i) The rivals conflict at some \((a,b)\in C\).

> L317 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict.

⟦B4⟧ D10.2
**D10.2 The two kinds.** Kind i :⟺ Conf at some (a,b) ∈ C. Kind ii :⟺ Conf at no pair of C, and at some pair outside C that both translate.

> L317 | recording it, the target's relations as well as its answer where their answers there agree, is a **test**.

⟦FROZEN⟧ D10.3
**D10.3 Test.** For Conf at (a,b) ∈ C: Test_ab := Ans_p(a,b), with (R*_j(a,b))_j where Ans_E(τa,σb) = Ans_E'(τ'a,σ'b), with its premises about background and instruments (K3) **[I140]**. Arg_test: 'Test_ab; Acc(ℰ) ⇒ A_ab(ℰ) ∧ Meets_ab(ℰ,R*)' (MP, MT). [r2: A2; D10.3, H20; A2-T11]

> L317 | A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind;

⟦B4⟧ D10.4
**D10.4 Easy to vary.** ETV_j(ℰ; p) :⟺ Prob_j(ℰ, ℰ'; p) of kind ii for some ℰ' **[I37]**. This is the text's 'easy to vary' only; what hard to vary covers is parked (S33–S34), and nothing here extends to it. [r2: A2; pointed to at L317 (A2-T12); I37]

> L315 | for an assessor who tentatively accepts \(\chi\) they pose a problem for \(p\) as rivals do (Problems, below), and for one who does not, they pose none on that account.

⟦B4⟧ D10.5
**D10.5 Problem given χ.** Prob_{χ,j}(ℰ, ℰ'; p) :⟺ Riv_χ(ℰ, ℰ'; p) ∧ χ ∈ Accepted_j(ξ) ∧ neither is ruled out for j.

> L317 | Solving a problem so rules one rival out for that assessor while the argument stays usable for that assessor.

⟦FROZEN⟧ D10.6
**D10.6 Solved.** A problem for j is solved while Out_j('Acc(ℰ)') or Out_j('Acc(ℰ')') holds, Out_j at the assessment's place ξ, time outside the model **[I141]**. Where the argument uses a claim taken as given, that is j's choice (D9.8 and the note after it: Out_j depends on Accepted_j, Forms_j and declared inputs). [r2: A2; D10.6] [r3: A2; W5: no change; FC47.new1 computes solved at ξ, posed again at ξ′ when the premise is withdrawn, solved at ξ″; P7 stays parked] [S106: L317's 'that it assumes its own answer, or' deleted (S106-T8): after S45 that finding rules out no rival's meeting (E); the ground of conflict with a claim (D8.5) is kept]

## §11 Occurrences, events, contents, histories, active routes

> L169 | An **occurrence** is a physically located carrier. A **content** is an organization together with its contract-relative commitments. Occurrences are not identified by carrying the same words; contents are not identified by having the same outputs.

⟦B3 ⟨Expl Suff Nec⟩⟧ D11.1
**D11.1 Occurrence; event.** Occ is a set of physically located carriers, interpreted by Θ. An event is a nonempty set of occurrences of a history **[I45]** (the text uses 'event' at L53, L55, L161, L397, L604 and L612 and defines it nowhere; FC105).

⟦FROZEN⟧ D11.2
**D11.2 Content.** c = (E_c, C_c, Γ_c): an organization, a contract on it, and its commitments **[I48]**. Contents are compared by transports (D13.4), not by outputs. A transport or a contract (D13.6, L590), a finite H ⊆ A × B, and the survival condition surv over 𝒯 (D12.1) are contents by L590's construction (a membership port per pair, a survival port per member of 𝒯, one component fixing them, settings as edits); so Rep(o, x) and Held(o, x) for x ∈ {t, H, surv, cod t} are typed as D12.5 types Rep **[I170]** [r3: A1; B5, S-D2: new sentence; FC97.new1].

> L375 | **Histories.** A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure) and a physical interpretation supplying process occurrences, their ports, and the connections actually instantiated.

⟦FROZEN⟧ D11.3
**D11.3 History.** h = (O_h, ≺_h, I_h): O_h ⊆ Occ; ≺_h well founded: ∀X ⊆ O_h [X ≠ ∅ ⇒ ∃x ∈ X ∀y ∈ X ¬ y ≺_h x], so acyclic with no infinite descending chain **[I169]** [r3: A1; B3, S-fQ2 and A3; S1: was '≺_h acyclic'; R3A3-T5 writes it at L375; FC98.new1, FC98.new2]; ⪯_h := ≺_h* **[I44, fixed by its choice (b)]**; I_h, supplied by Θ, gives process occurrences, their ports and the connections instantiated. Org_ℓ(h) is the organization Θ gives h at grain ℓ; a subhistory is a subset closed under the interpretation, with ≺ restricted **[I151]**. [r2: A3; D11.3, I44, H19; A3-L375.1]

> L375 | An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.

⟦FROZEN⟧ D11.4
**D11.4 Active route.** For a result occurrence r: ActRoute_h(R; i, r, K) :⟺ i, r ∈ R ⊆ O_h ∧ ∀n ∈ R: n ⇝_R r ∧ ∀n ∈ R: n meets Org_ℓ(h)'s relation ∧ ∃(x,x') ∈ K: val_r(Org_ℓ(h)|_R[i:=x]) ≠ val_r(Org_ℓ(h)|_R[i:=x']) ∧ ¬AtRest_h(R, r); Org_ℓ(h)|_R holds every occurrence outside R at its value in h **[I150]**; AtRest_h(R, r) read through Θ's run times, reading (a) all of R∖{r} ends before r starts, or (b) nothing of R runs at r and no product of R is carried to r, open **[I149]**; i's port carries a represented distinction, K the declared contrasts. [r2: A3; D11.4, I46 replaced, H11, I95; FC75]

> L217 | For an edit–boundary pair \((a,b)\in C\) actually occurring:

⟦B3 ⟨Dec Expl Suff Nec SCdef⟩⟧ D11.5
**D11.5 Occurring pairs.** Occurs(a, b, ξ) is a primitive read through Θ: the pair occurs at ξ in the system's history. [r2: A1; registered as I130; H13]

**Vague.** 'Represented input', 'operative result', 'applicable relations' and 'the declared contrasts' (L375) are defined nowhere [I46]; whether a route that ran to completion and whose product persists is 'already at rest when the result occurred' is not fixed (FC75). 'Event' is used and not defined [I45]. 'c's contract' presupposes contents with contracts of their own [I48]. [r2: 'at rest' now a clause of D11.4, its reading open (I149); 'event' is owner question Q7]

## §12 Provenance, representation, prediction

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

> L195 | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

> L195 | A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No member of the history represents \(t\), \(H\), or the survival condition.

⟦FROZEN⟧ D12.1
**D12.1 Selected.** Sel(t; 𝒯, μ, H) :⟺ t ∈ 𝒯; μ: 𝒯 → P(𝒯); H ⊆ C finite and nonempty, its pairs having occurred in h(t) (D11.5) **[I171]** [r3: A1; B8: + 'nonempty' (I52's registered other choice; Q2, L13); FC77, FC30.new1 (e)]; surv(t, H) :⟺ Faithful_H(t) (D5.7) ∧ Env_{h(t)}(value_t|_H), Env_{h(t)} the further requirement on t's values at the pairs of H that the environment enacts in h(t) (L481), read through Θ, none given: Env ≡ ⊤ **[I177]** [r3: A3; W6: was 'Faithful_H(t) (D5.7)' alone; FC80.new1]; t survives on H :⟺ t ∈ 𝒯 ∧ surv(t, H); 𝒯 = D15.8's population (L481); and ¬∃o ≺_{h(t)} o_t, x ∈ {t, H, surv, cod t}: Rep(o, x) (D12.5; x typed by D11.2), where Sel, Con and Dec are of a holding (t, o_t), o_t an occurrence at which t is held, and h(t) := h(t, o_t) is the history that produced that holding, its preparing episode included **[I52, I53, I128, I162, I167]** [r3: A1; B1: was 'o_t the occurrence at which t is held, h(t) the one history of t'; FC12.new2]; and ¬∃h' ⊆ h(t): CT(h', t) (D12.2) **[I161]**. [r2: A1 (D12.1', H05, I52, I53, FC78; T9) + A3 (H09: '𝒯 =', was 'members of 𝒯 admitted')] [r2b: second check; R1: + ¬CT (I161), so Sel ∧ Con is excluded by definition under every cut (FC12.new1, FC83, Rep computed); R3: the exclusion is staged at o ≺ o_t, the cut T′ (D18.1, I162); T9 writes it at L195 (R2)]

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target. Write \(\operatorname{Con}(t;h,e)\).

⟦FROZEN⟧ D12.2
**D12.2 Constructed.** CT(h', t) :⟺ t is held at an output o of a construction trace of h' (D13.3: Prepares(h', o, ·)); a transport assembled later from a trace's outputs is not thereby prepared by it **[I168]** [r3: A1; B2: was 'h' has a construction trace (D13.3) that prepares t'; FC12.new3]. Con(t; h, e) :⟺ some episode h' of h up to e (D13.8; it need hold no change of contract [owner S41: Q6]) has CT(h', t), and Held(o', x) for some o' ⪯ o_t of h' and x ∈ {t, cod t} (D18.1) **[I162]**. [r2: A3] [r2b: second check; R3: 'available as a represented target' read as Held, the cut T′ (Q1 ruled)] [r3: A1; K2: L201's 'a selected transport has no represented target and no criticism in its history; a constructed one has both.' replaced by '(D12.1, D12.2).' (R3A1-T6); Con with no criticism: FC84.new1 (a), N2] [r3b: second check; objection 2: L13's ' and criticism' deleted (R3SC-L13): Con, CT and Episode reach no Crit (D9.10) under U, K, T, T′, (EX) does through CCE (FC32.new1 (f))] [S47: the maths asks for no criticism event: Con, CT and Episode read no Crit (FC32.new1 (f)), and nothing here asks anything of the agent; the agent asks, when a question occurs to it as worth investigating, and a criticism (D9.10), when there is one, is that occurrence in the history. L13's 'an episode of conjecture and criticism' names the episode Con asks for (D13.8), which includes one in which no question occurred to the agent as worth investigating **[I190]**; ' and criticism' is back in L13
(cont.) (S47-T1, reverting R3SC-L13). The r3 mark's 'Con with no criticism: FC84.new1 (a), N2' made a stronger claim than the owner's (S47) and is withdrawn: the bridge is an episode in which no question about the brief occurred to the agent (one contract throughout, no criticism aimed at it, **[I191]**), and Con holds with no criticism in the history (FC84.new1 (a1)) and with a criticism of an earlier design in it (FC84.new1 (a2)). R3A1-T6's pointer at L201 is kept: it claims nothing about criticism; the words it replaced claimed a criticism in every constructed history and none in a selected one, which neither D12.2 nor D12.1 carries (R1 below; S47)] [r4: A1; N6 (B11, W-N6, S-N6, C-N6): I191's reading of 'no question about the brief occurred to the agent' is recorded, not chosen anew, beside two others **[I192]**: (d) a question-occurrence its own Θ label, with or without an alleged defect; (e) a question found (L15, L155, L161), operative at its occurrence; they part ways on B11's cases as labelled (Θ by hand, I90) and agree on (a1)'s chain; Con and Build at the output are the same under all three (FC84.new1 (a3))] [r4b: second check; O1: ': no computed value reads the labels (S47)' deleted: (EX) reads the criticism label through CompleteCritical, and Episode of a whole chain reads q(o), which (e) sets (FC84.new1 (a4)); O4: 'as labelled (Θ by hand, I90)']

> L199 | **Declared.** Neither of the above. The transport is entered into the model by its author. Write \(\operatorname{Dec}(t)\).

⟦FROZEN⟧ D12.3
**D12.3 Declared.** A holding (t, o') reached from a holding (t, o) by a composition of content-preserving transfers (relay, record; TransferComposite, D13.3) has prov(t, o') := prov(t, o), part by part (D12.4); for every other holding, Dec(t, o_t) :⟺ no parameters give Sel(t; ·) and none give Con(t; ·), both read on h(t, o_t) (D12.1) **[I53, I128, I167]** [r3: A1; B-e6, B1: was 'Dec(t) :⟺ no parameters give Sel(t; ·) and none give Con(t; ·). Sel and Con are read on t's one history h(t) (D12.1)'; L211; FC12.new2 (d)]; Dec(t) abbreviates Dec(t, o_t) where one holding is meant; Sel and Con exclude each other by D12.1's ¬CT (I161). [r2: A1; D12.3 via D12.1'; L199's second sentence deleted (T10)] [r2b: R1]

> L211 | A carrier keeps its provenance when present access to it is lost, and a later record made from the carrier carries that provenance, not a second, independent one.

> L405 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.

⟦B3 ⟨Dec Expl Suff Nec⟩⟧ D12.4
**D12.4 Provenance per part; inherited provenance.** prov assigns Sel, Con or Dec to each part of a transport (each component with its counterpart binding). A content-preserving transfer (relay or record) from carrier o to o' gives each part at o' the value it had at o; a binding newly built gets Con. 'Inherited' is this rule, not a fourth value **[I54]**.

> L205 | An occurrence \(o\) **represents** content \(c\) at grain \(\ell\) when there is a transport from the organization that \(o\) instantiates under the physical module, at grain \(\ell\), to \(c\), faithful on \(c\)'s contract, whose provenance is selected or constructed;

> L208 | \operatorname{Rep}_\ell(o,c)\iff\exists t\,[\operatorname{Faithful}_C(t:\operatorname{Org}_\ell(o)\to c)\land(\operatorname{Sel}(t)\lor\operatorname{Con}(t))]. \tag{R}

⟦B3 ⟨Dec Expl Suff Nec⟩⟧ D12.5
**D12.5 Representation (R).** Rep_ℓ(o, c) :⟺ there is t: Org_ℓ(o) → E_c, faithful (D5.7) on the preimage {(a,b) : (τ(a),σ(b)) ∈ C_c} with Γ_c as its active components **[I48]**, and some parameters give Sel(t; ·) or Con(t; ·). Org_ℓ is the one thing (R) takes from Θ (L213).

> L175 | The **object layer** \(P\) is an organization whose ports are persistent things with boundaries and identity, whose components are their continuity relations, and whose admitted edits include displacement, occlusion and re-identification.

> L177 | The **simulation layer** \(S\) is an organization over \(P\) whose components are dependencies among things and whose queries are predictions: what a port of \(P\) will take under an admitted edit.

⟦B3⟧ D12.6
**D12.6 Layers.** P and S are organizations typed as L175 and L177 say; nothing assumes either exists in a given system (L179).

> L219 | - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);

> L220 | - a **violation** occurs when fidelity fails at \((a,b)\);

> L221 | - **surprise** is a violation of a selected transport at \((a,b)\notin H\).

⟦FROZEN⟧ D12.7
**D12.7 Prediction, violation, surprise.** For t from P to S with contract C and, if selected, history H, at (a,b) ∈ C with Occurs(a,b,ξ): Pred_t(a,b) := Ans_S(τ(a),σ(b)); Viol(t; a,b) :⟺ ¬(F1 at (a,b) ∧ F2eq at (a,b)), and Viol⁺ adds (A) at (a,b) **[I50]**; Surp(t; a,b) :⟺ Sel(t; 𝒯_t, μ_t, H_t) ∧ (a,b) ∉ H_t ∧ Viol(t; a,b), (𝒯_t, μ_t, H_t) of the holding's history h(t, o_t) (L193, L217) [r3: A1; B1, re-based: was 'of t's one history']; so Sel ∧ Viol(a,b) ⇒ (a,b) ∉ H_t [r2: A1; D12.7, H07; L584 writes it (A3-L584.1)] [r2b: R6: L584 with 𝒯_t, μ_t, H_t]. Pred is extended to any transport, Pred_t(a,b) := Ans_E(τ(a),σ(b)), where a line uses it so (L151) **[I51]**.

> L225 | A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace.

⟦FROZEN⟧ D12.8
**D12.8 Responses.** SelResp(t → t'; a,b) :⟺ Sel(t; 𝒯, μ, H) ∧ Viol(t; a,b) ∧ t' ∈ μ⁺(t) ∧ Sel(t'; 𝒯, μ, H ∪ {(a,b)}) **[I129]**. ConResp(→ t''; a,b) :⟺ Viol(t; a,b) ∧ t'' or its codomain is new (D13.5) ∧ Con(t''; h, e). [r2: A1; D12.8, H08; FC82, FC83'] [r3: A1; B1, re-based: Sel of a holding, on h(t, o_t)]

> L572 | For every \((a,b)\in C\setminus H\) at which some \(t'\in\mathcal T\), also surviving on \(H\), has a different value from \(t\), the value of \(t\) at \((a,b)\) is underdetermined by \(H\)

⟦FROZEN⟧ D12.9
**D12.9 Value at a pair; underdetermination.** value_t(a,b) := (τ(a), σ(b), (L^E_k(τ(a),σ(b)))_{k∈J_E}); members of 𝒯 share the codomain's ports and components **[I71]**. Underdet(t; a,b; 𝒯, H) :⟺ some t' ∈ 𝒯 surviving on H (t' ∈ 𝒯 ∧ surv(t', H), D12.1) has value_t'(a,b) ≠ value_t(a,b) (FC80) [r3: A3; W6, re-based: 'surviving on H' := surv; L574's step holds for any condition on values at H, FC80.new1 (b)].

**Vague.** 'No member of the history represents' (L195) is said of a set of pairs, which cannot represent; the reading as occurrences of a physical history is invented, and without it Sel is met by every transport (FC77) [I52]. 'Exactly one of three' needs Sel and Con read on one history [I53]. 'Inherited provenance' (L405, L409) is used and not defined [I54]. [r2: 'member of the history' read as occurrences of h(t) (D12.1; T9)] [r2b: second check; R1: L201's 'no criticism in its history' and 'a constructed one has both' are carried by neither D12.1 nor D12.2 (D12.2 asks no criticism); I161, not 'no criticism', gives L193's 'exactly one'.] [S47: kept: 'D12.2 asks no criticism' is the maths asking for nothing (S47), not a claim that a constructed history holds none]

## §13 Deploy, Build, New, Origin, ownership, episodes

> L403 | \(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi;U)\) is met when \(s\) at \(\xi\) holds a representation of \(c\), by (R) a faithful transport with selected or constructed provenance, integrated into problem-directed activity and serving the declared use task \(U\) as a retained capability (Part XII). The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect.

⟦B3⟧ D13.1
**D13.1 Deploy.** Deploy_{β,ℓ}(s, c, ξ; U) :⟺ some occurrence o of s at ξ has Rep_ℓ(o, c), Integrated(o, s, ξ), and Can_{Ω,β}(ξ, U; χ) holds for some χ with a realization that uses o **[I55]**.

⟦B3⟧ D13.2
**D13.2 Repertoire.** R_{β,ℓ}(s, ξ) := {c : Deploy_{β,ℓ}(s, c, ξ; U) for some U with Nontrivial(U)} **[I55]**; R_{<e}(s,h) := ∪_{ξ before e} R_{β,ℓ}(s, ξ) (L415).

> L405 | **Construction.** \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.

⟦FROZEN⟧ D13.3
**D13.3 Build; construction trace.** Build_{β,ℓ}(s, c, h, e) :⟺ ∃h' ⊆ h ending at e [Owned_β(h', s) ∧ ∃o output of h' [Prepares(h', o, c) ∧ Held_ℓ(o, c) ∧ ExplUse(o, c)] ∧ BindingConstruction(h', c) ∧ ¬TransferComposite(h')] (D18.1) **[I56, I162, I178]**; ExplUse(o, c) :⟺ UsesClaim(o, 'Acc(ℰ)') for some ℰ = (E, p, t, Γ, δ_E) with c ∈ {E, t, C_p} (L425), UsesClaim read through Θ, the claim need not hold [r3: A3; S2(iii): was ExplUse a primitive (I148), so Build did not reach (E) (L526); FC32.new1 (d), FC90.new1]. [r3: A3; W7, S-e-represented: L405's 'a represented organization' replaced by 'Held_ℓ(o,c) (D13.3, D18.1)' (R3A3-T4), settling I162 for Build in the text] [r2: A3; D13.3] [r2b: second check; R3: 'represented organization' read as Held, the cut T′ (was Rep^ρ, ρ open, Q1)] A construction trace is (h', the controlled processes, the incoming carriers, the bindings constructed, the resulting representation) (L405). A binding may be identified by its use: by responses meeting D9.11's clauses (L409).

> L413 | **Newness.** Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\).

⟦B3⟧ D13.4
**D13.4 Matching.** d ≡_ℓ c :⟺ there are t: E_d → E_c faithful on the preimage of C_c, and t': E_c → E_d faithful on C_c, at grain ℓ **[I48]**. It is read with c fixed (L413) and is not claimed symmetric (FC85).

> L416 | \operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c. \tag{N}

⟦B3⟧ D13.5
**D13.5 New (N).** New(s, c, h, e) :⟺ no d ∈ R_{<e}(s, h) has d ≡_ℓ c.

> L422 | \operatorname{Origin}_{\beta,\ell}(s,c,p,h,e)\iff\operatorname{Attempt}(s,c,p,h,e)\land\operatorname{New}(s,c,h,e)\land\operatorname{Build}_{\beta,\ell}(s,c,h,e). \tag{G}

⟦B3⟧ D13.6
**D13.6 Attempt; Origin (G).** Attempt(s, c, p, h, e): c is used in h, up to e, to address p (L419; a claim read through Θ). Origin :⟺ Attempt ∧ New ∧ Build. c may be an organization, a transport or a contract (L425; E8).

> L427 | **Ownership.** The subhistory in Build is owned by \(s\) when its processes run inside the system boundary and resource contract declared for \(s\) (Part XII).

⟦FROZEN⟧ D13.7
**D13.7 Ownership.** Owned_β(h', s) :⟺ every process of h' runs inside the boundary β and resource contract declared for s. Contribution of content is a separate attribution (L427); Owned_β reads no authorship. [r2: A3; Contrib dropped, no definition used it; H14]

> L429 | **Episodes.** A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response. A **recognized difficulty** is a failure of a claimed aim, or a conflict in which what the system holds meets a claimed aim only by failing a protected one (Part XI), when the system represents it. A creative critical episode contains an instance of (G) connected to its inquiry.

⟦FROZEN⟧ D13.8
**D13.8 Episodes.** An episode is a subhistory in which every change of contract carries a provenance record, and which need hold no change of contract [owner S41: Q6; I131 settled: L55's 'in which contracts change' dropped (S41-Q6)]: Episode(h') :⟺ h' ⊆ h is a subhistory ∧ for every o ≺_h' o', o' immediately after o in h', with q(o) ≠ q(o'): Rec_h'(ρ_{q(o')}); o' immediately after o in h' :⟺ o ≺⁺_{h'} o' ∧ ¬∃o'' ∈ h' (o ≺⁺_{h'} o'' ≺⁺_{h'} o'), ≺⁺_{h'} the transitive closure of ≺_h on h' **[I173]** [r3: A1; B9, S-fQ6: was undefined; FC84.new2]; a record is keyed by the new contract here and by the change in the program (claims_b.episode), which differ only where one contract is entered twice with one record **[I174]** (recorded, not chosen); q(o) = (C, Q) is the contract operative at o, read through Θ, and Rec_h'(ρ) is a record in h' of ρ with its trace (D3.4) **[I165]**; Chg(h') := {(o, o') : q(o) ≠ q(o')} = ∅ is allowed. CompleteCritical(h') :⟺ Episode(h') ∧ h' contains a recognized difficulty (a represented failure of a claimed aim, or a represented conflict in which meeting a claimed aim fails a protected one), a target represented before its criticism, a criticism (D9.10) of it, and a response that uses the criticism as a reason (D9.11). CreativeCriticalEpisode(s, Δ, h, e) :⟺ ∃h' ⊆ h up to e [CompleteCritical(h') ∧ h_Δ ⊆ h' ∧ ∃c, p, e' (Origin(s, c, p, h, e') ∧ its Build subhistory ⊆ h' ∧ Conn(G, h'))]; Conn(G, h') :⟺ the (G) instance's Attempt addresses the question
(cont.) h''s recognized difficulty poses **[I152]**. [r2: A3; D13.8, H15, D14.7] [S47: an episode need hold no criticism occurrence as it need hold no change of contract (S41 Q6): an episode of conjecture and criticism (L13) includes one in which no question occurred to the agent as worth investigating (I190); CompleteCritical and CreativeCriticalEpisode, (EX)'s, hold a criticism (D9.10) because the agent asked, not because Con does] [r4: A1; N6; integration, pair 13: the note kept as written; 'because the agent asked' is I190's reading; I192 records (d), under which a criticism can be used with no question occurring (a claim taken as given, S27), and (e); Con and Build do not turn on it (FC84.new1 (a3)); (EX) does, through CompleteCritical's criticism (FC84.new1 (a4)), and the text types a criticism by its alleged defect (L377; D9.10) and a complete critical episode by 'a conjectural objection' (L429); A3's B12 not taken: (EX) needs a critical episode (L429, L447–L449), computed as FC32.new1 (f)] [r4b: second check; O1: was ''because the agent asked' is I191's reading' and 'no value of (EX), Con or Build turns on it (FC84.new1 (a3))']

**Vague.** 'Integrated into problem-directed activity', 'nontrivial use respect' (L403), 'prepares', 'nontrivial binding construction', 'content-preserving transfers' (L405) and 'connected to its inquiry' (L429) are defined nowhere [I55, I56]. [r2: D13.3 keeps 'represented' and 'for explanatory use' (I148); 'connected' is I152] 'Faithful on c's contract' for a transport into c needs c's contract on c's own organization [I48].

## §14 Repair, created explanation, appraisal

> L435 | **Repair.** The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes.

> L441 | The aims are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers. In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).

⟦FROZEN⟧ D14.1
**D14.1 Aims.** An aim is (cond, Occ) with Occ a set of times (declared). For o ∈ O: o(ξ) :⟺ cond met at ξ. For r ∈ P, on the left of (P): r(ξ) :⟺ cond met at ξ if ξ ∈ Occ_r, and holds otherwise; on the right: r(ξ') :⟺ cond met at every ω ∈ Occ_r with ξ ≤ ω ≤ ξ' **[I57]**. Lost_{ξ,ξ'}(r) :⟺ r(ξ) ∧ ¬r(ξ'); so (P)'s second conjunct ⟺ ¬∃r ∈ P Lost_{ξ,ξ'}(r) (FC86). [r2: A3; D14.1; A3-L441.1]

> L438 | \operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\iff\exists o\in O[\neg o(\xi)\land o(\xi')]\land\forall r\in P[r(\xi)\Rightarrow r(\xi')]\land\operatorname{ProducedBy}(\Delta,\xi,\xi';O). \tag{P}

⟦B3 ⟨SCdef⟩⟧ D14.2
**D14.2 Repair (P).** Repair_{O,P}(ξ, ξ'; Δ) :⟺ ∃o ∈ O [¬o(ξ) ∧ o(ξ')] ∧ ∀r ∈ P [r(ξ) ⇒ r(ξ')] ∧ ProducedBy(Δ, ξ, ξ'; O). Δ = (h_Δ, the content changes it makes).

> L441 | \(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair; it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran, the repair is attributed to both and the history supplies no division of the attribution that it does not contain.

⟦B3⟧ D14.3
**D14.3 ProducedBy.** ProducedBy(Δ, ξ, ξ'; O) :⟺ some o ∈ O with ¬o(ξ) ∧ o(ξ') has an active route (D11.4) from an occurrence of h_Δ to the occurrence at which o's condition comes to be met **[I57]**. Attr(o) := {Δ_i : ProducedBy(Δ_i, …) for o}; no share function is defined (a weighting is a declared input, L522).

> L441 | Losses outside \(P\) must be exposed.

⟦B3 ⟨SCdef⟩⟧ D14.4
**D14.4 Losses outside P.** A repair claim carries Aims* ⊇ O ∪ P and an exposure record X; WellFormed :⟺ {r ∈ Aims* ∖ P : r(ξ) ∧ ¬r(ξ')} ⊆ X **[I58]**.

> L443 | **Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,

⟦B3⟧ D14.5
**D14.5 Explanatory aims.** O_ex ⊆ O, a declared marking; o ∈ O_ex when o's condition is that s possesses a deployable account of a stated question, or is L443's 'the correction of a use through' a deployable account **[I59]**.

> L453 | \(\operatorname{Result}(\Delta)\) is the set of contents at \(\xi'\) that \(\Delta\) prepared. \(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\).

⟦B3⟧ D14.6
**D14.6 Result; ProducesVia.** Result(Δ) := the contents at ξ' that h_Δ prepared (Prepares, D13.3). ProducesVia(Δ, c, o; ξ, ξ') :⟺ some active route from an occurrence of h_Δ to the occurrence at which o comes to be met contains an occurrence instantiating the binding named in c's construction trace **[I60]**. [r2: A3; pointed to at L453 (A3-L453.1); I60]

> L447 | \operatorname{CreateEx}(s,\Delta,h,e)\iff{}&\operatorname{CreativeCriticalEpisode}(s,\Delta,h,e)\land\exists\xi,\xi'\,\bigl[\operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\\

> L448 | &\land\exists o\in O_{\mathrm{ex}}\,\exists c,p_c,e_c,t_c,\Gamma_c\,[e_c\preceq_h e\land\neg o(\xi)\land o(\xi')\land\operatorname{Origin}_{\beta,\ell}(s,c,p_c,h,e_c)\\

> L449 | &\quad\land\operatorname{Account}\big((c,p_c,t_c,\Gamma_c)\big)\land c\in\operatorname{Result}(\Delta)\land\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)\land\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')]\bigr].

⟦FROZEN⟧ D14.7
**D14.7 Created explanation (EX).** As displayed, with e_c ⪯_h e read in the partial order of D11.3 **[I44]**, and with Account((c, p_c, t_c, Γ_c)) evaluated on the contract of p_c fixed at e_c (L453): CreateEx(s, Δ, h, e) :⟺ CreativeCriticalEpisode(s, Δ, h, e) ∧ ∃ξ, ξ' [Repair_{O,P}(ξ, ξ'; Δ) ∧ ∃o ∈ O_ex ∃c, p_c, e_c, t_c, Γ_c, δ_c (e_c ⪯_h e ∧ ¬o(ξ) ∧ o(ξ') ∧ Origin(s, c, p_c, h, e_c) ∧ Acc((c, p_c, t_c, Γ_c, δ_c)) ∧ c ∈ Result(Δ) ∧ Deploy(s, c, ξ'; U_c) ∧ ProducesVia(Δ, c, o; ξ, ξ'))]. [r2: A3; s and Δ enter through D13.8; FC90, A3-L628.1–2] [r3: A3; S-e-Acc: δ_c, the designation of Q in c (D5.3, I20), is quantified with c, p_c, t_c, Γ_c **[I180]**; was 'Acc(c, p_c, t_c, Γ_c)', four data; FC90.new1 (c): the pole's forward candidate meets (E) with δ = L, not with δ = H; L449 unchanged]

> L455 | achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) (AR); and \(\mathcal N\subseteq \mathit{Act}\times\mathit{Occ}\times\mathsf{Rsn}\times\mathcal V_A\) taken as a substantive input when aesthetic value is claimed

⟦B3⟧ D14.8
**D14.8 Appraisal, typed only.** 𝓡 ⊆ Act × Occ × Eff, G ⊆ Occ × Eff, (AR): 𝓡[a,k] ≠ ∅ ∧ 𝓡[a,k] ⊆ G[k]; 𝒩 ⊆ Act × Occ × Rsn × V_A, an input with Rsn and V_A unspecified. No definition of this file uses 𝒩; where values are placed is the owner's question.

**Vague.** Which aim ProducedBy's route runs to is not tied to (P)'s first conjunct [I57]. The universe of 'losses outside P' is not given [I58]. L443 names two kinds of explanatory aim; (EX) treats them alike and the second is carried only by ProducesVia (FC89) [I59]. 'The relevant binding' (L453) [I60]. [r2: pointed to D14.6]

## §15 The physical module

> L461 | **Tasks.** A substrate is a physical system; an attribute a set of its states; a task a specified input-to-output attribute transformation with explicit resources and side effects. Possibility is the absence of a law-imposed limit, short of exact, on the tolerance to which a task can be performed and retained; it is not one trajectory that performed the task.

⟦FROZEN⟧ D15.1
**D15.1 Tasks.** A substrate has a state space Z_s; an attribute is a subset of Z_s; a task is T := (T_rel, Res_T, Side_T), T_rel a relation between input and output attributes with dom T and T[i], Res_T and Side_T its stated resources and side effects; T = T' ⟺ all three equal **[I61]**. [r2: A3; D15.1] Here physical possibility enters as the carrying out of a transformation.

> L466 | \operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C. \tag{CT1}

> L469 | Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task.

⟦FROZEN⟧ D15.2
**D15.2 Retained realization (CT1).** Exec(π, z, i; χ) is a set of executions, each with a completion flag, an output o and a final constructor state z'. RetReal(π, T, C; χ) :⟺ for every z ∈ C, i ∈ dom T and η ∈ Exec(π, z, i; χ): η completes with o ∈ T[i] and z' ∈ C. Standing assumption: Exec(π, z, i; χ) ≠ ∅ for every z ∈ Z and i ∈ dom T (L469) **[I61, fixed]**. RetReal^{q,r}(π, T, C; χ) :⟺ for every z ∈ C, i ∈ dom T and η ∈ Exec(π, z, i; χ): η completes with o ∈ T^q[i] and z' ∈ C^r (per execution) **[I153, fixed]** [r2b: second check; Q5 ruled: (CT1)'s ∀η (L466) and L479's 'a tolerance of performance'; the other side, a bound on failing executions over the family, needs a measure on executions no line gives]. [r2: A3; D15.2, FC92, E17] (Here C is a constructor attribute and π a protocol: the letters of Part XII are local.)

> L471 | **Retention fixed point.** \(F(C)\) = states whose executions all complete and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

⟦B3⟧ D15.3
**D15.3 Retention operator; (CT2).** F(X) := {z ∈ Z : for every i ∈ dom T and every η ∈ Exec(π, z, i; χ), η completes with o ∈ T[i] and z' ∈ X}, with 'complete' read as (CT1)'s completion **[I61]**. [r2: A3; L471 in symbols (A3-L471.1)] (CT2): F is monotone on P(Z); RetReal(π, T, C; χ) ⟺ C ⊆ F(C); gfp(F) = ∪{D ⊆ Z : D ⊆ F(D)}, with D a bound letter (FC91, FC92).

> L473 | **System boundary and continuity.** A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change).

⟦B3⟧ D15.4
**D15.4 Boundary and continuity.** β: the processes and resources that are the system's (declared); Ω: a relation on system states saying which are the same system (declared). Both are fixed before the attribution (L473).

> L475 | **Owned capability.** \(\operatorname{Can}_{\Omega,\beta}(\xi,T;\chi)\) requires an owned retained realization or an owned, physically admitted, finite construction of one under the same continuity and resource contract.

⟦FROZEN⟧ D15.5
**D15.5 Owned capability.** Owned_β(π, C, s) :⟺ every execution of π from z ∈ C is a subhistory owned by s (D13.7) **[I156]**. Can_{Ω,β}(ξ, T; χ) :⟺ there is a protocol π and constructor attribute C with Owned_β(π, C, s) at ξ and RetReal(π, T, C; χ); or an owned, physically admitted, finite construction of such, under Ω and the same resource contract (⟺: the line is its definition) **[I157]**. [r2: A3; D15.5, H20]

> L477 | **Achievement.** \(\operatorname{CanAdv}(\xi,p;\chi,J_p,C_I)\): for each starting configuration in the independently specified \(J_p\), every maximal execution completes with a history meeting the achievement predicate and a continuing organization in \(C_I\).

⟦B3⟧ D15.6
**D15.6 Advancing capability (CA).** CanAdv(ξ, p; χ, J_p, C_I) :⟺ for every z ∈ J_p, every maximal execution from z completes with a history meeting the achievement predicate for p and ends with an organization in C_I.

> L479 | **Tolerances.** The tolerances of the physical module (Part XIV) form a directed preorder \(Q_\Theta\), in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes, and none of them is exact;

⟦B3⟧ D15.7
**D15.7 Tolerances; Admit, Cap, Poss.** (Q_Θ, ≤) a directed preorder, q ≤ q' when q' excludes at least what q excludes; no member exact. Admit^{q,r} := the tasks with a realization (owned or not) at performance tolerance q and retention tolerance r, antitone in (q, r) **[I62]**; Cap^{q,r}_Ω(ξ) := the tasks with an owned realization, or an owned construction of one, at (q, r); Poss_Θ := ∩_{q,r} Admit^{q,r}; Cap^∞ := ∩_{q,r} Cap^{q,r}. (CT3): Cap^{q,r} ⊆ Admit^{q,r}; (CT4): Cap^∞ ⊆ Poss_Θ (FC93).

> L481 | The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it.

⟦FROZEN⟧ D15.8
**D15.8 Selection's population.** 𝒯 := {t : Θ admits t ∧ parts(t) ⊆ the parts of the stated construction}; μ is physically admitted; the survival condition, surv (D12.1), is enacted by the environment (L481): its part Env **[I177]** [r3: A3; W6, re-based]. This is where D12.1's witness is read. [r2: A3; parts(t) ⊆ the stated construction's parts registered as I158; D12.1 now writes 𝒯 = this population (H09)]

## §16 Recursion, universality, classes

> L487 | **Scrutinizability.** An aspect \(d\) of a system's practice is scrutinizable at \(\xi\) when there is an owned, admitted continuation in which a description of \(d\) becomes a represented target, criticism can be directed at it, and the result can affect its operative use.

⟦B4⟧ D16.1
**D16.1 Scrutinizable.** Scr(d, ξ) :⟺ some owned, physically admitted continuation from ξ has a description of d as a represented target, a criticism (D9.10) of it, and a result on an active route to d's operative use. [r2: A3; registered as I159 (H16); Q22]

> L492 | \forall n<\omega\ \forall\text{ admitted target chains of length }n,\ \exists\text{ an owned enabling continuation}. \tag{RC}

⟦B4⟧ D16.2
**D16.2 Recursive capacity (RC).** RC :⟺ for every n < ω and every admitted target chain d1, …, dn (each d(i+1) a description of di made a represented target), there is an owned continuation meeting Scr(dn) **[I74]**.

> L495 | \(\operatorname{Enable}(s,T,\chi)\) is met when \(\chi\) is an admitted, non-question-begging enabling condition for \(s\) and the task \(T\), in the sense of (CT1).

⟦FROZEN⟧ D16.3
**D16.3 Enable.** NQB(χ, s, U_c) :⟺ no realization witnessing Can(ξ0, U_c; χ) uses an occurrence o with Rep_ℓ(o, c) whose provenance was relayed from outside β **[I154]**. Enable(s, T, χ) :⟺ Θ admits χ ∧ NQB ∧ χ an enabling condition in (CT1)'s sense. [r2: A3; D16.3, NF11, E17]

> L500 | \operatorname{UU}\iff\forall c\in\mathfrak E_\Theta\ \exists\chi,\ \operatorname{Enable}(s,U_c,\chi)\land\operatorname{Can}(\xi_0,U_c;\chi), \tag{U1}

> L503 | \operatorname{UC}\iff\forall p\in\mathfrak P^{\mathrm{adv}}_\Theta\ \exists\chi,\ \operatorname{Enable}(s,A_p,\chi)\land\operatorname{CanAdv}(\xi_0,p;\chi,J_p,C_I), \tag{U2}

> L506 | \mathsf{UECS}=\{(M,s,\xi_0,\Omega,\beta):M\models\operatorname{RC}\land\operatorname{UU}\land\operatorname{UC}\}. \tag{U3}

⟦FROZEN⟧ D16.4
**D16.4 Universality.** 𝔈_Θ := {c : Acc((c, p, t, Γ, δ)) for some p, t, Γ, δ, δ the designation of Q in c (D5.3, I20), and Θ admits a carrier instantiating c} **[I75, I183]** [r3b: second check; objection 1: was 'Acc(c, p, t, Γ) for some p, t, Γ', four data, as D14.7 before A3 F4; Acc is not a function of the four (FC90.new1 (c): the pole's forward candidate meets (E) with δ = L, not with δ = H; nor with δ = T, the second check's run); F4's change (I180) in its second place, not counted apart]; 𝔓^adv_Θ is not defined beyond its name (NF12); it is read through Θ, and (U2), (U3) are stated given it [r2b: second check; Q8 ruled; the other side, a definition, needs content no line gives]. UU, UC, UECS as displayed.

> L528 | **Membership.** The base class: interpretations supplying these data with typing as declared, meeting physical realization wherever a physical attribution is made. The creative-episode class: base interpretations with an instance of (G) connected to a critical episode. The explanation-creation class: an instance of (EX). The recursive class: (RC). The universal class: (U3).

⟦FROZEN⟧ D16.5
**D16.5 Classes.** Base := the interpretations M of the data of §§1–15 with the typing above and Θ-realization of every physical attribution; CreativeEp := {M ∈ Base : M has a (G) instance with Conn(G, h') for a critical episode h'} **[I152]**; ExplCreation := {M : M ⊨ CreateEx for some s, Δ, h, e}; Recursive := {M : M ⊨ RC}; Universal := {M : ∃s, ξ0, Ω, β (M, s, ξ0, Ω, β) ∈ UECS} **[I164]** [r2b: R16; A3-L528.1 settles I164]. Each is the extension of a formula; no axiom here puts any system in any class (FC110). [r2: A3; D16.4, D16.5; A3-L528.1]

⟦FROZEN⟧ D16.XV
**D16.XV Part XV, the defeat conditions (formal shapes).** Expl(ℰ): an atom, no definition uses it; Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) [owner S41: Q2]: a candidate meeting (E) whose transport is declared is no explanation. (E) still takes no provenance (FC30); ¬Dec(t) stands beside it (FC30.new1). Uses(α): the symbols of α's leaves and forms; 'an argument not using (E)' := (E), Acc ∉ Uses(α). [r3: A1; O1–O3 (B-, W-, S-, C-): L61's (Suff), L49 and L69 now write Account(ℰ) ∧ ¬Dec(t) with a pointer here (R3A1-T1–T4); L69's 'an account, ' deleted (R3A1-T3), so 'account' keeps its one sense, Acc; with I171 the student's declared copy is Dec (FC30.new1 (d)) and a link no pair tried is not Sel (FC30.new1 (e))] [r3b: second check; objection 3: L61's '(Nec) their necessity' → '(Nec) necessity (D16.XV)' (R3SC-L61): after R3A1-T1 'their' had Account(ℰ) ∧ ¬Dec(t) as antecedent, while (Nec) below names no Dec; the student's declared copy is in the defeat set of the first and not of L538's (FC30.new1 (g))] [S106: L536's '; conclusion-as-premise fails non-circular dependence' deleted (S106-T13); the defeat sets' shapes are unchanged; Acc now admits candidates with a slot, so (Suff)'s range holds them, and S44, S45 hold them explanations, bad ones; S41 (Q2) kept: Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) for them as for any (FC23.new2 (f))] [r4: A3; W5 (F7): 'Acc ∉ Uses(α)' read as written, at the symbol: no leaf or form of α uses Acc of any candidate **[I196]**; the program read the instance before round 4 (no
(cont.) use of Acc(ℰ) for the candidate at issue), kept for comparison (claims_s41.USES_READINGS); the two part only on an argument whose only use of (E) is Acc(ℰ′) (FC30.new1 (h)); the program's reading of a definition]
- (Suff), L536 and L17: defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]; Def(L17) = Def(L536) [owner S41: Q2: was 'L17 has no ¬Dec(t): Def(L536) ⊊ Def(L17) (E06; Q2)'; L17 writes Account(ℰ) ∧ ¬Dec(t) (S41-Q2)].
- (Nec), L538 = L17: defeated for j ⟺ ∃ℰ [∃α ∈ X_j(¬Expl(ℰ)): Acc ∉ Uses(α) ∧ ∀C' on D ∀t': ¬Faithful_{C'}(t': D → E)].
- (Elim), L540: defeated ⟺ ∃ℰ, ℰ' with equal (F1), (F2), (A) data at every admitted change ∧ a kind-label kl(ℰ) ≠ kl(ℰ′) ∧ Work(kl); Work has no definition; κ stays D5.1's value maps (I14) [r4: A3; S-κ (F6): was 'κ(ℰ) ≠ κ(ℰ') ∧ Work(κ)'; notation, content unchanged].
- (Prov), L542: (i) ∃t [Sel(t;𝒯,μ,H) ∧ (a,b) ∈ C∖H ∧ ∃t' ∈ 𝒯 surviving on H with value_t'(a,b) ≠ value_t(a,b) ∧ value_t(a,b) a function of (𝒯,H)]: unsatisfiable by definition (FC80 (a)); (ii) 'without loss' and (iii) 'operates on' have no definition.
- (QF), L544: 'fails to capture' and 'not creative' have no definition. A mathematical error, L546: a model of a named claim's hypotheses where its conclusion fails (FC109).
No computation decides a defeat condition; a defeat is an argument some j can use (Out_j), and the ruling out is j's choice (L397, S28). [r2: A3; new; NF02, NF03, NF05, E06]

## §17 The text's exact constructions, encoded

⟦FROZEN⟧ E1
**E1 The pole and its shadow** **[I65]**.

> L325 | Stipulate \(H:=U_H,\ \theta:=U_\theta,\ L:=H\cot\theta\), where \(U_H\) and \(U_\theta\) are exogenous values setting the pole's height \(H\) and the sun's elevation \(\theta\), and \(L\) is the length of the pole's shadow.

D_pole: V = {H, θ, L}; B ∋ b = (u_H, u_θ); J = {c_H, c_θ, c_L}, V_cH = {H}, V_cθ = {θ}, V_cL = {H, θ, L}; L_cH(1,b) = {H = u_H}, L_cθ(1,b) = {θ = u_θ}, L_cL(1,b) = {L = H cot θ}; A: setH_h, setθ_φ, setL_l (each replacing its component, D2.1) and their composites. Production question: Q = Q_L; contracts C1 = settings of H and θ, C2 = C1 plus settings of L. E_rev (the reversed calculation): c'_L: L = the observed value (boundary), c'_θ, c'_H: H = L tan θ. Identification contract: C_id := {1} × B (u_H and u_θ varying; no setting edit) [r2: A2; E1, I65; A2-T13]; Q = the fibre {H : H cot θ = observed L}. Test grids: H ∈ {1,2,3}, θ ∈ {30°, 45°, 60°}. Claims: FC02, FC07, FC26–FC28, FC27.new1, FC99. [r4: A2; B4, C-K1 **[I193]**: settled by L271's colon: the transport carries the intervention on the upstream port to itself, and under it E_rev fails (F2) on C1 and on C_H := {1} ∪ settings of H, a production contract too (L151, D3.3 Prod) (FC27.new1 (b)); τ′ on C_H, under which E_rev meets (F2) and every conjunct of (E) (FC27.new1 (d)), is another candidate, which L271 does not describe] [r4b: second check; O2: B4, C-K1 ruled I, not W; R4A2-T1 (L271) and R4INT-T1 (L536) withdrawn; was ''the production contract' of L271 is C1 (R4A2-T1: '\(C_1\) (E1, FC27)'), and that of L536 (R4INT-T1; integration, pair 7)']

⟦FROZEN⟧ E2
**E2 Identification** **[I63, I64]**.

> L329 | Let \(Z\) be the admitted states, \(g:Z\to Y\) the measurement, \(f:Z\to F\) the feature. The fibre at \(y\) is \(Z_y=g^{-1}(y)\). The feature is identified at \(y\) exactly when \(Z_y\neq\varnothing\land|f[Z_y]|=1\). (I1)

Ident_y(f, g) :⟺ Z_y ≠ ∅ ∧ |f[Z_y]| = 1 (I1). (I2): (∀y ∈ g[Z] Ident_y) ⟺ f = f̄∘g for some f̄. (I3): for Z a vector space, g linear on Z, f = cᵀ: identification at every attainable y ⟺ ker g ⊆ ker cᵀ [r2: A2; I64, FC58]. Claims: FC57, FC58.

⟦B2⟧ E3
**E3 The two balances.** G = [[1,1,0],[1,0,1]] on (x, b_A, b_B) (L331). Claims: FC59, FC60.

⟦B2⟧ E4
**E4 Obstruction.**

> L335 | For allowed steps \(R\) and an invariant \(I\) with \(zRz'\Rightarrow I(z)=I(z')\), no allowed path joins states of different invariant value. (O1)

States with a step relation R and an invariant I; reachability R*. Tokens: distributions (n1, n2, n3) of 23 whole tokens. Claim: FC61.

⟦B2⟧ E5
**E5 Explanation that removes structure** **[I03]**. D with a component x deleted at the baseline and an edit a_x giving it a relation; E with k, λ(k) = {x}. Claim: FC62.

⟦B2⟧ E6
**E6 Odd-order skew-symmetric matrices** **[I66]**.

> L343 | Contract: remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed.

Ports: n, the entries M_ij, det, inv; components: skew (Mᵀ = −M), odd (n odd), det (Leibniz sum), inv (inv ⟺ det ≠ 0); edits: delete skew, delete odd, delete both; Q: does the family contain an invertible matrix? Leibniz candidate: one component per permutation term, one sum component. Test fields GF(p), p odd. Claim: FC63.

⟦B2⟧ E7
**E7 Transport results.**

> L353 | If \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\), the same equation is met by every admitted finite composition with matching scopes.

> L358 | zRy\land z\xrightarrow{a}z'\Rightarrow\exists y'[y\xrightarrow{\tau(a)}y'\land z'Ry'], \tag{T1}

> L363 | With one-step discrepancy \(d(\pi Sz,T\pi z)\le\varepsilon\) at every state \(z\) of a stated scope, and with \(T\) \(L\)-Lipschitz for \(d\), the discrepancy after \(n\) steps from one state \(z\), \(e_n=d(\pi S^nz,T^n\pi z)\) (so \(e_0=0\)), meets the bound \(e_n\le\varepsilon\sum_{k<n}L^k\)

Functional, relational (T1, forward and backward simulation) and approximate (T2) transport as written. Claims: FC64–FC66.

⟦B4⟧ E8
**E8 A contract as an organization** **[I67]**.

> L590 | Give it ports (the edits and their boundaries), components (the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits (add or remove a change; alter \(\mathcal Q\)).

D_C: one port m_(a,b) ∈ {0,1} per (a,b) ∈ A × B and a query port q; components: the baseline condition m_(1,b0) = 1 and the closure conditions the question declares; edits: set a membership port, set q, and composites. Claim: FC97. [r2: A3; L590 lists 𝒬 among the ports (A3-L590.1); I67 fixed for the query port]

⟦FROZEN⟧ E9
**E9 The two-layer episode** **[I68, I69]**.

> L620 | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell, swap the two identities.

P: N cells, two things (position, velocity ∈ {−1, 0, 1}), steps 0..K, continuity pos(t+1) = pos(t) + vel(t) with reflection at the ends; occupancy reading per cell, empty when occluded; swap exchanges the two things' states. S0: window-w occupancy predictor, t0 selected on H0 (displacements, velocity changes). S1: a component per thing carrying position and velocity through occlusion, a persistence component, t1 with λ sending each persistence component to its thing's continuity subnetwork. ψ: the exchange of the two things, ψ ∈ Aut(P), ψ[C] = C, Ans_p∘ψ = Ans_p. S0's window w ≤ L_occ, L_occ the steps a thing is hidden **[I155]**; the two things do not interact, may share a cell and cross **[I160]**. Claims: FC90, FC102, FC103. [r2: A3; I68, I69, I100; A3-L626.1, A3-L630.1] [r3: A3; K4: E9 built on a small instance, model/e9.py (4 cells, frames 0..3, S0 window 2) **[I182]**; FC102.new1, FC103.new1 computed as the text claims]

## §18 Dependence, invariance, and where the text was vaguest

> L526 | **Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined.

⟦FROZEN⟧ D18.1
**D18.1 The dependence graph.** Nodes: the symbols defined in §§1–16 (D-numbered). An edge from a definition to each symbol its right-hand side uses. Sinks allowed by the text (L526, L596): Θ with Org_ℓ, 𝒩, (O), (Q), the indices, the declared inputs of L522. The primitives of D0.2 are sinks the text does not list; FC98 asks of each whether it is a claim read through Θ. Of the two loops S101 read from the wording, K2 → Live → K2 closes below the step (D9.4, D9.6). The other, build → prov → rep, stays open here: L405's 'prepares a represented organization' asks for (R), (R) asks for Sel or Con, and Con asks for a construction trace, which is what Build's subhistory is. D13.3 hides the loop only by making Prepares a primitive [I56]; with 'represented' read through (R), Build, Con and Rep are defined together, as one fixed point, unless Con's trace is read without (R). The text names the risk at L526 ('A representation defined only by its own construction … has not supplied its place in the order'). FC98 tests both loops.
New [r2: A3; D18.1, FC32, E03; A3-L526.1] [r2b: second check; R5]: + edges NonCircular → (O), (Q), C, ℓ, δ; NonVacuous → (O), C, Σ (t and Γ are the candidate's own data, as for (F1), (F2), (A); NC0–NC2 read no signature). One edge set: this, the program's DEP and L526's pointer (D18.1) (FC32). The loop Rep → Con → Build → Rep is cut by Rep^ρ **[I146]**; ρ := T′ **[I162]** [r2b: R3; Q1 ruled]: [r3: A3; S2(i), S2(ii), S3 (F6): the program's graph (claims_b.DEP) now has 82 nodes; every paragraph D1.1–D16.XV is a node or folded into one (D_TO_NODE) **[I181]**; Sel → (F1), (F2), CT, 𝒯pop, surv, Occurs, staged (R); Con → CT, Episode; Dec → Sel, Con, TransferComposite; Build → ExplUse → (E) (I178); (K3) → Out, (K2), RO; L526's grouped subjects read together **[I179]**; U: cycles; K, T, T′: none (FC32.new1); round 2's graph kept as DEP_R2] [S106: S44, S45: Dependence → (O), (Q), C, δ (was NonCircular → (O), (Q), C, ℓ, δ; ℓ only NC1 read, I28); Slot (D6.3) → (O), (Q), C, ℓ, δ, Cand, no longer an ancestor of (E); (E) → (F1), (F2), (A), Dependence, NV; the program's DEP: node 'NC' renamed 'Dep', node 'Slot' added, D_TO_NODE: D6.3 → Slot (FC32, FC32.new1)] [S106b: node Open (D6.11) deleted with D6.11]
- Held_ℓ(o', c) :⟺ ∃t: Org_ℓ(o') → E_c faithful (D5.7) on {(a,b) : (τ(a),σ(b)) ∈ C_c} with Γ_c active (D12.5's extent), no provenance; so Rep_ℓ ⇒ Held_ℓ [r3: A1; S-D2: was '∃t Faithful(t: Org_ℓ(o') → c) (through Θ, no provenance)'; FC98.new1 (b): Rep ⊆ Held on every case];
- T′: Con's 'available as a represented target' (D12.2, L197) := Held at o' ⪯ o_t in the episode; Build reads Held_ℓ(o, c) outright (D13.3; L405 since R3A3-T4), under every reading; Sel's exclusion (D12.1) := ¬Rep at o' ≺_h o_t, a recursion along ≺_h, unique (D11.3) [r3: A1; B3 and A3; S1: was 'unique where ≺_h is well founded below o_t (every finite history)'; on an infinite descending chain the equations have no fixed point, FC98.new1 (a), FC98.new2 (a)]. [r4: A3; S2 (F2): was 'Con's … (D12.2) and Build's 'represented organization' (D13.3) := Held at o' ⪯ o in the episode'; the program's DEP['Build']: staged (R) → Held, under every reading; the r3 mark's 'Build → ExplUse → (E)' now reads Build → Held, ExplUse; ExplUse → (E); FC98 (a), (a′) re-based, results unchanged] [r4: integration; pair 5: FC83's build_at keeps round 2's reading of L405's old wording under the rejected cuts U and K (Build through (R), staged under K), named alternatives FC83 names; under T and T′ it reads Held, as DEP does; read as Held under K, FC83 (a) gives K's own defect (FC98 (d); area 3 runs §3.6); not changed] [r4b: second check; O3: FC83's statement re-based to T and T′, U and K with round 2's reading a comparison; FC83's look computes U and K with Build read as Held: U no counterexample, K one, K's defect]
Rejected, each on a computed case: U (as worded): 0–5 fixed points, none for a selection (FC98 (c)); K ((R) staged in Sel, Con, Build): a first construction of c gives no representation (FC98 (d); against L405); T (Held also in Sel's exclusion): an earlier holder by a declared transport blocks a selection (FC98 (e); against L195 with L211). T′: one fixed point on every chain of ≤ 4 occurrences; with I161, Sel ∧ Con at none (FC12.new1).

⟦FROZEN⟧ D18.2
**D18.2 Structure-preserving bijections** **[I70]**. A bijection φ of ports, values, components, edits (a partial-monoid isomorphism), boundaries and occurrences (preserving ≺_h and Θ's interpretation), with Q, δ, Σ and every declared input carried along. Argument 8 (FC100) is the claim that (E), (G), (P) and (EX) are kept by every such φ, the indices ℓ, β, Ω held fixed (L612). [r2: A3; D18.2, FC100, I70]

**Where the text was vaguest, for this formalization.** Three places needed the most inventions, and each carries weight elsewhere:

1. **Roles and families in Part II (L103, L109, L119, L123–L127).** The text speaks of 'the component assigning' a port and of 'observation edits', and supplies neither an assignment nor a way to read one off relational components; the two readings of L109's observation give different families on the pole's own contract (FC07), and L127's gloss adds a condition on solutions that (K) does not record (FC08). Inventions I04–I13.
2. **Non-circular dependence (L255, L257).** Its one fully formal sentence (NC2) does not exclude a lookup of the answer ('p because p' meets NC2 when the answer varies, FC23); the exclusion rests on NC1, whose 'unanalysed', 'at the declared grain' and 'structural' are defined nowhere, and on 'in the claimed way'. Inventions I21–I28. [S106: the least defined sentence (NC1) is out of (E); what stays of it is Slot, content a criticism can point at (D6.3); the condition is Dependence (D6.5)]
3. **How one query and one contract apply across organizations (L141, L253, L250; L205, L413).** (A) applies the target's query to the candidate's organization, whose ports differ; (R) and ≡ ask a transport into a content to be faithful 'on c's contract', a contract on the codomain, which a transport's conditions quantify over on the domain. Every (A), (R), New, Origin and (EX) rests on the choice. Inventions I20, I48.

Next after these: the undefined primitives of Parts IX–XI (L375, L385, L403, L405, L453; I46, I47, I55, I56, I60), each read as a plain word by the round-1 checkers and each needing a primitive predicate here.

**Counts.** 115 numbered definitions (D0.1–D18.2) and 9 encodings (E1–E9); 76 inventions, each marked here where it is used and recorded in `inventions register.md`; 110 claims in `formal claims.md`. After round 2: 118 definition paragraphs (D2.6, D8.new1, D16.XV new); 67 [r2] marks; inventions I122–I160 (`inventions register - addendum after round 2.md`); 113 claims (`formal claims, after round 2.md`). Second check on the critical review: 20 [r2b] marks; CT (D12.2) and Held (D18.1) defined; the cut ρ := T′ (Q1 withdrawn); inventions I161–I164. The owner's answers (S41): 10 [owner S41: Qn] marks (D6.4 and §6's Vague, Q15; D9.2, D9.6, D9.7, Q23; D0.2, D12.2, D13.8, Q6; D16.XV twice, Q2); inventions I165, I166; claims FC30.new1, FC84.new1 (115 claims). After round 3 (S105): no definition paragraph added or removed (118); definitions changed in form: D3.3, D4.6, D5.7, D11.2, D11.3, D12.1 (three fixes), D12.2, D12.3, D13.3, D13.8, D14.7, D18.1 (Held, uniqueness, the program's graph); re-based: D12.7, D12.8, D12.9, D15.8; D0.2's list extended; notes without a formal change: D6.3, D8.3, D9.6, D9.7, D10.6, D16.XV, E9; inventions I167–I182 (`inventions register - addendum after round 3.md`); 134 claims (`formal claims, after round 3.md`). Second check on the critical review of round 3: D16.4 changed in form (δ quantified, as D14.7; I183); 3 [r3b] marks (D12.2, D16.4, D16.XV); 134 claims, test parts FC30.new1 (g), FC32.new1 (f) added. S106 (decisions S44, S45): 119 definition
(cont.) paragraphs (D6.11 new); definitions changed in form: D6.5 (Dependence := NC0 ∧ NC2), D6.7 (Acc with Dependence; no grain), D18.1 (edges; the program's DEP); renamed in D6.8; notes without a formal change: D6.2, D6.3, D6.10, D9.7, D9.10, D10.6, D16.XV, §6 and §9 Vague, §18 item 2; inventions I184–I189 (`inventions register - addendum after S106.md`); 137 claims (`formal claims, after S106.md`: FC23.new2, FC23.new3, FC25.new2 new). S47: no definition paragraph added or changed in form; notes on D12.2, D13.8 and §12 Vague; FC84.new1 (a) re-encoded as (a1), (a2); FC32.new1 (f) restated; inventions I190, I191; 137 claims. Second checker on the critical review of S106 [S106b]: D6.11 withdrawn, 118 definition paragraphs; Pin a clause of D6.3 (no change in form); inventions I185, I186 withdrawn; 137 claims: FC23.new2 (c)–(e), FC23.new3 (b), (c) and (d)'s LeavesOpen clause deleted, FC23.new2 (f) computed, (g) a look. Round 4 (S107): 118 definition paragraphs (none added or removed); changed in form: D0.2 (twice: A3 F3, F4), D6.3 (A2 F1), D7.4 (A2 F2), D18.1 (A3 F2: the T′ item and the program's graph); notation: D9.10 (A3 F5), D16.XV (Elim) (A3 F6); the program's reading: D16.XV's Uses (A3 F7, I196); marks without a formal change: D6.9 (A2 F3), D9.7 (K1), D12.2, D13.8 (A1; I192), D18.1 (pair 5), E1 (I193); inventions I192–I197 (`inventions register - addendum after round 4.md`); 142 claims (`formal claims, after round 4.md`: FC27.new1, FC23.new4, FC23.new5, FC42.new1, FC72.new2 new;
(cont.) test parts FC84.new1 (a3), FC30.new1 (h) new; FC31, FC98, FC32.new1 re-based). Second checker on the critical review of round 4 [r4b]: no definition changed in form; marks on D12.2, D13.8 (O1, O4), E1 (O2), D18.1 (O3); no text change (R4A2-T1, R4INT-T1 withdrawn); 142 claims: FC84.new1 (a4) and FC83's look new (test parts); FC84.new1 (a3), FC27.new1, FC72.new2 (b), (d) and FC83 restated.

*Written 27 September 2026; integrated after round 2 on 28 September 2026; after round 3 on 28 September 2026; S106 (the written-in test taken out) on 28 September 2026; after round 4 (S107) on 28 September 2026; second check of round 4 on 28 September 2026.*

## 6. The claims, by section

Each claim with the lines its statement cites, and the free sections of the free sentences among them. A claim is a consequence the program tests; a variant that changes a definition may change a claim's result.

| claim | title | lines | free sentences cited, by section | result now |
|---|---|---|---|---|
| FC01 | Solutions shrink as relations shrink; deletion never removes a solution | L100, L103 | B1 | HOLDS ON ALL MODELS TRIED |
| FC02 | Direction is read from the admitted edits; output status is not | L109, L325 | B1, B2 | HOLDS ON ALL MODELS TRIED |
| FC2.new1 | The ground of D2.4: under R-i no reader of an assigned port is causal | L109, L123 | B1 | HOLDS ON ALL MODELS TRIED |
| FC03 | 'Of one kind on C' is an equivalence relation | L119 | — | HOLDS ON ALL MODELS TRIED |
| FC04 | A coarser contract identifies more components; a finer one can separate them | L119 | — | HOLDS ON ALL MODELS TRIED |
| FC4.new1 | L127's reading-part sentence in symbols | L127 | B1 | HOLDS ON ALL MODELS TRIED |
| FC05 | Kinds are fixed by relations, not by solution values | L119 | — | HOLDS ON ALL MODELS TRIED |
| FC06 | A setting edit leaves every reader's relation as it was | L119, L124 | B1 | HOLDS ON ALL MODELS TRIED |
| FC07 | The three families on the pole's contracts, under both readings of 'observation edit' | L109, L123, L127, L325 | B1, B2 | HOLDS ON ALL MODELS TRIED |
| FC08 | L127's gloss of a measurement's signature has a clause about solutions | L119, L127 | B1 | HOLDS ON ALL MODELS TRIED |
| FC09 | Four names, three families: a constitutive status is a rule application | L121, L347 | B2 | HOLDS ON ALL MODELS TRIED |
| FC10 | L57 against the new L123 | L57, L123 | B1 | HOLDS ON ALL MODELS TRIED |
| FC11 | Roles are relative to A; families are relative to C | L109, L113 | B1 | HOLDS ON ALL MODELS TRIED |
| FC12 | Invariance clauses can be vacuous; change clauses cannot | L124, L125 | B1 | HOLDS ON ALL MODELS TRIED |
| FC12.new1 | Selected and constructed exclude each other under D12.1 | L193, L195, L197, L201 | B3 | HOLDS ON ALL MODELS TRIED |
| FC12.new2 | Provenance per holding; a record carries its source's |  | — | HOLDS ON ALL MODELS TRIED |
| FC12.new3 | CT's 'prepares' exact, not transitive |  | — | HOLDS ON ALL MODELS TRIED |
| FC13 | The families are patterns in (K), not additional data | L127 | B1 | HOLDS ON ALL MODELS TRIED |
| FC13.new1 | D4.6's o_j when one component assigns two ports |  | — | HOLDS ON ALL MODELS TRIED |
| FC14 | No definition asks whether a component 'is' a cause | L127 | B1 | HOLDS ON ALL MODELS TRIED |
| FC15 | τ[C] is a contract of the candidate's organization | L141, L242, L554 | B1 | HOLDS ON ALL MODELS TRIED |
| FC16 | Reading a candidate's components through the transport agrees with (K) on τ[C] | L119 | — | HOLDS ON ALL MODELS TRIED |
| FC17 | Argument 1: (F1) makes each commitment's signature its counterpart's | L245, L554, L556 | B2, B4 | HOLDS ON ALL MODELS TRIED |
| FC18 | Argument 1's Consequence: a same-kind condition adds nothing; no third case | L281, L558 | B2, B4 | HOLDS ON ALL MODELS TRIED |
| FC19 | (F1) and (F2) do different work | L245 | B2 | HOLDS ON ALL MODELS TRIED |
| FC20 | When (F2) at a pair gives (A) at that pair (violation in either extent) | L219, L220, L250 | B3 | HOLDS ON ALL MODELS TRIED |
| FC21 | A contract of relabelings admits no candidate meeting (A) and Dependence | L257 | — | HOLDS ON ALL MODELS TRIED |
| FC22 | The baseline alone gives no contrast | L141, L255 | B1 | HOLDS ON ALL MODELS TRIED |
| FC23 | 'p because p' meets Dependence where its answer varies; its slot is content, not a failure of (E) | L273 | — | COUNTEREXAMPLE FOUND |
| FC23.new1 | D6.3's quantifier: four readings of Slot; (E) the same under all four |  | — | HOLDS ON ALL MODELS TRIED |
| FC23.new2 | The owner's shop sign (S44): an explanation under (E) after S106 |  | — | HOLDS ON ALL MODELS TRIED |
| FC23.new3 | Pin (D6.3's clause at one pair) on generated models and on the pole |  | — | HOLDS ON ALL MODELS TRIED |
| FC23.new4 | D6.3 with 't translates (a,b)' inside the ∀: Slot is Pin at every pair of Det_C |  | — | HOLDS ON ALL MODELS TRIED |
| FC23.new5 | The owner's sign on a target with one part: the two-part candidate fails (F1), not for a slot | L245 | B2 | HOLDS ON ALL MODELS TRIED |
| FC24 | L273's second sentence used 'account' for a candidate; packaging leaves the slot (content) | L273 | — | HOLDS ON ALL MODELS TRIED |
| FC25 | Tables: a fixed table fails (F1) where the projection moves; an encoding table meets it | L269 | — | HOLDS ON ALL MODELS TRIED |
| FC25.new1 | L269's formula (a*) for a table varying with the boundary |  | — | HOLDS ON ALL MODELS TRIED |
| FC25.new2 | L269's encoding table meets (E) where its answer varies; its one component a slot | L269 | — | HOLDS ON ALL MODELS TRIED |
| FC26 | The pole: the forward organization meets (E) on the production contract | L325 | B2 | HOLDS ON ALL MODELS TRIED |
| FC27 | The pole: the reversed calculation fails (F2) on the production contract | L271, L325 | B2 | HOLDS ON ALL MODELS TRIED |
| FC27.new1 | L271's reversed calculation: under the transport its colon describes, (F2) fails on C1 and C_H | L151, L271 | B1 | HOLDS ON ALL MODELS TRIED |
| FC28 | The pole: the reversed calculation meets (F1), (F2), (A) on the identification contract | L325 | B2 | HOLDS ON ALL MODELS TRIED |
| FC28.new1 | Ident on the pole under D3.3 (B7's code; N3) |  | — | HOLDS ON ALL MODELS TRIED |
| FC28.new2 | obs where g is not single on Sol: three readings |  | — | HOLDS ON ALL MODELS TRIED |
| FC29 | A contrast no admitted edit realizes witnesses nothing | L275 | — | HOLDS ON ALL MODELS TRIED |
| FC30 | (E) takes no assessor, history or provenance | L43, L67, L277 | B1 | HOLDS ON ALL MODELS TRIED |
| FC30.new1 | (Suff) at L17 and at L536: one defeat set; a declared account ruled out as an explanation defeats neither | L17, L536 | — | HOLDS ON ALL MODELS TRIED |
| FC31 | 'The four conditions', five conjuncts, and L520's three sources | L61, L231, L262, L520, L536 | B4 | NOT TESTED |
| FC32 | L520 (after round 1) against L526's dependence order | L520, L526 | B4 | HOLDS ON ALL MODELS TRIED |
| FC32.new1 | D18.1's graph against the formal core and L526 |  | — | HOLDS ON ALL MODELS TRIED |
| FC33 | 'Every conjunct is a condition on supplied relations; none inspects a label' | L265 | B2 | HOLDS ON ALL MODELS TRIED |
| FC34 | Two questions, one target: what 'an answer to one is not an answer to the other' allows | L151 | B1 | HOLDS ON ALL MODELS TRIED |
| FC35 | 'Prediction' at L151 is outside L219's definition | L151, L217 | B1, B3 | NOT TESTED |
| FC36 | What a question asks is fixed by the query and the contract, not by a label | L151 | B1 | HOLDS ON ALL MODELS TRIED |
| FC37 | The finite monotone claim | L305 | — | HOLDS ON ALL MODELS TRIED |
| FC38 | Redundant routes | L307 | B2 | HOLDS ON ALL MODELS TRIED |
| FC39 | Interference | L305, L309 | B2 | HOLDS ON ALL MODELS TRIED |
| FC40 | Infinitary routes: collective criticality, and the step the first sentence leaves unsaid | L311, L313 | B2 | HOLDS ON ALL MODELS TRIED |
| FC41 | Commitments that do no work, and why 'when Γ is infinite' | L313 | — | HOLDS ON ALL MODELS TRIED |
| FC42 | Criticality is relative to the route | L299 | B2 | HOLDS ON ALL MODELS TRIED |
| FC42.new1 | D7.4's Boundary with the designation carried (δ_v) |  | — | HOLDS ON ALL MODELS TRIED |
| FC43 | Conflict, rivals, problems and 'easy to vary' are symmetric | L317 | B4 | HOLDS ON ALL MODELS TRIED |
| FC44 | Two commitments with one counterpart and different relations cannot both meet (F1) | L315 | B4 | HOLDS ON ALL MODELS TRIED |
| FC45 | Recoded candidates, and candidates some relations let both meet, conflict nowhere | L315 | B4 | HOLDS ON ALL MODELS TRIED |
| FC46 | A conflict inside the contract: at most one account | L317 | B4 | HOLDS ON ALL MODELS TRIED |
| FC47 | A test at a conflict pair rules out at least one, for an assessor who can use it | L317 | B4 | HOLDS ON ALL MODELS TRIED |
| FC47.new1 | Solved, posed again, solved (D10.1, D10.6) |  | — | HOLDS ON ALL MODELS TRIED |
| FC48 | No conflict inside the contract: answers agree there | L317 | B4 | HOLDS ON ALL MODELS TRIED |
| FC49 | The two kinds of problem exclude each other and cover every pair of rivals | L317 | B4 | HOLDS ON ALL MODELS TRIED |
| FC50 | A finer contract makes a problem of the first kind; a narrowed one leaves the problem on p | L317 | B4 | HOLDS ON ALL MODELS TRIED |
| FC51 | A change that separates two accounts lies outside their shared contract | L317, L568 | B4 | HOLDS ON ALL MODELS TRIED |
| FC52 | Conflict with a claim: the first disjunct implies the second | L315 | B4 | HOLDS ON ALL MODELS TRIED |
| FC53 | Conflict with a claim rules a candidate out only with the premise that the claim speaks of the target | L315 | B4 | HOLDS ON ALL MODELS TRIED |
| FC54 | Rivals given χ conflict nowhere without χ at that pair | L315 | B4 | HOLDS ON ALL MODELS TRIED |
| FC55 | Nothing in Part VI counts rivals or orders candidates | L317 | B4 | HOLDS ON ALL MODELS TRIED |
| FC56 | Ruling out grows with what is accepted; withdrawal rules nothing out; absence rules out nothing | L393, L397 | B4 | HOLDS ON ALL MODELS TRIED |
| FC57 | (I2): identified at every attainable value exactly when the feature factors through the measurement | L329 | B2 | HOLDS ON ALL MODELS TRIED |
| FC58 | (I3): the kernel criterion; repeated rows; an independent calibration | L329 | B2 | HOLDS ON ALL MODELS TRIED |
| FC59 | The two balances | L331 | — | HOLDS ON ALL MODELS TRIED |
| FC60 | Setting a bias from the favoured mass: where the circularity can be registered | L331 | — | HOLDS ON ALL MODELS TRIED |
| FC61 | (O1): an invariant blocks paths; equal values do not give paths; twenty-three tokens | L335 | B2 | HOLDS ON ALL MODELS TRIED |
| FC62 | Eliminative explanation: the rival's structure as a deleted counterpart | L339 | — | HOLDS ON ALL MODELS TRIED |
| FC63 | Odd-order skew-symmetric matrices | L343 | B2 | COUNTEREXAMPLE FOUND |
| FC64 | Functional transport | L353 | — | HOLDS ON ALL MODELS TRIED |
| FC65 | Relational transport: simulations compose | L361 | B2 | HOLDS ON ALL MODELS TRIED |
| FC66 | (T2): the accumulated bound, and none without a modulus | L363 | — | HOLDS ON ALL MODELS TRIED |
| FC67 | A declared invertible recoding keeps the content | L365 | — | HOLDS ON ALL MODELS TRIED |
| FC68 | A failed answer stays failed | L369 | B2 | HOLDS ON ALL MODELS TRIED |
| FC69 | (K2) is well founded; the loop read in S101 closes below the step | L390, L393 | — | HOLDS ON ALL MODELS TRIED |
| FC70 | Withdrawing a premise that is live twice over leaves the step usable | L393 | — | HOLDS ON ALL MODELS TRIED |
| FC71 | (K3): a failed prediction rules out the conjunction, and nothing narrower | L395 | — | HOLDS ON ALL MODELS TRIED |
| FC72 | The block on a premise that is the denial, and a premise taken as given | L397 | B4 | HOLDS ON ALL MODELS TRIED |
| FC72.new1 | A premise alone: usable when taken up; rules out with no step |  | — | HOLDS ON ALL MODELS TRIED |
| FC72.new2 | K1: the myth about winter after S106 | L317 | B4 | HOLDS ON ALL MODELS TRIED |
| FC73 | Inconsistent accepted premises rule out a claim and its denial alike | L397 | B4 | HOLDS ON ALL MODELS TRIED |
| FC74 | A criticism occurrence can exist without bearing | L383 | B4 | HOLDS ON ALL MODELS TRIED |
| FC75 | Active routes: the excluded routes fail the definition's own clauses | L375 | B4 | HOLDS ON ALL MODELS TRIED |
| FC76 | Reason use gives neither bearing nor usability | L385 | B4 | HOLDS ON ALL MODELS TRIED |
| FC77 | Without a physical witness, selection is met by every transport | L195, L205 | B3 | HOLDS ON ALL MODELS TRIED |
| FC78 | Exactly one of three provenances | L193, L201 | B3 | HOLDS ON ALL MODELS TRIED |
| FC79 | Survival is how the transport got there; fidelity is what it is | L41 | B1 | HOLDS ON ALL MODELS TRIED |
| FC80 | Argument 3: underdetermination where the population leaves room | L572, L574 | B4 | HOLDS ON ALL MODELS TRIED |
| FC80.new1 | The survival condition enacted by the environment |  | — | HOLDS ON ALL MODELS TRIED |
| FC81 | Argument 4, and who can be surprised | L223, L580 | — | HOLDS ON ALL MODELS TRIED |
| FC82 | The two responses to a violation have no common result | L225 | B3 | HOLDS ON ALL MODELS TRIED |
| FC83 | Only the construction response can be originative | L225 | B3 | HOLDS ON ALL MODELS TRIED |
| FC84 | Every creative attribution requires construction | L47 | B1 | HOLDS ON ALL MODELS TRIED |
| FC84.new1 | Something can be constructed where the question never changes | L55, L197 | — | HOLDS ON ALL MODELS TRIED |
| FC84.new2 | 'Immediately after' as the covering relation |  | — | HOLDS ON ALL MODELS TRIED |
| FC85 | A content matches itself; the matching is read one way | L413, L416 | — | HOLDS ON ALL MODELS TRIED |
| FC86 | Repair: a protected aim failed in between is lost | L438, L441 | B3 | HOLDS ON ALL MODELS TRIED |
| FC87 | Two sufficient contributions that both ran are both attributed | L441 | B3 | HOLDS ON ALL MODELS TRIED |
| FC88 | Losses outside P are exposed in the claim, not in (P) | L441 | B3 | HOLDS ON ALL MODELS TRIED |
| FC89 | L443 (after round 1) puts 'deployable' where Deploy's type allows it | L443, L449 | B3 | NOT TESTED |
| FC90 | The worked case's '(EX) is met' against (EX)'s conjuncts | L628 | — | HOLDS ON ALL MODELS TRIED |
| FC90.new1 | ExplUse through the claim 'Acc(ℰ)'; (EX)'s δ_c |  | — | HOLDS ON ALL MODELS TRIED |
| FC91 | (CT1) is C ⊆ F(C) only with (CT1)'s completion read into F | L466, L471 | — | HOLDS ON ALL MODELS TRIED |
| FC92 | (CT2): monotone F and its greatest fixed point | L471, L546 | B4 | HOLDS ON ALL MODELS TRIED |
| FC93 | (CT3), (CT4), and capability at one tolerance | L479 | B3 | HOLDS ON ALL MODELS TRIED |
| FC94 | Recursion does not entail universality | L509 | B4 | NOT TESTED |
| FC95 | A system can represent a theory in error | L211 | — | HOLDS ON ALL MODELS TRIED |
| FC96 | Argument 2: same counterparts, one account | L562 | B4 | HOLDS ON ALL MODELS TRIED |
| FC97 | Argument 5: a contract can be an organization and a content | L588, L590 | — | HOLDS ON ALL MODELS TRIED |
| FC97.new1 | H and the survival condition as contents (L590) |  | — | HOLDS ON ALL MODELS TRIED |
| FC98 | Argument 6 and the dependence order: acyclic, and ending where the text says | L526, L596 | B4 | HOLDS ON ALL MODELS TRIED |
| FC98.new1 | Well-foundedness and the T′ equations; L195's strict exclusion |  | — | HOLDS ON ALL MODELS TRIED |
| FC98.new2 | S1's infinite chain: no fixed point; well-founded histories one |  | — | HOLDS ON ALL MODELS TRIED |
| FC99 | Argument 7: an account on C can fail on C' | L606 | — | HOLDS ON ALL MODELS TRIED |
| FC100 | Argument 8: structure-preserving bijections keep (E), (G), (P), (EX) | L612 | — | HOLDS ON ALL MODELS TRIED |
| FC101 | Argument 9: an input–output description does not fix an account | L616 | B4 | HOLDS ON ALL MODELS TRIED |
| FC102 | Argument 10: surprise, the structural failure of selection, and the constructed layer | L624, L626 | B4 | HOLDS ON ALL MODELS TRIED |
| FC102.new1 | E9 built: t0 selected on H0, surprised at re-emergence |  | — | HOLDS ON ALL MODELS TRIED |
| FC103 | Argument 10: the swap, two pairings, one account | L630 | B4 | HOLDS ON ALL MODELS TRIED |
| FC103.new1 | E9 built: t1 and t1∘ψ |  | — | HOLDS ON ALL MODELS TRIED |
| FC104 | The two extents of 'fidelity' across the text | L189, L245, L247, L520, L630 | B2, B4 | NOT TESTED |
| FC104.new1 | The two extents of 'fidelity' at L220 |  | — | HOLDS ON ALL MODELS TRIED |
| FC105 | 'Event' is used and never defined; 'occurrence' is defined | L161, L169, L604 | B1, B3, B4 | NOT TESTED |
| FC106 | A question's three defects, as far as they can be written | L161 | B1 | HOLDS ON ALL MODELS TRIED |
| FC107 | Exposing a question's defect is another question | L161 | B1 | HOLDS ON ALL MODELS TRIED |
| FC108 | The first sentence of Dependence adds no condition | L255 | — | HOLDS ON ALL MODELS TRIED |
| FC109 | 'A mathematical error': the named claims, each under its stated assumptions | L546 | B4 | HOLDS ON ALL MODELS TRIED |
| FC110 | The classes are defined; no membership is asserted | L27, L528 | B1, B4 | NOT TESTED |
