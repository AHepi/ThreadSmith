"""The MiMo client for plan W10, stage E (addendum W12: MiMo 2.6 Pro as a third examiner
family).

A LIBRARY. Nothing is sent on import. The only thing this file sends is what a caller asks
it to send, and `--dry` sends nothing at all.

  python3 mimo_client.py --dry                 # builds every stage E request shape, sends nothing
  python3 mimo_client.py --dry --save DIR      # and writes each request text to DIR

The key is read from the environment variable MIMO_API_KEY, at call time only. It is put in
one place, the authentication header of a live request, and in no other: no record this file
returns contains it, and `assert_no_key` is run over every record before it is handed back.
MIMO_API_KEY is also the variable name the service's own Python sample uses.

WHAT THE SERVICE SAYS (all of this is CLAIMED; read 22 September 2026, quoted with its
address; nothing outside this repository was kept as a file)

  https://mimo.mi.com/docs/en-US/quick-start/summary/first-api-call
    Base URLs: pay-as-you-go (real time) "https://api.xiaomimimo.com/v1" (OpenAI) or
    "https://api.xiaomimimo.com/anthropic" (Anthropic); batch inference
    "https://batch-api-cn.xiaomimimo.com/v1"; Token Plan "https://token-plan-cn.xiaomimimo.com/v1"
    (OpenAI) or "https://token-plan-cn.xiaomimimo.com/anthropic". Key formats:
    pay-as-you-go "sk-xxxxx", Token Plan (Individual) "tp-xxxxx", Token Plan (Team)
    "ttp-xxxxx". The OpenAI sample:
      client = OpenAI(api_key=os.environ.get("MIMO_API_KEY"),
                      base_url="https://api.xiaomimimo.com/v1")
      completion = client.chat.completions.create(
          model="mimo-v2.6-pro",
          messages=[{"role": "user", "content": "please introduce yourself"}],
          max_completion_tokens=1024)
  https://mimo.mi.com/docs/en-US/tokenplan/Token%20Plan/quick-access
    Token Plan keys are "tp-xxxxx" or "ttp-xxxxx", "distinct from pay-as-you-go keys
    (sk-xxxxx) and cannot be used interchangeably". Three regional clusters, OpenAI
    protocol: China "https://token-plan-cn.xiaomimimo.com/v1", Singapore
    "https://token-plan-sgp.xiaomimimo.com/v1", Europe
    "https://token-plan-ams.xiaomimimo.com/v1"; Anthropic protocol the same hosts with
    "/anthropic". OpenAI path "/chat/completions"; model "mimo-v2.6-pro".
  https://mimo.mi.com/models/en-US/mimo-v2.6-pro
    Model ID "mimo-v2.6-pro". Context window "1M tokens". Max output "128K tokens".
    Price per million tokens: input cache hit "$0.0036", input cache miss "$0.435",
    output "$0.87". Capabilities listed: "Omni-Modal Understanding", "Deep Thinking",
    "Tool Call", "Streaming", "Web Search", "Structured Output", "Context Caching".
  https://mimo.mi.com/docs/en-US/api/chat/openai-api
    POST "https://api.xiaomimimo.com/v1/chat/completions". Header
    'api-key: $MIMO_API_KEY' in the page's own curl:
      curl --location --request POST 'https://api.xiaomimimo.com/v1/chat/completions' \\
      --header "api-key: $MIMO_API_KEY" --header "Content-Type: application/json" \\
      --data-raw '{"model": "mimo-v2.6-pro", ...}'
    Message roles: "developer", "system", "user", "assistant", "tool". Models:
    "mimo-v2.6-flash", "mimo-v2.6-pro", "mimo-v2.6-pro-ultraspeed", "mimo-v2.5-pro",
    "mimo-v2.5". max_completion_tokens integer "1 to 131072", "default varies by model";
    temperature default 1.0 range "[0, 1.5]"; top_p default 0.95 "[0.01, 1.0]";
    frequency_penalty and presence_penalty "[-2.0, 2.0]"; stream boolean default false;
    stop "up to 4 sequences"; tools; tool_choice "Available options: auto", and "When a
    value other than auto is passed to tool_choice, the backend will remove this field by
    default"; response_format type "text"; thinking object type "enabled" or "disabled",
    default "enabled" for mimo-v2.6-pro. Reply: choices[0].message.content,
    message.reasoning_content "(in thinking mode)", message.tool_calls; finish_reason one
    of "stop|length|tool_calls|content_filter|repetition_truncation"; usage carries
    prompt_tokens, completion_tokens, total_tokens,
    prompt_tokens_details.cached_tokens, completion_tokens_details.reasoning_tokens.
    Streamed objects are "chat.completion.chunk" with delta fields.
  https://mimo.mi.com/docs/en-US/quick-start/faq/api-integration
    Authentication: '"api-key: $MIMO_API_KEY" or "Authorization: Bearer $MIMO_API_KEY"'
    for pay-as-you-go calls. Roles "developer/system/user/assistant" on the OpenAI
    interface; the Anthropic interface uses "a separate system parameter". In thinking
    mode the model returns "reasoning_content" beside "tool_calls", and developers should
    "keep all previous reasoning_content in the messages array".
  https://mimo.mi.com/docs/en-US/api/chat/anthropic-api
    "https://api.xiaomimimo.com/anthropic/v1/messages", header "api-key: $MIMO_API_KEY";
    max_tokens "[1, 131072]" for mimo-v2.6-pro; system "string | array"; thinking
    {"type": "enabled"}; in thinking mode temperature and top_p are "forcibly overridden"
    with the defaults 1.0 and 0.95.
  https://mimo.mi.com/docs/en-US/api/guidance/rate-limit
    mimo-v2.6-pro: RPM 100, TPM 10M (the same for mimo-v2.6-flash, mimo-v2.5-pro,
    mimo-v2.5; mimo-v2.6-pro-ultraspeed is "Customized services available, please contact
    us"). "The platform sets a model concurrency limit for each account" - with no number
    given. "When the server load is high, response delays or 429 error may occur."
  https://mimo.mi.com/docs/en-US/quick-start/summary/model
    Table: mimo-v2.6-pro, context window "1M", max output "128K", RPM 100, TPM 10M.
  https://mimo.mi.com/docs/en-US/api/guidance/error-codes
    400 "Invalid request format"; 401 "Missing or invalid API Key, or incorrect
    Authorization request header format"; 402 "Insufficient account balance"; 403
    "Forbidden Access"; 404 "Not Found"; 421 "Content Filter"; 429 "Too Many Requests" ->
    "Implement exponential backoff and retry logic, or reduce request frequency"; 500
    "Server Error" -> "Please try again later"; 503 "Server Overloaded" -> "Please try
    again later".
  https://mimo.mi.com/docs/en-US/price/token-plan
    Individual tiers: Lite "$6/month, ¥39/month" "4.1 billion Credits"; Standard "$16/month,
    ¥99/month" "11 billion Credits"; Pro "$50/month, ¥329/month" "38 billion Credits"; Max
    "$100/month, ¥659/month" "82 billion Credits". "all plans support the latest flagship
    models mimo-v2.6-pro, mimo-v2.6-flash, as well as ASR and TTS models". "When the monthly
    total quota of the package is used up, the system will suspend the service and will not
    continue to deduct from your bonus or account balance."

  TWO THIRD-PARTY PAGES, WHICH ARE NOT THE PROVIDER'S WORD
  https://docs.openclaw.ai/providers/xiaomi - "Token Plan keys (tp-...)" are used "against
    regional base URLs matching the subscription region (cn, sgp, or ams)"; context
    1,048,576, max output 131,072.
  https://github.com/openclaw/openclaw/issues/77692 (5 May 2026, open, no maintainer reply)
    "fix(tts/xiaomi): Xiaomi Token Plan endpoint uses Bearer auth, not api-key header":
    "api-key header -> token-plan-cn -> 401 Invalid API Key";
    "Authorization: Bearer -> token-plan-cn -> 200 OK, audio returned". That report is about
    the TTS endpoint, by a third party, and contradicts the provider's own curl. It is why
    this client sends BOTH headers by default (see AUTH_STYLE below).

WHAT NO PAGE FOUND SAYS (unknown, not absent; the questions are in clients/README.md)
  Which region a given tp- key belongs to, and what a wrong-region base returns.
  Whether a tp- key is accepted on the pay-as-you-go base (the pages say the two "cannot be
    used interchangeably"; they do not say what the refusal looks like).
  The account concurrency number; whether Token Plan keys share the pay-as-you-go RPM 100 /
    TPM 10M or have their own; which status code an exhausted plan quota returns.
  The default of max_completion_tokens when it is omitted for mimo-v2.6-pro.
  Whether the legacy name "max_tokens" is accepted on the OpenAI endpoint.
  Whether "stream_options": {"include_usage": true} is accepted, and so whether a streamed
    reply carries usage at all.
  Whether the last message may be an assistant message meant to be continued (DeepSeek's
    prefix completion). Nothing found says so either way. "Found nowhere" is unknown.

THE NUMBERS HERE, AND WHAT HOLDS THEM
  MAX_TOKENS = 131072, the documented maximum for max_completion_tokens (128K). The
    addendum W12 says "token spend not limited below the documented maximum", so this is the
    default; a caller's explicit ceiling is sent AS GIVEN and never raised, because the
    record has to show what the caller sent (the same rule as deepseek_client.send).
  MAX_WORKERS = 5. W12 section 3: "at most five MiMo examiners at a time as for DeepSeek".
    It is the plan's number, not the service's: the service documents RPM 100 and does not
    publish its concurrency number at all. Asking for six raises, with the plan quoted,
    rather than being clamped quietly.
  RPM_CAP = 30, the owner's later rule (decision W9), which clients/README.md says applies
    to this client as well as to Atria's. A pacer in this module, the same one and under the
    same names as in atria_client.py, holds two seconds between the starts of two HTTP
    attempts, retries included, across every thread. It spaces the starts and does not
    serialise the exchanges, so five examiners can still be in flight at once. It binds well
    below the documented RPM 100, so the owner's number is the one that decides.
  Seven attempts, 4 s doubling to 90 s with jitter, Retry-After honoured up to 300 s. The
    schedule is the DeepSeek client's, carried over: fitted on that rig's runs, not tested
    here, and the error-codes page asks for exactly "exponential backoff and retry logic"
    on a 429 without naming a schedule.
  Retry on 408/409/425/429 and 5xx and on transport errors; never on 400/401/402/403/404/421,
    whose own documented remedy is to change the request, the key or the content. 402 is in
    that list on purpose: an exhausted plan is not fixed by asking again.
  Nothing undocumented is sent. No reasoning_effort (that is DeepSeek's parameter, not this
    service's), no stream_options unless a caller asks for it, no temperature or top_p by
    default - in thinking mode the service says it overrides both, and a record showing a
    temperature that was overridden would describe a request that was not the one that ran.

RETRIES AND PA.1. As in the two other clients: one record per request, every transport
attempt listed inside it under "attempts". Count records for PA.1; read attempts to see how
the service behaved.

THE SEAM. `send(body, key, tag=, stream_path=, tries=)` returns
(message, finish_reason, usage, http) - the same four values as
clients/deepseek_client.send and clients/atria_client.send, so a driver written for one
holds this one.
"""
import argparse
import concurrent.futures as cf
import json
import os
import random
import sys
import threading
import time

try:
    import requests
except ImportError:                                   # --dry needs no transport
    requests = None

# The three documented Token Plan clusters. The owner's key begins "tp-", which the
# documentation makes a Token Plan (Individual) key, so a Token Plan base is the default
# here and the pay-as-you-go base is not. WHICH region is unknown: see clients/README.md.
TOKEN_PLAN_BASES = {
    "cn": "https://token-plan-cn.xiaomimimo.com/v1",
    "sgp": "https://token-plan-sgp.xiaomimimo.com/v1",
    "ams": "https://token-plan-ams.xiaomimimo.com/v1",
}
PAYG_BASE = "https://api.xiaomimimo.com/v1"
BATCH_BASE = "https://batch-api-cn.xiaomimimo.com/v1"

# Default region: sgp, SEEN on 22 September 2026 by the one-request live check (Workflow
# addendum W12, W10.11): the owner's tp- key got HTTP 401 from token-plan-cn ("both documented
# headers were sent") and HTTP 200 from token-plan-sgp (finish "stop", reasoning_content
# returned). ams was not tried. The documentation ties no key to a region; this line does.
REGION = (os.environ.get("MIMO_REGION") or "sgp").strip().lower()
BASE = os.environ.get("MIMO_BASE_URL") or TOKEN_PLAN_BASES.get(REGION, TOKEN_PLAN_BASES["cn"])
PATH = "/chat/completions"
MODEL = os.environ.get("MIMO_MODEL", "mimo-v2.6-pro")   # the id is lower case; the page's
                                                        # display name "MiMo-V2.6-Pro" is not it
# The five text ids the OpenAI-compatibility page lists, kept so that a MIMO_MODEL override
# to something the documentation does not name is seen in the dry run rather than at the 400.
DOCUMENTED_MODELS = ("mimo-v2.6-pro", "mimo-v2.6-flash", "mimo-v2.6-pro-ultraspeed",
                     "mimo-v2.5-pro", "mimo-v2.5")
MAX_TOKENS = 131072              # the documented maximum for max_completion_tokens (128K)
CONTEXT = 1048576                # the documented context window, 1M
MAX_WORKERS = 5                  # W12 section 3, as for DeepSeek
RPM = 100                        # documented for mimo-v2.6-pro; Token Plan's own is unknown
TPM = 10_000_000                 # documented for mimo-v2.6-pro
MAX_STOP = 4                     # "up to 4 sequences"
RPM_CAP = 30                     # the owner's rule (Workflow decision W9): at most 30 requests
                                 # a minute, and clients/README.md says it applies here too.
                                 # It is far below the documented RPM 100, so this cap, not the
                                 # service's, is the one that binds.
MIN_GAP = 60.0 / RPM_CAP         # seconds between the starts of two HTTP attempts
KEY_ENV = "MIMO_API_KEY"
PLAN_PREFIXES = ("ttp-", "tp-")  # longest first: "ttp-" also starts with no shorter prefix
PAYG_PREFIX = "sk-"

# "both" sends api-key AND Authorization: Bearer. The provider's own curl uses api-key; a
# third-party issue says the Token Plan host refuses it and wants Bearer (see the head of
# this file). The two claims disagree, so one request carries both documented headers and
# the first live call does not have to guess. Set MIMO_AUTH_STYLE to "api-key" or "bearer"
# to send one alone - which is how the live check settles which the host actually reads.
AUTH_STYLE = (os.environ.get("MIMO_AUTH_STYLE") or "both").strip().lower()
AUTH_STYLES = ("api-key", "bearer", "both")

TIMEOUT = (30, 1800)             # connect, read
TRIES = 7
DELAY0 = 4.0
DELAY_CAP = 90.0
RETRY_AFTER_CAP = 300.0          # a Retry-After is honoured up to here, above the backoff cap

NO_RETRY = (400, 401, 402, 403, 404, 421)
RETRY_STATUS = (408, 409, 425, 429, 500, 502, 503, 504)

# The documentation names no rate-limit response header. Whatever of these appears is kept;
# an empty dict means none appeared, which is itself worth seeing in the first live record.
RATE_HEADERS = ("retry-after", "x-ratelimit-limit-requests", "x-ratelimit-remaining-requests",
                "x-ratelimit-limit-tokens", "x-ratelimit-remaining-tokens",
                "x-rpm-limit", "x-rpm-remaining", "x-request-id", "x-mimo-request-id")

_print_lock = threading.Lock()
_SLEEP = time.sleep                  # named so the dry run can hold the clock still
_PACE_LOCK = threading.Lock()
_PACE_SLEEP = time.sleep             # the pacer's own sleep, so the dry run can stub it apart
                                     # from the backoff's
_LAST_START = [float("-inf")]        # wall-clock time of the last HTTP attempt's start
SENDS = 0                            # live HTTP attempts made by this process; --dry asserts 0


def _pace(now=None):
    """Hold the process to RPM_CAP: wait until MIN_GAP seconds have passed since the last
    attempt started, then claim this start. Retries count as attempts, so a 429 storm
    cannot exceed the cap either. The same pacer, with the same names, is in
    clients/atria_client.py, so a reviewer reads one mechanism and not two. Returns the
    seconds waited (the dry run reads it).

    Five workers are still five: the cap spaces the STARTS, it does not serialise the
    exchanges, so five MiMo examiners can be in flight at once as W12 allows."""
    with _PACE_LOCK:
        t = time.time() if now is None else now
        wait = max(0.0, _LAST_START[0] + MIN_GAP - t)
        if wait > 0:
            _PACE_SLEEP(wait)
        _LAST_START[0] = time.time() if now is None else t + wait
        return wait


def _pace_check():
    """The pacer's own check on a still clock: starts asked at t = 0, 0.5 and 2.6 s are held
    to t = 0, 2.0 and 4.0, so the waits are 0, 1.5 and 1.4 s."""
    global _PACE_SLEEP
    real, waited = _PACE_SLEEP, []
    _PACE_SLEEP = lambda w: waited.append(round(w, 3))
    try:
        _LAST_START[0] = float("-inf")
        w = [_pace(now=0.0), _pace(now=0.5), _pace(now=2.6)]
    finally:
        _PACE_SLEEP = real
        _LAST_START[0] = float("-inf")
    return [round(x, 3) for x in w], waited


class MiMoError(RuntimeError):
    """A request that did not come back as a reply. `retryable` says whether trying again
    could help; `status` and `body` carry the service's own words, unedited."""

    def __init__(self, message, status=None, body="", retryable=False, tag=""):
        super().__init__(message)
        self.status, self.body, self.retryable, self.tag = status, body, retryable, tag


# ---------------------------------------------------------------- the key, and the guards

def key_from_env(required=True):
    """Read the key from the environment at call time. Never written to a file, never
    returned inside a record, never printed."""
    k = os.environ.get(KEY_ENV, "")
    if not k and required:
        raise SystemExit(f"{KEY_ENV} not set. Nothing sent.")
    return k


def key_kind(key):
    """What the key's prefix says it is. Reads the prefix and nothing else, and returns no
    part of the key. "unknown" is not an error: the prefixes are the documentation's, not a
    rule the service is known to enforce."""
    if not key:
        return "none"
    for p in PLAN_PREFIXES:
        if key.startswith(p):
            return "token-plan-team" if p == "ttp-" else "token-plan"
    if key.startswith(PAYG_PREFIX):
        return "pay-as-you-go"
    return "unknown"


def base_kind(url):
    host = (url or "").split("//", 1)[-1].split("/", 1)[0].lower()
    if host.startswith("token-plan-"):
        return "token-plan"
    if host == "api.xiaomimimo.com":
        return "pay-as-you-go"
    if host.startswith("batch-api"):
        return "batch"
    return "other"


def check_key_and_base(key, url, strict=True):
    """Refuse, before anything is sent, to put a Token Plan key on a pay-as-you-go base or
    the other way round: the quick-access page says the two kinds of key are "distinct" and
    "cannot be used interchangeably". Returns a note for the record. An "unknown" prefix or
    an "other" host passes, with the note saying so - the guard is on what is documented,
    not on what is guessed. Pass strict=False to send anyway, which is how the owner would
    find out that the documentation is wrong."""
    kk, bk = key_kind(key), base_kind(url)
    note = f"key {kk} -> base {bk}"
    bad = ((kk in ("token-plan", "token-plan-team") and bk in ("pay-as-you-go", "batch"))
           or (kk == "pay-as-you-go" and bk == "token-plan"))
    if bad and strict:
        raise MiMoError(
            f"{note}: the two kinds of key are documented as separate and "
            f"'cannot be used interchangeably' (mimo.mi.com Token Plan quick-access). "
            f"Set MIMO_BASE_URL to the matching host, or pass check_mix=False to send "
            f"anyway. Nothing sent.")
    return note + (" (mixed, sent anyway)" if bad else "")


def assert_no_key(obj, key):
    if not key:
        return obj
    if key in json.dumps(obj, ensure_ascii=False, default=str):
        raise SystemExit("the API key appears in a record. Nothing saved, nothing returned.")
    return obj


def auth_headers(key, style=None):
    """The authentication header(s). Both names are the provider's own (the curl uses
    api-key; the integration FAQ gives Authorization: Bearer as an alternative)."""
    style = (style or AUTH_STYLE).strip().lower()
    if style not in AUTH_STYLES:
        raise ValueError(f"auth style must be one of {AUTH_STYLES}; got {style!r}")
    h = {"Content-Type": "application/json"}
    if style in ("api-key", "both"):
        h["api-key"] = key
    if style in ("bearer", "both"):
        h["Authorization"] = f"Bearer {key}"
    return h


def redacted_headers(style=None):
    style = (style or AUTH_STYLE).strip().lower()
    h = {"Content-Type": "application/json"}
    if style in ("api-key", "both"):
        h["api-key"] = "<redacted>"
    if style in ("bearer", "both"):
        h["Authorization"] = "Bearer <redacted>"
    return h


def endpoint(base=None):
    return (base or BASE).rstrip("/") + PATH


# ---------------------------------------------------------------- the request

def build_body(messages, *, model=MODEL, max_completion_tokens=MAX_TOKENS, max_tokens=None,
               stream=True, thinking=True, include_usage=False, temperature=None, top_p=None,
               tools=None, tool_choice=None, stop=None, response_format=None, extra=None):
    """The request body, with only documented fields in it.

    `max_tokens` is accepted as an alias so that a driver written for the DeepSeek or Atria
    client can hand its own body-building keyword over unchanged; what goes on the wire is
    the name this service documents, `max_completion_tokens`. Ranges are checked against
    the documentation before anything is sent: 1..131072 for the ceiling, at most 4 stop
    sequences, and `tool_choice` only "auto" (the page says any other value is dropped by
    the backend, so sending one would put a field in the record that the service ignored).
    Nothing else is added: no reasoning_effort, and no temperature or top_p unless the
    caller asks, because thinking mode is documented to override both."""
    if max_tokens is not None:
        max_completion_tokens = max_tokens
    if not isinstance(max_completion_tokens, int) or not (1 <= max_completion_tokens <= MAX_TOKENS):
        raise ValueError(f"max_completion_tokens must be an integer in 1..{MAX_TOKENS}; "
                         f"got {max_completion_tokens!r}")
    body = {"model": model, "messages": list(messages),
            "max_completion_tokens": max_completion_tokens, "stream": bool(stream)}
    if thinking is not None:
        # Sent explicitly although "enabled" is the documented default, so the record says
        # what ran rather than resting on a default that can change under a run.
        body["thinking"] = {"type": "enabled" if thinking else "disabled"}
    if stream and include_usage:
        body["stream_options"] = {"include_usage": True}
    if temperature is not None:
        body["temperature"] = temperature
    if top_p is not None:
        body["top_p"] = top_p
    if tools:
        body["tools"] = tools
    if tool_choice is not None:
        if tool_choice != "auto":
            raise ValueError("tool_choice: the documentation lists only 'auto', and says any "
                             "other value is removed by the backend; sending one would record "
                             "a field the service ignored")
        body["tool_choice"] = tool_choice
    if stop:
        stop = list(stop)
        if len(stop) > MAX_STOP:
            raise ValueError(f"at most {MAX_STOP} stop sequences are documented; got {len(stop)}")
        body["stop"] = stop
    if response_format is not None:
        if response_format.get("type") != "text":
            raise ValueError("response_format: the API page documents type 'text' only. The "
                             "model page lists 'Structured Output' as a capability, which is "
                             "the disagreement named in clients/README.md; pass it through "
                             "extra= once a live call has shown it accepted.")
        body["response_format"] = response_format
    if extra:
        body.update(extra)
    return body


def prefill_message(content):
    """An assistant message meant to be continued - DeepSeek's prefix completion.

    NOTHING FOUND DOCUMENTS THIS FOR MiMo. This helper adds no flag (there is none to add):
    it builds a plain assistant message and leaves it last, and whether the service
    continues it or answers as a new turn is unknown. Every record whose last message is an
    assistant message carries `prefill_untested: True`, so a run that used it cannot be read
    as if the question were settled. Stage E does not need it: arm (e) is DeepSeek's."""
    return {"role": "assistant", "content": content}


def request_text(body):
    """The exact bytes that go on the wire, as text: this module serialises the body itself
    and posts those bytes, so the text saved is the text sent."""
    b = {k: v for k, v in body.items() if k != "_endpoint"}
    return json.dumps(b, ensure_ascii=False)


# ---------------------------------------------------------------- the reply

def assemble_stream(lines):
    """Assemble an SSE reply from an iterable of lines (bytes or str). Pure: no network, so
    --dry runs it on canned lines. Returns (message, finish_reason, usage, raw_lines).

    The chunk shape is the documented one: choices[0].delta.content, .reasoning_content,
    .tool_calls, and choices[0].finish_reason. A usage-bearing chunk is kept if one arrives;
    whether one ever does is the open question about stream_options."""
    content, reasoning, finish, usage, tcs, raw = [], [], None, {}, {}, []
    for line in lines:
        s = line.decode("utf-8", "ignore") if isinstance(line, (bytes, bytearray)) else line
        if not s.strip():
            continue
        raw.append(s)
        if s.startswith(":"):
            continue
        if not s.startswith("data:"):
            continue
        data = s[5:].strip()
        if data == "[DONE]":
            break
        try:
            ch = json.loads(data)
        except ValueError:
            continue
        if ch.get("usage"):
            usage = ch["usage"]
        for c in ch.get("choices", []):
            d = c.get("delta") or {}
            if d.get("content"):
                content.append(d["content"])
            if isinstance(d.get("reasoning_content"), str) and d["reasoning_content"]:
                reasoning.append(d["reasoning_content"])
            for tc in d.get("tool_calls") or []:
                i = tc.get("index", 0)
                slot = tcs.setdefault(i, {"id": "", "type": "function",
                                          "function": {"name": "", "arguments": ""}})
                if tc.get("id"):
                    slot["id"] = tc["id"]
                f = tc.get("function") or {}
                if f.get("name"):
                    slot["function"]["name"] += f["name"]
                if f.get("arguments"):
                    slot["function"]["arguments"] += f["arguments"]
            if c.get("finish_reason"):
                finish = c["finish_reason"]
    msg = {"content": "".join(content), "reasoning_content": "".join(reasoning),
           "tool_calls": [tcs[i] for i in sorted(tcs)] or None}
    return msg, finish, usage, raw


def message_from_json(doc):
    """Assemble a non-streamed reply along the documented reply paths."""
    ch = (doc.get("choices") or [{}])[0]
    m = ch.get("message") or {}
    reasoning = m.get("reasoning_content") or ""
    msg = {"content": m.get("content") or "",
           "reasoning_content": reasoning if isinstance(reasoning, str)
           else json.dumps(reasoning, ensure_ascii=False),
           "tool_calls": m.get("tool_calls") or None}
    return msg, ch.get("finish_reason"), doc.get("usage") or {}


def reasoning_tokens(usage):
    d = (usage or {}).get("completion_tokens_details") or {}
    return d.get("reasoning_tokens")


def cached_tokens(usage):
    d = (usage or {}).get("prompt_tokens_details") or {}
    return d.get("cached_tokens")


def cost(usages):
    """The published pay-as-you-go card: cache hit $0.0036, cache miss $0.435, output $0.87
    per million tokens. A tp- key spends plan Credits instead, and the documentation gives
    no Credit-per-token rate, so this figure is what the same traffic would have cost on
    pay-as-you-go - a comparison with the DeepSeek round, not a bill."""
    hit = sum(cached_tokens(u) or 0 for u in usages)
    miss = sum((u.get("prompt_tokens", 0) - (cached_tokens(u) or 0)) for u in usages)
    out = sum(u.get("completion_tokens", 0) for u in usages)
    return hit, miss, out, hit / 1e6 * 0.0036 + miss / 1e6 * 0.435 + out / 1e6 * 0.87


# ---------------------------------------------------------------- the transport

def _stamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


def _say(s, verbose=True):
    if verbose:
        with _print_lock:
            print(s, file=sys.stderr, flush=True)


def _sleep(delay, retry_after):
    # `is not None`, not truthiness: Retry-After: 0 means retry now.
    wait = retry_after if retry_after is not None else delay * (0.75 + 0.5 * random.random())
    _SLEEP(wait)
    return min(delay * 2, DELAY_CAP)


def _retry_after(resp):
    try:
        v = resp.headers.get("Retry-After")
        return min(float(v), RETRY_AFTER_CAP) if v is not None else None
    except (TypeError, ValueError):
        return None


def _headers_seen(resp):
    try:
        got = {str(k).lower(): str(v) for k, v in dict(resp.headers).items()}
    except Exception:
        return {}, {}
    return got, {k: v for k, v in got.items() if k in RATE_HEADERS}


def call(body, key, *, tag="", url=None, stream_path=None, tries=TRIES, timeout=TIMEOUT,
         keep_raw=True, verbose=True, auth_style=None, check_mix=True):
    """Send one request and return the whole of both sides as one record.

    The record carries the body as sent and its exact text, the endpoint, the headers with
    the key redacted, every attempt, the response headers as they came, the assembled
    message, the finish reason, the usage, the raw return, and four gauges:
      truncated             finish_reason == "length": the ceiling was reached
      repetition_truncated  finish_reason == "repetition_truncation", which this service
                            documents and the other two do not
      usage_missing         a streamed reply that carried no usage at all, which is what
                            would show that stream_options is needed and undocumented
      thinking_seen         reasoning_content came back, or reasoning_tokens > 0: the
                            documented default "enabled" actually ran
    It carries no key."""
    global SENDS
    if requests is None:
        raise SystemExit("the requests package is not installed. Nothing sent.")
    url = url or body.get("_endpoint") or endpoint()
    style = (auth_style or AUTH_STYLE).strip().lower()
    mix_note = check_key_and_base(key, url, strict=check_mix)
    text = request_text(body)
    payload = text.encode("utf-8")
    headers = auth_headers(key, style)
    stream = bool(body.get("stream"))
    last_role = (body.get("messages") or [{}])[-1].get("role")
    rec = {"client": "clients.mimo_client", "tag": tag, "url": url,
           "model": body.get("model"), "max_completion_tokens": body.get("max_completion_tokens"),
           "auth_style": style, "key_base": mix_note, "rpm_cap": RPM_CAP,
           "request": {k: v for k, v in body.items() if k != "_endpoint"},
           "request_text": text, "request_bytes": len(payload),
           "headers_sent": redacted_headers(style),
           "attempts": [], "response_headers": {}, "rate_headers": {},
           "started_at": _stamp(), "seconds": None,
           "message": None, "finish_reason": None, "usage": {}, "raw": None,
           "http_status": None, "truncated": None, "repetition_truncated": None,
           "usage_missing": None, "thinking_seen": None,
           "prefill_untested": last_role == "assistant"}
    t0 = time.time()
    delay, last = DELAY0, None
    for n in range(1, tries + 1):
        a = {"n": n, "at": _stamp(), "status": None, "error": None, "seconds": None}
        ta = time.time()
        try:
            a["paced_seconds"] = round(_pace(), 3)
            SENDS += 1
            r = requests.post(url, data=payload, headers=headers, timeout=timeout,
                              stream=stream)
            a["status"] = r.status_code
            seen, rate = _headers_seen(r)
            rec["response_headers"] = seen or rec["response_headers"]
            rec["rate_headers"] = rate or rec["rate_headers"]
            if r.status_code in NO_RETRY:
                a["error"] = r.text[:2000]
                a["seconds"] = round(time.time() - ta, 1)
                rec["attempts"].append(a)
                rec.update({"http_status": r.status_code,
                            "seconds": round(time.time() - t0, 1), "finished_at": _stamp()})
                hint = ""
                if r.status_code == 401 and style != "both":
                    hint = (f" - only the {style!r} header was sent; the two documented "
                            f"headers disagree (see clients/README.md), so try the other")
                elif r.status_code == 401:
                    hint = f" - both documented headers were sent; {mix_note}"
                elif r.status_code == 402:
                    hint = " - 'Insufficient account balance'; a Token Plan quota that is " \
                           "used up suspends the service, and a retry cannot fix it"
                raise _with_record(
                    MiMoError(f"{tag}: HTTP {r.status_code}, not retryable{hint}",
                              status=r.status_code, body=r.text[:4000], retryable=False,
                              tag=tag), rec, key)
            if r.status_code != 200:
                a["error"] = r.text[:600]
                a["seconds"] = round(time.time() - ta, 1)
                rec["attempts"].append(a)
                last = MiMoError(f"{tag}: HTTP {r.status_code}", status=r.status_code,
                                 body=r.text[:4000],
                                 retryable=r.status_code in RETRY_STATUS, tag=tag)
                if r.status_code not in RETRY_STATUS or n == tries:
                    rec.update({"http_status": r.status_code,
                                "seconds": round(time.time() - t0, 1), "finished_at": _stamp()})
                    raise _with_record(last, rec, key)
                _say(f"  {tag}: HTTP {r.status_code}, attempt {n} of {tries}", verbose)
                delay = _sleep(delay, _retry_after(r))
                continue
            if stream:
                msg, finish, usage, raw = assemble_stream(r.iter_lines())
                if stream_path:
                    os.makedirs(os.path.dirname(os.path.abspath(stream_path)), exist_ok=True)
                    with open(stream_path, "w", encoding="utf-8") as f:
                        f.write("\n".join(raw))
                rec["raw"] = raw if keep_raw else {"stream_lines": len(raw),
                                                   "saved": stream_path}
            else:
                doc = r.json()
                msg, finish, usage = message_from_json(doc)
                rec["raw"] = doc if keep_raw else {"kept": False}
            a["seconds"] = round(time.time() - ta, 1)
            rec["attempts"].append(a)
            rt = reasoning_tokens(usage)
            rec.update({"message": msg, "finish_reason": finish, "usage": usage or {},
                        "http_status": 200,
                        "truncated": finish == "length",
                        "repetition_truncated": finish == "repetition_truncation",
                        "usage_missing": bool(stream) and not usage,
                        "thinking_seen": bool(msg.get("reasoning_content")) or bool(rt),
                        "seconds": round(time.time() - t0, 1), "finished_at": _stamp()})
            if rec["truncated"]:
                _say(f"  {tag}: finish reason 'length' at max_completion_tokens "
                     f"{body.get('max_completion_tokens')}: the reply is cut off", verbose)
            if rec["repetition_truncated"]:
                _say(f"  {tag}: finish reason 'repetition_truncation': the service cut the "
                     f"reply for repeating, which is not the same as a short answer", verbose)
            if rec["usage_missing"]:
                _say(f"  {tag}: the streamed reply carried no usage; "
                     f"include_usage=True adds stream_options, which is undocumented here",
                     verbose)
            return assert_no_key(rec, key)
        except MiMoError:
            raise
        except Exception as e:
            a["error"] = repr(e)[:600]
            a["seconds"] = round(time.time() - ta, 1)
            rec["attempts"].append(a)
            last = MiMoError(f"{tag}: {a['error']}", retryable=True, tag=tag)
            if n == tries:
                break
            _say(f"  {tag}: retry after {a['error']}", verbose)
            delay = _sleep(delay, None)
    rec["seconds"] = round(time.time() - t0, 1)
    rec["finished_at"] = _stamp()
    raise _with_record(last or MiMoError(f"{tag}: gave up with no attempt recorded", tag=tag),
                       rec, key)


def _with_record(err, rec, key):
    """Every failure carries the whole record out with it: the body as sent, every attempt,
    and the service's own words. A failed request is the one whose record is most needed."""
    err.record = assert_no_key(rec, key)
    return err


def send(body, key, tag="", stream_path=None, tries=TRIES):
    """The seam: (message, finish_reason, usage, http) - the same four values as
    clients/deepseek_client.send and clients/atria_client.send, so a driver written for one
    holds this one.

    The caller's body is sent as given. A caller's ceiling is NOT raised to this module's
    maximum: the record has to show what the caller sent, and a request quietly changed
    underneath a driver is a request the driver's own saved copy does not describe. Two
    disagreements with the documentation are said out loud once per call on stderr rather
    than repaired: a ceiling below the documented maximum, and a body carrying the legacy
    name `max_tokens`, which no page found says this service accepts."""
    mt = body.get("max_completion_tokens")
    if isinstance(mt, int) and mt < MAX_TOKENS:
        _say(f"  {tag}: caller's max_completion_tokens {mt} is below the documented maximum "
             f"{MAX_TOKENS}; sent as given (W12 section 3: token spend not limited below the "
             f"documented maximum)")
    if "max_tokens" in body:
        _say(f"  {tag}: the body carries 'max_tokens'; this service documents "
             f"'max_completion_tokens' and nothing found says the legacy name is accepted. "
             f"Sent as given; build_body(max_tokens=...) maps it to the documented name.")
    rec = call(body, key, tag=tag, stream_path=stream_path, tries=tries, keep_raw=False)
    http = {"status": rec["http_status"], "attempts": len(rec["attempts"]),
            "url": rec["url"], "seconds": rec["seconds"],
            "truncated": rec["truncated"],
            "repetition_truncated": rec["repetition_truncated"],
            "usage_missing": rec["usage_missing"], "thinking_seen": rec["thinking_seen"],
            "auth_style": rec["auth_style"], "rate_headers": rec["rate_headers"],
            "prefill_untested": rec["prefill_untested"],
            "stream_lines": (rec["raw"] or {}).get("stream_lines")
            if isinstance(rec["raw"], dict) else None,
            "saved": stream_path}
    return rec["message"], rec["finish_reason"], rec["usage"], http


# ---------------------------------------------------------------- the client

class MiMoClient:
    """At most five worker threads, a ceiling at the documented maximum, and both sides kept
    whole.

    A job is a dict: {"tag": str, "messages": [...], and any argument of build_body}.
    `many` returns one record per job, in the order the jobs were given, with a failure
    recorded as {"tag":..., "error":..., "record":...} rather than raised, so that one bad
    job does not throw away the replies that did come back. `each` runs the same jobs in
    sequence, for the case where the account's unpublished concurrency limit turns out to be
    one."""

    def __init__(self, key=None, *, model=MODEL, max_tokens=MAX_TOKENS, stream=True,
                 thinking=True, include_usage=False, workers=MAX_WORKERS, tries=TRIES,
                 timeout=TIMEOUT, base=None, auth_style=None, check_mix=True, keep_raw=True,
                 verbose=True):
        if workers > MAX_WORKERS:
            raise ValueError(f"at most {MAX_WORKERS} worker threads (W12 section 3: 'at most "
                             f"five MiMo examiners at a time as for DeepSeek'); "
                             f"asked for {workers}")
        if workers < 1:
            raise ValueError("at least one worker")
        style = (auth_style or AUTH_STYLE).strip().lower()
        if style not in AUTH_STYLES:
            raise ValueError(f"auth style must be one of {AUTH_STYLES}; got {style!r}")
        self.key = key if key is not None else key_from_env(required=False)
        self.model, self.max_tokens, self.stream = model, max_tokens, stream
        self.thinking, self.include_usage = thinking, include_usage
        self.workers, self.tries, self.timeout, self.base = workers, tries, timeout, base
        self.auth_style, self.check_mix = style, check_mix
        self.keep_raw, self.verbose = keep_raw, verbose
        # There is no per-client gap setting: the owner's 30-a-minute cap (decision W9) is
        # held by the pacer in this module, across every thread and every retry, so a caller
        # cannot forget it and two mechanisms cannot disagree about the number.

    def body(self, messages, **kw):
        kw.setdefault("model", self.model)
        kw.setdefault("max_completion_tokens", self.max_tokens)
        kw.setdefault("stream", self.stream)
        kw.setdefault("thinking", self.thinking)
        kw.setdefault("include_usage", self.include_usage)
        return build_body(messages, **kw)

    def chat(self, messages, *, tag="", stream_path=None, **kw):
        if not self.key:
            raise SystemExit(f"{KEY_ENV} not set. Nothing sent.")
        b = self.body(messages, **kw)
        return call(b, self.key, tag=tag, url=endpoint(self.base), stream_path=stream_path,
                    tries=self.tries, timeout=self.timeout, keep_raw=self.keep_raw,
                    verbose=self.verbose, auth_style=self.auth_style, check_mix=self.check_mix)

    def _one(self, i, job, stream_dir):
        job = dict(job)
        tag = job.pop("tag", str(i))
        msgs = job.pop("messages")
        sp = os.path.join(stream_dir, f"{tag}.stream.txt") if stream_dir else None
        try:
            return self.chat(msgs, tag=tag, stream_path=sp, **job)
        except MiMoError as e:
            return {"tag": tag, "error": str(e), "status": e.status, "body": e.body,
                    "record": getattr(e, "record", None)}

    def many(self, jobs, *, stream_dir=None):
        jobs = list(jobs)
        out = [None] * len(jobs)
        with cf.ThreadPoolExecutor(max_workers=min(self.workers, max(1, len(jobs)))) as ex:
            futs = {ex.submit(self._one, i, j, stream_dir): i for i, j in enumerate(jobs)}
            for f in cf.as_completed(futs):
                out[futs[f]] = f.result()
        return out

    def each(self, jobs, *, stream_dir=None):
        return [self._one(i, j, stream_dir) for i, j in enumerate(list(jobs))]


# ---------------------------------------------------------------- the stage E shapes

SKILL_SYSTEM = ("You carry the hard-to-vary skill, all eight files. [in a live run this is "
                "the skill as it is on disk, diffed against file 33 before the call]")
EXAMINER_USER = ("Here are the marked results of one arm family and the part of model W8 "
                 "they bear on. Falsify the marks and the reading. Report disagreement with "
                 "the Claude markers field by field.")
REMARK_USER = ("Re-mark this random half of the reports blind, under the frozen criteria of "
               "A4. You are not shown the Claude marks.")


def stage_e_shapes():
    """Every request shape stage E needs, built and returned. W10.11 asks for exactly this:
    "the client dry-runs every request shape stage E needs (a system message with the skill,
    a user message with the marked results, a structured reply) sending nothing"."""
    sys_user = [{"role": "system", "content": SKILL_SYSTEM},
                {"role": "user", "content": EXAMINER_USER}]
    remark = [{"role": "system", "content": SKILL_SYSTEM},
              {"role": "user", "content": REMARK_USER}]
    tool = [{"type": "function",
             "function": {"name": "open_module",
                          "description": "open one reference file of the skill",
                          "parameters": {"type": "object",
                                         "properties": {"name": {"type": "string"}},
                                         "required": ["name"]}}}]
    turn2 = remark + [
        {"role": "assistant", "content": "", "reasoning_content": "which module says so",
         "tool_calls": [{"id": "c1", "type": "function",
                         "function": {"name": "open_module",
                                      "arguments": '{"name":"reporting"}'}}]},
        {"role": "tool", "tool_call_id": "c1", "content": "the marks table"}]
    return {
        # the examiner: the skill as a system message, the marked results as a user message
        "examiner": build_body(sys_user),
        # the blind re-mark of the sampled half
        "remark": build_body(remark),
        # a structured reply: asked for in words, with the one documented response_format
        "structured": build_body(sys_user, response_format={"type": "text"}),
        # an examiner that can open a skill module, as DeepSeek mode 2 does
        "tools": build_body(sys_user, tools=tool, tool_choice="auto"),
        # the second turn, keeping reasoning_content as the documentation asks
        "thinking_turn2": build_body(turn2, tools=tool),
        # non-streamed, where usage comes back whole
        "nostream": build_body(sys_user, stream=False),
        # streamed with usage asked for, which is the undocumented parameter
        "usage": build_body(sys_user, include_usage=True),
        # thinking off, the control for "did thinking do anything"
        "nothinking": build_body(sys_user, thinking=False),
        # a ceiling below the maximum, to show the ceiling is a parameter
        "small": build_body(sys_user, max_tokens=4096),
        # an assistant message left last: UNTESTED, nothing documents it (see prefill_message)
        "prefill": build_body(sys_user + [prefill_message("## 1. The question, frozen\n")],
                              stop=["\n## 7."]),
    }


# ---------------------------------------------------------------- the dry run

CANNED = [
    b": keep-alive",
    b"",
    b'data: {"choices":[{"delta":{"reasoning_content":"weigh "}}]}',
    b'data: {"choices":[{"delta":{"reasoning_content":"it"}}]}',
    b'data: {"choices":[{"delta":{"content":"The mark is"}}]}',
    b'data: {"choices":[{"delta":{"content":" held by job 3."}}]}',
    b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":'
    b'{"name":"open_","arguments":"{\\"name\\":"}}]}}]}',
    b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"function":'
    b'{"name":"module","arguments":"\\"reporting\\"}"}}]}}]}',
    b'data: {"choices":[{"finish_reason":"tool_calls"}]}',
    b'data: {"usage":{"prompt_tokens":11,"completion_tokens":7,"total_tokens":18,'
    b'"prompt_tokens_details":{"cached_tokens":8},'
    b'"completion_tokens_details":{"reasoning_tokens":3}}}',
    b"data: [DONE]",
]
CANNED_NO_USAGE = [
    b'data: {"choices":[{"delta":{"content":"a reply with no usage chunk"}}]}',
    b'data: {"choices":[{"finish_reason":"stop"}]}',
    b"data: [DONE]",
]
CANNED_REPEAT = [
    b'data: {"choices":[{"delta":{"content":"again and again and"}}]}',
    b'data: {"choices":[{"finish_reason":"repetition_truncation"}]}',
    b"data: [DONE]",
]


class _StubResponse:
    def __init__(self, status, lines=None, text="", headers=None, doc=None):
        self.status_code, self._lines, self.text = status, lines or [], text
        self.headers, self._doc = headers or {}, doc

    def iter_lines(self):
        return iter(self._lines)

    def json(self):
        return self._doc


class _StubRequests:
    """A stand-in for the requests module. It reaches no network. It also records how many
    requests were in flight at once, which is how --dry sees the worker count."""

    def __init__(self, script):
        self.script, self.seen, self.lock = script, [], threading.Lock()
        self.inflight, self.peak = 0, 0

    def post(self, url, data=None, headers=None, timeout=None, stream=False):
        with self.lock:
            self.inflight += 1
            self.peak = max(self.peak, self.inflight)
            body = json.loads(data.decode("utf-8"))
            tag = body["messages"][-1]["content"]
            self.seen.append((url, tag, dict(headers)))
            q = self.script[tag]
            r = q.pop(0) if len(q) > 1 else q[0]
        time.sleep(0.02)          # the service taking its time, OUTSIDE the stub's own lock,
        with self.lock:           # so callers overlap here if nothing else stops them
            self.inflight -= 1
        return r


def _raises(fn, kind=Exception):
    try:
        fn()
    except kind:
        return True
    except Exception:
        return False
    return False


def _stub_checks(check):
    """Run the transport paths against the stub. Holds the clock still so no dry run waits."""
    global requests, _SLEEP, SENDS, _PACE_SLEEP
    real_requests, real_sleep, sends0, real_pace = requests, _SLEEP, SENDS, _PACE_SLEEP
    _PACE_SLEEP = lambda s: None   # the dry run does not wait out the 30 rpm cap on stubs
    _LAST_START[0] = float("-inf")
    waited = []
    good = _StubResponse(200, lines=CANNED, headers={"X-Request-Id": "r1",
                                                     "Content-Type": "text/event-stream"})
    script = {
        "fine": [good],
        "flaky": [_StubResponse(429, text="too many", headers={"Retry-After": "0"}), good],
        "nokey": [_StubResponse(401, text='{"error":"Invalid API Key"}')],
        "spent": [_StubResponse(402, text='{"error":"Insufficient account balance"}')],
        "nousage": [_StubResponse(200, lines=CANNED_NO_USAGE)],
        "repeat": [_StubResponse(200, lines=CANNED_REPEAT)],
        "plainjson": [_StubResponse(200, doc={
            "choices": [{"message": {"content": "no stream here", "reasoning_content": "r"},
                         "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 9, "completion_tokens": 6, "total_tokens": 15,
                      "prompt_tokens_details": {"cached_tokens": 4},
                      "completion_tokens_details": {"reasoning_tokens": 2}}})],
    }
    try:
        requests = _StubRequests(script)
        _SLEEP = lambda s: waited.append(s)
        SENDS = 0
        # auth_style is named here rather than left to MIMO_AUTH_STYLE, so the two header
        # checks below test what this client builds and not what the environment happens
        # to say; the single-style path is checked straight after.
        c = MiMoClient(key="tp-not-a-real-key", workers=5, verbose=False, keep_raw=True,
                       base=TOKEN_PLAN_BASES["cn"], auth_style="both")
        jobs = [{"tag": t, "messages": [{"role": "user", "content": t}]}
                for t in ("fine", "flaky", "nokey", "spent", "nousage", "repeat")]
        out = c.many(jobs)
        check("many: one record per job, in the order given",
              [r.get("tag") for r in out] == ["fine", "flaky", "nokey", "spent", "nousage",
                                              "repeat"])
        check("many: the good job carries the assembled reply",
              out[0]["message"]["content"] == "The mark is held by job 3.")
        check("many: the good job is one request with one attempt (PA.1 counts records)",
              len(out[0]["attempts"]) == 1)
        check("many: the ceiling sent is the documented maximum under the documented name",
              out[0]["request"]["max_completion_tokens"] == MAX_TOKENS == 131072)
        check("many: a 429 is retried, and the retry is an attempt, not a second request",
              out[1].get("message") is not None and len(out[1]["attempts"]) == 2,
              f"attempts={len(out[1].get('attempts', []))}")
        check("many: Retry-After was honoured rather than the backoff", waited == [0.0],
              str(waited))
        check("many: a 401 stops at once, is returned, and keeps its record",
              out[2].get("status") == 401 and len(out[2]["record"]["attempts"]) == 1)
        check("many: the service's own words are kept unedited",
              out[2]["body"] == '{"error":"Invalid API Key"}')
        check("many: a 402 is not retried - a spent plan is not fixed by asking again",
              out[3].get("status") == 402 and len(out[3]["record"]["attempts"]) == 1
              and "quota" in out[3]["error"])
        check("the usage gauge fires when a streamed reply carries no usage",
              out[4]["usage_missing"] is True and out[0]["usage_missing"] is False)
        check("the repetition gauge fires on 'repetition_truncation'",
              out[5]["repetition_truncated"] is True and out[5]["truncated"] is False)
        check("the thinking gauge fires on reasoning_content or reasoning_tokens",
              out[0]["thinking_seen"] is True and out[4]["thinking_seen"] is False)
        check("the record keeps the request and the reply whole",
              out[0]["request"]["messages"][-1]["content"] == "fine"
              and out[0]["raw"] == [s.decode() for s in CANNED if s.strip()])
        check("the response headers are kept as they came",
              out[0]["response_headers"].get("x-request-id") == "r1"
              and out[0]["rate_headers"] == {"x-request-id": "r1"})
        sent_headers = requests.seen[0][2]
        check("auth 'both': the key went in api-key AND Authorization, and in no record",
              sent_headers.get("api-key") == "tp-not-a-real-key"
              and sent_headers.get("Authorization") == "Bearer tp-not-a-real-key"
              and "tp-not-a-real-key" not in json.dumps(out, default=str))
        check("the record's own headers are redacted",
              out[0]["headers_sent"] == {"Content-Type": "application/json",
                                         "api-key": "<redacted>",
                                         "Authorization": "Bearer <redacted>"})
        check("SENDS counted every attempt, not every request", SENDS == 7, f"SENDS={SENDS}")

        ns = c.chat([{"role": "user", "content": "plainjson"}], tag="ns", stream=False)
        check("the non-streamed path assembles the reply and keeps the whole document",
              ns["message"]["content"] == "no stream here" and ns["finish_reason"] == "stop"
              and ns["raw"]["usage"]["total_tokens"] == 15 and ns["usage_missing"] is False)
        check("the non-streamed reply carries cached and reasoning token counts",
              cached_tokens(ns["usage"]) == 4 and reasoning_tokens(ns["usage"]) == 2)

        # Five jobs run at five workers and at one, because a check that comes out the same
        # either way measures nothing.
        def five_jobs(workers):
            global requests
            requests = _StubRequests({f"j{i}": [_StubResponse(200, lines=CANNED)]
                                      for i in range(5)})
            cc = MiMoClient(key="tp-not-a-real-key", workers=workers, verbose=False,
                            base=TOKEN_PLAN_BASES["cn"])
            cc.many([{"tag": f"j{i}", "messages": [{"role": "user", "content": f"j{i}"}]}
                     for i in range(5)])
            return requests.peak

        peak5, peak1 = five_jobs(5), five_jobs(1)
        check("five workers run five jobs at once", peak5 == 5, f"peak={peak5}")
        check("the control: one worker runs them one at a time", peak1 == 1, f"peak={peak1}")

        requests = _StubRequests({"seam": [_StubResponse(200, lines=CANNED)]})
        m, fin, us, http = send(build_body([{"role": "user", "content": "seam"}]),
                                "tp-not-a-real-key", tag="seam")
        check("send() returns the four values a driver unpacks",
              m["content"] == "The mark is held by job 3." and fin == "tool_calls"
              and us["total_tokens"] == 18 and http["status"] == 200
              and http["truncated"] is False and http["thinking_seen"] is True)
        check("send() used the module default base, which is a Token Plan one",
              base_kind(http["url"]) == "token-plan", http["url"])

        # The key/base guard, both ways round, and the escape hatch.
        requests = _StubRequests({"mix": [_StubResponse(200, lines=CANNED)]})
        check("a tp- key on the pay-as-you-go base raises before anything is sent",
              _raises(lambda: call(build_body([{"role": "user", "content": "mix"}]),
                                   "tp-not-a-real-key", url=endpoint(PAYG_BASE)), MiMoError))
        check("an sk- key on a Token Plan base raises too",
              _raises(lambda: call(build_body([{"role": "user", "content": "mix"}]),
                                   "sk-not-a-real-key",
                                   url=endpoint(TOKEN_PLAN_BASES["sgp"])), MiMoError))
        mixed = call(build_body([{"role": "user", "content": "mix"}]), "tp-not-a-real-key",
                     url=endpoint(PAYG_BASE), check_mix=False, verbose=False)
        check("check_mix=False sends anyway and the record says the pair was mixed",
              "mixed" in mixed["key_base"], mixed["key_base"])
        check("an unknown key prefix is not refused, only noted",
              key_kind("whatever") == "unknown"
              and "unknown" in check_key_and_base("whatever", endpoint(PAYG_BASE)))
        check("every attempt records the seconds the pacer held it",
              all("paced_seconds" in a for r in out if isinstance(r, dict)
                  and r.get("attempts") for a in r["attempts"])
              and out[0]["rpm_cap"] == RPM_CAP == 30)

        pw, pwaited = _pace_check()
        check("the pacer holds RPM_CAP = 30: starts asked at 0, 0.5 and 2.6 s wait 0, 1.5 "
              "and 1.4 s", pw == [0.0, 1.5, 1.4] and pwaited == [1.5, 1.4],
              f"waits {pw}, slept {pwaited}")
    finally:
        requests, _SLEEP, SENDS, _PACE_SLEEP = real_requests, real_sleep, sends0, real_pace
        _LAST_START[0] = float("-inf")


def _dry(save_dir=None):
    ok, fail = [], []

    def check(name, cond, note=""):
        (ok if cond else fail).append(f"{name}{(' - ' + note) if note else ''}")

    shapes = stage_e_shapes()
    b = shapes["examiner"]
    check("body: the model id is one the documentation lists, in its lower case",
          b["model"] == MODEL and b["model"] in DOCUMENTED_MODELS
          and b["model"] == b["model"].lower(),
          b["model"] + ("" if b["model"] == "mimo-v2.6-pro"
                        else "  - NOT the mimo-v2.6-pro W12 names; set from MIMO_MODEL"))
    check("body: the ceiling is the documented maximum, under the documented name",
          b["max_completion_tokens"] == MAX_TOKENS == 131072 and "max_tokens" not in b,
          str(b.get("max_completion_tokens")))
    check("body: thinking is sent explicitly rather than left to the default",
          b["thinking"] == {"type": "enabled"})
    check("body: nothing undocumented is sent by default",
          set(b) == {"model", "messages", "max_completion_tokens", "stream", "thinking"},
          ", ".join(sorted(b)))
    check("body: no temperature or top_p, which thinking mode is documented to override",
          "temperature" not in b and "top_p" not in b)
    check("body: the skill goes in a system message and the results in a user message",
          [m["role"] for m in b["messages"]] == ["system", "user"])
    check("body: max_tokens= is accepted and mapped to the documented name",
          shapes["small"]["max_completion_tokens"] == 4096
          and "max_tokens" not in shapes["small"])
    check("body: a ceiling above the documented maximum raises",
          _raises(lambda: build_body(b["messages"], max_completion_tokens=MAX_TOKENS + 1)))
    check("body: a ceiling of zero raises",
          _raises(lambda: build_body(b["messages"], max_completion_tokens=0)))
    check("body: more than four stop sequences raises (the page says up to 4)",
          _raises(lambda: build_body(b["messages"], stop=["a", "b", "c", "d", "e"])))
    check("body: a tool_choice other than 'auto' raises, since the backend drops it",
          _raises(lambda: build_body(b["messages"], tool_choice="required")))
    check("body: a response_format other than 'text' raises",
          _raises(lambda: build_body(b["messages"], response_format={"type": "json_object"})))
    check("body: stream_options is sent only when include_usage is asked for",
          "stream_options" not in b
          and shapes["usage"]["stream_options"] == {"include_usage": True})
    check("body: thinking can be turned off, and says so in the body",
          shapes["nothinking"]["thinking"] == {"type": "disabled"})
    check("body: the tools shape carries tools and tool_choice auto",
          shapes["tools"]["tools"][0]["function"]["name"] == "open_module"
          and shapes["tools"]["tool_choice"] == "auto")
    check("body: the second turn keeps reasoning_content, as the FAQ asks",
          shapes["thinking_turn2"]["messages"][2]["reasoning_content"] == "which module says so"
          and shapes["thinking_turn2"]["messages"][3]["role"] == "tool")
    check("body: the non-streamed shape has stream false and no stream_options",
          shapes["nostream"]["stream"] is False and "stream_options" not in shapes["nostream"])
    check("body: the prefill shape ends with an assistant message and carries no made-up flag",
          shapes["prefill"]["messages"][-1] == {"role": "assistant",
                                                "content": "## 1. The question, frozen\n"})
    check("every stage E shape builds", len(shapes) == 10, f"{len(shapes)} shapes")

    check("endpoint: the base in force is a Token Plan one, as a tp- key requires",
          endpoint() == BASE.rstrip("/") + PATH and base_kind(BASE) == "token-plan",
          f"{endpoint()}"
          f"{' (from MIMO_BASE_URL)' if os.environ.get('MIMO_BASE_URL') else ''}")
    check("endpoint: MIMO_BASE_URL overrides it",
          endpoint("https://example.invalid/v9") == "https://example.invalid/v9/chat/completions")
    check("endpoint: the three documented regions are all reachable",
          all(base_kind(u) == "token-plan" for u in TOKEN_PLAN_BASES.values())
          and base_kind(PAYG_BASE) == "pay-as-you-go" and base_kind(BATCH_BASE) == "batch")
    check("key kinds follow the documented prefixes",
          key_kind("tp-x") == "token-plan" and key_kind("ttp-x") == "token-plan-team"
          and key_kind("sk-x") == "pay-as-you-go" and key_kind("") == "none")
    check("auth headers: 'both' carries the two documented names",
          set(auth_headers("k", "both")) == {"Content-Type", "api-key", "Authorization"})
    check("auth headers: one style alone carries one name",
          set(auth_headers("k", "api-key")) == {"Content-Type", "api-key"}
          and set(auth_headers("k", "bearer")) == {"Content-Type", "Authorization"})
    check("auth headers: an unknown style raises", _raises(lambda: auth_headers("k", "basic")))
    check("more than five workers raises", _raises(lambda: MiMoClient(key="x", workers=6)))
    check("five workers is allowed", MiMoClient(key="x", workers=5).workers == 5)

    m, fin, us, raw = assemble_stream(CANNED)
    check("stream: content assembled", m["content"] == "The mark is held by job 3.",
          repr(m["content"]))
    check("stream: reasoning_content assembled", m["reasoning_content"] == "weigh it")
    check("stream: tool call assembled across chunks",
          m["tool_calls"] and m["tool_calls"][0]["function"]["name"] == "open_module"
          and m["tool_calls"][0]["function"]["arguments"] == '{"name":"reporting"}',
          json.dumps(m["tool_calls"]))
    check("stream: finish reason, usage, cached and reasoning tokens read",
          fin == "tool_calls" and us["total_tokens"] == 18 and cached_tokens(us) == 8
          and reasoning_tokens(us) == 3)
    check("stream: keep-alive comment and blank line skipped, raw kept",
          len(raw) == len(CANNED) - 1)
    m3, f3, u3, _ = assemble_stream(CANNED_NO_USAGE)
    check("stream: a reply with no usage chunk assembles and leaves usage empty",
          m3["content"] == "a reply with no usage chunk" and f3 == "stop" and not u3)
    doc = {"choices": [{"message": {"content": "hi", "reasoning_content": "r"},
                        "finish_reason": "length"}], "usage": {"total_tokens": 3}}
    m2, f2, u2 = message_from_json(doc)
    check("non-stream: the documented reply paths are read",
          m2["content"] == "hi" and m2["reasoning_content"] == "r" and f2 == "length"
          and u2["total_tokens"] == 3)

    hit, miss, out_t, usd = cost([{"prompt_tokens": 1_000_000, "completion_tokens": 1_000_000,
                                   "prompt_tokens_details": {"cached_tokens": 400_000}}])
    check("cost() uses the published card: 0.0036 hit, 0.435 miss, 0.87 output",
          (hit, miss, out_t) == (400_000, 600_000, 1_000_000)
          and abs(usd - (0.4 * 0.0036 + 0.6 * 0.435 + 0.87)) < 1e-9, f"${usd:.4f}")

    check("the request text is the bytes sent",
          request_text(b) == json.dumps(b, ensure_ascii=False))
    check("_endpoint is stripped from the text, as the other two clients do",
          "_endpoint" not in request_text(dict(b, _endpoint="https://example.invalid")))
    check("assert_no_key fires on a key in a record",
          _raises(lambda: assert_no_key({"p": "tp-secret"}, "tp-secret"), SystemExit))
    check("assert_no_key passes a clean record",
          assert_no_key({"p": "clean"}, "tp-secret") is not None)

    _stub_checks(check)

    k = os.environ.get(KEY_ENV, "")
    check("no key needed to build anything; key not in environment now", not k,
          "set" if k else "unset")
    if k:
        check("the key in the environment looks like a Token Plan key",
              key_kind(k) in ("token-plan", "token-plan-team"),
              f"it reads as {key_kind(k)}; check the base URL matches it")
    check("nothing was sent to any address", SENDS == 0, f"SENDS={SENDS}")

    print("dry run of clients/mimo_client.py - sends nothing\n")
    for line in ok:
        print("  ok    " + line)
    for line in fail:
        print("  FAIL  " + line)
    print(f"\nendpoint  {endpoint()}   (override with MIMO_BASE_URL; MIMO_REGION picks "
          f"{'/'.join(TOKEN_PLAN_BASES)})")
    print(f"model     {MODEL}   (override with MIMO_MODEL)")
    print(f"ceiling   max_completion_tokens {MAX_TOKENS}, the documented maximum; "
          f"a parameter everywhere")
    print(f"context   {CONTEXT} tokens, documented")
    print(f"threads   at most {MAX_WORKERS} (W12 section 3); documented RPM {RPM}, "
          f"TPM {TPM:,}; the account concurrency number is not published")
    print(f"pace      the owner's cap {RPM_CAP} rpm (decision W9), held by a pacer in this "
          f"file: {MIN_GAP:.1f} s between the starts of two attempts, retries included")
    print(f"auth      {AUTH_STYLE}  (api-key and Authorization: Bearer; the two sources "
          f"disagree - see clients/README.md)")
    print(f"key       read from {KEY_ENV} at call time; "
          f"{'present' if k else 'not present'} in this environment")
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        for name, body in shapes.items():
            p = os.path.join(save_dir, f"mimo.{name}.request.json")
            text = request_text(body)
            assert_no_key({"text": text}, k)
            with open(p, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"  wrote {p} ({len(text)} characters, no key in it)")
    print(f"\n{len(ok)} checks passed, {len(fail)} failed. Nothing sent.")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="MiMo-V2.6-Pro client for plan W10, addendum W12.")
    ap.add_argument("--dry", action="store_true",
                    help="build every stage E request shape, parse a canned stream, send nothing")
    ap.add_argument("--save", metavar="DIR", default=None,
                    help="with --dry, write each request text to DIR")
    args = ap.parse_args()
    if not args.dry:
        raise SystemExit("this file is a library; the only command it runs is --dry. "
                         "Nothing sent.")
    sys.exit(_dry(args.save))
