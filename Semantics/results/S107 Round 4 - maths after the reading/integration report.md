# S107 Round 4 — integration report

*Integration, last part (rule 7 of `results/S107 Round 4 - how the replies will be read, written before sending.md`, with its addendum; both read whole first): a fresh Opus 5.5 agent, 28 September 2026. Decisions S20–S48 read; S40, S41, S43, S44, S45, S46, S47 bind. Read: `integration notes.md` (§§1–9: the areas, the merge, the conflict resolved, the core and claims after round 4, the text changes chosen), the three area files, and the out folders of the Sonnet jobs. Rules on no finding. Written: `tests/107` is Sonnet's (committed here), this file and `moves after round 4.md`. Not written: the text under review or any earlier text, the rule, its addendum, the replies, the decisions, any committed file of an earlier round or step (git: nothing modified; `tests/107` the one untracked file before this commit). Every run: PYTHONHASHSEED=0, `-B`, under `timeout`. "Model" means only the program or its folder (S43).*

## 1. The Sonnet jobs of the integration

| job (spec) | out folder (`sonnet_harness_tests/r4-reading/`) | worker | checking agent | digests | checks failed | result |
|---|---|---|---|---|---|---|
| `r4 merge of the area models` | `r4-merge-area-models` | ok | ok | 6ada1a5a6ddba2b3, equal | none | pass; the one conflict (`run.py`, markers L23, L25, L27) resolved by the second part (notes §9.1) |
| `r4 claim suite, merged` (2d543d80ba508cb8cc4033ace9622b03) | `r4-claim-suite-merged` | ok | ok | a73d07dd1d989cd6, equal | none (15 of 15 pass) | pass |
| `r4 text changes` (6a0c3f25668b17eca0b1614e92c83ecb) | `r4-text-changes` | ok | ok | 694e9def23bd431f, equal | none (23 of 23 pass) | pass |

No job failed and no digest differs, so no cause to find and no rerun in its place. Checked here beyond the jobs (§§2–6).
- **The merge.** Sonnet's merged `model/` against the committed `model after round 4/model/`: 21 files equal. It differs in two files only: `run.py` (markers out, both imports kept, two comment lines) and `corefile.py` (NAME and folder pointed at the core after round 4). Both are as notes §9.1 records.

## 2. The claim suite on the merged program

| run | counts | against `after_round4` (claims json c6fea9d95235cd7483ebc0a0cc8b1afc) | s | raw md5 |
|---|---|---|---|---|
| Sonnet's worker, whole suite | 133 H, 2 CEX, 7 NT of 142 | 142 compared, 142 equal, 0 differences, 0 outside the record | 489.1 | 475b29948825dcf11bce8cec65a81859 |
| Sonnet's worker, spot | 11 H, 2 CEX, 1 NT of 14 | 14 equal | 39.9 | 5e4c366c0ac4af3a1ba93d32ad90a545 |
| **this agent, whole suite** (`run_claims.py`, the spec's own arguments, output in the scratchpad) | 133 H, 2 CEX, 7 NT of 142 | 142 equal, 0 differences; no error; folder unchanged; no `__pycache__` | 497.4 | 68d996163906c44d3777f481314e4362 |

- **The two whole runs** give claims files equal once timings are left out, and raw printouts that differ only in the seconds on each claim line and the total.
- **Why this run.** The job's equal digests cover one whole-suite run and two spot runs (notes §5); the whole suite has now run twice.
- **Which core FC14 and FC32.new1 read**, from the raw printouts (the claims comparison cannot see it): `formal core, after round 4.md`, md5 4f9bef648e2a876be27ac920dd561b54 (worker's raw L335, L1054; spot L6, L12; this run L335, L1054).
- **Their readings.** FC14: 118 definition lines, 0 'is a cause'. FC32.new1: 114 paragraphs, none unmapped. Note 6 is closed.
- **CEX left:** FC23, FC63. **NT left:** 7, as after S106.

## 3. `tests/107 The semantics, standing alone, after round 4.md`

Exists: 106,736 bytes, 632 newlines, no CR, md5 **6e9bd68fb1f98b52a3a02fc896cdc9bd**. This is the md5 the second part computed on a scratch copy (notes §9.3) and the one the job expected. Source `tests/106 …`: c7af964c329ab7959243405d394e6574, unchanged from HEAD. List: `text changes after round 4.json`, a05100798b237684fcf95b5704b4f7aa.

**Each change against its fix, byte for byte** (this agent's script, apart from `apply_changes.py`). Only L271 and L536 differ; the other 630 lines are equal byte for byte.

| id | line | kind | old span in 106's line | 107's line = 106's with old → new | undo gives 106's line | bytes before and after the span equal | at byte |
|---|---|---|---|---|---|---|---|
| R4A2-T1 | 271 | formal | once | yes | yes | yes | 68 |
| R4INT-T1 | 536 | formal | once | yes | yes | yes | 393 |

- **R4A2-T1:** "fails (F2) under the production contract:" → "fails (F2) under the production contract \(C_1\) (E1, FC27):"
- **R4INT-T1:** "fails (F2) under the production contract." → "fails (F2) under \(C_1\)."

**Words** (formulas \( \) and \[ \] stripped, as round 2's appliers do):

| count | 106 | 107 | change |
|---|---|---|---|
| words outside formulas: `apply_changes.py` (Sonnet), `text_scan.py` (Sonnet's check step), `text_scan.py` (this agent), this agent's own regex | 15,204 | 15,204 | 0: **not grown** |
| L271, outside formulas | 42 | 44 | +2 ("(E1,", "FC27):", pointer ids) |
| L536, outside formulas | 117 | 115 | −2 ("the production contract." → ".") |
| all words (harness) | 16,102 | 16,103 | +1 (\(C_1\)) |
| `wc -w`, C locale | 16,074 | 16,075 | +1 |

**Scans** (`text_scan.py`, 106 against 107; Sonnet's and this agent's runs agree):
- S95 residue: 80 → 80, 0 new, 0 on S23's list.
- S96 physical words: 196 → 196, 0 new.
- Headings 55, defined terms 154, labelled formulas 23: none lost.
- No new hit, so there is nothing to rule on.
- Neither change adds "model" (S43), a word S23 forbids, or prose (S40): kinds formal, formal.

## 4. The case scripts on the merged program

Rerun here from `model after round 4/` and, for comparison, from `model after S106/` (timeout 600 s each, exit 0). The message says "both case scripts"; three sit beside `model/`, and all three were run.

| script (md5, equal in both folders) | merged | after S106, rerun here | recorded (S106; round 4's printouts; notes §9.3) | equal |
|---|---|---|---|---|
| `s104_external.py` (2259687a6775b043d3e615de9c4711fc) | 86a67664a9a3584351fd4836a4140b69 | 86a67664a9a3584351fd4836a4140b69 | 86a67664a9a3584351fd4836a4140b69 | yes |
| `s104_creative_transport.py` (dd49e2b0bc0c72fde6c1b93977f73c8e) | d473944e74d2f349b1fdfb83277843cf | d473944e74d2f349b1fdfb83277843cf | d473944e74d2f349b1fdfb83277843cf | yes |
| `s106_cases.py` (5b153417c62c3b17ab275c81d52adcf5) | 043aeb3647a9004ae43009a7fed50b4e | 043aeb3647a9004ae43009a7fed50b4e | 043aeb3647a9004ae43009a7fed50b4e | yes |

- **What the scripts read.** They import `core`, `cases`, `claims_a`, `claims_b`, `claims_r3a2`, `claims_s106` and `e9`, and call none of the functions round 4 changed (grep: `boundary`, `corefile`, DEP, `build_at`, `not_using_E`, `expl_ruled_out`, `no_question_about_brief`: none). So equal outputs show that the merge left what they read as it was.
- **The folders.** Both were unchanged after the runs (md5 of every file); no `__pycache__`.

## 5. md5s

- **Checked by `md5_check.py`:** 39 files, 0 mismatches. They are the inputs of both specs (the 26 files of `model after round 4/`, the claims json, the core after round 4, tests/106, the list), tests/107, the files of notes §9.4, the two build scripts and the two specs.
- **By git:** the rule, its addendum, the replies, the decisions, and the area files and copies are unchanged from HEAD.

## 6. Moves (rule 16, strict)

**8**: 6 formal (A2 F1 D6.3, A2 F2 D7.4, A3 F2 DEP['Build'], A3 F3 and F4 D0.2, A3 F7 Uses at the symbol) and 2 text changes applied (R4A2-T1, R4INT-T1). This equals notes §9.5.
- **Not counted:** A2 F3 (a mark), A3 F1 (a path), A3 F5 and F6 (notation), the re-based and new test claims, I192–I197, K1.
- **Other readings:** 7 to 11. The two text changes alone give 2.
- **Not 0, so the series is not ended by this round (rule 17); S52 governs what follows.**
- Rows and reasons: `moves after round 4.md`.

## 7. Departures, recorded (lesson S19)

| # | what the rule or message names | what was done | why |
|---|---|---|---|
| a | "both case scripts" | all three scripts beside `model/` run | the rule's list of case scripts has three; the external examples are cases too |
| b | the suite on the merged copy is a harness job | this agent also ran the whole suite by the same script (`run_claims.py`, the spec's arguments), into the scratchpad | a check alongside Sonnet's job, not in its place: the job's checking agent re-runs spot claims only |
| c | `r4 md5s`, `r4 key grep` are harness jobs | done here: `md5_check.py` (§5); the orchestrator's key grep before the commit, file names only | as the second part did (notes §9.6 (b)); no spec written for either |
| d | `r4 scans` | run by `apply_changes.py` and the job's check step (Sonnet), and again here | as notes §9.6 (a) |

## 8. For the critical review

- **R4INT-T1** is the integration's own text change (pair 7, rule 7), not an area's; it settles I193 at L536 too.
- **Pair 5:** `build_at` keeps two readings (Held under T and T′; round 2's staged cuts under U and K), with D18.1's [r4: integration; pair 5] mark.
- **A3 F1** answers findings that hold (B14, W6, S1) and is not counted (a path, round 3's practice). Counting it gives 9.
- **A3 F5, F6** are not counted (notation). Counting them adds 2.
- **L271** gains 2 words outside formulas (pointer ids) and L536 loses 2, so the text's total is unchanged.

## 9. Files

| file | md5 |
|---|---|
| `tests/107 The semantics, standing alone, after round 4.md` (written by `r4 text changes`) | 6e9bd68fb1f98b52a3a02fc896cdc9bd |
| `moves after round 4.md` | 4be23e039b8426a58d7247f1048eb228 |
| this file | (a file cannot hold its own md5; see git) |
