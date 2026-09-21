# H56 Plan - repeatability of the two breaks, P3 and F4 three runs each

Written 21 September 2026, before any run is sent. Once the first run goes out, this file stays as it is. It is the one next step file 54 named, made into a frozen plan; it answers under plan 52's marking rules and changes none of them.

## The question
File 54 found two breaks in the skill's wording, each seen once, in one run each:
- **Break 1 (P3, mode 1).** The flip test, "Had the opposite happened, could the same explanation have covered it? If yes, it explains nothing" (SKILL.md, whole-explanation checks), fired on Bostrom's disjunction, a conclusion derived from a count. The mode 2 and mode 0 readers on the same paper read it correctly ("the argument partitions rather than absorbs").
- **Break 2 (F4, mode 1).** The two-lever machine, a free design choice, was marked **fixed** ("A design choice; either lever could be reversed and nothing breaks"), where the skill reserves *fixed* for a requirement the owner set and did not test.

One run per box cannot say whether these are the skill's doing or the run's. The question: **how often does each recur when the same paper is read again under the same mode, skill unchanged?**

## What is fixed
- Authority: skill file 30, unchanged; the runner diffs its copy against `authority/hard-to-vary/` and refuses to send if they differ.
- Readers, two: `deepseek-flash` (V4.1 Flash), thinking on, effort high, ceiling 24,000, as in plan 49; and **Claude Sonnet 5** (`claude-sonnet-5`, decision H3, added to this plan before any run was sent), adaptive thinking with the summary kept, effort high, ceiling 24,000, streamed, through the Anthropic SDK (`run_sonnet.py`). Same framing text, same modes, same tool for mode 2. Sonnet 5 has never read this skill in the record; this arm is both a repeatability check and a first reading. Not Opus 5, and never a Fable 5.1 subagent (decision H4).
- Sources: P3 (Bostrom 2003, pdf) and F4 (Wells 1895, Gutenberg, capped at 9,000 words), rebuilt by `fetch.py` from the manifest in `sources.json`; the texts are not kept.
- Framing text: word for word as in `run.py`, unchanged since plan 49.
- Runs: P3 and F4, modes 1 and 2, three repeats each: twelve runs per reader, twenty-four in all. (File 54 said "three more runs each under modes 1 and 2"; read as three per mode, so that each break is looked for three more times in the mode that produced it and three times in the other.) Mode 0 is not run: neither break is the bare reader's.
- Output: `runs_repeat/<source>-m<mode>-r<k>.json` (DeepSeek) and `runs_sonnet5/<source>-m<mode>-r<k>.json` (Sonnet 5), k = 1, 2, 3, kept as they came; the original runs in `runs/` untouched. An empty reply is kept and run once more, as in log 54.
- Marker: the same marker as file 54 (Claude, who wrote the skill), reading each report with the two original reports beside it, every claim about the document checked against the text with every search hit printed (Lesson 46).

## What counts as a recurrence, decided before reading
**Break 1 recurs** in a report when the flip test is run on the paper's disjunctive conclusion (or the trilemma as a whole) and the report treats the disjunction's covering every outcome as a fault of the explanation (words to the effect of "covers the opposite", "explains nothing", "weakest joint", or a mark of *loose* or *idle* on the disjunction for that reason). It does **not** recur when the flip is run and the report says the argument partitions, or runs the flip on some other part, or does not run the flip.

**Break 2 recurs** in a report when any part that the document presents as a design choice (the levers, the machine's form, the saddle, the model's construction) carries the mark **fixed**. It does **not** recur when *fixed* is put on a stipulation the narrator asks the company to grant (the four-dimension premise, "the owner set it and it was not tested"), which is the mark's proper use; the original F4 mode 1 report did both, and only the levers count.

Each report gets, in addition: shape (FULL, PART, NONE, by program then by eye), word count, finish reasons, modules opened (mode 2), and up to three claims checked SUPPORTED, MISREAD or OUTSIDE under plan 52's rule. No totals across the runs; the two counts of recurrence are reported as counts of three, per mode, per reader. The two readers are read side by side and never added together: a break that recurs in one reader and not the other is reported as that, and is a fact about the skill's wording only where it recurs in both.

## Predictions, frozen
1. Break 1 recurs in at least one of three P3 mode 1 runs, and in none of three P3 mode 2 runs. (The router opens `by-domain.md`, whose proofs section gives the right tool; the pasted-whole reader has it too but the main file's flip comes first.)
2. Break 2 recurs in at least one of three F4 mode 1 runs. No prediction for F4 mode 2: the original mode 2 report used *fixed* only of the outcome, and one run is not enough to guess from.
3. Every run is FULL in shape; no run returns empty; no CANNOT mark appears.
4. The "same explanation at this level" verdict (a conjuring trick against a time journey, F4; the trilemma's three arms, P3) appears in at least one skill-mode run per paper, in each reader.
5. Sonnet 5: break 1 recurs in none of three P3 mode 1 runs (a reader that has seen more proofs treats a derived disjunction as a partition without being told). Break 2 recurs in at most one of three F4 mode 1 runs. Every Sonnet 5 run is FULL in shape, and its mode 2 router opens `by-domain.md` on both papers.
6. Sonnet 5 reports run longer than the 1,200-word instruction in at least half of its runs (the DeepSeek mode 2 reports did in every pilot run; a stronger reader is not a shorter one).

## What follows from the result
- **If either break recurs at all** in these runs, in either reader: apply changes 1 and 2 from file 54 as skill file 31, and run the same twelve again under file 31 (a further frozen plan; not this one).
- **If neither recurs**: both changes stay held in file 54; the record says the two breaks were seen once each and not again in three tries per mode, which is not proof the wording is sound, and the next test of the skill is chosen on other grounds.
- Predictions are ticked against the result in the results file, one line each.

## An observation made before the run, recorded here so it is not made after
File 54's change 2 says to "put 'free is loose; inherited is fitted; a free choice is never *fixed*' into the design section of `by-domain.md`". That section (by-domain.md, section 2, "Designs and plans") **already** carries "in the eight marks used elsewhere in this skill, *free* is loose and harmless, and *inherited* is fitted". So the reader that broke had the mapping in front of it under mode 1. If break 2 recurs, change 2 in its file 54 form is not the fix; the marks table in `reporting.md` (where *fixed* is defined as "the owner set it as a requirement and it was not tested") is the more likely place for one clause, "a designer's free choice is loose, never fixed". This is noted, not decided; the decision waits on the result.

## What this does not test
- Whether the breaks recur under a different effort setting, or in readers other than these two.
- Change 3 (look inside), which has no single-document test here.
- A second marker. The marker wrote the skill.
- Anything about the 47 other sources.

## Traps
- Counting a *fixed* on the four-dimension premise as break 2. That is the mark's proper use.
- Counting a flip that is run and passed as break 1.
- Adding the two readers' counts together, or reading Sonnet 5's summarised thinking as its reasoning (the API returns a summary, not the chain).
- Reading the original P3 and F4 reports as a fourth run of each. They were one run each, under the earlier unstreamed runner (`run_v1_unstreamed.py`); the twelve here run under the streamed patch verified in log 54.
- Editing this file after the first run goes out.
