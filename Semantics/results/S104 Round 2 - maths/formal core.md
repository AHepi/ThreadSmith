# S104 Round 2 — formal core

*Log S104, review round 2 (the maths round), 27 September 2026, under decision S36 ("maybe exploring the math a bit more might help instead of words. Since words are vague"; "if implementation forces invention, that needs to be recorded"). The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd (not written to). Every quotation of the text is written `> Lnnn | …` and was compared by program (`s104_check.py`) with the line it names; " … " joins fragments of one line, in order.*

**What this is.** The definitions the text's structure rests on, each written as mathematics beside the sentences it formalizes. Where the text fixes something, the mathematics follows it. Where the text leaves something open, the choice made here is marked **[Inn]** and recorded in `inventions register.md` with the other choices that were possible; nothing marked [Inn] is the text's own content. Where the text is vague, the section says so under **Vague**. The claims these definitions let one state and test are in `formal claims.md` (FC01–FC110). Definitions are numbered D§.n; encodings of the text's worked constructions are numbered E1–E9 (§17). Nothing here is settled (S28): every definition is a conjecture about how the text can be written, open to replacement.

**The owner's decisions this file keeps.** No list, count, grade or record of rivals (S20): Part VI's rivals are formalized as a two-place relation on candidates someone has offered, and nothing here ranges over all of them. Nothing about what must happen (S21). No word S23 scrubs in this file's own voice; 'argument' is reasons why this and not that; 'accept' is only tentative. Physical possibility enters only where a content is instantiated or transformed (§§11–16: held, built, carried out) and as the content of a claim a candidate can conflict with (D8.4); questions, contracts, an account and conflict are defined without it (S25–S27). A ruling out that uses a claim taken as given is the choice of the person who takes it as given (S28); here that shows as a declared input, Accepted_j, which no definition sets. What hard to vary covers is parked (S33–S34): §10 writes down only the text's own 'easy to vary' (L317) and adds nothing about what hard to vary covers. The appraisal relation 𝒩 appears only as a typed input (D14.8); where values are placed is the owner's question and is not touched.

## §0 Conventions and the frame

- A condition holds or fails; a program returns yes or no. ⊥ is the undetermined answer (D3.2), not the value of a condition.
- P(X) is the set of subsets of X; ∏ is the cartesian product; z|U restricts a valuation to the ports U; f[S] is the image of S; R* is the reflexive-transitive closure of a relation; ⇀ marks a partial map.
- D is a target, E a candidate's organization; a subscript or superscript names the organization where needed (A_E, B_E, J_E, L^E_k).
- A pair (a,b) is an edit a and a boundary b. x := (τ(a),σ(b)) and x0 := (1,σ(b0)) in §6.

**D0.1 The frame.** Every definition below is relative to a frame Φ: the imports, the declared indices and the declared inputs.

> L31 | The semantics has two imports: the **physical module** \(\Theta\), which says what organization a physical occurrence instantiates at a grain, and the **appraisal relation** \(\mathcal N\), taken as an input wherever a question invokes an appraisal. Grain, boundary, continuity and the contract of admitted changes are **declared indices**: every claim is relative to them, and none is a predicate that a case meets or fails.

> L522 | **Declared inputs.** Besides the two imports, some claims take stated inputs that the semantics records and does not supply: the aims \(O\) and \(P\) of a repair, with the occasions each covers (Part XI); the scope of a contract and why the question asked is answered on that restriction and not on a wider one (Part III); the system boundary and continuity of an attribution (Part XII); for an assessor \(j\), the inference forms \(j\) admits, the scope \(j\) declares and the premises \(j\) tentatively accepts and has not withdrawn (K2, Part IX); a weighting of attribution among several contributions to one achievement, beyond any division its history contains (Part XI).

Φ = (Θ with Org_ℓ; 𝒩 where invoked; ℓ, β, Ω, C; the aims O, P with occasions; the scope statement Σ of each contract; boundary and continuity of each attribution; for each assessor j: Forms_j, the scope declarations Scope_j, Accepted_j(ξ); a weighting where one is used).

**D0.2 Primitives this formalization adds.** Beyond Φ, the formal core uses these symbols, which the text names or needs but neither defines nor lists among its imports, indices or declared inputs. Each is an invention, and FC98 asks of each whether it is a claim read through Θ or a primitive the text does not list: the designation δ of a query [I20]; the undetermined answer ⊥ [I21]; Excl(Σ) [I27]; the restriction operation [I29] (the text calls it declared, L287; L522 does not list it); Offered [I33]; Allow_χ and Applies [I34]; MadeFrom [I39]; the contrast set K of an active route [I46]; Rule, Rec, Chg of reason use [I47]; Integrated and Nontrivial [I55]; Prepares, BindingConstruction, TransferComposite [I56]; Aims* and the exposure record [I58]; O_ex's marking [I59]; Occurs (D11.5).

## §1 Organizations (O)

> L88 | D=(V,(X_v)_{v\in V},J,B,A,L).

> L91 | \(V\) is a set of ports, each with a nonempty value domain \(X_v\). A valuation is an element of \(X_D=\prod_v X_v\). \(J\) indexes components; each component \(j\) has a footprint \(V_j\subseteq V\). \(B\) is a set of boundary conditions. \(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\).

> L94 | L_j(a,b)\subseteq\prod_{v\in V_j}X_v .

**D1.1 Organization.** D = (V, (X_v)_{v∈V}, J, (V_j)_{j∈J}, B, A, ·, 1, L) with: V a set (ports), each X_v ≠ ∅; X_D := ∏_{v∈V} X_v (valuations); J a set (components), each with a footprint V_j ⊆ V; B a set (boundaries); A a set (admitted edits) with a partial composition · : A × A ⇀ A, Kleene-associative, with identity 1 ∈ A **[I01]**; L a function from J × A × B with L_j(a,b) ⊆ ∏_{v∈V_j} X_v. No law ties L_j(a2·a1, b) to L_j(a1,b) and L_j(a2,b) **[I02]**. V and J are the same under every edit **[I03]**.

> L105 | Values of ports may be paths, functions, fields, mathematical structures or histories. Cyclic constraints are admitted. Several solutions remain several.

The X_v are arbitrary sets; no order on J is assumed; nothing selects one solution.

> L100 | \operatorname{Sol}_D(a,b)=\{z\in X_D:\forall j\in J,\ z|_{V_j}\in L_j(a,b)\}. \tag{O}

**D1.2 Solutions (O).** Sol_D(a,b) := {z ∈ X_D : ∀j ∈ J, z|V_j ∈ L_j(a,b)} — the text's (O).

> L103 | A deleted component imposes the full relation on its ports.

> L339 | has a target \(D\) in which the ports and components a rival account would need are absent

**D1.3 Deletion and absence.** j is deleted at (a,b) when L_j(a,b) = ∏_{v∈V_j} X_v. For G ⊆ J, D−G is D with L_j(a,b) := ∏_{v∈V_j} X_v for every j ∈ G and every (a,b). An absent component is a deleted one; an absent port is one on which every component imposes the full relation **[I03]**.

**D1.4 Subnetwork.** A subnetwork is a set N ⊆ J (possibly empty), with V_N := ∪_{j∈N} V_j and Sol_N(a,b) := {z ∈ ∏_{v∈V_N} X_v : ∀j ∈ N, z|V_j ∈ L_j(a,b)}: the constraints of N alone, the rest of D ignored **[I14]**.

## §2 Setting edits and roles

> L103 | An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one. A changed rule is a changed component.

> L119 | An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it

**D2.1 Setting edit; the assigning component.** An edit a sets port v through component j at b when L_j(a,b) = {w ∈ ∏_{V_j} X : w_v = x} for some x ∈ X_v and L_k(a,b) = L_k(1,b) for every k ≠ j **[I04]**. Set_v := the edits of A that, at every b, set v through some component. asg(v) := the component through which the edits of Set_v set v, when there is exactly one; undefined otherwise **[I04]**. 'A changed rule is a changed component': an edit that alters L_j is a change of j, and nothing else is added.

> L109 | No role assignment is supplied. A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly.

**D2.2 Input.** Input_A(v) :⟺ Set_v ≠ ∅.

> L109 | A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

**D2.3 Output.** Out(v, j) :⟺ v ∈ V_j and, for every b ∈ B and all w, w' ∈ L_j(1,b), w|_{V_j∖{v}} = w'|_{V_j∖{v}} ⇒ w_v = w'_v **[I05]**.

> L109 | A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below).

**D2.4 Observation edits (two readings).** For a port o with j = asg(o) and a port m ∈ V_j ∖ {o} ('what it reports') **[I06]**:
- reading R-i: a ∈ Obs(o,m) :⟺ L_j(a,b) ≠ L_j(1,b) for some b, and L_asg(m)(a,b) = L_asg(m)(1,b) for every b. (Setting edits of o are included.)
- reading R-ii: the same, and a ∉ Set_o. (Only recalibrations of the reporting relation.)

Obs := ∪_{o,m} Obs(o,m) in the reading used. Observation(o) :⟺ Obs(o,m) ≠ ∅ for some m. Every claim that turns on Obs is stated under both readings (FC07).

> L109 | The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read.

**D2.5 Direction.** dir(D) := (Input_A, asg): which ports A sets and which component each setting edit replaces. Output status (D2.3) does not use A (FC02).

**Vague.** 'The component assigning that port' (L103, L109, L119) presupposes one assigning component per port; with a relational component (L325's L = H cot θ determines H given L and θ as well as L given H and θ), L109's 'output' does not single one out. D2.1 reads the assigning component off the setting edits, so that 'no role assignment is supplied' stays so [I04]. L109's observation has two readings, and its 'that is' clause equates a condition on A with a signature, which (K) builds on a contract C, not on A [I06]; the families of §4 differ between the readings on the pole's own contract (FC07).

## §3 Questions and contracts

> L138 | p=(D,\ C,\ b_0,\ \mathcal Q,\ O_p,\ \rho_p).

> L141 | The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over; it contains the baseline \((1,b_0)\). \(\mathcal Q\) is a specified set-theoretic operation on \(D\), its solutions and its component structure, with codomain \(Y_p\).

> L147 | \(O_p\) is the set of aims being addressed or protected.

**D3.1 Question.** p = (D, C, b0, Q, δ_D, O_p, ρ_p): the text's tuple with the designation δ_D added **[I20]**; C ⊆ A × B with (1, b0) ∈ C; O_p a set of aims (§14); ρ_p the contract's provenance (D3.4).

> L144 | \operatorname{Ans}_p(a,b)=\mathcal Q(D,a,b). \tag{Q}

> L253 | The query \(\mathcal Q\) is held fixed; an account of a different query is not an account of this one.

**D3.2 Query and answers.** Q is an operation on evaluated organizations: Q(O, a, b; δ_O) ∈ Y_p ∪ {⊥}, a function of Sol_O(a,b), of (L^O_j(a,b))_{j∈J_O} and of the ports and components the designation δ_O names **[I20, I21]**. Ans_p(a,b) := Q(D, a, b; δ_D). For a candidate's organization E with designation δ_E (supplied with the transport, D5.3): Ans_E(a',b') := Q(E, a', b'; δ_E). An answer is determined when it is not ⊥ **[I21]**. The port-reading query: Q_w(O, a, b; δ) := the single value of the projection of Sol_O(a,b) on δ(w) if there is exactly one, ⊥ otherwise.

> L151 | A production question has a \(\mathcal Q\) that reads an output port and a \(C\) containing interventions on upstream ports. An identification question has a \(\mathcal Q\) that computes a fibre and a \(C\) containing edits to the observed value. An obstruction question has a \(\mathcal Q\) that returns reachable or unreachable.

**D3.3 Respects** **[I72]**. v ⇝ w (v upstream of w) when there are components j1, …, jn with v ∈ V_j1, Out(u_i, j_i), u_i ∈ V_j(i+1) for i < n, and u_n = w. Prod(p) :⟺ Q = Q_w with Out(w, j) for some j, and C holds a setting edit of some v ⇝ w. Ident(p) :⟺ Q returns a fibre g⁻¹(y) (E2) and C holds edits to the observed value. Obst(p) :⟺ Y_p = {reachable, unreachable}. Rule-status: Rule_C (D4.6); purpose-achievement: (AR) (D14.8). These are sufficient conditions; they need not exclude one another (FC36).

> L155 | A claim that an episode *found* a question requires \(\rho_p=\text{constructed}\) for the contract in question, with the trace.

**D3.4 Provenance of a contract.** ρ_p ∈ {declared, selected, constructed}, with a trace; selected and constructed as for transports (D12.1, D12.2), with the contract as the content (E8); declared := neither. Found(p) requires ρ_p = constructed.

> L159 | Where the claim states why it restricts the contract as it does, an assessment of the restriction is given with that statement; where it states none and an assessment turns on one, that statement is a missing declared input (Part XIV).

**D3.5 Scope statement.** Σ is a declared input naming Excl(Σ) ⊆ A × B **[I27]**; Stated(C, Σ) :⟺ (A × B) ∖ C ⊆ Excl(Σ). Why the question is asked on C and not on a wider contract is a further declared input; no condition below uses it.

> L161 | A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.

> L161 | An assessment is an event with a frozen contract (Part 0, grievance 10): a change to \(C\) or \(\mathcal Q\) during it, left unrecorded, makes the record name a claim other than the one assessed.

> L367 | A proposition indexed to a contract remains that proposition when a later theory changes the current contract. A new index is a new claim.

**D3.6 Defects; indexing** **[I76]**. With a description Desc that p answers to: BadTarget :⟺ the organizations meeting Desc are not exactly one; BadBaseline :⟺ Sol_D(1,b0) = ∅ or b0 ∉ B; BadReq :⟺ the conditions Desc puts on (C, Q) have no joint instance. Every claim about a question is indexed by (D, C, b0, Q, δ_D); a claim with another index is another claim.

> L151 | Two questions with the same \(D\) and different \((C,\mathcal Q)\) are different questions, and an answer to one is not an answer to the other.

**D3.7 Different questions.** p ≠ p' when (C, Q) ≠ (C', Q') on the same D. 'An answer to one is not an answer to the other' is read narrowly: Acc on p does not by itself give Acc on p' **[I73]**; the wide reading (no candidate meets (E) on both) is a claim to test (FC34).

**Vague.** L141 makes Q an operation 'on D'; (A) at L250 applies it to E, whose ports are not D's. How the one query reads another organization is not said [I20]. 'Determined' (L255) presupposes answers that can fail to be determined; Q's codomain Y_p has no such value [I21].

## §4 Signatures, kinds and families

> L116 | \operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K}

**D4.1 Signature (K).** sig_C(j) := {(a, b, L_j(a,b)) : (a,b) ∈ C}; equivalently, the function on C sending (a,b) to L_j(a,b).

> L119 | Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide. A kind is an equivalence class of components under this relation.

**D4.2 One kind on C.** j ~_C j' :⟺ there is a bijection β: V_j → V_j' with X_v = X_β(v) for every v, and L_j'(a,b) = β_*(L_j(a,b)) for every (a,b) ∈ C, where β_*(R) := {w∘β⁻¹ : w ∈ R} **[I10]**. Kinds on C are the classes of ~_C. C' is coarser than C when C' ⊆ C, finer when C' ⊇ C **[I11]**.

> L119 | A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection

**D4.3 Reading through a transport.** For k ∈ J_E and a transport t = (π,τ,σ,λ): sig^t_C(k) := the function on C sending (a,b) to L^E_k(τ(a),σ(b)) **[I12]**; τ[C] := {(τ(a),σ(b)) : (a,b) ∈ C}. For candidates ℰ, ℰ' of one question, k ∈ J_E and k' ∈ J_E' are of one kind on C when sig^t_C(k) and sig^{t'}_C(k') coincide under a footprint bijection (as in D4.2).

> L119 | Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.

**D4.4 Signature of a counterpart.** For k ∈ Γ with λ(k) = (N_k, θ_k, κ_k) (D5.1): sig_C(λ(k)) := the function on C sending (a,b) to proj^λ_{V_k} Sol_{N_k}(a,b) (D5.2). This extends (K) from components to subnetworks **[I13]**.

**D4.5 Change and invariance on a contract.** For a set 𝒳 of edits: Changes_C(j, 𝒳) :⟺ some (a,b) ∈ C with a ∈ 𝒳 has L_j(a,b) ≠ L_j(1,b); Inv_C(j, 𝒳) :⟺ every (a,b) ∈ C with a ∈ 𝒳 has L_j(a,b) = L_j(1,b) **[I09]**. 'Variable under' is Changes; invariance holds vacuously when C holds no edit of 𝒳.

> L123 | - a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;

> L124 | - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

> L125 | - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

> L347 | Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\).

**D4.6 Families.** For a component j, o_j is the port j assigns (asg(o_j) = j) **[I04]**. Alt_j := {a ∈ A : L_j(a,b) ≠ L_j(1,b) for some b}.
- Causal_C(j) :⟺ Changes_C(j, Set_{o_j}) ∧ Inv_C(j, Obs). (L123 as it stands after round 1.)
- Meas_C(j, m) :⟺ m ∈ V_j, asg(m) ≠ j, Inv_C(j, Set_m) ∧ Changes_C(j, MR_j), with MR_j := Alt_j under R-i and Alt_j ∖ Set_{o_j} under R-ii **[I06, I07]**.
- Rule_C(j) :⟺ Inv_C(j, World_j) ∧ Changes_C(j, Alt_j ∖ Set_{o_j}), with World_j := ∪ {Set_v : asg(v) ≠ j} **[I08]**.
- A constitutive status is Rule_C (L347; FC09).

> L127 | These are descriptions of patterns in (K), not additional data.

Each family predicate is a function of D and C alone (FC13).

**Vague.** 'Observation edits' (L123) and 'the measured port' (L124) rest on L109's observation, which has two readings (D2.4). 'The world' and 'the rule' (L125) are not fixed [I08]. L127's gloss of a measurement's signature ('change the part and the reading follows') is a condition on solutions, which (K) does not record (FC08). L121 names four things and the bullets give three families (FC09).

## §5 Transports and fidelity

> L186 | t=(\pi,\tau,\sigma,\lambda)

> L189 | where \(\pi:X_D\to X_E\) on the stated scope, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\) with a port translation.

**D5.1 Transport.** t = (π, τ, σ, λ) from D to E: π: X_D ⇀ X_E, defined at least on Sol_D(a,b) at every pair t translates **[I16]**; τ: A_D ⇀ A_E and σ: B_D ⇀ B_E **[I17]**; λ assigns each k ∈ J_E a triple (N_k, θ_k, κ_k): N_k ⊆ J_D a subnetwork, θ_k: V_k → V_{N_k} injective, and value maps κ_{k,v}: X^D_{θ_k(v)} → X^E_v (the identity where the domains agree) **[I14]**. t translates (a,b) :⟺ a ∈ dom τ, b ∈ dom σ, and π is defined on Sol_D(a,b).

> L233 | the relation obtained by imposing the constraints of \(\lambda(k)\), projecting away its hidden ports and carrying what remains to \(V_k\) by the port translation of \(\lambda\)

**D5.2 Projection.** For S ⊆ ∏_{v∈V_{N_k}} X_v: proj^λ_{V_k}(S) := {(κ_{k,v}(z_{θ_k(v)}))_{v∈V_k} : z ∈ S}. The hidden ports are V_{N_k} ∖ θ_k[V_k] **[I14]**.

> L231 | An explanatory candidate for question \(p\) is an organization \(E\), a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), and an identified set \(\Gamma\) of active commitments in \(E\). The commitments \(\Gamma\) are components of \(E\), those the candidate offers as doing the work, whether or not anyone has described their work; the boundary conditions of \(E\) and the components of \(E\) outside \(\Gamma\), including any of them that assigns an input, belong to the named background of Part VI.

**D5.3 Candidate.** ℰ = (E, p, t, Γ, δ_E): E an organization, t a transport from p's target to E, Γ ⊆ J_E the commitments, which are the active components **[I15]**, δ_E the designation of Q in E **[I20]**. The background is J_E ∖ Γ with B_E.

> L236 | \operatorname{proj}^{\lambda}_{V_k}\!\big[\operatorname{Sol}_{\lambda(k)}(a,b)\big]=L_k(\tau(a),\sigma(b)). \tag{F1}

**D5.4 (F1).** F1_C(ℰ) :⟺ for every k ∈ Γ and every (a,b) ∈ C: proj^λ_{V_k}[Sol_{N_k}(a,b)] = L^E_k(τ(a),σ(b)).

> L242 | \pi[\operatorname{Sol}_D(a,b)]=\operatorname{Sol}_E(\tau(a),\sigma(b)),\qquad \tau(1)=1,\quad \tau(a_2a_1)=\tau(a_2)\tau(a_1). \tag{F2}

**D5.5 (F2).** F2eq_C(ℰ) :⟺ for every (a,b) ∈ C: π[Sol_D(a,b)] = Sol_E(τ(a),σ(b)). Hom(τ) :⟺ τ(1) = 1, and for all a1, a2 ∈ dom τ with a2·a1 defined, τ(a2)·τ(a1) is defined and equals τ(a2·a1) **[I18]**. F2_C := F2eq_C ∧ Hom(τ).

> L250 | \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A}

**D5.6 (A).** A_C(ℰ) :⟺ for every (a,b) ∈ C: Ans_E(τ(a),σ(b)) = Ans_p(a,b), with ⊥ = ⊥ **[I21]**.

> L189 | A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V.

> L245 | Together they are fidelity at every level the contract reaches.

> L247 | **Question fidelity.**

**D5.7 Faithful; two extents.** Faithful_C(t) := F1_C ∧ F2_C (the narrow extent, as L189 defines it) **[I49]**. Fid⁺_C := F1_C ∧ F2_C ∧ A_C (the wide extent, where a line counts (A) as fidelity: L247's heading, L520). At a pair (a,b): F1 and F2eq at that pair alone; Hom is a condition on τ as a whole, never at a pair **[I18]**.

**Vague.** One word, two extents: L189 and L245 give the narrow one; L247's heading and L520 (after round 1) the wide one; L630 keeps 'the fidelity and the answers' apart (FC104). The domain of π ('on the stated scope') and which pairs a transport 'translates' (L315) are not fixed [I16, I17]. Port translations carry ports, and nothing in the text carries values between different domains [I14].

## §6 Non-circular dependence, non-vacuity, Account

**D6.1 Deletion in a candidate.** For G ⊆ Γ, E−G as in D1.3; Ans_{E−G}(y) := Q(E−G, y; δ_E).

> L255 | **Non-circular dependence.** The answer follows by evaluating \(E\) under its independent boundary conditions.

**D6.2 NC0.** Holds of every candidate: every answer is computed by evaluating E at (τ(a),σ(b)), and σ(b) depends on b alone **[I23]**.

> L255 | The target's answer does not appear, at the declared grain, as an unanalysed boundary input or as a component; moving an assertion from an input slot into a component named "law" does not discharge this. Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements.

**D6.3 NC1 (no answer slot).** Slot_C(ℰ, k) :⟺ δ_E's answer ports lie in V_k, and for every (a,b) ∈ C, L^E_k(τ(a),σ(b)) = {w ∈ ∏_{V_k} X : w on the answer ports = Ans_p(a,b)} (and constrains nothing else); likewise for a boundary coordinate of E whose value at σ(b) is Ans_p(a,b). NC1(ℰ) :⟺ no k ∈ J_E and no boundary coordinate is a slot, in E as given at grain ℓ **[I24, I28]**.

> L255 | There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that the answer of \(E\) at \((\tau(a),\sigma(b))\) differs from its answer at \((1,\sigma(b_0))\), or is not determined at \((\tau(a),\sigma(b))\) in the claimed way, and this contrast is lost when the components of \(G\) are deleted from \(E\)

> L255 | evaluated at \((\tau(a),\sigma(b))\) and at \((1,\sigma(b_0))\), the answers of \(E\) with \(G\) deleted are determined and equal, or an answer that \(E\) determines at one of these points is not determined there once \(G\) is deleted.

**D6.4 NC2 (a contrast lost under deletion).** With x = (τ(a),σ(b)) and x0 = (1,σ(b0)):
- Contrast(E; x) :⟺ [Ans_E(x) ≠ ⊥ ∧ Ans_E(x0) ≠ ⊥ ∧ Ans_E(x) ≠ Ans_E(x0)] ∨ [Ans_E(x) = ⊥ ∧ Ans_E(x0) ≠ ⊥] **[I21, I22]**;
- Lost(E, G; x) :⟺ [Ans_{E−G}(x) ≠ ⊥ ∧ Ans_{E−G}(x0) ≠ ⊥ ∧ Ans_{E−G}(x) = Ans_{E−G}(x0)] ∨ [for some y ∈ {x, x0}: Ans_E(y) ≠ ⊥ ∧ Ans_{E−G}(y) = ⊥];
- NC2(ℰ) :⟺ there are (a,b) ∈ C and G ⊆ Γ, G ≠ ∅, with Contrast(E; x) ∧ Lost(E, G; x).

**D6.5 Non-circular dependence.** NonCircular(ℰ) :⟺ NC0 ∧ NC1 ∧ NC2 **[I25]**.

> L257 | **Non-vacuity.** \(\operatorname{Sol}_D(1,b_0)\neq\varnothing\). The contract \(C\) is a stated subset of the edits the target admits, and every edit the target admits that is excluded from \(C\) is excluded by a stated scope, not silently.

**D6.6 Non-vacuity.** NonVacuous(ℰ) :⟺ Sol_D(1,b0) ≠ ∅ ∧ Stated(C, Σ) (D3.5) **[I27]**.

> L262 | \operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}. \tag{E}

**D6.7 Account (E).** Acc(ℰ) :⟺ F1_C ∧ F2_C ∧ A_C ∧ NonCircular ∧ NonVacuous. Its arguments are (D, C, b0, Q, δ_D, E, t, Γ, δ_E, Σ, ℓ): no assessor, no history, no provenance (FC30).

> L231 | meets \(\operatorname{Account}(\mathcal E)\) exactly when the following four conditions are met

**D6.8 The four conditions.** The four headings of Part V: Component fidelity = F1 ∧ F2 (L233–L243), Question fidelity = A (L247), Non-circular dependence (L255), Non-vacuity (L257). (E) writes them as five conjuncts (FC31).

> L257 | A contract consisting only of relabelings, or excluding every change under which the active commitments could matter to \(\mathcal Q\), admits no candidate that meets non-circular dependence

**D6.9 Relabeling.** a is a relabeling for p when, at every b with (a,b) ∈ C, Ans_p(a,b) = Ans_p(1,b0) ≠ ⊥ **[I26]** (FC21).

> L269 | A **table of observed answers** has no component whose relation is replaced by an intervention; it fails (F1) under any contract containing one.

**D6.10 Tables.** E_tab: one active component k with λ(k) = (J_D, θ, κ) (the whole target, projected on k's ports) and L_k(a',b') := proj^λ_{V_k} Sol_D(1,b0) at every (a',b'); E_enc: the same with L_k(τ(a),σ(b)) := proj^λ_{V_k} Sol_D(a,b) **[I32]** (FC25).

**Vague.** NC1's 'unanalysed', 'at the declared grain' and 'structural' have no definition in (O) or (Q) [I24, I28], and NC2, the one fully formal clause, does not exclude a lookup of the answer (FC23): the exclusion of 'p because p' rests on the least defined sentence. 'In the claimed way' is not fixed [I22]. NC0 adds no condition as read [I23]. Non-vacuity's second sentence is a condition on a statement, not on relations under the changes in C (FC33).

## §7 Routes: (S), (B), (D)

> L287 | Fix \(\mathcal E\) and a declared restriction operation. For \(W\subseteq\Gamma\), let \(E|W\) retain the commitments in \(W\) with the named background fixed; the commitments of \(E|W\) are \(W\).

> L231 | for \(E|W\), \(t'\) is \(t\) with \(\lambda\) restricted to the components of \(E|W\), and \(\Gamma'\) is \(W\).

**D7.1 Restriction.** E|W := E − (Γ ∖ W), with t restricted to W and commitments W **[I29]**; Acc(E|W, p) := Acc((E|W, p, t|W, W, δ_E)).

> L290 | \mathsf S_{E,p}=\{W\subseteq\Gamma:\operatorname{Account}(E|W,p)\}. \tag{S}

> L293 | No upward closure and no minimal member are assumed. For nonempty \(B\subseteq W\),

**D7.2 Routes (S).** S_{E,p} := {W ⊆ Γ : Acc(E|W, p)}. A route is a member of S_{E,p}.

> L296 | \operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}. \tag{B}

**D7.3 Critical block (B).** CB(B; W) :⟺ ∅ ≠ B ⊆ W ∧ W ∈ S ∧ W ∖ B ∉ S.

> L302 | \operatorname{Boundary}_{E,p}=\{(v,w)\in\mathcal V^2:\operatorname{Account}(E_v,p)\neq\operatorname{Account}(E_w,p)\}. \tag{D}

**D7.4 Boundary (D).** For a declared family 𝒱 of organization edits: Boundary := {(v,w) ∈ 𝒱² : Acc(E_v, p) ≠ Acc(E_w, p)}, with E_v's transport and commitments those the edit carries t and Γ to (L231; the text does not fix them further).

> L305 | then \(d\in\Gamma\) is critical for some route (**contributory**) exactly when \(d\in\bigcup\min\mathsf S\), and \(d\) is **globally indispensable**, \(\Gamma\setminus\{d\}\notin\mathsf S_{E,p}\)

**D7.5 Contributory; globally indispensable.** Contrib(d) :⟺ CB({d}; W) for some W ∈ S. Indisp(d) :⟺ Γ ∖ {d} ∉ S.

> L313 | A commitment \(d\) of a candidate that has a route does no work by itself in it when every route stays a route after \(d\) is added to it and after \(d\) is removed from it

**D7.6 No work by itself.** NoWork(d) :⟺ S ≠ ∅ and, for every W ∈ S, W ∪ {d} ∈ S and W ∖ {d} ∈ S.

The worked examples of L307–L311 are read as set systems S ⊆ P(Γ) **[I30]**; the infinitary example's routes are the sets with unbounded index sets **[I31]**.

## §8 Conflict, rivals, conflict with a claim

> L315 | Two candidates **conflict** at such a pair \((a,b)\) when their answers there differ, or when each of them could meet (F1), (F2) and (A) there under some relations of the target's components at that pair, each a relation on the component's footprint (Part II), and no such relations let both

**D8.1 Meeting at a pair under hypothetical relations.** For a pair (a,b) and R = (R_j)_{j∈J_D} with R_j ⊆ ∏_{v∈V_j} X_v: D^R is D with L_j(a,b) replaced by R_j; Ans^R_p(a,b) := Q(D^R, a, b; δ_D). Meets_ab(ℰ, R) :⟺ for every k ∈ Γ, proj^λ_{V_k}[Sol^R_{N_k}(a,b)] = L^E_k(τ(a),σ(b)); π[Sol_{D^R}(a,b)] = Sol_E(τ(a),σ(b)); and Ans_E(τ(a),σ(b)) = Ans^R_p(a,b) **[I19]**. BothMeet_ab(R) :⟺ Meets_ab(ℰ,R) ∧ Meets_ab(ℰ',R).

**D8.2 Conflict.** For a pair (a,b) of the target that both transports translate, in C or outside it: Conf(ℰ, ℰ'; a,b) :⟺ Ans_E(τ(a),σ(b)) ≠ Ans_E'(τ'(a),σ'(b)) ∨ [∃R Meets_ab(ℰ,R) ∧ ∃R' Meets_ab(ℰ',R') ∧ ¬∃R'' BothMeet_ab(R'')].

> L315 | Whether two candidates conflict depends on their organizations and transports and on the target's ports and components, not on anyone's view of them; it is found by argument, with no test, and it does not turn on what any physics admits (Part I).

R ranges over every assignment of relations on the footprints; no physical module enters D8.1–D8.2.

> L315 | Two explanatory candidates for one question \(p\) are **rivals** when one of them has been offered as an answer to \(p\) in place of the other and they conflict at some admitted edit–boundary pair of the target that both their transports translate, in \(C\) or outside it.

> L315 | No list of all rivals is supposed: a candidate's rivals are among the candidates someone has offered, and a candidate that nobody has offered is no one's rival.

**D8.3 Offer; rivals.** Offered(ℰ, ℰ', p) is a primitive: a record that ℰ was offered for p in place of ℰ' **[I33]**. Riv(ℰ, ℰ'; p) :⟺ [Offered(ℰ,ℰ',p) ∨ Offered(ℰ',ℰ,p)] ∧ Conf(ℰ,ℰ'; a,b) for some pair both translate. Riv is a two-place relation; nothing here ranges over the rivals of a candidate.

> L315 | A candidate offered for \(p\) is offered for the whole of \(p\): it claims (F1), (F2) and (A) at every pair of \(C\), tested or not, and the rest of (E) on \(C\); outside \(C\) it claims nothing on \(p\)

A candidate offered for p is the claim Acc(ℰ) on p.

> L315 | \(\chi\) need not be an explanation or come with one, and it may be a claim about what is possible or impossible: the bare claim that perpetual motion is impossible is enough for a conflict with a candidate whose organization gives perpetual motion.

**D8.4 A claim at a pair.** A claim χ is given, at each pair, by Allow_χ(a,b), a set of assignments R of relations to the target's components (the behaviours χ allows), and by Applies(χ, a, b) ∈ {yes, no}, the premise that χ speaks of the target under that pair's edit **[I34]**. A claim about what is possible or impossible enters only through Allow_χ: here, and only here in §§1–10, physical possibility is content.

> L315 | A candidate **conflicts with** a claim \(\chi\) at an admitted pair of the target that its transport translates, in \(C\) or outside it, when \(\chi\) excludes what the candidate's organization and transport give there: its answer, or every relation of the target's components under which it could meet (F1), (F2) and (A) there.

**D8.5 Conflict with a claim.** ConfCl(ℰ, χ; a,b) :⟺ [every R with Ans^R_p(a,b) = Ans_E(τ(a),σ(b)) lies outside Allow_χ(a,b)] ∨ [every R with Meets_ab(ℰ,R) lies outside Allow_χ(a,b)].

> L315 | Two candidates that some relations of the target's components would let both meet (F1), (F2) and (A) at a pair, when \(\chi\) excludes every such relation, conflict there given \(\chi\)

**D8.6 Conflict given χ; rivals given χ.** ConfG_χ(ℰ, ℰ'; a,b) :⟺ some R has BothMeet_ab(R), and every such R lies outside Allow_χ(a,b) **[I35]**. Riv_χ(ℰ, ℰ'; p) :⟺ one offered in place of the other ∧ ConfG_χ at some pair.

**Vague.** 'One counterpart' is not fixed [I36]. What a claim is, and how it 'excludes', are not given beyond the example [I34]. 'Offered' has no definition and is not a declared input [I33].

## §9 Arguments, usability, ruling out, bearing, reason use

> L397 | **Arguments.** A record leaf is a reference to an event with an interpreted claim. An argument is an argument tree: argument steps whose leaves are premises, which are record leaves or stated assumptions and definitions.

**D9.1 Claims.** Claims are sentences of a first-order language with ¬ and ∧; Incons(φ, ψ) is classical inconsistency of {φ, ψ} **[I38]**. The claims used here include 'Acc(ℰ)', 'Ans_p(a,b) = y', records of a test, and conditionals.

**D9.2 Argument.** A finite tree α. Each internal node is a step u with an inference form Form(u) and a conclusion concl(u); its children are its premises. Leaves are record leaves (each referring to an event, D11.1, with an interpreted claim) or stated assumptions and definitions. MadeFrom(leaf, ψ) is a primitive: the record leaf was made from the claim ψ **[I39]**.

> L387 | **Usability.** For argument step \(u\) with essential premises \(\operatorname{Prem}(u)\), the premises its inference form uses:

> L393 | \(\operatorname{Form}_j(u)\): the inference form of \(u\) is one \(j\) admits. \(\operatorname{Scope}_j(u)\): \(u\) is applied within the contract, grain and boundary \(j\) has declared for it; \(\operatorname{Live}_j(d;u)\): \(d\) is the conclusion of a step of the same argument as \(u\) that is usable by \(j\), or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it, whether or not \(j\) holds an explanation of \(d\); a claim \(j\) has never taken up is not live for \(j\).

**D9.3 Essential premises.** Prem(u) ⊆ children(u): the premises Form(u) uses **[I40]**.

**D9.4 Live.** Accepted_j(ξ) is the set of claims j has taken up before ξ and not withdrawn before ξ (a declared input) **[I41]**. Live_j(d; u) :⟺ [d = concl(u') for a step u' in the subtree below u with Usable_j(u')] **[I40]** ∨ d ∈ Accepted_j(ξ).

**D9.5 Form and scope.** Form_j(u) :⟺ Form(u) ∈ Forms_j (declared). Scope_j(u) :⟺ C_u ⊆ C_j(u), ℓ_u = ℓ_j(u), β_u = β_j(u), where (C_u, ℓ_u, β_u) is the index u is applied at and (C_j(u), ℓ_j(u), β_j(u)) what j has declared for it **[I42]**.

> L390 | \operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u). \tag{K2}

**D9.6 Usability (K2).** Usable_j(u) :⟺ Form_j(u) ∧ Scope_j(u) ∧ ∀d ∈ Prem(u) Live_j(d; u), defined by recursion on the height of u, which D9.4 makes well founded **[I40]**. Usable_j(α) :⟺ every step of α is usable by j.

> L397 | Each step of an argument rules out the case in which the step's premises are met and its conclusion fails, for someone who admits its inference form (\(\operatorname{Form}_j\)), while that form stays admitted. An argument is usable by \(j\) when each of its steps is (K2), and it rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises (below). For \(\psi\), \(X_j(\psi)\) is the set of arguments usable by \(j\) that rule out \(\psi\).

> L397 | An argument does not rule out a claim when the claim's denial is among its premises, alone or joined to other claims by "and", read structurally as non-circular dependence reads identity (Part V) and not by logical equivalence alone; nor does an argument whose record leaf was made from a claim rule out that claim's denial.

**D9.7 Rules out.** A step u, for j with Form_j(u), rules out the case Prem(u) ∧ ¬concl(u); forms need not be classically sound **[I38]**. RO(α, φ) :⟺ Incons(φ, concl(root of α)); no leaf of α has ¬φ as a conjunct (flattened, up to renaming and the order of conjuncts) **[I39]**; and no record leaf of α is made from a claim whose denial is φ.

> L315 | A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out, and a candidate is ruled out for \(j\) when the claim that it meets (E) is;

> L315 | A candidate is **not ruled out** for \(j\) when no argument usable by \(j\) rules it out.

**D9.8 Ruled out; not ruled out.** X_j(φ) := {α : Usable_j(α) ∧ RO(α, φ)}. Out_j(φ) :⟺ X_j(φ) ≠ ∅; NotOut_j(φ) :⟺ X_j(φ) = ∅. A candidate ℰ is ruled out for j :⟺ Out_j('Acc(ℰ)').

> L397 | Where such an argument uses a claim taken as given, the ruling out is a choice the person using it made, not something the claim does by itself (Part 0).

Formally: Out_j depends on Accepted_j and Forms_j, which are declared inputs that no definition sets (FC56). The choice shows as the input; nothing here makes it.

> L395 | **What a test rules out.** For \(T\land B\land I\Rightarrow O\), an argument usable by \(j\) that rules out \(O\) rules out \(T\land B\land I\) together for \(j\), and nothing narrower. (K3)

**D9.9 (K3).** **[I43]** (i) If α ∈ X_j(O), the conditional T∧B∧I ⇒ O is live for j and j admits modus tollens, then α extended by one step is in X_j(T∧B∧I). (ii) From those premises alone, X_j(T), X_j(B) and X_j(I) gain no member (¬O, T∧B∧I ⇒ O and T have a common model).

> L377 | **Bearing.** A criticism has target \(z\), alleged defect \(\delta\), premise \(g\), and a connection. Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\), and \(\mathcal E_c\) the explanatory candidate (Part V) for \(p_\delta\) whose organization is the criticism's connection from \(g\) to \(\delta\), with its transport and its identified commitments. Then

> L380 | \operatorname{Bearing}(c,z,p)\iff\operatorname{Account}(\mathcal E_c). \tag{K1}

**D9.10 Criticism and bearing (K1).** A criticism c = (z, δ, g, Conn, occ): a target, an alleged defect, a premise, a connection (an organization from g to δ) and an occurrence in a history. p_δ, the question whether z has δ in respect of p, is supplied with c **[I76]**; ℰ_c := (Conn, p_δ, t_c, Γ_c, δ_c). Bearing(c, z, p) :⟺ Acc(ℰ_c).

> L383 | An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target.

A criticism's premise g is represented (D12.5) by an organization of the system.

> L385 | **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.

**D9.11 Reason use** **[I47]**. The represented objection ob is a content with role bindings (a map from role names to its ports); R is the response suborganization; Rec and Chg are declared sets of content-preserving recodings and content changes of ob; Rule: Chg → changes of R is declared. UsesReason(R, ob) :⟺ there is a map m from ob's ports to R's ports preserving role names, with trans(m(ρ·ob)) = trans(m(ob)) for every ρ ∈ Rec, m(γ·ob) = Rule(γ)(m(ob)) for every γ ∈ Chg, and some image port of m on an active route (D11.4). No clause uses Acc or Usable (FC76).

**Vague.** 'Structural map', 'role bindings', 'the same transition' and 'operative deliberative rule' (L385) are defined nowhere [I47]. 'Among its premises … read structurally' is given by pointing at NC1, which is itself not defined [I39, I24]. Whether the step making a premise live lies below the step (L393) is not said; with any step of the argument, (K2) can have two fixed points (FC69) [I40].

## §10 Problems and easy to vary

> L317 | **Problems.** Two rivals, neither of them ruled out for an assessor, pose, for that assessor, a **problem for \(p\)**: a conflict between ideas that no argument usable by that assessor has decided.

**D10.1 Problem.** Prob_j(ℰ, ℰ'; p) :⟺ Riv(ℰ, ℰ'; p) ∧ NotOut_j('Acc(ℰ)') ∧ NotOut_j('Acc(ℰ')').

> L317 | (i) The rivals conflict at some \((a,b)\in C\).

> L317 | (ii) They conflict at no pair of \(C\), only at admitted pairs outside it: the contract does not contain their conflict.

**D10.2 The two kinds.** Kind i :⟺ Conf at some (a,b) ∈ C. Kind ii :⟺ Conf at no pair of C, and at some pair outside C that both translate.

> L317 | recording it, the target's relations as well as its answer where their answers there agree, is a **test**.

**D10.3 Test.** A record at (a,b) ∈ C: the recorded relations R* of the target's components there and the recorded answer, with its premises about background and instruments (K3). The argument from it: 'R* at (a,b); Meets_ab(ℰ, R*) fails; Acc(ℰ) requires it'.

> L317 | A candidate is **easy to vary**, in the sense used here, when it and a rival pose a problem of the second kind;

**D10.4 Easy to vary.** ETV_j(ℰ; p) :⟺ Prob_j(ℰ, ℰ'; p) of kind ii for some ℰ' **[I37]**. This is the text's 'easy to vary' only; what hard to vary covers is parked (S33–S34), and nothing here extends to it.

> L315 | for an assessor who tentatively accepts \(\chi\) they pose a problem for \(p\) as rivals do (Problems, below), and for one who does not, they pose none on that account.

**D10.5 Problem given χ.** Prob_{χ,j}(ℰ, ℰ'; p) :⟺ Riv_χ(ℰ, ℰ'; p) ∧ χ ∈ Accepted_j(ξ) ∧ neither is ruled out for j.

> L317 | Solving a problem so rules one rival out for that assessor while the argument stays usable for that assessor.

**D10.6 Solved.** A problem for j is solved while Out_j('Acc(ℰ)') or Out_j('Acc(ℰ')') holds. Where the argument uses a claim taken as given, that is j's choice (D9.8).

## §11 Occurrences, events, contents, histories, active routes

> L169 | An **occurrence** is a physically located carrier. A **content** is an organization together with its contract-relative commitments. Occurrences are not identified by carrying the same words; contents are not identified by having the same outputs.

**D11.1 Occurrence; event.** Occ is a set of physically located carriers, interpreted by Θ. An event is a nonempty set of occurrences of a history **[I45]** (the text uses 'event' at L53, L55, L161, L397, L604 and L612 and defines it nowhere; FC105).

**D11.2 Content.** c = (E_c, C_c, Γ_c): an organization, a contract on it, and its commitments **[I48]**. Contents are compared by transports (D13.4), not by outputs.

> L375 | **Histories.** A history \(h\) is a set of occurrences with an acyclic causal precedence \(\prec_h\) (write \(\preceq_h\) for its reflexive closure) and a physical interpretation supplying process occurrences, their ports, and the connections actually instantiated.

**D11.3 History.** h = (O_h, ≺_h, I_h): O_h ⊆ Occ; ≺_h a strict partial order **[I44]**; I_h, supplied by Θ, gives process occurrences, their ports and the connections instantiated. Org_ℓ(h) is the organization Θ gives h at grain ℓ. A subhistory is a subset closed under the interpretation, with ≺ restricted.

> L375 | An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.

**D11.4 Active route** **[I46]**. For a result occurrence r: ActRoute_h(R; i, r, K) :⟺ R ⊆ O_h is connected by instantiated connections; i ∈ R is an input occurrence whose port carries a represented distinction; r ∈ R; every occurrence of R lies on a ≺_h-chain from i to r inside R; each occurrence of R meets the relation Org_ℓ(h) gives it; and for some pair (x, x') in the declared contrast set K of values of i's port, setting i's port to x and to x' in Org_ℓ(h) gives different values at r.

> L217 | For an edit–boundary pair \((a,b)\in C\) actually occurring:

**D11.5 Occurring pairs.** Occurs(a, b, ξ) is a primitive read through Θ: the pair occurs at ξ in the system's history.

**Vague.** 'Represented input', 'operative result', 'applicable relations' and 'the declared contrasts' (L375) are defined nowhere [I46]; whether a route that ran to completion and whose product persists is 'already at rest when the result occurred' is not fixed (FC75). 'Event' is used and not defined [I45]. 'c's contract' presupposes contents with contracts of their own [I48].

## §12 Provenance, representation, prediction

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

> L195 | **Selected.** There is a population \(\mathcal T\) of candidate transports, a variation operator \(\mu\) on \(\mathcal T\), a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered, and a survival condition requiring fidelity on \(H\).

> L195 | A transport **survives on \(H\)** when it is a member of \(\mathcal T\) that meets the survival condition on \(H\); fidelity on \(H\) without membership in \(\mathcal T\) is not survival. No member of the history represents \(t\), \(H\), or the survival condition.

**D12.1 Selected.** Sel(t; 𝒯, μ, H) :⟺ t ∈ 𝒯; μ: 𝒯 → P(𝒯); H ⊆ C finite, its pairs having occurred (D11.5); Faithful_H(t) (D5.7), i.e. t survives on H; and there is a physical selection history h_sel in which the pairs of H occur, the members of 𝒯 are admitted by the physics (D15.8), and no occurrence represents (D12.5) t, H or the survival condition **[I52]**.

> L197 | **Constructed.** There is an episode (Part X) whose construction trace prepares \(t\), and in which \(t\), or the organization it carries to, is available as a represented target. Write \(\operatorname{Con}(t;h,e)\).

**D12.2 Constructed.** Con(t; h, e) :⟺ some episode of h up to e (D13.8) has a construction trace (D13.3) that prepares t, and t or its codomain is a represented target in it.

> L199 | **Declared.** Neither of the above. The transport is entered into the model by its author. Write \(\operatorname{Dec}(t)\).

**D12.3 Declared.** Dec(t) :⟺ no parameters give Sel(t; ·) and none give Con(t; ·). Sel and Con are read on the whole history of t **[I53]**.

> L211 | A carrier keeps its provenance when present access to it is lost, and a later record made from the carrier carries that provenance, not a second, independent one.

> L405 | A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance.

**D12.4 Provenance per part; inherited provenance.** prov assigns Sel, Con or Dec to each part of a transport (each component with its counterpart binding). A content-preserving transfer (relay or record) from carrier o to o' gives each part at o' the value it had at o; a binding newly built gets Con. 'Inherited' is this rule, not a fourth value **[I54]**.

> L205 | An occurrence \(o\) **represents** content \(c\) at grain \(\ell\) when there is a transport from the organization that \(o\) instantiates under the physical module, at grain \(\ell\), to \(c\), faithful on \(c\)'s contract, whose provenance is selected or constructed;

> L208 | \operatorname{Rep}_\ell(o,c)\iff\exists t\,[\operatorname{Faithful}_C(t:\operatorname{Org}_\ell(o)\to c)\land(\operatorname{Sel}(t)\lor\operatorname{Con}(t))]. \tag{R}

**D12.5 Representation (R).** Rep_ℓ(o, c) :⟺ there is t: Org_ℓ(o) → E_c, faithful (D5.7) on the preimage {(a,b) : (τ(a),σ(b)) ∈ C_c} with Γ_c as its active components **[I48]**, and some parameters give Sel(t; ·) or Con(t; ·). Org_ℓ is the one thing (R) takes from Θ (L213).

> L175 | The **object layer** \(P\) is an organization whose ports are persistent things with boundaries and identity, whose components are their continuity relations, and whose admitted edits include displacement, occlusion and re-identification.

> L177 | The **simulation layer** \(S\) is an organization over \(P\) whose components are dependencies among things and whose queries are predictions: what a port of \(P\) will take under an admitted edit.

**D12.6 Layers.** P and S are organizations typed as L175 and L177 say; nothing assumes either exists in a given system (L179).

> L219 | - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);

> L220 | - a **violation** occurs when fidelity fails at \((a,b)\);

> L221 | - **surprise** is a violation of a selected transport at \((a,b)\notin H\).

**D12.7 Prediction, violation, surprise.** For t from P to S with contract C and, if selected, history H, at (a,b) ∈ C with Occurs(a,b,ξ): Pred_t(a,b) := Ans_S(τ(a),σ(b)); Viol(t; a,b) :⟺ ¬(F1 at (a,b) ∧ F2eq at (a,b)), and Viol⁺ adds (A) at (a,b) **[I50]**; Surp(t; a,b) :⟺ Sel(t; 𝒯, μ, H) for some 𝒯, μ, H with (a,b) ∉ H, and Viol(t; a,b). Pred is extended to any transport, Pred_t(a,b) := Ans_E(τ(a),σ(b)), where a line uses it so (L151) **[I51]**.

> L225 | A **selection response** extends the history \(H\) of a selected transport and lets \(\mu\) act: the transport is re-tuned within the population. A **construction response** introduces a new organization or a new transport with a construction trace.

**D12.8 Responses.** SelResp(t → t'; a,b) :⟺ Sel(t; 𝒯, μ, H), t' ∈ μ*(t) ⊆ 𝒯 and t' survives on H ∪ {(a,b)}. ConResp(→ t'') :⟺ t'' or its codomain is new (D13.5) and Con(t''; h, e).

> L572 | For every \((a,b)\in C\setminus H\) at which some \(t'\in\mathcal T\), also surviving on \(H\), has a different value from \(t\), the value of \(t\) at \((a,b)\) is underdetermined by \(H\)

**D12.9 Value at a pair; underdetermination.** value_t(a,b) := (τ(a), σ(b), (L^E_k(τ(a),σ(b)))_{k∈J_E}); members of 𝒯 share the codomain's ports and components **[I71]**. Underdet(t; a,b; 𝒯, H) :⟺ some t' ∈ 𝒯 surviving on H has value_t'(a,b) ≠ value_t(a,b) (FC80).

**Vague.** 'No member of the history represents' (L195) is said of a set of pairs, which cannot represent; the reading as occurrences of a physical history is invented, and without it Sel is met by every transport (FC77) [I52]. 'Exactly one of three' needs Sel and Con read on one history [I53]. 'Inherited provenance' (L405, L409) is used and not defined [I54].

## §13 Deploy, Build, New, Origin, ownership, episodes

> L403 | \(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi;U)\) is met when \(s\) at \(\xi\) holds a representation of \(c\), by (R) a faithful transport with selected or constructed provenance, integrated into problem-directed activity and serving the declared use task \(U\) as a retained capability (Part XII). The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect.

**D13.1 Deploy.** Deploy_{β,ℓ}(s, c, ξ; U) :⟺ some occurrence o of s at ξ has Rep_ℓ(o, c), Integrated(o, s, ξ), and Can_{Ω,β}(ξ, U; χ) holds for some χ with a realization that uses o **[I55]**.

**D13.2 Repertoire.** R_{β,ℓ}(s, ξ) := {c : Deploy_{β,ℓ}(s, c, ξ; U) for some U with Nontrivial(U)} **[I55]**; R_{<e}(s,h) := ∪_{ξ before e} R_{β,ℓ}(s, ξ) (L415).

> L405 | **Construction.** \(\operatorname{Build}_{\beta,\ell}(s,c,h,e)\) is met when an actual subhistory owned by \(s\) and delimited at \(e\) prepares a represented organization for explanatory use of \(c\), contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers.

**D13.3 Build; construction trace.** Build_{β,ℓ}(s, c, h, e) :⟺ some subhistory h' of h ending at e with Owned_β(h', s) (D13.7) has Prepares(h', c), BindingConstruction(h', c) and ¬TransferComposite(h') **[I56]**. A construction trace is (h', the controlled processes, the incoming carriers, the bindings constructed, the resulting representation) (L405). A binding may be identified by its use: by responses meeting D9.11's clauses (L409).

> L413 | **Newness.** Write \(d\equiv_\ell c\) when there are transports from \(d\) to \(c\) and from \(c\) to \(d\), both faithful on \(c\)'s contract at grain \(\ell\).

**D13.4 Matching.** d ≡_ℓ c :⟺ there are t: E_d → E_c faithful on the preimage of C_c, and t': E_c → E_d faithful on C_c, at grain ℓ **[I48]**. It is read with c fixed (L413) and is not claimed symmetric (FC85).

> L416 | \operatorname{New}(s,c,h,e)\iff\neg\exists d\in R_{<e}(s,h),\ d\equiv_\ell c. \tag{N}

**D13.5 New (N).** New(s, c, h, e) :⟺ no d ∈ R_{<e}(s, h) has d ≡_ℓ c.

> L422 | \operatorname{Origin}_{\beta,\ell}(s,c,p,h,e)\iff\operatorname{Attempt}(s,c,p,h,e)\land\operatorname{New}(s,c,h,e)\land\operatorname{Build}_{\beta,\ell}(s,c,h,e). \tag{G}

**D13.6 Attempt; Origin (G).** Attempt(s, c, p, h, e): c is used in h, up to e, to address p (L419; a claim read through Θ). Origin :⟺ Attempt ∧ New ∧ Build. c may be an organization, a transport or a contract (L425; E8).

> L427 | **Ownership.** The subhistory in Build is owned by \(s\) when its processes run inside the system boundary and resource contract declared for \(s\) (Part XII).

**D13.7 Ownership.** Owned_β(h', s) :⟺ every process of h' runs inside the boundary β and resource contract declared for s. Contribution of content is a separate attribution (L427): Contrib(h', w) records who supplied a content, and does not enter Owned.

> L429 | **Episodes.** A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response. A **recognized difficulty** is a failure of a claimed aim, or a conflict in which what the system holds meets a claimed aim only by failing a protected one (Part XI), when the system represents it. A creative critical episode contains an instance of (G) connected to its inquiry.

**D13.8 Episodes.** An episode is a subhistory. CompleteCritical(h') :⟺ h' contains a recognized difficulty (a represented failure of a claimed aim, or a represented conflict in which meeting a claimed aim fails a protected one), a target represented before its criticism, a criticism (D9.10) of it, and a response that uses the criticism as a reason (D9.11). CreativeCriticalEpisode(s, Δ, h, e) :⟺ a complete critical episode of h up to e that contains an instance of (G) 'connected to its inquiry' (read: the (G) instance's Attempt addresses the question the episode's difficulty poses; not fixed by the text).

**Vague.** 'Integrated into problem-directed activity', 'nontrivial use respect' (L403), 'prepares', 'nontrivial binding construction', 'content-preserving transfers' (L405) and 'connected to its inquiry' (L429) are defined nowhere [I55, I56]. 'Faithful on c's contract' for a transport into c needs c's contract on c's own organization [I48].

## §14 Repair, created explanation, appraisal

> L435 | **Repair.** The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes.

> L441 | The aims are declared inputs: \(O\) says what is to be repaired and \(P\) what is to be protected, each as a stated condition over stated occasions, and a protected condition is lost exactly when it fails on an occasion it covers. In (P), accordingly, \(r(\xi')\) says of a protected condition \(r\) that it was met on every occasion it covers from \(\xi\) to \(\xi'\), not only at \(\xi'\).

**D14.1 Aims.** An aim is (cond, Occ) with Occ a set of times (declared). For o ∈ O: o(ξ) :⟺ cond met at ξ. For r ∈ P, on the left of (P): r(ξ) :⟺ cond met at ξ if ξ ∈ Occ_r, and holds otherwise; on the right: r(ξ') :⟺ cond met at every ω ∈ Occ_r with ξ ≤ ω ≤ ξ' **[I57]**.

> L438 | \operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\iff\exists o\in O[\neg o(\xi)\land o(\xi')]\land\forall r\in P[r(\xi)\Rightarrow r(\xi')]\land\operatorname{ProducedBy}(\Delta,\xi,\xi';O). \tag{P}

**D14.2 Repair (P).** Repair_{O,P}(ξ, ξ'; Δ) :⟺ ∃o ∈ O [¬o(ξ) ∧ o(ξ')] ∧ ∀r ∈ P [r(ξ) ⇒ r(ξ')] ∧ ProducedBy(Δ, ξ, ξ'; O). Δ = (h_Δ, the content changes it makes).

> L441 | \(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair; it attributes the repair to each contribution whose active route ran to it in the history, and where two sufficient contributions both ran, the repair is attributed to both and the history supplies no division of the attribution that it does not contain.

**D14.3 ProducedBy.** ProducedBy(Δ, ξ, ξ'; O) :⟺ some o ∈ O with ¬o(ξ) ∧ o(ξ') has an active route (D11.4) from an occurrence of h_Δ to the occurrence at which o's condition comes to be met **[I57]**. Attr(o) := {Δ_i : ProducedBy(Δ_i, …) for o}; no share function is defined (a weighting is a declared input, L522).

> L441 | Losses outside \(P\) must be exposed.

**D14.4 Losses outside P.** A repair claim carries Aims* ⊇ O ∪ P and an exposure record X; WellFormed :⟺ {r ∈ Aims* ∖ P : r(ξ) ∧ ¬r(ξ')} ⊆ X **[I58]**.

> L443 | **Created explanation.** An explanatory aim requires a deployable account, or the correction of a use through one. With \(O_{\mathrm{ex}}\subseteq O\) the explanatory aims,

**D14.5 Explanatory aims.** O_ex ⊆ O, a declared marking; o ∈ O_ex when o's condition is that s possesses a deployable account of a stated question, or is L443's 'the correction of a use through' a deployable account **[I59]**.

> L453 | \(\operatorname{Result}(\Delta)\) is the set of contents at \(\xi'\) that \(\Delta\) prepared. \(\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')\) is met when an active route that runs from \(\Delta\) to the repair of \(o\) contains the relevant binding of \(c\).

**D14.6 Result; ProducesVia.** Result(Δ) := the contents at ξ' that h_Δ prepared (Prepares, D13.3). ProducesVia(Δ, c, o; ξ, ξ') :⟺ some active route from an occurrence of h_Δ to the occurrence at which o comes to be met contains an occurrence instantiating the binding named in c's construction trace **[I60]**.

> L447 | \operatorname{CreateEx}(s,\Delta,h,e)\iff{}&\operatorname{CreativeCriticalEpisode}(s,\Delta,h,e)\land\exists\xi,\xi'\,\bigl[\operatorname{Repair}_{O,P}(\xi,\xi';\Delta)\\

> L448 | &\land\exists o\in O_{\mathrm{ex}}\,\exists c,p_c,e_c,t_c,\Gamma_c\,[e_c\preceq_h e\land\neg o(\xi)\land o(\xi')\land\operatorname{Origin}_{\beta,\ell}(s,c,p_c,h,e_c)\\

> L449 | &\quad\land\operatorname{Account}\big((c,p_c,t_c,\Gamma_c)\big)\land c\in\operatorname{Result}(\Delta)\land\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)\land\operatorname{ProducesVia}(\Delta,c,o;\xi,\xi')]\bigr].

**D14.7 Created explanation (EX).** As displayed, with e_c ⪯_h e read in the partial order of D11.3 **[I44]**, and with Account((c, p_c, t_c, Γ_c)) evaluated on the contract of p_c fixed at e_c (L453): CreateEx(s, Δ, h, e) :⟺ CreativeCriticalEpisode(s, Δ, h, e) ∧ ∃ξ, ξ' [Repair_{O,P}(ξ, ξ'; Δ) ∧ ∃o ∈ O_ex ∃c, p_c, e_c, t_c, Γ_c (e_c ⪯_h e ∧ ¬o(ξ) ∧ o(ξ') ∧ Origin(s, c, p_c, h, e_c) ∧ Acc(c, p_c, t_c, Γ_c) ∧ c ∈ Result(Δ) ∧ Deploy(s, c, ξ'; U_c) ∧ ProducesVia(Δ, c, o; ξ, ξ'))].

> L455 | achievement \(\mathcal R[a,k]\neq\varnothing\land\mathcal R[a,k]\subseteq G[k]\) (AR); and \(\mathcal N\subseteq \mathit{Act}\times\mathit{Occ}\times\mathsf{Rsn}\times\mathcal V_A\) taken as a substantive input when aesthetic value is claimed

**D14.8 Appraisal, typed only.** 𝓡 ⊆ Act × Occ × Eff, G ⊆ Occ × Eff, (AR): 𝓡[a,k] ≠ ∅ ∧ 𝓡[a,k] ⊆ G[k]; 𝒩 ⊆ Act × Occ × Rsn × V_A, an input with Rsn and V_A unspecified. No definition of this file uses 𝒩; where values are placed is the owner's question.

**Vague.** Which aim ProducedBy's route runs to is not tied to (P)'s first conjunct [I57]. The universe of 'losses outside P' is not given [I58]. L443 names two kinds of explanatory aim; (EX) treats them alike and the second is carried only by ProducesVia (FC89) [I59]. 'The relevant binding' (L453) [I60].

## §15 The physical module

> L461 | **Tasks.** A substrate is a physical system; an attribute a set of its states; a task a specified input-to-output attribute transformation with explicit resources and side effects. Possibility is the absence of a law-imposed limit, short of exact, on the tolerance to which a task can be performed and retained; it is not one trajectory that performed the task.

**D15.1 Tasks.** A substrate has a state space Z_s; an attribute is a subset of Z_s; a task T is a relation between input and output attributes, with dom T and T[i], and with its resources and side effects stated **[I61]**. Here physical possibility enters as the carrying out of a transformation.

> L466 | \operatorname{RetReal}(\pi,T,C;\chi)\iff\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C. \tag{CT1}

> L469 | Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task.

**D15.2 Retained realization (CT1).** Exec(π, z, i; χ) is a set of executions, each with a completion flag, an output o and a final constructor state z'. RetReal(π, T, C; χ) :⟺ for every z ∈ C, i ∈ dom T and η ∈ Exec(π, z, i; χ): η completes with o ∈ T[i] and z' ∈ C. Standing assumption: Exec(π, z, i; χ) ≠ ∅ for z ∈ C and i ∈ dom T **[I61]**. (Here C is a constructor attribute and π a protocol: the letters of Part XII are local.)

> L471 | **Retention fixed point.** \(F(C)\) = states whose executions all complete and return into \(C\). \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)

**D15.3 Retention operator; (CT2).** F(X) := {z ∈ Z : for every i ∈ dom T and every η ∈ Exec(π, z, i; χ), η completes with o ∈ T[i] and z' ∈ X}, with 'complete' read as (CT1)'s completion **[I61]**. (CT2): F is monotone on P(Z); RetReal(π, T, C; χ) ⟺ C ⊆ F(C); gfp(F) = ∪{D ⊆ Z : D ⊆ F(D)}, with D a bound letter (FC91, FC92).

> L473 | **System boundary and continuity.** A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change).

**D15.4 Boundary and continuity.** β: the processes and resources that are the system's (declared); Ω: a relation on system states saying which are the same system (declared). Both are fixed before the attribution (L473).

> L475 | **Owned capability.** \(\operatorname{Can}_{\Omega,\beta}(\xi,T;\chi)\) requires an owned retained realization or an owned, physically admitted, finite construction of one under the same continuity and resource contract.

**D15.5 Owned capability.** Can_{Ω,β}(ξ, T; χ) :⟺ there is a protocol π and constructor attribute C, owned (D13.7) at ξ, with RetReal(π, T, C; χ); or an owned, physically admitted, finite construction of such, under Ω and the same resource contract.

> L477 | **Achievement.** \(\operatorname{CanAdv}(\xi,p;\chi,J_p,C_I)\): for each starting configuration in the independently specified \(J_p\), every maximal execution completes with a history meeting the achievement predicate and a continuing organization in \(C_I\).

**D15.6 Advancing capability (CA).** CanAdv(ξ, p; χ, J_p, C_I) :⟺ for every z ∈ J_p, every maximal execution from z completes with a history meeting the achievement predicate for p and ends with an organization in C_I.

> L479 | **Tolerances.** The tolerances of the physical module (Part XIV) form a directed preorder \(Q_\Theta\), in which \(q\) precedes \(q'\) when \(q'\) admits no performance \(q\) excludes, and none of them is exact;

**D15.7 Tolerances; Admit, Cap, Poss.** (Q_Θ, ≤) a directed preorder, q ≤ q' when q' excludes at least what q excludes; no member exact. Admit^{q,r} := the tasks with a realization (owned or not) at performance tolerance q and retention tolerance r, antitone in (q, r) **[I62]**; Cap^{q,r}_Ω(ξ) := the tasks with an owned realization, or an owned construction of one, at (q, r); Poss_Θ := ∩_{q,r} Admit^{q,r}; Cap^∞ := ∩_{q,r} Cap^{q,r}. (CT3): Cap^{q,r} ⊆ Admit^{q,r}; (CT4): Cap^∞ ⊆ Poss_Θ (FC93).

> L481 | The population is the set of transports the physics and the stated construction admit; a transport that would need a part every member of the population is built without is not in it.

**D15.8 Selection's population.** 𝒯 := {t : Θ admits t ∧ parts(t) ⊆ the parts of the stated construction}; μ is physically admitted; the survival condition is enacted by the environment (L481). This is where D12.1's witness is read.

## §16 Recursion, universality, classes

> L487 | **Scrutinizability.** An aspect \(d\) of a system's practice is scrutinizable at \(\xi\) when there is an owned, admitted continuation in which a description of \(d\) becomes a represented target, criticism can be directed at it, and the result can affect its operative use.

**D16.1 Scrutinizable.** Scr(d, ξ) :⟺ some owned, physically admitted continuation from ξ has a description of d as a represented target, a criticism (D9.10) of it, and a result on an active route to d's operative use.

> L492 | \forall n<\omega\ \forall\text{ admitted target chains of length }n,\ \exists\text{ an owned enabling continuation}. \tag{RC}

**D16.2 Recursive capacity (RC).** RC :⟺ for every n < ω and every admitted target chain d1, …, dn (each d(i+1) a description of di made a represented target), there is an owned continuation meeting Scr(dn) **[I74]**.

> L495 | \(\operatorname{Enable}(s,T,\chi)\) is met when \(\chi\) is an admitted, non-question-begging enabling condition for \(s\) and the task \(T\), in the sense of (CT1).

**D16.3 Enable.** Enable(s, T, χ) :⟺ χ is physically admitted, 'non-question-begging' (not defined; NF11), and an enabling condition in (CT1)'s sense.

> L500 | \operatorname{UU}\iff\forall c\in\mathfrak E_\Theta\ \exists\chi,\ \operatorname{Enable}(s,U_c,\chi)\land\operatorname{Can}(\xi_0,U_c;\chi), \tag{U1}

> L503 | \operatorname{UC}\iff\forall p\in\mathfrak P^{\mathrm{adv}}_\Theta\ \exists\chi,\ \operatorname{Enable}(s,A_p,\chi)\land\operatorname{CanAdv}(\xi_0,p;\chi,J_p,C_I), \tag{U2}

> L506 | \mathsf{UECS}=\{(M,s,\xi_0,\Omega,\beta):M\models\operatorname{RC}\land\operatorname{UU}\land\operatorname{UC}\}. \tag{U3}

**D16.4 Universality.** 𝔈_Θ := {c : Acc(c, p, t, Γ) for some p, t, Γ, and Θ admits a carrier instantiating c} **[I75]**; 𝔓^adv_Θ is not defined beyond its name (NF12). UU, UC, UECS as displayed.

> L528 | **Membership.** The base class: interpretations supplying these data with typing as declared, meeting physical realization wherever a physical attribution is made. The creative-episode class: base interpretations with an instance of (G) connected to a critical episode. The explanation-creation class: an instance of (EX). The recursive class: (RC). The universal class: (U3).

**D16.5 Classes.** Base := the interpretations M of the data of §§1–15 with the typing above and Θ-realization of every physical attribution; CreativeEp := {M ∈ Base : M has an instance of (G) in a critical episode}; ExplCreation := {M : M ⊨ CreateEx for some s, Δ, h, e}; Recursive := {M : M ⊨ RC}; Universal := UECS. Each is the extension of a formula; no axiom here puts any system in any class (FC110).

## §17 The text's exact constructions, encoded

**E1 The pole and its shadow** **[I65]**.

> L325 | Stipulate \(H:=U_H,\ \theta:=U_\theta,\ L:=H\cot\theta\), where \(U_H\) and \(U_\theta\) are exogenous values setting the pole's height \(H\) and the sun's elevation \(\theta\), and \(L\) is the length of the pole's shadow.

D_pole: V = {H, θ, L}; B ∋ b = (u_H, u_θ); J = {c_H, c_θ, c_L}, V_cH = {H}, V_cθ = {θ}, V_cL = {H, θ, L}; L_cH(1,b) = {H = u_H}, L_cθ(1,b) = {θ = u_θ}, L_cL(1,b) = {L = H cot θ}; A: setH_h, setθ_φ, setL_l (each replacing its component, D2.1) and their composites. Production question: Q = Q_L; contracts C1 = settings of H and θ, C2 = C1 plus settings of L. E_rev (the reversed calculation): c'_L: L = the observed value (boundary), c'_θ, c'_H: H = L tan θ. Identification contract: boundaries varying u_H; Q = the fibre {H : H cot θ = observed L}. Test grids: H ∈ {1,2,3}, θ ∈ {30°, 45°, 60°}. Claims: FC02, FC07, FC26–FC28, FC99.

**E2 Identification** **[I63, I64]**.

> L329 | Let \(Z\) be the admitted states, \(g:Z\to Y\) the measurement, \(f:Z\to F\) the feature. The fibre at \(y\) is \(Z_y=g^{-1}(y)\). The feature is identified at \(y\) exactly when \(Z_y\neq\varnothing\land|f[Z_y]|=1\). (I1)

Ident_y(f, g) :⟺ Z_y ≠ ∅ ∧ |f[Z_y]| = 1 (I1). (I2): (∀y ∈ g[Z] Ident_y) ⟺ f = f̄∘g for some f̄. (I3): for Z = ℝ^n, g = G linear, f = cᵀ: identification at every attainable y ⟺ ker G ⊆ ker cᵀ. Claims: FC57, FC58.

**E3 The two balances.** G = [[1,1,0],[1,0,1]] on (x, b_A, b_B) (L331). Claims: FC59, FC60.

**E4 Obstruction.**

> L335 | For allowed steps \(R\) and an invariant \(I\) with \(zRz'\Rightarrow I(z)=I(z')\), no allowed path joins states of different invariant value. (O1)

States with a step relation R and an invariant I; reachability R*. Tokens: distributions (n1, n2, n3) of 23 whole tokens. Claim: FC61.

**E5 Explanation that removes structure** **[I03]**. D with a component x deleted at the baseline and an edit a_x giving it a relation; E with k, λ(k) = {x}. Claim: FC62.

**E6 Odd-order skew-symmetric matrices** **[I66]**.

> L343 | Contract: remove skewness; remove oddness; remove both; field arithmetic and determinant–invertibility held fixed.

Ports: n, the entries M_ij, det, inv; components: skew (Mᵀ = −M), odd (n odd), det (Leibniz sum), inv (inv ⟺ det ≠ 0); edits: delete skew, delete odd, delete both; Q: does the family contain an invertible matrix? Leibniz candidate: one component per permutation term, one sum component. Test fields GF(p), p odd. Claim: FC63.

**E7 Transport results.**

> L353 | If \(\pi\circ S_a=T_a\circ\pi\) for every admitted generator \(a\), the same equation is met by every admitted finite composition with matching scopes.

> L358 | zRy\land z\xrightarrow{a}z'\Rightarrow\exists y'[y\xrightarrow{\tau(a)}y'\land z'Ry'], \tag{T1}

> L363 | With one-step discrepancy \(d(\pi Sz,T\pi z)\le\varepsilon\) at every state \(z\) of a stated scope, and with \(T\) \(L\)-Lipschitz for \(d\), the discrepancy after \(n\) steps from one state \(z\), \(e_n=d(\pi S^nz,T^n\pi z)\) (so \(e_0=0\)), meets the bound \(e_n\le\varepsilon\sum_{k<n}L^k\)

Functional, relational (T1, forward and backward simulation) and approximate (T2) transport as written. Claims: FC64–FC66.

**E8 A contract as an organization** **[I67]**.

> L590 | Give it ports (the edits and their boundaries), components (the closure conditions, each with the relation it imposes on its ports, as (O) requires), and admitted edits (add or remove a change; alter \(\mathcal Q\)).

D_C: one port m_(a,b) ∈ {0,1} per (a,b) ∈ A × B and a query port q; components: the baseline condition m_(1,b0) = 1 and the closure conditions the question declares; edits: set a membership port, set q, and composites. Claim: FC97.

**E9 The two-layer episode** **[I68, I69]**.

> L620 | Stipulate an object layer \(P\): a line of cells; two things, each with a position and a velocity; continuity components; admitted edits: displace a thing, set its velocity, occlude a cell, swap the two identities.

P: N cells, two things (position, velocity ∈ {−1, 0, 1}), steps 0..K, continuity pos(t+1) = pos(t) + vel(t) with reflection at the ends; occupancy reading per cell, empty when occluded; swap exchanges the two things' states. S0: window-w occupancy predictor, t0 selected on H0 (displacements, velocity changes). S1: a component per thing carrying position and velocity through occlusion, a persistence component, t1 with λ sending each persistence component to its thing's continuity subnetwork. ψ: the exchange of the two things, an automorphism of P preserving C and the answers. Claims: FC90, FC102, FC103.

## §18 Dependence, invariance, and where the text was vaguest

> L526 | **Dependence order.** (O) and (Q) depend on nothing; nor do the declared indices and the declared inputs, which are stated, not defined.

**D18.1 The dependence graph.** Nodes: the symbols defined in §§1–16 (D-numbered). An edge from a definition to each symbol its right-hand side uses. Sinks allowed by the text (L526, L596): Θ with Org_ℓ, 𝒩, (O), (Q), the indices, the declared inputs of L522. The primitives of D0.2 are sinks the text does not list; FC98 asks of each whether it is a claim read through Θ. Of the two loops S101 read from the wording, K2 → Live → K2 closes below the step (D9.4, D9.6). The other, build → prov → rep, stays open here: L405's 'prepares a represented organization' asks for (R), (R) asks for Sel or Con, and Con asks for a construction trace, which is what Build's subhistory is. D13.3 hides the loop only by making Prepares a primitive [I56]; with 'represented' read through (R), Build, Con and Rep are defined together, as one fixed point, unless Con's trace is read without (R). The text names the risk at L526 ('A representation defined only by its own construction … has not supplied its place in the order'). FC98 tests both loops.

**D18.2 Structure-preserving bijections** **[I70]**. A bijection φ of ports, values, components, edits (a partial-monoid isomorphism), boundaries and occurrences (preserving ≺_h and Θ's interpretation), with Q, δ, Σ and every declared input carried along. Argument 8 (FC100) is the claim that (E), (G), (P) and (EX) are kept by every such φ.

**Where the text was vaguest, for this formalization.** Three places needed the most inventions, and each carries weight elsewhere:

1. **Roles and families in Part II (L103, L109, L119, L123–L127).** The text speaks of 'the component assigning' a port and of 'observation edits', and supplies neither an assignment nor a way to read one off relational components; the two readings of L109's observation give different families on the pole's own contract (FC07), and L127's gloss adds a condition on solutions that (K) does not record (FC08). Inventions I04–I13.
2. **Non-circular dependence (L255, L257).** Its one fully formal sentence (NC2) does not exclude a lookup of the answer ('p because p' meets NC2 when the answer varies, FC23); the exclusion rests on NC1, whose 'unanalysed', 'at the declared grain' and 'structural' are defined nowhere, and on 'in the claimed way'. Inventions I21–I28.
3. **How one query and one contract apply across organizations (L141, L253, L250; L205, L413).** (A) applies the target's query to the candidate's organization, whose ports differ; (R) and ≡ ask a transport into a content to be faithful 'on c's contract', a contract on the codomain, which a transport's conditions quantify over on the domain. Every (A), (R), New, Origin and (EX) rests on the choice. Inventions I20, I48.

Next after these: the undefined primitives of Parts IX–XI (L375, L385, L403, L405, L453; I46, I47, I55, I56, I60), each read as a plain word by the round-1 checkers and each needing a primitive predicate here.

**Counts.** 115 numbered definitions (D0.1–D18.2) and 9 encodings (E1–E9); 76 inventions, each marked here where it is used and recorded in `inventions register.md`; 110 claims in `formal claims.md`.

*Written 27 September 2026. Not committed.*
