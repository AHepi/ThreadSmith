# S108 Part A - section 3 - variants computed

*Computing agent for section 3 (rule 5 of `S108 Part A - how the replies will be read, written before sending.md`), Opus 5.5, 28 September 2026. Fresh. Works only in `S108 Part A - computation/section 3 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`). Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: in progress, 28 September 2026. Filled as it goes; nothing ruled.

## 0. Setup

| item | state |
|---|---|
| copy | `S108 Part A - computation/section 3 model/` = program after round 4, 26 files, every file md5-identical at the copy |
| switches | `model/s108s3.py`: `S108_S3_VARIANT` ("none" default; V3.1–V3.8); `S108_S3_CT` for V3.4 only ("prepares" default = D12.2 as written; "build" = the reply's chain, S108-3-I2). Read at: `args.rules_out` (V3.1), `args.usable_step` and `usable_any_step` (V3.2), `args.usable` (V3.3), `claims_b.build_at`, `_con_at`, `con`, FC90.new1 (a) (V3.4), `claims_b.episode` (V3.5), `claims_b.sel` via `s108s3.in_population` (V3.6), `phys.act_route` (V3.7), FC84.new1 (a4) via `s108s3.create_ex` (V3.8); D18.1's graph `claims_b.DEP` follows each variant's right-hand side (`s108_s3_dep`) |
| default unchanged | under "none" the three case scripts print byte for byte the committed printouts: md5 86a67664a9a3584351fd4836a4140b69 (external), d473944e74d2f349b1fdfb83277843cf (creative transport), 043aeb3647a9004ae43009a7fed50b4e (written-in step), as the rule gives |
| scripts (in the copy) | `s108_s3_suite.py`, `s108_s3_compare.py`, `s108_s3_run_suites.sh` (whole suite), `s108_s3_cases.py` (worked cases, histories, the reply's small cases), `s108_s3_worlds.py` (generated worlds) |
| runs | PYTHONHASHSEED=0, `timeout` on every run; suite at scale 4, time cap 45 (the printout's settings); outputs in `S108 Part A - computation/section 3 runs/` |

## 1. Which variants are implemented (the tabulation, §1 and §6: no section-3 variant flagged)

| id | item | kind | implemented | how (the copy) | as written? |
|---|---|---|---|---|---|
| V3.1 | D9.7 (RO) | delete | yes | `rules_out`: Incons(φ, concl(α)) alone | yes |
| V3.2 | D9.4 (Live) | delete | yes | `usable_step`: Live := d ∈ Accepted; also in `usable_any_step` (I40's other reading, FC69) | yes (applied to both readings of "below": the variant removes the step disjunct itself) |
| V3.3 | D9.6 (Usable, premise alone) | delete | yes | `usable`: a premise alone (no step) usable by every j | yes |
| V3.4 | D13.3 (ExplUse) | strengthen | yes | `s108s3.expl_use(uses, acc)`: UsesClaim ∧ Acc(ℰ); `build_at(…, explu)`; FC90.new1 (a) reads D13.3 through it | yes for Build; the reply's step Build → CT → Con is not D12.2 as written (CT reads Prepares, not ExplUse; DEP: CT → h, Prepares, BindingConstruction): computed both ways, S108-3-I2 |
| V3.5 | D13.8 (Episode) | delete | yes | `episode`: the record clause skipped (both the S41 and the L55 readings) | yes |
| V3.6 | D15.8 (𝒯) | delete | yes, nearest statable | `s108s3.in_population(admitted, parts, stated)`; `Hist(parts=, stated=)` | nearest: the program carries no parts(t) and no stated construction (I158 is registered, never computed); S108-3-I3, S108-3-I4 |
| V3.7 | D11.4 (ActRoute) | delete | yes | `act_route`: the ∃(x,x′) ∈ K conjunct skipped | yes |
| V3.8 | D14.7 ((EX)) | delete | yes | `s108s3.create_ex(cce, origin, rest)`; FC84.new1 (a4); DEP's (EX) loses its CCE edge | yes; (EX)'s own Origin conjunct (L448) kept |

## 2. Inventions this computation forced (S36)

| id | where | choice | other choice |
|---|---|---|---|
| S108-3-I1 | V3.4, cases with no ℰ built (the bridge, FC83's chains) | ExplUse's new conjunct Acc(ℰ) is not computed; the Θ-set value (I56: ExplUse holds) kept | set Acc(ℰ) by hand both ways (done in §4 for the bridge) |
| S108-3-I2 | V3.4, the reply's chain "Build ✗ → CT ✗ → Con ✗" | reading (ii), `S108_S3_CT=build`: the construction trace Con asks for is a Build subhistory, so CT also asks ExplUse at its output (D18.1's sentence "Con asks for a construction trace, which is what Build's subhistory is") | reading (i), the default: D12.2 as written, CT := t held at an output of a trace (Prepares), no ExplUse |
| S108-3-I3 | V3.6, every history the program builds | a history that states no construction meets the parts clause (the program's reading so far: `admitted` alone) | the clause unknown, the case left out |
| S108-3-I4 | V3.6, the reply's small case and the generated populations | parts(t) := the components of t's organization E (each with its counterpart binding, D12.4); the stated construction := a declared set of parts (Θ by hand, I90): the base member's components | parts as ports, or as edits ("set H", "set T" in the reply's wording) |
| S108-3-I5 | V3.4, generated worlds | the ℰ whose claim the trace uses: the generated candidate on its own question, and (a second run) the same transport claimed on the widest contract of its target, A×B restricted to translated pairs | any other question sharing t |
| S108-3-I6 | V3.7, generated worlds | the program has no generator of histories as circuits (FC75, FC76 build five by hand): every DAG of ≤ 4 occurrences with Boolean values and functions from a fixed set, enumerated | random circuits |

## 3. The worked cases (rule 5.1): Acc and Account ∧ ¬Dec(t), off and on

Run: `s108_s3_cases.py` §A (output: `section 3 runs/cases/cases.txt`). The 27 candidate cases of the written-in step's script (`s106_cases.py`, collected by running its own `main()`), each under 'none' and the nine readings (V3.1–V3.8, and V3.4 with CT reading ExplUse). No worked case carries a history of its own (except the student's copy, the bridge and CT8, below); t's history is set by hand (Θ by hand, I90), the three histories of `provenance_of` and four where a section-3 variant can bite (script header).

| reading | Acc moves | Account ∧ ¬Dec(t) moves (history) | Dec(t) moves, Account ∧ ¬Dec(t) unmoved | Build moves |
|---|---|---|---|---|
| V3.1, V3.2, V3.3, V3.7, V3.8 | 0 | 0 | 0 | 0 |
| V3.4 (CT as D12.2 writes it) | 0 | 0 | 0 | 5: T → F (ℰ_rev on C1, ℰ_rev under τ′ on C1, E_tab on C1 and C2, the L257 relabelings), exactly the 5 with Acc F |
| V3.4, CT reads ExplUse (S108-3-I2) | 0 | 0 ('Con-explu' with the candidate's own claim: Con ⇔ Acc, so Account ∧ ¬Dec(t) = Acc ∧ Acc) | 5 ('Con-explu': the 5 with Acc F, Dec F → T) | 5, the same |
| V3.5 | 0 | **22 in** ('Con-chg (tags)': every case with Acc T; Dec T → F) | 'Con-chg (chain, T)', '(chain, T′)': 5 (the Acc-F cases whose t is not faithful at the output); 'Con-chg (chain, U)', '(chain, K)': 0 | 0 |
| V3.6 | 0 | **22 in** ('Sel-parts': every case with Acc T) | 3 more ('Sel-parts': Acc F, Sel's other conditions met) | 0 |

- Acc moves under no section-3 variant on any worked case (computed; `account` calls none of the switched functions).
- V3.5's move is the tag model's: the represented target labelled at o1 only, before the unrecorded change. In the chain model, where Held at the output is computed from t (D12.2 after the second check, T′), no candidate meeting (E) moves: Acc ⇒ Faithful ⇒ held at o_t, and {o_t} alone is an episode (no change inside it), so Con at o_t = the trace at o_t whether or not the record clause stands. The 5 Dec moves in the chain are candidates with Acc F. §6.2 checks this over every chain of ≤ 4 occurrences.
- The student's declared copy (FC30.new1 (d)), chain model, T′, H = {(1,b1_45)} and H = ∅: Acc T; fixed point {o1: Con}; Dec(t) at o2 T; Account ∧ ¬Dec(t) F, under 'none' and all nine readings (§B of the output). No section-3 variant makes the student's copy an explanation.
- The bridge (FC84.new1) and CT8: §4 (V3.5, V3.8) and §5.

## 4. The reply's small cases, run (every "after" was marked not run by the reply)

Run: `s108_s3_cases.py` §C. Standing: whether the reply's "after" is what the computation gives.

| variant | case | reply's claim (after) | computed: none → on | standing |
|---|---|---|---|---|
| V3.1 | FC72 (e): ¬PM alone, j accepts ¬PM | rules out PM | F → T | computed |
| V3.1 | FC72 (b): a record made from ψ | rules out ¬ψ | F → T | computed |
| V3.1 | FC72 (a): a leaf ¬φ ∧ q, AndE | – | F → T | **added** |
| V3.1 | "p because p": p alone, j accepts p | – | rules out ¬p: F → T | **added** (what else blocks it: only D9.6's acceptance clause; for j who accepts nothing: F both) |
| V3.1 | j accepts ¬(Ans_p(a,b) = y) alone | "accepting 'Ans_p(a,b)=y' rules out every candidate answering y at (a,b) with no test" | the answer y ruled out: F → T; Acc(ℰ) of a candidate answering y ruled out: F both (the claims are consistent, I87); with 'Acc(ℰ) → Ans = y' also accepted, MT rules Acc(ℰ) out: T both | **contradicted** as worded (no candidate is ruled out by the answer alone); computed for the answer itself |
| V3.1 | j accepts ¬Expl(ℰ) alone | "(Suff) and (Nec) defeat sets by acceptance alone" | an argument not using (E) rules out Expl(ℰ): F → T; the pole's forward candidate (Acc T, constructed) in Def(L536): F → T; j accepts Expl(ℰ) alone: (Nec)'s defeat (L61) F → T | computed |
| V3.1 | Expl, Acc | "Expl = Acc ∧ ¬Dec unmoved" | Acc, Dec, Account ∧ ¬Dec(t): 0 moves (§3) | computed |
| V3.2 | FC70: u after j withdraws d (d also concluded below) | after: False | T → F | computed |
| V3.2 | Arg_test: record, r → ¬O, then MT to ¬(T∧B∧I) | unusable unless each intermediate conclusion is in Accepted_j | usable T → F; X_j(T∧B∧I) ≠ ∅: T → F; with ¬O also accepted: T both | computed |
| V3.3 | FC72 (f): j0 accepts nothing | usable T, \|X_j\| = 1 | usable F → T; \|X_j0(design ∧ PM)\| 0 → 1 | computed |
| V3.3 | FC72 (d): j accepts ¬PM | – | (usable T, \|X_j\| 1) both | computed |
| V3.3 | X_j(design ∧ PM) for j0 and j | assessor-independent | equal: F → T; j′ accepting something else: ¬PM alone usable F → T | computed |
| V3.4 | ℰ_rev worked out, the claim used Acc(ℰ_rev on C1) (Acc F: F1, F2, A fail), judged on C_id (Acc T) | Build ✗ → CT ✗ → Con ✗ → Dec(t) → not an explanation on C_id | ExplUse T → F, Build T → F. CT as D12.2 writes it: Con T, Dec F, Account ∧ ¬Dec(t) on C_id T, **unmoved**; with CT reading ExplUse (S108-3-I2): Con T → F, Dec F → T, Account ∧ ¬Dec(t) on C_id T → F | **contradicted** under D12.2 as written (CT reads Prepares, not ExplUse); computed only under S108-3-I2 |
| V3.4 | the same, the claim used Acc(ℰ_rev on C_id) | – | nothing moves (ExplUse T both) | computed |
| V3.5 | FC84.new1: Episode(o1 ≺ o2), (base, iv-u) | [True, True] after | S41 reading (T, F) → (T, T); L55 reading (F, F) → (F, T) | computed |
| V3.5 | FC84.new1 (c): unrecorded C → C′, held [T, T], trace at o2 | "CT gains witnesses, Con grows" | S41 reading (D13.8 now): Con at o2 [T] both under T′, T; [F, T] both under U; [F] both under K. L55 reading (text 104's words): [F] → [T] under T′, T; [F] → [F, T] under U | **contradicted** under D13.8's reading (t held at o2 already gives Con through {o2}); computed under L55's reading only |
| V3.5 | added: held [T, F], trace at o2 (t not held at the output) | – | Con at o2, T and T′: F → T (both episode readings); U, K: F both | **added**: Con moves only where t is not held at the output, so for no candidate meeting (E) (Acc ⇒ held) |
| V3.6 | pole forward t (parts c_H, c_T, c_L = the stated construction), t′ = t plus a part k_x, H = {(1,b1_45)} | t′ ∈ 𝒯, both Sel, underdetermination reaches pairs where they differ | idle k_x (full relation): Acc(t′) T; Sel(t′) F → T; Dec(t′) T → F; Account ∧ ¬Dec(t′) F → T; \|𝒯\| 1 → 2. Copy of c_H: the same (Acc T). k_x fixing L off the answer at one pair x of C1∖H: Acc(t′) F, t′ faithful on H, Sel(t′) F → T, x underdetermined: 0 → 1 (each of the 6 pairs) | computed (on S108-3-I4) |
| V3.6 | the student's declared copy | untouched | Dec(t) at o2 T under every reading (§3) | computed |
| V3.7 | FC75 (a) did no work; (a′) dependence outside R | both active | F → T; F → T | computed |
| V3.7 | FC75 (a″), (b), (d); FC76 | – | (a″) T both; (b) at rest F both; (d) idle member F both; FC76 T both | computed |
| V3.8 | FC84.new1 (a4): CreateEx over the 1,024 Θ-values | "[True] under both" | I191 labelling: [F, T] (1 true) → [F, T] (16 true); I192 (d): [F] (0) → [F, T] (16) | computed (the reply's "[True]" is the set's true value: some valuation holds under both) |
| V3.8 | the bridge (a1), no criticism; (a2), an earlier design criticized | "counts as creating an explanation whenever repair, origin, Account, Deploy and ProducesVia hold" | (a1): 0 → 16 of 1,024; (a2): 1 → 16; with every other conjunct met, CreateEx F → T on (a1) and on (a4) I192 (d) | computed |

## 5. The external examples FC-E1–FC-E5, the creative transport case CT1–CT8, and the written-in step's case script (rules 5.1–5.3)

Run: each script under `S108_S3_VARIANT=<v>` (and V3.4 with `S108_S3_CT=build`), output compared line by line with its output under 'none' (= the committed printout, md5s in §0). Outputs: `section 3 runs/scripts/<script>.<v>.txt`.

| reading | FC-E1–FC-E5 (`s104_external.py`) | CT1–CT8 (`s104_creative_transport.py`) | written-in step (`s106_cases.py`) |
|---|---|---|---|
| V3.1–V3.8, V3.4 with CT reading ExplUse | 0 lines differ | 0 lines differ | 0 lines differ |

- Nothing in the three scripts reads a section-3 item except CT8's provenance, which calls `sel` and `con` on histories that state no construction (V3.6 idle there, S108-3-I3), no change of contract (V3.5 idle), and no ExplUse (V3.4 idle, S108-3-I1); CT8's T′ line reads Held at the output, which no variant touches. Under every reading CT8 prints the same: R1–R5 "Sel no, Con yes/no" as under 'none'.
- So on the external examples and the creative transport case no section-3 variant moves Acc or Account ∧ ¬Dec(t) (computed, 0 of 5 and 0 of 8).

## 6. The generated worlds at scale 4 (rule 5.4)

Run: `s108_s3_worlds.py` (outputs `section 3 runs/worlds/<kind>.{txt,json}`, witnesses in full in the JSONs). Five kinds, each at the scale the rule gives; "smallest" is the first found in ascending size order.

### 6.1 Candidates (`claims_a.gen_p_cand`, 40 × 4 = 160 models per size, one seeded stream)

Per candidate, Acc(ℰ) and, on hand-set histories (Θ by hand, I90; the §3 histories, plus 'Con-explu (widest)': the claim used is Acc of the same transport on the widest contract it translates, S108-3-I5), Dec(t) and Account ∧ ¬Dec(t); Build with ExplUse computed; and t′ = t plus one part the stated construction (t's own parts) lacks, S108-3-I4: 'idle' (full relation), 'copy' (the first component's relation again), 'deviate' (on the queried port, admitting at the first pair x of C∖H one value E's answer there does not take; where the port's domain has one value it is 'idle').

CANDS_TABLE_PLACEHOLDER

### 6.2 Provenance chains (every chain o1 ≺ … ≺ on; (held, trace, Sel's conditions) per occurrence; contracts C, C′ with each change recorded or not)

| reading | chains | cut | moves of Dec(t) at the output, t held there (Acc ⇒ held) | t not held there | smallest witness |
|---|---|---|---|---|---|
| V3.5 | 115,400 (n ≤ 4) | T′ | **0** | 11,240 (Dec T → F) | n = 2: held [1, 0], trace [0, 1], C → C′ unrecorded: Con at o2 F → T |
| V3.5 | | T | **0** | 11,240 | the same |
| V3.5 | | K | 5,118 (Dec T → F) | 5,118 | n = 2: held [1, 1], trace [0, 1], Sel's conditions [1, 0], C → C′ unrecorded |
| V3.5 | | U | 1,460 (Dec {F, T} → {F}); 8,704 fixed-point sets changed, Dec's values kept | 10,164 | n = 2 |
| V3.4, CT reads ExplUse (S108-3-I2) | 4,368 (n ≤ 3, one contract, ExplUse per occurrence) | T′ | 546 (Dec F → T: ExplUse fails at the output); **92 (Dec T → F: an earlier trace's ExplUse fails, so that occurrence is no longer represented and a later holding becomes selected)** | 400 F → T; 92 T → F | n = 1: held, trace, ExplUse F; n = 2: held [1, 1], trace [1, 0], Sel's conditions [0, 1], ExplUse [0, 0] |
| V3.4 (S108-3-I2) | | T | 546 F → T | 400 | n = 1 |
| V3.4 (S108-3-I2) | | K | 124 F → T | 124 | n = 2 |
| V3.4 (S108-3-I2) | | U | 786 (fixed-point sets; 124 left with **no fixed point**, Dec undefined) | 564 (32 with no fixed point) | n = 1 |

- Under D12.2's cut (T′), and under T, the record clause of D13.8 is idle wherever t is held at its holding: {o_t} alone is an episode (no change inside it) and Held(o_t) gives Con. Every move of Con under V3.5 is at a holding whose t is not faithful there, so no candidate meeting (E) moves (Acc ⇒ Faithful_C ⇒ held). Under the rejected cuts K and U (D18.1, FC98) the record clause does reach holdings that are held.
- Under S108-3-I2 (CT asks ExplUse), Dec moves both ways: a trace whose output uses a claim that fails (E) no longer constructs, so its holding is declared (F → T), and an occurrence it made represented no longer is, which can lift D12.1's exclusion of a later selection (T → F).

### 6.3 Arguments (FC56's generator: 2–5 random premises over p, q, r, a random accepted subset, random forms, every argument of height ≤ 2; 400 × 4 = 1,600 models; φ ∈ {p, q, r, ¬p, ¬q, ¬r}: 9,600 (model, φ))

| reading | arguments whose usability moves | Out_j(φ) moves | X_j(φ) moves, Out_j(φ) kept | smallest witness |
|---|---|---|---|---|
| V3.1 | 0 | 1,677 F → T | 175 | premises ¬p, ¬q; j accepts ¬q; forms {AndE}; φ = q: ¬q alone rules out q |
| V3.2 | 8,983 (T → F) | 26 T → F | 849 | premises (q → p) ∧ ¬q, q; both accepted; forms MP, AndE; φ = ¬p: MP from q and the AndE step's q → p is no longer usable |
| V3.3 | 2,621 (F → T) | 703 F → T | 71 | premises ((¬q → ¬r) ∧ (¬r ∧ r)), ¬¬p; j accepts ¬¬p; forms {MT}; φ = p: the unaccepted inconsistent premise alone rules out p |

No generated candidate's Acc or Account ∧ ¬Dec(t) reads X_j (6.1: 0 moves under V3.1–V3.3); what moves is who has ruled what out, hence problems (D10.1) and the defeat sets (D16.XV).

### 6.4 Routes (every circuit of ≤ 4 occurrences, S108-3-I6; every R ∋ i, r; K = {(0, 1)})

ROUTES_PLACEHOLDER

### 6.5 Created explanation (every chain n ≤ 3, one contract, held and trace per occurrence, a label per occurrence: none, a criticism of an earlier design, a question about the brief labelled a criticism; the 2^10 Θ-values of (EX)'s other conjuncts, as FC84.new1 (a4))

CREATEX_PLACEHOLDER
