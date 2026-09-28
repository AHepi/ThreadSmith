# S107 Round 4 — moves after round 4 (rule 16, counted strictly)

*Integration, last part (rule 7), 28 September 2026: a fresh Opus 5.5 agent; the reading rule and its addendum read whole first; decisions S20–S48 read (S40, S41, S43, S44, S45, S47 bind). Rule 16: the formal changes that answer a finding that holds (M, W or I: a changed or new definition, a changed claim or encoding, a change to the program's reading of a definition), plus the text changes applied. Counted as rounds 2 and 3 counted (lesson S41). Findings that hold: area 1 6 (M 4, one point; I 2), area 2 12 (M 7, W 2, I 3), area 3 9 (M 9, row 9 also I); K1 settled. Each counted change was checked present in `formal core, after round 4.md` or `model after round 4/model/`. "Model" means only the program or its folder (S43).*

*Recounted by the second checker on the critical review (`results/S107 Round 4 - the second checker on the critical review.md`), 28 September 2026: O2 ruled B4 and C-K1 I (L271's colon fixes the transport), not W, so R4A2-T1 (L271) and R4INT-T1 (L536) are withdrawn and `tests/107 …` is `tests/106` unchanged (md5 c7af964c329ab7959243405d394e6574). Area 2's findings that hold: M 7, W 0, I 5. The second check's own changes (O1, O3–O6) are marks, register and parked entries, re-based claims and test parts: none counted. The integration's count was 8.*

## Counted

| # | area | finding(s) | move | kind | checked at |
|---|---|---|---|---|---|
| 1 | A2 | B8, S3 | D6.3: ∀(a,b) ∈ Det_C [t translates (a,b) ∧ …] (F1) | changed definition | core D6.3 |
| 2 | A2 | B-N1, W-N1, S-N1, C-N1 | D7.4: Acc((E_v, p, t_v, Γ_v, δ_v)), δ_v carried (F2, I195); `core.boundary` its encoding | changed definition | core D7.4; `core.py` L887 |
| 3 | A3 | S2 | D18.1's T′ item: Build reads Held_ℓ(o, c) under every reading; DEP['Build']: staged (R) → Held (F2) | the program's reading of a definition | core D18.1; `claims_b.py` L2566 |
| 4 | A3 | S4 | D0.2: 'subhistory' out of the primitives; "subhistory (D11.3, I151) are defined" (F3) | changed definition | core D0.2 |
| 5 | A3 | S6 | D0.2: Work(kl), 'without loss', 'operates on', 'fails to capture', 'not creative' in; DEP['DefeatConds'] + 5 (F4) | changed definition | core D0.2 |
| 6 | A3 | W5 | D16.XV's Uses read at the symbol: (E), Acc ∉ Uses(α); `USES_READING = "symbol"` (F7, I196) | the program's reading of a definition | core D16.XV mark; `claims_s41.py` L42 |

| | formal | text applied | moves |
|---|---|---|---|
| area 1 | 0 | 0 | 0 |
| area 2 | 2 | 0 | 2 |
| area 3 | 4 | 0 | 4 |
| integration | 0 | 0 | 0 |
| second check | 0 | 0 | 0 |
| **total** | **6** | **0** | **6** |

## Withdrawn by the second check (O2)

| was | move | why withdrawn |
|---|---|---|
| 7 | R4A2-T1, L271: "… contract:" → "… contract \(C_1\) (E1, FC27):" (A2; B4, C-K1) | L271's colon ("intervening on the upstream port changes the target's downstream value but not the calculation's") writes the transport; under it (F2) fails on C1 and on C_H (FC27.new1 (b)); τ′ on C_H is another candidate (FC27.new1 (d)); I193 settled by the line's own words (rule 6); the change also kept the words and added a formula and pointers beside them |
| 8 | R4INT-T1, L536: "under the production contract." → "under \(C_1\)." (integration, pair 7) | L536 reports Part V ("Part V says which of the four each classic attempt fails"), so its "the production contract" is L271's; no reply named L536 |

## Not counted

| item | why |
|---|---|
| A2 F3: D6.9's [r4] mark (W4) | a mark; no definition, claim or encoding changes |
| A3 F1: `corefile.py`; FC14, FC32.new1 read one list of places (B14, W6, S1) | a path, not a reading of a definition; round 3 left the same kind of change uncounted |
| A3 F5: D9.10 δ_c → δ_Conn (S-δ) | notation: a renamed letter, the defined relation unchanged |
| A3 F6: D16.XV (Elim) κ → kl (S-κ) | notation, as F5 |
| FC31 (A1 F1); FC98 (a), (a′) and FC32.new1 (c) (A3) | re-based: statements follow R3A1-T1, A3-L520.1 and rows 3–5; statuses unchanged |
| FC83 restated (second check, O3) | re-based: the statement follows move 3 (Build reads Held), result unchanged; its look is a test part |
| FC27.new1, FC23.new4, FC23.new5, FC42.new1 (A2); FC72.new2 (A3) | new test claims; FC27.new1's title and (d), FC72.new2's (b) and (d) restated by the second check (O2, O5, O6), statuses unchanged |
| FC84.new1 (a3) (A1), restated by the second check (O1, O4); FC84.new1 (a4), FC83's look (second check, O1, O3); FC30.new1 (h) (A3); `no_question_about_brief`; `PartialPi` | new test parts and test code |
| I192–I197 (I193 settled by L271's own words, no text change) | register entries |
| K1: FC72.new2, I197 | settled by the owner's words (S44, S45 with S28, S21, S27, S41 Q23); no formal change, no text change, no owner question |
| [r4] marks on D9.7, D12.2, D13.8, E1; D18.1's [r4: integration; pair 5]; [r4b] marks on D12.2, D13.8, E1, D18.1 | marks; no value changes |
| `build_at` under U and K (pair 5) | unchanged |
| `run.py`'s two imports; `corefile.py`'s NAME and folder | the merge |
| owner questions: none; parked: none new, a pointer under P4 (O5) | records |

## How the count could move

| reading | moves |
|---|---|
| as above | 6 |
| D0.2's F3 and F4 as one change of D0.2 | 5 |
| + A3 F1 counted (a changed encoding of FC14, FC32.new1) | 7 |
| + A3 F5, F6 counted (notation) | 8 |
| + A2 F3 counted (a mark) | 9 |
| + R4A2-T1 kept (O2's other ruling, not taken) | 7 |

No reading gives 0. **Moves: 6, not 0: the series is not ended by this round (rule 17). Round 4 is final after the second check, and by S52 the review series is on hold (the orchestrator's decision 3).**
