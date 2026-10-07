# Designing the test a missing condition calls for

A missing condition is only useful once it becomes a test that could come out against the claim. This file says how to build one.

## 1. Write the prediction first

- **Before running anything, write:**
  - what the claim predicts;
  - what the rival predicts;
  - the result that would count against the claim.

  Date it. If the work matters, fingerprint the file: a code computed from its contents, which changes if anyone edits it.
- **Write the pass mark as a number or a plain condition.** "Better" is not a pass mark; "at least 3 fewer checks on 6 of 8 lesson draws" is.
- **Say what result would make you stop** and say the claim is wrong.

## 2. A ladder of rivals

For a comparative or credit claim (A beats B; the new part is why), run the claimed part against rivals, from weakest to strongest. A claim that only says "it runs" or "it completes" needs no ladder.
1. **Does nothing:** no change, "stays where it is", always the majority answer.
2. **Plain rule:** a fixed formula, a keyword rule, the obvious heuristic.
3. **Same supplied parts, without the claimed part:** for example, the supplied physics with no learning, or the old model with the new data.
4. **Strongest fair rival:** the best alternative someone competent would propose.

The claimed part earns credit only above the highest rung it beats. If rung 3 was not run, the claim of credit is *held if* that rung would lose.

## 3. The innocent neighbour

Every detector, metric or test must be run on two things:
- the case it is meant to catch;
- that case's nearest innocent neighbour, which is like it in every way except the property being tested.

A test both of them pass, or both fail, is measuring something else.

Examples:
- sincere sentences with the same punctuation as sarcastic ones;
- a crash test with the race removed and the cache still on;
- a scene outside the supplied models whose first seconds look exactly like a scene inside them.

## 4. Controls that are not the same by construction

- **A known-answer test of the instrument.** Before trusting a harness, scorer, scanner or metric, run it on a planted fault or a case with a known answer. It must catch it.
- **Work out each control's behaviour from its definition before running it.** If two controls must agree, keep one.
- **Run a null control:** the same world twice, with a change that should not matter, to measure how big a difference arises from nothing. Check the null control is null: a chaotic system can turn a tiny change into a large one.
- **Run a positive control:** a case built to be easy, to show the test can detect a difference at all.

## 5. Draws and size

- **Count independent draws, not rows:**
  - seeds;
  - training sets;
  - sites;
  - people;
  - makers.

  Rows from one draw are not independent.
- **Compare case by case** and report wins, losses and ties. Then ask how likely that count is by chance. A sign test is enough for small numbers.
- **For "zero events", say how many trials** would be needed to expect at least one at the known base rate. Run that many with the suspected cause present.

## 6. Change one thing

- Vary only the factor under test.
- If the change needed to test it also changes other things (timing, load, position, who wrote the data), test each of those on its own too. Or find a change that alters only the factor: remove the race but keep the cache.

## 7. Cases where the event was not observed

- Before counting a case as support, check that the event the claim is about happened inside the observation. Examples: the meeting happened before the clip ended; the user stayed long enough to be counted; the sensor was on.
- Cases where it did not happen are outside the claim. List them separately.

## 8. After the test

- **Keep the first result as it came.**
- **Every later change to the test is a patch.** Say which layer it changed (the claim, the rig, or the inputs) and what it gives up.
- **If the falsifier fired, say what you are changing:** the claim, the background assumptions, or the instrument. Say why that one.
- **If the falsifier did not fire, ask whether it could have.** If the test could not fail, it was not a test.
