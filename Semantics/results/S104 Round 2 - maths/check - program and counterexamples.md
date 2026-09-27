# S104 round 2 — check of the program and its counterexamples

*Log S104, review round 2 (the maths round), 27 September 2026. A fresh check (Opus 5.5) of the program in `model/` and of the twelve claims it reports with a counterexample. The text under review is `tests/103 The semantics, standing alone, after round 1.md`, md5 f31ebb1f050783f1a84f6136cec20fcd. Its md5 was the same before and after this check. This check wrote nothing except this file; the scratch scripts it used are in the session scratchpad and are not part of the record. Nothing here is settled (S28). Every verdict below is a conjecture about the program and the formal core, open to replacement.*

**How to read the verdicts.**
- **CONFIRMED** means three things. The one-command re-run printed the same counterexample. Working by hand from the printed model, the model meets the claim's premises as the formal core and the named inventions define them. And the model breaks the claim's conclusion.
- A counterexample is only as strong as the inventions it rests on. Where it also rests on a choice that the register does not list, this file says so. Such a choice is an **unrecorded invention**, in the owner's sense ("if implementation forces invention, that needs to be recorded").
- Nothing an invention fixes is the text's own content.

## 1 What was run

| Run | What | Result |
|---|---|---|
| R0 | The twelve one-line commands `python3 -m model.run --claim FCnn --scale 4 --time-cap 45` (FC05, FC18, FC20, FC23, FC25, FC63, FC77, FC78, FC81, FC82, FC83, FC102) | All twelve reproduce. Each counterexample or not-as-claimed text is identical, character for character, to the one in `search results.json` (12 of 12). |
| R1 | All 110 claims with new seeds (seed = 7,000,000 + 10·n + k in place of 104,000 + 10·n + k), `--scale 4 --time-cap 45`, 336 s | The same 87 / 12 / 11 split. All 185 parts have the same status as the record: 62 searches with no counterexample and 6 with one, 18 with a witness and 1 without, 51 + 6 computations, 16 by construction, 3 + 2 looks, 20 not tested. There are no new counterexamples and no errors. |
| R2 | 24 claims with more HOLDS parts, or parts whose hypothesis was met rarely, with new seeds again (9,100,000 + …), `--scale 12 --time-cap 120`, about 685,000 models | Every part has the status of the record. FC56 (a) again hit its time cap, now at 120 s, within its single placeholder size (§4.5). |
| R3 | 51 hand-made cases for the core predicates (`solve`, Sol, deletion, `sol_sub`, Set/asg/Out/Obs, the three families, `one_kind`, proj^λ with a hidden port and with a value map, (F1), (F2), (A), `hom`, `slot`/NC1, `contrast`, NC2, `routes`, `restrict`, `meets_ab`, `conflict`, `nonvacuous`) | 50 came out as worked by hand. The one mismatch was my expectation, not the code (§4.2). |
| R4 | The whole suite under two fixed hash seeds (PYTHONHASHSEED = 1, 2) with the recorded seeds | See §4.1. |
| R5 | The whole suite with I83's listed alternative in place of I83 ("the slot condition asked only at the pairs where Ans_p is determined") | See §5. |
| R6 | The whole suite with I80's listed alternative in place of I80 ("exclude 1 from Set_v") | See §5. |

## 2 The twelve counterexamples

### FC05 — CONFIRMED, under I93 reading (ii) only

> L119 | an edit under which the two relations stay equal does not separate the components.

**Model.**
- D has ports p0, p1 ∈ {0,1}, components c0 and c1, both on (p0, p1), and edits {1, e1}.
- At (1,b0): L_c1 = {(0,0),(0,1)} (p0 = 0) and L_c0 = {(0,0),(1,0)} (p1 = 0).
- At (e1,b0): both relations are {(0,1),(1,1)} (p1 = 1).
- C = {(1,b0)}.

**Hand check.**
- The swap β: p0 ↦ p1 carries L_c1(1,b0) to L_c0(1,b0), so c1 ~_C c0.
- At (e1,b0) the two relations are equal under the identity bijection. They are not equal under the swap, which gives {(1,0),(1,1)}.
- On C ∪ {(e1,b0)} one bijection would have to serve both pairs. The identity fails at (1,b0) and the swap fails at (e1,b0). So the new pair separates the components.

**What it rests on.**
- It rests on I93 reading (ii), "equal under some footprint bijection". FC05's own formal statement uses the same β throughout, which is reading (i), and under reading (i) the claim holds of every model tried. So the claim-level status "COUNTEREXAMPLE FOUND" is a counterexample to one reading of L119, not to FC05's formal sentence as written.
- **A third reading the register does not list:** "the edit leaves each of the two relations as it was at (1,b)". This fits the sentence just before it in L119 ("replaces only the component that assigns the port … not the relations of the components that read it"). I searched it on 1,752 G-free models that met its premise. 82 were separated, and every one of the 82 had (1,b) ∉ C. So under reading (iii) the sentence holds whenever the baseline at that boundary is in the contract.
- Also I10, I77, I78.

### FC18 — CONFIRMED, under I94 only

> L558 | A condition "each component's counterpart must be a component of the same kind" adds nothing to (F1) on any contract.

**Model.**
- D has one port p0 ∈ {0,1} and one component c0 with L_c0(1,b0) = {(1)}.
- E has p0 ∈ {1} and one component k0 with L_k0 = {(1)}.
- The value map is κ(0) = κ(1) = 1, and λ(k0) = ({c0}, κ).
- C = {(1,b0)}.

The printed counterexample does not show D. I recovered D by capturing the model object (§4.3).

**Hand check.**
- (F1): κ[{1}] = {1} = L_k0.
- Under I94 the counterpart is read untranslated, as {(1)} over the domain {0,1}. k0's relation is the same set {(1)}, but over the domain {1}. I10 requires X_v = X_β(v), so no footprint bijection exists between them. SameKind fails.

**What it rests on.**
- The failure comes only from the two domains differing, not from the relations.
- It rests on I14's value maps (which the text does not have), I94 and I10. Under D4.4's reading the claim held on every model tried. Also I13, I77, I78, I81.

### FC20 — CONFIRMED, and the summary's wording is slightly too strong

> L250 | \operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b). \tag{A}

**Model.**
- D has p0 ∈ {0,1} and c0 = the full relation, so Sol_D(1,b0) = {0,1} and Ans_p = ⊥.
- π reads p0 through κ(0) = κ(1) = 0.
- E has p0 ∈ {0} and L_k0 = {(0)}.

**Hand check.** π[Sol_D] = {(0)} = Sol_E, so the valuation equation of (F2) holds. Ans_E = 0, while κ(Ans_p) = κ(⊥).

**Unrecorded invention.** The test sets κ(⊥) := ⊥. The part's statement says so, but no register entry does, and the formal claim does not define κ at ⊥.

**What the counterexample shows.** By hand, whenever Ans_p(a,b) is determined (= y), the equation of (F2) makes the designated coordinate of Sol_E equal to {κ(y)}. So Ans_E = κ(Ans_p) for every κ, injective or not. The claim can fail only where Ans_p = ⊥ and κ merges the values Sol_D takes there into one.

So the summary's "(F2) at a pair gives κ(Ans_p) only if κ is injective" should read: "gives κ(Ans_p) wherever Ans_p is determined; where Ans_p = ⊥, E's answer is ⊥ only if κ does not merge the values Sol_D takes there".

It rests on I14, I16, I20, I21, I49, I50, I77, I78 and I81, and on the unrecorded κ(⊥) = ⊥.

### FC23 (b) — CONFIRMED, under a footprint reading of "constraining"

> L273 | "\(p\) because \(p\)" fails non-circular dependence.

**Model.**
- D has p0, p1 ∈ {0,1} and c0 on p0, with {(0)} at 1 and {(1)} at e1. Ans_p is 0 and 1, so it is not constant on C = {(1,b0),(e1,b0)}.
- E_lk has k on p0 (the answer slot) and a background component bg on p1 with the empty relation at both pairs.

**Hand check.**
- Sol_E = ∅ at both pairs, so Ans_E = ⊥ at both.
- Contrast needs Ans_E(x0) ≠ ⊥, so no pair gives a contrast and NC2 fails. FC23 (b) says NC2 holds.

**What it rests on.**
- The model meets FC23's premise "no other component constraining the answer ports" only if that premise is read by footprints: bg's footprint is {p1}. An empty relation removes every valuation, so under a reading by solutions bg does constrain p0. This choice is not recorded as such; I81 mentions only "lookups (FC23)".
- The counterexample does not bear against L273: this lookup fails NC1 and NC2, so it still fails non-circular dependence. It bears only on FC23's "through NC1 only".
- With a satisfiable background the claim held on every model tried.
- Also I21, I22, I24, I25, I77, I78, I79, I81, I82, I83.

### FC25 (b) — CONFIRMED; the failure is of λ's well-formedness

> L269 | A table that encodes an organization's response to every admitted change is not a table in that sense: it meets (F1) as a decomposition does

**Model.** D has p0, p1 ∈ {0} and one component h_p0 on p0, so p1 is in no footprint. E_enc records p1, and λ(tab) = (J_D, p1 ↦ p1).

**Hand check.**
- V_{J_D} = {p0}, so no θ can send p1 into it (I14).
- `proj_lam` returns None and (F1) fails. The same holds with two-valued domains: I checked D with p0, p1 ∈ {0,1}.

**Unrecorded invention.** The program scores an ill-formed λ (a translation that reads a port outside V_N) as a failure of (F1). The other choice is that such a tuple is no candidate at all. Under either choice "E_enc meets (F1)" fails as stated. The substance is that a port in no footprint, absent under I03, cannot be carried by any λ.

It rests on I03, I14, I32, I77 and I78, and on that unrecorded choice.

**The witness for (a).** The smallest witness in the record (a table faithful on a contract with a setting edit) is degenerate. It uses [p0 = 0] where p0 is already 0, so the edit changes no relation. I built a model that is not degenerate. There, [p0 = 1] replaces h_p0's relation, even with the identity edit excluded (I80's other choice), and a table on p1 alone still meets (F1). So the finding against L269's "under any contract containing one" stands without the degenerate case.

### FC63 (c) — CONFIRMED as computed, as a choice between two writings

> L343 | The full Leibniz expansion with skewness substituted meets (F1) and (F2): every intermediate product is a determinant suborganization whose hidden ports project away.

**Hand check of (c-i).**
- Variant (c-i)'s sum component relates all 3⁶ tuples of GF(3) term values to their sum. Its counterpart {order, det} projects only onto term tuples that some matrix gives.
- The tuple (1,1,1,1,1,1, 0) is not realizable. For a 3×3 M, each entry lies in exactly one even and one odd term, so t₀t₃t₄ = −t₁t₂t₅ (even against odd permutations). All ones would need 1 = −1 in GF(3). For orders 1 and 2 the other terms are 0 by I99.
- So (F1) fails for the sum component at every pair.

**What it rests on.** Variant (c-ii) meets (E). Which of the two is "the" Leibniz candidate is I99's choice. Both need I81's derived ports, and I14 excludes derived ports, so under the formal core as written the candidate cannot be written at all. That is stated in the record. Also I03, I27, I66, I82.

### FC77 — CONFIRMED; FC77's conclusion survives it

> L195 | The transport \(t\) is a member of \(\mathcal T\) that survived.

**Model.**
- The edits are G-surg overrides, with [p0=0]·[alt] = [p0=0,alt].
- τ: [p0=0] ↦ 1, [alt] ↦ [alt], [p0=0,alt] ↦ [p0=0].

**Hand check.**
- τ([p0=0])·τ([alt]) = 1·[alt] = [alt] ≠ τ([p0=0,alt]) = [p0=0], so Hom(τ) fails.
- Faithful_∅ includes Hom, and Hom is not relative to pairs (D5.7, I18). So Sel(t; {t}, id, ∅) fails, contrary to "fidelity on ∅ is vacuous".

**Why FC77's conclusion survives.** (R) itself asks Faithful_C(t), and that includes Hom. So every t that can figure in (R) has the trivial witness Sel(t; {t}, id, ∅). The second part, Sel(trivial) ⟺ Hom, held on every model tried. FC77's point, that (R) keeps no content from "selected" while the physical module is open, therefore stands. Only its "for every t" is too wide.

It rests on I18, I48, I52, I77, I78, I81 and I90.

### FC78, FC81 (d), FC82 — CONFIRMED as statements about the definitions; one finding, not three

> L193 | A transport \(t\) whose domain is an organization of a physical system has exactly one of three provenances, determined by its history in the physical module:

> L201 | Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both.

**Model.** The history h is set by hand (I90). One occurrence represents t's codomain, Prepares holds, every pair of C occurs, and nothing represents t, H or the survival condition. t is the pole's forward transport, and H = {(1,b1_45)}.

**Hand check.**
- D12.1 forbids only representations of t, H or the survival condition (L195). So Sel(t; {t}, id, H) holds: t is faithful on H, Hom included.
- D12.2 lets Con hold through "the organization it carries to" (L197), so Con holds too.
- I53's own gloss ("Sel has none") imports L201's clause, which D12.1 does not contain. The formal core is at odds with itself here, and the counterexample shows where.
- If the represented item is t itself rather than its codomain, Sel fails. I re-computed this. So everything turns on representation of the codomain.

**The three are one finding.**
- FC81 (d) uses the same history, with t replaced by a transport violated at (set(H=2), b1_45) ∉ H. So Sel, Viol, Surp and Con all hold.
- FC82 uses the same history with t' = t.
- These two follow from FC78's model and should be counted as one finding.

**FC82 made stronger.** The recorded FC82 uses a "response" in which t' = t and nothing is violated. That meets D12.8 as written, but a reader could object that it responds to no violation. I built the stronger case: 𝒯 = {t, t'} and μ(t) = {t'}; t is violated at x = (set(H=2), b1_45) ∉ H; t' survives on H ∪ {x}; and the same h gives Con(t'). SelResp and ConResp still have a common result.

These rest on I52, I53, I54, I56, I90 and I92. No physics was computed; the model shows what the definitions allow, not what any physics does.

### FC83 — CONFIRMED as a statement about the definitions

> L225 | Only the second can be originative under Part X.

**Hand check.** Origin's three conjuncts are set true by hand: Attempt, New, and Build's primitives (I56). SelResp holds on the same history. Nothing in D12.1, D12.8 or D13.3 ties Build's subhistory to the selection history, so the definitions do not exclude it.

**What it rests on.** This is independent of FC78. It shows that the definitions do not link the two, and does not model a physics. It rests on I52, I56, I90 and I92.

### FC102 (b), second half — CONFIRMED, by an independent re-implementation

> L626 | If the population's transports can only predict from occupancy, no member survives the extended history: the fidelity failure is structural, not parametric.

**Independent re-implementation.** I rewrote I100's object layer from the register's description: six cells, reflection at the ends, cells 1..4 hidden from t = 3 for L steps, and a window of w frames ending just before re-emergence. It gives the program's tables exactly:
- one thing fails at (w, L) = (1,0), (2,1), (3,2), that is, at w = L + 1;
- one thing never fails once w ≥ L + 2;
- two things fail at (1,0), (2,0), (2,1), (3,1), (3,2).

**Why.** One visible frame gives position but not velocity. So "a window at least as long as the occlusion" is not enough, and neither is a window one step longer.

**The two-thing example.** The printed example, (w,L) = (1,0), fails for one thing too, so it does not show the lack of identity. (w,L) = (2,0) does: things at 0 and 1 standing still, against things at 1 and 2 moving −1 (the reflection at cell 0 makes their occupancy {0,1} twice), give equal readings for two frames and differ on the third. In the open, two things crossing and two standing still do the same.

It rests on I52, I68 and I100.

## 3 Verdict table

| Claim | Verdict | Unrecorded choice found by this check |
|---|---|---|
| FC05 | CONFIRMED under I93 (ii) only; FC05's formal sentence (reading i) holds | a third reading of "stay equal" (unchanged relations), which holds when (1,b) ∈ C |
| FC18 | CONFIRMED under I94 (domains differ only) | none; the printout omits D |
| FC20 | CONFIRMED | κ(⊥) = ⊥; the claim fails only at ⊥ answers |
| FC23 (b) | CONFIRMED under a footprint reading of "constraining" | the reading of "no other component constraining the answer ports" |
| FC25 (b) | CONFIRMED | an ill-formed λ scored as a failure of (F1) |
| FC63 (c) | CONFIRMED as computed (variant c-i); c-ii meets (E) | none beyond I81/I99 |
| FC77 | CONFIRMED; FC77's conclusion survives | none |
| FC78 | CONFIRMED (definitions, I90) | none; I53's gloss disagrees with D12.1 |
| FC81 (d) | CONFIRMED; a corollary of FC78 | none |
| FC82 | CONFIRMED; a corollary of FC78; holds in a stronger form | none |
| FC83 | CONFIRMED (definitions, I90) | none |
| FC102 (b) | CONFIRMED (re-implemented) | none |

No counterexample is NOT CONFIRMED. None comes from a bug in the program.

## 4 Program review

I read `core.py`, `harness.py`, `gen.py`, `cases.py`, `run.py`, the tests of the twelve claims and a sample of the other tests. I did not read `args.py`, `phys.py` or the set-system tests in full; those were checked only through the re-runs R1–R4.

### 4.1 Bug: a run depends on Python's hash seed, not only on the recorded seed

**What happens.**
- Four places draw at random from, or take "the first" element of, a frozenset of string pairs, whose order changes from one Python process to the next:
  - `claims_a.py` L1083: FC34 builds C′ ⊆ C with `for x in p.C … rng.random()`.
  - `claims_b.py` L1499: FC80 builds H with `for x in p.C … rng.random()`.
  - `claims_b.py` L1561 and L1571: FC82 and FC83 take `[a for a in p.C if …][0]`.
  - FC38 prints `minimal(S)` in set order.
- In each of these, the pair the rng acts on changes with the process.

**What it changes (R4).**
- The recorded seeds, run under PYTHONHASHSEED = 1 and = 2, changed no status in any of the 185 parts.
- They did change the reported models:
  - FC34's "wide reading" and "not monotone" parts found different witnesses after different numbers of models (2,190 and 2,896 in place of 2,482 and 2,549). A plain re-run of FC34 in five processes gave four different outputs.
  - FC82 and FC83 named ('set(H=1)', 'b1_45') in place of ('set(H=2)', 'b1_45'). At b1_45, u_H = 1, so set(H=1) is an edit that changes nothing. The verdict is the same.
  - FC38 listed the minimal routes in the other order.
- FC56's count also varies, but that is its time cap, not the hash seed.

**Consequence.** "Every counterexample reproduces with one command" is true of every verdict. The printed text of FC82 and FC83 reproduces only when the process happens to order C as the recorded run did. It did so in my R0 re-run and not under PYTHONHASHSEED = 1. FC34's recorded witnesses are not reproducible by the one command.

**Fix.** Iterate `sorted(p.C, key=repr)` wherever the rng or a "first" pick meets a set. Or fix PYTHONHASHSEED at start-up, for example by having `run.py` re-execute itself with it set.

### 4.2 The core predicates against hand-made cases (R3)

**Coverage.** 51 cases with values worked out by hand. They cover:
- the solver: two constraints, an empty-footprint constraint, no constraints, a cyclic unsatisfiable pair;
- Sol, deletion and the solutions of a subnetwork, including the empty one ({()});
- Set, asg and Out, and I80: the identity sets a port that its component already fixes;
- Obs, and the three families on a two-component copy circuit;
- one kind (by swap, and refused between unequal domains);
- the pole:
  - the forward candidate meets (E) on the settings of H;
  - Ans at the baseline is 1 and at set(H=2) is 2;
  - deleting c_L gives ⊥;
  - NC1 holds and NC2 has a witness;
- `hom`: the identity map, a map whose images do not compose, a composite outside dom τ (I84), and τ(1) ≠ 1;
- the lookup: a slot, so NC1 fails and NC2 holds;
- contrast in its four ⊥ cases;
- proj^λ with a hidden port;
- a flipped value map, under which (F1) and (F2) hold and (A) fails;
- conflict by differing answers, `meets_ab` under the target's own relations, restriction, routes, and a scope statement that silently leaves a pair out.

**The one mismatch.** It was mine. In a circuit where c_v copies u into v and no edit sets v, Meas(c_v, v) holds. asg(v) is undefined, and I102 counts v among the ports c_v does not assign, so Inv_C(c_v, Set_v) holds vacuously. **So under I102 a component can have the measurement signature for its own output port.** The register records I102 but not this consequence.

### 4.3 Reporting defects (the verdicts are unaffected)

- **FC18.** The printed counterexample leaves out D (p0 ∈ {0,1}, L_c0 = {(1)}), and the failure turns on exactly that domain. A reader cannot check it from the printout.
- **FC102.** The "two things, no identity" example printed is (w, L) = (1, 0). A single thing fails there as well, so it does not show the point. (2, 0) does (§2).
- **FC25 (a).** The smallest witness in the record uses a setting edit that changes nothing. A witness that is not degenerate exists (§2), and the record could give it.
- **FC20.** The summary's "only if κ is injective" is too strong (§2).
- **Claim-level status of FC05.** The status is "COUNTEREXAMPLE FOUND" although FC05's formal sentence, reading (i), held. The counterexample is to I93 reading (ii).
- **`overall()`.** A "there is" part that finds no witness leaves a claim at "HOLDS ON ALL MODELS TRIED" (FC85; a constructed example stands in). For an existential claim that status reads oddly, and FC85 is among the 87.

### 4.4 Unrecorded inventions found

The owner's rule asks that each of these be recorded.

- **κ(⊥) := ⊥** (FC20, `claims_a.py` L707). FC20's counterexample exists only because of it.
- **An ill-formed λ(k) counts as a failure of (F1).** In `core.proj_lam`, a translation that reads a port outside V_N returns None, and F1_at then fails. The other choice is "no candidate". FC25 (b) uses it.
- **The footprint reading of "no other component constraining the answer ports"** (FC23 (b)).
- **A third reading of "the two relations stay equal"** (L119; FC05). The two relations are unchanged by the edit. Under it the sentence held whenever (1,b) ∈ C.
- **Dependence on core-level inventions is not carried to results.**
  - Dependence is recorded through each test's own tags. An invention that acts inside `core.account` reaches every result that computes (E), yet the register ties it to few or no results.
  - I83 lists only FC23 and FC24, and I84 lists no claim. `hom` (I84) runs inside every (F2).
  - `slot` (I83) runs inside every NC1. §5 shows this matters: FC34's "wide reading" witness depends on I83, and the record does not say so.

### 4.5 Smaller notes on the code (no effect on any verdict)

- **`gen.gen_candidate`.** The first "random τ" block is never passed to `_E_from_lam`. So E is always built from the identity τ, and both blocks give "a transport that reads the wrong edit". About 19% of candidates get a random τ, not the 10% the parameter suggests.
- **Some HOLDS searches cannot fail given the definitions.** They check only that the code agrees with itself; no model could have broken them. These are:
  - FC17: (F1) is that equation;
  - FC29: NC2's witness is on τ[C] by definition;
  - FC05 (i) and FC05 reading (i);
  - FC21 (a): (A) makes every relabeling pair's answer the baseline answer;
  - FC51 (a): adding pairs cannot remove an NC1 or NC2 witness.

  They are among the 62 "held" parts.
- **FC56 (a)** has one "size", and that size is only a label (its models are random premise sets over p, q, r with every argument of height ≤ 2). The time cap stops it after 1,162 of the 1,600 planned draws at 45 s, and after 3,309 of 4,800 at 120 s in R2. So its count depends on machine speed.

## 5 Sensitivity to I83 and I80

I83 and I80 both act inside the core, so a result can depend on them without its test naming them (§4.4). I re-ran the whole suite with the recorded seeds, first with I83 and then with I80 replaced by one of the other choices the register lists for it.

- **No claim status and no part status changed in either run** (R5, R6). This covers all 110 claims and 185 parts, including all twelve counterexamples.
- **The reported models change in these places (beyond what the hash seed alone changes):**
  - **FC34 under I83's alternative.**
    - The recorded "wide reading" witness does not survive. Its one commitment k0 is the target's own component, and it equals the answer slot at every pair where the answer is determined. It escapes NC1 only because I83 lets one ⊥ pair block the slot: at ([alt:h_p0], b0) the relation is empty, so the answer there is ⊥. I rebuilt the witness by hand and evaluated it under both readings: as coded it meets (E) on both questions. Under the alternative, k0 is a slot, and (E) fails on both questions.
    - The search then finds another witness after 5,681 models. In that witness E is again a copy of the target: two components each fix the answer at one boundary, so neither is a slot. The finding "a candidate can meet (E) on two questions about one target" survives I83's alternative, but the recorded witness rests on I83, and the record does not say so.
    - Three other parts of FC34 found different witnesses as well.
  - **FC46 under I83's alternative.** Pairs of candidates that both meet (E) became rarer: 98 met the hypothesis, against 722. It still held.
  - **FC02 and FC08 under I80's alternative.** FC02 (c) now reports "the identity edit is a setting edit of H and of θ: False", and FC02 (a) and FC08 found witnesses after one model and after 18,090 models respectively. No status changed.
- **Two consequences worth recording.**
  - The recorded FC34 "wide reading" witness, which the summary lists among the results bearing on L151, depends on I83. The finding does not.
  - In both witnesses the candidate that meets (E) on two questions is a copy of the target itself. Whether "D itself" counts as an explanation of D, and under which reading of NC1, is a question these models raise, not one they settle.

## 6 Summary

- **Counterexamples.** All twelve are CONFIRMED.
  - Each reproduces from its one command, and the verdict is the same under two other hash seeds.
  - Each checks by hand under the inventions it names, with these caveats:
    - FC05 holds as its formal sentence is written; the counterexample is to I93's reading (ii).
    - FC20 and FC25 (b) also rest on choices not in the register (κ(⊥) = ⊥; an ill-formed λ scored as a failure of (F1)).
    - FC23 (b) rests on a footprint reading of "constraining".
    - FC77's conclusion survives its counterexample.
    - FC81 (d) and FC82 are corollaries of FC78's model and not separate findings.
    - The provenance findings (FC78, FC81, FC82, FC83) show what the definitions allow, with Θ supplied by hand (I90).
- **Bugs.**
  - One real one (§4.1): four places draw from, or pick the first element of, a set whose order depends on Python's hash seed. No verdict changes. The printed models of FC34, FC38, FC82 and FC83 do.
  - Reporting defects (§4.3).
  - The dependence of results on inventions that act inside the core (I83, I84, and others) is not carried to the results (§4.4, §5).
- **No bug** was found that creates a false counterexample or hides a real one: the predicates sampled against hand-made cases, the new-seed re-runs (R1, R2) and the two sensitivity runs (R5, R6) all agree with the record.
