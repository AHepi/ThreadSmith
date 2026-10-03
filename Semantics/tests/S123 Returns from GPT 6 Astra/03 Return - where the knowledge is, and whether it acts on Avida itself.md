# Where knowledge is carried in Avida and how it can change the simulated world

Report for the owner and the reviewing experimenter, 2 October 2026. Brief 03, assessed with the hard-to-vary method by one agent. Source inspection and experimental specification are complete; the proposed Avida experiments are unrun.

## For the owner

The programs carry learned ways of doing tasks. Avida’s rules make those ways work, but needing a rule does not show that the rule stores what was learned. The selector may also retain useful information from earlier events; the supplied results do not yet establish that it does.

Programs can affect Avida’s resource levels through mechanisms present in its source. That is an effect on Avida itself if you mean its changing state. It is not evidence that programs rewrite the simulator’s underlying rules. Requiring an effect with no causal route would make the test impossible by definition. The useful next test is to remove a learned capability while preserving copying, then check whether changes in the surrounding world disappear and return when that capability is restored.

## Material corrections before testing

**A designed route still carries a causal effect.** The brief reports that no effect on Avida itself has been tested because the effects went through channels supplied by its designers. That inference does not follow under the state reading. A resource store belongs to the simulated world; changing it is an effect on that world, regardless of who supplied the mechanism. This does not establish that the recorded runs demonstrated a capability-specific effect. Their raw logs, saved populations and intervention results were not attached. [Checked: brief, “The owner’s words” and “What has been found”; inference about the distinction.]

**The source contains the outward route.** At commit `47f13dadb547fcf10f620ace60247f38b30b8b16`, Avida tests outputs against reactions, computes consumption from available finite resources, obtains resource changes from produced minus consumed amounts, and applies those changes to the population’s resource stores. This establishes an implemented mechanism, conditional on the reaction and resource configuration. It does not establish its activation in a particular saved run. [Checked: source S1–S4 below.]

**Rules and current settings need a sharper separation.** The source includes events that change reaction values and configuration entries during execution. Consequently, “the C++ and the configuration cannot change” is too broad if configuration means current parameter values. Keep the simulator’s implemented transition procedure separate from the mutable values that it reads. An external event or a population-sensitive driver changing a value is not evidence that an Avida program rewrote the C++ procedure. The project’s actual instruction set and driver would need inspection before making a complete claim about which settings program activity can influence. [Checked: S5; inference.]

**Elimination finds dependence before it finds knowledge.** Removing the interpreter, all processor time or a necessary resource can stop a task without locating the information learned in that run. The relevant comparison removes or replaces a task-specific arrangement while preserving the general means of execution. Restoring that arrangement should restore the corresponding capability. Removing a whole selector therefore cannot, by itself, separate H1 from H2. [Analysis of the supplied elimination proposal.]

**The definition should not acquire an extra requirement silently.** Marletto’s paper characterizes knowledge through information acting as a constructor and causing its continued instantiation. Its account distinguishes a task recipe from the machinery and elementary processes on which the recipe relies. It does not require a change to underlying laws or an effect without an available physical interaction. The paper also makes error correction central to its account of accurate replication. The reported survival of many one-instruction variants is consequently insufficient on its own to establish that account. [Checked: Marletto 2015, §3.1, PDF p. 5; S6. Application to the brief is an inference.]

The three hypotheses are not mutually exclusive as written. H1 can locate acquired task information in programs while H2 correctly attributes production of that capability to the coupled system. H3 adds a condition for using the word knowledge; it supplies no distinct trajectory prediction unless further causal commitments are stated. The tests below retain the originals and identify the narrower claims they can distinguish.

## The frozen question and working hypothesis

The question is which retained arrangements account for performing, preserving or reacquiring a specified capability, and for changing non-program state, in the supplied Avida setting. The scope is the pinned source, the stated heads instruction set, and the resource or temporal-selector setups described in the attachments. The tested transformations, intervals and system boundaries must be fixed before outcomes are inspected. Outside-data learning, explanatory status and construction are outside this brief.

The working hypothesis is that acquired task information is carried in retained, capability-specific arrangements. These may lie in instruction sequences, population composition, or history-dependent non-program state. Reliable performance is realized by their coupling to enabling machinery. A non-program state is a candidate carrier of acquired information only when its particular arrangement, rather than simply its resource quantity or the availability of rewards, makes a reproducible difference to a stated retained capability. It need not be independently sufficient: a population and selector state may work only together.

This is a hypothesis about causal organization, not a replacement definition of knowledge. To apply the owner’s three properties, also require evidence that use of the candidate arrangement contributes to its copying, resistance to specified disturbances, and persistence. A useful memory trace could fail that additional requirement. Conversely, a self-maintaining feedback loop could retain information without meeting the semantics’ conditions for representation or explanation.

The hypothesis would lose its proposed program dependence if properly matched capability ablations left performance and outward effects unchanged, including group ablations that remove redundant implementations. Its claim of an outward capability-dependent effect would fail for a particular setup if validated removals changed no non-program state and restoration added no effect. Its selector-memory extension would fail on the tested contract if retaining, wiping, exchanging and disrupting history-dependent state made no capability-specific difference despite an effective positive control. Such a null result would not establish that selector state can never matter elsewhere.

The admitted changes are targeted instruction replacements, shams, exact restorations, independently prepared replacement implementations, selector-state resets and swaps, live versus blind feedback, and bounded disturbances. A file rename should have no effect. Removing a capability or scrambling task identities in a useful memory should have an effect of the stated kind. Host failures, unrestricted changes of instruction meanings, outside data and unbounded persistence are excluded. Changing any of these exclusions creates a new assessment.

| Required contrast | Origin | What addresses it |
|---|---|---|
| Capability-specific effects versus generic damage to execution | Given: elimination turned outward | Ablation, matched sham, restoration and execution controls |
| Information carried by programs versus an additional history-dependent contribution outside them | Given: transplants | Crossed population and selector-state interventions |
| Copying, resistance and remaining caused by the candidate versus supplied entirely by its surroundings | Given: the owner’s three properties | Disturbance and causal-link tests on the selector |
| Attribution to programs versus the whole simulated world | Fixed: report both boundaries | Two declarations made before interpretation |
| Learned arrangement versus a generic increase in fuel or payment | Added methodological job | Match current resources and pay; disrupt the historical arrangement |
| A simulated result versus an experimenter’s description of a possible result | Fixed: ground rules | Separate source inspection, deductions and unrun predictions |

## How the hard-to-vary terms apply

| Method term | Current document term and location | Mapping and limit |
|---|---|---|
| Parts | “programs’ circuits”; “selector’s rule or state”, brief “Your question” | Proposed carriers or enablers of the capability |
| Jobs | Four requested tests, brief “Tests to give” | Causal localization and attribution, not explanatory status |
| Change list | Instruction removal, blind replay, sham, transplantation and wiping | These become a fixed intervention contract; extra controls above are explicitly added |
| Question | “Where does the knowledge … sit”, brief “Your question” | Split storage, realization, provenance and effects rather than treating them as one location |
| Match under change | Faithful transport, semantics Part IV, lines 181–213 | An effect alone does not establish a transport’s component fidelity or history |
| Attribution boundary | Semantics Part X, line 427; Part XII, lines 473–475 | Boundary and continuity are declared indices, not outcomes inferred from success |

## E1 to E3 and the two meanings of Avida itself

E1 and E2 describe how a mechanism is specified. They do not measure how much knowledge it contains. E1 can describe a task-specific trigger connected to an E2 shared-resource process, so the categories can overlap within one causal route. A generic formula reading a fixed list of detectors also remains restricted to the distinctions those detectors expose.

| Effect category | Assessment | What an experiment could establish |
|---|---|---|
| E1, named effect | Retain as a description of an explicit capability-to-effect coupling | Removing that capability stops the named transition; restoration restores it |
| E2, generic channel | Retain, but identify the channel’s actual domain and any named triggers feeding it | Different implementations affect a shared state through a common mechanism; indirect effects propagate through it |
| E3, no implemented causal route whatsoever | Unavailable under a closed, correctly specified simulation | A purported occurrence challenges the completeness of the causal account, instrumentation or closure assumption |
| E3, no special-purpose channel naming this particular consequence | Coherent, but a different reading | A new consequence is produced by composing existing interactions; those interactions can be traced and interrupted |

The distinction can be stated without a new knowledge definition. Write the simulated world as `W = (P, S)`, with `P` the program population and its execution states, and `S` the remaining simulated state. Under a fixed implementation, the next state is produced by `F(P, S, inputs, random state)`. If no direct or indirect route from an altered program component enters a particular later variable, that variable cannot depend on the alteration under matched external inputs. This is a conditional obstruction argument about the specified model, not a measurement of Avida and not a claim that all its routes have been exhaustively audited.

An unforeseen consequence can still occur through such routes. For example, resource depletion caused by one capability could change another capability’s replication opportunities even if the designer did not name that population-level consequence. That is an illustrative mechanism, not a result from these runs. Evidence would require the resource and competitive dependencies to be measured and interrupted. Designer intention is not recoverable from the trajectory alone.

**Reading a, underlying rules.** No provided result shows that an Avida program rewrites the simulator’s implemented transition procedure. Changing a reward parameter through an event or driver follows that procedure. If “rules” instead means the currently operative reward schedule, record the parameter changes as state changes with policy consequences; do not silently equate that reading with C++ modification. A learned program can alter what happens under fixed rules without editing those rules.

**Reading b, changing state.** Programs can affect Avida itself through the resource path identified in source. Establishing that an acquired capability, specifically, causes a later resource or selector change still requires the outward intervention below. Measure both the explicit reward schedule and the resulting pattern of differential replication: competition can change the latter while every reward parameter stays fixed.

H3’s original wording also needs logical care. An E3 observation would meet its proposed necessary condition, not refute that condition. To challenge “no knowledge without E3,” one needs an independently accepted knowledge case lacking E3, or an argument against the necessity of E3. Absence of E3 cannot decide between H1 and H2. Under the literal no-route reading, H3 places the threshold outside the closed model rather than offering an executable learning test.

## Common experimental contract

The following specifications are proposed, unrun experiments. They use the saved runs held by the reviewing experimenter. Choose the source populations and target capability before inspecting intervention outcomes. Preserve the first outputs and every preparation failure. The costs are planning estimates from the brief’s reported 0.35 CPU-hours per 20,000 updates at 3,600 cells, not measurements here.

The minimum record contains the exact build and configuration, patch and driver versions, initial instruction sequences and multiplicities, cell placement, resource arrays, reward and requirement values, input buffers and cursors, controller traces, update phase and random-generator states. Execution state includes registers, stacks, heads and relevant per-program counters. Where an item is absent, name the resulting loss of comparability.

A population save must not be assumed to restore the whole world. The inspected save routine writes structured population information; its name does not guarantee preservation of resources, controller history, random state or processor internals. A same-state restore control must reproduce the measured continuation before it is used for causal comparisons. [Checked: S4; requirement inferred from the intervention.]

For the literal “at one update” intervention, use an in-memory intervention on matched runs reproduced to that update, or a checkpoint route whose continuation has passed that control. If only population reconstruction is available, reconstruct every arm identically and label the result a test after reconstruction. It cannot answer a claim about uninterrupted state. The cost of rerunning to the intervention point must then be included.

Random seeds alone do not ensure matched exogenous inputs after programs consume random numbers differently. Record generator state and input delivery. For a short diagnostic, use controlled input and scheduling tapes where compatible with the question. For live selection, let merit affect scheduling as intended and distinguish the later divergence from the initially targeted change.

A task is measured as correct execution in a separate common probe environment with the same input contract and instruction budget, as well as by actual outputs in the evolving world. Log all configured tasks, copying behavior, occupancy, outputs, resources, applied reward values and reproduction. Probe rewards are disabled so that a higher payment cannot masquerade as a newly acquired task capability. This does not test outside-data reach.

Freeze the probe inputs, instruction budget, observation times and admissible collateral changes before comparing arms. For the initial diagnostic, require the cut to remove every `q` success on that finite panel, while the original and restored programs retain their recorded successes. Require the sham to preserve those outcomes and copying; publish execution-cost differences. Failure to find a qualifying cut is a preparation failure, not a negative knowledge result. Counts and discrete states are compared exactly. Floating-point comparisons use a tolerance fixed from the unchanged continuation control before intervention results are inspected. Report effect sizes and trajectories without converting them into a knowledge score. Retention over 5,000 or 20,000 updates remains precisely that finite claim.

## Test 1 Elimination turned outward

**Setup.** Select a saved population with a capability `q` that is active under a finite, depletable resource configuration, or whose measured occurrence enters the temporal controller. Record which coupling is claimed. Map every currently present instruction sequence that performs `q`, including less common sequences. A cut covering only common sequences cannot support a claim about eliminating `q` from the whole population.

Prepare capability-disabling instruction replacements for each relevant sequence. Retain copying and check other tasks and execution costs. Test combinations where there are redundant implementations. A nominal do-nothing instruction is not assumed neutral: the supplied reader’s guide explicitly warns that replacement is not the semantics’ deletion operation. If no sufficiently specific cut exists, report that limitation. An output-suppression experiment can separately locate the output-to-world route, but it does not locate the learned instructions.

Start each arm from the same declared state and run 5,000 updates. Inspect the immediate effects before population turnover and later effects at every controller update. Include a short diagnostic with program variation disabled, followed by the stated live-selection continuation; report that change of regime. If the capability reappears through new variation, record its timing and mechanism rather than continually ablating it without disclosure.

Existing output buffers, earned merit and per-program task counters can preserve consequences of earlier executions after the instructions are cut. Keep these identical at the intervention point, log them, and distinguish their carry-over from newly executed `q` events. If a reset is needed to isolate new execution, apply it to every arm and record the changed contract. A delayed disappearance of the effect is not automatically failed ablation or retained selector knowledge.

| Arm | Program intervention | World response |
|---|---|---|
| L0 | Original population, handled identically | Live resources and selector |
| Lq | Validated cuts removing `q` | Live resources and selector |
| Ls | Same number of removable instruction replacements, matched as far as feasible | Live resources and selector |
| Lr | Exact restoration of the removed arrangement, using the same intervention handling | Live resources and selector |
| R0 | Original population | Resource or pay trajectory from L0 replayed blind |
| Rq | Same cuts as Lq | The identical L0 trajectory replayed blind |

Record the L0 tape before the replay arms. The replay must not use current capability measurements to choose its values. For the temporal driver, replay the rewards and requirements at the same decision boundaries. Internal controller calculations may continue in a shadow copy, but only the tape governs applied pay.

For resources, “replay” must specify whether resource levels are clamped or merely inflow is replayed. Identical inflow does not hold levels fixed after different consumption. To block the resource-mediated route, present the same available levels at the relevant consumption opportunities and log attempted consumption separately. Applying a saved level once per 1,000 updates leaves intervening feedback live. Exact resource clamping therefore needs instrumentation unless an equivalent hook is already available.

The replayed variable is fixed by intervention. Equality of that variable is a manipulation check, not an independent result. Compare downstream replication and capability retention, as well as any state not clamped. The live difference between Lq and L0, corrected by the corresponding replay comparison Rq versus R0, can diagnose a feedback contribution under the specified intervention. It is not a universal additive decomposition: state interactions can change the size and sign of that contrast.

**Expected outcomes and adverse findings.** H1 permits the removal of program circuits to change resources and subsequent pay. H2 also permits it. Thus, an outward effect alone does not split them. If the claimed `q` route is a finite, depletable resource reaction with no compensating production, losing successful executions should initially reduce its consumption; longer-term resource levels have no unconditional direction. In a temporal selector, the expected timing and direction must come from the actual driver rule before running; its patch was not supplied here.

The claimed circuit dependence is challenged if validated complete cuts leave `q` execution and the specific outward effect intact. A resource effect accompanied by widespread copying failure diagnoses generic damage unless a further control separates it. Exact restoration should restore the immediate task-dependent contribution within the declared tolerance. H2 gains no evidence for stored selector knowledge merely because resource feedback exists. H3 predicts no different numerical trajectory; E1 or E2 effects leave its naming requirement unresolved.

**Classification.** A named task-to-resource trigger is E1 at that link. Shared depletion and its consequences are E2 where no particular downstream capability is named. A named task-list expansion is E1. A generic response over a configured detector list has E2-like routing while retaining that list’s scope. None is literal E3. An unexpected downstream consequence may meet the weaker E3 reading only after its route and the absence of a special-purpose rule have been documented.

**Cost and code.** Six 5,000-update arms cost approximately 0.525 CPU-hours per saved state; four independently selected saved states cost 2.10 CPU-hours. Add ablation discovery, common probes, tape storage and any rerun to the intervention point. Exact in-place changes and resource clamping likely require new diagnostic code. Temporal reward replay and state serialization require driver work. No patch is claimed complete or tested by this report.

## Test 2 Transplants and selector memory

**Setup.** Separate the non-program state into current operating conditions, such as resources and present pay, and retained history, such as controller traces, latches and sequence state. This is an experimental decomposition of the whole Avida execution environment; it does not redefine “execution environment” to exclude programs.

Use two donor histories A and B from the same implementation and resource contract. Prepare `P_A` and `P_B`, their evolved populations, and `P_0`, an ancestor population with matched occupancy and placement handling. Prepare history states `M_A` and `M_B` and the specified fresh state `M_0`. A wiped selector retains its rule and valid initial state; it is not a broken selector or one with pay disabled.

Begin with the requested ecological transplant, preserving the saved selector state or wiping it according to the declared condition. Any difference here is a total state effect, which can include resources, current pay and timing. Then perform the narrower memory transplant: equalize current resources, pay, inputs, clock phase and applicable operating conditions while varying only retained history. Use valid controller states. If history cannot be altered independently of current pay without violating an invariant, hold only the first applied pay vector equal and record subsequent divergence; call this a composite intervention rather than an isolated memory wipe.

| Population | Wiped or fresh history `M_0` | History `M_A` | History `M_B` |
|---|---|---|---|
| Ancestor `P_0` | Fresh baseline | Requested ancestor-under-experienced-selector arm | Ancestor under the other donor |
| Evolved `P_A` | Requested evolved-under-fresh-selector arm | Same-donor continuation | Cross-donor transplant |
| Evolved `P_B` | Second evolved-under-fresh-selector arm | Reciprocal cross-donor transplant | Second same-donor continuation |

The donor exchange distinguishes a task-specific historical arrangement from a generic warm-up advantage. Where the state structure permits it, replace a donor state with an admissible task-identity permutation preserving trace magnitudes and total resources. Predeclare the permutation. If it is not an admissible state, do not interpret damage from it as lost knowledge. A corresponding consistent relabeling of all task identities and their couplings should preserve behavior; mismatching only the alleged binding should not.

**Readouts and controls.** Before new variation, probe what each population can already execute with equal instruction budgets. During 20,000 updates, record retention, loss and first reappearance of each prespecified capability, the pay trajectory, resource trajectory and program ancestry. Probe the resulting populations in the same common environment. An ancestor receiving high pay has not thereby acquired the paid capability. A change in population composition can carry acquired information even if no new instruction sequence appears.

Check the controller independently with the same present input after two different past histories. A nonzero difference in its next action establishes functioning memory, not useful learning. The supplied report says such a difference occurred previously, but those traces were not attached. If kept and wiped states produce the same next action at the chosen point, a null population effect there does not test an active memory contribution.

| Claim being tested | Expected pattern if that specific claim holds | What counts against it |
|---|---|---|
| H1, acquired task information carried by programs, sharpened to exclude an additional retained historical contribution | Under equal immediate conditions, task execution follows `P_A` or `P_B`; selector history adds no task-specific retained advantage once ordinary enabling effects are controlled | A valid history swap transfers or removes a capability-specific retention or reacquisition effect with the same population, and matching restoration restores it |
| H2, broad coupled realization | Programs require an operative interpreter and selection setting; both matter causally | Not separated from H1 by that fact; breaking the general machinery is not a discriminating result |
| H2, sharpened to acquired information additionally carried by non-program history | Some same-population history contrast changes the specified capability; it may depend on a matching population | No effect on the tested contract after confirming active memory, valid states, sufficient observation and successful positive controls |
| H3, E3 required for knowledge | No unique behavioral prediction; it can accept either transplant pattern and withhold the word knowledge | A contrary result needs an independent knowledge criterion; E1 or E2 transplant effects alone do not contradict the proposed definition |

The sharpened H1 and H2 are new testable claims, not quotations of the original hypotheses. A memory effect alone establishes an additional causal carrier of history. Its status under the owner’s three properties still requires Test 3. A helpful history state may carry a parameter selected by the designer’s rule rather than a newly constructed explanatory binding.

H2 may require a particular population–history pairing. Therefore, failure of a saved history to teach the ancestor does not refute distributed storage. Conversely, a change caused solely by supplying more resources is an enabling-state effect and does not establish that the state carries the learned task arrangement. H1’s separate assertion that the knowledge concerns only Avida’s own rules is not tested by this brief’s internal transplants; successful performance on unencountered cases would not alone establish a different subject matter.

**Cost and code.** A nine-arm panel at 20,000 updates costs approximately 3.15 CPU-hours; four independently prepared donor panels cost 12.60 CPU-hours. This is the cost of one declared transplant regime. Running both ecological and memory-isolated panels doubles that continuation budget to 25.20 CPU-hours. Existing donor runs need not be repeated solely for this test. New donor preparation, probes and checkpoint work are additional. A driver memory probe should take much less than an Avida continuation; allow 0.02 CPU-hours provisionally and measure it. Driver export/import/reset and audit logging are required. Exact world-state restoration may require C++ instrumentation.

## Test 3 The three properties of the selector

“Selector” here means the whole Avida execution environment. The tested subcomponents are its rule implementation and its non-program state, separately. This prevents program replication from being counted automatically as replication of the selector’s rule or memory. The following is a source-constrained thought test, not an executed experiment.

| Property | Operational criterion | Rule implementation | Non-program state and control |
|---|---|---|---|
| Causes itself to be copied | Its particular information actively contributes to producing another instance of that information; interrupting the contribution reduces the copying | Copying the executable or starting a second run externally does not demonstrate this property within the simulated world | Saving a checkpoint on a fixed experimenter schedule is passive copying. A claimed state-driven replication mechanism needs a traced link and a matched intervention on it |
| Causes itself to resist change | After a declared disturbance, its operation prevents loss or restores the relevant functional arrangement, compared with a matched state whose maintenance route is interrupted | Inaccessibility of C++ to program writes is protection supplied by the implementation boundary. It does not demonstrate active repair by that rule | Perturb a trace, resource profile or latch and compare intact feedback with interrupted feedback and a blind restoring schedule. Recovery of a generic equilibrium is not enough to establish recovery of task-specific information |
| Causes itself to remain | Use of the arrangement contributes to maintaining or renewing the same declared information or capability across the observation interval | Continuing to execute an externally supported, unchanged rule establishes persistence; the self-maintaining causal claim requires another intervention | Compare retained capability under intact feedback, cut feedback and restoration. Mere slow decay, a fixed latch or repeated external reinitialization is not evidence of task-specific self-maintenance |

**Expected outcomes.** H1 is compatible with selector rules being indispensable but not self-copying or actively self-repairing. It also permits generic persistent world state. H2’s broad realization claim requires no self-replicating selector. Its stronger acquired-memory claim predicts only a retained historical contribution; whether that contribution meets all three properties is an additional hypothesis. H3 again has no independent numerical prediction and would reject E1/E2-only cases by its proposed naming condition.

Evidence against a particular copying, resistance or persistence attribution is continuation of the claimed property when its alleged causal route is cut, or failure to restore the property when the arrangement is restored and the enabling conditions are intact. Distinguish resistance to harmless changes from tolerance of arbitrary destruction. The prior instruction-variation figures concern functional robustness, not necessarily correction of altered instructions. [Checked: supplied brief’s S111 summary; interpretation, with raw results unavailable.]

**Control and cost.** A disconnected feedback loop is the negative control; a deliberately initialized, recoverable state and a known active controller are manipulation controls. For the supplied stock setup, thought analysis costs 0 Avida CPU-hours and no new code. If live state-maintenance testing is later chosen, four 5,000-update arms—intact, disturbed, disturbed with maintenance cut, and restored—cost approximately 0.35 CPU-hours per starting state, or 1.40 for four states. Disturbance and feedback-control hooks are needed. This optional experiment cannot establish indefinite retention.

## Test 4 Boundary and continuity

These declarations precede attribution. They do not alter the physical intervention or retrospectively convert outside contributions into internal discoveries. [Checked: semantics Part X, “Ownership”, and Part XII, “System boundary and continuity”.]

| Declared system | Boundary and continuity | Interpretation of Tests 1 and 2 |
|---|---|---|
| Programs alone | Include instruction sequences, program execution states and the population’s stated ancestry and organization. Interpreter rules, shared resources and controller are enabling surroundings. Population continuity follows declared descendant branches; a swap is recorded as an intervention | Outward ablation effects cross this boundary. A selector transplant changes surroundings. A capability that follows instruction sequences is carried inside this boundary; a selector contribution remains external |
| Programs with the simulated world | Include programs, interpreter processes, cells, resources, input-generation and selection processes. Continuity is the declared run lineage, with every reset, transplant and restored branch recorded | Resource and selector feedback are internal processes. Coupled performance can belong to the whole world even when acquired task information is localized in one part. This attribution does not establish a separately self-maintaining selector |

The temporal driver needs a further explicit declaration. Report the world with the driver excluded, where its decisions are external interventions, and the world with the driver included, where its running process is owned by the larger system. Including the driver does not make its designer-supplied content newly learned. The semantics separates ownership of a process from contribution of its content. This report does not choose one driver boundary for the owner.

Continuity of a task arrangement is also distinct from continuity of an exact string. If a different program maintains the same admitted task behavior, that can preserve capability while losing the original sequence. A selector that retains useful history through different numerical states can likewise preserve a function without preserving its exact bytes. Declare which of these is being measured before applying “remain.”

**Expected outcomes under H1, H2 and H3.** Every measured trajectory remains the same under both reporting boundaries. H1’s proposed location of acquired information remains a claim about the programs. H2’s system-level ownership attribution changes with the declared boundary, while its additional-memory claim still needs the same transplant evidence. H3’s E3 requirement is not met merely by redrawing a boundary. A conclusion that appears or disappears only because the boundary was chosen after seeing the result violates this test’s declared contract.

**Cost and code.** This is a paired interpretation of Tests 1 and 2: 0 additional Avida CPU-hours and no new simulation code. The recording scheme must identify driver actions, outside interventions and checkpoint branches. It cannot create empirical evidence absent from the underlying tests.

## Part marks and whole account checks

| Part assessed | Mark | What holds it or leaves it open |
|---|---|---|
| Required coupling between execution machinery and instruction sequences | Borrowed | Source establishes machinery; specific capability attribution relies on the unrerun project interventions |
| Acquired task arrangement localized in particular program instructions | Held if | The supplied ablations are task-specific and their restoration and execution controls succeed; Tests 1 and 2 examine this |
| Additional acquired information in non-program selector history | Unknown | Need valid history transplants separating particular historical arrangement from generic resources and current pay |
| Program outputs can change shared resources | Held | The inspected source supplies the conditional route; activation and magnitude in saved runs remain unmeasured here |
| Necessity of the selector alone establishes knowledge stored in it | Loose | Generic enabling machinery explains the same failure after removal; replace this test with selective removal and transfer of history |
| E3 as absence of every implemented causal route | Held if | The closed transition model is complete; under that condition its absence follows from the missing dependency, not from an empirical learning limit |
| E3 as absence of a purpose-written effect rule | Loose | Composed ordinary channels can produce the same effect; the common requirement is a traced causal dependency, not designer anticipation |
| Both system boundaries, the pinned setting and the stated exclusions | Fixed | Declared for this assessment rather than established by experiment |
| Three properties attributed to selector state | Unknown | Persistence and memory are reported; self-caused copying, resistance and maintenance are not established by the supplied evidence |
| Declaring a larger boundary establishes representation or construction | Idle | Ownership changes without supplying the fidelity or history conditions; this inference can be removed without losing the causal account |

The outcome-flip check exposes an underconstrained version of H2. If every effect of preserving state is called distributed knowledge, and every null effect is explained away as knowledge already absorbed into the programs, either result can be accommodated. The sharpened memory claim instead commits to specified starting states, contrasts, capabilities and horizons. A null result remains a null result there. Claims about another horizon must be new claims.

The direction check follows actual temporal order: program arrangement changes task execution; task execution changes resource use or a measured controller input; that state changes a later selection condition; later selection changes the population. Merely changing a printed task count should not change the world unless the driver reads that count. In that case the measurement is itself part of the operative feedback route and must be included in the boundary record.

The competing account for a selector advantage is ordinary ecological carry-over: a donor supplies more favorable resources, current pay or timing, without storing a capability-specific learned arrangement. The common-present transplant and valid history permutation are intended to distinguish it. If both accounts give the same internal and external responses over all admitted changes, the experiment does not separate them; do not settle the difference by vocabulary.

Two requirements pull against each other. Removing every implementation of a capability can damage copying or other capabilities, undermining specificity. Conversely, cutting too little preserves redundant routes. Record the protected behaviors lost by each cut rather than selecting a cut only because it produces an attractive resource trace. Similarly, matching all downstream rewards erases the very selector effect one wants to measure: blind replay is a control intervention, not the live test itself.

The catch-all “both together” is permitted only with a gauge: a named capability contrast, a specified intervention on historical state, the resulting state and capability trajectories, and the restoration comparison. “Emergence” is not a substitute for the path. An unexplained residual triggers inspection for omitted state, side effects, nondeterminism or instrumentation error; it is not automatically E3.

The candidate hypothesis is built here from the supplied cases and criticisms. The reported program arrangements arose through the project’s evolutionary search, as described by the attachments. Calling them “selected” in ordinary experimental language does not settle selected provenance in the semantics. Under Reading A, a faithful correspondence with the required history can be selected. Under Reading B, the prior represented target changes that provenance assessment to declared in the project’s stated reading. Both retain the same causal results. Neither outward influence nor a favorable transplant supplies a construction trace.

## What was run and what remains open

**Nothing run in Avida.** Avida was not built or executed, and no output from a proposed experiment exists to paste. The supplied workspace contained the five prose attachments, not the saved populations, source patches or serialized selector states needed to reproduce the described cases. Stock source files were retrieved and read at the pinned commit. I do not claim that Avida cannot be built in this environment; I did not attempt a build, because a stock build would not supply the missing experimental states.

The numerical run claims in the attachments remain reports by the previous experimenter. This report does not convert them into newly observed results. No simulated self-replication or host-level self-replicating code was executed. The proposed protocols keep all program replication inside Avida.

Source inspection establishes an available route and corrects the rule/state distinction. It does not show that selector memory contains knowledge, that any stored capability meets constructor-theoretic possibility at arbitrarily demanding tolerances, or that Avida represents, explains or constructs anything. Finite runs address specified finite horizons and enabling conditions. The hard-to-vary assessment exposes dependencies and competing accounts; it does not certify the hypothesis.

The next action is the live outward-ablation comparison with sham and restoration on one existing resource-coupled population. First confirm a specific cut that preserves copying and the continuation control. That resolves whether a learned capability changes a non-program part of the world without requiring a decision about E3 or a new definition of knowledge. The larger transplant program remains a costed option, not an already authorized selection of the owner’s next costly run.

## Sources and evidence status

“Checked” below means opened and inspected in this execution. When an attachment reports another source, the scope of that check is the attachment, not the unprovided underlying experiment or book. No verdict depends on a source recalled only from memory.

| Source | Status and precise use |
|---|---|
| Supplied Brief 03, “Where the knowledge is, and whether it acts on Avida itself” | Checked in full. Supplies question, hypotheses, tests, reported run claims, wording constraints and CPU-cost estimate |
| Supplied “the semantics, standing alone, after round 4” | Checked in full. Parts III–IV constrain question and provenance; Part VI covers redundant routes; Part X separates ownership and content contribution; Part XII supplies boundary, continuity and retention conditions. Formal-core D identifiers are pointers supplied by the guide; that separate core was not attached |
| Supplied “a reader’s guide to the semantics” | Checked in full. Its Avida interpretations remain interpretations; particularly its ablation warning and Reading A/Reading B distinction |
| Supplied “the shared context” | Checked in full. Source of descriptions of S111–S122 and the temporal driver. Underlying run files and patches were not inspected |
| Supplied “Pinker context” | Checked in full as background. Its inherited `[checked: P2004, pp. 949–950]` mark concerns constraints on learning from finite data; its `[unverified: details from memory]` mark on the 1984 book remains unverified. Those originals were not reopened here. The note’s proposed Avida requirements are explicitly Claude’s reading, not established Pinker requirements. No outside-data or within-lifetime-learning verdict is attempted in this brief |
| S1: [cEnvironment.cc at the pinned commit](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cEnvironment.cc) | Checked. Lines 1252–1294 contain input setup alternatives; 1314–1397 contain task and reaction dispatch; 1635–1735 contain finite-resource consumption and bonus computation; 1877–1927 contain reward-value setters. Blob `6ecb2464270b0337d40bc6a4180dddec7efd8d47` |
| S2: [cPhenotype.cc at the pinned commit](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cPhenotype.cc) | Checked. Lines 1493–1523 call the environment’s output test; 1675–1678 form resource changes from production and consumption |
| S3: [cOrganism.cc at the pinned commit](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cOrganism.cc) | Checked. Lines 485–519 apply output results to resources and, under configuration conditions, merit. Blob `9431768917f663355458f189dfe7d3f3b5ad3ff3` |
| S4: [cPopulation.cc at the pinned commit](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cPopulation.cc) | Checked. Population save inspected from line 6362; resource mutation at 7295–7312. This is not a claim that every checkpoint facility was audited. Blob `4070d3840e16e52c184db9ba56789ef528a1c921` |
| S5: [EnvironmentActions.cc at the pinned commit](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/actions/EnvironmentActions.cc) | Checked. Lines 651–693 change reaction values; 1675–1700 provide the configuration-changing event. Blob `b57b66f1861c1eb4c55b46617b6e3e72dc6d525f` |
| S6: [Marletto, Constructor theory of life, 2015](https://www.constructortheory.org/wp-content/uploads/2016/03/ct-life.pdf), DOI 10.1098/rsif.2014.1226 | Checked, especially §3.1, PDF p. 5. Used for the distinction between recipes, enabling machinery and knowledge’s continued instantiation, and the role of error correction. Does not establish that this Avida setup satisfies no-design laws |
| Marletto and Deutsch book passages reproduced in the brief | Checked as supplied passages only. The original books and page references were not independently opened. They remain supplied premises; no new book quotation or claim of book inspection is made |

END OF REPORT.
