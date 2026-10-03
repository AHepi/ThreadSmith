# S108 Part A - section 3 - variants computed

*Computing agent for section 3 (rule 5 of `S108 Part A - how the replies will be read, written before sending.md`), Opus 5.5, 28 September 2026. Fresh. Works only in `S108 Part A - computation/section 3 model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`). Nothing here changes the theory (rule 11). "Candidate" or "explanation" for what the theory judges; "model" only for the program or a small structure it builds (S43).*

Status: complete, 28 September 2026. Filled as it went; nothing ruled.

## 0. Setup

| item | state |
|---|---|
| copy | `S108 Part A - computation/section 3 model/` = program after round 4, 26 files, every file md5-identical at the copy |
| switches | `model/s108s3.py`: `S108_S3_VARIANT` ("none" default; V3.1–V3.8); `S108_S3_CT` for V3.4 only ("prepares" default = D12.2 as written; "build" = the reply's chain, S108-3-I2). Read at: `args.rules_out` (V3.1), `args.usable_step` and `usable_any_step` (V3.2), `args.usable` (V3.3), `claims_b.build_at`, `_con_at`, `con`, FC90.new1 (a) (V3.4), `claims_b.episode` (V3.5), `claims_b.sel` via `s108s3.in_population` (V3.6), `phys.act_route` (V3.7), FC84.new1 (a4) via `s108s3.create_ex` (V3.8); D18.1's graph `claims_b.DEP` follows each variant's right-hand side (`s108_s3_dep`) |
| default unchanged | under "none" the three case scripts print byte for byte the committed printouts: md5 86a67664a9a3584351fd4836a4140b69 (external), d473944e74d2f349b1fdfb83277843cf (creative transport), 043aeb3647a9004ae43009a7fed50b4e (written-in step), as the rule gives |
| scripts (in the copy) | `s108_s3_suite.py`, `s108_s3_compare.py`, `s108_s3_run_suites.sh` (whole suite), `s108_s3_cases.py` (worked cases, histories, the reply's small cases), `s108_s3_worlds.py` (generated worlds) |
| runs | PYTHONHASHSEED=0, `timeout` on every run; suite at scale 4, time cap 45 (the printout's settings), capped parts re-run at cap 300; outputs in `S108 Part A - computation/section 3 runs/` (`cases/`, `scripts/`, `worlds/`, `suite/`). The whole-suite runs were made by this agent's scripts, not through the Sonnet harness (this agent can start no other agent) |

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
| S108-3-I1 | V3.4, cases with no ℰ built (the bridge, FC83's chains) | ExplUse's new conjunct Acc(ℰ) is not computed; the Θ-set value (I56: ExplUse holds) kept | set Acc(ℰ) by hand both ways: done for the reversed calculation (§4: the claim used on C1, Acc F, and on C_id, Acc T); in FC84.new1 (a4) (EX)'s own Acc conjunct runs over both values |
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
- The bridge (FC84.new1) and CT8: §4 (V3.5, V3.8) and §5. E2 (identification: FC57, FC58), E3 (the two balances: FC59, FC60), E4 (obstruction: FC61), E6 (the skew-symmetric matrices: FC63) and E7 (transport results: FC64–FC66) are computed through their claims in the suite (§7): FC63's counterexample stands under every reading; of the rest only FC60 (b) moves (V3.1: the record made from the favoured mass now rules out its denial).

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
| V3.8 | FC84.new1 (a4): CreateEx over the 1,024 Θ-values | "[True] under both" | I191 labelling: [F, T] (1 true) → [F, T] (16 true); I192 (d): [F] (0) → [F, T] (16) | computed (the reply's "[True]" read as: some valuation meets (EX) under both) |
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

| world set | seed | models | Acc T under 'none' |
|---|---|---|---|
| SMALL (108 sizes: ports ≤ 3, dom ≤ 2, comps ≤ 3, \|B\| ≤ 2, edits ≤ 2) | 108301 | 17,280 | 1,013 |
| SMALL, value maps | 108302 | 17,280 | 881 |
| SMALL, proper targets (I101) | 108303 | 1,420 | 232 |
| MID (dom ≤ 3; 162 sizes) | 108304 | 25,920 | 1,670 |

Candidates whose result differs from 'none' (Acc moves under no reading, in any set: 0 of 61,900):

| reading | result | SMALL | SMALL vm | proper | MID | direction; smallest witness (SMALL) |
|---|---|---|---|---|---|---|
| V3.1, V3.2, V3.3, V3.7, V3.8 | every result: Acc, Dec(t) and Account ∧ ¬Dec(t) on every history, Build, t′ | 0 | 0 | 0 | 0 | – |
| V3.4 | Build, with the candidate's own claim | 16,267 | 16,399 | 1,188 | 24,250 | T → F: exactly the candidates with Acc F |
| V3.4 | Build, the claim on the widest contract | 15,856 | 16,024 | 1,091 | 23,627 | T → F |
| V3.4 (either CT reading) | Account ∧ ¬Dec(t), own claim ('Con-explu (self)') | 0 | 0 | 0 | 0 | with CT reading ExplUse, Dec F → T on every Acc-F candidate (16,267 …), never on an Acc-T one |
| V3.4, CT reads ExplUse (S108-3-I2) | Account ∧ ¬Dec(t), the claim on the widest contract | **122** | 93 | 36 | 200 | out: Acc on C, not on the widest contract; E_enc \| G-free: ports 1, dom 1, comps 1, \|B\| 1, edits 2 |
| V3.4, CT as D12.2 writes it | Account ∧ ¬Dec(t), any history | 0 | 0 | 0 | 0 | – |
| V3.5 | Account ∧ ¬Dec(t), 'Con-chg (tags)' | **1,013** | 881 | 232 | 1,670 | in: every Acc-T candidate; E_enc \| G-free and G-surg, lookup, random; smallest ports 1, dom 1, comps 1, \|B\| 1, edits 1 |
| V3.5 | Dec(t), 'Con-chg (chain, T′)' and '(chain, T)' | 8,081 | 8,144 | 650 | 12,454 | T → F, every one with t not faithful (Acc F) |
| V3.5 | Account ∧ ¬Dec(t), 'Con-chg (chain, U / K / T / T′)' | 0 | 0 | 0 | 0 | – |
| V3.6 | Account ∧ ¬Dec(t), 'Sel-parts' | **1,013** | 881 | 232 | 1,670 | in: every Acc-T candidate; smallest as V3.5's |
| V3.6 | t′ = t + an idle part: Account ∧ ¬Dec(t′) | **1,013** | 881 | 232 | 1,670 | in (Acc(t′) = Acc(t)) |
| V3.6 | t′ = t + a copied part: Account ∧ ¬Dec(t′) | 153 | 132 | 25 | 260 | in; elsewhere the copy breaks Dep (deleting a committed component no longer loses the answer) |
| V3.6 | t′ = t + a part deviating at x: Account ∧ ¬Dec(t′) | 638 | 627 | 22 | 889 | in, only where the queried port's domain has one value (the part is then idle) |
| V3.6 | t′ deviating at x: pairs of C∖H newly underdetermined | **1,141** | 859 | 469 | 2,577 | 0 → 1; E_enc \| G-free: ports 1, dom 2, comps 1, \|B\| 1, edits 1 (t′: Acc F, Sel F → T) |

Witnesses in full: `section 3 runs/worlds/cands.*.json`, field `witness`.

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

| result | count | smallest witness |
|---|---|---|
| circuits; (circuit, R) routes | 1,460; 5,724 | – |
| ActRoute F → T under V3.7 | **1,436** (every route whose members feed r inside R, not at rest, with no dependence on the contrast) | n = 2: n1 := c0(i) (a constant), R = {i, n1} |
| ActRoute T → F | 0 | – |
| ProducedBy (some R from i to r active) F → T | 685 of 1,460 circuits | – |
| ProducesVia (a middle occurrence on some active R) F → T | 952 of 2,860 (circuit, occurrence) | – |
| inactive under both | 3,024 (a member feeds r by no path inside R) | – |

Under 'none' every route active under V3.7 but not under 'none' fails only the dependence conjunct: the variant adds exactly the routes that did no work (the frozen L375.s2's "nonconstant dependence"). UsesReason (D9.11) reads an active route the same way ProducesVia does; the program supplies it by hand (I47, FC76), so it is counted here only through ProducesVia's form.

### 6.5 Created explanation (every chain n ≤ 3, one contract, held and trace per occurrence, a label per occurrence: none, a criticism of an earlier design, a question about the brief labelled a criticism; the 2^10 Θ-values of (EX)'s other conjuncts, as FC84.new1 (a4))

| result | count |
|---|---|
| chains; valuations | 1,884; 1,929,216 |
| CreateEx F → T under V3.8 | **7,086** valuations; CreateEx T → F: 0 |
| no criticism in the chain, Build T | 21 chains: holds on 0 → 16 of 1,024 (smallest: n = 1, held, trace, no label) |
| a criticism in the chain, Build T | 450 chains: holds on 1 → 16 of 1,024 (smallest: n = 1, a criticism of an earlier design) |
| Build F | 0 moves (Origin needs Build under both) |

Under 'none' CreateEx holds on one valuation of 1,024 at most (every CCE conjunct, the criticism clause and the rest met); under V3.8 on 16 (Origin and the rest met, whatever the CCE conjuncts and the labels). So the whole difference is the chains and valuations with no critical episode: V3.8 admits into (EX) every originative repair through an account, with or without a criticism, and whichever labelling of "no question occurred" (I191, I192 (d)) is used.

## 7. The whole suite with each variant on (rule 5, last clause)

Run: `s108_s3_run_suites.sh` (`s108_s3_suite.py` under `S108_S3_VARIANT=<v>`, scale 4, cap 45, PYTHONHASHSEED=0, three at a time, `timeout` 3000 s each), compared with the same run under 'none' by `s108_s3_compare.py` (status per claim; per part the status and the counterexample/witness/result text; model counts and timings not compared). The baseline under 'none': 133 hold, 2 counterexamples (FC23, FC63), 7 not tested of 142, every claim's status as the committed printout. Comparisons: `section 3 runs/suite/compare.<v>.txt`. Other sections' agents ran on the same machine at the same time: parts that reached the 45 s cap in any run are re-run alone at cap 300 (§7.1).

| reading | claims whose status moves | parts that move (status or text) | statuses under the reading (hold / counterexample / not tested) |
|---|---|---|---|
| V3.1 | 5 (FC60, FC71, FC72, FC72.new1, FC72.new2) | 7 | 128 / 7 / 7 |
| V3.2 | 7 (FC47, FC47.new1, FC53, FC68, FC69, FC70, FC71) | 9 | 126 / 9 / 7 |
| V3.3 | 2 (FC72, FC72.new1) | 3 | 131 / 4 / 7 |
| V3.4 | 1 (FC90.new1) | 2 (FC90.new1 (a); FC23.new1 (c)'s witness not found under the 45 s cap only, found at cap 300: §7.1) | 132 / 3 / 7 |
| V3.4, CT reads ExplUse (S108-3-I2) | 1 (FC90.new1) | 2 (as V3.4) | 132 / 3 / 7 |
| V3.5 | 1 (FC84.new1) | 6 | 132 / 3 / 7 |
| V3.6 | 0 | 2 (text only) | 133 / 2 / 7 |
| V3.7 | 1 (FC75) | 5 | 132 / 3 / 7 |
| V3.8 | 1 (FC32.new1) | 2 | 132 / 3 / 7 |

**V3.1** (every move is as claimed → not as claimed, or holds → counterexample):

| claim | what moved |
|---|---|
| FC72 | part (a), (b), (c): (a) a leaf with ¬φ as a conjunct no longer blocks, (b) a record made from ψ rules out ¬ψ ((c) holds as before); part (e): ¬PM alone rules out PM ("p because p") |
| FC72.new1 | (b) O4, O5: "the block alone tells it from the denial" fails: nothing tells a premise taken as given from the denial |
| FC72.new2 | (c) K1: j2's premise 'Slot ∧ ¬Acc(ℰ_myth1)' rules the myth out (blocked under 'none'); Acc(ℰ_myth1) T and the myth's standing as explanation unmoved |
| FC71 | (i), (ii) counterexample: α⁺ ∈ X_j(T∧B∧I) with a leaf having ¬(T∧B∧I) as a conjunct; (i′) a record leaf made from ¬(T∧B∧I) no longer blocks α⁺ |
| FC60 | (b) E3: the record made from x = m* (the favoured mass) rules out x ≠ m* |

**V3.2**:

| claim | what moved |
|---|---|
| FC47 | (b) the argument from a test's record (record → ¬meets → MT ¬Acc): not usable |
| FC47.new1 | the pole, forward against reversed on C1: never solved (\|X_j(Acc(ℰ_rev))\| 4, 0, 4 → 0, 0, 0; Prob_j F, T, F → T, T, T) |
| FC53 | (a) ConfCl with Applies: the argument through the AndI step not usable |
| FC68 | (b), (c) "every such candidate alike": the argument from (A) and each candidate's own answer not usable; (a) "a failed answer stays failed" holds |
| FC69 | I40's alternative: one fixed point (0 usable steps) where there were two (0 and 2) |
| FC70 | a premise live twice over: usable after withdrawal T → F |
| FC71 | (i) the MT from a failed prediction not usable; (i′) likewise |
| also moved, status kept | FC32.new1 (b): the cycle text of U (the loop K2 → Live gone from DEP) |

**V3.3**: FC72 (f) (a premise alone j has not taken up is usable: |X_j(design ∧ PM)| 0 → 1); FC72.new1 (a) (the words-alone reading and D9.6 agree: usable by j0), (c) (for j0, who accepts nothing, ¬PM rules the design out).

**V3.4** (both CT readings): FC90.new1 (a): Build for the reversed calculation used in error T → F ("A system may understand a theory in error", L403.s3, FROZEN). No other claim reads ExplUse with a computed Acc (the bridge's and FC83's Build set ExplUse by hand, S108-3-I1), so the CT reading changes nothing else in the suite.

**V3.5**: FC84.new1 (c) as claimed → not as claimed (the unrecorded change C → C′ is an episode; Con at o2 [T] both under the S41 reading, [F] → [T] under L55's); (a3) as claimed → not as claimed (under L55's reading iv-u's unrecorded change now moves Con); (a4) look not as expected (Episode (base, iv-u) (T, F) → (T, T)); FC84.new2 (b) witness found → none (with no record clause the unordered and covering forms cannot differ; claim status kept); FC32.new1 (c), FC98 (b) text only (the sinks q(o), Rec_h′, ImmAfter leave D18.1's graph). FC84.new1 (a1), (a2), (b), (d) and every provenance claim (FC12.new1–new3, FC77–FC83, FC98.new1, FC98.new2) unmoved.

**V3.6**: no claim's status moves. Text only: FC32.new1 (c) and FC98 (b), the sinks 'parts' and 'stated construction' leave D18.1's graph. FC80 (Argument 3) unmoved: its populations state no construction (S108-3-I3).

**V3.7**: FC75 (a) (a route that did no work is active) and (a′) (dependence only outside R: active) as claimed → not as claimed; (a″), (b) text only (the reason printed); FC98 (b) text (the sink K leaves); FC76 unmoved.

**V3.8**: FC32.new1 (f) as claimed → not as claimed: (EX) ⇝ Crit F under U, K, T and T′ (Con, CT, Episode ⇝ Crit F as before), so "created explanation does [ask for a criticism event]" fails; FC84.new1 (a4) look: I192 (d)'s CreateEx [F] → [F, T]. FC90 unmoved.

### 7.1 Parts that reached the 45 s cap

The claims with a part stopped by the 45 s cap in some run (FC23.new1, FC43, FC56, FC70; the other sections' suites ran at the same time) were re-run under 'none' and every reading at cap 300 (`s108_s3_rerun_capped.sh`, two at a time; `section 3 runs/suite/capped300.<v>.json`, comparisons `compare.capped300.<v>.txt`). No part reached the cap (under 'none': FC23.new1 103 s, FC43 45 s, FC56 132 s, FC70 20 s).

| reading | at cap 300, against 'none' at cap 300 |
|---|---|
| V3.1, V3.3, V3.4, V3.4 with CT reading ExplUse, V3.5, V3.6, V3.7, V3.8 | no status or text moves |
| V3.2 | FC70 holds → counterexample (a premise live twice over), as at cap 45 |

So FC23.new1 (c)'s "no witness found" under V3.4 at cap 45 was the cap (its witness is found at cap 300 under every reading); every other result of §7 stands at cap 300.

The suites under V3.1, V3.2, V3.3 and V3.5 were run twice: the first runs (19:48–20:42 UTC) were made before two fixes to the copy's own code, and are replaced by the second (`s108_s3_rerun_suites.sh`): FC90.new1's note on D13.3 printed under every variant (text only; it now prints under V3.4 alone), and FC84.new2's own encodings of D13.8's record clause (covering, ordered, unordered) had not been switched with V3.5, which made its part (c) compare a switched and an unswitched form. The second runs differ from the first only in those two places.

## 8. The edges (rule 5): the reply's, marked; and those the computation adds

Standing: **computed** (the computation shows it), **contradicted** (it shows otherwise), **not settled by computation** (with what would settle it), **computed in part** (a part of the row contradicted or not settled, named in it); **added**: shown by the computation, not named by the reply. Marks are the template's. Evidence names the run (cases, suite.<v>, worlds.<kind>: `section 3 runs/`). The `.json` beside this file holds every row (built by `s108_s3_edges.py` and `s108_s3_edges_rest.py`, in the copy).

### V3.1

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| constrains | L397.s5 [FROZEN] | X_j(ψ) = usable ∧ RO must stay a reading of the frozen words; the variant lives inside RO | computed | X_j(φ) := {α : Usable_j(α) ∧ RO(α, φ)} is still 'the set of arguments usable by j that rule out ψ' under V3.1 (the frozen words name no block); its extension grows: worlds.args 1,677 of 9,600 (model, φ) Out_j F → T, 175 more X_j moves; usability 0 moves |
| changes with | L8.s3 [S1] | 'the claim's denial is not among its premises' states the block in Part 0; must change with the variant | computed | L8.s3's clause is false of D9.7 under V3.1: ¬PM alone rules out PM (FC72 (e) as claimed → not as claimed; cases §C); p alone rules out ¬p for j who accepts p |
| moves | (Suff) and (Nec) defeat sets (D16.XV) [S4] | ruling out by bare acceptance enters them; being an explanation (Acc ∧ ¬Dec) unmoved | computed | j accepting ¬Expl(ℰ) alone: an argument not using (E) rules out Expl(ℰ) F → T; the pole's forward candidate (Acc T, constructed) in Def(L536) F → T; j accepting Expl(ℰ) alone rules out ¬Expl(ℰ) ((Nec), L61) F → T (cases §C). Acc, Dec, Account ∧ ¬Dec(t): 0 moves on 27 worked cases, FC-E1–E5, CT1–CT8, 61,900 generated candidates (§3, §5, §6.1) |
| changes with | L397.n14, L397.s16 [S3] | – | **added** | the two sentences varied with D9.7 (new form not given by the reply) are false of it under V3.1: 'p because p' (L397.s16) rules ¬p out for j who accepts p; a record made from ψ rules out ¬ψ (FC72 (b)); FC72.new1 (b) (O4, O5: 'the block alone tells it from the denial'): as claimed → not as claimed |
| changes with | D9.9 (K3), FC71 (i), (i′) [S3] | – | **added** | D9.9's clause 'no leaf of α with ¬(T∧B∧I) as a conjunct' and its record-leaf clause (L395) no longer block: FC71 (i), (ii) holds → counterexample (α⁺ ∈ X_j(T∧B∧I) with the block present); FC71 (i′) as claimed → not as claimed (suite.V3.1) |
| changes with | FC60 (b) (E3, the two balances: a bias set from the favoured mass) [–] | – | **added** | the record made from x = m* now rules out x ≠ m*: FC60 (b) as claimed → not as claimed (suite.V3.1) |
| changes with | FC72.new2 (c), K1 (the myth about winter, L397, S28) [–] | – | **added** | j2, who holds 'Slot ∧ ¬Acc(ℰ_myth1)' as one premise (the finding with the denial in it), rules the myth out under V3.1 (blocked under none): FC72.new2 (c) as claimed → not as claimed; the myth's Acc and being an explanation unmoved (S44, S45 untouched: ruled out for j is not 'not an explanation') |
| moves | who has ruled what out (D9.8), problems (D10.1) [S2; FROZEN] | – | **added** | worlds.args: 1,677 new Out_j(φ), smallest: ¬q accepted rules out q; no usability moves (V3.1 reads RO only) |

### V3.2

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| constrains | L389.s1 [FROZEN] | Live must remain a predicate of (d;u) read by K2's ∀d | computed | under V3.2 Live_j(d; u) is still a predicate of (d; u), constant in u; (K2) as displayed is read unchanged; every suite run under V3.2 computes (K2) through it |
| moves | X_j and everything downstream (D9.8; D10.1) [S2; FROZEN] | fewer usable arguments; fewer ruled out; fewer problems and fewer solved; no conjunct of (E) moves | computed, in part; 'fewer problems' contradicted | fewer usable: worlds.args 8,983 argument usabilities T → F, 26 Out_j T → F; FC47 (b), FC53 (a), FC68 (b)–(c), FC70, FC71 (i), (i′) move. Fewer solved, more problems: FC47.new1 (the pole, forward against reversed): solved at ξ and ξ″ under none (\|X_j(Acc(ℰ_rev))\| = 4, Prob_j F) → unsolved at all three (\|X_j\| = 0, Prob_j T): with fewer ruled out, D10.1's NotOut holds of more rivals, so problems grow. (E): 0 moves |
| changes with | L393.n2 [S3] | – | **added** | L393.n2 defines Live 'd = concl(u′) for some u′ ∈ Below(u) with Usable_j(u′) (D9.4), or a premise j tentatively accepts': false of D9.4 under V3.2 (FC70: a premise live twice over is no longer live after withdrawal) |
| changes with | L369.s3 (FC68 (b), (c)) [S3] | – | **added** | 'every such candidate alike is ruled out … from the candidate's own answer there': the two-step argument from (A) and each candidate's own answer is not usable: FC68 (b)–(c) as claimed → not as claimed; FC68 (a) ('a failed answer stays failed', L369.s1–s2 FROZEN) holds under V3.2 |
| changes with | D9.9 (K3) (FC71 (i)) [S3] | – | **added** | K3's u⁺ from a failed prediction is a step above the step concluding ¬O; with Live through no step it is unusable unless j accepts ¬O itself (cases §C: T → F; with ¬O accepted T): FC71 (i), (i′) move |
| changes with | D18.1's loop K2 → Live → K2; I40 (FC69) [S4; S3] | – | **added** | DEP's Live loses its staged (K2) edge: the loop S101 read closes trivially; FC69's alternative reading has one fixed point (0 usable steps) where it had two (0 and 2): FC69 (I40's alternative) as claimed → not as claimed; FC32.new1 (b)'s cycle text changes |
| changes with | FC47 (b), FC53 (a) (arguments from a test's record; ConfCl with Applies) [–] | – | **added** | each is a two-step argument whose intermediate conclusion j does not accept: usable T → F (suite.V3.2) |

### V3.3

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| constrains | L397.s5 [FROZEN] | as V3.1 | computed | X_j(ψ) is still the set of arguments usable by j that rule out ψ, but for a premise alone 'usable by j' reads nothing of j: X_j0(design ∧ PM) = X_j(design ∧ PM) for j0 who accepts nothing and j who accepts ¬PM (cases §C) |
| changes with | L393.n2 [S3] | 'a claim j has never taken up is not live for j'; the varied D9.6 contradicts it | computed | FC72.new1 (a) as claimed → not as claimed: j0 never took ¬PM up and ¬PM alone is usable by j0 and rules out design ∧ PM |
| moves | (Suff)/(Nec) defeat sets; Prob_j assessor-independent [S4; FROZEN] | bare claims rule out with no chooser, against S28 | computed | FC72 (f): usable F → T, \|X_j0\| 0 → 1; ψ = r ∧ (r → ¬Expl(ℰ)) alone, j0 accepts nothing: an argument not using (E) rules out Expl(ℰ) F → T (a bare ¬Expl(ℰ) stays blocked by D9.7); worlds.args 2,621 usabilities F → T, 703 Out_j F → T. What rules out is then the same for every assessor, so D10.1's problems and D16.XV's defeat sets no longer depend on j for premises alone |
| changes with | FC72.new1 (c) (S27 with S28 and Q23) [–] | – | **added** | 'for j0 (accepts nothing)': ruled out F → T; the conflict and the ruling out coincide with no chooser: FC72.new1 (c) as claimed → not as claimed (suite.V3.3) |

### V3.4

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| blocks | L403.s3 [FROZEN] | 'A system may understand a theory in error': a use in error can no longer prepare explanatory use | computed | FC90.new1 (a) as claimed → not as claimed (both CT readings): Build for the reversed calculation used in error T → F; worked cases: Build T → F exactly on the 5 with Acc F; worlds.cands: Build moves on 16,267 of 17,280 (every Acc-F candidate) |
| moves | Dec(t), via CT (D12.2) and Build [S2] | transports constructed only through uses-in-error become Dec; Expl = Acc ∧ ¬Dec shrinks on that class | **contradicted under D12.2 as written; computed only under S108-3-I2** | D12.2's CT reads Prepares (t held at an output of a trace), not ExplUse (the program's DEP: CT → h, Prepares, BindingConstruction): on the reply's case (ℰ_rev claimed on C1, judged on C_id) Con T, Dec F, Account ∧ ¬Dec(t) on C_id T both ways; 0 Dec moves on the worked cases, the scripts, the generated candidates. With CT reading ExplUse (S108-3-I2): the reply's case T → F; worked cases 'Con-explu' Dec moves 5 (Acc F; Account ∧ ¬Dec(t) unmoved, since with its own claim Con ⇔ Acc); worlds.cands 'Con-explu (widest)': Account ∧ ¬Dec(t) T → F on 122 (Acc on C, not on the widest contract); worlds.chains under T′: Dec F → T 546 held, and T → F 92 (below) — settle: whether 'the construction trace' of D12.2 (L197) is Build's subhistory with all Build's conjuncts (S108-3-I2) or t held at an output of a trace (D12.2 as written): a reading of L197 and D18.1's sentence 'Con asks for a construction trace, which is what Build's subhistory is' |
| constrains | L526.s11 ('Build depends on histories, Ownership and (E)') [S4] | ExplUse must keep reading the claim 'Acc(ℰ)'; it does, conjoined with Acc | computed | DEP unchanged by V3.4 (ExplUse → UsesClaim, (E), Cand); FC32.new1 (d) (L526's dependences as paths) unmoved; under V3.4 Build depends on (E)'s value, not only on the claim's content (FC90.new1 (a)) |
| moves | Origin (G), created explanation (EX) [S3] | – | **added** | Build is a conjunct of (G) (D13.6) and (G) of (EX): Build F wherever the claim used fails (E); (EX)'s own Account conjunct (L449) then repeats what Origin already asks where the claim used is (c, p_c, t_c, Γ_c)'s (FC90.new1 (a)'s statement) |
| moves | Sel via D12.1's exclusion (under S108-3-I2) [S2] | – | **added** | worlds.chains, T′: 92 chains with Dec T → F at a held output: an earlier trace whose output uses a claim failing (E) no longer constructs, its occurrence is no longer represented, and D12.1's exclusion of a later selection lifts (n = 2: held [1, 1], trace [1, 0], Sel's conditions [0, 1], ExplUse [0, 0]); under U, 124 chains left with no fixed point |

### V3.5

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| changes with | L55.n3 [S1] | 'An episode is a history in which every change C→C′ carries a provenance record (D13.8)' points at D13.8 an… | computed | under V3.5 FC84.new1 (c)'s chain with an unrecorded change C → C′ is an episode (S41 reading F → T); FC84.new1 (a4)'s iv-u chain: Episode F → T (cases §C); L55.n3's words no longer describe D13.8 |
| moves | Dec(t) via Episode → CT (D12.2) [S2] | more episodes → more Con → fewer Dec → more explanations | **contradicted under D12.2's cut (T′, and T) for every candidate meeting (E); computed in the tag encoding and under the rejected cuts K, U** | worlds.chains (115,400 chains, n ≤ 4): under T′ and T, Con moves only at holdings whose t is not held there (11,240), none where it is: Acc ⇒ Faithful ⇒ held at o_t, and {o_t} alone is an episode, so the record clause never decides Con there; worked cases: 'Con-chg (chain, T′)' Dec moves 5, all Acc F; worlds.cands: 0 Account ∧ ¬Dec(t) moves on the chain histories (61,900). In the tag encoding ('Con-chg (tags)': the target labelled represented at o1 only, before the unrecorded change) every candidate meeting (E) moves in: 22 of 27 worked cases, 1,013 / 881 / 232 / 1,670 generated. Under K: 5,118 chains with a held output move (Dec T → F) — settle: whether D12.2's 'available as a represented target' may be read at o_t itself (Held(o_t), T′, D12.2 as written) or only at an earlier occurrence of the episode (the tag encoding; K): a reading of L197 and D12.2 against D18.1's cut |
| changes with | D12.2's Held(o′, x) for some o′ ⪯ o_t (I162, the cut T′) [S2] | – | **added** | what keeps D13.8's record clause from ¬Dec(t) for a candidate meeting (E) is D12.2's o′ ⪯ o_t with Held at o_t (the chain model, T′): with o′ ≺ o_t only (K) the clause reaches 5,118 held chains; computed (worlds.chains) |
| changes with | FC84.new1 (a3), (c), (a4); FC84.new2 [–] | – | **added** | suite.V3.5: FC84.new1 (c) as claimed → not as claimed (the unrecorded change C → C′ is an episode under both readings; Con at o2 [T] both under the S41 reading, [F] → [T] under L55's); (a3) as claimed → not as claimed (under L55's reading iv-u's unrecorded change now moves Con, where only a recorded one did); (a4) look: Episode (base, iv-u) (T, F) → (T, T); FC84.new2 (b) witness found → none (with no record clause, P4's unordered form and the covering form cannot differ; the claim's status kept); FC32.new1 (c), FC98 (b): text only (the sinks q(o), Rec_h′, ImmAfter leave D18.1's graph) |

### V3.6

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| blocks | none found (no frozen sentence states the parts bound; L481.s3 is S3, varied with it) [–] | – | computed (search) | grep of the template's FROZEN sentences: L195.s1 ('There is a population 𝒯 of candidate transports, a variation operator μ on 𝒯, … a survival condition requiring fidelity on H') names 𝒯 and says nothing of parts; no other FROZEN sentence names the population or the stated construction; the suite under V3.6 moves no claim's status (text only: FC32.new1 (c), FC98 (b), the sinks 'parts' and 'stated construction' leave D18.1's graph) |
| constrains | D12.1 writes 𝒯 = D15.8's population [S2] | the variant must still define a set 𝒯; it does | computed | under V3.6 D12.1 reads t ∈ 𝒯 through s108s3.in_population (Θ's admission alone); Sel computed on every history of §3, §6.1 |
| moves | Sel (D12.1), hence Dec and Expl; Argument 3's extent (FC80) [S2; S4] | wider population: more Sel, fewer Dec, wider underdetermination | computed (on S108-3-I4); not settled for FC80 as built | worked cases 'Sel-parts': Account ∧ ¬Dec(t) F → T on the 22 with Acc T; worlds.cands: 1,013 / 881 / 232 / 1,670 in ('Sel-parts'; t′ + an idle part the same); pairs newly underdetermined (t′ deviating): 1,141 / 859 / 469 / 2,577 candidates; the pole: t′ faithful on H, Sel F → T, each of the 6 pairs of C1∖H underdetermined 0 → 1. FC80 (suite) does not move: its populations state no construction (S108-3-I3) — settle: for FC80 itself: a population with a stated construction built into FC80's generator |
| changes with | L481.s3 [S3] | – | **added** | L481.s3's second clause ('a transport that would need a part every member of the population is built without is not in it') is false of D15.8 under V3.6: t′ with a part none of 𝒯 has is in 𝒯 (cases §C) |
| moves | the student's declared copy (FC30.new1 (d)) [–] | – | **added** | unmoved, as the reply says: Dec(t) at o2 T under V3.6 (the copy's defect is the absent trace and D12.3's inheritance, not the population) |

### V3.7

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| blocks | L375.s2 [FROZEN] | 'nonconstant dependence on the represented distinction under the declared contrasts' is part of the frozen … | computed | FC75 (a) (did no work) and (a′) (dependence only outside R) as claimed → not as claimed (suite.V3.7; (a″), (b) text only: the reason printed); worlds.routes: 1,436 of 5,724 routes active under V3.7 with constant dependence, smallest n = 2: n1 := c0(i) |
| moves | (P) via ProducedBy (D14.3), (EX) via ProducesVia (D14.6), reason use (D9.11) [FROZEN] | idle routes become active; no part of (E) moves | computed for ProducedBy and ProducesVia on generated circuits; not settled for UsesReason; (E) computed | worlds.routes: ProducedBy F → T on 685 of 1,460 circuits, ProducesVia on 952 of 2,860 (circuit, occurrence); Acc 0 moves anywhere. The program supplies ProducedBy, ProducesVia and UsesReason by hand in its claims (I90, I47): FC76 (UsesReason) unmoved — settle: UsesReason computed over circuits with a represented objection and role maps (D9.11's m, Rec, Chg), which the program does not build |

### V3.8

| kind | item [mark] | the reply's why (cut) | standing | evidence / what would settle |
|---|---|---|---|---|
| blocks | none (L443.s3 constrains only O_ex ⊆ O; L445.s1, L429.s1–s3 are S3) [FROZEN; S3] | – | computed, in part | no frozen sentence about (EX) is false under V3.8 (L443.s3 names O_ex only); but see the added edge on L528.s2–s3 (FROZEN) |
| constrains | L443.n1 ('an explanatory aim requires a deployable account') [S3] | Deploy conjunct kept | computed | Deploy is kept in s108s3.create_ex's rest; CreateEx under V3.8 never holds with Deploy F (worlds.createx) |
| changes with | L628 and D18.1's DEP [S4] | FC90: CCE 'left unstated by L628', so no sentence change is forced; DEP's (EX) node loses its Crit edge (FC… | computed for DEP; the quotation does not match the text now; the owner's part not settled by computation | DEP: (EX) no longer reaches Crit: FC32.new1 (f) as claimed → not as claimed ((EX) ⇝ Crit F under U, K, T, T′; Con, CT, Episode ⇝ Crit F as before); FC84.new1 (a4) look: I192 (d)'s CreateEx [F] → [F, T]. L628: FC90 unmoved (its (EX) list is fixed); the words 'left unstated by L628' are FC90's result about text 103 (its first part); the text now, L628.n2, states 'with CreativeCriticalEpisode(s,Δ,h,e)' among its hypotheses, which under V3.8 becomes a surplus hypothesis (the conditional still holds), so no sentence is made false (rule 14) — settle: whether the owner wants (EX) to keep its critical episode (S47 with S41 Q6): the owner's yes or no |
| moves | the class of created explanations; not (E), not Expl, not (Suff)/(Nec) [–] | (EX) is a defined relation of an episode (L31.s4) | computed | worlds.createx: CreateEx F → T on 7,086 of 1,929,216 valuations (1,884 chains), T → F on 0; the bridge (a1), no criticism: 0 → 16 of 1,024; FC84.new1 (a4) I192 (d): [F] → [F, T]; Acc, Dec, Account ∧ ¬Dec(t) and the defeat sets: 0 moves (§3, §6.1) |
| changes with | L528.s2, L528.s3 (the creative-episode class; the explanation-creation class) [FROZEN] | – | **added** | under 'none' every instance of (EX) has a critical episode connected to (G), so the explanation-creation class (L528.s3) lies inside the creative-episode class (L528.s2); under V3.8 not: the bridge (a1) with no criticism meets (EX) on 16 valuations and CCE on none (worlds.createx: 21 such chains); DEP's 'Classes' still reads CCE |

### Edge counts

40 rows in the JSON, 22 named by the reply (all 22 of the tabulation's rows for section 3) and 18 added: computed 15, computed in part (a part contradicted or not settled, named in the row) 5, contradicted 2, not settled by computation 0, added 18.

### 8.1 Quotations compared (rule 14)

| where | quotation | found | note |
|---|---|---|---|
| the reply, V3.8's edge on L628 | CreativeCriticalEpisode "left unstated by L628" (FC90) | FC90's result for text 103 (its first part), not the text now | L628.n2 states "with CreativeCriticalEpisode(s,Δ,h,e)" among (EX)'s hypotheses; FC90's second part: every conjunct of (EX) is stated there. Under V3.8 that hypothesis is surplus, not false |
| the reply, V3.3 | "that ruling out is a choice that was made, not something the claim does by itself" (S28) | mixed (as the tabulation, §9, found) | the owner's words are 'That "ruling out" is a choice that was made.'; the rest is the text's (L397); read on what each says |
| the reply, V3.1's trace | "once an argument usable by an assessor rules out y…" (L369.s3) | found (L369.s3, S3) | computed: the answer y is ruled out by accepting its denial alone under V3.1; no candidate is ruled out by that alone (§4) |
| this file, §9 | the owner's words of S23, S27, S28, S41 (Q2, Q6, Q23), S47 | each found verbatim in `records/Semantics - Decisions.md` | S41's questions are Claude's; only the chosen answers are quoted as the owner's |

## 9. What the computation says of each variant and the explanation definition (for the map; nothing ruled)

| variant | which candidates meet (E) | being an explanation (Account ∧ ¬Dec(t)) | what else moves | owner's decisions the computed effect sits against (named, not ruled; rule 13) |
|---|---|---|---|---|
| V3.1 | unchanged everywhere | unchanged everywhere | who has ruled what out: a bare claim rules out its denial for whoever accepts it ("p because p" rules ¬p out for j who accepts p; ¬(Ans = y) rules out y; a record made from ψ rules out ¬ψ); (Suff)'s and (Nec)'s defeat sets reachable by accepting ¬Expl(ℰ) or Expl(ℰ) alone; D9.9's blocks lost; FC60, FC71, FC72, FC72.new1, FC72.new2 | S23 ("argument is short hand for: reasons why this and not that"): an argument whose only premise is the claim it keeps now rules out that claim's denial, with no reason why this and not that beyond the claim itself. S28 is not contradicted (the ruling out is still j's acceptance) |
| V3.2 | unchanged | unchanged | usability shrinks (8,983 generated arguments; every step above another step unless its intermediate conclusion is accepted); fewer ruled out; problems grow and stay unsolved (FC47.new1); K3 (D9.9) unusable from a failed prediction; D18.1's K2 → Live loop gone (FC69); FC47, FC53, FC68, FC70, FC71 | none computed |
| V3.3 | unchanged | unchanged | a premise alone is usable by every assessor, taken up or not: X_j, problems and the defeat sets no longer depend on j for premises alone (FC72 (f), FC72.new1 (a), (c); 703 generated Out_j F → T) | S28 ("That "ruling out" is a choice that was made"); S27 (""perpetual motion is impossible" is enough to trigger a conflict. It is not enough for a creative agent to do anything about it though."); S41 Q23 ("Yes, it's an argument", answering whether someone's using that one claim alone to rule out a design makes it an argument): under V3.3 the claim rules out with no one using it |
| V3.4 | unchanged | unchanged under D12.2 as written (CT reads Prepares); under S108-3-I2 (CT asks ExplUse) moves both ways: out where the trace's claim fails (E) while the candidate judged meets it (the reversed calculation on C_id claimed on C1; 122 / 93 / 36 / 200 generated), and in where a failed earlier construction stops excluding a later selection (92 chains) | Build, hence (G) and (EX), fail on every use of an account in error (L403.s3, FROZEN: FC90.new1 (a)) | S41 Q2 ("No, not if just declared"), under S108-3-I2 only: a link worked out by construction becomes declared because the claim its use rests on fails (E); the owner's split is between declared and worked out, not between uses right and in error |
| V3.5 | unchanged | unchanged under D12.2's cut T′ (and T) for every candidate meeting (E) (Held at o_t makes the record clause idle); moves in the tag encoding (every candidate meeting (E) whose target is labelled represented only before an unrecorded change: 22 of 27 worked cases, 1,013 / 881 / 232 / 1,670 generated) and under the rejected cut K (5,118 chains with a held output) | Episode (FC84.new1 (a3), (c), (a4); FC84.new2); Con at holdings whose t is not held | none computed (S41 Q6's "the question itself never changes" is kept: an episode still need hold no change) |
| V3.6 | unchanged | **moves in** under D12.2 as written, on S108-3-I4: every candidate meeting (E) whose history is a selection and whose t has a part the stated construction lacks (22 of 27 worked cases; 1,013 / 881 / 232 / 1,670 generated; the pole's t′ with an idle part) | Sel; the population; pairs underdetermined by the survivors on H (1,141 / 859 / 469 / 2,577 generated; each pair of the pole's C1∖H with a deviating t′); FC80 as built unmoved | none computed |
| V3.7 | unchanged | unchanged | routes that did no work are active (1,436 of 5,724 generated; FC75 (a), (a′)); ProducedBy (685 of 1,460 circuits) and ProducesVia (952 of 2,860) attribute repairs to idle contributions; L375.s2 (FROZEN) false of D11.4 | none computed |
| V3.8 | unchanged | unchanged | (EX) holds with no critical episode (7,086 of 1,929,216 valuations; the bridge with no criticism); the explanation-creation class (L528.s3) leaves the creative-episode class (L528.s2), both FROZEN; DEP's (EX) no longer reaches Crit (FC32.new1 (f)) | S47 ("The math doesn't ask for anything. The agent does when a question occurs as potentially important and worth investigating"), read strongly; the record's reading of S47 kept (EX)'s critical episode (A3's B12 not taken); with S41 Q6 ("Yes, it can", as S47 corrects it). The reply flags it for the owner's yes or no |

**Candidate definitions of explanation (rule 7), as computed here:** V3.6 changes which candidates count as explanations under the definitions as written (on S108-3-I4); V3.4 does so only under S108-3-I2; V3.5 only in the tag encoding or under the rejected cut K. V3.1, V3.2, V3.3, V3.7 and V3.8 change neither which candidates meet (E) nor which are explanations: they move ruling out, problems, defeat sets, attribution and the class of created explanations.

## 10. Unsure

- S108-3-I2 decides whether V3.4 reaches ¬Dec(t) at all; S108-3-I5 (the claim used on the widest contract) is one choice of "another ℰ sharing t" among many; with the candidate's own claim, V3.4 never moves Account ∧ ¬Dec(t) (Con ⇔ Acc).
- S108-3-I4 (parts := E's components, the stated construction := t's own) decides V3.6's reach; the program has no parts and no stated construction, and a population whose stated construction includes every part moves nothing.
- V3.5's effect on ¬Dec(t) depends on the encoding: the tag model (a label, `provenance_of`'s kind of history) and the chain model (Held computed, D12.2 after the second check) disagree for candidates meeting (E); which one the text's L197 means is a reading, named in §8.
- Dec(t) on the worked cases and the generated candidates is computed on histories set by hand (Θ by hand, I90), as the program's own claims do.
- The routes (§6.4) and the created-explanation chains (§6.5) are enumerations built here (S108-3-I6, and FC84.new1 (a4)'s Θ-values), not generators the program had; ProducedBy, ProducesVia and UsesReason are Θ-supplied in the program's claims.
- The suites ran beside other sections' suites on four CPUs; parts that reached the 45 s cap are re-run alone at cap 300 (§7.1); a counterexample found is not a timing effect, a "holds" under a cap is fewer models tried.
- "Smallest witness" is the first found in ascending size order, not a minimum over all models.
- Silence is not agreement (rule 3): items no variant of section 3 touched (D9.1, D9.2, D9.9, D9.10, D11.3, D13.7, D14.1, D15.1, D15.2, D15.5 as definitions varied) are not shown free of dependencies.

Computed by one Opus 5.5 agent under rule 5, 28 September 2026. Nothing here changes the theory's text, formal core, claims or program after round 4 (rule 11).
