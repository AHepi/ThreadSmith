# V5 continuation memory

V5 carries a joint physical state from one observation segment to the next without storing the current episode's past packets. It can save that state, restore it, consume the next public packet, forecast explicit force programs, answer bounded English questions, and select an exactly supported candidate program.

Language remains a meaning interface. Exact physical alternatives **within the surviving learned subset** and the inherited correlated semantics determine its answers. Certificates are conditional on that subset, not every surviving law in the wider bank. The full 648-law bank distinguishes learned-model mismatch from full-family contradiction. V5 does not promote an approximate point prediction to a certificate.

**Qualification status:** the bounded integration is functional. Eight runtime tests, two CLI tests, the actual simulation launcher, preservation checks and [final functional verification](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/results/functional_verification_02/summary.json>) passed. The seven-scene full run and unchanged replay also passed. The added attack failed its predicted full-family detection deadline: three laws still fit the interpreted observations at 31, and V5 agrees with the independent ledger. The [scientific qualification](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/qualification.json>) remains failed. Functional checks cannot override that finding. The [gate log](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/GATE_LOG.md>) records the accepted work and preserved failures.

## Run the simulation demo

From PowerShell, use a new output directory:

```powershell
$v5Root = 'C:\Users\darre\OneDrive\Desktop\Codex\Neuron timing and Memory\v5 continuation memory'
& "$v5Root\run.ps1" demo --output-dir "$v5Root\results\my_demo_01"
```

The demo observes five accelerating steps, saves a handoff, restores it, plans a ten-step coast, and executes the certified numeric commands in the evaluator's simulator. Its final observation index is 15. It writes `handoff.json`, `continued.json`, `plan.json`, `demo.json`, and reusable prefix, suffix and question requests. An existing output directory is refused rather than overwritten.

The verified run is already available: [demo result](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/results/functional_verification_01/launcher_demo/demo.json>) and [continued session](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/results/functional_verification_01/launcher_demo/continued.json>).

The launcher prefers the bundled Python runtime. Otherwise it tries `py -3`, then `python`. The source integration requires Python 3.10+ and the existing project's NumPy/CFFI dependencies, the preserved V1/V2/V4 folders, and the sibling Pinker source tree. Nothing is downloaded or installed by the launcher. Keep this directory layout: imported modules, learned artifacts and checkpoints are bound to their expected sources.

## Inspect and ask

After the demo:

```powershell
& "$v5Root\run.ps1" snapshot --session "$v5Root\results\my_demo_01\continued.json"
& "$v5Root\run.ps1" diagnose --session "$v5Root\results\my_demo_01\continued.json"
& "$v5Root\run.ps1" ask --session "$v5Root\results\my_demo_01\continued.json" --request "$v5Root\results\my_demo_01\ask_request.json"
```

Results are JSON on standard output. The supported goal in the generated question is:

> Regarding A and B: finally, A was left of B.

`Initially` and `finally` refer to the current continuation point and the endpoint of the proposed force program. The current interface does not answer arbitrary questions about discarded past observations. Unsupported language remains unknown. The acquired V20 grammar and supplied V22 bridge are inherited; V5 learns no new grammar.

## Build a session from public packets

The default model is the preserved V2 left/mass-1 checkpoint. `open` also accepts `--model` for an explicitly selected compatible base checkpoint.

```powershell
& "$v5Root\run.ps1" open --session "$v5Root\results\my_session_01.json"
& "$v5Root\run.ps1" append --session "$v5Root\results\my_session_01.json" --request "$v5Root\results\my_demo_01\prefix_request.json"
& "$v5Root\run.ps1" append --session "$v5Root\results\my_session_01.json" --request "$v5Root\results\my_demo_01\suffix_request.json"
```

Append requests have schema `continuation_append_request_v1` and a nonempty `packets` array of canonical V15 public packets. Observation indices must be consecutive, starting at zero. The first packet has the original episode's rest-start meaning; a moving episode must be resumed from its continuation state rather than silently restarted as index zero.

A batch is processed in a detached session before one atomic session-file replacement. An invalid packet prevents that batch from being saved. Valid evidence that makes tracking unavailable, exhausts a resource limit or contradicts the family is retained as a latched state. Persistence supports one writer; it is not a concurrent session service.

Use `handoff --session INPUT --output NEW_FILE` to save a validated copy at a fresh destination. Input/output aliases are refused. Runtime source changes deliberately invalidate old continuation checkpoints.

## Forecast and plan requests

All force programs are explicit numeric `[x, y]` arrays, one vector per fixed 0.1-second step.

```json
{"schema":"continuation_forecast_request_v1","forces":[[0,0],[0,0]]}
```

```json
{"schema":"continuation_ask_request_v1","text":"Regarding A and B: finally, A was left of B.","forces":[[0,0],[0,0]]}
```

```json
{"schema":"continuation_plan_request_v1","text":"Regarding A and B: finally, A was left of B.","candidates":[{"id":"coast","forces":[[0,0],[0,0]]},{"id":"push","forces":[[8,0],[8,0]]}]}
```

Run these through `forecast`, `ask` or `plan`, each with `--session` and `--request`. Planning accepts `--policy fixed` (input order, the default) or `--policy effort`, and an optional `--max-exact-calls` budget. A candidate name is only a label. Selection requires an exact affirmative answer over the surviving learned subset with the V5 conditional certificate; unknown or unsupported candidates cannot authorize selection. Ordinary plan calls return proposals; only the demonstration/evaluator executes commands in simulation.

The V2 learned temporal ranker remains available on its original full-prefix route. V5's discarded-prefix route currently uses fixed or effort ordering. No new learned ranking advantage is claimed for V5.

## State and scope

The Python API in [continuation.py](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/continuation.py>) exposes `ContinuationSession(base_checkpoint)`, `observe`, `joint_state`, `snapshot`, `diagnose`, `forecast`, `ask`, `plan`, `checkpoint`, `from_checkpoint`, `save` and `load`.

| Boundary | Meaning |
| --- | --- |
| 32 observations, indices 0–31 | Finite public episode, at most 3.1 seconds at the inherited cadence |
| 1–16 future commands; at most 8 candidates | Bounded forecasting and candidate enumeration |
| Predictions beyond global index 31 | Mathematical projections explicitly flagged as outside executable public feedback |
| `available` | Learned laws and the full supplied family both retain joint witnesses |
| `learned_model_mismatch` | Learned support is empty, but the supplied full family still has witnesses; answers abstain |
| `full_family_contradiction` | Completed filtering excludes every supplied family law |
| `unavailable` / `resource_stop` | Computation has not established physical contradiction; no certificate is issued |

The summary retains exact conditional velocity and joint position rectangles per surviving law, current visual cover, terminal correspondence nodes and a one-way input-lineage hash. It does not store a current-episode packet or force journal. Unchanged base-model training evidence remains a separate dependency.

The checkpoint is **trusted derived state**. Source, checksum and schema validation detect specified corruption and incompatibility; they do not prove that an otherwise valid summary was honestly derived from the discarded history. Retain public evidence separately when historical audit is needed. A summary can also be larger than the raw observations because it explicitly preserves uncertainty; no general memory-saving or real-time claim is made.

The physical assumptions remain a fixed supplied affine family, rest at the original episode start, two persistent conditional references, one controlled reference, a stationary other reference, and the inherited visual cover/tracking premises. Conditional reference correspondence is not established general object identity. No recovery after a latched stop, new-law learning, general initial-state inference, contact, noisy sensing, object birth/death, neural perception, 3D or part/texture learning is implemented here.

## Evidence and tests

The [build plan](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/BUILD_PLAN.md>) and original frozen cases predate implementation. Results include first failures and their source preimages where available; old failing runs have not been relabeled as passes.

The [viability report](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/VIABILITY_REPORT.md>) explains the scope and limitations. The accepted [full run](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/results/fixed_05_ablation_scope/summary.json>) and [replay](<C:/Users/darre/OneDrive/Desktop/Codex/Neuron timing and Memory/v5 continuation memory/results/fixed_06_replay/summary.json>) have identical scientific results. That replay establishes deterministic same-source repeatability on these cases, not independent statistical replication.

Focused tests can be run separately with the bundled interpreter:

```powershell
$v5Python = 'C:\Users\darre\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
& $v5Python -B "$v5Root\test_continuation.py" -v
& $v5Python -B "$v5Root\test_cli.py" -v
```

Run the exact files in separate processes because older versions contain colliding flat module names. The full experiment is substantially more expensive than these tests: it includes independent canonical conditioning, joint-set comparisons, restored child processes and private evaluator scoring. It requires its declared source versions and fresh output names.
