# S108 Part A, round 1: the second checker on the critical review

*A fresh Opus 5.5 agent that built nothing of Part A, 28 September 2026. Rule 9 of `S108 Part A - how the replies will be read, written before sending.md`; the orchestrator's decision 1. Read: the orchestrator's decisions; the critical review (O1–O13); the rule; decisions S20–S53; the tabulation; the four "variants computed" files and their copies; the map (.md, .json); the candidate list. Not opened: `S108 Part A - Sonnet 5.5 trial/`. Nothing in the theory is changed (rule 11): no text, formal core, claim, program after round 4, rule, reply, tabulation, section file, review or decision was written. "Candidate" or "explanation" for what the theory judges (S43).*

## 0. Files

| file | md5 before | md5 after |
|---|---|---|
| `S108 Part A - the dependency map.json` | ded3aa4da812ecbc17fb0ef403bd035d | 7ce9b1c65b55487d79f0c1a427adc2d9 |
| `S108 Part A - the dependency map.md` | a4b5a90a835380c017bc265cf21dcb48 | 1da37cf057ff02047fdeb1ca740eb5d8 |
| `S108 Part A - candidate definitions of explanation.md` | 2a2e6739f497df483dc5a8d12a9cb136 | 6541dd847a158233662c895c7eb30c13 |
| `S108 Part A - computation/map/s108_map_build_second_checker.py` | new (a copy of `s108_map_build.py`, ff3aab7c…, each change marked `# 2nd checker (On)`) | 81f9a0e171787a1fd9ecff0624d464fc |
| `S108 Part A - computation/second checker/` | new: `owner_cases.py` (8554c261…), `o3_trace_extent.py` (54fbdbf4…), `runs.sh` (0ee787e2…), three outputs | – |

- The original builder rebuilds the committed map byte for byte (checked); the second checker's copy rebuilds the new map byte for byte (checked twice). The map is generated, so it was corrected in the builder, not by hand.
- Unchanged against HEAD (checked): the four section files and their copies (the runs import them with `python3 -B`; no file written, no `__pycache__`), the review (94a67923…), the rule (0909c53d…), the orchestrator's decisions (23714d21…), `records/Semantics - Decisions.md` (9c73d974…), the tabulation, the original builder.
- Runs: PYTHONHASHSEED=0, every run under `timeout`.

## 1. Rulings

(a) keep; (b) the review's fix; (c) a third fix.

| id | ruling | reason |
|---|---|---|
| O1 | **b** | Run (§2 A): with the change read as a boundary (FC28.new2's D_vane; the sign with B = {mon, tue}), V2.3 drops the owner's vane and two-part sign, and E_enc on each question, so nothing on either question meets (E); read as edits (M13, `claims_s106`) nothing moves. C5 flagged against S41 Q15 and S44 on that reading. |
| O2 | **b** | Run (§2 A): the two-part sign (S44's case) stays under V2.4 and V4.1 with 'every', in either encoding; drops under 'some', 'some-exempt', 'some-exempt-set'. The one-part sign is `claims_s106`'s companion (R3-Q1's side 1). C6, C11: S45; S44 only under the other readings. |
| O3 | **c** | The review's settle, run (§2 B): the program's trace is a label at o_t, so {o_t} is an episode and the record clause is idle; with the output's trace spanning an unrecorded change (Prepares asking h′ to hold the trace's occurrences, D13.3's tuple), V3.5 moves Dec T → F on every such held output under T′ and T. So e3.25a stays contradicted, conditioned on "the trace at o_t", and a computed e3.25c is added; C9 admits on that reading and stays unflagged (no decision touched). |
| O4 | **b** | Section 4's E4.5c shows no move; Acc ⇒ F1 ∧ F2 = Faithful_C(t), so C′ = C, t′ = t: no candidate meeting (E) is exposed. e4.29 → independent of; the L538.s2 finding is in map §6.3 for the records (the orchestrator's decision 2). |
| O5 | **b** | D13.4 states no reflexivity ("read with c fixed (L413) and … not claimed symmetric (FC85)"); FC85 (a) does. e1.08 split: blocks FC85 [claim]; changes with D13.4, D13.5. |
| O6 | **b** | The row's own evidence: "L211.s3 still holds formally". e2.13 → changes with (in effect). |
| O7 | **b** | The reply named L556.s3 only as "the nearest"; section 4's search found no FROZEN item holding "not using" or Uses. e4.25 → a 'none found' row; L556.s3 leaves §3. |
| O8 | **b** | e3.09b: problems move (grow), computed; the reply's direction contradicted. e2.04b: kept contradicted, retargeted to "every candidate realizing L299.s1 fails (E)"; V2.2's move of (E) is s04's, computed. |
| O9 | **b** | The four sentences write being an explanation, which V4.3 moves at relayed holdings (e4.18), as e4.01, e4.13 for V4.1, V4.2. e4.19a computed; e4.19b (FC25.new2, the reply's reason) contradicted. |
| O10 | **b** | Section 1 §9 names S41 Q6 as not computed. Added to C2 (row and plain words). |
| O11 | **b** | Computed from the map's own D18.1 ancestors and statement reads (followed through the parts they read): the seven the review names, and no other of the 17 (§3 C). |
| O12 | **b** | (a) and (c) added to map §6.3 as "not computed"; (b) as a row "edit or boundary". |
| O13 | **b** | `s108_s3_cases.py` l.11–12: 'Sel-parts' states "all but E's last component". e3.30a and §6.3 corrected; the note "counts = the population meeting (E), by construction of the history" added to §2 and §6.3 (V2.5, V3.5 tags, V3.6, V4.2, V4.3). |

Also corrected (the map's own): §6.2 said "15 of them are of the three variants not run"; it is 9 (e1.45–e1.51, e2.20, e2.21), now computed by the builder; the orchestrator's ruling on V1.6, V1.7, V2.8 is written in §6.2, §7 and the list's §3.

Counts now: 221 edges (computed 179, claimed only 31, contradicted 11); 4 'none found' rows; 32 claims named.

**Wrong in a section file, left as it is (the map is corrected):** section 4 §3 and §9 "the owner's one-part sign (S44)" (S44's case is the two-part sign); section 1 §8 and §9 "D13.4's reflexivity" (FC85 (a)'s, not D13.4's); section 3 §2's S108-3-I4 "the stated construction := … the base member's components" (true of t′'s runs; 'Sel-parts' states all but E's last component); section 3 §8's V3.5 "contradicted under D12.2's cut" (only for a trace at o_t).

## 2. The runs

**A. The owner's cases, the change as an edit and as a boundary** (`second checker/owner_cases.py` in the section 1, 2, 4 copies; output `owner cases - output.txt`). Acc (E); for V4.1, being an explanation with Dec F.

| case | none | V1.1 | V1.5 (I5) | V2.1 | V2.2 | V2.3 | V2.4 ('every') | V4.1 'every' | V4.1 other three |
|---|---|---|---|---|---|---|---|---|---|
| vane as edit (M13) | T | F | F | T | T | T | T | T | T |
| vane as boundary, Γ = {cP} / {cW,cP} | T | F | F | T | T | **F** | T | T | T |
| two-part sign as edit (ℰ_two) | T | F | F | T | T | T | T | T | **F** |
| two-part sign as boundary | T | F | F | T | T | **F** | T | T | **F** |
| one-part sign, edit or boundary | T | T | F | T | T | T as edit, F as boundary | F | F | F |
| E_enc on the vane's / sign's question, as boundary | T | T | F | T | T | **F** | F (a slot) | – | – |

**B. V3.5 with a trace spanning occurrences** (`second checker/o3_trace_extent.py` in the section 3 copy; the chains of section 3's `s108_s3_worlds.py`, with the output's trace from o_s to o_n, s ≤ n; Dec at the output, 'none' → V3.5):

| n ≤ 4, cut T′ (T the same) | chains | held output: Dec moves | not held |
|---|---|---|---|
| trace at o_t (the program; control) | 57,700 + 57,700 | **0** (section 3's) | 11,240 (section 3's) |
| trace spans an unrecorded change of contract | 90,144 + 90,144 | **45,072**, T → F: every one with a trace at the output | 39,304 |
| trace spans occurrences, no unrecorded change | 80,448 + 80,448 | 0 | 3,392 |

Smallest: n = 2, held [0, 1], trace at o2 from o1, C → C′ unrecorded. Under K and U (n ≤ 3) the spanning trace moves held outputs too (242, 830).

**C. The untouched middle definitions upstream of the explanation definition** (map §6.1): D6.9: (E), Expl, (Suff), (Nec) (D18.1); D11.2, D11.3: Dec, Expl, (Suff), (Nec) (D18.1); D6.8, D9.1, D9.2: D16.XV's node, so Expl, (Suff), (Nec) (D18.1); D5.7: Dec and (Nec) by their statements, Expl and (Suff) through Dec's. None of D8.new1, D10.3, D12.7, D12.8, D13.7, D14.1, D15.1, D15.2, D15.5, E9 by either route.

## 3. For the orchestrator

**Flagged candidates, as they now stand (for Part C):**

| # | variant | decisions it does not appear to agree with | on what reading |
|---|---|---|---|
| C1 | V1.1 (D1.4) | S44 | any (the two-part sign drops as edit or boundary) |
| C2 | V1.5 (D3.4) | S44; S41 Q15; S41 Q6 not computed | S108-1-I5 only |
| C5 | V2.3 (D6.4) | S41 Q15; S44 | the owner's change (wind, day) read as a boundary |
| C6 | V2.4 (D6.7) | S45; S44 | S45 any; S44 only with D6.3's quantifier other than 'every' |
| C7 | V2.5 (D12.1) | S41 Q2, in part | the hand-set history 'nothing tried' (P-S2-3): the link written from nothing; not the student's copy |
| C8 | V3.4 (D13.3) | S41 Q2 | S108-3-I2 only |
| C11 | V4.1 (D16.XV) | S45; S44 | as C6 |
| C12 | V4.2 (D16.XV) | S41 Q2 | any |

Unflagged candidates: C3 (V2.1), C4 (V2.2), C9 (V3.5), C10 (V3.6), C13 (V4.3).

**Non-candidate variants that sit against decisions** (list §3): V2.6 (S20); V2.7 (S27); V3.1 (S23); V3.3 (S28, S27, S41 Q23); V3.8 (S47 with S41 Q6; the reply asks the owner's yes or no). V4.4: the reply names S23; computed, no decision touched.

**Gaps for round 2, in the review's order:**
1. **The readings the candidates rest on**, under their other choices: S108-1-I5 (C2); edit or boundary for the owner's changes (C5); D6.3's quantifier (C6, C11); S108-3-I2, S108-3-I5 (C8); the trace's extent and the tag encoding (C9); S108-3-I4 with 'Sel-parts' (C10); S108-4-I1, I2, I3 (C11, C12, C13); the hand-set histories, I90 (C7, C9, C10, C12, C13).
2. **The untouched middle definitions upstream of (E), Dec, Expl, (Suff), (Nec)**: D6.9, D11.2, D11.3, D6.8, D9.1, D9.2, D5.7 (§2 C); then the other ten.
3. **The edges claimed only** (31): e1.02, e1.03, e1.14, e1.36–e1.40, e1.45–e1.51, e2.03, e2.06c, e2.07, e2.09, e2.11b, e2.16c, e2.19, e2.20, e2.21, e2.26, e2.33, e3.30b, e3.34b, e3.37b, e4.22, e4.40; nine are V1.6's, V1.7's, V2.8's (ruled: decision 3). Also: the places the program cannot compute (map §6.3); the suite's D6.4 blind spots (e2.38, e2.39); the bridge, E2, E3, E4, E7, which carry no candidate.

## 4. Unsure

- O1 and O2's S44 turn on readings (edit or boundary; the quantifier) that are the owner's to settle; the flags say only "on that reading".
- O3's trace extent is my encoding (the output's trace over o_s..o_t; the other occurrences keep the program's). A round-2 agent may state another.
- V3.1's flag against S23 may also be read against S41 Q23 ("Yes, it's an argument": a single claim used alone counts); whether "p" ruling out "¬p" is "why this and not that" is the owner's. Not changed.
- The Sonnet 5.5 trial folder had uncommitted changes from another agent during this check; not opened, not staged.

Checked by one Opus 5.5 agent under rule 9, 28 September 2026. Nothing ruled for the owner; nothing applied to the theory (rule 11).
