# S118 An instinct without a named target: addendum after the owner's correction (S72), written before the pilots were read

*Log S118, decisions S71 and S72. Written 1 October 2026 by the second Opus 5.5 agent of log S118 (one agent per job, S56, S68), which continues the first S118 agent's work. The first agent was stopped by Claude at about 10:21 UTC because the owner corrected how S71 had been read; its plan (`results/S118 An instinct without a named target - how it will be tested, written before running.md`, commit d1ecec9) and its scripts (45eafb9) stand and are not edited. The two pilots were started at 10:13 UTC under a detached driver and were still running when this addendum was written and committed. **No pilot output (no log line beyond "started", no Avida data file) had been read when this was written.** Nothing in the theory, Part A, Part B, the S110 to S117 files, the plan, the decisions, the terms file or `authority/` is touched. S117's open reading stays open.*

---

## 1. The owner's correction

**S72, the owner's words:** "Oh. The execution environment is the thing I want to test. Not the individual programs. The environment is the thing that does selecting. Just as an autonomous agent does selection."

It restates S63: "The execution environment is an important clue. Looking inside the machines is the wrong direction. The question is, what kind of execution environment can use these machines to progressively learn how to do new things..."

**The question, as now read.** Can an Avida execution environment, the selector, have an instinct to solve problems: a way of selecting under which the program population comes to solve problems, without the execution environment being given exact target goals? The execution environment plays the part of the autonomous agent; the Avida programs are its material, what it selects among. The instinct, if there is one, is the execution environment's, not the programs'.

## 2. What is narrowed

**The term.** The plan's opening paragraph glossed an Avida execution environment as "what is paid for, by how much and from what resource". That is narrower than the owner's term (S61: "The simulated computational environment in which programs execute"). From here on, "execution environment" is used in the owner's sense: the whole simulated world, including what it pays for, what it requires before a copy is allowed, how it hands out processor time, how it copies programs (and so where copy errors come in), the size and layout of the world, and its resources. The plan's pay rules are one part of it; P2's copying requirement is another part, and was already inside the plan's experiments.

**The definition.** The plan's section 1 defined an instinct as "a standing pressure, built into the Avida execution environment or into the Avida programs". It is narrowed to:

> An **instinct of an execution environment** is a standing way of selecting, built into the Avida execution environment (not into the Avida programs), (a) that does not name which input-output function or which answer is wanted, (b) under which the program population comes to perform functions of the numbers handed in (solve problems) that no part of the execution environment singled out, and (c) that keeps acting: it is not used up once one function is found.

Conditions (a), (b) and (c), and the three grades (named exactly; named one level up; truly unnamed), are unchanged. A drive carried inside the programs themselves (for example a program that judges other programs by a rule it carries) is not an instinct in this sense; it counts only in so far as the execution environment's own way of selecting is what makes such programs last.

## 3. What this changes in how each mechanism is read

Every row of the plan's table except row 9 (in part) is already a rule of the execution environment, so the narrowing removes little; it changes the subject of the sentence, from "the programs are given an instinct" to "the execution environment selects in this way".

| Plan row | Mechanism | Whose selecting it is, read in the S72 sense |
|---|---|---|
| 1 | Pay for any function of the numbers | The execution environment's. Candidate instinct, grade 2. |
| 2 | Pay for any output | The execution environment's, but it selects for no problem; not an instinct to solve problems. |
| 3 | Pay for output that depends on the input | The execution environment's. Candidate, grade 2 (bitwise part = row 1). |
| 4 | Rare pays more | The execution environment's. Its preferences shift with what the program population does, by a fixed rule written down once. Candidate, grade 2. |
| 5 | Prediction of the world | The execution environment's (needs C++). The one route where the selector's criterion comes from outside its own checking code (what the world does next). Grade 3 at the level of the function. Not tested. |
| 6 | Copy only after solving something | The execution environment's: a copying rule, not a payment. In the agent picture, the selector refuses to keep any idea that does not solve something. Candidate, grade 2. |
| 7 | Energy model | The execution environment's. Not tested. |
| 8 | Foraging | The execution environment's; poses no problem of computing. |
| 9 | Parasites; programs judging programs | Split. The parasite matching rule is the execution environment's, but the function wanted at any moment is set by its own material (the hosts). Read in the S72 sense, this is an execution environment that uses part of its material as its judge: still the execution environment's instinct, grade 3 for which function, grade 2 for the class. S115 reply 02's carried judging rule is the programs', so it is not an instinct of the execution environment in this sense. Not tested. |
| 10 | Deme competition | The execution environment's: it selects groups. Not tested. |
| 11 | Stock tasks with a stated target | The execution environment's, named exactly; not an instinct. |
| 12 | Limits on tasks | The execution environment's, one level up at best. |

## 4. What this changes in how each pilot is read

Both pilots are execution environments, so both remain direct tests of the question as corrected. Read in the S72 sense:

- **P1 (any function, rare pays more)** is an execution environment that selects by "anything that computes some function of the numbers counts; whatever is rare counts more". The test is whether this selector, told no function, makes the program population come to compute many functions, and keeps doing so.
- **P2 (solve something to replicate, nothing paid)** is an execution environment that selects by "nothing is kept unless it solves something", with no preference among solutions. The test is whether this selector makes solving universal, and whether it does more than set a floor.

**Readings in the plan's section 5 (for and against).** None changes. The thresholds, comparisons, seeds and updates stand as written. Only the wording of the answer changes: where the plan says "Yes, at grade 2", the answer is now "the execution environment has an instinct at grade 2" (it selects for solving without singling out a function, but its checking code writes the class down), and "Yes, truly unnamed" still cannot be reached by these pilots.

**One reading made explicit, not new.** In the agent picture the execution environment also produces the variants it selects among, since copy errors come in when it copies programs. Both pilots keep S113's copy error rate, so this part of the selector is the same in every compared execution environment; the pilots vary only how it selects.

## 5. Left open for the owner

- Whether an execution environment whose criterion is fixed (P1's rule, P2's rule) but whose effect shifts with the population (P1) counts as an agent "selecting" in the owner's sense, or whether the owner means a selector whose criteria themselves change (S63: "progressively learn how to do new things"). Recorded, not decided.
- S117's open reading (whether a task list and its checking code, written by people, count as part of the history of the programs they selected) stays open.
- Whether grade 3 routes (prediction, which needs C++; parasites, stock) are worth a run is for the owner.
