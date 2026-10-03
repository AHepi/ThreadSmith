# Measuring learning with stock Avida

## Summary for the owner

Suppose a population performs XOR at update 10,000 and again at 20,000. That tells us XOR is present at both times. It does not tell us whether programs kept it throughout, lost it and found it again, or whether different branches supplied it.

This report measures that distinction as far as the saved record permits. It supplies fixed-input capability tests, a retention table, recorded ancestry paths, instruction-disabling tests, and snapshot measures of change. The code uses the existing engine and ordinary file processing.

[checked] The source contains 214 task names, but they are not 214 interchangeable tests of isolated programs. Some are aliases, some need other programs or environmental state, and some give partial credit. Historical population saving also omits extinct branches with no surviving descendants; reloading changes numeric identities.

The practical result is a runnable, explicitly bounded measurement protocol. Its task audit records unsupported contexts rather than counting them as failed capabilities. It distinguishes an observed capability, a capability never directly rewarded, and evidence of retained instruction dependence.

The supplied experimental findings remain owner-provided observations; their original data were not supplied here. This work does not turn the finite task catalogue into a test of unlimited learning. The next action is to run the supplied battery on the earliest and latest saved populations from one continuous run, inspect its raw outputs, then process the remaining snapshots.

## The measurements

### Capabilities never rewarded

[checked, source S1–S4] `cTaskLib::AddTask` registers 214 names, including 68 three-input logic names and 56 arithmetic names. Name counts are not counts of distinct computations. Ten `_dup` names alias existing tasks; the generated dictionary also collapses six additional checked alias names; `dontcare` supplies a positive-output control. Some other named arithmetic operations coincide. The appendix generator audits every registered name and assigns each to a runnable profile or an explicit unmet-context status. The 157-name core uses parameter-free, isolated-program tests, including fixed-output Fibonacci checks. Sixteen additional parameterized names run separately; 40 contextual names and the output-domain-sensitive `all-ones` test are excluded from the default suite. Their audit entries explain the absent context or domain. Thus testing all 214 as ordinary isolated-program capabilities is not supported by this brief’s constraints. Parameterized profiles remain separate: a task name without its parameters is not a complete problem definition.

Design: test every saved row with `num_units > 0`, including rare sequences, with the same input deck at every date. Keep the original instruction-set configuration. Load the snapshot, filter living rows, run one `RECALCULATE 0 -1 0 A B C` per triple, and export `DETAIL` before changing inputs. The generator writes the complete commands, task-index dictionary, inputs and snapshot manifest. Do not use repeated random trials as a replacement for these separately retained results.

[checked, S1–S4] Reactions use `process:value=0:type=pow`, meaning a multiplier of one. This observes task recognition without task merit increases. It does not reproduce the original resource ecology or the running CPU state. The logic evaluator needs all eight joint bit patterns across the three input words. The low-input deck preserves these patterns while keeping arithmetic inputs small and positive; the separate Boolean-only high-input deck probes magnitude dependence without exposing arithmetic evaluators to large intermediate values.

[checked, S1–S3] The exported columns, in order, are `id num_units viable length gest_time fitness update_born parent_id depth sequence hw_type inst_set env_input.0 env_input.1 env_input.2`, followed by alternating indexed task counts and quality sums. Avida strips the numeric arguments from `#format`, producing repeated `task` and `env_input` names. The generator therefore writes `schema.tsv` with exact zero-based positions and requested column names; the summarizer checks that schema against the exported header. `parents` can export blank after `LOAD`, so ancestry comes from the original `.spop`, not that DETAIL field. `task.i` is a count, not an input-general success rate. For graded tasks, a positive count can mean partial credit; `task_quality.i` sums quality across outputs and cannot identify an individual exact match. `viable` means the stock test CPU found a replication closure within its test horizon; it is not a claim that the initial sequence copies itself exactly.

Design: let \(b_{gjk}=1\) when sequence-group \(g\) is viable and task \(j\)'s count is positive on input set \(k\). Let \(v_{gj}=\min_k b_{gjk}\). Report raw task occurrence, viable occurrence on any tested input, and viable occurrence on every tested input separately. At snapshot \(t\), report \(p_{tj}=\sum_g n_{gt}v_{gj}/\sum_g n_{gt}\), retaining every raw count. Presence means \(p_{tj}>0\); a declared prevalence threshold may be displayed alongside it. This tests the same sequence across inputs; different sequences succeeding on different inputs do not satisfy that requirement.

Design: use a separate, complete reward-history ledger. For each canonical task record its earliest update with a positive reward opportunity, `never` if the complete run history excludes one, or `unknown`. Include adaptive controller changes and resource-limited reward rules, not just the final environment file. “Never directly rewarded” does not exclude indirect selection through shared circuitry. Future rewards mean “not yet rewarded” at earlier snapshots, not “never rewarded.” Alias rewards must propagate to their canonical name; unresolved semantic equivalences remain flagged. Missing history remains unknown.

Work estimate: with \(G\) sequence groups, \(K\) input sets and \(P\) isolated profiles, testing costs roughly \(GKP\) test-CPU evaluations; core tasks are checked together, not by 157 separate executions. [checked, S5] A test can run up to three replication generations, each allotted `TEST_CPU_TIME_MOD × current length` instructions; default multiplier 20. Profile/task checking and I/O add costs. Estimate CPU seconds by timing the first fixed batch of 100 sequences under the actual panel and multiplying by remaining evaluations; retain this as a forecast, not an experimental result. For 23,332 groups and eight input sets, the core entails 186,656 evaluations.

Misleading cases: an always-positive control inflates richness; aliases inflate it again; a task present only under one input is input-sensitive; a zero for an unavailable context is not a task failure; the finite deck misses untested input behavior. The appendix summarizer excludes known aliases and the control from core name richness, checks expected living IDs and actual inputs, and stops on missing output. Its counts still describe task definitions, not independent discoveries. Nine fixed-output Fibonacci checks remain tagged `constant_output`. On positive inputs, absolute value and echo cannot be distinguished; a new task label on this deck need not be a new transformation. Keep the generated schema, commands, environment and results together: repeated header names cannot detect a same-width task-order swap.

### Retention across saved populations

Design: use the same core profile, inputs, instruction meanings and test horizon for every snapshot. Assay overrides are `TEST_CPU_TIME_MOD 20`, `TASK_REFRACTORY_PERIOD 0`, a fixed `RANDOM_SEED`, and generated `ENVIRONMENT_FILE`, `ANALYZE_FILE`, `EVENT_FILE`, and `DATA_DIR`; the generator applies them explicitly. No additional evolution settings are needed. The summarizer produces `capabilities.tsv`, `retention.tsv` and `snapshot_dynamics.tsv`.

For capabilities \(S_t=\{j:p_{tj}>0\}\), endpoint retention is \(|S_a\cap S_b|/|S_a|\). Output its numerator and denominator; an empty earlier set gives an undefined fraction. Also output \(|\bigcap_{t=a}^{b}S_t|\): capabilities present at every saved observation. A capability present at both endpoints but absent at an intervening snapshot is reported as “present after sampled gap.” These are population measures, with no identity-of-carrier implication.

[checked-source inference, S7] Use recorded ancestry to ask a different question. Test every available node on a selected parent path with the same deck. A positive–negative–positive path supports loss and reacquisition along that recorded path. An all-positive path supports retention along its recorded nodes. Missing parents, branches omitted by saving, and merged origins prevent a complete historical verdict. Do not label positive endpoints alone as retention by descent. Saving every update reduces temporal gaps but does not remove the source's group-merging limitation.

Computation after testing is linear in exported rows plus a quadratic snapshot retention table; no additional virtual-CPU runs. Changing snapshot spacing can change the measured continuity. Report sampling intervals, carrier fractions and task identities, rather than interpreting the retention fraction alone as learning.

### First observed appearance and recorded ancestry

[checked, S6–S8] `SavePopulation filename=history:save_historic=1` writes `history-UPDATE.spop`. Its named arguments are separated by colons. Historical saving defaults to one. `DISABLE_GENOTYPE_CLASSIFICATION 0` permits classification and retained ancestry; `TRACK_MAIN_LINEAGE` is not a registered setting at this commit. The save contains living groups and retained ancestor groups, not every sequence ever created.

[checked, S7] The relevant saved columns include `id`, `parents`, `depth`, `update_born`, `num_units`, `total_units` and `sequence`. Read the file's `#format`; do not assume numeric column positions. `num_units=0` marks an extinct retained group. Parent records describe sequence-group origins. Avida merges matching sequences into an already active group, so an additional independent origin can disappear from this representation.

Design: find each task's earliest positive **sampled** snapshot from the capability table. Retest all retained historical groups, without the living filter, to locate earlier positive groups. [checked, S7] A group's birth update is the birth of that saved group, not the instant a running program first produced a task output. If ancestry and the assay are complete along a chosen path, report each negative-to-positive transition and its group birth update; otherwise report the observable interval and missing records.

The appendix ancestry helper unions files from one explicitly named continuous segment, checks identity conflicts and missing parents, and emits `selected-lineage.spop` in ancestor-to-descendant order plus an edge table. The analyze script exports aligned sequences and reconstructed `parent_dist` and `parent_muts` for non-root edges; root rows are excluded from the edge export because their change string is empty. [checked, S1–S3] Those changes are a minimum-edit reconstruction between saved strings, not a log of the actual copying events. Repeated blocks and insertions/deletions can admit other histories.

[checked, S6–S8] `LoadPopulation` allocates new group IDs and remaps parents. Treat each restart as a new identity namespace. Equal sequence strings across a restart can link computational content, but cannot by themselves link historical individuals. `PrintNewTasksData` counts renewed task performance relative to prior performance and does not name the originating sequence; it is not an origin archive. No checked setting supplies a complete per-program, per-birth task genealogy for these experiments.

Cost: parsing and parent traversal scale with saved records and path length; testing \(H\) retained ancestors costs approximately \(HK\) evaluations per profile. Retesting only a chosen path misses independent origins. Global first appearance remains unavailable when relevant branches were never saved.

### Reuse of earlier instruction dependencies

[checked, S9] `MAP_TASKS` runs the unmodified sequence and every single-site null ablation with the same explicit input set. It activates a stock internal null instruction; no instruction-set modification is needed. Its text file contains one-based position, original symbol and instruction name, the requested columns, and a baseline row with position `-1`, batch name and sequence ID. The appendix requests `viable fitness gest_time env_input.0 env_input.1 env_input.2` and task columns. Each file belongs to one sequence; its source row and ancestry metadata must be retained.

Design: for earlier task \(a\), collect positions whose null ablation removes \(a\) while the tested sequence remains viable. Do the same for later task \(b\). Report the input-by-position matrix before intersecting across inputs. An ablation that also removes replication is a joint dependency, not a task-specific one. Count neither as a proof of the route taken by data: an extra input read can change later input alignment without feeding the output directly.

Align the ancestor and descendant. Where a retained instruction's correspondence is supported by the chosen reconstruction, ask whether its ablation removes the earlier capability in the ancestor and the later capability in the descendant. Report shared ablation dependence conditional on that correspondence. For ambiguous repeated blocks, report alternative alignments or leave positional inheritance unresolved. Even a unique minimum-edit alignment is inferred, not recorded copying history.

A single ablation can miss interchangeable instructions. The appendix includes selected pair/group ablations for this case. A lost task after a joint ablation, when each single ablation preserves it and viability remains, indicates redundant support under that assay. These tests do not determine whether an earlier task caused the later one to arise or whether the population used the same circuit throughout.

Cost: \(K\sum_g(L_g+1)\) evaluations for single maps; exhaustive pairs add \(K\sum_g L_g(L_g-1)/2\). At length 100 and eight inputs, one sequence needs 808 baseline/single evaluations, or 39,600 additional pair evaluations. Start with preselected transition paths; the optional code tests specified groups, not all pairs. Keep resource and reward context fixed when interpreting fitness loss.

### Standard dynamics measures and explicit snapshot substitutes

[checked] Bedau, Snyder and Packard (1998) attach activity counters to components. Their presence-based increment is one per occupied time step; reported quantities include diversity, mean cumulative activity and activity within a declared “new” activity band. Their neutral shadow randomizes selected identities while matching event dynamics. Avida's no-task-reward treatment still selects for replication and is not that shadow. Accordingly, stock snapshots supply sampled presence counters, not the original neutral-normalized activity classification. [Primary paper](https://people.reed.edu/~mab/papers/alife6.pdf).

Design: define a component as `(hardware type, instruction set, instruction string)`. The appendix reports sampled activity \(a_i(k)=\sum_{r\leq k}1[i\in S_r]\), in observations, not elapsed updates. It computes diversity, mean activity and activity in a user-declared snapshot-count band. Equal strings across gaps share one counter; this is sequence-identity occupancy, not genealogical residence. An unchanged population makes these counters rise without learning. Multiplying by snapshot spacing would require an interpolation assumption; neither the script nor the interpretation does so. No neutral normalization is supplied.

[checked] MODES distinguishes change, novelty, complexity and ecology after an explicit filter. Its paper's Avida implementation uses future-descendant persistence and fitness-sensitive instruction skeletons; complexity concerns retained sites and ecology concerns component abundance diversity. The published experiment used modified Avida. The paper-linked code saves original snapshot abundances, filters by descendant survival, and combines identical skeletons. Its taxon creation rules preserve distinctions that stock Avida can merge. Therefore ordinary stock snapshot derivatives are not an exact replay of those published measurements. [Paper](https://cse.msu.edu/~dolsonem/pdfs/modes_paper.pdf); [implementation](https://github.com/emilydolson/Empirical/blob/5171c8713e2fcba9dd58b5b77abefe7529050f1d/source/Evolve/OEE.h).

Design: the appendix calculates unfiltered snapshot arrivals \(|S_t\setminus S_{t-1}|\), first-observed names/sequences \(|S_t\setminus\bigcup_{r<t}S_r|\), and abundance entropy. The core summary uses natural logarithms; the independent sequence-dynamics script labels its base-two entropy in bits. Its initial change fields are blank; the core summary's initial first-observed counts are baseline inventories, not demonstrated additions. The incomplete group genealogy does not support reproducing the published future-descendant filter, so no supplied script claims to apply it.

Design: for a stock fitness-complexity substitute, use `map_lineage.py --graded`, which gives the nine standard tasks their graded rewards and leaves the remaining core reactions neutral and uses the same fixed input deck. The map summarizer emits the count and ordered symbols of positions whose null ablation lowers baseline Avida fitness. Report the maximum count among viable tested sequences and retain the input-specific values. Differences smaller than the printed fitness precision can be missed. This supplies unfiltered, reference-environment complexity; it is not the full published MODES measurement. [checked, S2] `DETAIL complexity` uses another calculation and is not substituted. Grouping the saved abundances by these skeleton strings before computing entropy would define yet another explicitly chosen component set; that optional aggregation is not performed here.

The appendix's snapshot statistics need no extra engine runs; fitness-complexity maps cost the ablations above. Instruction-sequence turnover can raise novelty without adding a capability, and neutral variation can raise entropy. Observing a finite catalogue for a finite time cannot settle indefinitely continuing learning. Report new input-tested capabilities alongside retention, dependence and the fixed catalogue's remaining coverage.

The generated headers name every derived column; these are the principal output schemas.

| Output | Columns |
|---|---|
| `capabilities.tsv` | `label update task task_kind canonical first_reward_update reward_status population raw_any viable_any viable_all fraction_all inputs` |
| `retention.tsv` | `from_label to_label baseline endpoint_retained endpoint_fraction every_saved_snapshot present_after_sampled_gap` |
| `snapshot_dynamics.tsv` | `label update population distinct_sequences sequence_entropy_nats sequence_arrivals first_observed_sequences core_names_present first_observed_core_names` |
| Ancestry edge table | `parent_id child_id parent_update child_update parent_sequence child_sequence` |
| Ablation `summary.tsv` | `input_id id task baseline_viable baseline_task_count length required task_preserved viability_confounded baseline_ineligible baseline_task_absent` |
| `fitness_summary.tsv` | `input_id viable_baselines max_fitness_required_sites`; companion `fitness_sites.tsv` retains positions and skeletons |
| Raw dynamics CSV | `update program_count distinct_sequences raw_additions raw_losses raw_first_observations raw_sequence_entropy_bits mean_observed_presence_snapshots band_low_snapshots band_high_snapshots raw_band_activity_snapshots` |

## What must be switched on before a run

[checked, S6–S8] The appendix contains one configuration fragment and one event fragment for future continuous runs. Keep the original treatment, ancestor, instruction-set include, instruction-change rates, seed and world settings. Add classification and named snapshots; these save actions observe without restarting. Keep existing injection and exit events, placing the last save before the exit at that update.

[checked-source inference, S7–S8] Use historical snapshots every 1,000 updates and aggregate task-execution prints every update. The latter can locate the first logged live execution of an already configured task, but supplies no performer ID. Denser snapshots can narrow observation gaps at additional disk cost; they still miss within-update branches and merged origins. For a restart-based experiment, preserve separate directories, configuration/reward-controller histories and segment boundaries. The report does not remove the separate restart-effect question.

## What can be measured on runs already saved without those settings and what cannot

[checked-source inference, S1–S9]

| Available record | Supported measurement | Unresolved part |
|---|---|---|
| Living sequences, abundances and original instruction set | Fixed-input capabilities, sampled prevalence, endpoint retention, name/sequence novelty, direct ablations | What happened between snapshots |
| Retained historical sequences and parents from one segment | Recorded parent paths, inherited content candidates, reconstructed instruction edits | Pruned branches, merged origins, exact instruction-change chronology |
| Full reward schedules and controller logs | Direct reward exposure classification | Indirect selection; realized rewards unless separately recorded |
| Final reward configuration only | Current configured reward opportunities | “Never rewarded” during the whole run |
| Snapshot files from restarted pieces | Assays of saved content, within-segment ancestry | Cross-restart identity without a separate mapping record |
| Aggregate task output alone | Aggregate task occurrence at printed dates | Every-sequence capability, ancestry and instruction reuse |

These are consequences of the checked source behavior above, not claims that the owner's saved files contain every listed field. The scripts inspect formats and stop where their needed evidence is missing.

## Source locations checked

All source entries below were read at [`devosoft/avida` commit `47f13dadb547fcf10f620ace60247f38b30b8b16`](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16). Paths beginning `source/` are under `avida-core/`. `checked` means read in source, not measured on the owner's populations.

| Key | File and function | Command, argument or column checked |
|---|---|---|
| S1 | `source/analyze/cAnalyze.cc`: `LoadFile`, `CommandFilter`, `BatchRecalculate`, `CommandDetail`, `CommandDetail_Header`, `CommandDetail_Body`, `SetupCommandDefLibrary`, `BatchPurge`, `FindLineage` | `LOAD`, `FILTER num_units > 0`, `RECALCULATE` positional resource/update/random/manual arguments, `DETAIL`, `#format`, `PURGE_BATCH` registration |
| S2 | `source/analyze/cAnalyzeGenotype.cc`: `buildDataCommandManager`, `Recalculate`; header `GetTaskCount` | IDs, parents, abundances, sequences, input/task/quality columns; viable and fitness; inferred parent edits |
| S3 | `source/main/cTaskLib.cc`: `AddTask`, `SetupTests`, task loaders/evaluators; `cEnvironment.cc`: `LoadReaction`, `LoadReactionProcess`, `TestOutput`, `DoProcesses`; `cPhenotype.cc`: `TestOutput` | All registered names and per-name handlers/loaders in generated `task_audit.json`; `Task_AllOnes`, `Task_FibonacciSequence`, `Task_Optimize`, `Load_MatchProdStr` hazards; manual-input requirement, neutral reward, task/quality semantics |
| S4 | `source/main/cAvidaConfig.h`; `cAvidaConfig.cc`: `Load`; `source/util/CmdLine.cc`: `processArgs` | Config registration, instruction-set include, analysis mode and overrides |
| S5 | `source/cpu/cTestCPU.cc`: `ProcessGestation`, `TestGenome_Body`; `cCPUTestInfo`; `nHardware.h` | CPU horizon, three-generation default, fixed manual inputs, viability |
| S6 | `source/actions/SaveLoadActions.cc`: `cActionSavePopulation`, `cActionLoadPopulation` | Named colon-separated save/load arguments and filename suffix |
| S7 | `source/main/cPopulation.cc`: `SavePopulation`, `LoadPopulation`; `source/systematics/Genotype.cc`: constructor, `LegacySave`; `GenotypeArbiter.cc`: `ClassifyNewUnit`, `LegacyLoad`, `removeGenotype` | Historical retention, saved schema, IDs remapped on reload, merging/pruning |
| S8 | `source/actions/PrintActions.cc`: registrations; `source/main/cStats.cc`: `PrintTasksData`, `PrintTasksExeData`, `PrintNewTasksData`; `source/main/cEventList.cc`: `AddEventFileFormat`; `cPhenotype.cc`: `TestOutput` | Aggregate task output and why renewed-task counts do not identify first origins |
| S9 | `source/analyze/cAnalyze.cc`: `CommandMapTasks`, `CommandAlign`, `LoadSequence`; `source/cpu/cInstSet.cc`: `ActivateNullInst`; `cHardwareCPU.cc`: `initInstLib`; `source/core/InstructionSequence.cc`: `Instruction::GetSymbol` | `MAP_TASKS`, manual inputs, baseline/site rows, null activation, inferred alignment, optional group substitutions |
| S10 | Bedau, Snyder and Packard, *A Classification of Long-Term Evolutionary Dynamics* (1998), equations 1–7; Dolson et al., *The MODES Toolbox* (2019), sections 3–4 | Activity counters, filtering, definitions and implementation scope |
| S11 | Paper-linked Empirical `OEE.h`: `Update`, `CoalescenceFilter`, `CalcStats`, `Skeletonize`; `Systematics.h`: `AddOrg` | Snapshot counts, skeletons, filtering and independent-origin distinction |

## Assumptions and what you are unsure of

The frozen question is what saved populations can do under declared stock assays, how that changes, and what the record permits us to infer about retention and reuse. This is a design-and-measurement question. The owner's reported prior experiments are inputs to the brief, not new results measured here. No constructor-theoretic equivalence is assumed.

| Part of the design | Hard-to-vary mark | What the criticism changes |
|---|---|---|
| Unmodified pinned engine | Fixed | Owner's scope; no new execution environment or source patch |
| Identical inputs, horizon and instruction meanings | Held for the time comparison | Changing the assay alone can create apparent learning |
| Exact input deck size and prevalence threshold | Loose | Other declared decks/thresholds can serve the same question; show sensitivity |
| Reward-history ledger | Held | Removing it makes “never rewarded” indistinguishable from missing records |
| Endpoint retention alone | Idle for ancestry inference | A loss-and-return case gives the same endpoints; keep it for the narrower endpoint question |
| Full historical inference from group parents | Unknown | Pruning, merging and reload namespaces prevent the promised distinction |
| Shared ablation dependence | Held if correspondence is supported | A repeated-block alignment can change the attributed overlap |
| Open-endedness from rising catalogue counts | Unknown | A finite catalogue can exhaust; sequence turnover is a rival explanation |
| Named dynamics interpretation | Borrowed | Depends on published component/filter definitions; substitutes are explicitly renamed |

The whole-design countercases were frozen before the summarizer was written: unchanged populations, abundance-only change, no capabilities, loss then return, reordered task indices, incomplete input output, and missing parents. A passing smoke check exercises code behavior on those cases; it does not supply the missing historical observations. Paired ablations challenge a clean single-site map. The unsupported-context count is the gauge against hiding failures in an “other tasks” category.

[checked, executed here] Unmodified Avida 2.14.0 compiled at the pinned commit. A 100-update, 10×10 smoke run completed; it was an implementation check, not one of the owner’s experiments. All 18 enabled probe profiles ran on its saved ancestor/end populations and on three authored controls, producing 108 files and 2,160 rows. Explicit inputs and known alias counts matched; the controls produced the expected zero, one and two NOT counts. Single and paired null tests distinguished a necessary instruction from redundant support while viability remained.

The first live export exposed stripped column suffixes and blank `parents`; those outputs were retained and the rig changed to positional schemas and original ancestry fields. Earlier source review removed unsupported legacy batch keywords. Independent synthetic checks covered loss/return, abundance-only change, complementary performers, empty baselines and missing data; subsequent attacks prompted rejection of stale sequence identities and duplicate inputs. Stock historical-row parsing and a seven-group ancestry path were also exercised. These are limited implementation checks, not observations of new knowledge in the owner’s populations.

## Appendix

Save the code blocks under their displayed filenames in one working directory. Python 3.9 or later and the pinned, built Avida source are required. Replace the paths and selected sequence ID with actual records. Use global elapsed updates in the snapshot manifest; ancestry extraction accepts only one uninterrupted segment. Keep generated configurations, schemas, logs and results together.

### avida.cfg fragment

Merge this setting into the experiment's existing file; do not replace its other settings.

```text
DISABLE_GENOTYPE_CLASSIFICATION 0
```

### events.cfg fragment

Insert these lines after the initial injection/load event and before the final exit event. They add observation, not save/reload cycles. [checked] The first print has update then executions per configured task during that update; the second has update then counts based on stored task performance. Their task order is the evolution environment's order, not the later probe catalogue.

```text
u 0:1000:end SavePopulation filename=history:save_historic=1
u 0:1:end PrintTasksExeData task-executions.dat
u 0:100:end PrintTasksData task-performers.dat
```

### Run the probe battery and summaries

These shell variables are examples to fill with existing paths. The output directory must be new. `safe` runs the 18 enabled profiles serially; it does not attempt the 40 missing contexts or `all-ones`. The summarizer computes the binary core panel; parameterized profiles retain separate raw counts, qualities and signatures. Complete the generated reward-history template and rerun with `--rewards` only when the entire reward history is available.

```bash
AVIDA_BIN=/absolute/path/to/avida
AVIDA_SOURCE=/absolute/path/to/avida-source
ORIGINAL_RUN=/absolute/path/to/original-run
MEASUREMENT_DIR="$PWD"
PROBE_OUT="$MEASUREMENT_DIR/probes"
python probe_task_audit.py --source "$AVIDA_SOURCE" --run-dir "$ORIGINAL_RUN" \
  --snapshot u10000 10000 "$ORIGINAL_RUN/data/history-10000.spop" \
  --snapshot u20000 20000 "$ORIGINAL_RUN/data/history-20000.spop" \
  --out "$PROBE_OUT" --avida "$AVIDA_BIN" --profiles safe --run
python summarize_probes.py "$PROBE_OUT"
# After checking and completing the history template:
# python summarize_probes.py "$PROBE_OUT" --rewards complete-reward-history.tsv
```

The history TSV has `canonical` and `first_reward_update`; the latter holds an integer, `never`, or `unknown`. The generated template starts unknown. Known aliases must inherit the canonical exposure; domain-specific equivalences still require interpretation.

### Recover and map a selected ancestry path

The example ID must be replaced by the observed task-performing group's ID. Supply same-segment snapshots in time order. `map_lineage.py` uses the suite's exact core input deck and task indices, emits the analyze script and command, and optionally executes it. Run it again with `--graded` and a different output directory for reference-fitness complexity. The grade override rewards NOT/NAND by 2¹, AND/ORN by 2², OR/ANDN by 2³, NOR/XOR by 2⁴ and EQU by 2⁵; all other core reactions remain neutral.

```bash
python ancestry-helper.py --segment continuous-run1 --target 123 \
  --output selected-lineage.spop \
  "$ORIGINAL_RUN/data/history-10000.spop" "$ORIGINAL_RUN/data/history-20000.spop"
MAP_OUT="$MEASUREMENT_DIR/lineage-maps"
python map_lineage.py --suite "$PROBE_OUT" --lineage selected-lineage.spop \
  --target 123 --out "$MAP_OUT" --run
python - "$MAP_OUT" <<'PYRUN'
import pathlib, subprocess, sys
p=pathlib.Path(sys.argv[1])
subprocess.run([sys.executable,'summarize_maps.py',str(p/'maps.tsv'),
               '--out',str(p/'summary'),'--tasks',
               *(p/'task_indices.txt').read_text().split()],check=True)
PYRUN
```

For conditional reuse, provide `--matches matches.tsv` to the map summarizer. Its tab-separated columns are `ancestor_id ancestor_site ancestor_task descendant_id descendant_site descendant_task basis`. Sites are one-based; the written basis must identify the positional reconstruction. Endpoint symbol agreement alone is not uninterrupted instruction inheritance.

### Selected paired or grouped ablations

Create `groups.csv` with `id,sites`; a row such as `123,7;19` requests simultaneous null replacement at positions 7 and 19 of ID 123. Choose actual IDs/sites from the single maps. The pinned generated core uses task indices 6 for NOT and 22 for EQU; use its dictionary for other tasks. Synthetic names encode their source and sites. Group DETAIL columns are recorded separately in `group-analyze.columns.json`, because stock headers drop task suffixes.

```bash
python group_ablation.py selected-lineage.spop groups.csv group-analyze.cfg \
  6 22 --inputs "$PROBE_OUT/inputs.tsv"
mkdir -p "$MEASUREMENT_DIR/group-results"
cd "$ORIGINAL_RUN"
"$AVIDA_BIN" -c avida.cfg -a \
  -set ANALYZE_FILE "$MEASUREMENT_DIR/group-analyze.cfg" \
  -set ENVIRONMENT_FILE "$PROBE_OUT/core/environment.cfg" \
  -set EVENT_FILE "$PROBE_OUT/events.cfg" \
  -set DATA_DIR "$MEASUREMENT_DIR/group-results" \
  -set RANDOM_SEED 20260930 -set TASK_REFRACTORY_PERIOD 0 -set TEST_CPU_TIME_MOD 20
cd "$MEASUREMENT_DIR"
```

### Sampled sequence activity

Convert the existing manifest once, then choose an activity band before interpreting results. The example band is one to two observed snapshots; it is a declared design choice. No shadow normalization or descendant filter is applied.

```bash
python - "$PROBE_OUT" <<'PYRUN'
import csv,pathlib,sys
p=pathlib.Path(sys.argv[1])
with (p/'snapshots.tsv').open() as f:
    rows=list(csv.DictReader(f,delimiter='\t'))
with (p/'snapshots.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,['update','path']);w.writeheader()
    w.writerows({k:r[k] for k in ['update','path']} for r in rows)
PYRUN
python dynamics_metrics.py "$PROBE_OUT/snapshots.csv" "$PROBE_OUT/dynamics.csv" \
  --band-low 1 --band-high 2
```

### probe_task_audit.py

```python
#!/usr/bin/env python3
"""Generate stock-Avida 47f13dad probe environments and analyze scripts.

This is an external file generator, not an Avida modification. Each observation
is a fresh test-CPU execution. Existing run files and snapshots are read only.
Use --run to execute the generated commands sequentially (one Avida process).
All task claims are source-checked; an unrun profile is not a measured result.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import random
import re
import shlex
import subprocess
import time

COMMIT = "47f13dadb547fcf10f620ace60247f38b30b8b16"
BOOL = "not nand and orn or andn nor xor equ".split()
# Every parameter here is a chosen probe specification, not a task's identity.
# These profiles run separately because loaders can change buffer capacities.
PARAMS = {
    "matchstr": "string=01011010,partial=0,binary=0",
    "match_number": "target=12345,threshold=0,halflife=1",
    "matchprodstr": "string=01011010,partial=0,binary=0,tag=-1",
    "sort_inputs": "size=3,direction=0,contiguous=1,halflife=1",
    "fibonacci_seq": "target=8,penalty=0",
    **{n: "threshold=0,halflife=1" for n in
       "mult div log log2 log10 sqrt sine cosine".split()},
    "optimize": "function=22,binary=1,varlength=8,numvars=1,maxFx=8,minFx=0,thresh=0",
    "all-ones": "length=1",
    # length=1 avoids reading output-buffer entries before they are written.
    "royal-road": "length=1,block_count=1",
    "royal-road-wd": "length=1,block_count=1,width=1,height=1",
}
ALIASES = {n + "_dup": n for n in ["echo", *BOOL]}
ALIASES.update({"math_2AX": "math_2AT", "math_2AN": "add",
                "math_2AO": "sub", "math_2AY": "math_2AS",
                "math_3AH": "add3", "matchprodstr": "matchstr"})
CONTEXT = {
    "xor-max": "Reads resources, changes reaction resource; requires a resource profile.",
    "nand-resourceDependent": "Requires named pheromone resource and population resource table; cutoff 100.",
    "nor-resourceDependent": "Requires named pheromone resource and population resource table; cutoff 100.",
    "comm_echo": "Requires actual neighbor input buffers; test CPU has no neighbors.",
    "comm_not": "Requires actual neighbor input buffers; test CPU has no neighbors.",
    "sg_path_traversal": "Requires STATE_GRID, pathlen/sgname/poison and state-grid instructions absent from heads.",
    "form-group": "Reads population group sizes; isolated test CPU supplies no populated social context.",
    "form-group-id": "Requires group membership, group ID and population group sizes.",
    "live-on-patch-id": "Reads opinion attribute; relevant state-setting instruction absent from heads.",
    "collect-odd-cell": "Tests cell-ID parity; test CPU cell ID is -1, a misleading positive is possible.",
    "perfect_strings": "Reads stored-string state rather than generic IO; production context absent.",
    "event_killed": "Reads event-killed flag; event world and relevant instructions absent.",
    "consume-public-good": "Reads and modifies living neighboring programs; no such test-CPU population.",
    "ai-display-cost": "Reads lyse-display flag; relevant state-setting instruction absent from heads.",
    "produce-public-good": "Reads explosion/public-good phenotype state; relevant instructions absent from heads.",
    "exploded": "Reads explosion flag; explosion instruction absent from heads.",
    "exploded2": "Reads second explosion flag; explosion instruction absent from heads.",
    "opinion_is": "Reads opinion attribute; relevant state-setting instruction absent from heads.",
}


def function_body(source, function):
    m = re.search(r"(?:void|double) cTaskLib::" + re.escape(function) + r"\(", source)
    if not m:
        raise ValueError("Cannot locate function " + function)
    start = source.index("{", m.end())
    depth = 1
    end = start + 1
    while depth:
        depth += (source[end] == "{") - (source[end] == "}")
        end += 1
    return source[start:end], source[:m.start()].count("\n") + 1


def audit(source):
    registration = source[:source.index("void cTaskLib::NewTask")]
    found = list(re.finditer(r'name == "([^"]+)"', registration))
    rows = []
    for k, m in enumerate(found):
        name = m.group(1)
        chunk = registration[m.end():found[k + 1].start() if k + 1 < len(found) else len(registration)]
        load = re.search(r"(Load_\w+)\(name", chunk)
        call = re.search(r"&cTaskLib::(Task_\w+)", chunk)
        loader, args = "", []
        if load:
            loader = load.group(1)
            body, _ = function_body(source, loader)
            call = re.search(r"&cTaskLib::(Task_\w+)", body)
            args = re.findall(r'schema.AddEntry\("(\w+)"\s*,\s*\d+\s*,\s*([^;]+)\);', body)
        handler = call.group(1) if call else ""
        if not handler:
            raise ValueError("No handler for " + name)
        _, handler_line = function_body(source, handler)
        core = (name in ["echo", "echo_dup", "add", "add3", "sub", "dontcare"] or
                name.removesuffix("_dup") in BOOL or name.startswith(("logic_", "math_", "fib_")))
        profile = "core" if core else name if name in PARAMS else ""
        if name == "dontcare":
            status, reason = "control", "Always returns one when evaluated; exclude from capability richness."
        elif name.startswith("fib_"):
            status, reason = "constant_output", "Checks a fixed number after input; not an input-to-output function."
        elif name == "all-ones":
            status, reason = "output_domain_required", "Raw output/length can be negative and fail Avida's nonnegative-quality assertion. Disabled by default."
        elif name in ALIASES:
            status, reason = "alias", "Same detector behavior as canonical within this three-input profile; do not count twice."
        elif core:
            status, reason = "supported", "Source detector uses input/output buffers; fixed low input domain in this profile."
        elif name in PARAMS:
            status, reason = "parameterized", "Fresh isolated execution with the explicit parameters listed; interpretation is profile-specific."
        else:
            status = "context_missing"
            reason = CONTEXT.get(name)
            if name.startswith("eat-target"):
                reason = "Requires forage-target state; target-setting instruction absent from standard heads; fresh default is -1."
            elif name.startswith("move"):
                reason = "Requires population movement/location/event state; test interface returns cell -1, no deme, and Move false; detector may be vacuous or unsafe."
            if reason is None:
                raise ValueError("Unclassified task: " + name)
        if name == "fibonacci_seq":
            reason = "Eight-step prefix, fresh state; max_count=8 stops evaluation before large Fibonacci sums. task count 8 denotes full prefix."
        if name in ["matchstr", "matchprodstr", "sort_inputs", "optimize", "royal-road", "royal-road-wd"]:
            reason += " Nonzero count alone is not exact completion; quality is accumulated, not a maximum."
        if name.startswith("royal-road"):
            reason += " Length-one probe only; larger lengths can read unwritten output-buffer entries."
        if name == "optimize":
            reason += " Detector returns 0.001 even on failure; task count measures opportunities, not success."
        rows.append(dict(name=name, profile=profile, task_index="", status=status,
                         canonical=ALIASES.get(name, name), args=PARAMS.get(name, ""),
                         default_enabled=bool(profile) and name != "all-ones", reason=reason,
                         source_status="checked", loader=loader, handler=handler,
                         registration_line=registration[:m.start()].count("\n") + 1,
                         handler_line=handler_line, argument_schema=args))
    if len(rows) != 214 or len({r["name"] for r in rows}) != 214:
        raise ValueError("Expected exactly 214 names at the pinned commit")
    return rows


def write_tsv(path, rows, fields):
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fields, delimiter="\t", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def safe_path(path):
    path = Path(path).resolve()
    if re.search(r"\s|[#$]", str(path)):
        raise ValueError("Avida analyze paths must have no spaces, # or $: " + str(path))
    return path


def triples(count, seed, high=False):
    rng = random.Random(seed)
    result = []
    for i in range(count):
        if high:
            values = [(mask << 24) | rng.randrange(1 << 24) for mask in [15, 51, 85]]
        else:
            # Place all 8 Boolean cases in low bits, then vary bit order,
            # input-channel order, and two additional bits. All values 15..1023.
            bit_order = list(range(8))
            rng.shuffle(bit_order)
            values = [sum(((mask >> j) & 1) << bit_order[j] for j in range(8)) |
                      (rng.randrange(4) << 8) for mask in [15, 51, 85]]
        rng.shuffle(values)
        patterns = {sum(((v >> b) & 1) << j for j, v in enumerate(values)) for b in range(32)}
        assert patterns == set(range(8)) and len(set(values)) == 3
        if not high:
            assert all(3 <= v <= 1023 and v != 7 for v in values)
        result.append(values)
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", required=True, help="Pinned Avida source checkout")
    p.add_argument("--run-dir", required=True, help="Original run folder (instruction-set/config dependencies)")
    p.add_argument("--config", default="avida.cfg")
    p.add_argument("--snapshot", nargs=3, action="append", required=True, metavar=("LABEL", "UPDATE", "PATH"))
    p.add_argument("--out", required=True, help="New output directory; must not already exist")
    p.add_argument("--inputs", type=int, default=8)
    p.add_argument("--seed", type=int, default=20260930)
    p.add_argument("--avida", default="avida", help="Executable path or name on PATH")
    p.add_argument("--profiles", default="core", help="core, safe, all, or comma-separated profile names; safe includes 16 parameter profiles and logic_high")
    p.add_argument("--run", action="store_true", help="Execute selected profiles sequentially, preserving logs and first outputs")
    a = p.parse_args()
    if a.inputs < 2:
        p.error("Use at least two input triples")
    src, run_dir, out = map(safe_path, [a.source, a.run_dir, a.out])
    config = safe_path(run_dir / a.config)
    source_path = src / "avida-core/source/main/cTaskLib.cc"
    source = source_path.read_text()
    # Refuse silent use of a different revision when this is a Git checkout.
    head = subprocess.run(["git", "-C", str(src), "rev-parse", "HEAD"], text=True, capture_output=True)
    if head.returncode == 0 and head.stdout.strip() != COMMIT:
        p.error("Source checkout must be " + COMMIT)
    if not config.is_file():
        p.error("Missing config: " + str(config))
    snapshots = []
    for label, update, path in a.snapshot:
        if not re.fullmatch(r"[A-Za-z0-9_-]+", label):
            p.error("Labels may contain letters, digits, underscores, hyphens")
        path = safe_path(path)
        if not path.is_file():
            p.error("Missing snapshot: " + str(path))
        snapshots.append(dict(label=label, update=int(update), path=str(path)))
    if len({s["label"] for s in snapshots}) != len(snapshots):
        p.error("Snapshot labels must be unique")
    rows = audit(source)
    profiles = {}
    for row in rows:
        if row["profile"]:
            profile_rows = profiles.setdefault(row["profile"], [])
            row["task_index"] = len(profile_rows)
            profile_rows.append(row)
    # This companion isolates Boolean transfer to original-size input numbers,
    # so arithmetic detectors cannot overflow in the high-range execution.
    profiles["logic_high"] = []
    for row in rows:
        if row["name"] in BOOL or row["name"].startswith("logic_"):
            r = dict(row, profile="logic_high", task_index=len(profiles["logic_high"]))
            r["reason"] = "Boolean-only companion with original-size inputs; separate magnitude-transfer profile."
            profiles["logic_high"].append(r)
    if a.profiles == "safe":
        selected = [n for n in profiles if n != "all-ones"]
    elif a.profiles == "all":
        selected = list(profiles)
    else:
        selected = a.profiles.split(",")
    if set(selected) - profiles.keys():
        p.error("Unknown profiles: " + ", ".join(set(selected) - profiles.keys()))
    out.mkdir(parents=True, exist_ok=False)
    (out / "events.cfg").write_text("# Analyze-only; no population is advanced.\n")
    write_tsv(out / "snapshots.tsv", snapshots, ["label", "update", "path"])
    tsv_rows = [*rows, *profiles["logic_high"]]
    write_tsv(out / "tasks.tsv", tsv_rows, ["profile", "task_index", "name", "status", "canonical", "args", "reason", "default_enabled"])
    (out / "task_audit.json").write_text(json.dumps(dict(source_commit=COMMIT,
        source_sha256=hashlib.sha256(source.encode()).hexdigest(), task_names=rows,
        note="214 names audited, not 214 interchangeable capabilities. Runtime status is in run_status.json after --run."), indent=2) + "\n")
    # DETAIL drops .N suffixes in #format, so preserve the requested schema
    # separately. `parents` is omitted: the stock loader does not retain its
    # original string, so it prints an empty token and breaks whitespace rows.
    base = "id num_units viable length gest_time fitness update_born parent_id depth sequence hw_type inst_set env_input.0 env_input.1 env_input.2"
    input_rows, schema_rows, commands = [], [], []
    for profile, task_rows in profiles.items():
        d = out / profile
        d.mkdir()
        result_dir = out / "results" / profile
        result_dir.mkdir(parents=True)
        env_lines = ["# Source-checked at " + COMMIT]
        for row in task_rows:
            spec = row["name"] + (":" + row["args"] if row["args"] else "")
            req = " requisite:max_count=8" if row["name"] == "fibonacci_seq" else ""
            env_lines.append(f"REACTION P{row['task_index']:03d} {spec} process:value=0:type=pow{req}")
        env = d / "environment.cfg"
        env.write_text("\n".join(env_lines) + "\n")
        values = triples(a.inputs, a.seed, high=profile == "logic_high")
        for i, v in enumerate(values):
            input_rows.append(dict(profile=profile, input_id=i, input0=v[0], input1=v[1], input2=v[2]))
        fields = base + " " + " ".join(f"task.{i} task_quality.{i}" for i in range(len(task_rows)))
        schema_rows.extend(dict(profile=profile, position=i, column=column)
                           for i, column in enumerate(fields.split()))
        lines = []
        for snap in snapshots:
            lines += ["PURGE_BATCH", "LOAD " + snap["path"], "FILTER num_units > 0"]
            for i, v in enumerate(values):
                lines += ["RECALCULATE 0 -1 0 " + " ".join(map(str, v)),
                          f"DETAIL {snap['label']}-input{i}.dat {fields}"]
        analyze = d / "analyze.cfg"
        analyze.write_text("\n".join(lines) + "\n")
        cmd = [a.avida, "-c", str(config), "-a", "-set", "ENVIRONMENT_FILE", str(env),
               "-set", "ANALYZE_FILE", str(analyze), "-set", "EVENT_FILE", str(out / "events.cfg"),
               "-set", "DATA_DIR", str(result_dir), "-set", "RANDOM_SEED", str(a.seed),
               "-set", "VERBOSITY", "2",
               "-set", "TASK_REFRACTORY_PERIOD", "0", "-set", "TEST_CPU_TIME_MOD", "20"]
        commands.append(dict(profile=profile, cwd=str(run_dir), command=cmd, selected=profile in selected))
    write_tsv(out / "inputs.tsv", input_rows, ["profile", "input_id", "input0", "input1", "input2"])
    write_tsv(out / "schema.tsv", schema_rows, ["profile", "position", "column"])
    (out / "commands.json").write_text(json.dumps(commands, indent=2) + "\n")
    script = ["#!/usr/bin/env bash", "set -u", "cd " + shlex.quote(str(run_dir)), "status=0"]
    for c in commands:
        if c["selected"]:
            log = out / c["profile"] / "run.log"
            script.append(shlex.join(c["command"]) + " > " + shlex.quote(str(log)) + " 2>&1 || status=1")
    script.append('exit "$status"')
    (out / "run.sh").write_text("\n".join(script) + "\n")
    if a.run:
        status = []
        for c in commands:
            if not c["selected"]:
                continue
            start = time.monotonic()
            with (out / c["profile"] / "run.log").open("w") as log:
                run = subprocess.run(c["command"], cwd=c["cwd"], stdout=log, stderr=subprocess.STDOUT)
            expected = [out / "results" / c["profile"] / f"{s['label']}-input{i}.dat"
                        for s in snapshots for i in range(a.inputs)]
            missing = [str(path) for path in expected if not path.exists()]
            status.append(dict(profile=c["profile"], exit_code=run.returncode,
                               seconds=time.monotonic() - start, missing_outputs=missing,
                               complete=(run.returncode == 0 and not missing)))
            (out / "run_status.json").write_text(json.dumps(status, indent=2) + "\n")
            print(c["profile"], "exit", run.returncode, "missing", len(missing), flush=True)
        if any(not s["complete"] for s in status):
            raise SystemExit("At least one profile is incomplete; retain its log and do not treat absent rows as task failures.")
    print("Generated", out, "with", len(rows), "audited task names.")


if __name__ == "__main__":
    main()
```

### summarize_probes.py

```python
#!/usr/bin/env python3
"""Summarize the generated core battery. Python 3 standard library only."""
import argparse, csv, math
from collections import defaultdict
from pathlib import Path

def tsv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def detail(path, spop=False, expected_fields=None):
    fields = None; rows = []
    for line in Path(path).read_text().splitlines():
        if line.startswith('#format '):
            actual = line.split()[1:]
            if expected_fields is not None:
                if actual != [c.split('.')[0] for c in expected_fields]:
                    raise ValueError(f'{path}: header does not match positional schema')
                fields = expected_fields
            else: fields = actual
        elif line.strip() and not line.lstrip().startswith('#'):
            if fields is None: raise ValueError(f'{path}: missing #format')
            vals = line.split()
            row = dict(zip(fields, vals))
            omitted = fields[len(vals):]
            historical_tail = spop and int(row.get('num_units',row.get('num_cpus','-1'))) == 0 and set(omitted) <= {'cells','gest_offset','lineage'} and 'sequence' in row
            if len(vals) != len(fields) and not (len(vals)<len(fields) and historical_tail):
                raise ValueError(f'{path}: malformed row')
            rows.append(row)
    if fields is None: raise ValueError(f'{path}: missing #format')
    return rows

def write(path, fields, rows):
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fields, delimiter='\t'); w.writeheader(); w.writerows(rows)

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('suite', type=Path)
    p.add_argument('--rewards', type=Path, help='TSV: canonical,first_reward_update; integer, never, or unknown')
    a = p.parse_args(); base = a.suite.resolve()
    snaps = sorted(tsv(base/'snapshots.tsv'), key=lambda r:int(r['update']))
    if not snaps or len({r['label'] for r in snaps}) != len(snaps) or len({r['update'] for r in snaps}) != len(snaps):
        raise ValueError('Need unique labels and strictly ordered updates for ONE run')
    tasks = [r for r in tsv(base/'tasks.tsv') if r['profile']=='core' and r['name']==r['canonical'] and r['name']!='dontcare']
    inputs = [r for r in tsv(base/'inputs.tsv') if r['profile']=='core']
    if not tasks or not inputs: raise ValueError('Missing core task or input definitions')
    if len({r['input_id'] for r in inputs})!=len(inputs) or len({tuple(r[f'input{j}'] for j in range(3)) for r in inputs})!=len(inputs):
        raise ValueError('Input IDs and triples must be distinct')
    if len(inputs)<2: raise ValueError('Need at least two distinct input triples')
    schema = sorted([r for r in tsv(base/'schema.tsv') if r['profile']=='core'],key=lambda r:int(r['position']))
    if [int(r['position']) for r in schema] != list(range(len(schema))):
        raise ValueError('Column positions must be contiguous from zero')
    columns = [r['column'] for r in schema]
    if not columns or len(set(columns))!=len(columns): raise ValueError('Missing or duplicate column definitions')
    required = {'id','num_units','viable','sequence',*[f'env_input.{j}' for j in range(3)],*[f"task.{r['task_index']}" for r in tasks]}
    if not required<=set(columns): raise ValueError('Column schema misses required fields')
    rewards = {} if a.rewards is None else {r['canonical']:r['first_reward_update'] for r in tsv(a.rewards)}
    panel=[]; sets=[]; dynamics=[]; seq_seen=set(); task_seen=set(); previous_seq=set()
    for s in snaps:
        label=s['label']; update=int(s['update'])
        population=detail(s['path'], spop=True)
        living={r['id']:r for r in population if int(r.get('num_units',r.get('num_cpus','0')))>0}
        if len(living) != sum(int(r.get('num_units',r.get('num_cpus','0')))>0 for r in population):
            raise ValueError(f'{label}: duplicate source IDs')
        total=sum(int(r.get('num_units',r.get('num_cpus','0'))) for r in living.values())
        trials=[]
        for inp in inputs:
            file=base/'results'/'core'/f"{label}-input{inp['input_id']}.dat"
            rows=detail(file, expected_fields=columns) if living else []
            byid={r['id']:r for r in rows}
            if len(byid)!=len(rows) or set(byid)!=set(living):
                raise ValueError(f'{file}: incomplete or duplicate living ID set')
            for ident,r in byid.items():
                if r['sequence'] != living[ident]['sequence']:
                    raise ValueError(f'{file}: sequence identity changed')
                if int(r['num_units'])!=int(living[ident].get('num_units',living[ident].get('num_cpus','0'))):
                    raise ValueError(f'{file}: abundance changed')
                for j in range(3):
                    if int(r[f'env_input.{j}'])!=int(inp[f'input{j}']):
                        raise ValueError(f'{file}: input mismatch')
            trials.append(byid)
        present=set()
        for task in tasks:
            col=f"task.{task['task_index']}"; name=task['name']
            any_n=all_n=raw_n=0
            for ident,source in living.items():
                n=int(source.get('num_units',source.get('num_cpus','0')))
                raw=[int(t[ident][col])>0 for t in trials]
                hits=[r and int(t[ident]['viable'])>0 for r,t in zip(raw,trials)]
                raw_n += n*any(raw); any_n += n*any(hits); all_n += n*all(hits)
            exposure=rewards.get(task['canonical'],'unknown')
            if exposure=='never': status='never_rewarded_full_record'
            elif exposure=='unknown': status='reward_history_unknown'
            else: status='rewarded_by_snapshot' if int(exposure)<=update else 'not_yet_rewarded'
            if all_n: present.add(name)
            panel.append(dict(label=label,update=update,task=name,task_kind=task.get('status','unknown'),canonical=task['canonical'],first_reward_update=exposure,
                              reward_status=status,population=total,raw_any=raw_n,viable_any=any_n,viable_all=all_n,
                              fraction_all=all_n/total if total else '',inputs=len(inputs)))
        sets.append(present)
        counts=defaultdict(int)
        for r in living.values(): counts[r['sequence']]+=int(r.get('num_units',r.get('num_cpus','0')))
        seqs=set(counts)
        h=-sum((n/total)*math.log(n/total) for n in counts.values()) if total else 0
        dynamics.append(dict(label=label,update=update,population=total,distinct_sequences=len(seqs),
            sequence_entropy_nats=h,sequence_arrivals=len(seqs-previous_seq),first_observed_sequences=len(seqs-seq_seen),
            core_names_present=len(present),first_observed_core_names=len(present-task_seen)))
        seq_seen |= seqs; task_seen |= present; previous_seq=seqs
    retention=[]
    for i,old in enumerate(sets):
        continuous=set(old)
        for j in range(i,len(sets)):
            continuous &= sets[j]; both=old & sets[j]
            retention.append(dict(from_label=snaps[i]['label'],to_label=snaps[j]['label'],baseline=len(old),
                endpoint_retained=len(both),endpoint_fraction=len(both)/len(old) if old else '',
                every_saved_snapshot=len(continuous),present_after_sampled_gap=len(both-continuous)))
    out=base/'summary'; out.mkdir(exist_ok=True)
    write(out/'capabilities.tsv',list(panel[0]),panel)
    write(out/'retention.tsv',list(retention[0]),retention)
    write(out/'snapshot_dynamics.tsv',list(dynamics[0]),dynamics)
    if a.rewards is None:
        write(out/'reward_history_template.tsv',['canonical','first_reward_update'],
              [dict(canonical=t['canonical'],first_reward_update='unknown') for t in tasks])
    print(out)

if __name__=='__main__': main()
```

### ancestry-helper.py

```python
#!/usr/bin/env python3
"""Extract recorded sequence-group origins within ONE uninterrupted Avida segment.

Call with snapshots in time order. A shared --segment label is the caller's
assertion, not an automatic check that IDs survived a restart. Recurrent births
can merge into an active group; this output is not individual-program genealogy.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path


def read_spop(path):
    columns = None
    for lineno, raw in enumerate(path.read_text().splitlines(), 1):
        line = raw.strip()
        if line.startswith("#format "):
            columns = line.split()[1:]
        elif line and not line.startswith("#"):
            if columns is None:
                raise ValueError(f"{path}:{lineno}: no #format header")
            row = dict(zip(columns, line.split()))
            try:
                if "parents" not in row and "parent_id" not in row:
                    raise ValueError("missing parents column")
                parents = row.get("parents", row.get("parent_id", ""))
                if parents in ("", "(none)", "-1"):
                    parent_ids = ()
                else:
                    parent_ids = tuple(int(x) for x in parents.split(","))
                record = dict(id=int(row["id"]), parents=parent_ids,
                              depth=int(row["depth"]),
                              update_born=int(row["update_born"]),
                              sequence=row["sequence"],
                              num_units=int(row.get("num_units", row.get("num_cpus", "-1"))))
                if record["num_units"] < 0:
                    raise ValueError("missing/negative living count")
                record["hw_type"] = row.get("hw_type", "")
                record["inst_set"] = row.get("inst_set", "")
                yield record
            except (KeyError, ValueError) as exc:
                raise ValueError(f"{path}:{lineno}: invalid record: {exc}") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--segment", required=True, help="one uninterrupted process label")
    parser.add_argument("--target", required=True, type=int)
    parser.add_argument("--output", type=Path, default=Path("selected-lineage.spop"))
    parser.add_argument("snapshots", nargs="+", type=Path, help="same-segment files in time order")
    args = parser.parse_args()
    records, provenance = {}, []
    identity = ("parents", "depth", "update_born", "sequence", "hw_type", "inst_set")
    for path in args.snapshots:
        provenance.append(dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        for record in read_spop(path):
            old = records.get(record["id"])
            if old and any(old[k] != record[k] for k in identity):
                raise ValueError(f"ID {record['id']}: conflicting identity across supplied snapshots")
            records[record["id"]] = record  # abundance comes from its last supplied record
    lineage, seen, current = [], set(), args.target
    while current is not None:
        if current in seen:
            raise ValueError(f"cycle at ID {current}")
        if current not in records:
            raise ValueError(f"missing target or parent ID {current}")
        seen.add(current)
        record = records[current]
        lineage.append(record)
        if len(record["parents"]) > 1:
            raise ValueError(f"ID {current}: multiple parents; this helper requires asexual paths")
        current = record["parents"][0] if record["parents"] else None
    lineage.reverse()
    if lineage[0]["depth"] != 0:
        raise ValueError("root has nonzero depth: path is truncated despite an empty parents field")
    for parent, child in zip(lineage, lineage[1:]):
        if child["depth"] != parent["depth"] + 1:
            raise ValueError(f"depth mismatch at edge {parent['id']} -> {child['id']}")
        if child["update_born"] < parent["update_born"]:
            raise ValueError(f"birth-update reversal at ID {child['id']}")
    fields = ("id", "parents", "depth", "update_born", "sequence", "num_units")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as out:
        out.write("#filetype genotype_data\n#format " + " ".join(fields) + "\n")
        out.write("# Recorded group-origin path; counts are last supplied observations.\n")
        for record in lineage:
            row = dict(record, parents=",".join(map(str, record["parents"])) or "(none)")
            out.write(" ".join(str(row[k]) for k in fields) + "\n")
    edges = args.output.with_suffix(".edges.tsv")
    with edges.open("w", newline="") as out:
        writer = csv.writer(out, delimiter="\t")
        writer.writerow(("parent_id", "child_id", "parent_update", "child_update", "parent_sequence", "child_sequence"))
        for parent, child in zip(lineage, lineage[1:]):
            writer.writerow((parent["id"], child["id"], parent["update_born"], child["update_born"], parent["sequence"], child["sequence"]))
    audit = dict(segment=args.segment, inputs=provenance, target=args.target,
                 ids_root_to_target=[r["id"] for r in lineage],
                 meaning="recorded group origins; active matching sequences can merge independent births",
                 counts="last supplied record per group; not a single contemporaneous population",
                 hardware="minimal output assumes the matching single instruction set in analyze config")
    args.output.with_suffix(".audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(f"Wrote {len(lineage)} group records to {args.output}; edges to {edges}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc))
```

### map_lineage.py

```python
#!/usr/bin/env python3
"""Run stock lineage recalculation and null maps using a generated suite.
Only one continuous, checked asexual path from ancestry-helper.py is accepted.
Outputs do not determine instruction homology. --graded supplies a separate
nine-task-reward reference assay for fitness complexity, keeping task indices.
"""
import argparse, csv, json, re, subprocess
from pathlib import Path

def rows(p):
    with open(p,newline='') as f: return list(csv.DictReader(f,delimiter='\t'))

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--suite',type=Path,required=True)
    p.add_argument('--lineage',type=Path,required=True)
    p.add_argument('--target',type=int,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--graded',action='store_true')
    p.add_argument('--run',action='store_true')
    a=p.parse_args();suite=a.suite.resolve();lineage=a.lineage.resolve();out=a.out.resolve()
    if any(re.search(r'\s|[#$]',str(x)) for x in (suite,lineage,out)):
        p.error('Use paths without spaces, # or $')
    if not lineage.is_file():p.error('Missing lineage')
    out.mkdir(parents=True,exist_ok=False);(out/'data').mkdir()
    tasks=[r for r in rows(suite/'tasks.tsv') if r['profile']=='core']
    inputs=[r for r in rows(suite/'inputs.tsv') if r['profile']=='core']
    tasks.sort(key=lambda r:int(r['task_index']))
    fields='viable fitness gest_time env_input.0 env_input.1 env_input.2 '+ ' '.join('task.'+r['task_index'] for r in tasks)
    text=(suite/'core/environment.cfg').read_text()
    if a.graded:
        power=dict(not_=1,nand=1,and_=2,orn=2,or_=3,andn=3,nor=4,xor=4,equ=5)
        power={k.rstrip('_'):v for k,v in power.items()}
        for r in tasks:
            if r['name'] in power:
                old=f"REACTION P{int(r['task_index']):03d} {r['name']} process:value=0:type=pow"
                new=old.replace('value=0:',f"value={power[r['name']]}:")
                if text.count(old)!=1: raise ValueError('Reference reaction not unique')
                text=text.replace(old,new)
    (out/'environment.cfg').write_text(text)
    lines=['PURGE_BATCH',f'LOAD {lineage}',f'FIND_LINEAGE {a.target}','NAME_BATCH reuse']
    first=inputs[0];triple=' '.join(first[f'input{j}'] for j in range(3))
    lines += ['RECALCULATE 0 -1 0 '+triple,'ALIGN',
              'DETAIL lineage-sequences.dat id parent_id depth update_born sequence alignment']
    manifest=[]
    for r in inputs:
        directory=out/'data'/('I'+r['input_id']);directory.mkdir()
        triple=' '.join(r[f'input{j}'] for j in range(3))
        lines.append(f'MAP_TASKS {directory}/ text use_manual_inputs {triple} {fields}')
        manifest.append({**{k:v for k,v in r.items() if k!='profile'},'directory':str(directory)})
    lines+=['FILTER depth > 0','DETAIL lineage-edges.dat id parent_id depth update_born parent_dist parent_muts']
    (out/'analyze.cfg').write_text('\n'.join(lines)+'\n')
    with (out/'maps.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,list(manifest[0]),delimiter='\t');w.writeheader();w.writerows(manifest)
    command=next(r for r in json.loads((suite/'commands.json').read_text()) if r['profile']=='core')
    cmd=list(command['command'])
    for key,val in [('ANALYZE_FILE',out/'analyze.cfg'),('ENVIRONMENT_FILE',out/'environment.cfg'),('DATA_DIR',out/'data')]:
        indexes=[i for i,t in enumerate(cmd) if t==key and i and cmd[i-1]=='-set']
        if len(indexes)!=1: raise ValueError('Ambiguous original command')
        cmd[indexes[0]+1]=str(val)
    (out/'command.json').write_text(json.dumps(dict(cwd=command['cwd'],command=cmd,graded=a.graded),indent=2)+'\n')
    (out/'task_indices.txt').write_text(' '.join(r['task_index'] for r in tasks)+'\n')
    if a.run:
        with (out/'run.log').open('w') as log:
            r=subprocess.run(cmd,cwd=command['cwd'],stdout=log,stderr=subprocess.STDOUT)
        if r.returncode: raise SystemExit(f'Avida exited {r.returncode}; retain run.log')
    print(out)

if __name__=='__main__':main()
```

### summarize_maps.py

```python
#!/usr/bin/env python3
"""Summarize stock MAP_TASKS outputs; no sequence execution or homology inference.

MAP_TASKS must request columns in this exact order:
viable fitness gest_time env_input.0 env_input.1 env_input.2 task.N ...
The final task columns must match --tasks in order.
maps.tsv: input_id, input0, input1, input2, directory (tab separated).
Optional matches.tsv: ancestor_id, ancestor_site, ancestor_task, descendant_id,
descendant_site, descendant_task, basis. Sites are one based; basis records the
user-supplied positional reconstruction. Overlap remains conditional on it.
Fitness summaries compare printed fitness values, include viability-losing
ablations, and apply no persistence filter. Rounding can hide small differences.
The positional skeleton uses '_' as an output placeholder; it is not executable.
"""
import argparse
import csv
import math
from collections import Counter, defaultdict
from pathlib import Path


def read_tsv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_tsv(path, rows):
    if not rows:
        return
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, list(rows[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def phenotype(words, task_ids, inputs, where):
    if len(words) != 6 + len(task_ids):
        raise ValueError(f"{where}: wrong width; check MAP_TASKS column order")
    viable, gestation = int(words[0]), int(words[2])
    fitness = float(words[1])
    counts = [int(x) for x in words[6:]]
    if viable not in (0, 1) or not math.isfinite(fitness) or min(counts) < 0:
        raise ValueError(f"{where}: invalid phenotype values")
    if tuple(map(int, words[3:6])) != inputs:
        raise ValueError(f"{where}: actual input values differ from maps.tsv")
    return viable, fitness, gestation, dict(zip(task_ids, counts))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--tasks", nargs="+", required=True, type=int)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--matches", type=Path)
    args = parser.parse_args()
    if min(args.tasks) < 0 or len(set(args.tasks)) != len(args.tasks):
        raise ValueError("Task indices must be distinct and nonnegative")
    manifests = read_tsv(args.manifest)
    if not manifests or len({r["input_id"] for r in manifests}) != len(manifests):
        raise ValueError("Need nonempty maps.tsv with distinct input_id values")
    sites, summaries, fitness_rows, lookup = [], [], [], {}
    signatures = {}
    expected_ids = None
    for m in manifests:
        input_id = m["input_id"]
        inputs = tuple(int(m[f"input{i}"]) for i in range(3))
        directory = Path(m["directory"])
        if not directory.is_absolute():
            directory = args.manifest.resolve().parent / directory
        files = sorted(directory.glob("tasksites.*.dat"))
        if not files:
            raise ValueError(f"{directory}: no MAP_TASKS files")
        seen_ids = set()
        for path in files:
            rows = [line.split() for line in path.read_text().splitlines()
                    if line.strip() and not line.lstrip().startswith("#")]
            if not rows or len(rows[0]) < 3 or rows[0][0] != "-1":
                raise ValueError(f"{path}: missing baseline row")
            ident = int(rows[0][2])
            if ident in seen_ids:
                raise ValueError(f"{path}: duplicate ID within one input")
            seen_ids.add(ident)
            base = phenotype(rows[0][3:], args.tasks, inputs, str(path))
            if not rows[1:] or [int(r[0]) for r in rows[1:]] != list(range(1, len(rows))):
                raise ValueError(f"{path}: noncontiguous or missing site rows")
            signature = tuple((r[1], r[2]) for r in rows[1:])
            if ident in signatures and signatures[ident] != signature:
                raise ValueError(f"{path}: source instructions changed between inputs")
            signatures[ident] = signature
            tallies = {task: Counter() for task in args.tasks}
            fitness_sites = []
            skeleton = []
            for raw in rows[1:]:
                site = int(raw[0])
                mutant = phenotype(raw[3:], args.tasks, inputs, f"{path}:{site}")
                decreases = bool(base[0] and mutant[1] < base[1])
                if decreases:
                    fitness_sites.append(site)
                skeleton.append(raw[1] if decreases else "_")
                for task in args.tasks:
                    baseline_count, mutant_count = base[3][task], mutant[3][task]
                    if not base[0]:
                        status = "baseline_ineligible"
                    elif not baseline_count:
                        status = "baseline_task_absent"
                    elif not mutant[0]:
                        status = "viability_confounded"
                    elif not mutant_count:
                        status = "required"
                    else:
                        status = "task_preserved"
                    record = dict(input_id=input_id, id=ident, site=site, task=task,
                        original_symbol=raw[1], original_instruction=raw[2],
                        baseline_viable=base[0], baseline_task_count=baseline_count,
                        baseline_fitness=base[1], baseline_gest_time=base[2],
                        mutant_viable=mutant[0], mutant_task_count=mutant_count,
                        mutant_fitness=mutant[1], mutant_gest_time=mutant[2], status=status,
                        neutral_for_task=int(status == "task_preserved"),
                        fitness_unchanged=int(base[1] == mutant[1]),
                        count_unchanged=int(baseline_count == mutant_count))
                    sites.append(record)
                    lookup[(input_id, ident, site, task)] = record
                    tallies[task][status] += 1
            for task in args.tasks:
                summary = dict(input_id=input_id, id=ident, task=task,
                    baseline_viable=base[0], baseline_task_count=base[3][task],
                    length=len(rows)-1)
                summary.update({name: tallies[task][name] for name in
                    ("required", "task_preserved", "viability_confounded",
                     "baseline_ineligible", "baseline_task_absent")})
                summaries.append(summary)
            fitness_rows.append(dict(input_id=input_id, id=ident,
                baseline_viable=base[0], baseline_fitness=base[1], length=len(rows)-1,
                fitness_required_sites=len(fitness_sites) if base[0] else "",
                required_positions=";".join(map(str, fitness_sites)) if base[0] else "",
                ordered_required_symbols="".join(symbol for symbol in skeleton if symbol != "_") if base[0] else "",
                positional_skeleton="".join(skeleton) if base[0] else ""))
        if expected_ids is not None and seen_ids != expected_ids:
            raise ValueError("Different sequence-ID sets between input panels")
        expected_ids = seen_ids
    grouped = defaultdict(list)
    for row in sites:
        grouped[(row["id"], row["site"], row["task"])].append(row)
    across = [dict(id=k[0], site=k[1], task=k[2], inputs=len(rows),
        baseline_eligible_all=int(all(r["baseline_viable"] and r["baseline_task_count"] for r in rows)),
        required_all=int(all(r["status"] == "required" for r in rows)),
        task_preserved_all=int(all(r["status"] == "task_preserved" for r in rows)),
        viability_confounded_any=int(any(r["status"] == "viability_confounded" for r in rows)))
        for k, rows in grouped.items()]
    overlaps = []
    if args.matches:
        for n, match in enumerate(read_tsv(args.matches)):
            if not match["basis"].strip():
                raise ValueError("Each matched position requires a reconstruction basis")
            for m in manifests:
                inp = m["input_id"]
                old = lookup[(inp, int(match["ancestor_id"]), int(match["ancestor_site"]), int(match["ancestor_task"]))]
                new = lookup[(inp, int(match["descendant_id"]), int(match["descendant_site"]), int(match["descendant_task"]))]
                overlaps.append(dict(match=n, input_id=inp, **match,
                    ancestor_status=old["status"], descendant_status=new["status"],
                    endpoint_symbols_equal=int(old["original_symbol"] == new["original_symbol"]),
                    shared_dependence_conditional=int(old["status"] == new["status"] == "required")))
    args.out.mkdir(parents=True, exist_ok=True)
    write_tsv(args.out / "sites.tsv", sites)
    write_tsv(args.out / "summary.tsv", summaries)
    write_tsv(args.out / "sites_all_inputs.tsv", across)
    write_tsv(args.out / "conditional_overlap.tsv", overlaps)
    write_tsv(args.out / "fitness_sites.tsv", fitness_rows)
    fitness_summary = []
    for m in manifests:
        eligible = [row for row in fitness_rows if row["input_id"] == m["input_id"] and row["baseline_viable"]]
        fitness_summary.append(dict(input_id=m["input_id"], viable_baselines=len(eligible),
            max_fitness_required_sites=max((row["fitness_required_sites"] for row in eligible), default="")))
    write_tsv(args.out / "fitness_summary.tsv", fitness_summary)
    print(args.out)


if __name__ == "__main__":
    main()
```

### group_ablation.py

```python
#!/usr/bin/env python3
"""python group_ablation.py selected-lineage.spop groups.csv group-analyze.cfg 0 8 --inputs suite/inputs.tsv"""
import csv
import json
import argparse
import re
import sys
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('population',type=Path)
parser.add_argument('groupfile',type=Path)
parser.add_argument('outfile',type=Path)
parser.add_argument('task_ids',nargs='+',type=int)
parser.add_argument('--inputs',type=Path,required=True,help='Suite inputs.tsv; core profile only')
args=parser.parse_args()
population, groupfile, outfile=args.population,args.groupfile,args.outfile
task_ids=list(dict.fromkeys(args.task_ids))
with args.inputs.open(newline='') as f:
    triples=[tuple(int(r['input'+str(i)]) for i in range(3)) for r in csv.DictReader(f,delimiter='\t') if r['profile']=='core']
if len(triples)<2 or len(set(triples))!=len(triples): raise SystemExit('Need distinct core triples')
if not task_ids or min(task_ids) < 0:
    raise SystemExit("Supply nonnegative task indices from the assay manifest")
columns = None
sequences = {}
for line in population.read_text().splitlines():
    if line.startswith("#format "):
        columns = line.split()[1:]
    elif line.strip() and not line.lstrip().startswith("#"):
        if columns is None:
            raise SystemExit("Missing #format header")
        fields = line.split()
        if len(fields) != len(columns):
            raise SystemExit("Malformed population row")
        row = dict(zip(columns, fields))
        seq = row["sequence"]
        if re.fullmatch("[a-z]+", seq) is None:
            raise SystemExit("Expected unchanged 26-instruction heads sequences")
        ident = int(row["id"])
        if ident in sequences:
            raise SystemExit("Duplicate sequence ID: use one segment")
        sequences[ident] = seq
groups = []
with groupfile.open(newline="") as handle:
    for row in csv.DictReader(handle):
        ident = int(row["id"])
        sites = sorted(set(int(x) for x in row["sites"].split(";")))
        seq = sequences[ident]
        if not sites or sites[0] < 1 or sites[-1] > len(seq):
            raise SystemExit("Group has an out-of-range site")
        groups.append((ident, sites))
if not groups:
    raise SystemExit("No groups specified")
lines = ["PURGE_BATCH", "NAME_BATCH activate_null",
         f"LOAD_SEQUENCE {sequences[groups[0][0]]} initialize_null",
         "MAP_TASKS group-null-init/ text use_manual_inputs 15 51 85 viable",
         "PURGE_BATCH", "NAME_BATCH selected_groups"]
for ident in sorted({g[0] for g in groups}):
    lines.append(f"LOAD_SEQUENCE {sequences[ident]} base_{ident}")
for number, (ident, sites) in enumerate(groups):
    mutant = list(sequences[ident])
    for site in sites:
        mutant[site - 1] = "A"
    name = f"group_{number}_id_{ident}_sites_" + "_".join(map(str, sites))
    lines.append(f"LOAD_SEQUENCE {''.join(mutant)} {name}")
fields = "name viable fitness gest_time " + " ".join(f"task.{t}" for t in task_ids)
for k, triple in enumerate(triples):
    lines.append("RECALCULATE 0 -1 0 " + " ".join(map(str, triple)))
    lines.append(f"DETAIL reuse-groups-I{k}.dat {fields}")
outfile.write_text("\n".join(lines) + "\n")

outfile.with_suffix(".columns.json").write_text(json.dumps(fields.split(),indent=2)+"\n")
```

### dynamics_metrics.py

```python
#!/usr/bin/env python3
"""Raw sampled sequence dynamics from stock Avida .spop files.

Usage: python3 dynamics_metrics.py snapshots.csv dynamics.csv --band-low 2 --band-high 4
snapshots.csv columns: update,path (paths relative to that CSV).
These are raw sampled statistics, not normalized evolutionary activity or MODES.
For a sequence g, a_g is its number of observed snapshots, including the current
one. Optional band activity is sum(a_g for current g with low <= a_g <= high)
divided by the number of current sequences. Its units are observed snapshots.
"""
import argparse
import csv
import math
from collections import Counter
from pathlib import Path


def living_counts(path):
    counts = Counter()
    columns = None
    with path.open() as stream:
        for line_no, line in enumerate(stream, 1):
            line = line.strip()
            if not line:
                continue
            if line.startswith("#format "):
                columns = line.split()[1:]
                continue
            if line.startswith("#"):
                continue
            if columns is None:
                raise ValueError(f"{path}:{line_no}: missing #format header")
            values = line.split()
            # Historical rows omit per-cell trailing fields in stock saves.
            if len(values) > len(columns):
                raise ValueError(f"{path}:{line_no}: too many fields")
            row = dict(zip(columns, values))
            abundance_name = "num_units" if "num_units" in row else "num_cpus"
            if abundance_name not in row:
                raise ValueError(f"{path}:{line_no}: missing abundance")
            abundance = int(row[abundance_name])
            if abundance < 0:
                raise ValueError(f"{path}:{line_no}: negative abundance")
            if abundance:
                key = (row["hw_type"], row["inst_set"], row["sequence"])
                counts[key] += abundance
    return counts


def main(manifest_name, output_name, band_low=None, band_high=None):
    if (band_low is None) != (band_high is None):
        raise ValueError("Supply both --band-low and --band-high, or neither")
    if band_low is not None and not (1 <= band_low <= band_high):
        raise ValueError("Activity band must satisfy 1 <= low <= high")
    manifest = Path(manifest_name)
    with manifest.open(newline="") as stream:
        snapshots = [(int(row["update"]), manifest.parent / row["path"])
                     for row in csv.DictReader(stream)]
    if not snapshots:
        raise ValueError("The snapshot manifest is empty")
    if any(b[0] <= a[0] for a, b in zip(snapshots, snapshots[1:])):
        raise ValueError("Global update values must be strictly increasing")
    seen = set()
    previous = None
    observations = Counter()
    columns = ["update", "program_count", "distinct_sequences", "raw_additions",
               "raw_losses", "raw_first_observations", "raw_sequence_entropy_bits",
               "mean_observed_presence_snapshots", "band_low_snapshots",
               "band_high_snapshots", "raw_band_activity_snapshots"]
    with Path(output_name).open("w", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns)
        writer.writeheader()
        for update, path in snapshots:
            counts = living_counts(path)
            current = set(counts)
            total = sum(counts.values())
            observations.update(current)
            entropy = -sum((n / total) * math.log2(n / total) for n in counts.values()) if total else 0.0
            writer.writerow({
                "update": update,
                "program_count": total,
                "distinct_sequences": len(current),
                "raw_additions": len(current - previous) if previous is not None else "",
                "raw_losses": len(previous - current) if previous is not None else "",
                "raw_first_observations": len(current - seen) if previous is not None else "",
                "raw_sequence_entropy_bits": entropy,
                "mean_observed_presence_snapshots": sum(observations[g] for g in current) / len(current) if current else "",
                "band_low_snapshots": band_low if band_low is not None else "",
                "band_high_snapshots": band_high if band_high is not None else "",
                "raw_band_activity_snapshots": sum(observations[g] for g in current
                    if band_low <= observations[g] <= band_high) / len(current)
                    if current and band_low is not None else "",
            })
            seen.update(current)
            previous = current


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest")
    parser.add_argument("output")
    parser.add_argument("--band-low", type=int)
    parser.add_argument("--band-high", type=int)
    args = parser.parse_args()
    main(args.manifest, args.output, args.band_low, args.band_high)
```

END OF REPORT
