# S105 Round 3 — integration report

*Integration agent (a fresh Opus 5.5 agent), 28 September 2026; rule 7 of `results/S105 Round 3 - how the replies will be read, written before sending.md` (read whole first), decisions S20–S41 (S40: fixes are maths and code; S41 never reversed or weakened). Rules on no finding. Inputs: `results/S105 Round 3 - area N - verdicts and formal fixes.md` (commits 1a0edfb, 648c418, 1252964), each area's model copy, runs and text changes (this folder). Every run: PYTHONHASHSEED=0, `-B`, under `timeout`. Nothing written outside `Semantics/`; no earlier text, rule, reply, decision or committed file of an earlier round written.*

## 1. Merge (`model after round 3/`)

Three-way merge (`git merge-file`) of each area's copy against `results/S104 Round 2 - maths after the reading/model after round 2/` (md5s as the rule lists, checked). Run from `model after round 3/`: `python3 -m model.run --claim FCnn --scale 4 --time-cap 45`; whole suite with `--no-write` (as after round 2, `report.py` needs files absent here).

| file (md5, first 8) | base | A1 | A2 | A3 | merged | result |
|---|---|---|---|---|---|---|
| model/claims_b.py | 44992063 | 88ec0c44 | = | a2cdf9e8 | 83e940d4 | one textual conflict: `sel`'s signature (A1 `h_nonempty`, A3 `env`); both kept, conjoined; bodies merged clean |
| model/run.py | f3d491e3 | 2ba55200 | 48928b9a | cbc33844 | 5aecaffe | textual: three import lines, all kept |
| model/core.py | 68c9a65a | = | db053086 | = | db053086 | A2's |
| model/claims_a.py | cba30de2 | = | = | c5b70940 | 805ea33d | A3's + integration: FC14 reads `formal core, after round 3.md` first |
| model/claims_s41.py | 1f07a6a2 | a33f365d | = | = | a33f365d | A1's |
| model/claims_r3a1.py, claims_r3a2.py, e9.py | new | A1 | A2 | A3 | taken | — |
| model/claims_r3a3.py | new | — | — | afbd904d | fc0aacbc | A3's + integration: FC32.new1 reads the formal core after round 3 when present |
| s104_creative_transport.py | cdde2bf3 | 267217c9 | = | = | 267217c9 | A1's (F12) |
| every other file | | = | = | = | = | base |

**Conflicts in substance: none; no named alternatives were needed.** The one shared function, `claims_b.sel` (D12.1), got two conjoined conditions (A1 F5: H ≠ ∅; A3 F2: the environment's further condition), each defaulting to its area's reading; every claim computes as in its area's own run (§2). A2's `core.SLOT_QUANTIFIER` (default "every", D6.3 as it stands) is touched by no other area.

## 2. Claims (scale 4, cap 45 s; whole suite `--no-write`, 628 s, run beside the three area copies)

| run | result |
|---|---|
| the round's start (printout, md5 463685a01f3deeaf8021ac1699448137) | 105 H, 3 CEX, 7 NT of 115 |
| area 1 copy, rerun here | 114 H, 3 CEX, 7 NT of 124: = its runs file, claim by claim (124 rows, 0 differences) |
| area 2 copy, rerun here | 108 H, 3 CEX, 7 NT of 118: = its runs file §1 |
| area 3 copy, rerun here | 113 H, 2 CEX, 7 NT of 122: = its runs file §4 |
| **merged** | **125 H, 2 CEX, 7 NT of 134**; no traceback |

Part by part (label, kind, status): every claim of the merged run equals the start, or equals the one area that changed it; no claim was changed by two areas. Every difference from the start:

| id | start | A1 | A2 | A3 | merged | why |
|---|---|---|---|---|---|---|
| FC18 | CEX | CEX | CEX | H | H | A3 F5 (W8): I94's reading a look, as L554 |
| FC77 | H | H (parts relabelled) | H | H | H | A1 F5: part 1 "no Sel(t;{t},id,∅)" under H ≠ ∅; parts 2, 3 the other choice |
| FC30.new1 | H | H (+ (d)–(f)) | H | H | H | A1: test parts for B8, K3 |
| FC12.new2, FC12.new3, FC13.new1, FC28.new1, FC28.new2, FC84.new2, FC97.new1, FC98.new1, FC104.new1 | — | H | — | — | H | A1 new |
| FC23.new1, FC25.new1, FC47.new1 | — | — | H | — | H | A2 new |
| FC98.new2, FC72.new1, FC80.new1, FC32.new1, FC90.new1, FC102.new1, FC103.new1 | — | — | — | H | H | A3 new |

FC98's printed cycle ("(R) → Con → (R)") and sink list changed (A3), labels and statuses not. FC14 and FC32.new1 rerun after the formal core after round 3 was written: FC14 reads it (118 definition lines, no 'is a cause'), FC32.new1 reads its 114 paragraphs of §§1–16, all mapped; both H. CEX left: FC23 (b), FC63 (c-i). NT left: FC31, FC35, FC89, FC94, FC104, FC105, FC110.

**Under the other readings of D6.3's quantifier** (env `S105_SLOT_QUANTIFIER`; three merged runs at once): some 123 H, 4 CEX; some-exempt 124 H, 3 CEX; some-exempt-set 124 H, 3 CEX (of 134, 7 NT each). The changes from "every" are exactly area 2's (runs file §4): FC62 CEX under all three, FC26 CEX under "some", parts of FC23 (d), FC26, FC34; no claim of area 1 or area 3 changes under any reading.

## 3. The external examples and the creative transport case (from `model after round 3/`, timeout 600 s, exit 0)

| program | merged against the round's printout (body) | against the areas' copies |
|---|---|---|
| `s104_external.py` | identical (md5 86a67664a9a3584351fd4836a4140b69 = printout body): FC-E1–FC-E5 unchanged | = A1, A2, A3 |
| `s104_creative_transport.py` | CT1–CT7 identical; CT8 + five lines, one per reading R1–R5: "T′ (Held computed at the output): …" R1, R3, R5 constructed; R2, R4 neither (A1 F12, K1); nothing else | = A1 (34f908d6c2e0a20a496b86b1105a437f); A2, A3 = printout body (their copies lack F12) |

## 4. Text changes (`apply text changes.py` → `tests/105 The semantics, standing alone, after round 3.md`)

```
input md5 bc14045aae3139df710d8339a9c1c81b (as required); output tests/105 The semantics, standing alone, after round 3.md
changes read: 11 (area 1: 6, area 2: 0, area 3: 5)
applied: 11 on 8 lines; refused: 0
  APPLIED  L49   area 1 R3A1-T2  formal  bytes equal yes  prose words -10  settles: -
  APPLIED  L61   area 1 R3A1-T1  formal  bytes equal yes  prose words -4  settles: -
  APPLIED  L69   area 1 R3A1-T3  delete  bytes equal yes  prose words -2  settles: -
  APPLIED  L69   area 1 R3A1-T4  formal  bytes equal yes  prose words +1  settles: -
  APPLIED  L201  area 1 R3A1-T6  pointer bytes equal yes  prose words -16  settles: -
  APPLIED  L220  area 1 R3A1-T5  formal  bytes equal yes  prose words -3  settles: FC104 (the extent at L220: narrow)
  APPLIED  L375  area 3 R3A3-T5  formal  bytes equal yes  prose words +2  settles: R3A3-01 (= R3A1-03, area 1: ≺_h well founded)
  APPLIED  L397  area 3 R3A3-T1  formal  bytes equal yes  prose words -6  settles: I166
  APPLIED  L397  area 3 R3A3-T2  delete  bytes equal yes  prose words -12  settles: -
  APPLIED  L397  area 3 R3A3-T3  delete  bytes equal yes  prose words -13  settles: -
  APPLIED  L405  area 3 R3A3-T4  formal  bytes equal yes  prose words -1  settles: I162 (Build's 'represented organization')
lines with two or more changes, spans disjoint: L69 (2), L397 (3)
held lines: L255 OQ-R3A2-1 (area 2): L255 held until the owner answers
lines (newline count) input: 632; new: 632; lines differing: 8; empty lines input 283, new 283
md5 new: 5d2b7d869c5d284c4da66a684eb3cb95
S95 residue scan: hits input 78, new 80; new hits: 2; of them in S23's forbidden list: 0; S23-list hits in the whole text: input 0, new 0
  new  L397: accepted x1 [accept]
  new  L405: held x1 [hold]
S96 physical scan: physical-tie words input 196, new 196; new: 0
kept: headings 55, defined terms 154, labelled formulas 23 of the input; missing in the new text: 0; deleted on purpose: 0
words: input 16265, new 16223 (-42); words outside formulas: input 15388, new 15324 (-64)
prose check (new outside formulas <= input): yes
```

- Kinds: delete 3, formal 7, pointer 1; none refused; no whole-line delete. Each applied span compared with its JSON entry byte for byte, and undoing all changes gives each input line back.
- The two new residue hits are symbols: Accepted_j (D9.4; 'accept' is tentative by S23) and Held_ℓ (D18.1). No S23-forbidden word anywhere in the new text.
- Single changes adding words outside formulas: R3A1-T4 +1, R3A3-T5 +2, each a pointer id ("D16.XV)", "D11.3)"); the text as a whole has 64 fewer.
- Rule 6, settled in the text by name: I166 (T1), I162 for Build (T4), I169 (T5), FC104's narrow extent at L220 (R3A1-T5).
- L255 held (R3-Q1); no change proposed it.

## 5. Formal core, claims, inventions, questions

| file | content |
|---|---|
| `formal core, after round 3.md` | round 2's core (md5 96798d3bf3b60da8d67175c39462ef4a) + 33 [r3] marks (A1 18, A2 3, A3 12): D3.3, D4.6, D5.7, D11.2, D11.3, D12.1 (×3), D12.2, D12.3, D13.3, D13.8, D14.7, D18.1 (Held, uniqueness, graph), D0.2; re-based D12.7, D12.8, D12.9, D15.8; notes D6.3, D8.3, D9.6, D9.7, D10.6, D16.XV, E9 |
| `formal claims, after round 3.md`, `.json` | 134 claims; after_round3 per claim (parts, reproduce); r3 marks; FC18, FC77, FC104 restated; FC30.new1 extended; primed ids of FC02, FC07, FC28, FC32, FC36, FC78, FC81–FC83 re-based |
| `inventions register - addendum after round 3.md` | I167–I182 (16, from 17 provisional ids; R3A1-03 = R3A3-01 = I169); table provisional → I |
| `owner questions after round 3.md` | 1, blocking: R3-Q1 (was OQ-R3A2-1), L255, D6.3's quantifier |
| `parked after round 3.md` | none new; P1–P7 untouched |
| `moves after round 3.md` | 29 (18 formal, 11 text) |

## 6. Pairs of fixes that bear on one another

| # | fixes | how | handled |
|---|---|---|---|
| X1 | A1 F1 = A3 F1 (D11.3 well founded); R3A3-T5 (L375); D18.1 "unique (D11.3)" | one fix, two areas; the text change (A3) writes the fix counted under A1 | one [r3] mark; I169 once; counted once |
| X2 | A1 F5 (H ≠ ∅), A3 F2 (surv with Env), A1 F2 (per holding): all D12.1 | conjoined conditions; code `sel(h_nonempty, env)` | combined in D12.1; no claim changed |
| X3 | A1 F6 (H, surv typed as contents) × A3 F2 (surv redefined) | the survival condition is still one condition per member of 𝒯, so the typing holds | noted in D11.2, D12.1 |
| X4 | A1 F2, F3 (per holding; records carry provenance) × D12.4 (L405, L409, area 3's lines) × A3 F6 (DEP Dec → TransferComposite) | consistent: D12.3's record clause is D12.4's rule per holding | none needed |
| X5 | A1 F7 (Held with D12.5's extent) × R3A3-T4 (Held_ℓ(o,c) written at L405) × A1 K2 (L411 unchanged) | T4 points to the Held A1 changed | both in the core; T4 settles I162 for Build |
| X6 | A1 F4 (CT exact) × R3A1-T6 (L201 pointer) × A1 F12 (CT8 under T′) | L201's clause removed; CT8's five T′ lines computed with the merged D12.1 (H nonempty there) | CT8 output = area 1's |
| X7 | A1 F9 ("immediately after") × A3 F7 (D0.2 lists it defined) × A3 F6 (DEP Episode → ImmAfter) | consistent | D0.2 note |
| X8 | A3 F3 (ExplUse defined) × A3 F6 (Build → ExplUse → (E)) × A3 F7 (D0.2: ExplUse out, UsesClaim in) | one change, three places | D0.2, D13.3, D18.1 |
| X9 | R3A1-T1–T4 (L49, L61, L69: Account ∧ ¬Dec) × A1 F5 (H ≠ ∅) × D16.XV | with F5 a link no pair tried is Dec, so Q2's condition reaches it (FC30.new1 (e)) | D16.XV note |
| X10 | R3A3-T1 (L397, I166) × R3A3-T2, T3 (deletes on L397) | one line, spans disjoint | applied together |
| X11 | A2 W3 (R3-Q1, D6.3) × A1 F8 (D3.3 obs ⊥, Q15's convention) × FC22 (b), FC26, FC62 | the weathervane M13 keeps (E) under all four readings; merged runs under each reading change only area 2's claims | §2 |
| X12 | A2 A2-T13 (C_id at L325) × A1 F8, B7, R4-L151, N3 (D3.3 Ident) | C_id's identification is D3.3's Ident; FC28 H in the merged run | none needed |
| X13 | A2 W5 (FC47.new1) × area 1 S-c (D10.6 used by no claim) | FC47.new1 now computes D10.1, D10.6 | — |
| X14 | A2 W4 (I175) × D8.6 Riv_χ | D8.6 asks no offer; not a finding of this round | noted |
| X15 | A1 F11 (D5.7) × R3A1-T5 (L220) × D12.7 Viol | the maths fix and its text change | both applied |
| X16 | A3 F4 (D14.7 δ_c) × D16.4 (𝔈_Θ := {c : Acc(c, p, t, Γ) …}, four data) | the same four-data form stands in D16.4; no finding raised it | not changed (§8) |
| X17 | R3A1-T3 (L69 "an account, " deleted) × L43, L159 ("account" as Acc) | one sense kept | — |

## 7. Moves (rule 16, strict)

18 formal (A1 12, A3 6) + 11 text changes applied = **29**; the areas counted 28: area 3 left D0.2 (F7) uncounted as a register, counted here as a changed definition paragraph answering S-b (M), as round 2's second checker counted D0.2's classing. Not counted: A3 F1 (= A1 F1), re-based claims and definitions, 19 new test claims and test parts, I167–I182, R3-Q1, parked records. **29 moves: the series continues (rule 17).** List: `moves after round 3.md`.

## 8. Not done / for the critical review

- D16.4's 𝔈_Θ applies Acc to four data, as D14.7 did before A3 F4 (X16); no finding raised it; not changed.
- CT8's header in `s104_creative_transport.py` still says "Sel as D12.1 has it after round 2"; its lines are computed with the merged D12.1 (H nonempty there, so F5 changes nothing); not edited.
- The code keeps the checkers' provisional ids (R3A1-05, R3A3-05, …) and B6's label "I168" in comments; the addendum maps them.
- FC102, FC103 keep their NT parts; the built E9 is tested in FC102.new1, FC103.new1.
- The committed addenda (FC-E cards, the CT case card) are not rewritten for CT8's five new lines.
- The whole suite without `--no-write` stops at `report.py`'s write step, as after round 2.

## 9. Files written (md5)

| file | md5 |
|---|---|
| `model after round 3/` (committed as a snapshot at e49250f; unchanged since) | model files as §1 |
| `formal core, after round 3.md` | 2e865d917a0ff1ae98510566229dc738 |
| `formal claims, after round 3.md` | 79eac6bc938e6da937f2d9a7d2482ca0 |
| `formal claims, after round 3.json` | fc8e8c71d30d4208bce5dd5bb69d7f86 |
| `inventions register - addendum after round 3.md` | ee382f99c93b3ebdec626eb28bd05784 |
| `owner questions after round 3.md` | a3aef7a552cae1aba657cda8e605d429 |
| `parked after round 3.md` | 6a50b6b2c96281cbeb4d7ffab33ea79c |
| `moves after round 3.md` | cbcd917f09e6c8baf96be01abce7478b |
| `apply text changes.py` | 0164e28659f2fd8c6ea60caf50d9430c |
| `tests/105 The semantics, standing alone, after round 3.md` | 5d2b7d869c5d284c4da66a684eb3cb95 |
