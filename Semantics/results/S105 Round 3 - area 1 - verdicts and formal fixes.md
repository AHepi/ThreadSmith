# S105 Round 3 - area 1 (L1-L228, Parts 0 to IV): verdicts and formal fixes

*Checker of area 1 under rule 5 of `results/S105 Round 3 - how the replies will be read, written before sending.md` (read whole first): a fresh Opus 5.5 agent that built nothing of this round, 28 September 2026. Findings: the 41 the tabulation assigns to area 1, each read whole in its `.response.txt` (breaker r5-r81, maths_words r12-r136, structure r24-r119, cases r40-r136). Text under review: `tests/104 … with the owner's answers.md` (md5 bc14045aae3139df710d8339a9c1c81b), not written. Maths: `results/S104 Round 2 - maths after the reading/` (not written). Model copy: `S105 Round 3 - maths after the reading/area 1 model/` (copied from `model after round 2/`, md5s checked). Runs: `… area 1 - runs.txt`. Text changes: `… area 1 - text changes.json`. Decisions S20-S41 read; S23, S40, S41 bind every row.*

Codes: **M** holds against the maths (or the program); **W** holds against the words; **I** against an invention only; **N** does not hold. Rule 3: every model a reply marks "not run" was run before its row was written (runs file). Rule 10: rows rule on arguments; agreement among replies counts for nothing.

## 1. Verdicts (one row per finding)

| # | finding | lines | v | why (one line) | fix: maths / code / text |
|---|---|---|---|---|---|
| 1 | B1 | L193, L211 | M | D12.1's "o_t the occurrence at which t is held, h(t) the one history of t" presupposes one holding; a transport held at o1 (selected) and again at o3 (a record of o1, or prepared anew by o2's trace) has two; L211 makes provenance a carrier's | D12.1 per holding (F2), D12.3′ (F3); FC12.new2 (a), (b): o1 Sel, o3 Sel (record) or Con (re-prepared) under K, T, T′ (U: no fixed point for a selection). B1's fix (Con blocked by an earlier Sel holding) not taken: FC12.new2 (b), (c) give Dec for a re-construction and for FC98 (d)'s case, against L201 "Construction may operate on selected material" and L405 "Reconstruction by a learner is construction" |
| 2 | B2 | L201 | M | "prepares t" (I56) read transitively makes t constructed when a trace built only a part of the population it was selected from: FC12.new3, exact Sel, transitive Con (T, T′); L405 "the rest of the content keeps its inherited provenance" fixes the exact reading | D12.2 CT exact (F4); R3A1-02 |
| 3 | B3 | L193 (L526) | M | D11.3 asks ≺_h acyclic only; on an infinite descending chain below o_t the T′ equations have no fixed point (FC98.new1 (a): each truncation's one fixed point puts Rep at the deepest occurrence only, limit ∅, no fixed point; every R within depth 10 fails); L526 "The order has no cycle and no endless descent" | D11.3 well founded (F1); FC98.new1 (b): one fixed point on every finite partial order ≤ 3 occurrences (9,928); R3A1-03 |
| 4 | B4 | L195, L208 | N | L195's formula excludes Rep at o ≺_{h(t)} o_t, strict: the staged exclusion; U is the reading that puts o_t in its own history | none; FC98.new1 (c): strict exclusion, one fixed point, output Sel (K, T, T′); U none |
| 5 | B5 | L195 | M | D12.5 types Rep on contents; D12.1 applies it to H and the survival condition; D13.6 already makes transports and contracts contents by L590, and H ⊆ A × B is a contract's kind of set | D11.2′ (F6); FC97.new1 (construction); B5's other choice (drop H, surv) would contradict L195's own formula; R3A1-04 |
| 6 | B6 | L151, L105 | M | "the observed value g takes on Sol_D(a,b)" presupposes one value; L105 "Several solutions remain several" | D3.3 obs (F8): the single value or ⊥, ≠ as D6.4 (owner S41, Q15). FC28.new2: still/north Ident (⊥ ≠ n); still/gusty not (⊥ = ⊥); B6's image reading also calls still/gusty identification though the fibre query answers ⊥ at both its pairs; the singleton reading excludes the weathervane; the pole's C_id alike under all three. R3A1-06 |
| 7 | B7 | L151, L325 | N | L151 carries I163's formula (R4-L151); "edits to the observed value" is round 1's wording, not in the text (rule 15); the source of variation is what the formula says | none; B7's FC28.new1 run (FC28.new1 (a)): yes on C_id, settings of H, settings of L |
| 8 | B8 | L17, L195 | M | Main claim does not hold: the student's copy has the source holding E before the student's holding and no trace, so Sel is excluded by D12.1's cod t clause and Dec(t) holds (FC30.new1 (d): U, T, T′; K, rejected in round 2, leaves the source unrepresented). Two parts hold: FC30.new1 (a)'s Dec witness is `admitted=False`, not the example; and with H = ∅, Sel(t;{t},id,∅) ⟺ Hom(τ) (FC77), so a link no pair tried and nobody worked out is selected and Q2's condition misses it (FC30.new1 (e)); S41's question: "simply declared, not found by trial or worked out"; L13: "produced by variation and survival on a history of encountered changes" | D12.1 H ≠ ∅ (F5; I52's registered other choice); FC77 restated; FC30.new1 (d), (e). B8's fix (survival condition enacted by the environment) not taken: D15.8 already says it, and survival on ∅ stays vacuous whatever enacts it (FC77 parts 2, 3). Not parked P1 or P2: no strength ordering of survival conditions and no competitor in 𝒯 is asked. R3A1-05 |
| 9 | B9 | L55 | M | D13.8's "o′ immediately after o in h′" has no definition (D11.3 gives ≺, ⪯ only). q(o) a function: D13.8's "the contract operative at o"; L55's one change C → C′ | D13.8 covering relation (F9); FC84.new2 (a): = every ordered pair under D13.8's Rec_h′(ρ_{q(o′)}), 103,668 cases; (c): = the program's `episode` on chains. R3A1-07 |
| 10 | B-e6 | L211 (D12.4) | M | a record's own history gives it a provenance D12.4 does not: FC12.new2 (a) record of a selected carrier Dec by D12.1-D12.3, Sel by D12.4; (d′) record of a declared carrier Sel. L211: "a later record made from the carrier carries that provenance, not a second, independent one" | D12.3′ (F3); FC12.new2 (d): one fixed point, every record = its source, 1,768 chains (T′). With R3A1-01 |
| 11 | B-e7 | L195 | N | T9 wrote I161 into L195 under rule 6: the second check's ruling settled it there in so many words; the case B-e7 says it runs out on is B1's (row 1) | none |
| 12 | B-O1 | L61 | W | L61 says the four conditions of Account suffice; Q2 "No, not if just declared"; D16.XV's (Suff) has ¬Dec(t) | R3A1-T1. "Rests on B8": no; Dec reaches the example without B8's fix (row 8) |
| 13 | W-O1 | L61 | W | as row 12 | R3A1-T1; W-O1's "(Nec) their" → "its" not taken: a word change outside the three kinds (S40); "their" reads as the formula's conditions, since Expl ⇒ Acc (Nec) and Acc ∧ Dec ⇒ ¬Expl (Q2) give Expl ⇒ Acc ∧ ¬Dec |
| 14 | S-O1 | L61 | W | as row 12 | R3A1-T1 (the same span) |
| 15 | C-O1 | L61 | W | as row 12 | R3A1-T1 (the same span) |
| 16 | B-O2 | L49 | W | L49: mathematics explains when its components respond as the target does; that is less than Account and says nothing of Dec (Q2) | R3A1-T2: formula, no new word. B-O2's span adds "it meets", "on its question and contract" (S40, not taken) |
| 17 | W-O2 | L49 | W | as row 16 | R3A1-T2; W-O2's added words (S40) and "(Part V)" not taken: Part VII holds the exact constructions, mathematics among them |
| 18 | S-O2 | L49 | W | as row 16 | R3A1-T2; "holds of it" not taken (S40) |
| 19 | C-O2 | L49 | W | as row 16 | R3A1-T2; C-O2's added words not taken (S40) |
| 20 | B-O3 | L69 | W | L69: "Explanation" in the commitment means meeting Account; Q2 | R3A1-T3 (delete "an account, ", so "account" keeps its one sense, Acc, as at L43, L159 and L69's own "whether an account is easy to vary") and R3A1-T4 (the replies' formula) |
| 21 | W-O3 | L69 | W | as row 20 | R3A1-T3, R3A1-T4 |
| 22 | S-O3 | L69 | W | as row 20 | R3A1-T3, R3A1-T4 |
| 23 | C-O3 | L69 | W | as row 20 | R3A1-T3, R3A1-T4 |
| 24 | T5 | L127 | N | L127 as written: "functions of (D,C) (D4.6, FC13)"; the witness (equal sig_C, Causal differing through Set_{o_j} read from A) is what that says; the compared words ("patterns in (K)") are round 1's (rule 15) | none |
| 25 | T6 | L127 | N | compares round-1 words ("change the part and the reading follows"), not in the text; round 2 dropped them because (K) cannot record them (FC08); L124 asks invariance and variability only, as D4.6 | none |
| 26 | T8 | L151 | N | compares round-1 words; the witness needs Q′ ≠ Q with one function, but Q is an operation (D3.2), so equal functions are one Q and p = p′ (D3.7) | none |
| 27 | R4-L151 | L151 | N | L151 writes I163's formula; C_id (L325) needs it (FC28, R4 part); the compared words are round 1's | none |
| 28 | T9 | L195 | N | L195 is T9's formula; the cod t exclusion (L13 "with no represented target in that history") and ¬CT (second check R1, rule 6) were ruled in round 2; the compared words are round 1's | none |
| 29 | W1/W2 | L220, L189 | W | L220's "fidelity" is read narrow or wide (L245 "Together they are fidelity" of (F1), (F2); L247 heads (A) "Question fidelity"); round 2 ruled narrow (Q11: L189, I50) yet D5.7 still lists L220 open. FC104.new1: (a) F1, F2eq at a pair, (A) failing (δ_E = θ); (b) under the wide extent a selected transport is violated at a pair of its own history, so D12.7's Sel ∧ Viol(a,b) ⇒ (a,b) ∉ H (L221) holds only narrow | D5.7 (F11); R3A1-T5 (W2's formula; settles FC104 at L220, rule 6) |
| 30 | S-fQ2 | L17 | M | with row 3: on an admitted infinite history Dec(t), and so L17's defeat condition, has no value | F1 (D11.3); FC98.new1 (a), (b) |
| 31 | S-c | L109-L179 | N | a definition no claim uses is no defect; the reply says each formalizes a line; the D10.3/FC47 cross-pointer is area 2's (L317) and a note | none |
| 32 | S-D1 | L123, L127 | M | D4.6 "o_j is the port j assigns" singular; I124 (registered: the ports j assigns, a union) and `core.Roles.set_oj` take the union. FC13.new1 (P8 run): asg(v) = asg(w) = k, D4.6's o_k has no value, the program computes Causal_C(k) | D4.6 O_j (F10, P2); program unchanged (already so) |
| 33 | S-D2 | L195, L197 | M | (i) Rep, Held applied outside their type: as row 5; (ii) Held names no contract (D18.1 "∃t Faithful(t: Org_ℓ(o′) → c)"), where (R) at L205 has "faithful on c's contract" | D11.2′ (F6); D18.1 Held with D12.5's extent (F7), so Rep ⇒ Held (FC98.new1 (b): Rep ⊆ Held on every case). P3's record reading ("no record leaf is MadeFrom H or surv") not taken: it replaces "represents" (L195's formula) by "a record made from" |
| 34 | S-e-primed | L109-L220 | M | claims cite D2.1′ (FC02), D2.4′, D4.6′ (FC07), D3.3′ (FC28, FC36), D12.1′ (FC78, FC81-FC83), D12.7′ (FC81), D12.8′ (FC82, FC83), D18.1′ (FC32); the core holds them unprimed (replaced in place in round 2) | re-base the ids to D2.1, D2.4, D3.3, D4.6, D12.1, D12.7, D12.8, D18.1 in the claims after round 3 (editorial; not a move, rule 16) |
| 35 | S-fQ6 | L55 | M | as row 9 | F9 (B9's covering form). P4 as written ("for every o, o′ ∈ h′", unordered) not taken: it also asks a record of the first contract (FC84.new2 (b): chain C → C′, ρ_{C′} recorded: covering episode, P4 not) |
| 36 | C-CT8a | L193-L199, L13 | N | the count (R4 moved by D12.1′'s cod t ban, R5 by I161) concerns the brief, not the maths or the text; the residue C01 was ruled in round 2 (Q14: "constructed if a trace prepares t, else declared"); after K1, R5 is constructed. With Q2, R4 (target represented, no trace) is declared: L199 makes declared = neither, L35 puts the body over L13's gloss, and S41's "not found by trial or worked out" is, in the text's terms, ¬Sel ∧ ¬Con | none |
| 37 | K1 | L197 | M | CT8 computed Con from (R)-tags after D12.2 was read as Held (T′, I162): the program disagrees with D12.2 | code: CT8 prints a T′ line (Held computed at the output, Sel's other conditions computed): R1, R3, R5 constructed; R2, R4 neither (was: R5 neither) |
| 38 | K2 | L201; L411 | W | L201 "a selected transport has no represented target and no criticism in its history; a constructed one has both": D12.1, D12.2 ask no criticism (§12 Vague note, second check R1); Con with no criticism: FC84.new1 (a) (the owner's bridge), N2 run (T′: o2 Con). L411 "a constructed one does": under T′ Con's represented target is Held at o′ ⪯ o_t, which N2's history has at o2: holds, no change | R3A1-T6 (pointer at L201); none at L411 |
| 39 | K3 | L17, L211 | N | D12.4's part is "each component with its counterpart binding"; the student declared the bindings, so no part is a transfer and each is Dec, as the whole t is; D16.XV's Dec(t) is D12.3's (FC30.new1 (f)); K3's Con per part reads a part as the component alone | none |
| 40 | K5 | L193, L195 | N | N1 run (FC12.new2 (e)): tags give Dec (the superseded reading, row 37); T′ with Held computed gives Con; I161 was settled at L195 by a ruling (rule 6) | none |
| 41 | N3 | L151 | N | no defect claimed; run (FC28.new1 (b)): Ident no under I163 (obs 1 at both pairs), yes under round 1's wording; L151 carries I163's formula | none |

**Counts.** M 14 (rows 1, 2, 3, 5, 6, 8, 9, 10, 30, 32, 33, 34, 35, 37); W 14 (rows 12-23, 29, 38); I 0; N 13 (rows 4, 7, 11, 24-28, 31, 36, 39, 40, 41).

## 2. Formal fixes (old → new; ids kept)

| fix | item | old | new | answers | settles / invention |
|---|---|---|---|---|---|
| F1 | D11.3 | h = (O_h, ≺_h, I_h): O_h ⊆ Occ; ≺_h acyclic; ⪯_h := ≺_h* | …; ≺_h well founded: every nonempty X ⊆ O_h has a ≺_h-minimal member (so acyclic, no infinite descending chain); ⪯_h := ≺_h*. D18.1: "unique where ≺_h is well founded below o_t (every finite history)" → "unique (D11.3)" | B3, S-fQ2 | L526; R3A1-03 |
| F2 | D12.1 | o_t the occurrence at which t is held, h(t) the one history of t, its preparing episode included [I52, I53, I128, I162] | Sel, Con, Dec are of a holding (t, o_t), o_t an occurrence at which t is held; h(t) := h(t, o_t), the history that produced that holding, its preparing episode included (I128, per holding). D12.7's "t's one history" and D12.8 re-based to h(t, o_t) | B1 | L211; R3A1-01 |
| F3 | D12.3 | Dec(t) :⟺ no parameters give Sel(t; ·) and none give Con(t; ·); Sel and Con read on h(t) | D12.3′: a holding (t, o′) reached from a holding (t, o) by a composition of content-preserving transfers (relay, record; TransferComposite, D13.3) has prov(t, o′) := prov(t, o), part by part (D12.4); for every other holding, Dec(t, o_t) :⟺ no parameters give Sel(t; ·) and none give Con(t; ·), both on h(t, o_t) | B-e6, B1 | L211 over I53/I54's clash; R3A1-01 |
| F4 | D12.2 | CT(h′, t) :⟺ h′ has a construction trace (D13.3) that prepares t | CT(h′, t) :⟺ t is held at an output o of a construction trace of h′ (D13.3: Prepares(h′, o, ·)); a transport assembled later from a trace's outputs is not thereby prepared by it | B2 | L405, L201; I56 for CT; R3A1-02 |
| F5 | D12.1 | H ⊆ C finite, its pairs having occurred in h(t) (D11.5) | H ⊆ C finite and nonempty, its pairs having occurred in h(t) (D11.5) | B8 | Q2 (S41), L13, L195 "survived"; I52's other choice; R3A1-05 |
| F6 | D11.2 | c = (E_c, C_c, Γ_c): an organization, a contract on it, and its commitments [I48] | … A transport or a contract (D13.6, L590), a finite H ⊆ A × B, and the survival condition Faithful_H over 𝒯 are contents by L590's construction (a membership port per pair, a survival port per member of 𝒯, one component fixing them, settings as edits); so Rep(o, x), Held(o, x) for x ∈ {t, H, surv, cod t} are typed as D12.5 types Rep | B5, S-D2 | R3A1-04 |
| F7 | D18.1 Held | Held_ℓ(o′, c) :⟺ ∃t Faithful(t: Org_ℓ(o′) → c) (through Θ, no provenance) | Held_ℓ(o′, c) :⟺ ∃t: Org_ℓ(o′) → E_c faithful (D5.7) on {(a,b) : (τ(a),σ(b)) ∈ C_c} with Γ_c active (D12.5's extent), no provenance; so Rep_ℓ ⇒ Held_ℓ | S-D2 | (R) at L205 |
| F8 | D3.3 | obs(a,b) the observed value g takes on Sol_D(a,b) | obs(a,b) := the one value of g on Sol_D(a,b) if there is one, ⊥ otherwise; ≠ in X_g ∪ {⊥}, ⊥ ≠ x, ⊥ = ⊥ (as D3.2, D6.4) | B6 | Q15's convention (S41); R3A1-06 |
| F9 | D13.8 | "o′ immediately after o in h′" (undefined) | o′ immediately after o in h′ :⟺ o ≺⁺_{h′} o′ ∧ ¬∃o″ ∈ h′ (o ≺⁺_{h′} o″ ≺⁺_{h′} o′), ≺⁺_{h′} the transitive closure of ≺_h on h′ | B9, S-fQ6 | R3A1-07 |
| F10 | D4.6 | o_j is the port j assigns (asg(o_j) = j) [I04, I124]; Causal_C(j) :⟺ Changes_C(j, Set_{o_j}) ∧ Inv_C(j, Obs) | O_j := {v : asg(v) = j}; Set_{O_j} := ∪_{v ∈ O_j} Set_v [I04, I124]; Causal_C(j) :⟺ Changes_C(j, Set_{O_j}) ∧ Inv_C(j, Obs) | S-D1 | I124 as registered |
| F11 | D5.7 | Fid⁺_C := F1_C ∧ F2_C ∧ A_C only where L220 or L630 is read so (FC104) | … only where L630 is read so (FC104); L220's "fidelity" is the narrow extent, Viol of D12.7 (Q11, round 2; L189; L247 names (A) apart); Sel ∧ Viol(a,b) ⇒ (a,b) ∉ H holds only so (FC104.new1 (b)) | W1/W2 | FC104 at L220 |
| F12 | program | CT8 (s104_creative_transport.py): Con from (R)-tags | CT8 adds Con under T′ (D12.2): trace ∧ Held at an occurrence of the episode up to t's holding, Held computed at the output | K1 | — |
| — | claims | FC02, FC07, FC28, FC32, FC36, FC78, FC81-FC83 cite primed ids | re-based to the unprimed ids | S-e-primed | editorial |
| — | FC77 | FC77′: every t with Hom(τ) has Sel(t; {t}, id, ∅) | FC77: no t has Sel(t; {t}, id, ∅) (F5); parts 2, 3 keep the other choice as its record | B8 | re-based |

## 3. Code (in `area 1 model/`)

| file | change | fix |
|---|---|---|
| model/claims_b.py | `SEL_H_NONEMPTY = True`; `sel(…, h_nonempty=None)` returns no when H = ∅ (round2=True keeps round 2's D12.1) | F5 |
| model/claims_b.py | `_prov_step`, `prov_fixed_points(…, rec_of=None)`: a holding that is a relay or record of an earlier holding takes that holding's (Sel, Con) | F3 |
| model/claims_b.py | FC77 restated (3 parts) | F5 |
| model/claims_s41.py | FC30.new1 (d) the student's copy computed from its history, U/K/T/T′; (e) a link no pair tried, D12.1 after round 2 vs H ≠ ∅; (f) K3's parts under D12.4 | B8, K3 |
| model/claims_r3a1.py (new) | FC12.new2 (per holding, records, B1's fix computed, N1), FC12.new3 (CT exact vs transitive), FC98.new1 (infinite chain, finite partial orders, L195's strict exclusion), FC84.new2 (covering, ordered, P4's unordered), FC13.new1 (P8), FC104.new1 (the two extents), FC28.new1 (B7's code, N3), FC28.new2 (obs readings), FC97.new1 (H, surv as organizations) | F1-F11 |
| model/run.py | imports claims_r3a1 | — |
| s104_creative_transport.py | CT8: T′ line per reading | F12 |

Whole suite (scale 4, cap 45; runs file §1): baseline 105 hold, 3 counterexamples, 7 not tested, of 115; after area 1: 114 hold, 3 counterexamples, 7 not tested, of 124 (the 9 new claims hold; no baseline claim changed status). s104_external.py: output identical to the committed printout; s104_creative_transport.py: CT8's five T′ lines added, nothing else changed (runs file §4, §5).

## 4. Text changes (`area 1 - text changes.json`; words outside formulas and pointers 51 → 12, no new word)

| id | line | kind | old → new | finding |
|---|---|---|---|---|
| R3A1-T1 | L61 | formal | "(Suff) sufficiency of the four conditions of Account" → "(Suff) sufficiency of \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (D16.XV)" | O1 |
| R3A1-T2 | L49 | formal | "when its components respond to those edits as the target structure does (Part VII)" → "when \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) (Part VII, D16.XV)" | O2 |
| R3A1-T3 | L69 | delete | "an account, " | O3 |
| R3A1-T4 | L69 | formal | "meeting \(\operatorname{Account}\) on its contract (Part V)" → "meeting \(\operatorname{Account}(\mathcal E)\land\neg\operatorname{Dec}(t)\) on its contract (Part V, D16.XV)" | O3 |
| R3A1-T5 | L220 | formal | "a **violation** occurs when fidelity fails at \((a,b)\);" → "a **violation** occurs when \(\neg(\text{F1 at }(a,b)\land\text{F2eq at }(a,b))\) (D12.7);" (settles FC104 at L220) | W1/W2 |
| R3A1-T6 | L201 | pointer | "a selected transport has no represented target and no criticism in its history; a constructed one has both." → "(D12.1, D12.2)." | K2 |

No change writes an invention into the text except R3A1-T5, which settles FC104's extent at L220 (I50 narrow, ruled Q11 in round 2).

## 5. Inventions (provisional ids; rule 6: numbered at integration after I166)

| id | fills (line; item) | choice | other choices | why this one | used by |
|---|---|---|---|---|---|
| R3A1-01 | "its history" (L193), "o_t", "h(t)" for a transport held more than once | provenance of a holding (t, o_t); h(t, o_t) the history that produced the holding; a relay or record carries its source's (D12.3′) | one provenance per transport on its whole history (I53: FC12.new2 (b) gives the tuple Con); per transport on the history that first produced it (I128 as registered: Sel); B1's precedence (FC12.new2 (b), (c)) | L211 "A carrier keeps its provenance", L405, L201 | D12.1, D12.3′; FC12.new2 |
| R3A1-02 | "prepares t" in CT (L197; I56) | exact: t held at an output of the trace | transitive through contents built from its outputs (FC12.new3) | L405's last sentence, L201 | D12.2; FC12.new3 |
| R3A1-03 | "acyclic causal precedence" (L375) under T′'s recursion | ≺_h well founded | acyclic only (B3; FC98.new1 (a)) | L526 "no endless descent"; D18.1's own proviso | D11.3, D18.1; FC98.new1 |
| R3A1-04 | "represents … H, or the survival condition" (L195) | H and Faithful_H over 𝒯 as organizations by L590's construction | the exclusion over t, cod t only (contradicts L195's formula); P3's record reading | L590, D13.6 | D11.2′; FC97.new1 |
| R3A1-05 | "a finite history H … actually encountered", "survived" (L195) | H ≠ ∅ | H = ∅ allowed (round 2; FC77 parts 2, 3) | Q2 as asked and answered (S41); L13; I52's registered other choice | D12.1; FC77, FC30.new1 (e) |
| R3A1-06 | "the observed value" (L151) where g is not single on Sol | one value or ⊥, ≠ as D6.4 | the image g[Sol] (B6's I168); one value asked at both pairs | D3.2's ⊥; the owner's Q15 convention (⊥ ≠ y, ⊥ = ⊥); the fibre query answers ⊥ there | D3.3; FC28.new2 |
| R3A1-07 | "immediately after" (D13.8, I165) | the covering relation of ≺⁺ on h′ | every ordered pair (equal under D13.8's contract-keyed records, FC84.new2 (a)); every unordered pair (P4 as written; FC84.new2 (b)) | L55 "every change … carries", one change at a time; the program's `episode` | D13.8; FC84.new2 |
| R3A1-08 | records in D13.8: Rec_h′(ρ_{q(o′)}) | recorded, not chosen: D13.8 keys a record by the new contract; the program (`episode`, FC84.new1) keys it by the change | — | they differ only where one contract is entered twice with one record; nothing here turns on it | D13.8; claims_b.episode |

## 6. Owner questions

None. Row 36's case (a search that holds its own target and keeps a survivor, no trace) is declared by L199 and L35 and falls under Q2 as asked; no line is held.

## 7. Parked

None. Row 8's H ≠ ∅ is not parked P1 (no strength ordering of survival conditions) or P2 (no competitor in 𝒯); its ground is Q2 as asked and L13, not what hard to vary covers.

## 8. Quotations relied on (rule 15; all found in the text under review, S41 or the maths)

L13 "produced by variation and survival on a history of encountered changes"; L105 "Several solutions remain several."; L195 "The transport \(t\) is a member of \(\mathcal T\) that survived."; L201 "Construction may operate on selected material."; L211 "a later record made from the carrier carries that provenance, not a second, independent one"; L245 "Together they are fidelity at every level the contract reaches."; L247 "**Question fidelity.**"; L405 "Reconstruction by a learner is construction; relay is not." and "the rest of the content keeps its inherited provenance"; L526 "The order has no cycle and no endless descent."; S41 "simply declared, not found by trial or worked out"; D18.1 "unique where ≺_h is well founded below o_t (every finite history)". Replies' quotations not found (tabulation §2: B3's L199 sentence, B7's "edits to the observed value", T6's words): rows 3, 7, 25 ruled on the text.

## 9. Moves (rule 16, counted strictly)

| counted | n |
|---|---|
| formal: F1 D11.3; F2 D12.1 (per holding); F3 D12.3′; F4 D12.2; F5 D12.1 (H ≠ ∅); F6 D11.2′; F7 D18.1 Held; F8 D3.3; F9 D13.8; F10 D4.6; F11 D5.7; F12 the program's reading of Con in CT8 | 12 |
| text: R3A1-T1 to R3A1-T6 (proposed; applied at integration) | 6 |
| **moves** | **18** |

Not counted: register entries R3A1-01 to R3A1-08; re-based claims (FC77; D12.7, D12.8 on h(t, o_t); the primed ids); new test claims and parts (FC12.new2, FC12.new3, FC13.new1, FC28.new1, FC28.new2, FC84.new2, FC97.new1, FC98.new1, FC104.new1; FC30.new1 (d)-(f)); no owner question, nothing parked.

## 10. Pairs of fixes that bear on one another (for integration, rule 7)

- F1 (D11.3) with area 3's S1 (P1): one fix.
- F2, F3 (per holding, records) with D12.4 (area 3 lines L405, L409) and FC67.
- F5 (H ≠ ∅) with area 3's W6 (the survival condition, L481) and D15.8.
- F7 (Held's extent) and R3A1-T6 with area 3's S-e-represented (L405, Held) and W7 (D13.3).
- K2 at L411 (area 3's line): no change here.
- L13's "an episode of conjecture and criticism" says what R3A1-T6 removes at L201 (a constructed history has criticism); no finding raised L13; left.
