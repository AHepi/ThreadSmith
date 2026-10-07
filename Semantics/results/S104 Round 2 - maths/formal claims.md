# S104 Round 2 — formal claims

*Log S104, review round 2 (the maths round), 27 September 2026, under decision S36 ("maybe exploring the math a bit more might help instead of words. Since words are vague"). The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd (checked before every build; not written to). Built by `s104_build.py` from `s104_claims.py`; every quotation was compared by program with the line it names. The notation is fixed in `formal core.md` §0; the inventions are in `inventions register.md`.*

**What this is.** Each claim the formal core lets one state and test: its source sentences quoted, its formal statement, and its type — a *definition-consequence* (it follows from the definitions as formalized), a *stated result* (one of Arguments 1–10, or a sentence of the text that says something follows, entails or is so), or a *strong candidate* of S100 (the 36 sentences that stood longest). Every claim lists the inventions it uses; any result on it depends on them, and a counterexample that rests on an invention is a counterexample to this formalization, not to the text. Each claim's search result is added under it, from `search results.md`. Where a line under *Look* says where a counterexample might lie, that is a first reading, not a result. Nothing is settled (S28).

**Counts.** 110 claims: 52 definition-consequences, 58 stated results, 23 strong-candidate claims (types overlap: a claim can be more than one). 104 claims use at least one invention. 19 claims of the text are recorded as not formalized (below). Of the 36 strong candidates: 21 formalizable; 1 formal only as a gloss; 6 formalizable in part; 4 typing only; 3 syntactic; 1 not formalizable.

**The owner's decisions kept.** No claim lists, counts, grades or records rivals (S20); none says what must happen (S21); the prose here uses no word S23 scrubs; physical possibility enters only in §§12–16 of the formal core, where a content is held, built or carried out, and as the content of a claim a candidate can conflict with (S25–S27); nothing is settled, and a ruling out is a choice (S28). What hard to vary covers is parked (S33–S34): the only related claims are about the text's own 'easy to vary' at L317 (FC43), and they add nothing about what hard to vary covers. The appraisal relation appears only as a typed input (NF16, NF19); where values are placed is the owner's question.

## Index

| id | claim | type | lines | inventions |
| --- | --- | --- | --- | --- |
| FC01 | Solutions shrink as relations shrink; deletion never removes a solution | definition-consequence | L100, L103 | I03 |
| FC02 | Direction is read from the admitted edits; output status is not | stated result | L109, L325 | I04, I05, I65 |
| FC03 | 'Of one kind on C' is an equivalence relation | definition-consequence | L119 | I10 |
| FC04 | A coarser contract identifies more components; a finer one can separate them | definition-consequence | L119 | I10, I11 |
| FC05 | Kinds are fixed by relations, not by solution values | definition-consequence | L119 | I10 |
| FC06 | A setting edit leaves every reader's relation as it was | definition-consequence | L119, L124 | I04, I07, I09 |
| FC07 | The three families on the pole's contracts, under both readings of 'observation edit' | definition-consequence | L123, L109, L127, L325 | I04, I06, I07, I09, I65 |
| FC08 | L127's gloss of a measurement's signature has a clause about solutions | definition-consequence | L127, L119 | I04, I06, I07 |
| FC09 | Four names, three families: a constitutive status is a rule application | definition-consequence | L121, L347 | I08 |
| FC10 | L57 against the new L123 | definition-consequence | L57, L123 | I08, I09 |
| FC11 | Roles are relative to A; families are relative to C | definition-consequence | L109, L113 | I04, I09 |
| FC12 | Invariance clauses can be vacuous; change clauses cannot | definition-consequence | L124, L125 | I09 |
| FC13 | The families are patterns in (K), not additional data | strong candidate; definition-consequence | L127 | I04, I06, I08, I09 |
| FC14 | No definition asks whether a component 'is' a cause | strong candidate; definition-consequence | L127 | — |
| FC15 | τ[C] is a contract of the candidate's organization | definition-consequence | L141, L242, L554 | I12, I18 |
| FC16 | Reading a candidate's components through the transport agrees with (K) on τ[C] | definition-consequence | L119 | I10, I12 |
| FC17 | Argument 1: (F1) makes each commitment's signature its counterpart's | stated result | L554, L556, L245 | I12, I13, I14, I15 |
| FC18 | Argument 1's Consequence: a same-kind condition adds nothing; no third case | stated result | L558, L281 | I10, I13, I14 |
| FC19 | (F1) and (F2) do different work | stated result | L245 | I14, I15 |
| FC20 | When (F2) at a pair gives (A) at that pair (violation in either extent) | definition-consequence | L219, L220, L250 | I16, I20, I21, I49, I50 |
| FC21 | A contract of relabelings admits no candidate meeting (A) and non-circular dependence | stated result | L257 | I21, I22, I26 |
| FC22 | The baseline alone gives no contrast | definition-consequence | L141, L255 | I21, I22 |
| FC23 | 'p because p' fails non-circular dependence through NC1 only | strong candidate; stated result | L273 | I21, I22, I24, I25 |
| FC24 | L273's second sentence uses 'account' for a candidate | definition-consequence | L273 | I24 |
| FC25 | Tables: a fixed table fails (F1) where the projection moves; an encoding table meets it | stated result | L269 | I03, I04, I14, I32 |
| FC26 | The pole: the forward organization meets (E) on the production contract | stated result | L325 | I04, I20, I21, I24, I27, I65 |
| FC27 | The pole: the reversed calculation fails (F2) on the production contract | stated result | L271, L325 | I04, I65 |
| FC28 | The pole: the reversed calculation meets (F1), (F2), (A) on the identification contract | stated result | L325 | I20, I65 |
| FC29 | A contrast no admitted edit realizes witnesses nothing | definition-consequence | L275 | I12 |
| FC30 | (E) takes no assessor, history, provenance or wording | definition-consequence | L43, L67, L277 | I20, I27, I28 |
| FC31 | 'The four conditions', five conjuncts, and L520's three sources | definition-consequence | L61, L231, L262, L536, L520 | I49 |
| FC32 | L520 (after round 1) against L526's dependence order | definition-consequence | L526, L520 | I20, I27, I28 |
| FC33 | 'Every conjunct is a condition on supplied relations; none inspects a label' | stated result | L265 | I24, I27, I28, I70 |
| FC34 | Two questions, one target: what 'an answer to one is not an answer to the other' allows | stated result | L151 | I24, I27, I73 |
| FC35 | 'Prediction' at L151 is outside L219's definition | definition-consequence | L151, L217 | I51 |
| FC36 | What a question asks is fixed by the query and the contract, not by a label | stated result | L151 | I72 |
| FC37 | The finite monotone claim | stated result | L305 | — |
| FC38 | Redundant routes | stated result | L307 | I30 |
| FC39 | Interference | definition-consequence | L309, L305 | I30 |
| FC40 | Infinitary routes: collective criticality, and the step the first sentence leaves unsaid | strong candidate; stated result | L311, L313 | I30, I31 |
| FC41 | Commitments that do no work, and why 'when Γ is infinite' | stated result | L313 | I29 |
| FC42 | Criticality is relative to the route | definition-consequence | L299 | I30 |
| FC43 | Conflict, rivals, problems and 'easy to vary' are symmetric | stated result | L317 | I33, I37 |
| FC44 | Two commitments with one counterpart and different relations cannot both meet (F1) | stated result | L315 | I14, I19, I36 |
| FC45 | Recoded candidates, and candidates some relations let both meet, conflict nowhere | stated result | L315 | I17, I19, I20, I70 |
| FC46 | A conflict inside the contract: at most one account | stated result | L317 | I19, I21 |
| FC47 | A test at a conflict pair rules out at least one, for an assessor who can use it | stated result | L317 | I19, I38, I40, I42, I43 |
| FC48 | No conflict inside the contract: answers agree there | stated result | L317 | I21 |
| FC49 | The two kinds of problem exclude each other and cover every pair of rivals | definition-consequence | L317 | I16, I17, I33 |
| FC50 | A finer contract makes a problem of the first kind; a narrowed one leaves the problem on p | stated result | L317 | I11, I33 |
| FC51 | A change that separates two accounts lies outside their shared contract | stated result | L317, L568 | I18, I24, I27 |
| FC52 | Conflict with a claim: the first disjunct implies the second | definition-consequence | L315 | I19, I34 |
| FC53 | Conflict with a claim rules a candidate out only with the premise that the claim speaks of the target | stated result | L315 | I34, I38, I40 |
| FC54 | Rivals given χ conflict nowhere without χ at that pair | definition-consequence | L315 | I19, I33, I34, I35 |
| FC55 | Nothing in Part VI counts rivals or orders candidates | definition-consequence | L317 | — |
| FC56 | Ruling out grows with what is accepted; withdrawal rules nothing out; absence rules out nothing | strong candidate; definition-consequence | L393, L397 | I38, I40, I41 |
| FC57 | (I2): identified at every attainable value exactly when the feature factors through the measurement | stated result | L329 | I63, I64 |
| FC58 | (I3): the kernel criterion; repeated rows; an independent calibration | stated result | L329 | I63, I64 |
| FC59 | The two balances | stated result | L331 | I64 |
| FC60 | Setting a bias from the favoured mass: where the circularity can be registered | stated result | L331 | I24, I39 |
| FC61 | (O1): an invariant blocks paths; equal values do not give paths; twenty-three tokens | stated result | L335 | I63 |
| FC62 | Eliminative explanation: the rival's structure as a deleted counterpart | stated result | L339 | I03, I14 |
| FC63 | Odd-order skew-symmetric matrices | stated result | L343 | I03, I27, I66 |
| FC64 | Functional transport | stated result | L353 | — |
| FC65 | Relational transport: simulations compose | stated result | L361 | — |
| FC66 | (T2): the accumulated bound, and none without a modulus | stated result | L363 | — |
| FC67 | A declared invertible recoding keeps the content | stated result | L365 | I54, I70 |
| FC68 | A failed answer stays failed | stated result | L369 | I20, I38, I40, I41 |
| FC69 | (K2) is well founded; the loop read in S101 closes below the step | strong candidate; definition-consequence | L390, L393 | I40 |
| FC70 | Withdrawing a premise that is live twice over leaves the step usable | strong candidate; definition-consequence | L393 | I40, I41 |
| FC71 | (K3): a failed prediction rules out the conjunction, and nothing narrower | stated result | L395 | I38, I43 |
| FC72 | The block on a premise that is the denial, and a premise taken as given | definition-consequence | L397 | I38, I39 |
| FC73 | Inconsistent accepted premises rule out a claim and its denial alike | stated result | L397 | I38 |
| FC74 | A criticism occurrence can exist without bearing | strong candidate; definition-consequence | L383 | I45 |
| FC75 | Active routes: the excluded routes fail the definition's own clauses | strong candidate; definition-consequence | L375 | I44, I46 |
| FC76 | Reason use gives neither bearing nor usability | strong candidate; definition-consequence | L385 | I47 |
| FC77 | Without a physical witness, selection is met by every transport | definition-consequence | L195, L205 | I48, I52 |
| FC78 | Exactly one of three provenances | stated result | L193, L201 | I52, I53, I54 |
| FC79 | Survival is how the transport got there; fidelity is what it is | strong candidate; definition-consequence | L41 | I49, I52 |
| FC80 | Argument 3: underdetermination where the population leaves room | stated result | L572, L574 | I02, I52, I71 |
| FC81 | Argument 4, and who can be surprised | stated result | L580, L223 | I50, I52, I53 |
| FC82 | The two responses to a violation have no common result | strong candidate; definition-consequence | L225 | I52, I53 |
| FC83 | Only the construction response can be originative | strong candidate; stated result | L225 | I52, I56 |
| FC84 | Every creative attribution requires construction | strong candidate; definition-consequence | L47 | I53, I56 |
| FC85 | A content matches itself; the matching is read one way | definition-consequence | L413, L416 | I48 |
| FC86 | Repair: a protected aim failed in between is lost | strong candidate; definition-consequence | L438, L441 | I57 |
| FC87 | Two sufficient contributions that both ran are both attributed | definition-consequence | L441 | I46, I57 |
| FC88 | Losses outside P are exposed in the claim, not in (P) | strong candidate; definition-consequence | L441 | I57, I58 |
| FC89 | L443 (after round 1) puts 'deployable' where Deploy's type allows it | strong candidate; definition-consequence | L443, L449 | I59, I60 |
| FC90 | The worked case's '(EX) is met' against (EX)'s conjuncts | stated result | L628 | I44, I57, I59, I60, I68 |
| FC91 | (CT1) is C ⊆ F(C) only with (CT1)'s completion read into F | definition-consequence | L466, L471 | I61 |
| FC92 | (CT2): monotone F and its greatest fixed point | strong candidate; stated result | L471, L546 | I61 |
| FC93 | (CT3), (CT4), and capability at one tolerance | stated result | L479 | I62 |
| FC94 | Recursion does not entail universality | stated result | L509 | I74, I75 |
| FC95 | A system can represent a theory in error | stated result | L211 | I48, I52 |
| FC96 | Argument 2: same counterparts, one account | stated result | L562 | I10, I12, I14 |
| FC97 | Argument 5: a contract can be an organization and a content | stated result | L588, L590 | I01, I48, I67 |
| FC98 | Argument 6 and the dependence order: acyclic, and ending where the text says | stated result | L596, L526 | I20, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59 |
| FC99 | Argument 7: an account on C can fail on C' | stated result | L606 | I65 |
| FC100 | Argument 8: structure-preserving bijections keep (E), (G), (P), (EX) | stated result | L612 | I45, I70 |
| FC101 | Argument 9: an input–output description does not fix an account | stated result | L616 | I29, I46 |
| FC102 | Argument 10: surprise, the structural failure of selection, and the constructed layer | stated result | L624, L626 | I52, I68 |
| FC103 | Argument 10: the swap, two pairings, one account | stated result | L630 | I10, I14, I68, I69 |
| FC104 | The two extents of 'fidelity' across the text | definition-consequence | L189, L245, L247, L520, L630 | I49, I50 |
| FC105 | 'Event' is used and never defined; 'occurrence' is defined | definition-consequence | L169, L161, L604 | I45 |
| FC106 | A question's three defects, as far as they can be written | strong candidate; definition-consequence | L161 | I76 |
| FC107 | Exposing a question's defect is another question | strong candidate; definition-consequence | L161 | I76 |
| FC108 | The first sentence of non-circular dependence adds no condition | strong candidate; definition-consequence | L255 | I23 |
| FC109 | 'A mathematical error': the named claims, each under its stated assumptions | strong candidate; stated result | L546 | I10, I12, I13, I14, I61, I63, I64, I71 |
| FC110 | The classes are defined; no membership is asserted | strong candidate; definition-consequence | L27, L528 | I74, I75 |

## A. Organizations, roles, families, kinds

### FC01 · Solutions shrink as relations shrink; deletion never removes a solution

> L100 | \operatorname{Sol}_D(a,b)=\{z\in X_D:\forall j\in J,\ z|_{V_j}\in L_j(a,b)\}. \tag{O}

> L103 | A deleted component imposes the full relation on its ports.

**Formal.** If L_j(a,b) ⊆ L'_j(a,b) for every j, then Sol_D(a,b) ⊆ Sol_D'(a,b). In particular Sol_{D−G}(a,b) ⊇ Sol_D(a,b), where D−G deletes the components of G (full relations).

**Type.** definition-consequence.

**Uses.** Inventions: I03. Formal core §1.

**Look.** Used by NC2's loss clause: for a query that is not monotone in Sol, a deletion can make an undetermined answer determined, a case NC2's wording does not name.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 witness found). Rests on: I03, I77, I78. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC01 --scale 4 --time-cap 45`.

### FC02 · Direction is read from the admitted edits; output status is not

> L109 | The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read.

> L325 | Under \(A\) containing interventions on \(H\) and \(\theta\), these ports are inputs and \(L\) is an output, by Part II.

**Formal.** (a) Input(v) and asg(v) are functions of the setting edits in A (I04); two organizations with the same L and different A can differ in both. (b) Output(v,j) (I05) is a function of L_j(1,·) alone and does not depend on A. (c) In the pole encoding, c_L's relation L = H cot θ (θ in (0°,90°)) determines each of H, θ, L given the other two, so H and θ are outputs of c_L as well as L; the direction H,θ → L is carried by asg, not by output status.

**Type.** stated result.

**Uses.** Inventions: I04, I05, I65. Formal core §2, §17.

**Look.** Whether L325's 'L is an output, by Part II' needs A at all, and whether 'direction' is meant to include output status.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 witness found; 1 holds on all models tried; 1 computed: as claimed). Rests on: I04, I05, I65, I77, I78, I80, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC02 --scale 4 --time-cap 45`.

### FC03 · 'Of one kind on C' is an equivalence relation

> L119 | A kind is an equivalence class of components under this relation.

**Formal.** j ~_C j' (I10) is reflexive, symmetric and transitive on J.

**Type.** definition-consequence. S100 units: L115.s1, L113.s2.

**Uses.** Inventions: I10. Formal core §4.

**Look.** Holds under I10 and under its value-bijection alternative.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I10, I77, I78. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC03 --scale 4 --time-cap 45`.

### FC04 · A coarser contract identifies more components; a finer one can separate them

> L119 | a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract.

**Formal.** C' ⊆ C ⇒ (j ~_C j' ⇒ j ~_C' j'), since one footprint bijection serving every pair of C serves every pair of C'. And there are D, C' ⊊ C, j, j' with j ~_C' j' and not j ~_C j'.

**Type.** definition-consequence. S100 unit: L115.s1.

**Uses.** Inventions: I10, I11. Formal core §4.

**Look.** Under I11's alternative (coarser = a quotient of edits), the first half needs the quotient to respect the relations.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 witness found). Rests on: I10, I11, I77, I78. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC04 --scale 4 --time-cap 45`.

### FC05 · Kinds are fixed by relations, not by solution values

> L119 | two components that differ only in those values are of one kind on \(C\), whatever the difference is called.

> L119 | and an edit under which the two relations stay equal does not separate the components.

**Formal.** sig_C(j) is a function of (L_j(a,b))_{(a,b)∈C} alone. If β_*L_j(a,b) = L_j'(a,b) for every (a,b) in C, then j ~_C j', whatever the projections of Sol_D(a,b) on V_j and V_j' are; adding to C a pair at which β_*L_j = L_j' leaves the relation between j and j' as it was.

**Type.** definition-consequence. S100 unit: L115.s1.

**Uses.** Inventions: I10. Formal core §4.

**Search result (S104).** COUNTEREXAMPLE FOUND (2 holds on all models tried; 1 counterexample found). Rests on: I10, I77, I78, I93. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC05 --scale 4 --time-cap 45`.

### FC06 · A setting edit leaves every reader's relation as it was

> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it

> L124 | - a **measurement** has a signature invariant under interventions on the measured port

**Formal.** Under I04, for every port m, every setting edit a of m and every component j ≠ asg(m): L_j(a,b) = L_j(1,b). Hence every component that reads m and does not assign it is invariant under interventions on m on every contract (I09): the first clause of the measurement bullet holds of every reader of m.

**Type.** definition-consequence. S100 unit: L124.s1. Round 1: what the L123 change may have disturbed: the asymmetry the critical review gives between C07 and C08/C09.

**Uses.** Inventions: I04, I07, I09. Formal core §2, §4.

**Look.** If so, the measurement family is picked out by its second clause alone.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I04, I07, I09, I77, I78, I80, I102. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC06 --scale 4 --time-cap 45`.

### FC07 · The three families on the pole's contracts, under both readings of 'observation edit'

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

> L109 | A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports

> L127 | a part that reads or reports another part has a measurement's signature

> L325 | An intervention on \(L\) replaces its component and leaves \(H,\theta\) unchanged.

**Formal.** Causal_C(j): C holds a setting edit of j's output port that changes L_j, and j is invariant under Obs on C. (a) Under R-i, if j reads a port m other than its output o and C sets o, that setting edit alters asg(o) = j and leaves asg(m): it is in Obs, and j changes under it, so ¬Causal_C(j); and j is a measurement of m (FC06 and that edit). On a contract that sets every port, Causal_C is the set of components that read no port besides their own output. (b) Under R-ii, Obs holds only non-setting edits of a reporting component. Pole (I65), contract C1 = settings of H and θ: under both readings c_H, c_θ ∈ Causal and c_L is in no family (C1 sets no output of c_L and holds no edit of it). Contract C2 = settings of H, θ and L: under R-i c_H, c_θ ∈ Causal, c_L ∈ Meas(·,H) ∩ Meas(·,θ), c_L ∉ Causal; under R-ii c_H, c_θ, c_L ∈ Causal and no component is a measurement.

**Type.** definition-consequence. S100 units: L123.s1, L124.s1. Round 1: round-1 change L123; what the L123 change may have disturbed: L123–L125 against L57, L109, L127.

**Uses.** Inventions: I04, I06, I07, I09, I65. Formal core §2, §4, §17.

**Look.** The round-1 critical review keeps a measurement out of the causal family by R-i ('an intervention on the reading is, by L109, an observation edit') and, in the same paragraph, counts the pole's forward component in the causal family on the contracts the text uses; under R-i both hold only if that contract does not set L. Test whether one reading gives both.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (5 computed: as claimed). Rests on: I04, I06, I07, I09, I65, I80, I92, I102. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC07 --scale 4 --time-cap 45`.

### FC08 · L127's gloss of a measurement's signature has a clause about solutions

> L127 | change only the reading and the part it reports stays as it was; change the part and the reading follows.

> L119 | A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution

**Formal.** 'Change only the reading and the part it reports stays as it was' is a condition on relations (FC06). 'Change the part and the reading follows' is a condition on solutions: under a setting edit of m, the projection of Sol_D on the reading o changes. There are D and j reading m whose relation is constant in m (the projection on o does not follow m) and j still meets both clauses of L124.

**Type.** definition-consequence. S100 unit: L127.s1. Round 1: what the L123 change may have disturbed: L127.

**Uses.** Inventions: I04, I06, I07. Formal core §4.

**Look.** If the example stands, L127's gloss says more than L124's signature, or L124 would need a solution-level clause (which L119 excludes from signatures).

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 witness found). Rests on: I04, I06, I07, I77, I78. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC08 --scale 4 --time-cap 45`.

### FC09 · Four names, three families: a constitutive status is a rule application

> L121 | What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:

> L347 | Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\).

**Formal.** The bullets define three predicates Causal_C, Meas_C, Rule_C. L347 gives a constitutive rule the signature of Rule_C (Z read as the world's ports, C_r as the rule, I08). So 'a rule' and 'a constitutive status' both map to Rule_C.

**Type.** definition-consequence. S100 unit: L125.s1. Round 1: matter 4: L121 names four things with three bullets.

**Uses.** Inventions: I08. Formal core §4.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I08, I78. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC09 --scale 4 --time-cap 45`.

### FC10 · L57 against the new L123

> L57 | a rule's application changes when the rule is edited and not when the world is intervened on; a cause's assignment changes under intervention.

> L123 | has a signature that changes under intervention on its output port and is invariant under observation edits;

**Formal.** Rule_C(j) ⇒ (variable under rule edits ∧ invariant under world interventions), which is L57's rule sentence; Causal_C(j) ⇒ changes under intervention on its output, which is L57's cause sentence. L57 names no condition on observation edits; the bullet's second clause adds to L57 and does not conflict with it. The clause round 1 removed ('and under replacement of the component') has no counterpart in L57.

**Type.** definition-consequence. S100 units: L123.s1, L125.s1. Round 1: what the L123 change may have disturbed: L57.

**Uses.** Inventions: I08, I09. Formal core §4.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 not tested). Rests on: I08, I09, I77, I78. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC10 --scale 4 --time-cap 45`.

### FC11 · Roles are relative to A; families are relative to C

> L109 | A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly.

> L113 | Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).

**Formal.** Input(v) quantifies over A; Causal_C(asg(v)) over C ⊆ A × B. There are D, C, v with Input(v) and ¬Causal_C(asg(v)) (C holds no setting edit of v). Conversely every family predicate uses edits of A only, so no family membership needs an edit A lacks.

**Type.** definition-consequence. S100 unit: L113.s1. Round 1: matter 5: L109 gives roles under A while (K) builds a signature on a contract C; what the L123 change may have disturbed: L109.

**Uses.** Inventions: I04, I09. Formal core §2, §4.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed; 1 holds by construction). Rests on: I04, I09, I80, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC11 --scale 4 --time-cap 45`.

### FC12 · Invariance clauses can be vacuous; change clauses cannot

> L124 | variable under edits to the measuring relation;

> L125 | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

**Formal.** On C = {(1,b0)} no component is in any family (each family needs a 'changes' or 'variable' clause witnessed by a pair of C, I09). On a C with no Obs edit, Causal's second clause holds vacuously; with no world intervention, Rule's first clause does; with no intervention on m, Meas's first clause does.

**Type.** definition-consequence. S100 units: L123.s1, L124.s1, L125.s1. Round 1: what the L123 change may have disturbed: the C07 / C08–C09 asymmetry.

**Uses.** Inventions: I09. Formal core §4.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I09, I77, I78, I80. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC12 --scale 4 --time-cap 45`.

### FC13 · The families are patterns in (K), not additional data

> L127 | These are descriptions of patterns in (K), not additional data.

**Formal.** Causal_C(j), Meas_C(j,m) and Rule_C(j) are functions of D and C alone: of sig_C(j) and of how each edit of C is classed (a setting edit of a port, an observation edit, a rule edit, or none), a classification I04, I06 and I08 read off (A, L). Under I04's alternative (a), a declared asg, the classification needs data beyond D and C.

**Type.** strong candidate; definition-consequence. S100 unit: L127.s1.

**Uses.** Inventions: I04, I06, I08, I09. Formal core §4.

**Look.** Whether any reading of 'observation edit' needs a declared measured port (then it is additional data).

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 holds by construction). Rests on: I04, I06, I08, I09, I70, I77, I78. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC13 --scale 4 --time-cap 45`.

### FC14 · No definition asks whether a component 'is' a cause

> L127 | The semantics never asks whether a component "is" a cause. It asks what its signature is.

**Formal.** Syntactic: no definition of the formal core takes a predicate 'is a cause' as an argument; the component-level predicates are sig_C, ~_C and the family predicates, each a function of D and C (FC13).

**Type.** strong candidate; definition-consequence. S100 units: L127.s2, L127.s3.

**Uses.** Inventions: none. Formal core §4, §18.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: no invention. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC14 --scale 4 --time-cap 45`.

## B. Questions, transports, fidelity, account

### FC15 · τ[C] is a contract of the candidate's organization

> L141 | it contains the baseline \((1,b_0)\).

> L242 | \tau(1)=1

> L554 | has a signature on \(\tau[C]\)

**Formal.** If τ(1) = 1 and τ, σ map into A_E, B_E, then τ[C] ⊆ A_E × B_E and (1, σ(b0)) ∈ τ[C]: τ[C] is a contract of E with baseline σ(b0), as far as a contract is a set of pairs holding the baseline.

**Type.** definition-consequence. S100 unit: L113.s1. Round 1: matter 1: (K) applied beyond components (L119, L554–L556).

**Uses.** Inventions: I12, I18. Formal core §5.

**Look.** If τ is partial (I17), τ[C] is defined only when t translates every pair of C.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I12, I18, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC15 --scale 4 --time-cap 45`.

### FC16 · Reading a candidate's components through the transport agrees with (K) on τ[C]

> L119 | their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection

**Formal.** For k, k' in one candidate E and a footprint bijection β: the signatures of k and k' read on C through t coincide under β ⟺ k ~_{τ[C]} k' under β by (K), since (a,b) ↦ (τ(a),σ(b)) maps C onto τ[C].

**Type.** definition-consequence. S100 unit: L115.s1. Round 1: matter 1: (K) applied beyond components (L119, L554–L556).

**Uses.** Inventions: I10, I12. Formal core §4, §5.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I10, I12, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC16 --scale 4 --time-cap 45`.

### FC17 · Argument 1: (F1) makes each commitment's signature its counterpart's

> L554 | **Claim.** If a transport meets (F1) on \(C\), no active component \(k\) of \(E\) has a signature on \(\tau[C]\) that differs from the one its counterpart \(\lambda(k)\) has on \(C\), up to the port translation.

> L556 | (F1) equates the third coordinates pointwise.

> L245 | By (K), no component of \(E\) whose signature on \(C\) differs from its counterpart's meets (F1)

**Formal.** F1_C(ℰ) ⇒ ∀k∈Γ ∀(a,b)∈C: L_k(τ(a),σ(b)) = proj^λ_{V_k} Sol_{λ(k)}(a,b); that is, the signature of k read on C through t equals sig_C(λ(k),θ_k) (I13) as functions on C.

**Type.** stated result. S100 unit: L546.s1. Round 1: matter 1: (K) applied beyond components (L119, L554–L556).

**Uses.** Inventions: I12, I13, I14, I15. Formal core §4, §5.

**Look.** With the triples of L556 compared as sets (I12's third alternative), the two signatures are indexed by different pairs and meet only through τ×σ.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I12, I13, I14, I15, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC17 --scale 4 --time-cap 45`.

### FC18 · Argument 1's Consequence: a same-kind condition adds nothing; no third case

> L558 | A condition "each component's counterpart must be a component of the same kind" adds nothing to (F1) on any contract.

> L558 | The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case.

> L281 | There is no third case.

**Formal.** SameKind_C(ℰ) := for every k in Γ, the signature of k read through t and sig_C(λ(k),θ_k) coincide under a footprint bijection (I10). Claim: F1_C(ℰ) ⇒ SameKind_C(ℰ), so Acc(ℰ) ⟺ Acc(ℰ) ∧ SameKind_C(ℰ) for every ℰ and C.

**Type.** stated result.

**Uses.** Inventions: I10, I13, I14. Formal core §4, §5.

**Look.** With value maps that are not identities (I14) and kinds compared between equal domains (I10), (F1) can hold while SameKind fails: E's port domains differ from D's. Then the Consequence needs I10's value-bijection alternative.

**Search result (S104).** COUNTEREXAMPLE FOUND (1 holds on all models tried; 1 counterexample found). Rests on: I10, I13, I14, I77, I78, I81, I94. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC18 --scale 4 --time-cap 45`.

### FC19 · (F1) and (F2) do different work

> L245 | (F1) prevents an assembled match from hiding a decomposition in error. (F2) prevents a set of pieces each faithful locally from hiding a lost shared constraint.

**Formal.** (a) There is ℰ with F2_C ∧ A_C ∧ ¬F1_C. (b) There is ℰ with F1_C ∧ ¬F2_C: two commitments each matching its counterpart, whose counterparts share a port of D that E's two components do not share.

**Type.** stated result.

**Uses.** Inventions: I14, I15. Formal core §5.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 witness found). Rests on: I14, I15, I77, I78, I81, I101. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC19 --scale 4 --time-cap 45`.

### FC20 · When (F2) at a pair gives (A) at that pair (violation in either extent)

> L219 | - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);

> L220 | - a **violation** occurs when fidelity fails at \((a,b)\);

> L250 | \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A}

**Formal.** If Q reads a port w of the target, δ_E designates a port w' of E, and π(z)_{w'} = κ(z_w) for every z (π acts on the designated port as a value map κ), then the valuation equation of (F2) at (a,b) gives Ans_E(τ(a),σ(b)) = κ(Ans_p(a,b)); with κ the identity this is (A) at (a,b). Without that condition on π, (F2) at a pair does not give (A) there. Violation and Violation⁺ (I50) coincide exactly where it does.

**Type.** definition-consequence. S100 units: L219.s1, L220.s1. Round 1: matter 12: the narrow and wide senses of 'fidelity' (the C18 ruling's argument).

**Uses.** Inventions: I16, I20, I21, I49, I50. Formal core §5, §12.

**Look.** Whether the simulation layer's queries (L177: 'what a port of P will take') always meet the condition on π.

**Search result (S104).** COUNTEREXAMPLE FOUND (1 counterexample found; 2 holds on all models tried). Rests on: I14, I16, I20, I21, I49, I50, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC20 --scale 4 --time-cap 45`.

### FC21 · A contract of relabelings admits no candidate meeting (A) and non-circular dependence

> L257 | A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets non-circular dependence

**Formal.** (a) If every edit of C is a relabeling for p (I26), then for every ℰ with A_C(ℰ) and τ(1) = 1: ¬NC2(ℰ). (b) Without (A) the implication can fail: a candidate whose own answers vary over τ[C] can meet NC2 on a contract of relabelings. (c) 'Excluding every change under which the active commitments could matter to Q' is ¬NC2 for every candidate, by NC2's definition.

**Type.** stated result.

**Uses.** Inventions: I21, I22, I26. Formal core §6.

**Look.** The sentence says 'admits no candidate'; on this formalization it holds of candidates that meet (A), which suffices for 'not a contract on which an account can be claimed'.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 witness found; 1 holds by construction). Rests on: I21, I22, I26, I77, I78, I81, I85, I101. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC21 --scale 4 --time-cap 45`.

### FC22 · The baseline alone gives no contrast

> L141 | it contains the baseline \((1,b_0)\).

> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that

**Formal.** If C = {(1,b0)} and τ(1) = 1 then ¬NC2(ℰ) for every ℰ: the only pair compares the baseline with itself, and neither disjunct of the contrast holds.

**Type.** definition-consequence.

**Uses.** Inventions: I21, I22. Formal core §6.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I21, I22, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC22 --scale 4 --time-cap 45`.

### FC23 · 'p because p' fails non-circular dependence through NC1 only

> L273 | "\(p\) because \(p\)" fails non-circular dependence.

**Formal.** Let E_lk have Γ = {k}, L_k(τ(a),σ(b)) the answer slot for Ans_p(a,b) (I24), and no other component constraining the answer ports. (a) NC1 fails for E_lk. (b) If Ans_p is not constant on C, NC2 holds for E_lk with G = {k}: after deleting k the answer is ⊥ at both points, so an answer E_lk determined is no longer determined. So E_lk fails non-circular dependence through NC1 only; under I24's alternative (a), NC2 alone, E_lk meets non-circular dependence.

**Type.** strong candidate; stated result. S100 unit: L273.s1.

**Uses.** Inventions: I21, I22, I24, I25. Formal core §6.

**Look.** If this stands, the one formal clause of non-circular dependence (NC2) does not exclude the lookup; the exclusion rests on NC1, the least formal clause.

**Search result (S104).** COUNTEREXAMPLE FOUND (2 holds on all models tried; 1 counterexample found). Rests on: I21, I22, I24, I25, I77, I78, I79, I81, I82, I83. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC23 --scale 4 --time-cap 45`.

### FC24 · L273's second sentence uses 'account' for a candidate

> L273 | So does an account whose only substantive component restates the answer it was asked for; packaging a dependence that answers a different question beside it does not repair this.

**Formal.** No ℰ has Acc(ℰ) ∧ ¬NonCircular(ℰ), by (E); so 'an account' in this sentence is a candidate offered as an account (L69's 'a theory in error offered as an answer is an explanatory candidate'). Adding to Γ a component answering another question leaves the answer slot in place, so NC1 still fails (I24); FC23's remark on NC2 applies unchanged.

**Type.** definition-consequence. Round 1: matter 7: L273's second sentence.

**Uses.** Inventions: I24. Formal core §6.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 not tested). Rests on: I24, I77, I78, I79, I81, I83. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC24 --scale 4 --time-cap 45`.

### FC25 · Tables: a fixed table fails (F1) where the projection moves; an encoding table meets it

> L269 | A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing one.

> L269 | A table that encodes an organization's response to every admitted change is not a table in that sense: it meets (F1) as a decomposition does, and it is an account when it meets the other conjuncts of (E).

**Formal.** (a) E_tab (I32): F1 at (a,b) ⟺ the projection of Sol_D(a,b) on the table's ports equals that of Sol_D(1,b0). So E_tab fails (F1) under C exactly when C holds a pair at which that projection moves; a setting edit that leaves it unchanged (a port set to its baseline value, or a port the table's ports do not depend on) does not make it fail. (b) E_enc, with L_k(τ(a),σ(b)) := that projection at (a,b), meets (F1) on every C.

**Type.** stated result.

**Uses.** Inventions: I03, I04, I14, I32. Formal core §6, §17.

**Look.** Whether 'fails (F1) under any contract containing one' needs 'one that moves what the table records'.

**Search result (S104).** COUNTEREXAMPLE FOUND (2 holds on all models tried; 1 witness found; 1 counterexample found). Rests on: I03, I04, I14, I32, I77, I78, I80, I101. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC25 --scale 4 --time-cap 45`.

### FC26 · The pole: the forward organization meets (E) on the production contract

> L325 | The forward organization is faithful under this contract.

**Formal.** With I65: E_fwd = D_pole with the identity transport and Γ = {c_H, c_θ, c_L} meets (F1), (F2), (A), NC1, NC2 and non-vacuity (with a scope statement) on C1 = settings of H and θ, and on C2 = C1 plus settings of L; Q reads L.

**Type.** stated result.

**Uses.** Inventions: I04, I20, I21, I24, I27, I65. Formal core §6, §17.

**Look.** On a contract whose only non-baseline edits set L, c_L is an answer slot at every such pair (its relation becomes 'L = l', the target's answer), so NC1 would fail for the forward organization there.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 computed: as claimed; 1 look: not as expected). Rests on: I04, I20, I21, I24, I27, I65, I79, I85, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC26 --scale 4 --time-cap 45`.

### FC27 · The pole: the reversed calculation fails (F2) on the production contract

> L271 | A **reversed calculation**, identification presented as production, fails (F2) under the production contract: intervening on the upstream port changes the target's downstream value but not the calculation's.

> L325 | The reversed calculation \(H=L\tan\theta\) is not: intervening on \(H\) changes the target's \(L\) but not the calculation's \(L\).

**Formal.** E_rev: components c'_L (L = the observed value, from the boundary), c'_θ, c'_H (H = L tan θ); τ(set H := h) = set H := h. At (set H := h, b) with h ≠ u_H: π[Sol_D] has L = h cot θ, Sol_E_rev has L = u_H cot θ. (F2) fails there.

**Type.** stated result.

**Uses.** Inventions: I04, I65. Formal core §17.

**Look.** Which edit τ gives E_rev for 'set H' is a choice; with τ(set H) = 1 (F2) fails at the same pair for another reason.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I04, I65, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC27 --scale 4 --time-cap 45`.

### FC28 · The pole: the reversed calculation meets (F1), (F2), (A) on the identification contract

> L325 | It is faithful under the identification contract, whose edits alter the observed \(L\).

**Formal.** On I65's identification contract (boundaries varying u_H; Q the fibre {H : H cot θ = observed L}), E_rev with τ the identity and σ(b) the observed L meets (F1), (F2) and (A).

**Type.** stated result.

**Uses.** Inventions: I20, I65. Formal core §17.

**Look.** Rests wholly on I65's reading of 'edits that alter the observed L'. With edits that set L (replacing c_L), D's fibre over the set value is every H, and (A) fails for E_rev.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed; 1 look: not as expected). Rests on: I20, I65, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC28 --scale 4 --time-cap 45`.

### FC29 · A contrast no admitted edit realizes witnesses nothing

> L275 | A candidate whose only substantive contrast is one that no edit the target admits realizes has no pair of \(C\) at which the contrast appears, and fails non-circular dependence.

**Formal.** NC2 quantifies over pairs of C ⊆ A_D × B_D; a contrast of E at a pair of E that is the image of no pair of C witnesses nothing. If every contrast of E lies off τ[C], then ¬NC2.

**Type.** definition-consequence.

**Uses.** Inventions: I12. Formal core §6.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I12, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC29 --scale 4 --time-cap 45`.

### FC30 · (E) takes no assessor, history, provenance or wording

> L43 | Within any contract, whether a transport is faithful at a pair turns on the transport and the target, and no assessor appears in (E).

> L67 | Whether a transport is faithful on a contract is independent of whether anyone tentatively accepts it.

> L277 | (E) has no condition on how a mechanism came to be guessed: a mechanism meets (E) or fails it whatever led anyone to guess it

**Formal.** Acc(ℰ) is a function of (D, C, b0, Q, δ, E, t, Γ, Σ, ℓ) only (Σ the stated scope, I27; ℓ the grain, I28); it takes no assessor, no Accepted_j, no history and no provenance. Faithful_C(t) is a function of (D, E, t, C). Candidates alike in these arguments have the same Acc value, whatever else differs.

**Type.** definition-consequence.

**Uses.** Inventions: I20, I27, I28. Formal core §6.

**Look.** The stated scope Σ is a declared input; whether a declared input counts as 'the modeller' in L43's sense is left to L43 itself ('what the modeller chose to leave out lies in the stated scope').

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds by construction). Rests on: I20, I27, I28. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC30 --scale 4 --time-cap 45`.

### FC31 · 'The four conditions', five conjuncts, and L520's three sources

> L61 | (Suff) sufficiency of the four conditions of Account

> L231 | meets \(\operatorname{Account}(\mathcal E)\) exactly when the following four conditions are met

> L262 | \operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}. \tag{E}

> L536 | A candidate meeting all four conditions of (E)

> L520 | Account, from fidelity under change, non-circular dependence and non-vacuity (E).

**Formal.** (E) has five conjuncts; Part V has four headed conditions: Component fidelity = (F1) ∧ (F2), Question fidelity = (A), Non-circular dependence, Non-vacuity. 'The four conditions' at L61, L231 and L536 are the four headings. L520's three sources cover the four headings exactly when 'fidelity under change' has the wide extent Fid⁺ (I49); with the narrow extent L189 defines, L520 names no source for (A).

**Type.** definition-consequence. S100 unit: L520.s7. Round 1: round-1 change L520; what the L520 change may have disturbed: 'the four conditions' at L61, L231, L536.

**Uses.** Inventions: I49. Formal core §5, §6.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I49. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC31 --scale 4 --time-cap 45`.

### FC32 · L520 (after round 1) against L526's dependence order

> L526 | (F1), (F2), (A) depend on (O), (Q), (K). (E) depends on those.

> L526 | (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined.

> L520 | Account, from fidelity under change, non-circular dependence and non-vacuity (E).

**Formal.** In the formal core Acc uses (O), (Q), (K) (through F1), t, Γ, the stated scope Σ (a declared input), the grain ℓ (an index, in NC1) and the designation δ (I20). L526 gives (E) the ancestors (F1), (F2), (A) and 'those'; it names neither non-circular dependence nor non-vacuity, nor any index or declared input, among them. Test: is every argument of Acc an ancestor of (E) in L526's order?

**Type.** definition-consequence. S100 unit: L520.s7. Round 1: what the L520 change may have disturbed: L526's order.

**Uses.** Inventions: I20, I27, I28. Formal core §6, §18.

**Look.** Expected gaps: Σ, ℓ, δ, and the two conditions L520 now names.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I20, I27, I28. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC32 --scale 4 --time-cap 45`.

### FC33 · 'Every conjunct is a condition on supplied relations; none inspects a label'

> L265 | Every conjunct is a condition on how supplied relations behave under the changes in \(C\). None inspects a label.

**Formal.** (a) If E' is E with its components and ports renamed by bijections, with t, δ and Γ carried along, then Acc(ℰ') = Acc(ℰ). (b) Non-vacuity's scope clause (I27) is a condition on a declared statement, and Sol_D(1,b0) ≠ ∅ on the baseline only; NC1 is read at a grain (I28). So the first sentence holds, as written, of (F1), (F2), (A) and NC2.

**Type.** stated result.

**Uses.** Inventions: I24, I27, I28, I70. Formal core §6.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 not tested). Rests on: I24, I27, I28, I70, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC33 --scale 4 --time-cap 45`.

### FC34 · Two questions, one target: what 'an answer to one is not an answer to the other' allows

> L151 | Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other.

**Formal.** Narrow reading (I73): there are p, p' with the same D, (C,Q) ≠ (C',Q'), and ℰ with Acc on p and not on p'. Wide reading: no ℰ has Acc on both. Test the wide reading with C' ⊊ C and the same Q: if NC2's witness pair lies in C', NC1 holds on C' and Σ' states the scope of C', a candidate meeting (E) on C meets it on C'. (NC1 can fail on C' while holding on C: a component can coincide with the answer slot on the fewer pairs of C'.) Also: Acc is neither monotone nor antitone in C.

**Type.** stated result.

**Uses.** Inventions: I24, I27, I73. Formal core §3, §6.

**Look.** Expected: instances against the wide reading.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (5 witness found). Rests on: I24, I27, I73, I77, I78, I79, I81, I85, I101. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC34 --scale 4 --time-cap 45`.

### FC35 · 'Prediction' at L151 is outside L219's definition

> L151 | A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question

> L217 | Let \(t\) be a transport to the simulation layer \(S\)

**Formal.** L219 defines Pred for transports whose codomain is S (L217). L151 applies 'prediction' to a transport faithful on the contract with no codomain named. Under I51, Pred_t(a,b) := Ans_E(τ(a),σ(b)) for every t, and L151's use is covered; without it, L151's use lies outside the definition.

**Type.** definition-consequence. S100 unit: L219.s1. Round 1: matter 6: 'prediction' at L151.

**Uses.** Inventions: I51. Formal core §12.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I51. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC35 --scale 4 --time-cap 45`.

### FC36 · What a question asks is fixed by the query and the contract, not by a label

> L151 | What a question asks, production, identification, obstruction, rule-status or purpose-achievement, is fixed by the type of \(\mathcal Q\) and the shape of \(C\), not by a label.

**Formal.** Under I72, Prod(p), Ident(p), Obst(p) are functions of (D, Q, δ, C) and are unchanged by renaming ports and components (δ carried along). They need not exclude one another (a query can read an output port and also compute a fibre) and do not cover rule-status and purpose-achievement.

**Type.** stated result.

**Uses.** Inventions: I72. Formal core §3.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed; 1 holds by construction). Rests on: I72. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC36 --scale 4 --time-cap 45`.

## C. Part VI: routes, conflict, rivals, problems

### FC37 · The finite monotone claim

> L305 | **Finite monotone claim.** If \(\Gamma\) is finite, \(\mathsf S\) is upward closed, and \(\Gamma\in\mathsf S\), then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\), and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\), exactly when \(d\in\bigcap\min\mathsf S\).

**Formal.** For every finite Γ and every upward-closed S ⊆ P(Γ) with Γ ∈ S: (∃W∈S: CB({d};W)) ⟺ d ∈ ∪min S, and Γ∖{d} ∉ S ⟺ d ∈ ∩min S. Testable on every upward-closed family over |Γ| ≤ 5.

**Type.** stated result. S100 unit: L546.s1.

**Uses.** Inventions: none. Formal core §7.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 holds on all models tried). Rests on: I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC37 --scale 4 --time-cap 45`.

### FC38 · Redundant routes

> L307 | **Redundant routes.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\},\{b\},\{a,b\}\}\): each is contributory, neither indispensable.

**Formal.** S = {{a},{b},{a,b}} is upward closed with min S = {{a},{b}}: a and b are contributory, neither is globally indispensable.

**Type.** stated result.

**Uses.** Inventions: I30. Formal core §7.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I30. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC38 --scale 4 --time-cap 45`.

### FC39 · Interference

> L309 | **Interference.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\}\}\): the full candidate fails (E) although a subset meets it.

> L305 | an addition to \(\Gamma\) that stops a route being one is the interference case below, and there upward closure fails.

**Formal.** S = {{a}}: Γ ∉ S, {a} ∈ S, S is not upward closed, so the finite monotone claim's hypotheses fail; {a} is critical in {a}.

**Type.** definition-consequence.

**Uses.** Inventions: I30. Formal core §7.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I30. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC39 --scale 4 --time-cap 45`.

### FC40 · Infinitary routes: collective criticality, and the step the first sentence leaves unsaid

> L311 | every set of indices unbounded in \(\mathbb N\) determines \(x=0\); no minimal route, and no route of one commitment, exists.

> L311 | (B) records the collective contribution.

> L313 | When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary routes).

**Formal.** With I31: (a) S is upward closed, Γ ∈ S, min S = ∅, no member of S has one element. (b) For W ∈ S and nonempty B ⊆ W: CB(B;W) ⟺ the index set of W∖B is bounded; every critical block is infinite, and critical blocks exist (B = W). (c) Each d_n does no work by itself (L313): for W ∈ S, W ∪ {d_n} ∈ S and W ∖ {d_n} ∈ S. (d) So L313's last sentence has an instance here. Step (c) is the one L311's first sentence does not say in words.

**Type.** strong candidate; stated result. S100 unit: L311.s2. Round 1: matter 8: L311's first sentence; the second sentences of L311 and L273.

**Uses.** Inventions: I30, I31. Formal core §7.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I30, I31, I91. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC40 --scale 4 --time-cap 45`.

### FC41 · Commitments that do no work, and why 'when Γ is infinite'

> L313 | A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it: a candidate carrying \(d\) then meets (E) exactly when it meets (E) without \(d\), and \(\{d\}\) is critical in no route (B).

**Formal.** NoWork(d) := S ≠ ∅ ∧ ∀W∈S (W∪{d} ∈ S ∧ W∖{d} ∈ S). Then (a) for every W ⊆ Γ: W∪{d} ∈ S ⟺ W∖{d} ∈ S; (b) {d} is critical in no route; (c) a finite block every member of which does no work by itself is critical in no route, so the 'when Γ is infinite' of L313's last sentence cannot be dropped.

**Type.** stated result.

**Uses.** Inventions: I29. Formal core §7.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I29, I77. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC41 --scale 4 --time-cap 45`.

### FC42 · Criticality is relative to the route

> L299 | A block may be critical while no singleton in it is. Criticality is relative to the route \(W\) it is assessed in

> L299 | a commitment critical in one route need not be critical in the full candidate

**Formal.** (a) In Redundant routes, B = W = {a,b} is critical (W∖B = ∅ ∉ S) and neither singleton is. (b) There, a is critical in {a} and not in {a,b}.

**Type.** definition-consequence.

**Uses.** Inventions: I30. Formal core §7.

**Look.** (a) needs ∅ ∉ S.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I30. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC42 --scale 4 --time-cap 45`.

### FC43 · Conflict, rivals, problems and 'easy to vary' are symmetric

> L317 | the rival is then easy to vary too

**Formal.** Conf(ℰ,ℰ';a,b) ⟺ Conf(ℰ',ℰ;a,b); Riv is symmetric (either offered in place of the other, I33); so Prob_j and its kind are symmetric, and ETV_j(ℰ) through ℰ' gives ETV_j(ℰ').

**Type.** stated result.

**Uses.** Inventions: I33, I37. Formal core §8, §10.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I33, I37, I77, I78, I81, I86. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC43 --scale 4 --time-cap 45`.

### FC44 · Two commitments with one counterpart and different relations cannot both meet (F1)

> L315 | as none do when two of their active components with one counterpart have different relations there.

**Formal.** Under I36: if k ∈ Γ and k' ∈ Γ' have one counterpart and different relations at (a,b), then no R gives F1_ab(ℰ,R) ∧ F1_ab(ℰ',R). Under the reading 'one counterpart = the same subnetwork', there are ℰ, ℰ', R meeting both with different relations.

**Type.** stated result.

**Uses.** Inventions: I14, I19, I36. Formal core §8.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 witness found). Rests on: I14, I19, I36, I77, I78, I81, I101. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC44 --scale 4 --time-cap 45`.

### FC45 · Recoded candidates, and candidates some relations let both meet, conflict nowhere

> L315 | Two candidates that differ only in how they are written, one carried onto the other by a structure-preserving bijection that takes its transport with it and leaves its answers as they are, conflict at no pair

**Formal.** (a) If φ: E ≅ E' with t' = φ∘t, Γ' = φ[Γ] and Ans_E'(φa',φb') = Ans_E(a',b'), then ¬Conf(ℰ,ℰ';a,b) at every pair both translate. (b) If at every such pair some R lets both meet, they conflict nowhere.

**Type.** stated result.

**Uses.** Inventions: I17, I19, I20, I70. Formal core §8.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 holds by construction). Rests on: I17, I19, I20, I70, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC45 --scale 4 --time-cap 45`.

### FC46 · A conflict inside the contract: at most one account

> L317 | (i) The rivals conflict at some \((a,b)\in C\). Whatever the target does there, at most one of them is an account of \(p\), whether or not anyone records what it does;

> L317 | Two rivals that are both accounts on \(C\) conflict only outside it

**Formal.** ∀ℰ,ℰ' ∀(a,b)∈C: Conf(ℰ,ℰ';a,b) ⇒ ¬(Acc(ℰ) ∧ Acc(ℰ')). (If both met (E), both would meet (F1), the (F2) equation and (A) at (a,b) under the target's own relations R*: equal answers, and R* lets both.) So two accounts on C conflict at no pair of C.

**Type.** stated result.

**Uses.** Inventions: I19, I21. Formal core §8, §10.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I19, I21, I77, I78, I81, I85. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC46 --scale 4 --time-cap 45`.

### FC47 · A test at a conflict pair rules out at least one, for an assessor who can use it

> L317 | recording it, the target's relations as well as its answer where their answers there agree, is a **test**. Whatever it records, an argument from what it records rules out at least one of them for an assessor who can use it

**Formal.** (a) Conf(ℰ,ℰ';a,b) ⇒ ∀R ¬(Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R)); so for the recorded R*, Meets_ab fails for at least one. (b) For j who admits the forms used, whose scope holds (a,b), and for whom the record's premises about background and instruments are live, the argument 'R* at (a,b); Meets_ab(·,R*) fails; Acc requires it' puts a member in X_j(Acc(ℰ)) or in X_j(Acc(ℰ')).

**Type.** stated result.

**Uses.** Inventions: I19, I38, I40, I42, I43. Formal core §8, §9, §10.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 computed: as claimed). Rests on: I19, I38, I40, I42, I43, I77, I78, I81, I87, I88, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC47 --scale 4 --time-cap 45`.

### FC48 · No conflict inside the contract: answers agree there

> L317 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict. Their answers then agree at every pair of \(C\), so no argument from an answer recorded in \(C\) rules out one of them without the other;

**Formal.** If ¬Conf(ℰ,ℰ';a,b) at every (a,b) ∈ C, then Ans_E(τa,σb) = Ans_E'(τ'a,σ'b) at every (a,b) ∈ C (⊥ = ⊥, I21); so for any recorded answer at (a,b), (A) there holds for both or for neither.

**Type.** stated result.

**Uses.** Inventions: I21. Formal core §8, §10.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I21, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC48 --scale 4 --time-cap 45`.

### FC49 · The two kinds of problem exclude each other and cover every pair of rivals

> L317 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it

**Formal.** Riv(ℰ,ℰ';p) ⇒ exactly one of: some pair of C is a conflict pair; no pair of C is, and some translated pair outside C is.

**Type.** definition-consequence.

**Uses.** Inventions: I16, I17, I33. Formal core §10.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I16, I17, I33, I77, I78, I81, I86. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC49 --scale 4 --time-cap 45`.

### FC50 · A finer contract makes a problem of the first kind; a narrowed one leaves the problem on p

> L317 | A finer contract that contains a change at which two rivals conflict makes a new question (Part III), on which, offered for it, they pose a problem of the first kind while neither is ruled out;

> L317 | A contract narrowed to leave out the pairs at which two rivals conflict also makes a different question; it solves nothing on \(p\), and the problem for \(p\) remains until at least one of them is ruled out for that assessor.

**Formal.** (a) If Conf(ℰ,ℰ';a,b) with (a,b) ∉ C, p' is p with C' ⊇ C ∪ {(a,b)}, and ℰ, ℰ' are offered for p' with neither ruled out for j, then Prob_j(ℰ,ℰ';p') is of the first kind. (b) For C'' ⊆ C leaving out every conflict pair, p'' ≠ p, and Prob_j(ℰ,ℰ';p) is a function of p's data and j alone, unchanged by anything about p''.

**Type.** stated result.

**Uses.** Inventions: I11, I33. Formal core §10.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 holds by construction). Rests on: I11, I33, I77, I78, I81, I86. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC50 --scale 4 --time-cap 45`.

### FC51 · A change that separates two accounts lies outside their shared contract

> L317 | a claim that one of them and not the other meets (E) on a contract with some admitted change outside \(C\) is a claim that such a change separates them, and must supply it

> L568 | Where two candidates that meet (F1), (F2) and (A) differ only in which component has which counterpart, the contract does not contain the distinction

**Formal.** (a) If Acc(ℰ) and Acc(ℰ') on C, C' ⊋ C, Acc(ℰ) on C' and ¬Acc(ℰ') on C', then some (a,b) ∈ C'∖C has ¬(F1 ∧ (F2) equation ∧ A)_ab(ℰ'), or τ' fails the homomorphism clause on edits new in C', or the scope statements differ (NC1 and NC2 carry over from C to C'; Sol_D(1,b0) is unchanged). (b) If ℰ' is ℰ with λ' = λ∘ψ for a permutation ψ of Γ and both meet (F1) on C, then for every k and (a,b) ∈ C the projected relations of λ(k) and λ(ψk) agree under the port translations: no pair of C separates the two pairings.

**Type.** stated result.

**Uses.** Inventions: I18, I24, I27. Formal core §6, §8.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 holds on all models tried). Rests on: I18, I24, I27, I77, I78, I81, I85. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC51 --scale 4 --time-cap 45`.

### FC52 · Conflict with a claim: the first disjunct implies the second

> L315 | when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there.

**Formal.** Under I34: if χ excludes ℰ's answer at (a,b), then χ excludes every R with Meets_ab(ℰ,R) (Meets includes (A) at the pair, so the answer under such R is ℰ's answer). The definition reduces to its second disjunct.

**Type.** definition-consequence.

**Uses.** Inventions: I19, I34. Formal core §8.

**Look.** Under I34's alternative (χ constrains answers only), the second disjunct cannot be written and the first is the whole definition.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I19, I34, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC52 --scale 4 --time-cap 45`.

### FC53 · Conflict with a claim rules a candidate out only with the premise that the claim speaks of the target

> L315 | Where the pair is in \(C\), that argument rules out that the candidate meets (E) for any assessor \(j\) who can use it, and so who tentatively accepts \(\chi\) (K2)

> L315 | Either way the argument needs the premise that \(\chi\) speaks of the target under that pair's edit.

> L315 | without that premise the argument rules out no candidate there; the candidate still conflicts with \(\chi\).

**Formal.** (a) If ConfCl(ℰ,χ;a,b), (a,b) ∈ C, Applies(χ,a,b), χ and Applies live for j, forms admitted: X_j(Acc(ℰ)) ≠ ∅. (b) There is a model (the text's pendulum, its friction component deleted by the edit) with ConfCl(ℰ,χ;a,b), ¬Applies(χ,a,b), and no argument from χ in X_j(Acc(ℰ)).

**Type.** stated result.

**Uses.** Inventions: I34, I38, I40. Formal core §8, §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 computed: as claimed). Rests on: I34, I38, I40, I87, I88, I89, I90. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC53 --scale 4 --time-cap 45`.

### FC54 · Rivals given χ conflict nowhere without χ at that pair

> L315 | Two candidates offered one in place of the other that conflict at a pair given \(\chi\) are **rivals given \(\chi\)**: for an assessor who tentatively accepts \(\chi\) they pose a problem for \(p\) as rivals do (Problems, below), and for one who does not, they pose none on that account.

**Formal.** Riv_χ(ℰ,ℰ';p) := Offered ∧ ∃(a,b) ConfG_χ(ℰ,ℰ';a,b); Prob_{χ,j} := Riv_χ ∧ χ ∈ Accepted_j ∧ neither ruled out for j. Claim: ConfG_χ(a,b) ⇒ ¬Conf(a,b) (some R lets both meet, so their answers agree and the second disjunct of Conf fails). So a pair of rivals given χ that conflicts at no other pair is not a pair of rivals.

**Type.** definition-consequence.

**Uses.** Inventions: I19, I33, I34, I35. Formal core §8, §10.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I19, I33, I34, I35, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC54 --scale 4 --time-cap 45`.

### FC55 · Nothing in Part VI counts rivals or orders candidates

> L317 | Nothing here counts rivals or orders candidates: of one candidate, what is said is whether it meets (E) on a contract and whether it is ruled out for an assessor; of two, whether they conflict; of a candidate and a claim, whether they conflict.

**Formal.** Syntactic: every predicate of §§8–10 takes at most two candidates, or one candidate and one claim; none takes a set of candidates, a cardinality or an order on candidates.

**Type.** definition-consequence.

**Uses.** Inventions: none. Formal core §8, §10.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: no invention. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC55 --scale 4 --time-cap 45`.

### FC56 · Ruling out grows with what is accepted; withdrawal rules nothing out; absence rules out nothing

> L393 | Withdrawing a premise makes the step unusable; it does not rule the conclusion out.

> L397 | Where no argument usable by \(j\) rules out \(\phi\), that absence rules out nothing, neither \(\phi\) nor \(\neg\phi\).

**Formal.** (a) Usable_j and X_j(φ) are monotone in Accepted_j, in Forms_j and in the contracts j declares (grain and boundary held fixed): enlarging any of them never makes an argument unusable; RO does not depend on j. So withdrawing a premise adds no member to any X_j(φ): it rules out nothing not already ruled out. (b) There are j and φ with X_j(φ) = ∅ = X_j(¬φ).

**Type.** strong candidate; definition-consequence. S100 units: L393.s4, L389.s1.

**Uses.** Inventions: I38, I40, I41. Formal core §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 computed: as claimed). Rests on: I38, I40, I41, I87, I88, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC56 --scale 4 --time-cap 45`.

## D. Parts VII and VIII: exact constructions and transport results

### FC57 · (I2): identified at every attainable value exactly when the feature factors through the measurement

> L329 | It is identified on every attainable \(y\) exactly when \(f=\bar f\circ g\) for some \(\bar f\).

**Formal.** (∀y ∈ g[Z]: |f[Z_y]| = 1) ⟺ ∃f̄: Y → F with f = f̄∘g on Z.

**Type.** stated result. S100 unit: L546.s1.

**Uses.** Inventions: I63, I64. Formal core §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I63, I64, I77. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC57 --scale 4 --time-cap 45`.

### FC58 · (I3): the kernel criterion; repeated rows; an independent calibration

> L329 | For linear \(g\) and linear feature \(c^\top\), identification is \(\ker g\subseteq\ker c^\top\).

> L329 | Repeating rows changes no kernel; an independent calibration can.

**Formal.** Z = ℝ^n, g = G ∈ ℝ^{m×n}, feature c ∈ ℝ^n: (∀y ∈ G[ℝ^n]: |cᵀ[G⁻¹(y)]| = 1) ⟺ ker G ⊆ ker cᵀ. A row in the row space of G leaves ker G unchanged; a row outside it lowers dim ker G by one.

**Type.** stated result.

**Uses.** Inventions: I63, I64. Formal core §17.

**Look.** With Z a proper subset (I64's alternative), the criterion can fail.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 holds on all models tried; 1 look: as expected). Rests on: I63, I64, I77. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC58 --scale 4 --time-cap 45`.

### FC59 · The two balances

> L331 | the kernel is spanned by \((1,-1,-1)\); the readings identify \(b_B-b_A\) and not \(x\).

**Formal.** G = [[1,1,0],[1,0,1]] on (x, b_A, b_B): ker G = span{(1,−1,−1)}; c = (0,−1,1) gives c·(1,−1,−1) = 0 (identified); c = (1,0,0) gives 1 (not identified).

**Type.** stated result.

**Uses.** Inventions: I64. Formal core §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I64. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC59 --scale 4 --time-cap 45`.

### FC60 · Setting a bias from the favoured mass: where the circularity can be registered

> L331 | "Set \(b_B=0\) because it gives the mass I favour" is not an inference from the readings; it is circular, though the value it sets might be the target's.

**Formal.** (a) Two candidates with the boundary value b_B = 0, one set 'because it gives the mass I favour' and one set by an independent calibration, have the same (D, C, E, t, Γ, Σ), so the same Acc value (FC30): (E) does not register the circularity, and NC1 does not either, since the value 0 is not the answer (I24). (b) Where it can be registered is Part IX's block: an argument concluding x = m* whose premise b_B = 0 is a record MadeFrom the claim x = m* (I39) does not rule out x ≠ m* (D9.7). (c) Its value can equal the target's b_B, so (F1), (F2), (A) can hold at the baseline.

**Type.** stated result.

**Uses.** Inventions: I24, I39. Formal core §6, §9, §17.

**Look.** If (a) and (b) stand, L331's 'circular' is a matter of how an input was chosen (L277: '(E) has no condition on how a mechanism came to be guessed'), not of non-circular dependence.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds by construction; 1 computed: as claimed). Rests on: I24, I39, I87, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC60 --scale 4 --time-cap 45`.

### FC61 · (O1): an invariant blocks paths; equal values do not give paths; twenty-three tokens

> L335 | For allowed steps \(R\) and an invariant \(I\) with \(zRz'\Rightarrow I(z)=I(z')\), no allowed path joins states of different invariant value. (O1) Equal values do not suffice for reachability. Twenty-three indivisible tokens cannot be split equally three ways;

**Formal.** (a) If zRz' ⇒ I(z) = I(z'), then R* ⊆ {(z,z') : I(z) = I(z')}. (b) There are R, I, z, z' with I(z) = I(z') and not zR*z'. (c) Distributions (n1,n2,n3) of 23 whole tokens: an equal split needs 3n = 23, which has no whole solution.

**Type.** stated result. S100 unit: L546.s1.

**Uses.** Inventions: I63. Formal core §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 computed: as claimed). Rests on: I63, I77. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC61 --scale 4 --time-cap 45`.

### FC62 · Eliminative explanation: the rival's structure as a deleted counterpart

> L339 | An account is faithful when introducing those components changes the answer in \(E\) as it does in \(D\), and their absence leaves both unchanged. The rival's supposed structure has as its counterpart a *deleted* subnetwork, whose relation is full (Part II).

**Formal.** D with a component x whose baseline relation is full (I03) and an edit a_x giving it a relation; E with k, λ(k) = {x}, baseline relation full, τ(a_x) giving k the projected relation. F1 at (1,b0): full = full; at (a_x,b0): holds when τ(a_x) gives k that relation. On C = {(1,b0), (a_x,b0)}, E can meet (E) (NC2 with G = {k}) when the answer depends on x.

**Type.** stated result.

**Uses.** Inventions: I03, I14. Formal core §6, §17.

**Look.** Part XV lists this under (Nec) as a place where it may not be an account; the test can only say whether the formal conditions are met.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I03, I14, I78, I79. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC62 --scale 4 --time-cap 45`.

### FC63 · Odd-order skew-symmetric matrices

> L343 | Question: why is every odd-order real skew-symmetric matrix singular?

> L343 | Non-circular dependence is met: \(I_3\) is an instance under removal of skewness, and \(\begin{pmatrix}0&1\\-1&0\end{pmatrix}\) under removal of oddness.

> L343 | The expansion is an account.

**Formal.** (a) For every odd n and every n×n M over ℝ (or GF(p), p odd) with Mᵀ = −M: det M = 0. (b) det I3 = 1; det [[0,1],[−1,0]] = 1. (c) With I66, the Leibniz candidate meets (F1), (F2), (A), NC2 and non-vacuity (the scope statement naming the edits to field arithmetic and to the determinant–invertibility link).

**Type.** stated result.

**Uses.** Inventions: I03, I27, I66. Formal core §17.

**Search result (S104).** COUNTEREXAMPLE FOUND (3 computed: as claimed; 1 computed: not as claimed). Rests on: I03, I27, I66, I81, I82, I99. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC63 --scale 4 --time-cap 45`.

### FC64 · Functional transport

> L353 | If \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\), the same equation is met by every admitted finite composition with matching scopes.

**Formal.** If π∘S_a = T_a∘π for each generator a, then π∘S_{an}⋯S_{a1} = T_{an}⋯T_{a1}∘π for every finite word whose intermediate scopes match.

**Type.** stated result.

**Uses.** Inventions: none. Formal core §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I77. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC64 --scale 4 --time-cap 45`.

### FC65 · Relational transport: simulations compose

> L361 | Composition of relations preserves both directions when intermediate scopes agree.

**Formal.** If R ⊆ Z_D × Z_E is a forward simulation for τ and R' ⊆ Z_E × Z_F one for τ', then R;R' is a forward simulation for τ'∘τ; likewise backward; where the codomain of R lies in the domain of R'.

**Type.** stated result.

**Uses.** Inventions: none. Formal core §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I77. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC65 --scale 4 --time-cap 45`.

### FC66 · (T2): the accumulated bound, and none without a modulus

> L363 | meets the bound \(e_n\le\varepsilon\sum_{k<n}L^k\) whenever \(z,Sz,\dots,S^{n-1}z\) lie in that scope. (T2) Without a modulus, no accumulated bound follows.

**Formal.** (a) e_{k+1} ≤ ε + L·e_k for k < n, so e_n ≤ ε Σ_{k<n} L^k. (b) There are S, T, π, d with one-step discrepancy ≤ ε everywhere, T not Lipschitz, and e_2 larger than any given number.

**Type.** stated result. S100 unit: L546.s1.

**Uses.** Inventions: none. Formal core §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 computed: as claimed). Rests on: I77. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC66 --scale 4 --time-cap 45`.

### FC67 · A declared invertible recoding keeps the content

> L365 | A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing (Argument 8).

**Formal.** For an invertible recoding r of carrier values and a reader applying r⁻¹, the composite transport is faithful wherever the original was, and the carrier's provenance carries over (I54); so Rep is kept.

**Type.** stated result.

**Uses.** Inventions: I54, I70. Formal core §12, §18.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 holds by construction). Rests on: I54, I70, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC67 --scale 4 --time-cap 45`.

### FC68 · A failed answer stays failed

> L369 | Fix a question \(p\), a pair \((a,b)\in C\) and a value \(y\neq\operatorname{Ans}_p(a,b)\).

> L369 | and so on every question with the same target and query whose contract contains \((a,b)\).

> L369 | no candidate becomes an account by that (E).

**Formal.** (a) Ans_E(τa,σb) = y ≠ Ans_p(a,b) ⇒ ¬A_ab ⇒ ¬Acc on p, and on every p' with the same D, Q and δ whose contract holds (a,b). (b) If j has a usable argument ruling out 'Ans_p(a,b) = y', the premise 'Ans_E(τa,σb) = y' is live and the forms are admitted, then X_j(Acc(ℰ)) ≠ ∅ for every such ℰ alike. (c) If a premise of that argument stops being live, the ruling out lapses for all alike, and Acc(ℰ) is unchanged.

**Type.** stated result.

**Uses.** Inventions: I20, I38, I40, I41. Formal core §6, §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 computed: as claimed). Rests on: I20, I38, I40, I41, I77, I78, I81, I87, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC68 --scale 4 --time-cap 45`.

## E. Part IX: arguments, usability, bearing, reason use, active routes

### FC69 · (K2) is well founded; the loop read in S101 closes below the step

> L390 | \operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u). \tag{K2}

> L393 | \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\)

**Formal.** Under I40, Usable_j(u) is defined by recursion on height; the loop K2 → Live → a step's usability → K2 (S101) closes on steps strictly below u. Under I40's alternative (any step of the argument), there are arguments where the definition has two fixed points: a root u' concluding d with premise e, and a step u below it concluding e with premise d — both usable or both not.

**Type.** strong candidate; definition-consequence. S100 unit: L389.s1.

**Uses.** Inventions: I40. Formal core §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 computed: as claimed). Rests on: I40, I87, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC69 --scale 4 --time-cap 45`.

### FC70 · Withdrawing a premise that is live twice over leaves the step usable

> L393 | Withdrawing a premise makes the step unusable; it does not rule the conclusion out.

**Formal.** There is an argument with a step u and d ∈ Prem(u) such that d is also the conclusion of a usable step below u and d ∈ Accepted_j; after j withdraws d, Live_j(d;u) still holds through the first disjunct, and Usable_j(u) is unchanged. So the first clause holds of a premise live by acceptance only.

**Type.** strong candidate; definition-consequence. S100 unit: L393.s4. Round 1: matter 9: a premise that stays live twice over (L393).

**Uses.** Inventions: I40, I41. Formal core §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I40, I41, I87, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC70 --scale 4 --time-cap 45`.

### FC71 · (K3): a failed prediction rules out the conjunction, and nothing narrower

> L395 | For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\) rules out \(T\land B\land I\) together for \(j\), and nothing narrower. (K3)

**Formal.** (i) A usable argument concluding ¬O, a live conditional T∧B∧I ⇒ O and an admitted modus tollens give a usable argument ruling out T∧B∧I. (ii) From those premises alone no argument rules out T, B or I by itself: ¬O, (T∧B∧I ⇒ O) and T have a common model.

**Type.** stated result.

**Uses.** Inventions: I38, I43. Formal core §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 computed: as claimed). Rests on: I38, I43, I87, I88, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC71 --scale 4 --time-cap 45`.

### FC72 · The block on a premise that is the denial, and a premise taken as given

> L397 | An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone;

> L397 | a premise from which a step leads to the denial, as one does from \(r\) and "if \(r\), this candidate fails (E)", is a premise taken as given, and using it is the gamble above, not a circular argument.

**Formal.** (a) If ¬φ is a conjunct of a leaf (I39), then ¬RO(α,φ). (b) If a record leaf is MadeFrom ψ, then ¬RO(α,¬ψ). (c) The argument with leaves r and (r → ¬Acc(ℰ)) and one modus ponens step rules out Acc(ℰ): neither leaf has ¬Acc(ℰ) as a conjunct.

**Type.** definition-consequence.

**Uses.** Inventions: I38, I39. Formal core §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I38, I39, I87, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC72 --scale 4 --time-cap 45`.

### FC73 · Inconsistent accepted premises rule out a claim and its denial alike

> L397 | Where the premises \(j\) tentatively accepts are inconsistent, arguments from them can rule out, for \(j\), a claim and its denial alike;

**Formal.** There are j and φ with X_j(φ) ≠ ∅ and X_j(¬φ) ≠ ∅ (for example Accepted_j ⊇ {q, q → ¬φ, s, s → φ}, modus ponens admitted).

**Type.** stated result.

**Uses.** Inventions: I38. Formal core §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I38, I87, I89. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC73 --scale 4 --time-cap 45`.

### FC74 · A criticism occurrence can exist without bearing

> L383 | A criticism occurrence can exist when (K1) fails.

**Formal.** The data of a criticism (target z, alleged defect δ, premise g, connection, an occurrence in a history) are defined without Acc; so there are models with a criticism occurrence c and ¬Acc(ℰ_c), that is ¬Bearing(c,z,p).

**Type.** strong candidate; definition-consequence. S100 unit: L383.s1.

**Uses.** Inventions: I45. Formal core §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 witness found). Rests on: I45, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC74 --scale 4 --time-cap 45`.

### FC75 · Active routes: the excluded routes fail the definition's own clauses

> L375 | A route that started and did no work, or that was already at rest when the result occurred, is not active for that result; whether a route is active is read from the history, not from the result.

**Formal.** Under I46: (a) a route none of whose occurrences lies on a ≺_h-chain to r inside it fails the join clause; (b) a route whose value at r does not change when i's port is set across the declared contrasts fails the dependence clause; (c) activity is a function of (h, Org_ℓ(h), i, r, K), not of r's value alone.

**Type.** strong candidate; definition-consequence. S100 unit: L375.s2. Round 1: matter 11: the undefined phrases at L375 and L385.

**Uses.** Inventions: I44, I46. Formal core §11.

**Look.** A route that ran to completion early, whose product persists and feeds r, is joined to r; whether it is 'already at rest when the result occurred' is not fixed by the definition.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 computed: as claimed; 1 holds by construction; 1 look: as expected). Rests on: I44, I46, I95. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC75 --scale 4 --time-cap 45`.

### FC76 · Reason use gives neither bearing nor usability

> L385 | Using an objection does not give it bearing (K1) or make any argument from it usable (K2).

**Formal.** Under I47, UsesReason is defined without Acc and without Usable_j; there are models with UsesReason and ¬Bearing, and with UsesReason and no usable argument from the objection.

**Type.** strong candidate; definition-consequence. S100 unit: L385.s1. Round 1: matter 11: the undefined phrases at L375 and L385.

**Uses.** Inventions: I47. Formal core §9.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I47, I90, I95. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC76 --scale 4 --time-cap 45`.

## F. Parts IV and X–XIII: provenance, prediction, construction, repair, the physical module

### FC77 · Without a physical witness, selection is met by every transport

> L195 | The transport \(t\) is a member of \(\mathcal T\) that survived.

> L205 | in (R), \(\operatorname{Sel}(t)\) and \(\operatorname{Con}(t)\) abbreviate \(\operatorname{Sel}(t;\mathcal T,\mu,H)\) and \(\operatorname{Con}(t;h,e)\) for some such parameters

**Formal.** Read with no physical witness: for every t, Sel(t; {t}, id, ∅) holds (fidelity on ∅ is vacuous, and an empty history holds nothing that represents). Then (R) reduces to 'some faithful transport exists'. With I52, Sel needs a physical selection history; test which of I52's requirements block the trivial witness.

**Type.** definition-consequence.

**Uses.** Inventions: I48, I52. Formal core §12.

**Look.** Whether (R) keeps any content from 'selected' when the physical module is left open.

**Search result (S104).** COUNTEREXAMPLE FOUND (1 counterexample found; 1 holds on all models tried; 1 computed: as claimed). Rests on: I18, I48, I52, I77, I78, I81, I90. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC77 --scale 4 --time-cap 45`.

### FC78 · Exactly one of three provenances

> L193 | has exactly one of three provenances, determined by its history in the physical module:

> L201 | Construction may operate on selected material. Selection may continue to operate beneath construction.

**Formal.** Under I53, Sel(t) ∧ Con(t) is impossible and Dec(t) := ¬Sel ∧ ¬Con, so exactly one holds. Under I53's alternative there are histories with Sel on one part and Con on another. Per part (I54), exactly one holds of each part.

**Type.** stated result. S100 unit: L47.s2.

**Uses.** Inventions: I52, I53, I54. Formal core §12.

**Search result (S104).** COUNTEREXAMPLE FOUND (1 computed: not as claimed). Rests on: I52, I53, I54, I56, I90, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC78 --scale 4 --time-cap 45`.

### FC79 · Survival is how the transport got there; fidelity is what it is

> L41 | Whether that transport is faithful on changes it was never selected against turns on the transport and the target alone, not on whether it survived.

> L41 | Survival is how the transport got there; fidelity is what it is.

**Formal.** Faithful_C(t) is a function of (D, E, t, C); Sel(t;𝒯,μ,H) of (t, 𝒯, μ, H, the selection history). No clause of Faithful takes 𝒯, μ or H, so two transports alike in (D, E, t) have the same Faithful value on every C.

**Type.** strong candidate; definition-consequence. S100 unit: L41.s4.

**Uses.** Inventions: I49, I52. Formal core §5, §12.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds by construction). Rests on: I49, I52. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC79 --scale 4 --time-cap 45`.

### FC80 · Argument 3: underdetermination where the population leaves room

> L572 | the value of \(t\) at \((a,b)\) is underdetermined by \(H\): survival on \(H\) does not distinguish \(t\) from \(t'\) there.

> L574 | Where \(\mathcal T\) contains no such transport, \(H\) is silent on the value at \((a,b)\) and the population fixes it.

**Formal.** (a) If t, t' ∈ 𝒯 both survive on H and value_t(a,b) ≠ value_t'(a,b) (I71) for (a,b) ∈ C∖H, the survival condition does not separate them. (b) If all survivors on H agree at (a,b), that value is a function of (𝒯, H). (c) The step 'altered at one pair gives another admitted relation' uses I02; under an action law, an alteration at one pair can force others, and (a)'s hypothesis is harder to meet.

**Type.** stated result. S100 unit: L546.s1.

**Uses.** Inventions: I02, I52, I71. Formal core §12.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 witness found; 1 not tested). Rests on: I02, I52, I71, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC80 --scale 4 --time-cap 45`.

### FC81 · Argument 4, and who can be surprised

> L580 | **Claim.** A system can be surprised only if it holds a transport selected on a history \(H\) strictly smaller than its contract \(C\).

> L223 | A system with no transport cannot be surprised. A system whose history exhausts its contract cannot be surprised.

> L223 | a constructed one that fails at an actually occurring pair of its contract is violated, and the failure is not surprise

**Formal.** Surp(t;a,b) := Sel(t) ∧ Viol(t;a,b) ∧ (a,b) ∈ C∖H ∧ Occurs(a,b). (a) Surp ⇒ H ⊊ C. (b) No transport ⇒ no Surp. (c) H = C ⇒ no Surp. (d) Con(t) ∧ Viol ⇒ ¬Surp (I53).

**Type.** stated result. S100 unit: L217.s2.

**Uses.** Inventions: I50, I52, I53. Formal core §12.

**Search result (S104).** COUNTEREXAMPLE FOUND (1 holds by construction; 1 computed: not as claimed). Rests on: I50, I52, I53, I56, I90, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC81 --scale 4 --time-cap 45`.

### FC82 · The two responses to a violation have no common result

> L225 | A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace.

**Formal.** SelResp(t → t'): t' ∈ 𝒯, reached from t by μ, surviving on H ∪ {(a,b)}; ConResp(→ t''): t'' or its codomain new, with Con(t''). Under I53 no transport is the result of both (Sel(t') excludes Con(t')).

**Type.** strong candidate; definition-consequence. S100 unit: L225.s1.

**Uses.** Inventions: I52, I53. Formal core §12.

**Search result (S104).** COUNTEREXAMPLE FOUND (1 computed: not as claimed). Rests on: I52, I53, I56, I90, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC82 --scale 4 --time-cap 45`.

### FC83 · Only the construction response can be originative

> L225 | Only the second can be originative under Part X.

**Formal.** Claim to test: SelResp(t → t') ⇒ ¬Origin(s,c',p,h,e) for the content c' that t' carries to. (G) needs Build, and Build needs a subhistory that prepares a represented organization for explanatory use of c' (I56). Sel(t') forbids occurrences that represent t', H or the survival condition (L195), not the organization t' carries to (which Con names, L197).

**Type.** strong candidate; stated result. S100 unit: L225.s4.

**Uses.** Inventions: I52, I56. Formal core §12, §13.

**Look.** The claim follows only if preparing a represented organization for c' needs t' represented, or if Build excludes subhistories that are selection histories.

**Search result (S104).** COUNTEREXAMPLE FOUND (1 computed: not as claimed). Rests on: I52, I56, I90, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC83 --scale 4 --time-cap 45`.

### FC84 · Every creative attribution requires construction

> L47 | Construction is a separate provenance with a separate trace, and every creative attribution requires it.

**Formal.** Origin ⇒ Build; CreateEx ⇒ Origin ⇒ Build; the creative-episode class (L528) needs an instance of (G), hence Build; Build's subhistory is what a construction trace identifies (L405). Separate traces: Sel's history holds no represented target (L195), Con's holds one (L197).

**Type.** strong candidate; definition-consequence. S100 unit: L47.s2.

**Uses.** Inventions: I53, I56. Formal core §12, §13, §14.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds by construction). Rests on: I53, I56. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC84 --scale 4 --time-cap 45`.

### FC85 · A content matches itself; the matching is read one way

> L413 | Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\).

> L416 | \operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c. \tag{N}

**Formal.** Under I48: (a) c ≡_ℓ c (the identity transport both ways), so c ∈ R_<e ⇒ ¬New. (b) d ≡_ℓ c (on C_c) can hold while c ≡_ℓ d (on C_d) fails; (N) uses only d ≡_ℓ c with c fixed.

**Type.** definition-consequence.

**Uses.** Inventions: I48. Formal core §13.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 no witness found; 1 computed: as claimed). Rests on: I48, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC85 --scale 4 --time-cap 45`.

### FC86 · Repair: a protected aim failed in between is lost

> L438 | \operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\iff\exists o\in O[\neg o(\xi)\land o(\xi')]\land\forall r\in P[r(\xi)\Rightarrow r(\xi')]\land\operatorname{ProducedBy}(\Delta,\xi,\xi';O). \tag{P}

> L441 | a protected condition is lost exactly when it fails on an occasion it covers.

**Formal.** Under I57: a protected r met at ξ and at ξ' and failed on a covered occasion between them makes (P) fail; r is lost ⟺ it fails on a covered occasion in [ξ, ξ'].

**Type.** strong candidate; definition-consequence. S100 unit: L437.s1.

**Uses.** Inventions: I57. Formal core §14.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 look: as expected). Rests on: I57, I96. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC86 --scale 4 --time-cap 45`.

### FC87 · Two sufficient contributions that both ran are both attributed

> L441 | where two sufficient contributions both ran, the repair is attributed to both and the history supplies no division of the attribution that it does not contain.

**Formal.** ProducedBy attributes the repair to each Δ_i with an active route to it; with two such, both; no function from the history to shares of attribution is defined (a weighting is a declared input, L522).

**Type.** definition-consequence. S100 unit: L437.s1.

**Uses.** Inventions: I46, I57. Formal core §14.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds by construction). Rests on: I46, I57. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC87 --scale 4 --time-cap 45`.

### FC88 · Losses outside P are exposed in the claim, not in (P)

> L441 | Losses outside \(P\) must be exposed.

**Formal.** Under I58: a repair claim with aims O, P, Aims* and exposure record X is well formed ⟺ {r ∈ Aims*∖P : r(ξ) ∧ ¬r(ξ')} ⊆ X. The condition bears on the claim: (P) can hold while the claim is not well formed.

**Type.** strong candidate; definition-consequence. S100 unit: L441.s4.

**Uses.** Inventions: I57, I58. Formal core §14.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I57, I58, I96. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC88 --scale 4 --time-cap 45`.

### FC89 · L443 (after round 1) puts 'deployable' where Deploy's type allows it

> L443 | An explanatory aim requires a deployable account, or the correction of a use through one.

> L449 | \operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)

**Formal.** Deploy takes a content (L403). Under the old wording a correction (a subhistory with changes, L435) was asked to be deployable, a mismatch of type. Under the new wording (I59) both kinds of explanatory aim put Deploy on the account c, which is what (EX) asks for every o ∈ O_ex. (EX) has no condition that tells the two kinds apart; the second kind is carried only by ProducesVia.

**Type.** strong candidate; definition-consequence. S100 unit: L443.s2. Round 1: round-1 change L443; what the L443 change may have disturbed: (EX) L447–L449, ProducesVia L453.

**Uses.** Inventions: I59, I60. Formal core §14.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I59, I60. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC89 --scale 4 --time-cap 45`.

### FC90 · The worked case's '(EX) is met' against (EX)'s conjuncts

> L628 | If \(S_1\) was built by an owned subhistory containing a nontrivial binding construction, the binding of a persistence component to a continuity subnetwork, and \(S_1\) is not in the prior repertoire, then (G) is met.

> L628 | and since \(S_1\) is an account on its contract and deployable, (EX) is met.

**Formal.** (EX) needs: CreativeCriticalEpisode(s,Δ,h,e); Repair; o ∈ O_ex with ¬o(ξ) ∧ o(ξ'); Origin(s,c,p_c,h,e_c) with e_c ⪯_h e; Account; c ∈ Result(Δ); Deploy(s,c,ξ';U_c); ProducesVia(Δ,c,o;ξ,ξ'). L628 states (G)'s Build and New (not Attempt), (P), Account and 'deployable'. Test which of CreativeCriticalEpisode (L429's four parts), Attempt, c ∈ Result(Δ), ProducesVia and e_c ⪯_h e the worked case's description gives, and which it leaves to be read in.

**Type.** stated result. Round 1: what the L443 change may have disturbed: the worked case at L628.

**Uses.** Inventions: I44, I57, I59, I60, I68. Formal core §14, §17.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I44, I57, I59, I60, I68. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC90 --scale 4 --time-cap 45`.

### FC91 · (CT1) is C ⊆ F(C) only with (CT1)'s completion read into F

> L466 | \operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C. \tag{CT1}

> L471 | \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form

**Formal.** Under I61: RetReal(π,T,C;χ) ⟺ C ⊆ F(C). With 'complete' read without the output condition, C ⊆ F(C) follows from RetReal and is weaker than it.

**Type.** definition-consequence. S100 unit: L471.s2. Round 1: matter 10: 'complete' in L471's first sentence.

**Uses.** Inventions: I61. Formal core §15.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 witness found). Rests on: I61, I97. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC91 --scale 4 --time-cap 45`.

### FC92 · (CT2): monotone F and its greatest fixed point

> L471 | the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

> L546 | **A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions.

**Formal.** (a) X ⊆ Y ⇒ F(X) ⊆ F(Y). (b) U := ∪{D ⊆ Z : D ⊆ F(D)} has F(U) = U and contains every fixed point (the Knaster–Tarski construction on P(Z)). (c) The D of (b) is bound in the clause and is not a question's target. (d) (CT2) has no counterexample under either reading of 'complete', since monotonicity does not use the output condition.

**Type.** strong candidate; stated result. S100 units: L471.s2, L546.s1. Round 1: round-1 change L471; what the L471 change may have disturbed: the locally bound D and how L546 names (CT2).

**Uses.** Inventions: I61. Formal core §15.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried). Rests on: I61, I97. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC92 --scale 4 --time-cap 45`.

### FC93 · (CT3), (CT4), and capability at one tolerance

> L479 | Then \(\mathsf{Cap}^{q,r}_\Omega(\xi)\subseteq\mathsf{Admit}^{q,r}_\Theta\); \(\mathsf{Cap}^\infty=\bigcap_{q,r}\mathsf{Cap}^{q,r}\subseteq\mathsf{Poss}_\Theta\). (CT3, CT4) Capability at a given tolerance does not imply possibility at every tolerance.

**Formal.** (a) Under I62, Cap^{q,r} ⊆ Admit^{q,r}. (b) Intersecting over (q,r): Cap^∞ ⊆ Poss. (c) There are models with T ∈ Cap^{q,r} and T ∉ Poss.

**Type.** stated result.

**Uses.** Inventions: I62. Formal core §15.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 witness found). Rests on: I62, I98. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC93 --scale 4 --time-cap 45`.

### FC94 · Recursion does not entail universality

> L509 | Recursion does not entail universality; a historical extension leaves it open; a finite performance record does not suffice for it.

**Formal.** (a) There is a model of RC with ¬UU. (b) With 𝔈_Θ infinite (I75), no finite set of performed tasks decides UU.

**Type.** stated result.

**Uses.** Inventions: I74, I75. Formal core §16.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I74, I75. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC94 --scale 4 --time-cap 45`.

### FC95 · A system can represent a theory in error

> L211 | A system can represent a theory in error: the transport from carrier to content is faithful while the transport from the content's target to the content fails.

**Formal.** There are o, a content c = (E_c, C_c, Γ_c) and its target D_c with Rep_ℓ(o,c) and ¬Faithful for the candidate's transport t_c: D_c → E_c.

**Type.** stated result.

**Uses.** Inventions: I48, I52. Formal core §12.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I48, I52, I90, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC95 --scale 4 --time-cap 45`.

## G. Arguments 2 and 5–10, the dependence order, and matters from round 1

### FC96 · Argument 2: same counterparts, one account

> L562 | (i) Their answer profiles coincide on \(C\). (ii) If a bijection \(\varphi\) of their active components gives each \(k\) and \(\varphi(k)\) one counterpart, the same subnetwork of \(D\) with port translations that are bijections onto the same ports of \(D\), then \(k\) and \(\varphi(k)\) are of one kind on \(C\) for every \(k\);

**Formal.** (i) A_C(ℰ) ∧ A_C(ℰ') ⇒ Ans_E(τa,σb) = Ans_E'(τ'a,σ'b) on C. (ii) If φ: Γ → Γ' is a bijection with λ'(φk) = λ(k), θ_k and θ'_φk with the same image, and F1_C for both, then β_k := θ'_φk⁻¹∘θ_k is a footprint bijection under which the signatures of k and φk read through t, t' coincide on C, when the value maps agree (I14); with different value maps they coincide only up to recoding values (I10's alternative).

**Type.** stated result. S100 unit: L546.s1.

**Uses.** Inventions: I10, I12, I14. Formal core §4, §5.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (2 holds on all models tried). Rests on: I10, I12, I14, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC96 --scale 4 --time-cap 45`.

### FC97 · Argument 5: a contract can be an organization and a content

> L588 | **Claim.** A contract \(C\), taken with its edits and its query, can be given the structure of an organization in the sense of (O), and can be the content \(c\) in (G).

> L590 | Give it ports (the edits and their boundaries), components (the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits (add or remove a change; alter \(\mathcal Q\)).

**Formal.** Under I67, D_C (membership ports, a query port, closure components, setting edits) is an organization in the sense of (O): nonempty domains, footprints, a partial composition with identity, a relation for every (j,a,b). With a contract on D_C (I48), Deploy, Build, New and (G) take it as a content.

**Type.** stated result.

**Uses.** Inventions: I01, I48, I67. Formal core §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed; 1 not tested). Rests on: I01, I48, I67. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC97 --scale 4 --time-cap 45`.

### FC98 · Argument 6 and the dependence order: acyclic, and ending where the text says

> L596 | **Claim.** Every predicate in Parts II–XIII is defined in terms of \(\Theta\) (including \(\operatorname{Org}_\ell\)) and, where invoked, \(\mathcal N\), together with the structural vocabulary of (O) and (Q), declared indices and declared inputs.

> L526 | The order has no cycle and no endless descent.

**Formal.** Graph: nodes the defined symbols of the formal core; an edge from a definition to each symbol it uses. Test (a) acyclicity (S101 read two loops from the wording: build–prov–rep, and K2–arg–livej, which FC69 closes under I40); (b) every sink is Θ (with Org_ℓ), 𝒩, (O), (Q), an index, or a declared input of L522. Symbols the formal core uses that are none of these on their face: Offered (I33), the restriction operation (I29), Integrated and Nontrivial (I55), Prepares, BindingConstruction, TransferComposite (I56), MadeFrom (I39), Applies (I34), Aims* (I58), O_ex (I59), the contrasts K (I46), Rule, Rec, Chg (I47), Occurs (§12), the designation δ (I20). For each: a claim read through Θ, or a primitive the text does not list?

**Type.** stated result. S100 unit: L520.s7.

**Uses.** Inventions: I20, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59. Formal core §18.

**Look.** The loop build → prov → rep stays open unless Prepares is a primitive (I56): L405's 'prepares a represented organization' asks for (R), (R) for Sel or Con, and Con for a construction trace, which is Build's subhistory. L526 names this risk ('A representation defined only by its own construction … has not supplied its place in the order').

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I20, I29, I33, I34, I39, I46, I47, I55, I56, I58, I59. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC98 --scale 4 --time-cap 45`.

### FC99 · Argument 7: an account on C can fail on C'

> L606 | and \(\mathcal E\) can meet (E) on \(C\) and fail it on \(C'\).

**Formal.** There are D, C, C', Q and ℰ with Acc on (D, C, …) and ¬Acc on (D, C', …); for example the pole's forward candidate with C1 and with C' adding an edit at which its τ gives the wrong edit of E.

**Type.** stated result.

**Uses.** Inventions: I65. Formal core §6, §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I65, I92. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC99 --scale 4 --time-cap 45`.

### FC100 · Argument 8: structure-preserving bijections keep (E), (G), (P), (EX)

> L612 | Transporting all carriers, relations, transports, histories, contracts and declared inputs along structure-preserving bijections preserves (E), (G), (P), (EX).

> L612 | The result does not apply to coarsenings, changed boundaries, or lost event identities.

**Formal.** Under I70: Acc(φ·ℰ) = Acc(ℰ), and (G), (P), (EX) are kept, for every structure-preserving bijection φ of all the data, NC1's answer slot and the stated scope carried along. Testable on random isomorphic copies of finite models.

**Type.** stated result.

**Uses.** Inventions: I45, I70. Formal core §18.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 not tested). Rests on: I45, I70, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC100 --scale 4 --time-cap 45`.

### FC101 · Argument 9: an input–output description does not fix an account

> L616 | **Claim.** If \(M_0,M_1\) have the same input–output projection and differ on an account claim, no function of the projection agrees with the claim on both.

> L616 | Parallel and priority wiring are an instance.

**Formal.** (a) For any function f of the projection P: P(M0) = P(M1) ⇒ f(M0) = f(M1). (b) Construct M0 (two parallel routes to the output) and M1 (a priority route with a fallback) with equal input–output projections, a question whose contract holds edits deleting internal components, and a candidate that meets (E) for one and not the other.

**Type.** stated result.

**Uses.** Inventions: I29, I46. Formal core §6, §7.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds by construction; 1 computed: as claimed). Rests on: I29, I46, I78. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC101 --scale 4 --time-cap 45`.

### FC102 · Argument 10: surprise, the structural failure of selection, and the constructed layer

> L624 | \(S_0\), predicting from occupancy, predicts nothing there and is violated when the thing re-emerges at a cell consistent with its velocity. This is surprise (Argument 4).

> L626 | If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric.

> L626 | Under (F1), \(t_1\) is faithful on the extended contract.

**Formal.** With I68: (a) t0 (window w) survives on H0 and is violated at the re-emergence pair, which lies in C0∖H0: Surp. (b) If the occlusion hides the thing for longer than w steps, every window-w occupancy predictor fails on the extended history (two histories with equal last-w occupancy and different re-emergence cells); if w is at least that long, an occupancy predictor can extrapolate and the failure is not structural. (c) t1 meets (F1) and (F2) on the extended contract, and each persistence component's signature read through t1 equals its thing's continuity subnetwork's (Argument 1).

**Type.** stated result.

**Uses.** Inventions: I52, I68. Formal core §12, §17.

**Look.** A single occluded cell hides a thing moving one cell a step for one step only; 'recent' has to be shorter than that gap for (b).

**Search result (S104).** COUNTEREXAMPLE FOUND (1 computed: as claimed; 1 computed: not as claimed; 1 not tested). Rests on: I52, I68, I100. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC102 --scale 4 --time-cap 45`.

### FC103 · Argument 10: the swap, two pairings, one account

> L630 | On any contract containing it that admits each edit for both things alike, composing \(t_1\) with the exchange of the two things gives a second transport, which sends each persistence component to the other thing's continuity subnetwork.

> L630 | A claim that "component 1 is thing 1 and not thing 2" is a claim that some admitted change separates the two pairings of persistence components to things, and on this contract none does.

**Formal.** With I69: ψ an automorphism of P preserving C and the answers; t1' := t1∘ψ. (a) t1' meets (F1), (F2) and (A) on C exactly when t1 does. (b) The exchange of persistence components meets Argument 2 (ii)'s premise, so each k and its image are of one kind on C. (c) No pair of C separates the two pairings (FC51 (b)). (d) The swap edit leaves every occupancy answer unchanged.

**Type.** stated result.

**Uses.** Inventions: I10, I14, I68, I69. Formal core §17.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed; 1 not tested). Rests on: I10, I14, I68, I69, I100. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC103 --scale 4 --time-cap 45`.

### FC104 · The two extents of 'fidelity' across the text

> L189 | A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V.

> L245 | Together they are fidelity at every level the contract reaches.

> L247 | **Question fidelity.**

> L520 | Account, from fidelity under change

> L630 | carries the fidelity and the answers of \(t_1\) over

**Formal.** For each line using 'faithful' or 'fidelity' (L17, L23, L37, L41, L43, L49, L67, L69, L151, L189, L195, L205, L208, L211, L220, L233, L245, L247, L271, L277, L325, L339, L403, L407, L413, L520, L576, L622, L626, L630), assign the extent under which the sentence holds as written: narrow (F1) ∧ (F2), or wide (F1) ∧ (F2) ∧ (A). Claim to test: no single extent serves every line; L189, L245 and L630 need the narrow one, L247's heading and L520 the wide one.

**Type.** definition-consequence. S100 unit: L220.s1. Round 1: matter 12: the narrow and wide senses of 'fidelity' (L189, L245, L247, L520, L630).

**Uses.** Inventions: I49, I50. Formal core §5, §12.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I49, I50. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC104 --scale 4 --time-cap 45`.

### FC105 · 'Event' is used and never defined; 'occurrence' is defined

> L169 | An **occurrence** is a physically located carrier.

> L161 | Its formulation is still an event.

> L604 | **Claim.** An assessment event with contract \(C\) and an episode in which \(C\) is replaced by \(C'\) with a construction trace are both representable without contradiction.

**Formal.** Under I45 every use of 'event' (L53, L55, L161, L397, L604, L612) is read as a set of occurrences. Test whether any use needs more (for example 'lost event identities' at L612, an identity of an event beyond its occurrences). Argument 6 (L596) speaks of predicates; 'event' is a sort, defined nowhere.

**Type.** definition-consequence. S100 unit: L161.s2. Round 1: matter 2: 'event', never defined, beside 'occurrence' (L169).

**Uses.** Inventions: I45. Formal core §11.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I45. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC105 --scale 4 --time-cap 45`.

### FC106 · A question's three defects, as far as they can be written

> L161 | A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.

**Formal.** Under I76: 'incompatible baseline' is Sol_D(1,b0) = ∅ (then non-vacuity fails and no candidate has Acc) or b0 ∉ B; 'incompatible requirements' is a description whose conditions on (C, Q) have no joint instance; 'fails to pick out its alleged target' is a description met by no organization or by several, and cannot be written with p alone, since D is given in p.

**Type.** strong candidate; definition-consequence. S100 unit: L161.s1.

**Uses.** Inventions: I76. Formal core §3.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds on all models tried; 1 not tested). Rests on: I76, I77, I78, I81. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC106 --scale 4 --time-cap 45`.

### FC107 · Exposing a question's defect is another question

> L161 | Exposing the defect is another question with its own contract.

**Formal.** The question p_δ (whether p has defect δ) has a target, contract and query of its own, so p_δ ≠ p; a candidate for it is assessed by (E) on p_δ, as in (K1).

**Type.** strong candidate; definition-consequence. S100 unit: L161.s3.

**Uses.** Inventions: I76. Formal core §3, §9.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I76. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC107 --scale 4 --time-cap 45`.

### FC108 · The first sentence of non-circular dependence adds no condition

> L255 | **Non-circular dependence.** The answer follows by evaluating \(E\) under its independent boundary conditions.

**Formal.** Under I23, NC0 holds of every candidate: every answer is computed by evaluating E at (τ(a),σ(b)), with σ(b) a function of b. A reading on which it adds a condition needs a notion of how an answer is computed (propagation against lookup) that (O) and (Q) do not give.

**Type.** strong candidate; definition-consequence. S100 unit: L255.s1.

**Uses.** Inventions: I23. Formal core §6.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 holds by construction). Rests on: I23. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC108 --scale 4 --time-cap 45`.

### FC109 · 'A mathematical error': the named claims, each under its stated assumptions

> L546 | **A mathematical error.** A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions.

**Formal.** L546 names the finite monotone claim (FC37), (I2) (FC57), (O1) (FC61), (T2) (FC66), (CT2) (FC92) and Arguments 1–3 (FC17, FC96, FC80). Each is stated in the formal core with its assumptions. A counterexample that rests on an invention is a counterexample to the formalization, not to the text, and is reported with the invention it rests on.

**Type.** strong candidate; stated result. S100 unit: L546.s1.

**Uses.** Inventions: I10, I12, I13, I14, I61, I63, I64, I71. Formal core §18.

**Search result (S104).** HOLDS ON ALL MODELS TRIED (1 computed: as claimed). Rests on: I10, I12, I13, I14, I61, I63, I64, I71. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC109 --scale 4 --time-cap 45`.

### FC110 · The classes are defined; no membership is asserted

> L27 | It does not decide whether any human, machine, institution or lineage belongs to the classes defined. It defines the classes.

> L528 | **Membership.** The base class: interpretations supplying these data with typing as declared, meeting physical realization wherever a physical attribution is made.

**Formal.** Syntactic: each class of L528 (base, creative-episode, explanation-creation, recursive, universal) is the extension of a formula of the formal core; no axiom of the formal core places any particular system in a class.

**Type.** strong candidate; definition-consequence. S100 unit: L27.s2.

**Uses.** Inventions: I74, I75. Formal core §16, §18.

**Search result (S104).** NOT TESTED (1 not tested). Rests on: I74, I75. See `search results.md`; reproduce: `cd "/home/user/ThreadSmith/Semantics/results/S104 Round 2 - maths" && python3 -m model.run --claim FC110 --scale 4 --time-cap 45`.

## The 36 strong candidates of S100, and how far each is formal

Line numbers are those of file 103, which file 99 shares (round 1 changed four lines one for one). A display unit is given by the line that holds its formula. 'Tested' are the seven challenged and kept before round 1; 'never challenged' are the twenty-nine round 1 put to the readers. This table records how far each sentence can be written as mathematics; it grades nothing (S20).

| unit | line | before round 1 | status | claims | why |
| --- | --- | --- | --- | --- | --- |
| L546.s1 | L546 | tested | formalizable | FC109, FC37, FC57, FC61, FC66, FC92, FC17, FC96, FC80 | A list of named mathematical claims; each is stated and testable. |
| L255.s1 | L255 | tested | formal only as a gloss | FC108 | Read as NC0 it is met by every candidate (I23); a reading that adds a condition needs a notion of how an answer is computed that (O) and (Q) do not give. |
| L441.s4 | L441 | tested | formalizable in part | FC88 | Needs the set of aims considered and what 'exposed' is (I58), neither given; then it is a well-formedness condition on a repair claim. |
| L51.s1 | L51 | tested | typing only | — | A pointer to where aesthetics sits; its formal content is the typing of 𝒩 as an input (NF16). |
| L517.s1 | L517 | tested | typing only | — | Lists what the physical module supplies; a signature of types, not a claim (NF17). |
| L389.s1 | L390 | tested | formalizable | FC69, FC70, FC56 | (K2); well founded under I40. |
| L437.s1 | L438 | tested | formalizable | FC86, FC87 | (P), with the occasions read as in I57. |
| L311.s2 | L311 | never challenged | formalizable | FC40 | Every critical block in the example is infinite; critical blocks exist. |
| L47.s2 | L47 | never challenged | formalizable | FC84, FC78 | Origin, CreateEx and the creative-episode class each require Build. |
| L383.s1 | L383 | never challenged | formalizable | FC74 | A satisfiability claim. |
| L443.s2 | L443 | never challenged | formalizable in part | FC89, FC90 | O_ex is a declared marking; the sentence is read as characterizing it (I59). |
| L41.s4 | L41 | never challenged | formalizable | FC79 | Faithful takes no selection parameter. |
| L273.s1 | L273 | never challenged | formalizable | FC23 | Rests on NC1 (I24): NC2 alone does not exclude the lookup. |
| L225.s4 | L225 | never challenged | formalizable | FC83 | A claim to test; it follows only on a reading of Build (I56) the text does not fix. |
| L471.s2 | L471 | never challenged | formalizable | FC92, FC91 | Knaster–Tarski on the powerset; clause 2 needs I61's reading of 'complete'. |
| L520.s7 | L520 | never challenged | formalizable | FC31, FC32, FC98 | A claim about which definitions Account is built from; tested against (E) and L526. |
| L113.s2 | L113 | never challenged | typing only | FC03, FC04, FC05 | The lead-in to (K); its consequences are claims. |
| L115.s1 | L116 | never challenged | formalizable | FC03, FC04, FC05, FC16 | (K) itself; claims are its consequences. |
| L123.s1 | L123 | never challenged | formalizable | FC07, FC10, FC12 | Needs I04, I06 (two readings), I09. |
| L124.s1 | L124 | never challenged | formalizable | FC06, FC07, FC08, FC12 | Needs I06, I07, I09; its first clause holds of every reader (FC06). |
| L125.s1 | L125 | never challenged | formalizable | FC09, FC10, FC12 | Needs I08 ('the world', 'the rule'), I09. |
| L127.s1 | L127 | never challenged | formalizable | FC13, FC08 | The families are functions of D and C under I04 and I06. |
| L127.s2 | L127 | never challenged | syntactic | FC14 | A property of the definitions: none takes 'is a cause'. |
| L127.s3 | L127 | never challenged | syntactic | FC14 | As L127.s2. |
| L161.s1 | L161 | never challenged | formalizable in part | FC106 | Two defects can be written with p; the first needs a description p answers to (I76). |
| L161.s2 | L161 | never challenged | not formalizable | FC105 | 'Event' is defined nowhere; only under I45 does the sentence type the formulation as a set of occurrences (NF18). |
| L161.s3 | L161 | never challenged | formalizable | FC107 | p_δ ≠ p. |
| L113.s1 | L113 | never challenged | typing only | FC11, FC15 | Fixes the parameters of (K). |
| L217.s2 | L217 | never challenged | formalizable in part | FC81 | 'Actually occurring' is a primitive Occurs read through the physical module. |
| L219.s1 | L219 | never challenged | formalizable | FC20, FC35 | Pred for transports to S; L151's use lies outside it (FC35). |
| L220.s1 | L220 | never challenged | formalizable | FC20, FC104 | Needs the extent of 'fidelity' at a pair (I50). |
| L225.s1 | L225 | never challenged | formalizable | FC82 | The two responses have no common result under I53. |
| L393.s4 | L393 | never challenged | formalizable | FC70, FC56 | First clause fails for a premise live twice over; second clause holds (monotonicity). |
| L375.s2 | L375 | never challenged | formalizable in part | FC75 | Four phrases undefined ('represented input', 'operative result', 'applicable relations', 'declared contrasts'); I46. |
| L385.s1 | L385 | never challenged | formalizable in part | FC76 | Four phrases undefined ('structural map', 'role bindings', 'the same transition', 'operative deliberative rule'); I47. |
| L27.s2 | L27 | never challenged | syntactic | FC110 | The classes are formulas; no membership is asserted. |

## Claims of the text not formalized, and why

### NF01 · L17

> L17 | A candidate would conflict with the conjecture if an argument not using these four ruled out the claim that it is a non-explanation of its question while these four cannot represent it

**Why not.** 'Is a non-explanation of its question' is not a predicate of the semantics, and 'these four cannot represent it' has no definition; only the logical shape can be written.

### NF02 · L536

> L536 | such that an argument not using (E) rules out the claim that it is an explanation of what its question asks.

**Why not.** (Suff) relates Account to 'is an explanation of what its question asks', which the semantics leaves outside itself; formal shape only: ¬∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ some argument not using (E) is in X_j('ℰ is an explanation')].

### NF03 · L538

> L538 | whose organization no transport can preserve under any contract on its target.

**Why not.** The preservation clause is formal (∀C ∀t ¬Faithful_C(t)); 'rules out the claim that it is a non-explanation' is not.

### NF04 · L540

> L540 | and the distinction does explanatory work.

**Why not.** 'Explanatory work' is not defined; the formal part of (Elim) is FC18 and FC96.

### NF05 · L542

> L542 | a method that rewrites every construction trace as a selection history without loss

**Why not.** 'Without loss' is not defined; nor is 'explanation operates on the object layer' in the third item.

### NF06 · L544

> L544 | A case of finding a new question that treating a contract as a content, something that can be constructed, be new, and be the originative contribution of an episode, fails to capture

**Why not.** 'Fails to capture' is not defined; the formal part of (QF) is Argument 5 (FC97).

### NF07 · L201

> L201 | Neither provenance is reducible to the other

**Why not.** 'Reducible' is not defined; the formal part is exclusivity (FC78).

### NF08 · L151

> L151 | A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question

**Why not.** The candidate made of a measure and a prediction is not specified (organization, commitments, transport), so 'answers' cannot be checked against (E); FC35 takes up only the word 'prediction'.

### NF09 · L407

> L407 | An inexplicit representation is not an absent one.

**Why not.** 'Written in a particular format' has no formal counterpart; formally, (R), Deploy and Build take no format argument (a syntactic property).

### NF10 · L429

> L429 | Closing an episode is a choice

**Why not.** No formal content beyond the syntactic fact that no definition outputs a choice (decisions S21, S28).

### NF11 · L495

> L495 | An explanatory barrier is an independently characterized domain for which every admitted, non-question-begging enabling condition leaves the relevant capability unavailable.

**Why not.** 'Independently characterized' and 'non-question-begging' are not defined.

### NF12 · L497

> L497 | the coherently posed advanceable challenges

**Why not.** 'Coherently posed' and 'advanceable' are not defined, so (U2)'s domain is open.

### NF13 · L8

> L8 | A claim that no argument rules out is only not ruled out, and gets nothing from that

**Why not.** No notion of a claim 'getting' something exists in the semantics; formally, only the absence of any predicate triggered by NotOut (a syntactic property).

### NF14 · L397

> L397 | That a person can use a claim so, without containing its explanation, is a costly gamble for all creative agents

**Why not.** No measure of cost; the text says so ('puts no measure on it').

### NF15 · L45

> L45 | Whether the combination is new is a question about the literature.

**Why not.** About other theories, not a claim of the semantics.

### NF16 · L51

> L51 | **8. "Where is aesthetics?"** In Part XI, as a declared appraisal relation.

**Why not.** Strong candidate L51.s1: a pointer; formal content only the typing of 𝒩 ⊆ Act × Occ × Rsn × V_A as an input.

### NF17 · L517

> L517 | 1. The **physical module** \(\Theta\): substrate state spaces, attributes, admitted processes, controlled-action interpretation, resources, tolerances, and \(\operatorname{Org}_\ell\), the organization a physical occurrence instantiates at a grain.

**Why not.** Strong candidate L517.s1: a signature of types for the import, not a claim.

### NF18 · L161

> L161 | Its formulation is still an event.

**Why not.** Strong candidate L161.s2: 'event' is defined nowhere (FC105); under I45 it types the formulation as a set of occurrences and says nothing further.

### NF19 · L455

> L455 | None is defined as another.

**Why not.** The three aesthetic relations are typed inputs; 'none is defined as another' is a syntactic property, and no relation among them is given to test.

## The four round-1 changes and the matters round 1 left for this round, where each is taken up

- Round-1 change L123: FC07
- Round-1 change L443: FC89
- Round-1 change L471: FC92
- Round-1 change L520: FC31
- Matter 10: 'complete' in L471's first sentence: FC91
- Matter 11: the undefined phrases at L375 and L385: FC75, FC76
- Matter 12: the narrow and wide senses of 'fidelity' (L189, L245, L247, L520, L630): FC104
- Matter 12: the narrow and wide senses of 'fidelity' (the C18 ruling's argument): FC20
- Matter 1: (K) applied beyond components (L119, L554–L556): FC15, FC16, FC17
- Matter 2: 'event', never defined, beside 'occurrence' (L169): FC105
- Matter 4: L121 names four things with three bullets: FC09
- Matter 5: L109 gives roles under A while (K) builds a signature on a contract C: FC11
- Matter 6: 'prediction' at L151: FC35
- Matter 7: L273's second sentence: FC24
- Matter 8: L311's first sentence; the second sentences of L311 and L273: FC40
- Matter 9: a premise that stays live twice over (L393): FC70
- What the L123 change may have disturbed: L109: FC11
- What the L123 change may have disturbed: L123–L125 against L57, L109, L127: FC07
- What the L123 change may have disturbed: L127: FC08
- What the L123 change may have disturbed: L57: FC10
- What the L123 change may have disturbed: the C07 / C08–C09 asymmetry: FC12
- What the L123 change may have disturbed: the asymmetry the critical review gives between C07 and C08/C09: FC06
- What the L443 change may have disturbed: (EX) L447–L449, ProducesVia L453: FC89
- What the L443 change may have disturbed: the worked case at L628: FC90
- What the L471 change may have disturbed: the locally bound D and how L546 names (CT2): FC92
- What the L520 change may have disturbed: 'the four conditions' at L61, L231, L536: FC31
- What the L520 change may have disturbed: L526's order: FC32
