# Evaluation inside Avida programs using stock features

## Summary for the owner

One program sends the number 1. A neighboring program reads it, subtracts 1, and transfers energy only if the result is zero. Replace the sender's number with 0: the transfer stops. Change the evaluator's arithmetic: its choice can change. This is a concrete way to put a small decision inside an executing program.

**Checked, source inspection:** Avida 2.14.0 at commit `47f13dadb547fcf10f620ace60247f38b30b8b16` supplies the necessary instructions. They require an extended instruction-set file, but use the same heads virtual CPU. The unchanged standard 26-instruction set does not supply these interactions.

**Checked, source inspection:** Mate preferences, parasite task compatibility, and deme competition also affect selection, but their candidate comparisons are written in C++. They must not be mistaken for a program computing its own test.

The two experiments below test decisions about a received number and a neighbor's displayed reputation. The evaluator's arithmetic can change during replication. A separate encounter assay holds candidates fixed, freezes evaluator sequences, swaps recipients after the arithmetic, and disables transfers.

These are feasibility experiments. Their starting evaluators are hand-written, and only their arithmetic can change. They do not demonstrate the creation of an evaluator from the earlier ancestor, assessment of a candidate's computational correctness, or progressive creation of knowledge. Those remain separate questions.

**Checked, local runs:** The source compiled unchanged. Both encounters, rejection and arithmetic-change cases, 100-update populations, and snapshot replay were run. The proposed 5,000-update trials remain unrun.

## Mechanisms found in Avida 2.14.0

**Checked:** The inventory below refers to the pinned source, not feature names in old example files. “Extended heads” means stock `hw_type=0` with additional `INST` declarations; it is neither the unchanged heads-26 set nor new C++. Source paths are under `avida-core/`; exact locations are collected later. The inventory covers the requested families and additional interprogram families encountered in the active instruction libraries. It is not a runtime test of every variant.

| Mechanism | Checked source and activation | Concrete interpretation of evaluation |
|---|---|---|
| Sexual replication and recombination | `cHardwareCPU::Inst_HeadDivideSex`, `cBirthChamber::SubmitOffspring/DoBasicRecombination`. Extended heads `divide-sex`/`div-sex`; bundled `instset-heads-sex.cfg`. `RECOMBINATION_PROB`, `MAX_BIRTH_WAIT_TIME`, `TWO_FOLD_COST_SEX`; optional module and same-length settings. | Pairing and instruction exchange supply consequences, not an executable test. Recombination probability zero still permits pairing. |
| Mate labels | `Inst_HeadDivideMateSelect`, `cBirthMateSelectHandler::SelectOffspring`. Extended heads `div-sex-MS`, `ALLOW_MATE_SELECTION 1`; for the direct global route use `NUM_DEMES 1`, `MATING_TYPES 0`, `BIRTH_METHOD 4`, `SAME_LENGTH_SEX 0`. | A program chooses a label or which labeled division to execute; C++ matches labels. |
| Mate preferences and displays | `Inst_SetMatePreference`, display/type setters; `cBirthMatingTypeGlobalHandler::selectMate/compareBirthEntries`. Extended heads mating-type, display and `set-mate-preference-*` instructions; `MATING_TYPES 1`, `FORCED_MATE_PREFERENCE -1`, chamber size, `LEKKING`, optional assessment noise/group restrictions. | The executable selects among seven supplied comparisons; the candidate comparison itself stays in C++. Multiple demes take precedence over this handler. |
| Deme competition and replication | `cPopulation::CompeteDemes/ReplicateDemes/ReplicateDeme`; `CompeteDemes`, `ReplicateDemes` events and specialized competition actions. `NUM_DEMES>1`, seeding/germline/competition/trigger settings. Can surround heads-26 programs without extra instructions. | C++ compares group quantities. Group consequences can select programs containing evaluators, but do not themselves constitute executable evaluation. |
| Program-requested deme spawning | Extended heads `spawn-deme`: `Inst_SpawnDeme` → `cPopulation::SpawnDeme`; requires multiple demes. | A program chooses when to request spawning. The environment chooses another deme and a source program. `repro_deme` sets a flag; no consumer of its getter was found. |
| Parasites and executing injected code | `cHardwareTransSMT::Inst_Inject/InjectParasite/ParasiteInfectHost`, `cPopulation::ActivateParasite/TestForParasiteInteraction`. Requires TransSMT `hw_type=2`, its own ancestor and case-sensitive `Inject`; thread/memory limits, injection mutation settings, `INFECTION_MECHANISM`, `INJECT_METHOD`, virulence settings. | Programs initiate injection and injected code executes inside a host CPU. Task-repertoire compatibility is compared in C++. Heads `ParasiteInfectHost` returns failure. Host-controlled virulence is a C++-inherited scalar, not an executable assessment. |
| Horizontal instruction transfer | `cHardwareBase::Divide_DoMutations`, `cPopulationInterface::DoHGTMutation/DoHGTConjugation`. `ENABLE_HGT`, conjugation/competence probabilities, source/placement/fragment settings; no additional heads instruction needed. | Division triggers transfer. `HGT_CONJUGATION_METHOD 1` uses the faced donor, so program orientation can affect donor identity. Fragment matching/incorporation remains C++. No direct HGT-request instruction was found. |
| Direct attacks and predator–prey | Extended heads `get-faced-vitality-diff`, `get-faced-org-id`, `get-attack-odds`, `attack-faced-org`; combat rule `MOVEMENT_COLLISIONS_SELECTION_TYPE`. Experimental `hw_type=3` has `attack-prey`, category/ID-specific attacks, sensors and displays; `PRED_PREY_SWITCH`, odds, efficiency, injury, prey limits and optional bins/avatars. GP8/BCR also register attack/sensing operations. | A program can read a candidate, compute, and conditionally attack. Combat outcome and payoff remain instruction meanings. An unconditional attack alone shows no candidate-dependent test. |
| Scalar communication | `Inst_Send/Inst_Receive`, `cPopulationInterface::ReceiveValue`. Extended heads `send`, `receive`; no message-buffer switch needed. | `send` publishes BX; `receive` retrieves a neighbor's value and leaves that sender as the faced neighbor. Arithmetic can compute whether to act on it. No sender returns zero, which is ambiguous with a sent zero. |
| Buffered messages, alarms, flashes and networks | Extended heads message retrieval/sending/broadcast, alarm, flash and `network-*`/`create-link-*` instructions; `cHardwareCPU` methods and `cPopulationInterface` routing. `MESSAGE_SEND_BUFFER_SIZE`, `MESSAGE_RECV_BUFFER_SIZE/BEHAVIOR`, `NET_DROP_PROB`; `ACTIVE_MESSAGES_ENABLED 2` and available CPU threads for handlers; `BCAST_HOPS`, `SYNC_FLASH_LOSSRATE`; `DEME_NETWORK_*` for networks. `CHECK_TASK_ON_SEND` controls an additional environment task-check path. | Programs exchange values, construct links and route messages. A program can evaluate received data; message delivery or graph construction alone is not evaluation. Buffered retrieval exposes label/data rather than a general authenticated candidate identity. |
| Opinions, reputation, states and social admission | Extended heads `set-opinion`, `get-opinion`, reputation/raw-material/energy/vitality sensors, `pose`, group and tolerance instructions. `AUTO_REPUTATION`, `INHERIT_REPUTATION`; for admission `USE_FORM_GROUPS`, tolerance window/maximum/variation and group settings. | `get-opinion` reads self. `get-neighbors-reputation` reads the faced program; arithmetic can supply a test. `pose` can raise reputation without donating. Built-in reputation rotation and group-admission aggregation use C++ criteria. No callable heads `get-neighbors-opinion` was found, but reputation is stored as an opinion: the reputation sensor also exposes that peer value. |
| Donations, cooperation and public goods | Extended heads merit/energy/resource/raw-material/string donations, reciprocal/kin/distance variants, cooperation and lysis operations; task definitions in `cTaskLib`. Energy routes need `ENERGY_ENABLED` and a nonzero energy source; sharing mode governs receipt. Merit routes use `MERIT_GIVEN/RECEIVED`, `MAX_DONATES` and kin/distance settings. Bin donation uses `USE_RESOURCE_BINS` and `COLLECT_SPECIFIC_RESOURCE`; raw materials/strings use `ALT_COST`, material amounts, stock caps and failure settings. | A program can compute whether to transfer support. Built-in kin/reciprocity tests remain supplied tests. An environment-rewarded cooperative task by itself does not relocate the reward criterion into programs. Donation mnemonics are not interchangeable: `donate-facing` uses energy, `donate-rnd` ordinary merit. |
| Neighbor-dependent task rewards | `cTaskLib::Task_CommEcho/Task_CommNot` 3216–3249; environment `REACTION` entries for `comm_echo`/`comm_not`; ordinary heads-26 `IO` can trigger checking. | C++ compares caller output to neighbors’ stored inputs, equal or complemented. This does not expose those buffers to executable registers. No registered task using `REQ_NEIGHBOR_OUTPUT` was found. |
| Public-good flags and reaction products | Extended heads `display-lyse`, `check-lyse`, `sense-autoinducer`, `lyse`; `Inst_CheckLyse/Inst_SenseAI` 3681–3776. Task names `ai-display-cost`, `produce-public-good`, `consume-public-good`, `exploded*`; configured reaction payoff/product/lethality, `KABOOM_PROB` for `lyse`. | `check-lyse` returns a display count for program arithmetic. C++ embeds the threshold in `sense-autoinducer` and consumption, which randomly clears a producer flag. Zero reward does not disable that side effect. `lyse` alone does not remove the caller. Resource byproducts and `deme` payoff affect others through environment rules. |
| Environmental signals and communal energy | Extended heads cell marks/readers, pheromone operations and energy-relinquishment instructions; `cHardwareCPU` 4071–4119,8380–9260; `PHEROMONE_ENABLED`, drop/amount settings; `FRAC_ENERGY_RELINQUISH` and energy initialization. | Programs can leave values/resources or relinquish energy to neighbors/demes. Other programs can respond through sensors and logic; the configured distribution itself supplies no candidate correctness test. |
| Quorum, explosions, group killing and self-removal | Extended heads `sense-quorum`, `smart-explode`, `explode*`, `coop-SA`, `agg-SA`, `kill-group-member`, `suicide`; `KABOOM_*`, quorum noise and group/protection settings. | Programs can compute triggers or adjustable thresholds. C++ determines affected neighbors by distance/identity, or picks a random group member. Self-removal is not assessment of another candidate without an additional information path. |
| Changes to other programs and germline participation | Extended heads `point-mut-rand`, `point-mut-gs`, `join-germline`, `exit-germline`, `donate-res-to-deme`; `INST_POINT_MUT_PROB` and relevant deme settings. | Programs request instruction changes or affect participation; target scanning and random changes are supplied operations. `repair-on/off` names do not supply a demonstrated copy-error checking and reconstruction procedure. |

**Checked:** Active hardware factory cases are heads 0, TransSMT 2, Experimental 3, GP8 4 and BCR 5. Bundled SMT type 1 has no factory case here; old GX/heads-parasite files are not evidence of runnable support. The default hardware help text is incomplete. Sex also has TransSMT `Divide-Sex*` and Experimental `h-divide-sex` routes; preference setters are in heads hardware. Optional `rotate-l/r` labels inspect neighbors’ instruction labels, and `get-faced-edit-dist` exposes a supplied sequence-distance calculation.

**Checked:** Several apparent controls are unsuitable. HGT's advertised fragment shuffle reaches an assertion/commented-out implementation. `PrintSuccessfulMates` has its recording call commented out. `PrintFemaleMatePreferenceData` allocates four counters although preference enums include 4–6. `PREY_MUT_OFF` is not a generic evaluator freeze. `PRED_PREY_SWITCH -1` does not disable every attack variant. Random mating, sensor noise and random register values do not preserve and permute a decision record. `ALT_BENEFIT`, `REPUTATION_REWARD` and `DONATION_RESTRICTIONS` have declarations but no traced consumers; they are not active payoff controls.

## Experiments

### Shared question and apparatus

The frozen question is: **can an inherited instruction sequence transform information from a candidate into a consequential decision about it, and can instruction changes alter that transformation?** Inventory, changing evaluators, stock execution and the three controls are given jobs. The staged causal encounter is an added measurement choice. Testing open-ended learning, elimination of all environment rules, or candidate correctness would change the question.

The appendix supplies every file through one literal file-writing script, plus snapshot extraction and execution commands. It creates two experiments, each with a continuous evolutionary run and three small assay conditions. Proposed full runs use seeds 101, 102 and 103, a 60×60 population, 5,000 updates, copy-change probability 0.0075, and snapshots every 1,000 updates. There are no task rewards and no save/reload interruptions during these runs.

**Checked, implementation:** A custom heads set retains a protected scaffold and a five-instruction arithmetic region. `NO_MUT_INSTS` protects scaffold opcode symbols from `repro` copy substitutions; zero instruction redundancy prevents mutations into the scaffold. Only `inc`, `dec`, `add`, `sub`, and `nand` have positive mutation weight. Other mutation routes, including the earlier runs' division insertions/deletions, are zero. The stock default ancestor cannot perform this protocol. The supplied ancestor uses stock `repro`; its replication operation is supplied by the virtual CPU, not an evolved copy loop. The appendix also supplies two eight-instruction kernels, matching the platform minimum length (`Definitions.h:28`); both reproduced in separate 100-cell, 100-update smoke runs. The tested control fixtures are 40/41 instructions because they include the mutable region and timing padding.

**Proposed:** This restriction keeps the interpretation and assay timing intact. It allows the predicate to change but fixes cue production, sensing, conditional branch, donation size and reproduction. It is a deliberately bounded experiment, not a continuation of the earlier 26-instruction experiments.

**Checked, implementation:** Evolution uses merit-dependent scheduling. Assays use four programs in two isolated two-cell demes, round-robin scheduling, one execution per update, no speculative execution, no mutation and no replication before measurement. Candidates have padded self-replicating sequences; the assay stops before their replication instructions. Energy is supplied on injection/birth, energy transfer on cell replacement is zero, and the conversion-to-merit divisor is positive. A 0.5 birth decay bounds the source-defined parent recurrence near E_next = 0.5E + 1000; without it the parent gains energy on every division. This was a development correction to the rig, before running the canonical files. These choices must stay fixed across each matched assay.

### Received-number experiment

**Proposed:** Every evolving program both publishes 1 and acts as an evaluator. It reads a neighbor's published number, runs five arithmetic instructions, and donates 10 energy units if the result is zero. The initial arithmetic is `inc; dec; inc; dec; dec`, hence input minus one. This initially accepts 1 and rejects 0 and 2. Mutation can change the computed predicate; selection can change sequence frequencies. Whether any such change is useful is an experimental question, not an assumed outcome.

**Checked:** Scalar receive rotates through neighboring connections, reads the first active sender and leaves it faced. Each evaluator accepts or refuses its one neighbor; it does not compare two candidates in one execution. The two-cell encounter removes ambiguity over which program supplied the cue. Continuous populations can replace a sender between the read and donation; their aggregate sharing statistics alone cannot identify a decision about that same candidate.

**Proposed controls:** The frozen-evaluator condition saves the update-1,000 instruction-sequence bank and its weights, then reuses those exact sequences in fresh encounters. Compare it with update-5,000 evaluators on the identical candidate panel. This freezes inherited programs and their analysis weights, not CPU memory or the evolving population's later abundance distribution. A separate candidate-bank comparison may be added only as a labeled new test.

The shuffled condition exchanges candidate programs between the two target cells after both evaluators have consumed the cues and finished their arithmetic, before the conditional transfer. It preserves evaluator instructions, register values, donor positions, available energy and transfer opportunities. Across repeated paired encounters, use an equal number of identity and exchange mappings. The provided exchange file is the nonidentity member of that exact two-recipient permutation control. Do not interpret a swap of inputs before reading as this control.

The off condition retains sensing/arithmetic but sets `ENERGY_SHARING_METHOD 0`. **Checked:** the chosen `donate-energy-faced10` requires either push mode or an open request. No program in these files opens a request, so no energy is deducted or received. This switches off the consequential donation path while retaining the evaluator's decision computation.

**Proposed measurement:** Identify candidates by ID, not their cells after the swap. Inspect input, arithmetic and branch/action traces in the founder and changed-arithmetic encounters. The bank runner records cue settings and ID-matched energy changes; it does not emit individual CPU traces for every replayed evaluator. For the initial evaluator, the unshuffled panel should give candidate 1 exactly +10 and candidate 0 no gain; the exchanged panel should give candidate 0 +10 and candidate 1 no gain. Donor energy loss and total transferred energy should be the same. Off should give neither candidate a gain. Candidate 2 is a further rejection case. The bank uses the fixed pairs (0,1), (0,2) and (1,2), with balanced recipient permutations.

**Result against an added contribution:** If cue changes do not change decisions, changing the arithmetic does not change the cue-to-decision map, or correctly mapped support is indistinguishable from the permutation control on the prespecified outcome, the corresponding claim fails. Evolutionary disappearance of transfers or of discrimination counts against useful maintenance in this ecology. A difference in sequence abundance alone does not count as learning. Report cue-response vectors and distinguish always-give and never-give policies; avoiding donation can increase replication without adding useful discrimination.

### Displayed-reputation experiment

**Proposed:** Use the same arithmetic and transfer architecture, replacing scalar communication with a direct read of the neighbor's reputation. The starting evolving program uses `pose` once before reading. In the controlled panel one candidate poses once; the other does not. The initial evaluator accepts reputation 1 and rejects 0; a twice-posing candidate supplies value 2 for the rejection check.

**Checked:** `pose` increments reputation without requiring a donation. The sensor defaults to AX, so the supplied `nop-B` directs its result into BX for the arithmetic. That modifier is consumed by the sensor rather than receiving a separate execution. `AUTO_REPUTATION 0`, `INHERIT_REPUTATION 0`, `INHERIT_OPINION 0` and an opinion buffer of one prevent automatic/inherited reputation and reset parent opinion on replication. A missing neighbor leaves the destination register unchanged; the paired assay requires both candidates present.

**Proposed:** The same frozen update-1,000 bank, post-arithmetic recipient permutation and sharing-off controls apply. Read candidate reputation before the exchange and attribute the later energy change to the candidate ID that actually occupies the recipient cell. The expected initial energy table is the same as for received numbers. A pose-free candidate is the no-action case. Exchange cue identities while retaining the rest of candidate behavior to test whether the evaluator responds merely to the display.

**Result against an added contribution:** If an undisclosed donation or inheritance route determines the reputation, the intended cue manipulation has not been isolated. If moving or falsifying the display preserves the same selection pattern while actual candidate contribution changes, the program is selecting a display, not assessing contribution. The experiment can reveal that distinction; it cannot turn reputation into a measure of computational correctness by definition.

### Hard-to-vary assessment and cost

| Part and origin | Mark and discriminating change |
|---|---|
| Pinned stock version and no source edits; owner constraints | **Fixed.** Tested scope, not an argument that these are necessary to learning. |
| Candidate information entering executable arithmetic; built design | **Held within the tested encounters.** Changing the cue changed transfers; changing one arithmetic instruction changed which cue received support. |
| Transfer affecting the candidate; built design | **Held within the tested encounters.** Gains appeared with the operation active and disappeared with sharing off; ID records distinguished recipients. |
| Scalar values versus reputation; stock routes | **Two routes** to readable candidate information. Neither alone is necessary for this limited job. |
| Five arithmetic instructions, cue 1, 10 energy units; design conventions | **Loose.** Other bounded arithmetic regions, cue values or positive transfers can do the same job. No explanatory necessity is claimed. |
| Protected scaffold and synchronized encounters; built rig | **Held if** exact timing is required for this permutation design. An asynchronous event-level recorder would be another rig, not the same claim. |
| Energy conversion and computational selection; inherited platform | **Borrowed.** Fixed environment operations give the program's choice its consequence. |
| Progressive usefulness or new knowledge | **Unknown.** Neither a hand-written starting test nor evolving a cue preference settles it. |

The consequential rival is indiscriminate support: it may cause similar population changes without assessing candidates. The permutation condition preserves immediate support totals while removing recipient matching. A flip from accepting 1 to accepting 0 must produce a changed decision table, not be retold as the same successful explanation. The built-in energy allocator and the executable predicate jointly cause the outcome; this is not a claim that computational selection disappeared.

The main tension is between unrestricted evaluator changes and a precisely timed control. Protecting the scaffold sacrifices changes to sensing, action and replication. Removing protection requires a new asynchronous assay; it must not inherit the present timing claim. A second tension is that fixed cues isolate the mechanism while saying little about newly useful problems. No catch-all “learning” category is used: report cue-conditioned decisions and transfers, with broader claims left open.

**Cost estimate, not measured on Claude's machine:** Using the brief's one CPU-hour per 50,000 updates only as a scaling assumption, six 5,000-update runs total 0.6 CPU-hours. Interaction overhead and the altered instruction set can change that. Time one 1,000-update run per design, then estimate total process CPU time as six times the measured 5,000-update equivalent, plus assay startup time. At most three Avida processes run concurrently. All living sequences from a snapshot are batched into one world per condition: 24N programs for N sequences, with 18 update executions before the final events. Two designs × three seeds × two banks × three conditions require 36 assay launches. Include their measured CPU time; no per-sequence startup is required. Stop the 5,000-update pilot as specified before deciding whether a 50,000-update extension answers a remaining question. The latter is about 6 CPU-hours on the original scaling assumption.

### Local execution receipts

**Checked, measured here:** Unmodified stock source compiled with GCC 13 and CMake. For both mechanisms, the founder active encounter ended with energies `[990,1010,1000,1000]` in cells 0–3 and IDs `[0,1,2,3]`. After recipient exchange the energy grid was identical but IDs were `[0,3,2,1]`: candidate 0 received the transfer. Off ended with four energies of 1000. Replacing candidate 1 with candidate 2 produced no transfers. Changing the evaluator's final arithmetic instruction from `dec` to `sub` produced `[1000,1000,990,1010]`, selecting cue 0 instead. These added refusal and altered-circuit cases were chosen during development.

**Checked, measured here:** Two 100-update population smoke runs ended with 3,600 programs each. Their saved banks contained 198 and 190 living instruction sequences. Replaying every living sequence across cues 0, 1 and 2 produced five observed response patterns: reject all, accept only 0, accept only 1, accept only 2, and accept all. All six bank conditions completed with stable identities, transfers of 0 or 10, conserved transfer totals, and zero cue contrast after balanced permutation or switching off. This demonstrates changed inherited response rules in this restricted family, not added usefulness. Process CPU times for the two population runs were 14.41 and 13.18 seconds here, not measurements of Claude's machine.

**Checked, development corrections:** Initial predictions did not all survive the first rig. The following failures were retained, then rerun after the indicated change. Source code was not patched.

| First result | Layer changed and correction | What the corrected result covers |
|---|---|---|
| All six initial launches: `error: no instruction sets defined` | Rig: modern instruction declarations require `#include INST_SET=instset.cfg`. | Both mechanisms then loaded; no claim about the failed launches executing programs. |
| Scalar transfers absent; reputation runs exited 139 at the first peer read | Rig: a degenerate bounded 2×1 grid removed its peer links. Use a two-cell clique within each deme. | Both mechanisms produced the stated identity-matched transfers; the topology claim is specific to these files. |
| `SavePopulation assay.spop` and `InjectAll ancestor.org` reported unrecognized arguments; the latter yielded an empty population despite exit 0 | Rig: use `filename=...` for these named-argument events; reject error logs, empty populations and missing final updates in the runner. | Subsequent population runs completed and snapshots loaded. |
| Snapshot reader rejected short extinct historical records | Analysis preparation: inspect living count before requiring complete placement fields; retain all living sequences and census weights. | Both actual snapshots replayed; no sequence was selected by Avida fitness. |

## If source changes are needed

**Checked, bounded conclusion:** The proposed cue-to-decision-to-energy experiments use stock instructions and events. Required C++ change: **0 added lines, 0 removed lines**; no unified diff is applicable. This does not claim that stock Avida already supplies the earlier reviewer's complete B2, B3 or C designs.

A universal candidate-execution service, evaluators inventing unrestricted tests, a live event-level decision shuffle, and exact CPU-state checkpoint branching were not implemented here. Their absence from this report is not a statement that no stock composition could provide them. Adding a diff for a different experiment would silently change the requested fallback condition.

## Source locations checked

**Checked:** All following locations were read in the pinned checkout. Line ranges identify the relevant implementations; they are not claims that every intervening line was tested. Links resolve the same commit.

| Source | Checked locations |
|---|---|
| [Heads CPU](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/cpu/cHardwareCPU.cc) | Registration tables; `Inst_Repro` 3363–3425; scalar send/receive 4261–4276; energy donation 4890–4998 and 5958–5976; sex 7019–7050; direct attacks 9527–9620; reputation 9884–10100; social/network/mutation/mating families 10241–11035. |
| [Population](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cPopulation.cc) | Deme topology 359–423; inheritance 727–785; parasites 1032–1345; group killing 2169–2182; explosions 2351–2477; `SwapCells` 2483–2513; deme competition/replication 2515–3204; spawning 4497–4534; scheduler 7450–7474. |
| [Population interface](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cPopulationInterface.cc) | `ReceiveValue` 481–498; parasite request 502–507; network routing 887–963; HGT 1037–1222. |
| [Birth chamber](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cBirthChamber.cc) | Handler precedence 45–86; entry storage 135–156; recombination 286–312; submission 443–583. Related `cBirthMateSelectHandler.cc` 33–56, `cBirthDemeHandler.cc` 33–62, `cBirthMatingTypeGlobalHandler.cc` 231–382. |
| [Configuration declarations](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/main/cAvidaConfig.h) | Mutation/reproduction settings; sex 419–439; parasites 441–465; demes 481–524; scheduler 549; protection 593; energy 653–682; social/predator/network settings 791–838; instruction loading 885–887. |
| [Population actions](https://github.com/devosoft/avida/blob/47f13dadb547fcf10f620ace60247f38b30b8b16/avida-core/source/actions/PopulationActions.cc) | Injection/traces 86–140; mutation events 1999–2148; competition/replication events 2398–3924; `SwapCells` 4533–4563. `PrintActions.cc`: energy grids 3327–3358, mate-preference counters 5322–5327. |
| Other local files, checked | `cHardwareManager.cc` 48–149,245–278; `cInstSet.cc` 83–87,150–235; `cHardwareBase.cc` mutation routes; `cHardwareTransSMT.cc` 62–113,223–253,648–736,1657–1673; `cHardwareExperimental.cc` 3005–3013,4055–4092,5407–5426,5645–5680,6658–6690,6940–7143; GP8/BCR registration/factory interfaces; `cTaskLib.cc` 287–290,3216–3249,4025–4097; `cEnvironment.cc` 1336–1394,1824–1854; `cOrganism.cc` 653–655,1403–1418; `cTopology.h` 64–111; `cPhenotype.cc` 2061–2087,2403–2410; `cPopulationCell.cc` 262–306; `Avida2Driver.cc` 91–119; Apto `RoundRobin.cc` 36–51; stock heads/config/ancestor files. |

## Assumptions and what you are unsure of

**Checked, supplied brief only:** The earlier replication, circuit, ablation and task counts were read as reported results. Their populations and raw measurements were not supplied here and were not independently remeasured. Constructor-theoretic knowledge is the owner's framing; no claim about that literature is needed for this report's executable test.

**Checked source versus inference:** Source inspection identifies which code paths the proposed setup calls; runtime receipts are reported separately. An unrun prediction is not a result. Failure can belong to the proposed mechanism, the timing/configuration rig or candidate preparation. Preserve the first output before correcting any of those layers.

The candidate cases and starting programs were prepared here, with knowledge of the intended decision rule. They are development cases, not independent evidence of generalization. A snapshot assay deliberately resets execution state equally across conditions; it must not be described as preserving the full state of the continuous run. Fresh snapshot testing addresses inherited evaluator code only.

A source-family census cannot guarantee exhaustive behavior of thousands of variants and settings. Absences above are bounded to the searched registration tables, factory cases and named paths. The source review does not support treating all cooperative, mating or parasitic interactions as cognition.

The next step is the specified 5,000-update, three-seed run and update-1,000 versus update-5,000 bank comparison. The local development encounters already exercised the cue/arithmetic/ID/energy distinctions and zero-action cases; they do not settle long-run maintenance or utility. Hard-to-vary criticism constrains what this experiment can show; it does not turn a small causal demonstration into an account of knowledge creation.

## Appendix

The following self-contained Python 3 file contains the complete configuration, instruction-set and ancestor definitions, including every mutation setting used. Omitted Avida settings take the defaults of the pinned commit. It creates `stock_avida_evaluation` beside itself and refuses an existing destination. No source files are changed. `minimal.org` contains each compact eight-instruction kernel; the experiments use the longer, protected, padded `ancestor.org` so that the transfer can be interrupted at a known time.

Save the code as `make_experiments.py`, run it, then run the generated suite with the absolute path to the compiled Avida executable. The suite uses seeds 101–103, at most three Avida processes, fresh output directories, all living snapshot sequences, and the update-1,000 frozen reference. It rejects error messages and empty populations even when Avida returns exit code zero. The 5,000-update suite has not been run here.

```bash
python3 make_experiments.py
python3 stock_avida_evaluation/run_suite.py --avida /absolute/path/to/avida --output results_5000
```

To inspect a single founder encounter first, run Avida with `-c avida.cfg` from `stock_avida_evaluation/scalar/assay` or the corresponding `reputation/assay` directory. Its `data` directory contains full instruction traces and energy/ID grids. `shuffle` supplies the exchange encounter, and `off` disables transfers. The complete bank runner includes both identity and exchange permutations.

```python
from pathlib import Path
root=Path(__file__).resolve().parent/'stock_avida_evaluation'
root.mkdir(exist_ok=False)
instructions=['nop-A','nop-B','nop-C','nop-X','one','zero','send','receive','pose','get-neighbors-reputation','rotate-to-next-occupied-cell','if-equ-0','donate-energy-faced10','repro','inc','dec','add','sub','nand']
mutable=set(instructions[14:])
inst='INSTSET evaluator:hw_type=0\n'+'\n'.join(f'INST {x}:redundancy={int(x in mutable)}:cost=1:energy_cost=0' for x in instructions)+'\n'
common='''VERSION_ID 2.14.0
RANDOM_SEED 101
SPECULATIVE 0
#include INST_SET=instset.cfg
INST_SET -
INST_SET_LOAD_LEGACY 0
ENVIRONMENT_FILE environment.cfg
EVENT_FILE events.cfg
ANALYZE_FILE analyze.cfg
DATA_DIR data
MUT_RATE_SOURCE 1
COPY_MUT_PROB 0.0075
COPY_INS_PROB 0
COPY_DEL_PROB 0
COPY_UNIFORM_PROB 0
COPY_SLIP_PROB 0
DIV_MUT_PROB 0
DIV_INS_PROB 0
DIV_DEL_PROB 0
DIV_UNIFORM_PROB 0
DIV_SLIP_PROB 0
DIVIDE_MUT_PROB 0
DIVIDE_INS_PROB 0
DIVIDE_DEL_PROB 0
DIVIDE_UNIFORM_PROB 0
DIVIDE_SLIP_PROB 0
PARENT_MUT_PROB 0
PARENT_INS_PROB 0
PARENT_DEL_PROB 0
POINT_MUT_PROB 0
POINT_INS_PROB 0
POINT_DEL_PROB 0
INJECT_MUT_PROB 0
INJECT_INS_PROB 0
INJECT_DEL_PROB 0
META_COPY_MUT 0
INST_POINT_MUT_PROB 0
NO_MUT_INSTS abcdefghijklmn
DIVIDE_METHOD 1
MIN_EXE_LINES 0.5
MIN_COPIED_LINES 0.5
DEATH_METHOD 0
PREFER_EMPTY 0
REPRO_METHOD 1
ENERGY_ENABLED 1
ENERGY_GIVEN_ON_INJECT 1000
ENERGY_GIVEN_AT_BIRTH 1000
FRAC_PARENT_ENERGY_GIVEN_TO_ORG_AT_BIRTH 0
FRAC_PARENT_ENERGY_GIVEN_TO_DEME_AT_BIRTH 0
FRAC_ENERGY_DECAY_AT_ORG_BIRTH 0.5
FRAC_ENERGY_TRANSFER 0
NUM_CYCLES_EXC_BEFORE_0_ENERGY 1000
ENERGY_CAP -1
FIX_METABOLIC_RATE -1
ENERGY_SHARING_METHOD 1
ENERGY_SHARING_UPDATE_METABOLIC 1
RESOURCE_SHARING_LOSS 0
AUTO_REPUTATION 0
INHERIT_REPUTATION 0
INHERIT_OPINION 0
OPINION_BUFFER_SIZE 1
'''
# Four prefix executions, five mutable arithmetic executions, four idle executions,
# then branch/action. nop-B on the direct sensor is consumed by that instruction.
for mechanism in ('scalar','reputation'):
    base=root/mechanism
    base.mkdir(exist_ok=True)
    prefix=['one','send','nop-X','receive'] if mechanism=='scalar' else ['one','pose','nop-X','get-neighbors-reputation','nop-B']
    sequence=prefix+['inc','dec','inc','dec','dec']+['nop-X']*4+['if-equ-0','donate-energy-faced10']+['nop-X']*24+['repro']
    ancestor='#inst_set evaluator\n'+'\n'.join(sequence)+'\n'
    for mode in ('evolution','assay','shuffle','off'):
        d=base/mode; d.mkdir(exist_ok=True)
        (d/'instset.cfg').write_text(inst)
        (d/'ancestor.org').write_text(ancestor)
        (d/'environment.cfg').write_text('# No tasks, reactions, or task rewards. Energy supplied at injection and birth.\n')
        (d/'analyze.cfg').write_text('# Intentionally empty; run in normal simulation mode.\n')
        cfg=common
        if mode=='evolution':
            cfg+='WORLD_X 60\nWORLD_Y 60\nWORLD_GEOMETRY 2\nNUM_DEMES 1\nBIRTH_METHOD 0\nSLICING_METHOD 2\nAVE_TIME_SLICE 30\n'
            events='''u begin InjectAll filename=ancestor.org
u 0:100:end PrintAverageData
u 0:100:end PrintCountData
u 0:100:end PrintDemeEnergySharingStats
u 0:1000:end SavePopulation filename=detail
u 0:1000:end DumpEnergyGrid
u 5000 Exit
'''
        else:
            cfg=cfg.replace('COPY_MUT_PROB 0.0075','COPY_MUT_PROB 0')
            if mode=='off': cfg=cfg.replace('ENERGY_SHARING_METHOD 1','ENERGY_SHARING_METHOD 0')
            cfg+='WORLD_X 2\nWORLD_Y 2\nWORLD_GEOMETRY 3\nNUM_DEMES 2\nBIRTH_METHOD 12\nSLICING_METHOD 0\nAVE_TIME_SLICE 1\n'
            for cue in (0,1,2):
                if mechanism=='scalar':
                    tx=['zero' if cue==0 else 'one','nop-X','send'] if cue<2 else ['one','inc','send']
                else:
                    tx=['nop-X','pose' if cue else 'nop-X','pose' if cue==2 else 'nop-X']
                tx+=['nop-X']*60+['repro']
                (d/f'candidate{cue}.org').write_text('#inst_set evaluator\n'+'\n'.join(tx)+'\n')
            events='''u begin Inject ancestor.org 0 -1 10 0 evaluator0.trace
u begin Inject candidate1.org 1 -1 21 0 candidate1.trace
u begin Inject ancestor.org 2 -1 10 0 evaluator2.trace
u begin Inject candidate0.org 3 -1 20 0 candidate0.trace
u 12 DumpEnergyGrid energy_before.dat
u 12 DumpIDGrid ids_before.dat
'''
            if mode=='shuffle': events+='u 12 SwapCells 1 3\n'
            events+='''u 17 DumpEnergyGrid energy_after.dat
u 17 DumpIDGrid ids_after.dat
u 17 PrintDemeEnergySharingStats
u 17 SavePopulation filename=assay
u 17 Exit
'''
        (d/'avida.cfg').write_text(cfg)
        (d/'events.cfg').write_text(events)

(root/'prepare_bank.py').write_text(r'''#!/usr/bin/env python3
"""Make fresh, matched stock-Avida assays of every living sequence in a snapshot.
Usage: python prepare_bank.py SNAPSHOT SCALAR_OR_REPUTATION OUTPUT_DIR [PERMUTATION_SEED]
No fitness-based selection. Census counts are preserved as analysis weights.
"""
from pathlib import Path
import csv
import json
import random
import shutil
import sys

snapshot, mechanism, output = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
assert mechanism in ('scalar', 'reputation')
seed = int(sys.argv[4]) if len(sys.argv) > 4 else 701
source = Path(__file__).resolve().parent / mechanism
header = None
records = []
for line in snapshot.read_text().splitlines():
    if line.startswith('#format '):
        header = line.split()[1:]
    elif line.strip() and not line.startswith('#'):
        assert header is not None, 'Missing #format header'
        values = line.split()
        assert len(values) > header.index('num_units'), 'Missing population count'
        row = dict(zip(header, values))
        if int(row['num_units']) > 0:
            assert len(values) == len(header), 'Unexpected living-record fields'
            assert row['hw_type'] == '0' and row['inst_set'] == 'evaluator'
            records.append(row)
assert records, 'No living sequences found'
records.sort(key=lambda x: x['sequence'])
assert len({r['sequence'] for r in records}) == len(records), 'Duplicate sequence records; combine counts explicitly'
mnemonics = [s.split()[1].split(':')[0] for s in (source/'assay'/'instset.cfg').read_text().splitlines() if s.startswith('INST ')]
alphabet = 'abcdefghijklmnopqrstuvwxyz'
assert len(mnemonics) <= len(alphabet)
decode = dict(zip(alphabet, mnemonics))
reference = [s for s in (source/'assay'/'ancestor.org').read_text().splitlines() if s and not s.startswith('#')]
core_start = 4 if mechanism == 'scalar' else 5
mutable = {'inc', 'dec', 'add', 'sub', 'nand'}
for row in records:
    row['instructions'] = [decode[c] for c in row['sequence']]
    assert len(row['instructions']) == len(reference), 'Genome length changed'
    for i, (actual, expected) in enumerate(zip(row['instructions'], reference)):
        assert actual in mutable if core_start <= i < core_start+5 else actual == expected, 'Protected scaffold changed'

# Cases fixed before reading any outcomes. Every sequence receives every pair.
# For each pair, identity and swap are both run: this is the exact finite
# distribution of all recipient permutations for a two-recipient panel.
pairs = [(0, 1), (0, 2), (1, 2)]
panels = [(row, pair, side) for row in records for pair in pairs for side in (0, 1)]
# Paired complementary permutations preserve equal identity/swap coverage, while
# a predeclared seed determines which duplicate panel gets which permutation.
rng = random.Random(seed)
flips = {(row['id'], pair): rng.randrange(2) for row in records for pair in pairs}
output.mkdir(parents=True, exist_ok=True)
metadata=[]
for i,(row,pair,side) in enumerate(panels):
    start=4*i
    metadata.append(dict(panel=i, sequence=row['sequence'], id=row['id'], weight=int(row['num_units']),
                         cue_left=pair[0], cue_right=pair[1], evaluator_left=start,
                         candidate_left=start+1, evaluator_right=start+2, candidate_right=start+3,
                         swap=(side ^ flips[(row['id'], pair)])))
(output/'panels.json').write_text(json.dumps(metadata, indent=2)+'\n')
(output/'provenance.json').write_text(json.dumps(dict(snapshot=str(snapshot.resolve()), mechanism=mechanism,
    permutation_seed=seed, frozen_weights='num_units at snapshot', programs=len(records),
    panel_pairs=pairs, fresh_initialization=True), indent=2)+'\n')
for arm in ('active','shuffled','off'):
    d=output/arm
    d.mkdir(exist_ok=True)
    for filename in ('instset.cfg','environment.cfg','analyze.cfg','candidate0.org','candidate1.org','candidate2.org'):
        shutil.copyfile(source/'assay'/filename,d/filename)
    config=(source/('off' if arm=='off' else 'assay')/'avida.cfg').read_text()
    config=config.replace('WORLD_Y 2\n', f'WORLD_Y {2*len(panels)}\n')
    config=config.replace('NUM_DEMES 2\n', f'NUM_DEMES {2*len(panels)}\n')
    (d/'avida.cfg').write_text(config)
    events=[]
    for row in records:
        (d/f"evaluator_{row['id']}.org").write_text('#inst_set evaluator\n'+'\n'.join(row['instructions'])+'\n')
    for meta in metadata:
        for label in ('left','right'):
            events.append(f"u begin Inject evaluator_{meta['id']}.org {meta['evaluator_'+label]} -1 10")
            events.append(f"u begin Inject candidate{meta['cue_'+label]}.org {meta['candidate_'+label]} -1 {20+meta['cue_'+label]}")
    events+=['u 12 DumpEnergyGrid energy_before.dat','u 12 DumpIDGrid ids_before.dat']
    if arm=='shuffled':
        events += [f"u 12 SwapCells {m['candidate_left']} {m['candidate_right']}" for m in metadata if m['swap']]
    events+=['u 17 DumpEnergyGrid energy_after.dat','u 17 DumpIDGrid ids_after.dat',
             'u 17 PrintDemeEnergySharingStats','u 17 Exit']
    (d/'events.cfg').write_text('\n'.join(events)+'\n')
print(f'Prepared {len(records)} sequences, {len(panels)} panels, 3 arms in {output}')
''')

(root/'summarize_bank.py').write_text(r'''#!/usr/bin/env python3
"""Read prepared bank results and emit per-sequence, per-pair decision contrasts.
Usage: python summarize_bank.py BANK_DIR
No Avida runs are started by this script.
"""
from pathlib import Path
from collections import defaultdict
import csv
import json
import sys
root=Path(sys.argv[1])
metadata=json.loads((root/'panels.json').read_text())
def grid(path, cast=float):
    return [cast(x) for x in path.read_text().split()]
rows=[]
for arm in ('active','shuffled','off'):
    d=root/arm/'data'
    before=grid(d/'energy_before.dat')
    after=grid(d/'energy_after.dat')
    ids0=grid(d/'ids_before.dat',int)
    ids1=grid(d/'ids_after.dat',int)
    assert len(ids1)==len(set(ids1)), 'Missing or duplicated program identity'
    current={x:i for i,x in enumerate(ids1)}
    assert set(ids0)==set(ids1), 'Program identities changed during assay'
    for meta in metadata:
        gain={}
        donor_loss=0
        for side in ('left','right'):
            loc=meta['candidate_'+side]
            gain[side]=after[current[ids0[loc]]]-before[loc]
            eloc=meta['evaluator_'+side]
            donor_loss+=before[eloc]-after[current[ids0[eloc]]]
        assert abs(sum(gain.values())-donor_loss)<1e-8, 'Unmatched transfers'
        assert all(min(abs(v),abs(v-10))<1e-8 for v in gain.values()), 'Unexpected transfer amount'
        rows.append(dict(arm=arm, genotype_id=meta['id'], sequence=meta['sequence'],
            weight=meta['weight'], panel=meta['panel'], cue_left=meta['cue_left'],
            cue_right=meta['cue_right'], grant_left=gain['left'], grant_right=gain['right'],
            contrast=gain['right']-gain['left']))
with (root/'panels.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
groups=defaultdict(list)
for row in rows:
    groups[(row['arm'],row['genotype_id'],row['cue_left'],row['cue_right'])].append(row)
summary=[]
for (arm,genotype_id,left,right),members in sorted(groups.items()):
    assert len(members)==2
    summary.append(dict(arm=arm,genotype_id=genotype_id,weight=members[0]['weight'],
        cue_left=left,cue_right=right,grant_left=sum(r['grant_left'] for r in members)/2,
        grant_right=sum(r['grant_right'] for r in members)/2,
        contrast=sum(r['contrast'] for r in members)/2))
for row in summary:
    if row['arm'] in ('shuffled','off'):
        assert abs(row['contrast'])<1e-8, 'Recipient-permutation/off control has a cue-dependent contrast'
with (root/'contrasts.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(summary[0]));writer.writeheader();writer.writerows(summary)
aggregate=defaultdict(list)
for row in summary:
    aggregate[(row['arm'],row['cue_left'],row['cue_right'])].append(row)
weighted=[]
for (arm,left,right),members in sorted(aggregate.items()):
    total=sum(r['weight'] for r in members)
    weighted.append(dict(arm=arm,cue_left=left,cue_right=right,census_weight=total,
        grant_left=sum(r['weight']*r['grant_left'] for r in members)/total,
        grant_right=sum(r['weight']*r['grant_right'] for r in members)/total,
        contrast=sum(r['weight']*r['contrast'] for r in members)/total))
with (root/'weighted_contrasts.csv').open('w',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(weighted[0]));writer.writeheader();writer.writerows(weighted)
print(f'Read {len(rows)} panels; wrote panels.csv, contrasts.csv, weighted_contrasts.csv.')
''')

(root/'run_suite.py').write_text(r'''#!/usr/bin/env python3
"""Run the proposed continuous evolution and matched stock-Avida bank assays.
Usage: python run_suite.py --avida /absolute/path/to/avida --output results
Defaults: 2 mechanisms, seeds 101/102/103, 5000 updates, at most 3 processes.
This file is supplied for future execution; preparing it starts no runs.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import json
import re
import shutil
import subprocess
import sys
import time

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--avida',type=Path,required=True)
parser.add_argument('--output',type=Path,required=True)
parser.add_argument('--updates',type=int,default=5000)
parser.add_argument('--seeds',type=int,nargs='+',default=[101,102,103])
parser.add_argument('--processes',type=int,choices=[1,2,3],default=3)
args=parser.parse_args()
assert args.updates >= 1000 and args.updates % 1000 == 0
avida=args.avida.resolve();out=args.output.resolve()
assert avida.is_file()
assert not out.exists(), 'Use a new output directory; preserve previous results'
out.mkdir(parents=True)
source=Path(__file__).resolve().parent
jobs=[]
for mechanism in ('scalar','reputation'):
    template=source/mechanism/'evolution'
    for seed in args.seeds:
        d=out/mechanism/f'seed-{seed}'/'evolution';d.mkdir(parents=True)
        for filename in ('avida.cfg','events.cfg','environment.cfg','instset.cfg','ancestor.org','analyze.cfg'):
            shutil.copyfile(template/filename,d/filename)
        config=(d/'avida.cfg').read_text().replace('RANDOM_SEED 101\n',f'RANDOM_SEED {seed}\n')
        (d/'avida.cfg').write_text(config)
        events=(d/'events.cfg').read_text().replace('u 5000 Exit',f'u {args.updates} Exit')
        (d/'events.cfg').write_text(events)
        jobs.append((mechanism,seed,d))

# Each timing wrapper has exactly one Avida child. This avoids mixing CPU
# measurements from concurrently running children of the threaded runner.
timed_driver = """
import json, resource, subprocess, sys
from pathlib import Path
p = subprocess.run(sys.argv[1:])
u = resource.getrusage(resource.RUSAGE_CHILDREN)
Path('cpu_time.json').write_text(json.dumps(dict(exit_code=p.returncode,
    user_seconds=u.ru_utime, system_seconds=u.ru_stime,
    cpu_seconds=u.ru_utime+u.ru_stime)))
raise SystemExit(p.returncode)
"""

def run(d):
    t=time.monotonic()
    with (d/'run.log').open('w') as logfile:
        completed=subprocess.run([sys.executable,'-c',timed_driver,str(avida),'-c','avida.cfg'],cwd=d,stdout=logfile,stderr=subprocess.STDOUT)
    logfile_text=(d/'run.log').read_text()
    log_errors=re.findall(r'(?im)^error:.*$',logfile_text)
    status=re.findall(r'UD:\s*(\d+).*?Orgs:\s*(\d+)',logfile_text)
    requested=int(re.findall(r'^u (\d+) Exit$',(d/'events.cfg').read_text(),re.M)[-1])
    reached=int(status[-1][0]) if status else None
    living=int(status[-1][1]) if status else 0
    cpu=json.loads((d/'cpu_time.json').read_text()) if (d/'cpu_time.json').exists() else {}
    result=dict(directory=str(d),exit_code=completed.returncode,wall_seconds=time.monotonic()-t,cpu=cpu,
                requested_update=requested,final_update=reached,living_programs=living,log_errors=log_errors)
    (d/'run_status.json').write_text(json.dumps(result,indent=2)+'\n')
    if completed.returncode or log_errors or reached != requested or living == 0:
        raise RuntimeError(f'Avida did not satisfy completion checks (exit {completed.returncode}); see {d / "run.log"} and run_status.json')
    return result

# Dependencies are sequential: evolution, snapshot preparation, then fresh assays.
with ThreadPoolExecutor(max_workers=args.processes) as pool:
    evolution_results=list(pool.map(run,[d for _,_,d in jobs]))
assay_jobs=[]
for mechanism,seed,d in jobs:
    for update in sorted({1000,args.updates}):
        snapshot=d/'data'/f'detail-{update}.spop'
        assert snapshot.is_file(),f'Expected stock snapshot missing: {snapshot}'
        bank=d.parent/f'bank-{update}'
        subprocess.run([sys.executable,str(source/'prepare_bank.py'),str(snapshot),mechanism,str(bank),'701'],check=True)
        assay_jobs += [bank/arm for arm in ('active','shuffled','off')]
with ThreadPoolExecutor(max_workers=args.processes) as pool:
    assay_results=list(pool.map(run,assay_jobs))
for mechanism,seed,d in jobs:
    for update in sorted({1000,args.updates}):
        subprocess.run([sys.executable,str(source/'summarize_bank.py'),str(d.parent/f'bank-{update}')],check=True)
(out/'runs.json').write_text(json.dumps(dict(evolution=evolution_results,assays=assay_results),indent=2)+'\n')
print(f'Finished {len(evolution_results)} evolution runs and {len(assay_results)} bank assays. Results: {out}')
''')

minimal = {
    'scalar': ['one','send','receive','dec','if-equ-0','donate-energy-faced10','nop-X','repro'],
    'reputation': ['one','pose','get-neighbors-reputation','nop-B','dec','if-equ-0','donate-energy-faced10','repro']
}
for mechanism, instructions in minimal.items():
    (root / mechanism / 'minimal.org').write_text('#inst_set evaluator\n' + '\n'.join(instructions) + '\n')
import hashlib, json
manifest = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(root.rglob('*')) if p.is_file()}
(root/'files.sha256.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(root)
```

END OF REPORT
