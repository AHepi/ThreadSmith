# S104 Round 2 — inventions register

*Log S104, review round 2 (the maths round), 27 September 2026. Decision S36: "Also, if implementation forces invention, that needs to be recorded." The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd (checked by `s104_check.py` before every build; not written to). Built by `s104_build.py` from `s104_inventions.py`; the claims each invention is used by are read from `s104_claims.py`, so the two lists cannot drift apart. Every quotation below was compared by program with the line it names.*

**What this is.** Every choice the formal core or the claims make that the text does not fix: a missing definition, a default, a domain, a choice between two readings of a sentence, a finite bound, an encoding. Each entry quotes the sentence it fills in for, says what was invented and what else could have been chosen, and names the sections of `formal core.md` and the claims of `formal claims.md` that use it. Nothing invented is the text's own content, and no entry is offered as what the text means; each is the choice this formalization made so that the text could be written as mathematics, open to replacement.

**Results.** The claims were then searched for counterexamples on finite models by the program `model/` (`search results.md`). That program needed further choices the formal core leaves open; they are I77–I102 below, each tagged in the code where it is used. Each entry now lists the results of the search that depend on it: the claims whose results rest on it and, for a claim with a counterexample, the parts whose counterexample rests on it.

**Counts.** 102 inventions (I01–I76 from the formal core and the claims, I77–I102 from the program); 110 claims; 76 of the inventions are used by at least one claim.

## Index

| id | invention | lines | claims that use it |
| --- | --- | --- | --- |
| I01 | Composition of edits: a partial monoid with Kleene associativity | L91 | FC97 |
| I02 | No law links a composite edit's relations to its parts' relations | L91, L574 | FC80 |
| I03 | Ports and components are fixed; deletion and absence are the full relation | L103, L339 | FC01, FC25, FC62, FC63 |
| I04 | Setting a port: a surgical edit, and the assigning component read off the edits | L103, L109, L119 | FC02, FC06, FC07, FC08, FC11, FC13, FC25, FC26, FC27 |
| I05 | 'Output': at the identity edit, and 'determined' as at most one value | L109 | FC02 |
| I06 | Observation edits: two readings of 'the relation reporting it' | L109, L127 | FC07, FC08, FC13 |
| I07 | 'The measured port' and 'the measuring relation' | L124 | FC06, FC07, FC08 |
| I08 | 'Interventions on the world' and 'the rule' | L125 | FC09, FC10, FC13 |
| I09 | 'Changes under', 'invariant under', 'variable under': compared with the identity edit at the same boundary | L123 | FC06, FC07, FC10, FC11, FC12, FC13 |
| I10 | Kinds: a footprint bijection between equal value domains, relations compared as sets | L119 | FC03, FC04, FC05, FC16, FC18, FC96, FC103, FC109 |
| I11 | 'Coarser' and 'finer' contracts: fewer and more pairs | L119, L317 | FC04, FC50 |
| I12 | Reading a candidate's component on C through the transport; τ[C] | L119, L554 | FC15, FC16, FC17, FC29, FC96, FC109 |
| I13 | (K) extended from components to subnetworks | L556 | FC17, FC18, FC109 |
| I14 | Subnetworks, their solutions, and port translations with value maps | L189, L233 | FC17, FC18, FC19, FC25, FC44, FC62, FC96, FC103, FC109 |
| I15 | 'Active component' means a member of Γ | L233 | FC17, FC19 |
| I16 | The domain of π: 'on the stated scope' | L189 | FC20, FC49 |
| I17 | Partial τ and σ; which pairs a transport 'translates' | L315 | FC45, FC49 |
| I18 | The homomorphism clause of (F2): its range, and that it is not pointwise | L242 | FC15, FC51 |
| I19 | Meeting (F1), (F2) and (A) at one pair under hypothetical relations of the target | L315 | FC44, FC45, FC46, FC47, FC52, FC54 |
| I20 | How the fixed query is applied to a candidate's organization | L141, L253 | FC20, FC26, FC28, FC30, FC32, FC45, FC68, FC98 |
| I21 | Undetermined answers: a value ⊥ | L255 | FC20, FC21, FC22, FC23, FC26, FC46, FC48 |
| I22 | 'Not determined … in the claimed way' | L255 | FC21, FC22, FC23 |
| I23 | The first sentence of non-circular dependence, read as a heading gloss | L255 | FC108 |
| I24 | NC1: the target's answer as an unanalysed boundary input or component, read structurally | L255 | FC23, FC24, FC26, FC33, FC34, FC51, FC60 |
| I25 | Non-circular dependence is the conjunction of its sentences | L255 | FC23 |
| I26 | 'Relabelings' | L257 | FC21 |
| I27 | The stated scope: a declared statement over pairs | L257 | FC26, FC30, FC32, FC33, FC34, FC51, FC63 |
| I28 | The grain as a label on the organizations compared | L255 | FC30, FC32, FC33 |
| I29 | The restriction operation (E restricted to W): deletion | L287 | FC41, FC98, FC101 |
| I30 | The worked examples of routes are set systems | L307 | FC38, FC39, FC40, FC42 |
| I31 | The routes of the infinitary example | L311 | FC40 |
| I32 | A table of observed answers: its counterpart and its relation | L269 | FC25 |
| I33 | The offer of one candidate in place of another: a primitive | L315 | FC43, FC49, FC50, FC54, FC98 |
| I34 | A claim χ as a set of allowed behaviours at a pair, and the premise that it speaks of the target | L315 | FC52, FC53, FC54, FC98 |
| I35 | Conflict given χ: no requirement that each candidate can meet under χ | L315 | FC54 |
| I36 | 'Two of their active components with one counterpart' | L315 | FC44 |
| I37 | 'Easy to vary' is relative to an assessor | L317 | FC43 |
| I38 | Claims, their denials, and 'inconsistent with its conclusion' | L397 | FC47, FC53, FC56, FC68, FC71, FC72, FC73 |
| I39 | 'Among its premises', read structurally; records made from a claim | L397 | FC60, FC72, FC98 |
| I40 | Live through a step: a step below, and essential premises | L387, L393 | FC47, FC53, FC56, FC68, FC69, FC70 |
| I41 | Tentative acceptance over time; withdrawal | L393 | FC56, FC68, FC70 |
| I42 | Scope_j: within the declared contract, grain and boundary | L393 | FC47 |
| I43 | (K3): what it adds and what 'nothing narrower' says | L395 | FC47, FC71 |
| I44 | Causal precedence in a history is transitive | L375 | FC75, FC90 |
| I45 | 'Event' is a set of occurrences | L169, L161, L397 | FC74, FC100, FC105 |
| I46 | Active route: 'represented input', 'operative result', 'applicable relations', 'declared contrasts' | L375 | FC75, FC87, FC98, FC101 |
| I47 | Reason use: 'structural map', 'role bindings', 'the same transition', 'operative deliberative rule' | L385 | FC76, FC98 |
| I48 | Contents, 'c's contract', and transports into a content | L169, L205, L413 | FC77, FC85, FC95, FC97 |
| I49 | 'Faithful' and 'fidelity': the narrow extent by default, the wide one where a line asks for it | L189, L247, L520, L630 | FC20, FC31, FC79, FC104 |
| I50 | A violation at a pair: which conditions fail | L220 | FC20, FC81, FC104 |
| I51 | 'Prediction' for a transport not said to reach the simulation layer | L151 | FC35 |
| I52 | Selection: the parameters witnessed in a physical history | L195 | FC77, FC78, FC79, FC80, FC81, FC82, FC83, FC95, FC102 |
| I53 | 'Exactly one of three provenances': one whole history | L193, L201 | FC78, FC81, FC82, FC84 |
| I54 | Inherited provenance: a rule of carrying over, per part | L211, L405, L409 | FC67, FC78 |
| I55 | Deploy: 'integrated into problem-directed activity', 'nontrivial use respect' | L403 | FC98 |
| I56 | Build: 'prepares', 'nontrivial binding construction', 'content-preserving transfer' | L405 | FC83, FC84, FC98 |
| I57 | Repair: how the aims are read at ξ and over [ξ, ξ']; which aim ProducedBy runs to | L441 | FC86, FC87, FC88, FC90 |
| I58 | 'Losses outside P': the aims considered, and 'exposed' | L441 | FC88, FC98 |
| I59 | Explanatory aims: L443 read as a characterization of O_ex | L443 | FC89, FC90, FC98 |
| I60 | ProducesVia: 'the relevant binding of c' | L453 | FC89, FC90 |
| I61 | Tasks and executions; 'complete' in F read as (CT1)'s completion | L461, L469, L471 | FC91, FC92, FC109 |
| I62 | Tolerances: stricter tolerances admit fewer tasks; Admit contains every realized task | L479 | FC93 |
| I63 | A tag such as (I2) names the sentence before it | L329, L335, L471 | FC57, FC58, FC61, FC109 |
| I64 | Identification: 'attainable', and the admitted states in the linear case | L329 | FC57, FC58, FC59, FC109 |
| I65 | The pole and its shadow, encoded | L325 | FC02, FC07, FC26, FC27, FC28, FC99 |
| I66 | The odd-order skew-symmetric case, encoded | L343 | FC63 |
| I67 | A contract as an organization (Argument 5), encoded | L590 | FC97 |
| I68 | Argument 10's two-layer episode, encoded; 'recent occupancy' | L620, L622 | FC90, FC102, FC103 |
| I69 | 'Built alike': the exchange is an automorphism | L630 | FC103 |
| I70 | A structure-preserving bijection of all the data (Argument 8) | L612 | FC33, FC45, FC67, FC100 |
| I71 | The 'value' of a transport at a pair (Argument 3) | L572 | FC80, FC109 |
| I72 | Respects as sufficient conditions; 'upstream' | L151 | FC36 |
| I73 | 'An answer to one is not an answer to the other': the narrow reading | L151 | FC34 |
| I74 | Recursive capacity: target chains and enabling continuations | L492 | FC94, FC110 |
| I75 | The explanatory contents 𝔈_Θ | L497 | FC94, FC110 |
| I76 | The three defects of a question, formally | L161 | FC106, FC107 |
| I77 | Finite models and the bounds of the search | L91, L105 | FC01, FC02, FC03, FC04, FC05, FC06, FC08, FC10, FC12, FC13, FC15, FC16, FC17, FC18, FC19, FC20, FC21, FC22, FC23, FC24, FC25, FC29, FC33, FC34, FC37, FC41, FC43, FC44, FC45, FC46, FC47, FC48, FC49, FC50, FC51, FC52, FC54, FC57, FC58, FC61, FC64, FC65, FC66, FC67, FC68, FC74, FC77, FC80, FC85, FC96, FC100, FC106 |
| I78 | Two families of generated organizations: surgical edits with override, and free edits | L91, L574 | FC01, FC02, FC03, FC04, FC05, FC06, FC08, FC09, FC10, FC12, FC13, FC15, FC16, FC17, FC18, FC19, FC20, FC21, FC22, FC23, FC24, FC25, FC29, FC33, FC34, FC37, FC43, FC44, FC45, FC46, FC47, FC48, FC49, FC50, FC51, FC52, FC54, FC62, FC67, FC68, FC74, FC77, FC80, FC85, FC96, FC100, FC101, FC106 |
| I79 | Boundary inputs and exogenous values are carried by components | L255, L325 | FC23, FC24, FC26, FC34, FC62 |
| I80 | The identity edit can be a setting edit | L109 | FC02, FC06, FC07, FC11, FC12, FC25 |
| I81 | Transports as port translations; derived ports; generated candidates; the transport space searched for ≡ | L189, L343, L413 | FC15, FC16, FC17, FC18, FC19, FC20, FC21, FC22, FC23, FC24, FC29, FC33, FC34, FC37, FC43, FC44, FC45, FC46, FC47, FC48, FC49, FC50, FC51, FC52, FC54, FC63, FC67, FC68, FC74, FC77, FC80, FC85, FC96, FC100, FC106 |
| I82 | Queries in the program; NC1 only for a query that reads a port | L141 | FC23, FC63 |
| I83 | An answer slot needs a determined target answer at every pair | L255 | FC23, FC24 |
| I84 | The homomorphism clause when a composite lies outside τ's domain | L242 | — |
| I85 | The default scope statement states every excluded pair | L257 | FC21, FC26, FC34, FC46, FC51 |
| I86 | Every pair of candidates examined counts as offered one in place of the other | L315 | FC43, FC49, FC50 |
| I87 | Claims as propositional formulas, read structurally | L397 | FC47, FC53, FC56, FC60, FC68, FC69, FC70, FC71, FC72, FC73 |
| I88 | X_j ranges over a finite set of arguments; an argument has a step | L397 | FC47, FC53, FC56, FC71 |
| I89 | The inference forms: MP, MT, AND-introduction, AND-elimination and a free form | L387, L393 | FC47, FC53, FC56, FC60, FC68, FC69, FC70, FC71, FC72, FC73 |
| I90 | The physical module supplied by hand: histories and provenance as free predicates | L31, L195, L197, L405 | FC53, FC76, FC77, FC78, FC81, FC82, FC83, FC95 |
| I91 | The infinitary routes on eventually periodic index sets | L311 | FC40 |
| I92 | The pole in exact arithmetic, with its grids, baseline, contracts and fibre query | L325 | FC02, FC07, FC11, FC26, FC27, FC28, FC78, FC81, FC82, FC83, FC95, FC99 |
| I93 | 'The two relations stay equal': under which footprint bijection | L119 | FC05 |
| I94 | The counterpart's signature 'read on C directly … up to the port translation': untranslated | L119 | FC18 |
| I95 | Toy histories for active routes | L375 | FC75, FC76 |
| I96 | Aims on discrete time | L441 | FC86, FC88 |
| I97 | Tasks and executions on finite state sets | L466 | FC91, FC92 |
| I98 | Tolerances as a 3 × 3 grid of performance and retention | L479 | FC93 |
| I99 | The odd-order skew-symmetric case in GF(3), and the Leibniz candidate's sum component | L343 | FC63 |
| I100 | The two-layer episode's object layer: cells, occlusion and windows | L620, L622 | FC102, FC103 |
| I101 | Which models count as witnesses: the proper-model filter | L91 | FC19, FC21, FC25, FC34, FC44 |
| I102 | A component assigning several ports, or a port assigned by none | L109, L123 | FC06, FC07 |

## The entries
### I01 · Composition of edits: a partial monoid with Kleene associativity

**The sentence it fills in for.**

> L91 | \(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\).

**What was invented.** (A, ·, 1) is a partial binary operation on A: a2·a1 is either undefined or a member of A; a3·(a2·a1) is defined exactly when (a3·a2)·a1 is, and then they are equal; 1·a = a·1 = a for every a. 'Closed' is read as: a composite, when defined, is in A.

**Other choices that were possible.**

- weak associativity: equal only when both sides happen to be defined
- a category: edits typed by source and target boundary, composable only when they match
- a total monoid (every composite defined)

**Used by.** Formal core §1. Claims: FC97.

**Results that depend on it.** FC97 — holds on all models tried.
### I02 · No law links a composite edit's relations to its parts' relations

**The sentence it fills in for.**

> L91 | For each \(j\), edit \(a\), and boundary \(b\), the interpretation supplies

> L574 | The component relations \(L_j(a,b)\) are supplied independently for each \((a,b)\).

**What was invented.** L is an arbitrary function J × A × B → relations. Nothing ties L_j(a2·a1, b) to L_j(a1, b) and L_j(a2, b). The composition on A matters only through the homomorphism clause of (F2) and through Functional transport. (L574 fixes independence across pairs; it does not say whether composites are constrained, so the absence of any such law is the invention.)

**Other choices that were possible.**

- an action law: each edit acts on the assignment of relations, L(a2·a1) = a2·(a1·L)
- edits as endomaps of the organization, with L read off the image

**Used by.** Formal core §1. Claims: FC80.

**Results that depend on it.** FC80 — holds on all models tried.
### I03 · Ports and components are fixed; deletion and absence are the full relation

**The sentence it fills in for.**

> L103 | A deleted component imposes the full relation on its ports.

> L339 | has a target \(D\) in which the ports and components a rival account would need are absent

**What was invented.** An edit never adds or removes a member of V or J. A deleted or absent component is one whose relation under that edit and boundary is the full product of its ports' domains. An 'absent' port is one on which every component that could constrain it imposes the full relation.

**Other choices that were possible.**

- edits that change J and V (organizations as a varying family; then Sol_D(a,b) lives in different spaces for different edits)
- absent ports removed from V, with query answers compared across different valuation spaces

**Used by.** Formal core §1, §17. Claims: FC01, FC25, FC62, FC63.

**Results that depend on it.** FC01 — holds on all models tried; FC25 — counterexample ((b) with a port of D in no footprint); FC62 — holds on all models tried; FC63 — counterexample ((c-i) the Leibniz candidate, sum over every tuple of term values).
### I04 · Setting a port: a surgical edit, and the assigning component read off the edits

**The sentence it fills in for.**

> L103 | An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one.

> L109 | No role assignment is supplied. A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly.

> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it

**What was invented.** An edit a sets port v at boundary b through component j when L_j(a,b) = {w : w_v = x} for some x in X_v (the other ports of V_j left free) and L_k(a,b) = L_k(1,b) for every k ≠ j. 'Directly' is this surgical form. The component assigning v, asg(v), is read off A: it is the component that the setting edits of v replace; where two different components are replaced by setting edits of v, asg(v) is undefined. No assignment map is supplied with D.

**Other choices that were possible.**

- (a) a declared map asg: V ⇀ J supplied with the organization (it would be a supplied role assignment, which L109's first sentence denies)
- (b) asg(v) := the unique component of which v is an output in L109's second sense; this fails for relational components (a component L = H cot θ determines H given L and θ as well as L given H and θ)
- (c) a setting edit that adds a constraint beside the old one (L103 excludes it)

**Used by.** Formal core §2, §4. Claims: FC02, FC06, FC07, FC08, FC11, FC13, FC25, FC26, FC27.

**Results that depend on it.** FC02 — holds on all models tried; FC06 — holds on all models tried; FC07 — holds on all models tried; FC08 — holds on all models tried; FC11 — holds on all models tried; FC13 — holds on all models tried; FC25 — counterexample ((b) with a port of D in no footprint); FC26 — holds on all models tried; FC27 — holds on all models tried.
### I05 · 'Output': at the identity edit, and 'determined' as at most one value

**The sentence it fills in for.**

> L109 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

**What was invented.** v is an output of j when, for every b in B and all w, w' in L_j(1,b), w and w' agreeing off v implies w_v = w'_v. The relation is read at the identity edit; 'determined' means at most one value (a partial function), not exactly one.

**Other choices that were possible.**

- at every edit of A that does not replace j
- exactly one value for every admissible value of the other ports (a total function)
- 'across B' read as 'for some b'

**Used by.** Formal core §2. Claims: FC02.

**Results that depend on it.** FC02 — holds on all models tried.
### I06 · Observation edits: two readings of 'the relation reporting it'

**The sentence it fills in for.**

> L109 | A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below).

> L127 | In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows.

**What was invented.** The observed port is the reading o (the port the reporting component assigns), and 'what it reports' is a port m read by that component, compared at the level of relations: the edit leaves L_asg(m) as it was. Two readings of which edits count are both carried, since the text does not decide between them. Reading R-i: any edit that alters asg(o) and leaves asg(m) as it was, including an edit that sets o (the reading the round-1 critical review uses: 'an intervention on the reading is, by L109, an observation edit for the measured port'; it also matches L127's 'a part that reads … another part has a measurement's signature'). Reading R-ii: only an edit that alters asg(o) without setting o (a recalibration of the reporting relation). Where a program has to choose one, it runs both and reports both.

**Other choices that were possible.**

- 'the relation reporting it' read with the port as the thing reported (then the 'that is' clause, which speaks of the component assigning the port, no longer matches)
- 'what it reports' compared at the level of solutions: the projection of Sol on m unchanged
- a declared measured port for each observation (a supplied role, against L109's first sentence)

**Used by.** Formal core §2, §4. Claims: FC07, FC08, FC13.

**Results that depend on it.** FC07 — holds on all models tried; FC08 — holds on all models tried; FC13 — holds on all models tried.
### I07 · 'The measured port' and 'the measuring relation'

**The sentence it fills in for.**

> L124 | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

**What was invented.** Measurement is a relation between a component j and a port m: m is in V_j and is not assigned by j; 'the measuring relation' is L_j itself; 'edits to the measuring relation' are, under R-i, edits that alter L_j, and under R-ii, edits that alter L_j without setting j's output. A component with several read ports is a measurement of each separately.

**Other choices that were possible.**

- the measured port declared with the component
- the measuring relation as a separate component reading m

**Used by.** Formal core §4. Claims: FC06, FC07, FC08.

**Results that depend on it.** FC06 — holds on all models tried; FC07 — holds on all models tried; FC08 — holds on all models tried.
### I08 · 'Interventions on the world' and 'the rule'

**The sentence it fills in for.**

> L125 | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

**What was invented.** 'The rule' is the component j itself; 'edits to the rule' are edits that alter L_j without setting j's output; 'interventions on the world' are setting edits of every port that j does not assign.

**Other choices that were possible.**

- 'the world' as the ports j reads only
- 'the rule' as a port whose value j reads (a rule carried as data, as the relation C_r of L347 might be read)

**Used by.** Formal core §4. Claims: FC09, FC10, FC13.

**Results that depend on it.** FC09 — holds on all models tried; FC10 — holds on all models tried; FC13 — holds on all models tried.
### I09 · 'Changes under', 'invariant under', 'variable under': compared with the identity edit at the same boundary

**The sentence it fills in for.**

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

**What was invented.** For a class 𝒳 of edits: j's signature changes (is variable) under 𝒳 on C when some (a,b) in C with a in 𝒳 has L_j(a,b) ≠ L_j(1,b); it is invariant under 𝒳 on C when every (a,b) in C with a in 𝒳 has L_j(a,b) = L_j(1,b). The comparison is with the identity edit at the same boundary, whether or not (1,b) is in C. Invariance is met vacuously when C holds no edit of 𝒳.

**Other choices that were possible.**

- compare with the baseline pair (1,b0) instead of (1,b)
- compare only pairs that are both in C
- 'changes under intervention' read universally (every such intervention changes it)

**Used by.** Formal core §4. Claims: FC06, FC07, FC10, FC11, FC12, FC13.

**Results that depend on it.** FC06 — holds on all models tried; FC07 — holds on all models tried; FC10 — holds on all models tried; FC11 — holds on all models tried; FC12 — holds on all models tried; FC13 — holds on all models tried.
### I10 · Kinds: a footprint bijection between equal value domains, relations compared as sets

**The sentence it fills in for.**

> L119 | Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide.

**What was invented.** j and j' are of one kind on C when some bijection β: V_j → V_j' with X_v = X_β(v) for every v gives L_j'(a,b) = β_*(L_j(a,b)) for every (a,b) in C, where β_* renames coordinates. Values are compared as elements.

**Other choices that were possible.**

- allow a value bijection for each port as well (kinds up to recoding of values; far coarser)
- require β to be the identity on the ports the two components share

**Used by.** Formal core §4. Claims: FC03, FC04, FC05, FC16, FC18, FC96, FC103, FC109.

**Results that depend on it.** FC03 — holds on all models tried; FC04 — holds on all models tried; FC05 — counterexample ((ii) reading (ii): any bijection); FC16 — holds on all models tried; FC18 — counterexample (untranslated reading (I94)); FC96 — holds on all models tried; FC103 — holds on all models tried; FC109 — holds on all models tried.
### I11 · 'Coarser' and 'finer' contracts: fewer and more pairs

**The sentence it fills in for.**

> L119 | Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract.

> L317 | A finer contract that contains a change at which two rivals conflict makes a new question (Part III)

**What was invented.** C' is coarser than C when C' ⊆ C, finer when C' ⊇ C (both on the same target, with the same baseline).

**Other choices that were possible.**

- coarser as the image of C under a quotient of edits or boundaries (a coarser grain)
- coarser as fewer distinguishable pairs, however many pairs it has

**Used by.** Formal core §4. Claims: FC04, FC50.

**Results that depend on it.** FC04 — holds on all models tried; FC50 — holds on all models tried.
### I12 · Reading a candidate's component on C through the transport; τ[C]

**The sentence it fills in for.**

> L119 | A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection

> L554 | no active component \(k\) of \(E\) has a signature on \(\tau[C]\) that differs from the one its counterpart \(\lambda(k)\) has on \(C\), up to the port translation.

**What was invented.** The signature of k in E read on C through t = (π,τ,σ,λ) is the function on C sending (a,b) to L_k(τ(a),σ(b)); boundaries are translated by σ although L119 names only τ. τ[C] := {(τ(a),σ(b)) : (a,b) in C}. Signatures on C and on τ[C] are compared as functions on C.

**Other choices that were possible.**

- read through τ only, with E's boundary held at σ(b0)
- τ[C] as a set of edits only
- compare the two signatures as sets of triples, which needs τ×σ injective on C

**Used by.** Formal core §4. Claims: FC15, FC16, FC17, FC29, FC96, FC109.

**Results that depend on it.** FC15 — holds on all models tried; FC16 — holds on all models tried; FC17 — holds on all models tried; FC29 — holds on all models tried; FC96 — holds on all models tried; FC109 — holds on all models tried.
### I13 · (K) extended from components to subnetworks

**The sentence it fills in for.**

> L556 | By (K), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\)

**What was invented.** (K) is stated for a component. For a subnetwork N of D with a port translation θ into it, sig_C(N,θ) := {(a,b, proj^θ Sol_N(a,b)) : (a,b) in C} is taken as a definition (an extension of (K)), not as something (K) already gives.

**Other choices that were possible.**

- treat a subnetwork as one composite component whose relation is the projected relation (then (K) applies as written)
- leave Argument 1's 'By (K)' without a definition to rest on

**Used by.** Formal core §4. Claims: FC17, FC18, FC109.

**Results that depend on it.** FC17 — holds on all models tried; FC18 — counterexample (untranslated reading (I94)); FC109 — holds on all models tried.
### I14 · Subnetworks, their solutions, and port translations with value maps

**The sentence it fills in for.**

> L189 | \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation.

> L233 | the relation obtained by imposing the constraints of \(\lambda(k)\), projecting away its hidden ports and carrying what remains to \(V_k\) by the port translation of \(\lambda\)

**What was invented.** A subnetwork N is a subset of J_D (possibly empty); V_N is the union of its footprints; Sol_N(a,b) = {z in ∏_{V_N} X_v : z|V_j ∈ L_j(a,b) for every j in N}: the constraints of N alone, the rest of D ignored. A port translation for k is an injective map θ_k: V_k → V_N with a value map κ_v: X^D_θk(v) → X^E_v for each v (the identity where the domains agree). Hidden ports are V_N minus the image of θ_k. proj^λ_Vk(S) = {(κ_v(z_θk(v)))_{v in V_k} : z in S}.

**Other choices that were possible.**

- Sol of λ(k) in the context of the whole of D (the projection of Sol_D)
- a port translation as a map from V_N to V_k (several D ports to one E port)
- a subnetwork as a set of ports rather than of components

**Used by.** Formal core §1, §5. Claims: FC17, FC18, FC19, FC25, FC44, FC62, FC96, FC103, FC109.

**Results that depend on it.** FC17 — holds on all models tried; FC18 — counterexample (untranslated reading (I94)); FC19 — holds on all models tried; FC20 — counterexample (any value map κ); FC25 — counterexample ((b) with a port of D in no footprint); FC44 — holds on all models tried; FC62 — holds on all models tried; FC96 — holds on all models tried; FC103 — holds on all models tried; FC109 — holds on all models tried.
### I15 · 'Active component' means a member of Γ

**The sentence it fills in for.**

> L233 | **Component fidelity.** For every active component \(k\) of \(E\) with counterpart subnetwork \(\lambda(k)\subseteq D\)

**What was invented.** The active components of a candidate are exactly its commitments Γ; (F1) is required of these only.

**Other choices that were possible.**

- every component of E
- every component with a counterpart assigned by λ (L189 has λ assign one to every component)

**Used by.** Formal core §5. Claims: FC17, FC19.

**Results that depend on it.** FC17 — holds on all models tried; FC19 — holds on all models tried.
### I16 · The domain of π: 'on the stated scope'

**The sentence it fills in for.**

> L189 | where \(\pi:X_D\to X_E\) on the stated scope

**What was invented.** π is a map defined at least on the union of Sol_D(a,b) over the pairs (a,b) the transport translates; elsewhere it may be undefined.

**Other choices that were possible.**

- π total on X_D
- π a relation (several images per valuation)

**Used by.** Formal core §5. Claims: FC20, FC49.

**Results that depend on it.** FC20 — counterexample (any value map κ); FC49 — holds on all models tried.
### I17 · Partial τ and σ; which pairs a transport 'translates'

**The sentence it fills in for.**

> L315 | they conflict at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it.

**What was invented.** τ: A_D ⇀ A_E and σ: B_D ⇀ B_E are partial maps; t translates (a,b) when a is in dom τ, b is in dom σ and π is defined on Sol_D(a,b).

**Other choices that were possible.**

- τ and σ total (then every admitted pair is translated)
- 'translate' read as 'is in C'

**Used by.** Formal core §5. Claims: FC45, FC49.

**Results that depend on it.** FC45 — holds on all models tried; FC49 — holds on all models tried.
### I18 · The homomorphism clause of (F2): its range, and that it is not pointwise

**The sentence it fills in for.**

> L242 | \tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1).

**What was invented.** τ(1) = 1, and for all a1, a2 in dom τ with a2·a1 defined in A_D, τ(a2)·τ(a1) is defined in A_E and equals τ(a2·a1). The clause is a condition on τ as a whole, not at a pair; '(F2) at a pair' means only the valuation equation there.

**Other choices that were possible.**

- only for edits occurring in C, and composites that are in C
- only when both composites are defined
- the clause counted at each pair (then (F2) at a pair depends on edits outside it)

**Used by.** Formal core §5. Claims: FC15, FC51.

**Results that depend on it.** FC15 — holds on all models tried; FC51 — holds on all models tried; FC77 — counterexample (with H = ∅ and an empty selection history).
### I19 · Meeting (F1), (F2) and (A) at one pair under hypothetical relations of the target

**The sentence it fills in for.**

> L315 | when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both

**What was invented.** For a pair (a,b) and an assignment R = (R_j)_{j in J_D}, R_j ⊆ ∏_{V_j} X_v: D^R is D with its relations at (a,b) replaced by R; Meets_ab(ℰ,R) is (F1) at (a,b) for every k in Γ with Sol_λ(k) computed from R, the valuation equation of (F2) with Sol_D^R, and (A) with the target's answer computed by the query on D^R. The homomorphism clause is left out at a pair (I18). R ranges over every assignment of relations on the footprints.

**Other choices that were possible.**

- include the homomorphism clause
- R ranging only over assignments some physics admits (L315 excludes it: 'it does not turn on what any physics admits')
- R ranging over the relations the target has at other admitted pairs

**Used by.** Formal core §8. Claims: FC44, FC45, FC46, FC47, FC52, FC54.

**Results that depend on it.** FC44 — holds on all models tried; FC45 — holds on all models tried; FC46 — holds on all models tried; FC47 — holds on all models tried; FC52 — holds on all models tried; FC54 — holds on all models tried.
### I20 · How the fixed query is applied to a candidate's organization

**The sentence it fills in for.**

> L141 | \(\mathcal Q\) is a specified set-theoretic operation on \(D\), its solutions and its component structure, with codomain \(Y_p\).

> L253 | The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one.

**What was invented.** Q is an operation on any evaluated organization (O, a, b), taking Sol_O(a,b), the relations (L_j(a,b))_j and a designation δ_O of the ports and components it reads; its values lie in Y_p. For the target, δ_D is part of the question. For a candidate, δ_E is supplied with the transport: by default, the ports of E whose translations are the ports Q reads in D. Ans_E(a',b') := Q(E, a', b'; δ_E).

**Other choices that were possible.**

- (a) Ans_E supplied as part of the candidate (then 'held fixed' constrains only a label)
- (b) a shared space of port names, Q reading by name
- (c) Ans_E computed from the π-preimage of Sol_E

**Used by.** Formal core §0, §3, §5. Claims: FC20, FC26, FC28, FC30, FC32, FC45, FC68, FC98.

**Results that depend on it.** FC20 — counterexample (any value map κ); FC26 — holds on all models tried; FC28 — holds on all models tried; FC30 — holds on all models tried; FC32 — not tested; FC45 — holds on all models tried; FC68 — holds on all models tried; FC98 — not tested.
### I21 · Undetermined answers: a value ⊥

**The sentence it fills in for.**

> L255 | the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.

**What was invented.** Q returns an element of Y_p or ⊥ ('not determined'); for a query reading a port, the answer is determined when the port's projection of Sol is a single value, and is ⊥ when it is empty or has several. Two ⊥ answers count as equal where answers are compared (conflict, (A)).

**Other choices that were possible.**

- Q returns the set of possible values, 'determined' meaning a singleton
- ⊥ split into 'none' and 'several'
- two ⊥ answers counted as different

**Used by.** Formal core §0, §3, §5, §6. Claims: FC20, FC21, FC22, FC23, FC26, FC46, FC48.

**Results that depend on it.** FC20 — counterexample (any value map κ); FC21 — holds on all models tried; FC22 — holds on all models tried; FC23 — counterexample ((b) as stated); FC26 — holds on all models tried; FC46 — holds on all models tried; FC48 — holds on all models tried.
### I22 · 'Not determined … in the claimed way'

**The sentence it fills in for.**

> L255 | or is not determined at \((\tau(a),\sigma(b))\) in the claimed way

**What was invented.** 'Differs' is read for two determined answers that are unequal. The second disjunct is a contrast of determinacy: Ans_E(τ(a),σ(b)) = ⊥ while Ans_E(1,σ(b0)) ≠ ⊥, where (A) makes the target's answer at (a,b) ⊥ as well; 'in the claimed way' is read as the candidate's answer there being ⊥, as the target's is.

**Other choices that were possible.**

- a declared input saying in what way the answer is claimed to be undetermined (for example, which values remain)
- drop the clause: the contrast is 'differs' only

**Used by.** Formal core §6. Claims: FC21, FC22, FC23.

**Results that depend on it.** FC21 — holds on all models tried; FC22 — holds on all models tried; FC23 — counterexample ((b) as stated).
### I23 · The first sentence of non-circular dependence, read as a heading gloss

**The sentence it fills in for.**

> L255 | **Non-circular dependence.** The answer follows by evaluating \(E\) under its independent boundary conditions.

**What was invented.** The sentence adds no condition of its own: every answer in the formal core is computed by evaluating E at (τ(a),σ(b)), and σ(b) is fixed by b alone ('independent'). It is recorded as NC0 and is met by every candidate.

**Other choices that were possible.**

- a condition that E's boundary data carry nothing of the target's answer beyond σ(b) (formally automatic here, since σ is a function of b)
- a condition on how E's answer is computed (by propagation, not lookup), which would need a notion of computation the text does not give

**Used by.** Formal core §6. Claims: FC108.

**Results that depend on it.** FC108 — holds on all models tried.
### I24 · NC1: the target's answer as an unanalysed boundary input or component, read structurally

**The sentence it fills in for.**

> L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements.

**What was invented.** NC1 fails when E has a single component k (or a boundary coordinate) such that, for every (a,b) in C, L_k(τ(a),σ(b)) (or the boundary value at σ(b)) is exactly the relation that fixes E's designated answer ports to the target's answer Ans_p(a,b) and constrains nothing else: an 'answer slot'. 'Structural at the grain' = equality of relations of one component of E as given, not equality up to logical equivalence of statements.

**Other choices that were possible.**

- (a) leave NC1 out: non-circular dependence is the final sentence (NC2) alone
- (b) any single component whose relation by itself fixes the answer (semantic entailment)
- (c) syntactic identity of written assertions (needs a syntax of relations that (O) does not give)

**Used by.** Formal core §6, §9. Claims: FC23, FC24, FC26, FC33, FC34, FC51, FC60.

**Results that depend on it.** FC23 — counterexample ((b) as stated); FC24 — holds on all models tried; FC26 — holds on all models tried; FC33 — holds on all models tried; FC34 — holds on all models tried; FC51 — holds on all models tried; FC60 — holds on all models tried.
### I25 · Non-circular dependence is the conjunction of its sentences

**The sentence it fills in for.**

> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that

**What was invented.** NonCircular(ℰ) := NC0 ∧ NC1 ∧ NC2, where NC2 is the existential final sentence. The earlier sentences are conditions, not commentary on NC2.

**Other choices that were possible.**

- NC2 alone is the condition; the earlier sentences explain it
- NC1 alone is the condition; NC2 illustrates it

**Used by.** Formal core §6. Claims: FC23.

**Results that depend on it.** FC23 — counterexample ((b) as stated).
### I26 · 'Relabelings'

**The sentence it fills in for.**

> L257 | A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets non-circular dependence

**What was invented.** An edit a is a relabeling for p when, at every b with (a,b) in C, the target's answer is determined and equal to its answer at the baseline: Ans_p(a,b) = Ans_p(1,b0) ≠ ⊥.

**Other choices that were possible.**

- an edit that acts on D as an automorphism (renaming ports or values)
- an edit that changes no relation of D at all

**Used by.** Formal core §6. Claims: FC21.

**Results that depend on it.** FC21 — holds on all models tried.
### I27 · The stated scope: a declared statement over pairs

**The sentence it fills in for.**

> L257 | The contract \(C\) is a stated subset of the edits the target admits, and every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently.

**What was invented.** A scope statement Σ is a declared input naming a set Excl(Σ) ⊆ A_D × B_D; the clause holds when (A_D × B_D) \ C ⊆ Excl(Σ). Pairs, not edits, are what C excludes. Every a in A_D counts as an edit the target admits.

**Other choices that were possible.**

- edits rather than pairs: every a with no pair in C is named in Σ
- Σ as a yes/no flag ('the scope is stated')

**Used by.** Formal core §0, §3, §6. Claims: FC26, FC30, FC32, FC33, FC34, FC51, FC63.

**Results that depend on it.** FC26 — holds on all models tried; FC30 — holds on all models tried; FC32 — not tested; FC33 — holds on all models tried; FC34 — holds on all models tried; FC51 — holds on all models tried; FC63 — counterexample ((c-i) the Leibniz candidate, sum over every tuple of term values).
### I28 · The grain as a label on the organizations compared

**The sentence it fills in for.**

> L255 | The target's answer does not appear, at the declared grain

**What was invented.** The grain ℓ is carried as an index on each organization (E at grain ℓ is a given organization); NC1 and ≡_ℓ are evaluated on the organizations as given at that index. No map between grains is defined.

**Other choices that were possible.**

- a grain as a quotient map from a finer organization to a coarser one (components of the coarse one as unions of fine ones)

**Used by.** Formal core §6. Claims: FC30, FC32, FC33.

**Results that depend on it.** FC30 — holds on all models tried; FC32 — not tested; FC33 — holds on all models tried.
### I29 · The restriction operation (E restricted to W): deletion

**The sentence it fills in for.**

> L287 | Fix \(\mathcal E\) and a declared restriction operation. For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).

**What was invented.** E|W is E with every component of Γ \ W deleted (full relation at every edit and boundary, as L103 gives for deletion), the background untouched, J_E and V_E unchanged; the transport is t with λ restricted to W; the commitments are W.

**Other choices that were possible.**

- remove Γ \ W from J_E (their ports then free, or removed)
- some other declared operation: the text names the operation as declared, and it is not among the declared inputs of L522

**Used by.** Formal core §0, §7. Claims: FC41, FC98, FC101.

**Results that depend on it.** FC41 — holds on all models tried; FC98 — not tested; FC101 — holds on all models tried.
### I30 · The worked examples of routes are set systems

**The sentence it fills in for.**

> L307 | **Redundant routes.** \(\Gamma=\{a,b\}\), \(\mathsf S=\{\{a\},\{b\},\{a,b\}\}\)

**What was invented.** The examples of L305–L313 are read as statements about families S ⊆ P(Γ), not about a particular question and candidate; where a test needs a candidate that realizes one, the realization is a further invention, recorded with the test.

**Other choices that were possible.**

- realize each example by a concrete target, question and candidate before reading it

**Used by.** Formal core §7. Claims: FC38, FC39, FC40, FC42.

**Results that depend on it.** FC38 — holds on all models tried; FC39 — holds on all models tried; FC40 — holds on all models tried; FC42 — holds on all models tried.
### I31 · The routes of the infinitary example

**The sentence it fills in for.**

> L311 | every set of indices unbounded in \(\mathbb N\) determines \(x=0\); no minimal route, and no route of one commitment, exists.

**What was invented.** The routes are exactly the sets W whose index set {n : d_n ∈ W} is unbounded; a bounded set leaves x anywhere in [-1/max, 1/max] and is not a route; the empty set is not a route. (The question is read as 'is x determined to be 0?'.)

**Other choices that were possible.**

- the text does not say that bounded sets are not routes; another question (for example 'is |x| ≤ 1/N for a stated N?') gives another route family

**Used by.** Formal core §7. Claims: FC40.

**Results that depend on it.** FC40 — holds on all models tried.
### I32 · A table of observed answers: its counterpart and its relation

**The sentence it fills in for.**

> L269 | A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing one.

**What was invented.** The table is a candidate with one active component k whose counterpart is the whole of D (all of J_D, projected onto k's ports) and whose relation is the same under every edit: the relation D gives at the baseline. 'An intervention' is a setting edit (I04).

**Other choices that were possible.**

- the table's counterpart is only the subnetwork around the answer port
- a table keyed by edits (then it is the other kind L269 names, which encodes the response)

**Used by.** Formal core §6. Claims: FC25.

**Results that depend on it.** FC25 — counterexample ((b) with a port of D in no footprint).
### I33 · The offer of one candidate in place of another: a primitive

**The sentence it fills in for.**

> L315 | Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other

**What was invented.** Offered(ℰ, ℰ', p) is a primitive relation (a record of offers), not defined in the formal core; rivals are symmetric (either one offered in place of the other).

**Other choices that were possible.**

- offers as events in histories, read through the physical module
- offers as a declared input (L522 does not list them)

**Used by.** Formal core §0, §8. Claims: FC43, FC49, FC50, FC54, FC98.

**Results that depend on it.** FC43 — holds on all models tried; FC49 — holds on all models tried; FC50 — holds on all models tried; FC54 — holds on all models tried; FC98 — not tested.
### I34 · A claim χ as a set of allowed behaviours at a pair, and the premise that it speaks of the target

**The sentence it fills in for.**

> L315 | A candidate **conflicts with** a claim \(\chi\) at an admitted pair of the target that its transport translates, in \(C\) or outside it, when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there.

> L315 | Either way the argument needs the premise that \(\chi\) speaks of the target under that pair's edit.

**What was invented.** At each pair, χ is modelled as a set Allow_χ(a,b) of assignments R of relations to the target's components (the behaviours χ allows). 'χ excludes its answer' := every R whose query answer is Ans_E(τ(a),σ(b)) lies outside Allow_χ(a,b). 'χ excludes every relation under which it could meet' := every R with Meets_ab(ℰ,R) lies outside Allow_χ(a,b). The premise that χ speaks of the target under the pair's edit is a separate yes/no input Applies(χ,a,b).

**Other choices that were possible.**

- χ as a sentence of a language with its own semantics, related to behaviours by a declared reading
- χ as constraining answers only (then the second disjunct cannot be expressed)

**Used by.** Formal core §0, §8. Claims: FC52, FC53, FC54, FC98.

**Results that depend on it.** FC52 — holds on all models tried; FC53 — holds on all models tried; FC54 — holds on all models tried; FC98 — not tested.
### I35 · Conflict given χ: no requirement that each candidate can meet under χ

**The sentence it fills in for.**

> L315 | Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation, conflict there given \(\chi\)

**What was invented.** ConflictGiven_χ(ℰ,ℰ';a,b) := some R lets both meet at (a,b), and every such R lies outside Allow_χ(a,b). Nothing is required of what each can meet under χ alone.

**Other choices that were possible.**

- the second disjunct of plain conflict with R restricted to Allow_χ: each can meet under some allowed R, and no allowed R lets both

**Used by.** Formal core §8. Claims: FC54.

**Results that depend on it.** FC54 — holds on all models tried.
### I36 · 'Two of their active components with one counterpart'

**The sentence it fills in for.**

> L315 | as none do when two of their active components with one counterpart have different relations there.

**What was invented.** k in Γ and k' in Γ' have one counterpart when λ(k) = λ'(k') as subnetworks, their port translations have the same image, and θ'^-1∘θ is a bijection V_k → V_k' with matching value maps; 'different relations there' means L_k'(τ'(a),σ'(b)) ≠ β_*(L_k(τ(a),σ(b))) under that bijection β.

**Other choices that were possible.**

- one counterpart = the same subnetwork, whatever the port translations (then the clause can fail: the translations can carry one projected relation to two different relations)

**Used by.** Formal core §8. Claims: FC44.

**Results that depend on it.** FC44 — holds on all models tried.
### I37 · 'Easy to vary' is relative to an assessor

**The sentence it fills in for.**

> L317 | A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind

**What was invented.** ETV_j(ℰ) := for some ℰ', Problem_j(ℰ,ℰ';p) holds and is of the second kind. It inherits the assessor from 'problem'. (What hard to vary covers is parked by decisions S33–S34; this formalization touches only the text's 'easy to vary' and adds nothing about it.)

**Other choices that were possible.**

- assessor-free: some rival conflicts with it only outside C, ruled out or not
- for some assessor

**Used by.** Formal core §10. Claims: FC43.

**Results that depend on it.** FC43 — holds on all models tried.
### I38 · Claims, their denials, and 'inconsistent with its conclusion'

**The sentence it fills in for.**

> L397 | An argument is usable by \(j\) when each of its steps is (K2), and it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below).

**What was invented.** Claims are sentences of a first-order language with classical ¬ and ∧; 'inconsistent with' is classical inconsistency of {φ, conclusion}. Inference forms themselves are arbitrary (an admitted form need not be classically sound); only the ruling-out relation uses classical consistency.

**Other choices that were possible.**

- inconsistency relative to j's own admitted forms
- claims as sets of situations, inconsistency as disjointness

**Used by.** Formal core §9. Claims: FC47, FC53, FC56, FC68, FC71, FC72, FC73.

**Results that depend on it.** FC47 — holds on all models tried; FC53 — holds on all models tried; FC56 — holds on all models tried; FC68 — holds on all models tried; FC71 — holds on all models tried; FC72 — holds on all models tried; FC73 — holds on all models tried.
### I39 · 'Among its premises', read structurally; records made from a claim

**The sentence it fills in for.**

> L397 | An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone; nor does an argument whose record leaf was made from a claim rule out that claim's denial.

**What was invented.** ¬φ is among the premises when some leaf, flattened as a conjunction, has ¬φ as a conjunct, up to renaming of bound variables and the order of conjuncts. 'Made from a claim' is a primitive relation MadeFrom(leaf, ψ) on record leaves.

**Other choices that were possible.**

- up to a declared set of structural rewrites
- logical equivalence (the text excludes it)

**Used by.** Formal core §0, §9. Claims: FC60, FC72, FC98.

**Results that depend on it.** FC60 — holds on all models tried; FC72 — holds on all models tried; FC98 — not tested.
### I40 · Live through a step: a step below, and essential premises

**The sentence it fills in for.**

> L387 | **Usability.** For argument step \(u\) with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:

> L393 | \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\)

**What was invented.** An argument is a finite tree; Prem(u) is the set of u's children that its form uses. The step whose conclusion makes d live lies in the subtree below u, so Usable is defined by recursion on height and is well founded.

**Other choices that were possible.**

- any step of the argument, the definition read as a least fixed point
- arguments as finite acyclic graphs, one node shared by several steps

**Used by.** Formal core §9. Claims: FC47, FC53, FC56, FC68, FC69, FC70.

**Results that depend on it.** FC47 — holds on all models tried; FC53 — holds on all models tried; FC56 — holds on all models tried; FC68 — holds on all models tried; FC69 — holds on all models tried; FC70 — holds on all models tried.
### I41 · Tentative acceptance over time; withdrawal

**The sentence it fills in for.**

> L393 | or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it

**What was invented.** Accepted_j(ξ) is the set of claims j has taken up before ξ and not withdrawn before ξ; Live, Usable and ruled out are evaluated at a time ξ. Accepted_j is a declared input (L522).

**Other choices that were possible.**

- untimed sets (one assessor state)

**Used by.** Formal core §9. Claims: FC56, FC68, FC70.

**Results that depend on it.** FC56 — holds on all models tried; FC68 — holds on all models tried; FC70 — holds on all models tried.
### I42 · Scope_j: within the declared contract, grain and boundary

**The sentence it fills in for.**

> L393 | \(\operatorname{Scope}_j(u)\): \(u\) is applied within the contract, grain and boundary \(j\) has declared for it

**What was invented.** Each step u carries an index (C_u, ℓ_u, β_u); j declares (C_j(u), ℓ_j(u), β_j(u)); Scope_j(u) holds when C_u ⊆ C_j(u), ℓ_u = ℓ_j(u) and β_u = β_j(u).

**Other choices that were possible.**

- equality of contracts
- steps without an index, Scope_j vacuous for them

**Used by.** Formal core §9. Claims: FC47.

**Results that depend on it.** FC47 — holds on all models tried.
### I43 · (K3): what it adds and what 'nothing narrower' says

**The sentence it fills in for.**

> L395 | For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\) rules out \(T\land B\land I\) together for \(j\), and nothing narrower. (K3)

**What was invented.** (i) If j has a usable argument concluding ¬O, the conditional T∧B∧I ⇒ O is live for j and j admits modus tollens, the argument extended by one step rules out T∧B∧I for j. (ii) 'Nothing narrower': from those premises alone no argument rules out T, B or I by itself, since classically ¬O, T∧B∧I ⇒ O and T have a common model.

**Other choices that were possible.**

- (K3) as a restriction on j's admitted forms (j admits no form that concludes ¬T from them)
- (K3) as a definition of what a test rules out, not a consequence of (K2)

**Used by.** Formal core §9. Claims: FC47, FC71.

**Results that depend on it.** FC47 — holds on all models tried; FC71 — holds on all models tried.
### I44 · Causal precedence in a history is transitive

**The sentence it fills in for.**

> L375 | A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure)

**What was invented.** ≺_h is a strict partial order (irreflexive and transitive), so ⪯_h is a partial order.

**Other choices that were possible.**

- ≺_h any acyclic relation and ⪯_h its reflexive closure only (then ⪯_h need not be transitive)
- ⪯_h the reflexive-transitive closure of an acyclic ≺_h

**Used by.** Formal core §11, §14. Claims: FC75, FC90.

**Results that depend on it.** FC75 — holds on all models tried; FC90 — not tested.
### I45 · 'Event' is a set of occurrences

**The sentence it fills in for.**

> L169 | An **occurrence** is a physically located carrier.

> L161 | Its formulation is still an event.

> L397 | A record leaf is a reference to an event with an interpreted claim.

**What was invented.** An event is a nonempty set of occurrences of a history; a record leaf refers to one; an assessment and a formulation are events. 'Event' adds no sort beyond occurrences.

**Other choices that were possible.**

- events as a separate primitive sort
- events as occurrences of edit–boundary pairs only

**Used by.** Formal core §11. Claims: FC74, FC100, FC105.

**Results that depend on it.** FC74 — holds on all models tried; FC100 — holds on all models tried; FC105 — not tested.
### I46 · Active route: 'represented input', 'operative result', 'applicable relations', 'declared contrasts'

**The sentence it fills in for.**

> L375 | An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.

**What was invented.** Given the organization Org_ℓ(h) that the physical module assigns to the history h: an active route for a result occurrence r is a set R of occurrences of h, connected by the instantiated connections, containing an input occurrence i whose port carries a represented distinction and the result occurrence r (the 'operative result' is a designated result occurrence); every occurrence of R lies on a ≺_h-chain from i to r inside R; each occurrence of R meets the relation Org_ℓ(h) gives it ('the applicable relations'); and for a declared set K of pairs of values of i's port, setting i's port to the two values of some pair in K gives different values at r in Org_ℓ(h).

**Other choices that were possible.**

- 'operative result' = a result that later changes how the system proceeds (L73's operative return)
- dependence read on the actual history only, without setting i's port
- 'connected' read without direction

**Used by.** Formal core §0, §11. Claims: FC75, FC87, FC98, FC101.

**Results that depend on it.** FC75 — holds on all models tried; FC87 — holds on all models tried; FC98 — not tested; FC101 — holds on all models tried.
### I47 · Reason use: 'structural map', 'role bindings', 'the same transition', 'operative deliberative rule'

**The sentence it fills in for.**

> L385 | **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.

**What was invented.** The represented objection ob is a content with role bindings (a map from role names to its ports); a structural map m sends ob's ports to ports of the response suborganization R, preserving role names; Rec is a declared set of content-preserving recodings and Chg a declared set of content changes of ob; m(ρ·ob) induces the same state change of R as m(ob) for ρ in Rec; m(γ·ob) = Rule(γ)(m(ob)) for γ in Chg, with Rule a declared map ('the operative deliberative rule'); some image port of m lies on an active route (I46).

**Other choices that were possible.**

- the deliberative rule as a component of the system's organization, picked out by its signature
- the structural map as a transport (π,τ,σ,λ), making reason use a fidelity condition

**Used by.** Formal core §0, §9. Claims: FC76, FC98.

**Results that depend on it.** FC76 — holds on all models tried; FC98 — not tested.
### I48 · Contents, 'c's contract', and transports into a content

**The sentence it fills in for.**

> L169 | A **content** is an organization together with its contract-relative commitments.

> L205 | faithful on \(c\)'s contract, whose provenance is selected or constructed

> L413 | both faithful on \(c\)'s contract at grain \(\ell\).

**What was invented.** A content is c = (E_c, C_c, Γ_c) with C_c ⊆ A_Ec × B_Ec a contract on c's own organization (for the organization of a candidate for p: C_c := τ[C_p]). A transport t: X → E_c is faithful on c's contract when it meets (F1) and (F2) on the preimage {(a,b) ∈ A_X × B_X : (τ(a),σ(b)) ∈ C_c}, with Γ_c as the active components; a transport from c is faithful on C_c directly.

**Other choices that were possible.**

- a separately declared contract on the carrier's organization
- faithfulness on C_c read through a declared inverse of τ

**Used by.** Formal core §11, §12, §13. Claims: FC77, FC85, FC95, FC97.

**Results that depend on it.** FC77 — counterexample (with H = ∅ and an empty selection history); FC85 — holds on all models tried; FC95 — holds on all models tried; FC97 — holds on all models tried.
### I49 · 'Faithful' and 'fidelity': the narrow extent by default, the wide one where a line asks for it

**The sentence it fills in for.**

> L189 | A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V.

> L247 | **Question fidelity.**

> L520 | Account, from fidelity under change, non-circular dependence and non-vacuity (E).

> L630 | so the exchange carries the fidelity and the answers of \(t_1\) over to the second transport

**What was invented.** Faithful_C(t) := (F1) ∧ (F2) on C (the narrow extent L189 defines). Fid⁺_C(t) := (F1) ∧ (F2) ∧ (A) on C (the wide extent, used where a line names (A) as fidelity: L247's heading, L520). Each use of the word is assigned one extent in FC104.

**Other choices that were possible.**

- wide everywhere (then L630's 'the fidelity and the answers' says one thing twice)
- narrow everywhere (then L520 names no source for (A) and L247's heading is a name only)

**Used by.** Formal core §5. Claims: FC20, FC31, FC79, FC104.

**Results that depend on it.** FC20 — counterexample (any value map κ); FC31 — not tested; FC79 — holds on all models tried; FC104 — not tested.
### I50 · A violation at a pair: which conditions fail

**The sentence it fills in for.**

> L220 | - a **violation** occurs when fidelity fails at \((a,b)\);

**What was invented.** Violation(t;a,b) := not [(F1) at (a,b) and the valuation equation of (F2) at (a,b)] (narrow). Violation⁺ adds (A) at (a,b). Both are carried; FC20 asks when they coincide.

**Other choices that were possible.**

- only (A) at (a,b) (a failed prediction)
- the whole of (F2), homomorphism clause included

**Used by.** Formal core §12. Claims: FC20, FC81, FC104.

**Results that depend on it.** FC20 — counterexample (any value map κ); FC81 — counterexample ((d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC104 — not tested.
### I51 · 'Prediction' for a transport not said to reach the simulation layer

**The sentence it fills in for.**

> L151 | A measure that identifies an outcome, together with a prediction of the outcome from it through a transport faithful on the contract, answers the identification question

**What was invented.** Pred_t(a,b) := Ans_E(τ(a),σ(b)) for any transport t: D → E, extending L219's definition, which is for transports to S.

**Other choices that were possible.**

- L151's 'prediction' in the everyday sense, not the defined term

**Used by.** Formal core §12. Claims: FC35.

**Results that depend on it.** FC35 — not tested.
### I52 · Selection: the parameters witnessed in a physical history

**The sentence it fills in for.**

> L195 | There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

> L195 | No member of the history represents \(t\), \(H\), or the survival condition.

**What was invented.** μ: 𝒯 → P(𝒯); the survival condition is Faithful_H (narrow). Sel(t;𝒯,μ,H) also requires a physical selection history h_sel in which the pairs of H occur and the members of 𝒯 are admitted by the physics (L481), and in which no occurrence represents (R) t, H or the survival condition. 'Member of the history' is read as an occurrence of h_sel, since the members of H are pairs and cannot represent.

**Other choices that were possible.**

- a purely formal Sel with no physical witness (then 𝒯 = {t}, μ the identity and H = ∅ make every transport 'selected': FC77)
- H required to be nonempty

**Used by.** Formal core §12. Claims: FC77, FC78, FC79, FC80, FC81, FC82, FC83, FC95, FC102.

**Results that depend on it.** FC77 — counterexample (with H = ∅ and an empty selection history); FC78 — counterexample (exactly one provenance under I53); FC79 — holds on all models tried; FC80 — holds on all models tried; FC81 — counterexample ((d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 — counterexample (no common result); FC83 — counterexample (only construction is originative); FC95 — holds on all models tried; FC102 — counterexample ((b) second half: a window longer than the occlusion).
### I53 · 'Exactly one of three provenances': one whole history

**The sentence it fills in for.**

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

> L201 | Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both.

**What was invented.** Sel and Con are evaluated on one history: the whole physical history of t up to the attribution. Con then excludes Sel (Con puts a represented target in that history; Sel has none).

**Other choices that were possible.**

- Sel and Con evaluated on different parts of the history (then both can hold, as L201's 'Construction may operate on selected material' allows, and 'exactly one' needs a rule of precedence)

**Used by.** Formal core §12. Claims: FC78, FC81, FC82, FC84.

**Results that depend on it.** FC78 — counterexample (exactly one provenance under I53); FC81 — counterexample ((d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 — counterexample (no common result); FC84 — holds on all models tried.
### I54 · Inherited provenance: a rule of carrying over, per part

**The sentence it fills in for.**

> L211 | A carrier keeps its provenance when present access to it is lost, and a later record made from the carrier carries that provenance, not a second, independent one.

> L405 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.

> L409 | Use does not by itself construct: received content used as it was received keeps its inherited provenance.

**What was invented.** Provenance is assigned to each part of a transport (each component with its counterpart binding). A content-preserving transfer (relay, record) from carrier o to carrier o' gives each part at o' the provenance it had at o; a binding newly built gets Con; 'inherited' is not a fourth value but the rule by which Sel, Con and Dec carry over.

**Other choices that were possible.**

- 'inherited' as a fourth provenance value
- provenance per whole transport only (then L405's 'the rest of the content keeps' cannot be written)

**Used by.** Formal core §12. Claims: FC67, FC78.

**Results that depend on it.** FC67 — holds on all models tried; FC78 — counterexample (exactly one provenance under I53).
### I55 · Deploy: 'integrated into problem-directed activity', 'nontrivial use respect'

**The sentence it fills in for.**

> L403 | integrated into problem-directed activity and serving the declared use task \(U\) as a retained capability (Part XII). The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect.

**What was invented.** Deploy_βℓ(s,c,ξ;U) := for some occurrence o of s at ξ, Rep_ℓ(o,c), Integrated(o,s,ξ) and, for some χ, Can_Ωβ(ξ,U;χ) with a realization that uses o. Integrated and Nontrivial(U) are primitive predicates read through the physical module.

**Other choices that were possible.**

- Integrated defined through active routes (o lies on an active route to a problem's result)

**Used by.** Formal core §0, §13. Claims: FC98.

**Results that depend on it.** FC98 — not tested.
### I56 · Build: 'prepares', 'nontrivial binding construction', 'content-preserving transfer'

**The sentence it fills in for.**

> L405 | **Construction.** \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.

**What was invented.** Build := for some subhistory h' of h ending at e and owned by s, Prepares(h',c), BindingConstruction(h',c) and not TransferComposite(h'), with the three as primitive predicates read through the physical module.

**Other choices that were possible.**

- Build defined through Con (a construction trace)
- BindingConstruction defined through reason use (L409)

**Used by.** Formal core §0, §13, §18. Claims: FC83, FC84, FC98.

**Results that depend on it.** FC78 — counterexample (exactly one provenance under I53); FC81 — counterexample ((d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 — counterexample (no common result); FC83 — counterexample (only construction is originative); FC84 — holds on all models tried; FC98 — not tested.
### I57 · Repair: how the aims are read at ξ and over [ξ, ξ']; which aim ProducedBy runs to

**The sentence it fills in for.**

> L441 | In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).

> L441 | \(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair

**What was invented.** An aim is (cond, Occ) with Occ a set of times. o(ξ) for o in O: cond met at ξ. On the left of (P), r(ξ) := cond met at ξ if ξ ∈ Occ_r, and holds otherwise; on the right, r(ξ') := cond met at every ω ∈ Occ_r with ξ ≤ ω ≤ ξ'. ProducedBy(Δ,ξ,ξ';O) := some o in O with ¬o(ξ) ∧ o(ξ') has an active route from an occurrence of Δ to the occurrence at which its cond comes to be met; it need not be the o of (P)'s first conjunct.

**Other choices that were possible.**

- tie ProducedBy to the same o as the first conjunct
- r(ξ) on the left also read over an interval

**Used by.** Formal core §14. Claims: FC86, FC87, FC88, FC90.

**Results that depend on it.** FC86 — holds on all models tried; FC87 — holds on all models tried; FC88 — holds on all models tried; FC90 — not tested.
### I58 · 'Losses outside P': the aims considered, and 'exposed'

**The sentence it fills in for.**

> L441 | Losses outside \(P\) must be exposed.

**What was invented.** A repair claim carries a declared set Aims* ⊇ O ∪ P of aims under consideration and an exposure record X; the claim is well formed when {r ∈ Aims* \ P : r(ξ) ∧ ¬r(ξ')} ⊆ X. Aims* is a declared input that L522 does not list.

**Other choices that were possible.**

- all aims the system holds, read through the physical module
- exposure as a statement in the record, not a set

**Used by.** Formal core §0, §14. Claims: FC88, FC98.

**Results that depend on it.** FC88 — holds on all models tried; FC98 — not tested.
### I59 · Explanatory aims: L443 read as a characterization of O_ex

**The sentence it fills in for.**

> L443 | **Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one.

**What was invented.** O_ex ⊆ O is a declared marking of aims; L443 is read as: o is explanatory when its condition is 's possesses a deployable account of a stated question' or is L443's 'the correction of a use through' a deployable account. (EX) imposes the same conditions on both kinds.

**Other choices that were possible.**

- L443 as a necessary condition only
- O_ex defined by (EX)'s own conditions

**Used by.** Formal core §0, §14. Claims: FC89, FC90, FC98.

**Results that depend on it.** FC89 — not tested; FC90 — not tested; FC98 — not tested.
### I60 · ProducesVia: 'the relevant binding of c'

**The sentence it fills in for.**

> L453 | \(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\).

**What was invented.** The relevant binding of c is the binding named in c's construction trace (Build's binding construction); 'contains' means some occurrence of the route instantiates it.

**Other choices that were possible.**

- any occurrence that carries c

**Used by.** Formal core §14. Claims: FC89, FC90.

**Results that depend on it.** FC89 — not tested; FC90 — not tested.
### I61 · Tasks and executions; 'complete' in F read as (CT1)'s completion

**The sentence it fills in for.**

> L461 | a task a specified input-to-output attribute transformation with explicit resources and side effects.

> L469 | Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task.

> L471 | \(F(C)\) = states whose executions all complete and return into \(C\).

**What was invented.** A task T is a relation between inputs and outputs, with dom T and T[i]. Exec(π,z,i;χ) is a set of executions, each with a completion flag, an output o and a final constructor state z'. F(X) := {z : for every i in dom T and every η in Exec(π,z,i;χ), η completes with o in T[i] and z' in X}: 'complete' is read as (CT1)'s 'completes with o ∈ T[i]'. Nonemptiness of Exec (L469) is a standing assumption for z in C and i in dom T, not part of F.

**Other choices that were possible.**

- 'complete' without the output condition (then C ⊆ F(C) is weaker than (CT1))
- nonemptiness inside F (F(X) then leaves out states with no executions)

**Used by.** Formal core §15. Claims: FC91, FC92, FC109.

**Results that depend on it.** FC91 — holds on all models tried; FC92 — holds on all models tried; FC109 — holds on all models tried.
### I62 · Tolerances: stricter tolerances admit fewer tasks; Admit contains every realized task

**The sentence it fills in for.**

> L479 | form a directed preorder \(Q_\Theta\), in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes, and none of them is exact;

> L479 | \(\mathsf{Admit}^{q,r}_\Theta\) is the set of tasks physically achievable at tolerances \((q,r)\);

**What was invented.** q precedes q' when q' excludes at least what q excludes (q' is at least as strict). Admit^{q,r} is antitone in (q,r). A task with a realization, owned or not, at (q,r) is in Admit^{q,r} (so (CT3) follows from the definitions).

**Other choices that were possible.**

- Admit given by the physical module with no stated link to realizations (then (CT3) is an assumption)

**Used by.** Formal core §15. Claims: FC93.

**Results that depend on it.** FC93 — holds on all models tried.
### I63 · A tag such as (I2) names the sentence before it

**The sentence it fills in for.**

> L329 | The feature is identified at \(y\) exactly when \(Z_y\neq\varnothing\land|f[Z_y]|=1\). (I1)

> L335 | no allowed path joins states of different invariant value. (O1)

> L471 | the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

**What was invented.** Each parenthesized tag names the sentence it follows, as it can only do at L395 and L471 (nothing follows the tag there). So (I1) is the definition of identification at y, (I2) the factorization claim, (I3) the kernel criterion, and (O1) the invariance claim.

**Other choices that were possible.**

- a tag names the sentence after it (then (I2) is the kernel criterion and (O1) is 'Equal values do not suffice for reachability')

**Used by.** Formal core §17. Claims: FC57, FC58, FC61, FC109.

**Results that depend on it.** FC57 — holds on all models tried; FC58 — holds on all models tried; FC61 — holds on all models tried; FC109 — holds on all models tried.
### I64 · Identification: 'attainable', and the admitted states in the linear case

**The sentence it fills in for.**

> L329 | It is identified on every attainable \(y\) exactly when \(f=\bar f\circ g\) for some \(\bar f\).

> L329 | For linear \(g\) and linear feature \(c^\top\), identification is \(\ker g\subseteq\ker c^\top\).

**What was invented.** y is attainable when y ∈ g[Z]. In the linear case Z is the whole space ℝ^n and 'identification' is identification at every attainable y.

**Other choices that were possible.**

- Z a proper subset (a cone or box of admitted states; then the kernel criterion can fail)
- identification at one given y

**Used by.** Formal core §17. Claims: FC57, FC58, FC59, FC109.

**Results that depend on it.** FC57 — holds on all models tried; FC58 — holds on all models tried; FC59 — holds on all models tried; FC109 — holds on all models tried.
### I65 · The pole and its shadow, encoded

**The sentence it fills in for.**

> L325 | Stipulate \(H:=U_H,\ \theta:=U_\theta,\ L:=H\cot\theta\)

> L325 | It is faithful under the identification contract, whose edits alter the observed \(L\).

**What was invented.** Ports H, θ, L; the exogenous values u_H, u_θ carried by the boundary b = (u_H, u_θ); components c_H (footprint {H}, relation H = u_H), c_θ (θ = u_θ), c_L (footprint {H, θ, L}, relation L = H cot θ); edits: set H to h, set θ to φ, set L to l, each replacing its component (I04), and their composites. For tests, finite grids (H in {1,2,3}, θ in {30°,45°,60°}). The production question: Q reads L. The identification contract: boundaries varying u_H so that different values of L are observed, and Q returning the fibre {H : H cot θ = observed L}; 'edits that alter the observed L' are read as these boundary changes.

**Other choices that were possible.**

- u_H and u_θ as ports
- the identification contract with edits to a measuring component that reads L
- real values handled symbolically

**Used by.** Formal core §17. Claims: FC02, FC07, FC26, FC27, FC28, FC99.

**Results that depend on it.** FC02 — holds on all models tried; FC07 — holds on all models tried; FC26 — holds on all models tried; FC27 — holds on all models tried; FC28 — holds on all models tried; FC99 — holds on all models tried.
### I66 · The odd-order skew-symmetric case, encoded

**The sentence it fills in for.**

> L343 | Contract: remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed.

**What was invented.** Ports: the order n, the matrix entries, det, inv; components: skew (Mᵀ = −M), odd (n odd), determinant (Leibniz sum), invertibility (inv ⟺ det ≠ 0); edits: delete skew, delete odd, delete both; Q: 'does the family contain an invertible matrix?'. For tests: n in {1,2,3}, entries in GF(p) for an odd prime p (the statement also holds there, since 2 is invertible) or small integer ranges with exact determinants. The Leibniz candidate: one component per permutation term and a sum component.

**Other choices that were possible.**

- real entries handled symbolically
- entries in GF(2), where the statement fails (a different field arithmetic, which the contract holds fixed)

**Used by.** Formal core §17. Claims: FC63.

**Results that depend on it.** FC63 — counterexample ((c-i) the Leibniz candidate, sum over every tuple of term values).
### I67 · A contract as an organization (Argument 5), encoded

**The sentence it fills in for.**

> L590 | Give it ports (the edits and their boundaries), components (the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits (add or remove a change; alter \(\mathcal Q\)).

**What was invented.** One port m_(a,b) with domain {0,1} for each (a,b) in A × B (membership in C) and one port q whose domain is a declared set of queries; components: the baseline condition (m_(1,b0) = 1) and whatever closure conditions the question declares (for example m_(a1,b) ∧ m_(a2,b) → m_(a2·a1,b)); edits: set a membership port, set q, and composites.

**Other choices that were possible.**

- ports for edits only, boundaries fixed
- no closure conditions beyond the baseline (the text names 'the closure conditions' without saying which)

**Used by.** Formal core §17. Claims: FC97.

**Results that depend on it.** FC97 — holds on all models tried.
### I68 · Argument 10's two-layer episode, encoded; 'recent occupancy'

**The sentence it fills in for.**

> L620 | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell, swap the two identities.

> L622 | \(S_0\) predicts occupancy from recent occupancy.

**What was invented.** A line of N cells (N = 6 for tests), two things with position in {0..N−1} and velocity in {−1,0,1}, time steps 0..K; continuity: pos(t+1) = pos(t) + vel(t), with a stated rule at the ends (reflection); occluding cell c makes the occupancy reading of c empty; swap exchanges the two things' positions and velocities. S0 predicts occupancy at t+1 from the occupancy of the last w steps, with the window w shorter than the occlusion.

**Other choices that were possible.**

- continuous positions
- an unbounded window (then an occupancy predictor could extrapolate through an occlusion, and the 'structural' failure can fail: FC102)
- stopping at the ends instead of reflecting

**Used by.** Formal core §17. Claims: FC90, FC102, FC103.

**Results that depend on it.** FC90 — not tested; FC102 — counterexample ((b) second half: a window longer than the occlusion); FC103 — holds on all models tried.
### I69 · 'Built alike': the exchange is an automorphism

**The sentence it fills in for.**

> L630 | The two things are built alike in \(P\), and their persistence components alike in \(S_1\)

**What was invented.** The exchange ψ of the two things is a bijection of P's ports, components, edits and boundaries that preserves L, maps C onto C and leaves the query's answers unchanged; the same holds in S1 for the exchange of the persistence components.

**Other choices that were possible.**

- an isomorphism between the two things' subnetworks only

**Used by.** Formal core §17. Claims: FC103.

**Results that depend on it.** FC103 — holds on all models tried.
### I70 · A structure-preserving bijection of all the data (Argument 8)

**The sentence it fills in for.**

> L612 | Transporting all carriers, relations, transports, histories, contracts and declared inputs along structure-preserving bijections preserves (E), (G), (P), (EX).

**What was invented.** Bijections of ports, values, components, edits (a partial-monoid isomorphism), boundaries and occurrences (preserving ≺_h and the physical module's interpretation), with the query, its designation and every declared input carried along (Q^φ(φ·O, φa, φb) = Q(O,a,b)).

**Other choices that were possible.**

- the physical module not transported (then (G) and (EX) need it to commute with the bijection)

**Used by.** Formal core §18. Claims: FC33, FC45, FC67, FC100.

**Results that depend on it.** FC13 — holds on all models tried; FC33 — holds on all models tried; FC45 — holds on all models tried; FC67 — holds on all models tried; FC100 — holds on all models tried.
### I71 · The 'value' of a transport at a pair (Argument 3)

**The sentence it fills in for.**

> L572 | at which some \(t'\in\mathcal T\), also surviving on \(H\), has a different value from \(t\)

**What was invented.** value_t(a,b) := (τ(a), σ(b), (L^E_k(τ(a),σ(b)))_{k in J_E}): the translated pair and the relations the transport's organization has there. Members of 𝒯 share the codomain's ports and components and differ in relations; Argument 3's 'L_j(a,b) altered' is read as L^E_j(τ(a),σ(b)) altered.

**Other choices that were possible.**

- the prediction Ans_E(τ(a),σ(b)) only
- the π-image of Sol_D(a,b)

**Used by.** Formal core §12. Claims: FC80, FC109.

**Results that depend on it.** FC80 — holds on all models tried; FC109 — holds on all models tried.
### I72 · Respects as sufficient conditions; 'upstream'

**The sentence it fills in for.**

> L151 | A production question has a \(\mathcal Q\) that reads an output port and a \(C\) containing interventions on upstream ports.

**What was invented.** The three sentences are sufficient conditions naming a respect, not definitions: production when Q reads an output port w and C contains a setting edit of a port upstream of w (v upstream of w: a chain of components, each reading the output of the one before, from v to w); identification when Q computes a fibre g^-1(y) and C contains edits to the observed value; obstruction when Y_p = {reachable, unreachable}. The respects need not exclude one another.

**Other choices that were possible.**

- necessary conditions (every production question has such Q and C)
- a function from (type of Q, shape of C) to one respect

**Used by.** Formal core §3. Claims: FC36.

**Results that depend on it.** FC36 — holds on all models tried.
### I73 · 'An answer to one is not an answer to the other': the narrow reading

**The sentence it fills in for.**

> L151 | Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other.

**What was invented.** Narrow reading: meeting (E) on one does not by itself give (E) on the other. The wide reading (no candidate meets (E) on both) is carried as a claim to test (FC34).

**Other choices that were possible.**

- the wide reading
- 'answer' as the answer profile Ans_p (different profiles)

**Used by.** Formal core §3. Claims: FC34.

**Results that depend on it.** FC34 — holds on all models tried.
### I74 · Recursive capacity: target chains and enabling continuations

**The sentence it fills in for.**

> L492 | \forall n<\omega\ \forall\text{ admitted target chains of length }n,\ \exists\text{ an owned enabling continuation}.

**What was invented.** A target chain of length n is a sequence d1, …, dn of aspects of the system's practice, each d(i+1) a description of di made a represented target, each step admitted by the physical module; an owned enabling continuation is an owned continuation in which dn becomes a represented target, criticism is directed at it and the result can change its operative use (L487).

**Other choices that were possible.**

- chains of scrutiny of one aspect repeated n times

**Used by.** Formal core §16. Claims: FC94, FC110.

**Results that depend on it.** FC94 — not tested; FC110 — not tested.
### I75 · The explanatory contents 𝔈_Θ

**The sentence it fills in for.**

> L497 | With \(\mathfrak E_\Theta\) the explanatory contents that some carrier can hold under the physical module

**What was invented.** 𝔈_Θ := {c : for some p, t, Γ, Account((c,p,t,Γ)), and the physical module admits some carrier instantiating c}. It is taken to be infinite where FC94 needs it.

**Other choices that were possible.**

- contents that some carrier holds at present

**Used by.** Formal core §16. Claims: FC94, FC110.

**Results that depend on it.** FC94 — not tested; FC110 — not tested.
### I76 · The three defects of a question, formally

**The sentence it fills in for.**

> L161 | A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.

**What was invented.** A question is taken with a description Desc it answers to. 'Fails to pick out its alleged target': no organization satisfies Desc, or several do. 'Incompatible baseline': Sol_D(1,b0) = ∅, or b0 ∉ B. 'Incompatible requirements': the conditions Desc places on (C, Q) have no joint instance.

**Other choices that were possible.**

- the question as the tuple p alone (then the first defect cannot be written, since D is given in p)

**Used by.** Formal core §3, §9. Claims: FC106, FC107.

**Results that depend on it.** FC106 — holds on all models tried; FC107 — not tested.

## Inventions forced by the program (I77–I102)

These choices were made by the program `model/` that searched the formal claims on finite models (S104 round 2). None is marked in `formal core.md`, which the program does not change; each is tagged in the code, at the place named under 'Used by'. As with I01–I76, nothing here is the text's own content.

### I77 · Finite models and the bounds of the search

**The sentence it fills in for.**

> L91 | \(V\) is a set of ports, each with a nonempty value domain \(X_v\).

> L105 | Values of ports may be paths, functions, fields, mathematical structures or histories.

**What was invented.** Every port has a finite domain; the searched organizations have at most 3 ports (domains of at most 2 or 3 values), at most 3 or 4 components, at most 2 boundaries and at most 2 generator edits (so at most about 12 edits after closure); relations are explicit finite sets of tuples; the hypothetical relations R of D8.1 are enumerated in full, so conflict is decided only on targets with at most 4096 assignments (footprints of at most 2 two-valued ports). Sizes are tried in ascending order, so the first counterexample found is the smallest found. A result 'holds on all models tried' says nothing beyond these bounds.

**Other choices that were possible.**

- symbolic (infinite) domains, with claims decided by derivation rather than by search
- larger bounds (more ports, values, components, edits), at more cost
- a different ordering of sizes (the 'smallest' counterexample is smallest in this ordering only)

**Used by.** Code: model/gen.py (Size, sizes); model/core.py (all_R); model/claims_a.py, model/claims_b.py (the sizes of each search). Claims: FC01, FC02, FC03, FC04, FC05, FC06, FC08, FC10, FC12, FC13, FC15, FC16, FC17, FC18, FC19, FC20, FC21, FC22, FC23, FC24, FC25, FC29, FC33, FC34, FC37, FC41, FC43, FC44, FC45, FC46, FC47, FC48, FC49, FC50, FC51, FC52, FC54, FC57, FC58, FC61, FC64, FC65, FC66, FC67, FC68, FC74, FC77, FC80, FC85, FC96, FC100, FC106.

**Results that depend on it.** FC01 — holds on all models tried; FC02 — holds on all models tried; FC03 — holds on all models tried; FC04 — holds on all models tried; FC05 — counterexample ((ii) reading (ii): any bijection); FC06 — holds on all models tried; FC08 — holds on all models tried; FC10 — holds on all models tried; FC12 — holds on all models tried; FC13 — holds on all models tried; FC15 — holds on all models tried; FC16 — holds on all models tried; FC17 — holds on all models tried; FC18 — counterexample (untranslated reading (I94)); FC19 — holds on all models tried; FC20 — counterexample (any value map κ); FC21 — holds on all models tried; FC22 — holds on all models tried; FC23 — counterexample ((b) as stated); FC24 — holds on all models tried; FC25 — counterexample ((b) with a port of D in no footprint); FC29 — holds on all models tried; FC33 — holds on all models tried; FC34 — holds on all models tried; FC37 — holds on all models tried; FC41 — holds on all models tried; FC43 — holds on all models tried; FC44 — holds on all models tried; FC45 — holds on all models tried; FC46 — holds on all models tried; FC47 — holds on all models tried; FC48 — holds on all models tried; FC49 — holds on all models tried; FC50 — holds on all models tried; FC51 — holds on all models tried; FC52 — holds on all models tried; FC54 — holds on all models tried; FC57 — holds on all models tried; FC58 — holds on all models tried; FC61 — holds on all models tried; FC64 — holds on all models tried; FC65 — holds on all models tried; FC66 — holds on all models tried; FC67 — holds on all models tried; FC68 — holds on all models tried; FC74 — holds on all models tried; FC77 — counterexample (with H = ∅ and an empty selection history); FC80 — holds on all models tried; FC85 — holds on all models tried; FC96 — holds on all models tried; FC100 — holds on all models tried; FC106 — holds on all models tried.

### I78 · Two families of generated organizations: surgical edits with override, and free edits

**The sentence it fills in for.**

> L91 | \(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\).

> L574 | The component relations \(L_j(a,b)\) are supplied independently for each \((a,b)\).

**What was invented.** G-surg: each port has a home component (footprint: the port and up to two others); edits are the closure under override of up to two generators, each the setting of a port to a value or an alternative relation of a component; composition is override (a total monoid), and L at an edit is the surgery applied (the home component of a set port gets the slice v = x, an altered component its alternative relation). This is an action law, I02's alternative, so on G-surg a composite's relations follow from its parts'. G-free: abstract edits 1, e1, e2 whose only defined composites are those with 1; relations drawn independently for every (j, a, b), as I02 has it. Every random search draws from one or both families and says which.

**Other choices that were possible.**

- one family only (either restricts the space: G-surg to action laws, G-free to edits that never compose)
- edits with partial, non-trivial composition tables drawn at random (then Kleene associativity, I01, is needed as a further condition)
- setting edits that add a constraint beside the old one (L103 excludes them)

**Used by.** Code: model/gen.py (gen_surg, gen_free). Claims: FC01, FC02, FC03, FC04, FC05, FC06, FC08, FC09, FC10, FC12, FC13, FC15, FC16, FC17, FC18, FC19, FC20, FC21, FC22, FC23, FC24, FC25, FC29, FC33, FC34, FC37, FC43, FC44, FC45, FC46, FC47, FC48, FC49, FC50, FC51, FC52, FC54, FC62, FC67, FC68, FC74, FC77, FC80, FC85, FC96, FC100, FC101, FC106.

**Results that depend on it.** FC01 — holds on all models tried; FC02 — holds on all models tried; FC03 — holds on all models tried; FC04 — holds on all models tried; FC05 — counterexample ((ii) reading (ii): any bijection); FC06 — holds on all models tried; FC08 — holds on all models tried; FC09 — holds on all models tried; FC10 — holds on all models tried; FC12 — holds on all models tried; FC13 — holds on all models tried; FC15 — holds on all models tried; FC16 — holds on all models tried; FC17 — holds on all models tried; FC18 — counterexample (untranslated reading (I94)); FC19 — holds on all models tried; FC20 — counterexample (any value map κ); FC21 — holds on all models tried; FC22 — holds on all models tried; FC23 — counterexample ((b) as stated); FC24 — holds on all models tried; FC25 — counterexample ((b) with a port of D in no footprint); FC29 — holds on all models tried; FC33 — holds on all models tried; FC34 — holds on all models tried; FC37 — holds on all models tried; FC43 — holds on all models tried; FC44 — holds on all models tried; FC45 — holds on all models tried; FC46 — holds on all models tried; FC47 — holds on all models tried; FC48 — holds on all models tried; FC49 — holds on all models tried; FC50 — holds on all models tried; FC51 — holds on all models tried; FC52 — holds on all models tried; FC54 — holds on all models tried; FC62 — holds on all models tried; FC67 — holds on all models tried; FC68 — holds on all models tried; FC74 — holds on all models tried; FC77 — counterexample (with H = ∅ and an empty selection history); FC80 — holds on all models tried; FC85 — holds on all models tried; FC96 — holds on all models tried; FC100 — holds on all models tried; FC101 — holds on all models tried; FC106 — holds on all models tried.

### I79 · Boundary inputs and exogenous values are carried by components

**The sentence it fills in for.**

> L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component

> L325 | where \(U_H\) and \(U_\theta\) are exogenous values setting the pole's height \(H\) and the sun's elevation \(\theta\)

**What was invented.** A boundary b is a label; what it fixes enters through the relations L_j(a, b) of components (in the pole, c_H: H = u_H and c_θ: θ = u_θ). There are no separate boundary coordinates, so NC1's 'unanalysed boundary input' is checked by the same answer-slot test as a component.

**Other choices that were possible.**

- boundaries as valuations of designated boundary ports, with NC1 checking each boundary coordinate separately (D6.3's second clause)
- u_H and u_θ as ports (one of I65's other choices)

**Used by.** Code: model/core.py (slot, NC1); model/cases.py (pole). Claims: FC23, FC24, FC26, FC34, FC62.

**Results that depend on it.** FC23 — counterexample ((b) as stated); FC24 — holds on all models tried; FC26 — holds on all models tried; FC34 — holds on all models tried; FC62 — holds on all models tried.

### I80 · The identity edit can be a setting edit

**The sentence it fills in for.**

> L109 | A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly.

**What was invented.** D2.1 is applied as written, to every edit of A including 1: where some component's relation at (1, b) is already a slice v = x at every b (as c_H: H = u_H is in the pole), the identity edit sets v through that component, so v is an input even when A holds no other edit. The program reports this and keeps it; Roles(exclude_identity=True) gives the other reading.

**Other choices that were possible.**

- exclude 1 from Set_v: an input needs an edit other than the identity
- require a setting edit to change the component it sets through

**Used by.** Code: model/core.py (Roles, sets_through). Claims: FC02, FC06, FC07, FC11, FC12, FC25.

**Results that depend on it.** FC02 — holds on all models tried; FC06 — holds on all models tried; FC07 — holds on all models tried; FC11 — holds on all models tried; FC12 — holds on all models tried; FC25 — counterexample in a part that does not use it; its other parts hold on all models tried.

### I81 · Transports as port translations; derived ports; generated candidates; the transport space searched for ≡

**The sentence it fills in for.**

> L189 | \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation.

> L343 | every intermediate product is a determinant suborganization whose hidden ports project away

> L413 | Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\)

**What was invented.** π is induced by port translations: each port of E reads a tuple of D's ports through a value map (I14's case is one port and a map κ; several ports, a 'derived port', are used only for the term ports of the Leibniz candidate, FC63); π is then total. τ and σ are finite maps. Generated candidates: E's ports a subset of D's (optionally recoded by value maps), its components the projections of groups of D's components at each pair (an encoding candidate, I32's E_enc), τ and σ the identity or random, with background components and one perturbed relation at random; also random organizations with random τ, σ, λ (λ(k) chosen to cover k's footprint), and lookups (FC23). For ≡ (FC85) the transports searched are π and λ the identity on shared names with τ and σ every map, so 'no transport exists' is shown only over that space.

**Other choices that were possible.**

- π an arbitrary partial map X_D ⇀ X_E (I16), searched directly
- port translations as maps from V_N to V_k (several D ports to one E port without a function)
- the whole transport space for ≡ (feasible only for the smallest organizations)

**Used by.** Code: model/core.py (Translation, Candidate, proj_lam); model/gen.py (gen_candidate, gen_random_candidate, gen_lookup); model/claims_b.py (FC63, FC85). Claims: FC15, FC16, FC17, FC18, FC19, FC20, FC21, FC22, FC23, FC24, FC29, FC33, FC34, FC37, FC43, FC44, FC45, FC46, FC47, FC48, FC49, FC50, FC51, FC52, FC54, FC63, FC67, FC68, FC74, FC77, FC80, FC85, FC96, FC100, FC106.

**Results that depend on it.** FC15 — holds on all models tried; FC16 — holds on all models tried; FC17 — holds on all models tried; FC18 — counterexample (untranslated reading (I94)); FC19 — holds on all models tried; FC20 — counterexample (any value map κ); FC21 — holds on all models tried; FC22 — holds on all models tried; FC23 — counterexample ((b) as stated); FC24 — holds on all models tried; FC29 — holds on all models tried; FC33 — holds on all models tried; FC34 — holds on all models tried; FC37 — holds on all models tried; FC43 — holds on all models tried; FC44 — holds on all models tried; FC45 — holds on all models tried; FC46 — holds on all models tried; FC47 — holds on all models tried; FC48 — holds on all models tried; FC49 — holds on all models tried; FC50 — holds on all models tried; FC51 — holds on all models tried; FC52 — holds on all models tried; FC54 — holds on all models tried; FC63 — counterexample ((c-i) the Leibniz candidate, sum over every tuple of term values); FC67 — holds on all models tried; FC68 — holds on all models tried; FC74 — holds on all models tried; FC77 — counterexample (with H = ∅ and an empty selection history); FC80 — holds on all models tried; FC85 — holds on all models tried; FC96 — holds on all models tried; FC100 — holds on all models tried; FC106 — holds on all models tried.

### I82 · Queries in the program; NC1 only for a query that reads a port

**The sentence it fills in for.**

> L141 | \(\mathcal Q\) is a specified set-theoretic operation on \(D\), its solutions and its component structure, with codomain \(Y_p\).

**What was invented.** Random searches use the port-reading query Q_w with the designation δ_E of E's copy of the port (I20's default); the worked cases use queries written as functions of Sol (the fibre query of the pole, the 'contains an invertible matrix' query of E6). NC1's answer slot is defined for a port-reading query only; for any other query no component is a slot.

**Other choices that were possible.**

- answer slots for every query (a component whose relation fixes the query's value directly), which needs a notion of 'fixing a query value' the text does not give

**Used by.** Code: model/core.py (PortQuery, FnQuery, slot); model/cases.py (fibre_query); model/claims_b.py (FC63). Claims: FC23, FC63.

**Results that depend on it.** FC23 — counterexample ((b) as stated); FC63 — counterexample ((c-i) the Leibniz candidate, sum over every tuple of term values).

### I83 · An answer slot needs a determined target answer at every pair

**The sentence it fills in for.**

> L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component

**What was invented.** Where Ans_p(a, b) = ⊥ at some pair of C, no component is an answer slot on C (there is no answer to appear); the lookup candidate's relation at such a pair is the full relation.

**Other choices that were possible.**

- a slot at a ⊥ pair is the full relation (or the empty one), so a lookup can still be a slot
- the slot condition asked only at the pairs where Ans_p is determined

**Used by.** Code: model/core.py (slot); model/gen.py (gen_lookup). Claims: FC23, FC24.

**Results that depend on it.** FC23 — counterexample ((b) as stated); FC24 — holds on all models tried.

### I84 · The homomorphism clause when a composite lies outside τ's domain

**The sentence it fills in for.**

> L242 | \pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b)),\qquad \tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1). \tag{F2}

**What was invented.** Where a2·a1 is defined in D and not in dom τ, the clause fails (τ(a2·a1) has no value to equal τ(a2)·τ(a1)).

**Other choices that were possible.**

- the clause asks nothing of such a pair
- Kleene equality: both sides undefined counts as equal

**Used by.** Code: model/core.py (hom). Claims: none.

**Results that depend on it.** none: no test used it.

### I85 · The default scope statement states every excluded pair

**The sentence it fills in for.**

> L257 | every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently.

**What was invented.** Unless a test varies it, each question's scope statement names every pair of A × B outside C, so the scope clause of non-vacuity holds, and a narrowed or widened question gets a statement of its own.

**Other choices that were possible.**

- a scope statement drawn at random (then non-vacuity fails for reasons unrelated to the claim tested)
- one statement for all questions on one target

**Used by.** Code: model/core.py (Question). Claims: FC21, FC26, FC34, FC46, FC51.

**Results that depend on it.** FC21 — holds on all models tried; FC26 — holds on all models tried; FC34 — holds on all models tried; FC46 — holds on all models tried; FC51 — holds on all models tried.

### I86 · Every pair of candidates examined counts as offered one in place of the other

**The sentence it fills in for.**

> L315 | Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other

**What was invented.** The primitive Offered (I33) is taken to hold, both ways, of every pair of candidates a test examines; rivals are then the pairs that conflict somewhere both translate.

**Other choices that were possible.**

- Offered drawn at random (it would test nothing about conflict)
- Offered held of no pair (then there are no rivals)

**Used by.** Code: model/core.py (rivals); model/claims_b.py (FC43, FC49, FC50). Claims: FC43, FC49, FC50.

**Results that depend on it.** FC43 — holds on all models tried; FC49 — holds on all models tried; FC50 — holds on all models tried.

### I87 · Claims as propositional formulas, read structurally

**The sentence it fills in for.**

> L397 | it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below).

> L397 | read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone

**What was invented.** Claims are propositional formulas (atoms, ¬, ∧, →), a restriction of I38's first-order language; 'inconsistent with' is truth-table inconsistency; 'among its premises, read structurally' is: after removing double negations and flattening and sorting conjunctions, ¬φ is a conjunct of a leaf; the denial of ψ is ¬ψ with a double negation removed. Facts about the models (that a candidate meets a condition at a pair, that χ speaks of the target) enter the arguments as atoms and conditionals.

**Other choices that were possible.**

- first-order claims (I38) with a structural reading up to renaming of bound variables
- the denial of ψ read without removing double negations (then 'made from ¬χ' does not block χ)

**Used by.** Code: model/args.py (canon, conjuncts, denial, incons, rules_out). Claims: FC47, FC53, FC56, FC60, FC68, FC69, FC70, FC71, FC72, FC73.

**Results that depend on it.** FC47 — holds on all models tried; FC53 — holds on all models tried; FC56 — holds on all models tried; FC60 — holds on all models tried; FC68 — holds on all models tried; FC69 — holds on all models tried; FC70 — holds on all models tried; FC71 — holds on all models tried; FC72 — holds on all models tried; FC73 — holds on all models tried.

### I88 · X_j ranges over a finite set of arguments; an argument has a step

**The sentence it fills in for.**

> L397 | An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions.

**What was invented.** X_j(ψ) is computed over a finite set of arguments: those a test builds, or every tree of height at most 2 or 3 over the given premises with the admitted forms. An argument with no step (a bare leaf) is no argument. So 'no argument rules it out' is shown only over that set.

**Other choices that were possible.**

- every argument over the premises (infinite; decidable only by a search over derivations)
- a bare premise counts as an argument

**Used by.** Code: model/args.py (X, enumerate_args, usable). Claims: FC47, FC53, FC56, FC71.

**Results that depend on it.** FC47 — holds on all models tried; FC53 — holds on all models tried; FC56 — holds on all models tried; FC71 — holds on all models tried.

### I89 · The inference forms: MP, MT, AND-introduction, AND-elimination and a free form

**The sentence it fills in for.**

> L387 | For argument step \(u\) with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:

> L393 | \(\operatorname{Form}_j(u)\): the inference form of \(u\) is one \(j\) admits.

**What was invented.** Five forms: modus ponens, modus tollens, ∧-introduction, ∧-elimination, and a 'free' form (any premises, any conclusion; an admitted form need not be sound, I38). A step counts only where it instantiates its form; every premise of a step is essential.

**Other choices that were possible.**

- forms declared by each assessor as arbitrary relations between premise sets and conclusions
- essential premises a proper subset of a step's children

**Used by.** Code: model/args.py (form_ok, Step). Claims: FC47, FC53, FC56, FC60, FC68, FC69, FC70, FC71, FC72, FC73.

**Results that depend on it.** FC47 — holds on all models tried; FC53 — holds on all models tried; FC56 — holds on all models tried; FC60 — holds on all models tried; FC68 — holds on all models tried; FC69 — holds on all models tried; FC70 — holds on all models tried; FC71 — holds on all models tried; FC72 — holds on all models tried; FC73 — holds on all models tried.

### I90 · The physical module supplied by hand: histories and provenance as free predicates

**The sentence it fills in for.**

> L31 | the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain

> L195 | No member of the history represents \(t\), \(H\), or the survival condition.

> L197 | There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target.

> L405 | prepares a represented organization for explanatory use of \(c\)

**What was invented.** Where the formal core reads something through Θ (which occurrences represent what, which pairs occur, whether the physics admits a population, Prepares, BindingConstruction, TransferComposite, Attempt, Integrated), the program sets it by hand as a finite relation. 'The organization it carries to is a represented target' is an occurrence representing t's codomain. Transports and their fidelity are computed; the rest is stipulated. A model built so shows what the definitions allow, not what any physics does.

**Other choices that were possible.**

- a toy physics from which these relations are computed (e.g. occurrences as small organizations with Rep computed by (R)), which meets the build → prov → rep loop of FC98
- leaving every claim that needs Θ untested

**Used by.** Code: model/claims_b.py (Hist, sel, con; FC76-FC83, FC95); model/phys.py. Claims: FC53, FC76, FC77, FC78, FC81, FC82, FC83, FC95.

**Results that depend on it.** FC53 — holds on all models tried; FC76 — holds on all models tried; FC77 — counterexample (with H = ∅ and an empty selection history); FC78 — counterexample (exactly one provenance under I53); FC81 — counterexample ((d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 — counterexample (no common result); FC83 — counterexample (only construction is originative); FC95 — holds on all models tried.

### I91 · The infinitary routes on eventually periodic index sets

**The sentence it fills in for.**

> L311 | \(\Gamma=\{d_n:n\in\mathbb N\}\), \(d_n\) the constraint \(|x|\le 1/n\): every set of indices unbounded in \(\mathbb N\) determines \(x=0\)

**What was invented.** Sets of commitments are represented by eventually periodic subsets of ℕ, F ∪ {n ≥ N : n mod m ∈ R}; unbounded exactly when R is nonempty. The clauses of FC40 are tested on these sets only.

**Other choices that were possible.**

- arbitrary subsets of ℕ (not finitely representable)
- a finite truncation of Γ (which changes the claim: every finite family has minimal routes)

**Used by.** Code: model/claims_b.py (EP, FC40). Claims: FC40.

**Results that depend on it.** FC40 — holds on all models tried.

### I92 · The pole in exact arithmetic, with its grids, baseline, contracts and fibre query

**The sentence it fills in for.**

> L325 | Stipulate \(H:=U_H,\ \theta:=U_\theta,\ L:=H\cot\theta\)

> L325 | It is faithful under the identification contract, whose edits alter the observed

**What was invented.** Values of L are exact numbers r + s√3 (cot 30° = √3, cot 45° = 1, cot 60° = √3/3); X_L is the set of values H cot θ on the grid H ∈ {1,2,3}, θ ∈ {30°,45°,60°}; boundaries are the nine pairs (u_H, u_θ); b0 = (1, 45°); C1 holds the single settings of H and θ at b0, C2 adds the single settings of L, C2* adds the composites that set L with H or θ. The fibre query returns {H ∈ X_H : H cot θ = L} for the single value of (θ, L) in Sol, ⊥ when that value is not single. E_rev's components are c'_L (L = u_H cot u_θ, from the boundary), c'_θ and c'_H (H = L tan θ), with λ as in model/cases.py.

**Other choices that were possible.**

- real values handled symbolically
- C1 over every boundary rather than b0 only
- the fibre query read as every H when L is set (the Look of FC28)

**Used by.** Code: model/cases.py (Q3, pole, pole_rev, fibre_query); model/claims_a.py (FC07, FC26-FC28); model/claims_b.py (FC78-FC83, FC95, FC99). Claims: FC02, FC07, FC11, FC26, FC27, FC28, FC78, FC81, FC82, FC83, FC95, FC99.

**Results that depend on it.** FC02 — holds on all models tried; FC07 — holds on all models tried; FC11 — holds on all models tried; FC26 — holds on all models tried; FC27 — holds on all models tried; FC28 — holds on all models tried; FC78 — counterexample (exactly one provenance under I53); FC81 — counterexample ((d) Con(t) ∧ Viol ⇒ ¬Surp (under I53)); FC82 — counterexample (no common result); FC83 — counterexample (only construction is originative); FC95 — holds on all models tried; FC99 — holds on all models tried.

### I93 · 'The two relations stay equal': under which footprint bijection

**The sentence it fills in for.**

> L119 | an edit under which the two relations stay equal does not separate the components.

**What was invented.** Two readings are tested: (i) equal under a bijection that witnesses j ~_C j'; (ii) equal under some footprint bijection. The sentence holds under (i) and fails under (ii) (FC05).

**Other choices that were possible.**

- equal as sets of tuples with the footprints identified by position

**Used by.** Code: model/claims_a.py (FC05). Claims: FC05.

**Results that depend on it.** FC05 — counterexample ((ii) reading (ii): any bijection).

### I94 · The counterpart's signature 'read on C directly … up to the port translation': untranslated

**The sentence it fills in for.**

> L119 | Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.

**What was invented.** Besides D4.4's reading (the counterpart's projection carried to V_k by λ, value maps included), the program tests an untranslated reading: the counterpart's projection on its own ports θ_k[V_k] with D's domains, compared with k's signature under a footprint bijection between equal domains (I10).

**Other choices that were possible.**

- D4.4's reading only
- 'up to the port translation' as 'up to a port bijection and a value bijection' (I10's alternative)

**Used by.** Code: model/claims_a.py (FC18). Claims: FC18.

**Results that depend on it.** FC18 — counterexample (untranslated reading (I94)).

### I95 · Toy histories for active routes

**The sentence it fills in for.**

> L375 | An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result

**What was invented.** A history is a finite directed acyclic circuit of occurrences, each with its value computed from its parents; ≺ is reachability; the instantiated connections are the edges; 'connected' is weak connectivity by edges inside R; 'setting i's port' is an intervention on i's value with every later value recomputed; the declared contrasts are a given list of value pairs.

**Other choices that were possible.**

- occurrences with time stamps and persistence made explicit (then 'at rest when the result occurred' could be written)
- connectivity along directed chains only

**Used by.** Code: model/phys.py (Circuit, act_route); model/claims_b.py (FC75, FC76). Claims: FC75, FC76.

**Results that depend on it.** FC75 — holds on all models tried; FC76 — holds on all models tried.

### I96 · Aims on discrete time

**The sentence it fills in for.**

> L441 | each as a stated condition over stated occasions

**What was invented.** Times are 0..3; a condition is a sequence of truth values; occasions are a set of times; the repair's ξ ≤ ξ'; Aims* and the exposure record (I58) are finite lists.

**Other choices that were possible.**

- continuous time with occasions as intervals

**Used by.** Code: model/phys.py (r_left, r_right, repair); model/claims_b.py (FC86, FC88). Claims: FC86, FC88.

**Results that depend on it.** FC86 — holds on all models tried; FC88 — holds on all models tried.

### I97 · Tasks and executions on finite state sets

**The sentence it fills in for.**

> L466 | \operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C. \tag{CT1}

**What was invented.** At most 4 constructor states, 2 inputs, 3 outputs; each (state, input) has one or two executions, each a triple (completes, output, final state) drawn at random; Exec is nonempty everywhere (L469's standing assumption).

**Other choices that were possible.**

- executions as infinite traces (with 'completes' a property of the trace)

**Used by.** Code: model/phys.py (F_op, ret_real, gfp); model/claims_b.py (FC91, FC92). Claims: FC91, FC92.

**Results that depend on it.** FC91 — holds on all models tried; FC92 — holds on all models tried.

### I98 · Tolerances as a 3 × 3 grid of performance and retention

**The sentence it fills in for.**

> L479 | The tolerances of the physical module (Part XIV) form a directed preorder \(Q_\Theta\)

**What was invented.** Performance and retention tolerances are each 0 < 1 < 2 (stricter is larger); Admit and the realized tasks are random antitone families of four tasks; Cap is a random subset of the realized tasks.

**Other choices that were possible.**

- a preorder that is not a product of chains
- tolerances with no exact member, approached as a limit

**Used by.** Code: model/claims_b.py (FC93). Claims: FC93.

**Results that depend on it.** FC93 — holds on all models tried.

### I99 · The odd-order skew-symmetric case in GF(3), and the Leibniz candidate's sum component

**The sentence it fills in for.**

> L343 | Contract: remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed.

> L343 | The full Leibniz expansion with skewness substituted meets (F1) and (F2)

**What was invented.** n ∈ {1,2,3}, entries in GF(3), the matrix one port; components order, skew, odd, det, inv; edits remove skew, remove oddness, both; the edits to field arithmetic and to the determinant–invertibility link are not edits of this encoding. The Leibniz candidate has one term port and term component per permutation of three (for order 2 the permutations fixing the third index, for order 1 the identity; other terms 0) and one sum component; two relations of the sum component are tested: every tuple of term values with its sum, and only the tuples some matrix gives. Order-5 and GF(5), GF(7) cases enter only the check that odd skew matrices are singular.

**Other choices that were possible.**

- real entries handled symbolically
- D given term ports of its own (then the candidate is D itself)
- a sum component whose footprint includes the matrix

**Used by.** Code: model/claims_b.py (e6_org, e6_parts, term, FC63). Claims: FC63.

**Results that depend on it.** FC63 — counterexample ((c-i) the Leibniz candidate, sum over every tuple of term values).

### I100 · The two-layer episode's object layer: cells, occlusion and windows

**The sentence it fills in for.**

> L620 | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell, swap the two identities.

> L622 | \(S_0\) predicts occupancy from recent occupancy.

**What was invented.** Six cells, velocities −1, 0, 1, reflection at the ends, ten steps; the occlusion hides the interior cells 1..4 from step 3 for L steps (a run of occluded cells, not one cell); readings are occupancy without identity (L620's sensory field); a window-w predictor is any function of the last w readings; one thing and two things are both tried.

**Other choices that were possible.**

- a single occluded cell (the Look of FC102)
- stopping at the ends
- readings that carry identity

**Used by.** Code: model/claims_b.py (FC102, FC103). Claims: FC102, FC103.

**Results that depend on it.** FC102 — counterexample ((b) second half: a window longer than the occlusion); FC103 — holds on all models tried.

### I101 · Which models count as witnesses: the proper-model filter

**The sentence it fills in for.**

> L91 | \(V\) is a set of ports, each with a nonempty value domain \(X_v\).

**What was invented.** Existence searches whose smallest witnesses would otherwise be degenerate count only proper models: every domain has two values or more, every port lies in some footprint, Sol_D(1, b) is nonempty at every boundary, and Γ is nonempty. The filter is named with each search that uses it; universal searches use no filter (a degenerate counterexample is still a counterexample).

**Other choices that were possible.**

- no filter (smallest witnesses with one-valued domains or empty relations)
- a stronger filter (e.g. every component constraining something)

**Used by.** Code: model/claims_a.py (proper_D). Claims: FC19, FC21, FC25, FC34, FC44.

**Results that depend on it.** FC19 — holds on all models tried; FC21 — holds on all models tried; FC25 — counterexample in a part that does not use it; its other parts hold on all models tried; FC34 — holds on all models tried; FC44 — holds on all models tried.

### I102 · A component assigning several ports, or a port assigned by none

**The sentence it fills in for.**

> L109 | that is, when the component assigning it has a measurement's signature (below).

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

**What was invented.** Where j assigns several ports (asg(v) = j for more than one v), 'intervention on its output port' is the union of their setting edits; where asg(m) is undefined, a pair (o, m) yields no observation edits, and m counts among the ports j does not assign (so its settings are interventions on the world for every j).

**Other choices that were possible.**

- a component assigning several ports has no causal signature
- asg(m) undefined makes every edit that leaves m's readers an observation edit

**Used by.** Code: model/core.py (Roles.outputs_of, Roles.obs, Roles.world). Claims: FC06, FC07.

**Results that depend on it.** FC06 — holds on all models tried; FC07 — holds on all models tried.
