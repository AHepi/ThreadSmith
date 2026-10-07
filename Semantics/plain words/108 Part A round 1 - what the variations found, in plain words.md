# Part A, round 1: what the variations found. In plain words

*A note first. Written on 28 September 2026 by a Claude subagent, for you. It uses none of the words you asked to be removed, except inside quotations. The full record is "Semantics/results/S108 Part A round 1 - what the variations found.md". Nothing in the theory was changed: everything below was done on copies.*

---

## 1. One example: your shop sign and your weathervane

The largest effect of this round came from one small variation.

One of the theory's requirements is that each part of an explanation matches the piece of the thing it stands for. Today "matches" means that the part behaves as the piece's own rule says, taken alone.

One variation read "matches" another way: the part must behave as the piece actually does once the rest of the thing is in place. Under it:
- your shop sign, explained by a red part that switches on on Mondays and a blue part that switches on on Tuesdays, stopped counting as an explanation;
- so did the explanation of your weathervane by how it works;
- the sign explained by one part that gives both colours still counted.

Why: in each case that dropped, a piece's own rule allows more than the piece actually does inside the whole, so a part that follows that rule no longer matches. Where a single part stands for the whole thing, the two readings agree.

In all, 15 of the theory's 27 worked cases stopped meeting the requirements. The variation also clashed with one frozen definition, the one for how a group of pieces responds to changes. And in some small made-up examples, a thing no longer matched an exact copy of itself.

What it means for the idea: which explanations count leans heavily on what "matches" means for a single part. A small variation there reverses your answer on the sign: "In either case, it is an explanation."

## 2. What was done

You asked to "freeze all the parts that are hard to vary, changes bits around in the middle, and see how it changes how explanation is defined."

- **Frozen.** Of the theory's 815 items (its sentences, and the definitions in its maths), 238 were frozen and 577 were left in the middle. The frozen list is Claude's reading of "the parts that are hard to vary" (file 108); you have not answered on it.
- **Varied.** The middle was split into four sections. Four GLM agents, one per section, each proposed 8 variations, 32 in all. All four replies came back on the first try, in about 9 minutes, with no key in any output.
- **Run.** Three variations were set aside, because they touched frozen items or added a sentence. Four Opus agents ran the other 29 through the program, each in its own copy: on the 27 worked cases, and on tens of thousands of small made-up candidates.
- **Checked.** A fresh Opus agent reviewed the whole; one more checker decided its 13 objections.

## 3. What moved, and what did not

The requirements are the five things a candidate must do, such as matching the thing piece by piece. A candidate counts as an explanation when it meets them and its link to the thing was not simply declared.

- 6 variations changed which candidates meet the requirements.
- 7 changed which candidates count as explanations while the requirements stayed. All but one vary when a link counts as simply declared, or drop that rule; the other puts back the written-in test.
- 16 moved neither.

For example, varying which piece of a thing counts as an input or an output, what counts as a measurement or a rule, and what kind of question is being asked moved no candidate at all: 0 of about 62,000.

## 4. The dependency map, and a one-way finding

A dependency map is a chart of which items of the theory lean on which, found by varying one item and watching what else moves. This one has 859 boxes and 221 arrows. The program's runs show 179 of the arrows; 31 rest on argument alone; 11 were claimed by an agent and the runs showed otherwise.

An example first. One variation let a bare claim rule out its own denial for anyone who accepts it. Who had ruled what out changed in 1,677 of 9,600 small made-up arguments. Not one candidate's standing as an explanation moved.

The same held every time. Varying how the theory defines ruling out, conflict, the creation of explanations, which parts do the work, and universality never moved what counts as an explanation. The dependence runs one way: those ideas lean on what counts as an explanation, or stand beside it, and it does not lean on them.

## 5. The alternative definitions

13 of the variations are alternative definitions of explanation: with each one on, a different set of candidates counts. 8 of them seem to go against something you decided earlier. Among them are the variation of "matches" above, two that put back the written-in test you took out, and two that let a link that was only declared count. Several go against your decisions only on one reading.

None is applied. After Part B, Claude will bring you each flagged one, with an everyday example and your own words beside it, and you answer yes or no.

## 6. One finding about the theory itself

Among the ways the theory says it could be shown wrong is this: an explanation that someone can argue is real, but that no link could ever match to the thing it explains. The theory names "eliminative explanation", explaining why something is absent, as "the exposed case".

The program shows that the theory's own example of eliminative explanation meets the requirements, and anything that meets them has a link that matches. So the example cannot be the exposed case, with or without any variation. This is recorded for later. The review rounds are on hold, so nothing was changed.

## 7. What is unsure

- **The frozen list** is Claude's reading, not yours.
- **Several alternative definitions rest on one choice.** For example, is the north wind something done to the weathervane, or just its circumstances? Read as circumstances, one variation drops both your weathervane and your sign; read as something done, nothing moves. The program also keeps no record of how a question came about, and the histories of the links were set by hand.
- **The program tries small made-up examples only.**
- **One agent ran each section**, and one checker decided the review's objections.
- **The runs of all the program's claims** were meant for Sonnet, with a second Sonnet agent checking; the Opus agents ran them themselves. The review's eight reruns matched.
- **647 of the 815 items were touched by no variation**, and that silence shows nothing about them.
- **No outside reader has seen these results,** and the everyday cases were not read again.

## 8. Round 2, and the next step

The gaps are large, so a second round of Part A is under way. It aims first at the choices the alternative definitions rest on, tried the other way; then at seven untouched definitions that feed into what counts as an explanation; then at the arrows that rest on argument alone.

**The next step:** round 2 of Part A, with four GLM agents again, one per section, under a rule written and saved before anything is sent.
