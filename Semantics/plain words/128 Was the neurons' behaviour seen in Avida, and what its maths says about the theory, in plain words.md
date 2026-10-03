# Was the neurons' behaviour seen in Avida, and what its maths says about the theory? In plain words

*For the owner, after log S128, 2 October 2026. Your question (S82): "Was it demonstrated in Avida or another environment? And given the math that describes it, can anything be derived from it that looks vaguely like anything in the semantics or its kernal?" "It" is the timing behaviour in your report on neurons. The full working is in `results/S128 The neuron mathematics against the semantics' kernel.md`.*

## The two answers

**Seen in Avida? Some of it, and mostly in the execution environment, not in the programs.** Our runs showed a fading trace, tiring, a switch that stays on (worked by my runner, not by Avida), and short memories inside programs (in specially changed copies of Avida). Astra's designed "switch" and "rebound" parts never acted. Within-life learning was seen only in other people's Avida work; resonance, bursting and the other firing patterns only in the report's own sources.

**Anything in the theory? Yes, more than vaguely.** Several things follow directly from the theory's definitions, and others have the same shape with a stated difference; the clearest are listed below.

## One example: the NOT store as a fading trace

A **fading trace** is a number that jumps when something happens and then shrinks by the same fraction every moment, so it remembers recent events and forgets old ones.

In the "common tasks pay less" execution environment, each logic task is paid from its own store, which programs use up and which refills steadily while a share leaks away.

1. **Avida's code.** Between uses, the gap between a store and its full level shrinks exactly as your report's trace does, losing about 63 in 100 of itself every 99.5 updates. The full level is 9,950, not the 10,000 the settings suggest.
2. **The earlier runs agree.** In the old runs about 3,200 programs did NOT and kept its store near 290. When we took NOT out of the programs (file 126), the store climbed to about 4,300 in 100 updates; when we put NOT back, it fell to about 275 within the next 100.
3. **Read backwards.** The store's movement then tells how hard it was drawn on: about 97 units an update, untouched. With NOT taken out, the draw fell to about a tenth. With NOT put back, it was between one and a third and two times normal for about 50 updates, as the programs spent what had piled up.
4. **The confirming run.** Nine stores started at chosen levels (290, 0, 4,300, 20,000 and others), in a world whose one program does no task, for 50 updates. Every store, at every update, landed within 0.06 of the prediction, as precisely as Avida prints. The store started at 10,000 fell towards 9,950. The simple rule a reader might assume was off by about 20 everywhere.

So the store is a fading trace of a task's use, and the drop in pay is **tiring**: a response that fades the more something is repeated and comes back with rest.

## What the maths gives in the theory

- **DERIVED**: whether a system needs memory depends on which changes the question allows: none, if no allowed change touches an earlier input.
- **DERIVED**: if the only allowed changes move events earlier or later, a fading trace shows only its window, the time it takes to fade below its threshold.
- **DERIVED**: a fading-trace detector is exactly the short-memory predictor in the theory's example of a hidden object: it fails whenever a gap outlasts its window, no tuning saves it, and what does is a part that does not fade, a switch that stays on.
- **DERIVED**: the theory's rule for how small errors add up gives exactly the gap between Avida's store and the simple rule: 20 after 51 updates, 50 at rest.
- **DERIVED**: a fading trace and a stopwatch that agree on every input are one explanation, until a change touches one and not the other, such as a clock only the stopwatch reads.
- **DERIVED**: learning within one life from a teacher's answers counts as built, not selected, under all three of your readings A, B and C from file 127.
- **LIKENESS**: a switch that stays on has the shape of a problem being open or solved, but carries nothing of what the problem is.
- **LIKENESS**: a program's copying builds up, "fires" at division and is reset, like a firing nerve cell, except that nothing leaks away.
- **LIKENESS**: NOT coming back after its store refilled looks like a nerve cell's rebound, but it happened across the whole population, not inside one unit.
- **Runs the other way**: your report says two histories that leave the same state cannot be told apart. The theory says where an explanation came from depends on its history even when the state is the same.

## What this adds to the open proposals

File 127's proposal about selection needs the theory to record when each case happened, not just that it did: useful on its own, needed if you accept that proposal. And one sentence: something happening twice is one change to a time-stamped input, not one change made twice. Proposals only; nothing in the theory was changed.

## What is unsure

The test written before the run allowed 0.05 of error; the largest difference was 0.059, from Avida's rounding, so by its letter the run neither confirmed nor counted against the rule. The "drawn on" figures are averages from a few printed numbers. Several of the report's sources were not opened. The teacher result rests on reading training as building.

## One next step

Your choice of A, B or C from file 127, now with one more consequence in view: under all three, learning from a teacher's answers within a life counts as built.
