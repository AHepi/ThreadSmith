# S107 Round 4 - critical review of the round

*Rule 8 of `results/S107 Round 4 - how the replies will be read, written before sending.md` (e4dff1ff68c724863c4fa4c52ef1ff95) and its addendum (aa9642f5df4112b4dfe581cef58dd911), both read whole first. Reviewer: a fresh Opus 5.5 agent (S42: no Fable) that built nothing of this round, 28 September 2026. Decisions S20-S48 read (`records/Semantics - Decisions.md`, now 5d660d123a36e1369ba8289db445e18c: S49-S52 added since the rule, and stray backslashes removed in S41, S43, S44, S47, no word changed). Rules on nothing; the orchestrator decides (rule 9).*

*Read: the tabulation (18f6af15…); the three area files (cd8f9ac4…, a040c87a…, bb65b2dd…) with their runs; in `S107 Round 4 - maths after the reading/`: integration notes (777ca54e…), integration report (5825901c…), formal core after round 4 (4f9bef648e2a876be27ac920dd561b54, word-diffed against S106's), formal claims after round 4 (.md b91b201a…, .json c6fea9d9…), inventions addendum (567c1d51…), owner questions (600c4e47…), parked (e6b46848…), moves (4be23e03…), text changes (a0510079…); `tests/107` (6e9bd68fb1f98b52a3a02fc896cdc9bd) against `tests/106` (c7af964c329ab7959243405d394e6574): 2 lines differ, L271 and L536. The four `.response.txt` where a ruling turned on them.*

*Written: this file only. Not written: the text under review or any earlier text, the rule, the addendum, the replies, the decisions, any committed file. Reruns from `model after round 4/` (PYTHONHASHSEED=0, `-B`, under `timeout`, nothing written; the folder unchanged, no `__pycache__`); the three scratch scripts are in §6. "Model" means only the program or its folder (S43); for what the theory judges, "candidate" or "explanation".*

## 1. Objections

| id | weight | what | fix, in one line (§2 whole) |
|---|---|---|---|
| O1 | matters | I192, the D12.2 and D13.8 [r4] marks, FC84.new1 (a3) and owner questions §C row 1 say no computed value reads the question labels; (EX) and Episode do (FC32.new1 (f); run §3.1) | restrict each to Con and Build at the output; name (EX)'s reading; add a look (a4); ground "not the owner's" on L377, L429 |
| O2 | matters | B4, C-K1 ruled W and R4A2-T1 (L271), R4INT-T1 (L536) applied, though L271's colon fixes the transport, under which (F2) fails on every production contract tried (FC27.new1 (b)) | B4, C-K1 → I, settled by L271's own words (I193 (b)); neither text change applied; moves 8 → 6 (at least R4INT-T1 goes: 7) |
| O3 | minor | D18.1 now says Build reads Held "under every reading"; FC83 still states "under U, K, T and T′ … D13.3 with the cut", and holds under K only on the old reading (area 3 runs §3.6) | re-base FC83's statement to T, T′, with U, K named as round 2's comparison |
| O4 | minor | FC84.new1 (a3)'s "the readings part ways" compares functions of labels set by hand with a hand-typed table (lesson S39), the ground on which area 1 declined B11's code | (a3)'s condition reads Con and Build only; the readings printed as the labels give them |
| O5 | minor | K1's record states, on the stock case, that the tilt and the myth are "each easy to vary against the other" (D10.4): bears on what hard to vary covers (S33, S34; P4) | cut to kind ii (D10.2) in FC72.new2 (b); a pointer row under P4 in parked |
| O6 | minor | FC72.new2 (d) says "the myth fails (E)" on the finer question and computes the written-in myth only | compute both encodings (run §3.3: both fail (E), kind i) |

Two "matters", four "minor". No objection touches an owner's answer, the values, or the end-of-series outcome.

## 2. The objections whole

### O1 (matters): what reads the labels of a question that occurred

**Where.**
- The register, I192, "why this one": "no value of (R), Sel, Con, Dec, Episode, Build or (EX) reads the labels". Area 1's own row lists "(R), Sel, Con, Dec or Build"; the integration added Episode and (EX).
- D12.2's [r4] mark: "no computed value reads the labels (S47)".
- D13.8's [r4] mark: "'because the agent asked' is I191's reading; … no value of (EX), Con or Build turns on it (FC84.new1 (a3))".
- FC84.new1 (a3)'s statement: "no computed value reads the labels".
- Owner questions §C row 1: "Nothing the theory computes turns on it".

**Why it fails.**
- (a3) computes Con and Build at the output, nothing else.
- (EX) reads the criticism label. The program's own FC32.new1 (f) prints "(EX) ⇝ Crit True" under U, K, T, T′ (rerun here).
- Run §3.1, on one history (a question about the brief at o1, "why this brief?", no defect alleged, the brief kept), with area 3's own encoding of CreateEx (its runs §7, b12.py):

  | labelling (Θ, by hand, I90) | Con at o2 | Build | CreateEx over the 2^10 values of its Θ-read conjuncts |
  |---|---|---|---|
  | I191: the question a criticism aimed at the brief | [True] | True | {False, True} |
  | I192 (d): a question label, no criticism | [True] | True | {False} |

- Episode reads q(o), which I192 (e) sets. In (a3)'s case iv-u, under S41, Episode(o1 ≺ o2) is False; in the base chain it is True.
- "Because the agent asked" is I190's registered choice ("a criticism … is … the agent's asking when a question occurs"), not I191's. I191 maps a question to a criticism; the note states the converse.

**Fix** (records, marks and a test part; no definition, no value, no text; not a move).
1. **I192, "why this one":** → "under D13.8 as S41 has it, Con and Build at the output are the same under all three (FC84.new1 (a3)); (EX) reads the criticism label through CompleteCritical (FC32.new1 (f); (a4)); Episode of a whole chain reads q(o), which (e) sets".
2. **D12.2 [r4] mark:** delete ": no computed value reads the labels (S47)".
3. **D13.8 [r4] mark:**
   - "is I191's reading" → "is I190's reading";
   - "no value of (EX), Con or Build turns on it (FC84.new1 (a3))" → "Con and Build do not turn on it (FC84.new1 (a3)); (EX) does, through CompleteCritical's criticism ((a4))".
4. **FC84.new1:**
   - (a3)'s "no computed value reads the labels" → "Con and Build read none of the labels";
   - a new look part (a4): the table above (two labellings of one history; CreateEx exhaustive over Θ's other conjuncts).
5. **Owner questions §C row 1, "why not the owner's":** → "Con and Build do not turn on it (FC84.new1 (a3)). (EX) does; the text types a criticism by its alleged defect (L377: "alleged defect \(\delta\)"; D9.10) and a complete critical episode by "a conjectural objection" (L429). So a question with no defect alleged gives (EX) no criticism, as (d) labels it." Still no owner question (rule 12: the text settles it). S47 speaks of the maths asking, not of (EX)'s definition.

### O2 (matters): L271 read whole, and the two text changes

**The line** (text 106, L271): "A **reversed calculation**, identification presented as production, fails (F2) under the production contract: intervening on the upstream port changes the target's downstream value but not the calculation's."

**The finding** (B4, C-K1): read of every production contract, the line is false, because under τ′ on C_H E_rev meets (E) (FC27.new1 (d)).

**Why the W verdict says more than the finding shows.**
- **The colon writes which transport the line speaks of:** the intervention on the upstream port, carried to itself.
- **FC27.new1 (b)** states those words and computes the failure on every production contract tried. Its statement: "with each edit carried to itself, intervening on H changes the target's L and not E_rev's". Rerun (§3.2): F2eq fails at set(H=2), set(H=3) on C1 and on C_H; (E) False on both.
- **Under τ′ the colon is false of the candidate.** The calculation's L is set, so τ′'s candidate is another candidate. "Identification presented as production" does not describe it either: r_L is a slot, production written in through the transport (FC27.new1 (d)).
- **So I193's choice (b) is the line's own.** Area 2 rejected it as "writes a condition on τ the line does not write"; the colon writes it.
- **The change narrows the text.** R4A2-T1 binds Part V's general sentence to one example's contract (\(C_1\) of E1), and R4INT-T1 carries that into (Suff) at L536.
- **R4A2-T1 is none of the three kinds, strictly.** It keeps the words "the production contract" and adds a formula and pointers beside them.
- **R4INT-T1 answers no finding.** No reply names L536, and L536 opens "Part V says which of the four each classic attempt fails", so its "the production contract" is L271's.

**Fix.**
1. **B4, C-K1:** W → I (which transport). Settled by L271's own words, I193's choice (b); rule 6: nothing in the text changes.
2. **R4A2-T1 and R4INT-T1:** not applied. `text changes after round 4.json` without both, so the text after round 4 is `tests/106` unchanged (c7af964c…). Nothing is final before this review (rule 8); rule 9 gives the call to the orchestrator.
3. **I193's record:** → "settled by L271's colon: the transport carries the intervention on the upstream port to itself (FC27.new1 (b)); τ′ on C_H (FC27.new1 (d)) is another candidate, which L271 does not describe". The same words go into E1's [r4] mark and FC27's note.
4. **FC27.new1:**
   - title → "L271's reversed calculation: under the transport its colon describes, (F2) fails on C1 and C_H";
   - (d)'s "L271 read of every production contract states an (F2) failure the computation does not give" → "a candidate other than the one L271's colon describes";
   - statuses unchanged.
5. **Moves:** 8 → 6.
6. **If the orchestrator keeps R4A2-T1:** R4INT-T1 is still not applied (L536 reports Part V), and moves are 7.

### O3 (minor): FC83 against D18.1 (pair 5)

- **D18.1** now says (A3 F2): "Build reads Held_ℓ(o, c) outright (D13.3; L405 since R3A3-T4), under every reading".
- **FC83's statement:** "… under U, K, T and T′ (D12.1 with I161; D13.3 with the cut)". Its `build_at` reads Build through R under U and K.
- **Area 3 runs §3.6:** with D13.3 as the core now has it, FC83 gives a counterexample under K. So FC83's H under K rests on a reading of D13.3 that the core no longer carries.

**Fix: re-base FC83's statement** (statuses unchanged; not a move). The new statement: "SelResp(t → t') ⇒ ¬∃ Build of cod t' in h(t'), Rep computed as in FC12.new1, under T and T′ (D12.1 with I161; D13.3: Held_ℓ(o, c), L405 since R3A3-T4). Under U and K, `build_at` keeps round 2's reading of L405's old wording, a comparison; with D13.3 as it now reads, K gives a counterexample (area 3 runs §3.6), which is K's defect (FC98 (d))."

### O4 (minor): FC84.new1 (a3) from labels set by hand

**What rests on hand-set inputs.**
- `readings_as_claimed` applies `no_brief_question`, `no_question_about_brief` and `q == brief` to labels set per case by hand (crit, quest, qs; I90).
- It then compares the results with a hand-typed table. That restates its inputs (lesson S39).
- Area 1 declined B11's code on this ground ("a hand-set tag compared with nothing computed").
- What (a3) does compute is Con and Build.

**Fix** (in `claims_s41.fc84_new1`; statuses unchanged; not a move):
- (a3)'s condition `readings_as_claimed and s41_same and l55_as_b` → `s41_same and l55_as_b`;
- the readings printed as the labels give them;
- the statement's "The readings part ways" → "the labels of each case (Θ by hand, I90) give the three readings as printed".

### O5 (minor): "easy to vary" in K1's record

**Where.**
- Area 3 §1a (b), and FC72.new2 (b): "each easy to vary against the other (D10.2, D10.4)".
- Area 3 §1a: file 93's "If not" branch "is what (b) computes".

**Why it matters.** The myth about winter and the tilt are the stock pair for hard to vary. A computed "the tilt is easy to vary here", carried as settled, rules on what hard to vary covers, which is parked (S33, S34; P4 is "easy to vary" as a reading).

**What K1 needs.** Only kind ii (D10.2), which the code checks (`problem_kind == "ii"`); it computes no D10.4 of its own.

**Fix** (neither is a move):
- FC72.new2 (b): "… a problem of the second kind, each easy to vary against the other (D10.2, D10.4)" → "… a problem of the second kind (D10.2)".
- `parked after round 4.md`, a pointer row: "P4: FC72.new2 (b), on the Greeks' contract; D10.4 would call the tilt and the myth each easy to vary against the other; not built on, and not carried to the owner as settled (S33, S34)".

### O6 (minor): FC72.new2 (d)

- **What the claim says.** (b) says "for either encoding". (d) says "the myth fails (E)" but computes only ℰ_myth1.
- **Run §3.3.** On the finer contract ℰ_myth2 also fails (E): F1, F2 and A are no. It is kind i against the tilt, and gives 'warm' for June in the south, where the target gives 'cold'.
- **Fix.** In `claims_r4a3.fc72_new2` (d), compute `for mF in (myth_written(pF), myth_told(pF))`, with the expected values as run here. Status unchanged; not a move.

## 3. Reruns (from `model after round 4/`; folder md5s unchanged, no `__pycache__`)

| # | what | result |
|---|---|---|
| 3.1 | `ex_reads_labels.py` (§6) | the table of O1; iv-u Episode(o1 ≺ o2) False under S41 and L55; base True under S41 |
| 3.2 | `--claim FC27.new1 --claim FC27` | both H; (b), (c), (d) as the record gives them; (b)'s statement is L271's colon |
| 3.3 | `myth_told_finer.py` (§6) | ℰ_myth1 and ℰ_myth2 each (E) False on the finer contract, kind i, June south 'warm' against 'cold' |
| 3.4 | FC84.new1, FC72.new2, FC30.new1, FC83, FC98, FC23.new4, FC42.new1, FC23.new5, FC14, FC32.new1 | each H, every part as `after_round4` records it (FC98 (b) "look: not as expected", as recorded since round 2); FC14 and FC32.new1 read `formal core, after round 4.md` (4f9bef64…) |
| 3.5 | the cases reply's NC1, NC3 (r88–r110): not run by the reply, the tabulation's rule-3 list, run by no area | NC1: account False (NC2, Dep False), round 3's (E) False, as the reply says; its "r and u both slots" does not compute (no slot: r's relation at tue is unset); nothing turns on it. NC3: account False ('translates C' False), pin at set(H=2) False, Slot False, as the reply says |

The whole suite was not rerun. It ran twice with equal claims (Sonnet's worker, and the integration agent: 133 H, 2 CEX, 7 NT of 142), and no objection above depends on it.

## 4. Where I find nothing to object to

| item | finding |
|---|---|
| K1 against the owner's words | ruled with them. FC72.new2 (c): the finding "Slot" rules nothing out (S44, S45); j1's ground "Slot → ¬Acc", taken as given, is L397's "if \(r\), this candidate fails (E)", a premise taken as given, the person's choice (S28, S21); j2 blocked (D9.7), as Q23 with "p because p". No text change needed (L317, L397 already say it). Only O5, O6 |
| S40, prose | text: 2 lines, words outside formulas 15,204 → 15,204; no new word outside formulas and pointers (O2 is on need and kind, not prose). Formal core: marks only |
| S41, Q2, Q6, Q15, Q23 | none reversed or weakened: Acc ∧ Dec ⇒ ¬Expl under both Uses readings (FC30.new1 (h), FC23.new2 (f)); the bridge Con and Build the same under I191, (d), (e) (FC84.new1 (a3)); Q15, Q23 untouched |
| S44, S45, S47 | the written-in test is not back by any name; the maths asks no criticism of construction (FC32.new1 (f): Con, CT, Episode ⇝ Crit False); B11's and S-N6's glosses rightly not taken (rule 11) |
| S20, S21, S23, S25–S28 | no count, grade or order; no "must"; S23's words only in quotations (area 3 twice, quoting file 93 and S23); no physics in (E) |
| S33, S34, values | no fix on what hard to vary covers (O5 is on a record); nothing moves where values are placed (D14.8 untouched, area 3 row 11) |
| S36, inventions | I192–I197 recorded, numbered after I191, alternatives given; I193 settled in so many words (rule 6) at both lines (O2 contests the need, not the record) |
| S43, S46 | no "model" for a candidate in any file of the round the owner may see; Sonnet ran only mechanical jobs (merge, suites, text changes), Opus resolved the one conflict |
| the other verdicts | area 1's rows 1–15 (O1 and O4 are on records and a test part, not on these verdicts), area 2's rows 1, 3–15 and 17–20, and area 3's rows 1–24 hold on the texts and runs as given (checked by reading and §3.4). The tabulation rules on nothing, and its flags and area choices follow rules 4 and 5 |
| the formal changes | D6.3 (F1) agrees with Pin and `core.slot` (FC23.new4 (c)); D7.4's δ_v is carried, not ∃ (L253; FC42.new1 (d)); D0.2 (F3, F4); D9.10 δ_Conn, (Elim) kl (notation); D16.XV's Uses read at the symbol (F7, the program brought to the core); the letter δ one way after round 4 |
| the merge, the files | one conflict, both imports kept; git: since S106's records no file of an earlier round or step modified (only the decisions file, by the orchestrator: S49–S52 and the backslashes) |

## 5. Owner questions, and moves

- **Owner questions.** None new, and none missing. Each point of §C is settled by the texts or a computation, and none is the owner's. O1 corrects one stated ground (§C row 1) but not the outcome. No question uses "model" for a candidate (S43). K1 is settled by the owner's words, not sent.
- **Moves (rule 16).** 8 is rule 16 as rounds 2 and 3 counted it: 6 formal changes and 2 text changes applied.
  - D0.2 is counted twice, as round 3 counted D12.1's three fixes.
  - Not counted, as in round 3: A3 F1 (a path), F5 and F6 (notation), the marks, the tests and the register.
  - With O2: 6, or 7 if only R4INT-T1 goes.
  - No reading gives 0, so the series is not ended by rule 17; S52 governs what follows.

## 6. The scratch scripts (scratchpad `cr/`, not committed)

**`ex_reads_labels.py`** (3930dc6e0b4b880b209ec6ffc4ac2575). It is area 3's b12.py loop, with `theta` and the CreateEx formula verbatim, run on two labellings of one history:

```python
qs = ["C_brief"] * 2
lab_I191 = ([("C_brief (the contract)", "why this brief?"), None], [None, None])   # (crit, quest)
lab_d    = ([None, None], ["C_brief (the contract)", None])
# per labelling: Con, Build from prov_fixed_points/build_at (T', chain_eps S41); CreateEx over 2^10 Θ-values
Q_B = "C_brief? (a question found at o1, its target the brief)"
episode([Q_B, "C_brief"], [False, False], rd)   # iv-u, rd in (S41, L55); base: episode(qs, [False, False], rd)
```

**`myth_told_finer.py`** (d50d576ab5a862f795a25df21deb6a4d):

```python
pF = seasons_question(EVERY_PAIR, "p_finer", seasons_target())
for f in (myth_written, myth_told):
    m = f(pF)
    account(m, detail=True); problem_kind(tilt(pF), m); m.ans_E(ONE, "S")
```

**`nc1_nc3.py`** (55d1075fb61c1771efaf7323f3d63cd7): the reply's NC1 and NC3 blocks as written (r88–r110), with `pin(c3, "c_L", setH, "b1_45")` for pin's four arguments.
