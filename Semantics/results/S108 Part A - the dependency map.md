# S108 Part A - the dependency map

*Written by the map agent (Opus 5.5, fresh; rules 6 and 7 of `S108 Part A - how the replies will be read, written before sending.md`), 28 September 2026. Built by `S108 Part A - computation/map/s108_map_build.py` from the frozen template, the frozen set, the tabulation, the four "variants computed" files and their edge `.json`, and the program's D18.1 graph after round 4 (its source read, not run); every input's md5 is in the `.json` (`inputs`). An experiment on copies (rule 11): nothing here changes the theory's text, formal core, claims or program, and nothing is ruled. "Candidate" or "explanation" for what the theory judges; "model" only for the program's own small structures (S43).*

Status: complete, 28 September 2026. The candidate list (rule 7) is `S108 Part A - candidate definitions of explanation.md`.

**Corrected by the second checker** (a fresh Opus 5.5 agent, rule 9; the orchestrator's decision 1), 28 September 2026, on the critical review's O1–O13: rebuilt by `S108 Part A - computation/map/s108_map_build_second_checker.py` (the builder above with each change marked). What changed and why: `S108 Part A - the second checker on the critical review.md`. Two results here are the second checker's runs, not a section's: the owner's weathervane and two-part sign with the change read as a boundary (O1, §2's V2.3 row) and V3.5 with a construction trace spanning occurrences (O3, e3.25c); their scripts and outputs are in `S108 Part A - computation/second checker/`. Nothing ruled; nothing applied to the theory (rule 11).

## 0. What the map holds, and how to read it

| | count |
|---|---|
| nodes | 859: 815 template items (688 sentences, 127 definitions and encodings; 238 FROZEN, 577 middle) + 10 parts of the explanation definition + 32 claims + 2 cases named by edges |
| variants | 32 tabulated; 29 run; 3 flagged and not run (V1.6, V1.7, V2.8) |
| source rows | 182 (the four `.json`); 18 split by standing; 4 'none found' rows kept apart (§4) |
| edges | 221 (21 summary edges): computed 179, claimed only 31, contradicted 11; blocks 21, constrains 33, changes with 79, moves 50, independent of 38 |
| template items touched | computed 142, claimed only 26, untouched 647 (middle untouched: 473 of 577) |

- **from**: the item or items the variant varies (definitions; the sentences varied with them are in the `.json`). **to**: the items the edge names: template ids (`L<line>.s|n<k>`, `D…`, `E…`), the parts of the explanation definition (`X:…`, §1), claims (`FC…`) and two cases.
- **Kinds**: *blocks* (under the variant the item is false or has no reading); *constrains* (the item limits the variant and stays readable); *changes with* (the item's extension or wording moves with the variant); *moves* (what the item holds of changes); *independent of* (computed: the item does not move; a negative edge, kept so that "no move" is not read from silence, rule 3).
- **Standing**: *computed* (a run shows it); *contradicted* (a run shows otherwise); *claimed only* (the reply's argument, or the computing agent's where marked, with what would settle it). "cond." = shown only under the reading named. A source row whose parts differ in standing is split (`e<s>.<row>a`, `b`, …). Rows whose content is "none found" are listed apart (§4). Summary edges (`s<n>`) carry a file's own summary table where no row gives the variant's effect on (E) or on being an explanation.

## 1. The parts of the explanation definition (nodes `X:…`)

Being an explanation, now: Account(ℰ) ∧ ¬Dec(t) (D16.XV; L17.n2, L49.n3, L61.n2, L69.n3), with Account = (E) = Acc (D6.7). "Reads": by the statement; "D18.1 ancestors": every definition upstream of the node in the program's graph.

| node | defined by [mark] | statement | reads (by its statement) | D18.1 ancestors (definitions) |
|---|---|---|---|---|
| X:(E) | D6.7 [S2] | Acc(ℰ) :⟺ F1_C ∧ F2_C ∧ A_C ∧ Dependence ∧ NonVacuous; arguments (D, C, b0, Q, δ_D, E, t, Γ, δ_E, Σ): no assessor, no history, no provenance, no grain (FC30) | X:(F1), X:(F2), X:(A), X:Dependence, X:NonVacuous | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.5, D3.7, D4.1, D4.4, D5.4, D5.5, D5.6, D6.1, D6.2, D6.4, D6.5, D6.6, D6.9 |
| X:(F1) | D5.4 [FROZEN] | ∀k ∈ Γ ∀(a,b) ∈ C: proj^λ_{V_k}[Sol_{N_k}(a,b)] = L^E_k(τ(a),σ(b)) | D1.4, D5.2, D5.1, D5.3, D1.1 | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.7, D4.1, D4.4 |
| X:(F2) | D5.5 [FROZEN] | ∀(a,b) ∈ C: π[Sol_D(a,b)] = Sol_E(τ(a),σ(b)); Hom(τ) | D1.2, D5.1, D1.1 | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.7, D4.1, D4.4 |
| X:(A) | D5.6 [FROZEN] | ∀(a,b) ∈ C: Ans_E(τ(a),σ(b)) = Ans_p(a,b), ⊥ = ⊥ | D3.2, D5.3, D5.1 | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.7, D4.1, D4.4 |
| X:Dependence | D6.5 [S2], D6.4 [S2], D6.2 [FROZEN], D6.1 [FROZEN] | ∃(a,b) ∈ C, ∅ ≠ G ⊆ Γ: Contrast(E;x) ∧ Lost(E,G;x); NC0 holds of every candidate | D6.4, D6.2, D6.1, D1.3, D3.2, D5.3 | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.7 |
| X:NonVacuous | D6.6 [FROZEN] | Sol_D(1,b0) ≠ ∅ ∧ Stated(C,Σ) | D1.2, D3.5, D0.2 | D1.1, D1.2, D1.3, D1.4, D3.5 |
| X:Dec | D12.3 [S2] | a holding reached by transfer inherits prov (D12.4); otherwise Dec(t,o_t) :⟺ no parameters give Sel(t;·) and none give Con(t;·), on h(t,o_t) | D12.1, D12.2, D12.4, D13.3, D15.8, D13.8, D5.7, D12.5 | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.7, D4.1, D4.4, D5.4, D5.5, D11.2, D11.3, D11.5, D12.1, D12.2, D12.5, D13.8, D15.8 |
| X:Expl | D16.XV [S4] | Expl an atom; Acc(ℰ) ∧ Dec(t) ⇒ ¬Expl(ℰ) (S41 Q2); written in the text as Account(ℰ) ∧ ¬Dec(t) (L17.n2, L49.n3, L61.n2, L69.n3) | X:(E), X:Dec | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.5, D3.7, D4.1, D4.4, D5.4, D5.5, D5.6, D6.1, D6.2, D6.4, D6.5, D6.6, D6.7, D6.8, D6.9, D6.10, D9.1, D9.2, D9.3, D9.4, D9.5, D9.6, D9.7, D11.1, D11.2, D11.3, D11.5, D12.1, D12.2, D12.3, D12.4, D12.5, D12.9, D13.8, D15.8 |
| X:(Suff) | D16.XV [S4] | defeated for j ⟺ ∃ℰ [Acc(ℰ) ∧ ¬Dec(t) ∧ ∃α ∈ X_j(Expl(ℰ)): Acc ∉ Uses(α)] | X:(E), X:Dec, D9.8, D9.6, D9.7 | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.5, D3.7, D4.1, D4.4, D5.4, D5.5, D5.6, D6.1, D6.2, D6.4, D6.5, D6.6, D6.7, D6.8, D6.9, D6.10, D9.1, D9.2, D9.3, D9.4, D9.5, D9.6, D9.7, D11.1, D11.2, D11.3, D11.5, D12.1, D12.2, D12.3, D12.4, D12.5, D12.9, D13.8, D15.8 |
| X:(Nec) | D16.XV [S4] | defeated for j ⟺ ∃ℰ [∃α ∈ X_j(¬Expl(ℰ)): Acc ∉ Uses(α) ∧ ∀C′ on D ∀t′: ¬Faithful_{C′}(t′: D → E)] | D9.8, D9.6, D9.7, D5.7 | D1.1, D1.2, D1.3, D1.4, D3.1, D3.2, D3.5, D3.7, D4.1, D4.4, D5.4, D5.5, D5.6, D6.1, D6.2, D6.4, D6.5, D6.6, D6.7, D6.8, D6.9, D6.10, D9.1, D9.2, D9.3, D9.4, D9.5, D9.6, D9.7, D11.1, D11.2, D11.3, D11.5, D12.1, D12.2, D12.3, D12.4, D12.5, D12.9, D13.8, D15.8 |

Ancestor symbols that are no definition (D0.2's primitives, declared inputs, Θ): (E): C, δ; Dec: BindingConstruction, C, ImmAfter, Org, Prepares, Rec_h', TransferComposite, parts, q(o), stated construction, surv, Θ; D16.XV's node: Accepted, BindingConstruction, C, Expl, FailsToCapture, Forms, ImmAfter, MadeFrom, NotCreative, OperatesOn, Org, Out, Prepares, Rec_h', Scope, TransferComposite, WithoutLoss, Work, parts, q(o), stated construction, surv, Θ, δ.

## 2. How the explanation definition changes with each varied item (computed)

Counts: worked cases; generated candidates at scale 4, SMALL / SMALL with value maps / proper targets / MID (section 2: single / value maps / MID proper). "Being an explanation as the variant defines it" differs from Account ∧ ¬Dec(t) only for V4.1–V4.3, which redefine it. Last column: is the varied item's node upstream of (E) / Dec / D16.XV's defeat conditions in D18.1's graph (static, not run). Where a history is built so that the variant bites on every account (V2.5's 'nothing tried', V3.5's tag history, V3.6's 'Sel-parts', V4.2's declared and V4.3's relayed histories), the counts equal the population meeting (E), by construction of the history (§6.3).

| variant | item [mark] | Acc (E) | Account ∧ ¬Dec(t) | being an explanation as redefined | what else moves | suite (claims whose status moves) | D18.1 reach (E) / Dec / defeat |
|---|---|---|---|---|---|---|---|
| V1.1 | D1.4 [S1] | out 15 of 27 worked (E1 forward C1–C3, E_rev on C_id, M13, E5 ×2, E8, E9 ×2, the two-part sign, …); in ℰ_bv (S108-1-I1 (i)); generated in 16 / 13 / 1 / 19, out 199 / 203 / 30 / 358 | moves exactly where Acc moves | (as now) | Dec moves alone through Sel's fidelity (1,360 / 1,211 / 106 / 2,212), never moving Account ∧ ¬Dec(t) alone | 21 claims | yes / yes / yes |
| V1.2 | D2.1 [S1] | 0 | 0 | (as now) | Set_v, asg, Prod (549 of 17,280), families; FC06, FC09 (L347.s2 [FROZEN]) | 5 claims | – / – / – |
| V1.3 | D2.4 [S1] | 0 | 0 | (as now) | families (57 of 17,280) | 0 claims | – / – / – |
| V1.4 | D3.3 [S1] | 0 | 0 | (as now) | Ident's contract clause (1,113 of 17,280; C_id no longer an identification contract) | 3 claims | – / – / – |
| V1.5 | D3.4 [S1] | out: every candidate of a question with no recorded contract history, under S108-1-I5: 22 of 22 worked with Acc T; generated 961 / 886 / 221 / 1,674; with ρ_p recorded by hand: 0 | moves exactly where Acc moves | (as now) | reads nothing of (D, C, Q) but ρ_p | 15 claims | – / – / – |
| V1.6 | D3.6 [S1] | not computed (flagged) | not computed | not computed | – | – | – / – / – |
| V1.7 | D0.2 [S1] | not computed (flagged); I85's default scope already equals V1.7's formula on every question the program builds | not computed | (as now) | – | – | yes / – / yes |
| V1.8 | D2.6 [S1] | 0 | 0 | (as now) | rule and measurement families emptied (2,413 and 169 of 17,280 → 0); idle on the pole | 1 claim | – / – / – |
| V2.1 | D6.4 [S2] | in: generated 57 / 74 / 8; worked 0 | the same movers (Con, Sel histories) | (as now) | routes: ∅ ∈ S for 63; 120 routes with no critical block | 0 claims | yes / – / yes |
| V2.2 | D6.4 [S2] | out: generated 23 / 20 / 4; the built L307 case; worked 0 | the same | (as now) | every route has a critical singleton; L307's S realized by none (17 → 0) | 0 claims | yes / – / yes |
| V2.3 | D6.4 [S2] | out: generated 253 / 213 / 65 (every account on {1}×B: 168 → 0); E_rev and E_fwd on C_id; the owner's weathervane and two-part sign where the change (the wind, the day) is read as a boundary: FC28.new2's D_vane (Γ = {cP} or {cW,cP}) and the sign with B = {mon, tue}, A = {1}, Acc T → F, E_enc on each question too (second checker, O1); with the change read as an edit (M13, claims_s106) nothing moves | the same (4 worked (case, history)) | (as now) | – | 2 claims | yes / – / yes |
| V2.4 | D6.7 [S2] | out: 11 worked (E_enc C1, C2; 'p because p'; M1–M3; the one-part sign; ℰ_myth1; the hand-turned vane; E8's identity candidate; E_rev τ′); generated 972 / 776 / 301 of 1,027 / 847 / 310 | the same (22 worked (case, history)) | (as now) | Bearing (D9.10) of K1's criticism; (E) reads D6.3's quantifier again | 6 claims + 2 parts | yes / – / yes |
| V2.5 | D12.1 [S2] | 0 | in: every account on a history with nothing tried and no earlier representation: 28 of 28 worked; generated 1,027 / 847 / 310; FC30.new1 (e) in, (d) stays out | (as now) | FC77 counterexample | 2 claims | – / yes / yes |
| V2.6 | D8.2 [S2] | 0 | 0 | (as now) | rivalry and kind ii: 310 of 310 kind-ii pairs lose rivalry; 492 kind-i pairs lose outside-C conflicts | 1 claim | – / – / – |
| V2.7 | D8.5 [S2] | 0 | 0 | (as now) | ConfCl: 410 of 1,822 lost | 1 claim | – / – / – |
| V2.8 | D9.8 [S2] | not computed (flagged); its reading computed as V4.4 | not computed | (as now) | – | – | – / – / – |
| V3.1 | D9.7 [S3] | 0 | 0 | (as now) | Out_j: 1,677 of 9,600 F → T; (Suff)/(Nec) defeat sets by acceptance alone | 5 claims | – / – / yes |
| V3.2 | D9.4 [S3] | 0 | 0 | (as now) | usability 8,983 T → F; problems grow (FC47.new1) | 7 claims | – / – / yes |
| V3.3 | D9.6 [S3] | 0 | 0 | (as now) | usability 2,621 F → T; Out_j 703; ruling out no longer depends on j for premises alone | 2 claims | – / – / yes |
| V3.4 | D13.3 [S3] | 0 | 0 with D12.2 as written; under S108-3-I2: out 122 / 93 / 36 / 200 (claim used on the widest contract), and in and out on provenance chains (Dec F → T 546, T → F 92, T′) | (as now) | Build T → F on every use of an account failing (E) (L403.s3 [FROZEN]) | 1 claim | – / – / – |
| V3.5 | D13.8 [S3] | 0 | 0 under D12.2's cut T′ (and T) for every candidate meeting (E) when the trace lies at o_t (the program's encoding: Prepares a label at one occurrence, I56); in where the output's trace spans an unrecorded change of contract and Prepares(h′, o_t, ·) asks h′ to hold the trace's occurrences: every held output with such a trace, Dec T → F (second checker, O3: chains n ≤ 4: 45,072 of the 90,144 held-output chains whose output trace spans an unrecorded change, every one with a trace at the output; 0 where the trace lies at o_t (0 of 57,700, and 11,240 not held: section 3's counts) or spans occurrences with no unrecorded change; smallest n = 2, trace from o1 to o2 across C → C′ unrecorded); in, in the tag encoding: 22 of 27 worked, 1,013 / 881 / 232 / 1,670; under the rejected cut K: 5,118 chains | (as now) | Episode; Con at holdings whose t is not held | 1 claim | – / yes / yes |
| V3.6 | D15.8 [S3] | 0 | in (S108-3-I4, history 'Sel-parts': parts := E's components, stated construction := all but E's last component): 22 of 27 worked; generated 1,013 / 881 / 232 / 1,670; with the stated construction t's own, t does not move and only t′ = t + an idle part does (the same counts) | (as now) | pairs newly underdetermined 1,141 / 859 / 469 / 2,577 | 0 claims (text only) | – / yes / yes |
| V3.7 | D11.4 [S3] | 0 | 0 | (as now) | ActRoute 1,436 of 5,724 F → T; ProducedBy, ProducesVia | 1 claim | – / – / – |
| V3.8 | D14.7 [S3] | 0 | 0 | (as now) | CreateEx 7,086 of 1,929,216 valuations F → T | 1 claim | – / – / – |
| V4.1 | D16.XV [S4] | 0 | 0 | out: 10 of 29 worked (the one-part sign, E_enc, 'p because p', M1–M3, the hand-turned vane, E8's identity candidate, E_rev τ′ on C_H); generated 941 of 1,019 (MID 1,590 of 1,686) | (Suff) fails by definition unless its antecedent co-varies | 1–2 claims | – / – / yes |
| V4.2 | D16.XV [S4] | 0 | 0 | in: 24 of 24 worked under a declared or unrecorded history; the student's declared copy; a link no pair tried; CT8's R2, R4; FC-E 7; CT 4; generated 1,019 (MID 1,686) | FC30.new1 (c), FC23.new2 (f) fail | 2 claims | – / – / yes |
| V4.3 | D16.XV [S4] | 0 | 0 | out, only at holdings reached by a transfer: reading (a) 24 + 24 worked, 1,019 + 1,019 generated; (b) 24, 1,019; (c) 0 | D12.4's inherited provenance no longer enough | 0 claims (text only) | – / – / yes |
| V4.4 | D16.XV [S4] | 0 | 0 | (as now) | (Suff) defeat set grows 1,019 (Con), 1,019 (Sel); (Nec) 3,979 | 0 claims | – / – / yes |
| V4.5 | D16.XV [S4] | 0 | 0 | (as now) | (Nec) exposure +4 worked, +2,138 generated, all with Acc F | 0 claims | – / – / yes |
| V4.6 | D16.4 [S4] | 0 | 0 | (as now) | 𝔈_Θ +1 of 17,280, +2 of 25,920 searched witnesses | 0 claims | – / – / – |
| V4.7 | D16.3 [S4] | 0 | 0 | (as now) | toy only: UU F → T on 217 of 484 | 0 claims | – / – / – |
| V4.8 | D12.9 [S4], D16.XV [S4] | 0 | 0 | (as now) | (Prov)(i) satisfiable: 1,647 of 9,768 wide populations; 0 of FC80's own | 0 claims (text only) | – / – / yes |

### What the computation shows about the dependencies of the explanation definition (short)

- **(E) moves only when its own reads move.** Of the 29 variants run, six move which candidates meet (E): V1.1 (D1.4, what (F1) reads), V2.1–V2.3 (D6.4, Dependence's witness), V2.4 (D6.7, (E) itself) and V1.5, whose reading adds a conjunct "p is a question" to (E) (S108-1-I5). Every other section-1 item varied (D2.1, D2.4, D2.6, D3.3) moves families, Prod or Ident and never (E) (0 of 61,914 generated candidates), as D18.1's graph has it (Roles and Respects are not upstream of (E)).
- **Being an explanation moves with Dec and with D16.XV's rule, not with (E).** With (E) unmoved: V2.5 (D12.1, Sel with H = ∅), V3.6 (D15.8, the population's parts clause; on S108-3-I4) and V4.1–V4.3 (D16.XV). V3.4 (D13.3's ExplUse) and V3.5 (D13.8's record clause) reach Dec only under a reading: D12.2 as written reads Prepares, not ExplUse (contradicted, e3.20a); and its Held(o′, x) at o′ ⪯ o_t makes the record clause idle for every candidate meeting (E) when the trace lies at o_t (0 of 115,400 chains, cut T′; e3.25a, e3.26), not when the trace spans an unrecorded change of contract (e3.25c, the second checker's run: every such held output moves).
- **D18.1's reach is needed, and not enough.** Every computed move of Acc or of Account ∧ ¬Dec(t) is of a variant whose node the graph places upstream of (E) or Dec, or of one whose reading adds that edge (V1.5: ρ_p into (E); V3.4 under S108-3-I2: ExplUse into CT). One reach carries no move for candidates meeting (E) in the program's encoding: V3.5 (Episode → Con → Dec), screened by Held at o_t when the trace lies at o_t (§2's last column); with a trace spanning an unrecorded change the reach carries (e3.25c).
- **What the owner's changes are read as.** V2.3 (a contrast needs an edit) keeps the owner's weathervane and two-part sign as the program encodes them (the wind and Tuesday as edits: M13, `claims_s106`) and drops both, with every candidate on their questions, when the change is read as a boundary (FC28.new2's D_vane; the sign with Monday and Tuesday as boundaries): the second checker's run, §2.
- **Ruling out, conflict, creation and universality are downstream or aside.** V3.1–V3.3 (D9.7, D9.4, D9.6) and V4.4 move who has ruled what out, problems and the (Suff)/(Nec) defeat sets, never (E) or being an explanation; V2.6, V2.7 (D8.2, D8.5) move rivalry and conflict with a claim; V3.7, V3.8 (D11.4, D14.7) move (P) attribution and (EX); V4.6–V4.8 move 𝔈_Θ, UU (a toy) and (Prov)(i). Each with 0 moves of Acc and of Account ∧ ¬Dec(t) (§2).
- **Where the frozen words hold the middle.** Computed blocks of FROZEN items: D4.4 (V1.1); L347.s2 (V1.2, V1.8); L307.s1 (V2.2); L315.s1, L317.s6 (V2.6); L403.s3 (V3.4); L375.s2 (V3.7); L495.s1 (V4.7, toy only); and L528.s2–s3 change with V3.8, D13.4 and D13.5 with V1.1 (V1.1 blocks the claim FC85 (a), 'a content matches itself', which D13.4 does not state). By the template's own rule a variant that blocks a FROZEN item is not a reading of the frozen words (§3). No flagged candidate of V2.3, V2.4, V2.5, V4.1, V4.2 blocks a FROZEN item: what they sit against is an owner's decision (the candidate list).
- **The replies' claims the computation contradicts: 11 edges** (§5); among them the replies' routes from D13.3 and D13.8 to Dec (the latter only where the trace lies at o_t), V2.3's block of L329.s3, V4.5's reach to E5, V4.3's "no record" case, and V2.2's "every candidate realizing L299.s1 fails (E)". V3.2's "fewer problems" is now a computed move with the reply's direction contradicted (problems grow; e3.09b).

## 3. FROZEN items the variants reach

Every edge whose target is FROZEN, by standing. A FROZEN item *blocked* (computed) marks a variant that is, by the template's rule, not a reading of the frozen words.

| FROZEN item | edges (variant: kind, standing) |
|---|---|
| D2.2 | e1.15 V1.2: constrains, computed |
| D2.5 | e1.16 V1.2: constrains, computed |
| D3.1 | e1.37 V1.5: constrains, claimed only |
| D3.5 | e1.48 V1.7: blocks, claimed only |
| D4.4 | e1.00 V1.1: blocks, computed |
| D5.2 | e1.01 V1.1: constrains, computed |
| D5.3 | e4.31 V4.6: constrains, computed |
| D5.5 | e2.31 V2.5: changes with, computed |
| D6.6 | e1.45 V1.6: constrains, claimed only; e1.49 V1.7: constrains, claimed only |
| D6.10 | e2.30 V2.4: changes with, computed |
| D7.2 | e1.10 V1.1: changes with, computed; e2.01 V2.1: changes with, computed |
| D7.3 | e1.10 V1.1: changes with, computed; e2.23 V2.1: changes with, computed; e2.27 V2.2: changes with, computed |
| D8.4 | e2.18 V2.7: constrains, computed |
| D8.6 | e2.19 V2.7: changes with, claimed only |
| D9.11 | e3.34b V3.7: moves, claimed only |
| D10.1 | e2.16b V2.6: moves, computed; e3.07 V3.1: moves, computed; e3.09b V3.2: moves, computed; e3.17 V3.3: moves, computed |
| D10.2 | e2.34 V2.1/V2.2/V2.3/V2.4: independent of, computed |
| D10.4 | e2.05 V2.2: changes with, contradicted; e2.16b V2.6: moves, computed |
| D12.4 | e4.17 V4.3: constrains, computed; e4.20 V4.3: changes with, computed |
| D12.5 | e1.09 V1.1: constrains, computed; e4.36 V4.7: changes with, computed |
| D13.4 | e1.08b V1.1: changes with, computed |
| D13.5 | e1.08b V1.1: changes with, computed |
| D13.6 | e3.22 V3.4: moves, computed |
| D14.3 | e3.34a V3.7: moves, computed |
| D14.6 | e3.34a V3.7: moves, computed |
| E3 | e3.05 V3.1: changes with, computed |
| E5 | e4.28 V4.5: changes with, contradicted |
| E8 | e1.41 V1.5: changes with, computed; e2.29 V2.4: moves, computed |
| L57.s1 | e1.21 V1.2: changes with, computed; e1.53 V1.8: constrains, computed |
| L103.s2 | e1.14 V1.2: blocks, claimed only |
| L124.s1 | e1.27 V1.3: constrains, computed |
| L125.s1 | e1.27 V1.3: constrains, computed |
| L151.s2 | e1.31 V1.4: constrains, computed |
| L155.s6 | e1.37 V1.5: constrains, claimed only |
| L161.s1 | e1.45 V1.6: constrains, claimed only |
| L161.s2 | e1.45 V1.6: constrains, claimed only |
| L161.s3 | e1.45 V1.6: constrains, claimed only |
| L195.s1 | e2.12 V2.5: constrains, computed |
| L253.s1 | e2.08 V2.3: constrains, computed |
| L289.s1 | e2.01 V2.1: changes with, computed |
| L293.s1 | e2.23 V2.1: changes with, computed |
| L299.s1 | e2.04a V2.2: constrains, computed |
| L307.s1 | e2.25 V2.2: blocks, computed |
| L309.s1 | e2.22 V2.1: independent of, computed |
| L311.s2 | e2.03 V2.2: blocks, claimed only |
| L315.s1 | e2.15 V2.6: blocks, computed |
| L317.s6 | e2.15 V2.6: blocks, computed |
| L317.s15 | e1.50 V1.7: independent of, claimed only |
| L329.s3 | e2.06a V2.3: blocks, contradicted |
| L347.s2 | e1.23 V1.2: blocks, computed; e1.52 V1.8: blocks, computed |
| L375.s2 | e3.33 V3.7: blocks, computed |
| L389.s1 | e3.08 V3.2: constrains, computed |
| L397.s5 | e3.00 V3.1: constrains, computed; e3.15 V3.3: constrains, computed |
| L403.s3 | e3.19 V3.4: blocks, computed |
| L495.s1 | e4.34 V4.7: blocks, computed (cond.) |
| L528.s1 | e4.37 V4.7: changes with, computed |
| L528.s2 | e3.39 V3.8: changes with, computed; e4.37 V4.7: changes with, computed |
| L528.s3 | e3.39 V3.8: changes with, computed; e4.37 V4.7: changes with, computed |
| L528.s4 | e4.37 V4.7: changes with, computed |
| L574.s2 | e4.38 V4.8: constrains, computed |

60 of 238 FROZEN items are named by an edge; blocks computed: D4.4, L307.s1, L315.s1, L317.s6, L347.s2, L375.s2, L403.s3, L495.s1.

## 4. The edges

What shows it is cut here; whole in the `.json` (`what_shows_it`, `reply_why`, `what_would_settle`, `note`). For a claimed-only edge the cell gives the argument and what would settle it.


### Section 1

| id | variant | from | kind | to [mark] | standing | what shows it (cut) |
|---|---|---|---|---|---|---|
| e1.00 | V1.1 | D1.4 | blocks | D4.4 [FROZEN] | computed | sig_C({c_L}) != sig_C(c_L) at 7/7 pairs of C1, 15/15 of C2; generated SMALL: 7,552 of 17,280 (D,C) with sig_C({j}) != sig_C(j) for some j (I14: none) |
| e1.01 | V1.1 | D1.4 | constrains | D5.2 [FROZEN] | computed | FC-E4 at set(N=0,X=1): proj Sol_{c_N,c_Y} on (N,Y) [(0,0),(0,1)] -> [(0,1)]; c_M's constraint enters through Sol_D; D5.2's formula unchanged |
| e1.02 | V1.1 | D1.4 | changes with | L233.s1 [S2] | claimed only | argument: L233's wording is the old reading · settle: a reading of L233.s1 against the variant; no run settles it |
| e1.03 | V1.1 | D1.4 | changes with | L556.n2 [S4] | claimed only | argument: Argument 1's signatures recomputed · settle: a reading of the sentence against Argument 1's use |
| e1.04 | V1.1 | D1.4 | changes with | FC17 [claim], FC18 [claim] | contradicted | recomputed under V1.1: FC17 and FC18 hold; only FC18's I94 look changes its witness |
| e1.05 | V1.1 | D1.4 | moves | X:(F1) | computed | E_fwd Acc T->F on C1, C2, C3 ((F1) fails at every pair); ℰ_bv F->T on C1, C2 under S108-1-I1 (i), F both under (ii) |
| e1.06 | V1.1 | D1.4 | moves | X:(E), X:Expl | computed | 15 of 27 T->F: E1 forward C1-C3, E_rev tau' on C_H, E_rev on C_id (L325.n6, L271.s2), M2, M5, M13 (S41 Q15), E5 x2 (L339), E8 (FC107), E9 x2 (L626, L630), S44 two-part sign, day-port sign; … |
| e1.07 | V1.1 | D1.4 | changes with | D12.1 [S2], X:Dec | computed | Dec(t) under a hand-set selection history moves in 14 worked cases and 1,360/1,211/106/2,212 generated; CT8 under T': constructed -> declared; FC12.new2, FC12.new3, FC104.new1 move; … |
| e1.08a | V1.1 | D1.4 | blocks | FC85 [claim] | computed | FC85 (a) ('a content matches itself') holds → counterexample: the identity transport c → c is not faithful (two components on one port, one empty) |
| e1.08b | V1.1 | D1.4 | changes with | D13.4 [FROZEN], D13.5 [FROZEN] | computed | both stay readable; D13.4 states no reflexivity (read with c fixed, L413; not claimed symmetric, FC85), and with c ≢ c (N) can call a content already held new |
| e1.09 | V1.1 | D1.4 | constrains | D12.5 [FROZEN] | computed | FC95 (L211: a system represents a theory in error): no faithful transport o -> c |
| e1.10 | V1.1 | D1.4 | changes with | D7.2 [FROZEN], D7.3 [FROZEN], D7.4 [S2] | computed | FC-E1: routes {{d,k}} -> empty, d no longer critical; FC42.new1: /Boundary/ -> 0 |
| e1.11 | V1.1 | D1.4 | moves | X:(E), FC72.new2 [claim] | computed | FC72.new2 (a): tilt T->F, myth2 T->F, myth1 (a written-in slot) stays T; (d) the finer question's test moves |
| e1.12 | V1.1 | D1.4 | moves | FC99 [claim], FC101 [claim] | computed | FC99 (the account fails already on C), FC101 (b) |
| e1.13 | V1.1 | D1.4 | moves | X:(E) | computed | SMALL out 199, in 16 (vm 203/13; proper 30/1; MID 358/19); most at pairs where Sol_D is empty; ins at non-empty solutions write in a value D's other components fix |
| e1.14 | V1.2 | D2.1 | blocks | L103.s2 [FROZEN] | claimed only | argument: a setting that alters k 'adds an equation beside' · settle: a reading: does 'an equation beside an incompatible one' cover an alteration of another … |
| e1.15 | V1.2 | D2.1 | constrains | D2.2 [FROZEN] | computed | Input differs on 2,107 of 17,280 generated targets (only grows); pole: unchanged |
| e1.16 | V1.2 | D2.1 | constrains | D2.5 [FROZEN] | computed | asg differs on 1,758 of 17,280; pole: unchanged |
| e1.17 | V1.2 | D2.1 | changes with | D2.6 [S1] | computed | Slc_j reads asg, not Set_v: moves only where asg moves (Slc 881 of 17,280); pole unchanged (108,108,128) |
| e1.18 | V1.2 | D2.1 | changes with | D2.4 [S1] | computed | Obs (R-ii) moves on 18 of 17,280; pole: empty both ways |
| e1.19 | V1.2 | D2.1 | changes with | E1 [S2] | computed | E1's edits still replace their components; composites now set each port they set (/Set_H/ 3 -> 143); Prod(p*) F -> T; C1's Prod unchanged |
| e1.20 | V1.2 | D2.1 | changes with | FC27.new1 [claim] | contradicted | FC27.new1 unchanged under V1.2 (every part, status and text) |
| e1.21 | V1.2 | D2.1 | changes with | D2.6 [S1], L57.s1 [FROZEN] | computed | on the pole's C2* (R-ii) families unchanged with Slc unchanged: no co-variation needed there; on L347's case (FC09) the rule family is lost with Slc as it stands |
| e1.22a | V1.2 | D2.1 | independent of | X:(E), X:Expl | computed | no conjunct of (E) moves (0 of 61,914 generated) |
| e1.22b | V1.2 | D2.1 | moves | D3.3 [S1] | computed | Prod(p) moves on 549 of 17,280 (the respect 'production') |
| e1.23 | V1.2 | D2.1 | blocks | L347.s2 [FROZEN] | computed | FC09 HOLDS -> counterexample: c_r loses Rule_C under both readings (World_{c_r} now holds edits that alter c_r) |
| e1.24 | V1.2 | D2.1 | blocks | L119.n8 [S1] | computed | FC06 HOLDS -> counterexample: [alt:k0] sets p0 through h_p0 and alters k0 |
| e1.25 | V1.2 | D2.1 | changes with | L123.n1 [S1], FC2.new1 [claim], FC4.new1 [claim], FC07 [claim], FC08 [claim] | computed | FC2.new1 (R-i part), FC4.new1 (both readings), FC07 (C2 under R-i) -> counterexample; FC08's witness lost |
| e1.26 | V1.2 | D2.1 | changes with | FC-E3 | computed | every row 'both invariant under the settings of X' yes -> no; 'reproduced: no' |
| s00 | V1.2 | D2.1 | independent of | X:Dec | computed | Dec(t) (Sel-history) 0 moves (§3) |
| e1.27 | V1.3 | D2.4 | constrains | L124.s1 [FROZEN], L125.s1 [FROZEN] | computed | pole C2: causal {c_H,c_L,c_T} -> {c_H,c_T}, meas {} -> {(c_L,H),(c_L,T)}; generated families differ on 57 of 17,280 (MID 143 of 25,920) |
| e1.28 | V1.3 | D2.4 | changes with | L123.n1 [S1], D4.6 [S1] | computed | FC2.new1's for-all part (R-i) holds and is now the default reading's |
| e1.29 | V1.3 | D2.4 | independent of | X:(E), X:Expl | computed | Acc: 0 moves anywhere; the whole suite: no status moves (2 texts name the default reading) |
| s01 | V1.3 | D2.4 | independent of | X:Dec | computed | 0 moves (§3) |
| e1.30 | V1.4 | D3.3 | constrains | L151.s1 [S1] | computed | Prod moves on 0 generated questions; the clause reads (Q, C, b0) only |
| e1.31 | V1.4 | D3.3 | constrains | L151.s2 [FROZEN] | computed | Prod untouched (0 moves) |
| e1.32 | V1.4 | D3.3 | changes with | E1 [S2], L271.s2 [S2], L325.n6 [S2] | computed | C_id's contract clause T -> F; E_rev on C_id Acc T both, so L325.n6's 'faithful under the identification contract' names a contract D3.3 no longer calls one |
| e1.33 | V1.4 | D3.3 | changes with | FC28 [claim], FC28.new2 [claim], FC28.new1 [claim] | computed | both HOLDS -> counterexample; FC28.new1 too |
| e1.34a | V1.4 | D3.3 | independent of | X:(E), X:Expl | computed | Acc 0 moves anywhere |
| e1.34b | V1.4 | D3.3 | moves | D3.3 [S1] | computed | what meeting (E) on C_id answers: C_id no longer an identification contract |
| e1.35 | V1.4 | D3.3 | changes with | D3.3 [S1] | computed | FC28.new2's still/north (boundaries only): identification under I163, not under V1.4; 'the three readings agree on C_id' flips |
| s02 | V1.4 | D3.3 | independent of | X:Dec | computed | 0 moves (§3) |
| e1.36 | V1.5 | D3.4 | blocks | L155.s2 [S1], L155.s5 [S1] | claimed only | argument: declared contracts and 'any of the three' negated · settle: nothing computable: a definitional consequence |
| e1.37 | V1.5 | D3.4 | constrains | L155.s6 [FROZEN], D3.1 [FROZEN] | claimed only | argument: found => constructed readable; the slot stays · settle: encode a found question with its trace |
| e1.38 | V1.5 | D3.4 | changes with | D13.8 [S3] | claimed only | argument: episode records and question-finding quantify over contracts that must now be … · settle: give q(o) a rho_p and compute Episode and Con under V1.5 |
| e1.39 | V1.5 | D3.4 | changes with | D16.4 [S4] | claimed only | argument: as S1#38 (tabulation §4) · settle: a finite 𝔈_Θ over the program's questions with rho_p recorded |
| e1.40 | V1.5 | D3.4 | changes with | L544.s1 [S4] | claimed only | argument: as S1#38 (tabulation §4) · settle: definitions of the two terms |
| e1.41 | V1.5 | D3.4 | changes with | E8 [FROZEN] | computed | E8's p_δ candidate Acc T -> F; FC107's text moves |
| e1.42 | V1.5 | D3.4 | moves | X:(E), X:Expl | computed; cond.: under S108-1-I5 (no recorded contract history = declared); 0 moves with ρ_p recorded | every Acc-T worked case (22), FC-E1, FC-E4, CT1, CT2, CT5, all generated (961/886/221/1,674) -> F; with rho_p set by hand to selected or constructed: 0 moves |
| e1.43 | V1.5 | D3.4 | moves | X:(E), X:Expl | computed; cond.: under S108-1-I5 | two-part sign, one-part sign, E_enc on the sign's question; M13 and E_enc on the weathervane's question: all F |
| e1.44 | V1.5 | D3.4 | changes with | FC34 [claim], FC74 [claim] | computed | their witnesses no longer found: no candidate meets (E) on any question the searches build |
| e1.45 | V1.6 | D3.6 | constrains | L161.s1 [FROZEN], L161.s2 [FROZEN], L161.s3 [FROZEN], D6.6 [FROZEN] | claimed only | argument: defective questions stay questions; NonVacuous keeps BadBaseline, the variant adds the … · settle: the orchestrator's ruling on scope and S40; then a Desc (I76) for the worked … |
| e1.46 | V1.6 | D3.6 | changes with | X:(Suff), X:(Nec), FC106 [claim] | claimed only | argument: the defeat sets would quantify over non-defective p; FC106's untested parts become … · settle: as above; FC106's two untested defects need Desc |
| e1.47 | V1.6 | D3.6 | moves | X:Expl | claimed only | argument: gains the question's non-defect beside Account ∧ ¬Dec(t) · settle: as above; formula (on Acc) and trace (on being an explanation) are two variants |
| e1.48 | V1.7 | D0.2 | blocks | D3.5 [FROZEN], L43.s4 [S1], L159.s1 [S1] | claimed only | argument: 'Σ is a declared input naming Excl(Σ)'; the stated-scope requirement and grievance 4's … · settle: the orchestrator's ruling |
| e1.49 | V1.7 | D0.2 | constrains | D6.6 [FROZEN] | claimed only | argument: NonVacuous keeps its form; its second conjunct becomes vacuous · settle: the orchestrator's ruling |
| e1.50 | V1.7 | D0.2 | independent of | L317.s15 [FROZEN] | claimed only | argument: the theory hangs together; L317.s15 is safe (narrowing still makes a new question) · settle: the orchestrator's ruling |
| e1.51 | V1.7 | D0.2 | moves | X:NonVacuous | claimed only | argument: silently narrowed contracts newly meet (E) · settle: the orchestrator's ruling |
| e1.52 | V1.8 | D2.6 | blocks | L347.s2 [FROZEN] | computed | FC09 HOLDS -> counterexample: c_r loses Rule_C under both readings; generated: rule family nonempty 2,413 of 17,280 under none, 0 under V1.8 |
| e1.53 | V1.8 | D2.6 | constrains | L57.s1 [FROZEN] | computed | rule and (R-ii) measurement families empty on every generated (D, C) (2,413 and 169 -> 0); causal families stand |
| e1.54 | V1.8 | D2.6 | changes with | D4.6 [S1], L123.n1 [S1] | computed | families differ on 2,419 of 17,280; Obs (R-ii) nonempty 17 -> 0 |
| e1.55 | V1.8 | D2.6 | independent of | X:(E), X:Expl | computed | Acc: 0 moves anywhere |
| e1.56 | V1.8 | D2.6 | independent of | E1 [S2] | computed | on the pole Slc_j = Alt_j already: V1.8 changes nothing there (the list does not move because nothing does) |
| e1.57 | V1.8 | D2.6 | changes with | FC-E3 | computed | with recal(c_N): c_N's rule family yes -> no; under R-ii c_N causal no -> yes; 'no longer share their families' yes -> no under both readings |
| s03 | V1.8 | D2.6 | independent of | X:Dec | computed | 0 moves (§3) |

### Section 2

| id | variant | from | kind | to [mark] | standing | what shows it (cut) |
|---|---|---|---|---|---|---|
| e2.00 | V2.1 | D6.4 | moves | X:Dependence, X:(E), X:Expl | computed | Dep F→T on 57 / 74 / 8 generated candidates (single / value maps / MID proper), none T→F; the reply's case ¬Acc → Acc — note: the reply's gloss 'commitments that do no work (L313) become … |
| e2.01 | V2.1 | D6.4 | changes with | D7.2 [FROZEN], L289.s1 [FROZEN] | computed | ∅ ∈ S for 63 generated candidates under V2.1, 0 off; L299.s1 realized by 20 off and 20 under V2.1; L307's S by 17 and 17; L309's finite realization S = {{a}} under both |
| e2.02 | V2.1 | D6.4 | constrains | L275.n1 [S2] | computed | FC29 unchanged under V2.1 (§6): a contrast no admitted edit realizes sits at no pair of C, and V2.1 still asks a pair of C |
| e2.22 | V2.1 | D6.4 | independent of | L309.s1 [FROZEN] | computed | built (Γ = {a,b}, a: y = x, b: y = 0): S = {{a}}, full candidate (E) F under off and V2.1 (F1, F2, A fail); the reply left it unsettled |
| e2.23 | V2.1 | D6.4 | changes with | D7.3 [FROZEN], L293.s1 [FROZEN], L293.s2 [S2] | computed | off: every route has a critical block (0 of 1,322 without; argument §5: the Lost witness is critical); V2.1: 120 of 1,450 routes have none (63 of them ∅) |
| e2.24 | V2.1 | D6.4 | changes with | L313.s2 [S2] | computed | V2.1 admits more than L313's case: 8 of 57 new accounts have a commitment that does work for (F1)/(F2) while none carries the contrast (smallest: Γ = {k0} on p0, the answer on p1 set by … |
| e2.34 | V2.1/V2.2/V2.3/V2.4 | D6.4, D6.7 | independent of | D8.2 [S2], D8.3 [S2], D10.2 [FROZEN] | computed | 0 of 3,835 pairs change conflict pairs, rivals or kind under each of V2.1–V2.4 |
| e2.39 | V2.1 | D6.4 | independent of | – (no claim of the suite separates D6.4 from V2.1: a gap) | computed | no claim's result moves under V2.1 (§6); no worked case moves (§2); only the generated worlds (57 / 74 / 8) separate it — note: a gap for the map: every worked case with a contrast has a … |
| e2.03 | V2.2 | D6.4 | blocks | L311.s2 [FROZEN] | claimed only | argument: finite part computed: under V2.2 every route has a critical singleton (0 of 1,297 routes … · settle: a computation of S over an infinite Γ (the program enumerates a finite … |
| e2.04a | V2.2 | D6.4 | constrains | L299.s1 [FROZEN] | computed | 'constrains' computed: realizations 20 → 1 |
| e2.04b | V2.2 | D6.4 | moves | X:(E) | contradicted | claimed: every candidate realizing L299.s1 fails (E) under V2.2; contradicted as worded: one generated candidate meets (E) with a block critical and no singleton of it critical (the … |
| e2.05 | V2.2 | D6.4 | changes with | D10.4 [FROZEN], D10.6 [S2] | contradicted | V2.2 moves no pair's conflict pairs, rivals or kind (0 of 3,835); Prob_j (D10.1) reads Riv and NotOut, not the value of Acc; so no problem is added or removed |
| e2.25 | V2.2 | D6.4 | blocks | L307.s1 [FROZEN] | computed | no candidate realizes that S under V2.2 (17 → 0; all 17 become {{a},{b}}); argument: every route has a critical singleton, and in {a,b} neither is |
| e2.26 | V2.2 | D6.4 | blocks | L313.n3 [S2] | claimed only (the computing agent) | argument: by the argument of R4: L311's candidate has S = ∅ under V2.2, so its example goes · settle: as R4 |
| e2.27 | V2.2 | D6.4 | changes with | D7.3 [FROZEN] | computed | 0 of 1,297 routes under V2.2 without a critical singleton (21 of 1,322 off) |
| e2.38 | V2.2 | D6.4 | independent of | – (no claim of the suite (FC21–FC40) separates D6.4 from V2.2: a gap) | computed | no claim's result moves under V2.2 (§6); only the generated worlds (23 / 20 / 4) and the built L307 candidate separate V2.2 from D6.4 as it stands — note: a gap for the map: the text's … |
| s04 | V2.2 | D6.4 | moves | X:Dependence, X:(E), X:Expl | computed | T → F on 23 / 20 / 4 generated, none F → T; the built L307 case T → F; Account ∧ ¬Dec(t): the same movers |
| e2.06a | V2.3 | D6.4 | blocks | L329.s3 [FROZEN] | contradicted | identification reads no (E); FC57, FC58, FC28's Ident unchanged |
| e2.06b | V2.3 | D6.4 | moves | X:(E) | computed | no account on a {1}×B contract: 168 → 0 of 1,953 |
| e2.06c | V2.3 | D6.4 | blocks | L331.s2 [S2], E2 [S2] | claimed only | argument: settle: the two balances built as a question on {1}×B with a candidate · settle: for L331.s2: the two balances built as a question on {1}×B with a candidate (the program … |
| e2.07 | V2.3 | D6.4 | changes with | D3.3 [S1] | claimed only | argument: V2.3 leaves Ident(p) as it was (D3.3 reads no Dependence; FC28's Ident part under V2.3, … · settle: section 1's computation of V1.4 (Ident with a ≠ 1) read together with V2.3 … |
| e2.08 | V2.3 | D6.4 | constrains | L253.s1 [FROZEN] | computed | the switch reads only the pair's edit in NC2's pair loop; no query changes in any run |
| e2.28 | V2.3 | D6.4 | moves | X:Dependence, X:(E), X:Expl | computed | 253 generated accounts T→F, of which 168 on contracts {1}×B′; the other 85 on contracts that hold an edit but carry their contrast only at boundary pairs |
| e2.09 | V2.4 | D6.7 | blocks | – (not an item: the owner's decision S45 (with S44); goes to the candidate list) | claimed only | argument: not an item: the owner's decision S45 (with S44); goes to the candidate list · settle: the owner's yes or no in the later step (S52) |
| e2.10 | V2.4 | D6.7 | moves | X:(E), D9.10 [S3] | computed | (E): 11 worked cases, 972 / 776 / 301 generated accounts T→F; FC107 under V2.4: the identity candidate for p_δ (K1's criticism question) Acc T → F (its part 'base' a slot), so a criticism … |
| e2.11a | V2.4 | D6.7 | changes with | X:Expl, X:(Suff) | computed | Expl shrinks: 22 (case, history) T → F; 1,944 generated; ℰ_one in no defeat set of (Suff) (it fails (E)) |
| e2.11b | V2.4 | D6.7 | changes with | X:(Nec) | claimed only | argument: the (Nec) attack list is computed by no claim that moves |
| e2.29 | V2.4 | D6.7 | moves | E8 [FROZEN], E1 [S2], X:(E) | computed | all three T→F under V2.4 (§2); the reply named the myth's bearing, not these |
| e2.30 | V2.4 | D6.7 | changes with | D6.10 [FROZEN] | computed | 972 of 1,027 generated accounts fail (E) under V2.4 (E_enc 864, lookup 102, random 6), each by a slot: after S106 most generated accounts have a component that pins the answer |
| e2.36 | V2.4 | D6.7 | changes with | D6.3 [S2] | computed | FC23.new1 (h) under V2.4: counterexample: (E) (F,F,T,T) under (every, some, some-exempt, some-exempt-set) for one component, ⊥ at 1, 1 at e1; with NC1 back in (E), (E) depends on the … |
| s05 | V2.4 | D6.7 | moves | X:Expl | computed | 22 worked (case, history) T → F; 1,944 generated |
| e2.12 | V2.5 | D12.1 | constrains | L195.s1 [FROZEN] | computed | under V2.5 Sel accepts H = ∅: 'its pairs having occurred' vacuous, fidelity on ∅ is Hom(τ) (I18); FC77 part 3's 'other choice' is the variant's reading |
| e2.13 | V2.5 | D12.1 | changes with | L211.s3 [S2] | computed | FC30.new1 (e) under V2.5: the link nobody tried and nobody worked out is Sel, its fixed point {o1: Sel}, so its holding represents (D12.5); as an effect: the transport is no longer … |
| e2.14 | V2.5 | D12.1 | moves | X:Dec, X:Expl, X:(Suff) | computed | Account ∧ ¬Dec(t) F→T on the history 'nothing tried' for every account: 28 of 28 worked cases, 1,027 / 847 / 310 generated; no other history moves |
| e2.31 | V2.5 | D12.1 | changes with | D5.5 [FROZEN], X:(F2) | computed | Acc ⇒ (F2) ⇒ Hom(τ); with H = ∅ allowed, Hom(τ) ∧ Θ admits t ⇒ Sel(t;{t},id,∅); so on a holding with nothing tried Account ∧ ¬Dec(t) ⟺ Acc ∧ Θ admits t: ¬Dec(t) adds only Θ's admission … |
| e2.35 | V2.5/V2.6/V2.7 | D8.2, D8.5, D12.1 | independent of | X:(E) | computed | 0 Acc changes in every population and case |
| e2.37 | V2.5 | D12.1 | constrains | L195.n4 [S2], D12.1 [S2] | computed | FC30.new1 (d) under V2.5: the student's copy of a worked-out formula stays Dec under U, T, T′ with H = ∅ (the source's earlier representation excludes Sel); only (e), the link with no … |
| e2.15 | V2.6 | D8.2 | blocks | L315.s1 [FROZEN], L317.s6 [FROZEN] | computed | 310 of 310 kind-ii pairs lose every conflict pair, rivalry and kind; FC72.new2 (b): tilt and myth on the Greeks' C not rivals (§7) |
| e2.16a | V2.6 | D8.2 | independent of | X:(E) | computed | 0 Acc changes in every population |
| e2.16b | V2.6 | D8.2 | moves | D10.1 [FROZEN], D10.4 [FROZEN] | computed | no kind ii remains, so ETV_j holds of no candidate |
| e2.16c | V2.6 | D8.2 | moves | X:(Nec) | claimed only | argument: no claim computes an attack on (Nec) through easy to vary |
| e2.32 | V2.6 | D8.2 | changes with | D8.3 [S2] | computed | 492 kind-i pairs keep kind i and lose their conflict pairs outside C; rivals then need a conflict in C |
| s06 | V2.6 | D8.2 | independent of | X:Expl | computed | Account ∧ ¬Dec(t) unchanged |
| e2.17 | V2.7 | D8.5 | blocks | L315.s12 [S2] | computed | the reply's case: ConfCl T→F; 410 of 1,822 generated (candidate, pair) lose ConfCl, all by the second disjunct alone — note: where the candidate's answer is itself the motion χ excludes … |
| e2.18 | V2.7 | D8.5 | constrains | D8.4 [FROZEN] | computed | the switch touches only D8.5's second disjunct; Allow_χ and Applies are read as before in every run |
| e2.19 | V2.7 | D8.5 | changes with | D8.6 [FROZEN] | claimed only | argument: 'no longer feeds any ruling out of a single candidate': the program builds no argument … · settle: an encoding of L315.s13–s14's argument whose premise is a computed ConfCl |
| e2.33 | V2.7 | D8.5 | changes with | L317.n8 [S2], D10.6 [S2] | claimed only (the computing agent) | argument: 23 generated (candidate, pair) where the candidate meets (E) lose ConfCl (20 at a pair … · settle: an encoding of the argument from ConfCl (as R20); the program computes ConfCl, … |
| s07 | V2.7 | D8.5 | independent of | X:Expl | computed | Account ∧ ¬Dec(t) unchanged |
| e2.20 | V2.8 | D9.8 | constrains | D16.XV [S4] | claimed only | argument: V2.8 not implemented: out of scope as written (tabulation §6). The committed printout's … · settle: section 4's computation of V4.4 (the same reading) |
| e2.21 | V2.8 | D9.8 | moves | X:(Suff) | claimed only | argument: as R21 · settle: section 4's computation of V4.4 |

### Section 3

| id | variant | from | kind | to [mark] | standing | what shows it (cut) |
|---|---|---|---|---|---|---|
| e3.00 | V3.1 | D9.7 | constrains | L397.s5 [FROZEN] | computed | X_j(φ) := {α : Usable_j(α) ∧ RO(α, φ)} is still 'the set of arguments usable by j that rule out ψ' under V3.1 (the frozen words name no block); its extension grows: worlds.args 1,677 of … |
| e3.01 | V3.1 | D9.7 | changes with | L8.s3 [S1] | computed | L8.s3's clause is false of D9.7 under V3.1: ¬PM alone rules out PM (FC72 (e) as claimed → not as claimed; cases §C); p alone rules out ¬p for j who accepts p |
| e3.02a | V3.1 | D9.7 | moves | X:(Suff), X:(Nec) | computed | j accepting ¬Expl(ℰ) alone: an argument not using (E) rules out Expl(ℰ) F → T; the pole's forward candidate in Def(L536) F → T; (Nec)'s defeat by accepting Expl(ℰ) alone F → T |
| e3.02b | V3.1 | D9.7 | independent of | X:(E), X:Expl | computed | 0 moves on 27 worked, FC-E, CT, 61,900 generated |
| e3.03 | V3.1 | D9.7 | changes with | L397.n14 [S3], L397.s16 [S3] | computed | the two sentences varied with D9.7 (new form not given by the reply) are false of it under V3.1: 'p because p' (L397.s16) rules ¬p out for j who accepts p; a record made from ψ rules out … |
| e3.04 | V3.1 | D9.7 | changes with | D9.9 [S3], FC71 [claim] | computed | D9.9's clause 'no leaf of α with ¬(T∧B∧I) as a conjunct' and its record-leaf clause (L395) no longer block: FC71 (i), (ii) holds → counterexample (α⁺ ∈ X_j(T∧B∧I) with the block present); … |
| e3.05 | V3.1 | D9.7 | changes with | FC60 [claim], E3 [FROZEN] | computed | the record made from x = m* now rules out x ≠ m*: FC60 (b) as claimed → not as claimed (suite.V3.1) |
| e3.06 | V3.1 | D9.7 | changes with | FC72.new2 [claim] | computed | j2, who holds 'Slot ∧ ¬Acc(ℰ_myth1)' as one premise (the finding with the denial in it), rules the myth out under V3.1 (blocked under none): FC72.new2 (c) as claimed → not as claimed; the … |
| e3.07 | V3.1 | D9.7 | moves | D9.8 [S2], D10.1 [FROZEN] | computed | worlds.args: 1,677 new Out_j(φ), smallest: ¬q accepted rules out q; no usability moves (V3.1 reads RO only) |
| e3.08 | V3.2 | D9.4 | constrains | L389.s1 [FROZEN] | computed | under V3.2 Live_j(d; u) is still a predicate of (d; u), constant in u; (K2) as displayed is read unchanged; every suite run under V3.2 computes (K2) through it |
| e3.09a | V3.2 | D9.4 | moves | D9.8 [S2] | computed | fewer usable, fewer ruled out: 8,983 usabilities T → F, 26 Out_j T → F |
| e3.09b | V3.2 | D9.4 | moves | D10.1 [FROZEN] | computed | problems move: with fewer ruled out, problems grow (FC47.new1); the reply's direction ('fewer problems') contradicted |
| e3.10 | V3.2 | D9.4 | changes with | L393.n2 [S3] | computed | L393.n2 defines Live 'd = concl(u′) for some u′ ∈ Below(u) with Usable_j(u′) (D9.4), or a premise j tentatively accepts': false of D9.4 under V3.2 (FC70: a premise live twice over is no … |
| e3.11 | V3.2 | D9.4 | changes with | L369.s3 [S3], FC68 [claim] | computed | 'every such candidate alike is ruled out … from the candidate's own answer there': the two-step argument from (A) and each candidate's own answer is not usable: FC68 (b)–(c) as claimed → … |
| e3.12 | V3.2 | D9.4 | changes with | D9.9 [S3], FC71 [claim] | computed | K3's u⁺ from a failed prediction is a step above the step concluding ¬O; with Live through no step it is unusable unless j accepts ¬O itself (cases §C: T → F; with ¬O accepted T): FC71 … |
| e3.13 | V3.2 | D9.4 | changes with | D18.1 [S4], FC69 [claim] | computed | DEP's Live loses its staged (K2) edge: the loop S101 read closes trivially; FC69's alternative reading has one fixed point (0 usable steps) where it had two (0 and 2): FC69 (I40's … |
| e3.14 | V3.2 | D9.4 | changes with | FC47 [claim], FC53 [claim] | computed | each is a two-step argument whose intermediate conclusion j does not accept: usable T → F (suite.V3.2) |
| s08 | V3.2 | D9.4 | independent of | X:(E), X:Expl | computed | 0 moves (§3, §6.1) |
| e3.15 | V3.3 | D9.6 | constrains | L397.s5 [FROZEN] | computed | X_j(ψ) is still the set of arguments usable by j that rule out ψ, but for a premise alone 'usable by j' reads nothing of j: X_j0(design ∧ PM) = X_j(design ∧ PM) for j0 who accepts nothing … |
| e3.16 | V3.3 | D9.6 | changes with | L393.n2 [S3] | computed | FC72.new1 (a) as claimed → not as claimed: j0 never took ¬PM up and ¬PM alone is usable by j0 and rules out design ∧ PM |
| e3.17 | V3.3 | D9.6 | moves | X:(Suff), X:(Nec), D10.1 [FROZEN] | computed | FC72 (f): usable F → T, /X_j0/ 0 → 1; ψ = r ∧ (r → ¬Expl(ℰ)) alone, j0 accepts nothing: an argument not using (E) rules out Expl(ℰ) F → T (a bare ¬Expl(ℰ) stays blocked by D9.7); … |
| e3.18 | V3.3 | D9.6 | changes with | FC72.new1 [claim] | computed | 'for j0 (accepts nothing)': ruled out F → T; the conflict and the ruling out coincide with no chooser: FC72.new1 (c) as claimed → not as claimed (suite.V3.3) |
| s09 | V3.3 | D9.6 | independent of | X:(E), X:Expl | computed | 0 moves (§3, §6.1) |
| e3.19 | V3.4 | D13.3 | blocks | L403.s3 [FROZEN] | computed | FC90.new1 (a) as claimed → not as claimed (both CT readings): Build for the reversed calculation used in error T → F; worked cases: Build T → F exactly on the 5 with Acc F; worlds.cands: … |
| e3.20a | V3.4 | D13.3 | moves | X:Dec, D12.2 [S2], X:Expl | contradicted | D12.2 as written: CT reads Prepares, not ExplUse; 0 Dec moves |
| e3.20b | V3.4 | D13.3 | moves | X:Dec, D12.2 [S2], X:Expl | computed; cond.: under S108-3-I2 (CT asks ExplUse) | the reply's case T → F; generated 122 / 93 / 36 / 200 out (widest-contract claim) |
| e3.21 | V3.4 | D13.3 | constrains | L526.s11 [S4] | computed | DEP unchanged by V3.4 (ExplUse → UsesClaim, (E), Cand); FC32.new1 (d) (L526's dependences as paths) unmoved; under V3.4 Build depends on (E)'s value, not only on the claim's content … |
| e3.22 | V3.4 | D13.3 | moves | D13.6 [FROZEN], D14.7 [S3] | computed | Build is a conjunct of (G) (D13.6) and (G) of (EX): Build F wherever the claim used fails (E); (EX)'s own Account conjunct (L449) then repeats what Origin already asks where the claim used … |
| e3.23 | V3.4 | D13.3 | moves | D12.1 [S2], X:Dec | computed; cond.: under S108-3-I2 | worlds.chains, T′: 92 chains with Dec T → F at a held output: an earlier trace whose output uses a claim failing (E) no longer constructs, its occurrence is no longer represented, and … |
| s10 | V3.4 | D13.3 | independent of | X:(E) | computed | Acc 0 moves (§3, §6.1) |
| e3.24 | V3.5 | D13.8 | changes with | L55.n3 [S1] | computed | under V3.5 FC84.new1 (c)'s chain with an unrecorded change C → C′ is an episode (S41 reading F → T); FC84.new1 (a4)'s iv-u chain: Episode F → T (cases §C); L55.n3's words no longer … |
| e3.25a | V3.5 | D13.8 | moves | X:Dec, D12.2 [S2], X:Expl | contradicted; cond.: where the trace lies at o_t (the program's Prepares, a label at one occurrence, I56) | D12.2's cut T′ (and T): no candidate meeting (E) moves; the record clause idle where t is held and the trace lies at o_t ({o_t} alone is an episode) |
| e3.25b | V3.5 | D13.8 | moves | X:Dec, D12.2 [S2], X:Expl | computed; cond.: in the tag encoding, and under the rejected cuts K, U | tag: 22 of 27 worked in, 1,013 / 881 / 232 / 1,670 generated; K: 5,118 chains |
| e3.25c | V3.5 | D13.8 | moves | X:Dec, D12.2 [S2], X:Expl | computed; cond.: where the output's construction trace spans an unrecorded change of contract (Prepares(h′, o_t, ·) asks h′ to hold the trace's occurrences, D13.3's tuple, L405); the second checker's run, not section 3's | D12.2's cut T′ (and T): every held output whose trace spans an unrecorded change of contract has Dec T → F under V3.5 (chains n ≤ 4: 45,072 of the 90,144 held-output chains whose output … |
| e3.26 | V3.5 | D13.8 | changes with | D12.2 [S2] | computed | what keeps D13.8's record clause from ¬Dec(t) for a candidate meeting (E) is D12.2's o′ ⪯ o_t with Held at o_t (the chain model, T′): with o′ ≺ o_t only (K) the clause reaches 5,118 held … |
| e3.27 | V3.5 | D13.8 | changes with | FC84.new1 [claim], FC84.new2 [claim] | computed | suite.V3.5: FC84.new1 (c) as claimed → not as claimed (the unrecorded change C → C′ is an episode under both readings; Con at o2 [T] both under the S41 reading, [F] → [T] under L55's); … |
| s11 | V3.5 | D13.8 | independent of | X:(E) | computed | Acc 0 moves |
| e3.29 | V3.6 | D15.8 | constrains | D12.1 [S2] | computed | under V3.6 D12.1 reads t ∈ 𝒯 through s108s3.in_population (Θ's admission alone); Sel computed on every history of §3, §6.1 |
| e3.30a | V3.6 | D15.8 | moves | D12.1 [S2], X:Dec, X:Expl | computed; cond.: on S108-3-I4, history 'Sel-parts' (parts := E's components; stated construction := all but E's last component; s108_s3_cases.py l.11–12); with the stated construction t's own, t does not move, only t′ = t + a part; the counts equal the population meeting (E), by construction of the history | worked cases 'Sel-parts': Account ∧ ¬Dec(t) F → T on the 22 with Acc T; worlds.cands: 1,013 / 881 / 232 / 1,670 in ('Sel-parts'; t′ + an idle part the same); pairs newly underdetermined … |
| e3.30b | V3.6 | D15.8 | moves | FC80 [claim] | claimed only | argument: wider population: more Sel, fewer Dec, wider underdetermination · settle: for FC80 itself: a population with a stated construction built into FC80's generator |
| e3.31 | V3.6 | D15.8 | changes with | L481.s3 [S3] | computed | L481.s3's second clause ('a transport that would need a part every member of the population is built without is not in it') is false of D15.8 under V3.6: t′ with a part none of 𝒯 has is in … |
| e3.32 | V3.6 | D15.8 | independent of | FC30.new1 [claim] | computed | unmoved, as the reply says: Dec(t) at o2 T under V3.6 (the copy's defect is the absent trace and D12.3's inheritance, not the population) |
| s12 | V3.6 | D15.8 | independent of | X:(E) | computed | Acc 0 moves |
| e3.33 | V3.7 | D11.4 | blocks | L375.s2 [FROZEN] | computed | FC75 (a) (did no work) and (a′) (dependence only outside R) as claimed → not as claimed (suite.V3.7; (a″), (b) text only: the reason printed); worlds.routes: 1,436 of 5,724 routes active … |
| e3.34a | V3.7 | D11.4 | moves | D14.3 [FROZEN], D14.6 [FROZEN] | computed | ProducedBy F → T on 685 of 1,460 circuits; ProducesVia on 952 of 2,860 |
| e3.34b | V3.7 | D11.4 | moves | D9.11 [FROZEN] | claimed only | argument: idle routes become active; no part of (E) moves · settle: UsesReason computed over circuits with a represented objection and role maps (D9.11's m, … |
| e3.34c | V3.7 | D11.4 | independent of | X:(E) | computed | Acc 0 moves anywhere |
| s13 | V3.7 | D11.4 | independent of | X:Expl | computed | Account ∧ ¬Dec(t) 0 moves |
| e3.36 | V3.8 | D14.7 | constrains | L443.n1 [S3] | computed | Deploy is kept in s108s3.create_ex's rest; CreateEx under V3.8 never holds with Deploy F (worlds.createx) |
| e3.37a | V3.8 | D14.7 | changes with | D18.1 [S4] | computed | (EX) no longer reaches Crit (FC32.new1 (f)) |
| e3.37b | V3.8 | D14.7 | changes with | L628.n2 [S4] | claimed only | argument: FC90: CCE 'left unstated by L628', so no sentence change is forced; DEP's (EX) node … · settle: whether the owner wants (EX) to keep its critical episode (S47 with S41 Q6): the … |
| e3.38a | V3.8 | D14.7 | moves | D14.7 [S3] | computed | CreateEx F → T on 7,086 of 1,929,216 valuations; T → F 0 |
| e3.38b | V3.8 | D14.7 | independent of | X:(E), X:Expl, X:(Suff), X:(Nec) | computed | Acc, Dec, Account ∧ ¬Dec(t) and the defeat sets: 0 moves |
| e3.39 | V3.8 | D14.7 | changes with | L528.s2 [FROZEN], L528.s3 [FROZEN] | computed | under 'none' every instance of (EX) has a critical episode connected to (G), so the explanation-creation class (L528.s3) lies inside the creative-episode class (L528.s2); under V3.8 not: … |

### Section 4

| id | variant | from | kind | to [mark] | standing | what shows it (cut) |
|---|---|---|---|---|---|---|
| e4.00 | V4.1 | D16.XV | moves | X:Expl, X:(Suff), D18.1 [S4] | computed | graph recomputed: DefeatConds (D16.XV) gains Slot and through it ℓ, Cand, Transport; Expl stays an atom (a sink); Slot is reached by DefeatConds only; (E)'s ancestors unchanged. Being an … |
| e4.01 | V4.1 | D16.XV | changes with | L17.n2 [S1], L49.n3 [S1], L61.n2 [S1], L69.n3 [S1] | computed | the formula they write parts from V4.1's being an explanation on 10 worked cases (ℰ_one, E_enc C1 and C2, E_rev τ′ on C_H, 'p because p', M1–M3, the hand-turned vane, E8's identity … |
| e4.02 | V4.1 | D16.XV | changes with | L269.n1 [S2], L269.s2 [S2], L269.s3 [S2], L271.s1 [S2], L271.s2 [S2], L273.n1 [S2], L275.n1 [S2], L275.s2 [S2], … | contradicted | L269–L277 speak of (E), which V4.1 does not move (E_enc still meets (E): Acc unchanged on every case); the quoted row is the brief's summary of S44, S45 (brief line 90), not a line of the … |
| e4.03 | V4.1 | D16.XV | changes with | FC30.new1 [claim] | computed | (Suff) kept (as written): FC30.new1 (c) holds → fails by construction at (Acc T, Dec F, Slot T); (Suff) co-varied: (c) holds, (b)'s second identity (Def(L17 as text 104) = Def(L536) ∪ … |
| e4.04 | V4.1 | D16.XV | changes with | FC23.new2 [claim] | computed | (Suff) kept: no result moves ((f) checks the owner's condition, which V4.1 keeps); (Suff) co-varied: (f) moves (ℰ_one constructed leaves (Suff)'s defeat set) (§7) |
| e4.05 | V4.1 | D16.XV | changes with | FC23.new3 [claim], FC25.new2 [claim] | contradicted | no result of either moves under V4.1 (suite, both sub-choices): they compute the Pin, Slot and Acc facts V4.1 reads, which V4.1 does not change |
| e4.07 | V4.1 | D16.XV | changes with | D6.3 [S2] | computed | under V4.1 ℓ becomes an ancestor of D16.XV's defeat conditions (graph); after S106 ℓ was an ancestor of no conjunct of (E) and of no defeat condition |
| e4.08 | V4.1 | D16.XV | changes with | D6.3 [S2] | computed | the owner's two-part sign stays an explanation under V4.1 only with 'every' (T, F, F, F under every / some / some-exempt / some-exempt-set); under 'some' the pole's forward candidate on C2 … |
| e4.09 | V4.1 | D16.XV | constrains | X:(Suff), L61.n2 [S1], L536.s1 [S4] | computed | with (Suff)'s antecedent kept, V4.1 makes (Suff) as conjectured fail by definition of every constructed or selected candidate with a slot (FC30.new1 (c) fails by construction; ℰ_one: … |
| e4.10 | V4.1 | D16.XV | moves | E1 [S2], D6.3 [S2] | computed | the reply's trace has it stop being an explanation: under 'every' it has no slot (pins only at the settings of L) and stays (T → T); it stops only under 'some' (a correction of the reply's … |
| e4.11 | V4.1 | D16.XV | constrains | D18.2 [S4] | computed | the reply's (d) says V4.1 is safe: FC100's generator and bijections at scale 4 (12,960 port-query models, seed 108404): Slot under all four readings, the pins and Acc are kept by every … |
| s14 | V4.1 | D16.XV | independent of | X:(E), X:Dec | computed | Acc and Account ∧ ¬Dec(t): 0 moves (worked, scripts, 17,280 generated, suite) |
| e4.12 | V4.2 | D16.XV | moves | X:Expl | computed | F → T on 24 of 29 worked cases under a declared or unrecorded history (every Acc-T case), the student's copy (FC30.new1 (d)), a link no pair tried (FC30.new1 (e)), CT8's R2 and R4, FC-E 7, … |
| e4.13 | V4.2 | D16.XV | changes with | L17.n2 [S1], L49.n3 [S1], L61.n2 [S1], L69.n3 [S1], X:(Suff), FC30.new1 [claim] | computed | (b) breaks under the reply's trace reading (S108-4-I2 'L17': Def(L17) T, Def(L536) F for the declared copy; with (a), (c), (d), (e) of FC30.new1 and FC23.new2 (f)); as written ('rule') (b) … |
| e4.14 | V4.2 | D16.XV | constrains | FC30 [claim] | computed | FC30 unchanged in the suite under V4.2 (every sub-choice); Acc unchanged on every case, script and generated candidate |
| e4.15 | V4.2 | D16.XV | blocks | FC30.new1 [claim], FC23.new2 [claim] | computed | FC30.new1 (c) fails by construction at (Acc T, Dec T); FC23.new2 (f) not as claimed (ℰ_two, ℰ_one declared are explanations) |
| e4.16 | V4.2 | D16.XV | moves | CT8 | computed | the chosen pair's transport is declared under R2, R4 (T′): not an explanation now, an explanation under V4.2 only |
| s15 | V4.2 | D16.XV | independent of | X:(E), X:Dec | computed | Acc and Dec: 0 moves |
| e4.17 | V4.3 | D16.XV | constrains | D12.3 [S2], D12.4 [FROZEN] | computed | a holding with no record is Dec (D12.3: no parameters give Sel, none give Con; H0: Dec on 29 of 29); at every holding not reached by a transfer ¬Dec(t) ⇔ Sel ∨ Con ⇒ Sel ∨ CT (chains: 0 … |
| e4.18 | V4.3 | D16.XV | moves | X:Expl, X:(Suff) | computed | only relayed or recorded copies move, T → F: (a) of constructed and selected holdings (worked cases 24 + 24; chains 2,692 holdings; generated 1,019 + 1,019), (b) of selected holdings only … |
| e4.19a | V4.3 | D16.XV | changes with | L17.n2 [S1], L49.n3 [S1], L61.n2 [S1], L69.n3 [S1] | computed | the four sentences write being an explanation, which V4.3 moves at relayed and recorded holdings (e4.18: 24 + 24 worked, 2,692 chain holdings) |
| e4.19b | V4.3 | D16.XV | changes with | FC25.new2 [claim] | contradicted | the reply's reason, 'the encoding table stops being an explanation' (E_enc with no record): E_enc with no record is Dec now and under V4.3 (no explanation either way); with Con or Sel it … |
| e4.20 | V4.3 | D16.XV | changes with | D12.4 [FROZEN] | computed | under V4.3 (a) an inherited Con or Sel no longer makes a transferred holding an explanation: FC30.new1 (f)'s K3 reading (the student's component transferred, Con inherited) T → F; E9's t1 … |
| e4.21 | V4.3 | D16.XV | changes with | D12.2 [S2] | computed | (a) the holding itself: relays of constructed holdings move; (b) the holding or one it was transferred from: they do not; (c) through inherited provenance: V4.3 is now's reading (0 moves) |
| e4.22 | V4.3 | D16.XV | constrains | D18.2 [S4] | claimed only (the computing agent) | argument: the reply's (d): 'V4.3 is not obviously φ-invariant'; in the program's chains Sel, CT … |
| s16 | V4.3 | D16.XV | independent of | X:(E), X:Dec | computed | Acc and Dec: 0 moves |
| e4.23 | V4.4 | D16.XV | constrains | D9.6 [S3], D9.7 [S3], D9.8 [S2] | computed | the defeat set grows only through X_j: for a j that takes Acc(ℰ′) and Acc(ℰ′) → ¬Expl(ℰ) as given (usable by modus ponens); the record argument (r, r → ¬Expl) is in it under both readings |
| e4.24a | V4.4 | D16.XV | moves | X:(Suff), X:(Nec) | computed | (Suff): FC30.new1 (h)'s ℰ_fwd and E9's t1∘ψ enter (instance T, symbol F), declared ones do not; generated 1,019 (Con), 1,019 (Sel); (Nec): 3,979 exposed now |
| e4.24b | V4.4 | D16.XV | independent of | X:(E), X:Expl | computed | Acc and being an explanation: 0 moves; suite: 0 claims move |
| e4.26 | V4.4 | D16.XV | changes with | X:(Nec) | computed | for E_rev on the full pole's C1 both are needed: the rival-citing argument counts only at the instance (V4.4) and E_rev is exposed only on C alone (V4.5); on FC30.new1's pole (θ at 45) it … |
| e4.27 | V4.5 | D16.XV | constrains | L606.s4 [S4], FC99 [claim] | computed | FC99 unchanged (suite); now's exposure fails for 28 of 29 worked cases, each having a transport faithful at a single baseline pair (C′ = {(1,b)}; for 24 their own t is faithful on C), and … |
| e4.28 | V4.5 | D16.XV | changes with | L538.s1 [S4], FC30.new1 [claim], E5 [FROZEN] | contradicted | E5's two encodings meet (E), so their own t is faithful on C: exposed under neither shape (contradicted for E5); FC30.new1 (g) unchanged (t faithful); the widening is real elsewhere: E_rev … |
| e4.29 | V4.5 | D16.XV | independent of | L538.s2 [S4] | computed | neither of E5's encodings [FROZEN] is exposed under now's shape or V4.5's; the one worked case exposed now is L257's contract of relabelings (no injective θ_k exists: exact in D5.1's class) |
| e4.30 | V4.5 | D16.XV | moves | X:(Nec) | computed | exposed now: 1 of 29 (the relabelings); under V4.5: 5 (+ E_rev τ and τ′ on C1, E_tab C1 and C2); no candidate meeting (E) is exposed under either |
| s17 | V4.5 | D16.XV | independent of | X:(E), X:Expl | computed | 0 moves |
| e4.31 | V4.6 | D16.4 | constrains | D5.3 [FROZEN] | computed | (E) reads δ through (A) and Dependence: the pole on C1 meets (E) with δ = L only; FC90.new1 (c) unchanged |
| e4.32a | V4.6 | D16.4 | moves | D16.4 [S4] | computed | 1 of 17,280 (SMALL) and 2 of 25,920 (MID) searched witnesses meet (E) only with a non-designated δ; membership over every (p, t, Γ) not computed |
| e4.32b | V4.6 | D16.4 | independent of | X:(E) | computed | (E) unchanged |
| e4.33 | V4.6 | D16.4 | changes with | E1 [S2] | computed | the forward candidate meets (E) with δ_E = L and with δ_E = H: the designation clause separates witnesses there, not contents |
| s18 | V4.6 | D16.4 | independent of | X:Expl | computed | 0 moves |
| e4.34 | V4.7 | D16.3 | blocks | L495.s1 [FROZEN] | computed; cond.: on the toy only (S108-4-I7); the program computes no barrier, Enable or UU | on the toy (S108-4-I7, the only reading computable): with the barrier read as L495.s1's words have it, 'barrier ∧ UU' holds on 0 of 484 assignments now and on 217 under V4.7: the frozen … |
| e4.35 | V4.7 | D16.3 | moves | D16.4 [S4] | computed | graph: Enable is reached by UU, UC, UECS and Classes only, now and under V4.7; (E), Dec, DefeatConds do not reach it; toy: UU moves F → T on 217 of 484; all 24 script runs and the suite: … |
| e4.36 | V4.7 | D16.3 | changes with | D12.1 [S2], D12.2 [S2], D12.5 [FROZEN], D15.8 [S3] | computed | graph: under V4.7 Enable loses (R) and β, and UU, UC, UECS no longer reach any provenance node: universality stops reading provenance |
| e4.37 | V4.7 | D16.3 | changes with | L528.s1 [FROZEN], L528.s2 [FROZEN], L528.s3 [FROZEN], L528.s4 [FROZEN], D16.5 [S4] | computed | graph: Classes (D16.5) reaches Enable through UECS; the class's words are unchanged and its extension grows with UU (toy: UU F → T on 217 of 484) |
| s19 | V4.7 | D16.3 | independent of | X:(E), X:Expl | computed | 0 moves |
| e4.38 | V4.8 | D12.9, D16.XV | constrains | D12.1 [S2], L574.s2 [FROZEN] | computed | FC80 (d), (d′) (L574's step) and FC80.new1 unchanged under V4.8 (suite); surv still reaches the defeat conditions through Sel (graph) |
| e4.39 | V4.8 | D12.9, D16.XV | moves | D16.XV [S4] | computed | built on the pole: (Prov)(i) F now, T under V4.8; generated: 0 of FC80's own 9,930 populations, 1,647 of 9,768 wide ones (a member altered at an unseen pair's image and at H's, or τ×σ not … |
| e4.40 | V4.8 | D12.9, D16.XV | changes with | L572.s2 [S4], L574.n4 [S4], L576.s1 [S4], L576.s4 [S4] | claimed only | argument: Argument 3's wording and consequence shift together |
| e4.41 | V4.8 | D12.9, D16.XV | changes with | FC80 [claim] | computed | FC80's underdetermination witness is read through D12.9 under V4.8 (every member); its status holds; its text moves (suite, §7) |
| e4.42 | V4.8 | D12.9, D16.XV | blocks | D16.XV [S4] | computed | satisfiable under V4.8 (the pole case; 1,647 generated models) |
| e4.43 | V4.8 | D12.9, D16.XV | changes with | FC80 [claim] | computed | on FC80's own populations V4.8 moves nothing: a differing member there differs at an unseen pair only, so it survives and now's conjunct already holds |
| s20 | V4.8 | D12.9, D16.XV | independent of | X:(E), X:Expl | computed | 0 moves |

### Rows with no edge (a search or a 'none found' finding)

| row | variant | finding |
|---|---|---|
| S3#28 | V3.6 | V3.6 blocks no FROZEN sentence: none states the parts bound (search of the template); L481.s3 [S3] is varied with it |
| S3#35 | V3.8 | V3.8 makes no FROZEN sentence about (EX) false (L443.s3 names O_ex only); but L528.s2–s3 [FROZEN] change with it (S3#39) |
| S4#6 | V4.1 | V4.1: in D18.1 the only node gaining an edge is DefeatConds (D16.XV, S4); no FROZEN definition reaches Slot |
| S4#25 | V4.4 | V4.4: no FROZEN sentence or definition holds 'not using' or Uses (search of the template; the three that hold it, L17.n2, L536.s1, L538.s1, are middle); the reply's 'nearest', L556.s3 [FROZEN], is about Argument 1's proof and is no edge. The reply's question (whether citing a rival's being an account is 'using (E)') is a reading, not a run |

## 5. Contradicted edges (the computation shows otherwise)

| id | variant | claimed | what the computation shows (cut) |
|---|---|---|---|
| e1.04 | V1.1 | changes with FC17, FC18 | recomputed under V1.1: FC17 and FC18 hold; only FC18's I94 look changes its witness |
| e1.20 | V1.2 | changes with FC27.new1 | FC27.new1 unchanged under V1.2 (every part, status and text) |
| e2.04b | V2.2 | moves X:(E) | claimed: every candidate realizing L299.s1 fails (E) under V2.2; contradicted as worded: one generated candidate meets (E) with a block critical and no singleton of it critical (the critical … |
| e2.05 | V2.2 | changes with D10.4, D10.6 | V2.2 moves no pair's conflict pairs, rivals or kind (0 of 3,835); Prob_j (D10.1) reads Riv and NotOut, not the value of Acc; so no problem is added or removed |
| e2.06a | V2.3 | blocks L329.s3 | identification reads no (E); FC57, FC58, FC28's Ident unchanged |
| e3.20a | V3.4 | moves X:Dec, D12.2, X:Expl | D12.2 as written: CT reads Prepares, not ExplUse; 0 Dec moves |
| e3.25a | V3.5 | moves X:Dec, D12.2, X:Expl | D12.2's cut T′ (and T): no candidate meeting (E) moves; the record clause idle where t is held and the trace lies at o_t ({o_t} alone is an episode) |
| e4.02 | V4.1 | changes with L269.n1, L269.s2, L269.s3, L271.s1, L271.s2, L273.n1, L275.n1, L275.s2, … | L269–L277 speak of (E), which V4.1 does not move (E_enc still meets (E): Acc unchanged on every case); the quoted row is the brief's summary of S44, S45 (brief line 90), not a line of the text; what … |
| e4.05 | V4.1 | changes with FC23.new3, FC25.new2 | no result of either moves under V4.1 (suite, both sub-choices): they compute the Pin, Slot and Acc facts V4.1 reads, which V4.1 does not change |
| e4.19b | V4.3 | changes with FC25.new2 | the reply's reason, 'the encoding table stops being an explanation' (E_enc with no record): E_enc with no record is Dec now and under V4.3 (no explanation either way); with Con or Sel it is one … |
| e4.28 | V4.5 | changes with L538.s1, FC30.new1, E5 | E5's two encodings meet (E), so their own t is faithful on C: exposed under neither shape (contradicted for E5); FC30.new1 (g) unchanged (t faithful); the widening is real elsewhere: E_rev under τ … |

## 6. Gaps (rule 6: listed; rule 10: they decide a second round)

### 6.1 Items no variant touched

| stretch | FROZEN: computed / claimed only / untouched | middle: computed / claimed only / untouched |
|---|---|---|
| S1 | 7 / 7 / 43 | 18 / 4 / 132 |
| S2 | 28 / 5 / 62 | 39 / 6 / 108 |
| S3 | 9 / 1 / 39 | 17 / 0 / 120 |
| S4 | 7 / 0 / 30 | 17 / 3 / 113 |

Middle definitions neither varied nor named by any edge (17). **Upstream of the explanation definition** (7; by D18.1's graph, where Expl, (Suff) and (Nec) share D16.XV's node, or by the part's own statement, §1):

| definition | upstream of |
|---|---|
| D6.9 (Relabeling) | (E) (D18.1); Expl (D18.1); (Suff) (D18.1); (Nec) (D18.1) |
| D11.2 (Content) | Dec (D18.1); Expl (D18.1); (Suff) (D18.1); (Nec) (D18.1) |
| D11.3 (History) | Dec (D18.1); Expl (D18.1); (Suff) (D18.1); (Nec) (D18.1) |
| D6.8 (The four conditions) | Expl (D18.1); (Suff) (D18.1); (Nec) (D18.1) |
| D9.1 (Claims) | Expl (D18.1); (Suff) (D18.1); (Nec) (D18.1) |
| D9.2 (Argument) | Expl (D18.1); (Suff) (D18.1); (Nec) (D18.1) |
| D5.7 (Faithful; question fidelity) | Dec (statement); Expl (statement); (Suff) (statement); (Nec) (statement) |

Upstream of no part by either route (10): D8.new1, D10.3, D12.7, D12.8, D13.7, D14.1, D15.1, D15.2, D15.5, E9. FROZEN definitions no edge names (38): D0.1, D1.1, D1.2, D1.3, D2.3, D3.2, D3.7, D4.1, D4.2, D4.3, D4.5, D5.1, D5.6, D7.1, D7.5, D7.6, D8.1, D9.3, D9.5, D10.5, D11.1, D11.5, D12.6, D13.1, D13.2, D14.2, D14.4, D14.5, D14.8, D15.3, D15.4, D15.6, D15.7, D16.1, D16.2, E4, E6, E7. Every section had its eight variants; no section is untouched as a whole.

### 6.2 Edges the computation could not settle (claimed only)

31 edges: e1.02, e1.03, e1.14, e1.36, e1.37, e1.38, e1.39, e1.40, e1.45, e1.46, e1.47, e1.48, e1.49, e1.50, e1.51, e2.03, e2.06c, e2.07, e2.09, e2.11b, e2.16c, e2.19, e2.20, e2.21, e2.26, e2.33, e3.30b, e3.34b, e3.37b, e4.22, e4.40. Each with its argument and what would settle it in §4; 9 of them are of the three variants not run (V1.6, V1.7, V2.8), which the orchestrator has now ruled on (its decision 3): V1.6's formula, without its added sentence, to round 2 for section 2; V1.7, and V2.8's part on L315.s7 [FROZEN], to Part B; V2.8's D16.XV part is V4.4's reading, computed (e2.20, e2.21 stand as V2.8's; section 4's V4.4 rows compute the reading).

### 6.3 Results that rest on one reading, and what the program cannot compute

| rests on | what |
|---|---|
| S108-1-I5 | V1.5's whole effect (a question with no recorded contract history is declared); other choice: V1.5 computes nothing |
| S108-1-I1 | whether ℰ_bv becomes an account under V1.1 (reading (i) yes, (ii) no) |
| edit or boundary for the owner's changes | whether V2.3 drops the owner's weathervane and two-part sign: read as edits (M13, claims_s106) nothing moves; read as boundaries (FC28.new2's D_vane; the sign with B = {mon, tue}) both drop, with E_enc on their questions (the second checker's run, O1). V1.1 drops both either way; V2.4 and V4.1 keep the two-part sign either way under 'every' |
| D6.3's quantifier (I136) | whether V2.4 and V4.1 drop the owner's two-part sign: kept under 'every' (the program's reading), dropped under 'some', 'some-exempt', 'some-exempt-set' (FC23.new2 (a); computed both encodings by the second checker) |
| S108-3-I2 | whether V3.4 reaches Dec at all (CT asks Build's ExplUse) |
| the trace's extent (O3) | V3.5 under D12.2's cut T′ (and T): the trace at o_t (the program's Prepares, I56) moves no candidate meeting (E); a trace spanning an unrecorded change of contract moves every such held output (the second checker's run, e3.25c) |
| tag encoding / cut K | V3.5's moves in section 3's own runs |
| S108-3-I4 | V3.6's reach, on the history 'Sel-parts' (parts := E's components; stated construction := all but E's last component); with the stated construction t's own, t does not move and only t′ = t + an extra part does |
| S108-4-I3 | V4.3's reach (Sel ∨ CT read at the holding; through inherited provenance it moves nothing) |
| S108-4-I7 | V4.7 computed on a toy only |
| I90 (Θ by hand) | Dec(t) on every worked case and generated candidate: histories set by hand. Where a history is built so that the variant bites on every account (V2.5's 'nothing tried', V3.5's tag history, V3.6's 'Sel-parts', V4.2's declared and V4.3's relayed histories), the counts equal the population meeting (E), by construction of the history |

Not computable in the program as it stands: an infinite Γ (V2.2, L311); UsesReason over circuits (V3.7, D9.11); 𝔈_Θ membership over every (p, t, Γ) (V4.6); (CT1), Can, Enable, UU, barriers (V4.7); an argument whose premise is a computed ConfCl (V2.7, D8.6, D10.6); an attack on (Nec) through easy to vary (V2.4, V2.6); Desc, BadTarget, BadReq (V1.6); a recorded contract history ρ_p (V1.5). Suite blind spots: no claim separates D6.4 from V2.1 (e2.39); no claim separates D6.4 from V2.2 (e2.38).

Not computed (2nd checker, O12): the bridge (FC84.new1), E2, E3, E4 and E7 carry no candidate and no (E): no variant's effect on them as explanations is computed (sections 1, 2, 4); the four whole-suite runs were made by the computing agents' own scripts, not by Sonnet workers agreeing by script as the rule assigns (sections 2, 3); the critical review's eight reruns agree.

**A finding about the state after round 4** (O4; the orchestrator's decision 2): L538.s2 [S4] ('Eliminative explanation (Part VII) is the exposed case') is not met by E5's encodings under (Nec)'s current shape: no candidate meeting (E) is exposed (Acc ⇒ F1 ∧ F2 = Faithful_C(t), so C′ = C and t′ = t witness it), and FC62 has E5 meet (E) (section 4, E4.5c). For the orchestrator's records and the paused review rounds, not for change in Part A.

### 6.4 The untouched items, by id (each node in the `.json`)

- **S1 definition FROZEN** (11): D0.1, D1.1, D1.2, D1.3, D2.3, D3.2, D3.7, D4.1, D4.2, D4.3, D4.5
- **S1 sentence middle** (132): L8.n1, L8.s2, L8.s4, L8.s5, L8.n6, L8.s7, L8.n8, L8.n9, L11.s1, L11.s2, L11.s3, L11.s4, L13.s1, L13.s2, L13.s3, L13.s4, L13.s5, L13.s6, L13.s7, L15.s1, L15.s2, L15.s3, L17.s1, L17.s3, L17.s4, L21.s1, L21.s2, L21.s3, L21.s4, L23.s1, L23.s2, L23.s3, L25.s1, L25.s2, L25.s3, L27.s1, L31.s1, L31.s2, L31.s3, L31.s4, L35.s1, L37.s1, L37.s2, L37.s3, L37.s4, L39.s1, L39.s2, L39.s3, L39.s4, L39.s5, L41.s1, L41.s2, L41.s3, L43.s1, L43.s2, L43.s3, L43.s5, L45.s1, L45.s2, L45.s3, L45.s4, L45.s5, L47.s1, L47.s3, L49.s1, L49.s2, L49.s4, L49.s5, L51.s2, L51.s3, L53.s1, L53.s2, L53.s3, L55.s1, L55.s2, L55.s4, L57.s2, L57.s3, L61.s1, L61.s3, L67.s2, L69.s1, L69.s2, L71.s1, L71.s2, L71.s3, L73.s1, L75.s1, L75.s2, L75.s3, L75.s4, L75.s5, L75.s6, L75.s7, L77.s1, L77.s2, L77.s3, L85.s1, L97.s1, L105.s1, L109.n4, L119.s1, L119.s2, L119.s3, L119.n4, L119.n5, L119.s6, L119.s7, L121.s1, L127.n1, L127.n4, L127.s5, L135.s1, L141.s1, L141.n3, L141.s4, L151.n3, L151.s4, L151.s5, L151.n6, L151.s7, L155.s1, L155.s3, L155.s4, L159.s2, L159.s3, L159.s4, L159.s5, L159.s6, L159.s7, L161.s4, L161.s5
- **S1 sentence FROZEN** (32): L27.s2, L41.s4, L47.s2, L51.s1, L67.s1, L87.s1, L91.s1, L91.s2, L91.s3, L91.s4, L91.s5, L91.s6, L93.s1, L99.s1, L103.s1, L103.s3, L105.s2, L105.s3, L109.s1, L109.s2, L109.s3, L109.s5, L113.s1, L113.s2, L115.s1, L127.s2, L127.s3, L137.s1, L141.s2, L143.s1, L147.s1, L147.s2
- **S2 definition middle** (8): D5.7, D6.8, D6.9, D8.new1, D10.3, D11.2, D12.7, D12.8
- **S2 definition FROZEN** (12): D5.1, D5.6, D7.1, D7.5, D7.6, D8.1, D10.5, D11.1, D11.5, D12.6, E4, E6
- **S2 sentence middle** (100): L173.s1, L175.s1, L175.s2, L177.s2, L179.s1, L179.s2, L183.s1, L193.s1, L197.s1, L197.s2, L201.s1, L201.n4, L205.s1, L211.s1, L211.s2, L211.s4, L213.s1, L213.s2, L217.s1, L220.n1, L221.n1, L223.s1, L223.s2, L223.s3, L223.s4, L223.n5, L225.s2, L231.s1, L231.s2, L231.s3, L231.s4, L235.s1, L239.s1, L245.s4, L255.n1, L257.s1, L257.n2, L257.n3, L259.s1, L265.n1, L281.s1, L281.s2, L281.s5, L287.s2, L287.s3, L299.s2, L299.s3, L305.s1, L305.s2, L305.s3, L305.s4, L305.s5, L307.s2, L307.s3, L307.s4, L307.s5, L309.s2, L311.s1, L313.s1, L315.s3, L315.s9, L315.s13, L315.s14, L315.s15, L315.s16, L315.n18, L315.s19, L315.s20, L315.s21, L317.n4, L317.s5, L317.s7, L317.s9, L317.s10, L317.n11, L317.s13, L317.n14, L317.s16, L325.s1, L325.s2, L325.s5, L325.s7, L329.s1, L329.s2, L329.s4, L329.s5, L329.s6, L331.s1, L331.s3, L335.s3, L339.s1, L339.s2, L339.s3, L339.s4, L339.s5, L343.s4, L343.n5, L343.s6, L343.s7, L343.s9
- **S2 sentence FROZEN** (50): L169.s1, L169.s2, L169.s3, L177.s1, L185.s1, L189.s1, L189.s2, L195.s5, L199.s1, L199.s3, L201.s2, L201.s3, L207.s1, L217.s2, L219.s1, L225.s1, L225.s3, L225.s4, L241.s1, L245.s1, L245.s2, L245.s3, L247.s1, L249.s1, L265.s2, L281.s3, L281.s4, L287.s1, L295.s1, L301.s1, L315.s4, L315.s5, L315.s8, L315.s10, L315.s17, L317.s1, L317.s2, L317.s3, L317.s12, L317.s17, L325.s3, L325.s4, L335.s1, L335.s2, L343.s1, L343.s2, L343.s3, L343.s8, L347.s1, L347.s3
- **S3 definition middle** (8): D9.1, D9.2, D11.3, D13.7, D14.1, D15.1, D15.2, D15.5
- **S3 definition FROZEN** (13): D9.3, D9.5, D13.1, D13.2, D14.2, D14.4, D14.5, D14.8, D15.3, D15.4, D15.6, D15.7, E7
- **S3 sentence middle** (112): L353.s1, L353.s2, L353.s3, L353.s4, L355.s1, L357.s1, L361.s1, L363.s1, L363.s2, L363.s3, L363.s4, L365.s1, L365.s2, L367.s1, L367.s2, L369.s4, L369.s5, L369.s6, L375.n1, L375.s3, L377.s1, L377.s2, L377.s3, L379.s1, L383.s2, L385.s2, L387.s1, L393.n1, L393.s3, L393.n4, L395.n1, L397.s1, L397.n2, L397.s3, L397.n4, L397.s6, L397.n7, L397.n8, L397.s9, L397.s10, L397.n11, L397.s12, L397.s17, L397.n17, L397.s19, L397.s20, L403.s1, L403.s4, L405.n1, L405.s2, L405.s3, L405.s4, L405.s5, L407.s2, L407.s3, L407.s4, L407.s5, L409.s1, L409.s2, L409.s3, L409.s4, L409.s7, L411.s3, L413.s1, L413.s2, L413.s3, L419.s1, L421.s1, L425.s3, L427.s1, L427.s2, L427.s4, L429.s1, L429.s2, L429.s3, L429.n4, L435.s1, L435.s2, L441.n1, L441.s3, L441.s5, L441.s6, L453.n2, L453.s3, L453.s4, L453.s5, L455.s1, L455.s2, L455.s3, L455.s4, L455.s5, L461.s1, L461.s2, L461.s3, L461.s4, L461.s5, L461.s6, L463.s1, L471.n1, L471.n2, L473.s1, L473.s2, L473.s3, L473.s4, L475.s2, L475.s3, L477.s2, L479.s1, L479.s2, L479.s3, L481.s1, L481.s2
- **S3 sentence FROZEN** (26): L361.s2, L369.s1, L369.s2, L383.s1, L385.s1, L397.s13, L403.s2, L407.s1, L409.s5, L409.s6, L411.s1, L411.s2, L415.s1, L425.s1, L425.s2, L427.s3, L437.s1, L441.s2, L441.s4, L443.s3, L453.s1, L465.s1, L469.s1, L475.s1, L477.s1, L479.s4
- **S4 definition middle** (1): E9
- **S4 definition FROZEN** (2): D16.1, D16.2
- **S4 sentence middle** (112): L487.s2, L489.s1, L495.s2, L495.s3, L505.s1, L515.s1, L518.s1, L520.s1, L520.s2, L520.s6, L520.n7, L520.s8, L522.s1, L522.s2, L522.s3, L524.s1, L524.s2, L524.s3, L524.s4, L526.s1, L526.n4, L526.s5, L526.s7, L526.s8, L526.s12, L526.s13, L526.s15, L526.s16, L526.s17, L526.s18, L528.n5, L528.s6, L534.s1, L534.n2, L534.s3, L536.n2, L536.s3, L540.s1, L540.s2, L542.s1, L554.s1, L556.s1, L558.n1, L558.s2, L562.s1, L562.s3, L564.s1, L564.s2, L564.s3, L566.s1, L566.s2, L568.s1, L568.s2, L572.s1, L572.s3, L574.s1, L574.s3, L574.s5, L576.s2, L576.s3, L580.s1, L582.s1, L582.s2, L582.s3, L582.s4, L584.n1, L584.s2, L588.s1, L588.s2, L590.s1, L590.s2, L590.n3, L590.s4, L590.s5, L592.s1, L592.s2, L592.s3, L596.s1, L598.s2, L600.s1, L600.s2, L600.s3, L606.s1, L606.s2, L606.s3, L608.s1, L608.s2, L612.s1, L612.s2, L612.s3, L616.s2, L616.s4, L620.s1, L620.s2, L622.s1, L622.s3, L624.s1, L624.s2, L626.s1, L626.s2, L626.n3, L626.s4, L626.s6, L626.s7, L626.s8, L628.n1, L630.s1, L630.n3, L630.s4, L630.s5, L632.s1, L632.s2
- **S4 sentence FROZEN** (28): L487.s1, L491.s1, L499.s1, L502.s1, L509.s1, L517.s1, L520.s3, L520.s4, L520.s5, L526.s2, L526.s3, L526.s6, L526.s9, L526.s10, L526.s14, L546.s1, L556.s3, L558.s3, L562.s2, L598.s1, L604.s1, L616.s1, L616.s3, L622.s2, L624.s3, L624.s4, L626.s5, L630.s2

## 7. Is a second round of Part A needed? (rule 10)

**Yes.** The map has gaps of both kinds rule 10 names: items no variant touched (§6: 647 of 815 template items, 473 of 577 middle items, 17 middle definitions neither varied nor named) and edges the computation could not settle (31 claimed only). The orchestrator has decided a second round (its decision 4). The gaps, in the critical review's order (not a plan; the rule for round 2 is written and committed before sending):

1. **The readings the candidates rest on, under their other choices** (§6.3): S108-1-I5 (C2); edit or boundary for the owner's changes (C5; C1 computed both ways); D6.3's quantifier (C6, C11: S44 turns on it); S108-3-I2 and S108-3-I5 (C8); the trace's extent and the tag encoding (C9); S108-3-I4 and its history (C10); S108-4-I1 (C11), S108-4-I2 (C12), S108-4-I3 (C13); the hand-set histories (I90; C7, C9, C10, C12, C13, whose counts equal the population meeting (E) by construction of the history).
2. **The untouched middle definitions upstream of the explanation definition** (§6.1): D6.9 ((E), Expl, (Suff), (Nec)); D11.2 (Dec, Expl, (Suff), (Nec)); D11.3 (Dec, Expl, (Suff), (Nec)); D6.8 (Expl, (Suff), (Nec)); D9.1 (Expl, (Suff), (Nec)); D9.2 (Expl, (Suff), (Nec)); D5.7 (Dec, Expl, (Suff), (Nec)). Then the other untouched middle definitions: D8.new1, D10.3, D12.7, D12.8, D13.7, D14.1, D15.1, D15.2, D15.5, E9.
3. **The edges claimed only** (31; §6.2), each with its "settle" (§4), and the places the program cannot compute (§6.3). V1.6's formula, without its added sentence, goes to round 2 as a variant for section 2; V1.7 and V2.8's part on L315.s7 go to Part B; V2.8's D16.XV part is V4.4, computed (the orchestrator's decision 3).

Also: the suite's blind spots (no claim separates D6.4 from V2.1 or V2.2; e2.38, e2.39) get cases; the whole-suite runs go to the Sonnet harness (the orchestrator's decision 5).

## 8. Unsure

- **Mapping rows to items** is this agent's reading of each row's item text (the table `M` in the builder): line-level references (e.g. "L17, L49, L61, L69") are mapped to the sentences on those lines that the row's words name (the four writing Account(ℰ) ∧ ¬Dec(t)), or to the claims that test the lines where the row names them (e1.12, e1.25); "the L267–L277 table" to every sentence on L269–L277.
- **Touched** counts an item touched when a variant varies it or a computed or contradicted edge names it (an edge into an `X:` node also touches the definitions that define it); an item named only in claimed-only edges is "claimed only". An item a variant reads but no edge names is counted untouched, so the count of untouched items is an upper bound on what the variants did not reach, and a lower bound on nothing (silence is not agreement, rule 3).
- **Summary edges** (`s<n>`) restate the computing files' own summary tables; they add no computation.
- **D18.1's graph** is the program's `claims_b.DEP` after round 4, read from its source; D_TO_NODE folds several definitions into one node (e.g. D13.8 into CCE, while `Episode` is its own node: mapped here to D13.8 by hand, and `CT` to D12.2). The graph's ancestors of (Suff), (Nec) and being an explanation are those of D16.XV's one node, DefeatConds.
- **Kinds** follow the computing files' kinds; "keeps", "no claim separates" and the rows "moves nothing in (E)" are read as *independent of*.
- The whole-suite runs of sections 1–4 were made by the computing agents' own scripts, under load, with capped parts re-run at cap 300 (each file's §7.1); this map takes their results as they give them and reran nothing. (The critical review reran eight claims; they agree.)
- **Second checker.** The runs behind O1 and O3 import the section copies and write nothing in them; O3's trace extent is the second checker's encoding (the output's trace from o_s to o_t, the other occurrences' traces at their own occurrence), one of several a round-2 agent could state. Section 4's §3 and §9 and section 1's §8 and §9 carry wording the map no longer uses ("the owner's one-part sign (S44)": the owner's S44 case is the two-part sign; "D13.4's reflexivity": D13.4 states none, FC85 (a) does); the section files are left as they are.

Built by one Opus 5.5 agent under rules 6 and 10, 28 September 2026; corrected by the second checker (Opus 5.5, rule 9), 28 September 2026. Nothing ruled; nothing applied to the theory (rule 11).
