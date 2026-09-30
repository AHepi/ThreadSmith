# Summary for the owner

Give a program the same three numbers, ask it for one answer in one problem and a different answer in another, but never tell it which problem applies. The proposed function experiment does this. Its population can contain specialists; one deterministic program cannot satisfy the different requests simultaneously.

The earlier report contributes useful distinctions between changing demands, acquiring capabilities and retaining them. Its warning about population reloads is supported by the source. Its proposed experiments remain designs, however, and several details need correction before their outcomes could answer the intended questions.

Checked: the report pins the 2021 release tag; the owner's named revision is 133 commits later. The central reward and task code is unchanged, but the versions must not be treated as identical. Other gaps concern input handling, episode lifetimes, historical ancestry and controls that alter several things together.

This review supplies smaller, explicitly limited versions and a code/configuration appendix. These preserve particular interactions without claiming the coverage of the original designs. Source inspection, analytical counterexamples and any reported engineering checks are separated from evolutionary results. The owner's reported measurements were not repeated.

The owner can take the report as a research agenda with testable mechanisms. It does not yet show sustained learning, identify universal functions of knowledge, or supply an implemented general system for creating new problems.

# Source claims checked

Checked: source comparison used the owner's `47f13dadb547fcf10f620ace60247f38b30b8b16` and the reviewer's release tag `c6179ffc617fdbc962b5a9c4de3e889e0ef2d94c`. Links below name the owner's revision. Paths are relative to `avida-core/`. A verdict concerns the exact claim, not the entire report. **Checked** means source text inspected; it does not mean the associated experiment was run.

| Claim | Verdict | Checked file and function; qualification |
|---|---|---|
| The 2.14.0 tag names `c6179ffc`. | holds | Git tag resolution. It is 133 commits behind the owner's `47f13dad`; identical-source assumption does not hold. |
| Save retains sequences, locations and selected metadata. | holds | [cPopulation.cc](https://github.com/devosoft/avida/blob/47f13dad/avida-core/source/main/cPopulation.cc), `SavePopulation`; `systematics/Genotype.cc`, `LegacySave`. Merit/gestation are sequence-group means; execution offsets and lineage labels are also written. |
| Load creates programs afresh and approximates remaining execution using merit. | holds | `cPopulation::LoadPopulation`: `SetupInject`, then mean-merit adjustment by saved gestation/remaining gestation. |
| CPU, RNG and resources are not restored as a complete world. | holds | `SavePopulation`/`LoadPopulation`; `cOrganism` constructor. Resource reinitialization belongs to a fresh process; loading into an existing process does not itself reset all resource pools. |
| Save/load logs are not complete checkpoints. | holds | Same serializer/loader. Optional group/avatar/rebirth fields do not supply the missing world state. |
| Save filename/options and optional Load update syntax are native. | holds | [SaveLoadActions.cc](https://github.com/devosoft/avida/blob/47f13dad/avida-core/source/actions/SaveLoadActions.cc), `cActionSavePopulation`, `cActionLoadPopulation`. `detail-UPDATE.spop`; historic defaults 1, other optional flags 0; omitted load-update leaves the current clock. |
| Release source applies to the owner's source unchanged. | holds in part | Core reward/task/analyze files are unchanged. Owner loading adds transmission-source/parasite handling; separate germline actions were added. Save/load argument syntax remains unchanged. |
| Zero-valued `pow` contributes 1; value 1 contributes 2. | holds in part | [cEnvironment.cc](https://github.com/devosoft/avida/blob/47f13dad/avida-core/source/main/cEnvironment.cc), `DoProcesses`: multiplier `2^(consumed*value)`. Twofold holds for the report's full-quality, no-resource, max=1 case. |
| Zero reward can still consume resources or produce products. | holds | `DoProcesses`; consumption and product conversion are independent of reward value. `cReactionProcess` constructor supplies defaults. |
| Task recording follows activation/requisite tests. | holds | `cEnvironment::TestOutput`, `TestRequisites`: task marked after these gates, but before resource processing. Exhaustion can prevent reward while leaving task recording intact. |
| Product transfers quantity; reaction requisite tests focal history. | holds in part | `LoadReactionProcess`, `DoProcesses`, `TestRequisites`. Product is scalar resource quantity. Ordinary heads uses focal history; additional stolen/deme histories exist outside this setup. Neither routes another program's numeric answer. |
| Exact `match_number` and argument-changing action exist. | holds | [cTaskLib.cc](https://github.com/devosoft/avida/blob/47f13dad/avida-core/source/main/cTaskLib.cc), `Load_MatchNumber`, `Task_MatchNumber`; `actions/EnvironmentActions.cc`, `cActionSetTaskArgInt`. Target is integer argument 0; threshold 0 gives exact matching. |
| Task arguments use commas; process/requisite fields use colons. | holds | `cArgSchema` constructor; `cEnvironment::LoadReaction`, `LoadReactionProcess`, `LoadReactionRequisite`. |
| B1 target changes preserve previously earned lifetime reward. | holds | `cActionSetTaskArgInt` changes only the argument; `cPhenotype::TestOutput`, `DivideReset`; immediate merit application defaults off. |
| Neutral echo/no-resource reactions supply no merit bonus. | holds | `DoProcesses`; `cReactionProcess` defaults. They still record task/reaction events and do not implement controller credit. |
| Stock heads/ancestor have 26 instructions/100 positions; copy .0075 and division insert/delete .05 are defaults. | holds | [avida.cfg](https://github.com/devosoft/avida/blob/47f13dad/avida-core/support/config/avida.cfg); `cAvidaConfig` declarations. `support/config/{instset-heads.cfg,default-heads.org}` supplies the set/sequence. Probabilities use different units. |
| Appendix explicitly disables every other change mechanism. | holds in part | `cAvidaConfig.h` has omitted zero-default point/parent insert/delete, translocation/LGT, Poisson translocation/LGT and HGT switches. Clean stock configuration gives the intended setting; the shown overrides alone do not lock all mechanisms. |
| Base merit, probabilistic scheduling, birth0 and prefer-empty settings exist. | holds | `cAvidaConfig`; `cPopulation::BuildTimeSlicer`, `PositionOffspring`. Stock base method is 4; constant method 0 needs its constant value. |
| Full cohort/credit contract needs source changes. | holds in part | Native `NUM_DEMES`, birth6 and `PositionDemeRandom` already isolate birth placement. Scheduler3/4 cases are commented out in `BuildTimeSlicer`; custom equal cohort budgets/persistent credits still need work. `UpdateMerit` updates phenotype and scheduler. |
| Proposed integration paths and native I/O/TestCPU hooks exist. | holds | `cWorld`, `cActionLibrary::buildDefaultActionLibrary`, `cPopulation::{ScheduleOrganism,ActivateOffspring,ActivateOrganism}`, `cTestCPU::{TestGenome,ProcessGestation}`, `cCPUTestInfo::UseManualInputs`, `cOrganism::DoOutput`; CMake compilation list. Existence does not implement the proposal. |
| Stock TestCPU is not the proposed episodic runner. | holds | `ProcessGestation` uses length-scaled time and division/death; `TestGenome_Body` can recurse for replication testing. `cHardwareCPU::Inst_TaskIO` outputs then reads. |
| `S114...` commands are extensions, rejected by stock Avida. | holds | `cActionLibrary` registrations; `cEventList::{AddEvent,LoadEventFile}`. No such native actions occur. |
| InjectRange endpoint is exclusive; event/Print/Exit syntax is native. | holds | `actions/PopulationActions.cc`, `cActionInjectRange`; `cEventList::AddEventFileFormat`; `PrintActions.cc`, `DriverActions.cc`. |
| LOAD/FILTER/RECALCULATE/DETAIL and named output columns are native. | holds | [cAnalyze.cc](https://github.com/devosoft/avida/blob/47f13dad/avida-core/source/analyze/cAnalyze.cc), `LoadFile`, `CommandFilter`, `BatchRecalculate`, `CommandDetail`; `cAnalyzeGenotype` field registration. `num_cpus` is supported. |
| Arbitrary triples can replace the example in native logic analysis. | holds in part | `BatchRecalculate` accepts them; `cTaskLib::SetupTests` assumes all eight input-bit combinations occur. Missing patterns can trigger assertions or invalid classification. `cEnvironment::SetupInputs` normally preserves coverage. |
| `-a -c ... -set ...` is native command syntax. | holds | `source/util/CmdLine.cc`, option parsing. |
| There are 77 listed logic tasks; updates differ from generations. | holds | `cTaskLib::AddTask` lists nine plus 68 classes, followed by other task families. `cWorld::CalculateUpdateSize`, `cStats::PrintTimeData`. The 5.4-billion-step calculation assumes full occupancy throughout. |
| Listed files support the requested actual ancestry analysis. | does not hold | `SavePopulation` with historic=0 omits historical groups; `GenotypeArbiter::ClassifyNewUnit` merges matching sequences. Historical groups alone are not a per-birth log. Add actual parent/child identities or narrow the ancestry claim. |

Checked additional measurement caveat: `cStats::PrintTasksData` reports last-lifetime task counts. `cPhenotype::SetupInject` clears those records and resets generation, age and CPU cycles. Reload-induced count/generation drops therefore need not indicate lost capability or altered evolutionary speed. Use frozen-sequence assays and accumulated births/instructions. Driver/event ordering also makes five fresh segments ending at label 1000 execute 5005 update iterations versus 5001 for one ending at 5000; specify exposure rather than silently equating labels.


# The critique of the six environments, reviewed

The question held fixed here is whether the earlier report accurately describes the machinery and proposes experiments capable of separating its claimed mechanisms from alternatives. The owner's broader question concerns environments in which new capabilities accumulate. Endogenous problem generation, untouched transfer tests and retention are the reviewer's added operational demands, not definitions supplied by the owner's question. A finite, supplied task can still require discovery of a previously absent implementation.

| Environment | What the critique identifies | Qualification or missing contrast |
|---|---|---|
| Fixed graded | Acquisition occurs under a supplied reward scheme; reward size, computational form and accessible paths vary together. | Predetermined task definitions do not make discovered implementations predetermined. Record acquisition and loss separately. |
| EQU only | Failure within the budget cannot distinguish an inaccessible route from a rare or slow one. | The standard ancestry and instruction set remain scaffolding. EQU acquisition would concern the absence of intermediate *task rewards*, not the absence of intermediate computations or designer assistance. |
| No task rewards | Replication and competition continue. | Incidental tasks can hitchhike with replication changes. A zero-reward task is an observation condition only after resource/requisite effects are checked. |
| Growing list | Its contents, NAND ordering, threshold and sampling interval are supplied. Schedule replay tests a role for responsiveness. | Record capabilities before reward activation. Crossing 10% at one snapshot can reflect a transient expansion. Exact NAND complexity rankings and the actual wrapper were not supplied for inspection. |
| Common tasks pay less | Depletion may create frequency dependence, coexistence or cycling; reloads can alter resources. | Resource consumption follows task executions, not simply the number of programs capable of a task. Measure execution rate, inflow, outflow and depletion. The report's heading is conditional on these kinetics. |
| Fixed large list | Simultaneous incentives and multiplicative rewards change the environment. | The 77 entries are listed Boolean task classes, not Avida's entire capability repertoire. Equalizing total reward would itself change the treatment; report reward and computation differences, then add a matched intervention only for a specified causal question. |

The shared restart criticism holds as a mechanism warning. Applying the same reload procedure to all treatments does not cancel a treatment-by-reload interaction. It does not follow that the existing results are unusable or that the direction of distortion is known. The proposed restart pilot changes random seeds as well as resetting state; it estimates the effect of that complete procedure, not the isolated effect of losing CPU registers. Resource-rich and curriculum conditions need their own restart contrasts before a fixed nine-task result is generalized to them.

Counts of generations, births and executed instructions answer different questions. Updates are an appropriate common time coordinate for one comparison; instruction expenditure is another. Neither should silently replace the other. Three seeds describe variability in those seeds, and the proposed five-percentage-point/10% thresholds are declared practical choices, not general uncertainty bounds.

# Designs B1, B2, B3 and C, reviewed

**B1: population-dependent numeric targets.** The explicit causal loop is output → modal value → complemented target → reward → subsequent population. It can track demands generated from population behavior. If the population mode follows each new target, complementation permits a two-value cycle; that is a concrete rival to cumulative learning. Removing feedback and replaying the target history tests the live dependency; a frozen target tests changing exposure. These controls are missing from B1's detailed batch plan. The complement rule, unsigned tie-breaking, interval and exact-match criterion remain designer choices. A changing target is not evidence of an expanding problem-solving method. The original 150–300-line allowance is plausible for a collector and boundary action, but excludes robust lifecycle tests; its runtime allowance is unmeasured.

**B2: generated input-to-output functions.** With K distinct eight-output vectors and a deterministic runner on identical inputs, a candidate matches at most one vector. Therefore its credit is at most 1/K; at K=16, its stipulated merit is at most 104.43 against base 100. Supplier merit can approach 200. This asymmetry is derived from the specification, not an evolutionary measurement. The setup can select population specialists; it supplies no problem cue that lets one candidate switch between incompatible functions. A cue would change the specification and require a way to interpret unfamiliar cues.

The prose also says demand is supplied only when some candidates solve it and some do not. The written bank-admission rule instead admits every selected nonconstant complete vector; `0<p<1` gates supplier credit, not bank admission. Universally unsolved problems can therefore occupy the bank. This matters for bootstrapping from the taskless ancestor. Empty and wholly unsolved banks must remain visible failures of the starting arrangement.

Exact vector matching, eight public examples, nonconstancy and supplier sampling determine the problem boundary. Fresh packets test a mapping outside its training examples, but finite agreement does not determine a function everywhere. Replay preserves donor demands while breaking their response to the recipient; it also changes problem difficulty relative to recipient competence. Freezing suppliers while regenerating examples freezes a function source, not its sampled vectors. Setting supplier credit to zero additionally changes its population and, unless the scheduler isolates budgets, computation distribution. These are tests of specified bundled interventions, not a uniquely isolated feedback variable. A 1,000–1,800-line implementation is conceivable, but the runner, scheduling, births, logging and tests prevent treating that count as a delivery estimate.

**B3: generated graphs.** Constructor outputs determine adjacency; navigator successes alter constructor and navigator credits. That is a concrete reciprocal loop. Sixteen nodes, bitmask decoding, reachability, local observations, move limits and the reward rule remain supplied. One analytical counterexample exposes a boundary: both graphs show start edges to nodes 1 and 2; in one graph only node 1 leads to the goal, and in the other only node 2 does. Their initial observations are identical and the wrong branch is a dead end. Reachability does not imply solvability from the information the navigator receives. This does not refute the stated prediction of *some* transfer; it blocks a general interpretation of the reachability filter.

Relabelling is useful, but raw numeric labels and bit positions change together. Preserve the topology and start/goal roles, and record that representational burden. Pair relabelled tests with unrelabelled archival graphs. A frozen graph bank and a donor-replayed bank cut different links. Constructor credit retains B2's admission-versus-payment ambiguity. The 600–1,000 additional lines are an unmeasured allowance; state-preserving input delivery and execution limits require tests beyond graph decoding.

**C: mutable assessors.** An assessor's output chooses a candidate and can causally affect its credit. That moves a decision computation into a mutable program. The hidden audit, payoff, pair formation and allowable decisions still determine what choices receive computational selection. The heading “Beyond computational selection” consequently overstates the departure, although the body correctly acknowledges that selection remains.

The assessor has an information limit. Let candidates return x and y, with public examples satisfying x=y. A supplier returning x and one returning y produce the same assessor packet. On audit examples with x≠y, the required decisions are opposite. No unchanged assessor can distinguish those packets. Distribution-specific predictive performance remains testable; unrestricted assessment does not follow.

The frozen-candidate assay, reversed candidate order and equal-candidate packets are useful controls. Add public-identical/audit-different packets to expose the information limit. The specified shuffle preserves invalid slots, leaving packet-dependent abstention intact; it also credits recipient assessors for decisions made elsewhere, changing their learning feedback. Compare choices on fixed packets before replication, then compare downstream evolution separately. An instruction ablation should alter a discrimination rather than merely cause timeout or invalid output. The proposed fixed comparator needs an actual heads-26 implementation with matched packet handling. Its existence cannot be inferred from a line count. The extra 500–900 lines and 3–8-hour allowance are unmeasured; public/audit packet sharing must be specified to make caching and cost accounting reproducible.

Across B2/B3/C, checked native `IO` outputs before receiving input. B2's first answer after three reads is therefore the fourth `IO`; C's answer after 24 reads is the 25th. Interactive B3 must say which observation the input half of a move-producing `IO` receives. Checked native age limits can also terminate a short sequence before the proposed episode budget. Neutral rewards alone do not create the promised isolated runner.

# Smaller versions

**S115-mini-v1 is a reduced specification**, not an implementation of the original contracts. The appendix supplies a combined patch of 204 added C++ lines for all four designs plus a 37-line configuration generator; no external experiment controller is omitted from that count. It changes `actions/EnvironmentActions.cc`, adds `actions/S115Mini.h`, and changes `cpu/cTestCPU.cc` and `main/cEnvironment.cc`, all under `avida-core/source/`.

Generate separate `B1/`, `B2/`, `B3/`, `C/` directories from the pinned complete stock configuration. Each contains `avida.cfg`, `environment.cfg`, `events.cfg`, `default-heads.org` and `instset-heads.cfg`. The appendix fixes every changed value; all others remain the pinned defaults. Seeds are 11501–11503 in separate directories. Run continuously through update label 5000. No population reload occurs.

B1 has 16 cells; B2/B3 have two groups of 16, and C has three. Each cell starts with the supplied ancestor. B2/B3/C use native deme-restricted births, no migration and global probabilistic merit scheduling. They disable age death and speculative execution. This drops the original equal cohort execution budgets and native age limit. Scoring occurs every 100 updates; merits are refreshed every update to `100*2^q`. Unknown sequences receive base merit. Birth/division resets may therefore persist for up to one update. Credits are keyed by sequence within each group.

The shared runner uses fresh TestCPU copies, zero test mutation rates, one generation and a 2,000-dispatch bound. It bypasses native reaction detection during episodes, preventing arbitrary packets from entering the named-logic detector. The first qualifying output is used; division or timeout without it fails. A separate RNG seeded `RANDOM_SEED+10000019` generates nonnegative 31-bit inputs and selections. Sequences, supplied packets, qualifying outputs, dispatch counts and credits are logged. The bridge assumes one serialized world per process; it is not a concurrent evaluation service.

| Version | Exact reduced interaction | Lost scope and contrary result |
|---|---|---|
| B1 | Every 100 updates, count each occupied program's latest buffered output once. Complement the modal unsigned value; resolve ties ascending; retain target if no outputs. Native exact-match reaction supplies reward. | Buffered outputs can predate the interval. A fixed-output population should change target once and then hold it. A two-value cycle supplies no evidence of retention. |
| B2 | Select one supplier cell uniformly; evaluate two fresh triples. Both outputs must exist and differ. Every candidate receives q=1 for matching both, otherwise 0. Only the selected supplier sequence receives 1−p when candidate match fraction satisfies 0<p<1. | One function, two examples, no transfer assay. Invalid supplier means zero credits. Later additional unscored packets can challenge apparent matching. |
| B3 | Select one constructor; its first qualifying word encodes a four-node graph in its low 16 bits, four bits per row; clear self-edges. Require a route 0→3. Each navigator receives `(node,mask,3)` and retains CPU state across at most eight legal moves. Success gives q=1; constructor credit uses B2's rule. | One graph, four nodes. Invalid edge/node fails. After a move, clear input history and reset the input pointer; the next IO reads the new packet. The move-producing IO has already read one old-packet value. This explicit extra read differs from the original contract. Relabelling transfer remains untested. |
| C | Select a supplier and two distinct candidate cells in random order; use two public and two audit triples. Require public outputs, supplier audit outputs and nonconstant supplier public outputs. Missing candidate audit output is a mismatch. Each assessor reads six public integers then chooses 0/1. Candidates receive their selection fractions; assessor q is 1/0 for the audit-favored/other candidate, or .5 on ties. Invalid decisions earn zero and allocate no win. | One pair; no supplier reward. Unselected candidate sequences receive zero; identical sequences share average credit per presentation. This preserves mutable executed choice but omits three-way reciprocal selection and the independent final assay. |

No frozen/replay controller for B2/B3/C is included; these miniatures make the operations inspectable and cannot alone identify the necessity of live feedback. B1 frozen/replay controls need no additional C++: replace its MiniB1 event with native `SetTaskArgInt 0 0 TARGET` events at the donor's logged update labels. Freeze after the chosen boundary by omitting subsequent target changes. Use an independent donor and retain the full live history.

**Cost, calculated rather than timed:** full occupancy through label 5000 gives approximately 2.4/4.8/4.8/7.2 million live dispatches for B1/B2/B3/C. Across 51 scoring boundaries, additional episode ceilings are 0/3.468/1.734/2.856 million. Construction, injection tests, scans, logging, compilation and independent assays are extra. The original hours-per-run allowances cannot be transferred to these small worlds. Three seeds triple work; use at most three Avida processes. All four generated seed-11501 runs completed through label 5000 here, with observed times 0.71/3.82/2.80/6.63 seconds. These used optimized stock units and unoptimized modified units on this machine; they are not predictions for the owner's machine or expanded designs.


# Measures and references, reviewed

The retention matrix should keep problem identity, input packets, budgets and success definitions fixed across dates. Report population coverage and within-program capability combinations separately. A union of specialists can grow while no individual accumulates methods. An archived sequence demonstrates retrievability from the external archive; it is not evidence that the living population retained it. The observation protocol should distinguish a slow capability, a missing response and nonreplication.

The never-rewarded battery provides finite coverage of a declared expression grammar. Check overlap against every rewarded bank, not only the final bank, and label finite-signature equivalence as such. Repeatedly examining a held-out set while changing the design turns it into development evidence. Add separately frozen input families such as equal inputs and arithmetic boundary values; report them separately from IID packets. Checked native logic-task detection requires input bit-pattern coverage, so arbitrary manual triples need the correction in the source table. The supplied example triple contains all eight patterns.

Ablation plus restoration can identify present dependence, including I/O phase dependence. To claim historical reuse, also retain the earlier sequence and actual ancestry, reconstruct the relevant changes and test the old component's contribution before and after the new capability appears. Group ablations address redundancy but can destroy general execution rather than a particular module. Include a replication/control capability and matched disruption checks.

The adaptation assay changes starting sequence composition, abundance and replication characteristics together. State whether the target is an inherited population's adaptation or an individual sequence's evolvability. Reinitialization can be symmetric without reconstructing the prior living state. The calculation of 22.1184 billion maximum VM instructions for six fully distinct snapshots, 512 packets and 2,000 instructions is correct; evaluating expression trees, interpreting outputs, logging and failed episodes add work. No hours-per-run conversion follows without throughput measurements.

Every entry below is **Checked**, at the access level stated. The ten references' identifiers and broad attributions hold; no invented citation was found. Abbreviated titles are expanded where useful. None supplies an outcome for the proposed controllers.

| Reference and primary source | Checked scope and limitation |
|---|---|
| Lenski et al. (2003), *The evolutionary origin of complex features*, Nature 423:139–144, [doi:10.1038/nature01568](https://www.nature.com/articles/nature01568) | Publisher abstract: earlier functions and instruction changes contributed to complex task acquisition; no particular intermediate was essential. Prescribed task setting. |
| Ofria & Wilke (2004), *Avida: A Software Platform for Research in Computational Evolutionary Biology*, Artificial Life 10:191–229, [doi:10.1162/106454604773563612](https://authors.library.caltech.edu/records/2h3br-gvn73) | Author-repository abstract: platform/configuration/analysis description. Current implementation details require the source audit above. |
| Chow et al. (2004), *Adaptive radiation from resource competition in digital organisms*, Science 305:84–86, [doi:10.1126/science.1096307](https://cse.msu.edu/~ofria/pubs/2004ChowEtAl.pdf) | Relevant full text: diversification depends on resource supply regime; neither scarcity alone nor a finite resource list implies expanding scope. |
| Johnson & Wilke (2004), *Evolution of resource competition between mutually dependent digital organisms*, Artificial Life 10:145–156, [doi:10.1162/106454604773563577](https://pubmed.ncbi.nlm.nih.gov/15107227/) | Indexed primary abstract: two depletable, coupled resources. Earlier report appropriately limited its claim to that scope. |
| Zaman et al. (2014), PLOS Biology 12:e1002023, [doi:10.1371/journal.pbio.1002023](https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002023) | Full text: nine-function setting and frozen/replayed interaction controls. Source changes sampled replacement sequences in ongoing runs; this is not whole-world restarting. |
| Ray (1991), *An approach to the synthesis of life*, Artificial Life II:371–408, [author chapter](https://tomray.me/pubs/alife2/Ray1991AnApproachToTheSynthesisOfLife.pdf) | Relevant full text: spontaneously arising use of other programs' copying routines. Some other illustrated constructions were hand-prepared; the report does not attribute all of them to spontaneous origin. |
| Lehman & Stanley (2011), *Abandoning Objectives: Evolution through the Search for Novelty Alone*, Evolutionary Computation 19:189–223, [doi:10.1162/EVCO_a_00025](https://www.cs.swarthmore.edu/~meeden/DevelopmentalRobotics/lehman_ecj11.pdf) | Full text: novelty uses a supplied behavior representation and distance. The report's caveat holds. |
| Brant & Stanley (2017), *Minimal Criterion Coevolution: A New Approach to Open-Ended Search*, GECCO:67–74, [doi:10.1145/3071178.3071186](https://www.cmap.polytechnique.fr/~nikolaus.hansen/proceedings/2017/GECCO/proceedings/proceedings_files/pap140s3-file1.pdf) | Full text: accepted mazes need a solver and accepted navigators need a solvable maze. B3's 1−p payoff is a different rule; the cited work also prepares viable starting queues. |
| Wang et al. (2019), *POET: Open-Ended Coevolution of Environments and Their Optimized Solutions*, GECCO:142–151, [doi:10.1145/3321707.3321799](https://doi.org/10.1145/3321707.3321799), [preprint](https://arxiv.org/abs/1901.01753) | Conference metadata and full preprint: paired environments/solvers and transfer. The preprint's longer title differs legitimately from the conference title. |
| Mouret & Clune (2015), *Illuminating search spaces by mapping elites*, [arXiv:1504.04909](https://arxiv.org/abs/1504.04909) | Preprint: archive coordinates are user chosen. Archive coverage is distinct from live population retention. |

Checked omissions directly relevant here are Schmidhuber's [PowerPlay (2013), doi:10.3389/fpsyg.2013.00313](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2013.00313/full), whose main framework joins new-task discovery to retention checks; Ackley and Littman's [Interactions between Learning and Evolution (1991)](https://www.cs.unm.edu/~ackley/AckleyLittman1991.pdf), whose [author description](https://www.cs.unm.edu/~ackley/) discusses inherited internal reinforcement teachers; and Cliff and Miller's [Tracking the Red Queen (1995), doi:10.1007/3-540-59496-5_300](https://link.springer.com/chapter/10.1007/3-540-59496-5_300), whose publisher abstract addresses misleading contemporaneous performance measures. Access was relevant full text for PowerPlay, author summary for Ackley–Littman, and abstract for Cliff–Miller. These connect respectively to B2/retention, C, and time-indexed assessment; their results are not Avida controller results.


# What the report adds, and what it does not

It adds an actionable separation of generated demands, retained capabilities, transfer and causal evaluation. The restart warning, resource caution, replay ideas and fixed-candidate assessor assay have specific mechanisms and contrary outcomes. They turn broad claims into questions experiments can address.

It does not supply implementations of its original controllers, observed learning curves for them, a complete checkpoint, or a criterion for every kind of knowledge. Its finite tests do not make indefinite growth measurable, and fixed designer rules do not themselves prevent programs from discovering implementations. Removing designer rules entirely is not a demonstrated requirement of the owner's project.

The central rival remains demand tracking with forgetting. Compare a live history with frozen/replayed demands while holding the measurement packets fixed, and examine whether the living population retains earlier capabilities. Identical outcomes would leave the live feedback's necessity unresolved; a difference would still need its altered exposure and computation explained.

# Assumptions and what you are unsure of

The hard-to-vary mapping uses “population files” (A) for the proposed state carrier, “bank” (B2/B3) for generated demands, “assessor” (C) for mutable evaluation, and “retention” (D) for persistence under a fixed assay. Given jobs are accurate source checking and workable smaller designs. The owner-fixed constraints are Avida/source compatibility and the stated resource limits. The miniatures retain the supplied ancestor/instruction set while explicitly changing other pilot settings. Transfer, endogenous demands and isolated attribution are operational jobs added by the earlier reviewer or this review, explicitly distinguished from the owner's general knowledge claim.

| Part | Hard-to-vary mark and reason |
|---|---|
| Incomplete-checkpoint warning | Held by checked omissions from serialization and fresh program construction. The size of its experimental effect remains unknown; compare each treatment with continuous execution. |
| An exclusive reading of the environment claim | Loose: internal computation and environmental demands jointly affect performance. Changing routing with the environment fixed is an admitted alternative intervention. |
| Live feedback as necessary for retention | Unknown: donor replay can preserve varying demands without recipient feedback. The proposed controls can test the difference. |
| Stable archival tests | Held for the added comparison job: changing their denominator can change the apparent trend without changing capability. |
| Novelty rule and numeric pilot limits | Loose design choices. Different limits retain the diagnostic job; they were built or asserted, not inferred necessities. |
| An external audit in C | Fixed by the earlier reviewer: exact matching and audit scoring are supplied design standards. Their adequacy for the owner's broader knowledge question remains open. |
| Internal mutable decision route | Unknown as an evolutionary contribution. Fixed-packet intervention can test whether changing an assessor changes discrimination and resulting credits. |
| Owner's prior measurements | Borrowed evidence from the supplied account, with raw records unavailable. They do not by themselves identify universal minimum functions. |

Swapping complement targets for replay leaves changing exposure while removing live feedback. Flipping a rising learning curve to a flat one can fit several of the report's permissive predictions; those curves alone do not identify a mechanism. Novelty and current solvability pull against one another: admitting unsolved demands can stall feedback; requiring solvability can exclude the initially inaccessible. Empty-bank rate, invalid responses and lost archival capabilities expose those trade-offs rather than absorbing them into “no learning.”

**Observed engineering checks:** the owner revision and modified translation units built with GCC 13. Six self-authored cases exited with code 0: B1's constant-zero output changed its target to −1; B2's eight matching and eight mismatching candidates received 1/0 credits and the supplier .5; B3's 0→1→3 route succeeded while the invalid second move failed; C's fixed candidate pair had audit counts 0/2, and replacing constant-choice-0 assessors with constant-choice-1 assessors changed wins from 16:0 to 0:16 and assessor credit from 0 to 1; the unmodified ancestor produced an invalid B2 bank with no credits. The fixture script is included. These cases exercise controller behavior and include failures; their programs were written for the checks, not discovered by digital evolution.

The original B1/B2/B3/C systems, 50,000-update treatments, retention matrices and independent transfer assays were not run here. The original owner's executable, wrapper, raw populations and reported measurements were unavailable. The miniatures do not implement the requested per-birth ancestry log or frozen/replayed B2/B3/C treatments. Signed arithmetic behavior and generalization outside the sampled inputs remain limitations; no learning conclusion is inferred from compilation, fixtures or the short runs.

The next experimental step is to add the analytically ambiguous graph pair and public-identical/opposite-audit assessor packets to the acceptance suite before a long run. Preserve the first outputs and classify failures as controller, input preparation or candidate failures before changing the design. Passing engineering cases supports their stated behavior only.

# Appendix

Save the following blocks as `mini-all.patch`, `setup.py` and `smoke.py`. The combined patch installs all four modes; each mode runs independently. It contains 204 added physical C++ lines, including shared code. Individual mode extracts require 36/107/118/126 lines respectively; the combined form avoids repeating the bridge here. The setup and fixture scripts are additional scaffolding, not hidden controllers.

Use a fresh local checkout named `avida` at `47f13dadb547fcf10f620ace60247f38b30b8b16`, and fresh run/test directories. Checked: the diff applied to that revision and its modified translation units compiled and linked. The configuration generator is the exact specification of each complete file: it copies the pinned defaults and replaces the displayed assignments. It supplies seed 11501; make separate directories and change RANDOM_SEED for 11502/11503. Fixture outputs test the reduced mechanics only.

```bash
git -C avida submodule update --init libs/apto
git -C avida apply ../mini-all.patch
AVIDA_DISABLE_BACKTRACE=1 cmake -S avida -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_POLICY_VERSION_MINIMUM=3.5
AVIDA_DISABLE_BACKTRACE=1 cmake --build build --target avida -j 3
python3 setup.py avida small-runs
python3 smoke.py build/bin/avida small-runs small-smoke
(cd small-runs/B2 && ../../build/bin/avida -c avida.cfg)
```

The last command runs B2; change that directory to B1, B3 or C for the other modes. The four generated `events.cfg` files call only their corresponding controller. No source or results are published by these commands.

## mini-all.patch

```diff
diff --git a/avida-core/source/actions/EnvironmentActions.cc b/avida-core/source/actions/EnvironmentActions.cc
index b57b66f18..4caf519d5 100644
--- a/avida-core/source/actions/EnvironmentActions.cc
+++ b/avida-core/source/actions/EnvironmentActions.cc
@@ -36,6 +36,7 @@
 #include "cStats.h"
 #include "cUserFeedback.h"
 #include "cWorld.h"
+#include "S115Mini.h"
 
 class cActionInjectResource : public cAction
 {
@@ -1703,6 +1704,10 @@ public:
 
 void RegisterEnvironmentActions(cActionLibrary* action_lib)
 {
+  action_lib->Register<cActionMiniB1>("MiniB1");
+  action_lib->Register<cActionMiniB2>("MiniB2");
+  action_lib->Register<cActionMiniB3>("MiniB3");
+  action_lib->Register<cActionMiniC>("MiniC");
   action_lib->Register<cActionSetFracDemeTreatable>("SetFracDemeTreatable");
   action_lib->Register<cActionDelayedDemeEvent>("DelayedDemeEvent");
   action_lib->Register<cActionDelayedDemeEventsPerSlots>("DelayedDemeEventsPerSlots");
diff --git a/avida-core/source/cpu/cTestCPU.cc b/avida-core/source/cpu/cTestCPU.cc
index 0c317e394..5d3c8bff2 100644
--- a/avida-core/source/cpu/cTestCPU.cc
+++ b/avida-core/source/cpu/cTestCPU.cc
@@ -21,6 +21,9 @@
  */
 
 #include "cTestCPU.h"
+#include <functional>
+extern int s115_budget;
+extern std::function<bool(cOrganism&, Apto::Array<int>&)> s115_step;
 
 #include "avida/output/File.h"
 
@@ -151,6 +154,7 @@ bool cTestCPU::ProcessGestation(cAvidaContext& ctx, cCPUTestInfo& test_info, int
   ConstInstructionSequencePtr seq;
   seq.DynamicCastFrom(organism.UnitGenome().Representation());
   int time_allocated = m_world->GetConfig().TEST_CPU_TIME_MOD.Get() * seq->GetSize();
+  if (s115_budget > 0) time_allocated = s115_budget;
   time_allocated += m_res_cpu_cycle_offset; // If the resource offset has us starting at a different time, adjust @JEB
 
   // Prepare the inputs...
@@ -175,6 +179,7 @@ bool cTestCPU::ProcessGestation(cAvidaContext& ctx, cCPUTestInfo& test_info, int
     UpdateResources(ctx, time_used);
     
     organism.GetHardware().SingleProcess(ctx);
+    if (s115_step && !s115_step(organism, input_array)) break;
   }
   
   organism.GetHardware().SetTrace(HardwareTracerPtr(NULL));
diff --git a/avida-core/source/main/cEnvironment.cc b/avida-core/source/main/cEnvironment.cc
index 6ecb24642..9b4396998 100644
--- a/avida-core/source/main/cEnvironment.cc
+++ b/avida-core/source/main/cEnvironment.cc
@@ -20,6 +20,7 @@
  */
 
 #include "cEnvironment.h"
+extern bool s115_active;
 
 #include "avida/Avida.h"
 
@@ -1318,6 +1319,7 @@ bool cEnvironment::TestOutput(cAvidaContext& ctx, cReactionResult& result,
                               const Apto::Array<double>& rbins_count,
                               bool is_parasite, cContextPhenotype* context_phenotype) const
 {
+  if (s115_active) return false;
   //flag to skip processing of parasite tasks
   bool skipProcessing = false;
   
diff --git a/avida-core/source/actions/S115Mini.h b/avida-core/source/actions/S115Mini.h
new file mode 100644
--- /dev/null
+++ b/avida-core/source/actions/S115Mini.h
@@ -0,0 +1,192 @@
+// S115-mini-v1: continuous, finite, reduced-scope experiments.
+#include "cTestCPU.h"
+#include "cCPUTestInfo.h"
+#include <functional>
+#include <fstream>
+#include <map>
+#include <string>
+#include <vector>
+#include <cstdint>
+
+bool s115_active=false;
+int s115_budget=0;
+std::function<bool(cOrganism&, Apto::Array<int>&)> s115_step;
+
+class cActionMiniB1 : public cAction {
+public:
+  cActionMiniB1(cWorld* w, const cString& a, Feedback&) : cAction(w,a) {}
+  static const cString GetDescription() { return "No arguments"; }
+  void Process(cAvidaContext&) {
+    std::map<uint32_t,int> n;
+    cPopulation& p=m_world->GetPopulation();
+    for (int i=0;i<p.GetSize();++i) if (p.GetCell(i).IsOccupied()) {
+      const tBuffer<int>& b=p.GetCell(i).GetOrganism()->GetOutputBuf();
+      if (b.GetNumStored()) ++n[uint32_t(b[0])];
+    }
+    int count=0; uint32_t modal=0;
+    for (const auto& z:n) if (z.second>count) { count=z.second; modal=z.first; }
+    int target=m_world->GetEnvironment().GetTask(0).GetArguments().GetInt(0);
+    if (count) {
+      uint32_t v=~modal;
+      target=v<=0x7fffffffU ? int(v) : int(int64_t(v)-4294967296LL);
+      m_world->GetEnvironment().GetTask(0).GetArguments().SetInt(0,target);
+    }
+    std::ofstream log("mini-b1.log",std::ios::app);
+    log<<m_world->GetStats().GetUpdate()<<' '<<n.size()<<' '<<count<<' '<<modal<<' '<<target<<'\n';
+  }
+};
+
+class MiniBase : public cAction {
+protected:
+  typedef std::vector<cOrganism*> Group;
+  typedef std::pair<bool,int> Answer;
+  std::map<std::string,double> q[3];
+  Apto::RNG::AvidaRNG rng;
+  std::ofstream log;
+  std::string Key(cOrganism* o) { return (const char*)o->GetGenome().Representation()->AsString(); }
+  Apto::Array<int> Packet() {
+    Apto::Array<int> a(3);
+    for (int i=0;i<3;++i) a[i]=rng.GetUInt(2147483647);
+    return a;
+  }
+  void Run(cOrganism* source, Apto::Array<int> a, int reads,
+           std::function<bool(int,cOrganism&,Apto::Array<int>&)> output) {
+    cAvidaContext ctx(&m_world->GetDriver(),rng); s115_active=true;
+    cTestCPU cpu(ctx,m_world); cCPUTestInfo info(1);
+    info.UseManualInputs(a); s115_budget=2000;
+    int prior_reads=0, seen=0, used=0;
+    log<<"E "<<Key(source)<<' '<<reads;
+    for (int i=0;i<a.GetSize();++i) log<<' '<<a[i];
+    log<<'\n';
+    s115_step=[&](cOrganism& o,Apto::Array<int>& inputs) {
+      ++used; int total=o.GetOutputBuf().GetTotal();
+      if (total>seen && prior_reads>=reads) {
+        int value=o.GetOutputBuf()[0]; log<<"O "<<used<<' '<<value<<'\n';
+        if (!output(value,o,inputs)) return false;
+      }
+      seen=total; prior_reads=o.GetInputBuf().GetTotal(); return true;
+    };
+    cpu.TestGenome(ctx,info,source->GetGenome());
+    s115_step={}; s115_budget=0; s115_active=false;
+    log<<"Z "<<used<<' '<<info.GetTestPhenotype().GetNumDivides()<<'\n';
+  }
+  Answer Out(cOrganism* o,Apto::Array<int> a) {
+    Answer result(false,0);
+    Run(o,a,a.GetSize(),[&](int v,cOrganism&,Apto::Array<int>&) { result=Answer(true,v); return false; });
+    return result;
+  }
+  virtual void Score(Group* r)=0;
+public:
+  MiniBase(cWorld* w,const cString& a) : cAction(w,a),
+    rng(w->GetConfig().RANDOM_SEED.Get()+10000019),log("mini.log") {}
+  static const cString GetDescription() { return "No arguments; invoke every update"; }
+  void Process(cAvidaContext& ctx) {
+    cPopulation& p=m_world->GetPopulation(); int u=m_world->GetStats().GetUpdate();
+    if (u%100==0) {
+      Group r[3]; for (auto& scores:q) scores.clear(); log<<"U "<<u<<'\n';
+      for (int i=0;i<p.GetSize();++i) if (p.GetCell(i).IsOccupied()) {
+        int d=p.GetCell(i).GetDemeID(); cOrganism* o=p.GetCell(i).GetOrganism();
+        r[d].push_back(o); log<<"S "<<i<<' '<<d<<' '<<Key(o)<<'\n';
+      }
+      Score(r); log.flush();
+    }
+    for (int i=0;i<p.GetSize();++i) if (p.GetCell(i).IsOccupied()) {
+      int d=p.GetCell(i).GetDemeID(); std::string key=Key(p.GetCell(i).GetOrganism());
+      auto it=q[d].find(key); double credit=it==q[d].end()?0:it->second;
+      p.UpdateMerit(ctx,i,100*pow(2.0,credit));
+      cPhenotype& phenotype=p.GetCell(i).GetOrganism()->GetPhenotype();
+      if (!phenotype.GetGestationTime()) phenotype.SetLifeFitness(0);
+    }
+  }
+};
+
+class cActionMiniB2 : public MiniBase {
+  void Score(Group* r) {
+    if (r[0].empty() || r[1].empty()) { log<<"EMPTY\n"; return; }
+    cOrganism* supplier=r[0][rng.GetUInt(r[0].size())];
+    Apto::Array<int> a=Packet(), b=Packet(); Answer x=Out(supplier,a), y=Out(supplier,b);
+    log<<"BANK "<<Key(supplier)<<'\n';
+    if (!x.first || !y.first || x.second==y.second) { log<<"INVALID\n"; return; }
+    int matches=0;
+    for (auto o:r[1]) {
+      bool ok=Out(o,a)==x && Out(o,b)==y; matches+=ok; q[1][Key(o)]=ok;
+      log<<"Q 1 "<<Key(o)<<' '<<ok<<'\n';
+    }
+    double p=double(matches)/r[1].size();
+    q[0][Key(supplier)]=(p>0 && p<1)?1-p:0;
+    log<<"Q 0 "<<Key(supplier)<<' '<<q[0][Key(supplier)]<<'\n';
+  }
+public:
+  cActionMiniB2(cWorld* w,const cString& a,Feedback&) : MiniBase(w,a) {}
+};
+
+class cActionMiniB3 : public MiniBase {
+  void Score(Group* r) {
+    if (r[0].empty() || r[1].empty()) { log<<"EMPTY\n"; return; }
+    cOrganism* constructor=r[0][rng.GetUInt(r[0].size())]; Answer z=Out(constructor,Packet());
+    if (!z.first) { log<<"INVALID\n"; return; }
+    unsigned graph=unsigned(z.second)&65535U&~0x8421U, reached=1;
+    for (int k=0;k<4;++k) for (int i=0;i<4;++i) if (reached&(1U<<i)) reached|=(graph>>(4*i))&15U;
+    log<<"GRAPH "<<Key(constructor)<<' '<<graph<<'\n';
+    if (!(reached&8)) { log<<"UNREACHABLE\n"; return; }
+    int successes=0;
+    for (auto o:r[1]) {
+      int node=0,moves=0; bool success=false; Apto::Array<int> a(3);
+      a[0]=0; a[1]=graph&15; a[2]=3;
+      Run(o,a,3,[&](int v,cOrganism& program,Apto::Array<int>& inputs) {
+        ++moves; if (v<0 || v>3 || !(graph&(1U<<(4*node+v)))) return false;
+        node=v; log<<"MOVE "<<node<<'\n';
+        if (node==3) { success=true; return false; }
+        if (moves==8) return false;
+        inputs[0]=node; inputs[1]=(graph>>(4*node))&15; inputs[2]=3;
+        program.ResetInput(); return true;
+      });
+      successes+=success; q[1][Key(o)]=success; log<<"Q 1 "<<Key(o)<<' '<<success<<'\n';
+    }
+    double p=double(successes)/r[1].size();
+    q[0][Key(constructor)]=(p>0 && p<1)?1-p:0;
+    log<<"Q 0 "<<Key(constructor)<<' '<<q[0][Key(constructor)]<<'\n';
+  }
+public:
+  cActionMiniB3(cWorld* w,const cString& a,Feedback&) : MiniBase(w,a) {}
+};
+
+class cActionMiniC : public MiniBase {
+  void Score(Group* r) {
+    if (r[0].empty() || r[1].size()<2 || r[2].empty()) { log<<"EMPTY\n"; return; }
+    cOrganism* supplier=r[0][rng.GetUInt(r[0].size())];
+    unsigned ai=rng.GetUInt(r[1].size()), bi=rng.GetUInt(r[1].size()-1);
+    if (bi>=ai) ++bi;
+    cOrganism* candidate[2]={r[1][ai],r[1][bi]};
+    Apto::Array<int> public_data(6); int audit[2]={0,0}, first=0; bool constant=true;
+    for (int k=0;k<4;++k) {
+      Apto::Array<int> a=Packet(); Answer expected=Out(supplier,a);
+      Answer result[2]={Out(candidate[0],a),Out(candidate[1],a)};
+      if (!expected.first || (k<2 && (!result[0].first || !result[1].first))) { log<<"INVALID\n"; return; }
+      if (k==0) first=expected.second;
+      if (k==1) constant=first==expected.second;
+      for (int j=0;j<2;++j) {
+        if (k<2) public_data[3*k+j+1]=result[j].second;
+        else audit[j]+=result[j]==expected;
+      }
+      if (k<2) public_data[3*k]=expected.second;
+    }
+    if (constant) { log<<"CONSTANT\n"; return; }
+    log<<"PAIR "<<Key(supplier)<<' '<<Key(candidate[0])<<' '<<Key(candidate[1])<<' '<<audit[0]<<' '<<audit[1]<<'\n';
+    int wins[2]={0,0};
+    for (auto assessor:r[2]) {
+      Answer choice=Out(assessor,public_data); double credit=0;
+      if (choice.first && (choice.second==0 || choice.second==1)) {
+        int j=choice.second; ++wins[j];
+        credit=audit[0]==audit[1]?0.5:double(audit[j]>audit[1-j]);
+      }
+      q[2][Key(assessor)]=credit; log<<"Q 2 "<<Key(assessor)<<' '<<credit<<'\n';
+    }
+    for (int j=0;j<2;++j) q[1][Key(candidate[j])]+=double(wins[j])/r[2].size();
+    if (Key(candidate[0])==Key(candidate[1])) q[1][Key(candidate[0])]*=0.5;
+    log<<"WINS "<<wins[0]<<' '<<wins[1]<<'\n';
+    // Supplier selection is omitted in this miniature; its cohort evolves by replication.
+  }
+public:
+  cActionMiniC(cWorld* w,const cString& a,Feedback&) : MiniBase(w,a) {}
+};
```

## setup.py — exact configuration and event files

```python
#!/usr/bin/env python3
# Usage: python setup.py /path/to/avida-checkout /path/to/run-root
from pathlib import Path
import re, shutil, sys
source, destination = map(Path, sys.argv[1:])
config = source / 'avida-core/support/config'
base = (config / 'avida.cfg').read_text()
common = dict(RANDOM_SEED=11501, WORLD_X=16, WORLD_Y=2, WORLD_GEOMETRY=2,
              NUM_DEMES=2, BIRTH_METHOD=6, PREFER_EMPTY=1, SLICING_METHOD=1,
              BASE_MERIT_METHOD=0, BASE_CONST_MERIT=100, DEATH_METHOD=0,
              SPECULATIVE=0, COPY_MUT_PROB=0.0075, DIVIDE_INS_PROB=0.05,
              DIVIDE_DEL_PROB=0.05, MIGRATION_RATE=0, DEMES_MIGRATION_RATE=0,
              EVENT_FILE='events.cfg', ENVIRONMENT_FILE='environment.cfg')
for mode, demes in [('B1', 1), ('B2', 2), ('B3', 2), ('C', 3)]:
    run = destination / mode
    run.mkdir(parents=True, exist_ok=True)
    values = dict(common, NUM_DEMES=demes, WORLD_Y=demes)
    if mode == 'B1':
        values.update(BASE_MERIT_METHOD=4, DEATH_METHOD=2, BIRTH_METHOD=0)
    text = base
    for name, value in values.items():
        text, count = re.subn(r'^' + name + r'\s+.*$', f'{name} {value}', text, flags=re.M)
        if count == 0: text += f'\n{name} {value}\n'
        assert count <= 1, name
    (run / 'avida.cfg').write_text(text)
    for name in ['default-heads.org', 'instset-heads.cfg']:
        shutil.copyfile(config / name, run / name)
    environment = ('REACTION TARGET match_number:target=0,threshold=0,halflife=1 '
                   'process:value=1:type=pow:max=1 requisite:max_count=1\n') if mode == 'B1' else (
                   'REACTION OBS echo process:value=0:type=pow:max=1 requisite:max_count=1\n')
    (run / 'environment.cfg').write_text(environment)
    events = [f'u begin InjectRange default-heads.org 0 {16*demes}']
    events += ['u 100:100:5000 MiniB1'] if mode == 'B1' else [f'u 0:1:5000 Mini{mode}']
    events += ['u 0:100:5000 PrintAverageData', 'u 0:100:5000 PrintCountData',
               'u 0:100:5000 PrintTimeData',
               'u 0:100:5000 SavePopulation filename=detail:save_historic=0', 'u 5000 Exit']
    (run / 'events.cfg').write_text('\n'.join(events) + '\n')
```

## smoke.py — reproducible authored cases

```python
from pathlib import Path
import shutil, subprocess, json, sys
# Usage: python smoke.py /path/to/avida-mini /path/to/run-root /path/to/smoke-root
binary, runs, tests = [Path(x).resolve() for x in sys.argv[1:]]
ancestor=(runs/'B2/default-heads.org').read_text()
header='#inst_set heads_default\n#hw_type 0\n'
body='\n'.join(x for x in ancestor.splitlines() if not x.startswith('#'))+'\n'
def program(prefix): return header+'\n'.join(prefix)+'\n'+body
fixtures={'echo':program(['IO']*4), 'zero':program(['IO']*3+['IO','nop-C']),
          'graph':program(['IO']*3+['inc','nop-C']*130+['IO','nop-C']),
          'path':program(['IO']*3+['inc','nop-C','IO','nop-C']+['IO']*4),
          'one':program(['IO']*3+['inc','nop-C','IO','nop-C']),
          'choose0':program(['IO']*6+['IO','nop-C']),
          'choose1':program(['IO']*6+['inc','nop-C','IO','nop-C'])}
scenarios={
 'B1':('B1',['u begin InjectRange zero.org 0 16','u 1 MiniB1','u 1 Exit']),
 'B2':('B2',['u begin InjectRange echo.org 0 24','u begin InjectRange zero.org 24 32','u 0 MiniB2','u 0 Exit']),
 'B3':('B3',['u begin InjectRange graph.org 0 16','u begin InjectRange path.org 16 24','u begin InjectRange one.org 24 32','u 0 MiniB3','u 0 Exit']),
 'C0':('C',['u begin InjectRange echo.org 0 17','u begin Inject zero.org 17','u begin InjectRange choose0.org 32 48','u 0 MiniC','u 0 Exit']),
 'C1':('C',['u begin InjectRange echo.org 0 17','u begin Inject zero.org 17','u begin InjectRange choose1.org 32 48','u 0 MiniC','u 0 Exit']),
 'emptyB2':('B2',['u begin InjectRange default-heads.org 0 32','u 0 MiniB2','u 0 Exit'])}
results={}
for name,(mode,events) in scenarios.items():
 d=tests/name; shutil.copytree(runs/mode,d,dirs_exist_ok=True)
 (d/'events.cfg').write_text('\n'.join(events)+'\n')
 for f,s in fixtures.items(): (d/(f+'.org')).write_text(s)
 p=subprocess.run([str(binary),'-c','avida.cfg'],cwd=d,capture_output=True,text=True)
 (d/'stdout.log').write_text(p.stdout); (d/'stderr.log').write_text(p.stderr)
 log=(d/('mini-b1.log' if name=='B1' else 'mini.log')).read_text() if p.returncode==0 else ''
 brief=[x for x in log.splitlines() if x.startswith(('INVALID','EMPTY','UNREACHABLE','GRAPH','MOVE','Q ','WINS','PAIR'))]
 if name=='B1': brief=log.splitlines()
 results[name]={'exit':p.returncode,'records':brief}
(tests/'results.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
```


END OF REPORT
