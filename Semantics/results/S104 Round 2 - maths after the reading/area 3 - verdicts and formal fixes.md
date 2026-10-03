# S104 Round 2 - area 3 (L373-L632) - verdicts and formal fixes

*Checker 3 of 3 (Opus 5.5), decision S40: maths and code, no new prose. Text under review: `tests/103 The semantics, standing alone, after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd, not written to). Model copy: `area 3 model/` (runs: `area 3 - runs.txt`, R0 before, R1 after). Text changes: `area 3 - text changes.json`.*

Verdicts: **HM** holds against the maths; **HW** holds against the words; **INV** rests only on an invention the text leaves open (rule 6); **NO** does not hold. Counts: HW 43, HM 21, INV 37, NO 27 (128 items). Arguments weighed, not readers counted (rule 8); C-items count only for their argument (addendum, point 3). "as X" = the same verdict and fix as row X. A3-nn: new inventions (below). OQn: owner questions (below).

| id | verdict | reason | formal fix (old → new) | code change | claims run (R1, scale 4) |
|---|---|---|---|---|---|
| D6.7 | HW | L520 names 'fidelity under change' as (E)'s source; at L189/L245's narrow 'fidelity' (F1, F2) the conjunct (A) has none (I49) | maths none; text L520 formal: (E)'s five conjuncts | none | FC31 not tested (syntactic); FC32 not tested (syntactic) |
| D6.8 | HW | as D6.7 (GLM); four headings, five conjuncts is consistent (D6.8); the defect is L520's source list | as D6.7 | none | FC31 not tested (syntactic) |
| D9.1 | INV | 'inconsistent' classical or not: no claim of the text divides the readings (I38); FC73 needs no explosion (two MP steps) | none; I38 stays open | none | FC72 holds; FC73 holds |
| D9.4 | HW | 'a step of the same argument as u' leaves (K2) with two fixed points (FC69); 'argument tree' (L397) makes 'below' definable | D9.2 + Below(u) := steps of u's subtree other than u; D9.4 kept (Live through u' ∈ Below(u)); text L393 formal, settles I40 | none (args.usable_step already recurses below) | FC69 holds; FC56 holds; FC70 holds |
| D9.5 | INV | 'within the contract, grain and boundary' fixes containment for C; grain/boundary equality is I42's; no text claim turns on it | none; FC56 (a) now states the scope hypothesis explicitly | FC56 (a) with random declared contracts; (a'') grain change | FC56 holds |
| D9.6 | HW | as D9.4 | as D9.4 | none | FC69 holds |
| D9.7 | INV | as D9.1 (Mimo); GLM: leaf-level block matches L397's 'leaves are premises' | none | none | FC72 holds |
| D9.9 | HW | L395 states (K3) without the (K2) conditions its own step needs (Mimo model 1); D9.9 (ii) 'from those premises no argument rules out T' fails for unsound admitted forms (GLM; I38) | old (i) MT + live conditional; (ii) no argument rules out T,B,I → new (i) α∈X_j(O) ∧ Usable_j(u⁺) ∧ no leaf of α with ¬(T∧B∧I) as conjunct or record made from it ⇒ α⁺∈X_j(T∧B∧I), any form; (ii) ¬RO(α⁺,x), x∈{T,B,I}; (iii) Forms_j classically sound ⇒ no argument from those premises rules out x; text L395 formal, settles I43 | FC71 rewritten: (i) any form, (ii), (iii), (iv) GLM's model | FC71 holds; FC47 holds; FC53 holds; FC60 holds; FC68 holds |
| D9.10 | HM | Bearing(c,z,p) read p_δ as supplied with c, so p dropped out; L377 builds p_δ from z, δ, p | old p_δ supplied with c → new p_δ := Qf(z,δ,p) [A3-01]; ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_c), t_c, Γ_c, δ_c supplied [A3-03]; Bearing :⟺ Acc(ℰ_c); text KEEP | FC74 part 2: bearing relative to p | FC74 holds; FC76 holds |
| D9.11 | INV | the four phrases are undefined; both readers keep them open as declared data, which D9.11 already is (I47); no sentence shown to say what it should not | none (Rule, Rec, Chg stay in D0.2) | none | FC76 holds |
| D11.3 | HW | 'reflexive closure' of an acyclic, possibly intransitive ≺_h is not an order; (EX)'s e_c ⪯_h e needs chains | old ≺_h strict partial order [I44] → new ≺_h acyclic, ⪯_h := ≺_h* (settles I44 by its choice (b)); Org_ℓ(h), subhistory registered [A3-07]; text L375 formal | none (Circuit.prec is reachability) | FC75 holds; FC76 holds |
| D11.4 | HM | D11.4 drops L375's 'already at rest' (H11); its chain clause is not in the words and excludes side inputs (Mimo B); its dependence is read in the whole history, not along the route (Mimo A) | old I46 → new ActRoute_h(R;i,r,K) :⟺ i,r∈R ⊆ O_h; ∀n∈R n ⇝_R r; each n meets its relation; ∃(x,x')∈K val_r(Org_ℓ(h)∣_R[i:=x]) ≠ val_r(Org_ℓ(h)∣_R[i:=x']), outside R held at actual values [A3-06]; ¬AtRest_h(R,r) [A3-05]; text KEEP | phys.act_route rewritten (values_along, at_rest); FC75 rewritten | FC75 holds; FC76 holds |
| D12.4 | INV | the carrying rule is L211/L409's; the unit (component with its binding) is I54's; L211's 'keeps its provenance when access is lost' holds since prov is a function of history | none | none | FC78 counterexample; FC95 holds |
| D12.9 | INV | 'value' is fixed by L574's own step ('L_j(a,b) altered') up to I71's translated pair; Mimo's point on the population restriction is PARKED | none | none | FC80 holds |
| D13.1 | INV | (1) Rep_ℓ already carries Sel ∨ Con (D12.5): NO; (2) 'retained' is carried by Can's (CT1) (z' ∈ C): NO; (3) 'integrated', 'nontrivial' are I55's | none | none | FC97 holds |
| D13.3 | HM | D13.3 drops 'a represented organization' and 'for explanatory use' (Mimo); with them read through (R) the loop of E03 appears (D18.1) | old ∃h'[Owned ∧ Prepares(h',c) ∧ BindingConstruction ∧ ¬TransferComposite] → new ∃h' ending at e [Owned_β(h',s) ∧ ∃o output of h': Prepares(h',o,c) ∧ Rep^ρ_ℓ(o,c) ∧ ExplUse(o,c) ∧ BindingConstruction(h',c) ∧ ¬TransferComposite(h')], ρ ∈ {K,T} the owner's (OQ1, A3-02) [A3-04] | FC98 (c), (d) | FC98 holds; FC83 counterexample; FC84 holds |
| D13.4 | NO | L413 already says the relation is read 'with c and its contract fixed' and (N) uses it so; the sign is notation | none | none | FC85 holds |
| D13.6 | HM | Attempt is a primitive the formal core uses and D0.2 does not list (H20) | D0.2 + Attempt (read through Θ); its classification OQ2 | FC98 (b) lists it | FC98 holds |
| D13.8 | HM | CreativeCriticalEpisode(s,Δ,h,e) takes s and Δ and uses neither; its four readings (H15) are unregistered | new CCE(s,Δ,h,e) :⟺ ∃h' ⊆ h up to e: CompleteCritical(h') ∧ h_Δ ⊆ h' ∧ ∃ Origin(s,c,p,h,e') with Build subhistory ⊆ h' ∧ Conn(G,h') [A3-08]; text KEEP | none (FC89, FC90 not encoded as histories) | FC90 holds |
| D14.1 | HW | L441's 'lost exactly when it fails on an occasion it covers' is unbounded and calls lost an aim (P) does not protect (FC86 look; both readers) | new Lost_{ξ,ξ'}(r) :⟺ r(ξ) ∧ ¬r(ξ'); (P)'s second conjunct ⟺ ¬∃r∈P Lost; text L441 formal | FC86 parts 2, 3 | FC86 holds; FC87 holds; FC88 holds |
| D14.3 | NO | Attr is per aim, so Mimo's wrong attribution does not arise; the sentence's second half is negative and D14.3 matches it (GLM's positive half is not in the words) | none | none | FC87 holds |
| D14.5 | INV | 'requires' as necessary-only or as a characterization: (EX) takes O_ex as a declared marking either way (I59); OQ4 | none | none | FC89 not tested |
| D14.6 | HW | 'the relevant binding of c' is undefined and ProducesVia needs it; L405 lists 'the bindings constructed' in the trace (both readers) | D14.6 kept; text L453 pointer, settles I60 | none | FC90 holds |
| D14.7 | HM | as D13.8 (s, Δ unused); 'contract fixed at e_c' is in L453 ('The scope ... is the contract fixed at e_c'): NO on that half | via D13.8 new | none | FC90 holds |
| D14.8 | NO | 𝓡 ⊆ Act × Occ × Eff types k in 𝓡[a,k] as an occasion; the text fixes it; values untouched | none | none | — |
| D15.1 | HM | resources and side effects are 'explicit' parts of a task (L461); D15.1 records them and no definition carries them | old T a relation (resources stated) → new T := (T_rel, Res_T, Side_T), equal iff all three equal | none (no claim reads Res, Side) | FC91 holds |
| D15.2 | HM | E17: (CT1) has no tolerance, yet Cap^{q,r} (D15.7) uses 'a realization at (q,r)'; how tolerance meets the execution family is open (per execution or over the family) | new RetReal^{q,r}_ϑ(π,T,C;χ), ϑ ∈ {per-execution: o ∈ T^q[i], z' ∈ C^r for every η; family: a bound on failing executions} [A3-09]; ϑ not chosen (OQ12) | none | FC91 holds; FC93 holds |
| D15.4 | NO | Ω as a relation on states is 'what makes it the same system through change' read extensionally; no claim needs more (Mimo); E13 wants procedure outside the process (S21, S27) | none | none | — |
| D15.5 | HM | D15.5 applies Owned to a protocol and a constructor attribute; D13.7 defines it for subhistories (H20); 'requires' vs ⟺ is an unrecorded reading | new Owned_β(π,C,s) :⟺ every execution of π from z ∈ C is a subhistory owned by s [A3-12]; Can's ⟺ recorded [A3-13] | none | FC93 holds |
| D15.6 | NO | 'ends with an organization in C_I' is 'a continuing organization in C_I' extensionally; 'independently specified J_p' is not formalizable here (NF.new) | none; NF.new1: 'independently specified' (L477) | none | — |
| D15.7 | INV | Admit ⊇ realized tasks and antitonicity are the text's (T14); a strictest non-exact tolerance (Mimo) is left open by L479 ('none is exact'); OQ5 | none | none | FC93 holds |
| D15.8 | NO | L481's second clause is a consequence of its first (t ∈ 𝒯 ∧ needs(t,p) ⇒ some member has p), not circular; D15.8's 'parts(t) ⊆ parts of the stated construction' is a reading | none; reading registered [A3-14] | none | FC77 counterexample; FC78 counterexample |
| D16.1 | INV | 'can affect' read as 'on an active route' is a reading (H16); the modal is carried by ∃ continuation; OQ6 | none; H16 registered [A3-15] | none | FC94 not tested |
| D16.2 | INV | 'owned enabling continuation' has two readings (I74 vs L495's χ); I74 chose one | none | none | FC94 not tested; FC110 not tested |
| D16.3 | HW | E17: 'non-question-begging' (NF11) is undefined, and (U1) is met trivially if χ may supply c; the text's 'in the sense of (CT1)' is fine (L463 names χ enabling conditions) | maths: + NQB(χ,s,U_c) :⟺ no realization witnessing Can(ξ0,U_c;χ) uses an occurrence o with Rep(o,c) whose provenance was relayed from outside β [A3-10]; text KEEP (NF11 stays open in the words) | none | — |
| D16.4 | HW | L528's classes are classes of interpretations; (U3) is a set of tuples (M,s,ξ0,Ω,β); 𝔓^adv_Θ undefined (NF12, OQ7) | D16.5 new Universal := {M : ∃s,ξ0,Ω,β (M,s,ξ0,Ω,β) ∈ UECS}; text L528 formal | none | FC110 not tested |
| D16.5 | HM | 'in a critical episode' narrows L528's 'connected to a critical episode' (Mimo, GLM); typing as D16.4 | CreativeEp := {M ∈ Base : a (G) instance with Conn(G,h') for a critical episode h'} [A3-08]; Universal as D16.4 | none | FC110 not tested |
| D18.1 | HW | L526's 'no cycle' fails as worded: with 'represented' (L197, L405) read through (R), Rep has two fixed points for a first construction and none for a selection (computed) | new: dependence staged or structural, parameter ρ ∈ {K, T} (OQ1, A3-02); + dep(NonCircular), dep(NonVacuous) | FC98 implemented (a), (a'), (b), (c), (d) | FC98 holds |
| E8 | NO | the encoding places 𝒬 in a port (I67); E20's fixed ports: adding a port is building a new organization (L425), not an edit of the old | none (text L590 names 𝒬 as a port under FC97) | none | FC97 holds |
| E9 | HW | as E10: L626's 'can only predict from occupancy' fixes no memory bound, and without one its conclusion fails for one thing | as E10 | as FC102 | FC102 holds; FC103 holds |
| FC15 | NO | the counterexamples rest on E having a baseline other than σ(b0) (I12) or on a closure condition L141 does not state; (K) on τ[C] needs no baseline | none | none | FC15 holds; FC16 holds; FC17 holds |
| FC18 | HW | the counterexample rests on I94, which L556 excludes (T03): NO on it; but L558's quoted condition says 'each component' and 'a component', wider than L554's active components and subnetwork counterparts (Mimo) | FC18's SameKind over k ∈ Γ kept; text L558 formal (quoted condition → ∀k∈Γ SameKind_C(k,λ(k))) | none | FC17 holds; FC18 counterexample (I94 part, as committed); D4.4 part holds; FC96 holds |
| FC31 | HW | as D6.7 | as D6.7 | none | FC31 not tested (syntactic) |
| FC32 | HW | L526 names no ancestors for NonCircular and NonVacuous, which use ℓ, δ, t, C and Σ | D18.1 + edges NonCircular → (O),(Q),t,C,ℓ,δ; NonVacuous → (O),C,Σ; text L526 formal | FC98 DEP carries them | FC98 holds; FC32 not tested (syntactic) |
| FC56 | HM | (a) holds only with j's declared scopes held (Mimo's grain model); GLM's near miss adds W to Accepted, so it is not withdrawal alone | (a) + hypothesis C_j(u) ⊆ C_j'(u), ℓ, β equal; + (c) Accepted_j(ξ') ⊆ Accepted_j(ξ), Forms, Scope fixed ⇒ X^{ξ'}_j(φ) ⊆ X^ξ_j(φ) | FC56 rewritten: (a), (a''), (b), (c), (c') | FC56 holds |
| FC69 | HW | as D9.4 | as D9.4 | none | FC69 holds |
| FC70 | HW | L393's 'Withdrawing a premise makes the step unusable' fails for a premise also concluded by a usable step below (matter 9) | new: d∈Prem(u) ∧ d∉Accepted_j(ξ') ∧ ¬∃u'∈Below(u)[concl(u')=d ∧ Usable^{ξ'}_j(u')] ⇒ ¬Usable^{ξ'}_j(u); text L393 formal | FC70 + for-all part | FC70 holds |
| FC71 | HW | as D9.9 | as D9.9 | as D9.9 | FC71 holds |
| FC72 | INV | Mimo (1) rests on a dependence reading of 'among its premises' (I39, I40); (2) the two blocks are separate clauses ('nor does') and D9.7 applies both: no contradiction | none | none | FC72 holds |
| FC74 | HM | the witness shows no represented premise (L383) and D9.10 dropped p; Acc takes no history (FC30), so adding the representation keeps the witness | new ∃c [Rep_ℓ(o_g,g) ∧ ¬Bearing(c,z,p)] and ∃c,p,p' [Bearing(c,z,p) ∧ ¬Bearing(c,z,p')] | FC74 rewritten (2 parts) | FC74 holds |
| FC75 | HM | as D11.4 | as D11.4 | as D11.4 | FC75 holds; FC76 holds |
| FC76 | NO | 'does not give' is the non-entailment UsesReason ⇏ Bearing, Usable, which FC76 is; Mimo's model adds acceptance, not use | none | none (reruns under new D11.4) | FC76 holds |
| FC80 | HW | L574's step 'that transport survives on H' fails when (τ(a),σ(b)) is also the image of a pair of H (second check §5; computed); Mimo's (i)-(iii): L574's 'supplied independently' fixes I02 | + (d) (τ(a),σ(b)) ∉ (τ×σ)[H] ∧ t survives on H ⇒ t altered there survives on H; text L574 formal | FC80 parts 3, 4 | FC80 holds |
| FC85 | INV | c ≡ c fails only if the identity is not a transport, a property of I81's generated space; L413 fixes c's contract | none | none | FC85 holds |
| FC86 | HW | as D14.1 | as D14.1 | FC86 parts 2, 3 | FC86 holds |
| FC87 | NO | as D14.3 | none | none | FC87 holds |
| FC88 | INV | which aims count for 'Losses outside P' is I58's; GLM agrees with the reading computed | none | none | FC88 holds |
| FC89 | NO | kind-matching is carried by o's own condition being met (¬o(ξ) ∧ o(ξ')); (EX) needs nothing more | none | none | FC89 not tested |
| FC90 | HW | L628 says '(G) is met' without Attempt and '(EX) is met' from Account and 'deployable' alone; (EX) needs six more conjuncts (GLM) | FC90 new: every conjunct of (EX) is a stated condition of L628's conclusion; text L628 formal (2 spans) | FC90 implemented (2 parts) | FC90 holds |
| FC91 | HW | as matter 10; Mimo's domain model is removed by F quantifying over dom T | as matter 10 | none | FC91 holds |
| FC92 | HM | I61 scoped L469's nonemptiness to z ∈ C; L469 says 'on admitted inputs' with no scope on z; with the scope, a state with no execution sits in gfp(F) (Mimo) | D15.2 standing assumption: Exec(π,z,i;χ) ≠ ∅ for every z ∈ Z, i ∈ dom T; + FC92 (e) no vacuous member of gfp(F) | FC92 parts 2, 3 | FC92 holds; FC91 holds |
| FC93 | NO | (CT3) follows because 'achievable' includes 'has a realization' (T14); GLM's OQ5 recorded | none | none | FC93 holds |
| FC94 | HM | (b) 'no finite set decides UU' says both directions where L509 says 'does not suffice' (Mimo); 'a historical extension leaves it open' is unformalized | (b) new: no finite set of performed tasks suffices for UU (𝔈_Θ infinite, I75); NF.new2: 'historical extension' | none (FC94 not tested) | FC94 not tested |
| FC96 | INV | Mimo's (ii) model needs value maps (I14); the text has port translations and no value maps (T03) | none | none | FC96 holds |
| FC97 | HW | L590's 'alter 𝒬' needs 𝒬 among the organization's ports, which the words' port list omits (Mimo); the second conjunct is untested (GLM), Mimo's infinite-edit attack rests on finite footprints (I77) | E8 already has the query port; text L590 formal (settles I67 for the query port) | none | FC97 holds |
| FC98 | HW | as D18.1 (a); (b) the formal core needs sinks L522 does not list (OQ2) | as D18.1 | FC98 implemented | FC98 holds |
| FC99 | NO | Acc is meeting (E) (D6.7); no mismatch | none | none | FC99 holds |
| FC100 | NO | L612's 'does not apply to coarsenings, changed boundaries' holds indices fixed (Mimo's grain attack is a changed grain); populations are parts of histories | D18.2: + indices ℓ, β, Ω held fixed (clarification) | none | FC100 holds |
| FC101 | NO | the account claim is Acc on each model's question; (E) is universal over C's pairs, so Mimo's existential worry does not arise | none | none | FC101 holds |
| FC102 | HM | the counterexample is to the formalizer's added converse (second check); E10/Mimo: L626 needs a memory bound (handled under E10) | (b) second half dropped (look); + (b'') w ≤ L ⇒ no window-w occupancy predictor survives (one and two things) | FC102 parts rewritten | FC102 holds |
| FC103 | NO | the query is occupancy (L622, L630), so ψ keeps the answers (Mimo's δ naming thing 1 is outside the episode); 'admits each edit for both things alike' is ψ[C] = C (GLM's asymmetric C is excluded) | none (I69 settled under I69) | none | FC103 holds |
| I13 | NO | L556's formula writes the counterpart's signature in full, fixing the extension (T05); only 'By (K)' is loose (matter 1) | none | none | FC17 holds |
| I38 | INV | as D9.1 | none | none | FC72 holds; FC73 holds |
| I39 | INV | 'made from' is primitive in the text too; the structural reading points to NC1 (I24) | none | none | FC72 holds; FC60 holds |
| I40 | HW | as D9.4 | as D9.4 (settles I40) | none | FC69 holds |
| I41 | NO | both readers: the text settles taking up and withdrawal (L393) | none | none | FC56 holds |
| I42 | INV | as D9.5 | none | as D9.5 | FC56 holds |
| I43 | HW | as D9.9 | as D9.9 (settles I43) | as D9.9 | FC71 holds |
| I44 | HW | as D11.3 | settled by its choice (b) | none | FC75 holds |
| I46 | INV | the four phrases are defined nowhere; D11.4 carries formal readings; the text needs no new prose for them (S40) | D11.4 new (see D11.4) | as D11.4 | FC75 holds |
| I47 | INV | as D9.11 | none | none | FC76 holds |
| I54 | INV | as D12.4 | none | none | FC78 counterexample |
| I55 | INV | as D13.1 (3) | none | none | FC97 holds |
| I57 | INV | which aim ProducedBy runs to and the left r(ξ) are open; (P)'s first conjunct is existential, so the two choices coincide in force (GLM) | none (D14.1 + Lost uses r(ξ) as (P) does) | none | FC86 holds; FC87 holds |
| I58 | INV | as FC88 | none | none | FC88 holds |
| I59 | INV | as D14.5; OQ4 | none | none | FC89 not tested |
| I60 | HW | as D14.6 | settles I60 (L453 pointer) | none | FC90 holds |
| I61 | HW | as matter 10 and FC92 | settles I61 (L471 formal); D15.2 nonemptiness for every z | FC92 parts 2, 3 | FC91 holds; FC92 holds |
| I62 | NO | T14: 'physically achievable' includes having a realization; antitonicity follows from L479's order; OQ5 recorded | none | none | FC93 holds |
| I67 | HW | as FC97 | settles I67 (query port only; the value sets stay open, OQ9) | none | FC97 holds |
| I68 | HW | as E10 | settles I68 (window, via L626) | as FC102 | FC102 holds |
| I69 | HW | 'built alike' is undefined and Argument 10 needs ψ ∈ Aut(P) with ψ[C] = C and answers kept (both readers) | settles I69 (L630 formal) | none | FC103 holds |
| I70 | NO | L612's list and exclusions fix it: 'all carriers' carries Θ's interpretation; indices fixed | D18.2 clarification (see FC100) | none | FC100 holds |
| I71 | INV | as D12.9; PARKED point recorded | none | none | FC80 holds |
| I74 | INV | as D16.2 | none | none | FC94 not tested |
| I75 | INV | 'can hold' fixes membership; infinitude of 𝔈_Θ is open and FC94 (b) rests on it (both readers) | none (FC94 (b) states its assumption) | none | FC94 not tested |
| I87 | INV | the structural reading is the text's; propositional vs first-order stays open | none | none | FC56 holds; FC71 holds |
| I88 | NO | 'argument steps whose leaves are premises' gives every argument a step (GLM); the finite range is a search bound; Mimo's point on what an argument is is OQ8 | none | none | FC56 holds |
| I89 | INV | forms are per assessor ('one j admits'); the fixed set is a search bound | none | none | FC71 holds |
| I95 | INV | a search bound; its timing alternative is now used by AtRest (A3-05) | Circuit + run times in FC75 (b) | as D11.4 | FC75 holds |
| I100 | HW | as E10: the occlusion's length L in steps is what L626's conclusion turns on; the end rule and sharing stay open (OQ10, H17) | settles I100's occlusion as L hidden steps (via L626) | as FC102 | FC102 holds |
| H09 | HM | L481 fixes the population as the admitted set (equality); D12.1 writes inclusion | D12.1: 'members of 𝒯 admitted' → '𝒯 = the D15.8 population' | none (sel() takes 𝒯 by hand, I90) | FC77 counterexample; FC78 counterexample |
| H11 | HM | as D11.4 (the at-rest clause) | as D11.4 (¬AtRest, A3-05) | as D11.4 | FC75 holds |
| H12 | HM | as D9.10 | as D9.10 (A3-01, A3-03) | as D9.10 | FC74 holds |
| H14 | HM | Contrib is a primitive no definition uses; L427's distinction is Owned's not reading authorship | D13.7: Contrib dropped | none | — |
| H15 | INV | the four readings of L429 are unregistered choices; how s and Δ enter is HM (D13.8) | registered [A3-08]; CCE as D13.8 | none | FC90 holds |
| H16 | INV | as D16.1; OQ6 | registered [A3-15] | none | FC94 not tested |
| H17 | INV | L620 says nothing of interaction; L622's 'faithful on H_0' is a satisfiable stipulation (an H_0 without shared cells) | registered [A3-16] | none | FC102 holds |
| H19 | INV | Org_ℓ(h) and 'subhistory' are used and unnumbered | registered [A3-07] | none | FC75 holds |
| NF02 | NO | L536 is formal in shape once 'is an explanation' is an uninterpreted atom (section 'Part XV' below); E06's point on it is OQ3 | Part XV formal shapes (below) | none | — |
| NF03 | NO | L17 and L538 state the same necessity thesis (representable on some contract); E06's per-question thesis is not the text's | Part XV formal shapes (below) | none | — |
| NF05 | NO | (Prov)(i) is unsatisfiable by definition (FC80 (a)); (ii), (iii) rest on undefined 'without loss' and 'operates on' | Part XV formal shapes (below) | none | FC80 holds |
| NF11 | HW | as D16.3 (E17) | as D16.3 (A3-10) | none | — |
| matter 1 | HW | L556 says 'By (K)' of a subnetwork, where (K) is stated for a component; the formula itself is D4.4 (T05) | text L556 pointer (D4.4) | none | FC17 holds; FC18 counterexample (I94 part, as committed); D4.4 part holds |
| matter 3 | HW | 'signature' at L584 in the everyday sense beside the defined (K) invites equivocation (both readers) | text L584 formal (Surp's definition, D12.7) | none | FC81 counterexample |
| matter 9 | HW | as FC70 | as FC70 | as FC70 | FC70 holds |
| matter 10 | HW | 'complete' in L471 admits the weaker reading under which C ⊆ F(C) is weaker than (CT1) (FC91 witness) | D15.3 kept; text L471 formal (settles I61) | none | FC91 holds; FC92 holds |
| matter 11 | INV | the phrases of L375 and L385 are carried by D11.4 and D9.11 as declared data or primitives; no new prose (S40) | none | none | FC75 holds; FC76 holds |
| L443 | NO | the round-1 change stands (both readers); 'requires' is OQ4; the worked case is fixed under FC90 | none | none | FC89 not tested; FC90 holds |
| L471 | HW | as matter 10 | as matter 10 | none | FC91 holds; FC92 holds |
| L520 | HW | as D6.7 | as D6.7 | none | FC31 not tested (syntactic) |
| E03 | HW | Rep → Con → Build → Rep is a cycle of the words (D18.1); L526's 'no cycle' fails as worded; computed: two fixed points / none | as D18.1; the cut is OQ1 (A3-02); no text change until chosen | FC98 (c), (d) | FC98 holds |
| E06 | HW | Suff at L536 adds 'a transport whose provenance is not declared', absent from L17's statement and from (E) (L277): two defeat sets, Def(L536) ⊊ Def(L17); Nec: NO (L17 = L538) | Part XV formal shapes (below); which Suff to keep is OQ3 | none | — |
| E10 | HW | L626's 'can only predict from occupancy' fixes no memory bound; a predictor over the whole occupancy history reads the velocity and survives (one thing) | text L626 formal hypothesis w ≤ L (settles I68, I100's L; A3-11) | FC102 (b'), (b'') | FC102 holds |
| E13 | NO | the text declares indices and makes every claim relative to them (L524, L608); a procedure fixing them before testing is outside the process (S21, S27) | none (a finding about scope) | none | — |
| E17 | HM | tolerance vs the execution family is open (D15.2) and 'non-question-begging' is undefined (D16.3) | A3-09, A3-10 (see D15.2, D16.3) | none | FC93 holds |
| E20 | NO | adding a port is building a new organization (L425: 'adding it is construction'); (O)'s fixed port set per organization is consistent with that | none | none | FC97 holds |
| C06 | INV | whether blind exhaustive composition is 'a nontrivial binding construction relevant to that use' and task use 'explanatory use' is Build's primitives (I56, I115); the case has no outside verdict | none (D13.3 new carries ExplUse as a primitive) | none | FC98 holds |

## Formal fixes, old → new (formal core notation)

- **D0.2** + Attempt, Qf [A3-01], ExplUse [A3-04], AtRest [A3-05], Org_ℓ(h) and subhistory [A3-07], Below; − Contrib. Their class (read through Θ, declared input, or defined) is OQ2.
- **D9.2** + Below(u) := the steps of the subtree of u other than u. **D9.4** kept: Live_j(d;u) :⟺ ∃u'∈Below(u) [d = concl(u') ∧ Usable_j(u')] ∨ d ∈ Accepted_j(ξ). Settles I40 (L393).
- **D9.9** old: (i) α∈X_j(O), conditional live, MT admitted ⇒ α+1 step ∈ X_j(T∧B∧I); (ii) from those premises X_j(T), X_j(B), X_j(I) gain nothing.
  new: u⁺ := step with Prem(u⁺) = {concl(α), T∧B∧I⇒O}, concl(u⁺) = ¬(T∧B∧I); α⁺ := α under u⁺.
  (i) α∈X_j(O) ∧ Usable_j(u⁺) ∧ ∀ leaf l of α [¬(T∧B∧I) ∉ conj(l) ∧ ¬MadeFrom(l, ¬(T∧B∧I))] ⇒ α⁺ ∈ X_j(T∧B∧I), for any Form(u⁺) ∈ Forms_j;
  (ii) ∀x∈{T,B,I}: ¬RO(α⁺, x);
  (iii) Forms_j classically sound ⇒ no α' with leaves ⊆ leaves(α) ∪ {T∧B∧I⇒O} has α' ∈ X_j(x). Settles I43 (L395).
- **D9.10** old: p_δ supplied with c; Bearing(c,z,p) :⟺ Acc(ℰ_c). new: p_δ := Qf(z,δ,p) [A3-01]; ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_c), t_c, Γ_c, δ_c supplied with c [A3-03]; Bearing(c,z,p) :⟺ Acc(ℰ_c). A criticism's premise g: Rep_ℓ(o_g, g) for some o_g of the system (L383).
- **FC56** (a) + hypothesis ∀u [C_j(u) ⊆ C_j'(u) ∧ ℓ_j(u) = ℓ_j'(u) ∧ β_j(u) = β_j'(u)]; + (c) Accepted_j(ξ') ⊆ Accepted_j(ξ), Forms_j and Scope_j fixed ⇒ X^{ξ'}_j(φ) ⊆ X^ξ_j(φ).
- **FC70** new: d∈Prem(u) ∧ d∉Accepted_j(ξ') ∧ ¬∃u'∈Below(u)[concl(u') = d ∧ Usable^{ξ'}_j(u')] ⇒ ¬Usable^{ξ'}_j(u).
- **FC74** new: ∃c,z,p [Rep_ℓ(o_g,g) ∧ ¬Bearing(c,z,p)]; ∃c,z,p,p' [Bearing(c,z,p) ∧ ¬Bearing(c,z,p')].
- **D11.3** old: ≺_h a strict partial order [I44]. new: ≺_h acyclic; ⪯_h := ≺_h* (reflexive-transitive closure). Settles I44 by its choice (b) (L375).
- **D11.4** old (I46): R connected, i, r ∈ R, every n ∈ R on a ≺_h-chain from i to r inside R, relations met, ∃(x,x')∈K: setting i's port changes r in Org_ℓ(h).
  new: ActRoute_h(R;i,r,K) :⟺ i, r ∈ R ⊆ O_h ∧ ∀n∈R: n ⇝_R r ∧ ∀n∈R: n meets Org_ℓ(h)'s relation ∧ ∃(x,x')∈K: val_r(Org_ℓ(h)|_R[i:=x]) ≠ val_r(Org_ℓ(h)|_R[i:=x']) ∧ ¬AtRest_h(R,r); Org_ℓ(h)|_R holds every occurrence outside R at its value in h [A3-06]; AtRest [A3-05].
- **FC75** new: (a) no dependence along R ⇒ ¬ActRoute; (a') dependence only outside R ⇒ ¬ActRoute; (a'') a side input feeding r inside R is admitted; (b) AtRest ⇒ ¬ActRoute; (c) ActRoute is a function of (h, Org_ℓ(h), R, i, r, K, run times); (d) a member with no path to r inside R ⇒ ¬ActRoute.
- **D12.1** (H09): "the members of 𝒯 are admitted by the physics" → 𝒯 = D15.8's population (L481's equality).
- **D13.3** old: Build :⟺ ∃h' [Owned_β(h',s) ∧ Prepares(h',c) ∧ BindingConstruction(h',c) ∧ ¬TransferComposite(h')].
  new: Build :⟺ ∃h' ⊆ h ending at e [Owned_β(h',s) ∧ ∃o output of h' [Prepares(h',o,c) ∧ Rep^ρ_ℓ(o,c) ∧ ExplUse(o,c)] ∧ BindingConstruction(h',c) ∧ ¬TransferComposite(h')], ρ ∈ {K, T} (D18.1; OQ1) [A3-04].
- **D13.7** Contrib dropped (no definition used it; L427's distinction is that Owned_β reads no authorship).
- **D13.8** new: CCE(s,Δ,h,e) :⟺ ∃h' ⊆ h up to e [CompleteCritical(h') ∧ h_Δ ⊆ h' ∧ ∃c,p,e' (Origin(s,c,p,h,e') ∧ its Build subhistory ⊆ h' ∧ Conn(G,h'))]; Conn(G,h') :⟺ the (G) instance's Attempt addresses the question h''s recognized difficulty poses [A3-08].
- **D14.1** + Lost_{ξ,ξ'}(r) :⟺ r(ξ) ∧ ¬r(ξ'); so (P)'s second conjunct ⟺ ¬∃r∈P Lost_{ξ,ξ'}(r) (FC86 part 2).
- **D14.7** s and Δ enter through D13.8 new.
- **D15.1** old: T a relation, resources and side effects stated. new: T := (T_rel, Res_T, Side_T); T = T' ⟺ all three equal.
- **D15.2** standing assumption old: Exec ≠ ∅ for z ∈ C, i ∈ dom T [I61]. new: Exec(π,z,i;χ) ≠ ∅ for every z ∈ Z, i ∈ dom T (L469). + RetReal^{q,r}_ϑ, ϑ a parameter [A3-09; OQ12].
- **D15.5** + Owned_β(π,C,s) :⟺ every execution of π from z ∈ C is a subhistory owned by s (D13.7) [A3-12]; Can's ⟺ registered [A3-13].
- **D16.3** + NQB(χ,s,U_c) :⟺ no realization witnessing Can(ξ0,U_c;χ) uses an occurrence o with Rep_ℓ(o,c) whose provenance was relayed from outside β [A3-10]; Enable(s,T,χ) :⟺ Θ admits χ ∧ NQB ∧ χ an enabling condition of (CT1).
- **D16.5** new: CreativeEp := {M ∈ Base : M has a (G) instance with Conn(G,h') for a critical episode h'} [A3-08]; Universal := {M : ∃s,ξ0,Ω,β (M,s,ξ0,Ω,β) ∈ UECS}.
- **D18.1** new: + edges NonCircular → (O),(Q),t,C,ℓ,δ; NonVacuous → (O),C,Σ. The loop: Rep^ρ with ρ ∈ {K, T} [A3-02]:
  K: in Sel, Con and Build at o, (R) is read only at o' ≺_h o;
  T: Con's "available as a represented target" := Held(o',c) :⟺ ∃t Faithful(t: Org_ℓ(o') → c) (through Θ, no provenance), o' in the episode; Sel's exclusion := ¬Held(o',c) for o' ≺_h o.
  Unstaged (the words, U): FC98 (c): two fixed points for a first construction, none for a selection. K and T: one each; K gives no representation to a first construction of c, T gives one.
- **D18.2** + the indices ℓ, β, Ω are held fixed (L612: "does not apply to coarsenings, changed boundaries").
- **FC80** + (d) (τ(a),σ(b)) ∉ (τ×σ)[H] ∧ t survives on H ⇒ t with a relation of E altered at (τ(a),σ(b)) survives on H.
- **FC90** new: the conjuncts of (EX) (D14.7) are all stated conditions of L628's conclusion.
- **FC92** + (e): every z ∈ gfp(F) has, on every i ∈ dom T, an execution completing with o ∈ T[i].
- **FC94** (b) old: no finite set of performed tasks decides UU. new: no finite set of performed tasks suffices for UU (𝔈_Θ infinite, I75).
- **FC102** (b) second half (the formalizer's converse) → a look; + (b'') w ≤ L ⇒ no window-w occupancy predictor survives the extended history (one thing and two).

## Part XV: what can and cannot be formalized

Let Expl(ℰ) be an atom with no definition: no definition's right-hand side uses it; it occurs only as a claim ruled out. Let Uses(α) be the symbols of α's leaves and forms. "An argument not using (E)" := (E), Acc ∉ Uses(α). Then:
- (Suff), L536: defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α∈X_j(Expl(ℰ)): Acc ∉ Uses(α)]. L17's statement has no ¬Dec(t): Def(L536) ⊊ Def(L17) (E06; OQ3).
- (Nec), L538 = L17: defeated for j ⟺ ∃ℰ [∃α∈X_j(¬Expl(ℰ)): Acc ∉ Uses(α) ∧ ∀C' on D ∀t': ¬Faithful_{C'}(t': D → E)].
- (Elim), L540: defeated ⟺ ∃ℰ,ℰ' with equal (F1), (F2), (A) data at every admitted change ∧ a kind-label κ(ℰ) ≠ κ(ℰ') ∧ Work(κ). Work ("does explanatory work") has no definition.
- (Prov), L542: (i) ∃t [Sel(t;𝒯,μ,H) ∧ (a,b)∈C∖H ∧ ∃t'∈𝒯 surviving on H with value_t'(a,b) ≠ value_t(a,b) ∧ value_t(a,b) a function of (𝒯,H)]: with 'determined by its history' read so (FC80 (b)), unsatisfiable by definition (FC80 (a)), and only an argument against Argument 3's premises can meet it; read as 'fixed by the actual run', every selected t meets it, and it defeats nothing. (ii) "rewrites every construction trace as a selection history without loss": "without loss" has no definition. (iii) Out_j(¬"explanation operates on the object layer"): an atom, like Expl.
- (QF), L544: "fails to capture" and "not creative" (outside (G)) have no definition.
- A mathematical error, L546: a model of a named claim's stated hypotheses where its conclusion fails (FC109): fully formal.

Can be formalized: the shape Out_j(φ) through an argument not using (E) (D9.8, FC56), Acc, Faithful, Sel, value, and the quantifiers. Cannot: Expl ("is an explanation"), Work, "capture", "without loss". So no computation decides a defeat condition; a defeat is an argument some assessor j can use (Out_j), and the ruling out is j's choice (L397, S28).

## New inventions (provisional ids)

| id | fills in for | invented | other choices | why this one |
|---|---|---|---|---|
| A3-01 | L377 "the question whether z has δ in respect of p" | Qf(z,δ,p), a primitive question-forming map | p_δ supplied with c (drops p); Qf defined in (Q) (no such operation in the text) | L377 builds p_δ from z, δ, p |
| A3-02 | L197, L405 "represented", L526 "no cycle" | Rep^ρ, ρ ∈ {K staged by ≺_h, T structural}, not chosen | U (the words: no unique Rep); trace as stated data (Mimo); a definition by stages (E03) = K | both remove the cycle; the choice is OQ1 |
| A3-03 | L377 "with its transport and its identified commitments" | t_c, Γ_c, δ_c supplied with the criticism (H12) | read off the connection (not always unique) | the definite article presumes them |
| A3-04 | L405 "prepares a represented organization for explanatory use" | Prepares(h',o,c) ∧ Rep^ρ(o,c) ∧ ExplUse(o,c), ExplUse primitive | I56's Prepares(h',c) alone (drops both phrases) | keeps the words (Mimo); C06 shows the class turns on ExplUse |
| A3-05 | L375 "already at rest when the result occurred" | AtRest_h(R,r), read through Θ's run times; reading (a) all of R∖{r} ends before r starts, (b) nothing of R runs at r and no product of R is carried to r | the clause dropped (I46) | the text states the clause; which reading is open (GLM (a), Mimo (b)) |
| A3-06 | L375 "connected subnetwork … joining … which has nonconstant dependence" | every member of R reaches r inside R; dependence along R with the outside held at actual values | I46's chain clause; dependence in the whole Org_ℓ(h); outside R deleted | admits side inputs (Mimo B), excludes idle members and dependence outside R (Mimo A) |
| A3-07 | L375 "subhistory"; D11.4 "Org_ℓ(h)" | Org_ℓ(h) the organization Θ gives h; a subhistory a subset closed under the interpretation, ≺ restricted (H19) | Org_ℓ per occurrence only (L213) | D11.4 needs the whole history's organization |
| A3-08 | L429 "connected to its inquiry"; L528 "connected to a critical episode"; CCE(s,Δ,…) | Conn(G,h'): the (G) instance's Attempt addresses the difficulty's question; s the system of Origin; h_Δ ⊆ h' | GLM: Δ the episode's subhistory, s the owner of G's subhistory; Mimo: Δ the response's contribution | uses (G)'s own s; ties Δ to the episode as (EX) needs |
| A3-09 | L461 "short of exact", L479 tolerances, L466 (CT1) | RetReal^{q,r}_ϑ with ϑ ∈ {per execution, over the family} | (CT1) exact only (Cap^{q,r} undefined) | E17; ϑ not chosen (OQ12) |
| A3-10 | L495 "non-question-begging" | NQB: no witnessing realization uses a relayed outside carrier of c | undefined (NF11); no outside carrier of c at all (excludes teaching) | excludes supplying c, permits teaching (L405: reconstruction is construction) (E17) |
| A3-11 | L622 "recent", L626 "can only predict from occupancy" | window w ≤ L (L_occ in the text), L the steps the thing is hidden | w ≤ L+1 (exact only where the thing stays hidden; FC102 (b')); unbounded memory (L626 fails) | sufficient on the encoding for one and two things (FC102 (b'')) |
| A3-12 | L475 "owned retained realization" | Owned_β(π,C,s) via D13.7 on the executions (H20) | ownership of π as a static object | D13.7 defines ownership for subhistories |
| A3-13 | L475 "requires" | Can's ⟺ (the line is its definition) | necessary conditions only (then UU cannot be met) | the bold head makes the line a definition |
| A3-14 | L481 "the stated construction admit" | parts(t) ⊆ the stated construction's parts (D15.8) | any part the physics admits | GLM: the reading was unregistered |
| A3-15 | L487 "can affect its operative use" | ∃ admitted owned continuation with a result on an active route to d's operative use (H16) | "can change" (I74); left modal | OQ6 |
| A3-16 | L620 two things | things do not interact, may share a cell and cross (H17) | things that exclude one another | the encoding's choice; FC102's two-thing findings rest on it |

NF.new1: L477 "independently specified J_p" (not formalized). NF.new2: L509 "a historical extension leaves it open" (not formalized).

## Owner questions (recorded, not applied)

- **OQ1 (E03, D18.1, D13.3; A3-02).** K: representations inside Sel, Con, Build read only at earlier occurrences; no cycle, but a first construction of c gives no representation of c (FC98 (d)). T: Con's represented target read as held through Θ; no cycle, and a first construction represents (L405's "A first representation may be constructed").
- **OQ2 (FC98 (b), L522, L596).** The formal core's primitives (δ, Offered, restriction, Integrated, Nontrivial, Prepares, BindingConstruction, TransferComposite, ExplUse, MadeFrom, Applies, Aims*, O_ex, K, Rec, Chg, Rule, Occurs, Attempt, Qf, AtRest). GLM: list them as primitives stated, not defined. Other side: define some, so that L596 holds without new inputs.
- **OQ3 (E06, L536).** Keep "with a transport whose provenance is not declared": (Suff) is claimed only of non-declared transports. Drop it: (Suff) as L17 states it, (E) taking no provenance (L277).
- **OQ4 (I59, L443; GLM).** "requires" as a necessary condition on explanatory aims; or as their characterization.
- **OQ5 (I62, L479; GLM).** (CT3) as a consequence of "achievable" (T14's reading); or as an assumption on Admit.
- **OQ6 (H16, L487; GLM).** "can affect its operative use" read through active routes; or left modal.
- **OQ7 (D16.4, NF12; GLM).** 𝔓^adv_Θ defined; or (U2), (U3) stated as conditional on it.
- **OQ8 (I88; Mimo; reading of "argument", S23).** A bare premise is not an argument ("argument steps whose leaves are premises"); or an argument may have no step.
- **OQ9 (I67; Mimo).** The value sets of the contract's membership and query ports fixed; or left open.
- **OQ10 (I100; GLM).** The rule at the ends of the line of cells stated (reflect, stop); or left open.
- **OQ11 (FC18, I10 (a); Mimo).** A footprint bijection may recode values; or not.
- **OQ12 (E17, A3-09).** Tolerance over each execution's output and return; or over the family of executions (fallible performance kept as capability).
- Not an owner question: GLM's flag on FC102 (the window bound in the words). L626's conditional fails without a bound (computed), so the bound is a fix, not a choice.

## Parked (S33, S34)

- D12.9, I71 (Mimo): the population's restriction and "value" read as "the argument about hard to vary". Recorded, not applied.

## Context items (read; no row)

E01, E07, E09, E11, E12, E18, C09, C10, C12, C13, C14: findings about scope or no line challenged; none changes a verdict above. E08 bears on L584: the formal replacement there (Surp's definition) is the technical term E08's defence names. E16's remark on "argument" (L8, L397) is decision S23's reading: with OQ8, not applied. H20: its parts are ruled at D13.6, D15.5 and D16.5.

## Code changes (area 3 model/)

- `model/phys.py`: `act_route` rewritten (D11.4 new: reach-r clause, `values_along`, `at_rest` with readings a, b); the committed version kept as `act_route_s104` for comparison.
- `model/claims_b.py`: FC56, FC70, FC71, FC74, FC75, FC98 rewritten; FC80, FC86, FC92, FC102 extended; FC90 implemented; FC98 adds `DEP`, `dep_cycle`, `rep_fixed_points`.
- `s104_external.py`, `s104_creative_transport.py`: path depth only (the copy sits one folder deeper); outputs byte-identical to the originals.

## Text changes

`area 3 - text changes.json`: 19 changes on 17 lines, 17 formal and 2 pointers, no deletions. Settles: I40 (L393), I43 (L395), I44 (L375), I60 (L453), I61 (L471), I67 query port (L590), I68 and I100's L (L626; A3-11), I69 (L630).
