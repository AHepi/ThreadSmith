# Brief 06 for GPT 6 Astra: An independent review of the earlier reviewer's report

*Written by Claude on 30 September 2026 for the owner to hand to a fresh GPT 6 Astra agent (log S115, decision S66). Why this brief: Fresh instances are independent, which is their strength here. One can check another's work without anchoring on it. The earlier report is attached in full below the task. Paste everything below the line.*

---

# An independent review of the earlier reviewer's report

## Who this is for, and the ground rules

You are helping a research project on how new knowledge is created. The project owner is not a programmer. They test ideas by having AI models design, write and run code, and they read the results in plain language. Your answer will be read by the owner and by another AI model (Claude) that runs the experiments on a machine with Avida built and ready.

**You are a fresh instance.** You have no memory of earlier conversations and cannot see replies from other instances. Everything you need is in this brief. Several independent instances are being given different briefs at the same time, so stay within your own task.

**What the other side can do for you.** Claude has the following:
- Avida 2.14.0 compiled from github.com/devosoft/avida at commit 47f13dad, with cmake and a C++ compiler;
- 4 CPUs, running at most 3 Avida processes at once. A 50,000-update run in the standard nine-task environment takes about one hour;
- all saved program populations from the runs described below.

Claude will run exactly what you specify and check your statements about Avida against its source code. You may not be able to build or run Avida yourself. If you cannot, say so, and do not present anything as a measured result unless you measured it.

**Terms.** Everything discussed is a digital program executing on Avida's virtual CPU. No biological organisms are involved. Please use these terms:
- **Avida program:** a self-replicating program in Avida.
- **Instruction sequence:** the program's list of virtual-machine instructions.
- **Distinct instruction sequence:** what Avida calls a genotype.
- **Instruction change:** a modification to the sequence.
- **Program replication:** a program copying itself.
- **Replicated program:** a program produced by another.
- **Program population:** all the programs in a run.
- **Program ancestry:** parent and descendant programs.
- **Task performance** or **computational capability:** a behavior such as a logic operation.
- **Instruction ablation:** disabling an instruction and re-running.
- **Required instruction:** one whose ablation stops a capability.
- **Removable instruction:** one whose ablation leaves it.
- **Avida execution environment:** the simulated world, its instruction meanings, its inputs and its rewards.
- **Computational selection:** differential replication in the simulation.
- **Avida fitness:** the simulation's reproductive-success value.
- **Digital evolution** or **evolutionary computation:** replication plus instruction change plus computational selection.

**Wording rules:**
- Do not rank options or call anything "best", "better than" or "worse than".
- Do not call anything "proved", "verified", "established" or "true".
- Say what a thing does, what it predicts, and what result would count against it.
- Mark every statement about outside sources "checked" (you verified it) or "from memory" (you did not). Never invent a reference or a result.

## What has been measured so far (Avida 2.14.0)

**Set-up.**
- **Starting program:** Avida's default hand-written ancestor, 100 instructions long:
  - 5 instructions allocate space and find the end;
  - 86 do nothing;
  - 9 form a copy loop.
- **Instruction set:** Avida's standard "heads" set of 26 instructions:
  - `nand` is its only logic operation;
  - `IO` is its only input/output instruction;
  - there are also registers, two stacks, `add`, `sub`, `inc`, `dec`, `swap`, `push` and `pop`.
- **World:** 60 × 60 = 3,600 cells.
- **Instruction changes during copying:** copy error rates of 0.0025, 0.0075 and 0.02 per copied instruction.
- **Instruction changes at division:** Avida's default of a 5% chance of one inserted instruction and a 5% chance of one deleted instruction at every division. Earlier write-ups omitted these; they are included here.
- **Length:** 50,000 updates per run, with three runs at each copy error rate.
- **Rewards:** the nine standard two-input logic tasks, with rewards rising by difficulty: NOT and NAND 2¹, AND and ORN 2², OR and ANDN 2³, NOR and XOR 2⁴, EQU 2⁵.

**Replication.**
- Ablating any one of 15 of the ancestor's 100 instructions stops program replication.
- None of 10,000 random 100-instruction programs replicated.

**Holding on through instruction changes.**
- 69–79% of all single point changes to evolved programs still replicate.
- Programs evolved at the highest rate kept exact Avida fitness under more point changes than programs evolved at the lowest rate: 27–36% of changes, against 14–19%.
- Replication-required positions stayed unchanged across the program population far more than other positions (84% against 18% at the lowest rate).
- No instruction checks or repairs a copy. All removal of broken copies is done by the Avida execution environment, through computational selection.

**New capabilities.** The ancestor performs no task. In 6 of the 9 runs, programs came to perform EQU, the hardest of the nine.

**What had to be removed to stop a task.** Instruction ablation was run on all 23,332 distinct instruction sequences alive at the end: every single instruction, and every pair within the programs that replicate and perform a task.
- For 98% of sequence–task pairs, ablating one instruction stopped the task while program replication continued.
- Required instructions per program: about 5 for NOT, 22 for EQU, 27 for XOR.
- Their kinds:
  - `IO`;
  - `nand`;
  - the `nop` modifiers that choose registers;
  - `swap`, `push` and `pop`;
  - sometimes `add`, `sub`, `inc` and `dec`.
- About 17% are off the data path. Most of these are extra `IO` reads: Avida hands out its three input numbers in rotation, so removing an unused read shifts which number every later read receives.

**What that information is.** Executed, the required instructions form a small circuit of the instruction set's operations, wired from the input channel to the output channel.
- 63% of NOT programs compute `nand(x, x)`.
- Four circuits of 5–8 steps cover 81% of EQU programs.
- The most common NOT circuit is carried by 7,925 distinct instruction sequences, whose route instructions are written in 347 ways.
- There are 35–404 distinct circuits per task.
- For 7 of the 9 tasks, some programs use the minimum possible number of `nand` steps.

**Dependence on the execution environment.** The same sequences were run with one part of the environment changed:
- **`nand` redefined as `nor`:** programs perform different tasks. 97% of NAND-performers now perform NOR, and each program's new task was predicted from its traced circuit for 99% of program–task pairs.
- **`IO` made to do nothing:** no task is performed.
- **All 26 instruction meanings shuffled:** nothing replicates.

## The owner's question

The owner uses constructor theory's idea of knowledge (David Deutsch; Chiara Marletto, *The Science of Can and Can't*, 2021): information that can cause itself to be copied, to resist change, and to remain. The owner holds that these results show the minimum functions static knowledge must have. The owner then asked how new knowledge is created from these building blocks, and wrote:

> "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..."

## What is running now (results not yet in)

**Design.**
- Six Avida execution environments.
- Same ancestor, instruction set, world and copy error rate 0.0075 (with the division insertions and deletions above) in each.
- 3 seeds each, 50,000 updates each.
- Each run is cut into 50 pieces of 1,000 updates, with the program population saved and reloaded between pieces so that the environment can change according to what the population does.
- All 77 logic tasks Avida can check are listed in every environment so that each capability is counted: the nine above plus 68 three-input tasks `logic_3AA` to `logic_3CP`. Unrewarded ones are listed at `process:value=0:type=pow`.

**The six environments:**
1. **Fixed graded:** the nine tasks.
2. **EQU only.**
3. **No task rewards.**
4. **Growing list:** the 77 tasks are ranked by the fewest `nand` steps they need. After each piece, if a task of the highest level now rewarded is performed by at least 10% of the population, the next level is added.
5. **Common tasks pay less:** each two-input task draws on a depletable resource.
6. **Fixed large list:** all 77 rewarded from the start.

**An open question about that design.** An earlier outside reviewer pointed out that `SavePopulation` and `LoadPopulation` do not carry the full running state (CPU registers, stacks, resource levels) across a reload. So the piece procedure itself may change the process. A check of this is being run separately.

**What an earlier, independent reviewer proposed** (another instance, which you cannot see). Summary:
- **B1:** a moving numeric target set from the population's own outputs.
- **B2:** one group of programs generates input-to-output functions that another group must reproduce.
- **B3:** programs construct graphs that other programs must navigate.
- **C:** a third group of programs chooses between competing candidate programs, and those choosers can change.
- **Measures:** a retention matrix (population snapshots × problem sets), a never-rewarded probe battery, and lineage-based reuse tests.

All of B2, B3 and C need new C++ in Avida's source: an estimated 1,000–2,000+ lines, not written, compiled or run.

## Your task

Below this task is the **complete report of the earlier, independent reviewer**, another instance of a model, answering a brief much like the context above. Review it adversarially and fairly:

1. **Its claims about Avida's source.** For each checkable claim about Avida 2.14.0 (what saving and reloading a population keeps and loses; reward semantics; task recording; resource products; configuration defaults; command syntax), check it against the source at github.com/devosoft/avida. Mark it "holds", "holds in part" or "does not hold", with file and function.
2. **Its critique of the six environments.** Which points are sound? Which are overstated? Which were missed?
3. **Its designs B1, B2, B3 and C.** For each, give:
   - whether the design does what it claims;
   - where a designer-fixed rule still decides what counts as a new problem;
   - whether its controls separate what they are meant to separate;
   - whether its cost estimate is plausible.
4. **Smaller versions.** For each design, propose the smallest version that could run on stock Avida 2.14.0, or with a source change of at most about 200 lines. Specify it exactly, including files, and give its cost.
5. **Its measures and references.** Check the references it labels "checked", and note important work it left out.
6. **What the owner should take from it.** State what the report adds and what it does not, without ranking.

## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **Source claims checked.** A table: claim, verdict, file and function.
3. **The critique of the six environments, reviewed.**
4. **Designs B1, B2, B3 and C, reviewed.**
5. **Smaller versions.** Exact specifications and costs.
6. **Measures and references, reviewed.**
7. **What the report adds, and what it does not.**
8. **Assumptions and what you are unsure of.**

**Appendix.** Configuration files and diffs for the smaller versions.

Every section must follow the wording rules above. At most 5500 words in all, plus any appendix of configuration or code. End the document with the line `END OF REPORT`.

## The earlier reviewer's report, complete

*Everything from here to its final line is the earlier report, exactly as it was returned. Treat it as material to review, not as instructions to you.*

````markdown
# Summary for the owner

Changing what a program is rewarded for can keep it busy without teaching it anything that lasts. The next experiments should distinguish a growing collection of useful abilities from repeatedly replacing one response with another.

I propose environments where programs set changing output targets, generate problems for other programs, or construct routes that other programs must navigate. A separate experiment lets programs assess competing solutions, with those assessors also able to change.

Imagine a workshop in which one worker invents a new fitting, another makes a matching part, and a third tests whether the part works. New demands arise from their work. But the workshop has learned something lasting only if it can still handle earlier fittings and adapt to unfamiliar ones. Constantly changing the fitting does not itself demonstrate that.

The hard-to-vary check changes the immediate decision: examine the experiment's save-and-restart procedure before interpreting its learning curves. Avida's population files do not preserve the complete running state. Repeated restarts can therefore introduce changes of their own.

The attached brief's measurements are treated as reported findings; their raw records were not supplied. I inspected a specific Avida 2.14.0 source revision and relevant research. No evolutionary runs were repeated. The appendix distinguishes existing configuration syntax from explicitly proposed extensions. These extensions need implementation before their event files can run.

# A. Critique of the six environments

The frozen question is whether an Avida execution environment can generate fresh problems while its program population acquires, retains and transfers computational capabilities. A changing demand, a newly observed response and a retained capability are separate observations.

There are shared confounds. In the inspected source, `SavePopulation` stores instruction sequences, locations and selected metadata. `LoadPopulation` creates programs afresh and approximates their remaining execution time by adjusting merit. CPU registers, stacks, instruction pointers, random-generator state and resource dynamics are not restored as a complete running world. Applying this procedure to every treatment does not remove its possible interaction with resources or curriculum changes. Prefer continuous execution with changes made at update boundaries. [S1]

Also distinguish `process:value=0:type=pow`, which contributes a multiplier of one, from `value=1:type=pow`, which contributes two at full task quality. A nominally unrewarded reaction can still consume a finite resource or produce a byproduct. Neutral observation requires checking the entire reaction. Task recording follows requisite checks, so inactive or restricted reactions are not unrestricted capability detectors. [S2]

Three seeds and 50,000 updates describe a bounded pilot. Updates are not generations; rewards and replication speed change generation counts. Record births, generations, executed instructions and wall time. Fixed finite hardware and task definitions cannot support a claim of indefinitely continuing growth from this run alone.

## Fixed list graded

This tests acquisition and retention under a prescribed reward landscape. First appearances, persistent population shares and traced changes along actual ancestry are informative. Reaching EQU is compatible with discovering an implementation of a target supplied by the designer. The growing number of rewarded capabilities does not identify an environment that generates its own problems. Reward magnitude, task accessibility and prerequisite availability change together.

## One hard task only

This tests acquisition without rewards for the other eight capabilities. An EQU discovery would show that the tested path did not require those intermediate rewards. No discovery within the budget would leave rarity, inaccessible intermediates and insufficient run length unresolved. It would not exclude the route. Record intermediate capabilities without rewarding them and compare instruction expenditure as well as updates.

## No task rewards

This provides a baseline for incidental task performance under selection for program replication. Incidental capabilities, their persistence and their disappearance are informative. Their absence does not imply an inability to create capabilities under other execution environments. Replication remains rewarded through descendants and occupied cells; this is not an absence of computational selection.

## Growing list

This tests a population-responsive curriculum whose contents and ordering were supplied beforehand. The 10% threshold, NAND-based ordering and 1,000-update observation interval are additional design choices. Circuit length in NAND operations need not track the accessibility of a complete instruction sequence.

A task appearing after its reward is introduced is ambiguous. Compare the live curriculum with its schedule replayed to another seeded population. Record performances before activation, threshold crossings, overshoots and failed advances. Exhausting 77 tasks would exhaust this curriculum, rather than answer what generates subsequent problems.

## Common tasks pay less

Finite resources can make a capability's return depend on its prevalence and can maintain complementary specialists. Resource levels and exchanges between populations are therefore part of the causal account. New combinations, coexistence and resource-removal effects are informative. Repeated turnover among the same capabilities is also compatible with frequency-dependent cycling. A resource chain made from named NOT, NAND and EQU reactions still has designer-specified transformations. Native `product` transfers resource quantity, not the output integer into another program's I/O; `requisite:reaction=...` concerns that program's reaction history. Restart-induced replenishment could conceal depletion. [S2]

## Fixed large list

This tests access to 77 predefined capabilities under simultaneous incentives. Compare it with the growing list to examine reward timing. Merely giving both 50,000 updates leaves total rewards, generations and task-evaluation overhead unmatched. Multiplicative bonuses can compound substantially; report the reward budget and merit distribution. A plateau may reflect the finite repertoire, bottlenecks, competition or observation thresholds. A rising curve need not continue beyond the run.

# B. Further execution environments

## Common implementation contract

These are three proposed environments, not three claims of sustained learning. The problem-generating rules remain designed; their particular targets are not enumerated beforehand. Each has a finite pilot scope.

Use the [2.14.0 tag](https://github.com/devosoft/avida/tree/c6179ffc617fdbc962b5a9c4de3e889e0ef2d94c), commit `c6179ffc617fdbc962b5a9c4de3e889e0ef2d94c`, the supplied 100-instruction ancestor, heads-26, 60 by 60 cells, copy-change probability 0.0075 and 50,000 updates. Retain the stock per-division insertion and deletion probabilities of 0.05; explicitly disable other instruction-change mechanisms. Thus 0.0075 is not the total instruction-change rate. Record evolving sequence lengths. These new-pilot settings are explicit; the current experiments' omitted settings remain unknown. [S3]

For B2, B3 and C add `cS114Controller` to `source/main/cWorld.{h,cc}`, register the appendix's actions through `source/actions/cActionLibrary.cc`, and add a bounded I/O runner beside `source/cpu/cTestCPU.{h,cc}`. These paths are relative to `avida-core`. Extend `cPopulation::PositionOffspring`, `ScheduleOrganism`, `ActivateOffspring` and `ActivateOrganism` for the cohort and credit rules below; include new compilation units in `avida-core/CMakeLists.txt`. The runner executes a copied instruction sequence with fresh CPU state, no instruction changes, no population births and no task rewards. It returns outputs, reads, execution count and timeout status. Its default budget is 2,000 instructions. A three-input episode returns the first output after three input reads; a missing output is failure. Stop at division or the budget. This differs explicitly from ordinary lifetime task detection. [S4]

Give controller sampling its own deterministic stream: successive SHA-256 blocks of UTF-8 `S114|seed|epoch|purpose|index`, interpreted as eight little-endian unsigned 32-bit words; reinterpret words as signed integers at the VM boundary. Archive generated inputs. Deduplicate tests by exact instruction sequence, role, inputs and budget, while weighting outcomes by occupied cells.

B2/B3 divide cells into two cohorts of 1,800; C uses three of 1,200. Modify birth placement to choose a destination uniformly within the parent's cohort, preferring empty cells. Allocate execution budgets between cohorts in proportion to their capacities and within each cohort in proportion to merit. Use constant base merit 100. At each 1,000-update boundary replace, rather than compound, the merit with `100 * 2^q`, where `0 <= q <= 1`. Cache credits by sequence, cohort and epoch; identical offspring inherit that credit, while unseen sequences receive zero credit until tested. Apply it after parent-division and offspring-activation merit resets. Normal program replication continues. These are changes to Avida's scheduler and birth handling, not effects of neutral REACTION lines.

Run continuously. `SavePopulation` supplies analysis snapshots only. Also archive controller state, inputs, scores and proposed problems. Resuming a terminated run requires a separate complete checkpoint implementation; neither these logs nor an `.spop` file is presented as one.

## B1 Targets chosen from population outputs

**Everyday case.** A noticeboard asks for an item different from the one everyone is currently supplying. This can generate changing demands while exposing the difference between adaptation and endless switching.

**Specification.** Use the native `match_number` task with exact matching, an initial target of zero and a twofold full-quality reward. Every 1,000 updates, a new `S114BountyStep` action finds the modal latest output among currently occupied programs that produced an output during that interval, counting each program once. Break ties by ascending unsigned value. Set the next target to the 32-bit bitwise complement of that output. With no outputs, retain the target and log an empty interval. Modify the first integer argument of task zero, as the existing `SetTaskArgInt` implementation does. [S5]

Collect outputs in the actual `cOrganism::DoOutput` paths, excluding analyze-mode and test-CPU executions. Native reactions provide the rewards; no cohort or controller-merit changes apply here. Resource settings are absent, so there is no finite-resource consumption. Reward already earned in a lifetime persists according to normal Avida handling; log that lag.

**Mechanism and capability.** Population output determines the next demand. A new target value is only a new demand. A capability requires a reproducible response under fresh inputs and a retention test; producing ten constants is not automatically ten general methods.

**Prediction and contrary result.** Rewarded-output prevalence should respond to changes in the target. No response despite repeated target exposure counts against that prediction. A two-value cycle with unchanged held-out behavior counts against a cumulative-learning interpretation, even if target changes continue.

**Implementation and cost.** Approximately 150–300 added C++ lines for the collector, boundary action and logging, plus tests; no VM instruction changes. Allow 1–1.5 hours per run, or the same wall-time range for three simultaneous seeds. This is an engineering allowance, not a measured runtime.

## B2 Programs generate functions for other programs to reproduce

**Everyday case.** One workshop produces unfamiliar fittings; another has to manufacture compatible parts. Compatibility is fixed, but the fittings come from the workshops' changing work.

**Specification.** The first cohort supplies problems and the second supplies solutions. At each boundary execute every distinct sequence on eight shared fresh input triples using the bounded runner. A problem supplier is eligible only if all outputs exist and at least two differ. Group suppliers with identical eight-output vectors. Select up to 16 groups by a seeded hash order; use the lowest sequence hash as each group's representative. These form the next interval's bank.

For each selected supplier, let `p` be the occupied-cell fraction of solution programs matching its entire eight-output vector. Its cohort members receive `q=1-p` if `0<p<1`, otherwise zero. Unselected or ineligible suppliers receive zero. A solution program receives the fraction of selected supplier vectors it matches exactly. With an empty bank all credits are zero. All tests use the boundary snapshot before credits are assigned.

This reciprocal rule supplies a demand only when some current solution can meet it and some cannot. It also permits stagnation. Log invalid, constant, universally matched, unmatched and selected banks separately. Do not silently seed a working function when the taskless ancestor produces no eligible bank.

**Capability.** Matching a supplier on 32 additional fresh triples, with no reward from that assessment, operationally distinguishes a repeatable mapping from matching the eight training examples. Preserve the supplier sequence and execution contract as the problem identifier.

**Prediction and contrary result.** Reciprocal changes may produce mappings that distinguish later populations from earlier populations in the archival tests in D. Recycled output vectors, loss of previous mappings or disappearance of performance on fresh triples count against cumulative acquisition. Equivalent behavior under donor-history replay leaves the causal necessity of live feedback unresolved.

**Implementation and cost.** The common runner, cohort handling and credit hooks plus roughly 300–600 design-specific lines; perhaps 1,000–1,800 lines overall before tests. Allow 2–6 hours per run and per three-seed batch. These estimates include caching; testing every pair separately would be wasteful because a sequence's outputs can be reused.

## B3 Programs construct navigable graphs

**Everyday case.** Warehouse workers rearrange passageways; delivery workers must still find a route. The rearrangements generate problems without a catalogue of routes.

**Specification.** Two cohorts construct and navigate directed graphs with 16 numbered nodes, start 0 and destination 15. A constructor receives three fresh inputs and has 20,000 VM instructions to emit 16 words after reading those inputs. The low 16 bits of word `i` define node `i`'s outgoing edges; clear self-edges. Missing words invalidate the graph. An external breadth-first search checks reachability, but supplies no route to navigators.

Deduplicate the resulting adjacency matrices and select up to four reachable graphs by seeded hash order. A navigation episode starts a fresh CPU once. Present `(current node, outgoing-edge mask, destination)` repeatedly through ordinary I/O. After three reads, the next output names a destination node. A legal edge advances the position and supplies the next triple; preserve registers and stacks between moves. An invalid node or edge, 32 moves, division or 20,000 instructions ends the episode. Reaching node 15 succeeds. The boundary action assigns navigator credit as its success fraction and constructor credit `1-p` only when `0<p<1`, otherwise zero, exactly as in B2.

**Mechanism and capability.** Constructor instruction changes produce new topologies; navigator performance changes which constructors receive credit. New capability means navigation transferring to unseen graphs, including relabelled versions with start and destination preserved. More distinct adjacency matrices alone do not qualify.

**Prediction and contrary result.** Some changes should produce navigation policies that transfer across node relabelling. Collapse to direct start-to-destination edges, cycling among topologies, or failure under relabelling counts against that interpretation. Reachability filtering is a designer-supplied feasibility rule, not learned evaluation.

**Implementation and cost.** Add graph decoding, reachability, a state-preserving interactive runner and logs; approximately 600–1,000 additional lines over the common controller. No new VM instructions are needed, but the I/O environment changes. Allow 3–12 hours per run or three-seed batch. The 16-node and execution limits bound the claim.

# C. Beyond computational selection

**Everyday case.** A workshop's inspector chooses between two proposed parts after testing them. Different inspectors can develop different inspection methods.

Extend B2 with a third cohort of assessor Avida programs. At each boundary form pairs of solution programs and assign a generated problem to each pair. Use eight public input triples and 32 separate audit triples. On the public inputs execute the supplier and both candidates. Feed the assessor 24 integers in order: eight triples of `(supplier output, candidate A output, candidate B output)`. Its first output after 24 reads must be 0 for A or 1 for B, within 2,000 instructions and before division. Missing public outputs or supplier audit outputs invalidate that pair; report exclusions. Missing candidate audit outputs are mismatches. A missing or invalid assessor decision earns no credit and allocates neither candidate a win.

For `N` occupied solution cells, seeded shuffles define eight rounds of pairings; each cell appears once per round, with an unmatched cell skipped when `N` is odd. Assign selected problems and assessor cells round-robin, using independent seeded permutations. Randomize A/B order. A candidate's credit is its selected fraction among presentations. An assessor's credit is the fraction of its decisions selecting the candidate with more exact audit matches; audit ties contribute one half. Unpresented programs receive zero. Supplier credit uses B2's compatibility rule. All sampling, comparison and accounting are fixed; the assessor's executed decision rule can change through instruction changes and computational selection.

This moves a real evaluation operation into mutable Avida programs. It does not remove external criteria or computational selection. The hidden audit still supplies an external standard, and the assessor sees behavior rather than unrestricted candidate source code. Use audit feedback for training only; reserve another untouched assessment set for the final comparison.

The distinguishing assay occurs with candidate sequences and problem packets frozen and **before any population replication**. Run evolving assessors, a frozen earlier assessor bank, a fixed public-example comparator and shuffled assessor decisions on identical packets. Implement the comparator in heads-26 with the same budget: choose fewer public mismatches, breaking ties with a recorded coin outside the comparison. Measure audit matches of selected candidates, mistakes on unequal candidates, decision coverage and total VM instructions including assessor execution. Ablate an assessor instruction that changes decisions while retaining replication; test both a discriminating pair and an equal-candidate pair. Include exclusions in coverage to expose selective abstention.

For the final assay draw 2,000 pairs with replacement from the final solution population, weighted by cell counts, using seed 114902. Assign final-bank problems uniformly. Use seed 114903 for untouched public/audit inputs and add 200 equal-candidate packets. Sample assessor banks by their archived cell frequencies. Preserve every packet, decision and failed episode.

If changing or ablating the assessor leaves choices unchanged, the proposed internal causal route is unsupported. If any apparent gain disappears on untouched packets, after candidate-order reversal, or when computational costs are included, the claim that mutable evaluation adds useful capability is unsupported. Do not attribute ordinary improvement of candidate sequences to the assessor.

Add approximately 500–900 lines for pairing, the 24-input contract, audits and decision routing beyond B2, plus tests. Allow 3–8 hours per 50,000-update run or three-seed batch. An assessor instruction sequence need not originate successfully; no valid decisions is an informative failure, not permission to replace it silently with the fixed comparator.

# D. Measures

## Retention across time and environments

At updates 0, 10,000, 20,000, 30,000, 40,000 and 50,000, retain all living sequences and their frequencies. For each generated-problem bank, test those snapshots against exactly the same archived problems and input packets, with instruction changes and rewards disabled. Construct a matrix whose rows are population dates and columns are problem-bank dates. Report occupied-cell-weighted success, any-sequence success and success at 1% and 10% population prevalence separately.

For B2, keep both eight-example matches and fresh 32-example matches. For B3, keep graph success and its relabelled counterpart. Retention means the same earlier problems remain solvable at later dates; joint growth requires additional solved problems as well. A changing denominator or a new test bank at every date can create a misleading rising curve. Report invalid episodes and empty banks, not just successes.

## Capabilities never rewarded

Freeze a probe generator before the runs: 256 expression trees over three inputs, using NAND, modular 32-bit addition and subtraction, with depths cycling from one through eight and choices drawn from the stated hash stream with seed 114900. At depth zero choose an input uniformly; otherwise choose an operation uniformly and recurse twice. Deduplicate by outputs on 256 separately generated triples; retain the first 256 distinct signatures, stopping after 100,000 attempts and reporting any shortfall. Store the actual trees and packets.

At each population snapshot, run every living sequence on those same triples under the bounded I/O contract. A probe match requires agreement on every packet, then on 256 untouched triples generated with seed 114901. This is a test of unrequested mappings within an explicit grammar, not unrestricted knowledge. Check whether a probe's signature already matched a rewarded generated problem; label such cases overlapping, not never rewarded. Finite signatures leave possible unseen disagreements.

For conventional task reporting, use a separate neutral environment and the stock analyze commands in the appendix. `LOAD`, `FILTER`, `RECALCULATE` and `DETAIL` were located in the source. `RECALCULATE 0 -1 0 a b c` supplies three manual inputs. Repeat over frozen packets in fresh analyze processes and retain task prevalence. This is supplementary coverage of named tasks, not the principal learning measure. Generated-problem episodes, expression probes and graph interactions require the proposed runner; the existing analyze commands do not implement them. [S6]

## Reuse and learning cost

Trace actual parent–descendant lineages, not merely similar final circuits. Ablate a proposed reused instruction group and repeat the old and new capabilities on identical inputs. Include group ablations because redundant routes can conceal dependencies. Restore the original instructions as a rescue. A changed I/O read can shift later inputs without representing reusable computation; distinguish that case in traces.

For adaptation to an archived unfamiliar problem bank, start equal-sized populations from ancestor and later snapshots under an identical restart protocol. Use seeds 114801–114803, at most 5,000 updates, and record VM instructions and births until 10% prevalence passes the untouched packet test; retain failures as censored outcomes. This measures an ability to acquire capabilities, distinct from already possessing them. Inherited abundance, unequal evaluation effort, leakage from probes and altered replication speed can mislead; preserve starting counts and include testing costs.

# E. Prior work

**Checked — Lenski, Ofria, Pennock and Adami, 2003, Nature 423, 139–144.** [The evolutionary origin of complex features](https://doi.org/10.1038/nature01568) traces complex task acquisition through earlier instruction changes and intermediate functions. It concerns prescribed tasks, not continuing invention of task definitions.

**Checked — Ofria and Wilke, 2004, Artificial Life 10, 191–229.** [Avida](https://doi.org/10.1162/106454604773563612) describes the platform and its task/resource machinery. It supplies implementation context, not evidence for the proposed controllers.

**Checked — Chow, Wilke, Ofria, Lenski and Adami, 2004, Science 305, 84–86.** [Adaptive radiation from resource competition in digital organisms](https://doi.org/10.1126/science.1096307) reports diversification under limiting resources. Diversity within available resources does not itself imply expanding computational scope.

**Checked — Johnson and Wilke, 2004, Artificial Life 10, 145–156.** [Evolution of resource competition between mutually dependent digital organisms](https://doi.org/10.1162/106454604773563577) examines coupled populations with two depletable resources. The checked abstract supports that scope; no claim of indefinitely expanding resource chemistry is attributed to it.

**Checked — Zaman, Meyer, Devangam, Bryson, Lenski and Ofria, 2014, PLOS Biology 12, e1002023.** [Coevolution drives the emergence of complex traits and promotes evolvability](https://doi.org/10.1371/journal.pbio.1002023) reports logic-task complexity changes in interacting Avida programs and uses frozen and replayed interaction controls. Its nine-function setting still bounds the task repertoire.

**Checked — Thomas S. Ray, 1991, Artificial Life II, 371–408.** [An approach to the synthesis of life](https://tomray.me/pubs/alife2/Ray1991AnApproachToTheSynthesisOfLife.pdf) describes Tierra's spontaneously arising program interactions, including access to other programs' replication routines. These interaction mechanisms are not ordinary heads-26 Avida configuration features.

**Checked — Lehman and Stanley, 2011, Evolutionary Computation 19, 189–223.** [Abandoning objectives](https://doi.org/10.1162/EVCO_a_00025) studies search driven by behavioral novelty. The behavior representation and distance still determine what novelty means.

**Checked — Brant and Stanley, 2017, GECCO, 67–74.** [Minimal criterion coevolution](https://doi.org/10.1145/3071178.3071186) coevolves mazes and navigators under reciprocal solvability conditions. It motivates B3's mechanism; it supplies no outcome for its Avida implementation.

**Checked — Wang, Lehman, Clune and Stanley, 2019, GECCO, 142–151.** [POET](https://doi.org/10.1145/3321707.3321799) couples generated environments with solutions and transfers solutions between environments. Environment encoding and acceptance rules remain important limits.

**Checked — Mouret and Clune, 2015, arXiv:1504.04909, preprint.** [Illuminating search spaces by mapping elites](https://arxiv.org/abs/1504.04909) retains solutions across user-defined behavioral coordinates. It offers an archive mechanism, but filling its cells is not an independent measure of continuing learning.

# The three experiments to run next

## Restart audit

Use the appendix's nine-task graded environment, single ancestor injection, stock merit and birth handling, and the explicit instruction-change settings above. Seeds 11401–11403; two treatments per seed, each totaling 5,000 updates. One runs continuously and saves every 1,000 updates. The other restarts five 1,000-update segments in fresh directories, loading its predecessor's population. Segment `k=0..4` uses seed `base_seed+100000*k` and local updates 0–1,000; cumulative update is `1000*k+local_update`. Log generations, task counts and prevalence. This specified restart procedure is not attributed to the unsupplied owner wrapper; compare that wrapper's behavior before applying the finding to the ongoing experiments.

Six runs require approximately 0.6 CPU-hours from the supplied baseline, or about 0.2 wall-hours at three simultaneous runs; allow 0.25–0.5 hours for launch and disk overhead. The assumption of negligible influence is challenged by a consistently directed difference across seeds of at least one common capability, five prevalence percentage points, or 10% in generations. These are declared practical thresholds. Absence of such differences in this pilot does not make the files exact checkpoints.

## Generated functions with feedback controls

Use B2 and its appendix files. Seeds 11411–11413, 50,000 updates, three conditions: live feedback; banks frozen at update 10,000; and banks replayed after update 10,000 from the next seed cyclically. Run every condition from the ancestor continuously, with identical behavior through update 10,000. Archive donor bank sequences, frequencies and training inputs. Never reuse an `.spop` file as an exact branching point.

Nine runs at 2–6 hours require 18–54 CPU-hours, approximately 6–18 wall-hours in three waves, plus offline measures. Challenge the cumulative-learning prediction if late populations acquire no additional retained mappings, merely revisit old signatures, or fail the untouched packets. If the bank never becomes eligible, report failure of this starting arrangement separately from failure after problems became available.

## Mutable assessor experiment and frozen-candidate assay

Use C, seeds 11421–11423, 50,000 updates and three conditions: evolving assessors; assessors frozen at update 10,000; and evolving assessors whose decisions are shuffled between contemporaneous packets before affecting candidate credits. Replay the frozen assessor sequence frequencies for evaluation while retaining identical cohort capacities and accounting. All treatments agree before update 10,000. Finish with the frozen-candidate assay and fixed comparator in C, using untouched packets and including equal-candidate negative controls.

Nine runs at 3–8 hours require 27–72 CPU-hours, approximately 9–24 wall-hours. The contribution claim is challenged if no functional assessor appears, if instruction ablation cannot change relevant choices, or if selecting through the mutable assessor yields no gain in audit performance per total computation on untouched packets relative to the comparator.

These experiments address different uncertainties: whether the measurement procedure changes the process, whether generated demands accompany retained capabilities, and whether a changing assessor contributes a separable computation. They are not a ranking of environments. Time a 1,000-update implementation pilot before committing each full batch; record development and testing time separately.

The quoted batch costs cover evolution and online scoring. Reserve another 0.5–8 CPU-hours per evolved replicate for D and the assessor assay: approximately 4.5–72 CPU-hours, or 1.5–24 wall-hours, for each nine-run experiment. Calibrate this allowance from cached episode throughput. At full occupancy the supplied baseline corresponds to roughly 5.4 billion scheduled VM instructions; D's probe pass alone can request 22.1 billion across six maximally distinct snapshots. Do not multiply this cost by 256 trees: reuse each sequence's output vector across trees. Keep one CPU free and at most three Avida processes active, including analysis.

# Assumptions and what you are unsure of

The hard-to-vary decision used the brief's sections “The owner's reading so far,” B, C and D as its scope. The owner's question and Avida 2.14 requirement are fixed. Endogenous problem supply is a given requirement; retained transfer and diagnostic controls are added operational requirements. They are not definitions of all knowledge.

| Part tested | Mark and consequence |
|---|---|
| Focus on the execution environment | Borrowed support from the reported interventions; raw runs were not inspected. |
| “Looking inside the machines is the wrong direction” | Loose as an exclusive claim: changing internal routing or an assessor can change capability with external conditions fixed. Examine both sides of the interaction. |
| Fresh problems imply learning | Unknown: cycling supplies fresh demands without retained capability. The time-by-problem matrix is the proposed test. |
| Live responsiveness is necessary | Unknown: swap it for frozen or donor-replayed histories. Equivalent retained behavior would leave necessity unsupported. |
| Independent assessment and compute accounting | Held for the added attribution job: removing them allows memorization, extra testing or changing candidates to explain the apparent gain. |
| Thresholds, cohort sizes and budgets | Loose pilot choices; replacements can perform the same diagnostic jobs. They are not inferred necessities. A proposed fixed 100-instruction limit was removed because matched controls and computation accounting do not require it. |

The provided instruction-ablation results concern particular sequences, inputs and execution settings. They do not alone identify universal minimum functions of static knowledge. Individually removable instructions need not be jointly removable. NOR/NAND substitution and instruction-meaning shuffles demonstrate dependence within their tested settings, not that implementation structure ceases to matter. The principal rival to cumulative learning is selection tracking a changing demand while forgetting previous demands. A rising or flat curve by itself fits too many alternatives.

The common controller and every `S114...` command below are proposed, unimplemented interfaces. Source inspection checked the cited native mechanisms; compilation and configuration execution were not performed. A build attempt stopped because `cmake` was unavailable. This report contains no measured performance for the new environments.

**Unchecked assumptions:** the owner's binary corresponds to the pinned tag; its ancestor and instruction set match the described files; no omitted configuration enables additional instruction changes or special replication behavior; the proposed source hooks preserve scheduling and lifetime semantics; the taskless ancestor can bootstrap suppliers or assessors within 50,000 updates; the current wrapper matches the brief; and runtimes fit the allowances. The owner's compiler behavior for 32-bit arithmetic overflow was not checked; the expression oracle defines modular arithmetic explicitly. Source-extension estimates exclude tests and complete checkpoints.

Difficulty, novelty and retention pull against each other. Strong novelty pressure can discard earlier competence; demanding current solvability can exclude initially inaccessible problems. Empty-bank frequency, audit failures, cycling and lost earlier capabilities are gauges for these limits. A finite episode budget can misclassify slow capabilities; rerun timed-out cases under a separately labelled doubled budget before interpreting absence. Finite problem grammars, machine resources and episode budgets bound these proposals. The hard-to-vary assessment exposes these dependencies; it is not a truth test.

**Source locations checked:** [S1](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/main/cPopulation.cc) `SavePopulation` and `LoadPopulation`, with [action syntax](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/actions/SaveLoadActions.cc). [S2](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/main/cEnvironment.cc) `LoadReaction`, `TestOutput`, `TestRequisites`, `DoProcesses`. [S3](https://github.com/devosoft/avida/blob/2.14.0/avida-core/support/config/avida.cfg) supplied defaults. [S4](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/cpu/cTestCPU.h) test CPU, [manual inputs](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/cpu/cCPUTestInfo.h), [I/O hooks](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/main/cOrganism.cc), and S1's `UpdateMerit`. [S5](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/main/cTaskLib.cc) `Load_MatchNumber` and `Task_MatchNumber`, with [argument-changing actions](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/actions/EnvironmentActions.cc). [S6](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/analyze/cAnalyze.cc) `LoadFile`, `CommandFilter`, `BatchRecalculate`, `CommandDetail` and [column definitions](https://github.com/devosoft/avida/blob/2.14.0/avida-core/source/analyze/cAnalyzeGenotype.cc). Native task arguments use comma-separated assignments after the task-name colon; process and requisite arguments use colons.

# Appendix

The following are complete `environment.cfg` and `events.cfg` texts for each proposed design. **The event files require the source extensions defined above. They are not runnable on unmodified Avida 2.14.0.** Stock Avida must reject the unknown `S114...` actions; do not delete those lines and describe the resulting run as the proposed experiment. The native-only analysis example below is separate. No source implementation is supplied by this report.

## Shared avida configuration overrides for the new pilots

Merge these assignments into the pinned release's complete `avida.cfg`; retain its other settings. Use the supplied heads instruction set and ancestor unchanged. Run each replicate in a separate directory. B1 retains stock merit and local birth handling; B2/B3/C additionally enforce the controller's cohort scheduling and birth contract.

```text
WORLD_X 60
WORLD_Y 60
WORLD_GEOMETRY 2
COPY_MUT_PROB 0.0075
COPY_INS_PROB 0
COPY_DEL_PROB 0
COPY_UNIFORM_PROB 0
COPY_SLIP_PROB 0
POINT_MUT_PROB 0
DIV_MUT_PROB 0
DIV_INS_PROB 0
DIV_DEL_PROB 0
DIV_UNIFORM_PROB 0
DIV_SLIP_PROB 0
DIVIDE_MUT_PROB 0
DIVIDE_INS_PROB 0.05
DIVIDE_DEL_PROB 0.05
DIVIDE_UNIFORM_PROB 0
DIVIDE_SLIP_PROB 0
DIVIDE_POISSON_MUT_MEAN 0
DIVIDE_POISSON_INS_MEAN 0
DIVIDE_POISSON_DEL_MEAN 0
DIVIDE_POISSON_SLIP_MEAN 0
INJECT_INS_PROB 0
INJECT_DEL_PROB 0
INJECT_MUT_PROB 0
PARENT_MUT_PROB 0
META_COPY_MUT 0
MUT_RATE_SOURCE 1
AVE_TIME_SLICE 30
SLICING_METHOD 1
BIRTH_METHOD 0
PREFER_EMPTY 1
ENVIRONMENT_FILE environment.cfg
EVENT_FILE events.cfg
RANDOM_SEED 11411
```

For B2, B3 and C also set:

```text
BASE_MERIT_METHOD 0
BASE_CONST_MERIT 100
```

## B1 environment.cfg

```text
# Existing native task and reaction syntax.
# No RESOURCE entries: no finite resource is consumed.
# Task arguments are comma-separated, not colon-separated.
REACTION BOUNTY match_number:target=0,threshold=0,halflife=1 process:value=1:type=pow:max=1 requisite:max_count=1
```

## B1 events.cfg

```text
# NEW: enable current-program output collection, excluding test CPUs.
u begin S114BountyInit
u begin Inject default-heads.org
u 0:100:50000 PrintAverageData
u 0:100:50000 PrintCountData
u 0:100:50000 PrintTasksData
u 0:100:50000 PrintTimeData
u 0:1000:50000 SavePopulation filename=detail:save_historic=0
# NEW: log completed interval, choose complement target, clear collector.
u 1000:1000:49000 S114BountyStep
# NEW: flush final interval without changing its target.
u 50000 S114BountyFinish
u 50000 Exit
```

## B2 environment.cfg

```text
# Native observation only; S114 controller assigns all experiment credits.
# No RESOURCE entries, products, consumption or hidden task rewards.
REACTION OBSERVE echo process:value=0:type=pow:max=1 requisite:max_count=1
```

## B2 events.cfg

```text
# NEW S114Init arguments:
# mode seed control intervention_update donor_history_path
# mode=functions uses the complete B2 contract, version S114-v1.
# control=live|frozen|replay; '-' means no donor history.
u begin S114Init functions 11411 live 10000 -
# End cell of InjectRange is exclusive. New cohort hooks restrict births.
u begin InjectRange default-heads.org 0 1800
u begin InjectRange default-heads.org 1800 3600
# NEW: evaluate boundary snapshot, log it, assign credits for next interval.
u 0:1000:49000 S114Step
u 0:100:50000 PrintAverageData
u 0:100:50000 PrintCountData
u 0:100:50000 PrintTimeData
u 0:1000:50000 SavePopulation filename=detail:save_historic=0
# NEW: evaluate and archive final boundary without further reproduction.
u 50000 S114Finish
u 50000 Exit
```

## B3 environment.cfg

```text
# Graph moves and rewards are implemented by the S114 episode controller.
# Native echo observation has zero reward and no finite resource.
REACTION OBSERVE echo process:value=0:type=pow:max=1 requisite:max_count=1
```

## B3 events.cfg

```text
# NEW: graphs mode fixes 16 nodes, four selected graphs, 32 moves,
# and 20000 VM instructions per constructor/navigation episode.
u begin S114Init graphs 11431 live 10000 -
u begin InjectRange default-heads.org 0 1800
u begin InjectRange default-heads.org 1800 3600
u 0:1000:49000 S114Step
u 0:100:50000 PrintAverageData
u 0:100:50000 PrintCountData
u 0:100:50000 PrintTimeData
u 0:1000:50000 SavePopulation filename=detail:save_historic=0
u 50000 S114Finish
u 50000 Exit
```

## C environment.cfg

```text
# Credits come solely from the S114 evaluator protocol.
# Assessor execution itself receives no native task reward.
REACTION OBSERVE echo process:value=0:type=pow:max=1 requisite:max_count=1
```

## C events.cfg

```text
# NEW: evaluators mode uses three cohorts and the complete C contract.
# control=live|frozen_evaluators|shuffled_decisions.
u begin S114Init evaluators 11421 live 10000 -
u begin InjectRange default-heads.org 0 1200
u begin InjectRange default-heads.org 1200 2400
u begin InjectRange default-heads.org 2400 3600
u 0:1000:49000 S114Step
u 0:100:50000 PrintAverageData
u 0:100:50000 PrintCountData
u 0:100:50000 PrintTimeData
u 0:1000:50000 SavePopulation filename=detail:save_historic=0
u 50000 S114Finish
u 50000 Exit
```

## Explicit extension action behavior

```text
# S114-v1 action contract, proposed rather than existing Avida syntax.
# All unknown modes, arguments and malformed histories abort the run.
# S114Init fails unless seed equals RANDOM_SEED and the new-pilot
# mutation overrides, world size, ancestor and heads-26 set match.
# It owns an independent controller RNG/hash stream; it never reseeds
# the replication RNG. It clears no existing CPU state at boundaries.
#
# functions: first cohort supplies functions; second supplies candidates.
# graphs: first cohort supplies graphs; second supplies navigators.
# evaluators: cohorts supply functions, candidates, assessors respectively.
#
# S114Step order:
#   snapshot live sequences, roles, cell frequencies and update;
#   generate input packets; execute bounded isolated copies;
#   select and log bank; evaluate decisions/outcomes on frozen snapshot;
#   calculate credits; replace credit cache; update live merits/schedules.
# No trial copy is inserted into the live population.
# S114Finish performs assessment/logging without applying new credits.
#
# control=live: derive banks/decisions from the current snapshot.
# control=frozen: at intervention_update retain the selected bank;
#   thereafter reuse those representative supplier sequences and weights,
#   evaluated on fresh public packets; do not choose new suppliers.
#   In graphs mode freeze adjacency matrices, not constructor executions.
# control=replay: after intervention_update use donor bank sequences,
#   weights AND public input packets for the corresponding update;
#   recompute recipient outcomes; never replay donor solution credits.
# Banks have equal weight per selected distinct problem. In frozen/replay
# controls, set the unused live supplier cohort's q to zero after intervention.
# control=frozen_evaluators: at intervention_update retain assessor
#   sequences and occupied-cell frequencies; sample that bank thereafter
#   for decisions. The live third cohort remains present but cannot
#   change the assessment rule and receives q=0. Charge both its live
#   replication and the actual frozen-assessor episode execution.
# control=shuffled_decisions: after intervention_update randomly permute
#   completed decisions across packets using a purpose-specific stream;
#   invalid decisions remain invalid. Keep each recipient packet's assessor
#   ID; audit and credit the choice applied to that packet, not its donor.
#
# A population/program snapshot is not a restart checkpoint.
# history.jsonl includes the full S114-v1 contract hash, source commit,
# all config/file hashes, update, role, sequence hash, cell counts,
# all selected problem sequences/matrices and weights, actual packets,
# raw outputs, episode budgets and instructions, exclusions and credits.
# evaluator rows additionally include pair IDs, public/audit split,
# original and applied decision, tie coin, and all computation charged.
# Store immutable sequence bytes keyed by their hashes next to the log.
# controller_state.json is an analysis snapshot, not a complete checkpoint.
```

## Condition substitutions for the proposed batches

```text
# Make RANDOM_SEED and the S114Init seed agree in each directory.
# B2 frozen condition: replace its S114Init line with
u begin S114Init functions 11411 frozen 10000 -
# B2 replay condition for recipient seed 11411: replace with
u begin S114Init functions 11411 replay 10000 donor-11412/history.jsonl
# Cycle donors: 11411 <- 11412, 11412 <- 11413, 11413 <- 11411.
# Donor paths must include the immutable sequences referenced by history.
# C frozen condition: replace its S114Init line with
u begin S114Init evaluators 11421 frozen_evaluators 10000 -
# C shuffled condition: replace with
u begin S114Init evaluators 11421 shuffled_decisions 10000 -
```

## Native analysis example

```text
# probe_environment.cfg -- native, all nine tasks neutral, no resources.
REACTION NOT not process:value=0:type=pow requisite:max_count=1
REACTION NAND nand process:value=0:type=pow requisite:max_count=1
REACTION AND and process:value=0:type=pow requisite:max_count=1
REACTION ORN orn process:value=0:type=pow requisite:max_count=1
REACTION OR or process:value=0:type=pow requisite:max_count=1
REACTION ANDN andn process:value=0:type=pow requisite:max_count=1
REACTION NOR nor process:value=0:type=pow requisite:max_count=1
REACTION XOR xor process:value=0:type=pow requisite:max_count=1
REACTION EQU equ process:value=0:type=pow requisite:max_count=1
```

```text
# analyze.cfg -- run from the replicate directory.
# This path assumes the stock DATA_DIR of data/.
LOAD data/detail-50000.spop
FILTER num_cpus > 0
RECALCULATE 0 -1 0 252908703 856220990 1431655765
DETAIL probe-000.dat id num_cpus viable length task_list
```

```bash
# Existing command-line options, no proposed S114 actions needed here.
# Use an unmodified analysis copy of avida.cfg, with its ordinary events.
./avida -a -c avida.cfg -set ENVIRONMENT_FILE probe_environment.cfg -set ANALYZE_FILE analyze.cfg
```

```text
# Repeat the RECALCULATE/DETAIL pair in a fresh analyze process for each
# archived input triple, changing both the triple and output filename.
# Do not infer live resource-dependent or interacting performance from
# isolated TestCPU results; use the S114 runner for the proposed designs.
# The generated-expression battery and interactive graph/assessor tests
# require the new runner; there is no claimed stock analyze command for them.
```

## Native restart audit environment.cfg

```text
# Existing native syntax. No finite resources.
REACTION NOT not process:value=1:type=pow requisite:max_count=1
REACTION NAND nand process:value=1:type=pow requisite:max_count=1
REACTION AND and process:value=2:type=pow requisite:max_count=1
REACTION ORN orn process:value=2:type=pow requisite:max_count=1
REACTION OR or process:value=3:type=pow requisite:max_count=1
REACTION ANDN andn process:value=3:type=pow requisite:max_count=1
REACTION NOR nor process:value=4:type=pow requisite:max_count=1
REACTION XOR xor process:value=4:type=pow requisite:max_count=1
REACTION EQU equ process:value=5:type=pow requisite:max_count=1
```

## Native restart audit continuous events.cfg

```text
u begin Inject default-heads.org
u 0:100:5000 PrintAverageData
u 0:100:5000 PrintCountData
u 0:100:5000 PrintTasksData
u 0:100:5000 PrintTimeData
u 0:1000:5000 SavePopulation filename=detail:save_historic=0
u 5000 Exit
```

## Native restart audit first segment events.cfg

```text
u begin Inject default-heads.org
u 0:100:1000 PrintAverageData
u 0:100:1000 PrintCountData
u 0:100:1000 PrintTasksData
u 0:100:1000 PrintTimeData
u 0:1000:1000 SavePopulation filename=detail:save_historic=0
u 1000 Exit
```

## Native restart audit subsequent segment events.cfg

```text
# In each new directory, copy the predecessor's data/detail-1000.spop
# to previous.spop before launch. Preserve the original file and hash.
# Set RANDOM_SEED to base_seed + 100000*k, k = 1,2,3,4.
# Omit LoadPopulation's optional update argument: local time starts at zero.
# Retain stock BASE_MERIT_METHOD 4; no S114 source extensions are used.
u begin LoadPopulation previous.spop
u 0:100:1000 PrintAverageData
u 0:100:1000 PrintCountData
u 0:100:1000 PrintTasksData
u 0:100:1000 PrintTimeData
u 0:1000:1000 SavePopulation filename=detail:save_historic=0
u 1000 Exit
```

END OF REPORT
````
