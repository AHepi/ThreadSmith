# H61 Addendum to plans H56 and H58 - the Sonnet 5 arm run as Claude Code subagents

Written 21 September 2026, before any Sonnet 5 run, on the owner's word ("Run sonnet 5, now"; then subagent access granted). Plans H56 and H58 say the Sonnet 5 arm goes "through the Anthropic SDK (`run_sonnet.py`)". No Anthropic credential exists in the session, so that runner cannot send. The transport available is the session's Workflow tool, which spawns Claude Code subagents with a named model; decision H4 permits Sonnet and bars Fable 5.1 and Opus 5, so every agent in the run is pinned to Sonnet. This addendum says what is different, what it gives up, and what stays the same. Once the first run goes out it stays as it is.

## What is different from the plans
1. **The reader is a Claude Code subagent**, not a bare API call. It carries Claude Code's own system prompt and has tools. The plans' reader had only the framing text and the document.
2. **The model is "sonnet" as the Workflow tool names it.** The expectation is Claude Sonnet 5 (`claude-sonnet-5`); the exact model id is not verifiable from inside the run and is recorded as expected, not seen.
3. **Effort is set to high**, as the plans said. Thinking cannot be configured and nothing of it is returned or kept; the plans kept the summary.
4. **No finish reason, no usage, no timing** comes back. An empty or cut reply shows only as a short file.
5. **The framing text and document are read from a file**, not passed as system and user messages: each run's prompt file holds, in order, a short tool instruction, plan 49's framing text word for word, the skill (mode 1: all eight files; mode 2: SKILL.md only), the document, and the output path. The reader is told to read that file and treat it as its whole instruction. So that the file reads in one call, the document's line breaks inside paragraphs are joined; paragraph breaks and every word are as `fetch.py` wrote them.
6. **Mode 2's router is live through the Read tool**, not through `open_module`: the seven reference files sit in a folder the reader is given, and it opens them with Read. Which it opened is **self-reported** in the reader's structured return, not recorded by the rig.
7. **The reply is written by the reader to a file** with the Write tool, so that the raw return is the file the reader wrote; the reader also returns a small structured record (word count, modules opened, the path). The rig wraps the file into the same JSON shape as the DeepSeek runs, with `transport: "claude-code-workflow-agent"`.
8. **The reader could disobey the tool instruction** and read other files, including files in the repository that name the two breaks. The prompt files, the skill copies and the document texts are placed outside the repository, and the instruction is: Read only the prompt file and, in mode 2, the named references folder; Write only the output; no other tool, no other file. This cannot be enforced, and a contaminated reader cannot be told from a clean one by its report alone. Recorded as the main limit of this arm.

## What stays the same
Sources P3 and F4, the texts rebuilt by `fetch.py`; modes 1 and 2; three repeats each; file 30 then file 31; plan 49's framing text; the recurrence criteria of plan H56, word for word; the predictions of plan H56 (5 and 6) and plan H58 (1 to 5), unchanged; the marker; the claim-checking rule. Output folders: `runs_sonnet5/` and `runs_sonnet5_31/`, as the plans named them, with the transport in every record.

## What this gives up
A reader with nothing but the method and the document; a recorded module trace; finish reasons and usage; the reader's thinking. What it keeps is the thing the arm exists for: a second reader's reports on the same two papers under both skill versions, marked under the same frozen criteria. When an Anthropic key is supplied, `run_sonnet.py` runs the arm as the plans wrote it, into fresh folders, and the two transports are compared.

## Traps
- Reading a Sonnet 5 result here as the plans' Sonnet 5 result. It is the same reader through a different door, and the door is named in every record.
- Adding these runs to the DeepSeek counts. Plan H56 forbids it.
