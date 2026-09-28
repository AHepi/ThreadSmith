# S107: Round 4 — the second checker on the critical review

*A fresh Opus 5.5 agent that built nothing of this round, 28 September 2026 (the orchestrator's decision 1; rule 9 of `results/S107 Round 4 - how the replies will be read, written before sending.md`, e4dff1ff68c724863c4fa4c52ef1ff95, and its addendum, rules 6, 9, 11–16 binding). Read: the orchestrator's decisions, the critical review, the rule and addendum, decisions S20–S52 (`records/Semantics - Decisions.md`, 5d660d123a36e1369ba8289db445e18c), the integration notes and report, the three area files, the maths after round 4, `tests/106` and `tests/107`. For each objection: (a) keep what was merged, (b) the review's fix, (c) a third fix. Maths and code only; no new prose in the text (S40); no owner's answer reversed or weakened (S41, S44, S45, S47); what hard to vary covers stays parked (S33, S34). "Model" below means only the program or its folder (S43); for what the theory judges, "candidate".*

## 1. Rulings

| # | objection | ruling | reason (one line) | checked by the program |
|---|---|---|---|---|
| O1 | records say no computed value reads the labels of a question that occurred | (b), with (c) for (a3)'s wording | (EX) reads the criticism label through CompleteCritical, and Episode of a whole chain reads q(o), which I192 (e) sets; Con reads q(o) too (through Episode), so (a3) says "Con and Build at the output are the same, whichever reading the labels give", not the review's "read none of the labels". The ground for "not the owner's" moves to L377 ("alleged defect \(\delta\)") and L429 ("a conjectural objection"): the text settles it, so no owner question | new look FC84.new1 (a4): one history, two labellings; Con, Build equal; CreateEx {False, True} under I191's, {False} under I192 (d)'s (all 2^10 values of its Θ-read conjuncts); Episode(o1 ≺ o2) base True, iv-u False (S41). Look: as expected |
| O2 | B4, C-K1 W, and R4A2-T1 (L271), R4INT-T1 (L536) applied | (b) | L271's colon, "intervening on the upstream port changes the target's downstream value but not the calculation's", writes the transport (the intervention carried to itself); under it (F2) fails on both production contracts tried; τ′ sets the calculation's L, so it is another candidate, the answer written in through the transport. B4, C-K1 → I, settled by the line's own words (I193 (b); rule 6). R4A2-T1 narrowed Part V's sentence to one example's contract and kept the words with a formula beside them; L536 reports Part V. Neither applied | FC27.new1 rerun: (b) F2eq fails at set(H=2), set(H=3) on C1 and C_H, (E) no on both; (d) under τ′ on C_H every conjunct holds. Title and (d) restated; statuses unchanged |
| O3 | FC83 against D18.1's "under every reading" | (c): the review's re-based statement, and a look that computes what it cites | FC83's H under U and K rested on round 2's reading of L405's old wording, which D13.3 no longer carries; the statement is now under T and T′, U and K a comparison; the look computes Build read as Held under U and K instead of pointing to area 3's scratch run | FC83 look: 146 histories; U 0 counterexamples, K 26 (first: held [1, True], trace [1, 0], Sel's conditions [0, True]; fixed point o2 Sel), K's defect (FC98 (d)). Look: as expected; FC83 H |
| O4 | FC84.new1 (a3) rests on labels set by hand | (b) | `readings_as_claimed` compared functions of hand-set labels with a hand-typed table (lesson S39); nothing can compute Θ, so re-stated: the readings are printed as the labels give them; the condition reads Con and Build only | (a3): computed, as claimed (condition `s41_same and l55_as_b`) |
| O5 | "easy to vary" in K1's record | (b) | K1 needs only kind ii (D10.2), which the code checks; D10.4's gloss on the stock pair (the tilt and the myth) bears on what hard to vary covers (S33, S34; the orchestrator's decision 2) | FC72.new2 (b) statement cut to "(D10.2)"; P4 pointer row in `parked after round 4.md` |
| O6 | FC72.new2 (d) computes only one encoding | (b) | (b) speaks of either encoding, so (d) computes both | (d): ℰ_myth1 and ℰ_myth2 each (E) no (F1, F2, A no), kind i, June in the south 'warm' against the target's 'cold', ruled out for j3, the tilt not; as claimed |

No ruling reverses or weakens S41 (Q2, Q6, Q15, Q23), S44, S45 or S47: Con and Build of the bridge are untouched (FC84.new1 (a1)–(a3)); the maths still asks for no criticism event (FC32.new1 (f)); (EX)'s need of a criticism is the text's (L429, L447–L449), as area 3's B12 row found.

## 2. What changed, by objection

- **O1.** I192 "why this one"; D12.2's [r4] mark (": no computed value reads the labels (S47)" deleted); D13.8's [r4] mark ("I191's reading" → "I190's reading"; "no value of (EX), Con or Build turns on it" → "Con and Build do not turn on it (FC84.new1 (a3)); (EX) does, through CompleteCritical's criticism (FC84.new1 (a4)), and the text types a criticism by its alleged defect (L377; D9.10) and a complete critical episode by 'a conjectural objection' (L429)"); FC84.new1 (a3)'s statement; new look (a4); owner questions §C row 1 (its ground: L377, L429). Each change carries an [r4b] mark, or a "[second check, O1: was …]" note.
- **O2.** `text changes after round 4.json` → `[]`; `tests/107` rebuilt from `tests/106` by `tools/sonnet_harness/apply_changes.py` (the round's applier) with the empty list; I193's row (settled by L271's colon; the integration's C1 choice recorded as withdrawn) and its numbering row; I65's row; E1's [r4] mark; FC27's r4 note; FC27.new1 title, (b), (d), source quote; owner questions §C row 2; moves.
- **O3.** FC83's statement (json, md, the code's printed statement); FC83's look; D18.1's pair-5 mark; owner questions §C last row.
- **O4.** `claims_s41.fc84_new1` (a3): `readings_as_claimed` out of the condition; statement.
- **O5.** `claims_r4a3.fc72_new2` (b) statement; json and md; `parked after round 4.md`: a P4 pointer row.
- **O6.** `claims_r4a3.fc72_new2` (d): both encodings computed; statement.

Not touched: the area files, the integration notes and report (records of what the integration did; they keep 6e9bd68f… for its tests/107), the build scripts, the harness specs, `tests/106`, the rule, the replies, the decisions, every earlier round's file, `scratchpad/s108/`.

## 3. Runs (PYTHONHASHSEED=0, `-B`, scale 4, cap 45, `--no-write`, under `timeout`; no `__pycache__`)

| run | before | after |
|---|---|---|
| whole suite (`run_claims.py --expect … after_round4`) | 133 H, 2 CEX, 7 NT of 142; 142 of 142 equal to the integration's record (c6fea9d9…); 501.7 s; raw eea54918522da1049e1d799bf4a201a6; folder unchanged | 133 H, 2 CEX, 7 NT of 142; 142 of 142 equal to the record as changed here (3d9864f1…); 518.6 s; raw 51e536234dd3ce22f4a970aae40e05ef; folder unchanged; no error. CEX: FC23, FC63. NT: FC31, FC35, FC89, FC94, FC104, FC105, FC110. FC14 and FC32.new1 read `formal core, after round 4.md` d6e6ec62… (118 definition lines, none with 'is a cause'; 114 paragraphs, all mapped) |
| `s104_external.py` | 86a67664a9a3584351fd4836a4140b69 | 86a67664a9a3584351fd4836a4140b69 |
| `s104_creative_transport.py` | d473944e74d2f349b1fdfb83277843cf | d473944e74d2f349b1fdfb83277843cf |
| `s106_cases.py` | 043aeb3647a9004ae43009a7fed50b4e | 043aeb3647a9004ae43009a7fed50b4e |
| `apply_changes.py`, `tests/106` → new `tests/107`, list `[]` | — | 0 read, 0 applied, 0 refused, 0 held; out c7af964c329ab7959243405d394e6574 (= `tests/106`, byte for byte); lines differing 0; S95 new 0, S23 list 0, S96 new 0; headings 55, terms 154, labelled formulas 23 kept |

What changed in the printout (timings aside, compared line by line: the four claims the code touches, and the core's md5 in FC14 and FC32.new1; nothing else): FC84.new1 gains (a4), look as expected, and (a3)'s statement; FC27.new1 (b)'s statement and (d)'s label and statement; FC72.new2 (b)'s statement, (d) prints both encodings; FC83's statement for its first part, and a third part, a look, as expected. No status moves.

Scratch scripts (scratchpad `s107_2c/`, not committed): `ex_reads_labels.py` (7e37055ce4a5ebf04b50029799ff6e19; O1's table, as the review's §3.1), `myth_both_finer.py` (60d04f71c566d953e46e1b583dc9c799; O6), `fc83_held.py` (0b23feb467ce054dea55c29c1bb8ec64; O3: build_at and Held under each cut: U, T, T′ none; K 26 with Held, none with build_at), `code_edits.py` (724b859a679e2ba540556e49b557c49b) and `records_edits.py` (e7fca878ae4c170a0a48ce506ccc5b27): the changes as exact replacements, each span found once, first on a scratch copy.

## 4. md5s, before → after

| file (in `results/S107 Round 4 - maths after the reading/` unless named) | before | after |
|---|---|---|
| `tests/107 The semantics, standing alone, after round 4.md` | 6e9bd68fb1f98b52a3a02fc896cdc9bd | **c7af964c329ab7959243405d394e6574** |
| `tests/106 … without the written-in test.md` (input, not written) | c7af964c329ab7959243405d394e6574 | c7af964c329ab7959243405d394e6574 |
| `text changes after round 4.json` | a05100798b237684fcf95b5704b4f7aa | d751713988987e9331980363e24189ce |
| `formal core, after round 4.md` | 4f9bef648e2a876be27ac920dd561b54 | d6e6ec62acbc6ef763e07b7cd7b29540 |
| `formal claims, after round 4.md` | b91b201a3d292c700f7977df43312b8a | 1bebcb5b77f51303735bc65778fc9cd8 |
| `formal claims, after round 4.json` | c6fea9d95235cd7483ebc0a0cc8b1afc | 3d9864f1be8ec8b88914dc2800af4288 |
| `inventions register - addendum after round 4.md` | 567c1d51977cc67ee8419d67f7dbad80 | 4912096ebab724dcad7f841983b5e09d |
| `owner questions after round 4.md` | 600c4e477750d5a51d70c985c6b5e1a3 | 2f7425fc314e92e32e29059bf72e8b17 |
| `parked after round 4.md` | e6b46848e238ed7fd3b302cf07f0af4e | 57a0360ed51c57830388d04c7d7aa3de |
| `moves after round 4.md` | 4be23e039b8426a58d7247f1048eb228 | 784d72930bf1b9f1286ae51e23894755 |
| `model after round 4/model/claims_s41.py` | 5754e7fca358419ae0a88a5e934e98aa | fcacbcae7b4665bb97b041d76b749a65 |
| `model after round 4/model/claims_r4a2.py` | b9e0577a1bb01b22fede0502cc9e46c2 | e7571f13ef932c4dac89df1974e9492f |
| `model after round 4/model/claims_r4a3.py` | 1b848683769783629269c09343f8da2f | ab03749bbf499b1d3c6dd7c81d10eb72 |
| `model after round 4/model/claims_b.py` | a070ae7e7ad34b4a19808ac8731ac1ff | 931262d306e91896c727e369b79af36f |

Unchanged: the other 19 files of `model/`, the three case scripts, the integration notes and report, the build scripts, the area files. The json keeps each earlier title and statement it changes (`title_before_r4b`, `formal_before_r4b`) and an `r4b` note per claim; `after_round4` is the result on the program after the second check.

## 5. Words outside formulas

`tests/107` is `tests/106`: 15,204 → **15,204**; words 16,102; no line differs (the integration's `tests/107`: 2 lines, L271 +2 and L536 −2, words 16,103). No text change, so nothing of S40's three kinds is applied.

## 6. Moves (rule 16, strictly)

| | formal | text applied | moves |
|---|---|---|---|
| area 2 (D6.3, D7.4) | 2 | 0 | 2 |
| area 3 (D18.1 / DEP['Build'], D0.2 twice, D16.XV's Uses) | 4 | 0 | 4 |
| integration | 0 | 0 | 0 |
| second check | 0 | 0 | 0 |
| **total** | **6** | **0** | **6** |

Withdrawn: R4A2-T1, R4INT-T1 (O2). Not counted, as rounds 2 and 3: A3 F1 (a path), F5, F6 (notation), A2 F3 and every mark; re-based claims (FC31, FC98, FC32.new1; FC83, whose statement follows move 3 with its result unchanged); new test claims and parts (FC84.new1 (a3), (a4), FC83's look, FC27.new1, FC72.new2 and the others); I192–I197; K1; the P4 pointer. D0.2 counted once gives 5. **6, not 0 (the integration counted 8).** Round 4 is final after this check; by S52 the series is on hold, and part A (S108) starts from this state (the orchestrator's decision 3).

## 7. Owner questions

None. O1's point (whether a question that occurs to the agent is a criticism) is settled for everything computed: Con and Build do not turn on it (FC84.new1 (a3)); (EX) does, and the text types a criticism by its alleged defect (L377) and a complete critical episode by "a conjectural objection" (L429), so a question with no defect alleged gives (EX) no criticism (FC84.new1 (a4)). O2 is settled by L271's own words. Nothing is held.
