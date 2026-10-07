# Part A: the parts to be frozen. In plain words

*Written on 28 September 2026 by a Claude subagent for you. It uses none of the words you asked to be removed, except in quotations. This list is Claude's reading of your instruction; nobody has asked you to approve it yet. The full list, item by item with the reason for each, is "Semantics/results/S108 Part A - the frozen set.md". The program that made it is "Semantics/tools/s108_frozen_set.py".*

---

## 1. What you asked for, and how Claude read it

You asked: "freeze all the parts that are hard to vary, changes bits around in the middle, and see how it changes how explanation is defined. The goal in this part is to map dependencies."

To freeze something, we first need a list of "the parts that are hard to vary". Claude took them to be the parts that readers tried to change, round after round, and that came through unchanged while the parts around them kept changing. That is the approach you agreed to on 26 September ("Yup do that"), when we looked for the strong candidates.

The test applied to every sentence of the theory and every definition in its maths:

- **Frozen** if both hold:
  1. a reader or a checker was given it at least once, to attack or to test;
  2. no round of review, and no step you asked for, has changed it since.
- **In the middle** otherwise. Where the record can't say which applies, the part goes in the middle.

This list says nothing about what "hard to vary" covers in general. You parked that question, and it stays parked.

## 2. The numbers

The theory is used as it stands after the fourth review round. The fourth round's two wording changes were taken back, so the wording is the same as after the written-in test came out. Six pieces of the maths changed in that round, and every one of them was already in the middle.

| | frozen | in the middle | all |
|---|---|---|---|
| sentences of the theory | 169 | 519 | 688 |
| definitions in the maths | 69 | 58 | 127 |
| all parts | 238 | 577 | 815 |

About a third of the sentences and about half of the maths are frozen.

## 3. What is frozen, part by part

The theory has seventeen parts. These are the frozen parts, in plain words.

- **Part 0, read this first (5 sentences).** Three short lines stay put:
  - how a transport came about is one thing, and how faithful it is another;
  - a constructed correspondence has its own trace, and every creative attribution needs one;
  - the text defines the classes it speaks of.
  - Two answers to objections stay as well. Aesthetics has its place in Part XI, as a declared input. A rule and a cause differ in how they respond to changes.
- **Part I, commitments (1).** Whether a transport is faithful doesn't depend on who judges it.
- **Part II, organizations (25, the most of any part).** Most of the ground floor:
  - what an organization is: ports, values, components, boundary conditions and the changes it admits;
  - how its solutions are worked out;
  - a deleted component imposes nothing, and a changed rule is a changed component;
  - cycles are allowed, and several solutions stay several;
  - which way an organization runs comes from which changes it admits;
  - a component's signature is how it responds to the admitted changes;
  - "The semantics never asks whether a component "is" a cause. It asks what its signature is."
- **Part III, questions (10).**
  - A question is a target, a set of admitted changes (the contract), a starting point and a way of reading off the answer.
  - Finding a question needs the contract to have been constructed.
  - A question can fail to pick out what it is about, and exposing that is another question.
- **Part IV, transports and provenance (19).**
  - The two layers and what a transport is.
  - "Declared" means neither selected nor constructed.
  - Construction can work on selected material, and selection can go on beneath construction.
  - Of the two responses to a surprise, only building something new can be originative.
- **Part V, what an account is (10).** The heart of the definition of explanation is split:
  - **Frozen, in the maths:** four of its five conditions. These are component fidelity, fidelity of the whole, giving the question's own answer at every admitted change, and non-vacuity (the question has a starting point, and its admitted changes are stated).
  - **Frozen, in the sentences:**
    - the formulas for fidelity of the whole and for the question's own answer;
    - what the two fidelities each prevent;
    - "The query … is held fixed";
    - "None inspects a label."
  - **In the middle:**
    - the fifth condition, that the answer must depend on the explanation's parts;
    - the one line that joins the five into an account;
    - the wording of component fidelity and of non-vacuity.
    The step that took out the written-in test changed the first two. The wording of the last two changed during the drafts.
- **Part VI, work, rivals and problems (23).**
  - How the parts of an explanation share the work (routes, critical blocks, redundant routes, interference).
  - What rivals are, and that no list of all rivals is assumed.
  - A conflict with a claim doesn't say by itself which side to drop.
  - What a problem is, and its two kinds.
  - A criticism that an explanation is easy to vary must supply a rival.
- **Part VII, worked cases (12).** Parts of:
  - the pole and its shadow;
  - identification;
  - obstruction;
  - the skew-symmetric matrices ("The expansion is an account.");
  - rules as a status.
- **Part VIII, results about transports (3).** Among them "A failed answer stays failed".
- **Part IX, criticism and usable arguments (6).**
  - When an argument is usable by someone.
  - A criticism can occur even when it bears on nothing.
  - What using a reason is.
- **Part X, construction and origin (11).**
  - Construction is not selection: a selected transport has no represented target in its history, and a constructed one does.
  - Using something doesn't by itself construct it.
  - What counts as new.
  - The originative act can be finding a question.
- **Part XI, repair (5).**
  - The definition of a repair.
  - "Losses outside P must be exposed."
- **Part XII, the physical module (5).** Capabilities, and that a capability at one tolerance is not a possibility at every tolerance.
- **Part XIII, recursion and universality (6).** Among them: recursion does not bring universality with it.
- **Part XIV, the class collected (14).**
  - The physical module as an import.
  - Most of the order in which the ideas depend on one another.
  - What it takes to belong to each class.
- **Part XV, what would rule the class out (1).** Only "A mathematical error". Every other item in this part has changed over the rounds.
- **Part XVI, the Arguments (13).** Single steps in several of the ten arguments.

Of the 36 strong candidates found on 27 September, 27 are frozen. The other nine were changed by later rounds.

## 4. What is in the middle

The middle is everything else: 519 sentences and 58 definitions. Most of the middle sentences changed during the drafts, before the review rounds began. The rest changed in a review round or step, or were never put to a reader on their own.

The middle includes:
- most of Part 0's answers to objections;
- how selected and constructed are defined in the maths;
- the dependence condition of an account, and the line that joins the conditions into an account;
- conflict and rivals in the maths;
- how usable arguments and ruling out are defined;
- the episode, and the created explanation;
- the classes;
- most of Part XV and Part XVI.

## 5. What happens next

The middle is split into four stretches of the theory, of about the same size:

1. Parts 0 to III: the opening, organizations, kinds and questions (154 parts in the middle).
2. Parts IV to VII: transports, provenance, the account, rivals and the worked cases (153).
3. Parts VIII to XII: criticism, construction, repair and the physical module (137).
4. Parts XIII to XVI: recursion, the class, what would rule it out, and the Arguments (133).

Four GLM agents each get the same copy of the theory, with every frozen part marked. Each gets one stretch to vary. Each proposes small, exact changes in its own stretch only. For each change, the agent says which explanations would newly count and which would stop counting, and what the change bumps into: a frozen part that blocks it, or a part elsewhere that would have to change with it. Those bumps are the dependencies you asked to map.

Nothing in the theory changes. Other agents then work out each change's real effect in their own copies of the program. From that they build the map, and a list of the new definitions of explanation the changes turn up. Each entry is marked with any of your past decisions it doesn't appear to agree with. That list comes to you later for a yes or a no.

## 6. Two choices in the list you may want to know about

- **Word swaps count as unchanged.** Where a sentence changed only because a word you asked to remove was swapped for another, it counts as unchanged. This follows the earlier count of strong candidates. Removing references to history and versions does count as a change.
- **A sentence and its maths are judged separately.** For some sentences, the wording held while the maths written for them was corrected. The sentence is then frozen, and its maths is in the middle. Any change to that maths must still match the frozen wording.
