# Brief for GPT 6 Astra: execution environments that keep learning

*Written by Claude on 30 September 2026 for the owner to hand to GPT 6 Astra (log S114, decision S65). It is self-contained: Astra has none of the project's files. Paste everything below the line.*

---

## Who this is for and what it is about

You are helping a research project on how new knowledge is created. The project owner is not a programmer. They test ideas by having AI models write and run code, and they read the results in plain language. Your answer will be read by the owner and by another AI model that runs the experiments. Please be concrete, exact and honest about what you know and what you are unsure of.

**Terms.** This work uses Avida, an artificial-life and evolutionary-computation platform. Everything discussed is a digital program executing on Avida's virtual CPU. Please use these terms:
- **Avida program**: a self-replicating program in Avida.
- **Instruction sequence**: the program's list of virtual-machine instructions.
- **Instruction change**: a modification to that list.
- **Program replication**: a program copying itself.
- **Program population**: all the programs in a run.
- **Task performance** or **computational capability**: a behavior such as a logic operation.
- **Instruction ablation**: disabling an instruction and re-running.
- **Required instruction**: one whose ablation stops a capability.
- **Avida execution environment**: the simulated world, its instruction meanings, its inputs and its rewards.
- **Computational selection**: differential replication in the simulation.
- **Avida fitness**: the simulation's reproductive-success value.
- **Digital evolution**: the search process of replication, instruction change and computational selection.

No biological organisms are involved.

**Wording rules.**
- Do not rank designs or call any design "best", "better than" or "worse than".
- Do not say anything is "proved", "verified", "established" or "true".
- Say what a design does, what it predicts, and what result would count against it.

## What has been found so far (all measured in Avida 2.14.0)

**Set-up.**
- The starting program is Avida's default hand-written ancestor, 100 instructions long:
  - 5 instructions allocate space and find the end;
  - 86 do nothing;
  - 9 form a copy loop.
- The instruction set is Avida's standard "heads" set of 26 instructions:
  - `nand` is its only logic operation;
  - `IO` is its only input/output instruction;
  - there are also registers, two stacks, `add`, `sub`, `inc`, `dec`, `swap`, `push` and `pop`.
- The world is 3,600 cells.
- Three instruction-change rates were used: about 1 in 400, 1 in 133 and 1 in 50 copied instructions.
- Each run lasted 50,000 updates, with 3 runs per rate.
- The rewards were the nine standard two-input logic tasks, with rewards rising by difficulty: NOT and NAND 2¹, AND and ORN 2², OR and ANDN 2³, NOR and XOR 2⁴, EQU 2⁵.

**Replication.**
- Ablating any one of 15 of the ancestor's 100 instructions stops program replication; the other 85 are removable.
- None of 10,000 random 100-instruction programs replicated.

**Holding on through instruction changes.**
- 69–79% of all single instruction changes to evolved programs still replicate.
- Programs evolved at the high rate kept exact Avida fitness under more single changes: 27–36% of changes, against 14–19% at the low rate.
- Replication-required positions stayed unchanged across the program population far more than the others (84% against 18% at the low rate).
- No instruction in any program checks or repairs a copy. All the removing of broken copies is done by the Avida execution environment, through computational selection.

**New capabilities.**
- The ancestor performs no task.
- In 6 of the 9 runs, programs came to perform EQU, the hardest of the nine tasks.

**What had to be removed** to stop a task (instruction ablation on all 23,332 distinct instruction sequences alive at the end, every single instruction and every pair):
- For 98% of program–task pairs, ablating one instruction stopped the task while program replication continued.
- Required instructions per program: about 5 for NOT, 22 for EQU, 27 for XOR.
- They are always of the same kinds:
  - `IO`;
  - `nand`;
  - the `nop` modifiers that select registers;
  - `swap`, `push` and `pop`;
  - sometimes `add`, `sub`, `inc` and `dec`.
- About 17% of required instructions are not on the data path at all. Most are extra `IO` reads: Avida hands out its three input numbers in rotation, so removing an unused read shifts which number every later read receives.

**What that information is.** When the required instructions are executed, they form a small circuit of the instruction set's operations, wired from the input channel to the output channel.
- Most NOT programs (63%) compute `nand(x, x)`.
- Four circuits of 5–8 steps cover 81% of EQU programs.
- One circuit is written in many different instruction sequences. The most common NOT circuit is carried by 7,925 distinct instruction sequences, whose route instructions are written in 347 different ways.
- There are 35–404 distinct circuits per task across runs.
- For 7 of the 9 tasks, the smallest circuit found uses the minimum possible number of `nand` steps.

**Dependence on the execution environment.** The same instruction sequences were run with one thing in the environment changed:
- **`nand` redefined as `nor`:**
  - the programs perform different tasks (97% of NAND-performers now perform NOR);
  - which task each program would switch to was predicted from its traced circuit, correctly for 99% of program–task pairs.
- **`IO` made to do nothing:** no program performs any task.
- **All 26 instruction meanings shuffled:** nothing replicates or performs anything.

**The owner's reading so far.** The owner uses constructor theory's idea of knowledge (Deutsch; Marletto, *The Science of Can and Can't*, 2021): information that can cause itself to be copied, to resist change, and to remain. The owner holds that these Avida results show the minimum functions static knowledge must have. The owner then asked how new knowledge is created from these building blocks, and concluded, in their own words:

> "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..."

## What is being run now (do not repeat it; critique it)

**Design.**
- Six Avida execution environments.
- Same ancestor, instruction set, world size and instruction-change rate (about 1 in 133) in each.
- 3 seeds each, 50,000 updates each.
- Each run is cut into 50 pieces of 1,000 updates. Between pieces, the program population is saved and reloaded, so that the environment can change according to what the population does.
- All 77 logic tasks that Avida can check are listed in every environment (unrewarded ones at reward 2⁰), so that every capability is counted. The 77 are the nine two-input tasks plus Avida's 68 three-input logic tasks (`logic_3AA` to `logic_3CP`). Avida 2.14's task library also has 56 arithmetic tasks and others (214 task names in all); these are not used here.

**The six environments:**
1. **Fixed list, graded:** the nine tasks above.
2. **One hard task only:** only EQU rewarded.
3. **No task rewards:** program replication only.
4. **Growing list:** the 77 logic tasks are ranked by the fewest `nand` steps they need. After each piece, if a task of the highest level now rewarded is performed by at least 10% of the program population, the next level's tasks are added to the rewards.
5. **Common tasks pay less:** each task's reward comes from a depletable resource, so a task pays less as more programs perform it.
6. **Fixed large list:** all 77 rewarded from the start.

**Measures:**
- the number of distinct capabilities present over time, by any program and by at least a stated share of the population;
- when each capability first appears;
- whether capabilities are kept;
- whether the count keeps rising or levels off;
- whether new task circuits reuse circuits of tasks already present.

## Your task

**A. Critique the six environments.** For each one:
- what it can and cannot show about the owner's question;
- any confound, for example "growing list" still being a list the designer wrote in advance;
- which results would be informative, and which would be ambiguous.

**B. Propose three to five further Avida execution environments** in which the supply of new problems comes from the execution environment or the program population itself, not from a list written in advance. Examples of the kind meant, which you may use or replace:
- problems defined by other programs' outputs;
- resource chains, where one task's product is the input of another;
- environments that change in response to what the program population does;
- interactions between programs.

For each design give:
- a plain-language description, with an everyday example first;
- an exact specification for Avida 2.14.0: `environment.cfg` lines (REACTION, RESOURCE, PROCESS and REQUISITE settings), event lines, and any population save/load scheme. If Avida cannot do it without changing its source code, say exactly what would have to change and how large a change that is;
- the mechanism by which new problems keep arising;
- what a "new capability" means in it, operationally;
- what it predicts, and what result would count against that prediction;
- rough cost, given a machine with 4 CPUs running at most 3 Avida runs at once, where a 50,000-update run of the nine-task environment takes about one hour.

**C. The step beyond computational selection.** In every environment so far, all the choosing is done by the execution environment, through instruction changes plus removal of what does not replicate. Nothing inside the program population evaluates anything. Propose at least one concrete, testable Avida execution environment in which evaluation of candidate programs against problems is itself carried out by parts of the environment or of the program population, and in which those evaluators can themselves change. For it, give:
- the specification, as in B;
- what measurement would distinguish it from plain computational selection;
- what result would count against the idea that it adds anything.

**D. Measures of "progressively learns".** Define measures that do not reduce to counting the designer's own task list. For example, test the final program populations against a fixed large battery of probe tasks that are never rewarded, and count capabilities that were never asked for. For each measure, give the exact procedure in Avida (analyze-mode commands if relevant), and say what it would take for the measure to mislead.

**E. Prior work.** List the prior work most relevant to A–D. Possible starting points include:
- Avida studies such as Lenski, Ofria, Pennock and Adami 2003 on the origin of complex features;
- Tierra;
- open-endedness research: novelty search, minimal-criterion coevolution, POET, MAP-Elites;
- resource and cascade environments in Avida.

For each item give the authors, year and venue, one line on what it found that bears on this question, and a confidence label: "checked" if you verified it, "from memory" if not. Do not invent results or references. If you are unsure a paper exists or says what you remember, say so.

## Return exactly this

A single document, at most 5,000 words plus an appendix of configuration text, with these sections in this order:

1. **Summary for the owner.** At most 250 words, in plain everyday language with no jargon: what you propose and why, with one concrete example.
2. **A. Critique of the six environments.** One subsection per environment.
3. **B. Further execution environments.** One subsection per design, with every item listed under B.
4. **C. Beyond computational selection.** The design, the distinguishing measurement, and what would count against it.
5. **D. Measures.** Each measure with its exact procedure and how it could mislead.
6. **E. Prior work.** A list, each item with its confidence label.
7. **The three experiments to run next.** Chosen from A–D, each with:
   - its exact Avida set-up;
   - seeds and run length;
   - expected cost in hours on the machine described;
   - the result that would count against its prediction.

   Say why these three, without ranking them against each other as better or worse.
8. **Assumptions and what you are unsure of.** Every assumption you made about Avida's behavior that you did not check against its source code or documentation, marked as such.

**Appendix.** Complete `environment.cfg` and `events.cfg` text for every design in B and C, ready to paste.

End the document with the line `END OF REPORT`.
