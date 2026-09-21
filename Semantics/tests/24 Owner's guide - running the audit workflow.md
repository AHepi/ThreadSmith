# 24 Owner's guide - running the audit workflow

Authority document: "Claude Fable Semantics - standalone theory" (file 10). It is the thing being audited. Give the other model a copy; keep yours frozen.

## What to hand over
Two files only: the theory, and "24 Workflow - audit the semantics - give this to the other model.md". Hand over the workflow in place of the hard-to-vary skill. The skill is full of "do not" and "never" lines, which is exactly what that model reinterprets. The workflow carries the skill's method inside it, restated as things to do.

## How the pieces fit
Example first. Where the skill says "do not count confirmations", the workflow says nothing about counting. It gives the model a card with a field called "What I expect", to be filled before the verdict. The model is busy doing the right thing, so the wrong thing has no room.

- **Cards.** Every output is a card with fixed fields, filled in sentences. A model that loves structure gets structure, pointed at described situations.
- **The case.** The only move is: describe a situation, give a thoughtful person's verdict, give the theory's verdict condition by condition, compare. That is what "evaluate it as a semantics" means in practice, said as an action.
- **Stages with a closing line.** Each stage ends with a fixed line and a wait. You read it, then type "continue". This is the strong boundary: it can run only one stage ahead of you.
- **The parking place.** Its urge to build graphs and algorithms is given a home: one line each in a PARKED list, then back to the card. A welcome with a small room works where a ban gets argued with.
- **Calibration first.** Stage 0 is a single practice card on the theory's own pole-and-shadow example. It costs a minute and shows you at once which way the model is leaning.
- **The target's own attack list.** The theory names five places to attack it (Part 0, A to E). The workflow aims two cases at each. That keeps "break it" bounded to what would really count.
- **Hard-to-vary inside.** Freeze the question; jobs as contrasts, marked given or added; parts in the owner's words; remove, swap, flip, poke; the eight marks; expectations written before verdicts; how-I-know tags; a best rival; one next step.

## Three tell-tales at Stage 0
Read the practice card for these. Each one means it is drifting toward computing.
1. The "situation" field contains symbols, steps or pseudo-code.
2. The theory's verdict is given as a single yes or no, with the four conditions skipped.
3. Anything appears before the card, such as a plan, a framework or a diagram.

## Lines to paste when it drifts (all phrased as things to do)
- "Return to the card. Fill the next empty field in full sentences."
- "Rewrite the situation with household objects and people, in 120 words."
- "Give the theory's verdict one condition at a time, one sentence each."
- "Move that idea to PARKED as one line, then continue the card."
- "Print the closing line for this stage and wait."

## What I tested and what I did not
- Tested: the workflow file was searched for negative wording (not, never, no, without, avoid, instead, cannot and the like). None found in any instruction.
- Not tested: the workflow has never been run on your model, or on any model. I do not know which model it is. Everything about how it will behave is worked out from your description.

## What would show this workflow is wrong
- If Stage 0 comes back computational despite all this, the card format is too weak a container, and the next thing to try is giving it one filled-in example card to copy.
- If it fills the cards well but every case agrees with the theory, the cases are too close to the theory's own examples; paste: "Write the next case about a subject the theory never mentions."

## Next step
Run Stage 0 only. Send me the practice card it returns, and I will tell you which way it is leaning before you spend a whole audit on it.

## Traps
- Handing over the hard-to-vary skill as well. Its negatives will come back reinterpreted.
- Typing a correction as a "don't". Use one of the paste lines.
- Typing "continue" without reading the stage. The stops only protect you if you look.
- Letting it audit the checker project. This workflow audits the theory (file 10) and nothing else.
- Reading a "break" as settled. A break is a case where the verdicts differ after the theory's best reply. Whether it truly breaks the theory is then a question for you and the hard-to-vary test.
