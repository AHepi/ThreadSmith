# S109: Part B round 1 - tabulation of the replies, before any ruling

*Rule 4 of `results/S109 Part B round 1 - how the replies will be read, written before sending.md` (c28d832). By the one Opus 5.5 agent that, under decision S56, does the whole reading of Part B round 1 (rules 3 to 8). Created at once and filled as it went (lesson S28). Written before any computing. Rules on nothing. "Candidate" or "explanation" for what the theory judges; "model" only for the program's folder or a small structure it builds (S43).*

## 0. Status

Complete, 29 September 2026, before any computing. Four replies, **34 variants** (B1 9, B2 9, B3 8, B4 8). Flags in §6: **two** out of Part B (PB3.8, no formal statement; PB4.4, a FROZEN definition changed beyond its sentence's formalization), nine variants that depart from an owner's decision by the reply's own account (computed, not flagged out; rule 4). All three class-a carry-overs taken up (PB1.1, PB2.1, PB4.1); of class b, five of six (R2V1.2 not taken up). Nothing ruled, nothing implemented, no theory text, formal core, claim, program, Part A file, decision or authority file written.

## 1. Before reading (rules 1, 2)

| check | state |
|---|---|
| rule 1: every call ended | run log (`returns/run log.txt`): `s109_glm_loop: every pass ended; accepted 4 of 4 jobs`, `loop ended 2026-09-29T03:33:07Z`; the pid in `<scratchpad>/s109_glm_run.pid` (1524) has exited |
| rule 2: receipts | checked by the orchestrator, only these fields: `key_found_in_output_and_replaced` 0 ×4, `sandbox_unchanged` true ×4, model reported glm-5.3; each response ends END OF REPORT |
| replies read (`.response.txt` only) | B1 `4f944a65246f34ed74122e5847929665` (3,434 words); B2 `997a42fd9e34d8274abf2df693ec3858` (2,963); B3 `064c62ae6cab33eb3065e1172e791de7` (2,370); B4 `763cc7eb71aae709eb5cf0b64384d0b3` (2,357); each pass 1, attempt 1 |
| not opened | reasoning files, stream files, guard logs, requests |
| marks used | the free set `.json` (44f5ce43…): each item's section and what it bears on; the carry-overs table of the rule |

Every "after" in every reply is marked **not run** by the reply. "Before" results cite `python3 -m model.run --claim …` runs in the sandbox; nothing here checks them (rule 5's work). Everything below is the replies' claims (rule 3).

## 2. Section B1 (organizations, kinds, questions and contracts): 9 variants

Marks: [B1: E Dec …] = the free item's section and what it bears on (template); FROZEN = not in the free set.

| id | free item(s) [mark] | kind | carry-over | old formal | new formal | old → new sentence | departs (reply) |
|---|---|---|---|---|---|---|---|
| PB1.1 | D3.5 [B1: E Expl Suff Nec] | replace | V1.7 (a) | Σ a declared input naming Excl(Σ) ⊆ A×B (I27); Stated(C,Σ) :⟺ (A×B)∖C ⊆ Excl(Σ) | Excl(Σ) := (A×B)∖C; Stated(C,Σ) holds of every (C,Σ) | none (L43.s4, L159.s1 FROZEN) | none |
| PB1.2 | D3.1 [B1: E Dec Expl Suff Nec] | strengthen | R2V1.9 (b) | C ⊆ A×B, (1,b0) ∈ C | ∧ Question(p) ⇒ ∀(a,b) ∈ C: Θ_admits(a) | none (L159.s3 FROZEN, contradicted) | S25–S27 |
| PB1.3 | D3.2 [B1: E Dec …] | replace | R2V1.8 (b) | Q(O,a,b;δ_O) ∈ Y_p ∪ {⊥}, Y_p free | Y_p := X_δD | none | none |
| PB1.4 | D4.2 [B1: –] | replace | R2V1.7 (b) | j ~_C j′ :⟺ ∃β bijection V_j→V_j′, X_v = X_β(v), L_j′ = β_*(L_j) on C | j ~_C j′ :⟺ V_j = V_j′ (ordered) ∧ sig_C(j) = sig_C(j′) | none | none |
| PB1.5 | L155.s6 [B1: –], changes with D3.4 [FROZEN, its formalization] | replace | R2V1.4 (b) | Found(p) requires ρ_p = constructed | Found(p) :⟺ ρ_p ∈ {selected, constructed} | "…requires ρ_p = constructed…" → "…requires ρ_p selected or constructed." | none |
| PB1.6 | L103.s1, D1.3 [B1: E Dec …] | replace | – | D−G sets L_j(a,b) := ∏_{V_j} X_v (the full relation) | D−G sets L_j(a,b) := ∅; an absent port: every component imposes ∅ on it | "A deleted component imposes the full relation on its ports." → "…the empty relation…" | none |
| PB1.7 | L141.s2, D3.1 [B1: E Dec …] | strengthen | – | (1,b0) ∈ C | ∧ ∃(a,b) ∈ C: a ≠ 1 | "…contains the baseline (1,b0)." → "…and at least one edit other than 1." | none |
| PB1.8 | L115.s1 (SC), D4.1 [B1: E Dec …, SCdef] | strengthen | – (lifts e1.00, V1.1 on D4.4) | sig_C(j) = {(a,b,L_j(a,b))} | sig⁺_C(j) = {(a,b,L_j(a,b),Sol_D(a,b)\|_{V_j})} | (K) gains a fourth component | none |
| PB1.9 | L113.s1 (SC) [B1: –], with D4.1, D4.2, D4.3, D4.4 [B1] | replace | – | sig_C(j) on C; kinds: classes of ~_C | sig(j) on A×B; kinds: classes of ~_{A×B}; D4.3, D4.4 read sig on A×B | "Fix an organization D and a contract C ⊆ A×B (Part III)." → "Fix an organization D." | none |

| id | predicted meaning (the reply's) | predicted scope: sign / vane / bridge / student's copy; made-up | claims it expects to move | small cases (run?) | edges named | inventions (other choices) |
|---|---|---|---|---|---|---|
| PB1.1 | NonVacuous: Sol_D(1,b0) ≠ ∅ ∧ Stated → Sol_D(1,b0) ≠ ∅; (E)'s form unchanged; Σ no longer read | stays ×4; enter: candidates on questions with Excl(Σ) ⊊ (A×B)∖C; no generated case moves (I85 default) | none | FC34 twin with Excl(Σ) = ∅: Acc F → T (not run) | blocks L43.s4, L159.s1; constrains D6.6; changes with D0.2 (I27); moves NonVacuous | drops I27 (other: I27 kept) |
| PB1.2 | (E)'s domain narrows to Θ-admitted contracts; no conjunct changes | vane, sign, bridge, student **on that reading** (Θ strict: bridge and student leave); nothing generated moves (Θ not computed) | FC-E examples where Θ is read | pole's settings of H leave on that reading (not run) | blocks L159.s3, L49.s4; constrains Θ (D0.1); moves the domain of (E) | Θ_admits of a bare edit (others: of an attributed organization at a grain; of the pair) |
| PB1.3 | (A) and Contrast compare answers in X_δD ∪ {⊥} | stays ×4; leave: the pole's identification question, E2's fibre query, Obst | FC28 (C_id), FC36, D3.3's I163 clause | FC28 area 2 (not run) | constrains D3.3; changes with E4, E9; moves what (A), Contrast read | settles I21 (others: Y_p free; any set with ⊥) |
| PB1.4 | no part moves; Argument 1's "of one kind" loses β | stays ×4 | FC05 (ii) | mirrored footprints: one kind → two (not run) | changes with D4.3; moves nothing in (E) | drops I10 (others: β; β preserving an order) |
| PB1.5 | Found widens; no part moves | stays ×4 | (QF) class (L544) grows | a selected contract (not run) | changes with D3.4; constrains (QF) | which values count as found (others: all three) |
| PB1.6 | Dependence: NC2 ≈ Contrast ∧ (Ans_E(x) ≠ ⊥ ∨ Ans_E(x0) ≠ ⊥) | stays ×4; enter: candidates whose commitments are idle for the answer | none stated as moving; a claim "Γ idle ⇒ ¬NC2" would flip | the idle-c case (before run as FC21's structure; after not run): Acc F → T | constrains D3.6; changes with D6.1; moves Dependence | empty-relation deletion (others: full; removal from J, out of reach) |
| PB1.7 | Question(p) gains a clause; no conjunct moves | stays ×4; leave: E_rev on C_id = {1}×B (no question) | FC28's C_id parts, FC22 (a) vacuous, D3.3 on C_id | FC28 area 2 (not run) | constrains L257/D6.9; changes with E1/E2; moves the domain of (E) | "some edit ≠ 1" (others: some edit no relabeling; two pairs with different answers) |
| PB1.8 | (K) finer; no part of (E) moves | stays ×4 | FC17, FC18 (at risk), FC05 (i) fails | k with a free port D fixes: one kind → two (not run) | blocks L119 (FROZEN); changes with D4.4 (lifts e1.00); moves Argument 1's claims | Sol_D(a,b)\|_{V_j} (others: Sol of {j} alone; baseline only) |
| PB1.9 | kinds contract-free; no part of (E) moves | stays ×4 | FC05, FC17, FC18 fail as stated | pole's c_L and a twin differing off C1 (not run) | blocks L119 (FROZEN); constrains L11.s2; moves Argument 1's claims | A×B as index (others: C; C ⊆ C′ ⊆ A×B) |

B1's list of items not varied and why: the reply's §(e) (organization tuple clauses, (O), representational freedom, displays, O_p, ρ_p beyond Found, D3.7, D4.4 via PB1.8, L103.s2 out of reach, glosses, defects, items bearing on nothing). R2V1.2 not taken up (its clause is stated in B3's terms).

## 3. Section B2 (transports, fidelity, the account, routes, exact constructions): 9 variants

| id | free item(s) [mark] | kind | carry-over | old formal | new formal | old → new sentence | departs (reply) |
|---|---|---|---|---|---|---|---|
| PB2.1 | L189.s2 [B2: Dec Expl Suff Nec], changes with D5.7 [FROZEN, its formalization] and D12.7 (Viol) | replace | R2V2.7 (a) | Faithful_C(t) := F1_C ∧ F2_C; Viol := ¬(F1_ab ∧ F2eq_ab) | Faithful_C(t) := F1_C ∧ F2_C ∧ A_C; Viol := Viol⁺ (adds ¬A_ab) | "…component and global fidelity conditions…" → "…component, global and question fidelity conditions…" | none |
| PB2.2 | D5.5, L241.s1 [B2: E Dec …] | weaken | – | F2_C := F2eq_C ∧ Hom(τ) | F2_C := F2eq_C | the formula loses τ(1)=1, τ(a₂a₁)=τ(a₂)τ(a₁) | none |
| PB2.3 | D5.4 [B2: E Dec …] | strengthen | – | F1_C :⟺ ∀k ∈ Γ … | F1_C :⟺ ∀k ∈ J_E … | none | none |
| PB2.4 | D5.6 (L249.s1) [B2: E Expl Suff Nec]; L253.s1 [B2] | weaken | – | A_C :⟺ ∀(a,b) ∈ C: Ans_E(τa,σb) = Ans_p(a,b), ⊥ = ⊥ | A_C :⟺ ∀(a,b) ∈ Det_C: Ans_E(τa,σb) = Ans_p(a,b) | L253.s1 + "where the target gives no answer, (A) asks nothing" | none (blocks L369.s2) |
| PB2.5 | D6.2 [B2: E Expl Suff Nec] | strengthen | – | NC0 always true | NC0 :⟺ no background component of E that assigns an input carries Ans_p(a,b) at any (a,b) ∈ C (I23's other choice (a)) | D6.2's gloss "holds of every candidate" → "the boundary data of E carry nothing of the target's answer" | **S45** |
| PB2.6 | D6.6 [B2: E Expl Suff Nec] | weaken | – | NonVacuous :⟺ Sol_D(1,b0) ≠ ∅ ∧ Stated(C,Σ) | NonVacuous :⟺ Sol_D(1,b0) ≠ ∅ | L257's second sentence leaves (E) | none |
| PB2.7 | D5.6 reads D6.3 [FROZEN, unchanged] | re-order a dependence | – | A_C(ℰ) | A_C(ℰ) ∧ NC1(ℰ) | L247.s1 + "The answer is not simply written in." | **S45**, **S44** |
| PB2.8 | L311.s2 (SC), D7.3 [B2: –] | weaken | – | CB(B;W) :⟺ ∅ ≠ B ⊆ W ∧ W ∈ S ∧ W∖B ∉ S | … ∧ \|B\| < ∞ | "(B) records the collective contribution." → "…the contribution of a finite block." | none |
| PB2.9 | D5.1 (L185.s1, L189.s1) [B2: E Expl Suff] | replace | – | π: X_D ⇀ X_E defined on Sol_D(a,b) at every translated pair (I16) | π: X_D → X_E total | L189.s1 taken literally | none |

| id | predicted meaning | predicted scope: sign / vane / bridge / student; made-up | claims | small cases (run?) | edges named | inventions |
|---|---|---|---|---|---|---|
| PB2.1 | Dec's feed: Rep, Held, T′ read Faithful with (A); Expl's shape kept | sign stays (on the constructed reading); vane stays; bridge **on that reading** (the held transport's (A) on the content's contract); student stays out | FC104.new1, FC12.new1, FC98 family, FC79, FC31 | FC104.new1 (b) run before: Sel True, Viol⁺ True at ('1','b1_45') ∈ H; after not run | changes with D5.7, D12.7; blocks L221.n1, L223.s3; moves Dec, Expl | I49 wide (others: narrow; wide at L220 only) |
| PB2.2 | (F2) pointwise | stays ×4 (student out); enter: FC27 area 2 under τ′ (Hom the only failing conjunct, run before), FC21 (d)'s τ(1) ≠ 1 candidate | FC27, FC21 (d), FC15, FC51, FC48 | FC27 area 2 (before run) | blocks L257.n3; constrains L271.s1; moves (F2) | I18's dropped choice (others: Hom; pointwise Hom) |
| PB2.3 | (F1) over J_E | stays ×4 (bridge on its reading); leave: candidates with unfaithful background | FC26, FC29, FC34 counts | FC21 (b)'s witness + inactive k1 (not run): Acc T → F | constrains L231.s2, L245.s4; moves (F1) | PB2-In1 (others: Γ; J_E minus input assigners) |
| PB2.4 | (A) over Det_C | stays ×4; enter: determined answers at ⊥ pairs (vane rivals) | FC26, FC46, FC48, FC20, FC23 (e) | M13 with L_cy(1,b0) = {(0,1)} (not run): Acc F → T | blocks L369.s2; changes with D6.4, D8.2; moves (A) | PB2-In2 (others: C; Det_C ∪ both ⊥) |
| PB2.5 | Dependence = NC2 ∧ no answer in a boundary slot | stays ×4; leave: boundary-written-in candidates | FC26, FC29, FC34, FC108 | M13 + background y := 1 (not run): Acc T → F | constrains D6.5; moves Dependence | I23 (a) (other: the gloss) |
| PB2.6 | (E) no longer reads Σ | stays ×4; no computed case moves | FC33, FC26, FC30, FC51 Stated cases | M13 with Excl(Σ) = ∅ (not run): Acc F → T | constrains L257.n2, L265.n1; changes with V1.7 (PB1.1) | I27 "no conjunct" (others: as now; defined, V1.7) |
| PB2.7 | (A) reads D6.3: Acc ⇒ ¬Slot_C for every k | sign stays under 'every', leaves under 'some'; vane stays; bridge stays; student out; leave: E_enc, the one-part sign, the pole's E_enc and forward candidate on C2 | FC23.new1 (h), FC25.new2 (a), FC23 (e), FC26 | FC25.new2 (b) run before; after not run | blocks L269.s2; changes with D6.3; moves what (A) reads | I136's quantifier (not re-chosen; 'every') |
| PB2.8 | no part moves | stays ×4; infinitary example: CB = ∅ | FC40, FC39, FC41–FC43 | FC40 (before run) | blocks L313.n3; constrains L311.s1 | PB2-In3 (other: B unrestricted) |
| PB2.9 | a transport exists only with total π | stays ×4; leave: generated witnesses with partial π | FC20, FC49, FC45, FC48 | FC21 (b)'s witness with π undefined off Sol_D (not run) | changes with D8.2, D8.3, D12.5; constrains L315.s4 | I16 total (others: partial on solutions; on a stated scope) |

B2's items not varied (reply §(e)): L185.s1 (through D5.1), D5.2, D5.3, D6.1 (reads B1's D1.3), L253.s1 (said to be B1's; but PB2.4 records a changed sentence for it), L245.s1–s3, L265.s2, D6.10, L347.s2, L307.s1, L329.s3.

## 4. Section B3 (provenance, histories, representation, construction, repair, the physical module): 8 variants

| id | free item(s) [mark] | kind | carry-over | old formal | new formal | old → new sentence | departs (reply) |
|---|---|---|---|---|---|---|---|
| PB3.1 | D12.4 [B3: Dec Expl Suff Nec] | replace | R2V2.4 (b) | prov per part; transfer gives each part its value; a binding newly built gets Con | parts := {t}; a holding reached by a copy of the carrier's whole content inherits prov(t,o) whole | none | **S41 Q2** |
| PB3.2 | D12.5, L207.s1 [B3: Dec …] | weaken | – | Rep_ℓ(o,c) :⟺ ∃t [Faithful_C(t) ∧ (Sel ∨ Con)] | Rep_ℓ(o,c) :⟺ ∃t [Faithful_C(t)] (= Held) | L207 likewise | none (blocks L211.s1, L211.s3) |
| PB3.3 | L195.s1, L195.s5 [B3], changes with D12.1 [FROZEN, formalization] | strengthen | – | Sel(t;𝒯,μ,H) as D12.1 | Sel adds C ∩ Occ(h(t)) ⊆ H | "…fidelity on H" → "…fidelity on every pair of C that has occurred, H among them" | S41 Q2 in part, on that reading; S44, S41 Q15 on a selection history |
| PB3.4 | L199.s1, L199.s3 [B3], changes with D12.3 [FROZEN, formalization] | re-order a dependence | – | Dec(t,o_t) read on h(t,o_t) | read on h∪(t) := ∪{h(t,o): t held at o}; Sel, Con likewise | "Declared. Neither of the above." → "…on any history of t." | **S41 Q2** |
| PB3.5 | D11.5, L217.s2 (SC) [B3: Dec …] | weaken | – | Occurs(a,b,ξ) primitive, read through Θ | Occurs(a,b,ξ) :⟺ a admitted at ξ ∧ b actual at ξ | "…actually occurring:" → "…admitted:" | S41 Q2 in part |
| PB3.6 | D11.1, L169.s1 [B3: Expl Suff Nec] | strengthen | – | Occ: physically located carriers, by Θ | Occ := those inside the declared boundary β of s | "…a physically located carrier." → "…inside the system's declared boundary." | S41 Q2 in part, on that reading |
| PB3.7 | D13.4, L169.s3 [B3: –; L169.s3 Expl …] | replace | – | d ≡_ℓ c :⟺ faithful transports both ways on C_c | d ≡_ℓ c :⟺ Ans_d = Ans_c on C_c | "…not identified by having the same outputs" → "…identified by…" | none |
| PB3.8 | L225.s1, L225.s4 (SC) [B3: –] | drop (s4) | – | no formal change (D12.8 FROZEN) | none | "Only the second can be originative under Part X." dropped | none |

| id | predicted meaning | predicted scope: sign / vane / bridge / student; made-up | claims | small cases (run?) | edges named | inventions |
|---|---|---|---|---|---|---|
| PB3.1 | inheritance whole | student's copy **enters**; others stay | FC30.new1 (d), (f) | SC1 `n=2, held=[1,1], trace=[1,0], selc=[0,1]`: before run `[{'o1':'Con'}]`, Dec at o2; after (not run) `{'o1':'Con','o2':'Con'}` | blocks L405; constrains D12.3; moves Dec … | I54's other choice (others: per part; a fourth value) |
| PB3.2 | Sel's exclusion bans every earlier faithful holding | sign, vane **on that reading** leave; bridge stays; student stays Dec | FC98, FC12.new1 | SC2 (not run before or after): `[{'o1':'Dec','o2':'Sel'}]` → `[{'o1':'Dec','o2':'Dec'}]` | blocks L211.s3, L211.s1; changes with D12.5 / L205.s1; moves Sel's exclusion | none new (drops I48's clause) |
| PB3.3 | Sel harder | leave: selections with an unmet occurred pair; vane on that reading | FC81, FC95, FC102.new1, FC104.new1 (b) | SC3 (before "run as FC83's setup"; after not run): Sel → Dec | changes with D12.1; constrains L223.s3 (partly); moves Sel | occurrence up to o_t (others: up to e; all of h) |
| PB3.4 | Dec per transport | student's copy **enters**; others stay | FC30.new1 (d), (g), FC12.new2, FC78, FC83 | SC1 after (not run) | blocks L193.s1; changes with D12.3 | h∪ (others: last holding's, as now; earliest) |
| PB3.5 | Sel's H-clause reads admission | enter: FC30.new1 (e)'s link with nothing tried; student stays Dec | FC30.new1 (e), FC35, FC77, FC104.new1 (b) | SC4 (before run: Dec True; after not run: Sel) | changes with D12.1; constrains L223.s3 | admission × actual boundary (others: Θ by hand; the edit enacted) |
| PB3.6 | histories inside β | student's copy enters **on that reading** (textbook outside β) | FC30.new1 (d), FC12.new2, FC98, FC35 | SC1 on that reading (not run) | changes with D11.3; constrains D16.3 | "inside β" (others: anywhere; β plus relayed-in) |
| PB3.7 | nothing in the definition; New (Origin) moves | bridge's CreateEx **on that reading** | FC85 (b), FC89, FC90.new1 | SC5 (not run) | blocks L413.s1, L413.s2; changes with D13.5 | output equality on C_c (others: C_d; C_c ∪ C_d) |
| PB3.8 | nothing | nothing | none | – | constrains D13.3, D13.6 | none |

B3's items not varied (reply §(e)): L201.s2–s3, L219.s1, L225.s3, L403.s2–s3, L437.s1, L441.s4, and the definitions of Parts X–XII upstream of no part.

## 5. Section B4 (rivals, problems, criticism, the class, the Arguments): 8 variants

| id | free item(s) [mark] | kind | carry-over | old formal | new formal | old → new sentence | departs (reply) |
|---|---|---|---|---|---|---|---|
| PB4.1 | L315.s7 [B4: Suff Nec], changes with D9.8 [FROZEN, formalization] | replace | V2.8 part (a) | ℰ ruled out for j :⟺ X_j('Acc(ℰ)') ≠ ∅ | :⟺ ∃α ∈ X_j('Acc(ℰ)') with Acc(ℰ) ∈ Uses(α) | "…no argument usable by j rules it out" → "…usable by j that reads its meeting (E)…" | none named (S28 with S41 Q23 in effect) |
| PB4.2 | D9.5 [B4: Expl Suff Nec] | weaken | – | Scope_j(u) :⟺ C_u ⊆ C_j(u) ∧ ℓ_u = ℓ_j(u) ∧ β_u = β_j(u) | Scope_j(u) :⟺ C_u ⊆ C_j(u) | L393.n2's gloss loses grain, boundary | none |
| PB4.3 | D9.3 [B4: Expl Suff Nec] | weaken | – | Prem(u) := children(u) (I89) | Prem(u) := the premises Form(u) uses | none | none |
| PB4.4 | L397.s13 [B4: Expl Suff Nec; formalized by D9.1, D9.7, D9.8], adds to Live_j / K2 (D9.4, D9.6 FROZEN) | strengthen | – | Live_j(d;u) | Live_j(d;u) ∧ (d ∈ Accepted_j(ξ) ⇒ HeldExpl_j(d)), HeldExpl_j(d) :⟺ ∃o ≺ ξ, e: Rep(o,e) ∧ concl(e) = d ∧ Acc(ℰ_e) | "the semantics does not require it" → "before a premise taken as given is used, the agent holds a represented explanation of it" | **S27**; S41 Q23 in effect |
| PB4.5 | L383.s1 (SC) [B4: –], changes with D9.10 [FROZEN, formalization] | strengthen | – | a criticism occurrence may have ¬Bearing | Occ_criticism(c) ⇒ Bearing(c,z,p) | "can exist when (K1) fails" → "exists only when (K1) holds" | none |
| PB4.6 | L385.s1, D9.11 (SC) [B4: –] | weaken | – | UsesReason requires an image port of m on an active route | that clause dropped | "…and lands on an active route" dropped | none |
| PB4.7 | L546.s1 (SC) [B4: –] | strengthen | – | list {finite monotone, (I2), (O1), (T2), (CT2), Arguments 1–3} | … Arguments 1–10 | "Arguments 1–3" → "Arguments 1–10" | none |
| PB4.8 | D10.1, L317.s1 [B4: –] | weaken | – | Prob_j(ℰ,ℰ′;p) :⟺ Riv ∧ NotOut_j(Acc ℰ) ∧ NotOut_j(Acc ℰ′) | Prob(ℰ,ℰ′;p) :⟺ Riv | "Two rivals, neither ruled out for an assessor, pose, for that assessor, a problem" → "Two rivals pose a problem for p" | S21 (per the reply); I37 |

| id | predicted meaning | predicted scope | claims | small cases (run?) | edges named | inventions |
|---|---|---|---|---|---|---|
| PB4.1 | Out_j takes the instance reading; defeat sets keep D16.XV's | four cases stay; the perpetual-motion design not ruled out for j | FC72 (d), FC72.new1 (c), (d) | FC72.new1 (c) run before: True for j, False for j0; after (not run): False for both | changes with D9.8; constrains D9.7, D9.1; moves Out_j → D10.1, D10.6 | Uses at the symbol (other: 'Acc' of any candidate); classical Incons (other: φ among α's symbols) |
| PB4.2 | K2's Scope drops ℓ, β | four cases stay; FC56 (a'') X_j 1/0 → 1/1 | FC56 (a'') | FC56 (a'') run before | changes with D9.6; constrains L524.s1 | which indices j declares (I42) |
| PB4.3 | K2's third conjunct over used premises | nothing expected to move | none | idle-child step (not run) | changes with D9.6, I89; constrains D9.2 | what a form "uses" |
| PB4.4 | K2 gains a conjunct | four cases stay as explanations; the myth not ruled out for j1; FC30.new1 (a) moves **on that reading** | FC72 (d), (f), FC72.new1 (a), (c), (d), FC53 (a), FC30.new1 (a) | myth, ¬PM (not run) | blocks L397.s10; constrains D12.5; moves X_j | HeldExpl (others: provenance Con; record leaves exempt) |
| PB4.5 | criticism typing | FC74's witness impossible | FC74, FC76 | FC74 (before run) | changes with D9.10, D14.x, (EX); constrains L383.s2 | occurrence typed with its allegation |
| PB4.6 | UsesReason widens | nothing | none of the 142 | Part A's e3.34b cited | changes with D9.11, B3's response items | route readings of e3.34b |
| PB4.7 | what would rule the class out widens | nothing | FC109 | – | constrains L534.s1; changes with FC109 | none |
| PB4.8 | Prob loses the assessor | FC72.new2 (c) j1: problem False → True | FC72.new2 (c), FC47.new1 | FC72.new2 (c) run before | changes with L317.s1, D10.4, D10.5; blocks D10.6 as written (not settled) | whether Prob keeps ξ |

B4's items not varied (reply §(e)): L315.s10, L315.s17 (S21), L389.s1, L375.s2, L517.s1. The reply states: "Candidate definitions of explanation thrown up: none new".

## 6. Flags (rule 4: recorded, not implemented)

| id | flag | why |
|---|---|---|
| **PB3.8** | no formal statement changes (S40: "every variant is maths or code") | the reply drops a sentence and states no change to D12.8 or anything else; nothing to compute; recorded as a change of the text's wording only |
| **PB4.4** | changes a FROZEN item beyond the formalization of the free words | L397.s13 is formalized by D9.1, D9.7, D9.8; the variant adds a conjunct to Live_j / K2 (D9.4, D9.6, FROZEN). **Its effect on what (Suff) and (Nec) read** (X_j) can be stated on D9.8, L397.s13's own formalization: X_j(φ) := {α : Usable_j(α) ∧ RO(α,φ) ∧ every premise of α taken as given has a held explanation}. That restatement is in scope and is left to rule 5 to implement as PB4.4′, recorded as the reader's |

Not flagged out, recorded:

- **Carry-overs repeated by design** (rule: class a computed; class b where taken up): PB1.1 = V1.7; PB1.2 = R2V1.9; PB1.3 = R2V1.8; PB1.4 = R2V1.7; PB1.5 = R2V1.4; PB2.1 = R2V2.7; PB3.1 = R2V2.4; PB4.1 = V2.8's part on L315.s7. None repeats a Part A variant that Part A computed (V1.7, V2.8's part and R2V2.7 were ruled to Part B uncomputed; the class-b ones were never implemented).
- **Same effect across sections**: PB2.6 (NonVacuous drops Stated, B2's D6.6) and PB1.1 (Stated always true, B1's D3.5) give the same (E); each is B's own item.
- **Neighbours of Part A work**: PB4.6 neighbours Part A's e3.34b (a reading of D11.4's routes, FROZEN here); PB4.6 varies D9.11 (free), so it is not a repeat. PB2.7 restores round 3's written-in test through (A) rather than through D6.7 (Part A's V2.4 put it back through D6.7, C6); a different item, the same axis.
- **Changing with a FROZEN formalization, allowed by the rule**: PB1.5 (D3.4), PB2.1 (D5.7; and D12.7's Viol, which the carry-over's own statement names), PB3.3 (D12.1), PB3.4 (D12.3), PB4.1 (D9.8), PB4.5 (D9.10).
- **Departs from an owner's decision by the reply's own account** (computed; candidate definitions flagged for Part C if the computation bears it out; rule 4): PB1.2 (S25–S27), PB2.5 (S45), PB2.7 (S45, S44), PB3.1 (S41 Q2), PB3.3 (S41 Q2 in part; S44, S41 Q15 on a selection history), PB3.4 (S41 Q2), PB3.5 (S41 Q2 in part), PB3.6 (S41 Q2 on that reading), PB4.8 (S21).
- **Prose**: none adds prose beyond the changed-sentence record (PB2.4's and PB2.7's added clauses are the records of the changed sentences). **Where values are placed**: none moves it.
- **Invention not implementable as written, to be recorded by rule 5**: PB1.2's Θ_admits of a bare edit (the program computes Θ for occurrences only); PB2.5's "background component that assigns an input" (the program has no input-assigning role mark); PB3.4's precedence Sel/Con on h∪; PB3.6's β.

## 7. Carry-overs

| carry-over | class | taken up by | computed? (rule 5) |
|---|---|---|---|
| V1.7 | a | PB1.1 | to compute (and PB2.6, the same effect) |
| V2.8's part on L315.s7 | a | PB4.1 | to compute |
| R2V2.7 | a | PB2.1 | to compute |
| R2V1.2 | b | **not taken up** (the reply: its clause is in B3's terms) | not computed (class b only where taken up) |
| R2V1.4 | b | PB1.5 | to compute |
| R2V1.7 | b | PB1.4 | to compute |
| R2V1.8 | b | PB1.3 | to compute |
| R2V1.9 | b | PB1.2 | to compute |
| R2V2.4 | b | PB3.1 | to compute |

## 8. Free items bearing on the explanation definition that no variant reached (from the template's marks)

| section | items bearing | reached | not reached |
|---|---|---|---|
| B1 | 27 | 9 | 18: L87.s1, L91.s1–s6, L93.s1, L99.s1, L105.s2, L105.s3, L137.s1, L143.s1, L147.s1, L147.s2, D1.1, D1.2, D3.7 (all bear on (E) and Dec) |
| B2 | 20 | 13 | 7: L245.s1, L245.s2, L245.s3 (Dec …), D5.2, D5.3, D6.1 ((E) …), D6.10 |
| B3 | 13 | 12 | 1: L169.s2 |
| B4 | 8 | 4 | 4: L315.s10, L315.s17, L389.s1, L397.s5 |

(B1 counts D4.3, D4.4 reached through PB1.9; B2 counts L249.s1 through PB2.4's D5.6 and L253.s1, L247.s1 through their changed-sentence records.) Each reply gives its reasons in its §(e); whether each reason holds is for rule 10, after the computation.

Written by one Opus 5.5 agent under rule 4 and decision S56, 29 September 2026. Nothing ruled (rule 3).
