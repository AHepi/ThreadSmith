# Research, checked: selecting with drives but no fixed objectives

## Summary for the owner

The checked literature offers ways for an execution environment to choose its next challenge without naming its final achievement. It can seek unfamiliar behavior, learning progress, controllable possibilities, or challenges another program can already handle. Some methods preserve a collection of earlier solutions. [R1–R19]

My reading under your definitions: none of the mechanisms examined reaches grade 3. Their next challenge changes, but code still judges novelty, progress, success, or admission. A changing checker is still a checker.

Prediction and anticipation have been studied in Avida. Those studies use designed rewards and world dynamics; they do not supply a selector free of success rules. [R14–R16, checked]

There are concrete options for testing these ideas. Several can start with saved programs and an external driver. Two qualifications matter: restarting a saved population changes execution state, and stock parasites cannot infect the present “heads” programs. [R20, checked]

This report supplies options, costs, and results that would count against them. No Avida experiments were run. It leaves the meaning of knowledge, the status of human-written task history, and the choice of costly runs with you.

## Table

Grades follow the brief: **1**, exact named functions; **2**, a specified class or rule; **3**, no solution-checking code. Grade assignments and Avida mappings are this report's inferences. None of the rows is a grade-3 demonstration. A method can combine a grade-2 selector with grade-1 task rewards.

**Cost convention:** all line counts are provisional engineering estimates for a restricted prototype, not implemented code. D means new driver lines; C means new C++ lines; cfg means configuration/event lines. Counts exclude tests unless explicitly labelled as checks, and exclude supporting libraries and experiment analysis; allow a separate test effort, described below. “Driver” includes program reseeding between run segments; test allowances explicitly shown in rows are not charged again below. Raw-output drivers assume Claude's existing `RUN_BOUNDED` patch, so they are not wholly stock Avida.

| Name | The selector's instinct | Its memory and model | Grade of naming | Stock or C++ | Estimated cost | What counts against |
|---|---|---|---|---|---|---|
| Novelty search | Select unfamiliar behavior | Behavior records and archive | 2: descriptor, distance, admission | Driver plus supplied patch; C++ for live selection | D 300–700; live C 600–1,500 | Novel traces grow; repeatable capabilities do not |
| Minimal criterion novelty search | Explore novelty within an eligibility condition | Archive and pass/fail criterion | 2; 1 if a named function is required | Stock named gate plus novelty driver; arbitrary live gate needs C++ | D +50–150 beyond novelty; C +150–350 for gate | Gate blocks almost all variation or protects only its starting behavior |
| Minimal criterion coevolution | Admit challenges and programs with a working counterpart | Two changing queues and interaction results | 2: success relation remains specified | Restricted driver; C++ for new interactions | D 700–1,600 | Trivial mutual compatibility, cycling, or loss of earlier behavior |
| POET | Preserve varied, manageable challenges and exchange solutions | Environment–program pairs and archive | 2: world encoding, score, thresholds | Stock settings plus driver | D 1,000–2,500 | Transfers add no independently repeatable capability |
| Enhanced POET | Seek challenges that distinguish the current solver collection | Cross-evaluation matrix and archived specialists | 2: score-vector construction and distance | Driver extension; new world primitives may need C++ | D +300–800 beyond POET | Distances grow only through noise or changing reference membership |
| PAIRED | Seek a performance gap a reference solver can bridge | Two learning program populations; generator state | 2: return and regret rule | Restricted stock-world driver analogue | D 1,500–3,000 | Gaps arise from disabling the learner, without capability gains |
| OMNI | Select learnable tasks judged interesting by a model | Success histories, prompts, pretrained model | 2: task language and completion checks | Driver over tasks/traces; live new predicates need C++ | D 800–2,000; live C +500–1,200 for restricted predicates | Labels influence selection while tested behavior does not expand |
| Learning progress | Select observations or challenges with reducible error | Predictor and progress histories | 2: observations, loss, progress window | Stock-task driver; supplied patch for raw traces | D 250–600 for task menu | Forgetting and relearning produce the entire signal |
| Compression progress | Select experiences that improve a compressor | Trace history and old/new models | 2: encoding, compressor, progress rule | Driver plus supplied patch; live hook needs C++ | D 500–1,200; live C +600–1,500 | Noise or bookkeeping earns continuing credit |
| Empowerment | Preserve controllable future possibilities | Causal transition model or intervention trials | 2: interventions, observations, horizon | Driver branches; C++ for new action/world coupling | D 1,000–2,500 | Only trivial control over counts or inputs increases |
| MAP-Elites / quality diversity | Preserve high-quality representatives of chosen kinds | Descriptor cells and stored programs | 2; possibly grade-1 quality rewards | Driver; live integration needs C++ | D 300–800; live C 800–1,800 | Filled cells represent incidental differences, not retained behavior |
| Avida host–parasite coevolution | Favor escape from current parasites and successful infection | Changing program communities | 2 over a fixed task vocabulary | Stock TransSMT setup, not current heads setup | cfg 40–150; checks D 150–400 | Parasites disappear or only old task combinations cycle |
| Prediction / anticipation | Favor behavior suited to upcoming events | Clock/trail state, forecast records, or joint frequencies | 1/2 according to score | Driver can test history windows; live delayed forecasts need C++ | C 500–1,200; checks D 250–500 | Timing, copying, or current cues explain apparent anticipation |
| Resource-dependent Avida feedback | Reduce returns to frequently consumed resources | Current resource quantities and inflow/outflow | 2 over a named task catalogue | Stock resource configuration | cfg 20–180; checks D 100–250 | Replay gives the same effect or gains stop at the same repertoire |
| Fluctuating Avida task environments | Favor context-dependent responses | Resource state and schedule; no adaptive selector model required | 1/2: fixed task menu and switching rule | Stock settings/events; suitable sensory instructions | cfg 30–120; checks D 100–300 | Switching reuses a closed repertoire without further capabilities |
| POWERPLAY | Accept a new solvable task while retaining previous solutions | Task archive, solver versions, dependency records | 2: executable success procedures | Restricted driver plus supplied patch | D 700–1,600 | New task labels or cheaper old behavior masquerade as new capabilities |

## One section per line of work

### Reading and implementation boundaries

This is a literature and source audit, completed on 2 October 2026 Brisbane time. Each cited primary source was opened by a research helper and reopened during merging; duplicate accounts were consolidated. “Checked” means the stated text or figure was inspected, not that its experiment was reproduced. No source-dependent conclusion relies on memory. The brief's S113–S118 accounts are supplied background, not independently rerun findings. No S118 outcome is assumed.

The frozen question is what a **selecting Avida execution environment** could do with programs as its material. Moving a robot's curiosity mechanism into this selector is a proposed translation. It is not evidence that the translation works. “Capability” below means specified behavior that can be reproduced under declared tests, without deciding whether that is knowledge.

Checked source [R20]: commit `47f13dadb547fcf10f620ace60247f38b30b8b16` was read. Source-file paths below are relative to `avida-core/source/`; fixture paths show their separate prefix. Stock reaction/resource controls are in `actions/EnvironmentActions.cc`. Population save/load actions are in `actions/SaveLoadActions.cc`; `main/cPopulation.cc::LoadPopulation` creates execution instances and calls `SetupInject`, with an approximate merit adjustment for saved execution offsets. It is not an exact live-machine checkpoint. `CompeteOrganisms` aggregates trial scores; it does not accept arbitrary novelty scores as an event argument.

Checked source [R20]: a live custom selector could use a new action in `actions/PopulationActions.cc` and the existing `main/cPopulation.cc::UpdateMerit` scheduling interface. This is an integration hook, not a completed selector. Nonpositive merit invokes program removal, so a paper's zero novelty must not be translated casually into zero live merit. New criteria may touch `main/cOrganism.cc`, `main/cEnvironment.cc/.h`, `main/cTaskLib.cc/.h`, or the relevant virtual hardware. Tests must check reward timing, replication, and score persistence.

Between-segment selection is only one layer: inside each segment, copying speed, replication failures, replacement, and any task rewards still select programs. A driver adaptation must declare those pressures; reseeding alone does not reproduce novelty-only selection. Stock event controls also do not imply arbitrary live changes to hardware or world layout.

I did not build or execute Avida, modify its source, or write replication code. Claude's populations and `RUN_BOUNDED` implementation were not supplied here, so their interfaces and behavior could not be inspected. All experiments below remain options.

### Novelty search

**Checked [R1], §§3, 5–6, 9.1:** novelty search scores distance from current and archived behavior. The designer selects the descriptor, metric, neighbor rule, and archive admission policy. In the hard-maze experiment, it found solutions in 39 of 40 runs within a 250,000-evaluation budget. Finding a solution does not impose continuing pressure to preserve or refine it. This is finite discovery evidence; it does not test continued retention of all discoveries.

**Avida proposal:** the selector could compare bounded output traces without classifying them as named logic functions. This is grade 2 because “different under this metric” is the rule. Input order, trace length, and execution budget are part of the specification. The table's driver estimate uses saved-program evaluation and reseeding; live C++ would use `PopulationActions.cc`, `cPopulation.cc`, and new archive storage. `RUN_BOUNDED` would need a checked interface before reuse.

Claude could first inspect whether novelty changes when inputs are reordered or runs repeated. Continuing novelty caused by output timing or unstable traces, without reproducible additional behavior, would count against this use. An archive of descriptors alone cannot recover the programs that produced them: store instruction sequences if recovery is intended.

### Minimal criterion novelty search

**Checked [R2], §§3–6:** MCNS restricts novelty search to candidates satisfying a minimum condition. Failed candidates receive zero novelty and a failure descriptor. The two-point navigation study starts from controllers already reaching the first point. Experiments used 100 runs per method per task, each limited to 500,000 evaluations. The authors identify stringent criteria and fragile starting controllers as causes of stalled exploration; they do not demonstrate indefinite retention.

**Avida proposal:** require replication capability while selecting novel traces, or require a declared behavioral condition. A particular required logic function adds grade 1; any qualifying member of a specified family is grade 2. Checked source [R20]: `REQUIRED_TASK`, `REQUIRED_REACTION`, and `REQUIRE_SINGLE_REACTION` have stock division checks in `cOrganism.cc`. They do not implement novelty or arbitrary trace criteria.

Costs in the table are additions to novelty. A driver can filter saved programs; an arbitrary live gate would touch `cOrganism.cc` and its evaluator. Before a run, check that qualifying programs exist and have qualifying descendants. The brief's task-free ancestor cannot be assumed to satisfy a task gate. If almost all variation is rejected, or only the protected behavior remains, the intended carry-over has not occurred.

### Minimal criterion coevolution

**Checked [R3], §§3–6:** MCC admits maze solvers that solve a current maze and mazes solved by a current solver. It bootstraps qualifying maze–solver pairs using novelty search, then keeps bounded queues with retirement of older entries; a variant groups candidates by encoded structure. Twenty runs per variant used 2,000 batches. The reported mazes reached an imposed complexity ceiling. A changing counterpart supplies challenges, but an exit-reaching checker still determines success. Queue retirement does not preserve every historical solution.

**Avida proposal:** keep a challenge queue and a program queue, with admission based on their interaction. This remains grade 2. The relation, challenge language, eligibility rule, queue policy, and initial compatible pairs are specified. MCC is also a counterexample to the claim that every divergent selector needs a behavioral distance.

A restricted driver can cross-test saved programs before introducing new search. Its estimate assumes existing evaluators and `SaveLoadActions.cc` interfaces; a specified new evaluator could add 500–1,500 C++ lines in `cTaskLib.cc/.h` and `cEnvironment.cc/.h`. Unrestricted new interactions have no defensible generic line estimate. Admission dominated by mutually compatible trivial cases, repeated cycles, or disappearing earlier capability would count against the translation. Merely changing both queues is insufficient.

### POET

**Checked [R4], §§3, 4.1–4.4:** POET maintains paired environments and controllers, proposes changed environments, filters difficulty, selects environmental novelty, and attempts solution transfers. Its distance uses environment encodings; its reward and admission thresholds remain specified. Three runs reached up to 25,200 iterations with 20 active pairs (§4.4, PDF p.14). The resulting courses and specialist controllers illustrate finite discovery and transfer. Retirement of active pairs means the result is not one controller retaining every skill.

**Avida proposal:** a driver could maintain several execution environments with bounded resource flows, reaction settings, and permitted event schedules. The driver and archives are part of the selector; the program populations are its material. A different final environment can emerge while the grammar and success rule remain grade 2.

The estimate covers configuration generation, transfers, bookkeeping, and restart handling, using the stock event and save/load interfaces already named. It does not recreate the paper's neural optimizer. First cross-test saved programs across candidate worlds. In subsequent matched transfer/no-transfer conditions, absence of additional retained behavior on unused input probes would count against the proposed role of transfer. A rotation through already-paid tasks is not by itself cumulative capability growth.

### Enhanced POET

**Checked [R5], §§3–4, 6–7:** Enhanced POET characterizes a world by clipped, rank-normalized scores of current and archived controllers. Their changing collection therefore changes the reference for novelty. It also expands terrain generation and modifies transfer handling. Runs use 60,000 iterations and 40 active environments (§6); the paper reports continued challenge creation within that horizon and specialist behavior. Its discussion anticipates an eventual physical-domain ceiling.

**Avida proposal:** replace direct distance between world settings with distance between their cross-evaluation score vectors. This is grade 2: changing the reference collection does not remove the score, transformation, distance, or admission rule. The table gives an increment to the POET driver, with no C++ required for this restricted stock-world matrix. A new world language is a separate implementation, not supplied by the matrix.

Claude could recompute novelty using a frozen reference collection and compare it with the changing collection. If novelty arises chiefly from reference turnover or noisy tests, while independently reproduced capabilities remain unchanged, that counts against the intended interpretation. Archive size multiplies cross-evaluation cost. Recovery from archived specialists and retention in currently executing programs need separate records.

### PAIRED

**Checked [R6], §§4–5:** PAIRED rewards an environment generator for a return gap between a reference agent and the learner on the same environment. The implementation estimates that gap from rollouts. It retains learned policies rather than requiring a novelty archive. Maze results span five seeds beyond 350,000 axis-labelled training steps in Figure 2, PDF p.8; these are not a checked count of environment interactions. The curves are nonmonotonic, and held-out maze transfer is tested. Neither result supplies indefinite retention.

**Avida proposal:** retain two changing program populations and select bounded execution-environment settings exposing a reproducible performance gap. The reference program population must continue searching to preserve the mechanism. This is a driver analogue, not the original training algorithm. Both the return and the gap calculation make it grade 2.

The table's driver estimate uses stock resource/reaction controls and program reseeding; no new source file is required. First score saved program populations on identical proposed worlds, then repeat with equalized evaluation budgets. A gap caused entirely by denying the learner processor time, or by alternating losses of familiar behavior, would count against capability accumulation. Reference success suggests feasibility for that case; reference failure does not identify an impossible world.

### OMNI

**Checked [R7], §§3.2–3.3, 4.3, 5.1–5.6:** OMNI combines learning progress with a pretrained model's judgement of interesting tasks. The finite-task studies run for 100 million steps across ten seeds. In AI2-THOR, GPT-4 generates tasks and completion-checking code. After one million steps across ten seeds, the median is 13 tasks meeting a 0.6 success threshold, with a 95% bootstrap interval of 11–17 (§5.6, p.12). Evaluation uses tasks each treatment previously sampled, not one common complete task set.

**Avida proposal:** a model could choose among existing world settings from logged performance histories. This remains grade 2, including when a model generates the checker. Prompts, pretrained knowledge, task grammar, state access, and success tests constrain selection. The table's driver cost includes the interest/progress manager and excludes model-call charges.

New predicates on captured traces can be evaluated in the driver. Installing them as live reactions would touch `cTaskLib.cc/.h` and `cEnvironment.cc/.h`; the C++ estimate assumes a restricted evaluator, not unrestricted generated code. Claude could first replace descriptive task names with neutral identifiers. Choices driven by labels without expanding independently tested behavior would count against the proposed role of interestingness. Whether the model's human-derived history belongs in the knowledge account remains open.

### Learning progress and intrinsic motivation

**Checked [R8], §§IV, VI-D:** Intelligent Adaptive Curiosity stores experiences, divides a chosen sensorimotor space into regions, maintains predictors and error histories, and selects actions associated with local learning progress. Figure 4 illustrates a 5,000-step sequence moving between learnable regions while avoiding an unpredictable region (printed pp.273–274). This is a finite learning sequence, not a long-term capability-retention result.

**Avida proposal:** put the predictor and history in the execution environment. It could allocate program-search time to regions where measured prediction or competence changes. A stock-task approximation changes resources or rewards using `EnvironmentActions.cc`. A raw-trace version uses the supplied patch and an external model; a live raw-trace version could add 600–1,500 C++ lines around trace collection and the merit hook. The common choices—observations, loss, model capacity, partitions, window, and allocation rule—keep it grade 2.

Claude could first train on earlier saved traces and test on untouched later probes. Resetting the predictor provides a rival explanation: repeated relearning can produce apparent progress. Progress vanishing on fresh inputs, or consisting entirely of forgotten behavior being reacquired, would count against cumulative learning. A stationary progress score of zero can also accompany retained mastery; it is not automatically a failure.

### Schmidhuber's artificial curiosity and compression progress

**Checked [R9], §II-A–B and §III:** compression progress compares old and new models on the same recorded data, allowing for model and residual description costs. Prediction error alone can reward persistent unpredictability; reduction in error is a different drive. The formal account does not itself report a run showing unlimited accumulation. **Checked [R10], “Experiments”:** the 1991 curiosity experiment uses a 100-state world with deterministic and random reactions and reports predictive learning; that section supplies no training horizon.

**Avida proposal:** favor programs whose traces enable the selector's adaptive model to reduce description cost. The selector stores observations and model versions. It remains grade 2 because the encoding, model family, training allowance, and progress computation are specified. Compressing each trace independently with an unchanged compressor measures compressibility, not this learning-progress mechanism.

The driver estimate assumes an existing model library and the supplied tracing patch. Live selection adds trace and merit integration in `PopulationActions.cc`, `cPopulation.cc`, and possibly `cEnvironment.cc`; model training is extra compute. Compare old/new models on identical frozen data. Persistent rewards from noise, file order, or forgetting cycles would count against the translation. Increasing predictability of the selector's observations must still be distinguished from increasing capabilities of the programs.

### Empowerment

**Checked [R11], §2.2 and §§3.2–3.3:** empowerment measures the capacity of the channel from actions to later sensed outcomes. The study searches sensor and actuator arrangements using a causal model. Sensor searches use at least ten runs of 1,000 generations; actuator searches use ten such runs (printed pp.132–133). These finite configuration searches do not demonstrate a continuing stock of new capabilities.

**Avida proposal:** because the execution environment is the selector under test, define its actions as interventions on program allocation or world settings and its observations as subsequent program-population behavior. This relocation is explicit: merely rewarding each program's own empowerment would test a different arrangement. Counting distinct outputs without interventions does not identify controllable alternatives.

Intervention vocabulary, observation resolution, time horizon, and estimator make this grade 2. The driver estimate covers controlled branches from saved program populations; all branches must share the reconstruction procedure. New causal action channels could add 500–1,500 C++ lines in `cEnvironment.cc/.h`, `cPopulation.cc`, and relevant hardware. Claude could begin with a small intervention set and repeated outcomes. If the entire score gain comes from controlling program-population size or copying inputs, while computational capabilities remain fixed, that counts against its proposed use here. Rollout costs grow with the number and depth of interventions.

### Quality diversity and MAP-Elites

**Checked [R12], §§3, 7, 9.3:** MAP-Elites partitions a designer-selected feature space and stores a quality-scored representative in each cell. The checked source is explicitly a preliminary preprint. Its retina study reports 20 replicates, 10,000 iterations, and batches of 2,000 evaluations (§9.3, PDF p.11). I do not convert this into a total because initialization is separate. The paper discusses the limitation imposed by its chosen feature space. Stored representatives provide a repertoire, but replacement need not preserve unmeasured properties.

**Avida proposal:** cells could describe repeatable output behavior or input-order sensitivity; quality could be replication performance or another declared criterion. This is grade 2, with grade 1 added by named-task quality rewards. It is not objective-free: quality remains explicit.

The driver estimate covers archive admission and reseeding. Live integration would use `PopulationActions.cc`, `cPopulation.cc`, and archive storage. First ask whether saved programs occupy cells representing distinct reproducible behavior. Filled cells distinguished only by delays or unstable output, or replacement programs losing earlier tested capabilities, would count against the repertoire's intended role. Test preservation in the archive separately from active execution.

### Host–parasite coevolution in Avida

**Checked [R13], Results and Discussion; Materials and Methods:** parasite programs infect host programs sharing a logic function and take processor time. Fifty coevolution runs extend to 500,000 updates. EQU appears in 17 of 50, versus none without parasites; parasites disappear in 12 coevolution runs. Community diversity retains past interaction pressures, but the experiment permits nine named logic functions. Starting host programs already perform NOT. Changing interaction partners therefore supplies grade-2 pressure within a fixed task vocabulary, not grade 3.

**Checked source [R20]:** current heads hardware implements `cpu/cHardwareCPU.h::ParasiteInfectHost` as an immediate failure. Stock parasite execution is available in `cpu/cHardwareTransSMT.cc`, with a compatible included fixture in `avida-core/tests/parasites_log_injections/config/`. The fixture was read, not executed. Reusing the present heads program populations as hosts is not a configuration toggle.

**Avida proposal:** the table's zero-C++ route starts a separate compatible hardware/instruction/ancestor setup. Its costs include configuration and checking, not conversion of saved heads programs. Any preservation of the task-free starting condition needs its own bootstrap test. First test whether infection works and persists in that setup. Parasite disappearance, repeated familiar task cycles, or failure to retain new behavior would count against the intended use. A 500,000-update comparison has a different compute scale from a 50,000-update pilot.

### Prediction and anticipation in digital evolution

**Checked [R14], §§3–4:** Avida programs evolved timed sleep and preparation for resource return under a designed periodic resource schedule, named tasks, and added sensing/time/sleep instructions. Anticipatory sleep is reported in 37 of 50 diminishing-resource runs. The schedule has 500 days of 256 updates per year and sixteen annual reductions to zero resources (§3). That implies 2,048,000 updates to sixteen reductions, not a checked final stopping time. This paper defines an update as about one executed instruction per program, so its units cannot be directly costed from the brief. **Checked [R15], “The Behavioral Task,” Table 2:** Avida navigation studies include path prediction and associative/reversal learning under explicit trail-following scores and cue manipulations. The total run horizon could not be checked in the accessible main text; the supplement was inaccessible. These are selected behaviors, not an autonomous environment inventing its own success standard.

**Checked [R16], published pp.7, 9, 15:** on the adjacent Markov Brain platform, explicit one-step predictive-information bonuses were combined with task scores over 10,000 generations and 128 repeats. The tested prediction bonuses impeded finding fully successful task solutions. This does not test all forms of prediction, and it is not an Avida result.

**Avida proposal:** an explicit forecast drive should record a prediction before revealing the next datum, then compare it with the later observation. This gives grade 2 even if the actual datum is not known in advance. Checked source [R20]: `SetEnvironmentInputs` accepts three numbers with restricted ordered high bytes; it is not an arbitrary streaming protocol. A driver can first score forecasts from fixed history windows using the supplied patch. The C++ estimate is for a continuing live stream: input/output ordering, forecast state, and reward handling in `cEnvironment.cc/.h`, `cOrganism.cc/.h`, `cTaskLib.cc/.h`, and possibly `cpu/cHardwareCPU.cc`; it is not a reimplementation of all historical experiments.

Claude could first inspect traces for copying, fixed-cycle timing, and data leakage. Randomize phase and break cue–future relationships while preserving marginal frequencies. Apparent forecasting that survives only through exposed future data, or produces no retained behavior beyond a schedule, would count against the intended carry-over.

### Other Avida work: resource-dependent feedback

**Checked [R21], System, Environment, Results, Figures 2 and 4:** Nahum and colleagues use 60-replicate treatments lasting 100,000 updates. Resource consumption reduces returns to common named tasks during the middle phase; the first and final phases share a reference world. The live feedback treatment yields increased final Avida fitness. Replaying another program population's resource history does not reproduce that result, nor does the tested positive-feedback rule. The endpoint is reference-world performance, not an indefinitely expanding repertoire.

**Avida proposal:** grade 2 arises from a written resource/task rule whose current returns depend on use. Resource quantities are a form of world memory, without a learned predictor. Checked source [R20]: `main/cEnvironment.cc::DoProcesses` handles finite resource consumption; `avida-core/support/config/misc/environment-9resource.cfg` supplies a stock example.

The table estimates a bounded resource pilot. A replay control also needs a checked mechanism that replaces endogenous depletion rather than merely adding inflow; budget a further 150–400 driver lines or 200–500 C++ lines in `EnvironmentActions.cc` and `cEnvironment.cc`. Claude could first inspect existing resource histories and replay feasibility. Matching gains under live feedback and replay, or transient gains followed by the same retained repertoire, would count against the relevant carry-over claim. This does not predict P1's outcome.

### Other Avida work: changing rewards and plastic behavior

**Checked [R17], §§2.2–3:** fluctuating Avida environments reward one subset of six named logic functions and penalize the other, then reverse those roles. Sensory instructions allow responses to the current state. Each experiment has two phases of 200,000 updates. A later condition adds 71 other explicitly named, continuously rewarded functions (§2.2). The paper reports that adaptive plastic behavior can stabilize digital evolution in changing conditions. This concerns adjustment within a specified menu, not continuing invention of new success criteria.

**Avida proposal:** stock events can vary reaction values or resource flows using `EnvironmentActions.cc`; the instruction-set configuration must actually expose the required sensing behavior. The table estimates configuration and checking work, with no C++ for that restricted schedule. A driver that chooses when to switch would add state and a specified grade-2 policy. Resource depletion can likewise make rewards depend on other programs while still using named reactions. Neither mechanism alone escapes grades 1/2.

An initial option is to inspect retained behavior across schedule phases in existing populations. Stable switching among a closed repertoire would count against the claim that changing pay alone continues producing new capabilities. Conversely, reduced instruction-sequence turnover is not by itself evidence of failure: the retained programs may already respond to both contexts. The outcome must be assessed at the capability level the owner asked about.

### POWERPLAY: self-generated tasks with retention checks

**Checked [R18], §§2–3.3:** POWERPLAY searches jointly for a task and a solver modification, accepting when the changed solver handles the addition while retaining previous solutions and the earlier solver cannot handle the addition. Task descriptions include success procedures; dependency records can associate solver components with tasks. **Checked [R19], §4.3, Figure 4:** an illustrative eight-hour run produces 67 new action sequences; its 340-task total also includes compression tasks. These are not 340 distinct new behavioral capabilities.

**Avida proposal:** maintain a task archive and test prospective additions and retained performance using bounded execution. Grade 2 follows from the task language and success checker. The table's driver estimate assumes a restricted task grammar and the supplied tracing patch; a new evaluator could add 500–1,200 C++ lines in `cTaskLib.cc/.h` and `cEnvironment.cc/.h`.

Claude could first test additions against saved programs with frozen old-task probes. Choosing an archive of specialists rather than one solver changes the retention claim and must be recorded. Accumulating synonymous tasks, compressions counted as new capabilities, or regression tests that no longer cover the earlier behavior would count against the intended claim. This literature does represent explicit problems; that fact must not be erased when identifying what remains missing.

## Where the literature has nothing

Within this checked set, I found no demonstrated selector meeting the brief's grade 3, and no demonstrated Avida execution environment that maintains explanatory problems, directs a criticism at a particular claimed part, and revises its selection standard on that basis. This is a bounded search finding, not a claim that no such work exists or could exist. Coverage followed all requested research lines, their primary papers, and targeted Avida anticipation/learning searches; it is not an exhaustive census through 2026.

The narrower gaps matter. POWERPLAY holds executable tasks and component dependencies; MCC and POET hold changing challenges. Those are counterexamples to “the literature has no problem representation.” A failure score or a dependency trace, however, does not supply an articulated account of why a proposed explanation fails. That missing account is not supplied by renaming a penalty “criticism.” [R3–R5, R18, checked; distinction is this report's interpretation.]

Likewise, prediction and anticipation are present in the checked literature. What remains absent here is evidence that paying for prediction, by itself, gives this Avida selector an indefinitely expanding retained repertoire or a grade-3 standard. Existing demonstrations and the negative predictive-information result constrain that extrapolation without settling it. [R14–R16, checked.]

## Shared assumptions

Not all methods require a hand-designed behavioral distance: MCC uses relational eligibility, and PAIRED uses returns. What they share in the checked implementations is an operational rule for selection, an admissible interaction space, and finite resources. Some representations change during the run, but the permitted changes and acceptance machinery still matter. This is the reason for the grade assignments, not an argument that every conceivable artificial selector must use an explicit solution checker.

The hard-to-vary audit keeps the owner's question and grades **fixed**. Transport from robots or neural controllers to an Avida execution environment is **borrowed** from those mechanisms and remains **unknown** until tested. Specific descriptor distances, progress windows, and archive sizes are **loose design choices** unless a stated test distinguishes them. Lasting additional capability is **unknown** wherever the paper reports discovery, a transient score, or an archive without retesting old behavior.

Three changes discriminate interpretations. Remove or freeze selector memory while retaining the same evaluation budget. Swap adaptive world changes for replay of an earlier world's schedule. Change unused input instances and order while retaining the declared problem class. These are proposed tests, not performed interventions. If memory removal leaves the claimed accumulation unchanged, memory is not needed for that observed effect; if replay reproduces it, a changing feedback loop has not yet been isolated.

Novelty and retention can pull in different directions; a strict eligibility gate can also suppress stepping stones. Archive growth, score growth, and processor allocation are therefore inadequate substitutes for repeated capability checks. The evaluation probes are this report's added way to discriminate hypotheses, not a definition of knowledge. Probe results should not quietly become training rewards, and a revised probe set must be recorded as a new test.

## Options for Claude

No option below is a run decision. The table gives prototype engineering costs; additional test code could require roughly 150–500 lines for a bounded driver and 250–800 for a live C++ integration. These are planning allowances, not measurements. Model training, cross-evaluation, instrumentation, and historical-data compatibility are additional work.

| Option | What could be tested first | Cost and boundary |
|---|---|---|
| Novelty, MCNS, MAP-Elites | Score saved programs; inspect repeatability, archive cells, and whether a minimum criterion has qualifying descendants | Driver costs above; no new evolutionary run needed initially. Trace route assumes supplied patch |
| MCC | Cross-test a small saved program set and declared challenge set before changing either queue | Driver plus interaction matrix; cost grows with programs × challenges × repeats |
| POET / Enhanced POET | Try saved-program transfers; compare direct world descriptors with performance-vector descriptors | Three worlds × three seeds × two conditions × 50,000 updates gives about 18 baseline CPU-hours, plus cross-tests |
| PAIRED | Test gaps with two changing program populations and identical world/evaluation budgets | Two populations × three seeds × two conditions × 50,000 updates gives about 12 baseline CPU-hours, plus generator evaluation |
| Progress, compression, OMNI | Replay traces with old/new models; compare forgetting, raw error, and progress; optionally vary task descriptions | Driver and model compute first; a three-seed, two-condition 50,000-update comparison gives about six baseline CPU-hours plus model costs |
| Empowerment | Branch the same reconstructed population under a small intervention vocabulary | Driver plus repeated rollouts; no justified single multiplier from the supplied timing |
| Host–parasite | Check compatible hardware, successful infection, and persistence before long search | Separate stock setup; three seeds × two conditions × 500,000 updates would be about 60 baseline CPU-hours only if the brief's timing scaled unchanged; it may not |
| Resource feedback | Compare live depletion with a recorded schedule that cannot respond to the current program population | Stock pilot costs above; replay needs the separate integration allowance. Three seeds × two conditions × 100,000 updates gives about 12 baseline CPU-hours |
| Forecasting / fluctuating worlds | Inspect cue ordering and leakage; compare intact versus disrupted temporal relationships | Forecast protocol estimate above, or stock schedule setup. Calibrate runtime before extrapolating |
| POWERPLAY | Test one genuinely additional task and retention of frozen old behavior | Driver, task search, and repeated regression evaluations; archive testing cost grows unless dependencies safely limit it |

All CPU estimates are arithmetic from the owner's one-CPU-hour reference for 50,000 updates, not measured runtimes here. Keep at most three Avida processes concurrent on the stated four CPUs; total CPU-hours are not elapsed hours. Match restarts, world sizes, instruction-change rates, and total evaluation effort unless one is the declared intervention. Deliberately vary memory or archive access in the corresponding ablation, with the remaining budgets matched. Retain raw traces, selector decisions, and distinct records of active and archived capabilities. If a no-task ancestor cannot pass a proposed gate, record that failure before supplying a qualified starting program. Any supplied seed should be shared with the comparator, with its earlier search history disclosed.

## Reference list

**R1 — checked.** Joel Lehman and Kenneth O. Stanley (2011). *Abandoning Objectives: Evolution through the Search for Novelty Alone*. Evolutionary Computation 19(2), 189–223. [DOI](https://doi.org/10.1162/EVCO_a_00025). [Opened author manuscript](https://www.cs.swarthmore.edu/~meeden/DevelopmentalRobotics/lehman_ecj11.pdf), especially §§3, 5–6, 9.1; PDF pagination differs from journal pagination.

**R2 — checked.** Joel Lehman and Kenneth O. Stanley (2010). *Revising the Evolutionary Computation Abstraction: Minimal Criteria Novelty Search*. GECCO '10, 103–110. [DOI](https://doi.org/10.1145/1830483.1830503). [Opened full-paper transcription](https://www.academia.edu/170705424/Revising_the_evolutionary_computation_abstraction), §§3–6; not a publisher PDF.

**R3 — checked.** Jonathan C. Brant and Kenneth O. Stanley (2017). *Minimal Criterion Coevolution: A New Approach to Open-Ended Search*. GECCO '17, 67–74. [DOI](https://doi.org/10.1145/3071178.3071186). [Opened proceedings PDF](https://www.cmap.polytechnique.fr/~nikolaus.hansen/proceedings/2017/GECCO/proceedings/proceedings_files/pap140s3-file1.pdf), §§3–6.

**R4 — checked.** Rui Wang, Joel Lehman, Jeff Clune, Kenneth O. Stanley (2019). *Paired Open-Ended Trailblazer (POET): Endlessly Generating Increasingly Complex and Diverse Learning Environments and Their Solutions*. [Opened arXiv:1901.01753v3](https://arxiv.org/pdf/1901.01753), §§3–4. Conference version: *POET: Open-Ended Coevolution of Environments and Their Optimized Solutions*, GECCO 2019, 142–151, [DOI](https://doi.org/10.1145/3321707.3321799). Numerical claims refer to the opened extended version.

**R5 — checked.** Rui Wang, Joel Lehman, Aditya Rawal, Jiale Zhi, Yulun Li, Jeff Clune, Kenneth O. Stanley (2020). *Enhanced POET: Open-Ended Reinforcement Learning through Unbounded Invention of Learning Challenges and their Solutions*. ICML, PMLR 119, 9940–9951. [Opened proceedings PDF](https://proceedings.mlr.press/v119/wang20l/wang20l.pdf), §§3–4, 6–7 and Appendix A.

**R6 — checked.** Michael Dennis, Natasha Jaques, Eugene Vinitsky, Alexandre Bayen, Stuart Russell, Andrew Critch, Sergey Levine (2020). *Emergent Complexity and Zero-shot Transfer via Unsupervised Environment Design*. NeurIPS 33. [Proceedings record](https://proceedings.neurips.cc/paper/2020/hash/985e9a46e10005356bbaf194249f6856-Abstract.html). [Opened full paper](https://arxiv.org/pdf/2012.02096), §§4–5 and appendices; Figure 2 inspected as an image.

**R7 — checked.** Jenny Zhang, Joel Lehman, Kenneth Stanley, Jeff Clune (2024; preprint 2023). *OMNI: Open-endedness via Models of human Notions of Interestingness*. ICLR 2024. [Publication record](https://openreview.net/forum?id=AgM3MzT99c). [Opened primary text, arXiv:2306.01711v3](https://arxiv.org/abs/2306.01711), §§3–5; retrieved as raw PDF pages, not an AI summary.

**R8 — checked.** Pierre-Yves Oudeyer, Frédéric Kaplan, Verena V. Hafner (2007). *Intrinsic Motivation Systems for Autonomous Mental Development*. IEEE Transactions on Evolutionary Computation 11(2), 265–286. [DOI](https://doi.org/10.1109/TEVC.2006.890271). [Opened PDF](https://www.pyoudeyer.com/ims.pdf), §§IV, VI-D.

**R9 — checked.** Jürgen Schmidhuber (2010). *Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990–2010)*. IEEE Transactions on Autonomous Mental Development 2(3), 230–247. [DOI](https://doi.org/10.1109/TAMD.2010.2056368). [Opened author preprint](https://people.idsia.ch/~juergen/ieeecreative.pdf), §§II–III.

**R10 — checked.** Jürgen Schmidhuber (1991). *Curious Model-Building Control Systems*. International Joint Conference on Neural Networks, Singapore, vol.2, 1458–1463. [DOI](https://doi.org/10.1109/IJCNN.1991.170605). [Opened author paper](https://people.idsia.ch/~juergen/curioussingapore/curioussingapore.html) and [experiment text](https://people.idsia.ch/~juergen/curioussingapore/node7.html).

**R11 — checked.** Alexander S. Klyubin, Daniel Polani, Chrystopher L. Nehaniv (2005). *Empowerment: A Universal Agent-Centric Measure of Control*. IEEE Congress on Evolutionary Computation, vol.1, 128–135. [DOI](https://doi.org/10.1109/CEC.2005.1554676). [Opened institutional PDF](https://uhra.herts.ac.uk/id/eprint/282/1/901241.pdf), §§2.2, 3.2–3.3.

**R12 — checked.** Jean-Baptiste Mouret and Jeff Clune (2015). *Illuminating search spaces by mapping elites*. Preliminary arXiv preprint 1504.04909. [Opened PDF](https://arxiv.org/pdf/1504.04909), §§3, 7, 9.3. Internally inconsistent physical-arm budgets were excluded from this report.

**R13 — checked.** Luis Zaman, Justin R. Meyer, Suhas Devangam, David M. Bryson, Richard E. Lenski, Charles Ofria (2014). *Coevolution Drives the Emergence of Complex Traits and Promotes Evolvability*. PLOS Biology 12(12), e1002023. [Opened article and DOI](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002023), Results and Discussion; Materials and Methods.

**R14 — checked.** Benjamin E. Beckmann, Philip K. McKinley, Charles Ofria (2007). *Evolution of an Adaptive Sleep Response in Digital Organisms*. ECAL 2007, *Advances in Artificial Life*, LNCS 4648, 233–242. [DOI](https://doi.org/10.1007/978-3-540-74913-4_24). [Opened author manuscript](https://lalejini.com/mercere99.github.io/pubs/2007bBeckmannEtAl.pdf), §§3–4, especially PDF pp.7–8.

**R15 — checked.** Anselmo C. Pontes, Robert B. Mobley, Charles Ofria, Christoph Adami, Fred C. Dyer (2020). *The Evolutionary Origin of Associative Learning*. The American Naturalist 195(1), E1–E19. [Opened publisher text](https://www.journals.uchicago.edu/doi/full/10.1086/706252), “The Behavioral Task,” Table 2, and methods.

**R16 — checked.** Jory Schossau, Christoph Adami, Arend Hintze (2016). *Information-Theoretic Neuro-Correlates Boost Evolution of Cognitive Systems*. Entropy 18(1), 6. [DOI](https://doi.org/10.3390/e18010006). [Opened published PDF](https://du.diva-portal.org/smash/get/diva2%3A1557883/FULLTEXT01.pdf), pp.7, 9, 15; also checked against the [preprint](https://arxiv.org/abs/1511.07962). Published online 25 December 2015, in the 2016 volume.

**R17 — checked.** Alexander Lalejini, Austin J. Ferguson, Nkrumah A. Grant, Charles Ofria (2021). *Adaptive Phenotypic Plasticity Stabilizes Evolution in Fluctuating Environments*. Frontiers in Ecology and Evolution 9, 715381. [Opened article and DOI](https://www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2021.715381/full), §§2.2–3.

**R18 — checked.** Jürgen Schmidhuber (2013). *PowerPlay: Training an Increasingly General Problem Solver by Continually Searching for the Simplest Still Unsolvable Problem*. Frontiers in Psychology 4, 313. [Opened article and DOI](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00313/full), §§2–3.3.

**R19 — checked.** Rupesh Kumar Srivastava, Bas R. Steunebrink, Jürgen Schmidhuber (2012). *First Experiments with PowerPlay*. [Opened arXiv preprint 1210.8385](https://arxiv.org/pdf/1210.8385), §4.3, Figure 4. Published in Neural Networks 41, 130–136 (2013); numerical claims refer to the opened preprint.

**R20 — checked.** Avida development contributors, *Avida source*, commit [47f13dadb547fcf10f620ace60247f38b30b8b16](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16), inspected 1 October 2026 UTC. [Population handling](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cPopulation.cc), [world events](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/actions/EnvironmentActions.cc), [division checks](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cOrganism.cc), [heads hardware](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/cpu/cHardwareCPU.h), and corresponding TransSMT, configuration, action, and save/load files named above. Publication year is not applicable to a pinned source tree.

**R21 — checked.** Joshua R. Nahum, Jevin West, Benjamin M. Althouse, Luis Zaman, Charles Ofria, Benjamin Kerr (2017). *Improved Adaptation in Exogenously and Endogenously Changing Environments*. Proceedings of the 14th European Conference on Artificial Life, 306–313. [Opened author PDF](https://jevinwest.org/papers/Nahum2017ECAL.pdf), System, Environment, Results, Figures 2 and 4.

END OF REPORT
