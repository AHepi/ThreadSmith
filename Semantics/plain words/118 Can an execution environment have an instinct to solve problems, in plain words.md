# Can an execution environment have an instinct to solve problems? In plain words

*Log S118, 1 October 2026. Your questions: "can you give it an instinct to solve a problem without specifying exact target goals?" and then "The execution environment is the thing I want to test. Not the individual programs. The environment is the thing that does selecting. Just as an autonomous agent does selection."*

## The answer

Partly yes. An Avida execution environment can choose among programs the way an agent chooses among ideas. It can keep "whatever works" without being told which particular answer it wants, and the programs then come to solve many problems it never named. But it still has to be told what kind of thing counts as working. In the time we gave it, it found only fairly easy things and showed no sign of reaching for harder ones on its own.

## One example, step by step

A word first. In Avida, a **function** is a fixed rule for turning the three numbers a program is handed into the number it hands back. "Flip every bit of the first number" is one function. Avida can recognise 251 of them.

1. **What the execution environment was told.** Only this: "Any of the 251 functions counts, all the same. But a function that many programs already do counts less." That was the whole instruction. It was not told which function is wanted, or which is harder, or in what order to look.
2. **How it selects.** A program that hands back the result of some function gets more running time, so it copies itself faster than its neighbours. A program doing a function that most others already do gets less extra time than one doing a function that few do. Copies are not perfect, so new variants keep appearing, and the execution environment keeps favouring the ones that do something, especially something uncommon.
3. **What it started with.** A single program that copies itself and does nothing else: no function at all.
4. **What the programs came to do.** By the end of the run, the population had come to do between a dozen and twenty functions commonly, many of them using all three numbers at once. A typical program did several of them, and in one try nearly all twenty. None of these functions had been named.
5. **Where it stopped.** The functions found were the easier ones. In one of the three tries, nothing new became common in the second half of the run. An execution environment told about all the functions and how hard each one is did better in two tries out of three and worse in the third. One told only a short list did clearly worse.

We also tried a second execution environment that pays nothing at all but refuses to let a program copy itself unless it has solved something, anything. The programs survived the change, and soon nearly every program that could copy itself was solving something. But they settled on the two easiest functions and stayed there. Making solving a condition of survival set a floor. It did not create a drive.

## What this means for your idea

Your picture holds in one respect. The execution environment does act as the selector, and it can select for "solving" without a list of exact targets. Saying "something useful, and preferably something new" is enough to get many solutions it never asked for.

Two limits showed up. First, the execution environment still contains a written-down idea of what counts: "a function of the numbers". It does not name the target, but it names the kind of target. Second, its way of choosing is fixed. It never changes what it looks for in the light of what it has seen, and that may be what "progressively learn how to do new things" needs. The things it got were variety, not growing difficulty.

## What was tested, what was not, what is unsure

**Tested:** two execution environments, three tries each, in the ordinary Avida program with no changes to its code: "any function, common ones count less" and "solve something or you cannot copy".

**Not tested:**
- An execution environment whose sense of what counts comes from outside itself. One example is other evolving programs acting as judges, which Avida can do but which needs a different setup. Another is rewarding programs for guessing what the world will do next, which needs new code.
- Longer runs.
- More tries.

**Unsure:**
- Three tries are too few to say whether "any function" really does worse than naming every function with its difficulty. The tries overlap.
- The runs were shorter than earlier ones, so we do not know whether the variety would have kept growing.
- Whether a fixed way of choosing counts as an instinct in your sense is your call, not ours.

## One next step

If you want to go on, the step that tests your idea most directly is an execution environment whose standard is not written inside it: one that rewards programs for anticipating something the world does that the execution environment itself never works out. That needs a small piece of new code in Avida and a few hours of computer time. Nothing is started until you say.
