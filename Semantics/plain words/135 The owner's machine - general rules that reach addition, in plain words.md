# The owner's machine: general rules that reach addition, in plain words

*3 October 2026. Your words: "I wanted a set of general rules that could be run autonomously to recognise objects, understand displacement, understand object permeance, have a general notion of amounts of objects, then represent addition with those rules."*

## The main point

We built it. A small program lives in a 16 by 16 grid of moving coloured blobs and a grey screen that comes down and lifts. It sees only the picture and runs on its own; the world makes up its own scenes, so nobody writes one by hand. We handed it four general rules. With them it tried to predict how many things would be behind the screen when it lifted; where that failed, it built a rule for addition itself, from its own record. **Addition was not handed in: the machine built it, but only from a menu of possible rules that we wrote.**

## The four rules we handed in

1. **Recognise objects**: a patch of one colour is one thing.
2. **Displacement**: a thing seen a little further on is the same thing moved, and should keep moving the same way; if not, the machine notes a **violation** (a broken expectation).
3. **Object permanence**: a thing that goes behind the screen is still there and should come out where its path leads. The machine can follow at most three hidden things one by one.
4. **Amounts**: it counts the things in a place or a group, and says whether one count is more, fewer or the same as another. It cannot add.

## One example, step by step

One blob sits on the stage. The screen comes down over it. One more blob comes down from the top and goes behind the screen. Then the screen lifts on just one blob.

- Rule 1 sees each blob; rule 2 follows the second one down to the screen.
- Rule 3 says both are still there, behind the screen.
- Rule 4 counts: one before, one added; two being followed.
- The machine expects **two**.
- The screen lifts on **one**. The count is fewer than expected: the machine notes a violation, which is what the infant studies call surprise. On two it notes nothing; on three it notes a violation again.

The four rules alone pass this test: following each thing is enough for small numbers. Addition is needed when there are more than it can follow.

## How it built addition

With four or five behind the screen, following one by one failed: it could hold only three, so it kept expecting three. It kept a record of every scene: how many before, how many added, how many came out, how many it was following, how many it counted at the lift. After a wrong guess it worked out, from its own mistakes, which rules on a menu of 405 ways of adding and subtracting those counts would put every wrong guess right without spoiling a right one. At first ten fitted, so it said "I can't tell yet". By the fifth record one was left: **after = before + added − taken away**. It kept that rule and used it from then on.

On 300 new scenes, with colours, sizes and amounts it had never seen (up to 9 + 5 − 4), it expected the right number every time the world was honest (157 of 157) and noted a violation every time the world cheated (143 of 143).

## The five rungs

- Recognise objects: **handed in**
- Displacement: **handed in**
- Object permanence: **handed in**
- Amounts: **handed in**
- Addition: **built** (by the machine, from a menu we wrote)

## What the knock-outs showed

- **Permanence switched off**: the addition rule failed whenever something was already behind the screen (right in 17 of 157, only the ones that started empty). Addition rests on permanence.
- **The addition rule taken out**: the machine went back to following things one by one and failed again with more than three; it was even fooled when two and two lifted on three.
- **A pretend removal** changed nothing. **Putting it back** restored every answer.

## Found or built?

A second version simply took the first rule on a fixed list that fitted. It grabbed a wrong rule for a moment, and what it held depended on the list's order. The built version did not change with any order. One honest catch: it gives exactly the same answers as a version that tries all 405 rules and keeps whatever fits; only how it got there differs. Whether that counts as worked out is still your question from last time: is a rule a machine works out for itself, inside a menu its builders wrote, worked out or only found?

## Tested, not tested, unsure

**Tested**: the four rules; the infant-style tests; building; new amounts, colours and sizes; the knock-outs; the order of the menu; pairs of scenes ending on the same picture with different right answers (the machine 100 of 100; anything reading only the last picture and the time, at most 16).

**Not tested**: anything about real infants; noisy pictures; the machine making its own menu, its own rules or its own tasks; it finding a new question.

**Unsure**: whether working out from a menu counts as building in your sense; we chose the limit of three that made following fail.

## One next step

Take away the menu of 405 rules and give the machine only "one more" and "one fewer", so that it would have to build adding out of counting on, one step at a time.
