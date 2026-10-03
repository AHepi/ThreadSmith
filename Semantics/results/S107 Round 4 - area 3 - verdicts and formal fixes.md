# S107 Round 4 - area 3 (L373-L632, Parts IX to XVI): verdicts and formal fixes

*Checker of area 3 under rule 5 of `results/S107 Round 4 - how the replies will be read, written before sending.md` and its addendum (both read whole first): a fresh Opus 5.5 agent that built nothing of this round, 28 September 2026. Findings: the 24 the tabulation (`… tabulation of the replies, before any ruling.md`, §0, §3) assigns to area 3, and item K1 (the winter-myth knock-on; addendum 1: L397 is area 3's), each passage read whole in its `.response.txt` (breaker r74-r75, r88-r89, r104-r105, with r33, r83 for K1; maths_words r3, r17, r20-r21, r30-r33, r38, r66, r85-r91, r106-r107; structure r10, r24-r39, r49-r50, r56, r60-r62, r70-r74, r84-r90, r101-r108, r110-r112, r118-r119; cases r123-r134, r171-r172). Text under review: `tests/106 The semantics, standing alone, without the written-in test.md` (md5 c7af964c329ab7959243405d394e6574), not written. Maths: `results/S106 The written-in test taken out/` (core 40d7c80ec78574794962fece34a4cb51, claims c0884083daae9b95be0c36d111d71019), not written. Program copy: `results/S107 Round 4 - maths after the reading/area 3 model/` (copied from `model after S106/`, all 23 files md5-equal before any change). Runs: `… maths after the reading/area 3 - runs.txt`. Text changes: `… area 3 - text changes.json` (none). Expected claims for the harness: `… area 3 - expected claims.json`. Decisions S20-S52 read (S52 keeps round 4's reading going); S23, S40, S41, S43, S44, S45, S47 bind every row. "Model" here means only a small structure the program builds, or the program's folder; for what the theory judges, "candidate" or "explanation" (S43).*

Codes (as rounds 2 and 3): **M** holds against the maths or the program; **W** against the words; **I** against an invention only; **N** does not hold. Rule 3: every computation a reply marks not run was run before its row (runs §3-§6). Rule 10: agreement among replies counts for nothing.

## 1. Verdicts (one row per finding)

| # | finding | lines | v | why (one line) | fix |
|---|---|---|---|---|---|
| 1 | B14 | FC14, FC32.new1 (L526) | M | both read the core by lists of places ending in older cores; sandbox layout (run, §3): FC14 NT, FC32.new1 FileNotFoundError; a copy away from the S106 folder (run, baseline here) reads `formal core, after round 3.md` without saying so | F1 (code). B14's relative "maths/formal core, now.md" run: works only from the sandbox's root (cwd-dependent) |
| 2 | W6 | FC32.new1 | M | as row 1 | F1. P4 run as written: still FileNotFoundError (HERE/../../maths lies above the sandbox's root) |
| 3 | S1 | FC14, FC32.new1 | M | as row 1 | F1. P7 run: works in the sandbox; from a copy under results/ still reads round 3's core |
| 4 | S2 | D18.1, D13.3, D12.2; `DEP` | M (Build); N (Con) | D13.3 and L405 (since R3A3-T4) read Held_ℓ(o,c) outright; DEP["Build"] kept a staged (R), L405's old "a represented organization", so its reading U ("as worded") read words the text no longer has, and K staged them; Con's staged (R) is L197's "available as a represented target", which T, T′ read as Held (dep_edges) | F2 (DEP["Build"], D18.1's note). P2 run as written (§3): statuses unchanged, U's cycle becomes (R) → Sel → (R); its Con edge not taken (L197) |
| 5 | S4 | D0.2, D11.3; `D0_2`, DEP["Episode"] | M | D0.2 lists "subhistory" among primitives "stated, not defined"; D11.3 defines it (I151: "subhistory closed under the interpretation"); DEP kept it a sink | F3. P6 code run as written: statuses unchanged |
| 6 | S6 | D16.XV, D0.2; DEP["DefeatConds"] | M | D0.2 claims to list what the core uses and neither defines nor lists; D16.XV's Work, 'without loss', 'operates on', 'fails to capture', 'not creative' ("no definition", D16.XV) are absent, and DEP["DefeatConds"] omitted them, so FC32.new1 (c) could not see them | F4 |
| 7 | S-δ | D9.10 (L377) | M | D9.10 writes δ for the alleged defect (L377's letter) and δ_c for ℰ_c's designation (I20), c there a criticism, not an organization; elsewhere δ's subscript names the organization (D3.1 δ_D, D5.3 δ_E, D14.7 δ_c, c a content), which the text never uses (δ occurs only at L377) | F5 (D9.10 alone). P9 (I20's letter renamed in nine definitions and the program's node) not taken: the clash is in one paragraph |
| 8 | S-κ | D16.XV (Elim) (L540) | M | κ is D5.1's value maps (κ_{k,v}; D6.10, D8.new1) and (Elim)'s kind-label κ(ℰ) | F6 (P8 taken) |
| 9 | W5 | D16.XV, L536, L538 | M (program) and I | "an argument not using (E)": the text does not fix the symbol or the instance; no register entry records it; D16.XV writes the symbol ((E), Acc ∉ Uses(α)); the program read the instance (`"Acc_" + name not in uses(a)`), not the symbol as W5 says; run (FC30.new1 (h)): the readings part on an argument whose only (E)-use is Acc(ℰ′) | F7; R4A3-01 (register) |
| 10 | B12 | L429, L447-L449; D13.8, D14.7 | N | (EX) and CompleteCritical are L447-L449 and L429 as written (a conjectural objection: a criticism, D9.10); FC32.new1 (f) already computes (EX) ⇝ Crit through CCE and Con, CT, Episode not; run (§4): on (a1) Con, Build hold and CreateEx fails at CCE's criticism clause under all 1,024 Θ-values of its other conjuncts, on (a2) it can hold; Q6 asks "Can something be created" (Con, Build, (G)); S47: the maths asks the agent nothing, a criticism is in CCE when the agent asked (D13.8's note) | none. FC84.new3 not taken: its content is FC32.new1 (f) with FC84.new1 (a1); the rest of CreateEx is Θ's (a hand-set tag, lesson S39) |
| 11 | S-d | D7.4, D12.6, D14.8, D15.6, D16.1, D16.3 | N | no defect claimed ("The text needs every one"); DEP holds them; testing them needs Θ; D14.8 is values (S33, S34: the owner's) | none |
| 12 | S-f | "Dependence", C, program names | N | none claimed: L526's "(E) depends on those (D18.1)" and D18.1's title keep the two Dependences apart; D15.2's note makes Part XII's letters local; the program's scopes are disjoint | none |
| 13-16 | B-N3, W-N3, S-N3, C-N3 | N3: L380, L383, D9.10 | N | (K1) Bearing ⟺ Account(ℰ_c) is L380 and D9.10; S45's "The theory changes everywhere the test is used" gives a slot connection bearing where it meets the rest of (E) (FC107, suite: Acc yes, NC1 no); L383 keeps its truth: C-N3's NC5 run as written (§5): Acc no (Dep no: one pair, no contrast), NC1 no, round 3's (E) no; what such a criticism leaves open is parked (P8) | none |
| 17-20 | B-N4, W-N4, S-N4, C-N4 | N4: L536 | N | (Suff)'s range holds slot candidates (D16.XV's [S106] note): S44, S45 hold them explanations, "Just not a good one"; Q2's ¬Dec(t) kept (FC23.new2 (f), suite); L536's "the four" is D6.8's headings (area 1, FC31) | none |
| 21 | R3A3-T1 | L397 | N | "more" is R3A3-T1 settling I166 in the text (rule 6): Q23 with L393's "a claim j has never taken up is not live for j"; L397 now writes D9.6's clause; FC72 (f) (suite): a premise not taken up rules nothing out | none |
| 22 | R3A3-T4 | L405 | N | "less" is I162's cut T′ (Q1 ruled, round 2), which R3A3-T4 wrote into L405; FC98 (c)-(e) compute the cuts; the program's graph kept L405's old wording (row 4) | none here (F2 answers S2) |
| 23 | R3A3-T5 = W3 | L375 | N | L375 writes D11.3's well-foundedness since R3A3-T5 (I169 settled, rule 6), "acyclic" beside the stronger formula; the witness "o_m ≺ o_n iff m<n" is well founded when indexed by ℕ: it must descend, as FC98.new1 (a), FC98.new2 (a) build it (suite) | none |
| 24 | S106-T11 | L397 | N | the pointer names D9.7's defined block (I39) where the words named NC1's undefined reading (I24, I28); B6: "Residue, harmless", "a self-pointer" | none |
| 25 | K1 (the winter-myth knock-on) | L317 [2], L397 [3] | settled | §1a: computed (FC72.new2); the owner's words settle the older question (S44, S45 with S28, S21, S27, S41 Q23, S23): no owner question, no text change | FC72.new2 (a new test claim); R4A3-02 (register) |

**Counts.** M 9 (rows 1-9; rows 1-3 one point); W 0; I 0 apart from row 9's; N 15 (rows 10-24); K1 settled. No proposal of area 3 is flagged by the tabulation (S40, S41, S44/45, S47: none).

### 1a. K1, the winter-myth knock-on (addendum 2)

S106-T8 (L317) and S106-T10 (L397) deleted "that it assumes its own answer, or"; the one no-test ground left is "that at a pair of \(C\) it gives what a claim the assessor tentatively accepts excludes" (L317; L397 the same). No reply names the myth (tabulation §3.5). The replies' points on these lines (R3A3-T1, S106-T11: rows 21, 24; held: B (f) r83, B6 r33, W r30, r32, S (a) r10) find nothing against them.

**What the theory now says, computed** (FC72.new2, new; encoding R4A3-02: the noon sun's height and the temperature, the hemisphere a boundary N/S, the time of year an edit 1 = June / dec; the tilt gives the sun's height by hemisphere and month; the myth gives the same seasons everywhere; runs §6):

| part | computed |
|---|---|
| (a) the Greeks' contract C_G = {(1,N), (dec,N)} | tilt: (E) yes, no slot. Myth with its answer written in (one part, the bargain: warm in June, cold in December): Slot (every) yes, pins at both pairs; (E) after S106 yes; round 3's (E) no under every reading. Myth as told (bargain places Persephone; grief sets the cold): no slot under 'every', (E) yes under both |
| (b) offered one in place of the other (Offered, I33) | conflict pairs {(1,S), (dec,S)}, both outside C_G; rivals; kind ii (either myth): for an assessor who rules out neither, each easy to vary against the other (D10.4) |
| (c) no test (L397, D9.6-D9.8) | j0 takes up the finding "Slot(myth)" (computed): nothing rules out Acc(myth) or Acc(tilt): the problem stands. j1 also takes as given "Slot(myth) → ¬Acc(myth)" (the deleted ground; (E) does not give it: Slot and Acc both computed yes): MP rules the myth out for j1, not blocked (the premise is not the denial): j1's choice (L397 "the ruling out is a choice the person using it made"; S28); no problem for j1. j2 holds Slot ∧ ¬Acc as one premise: blocked (D9.7), nothing ruled out |
| (d) a finer contract with the south | myth: (F1), (F2), (A) no, (E) no; tilt (E) yes; kind i; a record of June in the south ('cold'; the myth gives 'warm') with (A)'s premise rules out the myth, not the tilt, for whoever takes them up (L317, K2, K3) |

**Do the owner's words settle the older question** (file 96's second question: does finding by argument that a candidate assumes its own answer count, like a conflict, on a question about the world; file 93's first choice: should such a failure "count as established")? **Yes.**
- S44, S45: "A written-in answer never stops something being an explanation. It only makes it a bad one" (the description the owner chose). So the finding is not a failure of (E): (a), (c) j0.
- S28 ("That "ruling out" is a choice that was made"), S21 ("Resolution is up to the person"): a person may still rule the myth out on that ground by taking a claim as given; that is the person's choice, not an exclusion the theory makes: (c) j1.
- S27, S41 (Q23): a conflict with a claim taken as given, even a bare one, rules out with no test; that ground stands (L317, L397).
- S23 forbids "established"; S28: nothing is settled. File 93's wording of the choice does not survive; its "If not" branch (the two pose a problem outside the range, each easy to vary against the other) is what (b) computes.
- The orchestrator's reading (addendum 2) holds, computed. Whether the myth's link was only declared is its history (Q2, D16.XV), not what examining it finds (not computed: Θ). What makes it a bad one, the questions it leaves open, is parked (P8).

No owner question (rule 12: the owner's words settle it). No text change: L317 and L397 already say it (S40). No formal change. Not a move.

## 2. Formal fixes (old → new; ids kept)

| fix | item | old | new | answers | counted |
|---|---|---|---|---|---|
| F2 | D18.1, the T′ item and the note | "T′: Con's 'available as a represented target' (D12.2) and Build's 'represented organization' (D13.3) := Held at o' ⪯ o in the episode"; the r3 note "Con → CT, Episode; … Build → ExplUse → (E) (I178)" | "T′: Con's 'available as a represented target' (D12.2, L197) := Held at o' ⪯ o_t in the episode; Sel's exclusion as before. Build reads Held_ℓ(o, c) outright (D13.3; L405 since R3A3-T4), under every reading: Build → Held, ExplUse; ExplUse → (E)." The program's DEP["Build"]: staged (R) → Held | S2 (Build) | yes: the program's reading of a definition (DEP) |
| F3 | D0.2 | "… AtRest [I149]; Org_ℓ(h) and subhistory [I151]; q(o), …" ; "Below (D9.2) is defined." | "… AtRest [I149]; Org_ℓ(h) [I151]; q(o), …"; "Below (D9.2) and subhistory (D11.3, I151) are defined." DEP["Episode"] loses the sink 'subhistory' (D11.3 is node h) | S4 | yes: changed definition (D0.2; round 3's integration counted D0.2's classing) |
| F4 | D0.2 | (no entry) | append: "Used by D16.XV's shapes and defined nowhere (D16.XV says so of each): Work(kl) [(Elim), L540]; 'without loss', 'operates on' [(Prov) (ii), (iii), L542]; 'fails to capture', 'not creative' [(QF), L544]." DEP["DefeatConds"] gains Work, WithoutLoss, OperatesOn, FailsToCapture, NotCreative; classed in `D0_2_R4A3` | S6 | yes: changed definition (D0.2), a second change |
| F5 | D9.10 | ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_c), with t_c, Γ_c, δ_c supplied with c [I147] | ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_Conn), with t_c, Γ_c and δ_Conn, the designation of Qf(z,δ,p)'s query in Conn (D5.3, I20), supplied with c [I147]; δ alone is the alleged defect (L377) | S-δ | no: notation, content unchanged (as the primed ids, round 3) |
| F6 | D16.XV (Elim) | "a kind-label κ(ℰ) ≠ κ(ℰ') ∧ Work(κ)" | "a kind-label kl(ℰ) ≠ kl(ℰ′) ∧ Work(kl)"; κ stays D5.1's value maps (I14) | S-κ | no: notation |
| F7 | D16.XV (unchanged); the program's reading | `"Acc_" + name not in uses(a)` (the instance) | "(E), Acc ∉ Uses(α)" read as written: no leaf of α uses Acc of any candidate (`not_using_E`, reading "symbol"; "instance" kept for comparison) [R4A3-01] | W5 | yes: the program's reading of a definition |
| F1 | FC14, FC32.new1 (code) | each claim's own list of places, falling back to the cores after round 3 and round 2 | one list (`model/corefile.py`): beside the program's folder; its committed folder from a copy under results/; maths/ beside model/ (the sandbox); name and md5 printed; no older core read; none found: the part that reads it is not tested (FC32.new1's other parts still computed) | B14, W6, S1 | no: a path, not a reading of a definition (round 3's precedent) |

Re-based, not counted: FC98 (a) statement "(L197, L405)" → "(L195's Rep, L197) …; Build reads Held (L405 since R3A3-T4)"; FC98 (a′) "(R) inside Sel, Con, Build staged" → "inside Sel and Con …, Build reading Held under each"; results unchanged (cycle (R) → Con → (R); K, T, T′ none). FC32.new1 (c) classes D0_2_R4A3 beside D0_2_R3A3.

## 3. Code (in `area 3 model/`)

| file | change | fix |
|---|---|---|
| model/corefile.py (new) | `formal_core()`: the one list of places; (path, md5) or (None, places tried) | F1 |
| model/claims_a.py | FC14 reads through `formal_core()`, prints name and md5 | F1 |
| model/claims_r3a3.py | `core_def_ids()` → (ids, "name (md5 …)") or (None, places); FC32.new1 (a) not tested when none, (b)-(f) computed; (c) classes `D0_2_R4A3` | F1, F4 |
| model/claims_b.py | DEP["Build"] staged (R) → "Held"; DEP["Episode"] without 'subhistory'; DEP["DefeatConds"] + the five; `D0_2_R4A3`; dep_edges docstring; FC98 (a), (a′) statements; FC98 (b) look's text. `build_at` unchanged (below) | F2, F3, F4 |
| model/claims_s41.py | `USES_READINGS`, `not_using_E` (default "symbol"); `expl_ruled_out` and FC30.new1 (g) through it; FC30.new1 (h) new part: W5's argument under both readings | F7 |
| model/claims_r4a3.py (new), model/run.py (import) | FC72.new2: K1, parts (a)-(d) | K1 |

`build_at` (FC83's cuts) keeps round 2's reading of L405's old wording under U and K. Run (§3.6): read as Held under every cut, FC83 (a) finds a counterexample under K (held [1, 1], trace [1, 0], Sel's conditions [0, 1]: a first construction unrepresented under K, then a selection), K's own defect (FC98 (d)); not changed here: no finding asks it, and FC83 names round 2's cuts. For integration (§10).

md5s after area 3 (every other file as in `model after S106/`): model/claims_a.py eca4152440cdca32f52fe82633f5bf2c (was c1e323dd533dd60babccfcec20c9b269); model/claims_b.py a070ae7e7ad34b4a19808ac8731ac1ff (was 4d69c86f37e36a78b8222f9e5efcfe7e); model/claims_r3a3.py 85d8b1e8783515c46df0afc54ea8b0b6 (was 6a49482b69cb49598a0a03aa6ba021a8); model/claims_s41.py 88a94439b4d19c275c8655cb9f076cc2 (was f0611d34990664a342390068b427f57b); model/run.py 3532569a1eccf6f88200472f8ed5ec91 (was 1088045c37731cff5f18d6e906e19932); new: model/corefile.py 94619363af03e6b8c34431f491cdfca6, model/claims_r4a3.py 1b848683769783629269c09343f8da2f.

Whole suite, scale 4, cap 45 (runs §1): baseline on the unchanged copy 128 hold, 2 counterexamples, 7 not tested, of 137, every claim and part equal to `formal claims, after S106.json` (after_s106); after area 3: 129 hold, 2 counterexamples, 7 not tested, of 138, no error; against the record, FC30.new1 differs by its new part (h) (computed: as claimed) and FC72.new2 is new; no status changed; FC14 and FC32.new1 now read `formal core, after S106.md` (md5 40d7c80ec78574794962fece34a4cb51) from its committed folder (they read round 3's core from this copy before). Recorded for the harness in `area 3 - expected claims.json` (key area3_r4; 138 claims, parts as (label, kind, status)). Case scripts on the changed copy: outputs md5-identical to the records (86a67664a9a3584351fd4836a4140b69, d473944e74d2f349b1fdfb83277843cf, 043aeb3647a9004ae43009a7fed50b4e).

Harness job (rule 5.3), run after this hands back: `tools/sonnet_harness/specs/r4 claim suite, area 3 copy.json` (27 inputs with md5s: the copy's 25 files, the record, and the formal core after S106 that FC14 and FC32.new1 read; the whole suite compared with `area 3 - expected claims.json`, key area3_r4, counts H=129, CEX=2, NT=7, of 138; a spot re-run of ten claims). Checked here: `run_task.py --phase validate` under a run label of its own (a3-selfcheck: inputs ok, no command run), and the spot re-run by `run_claims.py` into the scratchpad (10 of 10 equal to the record, the copy unchanged); its brief printed under `--run r4-reading`.

## 4. Text changes (`area 3 - text changes.json`)

None. No finding of area 3 holds against the words (W 0); K1 needs none (L317, L397 already say what S44, S45, S28 say). Words outside formulas unchanged.

## 5. Inventions (provisional ids; rule 6: numbered at integration after I191)

| id | fills (line; item) | choice | other choices | why this one | used by |
|---|---|---|---|---|---|
| R4A3-01 | "an argument not using (E)" (L536, L538; D16.XV's Uses) | the symbol: no leaf or form of α uses (E), Acc of any candidate | the instance: no use of Acc(ℰ) for the candidate ℰ at issue (the program's reading before round 4; W5's "does not use (E) on ℰ") | the text names (E), not (E) on ℰ; D16.XV writes the symbol; the readings part only on an argument that uses Acc(ℰ′) (FC30.new1 (h)) | D16.XV; `claims_s41.not_using_E`; FC30.new1 (a), (b), (g), (h); FC23.new2 (f) |
| R4A3-02 | the myth about winter and the seasons (file 93, file 96; K1), encoded | target: ports sun ∈ {high, low}, temp ∈ {warm, cold}; c_sun by (edit, boundary) as the tilt gives it, c_temp warm iff high; edits 1 (June), dec; boundaries N (the Greeks'), S; query reads temp. Myth: one part writing the answer (a slot), or two parts (bargain places Persephone, grief sets the cold; π reads her place off the sun's height) | the myth's answer read off a calendar port; months finer than two; the myth's parts given no counterparts in the target (not encoded) | the smallest target on which the Greeks' contract and the south part the two, and both readings of "assumes its answer" can be computed | FC72.new2 |

## 6. Owner questions

None. K1: the owner's words settle it (§1a). B12: L429 and L447 settle that (EX) needs a critical episode; Q6 asked whether "something" can be created, which Con, Build and (G) give with no criticism (FC84.new1 (a1)); S47 is kept (the maths asks nothing; a criticism occurs when the agent asks). No line is held.

## 7. Parked

Nothing new. K1's "what makes the myth a bad one" and N3's "what a slot connection leaves open" stay under P8 (S33, S34).

## 8. Quotations relied on (rule 15; each found)

Text: L197 "is available as a represented target"; L317 "one that finds, by examining it, that at a pair of \(C\) it gives what a claim the assessor tentatively accepts excludes"; L375 "an acyclic causal precedence"; L377 "alleged defect \(\delta\)"; L383 "A criticism occurrence can exist when (K1) fails."; L393 "has never taken up is not live for"; L397 "read structurally (D9.7)", "Where such an argument uses a claim taken as given, the ruling out is a choice the person using it made"; L405 "prepares \(\operatorname{Held}_\ell(o,c)\) (D13.3, D18.1)"; L429 "A complete critical episode contains a recognized difficulty, a target available before its criticism, a conjectural objection, and a content-sensitive response."; L536 "an argument not using (E)"; L540 "a kind-label distinguishes two accounts". Decisions: S41 "Can something be created in a stretch of work like that", "Yes, it can"; S44 "In either case, it is an explanation. Just not a good one"; S45 "Yes, take the test out", "A written-in answer never stops something being an explanation"; S28 "is a choice that was made"; S21 "Resolution is up to the person"; S47 "The math doesn't ask for anything." Formal core: D0.2 "Org_ℓ(h) and subhistory [I151]"; D11.3 "a subhistory is a subset closed under the interpretation, with ≺ restricted"; D9.10 "ℰ_c := (Conn, Qf(z,δ,p), t_c, Γ_c, δ_c)"; D13.8 "hold a criticism (D9.10) because the agent asked, not because Con does"; D16.XV "'an argument not using (E)' := (E), Acc ∉ Uses(α)", "a kind-label κ(ℰ) ≠ κ(ℰ') ∧ Work(κ)"; D18.1 "Build's 'represented organization' (D13.3) := Held". Replies' quotations: as the tabulation's §2 found them.

## 9. Moves (rule 16, counted strictly)

| counted | n |
|---|---|
| formal: F2 (the program's reading of D13.3 in D18.1's graph), F3 and F4 (D0.2, two changes), F7 (the program's reading of D16.XV) | 4 |
| text | 0 |
| **moves** | **4** |

Not counted: F1 (a path); F5, F6 (notation, content unchanged); FC98 (a), (a′) and FC32.new1 (c) re-based; FC72.new2 and FC30.new1 (h) (a new test claim, a new test part); R4A3-01, R4A3-02 (register entries); K1 (settled; no owner question); nothing parked. If F3 and F4 are counted as one change of D0.2: 3.

## 10. Pairs of fixes that bear on one another (for integration, rule 7)

- F2 with `build_at` (FC83): DEP now reads Build as Held under every reading; build_at keeps round 2's cuts of L405's old words; read as Held, FC83 (a) is a counterexample under K (§3.6), the defect K was rejected for (FC98 (d)).
- F2 with R3A3-T4 (row 22) and area 2's findings on D6.3, D6.5 (DEP's Dep, Slot nodes): the same table `claims_b.DEP`, different entries.
- F3 and F4 edit D0.2 together; F4 uses F6's letter (Work(kl)).
- F5 (δ_Conn in D9.10) with area 2's N1 fixes (δ_v in D7.4) and S-δ's P9 (not taken): the letter δ.
- F7 and FC30.new1 (h) with area 1's `no_question_about_brief` and FC84.new1 (a3) in `claims_s41.py`: different hunks (mine: the import line, `uses`/`not_using_E`/`expl_ruled_out`, FC30.new1 (g) and (h)).
- F1 with area 1's layout note (its §3) and S49: `model/corefile.py` names the core the program formalizes; integration sets NAME and the committed folder to the core after round 4.
- `model/run.py`: my import line follows `claims_s106`, where area 2 added `claims_r4a2`'s: a conflict at merge (keep both).
- FC72.new2's id: areas 1 and 2 use FC84.new1 (a3), FC23.new4, FC23.new5, FC27.new1, FC42.new1; none clash.
- K1 (FC72.new2) with area 2's L317 (S106-T8): the addendum sent K1 here.
- Area 2's R4A2-T1 (L271: "the production contract" read as E1's \(C_1\), R4A2-01) with L536's same words, "a reversed calculation fails (F2) under the production contract.": no area 3 finding names L536's phrase (N4 is about (Suff)'s range), so no change here; the integrator's (tabulation §6.1; area 2's note).
- B12 (row 10) with area 1's R4A1-01 and FC84.new1 (a3): D13.8's note "because the agent asked".
- Noted, no finding: the formal core's quoted span above D9.7 still carries L397's old "read structurally as non-circular dependence reads identity (Part V)" (D9.7's [S106] mark records the change), as W4 (area 2) finds for D6.9's quote.
