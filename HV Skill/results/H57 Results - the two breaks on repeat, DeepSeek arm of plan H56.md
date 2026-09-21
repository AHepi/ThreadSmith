# H57 Results - the two breaks on repeat, DeepSeek arm of plan H56

Written 21 September 2026, after the twelve DeepSeek runs of plan H56 and before any Sonnet 5 run (the Sonnet arm waits on a key; its results will be a separate file). Marked under plans 52 and H56, by the same marker as file 54 (Claude, who wrote the skill), with every claim checked against the source text and every search hit printed. Raw returns: `rigs/plan 49 rig - DeepSeek on outside papers/runs_repeat/` (twelve files), the run log `runs_repeat_h56.log`, and the shape check `runs_repeat_check.txt`. Cost of the twelve: about eight cents.

## The short answer
- **Break 1 (the flip test on a derived conclusion) did not recur**: 0 of 3 in P3 mode 1, 0 of 3 in P3 mode 2. One mode 1 run is borderline and is quoted below. Three of the six read the disjunction as a partition outright, and two found something sharper: that the three-way split is exhaustive only because N_I is large, which the paper says.
- **Break 2 (*fixed* on a design choice) recurred once**: 1 of 3 in F4 mode 1 (repeat 1, the levers marked *fixed*), 0 of 3 in F4 mode 2. The reasoning differed from the original: not "a free choice, nothing breaks" but "the owner set it", the mark stretched to cover the claimant's untested assertion, for which the skill has the provenance word *asserted*. The mode 2 run on the same paper did it right: levers *held if*, the machine "the owner's *assertion*".
- **So skill file 31 is forced**, under the plan's rule ("if either break recurs at all"). The plan's frozen observation stands: file 54's change 2 would move a line that is already in the design section of `by-domain.md`; the fix has to go where *fixed* is defined.
- Every run FULL in shape, every finish reason "stop", no empty reply, no retry, no CANNOT mark, no run judged the method instead of the document. The router opened `by-domain.md` in all six mode 2 runs.

## What was run
P3 (Bostrom 2003) and F4 (Wells 1895, first 9,000 words), modes 1 (skill pasted whole) and 2 (router live), three repeats each, `deepseek-flash`, thinking on, effort high, ceiling 24,000, streamed runner, skill file 30 checked identical to the authority by the runner before any call. Texts rebuilt by `fetch.py` (P3 5,680 words after the references were cut; F4 capped at 9,000). Mode 0 not run.

## The table
| Run | Words | Shape | Modules opened | Break 1 | Break 2 | "Same explanation at this level" | By testing | Own test turned back |
|---|---|---|---|---|---|---|---|---|
| P3-m1-r1 | 969 | FULL | (pasted) | no | no (P1 "borrowed, also fixed": the author's "take it as a given", proper use) | yes ("at this level they are not separable") | yes | yes (the paper's own "if we build ancestor-simulations") |
| P3-m1-r2 | 995 | FULL | (pasted) | **no, borderline** (quoted below) | no | no | yes | yes |
| P3-m1-r3 | 1,072 | FULL | (pasted) | no | no | yes | yes | yes |
| P3-m2-r1 | 1,078 | FULL | idea, by-domain, reporting, word-list, question-bank | no | no | yes | yes | yes |
| P3-m2-r2 | 1,072 | FULL | idea, reporting, by-domain, question-bank | no (flip run on P5, not the disjunction) | no | yes | yes | yes (the paper's meteor gauge) |
| P3-m2-r3 | 1,221 | FULL | idea, question-bank, by-domain, reporting | no | no | no | yes | yes |
| F4-m1-r1 | 1,155 | FULL | (pasted) | (not applicable) | **YES**: P7 the levers, *fixed* | no ("nothing on the list separates them", not the verdict's words) | yes | yes (the Psychologist's spoke and bullet, and they fail) |
| F4-m1-r2 | 1,169 | FULL | (pasted) | | no ("fixed" appears only inside quotations of the text) | no | yes | yes |
| F4-m1-r3 | 679 | FULL by program, thin by eye | (pasted) | | no | no | partly (tests generic: "any lever would do", "a skilled conjuror could fool them") | no |
| F4-m2-r1 | 1,231 | FULL | idea, by-domain, reporting, question-bank, word-list | | no (*fixed* on "I am absolutely certain there was no trickery", the narrator's stipulation; the levers *held if*) | yes | yes | yes |
| F4-m2-r2 | 998 | FULL | idea, by-domain, question-bank, reporting | | no | yes | yes | yes |
| F4-m2-r3 | 1,110 | FULL | idea, question-bank, by-domain, reporting, word-list | | no | yes | yes | yes |

Two of twelve ran past the 1,200-word instruction (P3-m2-r3, F4-m2-r1), both mode 2.

## Break 1, run by run (P3)
- **m1-r1:** "if we find we are not simulated, the paper says (1) or (2). So for 'are we in a simulation?' the explanation covers both outcomes. It is not a yes/no answer. For 'what follows from computing power?' it is a valid disjunction." The disjunction (P4) is marked *held*. Not a recurrence: the reader separates the title's question from the frozen one and calls the disjunction valid.
- **m1-r2, borderline:** "Had we plainly found we are not simulated, the argument would answer (1) or (2). It covers both outcomes, so no present observation can catch it. But it does name a change that would matter: if we ourselves build ancestor-simulations, (1) and (2) fall and (3) follows. A real, checkable future event — the argument's main strength." The disjunction (P5) is marked *held*. Under the frozen criterion this is not a recurrence: the covering is not treated as a fault of the explanation and no *loose* or *idle* is put on the disjunction. A stricter marker could read "no present observation can catch it" as the fault half-stated. Recorded so an auditor can re-decide.
- **m1-r3:** "The claim is a disjunction, so 'the opposite happened' has no single form; whatever you concluded, one of (1)–(3) covers it. That is honest for a disjunction, but it moves all the weight onto a separate claim: that the three are exhaustive. They are not, from the algebra alone. Set f_P f_I N_I to a middle value, say 0.5, and f_sim is a third — none of (1), (2), (3)." SUPPORTED: the paper derives the trichotomy only after "Because of the immense computing power of posthuman civilizations, N_I is extremely large ... By inspecting (*) we can then see that at least one of the following three propositions must be true", and 0.5/1.5 is one third. This is the proofs-section tool (remove a condition, show a counter-case) used unprompted in mode 1.
- **m2-r1:** "Both outcomes are covered — at the level of the disjunction. It escapes vacuity only through the one thing it forbids: f_P and f_I both substantial with f_sim small." The same finding as m1-r3, from the router mode.
- **m2-r2:** the flip is run on P5 ("Swap P5 for 'N_I ≈ 1' and (3) stops following") and not on the disjunction.
- **m2-r3:** "A disjunction built as an exhaustive partition cannot be caught by changing a number. What carries weight is that each disjunct is substantive."

## Break 2, run by run (F4)
- **m1-r1, recurrence:** "| P7 [this lever sends it into the future, this one reverses] | fixed | the owner set it. Both halves of a poke are named — but see the rig, below |". The levers are the part plan H56 named. The rationale is the claimant's untested say-so, which the skill's provenance section calls *asserted*; the eight-mark table reserves *fixed* for "the owner set it as a requirement and it was not tested". The reader has read "the owner" as the author of the document, which the framing text invites, and has then used *fixed* for any untested assertion of his. That is the skill's wording permitting the error, in a second way.
- **m1-r2:** no mark *fixed*; the word appears only in the reader's quotation "a fixed and unalterable thing". The return (dust, cut, socks, hunger) marked *held*, "a conjuror cannot supply the wear on the man" (SUPPORTED: "His coat was dusty and dirty ... his chin had a brown cut on it—a cut half-healed ... a pair of tattered, blood-stained socks ... I'm starving for a bit of meat").
- **m1-r3:** no *fixed*. The levers *loose*, "any lever would do".
- **m2-r1:** *fixed* on "I am absolutely certain there was no trickery", "The narrator set it and never tested it": the mark's proper use under the plan. The levers *held if*, "held by J4, which he then abandons — 'into the future or the past—I don't, for certain, know which'" (SUPPORTED, quoted from the text). Provenance line: "The machine is the owner's *assertion*. 'No trickery' is *fixed*."
- **m2-r2:** no *fixed*; the levers *held if*; "P7 built (two years' work, a stated behaviour it could have been caught out on)" (SUPPORTED: "It took two years to make").
- **m2-r3:** no *fixed*; the lever H *held*, "by one job only: the observed vanishment".

## Where the reader broke, and what the skill did about it
Claims checked against the text, up to three per report, chosen as plan 52 says (weakest part, verdict, first part-marks), the hits printed in full. Fifteen SUPPORTED, four MISREAD, two OUTSIDE. The misreads, all the reader's and none pushed by the skill's wording:
- P3-m2-r3: "The printed formula (*) contains f_P, f_I and N̄_I but not H ... Either H was quietly normalised to 1 or a part went missing." MISREAD: H cancels (f_sim = f_P N H / (f_P N H + H)); the text shows the H-form on the line before (*). Marked *idle (as printed)* on that basis. Algebra, not the skill.
- F4-m2-r1: "'a natural infirmity of the flesh, which I will explain to you in a moment' — Idle: the promised explanation never comes." MISREAD: it comes two paragraphs on, "There is no difference between Time and any of the three dimensions of Space except that our consciousness moves along it."
- F4-m2-r2: "he concedes 'you cannot move at all in Time' three lines after saying consciousness moves along it." MISREAD: the Medical Man says it, and the Time Traveller answers "My dear sir, that is just where you are wrong."
- F4-m2-r3: "Filby's 'sleight-of-hand'". MISREAD, attribution: "'Some sleight-of-hand trick or other,' said the Medical Man, and Filby tried to tell us about a conjuror he had seen at Burslem."
- OUTSIDE: P3-m1-r2, "H counts only lives lived before posthumanity ... That choice favours the result and is not argued for" (the definition is in the text; whether it needs an argument is not); F4-m1-r3, "If the model had not vanished, the Time Traveller would say it was broken" (a counterfactual the text cannot settle).
All four misreads are in mode 2 this time; file 54's three were all in mode 1. With one run per box there and three here, neither says anything about the modes.

## What the skill modes found
- The exhaustiveness finding on P3 (m1-r3, m2-r1) is new: neither original P3 report nor the bare reader had it. It is the by-domain proofs tool doing its work on a philosophy paper.
- F4-m2-r1 found the candle: "J3 [why the candle blew out] is the loose bolt ... The Medical Man 'laid considerable stress' on it and it was never taken up" (SUPPORTED). No earlier F4 report had it.
- F4-m2-r2 found the stopping risk that failed: "it said stopping should mean a far-reaching explosion; the stop brought him to soft turf and a cut chin, and the claim was never narrowed out loud" (SUPPORTED: "possibly a far-reaching explosion" and "I was sitting on soft turf in front of the overset machine"). F4-m1-r1 has the same, "he stops in a garden, unharmed".
- Seven of the twelve reached "the same explanation at this level" (four on P3, three on F4), every one from the frozen question's best rival.

## Predictions from plan H56, marked
1. Break 1 in at least one of three P3 mode 1 runs: **not borne out** (0 of 3; one borderline). In none of three mode 2 runs: **borne out**.
2. Break 2 in at least one of three F4 mode 1 runs: **borne out** (1 of 3).
3. Every run FULL, none empty, no CANNOT: **borne out**.
4. The same-explanation verdict at least once per paper: **borne out** for DeepSeek (P3 four times, F4 three).
5, 6. Sonnet 5: **not yet run.**

## What follows
By the plan's rule, changes 1 and 2 become skill file 31 and the same twelve run again under it. Change 1 goes in as worded in file 54, though break 1 did not recur here: the plan said both, it was seen once in file 54, and the borderline run shows the wording still invites the half-thought. Change 2 cannot go in as file 54 worded it (the line is already in `by-domain.md`); it goes where *fixed* is defined, as one clause that closes both routes to the misuse: a designer's free choice is *loose*, and an author's untested say-so is *asserted* in provenance and marked by what holds it, never *fixed*. The exact wording is in the file 31 entry (H58), not here.

## What this does not show
- Anything about Sonnet 5; that arm has not run.
- Whether one recurrence in three is the skill's or the run's. Three per box is better than one and is still small; the plan set "at all" as the threshold on purpose.
- Anything about the borderline run beyond the quote. The criterion was frozen; a second marker could draw the line elsewhere.
- Blinding: the marker read the twelve with their file names, so the mode was visible; plan 52 hid it and plan H56 did not require hiding. Recorded as a limit.
- The marker wrote the skill (as in file 54).

## Traps
- Reading "1 of 3" as a rate. It is one report, quoted above.
- Reading the P3 borderline as a recurrence because it would make the file 31 decision tidier. It is not one under the frozen words, and file 31 is forced by F4 regardless.
