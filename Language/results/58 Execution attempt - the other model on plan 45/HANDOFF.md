# Resume plan 45 without changing the experiment

The execution attempt stopped during a native runtime smoke test. Read `00_Execution_report.md` and `evidence/native_smoke_result.json` first. The plan did not reach a completed Part A comparison. The observed Part B piles are all null. No patch is waiting to be accepted as if it had passed.

The repository snapshot is `ce30053e4369675e989ae4f21103132e5398cbe6`. The original language and translator prompt are in `sources/original_audit/Ledger_38_39_Audit/sources/`; their bytes are checked against both the mounted attachments and the repository Git blobs in `evidence/authority_identity.json`.

The native smoke can be repeated with Python and an actual s(CASP) executable:

```sh
python tools/resume_smoke.py --scasp /absolute/path/to/scasp
```

Each invocation creates a new replay directory. It does not overwrite this attempt's evidence. It relocates only the executable path in memory, not any rule, and never calls a successful process exit a semantic pass.

The six `.json`/`.pl` exports in `prepared/part_a_original_side` preserve the older assistant-authored tables. They are not Claude's new comparison translations. Read the export notes before running them: the bin-entry gauge does not equal the old lost-sentence count, and Prolog parsing is unverified. The original five-section texts remain in the same directory.

Find the actual sameness-test command before comparison. Do not substitute a string-difference program while reporting that the rig's existing test ran. Produce or retrieve the six genuinely new comparison-side ledgers under unchanged 38 and 39, with their actual author identified. Do not derive the new side from the frozen predictions. The experiment is already disclosed as non-blind, but that does not permit fabricated independence.

After Part A, use `prepared/part_b_manifest.json` to locate the forcing cases and controls in `prepared/part_b_inputs.jsonl`. Unsuffixed families were expanded for preparation only. Preserve the literal input and question; do not change N17 to LETS or remove N22's supplied dependency/change to force the predicted outcome. Keep the original frozen plan unchanged and record discrepancies alongside it.

Run the baseline and frozen rigs, preserve raw output, then sort. Only a forcing-case result may support the first pile-2 patch. Rerun every earlier ledger and compare reports as specified. The original plan's instruction to omit GAUGE for historical comparisons must not erase the separately required disclosure of lost content.
