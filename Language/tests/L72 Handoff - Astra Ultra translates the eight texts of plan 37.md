# L72 Handoff - Astra Ultra translates the eight texts of plan 37

**Read this paragraph before anything else.** Your whole task is inside this bundle, and your only output is **one zip file returned to the owner**. You have no task in any repository: do not open, clone, read from, or write to any GitHub repository, whether or not you have access to it; do not reconcile, update or summarise any record; push nothing anywhere. If you find yourself writing about the project's status rather than translating a text, stop and return to the first text.

You are a fresh session with no memory of earlier work on this project. Name yourself, Astra Ultra, in every file you write. The orchestrator, Claude working in the repository with the owner, keeps the record, checks what you return (hashes, counts, every claim against the file it points to), and decides what enters the repository. You return materials and a draft; you change nothing in any record folder.

## The job
Eight short texts, in four pairs, were translated into the ledger language on 20 September by the project's first translator and run through the checker. Nobody else has translated them from scratch. You will: translate all eight under the language definition (38) and the translator's task (39) exactly as they stand; write each as a ledger pair for rig 1; run the checker and the consequences program on each; and return everything. Your ledgers will be laid beside the earlier ones by the sameness program, line by line, by the orchestrator. That comparison is the point: it is the first between two translators who never saw each other's work on these texts.

## What is in this bundle
```
READ ME FIRST.md            this file
authority/                  10 (the theory the language rests on), 38 (the language), 39 (the translator's task)
scope/L64 ...               the contract the language claims
texts/T05-B.txt .. T11-D.txt   the eight texts, each with the question its corpus attached; MANIFEST.json (hashes)
rigs/                       both checkers, frozen and patched, with the earlier ledgers of OTHER texts as examples (rig 1's raw log is left out: it holds the earlier runs of these eight texts)
tools/install_scasp.sh      puts s(CASP) where the drivers expect it; smoke_expected_report_A.txt says what a working rig prints
tools/consequences.py       what follows from a ledger, and what changes when a line is taken out
examples/                   six five-section translations of other texts, and one ledger pair, as the form to follow
```
The earlier ledgers of these same eight texts have been removed from `rigs/` on purpose. Do not go looking for them.

## Read in this order
1. This file. 2. `authority/38`, then `authority/39`, whole. 3. `scope/L64`, sections 1, 3, 5 and 6. 4. `examples/`: one translation and its `.json`/`.pl` pair. Then the texts, one at a time.

## Set up, then prove the rig runs
Run `tools/install_scasp.sh` as root if `/home/claude/sCASP/scasp` is not already there. From `rigs/rig 1 - arguments/`:
```
python3 patched/run_check.py ledger_A.pl /tmp/raw_log_smoke.txt
```
The report must find a contradiction about the door plant and a BECAUSE that follows (the tomato paragraph; `tools/smoke_expected_report_A.txt`). The drivers ask every ledger the same questions and print "predicate does not exist" errors in the raw log for kinds of line the ledger has none of; that is the rig's way of asking. Keep the raw logs.

## The work
**1. Translate.** Each of the eight, in the order T05-B, T05-D, T07-B, T07-D, T10-B, T10-D, T11-B, T11-D, under 38 and 39 as they stand, in 39's five-section form, closing with TRANSLATION COMPLETE; finish each before opening the next. Standing: the text is the actual ledger (CLAIMED and GIVEN); TOLD only for a story, note or report *inside* the text; a quoted command or question is a mentioned line in the bin. Keep the writer's verbs. Keep the question each text carries fixed; it goes in the bin as mentioned if it is not a sentence of the text. Record every reading you chose.

**2. Ledgers.** Each as `ledger_T05B.json` and `ledger_T05B.pl` (and so on, the hyphen dropped) in `rigs/rig 1 - arguments/`, with `"whose"` reading "Astra Ultra, under L72, from the other model's corpus".

**3. Run.** Every ledger through `patched/run_check.py` into its own raw log; every report kept as printed. Then `tools/consequences.py` on every ledger, output and raw log kept.

**4. The gauge.** One table: sentences; sentences that lost something to the bin; lines said, filled in, usual case; verbs with no shape; cannot-tells.

**5. The draft.** One file, "DRAFT L72 - what the run showed.md": one row per text, what the rig reported and the line it names, what consequences printed as derived, what you had to choose; then what you could not translate and why; then PARKED. No verdict on the texts.

## What to return
One zip: the eight ledger pairs; every report; every raw log; the consequences outputs; the gauge; the eight translations; the draft; a manifest with the SHA-256 of every file (as `examples/BUNDLE_MANIFEST.json` does it). Nothing edited after the fact; a correction is a new file beside the old.

## Rules
38 and 39 as they stand; every added line marked; the claimed line never restated as a premise; raw evidence untouched; say how you know each thing; no scores.

## Traps
- Looking for the earlier translations of these texts. They are not in the bundle, and the comparison is worthless if you have seen them.
- Substituting a shape-book verb for the writer's.
- Treating a bin entry as a failure.
- Writing into any record, or opening any repository.
