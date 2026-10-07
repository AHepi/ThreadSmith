# Sources: the shared context of the S123 briefs

*Written by Claude on 2 October 2026 (log S123, decisions S77, S78, S79). The context common to the four S123 briefs, updated from S121's: the S122 results (Astra's four timing replies, checked), the owner's words S76 to S79, the Pinker research (log S124), the assessment written for these briefs (`results/S123 What knowledge could mean in Avida - how best to find out, and whether the trajectory is sufficient.md`), with its candidate meanings of knowledge, its transports and its six rival hypotheses. Each brief carries a shorter version of this below its line. The owner's Avida terms table is copied unchanged from `records/Semantics - Avida terms, given by the owner.md`.*

---

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

> "Shit there's also a lot of context to be added from Steven Pinkers books: How the mind Works, and Learning and Cognition. I just realised you don't have this info anywhere, and it's essential. So research agent first, then the one I suggested." (S79; the books themselves were not read: the note attached was built from Pinker's papers, interviews and other published sources)

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

## Avida's inputs, in more detail (read at commit 47f13dad)

- Three numbers per cell, from Avida's own random generator with top bytes 0F, 33, 55 (`cEnvironment::SetupInputs`, `main/cEnvironment.cc` 1252-1294), set when a program is placed in a cell (`main/cPopulation.cc` 1365) or, if `RESET_INPUTS_ON_DIVIDE` (default 0, `main/cAvidaConfig.h` 382) is set, when its parent divides (`main/cPopulation.cc` 916); `IO` outputs a register and reads the next of the three in rotation (`cpu/cHardwareCPU.cc` 4188-4201).
- Specific inputs and a random mask by event (`SetEnvironmentInputs`, `SetEnvironmentRandomMask`; `actions/EnvironmentActions.cc` 999-1039).
- Resources with inflow, outflow, periodic and seasonal schedules and gradients (environment file and events); read by `sense` and `collect` instructions (`cpu/cHardwareCPU.cc` 241-265), which are not in the heads set used so far.
- Messages between programs (`send-msg`, `retrieve-msg`, `cpu/cHardwareCPU.cc` 583-584).
- State grids loaded from the environment file (`LoadStateGrid`, `main/cEnvironment.cc` 1041, 1198) with `sg-move`, `sg-rotate-l`, `sg-rotate-r`, `sg-sense` (`cpu/cHardwareCPU.cc` 330-333) and a path-traversal task (`main/cTaskLib.cc` 314, 3446).
- Pay changed during a run by events (`SetReactionValue`, `SetReactionValueMult`) or by a driver between pieces (S113, S122).

Claude's reading: none of these carries information about anything outside Avida's own rules; all are made by Avida's code from its seed or written beforehand by the person setting up the run.

## The patches so far

- **S119 reply 01, `ANTICIPATE_MODE`** (five C++ files, off by default; reproduced exactly in S120): each program reads a private stream from a designer's rule (random; one number repeated; plus one each read; repeat then switch to plus one at a set update); a task pays an output equal to the next number to be read. Pilot: "add one" learned by 95 in 100 programs within 20,000 updates; at most 3 in 100 unpaid.
- **S121 reply 02, history tasks** (applies to clean 47f13dad; reproduced byte for byte in S122): frames of marked events (X, A, B, C); tasks order, interval, sequence; a pair pays only if both its frames are answered right. Flaw: counting reads alone earns order on every pair, sequence on 4 pairs in 5, interval on 1 in 2. Pilot: in the paid interval run, 14 of the 50 commonest sequences (71 programs) earn more than any read-counting rule, by keeping where the A came within a frame; none in unpaid runs.
- **S121 reply 01, a temporal selector** (a Python driver between pieces of 1,000 updates, stock Avida): traces, adaptation, latches, rebound, coincidence, sequence and expectation units; pay 18 doublings over 66 detectors. Pilot: 2-6 capabilities common in 20,000 updates, as with its memory wiped; no latch ever set. Its pay after two different histories ending in the same present differs (the minimum test for a selector with memory).

## Candidate meanings of knowledge (from the assessment)

- **K-CT** (Marletto): resilient information; the elimination test; the abstract catalyst (copiable, enabling a transformation, perpetuating itself); in use, knowledge "of" features of an environment.
- **K-D** (Deutsch): information that tends to cause itself to remain in a suitable environment, arising by error correction; two kinds, adaptive (non-explanatory, limited reach) and explanatory (reaching unmet cases).
- **K-O3** (the owner, S59, S76): the three properties, and a causal effect on the surroundings, "Not just other little programs, but Avida itself".
- **K-P** (Pinker, via the note): accurate representation used in inference, learned within a lifetime by a learner whose constraints were selected.
- **K-Sem** (the semantics, which has no "knowledge"): representation (a faithful transport with a selected or constructed history); being an explanation (Account and not declared); created explanation (EX).

## Transports learning from external data needs (from the assessment; to criticise)

| | Transport | From | To | In stock Avida |
|---|---|---|---|---|
| L1 | data | the world's process (a source the selector does not contain) | the program's input states | present, but the source is Avida's own generator |
| L2 | output and action | the program's states | outputs; actions that change the world | outputs checked by code; no loop through the data source |
| L3 | model | the program's organization | a content about the world | a circuit from inputs to an output; representation only under Reading A, and of Avida's rule |
| L4 | selector | the material selected | the execution environment's standard | the checking code (grade 1 or 2) |
| L5 | second channel | the same events, as perceived | the model of the situation | none |
| L6 | prior link | the learner's categories | its hypotheses | none |
| L7 | constraint on candidates | all mappings | the population | all sequences reachable by copying with changes |

## Six rival hypotheses (from the assessment; each with what would count against it)

- **H1, the circuit, of Avida's own rules**: the knowledge is the instructions the elimination test picks out, and it is knowledge of Avida's instruction meanings and checking code only. *Against*: a capability right on unseen cases more often than the population's other survivors allow; or one whose loss and recovery depend on the selector's state.
- **H2, the coupled system**: selector and population together hold it. *Against*: no difference between kept and wiped selector state in transplant tests at pay that makes capabilities common.
- **H3, not knowledge without an effect on the execution environment itself** beyond channels written for that effect. *Against*: removing a circuit changes what the execution environment selects for through no channel written to carry that effect (E3, below).
- **H4, adaptive, never explanatory, in Avida**: nothing constructs. *Against*: reach beyond what the history and population fix; or any history meeting "constructed".
- **H5, learning begins only with an outside source**. *Against*: no held-out gain from an outside stream; or no difference from a matched stream made by Avida's own generator.
- **H6, construction within a lifetime is the threshold**, on selected material. *Against*: within-lifetime learning whose binding is only selected; or "constructed" met in stock Avida.

## A scale for effects on the execution environment (offered for criticism)

**E1**, named effect: the code names which capability changes which part of the execution environment (S113's growing list). **E2**, generic channel: any capability can affect a shared part without the code naming which (resource stores; a selector reading the shares of all tasks). **E3**, unnamed: a change in what the execution environment selects for, through no channel written to carry that effect. Two readings of "Avida itself" (S76), both open: its rules (the C++, fixed during a run) or its state.

## Grades of naming a target (use them strictly)

| Grade | Meaning |
|---|---|
| 1, named exactly | A list of functions, each paid or required. |
| 2, named one level up | A class or rule is written down ("any of these 251", "whichever is rare"). |
| 3, truly unnamed | No checking code computes what counts as a solution; the standard comes from something that itself changes. |

## Left open by the owner

Offer options, never decisions, on: whether a task list written by people counts in the history of the programs it selected (Reading A or B); what knowledge is; whether a fixed way of selecting counts as an instinct; whether a driver between pieces counts as part of the execution environment; what "Avida itself" means in S76; which environment to go on with; which costly runs come next.
