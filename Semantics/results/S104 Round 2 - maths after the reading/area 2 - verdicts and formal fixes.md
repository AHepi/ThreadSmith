# S104 Round 2 - area 2 (L229-L372): verdicts and formal fixes

*Checker 2 of 3 (Opus 5.5), decision S40. Maths and code; no new prose. Text: `tests/103 …after round 1.md` (md5 f31ebb1f050783f1a84f6136cec20fcd). Model copy: `area 2 model/model/` (run from `area 2 model/`: `PYTHONHASHSEED=0 python3 -B -m model.run --claim FCnn --scale 4 --time-cap 45`). Runs: `area 2 - runs.txt`. Text changes: `area 2 - text changes.json` (A2-T1…T13).*

Verdicts: **HM** holds against the maths · **HW** holds against the words · **INV** rests only on an invention the text leaves open (rule 6) · **NO** does not hold. Weighed on arguments (rule 8); the finished rulings L255-L257 and L315-L568 used where their arguments hold.

## 1. The formal fixes (old → new)

| id | old | new | why | code |
|---|---|---|---|---|
| D6.3 | Slot_C(ℰ,k) :⟺ ∀(a,b)∈C: Ans_p(a,b)≠⊥ ∧ L^E_k(τa,σb) = {w : w_δE = Ans_p(a,b)} (and nothing else) [I24, I83] | Det_C := {(a,b)∈C : Ans_p(a,b)≠⊥}; Slot_C(ℰ,k) :⟺ δ_E∈V_k ∧ Det_C≠∅ ∧ ∀(a,b)∈Det_C: {w_δE : w∈L^E_k(τa,σb)} = {Ans_p(a,b)} [A2-01 = I24 (b) + I83 (b); quantifier A2-02; I79, I82 unchanged] | L255 "does not appear … as a component" with L397 ("joined … by "and", read structurally") and L273 ("restates the answer"); M1-M3 met (E) under the old test | `core.slot`, `NC1_READING="area2"` |
| D6.9 | a relabeling :⟺ ∀b ((a,b)∈C ⇒ Ans_p(a,b) = Ans_p(1,b0) ≠ ⊥) [I26] | ∀b ((a,b)∈C ⇒ Ans_p(a,b) = Ans_p(1,b0)), ⊥ = ⊥; settles I26 (A2-T2) | automorphism and no-relation-change readings fail even for Acc (ruling M8, M9); "≠⊥" not needed (FC21 (a2)) | FC21 (a2) |
| FC21 | (a) Relab ∧ A_C ∧ τ(1)=1 ⇒ ¬NC2, Relab with ≠⊥ | (a2) Relab (⊥ allowed) ∧ A_C ∧ τ(1)=1 ⇒ ¬NC2; (d) ∃ℰ: A ∧ NC1 ∧ NC2 ∧ τ(1)≠1 on a relabeling contract ⇒ L257 needs (F2) and (A) (A2-T3) | FC21 (b), ruling M6, M12 | FC21 parts 4, (d) |
| D8.2 | Conf at "a pair of the target that both translate": Ans_E ≠ Ans_E' ∨ … | (a,b)∈A_D×B_D (admitted, D1.1, L141), both translate; Ans_E(τa,σb) ≠ Ans_E'(τ'a,σ'b) in Y_p∪{⊥}: ⊥≠y for y∈Y_p, ⊥=⊥ [I21]; settles H10 (A2-T8) | L317 (ii) "Their answers then agree at every pair of C" needs ⊥≠y (H10 model) | none (the code already reads so) |
| D8.3 | Riv :⟺ [Offered(ℰ,ℰ',p) ∨ Offered(ℰ',ℰ,p)] ∧ ∃ Conf | Riv :⟺ Off(ℰ,p) ∧ Off(ℰ',p) ∧ [Offered(ℰ,ℰ',p) ∨ Offered(ℰ',ℰ,p)] ∧ ∃(a,b)∈A_D×B_D Conf; Off a unary primitive (I33 amended); nothing ranges over rivals (S20) | L315 "a candidate that nobody has offered is no one's rival" | `core.rivals(both_offered)` |
| D8.5 | ConfCl :⟺ [∀R (Ans^R_p(a,b)=y ⇒ R∉Allow)] ∨ [∀R (Meets_ab(ℰ,R) ⇒ R∉Allow)] (both vacuous) | [∃R Ans^R_p(a,b)=y ∧ ∀R (Ans^R_p(a,b)=y ⇒ R∉Allow)] ∨ [∃R Meets_ab(ℰ,R) ∧ ∀R (Meets_ab(ℰ,R) ⇒ R∉Allow)], y := Ans_E(τa,σb) [A2-03] | L315 lead "χ excludes what the candidate's organization and transport give there"; a claim allowing everything conflicted (ruling check 3) | `core.conf_claim`, `CONFCL_READING="area2"` |
| D8.new1 | — (I36 in the register only) | k∈Γ, k'∈Γ' have one counterpart :⟺ λ(k)=(N,θ,κ), λ'(k')=(N,θ',κ'), θ[V_k]=θ'[V_k'], θ,θ' bijections onto those ports; β := θ'⁻¹∘θ; DiffRel_ab(k,k') :⟺ L^{E'}_{k'}(τ'a,σ'b) ≠ β_*(L^E_k(τa,σb)) (L562, L564); κ as I14. Settles I36 less κ (A2-T9) | by-name comparison contradicts L315's recoding sentence (ruling check 4) | none; FC44 run |
| D10.3 | Test: record of R* and Ans_p at (a,b)∈C | Test_ab (Conf at (a,b)∈C) := Ans_p(a,b), with (R*_j(a,b))_j where Ans_E(τa,σb) = Ans_E'(τ'a,σ'b); with its (K3) premises. Arg_test (H20): 'Test_ab; Acc(ℰ) ⇒ A_ab(ℰ) ∧ Meets_ab(ℰ,R*)' (MP, MT). [A2-06; settled A2-T11] | L317 read two incompatible ways (Mimo, GLM); its next sentence ("Whatever it records … rules out at least one") fixes this one | none (FC47 (b) unchanged) |
| D10.4 | ETV_j(ℰ;p) :⟺ ∃ℰ' Prob_j(ℰ,ℰ';p) of kind ii [I37] | unchanged; settles I37 by pointer (A2-T12) | "for some assessor" not excluded by the words (ruling) | none |
| D10.6 | "that is j's choice (D9.8)" | "that is j's choice (D9.8 and the note after it: Out_j depends on Accepted_j, Forms_j, declared inputs)"; "while … usable" = Out_j at the assessment's place ξ, time outside the model [A2-07] | D9.8 carries no choice clause | none |
| D5.7 | Faithful_C := F1∧F2; Fid⁺_C := F1∧F2∧A "where a line counts (A) as fidelity: L247, L520" [I49] | Faithful_C := F1_C ∧ F2_C (L189, L245); QFid_C := A_C (L247's heading, a separate name); Fid⁺ dropped in area 2. L220 (area 1), L520, L630 (area 3) left to those areas | L245 and L247 need no wide extent | none |
| D7.4 | E_v's transport and commitments "(L231; the text does not fix them further)" | 𝒱 a declared family; each v declares (E_v, t_v, Γ_v) as L231 fixes for any declared operation ("t' the transport the operation carries t to and Γ' the commitments it leaves") | L231 fixes it | none |
| E1 | identification contract: boundaries varying u_H at θ = 45° [I65, I92] | C_id := {1}×B (u_H and u_θ varying; no setting edit); settles I65's identification contract (A2-T13) | the setting reading of "whose edits alter the observed L" makes L325 fail (FC28 look); one θ-setting also does (GLM) | FC28 new parts |
| D1.4/I14 | V_N := ∪_{j∈N} V_j for every N | V_{J_D} := V_D (Sol_{J_D} = Sol_D), other N as before [A2-04] | FC25 (b) failed on I14's bookkeeping only | `Org.sol_sub` |
| D3.5 | unchanged: Stated(C,Σ) :⟺ (A×B)∖C ⊆ Excl(Σ) | L257's second sentence replaced by it (A2-T1); settles I27 | L141 C ⊆ A×B; L43, L159 | none |
| FC23 | (a), (b) | + (c) M1, M2, M3 meet (E) under D6.3 as registered and fail NC1 under A2-01; + (d) M5 meets (E) under A2-01 (quantifier A2-02 open) | ruling L255-L257 | FC23 (c), (d) |
| FC25 | (a) under I32 | (a*) for any table component k (L_k constant in the edit): (1,b),(a,b)∈C ∧ proj^λ_{V_k}Sol_{λ(k)}(a,b) ≠ proj^λ_{V_k}Sol_{λ(k)}(1,b) ⇒ ¬F1 (A2-T5); (b) holds under A2-04 | FC25 (a) witness (non-degenerate, program check) | via core |
| FC27 | τ(set H:=h) = set H:=h | + look: under Mimo's τ' (set H:=h ↦ a setting of E_rev's L), F2eq holds on C1, Hom fails, NC1 fails (r_L a slot) | L325 "intervening on H … the calculation's L" fixes τ; the lever fails anyway | FC27 new look |
| FC33 | (b) not tested | (b) L265 holds of every conjunct but Stated(C,Σ) (A2-T4) | Stated is a condition on Σ | none |
| FC44 | under I36 | under D8.new1 (unchanged result) | — | run |
| FC48 | ¬Conf on C ⇒ equal answers | + hypothesis: both transports translate every pair of C [A2-10] | the code already asks it | none |
| FC50 | (b) "a function of p's data and j alone" | "… of p's data and j's declared inputs (Forms_j, Scope_j, Accepted_j)" | Mimo's case changes j's own declared scope | none |
| FC51 | (a) "… or τ' fails Hom on edits new in C' …"; (b) ψ any permutation | (a) that channel dropped (Hom is on τ as a whole, D5.5); (b) ψ keeps footprints [A2-08]; (F2),(A) half of L568 not yet formalized | check §5; search results | none |
| FC52 | first ⇒ second (D8.5 vacuous) | first ∧ ∃R Meets_ab(ℰ,R) ⇒ second; and ∃ pairs with first ∧ ¬second (the 'or' is two routes) | D8.5 fixed | FC52 parts 2, 3 |
| FC53 | (a) X_j(Acc(ℰ)) ≠ ∅ | (a) if the stated assumption (χ ∧ Applies) → ¬Acc(ℰ) (L397) is live for j … [A2-09] | the computation supplies it by hand | none |
| FC58, I64 | Z = ℝ^n | Z any vector space, g linear on Z, ker g = ker of g on Z | "linear g" needs a vector-space domain; proper non-linear subsets are not "linear g" | none |
| FC63 | (c) lists NC2 | (c) lists NC1 and NC2 (NC1 holds by I82 for this query) | L343 "Non-circular dependence is met" | none |
| FC64 | "whose intermediate scopes match" | ∀i<n: S_{a_i}⋯S_{a_1}z ∈ dom π | the formal was as vague as the words | none |
| FC65 | R;R' a simulation for τ'∘τ | over a ∈ dom τ with τ(a) ∈ dom τ' | GLM (partial τ) | none |
| FC67 | fidelity kept ∧ provenance carries over (I54) ⇒ Rep kept | fidelity kept under r and the reader's r⁻¹; provenance clause dropped (not L365's "content"; I54 is area 3's) | Mimo, GLM | FC67 part 2 → not tested |
| FC68 | (b) "the forms are admitted"; (c) "a premise" | (b) forms {MP, MT} ⊆ Forms_j; (c) a premise about the test's background and instruments (L369's "a premise about them") | as the code already does | none |
| FC104 | L247, L520 need Fid⁺ | no line of L229-L372 needs Fid⁺; open only for L220 (area 1), L520, L630 (area 3) | D5.7 | none |
| register | I83 → FC23, FC24; I84 → none | I83 → every result computing NC1; I84 → every result computing (F2) (U6) | check §4.4, §5 | none (register data) |

## 2. Verdicts, item by item (104 items)

| id | verdict | reason (one line) | formal fix | code | runs |
|---|---|---|---|---|---|
| D3.5 | HW | L257 "subset of the edits" vs C ⊆ A×B (L141); pairs needed (L43, L159) | D3.5 unchanged; A2-T1 settles I27 | none | FC21, FC26 held |
| D5.1 | INV | π partial, τ,σ partial, κ: I16, I17, I14 open; "on the stated scope" consistent with partial π; L189 is area 1 | none | none | — |
| D5.3 | INV | δ_E (I20): (a) excluded by L253, (b) by L265 ("None inspects a label"); I20 vs (c) open | none | none | — |
| D5.4 | NO | L245's "signature on C" of a component of E is read through τ (L119, D4.3); true of every component with a counterpart | none | none | FC17 held |
| D5.5 | INV | range of Hom (I18) and I84 open; "(F2) at a pair" = F2eq (D5.7) | none | none | FC19 held |
| D5.6 | INV | ⊥=⊥ (I21), κ(⊥) (U1) are the program's | none | none | FC20 unchanged (CEX, area 1) |
| D5.7 | HM | Fid⁺ not needed by L245, L247 | §1 D5.7 | none | — |
| D6.3 | HM | I24's "constrains nothing else" and I83 narrower than L255+L273+L397 | §1 D6.3 (A2-01) | core.slot | FC23 (c) as claimed; FC24, FC26, FC34 held |
| D6.4 | NO | Contrast/Lost = the words under I21, I22; asymmetry → OQ-1; G = Γ → OQ-2 | none | none | FC22 held |
| D6.5 | NO | conjunction NC0∧NC1∧NC2 is L255 (I25 by L273) | none | none | — |
| D6.6 | NO | "where/by whom" answered: the scope is a declared input (L522, L524) | none | none | — |
| D6.9 | HW | L257 fails without (A), (F2) (FC21 (b), M6, M12); "relabeling" undefined | §1 D6.9; A2-T2, A2-T3 | FC21 | FC21 (a2), (d) as claimed |
| D6.10 | HW | via FC25 (a): L269 "under any contract containing one" overstates; several table components: NO | A2-T5 | none | FC25 held |
| D7.1 | INV | which restriction is declared is open by design (L287); its absence from L522 is FC98's (area 3) | none | none | FC-E1 reproduced |
| D7.3 | NO | "nonempty B" is L293's | none | none | — |
| D7.4 | HM | D7.4's "(the text does not fix them further)" ignores L231's declared-operation clause | §1 D7.4 | none | — |
| D7.5 | NO | appositives define; "exactly when" is the claim, scoped by L305's last sentence | none | none | FC37 held |
| D7.6 | NO | faithful (both readers) | none | none | FC41 held |
| D8.1 | NO | R's range fixed by L315 ("footprint", "no physics"); Hom at a pair is I18's (L242) | none | none | FC44, FC47 held |
| D8.2 | NO / HW (H10) | A_D×B_D are the admitted pairs (D1.1, L141), so "admitted" is not dropped; "differ" fixed by pointer | §1 D8.2; A2-T8 | none | FC48, FC49 held |
| D8.3 | HM | L315 requires both candidates offered | §1 D8.3 | core.rivals | FC43 held |
| D8.5 | HW | the words' strict "every relation … under which it could meet" is vacuous; lead clause excludes that | §1 D8.5; A2-T10 | core.conf_claim | FC52 parts 2-3; FC53 held |
| D10.1 | NO | "decided" = one ruled out (L8, L71); conflict is no one's view (L315) | none | none | — |
| D10.2 | NO | "admitted" as D8.2 | none | none | FC49 held |
| D10.3 | HW | two incompatible readings; L317's next sentence fixes one | §1 D10.3; A2-T11 | none | FC47 held |
| D10.4 | HW | assessor unnamed ("for some assessor" not excluded) | D10.4; A2-T12 | none | FC43 held |
| D10.5 | NO | negative clause follows from the conjunction | none | none | — |
| D10.6 | HM | citation misplaced; time reading unrecorded | §1 D10.6 | none | — |
| FC01 | NO | monotone by (O); the look turns on I21 ("none"/"several" merged), named by L255's loss clause | none | none | held |
| FC17 | NO | holds by construction; L245 fine under D4.3 | none | none | held |
| FC19 | NO | Mimo's two alike-projecting subnetworks are not separated by C (L281, L568), so no "decomposition in error" on C | none | none | held |
| FC21 | HW | as D6.9 | §1 FC21 | FC21 | held; new parts as claimed |
| FC23 | HM | (b) against the claim's wording (U3), not L273; M1-M3 against I24/I83 | §1 FC23 | FC23 (c), (d) | CEX (b) unchanged; (c), (d) as claimed |
| FC24 | HW | matter 7: "an account" there is a candidate | A2-T6 | none | held |
| FC25 | HW (a); INV (b) | (a) non-degenerate witness; (b) I14 bookkeeping | §1 FC25, D1.4 | core.sol_sub | CEX → HOLDS |
| FC26 | NO | holds on C1, C2 under A2-01; C3 look turns on A2-02 | none | none | held |
| FC27 | NO | τ fixed by L325's words; τ' fails Hom and NC1 | §1 FC27 | FC27 look | held; look as expected |
| FC28 | HW | "whose edits alter the observed L" admits the setting reading, under which L325 fails | §1 E1; A2-T13 | FC28 parts | held; new parts as claimed |
| FC29 | NO | C ⊆ A_D×B_D; holds by construction | none | none | held |
| FC33 | HW | L265's first sentence fails of Stated(C,Σ) | A2-T4 | none | held |
| FC40 | HW | matter 8: L313's "such commitments" at L311 needs step (c) | A2-T7 | none | held |
| FC41 | NO | "when Γ is infinite … can" is true; finite blocks: FC41 (c) | none | none | held |
| FC43 | NO | symmetric by form (Conf) and by "one … the other" (Riv); Mimo's reading parked (P-1) | none | none | held |
| FC44 | HW | "one counterpart", "different relations" unfixed at L315 (fixed only at L562, L564) | §1 D8.new1; A2-T9 | none | held |
| FC46 | NO | L315 "claims (F1), (F2), (A) at every pair of C"; "whatever the target does there" | none | none | held |
| FC47 | NO | L317 itself unpacks "who can use it"; GLM's case is I89's | none | none | held |
| FC48 | HW (H10); INV (partial τ, I17) | fixed by A2-T8; formal hypothesis added | §1 FC48 | none | held |
| FC49 | NO | "admitted" as D8.2 | none | none | held |
| FC50 | HM | (b)'s "data" unstated | §1 FC50 | none | held |
| FC51 | HM | (a) impossible channel; (b) unstated footprint restriction | §1 FC51 | none | held |
| FC52 | HM | a result of D8.5's vacuity | §1 FC52 | FC52 parts | restated part holds; two-routes witness found |
| FC53 | HM | (a) asserts an argument the computation supplies by hand | §1 FC53 | none | held |
| FC57 | NO | f, g : Z → … fix the domain; "attainable" = y∈g[Z] is the only reading under which (I2) holds | none | none | held |
| FC58 | NO (words); HM (I64) | "linear g" needs Z a vector space; an independent calibration is a row outside the row space | §1 FC58 | none | held |
| FC60 | INV | registered circularity rests on I39, I89 | none | none | held |
| FC62 | NO | "unchanged" = at the baseline; G ranges over Γ; no slot under A2-01 (k full at the baseline) | none | none | held |
| FC63 | INV (c-i); HM (NC1) | L343 "every intermediate product is a determinant suborganization whose hidden ports project away" gives (c-ii); (c-i) is I99's | §1 FC63 | none | CEX (c-i) unchanged |
| FC64 | HM | scope pinned | §1 FC64 | none | held |
| FC65 | HM | partial τ pinned | §1 FC65 | none | held |
| FC66 | NO | e_0 = 0 by definition (L363); "follows" = from the stated hypotheses | none | none | held |
| FC67 | HM | provenance is not L365's content | §1 FC67 | FC67 | held |
| FC68 | HM | forms and shared premise pinned (the words have them) | §1 FC68 | none | held |
| FC104 | HM | as D5.7 | §1 FC104 | none | not tested |
| I03 | NO; INV (fixed V, J; absent ports) | L103, L255, L339 carry deletion as the full relation; the rest is L103's (area 1) | none | none | FC01 held |
| I15 | NO | L231 "active commitments" settles it (T01) | none | none | — |
| I18 | INV | range of Hom open | none | none | — |
| I19 | NO | range settled by L315; Hom at a pair → I18 | none | none | — |
| I20 | INV | as D5.3 | none | none | — |
| I22 | NO | "the claimed way" = (A)'s, which L315 says a candidate claims at every pair; asymmetry → OQ-1 | none | none | — |
| I24 | HM | → A2-01 | §1 D6.3 | core.slot | as D6.3 |
| I25 | NO | L273 | none | none | — |
| I26 | HW | settled by A2-T2 (D6.9 without ≠⊥) | §1 D6.9 | FC21 | as FC21 |
| I27 | HW | settled by A2-T1 | D3.5 | none | — |
| I28 | NO | grain a declared index, stated not defined (L31, L524, L526) | none | none | — |
| I29 | INV | as D7.1 | none | none | — |
| I30 | NO | L307 states the families | none | none | FC38, FC39 held |
| I31 | NO | L311 "no minimal route exists" excludes bounded routes (T12) | none | none | FC40 held |
| I32 | INV | constant relation settled by L269; counterpart open | none | none | FC25 held |
| I33 | NO | symmetric by the words (T09); Off added (D8.3) | §1 D8.3 | core.rivals | — |
| I34 | INV | what a claim is stays open (S27; L397) | none | none | FC53 held |
| I35 | NO | D8.6 is L315's sentence (T06) | none | none | FC54 held |
| I36 | HW | settled by A2-T9 (D8.new1), less κ | §1 D8.new1 | none | FC44 held |
| I37 | HW | settled by A2-T12 | D10.4 | none | FC43 held |
| I49 | HM | → D5.7 | §1 D5.7 | none | — |
| I63 | NO | the text's tags follow what they name (T11) | none | none | FC57 held |
| I64 | NO; HM (Z) | as FC57, FC58 | §1 FC58 | none | held |
| I65 | HW | identification contract settled by A2-T13; U_H, U_θ are values, not ports (L325 "these ports" = H, θ, L) | §1 E1 | FC28 | FC28 held |
| I66 | INV | encoding choices; field fixed by "real" | none | none | FC63 |
| I79 | NO (words) | L255 names both routes; where boundary values sit → OQ-3 | none | none | — |
| I83 | HM | → A2-01 | §1 D6.3 | core.slot | FC34 held |
| I84 | INV | open; register it against every (F2) (U6) | register | none | — |
| I86 | NO | a search device; stays out of the text | none | none | — |
| I92 | INV | grids, exact values, fibre query's ⊥ | none | none | FC28 held |
| I99 | INV | as FC63 | none | none | FC63 |
| U1 | INV | κ(⊥) := ⊥ is the program's → A2-05 | register | none | FC20 unchanged |
| U6 | HM (record) | I83, I84 act in every (E)/(F2) result; G4-B8's text point: NO (ruling) | register | none | — |
| H10 | HW | L315's "differ" unfixed; L317 (ii) needs ⊥≠y | §1 D8.2; A2-T8 | none | FC48 held |
| matter 7 | HW | as FC24 | A2-T6 | none | FC24 held |
| matter 8 | HW | as FC40 | A2-T7 | none | FC40 held |
| matter 12 | HM | in L229-L372 only L245, L247, both narrow; L220, L520, L630 are areas 1, 3 | §1 D5.7 | none | — |
| matter 13 | NO | L311's "(B) records the collective contribution" fixes its sense | none | none | — |
| E02 | NO | FC-E1 follows from L231 (π kept), L287, (B), (E): (F2) is part of the work (B) measures → OQ-5 | none | s104_external.py path only | FC-E1 reproduced |
| E15 | NO | scope: asks a worked idealization; L277, L363 claim nothing more | none | none | FC66 held |
| E19 | HM | the maths' NC1 was narrower than the words; rest (A2-02, I79, value maps) open | §1 D6.3 | core.slot | FC23 (c) |

Context items (no verdict asked): E01, E18 (consistent with FC25 (a*), (b)), E21 (FC-E5 reproduced, 193 families, 0 failures), C12 (scope), H20 (D10.3's argument named Arg_test).

**Counts.** HW 26 · HM 30 · INV 20 · NO 34 (split verdicts counted once, by the first). Text changes: 13 (formal 5, pointer 8, delete 0).

## 3. New inventions (provisional ids; the integration numbers them from I122)

| id | fills | taken | other choices | why this one |
|---|---|---|---|---|
| A2-01 | L255 "does not appear … as a component" | D6.3 new (I24 (b), I83 (b), Det_C ≠ ∅, relation nonempty) | I24 as registered; I83 as registered; a block (M6-B6: fails the forward pole, M10) | L255 with L273, L397; M1-M3 |
| A2-02 | the slot's quantifier over C | every determined pair (not applied to the text) | some pair; some pair, a component the contract's own edit replaces exempt (G7-B5) | M5 separates them; not run in the text's cases yet |
| A2-03 | D8.5's two disjuncts where nothing is given | existence clauses; settled at L315 by A2-T10 (second disjunct); first disjunct's clause rests on I34 | vacuous (registered) | L315's lead clause |
| A2-04 | I14's V_N for N = J_D | V_{J_D} := V_D | V_N = V_D for every N; U2 "no candidate" | L269 "meets (F1) as a decomposition does" |
| A2-05 | U1 | κ(⊥) := ⊥ (FC20) | κ undefined at ⊥; FC20 restated without it | recorded, not applied to the text |
| A2-06 | L317's test clause | D10.3 new; settled by A2-T11 | R* and answer always (registered); only where answers agree | L317's next sentence |
| A2-07 | L317 "while the argument stays usable" | Out_j at ξ, time outside | a time-indexed Out_j | nothing in (O), (Q) models time |
| A2-08 | FC51 (b)'s ψ | ψ keeps footprints | any permutation of Γ | the search used it |
| A2-09 | FC53 (a)'s premise | (χ ∧ Applies) → ¬Acc(ℰ) a stated assumption (L397) | a definition; none (Mimo: X_j empty) | L397 admits stated assumptions |
| A2-10 | FC48's hypothesis | both transports translate every pair of C | I17 total | L315 "claims … at every pair of C" |

Amended, not new: I24, I83 (→ (b)); I26 (≠⊥ dropped); I33 (+ Off(ℰ,p)); I36 (less κ); I49 (Fid⁺ dropped); I64 (Z a vector space); I65 (C_id := {1}×B); I14 (A2-04).
Settled in the text by this area (rule 6): I27 (A2-T1), I26 (A2-T2), H10 (A2-T8), I36 (A2-T9), A2-03 (A2-T10), A2-06 (A2-T11), I37 (A2-T12), I65 (A2-T13).

## 4. Owner questions (not applied; one line each side)

| id | question | one side | other side |
|---|---|---|---|
| OQ-1 | NC2's contrast when the baseline answer is not determined (D6.4, I22; GLM part 8) | asymmetric (the maths): only ⊥ at (τa,σb) counts; a contrast needs two determined ends | symmetric: a value against ⊥ at either point counts; under the asymmetric reading a question with ⊥ at the baseline and a value at an edit admits no NC2 (M13) |
| OQ-2 | may the deleted block G be the whole of Γ (D6.4; GLM part 6) | G ≠ Γ: with G = Γ NC2 asks little; the bite is NC1's | G ⊆ Γ (the text; L293's blocks): G ≠ Γ fails every one-commitment candidate |
| OQ-3 | where boundary values sit for NC1 (I79; Mimo part 4) | boundary coordinates of their own, checked apart (L255 names two routes) | carried by components (the program; the "law" clause makes one failure of two routes) |
| OQ-4 | a problem posed again once the ruling-out argument is no longer usable (D10.6; GLM part 11) | yes: L317 "while the argument stays usable" | S20 "the mistake shouldn't be able to creep back in" points the other way |
| OQ-5 | what "work" is in L231, (B), L305, L313 (E02) | work for (E) as a whole, (F2) included: d (V = U) is critical and indispensable (FC-E1) | work for the answer to 𝒬 only: a relevance condition (the external reader); a new definition, an invention |

Reader-marked, not owner questions: D5.1 (Mimo: value maps κ) — port values (I14), not where values are placed; I65 (Mimo: U_H ports or boundary) — fixed by L325; FC62 (GLM: counterpart a slot) — no slot under A2-01; FC63, I99 (GLM: optional wording) — the words give (c-ii).

## 5. Parked (S33, S34)

| id | point |
|---|---|
| P-1 | FC43 (Mimo part 10): "easy to vary" read as "has a variation that still meets" — about what hard to vary covers; not applied |

## 6. Not done

- FC51 (b) extended to (F2), (A) (GLM): stated, not coded.
- A2-02's three readings not run on the text's worked cases (the ruling's advice); only M5.
- The whole-suite comparison (every claim, original against copy): see `area 2 - runs.txt`, last section.
