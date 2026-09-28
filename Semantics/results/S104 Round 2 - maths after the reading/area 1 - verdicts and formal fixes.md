# S104 Round 2 - area 1 (L1-L228): verdicts and formal fixes

*Checker 1 of 3 (fresh Opus 5.5, built nothing of this round). Decision S40; reading rule rules 3, 6, 8-11; both addenda. Text under review: `tests/103 ...after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd, not written). Maths: `results/S104 Round 2 - maths/` (not written). Model copy: `area 1 model/`. Runs: `area 1 - runs.txt`. Text changes: `area 1 - text changes.json`. Analysis used where its argument holds: `ruling L113-L127.md`, `ruling L13-L201.md` (their wordings not used).*

Verdict codes: **M** holds against the maths; **W** holds against the words; **I** rests only on an invention the text leaves open (rule 6); **N** does not hold.
Principle kept: a vague sentence is filled in the maths (invention recorded), not in the text; the text changes only where its words say something they should not.

## 1. Formal fixes (old → new, formal core notation)

| fix | old | new | settles / invention |
|---|---|---|---|
| D2.1' | Set_v := edits of A that, at every b, set v through some component | Set_v := {a ∈ A∖{1} : ∀b ∃j, a sets v through j at b} | I80 → its other choice (a), fixed by L103 "replaces", L141 baseline, L325 (check T13) |
| D2.4' | Obs(o,m) under R-i (any a ∈ Alt_j leaving asg(m)) and R-ii (also a ∉ Set_o), both carried | Obs(o,m) := {a ∈ Alt_j ∖ Slc_j : L_asg(m)(a,b) = L_asg(m)(1,b) ∀b}, j = asg(o), m ∈ V_j∖{o}, asg(m) defined. R-i kept as recorded other choice only | settles I06 (R-ii); text T1 |
| D2.6 (new) | — | Slc_j := {a ∈ Alt_j : ∀b [L_j(a,b) ≠ L_j(1,b) ⇒ ∃v ∈ V_j, asg(v) = j, ∃x: L_j(a,b) = {w : w_v = x}]} (interventions on j, single or composite) | A1-04 |
| D3.3' | v ⇝ w: j_1..j_n, v ∈ V_j1, Out(u_i,j_i), u_i ∈ V_j(i+1) for i < n, u_n = w; respects "sufficient conditions" | v ⇝ w :⟺ ∃n ≥ 1, j_1..j_n, u_1..u_n: v ∈ V_j1∖{u_1}; Out(u_i,j_i) ∀i ≤ n; u_i ∈ V_j(i+1)∖{u_(i+1)} ∀i < n; u_n = w. Prod, Ident, Obst are L151's conditions (by "fixed by", both ways); they may overlap | I72 (part); A1-05 |
| D3.4' | ρ_p selected/constructed "as for transports (D12.1, D12.2)" | selected :⟺ C survived in a population 𝒞 of contracts under a variation operator and a survival condition in a physical history (read through Θ); constructed :⟺ C results from an episode with a construction trace; declared :⟺ neither (L155) | A1-06 (H20, D3.4 part) |
| D3.6' | BadBaseline :⟺ Sol_D(1,b0) = ∅ ∨ b0 ∉ B | BadBaseline :⟺ Sol_D(1,b0) = ∅ (b0 ∉ B excluded by D3.1: (1,b0) ∈ C ⊆ A×B) | — |
| D4.6' | Meas_C(j,m) :⟺ m ∈ V_j, asg(m) ≠ j, Inv_C(j,Set_m) ∧ Changes_C(j,MR_j), MR_j = Alt_j (R-i) or Alt_j∖Set_oj (R-ii); Rule_C(j) :⟺ Inv_C(j,World_j) ∧ Changes_C(j, Alt_j∖Set_oj) | Meas_C(j,m) :⟺ m ∈ V_j, asg(m) defined, asg(m) ≠ j, Inv_C(j,Set_m) ∧ Changes_C(j, Alt_j∖Slc_j); Rule_C(j) :⟺ Inv_C(j,World_j) ∧ Changes_C(j, Alt_j∖Slc_j); Causal_C(j) with Obs of D2.4' | U5 closed (I102's 2nd clause trimmed); H01 |
| D12.1' | Sel(t;𝒯,μ,H): …, no occurrence represents t, H or the survival condition | Sel(t;𝒯,μ,H) :⟺ t ∈ 𝒯; μ: 𝒯 → P(𝒯); H ⊆ C finite, pairs occurring; Faithful_H(t); members of 𝒯 admitted (D15.8); ¬∃o ∈ h(t), x ∈ {t, H, surv, cod t}: Rep(o,x) | settles H05, I52 (occurrence reading), I53; A1-07; text T9 |
| D12.7' | Surp(t;a,b) :⟺ Sel(t;𝒯,μ,H) for some 𝒯,μ,H with (a,b) ∉ H, and Viol | Surp(t;a,b) :⟺ Sel(t;𝒯_t,μ_t,H_t) ∧ (a,b) ∉ H_t ∧ Viol(t;a,b), (𝒯_t,μ_t,H_t) of t's one history (L193, L217). Consequence: Sel ∧ Viol(a,b) ⇒ (a,b) ∉ H_t | H07 (the text's) |
| D12.8' | SelResp(t→t';a,b) :⟺ Sel(t), t' ∈ μ*(t), t' survives on H∪{(a,b)}; ConResp(→t'') :⟺ new ∧ Con | SelResp(t→t';a,b) :⟺ Sel(t;𝒯,μ,H) ∧ Viol(t;a,b) ∧ t' ∈ μ⁺(t) ∧ Sel(t';𝒯,μ,H∪{(a,b)}); ConResp(→t'';a,b) :⟺ Viol(t;a,b) ∧ New(t'' or cod t'') ∧ Con(t'';h,e) | H08; A1-08 |
| FC02' (c) | "the direction H,θ → L is carried by asg"; identity a setting of H, θ | asg(L) = c_L where A holds a setting of L; Out(v,c_L) for v = H, θ, L; 1 ∉ Set_v (D2.1') | — |
| FC06' | ∀m, ∀a ∈ Set_m, ∀j ≠ asg(m) | ∀m with asg(m) defined, … (as the code) | A1-12 |
| FC20' | F2eq(a,b) ∧ π acts on δ as κ ⇒ Ans_E = κ(Ans_p) (κ(⊥) := ⊥) | F2eq(a,b) ∧ Ans_p(a,b) ≠ ⊥ ∧ π acts on δ as κ ⇒ Ans_E(τa,σb) = κ(Ans_p(a,b)) | U1 recorded as A1-11 |
| FC30' | title "(E) takes no assessor, history, provenance or wording" | "(E) takes no assessor, history or provenance" (Σ, a stated scope, is an argument) | — |
| FC77' | ∀t: Sel(t;{t},id,∅) when Θ admits t | ∀t with Hom(τ): Sel(t;{t},id,∅) when Θ admits t | — |
| FC83' | SelResp(t→t') ⇒ ¬Origin(…, c', …) | SelResp(t→t') ⇒ ¬∃ Build of cod t' in h(t') (Build prepares a represented organization, L405; D12.1' forbids Rep(o, cod t') in h(t')) | — |
| FC2.new1 (new) | — | (1) under R-i: j reads m, asg(m) ∉ {j, undef} ⇒ ¬Causal_C(j), ∀C; (2) under R-ii ∃ such j with Causal_C(j); (3) pole: Causal_C2(c_L) under R-ii, not R-i | ground of D2.4' |
| FC4.new1 (new) | — | m ∈ V_j ∧ asg(m) ∉ {j, undef} ∧ Changes_C(j, A∖Slc_j) ⇒ Meas_C(j,m) (R-ii; R-i with A) | text T6 |
| FC12.new1 (new) | — | ¬(Sel(t) ∧ Con(t)) on every history h (D12.1'); round 2's D12.1 admits h with both | ground of T9 |

## 2. Code changes (in `area 1 model/model/`)

| file | change | fix |
|---|---|---|
| core.py | `Roles` excludes the identity from Set_v by default (`exclude_identity`) | D2.1' |
| core.py | `Roles.slc[j]`, `_slices`; R-ii `obs`/`obs_pairs` skip Slc_j; `meas` needs asg(m) defined, R-ii MR drops Slc_j; `rule` drops Slc_j; `OBS_READING = "R-ii"` | D2.4', D2.6, D4.6' |
| core.py | `Roles.upstream(v,w)` | D3.3' |
| claims_b.py | `sel(..., cod)` bans cod; `con(h, cod)`; `viol_at`; `selresp` (D12.8'; flag `round2` keeps round 2's) | D12.1', D12.8' |
| claims_b.py | FC77 part 1 needs Hom; FC78, FC81 (d) print round 2 and fixed; FC82 rewritten + the second check's stronger case; FC83 → FC83'; x picked from `sorted(p.C)` (program check §4.1) | FC77', D12.1', D12.8', FC83' |
| claims_b.py | FC101: del_r1, del_r2 impose the full relation | H18 |
| claims_a.py | FC20 part 1: hypothesis Ans_p ≠ ⊥; FC05 reading (ii) → look; FC07 C2* text computed; FC36 uses `upstream`; FC14 reads the committed formal core (read only) | FC20', T4, H01, D3.3' |
| claims_area1.py (new) | FC2.new1, FC4.new1, FC12.new1 | new claims |
| harness.py, run.py | seeds and sort for ids `FCn.newm`; import claims_area1 | — |

**Runs** (`area 1 - runs.txt`; scale 4, cap 45 s, every claim, 306.5 s): round 2's 87 hold / 12 CEX / 11 not tested → 97 / 5 / 11 of 110, plus 3 new claims holding. No claim or part newly fails. Resolved: FC05, FC20, FC77, FC78, FC81, FC82, FC83. Left (other areas): FC18, FC23, FC25, FC63, FC102.

## 2b. Text changes (exact spans in `area 1 - text changes.json`)

| id | line | kind | what | settles |
|---|---|---|---|---|
| T1 | L109 | formal | L109's observation sentence → D2.4' in symbols (drops the "that is" clause) | I06 (reading R-ii); A1-04 |
| T2 | L119 | formal | "through τ and τ'" → "through τ,σ and τ',σ'" | I12 (in part: σ on boundaries, as L556 writes it) |
| T3 | L119 | formal | "through τ, and its counterpart" → "through τ,σ, …" | I12 (in part) |
| T4 | L119 | formal | "stay equal … does not separate" → FC05 (i) in symbols | I93 (reading i) |
| T5 | L127 | formal | "patterns in (K)" → "functions of (D,C) (D4.6, FC13)" | — |
| T6 | L127 | formal | L127's reading-part sentence and its solutions gloss → FC4.new1 in symbols | A1-04 |
| T7 | L141 | formal | codomain Y_p → Y_p ∪ {⊥} (D3.2) | I21 |
| T8 | L151 | formal | "an answer to one is not an answer to the other" → Acc(ℰ,p) ⇏ Acc(ℰ,p′) (FC34) | I73 (narrow reading) |
| T9 | L195 | formal | "No member of the history represents t, H, or the survival condition." → D12.1's clause in symbols | H05; I52 (in part: occurrences of the history of t); I53; A1-07 |
| T10 | L199 | delete | "The transport is entered into the model by its author." deleted | — |

## 3. Verdicts, one row per item (117)

| id | v | reason (one line) | formal fix | code | runs |
|---|---|---|---|---|---|
| D1.1 | I | "partial associative" admits Kleene or weak (I01); no sentence or result turns on it | none | none | FC01 H |
| D1.3 | I | deletion is L103's; "absent port" (L339, area 2) is I03's reading | none | none | FC01 H |
| D2.1 | M | D2.1 lets 1 set a port (I80); L103 "replaces", L141 baseline, L325 fix a ≠ 1 | D2.1' | Roles default | all 110+3 |
| D2.2 | M | Input follows D2.1 (GLM, I80) | D2.1' | as D2.1 | FC02 H |
| D2.3 | I | which edit, at most one (I05); "across B" fixes every b; nothing turns | none | none | FC02 H |
| D2.4 | W | L109's words admit R-i, under which no reader of an assigned port is causal (FC2.new1), against L37, L57 causes; "that is" equates an A-condition with a C-signature (FC11) | D2.4', D2.6; T1 | obs, slc | FC2.new1, FC07, FC11 H |
| D2.5 | I | direction as (Input_A, asg) is a reading (H04); L109 says what it is a consequence of | none (A1-02) | none | FC02 H |
| D3.1 | W | how Q reads E is not said (L141 vs L250); maths fills it with δ (I20) | none (I20 stands) | none | — |
| D3.2 | W | codomain Y_p vs "not determined" (L255); maths has ⊥ (I21) | none; T7 | none | — |
| D3.3 | M | printed chain's "for i < n" leaves n = 1 unlinked and v = w: every port upstream (Mimo); "fixed by" gives both directions | D3.3' | upstream; FC36 | FC36 H |
| D3.4 | M | borrows transports' Sel/Con; L155 gives contracts their own (H20) | D3.4' | none | — |
| D3.6 | M | "b0 ∉ B" cannot occur under D3.1; Desc is I76 (open) | D3.6' | none | FC106 H |
| D3.7 | W | L151's clause read literally (wide) fails: one candidate meets (E) on two questions (FC34) | D3.7 narrow; T8 | none | FC34 H |
| D4.2 | I | equal-domain clause (I10) beyond the words; no result turns once I94 excluded; I10 (b) excluded by "equivalence class" | none; OQ-1 | none | FC03, FC04 H |
| D4.3 | W | "through τ" alone reads E's component at no E-boundary; L556 writes σ | none; T2, T3 | none | FC16, FC17 H |
| D4.4 | N | "up to the port translation" with L233, L556 is D4.4's reading (check T03) | none | none | FC18 CEX (rests on I94, unchanged) |
| D4.5 | I | same-boundary, existential "changes", vacuous "invariant" are the words' (L123 contrast); I09 (b) turns nothing | none | none | FC10, FC12 H |
| D4.6 | M | Meas counted m with asg(m) undefined (U5, against L127 "another part"); composites of settings counted as rule edits (H01, against L57) | D4.6', D2.6 | meas, rule, slc | FC06-FC13, FC4.new1 H |
| D5.2 | N | formula is L233 read part by part (I14); "alone" repeats "the constraints of λ(k)" | none | none | FC15-FC17 H |
| D11.1 | W | "event" used at L53, L55, L161, L397, L604, L612, defined nowhere | none (I45 stands); OQ-4 | none | — |
| D11.2 | N | I48's triple is "contract-relative commitments"; comparison by transports is D13.4's | none | none | — |
| D11.5 | I | Occurs read through Θ (L193, L481); unregistered (H13) | none (A1-09) | none | — |
| D12.1 | W | L195 forbids nothing as written (H's members are pairs) and leaves a represented cod t open, against L13, L201, L411; Sel ∧ Con on one history (FC78) | D12.1'; T9 | sel | FC77, FC78, FC81-FC84, FC95, FC12.new1 H |
| D12.2 | I | "episode" as any subhistory (H06, OQ-5); E03's Rep→Con→Build loop is L526's (area 3) | none | none | — |
| D12.3 | M | Dec = ¬Sel ∧ ¬Con is "Neither of the above" only with D12.1' (GLM) | via D12.1'; T10 | none | FC12.new1 H |
| D12.5 | W | "faithful on c's contract" is a contract on E_c, not on the transport's domain: too vague for (R); maths fills (I48 preimage), no text change | none | none | FC85, FC95 H |
| D12.7 | M | "for some 𝒯,μ,H" against L217's one H and L193 (H07); violation extent rests on I50/I18 (OQ-3) | D12.7' | none | FC81 H |
| D12.8 | M | no trigger (L225 "to a violation"); μ* allows zero steps against "lets μ act"; result not required selected | D12.8' (A1-08) | selresp | FC82, FC83 H |
| FC02 | M | (c)'s "carried by asg" needs the pole's full A; identity-as-setting (I80) | FC02' | via D2.1' | FC02 H |
| FC05 | W | counterexample is to reading (ii), which "stay equal" admitted; formal reading (i) holds | T4 | (ii) → look | FC05 H |
| FC06 | M | statement quantifies every m, code only asg(m) defined (Mimo break 1); break 2 rests on H01's alternative | FC06' (A1-12) | none | FC06 H |
| FC07 | W | on C1 c_L reads H, θ and has no family: L127 S4 fails unhedged; C2 splits on I06; C2* on H01 | via D2.4', D4.6'; T6 | C2* text | FC07 H |
| FC08 | W | both L124 clauses hold and the reading does not follow: L127's gloss is about solutions (L119) | T6 deletes gloss | none | FC08 H |
| FC09 | N | L347's pattern is L125's word for word; D4.6 maps constitutive status to Rule_C | none | none | FC09 H |
| FC10 | I | L57 fails only read universally (I09 (c)); L123's contrast gives the existential reading | none | none | FC10 H |
| FC11 | W | L109's "that is" equates Observation (on A) with a signature (on C); they come apart | T1 | none | FC11 H |
| FC12 | N | change clauses need a witness in C, invariance ones may be vacuous: the text's structure | none | none | FC12 H |
| FC13 | W | families use how C's edits touch other components (Obs, Set_m), not j's (K) alone | T5 | none | FC13 H |
| FC14 | N | the scan claims what FC14 states; indexing to C carries L127 S2-S3 | none | path only | FC14 H |
| FC20 | M | counterexample to the claim's lemma (κ merges values at Ans_p = ⊥, U1), not to a sentence | FC20' | FC20 part 1 | FC20 H |
| FC30 | M | "or wording" not carried: Σ, a stated scope, is an argument of Acc | FC30' | none | FC30 H |
| FC34 | W | wide reading fails (witness survives I83's alternative, program check §5) | T8 | none | FC34 H |
| FC35 | W | L151's "prediction" lies outside L219's (transports to S) | none; OQ-6 | none | FC35 NT |
| FC36 | I | purpose-achievement fails only if (AR)'s purpose G is O_p, not in Q; text does not identify them | D3.3' in code | FC36 | FC36 H |
| FC77 | M | "every transport": Hom(τ) not vacuous on ∅ (I18); residue (H = ∅, I52 (b); population of one, H09 → L481) stays | FC77' | part 1 | FC77 H |
| FC78 | W | Sel ∧ Con through L195's gap (H05) | via D12.1'; T9 | text | FC78 H |
| FC79 | N | C := H is a reading nothing forces; H ⊆ C (L195), H ⊊ C where asked (L572, L580) | none | none | FC79 H |
| FC81 | W | (d) as FC78; Mimo's (a)-(c) attack is on D12.7's "for some" (H07) | via D12.1', D12.7' | text | FC81 H |
| FC82 | M | as FC78, plus no trigger, no μ-step (H08), result not required selected (stronger case) | via D12.1', D12.8' | rewritten | FC82 H |
| FC83 | M | claim predicates Origin of c' anywhere; sentence says the response is not originative | FC83' | rewritten | FC83 H |
| FC84 | M | 2nd sentence said what L195 did not (check §5) | via D12.1' | none | FC84 H |
| FC95 | N | a transport is the tuple (π,τ,σ,λ) (L186), not fixed by domain and codomain; L211 names two transports | none | none | FC95 H |
| FC105 | W | as D11.1 | none; OQ-4 | none | FC105 NT |
| FC106 | N | "no account" follows from L257's Sol_D(1,b0) ≠ ∅ (the target's; Mimo's model misreads it) | D3.6' | none | FC106 H |
| FC107 | I | p_δ needs an organization as target (H12); open whether a question is one | none; OQ-8 | none | FC107 NT |
| I01 | I | as D1.1 | none | none | — |
| I02 | N | the text fixes it (L574 "supplied independently for each (a,b)"); register label only | none | none | FC80 H |
| I04 | W | "the component assigning" undefined (E04); D2.1 defines it from the setting edits (I04), the one reading L109 "No role assignment is supplied" and L103 leave | none (D2.1' stands) | none | FC02, FC06 H |
| I05 | I | as D2.3 | none | none | — |
| I06 | W | as D2.4 | D2.4'; T1 | obs | FC2.new1 H |
| I07 | N | settled in substance: measuring relation j's own (L124), measured port another part assigns (L127), per port | none | none | — |
| I08 | M | "the rule" = j's relation (L347), own setting no rule edit (L57); composites counted as rule edits (H01) | D2.6, D4.6' | rule | FC07, FC09 H |
| I09 | I | as D4.5 | none | none | — |
| I10 | I | as D4.2 | none; OQ-1 | none | — |
| I11 | N | the text fixes it: L39 "more admitted changes", L317 "a finer contract that contains a change" | none | none | — |
| I12 | W | as D4.3; comparison as functions on C stays I12 | T2, T3 | none | — |
| I14 | I | value maps κ, several D ports into one: open | none; OQ-2 | none | — |
| I16 | I | "on the stated scope" leaves π's domain open; nothing in area 1 turns | none | none | — |
| I17 | I | partial τ, σ; "translates" (L315, area 2) open | none | none | — |
| I21 | W | as D3.2 | T7 | none | — |
| I45 | W | as D11.1 | none; OQ-4 | none | — |
| I48 | W | as D12.5 | none | none | — |
| I50 | I | L189's fidelity read at a pair; Hom has no pairwise form (I18) | none; OQ-3 | none | FC20 H |
| I51 | W | as FC35 | none; OQ-6 | none | — |
| I52 | W | "member of the history" must be an occurrence of h(t) (T9); H nonempty (b) stays open (L195 last sentence, L574); Faithful_H exact stays the search's | D12.1'; PARKED-1, 2 | sel | FC77 H |
| I53 | W | one history (L193 "its history") now also at L195 | D12.1' (A1-07); T9 | sel | FC78 H |
| I56 | I | Prepares etc. read through Θ; E03 → L526, C06 → L405 (area 3) | none | none | — |
| I72 | M | as D3.3 | D3.3' (A1-05) | upstream | FC36 H |
| I73 | W | as D3.7 | T8 | none | FC34 H |
| I76 | I | Desc for the three defects: open; nothing turns | none | none | FC106 H |
| I80 | M | as D2.1 | D2.1' | Roles default | all |
| I81 | I | search design (π induced, computed ports, candidates generated): recorded | none | none | — |
| I82 | I | NC1 only for port-reading queries: a recorded narrowing (L255, area 2) | none | none | — |
| I93 | W | as FC05 | T4 | FC05 look | FC05 H |
| I94 | N | excluded by "up to the port translation", L233, L556 (check T03) | none | none | FC18 CEX (unchanged) |
| I102 | M | union for several outputs stays open; 2nd clause gave U5 | D4.6' | meas | FC4.new1 H |
| U4 | N | each relation unchanged ≠ the two equal to each other; sufficient for (i) where (1,b) ∈ C | none | none | — |
| U5 | M | as I102 ("another part", L127) | D4.6' | meas | FC4.new1, FC08 H |
| H01 | M | composite of settings counted as rule edit (I08) against L57; "a composite is no setting in L119's sense" is the text's | D2.6 (A1-04) | slc | FC07 H (C2* = C2 under R-ii) |
| H02 | I | "its output port" as ports j assigns: by L119 same causal components as D2.3 outputs except E04's case | none (A1-03) | none | — |
| H03 | I | "at every b": L109 names no boundary | none (A1-01) | none | — |
| H04 | I | as D2.5 | none (A1-02) | none | — |
| H05 | W | as D12.1 | D12.1'; T9 | sel | FC78, FC12.new1 H |
| H06 | W | L55 (the one definition) vs the body's uses and D13.8 (any subhistory); which stands is OQ-5 | none (A1-10); OQ-5 | none | — |
| H07 | M | as D12.7; GLM's time-indexed survival recorded (A1-13) | D12.7'; PARKED-3 | none | FC81 H |
| H08 | M | as D12.8 | D12.8' | selresp | FC82, FC83 H |
| H13 | I | as D11.5 | none (A1-09) | none | — |
| H18 | M | FC101's deletions set m := 0; L103: full relation | none (code) | FC101 | FC101 H |
| NF01 | N | L17 states a conjecture and what would rule it out; E06 is L536-L538 (area 3) | none | none | — |
| NF07 | N | "reducible" unformalized; the colon clause and L542 say what it is and what would rule it out; formal part FC12.new1 | none | none | FC12.new1 H |
| matter 2 | W | as D11.1 | none; OQ-4 | none | — |
| matter 4 | N | as FC09 | none | none | FC09 H |
| matter 5 | W | as FC11 | T1 | none | FC11 H |
| matter 6 | W | as FC35 | none; OQ-6 | none | — |
| matter 14 | N | L27 states nothing false; a missing pointer is no defect the maths shows | none | none | — |
| L123 | N | removal stands (a setting replaces the component, L103); R-i unsatisfiability is FC2.new1 (1), met by T1; "model two" fails for c_H (footprint {H}) | none | none | FC07 H |
| E04 | W | as I04; FC-E2 (both ports outputs) is D2.3/I05 | none | none | FC02 H |
| E05 | W | in part: L127 S4 unhedged and its solutions gloss (FC07 C1, FC08) → T6; families not claimed exclusive; kinds beyond signatures: scope | T6 | none | FC4.new1 H |
| E14 | N | text claims a difference in what histories contain (L13, L47, L201, L542), which E14 grants | none | none | FC12.new1 H |
| E22 | N | L3, L17 call it a conjecture; priorities and benchmark are proposals | none | none | — |
| C01 | W | L199's "its author" makes a computed or written transport declared by its maker (L409, L427); L13, L193 stand | T10 | none | — |
| C02 | I | "represented target" in the run rests on I114-I116; L201 claims no exhaustion; criticism residue turns on H06 | none; OQ-5 | none | — |
| C03 | I | with T9 in (R)'s sense the coding search's class turns on the code writing's provenance (I56, I90, I114) | none; OQ-9 | none | — |
| C04 | I | L195 asks survival requiring fidelity (L189, L23); the answers-only divergence rests on I110, I113; extent is I49 (area 2) | none | none | — |
| C05 | N | L225 distinguishes two responses and claims no exhaustion; "by whom" is L427's | none | none | — |
| C07 | I | Con's "episode" turns on H06 | none; OQ-5 | none | — |
| C11 | N | provenance is asked of transports a physical system holds (L193, L205, L213); I111 is the card's | none | none | — |

Context items (no verdict asked): E01, E07 (instance of L127 S5 with T6), E08, E11 (no mapping to model-free/model-based in L13), E12, E16, C08 (I51's extension: OQ-6), C13 (L195 last sentence works), H20 (D3.4 part fixed as D3.4'; the rest not area 1).

Counts (by program from the table): M 26, W 37, I 31, N 23; 117 rows, every area 1 item once.

## 4. New inventions (provisional ids; the orchestrator numbers them from I122)

| id | fills | choice made | other choices | why this one |
|---|---|---|---|---|
| A1-01 | "sets v directly" (L109): boundaries (H03) | at every b | some b; the contract's boundaries | L109 makes input a property of A alone (GLM) |
| A1-02 | "direction … a consequence of which edits it admits" (L109) (H04) | dir(D) := (Input_A, asg) | add Obs; leave undefined | FC02 needs a carrier; no sentence uses more |
| A1-03 | "its output port" (L123) (H02) | the ports j assigns | D2.3 outputs with a union | same causal components by L119, except E04's case |
| A1-04 | what counts as an intervention on j when an edit alters several components (H01) | Slc_j (D2.6): any edit replacing j by a slice on a port j assigns, whatever else it alters | round 2: only single settings, composites rule edits; every alteration a setting (global); a composite "sets each port" (against L119 "only") | L57 sets rule edits against interventions; per component, so mixed edits are classed by what they do to j |
| A1-05 | "upstream" (L151) (I72 part) | chain through Out, start irreflexive | chain through asg (direction from A) | Mimo's corrected chain; through asg a port with no setting edit breaks every chain |
| A1-06 | a contract's selection (L155) (H20 part) | population, variation, survival of contracts read through Θ; survival condition not fixed | as for transports (round 2) | L155's own words; a contract has no transport to be faithful |
| A1-07 | "the history of t" (L193, L195 as T9, L201, L411) | the history that produced t, an episode whose trace prepares t included | I53's "whole history up to the attribution" | a later Rep of cod t (a simulation layer over P) would un-select an object-layer transport, against L201's first sentence and L211 |
| A1-08 | a selection response (L225) (H08) | Viol(t;a,b), t' ∈ μ⁺(t), Sel(t';𝒯,μ,H∪{(a,b)}) | round 2: μ*, survival only, no trigger | L225 "to a violation", "lets μ act"; else FC82's stronger case gives a common result |
| A1-09 | "actually occurring/encountered" (L217, L195) (H13) | Occurs(a,b,ξ) read through Θ | a labelled occurrence of O_h | L193, L481 place it in the physical module |
| A1-10 | "episode" (L197, L405, L429) (H06) | any delimited subhistory (D13.8) | L55's (contract changes with records) | OQ-5; not applied either way |
| A1-11 | FC20's value of κ at ⊥ (U1) | κ(⊥) := ⊥ | κ undefined at ⊥ | no longer used: FC20' asks Ans_p ≠ ⊥ |
| A1-12 | FC06's range | ports with asg defined | every port | a port set through two components has no single assigner |
| A1-13 | "survives on H" in time (H07, GLM) | not adopted: Faithful_H as a standing condition | fidelity at the times of the encounters | recorded only; D12.7' needs neither |

## 5. Owner questions (not applied; both sides one line each)

- **OQ-1 (D4.2, I10).** Mimo: whether a footprint bijection may recode port values is "where values are placed", the owner's. GLM: nothing in the owner's words points either way; write equal domains in. Checker: no change; I10's clause stays open.
- **OQ-2 (FC20, I14).** GLM: value maps must be injective (a merging κ hides a difference (F1) should catch, L245). Other: L189 lets π merge values; κ stays open.
- **OQ-3 (I50, D12.7).** Mimo: if a failed prediction ((A) at a pair) is to count as violation, the words must say so. Other: L220 names fidelity, which L189 defines by (F1), (F2) only.
- **OQ-4 (matter 2, D11.1, I45, FC105).** An event is a nonempty set of occurrences of one history (I45). Or events have identities of their own (L612 "lost event identities").
- **OQ-5 (H06, C07, C02, D12.2).** An episode is a delimited subhistory (the body's uses). Or L55's history in which contracts change, each change with a record (then Con and (EX) need contract changes).
- **OQ-6 (matter 6, FC35, I51).** L151 stops borrowing "prediction" (writes Ans_E(τa,σb)). Or L219 widens "prediction" to every transport (writes I51 in).
- **OQ-7 (FC83).** GLM: S20's "a variation is a competitor … two discovered variations" lets a population hold variants discovered new. Other: L225, L47 keep origin with construction; FC83' formalizes the sentence as it stands.
- **OQ-8 (FC107).** GLM: whether a question or a defect can be a target organization for p_δ is the owner's. Other: L161 says only "another question with its own contract".
- **OQ-9 (C03, C02).** T9 read in (R)'s sense: a coding search whose code represents H, the survival condition or cod t is not selected. Other: a coded-fitness search is ordinarily called selection; its class then turns on the provenance of the code's writing.

## 6. Parked (S33, S34; recorded, not applied)

- **PARKED-1 (I52, GLM part 14):** strength of survival conditions under S20's "Good explanations make bad ones harder to fit".
- **PARKED-2 (I52, FC77, GLM part 13):** S20's "A variation is a competitor" as a requirement that t have a competitor in 𝒯, as far as it bears on hard to vary.
- **PARKED-3 (H07, GLM part 14):** S20's "Once the explanation is rescued, the mistake shouldn't be able to creep back in" cited for time-indexed survival.

## 7. For the integration step

- T1 and T6 use D2.6 (Slc_j) and D2.4'; T9 uses D12.1'; T4 uses FC05; T8 uses FC34; T7 uses D3.2. The formal core after round 2 must carry these ids.
- Shared lines outside area 1 not changed here: L233 ("alone", M3-B4), L325 (G1-B1), L339 (absence), L405, L409, L427, L481 (H09), L526 (E03), L220-L225 wording (none changed), L255 (G4-B8), L257, L315.
- L223's "the failure is not surprise" now follows from D12.1' (FC81 (d)); L411 says what T9 says.
