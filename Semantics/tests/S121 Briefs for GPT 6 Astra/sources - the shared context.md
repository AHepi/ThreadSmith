# Sources: the shared context of the S121 briefs

*Written by Claude on 1 October 2026 (log S121, decision S75). This text sits below the line of every S121 brief, between the brief's title and its task. It is the S119 shared context, updated: the S118 results, Astra's S119 replies and what the S120 checks confirmed so far, the owner's words S75 with Claude's reading of them, the owner's report in a few lines, and the open questions. The owner's Avida terms table is copied unchanged from records/Semantics - Avida terms, given by the owner.md.*

---

## Who this is for, and the ground rules

This is for a research project on how new knowledge is created. The owner is not a programmer. Claude, another AI model, will check your reply against Avida's source and run any experiment.

**You are a fresh instance.** Everything you need is here, with the owner's report attached. Stay within your task.

**Claude has** Avida 2.14.0 at commit 47f13dad (github.com/devosoft/avida), a C++ toolchain, 4 CPUs (at most 3 Avida processes at once; a 50,000-update run in a 3,600-cell world takes about one CPU-hour), every saved program population below, and `RUN_BOUNDED`, an analyze-mode command that runs each program on given inputs and records every output.

**Your limits.** You may not be able to build or run Avida; if not, say so. If you run anything, say exactly what and paste its output. Never present as a result anything you did not run.

**Safety.** Write no self-replicating code that executes on a real machine. All replication stays inside Avida.

## The owner's Avida terms (binding)

Use them throughout. The glossary's table in full:

```
Avida Terminology Glossary

Use these terms when describing experiments involving Avida digital organisms.

Potentially ambiguous wording| Prefer| Meaning in this project
organism| digital organism / Avida program| A self-replicating program running inside the Avida virtual environment
genome| instruction sequence / digital genome| The ordered sequence of Avida virtual-machine instructions
gene| instruction / instruction region| One instruction or a functional region of an Avida program
mutation| instruction change / program variation| A modification to the digital instruction sequence
mutate| modify an instruction / introduce program variation| Change one or more virtual-machine instructions
evolution| evolutionary computation / digital evolution| A computational search process involving replication, variation, and selection
evolve an organism| evolve an Avida program / run evolutionary search| Use Avida's evolutionary process to discover programs with a desired computational behavior
fitness| Avida fitness / computational performance| A value used by the Avida simulation to determine reproductive success
reproduction| program replication / self-replication| Copying an Avida program within the simulation
offspring| replicated program / descendant program| A new program produced by another Avida program
population| program population| The collection of digital programs in an Avida run
phenotype| observed computational behavior| What the Avida program actually does when executed
trait| computational capability / task performance| A behavior such as performing an arithmetic or logic operation
kill / lethal| fails replication / nonfunctional| The modified program no longer passes the relevant execution or replication test
viability| functional execution / replication capability| Whether the program still executes or reproduces under the experiment's criteria
delete genes| remove instructions| Delete virtual-machine instructions from the program
gene deletion| instruction deletion / program ablation| Removal of an instruction or instruction region
knockout| instruction ablation| Disable or remove a digital instruction and measure the resulting behavior
essential gene| required instruction| An instruction whose removal causes the tested capability to disappear
nonessential gene| removable instruction| An instruction that can be removed while preserving the tested behavior
minimal genome| minimal instruction sequence| The smallest tested Avida program that retains the specified computational behavior
minimum viable organism| smallest functional program| The shortest program that still satisfies the experiment's execution criteria
selection| computational selection| Differential replication within the digital simulation
environment| Avida execution environment| The simulated computational environment in which programs execute
metabolism| task-processing behavior| Avida's mechanism for rewarding specified computational operations
adaptation| improved computational performance| A program change that increases performance under the simulation's scoring rules
lineage| program ancestry / digital lineage| A sequence of parent and descendant programs in the simulation
genetic diversity| instruction-sequence diversity| Variation among digital programs in the simulated population
experimental evolution| evolutionary-computation experiment| A simulation in which digital programs change over many generations
engineer an organism| modify an Avida program| Deliberately alter the virtual instruction sequence
optimize the organism| optimize the program| Search for a program that performs a specified computational task efficiently
preserve function| preserve tested behavior| Keep the program's specified arithmetic or logic output unchanged
remove everything unnecessary| program minimization| Remove instructions while repeatedly checking whether the required behavior remains
```

No biological organisms are involved. **"Avida execution environment" means the whole simulated world**: instruction meanings, the inputs handed in, how processor time is shared and copies are made, what is paid or required before a copy, resources, world size and layout.

**Wording rules.** Do not rank options or call anything "best", "better" or "worse", "proved", "verified", "established" or "true". Say what a thing does, what it predicts, and what would count against it. Mark each statement about an outside source "checked" (you opened it) or "from memory". Never invent a reference or a result.

## Avida in brief, and what was found

Programs use the "heads" set of 26 instructions; `nand` is the only logic operation. `IO` outputs a register's number, then reads the next of three input numbers, in rotation. C++ (`cEnvironment::TestOutput`, `cTaskLib`) checks each output against functions of the inputs; a match ("task performance") earns processor time. The 77 logic tasks accept 251 of the 256 three-input bitwise functions. Runs start from one ancestor that performs no task. **Every paid capability so far is memoryless**: checked against the inputs, never their order or timing.

- **S113**, six execution environments, 50,000 updates in pieces of 1,000, a driver saving and reloading the program population. Tasks done by one program in ten: a list growing harder as tasks were mastered 48–65 of 77; all 77 paid 13–41; common tasks pay less 8–17; nine fixed 7–8; nothing paid 0. Every count levelled off.
- **S114**: a reload keeps instruction sequences, not processor state, random state, resource levels or task records; a reloaded program counts as doing nothing until it finishes a copy.
- **S116**: some capabilities work only in the world's fixed input order (2,377 programs did NOT in it; 61–369 in most other orders).
- **S117**, against the project's theory of explanation: lasting does not require doing a task; nothing holds a problem or criticises (withheld pay is a signal, not a criticism); capabilities come by selection, not creation; programs predict nothing, so nothing is surprised; all choosing is by the execution environment, from lists people wrote.
- **S118**: "any function counts, common ones pay less" gave 12–21 common functions, all easy; "copy only after solving something" gave a floor, not a drive.

## Astra's earlier replies (S119), and what checking confirmed (S120)

- **01, patch `ANTICIPATE_MODE`** (off by default): each program reads a private number stream (random; repeated; plus one each read; repeat then plus one); task `anticipate` pays an output equal to the next number to be read. Builds; its tests reproduce exactly; off, it matches stock.
- **02, selectors with memory**, stock Avida in pieces with a Python driver: A pays tasks whose share rose fastest; B pays the rarely seen. Controls: blind replay of the pay schedule; fixed mean pay. Runs reproduce; but A pays almost nothing once nothing rises, a reload's undercount reads as a fall, and pay is weak.
- **04, the execution environment as an agent**: eight gaps (memory of what was selected; a model of candidates; choosing the next test; holding a problem; criticism aimed at a part; expectation and surprise; rivals for one problem; findings that change selection), each with a driver addition at grade 2. Its 13 source claims hold.
- Pilots of 01 and 02 are running. **Do not presume their results.**

## The owner's question, in the owner's words

> "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..." (S63)

> "I don't know yet.  Avida can exhibit a type of autonomy. But can you give it an instinct to solve a problem without specifying exact target goals?" (S71)

> "Oh. The execution environment is the thing I want to test. Not the individual programs. The environment is the thing that does selecting. Just as an autonomous agent does selection." (S72)

> "Can you see where I'm going with this? If so, 4 more tasks for Astra. Unless only one task makes sense right Now" (S75, with the report)

**Claude's reading of S75** (not the owner's words): what S117 found missing and reply 04 proposed (memory, expectation, surprise, holding a problem) are temporal: an input changes how a system responds later. So the selector might be a small neuron-like system whose instinct is its dynamics, not a target list, and programs may need tasks that need history. "Common pays less" is already adaptation; learning progress is a trace's rate of change.

## The report, in a few lines

A synthesis whose 22 cited studies were not rechecked. Memoryless: y = f(x). Stateful: s' = F(s, x, Δt), y = G(s, x), so B after A can differ from B alone. Cheap units: leaky integration, coincidence and interval detection, adaptation, rebound after release, bistable latches, sequence detection; learning rules (tempotron, chronotron). Order detector: a trace set to 1 on A, decaying as exp(−Δt/τ); on B, respond if it exceeds θ. **Its caution:** timing adds no class of computation that digital logic with memory lacks; any gain is in representation and cost, measured against simpler alternatives, with input identities and counts fixed while order or spacing changes, and each component removed in turn.

## Grades of naming a target (use them strictly)

| Grade | Meaning |
|---|---|
| 1, named exactly | A list of functions, each paid or required. |
| 2, named one level up | A class or rule is written down ("any of these 251", "whichever is rare"). |
| 3, truly unnamed | No checking code computes what counts as a solution; the standard comes from something that itself changes. |

## Left open by the owner

Offer options, never decisions, on: whether a task list written by people counts in the history of the programs it selected; what knowledge is; whether a fixed way of selecting counts as an instinct; which costly runs come next.
