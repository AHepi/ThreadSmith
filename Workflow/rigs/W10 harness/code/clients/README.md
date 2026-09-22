# The two API clients (plan W10, stage A, task A6)

Two files, one per service, plus this read-me. Both are libraries: nothing is sent on import,
and the only command either runs is `--dry`, which sends nothing.

```
python3 deepseek_client.py --dry [--save DIR]
python3 atria_client.py    --dry [--save DIR]
```

`--dry` builds every request shape the plan needs, drives the retry loop, the thread rule and
the stream parser against a stand-in that reaches no network, prints one line per check, and
ends with `Nothing sent.` With `--save DIR` it also writes the exact request text of each
shape, which is what W10.1 asks to see ("the harness dry-runs every arm on one document
sending nothing, with the request text saved").

Today both dry runs pass: 37 checks for DeepSeek, 34 for Atria, 0 sent.

---

## What each client does

### `deepseek_client.py` - DeepSeek V4.1 Flash

- **Endpoint.** `https://api.deepseek.com/chat/completions`, and
  `https://api.deepseek.com/beta/chat/completions` when the last message is a prefix. The
  host is chosen from the messages, not from a flag, so a prefix cannot be sent to the host
  where the feature is off; an explicit base that is not the beta one raises before sending.
- **Prefix completion,** for arm (e), the port-setting arm. `prefix_message(text)` builds the
  `{"role": "assistant", "content": ..., "prefix": true}` last message the documentation
  requires, and takes an optional `reasoning_content` for the thinking-mode form.
- **Token ceiling.** `MAX_TOKENS = 393216`, the service's documented maximum (384K). That is
  this client's own default, as the task for A6 requires: no token limit below the service's
  maximum. A caller's explicit `max_tokens` is sent **as given** and never raised, because the
  record has to show what the caller sent (see *One thing for the reviewer* below).
- **Five worker threads at most.** `DeepSeekClient.many()` runs a list of jobs on at most five
  threads, the number W10 section 2 fixes. Asking for six raises, with the plan quoted, rather
  than being clamped quietly. `--dry` shows five jobs overlapping at five workers and not
  overlapping at one, so the number is visible and not merely asserted.
- **Retries.** Seven attempts, 4 s doubling to 90 s with jitter, `Retry-After` honoured when
  the service sends one (up to 300 s, deliberately above the backoff cap: a service that asks
  for five minutes means it). Retries on 408/409/425/429 and 5xx and on transport errors;
  never on 400/401/402/422, whose documented remedy is to change the request.
- **Both sides whole.** Every call returns one record: the body as sent, the exact request
  text (this client serialises the body itself and posts those bytes, so the saved text is the
  sent text), the endpoint, the headers with the key redacted, every attempt, the assembled
  message, the finish reason, the usage, and the raw return - the SSE lines as they came, or
  the whole JSON document. A failure carries the same record out on the exception
  (`err.record`), because a failed request is the one whose record is most needed.
- **The seam.** `send(body, key, tag=, stream_path=, tries=)` returns
  `(message, finish_reason, usage, http)`, which is exactly what A1's `deepseek_transport.py`
  imports and unpacks. With this file present that module reports
  `CLIENT = "clients.deepseek_client"`; without it, its own poster and
  `CLIENT = "deepseek_transport"`. That field is the gauge: no run can be read without knowing
  which client sent it.

### `atria_client.py` - Atria Asi (Atria Dawn Preview)

- **Endpoint.** `https://api.atria-asi.ai/v1/chat/completions`, overridable with
  `ATRIA_BASE_URL`. Model `Atria-Dawn-Preview` (the documentation says the id is
  case-sensitive), overridable with `ATRIA_MODEL`.
- **At most 30 requests a minute,** the owner's rule (Workflow decision W9), held by a pacer in the file: the start of every HTTP attempt, retries included, waits until two seconds have passed since the last one; the wait is recorded on the attempt (`paced_seconds`) and the cap on the record (`rpm_cap`). The same cap applies to the MiMo client.
- **One request at a time,** the owner's rule. A lock in this file is held for the whole
  exchange, the streamed read included, so a request counts as in flight until its reply is
  complete. The lock is here and not in the caller because a caller that forgets is the very
  failure the rule is against. There is no `many()`; the list method is `each()`, which runs
  jobs in sequence. `--dry` runs five threads at the client at once and shows one in flight,
  then runs the same five with the lock taken out and shows five - so the check can fail.
- **Token ceiling,** the owner's second rule. `MAX_TOKENS = 65536`, the service's documented
  maximum, is the default, and the ceiling is a parameter on the client, on `build_body` and
  on every call. **The gauge:** every record carries `truncated`, true when the finish reason
  is `length`. If the owner's failure was a cut-off reply, a ceiling at the maximum should
  drive that count to zero; if `truncated` is still true at 65,536, the ceiling was not the
  cause and the questions below are the live ones.
- **Retries.** Same shape as DeepSeek's, cap 120 s, `Retry-After` honoured; the documented
  rate-limit headers `x-rpm-limit` and `x-rpm-remaining` are kept in every record.
- **Nothing undocumented is sent.** No `reasoning_effort`, no `thinking` object: the service's
  own page names neither, and an undocumented parameter is a way to earn a 400 on every call.
  Pass `extra={"reasoning_effort": "max"}` once a live call has shown it is accepted, and
  record that it was.
- **Both sides whole,** and the same `send(...)` seam shape as the DeepSeek client, so a driver
  can hold either.

---

## What the environment must hold

| Variable | Needed by | Note |
|---|---|---|
| `DEEPSEEK_API_KEY` | `deepseek_client.py`, at call time only | Neither file writes it anywhere. |
| `ATRIA_API_KEY` | `atria_client.py`, at call time only | The documentation's own line is `export ATRIA_API_KEY=atr_xxx`. |
| `ATRIA_BASE_URL` | optional | Overrides `https://api.atria-asi.ai/v1`. |
| `ATRIA_MODEL` | optional | Overrides `Atria-Dawn-Preview`. |

Neither key is in this environment today, and neither client needs one to build a request or
to run `--dry`. The key is put in one place, the `Authorization` header of a live request, and
in no other: the record's headers read `Bearer <redacted>`, and `assert_no_key` is run over
every record before it is handed back or saved, so a key pasted into a prompt by mistake stops
the run instead of being written to disk.

Both keys were pasted into a chat, so both should be rotated now and deleted at the provider
when the round ends (W10's addendum, decision W7).

---

## What Atria Asi is, and what I could not find out

Everything in this section is **CLAIMED**: read on the web on 22 September 2026, quoted with
its address, and kept nowhere as a file. The full quotations are in the head of
`atria_client.py`.

Atria Asi serves **Atria Dawn Preview**, an agentic model (a 744B-parameter MoE foundation
model, from the Shanghai Artificial Intelligence Laboratory, per the model page), through an
OpenAI-compatible HTTP API at `https://api.atria-asi.ai/v1`. Its own integration page
(`https://api.atria-asi.ai/docs`) gives the base URL, the case-sensitive model id, Bearer
authentication with an `atr_`-prefixed key, three interfaces (`/v1/chat/completions`,
`/v1/messages` Anthropic-shaped with `x-api-key`, `/v1/responses`), a 256K context, text only,
SSE streaming, `max_tokens` accepting an integer from 1 to 65,536, `x-rpm-limit: 60` with
`x-rpm-remaining` and a `Retry-After` on 429, and three error classes (401, 429, 5xx). The
model's repository (`https://github.com/atria-asi/Atria-Dawn-Preview`) gives
`max_output_size = 65536`. So the service **was** found, and `ATRIA_BASE_URL` is an override
here rather than the required variable the task named for the case where it was not.

**Open questions for the owner.** None of these could be settled from the web; each is a thing
a first live call, or the owner's own memory of the failure, would settle.

1. **What did the failure look like?** The owner's rule is "it tends to fail otherwise". The
   client assumes the failure is a cut-off reply and gauges it with `truncated`. If it was a
   timeout, a 429, or a 5xx instead, the ceiling is the wrong fix and the retry schedule or
   the read timeout is the thing to move.
2. **What is `max_tokens` when it is omitted?** The page does not say. If the default is
   small, that alone would explain the failure; if it is already 65,536, the ceiling is idle.
3. **Does the HTTP API take `reasoning_effort` or a `thinking` object, and with which values?**
   The repository's client config lists `["low", "medium", "high", "xhigh", "max"]` with
   default `max`, but that is a client's config, not the API's parameter list. Nothing is sent
   today.
4. **Does the reply carry a reasoning field, and under what name?** The client collects
   `reasoning_content` or `reasoning` if either appears and keeps the raw return either way,
   so nothing is lost - but the field is a guess.
5. **Are tool calls accepted on `/v1/chat/completions`?** A gateway listing says the model
   supports tools; the service's own page does not list the parameter. This matters if an
   Atria examiner is ever to open a skill module the way DeepSeek mode 2 does.
6. **Is there a concurrency limit, separate from 60 requests a minute?** The owner's rule is
   one at a time; the page gives only the per-minute cap, and does not say the cap is the same
   for every account.
7. **Is there any way to prefill the assistant turn** (DeepSeek's prefix completion)? Nothing
   on the page suggests one. If Atria were ever wanted for arm (e), this is the blocker.
8. **What does it cost?** The only price seen was a gateway's `$0/M`, which is that gateway's
   listing and not the provider's price.

---

## How these two files sit in the rig

There is no `__init__.py` here on purpose. `clients` is an implicit namespace package, which
is what A1's `from clients.deepseek_client import send` needs, and it is the safer of the two:
with an `__init__.py`, a `clients/` folder earlier on `sys.path` would hide this one, whereas
a namespace package merges. This was checked by importing A1's `deepseek_transport` from an
unrelated working directory and reading back `CLIENT = "clients.deepseek_client"`.

No driver holds the Atria client yet. Stage E is where it is wanted (W10's addendum: "stage
E's cross-examination may use Atria beside the five DeepSeek examiners for the analysis the
owner names, one at a time"). Its `send(...)` has the same four-value shape as the DeepSeek
seam, so a driver written for one can hold the other.

## One thing for the reviewer (A5)

A1's `deepseek_transport.py` sets `MAX_TOKENS = 32000` and passes it in every body, with the
comment that a report under 1,200 words needs far less. The task for A6 says the client is to
have "no token limit below the service's maximum", and this client's own default is 393216.
The two do not agree, and this client does **not** settle it by rewriting a caller's value:
silently raising a number the driver has already written into its saved `.request.json` would
make the record describe a request that was not sent, which is the one thing PA.1 rests on. So
the number in a live run will be A1's 32000 unless A1 or the reviewer changes it. Whoever
decides should note that arm (e) prefills the emission and the port-setting reports are the
long ones.

## How to count requests (PA.1)

W8's PA.1 counts "the number of requests and the text of each request as sent", and predicts
exactly one request per step in arms (b), (c), (c') and (d). **A retry is a second attempt at
the same request, not a second request.** Both clients keep the two apart: one record per
request, every transport attempt listed inside it under `attempts`. Count records for PA.1;
read `attempts` to see how the service behaved.

## What is not settled here, and not by anything on the web

Whether the beta prefix endpoint accepts thinking mode on `deepseek-flash`. No page found says.
Neither client drops thinking to make a request succeed: a run made under a different thinking
setting is a different arm, so the service's own words come back instead, whole, and the
driver stops the run.
