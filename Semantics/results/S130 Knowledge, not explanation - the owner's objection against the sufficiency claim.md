# S130 Knowledge, not explanation: the owner's objection against the sufficiency claim

*Log S130, 2 October 2026, decision S85. One Opus 5.5 agent doing the whole job (S56, S68; no subagent or workflow). Writing only: no Avida run, no experiment, no outside model, no GLM check (S70); no book file opened and no book quoted. **Nothing in the theory changes**: text 107, the formal core, claims and program after round 4, every S108 to S129 file, the decisions file, the S61 terms and `authority/` were read and not written; every change below is a PROPOSAL for the owner. The semantics is cited from `tests/107 The semantics, standing alone, after round 4.md` by line ("L536"); the formal core and claims (`results/S107 Round 4 - maths after the reading/`) by id; S129's copies and data by their files. The one script, `tools/s130_quote_the_not_program_encoding.py`, only reads S129's feeding script and data and prints them.*

**The owner's words (S85)**, said after plain file 129 told the owner that under Reading C the evolved NOT program "counts as a narrow explanation of NOT": "Oh I don't know about explanation. It seems like it counts as knowledge, not explanation. Which is the part we are currently at. Knowledge evolved through natural selection is case closed. And knowledge created is mostly. Actually, can we experiment with created knowledge again. But this time beyond just math?"

**Words used here.** The owner's words are *evolved knowledge* and *created knowledge*. The theory's words for the two histories are *selected* (variation and survival, with nothing in the history aiming at the target; L195, D12.1) and *constructed* (worked out in an episode with the target held; L197, D12.2); a third, *declared*, is a link someone simply wrote in (L199, D12.3). They are introduced here once; below, "selected" and "constructed" are used only where the theory's own definitions are meant.

## 0. In short

- **(a) Does MC1 meet (E) on a contract of its question? Yes, strictly, and only in a narrow way.** Taken as one block, the NOT program meets all four conditions of (E) (F1, F2, (A), Dependence, Non-vacuity; D6.7, D6.8) on the question S117 wrote for it: target the NOT task with one input bit and one output bit, a contract of exactly two pairs (input 0, input 1) with **no admitted edit** but the identity, the query reading the output. Its transport is selected at the S72 boundary under Reading C with the graded survival condition, so it is not declared. Cut into its instructions it fails (F1). The question is **held by nobody inside the boundary**: not the program (no represented target, S117, S123, S125), not the execution environment (no rivals offered, and rivals are not a selection population, L315; its checker represents nothing at the S72 boundary, I200), and not the people, who are outside it. The contract **equals the selection history** (H = C), so nothing in it was unseen. (E) asks none of these things.
- **"Narrow explanation" was the theory's verdict, through its conjecture, not a theorem and not an over-reading of (E).** The formal core keeps "explanation" an undefined atom (D16.XV: "Expl(ℰ): an atom, no definition uses it"); what calls MC1 an explanation is the sufficiency conjecture (Suff) at L17, L61, L536, read with ¬Dec(t). S117's map and S129's results applied it correctly; their wording over-read it in four places (section 5).
- **So the owner's objection is of the shape (Suff) names** (section 3): an argument not using (E) that rules out "MC1 is an explanation", for a candidate that meets (E) with a transport that is not declared. S127's table and S129's computation (MC1, "(Suff) defeated at L536: True" at the S72 boundary) had already said that an assessor holding this premise holds an argument against (Suff). The theory does not already agree with the owner (section 3.1). For the owner, while the argument stays usable, (Suff) as written is ruled out at the S72 boundary.
- **PROPOSAL (section 4): reserve "explanation" for constructed provenance.** Formally, in D16.XV and (Suff): Account(ℰ) ∧ Con(t) in place of Account(ℰ) ∧ ¬Dec(t); the owner's S41 condition widened from "declared, so not an explanation" to "not constructed, so not an explanation". In words, two terms, one already in the text: **representation** (R), a faithful correspondence with a selected or constructed history, is what the owner calls knowledge (evolved knowledge where selected, created knowledge where constructed); **explanation** is reserved for an account whose transport was constructed. (E) itself is untouched and still takes no provenance (FC30).
- **What it changes**: L17, L49, L61, L69, L536, Argument 6 at L47, D16.XV, FC30.new1's parts (a) and (c), S127's tables and S129's map wording (not its counts), and what the theory says of adaptations in nature (evolved knowledge, never explanations). **What counts against it**: S41 Q2 as S108 read it (C16), Grievance 7 on mathematics found by search, the reach of selected correspondences, and the breadth of "constructed" (it reaches learning from labels, S128), each in section 4.4.
- **The owner's choice, in one sentence** (section 6): keep "explanation" for what was worked out, so the evolved NOT program is evolved knowledge that passes the test and not an explanation; or keep the theory as it is, so it is a narrow and bad explanation, and "knowledge, not explanation" stays your argument against the theory's central claim.

## 1. What is checked, on what record

The question put (decision S85, Claude's reading): whether MC1, the evolved NOT program, meets all four conditions of (E) on a contract of *its question*, strictly, as S117's map and S129's feeding encoded it; whether "narrow explanation" was the theory's verdict or an over-reading; and then either the correction (if it does not meet (E)) or the proposal (if it does).

Read for it: text 107 (Part 0 L11 to L61, Part III, Part IV L191 to L225, Part V, Part VI L315 to L317, Parts X, XI, XIV, XV, Argument 6 at L594 and the grievance at L47); the formal core (D6.5 to D6.8, D10.1, D12.1 to D12.5, D13.1 to D13.8, D14.1 to D14.7, D16.XV); the claims FC23.new2, FC30, FC30.new1, FC90, FC90.new1, FC12.new1 to FC12.new3, FC77, FC78, FC80, FC83; S117's results and both maps; S125's corrections (row 16) and check 04; S127's hinge; S128's learning-rule derivation (i); S129's results, the feeding script `tools/s129_feed_avida_cases_to_the_copy_under_reading_c.py` and its data `results/S129 Reading C carried into copies/map feeding under Reading C.json`; decisions S41, S44, S45, S57, S59, S60, S72, S83, S84, S85.

## 2. MC1 against (E), strictly

### 2.1 The encoding, quoted

From S129's feeding script (lines 55 to 67, and line 129), unchanged from S117's (printed by `tools/s130_quote_the_not_program_encoding.py`):

```
  59      D = org('D_task(NOT)', ['x', 'y'], {'x': bit, 'y': bit}, ['c_x', 'c_task'], {'c_x': ('x',), 'c_task': ('x', 'y')},
  60              B, [ONE], lambda j, a, b: {(uval[b],)} if j == 'c_x' else {(x, 1 - x) for x in bit})
  61      C = [(ONE, 'u0'), (ONE, 'u1')]
  62      p = Question(D, C, 'u0', PortQuery(), 'y', name='p_task')
  63      nand = lambda u, v: 1 - (u & v)
  64      E1 = org('E_program(one block)', ['x', 'y'], {'x': bit, 'y': bit}, ['e_x', 'e_prog'], {'e_x': ('x',), 'e_prog': ('x', 'y')},
  65               B, [ONE], lambda j, a, b: {(uval[b],)} if j == 'e_x' else {(x, nand(x, x)) for x in bit})
  66      c1 = Candidate(E1, p, ident(['x', 'y']), {ONE: ONE}, {b: b for b in B},
  67                     {'e_prog': (frozenset(['c_task']), ident(['x', 'y']))}, ['e_prog'], 'y', name='program')
 129  H = [(ONE, 'u0'), (ONE, 'u1')]
```

Read in the theory's terms (Part III, L131 to L147; Part V, L231):

| Piece | MC1 | Where it comes from |
|---|---|---|
| Target D | two ports, x (the input bit) and y (the output bit); two components: c_x, which sets x from the boundary, and c_task, the relation y = 1 − x | S117: "one bit per number, exact for bitwise NOT" (Avida's NOT task is bitwise, so one bit stands for every bit) |
| Admitted edits A of the target | only the identity (`[ONE]`) | S117's choice: the target admits no change to its rule, its width or its order |
| Contract C | two pairs, (identity, input 0) and (identity, input 1); baseline input 0 | the inputs the world hands in |
| Query 𝒬 | read the port y | "what does the program hand back" |
| Candidate E | the program as one block: e_x sets x from the boundary, e_prog the relation y = nand(x, x) | the most common NOT program of run low seed 2 (S112: 110 instructions, 44 copies) |
| Transport t | identity on x and y; λ sends e_prog to c_task | written by S117 |
| Commitments Γ | {e_prog} | the block |
| History H | the same two pairs as C | both input bits occur in every number the world hands in (the fixed top bytes 0F, 33, 55, S125 check 04, item 1) |

### 2.2 Which question, and who holds it

A question is the tuple p = (D, C, b₀, 𝒬, O_p, ρ_p) (L135 to L147). (E) is a condition on a candidate *for* a question (L231); it asks nothing about who holds the question, whether anyone offered the candidate, or whether any rival exists. The text says so twice: "a candidate that nobody has offered is no one's rival" (L315), and a question's provenance may be declared, selected or constructed, and "any assessment may use any of the three" (L155).

D10.1's **problem** (Prob_j(ℰ, ℰ′; p) :⟺ Riv(ℰ, ℰ′; p) ∧ NotOut_j('Acc(ℰ)') ∧ NotOut_j('Acc(ℰ′)'); L317) is not a conjunct of (E). It needs two candidates *offered* for p, one in place of the other, and an assessor j for whom neither is ruled out. For MC1:

- **The program** holds no question: nothing in it represents the task or a rival (S117 B5; S123 H4; S125 clause 5, row 16). It makes no offer.
- **The execution environment** (the selector, S72) holds no problem either: the programs it keeps are a population, and "rivals are not a selection population" (L315); and under Reading C its task checker "entered the boundary whole" and represents nothing there (S129 data, MC1 at the S72 boundary: "the task-check code represents (survival condition, task) at this boundary: False"; I200).
- **The people** (Avida's authors, who named the task; S117, who wrote p) hold it, and they are outside the S72 boundary.

So MC1's question is a **declared** question in the sense of L155 (stipulated by the modeller, S117, from a task Avida's authors named), held by no one inside the boundary. (E) is still met on it, because (E) does not ask.

### 2.3 Which account: the four conditions

S129's data, MC1 at every setting, taken whole: "translates C" True, F1 True, F2eq True, Hom True, F2 True, A True, NC1 True, NC2 True, Dep True, NonVacuous True; so (E) True. Cut into its four instructions (read, copy, nand, out): F1 False, so (E) False. Checked by hand against the definitions:

- **F1** (L236; D5.7): the one active component e_prog has the relation {(0,1), (1,0)} at both pairs; its counterpart c_task has the same. Met. Cut into instructions, `read` and `copy` have counterparts (c_x) whose relation fixes x from the boundary, not the identity relation they carry: the task has no parts for them to match (S117 B3).
- **F2** (L242): the assembled block's solutions are the target's at both pairs. Met.
- **(A)** (L250): the block hands back 1 at input 0 and 0 at input 1, as the target does. Met.
- **Dependence** (L255; D6.5 ⟺ NC2): the answer at input 1 differs from the baseline answer at input 0, and deleting e_prog leaves y undetermined at both, so the contrast is lost. Met. The contrast is a change of **input** (a boundary), not of any edit to the target.
- **Non-vacuity** (L257; D6.6): Sol_D(1, b₀) is not empty; and since the encoded target admits only the identity, A × B = C, so nothing is excluded and nothing needed stating. Met, because the target was written with no other changes; the NOT task as Avida checks it admits others (wider numbers, other orders of the three inputs), and S117 stated the one-bit restriction.

### 2.4 Which contract, and what it leaves out

The contract is the two input bits. Three consequences, none of which (E) forbids:

1. **H = C.** The program was kept on every pair of its contract. On this contract it is faithful *where it was tested and nowhere else*, because there is nowhere else. The contract has no unseen change, so Argument 3 (L570 to L576) and surprise (L221) have no place here; "faithful on changes it was never selected against" (Grievance 3, L41) is not tested. On a wider contract (the inputs handed in another order) the record shows that programs differ (S116; S117 C3; MC2; 34 of 2,370 still did NOT with two inputs swapped, S125 row 17): that is a different question.
2. **No admitted edit.** The account answers "what does the program hand back for each input", a question whose only contrast is input 0 against input 1. It is the kind of candidate L269 calls "a table that encodes an organization's response to every admitted change": it "meets (F1) as a decomposition does, and it is an account when it meets the other conjuncts of (E)". The owner's one-part shop sign is the same shape (FC23.new2 (b)), which the owner called "an explanation. Just not a good one" (S44, S45).
3. **Taken whole only.** The verdict is about the block, not about the 110 instructions or the circuit S112 read from the trace (S117 B3: the circuit fails (A) at 5.4 in 100 single ablations; MC1 cut into instructions fails F1).

### 2.5 Which boundary, which provenance

S129's data, setting "C on, graded on" (both decisions, S83 and S84), MC1 (the graded-pay run, where doing NOT raised the rate of copying):

| Boundary | Sel | Con | Dec | stands for NOT (R) | (Suff) defeated at L536 by an argument not using (E) |
|---|---|---|---|---|---|
| A (S117), no boundary declared | True | False | False | True | True |
| B (S117), no boundary declared | False | False | True | False | False |
| C, the S72 boundary (the whole execution environment, its checker inside, its writers outside) | **True** | False | **False** | **True** | **True** |
| C, a wide boundary taking in Avida's authors | False | False | True | False | False |

At the S72 boundary, the owner's boundary (S72, S83), the transport is selected, so not declared; MC1 meets (E); so (Suff)'s antecedent, "Account(ℰ) ∧ ¬Dec(t)" on a contract of its question (L17, L61, L536; D16.XV), holds. At the wide boundary it is declared, and the owner's own S41 condition (Acc ∧ Dec ⇒ ¬Expl, D16.XV) already says it is no explanation there.

The last column is computed for an assessor stipulated to hold a record r and the premise r → ¬Expl (`claims_s41.expl_ruled_out`, used by S129's script at lines 107 to 124): it says what happens *if* someone holds such an argument. S85 is the owner saying, in effect, that the owner does.

### 2.6 Verdict: what "narrow explanation" was

**MC1 meets all four conditions of (E), strictly, on a contract of its question**, with these qualifications, each true of the encoding and none a condition of (E): the question is S117's, declared, held by no one inside the S72 boundary; its contract has two pairs and no edit; the contract equals the selection history; and the verdict is of the block taken whole.

"Narrow explanation" was therefore **the theory's verdict through its sufficiency conjecture**, not a theorem of the formal core and not an over-reading of (E): D16.XV leaves Expl an atom, and only (Suff) conjectures that Account ∧ ¬Dec suffices for it. "Narrow" was S127's word for that conjecture's sense of "explanation" (Account and not declared), as against the created explanation of (EX); the text itself never says "narrow". What over-read it is wording, listed in section 5: "explanation of NOT" for what is an account on a two-pair, no-edit question about NOT that S117 declared; "the semantics calls it" for what its conjecture predicts; and, in plain file 129, the omission of what S129's own table and S127's table both said, that an assessor who holds it is no explanation holds an argument against (Suff).

## 3. Why the answer is (c): the owner's view is an objection of the shape (Suff) names

### 3.1 The theory does not already agree with the owner

The theory would already agree if a representation with selected provenance (R, L205 to L208) were not thereby an explanation *by the text's own rules*. It is not thereby one, but the text does not stop there: (Suff) says that a candidate meeting (E) with a transport that is not declared is an explanation, unless an argument not using (E) rules that out. A selected transport is not declared (D12.1 to D12.3: exactly one of the three holds, FC78). S125's correction 16 already held this against our own earlier claim ("nothing constructs, so nothing explains" does not follow; the absence of Build blocks only *created* explanation), and S127's hinge file (section 0) said so for adaptations in nature under every reading. So, as the theory stands, the evolved NOT program at the S72 boundary falls inside (Suff)'s claim.

One reading would make the theory agree without a change: read "a contract of its question" (L536) as a question the holder of the candidate itself addresses (Attempt, D13.6) or holds as a problem (D10.1). Then MC1, which addresses nothing, would be outside (Suff)'s range, neither an explanation nor a counterexample. That reading is not the text's: (E) and (Suff) take the question as an argument and never mention Attempt or Problem (L231, L536; D6.7, D16.XV), and L315 contemplates candidates nobody offered. It is kept as an alternative proposal (section 4.5).

### 3.2 The owner's objection, as an argument

Written in the theory's terms (Part IX, L397; S41 Q23: a single claim used alone to decide this and not that is an argument):

- Premise 1 (taken as given, Part IX "Premises taken as given"): what is made by selection, with no construction, is knowledge, not explanation. ("Knowledge evolved through natural selection is case closed"; S59: "The explanation kind comes next.")
- Premise 2 (from the record): MC1's correspondence is selected, not constructed, at the S72 boundary (S129, the table above).
- Conclusion, by one modus ponens: MC1 is not an explanation of what its question asks.

Neither premise uses (E) or Acc (D16.XV's "an argument not using (E)", read at the symbol, I196). The argument is usable by the owner while the owner admits the form and the premises stay live (K2, L390). By D16.XV, "(Suff), L536 and L17: defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]", with ℰ = MC1 taken whole and j = the owner: **for the owner, (Suff) as written is ruled out at the S72 boundary**, while the argument stays usable (Part 0: a ruling out by a claim taken as given is a choice the person made). It is ruled out for no one else by that, and it is not ruled out at a boundary taking in Avida's authors, where MC1 is declared and S41 already gives ¬Expl.

This is the case Grievance 6 names, "You have replaced explanation with evolution" (L47). The text's answer there protects *creativity* ("every creative attribution requires it", construction); it does not protect *explanation*, which (Suff) lets selection produce. The owner's objection is that grievance made against (Suff), with an instance.

The owner then has three ways on, each a choice: drop Premise 1 (call MC1 a narrow, bad explanation, as S44 and S45 call the one-part shop sign); keep (Suff) and hold it ruled out (the theory would stand for others and not for its owner); or narrow what (Suff) claims so that the premise becomes part of the theory (section 4).

## 4. PROPOSAL: "explanation" reserved for constructed provenance

*Marked PROPOSAL. Nothing is applied. Written as maths first and the least prose that says it (S40).*

### 4.1 The smallest wording

- **D16.XV, the owner's condition.** Was: "Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) [owner S41: Q2]". Proposed: "**Acc(ℰ) ∧ ¬Con(t) ⇒ ¬Expl(ℰ)** [owner S41: Q2; S85]": a candidate meeting (E) whose transport is declared or selected is no explanation. Expl stays an atom; (E) still takes no provenance (FC30 unchanged).
- **D16.XV, (Suff).** Was: "defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]". Proposed: "defeated for j ⟺ ∃ℰ [**Acc(ℰ) ∧ Con(t)** ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)]".
- **Under Reading C** (if the owner writes S83 in): Con_β and Expl_β, read at the boundary declared for the claim (S129's K1 proposal, "write Expl_β(ℰ) in D16.XV and 'at the boundary declared' at L536"); by I201 a construction whose target is held only outside β is declared at β (S129 section 5, item 11).
- **Text.** The replacement "\(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\)" → "\(\operatorname{Account}(\mathcal E)\land\operatorname{Con}(t)\)" at L17 (twice), L49, L61 and L69, and at L536 "with a transport whose provenance is not declared (Part IV)" → "with a transport whose provenance is constructed (Part IV)". Nothing else in the text needs to change for the definitions to hold; L47 gains two words (below, 4.3).

### 4.2 Two words, one already in the text

The text already has the word for what the owner calls knowledge: **representation** (R), "a fidelity relation with a history" (L211), selected or constructed (L205 to L208). Under the proposal the theory's two terms are:

| Theory's term | Definition | The owner's word |
|---|---|---|
| representation | (R): a faithful transport with selected or constructed provenance (unchanged) | knowledge: **evolved knowledge** where selected, **created knowledge** where constructed |
| explanation | an account meeting (E) on its question whose transport is constructed (proposed) | the explanation kind (S59) |
| created explanation | (EX), unchanged | an explanation created in a creative critical episode that repairs an aim |

Whether the owner's two phrases should enter the text as names (for example after L211: "a selected representation is what an adaptation holds; a constructed one is what a learner or a thinker holds") is a further question; this proposal does not need them. The text never uses "knowledge" (S110, O10 and O11), and S127's missing-words file left "a bridging sentence on knowledge" to the owner.

### 4.3 What it changes

| Place | Now | Under the proposal |
|---|---|---|
| **L17** (the constitutive conjecture) | a counterexample is a candidate meeting Account ∧ ¬Dec(t) that an argument not using these four rules out as an explanation | the same with Account ∧ Con(t); a selected account is no counterexample, since it is not claimed to be an explanation |
| **L47**, Argument 6, "You have replaced explanation with evolution" | "every creative attribution requires it" | "every explanation and every creative attribution requires it": the grievance is then answered for explanation too |
| **L49**, Grievance 7 (mathematics) | a piece of mathematics explains, relative to a question, when Account ∧ ¬Dec(t) | when Account ∧ Con(t): a proof explains where it was worked out; a proof found by a search scored by a checker, with no represented target, is a selected account until someone reconstructs it (and a reconstruction is new to the one who makes it, S129 item 9) |
| **L61** (where to attack) | (Suff) sufficiency of Account ∧ ¬Dec(t) | sufficiency of Account ∧ Con(t) |
| **L69** (Fallibility without error-as-work) | "explanation" in this commitment means Account ∧ ¬Dec(t) | Account ∧ Con(t) |
| **L536**, (Suff) | provenance not declared | provenance constructed |
| **D16.XV** | as 4.1 | as 4.1 |
| **FC30** ((E) takes no provenance) | holds | holds, unchanged: the proposal changes what suffices for "explanation", not (E) |
| **FC30.new1** | (a) "with a constructed or a selected transport it is in all three [defeat sets]"; (c) "Expl := Acc ∧ ¬Dec meets both (Suff) and the owner's condition" | (a) a selected transport leaves the student's formula outside every defeat set, as a declared one does; (c) restated: Expl := Acc ∧ Con meets the reworded (Suff), S41 and S85; (b), (g), (h) unchanged in shape; the claim to be recomputed by a checker before anything is written in |
| **The (Prov) claims** (L542; FC12.new1 to FC12.new3, FC77, FC78, FC80, FC83) | unchanged in content | unchanged; (Prov)'s second clause (a method rewriting every construction trace as a selection history) would now remove explanation from the semantics as well as creativity, which raises its stakes; (Prov)'s third clause (explanation operates on the object layer) reads more simply, since L201's arrangement becomes the rule for explanation: selected representations below, constructed explanations above |
| **(EX)** (L447; D14.7; FC90, FC90.new1) | its account conjunct is Account((c, p_c, t_c, Γ_c)) | unchanged in wording; **to check**: whether Origin(s, c, …) with Build already gives Con(t_c), or whether (EX) needs Con(t_c) as a conjunct for every created explanation to be an explanation. Not computed here |
| **S127's table** (hinge, section 3) | NOT program under A and C: "taken whole, an explanation of NOT, never created"; adaptations: "narrow explanations where (E) holds"; owner's premise "rules out (Suff) for the owner" | NOT program: a selected representation of NOT that meets (E) taken whole: evolved knowledge, not an explanation; adaptations: evolved knowledge, never explanations; the owner's premise "agrees" under every reading |
| **S129's map** (R117: D16.XV and FC30.new1; R003: T01, L17) | R117 LINES UP EXACTLY, "the semantics calls it an explanation of NOT in its narrow sense"; R003 NOTHING IN AVIDA | by hand, not computed: R117 still lines up exactly, now as an instance of Acc ∧ Sel ⇒ ¬Expl; R003 still nothing in Avida; the counts 122 / 28 / 18 / 116 unchanged; only the wording of R117 moves |
| **Adaptations in nature** | under every reading, where (E) holds of a trait taken whole, a narrow explanation, never a created one (S127, section 0) | a selected representation (evolved knowledge) where faithful, never an explanation; explanation only where an account was constructed; the line between Deutsch's adaptive and explanatory kinds, as S110 (O4, O10, O11) and S123 (H4) give them, becomes the line between representation and explanation |

### 4.4 What could count against it

1. **The theory's own line that (E) takes no provenance** (FC30; L277: "a mechanism meets (E) or fails it whatever led anyone to guess it"). Not violated: (E) is untouched. But the proposal makes two candidates with the same organization, transport and fidelity differ in being an explanation by history alone. The theory already does this with Dec (S41: the student's copied formula is no explanation), and says the three provenances are "told apart by their histories, not their outputs" (L13); so the cost is not new in kind, only wider.
2. **S41 Q2, as S108 read it (C16).** The owner set a link "simply declared" against one "found by trial or worked out" and answered "No, not if just declared". S108 read "found by trial" as selection, and its candidate C16 (explanation as Account ∧ Con) was flagged because it took the owner's sign and weathervane out wherever they were reached by trial. Read again: an agent's trials *against a target it holds* are construction in the theory's sense (D12.2: the target held; L405: "Reconstruction by a learner is construction"), not selection (L411: "A selected transport has no represented target in its history"). Only blind variation with no held target is selected. S85 now says such a result is "knowledge, not explanation". So C16's objection holds only if the owner meant blind trial in S41; the owner can say.
3. **Reach.** If a selected correspondence passed (E) on changes it never met (reach), it would be "knowledge of" its question in the adaptive sense on every source S110 lists (O1 to O4, O11), and some would call reach the mark of explanation. The proposal still withholds "explanation" from it. That is the owner's line in S85, and it matches Deutsch's distinction as S110 and S123 give it (adaptive knowledge from variation and selection, explanatory knowledge from conjecture and criticism); but it means a selected account with great reach is not an explanation, which some readers will contest. MC1 itself has no reach to test (H = C).
4. **"Constructed" is broad.** Con needs an owned trace with the target held and no mere relay; S128 (i) derived that a unit learning from supplied labels is constructed under Readings A, B and C alike. So a classifier trained on labels whose correspondence meets (E) would be an explanation under this proposal. If the owner would also call that "knowledge, not explanation", the line has to be higher: **Build for explanatory use** (D13.3's ExplUse: the content used as an account), or only **(EX)**'s created explanation. The ladder is: ¬Dec (now) ⊃ Con (this proposal, the smallest) ⊃ Build with ExplUse ⊃ (EX). The proposal takes the smallest step that answers S85; a higher rung is the owner's to choose if the experiment of the companion file shows constructed accounts the owner would still not call explanations.
5. **S110's two-types result.** FW3 and FW4 held that physical (constructor-theory) knowledge and explanatory knowledge differ in type and are independent; the proposal fits it (representation on one side, explanation on the other). But S110 found the result rests on readings (the "one-place" wording against the book's use with an environment and an "of"; "capable of remaining instantiated" read as "did remain"), and left open whether explanatory knowledge is ever resilient *because* it is explanatory. The proposal does not depend on the result, and does not make (R) into constructor theory's resilient information: it says nothing about copying, resisting change or remaining (the owner's three properties, S59).
6. **Mathematics found by search** (Grievance 7, L49). Under the proposal, a correct proof produced by a blind search against a checker is not an explanation at the search's boundary, though it meets (E). Some will find that wrong; it is the same verdict the proposal gives MC1.

### 4.5 Alternatives considered, not proposed

- **Read "its question" as one the holder attempts** (Attempt, D13.6) or holds as a problem (D10.1): MC1 then falls outside (Suff). Smaller in the text (one phrase at L536), but it reaches past S85: an agent who uses an evolved rule of thumb on a question it holds would make that rule an explanation; and it ties explanation to who asks, which L231 and L315 avoid.
- **Keep (Suff) and drop the owner's premise**: no change; MC1 is a narrow, bad explanation (as S44, S45 for the shop sign). Costs the owner S85.
- **Index only** (S129's K1: Expl_β): needed under Reading C whatever is chosen; it does not by itself answer S85, since at the S72 boundary MC1 is selected.

## 5. What S117's map and S129's results should have said (proposed corrections, listed, not applied)

These files are not written (S108 to S129 are read only). Proposed wording, for the owner and for any later integration:

1. **S129 results, section 0 and the owner's-words paragraph**, "counts, taken whole, as a narrow explanation of it": should read "taken whole, meets (E) on the question S117 declared for it (one input bit, two pairs, no admitted edit, the contract equal to its selection history), with a selected transport at the S72 boundary, so (Suff) conjectures that it is an explanation in the narrow sense (Account and not declared), never a created one; an assessor who holds, by an argument not using (E), that it is no explanation holds an argument against (Suff) there (MC1: 'defeated at L536: True')."
2. **S129 results, section 4's table**: the column "(Suff) defeated by an argument not using (E)" should be headed "(Suff) defeated *for an assessor who holds* an argument not using (E) that it is no explanation (stipulated, `claims_s41.expl_ruled_out`)", since the value is computed for a stipulated assessor, not found in the case.
3. **Plain file 129**, "it passes the theory's test, so it counts as a narrow explanation of NOT, with nothing in it built": should add "if you hold that it is not an explanation, the theory's central claim is ruled out for you at your edge; that is your choice to make" (S127's table and S129's own row both said it; the plain file left it out).
4. **S117's corrected map, R117** (`what_matches`), "so the semantics calls it an explanation of NOT in its narrow sense": should read "so the semantics' sufficiency conjecture counts it an explanation in its narrow sense, on a two-pair question about NOT declared by the modeller and held by nothing inside the boundary". Its last sentence already names the argument against (Suff), and stays.
5. **S117's results, B1** (both maps' unit D16.XV): "passes as an explanation" should read "passes the test of an explanation (E), on a question declared by the modeller"; the computed values are right.
6. **S127's hinge, section 0**, "an explanation of it in the semantics' narrow sense": the same qualification as 1; and its table's row "Owner's 'Avida programs are not explanations', held in the narrow sense" is exactly S85, and should be cited when the owner decides.
7. **Everywhere "explanation of NOT" is said of MC1**: "an account of the two-pair NOT question", since the account answers nothing about any change to NOT itself (the target admits none).

## 6. The owner's choice, in one sentence

Either "explanation" is kept for what was worked out, so the evolved NOT program, and every adaptation in nature, is evolved knowledge that passes the test and not an explanation (the proposal of section 4); or the theory stays as it is, the program is a narrow and bad explanation, and your "knowledge, not explanation" remains an argument, for you, against the theory's central claim.

## 7. What is unsure

- **The encoding is S117's** (Θ by hand, I90), carried unchanged by S129. A different encoding of the NOT task (wider numbers, admitted changes to order or width) would make a different question; the program would then fail (E) or meet it on a different contract (S117 C3, MC2). The verdict above is for the question as encoded.
- **Whether the owner's S85 is a premise held "in the narrow sense"** of (Suff), as section 3.2 writes it, or a wish about the word, is Claude's reading; the argument form is the owner's to accept.
- **(EX) and Con(t_c)** (section 4.3): not computed; a checker should compute whether every (EX) instance has a constructed t_c before the proposal is written in.
- **The map counts under the proposal** were moved by hand (R117, R003), not by program.
- **S41's "found by trial"**: Claude's reading of it as an agent's trials (section 4.4, item 2) differs from S108's; only the owner can say which was meant.
