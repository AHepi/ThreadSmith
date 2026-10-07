# How the Avida work and the semantics relate, in plain words

*Written on 1 October 2026 by one Claude agent, for you. There is no GLM check of this work, as you asked. The main thing to look at is the map page, "117 How the Avida work and the semantics relate - the map.html", in this folder: it shows each group of the semantics, what in Avida sits beside it, and, for everything that does not line up, why, with an example. This page is written around the map, so it stays short. It uses your Avida terms. Nothing in the semantics was changed.*

---

## 1. What happened, and what it means for your idea

You asked whether, and how, the Avida work lines up with the semantics exactly. Every piece of the semantics was taken one at a time: its definitions, its claims and its named terms, 284 pieces in all. For each, the question was: is there something in Avida in the same place, and does it behave as the semantics says?

**The answer is: in part, and the line between the two halves is sharp.**

- **Where the semantics describes things, their parts, changes and selection, Avida lines up with it**, often exactly, and in several places with new numbers computed on Avida's own records. 114 pieces line up exactly.
- **Where the semantics describes explanation as something done** (holding a problem, arguing, criticising, building something new, using it), **Avida has nothing.** No Avida program holds a problem or criticises anything; all the choosing is done by the execution environment, and all the asking and testing by the people studying Avida.
- **At the one point where the two meet, the semantics' own answer flips.** Does an evolved Avida program "stand for" the task it does, and could it count as an explanation of that task? The semantics' answer depends on one question it has not settled: whether Avida's task list and the code that checks it, both written by people, count as part of the history that shaped the program. That question is yours (section 6).

For your idea this means: Avida is a working example of the half of the picture the semantics shares with constructor theory (information that is copied, kept and selected), and no example at all of the half the semantics is about (explanation). This fits what the earlier record suspected: knowledge in Avida's sense and explanation may be different kinds of thing.

## 2. One example, step by step

**The program.** Among the programs studied earlier, the most common program doing the task NOT in one low-mistake run has 110 instructions and was carried by 44 programs in its population. Avida's step-by-step record shows what it does: it reads a number, copies it so the same number sits in two places, combines the number with itself using Avida's one combining instruction, and hands the result back. Combining a number with itself that way gives NOT of it, so the program does NOT.

**The definition.** The semantics has a test for when something counts as an explanation of a question. In plain words it asks five things:
1. each working part of the candidate matches a part of the target;
2. the candidate as a whole agrees with the target;
3. the candidate gives the target's answer under every change the question asks about;
4. the answer depends on the candidate's parts: take a part away and some difference in the answer is lost;
5. the question states which changes it covers.

**Does the program pass?** This was computed in a copy of the semantics' own program, with the target being the task as Avida checks it ("hand back NOT of the number you were handed") and the changes being the numbers the world hands in.
- **Taken as one block, yes**: all five hold.
- **Cut into its instructions, no**: the second condition holds but the first fails, because the task has no parts for the program's instructions to match. The semantics has a word for this case: the pieces do not match, though the whole agrees.

**Is it then an explanation?** Here the semantics asks one more thing: where the program's match with the task came from. If it came from variation and survival with nothing in its history standing for the task, it is "selected", and the semantics counts it as an explanation. If not, it is "declared", and it does not count.
- If Avida's task list and checking code are part of the world's rules, not of the program's history, the program is selected, it stands for NOT on the numbers the world hands in, and the semantics calls it an explanation. That goes against your own reading of Avida as the knowledge kind, with "the explanation kind" still to come.
- If the task list and checking code count as part of its history (they were written by people and they compute the task), the program is declared: it stands for nothing and is no explanation. That agrees with you, and with the first Avida study's observation that nothing in the programs refers to where the numbers come from.

The text does not say which. That is the first break on the map.

## 3. The main breaks, and why

These are on the map page, each with an example.

1. **Whether an evolved program stands for its task flips on one reading.** Why: in nature nothing writes the target down; in Avida people write it down in advance, and the semantics never said whether that counts.
2. **Avida's ablation is not the semantics' "taking a part away".** (Ablation: swapping an instruction for one that does nothing.) Why: the do-nothing instruction still does something; for example, when an unused read is swapped out, the next read takes its number, and the task fails for that reason. The semantics' taking-away leaves the part's values completely open. So your "required instruction" means, in the semantics' words, "a change at which the answer differs", not "a part the answer depends on".
3. **The earlier answer to "what is it?", the circuit, fails the semantics' test.** Why: the circuit is the path the numbers took; the test asks for the right answer at every ablation. The circuit gets 95 in 100 ablations right, but every ablation right in fewer than 9 in 100 program-task pairs, and in none of the programs doing EQU.
4. **In Avida, lasting does not require doing the task.** Why: Avida pays better for doing a task; it does not remove programs for failing. In the environment that pays for nothing, 3,600 programs lasted to the end and 11 did NOT.
5. **Everything about explanation as something done has nothing in Avida.** Why: no program holds a problem, makes or uses a claim, compares versions, or criticises; the world's withholding of pay is, in the semantics' own words, a signal, not a criticism.
6. **"Learning new things" in Avida is, in the semantics' words, selection, not creation.** Why: every new task came by a copying mistake that lasted; the semantics asks for something built with a target in view.
7. **Programs fail where the world never looks, but nothing is surprised.** In one growing-list run, 2,370 programs do NOT in the world's order of numbers; with two of the numbers swapped, only 34 still do. Why nothing is surprised: Avida programs predict nothing, and the world never changes its order.
8. **Avida's simulated world is exact; the semantics' physics never is.** Why: Avida's "physics" is a program.

## 4. What lines up

- **An Avida program is exactly what the semantics calls a thing with parts and changes**, and Avida's tasks are its questions; every one of them comes from a list written in advance, which the semantics calls a declared question.
- **What kind a part is depends on the changes you ask about.** Of 318 groups of programs that behave identically in the plain test, 302 came apart when one instruction's meaning was changed.
- **Selection leaves open what was never tested.** In 16 of 18 saved program populations, programs that all do NOT in the world's order part ways when the order changes; the semantics says exactly this.
- **Two programs alike now can be different things**: the two hand-built programs from Astra's fourth reply do the same today and become different things after the same change.
- **Parts that must go together, and parts that do no work**: a task done in two places can only be stopped by taking out a pair; the first program's 85 idle instructions are your "removable instructions".
- **Your three properties, "causes itself"**: whether the copying is the program's own, and whether "it" remained, depend on where the boundary of the system is drawn and what counts as the same system, as the semantics says. The program's instructions are inside; the world's rules are outside.

**What Avida shows that the semantics has no word for** (the last part of the map): copying itself, withstanding change, lasting by out-copying removal, a graded advantage, how widespread a capability is, pay that falls as more programs use it, the order in which problems are posed, what a program can become next, and a cost borne for another. The first three are your three properties: the semantics, as it stands, has no terms for them.

## 5. Tested, not tested, unsure

**Tested:** all 284 pieces, each against the Avida work; four computations: the circuit against the test of an explanation, on every single ablation of the earlier study (7.15 million); programs that behave alike, against changes of instruction meaning and of numbers; every saved population of the routine runs, in Avida, with the numbers in all six orders (about 100 seconds of computer time); four small cases in a copy of the semantics' own program.

**Not tested:** anything that needs new Avida code or new evolutionary runs; the further runs of file 115 that await your word; the parked Part B.

**Unsure:** many of the pieces that line up exactly were judged by argument from the records, not computed (60 of 114); the copy of the semantics' program used numbers one digit long, which is exact for these logic tasks but not for the arithmetic some programs use; reading the circuit as an explanation was done one way (an ablation stops the task when it hits every route), and other ways were not computed.

## 6. One next step

Your word on the open reading: **does a task list and its checking code, written by people, count as part of the history of the programs it selected?** If not, the semantics says Avida's evolved programs stand for their tasks and can count as explanations, against your reading. If so, it says they are declared and stand for nothing, with your reading. Nothing will be changed until you say.
