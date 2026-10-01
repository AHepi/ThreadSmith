# Brief 04 for GPT 6 Astra: The execution environment as an autonomous agent: what it lacks, and the smallest additions

*Written by Claude on 1 October 2026 for the owner to hand to a fresh GPT 6 Astra agent (log S119, decision S73). Why this brief: it takes the owner's comparison (S72) item by item. For each thing an agent's selection has and Avida's lacks, it asks for the smallest addition and a test in Avida, strict about what is named in advance. Run it as a single agent at maximum, because it is one line of reasoning whose items depend on one another. Paste everything below the line.*

---

# The execution environment as an autonomous agent: what it lacks, and the smallest additions

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

The owner compares the Avida execution environment to an autonomous agent that selects. Take that comparison item by item.

For each item, work through these six steps:
1. **What an agent's selection has.** Say what an autonomous agent's selection has that Avida's execution environment lacks. Use plain words, and draw on any field, saying which.
2. **What Avida does now.** Give file and function at 47f13dad, and the S117 point it bears on.
3. **The smallest addition** to an Avida execution environment that would supply it:
   - stock if possible (settings, events, a driver script between pieces);
   - otherwise C++, with an estimate of lines, marked as an estimate, and the files it touches.
4. **What is named in advance.** List exactly what the designer must write down before the run, and give the grade. Be strict: an addition that only moves the named target one level up must say so.
5. **A test in Avida.**
   - the arms, including a control without the addition;
   - world size, length and number of seeds, with arithmetic from the spreads above;
   - the measure;
   - what result would count against the addition working.
6. **Whether it needs another item first.**

**Items, at least:**
- **Memory of what it selected.** Today pay depends on the present output only.
- **A model of what it selects among.** An expectation of what programs will do.
- **Choosing what to test next.** Today the same three-number test runs at every output.
- **Holding a problem.** A standing, unsolved question that stays until something solves it.
- **Criticism with a target.** A reason a program failed, aimed at a part, not only less pay.
- **Expectation and surprise** (S117 found that nothing in Avida is surprised).
- **Keeping rival candidates for one problem.**
- **Anything else you find.**

**Build on earlier work.**
- An earlier reply proposed seven conditions for an environment that keeps creating knowledge, in constructor theory's terms. It included representations used to predict, and criticism that revises them.
- One of its load-bearing claims about Avida did not hold: it said recoding the instructions needed C++, and it did not.
- Do not repeat that work. Go item by item on the selector, and check every claim about Avida in the source.

**Then:**
- **Dependencies.** A short dependency order of the additions, not a ranking.
- **One combined design.** The smallest that brings three or more items together, with its cost and what counts against it.
- **What no addition can supply** inside Avida, if anything, and why.

## Return exactly this

One document, with these sections in this order:
1. **Summary for the owner.** At most 200 everyday words, with one example.
2. **Table.** One row per item, with columns:
   - what the agent has;
   - what Avida has now;
   - smallest addition;
   - stock or C++;
   - named in advance, and grade;
   - test;
   - what counts against.
3. **One section per item.** The six steps above, with source references.
4. **Dependency order.**
5. **The combined design.** Files, or a C++ outline, with cost.
6. **What no addition can supply.**
7. **What you ran, with outputs, and what you are unsure of.** Mark each outside source checked or from memory.

At most 5,000 words. Follow the wording rules. End with the line `END OF REPORT`.
