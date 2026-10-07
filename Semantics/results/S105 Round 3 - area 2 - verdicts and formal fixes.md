# S105: Round 3 — area 2 (L229–L372, Parts V–VIII), verdicts and formal fixes

*Checker of area 2 (rule 5): a fresh Opus 5.5 agent that built nothing of this round. Created at once, filled as it goes (lesson S28). Obeys S23 except where it quotes. No text under review, rule, reply, decision or earlier file written. Read whole first: the rule; decisions S20–S41; the tabulation; the reply `s105_glm_maths_words.response.txt` (all six findings are its). Text under review: `tests/104 …with the owner's answers.md`, md5 bc14045aae3139df710d8339a9c1c81b (checked).*

- **Model copy:** `results/S105 Round 3 - maths after the reading/area 2 model/` (the program of `model after round 2/`, 15 files, md5s as the rule gives, checked at the copy). Run from that folder: `PYTHONHASHSEED=0 python3 -B -m model.run --claim FCnn --scale 4 --time-cap 45 --no-write`.
- **Runs:** `… maths after the reading/area 2 - runs.txt`. **Text changes:** `… maths after the reading/area 2 - text changes.json` (none).
- Verdicts (rule 5.1): **M** holds against the maths · **W** holds against the words · **INV** holds against an invention only · **NO** does not hold. T/F below are the program's boolean results.

## 1. Verdicts, one row per finding

| id (reply line) | item, line | verdict (one line) | fix as maths | code | runs | text |
|---|---|---|---|---|---|---|
| A2-T3 (r21) | D6.9, FC21; L257 | **NO**: the "less" is against round 1's words, which FC21 (b), (d) make false; L257 as it stands ("admits no candidate that meets (F2), (A) and non-circular dependence (FC21)") is FC21 (a2) with (F2) ⇒ τ(1)=1 (D5.5) and (1,b0) ∈ C (D3.1). | none | none | FC21 H (a2, d) | none |
| A2-T5 (r23) | D6.10, FC25; L269 | **NO**: the "less" is against round 1's "under any contract containing one", which FC25 part 2 makes false; L269's formula is FC25 (a*): L_k constant in the edit ∧ (1,b),(a,b) ∈ C ∧ F1 at both ⇒ proj(a,b) = L_k(τa,σb) = L_k(1,σb) = proj(1,b). | none | new test FC25.new1 ((a*) for a table varying with the boundary) | FC25 H; FC25.new1 H (25,920 models, 4,050 meet the hypothesis) | none |
| A2-T13 (r31) | E1, C_id, FC28; L325 | **NO**: the dropped clause "whose edits alter the observed L" is false of C_id = {1}×B, whose only edit is 1 (FC28, R4 part: an edit a ≠ 1 in C_id altering the observed L: F); what it named is D3.3's Ident (I163, L151: area 1, B6, B7, R4-L151, N3). L325 = E1 = FC28. | none | none | FC28 H | none |
| W3 (r76, r128) | D6.3 (I136); L255 | **INV**: D6.3's ∀ over Det_C (I136, a choice L255 leaves open: "does not appear … as a component" has no quantifier over C, round 2's ruling L255–L257) keeps a computed partial lookup (FC23.new1 (b)); W3's ∃ as written excludes the target's own organization wherever C sets the answer port (FC23.new1 (a) pole C2, C3; (c)), against its own expectation "FC26 … unchanged" (whole suite: FC26, FC62 fail): not taken. The choice between ∀ and ∃ with the edit's own setting exempt is **OQ-R3A2-1** (§4). | none adopted; the readings written in §2 | `core.slot`: `SLOT_QUANTIFIER` ∈ {every (default, D6.3 as it stands), some, some-exempt, some-exempt-set}; new test FC23.new1 | FC23.new1 (a)–(g); whole suite and the two other programs under each reading (§3) | none; L255 held (rule 12) |
| W4 (r79, r130) | D8.3 (I33, Off); L315 | **NO**: Off(ℰ′,p) is the text's own condition for a pair to pose a problem on a question: L317 "on which, offered for it, they pose a problem of the first kind"; L315's unqualified "a candidate that nobody has offered is no one's rival" is read with it. The other reading (∃q Off(ℰ′,q)) is recorded, since no register entry lists it: **R3A2-01**. No claim computes Riv (`core.rivals` is called by no claim). | none | none | none needed (no claim reads Riv) | none |
| W5 (r86, r136) | D10.6 (I141); L317 | **NO**: "while the argument stays usable" needs Out_j at each place, not an order of places: Solved(ξ) :⟺ Out^ξ_j (D10.6, D9.8), and where the premise is withdrawn X^{ξ′}_j = ∅ (FC56 (c), FC70), Solved fails and D10.1 poses the problem again. Computed: FC47.new1 (solved at ξ, posed again at ξ′, solved at ξ″). Q18 (ruled "yes") is what it computes; P7 stays parked (S33, S34). | none | new test FC47.new1 | FC47.new1 H | none |

**Counts.** 6 findings: M 0 · W 0 · INV 1 (W3) · NO 5. Formal changes: 0. Text changes: 0. Moves (rule 16): **0**. Not counted: new test claims FC23.new1, FC25.new1, FC47.new1; the quantifier switch (default unchanged, D6.3 as it stands); register entries R3A2-01, R3A2-02; owner question OQ-R3A2-1.

## 2. W3: the quantifier of D6.3 (I136), four readings, as maths

Det_C := {(a,b) ∈ C : Ans_p(a,b) ≠ ⊥}; P_k(a,b) :⟺ (a,b) translated ∧ {w_δE : w ∈ L^E_k(τa,σb)} = {Ans_p(a,b)}. Slot_C(ℰ,k) :⟺ δ_E ∈ V_k ∧ Det_C ≠ ∅ ∧ Q_k, with

| reading | Q_k | status |
|---|---|---|
| every | ∀(a,b) ∈ Det_C: P_k(a,b) | D6.3 as it stands (A2-02 = I136's choice); default |
| some | ∃(a,b) ∈ Det_C: P_k(a,b) | W3's proposal; not taken |
| some-exempt | ∃(a,b) ∈ Det_C: P_k(a,b) ∧ [τ(a) = 1 ∨ L^E_k(τa,σb) = L^E_k(1,σb)] | I136's third choice (round 2, G7-B5); side 2 of OQ-R3A2-1 |
| some-exempt-set | ∃(a,b) ∈ Det_C: P_k(a,b) ∧ [τ(a) = 1 ∨ ¬SetsThrough_E(τa, σb, δ_E, k)] (D2.1) | the exemption's narrow extent (R3A2-02) |

FC23.new1 (a), Acc under (every, some, some-exempt, some-exempt-set), computed:

| case | Acc |
|---|---|
| pole C1 (settings of H, θ; FC26) | T T T T |
| pole C2 (C1 + settings of L; FC26) | T F T T |
| pole C3 (baseline + settings of L; FC26 look) | T F T T |
| M5 (FC23 (d)) | T F F F |
| M13, the weathervane (FC22 (b), S41 Q15) | T T T T |
| M1, M2, M3 (FC23 (c)) | F F F F |

Generated (FC23.new1, SMALL, both families, scale 4):
- (b) W3's partial lookup, found (21,765 models): D: p0 ∈ {0,1}; h_p0 = {1} at b0, full at b1; k0 = full at b0, {0} at b1; C = {(1,b0),(1,b1)}; ℰ its copy. Acc (T,F,F,F).
- (c) 'some' alone excludes, found (45,308): a setting [p1=0] of the answer port replaces the component that assigns it. Acc (T,F,T,T).
- (d) 'some-exempt' keeps what 'every' excludes, found (8,818): c0 full at 1, {0} at e1; Ans_p ⊥ at the baseline, 0 at e1; ℰ its copy. Acc (F,F,T,T).
- (e) Acc_some ⇒ Acc under the other three: holds (25,920).
- (f) the two exempt extents differ, found (20,112): e1 sets p0 = 1 at b0 as the identity does; Acc (F,F,F,T): only 'some-exempt-set' treats a setting whose value the identity also gives as the edit's.
- (g) L339's eliminative construction: FC62's encoding (background k_rest the constant e = 0 at the baseline) (T,F,F,F); a second encoding with the same answers, edit and commitment (rest: e = 1 − u; h_u: u = 1) (T,T,T,T).

So: 'some' is the strongest reading (e); 'every' and 'some-exempt' differ both ways ((b), (d)); the two exempt extents differ only on a setting that coincides with the identity (f). Q15's answer is untouched under all four (M13).

## 3. Whole suite under each reading

Baseline (unchanged copy): 105 H, 3 CEX, 7 NT of 115, as the round's printout. The changed copy, default 'every': the same, plus FC23.new1, FC25.new1, FC47.new1 (H): 108 H, 3 CEX, 7 NT of 118; no other status or part changes.

| reading | H / CEX / NT of 118 | claims whose status changes from 'every' | parts that change |
|---|---|---|---|
| some | 106 / 5 / 7 | FC26 (C2: the setting of L is a slot), FC62 | FC23 (d) look (M5), FC26 C3 look, FC34 remark |
| some-exempt | 107 / 4 / 7 | FC62 | FC23 (d) look, FC34 remark |
| some-exempt-set | 107 / 4 / 7 | FC62 | FC23 (d) look, FC34 remark |

- FC62 under the ∃ readings: its encoding's background component is the constant e = 0 at the baseline, a slot at (1,b0); the second encoding (FC23.new1 (g)) keeps (E) under all four, so L339 ("it is offered as an account, and is listed under attack (Nec) … as a place where it may not be one") separates no reading; FC62's encoding does. Under side 2 of OQ-R3A2-1, FC62 is re-based on the second encoding (not a move, rule 16).
- FC34's remark "NC1 can fail on C′ while holding on C": under an ∃ reading NC1(C) ⇒ NC1(C′) for C′ ⊆ C (Det_C′ ⊆ Det_C), so no witness exists; FC34 stays H.
- `s104_external.py` (FC-E1–E5) and `s104_creative_transport.py` (CT1–CT8): output identical under all four readings, and to the round's printouts.

## 4. Owner question (rule 12)

**OQ-R3A2-1 (L255; D6.3, I136).** The owner's words say nothing on it; L255 has no quantifier over the cases of the question (round 2's ruling L255–L257); the computation shows what each side keeps and excludes (§2) and does not choose. L255 is held until the owner answers; the maths keeps side 1 meanwhile.

*In plain words:* when does a model count as simply having the answer written into it?

What the computation shows (§2, §3): of the text's own cases, the pole on C1, the weathervane (Q15), the lookups M1–M3, FC-E1–E5 and CT1–CT8 come out alike under both sides; M5 and FC23.new1 (b), (d) separate them; FC62's encoding of L339 separates them and a second encoding of the same construction does not.

| side | formal | everyday example |
|---|---|---|
| 1 (the maths now) | every | Only when one part of the model gives the answer by itself in every case the question covers that has an answer. A shop sign is red on Mondays and blue on Tuesdays; a model with one part saying "red", in place on Mondays, and another saying "blue", in place on Tuesdays, is not counted as having the answer written in, since no one part gives it in both cases (FC23.new1 (b)). A vane that points anywhere in still air and north when someone turns it north by hand: a model whose one part is "north when turned" is counted as written in, since that part gives the only answer there is (FC23.new1 (d)). |
| 2 | some-exempt | Whenever one part gives the answer by itself in any one case, unless the change the question asks about put it there. The two-part sign model is counted as written in (on Mondays the "red" part simply gives the answer). The hand-turned vane's "north" part is not, since the turning, the change asked about, put it there. |

Not offered: 'some' without the exception (W3 as written), which counts the pole's own mechanism as written in whenever the question includes setting the shadow's length directly (FC23.new1 (a), (c)). Neither side changes the owner's weathervane with the wind (Q15): it keeps (E) under both.

## 5. Inventions (rule 6; provisional ids, numbered at integration)

| id | fills (line; item) | taken | other choices | why this one | used by |
|---|---|---|---|---|---|
| R3A2-01 | L315 "a candidate that nobody has offered is no one's rival": which offer the displaced candidate needs (D8.3; W4) | Off(ℰ′,p): offered for p (round 2's amendment of I33) | ∃q Off(ℰ′,q): offered for some question; no offer clause (as D8.6's Riv_χ reads "offered one in place of the other") | L317 "on which, offered for it, they pose a problem of the first kind" | D8.3; D10.1, D10.4 through Riv; no claim computes Riv |
| R3A2-02 | the exemption of I136's third choice: "a component the contract's own edit replaces" (L103 "replaces"; W3) | not chosen; both run (FC23.new1 (f): they differ only where a setting's value is also the identity's) | alters k at σ(b) (some-exempt); sets δ_E through k (some-exempt-set, D2.1) | L103 gives "replaces" for setting edits; "A changed rule is a changed component" (L103) leaves an edit altering several relations (M5) unplaced | FC23.new1 only |

## 6. Parked (S33, S34)

None new. P7 (S20's "the mistake shouldn't be able to creep back in", read as keeping a problem solved after its argument lapses) stays parked; W5's ruling rests on D10.6 as written and touches it not.

## 7. Bears on other areas (for the integrator)

| here | there | how |
|---|---|---|
| A2-T13 | area 1: B6, B7, R4-L151, N3 (D3.3, I163) | C_id's "identification" is D3.3's Ident; FC28's R4 part computes it |
| W3 / OQ-R3A2-1 | FC22 (b) (Q15); FC26; FC107 | M13 unchanged under all readings; FC26 C2 changes only under 'some'; FC107 (E8's slot 'base') unchanged under all four |
| W4 / R3A2-01 | D8.6 (Riv_χ) | D8.3 asks Off(ℰ,p) ∧ Off(ℰ′,p); D8.6 asks no offer for the same words ("offered one in place of the other"); not a finding of this round, not changed |
| W5 / FC47.new1 | area 1: S-c ("D10.6 … no claim uses") | FC47.new1 now computes D10.1 and D10.6 |

## 8. Quotations compared (rule 15)

| quotation (reply) | line | result |
|---|---|---|
| "the target's answer does not appear … as a component" (W3) | L255 | found |
| "anywhere on C" (W3's gloss of L255) | L255 | not in the text; L255 has no quantifier over C |
| "offered as an answer to p in place of the other" (W4) | L315 | found |
| "while the argument stays usable" (W5) | L317 | found |
| "no candidate meeting non-circular dependence" (A2-T3, round 1's words) | L257 | not in text 103 or 104; text 103 L257 "admits no candidate that meets non-circular dependence" |
| "any contract containing one" (A2-T5, round 1's words) | L269 | text 103 only (dropped in round 2) |
| "whose edits alter the observed L" (A2-T13, round 1's words) | L325 | text 103 only (dropped in round 2) |
