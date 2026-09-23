# Revision 2 - plan and test round, draft of 23 September

**DRAFT — not frozen; decisions D1–D11 open**

*Moved into the repository on 23 September 2026 from the session scratchpad, where it was `revision2/02 plan for revision 2 and its test.md`. Edits on moving in: the title, the line above, this paragraph, and the pointers that led into the scratchpad. Written on 23 September 2026 by a Claude subagent for the orchestrator: a plan for revision 2 of the theory and for the round that would test it, with its risks and the decisions D1–D11 to be made before writing starts. Nothing in it is decided or built. The working files it asks to have committed first (3.3, R7, D10) are now at the paths it gives, with the candidate cases and their author rounds in `tests/` rather than the `results/` its text names. The log number it expects for file 13 (S89) has since gone to the source audit and the candidate cases.*

23 September 2026. Written by a Claude subagent for the orchestrator. This is a plan, not a decision, and nothing is built. Nothing in the repository was edited. Section 3 is written in the form of the S81 plans so that it can be frozen as it stands. It becomes a frozen plan only after the decisions listed in section 4 are made and the plan itself has been cross-examined (section 2.7, X2).

## Sources

**Read.**
- The worklist `tests/Revision 2 - worklist, draft of 23 September.md` (W1–W56) and the three checks in `results/S88 Claude's checks of the three defects/`.
- In `Semantics/results/S81 File 11 against every case - outputs/determination/`: files 03, 04 and 05 and the READ ME in full, plus the parts of 01 and 02 that 03 and 04 cite.
- File 11 in full. File 10, file 12 and file 00 at the lines cited here.
- The S88 brief (`tests/S88 Cross-examination - three defects in the theory's own defeat list.md`) and the S88 reading rule (`results/S88 How the cross-examination will be read - ….md`).
- The READ ME of the supplementary Mimo-on-A folder, and the word counts of its briefs.
- The three S81 plans; the S81 Stage 1 and Stage 2 instruction files; the S81 case book and its provenance file.
- S75 and S78 Results.
- The records: Decisions, Lessons, the project story (S76, S78, S79, S81, S83) and Status.
- `results/S89 The theory against its sources - Deutsch and Marletto.md` and `tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md`.
- The session's process audit, the S81 tools (`s80_common.py`, `s87_run.py`), LEGEND and `authority/NOT-IN-BUNDLE.md`.
- D3-T's text, in the S72 Stage 2 return, file 04.

**Not opened.**
- Any S87 or S88 return.
- Any return of the supplementary Mimo-on-A audit. Only the folder listing and its READ ME were seen.
- The text of the Pinker book.
- The S81 1C, 1K, 2a and 2b returns. Their word counts were taken with `wc` and nothing else.

**Names.** "F11 L419" is file 11, line 419, and "s2" is a line's second sentence. "00:210" is file 00, line 210. "04 §7.10" is determination file 04, section 7.10, and "03 §8" is determination file 03, section 8. "M28" is a place on 03's master list. The owner's outside models are Atria and Mimo. Claude's own agents are called "Claude subagents" throughout.

---

## 0. What this plan rests on, and what has changed since the worklist

- **S81's standing verdict (04 §6).** File 11 stands as the authority under the plan's second clause. The findings are recorded against its note:
  - 41 undeclared CLAIM places inside the theory, plus the meta place M7. No case shows any of them harmful.
  - P2 fails at O45 only, by a theory change toward the thoughtful person, through M28 (F11 L309 s3, first clause).
  - There are three S75 corrections and seven cross-reference errata (XR1–XR7).
  - This verdict was reached **before** cross-examination. The S87 cross-examination and the supplementary Mimo-on-A audit are still to be read. 04 §7.11 names the rows that decide test (b): O5, O30 and O17. Section 2.2 gives what changes if S81 falls.
- **The owner's word.** Decision S18 is read as the owner's request for a revision 2. The S81 plan anticipated one "if the owner asks". This is Claude's reading, and it is recorded as that. It is not a decision in the owner's words. Under S18 the test for stopping is whether something significant within the scope of the semantics has to be lost. The only claims this plan withdraws are false or misleading ones: Derivation 2's component half, and file 11's "a table … is an account". The rest are narrowings, typings and restorations. Nothing significant is lost, so S18 says continue.
- **The worklist was written from determination files 01 and 02, before 03 and 04 existed.** 03 and 04 change seven of its items:
  - **W3.** O18, O37 and O41 are AGREE under file 10 by the plan's rule, so they are not changed verdicts. Their sentences (M35, M49, M37 and M44) remain undeclared CLAIM places and are simply to be declared.
  - **W4.** O35 is SILENT under file 10 as well (the baseline, both 1K returns, and Claude's reading), so it is SILENT→SILENT. It is not a change away, and no default input is needed to repair it.
  - **W56.** 04 settles O38: AGREE in both files.
  - **O45 is new.** M28 is an undeclared CLAIM that moved O45 toward the thoughtful person. It is to be declared.
  - **W1's counts.** 03 counts 49 CLAIM places: 6 declared, M1 (the note itself), and 42 undeclared. The 42 are 41 inside the theory plus M7; counting M5 with M47, the 41 are 40 distinct changes. Four of them (M19, M21, M46, M59) carry the declared Derivation 3 change at places the note does not list.
  - **Reading hazards found by S81's readers (04 §7.10).** F11 L161 s3 on O5, where 4 of 5 file-11 readings were SILENT. F11 L419 with L514 on O30 and O17. Shared text on O10, where every blind reading and 3 of 5 file-11 marks were not AGREE. Test (b) turned on O5, O30 and O17, and the worklist has no item for L161. It is added as **W57**.
  - **03 §8** lists twelve unclear wordings. Items 10 and 11 are not in the worklist and are added as **W58**. The others map onto W1, W6, W7, W10, W13, W17 and W27.
- **S88** was sent with file 10's text. Derivation 2, (T2) and non-circular dependence read the same in files 10 and 11 (the checks confirm this by diff). The S88 reading rule freezes Claude's positions before either reply is opened:
  - F1: Derivation 2 is false as stated; the repair is "Same anchors, one account".
  - F2: (T2) is a drafting omission; an erratum restores h1–h3.
  - F3: Γ is untyped; option B is preferred to A.
  
  This plan takes those positions and says what follows from each S88 ruling (UPHELD, NARROWED or WITHDRAWN).

---

## 1. Scope

### 1.1 How each item was weighed

An item is taken when at least one of these holds, and its loss (cost in verdict risk) is small and guarded by named cases:
- the theory's own defeat list exposes it (Part XV);
- S81's readers showed a reading hazard that a verdict turned on;
- it is a pointer, label, symbol or hypothesis that can be corrected or restored word for word;
- a source-derived clarification says what the text already implies, with a case to show it.

An item is left out when:
- it adds a new claim that no case in hand earns;
- it adds a default input, a weighting or a grading;
- it imports from file 12, which is under no round, anything beyond wording;
- it conflicts with another item that is taken.

**Grades.**
- Each change carries a **kind**, which says why it is made:
  - **erratum**: corrects or restores a pointer, a label, a symbol or a hypothesis;
  - **clarification**: says what the text implies, or closes a reading the text left open;
  - **change of claim**.
- Each change also carries an **expected ruling** under 03's definitions: CLAIM, WORDING or ORDER.
- Every change whose expected ruling is CLAIM is declared as a change of claim, whatever its kind. Following 03, a clarification that closes an open reading, or states for the first time something derivable from the text, is CLAIM. That is the lesson of file 11's note.

**Stages** (the order of work, 1.5): 1 errata; 2 repairs the defeat list exposes; 3 file 11's verdict-bearing text; 4 source-derived clarifications; 5 the note, the record and the sources note.

### 1.2 The scope list

"Guards" are the rows that must keep their mark; the round's predictions (3.4) use them.

| Item | Recommendation | Kind → expected ruling | Gain | Loss or risk; guards | Stage |
|---|---|---|---|---|---|
| W1 note | **Take**: a new note and a revision record (2.5) replace file 11's L5 | meta | a note a reader can trust; no case id or record file inside the theory (XR1, XR2) | length; withheld from every test brief | 5 |
| W2 carry Derivation 3 onto file 10 | **Leave**: only needed on a file-10 base (2.2 branch C) | — | — | — | — |
| W3 undeclared sentences, and M28 | **Take, declare only**: F11 L401 s5, L518 last, L419 and L465, and L309 s3 first clause, each entered in the record as a change of claim against file 10; no text change | meta | the three toward-sentences and O45's sentence are declared | none | 5 |
| W4 O35 default | **Leave**: no default for occasions; O35 stays SILENT in both files (04) | — | no input chosen from the verdict wanted | O35 is not AGREE | — |
| W5 (P) against the occasions prose | **Take**: after (P), state in words that for a protected condition \(r(\xi')\) means r held on every occasion it covers from \(\xi\) to \(\xi'\) | clarification → CLAIM | the formula and the prose say one thing | (P) becomes history-valued; Derivation 8 carries occasions. Guards: O35 (SILENT), O38 (AGREE) | 3 |
| W6 \(\mathcal N\), and L27's overclaim (XR3, XR5) | **Take**: L27 s2 narrowed to what the body carries; L447 points to primitive 2; L514's "Besides the two primitives" kept | erratum → CLAIM | the front matter becomes true; O12's SILENT gets its rule | L27 s2–s3 carry 04's O40 ruling. Guards: O12, O21, O27, O40, O50 | 1 |
| W7 indices against declared inputs; Derivation 6's proof (XR6) | **Take**: one sentence separates indices from declared inputs; L33 and L512 read "derived from these, the declared indices and the declared inputs"; the dependence order lists the declared inputs, Ownership, ProducedBy, and boundary and continuity; Derivation 6's proof cites the fuller order | erratum → CLAIM | the proof covers its claim; 03 §8 items 2, 3 and 5 closed | none on cases. Guards: O37, O49 | 1 |
| W8 L63 short form of attack (D) | **Take**: add "where the population admits a differing survivor" | erratum → ORDER | one qualification everywhere | none | 1 |
| W9 "the bell and the tide" (XR4) | **Take**: drop the parenthesis at L275 and keep its rule | erratum → WORDING | no case content inside the theory | a vivid example. Guard: O2 | 1 |
| W10 Derivation 10's glosses | **Take (a)** (XR7): drop L616's "Derivation 3's qualification seen from the other side …". **(b)** is replaced by W19's edit to Derivation 10; the check shows "cite (K)" would not deliver the sentence | erratum → CLAIM (removes M59) | exact pointers | none | 1 |
| W11 "a table … is an account" | **Take**: at L271, "is not excluded by (F1), and is an account when it meets the other conditions of (E)"; L528 s3 changed in step; S70's deference of the front matter to Part V kept | clarification → CLAIM (narrowed) | no Account granted unchecked; L271's clash with S2 and L275 on O2 removed | loses file 11's crisp closure of the lookup-table question. Guards: O2, O33, O7; N17 is watched | 3 |
| W12 boundary | **Take in form (a′)**, 04's wording: a boundary is stated when the situation names the system and places a process inside or outside it. This is a rule for what counts as stating the input, not a default | clarification → CLAIM | closes the O30 and O17 hazard that test (b) turned on | could be read as a default. Guards: O51 (the declared boundary excludes the module), O41, O3, O14, O18, O21, O31 | 3 |
| W13 the two halves of Ownership | **Take**: one clause saying credit for content and ownership of a process are different attributions; drop "today" from L419 to match L465 (03 §8 item 9) | clarification → CLAIM | stops the O30 and O40 misreadings | none. Guards: O30, O40, O41, O50 | 3 |
| W14 "mostly" | **Take the weak form only**: a weighting of several contributions to one achievement is a declared input the semantics does not supply, and a claim that needs one is unsettled. No premise that credit goes with the originative act | clarification → CLAIM | O21, O27 and O50 get their stated rule | no row moves toward. Guards: O21, O27, O50 (SILENT), O40 (AGREE) | 3 |
| W15 a missing input is not a refutation | **Take**: one Part XV sentence, limited to the inputs Part XIV lists (the form of 12:554) | clarification → CLAIM | SILENT rows are not read as defeats | could shelter the theory; limited to the list | 3 |
| W16 Derivation 3's refutable content | **Leave**: no case needs it, and widening the refuter again risks O48. Recorded as a known weakness in results. D3-T tests W17 instead | — | — | the (D) limb stays close to analytic | — |
| W17 "survives on H" | **Take**, with 03 §8 item 1: a transport survives on H when it is a member of \(\mathcal T\) that meets the survival condition on H; one wording of population membership at L473 and L562 | clarification → CLAIM | Derivation 3's claim and proof match by definition | file 10's unconditional reading is dropped openly. Guards: O48, O24, O11, D3-T | 2 |
| W18 whose knowledge a population fixes | **Leave**: no usable case (N14 is set aside); it complicates Sel; it is the first candidate for revision 3 once N14 is rewritten and agreed | — | — | the robot question stays unstatable | — |
| W19 Derivation 2 | **Take, pending S88**: wording (i) or (ii) (1.3.3); the kinds-across-candidates sentence after (K); Derivation 10 restated | change of claim → CLAIM | Part XV no longer lists a false result | the slogan "indistinguishable is identical" goes, and the Consequence narrows. Guards: O46 (decisive), O45, O36, O24, O10; N25 and N17 watched | 2 |
| W20 non-circular dependence, Γ | **Take, pending S88**: option B with the deletion reading, or A (1.3.4) | change of claim → CLAIM | a well-typed condition; O33, O5 and O7 secured on the text | the logical form changes. Guards: O2, O4, O5, O7, O33, O36, the skew-symmetric case, Part VII's production case; N1, N3, N25 | 2 |
| W21 \(\equiv_\ell\) | **Take**: \(d\equiv_\ell c\) when transports from d to c and from c to d are both faithful on c's contract at grain \(\ell\); restore the first sentence of 00:746 only; written independently of Derivation 2 (conflict 7) | new definition → CLAIM | New and Origin become checkable | the reacquisition sentences of 00:746 stay out. Guards: O3, O11, O15, O18, O27, O31; N4, N15, N21 | 2 |
| W22 \(\mathcal E_c\) and \(p_\delta\) | **Take**: restore 00:620; gloss \(p_\delta\) as "the question whether z has \(\delta\) in respect of p"; "represents how it bears" becomes "represents its alleged connection" | erratum → CLAIM (minor) | (K1) is typed | none; no case touches it | 1 |
| W23 \(\Delta\), Result, ProducesVia | **Take**: \(\Delta\) typed as a subhistory with its content changes; Result(\(\Delta\)) as the contents at \(\xi'\) that \(\Delta\) prepared; 00:839's ProducesVia restored | definitions → CLAIM | (P) and (EK) can be evaluated | guard: O13 (Ana's account produced nothing) | 3 |
| W24 \(S_a\), \(T_a\), generator | **Take**: restore 00:518 before functional transport. It must land before W31, whose S and T refer to it | erratum → WORDING | a readable theorem | none | 1 |
| W25 Admit, Cap, grades, Poss, Enable | **Take**: restore 00:1015–1031 (one sentence each); define Enable in the Barriers paragraph's own terms | erratum and definition → CLAIM | Parts XII and XIII become readable | none; N24 | 1 |
| W26 tag (I3) missing | **Take**: renumber (I4) as (I3) | erratum → WORDING | tidy | record pointers to (I4) go stale | 1 |
| W27 attack labels collide with equation tags | **Take**: rename the attacks Attack 1–5 in Part 0 and Part XV and update every pointer (L63, L337, L528–536); the record gives the old→new map | erratum → WORDING | no collision for a reader of the theory | the record's "attack (D)" needs the map | 1 |
| W28 route against active route | **Take**: a Part VI route is a support of the candidate, a Part IX active route is a subnetwork of actual occurrences, and the two meet in ProducedBy; L309 s3's first clause kept | clarification → CLAIM | fewer mistaken splits | must not undo M28. Guards: O45, O19, O39, O52, O25, O20 | 3 |
| W29 proxy measure | **Leave**: O4 is AGREE on L129 and L153 (04); a tight wording risks O6, O7 and O9. Take it up if this round shows O4 split | — | — | O4 rests on existing sentences | — |
| W30 set-point as a state | **Take**: whether a difference is a state or a relation is fixed by how the organization is written, and an edit acting alike on both components cannot separate them | clarification → CLAIM | the O10 hazard in shared text | guards: O10, O22 | 3 |
| W31 (T2) | **Take**: the three hypotheses restored (A and C); the general bound B pending S88 (1.3.2) | erratum (A, C) → CLAIM (narrowed); B generalizes | removes the one literal counterexample; with B, R2 J's second clause is closed | none; N20 weakly | 2 |
| W32 scope | **Take (b)**, merged with W57. **Leave (c)**, the Part VI "loose limit" measure | clarification → CLAIM | the books and the skill agree in words; O5 secured | O1 stays SILENT. Guards: N7, O8, O33 | 3 |
| W33 idle parts | **Take**: "(E) is fidelity: a commitment that does no work passes (E), and (B) reports it as critical in no support; how hard an account is to vary is a separate measure and grades nothing" | clarification → CLAIM | the (E)/(B) split stated; the departure from D p.25 goes in the sources note | none while it is not a condition. Guards: O36, O45, O47; N1, N25, N2 | 4 |
| W34 reach | **Take**: in Part VI, the reach of E is the set of jobs f with Account(E, f), fixed by E and the world, not by which jobs anyone has checked. Chosen over restoring 00:383 | definition → CLAIM | the lemma's key word gets a meaning; D p.29 becomes statable | none; N4, N5 | 4 |
| W35 surprise and "problem" | **Take (b′)**: expectation and violation defined for any transport; surprise kept for selected transports and said so; "recognized difficulty" defined as a represented failure of a claimed obligation, or a represented conflict between a claimed and a protected obligation (Part XI) | clarification → CLAIM | Deutsch's "problem" gets a home; N18 and N19 become reachable; Derivations 4 and 10 untouched | "surprise" stays narrower than ordinary use. Guards: O3, O12, O27 | 4 |
| W36 two senses of "explanation" | **Take**: one sentence after Part I's Fallibility commitment; no global change of capitals; the commitment sentence itself unchanged | clarification → CLAIM | removes a misreading. Tests: O15, N2, N3 | none | 4 |
| W37 "blind" | **Take**: restore "blind" at L15, with "no represented target" | erratum → WORDING (M2) | eases the clash of vocabulary | guard: O11; N11 | 1 |
| W38 attribution | **Take**: a sources-and-departures note (2.5), withheld from tests | meta | lineage, and honesty about departures | readers may hold the theory to the books | 5 |
| W39 same-form regress | **Take**: restore 00:210's sentence "Identity of that assertion is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical truths" into S2. Its counterfactual-law sentence is **not** restored (conflict 14) | clarification → CLAIM | same-form regress caught at the grain | guards: O2, O4; N25, N3 | 2 |
| W40 eliminative explanation | **Take**: "why does X appear?" is a separate question with its own contract, and a bare denial is not an account of it | clarification → CLAIM | a sharper attack (B); N22 | none; N8, N25 watched | 4 |
| W41 inexplicit representation | **Take, with a relay guard**: restore the first two paragraphs of 00:855–861 after Build, and add: a witness may identify a binding by its use (reason use, Part IX); a carrier that delivers content it does not use that way has relayed it, and relay is not construction | clarification → CLAIM | tacit construction becomes reachable (N21) | the witness is harder to check. Guards: N13 (the parrot stays a carrier), O14, N12 | 4 |
| W42 error correction | **Leave** until W31 is in and N20 has been run | — | — | — | — |
| W43 knowledge as self-preserving information | **Leave**, with the reason in the sources note: it is outside the class, and adding it would put Derivation 6 at risk | — | — | N9 and N10 are not reached | — |
| W44 level of explanation | **Leave**: indices and L279 already say it, and a predicate on grain would break "indices, not primitives" | — | — | N16 and N17 read on existing text | — |
| W45 interoperability | **Take**: Part I's substrate independence is stated relative to the interoperability of the adopted physics; a physics without it has barriers in Part XIII's sense | change of claim (narrowed commitment) → CLAIM | N24 becomes reachable; M p.95 | none on O-cases | 4 |
| W46 realized edits (12:491, 12:77) | **Leave**: 12:77, and 12:491's sentence excluding every unrealized edit, clash with formal edits (grievance 7; the skew-symmetric case). Settle with conflict 14 in revision 3 | — | — | O22's "together" rests on existing text (AGREE in 04) | — |
| W47–W50 file 12's causal claims | **Leave**: file 12 is under no round, and a claim change is earned by a case | — | — | N23 and N8 are read on existing text | — |
| W51 S79 unfinished | **Process**: kept separate; the (T2) change is never fed into S79's sealed comparison | — | — | — | — |
| W52 N-cases | **Process**: adopted in the round (3.3) | — | — | — | — |
| W53 D3-T | **Process**: its verdict is fixed by the N-case method; it becomes O76 if the authors agree (3.3) | — | — | — | — |
| W54 FW5 richness; W55 the 32 unrecovered rows | **Leave**: recorded in "Not tested" | — | — | — | — |
| W56 O38 | **Settled** by 04 (AGREE in both files) | — | — | — | — |
| **W57** (new, 04 §7.10) L161 s3 | **Take**: after "supplies no rule that certifies it", add: where the claim states the ground of its restriction, the verdict is given with that ground; where it states none, the ground is a missing declared input (Part XIV) | clarification → CLAIM | closes the O5 hazard that test (b) turned on | guards: O1 (stays SILENT), O5, O8; N7 | 3 |
| **W58** (new, 03 §8 items 10 and 11) | **Take**: at L301, "the supports assessed are subsets of the written Γ, not a support someone could write in its place"; at L33 s4, "appears anywhere" becomes "is defined or presupposed (Derivation 6)" | clarification → WORDING or CLAIM | two readings closed | guard: O36 | 3 |

**Count.** 39 items taken: 36 with text changes and 3 as meta (W1, W3, W38). 14 left out (W2, W4, W16, W18, W29, W32(c), W42, W43, W44, W46, W47–W50). Six process items (W51–W56). The record will have about 45–55 entries against file 11, because some items touch several places.

### 1.3 The items the brief requires, in detail

#### 1.3.1 The seven cross-reference errata (04 §7.5; 03 §5)

| id | F11 line | the fix in revision 2 | item |
|---|---|---|---|
| XR1 | L5 | The note is replaced (2.5). The new record lists all four places of the Derivation 3 cluster that the note missed (L197, L225, L473, L616), and treats attack point (D) and the Part XV entry as one passage (L534). | W1 |
| XR2 | L5 | The new note names no case, no record file and no round. The build asserts this. | W1 |
| XR3 | L27 | L27 s2 becomes: "Where a claim needs one of these, the semantics does not supply it and marks the place: a claim of worth takes the normative relation as an input (Parts XI, XIV), and a claim that needs any of the others is unsettled (Part XIV)." L27 s3 is kept. | W6 |
| XR4 | L275 | Drop "(the bell does not explain the tide)". | W9 |
| XR5 | L447 | "takes a **normative relation** \(\mathcal N\) as a declared input" becomes "takes the **normative relation** \(\mathcal N\) (primitive 2, Part XIV) as an input". | W6 |
| XR6 | L588 | The dependence order at L518 lists the declared inputs and the definitions that rest on them (Ownership L419, ProducedBy L433, boundary and continuity L465). Derivation 6's proof cites that order. | W7 |
| XR7 | L616 | Drop the clause "and this is Derivation 3's qualification seen from the other side, a population that admits no survivor at the new change". Keep "the fidelity failure is structural, not parametric". | W10(a) |

NEW-XR1 (L620, "(Derivation 2)"), which 03 ruled CORRECT (loose), is handled by W19's restatement of Derivation 10's sentence.

#### 1.3.2 (T2): the restored hypotheses (W31)

- **Recommended wording** (options A and C; the S88 brief's repair). It restores 00:570 and 00:572 and makes 00:578 explicit:

  > **Approximate transport.** With one-step discrepancy \(d(\pi Sz,T\pi z)\le\varepsilon\) at every state \(z\) of the stated scope and an \(L\)-Lipschitz represented next-step map \(T\), the discrepancy after \(n\) steps from one state, \(e_n=d(\pi S^nz,T^n\pi z)\) (so \(e_0=0\)), satisfies \(e_n\le\varepsilon\sum_{k<n}L^k\). (T2) Without a modulus, no accumulated bound follows. An exact question is not silently replaced by an approximate one.

- **Optional addition (option B, the general bound):** "With an initial discrepancy \(e_0\), \(e_n\le L^ne_0+\varepsilon\sum_{k<n}L^k\), both runs staying within the stated scope." It is a new claim (a generalization), checked by proof and by script, and tight. It closes R2 J's second clause ("retain its propagated contribution") and S78 item 10.
- **Prerequisite.** W24 must land first, so that S and T refer to the restored \(S_a\) and \(T_a\).
- **Rule on S88** (fixed now, before any S88 reply is read):
  - A and C are taken unless the S88 reading rules one of the three hypotheses false or excessive.
  - B is added only if neither S88 reading finds a flaw in it. Otherwise it waits.
  - If F2 is WITHDRAWN (the defence's reading M is ruled to be stated by the text), A and C are still taken as errata: they restore what FW5 stated and lose nothing.
- **Cosmetic, left alone.** L also names the component relations \(L_j\) and the shadow length. Renaming it is not worth the notation change.

#### 1.3.3 Derivation 2: the candidate wordings (W19), pending S88

- **Wording (i), recommended**, the "Same anchors, one account" of the S88 brief. It replaces F11 L552–558:

  > **2. Same anchors, one account.** **Claim.** Let \(\mathcal E,\mathcal E'\) be candidates for the same \(p\) that both satisfy (F1), (F2) and (A) on \(C\). (i) Their answer profiles coincide on \(C\). (ii) If a bijection \(\varphi\) of their active components satisfies \(\lambda'(\varphi(k))=\lambda(k)\) for every \(k\), up to port translation, then \(k\) and \(\varphi(k)\) are of one kind on \(C\) for every \(k\), and the two are one account on \(C\). *Proof.* (i) By (A), \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)=\operatorname{Ans}_{E'}(\tau'(a),\sigma'(b))\) for every \((a,b)\in C\). (ii) By Derivation 1, \(k\) has the signature of \(\lambda(k)\), and \(\varphi(k)\) the signature of \(\lambda'(\varphi(k))=\lambda(k)\); composing the two port translations gives a footprint bijection under which the two signatures, read on \(C\), coincide. ∎ Without the premise of (ii) nothing more follows: candidates that anchor different subnetworks, or cut \(D\) at different places, are different candidates with one answer profile (Derivation 9; Part VI, redundant routes). A coarsening is not a recoding (Derivation 8). **Consequence.** Where two faithful candidates differ only in which component carries which anchor, the contract does not contain the distinction; a claim that one assignment is "really" right is a claim that some admitted change separates them, and must supply it. The remedy is a finer contract, which is a new question.

- **Wording (ii), the smaller fallback:**

  > Two candidates \(\mathcal E,\mathcal E'\) for the same \(p\) that both satisfy (F1), (F2) and (A) on \(C\) have one answer profile on \(C\); and a component of \(E\) and a component of \(E'\) anchored to one subnetwork of \(D\), up to port translation, are of one kind on \(C\), their signatures read through \(\tau\) and \(\tau'\).

- **Supporting edits, taken with either wording:**
  - After (K) at F11 L121: "A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivations 1 and 2 use kinds in this sense."
  - Derivation 10 at F11 L620: "the two persistence components are of one kind (Derivation 2)" becomes "exchanging the two persistence components' anchors gives a second faithful transport, and the two transports are one account (Derivation 2)".
- **Why (i) and not (ii).** Derivation 10's restated sentence needs (i)'s "one account". The premise is "the same subnetworks" rather than "anchors of one kind", because the weaker premise would identify O45's two springs, and O46's spring and cable, against Part VI's redundant routes and against M28.
- **Rule on S88:**
  - F1 UPHELD: take (i).
  - F1 NARROWED, with (i)'s premise or its "one account" conclusion ruled defective and (ii) surviving: take (ii). Derivation 10's sentence then reads "the two transports have one answer profile, and each persistence component is of one kind with the component that takes its anchor".
  - F1 WITHDRAWN: take only the sentence after (K), and record the reason.

#### 1.3.4 Non-circular dependence: typing Γ (W20), options A and B

**Option B, recommended.** S3 at F11 L257 becomes (the S88 brief's wording):

> "There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer profile at \((a,b)\) differs from its value at \((1,b_0)\), or is not determined there in the claimed way, and in \(E|(\Gamma\setminus G)\), with the named background fixed, that difference is lost or the answer ceases to be determined."

- **Rider proposed here, not yet examined by S88.** Read the restriction as deletion under (O), so that Account takes no new declared input:
  - replace "in \(E|(\Gamma\setminus G)\), with the named background fixed" with "in \(E\) with the components of \(G\) deleted (Part II: a deleted component imposes the full relation on its ports)";
  - at F11 L233, add "\(\Gamma\) is a set of components of \(E\): those the candidate offers as doing the work".
  - **Why.** Part VI's \(E|W\) rests on "a declared restriction operation" and a "named background". Written into (E), those would make every Account relative to a further declared operation, a new input on the core definition (see W7). Deletion under (O) is the canonical restriction the text already has.
  - The draft cross-examination (X1) must test the rider.
- **What B gains.**
  - The witnessing contrast stays in \(C\), so non-vacuity's last sentence stays true.
  - The dependence lands on Γ without making input settings into commitments.
  - An idle block can never witness. That derives half of F11 L275 and agrees with W33.
  - O33, O5 and O7, Part VII's production case, and the skew-symmetric case hold.
  - N25 fails S3, since no admitted change alters its answer.
- **What B loses.**
  - The logical form of a defining clause changes, which is a change of claim.
  - The dependence order must list (O)'s deletion rule for (E), or, without the rider, the restriction operation.

**Option A, the fallback.**
- S3 becomes: "There exists \((a,b)\in C\) whose translation \((\tau(a),\sigma(b))\) removes or replaces a nonempty block of \(\Gamma\), with \(\sigma(b)\) keeping the rest of the baseline \(\sigma(b_0)\), under which the answer profile changes or ceases to be determined in the claimed way."
- At F11 L233, add: "The commitments \(\Gamma\) are components and boundary values of \(E\), including the components that assign the inputs the candidate commits to; since an edit that sets a port replaces the component assigning it (Part II), an intervention in \(C\) on such an input removes or replaces a block of \(\Gamma\)."
- **What A gains.** It is closest to an erratum.
- **What A loses.** Input settings become commitments that sit in every support and are reported critical in every support (noise in (B)); "commitment" loses 00:165's sense.

**Kept under either option.**
- S2 unchanged, plus W39's identity sentence.
- F11 L275's rule without its parenthesis (W9).
- 00:210's counterfactual-law sentence is **not** restored. It would clash with non-vacuity's "declared subset of the physically admitted edits" (conflict 14). The skew-symmetric case holds under B without it.

**Rule on S88.**
- F3 UPHELD: take B, with the rider unless X1 finds that the rider breaks a worked case.
- F3 NARROWED against B, for example B breaks the skew-symmetric case, O33, O5, O7 or Part VII while A keeps them: take A.
- Both options break something: take only the \(\tau,\sigma\) erratum. Every reading concedes it as a drafting fault. It reads "whose translation \((\tau(a),\sigma(b))\) removes or replaces …", with Γ left untyped and recorded as open.

#### 1.3.5 Declaring every CLAIM place file 11 did not declare (W1, W3)

The revision record (2.5) has two layers.
- **Layer 1: revision 2 against file 11.** Every change, with its old text, its new text, its kind, its expected ruling and the claim it changes.
- **Layer 2: file 11 against file 10, as file 11's note should have said.**
  - The 42 undeclared places from 03's master table: 41 inside the theory (40 distinct changes, with M5 counted with M47) and M7.
  - Each is given by Part and heading, file-10 line and file-11 line, with one line saying what a reader can now conclude.
  - Layer 2 includes the four places of the Derivation 3 cluster (M19, M21, M46, M59; M59's clause is removed by XR7's fix), the sentences behind O18, O37 and O41, and M28.
  - No M-number, case or record is named in the theory. S81 Results holds the map from each entry to its M-number.

#### 1.3.6 Attribution of the sources (W38): a note, not claims

A short "Sources and departures" section, placed after the revision note. It is part of the authority file and is cut from every test brief (2.5). It contains:

- **Sources, in the owner's words (decision S19).** Marletto, *The Science of Can and Can't* (2021), and Deutsch, *The Beginning of Infinity* (2011). The physical module's task wording comes from constructor theory (the 2013 *Synthese* paper, cited by file 00 as [R2]). The FW5 predecessor is file 00.
- **Close parallels, named without claiming derivation.** Derivation 9, declared provenance, relay against reconstruction, and reason use (Deutsch, chapters 7 and 16).
- **Deliberate departures:**
  - "explanation" as a candidate that may be false (W36);
  - an idle commitment passes (E), where Deutsch counts superfluous features as bad (W33);
  - a stated limit need not be explained (W32);
  - "selection" means blind selection only (W37);
  - "surprise" is narrower than "problem" (W35);
  - "every acquisition is creation" is rejected (00:1304–1306);
  - knowledge as self-preserving information is left out, with the reason (W43);
  - universality and objective aesthetics are abstained from (Part XIII; worth).
- **Page numbers.** Each is checked against the books by the writer before freezing, or else given by chapter. Book quotations are at most 25 words.
- **What it does not do.** It asserts nothing about what follows from the books. The third source the owner named in S19 is not cited: it was named for exploration, not as a source.

#### 1.3.7 The source items ranked highest by the verification

| Rank | Item | Recommendation | Reason |
|---|---|---|---|
| 1 | Scope (obs 6; W32) | **Take (b)**, joined with W57. **Leave (c).** | (b) says in words that (E) on a scoped contract certifies no limit, and gives a claim that states its ground its verdict. (c), a Part VI measure of loose limits, would make "what makes a restriction appropriate" partly derived, against L514 (conflict 3). S29's failed A-prime shows how easily the shape goes wrong. Its one target row, O1, has a verdict Claude fixed. Waiting loses nothing: O1 stays honestly SILENT. |
| 2 | Idle parts and reach (obs 2, M7; W33, W34) | **Take both, as clarifications.** Leave hard-to-vary as a condition. | They state the (E)/(B) split N1 shows. Making it a condition would bring back grading and flip N7 and O8. |
| 3 | Surprise, "problem" and Repair (obs 13, M2; W35) | **Take (b′).** Leave file 12's (c). | (b′) keeps Derivations 4 and 10 whole. (c) would rewrite "learning versus creating". |
| 4 | Reach undefined (obs 5; W34) | **Take**, defined from Part VI. | No new primitive; D p.29's "determined by the content" becomes a definition. |
| 5 | Attribution plus the population point (obs 1, 3, 10, M3; W38, W18) | **Take W38 as a note. Leave W18.** | The note is free. W18 has no usable case until N14 is rewritten, and it would complicate Sel beside W17. |

### 1.4 Left out, and what is lost by leaving each

W2 applies only on a file-10 base. W4 and W14's strong form would each need a default input or a weighting, so O35, O21, O27 and O50 stay SILENT. W16 is left, so Derivation 3's defeat limb stays close to analytic. W18 is left, so the robot question stays open. W29 is left, so O4 rests on existing sentences. W32(c) is left, so O1 stays SILENT. W42 is left, so error correction has no lemma yet. W43 is left, so N9 and N10 are not reached. W44 is left, so N16 and N17 read on existing text. W46–W50 are left, so file 12's causal patterns stay in file 12 until it has a round.

### 1.5 Order of work, by dependency

0. **Before writing.** S81 Results final, after the S87 cross-examination and the supplementary audit. S88 read under its rule, and the three rules in 1.3 applied. Every decision in section 4 made.
1. **Errata, stage 1.** W24, then W31. W26, W27, W22, W25, W37, W8, W9, W10(a). Then W6 and W7, which change L27, L33, L447, L512–518 and Derivation 6's proof.
2. **Repairs the defeat list exposes, stage 2.** W19 and the sentence after (K), then Derivation 10. Then W21, written after W19 and independently of it. Then W20 with W39. Then W17.
3. **File 11's verdict-bearing text, stage 3.**
   - W57 with W32(b), at L161.
   - W12 with W13, at L419 and L465.
   - W14, W6's L514 wording and W15, at L514 and Part XV.
   - W5, W11 (L271 and L528), W28, W30, W23, W58.
4. **Source-derived clarifications, stage 4.** W33 and W34 in Part VI; W35 in Parts IV and X; W36 and W45 in Part I; W40 in Part VII; W41 in Part X.
5. **Meta, stage 5.** The record's layer 1 is written from the applied changes and layer 2 from 03's table. Then the note, then the sources note.

Stages 3 and 4 touch the same Parts as stage 2 only at Part V and Part VI, so their paragraphs are assigned to one drafter each (2.4). **A cap on iteration:** an item from stage 3 or 4 that fails its check twice is dropped from revision 2 and listed for revision 3, not reworked a third time.

---

## 2. Method for writing it

### 2.1 Who does what

- **Claude subagents do all the analysis and building** (decision S17). At most five run at a time.
- **The orchestrator** only delegates, interprets and decides (decisions S13 and S17).
- **Atria and Mimo cross-examine**, at medium effort, with at most three calls in flight each, across every process.

| Role | Claude subagents | Reads | Writes |
|---|---|---|---|
| Drafter A (stages 1 and 2: Parts 0, IV (Selected), V, VI, VII, VIII, XV, XVI) | 1 | file 11, the frozen scope list, the worklist items, the checks, the S88 readings, file 00 at the cited lines | change-specification entries |
| Drafter B (stages 3 and 4: Parts I, II, III, IV (expectation), IX, X, XI, XII, XIII, XIV) | 1 | the same | change-specification entries |
| Builder | 1 | the change specification, file 11 | the draft, by program; the diff map |
| Checkers 1 and 2, independent | 2 | file 11, the draft, the specification, the worklist items | a ruling per entry |
| Reconciler | 1 | both checks | rulings where they differ |
| Unlisted-change hunter | 1 | file 11 and the draft only | a 1D-style list |
| Record writer | 1 | 03's master table, the applied changes | the record's layers 1 and 2; the note; the sources note |
| X1 and X2 reader (a fresh determiner) | 1–2 | the replies, under the rule written before sending | rulings |

### 2.2 The base, and what changes if S81 falls

- **A. S81 stands** (the expected case). The base is file 11 (md5 5e494c1095d920d128b9a79de378f923). The round's control arm is file 11, the authority. The baseline for O1–O52 is S81's ruled file-11 marks.
- **B. S81 falls on test (b) alone.** This happens if the S87 cross-examination or the supplementary audit turns O5, O30, O17 or another row into a theory change away that traces to a new sentence of file 11.
  - File 10 stays the authority.
  - The base is **still file 11's text**, because its other 40 undeclared changes were found harmless and its coherence gains stand.
  - The sentences behind the failing rows are repaired in revision 2. Those are exactly W57 and W12(a′), already in scope.
  - The record's layer 2 is then the whole list of changes against the authority.
  - The round's control arm becomes file 10, and the baseline is S81's ruled file-10 marks, with the S75 corrections.
  - The predictions add: O48 and O45 toward, the failing rows restored to AGREE, nothing else.
- **C. S81 falls on (a), (c) or (d).** For example, O48 is not AGREE under file 11, or a sentence of file 11 is ruled wrong where file 10's was right.
  - The base becomes **file 10**, with imports from file 11 only where a case earned them. That is the Derivation 3 cluster, all ten places (W2), unless (a) failed.
  - The worklist's file-10 variants then apply: W3 imports, W4(c) and W5 on endpoints.
  - Revision 2 shrinks to errata, the Part XV repairs and those imports.
  - The file number and method are unchanged.

### 2.3 The file number and names

- **The file: `authority/13 Claude Fable Semantics - standalone theory, revision 2.md`.**
  - The authority folder keeps its own sequence: 00 is the predecessor; 10 the original; 11 revision 1; 12 the causality draft. 20 is the set-aside file the owner never supplied (decision S4); it is taken by name though absent.
  - 13 is the next free number in the 1x line. It says nothing that 20 would, since 20 was the other model's "revised" theory.
  - LEGEND's log-number rule has not governed this folder since file 10 (file 11 was made at S76, file 12 at S77), and every plan names authority files as 10, 11 and 12. So an "S89 …" authority name would break the one sequence readers use.
- **The log entry** under which it is made takes the next number across all three projects' logs at the time of writing (lesson S5). Today that would be **S89**: S87 and S88 are used, and the highest outside Semantics is L86. The round keeps that number in its file names ("S89 Plan …", "S89 Case book …").
- **Status.** File 11 stays frozen. File 13 is the candidate until its round decides.

### 2.4 Patch, not rewrite

File 11 was made as a full rewrite for coherence, and its note missed 41 CLAIM places. Revision 2 is made the opposite way.

1. **The change specification is written first**, as a file of entries. Each entry gives: an id (R2-01, …); its item (W-number); the Part, heading and F11 line; the exact old text, which must occur once in file 11; the exact new text; its kind; its expected ruling; and "what a reader can now conclude that file 11 left open", with no case id.
2. **Each paragraph belongs to one drafter.** The program refuses two entries whose old texts overlap.
3. **The builder applies the specification to file 11 by program.** The draft is file 11 with those replacements and nothing else. The program asserts two things:
   - every line not touched by an entry is byte for byte file 11's line;
   - every diff hunk maps to exactly one entry.
   
   Lesson 26 applies: the program is tested on a planted unlisted edit (the catch) and on a clean draft (the neighbour) before use.
4. **The meta blocks are added last**, between marker lines so the build can cut them exactly: the note after the title, the sources note after it, and the record as a final section.

### 2.5 The note, the sources note and the record

- **The note** is one paragraph, as it stands at the head of the file. It says:
  - "Revision 2 (file 13), <date>. File 11 with the changes listed in the revision record at the end of this document, and no other."
  - "Each change is given with its old and new text, the reason it is made (erratum, clarification or change of claim), and whether a reader can conclude from it something file 11 left unconcluded. Every change of the last kind is declared as a change of claim: N of the M changes."
  - "The record also lists every change in claim that file 11 made against file 10 and that file 11's own note did not declare."
  - "Nothing else differs."
  
  It names no case, no record file, no round and no model.
- **The sources note** is 1.3.6.
- **The record** has layer 1 and layer 2 (1.3.5), and the old→new map of the attack labels (W27).
- **None of the three travels in a test brief.** The build cuts them between their markers, checks the md5 of what remains, and asserts that no brief carries "revision", "file 13", "record", "Deutsch", "Marletto" or any record file name. That is S81's withholding of L5, done by construction.
- **Verdict movements** are reported in the round's Results, never in the theory.

### 2.6 Independent checks before freezing

1. **By program.** The diff map (2.4), the old texts' uniqueness, the tag and label inventory (every tag of file 11 present, with (I4) renamed to (I3)), and a search for dangling pointers ("Derivation n", "Part X", bracketed labels).
2. **Two independent Claude checkers**, each blind to the other (lesson S2). For every entry each answers:
   - (a) does the new text do what its worklist item and the scope list say;
   - (b) does it claim anything beyond its entry;
   - (c) are its kind and expected ruling right under 03's definitions;
   - (d) does it break another sentence? This is lesson 50: the whole of the draft is searched for the qualifications of the claim touched, and each is quoted;
   - (e) on its guard rows, does the checker's own reading of the case keep the mark?
   
   Each entry gets HOLDS, FIX or DROP.
3. **A Claude reconciler** rules where the checkers differ. The drafters fix the entries marked FIX once. An entry still failing is dropped under 1.5's cap.
4. **An unlisted-change hunter.** A fresh Claude subagent is given file 11 and the draft without the record, and makes a 1D-style list of every difference in claim. Every CLAIM place it finds outside the record is either declared (added to the record) or removed. This is the pre-freeze test of "declare every change".
5. **Guard rows by hand.** A Claude subagent works the guard rows named in 1.2 under the draft, and O2, O5, O33 and the skew-symmetric case for W20. Any flip goes back to its entry.

### 2.7 Cross-examination by Atria and Mimo, before freezing

- **X1: the draft revision.** One call each to Atria and Mimo, at medium effort. Mimo's max_tokens is 131,072 and Atria's 65,536; one pass; accepted only when the call finishes "stop" with END OF REPORT on the last line.
  - **Size.** Revision 2 whole, with line numbers (about 10,800 words); the record's layer 1 with old and new text (about 3,000); tasks (about 1,500). **About 16,000 words**, against a ceiling of 28,000. Mimo's 2b audit of tester A failed at 36,690 words at both efforts; Mimo on tester B succeeded at 37,701, at medium. So about 37,000 words is the edge, and 28,000 is the working limit.
  - **Tasks.**
    1. For each entry: does it fix what it says, and does it break anything? Name each case or derivation it breaks, quoting the text. The line for each entry reads HOLDS, BREAKS, OVERREACHES or UNCLEAR.
    2. Hunt counterexamples to the revised Derivation 2, (T2) and non-circular dependence, under their stated assumptions, with concrete instances, in S88's task-3 form. Test the deletion rider in particular.
    3. Name any place where the entry's old text and new text differ in claim beyond what the entry declares.
    4. Close with one line: FREEZE AS IS, FREEZE WITH CHANGES, or DO NOT FREEZE.
  - **Form.** The brief names no model. The author is "the author", and the auditors are unnamed. It is searched for negative wording (lesson 27). Before any claim is named as a target, the draft is searched for that claim's qualifications and they are quoted (lesson 50).
- **X2: the round plan.** The same settings. The brief holds section 3 as frozen, the instruction parts of the Stage 1 and Stage 2 briefs, and the case-book format, in **about 12,000 words**. It asks for what would make the result wrong, biased or unreadable, and closes with RUN AS IS, RUN WITH CHANGES or DO NOT RUN. This is the S80 precedent: its plan cross-examination caught what Claude's checks missed (lesson S6).
- **The reading rule, written and committed before either brief is sent,** in the form of 04's file 05:
  - A reply is evidence, not a result.
  - A failed call supports nothing.
  - The two replies are read independently.
  - Every BREAKS, OVERREACHES, counterexample or design defect is re-read from the texts by a fresh Claude determiner. The determiner states Claude's position first, then the reply's argument, then rules.
  - Every change it causes is recorded, with the fact that it came after the cross-examination.
- **Changes and the freeze.** A change caused by X1 goes through the diff map and the two checkers again, for the changed entries only. A change that adds a new change of claim gets a small X1′ on that change alone. Then **revision 2 is frozen**: its md5 is recorded, it is committed as file 13, and it is never edited again. A later change is a new file.
- **No other Atria or Mimo call is in flight** from any process while X1 or X2 run. The shared slot lock (`s80_common.provider_slot`) enforces this. S87 and S88 must be finished first (lesson S10; process-audit finding 1).

---

## 3. The test round: S89, revision 2 against every case

*The plan in S81's house style. It becomes "S89 Plan - revision 2 against every case" in `tests/` when frozen. The prediction, the baseline, the parts and the standing rule live in the plan and the build tool only.*

### 3.1 What this round is

- Revision 2 (file 13), the candidate, is tested against every case: the 52 of S81 and the adopted new cases. Testing and then audit, as decision S7 requires. File 11, the authority, is the control arm.
- Claude reads both stages and determines the result (decision S13).
- It carries forward the S78 group A repairs as S81 applied them, and S81's third-version changes f (rulings from the texts before any return is opened) and g (cross-examination of the determination).
- It applies part of S78 group C (3.3).
- The testers are Claude subagents (decisions S16, S17). The auditors are Atria and Mimo at medium effort (decision S17).

### 3.2 The texts

| Text | Source | As sent |
|---|---|---|
| Revision 2 | `authority/13 …revision 2.md` (md5 at freeze) | The note, the sources note and the record cut between their markers; the md5 of the rest recorded. About 10,800 words. |
| File 11 | `authority/11 …revision 1.md` (md5 5e494c1095d920d128b9a79de378f923) | Line 5 and the blank line after it withheld, as in S81. 9,487 words. |
| The case book | `tests/S89 Case book - the 75 cases, situations, questions and fixed verdicts, as the tested agent sees them.md` (md5 at freeze) | O1–O52 byte for byte from S81's book (md5 4f488d149e44669240d5db546c8e946a, entries only). O53 onward as in 3.3. |
| Provenance | `tests/S89 Case book - provenance.md` | Never sent. |
| Briefs | S81's instruction parts, carried with only the changes listed in 3.6 | Lifted between markers; checked by program. |

### 3.3 The cases

- **O1–O52.** S81's cases, unchanged.
- **The new cases, adopted from the candidates N1–N25 as O53–O75** (applying S78 group C in part). Their verdicts were fixed by Claude authors who never read the theory, in three rounds. None was BOOK-DEPENDENT.

| O | N | Title | Why adopted |
|---|---|---|---|
| O53 | N1 | The seasons and the sun god | Agreed in round 1; held in round 3. Tests W33, W20, W36. |
| O54 | N2 | The myth amended | Agreed in round 1; held in round 3. The historical index; W36. |
| O55 | N3 | A myth about winter | Agreed in round 1; held in round 2. W36, W39, W20. |
| O56 | N4 | The tilt and the midnight sun | Agreed in round 2. W34, W21. |
| O57 | N5 | A farmer's rule carried south | Agreed in round 1. A Derivation 3 control. |
| O58 | N7 | Two bakers | Agreed in round 1. The guard for W32 and W57. |
| O59 | N8 | The machine that runs forever | Agreed in round 1; held in round 3. Barriers; W40. |
| O60 | N9 | Dark moths | Agreed in round 2. A left-out item (W43). |
| O61 | N10 | The burned notebook | Agreed in round 1. (EK) indexed to an event; W23. |
| O62 | N11 | Two students, ten drafts each | Agreed in round 1. W37, W12. |
| O63 | N12 | Consent by rephrasing | Agreed in round 1. A positive control. |
| O64 | N13 | The parrot in the lecture hall | Agreed in round 1; held in round 2. The guard for W41. |
| O65 | N15 | The miscopied notes | Agreed in round 1; held in round 3. W21, W12. |
| O66 | N16 | The domino that never falls | Agreed in round 1; held in round 2. S2; W44 is left out. |
| O67 | N17 | The transistor at the end of the run | Agreed in round 2. W19, W11; W44 is left out. |
| O68 | N18 | Two footbridges on opening day | Agreed in round 2. W35. |
| O69 | N19 | The novelist's two demands | Agreed in round 1; held in round 3. W35, W5. |
| O70 | N20 | Keeping count with string | Agreed in round 1; held in round 2. W31; W42 is left out. |
| O71 | N21 | The order of adjectives | Agreed in round 2. W41, W21. |
| O72 | N22 | Denying the inner experience | Agreed in round 2. W40. |
| O73 | N23 | The planets tonight and a thousand years ago | Agreed in round 1; held in round 2. Direction. |
| O74 | N24 | Two sealed sorts of matter | Agreed in round 1; held in round 2. W45, W25. |
| O75 | N25 | What holds the universe up | Agreed in round 1; held in round 2. W19, W20, W33, W39. |
| O76 | D3-T | The controller that failed yesterday | Only if its verdict is re-fixed (below). Tests W17. |

- **Set aside.**
  - **N14**, which is SET ASIDE in the candidates file.
  - **N6.** Round 3's second author rated its Leon half "low to medium". Under the rule rounds 1 and 2 used ("medium-low counts as low"), that makes N6 disputed. It is set aside by the rule as written, as N14 was. Its only item, W32(c), is left out anyway.
  - Both wait for a rewrite and a fresh judgement.
- **D3-T** (W53). Its situation and its first verdict were written by the S72 auditor, who had read the theory.
  - Two fresh Claude authors who have never read the theory fix its verdict from the situation. The question is written once: "Does the discarded design show that what survives the testing is undecided at the untried setting?"
  - They follow the N-case rules: agreement in substance, and neither rating low.
  - If they agree before the freeze, it enters as O76. If not, it goes to "Not tested".
- **The format.** Each new case is entered as:
  - `## O53 - <title>`;
  - `**Situation.**` word for word;
  - `**Question.**` or `**Questions.**` word for word;
  - `**Thoughtful person's verdict.**`: the candidate's "Verdict" section, word for word, except for sentences that only report the authors' process (who said what, "(R2 A1)", "Both round-1 authors said the same …"). Each cut is listed verbatim in the provenance file, and a Claude checker confirms that no finding was cut.
  
  Confidence and open notes go to the provenance file only. The book's opening paragraph becomes: "Seventy-five cases, O1 to O75 … Where a case states a question, its verdict answers that question." The difference in form marks the new block, so the cases are not "mixed unmarked" (see Not tested).
- **Provenance.** For each new case the provenance file gives:
  - its N-id and source file;
  - its status and rounds;
  - every author's confidence, and its open notes;
  - the cuts;
  - the "specialist knowledge" notes;
  - the sketch's aim, from `sketches - why each was chosen.md` (now Part 2 of `tests/S89 Case book - candidate cases, provenance.md`), which travels in no brief.
- **Commit the sources first.** The candidate files live only in this session's scratchpad. Before adoption they are committed into `Semantics/results/` as the record the provenance file cites: the final candidates, the reconciliation, every author's return in rounds 1–3, the prompts and the sketches. The worklist, the checks and the source verification are committed too. The book texts are not committed.
- **Who wrote what (recorded, not hidden).**
  - The sketches were chosen by a reader of the theory and the books.
  - The verdicts were fixed by Claude authors who read neither.
  - The worklist used the candidates to choose items, so **these cases are not held out from the revision** (section 4, R3).

### 3.4 The frozen prediction

**The baseline.**
- **O1–O52:** S81's ruled file-11 marks as they stand in S81 Results after the cross-examination. Today that is AGREE on 46 and SILENT on O1, O12, O21, O27, O35 and O50. Any change S81 Results makes is copied here before the freeze.
- **O53–O76:** no baseline. Their file-11 marks are ruled in this round.

**The predictions.**

- **P1: nothing moves among the old cases.** Under revision 2, Claude's ruled mark on each of O1–O52 equals the baseline: 46 AGREE, the same six SILENT on the same points, and no DISAGREE, SPLIT or CASE DISPUTED. This includes the guard rows O2, O5, O7, O10, O13, O17, O24, O30, O33, O36, O38, O41, O45, O46, O48 and O51.
- **P2: the new cases.**
  - **(a) None moves away.**
  - **(b) The aimed set is AGREE under revision 2.** The aimed set is O53 (N1), O55 (N3), O56 (N4), O65 (N15), O68 (N18), O69 (N19), O71 (N21), O72 (N22), O74 (N24), O75 (N25), and O76 if it is adopted. Wherever file 11's ruled mark there is not AGREE, the row is a theory change toward the thoughtful person, and it traces to a record entry.
  - **(c) The guards are AGREE under both texts:** O58 (N7), O63 (N12) and O64 (N13).
  - **(d) Nothing else changes.** On O54, O57, O59, O60, O61, O62, O66, O70 and O73, the two ruled marks are equal and on the same point.
  - **O67 (N17) carries no mark prediction.** W19 bears on its "each tells the asker something the other does not" and W44, which is left out, on its "only in a thin sense", so its mark may change point without changing direction. It is reported.
- **P3: the record is complete and right.** The CLAIM places Claude rules between file 11 and revision 2, after both 1D lists and both 2D audits, are exactly the record's entries with expected ruling CLAIM. Every entry expected WORDING or ORDER is ruled so. No other place is CLAIM.
- **P4: the repairs the defeat list exposes hold.** No reader produces a counterexample that Claude rules valid to the revised Derivation 2, (T2) or the revised non-circular dependence, under their stated assumptions. The readers are the testers' "Noticed" sections, the auditors, X1 and the S88 readings.

**One expectation, about the readers and not about the theory.**
- **E1: the hazards are fixed.** On O5, O10, O17 and O30, the number of the two testers' 1C readings (revision 2) that are not AGREE is lower than the number of their 1K readings (file 11) that are not AGREE, in this round. It is reported with its counts.

### 3.5 The words Claude rules with, fixed before the data

- **Marks.** S81's five marks and their order, carried word for word: CASE DISPUTED, DISAGREE, SPLIT, SILENT, AGREE. Also carried: "Point", "Same finding", SILENT with a recorded search.
- **The revision-2 mark:** Claude's ruling from revision 2's text, informed by both 1C returns and every 2b part.
- **The file-11 mark:**
  - O1–O52: the baseline, unless both 1K returns agree on a different mark and Claude's own reading of file 11 confirms it. Then the baseline is corrected, and the correction is recorded with its row.
  - O53–O76: Claude's ruling from file 11's text, informed by both 1K returns and by the 2a-K readings, if run.
- **Verdict, passage, direction, theory change and reader variation:** S81's definitions, with file 11 in the place of file 10.
- **CASE DISPUTED on a new case is not ruled by the determiner,** because its verdict is out of the determiner's hands. The disputed point goes to two fresh Claude authors who never read the theory, under the N-case rules. If either changes the verdict or rates it low, the case is set aside from every count and named. It is never rewritten mid-round. On O1–O52, CASE DISPUTED is ruled as in S81.

### 3.6 What is run

**The parts,** fixed now so that every outside brief stays under about 28,000 words:

| Part | Rows | Count |
|---|---|---|
| P1 | O1–O18 | 18 |
| P2 | O19–O36 | 18 |
| P3 | O37–O52 | 16 |
| P4 | O53–O64 | 12 |
| P5 | O65–O76 | 11 or 12 |

**Stage 1: Claude subagents,** each fresh, each in a fresh folder outside the repository holding only `brief.md`. The prompt, prep, contamination check and collector are S81's. The collector's reader label is corrected (S81 change k), and the hand-back tool passes (change l). The void words are tested on the real texts and a real transcript before the run (lesson S9); they include "S89", "S81", "revision", "file 13" and "N1"–"N25".

| Agent | Tester | Call | Brief | Approximate words |
|---|---|---|---|---|
| A1, B1 | A, B | 1C, first half | 1C instruction + revision 2 + O1–O52 | 17,000 |
| A2, B2 | A, B | 1C, second half | 1C instruction + revision 2 + O53–O76 | 21,500 |
| A3, B3 | A, B | 1K, first half | the same instruction + file 11 + O1–O52 | 15,500 |
| A4, B4 | A, B | 1K, second half | the same + file 11 + O53–O76 | 20,000 |
| A5, B5 | A, B | 1D | 1D instruction ("Text B is a revision of Text A") + file 11 as A + revision 2 as B | 21,000 |

- **Why halves.** 75 or 76 cases in one return would be about 17,000 words. The halves keep each return near S81's size and match the audit parts. Each arm was already a separate agent, so nothing is lost within a tester.
- **The instruction changes.** "fifty-two" becomes the counts; "O1 to O52" becomes the half's range; the 1D wording changes as above. Nothing else changes.

**Stage 2: Atria and Mimo, at medium effort.**
- Settings: thinking on; temperature 0.7; Mimo's max_tokens 131,072 and Atria's 65,536 on every rung; up to six attempts; one further pass only for a failed call.
- Accepted only when the call finishes "stop" with END OF REPORT.
- Sent by `tools/s87_run.py`, which holds the cross-process slot lock and refuses to start while another runner lives. At most three in flight per provider.

| Call | Per | What it holds | Approximate words | Calls |
|---|---|---|---|---|
| 2a, the blind reading | auditor × part | brief 2a + revision 2 + the part's situations and questions, verdicts withheld | 13,000–15,000 | 10 |
| 2a-K, the blind reading of file 11 on the new cases (recommended; cuttable) | auditor × P4, P5 | brief 2a + file 11 + the part's situations and questions | 13,000 | 4 |
| 2b, the open audit, fully crossed | auditor × tester × part | brief 2b + revision 2 + the part's cases + that tester's 1C records for the part + the auditor's own 2a records for the part | 20,000–24,000 | 20 |
| 2D, the difference audit | auditor × two halves of the Parts (0–VIII, IX–XVI) | brief 2D + revision 2 whole + file 11's text of every changed paragraph, aligned by the build + both 1D lists' records for the half | 19,000–22,000 | 4 |

- **No sampling.** Each 2b part audits every row in it in full. In S81 the rules M1–M6 left only 3 and 2 rows to draw, so each sample was every row (third version, change i). The stopping rule and 2W are dropped.
- **2D is split** because revision 2, file 11 and two lists together would pass 28,000 words. The build certifies that every paragraph it does not reprint from file 11 is byte for byte in revision 2.
- **The build** (`tools/s89_build.py`, from `s81_build.py`) asserts:
  - no brief carries the plan, the prediction, the note, the sources note, the record, a round or file number, "revision", an N-id, or any provenance text;
  - no Stage 1 or 2a brief carries a verdict line;
  - every outside brief is at most 28,000 words;
  - every source md5 is as frozen.
  
  It prints every negative word in every brief (lesson 27). Its guards raise errors rather than using `assert` (process-audit finding 12).
- **The pilot** (lessons S7 and S11; process-audit finding 9). Before any counted call, one call per provider is sent at the counted size and effort, and it counts for nothing. The pilot text is a 2b part built from S81's own texts (file 11, O1–O18, tester B's S81 1C records and Mimo's S81 2a records), so it shares nothing with this round's data. If either provider does not finish within its ceiling, the parts are cut to 12 rows before any counted call, and this plan records the change as a third version.
- **Stage 2 starts after Stage 1 is collected.** 2a may run beside Stage 1, since it shares nothing with it. 2b follows 2a.

### 3.7 How Claude determines the result

1. **Receipts.** As in S81. Stage 1 is collected with the contamination check. Every Stage 2 call has its receipt, the model as served, and its hashes. A failed call is kept, run once more, and then recorded MISSING.
2. **Rulings from the texts, before any return is opened** (lesson S2; S81 change f). These are written as soon as the round is frozen and committed before `table` is built; the commit order is the proof.
   - Two independent Claude readers each rule all 76 cases under both texts, in three ranges each.
   - A reconciler rules where the readers differ.
   - Two difference readers rule every place where file 11 and revision 2 differ, against the record, and a reconciler rules between them.
3. **The table, by program.** 1K and 1C per tester; the 2a blind marks; each 2b part's YOUR MARK, ON VERDICT, ON MARK and BLIND MARK; the effort of each column (all medium); MISSING wherever a call failed. Every quotation is checked VERBATIM, LOOSE or ABSENT against its text.
4. **Step 3: the rows, ruled from the texts.** At most four Claude determiners, one per group of rows, then two verifiers, one on the texts and one on the rules. The rows ruled are:
   - every row where any reading differs from the pre-ruling or from the baseline;
   - every row named by P1, P2 or E1;
   - every CASE DISPUTED;
   - every row named under "Disagreements … left unmarked" or "Wrong, and uncorrected …";
   - every row with an ABSENT quotation;
   - every row where both testers' 1C marks are AGREE and an auditor's blind mark is not.
5. **Step 4: the differences.** Every CLAIM place on either 1D list, and every surviving or missed difference in either 2D part, ruled CLAIM, WORDING or ORDER and matched to the record (P3).
6. **CASE DISPUTED on the new cases:** under 3.5.
7. **The repairs the defeat list exposes (P4).** Every counterexample claim from any source is checked by a Claude verifier, by script where it is mathematical, as the checks were.
8. **The assembly.** P1–P4 and E1 scored; tests (a)–(e); the standing verdict; "Not tested".
9. **Cross-examination of the determination** by Atria and Mimo at medium effort, as S87 did.
   - The brief is at most 28,000 words: revision 2 whole, file 11's changed paragraphs, the rules word for word, and only the pressed rows with their cases, the rulings and the contrary readings. It is not the whole case book.
   - Its reading rule is written and committed before sending.
10. **Results** (`results/S89 Results - …md`), the log entry, Status. If revision 2 stands, the authority folder's read-me and the project read-me are updated.

### 3.8 What counts as revision 2 standing as the authority

- **(a) The repairs hold.** P4 holds, and the guard rows of W19 and W20 keep their marks: O46, O45, O36 and O24; O2, O5, O7 and O33.
- **(b) No case shows a theory change away** from the thoughtful person, file 11 → revision 2, on O1–O76.
- **(c) No sentence of revision 2 is ruled to give a wrong verdict** on a case where file 11's corresponding sentence gave the thoughtful person's.
- **(d) No cross-reference in revision 2 is ruled to point wrong** in a way that changes what a sentence claims. A slip is recorded as an erratum.
- **(e) No undeclared CLAIM place is shown harmful by a case.** An undeclared place that no case shows harmful is a finding against the record, recorded in Results.

**Three clauses:**
1. (a)–(e) hold, and P1, P2 and P3 hold: revision 2 stands as written, and its record is confirmed.
2. (a)–(e) hold, and P1, P2 or P3 fail only by theory changes toward the thoughtful person, or by undeclared CLAIM places that no case shows harmful: revision 2 stands, with those findings recorded against its record in Results.
3. Any of (a)–(e) fails: file 11 (or the authority of 2.2 B or C) remains. Results lists what a revision 3 would have to repair.

### 3.9 The lessons carried

| Lesson | How it is carried |
|---|---|
| S2: prediction out of every pack; second reader before first; rule before data | The prediction lives in this plan and the build only, and is asserted absent. The rulings from the texts are committed before `table`. Every reading rule is committed before its calls are sent. A rule adopted after the data is recorded as adopted then. |
| S7 and S11, with process-audit finding 9: pilot at full size and effort; a setting changes everywhere at once | The pilot in 3.6. The ceilings and the effort are set in one place (`s80_common`), used by every job. |
| S8: a deadline on the whole call | `s80_call`'s stream deadline and idle timeout, unchanged. |
| S9: test the contamination rule on real texts | The void words are tested on the real briefs and a real transcript before the run. |
| S10, with process-audit finding 1: one runner per provider, or a shared lock | `s87_run.py` with the flock slots. No round call while S87, S88 or any supplementary call lives. |
| S5: numbering | The log number is read from all three logs when the entry is written. |
| 26: test the catch and its innocent neighbour | Applied to the diff map, the build's assertions and the collector. |
| 27: negative wording to the outside models | The build prints every negative word; zero at freeze, apart from the mark values. |
| 35: a zero gauge may mean the pass is too easy | Agreement is reported as agreement, never as a confirmation. E1 is reported with its counts. |
| 49, 50: the theory's own distinction; search for qualifications | X1, X2 and the determination brief quote a claim's qualifications before naming it as a target. |
| S1 and S4: script before commit in the chain; never amend after an unread result | Unchanged practice. |
| S81 third version: a change after the freeze is a new version file | Any change after the first call is a "third version" of this plan, with (i) to (iv) as S81 wrote them. |

### 3.10 Run order

1. Freeze revision 2 (2.7), the case book and provenance, and this plan (after X2). Commit them.
2. `s89_build.py build`: every text, with hashes, word counts, assertions and the negative-word printout. Then the pilot.
3. The rulings from the texts (3.7 step 2) begin, alongside the Stage 1 agents: ten agents in two waves, within the cap of five.
4. Collect Stage 1. Run 2a (and 2a-K). Then `build2` and run 2b and 2D.
5. Commit the rulings from the texts. Then `table`.
6. Steps 3–8 of 3.7. Then the cross-examination of the determination, then Results, the log and Status.

### 3.11 Not tested

**Carried from S81:**
- Whether the fixed verdicts of O1–O52 are right. They are Claude's. CASE DISPUTED is the only channel against them.
- R2's first 32 Stage B rows (unrecovered) and the R2 file.
- FW5's richness beyond the lines used.
- File 12.
- Any reader armed with the audit workflow (file 24).
- The Stage 1 settings, which are the harness's.
- What the harness shows a subagent beyond its prompt.
- Whether a reader with a file and tools reads as it would from one prompt.
- Whether the pattern can fail a wrong theory. That is S79's question, and its return is still awaited.

**New with this round:**
- **The new cases are not held out.** The worklist chose items with them, and the drafters see them as the worklist cites them. The round tests whether the changes do what they were chosen to do, not whether the revision generalizes. A held-out block for revision 3 is the remedy.
- **The new cases' authors are Claude**, one family, though they never read the theory. S78 group C's "an agent that has never read file 10" is met. Its wish that cases come from outside the family is not met. The cases are not mixed unmarked: the question line marks them.
- **N6 and N14 are set aside.** D3-T is set aside too, unless it is adopted.
- **One model family throughout the Claude side:** the author of the theory, the revision, the checks, the testers and the determiner.
- **Splitting.** The audits are split into parts, so no auditor sees cross-row work. Each 2a part is read without the other parts' cases.
- **All outside calls run at medium effort.** There is no effort confound between columns this time, and no high-effort comparison.
- **The left-out items (1.4):** their questions stay open, and the rows that turn on them are expected not to change.
- **(T2) has no case.** N20 bears on it only weakly. P4 rests on argument and script.
- **Conflict 14** (physical against formal edits) stays unresolved.

---

## 4. Risks and conflicts: the choices to make before writing

**The worklist's thirteen conflicts, and one more.**

| # | Conflict | Must it be decided before writing? | Recommendation |
|---|---|---|---|
| 1 | Default inputs (W4(b), W12(a)) against L514 and L465 | Yes | **Neither default.** W4 left. W12 taken as (a′), 04's rule for what counts as stating a boundary, which is not a default. |
| 2 | Weighting (W14(b)) against O21, O27 and W48 | Yes | **W14's weak form**: a weighting is an unsupplied declared input, and a claim needing one is unsettled. No premise that credit goes with origin. |
| 3 | Scope (W32(c)) against appropriateness as a declared input; S29; N7 | Yes | **(b) only**, joined with W57. (c) left for a later revision with cases of its own. |
| 4 | Surprise: (b) against (c) | Yes | **(b′)**: expectation and violation for any transport, surprise for selected ones, recognized difficulty defined. |
| 5 | Tables (W11) against S70's fix | In drafting | W11 is taken, and the front matter still defers to Part V. L528 is changed in step. |
| 6 | The Derivation 3 family (W16, W17, W18) | Yes | **W17 only**, with one notion of population membership. W16 and W18 are left. |
| 7 | Derivation 2 and \(\equiv_\ell\) | Yes (order) | W19 first. W21 is defined by faithful transports both ways, never through Derivation 2. Guards O11, N15 and O18. |
| 8 | Non-circular dependence: keep S2, L275's rule, and 00:210's contrasts | Yes, after S88 | **B with the deletion rider**, under 1.3.4's rule. Keep S2 and L275's rule. Restore 00:210's identity sentence, not its counterfactual-law sentence. |
| 9 | File 12 removes provenance | Yes | Import only 12:554's pattern (W15). W46 is left (conflict 14). No other import. |
| 10 | W36 rewords Part I | In drafting | **Add a sentence**; leave the commitment sentence as it is. |
| 11 | Inexplicit witnesses (W41) against "relay is not" | In drafting | Take W41 with the relay guard. N13 and O14 are guards. |
| 12 | Idle parts (W33) against D p.25, and against W32 read as a condition | Yes | A clarification, never a condition. The departure goes in the sources note. |
| 13 | The occasions sentence on a file-10 base | Only in branch 2.2 C | W4(c) and W5 on endpoints, as the worklist says. |
| 14 (new) | Non-vacuity's "physically admitted edits" against formal edits (grievance 7; the skew-symmetric case; 00:210's counterfactual contrasts; 12:77; 12:491) | Yes: do not widen it | **Touch none of it in revision 2.** Leave W46; leave 00:210's counterfactual sentence out. Record it for revision 3. |

**Other risks.**
- **R1. S81 falls at the cross-examination.** 2.2 gives the branch, and the scope already holds the likely repairs (W57, W12(a′)). Nothing is drafted until S81 Results is final.
- **R2. S88 narrows or withdraws a finding.** 1.3.2–1.3.4 fix, before its replies are read, what follows from each ruling.
- **R3. The new cases are not held out** (3.11). Mitigations:
  - the drafters write each change from its item's reason and the text, never from a case's verdict wording;
  - the checkers flag any entry whose wording echoes a verdict;
  - "Not tested" says so.
- **R4. Scope size.** About 39 items and about 50 entries makes attributing any moved verdict harder. Every entry is small and local, the rulings from the texts trace each row to an entry, and 1.5's cap drops a failing stage-3 or stage-4 item rather than iterating. A leaner revision (stages 1–3 only, with stage 4 moved to revision 3) is a fallback if X1 marks more than a few stage-4 entries BREAKS.
- **R5. The ceilings.** The parts and the pilot guard against these. A failed part supports nothing and is recorded MISSING, as in S81.
- **R6. Atria disconnects under three-way load** (process audit). Shorter parts make them less likely, and each call is allowed one further pass.
- **R7. The scratchpad is lost.** The worklist, the checks, the verification and the candidate cases are committed into `Semantics/` before any of them is cited (3.3).
- **R8. S79 is still open.** "Nothing else changes" rests on a pattern whose power to catch a wrong theory is untested. Stated in "Not tested", not solved here.

**The decisions to make before writing starts.**
- **D1.** The base, once S81 Results is final: 2.2 A, B or C.
- **D2.** The three S88 outcomes, applied by the rules in 1.3.2–1.3.4. That fixes the wordings of W31 (with or without B), W19 ((i), (ii) or the (K) sentence only) and W20 (B with the rider, A, or the erratum only).
- **D3.** The four choices of conflicts 1–4: no default inputs; W14's weak form; scope (b) with W57; surprise (b′).
- **D4.** The Derivation 3 family: W17 only.
- **D5.** File 12: only 12:554's pattern. W46 is left, under conflict 14.
- **D6.** The note's form: a patch with a change specification; an in-file record in two layers, listing all 42 of file 11's undeclared places; a sources note; all withheld from tests; every CLAIM-expected change declared as a change of claim.
- **D7.** File number 13, and the log number read from all three logs (expected S89).
- **D8.** The cases: 23 new cases as O53–O75; N6 and N14 set aside; D3-T through the N-case method as O76 if it is agreed.
- **D9.** The attack labels renamed (W27), with the map in the record.
- **D10.** Commit the working files from the scratchpad as records first.
- **D11.** Whether to run the recommended 2a-K calls and the X2 cross-examination of the plan, or the lean variant (section 5).

---

## 5. Time and call budget

Estimates from S81's measured times:
- Mimo 2b calls at about 37,000 words took 2,800–3,200 s. At about 20,000–24,000 words, 25–45 minutes is expected.
- Atria takes 15–30 minutes, with occasional 1,800 s disconnects.
- A Claude subagent tester or reader takes 30–60 minutes.
- At most five Claude subagents run at once, and at most three calls per provider.

| Phase | Claude subagent runs | Outside calls (Atria + Mimo) | Elapsed, approximately |
|---|---|---|---|
| 0. Wait for S81 Results and the S88 readings; decisions D1–D11 | 2–3 (S88 readers, under their rule) | — | depends on S87 and S88 |
| Commit the working files; case book; D3-T verdict | 4–5 (builder, cut checker, two D3-T authors, reconciler) | — | 1–1.5 h, alongside drafting |
| Drafting, the diff map, checks, hunter, record | 8–9 | — | 3–4 h |
| X1 and X2, reading, fixes, freeze | 2–3 | 4 | 2–2.5 h |
| Build and pilot | 1 | 2 | 1.5–2 h |
| Stage 1, and the rulings from the texts | 10 + 10 | — | 3–4 h (four waves of five) |
| Stage 2 | — | 10 (2a) + 4 (2a-K) + 20 (2b) + 4 (2D) = 38; about 45 with reruns | 6–7 h (Mimo is the bottleneck: about 19 of its calls in about seven rounds of three) |
| Determination (steps 3–8) | 10–12 | — | 3–4 h |
| Cross-examination of the determination; Results; log | 2–3 | 2 | 2 h |
| **Total** | **about 50–55** | **about 46 counted, about 52 with reruns** | **about 22–26 h elapsed** once S81 and S88 are settled |

**The lean variant** (D11):
- drop X2 and the 2a-K calls;
- un-cross 2b, so each auditor audits one tester (10 calls);
- keep everything else.

That is about 28 outside calls and about 15–17 hours.

What the lean variant loses:
- a design check before the run; S80's own plan cross-examination caught what Claude's checks missed;
- any outside-family reading of file 11 on the new cases, whose direction then rests on Claude alone;
- the separation of auditor from run that S81 crossed for.

**The recommendation is the full design.** The new cases are the round's new evidence. Their file-11 side is the half that nothing else covers.

---

## Summary

**The scope list** (take or leave, one line each):
- W1 note → take: a new note and a two-layer record.
- W2 → leave (file-10 base only).
- W3 and M28 → take, declare only.
- W4 O35 default → leave.
- W5 (P) and occasions → take.
- W6 \(\mathcal N\) and L27 (XR3, XR5) → take.
- W7 indices, inputs, Derivation 6 (XR6) → take.
- W8 L63 → take.
- W9 bell and tide (XR4) → take.
- W10(a) L616 gloss (XR7) → take; W10(b) → replaced by W19's edit.
- W11 the encoding table → take.
- W12 boundary → take as (a′).
- W13 Ownership halves and "today" → take.
- W14 "mostly" → take the weak form.
- W15 missing input is not a refutation → take.
- W16 → leave.
- W17 "survives on H" → take.
- W18 population provenance → leave.
- W19 Derivation 2 → take ((i); (ii) the fallback; pending S88).
- W20 Γ → take (B with the deletion rider; A the fallback; pending S88).
- W21 \(\equiv_\ell\) → take.
- W22 \(\mathcal E_c\) → take.
- W23 \(\Delta\), Result, ProducesVia → take.
- W24 \(S_a\), \(T_a\) → take.
- W25 Admit, Cap, Poss, Enable → take.
- W26 (I3) → take (renumber).
- W27 attack labels → take.
- W28 routes → take.
- W29 proxy → leave.
- W30 state against kind → take.
- W31 (T2) → take (A and C; B pending S88).
- W32 scope → take (b); leave (c).
- W33 idle parts → take.
- W34 reach → take.
- W35 surprise → take (b′).
- W36 "explanation" → take.
- W37 "blind" → take.
- W38 attribution → take, as a note.
- W39 identity at the grain → take.
- W40 eliminative explanation → take.
- W41 inexplicit representation → take, with the relay guard.
- W42 → leave. W43 → leave. W44 → leave.
- W45 interoperability → take.
- W46 → leave (conflict 14). W47–W50 → leave.
- W51–W56: process. S79 kept separate; the new cases adopted; D3-T via the N-case method; W54 and W55 recorded; W56 settled.
- W57 L161's ground of a restriction → take.
- W58 "supports actually written" and "appears anywhere" → take.

**The recommended file number:** `authority/13 Claude Fable Semantics - standalone theory, revision 2.md`, made under the next log entry (expected S89).

**The test round in ten lines:**
1. Revision 2 against 75 or 76 cases, with file 11 as the control arm and revision 2 frozen by md5 first.
2. The cases: O1–O52 unchanged, plus 23 new cases as O53–O75 (all but N6 and N14), and D3-T as O76 if two fresh authors agree on its verdict.
3. The prediction is frozen in the plan only: nothing moves among O1–O52; ten aimed new cases are AGREE; three guards are AGREE in both texts; the rest are unchanged; none moves away; the record is complete; the repairs hold.
4. Stage 1: ten Claude subagents (two testers × 1C and 1K in halves, plus 1D), each in a fresh folder, with the contamination check.
5. Stage 2: Atria and Mimo at medium effort, in five fixed parts of 11–18 rows, every brief at most 28,000 words, fully crossed. That is 2a (10), 2a-K (4), 2b (20) and 2D (4).
6. A pilot per provider at full size before any counted call; one runner and the shared slot lock.
7. Claude's rulings of every case and difference from the texts, committed before the table is built.
8. Steps 3 and 4 by Claude determiners and verifiers. CASE DISPUTED on a new case goes back to fresh authors, not the determiner.
9. Revision 2 stands on (a) the repairs hold, (b) nothing moves away, (c) no wrong sentence, (d) no claim-changing pointer, (e) no harmful undeclared change, with S81's three clauses.
10. Atria and Mimo cross-examine the determination (at most 28,000 words), then Results, with "Not tested" (the new cases are not held out; one model family; S79 still open).

**The decisions to make before writing starts:**
- D1: the base, after S81 Results.
- D2: the three S88 outcomes, and so the wordings of (T2), Derivation 2 and Γ.
- D3: no default inputs; "mostly" in its weak form; scope (b) with W57; surprise (b′).
- D4: W17 only in the Derivation 3 family.
- D5: file 12, 12:554's pattern only; W46 left.
- D6: patch discipline and the two-layer record, withheld from tests.
- D7: file 13 and the log number.
- D8: the case set, with N6 set aside and D3-T's route.
- D9: the attack labels renamed.
- D10: commit the working files first.
- D11: the full or lean Stage 2 and the X2 cross-examination of the plan.
