# S108 Part A - section 4 - variants computed

*Computing agent for section 4 (rule 5 of `S108 Part A - how the replies will be read, written before sending.md`), Opus 5.5, 28 September 2026. Fresh. Works only in `S108 Part A - computation/section 4 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`). Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: in progress, 28 September 2026. Filled as it goes; nothing ruled.

## 0. Setup

| item | state |
|---|---|
| copy | `S108 Part A - computation/section 4 model/` = program after round 4, 26 files, every file md5-identical at the copy |
| switch | `model/s108_s4.py`: `S108_S4_VARIANT` (none default; V4.1–V4.8) and the sub-choices `S108_S4_V41_SUFF`, `S108_S4_V41_Q`, `S108_S4_V42_SUFF`, `S108_S4_V43_READ` (§2); read by `claims_s41` (suff_defeats, USES_READING, FC30.new1 (c)), `claims_s106` (FC23.new2 (f)), `claims_b` (FC80's Underdet witness; D18.1's graph DEP) |
| new code | `model/s108_s4_nec.py` ((Nec)'s exposure: a search for faithful transports, V4.5); scripts `s108_s4_suite.py`, `s108_s4_compare.py`, `s108_s4_cases.py`, `s108_s4_scripts_expl.py`, `s108_s4_worlds.py` |
| default unchanged | under none the three case scripts print byte for byte the committed printouts (86a67664…, d473944e…, 043aeb36…) |
| runs | PYTHONHASHSEED=0, `timeout` on every run; suite at scale 4, cap 45; outputs in `S108 Part A - computation/section 4 runs/` |
| in scope | V4.1–V4.8, all eight (tabulation §6 flags no section-4 variant) |

## 1. The variants and how each is implemented (tabulation §2; the reply read whole)

| id | item varied | as the reply writes it | implemented as | as written? |
|---|---|---|---|---|
| V4.1 | D16.XV, the rule on Expl | + Acc(ℰ) ∧ Slot_C(ℰ) ⇒ ¬Expl(ℰ); Expl :⟺ Acc ∧ ¬Dec ∧ ¬Slot (D6.3, 'every') | `s108_s4.expl`: Acc ∧ ¬Dec(t) ∧ ¬Slot_C(ℰ), Slot_C(ℰ) := some component of E is a slot (¬NC1, `core.slot`); (Suff)'s shape kept (default) or co-varied | yes; the (Suff) shape is not stated by the reply: S108-4-I1 |
| V4.2 | D16.XV, the rule on Expl | rule deleted: Expl :⟺ Acc | `s108_s4.expl` = Acc; (Suff)'s shapes: 'rule' (default, as written), 'L17', 'both' | yes; the reply's trace reads L17 with it: S108-4-I2 |
| V4.3 | D16.XV, (Suff)'s shape and being an explanation | ¬Dec(t) → ¬Dec(t) ∧ (Sel(t) ∨ CT(t)), in both | `s108_s4.expl`, `suff_antecedent`: Acc ∧ ¬Dec ∧ (Sel ∨ CT) read at the holding | nearest statable: "Sel(t) ∨ CT(t)" names no holding; D12.3's Dec is already ¬Sel ∧ ¬Con at every holding not reached by a transfer, so V4.3 as written is now's reading unless read at the holding (S108-4-I3) |
| V4.4 | D16.XV, Uses(α) | 'not using (E)' at the instance: Acc(ℰ) ∉ Uses(α) | `claims_s41.USES_READING` = "instance" (the program's own reading before round 4, kept by I196) | yes |
| V4.5 | D16.XV, (Nec)'s shape (L538) | ∀C′ on D ∀t′ ¬Faithful_{C′}(t′) → ∀t′ ¬Faithful_C(t′) | `model/s108_s4_nec.py`: exposure now and under V4.5 by a search for faithful transports | nearest statable: "∀t′" is over every transport D → E; the search covers a stated class (S108-4-I5) |
| V4.6 | D16.4, 𝔈_Θ | drop "δ the designation of Q in c" | Acc under every port of E as δ against the designated δ (I20's default from t, I183's other choice: S108-4-I6) | nearest statable: 𝔈_Θ quantifies over every (p, t, Γ, δ); computed on the witnesses the cases and the generator build |
| V4.7 | D16.3, Enable | drop NQB | **cannot be implemented as written**: the program builds no χ, no realization witnessing Can, no Enable, UU, UC or UECS (FC94, FC110 not tested). Nearest statable reading: a finite toy with Rep and relayed provenance from `prov_fixed_points` (S108-4-I7); D18.1's graph with Enable's edges to (R) and β removed | no: S108-4-I7 |
| V4.8 | D12.9, Underdet; (Prov)(i) in D16.XV | Underdet without surv; (Prov)(i)'s middle conjunct → Underdet | `s108_s4.underdet_members` (FC80's witness reads every member); (Prov)(i) computed on populations (s108_s4_cases §3, s108_s4_worlds `pops`) | yes; "a function of (𝒯,H)" read as FC80 (b) reads it: S108-4-I8 |

D18.1's graph (the program's `claims_b.DEP`) co-varies with each definition changed (`s108_s4.dep_patch`): V4.1 DefeatConds + Slot; V4.3 DefeatConds + CT; V4.7 Enable − (R), β; V4.8 Underdet − surv; V4.2 'both' DefeatConds − Dec.

## 2. Inventions this computation made (S36)

| id | where | chosen | other choices (computed where marked) |
|---|---|---|---|
| S108-4-I1 | V4.1 | Slot under 'every' (the reply's); (Suff)'s antecedent kept as D16.XV writes it | Slot under 'some', 'some-exempt', 'some-exempt-set' (computed on every case, §3–§5); (Suff) co-varied, antecedent Acc ∧ ¬Dec ∧ ¬Slot (computed: suite, §7) |
| S108-4-I2 | V4.2 | 'rule': only Acc ∧ Dec ⇒ ¬Expl deleted; (Suff)'s shapes (L536, L17 as S41 writes it) keep ¬Dec(t) | 'L17': L17's antecedent follows being an explanation (Acc), L536 keeps ¬Dec (the reply's trace); 'both': L17 and L536 lose ¬Dec (computed: suite, §7) |
| S108-4-I3 | V4.3 | (a) Sel(t) ∨ CT(t) at the holding (t, o_t), on its own history: Sel's conditions with their exclusions at o_t, CT := a construction trace prepares t's holding at o_t (the program's trace[o_t]) | (b) CT := a trace's output holds t at o_t or at a holding o_t was transferred from; (c) through D12.3's inherited provenance: then V4.3 is now's reading (computed: 0 exceptions, §5) |
| S108-4-I4 | V4.4 | the rival's Acc(ℰ′) and 'Acc(ℰ′) → ¬Expl(ℰ)' taken as given by j (declared inputs, L522), as FC30.new1 (h) | – |
| S108-4-I5 | V4.5 | the class of transports searched: σ any map; τ any map on the closure of C's edits meeting Hom (I84); π any function on the solutions (D5.1 as written); λ(k): N_k ⊆ J_D nonempty, θ_k injective onto ports of the same domain, κ the identity. "C′ on D": every contract (a set of pairs holding some (1,b)); by per-pair (F1), (F2eq) and Hom of a restriction, now's exposure is "no t′ faithful on {(1,b)} for any b" | value maps between different domains (not searched): a witness there would make a V4.5-exposed case not exposed; only declared contracts of the question as C′ (the reply's other choice) |
| S108-4-I6 | V4.6 | "the designation of Q in c" := the ports of E whose translation reads exactly δ_D (I20's default from t; port queries only) | δ supplied with c (as D9.10); for non-port queries (the fibre query, E6) not computed |
| S108-4-I7 | V4.7 | the toy of `s108_s4_worlds.py toy`: χ1, χ2 admitted or not, 0–2 witnessing realizations each, over three occurrences; Rep(o,c) and "relayed from outside β" from provenance chains (T′); Can := some witnessing realization; UU := ∃χ Enable ∧ Can | none recorded; the program has no (CT1), Can or task |
| S108-4-I8 | V4.8 | value_t(a,b) "a function of (𝒯,H)" := every member of 𝒯 surviving on H has one value at (a,b) (FC80 (b)); Sel(t) on H by hand (H occurred, admitted, no Rep, no trace) | – |
| S108-4-I9 | all | provenance by hand (I90) on every worked case and generated candidate: H0 (no occurrence), Dec, Con, Sel (`provenance_of`), rCon, rSel (a relay of a constructed or selected holding, chains under T′, Held at o1 := Faithful_C(t)) | the program's own cases carry no history but the student's copy, the bridge, CT8 |

## 3. The worked cases (rule 5.1): Acc, Account ∧ ¬Dec(t) and being an explanation, off and on

Run: `s108_s4_cases.py` → `section 4 runs/cases.txt`. The 27 candidates of the written-in step's script (collected from `s106_cases.py`, its `case` function replaced by a collector), E6's Leibniz candidate (c-i) as FC63 builds it, and the student's copy's candidate (FC30.new1's pole, θ at 45): 29. Provenance by hand six ways (S108-4-I9).

**Acc and Account ∧ ¬Dec(t): no variant moves either on any worked case.** `core.account` and the provenance functions read no switch; the written-in step's script prints under every variant byte for byte what it prints under none (§6). What moves is being an explanation, which V4.1–V4.3 redefine (now: Account ∧ ¬Dec(t); V4.1: ∧ ¬Slot; V4.2: Account; V4.3: ∧ (Sel ∨ CT) at the holding).

| history (Θ by hand) | Dec(t) on the 29 | being an explanation moves: V4.1 | V4.2 | V4.3 (a) | V4.3 (b) |
|---|---|---|---|---|---|
| H0: no occurrence (the reply's "no record") | 29 | 0 | 24 (every Acc-T case) | 0 | 0 |
| Dec | 29 | 0 | 24 | 0 | 0 |
| Con | 0 | 10 | 0 | 0 | 0 |
| Sel on {(1,b0)} | 2 (τ′ on C1, the relabelings: Faithful_H fails) | 10 | 0 | 0 | 0 |
| rCon: relay of a constructed holding | 5 (Acc F: no Held at o1) | 10 | 0 | 24 | 0 |
| rSel: relay of a selected holding | 2 | 10 | 0 | 24 | 24 |

- **V4.1 moves 10 cases, all T → F, all with a slot under 'every'**: E_enc on the pole's C1 and C2; E_rev under τ′ on C_H (slot r_L); "p because p" (L273); M1, M2, M3 (the readers' lookups); the hand-turned vane (R3-Q1); **the owner's one-part sign (S44)**; E8's identity candidate (slot 'base'). Unchanged under 'every': the pole's forward candidate on C1, C2, C3, M5, M13 (the weathervane), E5 both, E9 both, E6, **the owner's two-part sign**, the day-port sign, E_rev on C_id (fibre query: no slot, I82). Under 'some' the pole on C2 and C3 (c_L), M5, E5's FC62 encoding (k_rest) and the two-part sign also move (§4).
- **V4.2 moves every Acc-T case under a declared or unrecorded history (24 of 24), F → T**; none under Con, Sel, relays.
- **V4.3 moves nothing at a holding not reached by a transfer**: with no record (H0) Dec(t) holds (D12.3: no parameters give Sel, none give Con), so no case is an explanation now either; Con and Sel give Sel ∨ CT. It moves only relayed copies: (a) of constructed and of selected holdings (24 + 24), (b) of selected holdings only (24).
- V4.4–V4.8 read nothing being an explanation reads (`s108_s4.expl` equals now's on all four values of (Acc, Dec) for each).

**The student's copy and its neighbours** (FC30.new1 (d)–(f), provenance computed on the chain, T′):

| case | provenance | Expl: now / V4.1 / V4.2 / V4.3 (a) / (b) |
|---|---|---|
| (d) the student's declared holding (source constructed, no trace at o2) | [{o1: Con}]: Dec at o2 | F / F / **T** / F / F |
| (f) K3's reading: the component alone, transferred from o1 | [{o1: Con, o2: Con}] (inherited) | T / T / T / **F** / T |
| (e) a link no pair tried, D12.1 with H ≠ ∅ | Dec | F / F / **T** / F / F |
| (e) the same, D12.1 after round 2 (H = ∅ allowed) | Sel | T / T / T / T / T |

- The bridge (FC84.new1): no candidate and no (E) is built; Con and Build read hand-set labels. No variant reaches it (FC84.new1 moves in no suite run, §7).
- E2, E3, E4, E7, the route examples: no candidate's (E) computed; none of their claims moves (§7).

## 4. The reply's small cases, run (every "after" was marked not run by the reply)

Run: `s108_s4_cases.py` §3 (`cases.txt`).

| variant | case | the reply's "after" | computed | standing |
|---|---|---|---|---|
| V4.1 | ℰ_one (sign, one part), constructed | stops being an explanation | slot k under all four readings; Expl T → F under all four | computed |
| V4.1 | ℰ_two (sign, two parts), constructed | remains | pins r, u (2); no slot under 'every': T → T; under some, some-exempt, some-exempt-set it is a slot: T → F | computed under 'every' (the reply's reading) only |
| V4.1 | E_enc, pole C1, C2 | stops | slot tab (7 and 15 pins): T → F under all four | computed |
| V4.1 | E_rev under τ′ on C_H | stops | slot r_L (4 pins): T → F under all four | computed |
| V4.1 | the pole's forward candidate on C1 | remains | no pin, no slot: T → T | computed |
| V4.1 | the pole's forward candidate on C2 ("8 pins by c_L") | stops | 8 pins by c_L, **no slot under 'every'** (pins only at the settings of L): T → T; F under 'some' only | **contradicted** under 'every'; holds under 'some' |
| V4.1 | "no candidate newly counts" | – | V4.1 only adds a conjunct: no F → T anywhere (29 cases, §5) | computed |
| V4.1 | (Suff) with ℰ_one constructed and an argument not using (E) ruling out Expl(ℰ_one) | not given | (Suff) kept: ℰ_one in the defeat set of L536 and L17, and "(Suff) as conjectured" (Acc ∧ ¬Dec ⇒ Expl) fails of ℰ_one by definition; co-varied: out of both defeat sets, (Suff) holds of it | **added** (S108-4-I1) |
| V4.2 | the student's declared copy (FC30.new1 (a), Dec) | an explanation | Acc T, Dec T: Expl F → T; the owner's condition Acc ∧ Dec ⇒ ¬Expl fails | computed |
| V4.2 | FC30.new1 (b): Def(L17, S41) = Def(L536) | fails unless L536's "provenance not declared" goes too | 'rule' (as written): holds (L17 F, L536 F); 'L17': **fails** (L17 T, L536 F); 'both': holds, and the declared copy is in both defeat sets ("before: defeats neither") | computed under the reply's trace reading ('L17'); under 'rule' contradicted |
| V4.3 | E_enc (pole C1) with no provenance record | stops being an explanation | H0: Dec T now: Expl F now and under V4.3 (no move); Con, Sel: T both; rCon: T → F (a), T (b); rSel: T → F (a), (b) | **contradicted** for "no record"; V4.3 moves relayed copies only |
| V4.3 | E_rev under τ′ on C_H, no record | stops | the same pattern as E_enc | contradicted for "no record" |
| V4.3 | E9's t1 (Con), a selected t0 | unaffected | t1 Con, Sel: T both; t1 relayed from a constructed holding: T → F (a), T (b) | computed (for Con, Sel) |
| V4.4 | FC30.new1 (h): [Acc(ℰ_rev), Acc(ℰ_rev) → ¬Expl(ℰ_fwd)] | ℰ_fwd enters (Suff)'s defeat set | usable by j; ℰ_fwd constructed or selected: symbol F, instance **T**; declared: F both (¬Dec(t) of the antecedent) | computed |
| V4.4 | E9: [Acc(t1), Acc(t1) → ¬Expl(t1∘ψ)] (FC103.new1's pair) | not run | t1∘ψ constructed: Acc(t1) T, Acc(t1∘ψ) T; symbol F, instance **T** | computed |
| V4.4 | (Nec): [Acc(ℰ_fwd), Acc(ℰ_fwd) → Expl(ℰ_rev)] rules out ¬Expl(ℰ_rev) | not given | usable; not using (E): symbol F, instance T; the defeat also asks exposure: not exposed now, exposed under V4.5 (next rows) | **added** |
| V4.5 | E_rev under τ on C1 | ∀t′ ¬Faithful_C1 holds: exposed | Acc F, Faithful_C(t) F; now: not exposed (a faithful t′ on {(1,b1_30)}); V4.5: **exposed** (no t′ in the class S108-4-I5) | computed (over the class) |
| V4.5 | E_rev under τ′ on C1 | – | the same: not exposed now, exposed under V4.5 | computed (over the class) |
| V4.5 | E_rev under τ′ on C_H (FC27.new1 (d)) | "a faithful transport of E_rev exists on a contract on D" | Acc T: not exposed now or under V4.5 (τ′ itself, H settings carried to settings of L) | computed |
| V4.5 | E5, eliminative (FC62's encoding and the second) | "the same holds for the eliminative candidates" | Acc T, Faithful_C(t) T: not exposed now or under V4.5 | **contradicted** |
| V4.6 | the pole's forward candidate (θ ∈ {30,45,60}), C1 | only δ = L | Acc: δ_E = L T, H F, T F; designated L | computed |
| V4.6 | the pole with θ at 45 (FC30.new1's), C_H | – | Acc: δ_E = L T, **H T**, T F: a non-designated δ meets (E) there (L = H at θ = 45); the content is in 𝔈_Θ through δ = L anyway | **added** |
| V4.8 | FC80 (d)'s shape on the pole (θ at 45): 𝒯 = {t, t_ab,H}, t_ab,H altered at H's image and at (set(H=1), b1_45)'s | (Prov)(i) becomes satisfiable | Sel(t) on H T; t_ab,H does not survive on H; the survivors agree at (a,b); a differing survivor F, a differing member T: (Prov)(i) now **F**, under V4.8 **T** | computed |
| V4.8 | t altered at (τ(a),σ(b)) only | – | survives on H: now's middle conjunct holds and the value is no function of (𝒯,H): (Prov)(i) F both ways (FC80 (a)) | computed |
| V4.7 | – (no small case; "trace is formal") | UU, UC met more easily; UECS grows; RC untouched | the toy (§5): UU moves on 217 of 484 assignments, every move F → T; RC reads no Enable (D18.1) | computed on S108-4-I7 |

**(Nec)'s exposure on the worked cases** (V4.5; `section 4 runs/nec_worked.txt`; class S108-4-I5; a transport faithful on C is a witness in any class):

| | exposed now (∀C′ ∀t′ ¬Faithful_{C′}) | exposed under V4.5 (∀t′ ¬Faithful_C) |
|---|---|---|
| 24 cases whose own t is faithful on C (every Acc-T case, E_rev τ′ on C_H, E6, E9 both, E5 both) | no | no |
| E_rev under τ on C1; E_rev under τ′ on C1; E_tab on C1; E_tab on C2 | no (a transport faithful at one baseline pair exists) | **yes** |
| L257's contract of relabelings, τ(1) ≠ 1 (E's component k on (y, z), the target's one port y) | **yes**: θ_k must be injective (D5.1) and V_k has two ports, the target one, so no λ(k) exists at any pair: exact in D5.1's class | yes |

Now's exposure holds of one worked case (the relabelings); V4.5 adds four, all with Acc false. Being an explanation and Acc read no exposure: V4.5 moves neither.

## 5. The generated worlds at scale 4 (rule 5.4)

Run: `s108_s4_worlds.py` (outputs `section 4 runs/worlds.*.json`, witnesses written out in full). **cands**: gen_p_cand's stream with the kind recorded (G-surg or G-free target; E_enc-built 60%, random 20%, lookup 20%), 108 sizes of claims_a.SMALL × 160 = 17,280 models, seed 108401, sizes ascending (the first witness is the smallest found); provenance by hand on each (S108-4-I9). **pops**: FC80's populations (a base and three members, each altered at one pair), seed 108402, 9,930 models; **pops-wide**: the base's τ random half the time (as FC80 (d)'s step generator) and each member altered at one or two pairs, seed 108403, 9,768 models. **chains**: every provenance chain of 1–3 holdings (held, trace, Sel's conditions, each holding a transfer of an earlier one or not), cuts U, K, T, T′, every fixed point: 13,509 fixed points, 39,926 holdings. **toy**: V4.7 (S108-4-I7), 484 assignments. **graph**: D18.1's graph under each variant. No run reached a cap (the exposure search's 20 s cap: 0 stops).

**Acc and Account ∧ ¬Dec(t): 0 moves under every variant** (1,019 of the 17,280 candidates meet (E); no variant reads anything Acc or Dec reads).

**Being an explanation** (candidates whose value differs; one count per history):

| variant | H0 | Dec | Con | Sel | rCon | rSel | direction | per history, by kind (E_enc-built / lookup / random) | smallest witness (first found) |
|---|---|---|---|---|---|---|---|---|---|
| V4.1 ('every') | 0 | 0 | 941 | 941 | 941 | 941 | out | 816 / 120 / 5 | E_enc-built, G-free, ports 1, dom 1, comps 1, \|B\| 2, edits 0 (index 26) |
| V4.2 | 1,019 | 1,019 | 0 | 0 | 0 | 0 | in | 891 / 120 / 8 | the same model |
| V4.3 (a) | 0 | 0 | 0 | 0 | 1,019 | 1,019 | out | 891 / 120 / 8 | the same model |
| V4.3 (b) | 0 | 0 | 0 | 0 | 0 | 1,019 | out | 891 / 120 / 8 | the same model |

- Slots among the 1,019 Acc-T candidates: 'every' 941; 'some' 952; 'some-exempt' 849; 'some-exempt-set' 854. V4.1 takes out 941 (92%) of the generated candidates that meet (E) under a ¬Dec history: every E_enc-built (816 of 891) and lookup (120 of 120) candidate with a slot.
- V4.3 moves every Acc-T candidate exactly when its holding is a relay, and none otherwise (the chains: at 39,926 holdings, ¬Dec(t) without Sel or Con at a holding not reached by a transfer: 0). Chains: (a) moves 2,692 holdings (1,468 transfers of constructed holdings, 1,224 of selected), (b) 1,126 (transfers of selected holdings only); smallest: two holdings, o2 a relay of o1 (T′: held (1,0), trace (1,0) for Con; Sel's conditions at o1 for Sel).

**V4.4** ((Suff) and (Nec) defeat sets, with j taking Acc(ℰ′) and Acc(ℰ′) → ¬Expl(ℰ), or → Expl(ℰ), as given): (Suff) grows on 1,019 (Con), 1,019 (Sel), 0 (Dec): every Acc-T candidate with a transport not declared; (Nec) grows only where exposure holds too: on the 3,979 candidates exposed now (V4.4 alone; the argument is usable and uses only Acc(ℰ′)), and on 2,138 more with V4.5 on (all Acc F).

**V4.5** ((Nec)'s exposure; class S108-4-I5): exposed now 3,979; exposed under V4.5 6,117; **moves 2,138, all not exposed → exposed, all Acc F** (E_enc-built 840, lookup 753, random 545); smallest: ports 1, dom 1, comps 1, |B| 2, edits 0 (G-free). No candidate meeting (E) is exposed under either shape (its own t is faithful on C).

**V4.6** (Acc under every port of E as δ, against the designated δ, S108-4-I6): the generator's δ_E is the designated port on every port-query candidate; **1 candidate meets (E) only with a non-designated δ** (E_enc-built, G-surg, ports 2, dom 2, comps 2, |B| 2, edits 1, index 90: π the identity, δ_D = p0; Acc with δ_E = p0 F, with δ_E = p1 T); 334 meet it with the designated δ and also with another. So on the searched witnesses V4.6 lets one content into 𝔈_Θ that the designation clause keeps out (unless another witness admits it: not computed).

**V4.7** (the toy): UU moves on 217 of 484 assignments, every move F → T; with the barrier read as L495.s1 [FROZEN] words it (no admitted, non-question-begging χ with Can), "barrier ∧ UU" holds on 0 assignments now and on 217 under V4.7 (first: χ1 not admitted, χ2 admitted with one realization using a relayed copy of c).

**V4.8** (FC80's populations): Underdet and (Prov)(i) **move on none of FC80's own 9,930 populations** (one alteration per member and τ one-to-one: a member that differs at an unseen pair survives on H, so now's middle conjunct already holds and the value is no function of (𝒯,H)); on the wide populations **(Prov)(i) moves F → T in 1,647 of 9,768 models** (3,010 (t, (a,b)) occurrences: G-free 1,614, G-surg 1,396; Underdet the same), smallest: ports 1, dom 1, comps 1, |B| 1, edits 1 (G-surg: t and a member altered at H's image and at the unseen pair's; 4 members, 2 survivors). (Prov)(i) holds now: 0 (FC80 (a) computed again).

**D18.1's graph** (`worlds.graph.json`; ancestors under T′):

| variant | what moves in the graph |
|---|---|
| V4.1 | DefeatConds (D16.XV) gains Slot, and through it **ℓ (the grain)**, Cand, Transport; Slot is reached by DefeatConds only; (E)'s ancestors unchanged |
| V4.2 ('rule') | nothing |
| V4.3 | nothing (CT is already an ancestor of the defeat conditions, through Sel) |
| V4.4, V4.5, V4.6 | nothing (Uses, the exposure and 𝔈's δ are not nodes; 𝔈 reads δ through (E) already) |
| V4.7 | Enable loses (R), β and with them 24 ancestors; **UU, UC, UECS no longer reach Part IV's provenance** (Sel, Con, CT, Held, (R), surv, 𝒯pop, Episode); Enable is reached by UU, UC, UECS, Classes only, now and under V4.7 |
| V4.8 | Underdet loses surv; surv still reaches the defeat conditions through Sel |

## 6. The external examples FC-E1–FC-E5, the creative transport case CT1–CT8, and the written-in step's case script (rules 5.1–5.3)

Run: each script under `S108_S4_VARIANT=<v>`, output compared byte for byte with its output under none (= the committed printout): `section 4 runs/scripts/diffs.txt`. **All 24 runs (8 variants × 3 scripts) print exactly what they print under none** (md5 86a67664…, d473944e…, 043aeb36…): no printed value ((E), fidelity, (A), provenance or episode) moves under any section-4 variant.

Being an explanation on the candidates the scripts evaluate (`s108_s4_scripts_expl.py`, every candidate each script hands to `core.account` recorded; `section 4 runs/scripts_expl.txt`):

| script | candidates | meeting (E) | with a slot ('every') | V4.1 | V4.2 | V4.3 (a) | V4.3 (b) |
|---|---|---|---|---|---|---|---|
| FC-E1–FC-E5 | 12 | 7 (FC-E1's ℰ, its restrictions ℰ\|k, ℰ\|d,k, ℰ with d in the background; FC-E4's two readouts) | 0 | 0 | 7 under H0, 7 under Dec | 7 rCon, 7 rSel | 7 rSel |
| CT1–CT8 | 775 | 4 (CT1's E_EQ,EQ; CT2's two pairs; CT5's E_direct) | 0 | 0 | 4 + 4 | 4 + 4 | 4 |

CT8 (the run's own provenance, the script's five readings under T′): R1, R3, R5 constructed → an explanation under now and every variant; **R2, R4 (Build's primitives not met) declared → an explanation under V4.2 only**.
