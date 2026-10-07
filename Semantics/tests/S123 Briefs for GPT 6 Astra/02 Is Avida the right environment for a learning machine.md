# Brief 02 for GPT 6 Astra: Is Avida the right environment for a learning machine

*Written by Claude on 2 October 2026 for the owner to hand to a fresh GPT 6 Astra agent (log S123, decisions S77, S78, S79). Why this brief: the owner's question (S78) whether Avida is the right environment at all, since a learning machine needs constant external input. It asks for a criterion for each meaning of knowledge, not a verdict, and for other platforms only as options with costs. Run it as **Ultra, every helper at maximum**: the input inventory in Avida's code, the platforms and the criteria are separate pieces of work. Attach to the chat, for every brief: `sources - the semantics, standing alone, after round 4.md`, `sources - a reader's guide to the semantics.md`, `sources - the shared context.md` and `sources - Pinker context.md`, all in this folder. Paste everything below the line.*

---

# Is Avida the right environment for a learning machine

## Ground rules

A research project on how new knowledge is created; the owner is not a programmer. Claude, another AI model, will check your reply against Avida's source and the semantics, and run any experiment. **You are a fresh instance**: all you need is here and in the attachments (the semantics, whole; a reader's guide to it; the shared context, with more detail; a note on Steven Pinker).

**Claude has** Avida 2.14.0 at commit 47f13dad (github.com/devosoft/avida), 4 CPUs (a 20,000-update run in a 3,600-cell world costs about 0.35 CPU-hours), the saved populations and the patches named below. **Your limits**: if you cannot build or run Avida, say so; if you run anything, say what and paste its output; never present as a result anything you did not run. No self-replicating code that executes on a real machine: all replication stays inside Avida. **Wording**: do not rank options or call anything "best", "proved", "verified" or "true"; mark each claim about an outside source "checked" (you opened it) or "from memory", and keep the Pinker note's marks; never invent a reference or a result; quote no book for more than 25 words in a row.

## What Avida is

A simulated computer in which small programs (instruction sequences; "heads" set of 26 instructions, `nand` the only logic operation) copy themselves with occasional instruction changes; the execution environment pays (processor time) for outputs matching tasks written in its C++. **Each program reads three numbers made by Avida's own random generator, always in one order** (`main/cEnvironment.cc` 1252-1294; `IO`, `cpu/cHardwareCPU.cc` 4188-4201). A processor is reset at division; only the instruction sequence passes on. Runs start from one ancestor that does no task.

## The owner's words

> "We have a definition of information and knowledge, and they are in constructor theory. I suspect the next move is how do we know when this indefinite amorphous thing in a creative agent constitutes knowledge." (S57)

> "What kind of information has the following properties: - Can cause itself to be copied. - Can cause itself to resist change. - Can cause itself to remain." Then: "The explanation kind comes next. I know I defined knowledge. I'm asking if you can think of a type of program with these exact properties" (S59)

> "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..." (S63)

> "Avida can exhibit a type of autonomy. But can you give it an instinct to solve a problem without specifying exact target goals?" (S71)

> "Oh. The execution environment is the thing I want to test. Not the individual programs. The environment is the thing that does selecting. Just as an autonomous agent does selection." (S72)

> "Can you see where I'm going with this? If so, 4 more tasks for Astra." (S75, with a report on timing in neurons)

> "The definition of knowledge says it must has a causal affect on its surroundings. Not just other little programs, but Avida itself. Has that been demonstrated yet?" (S76) Answer from the record: effects so far run only through channels Avida's designers wrote; none was tested on Avida itself.

> "The next step is wait for these runs and build a hypothesis of what knowledge could mean in the context of Avida. In order for this to work, Astra will need to know a bit about the semantics, the relevant passages from constructor theory and maybe the beginning of infinity to pad out the vagueness. The four tasks will need to ask different questions with tests. The step after that is refinement. [...] Include the whole semantics so that evolution and transports make sense to astra so it can distinguish between what it's testing and what it is not." (S77)

> "We also need to tell whether Avida is the right environment or not. Because a learning machine also needs constant external input. Which actually refines the question further. What transports are needed for learning from external data to even begin." (S78)

## The owner's Avida terms (binding)

**"Avida execution environment" means the whole simulated world**, and it is the selector under test (S72). The glossary's table in full:

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

## What has been found (S111 to S122)

- **S111**: the three properties, measured: 15 of the ancestor's 100 instructions cause its copying; 69-79 in 100 one-instruction variants still copy, though nothing repairs; the lineage remained, the ancestor did not. Marletto's elimination test on EQU picks out 19-26 instructions per program. In each property the program's instructions are a necessary part, Avida's rules the other.
- **S112**: the evolved information is a small circuit of Avida's operations from input to output, a circuit only relative to Avida's instruction meanings (with `nand` meaning `nor`, 97 in 100 NAND programs do NOR).
- **S113, S116**: a task list growing harder made 48-65 of 77 tasks common; every count levelled off; many capabilities work only in the world's input order.
- **S117**: against the semantics, structure lines up; explanation, construction, prediction and surprise have nothing in Avida. Whether a program represents its task flips on an open reading: **Reading A**, the checking code is part of the world's rules (the program's correspondence is selected); **Reading B**, it is an earlier occurrence representing the task (declared). Lasting does not require doing a task.
- **S118 to S122**: "any function, common ones pay less" made 12-21 easy functions common (grade 2); a patch (`ANTICIPATE_MODE`) streams a designer's rule to each program and pays the next number ("add one" learned by 95 in 100); selectors with memory made no clear difference at weak pay; a history patch: in one paid run 14 of the 50 commonest sequences kept where an event came. No grade 3 mechanism found.

## Constructor theory and The Beginning of Infinity

Marletto defines knowledge as "information that is capable of keeping itself instantiated in physical systems. It is resilient information." (ch. 1, p. 13). She gives one test for finding it in a system: it is what one "would ultimately have to eliminate in order to prevent a particular transformation from being performed reliably" (ch. 5, p. 145). Deutsch: knowledge tends to cause itself to remain once embodied in a suitable environment, and arises almost only by the error-correcting processes of evolution or thought (ch. 4, p. 78, paraphrased). He sets adaptation against explanation: "adaptations are never explanatory and rarely have much reach beyond the situations in which they evolved" (ch. 4, pp. 105-106). What explanation has and adaptation lacks, on his account, is reach to cases never met: "Non-explanatory systems cannot cross the conceptual gap that an explanatory conjecture crosses, to engage with unexperienced evidence or non-existent phenomena." (ch. 3, p. 73).

## The semantics, in one paragraph (whole text and reader's guide attached)

It never says "knowledge". A **transport** carries one organization onto another (L181-189, D5.1), faithful when parts and whole agree under every admitted change (D5.4-D5.7); it has **exactly one of three histories** (L191-201): **selected** (population, variation, a history of changes that occurred, no represented target: D12.1), **constructed** (a construction trace with a represented target: D12.2) or **declared** (D12.3). **Representation** is a faithful transport with a selected or constructed history (L205-213, D12.5); **surprise** needs a prediction transport and a change outside its history (L215-225, D12.7).

**Pinker** (note attached): a learner needs outside data with a pattern it lacks, a second view of what the data are about, and prior limits on its guesses: "the data alone are insufficient" **[checked: P2004, pp. 949-950]**.

## Grades of naming a target

1, named exactly (a list of functions, each paid or required); 2, named one level up (a class or rule written down); 3, truly unnamed (no checking code computes what counts as a solution; the standard comes from something that itself changes).

**Left open by the owner** (options only): Reading A or B; what knowledge is; whether a fixed way of selecting is an instinct; what "Avida itself" means in S76 (its rules or its state); which costly runs come next.

---

## Your question

**Is Avida the right environment for finding out what knowledge could mean, given that a learning machine needs constant external input?** Answer it by a criterion, not a verdict:

1. **State a criterion** for "right environment" for each meaning of knowledge in play: Marletto's (resilient information; the elimination test), the owner's three properties with S76's effect on Avida itself, Deutsch's two kinds (adaptive, and explanatory), Pinker's (accurate representation learned from data within a life, within selected constraints; see the note), and the semantics' representation, prediction and construction (L205-225, L405). A criterion says what an environment must supply for a case of that meaning to be able to occur, and what observation would show it did.
2. **What external input Avida supplies now.** Check and extend Claude's list in the shared context ("Avida's inputs, in more detail": three numbers per cell from Avida's own generator, always in one order; inputs set by event; resources and their schedules; messages; state grids; pay changed by events or a driver), each with file and line. Claude's reading: none of it carries information about anything outside Avida's own rules.
3. **What it could be given**: a recorded outside stream by a small patch (as S119's `ANTICIPATE_MODE` gives a designer's stream); data turned into events; a driver; other programs as a source the selector does not contain; a state grid built from data; learning within a program's life (a modified Avida evolved associative learning when patterns varied between generations but held within a life **[checked in the note: Pontes et al. 2020, abstract]**).
4. **What it cannot be given without becoming something else**: Claude's list to test: a second channel telling what the data are about; live continuous input (Avida runs in updates); learned state passed on (only the instruction sequence is inherited); rules programs can change (the C++ is fixed).
5. **Other platforms**, only as options with their costs and what each would lose (the project's tools, its saved populations, the owner's terms): for example a purpose-built world with lasting objects like the semantics' Argument 10 (L618-632); reinforcement-learning or neuroevolution environments; Avida modified as in Pontes et al. **Do not choose.**

## What this brief tests, and what it does not

**Tests**: whether Avida can supply, for each meaning, what that meaning needs to occur; in the semantics' terms, whether Avida can carry a **data transport from a source outside the selector**, an **object layer of persistent things** (L175, D12.6) on which **prediction and surprise** (L215-223, D12.7) can be defined, and a history in which a program builds a binding during its own run (**construction**, D12.2, L405). **Does not test**: the full transport inventory (brief 01); where the knowledge sits or its effect on Avida (brief 03); whether anything explains (brief 04). Keep **selected** correspondences (all of Avida's so far) apart from **constructed** ones (none so far) and **declared** ones (S117's Reading B).

## Tests to give

For each: set-up, expected outcome, control, what counts against, cost in CPU-hours, new C++ or not.

1. **A minimal outside-input test**: the cheapest set-up in which a regularity the selector does not contain could be learned; and the criterion that would show it was.
2. **Learning within a life**: a pattern that varies between generations but holds within a life, against a pattern fixed across generations (expected, from the note: learning against reflexes). What would count against Avida being able to host this without a rebuild?
3. **An object layer**: can a state grid, or a small patch, give persistent things with displacement and occlusion, so that a program could be surprised in D12.7's sense? A thought test with a criterion is acceptable.
4. **For each meaning**, one line: Avida as it stands, Avida with a small patch, or another environment, with the observation that would change that line.

## What to return

1. **For the owner** (at most 150 words, no jargon): whether Avida is the right environment, for which meaning of knowledge, and what it would need.
2. **Your hypothesis** and what would count against it.
3. **The criteria**, one per meaning.
4. **The input inventory** (now; could be given; cannot without becoming something else), with file and line.
5. **The tests**, each as specified.
6. **Options** for other platforms with costs; no choice.
7. **What you ran**, or "nothing run". 8. **Sources**, checked or from memory.

End with the line END OF REPORT.
