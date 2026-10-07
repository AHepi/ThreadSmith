# Temporal selector for the Avida execution environment

Prepared for Aza on 2 October 2026. Design v1.2; runnable code and observed outputs follow the report. “Checked” means the cited file or source was opened; it does not turn a reported claim into a replicated result.

## 1. Summary for the owner

This design gives the Avida execution environment a small memory that changes what it pays. For example, if a capability becomes common but fails when inputs arrive in another order, a latch keeps that problem open. Two successful population assays release the latch and trigger a short rebound. Other units respond to recent activity, capabilities occurring in the same program, and their order of appearance. The Python components have been exercised; the execution record below distinguishes those checks from Avida runs. This remains grade 2: people supply the detectors, equations and constants. It prevents the earlier selector’s pay from disappearing when progress stops, but it cannot guarantee continuing progress or unnamed goals.

## 2. The units

The clock advances once per 1,000-update piece. All state starts at zero; the first piece receives equal pay across eligible tasks. The assay after piece t determines pay for piece t+1. These are proposed engineering constants, not estimates of biological timescales.

For saved instruction sequence g, let n_g be its number of active copies and N their total. Let x_goj indicate that capability j was recorded during the cold-start assay in input order o. Define z_gj=product over the six x_goj, p_j=sum(n_g x_g0j)/N, q_j=sum(n_g z_gj)/N, and c_jk=sum(n_g z_gj z_gk)/N. Thus q counts the same programs succeeding in every order. Taking the minimum of six population shares would allow six different specialists to masquerade as one robust program. A capability is common at a share of at least 0.10.

K=77 detectors retain the order in stock `environment-all-logic.cfg`. Zero-based indices congruent to 6 modulo 7 form eleven withheld detectors H. The remaining 66 form E. H is used for measurement only: neither its outputs nor its coincidence or sequence signals enter the policy. This arbitrary split is declared before any population trial; it makes the never-paid measure nonempty without naming an additional function. It changes the experiment from paying all 77 and therefore requires its own matched controls.

Below, a_T=exp(−1/T); unprimed state is from the previous assay and primed state is the new state. Equations apply to E. Every policy is **grade 2**, acting through **grade 1** named task detectors and instantaneous payment lists. None is grade 3.

| Unit | Equation and timescale in pieces | What it reads and how it affects selection |
|---|---|---|
| Decaying trace | h′_j=a_4 h_j+(1−a_4)q_j; τ=4 | Recent robust shares. Supplies adaptation, loss detection and expectation. |
| Adaptation | A_j=0.1+1/(1+8h′_j); inherits τ=4 | High trace suppresses its raw pay term; a fading trace restores it. With other raw terms fixed, this reduces its relative pay. |
| Bistable latch | When off, set L_j if p_j≥0.10 and q_j<0.02, or (q_old,j≥0.10 or h_j≥0.10) and q_j<0.02. When on, clear only after two consecutive q_j≥0.10 assays. | Reads current order fragility or loss of previously common robust capability. Adds L_j to its raw score. Persistence has no decay or timeout; clearance dwell is two pieces. |
| Rebound | R′_j=a_2 R_j+1[L_j=1 and L′_j=0]; τ=2 | Adds 0.5R′_j after population-associated resolution. It is a pulse relative to the no-rebound control; total pay can still decline when the larger latch term disappears. |
| Coincidence | C′_jk=a_2 C_jk+(1−a_2)c_jk, j≠k; C_jj=0; τ=2 | Adds 0.5 max_k C′_jk to j. Reads two robust capabilities in the same program. Payment remains to the individual tasks, so separate specialists can also receive it. |
| Sequence | e_j=1[q_old,j<0.10≤q_j]; d_j=a_3 r_j; S_j=e_j max_(k∈E,k≠j)d_k; r′_j=1 if e_j else d_j; τ=3 | Adds 0.5S_j for a newly common capability following another’s recent crossing. Uses old traces before setting new ones. Simultaneous first arrivals and self-pairs produce no sequence response. No particular A or B is privileged. |
| Expectation | qhat_j=clip(2h_j−h_previous,j,0,1); Z_j=abs(q_j−qhat_j) | Adds 0.5Z_j. Predicts the next robust share from the previous two traces, before seeing that share. One-piece forecast horizon, τ=4 inherited from traces. This is forecast error, not an explanation of a program. |

The raw score is w_j=A_j+L′_j+0.5(R′_j+max_k C′_jk+S_j+Z_j). Pay is b_j=18w_j/sum_(k∈E)w_k for E, and zero for H. Stock reactions use b as a log2 merit bonus with a one-performance limit. The nominal sum is always 18. Equal offered log-pay does not equal equal earned processor time. Global normalization means a component can rise while its final pay falls because other components rise more.

With 77 detectors the dense coincidence matrix stores 5,929 numbers; the seven remaining vectors store 539 entries. This is a bounded controller state. The population assays, not these updates, are expected to dominate cost; no efficiency comparison was run.

The latch names an observable condition, not a conjecture or criticism. It can remain open indefinitely. Fixed-world task rewards do not distinguish two programs with equal world-order task outputs but different cross-order robustness. Consequently, changing these rewards might not resolve the held problem. A future opportunity filter could explicitly select robust programs, but would add a direct grade-2 gate and is not silently included here.

## 3. The instinct, and what is still named

The proposed instinct is a persistent response pattern: reduce attention to sustained capability, retain unresolved losses, react to release, and change attention when capabilities co-occur or arrive in sequence. It applies the same equations to every eligible detector. Temporal state belongs to the selector, not to a claim that an Avida program has gained temporal computation.

People still name the 77 detectors, the eligible class, the withheld split, the meaning of a problem, commonness and loss thresholds, six assay orders, sampling clock, initial state, coefficient 8, budget 18, other gains and all timescales. Even the criterion for latch resolution is fixed code. A changing payment list is not a changing standard in the brief’s grade-3 sense.

Whether a human-written detector list counts in the history of the programs remains an owner choice. It can be counted as inherited structure, or reported separately as external scaffolding. Whether “knowledge” means retained tested behavior or requires conjecture and criticism also remains open. One can call these fixed dynamics an instinct operationally; a requirement that instincts themselves change would demand another experiment. No definition is decided by the present code.

## 4. What is new against replies 02 and 04

Checked in the supplied brief, rather than independently rerun: reply 02 used progress or rarity, and reply 04 proposed a ledger, questions and rivals. This implementation adds several interacting timescales, persistent unresolved state, release pulses, same-program coincidence, ordered threshold crossings and a forecast-error readout. The saved selector state survives Avida restarts.

No rise in capability is needed to issue pay: A_j≥0.1, so the payment denominator cannot become zero. This addresses reply 02’s disappearing-pay mechanism without introducing a rescue function. It does not prevent a stationary schedule, oscillation, loss of capabilities or an eventual count plateau. Paying unfamiliar eligible detectors still draws from a human-written class.

The stronger claim is frozen as follows: population-conditioned history may sustain acquisition of robust capabilities over 50 pieces relative to state erasure and externally supplied schedules. The code’s temporal response is a separate, narrower claim. A timer-and-state-machine implementation can reproduce these responses; the neuron analogy adds no computational class. Checked: the attached report makes this distinction, and the opened sequential-logic reference describes circuits with memory. The biological studies in that report were not re-audited here.

## 5. Files

The code appendices provide `selector.py`, `runner.py`, `assay.py`, `summarize.py`, component checks and the independent challenge script. Save each fenced block under its displayed relative path, preserving the `temporal_selector` directory. The runner generates the exact `avida.cfg`, reaction environment, events and analyze scripts, recording the seed and applied pay for each piece. It uses stock support files from the pinned checkout; it does not depend on the earlier patched `RUN_BOUNDED` command.

The environment template retains all 77 task detectors, including zero-pay withheld detectors. Each reaction has the form `REACTION R0 not process:value={b0}:type=pow requisite:max_count=1`. No resource pools are defined. This avoids pretending to preserve resource balances across reloads. The cfg template uses a fixed world, the heads instruction set, program-variation settings inherited from the pinned stock configuration, and the generated environment/events files; the appendix is the authoritative runnable configuration.

The event template sets the fixed input triple before injecting the ancestor or loading a saved program population. It then saves the population and exits at update label 999. Each analyze script loads the snapshot and runs six explicit permutations of the same triple. The assay environment has zero task rewards and no resources; test duration and other settings stay fixed.

Expected tiny-run behavior, declared before running: two pieces must yield two distinct seed records, six assay outputs per snapshot, 77-element pay vectors summing to 18, eleven zero-pay entries, and a recorded reload between pieces. No capability acquisition is predicted for this plumbing check. A zero count is an admissible result. A synthetic two-capability fixture separately checks that the assay parser and same-program conjunction do not combine distinct specialists. Commands and observed outputs appear in section 10.

## 6. Restart cautions handled

All arms restart at the same interval. Exit at label 999 is not interchangeable with exit at 1000; the tiny run checks the actual terminal label. Piece seeds are generated deterministically and written before execution. Identical seeds provide repeatable inputs to the random generator, not an equivalence between restarted and uninterrupted execution.

Checked source: stock population snapshots store instruction sequences and active copy/cell information; reload creates executing programs. They are not complete processor, input-buffer, random-generator or resource-state checkpoints. The driver preserves the external selector state and full applied schedules, while accepting that the simulated programs restart. The inference concerns this piecewise execution environment.

The cold-start analyze assay does not read newly reloaded live task counters, so their initial undercount cannot be interpreted as capability loss. It measures reproducible behavior of saved instruction sequences under the assay. Transient within-lifetime state is intentionally outside that measure. Active multiplicities weight every share; extinct historical entries are excluded. Spatial placement and differing stage-of-replication histories can still influence the next piece. Checked in `cPopulation.cc`: reload also restores saved merit and approximately adjusts it for the remaining replication time. Previous rewards can therefore affect initial processor allocation after a schedule changes. Restart-matched arms share this mechanism; an applied b vector describes offered task rewards, not an instantaneous reset of every program’s merit.

Checked source limitation: stock analyze task columns use task counts attached to a completed replication in the test CPU. The time allowance is `TEST_CPU_TIME_MOD × instruction-sequence length`. A program that emits a useful output but does not complete the relevant replication can receive zero task counts. Thus “capability” here means the assay-defined recorded behavior, not every output a program could ever emit. Order robustness covers six orders of one fixed triple, not arbitrary streams, intervals or number values.

## 7. C++, only if needed

No C++ change is needed for this design. The diff against 47f13dad is empty. Checked: stock supports generated reaction rewards, saved program populations and manual-input analyze assays. Python supplies the selector state and between-piece feedback.

Direct reward for an all-order property within an individual world execution is not supplied. Nor are exclusive conjunction rewards, arbitrarily timed IO streams or every-output logging. Those would be separate specifications. The current coincidence detector changes marginal task pay; calling it an exclusive pair reward would misdescribe the implementation.

## 8. Controls, sizes and cost

| Arm | Applied schedule and controlled difference |
|---|---|
| Full | Stateful equations above, observed receiver population controls the next piece. |
| Memoryless | Same equations and inputs, fresh zero state before every update. It can react to the current assay but cannot retain a problem, prior sequence or release history. |
| Blind replay | Apply one full run’s complete schedule to another seed. Receiver assays are measured but never used for decisions. |
| Fixed list | Apply the donor’s per-task time-mean b vector throughout. This matches mean log2 bonus, not mean arithmetic multiplier 2^b. |
| Seven removals | Separately remove trace, adaptation, latch, rebound, coincidence, sequence and expectation; preserve all other coefficients and normalize to the same budget. |

Removing trace substitutes h′=q; it changes the inputs to adaptation, the loss latch and expectation. Removing adaptation substitutes A=1.1. Removing latch also removes the release source for rebound. Other removals zero their component. These are interacting component removals, not seven independent mechanistic estimates. A predeclared paired removal of latch and rebound would expose their shared route, but is additional to the eleven-arm cost below.

Each independent block has one full run, one memoryless run, one different-seed replay, one different-seed fixed run and the seven removals. The full run is the donor, so no extra donor run is charged. Donor-linked observations form a block; repeated reuse of one donor does not create independent schedules. Replay and fixed execution wait for the donor schedule. Nominal budgets match; the per-task mean vector of the memoryless arm is not forced to match its donor.

The named difference is ten additional common all-order capabilities at 50,000 updates. Checked in the supplied brief only: S113 gives growing-list counts 48,55,65 and all-77 counts 13,32,41. Their means are 56 and 28.667. Sample variances are (64+1+81)/2=73 and (245.444+11.111+152.111)/2=204.333; standard deviations are 8.544 and 14.295. Pooled variance is (146+408.667)/4=138.667, giving 11.776.

For an approximate independent two-arm calculation with two-sided α=0.05 and 80% power, n=ceil[2(1.96+0.84)^2 s²/10²]. This gives 12,22 or33 seeds per arm for those three variability scenarios. With two primary contrasts, full versus memoryless and full versus replay, a Bonferroni α=0.025 per contrast replaces 1.96 with 2.2414; the largest-variance scenario gives 38.80, hence39 before rounding. Forty per arm is an approximate planning option. A conventional equal-variance noncentral-t calculation puts the corresponding minimum at41. These are calculations under assumptions, not a measured power guarantee: three historical runs, another endpoint, the holdout split and donor dependence do not identify the required variance. The pilot must estimate block-difference variability before a funded design is frozen.

| Owner option | Runs and simulation CPU-hours | Allowance and wall-time arithmetic |
|---|---|---|
| Small engineering and variance pilot | Eleven arms × three blocks × one CPU-hour =33 | Metered allowance12 CPU-hours for assays, driver and tiny checks gives45 total, under about50. At three processes,45/3=15 hours is a capacity lower bound; donor barriers and uneven runtimes add time. Stop at the allowance and report incomplete work. |
| Larger approximate comparison | Eleven arms ×40 blocks =440 | A provisional25% overhead gives550 CPU-hours. 550/3=183.33 hours, or7.64 days, is a capacity lower bound. If41 blocks are chosen,451×1.25=563.75 CPU-hours and187.92 hours, or7.83 days. |

At n=3 and s=14.295, the same unadjusted formula corresponds to roughly 32.68 capabilities, rather than the named ten. The small option cannot support a ten-capability effect claim. The larger allowance must be replaced with measured assay costs before launch. All six assays may be expensive in diverse saved populations. No extra evolutionary warm-up is required for a cold-start assay; adding one would change both cost and execution environment. The one CPU-hour benchmark is supplied by the owner, not calibrated here at 3,600 cells.

For every snapshot record C_world=sum 1[p_j≥0.10], C_all=sum 1[q_j≥0.10], the count for withheld H, ever-common counts, gains and losses. Record the actual zero-pay set from the complete history, not merely zero pay in the current piece. Zero direct reward does not exclude indirect benefit through shared instruction regions or rewards for other tasks. Report C_all,50−C_all,25 and the per-run slope over pieces 26–50, distinguishing cumulative discovery from currently retained capability. Pieces within one run are not independent replicates. Log every latch’s set, clear, duration and triggering shares, including latches still open at the end. If no latch ever sets, this run does not test latch resolution.

## 9. What counts against

No separation from state erasure counts against a useful contribution of persistent history; no separation from replay counts against population-contingent feedback. A statistical interval wide enough to include substantial effects in either direction is inconclusive, not equivalence. Fixed-mean similarity questions the necessity of changing schedules. Unchanged outcomes after a component removal question that component’s contribution at the tested scale. A plateau after 25,000 updates counts against continued capability accumulation even if the selector keeps moving.

The hard-to-vary question is frozen to these changes and this assay. The units are fixed requirements of the brief; their contribution to sustained acquisition is **unknown** pending population comparisons. The exact gains, timescales, thresholds and holdout split are **loose** engineering choices. A finite-state timer can substitute for a trace-and-threshold sequence detector, so neuron vocabulary does not explain an otherwise inaccessible capability. The assay semantics and Avida merit machinery are **borrowed** from the checked source. The two-piece clearance and bounded pay are **built** responses to declared jobs, not independent evidence of learning.

Normalization makes units compete; high surprise can repeatedly pay oscillation; increasing a loss response can crowd out unrelated opportunities. Gauges are the raw terms alongside final pay, repeated threshold crossings, latch occupancy and age, capability turnover, and exposure of never-common eligible tasks. A permanently latched capability is a failed resolution outcome, not a reason to introduce an unreported timeout. The strongest rival is a memoryless rarity schedule with identical pay budget; the memoryless arm makes that comparison without changing detectors.

Independent probes found that alternating shares of 0.099 and 0.101 repeatedly trigger the sequence unit although both capabilities remain present throughout. The implemented event means becoming common again, not acquiring an unseen capability. This is retained as a mechanism limit rather than repaired after seeing the result.

A further timing probe holds the identities and counts of synthetic capability events fixed while changing their order or spacing. It tests temporal discrimination, not biological fidelity. The independent challenge also changes co-occurrence while holding marginal shares fixed. Success on designer-written fixtures does not settle behavior on the owner’s saved populations. None of S113–S120’s original populations was provided here.

## 10. What you ran, with outputs; sources marked checked or from memory; what you are unsure of

Actual execution included a stock Avida build, Python component and independent probes, two initial 64-cell pieces, two final 64-cell pieces with the frozen driver, two replay pieces, two fixed-mean pieces, a completed-run resume, and three versions of an Avida assay fixture. No 50,000-update run,3,600-cell experiment, biological-neuron simulation or costly multi-seed trial was run. All virtual program replication stayed inside Avida.

The first fixture produced zero for both intended positive task columns because its final IO inherited a nop-C modifier. The second corrected IO, exposing another fixture error: the presumed NOT operation used a nonzero CX left by the ancestor’s h-search. The final fixture explicitly copies the input before NAND. These were corrections to hand-prepared virtual programs, not changes to the assay or selector after observing population outcomes. The first fixture gave NOT world/all-order 0 and NAND world/all-order 0; the second gave NOT 0/0 and NAND 0.375/0; the final output below records the corrected result.

The final full run used master seed 4101; replay used 4102 and fixed mean 4103. Each used an 8×8 world and two 1,000-update pieces. Every run checked all 1,000 update labels and the loaded cell-to-instruction-sequence mapping. The final full run reproduced the initial zero-common outcomes. Replay also had zero common capabilities. Fixed mean ended with one world-order common capability and zero all-order common capabilities. These tiny differences are not treatment-effect estimates. No population latch opened or cleared in these tiny runs; synthetic probes alone exercised clearance.

The final fixture used three virtual instruction sequences with abundances 3,1,4. NOT was present at share 0.5 in every order in the same programs. NAND was present in every order at the population level, but only in complementary specialists; its all-order same-program share was 0. All 18 replication-test flags were 1. This directly exercises the distinction used by the robust endpoint.

The completed-run `--resume` command returned exit 0 with empty stdout and ran zero additional pieces. Partial-piece crash recovery was not simulated. The runner refuses to overwrite a partial directory; retain it and move it aside before resuming. Long-run resource use was not measured. The small runs are unsuitable for scaling the owner’s 3,600-cell CPU-hour benchmark.

Exact executable commands, outputs and code follow. Avida subprocesses write complete stdout/stderr to each piece or assay directory; the pasted outputs are the Python run summaries and probe outputs, not a claim that every verbose per-update line is reproduced here. Code and configuration hashes are recorded by the runner. The sizing arithmetic was also run: sample SDs 8.544004/14.294521, pooled 11.775681, approximate seed counts 12/22/33; conditional t-model power 0.798581 at 40 and0.809506 at 41; cost totals 45/550/563.75 CPU-hours.


The runnable selector was frozen before its component probes. Before implementation, review found that withheld capabilities could indirectly affect eligible pay through coincidence or sequence sources; v1.1 explicitly masks those routes. This is a recorded design amendment, not a population result. An independent boundary probe then found that a trace approaching exactly 0.10 from below never crossed the loss threshold. Version 1.2 includes the previous observed share≥0.10 in the loss trigger. The original failed case is retained. The cost is that a single common observation followed by loss can now open a persistent latch; regression probes distinguish it from an always-below-threshold history. Any later implementation corrections and independent findings are reported with the execution record.

Checked primary-source trail: the local checkout at full commit 47f13dadb547fcf10f620ace60247f38b30b8b16, opened files `avida-core/source/actions/SaveLoadActions.cc`, `EnvironmentActions.cc`, `source/analyze/cAnalyze.cc`, `cAnalyzeGenotype.cc`, `source/cpu/cTestCPU.cc`, and `support/config/misc/environment-all-logic.cfg`. Source locations and command details are included with the code. Repository: [devosoft/avida at 47f13dad](https://github.com/devosoft/avida/tree/47f13dadb547fcf10f620ace60247f38b30b8b16).

Checked: [sequential logic](https://computationstructures.org/notes/sequential_logic/notes.html) supplies the memory-versus-combinational distinction. Checked: [Brian2 event-driven equations](https://brian2.readthedocs.io/en/2.10.0/user/synapses.html#event-driven-updates) describes independent one-dimensional linear traces and limits automatic event-driven treatment to suitable equations. The driver uses elementary discrete updates and does not depend on Brian2. Checked attachments: the supplied execution brief and `Temporal_Neuron_Computation_Report.docx`; their project histories and 22-study synthesis are attributed reports, not new replications. No outside claim is offered solely from memory. Additional checked source locations are `cStats.cc:65`, `Avida2Driver.cc:91–127` for update order, `SaveLoadActions.cc:69–94,148–181` for load/save, `cPopulation.cc:7018–7064` for merit carryover, `cAnalyze.cc:10261–10320` for manual inputs, and `cEnvironment.cc:1756–1758` for the power-of-two reward.

Still uncertain are sustained acquisition, the relevance of each unit, the adequacy of this reward strength, long-run assay cost, effects of input values beyond the fixed triple, and the owner’s definitions of knowledge and instinct. The next empirical option is the bounded pilot with the frozen controls; choosing it or the larger option remains with the owner.


## Code appendices

The paths below are relative to one working directory. Code is Python3 standard library; the optional sizing calculation used SciPy only in this session. Preserve the pinned Avida checkout alongside the `temporal_selector` directory. The full experiments remain owner options.

### Executed commands and selected build output

The clone ran from the session working directory; subsequent build commands ran inside `avida-source`. Runner and fixture commands ran inside `temporal_selector`. Build output below is explicitly an excerpt; per-update Avida output is logged by the scripts. The resume had empty stdout and exit0. Python probes ran from the parent directory using `python temporal_selector/checks.py`, `python independent_test.py` and `python evidence/additional_check.py`. The summary script was run on the full and fixed tiny directories.

#### Build commands

```bash
git clone https://github.com/devosoft/avida.git /workspace/scratch/e7208be14540/avida-source
git checkout 47f13dad
git rev-parse HEAD
git submodule update --init libs/apto libs/backward-cpp
python -m cmake -S . -B cbuild -DCMAKE_POLICY_VERSION_MINIMUM=3.5 -DAVD_GUI_NCURSES=OFF -DCMAKE_BUILD_TYPE=Release
python -m cmake --build cbuild --target avida -j 3 > cbuild/build.log 2>&1
./cbuild/bin/avida -v
```

#### Selected build output

```text
HEAD is now at 47f13dadb Merge pull request #95 from mmore500/whole-genome-duplication
47f13dadb547fcf10f620ace60247f38b30b8b16
Submodule path 'libs/apto': checked out '02e18980071d237f1ea4641f3f35cae469e2ed38'
Submodule path 'libs/backward-cpp': checked out 'dc8b8c76822dcbc8918f032171050ad90e11eb7f'
-- The C compiler identification is GNU 13.3.0
-- The CXX compiler identification is GNU 13.3.0
-- Configuring done (0.4s)
-- Generating done (0.0s)
-- Build files have been written to: /workspace/scratch/e7208be14540/avida-source/cbuild
[100%] Linking CXX executable ../bin/avida
[100%] Built target avida
Avida 2.14.0
release build
```

#### Initial tiny run

```bash
python runner.py --avida ../avida-source/cbuild/bin/avida --source ../avida-source --out ../evidence/tiny_full --seed 4101 --pieces 2 --width 8 --height 8
```

#### Final frozen tiny run

```bash
python runner.py --avida ../avida-source/cbuild/bin/avida --source ../avida-source --out ../evidence/tiny_checked --seed 4101 --pieces 2 --width 8 --height 8
```

#### Full output for both full runs

```text
{"all_order_common": 0, "assay_seed": 1797738470, "completed_updates": 1000, "latches": 0, "never_paid_common": 0, "piece": 0, "program_population": 64, "releases": 0, "seed": 744718624, "world_common": 0}
{"all_order_common": 0, "assay_seed": 456554504, "completed_updates": 2000, "latches": 0, "never_paid_common": 0, "piece": 1, "program_population": 64, "releases": 0, "seed": 958222715, "world_common": 0}
```

#### Replay command

```bash
python runner.py --avida ../avida-source/cbuild/bin/avida --source ../avida-source --out ../evidence/tiny_replay --seed 4102 --arm replay --donor ../evidence/tiny_checked --pieces 2 --width 8 --height 8
```

#### Replay output

```text
{"all_order_common": 0, "assay_seed": 1499611839, "completed_updates": 1000, "latches": 0, "never_paid_common": 0, "piece": 0, "program_population": 64, "releases": 0, "seed": 1693314807, "world_common": 0}
{"all_order_common": 0, "assay_seed": 1828401919, "completed_updates": 2000, "latches": 0, "never_paid_common": 0, "piece": 1, "program_population": 64, "releases": 0, "seed": 1851297359, "world_common": 0}
```

#### Fixed command

```bash
python runner.py --avida ../avida-source/cbuild/bin/avida --source ../avida-source --out ../evidence/tiny_fixed --seed 4103 --arm fixed --donor ../evidence/tiny_checked --pieces 2 --width 8 --height 8
```

#### Fixed output

```text
{"all_order_common": 0, "assay_seed": 1453822508, "completed_updates": 1000, "latches": 0, "never_paid_common": 0, "piece": 0, "program_population": 64, "releases": 0, "seed": 984211725, "world_common": 0}
{"all_order_common": 0, "assay_seed": 2057528024, "completed_updates": 2000, "latches": 0, "never_paid_common": 0, "piece": 1, "program_population": 64, "releases": 0, "seed": 1272671840, "world_common": 1}
```

#### Completed-run resume command

```bash
python runner.py --avida ../avida-source/cbuild/bin/avida --source ../avida-source --out ../evidence/tiny_checked --seed 4101 --pieces 2 --width 8 --height 8 --resume
```

#### Two failed fixture development commands

```bash
python integration_checks.py --avida ../avida-source/cbuild/bin/avida --source ../avida-source --out ../evidence/positive_fixture
python integration_checks.py --avida ../avida-source/cbuild/bin/avida --source ../avida-source --out ../evidence/positive_fixture_v2
```

#### Failure output from each fixture attempt

```text
assert observation["p"][not_id] == .5 and observation["q"][not_id] == .5
AssertionError
```

#### Final fixture command

```bash
python integration_checks.py --avida ../avida-source/cbuild/bin/avida --source ../avida-source --out ../evidence/positive_fixture_v3
```

#### Final fixture output

```text
{"NAND_all_orders": 0, "NAND_each_order": [0.375, 0.375, 0.125, 0.375, 0.125, 0.125], "NAND_world": 0.375, "NOT_NAND_same_program_all_orders": 0, "NOT_all_orders": 0.5, "NOT_world": 0.5, "checks": "Positive task parsing, multiplicity weighting, all-six same-program conjunction, replication passed", "population": 8, "virtual_programs": 3}
```

### Recorded outputs

#### Component probes after the version1.2 change

```text
adaptation sustained 0.630561 -> 0.324283; after absence 1.040426
latch held across 20 absent pieces; clears after two robust assays; rebound 1.000000
sequence short 0.716531; long 0.025562; alone 0; simultaneous 0
same-program coincidence 0.078694; separate programs 0
constant empty assay after 100 pieces: nominal budget 18.000000; withheld 11; eligible 66
seven ablations preserve nominal budget; serialized state replay identical
COMPONENT CHECKS COMPLETED
```

#### Independent version1.1 boundary observation before the amendment

```text
collective_suppression: {"final_adaptation": [0.221955962, 0.221955962], "final_pay": [9.0, 9.0], "initial_adaptation": [0.949646999, 0.949646999], "initial_pay": [9.0, 9.0]}
release_response: {"latched_pay": 11.8125, "release_contribution": 0.5, "released_pay": 10.666666667, "released_without_rebound_pay": 9.0}
threshold_recrossing: {"sequence_responses": [0.0, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311], "stationary_responses": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "task_identities_present_throughout": 2}
heldout_mask: {"maximum_pay_difference_each_piece": [0.0, 0.0, 0.0]}
empty_task_set: {"earned_log2_task_bonus_for_empty_set": 0, "nominal_sum": 18.0, "offered_eligible_bonus": 0.272727273, "pieces": 200}
unresolved_latch: {"latch": [1, 0], "pay": [11.8125, 6.1875], "pieces": 200, "rebound": [0.0, 0.0]}
selector_continuation: {"equal_future_steps": 4}
joint_membership: {"pair_coincidence": [0.098367335, 0.098367335, 0.0], "pair_pay": [6.086836406, 6.086836406, 5.826327188], "specialist_coincidence": [0.0, 0.0, 0.0], "specialist_pay": [6.0, 6.0, 6.0]}
common_threshold_loss: {"exact_common_loss_latch": [0, 0], "historical_traces": ["0.09999999999999995", "0.10027777777777774"], "nearby_common_loss_latch": [1, 0]}
Audit cases completed. No Avida evolutionary run was performed.
```

#### Independent probes after the version1.2 change

```text
collective_suppression: {"final_adaptation": [0.221955962, 0.221955962], "final_pay": [9.0, 9.0], "initial_adaptation": [0.949646999, 0.949646999], "initial_pay": [9.0, 9.0]}
release_response: {"latched_pay": 11.8125, "release_contribution": 0.5, "released_pay": 10.666666667, "released_without_rebound_pay": 9.0}
threshold_recrossing: {"sequence_responses": [0.0, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311, 0.716531311], "stationary_responses": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], "task_identities_present_throughout": 2}
heldout_mask: {"maximum_pay_difference_each_piece": [0.0, 0.0, 0.0]}
empty_task_set: {"earned_log2_task_bonus_for_empty_set": 0, "nominal_sum": 18.0, "offered_eligible_bonus": 0.272727273, "pieces": 200}
unresolved_latch: {"latch": [1, 0], "pay": [11.8125, 6.1875], "pieces": 200, "rebound": [0.0, 0.0]}
selector_continuation: {"equal_future_steps": 4}
joint_membership: {"pair_coincidence": [0.098367335, 0.098367335, 0.0], "pair_pay": [6.086836406, 6.086836406, 5.826327188], "specialist_coincidence": [0.0, 0.0, 0.0], "specialist_pay": [6.0, 6.0, 6.0]}
common_threshold_loss: {"exact_common_loss_latch": [1, 0], "historical_traces": ["0.09999999999999995", "0.10027777777777774"], "nearby_common_loss_latch": [1, 0]}
loss_amendment_neighbours: {"below_common_loss_latch": [0, 0], "one_piece_common_loss_latch": [1, 0], "slow_loss_latch": [1, 0], "slow_prior_h": 0.582958298, "slow_prior_q": 0.05}
Audit cases completed. No Avida evolutionary run was performed.
```

#### Task label permutation probe

```text
task relabelling with eligibility carried: 3 successive pay vectors commute
```

#### Final integration summaries

```text
{
  "tiny_checked": [
    {
      "all_order_common": 0,
      "assay_seed": 1797738470,
      "completed_updates": 1000,
      "latches": 0,
      "never_paid_common": 0,
      "piece": 0,
      "program_population": 64,
      "releases": 0,
      "seed": 744718624,
      "world_common": 0
    },
    {
      "all_order_common": 0,
      "assay_seed": 456554504,
      "completed_updates": 2000,
      "latches": 0,
      "never_paid_common": 0,
      "piece": 1,
      "program_population": 64,
      "releases": 0,
      "seed": 958222715,
      "world_common": 0
    }
  ],
  "tiny_replay": [
    {
      "all_order_common": 0,
      "assay_seed": 1499611839,
      "completed_updates": 1000,
      "latches": 0,
      "never_paid_common": 0,
      "piece": 0,
      "program_population": 64,
      "releases": 0,
      "seed": 1693314807,
      "world_common": 0
    },
    {
      "all_order_common": 0,
      "assay_seed": 1828401919,
      "completed_updates": 2000,
      "latches": 0,
      "never_paid_common": 0,
      "piece": 1,
      "program_population": 64,
      "releases": 0,
      "seed": 1851297359,
      "world_common": 0
    }
  ],
  "tiny_fixed": [
    {
      "all_order_common": 0,
      "assay_seed": 1453822508,
      "completed_updates": 1000,
      "latches": 0,
      "never_paid_common": 0,
      "piece": 0,
      "program_population": 64,
      "releases": 0,
      "seed": 984211725,
      "world_common": 0
    },
    {
      "all_order_common": 0,
      "assay_seed": 2057528024,
      "completed_updates": 2000,
      "latches": 0,
      "never_paid_common": 0,
      "piece": 1,
      "program_population": 64,
      "releases": 0,
      "seed": 1272671840,
      "world_common": 1
    }
  ],
  "positive_fixture": {
    "NAND_all_orders": 0,
    "NAND_each_order": [
      0.375,
      0.375,
      0.125,
      0.375,
      0.125,
      0.125
    ],
    "NAND_world": 0.375,
    "NOT_NAND_same_program_all_orders": 0,
    "NOT_all_orders": 0.5,
    "NOT_world": 0.5,
    "checks": "Positive task parsing, multiplicity weighting, all-six same-program conjunction, replication passed",
    "population": 8,
    "virtual_programs": 3
  },
  "source_commit": "47f13dadb547fcf10f620ace60247f38b30b8b16",
  "binary_sha256": "92c377b7b4f0e05f425e714a3088b273c5cbed700e7d7c8b9e1e8c7158fb08fe",
  "completed_resume": {
    "exit_code": 0,
    "stdout": "",
    "pieces_rerun": 0
  }
}
```

### Files to save

#### temporal_selector/selector.py

```python
"""Population-conditioned selector, specification v1.2. Python 3 standard library."""
import copy
import math

UNITS = ('trace', 'adaptation', 'latch', 'rebound', 'coincidence', 'sequence', 'expectation')

class Selector:
    def __init__(self, k, eligible=None, disabled=()):
        self.k = k
        self.eligible = list(eligible if eligible is not None else (i for i in range(k) if i % 7 != 6))
        if not self.eligible or len(set(self.eligible)) != len(self.eligible):
            raise ValueError('eligible indices must be nonempty and unique')
        if any(i < 0 or i >= k for i in self.eligible):
            raise ValueError('eligible index outside catalog')
        self.disabled = set(disabled)
        if not self.disabled <= set(UNITS):
            raise ValueError('unknown ablation')
        self.state = dict(h=[0.0]*k, hprev=[0.0]*k, q=[0.0]*k,
                          latch=[0]*k, clear=[0]*k, rebound=[0.0]*k,
                          event=[0.0]*k, coincidence=[[0.0]*k for _ in range(k)])

    def load(self, state):
        if set(state) != set(self.state):
            raise ValueError('state schema differs')
        if any(len(v) != self.k for v in state.values()):
            raise ValueError('state catalog size differs')
        self.state = copy.deepcopy(state)
        return self

    def initial_pay(self):
        return [18.0/len(self.eligible) if i in self.eligible else 0.0 for i in range(self.k)]

    def step(self, obs):
        k = self.k
        if len(obs['p']) != k or len(obs['q']) != k or len(obs['cooc']) != k:
            raise ValueError('observation catalog size differs')
        vals = list(obs['p']) + list(obs['q'])
        for row in obs['cooc']:
            if len(row) != k:
                raise ValueError('coincidence shape differs')
            vals.extend(row)
        if any(not math.isfinite(v) or v < 0 or v > 1 for v in vals):
            raise ValueError('shares must be finite in [0,1]')
        if any(obs['q'][j] > obs['p'][j] + 1e-12 for j in range(k)):
            raise ValueError('all-order share exceeds world-order share')
        for j in range(k):
            for i in range(k):
                if obs['cooc'][j][i] > min(obs['q'][j], obs['q'][i]) + 1e-12:
                    raise ValueError('coincidence exceeds marginal')
                if abs(obs['cooc'][j][i]-obs['cooc'][i][j]) > 1e-12:
                    raise ValueError('coincidence matrix is not symmetric')
        allowed = set(self.eligible)
        p = [obs['p'][i] if i in allowed else 0.0 for i in range(k)]
        q = [obs['q'][i] if i in allowed else 0.0 for i in range(k)]
        old = self.state
        h = [math.exp(-.25)*old['h'][i] + (1-math.exp(-.25))*q[i] for i in range(k)]
        if 'trace' in self.disabled:
            h = q[:]
        prediction = [min(1., max(0., 2*old['h'][i]-old['hprev'][i])) for i in range(k)]
        surprise = [abs(q[i]-prediction[i]) if 'expectation' not in self.disabled else 0.0 for i in range(k)]
        latch, clear, release = [], [], []
        for i in range(k):
            L = old['latch'][i]
            streak = old['clear'][i]+1 if q[i] >= .1 else 0
            if 'latch' in self.disabled:
                L, streak, released = 0, 0, 0
            else:
                if L:
                    if streak >= 2:
                        L = 0
                elif (p[i] >= .1 or old['q'][i] >= .1 or old['h'][i] >= .1) and q[i] < .02:
                    L, streak = 1, 0
                released = int(old['latch'][i] == 1 and L == 0)
            latch.append(L)
            clear.append(min(2, streak))
            release.append(released)
        rebound = [math.exp(-.5)*old['rebound'][i]+release[i] if 'rebound' not in self.disabled else 0.0 for i in range(k)]
        C = [[(math.exp(-.5)*old['coincidence'][i][j]+(1-math.exp(-.5))*obs['cooc'][i][j])
              if i != j and i in allowed and j in allowed and 'coincidence' not in self.disabled else 0.0
              for j in range(k)] for i in range(k)]
        coinc = [max(row) for row in C]
        events = [int(old['q'][i] < .1 <= q[i]) for i in range(k)]
        decayed = [math.exp(-1/3)*v for v in old['event']]
        seq = [events[i]*max((decayed[j] for j in self.eligible if j != i), default=0.0)
               if 'sequence' not in self.disabled else 0.0 for i in range(k)]
        event_trace = [1.0 if events[i] else decayed[i] for i in range(k)]
        if 'sequence' in self.disabled:
            event_trace = [0.0]*k
        adapt = [.1 + 1/(1+8*x) if 'adaptation' not in self.disabled else 1.1 for x in h]
        raw = [adapt[i]+latch[i]+.5*(rebound[i]+coinc[i]+seq[i]+surprise[i]) for i in range(k)]
        denom = sum(raw[i] for i in self.eligible)
        pay = [18*raw[i]/denom if i in allowed else 0.0 for i in range(k)]
        self.state = dict(h=h, hprev=old['h'][:], q=q, latch=latch, clear=clear,
                          rebound=rebound, coincidence=C, event=event_trace)
        return dict(pay=pay, diagnostics=dict(adaptation=adapt, prediction=prediction,
                    surprise=surprise, latch=latch, release=release, rebound=rebound,
                    coincidence=coinc, sequence=seq, events=events, raw=raw))
```

#### temporal_selector/assay.py

```python
"""Stock Avida 47f13dad: abundance-weighted, six-input-order cold-start assay."""
from __future__ import annotations

import hashlib
import itertools
import json
import re
import shutil
import subprocess
from pathlib import Path

COMMIT = "47f13dadb547fcf10f620ace60247f38b30b8b16"
INPUTS = (0x0F13149F, 0x3308E53E, 0x556241EB)
ORDERS = tuple(itertools.permutations(range(3)))
TASKS = ("not nand and orn or andn nor xor equ".split()
         + ["logic_3" + a + b for a, b in itertools.product("ABC", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            if a + b <= "CP"])


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def atomic_json(path, value):
    path = Path(path)
    temp = path.with_name(path.name + ".tmp")
    temp.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")
    temp.replace(path)


def table(path):
    """Read Avida's explicit #format header; never assume .spop column numbers."""
    fields, rows = None, []
    for line in Path(path).read_text().splitlines():
        if line.startswith("#format "):
            fields = line.split()[1:]
        elif line.strip() and not line.lstrip().startswith("#"):
            values = line.split()
            if fields is None or len(values) != len(fields):
                raise ValueError(f"Malformed table: {path}")
            rows.append(dict(zip(fields, values)))
    if fields is None:
        raise ValueError(f"Missing format header: {path}")
    return rows


def environment(pay):
    if len(pay) != len(TASKS):
        raise ValueError("Expected 77 task rewards")
    return "".join(f"REACTION T{i:02d} {task} process:value={value:.17g}:type=pow "
                   "requisite:max_count=1\n"
                   for i, (task, value) in enumerate(zip(TASKS, pay)))


def prepare(source, dest, settings):
    """Use the pinned stock configuration and its 26-instruction heads set."""
    source, dest = Path(source), Path(dest)
    dest.mkdir(parents=True, exist_ok=True)
    support = source / "avida-core/support/config"
    cfg = (support / "avida.cfg").read_text()
    for key, value in settings.items():
        pattern = rf"(?m)^{re.escape(key)}\s+[^\n]*$"
        if not re.search(pattern, cfg):
            raise ValueError(f"Setting absent from stock config: {key}")
        cfg = re.sub(pattern, f"{key} {value}", cfg)
    (dest / "avida.cfg").write_text(cfg)
    for name in ("instset-heads.cfg", "default-heads.org"):
        shutil.copy2(support / name, dest / name)


def execute(binary, cwd, analyze=False):
    argv = [str(Path(binary).resolve()), "-c", "avida.cfg"]
    if analyze:
        argv.append("-a")
    cwd = Path(cwd)
    atomic_json(cwd / "command.json", argv)
    with (cwd / "stdout.log").open("w") as stdout, (cwd / "stderr.log").open("w") as stderr:
        result = subprocess.run(argv, cwd=cwd, stdout=stdout, stderr=stderr, check=False)
    if result.returncode:
        raise RuntimeError(f"Avida exit {result.returncode}; see {cwd}/stderr.log and stdout.log")
    for log in ("stdout.log", "stderr.log"):
        if re.search(r"(?im)^\s*error\s*:", (cwd / log).read_text()):
            raise RuntimeError(f"Avida reported an error in {cwd / log}")


def assay(binary, source, snapshot, dest, seed):
    """Count tasks recorded at first replication; does not count all outputs.

    All orders use the same three numbers, fixed neutral rewards, one trial,
    and stock TEST_CPU_TIME_MOD=20. No live task counters enter the result.
    """
    dest = Path(dest)
    prepare(source, dest, {"RANDOM_SEED": seed, "WORLD_X": 1, "WORLD_Y": 1,
                          "VERBOSITY": 1, "TEST_CPU_TIME_MOD": 20})
    shutil.copy2(snapshot, dest / "population.spop")
    (dest / "environment.cfg").write_text(environment([0.0] * len(TASKS)))
    (dest / "events.cfg").write_text("")
    lines = ["LOAD population.spop", "FILTER num_units > 0"]
    for order in ORDERS:
        values = " ".join(str(INPUTS[i]) for i in order)
        name = "order_" + "".join(map(str, order)) + ".dat"
        lines += [f"RECALCULATE 0 -1 0 {values}",
                  f"DETAIL {name} id num_units viable task_list sequence"]
    (dest / "analyze.cfg").write_text("\n".join(lines) + "\n")
    execute(binary, dest, analyze=True)
    original = {row["id"]: int(row.get("num_units", row.get("num_cpus", 0)))
                for row in table(snapshot)
                if int(row.get("num_units", row.get("num_cpus", 0))) > 0}
    if not original or sum(original.values()) <= 0:
        raise RuntimeError("Empty saved program population")
    by_order = []
    for order in ORDERS:
        filename = "order_" + "".join(map(str, order)) + ".dat"
        rows = table(dest / "data" / filename)
        result = {row["id"]: row for row in rows}
        if len(result) != len(rows) or set(result) != set(original):
            raise ValueError("Assay IDs do not match saved program population")
        for key, row in result.items():
            if int(row["num_units"]) != original[key] or len(row["task_list"]) != len(TASKS):
                raise ValueError("Assay abundance or task catalog mismatch")
        by_order.append(result)
    n, k = sum(original.values()), len(TASKS)
    p, q = [0.0] * k, [0.0] * k
    cooc = [[0.0] * k for _ in range(k)]
    programs = []
    for key, count in original.items():
        records = [result[key] for result in by_order]
        if len({row["sequence"] for row in records}) != 1:
            raise ValueError("Program sequence changed across orders")
        bits = [[c != "0" for c in row["task_list"]] for row in records]
        robust = [all(order[j] for order in bits) for j in range(k)]
        active = [j for j in range(k) if robust[j]]
        for j in range(k):
            p[j] += count * bits[0][j]
            q[j] += count * robust[j]
        for j in active:
            for l in active:
                if j != l:
                    cooc[j][l] += count
        programs.append({"id": key, "count": count, "orders": bits,
                         "robust": robust, "replication_test": [int(r["viable"]) for r in records]})
    obs = {"p": [v / n for v in p], "q": [v / n for v in q],
           "cooc": [[v / n for v in row] for row in cooc], "population_size": n,
           "distinct_program_records": len(original)}
    atomic_json(dest / "programs.json", programs)
    atomic_json(dest / "observation.json", obs)
    return obs
```

#### temporal_selector/runner.py

```python
#!/usr/bin/env python3
"""Run stock Avida in restart-matched 1,000-update pieces. No C++ patch."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import shutil
import subprocess
from pathlib import Path

from assay import COMMIT, INPUTS, ORDERS, TASKS, assay, atomic_json, digest, environment, execute, prepare, table
from selector import Selector, UNITS


def piece_seed(master, piece, stream):
    message = f"temporal-selector-v1:{master}:{piece}:{stream}".encode()
    return 1 + int.from_bytes(hashlib.sha256(message).digest()[:8], "big") % 2147483646


def cell_programs(path):
    mapping = {}
    for row in table(path):
        count = int(row.get("num_units", row.get("num_cpus", 0)))
        if count == 0:
            continue
        cells = row["cells"].split(",")
        if len(cells) != count:
            raise ValueError("Cell list does not match saved multiplicity")
        for cell in cells:
            if cell in mapping:
                raise ValueError("Duplicate occupied cell in saved program population")
            mapping[cell] = row["sequence"]
    return mapping


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--avida", required=True, type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--seed", required=True, type=int)
    parser.add_argument("--arm", default="full",
                        choices=["full", "memoryless", "replay", "fixed"] + ["no_" + u for u in UNITS])
    parser.add_argument("--pieces", type=int, default=50)
    parser.add_argument("--width", type=int, default=60)
    parser.add_argument("--height", type=int, default=60)
    parser.add_argument("--donor", type=Path, help="Completed full-arm run directory for replay/fixed")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.pieces < 1 or args.width < 1 or args.height < 1:
        parser.error("Pieces and world dimensions must be positive")
    args.source, args.avida, args.out = args.source.resolve(), args.avida.resolve(), args.out.resolve()
    source_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=args.source, text=True).strip()
    if source_commit != COMMIT:
        parser.error("Source checkout is not pinned commit " + COMMIT)
    tracked = subprocess.check_output(["git", "status", "--porcelain", "--untracked-files=no"],
                                     cwd=args.source, text=True).strip()
    if tracked:
        parser.error("Pinned source has tracked modifications")
    disabled = [args.arm[3:]] if args.arm.startswith("no_") else []
    selector = Selector(len(TASKS), disabled=disabled)
    manifest = dict(version=1, selector_spec="1.2", source_commit=source_commit, binary_sha256=digest(args.avida),
                    stock_config_sha256=digest(args.source / "avida-core/support/config/avida.cfg"),
                    tasks=TASKS, eligible=selector.eligible, inputs=INPUTS, orders=ORDERS,
                    seed=args.seed, arm=args.arm, pieces=args.pieces,
                    width=args.width, height=args.height, piece_updates=1000,
                    code_sha256={name: digest(Path(__file__).with_name(name))
                                 for name in ("runner.py", "assay.py", "selector.py")},
                    assay="neutral rewards; six orders; completed first-replication task records; time factor 20")
    donor_pay = None
    if args.arm in ("replay", "fixed"):
        if args.donor is None:
            parser.error("Replay/fixed require --donor")
        donor = json.loads((args.donor / "manifest.json").read_text())
        donor_pay = json.loads((args.donor / "schedule.json").read_text())
        for key in ("tasks", "eligible", "pieces", "width", "height", "binary_sha256", "inputs", "orders",
                    "piece_updates", "stock_config_sha256", "source_commit", "code_sha256"):
            if donor[key] != json.loads(json.dumps(manifest[key])):
                parser.error("Donor differs in " + key)
        if donor["seed"] == args.seed or donor["arm"] != "full" or len(donor_pay) != args.pieces:
            parser.error("Donor must be a completed full arm with another seed")
        manifest["donor_manifest_sha256"] = digest(args.donor / "manifest.json")
        manifest["donor_schedule_sha256"] = digest(args.donor / "schedule.json")
        if args.arm == "fixed":
            mean = [math.fsum(row[j] for row in donor_pay) / args.pieces for j in range(len(TASKS))]
            donor_pay = [mean[:] for _ in range(args.pieces)]
    # Normalize tuples to JSON's arrays before comparing resume manifests.
    manifest = json.loads(json.dumps(manifest))
    args.out.mkdir(parents=True, exist_ok=True)
    manifest_path = args.out / "manifest.json"
    if manifest_path.exists():
        if not args.resume or json.loads(manifest_path.read_text()) != manifest:
            parser.error("Existing run requires --resume with identical settings")
    else:
        atomic_json(manifest_path, manifest)
    pay, previous, schedule = selector.initial_pay(), None, []
    for piece in range(args.pieces):
        directory = args.out / f"piece_{piece:03d}"
        checkpoint = directory / "complete.json"
        if checkpoint.exists():
            saved = json.loads(checkpoint.read_text())
            pay = saved["next_pay"]
            selector.load(saved["selector_state"])
            previous = directory / "data/population-999.spop"
            if digest(previous) != saved["snapshot_sha256"]:
                raise ValueError("Completed snapshot changed")
            schedule.append(saved["applied_pay"])
            continue
        if directory.exists():
            raise RuntimeError(f"Partial piece retained at {directory}; move it aside before --resume")
        if donor_pay is not None:
            pay = donor_pay[piece]
        if (len(pay) != len(TASKS) or any(not math.isfinite(v) or v < 0 for v in pay)
                or abs(sum(pay) - 18) > 1e-10
                or any(pay[j] != 0 for j in range(len(TASKS)) if j not in selector.eligible)):
            raise ValueError("Invalid nominal pay")
        seed = piece_seed(args.seed, piece, "world")
        assay_seed = piece_seed(args.seed, piece, "assay")
        prepare(args.source, directory, {"RANDOM_SEED": seed, "WORLD_X": args.width,
                                        "WORLD_Y": args.height, "VERBOSITY": 1})
        (directory / "environment.cfg").write_text(environment(pay))
        inject = "u begin Inject default-heads.org"
        if previous is not None:
            shutil.copy2(previous, directory / "input.spop")
            inject = "u begin LoadPopulation input.spop"
        events = ["u begin SetEnvironmentInputs " + " ".join(map(str, INPUTS)), inject,
                  "u begin SavePopulation filename=initial:save_historic=0",
                  "u 999 PrintTimeData", "u 999 PrintCountData",
                  "u 999 SavePopulation filename=population:save_historic=0", "u 999 Exit"]
        (directory / "events.cfg").write_text("\n".join(events) + "\n")
        execute(args.avida, directory)
        labels = [int(x) for x in re.findall(r"(?m)^UD:\s*(\d+)", (directory / "stdout.log").read_text())]
        if labels != list(range(1000)):
            raise RuntimeError("Piece did not execute update labels 0 through 999 exactly once")
        seed_line = re.search(r"(?m)^Random Seed:.*$", (directory / "stdout.log").read_text())
        snapshot = directory / "data/population-999.spop"
        if previous is not None and cell_programs(previous) != cell_programs(directory / "data/initial--1.spop"):
            raise ValueError("Reload changed occupied cells or program multiplicities")
        obs = assay(args.avida, args.source, snapshot, directory / "assay", assay_seed)
        if args.arm == "memoryless":
            selector = Selector(len(TASKS))
        response = selector.step(obs) if donor_pay is None else {"pay": pay, "diagnostics": {}}
        eligible = set(selector.eligible)
        metrics = dict(piece=piece, completed_updates=1000*(piece+1), seed=seed, assay_seed=assay_seed,
                       program_population=obs["population_size"], world_common=sum(v >= .1 for v in obs["p"]),
                       all_order_common=sum(v >= .1 for v in obs["q"]),
                       never_paid_common=sum(obs["q"][j] >= .1 for j in range(len(TASKS)) if j not in eligible),
                       latches=sum(response["diagnostics"].get("latch", [])),
                       releases=sum(response["diagnostics"].get("release", [])))
        saved = dict(metrics=metrics, applied_pay=pay, next_pay=response["pay"],
                     avida_seed_line=seed_line.group(0) if seed_line else None,
                     selector_state=selector.state, diagnostics=response["diagnostics"],
                     snapshot_sha256=digest(snapshot))
        atomic_json(checkpoint, saved)
        schedule.append(pay)
        atomic_json(args.out / "schedule.json", schedule)
        print(json.dumps(metrics, sort_keys=True), flush=True)
        pay, previous = response["pay"], snapshot
    atomic_json(args.out / "schedule.json", schedule)


if __name__ == "__main__":
    main()
```

#### temporal_selector/summarize.py

```python
#!/usr/bin/env python3
"""Read completed run records; do not treat pieces as independent runs."""
import argparse
import json
from pathlib import Path

def summarize(directory):
    directory=Path(directory)
    manifest=json.loads((directory/'manifest.json').read_text())
    paths=sorted(directory.glob('piece_*/complete.json'))
    if len(paths) != manifest['pieces']:
        raise ValueError('run is incomplete')
    records=[json.loads(p.read_text()) for p in paths]
    applied=[r['applied_pay'] for r in records]
    k=len(manifest['tasks'])
    never=[j for j in range(k) if all(row[j] == 0 for row in applied)]
    ever=set(); prior=set(); trajectory=[]; episodes=[]; open_latches={}
    for i,(path,record) in enumerate(zip(paths,records)):
        observation=json.loads((path.parent/'assay/observation.json').read_text())
        common={j for j,v in enumerate(observation['q']) if v >= .1}
        ever |= common
        current_latches={j for j,v in enumerate(record['diagnostics'].get('latch',[])) if v}
        for j in current_latches-set(open_latches):
            open_latches[j]=i+1
        for j in set(open_latches)-current_latches:
            episodes.append(dict(task=j,set_piece=open_latches.pop(j),clear_piece=i+1))
        trajectory.append(dict(piece=i+1,world_common=sum(v>=.1 for v in observation['p']),
                               all_order_common=len(common),ever_common=len(ever),
                               gained=sorted(common-prior),lost=sorted(prior-common),
                               never_directly_paid_common=len(common & set(never))))
        prior=common
    for j,start in open_latches.items():
        episodes.append(dict(task=j,set_piece=start,clear_piece=None))
    delta=slope=None
    if len(trajectory)>=50:
        delta=trajectory[49]['all_order_common']-trajectory[24]['all_order_common']
        x=list(range(26,51)); y=[trajectory[i-1]['all_order_common'] for i in x]
        xm=sum(x)/len(x); ym=sum(y)/len(y)
        slope=sum((a-xm)*(b-ym) for a,b in zip(x,y))/sum((a-xm)**2 for a in x)
    return dict(arm=manifest['arm'],seed=manifest['seed'],completed_pieces=len(paths),
                never_directly_paid_indices=never,trajectory=trajectory,latch_episodes=episodes,
                late_delta_50_minus_25=delta,late_slope_per_piece=slope,
                note='Late outcomes require 50 pieces; latch continuity applies only to stateful arms.')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run',type=Path)
    args=parser.parse_args()
    print(json.dumps(summarize(args.run),indent=2,sort_keys=True))
```

#### temporal_selector/checks.py

```python
"""Self-authored component probes frozen in spec_v1 before this test rig."""
from selector import Selector, UNITS
import math

def obs(q, p=None, pairs=None):
    k=len(q)
    C=[[0.0]*k for _ in range(k)]
    if pairs:
        for i,j,v in pairs: C[i][j]=C[j][i]=v
    return dict(p=q[:] if p is None else p, q=q, cooc=C)

def check():
    s=Selector(3)
    a=[]
    for _ in range(8): a.append(s.step(obs([.5,0,0]))['diagnostics']['adaptation'][0])
    assert a[-1] < a[0]
    for _ in range(16): out=s.step(obs([0,0,0]))
    assert out['diagnostics']['adaptation'][0] > a[-1]
    print('adaptation sustained %.6f -> %.6f; after absence %.6f' % (a[0],a[-1],out['diagnostics']['adaptation'][0]))
    s=Selector(3)
    out=s.step(obs([0,0,0],[.5,0,0]))
    assert out['diagnostics']['latch'][0]==1
    for _ in range(20): out=s.step(obs([0,0,0]))
    assert out['diagnostics']['latch'][0]==1
    one=s.step(obs([.2,0,0])); two=s.step(obs([.2,0,0]))
    assert one['diagnostics']['latch'][0]==1 and two['diagnostics']['latch'][0]==0
    assert two['diagnostics']['release'][0]==1 and two['diagnostics']['rebound'][0]==1
    print('latch held across 20 absent pieces; clears after two robust assays; rebound 1.000000')
    s=Selector(3); s.step(obs([.2,0,0])); out=s.step(obs([.2,.2,0]))
    alone=Selector(3).step(obs([0,.2,0]))
    simultaneous=Selector(3).step(obs([.2,.2,0]))
    assert out['diagnostics']['sequence'][1] > 0
    assert alone['diagnostics']['sequence'][1]==simultaneous['diagnostics']['sequence'][1]==0
    delayed=Selector(3); delayed.step(obs([.2,0,0]))
    for _ in range(10): delayed.step(obs([.2,0,0]))
    late=delayed.step(obs([.2,.2,0]))['diagnostics']['sequence'][1]
    assert late < out['diagnostics']['sequence'][1]
    print('sequence short %.6f; long %.6f; alone 0; simultaneous 0' % (out['diagnostics']['sequence'][1],late))
    together=Selector(3).step(obs([.2,.2,0],pairs=[(0,1,.2)]))
    separate=Selector(3).step(obs([.2,.2,0]))
    assert together['diagnostics']['coincidence'][0] > separate['diagnostics']['coincidence'][0]
    print('same-program coincidence %.6f; separate programs 0' % together['diagnostics']['coincidence'][0])
    s=Selector(77)
    flat=obs([0]*77)
    for _ in range(100): out=s.step(flat)
    assert math.isclose(sum(out['pay']),18) and all(out['pay'][i]==0 for i in range(6,77,7))
    print('constant empty assay after 100 pieces: nominal budget %.6f; withheld 11; eligible 66' % sum(out['pay']))
    for unit in UNITS:
        s=Selector(3,disabled=[unit]); s.step(obs([.2,0,0])); o=s.step(obs([.2,.2,0]))
        assert math.isclose(sum(o['pay']),18)
    s=Selector(3); s.step(obs([.2,0,0])); state=s.state
    a=s.step(obs([.2,.2,0])); b=Selector(3).load(state).step(obs([.2,.2,0]))
    assert a==b
    print('seven ablations preserve nominal budget; serialized state replay identical')
    print('COMPONENT CHECKS COMPLETED')

if __name__=='__main__': check()
```

#### temporal_selector/integration_checks.py

```python
#!/usr/bin/env python3
"""Small source-bound checks, including real stock Avida positive assay data."""
import argparse
import json
from pathlib import Path

from assay import TASKS, assay, atomic_json


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--avida", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    out = args.out.resolve()
    out.mkdir(parents=True, exist_ok=False)
    support = args.source / "avida-core/support/config"
    instructions = [line.split()[1] for line in (support / "instset-heads.cfg").read_text().splitlines()
                    if line.startswith("INST ")]
    symbols = dict(zip(instructions, "abcdefghijklmnopqrstuvwxyz"))
    ancestor = [line.split("#")[0].strip() for line in (support / "default-heads.org").read_text().splitlines()
                if line.split("#")[0].strip()]
    # All following instructions execute only inside Avida's virtual machine.
    prefixes = ["IO IO nop-C if-less nand IO nop-B", "IO IO nop-C swap if-less nand IO nop-B",
                "IO push pop nop-C nand IO nop-B"]
    rows = []
    for i, (prefix, count) in enumerate(zip(prefixes, (3, 1, 4)), 1):
        program = ancestor[:6] + prefix.split() + ancestor[6:]
        sequence = "".join(symbols[instruction] for instruction in program)
        (out / f"fixture_{i}.org").write_text("#inst_set heads_default\n#hw_type 0\n" + "\n".join(program) + "\n")
        rows.append(f"{i} {count} {sequence}")
    snapshot = out / "fixture.spop"
    snapshot.write_text("#filetype genotype_data\n#format id num_units sequence\n" + "\n".join(rows) + "\n")
    observation = assay(args.avida, args.source, snapshot, out / "assay", 73)
    programs = json.loads((out / "assay/programs.json").read_text())
    not_id, nand_id = TASKS.index("not"), TASKS.index("nand")
    nand_shares = [sum(row["count"] * row["orders"][order][nand_id] for row in programs)/8
                   for order in range(6)]
    assert observation["p"][not_id] == .5 and observation["q"][not_id] == .5
    assert observation["p"][nand_id] == .375 and observation["q"][nand_id] == 0
    assert min(nand_shares) == .125
    assert observation["cooc"][not_id][nand_id] == 0
    assert all(all(row["replication_test"]) for row in programs)
    summary = dict(population=8, virtual_programs=3, NOT_world=.5, NOT_all_orders=.5,
                   NAND_world=.375, NAND_each_order=nand_shares, NAND_all_orders=0,
                   NOT_NAND_same_program_all_orders=0,
                   checks="Positive task parsing, multiplicity weighting, all-six same-program conjunction, replication passed")
    atomic_json(out / "summary.json", summary)
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
```

#### independent_test.py

```python
"""Independent selector challenge cases; no Avida evolutionary run is performed."""
import copy
import json
import math

from temporal_selector.selector import Selector, UNITS


def population(k, rows):
    """Rows are (abundance share, world-order task set, all-order task set)."""
    assert math.isclose(sum(row[0] for row in rows), 1.0, abs_tol=1e-12)
    out = {"p": [0.0] * k, "q": [0.0] * k,
           "cooc": [[0.0] * k for _ in range(k)]}
    for weight, world, robust in rows:
        world, robust = set(world), set(robust)
        assert robust <= world
        for j in world:
            out["p"][j] += weight
        for j in robust:
            out["q"][j] += weight
            for i in robust:
                out["cooc"][j][i] += weight
    return out


def out(name, **values):
    def rounded(x):
        if isinstance(x, float):
            return round(x, 9)
        if isinstance(x, list):
            return [rounded(y) for y in x]
        return x
    print(name + ": " + json.dumps({k: rounded(v) for k, v in values.items()}, sort_keys=True))


def main():
    # Case 1: the observations come from a same-program pair, so cooc is physical.
    collective = Selector(2, eligible=[0, 1])
    initial = collective.step(population(2, [(0.1, [0, 1], [0, 1]), (0.9, [], [])]))
    for _ in range(40):
        final = collective.step(population(2, [(0.9, [0, 1], [0, 1]), (0.1, [], [])]))
    assert final["diagnostics"]["adaptation"][0] < initial["diagnostics"]["adaptation"][0]
    assert initial["pay"] == final["pay"] == [9.0, 9.0]
    out("collective_suppression", initial_adaptation=initial["diagnostics"]["adaptation"],
        final_adaptation=final["diagnostics"]["adaptation"], initial_pay=initial["pay"],
        final_pay=final["pay"])

    # Case 2: hold every contribution except latch and release response constant.
    disabled = set(UNITS) - {"latch", "rebound"}
    with_rebound = Selector(2, eligible=[0, 1], disabled=disabled)
    no_rebound = Selector(2, eligible=[0, 1], disabled=disabled | {"rebound"})
    bad = population(2, [(0.2, [0], []), (0.8, [], [])])
    resolved = population(2, [(0.1, [0], [0]), (0.1, [0], []), (0.8, [], [])])
    for selector in (with_rebound, no_rebound):
        selector.step(bad)
    before = with_rebound.step(resolved)
    no_rebound.step(resolved)
    after = with_rebound.step(resolved)
    removed = no_rebound.step(resolved)
    assert before["pay"][0] > after["pay"][0] > removed["pay"][0]
    assert after["diagnostics"]["release"] == [1, 0]
    out("release_response", latched_pay=before["pay"][0], released_pay=after["pay"][0],
        released_without_rebound_pay=removed["pay"][0],
        release_contribution=0.5 * after["diagnostics"]["rebound"][0])

    # Case 3: existing specialist proportions cross the threshold in opposite phases.
    oscillating = Selector(2, eligible=[0, 1], disabled=set(UNITS) - {"sequence"})
    stable = Selector(2, eligible=[0, 1], disabled=set(UNITS) - {"sequence"})
    responses, stable_responses = [], []
    for t in range(10):
        a, b = (0.101, 0.099) if t % 2 == 0 else (0.099, 0.101)
        result = oscillating.step(population(2, [(a, [0], [0]), (b, [1], [1]), (0.8, [], [])]))
        control = stable.step(population(2, [(0.101, [0], [0]), (0.101, [1], [1]), (0.798, [], [])]))
        responses.append(sum(result["diagnostics"]["sequence"]))
        stable_responses.append(sum(control["diagnostics"]["sequence"]))
    assert responses[0] == 0 and all(x > 0 for x in responses[1:])
    assert stable_responses == [0] * 10
    out("threshold_recrossing", sequence_responses=responses, stationary_responses=stable_responses,
        task_identities_present_throughout=2)

    # Case 4: only withheld incidences differ, including pair incidence and prior event.
    quiet = Selector(3, eligible=[0, 1])
    heldout = Selector(3, eligible=[0, 1])
    quiet_rows = [
        [(1.0, [], [])],
        [(0.2, [0], [0]), (0.8, [], [])],
        [(0.2, [0, 1], [0, 1]), (0.8, [], [])],
    ]
    heldout_rows = [
        [(0.3, [2], [2]), (0.7, [], [])],
        [(0.2, [0, 2], [0, 2]), (0.1, [2], [2]), (0.7, [], [])],
        [(0.2, [0, 1, 2], [0, 1, 2]), (0.8, [2], [])],
    ]
    differences = []
    for left, right in zip(quiet_rows, heldout_rows):
        a = quiet.step(population(3, left))
        b = heldout.step(population(3, right))
        assert a == b and quiet.state == heldout.state
        differences.append(max(abs(x - y) for x, y in zip(a["pay"], b["pay"])))
    out("heldout_mask", maximum_pay_difference_each_piece=differences)

    # Case 5: an offered schedule does not create a performed task.
    empty = Selector(77)
    for _ in range(200):
        nothing = empty.step(population(77, [(1.0, [], [])]))
    assert math.isclose(sum(nothing["pay"]), 18)
    out("empty_task_set", pieces=200, nominal_sum=sum(nothing["pay"]),
        offered_eligible_bonus=min(nothing["pay"][i] for i in empty.eligible),
        earned_log2_task_bonus_for_empty_set=sum(nothing["pay"][i] for i in []))

    # Case 6: absence cannot close the persistent problem.
    unresolved = Selector(2, eligible=[0, 1])
    for _ in range(200):
        result = unresolved.step(bad)
    assert result["diagnostics"]["latch"] == [1, 0]
    assert result["diagnostics"]["rebound"] == [0.0, 0.0]
    out("unresolved_latch", pieces=200, latch=result["diagnostics"]["latch"],
        rebound=result["diagnostics"]["rebound"], pay=result["pay"])

    # Case 7: serialize plain state, not the Python object or a generator seed.
    restored = Selector(2, eligible=[0, 1]).load(json.loads(json.dumps(unresolved.state)))
    for obs in (resolved, bad, resolved, resolved):
        assert unresolved.step(obs) == restored.step(obs)
    out("selector_continuation", equal_future_steps=4)

    # Case 8: joint membership changes while every marginal stays fixed.
    only_coincidence = set(UNITS) - {"coincidence"}
    specialist = Selector(3, eligible=[0, 1, 2], disabled=only_coincidence)
    pair = Selector(3, eligible=[0, 1, 2], disabled=only_coincidence)
    single_obs = population(3, [(0.25, [0], [0]), (0.25, [1], [1]),
                                (0.25, [2], [2]), (0.25, [], [])])
    pair_obs = population(3, [(0.25, [0, 1], [0, 1]), (0.25, [2], [2]), (0.5, [], [])])
    assert single_obs["p"] == pair_obs["p"] and single_obs["q"] == pair_obs["q"]
    one = specialist.step(single_obs)
    two = pair.step(pair_obs)
    assert one["diagnostics"]["coincidence"] == [0, 0, 0]
    assert two["pay"][0] > one["pay"][0] and two["pay"][2] < one["pay"][2]
    out("joint_membership", specialist_pay=one["pay"], pair_pay=two["pay"],
        specialist_coincidence=one["diagnostics"]["coincidence"],
        pair_coincidence=two["diagnostics"]["coincidence"])

    # Added after the initial run: common observed share and common trace differ.
    exact, nearby = Selector(2, eligible=[0, 1]), Selector(2, eligible=[0, 1])
    for _ in range(200):
        for selector, share in ((exact, 0.1), (nearby, 361 / 3600)):
            selector.step(population(2, [(share, [0], [0]), (1 - share, [], [])]))
    histories = [format(x.state["h"][0], ".17g") for x in (exact, nearby)]
    absence = population(2, [(1.0, [], [])])
    exact_loss, nearby_loss = exact.step(absence), nearby.step(absence)
    assert exact_loss["diagnostics"]["latch"] == [1, 0]
    assert nearby_loss["diagnostics"]["latch"] == [1, 0]
    out("common_threshold_loss", historical_traces=histories,
        exact_common_loss_latch=exact_loss["diagnostics"]["latch"],
        nearby_common_loss_latch=nearby_loss["diagnostics"]["latch"])

    # v1.2 regression neighbours, declared after the initial boundary finding.
    below = Selector(2, eligible=[0, 1])
    for _ in range(200):
        below.step(population(2, [(0.099, [0], [0]), (0.901, [], [])]))
    below_loss = below.step(absence)
    assert below_loss["diagnostics"]["latch"] == [0, 0]
    slow = Selector(2, eligible=[0, 1])
    for _ in range(10):
        slow.step(population(2, [(0.8, [0], [0]), (0.2, [], [])]))
    slow.step(population(2, [(0.05, [0], [0]), (0.95, [], [])]))
    slow_prior_q, slow_prior_h = slow.state["q"][0], slow.state["h"][0]
    assert slow_prior_q < 0.1 and slow_prior_h >= 0.1
    slow_loss = slow.step(absence)
    assert slow_loss["diagnostics"]["latch"] == [1, 0]
    transient = Selector(2, eligible=[0, 1])
    transient.step(population(2, [(0.1, [0], [0]), (0.9, [], [])]))
    transient_loss = transient.step(absence)
    assert transient_loss["diagnostics"]["latch"] == [1, 0]
    out("loss_amendment_neighbours", below_common_loss_latch=below_loss["diagnostics"]["latch"],
        slow_prior_q=slow_prior_q, slow_prior_h=slow_prior_h,
        slow_loss_latch=slow_loss["diagnostics"]["latch"],
        one_piece_common_loss_latch=transient_loss["diagnostics"]["latch"])
    print("Audit cases completed. No Avida evolutionary run was performed.")


if __name__ == "__main__":
    main()
```

#### evidence/additional_check.py

```python
import sys
sys.path.insert(0,'temporal_selector')
from selector import Selector
from checks import obs
order=[2,0,1]
a=Selector(3,eligible=[0,2]); b=Selector(3,eligible=[order.index(i) for i in [0,2]])
cases=[obs([.2,0,0]),obs([.2,0,.3],pairs=[(0,2,.1)]),obs([0,0,.3],[.3,0,.3])]
for o in cases:
 transformed={'p':[o['p'][i] for i in order],'q':[o['q'][i] for i in order],
              'cooc':[[o['cooc'][i][j] for j in order] for i in order]}
 x=a.step(o)['pay']; y=b.step(transformed)['pay']
 assert all(abs(y[j]-x[i])<1e-12 for j,i in enumerate(order))
print('task relabelling with eligibility carried: 3 successive pay vectors commute')
```

### File hashes

These SHA256 values identify the code embedded above.

```text
19f431daf472fb2053900e0beeb9e125a7aa29cc5df69d00b2571dbb02bb22c9  temporal_selector/selector.py
b643bf938f72ebfca21725681caa43f7f15b6e47db61e8a84e4531ef24a43cef  temporal_selector/assay.py
ec5c53dbad409ba47604a148ed45ca205a036dd0d6971b249e8b58c9feaaec12  temporal_selector/runner.py
da584c20fe34d0c25bef30d7fb61d4475b2964e0ee2cf2b74b8f53f05150027e  temporal_selector/summarize.py
dff1e5b5b2c1f0db2bbf97245562aed95d984d6833be63b9de27ab8dc3f45246  temporal_selector/checks.py
b0c9d2fcb78bfe38ca3c7530730ff7c928e1187014a0e6905bdef867a9382041  temporal_selector/integration_checks.py
3c27658efc123ad0e47987adf8b418822265852d174a09454c61e6830e61d0cc  independent_test.py
ebb761e96736e2a52b000f3a58ce7c387be90854507871b4a745420f6ec9e1cf  evidence/additional_check.py
```

END OF REPORT
