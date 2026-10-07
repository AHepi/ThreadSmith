# S104 note - four GLM calls at once, tested before round 3

Written 28 September 2026 by one Claude agent (Opus 5.5), on decisions S38 ("After this run, remove Mimo from workflow") and S39 ("use multiple GLM agents to do slightly different job. I think you can run 4 agents"). Round 2's runs had ended (GLM 17 of 17, Mimo 17 of 17). No file of round 2's reading was read or written.

## In short

- **Four GLM calls at once work on this key.** Two tests were run, each with four calls started within 6 thousandths of a second of one another. All eight calls came back whole, on the first try, with no refusal and no rate-limit message.
- In the second test each call ran about 16 seconds, so all four were certainly running on Z.ai's side at the same moment, for at least 15 seconds.
- Because four worked, three and two did not need to be tried.
- **The code now allows four GLM calls at once** (`tools/s80_common.py`, `"glm": 4`). Mimo's setting was left at 1 on purpose (reason below). Mimo is kept out by not sending to it.
- Z.ai publishes **no fixed number** for how many calls may run at once. It says the limit depends on the plan tier and **changes with demand**, and is higher off-peak. So four working now does not promise four at a busy hour.
- One thing to know before round 3: the round-2 GLM runner (`tools/s104_glm_loop.py`) sends its parts **one after another**. The new limit allows four at once, but something must actually start four at once: four runners, or a new runner that does.

## 1. What was tested and how

**The route was the same as the real calls.** Each test call went through the unmodified helper `tools/glm_via_claude_code.py`:

- model glm-5.3, through the Claude Code CLI 2.1.283 (`/opt/node22/bin/claude -p`);
- `ANTHROPIC_BASE_URL` https://api.z.ai/api/anthropic;
- `--effort medium` (decision S17);
- the helper's usual home in the scratchpad, `glm_claude_code_home`. Its `config/` folder is the `CLAUDE_CONFIG_DIR`, never `~/.claude`.

All four calls of a test shared that one home, as round 3's calls will.

**How the helper handles the key and the config (from the code).**

- The key is read from the environment variable `GLM_API_KEY`. It goes only into `ANTHROPIC_AUTH_TOKEN` of a fresh environment built for the child process. It never goes into a file, an argument or a log, and a guard replaces it in anything written.
- `HOME` is the `--home` folder, and `CLAUDE_CONFIG_DIR` is `<home>/config`. The helper refuses a home inside the repository, or one that holds or sits inside `~/.claude`.

**What the helper demands, and how the test met it.**

- `--rule` (a committed, unchanged reading rule) and `--brief-md5` are both **optional**. A call without them simply skips those checks.
- So a tiny call needs only a brief file, a tag and an output folder. For this test those were in the scratchpad, with `--attempts 1 --max-rejects 1 --deadline 600`. That meant one try per call, no retries to hide a refusal, and each call stopped at 600 s at most.
- The helper accepts a reply only if its last line carries END OF REPORT. Each brief therefore asked GLM to end with "READY <n> END OF REPORT".

**How the old limit of 1 was kept from queuing the test calls.**

- Until this change, the helper's slot lock (`s80_common.provider_slot`) let only one GLM call run at a time. Four calls through it would have queued one behind another.
- So each test call was given its own `SEMANTICS_RUN_DIR` under the test folder, which gave each call its own lock folder. The helper itself was not changed.
- Meanwhile, a small holder process took the **real** GLM slot, in the shared lock folder, for the whole test. It sent nothing. This meant no real GLM call from another agent could run alongside the test.
- Before the test, every provider slot was free, and no GLM or Mimo process was running.

**How the key was handled.** A runner script in the scratchpad loaded the key file with `set -a; . <file>; set +a` and unset the other keys (ATRIA, MIMO, OPENAI). It then started the four helpers in the background. The key was never printed or placed on a command line. After each test, a check run from inside Python confirmed that no file in the test folder holds the key. The helper also counts zero replacements in every receipt.

**The two tests.**

- **Test 1 ("wave4"):** each brief asked for one line only, "READY n END OF REPORT".
- **Test 2 ("wave4long"):** each brief asked for the numbers one to four hundred written in words, one per line, then that last line. About 2,100 output tokens each, so each call streams for about 16 s and the calls surely overlap.

All test files are in the scratchpad, not the repository: `.../scratchpad/glm_concurrency_test/`. The folder holds the briefs, `run_wave.sh`, `hold_real_glm_slot.py`, and, for each test, the console output, each call's times and progress lines, and the helper's request, receipt and response files.

## 2. What Z.ai's documents say

- **Usage policy**, https://docs.z.ai/devpack/usage-policy: "Rate (concurrency) limits are tied to your plan tier. The platform dynamically adjusts these limits based on resource availability, with the general principle being Max > Pro > Lite."
  - The same page recommends one project at a time on Lite, one or two on Pro, and two or more on Max. It adds that "you can use methods like Subagent to make concurrent model calls".
  - It also says: "Plan users will enjoy higher concurrency limits during off-peak hours (dynamically increased)".
  - And: the plan "may only be used within officially supported tools and products".
- **The Claude Code page**, https://docs.z.ai/devpack/tool/claude: setup only. It says nothing about concurrency or limits.
- **FAQ**, https://docs.z.ai/devpack/faq: a 5-hour usage quota and a weekly quota (on a 7-day cycle from the order date), and "Users subscribed to the Coding Plan can only make calls via the plan's quota in supported tools." It gives no number of calls at once.
- **Error codes**, https://docs.z.ai/api-reference/api-code: these come with HTTP 429.
  - 1302 "Rate limit reached for requests";
  - 1305 "temporarily overloaded";
  - 1308 "Usage limit reached ... Your limit will reset at ...";
  - 1310 weekly or monthly limit used up;
  - 1113 no balance, and 1309 package expired (the helper treats these two as final).
- Z.ai states **no fixed concurrency number** for the Coding Plan. Outside write-ups say the same, for example https://zentor.ai/blog/glm-coding-plan-rate-limits. Those are not Z.ai's word.
- **This key's tier (Lite, Pro or Max) is not recorded in the project**, so which recommendation applies is not known.

## 3. The result, call by call

Times are UTC on 28 September 2026. "Start" and "end" are the wrapper's clock, around the whole helper process. "API" is the time the CLI itself reports it spent waiting on Z.ai (`duration_api_ms`). All eight calls:

- exited with code 0;
- were accepted on attempt 1, with result `success` and no `api_error_status`;
- reported model `glm-5.3`;
- the helper wrote nothing to stderr;
- showed no tools and no MCP servers at startup, as the helper requires;
- had the key replaced 0 times.

**Test 1: one short line each.**

| Call | Start | End | Helper attempt | API | Reply | Tokens in / out |
|---|---|---|---|---|---|---|
| 1 | 01:36:07.313 | 01:36:10.368 | 2.7 s | 2.02 s | READY 1 END OF REPORT | 73 / 8 |
| 2 | 01:36:07.315 | 01:36:10.365 | 2.7 s | 1.92 s | READY 2 END OF REPORT | 73 / 8 |
| 3 | 01:36:07.316 | 01:36:10.370 | 2.7 s | 1.94 s | READY 3 END OF REPORT | 73 / 8 |
| 4 | 01:36:07.319 | 01:36:10.273 | 2.6 s | 1.90 s | READY 4 END OF REPORT | 73 / 8 |

The calls here are too short to prove on arithmetic alone that all four were in flight at one instant, though they almost surely were. Test 2 settles it.

**Test 2: about 2,100 tokens each.**

| Call | Start | End | Helper attempt | API | Reply | Tokens out |
|---|---|---|---|---|---|---|
| 1 | 01:36:48.973 | 01:37:05.775 | 16.6 s | 16.29 s | 400 lines, "one" to "four hundred", then READY 1 END OF REPORT | 2,106 |
| 2 | 01:36:48.975 | 01:37:05.520 | 16.4 s | 16.02 s | the same, READY 2 END OF REPORT | 2,097 |
| 3 | 01:36:48.977 | 01:37:05.622 | 16.5 s | 16.11 s | the same, READY 3 END OF REPORT | 2,092 |
| 4 | 01:36:48.979 | 01:37:05.339 | 16.2 s | 15.78 s | the same, READY 4 END OF REPORT | 2,101 |

**Why this proves all four were running at once.** Each call's API time lies inside its own start-to-end window. So:

- The latest any of the four could have begun talking to Z.ai is 01:36:49.56 (call 4: end minus API time).
- The earliest any could have finished is 01:37:04.76 (call 4: start plus API time).
- So **all four were streaming from Z.ai at the same time for at least 15 seconds.** No refusal, no slowdown message, and no retry came in that time.

GLM also returned a few dozen characters of thinking per call in test 2; it reported 0 thinking tokens.

## 4. The largest number that worked

**Four**, the most decision S39 asks for. Every call at four came back, so three and two were not tried. More than four was not tried.

## 5. What changed in `tools/s80_common.py`

- `SLOTS_BY_PROVIDER` changed from `{"mimo": 1, "glm": 1}` to `{"mimo": 1, "glm": 4}`.
  - Every GLM call through `glm_via_claude_code.py`, or the older `s96_glm_call.py`, takes one of four slots now, `glm.slot0` to `glm.slot3` in the shared lock folder.
  - Checked without sending anything, in a separate lock folder: five threads asking for a GLM slot got slots 0, 1, 2 and 3 at once, and the fifth waited until one was free.
- **Mimo was left at 1, not 0 and not removed.** `slots_for` feeds `provider_slot`, which loops over `range(limit)` and waits until a slot is free:
  - with 0 there is never a slot, so a Mimo call would wait for ever without an error;
  - with "mimo" removed, Mimo would fall back to the default of 3 (`SLOTS_PER_PROVIDER`), which is more than before.
  - Neither is safe, so decision S38 is kept by not sending to Mimo. A comment in the file says this.
- The comments stating GLM's limit were brought up to date: decision S39 and four slots, with a pointer to this note.
- **No pinned file is affected.**
  - The file's md5 before the change, `01946dd4ae06efc2e2b01f2676b34520`, and its SHA-256 appear in no file under `Semantics/`.
  - Round 2's reading rule does not name `s80_common.py`.
  - Round 2's job lists pin only the briefs' md5s.
  - Round 2's sending is over in any case.
  - The md5 after the change is `0e06025e87d66fce6d17e32323bfe0fc`.
- No GLM or Mimo call was running when the change was made.
- **Not changed (outside this task):** the docstring of `tools/glm_via_claude_code.py` still says "one GLM call at a time from 27 September 2026, decision S35". It is a comment only: the helper reads the limit from `s80_common`. `tools/s104_glm_loop.py` still sends one part after another.

## 6. What was not tested

- **Long calls at once.** Real round-3 calls may run for many minutes with large briefs and long thinking. Only 3-second and 16-second calls were tested.
- **Sustained use.** Only two bursts of four were tried, about 40 seconds apart. Many hours of four at once were not tried, and neither was the effect on the 5-hour and weekly quotas. Four long calls at once will use those quotas about four times as fast.
- **Busy hours.** Z.ai lowers or raises the limit with demand. The test ran at 01:36 UTC (09:36 in Beijing), not at a busy hour Z.ai names (it names none on the pages read). Four may be refused at another time; the helper would then see HTTP 429 (for example code 1302), wait and retry, up to six attempts.
- **More than four**, and the plan tier of this key.
- **Four real runners at once through the shared lock folder.** The slot code was checked on its own. The test calls used separate lock folders, so the old limit of 1 would not queue them.
