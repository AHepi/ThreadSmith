# S123 What knowledge could mean in Avida: how the replies will be refined, written before sending

*Log S123, 2 October 2026 (decisions S77, S78, S79). Written by the one S123 agent before any brief was sent, so that the reading of the four replies cannot be shaped by what they say. It follows the checks of S120 and S122 (each reply checked against Avida's source at commit 47f13dad and against the record; what it ran reproduced; its sources spot-checked) and adds what S77 asks next: the replies compared and merged into one refined hypothesis. The briefs are in `tests/S123 Briefs for GPT 6 Astra/`; the rivals and transports are those of `results/S123 What knowledge could mean in Avida - how best to find out, and whether the trajectory is sufficient.md` (the assessment). Nothing here decides what the owner left open. If the owner changes the plan, the change is recorded with the date before any reply is opened.*

## 1. Who does it

One Opus agent for the whole reading (S56, S68), started when the replies are in and no more than one other agent is running; no GLM check unless the owner asks (S70's latest word). Replies are kept unchanged in `tests/S123 Returns from GPT 6 Astra/`, Word files with their text extracted beside them; code blocks extracted unchanged into `tools/s123/<nn>/` with a byte-for-byte check, as S122 did.

## 2. How each reply will be checked

Each reply gets a check file, `results/S123 Checking the Astra returns/<nn> Check of reply <nn> - <title>.md`, with these parts, in this order:

1. **What it offers**, in a table, against the brief's question.
2. **Its claims about Avida**, each against the source at 47f13dad (file and line), counted: holds, in part, does not hold.
3. **Its claims about the semantics**, each against the attached text by line and the formal core by definition id: does it use "transport", "selected", "constructed", "declared", "representation", "prediction" and "surprise" as defined (L181-225; D5.1, D12.1-D12.7)? Does it keep representation apart from a correspondence that merely holds? Does it give results under Reading A and Reading B where they differ? Does it say what its tests test and do not test, and does that match what the tests could bear on (the reader's guide, section 14)? Each misuse is listed with the line it contradicts.
4. **Its claims about the books and Pinker**: quotations checked against the books (at most 25 words in a row; never more is copied into the repository); Pinker claims checked against the S124 record, keeping its checked and unverified marks; any new outside source opened where it can be and marked.
5. **What it ran**, reproduced where the code is given (the S120 and S122 standard: identical output, or the difference stated); what it did not run but presents as a result is flagged.
6. **Its tests**: for each, whether it is well formed (set-up, expected outcome, control, what counts against, cost), which rival hypotheses (H1 to H6) it can split, and whether its control separates what it claims to separate (S122's lesson: the memory-wiped control removed more than memory; counting reads earned the history tasks).
7. **Grades**: whether its grades of naming (1, 2, 3) and, for brief 03, its effect grades (E1 to E3) are used strictly.
8. **Strengths and weaknesses**, in a few lines.

**Pilots.** At most one small pilot per reply, routine only (under about 3 CPU-hours, no new C++ beyond a reply's own small patch, no change to a reply's design), with what would count written and committed before it runs, as in S120 and S122. Everything costlier waits for the owner's word.

## 3. How the four will be compared

A table, `results/S123 Checking the Astra returns/00 The four replies compared, and the refined hypothesis.md`, with one row per rival hypothesis (H1 to H6) and one column per reply. Each cell: **for** (a checked argument or a reproduced result that the hypothesis predicts and a rival does not), **against** (its stated counter-observation, found or argued), **silent**, or **bears, unchecked** (a proposed test not yet run). Only checked items count; a claim the check found not to hold is listed and not counted. A second table does the same for the transports L1 to L7 (present, added by a patch, missing, disputed) and for the six readings left to the owner (each reply's option on each, listed, not chosen).

## 4. How they will be merged into one refined hypothesis

1. Drop every rival that a checked argument or a reproduced result counts against, saying which and why.
2. Of the rest, keep the parts that the replies' checked material bears on, and state them as one hypothesis of what knowledge could mean in Avida, in the form the assessment used: what it says, what it predicts in a named Avida set-up, what would count against it, and which meaning of knowledge (K-CT, K-D, K-O3, K-P, K-Sem) it is a hypothesis about.
3. Make it as hard to vary as the material allows: for each part, say what in the material it rests on; a part that could be changed without changing any prediction is named as such (the semantics' "no work by itself", L313).
4. Where two survivors remain that no checked material separates, keep both, as a problem in the semantics' sense (L317), with the test that would separate them.
5. State it twice where the owner's open readings change it (Reading A or B; the two readings of "Avida itself"), never choosing between them.

## 5. What would count as the refined hypothesis surviving or failing

- **Surviving the reading**: no checked claim counts against it; at least one test that could count against it is well formed and costed; it says which meaning of knowledge it concerns.
- **Failing the reading**: a checked reply argument or a reproduced result is the observation it names as counting against it; or it turns out to depend on a misuse of a semantics term found in section 2, part 3.
- **Surviving a run** (later, on the owner's word): the pilot's written expectation is met, and its stated counter-observation is not made, in every seed run.
- **Failing a run**: the counter-observation is made in a seed, or the control shows the effect without the factor the hypothesis names.
- **Neither**: the run was too weak to make either observation (S122's weak-pay pilot is the example); reported as such, not as survival.

## 6. What the next round would ask

Written now as options, to be revised by what the replies say:

1. If **H5** survives (outside data matter): the outside-stream run of brief 01 (a small patch on the `ANTICIPATE_MODE` model, a recorded stream, a matched internal stream, held-out stretches), then a second channel.
2. If **H2** or **H3** survives: the outward elimination and transplant runs of brief 03, with blind replay controls.
3. If **H6** survives: a within-lifetime learning set-up (patterns varying between generations, holding within a life), and the construction criterion of brief 04 applied to what appears.
4. If **Avida is judged unable** to carry what the surviving hypothesis needs (brief 02's criteria): the options for another environment, with their costs, put to the owner; nothing is built before the owner chooses.
5. In every case: four new briefs, each aimed at the surviving rivals, asking the questions the first round left open, written for a fresh Astra with this round's checked findings.

## 7. Plain file

When the reading is done: a plain-words file (under about 1,000 words) with the main point, one example step by step, what the four replies found, the refined hypothesis in plain words, tested / not tested / unsure, and one next step; then log entries in both project stories, and Status, INDEX and README updated.
