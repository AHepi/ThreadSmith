# How the sealed box would be run, in plain words

*Log S132, 2 October 2026. Your words: "Correct. Knowledge doesn't need to be worked out, explanation does. That is an excellent experiment. How are you going to pull it off though? LLMs may already have the shape of the solution in its training data. Should I invent a difficult problem then see what happens? Or are you using one of these machines in Avida?" Nothing was built or run; one tiny test call was made.*

## The main point

It can be done from here: a fresh Claude session, knowing nothing of this project, can be started in an empty folder whose only tools are the box's. Your worry about training is real, so I add boxes whose parts behave in ways no textbook describes; doing about as well on those means it worked the box out, not recognised it.

## The pieces, in order

- **Box maker**: wires six hidden parts at random from a secret number; writes the rules and 40 test questions where the subject cannot see them.
- **Box**: the only thing the subject can touch (press, turn, look, take a part out, hold one fixed); it keeps the notebook and logs every move.
- **Subject**: a fresh Claude session (a program like the one writing this) in an empty folder, working in stretches of 10 moves; between stretches it keeps only its notebook and its list of moves, so what it works out must be written down.
- **Marker**: the 40 sealed questions about changes it never tried, then opening the door of a changed box.
- **Rerun**: one stretch run again with one notebook line changed: does the notebook steer what it does?
- **Checks**: the rules handed over (should count as copied); a blind search (evolved knowledge); boxes with no trap; questions with no box (guessing); everything renamed.
- **Readers**: two readers, blind to which set a notebook came from, mark rival ideas, wrong guesses noticed, faulty parts named and fixed.

First a trial on two practice boxes; then I stop and tell you the cost.

## The worry about training

- **New:** each box comes from a secret number, so no box is in any training; the account of *this* box cannot have been read anywhere.
- **Allowed to be old:** the method (guess, test, fix) and common kinds of part (counters, delays, switches that stay on). The theory allows that; what must be worked out is how *this* box is wired.
- **Where your worry bites:** if it succeeds only because the parts are familiar, it picked from a known list. That is weaker.
- **The new boxes:** each part follows a random rule table, the same size as a familiar part but matching none. Written down before anything runs: about as good on these means worked out; much worse means the familiar list carried it.

## Your own problem

Yes, as an extra. Before anything runs, write what can be done and seen, the hidden rules exactly, the answers, and 20 to 40 sealed questions; send it to me in a file, which I keep out of the subject's reach, and I check my coded version against your answers. You never talk to the subject. Make it new in how it works, testable by doing things to it, with a first easy guess that turns out wrong; avoid riddles, known puzzles in disguise, and anything you couldn't write as rules. It cannot be the whole experiment: one problem can't tell luck from skill, nobody can show it is unlike anything in training, and you must stay entirely outside. **New and testable matters more than difficult: a hard problem the subject has seen can be remembered; an easy one nobody has seen must be worked out.**

## Avida

Not as the subject. An Avida program holds no problem, no rival idea and no account, so whatever it did would be paid for by the execution environment (Avida's whole simulated world): evolved knowledge, which you closed. As a comparison it needs new C++ and many hours; a blind search does the same for far less.

## What the test call found

A fresh Opus 5.5 session in an empty folder answered "hello" in under four seconds, saw only that folder, and left it unchanged. To fix: it borrowed this session's id, made one small bookkeeping call to a smaller model, and reported usage data.

## Tested, not tested, unsure

- **Tested:** a fresh, sealed-off session can be started from here.
- **Not tested:** whether the seals hold if the subject tries to get out (first thing in the build); everything else.
- **Unsure:** whether random parts are simply harder (the blind search measures it); whether readers agree; the cost; whether wiring worked out on remembered kinds of part counts as worked out as a whole.

## One next step

Your yes or no: a fresh Opus 5.5 session as the subject, with the unfamiliar boxes added (about 9,800 calls, under three hours of computer time, after building), and your own problem only if you want to write one.
