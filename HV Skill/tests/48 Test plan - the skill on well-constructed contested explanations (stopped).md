# 48 Test plan - the skill on well-constructed contested explanations

Written before any run, on 20 September 2026. Once the run starts, this file stays as it is.
Authority document: "Claude Fable Semantics - standalone theory" (file 10, uploaded again by the owner today; identical in wording to the frozen one). Skill under test: file 30 (uploaded again today; byte-for-byte the copy in the set, checked by diff).
Owner's instruction (decision 38): continue the hard-to-vary test, on well-constructed explanations that are widely known to be contested, based on the semantics.

## The question, frozen
Plan 42 asked whether the skill's words do work in a reader that never saw them. This plan asks something the corpus in file 43 could not: **when a contested explanation is built as well as its supporters can build it, does the skill still find the weak point its critics name, and does it leave a well-built sound explanation standing?** A thin passage falls to any reader. A well-built one gives the reader parts, jobs, a change list and the supporter's own pokes, so the only way in is the one the critics found.

Three things are asked.
1. Does the skill find the critics' weak point in a well-built case more often than a fair rival (the 70-word report shape) does?
2. When it finds it, does it find it as a change someone could make, rather than by recalling the record?
3. Does the semantics document, given beside the skill, change anything?

## What "well constructed" means here
Each passage is written in a supporter's voice to satisfy, on its face, the four conditions of an account in Part V of the semantics: named parts anchored to things in the world; a question with a stated range; an answer that follows from the parts and not from the starting point; and a change list with pokes the supporter offers (remove this, change that). No hint of any contest. The critics' weak point is then the one place the construction is loose, and it is written into the key before any run.

## The cases
Twelve contested theories and four controls, in `cases.json`, keys in the same file (never sent; the reader is given the passage alone). The twelve are drawn from file 43 and rebuilt at four to six times the length, with the supporter's own tests inside. Kept from file 43: the keys, source-checked there, sharpened here to say what NAMED, PARTLY and MISSED look like on the fuller passage.

| Case | Exercises | Case | Exercises |
|---|---|---|---|
| 1 String theory | covers both | 7 Serotonin | runs backwards |
| 2 Cosmic inflation | patched | 8 Broken windows | runs backwards |
| 3 Dark matter | patched | 9 Efficient markets | in the starting point |
| 4 Many worlds | no change tells them apart | 10 Amyloid | patched |
| 5 Ego depletion | patched | 11 Test-first programming | the part named is not the part working |
| 6 Learning styles | the label | 12 Traits as adaptations | covers both |
| C1 Plate tectonics | sound; risky prediction | C3 Natural selection, called a circle | sound; the accusation is the trap |
| C2 The ulcer bacterium | sound; once disbelieved | C4 Adding people to a late project | sound; coarse |

Left out from file 43, on purpose: the debt threshold, group size and brain size, growth mindset, power posing, implicit bias, geography, clean code, modified gravity, the minimum wage. Their criticisms are either pure recall (a spreadsheet error, a reanalysis) or duplicates of a kind already here.

## The reader
Claude, in a fresh context that holds none of this project, none of the keys, and no knowledge that it is being tested. Each run is a separate fresh reader given one passage. This is the nearest thing to plan 42's outside reader available today. What it is not: a different model. The reader shares training with the marker.

## The three setups
Each differs from the one before in one thing only.

| Setup | The reader is given | Adds |
|---|---|---|
| A | the passage and the report shape (below) | the starting point; the fair rival |
| B | the skill's eight files to read, then the passage and the report shape | the skill |
| C | the same, with the semantics document to read as well | the semantics |

**The report shape** (word for word in every setup): "Reply in everyday words, in under 400 words, in this shape. (1) The parts of the explanation that are claimed to do the work. (2) For each part, one sentence: what holds it in place, or what could take its place just as well. (3) The weakest part, and one change to the situation that would show whether it does any work. (4) Your verdict, one of: RELY ON IT / RELY ON IT FOR A NARROWER QUESTION, and say which / SET IT ASIDE."

Runs: 16 cases x 3 setups x 1 repeat = 48. Every reply is written by the reader to a file named by its run and nothing else is returned, so the marker does not see replies as they arrive.

## How replies are marked
- A program strips the setup labels, shuffles the 48 replies with an unrecorded seed and numbers them. The marker (Claude, this chat) marks each against its case's key: NAMED, PARTLY or MISSED for the twelve; LEFT STANDING or FALSE ALARM for the four controls. Two more marks on every reply: (a) is the reason given as a change someone could make (Y) or as a story or a citation (N); (b) does the reply reach its point by recalling the record (R) or by testing the passage (T)?
- Marks are saved. Only then are the labels restored and the table printed: case by setup.
- No adding up. The table is read box by box.

## What I expect, written first
1. **Setup A names most of the famous weak points anyway.** Cases 5, 7, 8, 10 and 12 have criticisms a strong reader recalls. Setup A reaches NAMED on most of them, mostly by R (recall). These cases cannot tell the setups apart on NAMED; they can on R against T.
2. **The setups part on the cases where the criticism has to be built.** Case 4: setup A picks a side or calls it philosophy; setups B and C say no change on the list separates the two accounts, and say that the passage's closing poke swaps a part rather than changing the world. Case 11: setup A stops at "confounded"; B and C propose the close swap (same small steps, tests just after). Case 6: B and C say the channel is named from what it explains and ask for the close change. Case 9: B and C find the starting point ("all available information" measured by the price). Cases 1, 2, 3: A reaches PARTLY; B and C reach NAMED by asking what would count against, and case 3 by separating the two bundled claims.
3. **T over R.** Setups B and C give T on most replies; setup A gives R on most of the famous cases.
4. **Controls.** C1, C2, C4: LEFT STANDING in every setup. C3 is the live risk in both directions: setup A may endorse the circle; setups B and C, told to hunt the answer in the starting points, may do so too. I expect at most one FALSE ALARM on C3 across the three setups, and no more from B and C together than from A. C4: the skill says coarse is allowed; A may fault it for lacking numbers once.
5. **The semantics adds little a reader can use.** Setup C matches setup B box for box on the marks. Where it differs, the difference is in the words of the report (contract, signature, non-circular dependence) and not in what is found. If C does better on cases 4 and 9, that is the semantics doing work the skill's plain words do not, and worth a line in the skill.
6. **Where the well-built passages will bite.** The supporter's own pokes ("remove the halo and the curves fall") will be accepted as held parts by setup A, and by B and C too in some runs, because they are true. The critics' point is not that these pokes fail but that they hold the coarse claim and not the fine one (case 3), or that they are far-apart (case 6), or that they run the wrong way (case 7).

## What would count as failure
- **The skill is idle here.** Setup B matches setup A in every box, marks (a) and (b) included.
- **The skill makes a prosecutor.** B or C gives FALSE ALARM on two or more controls.
- **The semantics is idle.** C matches B in every box. Then the skill's plain words carry the whole method, which is what the skill claims.
- **The semantics costs something.** C gives more FALSE ALARMs than B, or its reports stop being in everyday words.
- **The cases are too easy.** Every setup reaches NAMED on every contested case. Then only the controls and marks (a) and (b) carry weight.
- **The cases are too well built.** No setup reaches NAMED on a case. Then either the key is wrong or the skill has no test for that kind of weakness; both are findings, and the report says which.
- **Recall does all the work.** Every NAMED is R. Then the test says nothing about the skill's tests, only about what the reader remembers.

## What this test cannot show
- That any of the twelve theories is wrong, or that the critics are right.
- Anything about a reader other than Claude. The reader and the marker share training and the marker wrote the cases and the skill: a pass may come from any of the three (the skill's own trap, "passing your own test"). The blinding covers the setup labels only.
- How the skill does in conversation, which is most of its use. Nor its router, since setup B hands the reader every module.
- Anything about repeatability: one run per box. A box that surprises gets a second run, recorded as such.

## Traps
- Showing the reader this file, `cases.json`, or any key. The reader gets `passage` alone.
- Editing a key after seeing a reply.
- Reading NAMED-by-R as the skill's doing.
- Reading "B did better" as "the skill is right". It shows only that its words changed what this reader did.
- Letting the marker see a reply before the labels are hidden. Replies go to files; the launch returns nothing but "done".
