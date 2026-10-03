# S104 Round 2 — integration report

*Integration agent (Opus 5.5), 28 September 2026; decision S40. Inputs: `area N - …` (commits a2a78c1, 24b9029, cd077b0). Rules on no challenge.*

## 1. Merge (`model after round 2/`)

Three-way merge (`git merge-file`) of each area's `model/` against the committed `S104 Round 2 - maths/model/`. Layout: all three copies are `area N model/model/`; the merged one is `model after round 2/model/`, run from `model after round 2/` as `python3 -m model.run --claim FCnn --scale 4 --time-cap 45`.

| file | areas | result |
|---|---|---|
| core.py | A1 (Roles: 1 ∉ Set_v, Slc_j, R-ii Obs, Meas, Rule, upstream), A2 (Org.sub, slot/NC1, conf_claim, rivals) | clean; no function shared |
| claims_a.py | A1 (FC05, FC07, FC14, FC20, FC36), A2 (FC14, FC21, FC23, FC27, FC28) | one textual conflict, FC14: both added the same path fallback; combined; now reads `formal core, after round 2.md` first |
| claims_b.py | A1 (sel, con, viol_at, selresp, FC77–FC83, FC101), A2 (FC52, FC67), A3 (FC56, FC70, FC71, FC74, FC75, FC80, FC86, FC90, FC92, FC98, FC102) | clean; no function shared |
| harness.py, run.py, claims_area1.py | A1 | taken |
| phys.py | A3 | taken |
| s104_external.py, s104_creative_transport.py | A2, A3 (path depth only) | A3's copies |

**Conflicts in substance in the code: none.** No named alternatives were needed. Interactions recorded for the critical review:

| # | where | areas | how handled |
|---|---|---|---|
| X1 | D12.1 | A1 (D12.1': no Rep(o, cod t) in h(t); one history) + A3 (H09: 𝒯 = the population) | combined in the formal core |
| X2 | Rep in D12.1', FC83', FC12.new1, T9 (L195) | A1 uses Rep unstaged; A3 (D18.1, OQ1) stages Rep as Rep^ρ, ρ ∈ {K, T} open | formal core writes 'Rep as D18.1, ρ open (Q1)'; code: sel() bans a hand-set tag, so no clash; FC83', FC12.new1 under K and T not tested |
| X3 | Fid⁺ (D5.7, FC104) | A2 drops it for L245, L247; A3 rewrites L520 | combined: Fid⁺ open only for L220, L630 |
| X4 | κ(⊥) := ⊥ | A1-11, A2-05 | one choice, two numbers: I132 = I139 |
| X5 | footprint bijection recoding values | A1 OQ-1, A3 OQ11 | one owner question, Q9 |
| X6 | case programs | A1's D2.6/D4.6' and D12.1' | change FC-E3 and CT8 output lines (§3); A3 checked the programs on its own copy only |

## 2. Claims (scale 4, time cap 45 s, PYTHONHASHSEED=0, timeout 1800 s)

Round 2 (committed): 87 H, 12 CEX, 11 NT of 110. After round 2: 98 H, 3 CEX, 9 NT of 110; with the 3 new claims 101 H, 3 CEX, 9 NT of 113. Run time 360 s.

Each area's copy rerun here: its statuses equal its own `area N - runs.txt`, claim by claim (A1 113, A2 110, A3 110). Merged against the area that changed each claim, part by part (label and status): equal for every claim, except FC14 (A3's copy could not find the formal core; the merge fixes the path). No claim was changed by two areas at part level. Differences from round 2 are the areas' own:

| id | round 2 | A1 | A2 | A3 | after | why |
|---|---|---|---|---|---|---|
| FC01 | H | H | H | H | H |  |
| FC02 | H | H | H | H | H |  |
| FC2.new1 | — | H | — | — | H | A1 new |
| FC03 | H | H | H | H | H |  |
| FC04 | H | H | H | H | H |  |
| FC4.new1 | — | H | — | — | H | A1 new |
| FC05 | CEX | H | CEX | CEX | H | A1: reading (ii) now a look (T4) |
| FC06 | H | H | H | H | H |  |
| FC07 | H | H | H | H | H |  |
| FC08 | H | H | H | H | H |  |
| FC09 | H | H | H | H | H |  |
| FC10 | H | H | H | H | H |  |
| FC11 | H | H | H | H | H |  |
| FC12 | H | H | H | H | H |  |
| FC12.new1 | — | H | — | — | H | A1 new |
| FC13 | H | H | H | H | H |  |
| FC14 | H | H | H | NT | H | A3's copy: path artifact (NT); merged reads the new formal core |
| FC15 | H | H | H | H | H |  |
| FC16 | H | H | H | H | H |  |
| FC17 | H | H | H | H | H |  |
| FC18 | CEX | CEX | CEX | CEX | CEX |  |
| FC19 | H | H | H | H | H |  |
| FC20 | CEX | H | CEX | CEX | H | A1: FC20' (Ans_p ≠ ⊥) |
| FC21 | H | H | H | H | H |  |
| FC22 | H | H | H | H | H |  |
| FC23 | CEX | CEX | CEX | CEX | CEX |  |
| FC24 | H | H | H | H | H |  |
| FC25 | CEX | CEX | H | CEX | H | A2: V_{J_D} := V_D (I138) |
| FC26 | H | H | H | H | H |  |
| FC27 | H | H | H | H | H |  |
| FC28 | H | H | H | H | H |  |
| FC29 | H | H | H | H | H |  |
| FC30 | H | H | H | H | H |  |
| FC31 | NT | NT | NT | NT | NT |  |
| FC32 | NT | NT | NT | NT | NT |  |
| FC33 | H | H | H | H | H |  |
| FC34 | H | H | H | H | H |  |
| FC35 | NT | NT | NT | NT | NT |  |
| FC36 | H | H | H | H | H |  |
| FC37 | H | H | H | H | H |  |
| FC38 | H | H | H | H | H |  |
| FC39 | H | H | H | H | H |  |
| FC40 | H | H | H | H | H |  |
| FC41 | H | H | H | H | H |  |
| FC42 | H | H | H | H | H |  |
| FC43 | H | H | H | H | H |  |
| FC44 | H | H | H | H | H |  |
| FC45 | H | H | H | H | H |  |
| FC46 | H | H | H | H | H |  |
| FC47 | H | H | H | H | H |  |
| FC48 | H | H | H | H | H |  |
| FC49 | H | H | H | H | H |  |
| FC50 | H | H | H | H | H |  |
| FC51 | H | H | H | H | H |  |
| FC52 | H | H | H | H | H |  |
| FC53 | H | H | H | H | H |  |
| FC54 | H | H | H | H | H |  |
| FC55 | H | H | H | H | H |  |
| FC56 | H | H | H | H | H |  |
| FC57 | H | H | H | H | H |  |
| FC58 | H | H | H | H | H |  |
| FC59 | H | H | H | H | H |  |
| FC60 | H | H | H | H | H |  |
| FC61 | H | H | H | H | H |  |
| FC62 | H | H | H | H | H |  |
| FC63 | CEX | CEX | CEX | CEX | CEX |  |
| FC64 | H | H | H | H | H |  |
| FC65 | H | H | H | H | H |  |
| FC66 | H | H | H | H | H |  |
| FC67 | H | H | H | H | H |  |
| FC68 | H | H | H | H | H |  |
| FC69 | H | H | H | H | H |  |
| FC70 | H | H | H | H | H |  |
| FC71 | H | H | H | H | H |  |
| FC72 | H | H | H | H | H |  |
| FC73 | H | H | H | H | H |  |
| FC74 | H | H | H | H | H |  |
| FC75 | H | H | H | H | H |  |
| FC76 | H | H | H | H | H |  |
| FC77 | CEX | H | CEX | CEX | H | A1: FC77' (Hom) |
| FC78 | CEX | H | CEX | CEX | H | A1: D12.1' |
| FC79 | H | H | H | H | H |  |
| FC80 | H | H | H | H | H |  |
| FC81 | CEX | H | CEX | CEX | H | A1: D12.1', D12.7' |
| FC82 | CEX | H | CEX | CEX | H | A1: D12.8' (+ stronger case) |
| FC83 | CEX | H | CEX | CEX | H | A1: FC83' |
| FC84 | H | H | H | H | H |  |
| FC85 | H | H | H | H | H |  |
| FC86 | H | H | H | H | H |  |
| FC87 | H | H | H | H | H |  |
| FC88 | H | H | H | H | H |  |
| FC89 | NT | NT | NT | NT | NT |  |
| FC90 | NT | NT | NT | H | H | A3: implemented |
| FC91 | H | H | H | H | H |  |
| FC92 | H | H | H | H | H |  |
| FC93 | H | H | H | H | H |  |
| FC94 | NT | NT | NT | NT | NT |  |
| FC95 | H | H | H | H | H |  |
| FC96 | H | H | H | H | H |  |
| FC97 | H | H | H | H | H |  |
| FC98 | NT | NT | NT | H | H | A3: implemented |
| FC99 | H | H | H | H | H |  |
| FC100 | H | H | H | H | H |  |
| FC101 | H | H | H | H | H |  |
| FC102 | CEX | CEX | CEX | H | H | A3: converse a look; (b'') |
| FC103 | H | H | H | H | H |  |
| FC104 | NT | NT | NT | NT | NT |  |
| FC105 | NT | NT | NT | NT | NT |  |
| FC106 | H | H | H | H | H |  |
| FC107 | NT | NT | NT | NT | NT |  |
| FC108 | H | H | H | H | H |  |
| FC109 | H | H | H | H | H |  |
| FC110 | NT | NT | NT | NT | NT |  |

CEX left: FC18 (rests on I94, which L556 excludes), FC23 (b) (the claim's own wording, U3), FC63 (c-i) (I99). NT left: FC31, FC32, FC35, FC89, FC94, FC104, FC105, FC107, FC110.

## 3. External examples and the case program (copied beside the model; path one folder deeper)

`s104_external.py`: FC-E1–FC-E5 reproduced: yes (5 of 5). Output differs from the committed run in 2 lines (FC-E3, contract C_all): composites of settings are now interventions (Slc_j, D2.6), not rule edits. FC-E3's finding (c_N and c_Y share every family) unchanged.

```
35,36c35,36
<    D_ro, C_all (every edit), R-i: c_N causal no, measurement of ['X'], rule yes | c_Y causal no, measurement of ['X'], rule yes | both invariant under the settings of X: yes
<    D_ro, C_all (every edit), R-ii: c_N causal no, measurement of ['X'], rule yes | c_Y causal no, measurement of ['X'], rule yes | both invariant under the settings of X: yes
---
>    D_ro, C_all (every edit), R-i: c_N causal no, measurement of ['X'], rule no | c_Y causal no, measurement of ['X'], rule no | both invariant under the settings of X: yes
>    D_ro, C_all (every edit), R-ii: c_N causal yes, measurement of none, rule no | c_Y causal yes, measurement of none, rule no | both invariant under the settings of X: yes
```

`s104_creative_transport.py`: CT1–CT7 unchanged; CT8 differs in 2 lines: under D12.1' (A1) the 'D12.1' column now equals the 'with L201 and L411' column (a represented codomain excludes Sel). The program's label 'Sel as D12.1 has it (L195 alone)' is now stale; not edited.

```
40c40
<          D12.1: Sel yes, Con yes => both;  with L201 and L411: Sel no, Con yes => constructed
---
>          D12.1: Sel no, Con yes => constructed;  with L201 and L411: Sel no, Con yes => constructed
42c42
<          D12.1: Sel yes, Con no => selected;  with L201 and L411: Sel no, Con no => neither (declared by exclusion)
---
>          D12.1: Sel no, Con no => neither (declared by exclusion);  with L201 and L411: Sel no, Con no => neither (declared by exclusion)
```

## 4. Text changes (`apply text changes.py` → `tests/104 …after round 2.md`)

```
input md5 f31ebb1f050783f1a84f6136cec20fcd (as required); output tests/104 The semantics, standing alone, after round 2.md
changes read: 42 (area 1: 10, area 2: 13, area 3: 19)
applied: 42 on 32 lines; refused: 0; held: 0
  APPLIED  L109  area 1 T1     formal  prose words -19
  APPLIED  L119  area 1 T2     formal  prose words +0
  APPLIED  L119  area 1 T3     formal  prose words +0
  APPLIED  L119  area 1 T4     formal  prose words -10
  APPLIED  L127  area 1 T5     formal  prose words -1
  APPLIED  L127  area 1 T6     formal  prose words -30
  APPLIED  L141  area 1 T7     formal  prose words +0
  APPLIED  L151  area 1 T8     formal  prose words -10
  APPLIED  L195  area 1 T9     formal  prose words -11
  APPLIED  L199  area 1 T10    delete  prose words -10
  APPLIED  L257  area 2 A2-T1  formal  prose words -28
  APPLIED  L257  area 2 A2-T2  pointer prose words +1
  APPLIED  L257  area 2 A2-T3  formal  prose words +4
  APPLIED  L265  area 2 A2-T4  formal  prose words +3
  APPLIED  L269  area 2 A2-T5  formal  prose words +4
  APPLIED  L273  area 2 A2-T6  pointer prose words +1
  APPLIED  L313  area 2 A2-T7  pointer prose words +2
  APPLIED  L315  area 2 A2-T8  pointer prose words +1
  APPLIED  L315  area 2 A2-T9  pointer prose words +1
  APPLIED  L315  area 2 A2-T10 pointer prose words +1
  APPLIED  L317  area 2 A2-T11 pointer prose words -12
  APPLIED  L317  area 2 A2-T12 pointer prose words +1
  APPLIED  L325  area 2 A2-T13 formal  prose words -5
  APPLIED  L375  area 3 A3-L375.1 formal  prose words -3
  APPLIED  L393  area 3 A3-L393.1 formal  prose words -11
  APPLIED  L393  area 3 A3-L393.2 formal  prose words -5
  APPLIED  L395  area 3 A3-L395.1 formal  prose words +10
  APPLIED  L441  area 3 A3-L441.1 formal  prose words -13
  APPLIED  L453  area 3 A3-L453.1 pointer prose words +1
  APPLIED  L471  area 3 A3-L471.1 formal  prose words -9
  APPLIED  L520  area 3 A3-L520.1 formal  prose words -7
  APPLIED  L526  area 3 A3-L526.1 formal  prose words +2
  APPLIED  L528  area 3 A3-L528.1 formal  prose words +0
  APPLIED  L556  area 3 A3-L556.1 pointer prose words +1
  APPLIED  L558  area 3 A3-L558.1 formal  prose words -10
  APPLIED  L574  area 3 A3-L574.1 formal  prose words +1
  APPLIED  L584  area 3 A3-L584.1 formal  prose words -11
  APPLIED  L590  area 3 A3-L590.1 formal  prose words +2
  APPLIED  L626  area 3 A3-L626.1 formal  prose words +17
  APPLIED  L628  area 3 A3-L628.1 formal  prose words +2
  APPLIED  L628  area 3 A3-L628.2 formal  prose words +2
  APPLIED  L630  area 3 A3-L630.1 formal  prose words +3
  held with no JSON entry: area 3 OQ1 (E03, D18.1): the cut of 'represented' at L405 and L526's 'no cycle'; not written
lines (newline count) 103: 632; 104: 632; lines differing: 32
md5 104: d0b3987cb89626585a1f6d68c2abc270
S95 residue scan: hits 103 76, 104 78; new hits in 104: 3; of them in S23's forbidden list: 0
  new  L393: accepted x3 [accept]
S96 physical scan: physical-tie words 103 198, 104 196; new in 104: 0
kept: headings 55, defined terms 154, labelled formulas 23 of 103; missing in 104: 0
words: 103 16394, 104 16339 (-55); words outside formulas: 103 15611, 104 15463 (-148)
prose check (104 outside formulas <= 103): yes
```

- Refused: 0. Held: 0 JSON entries. Held with no entry: A3 OQ1's cut of 'represented' (L405, L526 'no cycle').
- A3-L526.1 applied: its span is FC32's dependence edges ('(E) depends on those.'), not OQ1's; A3 did not mark it waiting. Strike it if the orchestrator reads L526 as held whole.
- T9 (L195) applied; its Rep is the one Q1 will stage (X2).
- Prose words added by single changes: A3-L626.1 +17, A3-L395.1 +10 (formal statements with connecting words); the text as a whole has fewer.

## 5. Scans of tests/104

| scan | result |
|---|---|
| S95 residue (FAMILIES of `tests/S95 Scrub - scripts/scrub_apply.py`), new per line | 3 new hits, all 'Accepted' in L393's formal replacement (the symbol Accepted_j, D9.4; family 'accept', allowed as tentative by S23); 0 of S23's forbidden list |
| S96 physical (PHYS of `tests/S96 Repair - scripts/repair_apply.py`), new per line | 0 new (198 → 196) |
| headings, defined terms (**bold**), labelled formulas (\tag) | 55, 154, 23 of 103: none missing |
| words (all) | 16394 → 16339 (−55) |
| words outside formulas | 15611 → 15463 (−148): no more prose |
| md5 tests/104 | d0b3987cb89626585a1f6d68c2abc270 |

## 6. Moves (formal changes answering a challenge that holds, M/W/I or HM/HW/INV; plus text changes applied)

| area | formal changes (count: ids) | text changes applied |
|---|---|---|
| A1 | 20: D2.1', D2.4', D2.6, D3.3', D3.4', D3.6', D4.6', D12.1', D12.7', D12.8', FC02', FC06', FC20', FC30', FC77', FC83', FC2.new1, FC4.new1, FC12.new1, FC101 code (H18) | 10: T1–T10 |
| A2 | 30: D6.3, D6.9, D8.2, D8.3, D8.5, D8.new1, D10.3, D10.6, D5.7, D7.4, E1, D1.4, E2/FC58 (I64), FC21, FC23, FC25, FC33, FC44, FC48, FC50, FC51, FC52, FC53, FC63, FC64, FC65, FC67, FC68, FC104, register I83/I84 (U6) | 13: A2-T1–A2-T13 |
| A3 | 28: D0.2, D9.2/D9.4 (Below), D9.9, D9.10, D11.3, D11.4, D12.1 (H09), D13.3, D13.7, D13.8, D14.1, D14.7, D15.1, D15.2, D15.5, D16.3, D16.5, D18.1, Part XV (D16.XV), FC56, FC70, FC74, FC75, FC80, FC90, FC92, FC94, FC102 | 19: A3-L375.1 … A3-L630.1 |
| **total** | **78** | **42** |

**Moves: 120.** Not counted: A2's FC27 look (FC27 does not hold), A3's D18.2 (FC100, I70 do not hold), D3.5 and D10.4 (unchanged; their moves are A2-T1, A2-T12).

## 7. Files written

`model after round 2/` (model + the two programs); `formal core, after round 2.md`; `formal claims, after round 2.md`, `.json`; `inventions register - addendum after round 2.md` (I122–I160); `owner questions after round 2.md` (25: 8 block a change, Q1 first); `parked after round 2.md` (5); `apply text changes.py`; `tests/104 The semantics, standing alone, after round 2.md`; this report.

## 8. Not done

- X2 not resolved: FC83' and FC12.new1 are not tested under Rep^K or Rep^T (Q1 open).
- A2's own 'not done' stands: FC51 (b) for (F2), (A); A2-02's readings on the text's cases.
- The committed addenda files (FC-E claims, the CT case card) are not rewritten for §3's changed lines.
- `formal claims, after round 2.md` is a table; sources, quotations and looks stay in the committed file and in the .json.
- `model/report.py` is the committed one: it needs `s104_check.py` and `formal claims.json` beside the model, absent here, so a whole-suite run without `--no-write` stops at the write step (nothing written). The per-claim command and `--no-write` runs work.
