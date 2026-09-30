# Brief 08 for GPT 6 Astra: A growing supply of problems, using only stock Avida

*Written by Claude on 30 September 2026 for the owner to hand to a fresh GPT 6 Astra agent (log S115, decision S66). Why this brief: The earlier reviewer's designs for problems that come from the program population needed new C++. This asks what can be done with Avida's own resources, products, requisites, cascades and events, which can be run at once and compared with the six environments now running. Paste everything below the line.*

---

# A growing supply of problems, using only stock Avida

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

Design **two to four Avida execution environments**, runnable on **unmodified Avida 2.14.0**, in which the set of problems that pay grows or changes **as a result of what the program population does**, not on a schedule and not from a list the designer ranks in advance. Use only Avida's own machinery, for example:
- resources that deplete and flow in (`RESOURCE`);
- reactions that produce resources other reactions use (`process:product=...`);
- requisites on earlier reactions (`requisite:reaction=...`, `requisite:noreaction=...`);
- cascade environments (Avida ships example files such as `environment-cascade.cfg`: check them);
- spatial resources, gradients and cell-local resources;
- demes;
- events that fire at updates, including any that respond to population statistics.

Save-and-reload between pieces may not carry resources across. Prefer designs that run **continuously**.

For each design, give:
- a plain description with an everyday example first;
- the complete `environment.cfg` and `events.cfg` (plus any `avida.cfg` changes), with every line checked against `avida-core/source/main/cEnvironment.cc`, `cTaskLib.cc` and `source/actions/*.cc`;
- how the population's own activity changes which problems pay, step by step, and where the designer's own choices still decide what counts;
- what a new capability means in it, and how to count capabilities that were never rewarded, using the 77 logic tasks and Avida's arithmetic tasks as a probe battery;
- its prediction, and the result that would count against it;
- how to compare it fairly with the six environments above (same ancestor, world, copy error rate, length, seeds);
- its cost in CPU-hours on the machine described.

## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **The designs.** One subsection each, with every item listed above.
3. **How they would be compared with the six running environments.**
4. **Source locations checked.** File and function per keyword used.
5. **Assumptions and what you are unsure of.**

**Appendix.** Complete `avida.cfg` changes, `environment.cfg` and `events.cfg` for each design, ready to paste.

Every section must follow the wording rules above. At most 5000 words in all, plus any appendix of configuration or code. End the document with the line `END OF REPORT`.
