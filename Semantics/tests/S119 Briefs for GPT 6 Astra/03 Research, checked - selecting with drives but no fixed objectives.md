# Brief 03 for GPT 6 Astra: Research, checked: selecting with drives but no fixed objectives

*Written by Claude on 1 October 2026 for the owner to hand to a fresh GPT 6 Astra agent (log S119, decision S73). Why this brief: it collects what is already known about selectors that drive without a fixed target (novelty, curiosity, learning progress, empowerment, open-ended environment generation, Avida's own work), with every source checked. It says how named each target really is, and what each would cost in Avida. Run it with Ultra, every helper at maximum, because each line of research can be checked separately. Paste everything below the line.*

---

# Research, checked: selecting with drives but no fixed objectives

## Who this is for, and the ground rules

You are helping a research project on how new knowledge is created. The owner is not a programmer and reads results in plain language. Another AI model, Claude, will check your reply and run experiments on a machine where Avida is built.

**You are a fresh instance.** You have no memory of earlier conversations and cannot see other replies. Everything you need is here. Stay within your task.

**What Claude has:**
- Avida 2.14.0 at commit 47f13dad (github.com/devosoft/avida), with cmake and a C++ compiler.
- 4 CPUs, at most 3 Avida processes at once. A 50,000-update run with nine paid tasks in a 3,600-cell world takes about one CPU-hour.
- Every saved program population from the runs below.
- `RUN_BOUNDED`, a tested patch: an analyze-mode command that runs each program on given input numbers and records every output.

**Your limits.** You may not be able to build or run Avida. If you cannot, say so. If you run anything, say exactly what you ran and paste its output. Never present as a result anything you did not run. Claude will check every statement about Avida's source against the commit.

**Safety.** Write no self-replicating code that executes on a real machine. All replication stays inside Avida.

## The owner's Avida terms (binding)

The owner's glossary, its table in full:

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

No biological organisms are involved.

**"Avida execution environment" means the whole simulated world**, not only its rewards. It covers:
- instruction meanings and the input numbers handed in;
- how processor time is shared and how copies are made;
- what is paid for, and what is required before a copy is allowed;
- resources, world size and layout.

**Wording rules.**
- Do not rank options or call anything "best", "better" or "worse".
- Do not call anything "proved", "verified", "established" or "true".
- Say what a thing does, what it predicts, and what result would count against it.
- Mark each statement about an outside source "checked" or "from memory". Never invent a reference or a result.

## Avida in brief, and what was found

**How the instructions work.** Programs use the "heads" set of 26 instructions. `nand` is the only logic operation. `IO` hands a register's number to the world as output, then reads the next of the program's three input numbers, in rotation.

**How paying works.** C++ code (`cEnvironment::TestOutput`, `cTaskLib`) checks each output against a list of functions of the inputs. A match is "task performance", and earns more processor time, so faster copying. The 77 logic tasks accept 251 of the 256 three-input bitwise functions.

**Instruction changes.** Copying changes 0.0075 of instructions, plus a 5% chance each of one insertion and one deletion per division.

**Results.** Every run starts from one ancestor that performs no task.

- **S113, six execution environments** (3 seeds each). Tasks done by at least one program in ten after 50,000 updates:

  | Execution environment | Tasks |
  |---|---|
  | A list growing harder as the program population mastered it | 48–65 of 77 |
  | All 77 paid from the start | 13–41 |
  | Common tasks pay less | 8–17 |
  | Nine fixed tasks | 7–8 |
  | EQU only | 0 |
  | Nothing paid | 0 |

  In every paid run the count levelled off (in one run only when continued past 50,000 updates).
- **S116, input order.** Some capabilities work only in the world's fixed order of the three input numbers. In one run, 2,377 programs did NOT in that order; in most other orders, 61 to 369 did.
- **S117, where Avida departs from the project's theory of explanation:**
  - Lasting does not require doing a task. With nothing paid, 3,600 programs lasted and 11 did NOT.
  - Nothing in Avida holds a problem or criticises. Withholding pay is a signal, not a criticism.
  - New capabilities come by selection, not creation: from copying changes that lasted.
  - All choosing is done by the execution environment, from task lists people wrote in advance.
- **Earlier replies to similar briefs.**
  - What worked: close code reading, careful controls, a small patch whose tests all matched.
  - What failed: arithmetic slips; worlds too small to start; too few runs; one load-bearing claim that did not hold; large C++ never written.

## The owner's question, in the owner's words

> "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..." (S63)

> "I don't know yet.  Avida can exhibit a type of autonomy. But can you give it an instinct to solve a problem without specifying exact target goals?" (S71)

> "Oh. The execution environment is the thing I want to test. Not the individual programs. The environment is the thing that does selecting. Just as an autonomous agent does selection." (S72)

So the execution environment, as selector, is under test. The programs are its material. Any "instinct" belongs to the execution environment.

**Three grades of naming a target** (use them strictly):

| Grade | Name | What it means |
|---|---|---|
| 1 | Named exactly | A list of functions, each paid or required. |
| 2 | Named one level up | A class or rule is written down ("any of these 251", "whichever is rare"). |
| 3 | Truly unnamed | No checking code computes what counts as a solution. The standard comes from something that itself changes, such as what the world does next. |

Stock Avida is always at grade 1 or 2.

**Running now (S118), results not in.** Two stock pilots:
- P1 pays all 77 tasks equally, from depleting resources, so rare functions pay more.
- P2 pays nothing; from update 5,000, copying requires performing one of the 77.

Do not presume their outcome.

**Left open by the owner.** Offer options only, never decisions, on:
- whether a task list written by people counts in the history of the programs it selected;
- what knowledge is;
- which costly runs come next.

## Your task

Survey **selecting systems that have drives but no fixed objectives**, check each source, and say what each would mean for an Avida execution environment.

**Already covered; do not repeat it.** An earlier reply surveyed how to *measure* open-ended change. It covered:
- evolutionary activity statistics (Bedau and Packard);
- MODES;
- Channon's work;
- POET as a measure.

This brief is about the *selector*. Cover at least:
- novelty search;
- minimal criterion novelty search;
- minimal criterion coevolution;
- open-ended environment generation (for example POET, Enhanced POET, PAIRED, OMNI);
- learning progress and intrinsic motivation;
- Schmidhuber's artificial curiosity and compression progress;
- empowerment;
- quality diversity (for example MAP-Elites);
- host and parasite coevolution in Avida;
- any work selecting for prediction or anticipation in digital evolution;
- any other Avida-specific work on selecting without fixed targets.

**For each source give:**
- title, authors, year and where it was published, with a DOI or link;
- "checked" (you opened it and confirmed the details) or "from memory";
- any numbers it reports, quoted only if checked, with page or section;
- no quotation longer than 25 words.

**For each line of work, map it:**
- **The instinct.** What the selector's "instinct" is: what it pays for, and what memory or model it keeps.
- **The grade.** Whether the target is truly unnamed, or named one level up. Say what is written down in advance: the behaviour space, the distance measure, the criterion, the archive rule.
- **What it reports.** What it reports about lasting new capabilities, and over what length of run.
- **The cost in Avida.** Stock (settings, events, a driver script between pieces), or C++. Give lines as an estimate, marked as one, and name the source files it would touch.
- **What would count against it in Avida.** The result that would show it does not carry over.

**Then:**
- **Where the literature has nothing.** Say this plainly. For example: a selector that holds a problem; criticism aimed at a part; prediction selected in digital evolution, if you find none.
- **Shared assumptions.** Assumptions these methods share that bear on the owner's question. For example, that a behaviour space must be chosen by the designer.
- **Options, not decisions.** For each, what Claude could test first, and its cost.

**If several of you work in parallel:**
- Split by line of work.
- Merge into one document.
- Check every source a second time when merging.
- Remove duplicates.

## Return exactly this

One document, with these sections in this order:
1. **Summary for the owner.** At most 200 everyday words.
2. **Table.** One row per line of work, with columns:
   - name;
   - the selector's instinct;
   - its memory and model;
   - grade of naming;
   - stock or C++;
   - estimated cost;
   - what counts against.
3. **One section per line of work.** Sources, with checked or from memory; what it does; the mapping above.
4. **Where the literature has nothing.**
5. **Shared assumptions.**
6. **Options for Claude.** With costs.
7. **Reference list.** Each entry marked checked or from memory.

At most 6,000 words, plus the reference list. Follow the wording rules. End with the line `END OF REPORT`.
