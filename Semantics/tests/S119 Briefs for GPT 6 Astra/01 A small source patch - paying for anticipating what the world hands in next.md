# Brief 01 for GPT 6 Astra: A small source patch - paying for anticipating what the world hands in next

*Written by Claude on 1 October 2026 for the owner to hand to a fresh GPT 6 Astra agent (log S119, decision S73). Why this brief: it asks for the one Avida execution environment the S118 plan found stock Avida cannot make, one whose standard is what the world does next rather than a function its checking code computes. It is modelled on S115's brief 07, whose small patch worked when Claude built it. Run it as a single agent at maximum, because one small patch must fit together. Paste everything below the line.*

---

# A small source patch - paying for anticipating what the world hands in next

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

Write a **small C++ patch** to Avida at commit 47f13dad. It adds an execution environment that pays programs for **anticipating a hidden regularity** in the numbers the world hands in.

**What the patch does:**
- **Hand out a sequence.** When switched on, the world hands each program its input numbers from a sequence made by a hidden rule. The rule is chosen by one setting, instead of three random numbers in rotation.
- **Pay for matching what comes next.** When a program outputs a number, the patch checks whether it equals the number that program's next read will receive. If it does, the program is paid. It may also be counted as a reaction, so that `REQUIRE_SINGLE_REACTION` can use it.
- **Never name the rule.** The checker compares only the output with the world's next number. It never computes the rule as a target function.

`IO` already outputs first and reads second. Claude's reading of where this happens is below; check it.
- `cHardwareCPU::Inst_TaskIO` (`cpu/cHardwareCPU.cc`, about line 4188)
- `cOrganism::DoInput` and `DoOutput` (`main/cOrganism.cc`, 368–410)
- `cEnvironment::SetupInputs` (`main/cEnvironment.cc`, 1252)
- `cEnvironment::TestOutput` (from 1337)

**Rules:**
- Include at least these:
  - R0: independent random numbers, a control with nothing to anticipate.
  - R1: a simple rule.
  - R2: a rule that cannot be met by repeating a number already read.
  - R-switch: the rule changes at a set update, to test whether the pressure keeps acting.
- For R1 and R2, hand-write in heads mnemonics the shortest program you can find that anticipates them.
- Give the chance of a match by luck for each rule, with the arithmetic shown.

**Limits on the patch:**
- About 150 changed lines of C++ at most, not counting comments and tests.
- Off by default. When off, Avida must behave exactly as stock.
- Give each change a one-line comment.
- Say how the test CPU and `RUN_BOUNDED` see the new inputs.

**Tests, with expected outputs worked out by hand:**
- the stock ancestor under R1;
- your anticipating program under R1, and under R0;
- a program that repeats an earlier input;
- the R-switch;
- the patched binary with the feature off, against the stock binary: a 400-update run with a given seed and identical data files expected. Give the commands; Claude will compare.

**A first experiment.** Give the arms (R0, R1, R2, R-switch), the world size, the length, and the number of seeds. Work out the number of seeds from the seed-to-seed spreads given above, with the arithmetic shown. Say what would count against "this execution environment makes anticipation appear". For example: matches never above chance, or matches only by repeating inputs.

**The limits, strictly.** Say what is still named in advance, and at which grade. For example:
- the relation "say the next number";
- the designer's choice of rule family;
- exact equality.

Say also whether matching the next number is the same as anticipating it, and how S116's input-order finding bears on that.

## Return exactly this

One document, with these sections in this order:
1. **Summary for the owner.** At most 150 everyday words, with an example.
2. **Where in the source.** File, function and line at the commit, with short quoted lines.
3. **The design.** Settings, rules, and how matching and payment work.
4. **The diff.** Complete and unified, against 47f13dad.
5. **Build steps.** Exact commands; say whether any `CMakeLists.txt` changes.
6. **Tests.** Files, programs in mnemonics, expected output lines, and how each was worked out.
7. **Ordinary runs unchanged.** The check, and its commands.
8. **The first experiment.** Arms, sizes, cost in CPU-hours, and what counts against.
9. **What is still named.** The grade, with reasons.
10. **What you ran, and what you are unsure of.** Paste any outputs. Say whether you compiled the patch.

At most 4,000 words, plus a code appendix. Follow the wording rules. End with the line `END OF REPORT`.
