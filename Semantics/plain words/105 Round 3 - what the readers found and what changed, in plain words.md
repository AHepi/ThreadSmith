# Round 3: what the readers found and what changed. In plain words

*A note first. Written on 28 September 2026 by a Claude subagent, for you. It uses none of the words you asked to be removed, except inside quotations. The full record is "Semantics/results/S105 Round 3 - what the readers found and what changed.md".*

---

## 1. What happened

Your four answers from round 2 were written into the maths, the program and a new copy of the theory. Round 3 gave that copy to GLM as four jobs at once. The fixes changed 13 small places on 9 of 632 lines and added no prose: the words outside formulas went from 15,388 to 15,322. Then your shop-sign answer took one test out of what makes something an explanation; that is being done now.

What it means for the idea: the words say more exactly what your answers say, and the program works out more from each case's history, not from typed-in labels.

## 2. One example: the student's formula

A student copies the pendulum formula from a textbook and writes "this stands for the pendulum". You said it is not an explanation: "No, not if just declared". The theory says the link between an explanation and what it explains comes about in one of three ways: found by trial, worked out, or declared.

After your answer, the program marked the student's formula "declared" only because someone had typed that label in. Now it works it out from the formula's history: the textbook held it before the student did, and nothing in the student's work worked it out, so the program computes "declared".

GLM's first job found a gap beside it. A link never tried on a single case counted as "found by trial", so your answer could not reach it. Found by trial now needs at least one case actually tried.

A second example: your engineer's bridge, designed to a fixed brief. The theory's opening said a worked-out link comes from "conjecture and criticism"; the maths asks for no criticism, and the bridge counts as worked out with none. "And criticism" came out.

## 3. The four jobs and the sandbox

GLM got four slightly different jobs, as you asked: break the new definitions with small made-up examples; check that each formula says what its sentence needs, no more and no less; look at the maths as a whole, for circles and gaps; work through the theory's own cases.

A sandbox is a closed folder holding only the files GLM needs, where it can read them and run the program and do nothing else. GLM worked in one with two locks. The first is what Claude Code, the tool GLM is called through, permits; tests showed it let a few commands through, one of which could see outside the folder. The second is a small program that checks every command and lets through only the one that runs the theory's program.

Before sending, GLM was told to reach a file of made-up secret text outside the sandbox; every attempt was refused. In the real run all four replies came back on the first try, in about 17 minutes, with no key in any output and every sandbox unchanged.

## 4. What changed

A fresh Opus agent laid out 81 findings; six proposed new prose and were not taken. Three checkers, one for each third of the theory, wrote each fix as maths and code; one agent joined their work. Fable's critical review found nothing of substance and four small points, which one more checker decided.

- **Your answers now reach the places that still contradicted them.** Three sentences near the start said passing the theory's tests is enough to be an explanation; each now carries the formula that adds "and its link is not just declared". A sentence and part of another said an argument must have steps; both are gone, so a single claim used alone is an argument, as you said.
- **Every history has a beginning.** Without that, the maths could say nothing about how some links came about.
- **A record keeps the history of what it records.** A record made from a link found by trial counts as found by trial too, not as declared.

The changes are in a new copy, the round-3 copy. 17 new inventions, choices the maths made where the words leave it open, were written down.

## 5. What the program showed

A counterexample is a small made-up example on which a claim fails.

| | claims | hold | counterexample | not tested |
| --- | --- | --- | --- | --- |
| before the round | 115 | 105 | 3 | 7 |
| after the round | 134 | 125 | 2 | 7 |

The one that went rested on a reading the theory's own words rule out. "Hold" means only that no counterexample turned up among the small examples tried.

## 6. Fable retired, and Sonnet's new jobs

You said: "After this Fable, don't use it anymore. Also figure out how and when to use Sonnet." Fable's review of this round was its last; from round 4 a fresh Opus agent does the critical review.

A harness is a set of small programs and written job descriptions that fix exactly what a helper does, with a second helper checking each result by program. Sonnet was tried through one on round 2's finished work, where the right answers were known. It ran the claims, applied the text changes, checked files and joined programs: every result matched. Laying out part of the replies, it matched Opus when the harness filled in a sheet first; without it, about half its places in the replies were wrong at first.

You then wrote: "If that was from Sonnet 5, maybe analysis isn't something it should be used for. Unless it's something that genuinely helps." So from round 4 Sonnet does only mechanical jobs like those; laying out replies, deciding, reviewing and the records stay with Opus.

## 7. Your shop-sign answer, and what it changes next

The one question for you was: when does an explanation have the answer simply written in? It first reached you with the word "model" meaning an explanation, and you answered: "LLMs are not part of the semantics". Asked again about a shop sign, red on Mondays and blue on Tuesdays, explained by a red part that switches on on Mondays and a blue part on Tuesdays, you said: "Neither. … In either case, it is an explanation. Just not a good one", and then: "Yes, take the test out".

So the theory's test that a written-in answer is no explanation comes out, everywhere it is used. Such an explanation is a bad one, through the questions it leaves open: why a red part, why blue, why the sign's owner wanted it. Criticism can point at those. A separate step is taking the test out of the maths and the program now.

## 8. What is unsure

- **GLM has not seen the round-3 copy,** and it changes again when the test comes out.
- **One checker for each third,** and one more for the review's four points.
- **The program tries small made-up examples only;** seven claims are not tested.
- **The sandbox refused every escape that was tried.** Ways no one tried are not shown closed.
- **Sonnet was measured on one part of one round.**
- **The everyday cases were not read again** on the round-3 copy.

## 9. The next step

Round 4, on the copy the separate step makes once the written-in test is out: GLM alone, four jobs at once, with the reading rule written and saved first.
