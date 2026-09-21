# 51 Pilot results - nine runs on three outside sources

Phase 1 of plan 49, run 20 September 2026. Three sources by three modes, one run each. Nothing in this file changes plan 49.
Reader: DeepSeek V4.1 Flash (`deepseek-flash`), thinking on, effort high, one system message and one user message, a fresh conversation each time.
Sources, each sent with its provenance header stripped: **S7** Bialy and Loeb on 'Oumuamua (3,732 words, a paper), **F1** Poe's *The Philosophy of Composition* (4,842 words, a story-maker explaining his choices), **R1** *Nix v. Hedden* (553 words, a rule).

## What happened

| Run | Words | Seconds | Calls | Modules opened by the reader |
|---|---:|---:|---:|---|
| S7 mode 0 | 795 | 34 | 1 | - |
| S7 mode 1 | 973 | 36 | 1 | - |
| S7 mode 2 | 995 | 35 | 2 | the idea in depth, question bank, by domain, word list, reporting |
| F1 mode 0 | 925 | 24 | 1 | - |
| F1 mode 1 | 1,094 | 46 | 1 | - |
| F1 mode 2 | 1,329 | 49 | 2 | the idea in depth, reporting |
| R1 mode 0 | 818 | 19 | 1 | - |
| R1 mode 1 | 1,003 | 44 | 1 | - |
| R1 mode 2 | 1,183 | 43 | 6 | the idea in depth, by domain, question bank, reporting, word list, testing against cases |

Nine runs for six cents at off-peak prices: 37,632 word-pieces served from the cache, 134,668 not, 60,505 out. At this rate the whole corpus under three modes costs about one dollar.

## Did the introduction work?
This is what the pilot was for. All six things watched for in plan 49, checked across all nine replies:

| Watched | Result |
|---|---|
| The reader judges the method instead of the document | did not happen in any run |
| The reader asks for the source theory that is not supplied | did not happen in any run; the framing's last sentence appears to have done its job |
| The reader ignores the modules and gives a generic critique | did not happen; modes 1 and 2 use the method's own steps and marks |
| The reader repeats the author's own tests as if they were its own | did not happen in these three; in S7 the reader took the paper's argument against outgassing and turned it back on the paper's own mechanism |
| The reply runs past the ceiling | no; the longest was 1,329 words against a 1,200-word instruction, so the instruction is treated as a guide rather than a limit |
| The "never" wording confuses the reader | nothing visible; this is a conversation-mode risk and conversation mode has not been run |

## What the three modes did differently
Mode 0 wrote a competent critique in its own shape: what works, what is loose, what would test it. It used none of the method's structure and none of its marks.

Mode 1 and mode 2 both froze the question, listed parts and jobs, ran the named tests, put one of the eight marks on each part, and closed with what would tighten the explanation, what the test cannot show, and one next step. Mode 2 was longer in every pair and, on two of three sources, went further: on the tomato case it reached the finding that the court's test and "the court's own table manners" are **the same explanation at this level**, because on that record the only reading of common usage is the judges' own. That is the skill's *build the best rival* step arriving at its hardest verdict, and mode 1 did not reach it.

Mode 2's router worked without being told what to open. On the rule case the reader opened six modules, among them the domain file and the testing file; on the story it opened two. Nothing in the framing names the modules, so the choices came from the skill's own table and map.

## What the pilot does not show
- Nothing about whether any finding is **right**. No reply has been marked. The marking plan (file 52) is written and frozen before any of this is scored.
- Nothing about the other forty-six sources, or about long documents: the three here are 553 to 4,842 words, the corpus runs to 18,000.
- Nothing about the conversation mode, where the skill's questioning half and its negative wording would be tested.
- One run per box, so nothing about how much two runs of the same box differ.
- The reader and the marker share a maker with the skill. The pilot does not reduce that.

## Two things to fix before phase 2
1. **The word ceiling is soft.** Every mode 2 reply ran over 1,200 words. Either the instruction stands as a guide and the reports are longer, or the ceiling is enforced. Recommended: leave it, and record length as a finding rather than a fault.
2. **Mode 0 is visible to the marker.** Its reports have no marks and no frozen question, so a marker can always tell mode 0 from the other two. Modes 1 and 2 are the pair that matters and they can be told apart only by the module list, which the hider strips. Recorded in file 52.

## Traps
- Reading a fuller report as a better one. Length is not a finding.
- Reading mode 2's win on the tomato case as the router's doing. One case, one run.
