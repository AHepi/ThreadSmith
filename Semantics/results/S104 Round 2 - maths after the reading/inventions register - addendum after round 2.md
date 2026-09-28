# S104 Round 2 — inventions register, addendum after round 2

*Integration, 28 September 2026 (decisions S36, S40). The checkers' provisional inventions, numbered I122 onward in the order A1-01…A1-13, A2-01…A2-10, A3-01…A3-16. Source rows: `area N - verdicts and formal fixes.md` (not edited; the table below is the link). Fix ids: `formal core, after round 2.md`, `formal claims, after round 2.md`; T/A2-T/A3-L: text changes.*

**Counts.** 39 inventions, I122–I160; the second check adds I161–I164 (below); the owner's answers (S41) add I165, I166 (below) and settle I22, I131 and I88's 'an argument has a step'. Two are one choice registered twice: I132 = I139 (κ(⊥) := ⊥). Two are recorded and not adopted: I131 (OQ-5), I134. Three leave a choice to the owner: I146 (OQ1), I149 (reading a/b), I153 (OQ12). After the second check: I146 fixed by I162, I153 fixed (per execution); I149's reading stays open, not the owner's.

## Provisional id → I number

| prov. | I | prov. | I | prov. | I |
|---|---|---|---|---|---|
| A1-01 | I122 | A2-01 | I135 | A3-01 | I145 |
| A1-02 | I123 | A2-02 | I136 | A3-02 | I146 |
| A1-03 | I124 | A2-03 | I137 | A3-03 | I147 |
| A1-04 | I125 | A2-04 | I138 | A3-04 | I148 |
| A1-05 | I126 | A2-05 | I139 | A3-05 | I149 |
| A1-06 | I127 | A2-06 | I140 | A3-06 | I150 |
| A1-07 | I128 | A2-07 | I141 | A3-07 | I151 |
| A1-08 | I129 | A2-08 | I142 | A3-08 | I152 |
| A1-09 | I130 | A2-09 | I143 | A3-09 | I153 |
| A1-10 | I131 | A2-10 | I144 | A3-10 | I154 |
| A1-11 | I132 | | | A3-11 | I155 |
| A1-12 | I133 | | | A3-12 | I156 |
| A1-13 | I134 | | | A3-13 | I157 |
| | | | | A3-14 | I158 |
| | | | | A3-15 | I159 |
| | | | | A3-16 | I160 |

## The inventions

| I | prov. | fills (line; item) | choice | other choices | why this one | used by |
|---|---|---|---|---|---|---|
| I122 | A1-01 | "sets v directly" (L109; H03): which boundaries | at every b | some b; the contract's boundaries | L109 makes input a property of A alone | D2.1', D2.2 |
| I123 | A1-02 | "direction … consequence of which edits it admits" (L109; H04) | dir(D) := (Input_A, asg) | add Obs; leave undefined | FC02 needs a carrier; no sentence uses more | D2.5, FC02' |
| I124 | A1-03 | "its output port" (L123; H02) | the ports j assigns | D2.3 outputs, with a union | same causal components by L119, except E04's case | D4.6' (o_j) |
| I125 | A1-04 | intervention on j by an edit altering several components (H01) | Slc_j (D2.6): replaces j by a slice on a port j assigns, whatever else it alters | single settings only, composites rule edits (round 2); every alteration a setting; a composite sets each port | L57 sets rule edits against interventions; classed per component | D2.6, D2.4', D4.6'; T1, T6; FC4.new1 |
| I126 | A1-05 | "upstream" (L151; I72 part) | chain through Out, start irreflexive | chain through asg | a port with no setting edit breaks every asg-chain | D3.3'; FC36 |
| I127 | A1-06 | a contract's selection (L155; H20 part) | population, variation, survival of contracts, read through Θ | as for transports (round 2) | L155's own words; a contract has no transport to be faithful | D3.4' |
| I128 | A1-07 | "the history of t" (L193, L195, L201, L411) | the history that produced t, its preparing episode included | I53's whole history up to the attribution | a later Rep of cod t would un-select an object-layer transport (against L201, L211) | D12.1', D12.7'; T9 |
| I129 | A1-08 | a selection response (L225; H08) | Viol(t;a,b) ∧ t' ∈ μ⁺(t) ∧ Sel(t';𝒯,μ,H∪{(a,b)}) | μ*, survival only, no trigger (round 2) | L225 "to a violation", "lets μ act" | D12.8'; FC82, FC83' |
| I130 | A1-09 | "actually occurring / encountered" (L217, L195; H13) | Occurs(a,b,ξ) read through Θ | a labelled occurrence of O_h | L193, L481 place it in the physical module | D11.5 |
| I131 | A1-10 | "episode" (L197, L405, L429; H06) | any delimited subhistory (D13.8) | L55's (contract changes with records) | recorded; not applied either way (OQ-5) | none |
| I132 | A1-11 | κ at ⊥ in FC20 (U1) | κ(⊥) := ⊥ | κ undefined at ⊥ | no longer used: FC20' asks Ans_p ≠ ⊥ | FC20 (recorded) |
| I133 | A1-12 | FC06's range | ports with asg defined | every port | a port set through two components has no single assigner | FC06' |
| I134 | A1-13 | "survives on H" in time (H07) | not adopted: Faithful_H standing | fidelity at the encounter times | recorded only; D12.7' needs neither | none |
| I135 | A2-01 | L255 "does not appear … as a component" | Det_C := {(a,b)∈C : Ans_p≠⊥}; Slot :⟺ δ_E∈V_k ∧ Det_C≠∅ ∧ ∀(a,b)∈Det_C {w_δE : w∈L^E_k(τa,σb)} = {Ans_p(a,b)} | I24, I83 as registered; a block (fails the forward pole) | L255 with L273, L397; M1–M3 | D6.3; core.slot; FC23 (c) |
| I136 | A2-02 | the slot's quantifier over C | every determined pair | some pair; some pair with the contract's own edit exempt | M5 separates them; not run on the text's cases | D6.3; FC23 (d) look |
| I137 | A2-03 | D8.5's disjuncts where nothing is given | existence clauses ∃R … | vacuous (registered) | L315's lead clause | D8.5; core.conf_claim; FC52; A2-T10 |
| I138 | A2-04 | V_N for N = J_D (I14) | V_{J_D} := V_D | V_N = V_D for every N; no candidate | L269 "meets (F1) as a decomposition does" | D1.4; Org.sub; FC25 (b) |
| I139 | A2-05 | κ at ⊥ (U1) | κ(⊥) := ⊥ (= I132) | κ undefined at ⊥; FC20 restated | recorded, not applied to the text | FC20 (recorded) |
| I140 | A2-06 | L317's test clause | Test_ab := Ans_p(a,b), with R*_j where the answers agree; Arg_test | R* and answer always (registered); only where answers agree | L317's next sentence | D10.3; A2-T11 |
| I141 | A2-07 | L317 "while the argument stays usable" | Out_j at ξ; time outside the model | a time-indexed Out_j | nothing in (O), (Q) models time | D10.6 |
| I142 | A2-08 | FC51 (b)'s ψ | ψ keeps footprints | any permutation of Γ | the search used it | FC51 (b) |
| I143 | A2-09 | FC53 (a)'s premise | (χ ∧ Applies) → ¬Acc(ℰ) a stated assumption | a definition; none | L397 admits stated assumptions | FC53 (a) |
| I144 | A2-10 | FC48's hypothesis | both transports translate every pair of C | I17 total | L315 "claims … at every pair of C" | FC48 |
| I145 | A3-01 | L377 "the question whether z has δ in respect of p" | Qf(z,δ,p), a primitive | p_δ supplied with c (drops p); Qf defined in (Q) | L377 builds p_δ from z, δ, p | D9.10; FC74 |
| I146 | A3-02 | "represented" (L197, L405); "no cycle" (L526) | Rep^ρ, ρ ∈ {K staged by ≺_h, T structural}, not chosen | U (as worded: no unique Rep); trace as stated data | both remove the cycle; the choice is OQ1 | D13.3, D18.1; FC98 |
| I147 | A3-03 | L377 "with its transport and its identified commitments" | t_c, Γ_c, δ_c supplied with the criticism | read off the connection | the definite article presumes them | D9.10 |
| I148 | A3-04 | L405 "prepares a represented organization for explanatory use" | Prepares(h',o,c) ∧ Rep^ρ(o,c) ∧ ExplUse(o,c) | I56's Prepares(h',c) alone | keeps the words; C06 turns on ExplUse | D13.3 |
| I149 | A3-05 | L375 "already at rest when the result occurred" | AtRest_h(R,r) on Θ's run times; reading (a) or (b) open | the clause dropped (I46) | the text states the clause | D11.4; FC75 (b) |
| I150 | A3-06 | L375 "connected subnetwork … nonconstant dependence" | every n∈R reaches r in R; dependence along R, outside R at actual values | I46's chain clause; dependence in all of Org_ℓ(h) | admits side inputs; excludes idle members and dependence outside R | D11.4; phys.act_route; FC75 |
| I151 | A3-07 | "subhistory" (L375); Org_ℓ(h) | Org_ℓ(h): Θ's organization of h; subhistory closed under the interpretation | Org_ℓ per occurrence only (L213) | D11.4 needs the whole history's organization | D0.2, D11.3 |
| I152 | A3-08 | "connected to its inquiry" (L429), "to a critical episode" (L528); CCE(s,Δ,…) | Conn(G,h'); s the system of Origin; h_Δ ⊆ h' | Δ the episode's subhistory (GLM); Δ the response's contribution (Mimo) | uses (G)'s own s; ties Δ to the episode | D13.8, D14.7, D16.5 |
| I153 | A3-09 | "short of exact" (L461), tolerances (L479), (CT1) | RetReal^{q,r}_ϑ, ϑ ∈ {per execution, over the family}, not chosen | (CT1) exact only | E17; ϑ is OQ12 | D15.2 |
| I154 | A3-10 | "non-question-begging" (L495) | NQB: no witnessing realization uses a relayed outside carrier of c | undefined (NF11); no outside carrier of c at all | excludes supplying c, permits teaching (L405) | D16.3 |
| I155 | A3-11 | "recent" (L622), "can only predict from occupancy" (L626) | window w ≤ L_occ | w ≤ L_occ + 1; unbounded memory | sufficient for one and two things (FC102 (b'')) | FC102; A3-L626.1 |
| I156 | A3-12 | "owned retained realization" (L475) | Owned_β(π,C,s): every execution from z ∈ C owned (D13.7) | π owned as a static object | D13.7 defines ownership of subhistories | D15.5 |
| I157 | A3-13 | "requires" (L475) | Can :⟺ (a definition) | necessary conditions only (UU then unmeetable) | the bold head makes the line a definition | D15.5 |
| I158 | A3-14 | "the stated construction admit" (L481) | parts(t) ⊆ the stated construction's parts | any part the physics admits | the reading was unregistered | D15.8 |
| I159 | A3-15 | "can affect its operative use" (L487; H16) | ∃ admitted owned continuation with a result on an active route to d's use | "can change" (I74); left modal | registered; OQ6 | D16.1 |
| I160 | A3-16 | two things (L620; H17) | no interaction; may share a cell and cross | things that exclude one another | the encoding's; FC102's two-thing findings rest on it | E9; FC102 |

## Second check on the critical review (I161–I164)

*Second checker (Opus 5.5), 28 September 2026: `results/S104 Round 2 - the second checker on the critical review.md`. Rule 6: I161, I162 are settled at L195 by T9 (amended), I163 at L151 by R4-L151, I164 at L528 by A3-L528.1.*

| I | from | fills (line; item) | choice | other choices | why this one | used by |
|---|---|---|---|---|---|---|
| I161 | R1 | "exactly one of three" (L193); "the traces differ" (L411) | Sel(t) also asks ¬∃h' ⊆ h(t): CT(h', t), no construction trace in t's history prepares t | L201's "no criticism in its history" (D12.2 asks no criticism, so no exclusivity); ¬Con(t) inside Sel; none (T, T′ then give Sel ∧ Con: FC12.new1 part 3) | Sel ∧ Con excluded by definition under U, K, T, T′, whatever the cut (FC12.new1, FC83 with Rep computed) | D12.1, D12.3; T9 |
| I162 | R3, Q1 | "represented" (L195, L197, L405); "no cycle" (L526) | the cut T′: Held in Con (D12.2) and Build (D13.3); Sel's exclusion by Rep at o ≺_h o_t, a recursion along ≺_h (well founded below o_t) | U (as worded: 0–5 fixed points, a selection none); K (a first construction represents nothing, against L405); T (a declared earlier holder blocks a selection, against L195 with L211) | the one of the four meeting L405, L193 (with I161), L195 with L211, L526 (FC98 (c)–(e), FC12.new1) | D12.1, D12.2, D13.3, D18.1; T9 |
| I163 | R4 | "a C containing edits to the observed value" (L151) | ∃(a,b),(a',b') ∈ C: obs(a,b) ≠ obs(a',b'), obs the value the fibre is taken at | a setting edit of the observed port (E_rev then fails (F1), (F2): FC28 look); an edit a ≠ 1 of C altering obs (C_id holds none) | L325's identification contract C_id = {1} × B varies the observed L by boundaries only (FC28, R4 part) | D3.3; R4-L151 |
| I164 | R16 | "The universal class: (U3)" (L528) | Universal := {M : ∃s, ξ0, Ω, β (M, s, ξ0, Ω, β) ∈ UECS} | (U3)'s class of tuples as stated; ∀s (every system of M) | L528's other classes are classes of interpretations; "places its author in the universal class" reads it over some system | D16.5; A3-L528.1 |

Registered inventions ruled by the second check (owner questions re-sorted, `owner questions after round 2.md`): I146 fixed by I162 (Q1); I153 fixed: per execution (Q5); kept on argument, the other side recorded there: I10 (Q9), I14 (value maps need not be injective, Q10), I45 (Q7), I50 (Q11), I51 (Q3), I59 (Q20), I62 (Q21), I67 (Q24), I79 (Q17), I88 (Q23), I100 (Q25), I159 (Q22). Open as the owner's: I22 (Q15), I131 (Q6). [owner S41: both answered; see the section below.]

## The owner's answers (S41): I165, I166, and the inventions they settle

*28 September 2026: decision S41, written into the maths and the code (`results/S104 Round 2 - the owner's answers written into the maths.md`). Rule 6: I165 is pointed to at L55 by S41-Q6, I166 at L397 by S41-Q23b (`text changes for the owner's answers.json`).*

| I | serves | fills (line; item) | choice | other choices | why this one | used by |
|---|---|---|---|---|---|---|
| I165 | Q6 | "every change carries a provenance record" (L55), kept once "in which contracts change" is dropped (S41-Q6) | Episode(h'): a subhistory in which each change of contract, o ≺ o' with o' immediately after o and q(o) ≠ q(o'), has a record in h' of ρ_{q(o')} with its trace (D3.4); q(o) = (C, Q), the contract operative at o, read through Θ; no change need occur | the record clause dropped too (I131 as registered: any delimited subhistory); L55 as worded (at least one change: excluded by S41, Q6) | keeps the rest of L55's sentence and of its indexing ("the two ways are indexed so they cannot be confused"); the owner's words fix only that no change is needed | D13.8 (Episode; CompleteCritical), D12.2 (Con); model/claims_b.py (episode, chain_eps, _con_at, con); FC84.new1 |
| I166 | Q23 | a premise alone as an argument (D9.2): when j can use it (L397 "usable by j when each of its steps is (K2)" has no step to apply to) | Usable_j(α) for α a premise alone d :⟺ d ∈ Accepted_j(ξ) (Live_j with no step); no Form_j or Scope_j (no step has a form or an index) | vacuous (every premise alone usable by everyone, since it has no step); also Scope_j on an index the premise is used at | L393 "a claim j has never taken up is not live for j"; L397 "(K2) asks only that they be live for the person using the step"; the owner's example is a claim the person uses, so takes up | D9.6; model/args.py (usable, ARG_READING); FC72 (d)–(f) |

Settled by the owner's answers (the register's entries are not edited; the fixes are here):

| I | now | by |
|---|---|---|
| I22 | settled: the contrast is ≠ in Y_p ∪ {⊥} (⊥ ≠ y, ⊥ = ⊥), symmetric; "in the claimed way" leaves L255 | S41 Q15; D6.4; S41-Q15; FC22 (b) |
| I131 | settled: an episode is a subhistory and need hold no change of contract; its changes, if any, carry records (I165) | S41 Q6; D13.8; S41-Q6; FC84.new1 |
| I88 | amended: a premise alone is an argument (its second clause, "an argument has a step", reversed); the finite range of X_j stays | S41 Q23; D9.2, D9.6, D9.7; S41-Q23a, S41-Q23b; FC72 (d)–(f) |

Q2 needed no invention: the owner's words fix Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ), and L536 already writes ¬Dec(t) (D16.XV; S41-Q2; FC30.new1). Q15 needed none: D8.2 already reads "differ" in Y_p ∪ {⊥}.

## Registered inventions fixed or amended in round 2

| I | now | by |
|---|---|---|
| I06 | fixed: R-ii, with Slc_j | D2.4'; T1 (A1) |
| I80 | fixed: 1 ∉ Set_v | D2.1' (A1) |
| I72 | part: upstream as I126 | D3.3' (A1) |
| I52, I53 | fixed in part: occurrences of t's one history | D12.1'; T9 (A1) |
| I93 | fixed: reading (i) | FC05; T4 (A1) |
| I21 | codomain Y_p ∪ {⊥} in the text | T7 (A1) |
| I73 | narrow reading in the text | T8 (A1) |
| I102 | 2nd clause trimmed (asg(m) defined) | D4.6' (A1) |
| I14 | V_{J_D} := V_D | D1.4 (A2, I138) |
| I24, I83 | amended to their (b) | D6.3 (A2, I135) |
| I26 | "≠ ⊥" dropped | D6.9; A2-T2 |
| I27 | in the text | D3.5; A2-T1 |
| I33 | + Off(ℰ,p) | D8.3 (A2) |
| I36 | fixed less κ | D8.new1; A2-T9 |
| I37 | pointed to | D10.4; A2-T12 |
| I49 | Fid⁺ dropped where L245, L247, L520 are read | D5.7 (A2; L520 by A3) |
| I64 | Z any vector space | E2, FC58 (A2) |
| I65 | C_id := {1} × B | E1; A2-T13 |
| I40 | fixed: Below(u) | D9.2, D9.4; A3-L393.1 |
| I43 | fixed | D9.9; A3-L395.1 |
| I44 | fixed by its choice (b): ⪯_h := ≺_h* | D11.3; A3-L375.1 |
| I46 | replaced by I149, I150 | D11.4 (A3) |
| I60 | pointed to | D14.6; A3-L453.1 |
| I61 | fixed: Exec ≠ ∅ for every z ∈ Z | D15.2, D15.3; A3-L471.1 |
| I67 | fixed for the query port | E8; A3-L590.1 |
| I68, I100 | window and L_occ fixed | FC102; A3-L626.1 |
| I69 | fixed | FC103; A3-L630.1 |
| I76 | p_δ := Qf(z,δ,p) replaces "supplied" | D9.10 (A3, I145) |
| I83, I84 | rest under every result computing NC1 (I83) or (F2) (I84), not only FC23, FC24 | U6 (A2; register) |
