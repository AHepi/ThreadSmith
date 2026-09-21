# 53 Corpus run - what happened, before any report was marked

Phase 2 of plan 49, run 20 to 21 September 2026 on the owner's word ("Great. Do it"). This file records the run itself and what a program can see in the replies. No report has been read for its content and no mark from plan 52 has been given.

## The run
- 49 sources x 3 modes = 147 runs, ten at a time, 89 minutes of reader time summed, about 55 minutes on the clock.
- One transient service error (a 502 on S2 mode 2), retried by the runner and recovered.
- Two runs came back with thinking and no report: P6 (Swift) and S12 (Feynman), both mode 1. Their reasoning stops mid-sentence, so the service cut the reply before the report began; nothing in either trace refuses or wanders. Both first results are kept as they came (`runs_first_attempts/`) and each was run once more; the second attempts returned reports of 844 and 1,103 words and are the ones on file. This is the only patch to the run, it is in the rig layer, and it gives up nothing.
- Cost: 1,986,304 word-pieces served from the cache, 2,350,937 not, 913,419 out: about 91 cents at off-peak prices.

## What a program can see
Shape by program means: the report's seven headings, the eight marks, and "the question, frozen" found by pattern. FULL needs six headings and three marks. This is not a mark of quality; it says whether the reader produced the method's form.

| Mode | FULL / PART / NONE | Words, average | Marks used, average | Tests named, average |
|---|---|---:|---:|---:|
| 0, no skill | 0 / 49 / 0 | 836 | 1.3 | 0.5 |
| 1, skill pasted whole | 40 / 9 / 0 | 986 | 5.4 | 7.1 |
| 2, router live | 49 / 0 / 0 | 1,078 | 5.9 | 6.8 |

Mode 1's nine PART reports: C1, C2, C6, C7 (four of the seven computability sources), S1, S4, S7, S18, E2a. Whether these are a shortfall or a fitting of the form to a proof is a close-marking question; it is noted here because it clusters on proofs and long papers.

**The router, mode 2.** Every one of the 49 runs opened at least one module; the average was 4.3 calls, the most 6. The idea-in-depth file and the reporting file were opened in all 49; the domain file in 47; the question bank in 39; the word list in 19; the testing-against-cases file in 6. So the router sends the reader to the same three modules almost every time, uses the question bank in four runs out of five, and reaches the testing module rarely, which fits its row (only when the reader is about to check a claim against cases). No run asked for the source theory the word list points to.

**Length.** 8 of 147 reports ran past the 1,200-word instruction, all under 1,330 words. Recorded, not a fault.

**The verdict line.** The framing asked for the skill's report form, which ends in "what would tighten it", "what this does not show" and "one next step" rather than a one-word verdict. So plan 52's "verdict, recorded as given" will be read from those closing parts, not from a RELY/SET ASIDE line, which 145 of 147 reports do not carry.

**Lines where the reader says a test has no purchase** (plan 52's CANNOT mark), found by pattern: two, and both are the reader adapting rather than stopping: on the tomato case, "you cannot poke the world and watch the verdict move; you rewrite the rule"; on modified gravity, "since galaxies cannot be poked, the change list is made of comparisons". Both are what the skill's domain file says to do. The real CANNOT marks, if any, will come from close reading, not from this pattern.

## What is ready for phase 4
- `marking/to_mark.md`: the 48 close-marking reports (sixteen sources drawn before the run, three modes each), mode labels and module lists stripped, shuffled with an unrecorded seed, numbered. Mode 0 stays visible by its shape, as plan 52 says.
- `marking/marks.csv`: the empty sheet with plan 52's columns.
- `marking/shape_by_program.json`: the light marks for all 147.
- `marking/secret_mapping.json`: not to be opened until the sheet is full.

## What this file does not say
Nothing about whether any report is right, sharp, or empty. That is phase 4, under plan 52, and it has not begun.
