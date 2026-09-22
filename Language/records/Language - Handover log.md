# Language - Handover log

Kept for a fresh context after an auto-compaction: what is running, where things are, what comes next. Updated at every step; the log (project story) stays the record. Newest entry first.

## 22 September 2026, evening - the API agents and Arm B
- **Owner's instructions this stretch** (decision L11, verbatim in Decisions): use two API models for the outside-agent roles, Atria (30 requests per minute) and Mimo (100 per minute); think as high as possible, skills as needed; work autonomously until tokens run out; at most 5 Opus subagents at a time, never Fable subagents; keep goals calibrated to file 11 (Semantics revision 1) and to the goal, reasoning with prose; keep asking when a vaguely incorrect translation is acceptable; the owner reviews at the end; push often, "work lost is more costly than a cluttered repo"; keep this handover log.
- **Agents rule** (owner, later in the same stretch): Opus 5 at extra effort for complex analysis; Sonnet 5 for testing language candidates; at most 5 Opus at a time; never Fable.
- **Keys**: NOT in the repository. They sit in the scratchpad at `scratchpad/keys/api.env` (variables ATRIA_API_KEY, MIMO_API_KEY). If the scratchpad is gone, the owner has them.
- **Atria**: works. OpenAI-shaped. `POST https://api.atria-asi.ai/v1/chat/completions`, header `Authorization: Bearer $ATRIA_API_KEY`, model `Atria-Dawn-Preview`; returns `reasoning_content` beside `content`. 30 RPM.
- **Mimo**: works at the Singapore token-plan endpoint only: `POST https://token-plan-sgp.xiaomimimo.com/v1/chat/completions`, Bearer, model `mimo-v2.6-pro`; the China and Amsterdam endpoints reject the key. 100 RPM. Returns `reasoning_content`.
- **The caller**: `Language/tools/ask_model.py PROVIDER --system F --user F --out DIR --tag T`; keys from the environment (`. scratchpad/keys/api.env; export ATRIA_API_KEY MIMO_API_KEY`); writes response, reasoning, request and a receipt with the provider's response id per call; rate-limited per provider; retries.
- **State of the project**: Arm A done (L79 results, eight of eight on two markings; new versions run_check_2.py, consequences_2.py, sameness_2.py, L80 built beside the old). Next is Arm B: ten new short texts nobody in the loop wrote, two translators (Atria, Mimo), old and new rig, a reader on shuffled reports, a plan with quoted premises and a mock suite covering every fixed string (Lesson L12), frozen by a second agent (Opus), marked twice.
- **Before Arm B**: a calibration note against file 11 and the "reasoning with prose" goal, and the rule for when a vaguely incorrect translation is acceptable (L64 section 6 has the layer table; make the rule explicit for Arm B's marking).
- **Where things are**: plan L79 and its checks in tests/; outputs in results/"L79 Arm A outputs"; the API caller script, once written, in Language/tools/ (reads keys from the env, never from a file in the repo).

## Traps
- Committing a key. `git diff --cached | grep -i "atr_\|tp-"` before every commit.
- Letting this file replace the log. It is a pointer; the entries in the project story are the record.
