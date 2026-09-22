# L66 Handoff - a new agent translates and runs the blind corpus

You are a new agent given one piece of the Language project: **translate eighteen short passages into the ledger language, run the checkers on them, and return the evidence.** You are not Claude and not any agent that worked on this project before. Name yourself in every file you write.

**Who keeps the record.** The orchestrator, Claude working in the repository with the owner, made this corpus, keeps the project's record, checks what you return (hashes, counts, every claim against the file it points to), and decides what enters the repository. You return materials and a draft; you change nothing in any record folder.

## What is in this bundle
```
READ ME FIRST.md            this file
authority/                  10 (the theory the language rests on), 38 (the language), 39 (the translator's task)
scope/L64 ...               the contract the language claims: what is in scope, what is out, and the gauges
corpus/P01.txt .. P18.txt   the passages, sentences numbered; MANIFEST.json (hashes); SOURCES.md (where the words come from); KEY.enc (sealed; not for you)
rigs/                       both checkers, frozen and patched, every earlier ledger, raw_log.txt
tools/install_scasp.sh      puts s(CASP) where the drivers expect it; smoke_expected_report_T05B.txt says what a working rig prints
tools/consequences.py       what follows from a ledger, and what changes when a line is taken out
tools/sameness.py           what two ledgers both say, what only one says, standing set aside
examples/                   plan and results 37, and the six five-section translations from L62, as the form to follow
```

## Read in this order
1. This file. 2. `authority/38`, then `authority/39`, whole. 3. `scope/L64`, sections 1, 3, 5 and 6. 4. `examples/`: one five-section translation and its `.json`/`.pl` pair. 5. `corpus/SOURCES.md`. Then the passages, one at a time, as you translate them.

## Set up, then prove the rig runs
Run `tools/install_scasp.sh` as root. From `rigs/rig 1 - arguments/`:
```
python3 patched/run_check.py ledger_T05B.pl /tmp/raw_log_smoke.txt
```
The report must read as `tools/smoke_expected_report_T05B.txt`. An empty raw log with exit 1 means s(CASP) was not found. Rig 2's driver is `rig 2 - causes/patched/check2.py`. Both drivers ask every ledger the same questions and print "predicate does not exist" errors in the raw log for kinds of line the ledger has none of; that is the rig's way of asking, and the report says NO FAULT FOUND when nothing of that kind was there to check. Keep the raw logs; do not read a printed NO FAULT FOUND without them.

## The work
**1. Translate, blind.** Each of P01 to P18, under 38 and 39 exactly as they stand, in 39's five-section form, closing with TRANSLATION COMPLETE. The passages are prose and verse set as prose; take each sentence as the writer's, however it reads. Standing: the passage is the actual ledger (CLAIMED and GIVEN); TOLD only for a story, note or report *inside* a passage; a quoted saying is a mentioned line in the bin. Keep the writer's verbs; a verb with no shape is "not checked", which is the right finding. Where a sentence reads as a slip or a corruption of the text, translate what it says and record your reading under "Readings I chose", as 39 rule 16 asks; do not repair it. Where a sentence will not go into the language, it goes to the bin with its reason; the bin is not a failure, it is the contract working. Translate the passages in the order P01 to P18 and finish each before opening the next.

**2. Ledgers.** Each translation as `ledger_P01.json` and `ledger_P01.pl` in `rigs/rig 1 - arguments/`, with `"whose"` reading "<your name>, under L66, from the sealed corpus", the passage's sentences in the json, and every line's standing in the text as the examples show. Where a passage is about bodies pressing, moving, falling or resisting (some of the Lucretius passages), write a rig-2 ledger as well, in `rigs/rig 2 - causes/`, following `ledger_A.*` and `ledger_C1.*` there. Say in the json which rig each ledger is for.

**3. Run.** Every rig-1 ledger through `patched/run_check.py`, and every rig-2 ledger through `patched/check2.py`, each into its own raw log; keep every report as printed. Then `tools/consequences.py` on every rig-1 ledger, output and raw log kept. Then, wherever two passages share most of their sentences, `tools/sameness.py` on their two ledgers, output kept, with your hand decisions on the "only" and "near" lists written beside it.

**4. The gauge.** For each passage: sentences in the passage; sentences that lost something to the bin; lines said, filled in, usual case; verbs with no shape; cannot-tells. One table.

**5. The draft.** One file, "DRAFT L66 - what the run showed.md": for each passage, one row: what the rig reported (the finding and the line it names), what consequences printed as derived, and anything you had to choose. Then what you could not translate and why. Then a PARKED list. Nothing in it is a verdict on the text's truth or the writer's quality; the passages are famous and contested and none of that is your job.

## What to return
One zip: eighteen (or more) ledger pairs; every report as printed; every raw log; the consequences outputs; the sameness outputs with your hand decisions; the gauge table; the eighteen five-section translations; the draft; a manifest with the SHA-256 of every file, as `BUNDLE_MANIFEST.json` in the examples does it. Nothing edited after the fact; a correction is a new file beside the old.

## Rules
- 38 and 39 as they stand. Any thought about changing them goes in PARKED.
- Every line you add is marked "filled in" or "usual case".
- The claimed line is never restated as a premise (39 rule 9).
- Raw evidence stays as it came. The passages are not edited; their hashes are in MANIFEST.json and will be checked.
- Say how you know each thing: seen, worked out, or read.
- No scores, no totals as evidence. Counts are inventory.

## Traps
- Repairing a sentence that reads wrongly. Translate it; record your reading.
- Treating a bin entry as a failure and forcing the sentence into a line.
- Substituting a shape-book verb (push, hit) for the writer's verb to get a check.
- Reading the passages against each other. Each is its own ledger; the sameness test is the only comparison, and only where the sentences are plainly shared.
- Writing into any record folder. Your draft is the orchestrator's input.
- Reading KEY.enc, or trying to. It is sealed for a reason and it is not yours.
