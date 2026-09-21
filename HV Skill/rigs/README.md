# Rigs - the programs and raw returns behind the skill tests

Three rigs, one per test. Raw returns are kept as they came; the reading of each is in `results/`. Numbers are log entries.

## plan 42 rig - DeepSeek, unrun
The runner, hider and table-maker built for plan 42 with corpus 43 (log 47). `passages.json` is what a reader would be sent; `keys.json` is the answer key and is never sent. `skill_with_line/` is the skill with the one proposed poke line added (setup 3); setup 2's skill is the authority copy in `../authority/`. Dry-run on a stub reply only; nothing was ever sent to DeepSeek from this rig.

## plan 48 - Claude readers, stopped
Sixteen well-built cases (`cases.json`, keys inside; `passages_only.json` is what the reader saw), the 48 prompts, and the 31 replies written by fresh Claude agents before the owner stopped the run (log 48). Unmarked. Setup C's prompt named the owner's authority document, file 10, which is not in this repository.

## plan 49 rig - DeepSeek on outside papers
- `sources.json`, `fetch.py`: the manifest and fetcher for the 49-source corpus (file 50). **The fetched texts are not kept here**: they are other people's papers, public domain, open access or author-posted, and `fetch.py` rebuilds them from the addresses in the manifest.
- `run.py`: the streamed runner, three modes (0 no skill; 1 skill pasted whole; 2 router live through an `open_module` tool). `run_v1_unstreamed.py` is the runner as it ran phase 2, before the patch of log 54. `runs_verify/` is the one run that verified the patch.
- `runs/`: all 147 single-shot returns, one JSON per source and mode, with the reply, the reader's thinking, the modules it opened, finish reasons where recorded, and usage. `runs_first_attempts/`: the two empty returns (P6, S12, mode 1), kept as they came. `runs_phase2.log`: the run log.
- `conv.py`, `conv/`: conversation mode, twelve dialogues, reader and author transcripts with the final report.
- `shape.py`: light marking by program. `hide.py`: the hider for the close-marking sample. `close_marking_sample.json`, `conversation_sample.json`: the draws, with the rule and seed.
- `marking/`: `to_mark.md` (48 reports, labels hidden, as the marker saw them), `secret_mapping.json` (opened after marking), `close_marks_all.json` (the marks as given, with the marker's corrections noted in place), `close_marks_restored.json` (the same with the labels back), `shape_by_program.json`, `cannot_candidates.json`, the staged batches.

The key for DeepSeek's service was read from the environment and is in no file here.
- Plan H56 (repeatability of the two breaks): `run.py` with a repeat index writes to `runs_repeat/` (DeepSeek); `run_sonnet.py` writes to `runs_sonnet5/` (Claude Sonnet 5, Anthropic SDK); `repeat_check.py` prints shape by program and the flip and *fixed* passages for the marker; `runs_repeat_h56.log` and `runs_repeat_check.txt` are the DeepSeek run as it happened. A fresh session needs `requests` and `pymupdf` (Lesson H1), and `anthropic` for the Sonnet runner. Both runners diff the `skill/` copy against the authority before any call and send nothing if it differs.

## Inside the skill rigs - the names
- `runs/<source>-m<mode>.json`: one DeepSeek return; `source` is the id in `sources.json` (S1 to S18 science, E economics, P philosophy, C computability, F fiction, D design, R rules, I instructions; `b` a paired critique), `mode` 0 no skill, 1 skill pasted whole, 2 router live. `conv/<source>-conv.json`: a conversation dialogue with its report.
- `marking/to_mark.md` is what the marker saw (labels hidden); `secret_mapping.json` restores them; `close_marks_restored.json` is the marks with the labels back.
