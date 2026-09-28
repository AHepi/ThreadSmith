# S107: Round 4 — area 2 (L229–L372, Parts V to VIII): verdicts and formal fixes

*Checker of area 2 under rule 5 of `results/S107 Round 4 - how the replies will be read, written before sending.md` (read whole first, with its addendum): a fresh Opus 5.5 agent that built nothing of this round, 28 September 2026. Findings: the 20 that the tabulation (`… tabulation of the replies, before any ruling.md`, §0, §3) assigns to area 2. Each was read whole in its `.response.txt`: breaker r3–r42, r91–r92, r98–r107; maths_words r3, r9–r36, r60–r83, r102–r109; structure r41–r82, r97, r114–r121; cases r3–r29, r60–r84, r136–r174. K1 (the winter-myth knock-on) is area 3's (addendum 1: L317 [2], L397 [3], so L397's area); L317 is not ruled here. Text under review: `tests/106 … without the written-in test.md`, md5 c7af964c329ab7959243405d394e6574, not written. Maths: `results/S106 The written-in test taken out/`, not written. Program copy: `S107 Round 4 - maths after the reading/area 2 model/` (from `model after S106/`; md5s of core.py, claims_s106.py, claims_a.py, claims_b.py, claims_s41.py, claims_r3a3.py as the rule gives, checked at the copy). Runs: `… area 2 - runs.txt`. Text changes: `… area 2 - text changes.json`. Claims recorded for the harness: `… area 2 - expected claims.json`. Decisions S20–S49 read; S23, S40, S41, S43, S44, S45, S47 bind every row. "Model" below means only a small structure the program builds, or its folder (S43).*

Codes: **M** holds against the maths (or the program); **W** against the words; **I** against an invention only; **N** does not hold. Rule 3: every computation a reply marks not run, or that a ruling needs, was run first (runs §3). Rule 10: arguments, not agreement among replies. Rule 15: every quotation below compared with text 106 or the maths (the tabulation's §2; this file's own quotations in runs §6).

## 1. Verdicts

| # | finding | lines | v | why (one line) | fix |
|---|---|---|---|---|---|
| 1 | B2 | L255; D6.5 | N | D6.5 already states Dependence ⟺ NC2 (NC0 holds of every candidate, D6.2); FC108 H computes it; the conjunct formalizes L255's first sentence, which the text keeps; dropping it changes no value and leaves that sentence unformalized | none |
| 2 | B4 | L271 (L325) | W | L151: a production question has "a \(C\) containing interventions on upstream ports" (D3.3 Prod); C_H = {1} ∪ settings of H is one (FC27.new1 (a)); under τ′ on C_H, E_rev meets (F2) and every conjunct of (E) (FC27.new1 (d)), so L271 read of the production contracts L151 defines states an (F2) failure the computation does not give; read of E1's C1 (L325's contract) it holds under τ and τ′ (FC27.new1 (b), (c)). The step's reading (C1) was in no register: R4A2-01. B4's "on" for "under" not taken (S40) | R4A2-T1 (formal; settles R4A2-01) |
| 3 | B8 | D6.3 (L255) | M | D6.3's displayed ∀ has no "t translates (a,b)"; where τ(a) or σ(b) is undefined at a determined pair the clause has no value (FC23.new4 (a)); Pin (I184), `core.slot` and FC23.new3 (a) have the conjunct | F1 |
| 4 | B9 | D6.3 (Pin) | I | on C2, c_L pins at the 8 settings of L, each a pair whose own edit replaces c_L by a slice (FC23.new3 (d), FC23.new4 (d)); that this counts as a pin is I184's choice; I136's exempt reading exempts it for Slot; (E) reads neither (FC23.new1 (h)) | none; R4A2-02 recorded |
| 5 | B15 | FC23 (b); L273, L255 | N | FC23 (b) as stated has a counterexample (a background that empties Sol_E), ruled since round 2 as against the claim's own wording; its part "(b) with satisfiable background" (15,666 models, 431 meeting the hypothesis) and (e) hold, and carry what the step's M4 says; the loose citation is in a record of the step (`S106 report.md` §1 M4), which is not the maths or the text; restating (b) would turn a real counterexample of its wording into H | none; note §8 |
| 6 | B-N1 | N1: D7.4 (L302) | M | D7.4's Acc(E_v, p) has no designation, while Acc takes δ (D6.7); FC90.new1 (c): δ = L gives (E), δ = H does not; FC42.new1 (b): Boundary is no function of (E_v, t_v, Γ_v); (c): a renaming leaves δ_E no port of E_v | F2 |
| 7 | B-N5 | N5: L255's heading | N | the heading is D6.5's formal name (I188, S106-T1); a plain-word name would be new prose (S40); nothing reads the heading apart from the formula. The "vacuous first sentence" it points to is row 1 | none |
| 8 | S106-T3 | L255 | N | the deleted words and (E) part where S45 says they must: E_lk with a varying answer meets (E) (FC23 (e), FC23.new2 (b)); words and maths now agree | none |
| 9 | S106-T6 | L273 | N | as row 8: the one-part sign meets (E) under every reading (FC23.new2 (b)), as S44, S45 say; L273 is a pointer | none |
| 10 | W4 | D6.9's quote of L257 | M | the quote is text 103's by the core's convention (its preamble) and D6.9's [r2] mark names A2-T3; S106-T4's change of the same span is named at D6.5, not at D6.9, against "an [S106] mark names the text-106 change of a line where there is one". P3 (replace the quote) not taken: quotes stay text 103's | F3 (a mark; not counted) |
| 11 | W-N1 = W7 | N1: D7.4 | M | as row 6; P1's Acc(E_v, p, δ_v) written as D6.7's tuple, Acc((E_v, p, t_v, Γ_v, δ_v)) | F2 |
| 12 | W-N5 | N5 | N | as row 7 | none |
| 13 | S3 | D6.3 (L255) | M | with π undefined on Sol_D(a,b) at a determined pair and τ, σ defined, the displayed clause holds and Pin fails, so the core's "Slot_C(ℰ,k) ⟺ Det_C ≠ ∅ ∧ Pin … at every (a,b) ∈ Det_C" is false of D6.3 as displayed (FC23.new4 (b), a partial π); the program's π is total (I81), where the two coincide (FC23.new3 (a)) | F1 |
| 14 | S-N1 | N1: D7.4 | M | as row 6; P4's gloss (D5.3) kept; which designation: the one the operation carries δ_E to (R4A2-03) | F2 |
| 15 | S-N5 | N5 | N | as row 7 | none |
| 16 | C-K1 | L271 (L325) | W | as row 2; T1's "on" for "under" not taken (S40); T1's "L325 needs no change" agreed: L325 speaks of C1, where (F2) fails under τ and τ′ | R4A2-T1 |
| 17 | C-K3 | FC23.new2 (a) (L255, L273); L31 as ground | I | on a target with one part (c: red on Mondays, blue on Tuesdays) ℰ_two fails (F1) under all 1,568 λ and τ tried (FC23.new5 (a)): a decomposition the target lacks (L245 "(F1) prevents an assembled match from hiding a decomposition in error"), not a slot; the one-part candidate meets (E) there (b); on I189's target ℰ_two does (c). FC23.new2 (a) rests on I189, whose target holds the parts, as the owner's words have it (S44: "why is the red part or blue part there in the first place?"); the grain is a declared index (L31). The text settles it; no owner question | none; FC23.new5 |
| 18 | C-E6 | L343 | I | FC63's counterexample is part (c-i), I99's "sum over every tuple of term values" (F1 fails at the sum); with the sum over realizable term tuples (c-ii) the expansion meets (E), as L343 says; standing since round 2 (R17), unmoved by S106 | none |
| 19 | C-N1 | N1: D7.4 | M | as row 6; M2's "δ_v the designation carried to E_v (D5.3, I20)" is F2's | F2 |
| 20 | C-N5 | N5 | N | as row 7 | none |

**Counts.** M 7 (rows 3, 6, 10, 11, 13, 14, 19; rows 6, 11, 14, 19 one fix, F2; rows 3, 13 one fix, F1); W 2 (rows 2, 16; one fix, R4A2-T1); I 3 (rows 4, 17, 18); N 8 (rows 1, 5, 7, 8, 9, 12, 15, 20). 20 in all. No proposal of the area reverses or weakens an answer of S41 (with S47), puts the written-in test back (S44, S45), or has the maths ask for a criticism event (S47): the one computed candidate whose status moves in a record here, E_rev under τ′ on C_H, keeps meeting (E), a written-in candidate (r_L a slot), an explanation, a bad one.

## 2. Formal fixes (old → new; ids kept)

| fix | item | old | new | finding | settles / invention |
|---|---|---|---|---|---|
| F1 | D6.3 | Slot_C(ℰ, k) :⟺ δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C: {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)} [I135; quantifier I136]; likewise for a boundary coordinate of E whose value at σ(b) is Ans_p(a,b) [I79] | Slot_C(ℰ, k) :⟺ δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ ∀(a,b) ∈ Det_C [t translates (a,b) ∧ {w_δE : w ∈ L^E_k(τ(a),σ(b))} = {Ans_p(a,b)}] [I135; quantifier I136; I184]; likewise for a boundary coordinate of E whose value at σ(b) is Ans_p(a,b), t translating (a,b) [I79]. Mark: [r4: A2; B8, S3: "t translates (a,b)" (D5.1) inside the ∀, as Pin and `core.slot` have it; the [S106b] equivalence Slot ⟺ Det_C ≠ ∅ ∧ Pin at every pair of Det_C now holds of D6.3 as written (FC23.new3 (a), FC23.new4 (a)–(c))]. The rest of D6.3 unchanged | B8, S3 | — (I184's clause) |
| F2 | D7.4 | Boundary := {(v,w) ∈ 𝒱² : Acc(E_v, p) ≠ Acc(E_w, p)}, each v ∈ 𝒱 declaring (E_v, t_v, Γ_v), t_v the transport the operation carries t to and Γ_v the commitments it leaves (L231) | Boundary := {(v,w) ∈ 𝒱² : Acc((E_v, p, t_v, Γ_v, δ_v)) ≠ Acc((E_w, p, t_w, Γ_w, δ_w))}, each v ∈ 𝒱 declaring (E_v, t_v, Γ_v, δ_v), t_v the transport the operation carries t to, Γ_v the commitments it leaves and δ_v the designation it carries δ_E to (L231; D5.3, I20) [R4A2-03]. Mark: [r4: A2; N1 (B-N1, W-N1, S-N1, C-N1): Acc takes δ (D6.7); without δ_v Boundary is no function of the declared data (FC42.new1 (b); FC90.new1 (c)); δ_v carried, not quantified: L253 holds the query fixed (FC42.new1 (d))] | B-N1, W-N1, S-N1, C-N1 | R4A2-03 |
| F3 | D6.9 (a mark) | [r2: A2; D6.9, I26 ('≠ ⊥' dropped); A2-T2, A2-T3] | the same, then [r4: A2; W4: the quote is text 103's (preamble); L257 now reads "admits no candidate that meets (F2), (A) and \(\operatorname{Dependence}\) (FC21)" (A2-T3, S106-T4)] | W4 | not counted (no definition, claim or encoding changes) |

Text 106's L302 writes Boundary with Account(E_v, p); the text's candidate carries no designation (δ is I20, as at L449 in round 3), so L302 is not changed.

## 3. Code (in `area 2 model/`)

| file | change | fix |
|---|---|---|
| model/core.py | `boundary(family)`: family v ↦ ℰ_v = (E_v, p, t_v, Γ_v, δ_v); returns {(v,w) : Acc(ℰ_v) ≠ Acc(ℰ_w)} (after `minimal`) | F2 |
| model/claims_r4a2.py (new) | FC27.new1 (B4, C-K1); FC23.new4 (B8, S3, B9) with `PartialPi` (a candidate whose π is defined on a given set of solutions: D5.1's partial π, I16; test only), `slot_as_displayed_s106`; FC23.new5 (C-K3); FC42.new1 (N1) with `_moved_answer` (an edit that moves the answer onto a new port) | F1, F2, R4A2-T1; test claims |
| model/run.py | imports claims_r4a2 (one line after claims_s106's) | — |

`core.slot` and `core.pin` are unchanged: under "every" `slot` already asks `cand.translates(a, b)`, so F1 brings the maths to the code. D18.1's DEP is unchanged: "(D)" reaches δ through "(E)" → "Dep" → "δ", as "(S)" does for D7.1.

Whole suite (runs §1, §4; PYTHONHASHSEED=0, scale 4, cap 45, --no-write): baseline 128 H, 2 CEX (FC23, FC63), 7 NT of 137, equal to the round's printout but FC14's file-name line (the copy reads round 3's core by its fallback path; area 3's B14, W6, S1) → after area 2: 132 H, 2 CEX, 7 NT of 141; 4 new claims, each H; every other claim and part equal to the baseline (runs §4).

## 4. Text changes (`area 2 - text changes.json`)

| id | line | kind | old → new | finding | settles |
|---|---|---|---|---|---|
| R4A2-T1 | L271 | formal | "fails (F2) under the production contract:" → "fails (F2) under the production contract \(C_1\) (E1, FC27):" | B4, C-K1 | R4A2-01 |

Checked by the harness's `apply_changes.py` on a scratch copy (runs §5): the span occurs once in L271; applied and undone byte for byte; 632 lines; words outside formulas 15,204 → 15,206, the two the pointer's ids "(E1, FC27)"; no new word of prose; S95 80 → 80, S96 196 → 196, 0 new; headings, terms and tags kept. Rule 6, in so many words: the text should now settle R4A2-01 at L271, since read of the production contracts L151 defines the line states an (F2) failure the computation does not give (FC27.new1 (d)), and L325, the text's own construction, fixes C1.

## 5. Inventions (provisional ids; numbered at integration after I191)

| id | fills | choice | other choices | why this one | used by |
|---|---|---|---|---|---|
| R4A2-01 | L271's "the production contract" (the step's reading, in no register: B4) | E1's C1: the settings of H and θ at b1_45 (L325) | (a) every production contract (L151; D3.3 Prod): false for τ′ on C_H (FC27.new1 (d)); (b) every production contract with τ carrying each intervention to itself: holds (FC27.new1 (b)), but writes a condition on τ L271 does not write | L325 is the text's own worked contract for the reversed calculation; the formula and pointers add no word (S40) | R4A2-T1; FC27, FC27.new1 |
| R4A2-02 | Pin (I184) at a pair whose own edit alters k (B9) | counts as a pin (I184 as registered) | (d) exempt there, I136's "some-exempt" at one pair: every pin of c_L on C2 would go (FC23.new4 (d)) | I184's registered choice; the exemption was registered for Slot's quantifier (I136), not for Pin; (E) reads neither | D6.3 (Pin); FC23.new3 (d), FC23.new4 (d) |
| R4A2-03 | D7.4's designation of E_v (N1) | δ_v, the designation the operation carries δ_E to, declared with t_v and Γ_v | (a) quantified, ∃δ_v, as D14.7 (I180) and D16.4 (I183): an edit that moves the answer onto another port keeps Acc (FC42.new1 (d)); (b) δ_E unchanged: no value where the edit renames L (FC42.new1 (c)) | L231's pattern ("t′ the transport the operation carries t to"); L253 "The query \(\mathcal Q\) is held fixed"; D7.1 carries δ_E | D7.4 (F2); core.boundary; FC42.new1 |

Settled by a text change: R4A2-01 (R4A2-T1). Recording R4A2-02 and R4A2-03 is not a move (rule 16).

## 6. Owner questions

None. B4, C-K1: L325 fixes C1 and the computation shows the general reading fails; nothing the owner's words leave open. C-K3: the text settles which candidate meets (F1) on which target ((F1), L245; the grain a declared index, L31), and S44's own words give the sign red and blue parts; S44 and S45 speak of the written-in answer, which is not what fails on the one-part target.

## 7. Parked

None: no finding of the area concerns what hard to vary covers (S33, S34; P8) or where values are placed.

## 8. Moves (rule 16, strict), notes and pairs for the integrator

| | items | n |
|---|---|---|
| formal | F1 (D6.3), F2 (D7.4) | 2 |
| text | R4A2-T1 | 1 |
| **moves** | | **3** |

Not counted: F3 (D6.9's mark); R4A2-01…03; test claims FC27.new1, FC23.new4, FC23.new5, FC42.new1; `core.boundary` (F2's encoding, counted with F2); `PartialPi` (a test encoding).

Notes: B15: the step's M4 citation "FC23 (b)" is served by FC23's part "(b) with satisfiable background" and (e); a matter for the records, which this checker does not write. W5, S-δ, S-κ, B14, W6, S1 are area 3's.

Pairs that bear on one another:
- R4A2-T1 (L271) and L536 (area 3): the same words, "a reversed calculation fails (F2) under the production contract.", ending "."; neither reply names L536; left as it is, the two lines read "the production contract" differently. The same formula and pointers can stand there.
- F1 (D6.3), F2 (D7.4) and S-δ's P9 (area 3): P9 renames δ_D, δ_E in D6.3 and D7.4 among others (tabulation §6.5).
- F2 (δ_v carried) and D14.7 (I180), D16.4 (I183) (∃δ): a different choice for a different use, recorded as R4A2-03's other choice (a).
- FC23.new5 and FC23.new2 (a) (I189): C-K3.
- `model/run.py`: one import line added after claims_s106's; other areas' import lines at the same place will conflict in a three-way merge (Opus resolves: keep all).
- FC14 in this copy reads round 3's formal core through its fallback path (B14, W6, S1, area 3); its status and parts are unchanged, so the harness's comparison, which reads statuses and parts only, is not affected.
