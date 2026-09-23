# W15 Results - stage B, the instrument re-marked by two blind Sonnet 5 markers; sixteen of twenty-two fields certified

*DRAFT, 23 September 2026. Not committed. It is to be questioned first, by Atria Asi and MiMo 2.6 Pro under decision W16, and then finished. It is not frozen and it is not yet logged.*

Written under plan W14, which was frozen on 22 September 2026 before any marker started, and under stage B of plan W10. It is read with W3 section 5, W13 section 2 and the marking plan's sections 5, 6 and 13 to 15 (`rigs/W10 harness/instrument/marking-plan.md`).

**What ran.** Two blind markers marked the 96 reports of the record: 192 marks from 193 Sonnet 5 subagent runs, because one marker timed out and was run again. Those marks were then counted three ways:
- by the harness's own programs, run on a scratch copy;
- by those same programs run in place, which gives the governing numbers;
- by an independent program written from the frozen texts.

A field-by-field comparison checked the counts against each other.

**Where the raw evidence is.** It is all under `rigs/W10 harness/` and kept as it came:
- the marks: `stage-B/w10/marking1/marks/` (M001 to M096) and `stage-B/w10/marking2/marks/` (R001 to R096);
- the markers' returns and the tool audit: `stage-B/returns.json`, `stage-B/returns_M085_rerun.json` and `stage-B/tool_audit.json`;
- the collection logs: `stage-B/collection/`;
- the governing counts: `marking/stage_b_record96.json` and `marking/agreement_markers_record96.json`;
- the independent recompute and the comparison: `stage-B/independent-check/`;
- the numbers this file computes itself: `stage-B/results-w15/` (`w15_consequences.py`, with `output.txt` and `output.json`).

**Whose cases.** The 96 reports are the project's own record. HV plan 49's rig ran DeepSeek V4.1 Flash and Sonnet 5 readers on them in earlier rounds. The criteria were written and reworded by agents who had read 20 of these 96 reports (W14 section 3's read set, section 5 below). No report was written under file 33, and none was handed a question.

## The short answer
- **Sixteen of the twenty-two candidate fields are certified.** A certified field reached its threshold in each set of 48, the close-marked 48 of HV plan 52 and the repeat 48:
  - test_remove, test_flip, test_reverse, test_hunt, test_addjob, test_rival, test_pull, test_patches, test_inside;
  - shape, turned_own_test, same_explanation;
  - pairs_that_pull, remove_in_groups, modules_self_reported, attributions.
- **Six are struck:** test_swap, test_poke, shape_elements, marks_per_part, rivals_built and question_identity. "Struck" means: still marked, their quotes kept, but they carry no arm difference in stage C.
- **The counts can be trusted as counts.** The in-place run of the harness's programs equals the scratch-copy run apart from timestamps, paths and log layout. The independent recompute gives the same agree/disagree/unreadable counts on every field in each set, and names the same reports.
- **The two differ only where the frozen texts can be read two ways, or where a program applies a rule no frozen text states.** There are four such places (the comparison's D1 to D4). No certification and no prediction verdict moves under any of the readings.
- **The predictions:**
  - **W3 P3.1 holds.** All three struck-and-reworded fields reach 44 in both sets.
  - **P3.2, P3.3 and P3.5 fail.** P3.4 was already recorded as failed before any mark existed.
  - **The other fields at 39 fail on shape_elements.**
  - **W10.16 fails.** Under the governing reading it fails on marks_per_part; under the independent's reading it fails on rivals_built. Both fields are struck already.
  - **W10.17 fails on question_identity.**
  - **W10.18 holds.**
- **question_identity was not tested; it did not fail between markers.**
  - None of the 192 marking prompts carries the question handed in, and the marking program has no place for one.
  - Most marks on it are empty: both markers left it null on 77 of the 96 reports.
  - That is a fault of the stage-B inputs, not of the markers. The same program will build stage D's prompts, so it has to be fixed before stage D.
- **Departures from the frozen plan** (section 2). None of them moves a number. The three that matter most:
  - The markers were told to read seven of the skill's eight files: by-domain.md was left out, against W14 section 1 and W10 section 2.
  - The markers used criteria version W10-A4-4. W14 names W10-A4-2, a stale name at the time W14 was frozen.
  - The collection's step list left out the adapter that rebuilds the ignored run records, so the first in-place attempt stopped with no count.
- **What stage B hands to stage C and D:**
  - P4.2 and P4.3 are read over eleven certified cross-step fields.
  - P4.4 is read over the within-step set that remains once test_swap and test_poke leave it: seven fields as the marking plan writes them, four of them certified.
  - test_remove now carries the within-step tests on its own.
  - Two certified fields sit exactly on their line in the close set: test_addjob and attributions, 39 of 39 each.

## 1. What ran
| Step | What | Where | Commit |
|---|---|---|---|
| Prompts | W14 frozen. 96 first-marker prompts (M001 to M096, report number and document id only) and 96 second-marker prompts (R001 to R096, the same reports shuffled with seed 20260922). The mapping is closed in `marking/secret_mapping_record96.json`. `stage_b.py` was written before any mark. The stage-B workflow was saved. | `stage-B/w10/marking1/`, `marking2/`, `code/stage_b.py`, `workflows/llm-theory-stage-b.js` | 87fd44b (22 Sept, 16:47); the job list 191ac2e |
| Markers | One subagent per prompt, 192 in all, at most five at a time (the workflow's pool, default 5). `model: 'sonnet'`, `effort: 'high'`, blind. Each read seven of the skill's eight files (section 2, item 2) and its one prompt, and wrote one JSON file. 191 returned. M085 timed out with no result, so it was run again alone and saved. | `stage-B/returns.json`, `returns_M085_rerun.json`; marks as written | c3caa66 (partial); 003a497 (191 of 192, returns, audit); f1bb829 (M085, all 192) |
| Audit | From the markers' transcripts: 192 transcripts; Read 1536, Write 191, StructuredOutput 191. Every marker made 8 reads (7 skill files and its own prompt) and no other call. M085's first run wrote nothing. Its re-run made 8 reads, none outside, and 1 write. Key hits 0; strikes []. | `stage-B/tool_audit.json` | 003a497, f1bb829 |
| Collection, first attempt | `first_marker.py collect` stopped at command 1, exit 1: "no run records at .../runs/record96. Nothing to mark." `runs/record96/` has been gitignored since d7e1c72 (log W11) and was not in this checkout. The handover's step list had no adapter step. | `stage-B/collection/00-first-collect-failed-no-run-records.txt` | f708cc4 (renamed in 0d25964) |
| Collection, scratch copy | `code/`, `instrument/`, `marking/` and `stage-B/w10/` were copied outside the repository, and `diff -r` showed them identical. Then `record_adapter.py` and the six commands ran unchanged. All exited 0. | `stage-B/independent-check/checks/harness-programs-on-a-scratch-copy/` | f708cc4 |
| Collection, in place (governing) | `record_adapter.py`, then `first_marker.py collect`, `second_marker.py collect`, `first_marker.py validate` on both, `second_marker.py compare` and `stage_b.py`. All exited 0 with empty stderr. | logs `stage-B/collection/00b` to `06`; outputs in `marking/` | 0d25964 |
| In place against the scratch copy | Every difference falls in one of four classes: timestamps 100, a path computed from the rig's location 96 (`from_the_record` in the ignored run records), absolute paths in log lines 4, log format 11. FINDINGS 0. The canaries (a changed mark, a changed count) were caught. | `stage-B/collection/07-equal-to-the-scratch-copy.py` and `.txt` | 0d25964 |
| Independent recompute | Written from the frozen texts and the raw marks. It read no harness marker or agreement code. For names only it read `record_adapter.py`, `code/README.md`, `CRITERIA-SCHEMA.md` and line 27 of the workflow. It computes every count, five readings of the read set, and rival checks. | `stage-B/independent-check/recompute.py`, `output.json`, `output.txt`, `README.md` | f708cc4 |
| Comparison | Field by field, checks c1 to c7: 450 items compared, 417 matching, 33 differing, every one from the comparison's D1 to D3; D4 changes no number. Re-run on the in-place outputs: byte-identical, 450/417/33. A canary with one count lowered gave 416/34, so the re-run was not reading the old folder. | `stage-B/independent-check/comparison.md`, `checks/`, `stage-B/collection/08-checks-c1-c7-inplace.txt` | f708cc4; in place 0d25964 |
| This file's own numbers | These are not computed by any harness program: the section 6 consequences, the margins, W10.16's consequence under each reading, and where the disagreements sit. The program first recomputes every per-set count with the harness's rule and asserts it equals `stage_b_record96.json`. | `stage-B/results-w15/w15_consequences.py`, `output.txt` | not committed (draft) |

**What the in-place equality shows, and what it does not.**
- **What it forbids:** any output difference other than a timestamp or a path. The canaries show the check could have caught one.
- **The rival:** equality by construction, because the code, instrument, marks and mapping were byte-identical in the two runs. That rival holds, and it is the point. The in-place run adds only that the numbers no longer depend on where the rig sits. It does not re-test any rule the programs apply. Those rules are tested only by the independent recompute, which shares with the harness the per-kind rule of marking plan section 5 and the pairing through `index.json` and the mapping. A fault shared there would pass both (comparison section 7).

## 2. Departures from the frozen plan
Each departure is given as what W14 says, what happened, and its effect. None of them moves a count.

1. **The adapter step was missing from the collection's step list.**
   - **What W14 says.** Section 1 names `record_adapter.py` as what adapts the 96 reports. Its collection list starts at `first_marker.py collect`, and so did the handover's step 2.
   - **What happened.** The adapter's output, `runs/record96/`, is gitignored. So the first in-place attempt stopped at command 1 and wrote no count.
   - **Effect.** No mark and no count was affected. The collection ran first on a scratch copy, then in place after the adapter, and the two agree.
   - **Why the rebuilt records are the ones the prompts were made from.** Rival: the adapter could have rebuilt different records from those the prompts were made from. Check c5 rebuilt all 192 saved prompts byte for byte from the adapter's records with the harness's own `prompt_for`: 0 differ and 0 documents mismatch (seen on the scratch records). The in-place records equal the scratch records except for `adapted_at` and `from_the_record`, which no file under `marking/` carries (07).
2. **The markers were armed with seven of the skill's eight files.**
   - **What W14 and W10 say.** W14 section 1 says each marker was "told to read the skill (HV file 33, all eight files...)". W10 section 2 and decision W6 say the same.
   - **What happened.** Line 27 of `workflows/llm-theory-stage-b.js` lists SKILL.md and six references, and leaves out `references/by-domain.md`. All 192 markers read exactly those seven. The audit shows 7 skill files per marker. The markers' own `files_read` lists, which are claimed, lack by-domain.md in all 192 (independent output.txt, "skill files not in the list").
   - **Explanation.** The instruction departed from the plan, not the markers. It forbids a marker who was told to read by-domain.md and skipped it. Rival: each marker chose to skip it. Check: the workflow's line 27 omits the file (independent README E6). The rival is ruled out.
   - **Why the audit could not catch it.** The audit's expected list of skill files is the same seven, so it passes by construction.
   - **Effect.** Unknown. by-domain.md is the module for "what counts as a part, a job or a change in this field". It bears most on marks_per_part and the per-test fields. What would settle it: re-marking a sample with all eight files read and comparing. That was not run.
   - **Bearing on W10.18.** None. Its falsifier is reads outside the skill and the prompt, and there were none.
3. **The criteria version.**
   - **What W14 says.** Its heading names "`instrument/criteria.json` version W10-A4-2 with the marking plan's addenda".
   - **What happened.** Every prompt, the index and the mapping carry W10-A4-4 (independent output.txt, freeze check). Both validate runs checked against 'W10-A4-4' (logs 03, 04). criteria.json was W10-A4-4 from commit dd7da4e (22 September, 15:33), before W14 was frozen at 87fd44b (16:47); `git show` of both commits confirms it.
   - **The two addenda between A4-2 and A4-4:**
     - Marking plan section 14 (W10-A4-3, round 2, faults 4 and 25) reworded marks_per_part and pairs_that_pull a second time (the key rule's two clauses) and rivals_built a second time (three clauses).
     - Section 15 (W10-A4-4, round 3, fault 28) changed only `affordance.json`'s shape. It reworded no criterion, and its `fields` array is byte-identical to A4-3's.
   - **Explanation: the version string in W14 is stale; W14 meant the criteria as they stood.** It forbids any sign in W14 that the markers were to mark under A4-2. Rival: W14 meant A4-2, and the markers marked under the wrong instrument. Check: W14 section 3 names the fields "reworded twice or more" as marks_per_part, pairs_that_pull and rivals_built. Those three were reworded twice only in section 14, so W14's own text presupposes A4-3 at least. The rival is ruled out.
   - **Effect.** The instrument the markers used is the one W14's words "with the marking plan's addenda" include. Nothing in `criteria.json` or `marking-plan.md` changed after dd7da4e (git log). So A4's rule "from the moment stage B begins, any change to any field stops the phase" was not triggered.
4. **None of section 6's consequences is applied by a program.** W14 section 2 says the section 6 consequences "are applied as written". W14 section 1 says a read outside the skill "is named in the results and that mark is struck". No harness program does either (comparison section 5, items 1 and 2). Both are applied by hand in section 6 below. The strike count is 0, so W10.18 needs nothing applied.
5. **The governing collection ran after the counts had been seen.** The scratch-copy counts and the independent counts were committed at f708cc4 before the in-place run at 0d25964. The programs were unchanged: `stage_b.py` has one commit, 87fd44b, and the harness code was byte-identical to the scratch copy before the run. So the numbers are the pre-written programs' numbers. The choice of which numbers govern was made after seeing them (section 3).
6. **Not a departure, recorded.** M085's first run timed out and returned no result. It was run again alone after the other 191 had returned. Decisions W12 and W13 came in between, and the pause of W13 followed. W14 neither requires nor forbids a re-run. The mark in hand is the re-run's, and its audit is clean.

## 3. The orchestrator's ruling on readings
This ruling is **the orchestrator's, made on 23 September 2026 after the counts had been seen**. It is not a frozen rule, and W14 does not contain it:

> The governing numbers are those of the programs W14 section 1 names as written before the run (the harness's collection and `stage_b.py`), run in place. Wherever those programs apply a rule no frozen text states, or the texts admit two readings, W15 names it and gives every reading's numbers beside, and says whether any certification or verdict moves. The section 6 consequences, which no program applies, are applied here by hand as the marking plan writes them, and are named as applied by hand.

Four places need it. Each is named where it bites below.

| | What the texts leave open | The governing reading (`stage_b.py`) | The other reading(s) | Does a certification or verdict move? |
|---|---|---|---|---|
| comparison D1 | Whether "marks_per_part read by document" makes documents or reports the unit of the gate. The ceil scaling is stated in no frozen text. `stage_b.py`'s docstring lists it among "Rules fixed in W14", and W14 contains no "ceil", "scaled" or "proportion" (c3). | Documents all of whose reports agree, against ceil(40/48 × documents): p52 6 of 16 (needs 14); repeat 0 of 2 (needs 2) | Reports against 40 of 48: p52 37, repeat 44 (the independent) | No. p52 misses under both, so marks_per_part is struck and P3.2 fails either way. The repeat set's per-set result does move: it misses by document and reaches by report. |
| comparison D2 | W10.16's read set, and the base of its percentages | Read set A: the record files named in `criteria.json` and `marking-plan.md`, 20 reports. Percentages over readable reports. | Read sets B (26 reports, the independent's primary), C, D, E; percentages over all reports | The verdict does not move: W10.16 fails under all ten reading-and-base pairs (the governing one is A over readable). The field it falls on does move (section 5). Both candidate fields are struck already. |
| comparison D3 | A threshold for the two fields that are not candidates | Prints 39 and `certified: false` for marks_outside_closed_list and layer_at_fault | No threshold (the texts give none) | No. Presentation only. |
| comparison D4 | The independent's reason for not counting the four run-record fields | Only the first marks carry them; the second marker's collect fills none | The independent said both sides do | No number. The exclusion stands on its other ground: none of the four is a candidate. |

Each difference was also checked against its rival, that the two programs pair or compare the marks differently. The rival was ruled out both times:
- **D1:** the independent's per-report outcomes, grouped by document, give `stage_b.py`'s 6 of 16 and 0 of 2 (c3).
- **D2:** `stage_b.py`'s split numbers equal the independent's reading A over readable reports exactly (c1's cause rows, 26 of 26).

**What the ruling gives up.**
- On D1 it lets a rule the harness wrote, and attributed to W14, govern a count against the marking plan's own gloss. Section 4.3 of that plan says "the map belongs to one report on one document", which weighs toward counting reports.
- The best-reading rival is "the texts' best reading governs". It gives the same sixteen fields and the same verdicts. At this level the two rules are one rule, and the choice between them is loose here. It would matter the first time a reading moved a certification. Section 6 applies the consequences to both lists wherever they differ.

## 4. The table
Sources:
- Counts, thresholds and the certified flags: `marking/stage_b_record96.json` (in place, 0d25964).
- The independent's column: `stage-B/independent-check/output.json`, compared item by item in `comparison.md` section 2 and re-run in place (`08`).
- Thresholds: W3 P3.1, P3.2, P3.3 and P3.5, and the marking plan's section 6 for the added 39.

Candidate means `certified_candidate: true` in `criteria.json`. Counts are reports: agree / disagree / unreadable. They are never summed across fields or sets. The pooled 96 is never the gate (W14 section 2).

| field | sort | candidate | threshold of 48 (source) | p52 (close 48) | repeat 48 | pooled 96 | certified | the independent recompute, where it differs |
|---|---|---|---|---|---|---|---|---|
| test_remove | within-step | yes | 39, section 6 (added) | 46 / 2 / 0 | 48 / 0 / 0 | 94 / 2 / 0 | **yes** | same. Certifiable only under the independent's reading A3 of "the other eight tests"; the texts forbid the other reading (comparison section 4) |
| test_swap | within-step | yes | 42, W3 P3.5 | 40 / 8 / 0 | 48 / 0 / 0 | 88 / 8 / 0 | no | same |
| test_poke | within-step | yes | 42, W3 P3.5 | 39 / 9 / 0 | 38 / 10 / 0 | 77 / 19 / 0 | no | same |
| test_flip | cross-step | yes | 39, section 6 (added) | 47 / 1 / 0 | 47 / 1 / 0 | 94 / 2 / 0 | **yes** | same |
| test_reverse | cross-step | yes | 39, section 6 (added) | 41 / 7 / 0 | 42 / 6 / 0 | 83 / 13 / 0 | **yes** | same |
| test_hunt | cross-step | yes | 39, section 6 (added) | 47 / 1 / 0 | 47 / 1 / 0 | 94 / 2 / 0 | **yes** | same |
| test_addjob | cross-step | yes | 39, section 6 (added) | **39** / 9 / 0 | 43 / 5 / 0 | 82 / 14 / 0 | **yes, at the line** | same |
| test_rival | cross-step | yes | 39, section 6 (added) | 41 / 7 / 0 | 48 / 0 / 0 | 89 / 7 / 0 | **yes** | same |
| test_pull | cross-step | yes | 39, section 6 (added) | 44 / 4 / 0 | 46 / 2 / 0 | 90 / 6 / 0 | **yes** | same |
| test_patches | cross-step | yes | 39, section 6 (added) | 41 / 7 / 0 | 48 / 0 / 0 | 89 / 7 / 0 | **yes** | same |
| test_inside | cross-step | yes | 39, section 6 (added) | 40 / 8 / 0 | 40 / 8 / 0 | 80 / 16 / 0 | **yes** | same |
| shape_elements | within-step | yes | 39, section 6 (added) | 35 / 13 / 0 | 41 / 7 / 0 | 76 / 20 / 0 | no | same |
| shape | within-step | yes | 44, W3 P3.1 | 48 / 0 / 0 | 46 / 2 / 0 | 94 / 2 / 0 | **yes** | same |
| turned_own_test | cross-step | yes | 44, W3 P3.1 | 45 / 3 / 0 | 47 / 1 / 0 | 92 / 4 / 0 | **yes** | same |
| same_explanation | cross-step | yes | 44, W3 P3.1 | 48 / 0 / 0 | 47 / 1 / 0 | 95 / 1 / 0 | **yes** | same |
| marks_per_part | within-step | yes | 40, W3 P3.2; by document, ceil(40/48 × documents) in `stage_b.py` only | by document 6 of 16 (needs 14); reports 37 / 10 / 1 | by document 0 of 2 (needs 2); reports 44 / 4 / 0 | 81 / 14 / 1 | no | the reports are the same. The gate is counted by report: 37 and 44 against 40, so p52 misses and repeat reaches (comparison D1) |
| pairs_that_pull | cross-step | yes | 40, W3 P3.2 | 47 / 1 / 0 | 46 / 2 / 0 | 93 / 3 / 0 | **yes** | same |
| rivals_built | cross-step | yes | 40, W3 P3.2 | 36 / 9 / 3 | 41 / 3 / 4 | 77 / 12 / 7 | no | same |
| remove_in_groups | cross-step | yes | 39, section 6 (added) | 47 / 1 / 0 | 45 / 3 / 0 | 92 / 4 / 0 | **yes** | same |
| question_identity | within-step | yes | 46, W3 P3.3 | 1 / 0 / 47 | 3 / 1 / 44 | 4 / 1 / 91 | no (and unreadable, W10.17) | same |
| modules_self_reported | within-step | yes | 39, section 6 (added) | 47 / 1 / 0 | 47 / 1 / 0 | 94 / 2 / 0 | **yes** | same |
| attributions | within-step | yes | 39, section 6 (added) | **39** / 9 / 0 | 41 / 7 / 0 | 80 / 16 / 0 | **yes, at the line** | same |
| marks_outside_closed_list | within-step | no (a gauge) | none; `stage_b.py` prints 39 | 40 / 5 / 3 | 46 / 2 / 0 | 86 / 7 / 3 | - | same counts; no threshold printed (comparison D3) |
| layer_at_fault | within-step | no | none; `stage_b.py` prints 39 | 35 / 11 / 2 | 31 / 17 / 0 | 66 / 28 / 2 | - | same counts; no threshold printed (comparison D3) |
| modules_served | within-step | no (filled by program) | none; `stage_b.py` prints 39 | 0 / 0 / 48 | 0 / 0 / 48 | 0 / 0 / 96 | - | not counted. It is unreadable by construction: `second_marker.py collect` fills no run-record field (comparison D4 and section 5.6) |

Other readings the independent computed, none of which moves a certification (independent README section 5):
- **The threshold as a proportion of readable reports (A7):** rivals_built reads p52 36 against 38. question_identity's single readable p52 report would "reach" it, which is why the count is the reading kept.
- **An empty map as no value (A10):** marks_per_part p52 30.
- **Source documents as the unit for every field (A9):** no threshold can be applied.

## 5. The predictions of W14 section 4, ticked
The governing numbers are `stage_b_record96.json`. Other readings come from the independent's `output.txt` and from `results-w15/output.txt`.

| Prediction | Verdict | Governing numbers | Other readings beside |
|---|---|---|---|
| **W3 P3.1**: at least two of shape, turned_own_test and same_explanation reach 44 of 48, per set | **holds** | shape 48 and 46; turned_own_test 45 and 47; same_explanation 48 and 47. All three reach 44 in both sets. | Two of three within each set, possibly a different two in each (the independent's A4): the same. |
| **W3 P3.2**: marks_per_part, pairs_that_pull and rivals_built each 40 of 48, marks_per_part read by document | **fails** | marks_per_part by document 6 of 16 (needs 14) and 0 of 2 (needs 2); pairs_that_pull 47 and 46; rivals_built 36 (3 unreadable) and 41 | marks_per_part by report: 37 and 44 against 40, still failing in p52. As a proportion of readable: rivals_built p52 36 against 38. Empty map as no value: marks_per_part p52 30. The verdict is the same in every reading. |
| **W3 P3.3**: question_identity 46 of 48 | **fails** | 1 / 0 / 47 and 3 / 1 / 44. Both markers null on 45 and 32 reports; one null on 2 and 12; both valued on 1 and 4, of which 1 and 3 equal (`results-w15/output.txt` section 6). | None changes it. For where the failure sits, see section 6.4. |
| **W3 P3.4**: at most one field a second rewording | **fails**. Recorded before any mark and not re-read (W13 section 2, W14 section 4). | marks_per_part twice, pairs_that_pull twice, rivals_built twice, or three times on section 13.5's stricter reading (marking plan section 14.4). No program computes it from marks. | - |
| **W3 P3.5**: test_swap and test_poke each 42 of 48 | **fails** | test_swap 40 and 48; test_poke 39 and 38 | Which field leaves if one fails: no count changes (the independent's A5), since both fail. |
| **The other fields at 39** (the instrument's own addition) | **fails, on shape_elements** | shape_elements 35 and 41. Every other field at 39 reaches it in both sets. test_addjob and attributions reach it exactly in p52. | test_remove is included only under the reading that gives it 39. The texts forbid the other reading, which would leave test_remove unable to be certified (comparison section 4). |
| **W10.16**: on the twice-reworded fields, agreement over the read reports does not exceed agreement over the unread reports by more than 10 points | **fails** | Read set A, over readable reports: marks_per_part read 20 of 20 (100.0%) against unread 61 of the 75 readable of 76 (81.3%), a gap of **+18.7**; pairs_that_pull −2.4; rivals_built +9.9. So it is falsified on **marks_per_part**. | Read set A, over all reports: marks_per_part +19.7. B (primary): rivals_built +11.3 over all, +12.8 over readable. C: both over all (marks_per_part +10.5, rivals_built +12.4); rivals_built alone over readable (+11.3). D (W13's set): rivals_built +25.0 and +17.4. E: rivals_built +12.4 and +15.7. It fails under all ten reading-and-base pairs, the governing one among them. pairs_that_pull is falsified under none. |
| **W10.17**: a closed-list value from both markers on at least 95 of 96 reports, on every enum field | **fails, on question_identity** | First marker 10 closed-list values (86 null); second 14 (82 null); 0 values outside the list on any enum field. Every other enum field is at 96 on both sides, except layer_at_fault at 95 on both. question_identity is named unreadable for this stage. | With map_enum fields added, or with only the certified candidates: the same (the independent's A8). |
| **W10.18**: every marker's audit shows reads of the skill and its prompt only; more than three outside reads re-run the stage | **holds** | 0 markers read another file. 0 marks struck. No re-run. | The audit is **claimed**: the transcripts behind it are not in this container (comparison section 6). No harness program applies W10.18 (fault HF3). |

**W10.16's own reading of its failure, with its rival.**
- **The explanation W10.16 writes in:** "the criterion was fitted to what its makers read".
- **What it forbids:** gaps as large on fields never reworded twice, and gaps as large in random read sets of the same shape.
- **The rival:** set composition and small numbers. 16 of read set A's 20 reports are in the repeat set, which agrees more on nearly every field, and one report moves a percentage by about 5 points.
- **The checks** (the independent's E2, all run):
  - Placebo: under read set B, four fields never reworded twice also show gaps over 10 points (test_swap +11.4, test_poke +11.3, test_reverse +13.3, shape_elements +18.0).
  - Permutation: random read sets of the same per-set sizes reach the observed gap in 6.3% of draws for marks_per_part under A, in 30% for rivals_built under B, and in 1.2% for rivals_built under D.
- **Result:** the tick stands as written. Under the governing reading, "fitted" is not separated from its rival. It is separated for rivals_built only under W13's read set (D). There it reads as the qualified Derivation 3 says: faithful where it was tested, and unconstrained where it was not.

## 6. The section 6 consequences, applied by hand
No harness program applies these. Every list below is computed by `results-w15/w15_consequences.py` from `stage_b_record96.json`, `criteria.json` and `affordance.json` (`output.txt` section 4). The rules are the marking plan's section 6, with section 5 for what the predictions are read over.

**6.1 P3.1 holds: what it licenses for the cross-step fields.**
- The consequence of failure ("the cross-step fields cannot carry an arm difference") does not arise. The cross-step fields that certified may carry an arm difference in stage C.
- Of the 13 cross-step candidates, 12 are certified: test_flip, test_reverse, test_hunt, test_addjob, test_rival, test_pull, test_patches, test_inside, turned_own_test, same_explanation, pairs_that_pull, remove_in_groups. rivals_built is struck.
- **P4.2 and P4.3 are read over 11 fields:** those twelve less test_patches, which `affordance.json` records as afforded by no arms document (marking plan sections 13.4 and 15.2). The eleven are test_flip, test_reverse, test_hunt, test_addjob, test_rival, test_pull, test_inside, turned_own_test, same_explanation, pairs_that_pull and remove_in_groups. This is marking plan section 15.2's twelve less the struck rivals_built.
- turned_own_test is among the eleven although the corpus records it neither way. That is the rule of section 15: "found nowhere means unknown".
- The thin cases section 13.4 names stand: test_reverse and test_inside each rest on one arms document, so a loss on either is read against n = 1.

**6.2 P3.2 fails.**
- marks_per_part and rivals_built are "kept as quotes only, as H64 kept the verdict" (W3 P3.2). They are marked in stage D and carry no arm difference.
- pairs_that_pull is certified. It is now the only field that records which parts the report names as pulling.

**6.3 P3.5 fails: test_swap and test_poke leave the within-step set.**
- **The within-step tests.** W3 P3.5 and `criteria.json`'s P3.5 say "remove carries it alone". Of the three within-step tests only test_remove is left, certified at 46 and 48.
- **The within-step set as section 6 writes it**, which P4.4 is read on: test_remove, shape, shape_elements, marks_per_part, question_identity, modules_self_reported and attributions, seven fields.
- **Of those seven, stage B certified four:** test_remove, shape, modules_self_reported and attributions. shape_elements, marks_per_part and question_identity are struck.
- **The two readings.** Section 5 says "P4.1 to P4.5 and PA.3 are read over certified fields only". So P4.4 is read on the four, and the seven is the list as written. Both are given here, as the independent gave them (its A6).
- **What that leaves P4.4 able to show (worked out).**
  - Marking plan section 10 says P4.4 "is about the within-step *marks*, not about the vocabulary".
  - After stage B no certified field records a part's mark: marks_per_part is struck.
  - So P4.4, as this rule leaves it, reaches the marks only through test_remove. The other three certified fields are the report's shape, the modules the reader says it opened, and the attributions.
  - Whether P4.4 so read still tests W8 part B10 is for the stage C plan to say before stage C runs. It is put to the owner below.
- **Where the P3.5 failure sits** (`results-w15/output.txt` section 7). Two explanations of the failure: the criterion reads two ways on any report, or it reads two ways on some kinds of report. The first forbids disagreements that gather in one kind. The check is where they sit:
  - test_swap's 8 disagreements are all in p52, and 5 of them are p52's mode-0 reports. In the plan 49 rig's `run.py`, mode 0 is the reader with no skill at all, sent the BARE system message. The repeat set agrees 48 of 48.
  - test_poke's 19 are spread across every subset: p52 modes 0, 1 and 2 have 5, 2 and 2; rep 2, rep31 2, son 1, son31 5.
  - So swap's failure is held by the close set's report kinds, and poke's is not.
  - This moves no tick: W14 fixed the gate per set of 48. It bears on section 8.

**6.4 P3.3 fails, and its cause.**
- **The explanation.** The failure sits in the stage-B inputs, the rig layer: the markers were never handed the question the criterion compares against, so most of them left the field null. It forbids a failure made of reports on which both markers gave a value and disagreed.
- **The rival.** The markers had what they needed and cannot agree on whether the frozen question moved.
- **A second rival.** The reports freeze no question for the markers to compare. It forbids nulls on reports that do freeze one. The repeat set's reports are all in the skill's modes, and marking plan section 4.4 quotes two of them freezing a question. Yet both markers left the field null on 32 of those 48. So this rival does not carry the nulls.
- **The check.** All 192 prompts have only the sections "THE FIELDS", "THE REPORT" and "END OF THE REPORT". None carries a question handed in (independent output.txt). `first_marker.prompt_for(num, doc, report, crit, out_path)` has no place for one: read from the source in this step, and c5 says the same. Both markers gave a value on only 5 of 96 reports, and they agree on 4 of those.
- **Result.** The failure is 91 unreadable reports and 1 disagreement, so the rival is ruled out as the cause of this failure. The criterion compares "the question the report freezes" with "the one handed in", and no stage-B marker was handed one. Whether markers who were handed a question would agree is a different question, and nothing here tested it.
- **Marking plan section 4.4 said this would be tested.** It says stage B would test the field "on the reports in hand, against the questions the record's framing names". No step made that true.
- **So what stage B shows about question_identity is that it was not tested.** W3 P3.3's clause "a field that cannot record drift falsifies the instrument" is not triggered on this evidence, because the field was never given its input. A failed test knocks down the bundle (the criterion, the markers, the inputs), and the check points at the inputs. It does not show the markers would agree if handed a question.
- **What it means for stage C and D:**
  - question_identity is not certified, so it carries no arm difference in stage C (W10 stage B: "No field carries an arm difference in stage C unless it agreed here").
  - W10 section 4 still requires it to be recorded on every run. W3 phase 4's "runs that moved counted separately" would therefore rest on an uncertified field, and that count is unreadable until the field is tested.
  - The same `prompt_for` builds stage D's marking prompts. Unless it is changed (HF7), stage D's markers will not be handed the question either, and the field will be unmarkable there too.
- **Two routes, for the owner:**
  - Re-mark question_identity alone in stage B, with each report's handed-in question (the stand-in the marking plan writes for the record's framing) put in the prompt. That needs HF7 fixed, an addendum written before it runs, the Sonnet-5 marker role settled (decision W15's open question), and a note that handing in the question changes the inputs and not the criterion.
  - Or run stage C with question_identity as an uncertified read-out, and report the moved-runs count as unreadable.

**6.5 W10.16's consequence.** "That field is reported as certified on the unread reports only, or struck if it fails there."
- No frozen text says what threshold applies to fewer than 48 reports. Two gates were computed: the threshold scaled to the unread reports, ceil(threshold/48 × n), and the absolute threshold.
- **Governing reading (read set A, over readable reports): the field is marks_per_part.** On the unread reports only:
  - p52: 33 agree, 10 disagree, 1 unreadable of 44. The scaled threshold is 37; the absolute is 40.
  - repeat: 28 of 32, which reaches the scaled 27 but not the absolute 40.
  - By document: 6 of 16 (needs 14) and 0 of 2 (needs 2).
  - So it is **struck**. It was struck already by P3.2, and nothing changes.
- **Independent's primary reading (read set B): the field is rivals_built.** On the unread reports only, p52 is 31 of 43 against a scaled 36, so it is **struck**. It was struck already by P3.2.
- **Under every other pair** (C, D, E × two bases), the field or fields W10.16 falls on are struck on the unread reports in p52 (`results-w15/output.txt` section 5).
- **pairs_that_pull** is never falsified, so its certification does not rest on the reading.
- **What is loose (comparison D2).** Which field the consequence lands on is held by the reading, not by the marks. It moves nothing here only because both candidate fields are struck already.

**6.6 P3.4.**
- Section 6 says: "If a second field needs a second rewording, the phase stops and reports the patches with what each gave up."
- The count failed before stage B (marking plan section 14.4). The owner's decision W11 was taken as: "stage B starts after that, with the rewording count recorded as it stands" (Decisions, W11).
- So this consequence is recorded and **not applied**, by the owner's decision rather than by this file. The patches, each with what it gave up, are sections 13 and 14 of the marking plan.

**6.7 The margins** (`results-w15/output.txt` section 3).
- **Two certified fields sit exactly on their threshold in p52:** test_addjob (39 of 39) and attributions (39 of 39). One report marked the other way on either would strike it.
  - test_addjob's nine disagreeing p52 reports: C5-m0, C5-m1, D1-m0, E3b-m0, F4-m1, I1-m0, I2-m0, P4-m0 and S14b-m0.
  - attributions's nine: D1-m1, E2b-m2, E3b-m0, E3b-m1, E3b-m2, F6-m2, R1-m1, R1-m2 and S14b-m1.
- **Two more are one report above:** test_inside (40 in both sets) and turned_own_test (45 against 44 in p52).
- **One struck field is two below:** test_swap (40 against 42 in p52).
- **The line itself is a free choice.** It is the instrument's own added threshold: "80 percent of 48, rounded up" (marking plan section 6), fixed before any mark. Swapped for its neighbours (`output.txt` section 3b):
  - at 38 of 48 the same twelve fields are certified;
  - at 40, attributions and test_addjob are lost;
  - at 41, test_inside is lost too;
  - at 42, test_reverse, test_rival and test_patches are lost too.
- **So two certifications are held by where a free line was drawn:** they are "held if" 39 is the right line.
- **What depends on them:**
  - attributions is the field arm (x) was built to be read on (marking plan section 4.8; PA.3).
  - test_addjob is one of the eleven P4.2 and P4.3 fields, and the corpus records four arms documents that afford it.
- **What would settle them:** a third reading of the nine disagreeing p52 reports on each field. That was not run. By the rule as written they are certified, and this file does not re-read the rule.

## 7. Harness faults found, recorded and not fixed
None was fixed in this step (the session's rule). Each is listed with what it would change and when it must be fixed. "Stage D" means before stage D's marking prompts are built or its counts are read.

| | Fault | Where, and who found it | What it would change | Fix before |
|---|---|---|---|---|
| HF1 | `stage_b.py` gates marks_per_part by document against ceil(40/48 × documents), a scaling no frozen text states, and its docstring lists it among "Rules fixed in W14". The same program counts the same field by report in its W10.16 split. The split's percentages are over readable reports, while the gate counts unreadable as not agreeing. | `code/stage_b.py`; comparison D1 and D2, checked by c3 | In the repeat set (2 documents of 24 reports) the gate passes only at 48 of 48 reports. In p52 it can pass at 42 or fail at 45. A field could pass by report and fail by document. | Any re-run of `stage_b.py`, for example a re-mark of question_identity. The reading is ratified in an addendum first. It does not block stage C. |
| HF2 | No program applies section 6's consequences. The certified list is built field by field. Nothing writes the within-step set after P3.5, P4.4's read set, or the P3.1-failure branch. | `stage_b.py`; comparison section 5.2 | Here, applied by hand (section 6). If `agreement.py` is run in stage D without `--certified`, it reads over the candidates by `sort`, and test_swap and test_poke would carry P4.4. | Stage D's counts |
| HF3 | No program applies W10.18: none reads `tool_audit.json` or strikes a mark. | c6 | 0 strikes here, so nothing. A mark whose marker read outside the skill and its prompt (the mapping, say) would still be counted. | Stage D's marking (its plan restates the audit rule) |
| HF4 | `agreement.py --certified` reads `c.get("certified") or c.get("fields")`. With an empty certified list it falls through to `stage_b.py`'s `fields` map, so every candidate is treated as certified. | `code/agreement.py`; the harness worker, confirmed on the real file by c6 | Nothing here: the list has 16 names. If stage B had certified none, stage C's predictions would be read over all 22 candidates. | Stage D's counts |
| HF5 | `stage_b.py` looks each report's document up in the gitignored `runs/record96/`. If the folder is absent it takes None for every report without an error: one "document" per set, threshold 1, passing only if all 48 agree. | `stage_b.py` `rig_document`; the harness worker, comparison section 5.5 | Here the records were present and every document matched (c5). In a fresh checkout without the adapter, marks_per_part's gate would change silently. (`first_marker.py collect` does stop with an error; `stage_b.py` does not.) | Any re-run of `stage_b.py` |
| HF6 | `record_adapter.py` ends: "Now: first_marker.py prompts --reader record96, second_marker.py prep --reader record96, agreement.py markers --reader record96". Followed now, `prompts` would rewrite `stage-B/w10/marking1/index.json`. `prep` without `--seed` would draw a random seed and overwrite the tracked closed mapping `secret_mapping_record96.json` (and, with `--scratch "../stage-B"`, marking2's prompts), pairing the 96 R-numbered marks with different runs. | `code/record_adapter.py`, `code/second_marker.py` (`random.randrange`; an unconditional mapping write); the in-place worker, read from the source and not run | The pairing of every second mark, silently | Now. The adapter must be run again in any fresh checkout before stage B's files can be re-read. |
| HF7 | `first_marker.prompt_for(num, doc, report, crit, out_path)` has no place for the question handed in, yet question_identity's criterion compares against "the one handed in". Stage C's run records carry `question` and `question_as_sent` (`sonnet_prompts.py`, `run_deepseek.py`), but the marking prompt does not. | `code/first_marker.py`; the independent's E1, c5, and read from the source in this step | question_identity unmarkable in stage D exactly as in stage B | Stage D; and any re-mark of question_identity in stage B |
| HF8 | `second_marker.py collect` fills none of the four run-record fields. So `first_marker.py validate` on the second marks prints 384 "no value" lines (4 fields × 96, log 04) that are not the marker's faults, and modules_served compares 0 / 0 / 96 by construction. | comparison D4, c4 | A count of "marker faults" read off the validate log would be wrong by 384. modules_served is not a candidate, and P4.6 reads it from the run records. | Stage D |
| HF9 | `stage_b.py` prints a threshold of 39 and `certified: false` for the three fields that are not candidates. "40/39" for marks_outside_closed_list reads like a pass. | comparison D3 | Presentation only | Stage D's results |
| HF10 | The stage-B workflow's instruction lists seven of the eight skill files (line 27, by-domain.md missing), and the audit's expected list is built from the same seven, so the audit cannot see the omission. | `workflows/llm-theory-stage-b.js`; the audit; the independent's E6 | Markers armed with seven files, against W14 and W10. Unknown effect on the marks (section 2, item 2). | Any re-run of the stage-B workflow, and stage D's marking workflow. The audit's list is taken from the skill folder, not from the instruction. |

## 8. What stage B certifies for stage C and D, and what it does not
**It certifies:**
- On these 96 reports, under criteria W10-A4-4, two blind markers applied sixteen fields alike often enough to reach their thresholds in each set of 48. The markers were Sonnet 5 at effort high, each armed with seven of the skill's eight files and the qualified Derivation 3.
- Those sixteen, and no others, may carry an arm difference when stage C's reports are marked in stage D: P4.1 and PA.3 over all sixteen; P4.2 and P4.3 over the eleven of section 6.1; P4.4 over the four (or the seven as written) of section 6.3; and P4.5 over the certified fields of the sort each of its clauses names.

**It does not certify:**
- **That any field measures what it is meant to.** Agreement between two markers is not validity. Both markers are one model family, carry one skill, and read one instrument written by one author (marking plan section 7, conflicts 1, 5 and 6). A misreading the two share passes this test.
- **Anything across model families.** Stage C's reader is Sonnet 5 as well (W10 section 4), so in stage D a model will be marking its own family's reports. Stage E's examiners of other families are the only check on that, and the DeepSeek examiners wait on the key (decision W17).
- **The instrument beyond the kinds of report it was tested on.** Under the qualified Derivation 3 ("faithful where it was tested and, wherever its population admits an alternative, unconstrained where it was not"), the certification holds for these 96 reports' kinds:
  - p52: DeepSeek V4.1 Flash on 16 outside documents in the plan 49 rig's three modes (0, no skill; 1, the whole skill in the system message; 2, SKILL.md with a tool to open the modules).
  - The repeat set: DeepSeek and Sonnet 5 readers on two documents (P3, F4) in modes 1 and 2, under skill files 30 and 31.
  - None was written under file 33, none under any W10 arm, and none was handed a question.
- **That the kind of report doesn't matter.** The evidence says it does. Several struck fields fail mostly on p52's mode-0 reports, where the reader had no skill:
  - test_swap: 5 of its 8 disagreements;
  - shape_elements: 9 of 13 in p52;
  - marks_per_part: 9 of 11 in p52;
  - test_addjob: 7 of its 9 in p52.
  (`results-w15/output.txt` section 7; the independent's E3.) Stage C's reports are all file-33 reports under arms. So what these fields would do on them is unconstrained by stage B in both directions. The same holds for kinds no stage-B report had: arm (d)'s assembled reports, arm (e)'s skeleton, arm (x)'s exchanged names.
- **A marker other than Sonnet 5 at high.** If the open question of decision W15 moves stage D's markers to Opus 5.5, this certification does not carry over by itself.
- **question_identity**, which was not tested (section 6.4).

## 9. Not tested
- Which marker is right wherever the two disagree. No third reading ran: not on the margins (section 6.7), not on shape_elements, not on marks_per_part.
- The model each marker was served. The workflow asks for `sonnet`, and neither the returns nor the audit records a model id. "Sonnet 5" is claimed.
- The transcripts behind `tool_audit.json`. They are not in this container, so the audit is claimed, and W10.18's verdict rests on it.
- Whether reading `by-domain.md` would have changed any mark.
- question_identity, which was given no input.
- Blindness at the level of the report's own text: whether a report's wording reveals its reader, mode, repeat or skill version. W14 asked only that the prompt not name them, and the prompt's head names the report number and document id only (seen in M001).
- The old first marks of plan 52 and H63 against these (W14 section 5).
- Whether any certified field carries an arm difference (stage C), or whether the instrument travels to a marker of another family (stage E).
- The fields no program compares: modules_served, requests, request_text_saved, ports_set and every text field.
- A third route to the counts that shares neither the per-kind rule nor the pairing. This file's program uses the harness's own `marks.same`, so it is not that route either.
- `agreement.py runs` and `agreement.py records`, which produce stage D's counts. Not run.
- HF6 and HF7 were read from the source, not run.
- The independent's E5 reading, that five of rivals_built's twelve disagreements are one rival written two ways. It was worked out, not seen, and it moves no tick.
- Whether a marker agrees with itself. No marker marked a report twice.

## 10. Traps
- Reading the pooled 96 as the gate. W14 section 2 makes each set of 48 the gate.
- Reading "sixteen certified" as a score, or as "the instrument works". It says two markers of one family applied those fields alike on these reports.
- Reading P3.3's failure as markers who cannot agree, or as the field being unable to record drift. It was untested.
- Treating test_addjob and attributions as safely certified. They sit on a free line, with no report to spare.
- Treating W10.16's falsified field as a fact about the marks. It moves with the read set.
- Reading the in-place equality as a re-test of the rules. It shows only that the numbers no longer depend on where the rig sits.
- Following the adapter's closing hint (HF6).
- Quoting the ceil scaling as W14's.
- Moving a field between within-step and cross-step now. W8 part B4 forbids re-sorting on the reports.
- Editing `criteria.json` to fix question_identity. Any change to any field stops the phase. Handing in the question is a change to the inputs and needs its own addendum.

## What the owner is asked
- **question_identity.** Choose one of the two routes of section 6.4: re-mark it in stage B with the question handed in, after HF7 is fixed, under an addendum; or carry it into stage C as an uncertified read-out.
- **P4.4.** P4.4 is now read on test_remove, shape, modules_self_reported and attributions, none of which records a part's mark. Should the stage C plan say what that leaves it testing before stage C runs?
- **by-domain.md.** Re-mark a sample with all eight files, or accept the seven and record it.
- **The readings of section 3.** They are the orchestrator's and were made after the counts. The owner may take another reading. None moves a certification or a verdict here.
- **The open question of decision W15:** whether stage C's reader and stage D's markers stay Sonnet 5. Stage B certified the instrument on Sonnet 5 markers only.

## Lessons (candidates for the Lessons file, to be numbered when fixed)
- **A step list omitted the step that rebuilds an ignored input.** The adapter was missing, so the first collection stopped. The rule: a step list names every input that is not in git and the command that makes it.
- **The markers' instruction listed seven of the eight skill files, and the audit built its expected list from the same instruction**, so it could not see the gap. The rule: an audit's expected list comes from the source (the skill folder), never from the instruction it audits.
- **A criterion compared against "the question handed in", and no stage-B prompt carried one.** The marking plan said stage B would test it, and nothing checked that the prompts carried the input. The rule: before markers run, check that the prompt carries every input each field's criterion names.
