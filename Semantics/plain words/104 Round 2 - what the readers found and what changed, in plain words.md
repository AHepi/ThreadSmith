# Round 2: what the readers found and what changed. In plain words

*A note first. Written on 28 September 2026 by a Claude subagent, for you. It uses none of the words you asked to be removed, except inside quotations. The full record is "Semantics/results/S104 Round 2 - what the readers found and what changed.md".*

---

## 1. What happened

Round 2 changed 43 small places in the theory and added no new prose: the words outside its formulas went from 15,611 to 15,409. Where the words were vague, the maths now says exactly what they mean, and a program checks it. Three questions are left for you, and a fourth comes back to you because it is about what counts as an argument.

Before the round, the theory was written out as mathematics, called here the maths: each definition as a formula beside its sentence, and 110 claims the formulas let one check. A program builds many small made-up examples and checks each claim on them. Where the words leave something open, the maths had to choose, and each such choice is written down as an invention, as you asked: "if implementation forces invention, that needs to be recorded."

Mimo and GLM each got the maths beside the words, in 17 pieces, and were asked where the two part company. All 34 replies came back. The outside cross-examination and the small experiment you sent were read beside them; the workspace you sent added nothing the maths had not already tested.

## 2. One example: found by trial, or worked out

The theory says the link between an explanation and what it explains comes about in exactly one of three ways: found by trial, worked out, or declared. Picture a key for a lock. Found by trial: a locksmith tries blank after blank and keeps the one that turns. Worked out: the locksmith measures the lock and cuts a key to the measurements. Declared: someone hands you a key and says "this opens that lock".

By running the program, the critical review found a history like this: a key cut to the measurements that, at the same moment, came out of a round of trials. Under one way of reading the maths, that key counted as both found by trial and worked out, though the theory says exactly one.

The fix adds one condition to "found by trial": nothing in the key's history worked it out on purpose. So the measured and cut key counts as worked out, whatever trials also happened. The program then checked all 4,680 short histories of up to four steps: none counts as both, under any of the four ways of reading the maths tried.

## 3. Why maths and code, not more words

The round began with 78 checkers, one for each group of sentences, each to write new wording. You asked: "Are the checkers constructing code or doing math? Because more prose is self defeating", and then: "This only needs maybe 3 checkers."

The run was stopped; its eight decisions, four finished and four begun, are kept as a record. Three checkers then took one third of the theory each and said, for each point raised, whether it holds against the maths, holds against the words, rests only on an invention, or does not hold. Each fix went into the maths and the program, which was run again. The words could only lose a phrase, have a phrase replaced by its formula, or get a pointer to the formula. One agent put the three thirds together; a critical review by Fable raised 16 objections; one more checker decided them.

## 4. What changed

- **43 changes on 32 of the theory's 632 lines.** 32 replace a phrase by the formula that says it exactly; 10 add a pointer to a definition in the maths; one sentence is gone. They are in a new copy, the round-2 copy (file 104, like this note); the round-1 copy is unchanged.
- **The sentence that is gone** said the link is entered by its author. Read as written, it made every link declared by whoever wrote it down, even one a computer search had found by trial, as in the small experiment you sent.
- **A circle is cut.** The theory defines "represented" partly through "worked out", and "worked out" partly through "represented". Tried by program, the words as they stand and two ways of cutting the circle each broke at least one of the theory's own sentences; one left a first ever working-out representing nothing. A fourth way, found in this round, broke none of the four sentences checked.
- **43 new inventions** are written down. Where a change to the words writes one in, the change says so.

## 5. What the program showed

A counterexample is a small made-up example on which a claim fails.

| | claims | hold | counterexample | not tested |
| --- | --- | --- | --- | --- |
| before the round | 110 | 87 | 12 | 11 |
| after the round | 113 | 103 | 3 | 7 |

Each counterexample left rests on an invention of the maths or on how the claim itself was worded, not on the theory's words. "Hold" means only that no counterexample turned up among the small examples tried.

## 6. Your questions

Round 3 does not wait on these; they wait for you.

1. **Is a declared link enough?** A student copies the pendulum formula from a textbook and writes "this stands for the pendulum". If it passes all four of the theory's tests for an explanation, is it one, though its link was simply declared? One sentence of the theory says passing the four tests is enough; the theory's list of what would rule it out claims this only for links found by trial or worked out.
2. **Must the question change for something to be created?** An engineer designs a new bridge to a fixed brief. Can something be worked out there, or must the brief itself change along the way? The theory's opening definition asks for what the question covers to change; the rest of the theory uses the word for any stretch of work.
3. **Can a change from no answer to an answer be explained?** In still air a weathervane may point anywhere; a north wind makes it point north. Can anything count as explaining why it points north? The maths counts only a change from one definite answer to another; the other reading counts a change from no answer to one, and without it such a question could have no explanation at all.
4. **Is a single claim an argument?** "Perpetual motion is impossible", used alone to rule out a design for a machine that would run for ever. The last checker said no: the theory calls an argument a set of steps that start from premises, and you wrote that an argument is "something that can be strung together into a coherent structure". The other side: you also wrote that this claim alone "is enough to trigger a conflict". What counts as an argument is yours to say.

## 7. What was not tested, and what is unsure

- **No outside reader has seen** the round-2 copy or the new maths.
- **One checker for each third,** and one for the review's objections. The fourth way of cutting the circle is that checker's own, and no one else has read it. It needs every history to have a beginning: no endless chain of earlier and earlier events.
- **The program tries small made-up examples only.** Seven claims are not tested at all. The part of the theory where predictions live is not built in the program. In two claims, the earlier events of a history are still set by hand.
- **The everyday cases were not read again** on the round-2 copy.

## 8. Were there moves left?

Yes: 115 changes, to the maths and to the words. The rounds end only with a round in which nothing changes.

## 9. The next step

Round 3: the round-2 copy and its maths go to GLM alone, up to four calls at once, each with a slightly different job, with the rule for reading the replies written and saved first. Mimo is left out, as you said: "After this run, remove Mimo from workflow".
