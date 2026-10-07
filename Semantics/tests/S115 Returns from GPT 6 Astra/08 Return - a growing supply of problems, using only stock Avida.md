# A growing supply of problems using stock Avida

## 1. Summary for the owner

Imagine workshops that turn their used material into supplies for other workshops. Their activity changes which jobs can earn a payment, without anyone announcing the next job.

Two proposed Avida execution environments implement versions of that idea. In **A, a shared market**, NOT and NAND performances produce a resource that can make seven other tasks payable. In **B, reciprocal exchange**, two groups of tasks transfer resources between two pools; their activity can close and reopen payment opportunities. Neither schedules advancement through a ranked task list. The designer still chooses the tasks, their connections and the payment rules. A explicitly retains a selected entry tier of two tasks before seven downstream tasks.

**Checked source and measured short checks:** I compiled the specified Avida commit without changing its source. Both configurations loaded and ran. Controlled programs produced resources and crossed payment thresholds as described below. These checks do not measure the proposed evolutionary outcomes; no 50,000-update treatment was run here.

The question is whether these population-dependent opportunities produce additional, retained computational capabilities. The report specifies measurements that could count against that prediction. These designs rearrange opportunities within a finite menu; they do not create new task definitions or promise an indefinitely growing supply of problems.

## 2. The designs

### Common mechanism and settings

**Proposal.** Run each design continuously for 50,000 updates, with three matched seeds, the supplied ancestor, 60 × 60 cells, copy error probability 0.0075 and division insertion/deletion probabilities 0.05 each. Preserve the baseline instruction set, placement, scheduling and replication settings. Appendix A supplies changes; each design has its complete environment and events files below. After the initial injection, scheduled events only record observations and stop the run.

**Checked source.** For an exact logic task, Avida calculates consumption from the available resource, `frac`, `max` and `min`; below the minimum it skips the process. A successful `pow` process multiplies the task bonus by `2^(consumed × value)`. A product adds `consumed × conversion` to its named resource. These are task-bonus multipliers, not guaranteed multipliers of Avida fitness.

**Checked source.** `reaction_max_count=1` allows one paid occurrence of that named reaction between division resets. An unpaid task attempt does not use that allowance. In contrast, `max_count=1` can use the task allowance even when its resource is empty. The rewarded reactions therefore use the reaction cap. The 68 three-input tasks have separate zero-reward monitors. Those monitors still record reactions; never classify every recorded reaction as a payment.

**Definition.** A task is *resource-payable* if a fresh valid performance, with an unused reaction allowance, could receive a positive reward at the current resource stock. An actual program must also perform the computation. Stocks refer to the whole shared pool. Availability during one output can also reflect consumption by earlier matching reactions in that output.

### A. Work opens a shared market

**Everyday example.** Two workshops produce offcuts; seven other kinds of work become worthwhile when enough offcuts accumulate.

**Proposal, step by step.**

1. `feed` starts with 3,600 units and receives external inflow 360. `market` starts empty and has no external inflow. Both have outflow 0.1.
2. A paid NOT or NAND performance consumes feed and produces the same quantity of market resource.
3. AND, ORN, OR, ANDN, NOR, XOR and EQU consume market resource. They produce nothing.
4. Each successful process consumes at most one unit. `frac=0.001` and `min=0.01` give a market eligibility threshold of 10 units. Below that threshold, its seven tasks cannot pay. All seven become eligible together at or above it; no difficulty ladder orders them.
5. Consumption and outflow can close that gate. Further production can reopen it. The producer and consumer may be the same Avida program.

**Checked source-derived consequences.** For an eligible exact task, consumption is `min(1, 0.001 × available)`, set to zero if below 0.01. Payment ranges from `2^0.01` to 2. Resource production is applied after the current output evaluation, so it is available to later outputs, not retroactively within that evaluation.

**Designer choices.** NOT/NAND are selected entry tasks, creating a two-tier dependency. The seven recipients, equal payment coefficients, threshold, supply and decay are also choices. This meets population-dependent release without a pre-ranked difficulty list; it does not remove designer-specified dependencies. If market stock crosses 10 once and stays above it, the result is one expansion followed by changing payment amounts, not continuing expansion.

**New capability and probes.** Count first appearance and subsequent retention of each capability using the common 85-task assay in section 3. Record a newly payable task separately from a newly performed task. All 68 three-input logic tasks and the eight arithmetic probes remain unrewarded in this treatment; their assay scores measure capabilities absent from its reward menu.

**Prediction and contrary result.** Population production should precede downstream eligibility. Removing production should leave the market empty and prevent downstream payments. A separate evolutionary hypothesis is that downstream exposure accompanies acquisition and retention of previously absent capabilities. No downstream acquisition by update 50,000, or repeated replacement without the retention defined below, counts against that design purpose under these settings. Report the fraction of resource samples that were eligible and elapsed updates since first observed opening alongside that outcome; do not add an exposure exemption afterwards. Acquisition before eligibility would indicate incidental capability, not reward-driven acquisition at that time.

**Comparison and cost.** Use the common baseline and assays. The existing fixed, growing-list and scarcity runs provide treatment comparisons; continuous controls are needed to separate environment effects from restart effects. Three seeds cost approximately **3 × kA CPU-hours**, where `kA` is its measured runtime relative to the brief's one-hour baseline. The estimate is planning arithmetic, not a timing measurement.

### B. Reciprocal exchange between two pools

**Everyday example.** Two groups of workshops exchange containers. When one group uses many containers, it sends supplies to the other group and temporarily exhausts its own supply.

**Proposal, step by step.** Both pools start at 1,800, each receives inflow 180, and both have outflow 0.1. The assignment is:

| Task group | Consumes | Produces |
|---|---|---|
| NOT, OR, ANDN, XOR | left | right |
| NAND, AND, ORN, NOR, EQU | right | left |

Each paid performance transfers 100 units. `max=100:min=100:frac=0.1:value=0.01` means a pool needs at least 1,000 units, and a paid occurrence multiplies the task bonus by 2. Both groups are initially resource-payable. Relative task activity changes the distribution of material, making a group temporarily ineligible while supplying the other group. External replenishment can also reopen a gate; opening by itself does not imply reciprocal activity.

**Checked source-derived consequences.** Each reaction conserves the sum of the two pools while changing their distribution. Inflow and outflow change the sum. A payment at stock 1,000 leaves 900. With no opposite-side production, the stated flow restores 1,000 after approximately 1.253 updates. This is a calculation from Avida's resource integration, not an evolutionary measurement. Counterflow can reopen the gate sooner.

**Designer choices.** The four/five partition is not a difficulty ranking; nevertheless, task identities matter and five versus four supplies unequal maximum transfers for a program performing all nine. The 100-unit packet was selected after source arithmetic showed that a one-unit packet could close a gate for only about 0.0134 update. This changes the resource feedback, not merely the logging resolution. Thresholds, packet size and task grouping remain free parameters, not discovered laws.

**New capability and probes.** Apply the same acquisition/retention assay and the same 68 logic plus eight arithmetic unrewarded probes as A. Also ask whether new capabilities occur on the side receiving population-produced resources. Measure both roles within each instruction sequence; population-level exchange need not involve distinct sequences or division of work.

**Prediction and contrary result.** Sufficiently uneven task activity should redistribute stock and close payment gates. In a matched control, send each product back into the pool it consumed: net stock change per reaction becomes zero. A gate closing in that control under the stated flows would count against the implementation account. If treatment runs never show closed gates, the proposed changing opportunity set has not been demonstrated by those observations. If gates change but capabilities do not accumulate or persist, the evolutionary hypothesis has not received support.

**Comparison and cost.** Compare especially with the existing scarcity environment, plus B's same-pool-return control. The control retains the supply budget, reaction cap and twofold payments. Its pools remain above the eligibility threshold, making it a continuous fixed equal-reward nine-task reference. Three treatment seeds cost approximately **3 × kB CPU-hours**; the three control seeds have their own measured runtime factor.

## 3. How they would be compared with the six running environments

### Preserve the comparison and distinguish its questions

**Given in the brief, not reproduced here:** the six existing treatments use 1,000-update segments with population reloads. Their exact seed values and baseline files were not attached. Use those original seeds and files; do not substitute arbitrary seed values or assume an unlisted setting matches. Keep the same initial injection as well as the same ancestor.

**Checked source.** A saved population is not a running-state checkpoint. Loading constructs fresh execution state and can apply a gestation-based merit correction. It does not restore the original CPU state or resource pools. The proposed runs save snapshots but never reload them into the evolving process. Ordinary division resets remain part of the baseline.

Compare all eight treatments descriptively. For causal comparison, add continuous versions of fixed graded, EQU-only, no rewards, scarcity, and fixed 77. Keep growing-list results identified as the segmented adaptive protocol until its separately running restart check resolves what can be compared. Use each original task/reward configuration unchanged in its continuous reference. Record updates, divisions and executed-instruction exposure: equal update budgets do not imply equal replication opportunities.

Equal reward coefficients are another deliberate difference: these designs permit at most a twofold multiplier per trained task. B's same-pool-return reference separates its feedback from that reward scale. A's production-removal control tests its gate, but also removes downstream reward supply; it cannot alone attribute capability differences to feedback rather than reward exposure. Do not make that causal attribution from the six original treatments either.

### Capability and payment measurements

**Checked source.** The appendix's neutral assay declares 77 logic tasks plus eight arithmetic tasks: `2X`, `X−5`, `−X`, `X/4`, `X+Y`, `X−Y`, `X+Y+Z`, and `−X−Y−Z`. All processes have reward value zero and no resource requirements. Its task-ID order is fixed by the supplied file.

Use a separate analyze process on each snapshot. Appendix D runs eight specified input triples, one cold evaluation per triple, for every saved distinct instruction sequence. Each triple contains all eight three-input bit combinations in its low eight bits. The bounded numbers avoid overflow in the selected arithmetic checker expressions. They do not constrain arbitrary intermediate program arithmetic.

**Checked source.** Separate single-trial `RECALCULATE` calls preserve those manual inputs. Multiple-trial recalculation follows different random-input/modal-phenotype behavior, so do not replace them with a single eight-trial call. The output records sequence ID, population count, viability, length, gestation, inputs and every task count. Stock column descriptions mislabel the three input columns; use the explicit output order.

**Proposed scoring.** For each sequence/task, retain its complete eight-element success vector and replication vector. Report both any-panel performance and performance on all eight panels with replication on all eight. Count unique tasks and population-count-weighted prevalence separately; several specialists can give the population a repertoire no individual sequence has. A capability is new only relative to earlier snapshots under the same assay. First detection is bounded by snapshot spacing, not an exact discovery time.

Build a retention matrix with snapshots as rows and fixed task/panel pairs as columns. Keep “ever seen,” “currently present” and “retained at later snapshots” separate. Before running, define retained acquisition as detection of an all-eight-panel replicating performer at each of the next five 1,000-update snapshots after first detection. Late gains lacking five subsequent snapshots are unassessable for that endpoint, not losses. Report prevalence and the full retention matrix as well. Evaluate the ancestor under the identical assay. These finite-panel and retention-window choices are operational measures, not claims about every input or indefinite persistence.

Keep an arm-by-task reward-history table. Three-input tasks are unrewarded in A/B but rewarded in fixed 77 and potentially in growing-list. Only the arithmetic subset is a common never-rewarded battery across all treatments described in the brief. A task that is temporarily gated off, or previously rewarded in an ancestor, is not never rewarded.

**Checked source.** Native task/reaction counts describe recent completed-cycle phenotypes of living programs; `PrintTasksExeData` and `PrintReactionExeData` are not cumulative resource-flux counters. Do not sum their rows to estimate product creation. Restrict payment observations to the nine trained reactions. Resource logs give stocks, not an exact history of every gate crossing. The supplied one-update stock log can miss within-update closures; observed closures are a lower bound. Use the cold assay for latent capabilities, not native reward-dependent recognition alone.

For claims of reuse, select a lineage with an assay gain, inspect parent and descendant under the same panels, and ablate the proposed shared instructions. Compare with nearby removable instructions. Ancestry membership or co-occurring tasks alone does not identify reused computation. Final historic snapshots contain retained ancestry, not every extinct side branch.

### Discriminating checks and compute budget

**Measured here.** Nine live checks of 100 updates each completed: two stock-ancestor configuration checks and seven controlled mechanism checks. Controlled tests disabled instruction changes and used hand-constructed task performers; these are not evolved solutions.

| Check | Observed result |
|---|---|
| A, AND performer, market held initially at 9 or 10 with no market flow | At 9: no paid AND, stock stayed 9. At 10: paid AND, stock became 9.99. |
| A, NOT/AND performer, normal products versus conversion zero | Normal products: market reached 47.7504 at update 100 and paid AND appeared. Conversion zero: market stayed zero and no paid AND appeared. |
| B, NOT performer, left initially 999 or 1,000 with left flow disabled | At 999: no paid NOT, stock stayed 999. At 1,000: paid NOT, stock became 900. |
| B, NOT performer, product returned to left, same 1,000-unit assay | Stock stayed 1,000 while paid NOT appeared. |

**Measured here.** The neutral probe check ran three controls across all eight panels: the default ancestor replicated with no detected tasks; a NOT control replicated and showed only NOT; a `2X` control replicated and showed only its arithmetic task. These 24 evaluations check basic assay behavior, not evolved-program generalization.

**Planning arithmetic from the brief.** At one CPU-hour per run: six new treatment runs ≈6 CPU-hours; five continuous references × three seeds ≈15; A's production-removal and B's same-pool-return controls × three seeds ≈6. The full stated comparison is therefore approximately **27 CPU-hours**, or about **nine elapsed hours at three simultaneous processes**, before probes and sensitivity runs. Runtime factors may differ substantially; do not treat this as a reservation or deadline. Every added three-seed arm costs approximately three baseline CPU-hours.

Measure each treatment's runtime on a fixed pilot before committing the full batch; retain the pilot's designation. Probe cost is `8 × N × t / 3600` CPU-hours, where N is the number of sequence evaluations across snapshots and t is measured seconds per sequence-panel test. Before deduplication, 51 snapshots × 3,600 occupied cells bounds N at 183,600 per run. All 85 tasks are checked together, not in 85 separate runs. Three seeds provide trajectories, not a precise distribution of outcomes. Full instruction-ablation costs require their own timing.

## 4. Source locations checked

**Checked source throughout this table:** [devosoft/avida, commit 47f13dadb547fcf10f620ace60247f38b30b8b16](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16), inspected as a local checkout. Paths below are relative to `avida-core/`. The checkout remained unchanged after compilation. Configuration numbers are proposed experimental choices; checking a parser does not determine an evolutionary outcome.

| Keywords or behavior used | File and function or definition |
|---|---|
| `RESOURCE`, `REACTION` | `source/main/cEnvironment.cc`: `LoadLine`, `LoadResource`, `LoadReaction` |
| `initial`, `inflow`, `outflow`, `geometry=global` | `cEnvironment.cc`: `LoadResource`; `source/main/cResource.cc`: `SetGeometry`; `source/main/cResourceCount.cc`: `Setup`, `DoUpdates`, `DoNonSpatialUpdates` |
| `process`, `resource`, `value`, `type=pow`, `max`, `min`, `frac`, `product`, `conversion` | `cEnvironment.cc`: `LoadReactionProcess`, `DoProcesses`; defaults in `source/main/cReactionProcess.h` |
| `requisite`, `max_count`, `reaction_max_count`; excluded `reaction`/`noreaction` | `cEnvironment.cc`: `LoadReactionRequisite`, `TestRequisites`, `TestOutput` |
| Logic and arithmetic task identifiers and outputs | `source/main/cTaskLib.cc`: `AddTask`; `Task_Not`, `Task_Nand`, `Task_And`, `Task_OrNot`, `Task_Or`, `Task_AndNot`, `Task_Nor`, `Task_Xor`, `Task_Equ`, `Task_Logic3in_AA` through `Task_Logic3in_CP`; `Task_Math1in_AA`, `Task_Math1in_AK`, `Task_Math1in_AL`, `Task_Math1in_AN`, `Task_Math2in_AN`, `Task_Math2in_AO`, `Task_Math3in_AH`, `Task_Math3in_AI` |
| Task counting, resource deltas, division resets | `source/main/cPhenotype.cc`: `TestOutput`, `DivideReset`; `source/main/cOrganism.cc`: `DoOutput`; `source/main/cPopulationInterface.cc`: `UpdateResources` |
| Shipped cascade | `support/config/misc/environment-cascade.cfg`: NOT/NAND source resources followed by product-dependent tasks; it supplies a designer-ordered cascade, which is not copied here |
| `u`, `begin`, interval `start:step:stop` | `source/main/cEventList.cc`: `AddEventFileFormat`, `Process` |
| `Inject` | `source/actions/PopulationActions.cc`: `cActionInject` constructor and `Process` |
| `PrintAverageData`, `PrintCountData`, `PrintTasksData`, `PrintTasksExeData`, `PrintReactionData`, `PrintReactionExeData`, `PrintTimeData` | `source/actions/PrintActions.cc`: `STATS_OUT_FILE` generates each named `cAction...::Process`; each calls the identically named `cStats` function in `source/main/cStats.cc` |
| `PrintResourceData resource.dat 0` | `source/actions/PrintActions.cc`: `cActionPrintResourceData` constructor and `Process`; `source/main/cStats.cc`: `PrintResourceData`; final argument disables spatial maps |
| Meaning of last-cycle counts | `source/main/cPopulation.cc`: `UpdateOrganismStats`; `cStats.cc`: `ProcessUpdate` |
| `SavePopulation`, `filename`, `save_historic`; reload limitation | `source/actions/SaveLoadActions.cc`: `cActionSavePopulation`, `cActionLoadPopulation`; `source/main/cPopulation.cc`: `SavePopulation`, `LoadPopulation`; `source/systematics/GenotypeArbiter.cc`: `LegacySave`, `PerformUpdate`, `removeGenotype` |
| `Exit` | `source/actions/DriverActions.cc`: `cActionExit::Process` |
| All `avida.cfg` entries below, instruction-set include | `source/main/cAvidaConfig.h`: named configuration definitions; `support/config/avida.cfg`, `support/config/instset-heads.cfg` |
| `-c`, `-a`, `-set` | `source/util/CmdLine.cc`: `ProcessCmdLineArgs`, `processArgs` |
| `CONFIG_SET`, `FORRANGE`, `PURGE_BATCH`, `LOAD`, `RECALCULATE`, `DETAIL`, `END` and output columns | `source/analyze/cAnalyze.cc`: `LoadCommandList`, `ConfigSet`, `CommandForRange`, `BatchPurge`, `LoadFile`, `BatchRecalculate`, `CommandDetail`, `SetupCommandDefLibrary`, `PreProcessArgs`; `source/analyze/cAnalyzeGenotype.cc`: `buildDataCommandManager`, `Recalculate`; `source/cpu/cTestCPU.cc`: `TestGenome`, `TestGenome_Body`, `ProcessGestation` |

## 5. Assumptions and what you are unsure of

**Frozen question for the hard-to-vary test.** Can these stock continuous environments make eligibility depend on program activity, and does that support acquisition and retention during 50,000 updates? The first claim is about implementation; the second remains an experimental hypothesis.

**Jobs.** Given: opportunities depend on population activity rather than scheduled advancement. Fixed: unmodified Avida, baseline ancestor/world/instruction changes, finite run budget. Given: count unrewarded capabilities and state designer choices. Added: use neutral assays and mechanism controls to separate eligibility, recognition and retained capability.

All parts below are **in test**. Their **dependency** is Avida's virtual CPU, task checkers and scheduling; interpreting capability retention as durable knowledge additionally borrows the owner's knowledge criterion, which this experiment does not assess. Provenance is stated separately from status. The prescribed ancestor, instruction meanings, world and instruction-change rates are **owner-fixed/outside the test**, **not assessed** as explanations, and **asserted in the brief**; their dependency is the supplied project record.

| Part | Status and what holds or leaves it open | Provenance |
|---|---|---|
| A's product route plus absent external market supply | Held jointly for producer-dependent market opening: product removal left the market empty in the controlled check | Built |
| B's cross-pool transfer plus finite stock gate | Held jointly for activity-dependent resource eligibility: threshold and same-pool-return checks separated their effects | Built |
| Initial stock and external inflow | Two routes to initial availability; sustained availability additionally depends on replenishment and consumption. Exact amounts remain loose | Built |
| Successful-reaction accounting and continuous execution | Held for retry after an unpaid attempt and avoiding extra reload resets. The exact cap of one remains loose | Built |
| Task identities, partition, coefficients, thresholds and packet size | Loose choices; named permutations or nearby values can implement the same general mechanism. Their evolutionary effects are unknown | Built |
| Neutral assay and eight-panel rule | Held if the added comparability job is accepted; controls distinguish capability from unavailable payment. Eight panels remain a finite, chosen sample | Built |
| Acquisition, retention and reuse caused by feedback | Unknown; requires the matched treatment trajectories and lineage interventions | Asserted hypothesis |

**Whole-explanation checks.** Remove/swap/poke — result: the measured product-off, threshold and return controls distinguish nearby cases; removing all producer routes blocks A's market. Flip — result: mechanism claims cannot accommodate payment below their resource threshold with all conditions fixed; evolutionary outcomes remain unsettled. Reverse — result for immediate directions; evolutionary feedback not settled: producer removal tests task-to-resource dependence; stock interventions test resource-to-payment dependence. Effects on later population task frequencies still require trajectories or interventions. Hidden answer — result: capability growth is not assumed in the definition of a payable task. Job origins — result: listed above; assay support is conditional on an added job.

Add a job — result: B also commits to conservation during each cross-transfer, unlike a model with net product creation; this follows from source arithmetic, while full trajectory accounting remains unsettled. Look inside — result for source mechanics; reuse not settled: source inspection and controlled outputs reach the mechanism; evolutionary reuse is unsettled. Pull — result: strong depletion can create unpayable opportunities while preventing acquisition; dense capability within one program can remove the need for exchange among different programs. Check patches — result: the 100-unit packet addresses short gate closures but changes feedback strength; it has not been fitted to evolutionary outcomes. No “other causes” bin rescues a failed prediction.

Change-list limits — result: task mapping, product routing, resource stock and packet size are testable; new task definitions, altered instruction meanings and unbounded progression are outside this claim. Rivals — not settled: fixed equal rewards, depletion without cross-feeding, and incidental capability from selection for replication remain alternatives; the specified controls and timing distinguish only parts of them. Provenance — result: built mechanisms and an asserted evolutionary hypothesis, with no evolutionary fitting performed here. These are results or explicitly unsettled checks; no whole test is omitted as inapplicable.

**Remaining limits.** The supplied historical measurements were not reproduced. The full treatment runs, mapping permutations and retention results are outstanding. Input panels do not exhaust integer inputs; program arithmetic may depend on compiler/platform behavior. Short-lived gates can escape sampled logs. Parameters may yield a single opening, persistent eligibility, throttling, or no capability accumulation. Report those outcomes under the original claim rather than relabeling every fluctuation as learning. A constrained mechanism does not by itself settle the owner's account of knowledge.

**One next step.** Run the three matched-seed A/B trajectories continuously with the supplied logging, retaining the two mechanism controls and continuous-reference plan for interpreting their results.

## Appendix

The following configuration syntax is **checked** against the source locations above. Copy each design's blocks into its own working directory beside the original ancestor and instruction-set files. Preserve the original baseline `avida.cfg`; replace the named entries with Appendix A's values rather than appending conflicting definitions. Use the original actual seed for each matched run. No C++ changes or population reloads are required.

### A. avida.cfg changes for both designs

Apply this identical block to each original baseline configuration. Its file names assume each design and seed has a separate working directory. Keep the baseline instruction-set include `#include INST_SET=instset-heads.cfg`; do not replace the instruction definitions.

#### avida.cfg entries to replace

```text
# Apply these entries to the same stock avida.cfg used in the old runs.
# Keep the existing instruction-set include and all unlisted baseline entries.
# Supply each old run's actual seed with -set RANDOM_SEED NUMBER.
# Do not use RANDOM_SEED -1 for the paired comparison.
WORLD_X 60
WORLD_Y 60
COPY_MUT_PROB 0.0075
COPY_INS_PROB 0
COPY_DEL_PROB 0
POINT_MUT_PROB 0
DIV_MUT_PROB 0
DIV_INS_PROB 0
DIV_DEL_PROB 0
DIVIDE_MUT_PROB 0
DIVIDE_INS_PROB 0.05
DIVIDE_DEL_PROB 0.05
PRECALC_PHENOTYPE 0
ENERGY_ENABLED 0
USE_RESOURCE_BINS 0
TASK_REFRACTORY_PERIOD 0
TASK_SWITCH_PENALTY 0
TASK_SWITCH_PENALTY_TYPE 0
ENVIRONMENT_FILE environment.cfg
EVENT_FILE events.cfg
DATA_DIR data
```

Launch each evolution run after assigning `SEED` the corresponding original seed value:

```bash
: "${SEED:?Set SEED to the matched original run seed}"
avida -c avida.cfg -set RANDOM_SEED "$SEED"
```

### B. Design A complete files

#### environment.cfg

```text
# Design A: work opens a shared market.
# Checked against Avida commit 47f13dadb; evolution outcomes unmeasured.
RESOURCE feed:initial=3600:inflow=360:outflow=0.1:geometry=global
RESOURCE market:initial=0:inflow=0:outflow=0.1:geometry=global

REACTION NOT not process:resource=feed:value=1:type=pow:max=1:min=0.01:frac=0.001:product=market:conversion=1 requisite:reaction_max_count=1
REACTION NAND nand process:resource=feed:value=1:type=pow:max=1:min=0.01:frac=0.001:product=market:conversion=1 requisite:reaction_max_count=1
REACTION AND and process:resource=market:value=1:type=pow:max=1:min=0.01:frac=0.001 requisite:reaction_max_count=1
REACTION ORN orn process:resource=market:value=1:type=pow:max=1:min=0.01:frac=0.001 requisite:reaction_max_count=1
REACTION OR or process:resource=market:value=1:type=pow:max=1:min=0.01:frac=0.001 requisite:reaction_max_count=1
REACTION ANDN andn process:resource=market:value=1:type=pow:max=1:min=0.01:frac=0.001 requisite:reaction_max_count=1
REACTION NOR nor process:resource=market:value=1:type=pow:max=1:min=0.01:frac=0.001 requisite:reaction_max_count=1
REACTION XOR xor process:resource=market:value=1:type=pow:max=1:min=0.01:frac=0.001 requisite:reaction_max_count=1
REACTION EQU equ process:resource=market:value=1:type=pow:max=1:min=0.01:frac=0.001 requisite:reaction_max_count=1

# Checked task names in cTaskLib::AddTask. No reward or resource use.
REACTION PROBE_logic_3AA logic_3AA process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AB logic_3AB process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AC logic_3AC process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AD logic_3AD process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AE logic_3AE process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AF logic_3AF process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AG logic_3AG process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AH logic_3AH process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AI logic_3AI process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AJ logic_3AJ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AK logic_3AK process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AL logic_3AL process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AM logic_3AM process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AN logic_3AN process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AO logic_3AO process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AP logic_3AP process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AQ logic_3AQ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AR logic_3AR process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AS logic_3AS process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AT logic_3AT process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AU logic_3AU process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AV logic_3AV process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AW logic_3AW process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AX logic_3AX process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AY logic_3AY process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AZ logic_3AZ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BA logic_3BA process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BB logic_3BB process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BC logic_3BC process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BD logic_3BD process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BE logic_3BE process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BF logic_3BF process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BG logic_3BG process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BH logic_3BH process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BI logic_3BI process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BJ logic_3BJ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BK logic_3BK process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BL logic_3BL process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BM logic_3BM process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BN logic_3BN process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BO logic_3BO process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BP logic_3BP process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BQ logic_3BQ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BR logic_3BR process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BS logic_3BS process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BT logic_3BT process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BU logic_3BU process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BV logic_3BV process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BW logic_3BW process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BX logic_3BX process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BY logic_3BY process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BZ logic_3BZ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CA logic_3CA process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CB logic_3CB process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CC logic_3CC process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CD logic_3CD process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CE logic_3CE process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CF logic_3CF process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CG logic_3CG process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CH logic_3CH process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CI logic_3CI process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CJ logic_3CJ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CK logic_3CK process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CL logic_3CL process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CM logic_3CM process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CN logic_3CN process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CO logic_3CO process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CP logic_3CP process:value=0:type=pow requisite:max_count=1
```

#### events.cfg

```text
# Stock Avida 2.14 commit 47f13dadb; continuous evolution.
# Use the same initial injection and exact seed as the comparison runs.
u begin Inject default-heads.org
u 0:100:50000 PrintAverageData
u 0:100:50000 PrintCountData
u 0:100:50000 PrintTasksData
u 0:100:50000 PrintTasksExeData
u 0:100:50000 PrintReactionData
u 0:100:50000 PrintReactionExeData
u 0:100:50000 PrintTimeData
u 0:1:50000 PrintResourceData resource.dat 0
u 0:1000:50000 SavePopulation filename=detail:save_historic=0
u 50000 SavePopulation filename=ancestry:save_historic=1
u 50000 Exit
```

### C. Design B complete files

#### environment.cfg

```text
# Design B: symmetric pools exchanged by task performance.
# Checked against Avida commit 47f13dadb; evolution outcomes unmeasured.
RESOURCE left:initial=1800:inflow=180:outflow=0.1:geometry=global
RESOURCE right:initial=1800:inflow=180:outflow=0.1:geometry=global

REACTION NOT not process:resource=left:value=0.01:type=pow:max=100:min=100:frac=0.1:product=right:conversion=1 requisite:reaction_max_count=1
REACTION NAND nand process:resource=right:value=0.01:type=pow:max=100:min=100:frac=0.1:product=left:conversion=1 requisite:reaction_max_count=1
REACTION AND and process:resource=right:value=0.01:type=pow:max=100:min=100:frac=0.1:product=left:conversion=1 requisite:reaction_max_count=1
REACTION ORN orn process:resource=right:value=0.01:type=pow:max=100:min=100:frac=0.1:product=left:conversion=1 requisite:reaction_max_count=1
REACTION OR or process:resource=left:value=0.01:type=pow:max=100:min=100:frac=0.1:product=right:conversion=1 requisite:reaction_max_count=1
REACTION ANDN andn process:resource=left:value=0.01:type=pow:max=100:min=100:frac=0.1:product=right:conversion=1 requisite:reaction_max_count=1
REACTION NOR nor process:resource=right:value=0.01:type=pow:max=100:min=100:frac=0.1:product=left:conversion=1 requisite:reaction_max_count=1
REACTION XOR xor process:resource=left:value=0.01:type=pow:max=100:min=100:frac=0.1:product=right:conversion=1 requisite:reaction_max_count=1
REACTION EQU equ process:resource=right:value=0.01:type=pow:max=100:min=100:frac=0.1:product=left:conversion=1 requisite:reaction_max_count=1

# Checked task names in cTaskLib::AddTask. No reward or resource use.
REACTION PROBE_logic_3AA logic_3AA process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AB logic_3AB process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AC logic_3AC process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AD logic_3AD process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AE logic_3AE process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AF logic_3AF process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AG logic_3AG process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AH logic_3AH process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AI logic_3AI process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AJ logic_3AJ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AK logic_3AK process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AL logic_3AL process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AM logic_3AM process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AN logic_3AN process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AO logic_3AO process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AP logic_3AP process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AQ logic_3AQ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AR logic_3AR process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AS logic_3AS process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AT logic_3AT process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AU logic_3AU process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AV logic_3AV process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AW logic_3AW process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AX logic_3AX process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AY logic_3AY process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3AZ logic_3AZ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BA logic_3BA process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BB logic_3BB process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BC logic_3BC process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BD logic_3BD process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BE logic_3BE process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BF logic_3BF process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BG logic_3BG process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BH logic_3BH process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BI logic_3BI process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BJ logic_3BJ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BK logic_3BK process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BL logic_3BL process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BM logic_3BM process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BN logic_3BN process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BO logic_3BO process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BP logic_3BP process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BQ logic_3BQ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BR logic_3BR process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BS logic_3BS process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BT logic_3BT process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BU logic_3BU process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BV logic_3BV process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BW logic_3BW process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BX logic_3BX process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BY logic_3BY process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3BZ logic_3BZ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CA logic_3CA process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CB logic_3CB process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CC logic_3CC process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CD logic_3CD process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CE logic_3CE process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CF logic_3CF process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CG logic_3CG process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CH logic_3CH process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CI logic_3CI process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CJ logic_3CJ process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CK logic_3CK process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CL logic_3CL process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CM logic_3CM process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CN logic_3CN process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CO logic_3CO process:value=0:type=pow requisite:max_count=1
REACTION PROBE_logic_3CP logic_3CP process:value=0:type=pow requisite:max_count=1
```

#### events.cfg

```text
# Stock Avida 2.14 commit 47f13dadb; continuous evolution.
# Use the same initial injection and exact seed as the comparison runs.
u begin Inject default-heads.org
u 0:100:50000 PrintAverageData
u 0:100:50000 PrintCountData
u 0:100:50000 PrintTasksData
u 0:100:50000 PrintTasksExeData
u 0:100:50000 PrintReactionData
u 0:100:50000 PrintReactionExeData
u 0:100:50000 PrintTimeData
u 0:1:50000 PrintResourceData resource.dat 0
u 0:1000:50000 SavePopulation filename=detail:save_historic=0
u 50000 SavePopulation filename=ancestry:save_historic=1
u 50000 Exit
```

### D. Complete neutral probe files

Place these two files in each finished run directory. They are used only by a separate analysis process. The first nine columns after the metadata are the nine standard logic tasks; the next 68 are three-input logic tasks; the final eight are the listed arithmetic tasks. Inline task IDs in the environment file give the exact mapping.

#### probe-environment.cfg

```text
# Offline task recognition only; no resources or rewards.
# Match this exact task order when reading DETAIL task.N columns.
# Use only the bounded manual input panels in probe-analyze.cfg.
# Task recognition functions use C++ signed-int arithmetic.
REACTION OBS_not not process:value=0:type=pow # task.0
REACTION OBS_nand nand process:value=0:type=pow # task.1
REACTION OBS_and and process:value=0:type=pow # task.2
REACTION OBS_orn orn process:value=0:type=pow # task.3
REACTION OBS_or or process:value=0:type=pow # task.4
REACTION OBS_andn andn process:value=0:type=pow # task.5
REACTION OBS_nor nor process:value=0:type=pow # task.6
REACTION OBS_xor xor process:value=0:type=pow # task.7
REACTION OBS_equ equ process:value=0:type=pow # task.8
REACTION OBS_logic_3AA logic_3AA process:value=0:type=pow # task.9
REACTION OBS_logic_3AB logic_3AB process:value=0:type=pow # task.10
REACTION OBS_logic_3AC logic_3AC process:value=0:type=pow # task.11
REACTION OBS_logic_3AD logic_3AD process:value=0:type=pow # task.12
REACTION OBS_logic_3AE logic_3AE process:value=0:type=pow # task.13
REACTION OBS_logic_3AF logic_3AF process:value=0:type=pow # task.14
REACTION OBS_logic_3AG logic_3AG process:value=0:type=pow # task.15
REACTION OBS_logic_3AH logic_3AH process:value=0:type=pow # task.16
REACTION OBS_logic_3AI logic_3AI process:value=0:type=pow # task.17
REACTION OBS_logic_3AJ logic_3AJ process:value=0:type=pow # task.18
REACTION OBS_logic_3AK logic_3AK process:value=0:type=pow # task.19
REACTION OBS_logic_3AL logic_3AL process:value=0:type=pow # task.20
REACTION OBS_logic_3AM logic_3AM process:value=0:type=pow # task.21
REACTION OBS_logic_3AN logic_3AN process:value=0:type=pow # task.22
REACTION OBS_logic_3AO logic_3AO process:value=0:type=pow # task.23
REACTION OBS_logic_3AP logic_3AP process:value=0:type=pow # task.24
REACTION OBS_logic_3AQ logic_3AQ process:value=0:type=pow # task.25
REACTION OBS_logic_3AR logic_3AR process:value=0:type=pow # task.26
REACTION OBS_logic_3AS logic_3AS process:value=0:type=pow # task.27
REACTION OBS_logic_3AT logic_3AT process:value=0:type=pow # task.28
REACTION OBS_logic_3AU logic_3AU process:value=0:type=pow # task.29
REACTION OBS_logic_3AV logic_3AV process:value=0:type=pow # task.30
REACTION OBS_logic_3AW logic_3AW process:value=0:type=pow # task.31
REACTION OBS_logic_3AX logic_3AX process:value=0:type=pow # task.32
REACTION OBS_logic_3AY logic_3AY process:value=0:type=pow # task.33
REACTION OBS_logic_3AZ logic_3AZ process:value=0:type=pow # task.34
REACTION OBS_logic_3BA logic_3BA process:value=0:type=pow # task.35
REACTION OBS_logic_3BB logic_3BB process:value=0:type=pow # task.36
REACTION OBS_logic_3BC logic_3BC process:value=0:type=pow # task.37
REACTION OBS_logic_3BD logic_3BD process:value=0:type=pow # task.38
REACTION OBS_logic_3BE logic_3BE process:value=0:type=pow # task.39
REACTION OBS_logic_3BF logic_3BF process:value=0:type=pow # task.40
REACTION OBS_logic_3BG logic_3BG process:value=0:type=pow # task.41
REACTION OBS_logic_3BH logic_3BH process:value=0:type=pow # task.42
REACTION OBS_logic_3BI logic_3BI process:value=0:type=pow # task.43
REACTION OBS_logic_3BJ logic_3BJ process:value=0:type=pow # task.44
REACTION OBS_logic_3BK logic_3BK process:value=0:type=pow # task.45
REACTION OBS_logic_3BL logic_3BL process:value=0:type=pow # task.46
REACTION OBS_logic_3BM logic_3BM process:value=0:type=pow # task.47
REACTION OBS_logic_3BN logic_3BN process:value=0:type=pow # task.48
REACTION OBS_logic_3BO logic_3BO process:value=0:type=pow # task.49
REACTION OBS_logic_3BP logic_3BP process:value=0:type=pow # task.50
REACTION OBS_logic_3BQ logic_3BQ process:value=0:type=pow # task.51
REACTION OBS_logic_3BR logic_3BR process:value=0:type=pow # task.52
REACTION OBS_logic_3BS logic_3BS process:value=0:type=pow # task.53
REACTION OBS_logic_3BT logic_3BT process:value=0:type=pow # task.54
REACTION OBS_logic_3BU logic_3BU process:value=0:type=pow # task.55
REACTION OBS_logic_3BV logic_3BV process:value=0:type=pow # task.56
REACTION OBS_logic_3BW logic_3BW process:value=0:type=pow # task.57
REACTION OBS_logic_3BX logic_3BX process:value=0:type=pow # task.58
REACTION OBS_logic_3BY logic_3BY process:value=0:type=pow # task.59
REACTION OBS_logic_3BZ logic_3BZ process:value=0:type=pow # task.60
REACTION OBS_logic_3CA logic_3CA process:value=0:type=pow # task.61
REACTION OBS_logic_3CB logic_3CB process:value=0:type=pow # task.62
REACTION OBS_logic_3CC logic_3CC process:value=0:type=pow # task.63
REACTION OBS_logic_3CD logic_3CD process:value=0:type=pow # task.64
REACTION OBS_logic_3CE logic_3CE process:value=0:type=pow # task.65
REACTION OBS_logic_3CF logic_3CF process:value=0:type=pow # task.66
REACTION OBS_logic_3CG logic_3CG process:value=0:type=pow # task.67
REACTION OBS_logic_3CH logic_3CH process:value=0:type=pow # task.68
REACTION OBS_logic_3CI logic_3CI process:value=0:type=pow # task.69
REACTION OBS_logic_3CJ logic_3CJ process:value=0:type=pow # task.70
REACTION OBS_logic_3CK logic_3CK process:value=0:type=pow # task.71
REACTION OBS_logic_3CL logic_3CL process:value=0:type=pow # task.72
REACTION OBS_logic_3CM logic_3CM process:value=0:type=pow # task.73
REACTION OBS_logic_3CN logic_3CN process:value=0:type=pow # task.74
REACTION OBS_logic_3CO logic_3CO process:value=0:type=pow # task.75
REACTION OBS_logic_3CP logic_3CP process:value=0:type=pow # task.76
REACTION OBS_math_1AA math_1AA process:value=0:type=pow # task.77
REACTION OBS_math_1AK math_1AK process:value=0:type=pow # task.78
REACTION OBS_math_1AL math_1AL process:value=0:type=pow # task.79
REACTION OBS_math_1AN math_1AN process:value=0:type=pow # task.80
REACTION OBS_math_2AN math_2AN process:value=0:type=pow # task.81
REACTION OBS_math_2AO math_2AO process:value=0:type=pow # task.82
REACTION OBS_math_3AH math_3AH process:value=0:type=pow # task.83
REACTION OBS_math_3AI math_3AI process:value=0:type=pow # task.84
```

#### probe-analyze.cfg

```text
# Run in a separate analyze-mode process with probe-environment.cfg.
# Output goes to the DATA_DIR chosen for analysis, e.g. probe-results.
# Snapshots are read from data/. Do not reload the evolving run.
CONFIG_SET TEST_CPU_TIME_MOD 20
FORRANGE u 0 50000 1000
  PURGE_BATCH
  LOAD data/detail-$u.spop
  RECALCULATE 0 -1 0 -16976881 -19664589 -19966379
  DETAIL probe-$u-p01.dat id num_cpus viable length gest_time env_input.0 env_input.1 env_input.2 task.0 task.1 task.2 task.3 task.4 task.5 task.6 task.7 task.8 task.9 task.10 task.11 task.12 task.13 task.14 task.15 task.16 task.17 task.18 task.19 task.20 task.21 task.22 task.23 task.24 task.25 task.26 task.27 task.28 task.29 task.30 task.31 task.32 task.33 task.34 task.35 task.36 task.37 task.38 task.39 task.40 task.41 task.42 task.43 task.44 task.45 task.46 task.47 task.48 task.49 task.50 task.51 task.52 task.53 task.54 task.55 task.56 task.57 task.58 task.59 task.60 task.61 task.62 task.63 task.64 task.65 task.66 task.67 task.68 task.69 task.70 task.71 task.72 task.73 task.74 task.75 task.76 task.77 task.78 task.79 task.80 task.81 task.82 task.83 task.84
  RECALCULATE 0 -1 0 12228111 -4894669 -18491051
  DETAIL probe-$u-p02.dat id num_cpus viable length gest_time env_input.0 env_input.1 env_input.2 task.0 task.1 task.2 task.3 task.4 task.5 task.6 task.7 task.8 task.9 task.10 task.11 task.12 task.13 task.14 task.15 task.16 task.17 task.18 task.19 task.20 task.21 task.22 task.23 task.24 task.25 task.26 task.27 task.28 task.29 task.30 task.31 task.32 task.33 task.34 task.35 task.36 task.37 task.38 task.39 task.40 task.41 task.42 task.43 task.44 task.45 task.46 task.47 task.48 task.49 task.50 task.51 task.52 task.53 task.54 task.55 task.56 task.57 task.58 task.59 task.60 task.61 task.62 task.63 task.64 task.65 task.66 task.67 task.68 task.69 task.70 task.71 task.72 task.73 task.74 task.75 task.76 task.77 task.78 task.79 task.80 task.81 task.82 task.83 task.84
  RECALCULATE 0 -1 0 -5180913 25091379 21074517
  DETAIL probe-$u-p03.dat id num_cpus viable length gest_time env_input.0 env_input.1 env_input.2 task.0 task.1 task.2 task.3 task.4 task.5 task.6 task.7 task.8 task.9 task.10 task.11 task.12 task.13 task.14 task.15 task.16 task.17 task.18 task.19 task.20 task.21 task.22 task.23 task.24 task.25 task.26 task.27 task.28 task.29 task.30 task.31 task.32 task.33 task.34 task.35 task.36 task.37 task.38 task.39 task.40 task.41 task.42 task.43 task.44 task.45 task.46 task.47 task.48 task.49 task.50 task.51 task.52 task.53 task.54 task.55 task.56 task.57 task.58 task.59 task.60 task.61 task.62 task.63 task.64 task.65 task.66 task.67 task.68 task.69 task.70 task.71 task.72 task.73 task.74 task.75 task.76 task.77 task.78 task.79 task.80 task.81 task.82 task.83 task.84
  RECALCULATE 0 -1 0 17940239 2122291 15182933
  DETAIL probe-$u-p04.dat id num_cpus viable length gest_time env_input.0 env_input.1 env_input.2 task.0 task.1 task.2 task.3 task.4 task.5 task.6 task.7 task.8 task.9 task.10 task.11 task.12 task.13 task.14 task.15 task.16 task.17 task.18 task.19 task.20 task.21 task.22 task.23 task.24 task.25 task.26 task.27 task.28 task.29 task.30 task.31 task.32 task.33 task.34 task.35 task.36 task.37 task.38 task.39 task.40 task.41 task.42 task.43 task.44 task.45 task.46 task.47 task.48 task.49 task.50 task.51 task.52 task.53 task.54 task.55 task.56 task.57 task.58 task.59 task.60 task.61 task.62 task.63 task.64 task.65 task.66 task.67 task.68 task.69 task.70 task.71 task.72 task.73 task.74 task.75 task.76 task.77 task.78 task.79 task.80 task.81 task.82 task.83 task.84
  RECALCULATE 0 -1 0 -15831537 -3797709 11959381
  DETAIL probe-$u-p05.dat id num_cpus viable length gest_time env_input.0 env_input.1 env_input.2 task.0 task.1 task.2 task.3 task.4 task.5 task.6 task.7 task.8 task.9 task.10 task.11 task.12 task.13 task.14 task.15 task.16 task.17 task.18 task.19 task.20 task.21 task.22 task.23 task.24 task.25 task.26 task.27 task.28 task.29 task.30 task.31 task.32 task.33 task.34 task.35 task.36 task.37 task.38 task.39 task.40 task.41 task.42 task.43 task.44 task.45 task.46 task.47 task.48 task.49 task.50 task.51 task.52 task.53 task.54 task.55 task.56 task.57 task.58 task.59 task.60 task.61 task.62 task.63 task.64 task.65 task.66 task.67 task.68 task.69 task.70 task.71 task.72 task.73 task.74 task.75 task.76 task.77 task.78 task.79 task.80 task.81 task.82 task.83 task.84
  RECALCULATE 0 -1 0 -1055985 -3123405 5367125
  DETAIL probe-$u-p06.dat id num_cpus viable length gest_time env_input.0 env_input.1 env_input.2 task.0 task.1 task.2 task.3 task.4 task.5 task.6 task.7 task.8 task.9 task.10 task.11 task.12 task.13 task.14 task.15 task.16 task.17 task.18 task.19 task.20 task.21 task.22 task.23 task.24 task.25 task.26 task.27 task.28 task.29 task.30 task.31 task.32 task.33 task.34 task.35 task.36 task.37 task.38 task.39 task.40 task.41 task.42 task.43 task.44 task.45 task.46 task.47 task.48 task.49 task.50 task.51 task.52 task.53 task.54 task.55 task.56 task.57 task.58 task.59 task.60 task.61 task.62 task.63 task.64 task.65 task.66 task.67 task.68 task.69 task.70 task.71 task.72 task.73 task.74 task.75 task.76 task.77 task.78 task.79 task.80 task.81 task.82 task.83 task.84
  RECALCULATE 0 -1 0 17197839 7993651 22524245
  DETAIL probe-$u-p07.dat id num_cpus viable length gest_time env_input.0 env_input.1 env_input.2 task.0 task.1 task.2 task.3 task.4 task.5 task.6 task.7 task.8 task.9 task.10 task.11 task.12 task.13 task.14 task.15 task.16 task.17 task.18 task.19 task.20 task.21 task.22 task.23 task.24 task.25 task.26 task.27 task.28 task.29 task.30 task.31 task.32 task.33 task.34 task.35 task.36 task.37 task.38 task.39 task.40 task.41 task.42 task.43 task.44 task.45 task.46 task.47 task.48 task.49 task.50 task.51 task.52 task.53 task.54 task.55 task.56 task.57 task.58 task.59 task.60 task.61 task.62 task.63 task.64 task.65 task.66 task.67 task.68 task.69 task.70 task.71 task.72 task.73 task.74 task.75 task.76 task.77 task.78 task.79 task.80 task.81 task.82 task.83 task.84
  RECALCULATE 0 -1 0 11237903 11659315 3456341
  DETAIL probe-$u-p08.dat id num_cpus viable length gest_time env_input.0 env_input.1 env_input.2 task.0 task.1 task.2 task.3 task.4 task.5 task.6 task.7 task.8 task.9 task.10 task.11 task.12 task.13 task.14 task.15 task.16 task.17 task.18 task.19 task.20 task.21 task.22 task.23 task.24 task.25 task.26 task.27 task.28 task.29 task.30 task.31 task.32 task.33 task.34 task.35 task.36 task.37 task.38 task.39 task.40 task.41 task.42 task.43 task.44 task.45 task.46 task.47 task.48 task.49 task.50 task.51 task.52 task.53 task.54 task.55 task.56 task.57 task.58 task.59 task.60 task.61 task.62 task.63 task.64 task.65 task.66 task.67 task.68 task.69 task.70 task.71 task.72 task.73 task.74 task.75 task.76 task.77 task.78 task.79 task.80 task.81 task.82 task.83 task.84
  PURGE_BATCH
END
```

Launch the probe process from the finished evolution directory:

```bash
avida -c avida.cfg -a \
  -set ENVIRONMENT_FILE probe-environment.cfg \
  -set ANALYZE_FILE probe-analyze.cfg \
  -set DATA_DIR probe-results
```

The supplied loop expects the new runs' `data/detail-0.spop` through `data/detail-50000.spop`. For older runs, point `LOAD` at their actual snapshots and preserve update labels; if update zero was not saved, test the ancestor separately and start the snapshot loop at 1000. Do not invent a missing snapshot.

### E. Exact mechanism control edits

For A's production-removal control, copy A into a separate run directory and replace its two `conversion=1` settings with `conversion=0`. Leave all other entries and the seed unchanged.

For B's same-pool-return control, copy B into a separate directory. On NOT, OR, ANDN and XOR, replace `product=right` with `product=left`. On NAND, AND, ORN, NOR and EQU, replace `product=left` with `product=right`. Keep `conversion=1`, all consumption/payment settings, resource definitions and the matched seed. The control uses the same complete events file.

These are new control runs. Do not edit an evolving run's files mid-run.

END OF REPORT
