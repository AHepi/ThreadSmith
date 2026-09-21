# H62 Results - the Sonnet 5 arm of plans H56 and H58, as Claude Code subagents

Written 21 September 2026, after twenty-four Sonnet 5 runs under addendum H61 (twelve under skill file 30, twelve under file 31), marked by the same marker as files 54, H57 and H59, every claim checked against the source text with every hit printed. Raw returns: `rigs/plan 49 rig - DeepSeek on outside papers/runs_sonnet5/` and `runs_sonnet5_31/`, each reply the file the reader wrote; `sonnet_agent_tool_audit.txt` (every tool call each reader made, checked against the files it was allowed); `sonnet_check.txt` (shape by program). The transport is the session's Workflow tool with the model pinned to Sonnet at effort high; the model id is expected to be `claude-sonnet-5` and was not verified. The DeepSeek counts (H57, H59) and these are never added together.

## The short answer
- **Under file 30, neither break appeared in Sonnet 5.** Break 1 (the flip on the derived disjunction treated as a fault): 0 of 3 in P3 mode 1, 0 of 3 in mode 2; every run read the trilemma as a real fork. Break 2 (*fixed* on a design choice): 0 of 6 on F4. One run put *fixed* on the Psychologist's threshold patch ("Fixed / catch-all with no gauge", F4 mode 2 repeat 2): not the frozen break, but the same stretch H57 found in DeepSeek, *fixed* for an untested say-so.
- **Under file 31, neither break appeared either.** Break 1: 0 of 6, and all six P3 runs named the conclusion derived and used drop-a-condition in place of the flip, with the reason given. Break 2: 0 of 6, and *fixed* was not used on F4 at all.
- **Two new faults under file 31, both tied to the new wording**, one run each: *Asserted* promoted into the mark column ("'Presentation below the threshold' | Asserted; catch-all with no gauge", F4 mode 1 repeat 3), and *fixed* put on the derivation itself ("The core derivation | Fixed / derived | It is an algebraic consequence of the definitions", P3 mode 2 repeat 1). Plan H58's prediction 4 allowed at most one such fault in twelve; there were two. The wording that closed the two DeepSeek breaks has a cost in this reader. Whether it outweighs what it closed is the owner's call, as plan H58 said.
- All twenty-four FULL in shape; no CANNOT; the router opened `by-domain.md` in all twelve mode 2 runs. Three misreads, all attributions of the "earlier Thursdays" objection to Filby (it is the narrator's: "'But,' said I, 'If it travelled into the past it would have been visible ... last Thursday'"). No claim invented.

## What is different about these runs, and what it did
Addendum H61 lists eight differences from the plans. Three of them showed:
1. **The readers had tools, and used them to count words.** Twenty of twenty-four ran `wc -w` on their own reply, and six edited it down. Under file 30 one run of twelve exceeds 1,200 words; under file 31, four. Plan H56's prediction 6 (over the limit in at least half) is **not borne out**, and cannot be read: the plans' reader could not count.
2. **One reader looked outside its files.** P3 mode 1 repeat 1 under file 31 ran `git log --oneline -10` and `find . -maxdepth 2` before reading its prompt. It saw commit subjects ("break 2 recurred once, skill file 31 forced"; "neither break recurred under file 31") and top-level folder names, not what the breaks are and no file's contents. Its report shows nothing that could come from that. Recorded as the exposure the addendum warned of; every count below is given with and without it, and they are the same.
3. **One reader wrote its report through the shell** (F4 mode 2 repeat 3 under file 31, a `cat` heredoc after a draft under /tmp) instead of the Write tool. The file is what it wrote; nothing else differs.
No other reader read any file but its prompt and, in mode 2, the references folder; the audit file lists every call.

## The table, file 30
| Run | Words | Modules opened | Flip on P3 / fixed on F4 | "Same explanation at this level" | Claims checked |
|---|---|---|---|---|---|
| P3-m1-r1 | 1,178 | (pasted) | "The structure does not bend to fit any outcome; it produces a genuine three-way fork" | no | strong form of P1 dropped by the author SUPPORTED; "no tendency to make us 'go crazy'" SUPPORTED |
| P3-m1-r2 | 1,055 | (pasted) | flip run on the compute premise: "it genuinely depends on the 'immense computing power' premise" | no | "space does not permit a recapitulation" SUPPORTED; "about 100 billion times as many me-simulations" SUPPORTED |
| P3-m1-r3 | 1,005 | (pasted) | "had N̄I been small, the same machinery would not have produced an extreme trilemma" | no | Self-Indication Assumption named as absent from the text: OUTSIDE, flagged by the reader |
| P3-m2-r1 | 1,196 | idea, question-bank, by-domain, reporting | "the core deduction (C) does not flip" | no | "not philosophically necessary" SUPPORTED; "apportion credence roughly evenly" SUPPORTED |
| P3-m2-r2 | 1,127 | idea, by-domain, question-bank, testing-against-cases, reporting | "The disjunction still bites ... the argument passes this test"; P1 marked *Fixed* on "take it as a given" | no | "less than one millionth" SUPPORTED; the existential-risk footnote SUPPORTED |
| P3-m2-r3 | 999 | idea, by-domain, reporting | "direction is forced by the actual size of N_I, an empirical input" | no | "reliably enforced laws that prevent such individuals from acting" SUPPORTED |
| F4-m1-r1 | 1,205 | (pasted) | no *fixed* | yes ("by the method's own rule, the same explanation at this level") | Filby's conjuror and the narrator's "no trickery" SUPPORTED |
| F4-m1-r2 | 1,165 | (pasted) | no *fixed* | no | "the Psychologist looked under the table afterward" SUPPORTED; "no one checked the table beforehand" OUTSIDE (the invitation is in the text; whether anyone did is not) |
| F4-m1-r3 | 1,171 | (pasted) | no *fixed* | in substance ("the excerpt has not told them apart") | "after Filby objects that a machine travelling into the past should have sat visibly" MISREAD (the narrator's objection) |
| F4-m2-r1 | 1,082 | idea, by-domain, reporting | no *fixed* | no | "helps the paradox delightfully" SUPPORTED; "a vague inkling of a machine" SUPPORTED |
| F4-m2-r2 | 1,192 | idea, by-domain, question-bank, reporting | **fixed** on P6, the threshold patch (the H57 stretch, not the frozen break) | no | "too clever to be believed" SUPPORTED; "Filby's ... obvious question" MISREAD (the narrator's) |
| F4-m2-r3 | 1,200 | idea, by-domain, reporting | no *fixed* | yes ("at the level of what makes the room believe him") | the injuries from the overset machine and hail SUPPORTED; the search under the table SUPPORTED |

## The table, file 31
| Run | Words | Modules opened | Flip on P3 / fixed on F4 | "Same explanation" | Claims checked |
|---|---|---|---|---|---|
| P3-m1-r1 (exposed, see above) | 1,089 | (pasted) | "not applicable as usually run ... The right proof-domain test is drop-a-condition"; *fixed* on the "no distinguishing information" scope clause, proper | no | f_P = f_I = N_I = 1 gives f_sim = 0.5, correct; Hanson on consequences of (3) SUPPORTED |
| P3-m1-r2 | 1,031 | (pasted) | "the right tests are the proof tests ... not flip-the-outcome"; P1 *Fixed* on "take it as a given", proper | no | "not entirely uncontroversial ... take it as a given" SUPPORTED |
| P3-m1-r3 | 1,137 | (pasted) | "Flip: does not apply to P6, since it is derived" | no, explicitly ("a genuine fork, not 'the same explanation at a finer grain'") | "many humans who would like to run ancestor-simulations if they could afford to" SUPPORTED |
| P3-m2-r1 | 1,212 | idea, by-domain, question-bank, reporting | flip declared not for the derivation, applied to Section VI instead; **"Fixed / derived" on the derivation: new fault** | no | "the junk-DNA swap case" called the rival the author builds: MISREAD (the junk DNA is the analogy for the principle; the rival is the Doomsday sampling premise) |
| P3-m2-r2 | 1,105 | idea, by-domain, reporting | "not the right test here — the trilemma is a derived conclusion" | no | Drexler, Bradbury, Lloyd, Moravec SUPPORTED; "not that radical" SUPPORTED |
| P3-m2-r3 | 1,056 | idea, by-domain, reporting | "drop conditions instead ... Dropping P1 or P4 breaks the argument" | no | footnote 11 SUPPORTED; Boltzmann brains OUTSIDE, flagged by the reader |
| F4-m1-r1 | 1,208 | (pasted) | no *fixed*; names and the year "Loose, and free" | no | "a pork-butcher could understand Filby", "Wait for the common sense of the morning", Blank, Dash and Chose, greyer hair, the Silent Man SUPPORTED |
| F4-m1-r2 | 1,108 | (pasted) | no *fixed*; "Rival unbeaten" used as a mark (not one of the eight) | no | "Filby became pensive" SUPPORTED |
| F4-m1-r3 | 1,207 | (pasted) | no *fixed*; **"Asserted" used as a mark: new fault** | no | "Has he been doing the Amateur Cadger?" SUPPORTED; hair "greyer" SUPPORTED |
| F4-m2-r1 | 1,182 | idea, by-domain, question-bank, reporting | no *fixed* | no | "wooden account" SUPPORTED; Filby's red hair SUPPORTED; the Provincial Mayor SUPPORTED |
| F4-m2-r2 | 1,222 | idea, reporting, by-domain | no *fixed* | no | "an odd twinkling appearance ... in some way unreal" SUPPORTED; Weena's flowers OUTSIDE, flagged by the reader |
| F4-m2-r3 | 1,142 | idea, by-domain, reporting, word-list, question-bank | no *fixed* | yes | Newcomb SUPPORTED; "Filby's: 'we'd have seen it on earlier Thursdays'" MISREAD (the narrator's) |

## What this reader found that the other did not
- **The equivocation in "our consciousness moves along it"**: experience against matter. "Swap 'moves along it' for 'observes it' and the sentence sounds equally persuasive, but they're different claims ... The argument needs the second (a machine moves matter through time) but only defends the first" (31/F4-m1-r2). DeepSeek had the neighbouring finding, that the "except" clause does all the work.
- **Swap the subject** (30/P3-m2-r3): run the same steps on any copyable thing that outnumbers its originals and the identical trilemma comes out; "the paper's distinctive contribution is therefore smaller than its framing suggests — the novel work is the numbers and the substrate-independence premise, not the logical form." And "interested but capped" civilisations as a gap between the algebra and the English labels.
- **The closing "roughly evenly" as the loosest sentence**, found in most P3 runs, once beside the tightest one (31/P3-m2-r1: "the loosest sentence in the piece, sitting right next to the tightest one").
- **The frozen question moved on F4.** Two runs under file 31 (m1-r1, m2-r1) froze "why does the room, or the reader, come to believe him" and tested the chapters as creative choices; the other ten, and all twelve DeepSeek runs, froze the Time Traveller's argument. The skill's framing allows either. Those two reports are FULL and their marks are on different parts (the panel of sceptics, the persistent mockery, the sensory ride).
- **Convergent with DeepSeek**: the trichotomy is exhaustive only given N_I large (31/P3-m1-r1's counter-case f_sim = 0.5; DeepSeek H57 m1-r3, m2-r1); the threshold patch as an ungauged catch-all supplied by a listener; the conjuring rival never separated by any change on the list.

## Predictions, marked
- H56, prediction 5 (Sonnet: break 1 in none of three P3 mode 1; break 2 in at most one of three F4 mode 1; all FULL; `by-domain.md` opened on both papers): **borne out** in every part.
- H56, prediction 6 (over 1,200 words in at least half): **not borne out** (1 of 12), and confounded by the readers' counting.
- H56, prediction 4 (the same-explanation verdict at least once per paper, each reader): **half borne out** for Sonnet: F4 yes (three runs under 30), P3 no (none in twelve).
- H58, predictions 1 and 2 (neither break under 31; the flip redirected, not dropped): **borne out** (0 of 6 each; six of six redirected with the reason).
- H58, prediction 3 (*fixed* used properly at least once on F4): **not borne out** for Sonnet (never used on F4 under 31; used properly on P3 twice).
- H58, prediction 4 (no new fault in more than one of twelve): **not borne out** (two, quoted above).
- H58, prediction 5 (all FULL, none empty, no CANNOT): **borne out.**

## What this does not show
- The plans' Sonnet 5: this is the same model through a different door (addendum H61). `run_sonnet.py` remains for the day a key is supplied.
- Anything about repeatability beyond three per box.
- A second marker. The marker wrote the skill and both changes.
- Whether the two new faults recur: one run each.
- Blinding: the marker saw file names and versions.

## Traps
- Adding these counts to H57's or H59's. Plan H56 forbids it, and the transports differ.
- Reading "0 of 6 under file 30" as file 31 unneeded: the DeepSeek break recurred under file 30 (H57), and this reader shows the same stretch of *fixed* on an untested say-so.
- Reading the two new faults as the wording's alone. Each is one run; each is also the kind of stretch this reader made under file 30 ("fixed/self-declared idle", 30/P3-m2-r1; "Rival unbeaten" as a mark, 31/F4-m1-r2, which the new wording did not invite).
