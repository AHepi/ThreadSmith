# S107 Round 4 - integration notes (first part: the three areas side by side, the merge spec)

*Integration agent, first part, under rule 7 of `results/S107 Round 4 - how the replies will be read, written before sending.md` and its addendum (both read whole first): a fresh Opus 5.5 agent that built nothing of this round, 28 September 2026. Read: the three area files (`results/S107 Round 4 - area <n> - verdicts and formal fixes.md`), their text changes and expected claims, the diffs of the three program copies against `results/S106 The written-in test taken out/model after S106/`, and the Sonnet results of `r4 claim suite, area <n> copy` (scratchpad `sonnet_harness_tests/r4-reading/`). Decisions S20-S48 read; S40, S41, S43, S44, S45, S46, S47 bind. Written here: this file and `tools/sonnet_harness/specs/r4 merge of the area models.json`. Nothing else: no text, maths, program copy, rule, reply or earlier file. Nothing is decided here that rule 7 gives the integration (conflicts, invention numbers, the core and claims after round 4, text changes); §6 lists them for the second part. "Model" means only the program or its folder (S43).*

## 1. What each area changed

| area | lines | findings: M / W / I / N | formal core | program copy | text | inventions (provisional) | moves (area's count) | suite on the copy | commit |
|---|---|---|---|---|---|---|---|---|---|
| 1 | L1-L228 | 15: 4 / 0 / 2 / 9 | none (D12.2, D13.8 [S47] notes stand) | `claims_s41.py`: `no_question_about_brief`; FC84.new1 (a3). `claims_a.py`: FC31 re-based (NT) | none | R4A1-01 | 0 | 128 H, 2 CEX, 7 NT of 137 | 6a00be4 |
| 2 | L229-L372 | 20: 7 / 2 / 3 / 8 | D6.3 (F1: "t translates (a,b)" inside the ∀); D7.4 (F2: Acc((E_v, p, t_v, Γ_v, δ_v)), δ_v carried); D6.9 mark (F3, not counted) | `core.py`: `boundary(family)` (new function). `claims_r4a2.py` (new): FC27.new1, FC23.new4, FC23.new5, FC42.new1, `PartialPi` (test only). `run.py`: import | R4A2-T1, L271, formal (settles R4A2-01) | R4A2-01, R4A2-02, R4A2-03 | 3 (F1, F2, R4A2-T1) | 132 H, 2 CEX, 7 NT of 141 | 204159a |
| 3 | L373-L632 | 24: 9 / 0 / 0 (row 9 also I) / 15; K1 settled | D18.1 T′ item and note (F2); D0.2 (F3: "subhistory" out; F4: D16.XV's five undefined terms in); D9.10 δ_c → δ_Conn (F5, notation); D16.XV (Elim) κ → kl (F6, notation); D16.XV's Uses read at the symbol (F7, the program's reading; R4A3-01) | `corefile.py` (new); `claims_a.py`: FC14 through it; `claims_r3a3.py`: `core_def_ids`, FC32.new1; `claims_b.py`: DEP Build → Held, Episode, DefeatConds, `D0_2_R4A3`, FC98 statements; `claims_s41.py`: `USES_READINGS`, `not_using_E`, `expl_ruled_out`, FC30.new1 (h); `claims_r4a3.py` (new): FC72.new2; `run.py`: import | none | R4A3-01, R4A3-02 | 4 (F2, F3, F4, F7); 3 if F3 and F4 count as one change of D0.2 | 129 H, 2 CEX, 7 NT of 138 | 069d75d |

- **All areas:** 59 findings, plus K1. Moves by the areas' counts: 7, or 6 with D0.2 counted once. Neither count is 0 (rule 17).
- **Owner questions:** none. Nothing new parked.
- **Flagged proposals:** none taken. No area took a proposal that reverses S41, puts the written-in test back (S44, S45), or has the maths ask for a criticism event (S47).
- **K1** (addendum): area 3 computes FC72.new2 and reads the owner's words as settling it (S44, S45 with S28, S21, S27, S41 Q23). No owner question and no text change: L317 and L397 already say it.

## 2. The claims

| change | claims | area |
|---|---|---|
| new claims (all H) | FC27.new1, FC23.new4, FC23.new5, FC42.new1 | 2 |
| new claim (H) | FC72.new2 | 3 |
| new parts | FC84.new1 (a3) | 1 |
| new parts | FC30.new1 (h) | 3 |
| re-based statement, status unchanged | FC31 (NT) | 1 |
| re-based statement, status unchanged | FC98 (a), (a′); FC32.new1 (c) classes `D0_2_R4A3` | 3 |
| core read through `corefile.py` (name and md5 printed) | FC14, FC32.new1 | 3 |

- **The three records compared by program.** On every claim id the three expected-claims files share, the statuses and parts are equal, except for the two new parts: FC84.new1 (a3) (area 1) and FC30.new1 (h) (area 3). Area 1 adds no id; area 2 adds 4; area 3 adds 1.
- **Merged program, predicted:** 142 claims, 133 H, 2 CEX (FC23, FC63), 7 NT. The prediction rests on §3's call check, not on a run; `r4 claim suite, merged` decides.

## 3. The program: who touched which file, and the merge

| file | area 1 | area 2 | area 3 | merge (the spec's known answer) | from the diffs |
|---|---|---|---|---|---|
| `claims_a.py` | FC31's return line (base L1254-L1260) | - | FC14's body (base L521-L546) | merged clean | the two hunks are about 700 lines apart |
| `claims_s41.py` | inserts after base L185 (`no_question_about_brief`) and after L228 (FC84.new1 (a3)) | - | L9-L14, L33-L43, L161-L167; inserts after L171 (FC30.new1 (h)) | merged clean | base L172-L185, 14 lines, lie unchanged between the nearest hunks |
| `run.py` | - | import `claims_r4a2`, after base L22 | import `claims_r4a3`, after base L22 | **CONFLICT, 1 hunk** | both insert at the same place |
| `core.py` | - | `boundary` inserted after base L886 | - | taken (area 2) | |
| `claims_b.py` | - | - | DEP, `D0_2_R4A3`, `dep_edges` docstring, FC98 | taken (area 3) | |
| `claims_r3a3.py` | - | - | `core_def_ids`, FC32.new1 | taken (area 3) | |
| `claims_r4a2.py` (new) | - | new | - | taken (area 2) | |
| `claims_r4a3.py`, `corefile.py` (new) | - | - | new | taken (area 3) | |
| the other 14 files of `model/` | - | - | - | base | |
| `s104_external.py`, `s104_creative_transport.py`, `s106_cases.py` (beside `model/`) | unchanged | unchanged | unchanged | not merged (merge_models.py reads `model/` only); the base's | md5-equal in all four folders (inputs of the spec) |

No source file holds a line that looks like a conflict marker, and git has no `merge.conflictstyle` set.

**Calls across areas** (grep of the three copies): no claim of one area reads code another area changed. The only shared files are the ones merged above.
- **Area 2's `claims_r4a2`** imports from `core` (its own `boundary` among them), `gen`, `cases`, `harness`, `claims_s106`, and from `claims_a` (`SMALL`, `BOTHFAM`, `D_and_p`, `pole_contracts`, `_T`). None of these was changed by area 1 or area 3.
- **Area 3's `claims_r4a3`** imports `core.slot`, `pins`, `account`, `NC1`, `conflict_pairs`, `problem_kind`, `rivals`, plus `args`, `claims_s106` and `claims_a._T`. Area 2 only added `boundary`.
- **Area 1's FC84.new1 (a3)** calls `no_brief_question`, `prov_fixed_points`, `chain_eps`, `build_at` and `EPISODE_READINGS`. Area 3's `claims_b.py` hunks touch only DEP, `D0_2_R4A3`, the `dep_edges` docstring and FC98.
- **Area 3's `not_using_E` and `expl_ruled_out`** are called by FC30.new1 and by `claims_s106` L152 (FC23.new2 (f)); area 3's suite shows FC23.new2 unchanged. `core.boundary` is called only by `claims_r4a2`.

## 4. Pairs of fixes that bear on one another

| # | fixes | where they meet | what the files show | left for |
|---|---|---|---|---|
| 1 | A2 `run.py` / A3 `run.py` | the two import lines, after `claims_s106`'s | the one merge conflict; both areas: keep both | 2nd part |
| 2 | A1 FC31 / A3 FC14, in `claims_a.py` | one file | different hunks: merged clean | - |
| 3 | A1 (`no_question_about_brief`, FC84.new1 (a3)) / A3 (`not_using_E`, `expl_ruled_out`, FC30.new1 (g), (h)), in `claims_s41.py` | one file | different hunks; neither calls the other | - |
| 4 | A3 F2 (DEP: Build → Held, every reading) / A1 FC84.new1 (a3) (Build by `build_at` under T′) | the reading of Build | `build_at` under T′ returns `held[o]` (claims_b L1784): the same reading; (a3) unaffected | - |
| 5 | A3 F2 / `build_at` under U and K (FC83) | the reading of Build, in two places | the program reads Build two ways: DEP as Held under every reading, `build_at` staged under U and K. If `build_at` read Held, FC83 (a) would give a counterexample under K (A3 runs §3.6), the defect K was rejected for (FC98 (d)). Area 3 left it | 2nd part / review |
| 6 | A3 F1 (`corefile.py`) / A1, A2 copies / the core after round 4 | which formal core FC14 and FC32.new1 read | see note 6 below | 2nd part |
| 7 | A2 R4A2-T1 (L271) / L536 (area 3's lines; no area 3 finding names it) | "a reversed calculation fails (F2) under the production contract" | the same words; L536 ends in "."; left as they are, the two lines read "the production contract" two ways. `apply_changes.py` checks that a span is unique within its line, so a parallel formal change at L536 is possible (old span ending "."; it would settle R4A2-01 there too) | 2nd part |
| 8 | A1 F1 (FC31) / A3 N4 (L536's "the four") / A2 N5, B2 (D6.5) | D6.8's headings | D6.5 and D6.8 are unchanged, so FC31 stands as area 1 re-based it. Pair 7's span at L536 is not FC31's "all four conditions of (E)" | - |
| 9 | A2 F2 (δ_v in D7.4; R4A2-03) / A3 F5 (δ_c → δ_Conn in D9.10) / S-δ's P9 (not taken) | the letter δ | after both: δ alone is the alleged defect (D9.10); a subscripted δ is the designation of the organization named (δ_D, δ_E, δ_c in D14.7, δ_v of E_v, δ_Conn) | core writer: one check of D7.4 |
| 10 | A2 F1 (D6.3) and R4A2-02 (Pin) / A3 FC72.new2 (a) (the myth's Slot 'every' and pins) | D6.3, `core.slot`, `core.pins` | `core.slot` and `core.pins` are unchanged. F1 brings D6.3 to `core.slot`; R4A2-02 keeps Pin as registered (I184); FC72.new2 reads the same code in the merge | - |
| 11 | A3 F3, F4 (D0.2) / A3 F6 (kl) | D0.2 | F4 writes Work(kl), F6's letter; counted as 2 changes or 1 | 2nd part (count) |
| 12 | A3 F2, F3, F4 (DEP entries) / area 2's D18.1 (DEP unchanged: "(D)" reaches δ through (E) → Dep → δ) | `claims_b.DEP` | only area 3 edits the table | - |
| 13 | A1 R4A1-01, FC84.new1 (a3) / A3 B12 (not taken) | D13.8's [S47] note, "because the agent asked" | both bear on the note's wording; neither changes a value of (EX), Con or Build; area 1 keeps the note as written | core writer |
| 14 | A2 W4 (F3: D6.9's quote is text 103's, marked) / A3's note (the quote above D9.7 still carries L397's old words; D9.7's [S106] mark records it) | quoted spans in the core | one convention (the core's preamble: quotes are text 103's; marks name the later change) | core writer: both alike |
| 15 | A3 F7 (R4A3-01) / FC23.new2 (f) / A2's C-K3, B15 (FC23.new2 (a), (b), (e)) | `expl_ruled_out` | FC23.new2 is unchanged under the new default (area 3's suite); area 2's new claims do not call it | - |
| 16 | A3 K1 (FC72.new2, R4A3-02) / A2's L317 (S106-T8, not ruled by area 2; addendum 1) | L317, L397 | no area changes either line | - |
| 17 | A2 F2 (δ_v carried) / D14.7 (I180), D16.4 (I183) (∃δ) | the designation of a changed candidate | a different choice for a different use; recorded as R4A2-03's other choice (a) | - |
| 18 | ids and inventions | FC84.new1 (a3); FC27.new1, FC23.new4, FC23.new5, FC42.new1; FC72.new2, FC30.new1 (h) | no id clashes. Six provisional inventions (R4A1-01; R4A2-01 to 03; R4A3-01, 02); the next free number is I192 (rule 6) | 2nd part |
| 19 | A1 R4A1-01 (d), (e) / S51 (on hold, S52) | "questions occurring to the agent" | a pointer only | - |

**Note 6** (pair 6):
- **What the copies read.** On the area 1 and area 2 copies, FC14 and FC32.new1 read round 3's core by the old fallback; the Sonnet runs show it (§5). After the merge, `corefile.py` decides.
- **What `corefile.py` still names.** Its `NAME` is "formal core, after S106.md", and its second place is the folder "S106 The written-in test taken out". From `model after round 4/model/` it would read S106's core. Pointing both at the core after round 4 is the second part's job (area 3 §10).
- **From the scratchpad**, no place exists: FC14 and FC32.new1 (a) would come out not tested. So `r4 claim suite, merged` runs from `model after round 4/`.
- **FC32.new1 (a)** maps D18.1's nodes against the core's 114 paragraphs; the core after round 4 has to keep that map.

## 5. What the Sonnet suites showed

| area | spec | suite (s) | counts | against the checker's record | spot re-run | copy's folder | worker and checking agent digests | result |
|---|---|---|---|---|---|---|---|---|
| 1 | `r4 claim suite, area 1 copy` | 508 | 128 / 2 / 7 of 137 | 137 of 137 equal (key area1_r4) | 10 claims (7 H, 2 CEX, 1 NT: FC31), equal | unchanged, no `__pycache__` | 6eb29fc31a51d7b1, equal | pass |
| 2 | `r4 claim suite, area 2 copy` | 505 | 132 / 2 / 7 of 141 | 141 of 141 equal (key after_r4a2) | 12 claims (9 H, 2 CEX, 1 NT: FC31), equal | unchanged, no `__pycache__` | 9ec4d14372a82217, equal | pass |
| 3 | `r4 claim suite, area 3 copy` | 472 | 129 / 2 / 7 of 138 | 138 of 138 equal (key area3_r4) | 10 claims (8 H, 2 CEX), equal | unchanged, no `__pycache__` | 473328ba9fdf2ad6, equal | pass |

- **No differences.** No record differs from its checker's, and nothing goes back to an area.
- **Which core FC14 and FC32.new1 read**, from the raw printouts:

  | copy | core read | raw.txt lines |
  |---|---|---|
  | area 1 | `formal core, after round 3.md` | L335, L993 |
  | area 2 | `formal core, after round 3.md` | L335, L1045 |
  | area 3 | `formal core, after S106.md` (md5 40d7c80ec78574794962fece34a4cb51) | L335, L1002 |

  This is area 3's B14/W6/S1 finding, seen in the harness's own runs. The records hold statuses and parts only, so the comparison could not see it.
- **What the equal digests cover.** The whole suite ran once per area, by the worker. The checking agent re-ran the spot claims and re-read the worker's `suite.json`. So the equal digests mean the two agents' checks agree on that one suite output and on two independent spot runs; the whole suite was not run twice.
- **A gap in area 2's spec.** It has no "did not time out" or "claims compared" check; areas 1 and 3 have both. Its `suite.json` shows `timed_out` false, and its `spot.json` compared 12 claims.
- **Raw printout md5s** (suite, spot): area 1 caa1809371ae1edb952088ec11862535, e21b05f9eac6f1b2525961af4d09aa24; area 2 bd85617f0df833a1008725cdaf4075a9, b035c0647d91826ee1d66802de770f85; area 3 7ad3923561ef20ed70c7acafc6c1f5ef, b0ff8a1921f7904b224952cc1c7be9d6.

## 6. For the second part (rule 7; none decided here)

1. Resolve `run.py`, after the merge job hands back (pair 1).
2. Write `model after round 4/`:
   - `model/` from the merged folder;
   - the three case scripts from `model after S106/`;
   - `corefile.py`'s `NAME` and second place pointed at the core after round 4 (note 6).
3. The formal core after round 4, as a new file. Area 1 changes nothing. The changes:
   - area 2: D6.3 (F1), D7.4 (F2), D6.9's mark (F3);
   - area 3: D18.1 (F2), D0.2 (F3, F4), D9.10 (F5), D16.XV (Elim) (F6), D16.XV's Uses (F7, R4A3-01);
   - pairs 9, 13 and 14 for the core writer.
4. The formal claims after round 4 (§2), and the claims file for `r4 claim suite, merged` (predicted 133 / 2 / 7 of 142).
5. Number the six inventions, from I192 (pair 18).
6. The text:
   - R4A2-T1 at L271;
   - L536 (pair 7);
   - the specs `r4 text changes` and `r4 scans`.
7. `build_at` and FC83 (pair 5).
8. The moves count, 7 or 6 (pair 11).

## 7. The merge spec

`tools/sonnet_harness/specs/r4 merge of the area models.json`, modelled on `r2 merge of the area models.json`.

**Inputs** (98, each with its md5):
- the base's `model/`: 20 files;
- the three copies' `model/`: 20, 21 and 22 files;
- the case scripts beside `model/`, in the base and in each copy: 12 files, md5-equal across the four folders;
- `merge_models.py`, `hcommon.py`, `md5_check.py`.

**What it runs:**
- **Step:** `merge_models.py --base "model after S106/model" --area A1=… --area A2=… --area A3=… --out {OUT}/merged` (300 s).
- **Check step:** `md5_check.py` on the 20 files taken whole: 14 from the base, 6 from one area (120 s).
- **Checks** (19): the known answer of §3, read from the diffs, not from a run. They are: 23 files, 9 changed; each of the 8 files taken or merged clean, as a whole row; `run.py` in conflict, changed by A2 and A3, 1 hunk, 3 marker lines; the merge reports the conflict; the 20 md5s.

A difference from the known answer escalates to Opus. When every check passes, the `run.py` conflict still goes to Opus.

**A departure from the message, recorded (lesson S19).** The message asked for the merge "into … model after round 4/". But `merge_models.py` writes only in the scratchpad: `hcommon.guard_write`, with no flag for Semantics/. So the merged folder is `{OUT}/merged/model/`, and `model after round 4/` is written by the second part once the conflict is resolved. A folder with conflict markers never enters the repository. Rule 7 and the harness table name only `merge_models.py` and "every conflict (Opus resolves it)".

**Checked here:**
- `run_task.py --phase validate` under a run label of its own, int1-selfcheck: inputs ok, no command run;
- the brief printed under `--run r4-reading`.

The job itself was not run.

## 8. Unsure

- "Merged clean" for `claims_a.py` and `claims_s41.py` is read from where the hunks sit, not from git merge-file. If git says otherwise, the job escalates.
- 133 / 2 / 7 of 142 rests on the call check of §3, not on a run.
