# The Avida execution environment as an autonomous selector

## Summary for the owner

Checked in the source: Avida already remembers some things. Past task counts and depleted resources can affect payment. It can also test programs on supplied inputs. The proposed missing connection is a record of what the selector expected, what contradicted it, and how that changes its next choice.

For example, the selector could retain the question, “Can this program still do NOT when the input order changes?” It could save two rival programs, retain the cases each fails, and give their descendants another opportunity. That combines memory, a standing problem and protected alternatives. The question and its acceptance rule would still be named in advance.

The additions below are options for testing particular functions of an autonomous selector. They are not conditions that every autonomous agent must meet. None of the proposed working designs reaches grade 3 under the brief’s definition.

I checked the requested source commit and ran source-extraction and arithmetic checks. I did not run Avida: configuration stopped because CMake is unavailable. The proposed experiments, driver and patches remain unrun. No conclusion here decides what knowledge is or which costly experiment the owner should commission.

## Table

Every addition and test in this table is a proposal. “Stock + driver” means new external decision code using stock facilities, not an existing autonomous-selector feature. Source keys refer to the checked references in the final section.

| What the agent has | What Avida has now | Smallest addition | Stock or C++ | Named in advance, and grade | Test | What counts against |
|---|---|---|---|---|---|---|
| Memory used in selection | Checked E/P: task history, resource state and counts affect reactions | Persistent selection and failure ledger consulted before allocating another trial | Stock + driver | Record identity, replay rule, task domain and budget; grade 2, with grade-1 tasks underneath | Retained versus erased history | Erasure leaves choices and repeated failures unchanged |
| Model of candidates | Checked A/T: test execution gives measured behavior | Candidate-specific predictions for inputs not yet tried | Stock + driver | Prediction language, evidence scope, revision rule; grade 2 | Predictive versus table-only selector | Predictions fail withheld cases or are never used |
| Choice of next test | Checked A/I: supplied-input analysis; constrained live-input event | Choose an unanswered case that separates rival predictions | Stock + driver; optional live C++ | Input family, disagreement rule, tie rule; grade 2 | Adaptive versus fixed test order | Same discoveries at equal test cost; persistent missed failures |
| Standing problem | Checked O: fixed division requirements; no problem record in that path | Persistent question with counterexamples and explicit closure conditions | Stock + driver | Question, closure and reopening rules; grade 2; named operation grade 1 | Persistent versus expiring question | False closure or no effect of persistence |
| Criticism aimed at a part | Checked A: traces and instruction ablation, assessed through Avida fitness | Failed-case record linked to controlled instruction interventions | Stock + driver | Intervention set, comparison and failure rules; grade 2 | Targeted versus budget-matched shuffled interventions | Alleged repair fails replay or also breaks protected cases |
| Expectation and surprise | Checked E/T: scoring and test execution, not a forecast-discrepancy loop in these paths | Commit prediction before observation; contradiction opens a retest | Stock + driver | Prediction representation, discrepancy and response rules; grade 2 | Discrepancy-triggered versus scheduled retests | Quiet controls trigger repeatedly; contradictions do not change choices |
| Rivals for one problem | Checked S/J: save, load and inject programs | Problem-indexed archive with explicit trial opportunities | Stock + driver | Rival identity, capacity, retention and re-entry rules; grade 2 | Two rivals versus one; same storage and trial budget | Rival is never usable again or adds no retained capability |
| Findings that alter selection | Checked J/E: injection and reaction-value changes | Connect a recorded finding to the next material allocation | Stock + driver | Intervention, dosage, timing and resource budget; grade 2 | Finding-dependent versus replayed interventions | Effects follow intervention schedule regardless of findings |

## Memory of what it selected

**Agent function.** In the software-testing sense used here, remember which candidate was tried, under which conditions, and why it was retained. The record must affect a later choice; writing a log alone does not supply this function.

**Avida now.** Checked E: `cEnvironment::TestOutput` receives task counts, reaction counts and resources, calls `TestRequisites`, then `DoProcesses`. Checked P: `cPhenotype::TestOutput` updates counts and accumulated bonuses. Thus “pay depends on the present output only” is too broad. The missing proposal is explicit, cross-episode memory of selection decisions and counterexamples. This narrows S117’s “all choosing” claim: the specified task checker is only part of the execution environment’s selection machinery.

**Smallest addition.** A driver stores candidate sequence plus instruction-set identity, input triple and order, execution bound, observed result, selection action and reason. A persistent index prevents the same unchanged candidate receiving another development trial on a case it already failed. Independent audit retests remain permitted. Stock save/load and analyze commands supply material and observations; the decision ledger is new code.

**Naming.** Predefine those fields, exact-identity rule, context invalidation, repetition rule, audit exception and the common test contract below. Grade 2 governs selection; any paid named tasks remain grade 1.

**Test.** Use the common 60 × 60, 50,000-update, 12-seed design. Compare retained history against history erased at each epoch; both retain identical raw audit logs and receive identical trial budgets. Measure repeated failed trials, changed allocations and retained task behavior on withheld inputs. If erasure changes no relevant choice, the ledger has not supplied functional selection memory. Fewer repeated trials without retained behavior supports only an accounting claim.

**Dependency.** None beyond stable identity and measurement. History becomes stale when execution conditions change; re-key it rather than interpreting old failure as permanent inability.

## A model of what it selects among

**Agent function.** In the model-based-control sense used here, write down what a candidate is expected to do before running that case. A stored observation and a prediction about an untried case have different jobs.

**Avida now.** Checked A/T: `BatchRecalculateWithArgs` supplies manual inputs to `cTestCPU::TestGenome_Body`; the latter executes the program. That is a usable simulator, so claiming that Avida has no way to anticipate behavior would be too broad. The examined path does not maintain and criticise a selector’s generalisation across untested cases. This bears on S117’s absent criticism, without denying the simulator.

**Smallest addition.** Store a tentative relation: “candidate C performs task T on every permutation in this input family.” An observed success on one order can generate that conjecture; it does not settle it. Mark untested orders explicitly. Before a probe, record the predicted task result; on contradiction, retain the failed conjecture and either restrict its stated scope or leave the wider claim unresolved. Executing all cases in advance is a separate simulator route whose costs must be counted.

**Naming.** Predefine the candidate identity, task vocabulary, permutation family, conjecture-generation rule, unknown state and revision rule. Grade 2, with named task predicates beneath it. No prediction about arbitrary programs is promised.

**Test.** Common design; compare predictive selection with a selector storing only observed cases. Give both the same execution budget, including simulated forecasts. Measure preregistered prediction errors on withheld cases and ensuing allocations, not agreement on remembered inputs. Include order-sensitive and order-insensitive cases chosen by an independent preliminary assay. If predictions fail withheld cases, that model’s generalisation is challenged. If the table-only control makes the same choices, the proposed predictive representation is unnecessary for that tested job.

**Dependency.** Memory supplies provenance. Test choice supplies an opportunity to catch the model out; neither prediction nor a simulator alone supplies revision.

## Choosing what to test next

**Agent function.** In experimental-design terms, choose an observation that can separate current alternatives, rather than repeatedly asking a question on which they agree.

**Avida now.** Checked I: `Inst_TaskIO` outputs before obtaining the next input; `cPopulationCell::GetInputAt` cycles through its array. Checked A: analyze-mode `RECALC use_manual_inputs` and `TRACE` accept supplied inputs. Checked I: live `cActionSetEnvironmentInputs` requires three inputs with leading bytes 0F, 33, 55 in that order, then resets inputs. Therefore “same test at every output” describes the supplied setup, not all stock facilities. This bears on S117’s fixed human-written tests.

**Smallest addition.** The driver chooses the first untested permutation on which two recorded predictions disagree; if none exists, it cycles through remaining cases. It uses analyze mode between population segments. For live order changes, an optional patch replaces the prefix-order guard with validation that all eight three-bit input patterns occur. Estimate: 30–60 added or changed C++ lines in `actions/EnvironmentActions.cc`. That patch is unnecessary for the external assay and is not implemented here.

**Naming.** Predefine the six permutations, admissible triples, prediction-disagreement rule, fallback, tie order and probe cap. All are grade 2. Choosing within a named family does not make the target unnamed.

**Test.** Common design; adaptive ordering versus fixed cyclic ordering, with the same candidate pool and per-epoch probe allowance. Measure executions until the first reproducible counterexample and errors remaining on an untouched audit panel. Add a case where candidates agree everywhere: the chooser should simply exhaust its declared fallback. If adaptive ordering leaves the same failures undiscovered at equal cost, the claimed testing advantage is unsupported. Repeat with candidate names exchanged: names must not determine discoveries except declared ties.

**Dependency.** Disagreement-based choice needs rival predictions; exhaustive cycling does not. Checked E: `SetupTests` assumes a complete bit-pattern classification when three inputs have been read. Arbitrary triples can violate that assumption. Restrict the assay inputs accordingly; do not mistake a broken test setup for program failure.

## Holding a problem

**Agent function.** In problem-solving terms, preserve an unanswered question through failed attempts and distractions. The question has an identity and remains open independently of the current candidate.

**Avida now.** Checked O: `cOrganism::Divide_CheckViable` consults `REQUIRED_TASK`, `REQUIRED_REACTION` and `REQUIRE_SINGLE_REACTION`. These are standing demands, but this path has no evolving question with attached rival answers and counterexamples. A division gate alone therefore supplies a narrower function than the proposal. This bears on S117’s distinction between an unsolved problem and withheld payment.

**Smallest addition.** A driver record holds the question, open cases, attempted candidates and status. Example: retain NOT across all six orders of a specified triple family. Close it only when a candidate passes the finite closure panel; retain the wording “passed this panel.” Reopen on a reproducible counterexample. An exhausted budget leaves it open.

**Naming.** Predefine the question template, opening trigger, closure panel, reopening rule, budget and priority. The particular failing order may be discovered during execution. The rule selecting such problems is still grade 2; NOT is grade 1. A dynamically filled template is not grade 3.

**Test.** Common design; persistent question versus expiry after one epoch, using the same question-generation rule and compute. A separately scheduled task switch interrupts work at update 20,000 and ends at 30,000. Measure whether the original question returns, whether its counterexamples survive and whether closure withstands the audit panel. An unresolved question disappearing, or closure merely because time ran out, counts against implementation. Equal eventual results with expiry challenge the need for persistence on these cases.

**Dependency.** Memory is needed for persistence. Rivals and a model can be added, but a queue of explicit questions does not require either.

## Criticism with a target

**Agent function.** In debugging terms, connect an observed failure to a specific claim or instruction intervention. “No reward” alone does not explain which commitment failed.

**Avida now.** Checked A: `CommandTrace` records execution; `AnalyzeKnockouts` substitutes a null instruction and compares Avida fitness, including optional pairs. These are existing diagnostic facilities. Their availability corrects an absolute reading of S117’s “nothing criticises”; they do not themselves supply the proposed problem-specific criticism-and-revision loop.

**Smallest addition.** Record a counterexample against the candidate’s prediction, then compare the unchanged sequence with controlled instruction substitutions under that exact case. A driver can generate virtual instruction variants for stock analysis. Report “changing location L changed this output” before claiming that L explains failure. Test replication separately. Null substitution, deletion and substituting a permitted instruction are different interventions and must not be conflated. No real-machine replication code is required.

**Naming.** Predefine the failed predicate, execution bound, substitution set, protected previously passed cases, repair criterion and intervention budget. Grade 2. A script finding a successful substitution has searched a named repair space; calling its output criticism does not change that.

**Test.** Common design; targeted interventions against budget-matched interventions at shuffled locations, with unchanged candidates as controls. Cap each diagnosis at 256 variants; report truncation rather than silently extending it. Measure reproducible output changes, replication, and retained protected behavior. Include a passing program and a program whose failure arises only from a pair of interacting locations. A local intervention that changes global execution length may locate dependence without isolating the cause. Failed replay, lost protected behavior, or equal repair incidence under shuffled targeting counts against the proposed diagnosis mechanism.

**Dependency.** A problem specifies what failed; memory preserves the failed prediction and comparisons. A mechanistic explanation of a repair requires additional evidence beyond the intervention record.

## Expectation and surprise

**Agent function.** In predictive-control terms, a committed expectation conflicts with an observation and changes the next action. Here “surprise” names this functional event, not a feeling.

**Avida now.** Checked E/T: reaction testing evaluates outputs and the test CPU executes candidates. Neither examined path records a selector forecast, compares it with a later observation, and revises a question in response. Task-failure or division-fault messages alone are not that loop. This is the bounded source claim relevant to S117’s surprise finding.

**Smallest addition.** Store the model’s prediction before execution. If observation contradicts it, queue an exact replay. A reproducible contradiction attaches a counterexample and suspends the affected prediction. A non-reproducible discrepancy remains unresolved with execution context attached; do not repeatedly pay for it as “interesting.”

**Naming.** Predefine prediction format, equality rule for task outcomes, replay count, context identity and suspension policy. Grade 2. A reward for prediction error would also be a named rule and could reward persistent error; this design supplies no such reward.

**Test.** Common design; discrepancy-triggered retesting versus the same retest allowance on a fixed schedule. Use an independently specified input-order change and a no-change control. Measure time to a reproducible contradiction, false triggers and the next selection action. Inject a corrupted observation only in the test harness: it should provoke checking, not permanent rejection without replay. If unchanged conditions provoke continuing alarms, or real contradictions never affect selection, the proposed function fails its stated job.

**Dependency.** Requires a model and remembered prediction. Holding a problem gives a place to retain the discrepancy; continuing search needs a material-selection action.

## Keeping rival candidates for one problem

**Agent function.** In search terms, retain alternatives that answer the same question differently and remain available for later trials. Mere sequence diversity does not identify rivals or preserve access to them.

**Avida now.** Checked S/J: population save/load and program injection supply persistence and re-entry machinery. Checked E: reaction processing does not itself assign two candidate sequences to a standing question. Consequently S117’s observations about computational selection do not exclude adding an explicit rival archive outside the programs.

**Smallest addition.** A driver keeps two distinct candidate sequences per open question, their tested behavior and counterexamples. The second candidate must differ on an observed or predicted answer, not merely its filename. A fixed, equal trial allowance keeps both available. The archive is not counted as live program-population diversity.

**Naming.** Predefine rival equivalence, two slots, finite number of questions, admission, eviction, re-entry and trial quotas. Grade 2. Keeping whichever candidate is behaviorally different still names a selection rule.

**Test.** Common design; two problem-linked slots against one slot, while the control stores a second inert copy so storage and injected-cell budgets match. Change which order is probed at update 25,000. Measure recovery of previously demonstrated behavior and actual use of the retained alternative. Include duplicate candidates and a case with no discovered alternative; report the latter as absence of a rival, not success. If the second slot is never used, or re-entry explains the result regardless of its contents, the rival mechanism has not earned the claimed role.

**Dependency.** Requires memory and a shared question. The model can distinguish predicted rivals, but observed disagreement suffices.

## Using findings to change selection

**Agent function.** In control terms, observations must reach an actuator. Otherwise the proposed selector is an observer attached to an unchanged selection process.

**Avida now.** Checked J/E: `cActionInject::Process` injects a selected program, and `SetReactionValue` changes reaction payment. These are existing actuators. The added part is the connection from a particular finding to a particular intervention. This directly addresses S117’s claim about who chooses.

**Smallest addition.** After a probe, a driver chooses which archived candidate occupies a fixed set of trial cells in the next segment. Keep payment unchanged. Log finding, decision, candidate, cells and context before launching the segment. This counts as the execution environment selecting its material; it is not autonomous behavior inside an individual program.

**Naming.** Predefine acceptance rule, exact cell count, cell locations, timing, initial merit policy and equal compute allowance. Grade 2. Any task used to admit a candidate remains explicitly named.

**Test.** Common design; finding-dependent interventions versus a saved schedule from another seed, replayed without consulting current findings. Match intervention counts, cells and timing. Measure resulting ancestry, retained behavior and dependence of actions on findings. If replayed schedules produce the same response, test the intervention itself before attributing the effect to reasoning. If the controller never changes which material receives an opportunity, it has not become a selector.

**Dependency.** A finding needs an identified candidate and observation. Memory, problems and models enrich that finding but are not logically required for every feedback controller.

## Dependency order

The source-corrected question is whether explicit selector state changes subsequent computational selection and retains tested behavior under changed inputs. The owner supplies the seven requested functions and the naming grades. The particular NOT question, budgets, archive rules and finite panels are additions proposed here, not definitions of knowledge.

Stable identity and bounded measurement support memory. Memory supports persistent problems and recorded predictions. Problems plus candidate differences support rivals. Rival predictions support discriminating test choice. Predictions followed by observations support surprise; a failed problem claim plus controlled interventions supports targeted criticism. Findings reach computational selection through an actuator. This is a dependency order, not an ordering of desirability.

Hard-to-vary assessment: the requested functions and grades are **fixed** for this audit. Each proposed implementation is **unknown** as an empirical mechanism until its removal or swap test runs. JSON versus a database is **loose**: either can retain the same state. Direct test execution and a predictive representation are **two routes** to anticipating finite-case behavior, with different costs and scope. The claim that these functions create knowledge remains **unknown**, rather than being smuggled into the experiment’s acceptance rules.

Deleting both memory and the rival archive differs from deleting one: each can preserve information the other loses. They therefore need a joint-removal arm. Preserving every failed case can also consume the entire trial budget. The gauge is the fraction of epochs spent only replaying old failures; a sustained fraction of one means the search function has stopped. An opposite outcome cannot rescue the claim: if more elaborate state yields no changed choices or retained capabilities, rename the result as recordkeeping, not learning.

## The combined design

### Common experimental contract

All individual tests above use 60 × 60 cells, 50,000 total updates, 50 segments of 1,000 updates, and 12 paired seed labels, provisionally 101–112. All arms begin from the same task-free ancestor, use the brief’s instruction-change rates and identical named-task payments. Use the nine-task configuration for this bounded comparison; do not claim it recreates the 77-task runs. For isolation tests, supply other required components identically in both arms. A missing precursor makes the test inapplicable, not a negative finding about the item.

Arithmetic from the supplied S113 ranges: 65−48 = 17, 41−13 = 28, 17−8 = 9, and 8−7 = 1 tasks. These three-seed ranges cannot supply a variance estimate or a powered sample size. Twelve is an explicitly provisional fourfold expansion of the earlier three-seed replication. Report every seed and paired difference; do not turn a small average difference into a general result. The original endpoints measure task breadth, not every measure proposed here. No long-run escape from a plateau can be inferred from this horizon.

At the brief’s nine-task rate, two arms × 12 seeds × one CPU-hour = 24 reference CPU-hours, or eight ideal wall-hours with three Avida processes. Four arms give 48 and 16 respectively. Assays, restarts and altered program lengths add unmeasured cost. These are options, not commissioned runs.

Use at most 256 distinct candidates per epoch, including archive entries; select the non-archive sample by a frozen seeded rule. The development family uses the stock deterministic triple, across its six permutations. Reserve 32 triples generated before the experiment with independent lower 24 bits and the same complete eight-pattern prefixes, each in six orders, for a read-only audit. Do not feed audit results into selection. Interpret task success through the named task predicate, not a particular output position. Report replication separately and treat reaching the execution limit as censored behavior.

### One small combined selector

Combine memory, a standing problem, two rivals and material allocation. A model, surprise trigger and instruction-level diagnosis are optional extensions, not prerequisites for this bundle.

The question is the NOT order-robustness example. After each segment, save the population, sample candidates, assay the development orders, append observations and update the two-slot archive. Admission requires replication and NOT on at least one development order. Fill vacancies by fixed sequence-hash order; the second slot requires a distinct observed pass/fail vector. Retain incumbents unless an all-six pass replaces the first slot as the closure witness. Record all passed and failed cases. If no candidate qualifies, keep the question open and allocate the reserved cells by the same seeded exploration rule in every arm. Do not insert a human-written solution to make the demonstration succeed.

Consult the ledger before filling the assay batch: skip previously failed, unchanged candidate-context pairs and use those slots for untested candidates, up to the 256-candidate cap. Retest incumbents every tenth epoch regardless. The erased-memory arm loses that exclusion history but retains its archive; the one-rival arm retains history but has one usable archive slot. Record actual probe expenditure as well as the common allowance.

Re-enter each available rival in 18 cells, using cells 0–35 as a fixed 36-cell trial region, 1% of the 3,600-cell world. Use stock injection's default merit in every arm. With one candidate, fill both halves with that candidate; with none, use the stated exploration rule. All arms overwrite the same cell locations. The question closes only on all six development orders passing; its finite-panel scope stays attached. Retain closed records and retest every tenth epoch. A timeout never closes it.

Proposed files are `selector.py` for ledger, archive and decisions; `assay.py` for analyze-mode invocation and result parsing; `selector.json` for the frozen contract; `events.template.cfg` for segment save/load and injection events; and append-only `observations.jsonl` and `decisions.jsonl`. Estimated implementation: 350–600 Python lines plus 60–100 configuration lines, excluding tests and any `RUN_BOUNDED` integration. These are estimates, not delivered or tested code. Stock C++ changes: zero for the finite task assay.

Checked S: `LoadPopulation` constructs new programs, calls `SetupInject` and can adjust merit using saved execution offsets. This is not an instruction-state checkpoint. Consequently every arm must undergo the same segment reconstruction, input/resource initialisation, and seed schedule. The resulting experiment tests a segmented execution environment; an uninterrupted-world claim needs a separate live-controller implementation and restart comparison.

The four optional arms are full bundle, erased decision memory, one rival, and both removals. Give every arm identical probe allowances and cell allocations. The last three test whether apparent memory effects are actually archive effects, and whether either substitutes for the other. Measure closed finite problems, audit failures, recurrence of known failures, rival re-entry and program ancestry. If gains vanish under equal probe budgets, occur only through restart effects, or fail withheld inputs, the corresponding interpretation is challenged. Cases where no rival arises cannot test rival retention.

For a bounded-output implementation using Claude’s supplied patch, 50 × 256 × 6 × 10,000 = 768,000,000 virtual instruction cycles is the maximum development-probe allowance per run. It excludes audit and diagnosis. The patch’s interface and exact termination behavior must be read before implementation; they were not supplied here. Stock `RECALC` uses its test-CPU execution rules instead, so that numerical cap cannot simply be asserted for it.

## What no addition can supply

None of these additions supplies grade 3. They specify what counts as passing, retaining, reopening or repairing. Changing which input arrives next does not remove the named rule when code still checks “match the next value.” Allowing a critic to change its scores likewise does not, by itself, remove a named acceptance rule.

This is not a claim that every possible Avida extension must have an explicit solution checker. A different design could let actions change resources or future interactions directly, with consequences rather than a central solution predicate. Its causal rules would still need description. Whether that supplies the owner’s intended changing standard would require a concrete design and test; it cannot be inferred merely from calling the world open-ended.

No finite panel supplies a guarantee about all unseen inputs, indefinite creation of new capabilities, or which programs will eventually be generated. More memory can preserve a mistake; more rivals can preserve redundant candidates; more surprise can spend the budget on noise. Their names supply none of the missing causal evidence.

Whether a human-written task list contributes to the selected programs’ knowledge history remains an owner-level option. One account includes the list’s contribution; another restricts attribution to changes arising during the run. The report does not select either account, define knowledge, or infer that program variation cannot create something new. Source code describes mechanisms; that last philosophical contrast needs a stated criterion.

## What I ran with outputs and what remains uncertain

Work used one agent. Outside-source claims marked **checked** mean direct reading of the pinned source, not execution of the proposed feature. The S113–S118 outcomes and `RUN_BOUNDED` status are supplied by the brief; I did not inspect their raw data or presume P1/P2 outcomes. Field labels above identify the kinds of design being proposed, not empirical claims borrowed from outside publications. No conclusion depends on a source recalled from memory.

### Checked source references

All paths below are relative to `avida-core/source/` at [commit 47f13dadb547fcf10f620ace60247f38b30b8b16](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16).

| Key | Checked file and function |
|---|---|
| E | `main/cEnvironment.cc`: `SetupInputs` at 1252, `TestOutput` at 1314, `TestRequisites` at 1408, `SetReactionValue` at 1877; `main/cTaskLib.cc`: `SetupTests` at 369 and the 77 logic-task methods; `main/cTaskLib.h`: `TestOutput` at 70 |
| P | `main/cPhenotype.cc`: `TestOutput` at 1493 |
| A | `analyze/cAnalyze.cc`: `LoadOrganism` at 168, `LoadSequence` at 211, `LoadFile` at 770, `CommandTrace` at 1725, `AnalyzeKnockouts` at 4483, `BatchRecalculateWithArgs` at 10324 |
| T | `cpu/cTestCPU.cc`: `ProcessGestation` at 144, `TestGenome` at 190, `TestGenome_Body` at 233 |
| I | `cpu/cHardwareCPU.cc`: `Inst_TaskIO` at 4188; `main/cPopulationCell.h`: `GetInputAt` at 214; `actions/EnvironmentActions.cc`: `cActionSetEnvironmentInputs` at 999; `main/cPopulation.cc`: `ResetInputs` at 7434 |
| O | `main/cOrganism.cc`: `Divide_CheckViable` at 788; `main/cAvidaConfig.h`: division-task configuration near 399 |
| S | `actions/SaveLoadActions.cc`: `cActionLoadPopulation` at 54 and `cActionSavePopulation` at 138; `main/cPopulation.cc`: `SavePopulation` at 6362 and `LoadPopulation` at 6820, especially reconstruction near 7018 |
| J | `actions/PopulationActions.cc`: `cActionInject` at 84 and its `Process` method |

### Execution record

I cloned `https://github.com/devosoft/avida.git`, checked out `47f13dad`, initialised its pinned submodules, and inspected the files above using `rg` and `sed`. `git rev-parse HEAD` returned:

```text
47f13dadb547fcf10f620ace60247f38b30b8b16
```

I attempted configuration with:

```sh
AVIDA_DISABLE_BACKTRACE=1 cmake -S avida-source -B avida-build -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5
```

Its diagnostic was:

```text
/bin/bash: line 1: cmake: command not found
```

No executable was built and no Avida simulation or proposed selector was run. I also ran `python3 checks/source_checks.py`. It extracted the nine standard logic methods and every `Task_Logic3in_*` method from `cTaskLib.cc`, collected their literal `logic_id == integer` cases, checked input-pattern coverage for all permutations of `(0x0f13149f, 0x3308e53e, 0x556241eb)`, and calculated the stated spreads and budgets. Exact output:

```text
logic_task_functions = 77
accepted_logic_ids = 251
excluded_logic_ids = [0, 170, 204, 240, 255]
complete_bit_patterns_per_permutation = [8, 8, 8, 8, 8, 8]
S113_spreads = [17, 28, 9, 1]
two_arms_twelve_seeds_reference_CPU_hours = 24
four_arms_twelve_seeds_reference_CPU_hours = 48
reference_wall_hours_at_three_processes = (8.0, 16.0)
fifty_epochs_256_candidates_6_tests_10000_cycles = 768000000
```

This is source extraction and arithmetic, not a behavioral Avida result. Missing evidence includes the saved program populations, original configurations, the bounded-output patch, predictive usefulness, targeted-repair effects, restart interactions and actual compute costs. The proposed sample size has no power calculation. A bounded next option is to run the stock supplied-input assay on one saved order-sensitive program and one order-insensitive program, preserving first outputs, before deciding whether to commission any population experiment.

END OF REPORT
