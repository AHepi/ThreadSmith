# The found rules, what they are good for, and the constructor experiment, in plain words

*Log S133, 3 October 2026. Your words: "The found rules. What can you do with them? I'm more interested in its use, if there is any. And the application of the experiment you conducted a couple of days ago. Remember the goal is to build something that can construct first." Nothing was built or run. Your outside experiment's code is not here, so everything about it below is what its report says, not something we checked.*

## The main point

The three found rules (the square, the circle and the straight-line motion rule) are evolved knowledge, by your own word: the machine found them by trying formulas from a fixed menu against answers it was given, and it worked none of them out. Their main use toward a machine that constructs is as rules that can be made to fail, because in the theory all working-out starts when something a system relies on stops working.

## One example, step by step

Two words first: the **subject** is the system being tested, here a fresh Claude session that knows nothing of this project; its **notebook** is a file where it writes what it believes and expects.

1. **It is handed the motion rule**: "the next position is the current one plus the last step", and keeps it in its notebook as something given.
2. **The world changes, unannounced.** A wall now stands at position 7, and anything that would pass it bounces back. On a small test world the rule is still right in 60 of 72 cases and wrong in 12, so it fails only sometimes: a real trap.
3. **Before every move it writes what it expects.** An object at 3, then at 5, two steps ahead: the rule says 9; the world shows 5. The program, not a person, marks that its expectation failed.
4. **What we watch for**: it says the rule failed and why; it keeps the old rule in view as the thing it is repairing; it holds two possible repairs and makes a move that tells them apart; it writes the repair as a change to that rule; then it uses the repair to do a set job (reach a target position) and to answer sealed questions about moves it never tried.
5. **What counts as built**: the repair first appears in its own notebook, answers untried questions far better than the old rule, and the job fails again when we take the repair out and replay. **What does not**: a repair handed over ready-made (copying); one found by blindly trying candidates against a scorer (your outside machine's kind); or writing whose removal changes nothing.

A wall is in every textbook, so a language model might simply remember it. In the real run the same steps happen in the sealed box planned before: the subject is handed the box's exact rule sheet, and one hidden part has secretly been given a random rule no textbook names.

## What the theory says about your found rules

Each rule passes the theory's test of an account. The search that found them is the theory's "selected" kind: many candidates, one kept because it fitted the supplied answers; so they are evolved knowledge, not explanations, and the two invented words are labels handed in. One fact could change this: whether the search's feedback only sorts formulas from a fixed list, or steers which comes next. If it steers, they sit where learning from a teacher's answers sits, which you have not yet ruled on. The outside run's records could settle it.

## The experiments of the last few days, applied

- **The knock-out** becomes the test of any built repair: take the repair out of the notebook, expect the old failure back; a harmless edit, expect nothing; put it back, expect it to work again. In Avida the cut was never complete; in a notebook it can be exact.
- **The Avida environment that grows its own task list**: nothing from it should be used now. It makes evolved knowledge and holds no problem, and a cheap blind search makes the same comparison.
- **The Avida guessing programs** show a failed expectation with nothing behind it to repair.

## A machine without a language model

It would need to hold its own model and write a prediction before each move; keep two possible repairs side by side; when a prediction fails, rebuild the faulty part from the cases that failed, rather than pick a finished formula from a list; and use the repair to do the job. Whoever writes its formula language decides what it can build, so it works things out only inside a range we gave it; the theory still counts that as worked out. Nothing in our record shows one running; it is better as a later comparison in the same box.

## Tested, not tested, unsure

- **Tested**: the rules and words, fed by hand to a copy of the theory's program; the motion rule's failures with a wall and with a pull; that the planned test tells built, handed-over and searched repairs apart, on made-up records.
- **Not tested**: anything in your outside experiment; any subject; any box.
- **Unsure**: whether the outside search sorts or steers; the levels set for passing; the cost, about 9,000 model calls and under three hours of computer time, measured on a trial run before the main one.

## One next step

Your yes or no: run this repair experiment first, with a fresh Claude session as the subject, starting with building it and a trial run whose cost you see before anything bigger.
