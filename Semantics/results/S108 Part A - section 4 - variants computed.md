# S108 Part A - section 4 - variants computed

*Computing agent for section 4 (rule 5 of `S108 Part A - how the replies will be read, written before sending.md`), Opus 5.5, 28 September 2026. Fresh. Works only in `S108 Part A - computation/section 4 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`). Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: complete, 28 September 2026. Filled as it went; nothing ruled.

## 0. Setup

| item | state |
|---|---|
| copy | `S108 Part A - computation/section 4 model/` = program after round 4, 26 files, every file md5-identical at the copy |
| switch | `model/s108_s4.py`: `S108_S4_VARIANT` (none default; V4.1–V4.8) and the sub-choices `S108_S4_V41_SUFF`, `S108_S4_V41_Q`, `S108_S4_V42_SUFF`, `S108_S4_V43_READ` (§2); read by `claims_s41` (suff_defeats, USES_READING, FC30.new1 (c)), `claims_s106` (FC23.new2 (f)), `claims_b` (FC80's Underdet witness; D18.1's graph DEP) |
| changed and new code | changed: `model/claims_s41.py`, `model/claims_s106.py`, `model/claims_b.py` (each change reads the switch; under none every path is round 4's); new: `model/s108_s4.py`, `model/s108_s4_nec.py` ((Nec)'s exposure: a search for faithful transports, V4.5); scripts `s108_s4_suite.py`, `s108_s4_compare.py`, `s108_s4_cases.py`, `s108_s4_scripts_expl.py`, `s108_s4_worlds.py`, `s108_s4_bij.py`, `s108_s4_edges.py` (writes the `.json`) |
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
| S108-4-I7 | V4.7 | the toy of `s108_s4_worlds.py toy`: χ1, χ2 admitted or not, 0–2 witnessing realizations each, over four occurrences (a holding built inside β, a relay of a constructed and of a selected holding outside β, no holding); Rep(o,c) and "relayed from outside β" from provenance chains (T′); Can := some witnessing realization; UU := ∃χ Enable ∧ Can | none recorded; the program has no (CT1), Can or task |
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
| V4.4 | (Nec): [Acc(ℰ_fwd), Acc(ℰ_fwd) → Expl(ℰ_rev)] rules out ¬Expl(ℰ_rev) | not given | usable; not using (E): symbol F, instance T (the argument reads names only). The defeat also asks exposure: on the full pole's C1 E_rev is exposed under V4.5 only (next rows), so (Nec) is defeated by it only with V4.4 and V4.5 both on; on FC30.new1's pole (θ at 45, C = baseline and settings of H) E_rev is exposed under neither (a transport carrying set(H=h) to set(L=h) is faithful there) | **added** |
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
| 24 cases whose own t is faithful on C (every case meeting (E): the pole's forward candidate, E_rev τ′ on C_H and on C_id, E_enc, the lookups, the signs, E5, E6, E8, E9, …) | no | no |
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

- Slots among the 1,019 Acc-T candidates: 'every' 941; 'some' 952; 'some-exempt' 849; 'some-exempt-set' 854. V4.1 takes out 941 of the 1,019 generated candidates that meet (E), under each ¬Dec history: those with a slot, 816 of the 891 E_enc-built, 120 of the 120 lookups, 5 of the 8 random.
- V4.3 moves every Acc-T candidate exactly when its holding is a relay, and none otherwise (the chains: at 39,926 holdings, ¬Dec(t) without Sel or Con at a holding not reached by a transfer: 0). Chains: (a) moves 2,692 holdings (1,468 transfers of constructed holdings, 1,224 of selected), (b) 1,126 (transfers of selected holdings only); smallest: two holdings, o2 a relay of o1 (T′: held (1,0), trace (1,0) for Con; Sel's conditions at o1 for Sel).

**MID** (claims_a.MID: domains up to 3, 162 sizes × 160 = 25,920 models, seed 108405, `worlds.cands-mid.json`; the exposure search of V4.5 not run there, `S108_S4_NO_NEC=1`): 1,686 meet (E); being an explanation moves as on SMALL: V4.1 out 1,590 per ¬Dec history (E_enc-built 1,344, lookup 228, random 18; slots 'every' 1,590, 'some' 1,617, 'some-exempt' 1,361, 'some-exempt-set' 1,385); V4.2 in 1,686 under H0 and Dec; V4.3 (a) out 1,686 per relay history, (b) 1,686 (rSel); V4.4 (Suff) 1,686 (Con), 1,686 (Sel); V4.6: 2 candidates meet (E) only with a non-designated δ (E_enc-built; smallest ports 2, dom 3, comps 2, |B| 2, edits 1), 355 with the designated δ and another.

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

## 7. The whole suite with each variant on (rule 5, last clause)

Run: `s108_s4_suite.py` under `S108_S4_VARIANT=<v>` (and the sub-choices), scale 4, cap 45, PYTHONHASHSEED=0, two at a time beside section 3's runs (load 6–9 on four CPUs); compared with the run under none by `s108_s4_compare.py` (status per claim; per part the status and the counterexample/witness/result text; model counts and timings not compared). Under none: **133 hold, 2 counterexamples (FC23, FC63), 7 not tested of 142, every claim's status as the committed printout**. Comparisons in full: `section 4 runs/suite/compare.<v>.txt`.

| reading | claims whose status moves | parts that move (status or text) | statuses under it |
|---|---|---|---|
| V4.1, (Suff) kept (as written) | 1: FC30.new1 | (c) holds → **fails by construction** at (Acc T, Dec F, Slot T) | 132 / 3 / 7 |
| V4.1, (Suff) co-varied | 2: FC30.new1, FC23.new2 | FC30.new1 (b) **counterexample**: Def(L17 as text 104) ≠ Def(L536) ∪ {declared}, smallest ports 1, dom 1, comps 1, \|B\| 1, edits 1 (a one-component lookup with a slot, constructed); (c) holds (text: checked on the 8 values of (Acc, Dec, Slot)); FC23.new2 (f) **not as claimed**: ℰ_one constructed or selected leaves (Suff)'s defeat set | 131 / 4 / 7 |
| V4.2, 'rule' (as written) | 2: FC30.new1, FC23.new2 | FC30.new1 (c) **fails by construction** at (Acc T, Dec T) (the owner's condition); FC23.new2 (f) **not as claimed** (ℰ_two, ℰ_one declared: Expl T) | 131 / 4 / 7 |
| V4.2, 'L17' (the reply's trace) | 2: FC30.new1, FC23.new2 | FC30.new1 (a), (d), (e) **not as claimed** (the declared copy and the link no pair tried are in Def(L17), not in Def(L536)); (b) **counterexample** (Def(L17, S41) ≠ Def(L536)); (c) **fails by construction**; FC23.new2 (f) **not as claimed** | 131 / 4 / 7 |
| V4.2, 'both' | 2: FC30.new1, FC23.new2 | FC30.new1 (a), (d), (e) **not as claimed** (the declared copy in both defeat sets); (b) holds (one defeat set again); (c) **fails by construction**; FC23.new2 (f) **not as claimed** | 131 / 4 / 7 |
| V4.3 (holding) | 0 | FC30.new1 (c) text only (checked on the 8 values of (Acc, Dec, Sel ∨ CT); holds) | 133 / 2 / 7 |
| V4.4 | 0 | none | 133 / 2 / 7 |
| V4.5 | 0 | none (no claim reads the switch for V4.5; FC30.new1 (g)'s (Nec) reads Faithful_C(t), which holds of its candidate: not exposed under either shape) | 133 / 2 / 7 |
| V4.6 | 0 | none (no claim computes 𝔈_Θ: FC94, FC110 not tested; FC90.new1 (c) reads Acc under two δ and does not move) | 133 / 2 / 7 |
| V4.7 | 0 | none (D18.1's DEP changes; no claim reading DEP moves: FC32, FC32.new1, FC98, FC98.new2) | 133 / 2 / 7 |
| V4.8 | 0 | FC80 (a) underdetermination: witness text only (the same model and pair; the witness now counts members, 4, of which 2 survive) | 133 / 2 / 7 |

- **Across all twelve runs only four claims move at all**: FC30.new1 and FC23.new2 (V4.1, V4.2, V4.3's text), FC80 (V4.8, text), and FC23.new1 (c) (the cap, §7.1). **Not moved under any reading** (among those the reply names or the worked cases use): FC23.new3, FC25.new2, FC27.new1, FC30, FC62, FC80.new1, FC84.new1, FC90.new1, FC94 and FC110 (not tested), FC99, FC100, FC103.new1, FC12.new2, FC12.new3, FC83, FC32, FC32.new1, FC98, FC98.new2.
- FC30.new1 (a), (d)–(h) move under no reading of V4.1 (the student's candidate has no slot); FC30.new1 (g) ((Nec), L538) moves under none: its t is faithful on C, so it is not exposed under either shape (V4.5).

### 7.1 Parts that reached the 45 s cap

Under contention (section 3's runs on the same four CPUs) these parts reached the cap in some run: FC56 (a), (c) (under none and nine readings; not under V4.5, V4.6, which ran when the load had dropped), FC23.new1 (c) (V4.2, V4.3, V4.4, V4.8), FC43 (V4.2, V4.2 'L17', V4.3). FC23.new1 (c) is the one part whose result differs from none's in a run: "witness found" → "no witness found", the cap reached before the witness. None of the three claims reads any switch. Re-run alone at cap 300 under none and under every reading (`capped300.<v>.json`, `compare.capped300.txt`): no part reached the cap; under every reading every part's status and text equals none's (FC23.new1 (c) witness found, 45,308 models under none). So the caps hid nothing.

## 8. The edges (rule 5): the reply's, marked; and those the computation adds

Standing: **computed** (the computation shows it), **contradicted** (it shows otherwise), **not settled by computation** (with what would settle it); **added**: shown by the computation, not named by the reply. Marks are the template's. The reply's one "changes with" row for V4.1 is split by the item it names (E4.1b–f). Every row is in the `.json` beside this file (written by `s108_s4_edges.py`).

### V4.1

| id | kind | item [mark] | named by | standing | evidence / what would settle it |
|---|---|---|---|---|---|
| E4.1a | moves | Expl gains ¬Slot; D18.1's graph: Slot an ancestor of Expl/(Suff) [D18.1 S4; D16.XV S4] | reply | computed | graph recomputed: DefeatConds (D16.XV) gains Slot and through it ℓ, Cand, Transport; Expl stays an atom (a sink); Slot is reached by DefeatConds only; (E)'s ancestors unchanged. Being an explanation T → F on 10 of 29 worked cases, 941 of 1,019 generated Acc-T candidates (each ¬Dec history) |
| E4.1b | changes with | L17, L49, L61, L69 (Account(ℰ) ∧ ¬Dec(t) as being an explanation) [S1] | reply | computed | the formula they write parts from V4.1's being an explanation on 10 worked cases (ℰ_one, E_enc C1 and C2, E_rev τ′ on C_H, 'p because p', M1–M3, the hand-turned vane, E8's identity candidate) under Con, Sel and relay histories; L61's (Suff) fails by definition of ℰ_one (FC30.new1 (c), (Suff) kept) |
| E4.1c | changes with | the L267–L277 table ('a written-in answer never stops…') [L269–L277 S2 (L267 a heading)] | reply | contradicted | L269–L277 speak of (E), which V4.1 does not move (E_enc still meets (E): Acc unchanged on every case); the quoted row is the brief's summary of S44, S45 (brief line 90), not a line of the text; what it summarizes (S44, S45) is reversed on 10 worked cases (§9) |
| E4.1d | changes with | FC30.new1 [claim S1, S4] | reply | computed | (Suff) kept (as written): FC30.new1 (c) holds → fails by construction at (Acc T, Dec F, Slot T); (Suff) co-varied: (c) holds, (b)'s second identity (Def(L17 as text 104) = Def(L536) ∪ declared) fails on slot candidates (suite, §7) |
| E4.1e | changes with | FC23.new2 [claim (S44)] | reply | computed | (Suff) kept: no result moves ((f) checks the owner's condition, which V4.1 keeps); (Suff) co-varied: (f) moves (ℰ_one constructed leaves (Suff)'s defeat set) (§7) |
| E4.1f | changes with | FC23.new3, FC25.new2 [claims S2] | reply | contradicted | no result of either moves under V4.1 (suite, both sub-choices): they compute the Pin, Slot and Acc facts V4.1 reads, which V4.1 does not change |
| E4.1g | blocks | none FROZEN [-] | reply | computed | in D18.1 the only node gaining an edge is DefeatConds (D16.XV, S4); the claims that move (FC30.new1, FC23.new2) test S1/S4 lines and S44; no FROZEN definition reaches Slot. Frozen sentences are not read by the program (not searched beyond the graph) |
| E4.1h | changes with | ℓ, 'at the declared grain' (D6.3's NC1 words; I28) [D6.3 S2] | computation | **added** (computed) | under V4.1 ℓ becomes an ancestor of D16.XV's defeat conditions (graph); after S106 ℓ was an ancestor of no conjunct of (E) and of no defeat condition |
| E4.1i | changes with | D6.3's quantifier over Det_C (I136) [D6.3 S2] | computation | **added** (computed) | the owner's two-part sign stays an explanation under V4.1 only with 'every' (T, F, F, F under every / some / some-exempt / some-exempt-set); under 'some' the pole's forward candidate on C2 and C3, M5 and E5 (FC62's encoding) also stop; generated Acc-T with a slot: 941 / 952 / 849 / 854 |
| E4.1j | constrains | (Suff)'s shape (D16.XV; L61, L536) [D16.XV S4; L61 S1; L536 S4] | computation | **added** (computed) | with (Suff)'s antecedent kept, V4.1 makes (Suff) as conjectured fail by definition of every constructed or selected candidate with a slot (FC30.new1 (c) fails by construction; ℰ_one: 'holds of ℰ_one' F); only with the antecedent co-varied (Acc ∧ ¬Dec ∧ ¬Slot) do the two have a common model |
| E4.1k | moves | the pole's forward candidate on C2 ('8 pins by c_L') [E1 S2] | computation | **added** (computed) | the reply's trace has it stop being an explanation: under 'every' it has no slot (pins only at the settings of L) and stays (T → T); it stops only under 'some' (a correction of the reply's trace, recorded as an edge of the quantifier, E4.1i) |
| E4.1l | constrains | D18.2 (structure-preserving bijections; Argument 8) [D18.2 S4] | computation | **added** (computed) | the reply's (d) says V4.1 is safe: FC100's generator and bijections at scale 4 (12,960 port-query models, seed 108404): Slot under all four readings, the pins and Acc are kept by every bijection tried (0 exceptions), so V4.1's being an explanation is kept |

### V4.2

| id | kind | item [mark] | named by | standing | evidence / what would settle it |
|---|---|---|---|---|---|
| E4.2a | moves | Expl := Acc; being an explanation loses ¬Dec [D16.XV S4] | reply | computed | F → T on 24 of 29 worked cases under a declared or unrecorded history (every Acc-T case), the student's copy (FC30.new1 (d)), a link no pair tried (FC30.new1 (e)), CT8's R2 and R4, FC-E 7, CT 4, 1,019 of 1,019 generated Acc-T candidates |
| E4.2b | changes with | L17/L49/L61/L69; D16.XV (Suff) shape; FC30.new1 (the one-defeat-set identity (b)) [S1; D16.XV S4] | reply | computed | (b) breaks under the reply's trace reading (S108-4-I2 'L17': Def(L17) T, Def(L536) F for the declared copy; with (a), (c), (d), (e) of FC30.new1 and FC23.new2 (f)); as written ('rule') (b) holds and FC30.new1 (c) (the owner's condition) and FC23.new2 (f) fail instead; with 'both', (b) holds and (a), (c), (d), (e) fail: the declared copy is in both defeat sets (suite, §7) |
| E4.2c | constrains | FC30 ((E) takes no provenance) [claim S1, S2] | reply | computed | FC30 unchanged in the suite under V4.2 (every sub-choice); Acc unchanged on every case, script and generated candidate |
| E4.2d | blocks | the owner's condition Acc ∧ Dec ⇒ ¬Expl (S41 Q2), as FC30.new1 (c) and FC23.new2 (f) compute it [D16.XV S4 (owner S41)] | computation | **added** (computed) | FC30.new1 (c) fails by construction at (Acc T, Dec T); FC23.new2 (f) not as claimed (ℰ_two, ℰ_one declared are explanations) |
| E4.2e | moves | CT8's readings R2, R4 (Build's primitives not met) [CT8 (case)] | computation | **added** (computed) | the chosen pair's transport is declared under R2, R4 (T′): not an explanation now, an explanation under V4.2 only |

### V4.3

| id | kind | item [mark] | named by | standing | evidence / what would settle it |
|---|---|---|---|---|---|
| E4.3a | constrains | D12.3/D12.4, provenance per holding [D12.3 S2; D12.4 FROZEN] | reply | computed | a holding with no record is Dec (D12.3: no parameters give Sel, none give Con; H0: Dec on 29 of 29); at every holding not reached by a transfer ¬Dec(t) ⇔ Sel ∨ Con ⇒ Sel ∨ CT (chains: 0 exceptions in 39,926 holdings), so V4.3 is vacuous there; it bites only at transferred holdings, whose provenance D12.3's first clause and D12.4 [FROZEN] inherit |
| E4.3b | moves | Expl and (Suff)'s range [D16.XV S4] | reply | computed | only relayed or recorded copies move, T → F: (a) of constructed and selected holdings (worked cases 24 + 24; chains 2,692 holdings; generated 1,019 + 1,019), (b) of selected holdings only (24; 1,126; 1,019); no case with no record moves |
| E4.3c | changes with | L17 etc.; FC25.new2's reading ('the encoding table stops being an explanation') [S1; claim S2] | reply | contradicted | E_enc with no record is Dec now and under V4.3 (not an explanation either way); with Con or Sel it is one either way; it moves only as a relayed copy; FC25.new2 does not move (suite) |
| E4.3d | changes with | D12.4 (a transfer gives each part at o′ the value it had at o) [FROZEN] | computation | **added** (computed) | under V4.3 (a) an inherited Con or Sel no longer makes a transferred holding an explanation: FC30.new1 (f)'s K3 reading (the student's component transferred, Con inherited) T → F; E9's t1 relayed T → F; (b) keeps relays of constructed holdings |
| E4.3e | changes with | which holding CT(t) is read at (S108-4-I3) [D12.2 S2] | computation | **added** (computed) | (a) the holding itself: relays of constructed holdings move; (b) the holding or one it was transferred from: they do not; (c) through inherited provenance: V4.3 is now's reading (0 moves) |
| E4.3f | constrains | D18.2 (bijections carry occurrences; Argument 8) [D18.2 S4] | computation | **added** (not settled by computation) | the reply's (d): 'V4.3 is not obviously φ-invariant'; in the program's chains Sel, CT and transfers are fixed by ≺ and the transfer relation, which a structure-preserving bijection keeps, so V4.3 is kept there trivially; the program's histories are hand-set labels (I90); to settle: histories built by the program (Θ realized), with D18.2's bijections acting on occurrences, and V4.3 computed before and after |

### V4.4

| id | kind | item [mark] | named by | standing | evidence / what would settle it |
|---|---|---|---|---|---|
| E4.4a | constrains | X_j / Out_j (D9.x), assessor-relative [D9.6, D9.7 S3] | reply | computed | the defeat set grows only through X_j: for a j that takes Acc(ℰ′) and Acc(ℰ′) → ¬Expl(ℰ) as given (usable by modus ponens); the record argument (r, r → ¬Expl) is in it under both readings |
| E4.4b | moves | (Suff) and (Nec) defeat sets only [D16.XV S4] | reply | computed | (Suff): FC30.new1 (h)'s ℰ_fwd and E9's t1∘ψ enter (instance T, symbol F), declared ones do not; generated: 1,019 (Con), 1,019 (Sel); (Nec): 3,979 generated candidates exposed now enter; the full pole's E_rev on C1 only with V4.5 too (not exposed now); Acc and being an explanation: 0 moves; suite: 0 claims move |
| E4.4c | blocks | any FROZEN item (the reply's unsettled edge) [-] | reply | not settled by computation | a search of the template: no FROZEN sentence or definition holds 'not using' or Uses (the three that hold it, L17.n2, L536.s1, L538.s1, are middle: S1, S4, S4); the program has no node for Uses; to settle: a reading, not a run: whether citing a rival's being an account is 'using (E)' (the owner's gloss of argument, S23), as the reply says |
| E4.4d | changes with | V4.5 ((Nec)'s exposure) [D16.XV S4] | computation | **added** (computed) | for E_rev on the full pole's C1 both are needed: the rival-citing argument counts only at the instance (V4.4) and E_rev is exposed only on C alone (V4.5); on FC30.new1's pole (θ at 45) it is exposed under neither; generated: 2,138 candidates enter (Nec)'s defeat set with both on and not with V4.4 alone |

### V4.5

| id | kind | item [mark] | named by | standing | evidence / what would settle it |
|---|---|---|---|---|---|
| E4.5a | constrains | L606.s4 (Argument 7), FC99 [L606.s4 S4; claim S4] | reply | computed | FC99 unchanged (suite); now's exposure fails for 28 of 29 worked cases, each having a transport faithful at a single baseline pair (C′ = {(1,b)}; for 24 their own t is faithful on C), and for 3,979 of 17,280 generated candidates it holds: fidelity on some contract is cheap, the transport-level form of Argument 7's point |
| E4.5b | changes with | L538.s1 (co-varied); FC30.new1 (g); Part VII's exposure (E5) [L538.s1 S4; claim S1, S4; E5 FROZEN] | reply | contradicted | E5's two encodings meet (E), so their own t is faithful on C: exposed under neither shape (contradicted for E5); FC30.new1 (g) unchanged (t faithful); the widening is real elsewhere: E_rev under τ and τ′ on C1, E_tab on C1 and C2, 2,138 generated, all Acc F |
| E4.5c | moves | L538.s2 'Eliminative explanation (Part VII) is the exposed case' [L538.s2 S4] | computation | **added** (computed) | neither of E5's encodings [FROZEN] is exposed under now's shape or V4.5's; the one worked case exposed now is L257's contract of relabelings (no injective θ_k exists: exact in D5.1's class) |
| E4.5d | moves | (Nec)'s defeat set on the worked cases [D16.XV S4] | computation | **added** (computed) | exposed now: 1 of 29 (the relabelings); under V4.5: 5 (+ E_rev τ and τ′ on C1, E_tab C1 and C2); no candidate meeting (E) is exposed under either |

### V4.6

| id | kind | item [mark] | named by | standing | evidence / what would settle it |
|---|---|---|---|---|---|
| E4.6a | constrains | D5.3/I20 (designation) [D5.3 FROZEN] | reply | computed | (E) reads δ through (A) and Dependence: the pole on C1 meets (E) with δ = L only; FC90.new1 (c) unchanged |
| E4.6b | moves | 𝔈_Θ, UU, UECS; nothing in (E) [D16.4 S4] | reply | computed | on the searched witnesses: 1 of 17,280 generated candidates (SMALL) and 2 of 25,920 (MID) meet (E) only with a non-designated δ (so enter 𝔈_Θ through it under V4.6); 334 and 355 meet it with the designated δ and another; worked cases: none (on the pole with θ at 45, δ = H also meets (E), δ = L too); (E) unchanged; 𝔈's graph unchanged. Membership over every (p, t, Γ) not computed |
| E4.6c | changes with | the pole with θ at 45 (FC30.new1's target): L = H at every pair [E1 S2] | computation | **added** (computed) | the forward candidate meets (E) with δ_E = L and with δ_E = H: the designation clause separates witnesses there, not contents |

### V4.7

| id | kind | item [mark] | named by | standing | evidence / what would settle it |
|---|---|---|---|---|---|
| E4.7a | blocks | L495.s1 (barriers: 'every admitted, non-question-begging enabling condition leaves the relevant capability unavailable') [L495.s1 FROZEN] | reply | computed | on the toy (S108-4-I7, the only reading computable): with the barrier read as L495.s1's words have it, 'barrier ∧ UU' holds on 0 of 484 assignments now and on 217 under V4.7: the frozen barrier no longer excludes universality over the same content. The program computes no barrier, Enable or UU: on the program itself not settled; to settle: a (CT1)/Can model of tasks and realizations in the program; then Enable, UU and a barrier computed on it |
| E4.7b | moves | UECS only [D16.4 S4] | reply | computed | graph: Enable is reached by UU, UC, UECS and Classes only, now and under V4.7; (E), Dec, DefeatConds do not reach it; toy: UU moves F → T on 217 of 484; all 24 script runs and the suite: nothing moves |
| E4.7c | changes with | Part IV's provenance (Sel, Con, CT, Held, (R), surv, 𝒯pop) [D12.1–D12.5 S2/FROZEN] | computation | **added** (computed) | graph: under V4.7 Enable loses (R) and β, and UU, UC, UECS no longer reach any provenance node: universality stops reading provenance |
| E4.7d | changes with | the universal class (L528's membership sentences; D16.5's Universal) [L528.s1–s4 FROZEN; D16.5 S4] | computation | **added** (computed) | graph: Classes (D16.5) reaches Enable through UECS; the class's words are unchanged and its extension grows with UU (toy: UU F → T on 217 of 484) |

### V4.8

| id | kind | item [mark] | named by | standing | evidence / what would settle it |
|---|---|---|---|---|---|
| E4.8a | constrains | D12.1 surv; L574.s2 [D12.1 S2; L574.s2 FROZEN] | reply | computed | FC80 (d), (d′) (L574's step) and FC80.new1 unchanged under V4.8 (suite); surv still reaches the defeat conditions through Sel (graph) |
| E4.8b | moves | (Prov)(i) from closed by definition to open [D16.XV S4] | reply | computed | built on the pole: (Prov)(i) F now, T under V4.8; generated: 0 of FC80's own 9,930 populations, 1,647 of 9,768 wide ones (a member altered at an unseen pair's image and at H's, or τ×σ not one-to-one); now: 0 anywhere (FC80 (a)) |
| E4.8c | changes with | L572.s2, L574.n4, L576.s1, L576.s4 (co-varied) [S4] | reply | not settled by computation | the sentences are not read by the program; to settle: a reading of the four sentences against Underdet without surv |
| E4.8d | changes with | FC80 [claim S4] | reply | computed | FC80's underdetermination witness is read through D12.9 under V4.8 (every member); its status holds; its text moves (suite, §7) |
| E4.8e | blocks | D16.XV's note '(Prov)(i) unsatisfiable by definition (FC80 (a))' [D16.XV S4] | computation | **added** (computed) | satisfiable under V4.8 (the pole case; 1,647 generated models) |
| E4.8f | changes with | FC80's population generator (one alteration per member, τ one-to-one) [claim S4] | computation | **added** (computed) | on FC80's own populations V4.8 moves nothing: a differing member there differs at an unseen pair only, so it survives and now's conjunct already holds |

Counts: added / computed 17; added / not settled by computation 1; reply / computed 20; reply / contradicted 4; reply / not settled by computation 2; 44 rows.

## 9. What the computation says of each variant and the explanation definition (for the map; nothing ruled)

(E) itself is untouched by every section-4 variant: Acc moves nowhere (worked cases, scripts, 17,280 generated candidates, the suite). Account ∧ ¬Dec(t) moves nowhere either. What moves is **being an explanation** (V4.1–V4.3, which redefine it) or what surrounds it (V4.4–V4.8).

| variant | which candidates meet (E) | being an explanation | what else moves | owner's decisions the computed effect sits against (named, not ruled; rule 13) |
|---|---|---|---|---|
| V4.1 | unchanged | **out**: every candidate meeting (E) with a slot under 'every' and a transport not declared: 10 of 29 worked cases (the owner's one-part sign, E_enc, "p because p", the lookups M1–M3, the hand-turned vane, E8's identity candidate, E_rev under τ′ on C_H), 941 of 1,019 generated; the owner's two-part sign stays under 'every' only | (Suff) fails by definition unless its antecedent co-varies (FC30.new1 (c)); D18.1: the grain ℓ becomes an ancestor of the defeat conditions | **S45** ("Yes, take the test out": a written-in answer never stops a candidate being an explanation): reversed on 10 worked cases; **S44** ("In either case, it is an explanation"): the one-part sign stops being one; the two-part sign stays under 'every', not under the other three readings |
| V4.2 | unchanged | **in**: every candidate meeting (E) whose transport is declared or unrecorded: 24 of 29 worked cases under such a history, the student's declared copy, a link no pair tried, CT8's R2 and R4, FC-E 7, CT 4, 1,019 generated | FC30.new1 (c) and FC23.new2 (f) fail (the owner's condition); FC30.new1 (b) under the reply's reading 'L17' | **S41 Q2** ("No, not if just declared"): the student's declared copy (FC30.new1 (d)) becomes an explanation |
| V4.3 | unchanged | **out**, only at transferred holdings: relays or records of selected holdings (readings a, b) and of constructed ones (a): the student's component under K3's reading, E9's relayed t1, 24 + 24 worked (history, case) pairs, 1,019 generated per relay history; nothing with no record moves (it is Dec now) | D12.4's inherited provenance no longer suffices for being an explanation | none named by the reply; none computed |
| V4.4 | unchanged | unchanged | (Suff)'s defeat set: every constructed or selected candidate meeting (E), for a j who takes a rival's Acc as given (1,019 + 1,019 generated; FC30.new1 (h)'s ℰ_fwd; E9's t1∘ψ); (Nec)'s: 3,979 generated exposed now | none computed (the reply names a tension with S23's gloss of argument, a reading) |
| V4.5 | unchanged | unchanged | (Nec)'s exposure: +4 worked cases, +2,138 generated, all not meeting (E); E5 exposed under neither shape | none |
| V4.6 | unchanged | unchanged | 𝔈_Θ: +1 of 17,280 (SMALL) and +2 of 25,920 (MID) searched witnesses (each meets (E) only with a non-designated δ) | none |
| V4.7 | unchanged | unchanged | (toy) UU F → T on 217 of 484; barrier ∧ UU on 217 (0 now); D18.1: UU, UC, UECS stop reading provenance | none (V4.7 stays inside the physical module, where S25–S27 place physical possibility) |
| V4.8 | unchanged | unchanged | (Prov)(i) satisfiable: the pole case, 1,647 wide generated models; 0 on FC80's own populations | none |

**Discovered candidate definitions of explanation (rule 7, for the map's agent):** V4.1 (Account ∧ ¬Dec(t) ∧ ¬Slot), V4.2 (Account), V4.3 (Account ∧ ¬Dec(t) ∧ (Sel ∨ CT) at the holding). Each changes which candidates count as explanations (computed above); none changes which meet (E). V4.4–V4.8 change neither.

## 10. Unsure

- Provenance on every worked case and generated candidate is set by hand (S108-4-I9, I90), as the program's own claims set it; no worked case carries a history of its own except the student's copy, the bridge and CT8. Which history a case "has" is not computed; the tables give each.
- V4.3's effect rests on which holding "Sel(t) ∨ CT(t)" is read at (S108-4-I3): read through D12.3's inherited provenance it is now's reading at every holding (computed: 0 exceptions); read at the holding it moves transferred copies only.
- V4.5's "exposed" is over the class S108-4-I5 (no value maps between different domains); a transport outside it faithful on C1 would take E_rev on C1 out of V4.5's exposed set. Now's "not exposed" is exact (a witness).
- V4.6's reach is over the witnesses the cases and the generator build; membership of a content in 𝔈_Θ quantifies over every question and transport and is not computed.
- V4.7 is computed only on a toy (S108-4-I7); the program has no (CT1), Can, task or realization.
- V4.1's and V4.2's effects on (Suff) depend on the sub-choices S108-4-I1, I2; each is computed (§7).
- The whole-suite runs shared four CPUs with section 3's runs (load 7–9); parts that reached the 45 s cap are listed and re-run (§7.1).
- "Smallest witness" is the first found in ascending size order, as the harness takes it, not a minimum over all models.
- Quotation compared (rule 14): the reply's V4.1 row "a written-in answer never stops…" is the brief's summary of S44 and S45 (brief line 90), not a line of L267–L277; the text's L269–L277 speak of (E), which V4.1 does not move.
- Silence is not agreement (rule 3): items no variant of section 4 varied (D16.5, E9, D18.1 and D18.2 themselves, (Elim), (QF)) are not shown free of dependencies; D18.1 was recomputed under each variant (§5) and D18.2 checked only for V4.1 (E4.1l).

Computed by one Opus 5.5 agent under rule 5, 28 September 2026. Nothing here changes the theory's text, formal core, claims or program after round 4 (rule 11).
