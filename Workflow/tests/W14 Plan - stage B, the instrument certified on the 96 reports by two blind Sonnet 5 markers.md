# W14 Plan - stage B, the instrument certified on the 96 reports by two blind Sonnet 5 markers

*Frozen 22 September 2026, after the fix loop closed (log W11) and before any marker started. Read with W10 (stage B), the marking plan `rigs/W10 harness/instrument/marking-plan.md` (sections 5 and 6 fix the rule and the thresholds), and addendum W13 section 2. The instrument is `instrument/criteria.json` version W10-A4-2 with the marking plan's addenda; from the moment the first marker starts, any change to any field stops the phase (A4's rule, W13).*

## 1. What runs
- **The reports:** the 96 marked reports of the record, adapted by `record_adapter.py` (the 48 close-marked reports of HV plan 52 and the 48 repeat reports of H56 and H58), sixteen documents, run ids `<set>_<stem>` with sets p52, rep, rep31, son, son31.
- **Two markers, both Sonnet 5 at effort high, both blind.** The first marker's prompts (`first_marker.py prompts`, M001 to M096 in the record's order) carry the report number and the document id only; the second marker's prompts (`second_marker.py prep`, seed 20260922, R001 to R096) are the same 96 shuffled, the mapping closed in `marking/secret_mapping_record96.json` until the marks are saved. Neither prompt names the set, the reader, the mode, the repeat or the skill version of the report. Every marker is one Sonnet 5 subagent per report, told to read the skill (HV file 33, all eight files, with the qualified Derivation 3 stated) and then its one prompt file, and to write one JSON object once to the path the prompt names; told to read no other file. At most five subagents at a time (decision W6), by a worker pool in the saved workflow `llm-theory-stage-b.js`. Every marker's tool calls are audited from its transcript: a Read of any file other than the skill and its prompt, or of the mapping, is named in the results and that mark is struck.
- **Collection, by program:** `first_marker.py collect` (the four run-record fields filled by program), `second_marker.py collect` (the mapping opened only now), `first_marker.py validate` on both (a value outside a closed list is a fault of the marker, counted), `second_marker.py compare` (agreement by field over the 96), then `stage_b.py` (written before the run, below) for the thresholds and the split.

## 2. The thresholds, and how 48 reads on 96
The marking plan's section 6 table gives every threshold "of 48", as W3 did for the 48 close-marked reports. Stage B marks two sets of 48. Fixed here, before any mark: **a field is certified when it reaches its threshold in each set of 48 separately** (the close-marked 48; the repeat 48). The pooled count of 96 is reported beside, never as the gate. `marks_per_part` is read by document as the plan says. The consequences in section 6 (the struck-and-reworded three; swap and poke leaving the within-step set; a second rewording stopping the phase) are applied as written.

## 3. The split (W13 section 2)
The reports any maker or reviewer read while writing or rewording the criteria are the record files named anywhere in `instrument/criteria.json` and `instrument/marking-plan.md` (placeholders like `X.json` excluded), mapped to run ids by set. For every field reworded twice or more (`marks_per_part`, `pairs_that_pull`, `rivals_built`, and any the marking plan's addenda add), agreement is reported three ways: over all 96, over the read reports, over the unread reports. Nothing is certified from the read reports alone.

## 4. Predictions, as counts that could fail
- **W3 P3.1 to P3.5** as W10 section 5 restates them, read per set of 48 (section 2): shape, turned_own_test, same_explanation at least two of three at 44; marks_per_part, pairs_that_pull, rivals_built each 40; question_identity 46; at most one second rewording (already failed on the count before marking, W13; recorded, not re-read); test_swap and test_poke each 42. The other fields at 39 (the instrument's own addition).
- **W10.16:** on the twice-reworded fields, agreement over the read reports does not exceed agreement over the unread reports by more than 10 percentage points. Falsified if it does on any of the three; then the criterion was fitted to what its makers read, and that field is reported as certified on the unread reports only, or struck if it fails there.
- **W10.17:** both markers return a value in a closed list for at least 95 of 96 reports on every enum field; more nulls or off-list values than that on any field, and that field is unreadable for this stage and named.
- **W10.18:** every marker's audit shows Reads of the skill and its prompt only; one marker reading any other file strikes its mark and is counted; more than three such and the stage is re-run with a tighter prompt.

## 5. Not tested
Whether the certified fields carry an arm difference: stage C. Whether the instrument travels to a non-Claude marker: stage E. The old first marks of plan 52 and H63 are not compared here.

## 6. Traps
Reading the pooled 96 as the gate; a marker reading the mapping; any edit to criteria.json after the first marker starts; certifying from the read reports; summing fields.
