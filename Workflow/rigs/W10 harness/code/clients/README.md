# The API clients (plan W10, stage A, task A6; the third added by addendum W12)

Three files, one per service, plus this read-me. All are libraries: nothing is sent on import,
and the only command any of them runs is `--dry`, which sends nothing.

```
python3 deepseek_client.py --dry [--save DIR]
python3 atria_client.py    --dry [--save DIR]
python3 mimo_client.py     --dry [--save DIR]
```

`--dry` builds every request shape the plan needs, drives the retry loop, the thread rule and
the stream parser against a stand-in that reaches no network, prints one line per check, and
ends with `Nothing sent.` With `--save DIR` it also writes the exact request text of each
shape, which is what W10.1 asks to see ("the harness dry-runs every arm on one document
sending nothing, with the request text saved"), and what W10.11 asks of the MiMo client.

Today all three dry runs pass, as measured on 22 September 2026: 37 checks for DeepSeek,
35 for Atria, 71 for MiMo, 0 sent.

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

### `mimo_client.py` - MiMo-V2.6-Pro (addendum W12, the third examiner family in stage E)

- **Endpoint.** `https://token-plan-cn.xiaomimimo.com/v1/chat/completions` by default,
  because the owner's key begins `tp-` and the provider's own pages make `tp-` a **Token
  Plan** key, which has its own hosts. `MIMO_BASE_URL` overrides the base outright;
  `MIMO_REGION` picks among the three documented Token Plan clusters, `cn` (the default),
  `sgp` and `ams`. Model `mimo-v2.6-pro` - the id is lower case, the page's display name
  `MiMo-V2.6-Pro` is not it - overridable with `MIMO_MODEL`, and a `MIMO_MODEL` the
  documentation does not list makes the dry run say so instead of earning a 400.
- **The key and the base must match.** The quick-access page says the two kinds of key are
  "distinct" and "cannot be used interchangeably", so a `tp-` key on the pay-as-you-go base
  (or an `sk-` key on a Token Plan base) **raises before anything is sent**, naming the
  remedy. `check_mix=False` sends anyway, which is how the owner would find out that the
  documentation is wrong; the record then says `key token-plan -> base pay-as-you-go
  (mixed, sent anyway)`.
- **Both documented authentication headers are sent.** The provider's curl uses
  `api-key: $MIMO_API_KEY`; its integration FAQ also gives `Authorization: Bearer`; a
  third-party issue report says the Token Plan host *refuses* `api-key` and wants Bearer.
  The sources disagree, so one request carries both and the first live call does not have to
  guess. `MIMO_AUTH_STYLE=api-key` or `=bearer` sends one alone, which is how the live check
  settles which the host reads; a 401 from a single-style call says in its message that the
  other style is untried.
- **Token ceiling.** `MAX_TOKENS = 131072`, the documented maximum (128K), under the name
  this service documents, `max_completion_tokens`. W12 section 3 fixes the default there
  ("token spend not limited below the documented maximum"), and the ceiling is a parameter
  on `build_body`, on the client and on every call. `build_body(max_tokens=...)` is accepted
  as an alias so a driver written for the other two clients needs no edit; what goes on the
  wire is always the documented name. A caller's explicit ceiling is sent **as given** and
  never raised, for the reason under *One thing for the reviewer* below.
- **Five worker threads at most,** the number W12 section 3 carries over from DeepSeek.
  Asking for six raises with the plan quoted. `--dry` shows five jobs overlapping at five
  workers and not overlapping at one, so the number is visible and not merely asserted.
- **Thirty requests a minute,** the owner's later rule (decision W9), held by the same pacer
  as in `atria_client.py` and under the same names: two seconds between the starts of two
  HTTP attempts, retries included, across every thread, recorded as `paced_seconds` on each
  attempt and `rpm_cap` on the record. It spaces the starts and does not serialise the
  exchanges, so five examiners can still be in flight at once. It binds far below the
  documented RPM 100, so the owner's number is the one that decides.
- **Retries.** Seven attempts, 4 s doubling to 90 s with jitter, `Retry-After` honoured up to
  300 s. Retries on 408/409/425/429 and 5xx and on transport errors; never on
  400/401/402/403/404/421. **402 is in that list on purpose:** the price page says an
  exhausted Token Plan quota "will suspend the service", and asking again cannot undo that -
  the error message says so rather than spending seven attempts.
- **Nothing undocumented is sent.** No `reasoning_effort` (that is DeepSeek's parameter), no
  `stream_options` unless `include_usage=True` is asked for, and **no `temperature` or
  `top_p`**: thinking mode is documented to override both, so a record carrying a temperature
  would describe a request that did not run. `thinking` *is* sent, explicitly, although
  `enabled` is the documented default, so the record says what ran rather than resting on a
  default that can change under a run. A `tool_choice` other than `auto` and a
  `response_format` other than `text` raise, because the page says the backend drops the
  first and documents only the second.
- **Four gauges in every record.** `truncated` (finish reason `length`: the ceiling was
  reached); `repetition_truncated` (finish reason `repetition_truncation`, which this service
  documents and the other two do not, so a report cut for repeating is not read as a short
  answer); `usage_missing` (a streamed reply that carried no usage at all, which is what
  would show that `stream_options` is needed here and undocumented); `thinking_seen`
  (`reasoning_content` came back, or `reasoning_tokens > 0`).
- **Both sides whole,** and the same four-value `send(body, key, tag=, stream_path=, tries=)`
  seam as the other two - checked by reading the three signatures back side by side - so a
  driver written for one holds this one.
- **`stage_e_shapes()`** builds the ten request shapes stage E needs (examiner, blind
  re-mark, structured reply, tools, the second thinking turn that keeps `reasoning_content`,
  non-streamed, usage, thinking off, a small ceiling, and the untested assistant-prefill),
  and `--dry --save DIR` writes each one's exact request text. That function, not a comment,
  is what W10.11 is to be read against.

---

## What the environment must hold

| Variable | Needed by | Note |
|---|---|---|
| `DEEPSEEK_API_KEY` | `deepseek_client.py`, at call time only | Neither file writes it anywhere. |
| `ATRIA_API_KEY` | `atria_client.py`, at call time only | The documentation's own line is `export ATRIA_API_KEY=atr_xxx`. |
| `ATRIA_BASE_URL` | optional | Overrides `https://api.atria-asi.ai/v1`. |
| `ATRIA_MODEL` | optional | Overrides `Atria-Dawn-Preview`. |
| `MIMO_API_KEY` | `mimo_client.py`, at call time only | The provider's own Python sample reads this very name. The owner's key begins `tp-`, which the provider makes a Token Plan (Individual) key. |
| `MIMO_BASE_URL` | optional | Overrides `https://token-plan-cn.xiaomimimo.com/v1`. |
| `MIMO_MODEL` | optional | Overrides `mimo-v2.6-pro`. |
| `MIMO_REGION` | optional | `cn` (default), `sgp` or `ams`: picks among the three documented Token Plan hosts. Ignored when `MIMO_BASE_URL` is set. |
| `MIMO_AUTH_STYLE` | optional | `both` (default), `api-key` or `bearer`. See the header question below. |

None of the three keys is in this environment today, and no client needs one to build a
request or to run `--dry` - which is W12's own rule, "No key is in the environment while it
builds", and is why `--dry` reports a **failure** if one is present. The key is put in one
place, the authentication header of a live request, and in no other: the record's headers read
`<redacted>`, and `assert_no_key` is run over every record before it is handed back or saved,
so a key pasted into a prompt by mistake stops the run instead of being written to disk.

All the keys were pasted into a chat, so all should be rotated now and deleted at the provider
when the round ends (W10's addendum, decision W7; the same goes for the MiMo key under W12).

**One gap the reviewer should close, outside this folder.** `rig.py` sets
`KEY_ENV = ["DEEPSEEK_API_KEY", "ATRIA_API_KEY"]`, and `rig.write_json` refuses to write only
what it finds in those. A MiMo key would pass that check. `mimo_client.py` runs its own
`assert_no_key` over every record it hands back or saves, so nothing this client produces can
carry the key; but anything written through `rig.write_json` is unguarded against it until
`"MIMO_API_KEY"` is added to that list. The task for this addendum allowed writing only in
`clients/`, so the line is named here rather than changed.

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

## What MiMo 2.6 Pro is, and what I could not find out

Everything in this section is **CLAIMED**: read on the web on 22 September 2026, quoted with
its address, and kept nowhere as a file. The full quotations, with every address, are in the
head of `mimo_client.py`.

**MiMo 2.6 Pro** is `mimo-v2.6-pro`, Xiaomi's flagship text model, served from the Xiaomi
MiMo API Open Platform (`mimo.mi.com/docs`, the same pages under `platform.xiaomimimo.com`,
which redirects there) through an **OpenAI-compatible** chat endpoint, `/v1/chat/completions`,
and an Anthropic-compatible one, `/anthropic/v1/messages`. The model page gives a **1M-token
context** and a **128K maximum output**, and prices the pay-as-you-go card at **$0.435 per
million input tokens (cache miss), $0.0036 (cache hit) and $0.87 output**. The API page gives
`max_completion_tokens` a range of **1 to 131072**, roles **developer / system / user /
assistant / tool**, `tools` with `tool_choice` **`auto` only** ("When a value other than `auto`
is passed to `tool_choice`, the backend will remove this field by default"), `response_format`
type **`text`**, a `thinking` object whose **default is `enabled`** for this model, a reply
carrying `reasoning_content` beside `content`, finish reasons
`stop|length|tool_calls|content_filter|repetition_truncation`, and usage with
`prompt_tokens_details.cached_tokens` and `completion_tokens_details.reasoning_tokens`. The
rate-limit page gives **RPM 100 and TPM 10M** for this model and says only that "the platform
sets a model concurrency limit for each account", without a number. So **tool calling and a
system message are documented and supported; a prefilled assistant message is not documented
anywhere I found, which makes it unknown, not absent.**

The owner's key prefix decided the base URL. The provider's pages say pay-as-you-go keys are
`sk-`, Token Plan (Individual) keys are **`tp-`** and Token Plan (Team) keys `ttp-`, that the
two kinds "cannot be used interchangeably", and that Token Plan has **its own hosts**:
`token-plan-cn`, `token-plan-sgp`, `token-plan-ams`. A `tp-` key therefore does **not** belong
on `api.xiaomimimo.com`, and the client refuses that pair before sending. The price page says
every Token Plan tier covers `mimo-v2.6-pro`, so the plan reaches the model W12 names, and
that spend is against monthly **Credits**, not the dollar card above - so `cost()` in the
client is what the same traffic *would* have cost on pay-as-you-go, a comparison with the
DeepSeek round and not a bill.

**Open questions for the owner.** None could be settled from the web. Each names what would
settle it.

1. **Which region is the subscription - `cn`, `sgp` or `ams`?** Nothing in a key's text says.
   The default here is `cn`, the cluster the documentation lists first; if the plan was bought
   elsewhere, set `MIMO_BASE_URL` (or `MIMO_REGION`). What a wrong-region base returns is also
   unknown: 401 and 404 are both plausible, and the first live call will show which.
2. **Which authentication header does the Token Plan host read?** The provider's curl uses
   `api-key`; its FAQ offers `Authorization: Bearer` as well, but says so about the
   pay-as-you-go call; an openclaw issue of 5 May 2026 reports `api-key` -> **401** and
   `Bearer` -> **200** on `token-plan-cn` (for TTS, by a third party, with no maintainer
   reply). The client sends both, so the live check should pass either way; running it once
   with `MIMO_AUTH_STYLE=api-key` and once with `=bearer` is what would settle it.
3. **Do Token Plan keys share the pay-as-you-go RPM 100 / TPM 10M, or have their own?** The
   rate-limit page does not say, and the Token Plan pages give no numbers at all. The owner's
   30 a minute (decision W9) is below anything published, so this matters only if the plan's
   real limit is lower still.
4. **What is the account's concurrency limit?** The page says one exists and gives no number.
   Five is W12's number, not the service's.
5. **Which status code does an exhausted plan quota return?** The price page says the service
   is suspended; the error table has 402 "Insufficient account balance", which is about
   balance, not about a plan. The client does not retry 402 either way.
6. **What is `max_completion_tokens` when it is omitted?** "Default varies by model", and the
   number for this model is not given (the Anthropic page gives 32768 for `mimo-v2.5` only).
   The client sends the documented maximum, so this matters only to a caller who omits it.
7. **Is the legacy name `max_tokens` accepted on the OpenAI endpoint?** No page found says.
   `build_body(max_tokens=...)` maps it to `max_completion_tokens`; a body that arrives with
   a raw `max_tokens` is sent as given and said out loud on stderr.
8. **Is `stream_options: {"include_usage": true}` accepted?** Not documented here. Until a
   live call shows it is, a streamed reply may carry no usage at all - which is what the
   `usage_missing` gauge counts. Pass `include_usage=True` to try it; use `stream=False` if
   usage must be certain.
9. **Does the endpoint continue a prefilled assistant message?** Nothing found says either
   way. `prefill_message()` adds no invented flag, and every record whose last message is an
   assistant message carries `prefill_untested: True`. Stage E does not need it - arm (e) is
   DeepSeek's - so this is only for a later addendum.
10. **The model page lists "Structured Output" as a capability; the API page documents
    `response_format` type `text` only.** Two of the provider's own pages disagree. The client
    sends nothing but `text`, and a stage E reply that must be structured is asked for in
    words. `extra={"response_format": {"type": "json_object"}}` is the way to test the other
    reading once, and to record that it was tested.

## The one live check, before stage E

W12 section 3 allows "One live request of a few tokens, sent by Claude with the key in the
command's environment only". That is one request and no more, and it is the only thing in this
round that reaches the service. With the key in the command's environment (not in a file, not
in the shell's history if the shell supports a leading space):

```
cd "rigs/W10 harness/code/clients"          # so that `import mimo_client` finds this file
MIMO_API_KEY=tp-... python3 - <<'PY'
import json, os
from mimo_client import build_body, call
body = build_body([{"role": "system", "content": "Answer in five words."},
                   {"role": "user", "content": "Name the mark of a good explanation."}],
                  max_tokens=512, stream=False)
rec = call(body, os.environ["MIMO_API_KEY"], tag="live")
print(json.dumps({k: rec[k] for k in ("url", "auth_style", "http_status", "finish_reason",
                                      "usage", "truncated", "usage_missing",
                                      "thinking_seen", "rate_headers")}, indent=1))
print("model id returned:", (rec["raw"] or {}).get("model"))
print(rec["message"]["content"])
PY
```

`call` rather than `send` here, because W10.11 asks for the **model id in the reply** and only
the whole record carries it. The ceiling is 512 and not 64 on purpose: thinking mode is on by
default and its tokens come out of the same budget, so a 64-token ceiling can return an empty
`content` with finish reason `length` - which would look like a broken client and is only a
ceiling too small to think in. `send(...)` is the seam a stage E driver uses; it is exercised
in `--dry` and needs no separate live call.

What it settles, and what each answer means:

- **A 200 whose `model` reads `mimo-v2.6-pro`** satisfies W10.11's second half ("one live
  request returns a reply with the model id named in the documentation"). A 200 whose `model`
  reads something else - a gateway's id, an older version - is a finding, not a pass, and the
  results file should carry the string that came back.
- **A 401** means the base URL, the region or the header is wrong. Try
  `MIMO_AUTH_STYLE=api-key` and `=bearer` in turn, then `MIMO_REGION=sgp` and `=ams`. Every
  such attempt is its own request: say how many were spent.
- **A raised `MiMoError` before anything is sent** means the key and the base do not match -
  set `MIMO_BASE_URL` to a Token Plan host.
- **A 402 or a suspension message** means the plan's quota is gone, and no retry will help.
- **`thinking_seen` false** on a 200 means the documented default `enabled` did not run, and
  every stage E prompt should then send `thinking=True` and be re-read.
- **`usage_missing` true** on a streamed call (this check is non-streamed, so it should be
  false) is question 8 answering itself.

Whatever comes back, the run is one request. If MiMo cannot be reached at all, W10.11 is
falsified and "MiMo does not run in stage E and the results file says so" (W12 section 4).

---


### The live check of the MiMo client (22 September 2026, by Claude, key in the command environment only)
SEEN. Two requests, records kept key-free under `stage-A returns/A7 live check/`. (1) "Reply with the single word: ok", `max_completion_tokens` 512, not streamed, auth style `both`: token-plan-**cn** returned HTTP 401 ("both documented headers were sent"); token-plan-**sgp** returned HTTP 200, finish `stop`, content "ok", `reasoning_content` present, usage 14 prompt / 17 completion (14 reasoning). ams not tried. (2) A second request to sgp to read the reply's model field: `"model": "mimo-v2.6-pro"`, the documented id; finish `stop`; no rate-limit headers in the response (`server: MiFE/3.4.29` and `x-mife-upstream-status` only). So the owner's Token Plan is in the sgp cluster, and the client's default region is now `sgp`, with this evidence in the file. W10.11 (addendum W12) holds on both halves: 71 dry-run checks passed sending nothing, and one live request returned the documented model id. Not settled: which of the two authentication headers the host reads (both were sent); the account's concurrency limit; the quota's status code when exhausted.

## How these three files sit in the rig

There is no `__init__.py` here on purpose. `clients` is an implicit namespace package, which
is what A1's `from clients.deepseek_client import send` needs, and it is the safer of the two:
with an `__init__.py`, a `clients/` folder earlier on `sys.path` would hide this one, whereas
a namespace package merges. This was checked by importing A1's `deepseek_transport` from an
unrelated working directory and reading back `CLIENT = "clients.deepseek_client"`.

No driver holds the Atria client yet. Stage E is where it is wanted (W10's addendum: "stage
E's cross-examination may use Atria beside the five DeepSeek examiners for the analysis the
owner names, one at a time"). Its `send(...)` has the same four-value shape as the DeepSeek
seam, so a driver written for one can hold the other.

No driver holds the MiMo client either, and stage E is where it is wanted as well (W12:
"MiMo 2.6 Pro runs as an examiner armed with the skill, over the same marked results and the
same sampled half of the reports"). The three `send(...)` signatures were read back side by
side from an unrelated working directory - all three are
`(body, key, tag='', stream_path=None, tries=7)` - and importing `clients.mimo_client` there
left `SENDS` at 0, so nothing is sent on import. What a stage E driver must **not** do is sum
the families: W12 section 6 names "summing families" as the first trap, and each family's
agreement is its own count against the same 40 of 48.

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
the same request, not a second request.** All three clients keep the two apart: one record per
request, every transport attempt listed inside it under `attempts`. Count records for PA.1;
read `attempts` to see how the service behaved. In `mimo_client.py` each attempt also carries
`paced_seconds`, the seconds the 30-a-minute pacer held it, so a slow run can be read as
pacing rather than as the service being slow.

## What is not settled here, and not by anything on the web

Whether the beta prefix endpoint accepts thinking mode on `deepseek-flash`. No page found says.
No client drops thinking to make a request succeed: a run made under a different thinking
setting is a different arm, so the service's own words come back instead, whole, and the
driver stops the run.

Whether MiMo continues a prefilled assistant message, and whether its Token Plan host reads
`api-key` or `Authorization: Bearer`. Neither is settled by anything on the web; the second
is settled by the live check above, the first only by a run nobody has asked for yet.

## What this MiMo client would be wrong about, and how it would show

Written before the live check, so that the check can catch it out rather than agree with it.

| Claim in the client | What would show it wrong | Looked? |
|---|---|---|
| A `tp-` key belongs on a `token-plan-*` host, not `api.xiaomimimo.com` | a 200 from the pay-as-you-go base with a `tp-` key (run it with `check_mix=False`) | Read the provider's own quick-access page; not tried live |
| The default region `cn` is the owner's | a 401 or 404 from `token-plan-cn` that `sgp` or `ams` answers | No; nothing on the web ties a key to a region |
| Sending both headers is accepted | a 400 or 401 that one header alone does not get | No; the two sources disagree and no page forbids both |
| `max_completion_tokens` is the name this endpoint takes | a 400 naming the parameter, or a 200 whose reply is short because the ceiling was ignored | Read on the API page and in the provider's Python sample |
| 131072 is the ceiling's maximum | a 400 at 131072, or a documented number elsewhere | Read on the API page (`1 to 131072`) and the model page (`128K`) |
| `thinking` defaults to enabled and may be sent explicitly | a 400 on the `thinking` object, or `thinking_seen` false | Read on the API page; the gauge is in every record |
| Streaming may lose usage without `stream_options` | `usage_missing` false on a streamed call | No page found says; the gauge is the only evidence there will be |
| A retry is useless on 402 | a 402 that a later attempt answers with a 200 | Read the error table and the price page; not tried |
| 30 a minute is the binding cap | the service refusing at a rate below 30 | Documented RPM is 100; the owner's rule is the lower number |
