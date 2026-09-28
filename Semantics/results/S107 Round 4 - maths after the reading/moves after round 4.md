# S107 Round 4 — moves after round 4 (rule 16, counted strictly)

*Integration, last part (rule 7), 28 September 2026: a fresh Opus 5.5 agent; the reading rule and its addendum read whole first; decisions S20–S48 read (S40, S41, S43, S44, S45, S47 bind). Rule 16: the formal changes that answer a finding that holds (M, W or I: a changed or new definition, a changed claim or encoding, a change to the program's reading of a definition), plus the text changes applied. Counted as rounds 2 and 3 counted (lesson S41). Findings that hold: area 1 6 (M 4, one point; I 2), area 2 12 (M 7, W 2, I 3), area 3 9 (M 9, row 9 also I); K1 settled. Each counted change was checked present in `formal core, after round 4.md` (md5 4f9bef648e2a876be27ac920dd561b54) or `model after round 4/model/`, and each text change in `tests/107 …` (md5 6e9bd68fb1f98b52a3a02fc896cdc9bd), byte for byte. "Model" means only the program or its folder (S43).*

## Counted

| # | area | finding(s) | move | kind | checked at |
|---|---|---|---|---|---|
| 1 | A2 | B8, S3 | D6.3: ∀(a,b) ∈ Det_C [t translates (a,b) ∧ …] (F1) | changed definition | core D6.3 |
| 2 | A2 | B-N1, W-N1, S-N1, C-N1 | D7.4: Acc((E_v, p, t_v, Γ_v, δ_v)), δ_v carried (F2, I195); `core.boundary` its encoding | changed definition | core D7.4; `core.py` L887 |
| 3 | A3 | S2 | D18.1's T′ item: Build reads Held_ℓ(o, c) under every reading; DEP['Build']: staged (R) → Held (F2) | the program's reading of a definition | core D18.1; `claims_b.py` L2566 |
| 4 | A3 | S4 | D0.2: 'subhistory' out of the primitives; "subhistory (D11.3, I151) are defined" (F3) | changed definition | core D0.2 |
| 5 | A3 | S6 | D0.2: Work(kl), 'without loss', 'operates on', 'fails to capture', 'not creative' in; DEP['DefeatConds'] + 5 (F4) | changed definition | core D0.2 |
| 6 | A3 | W5 | D16.XV's Uses read at the symbol: (E), Acc ∉ Uses(α); `USES_READING = "symbol"` (F7, I196) | the program's reading of a definition | core D16.XV mark; `claims_s41.py` L42 |
| 7 | A2 | B4, C-K1 | R4A2-T1, L271: "… contract:" → "… contract \(C_1\) (E1, FC27):" (settles I193) | text change applied | tests/107 L271 |
| 8 | integration | B4, C-K1 (pair 7) | R4INT-T1, L536: "under the production contract." → "under \(C_1\)." (settles I193 there) | text change applied | tests/107 L536 |

| | formal | text applied | moves |
|---|---|---|---|
| area 1 | 0 | 0 | 0 |
| area 2 | 2 | 1 | 3 |
| area 3 | 4 | 0 | 4 |
| integration | 0 | 1 | 1 |
| **total** | **6** | **2** | **8** |

The areas' own counts: 0 + 3 + 4 = 7 (6 with D0.2 once); the difference is row 8. Integration notes §9.5: 8, the same rows.

## Not counted

| item | why |
|---|---|
| A2 F3: D6.9's [r4] mark (W4) | a mark; no definition, claim or encoding changes |
| A3 F1: `corefile.py`; FC14, FC32.new1 read one list of places (B14, W6, S1) | a path, not a reading of a definition; round 3 left the same kind of change uncounted |
| A3 F5: D9.10 δ_c → δ_Conn (S-δ) | notation: a renamed letter, the defined relation unchanged |
| A3 F6: D16.XV (Elim) κ → kl (S-κ) | notation, as F5 |
| FC31 (A1 F1); FC98 (a), (a′) and FC32.new1 (c) (A3) | re-based: statements follow R3A1-T1, A3-L520.1 and rows 3–5; statuses unchanged |
| FC27.new1, FC23.new4, FC23.new5, FC42.new1 (A2); FC72.new2 (A3) | new test claims |
| FC84.new1 (a3) (A1); FC30.new1 (h) (A3); `no_question_about_brief`; `PartialPi` | new test parts and test code |
| I192–I197 (I193 settled at L271 and L536) | register entries |
| K1: FC72.new2, I197 | settled by the owner's words (S44, S45 with S28, S21, S27, S41 Q23); no formal change, no text change, no owner question |
| [r4] marks on D9.7, D12.2, D13.8, E1; D18.1's [r4: integration; pair 5] | marks; no value changes |
| `build_at` under U and K (pair 5) | unchanged |
| `run.py`'s two imports; `corefile.py`'s NAME and folder | the merge |
| owner questions: none; parked: none new | records |

## How the count could move

| reading | moves |
|---|---|
| as above | 8 |
| D0.2's F3 and F4 as one change of D0.2 | 7 |
| + A3 F1 counted (a changed encoding of FC14, FC32.new1) | 9 |
| + A3 F5, F6 counted (notation) | 10 |
| + A2 F3 counted (a mark) | 11 |
| floor: the two text changes applied (rule 16 counts each) | 2 |

No reading gives 0. **Moves: 8, not 0: the series is not ended by this round (rule 17); S52 governs what follows.**
