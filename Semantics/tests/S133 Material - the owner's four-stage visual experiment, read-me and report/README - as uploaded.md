# Four-stage non-neural visual experiment

Start with [REPORT.md](REPORT.md), the [evidence figure](four_stage_results_v2.png), and the [Pinker rationale](RATIONALE.md). The final machine passes two frozen confirmation batches of 788 checks each. Tests include correct predictions, necessary UNKNOWN responses, and specified changes under causal interventions; this is not a 1,576-example classification-accuracy claim.

The executable acquired content is in [learned_model.json](learned_model.json). It contains two arithmetic pixel predicates, a motion expression, and two arbitrary taught words. The pose system, calibrated coordinates, memory records, continuity tracker, and route search are supplied machinery. No neural networks, model services, or network access are used by the experiment.

From the Pinker workspace in PowerShell:

```powershell
$pinkerPython = 'C:\Users\darre\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $pinkerPython -B -m unittest discover -s thinking_machine_v2 -v
Set-Location .\thinking_machine_v2
& $pinkerPython -B run_bounded.py --replay-directory runs/confirmation_20261007
& $pinkerPython -B run_bounded.py --replay-directory runs/confirmation_20261011
```

Replay verifies the seals, checks the source hashes, reconstructs every constructor proposal and score from raw observations, repeats every machine transition with identical state and operation counts, and independently audits the assessments. A replay writes a fresh controller receipt; existing evidence is never replaced. Keep the sibling `computational_mind/versions/v1_3_post_campaign_tests` directory: three pinned evidence/resource modules are imported from that immutable snapshot.

`run_bounded.py` uses Windows Job Objects: 2 GiB memory, 600 seconds CPU, 900 seconds wall time, one process, and 4 MiB captured output. The frozen confirmation contract is [confirmation_lock.json](confirmation_lock.json). A changed source, model, or uncommitted seed cannot silently count as confirmation of this version.

The runtime API is `ExperimentMachine(model)` in [runtime.py](runtime.py). It accepts raw calibrated coordinate/bit samples and explicit perception, memory, tracking, or spatial-action commands. The private world and scorer live separately in [world.py](world.py) and [experiment.py](experiment.py). This is a logical boundary in trusted Python, not a hostile-code sandbox.

Evidence is under `runs/` and `checks/`. The supplied archive was extracted to `reading_record/` for reading and provenance; its historical research scripts are not part of the experiment and were not executed.
