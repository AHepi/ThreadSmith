*Text extracted by Claude from the .docx beside it (paragraphs and tables, in order), 1 October 2026; the .docx is the reply as sent.*

Does temporal state close the gaps in the Avida selector

Research report  |  2 October 2026

# Summary for the owner

Temporal state can supply a forecast, an alarm when the forecast fails, and a persistent signal to continue investigating. It does not, by itself, supply what the investigation concerns, which program made which claim, or why a particular instruction is responsible.

For example, two program populations can currently perform a task equally often, although one has recently gained the capability and the other has lost it. Two traces can distinguish those histories and allocate processor time differently. A selector reading only the current task share cannot make that distinction.

This closes some control and memory gaps. It leaves the content of problems, criticisms and comparisons to be represented somewhere. That representation could itself be a network state; it need not be prose.

Replacing a written timing rule with a decaying trace does not remove the rule specifying what receives processor time. The proposed circuits retain named task checks and a human-specified allocation rule.

The experiment below separates history sensitivity, its consequences for Avida task performance, and any contribution specific to neuron-like implementation. I ran small arithmetic checks, not Avida. The supplied pilot outcomes remain unknown.

# Table

“Partial” means the small circuit supplies the stated mechanism, not the whole gap. Grades describe solution criteria, not computational complexity. Throughout this table, 1/2 means grade 1 task checks and grade 2 allocation or testing rules; adding temporal state leaves both unchanged. Missing mechanisms previously had no separate grade.

| Gap and supply | Circuit | Representation still needed | Grade before → after | Memoryless comparison | Counts against |

| Prediction: partial | Leaky forecast | Predicted quantity, horizon and conditions | 1/2 → 1/2 | Same present; different histories | Forecast adds no usable distinction |

| Surprise: partial | Forecast comparator and alarm trace | Which expectation failed | 1/2 → 1/2 | Compare with current rarity | Alarm follows rarity or reload only |

| Holding a problem: partial | Set/reset latch | Problem identity and discharge condition | 1/2 → 1/2 | Remove the trigger | Persistence loses its referent |

| Targeted criticism: partial | Eligibility traces plus intervention | Program, instruction, case and dependency | 1/2 → 1/2 | Current activity credit | Blame fails matched ablation |

| Lasting without solving: conditional | Success latch and copy gate | Success check, expiry and gate connection | 1/2 → 1/2 | Immediate-success gate | Copies occur without a valid certificate |

| Selected-history memory: partial | Selection traces | Identities, outcomes and exact records | 1/2 → 1/2 | Current-share selector | Equal traces conceal required history |

| Candidate model: partial | Candidate-indexed forecast bank | Stable identities and test conditions | 1/2 → 1/2 | Current observed outputs | Predictions fail held-out conditions |

| Choosing the next test: partial | Disagreement and adaptation | Available tests and rival predictions | 1/2 → 1/2 | Current-disagreement rule | Only cycles through tests |

| Standing problem: partial | Persistent indexed latch | Question, criterion version, unresolved cases | 1/2 → 1/2 | Current-deficit rule | Retargets or closes without resolution |

| Rivals for one problem: partial | Separate traces and comparison | Two claims about the same case | 1/2 → 1/2 | Current-head comparison | Rivals share only activity, not a question |

| Findings change selection: partial | Eligibility-dependent weight update | Intervention record and consequence | 1/2 → 1/2 | Frozen current-input rule | Change follows drift or irrelevant signals |

# One section per gap

## Shared interpretation and interface

The frozen question is whether adding temporal state closes the specified gaps in the selector. The eleven gaps are given; grade definitions and terminology are fixed. The circuits and experiments below are my proposed constructions, not observed Avida results.

Here “representation” means a distinguishable state that carries relevant content and can affect later action. A latch is already a representation. A prose question, addressable record and distributed neural state are alternative encodings; tiny unlabelled traces cannot be credited with information they discard.

Let k denote a boundary between 1,000-update pieces. Read a bounded audit of the instruction sequences: program identifier g, tested inputs and order c, outputs, task indicators, replication capability and audit limit. Weight duplicate sequences by their number of copies to obtain task share p_j. Separately record the selector's actual allocation a_j. The audit must not replace the running program population. Persist selector state outside reloads. The brief reports that ordinary reloads lose processor state and distort task records [checked A1, supplied account only]; audit-derived shares avoid treating those records as capability loss.

In the update descriptions, all right-hand values are old values unless stated otherwise. Coefficients, thresholds, indexing and reset rules are specified design choices. A memoryless control receives the same current audit but no previous observations or actions. The Avida execution environment itself remains stateful.

## Prediction

A trace can forecast a defined observable. For each task, store m_j. Before seeing the next audit, issue forecast m_j; after observing p_j, update m_j to (1−alpha)m_j + alpha p_j, with alpha between zero and one. This is a persistence-based numerical model of task share, not a forecast invented by the Avida programs.

The forecast needs a task identity, horizon, conditions and a record showing it preceded the observation. A scalar does not predict an unrepresented capability. Grade 1 checks remain grade 1; the forecast-based allocation rule remains grade 2.

In Avida, replay two audit histories ending at the same p_j, then reveal their next observations. Compare squared forecast error with a preregistered current-share forecast. Shuffle earlier observations while preserving their counts. No reduction in error on held-out continuations, or equivalent forecasts after history erasure, counts against this mechanism's claimed forecasting contribution. The numerical errors would not decide what the owner calls knowledge.

## Surprise

Store the previous forecast and an alarm trace z_j. Compute discrepancy d_j as the absolute difference between p_j and the forecast before updating that forecast. Update z_j to lambda z_j + max(0, d_j−epsilon). Trigger investigation when z_j exceeds theta. This produces an operational mismatch alarm.

It still needs the expectation's referent, issue time and conditions. A discrepancy is not yet a criticism of an explanation. The task checks stay grade 1 and the discrepancy criterion grade 2.

Use identical current bounded audits after histories predicting different shares. Compare with a memoryless rarity alarm and include a correctly predicted low-share case that should remain quiet. Inject a changed forecast without changing the program population. Alarms tracking current rarity regardless of expectations, or appearing only in native post-reload counters, count against the proposed interpretation. Threshold-crossing noise must be reported rather than called discovery.

## Holding a problem

A set/reset latch supplies persistence: set L to one on trigger D; set it to zero on resolution R, with resolution taking precedence; otherwise retain L. While L is one, reserve a fixed investigation budget. Read discrepancies and resolution-test results between pieces.

This holds an obligation to act. It does not identify what remains unresolved. D and R must refer to the same problem; otherwise unrelated success can silence the latch. A bank of indexed latches can retain several obligations, at an explicit memory cost. Named task checks remain grade 1 and latch management grade 2.

Trigger a problem, then supply neutral audits for several pieces. Compare with memoryless L = D. Follow with resolution of a different problem, then the original one. Premature clearing, endless activity after matching resolution, or attention without an identifiable problem counts against closure of the gap. This tests persistence, not problem creation.

## Criticism with a target

An eligibility trace e_r can remember activity in instruction region r: e_r becomes lambda e_r + v_r, where v_r is recorded execution of that region during a bounded test. Coincidence with subsequent discrepancy d assigns provisional suspicion proportional to e_r d. Read execution traces and the test outcome, not task totals alone.

That association supplies a place to investigate, not a reason the region caused failure. Store the instruction-sequence identity, region coordinates, case, prediction and dependency. Compare the intact program with controlled instruction ablations; coordinate mappings must be refreshed after sequence changes. Grade 1 checks and grade 2 targeting remain.

Against a memoryless current-activity control, test delayed failures and harmless recently active regions. A recent region whose removal preserves the disputed behavior defeats that particular attribution. Also test joint ablations: redundant regions can each survive removal alone. A failure to replicate does not isolate the arithmetic dependency.

## Lasting without solving

A latch can remember success during a replication cycle. Set C on a qualifying computation, permit a copy only when C is set, then clear C after the permitted copy. Give new or modified instruction sequences no inherited certificate. The selector reads success and copy events.

However, a driver observing only between pieces cannot enforce this rule at each copy. It needs a connection to Avida's copy authorization path. Filtering snapshots later is a different rule. The success predicate, certificate scope and expiry remain represented. Requiring a named task stays grade 1; “any member of this class” is grade 2 before and after temporal encoding.

Compare delayed-success certificates with a memoryless gate accepting only success present at the copy event. Include zero-task replicators, stale certificates and a success long before copying. Any uncertified copy counts against the gate. Even a functioning gate supplies a replication floor, not a demand for new capabilities. Persistence without copying is a separate policy choice.

## Memory of what was selected

For each selected item j, maintain h_j = lambda h_j + a_j, where a_j records actual allocated processor time, not observed prevalence. A latch can additionally retain “ever selected.” Read action receipts and subsequent bounded audits.

The trace records a compressed selection history. It does not retain exact dates, allocations, instruction-sequence identities or consequences. Those need addressable records or a state encoding with the required capacity. Different action sequences can have the same h_j. Grades remain 1 and 2.

Construct histories with the same current program population and different earlier allocations. Compare future choices with a current-share control. Then construct colliding trace histories whose exact order matters to the proposed question. If the selector cannot distinguish them, that counts against a claim of complete selection memory, while leaving its narrower recency memory intact. Erasing the trace tests whether it participates in allocation at all.

## A model of the candidates

A small model can use an indexed bank m_gc, predicting whether program g will meet case c. After its bounded test result y_gc, update m_gc to (1−alpha)m_gc + alpha y_gc. A second trace can retain timing or execution cost. Reads require candidate-level results; aggregate task shares cannot reconstruct them.

This predicts repeated cases. It does not infer how an unfamiliar instruction sequence works or how a candidate will respond to a novel intervention. A proposed feature model adds explicit features and dependencies. Instruction-sequence hashes prevent accidental identity reuse. Checks stay grade 1; model-guided testing stays grade 2.

Compare with current observed performance while withholding specified input orders or ablations. Change candidate identities without changing their population shares. Failure on those interventions counts against the claimed scope of the model. Looking up a repeated deterministic result should not be reported as explanatory understanding.

## Choosing the next test

For each available case c, compute disagreement D_c from candidate predictions. Maintain use trace h_c = lambda h_c + selected_c. Choose the case maximizing D_c/(1+h_c), with a fixed tie rule. Read candidate predictions, recent results and test receipts. Adaptation discourages repeatedly choosing the same case.

A release detector can schedule a previously blocked test: store previous blockage I; fire when I changes from one to zero. That supplies rebound-like scheduling, not a new question. The case generator and admissibility conditions remain explicit. Existing named checks stay grade 1; disagreement and scheduling are grade 2.

Compare with memoryless maximum current disagreement. Include a repeated uninformative test and a newly available discriminating case. Measure whether the chosen test actually separates the recorded rival predictions. Cycling without separation, or preferring irrelevant novelty, counts against purposeful test choice. The experiment does not establish unrestricted question generation.

## A standing problem

This overlaps holding a problem, but adds content identity. Store problem key q, criterion version v, unresolved-case set U and latch L. Set L when U is nonempty. Remove a case only after its matching resolution audit; keep L set while cases remain. Read candidate results keyed to q and v.

Temporal units can implement this indexed state. The distinction from an unlabelled latch is what survives: the same unresolved question, with its history. Neither the question nor its criterion arises merely because L persists. Task checks remain grade 1 and problem-management rules grade 2.

Interrupt investigation with unrelated failures and successes. Compare with a memoryless selector reacting to the current deficit. Returning to a different question, accepting an obsolete criterion version, or clearing the obligation without its resolution record counts against a standing problem. Holding and standing must not be counted as two independent acquisitions when one record supplies both.

## Rivals for one problem

Maintain separate registers for candidates A and B under problem q. For case c, store their predicted outputs and set disagreement latch L_qc when they differ. Keep both candidates addressable until the chosen test reports; update their discrepancy traces separately.

Coactivity, inhibition and persistence alone do not make candidates rivals. They must concern the same case and make incompatible commitments. A predicted output is a limited commitment, not automatically an explanation. Candidate identities, problem identity and comparison conditions are indispensable representations. Grades remain 1 and 2.

Use two candidates agreeing on familiar cases but differing on an unseen input order. Compare with a memoryless selector retaining only current performance. Loss of a rival before the separating test, comparison under different questions, or a conclusion unsupported by the observed output counts against this implementation. Identical observable predictions leave the comparison unresolved.

## Findings that change selection

Let e_j = lambda e_j + a_j record recent allocation. Change an allocation weight w_j by eta e_j delta, clipping it to stated bounds. Here delta is a signed consequence measured after a specified intervention, not simply any later rise in task share. Read allocation receipts, matched outcomes and intervention identifiers.

The circuit can make findings causally affect later choices. It still needs a definition of consequence and evidence linking it to the intervention. Plastic weights are stored representations. A human-specified consequence rule remains grade 2, with grade 1 task checks intact.

Give two replicas identical current audits after different intervention findings. Compare with frozen weights, then swap the findings while preserving their magnitudes. Choices should follow the relevant recorded finding. Changes following unrelated signals, disappearing outside reload artifacts, or recurring under blind replay with no corresponding performance difference count against the claimed feedback contribution. Updating a rule does not by itself create a new standard of solution.

# The report's claim and what it means for the owner's idea

The attached report distinguishes memoryless computation from state updates and qualifies its argument using finite precision [checked A2, sections on timing and logic]. That qualification matters.

Sequential digital circuits retain state in registers and compute subsequent state and outputs [checked S1, sections 8.1–8.3]. My inference is constructive: encode all states of a finite-precision selector, its clock and any pseudorandom generator in bits; implement its specified transition function digitally. With b stored bits there are at most 2 raised to b internal states. An unbounded external archive removes that particular bound, but remains digital storage. Avida software already executes by such digital transitions.

Korsky and Berwick derive finite-automaton characterizations for specified finite-precision recurrent architectures [checked S2, Theorems 1.1 and 2.1]. Their result is architecture-specific; it is not a statement about every ideal continuous physical system. Unlimited numerical precision must not be silently equated with fixed machine precision. The report's qualified computational claim applies to the proposed software selectors; it does not settle efficiency or biological implementation.

For the report's reset-to-one trace, threshold crossing is exactly a timer condition: elapsed time is less than −tau times log(theta). My arithmetic check below uses that equivalence. The thresholded response constrains the resulting time window, not tau and theta independently. A trace amplitude readout could distinguish parameter choices sharing the window.

Brian supports event-driven updates for suitable independent linear equations [checked S3, “Event-driven updates”]. This permits an economical implementation route, not a measured saving here. Naud and colleagues demonstrate several response regimes in a two-variable AdEx model, including rebound [checked S4, sections 2–3]. Those results concern firing behavior, not autonomous criticism.

One reading of the owner's idea is therefore implementation: compact traces can make relevant history inexpensive to retain. Another is search structure: timescales, adaptation and latches can make some histories easy to distinguish and others hard to preserve. A third is system organization: feedback between selector and program population could produce schedules and capabilities nobody enumerated individually. Each is compatible with digital implementation. None follows from temporal units alone.

In the hard-to-vary audit, history dependence is held by the identical-present/different-history distinction. The exponential implementation is loose because a timer supplies the same thresholded behavior. Information-bearing state has two routes: an explicit record or another adequate encoding. Particular time constants are loose pending cost and spacing tests. The grade rules are fixed by the brief. New capability creation remains unknown. These are marks of dependencies, not a ranking.

Long persistence can preserve unresolved cases but also obsolete suspicions; aggressive adaptation can free tests while discarding a necessary repeated check. Those tensions require explicit reset and retry conditions. Different allocations with no future task-performance difference would leave memory operational but its proposed practical contribution unsupported.

Grade 3 does not follow from replacing if-statements with dynamics. Conversely, fixed physical update laws alone do not rule it out: the question is whether checking code still computes a prescribed solution class or the operative standard itself changes through the system's interactions. These proposed circuits retain such checks. The owner can retain either interpretation of human task lists in the history of selected programs, either vocabulary for “instinct,” and their own account of knowledge; no naming decision is required for the interventions above.

# The sharpest test

## One experiment with a causal diagnostic and continuation

The proposed claim is narrow: retaining the direction of task-share change alters allocation at an identical present and contributes to later common-task acquisition beyond current rarity and a prerecorded schedule. This is a grade 2 allocation experiment over grade 1 tasks, not a grade 3 demonstration. It requires no new temporal task inside the Avida programs.

Use 77 existing task checks and an unchanged task-free ancestor. At each boundary compute p_j from a fixed bounded audit. Set fast and slow traces initially to zero. Update fast to 0.5 fast + 0.5 p_j and slow to 0.875 slow + 0.125 p_j. Temporal arm T uses u_j = 0.01 + (1−p_j) + max(fast−slow, 0). Memoryless arm M uses u_j = 0.01 + (1−p_j). Both allocate coefficient b_j = B[0.5/77 + 0.5 u_j/sum(u)]. Thus every task retains a positive floor and the nominal coefficient total stays B, including at a plateau. Fix B and its mapping to Avida's reward settings before outcome runs. Equal coefficient totals do not imply equal processor time actually earned; log both.

Arm Y applies a T schedule from a different, independent seed, without reading its own history. Pair adjacent seeds for this schedule exchange, fixing the mapping beforehand. T versus M tests the added historical term; T versus Y tests feedback to the receiving program population. A conventional register implementation of T runs on the same recorded audits without extra Avida continuations; its allocations should match T to the declared numerical tolerance. This controls implementation claims, not memory.

For the causal diagnostic, give cloned selectors two permutations of the same earlier audit records, followed by one identical current audit. Restore the identical program snapshot using the same initialization and random seed before applying either resulting allocation. No program population is advanced while these histories are injected. Hold record identities, counts, timestamp slots and current inputs fixed; change only order. Then change spacing with order fixed, using decay coefficients raised to elapsed duration in 1,000-update units, with complementary input weights. Erase both traces as a joint ablation. M must produce the same allocation at the shared endpoint; a suitable T history pair must differ. Constant histories initialized at their equilibrium and all-zero histories are negative controls. The synthetic scalar example below demonstrates the intended contrast, not an Avida observation.

During continuations, use the same save/reload procedure in all arms, retain controller state, and audit independently of native post-reload task records. This tests the interrupted execution regime described in the brief; it does not remove its limitations. Cache bounded-audit results by instruction sequence, inputs, instruction budget and executable/configuration identity. Use one fixed input triple in all six orders online, and a frozen disjoint panel of triples at the endpoint. Unfinished tests are unresolved, not absent capabilities. Freeze the execution limit and all parameters after an interface pilot, before collecting outcome seeds.

## Measures and falsifiers

The causal measure is the change in the 77 allocation coefficients at the identical endpoint. Log it before advancing Avida. The continuation endpoint is the number C of the 77 tasks performed by at least 10% of programs at 50,000 updates, assessed consistently with S113 where its protocol can be recovered. Report held-out input-order results separately; they are not automatically the same endpoint. Also record task acquisition and loss through time, earned processor time, replication capability and audit cost. Task counts do not measure criticism or unnamed knowledge creation.

For each seed record paired differences C_T−C_M and C_T−C_Y, with intervals and full seed values. For T−Y, resample whole donor pairs: exchanged schedules connect two seed blocks. No selective stopping or parameter changes after viewing these outcomes. If T fails to distinguish the diagnostic histories, the implementation fails its history claim. If the register version differs, resolve the numerical or interface discrepancy before attributing it to neurons.

A nonpositive population-level T−M effect counts against useful additional task acquisition by this circuit in this setting; an interval spanning consequential gains and losses leaves that effect unresolved. If the upper interval limit is below ten tasks, it counts against the chosen ten-task effect size. If Y reproduces T's outcome distribution, feedback-specific benefit remains unsupported. Such results do not eliminate all possible temporal selectors. Gains confined to native reload counters count against the measurement interpretation.

## Seeds and cost arithmetic

The supplied 48, 55, 65 and 13, 32, 41 are task counts, not seed identifiers [checked A1]. Treating each triplet as three observations solely for planning gives means 56 and 28.666667, sample variances 73 and 204.333333, and standard deviations 8.544004 and 14.294521. If these are selected range summaries rather than all independent observations, even those variance estimates are only illustrations.

For an explicitly chosen ten-task difference, a normal approximation using two-sided 5% error and 80% power gives n approximately 2(1.96+0.84) squared times variance divided by 100: 11.4464 → 12 seeds per arm from the growing-list triplet, and 32.039467 → 33 from all 77. This assumes zero cross-arm covariance. For paired arms multiply by (1−rho); rho is unknown. Three supplied values do not support a reliable power guarantee, and the calculation covers one comparison, not simultaneous confirmation of both contrasts.

A concrete budgeting option is 36 independent seed blocks for the all-77 setting, each with T, M and Y. Reusing one original program population repeatedly does not supply 36 independent ancestry histories. Register distinct seeds before running; do not invent the original S113 identifiers. The growing-list calculation is a sensitivity comparison, not another experimental condition.

At the brief's approximate rate [checked A1], 36 × 3 × 1 gives 108 CPU-hours for 50,000-update continuations, or about 36 wall-hours with at most three Avida processes. Six seed blocks would cost about 18 CPU-hours and six wall-hours, without the stated planning sample size. These are options for the owner, not launched runs.

Add total measured audit, controller, I/O and setup CPU-seconds divided by 3,600. Audit work may dominate: 108 runs × 50 boundaries × 3,600 distinct programs × six cases is a ceiling of 116,640,000 online bounded executions before caching, excluding endpoint tests. Time the pilot's audit throughput; do not quote 108 hours as an all-inclusive cost or assume the four CPUs can run four Avida processes.

# What no temporal unit can supply

No selector can distinguish histories that have become identical in every accessible state and future input. With the same random-state distribution, randomness cannot recover which history occurred. A trace cannot recover an omitted program identity or an unrecorded counterexample.

A signal cannot enforce a copy condition without a route to copy authorization. Activity following a failure cannot, by timing alone, identify its causal target. A fixed-capacity circuit cannot preserve arbitrarily many independently addressable unresolved cases. None of these limits is removed by calling the selector an agent.

These are information, interface and capacity limits, not a prohibition on neural representations of problems or criticisms. A sufficiently structured temporal system could implement the needed records, models and interventions. Whether it then creates knowledge under the owner's account remains open; the full project semantics and the relevant trial evidence were not supplied. The proposed circuits supply no basis for claiming that gap closed.

# What I ran with outputs and sources and uncertainties

## Execution record

I read both supplied files, extracted the Word report and checked the sources below. A local executable/workspace probe printed no Avida path or matching source file. I did not obtain a build, run Avida, inspect saved program populations, execute RUN_BOUNDED or access pilot outcomes. Document extraction and rendering are preparation, not experiments.

I ran two Python arithmetic checks. The first exploratory check initialized both traces at 0.5 and applied fast = 0.5 fast + 0.5 p and slow = 0.875 slow + 0.125 p to the two histories. Its complete output was:

[0.8, 0.2, 0.5] 0.4625 0.4958984375 -0.03339843749999999

[0.2, 0.8, 0.5] 0.5375 0.5041015625 0.03339843749999993

The second check evaluated exp(−gap/50) against threshold 0.5 and its equivalent timer; repeated those trace calculations; computed u for the proposed T and M rules; used sample variance with denominator two for each triplet; and evaluated the displayed sample-size and cost formulas. Complete output:

short: trace=0.818731; trace_gate=1; timer_gate=1

long: trace=0.135335; trace_gate=0; timer_gate=0

fall_then_middle: fast=0.462500000; slow=0.495898438; temporal_u=0.510000000; memoryless_u=0.510000000

rise_then_middle: fast=0.537500000; slow=0.504101563; temporal_u=0.543398437; memoryless_u=0.510000000

growing: mean=56.000000; sample_variance=73.000000; sample_sd=8.544004; n_raw=11.446400; n_ceil=12

all77: mean=28.666667; sample_variance=204.333333; sample_sd=14.294521; n_raw=32.039467; n_ceil=33

36 seeds x 3 arms x 1 CPU-hour = 108 CPU-hours; at 3 concurrent = 36 wall-hours

6 seeds x 3 arms x 1 CPU-hour = 18 CPU-hours; at 3 concurrent = 6 wall-hours

These are self-authored arithmetic cases, not independent evidence about Avida. They show different raw allocation scores at a common current share; normalized allocations also require the other task scores. No parameters were fitted to Avida outcomes.

## Sources

A1 — checked: supplied “04 Does temporal state close the gaps.md,” especially the Avida findings, earlier replies, grades and task. This checks what the brief reports, not its source-level or experimental claims independently.

A2 — checked: supplied “Temporal_Neuron_Computation_Report.docx,” especially comparison with logic gates, the order detector and model-testing cautions. Its 22-study bibliography was not checked wholesale.

S1 — checked: Computation Structures, “Sequential Logic,” sections 8.1–8.3. Registers, feedback and subsequent-state computation. https://computationstructures.org/notes/sequential_logic/notes.html

S2 — checked: Samuel A. Korsky and Robert C. Berwick, “On the Computational Power of RNNs” (2019), Theorems 1.1 and 2.1 and precision qualifications. https://arxiv.org/html/1906.06349v2

S3 — checked: Brian 2 version 2.10.0 documentation, “Synapses,” event-driven updates and their equation restrictions. https://brian2.readthedocs.io/en/2.10.0/user/synapses.html

S4 — checked: Richard Naud, Nicolas Marcille, Claudia Clopath and Wulfram Gerstner (2008), “Firing patterns in the adaptive exponential integrate-and-fire model,” Biological Cybernetics 99, 335–347, especially equations 1–3 and rebound discussion. https://lcnwww.epfl.ch/gerstner/PUBLICATIONS/Naud08.pdf

No outside-source claim is offered from memory. Circuits, bounds, causal distinctions and experimental proposals are my derivations, explicitly separate from these source reports.

## Remaining uncertainty

The exact S113 counting protocol and raw seed distribution, reward-coefficient semantics at commit 47f13dad, available boundary interfaces, audit speed and suitable execution limit require Claude's source and pilot checks. The neuron report does not settle whether temporal selection creates new problems or revises solution standards. An identical-present history intervention can settle whether the proposed memory changes selection; continuation runs are a separate part of the same experiment and remain optional for the owner.

END OF REPORT