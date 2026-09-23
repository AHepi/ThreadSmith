# Stage B, recomputed independently

This folder holds the independent check for stage B of plan W10, run under plan W14. It computes stage B's counts a second time, from the frozen texts and the raw marks only. Another worker is running the harness's own collection programs on the same marks. The two results are meant to be compared field by field. None of the harness's marker or agreement code was read (the full list of what was read is in section 3).

Run it with:

```
/home/user/.venvs/threadsmith/bin/python recompute.py
```

It uses the standard library only and takes about five seconds. It writes `output.json` (every count, with every disagreeing and unreadable report named) and `output.txt` (the same, readable). It writes nothing else.

## 1. What the program does

1. **Pairs the marks.** Each first mark `M###` is matched to its run id through `marking1/index.json`. Each second mark `R###` is matched through `marking/secret_mapping_record96.json`. Both sides turn out to cover the same 96 run ids, with no document mismatches. The sets are p52 48; rep, rep31, son and son31 12 each.
2. **Checks the freeze.** All 28 marker-read fields are checked in all 192 prompts. Each field's criterion, heading, kind, per, layer and closed list appears word for word as `criteria.json` has it. The version string is `W10-A4-4` in criteria.json, in the index and in the mapping. No prompt asks a marker for a field that a program fills. No marker's `shape` breaks the rule that derives it from its own seven elements.
3. **Applies the agreement rule** field by field (marking plan section 5; `criteria.json` `agreement.per_kind`):
   - enum and int fields agree when the two values are equal;
   - a set agrees when the two sets are equal, with exact strings, so `A|B` is not `B|A`;
   - a map_enum field agrees when the whole map is equal;
   - text fields are never compared;
   - a report where either side is null or missing is **unreadable**. It is named and never counted as agreement.
   - A struck mark (W10.18) would make that marker's report unreadable on every field. There are none.
4. **Counts agreement per field** in each set of 48 (p52; rep+rep31+son+son31), with the pooled 96 beside. It then applies the thresholds of marking plan section 6 per set: a field is certified only when it reaches its threshold in **each** set of 48.
5. **Computes the split** of W14 section 3 for the fields reworded twice or more (`marks_per_part`, `pairs_that_pull`, `rivals_built`; addendum 15 adds none). It gives agreement over all 96, over the read reports and over the unread reports, under five readings of "read" (section 5, A1).
6. **Counts W10.17** per enum field per marker: closed-list values, nulls and off-list values.
7. **Applies W10.18** from `tool_audit.json`, including its `M085_rerun` block.
8. **Runs the rival checks** in section 6. They change no tick. They say what a tick can and cannot be read as.

Not counted: `modules_served`, `requests`, `request_text_saved` and `ports_set`. `record_adapter.py` and the criteria mark these as filled by program from the run record for both sides. Any agreement on them would hold by construction, and none of them is a certified candidate.

The program was checked in two ways:

- **A second route.** A separate minimal script, sharing no code with the program, reproduced the counts on ten fields in both sets.
- **A test of the rig.** An outside read was planted on R019 in a copy of the audit. The program struck that report (p52_I2-m2 became unreadable), and the unplanted run still agreed. It also treats `["A|B","C|D"]` and `["C|D","A|B"]` as equal and `A|B` and `B|A` as different.

## 2. Results

Counts are of agreeing reports, as agree / disagree / unreadable. They are never summed across fields or sets.

| field | threshold | p52 (48) | repeat (48) | pooled 96 | certified |
|---|---|---|---|---|---|
| test_remove | 39 (see A3) | 46/2/0 | 48/0/0 | 94/2/0 | yes |
| test_swap | 42 | **40**/8/0 | 48/0/0 | 88/8/0 | **no** |
| test_poke | 42 | **39**/9/0 | **38**/10/0 | 77/19/0 | **no** |
| test_flip | 39 | 47/1/0 | 47/1/0 | 94/2/0 | yes |
| test_reverse | 39 | 41/7/0 | 42/6/0 | 83/13/0 | yes |
| test_hunt | 39 | 47/1/0 | 47/1/0 | 94/2/0 | yes |
| test_addjob | 39 | 39/9/0 | 43/5/0 | 82/14/0 | yes (on the line in p52) |
| test_rival | 39 | 41/7/0 | 48/0/0 | 89/7/0 | yes |
| test_pull | 39 | 44/4/0 | 46/2/0 | 90/6/0 | yes |
| test_patches | 39 | 41/7/0 | 48/0/0 | 89/7/0 | yes |
| test_inside | 39 | 40/8/0 | 40/8/0 | 80/16/0 | yes |
| shape_elements | 39 | **35**/13/0 | 41/7/0 | 76/20/0 | **no** |
| shape | 44 | 48/0/0 | 46/2/0 | 94/2/0 | yes |
| turned_own_test | 44 | 45/3/0 | 47/1/0 | 92/4/0 | yes |
| same_explanation | 44 | 48/0/0 | 47/1/0 | 95/1/0 | yes |
| marks_per_part | 40 | **37**/10/1 | 44/4/0 | 81/14/1 | **no** |
| pairs_that_pull | 40 | 47/1/0 | 46/2/0 | 93/3/0 | yes |
| rivals_built | 40 | **36**/9/3 | 41/3/4 | 77/12/7 | **no** |
| remove_in_groups | 39 | 47/1/0 | 45/3/0 | 92/4/0 | yes |
| question_identity | 46 | **1**/0/47 | **3**/1/44 | 4/1/91 | **no** |
| modules_self_reported | 39 | 47/1/0 | 47/1/0 | 94/2/0 | yes |
| attributions | 39 | 39/9/0 | 41/7/0 | 80/16/0 | yes (on the line in p52) |
| marks_outside_closed_list | not a candidate | 40/5/3 | 46/2/0 | 86/7/3 | - |
| layer_at_fault | not a candidate | 35/11/2 | 31/17/0 | 66/28/2 | - |

- **Certified (16):** test_remove, test_flip, test_reverse, test_hunt, test_addjob, test_rival, test_pull, test_patches, test_inside, shape, turned_own_test, same_explanation, pairs_that_pull, remove_in_groups, modules_self_reported, attributions.
- **Struck (6):** test_swap, test_poke, shape_elements, marks_per_part, rivals_built, question_identity.

Every disagreeing and unreadable report is named, field by field, in `output.txt` and `output.json`. That is so the comparison with the harness can go report by report.

### The predictions of W14 section 4, ticked

| prediction | verdict | the numbers |
|---|---|---|
| **W3 P3.1** (shape, turned_own_test, same_explanation: at least two of three at 44, per set) | **holds** | shape 48 and 46; turned_own_test 45 and 47; same_explanation 48 and 47. All three reach 44 in both sets, so it holds under both readings (A4). |
| **W3 P3.2** (marks_per_part, pairs_that_pull, rivals_built each 40, per set) | **fails** | marks_per_part 37 (p52) and 44; rivals_built 36 (p52) and 41; pairs_that_pull 47 and 46. marks_per_part and rivals_built are kept as quotes only; pairs_that_pull is certified. |
| **W3 P3.3** (question_identity 46, per set) | **fails** | 1 of 48 (p52) and 3 of 48 (repeat); unreadable on 47 and 44. W10.17 names the field unreadable. See section 6, E1, for where the failure sits. |
| **W3 P3.4** (at most one second rewording) | **fails** | Failed on the count before any mark existed: marks_per_part twice, pairs_that_pull twice, rivals_built twice (three times on the stricter reading of marking plan 13.5). This is recorded and not re-read (W13 section 2; W14 section 4). It was not computed from marks. |
| **W3 P3.5** (test_swap and test_poke each 42, per set) | **fails** | test_swap 40 (p52) and 48; test_poke 39 and 38. Both leave the within-step set (A5, A6). |
| **The other fields at 39** | **fails** on one field | shape_elements 35 (p52) and 41. Every other field at 39 reaches it in both sets: test_remove 46/48, flip 47/47, reverse 41/42, hunt 47/47, addjob 39/43, rival 41/48, pull 44/46, patches 41/48, inside 40/40, remove_in_groups 47/45, modules_self_reported 47/47, attributions 39/41. test_addjob and attributions sit exactly on 39 in p52. |
| **W10.16** (read minus unread no more than 10 points on the twice-reworded fields) | **fails** | On the primary read set (B, 26 reports), rivals_built is read 23/26 (88.5%) against unread 54/70 (77.1%), **+11.3 points**; counted over readable reports, 95.8% against 83.1%, +12.8. marks_per_part is +5.6 and pairs_that_pull −6.3. The verdict "fails" holds under all five readings and both bases, but the field it fails on changes with the reading (A1). The consequence: rivals_built on the unread reports only, p52, is 31/43 against 36 needed, so it is struck. It is struck by P3.2 already. |
| **W10.17** (a closed-list value on at least 95 of 96 on every enum field, both markers) | **fails** on question_identity | First marker: 10 closed-list values, 86 nulls, 0 off-list. Second marker: 14, 82 and 0. No off-list value occurs on any enum field. Every other enum field is at 95 or above on both sides (layer_at_fault 95 and 95; marks_per_part, if counted as an enum field, 95 and 96). question_identity is unreadable for this stage and is named. |
| **W10.18** (reads of the skill and the prompt only; more than three outside reads and the stage re-runs) | **holds** | 0 markers read another file and 0 marks are struck, so no re-run. The audit holds 192 transcripts (96 first, 96 second): Read 1536, Write 191, StructuredOutput 191, key hits 0, strikes []. M085's first run wrote nothing. Its rerun read 8 files, none outside, and wrote M085.json. The markers' own `files_read` lists (192 of them, claimed rather than seen) agree: none reads outside the skill and its own prompt. |

### The consequences of marking plan section 6, as written

- **P3.1 holds**, so the cross-step fields may carry an arm difference where they are certified.
- **P3.5 fails on both fields.** test_swap and test_poke leave the within-step set. Section 6 says P4.4 is then read on test_remove, shape, shape_elements, marks_per_part, question_identity, modules_self_reported and attributions. Of those seven, stage B certified four: test_remove, shape, modules_self_reported and attributions (A6).
- **P3.2:** marks_per_part and rivals_built are kept as quotes only.
- **P3.4:** failed before marking and recorded (W13, W14). It is not applied a second time.

## 3. Every file read

All paths below are under `/home/user/ThreadSmith/`.

**The skill, all eight files, read in full.** These are in `HV Skill/authority/33/hard-to-vary/`: `SKILL.md`, `references/building.md`, `by-domain.md`, `question-bank.md`, `reporting.md`, `testing-against-cases.md`, `the-idea-in-depth.md` and `word-list.md`.

**The texts that fix the rule:**
- `Workflow/tests/W14 Plan - stage B, the instrument certified on the 96 reports by two blind Sonnet 5 markers.md`, in full.
- `Workflow/tests/W13 Addendum to W10 - the fix loop runs until no fault is found, every round a saved version (decision W11).md`, in full (it is 24 lines).
- `Workflow/tests/W10 Plan - getting the LLM theory right; the harness, the corpus, the fourth clause, the instrument, the arms, the cross-examination.md`: only lines 16 to 45 (sections 3 to 5), read because W14 section 4 reads P3.1 to P3.5 "as W10 section 5 restates them". Its headings were listed by grep.
- `Workflow/rigs/W10 harness/instrument/marking-plan.md`, in full.
- `Workflow/rigs/W10 harness/instrument/criteria.json`, in full.

**Allowed harness files, read in full:**
- `Workflow/rigs/W10 harness/code/record_adapter.py`, read only for the set tags, the run-id rule `<set>_<stem>` and the four fields filled by program.
- `Workflow/rigs/W10 harness/code/README.md`.
- `Workflow/rigs/W10 harness/code/CRITERIA-SCHEMA.md`.

**The marks and what pairs them:**
- `Workflow/rigs/W10 harness/stage-B/w10/marking1/index.json`.
- `Workflow/rigs/W10 harness/stage-B/w10/marking1/marks/M001.json` to `M096.json`, all read by program.
- `Workflow/rigs/W10 harness/marking/secret_mapping_record96.json`.
- `Workflow/rigs/W10 harness/stage-B/w10/marking2/marks/R001.json` to `R096.json`, all read by program.
- `Workflow/rigs/W10 harness/stage-B/w10/marking1/prompts/M001.txt` to `M096.txt` and `marking2/prompts/R001.txt` to `R096.txt`. All 192 were read by program, for the freeze check and their section headings. `M001.txt` was also read in part by eye.

**The audit, and the markers' own returns:**
- `Workflow/rigs/W10 harness/stage-B/tool_audit.json`.
- `Workflow/rigs/W10 harness/stage-B/returns.json`, read by program for each return's `files_read`, `nulls` and missing result. It is not on the forbidden list. It is the markers' own claim and is used only as a cross-check.
- `Workflow/rigs/W10 harness/stage-B/returns_M085_rerun.json`.

**One line of the stage-B workflow.** `Workflow/rigs/W10 harness/workflows/llm-theory-stage-b.js` was grepped for the skill's file names. The one matching line, line 27, was read to settle which skill files the markers were told to read (section 6, E6). Nothing else in it was read.

**Directory listings only** (names, no contents): the skill folder, `Workflow/tests/`, `Workflow/rigs/W10 harness/`, `instrument/`, `code/`, `workflows/`, `stage-B/` and `stage-B/w10/` with its subfolders. The listing of `stage-B/` shows a `collection` folder. It was not opened.

**Not read:** `code/agreement.py`, `code/stage_b.py`, `code/second_marker.py`, `code/first_marker.py`, `code/marks.py`, any file under `marking/` other than the mapping, and anything under `stage-B/collection/`.

## 4. How the numbers were checked

- **The pairing:** 96 and 96, the same run ids and the same documents.
- **The freeze:** all 192 prompts carry every marker field of `criteria.json` word for word, and the version is the same in all three files.
- **A second route:** a separate script counted ten fields and matched on all ten.
- **A planted fault:** one planted strike was caught, and its unplanted neighbour was left alone.

What this does not show: that the harness's programs compute the same numbers. That is the comparison this folder exists for.

## 5. Where the texts can be read two ways

For each place below: the reading chosen, the other reading, and which counts change. Both were run wherever the other reading can be computed.

**A1. Which reports are "read" (W14 section 3).** W14 defines them as "the record files named anywhere in `criteria.json` and `marking-plan.md` (placeholders like `X.json` excluded), mapped to run ids by set". Five readings were computed:

- **A.** Names written as record files only (`runs_repeat/F4-m1-r1`, `runs/C5-m1.json` and so on). 20 reports: p52 4, repeat 16.
- **B (primary).** A, plus the run ids that section 14.1 names directly (`rep31_P3-m2-r2`, `p52_I2-m2` and others). A run id names a record file by the adapter's own rule, and W14 says "anywhere". 26 reports: p52 5, repeat 21.
- **C.** B, plus the bare stems at marking plan lines 415, 417 and 521 (`F4-m2-r3`, `F4-m1-r2`, `F4-m1-r3`), taken in every set that has them. 34 reports. This is the weakest reading, because in context those stems are the fitting reports already named with their folder.
- **D.** W13 section 2's own definition: names in the marking plan's sections 13 onward only. 20 reports.
- **E.** W14's purpose sentence ("the reports any maker or reviewer read"). The marking plan says A4 read all 24 of runs_sonnet5 and runs_repeat (section 10: "Read all 24 for the strict pattern"), so E is B plus all of rep and son. 34 reports.

What changes: W10.16 fails under every reading and on both bases, but **the field it fails on moves with the reading**. The read-minus-unread gaps are:

| reading | marks_per_part | pairs_that_pull | rivals_built | fails on |
|---|---|---|---|---|
| A | +19.7 | −2.4 | +6.1 (+9.9 of readable) | marks_per_part |
| B | +5.6 | −6.3 | +11.3 (+12.8 of readable) | rivals_built |
| C | +10.5 (+9.2 of readable) | −4.3 | +12.4 | both over n; rivals_built alone over readable |
| D | +0.8 | −8.7 | +25.0 (+17.4 of readable) | rivals_built |
| E | +6.0 | −8.8 | +12.4 (+15.7 of readable) | rivals_built |

Certification does not move under any reading. Whichever field W10.16 falls on is also struck on the unread reports alone in p52, and P3.2 has struck it already.

**A2. The base of a percentage in W10.16.** The primary reading divides by all reports in the subset, counting unreadable ones as not agreeing. That matches the gate, where unreadable is "never agreement". The other reading divides by readable reports only. Marking plan 14.2 supports it: a null "subtracts a document from rivals_built's denominator". Both are printed. The verdict changes only under reading C, where marks_per_part is +10.5 over n but +9.2 over readable.

**A3. test_remove's threshold.** The section 6 table puts "the other eight tests" at 39. Once swap and poke are taken out, nine tests remain. The eight could be the eight cross-step tests (section 3 says "Eight of the eleven tests are cross-step"), which would leave test_remove with no threshold. Chosen: 39, following W14 section 4's "The other fields at 39". Under the other reading the counts (46 and 48) are the same, but test_remove cannot be certified.

**A4. P3.1 per set.** The primary reading makes each of the three fields reach 44 in both sets, and then needs two of the three. The other reading needs two of three in each set, possibly a different two. No count changes: all three fields reach 44 in both sets.

**A5. P3.5's consequence.** "Otherwise they leave the within-step set" could mean that each failing field leaves, that both leave if either fails, or that both leave only if both fail. No count changes, because both fail.

**A6. What P4.4 is read on after P3.5 fails.** Section 6 as written lists seven fields. Stage B's gate says no struck field carries an arm difference, which leaves four: test_remove, shape, modules_self_reported and attributions. Both lists are in `output.json`.

**A7. A threshold "of 48" as a count or as a proportion.** The primary reading counts agreeing reports against the fixed number, as W14 writes it. The other reading scales the threshold to the readable reports. Only three fields have unreadable reports, and no certification moves:

- marks_per_part p52: 37 against 40 needed, still no;
- rivals_built: p52 36 against 38, still no; repeat 41 against 37;
- question_identity: 1 of 1 readable reaches its scaled threshold in p52, but 3 of 4 misses in the repeat set.

That p52 pass on one readable report is the reason the absolute count is the reading kept.

**A8. What counts as an "enum field" in W10.17.** The primary reading takes the 17 fields of kind `enum`, including layer_at_fault, which is not a certified candidate. The other readings add the map_enum fields, or keep only the certified candidates. All three give the same verdict: it fails on question_identity alone.

**A9. "A count of documents" (W3 section 7).** Chosen: reports, following `criteria.json`'s `marker_to_marker_rule` ("counted over reports") and thresholds "of 48". There are 48 reports per set, not 48 documents. The other reading counts source documents (16 in p52, 2 in the repeat set), with a document agreeing only when every report on it agrees. Those counts are in `output.json`. No threshold can be applied to them.

**A10. An empty map as a value.** Chosen: `{}` is a value, and two empty maps agree (the whole map is equal; "no value" is null). The other reading treats `{}` as no value. marks_per_part in p52 would go from 37 to 30, since seven reports have both maps empty; the repeat set stays at 44. shape_elements does not change. No certification moves.

**A11. What is struck.** The audit strikes nothing. M085's first run (writes 0, no result) produced no mark. The mark in hand comes from the rerun, whose audit is clean. Whether the first run counts as a marker or not, the strike count is 0.

**A12. P3.4 "applied as written".** Section 6 says the phase stops on a second rewording. W13 and W14 record P3.4 as failed before marking and not re-read, and stage B ran. It is recorded as failed and not applied again.

## 6. The explanations, each with its rival and the check

Each explanation below names what it forbids, the rival that would explain the same thing, and the check that separates them. Every check was run.

**E1. Why P3.3 fails.**
- **The explanation:** the markers cannot agree on whether the frozen question moved. It forbids reports where both markers give a value and the values differ.
- **The rival:** the field has nothing to bite on. The criterion compares the report's question with "the one handed in", and no question was handed in.
- **The check:** the section headings of all 192 prompts are FIELDS, REPORT and END. No prompt has a question section. Across the 96 reports: both markers null on 77, one null on 14, both valued on 5, and 4 of those 5 agree.
- **Result:** the rival holds. P3.3's failure sits in the stage-B inputs, the rig layer, not in the markers.
- **What it does not show:** whether markers handed a question would agree. Marking plan 4.4 already names that as untested.

**E2. W10.16's own reading of its failure: "the criterion was fitted to what its makers read".**
- **What it forbids:** gaps as large on fields never reworded twice, and gaps as large in random read sets of the same shape.
- **The rival:** set composition and small n. 21 of B's 26 read reports are in the repeat set, which agrees more on nearly every field. With 26 read reports, one report moves a percentage by about 4 points.
- **Check 1, the placebo.** Under B, 4 of the 21 fields never reworded twice also show gaps over 10 points: test_swap +11.4, test_poke +11.3, test_reverse +13.3 and shape_elements +18.0.
- **Check 2, a permutation.** It keeps each set's number of read reports and draws the read set at random, 20,000 times with seed 20260923. Under B, 30% of random read sets give a rivals_built gap of 11.3 points or more.
- **Check 3, the gap inside each set.** rivals_built's gap sits wholly in p52: read 5/5 against unread 31/43. In the repeat set it is +0.5 points. Four of those five p52 read reports (C5-m1, F4-m2, I1-m1, R2-m2) are the reports on which fault 25's clauses were written and tested (marking plan 14.2).
- **The same checks under D** (W13's read set): rivals_built is read 20/20 against unread 57/76, +25 points, and only 1.2% of random read sets reach that.
- **Result:** the tick "fails" stands as written under every reading. Under the primary reading, the explanation "fitted" is not separated from its rival. It is separated for rivals_built only under W13's read set. There it reads as the qualified Derivation 3 says: faithful where it was tested, unconstrained where it was not.

**E3. The qualified Derivation 3 across the sets.**
- **What the unqualified form predicts:** the criteria were tested on the 24 reports of rep and son, so they should be undetermined wherever untested. The untested rep31+son31 reports (the same two documents, never named by the instrument) would then agree less than rep+son.
- **What the qualified form predicts:** agreement drops only where the population admits an alternative reading.
- **The check:** compare rep+son with rep31+son31. rep+son agree more on 10 fields and rep31+son31 on 7. No difference is larger than 4 of 24. The largest on a struck field is test_poke, 21 against 17, and the rest of the struck fields are within 3.
- **Where the drop sits instead:** p52 mode 0 carries it. There shape_elements is 7/16, marks_per_part 7/16, test_addjob 9/16, and test_swap, test_patches and rivals_built 11/16 each. These are the reports where both markers mark E3, E6 and E7 N on all 16, and where 7 have empty part maps on both sides: reports not in the skill's report shape.
- **Result:** consistent with the qualified form, not the unqualified one. rivals_built is also low in p52 mode 2 (11/16), so mode 0 is not the whole story.

**E4. Why shape passes and shape_elements fails.**
- **The explanation:** shape's written rule makes markers agree.
- **The rival:** PART spans one to six Y elements, so it can absorb disagreement at the element level.
- **The check:** of the 20 shape_elements disagreements, 18 carry the same shape.
- **Result:** P3.1's hold on shape is real at the FULL-against-not-FULL grain. PART works as a catch-all, and its gauge, shape_elements, fails its own threshold in p52 (35 of 48).

**E5. Where the P3.2 disagreements sit.** Marking plan 13.5 names the first thing to look for: whether "disagreements on these four fields ... sit on the quoted text rather than on the rule". The program classifies each disagreement mechanically.
- **marks_per_part, 14 disagreements:**
  - 3 are transcription only, equal once quote characters, punctuation and case are dropped. rep31_P3-m1-r2's whole-label key is one example: `special" for (1` against `special” for (1`.
  - 7 are one map being the other plus rows. This is whether a row counts as a marked part, and 6 of the 7 are p52 mode-0 reports.
  - 4 are keys applied differently. On p52_I2-m2, the label-shape test admits the bare number `60` as an enumerator.
  - Forgiving the transcription cases would lift p52 only to 38, still under 40.
- **rivals_built, 12 disagreements:** 6 are about whether a rival was built, and 6 have member strings that differ. On my reading of those strings (worked out, not seen in the reports), five look like one rival written two ways by the naming rule: short name against five words on p52_D1-m1, D2-m2, F6-m2 and P4-m1, and one member against two on son_F4-m1-r1. Four of the five are in p52. Counted as agreement, p52 would read exactly 40. So rivals_built's failure in p52 sits at the margin, on how a member is written. That is the bill section 13.5 foresaw. It moves no tick.

**E6. Why no marker read `by-domain.md`.**
- **What was seen:** all 192 markers read SKILL.md and six references, and none read by-domain.md. The audit's own key is `read_all_seven_skill_files`.
- **The rival explanations:** each marker chose to skip it, or the instruction left it out.
- **The check:** line 27 of `workflows/llm-theory-stage-b.js` lists SKILL.md and six references and leaves out by-domain.md.
- **Result:** the instruction departed from W14 section 1 ("all eight files"). The markers did not.
- **The audit could not catch it.** The audit's list of skill files is the same seven, so a check built from the instruction it audits passes by construction.
- **Bearing on W10.18:** none. Its falsifier is reads outside the skill and the prompt, and there are none.
- **What would settle whether it mattered:** re-mark a sample with by-domain.md read and compare. Until then that is unknown.

## 7. What this does not show

- It does not show which marker is right where the two disagree.
- It does not show whether a certified field carries an arm difference; that is stage C.
- A certified field is one that two markers applied alike on these 96 reports. That says nothing about whether the field measures what it is meant to. Hard to vary is not true.
- The rival checks bear on how a tick may be read. They move no tick.

**Next step:** compare `output.json`'s `per_field` counts and named reports with the harness's collection, field by field and set by set. Where the two differ, check first which reading of section 5 each side took.
