# Saved workflows (Workflow project, plan W10)

Named workflow scripts, one per stage of plan W10 ("getting the LLM theory right"), saved on the owner's word (decision W6: "This workflow should be saved"). Run a stage with the Workflow tool by name. Copies are kept in `Workflow/rigs/W10 harness/workflows/`. Every agent is armed with the hard-to-vary skill (HV file 33); Opus 5 at xhigh for collecting, coding and reviewing; Sonnet 5 at high for running the harness and as a reader; at most five Claude subagents at a time; DeepSeek runs through the Python harness, five at a time, when a key is in the environment.

- `llm-theory-stage-a.js`: building and collecting (harness coder, corpus collector, fourth-clause collector, instrument writer, then the reviewer).
