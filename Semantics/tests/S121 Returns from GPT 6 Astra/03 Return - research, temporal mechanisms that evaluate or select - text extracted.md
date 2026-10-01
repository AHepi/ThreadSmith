*Text extracted by Claude from the .docx beside it (paragraphs and tables, in order), 1 October 2026; the .docx is the reply as sent.*

Temporal mechanisms for Avida computational selection

Checked research and source audit for Brief 03  |  2 October 2026

# Summary for the owner

Temporal mechanisms can make the Avida execution environment respond to its own history. They can reduce pay for recently common behavior, remember which earlier opportunity preceded an outcome, or predict what follows a choice. They do not, by themselves, supply a changing standard of success. The proposals here use grade 2 rules; named task checks remain a grade 1 layer.

For example, after many programs perform NOT, a fading trace could reduce its pay. After a quiet interval, that pay could recover. This can produce repeated switching without adding a new capability. Testing the distinction requires recording both newly acquired and retained capabilities.

Checked research already describes Avida resources that remember past consumption through depletion and renewal [31]. The neuron report has one mismatched citation, one mislabelled article and one partly supported simulation-cost citation. Its prominent numerical and hardware claims have source support within the qualifications below. No Avida experiment was run. The options leave the meaning of knowledge, whether fixed selection counts as instinct, and the next costly experiment open.

# Table

Grades apply separately to the selection rule and the task checker. “2 / 1” means a grade 2 selector acting on a grade 1 named-task substrate. Every implementation below is proposed, not run. Grade 1 names functions exactly; grade 2 names a class or rule; grade 3 requires a changing standard without checking code that defines a solution. Costs are incremental, estimated lines of driver code; C++ is zero for these blockwise versions, conditional on reusing the brief’s existing driver. References in this table are checked.

| Mechanism and operation | Function as an Avida selector | Grade | Cost estimate | What would count against the stated contribution | Sources |

| Habituation and stimulus-specific adaptation: response fades with repetition. | Reduce pay or tests for recently common behavior; restore it after absence. | 2 / 1 | 60–150 lines | A present-frequency rule reproduces the effect; only familiar behaviors cycle. | 23, 32 |

| Reward prediction error and TD: revise expected outcomes. | Learn which pay or opportunity choices precede a declared later return. | 2 / 1 | 150–300 lines | Predictions miss delayed consequences; noise attracts allocation when return does not. | 24, 25 |

| Eligibility traces: retain recent candidate causes. | Spread a later update across earlier selector actions. | 2 / 1 | 50–120 lines | Shuffled traces or zero trace give the same delayed-action behavior. | 24, 26 |

| Neuromodulated plasticity: gate changes to weights. | Permit selector learning only in specified contexts. | 2 / 1 | 80–180 lines | A matched constant learning rate has the same retention and switching behavior. | 26 |

| Homeostatic plasticity: compensate for sustained activity changes. | Keep opportunity or pay allocation within a declared operating range. | 2 / 1 | 60–150 lines | Only uniform pay scaling occurs, or oscillation replaces stable allocation. | 27 |

| Neuromodulation in evolutionary robotics: search for plastic controllers. | Search over a selector’s learning dynamics, outside Avida. | 2 / 1 | 300–700 lines | Performance depends on the familiar schedule or survives removing modulation. | 28 |

| Reservoir readout critic: map history to predicted return. | Choose pay or tests from a learned readout of program-population history. | 2 / 1 | 200–450 lines | A matched lagged linear critic captures the same consequences at the tested horizon. | 29 |

| Learning progress: track reduction in prediction error. | Allocate opportunities to behavior regions where prediction is changing. | 2 / 1 | 150–350 lines | Reload artefacts, forgetting or stochastic noise drive allocation without new retained capability. | 30 |

| Resource depletion and renewal: opportunity depends on consumption history. | Continuous Avida resource feedback; a driver can retain an external stock across pieces. | 2 / 1 | 0–180 lines | Instantaneous-frequency pay explains the observations; reset resource stocks drive them. | 31 |

# One section per mechanism

The frozen question is whether history in the Avida execution environment changes computational selection in ways that support further capability acquisition. The owner supplies that question; causal attribution and resistance to measurement artefacts are added audit requirements. Here “selector” means the observation–state–pay or opportunity loop. Each mapping below is an unrun design inference, separate from what the cited source reports.

A history-dependent selector and a history-dependent task are separate interventions. Paying memoryless tasks with a temporal driver does not make the tasks require memory. Conversely, a fixed checker can pay an Avida program for a temporal output. For the proposed comparisons, declare elapsed time in Avida updates, retain input identities, and keep the observation windows and total opportunity budget comparable.

## Habituation and stimulus-specific adaptation

Checked [32], pp. 17–19: habituation includes reduced response to repetition and recovery after a pause; its criteria exclude response loss entirely caused by receptor adaptation or fatigue. Checked [23], p. 10440 abstract/introduction: auditory responses can attenuate to a frequent sound while retaining a response to a rarer sound, with several timescales. Stimulus-specific adaptation is not identical to behavioral habituation; neither automatically distinguishes meaningful change from rarity.

Avida proposal: maintain a separate fading count for each observed behavior. Repetition reduces its later pay or testing share; time without it permits recovery. A single global fatigue value cannot preserve which behavior became familiar. The behavior description, decay times, recovery rule and pay mapping are named in advance: grade 2, with grade 1 retained wherever stock named tasks are checked. Estimated driver cost is 60–150 lines, no C++ for blockwise control of existing task pay. New behavioral signatures need a separate payment interface.

Against the temporal contribution: match current task shares while varying earlier exposure and quiet intervals. If pay does not follow the stored history, the implementation misses its claim. If a present-frequency controller produces the same downstream behavior, the added trace has no demonstrated role on those cases. Repeated switching among familiar capabilities counts against the separate claim of continuing capability acquisition.

## Reward prediction error and temporal difference learning

Checked [24], §§2.2–2.3 and 5.2, and [25], p. 1595, Eq. 3: TD learning updates predictions from successive predictions and outcomes. Reward prediction error is signed: received reward plus discounted next value minus present predicted value. It is not simply unusualness.

Avida proposal: make the driver the decision-maker. Its action is a pay vector or opportunity allocation; its observation is the program-population summary; its declared return might be retained performance on a fixed probe set after a delay. A critic predicts that return and changes subsequent choices. Observation features, action space, return, discount horizon and update rule are explicit: grade 2 over any grade 1 checks. Estimated cost is 150–300 driver lines, zero C++.

Against: compare predicted and observed consequences after an unannounced change, using frozen held-out probes. Compare live feedback with blind schedule replay and with the same driver without prediction learning. If the responsive loop merely rewards large absolute errors on an unpredictable stream, it is implementing surprise-seeking, not the stated signed-return rule. A prediction error signals a discrepancy; it does not supply a criticism aimed at a conjecture’s part.

## Eligibility traces

Checked [24], §2.3, pp. 15–16, and [26], Methods pp. 2444–2445, Eqs. 1–2: traces keep fading records of prior activity so a later signal can update earlier contributions. In [26] a dopamine-like signal acts on a synaptic eligibility trace. This is a computational credit-assignment model, not a demonstration that temporal proximity establishes causation.

Avida proposal: retain traces of the driver’s earlier allocation choices, then apply a later declared outcome to those traces. Use selector-action traces first; individual-program traces require stable identity and program ancestry records across replacement. The trace decay and outcome source remain named: grade 2 over grade 1 tasks. Estimated incremental cost is 50–120 driver lines, zero C++. An eligibility trace supplies no criterion on its own.

Against: delay an otherwise identical consequence, insert unrelated intervening actions, and compare intact, shuffled and zeroed traces under matched budgets. If unrelated recent actions receive the same credit as the manipulated antecedent, the proposed assignment is confounded. If removing traces does not change the delayed-choice result at the claimed horizon, this component has no demonstrated contribution there.

## Neuromodulated plasticity

Checked [26], Methods and Fig. 1: a third signal gates changes to eligible connections. That changes when activity leaves a lasting effect. The experimenter still supplies the rewarding event in this model.

Avida proposal: gate updates to the selector’s weights using a defined signal, such as a sustained change in residual prediction error. This changes learning sensitivity; it need not directly alter pay. Keep the gate separate from the critic’s outcome and the pay readout. The gate signal, thresholds, eligible weights and outcome are named: grade 2, not grade 3, with grade 1 task checks retained. Estimated extra cost is 80–180 driver lines, zero C++.

Against: freeze the gate, replay its past values blindly, and substitute a constant learning rate matched for total update magnitude. If all preserve the same switching and retained-capability behavior, conditional gating has no demonstrated role. Test abrupt change and unchanged conditions separately: a gate that reopens on every reset may erase learned behavior without detecting a change in the program population.

## Homeostatic plasticity

Checked [27], pp. 893–895, Figs. 1–4: cortical cultures compensate for sustained activity manipulation through changes in excitatory synaptic strengths, including approximately multiplicative scaling. This concerns stabilization of activity, not a mechanism that chooses new problems.

Avida proposal: maintain a slow record of allocation or activity and adjust gains to keep a declared quantity within an operating range. For example, preserve testing opportunities for several behavior regions while another selector sets their relative priority. Setpoints, measured activity, timescale and clipping limits are fixed choices: grade 2 over any grade 1 task checks. Estimated cost is 60–150 driver lines, zero C++.

Against: impose a temporary activity drop and inspect recovery after removing it. Compare simple budget normalization. Uniformly multiplying all pay can leave relative computational selection unchanged, depending on basal pay and resource saturation; measure those quantities. Overshoot, oscillation, or compulsory preservation of unproductive categories counts against the specified stabilization job. Stabilization alone is not evidence of new capability acquisition.

## Neuromodulation in evolutionary robotics and artificial life

Checked [28], pp. 570–572, Eqs. 1–4 and the T-maze experiments: evolutionary search constructs neural controllers with modulatory signals that gate plasticity. Reward locations change during a simulated agent’s lifetime. This is a precedent for searching over learning dynamics, not an Avida execution-environment selector experiment.

Avida proposal: an outer search varies a small driver controller whose outputs set pay or opportunity. Each candidate is evaluated over multiple Avida histories; its within-run state can change. The outer evaluation, controller family and observation interface are named: grade 2, with a grade 1 substrate if named Avida tasks remain. Estimated scaffolding is 300–700 driver lines, zero C++ for blockwise operation; evaluation costs multiply by candidate count.

Against: test a held-out change schedule and compare removing modulation, freezing plasticity and replaying the same allocation schedule. If the controller only tracks a familiar timetable or its adaptive behavior remains unchanged after modulation is removed, the proposed adaptive mechanism is not isolated. Moving the designer’s objective to the outer search does not make the target unnamed.

## Reservoir or liquid state readouts used as critics

Checked [29], §2, Eqs. 1–4, and §3: an echo-state reservoir with fixed recurrent weights supplies history-sensitive features; a learned readout estimates future utility for robot control. This opened source directly demonstrates an echo-state critic. A spiking liquid-state substitution is a proposed variant here, not an inspected Avida result.

Avida proposal: feed task shares, resource levels, past allocations and time gaps into a small reservoir. Train a readout to predict a declared later outcome and let the driver choose opportunities from that prediction. Outcome, training loss, inputs and action rule are named: grade 2 over any grade 1 tasks. Estimated cost is 200–450 driver lines, zero C++; recurrent state and readout weights must survive between pieces.

Against: compare a linear critic supplied with an explicit matched history window, then reset or shuffle reservoir state while preserving current observations. If both critics have the same tested behavior, the specific reservoir representation remains replaceable. A rich state cannot recover within-piece order discarded by the observation interface. Dense recurrent updates cost quadratically in reservoir size; sparse updates depend on connection count. These are implementation estimates, not measured Avida costs.

## Learning progress as a temporal selector

Checked [30], §III.C and §IV.E–F: Intelligent Adaptive Curiosity allocates activity using changes in prediction error within regions of experience. Its temporal signal concerns learning progress rather than raw high error; the experiments include situations with differing predictability.

Avida proposal: keep short and long error records for each behavior region and allocate opportunities where held-out prediction error is decreasing. Record progress using a stable probe distribution so changing sample composition does not manufacture it. Regions, error measure, windows and allocation rule are named: grade 2 over any grade 1 tasks. Estimated cost is 150–350 driver lines, zero C++.

Against: include a learnable stream, a constant stream and irreducible noise, then remove the temporal difference while retaining current error. Reload-induced undercounts, forgetting followed by relearning, or moving probes can all create apparent progress. If allocation follows these artefacts while acquired and retained capabilities do not change, it counts against the proposed progressive-learning role. This criterion can also neglect a difficult capability before any measurable progress appears.

## Resource depletion and replenishment

Checked [31], p. 84: Avida pay for named logic functions depends on resources consumed by the program population; those resources are replenished by inflow and reduced by outflow and consumption. Resource stocks therefore carry the effects of earlier activity. This is already temporal feedback in the Avida execution environment.

Avida proposal: use stock resources in continuous execution, or maintain an external resource record across pieces. Because reload resets resource stocks, merely changing inflow does not preserve their history; a blockwise external pool approximates within-piece consumption. The named functions remain grade 1; resource-use and renewal rules are grade 2. Changing resource stocks alone does not meet grade 3. Estimated code cost is zero for an available stock configuration, or 80–180 driver lines for an external pool; zero C++. Compatibility with the stated Avida commit needs source/configuration checking by Claude.

Against the temporal explanation: create equal present task shares but different prior consumption, then measure resource levels and pay. Clamp resource stocks or compare a current-frequency rule. If the tested history effect survives clamping resource stocks, resource memory is not isolated on those cases. A system that preserves several familiar task-use patterns has not thereby shown continuing acquisition of capabilities beyond its named repertoire.

# The report’s 22 sources

“Holds” concerns the report’s stated claim at the inspected location; it is not a reproduction of the study. Original links were attempted individually. A footer, browser check or cookie error is recorded separately from support obtained through an opened alternate copy. Where an original endpoint remained unreadable, its live resolution remains uncertain; the claim check rests on the identified alternate. Reference numbers below preserve the report’s numbering.

| Source | Mark | Claim and access record |

| 1 | checked: holds | Original PDF opened. §II and Fig. 1, pp. 1063–1065: 20 behaviors, simulated with the same equations and different parameters. Some are mutually exclusive; this is not 20 cell types or simultaneous behavior. |

| 2 | checked: holds | PubMed returned a footer; published PDF opened elsewhere. Summary p. 989 and Fig. 1: a CA1 simulation’s firing-rate mapping uses two layers. The Boolean example is illustrative. |

| 3 | checked: holds in part | PubMed returned a footer; publisher abstract opened. It supports nonlinear local dendritic summation. The report labels it a review; it is a primary experimental article. |

| 4 | checked: holds | PubMed abstract opened. Five to eight temporal-convolutional layers model the stated simulated layer-5 cell at millisecond resolution. This is conditional on the model and method, not a universal conversion. |

| 5 | checked: holds | Original course notes opened, §§8–8.2.1. Gates with feedback store state. The finite-precision neuron argument is the report’s mathematical inference, not a neuron experiment. |

| 6 | checked: does not hold | The PMID identifies Brette and Gerstner’s 2005 AdEx modelling article, not a dendritic sequence experiment. Identity checked through PubMed and the author’s publication list; full paper not read. Use source 7 for the sequence claim. |

| 7 | checked: holds | PMC gave a browser check; author-hosted published PDF opened. pp. 1671–1675, Figs. 1–4: cortical dendrites distinguish direction, input speed and input order experimentally. |

| 8 | checked: holds | PMC access was intermittent; publisher full text opened. §2, Eqs. 1–3; §3 and Fig. 4: voltage/adaptation state, multiple patterns, and rebound after abrupt versus gradual release. |

| 9 | checked: holds | Original Brian 2.10.0 page opened, Event-driven updates. Independent one-dimensional linear synaptic traces have event updates. This does not make the whole simulator asynchronous. |

| 10 | checked: holds | Original abstract and arXiv v2 full text opened, §§3.2 and 3.5.2. Input-dependent state parameters govern retention. The report makes a computational analogy, not a physiology claim. |

| 11 | checked: holds in part | Original Brian stable page, resolving to 2.10.1, opened. Clock-driven versus event-driven supports restrictions and timing-grid error; it does not substantiate the report’s specific sparse-activity speed-saving claim. |

| 12 | checked: holds | Publisher full text reached through its cookie redirect. Introduction and Stability analysis, Fig. 3: one-state LIF and numerical-instability cautions are supported. Not evidence of a general event-driven runtime saving. |

| 13 | checked: holds | Original full text, §4.3, Figs. 7–8: SpiNNaker tests synthetic −30, 0 and +30 microsecond differences, with ±5 microsecond jitter. Hardware model; generated inputs. |

| 14 | checked: holds | Publisher full text opened after cookie redirect. Published 23 May 2026. Chirp test and Temporal detection test, Figs. 8–9: measured bandpass and optical timing responses. Prospective multi-GHz operation is simulated. |

| 15 | checked: holds | Publisher full text opened after cookie redirect. Fig. 9 and Methods: digit/speech tests and hybrid UP/DOWN demonstration. Adaptive thresholds use CMOS-OxRAM circuits; integrators/comparators and other network operations use software. |

| 16 | checked: holds | Original project tutorial opened. Silicon neuron implementation and Bursting describe configurable AdEx hardware and initial/regular bursting. This is documentation with a hardware-run example, not a newly reproduced experiment. |

| 17 | checked: holds | arXiv full text opened, including version 1. Sections II.1–II.2 report measured rate/latency encoding; section IV and Fig. 10 explicitly use numerical multilevel reconstruction. |

| 18 | checked: holds | Original DOI landing page and publisher PDF opened. Published 24 December 2024. pp. 2–4, Figs. 1–3: physical RTD set/reset memory; switching depends on pulse timing. |

| 19 | checked: holds | Original publisher full text opened. Sections 2.1, 2.4, 3.3 and 4.2: compartmental simulation and restricted direction-reversal learning. The report correctly separates this from experiments in living cells. |

| 20 | checked: holds | Publisher abstract and complete supplements opened; main body paywalled. Supplementary Methods pp. 1–2 document simulations; Supplementary Note p. 2 and Fig. 1 support a binary time-window decision. |

| 21 | checked: holds | PMC access was intermittent; publisher full text opened. Abstract and Figs. 6–9 report simulated sub-millisecond output timing and classification through shared target patterns. |

| 22 | checked: holds | Publisher full text obtained after cookie redirect. Delay characterization measures 8.08–58.26 ms; Hardware-aware simulations uses a speech-delay distribution with 500 ms mean. The report’s circuit/benchmark caveat holds. |

# Where nothing is known

This bounded search opened the report’s sources and targeted primary work on adaptation, TD learning, traces, plasticity, robotics, reservoirs, learning progress and Avida resources. Search queries included “Avida adaptive environment selection temporal memory neuromodulation learning progress digital evolution” and “Avida habituation reward prediction error reservoir critic”, supplemented by paper-title and source searches. It was not a census.

Checked [31] prevents a broad claim that temporal selection in Avida is absent. The search did not identify a direct demonstration of the particular blockwise learned selector proposed here, with persistent selector state, declared restart effects, blind-replay controls and independent retained-capability measurements. No conclusion about its absence elsewhere follows. A liquid-state critic for this Avida interface was not located either.

Grade 3 remains unresolved. A moving novelty threshold, learned reward predictor or changing task generator still falls under grade 2 when checking code determines what earns success. A candidate interaction-based standard would have to explain where selective consequences arise without a solution-checking predicate. Fixed simulation laws alone neither exclude nor demonstrate that possibility. None of the mappings above is presented as grade 3.

Hard-to-vary assessment: history-bearing state is held if distinct histories must change responses to identical present observations; the neuron-like representation is loose where a timer or ordinary stored history does the same job. The observation interface and progressive capability-acquisition claim are unknown. The grades are fixed by the owner. Restart behavior is borrowed from S114, not reproduced here. The empirical mechanisms are borrowed from the checked literature; the Avida mappings are newly built proposals, not fitted results.

The trace/timer swap matters: for the report’s resetting exponential trace and a single threshold, a timestamp gives the same response window. Additional dynamics need an additional discriminating job. The interaction also matters: novelty pressure can redirect opportunities away from capabilities that need maintenance. Record acquisition and retention separately. A count of functions is a restricted observation, not a settled definition of knowledge.

# Options for Claude

None is chosen. Costs below are estimates using the brief’s one CPU-hour per 50,000 updates at 3,600 cells, linearly scaled. They exclude compilation, driver overhead, archive storage and bounded replay of saved programs. The linear assumption itself is unmeasured here. Keep at most three Avida processes active; CPU-hours are not elapsed hours.

| Option | Design and scope | CPU-hours estimate |

| Driver and observation check | Replay saved summaries through a frozen selector. Change order, spacing and history while matching present observations; include constant and noisy streams. No new Avida run. | 0 Avida CPU-hours; driver time unmeasured. |

| Short causal pilot | One selected mechanism; live feedback, blind replay, fixed mean allocation and memory ablation. Three starting seeds each; 10,000 updates per run. | 12 × 0.2 = 2.4, plus replay/driver overhead. |

| Longer matched comparison | Same four arms and three seeds, 50,000 updates each. Freeze probes and budgets before execution. | 12 × 1 = 12, plus overhead. |

| Restart contribution | Continuous and chunked protocols, three seeds each, 50,000 updates. Hold pay schedules fixed where feasible; measure reset effects explicitly. | 6 × 1 = 6, plus overhead. |

| Outer controller search | For C candidate controllers, R trials each, U updates per trial; separate held-out evaluation. No population size or search budget chosen. | C × R × U/50,000; e.g. 20 × 3 × 10,000 gives 12, before held-out tests. |

Before an Avida comparison, freeze observation features, clocks, state persistence, controller actions, pay strength, probes and predicted counter-results. A 50,000-update run in 1,000-update pieces supplies only 50 selector decisions; critic size and training data must reflect that. The brief reports that reloading preserves instruction sequences but drops processor, random, resource and task-record state. Preserve driver traces, learned weights and archives explicitly; log simulator resets. Re-evaluating saved instruction sequences on common probes measures tested capability, not continuation of the original processor state. If continuation cannot be preserved, describe the experiment as periodically restarted and match boundaries across arms.

For order and spacing tests, use equal input identities and counts, with order and timing manipulated separately. Perturb only observed task counts in an additional replay to expose responses to measurement artefacts. Replay schedules on a different seed or history, or after a held-out perturbation: replay on the same seeded trajectory can reproduce the original by construction. A blind replay can test dependence on feedback; it cannot alone isolate which memory mechanism caused an effect. Within-piece temporal questions need observations that retain within-piece timing; end-of-piece totals cannot supply it.

An in-process alternative could avoid driver-induced restarts. A narrowly scoped observation/control hook might require 200–500 C++ lines, estimated, plus driver code; this estimate excludes complete simulator checkpointing and has not been checked against commit 47f13dad. The owner can separately decide whether a human-written task list counts in program history, what counts as knowledge, and whether fixed selector dynamics deserve the name instinct.

# References

Every entry below is checked through the stated opened material. No from-memory reference carries a finding. An abstract-only check is labelled. Source numbers 1–22 match the supplied report; 23–32 support the mechanism research. Titles are retained as bibliographic identifiers.

[1] Checked. Izhikevich (2004). Which Model to Use for Cortical Spiking Neurons? IEEE Transactions on Neural Networks 15, 1063–1070. Opened: full PDF, §II, Fig. 1 and §III.F. Original link

[2] Checked. Poirazi, Brannon and Mel (2003). Pyramidal Neuron as Two-Layer Neural Network. Neuron 37, 989–999. Opened: published PDF, Summary p. 989 and Fig. 1. Original link · Text inspected

[3] Checked. Polsky, Mel and Schiller (2004). Computational subunits in thin dendrites of pyramidal cells. Nature Neuroscience 7, 621–627. Opened: publisher abstract and metadata only. Original link · Text inspected

[4] Checked. Beniaguev, Segev and London (2021). Single cortical neurons as deep artificial neural networks. Neuron 109, 2727–2739.e3. Opened: PubMed abstract and metadata only. Original link

[5] Checked. Ward (undated). Sequential Logic. Computation Structures course notes. Opened: original page, §§8–8.2.1. Original link

[6] Checked. Brette and Gerstner (2005). Adaptive exponential integrate-and-fire model as an effective description of neuronal activity. Journal of Neurophysiology 94, 3637–3642. Opened: article identity and author publication list only; citation mismatch. Original link · Text inspected

[7] Checked. Branco, Clark and Häusser (2010). Dendritic Discrimination of Temporal Input Sequences in Cortical Neurons. Science 329, 1671–1675. Opened: author-hosted published PDF, Figs. 1–4. Original link · Text inspected

[8] Checked. Naud, Marcille, Clopath and Gerstner (2008). Firing patterns in the adaptive exponential integrate-and-fire model. Biological Cybernetics 99, 335–347. Opened: publisher full text, §§2–3 and Fig. 4. Original link · Text inspected

[9] Checked. Brian team (undated). Synapses. Brian 2.10.0 documentation. Opened: Event-driven updates and Explicit event-driven updates. Original link

[10] Checked. Gu and Dao (2023, revised 2024). Mamba: Linear-Time Sequence Modeling with Selective State Spaces. arXiv:2312.00752. Opened: abstract and full version 2, §§3.2 and 3.5.2. Original link · Text inspected

[11] Checked. Brian team (undated). How Brian works. Brian documentation, stable page resolving to 2.10.1. Opened: Clock-driven versus event-driven. Original link

[12] Checked. Baronig, Ferrand, Sabathiel and Legenstein (2025). Advancing spatio-temporal processing through adaptation in spiking neural networks. Nature Communications 16, 5776. Opened: publisher full text, Introduction and Stability analysis, Fig. 3. Original link

[13] Checked. Lagorce et al. (2015). Breaking the millisecond barrier on SpiNNaker: implementing asynchronous event-based plastic models with microsecond resolution. Frontiers in Neuroscience 9, 206. Opened: full text, §§1, 4.3, Figs. 7–8. Original link

[14] Checked. Adair et al. (2026). Resonate-and-fire photonic-electronic spiking neurons for fast and efficient light-enabled neuromorphic processing systems. Communications Physics 9, 271. Opened: publisher full text, Chirp test and Temporal detection test, Figs. 8–9; publication metadata. Original link

[15] Checked. Shaban, Bezugam and Suri (2021). An adaptive threshold neuron for recurrent spiking neural networks with nanodevice hardware implementation. Nature Communications 12, 4234. Opened: publisher full text, Fig. 9; Methods, Experimental setup for end to end speech recognition. Original link

[16] Checked. BrainScaleS-2 contributors (undated). Complex Neuron Dynamics with a Silicon Adaptive Exponential Integrate-and-Fire Neuron. Project documentation. Opened: original tutorial, Silicon neuron implementation and Bursting. Original link

[17] Checked. Donati et al. (2025). Spiking Rate and Latency Encoding with Resonant Tunnelling Diode Neuron Circuits and Design Influences. arXiv:2503.21342v1. Opened: full text, sections II.1–II.2 and IV, Figs. 2–4 and 10. Original link · Text inspected

[18] Checked. Donati et al. (2024). Spiking Flip-Flop Memory in Resonant Tunneling Diode Neurons. Physical Review Letters 133, 267301. Opened: publisher abstract and full PDF, pp. 2–4, Figs. 1–3. Original link · Text inspected

[19] Checked. Tamura, Yamamoto, Kobayashi, Kuriyama and Yamazaki (2023). Discrimination and learning of temporal input sequences in a cerebellar Purkinje cell model. Frontiers in Cellular Neuroscience 17, 1075005. Opened: publisher full text, sections 2.1, 2.4, 3.3 and 4.2. Original link

[20] Checked. Gütig and Sompolinsky (2006). The tempotron: a neuron that learns spike timing–based decisions. Nature Neuroscience 9, 420–428. Opened: publisher abstract, Supplementary Methods, Supplementary Note and Supplementary Fig. 1; main body not read. Original link · Text inspected

[21] Checked. Florian (2012). The Chronotron: A Neuron That Learns to Fire Temporally Precise Spike Patterns. PLOS ONE 7, e40233. Opened: publisher full text, Abstract and Figs. 6–9. Original link · Text inspected

[22] Checked. D’Agostino et al. (2024). DenRAM: neuromorphic dendritic architecture with RRAM for efficient temporal processing with delays. Nature Communications 15, 3446. Opened: publisher full text, Delay characterization, Hardware-aware simulations and Outlook; author preprint also opened. Original link · Text inspected

[23] Checked. Ulanovsky, Las, Farkas and Nelken (2004). Multiple Time Scales of Adaptation in Auditory Cortex Neurons. Journal of Neuroscience 24, 10440–10453. Opened: author-hosted published PDF, p. 10440 abstract/introduction only, visually inspected; later-page retrieval failed. Original link

[24] Checked. Sutton (1988). Learning to Predict by the Methods of Temporal Differences. Machine Learning 3, 9–44. Opened: full PDF, §§2.2–2.3 and 5.2. Original link

[25] Checked. Schultz, Dayan and Montague (1997). A Neural Substrate of Prediction and Reward. Science 275, 1593–1599. Opened: author-hosted paper, p. 1595, Eq. 3; synthesis of evidence and model. Original link

[26] Checked. Izhikevich (2007). Solving the Distal Reward Problem through Linkage of STDP and Dopamine Signaling. Cerebral Cortex 17, 2443–2452. Opened: author PDF, Methods pp. 2444–2445, Eqs. 1–2 and Fig. 1. Original link

[27] Checked. Turrigiano et al. (1998). Activity-dependent scaling of quantal amplitude in neocortical neurons. Nature 391, 892–896. Opened: published PDF, pp. 893–895, Figs. 1–4. Original link

[28] Checked. Soltoggio, Bullinaria, Mattiussi, Dürr and Floreano (2008). Evolutionary Advantages of Neuromodulated Plasticity in Dynamic, Reward-based Scenarios. Artificial Life XI, 569–576. Opened: author PDF, pp. 570–572, model and T-maze protocol. Original link

[29] Checked. Oubbati, Kächele, Koprinkova-Hristova and Palm (2011). Anticipating Rewards in Continuous Time and Space with Echo State Networks and Actor-Critic Design. ESANN, 117–122. Opened: proceedings PDF, §§2–3, Eqs. 1–4. Original link

[30] Checked. Oudeyer, Kaplan and Hafner (2007). Intrinsic Motivation Systems for Autonomous Mental Development. IEEE Transactions on Evolutionary Computation 11, 265–286. Opened: author PDF, §III.C and §IV.E–F. Original link

[31] Checked. Chow, Wilke, Ofria, Lenski and Adami (2004). Adaptive Radiation from Resource Competition in Digital Organisms. Science 305, 84–86. Opened: author-hosted published PDF, p. 84 resource dynamics. Original link

[32] Checked. Thompson and Spencer (1966). Habituation: A model phenomenon for the study of neuronal substrates of behavior. Psychological Review 73, 16–43. Opened: full paper, pp. 17–19, Parametric characteristics; theoretical framework, review and physiological experiments. Original link

# What you ran, and what you are unsure of

No Avida executable, evolutionary-computation experiment, hardware experiment or neuron simulation was run. I did not inspect or build Avida commit 47f13dad. The S113–S120 outcomes and local interfaces are supplied premises, not reproduced results; no pilot outcome was presumed. Code-size and CPU-hour figures above are estimates, not benchmarks.

I ran local document extraction, report assembly, a text/structure check and page rendering for layout inspection. Those operations concern the documents only. The report check prints the following output; the command was "$CODEX_PRIMARY_RUNTIME_PYTHON" check_report.py on this final DOCX.

AUDIT_ROWS=22MECHANISM_SECTIONS=9REFERENCES=32FINAL_LINE=END OF REPORT

Uncertainty remains about costs at the stated Avida commit, observation sufficiency, the consequences of periodic restarting, results on held-out histories, and whether any proposed behavior warrants the owner’s term knowledge. A bounded source search cannot settle nonexistence. Sources accessed only through abstracts or alternate copies remain limited to the claims and versions stated in the audit. Reading a paper is not rerunning its experiment.

END OF REPORT