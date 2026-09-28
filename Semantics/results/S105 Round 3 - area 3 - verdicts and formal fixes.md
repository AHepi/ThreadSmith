# S105: Round 3 — area 3 (L373–L632, Parts IX to XVI): verdicts and formal fixes

*Checker of area 3 under rule 5 of `results/S105 Round 3 - how the replies will be read, written before sending.md` (read whole first): a fresh Opus 5.5 agent that built nothing of this round, 28 September 2026. Findings: the 34 the tabulation assigns to area 3, each read whole in its `.response.txt` (breaker r1, r50–r81; maths_words r3, r32–r136; structure r3–r123; cases r3, r9–r22, r127–r138). Text under review `tests/104 … with the owner's answers.md` (md5 bc14045aae3139df710d8339a9c1c81b), not written. Maths `results/S104 Round 2 - maths after the reading/`, not written. Model copy `S105 Round 3 - maths after the reading/area 3 model/` (md5s checked at the copy). Runs `… area 3 - runs.txt`; text changes `… area 3 - text changes.json`. Decisions S20–S41 read; S23, S40, S41 bind every row.*

Codes: **M** holds against the maths (or the program); **W** against the words; **I** against an invention only; **N** does not hold. Rule 3: every model a reply marks "not run" was run before its row (runs file §3). Rule 10: arguments, not agreement among replies. Rule 15: quotations compared with text 104 (where a reply compares round-1 words, the row says so).

## 1. Verdicts

| # | finding | lines | v | why (one line) | fix |
|---|---|---|---|---|---|
| 1 | B-Q23n | L397 | W | L397 "usable by \(j\) when each of its steps is (K2)": a premise alone has no step, so the words make every premise usable by everyone; D9.6 (I166) asks \(d\in\operatorname{Accepted}_j\). FC72.new1 (a): for j0 who never took ¬PM up, the words rule design ∧ PM out, D9.6 does not; against L393 "a claim \(j\) has never taken up is not live for \(j\)" and L397 "not something the claim does by itself". Second half (no Form_j, Scope_j for a premise alone): N, L397 gives forms to steps and rules out by inconsistency | R3A3-T1 (formula; settles I166) |
| 2 | B-O4 | L397 | W | S41 Q23 "Yes, it's an argument": a premise alone stands in for the steps; FC72 (d), FC72.new1 (b): ¬PM alone, no step, rules out design ∧ PM | R3A3-T2 (delete) |
| 3 | B-O5 | L397 | W | "the argument has steps from it to what it rules out" is false of a premise alone (FC72.new1 (b)); what tells it from the denial is D9.7's block (RO ⟺ ¬φ no conjunct, 684 cases) | R3A3-T3 (B-O5's span) |
| 4 | B-O6 | S27, S28, L315, L317 | N | no clash: S27's "not enough … to do anything about it" is said of the conflict the bare claim triggers (Incons holds for every assessor); S28's ruling out is the person's taking the claim up (Out_j ⟺ ¬PM ∈ Accepted_j); Q23 makes that use an argument. FC72.new1 (c), (d) | none |
| 5 | A3-L375.1 | L375 | N | compares round-1 words ("reflexive closure", rule 15: not in text 104); L375 writes \(\preceq_h:=\prec_h^{*}\) = D11.3 | none |
| 6 | A3-L393.1 | L393 | N | round-1 words ("a step of the same argument"); L393 writes \(u'\in\operatorname{Below}(u)\) (D9.4) | none |
| 7 | A3-L393.2 | L393 | N | L393 now states the monotonicity the maths states (D9.8, FC70, FC56); the reply: "no case separates them" | none |
| 8 | A3-L395.1 | L395 | N | L395 writes D9.9 (i) with its leaf clause (second check R8): words = maths | none |
| 9 | W9 | L556 | N | "(K)" is L116's tag, D4.1, which is \(\operatorname{sig}_{\tau[C]}(k)\) read at τ[C]; "(D4.4)" covers \(\operatorname{sig}_C(\lambda(k))\); both signatures of the formula are pointed to | none |
| 10 | W8 | L558 | M | L558 cites FC18 for "adds nothing to (F1) on any contract"; FC18's status is CEX only through I94's untranslated reading, which L554 "up to the port translation" excludes (round 2, area 3 row 50); its D4.4 part holds (17,280 models) | F5 (FC18 restated); status CEX → H |
| 11 | A3-L574.1 | L574 | N | L574 writes the image condition; FC80 (d′) H; words = maths | none |
| 12 | A3-L590.1 | L590 | N | L590 lists 𝒬 among the ports (FC97 H); words = maths | none |
| 13 | A3-L626.1 | L626 | N | L626 writes \(w\le L_{\mathrm{occ}}\) as the hypothesis (FC102 (b″)); words = maths; L622's "recent" is what the bound fixes | none |
| 14 | W6 | L481, L195 | W | L195 "a survival condition requiring fidelity on \(H\)", L481 "enacted by the environment"; D12.1 sets the condition to fidelity alone. FC80.new1 (a): two members faithful on H, the environment's condition keeps one; D12.1 selects both | F2 (D12.1 surv); code sel(env); FC80.new1 (b): L574's step holds for any condition on H |
| 15 | W7 | L405, L205 | W | by L205 "represents" is (R); L405's "represented organization" read so gives L526 a cycle (U, FC98 (a)) or no first representation (K, FC98 (d)), against L405 "A first representation may be constructed"; D13.3 reads Held (I162, the only cut meeting both) | R3A3-T4 (formula; settles I162 for Build) |
| 16 | W-O4 | L397 | W | as row 2 | R3A3-T2 |
| 17 | W-O5 | L397 | W | as row 3; W-O5's formula adds "is not a conjunct of" (S40): not taken | R3A3-T3 |
| 18 | W-O6 | S27, S28 | N | as row 4. Its argument against the orchestrator's reading holds in part: S28's "yes" and L315 ("ruling the candidate out by χ is already doing something about it") make ruling out a doing; the reading's "not the same act as doing something about the conflict" should say: not the same act as repairing it | none (note §6) |
| 19 | S1 | L526, L375 | M | D11.3 asks acyclic only; on an infinite descending chain below o_t the T′ equations have **no** fixed point (FC98.new2 (a): S1's {o_1}, {o_2} fail at o_2, o_3; every finite R fails; an infinite R fails); L526 "no endless descent", L193 "exactly one" fail there. S1's witness (two fixed points) is wrong; its conclusion holds | F1 (D11.3 well founded; = area 1 F1); R3A3-T5 (formula; settles R3A3-01) |
| 20 | S2(i) | L526 | M | D18.1: "Nodes: the symbols defined in §§1–16"; the program's DEP had 28 nodes; FC98 (b)'s sink check saw a subgraph | F6 (DEP 82 nodes; every paragraph of §§1–16 mapped: FC32.new1 (a)) |
| 21 | S2(ii) | L526 | M | DEP["Sel"] lacked Faithful_H (→ (F1), (F2)) and ¬CT (→ CT) | F6; FC32.new1 (b): no cycle under K, T, T′ with them |
| 22 | S2(iii) | L526, L405 | M | L526 "Build depends on histories, Ownership and (E)"; D13.3's only route to (E) is ExplUse, a primitive (I148): Build ⇝ (E) false (FC32.new1 (d)). P5 (Acc on c's organization) not taken: no contract could then be built (FC90.new1 (b); L425, L588) | F3 (ExplUse through the claim 'Acc(ℰ)', R3A3-05) |
| 23 | S3 | L526 | M | "(K3) on (K2)": no (K3) node | F6; FC32.new1 (d): (K3) ⇝ (K2) |
| 24 | S-b | L522, L31 | M | D0.2 claims to list the symbols the core uses and neither defines nor lists; the graph's sinks show 12 it lacks (FC32.new1 (c)). h(t), o_t (D12.1, I53, I128), cod t (D5.1's codomain), val_r, ⇝_R (Org_ℓ(h)), Exec (Θ's), "output of h′" (Prepares) are defined or listed | F7 (D0.2 extended, computed list); not counted |
| 25 | S-e-letters | L395 and others | N | each letter is bound where it is used; no definition or claim reads one use as another (DEP keeps "K" and "(K)" apart); no renaming given | none |
| 26 | S-e-represented | L405 | W | as row 15 (the L405 use); the D11.4 and D13.8 uses ("represented input", "represented failure") change no computed result; none proposed | R3A3-T4 |
| 27 | S-e-Acc | L449 | M | D14.7 applies Acc to four data; D6.7 needs δ_E (D5.3, I20). FC90.new1 (c): the pole's forward candidate meets (E) with δ_E = L, not with δ_E = H | F4 (D14.7 ∃δ_c); L449 unchanged: the text's candidate (L231) has no designation; δ is I20 (rule 6) |
| 28 | S-O4 | L397 | W | as row 2 | R3A3-T2 |
| 29 | S-O5 | L397 | W | as row 3; S-O5's pointer "(D9.2)" not taken: D9.2 does not state the difference, D9.7 does, and the next sentence carries it | R3A3-T3 |
| 30 | S-O6 | S27 | N | as row 4 | none |
| 31 | K4 | L620–L630 | M | E9's layers were not built: FC102 (a), (c), FC103 (a)–(c) NOT TESTED; the text's conclusions rested on other claims | code: e9.py; FC102.new1, FC103.new1 computed as claimed (runs §3) |
| 32 | C-O4 | L397 | W | as row 2 | R3A3-T2 |
| 33 | C-O5 | L397 | W | as row 3; the whole-sentence delete not taken: its remainder "it finds that the candidate gives what the premise excludes" is D9.7's difference and meets Q23 | R3A3-T3 |
| 34 | C-O6 | S27, S28 | N | as row 4 | none |

**Counts.** M 9 (rows 10, 19–24, 27, 31; 20, 21, 23 one fix); W 12 (rows 1–3, 14–17, 26, 28, 29, 32, 33; row 1's second half N); I 0; N 13 (rows 4–9, 11–13, 18, 25, 30, 34). 34 in all.

## 2. Formal fixes (old → new; ids kept)

| fix | item | old | new | finding | settles / invention |
|---|---|---|---|---|---|
| F1 | D11.3 | ≺_h acyclic | ≺_h well founded: ∀X ⊆ O_h [X ≠ ∅ ⇒ ∃x ∈ X ∀y ∈ X ¬ y ≺_h x] (so acyclic, no infinite descending chain). D18.1: "unique where ≺_h is well founded below o_t (every finite history)" → "unique (D11.3)" | S1 | = area 1 F1 (B3); counted once there; R3A3-01 = R3A1-03 |
| F2 | D12.1 | Faithful_H(t) (D5.7), i.e. t survives on H | surv(t, H) :⟺ Faithful_H(t) ∧ Env_{h(t)}(value_t\|_H), Env_{h(t)} the further requirement on t's values at the pairs of H that the environment enacts in h(t) (L481; read through Θ; none given: Env ≡ ⊤); t survives on H :⟺ t ∈ 𝒯 ∧ surv(t, H). D12.9's and D15.8's "surviving on H", "the survival condition" := surv | W6 | R3A3-03 |
| F3 | D13.3 | ExplUse(o, c) [I148], a primitive (D0.2) | ExplUse(o, c) :⟺ UsesClaim(o, 'Acc(ℰ)') for some ℰ = (E, p, t, Γ, δ_E) with c ∈ {E, t, C_p} (L425); UsesClaim read through Θ; the claim need not hold. D0.2: ExplUse out, UsesClaim in | S2(iii) | R3A3-05 |
| F4 | D14.7 | ∃c, p_c, e_c, t_c, Γ_c (… ∧ Acc(c, p_c, t_c, Γ_c) ∧ …) | ∃c, p_c, e_c, t_c, Γ_c, δ_c (… ∧ Acc((c, p_c, t_c, Γ_c, δ_c)) ∧ …), δ_c the designation of Q in c (D5.3, I20) | S-e-Acc | R3A3-07 |
| F5 | FC18 | status CEX: parts D4.4 reading (H), I94 untranslated reading (CEX) | FC18 := F1_C ⇒ SameKind_C with the counterpart read up to the port translation (D4.4; L554); I94's search kept as a look (its counterexample printed); status H | W8 | — |
| F6 | D18.1 (the program's DEP) | 28 nodes; Sel → h, Θ, staged (R); no (S), (B), (D), (K3), Result, Episode, Scr, RC, UU, UC | 82 nodes; every paragraph D1.1–D16.XV a node or folded into one (D_TO_NODE); Sel → (F1), (F2), CT, 𝒯pop, surv, Occurs, staged (R); Con → CT, Episode; Build → ExplUse → (E); (K3) → Out, (K2), RO; "one edge set" computed (FC32.new1) | S2(i), S2(ii), S3 | R3A3-08 |
| F7 | D0.2 | the list after round 2 | + C_I, J_p, 𝒱, the stated construction, Desc (declared inputs L522 does not list); surv, UsesClaim, 𝔓^adv_Θ, trans (read through Θ); parts, Event, Expl (defined); "immediately after" (area 1 F9); − ExplUse (F3) | S-b | not counted (register) |

## 3. Code (in `area 3 model/`)

| file | change | fix |
|---|---|---|
| model/claims_b.py | DEP extended, DEP_R2 kept; D_TO_NODE; D0_2, D0_2_R3A3; DEP_EXPLUSE_PRIMITIVE; dep_edges, dep_cycle take a graph and `through`; FC98 (a) the cycle through (R), (b) sinks against D0.2 | F6, F7, F3 |
| model/claims_b.py | sel(…, env=None): Env on t's values at H; None = D12.1 after round 2 | F2 |
| model/claims_a.py | FC18's I94 part a look | F5 |
| model/claims_r3a3.py (new) | FC98.new2 (S1), FC72.new1 (B-Q23n, O4–O6), FC80.new1 (W6), FC32.new1 (S2, S3, S-b), FC90.new1 (S2(iii), S-e-Acc), FC102.new1, FC103.new1 (K4) | all |
| model/e9.py (new) | E9: P, S1, S0, t1, t1∘ψ, t0 (R3A3-09) | K4 |
| model/run.py | imports claims_r3a3 | — |

Whole suite (runs §1, §4; PYTHONHASHSEED=0, scale 4, cap 45): baseline 105 H, 3 CEX, 7 NT of 115 → after area 3 113 H, 2 CEX (FC23, FC63), 7 NT of 122. Changed: FC18 (CEX → H) and FC98's printed cycle and sink list; 7 new claims, each H; every other claim identical line by line. `s104_external.py`, `s104_creative_transport.py`: output identical.

## 4. Text changes (`area 3 - text changes.json`; words outside formulas 40 → 7, the 7 all kept from the old spans or T5's pointer "D11.3"; no new word; spans checked by program: each occurs once in its line, T1–T3 do not overlap)

| id | line | kind | old → new | finding | settles |
|---|---|---|---|---|---|
| R3A3-T1 | L397 | formal | "An argument is usable by \(j\) when each of its steps is (K2) (D9.6)" → "An argument \(\alpha\) is usable by \(j\) when \(\forall u\in\operatorname{steps}(\alpha)\ \operatorname{Usable}_j(u)\land[\operatorname{steps}(\alpha)=\varnothing\Rightarrow\operatorname{concl}(\alpha)\in\operatorname{Accepted}_j(\xi)]\) (D9.6)" | B-Q23n | I166 |
| R3A3-T2 | L397 | delete | "What a stated premise cannot do is stand in for the steps. " | O4 (×4) | — |
| R3A3-T3 | L397 | delete | " in that the argument has steps from it to what it rules out" | O5 (×4) | — |
| R3A3-T4 | L405 | formal | "a represented organization" → "\(\operatorname{Held}_\ell(o,c)\) (D13.3, D18.1)" | W7, S-e-represented | I162 (Build) |
| R3A3-T5 | L375 | formal | "(\(\preceq_h\,:=\,\prec_h^{*}\))" → "(\(\preceq_h\,:=\,\prec_h^{*}\); \(\forall X\subseteq h\,[X\neq\varnothing\Rightarrow\exists x\in X\,\forall y\in X\,\neg\,y\prec_h x]\), D11.3)" | S1 | R3A3-01 |

Rule 6, in so many words: the text should now settle I166 at L397 (the words without it contradict L393 and L397's "not something the claim does by itself": FC72.new1 (a)); I162 at L405 (every other cut contradicts L405 or L526: FC98 (a), (d)); well-foundedness at L375 (without it L195's formula, L208 and L193 have no value on an admitted history: FC98.new2 (a)).

## 5. Inventions (provisional ids; numbered at integration after I166)

| id | fills | choice | other choices | why this one | used by |
|---|---|---|---|---|---|
| R3A3-01 | "acyclic causal precedence" (L375) under L195's staged formula | ≺_h well founded | acyclic only (FC98.new2 (a): no fixed point); well founded below o_t only | L526 "no endless descent"; L193 "exactly one"; = R3A1-03 | D11.3, D18.1; T5 |
| R3A3-03 | "a survival condition requiring fidelity on \(H\)" (L195), "enacted by the environment" (L481) | Faithful_H ∧ Env on t's values at H, Env through Θ | fidelity alone (round 2, unregistered: FC80.new1 (a)); any condition on t (L574's step then need not hold) | L195 "requiring", L481, L574 "Survival on \(H\) constrains only" values at H (FC80.new1 (b)) | D12.1, D12.9, D15.8 |
| R3A3-05 | "for explanatory use of \(c\)" (L405) | o uses the claim 'Acc(ℰ)', c ℰ's organization, transport or contract; the claim need not hold | primitive (I148: L526's "(E)" unbacked); organization only (P5: no contract built, against L425); the claim must hold (ℰ_rev not built, (EX)'s Account idle, against L403) | L526, L425, L449, L403; FC90.new1 (a), (b) | D13.3, D0.2 |
| R3A3-06 | L526's grouped subjects ("(N), (G) depend on Deploy and Build"; "(P), (EX) depend on (G), (E), Deploy") | read together | each alone: New on Build, (P) on (G), (E), Deploy are then false (FC32.new1 (d)) | the definitions (D13.5, D14.2); found by the checker, no reply raised it; recorded, no move | FC32.new1 |
| R3A3-07 | (EX)'s candidate data (L449) | δ_c quantified with c, p_c, t_c, Γ_c | supplied with c (as D9.10) | (EX) quantifies the rest | D14.7 |
| R3A3-08 | D18.1's nodes | the folds of D_TO_NODE; D0.2's classes (C_I, J_p, 𝒱, the stated construction, Desc as declared inputs L522 does not list) | a node per paragraph | a record of the graph; L522's list is not changed (new items would be prose) | DEP, D0.2 |
| R3A3-09 | E9's instance (L620–L630) | 4 cells, frames 0..3, two things; occlusion of cells 1–2 at t = 1, 2 shows nothing (L624); edits on the initial frame; S0 window 2, its predictor components indexed by its own pair, λ = the whole of P on those frames; B0 the initial states on which H0's windows never conflict ("It is faithful on \(H_0\)"); t0 keeps the frame where H0 is silent | edits at t = 1 (not computed); occluded cells a third value | L622, L624, L626; the smallest instance with an occlusion of L_occ = w = 2 | e9.py; FC102.new1, FC103.new1 |

Settled by text changes: I166 (T1), I162 for Build (T4), R3A3-01 (T5). Ids R3A3-02 and R3A3-04 are not used (the settling of I166 and of I162 is no new invention); the program's labels keep the ids above.

## 6. Owner questions

None. O6: the clash is not real (row 4; FC72.new1 (c), (d)); nothing the owner's words leave open. The orchestrator's reading of O6 stays a reading; W-O6's correction recorded: S27's "not enough" is said of the conflict (the bare claim); S28's "yes" makes the ruling out a doing (L315); what it is not is a repair (L315, D12.8, D14.2).

## 7. Parked

None: no finding concerns what hard to vary covers (S33, S34) or where values are placed.

## 8. Moves (rule 16, strict) and pairs for the integrator

| | items | n |
|---|---|---|
| formal | F2 (D12.1), F3 (D13.3), F4 (D14.7), F5 (FC18), F6 (the program's D18.1) | 5 |
| text | R3A3-T1 … T5 | 5 |
| **moves** | | **10** |

Not counted: F1 (= area 1 F1, counted there); F7 (D0.2's list); inventions R3A3-01…09; new test claims FC98.new2, FC72.new1, FC80.new1, FC32.new1, FC90.new1, FC102.new1, FC103.new1; the re-based D12.9, D15.8, D18.1 phrases.

Pairs that bear on one another: F1 = area 1 F1 (B3), T5 writes it at L375; F2 and area 1 F2, F5 (all change D12.1; area 1 F6 types surv as a content, which F2's Env keeps); code: sel(env) here and sel(h_nonempty) in area 1; T4 (Held at L405) and area 1 F7 (Held with D12.5's extent) and K2 (area 1: L411 unchanged); F7 and area 1 F9 ("immediately after"); T1–T3 are one line (L397), no overlap.
