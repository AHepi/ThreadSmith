# Brief 07 for GPT 6 Astra: a small source patch, a bounded test runner for Avida's analyze mode

*Written by Claude on 30 September 2026 for the owner to hand to a fresh GPT 6 Astra agent (log S115, decision S66). Why this brief: Many proposed measures, such as testing programs on problems nobody rewarded, need a way to run one program on given inputs and read all its outputs. This brief asks for that one piece as a small, reviewable patch. It plays to the model's source-reading strength and keeps the unbuildable part small. Claude will compile it and report back. Paste everything below the line.*

---

# A small source patch: a bounded test runner for Avida's analyze mode

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

Write a **small C++ patch** to Avida at commit 47f13dad (github.com/devosoft/avida). It adds an **analyze-mode command** that does the following:
- takes the currently loaded batch of distinct instruction sequences;
- for each sequence, and for each of a list of input triples read from a file, executes the sequence on Avida's test CPU:
  - with fresh CPU state;
  - with no instruction changes;
  - with no births into any population;
  - with no rewards;
  - up to a given instruction budget;
- feeds the inputs through the ordinary `IO` instruction, three numbers in the order given, repeating in rotation as Avida normally does;
- records, per sequence and per triple:
  - every output value in order;
  - the number of reads;
  - the number of instructions executed;
  - whether it divided;
  - whether it hit the budget;
- writes one line per sequence and triple to a named output file, with the columns documented.

**Requirements:**
- Keep it as small as possible, and reuse `cTestCPU` and `cCPUTestInfo` where they already provide this.
- Deliver a unified diff against the exact files at that commit.
- Include:
  - build instructions (Avida builds with cmake; say whether `avida-core/CMakeLists.txt` needs a change);
  - a test: an analyze script and an input file that runs the command on Avida's default ancestor and on two hand-written sequences whose outputs you work out by hand;
  - the expected output lines.
- Say precisely how this command differs from Avida's existing `RECALCULATE` with manual inputs, and why that is not enough, or, if it is enough, say so and stop.
- If you cannot compile, say so. Claude will compile it and send the compiler's messages to a fresh instance if it fails, so make the diff easy to read and each change self-explanatory in a one-line comment.

## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 150 words, everyday language: what the tool does, with an example.
2. **Why `RECALCULATE` is or is not enough.**
3. **The design.** Which existing classes are reused, and the output format.
4. **The diff.** Complete, unified, against commit 47f13dad.
5. **Build instructions.**
6. **The test.** Script, input file, the two hand-written sequences in mnemonics, and the expected output lines with how they were worked out.
7. **Assumptions and what you are unsure of.** Including whether you compiled it.

Every section must follow the wording rules above. At most 4000 words in all, plus any appendix of configuration or code. End the document with the line `END OF REPORT`.
