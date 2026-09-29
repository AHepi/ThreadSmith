# S108 Part A round 2 - section 4 - variants computed

*Rule 5 of `S108 Part A round 2 - how the replies will be read, written before sending.md`, for section 4 (Parts XIII to XVI). Written 29 September 2026 by the one Opus 5.5 agent that, under decision S56, does the whole reading of round 2 (a departure from the rule's "at most one agent per section": S56, "It's capable of doing the whole thing on its own"). The work was begun by an earlier agent of the same job (its script `s108r2_s4_cases.py` and the switch `model/s108r2_s4.py`, committed in f601771), which a session restart cut off at about 00:24 UTC; this agent checked both, found the script complete, corrected one count (§3, below) and ran everything. An experiment on a copy (rule 11): nothing in the theory's text, formal core, claims, the program after round 4, round 1's files or round 1's program copies is written. "Candidate" or "explanation" for what the theory judges; "model" only for the program's folder or a small structure it builds (S43).*

Status: complete, 29 September 2026, with the whole-suite runs in the addendum (§8). Nothing ruled; nothing applied to the theory.

## Findings in brief

| variant (reply) | in scope (tabulation §7) | (E) (Acc) | being an explanation | what the computation adds or corrects |
|---|---|---|---|---|
| R2V4.1 C11 with D6.3's quantifier, (Suff) co-varied | yes; in part a repeat (new: 'some' co-varied; the two exempt readings, a gap of the share) | 0 | drops (case, history): 'every' 40 (10 cases), 'some' 60 (15), 'some-exempt' 48 (12), 'some-exempt-set' 48 (12) of 29 worked; generated 941 / 952 / 849 / 854 of 1,019 (SMALL), 1,590 / 1,617 / 1,361 / 1,385 of 1,686 (MID) | beyond 'every': 'some' adds the pole's forward candidate on C2 and C3, E5 (FC62's encoding), M5 and **the owner's two-part sign**; the exempt readings add E5, M5 and the two-part sign. (Suff) as conjectured fails on exactly the drops with its antecedent kept, on none co-varied. **S44 comes under the three non-'every' readings; S45 stands under all four** (the reply's claim, computed) |
| R2V4.2 C12 with (Suff) 'both' and S41 Q2's answer as an argument | yes; in part a repeat (new: the argument) | 0 | the student's declared copy ℰ_dec: Expl F now, T under 'rule', 'L17', 'both'; in (Suff)'s defeat set (L536) only under 'both' | the owner's Q2 answer, read as an argument (MP on r and r → ¬Expl), defeats (Suff) under 'both': computed. C12's flag S41 Q2 stands under all three shapes |
| R2V4.3 C13's fifth reading (e), at the content | yes | 0 | chains n ≤ 3 (3,208, each one fixed point under T′): (e) differs from ¬Dec at 210 last holdings, **25 with t held there**; (a) 494 / 247; (b) 174 / 87 | the reply's lemma ("every chain-wide reading returns the inherited value": 0 moves) **contradicted** on 25 held outputs (smallest: o1 with Sel's conditions not holding t, o2 a relay of o1 holding t: o2 inherits Sel, no holding holds t with Sel) |
| R2V4.4 histories built as chains | yes | 0 | on the chain histories (S108r2-4-I1) 24 of 24 worked accounts are explanations now, 0 under C13 (a); generated 1,019 of 1,019 and 1,686 of 1,686, 0 under C13 (a) | every worked and generated account has a named trial pair, so none "stays Dec" (the reply's second half contradicted as to the worked cases); C12 and "now" agree on every worked case under these histories, and part only on the student's copy, whose history the program computes (FC30.new1 (d)): C12's flag no longer rests on a hand-set history |
| R2V4.5 E9 with the set query Q_id | yes | **t1∘ψ: Acc T → F** ((A) fails at 2,768 of 3,456 pairs); t1 T | t1∘ψ no longer an explanation | L630.n3's Ans_p∘ψ = Ans_p and L630.s4's "none separates" false of this question (2,768 separating pairs): computed. The reply's "(E), Expl independent" **contradicted** for t1∘ψ |
| R2V4.6 L524.s2: a claim a predicate of the case alone | yes | – (no code) | – | one candidate, two values: ℰ_rev meets (E) on C_id and not on C1, C2, C3, C_H (the forward candidate on all five): read as one unindexed predicate, it takes both values: the block of L604.s1 [FROZEN], computed |
| R2V4.7 L522.s1's declared inputs struck | yes | 0 | 0 on cases | nearest statable (S108r2-4-I2): nothing usable by any j: the record argument of FC30.new1 (a) T → F, a premise alone T → F; (Suff)'s and (Nec)'s defeat sets empty for every j |
| R2V4.8 L526.s18 deleted: cut U admitted | yes | 0 | not defined where t is held: under U, 2 fixed points (Con histories) or none (Sel histories) on 24 of 29 worked (case, history) and on every generated account (1,019; 1,686) | DEP gains the cycle Live → (K2) → Live; "cut U usable again" **contradicted** (FC98's failure, on every account) |
| R2V4.9 D12.9 with four sentences reworded | **no** (repeats V4.8's formula; adds prose) | not implemented | – | e4.40 settled on the pole case (§6) |
| R2V4.10 D18.2 carrying traces and records | yes (e4.22) | 0 | the pair h / h′ (a trace at o2 or none): Expl now T / F, C13 (a) T / F | e4.22 **contradicted**: both definitions read the trace, and D18.2 as written keeps Θ's interpretation, which carries Prepares and Rec (D0.2) |

Discovered changes to which candidates meet (E): R2V4.5 (E9's t1∘ψ). To which count as explanations with (E) unchanged: R2V4.1 (the exempt readings new), R2V4.3 (e) (25 chains), R2V4.4 (the histories), R2V4.7 (defeat sets only), R2V4.8 (no value where t is held). Edges: §7 and the `.json`.

## 0. Set-up

| item | state |
|---|---|
| copy | `S108 Part A round 2 - computation/section 4 model/`, round 1's `S108 Part A - computation/section 4 model/` copied (every file identical at the copy but the two below); round 1's copy never written; its switch `S108_S4_*` (V4.1–V4.8 with their sub-choices) kept, so R2V4.1 and R2V4.2 are round 1's V4.1 and V4.2 under the sub-choices the reply names |
| round 2's switch | `model/s108r2_s4.py`: `S108R2_S4_VARIANT` ∈ {none, R2V4.5, R2V4.7}; hooks in `model/e9.py` (the question's query) and `model/args.py` (`usable`, and the accepted-premise test); everything else of round 2 is in the scripts (the variants read no code the suite runs, or are round 1's switches) |
| default unchanged | every switch off: `s104_external.py`, `s104_creative_transport.py`, `s106_cases.py` print the committed md5s (86a67664…, d473944e…, 043aeb36…), and `s106_cases.py` prints the same as in round 1's copy |
| scripts (in the copy) | `s108r2_s4_cases.py` (the worked cases, the owner's signs and the reply's small cases, §1–§10), `s108r2_s4_worlds.py` (generated worlds on round 1's own stream, seeds 108401 SMALL and 108405 MID) |
| runs | PYTHONHASHSEED=0, `python3 -B`, `timeout` on every run; outputs in `S108 Part A round 2 - computation/section 4 runs/` (`cases.txt`, `scripts/`, `worlds/`); the whole suite in `… - computation/whole suite/section 4/` |

A correction made by this agent to the cut-off agent's script: its §3 counted a difference at the last holding of a chain whether or not t is held there; a candidate meeting (E) is faithful on C, so held at its holding. §3 now also counts the differences with t held at the last holding (25 / 247 / 87 of 210 / 494 / 174).

## 1. The variants as implemented

| id | item | as implemented | as written? |
|---|---|---|---|
| R2V4.1 | D16.XV with S108-4-I1 | round 1's V4.1 (`S108_S4_VARIANT=V4.1`) with `S108_S4_V41_Q` ∈ {every, some, some-exempt, some-exempt-set} and `S108_S4_V41_SUFF=covaried` | yes; the two exempt readings added (the share names them; the reply did not reach them) |
| R2V4.2 | D16.XV with S108-4-I2 | round 1's V4.2 with 'rule', 'L17', 'both'; the reply's case ℰ_dec: the student's copy's holding as FC30.new1 (d) computes it, j = Assessor(MP; r, r → ¬Expl_dec) | yes |
| R2V4.3 | C13 read at the content (e) | on every chain of 1 to 3 holdings (held, trace, Sel's conditions at each, each later holding a relay of an earlier one or not), cut T′: (e) := some holding held with Sel's conditions or a trace (S108r2-4-I3) | nearest statable: "a holding of t's content" read as every holding of the chain |
| R2V4.4 | I90 | o1 a selection on (1, b0) where (1, b0) ∈ C and t is faithful there, else declared; o2 a relay of o1; cut T′ (S108r2-4-I1) | yes |
| R2V4.5 | E9's query | `e9.question` returns the question with Q_id (the set query on x1_3, x2_3; R2-4-I5) | yes |
| R2V4.6 | L524.s2 | no code: Acc of one candidate at several contracts, read as one predicate (R2-4-I6) | computed as a reading |
| R2V4.7 | L522.s1 | `args.usable` false for every α, no premise accepted (S108r2-4-I2) | nearest statable of "not statable" |
| R2V4.8 | L526.s18 | cut U (the program's `rd="U"`) in place of T′ on the worked and generated (candidate, history) | yes |
| R2V4.9 | D12.9 + four sentences | not implemented (tabulation §7: repeats V4.8's formula, adds prose; rule 4); e4.40's settlement computed (§6) | – |
| R2V4.10 | D18.2 | the pair h / h′ of §10; D18.2 read as written | computed as a case |

## 2. The worked cases, the owner's cases and the reply's small cases (rule 5.1)

`s108r2_s4_cases.py` (output `section 4 runs/cases.txt`): round 1's 29 cases (the case script of the written-in step with round 1's additions; the owner's two-part and one-part signs among them), hand-set histories H0, Dec, Con, Sel, rCon, rSel (round 1's, I90) except where a variant sets them.

| variant | worked cases | the owner's cases |
|---|---|---|
| R2V4.1 | (case, history) whose being an explanation drops: every 40, some 60, some-exempt 48, some-exempt-set 48 (cases 10 / 15 / 12 / 12) | the two-part sign (S44): slots none under 'every'; ['r','u'], ['r'], ['r','u'] under the others: Expl T under 'every', F under the three others (Con history), with (Suff) as conjectured failing there with its antecedent kept and holding co-varied. The one-part sign: slot ['k'] under all four. The hand-turned vane (R3-Q1): slot under 'every' and 'some', none under the exempt readings |
| R2V4.2 | ℰ_dec (the student's copy): Acc T, Dec T ([{'o1': 'Con'}]); α usable, not using (E), rules out Expl | – |
| R2V4.3 | see §3 | – |
| R2V4.4 | 24 of 24 accounts have a named trial pair; on the chain every one is an explanation now; 0 under C13 (a) | the pole: FC30.new1 (d)'s chain with o2 a relay: [{o1: Con, o2: Con}], Dec F, Expl T, C13 (a) F; o2 not a relay (as FC30.new1 (d) computes the student's holding): [{o1: Con}], Dec T |
| R2V4.5 | E9: t1 Acc T; t1∘ψ (A) F, Acc F (`s106_cases.py`: the only line that moves; FC-E and CT unchanged) | – |
| R2V4.6 | ℰ_fwd Acc T on C1, C2, C3, C_H, C_id; ℰ_rev F, F, F, F, T | – |
| R2V4.7 | the record argument of FC30.new1 (a): usable T → F; rules out Expl(ℰ_fwd) T → F; a premise alone usable T → F | – |
| R2V4.8 | T′: one fixed point on every (case, history); U: Con and rCon 2 fixed points on 24, 1 on 5; Sel and rSel none on 24, 1 on 5 | – |

FC-E1–E5 and CT1–CT8 (rule 5.2, 5.3): `s104_external.py` and `s104_creative_transport.py` print the same under R2V4.5 and R2V4.7 as off (`section 4 runs/scripts/`); R2V4.1–R2V4.4 and R2V4.8 read hand-set or chain histories the scripts do not build, R2V4.6 no code; the bridge (FC84.new1) builds no candidate (as in round 1).

## 3. R2V4.3 (e), on chains

3,208 chains (n ≤ 3), one fixed point each under T′. Holdings where ¬Dec(t) ∧ (Sel ∨ CT) under a reading differs from ¬Dec(t):

| reading | all last holdings | with t held there | smallest with t held |
|---|---|---|---|
| (e) at the content | 210 | 25 | n = 2: held (0,1), no trace, Sel's conditions at o1 only, o2 a relay of o1: fixed point {o2: Sel} |
| (a) at the holding (round 1) | 494 | 247 | the same chain |
| (b) along transfers (round 1) | 174 | 87 | the same chain |

The reply's lemma is contradicted on 25 held outputs; every reading of C13 moves the same smallest chain, where a relay inherits a selection made at a holding that did not hold t (the chain model's bits are independent; whether such an occurrence stands in a history is I90's).

## 4. The generated worlds at scale 4 (rule 5.4)

`s108r2_s4_worlds.py` on round 1's stream (SMALL: 17,280, 1,019 accounts; MID: 25,920, 1,686), 4.5 s and 8.9 s. Round 1's 'every' counts reproduce (941; 1,590).

| variant | SMALL | MID | smallest |
|---|---|---|---|
| R2V4.1: accounts no longer explanations (every / some / some-exempt / some-exempt-set) | 941 / 952 / 849 / 854 | 1,590 / 1,617 / 1,361 / 1,385 | ports 1, dom 1, comps 1, B 1, edits 1 (E_enc-built) |
| R2V4.1: (Suff) as conjectured fails, antecedent kept / co-varied | = the drops (3,764 / 3,808 / 3,396 / 3,416 (case, history)) / 0 | 6,360 / 6,468 / 5,444 / 5,540 / 0 | – |
| R2V4.4: accounts with a named trial pair; explanations on the chain; under C13 (a) | 1,019; 1,019; 0 | 1,686; 1,686; 0 | – |
| R2V4.8: fixed points under U (Con, rCon / Sel, rSel) | 2 on every account / none on every account | the same | – |

R2V4.2 is round 1's V4.2 (1,019 admitted, MID 1,686; not rerun); R2V4.3 is computed on chains (§3); R2V4.5 reads E9 only; R2V4.6, R2V4.7 read no candidate's Acc or Dec. With section 2 (its §5, §7.2): C6 = C11 on every generated candidate under each quantifier, so C11's counts here and C6's there are one computation of the same reading.

## 5. The readings round 1's candidates rest on (rule 5 (1))

| candidate | reading | admits / drops under each choice | flags |
|---|---|---|---|
| C11 (V4.1) | S108-4-I1: D6.3's quantifier × (Suff) kept / co-varied | drops, worked: 10 / 15 / 12 / 12 cases (every / some / some-exempt / some-exempt-set); generated above; admits nothing | S45 stands under all four; S44 comes under 'some', 'some-exempt', 'some-exempt-set' (the owner's two-part sign drops), goes under 'every'; the (Suff) shape moves no flag (kept: (Suff) as conjectured fails on the drops; co-varied: holds) |
| C12 (V4.2) | S108-4-I2: 'rule', 'L17', 'both' | admits the student's declared copy under all three; only 'both' puts it in (Suff)'s defeat set, where the owner's Q2 answer read as an argument defeats (Suff) | S41 Q2 stands under all three |
| C13 (V4.3) | S108-4-I3: (a), (b), (c) and the reply's (e) | drops at held last holdings: (a) 247, (b) 87, (e) 25 of 3,208 chains; (c) (inherited provenance) 0 (round 1); under R2V4.4's histories (a) drops all 24 worked and all generated accounts | none under any reading (no owner's case turns on a relay) |
| C12, C13 | I90 (R2V4.4) | on chain histories: C12 = now on every worked case; C13 (a) drops every account (all reached by a relay) | as above |

## 6. Round 1's claimed-only edges of the share (rule 5 (2))

| edge | settlement computed | standing | what shows it |
|---|---|---|---|
| e4.22 V4.3 (D16.XV) constrains D18.2 | the pair h (trace at o2) / h′ (none), the pole's forward candidate; D18.2 as written | **contradicted** | Expl now T / F and C13 (a) T / F on the pair: both definitions read the trace; D18.2 maps preserve ≺_h and Θ's interpretation, and D0.2 lists Prepares and Rec among Θ's primitives, so h ↦ h′ is no D18.2 map; nothing is specific to V4.3 and D18.2.v1 adds what D18.2 already carries |
| e4.40 V4.8 changes with L572.s2, L574.n4, L576.s1, L576.s4 | the pole case, 𝒯 = {t, t_ab} and {t, t_ab,H} (S108r2-4-I4), at the 2 unseen pairs of C | **computed** for L572.s2 and L574.s5; **independent** for L574.n4; **not settled** for L576.s1, L576.s4 | with {t, t_ab,H}: L572.s2's condition (a surviving differer) at 0 pairs, V4.8's Underdet at 2, the survivors agree at 2 (L574.s5: "the population fixes it"): V4.8 calls a value underdetermined where survival on H separates t from every differer; with {t, t_ab} all agree. L574.n4's route (t_ab survives at every unseen pair, t_ab,H at none) is the same under V4.8. L576.s1 ("wherever its population admits an alternative") and L576.s4 turn on reading "admits": not settled by computation |

## 7. The edges (the reply's rows, each marked; then added)

| id | variant | kind | item [mark] | standing | what shows it / what would settle it |
|---|---|---|---|---|---|
| R4E01 | R2V4.1 | constrains | (Suff)'s shape: D16.XV [S4]; L61 [S1], L536 [S4] | computed | kept: (Suff) as conjectured fails on every drop; co-varied: holds (§2, §4) |
| R4E02 | R2V4.1 | changes with | D6.3's quantifier, I136 [S2] | computed | the drops per quantifier (§2, §4); the two-part sign under the three non-'every' readings |
| R4E03 | R2V4.1 | changes with | L17.n2, L49.n3, L61.n2, L69.n3 [S1] | computed | each writes being an explanation as Account ∧ ¬Dec(t), which C11 narrows on the drops |
| R4E04 | R2V4.2 | blocks | (Suff) as L536 states it [S4] | computed | under 'both' the Q2 argument defeats (Suff) for j (ℰ_dec in Def(L536), Expl ruled out) |
| R4E05 | R2V4.2 | constrains | FC30.new1, FC23.new2 [claims] | computed (round 1's suite; the whole suite §8) | – |
| R4E06 | R2V4.3 | constrains | D12.4 [FROZEN] | computed | (e) departs from D12.4's inherited provenance on 25 held relays (§3) |
| R4E07 | R2V4.3 | independent of | X:Expl on chains (the reply's lemma) | **contradicted** | 25 held outputs move (§3) |
| R4E08 | R2V4.4 | constrains | I90 | computed | on chain histories every account is an explanation; the separation of C12 from now rests on FC30.new1 (d)'s computed history |
| R4E09 | R2V4.5 | constrains | Argument 2, L562.s3 [S4] | not settled by computation | Argument 2's text is not read by the program |
| R4E10 | R2V4.5 | moves | FC103.new1; L630.n3, L630.s4, L630.s5 [S4] | computed (L630.n3, L630.s4; FC103.new1 in §8); L630.s5 not computed | Ans_p∘ψ ≠ Ans_p at 2,768 of 3,456 pairs; 2,768 separating pairs |
| R4E11 | R2V4.5 | independent of | X:(E), X:Expl | **contradicted** | t1∘ψ: (A) fails, Acc T → F |
| R4E12 | R2V4.6 | blocks | L604.s1 [FROZEN] | computed | ℰ_rev: Acc T on C_id, F on C1–C_H: an unindexed predicate takes both values |
| R4E13 | R2V4.6 | changes with | L606.s2–s4, L608.s1–s2 [S4] | not settled by computation | sentences the program does not read |
| R4E14 | R2V4.6 | moves | X:(Suff), X:(Nec) | not settled by computation | one unindexed defeat set each: a reading of D16.XV, no code |
| R4E15 | R2V4.7 | blocks | D16.XV's shapes and note [S4] | computed (nearest statable) | X_j empty: no defeat of (Suff) or (Nec) for any j |
| R4E16 | R2V4.7 | constrains | L522.s2 [S4] | not settled by computation | a sentence the program does not read |
| R4E17 | R2V4.8 | blocks | L526.s17 [S4] | computed | DEP gains Live → (K2) → Live under U; T′ none |
| R4E18 | R2V4.8 | constrains | FC32.new1 (b), FC98 (c) [claims] | computed (§8) | under U no unique provenance on any account |
| R4E19 | R2V4.8 | changes with | L598.s2, L596.s1 [S4] | not settled by computation | sentences |
| R4E20 | R2V4.9 | constrains / changes with | L574.n4, L574.s5; L572.s2, L576.s4 [S4] | as e4.40 (§6) | – |
| R4E21 | R2V4.9 | independent of | X:(E), X:Expl | computed (round 1's V4.8: 0 moves) | – |
| R4E22 | R2V4.10 | constrains | D18.2 [S4], FC100 | contradicted as to D18.2 (e4.22, §6); FC100 unchanged (off) | – |
| R4E23 | R2V4.10 | changes with | D0.2's Rec_h′ (I165) [S1] | computed | D18.2 already preserves Θ's interpretation, which carries Rec (D0.2) |
| N41 (added) | R2V4.8 | moves | X:Dec, X:Expl | computed | under U, Dec has two values or none on every account where t is held (24 of 29 worked; every generated) |
| N42 (added) | R2V4.4 | moves | C13 (a)'s admits | computed | 0 of 24 worked and 0 of every generated account on chain histories |

## 8. The whole suite (addendum)

Run by this agent with `tools/sonnet_harness/run_claims.py` (a script, not a Sonnet worker and verifier: a departure from the rule's harness clause, recorded in the map's §0; S55, S56: cost), scale 4, time cap 45, compared with the round-4 record (key after_round4). Runs: off; R2V4.1 with 'some', 'some-exempt', 'some-exempt-set' co-varied; R2V4.5; R2V4.7. Results (`S108 Part A round 2 - computation/whole suite/section 4/`): off 133 / 2 / 7, no difference; R2V4.1 co-varied under 'some', 'some-exempt', 'some-exempt-set': each moves FC23.new2 and FC30.new1 (131 / 4 / 7); R2V4.5: FC103.new1 (132 / 3 / 7); R2V4.7: 14 claims about arguments, ruling out and the defeat sets (119 / 16 / 7). The map's §5.

## 9. Inventions (S36)

| id | choice | other choices |
|---|---|---|
| S108r2-4-I1 | R2V4.4: a case has a named trial history where (1, b0) ∈ C and t is faithful there; o1 a selection on it, else declared; o2 a relay | the case's own trial histories (the pole's grids, E9's H0) as the reply names them: on every worked account both give a trial pair |
| S108r2-4-I2 | R2V4.7: "not statable" read as no declared input, so no usable step and no accepted premise | the reply's "not statable" kept: then no value computed |
| S108r2-4-I3 | R2V4.3 (e): a holding of the chain holds t's content; (e) = some holding held with Sel's conditions or a trace | the content's holdings read from D11.2 across histories (not built) |
| S108r2-4-I4 | e4.40: 𝒯 = {t, t_ab, t_ab,H} on the pole (round 1's FC80 (d) shapes) | other alterations |

The reply's inventions used as it states them: R2-4-I1 (the quantifier pair), R2-4-I2 (Q2 as an argument), R2-4-I5 (Q_id), R2-4-I6 (unindexed predicate), R2-4-I7 (the four sentences), R2-4-I8 (D18.2.v1, not needed: §6).

## 10. Unsure

- R2V4.3's 25 chains, and C13's drops on them, rest on the chain model's independent bits (a selection's conditions at a holding that does not hold t); I90 decides whether such a history stands.
- R2V4.4's histories are this agent's (S108r2-4-I1); with them every account has a trial pair, so the result "every account is an explanation" is by construction of the history, as round 1's §6.3 warns.
- R2V4.7 and R2V4.8 are computed at the nearest statable reading; the reply calls R2V4.7 "not statable".
- e4.22 is settled by argument from D18.2's words and D0.2's list, with the pair computed; no φ was enumerated.

Computed by one Opus 5.5 agent under rule 5 and decision S56, 29 September 2026. Nothing ruled.
