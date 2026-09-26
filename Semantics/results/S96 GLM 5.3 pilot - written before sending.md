# S96: GLM 5.3 pilot, one call on part A - written before sending

*Written by one Claude agent (Opus 5.5, decision S22: one agent, kept economical) on 26 September 2026 from about 08:00 UTC, before the pilot call was sent, and committed with its caller, `tools/s96_glm_call.py`, before the launch. When it was written: the S96 cross-examination run (loop pid 8390) was still going, with Atria's part B on its second pass; this agent opened no S96 reply, receipt, reasoning or attempt file, and changed none of the shared tools (`s80_common.py`, `s80_call.py`, `s87_run.py`); no file of the tag `s96_xexam_glm_A` existed. The only calls sent to Z.ai before this note were five tiny tests of the endpoint, listed below, none carrying any S96 text. This file obeys decision S23 except where it quotes others.*

## Why

The owner asked "Should I use GLM 5.3 instead?". The quick research (`results/S96 note - GLM 5.3 as an outside reader, quick research.md`) recommended not instead of either reader, for now, but a pilot of GLM 5.3 beside Atria and Mimo on one part both have answered, at high effort. The owner then sent a Z.ai key. This is that pilot: one call, a third outside reader on a part already sent to both current readers.

## The call

- **Brief**: `tests/S96 Cross-examination - repaired copy - part A, Parts 0 to VIII, with the opening notes.md`, byte for byte as sent to Atria: md5 e47980f7d02a1b5822ec9b50f9c31fed, sha256 344ba172876b2852bd19726f9c0d82145689b16405b6fc59e6ec52f21b4dd6ad, 13,571 words, 83,818 bytes. The whole file is the one user message; no system text. The caller refuses to send unless the brief has that md5 and this note is committed and unchanged from HEAD (lesson S12).
- **Lines examined**: 1–372 of the repaired copy (the title and editorial note, Parts 0 to VIII), the same as Atria's part A. Mimo examined those lines in its parts 1 (lines 1–164) and 2 (165–320) and, for lines 321–372, in its part 3 (321–484). *Declared correction to the brief this agent was given*, which said the part covers the same lines as Mimo's parts 1 and 2: it covers those and lines 321–372, so the comparison below takes Mimo's parts 1 and 2 whole and Mimo's part 3 on lines 321–372 only.
- **Model and endpoint**: `glm-5.3`, at `https://api.z.ai/api/coding/paas/v4/chat/completions` (Z.ai's OpenAI-compatible URL for the GLM Coding Plan), key from the environment variable `GLM_API_KEY`, loaded only into the sending process.
- **Effort**: `thinking: {"type": "enabled"}` (GLM 5.3 cannot switch thinking off) and `reasoning_effort: "high"`. The owner's rule for cross-examination is medium (decision S17: "Use Atria and Mimo on medium thinking effort for cross examination"), and it names Atria and Mimo only; by lesson S16 a setting given for one role is set for that role only, as DeepSeek was sent at high. Z.ai's model page gives GLM 5.3 only low, high and max, and the research note suggested high; the owner sent the key after that suggestion. *Found in testing, and declared*: this endpoint also takes `"medium"` (answered HTTP 200), and refuses a made-up value with code 1210, "reasoning_effort must be one of: none, minimal, low, medium, high, xhigh, max". Whether GLM 5.3 acts on medium or maps it to another level is not known. This pilot goes at high, as recommended; GLM at medium would need the owner's word and its own test.
- **Other settings**: `max_tokens` 65,536 (the orchestrator's cap for this pilot; the API's range goes to 131,072; Atria's ceiling is also 65,536); temperature 0.7 (`s80_common.TEMPERATURE`, as every Atria and Mimo call); top_p unset; streamed, with usage asked for.
- **Attempts**: one pass, at most 6 attempts. Connection failures, timeouts (900 seconds of silence, or 7,200 seconds for one attempt), a stream cut before its finish, a finish of `network_error`, HTTP 429 and 5xx are sent again with the same request after a back-off of min(120, 10 × 2^n) seconds; 429 with code 1113 or 1309 (no balance, package expired) and other 4xx are final. An answer that comes back and fails the test below is sent again at the same `max_tokens`, at most 3 such answers, as in the S96 job list. No second pass is sent without a new note written before sending.
- **Counts as returned** only by the test of `s80_call.accept_reader`, restated in the caller: finish `stop` and END OF REPORT on the last non-blank line.
- **Tag and files**: `s96_xexam_glm_A`, in `results/S96 Cross-examination - repaired copy - returns/`: `.request.json` (no key), then either `.reasoning.txt`, `.receipt.json` and `.response.txt` last, or `.error.txt` and a receipt with `"accepted": false`; an answer that came back and failed the test leaves `.aN.truncated.txt` and `.aN.reasoning.txt`. The caller refuses to start if any file of the tag exists, and never writes over a file. The receipt holds the model, the effort, every attempt with its status, error class and times, the finish reason, usage (prompt, completion and reasoning tokens), the sha256 of the request and of the response, the start and end times, and whether the reply counts as returned. Every attempt holds one of three `glm` provider slots (`s80_common.provider_slot`).

**The job, in one line** (from the repository root; the keys file is loaded into the process only, never printed):

```
setsid nohup bash -c 'echo "launched $(date -u +%Y-%m-%dT%H:%M:%SZ)"; set -a; . <scratchpad>/cross_examiner_keys.env; set +a; <scratchpad>/venv/bin/python Semantics/tools/s96_glm_call.py --brief "Semantics/tests/S96 Cross-examination - repaired copy - part A, Parts 0 to VIII, with the opening notes.md" --brief-md5 e47980f7d02a1b5822ec9b50f9c31fed --rule "Semantics/results/S96 GLM 5.3 pilot - written before sending.md" --tag s96_xexam_glm_A --out "Semantics/results/S96 Cross-examination - repaired copy - returns"' > <scratchpad>/s96_glm_run.log 2>&1 < /dev/null &
```

`<scratchpad>` is `/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad`; the session leader's pid goes in `<scratchpad>/s96_glm_run.pid`. The call is over when that process has exited and the log's last line begins `done: ok` or `done: failed`, or when the returns folder holds `s96_xexam_glm_A.response.txt`, or `s96_xexam_glm_A.error.txt` with its receipt. A watcher outside the launching agent waits for that (lesson S14).

## The tests sent before this note

All to a scratchpad folder, with the seven-word brief "Reply with the words END OF REPORT.", through the caller unless said otherwise; their files stay in the scratchpad, and what they showed is here, so nothing committed depends on them (lesson S23).

1. General URL `https://api.z.ai/api/paas/v4/chat/completions`: HTTP 429, code 1113, "Insufficient balance or no resource package. Please recharge." after 1.4 seconds. The key is a GLM Coding Plan key, not a pay-as-you-go one.
2. Coding Plan URL, effort high, `max_tokens` 65,536: HTTP 200, finish `stop`, reply "END OF REPORT.", model returned `glm-5.3`, 3.9 seconds, usage 20 prompt and 115 completion tokens, 109 of them reasoning. The reply counted as returned.
3. A direct request, not through the caller, with effort `"medium"` and 64 tokens: HTTP 200, finish `length`.
4. A direct request with a made-up effort value: HTTP 400, code 1210, the list of values quoted above.
5. The caller again, with its default URL after the change to the Coding Plan URL: as test 2, 3.0 seconds. Its three refusals (a tag already present, an uncommitted rule file, a brief md5 that differs) were each tried and each sent nothing.

## For the owner: the plan's terms

Z.ai's usage policy for the Coding Plan (docs.z.ai, "Usage Policy") says the plan "may only be used within officially supported tools and products", that use in other tools "may result in restricted benefits", and that breaking its rules may bring "rate limiting, account freezing, or other restrictions". This pilot calls the plan's endpoint from the project's own script, not from a listed coding tool. It is sent because the owner sent this key for this pilot; whether to use the key this way again is the owner's choice. The per-token prices in the research note ($1.40 and $4.40 per million) are the pay-as-you-go prices and do not apply to this key; the plan's own quota applies instead.

## Declared addition to the S96 reading rule

The S96 rule (`results/S96 How the cross-examination of the repaired copy will be read - written before sending.md`) governs six calls. This pilot is a seventh call, added after that rule, and this note adds it:

1. **The single Claude reader waits for it too.** The reader (agent 15) opens no reply until the six calls have ended as that rule says and this call has ended, or until 24 hours after this call's launch (the time on the first line of `s96_glm_run.log`), whichever comes first for this call; the 36-hour limit of that rule still holds for the six. If the 24 hours pass first, the reading goes ahead without it, and a reply that comes later is read under these same rules and recorded as late.
2. **It is read under the same rule**, points 1 to 11: a set of arguments to rule on, not a result; challenges as that rule defines them; each ruled KEEP, FIX or DROP on its arguments, never by counting replies; bounded by the owner's words of S20 to S27; quotations compared with the text. Its points count like those of any reply, and each is marked as the pilot: rulings carry ids `glm A <n>`. A finding the reader takes up from GLM alone is ruled like any other and marked as coming from the pilot only.
3. **A comparison is recorded as well**, in the reader's file, in its own section:
   - which of GLM's findings Atria's part A or Mimo's parts 1 and 2 (or Mimo's part 3 on lines 321–372) also made;
   - which only GLM made, and how each of those was ruled;
   - which the others made and GLM did not;
   - whether GLM challenged anything at all, or reported nothing to repair (the S83 finding: DeepSeek matched the others' verdicts and chose to report no holes);
   - its verdict lines (Q1 to Q6 and OVERALL) beside Atria's part A and Mimo's;
   - time taken, attempts, connection failures and rejected answers, and tokens (prompt, completion, reasoning), from its receipt.
4. **A call that fails only on the connection is not an answer** (lessons S21 and S24): every attempt ending with no HTTP status, a cut stream, a `network_error` finish or a proxy refusal counts for nothing either way, and the call may go again only under a new note written before sending. A call that fails on answers GLM did give (length at 65,536, or no END OF REPORT, three times) is final for this pilot; that it did not finish at this cap is then itself the pilot's result, and its lines count as not examined by GLM. Its attempt files are kept and are not read for arguments.
5. **What the pilot can show**, proposed by Claude in the research note and not decided: whether GLM finishes inside its cap in under an hour, whether it names holes, and whether it finds at least one hole, taken up by the reader, that neither Atria nor Mimo found. One part is one sample; the pilot does not settle disconnect rates over many calls. Whether GLM is used again, and in whose place, is the owner's choice.

Decided by Claude under decisions S17, S22 and S24, on the owner's sending of the key. 26 September 2026.
