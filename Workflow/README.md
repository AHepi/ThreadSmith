# Workflow - the research toward a workflow that embodies the semantics

The end goal, in the owner's words (HV decision H6): "The end goal is an entire workflow that embodies the yet incomplete semantics theory HV is based on." This project holds the research toward it: first a model of large-language-model agents written in the terms of Semantics file 10, then the map of which skills the workflow needs and where their boundaries lie, then the workflow itself. It was made 22 September 2026, after the HV Skill (file 33) and Planning (file 2) were hardened and frozen, on the owner's word ("Yup continue. Do it", decision W1).

The project is named by the owner's word for the end thing. It is not the kind of file the LEGEND calls "Workflow" (an instruction handed to the other model, as in Semantics file 24); that kind keeps its name and this folder keeps its own.

## Current state
- **Authority: none yet.** The first authority file will be the model (phase 1 of the plan), once its predictions are frozen and the owner has given the word.
- **The plan: [W3 Research plan (frozen)](<tests/W3 Research plan - a model of LLM agents in the semantics' terms, the instrument, the arrangements, the skill map, the workflow (frozen).md>), 22 September 2026.** Six phases, each with its own frozen plan when its turn comes, each on the owner's word: the model of an LLM agent in file 10's terms; the reading of the evidence in hand under it; the instrument (the marking certified on the 96 reports in hand before any arrangement is measured with it); the arrangements (the arms that separate stateful from stateless, the partition harness, the port-setting harness, the context with one item withheld, the router criticised); the skill map; the workflow and its first run on the clean part of the reserve. The model is sketched in ten parts, each on a quoted sentence of file 10 with its Part and what would count against it; the skill map is sketched from Part XIV with a row for every operation; the predictions are counts that are falsifiers and never verdicts. It is [draft W1](<tests/W1 Research plan - a model of LLM agents in the semantics' terms, then the skills and their boundaries, then the workflow (draft).md>) with every edit five Opus 5 judges armed with the hard-to-vary skill forced ([W2 Results](<results/W2 Results - five Opus 5 judges on the draft research plan; what they forced into W3.md>)).
- **The theory is now file 11** (revision 1, Semantics decision S8, log S76; handed to this project by decision W2 and merged in from `main`), read beside file 10: [W5 Addendum (frozen)](<tests/W5 Addendum to W3 - the theory is now file 11; what changes in the plan, and what it gives up (frozen).md>), read with W3, says what changes (every sentence of W3 that named file 10; M2 and M6 under the qualified Derivation 3; the sentences of file 11 that now hold parts W3 had built or declared; M9's boundary phrase) and what is given up; it is draft W4 with what two Opus 5 judges forced ([W5 Results](<results/W5 Results - two Opus 5 judges on the addendum W4; what they forced into W5.md>)). File 11 is under test in the Semantics project's round S76 and not yet confirmed there; every row of phase 1's word list will say whether it rests on 10 and 11 or on 11 only.
- **What the plan asks** (W3 section 12): of the HV Skill, after phase 1, one change to its word list under its own plan; of the owner, the "5 tops" sentence into HV Decisions, the two root navigation edits confirmed, the harness material for Q1 if any, and whether the 33 held-out sources of file 50 stay held for HV plan H67.

## Where to start
[INDEX.md](INDEX.md) for the timeline. [ORIGIN.md](ORIGIN.md) for the owner's words and where the programme's content came from. This project keeps its own record in [records/](records/): [project story](<records/Workflow - project story.md>) (the log), [Decisions](<records/Workflow - Decisions.md>), [Lessons](<records/Workflow - Lessons.md>), [Status](<records/Workflow - Status.md>); its [READ ME FIRST](<records/READ ME FIRST.md>) says how it relates to the other projects. Its claims about the other projects are in [RELATIONS.md](RELATIONS.md).

## What is in this folder
```
ORIGIN.md      the owner's words on the end goal and the order of work; where the programme's content came from
records/       this project's own log, Decisions, Lessons and Status, from 22 September 2026
RELATIONS.md   this project's claims about the other four, with status and evidence; what it asks of them
INDEX.md       the timeline of research states
authority/     (empty until phase 1 freezes the model)
tests/         W1 (draft); W3 (frozen, current)
results/       W2: what the judges found and what it forced
rigs/          W2 judges/ (five returns, tool audit); W3 quote check/ (program and output)
```

## Rules of this project
- **The theory is Semantics file 11, read beside file 10** (decisions S4, S8, W2; addendum W4). This project reads them and never edits them; where it finds the theory cannot reach a question, that is written as an ask in RELATIONS, never as a change.
- **The other four projects are read only** (HV decision H8). What this project asks of them is written in its RELATIONS.md; each change is that project's to make under its own plan.
- **Every phase has its own frozen plan with predictions as counts that could fail; every result names what it did not test; each phase starts on the owner's word** (Planning file 2; the root conventions).
- **Never a Fable 5.1 reader under test or subagent** (HV decisions H4, H7). Opus 5 subagents permitted, geared with the hard-to-vary skill, at effort "extra" (xhigh), not max; five at most for a judging round (H7: "5 tops"). Readers under test as before: DeepSeek V4.1 Flash through the rig, Sonnet 5 as Claude Code subagents.
- **Nothing about an agent is read off one of its reports.** Semantics file 10, Derivation 9: "The same holds for attribution from emitted text". Evidence about what an agent instantiates is what changes in its emission when what it is given is changed, across arms.
- **Numbering is this project's own** (W1 first; decisions and lessons W1 onward). Work here edits only this folder, and the root only for navigation.

## Words used in this project
Short form; the theory's terms are file 10's, and the plan quotes the sentence for each use.
- **A call, the context, the emission.** One execution of the language model; the text it is given; the text it writes. The model of phase 1 works at this grain and no finer.
- **Stateful, stateless.** An agent whose executions carry their state between calls; one whose state between calls is only what its carrier text carries. The plan's M5 says the difference tracks what is represented at each call, not the label.
- **Arm.** One arrangement of an agent in a run (stateful; fresh calls with the transcript; fresh calls with a summary; the partition harness), all on the same skill, documents and framing.
- **Within-step and cross-step fields.** What a marker records that one call can settle (a part's mark by remove, swap, poke) and what needs a target carried across steps (the same-explanation verdict, pairs that pull, the best rival).
- **The six unknowns, Q1 to Q6.** The owner's sentences in decision H6, numbered in the plan so it can be held to them.

## Traps
- **Reading the sketch in the plan (M1 to M10, the skill map table) as the model.** They are what the judges cut. The model is phase 1's file, when it exists.
- **Counting the unknowns answered.** One the theory cannot reach matters more than five it can.
- **Reading this folder's name as the LEGEND's kind "Workflow".** See the second paragraph above.
- **Editing another project from here.** HV file 33 and Planning file 2 are frozen and theirs; the asks are in RELATIONS.
