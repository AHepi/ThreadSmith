# L60 Handoff - a new agent runs plan 45

You are a new agent taking over one piece of the Language project: **running test plan 45**. The plan is frozen; your job is to do what it says, keep every raw output as it comes, and return the evidence. The agent that wrote the audit under test stalled; you are not it, and you are not Claude. Where the plan says "Claude translates", the translator is you: say so by name in every file you write.

## What is in this bundle
```
READ ME FIRST.md                 this file
authority/                       10 (the theory the plans name), 38 (the language), 39 (the translator's task)
plan/45 Test plan ...            the frozen plan: read it whole before anything else
records/                         the Language project's own record: read me, log, Decisions, Lessons, Status
results/45 Audit package .../    the other model's audit of 38 and 39; its corpus; its six translations (03_Worked_translations.md)
results/58 Execution attempt/    its stalled attempt: 00_Execution_report.md, and prepared/ with its six tables exported as .json/.pl
                                 and part_b_inputs.jsonl (the 48 texts Part B names) with part_b_manifest.json
results/37 ...                   the last completed run on the other model's texts: plan and results, the form to follow
rigs/                            both checkers, frozen and patched, every ledger so far, raw_log.txt
tools/install_scasp.sh           puts s(CASP) where the drivers expect it; tools/smoke_expected_report_T05B.txt says what a working rig prints
tools/sameness.py                the sameness test as a program: the mechanical part of Part A
```

## Read in this order
1. This file. 2. `plan/45 ...` whole. 3. `authority/38`, then `authority/39`. 4. `records/READ ME FIRST.md` and `records/Language - Status.md`. 5. `results/45 .../README.md` and `03_Worked_translations.md`. 6. `records/Language - Lessons.md`, entries 51 to 53: what is already known to be wrong or missing in the plan. 7. `results/37 Test plan` and `37 Test results`: the form a run and its write-up take here.

## Set up, then prove the rig runs
Run `tools/install_scasp.sh` as root. Then, from `rigs/rig 1 - arguments/`:
```
python3 patched/run_check.py ledger_T05B.pl /tmp/raw_log_smoke.txt
```
The report must read as `tools/smoke_expected_report_T05B.txt`. An empty raw log with exit code 1 means s(CASP) was not found, not that nothing was found (Lesson 53). Rig 2's driver is `rig 2 - causes/patched/check2.py`, same path for s(CASP). The joined driver, `joined/run_joined.py`, reads rig 2's laws from `/home/claude/rig2/patched/laws.pl`; make that path point at `rigs/rig 2 - causes/patched/laws.pl` if you use it.

## The work, in the plan's order
**1. The sameness test.** The plan names it; the rig had no program for it (Lesson 52). `tools/sameness.py A.json B.json` now does the mechanical part: what both ledgers say word for word (standing set aside), what only one says, where the same content carries a different standing, and near matches. It compares wording, not meaning. You read the "only" and "near" lists and decide which are one fact in two wordings; write those decisions down with the output, and quote the tool only with that said.

**2. Part A, six translations.** Translate T02-B, T02-D, L09, N03-A, N03-B and N05-A (texts in `results/45 .../corpus/`, the first three in `inputs.jsonl`, the rest in `new_60.jsonl`) under 38 and 39 exactly as they stand, in 39's five-section form, each closing with TRANSLATION COMPLETE. Do this **before** reading the other model's six again; you will have seen them once in step 5 above, and the write-up says so. Standing: write the fixture as the actual ledger (CLAIMED and GIVEN), and use TOLD only for what a story, note or report inside the text says. That is the choice the project made for the other model in file 46; the owner may change it; name the choice you used in the count section of every translation.

Then write each as a `.json` and `.pl` pair in `rigs/rig 1 - arguments/`, named `ledger_T02B`, `T02D`, `L09`, `N03A`, `N03B`, `N05A`, with `"whose"` reading "<your name>, under plan 45, from the other model's corpus". The forms to copy: `ledger_T07B.*` (a told world), `ledger_A.*` (things, general lines, BECAUSE), `ledger_G.*` (SINCE), and `patched/checker_rules.pl` for what the rules expect. The other model's side is already exported as `.json`/`.pl` in `results/58 .../prepared/part_a_original_side/`; it has not been parsed or run, and its adapter notes say what was chosen. Copy those six pairs into the rig folder under the names `ledger_T02B_other` and so on, run the driver on all twelve, and run `sameness.py` on each pair. Record, per pair: both / only theirs / only yours / standing differences / your hand decisions on the near list.

**3. Part B, the forcing cases.** For each of the fifteen findings, translate the case or cases the plan's table names (all 48 texts are in `results/58 .../prepared/part_b_inputs.jsonl`; the manifest says which belong to which finding) and run them on the patched rig, and on the frozen rig where the plan's "what I expect" mentions it. Every query goes to `raw_log.txt` as the driver writes it; keep every report as printed. Three of the plan's predictions are already known to rest on the audit's description rather than the text (Lesson 51: N17, N22, N03-B); the predictions stand as written and the runs decide.

**4. The sort.** Only after every run: put each finding in one of the three piles the plan defines, by what the rig said, and say for each whether the plan's prediction was right, wrong, or not tested. Where a run shows a pile-2 change is needed, describe what the forcing case did and **stop there**: the change itself is the next round, on the owner's word, and it records what it gives up.

**5. The write-up.** One file, "45 Test results - the 38 and 39 audit package: ledgers compared, findings sorted.md", in the form of `results/37 Test results ...`: the plan's expectation beside what happened, row by row; what was seen and what was worked out; what this run did not test; traps. Then one log entry in the project's voice for `records/Language - project story.md`, numbered **L61**, saying what was done, what was not, and what the outputs are.

## What to return
One zip: the twelve ledger pairs; `raw_log.txt` from both rigs (whole files); every report as printed; the six sameness outputs with your hand decisions; every Part B ledger pair and report; the six translations in five-section form; the results file; the L61 entry; and a short list of anything you had to choose that the plan or 39 did not settle, each with the choice made. Nothing edited after the fact: if you correct something, the correction is a new file beside the old one.

## Rules this project works by
- The plan is frozen. Discrepancies go beside it, never into it.
- A prediction is never turned into a result. A run that did not happen is "not run".
- Every line you add to a ledger is marked "filled in" or "usual case"; every guess is visible.
- Raw evidence stays as it came. Reports are compared with the GAUGE line left out (it carries timings) but the lost-sentence count is still reported.
- A clean report means the lines fit together, nothing more. Name what was not tested every time.
- No scores, no totals as evidence. Counts are inventory.
- Say how you know each thing: seen (watched the rig do it), worked out (follows from what was seen), or read.
- Ideas for procedures, scoring or changes to the language go in a PARKED list at the end of the write-up, one line each. Then back to the line in hand.

## Traps
- Reading the other model's six translations again just before writing your own. Translate first.
- Scoring Part A as agreement when the only difference is TOLD against CLAIMED. The sameness output lists standing separately for this reason.
- Substituting HIT for STRUCK or TOUCHED to get a shape-book entry. Keep the text's verb; "not checked" is the right finding.
- Inventing a producer to fit the Result form (F04's case). Use a Fact and say so.
- Taking the export in `results/58` as a run. It was never parsed; if s(CASP) rejects a line of it, that is a finding about the export, recorded, not fixed silently.
- Patching the rig in this round. The sort ends the round.
- Numbering a file by the shared record's sequence. This project's next entries are L61 onward.
