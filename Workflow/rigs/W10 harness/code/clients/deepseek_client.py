"""The DeepSeek V4.1 Flash client for plan W10, stage A, task A6.

A LIBRARY. Nothing is sent on import. The only thing this file sends is what a caller
asks it to send, and `--dry` sends nothing at all.

  python3 deepseek_client.py --dry                 # builds every request shape, sends nothing
  python3 deepseek_client.py --dry --save DIR      # and writes each request text to DIR

The key is read from the environment variable DEEPSEEK_API_KEY. It is put in one place,
the Authorization header of a live request, and in no other: no record this file returns
contains it, and `assert_no_key` is run over every record before it is handed back.

WHAT THE SERVICE SAYS (CLAIMED; read 22 September 2026, quoted with its address)

  https://api-docs.deepseek.com/api/create-chat-completion/
    endpoint "POST /chat/completions"; max_tokens "The maximum number of tokens that can be
    generated in the chat completion.", "Defaults to 8K (non-thinking) or 64K (thinking;
    128K with reasoning_effort: max). Range: 1-384K (393216)."; reasoning_effort accepts
    "none", "low", "high", "max", default "high"; "thinking": an object with "type"
    ("enabled"/"disabled"); "stop": up to 16 sequences; "stream": SSE terminated by
    "data: [DONE]".
  https://api-docs.deepseek.com/quick_start/pricing
    "deepseek-flash": context "1M", Max Output "MAXIMUM: 384K"; off-peak prices
    cache-hit $0.003, cache-miss $0.15, output $0.6 per 1M tokens; "Peak hours are
    01:00 - 04:00 and 06:00 - 10:00 UTC, Monday through Friday".
  https://api-docs.deepseek.com/guides/chat_prefix_completion/
    base_url "https://api.deepseek.com/beta"; the last message must have role "assistant"
    and "prefix": True; the sample sets stop=["```"]; the feature is Beta. The search
    result for the same page adds: "The reasoning_content is used for the thinking mode in
    the Chat Prefix Completion feature as the input for the CoT in the last assistant
    message, and when using this feature, the prefix parameter must be set to true."
  https://api-docs.deepseek.com/quick_start/rate_limit
    "deepseek-flash": 2500 concurrent connections; "A request counts as one concurrent
    connection from the time it is sent until the model response is complete."; "when the
    concurrency limit is exceeded, you will receive an HTTP 429 error code"; under load the
    service sends keep-alive - non-streaming "Continuously return empty lines", streaming
    "Continuously return SSE keep-alive comments (`: keep-alive`)"; "If the request has not
    started inference after 10 minutes, the server will close the connection."
  https://api-docs.deepseek.com/quick_start/error_codes
    400 "Invalid request body format.", 401 "Authentication fails due to the wrong API
    key.", 402 "You have run out of balance.", 422 "Your request contains invalid
    parameters.", 429 "You are sending requests too quickly.", 500 "Our server encounters
    an issue." -> "Please retry your request after a brief wait", 503 "The server is
    overloaded due to high traffic." -> "Please retry your request after a brief wait."

WHAT THE OLD RIG DOES (SEEN, in this repository)
  HV Skill/rigs/plan 49 rig - DeepSeek on outside papers/run.py:
    URL = "https://api.deepseek.com/chat/completions", MODEL = "deepseek-flash",
    EFFORT = "high", MAX_TOKENS = 24000, ten threads, seven attempts, delay 4 s doubling
    to 90 s, SystemExit on 400/401/402, and the docstring "Streaming captures partial
    output and the finish reason even when the service ends early."

THE NUMBERS HERE, AND WHAT HOLDS THEM
  MAX_TOKENS = 393216. The task for A6 says no token limit below the service's maximum;
    the maximum quoted above is 384K (393216). The old rig's 24000 and the harness's 32000
    are both below it. This client's own default is the maximum; a caller's explicit value
    is sent unchanged (see `send`), because the record must show what the caller sent.
    Untested, and the thing that would show this default wrong: whether the service refuses
    a max_tokens that, with the prompt, would overrun the 1M context. No page found says.
    If it does, the 400 comes back whole, with the service's own words, and is not retried.
  MAX_WORKERS = 5. W10 section 2: "five DeepSeek agents at a time through its API". This is
    the plan's number and not the service's: the rate-limit page above allows 2500
    concurrent connections on deepseek-flash. Asking for more than five raises rather than
    being clamped, so the plan's number cannot be lost quietly.
  Seven attempts, 4 s doubling to 90 s, with jitter and Retry-After honoured. The attempt
    count and the schedule are the old rig's, carried over (fitted on that rig's runs, not
    tested here); the jitter and Retry-After are new and are guesses. Retry-After is
    honoured up to RETRY_AFTER_CAP, which is larger than the backoff cap on purpose: a
    service that asks for five minutes means it, and capping its answer at the backoff
    would just spend the remaining attempts on refusals.
  Retry on 408/429/5xx and on transport errors; never on 400/401/402/422, whose own
    documented remedy is to change the request, so a second identical request cannot help.

RETRIES AND PA.1. W8's PA.1 counts "the number of requests and the text of each request as
sent", and predicts exactly one request per step in arms (b), (c), (c') and (d). A retry is
a second HTTP attempt at the SAME request, not a second request. This client keeps the two
apart: one `Call` record per request, with every transport attempt listed inside it under
"attempts". Count `Call` records for PA.1; count `attempts` to see how the service behaved.

WHAT IS NOT SETTLED HERE. Whether the beta prefix endpoint accepts thinking mode on
deepseek-flash: no page above says. `send` does not drop thinking to make a request
succeed; it returns the service's own words, because a run made under a different thinking
setting is a different arm. See clients/README.md.
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

BASE = "https://api.deepseek.com"
BASE_BETA = "https://api.deepseek.com/beta"
PATH = "/chat/completions"
URL = BASE + PATH
URL_BETA = BASE_BETA + PATH

MODEL = "deepseek-flash"
EFFORT = "high"
MAX_TOKENS = 393216              # the documented maximum, 384K
MAX_WORKERS = 5                  # W10 section 2, and the task for A6
KEY_ENV = "DEEPSEEK_API_KEY"
TIMEOUT = (30, 1800)             # connect, read
TRIES = 7
DELAY0 = 4.0
DELAY_CAP = 90.0
RETRY_AFTER_CAP = 300.0          # a Retry-After is honoured up to here, above the backoff cap

NO_RETRY = (400, 401, 402, 422)
RETRY_STATUS = (408, 409, 425, 429, 500, 502, 503, 504)

_print_lock = threading.Lock()
SENDS = 0                        # live HTTP attempts made by this process; --dry asserts 0


class DeepSeekError(RuntimeError):
    """A request that did not come back as a reply. `retryable` says whether trying again
    could help; `status` and `body` carry the service's own words, unedited."""

    def __init__(self, message, status=None, body="", retryable=False, tag=""):
        super().__init__(message)
        self.status, self.body, self.retryable, self.tag = status, body, retryable, tag


# ---------------------------------------------------------------- the key

def key_from_env(required=True):
    """Read the key from the environment. It is never written to a file by this module,
    never returned inside a record, and never printed."""
    k = os.environ.get(KEY_ENV, "")
    if not k and required:
        raise SystemExit(f"{KEY_ENV} not set. Nothing sent.")
    return k


def assert_no_key(obj, key):
    """Raise if the key appears anywhere in a record about to be handed back or saved.
    The key is only ever put in a header, so this fires on a caller's mistake - a key
    pasted into a prompt, a body, a tag - not on this module's own doing."""
    if not key:
        return obj
    if key in json.dumps(obj, ensure_ascii=False, default=str):
        raise SystemExit("the API key appears in a record. Nothing saved, nothing returned.")
    return obj


# ---------------------------------------------------------------- the request

def prefix_message(content, reasoning_content=None):
    """The last message of a prefix completion: role assistant, prefix true.
    https://api-docs.deepseek.com/guides/chat_prefix_completion/ (CLAIMED, 22 Sep 2026)."""
    m = {"role": "assistant", "content": content, "prefix": True}
    if reasoning_content is not None:
        m["reasoning_content"] = reasoning_content
    return m


def has_prefix(messages):
    return bool(messages) and bool(messages[-1].get("prefix"))


def endpoint_for(messages, base=None):
    """The beta host when the last message is a prefix, the standard host otherwise.
    An explicit base is used as given, and a prefix sent to a non-beta base raises here
    rather than at the service, because the documentation says the feature needs the beta
    base_url to be enabled."""
    if base is None:
        return (BASE_BETA if has_prefix(messages) else BASE) + PATH
    url = base.rstrip("/") + PATH
    if has_prefix(messages) and "/beta" not in base:
        raise ValueError(f"prefix completion needs the beta base ({BASE_BETA}); got {base!r}")
    return url


def build_body(messages, *, model=MODEL, max_tokens=MAX_TOKENS, effort=EFFORT,
               thinking=True, tools=None, stream=True, stop=None, extra=None):
    """The request body. max_tokens defaults to the service's maximum, as the task requires;
    the value is checked against the documented range 1-393216 before anything is sent."""
    if not isinstance(max_tokens, int) or not (1 <= max_tokens <= MAX_TOKENS):
        raise ValueError(f"max_tokens must be an integer in 1..{MAX_TOKENS}; got {max_tokens!r}")
    if effort not in ("none", "low", "high", "max"):
        raise ValueError(f"reasoning_effort must be none/low/high/max; got {effort!r}")
    if stop is not None and len(stop) > 16:
        raise ValueError("at most 16 stop sequences")
    body = {"model": model, "messages": list(messages), "max_tokens": max_tokens,
            "reasoning_effort": effort, "stream": bool(stream)}
    if thinking is not None:
        body["thinking"] = {"type": "enabled" if thinking else "disabled"}
    if stream:
        body["stream_options"] = {"include_usage": True}
    if tools:
        body["tools"] = tools
    if stop:
        body["stop"] = list(stop)
    if extra:
        body.update(extra)
    return body


def request_text(body):
    """The exact bytes that go on the wire, as text. This module serialises the body itself
    and posts the bytes, so that the text saved for PA.1 is the text sent and not a second
    serialisation of the same dict."""
    b = dict(body)
    b.pop("_endpoint", None)
    return json.dumps(b, ensure_ascii=False)


# ---------------------------------------------------------------- the reply

def assemble_stream(lines):
    """Assemble an SSE reply from an iterable of lines (bytes or str).

    Pure: it touches no network, so --dry can run it on canned lines. Skips blank lines and
    comment lines (the service's `: keep-alive` under load). Returns
    (message, finish_reason, usage, raw_lines)."""
    content, reasoning, finish, usage, tcs, raw = [], [], None, {}, {}, []
    for line in lines:
        s = line.decode("utf-8", "ignore") if isinstance(line, (bytes, bytearray)) else line
        if not s.strip():
            continue
        raw.append(s)
        if s.startswith(":"):                      # `: keep-alive`
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
            if d.get("reasoning_content"):
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
    """Assemble a non-streamed reply. The service may send leading empty lines as keep-alive;
    json.loads ignores leading whitespace, so the document parses as it comes."""
    ch = (doc.get("choices") or [{}])[0]
    m = ch.get("message") or {}
    msg = {"content": m.get("content") or "",
           "reasoning_content": m.get("reasoning_content") or "",
           "tool_calls": m.get("tool_calls") or None}
    return msg, ch.get("finish_reason"), doc.get("usage") or {}


# ---------------------------------------------------------------- one request

_SLEEP = time.sleep      # named so the dry run can hold the clock still; never changed live


def _sleep(delay, retry_after):
    # `is not None`, not truthiness: Retry-After: 0 means retry now, and a falsy test would
    # throw that away and wait the backoff instead.
    wait = retry_after if retry_after is not None else delay * (0.75 + 0.5 * random.random())
    _SLEEP(wait)
    return min(delay * 2, DELAY_CAP)


def _retry_after(resp):
    try:
        v = resp.headers.get("Retry-After")
        return min(float(v), RETRY_AFTER_CAP) if v is not None else None
    except (TypeError, ValueError):
        return None


def call(body, key, *, tag="", url=None, stream_path=None, tries=TRIES, timeout=TIMEOUT,
         keep_raw=True, verbose=True):
    """Send one request and return the whole of both sides as a record.

    The record is a dict: the body as sent and its exact text, the endpoint, the headers with
    the key redacted, every transport attempt, the assembled message, the finish reason, the
    usage, and the raw return (the SSE lines, or the whole JSON document) unless keep_raw is
    off. It carries no key. Raises DeepSeekError when no attempt returned a reply."""
    global SENDS
    if requests is None:
        raise SystemExit("the requests package is not installed. Nothing sent.")
    url = url or body.get("_endpoint") or endpoint_for(body.get("messages") or [])
    text = request_text(body)
    payload = text.encode("utf-8")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    stream = bool(body.get("stream"))
    rec = {"client": "clients.deepseek_client", "tag": tag, "url": url,
           "model": body.get("model"), "prefix": has_prefix(body.get("messages") or []),
           "request": {k: v for k, v in body.items() if k != "_endpoint"},
           "request_text": text, "request_bytes": len(payload),
           "headers_sent": {"Authorization": "Bearer <redacted>",
                            "Content-Type": "application/json"},
           "attempts": [], "started_at": _stamp(), "seconds": None,
           "message": None, "finish_reason": None, "usage": {}, "raw": None,
           "http_status": None}
    t0 = time.time()
    delay, last = DELAY0, None
    for n in range(1, tries + 1):
        a = {"n": n, "at": _stamp(), "status": None, "error": None, "seconds": None}
        ta = time.time()
        try:
            SENDS += 1
            r = requests.post(url, data=payload, headers=headers, timeout=timeout, stream=stream)
            a["status"] = r.status_code
            if r.status_code in NO_RETRY:
                a["error"] = r.text[:2000]
                a["seconds"] = round(time.time() - ta, 1)
                rec["attempts"].append(a)
                rec["http_status"] = r.status_code
                rec["seconds"] = round(time.time() - t0, 1)
                rec["finished_at"] = _stamp()
                raise _with_record(
                    DeepSeekError(f"{tag}: HTTP {r.status_code}, not retryable",
                                  status=r.status_code, body=r.text[:4000],
                                  retryable=False, tag=tag), rec, key)
            if r.status_code != 200:
                a["error"] = r.text[:600]
                a["seconds"] = round(time.time() - ta, 1)
                rec["attempts"].append(a)
                last = DeepSeekError(f"{tag}: HTTP {r.status_code}", status=r.status_code,
                                     body=r.text[:4000],
                                     retryable=r.status_code in RETRY_STATUS, tag=tag)
                if r.status_code not in RETRY_STATUS or n == tries:
                    rec["http_status"] = r.status_code
                    rec["seconds"] = round(time.time() - t0, 1)
                    rec["finished_at"] = _stamp()
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
                rec["raw"] = raw if keep_raw else {"stream_lines": len(raw), "saved": stream_path}
            else:
                doc = r.json()
                msg, finish, usage = message_from_json(doc)
                rec["raw"] = doc if keep_raw else {"kept": False}
            a["seconds"] = round(time.time() - ta, 1)
            rec["attempts"].append(a)
            rec.update({"message": msg, "finish_reason": finish, "usage": usage or {},
                        "http_status": 200, "seconds": round(time.time() - t0, 1),
                        "finished_at": _stamp()})
            return assert_no_key(rec, key)
        except DeepSeekError:
            raise
        except Exception as e:                       # transport: reset, timeout, bad chunk
            a["error"] = repr(e)[:600]
            a["seconds"] = round(time.time() - ta, 1)
            rec["attempts"].append(a)
            last = DeepSeekError(f"{tag}: {a['error']}", retryable=True, tag=tag)
            if n == tries:
                break
            _say(f"  {tag}: retry after {a['error']}", verbose)
            delay = _sleep(delay, None)
    rec["seconds"] = round(time.time() - t0, 1)
    rec["finished_at"] = _stamp()
    raise _with_record(last or DeepSeekError(f"{tag}: gave up with no attempt recorded",
                                             tag=tag), rec, key)


def _with_record(err, rec, key):
    """Every failure carries the whole record out with it: the body as sent, every attempt,
    and the service's own words. A failed request is the one whose record is most needed."""
    err.record = assert_no_key(rec, key)
    return err


def send(body, key, tag="", stream_path=None, tries=TRIES):
    """The seam deepseek_transport.py imports: (message, finish_reason, usage, http).

    The caller's body is sent as given. In particular a caller's max_tokens is NOT raised to
    this module's maximum: the record has to show what the caller sent, and a request quietly
    changed underneath a driver is a request the driver's own saved copy does not describe.
    `_endpoint`, if the caller put one there, names the URL and is stripped before sending.

    A caller's ceiling below this client's default is said out loud once per call on stderr,
    so the disagreement between A1's 32000 and A6's 393216 is visible in a live run's log and
    not only in clients/README.md."""
    mt = body.get("max_tokens")
    if isinstance(mt, int) and mt < MAX_TOKENS:
        _say(f"  {tag}: caller's max_tokens {mt} is below the service maximum {MAX_TOKENS}; "
             f"sent as given (clients/README.md, 'One thing for the reviewer')")
    rec = call(body, key, tag=tag, stream_path=stream_path, tries=tries, keep_raw=False)
    http = {"status": rec["http_status"], "attempts": len(rec["attempts"]),
            "url": rec["url"], "seconds": rec["seconds"],
            "stream_lines": (rec["raw"] or {}).get("stream_lines")
            if isinstance(rec["raw"], dict) else None,
            "saved": stream_path}
    return rec["message"], rec["finish_reason"], rec["usage"], http


def _stamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())


def _say(s, verbose=True):
    if verbose:
        with _print_lock:
            print(s, file=sys.stderr, flush=True)


# ---------------------------------------------------------------- the client

class DeepSeekClient:
    """Five worker threads at most, and every request and reply kept whole.

    A job is a dict: {"tag": str, "messages": [...], and any argument of build_body}.
    `many` returns one record per job, in the order the jobs were given, with a failure
    recorded as {"tag":..., "error":..., "record":...} rather than raised, so that one bad
    job does not throw away the replies that did come back."""

    def __init__(self, key=None, *, model=MODEL, max_tokens=MAX_TOKENS, effort=EFFORT,
                 thinking=True, stream=True, workers=MAX_WORKERS, tries=TRIES,
                 timeout=TIMEOUT, base=None, keep_raw=True, verbose=True):
        if workers > MAX_WORKERS:
            raise ValueError(f"at most {MAX_WORKERS} worker threads (W10 section 2: "
                             f"'five DeepSeek agents at a time'); asked for {workers}")
        if workers < 1:
            raise ValueError("at least one worker")
        self.key = key if key is not None else key_from_env(required=False)
        self.model, self.max_tokens, self.effort = model, max_tokens, effort
        self.thinking, self.stream, self.base = thinking, stream, base
        self.workers, self.tries, self.timeout = workers, tries, timeout
        self.keep_raw, self.verbose = keep_raw, verbose

    def body(self, messages, **kw):
        kw.setdefault("model", self.model)
        kw.setdefault("max_tokens", self.max_tokens)
        kw.setdefault("effort", self.effort)
        kw.setdefault("thinking", self.thinking)
        kw.setdefault("stream", self.stream)
        return build_body(messages, **kw)

    def chat(self, messages, *, tag="", stream_path=None, **kw):
        if not self.key:
            raise SystemExit(f"{KEY_ENV} not set. Nothing sent.")
        b = self.body(messages, **kw)
        url = endpoint_for(messages, self.base)
        return call(b, self.key, tag=tag, url=url, stream_path=stream_path,
                    tries=self.tries, timeout=self.timeout, keep_raw=self.keep_raw,
                    verbose=self.verbose)

    def many(self, jobs, *, stream_dir=None):
        jobs = list(jobs)
        out = [None] * len(jobs)

        def one(i, job):
            job = dict(job)
            tag = job.pop("tag", str(i))
            msgs = job.pop("messages")
            sp = os.path.join(stream_dir, f"{tag}.stream.txt") if stream_dir else None
            try:
                return self.chat(msgs, tag=tag, stream_path=sp, **job)
            except DeepSeekError as e:
                return {"tag": tag, "error": str(e), "status": e.status, "body": e.body,
                        "record": getattr(e, "record", None)}

        with cf.ThreadPoolExecutor(max_workers=min(self.workers, max(1, len(jobs)))) as ex:
            futs = {ex.submit(one, i, j): i for i, j in enumerate(jobs)}
            for f in cf.as_completed(futs):
                out[futs[f]] = f.result()
        return out


def cost(usages):
    """The old rig's off-peak arithmetic, kept so two rounds can be compared (plan 49 rig,
    run.py, cost_so_far): cache-hit 0.003, cache-miss 0.15, output 0.6 per million."""
    hit = sum(u.get("prompt_cache_hit_tokens", 0) for u in usages)
    miss = sum(u.get("prompt_cache_miss_tokens", 0) or
               (u.get("prompt_tokens", 0) - u.get("prompt_cache_hit_tokens", 0)) for u in usages)
    out = sum(u.get("completion_tokens", 0) for u in usages)
    return hit, miss, out, hit / 1e6 * 0.003 + miss / 1e6 * 0.15 + out / 1e6 * 0.6


# ---------------------------------------------------------------- the dry run

CANNED = [
    b": keep-alive",
    b"",
    b'data: {"choices":[{"delta":{"reasoning_content":"weigh "}}]}',
    b'data: {"choices":[{"delta":{"reasoning_content":"it"}}]}',
    b'data: {"choices":[{"delta":{"content":"The pole"}}]}',
    b'data: {"choices":[{"delta":{"content":" casts it."}}]}',
    b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"id":"c1","function":'
    b'{"name":"open_","arguments":"{\\"name\\":"}}]}}]}',
    b'data: {"choices":[{"delta":{"tool_calls":[{"index":0,"function":'
    b'{"name":"module","arguments":"\\"reporting\\"}"}}]}}]}',
    b'data: {"choices":[{"finish_reason":"tool_calls"}]}',
    b'data: {"usage":{"prompt_tokens":11,"completion_tokens":7,"total_tokens":18}}',
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
    """A stand-in for the requests module. It reaches no network: it hands back whatever the
    script tells it to, in order, per tag. It exists so that --dry can exercise the retry
    loop, the not-retryable stop and the five threads without sending anything. It also
    records how many requests overlapped, which is how --dry sees the threads work."""

    def __init__(self, script):
        self.script, self.seen, self.lock = script, [], threading.Lock()
        self.inflight, self.peak = 0, 0

    def post(self, url, data=None, headers=None, timeout=None, stream=False):
        with self.lock:
            self.inflight += 1
            self.peak = max(self.peak, self.inflight)
            body = json.loads(data.decode("utf-8"))
            tag = body["messages"][-1]["content"]
            self.seen.append((url, tag, headers.get("Authorization")))
            queue = self.script[tag]
            r = queue.pop(0) if len(queue) > 1 else queue[0]
        time.sleep(0.02)          # the service taking its time, OUTSIDE the stub's own lock,
        with self.lock:           # so workers overlap here when there is more than one
            self.inflight -= 1
        return r


def _stub_checks(check):
    """Run the transport paths against the stub. Holds the clock still so no dry run waits."""
    global requests, _SLEEP, SENDS
    real_requests, real_sleep, sends0 = requests, _SLEEP, SENDS
    waited = []
    good = _StubResponse(200, lines=CANNED)
    script = {
        "fine": [good],
        "flaky": [_StubResponse(429, text="rate", headers={"Retry-After": "0"}), good],
        "bad": [_StubResponse(400, text='{"error":"bad body"}')],
        "plainjson": [_StubResponse(200, doc={
            "choices": [{"message": {"content": "no stream here", "reasoning_content": "r"},
                         "finish_reason": "stop"}],
            "usage": {"total_tokens": 5}})],
    }
    try:
        requests = _StubRequests(script)
        _SLEEP = lambda s: waited.append(s)
        SENDS = 0
        c = DeepSeekClient(key="sk-not-a-real-key", workers=5, verbose=False, keep_raw=True)
        jobs = [{"tag": t, "messages": [{"role": "user", "content": t}]}
                for t in ("fine", "flaky", "bad")]
        out = c.many(jobs)
        check("many: one record per job, in the order given",
              [r.get("tag") for r in out] == ["fine", "flaky", "bad"])
        check("many: the good job carries the assembled reply",
              out[0]["message"]["content"] == "The pole casts it.")
        check("many: the good job is one request with one attempt (PA.1 counts records)",
              len(out[0]["attempts"]) == 1)
        check("many: a 429 is retried and the retry is an attempt, not a second request",
              out[1].get("message") is not None and len(out[1]["attempts"]) == 2,
              f"attempts={len(out[1].get('attempts', []))}")
        check("many: Retry-After was honoured rather than the backoff", waited == [0.0], str(waited))
        check("many: a 400 stops at once and is returned, not raised",
              out[2].get("error") and out[2].get("status") == 400
              and len(out[2]["record"]["attempts"]) == 1)
        check("many: the service's own words are kept unedited",
              out[2]["body"] == '{"error":"bad body"}')
        check("the record keeps the request and the reply whole",
              out[0]["request"]["messages"][-1]["content"] == "fine"
              and out[0]["raw"] == [s.decode() for s in CANNED if s.strip()])
        check("the key went in the header and in no record",
              requests.seen[0][2] == "Bearer sk-not-a-real-key"
              and "sk-not-a-real-key" not in json.dumps(out, default=str))
        check("SENDS counted every attempt", SENDS == 4, f"SENDS={SENDS}")
        ns = c.chat([{"role": "user", "content": "plainjson"}], tag="ns", stream=False)
        check("the non-streamed path assembles the reply and keeps the whole document",
              ns["message"]["content"] == "no stream here" and ns["finish_reason"] == "stop"
              and ns["raw"]["usage"]["total_tokens"] == 5)
        # The five threads: the same five jobs run at five workers and at one, because a
        # check that comes out the same either way measures nothing.
        def five_jobs(workers):
            global requests
            requests = _StubRequests({f"j{i}": [_StubResponse(200, lines=CANNED)]
                                      for i in range(5)})
            cc = DeepSeekClient(key="sk-not-a-real-key", workers=workers, verbose=False)
            cc.many([{"tag": f"j{i}", "messages": [{"role": "user", "content": f"j{i}"}]}
                     for i in range(5)])
            return requests.peak

        peak5, peak1 = five_jobs(5), five_jobs(1)
        check("five workers run five jobs at once", peak5 == 5, f"peak={peak5}")
        check("the control: one worker runs them one at a time", peak1 == 1, f"peak={peak1}")

        requests = _StubRequests(script)
        script["fine"] = [good]
        m, fin, us, http = send({"model": MODEL, "stream": True,
                                 "messages": [{"role": "user", "content": "fine"}]},
                                "sk-not-a-real-key", tag="seam")
        check("send() returns the four values deepseek_transport.py unpacks",
              m["content"] == "The pole casts it." and fin == "tool_calls"
              and us["total_tokens"] == 18 and http["status"] == 200)
    finally:
        requests, _SLEEP, SENDS = real_requests, real_sleep, sends0


def _dry(save_dir=None):
    ok, fail = [], []

    def check(name, cond, note=""):
        (ok if cond else fail).append(f"{name}{(' - ' + note) if note else ''}")

    msgs = [{"role": "system", "content": "the method"}, {"role": "user", "content": "the document"}]
    plain = build_body(msgs)
    check("plain body: max_tokens is the service maximum",
          plain["max_tokens"] == MAX_TOKENS == 393216, str(plain["max_tokens"]))
    check("plain body: thinking enabled, effort high",
          plain["thinking"] == {"type": "enabled"} and plain["reasoning_effort"] == "high")
    check("plain body: endpoint is the standard host",
          endpoint_for(msgs) == URL, endpoint_for(msgs))

    pmsgs = msgs + [prefix_message("## 1. The question, frozen\n")]
    pbody = build_body(pmsgs, stop=["\n## 8."])
    check("prefix body: last message is assistant with prefix true",
          pbody["messages"][-1]["role"] == "assistant" and pbody["messages"][-1]["prefix"] is True)
    check("prefix body: endpoint is the beta host",
          endpoint_for(pmsgs) == URL_BETA, endpoint_for(pmsgs))
    check("prefix against a non-beta base raises", _raises(lambda: endpoint_for(pmsgs, BASE)))

    tool = [{"type": "function", "function": {"name": "open_module", "parameters": {}}}]
    tbody = build_body(msgs, tools=tool, stream=False)
    check("tool body: tools carried, no stream_options when not streaming",
          tbody["tools"] == tool and "stream_options" not in tbody)

    check("max_tokens above the maximum raises",
          _raises(lambda: build_body(msgs, max_tokens=MAX_TOKENS + 1)))
    check("max_tokens of zero raises", _raises(lambda: build_body(msgs, max_tokens=0)))
    check("an unknown effort raises", _raises(lambda: build_body(msgs, effort="medium")))
    check("more than five workers raises",
          _raises(lambda: DeepSeekClient(key="x", workers=6)))
    check("five workers is allowed", DeepSeekClient(key="x", workers=5).workers == 5)

    m, fin, us, raw = assemble_stream(CANNED)
    check("stream: content assembled", m["content"] == "The pole casts it.", repr(m["content"]))
    check("stream: reasoning assembled", m["reasoning_content"] == "weigh it")
    check("stream: tool call assembled across chunks",
          m["tool_calls"] and m["tool_calls"][0]["function"]["name"] == "open_module"
          and m["tool_calls"][0]["function"]["arguments"] == '{"name":"reporting"}',
          json.dumps(m["tool_calls"]))
    check("stream: finish reason and usage read", fin == "tool_calls" and us["total_tokens"] == 18)
    check("stream: keep-alive comment and blank line skipped, raw kept",
          len(raw) == len(CANNED) - 1)

    doc = {"choices": [{"message": {"content": "hi", "reasoning_content": "r"},
                        "finish_reason": "stop"}], "usage": {"total_tokens": 3}}
    m2, f2, u2 = message_from_json(doc)
    check("non-stream: message read", m2["content"] == "hi" and f2 == "stop" and u2["total_tokens"] == 3)

    check("the request text is the bytes sent",
          request_text(plain) == json.dumps({k: v for k, v in plain.items()
                                             if k != "_endpoint"}, ensure_ascii=False))
    check("assert_no_key fires on a key in a record",
          _raises(lambda: assert_no_key({"body": "sk-secret"}, "sk-secret"), SystemExit))
    check("assert_no_key passes a clean record", assert_no_key({"body": "clean"}, "sk-secret") is not None)
    _stub_checks(check)

    check("no key needed to build anything; key not in environment now",
          not os.environ.get(KEY_ENV), "set" if os.environ.get(KEY_ENV) else "unset")
    check("nothing was sent to any address", SENDS == 0, f"SENDS={SENDS}")

    print("dry run of clients/deepseek_client.py - sends nothing\n")
    for line in ok:
        print("  ok    " + line)
    for line in fail:
        print("  FAIL  " + line)
    print(f"\nendpoints: plain {URL}\n           prefix {URL_BETA}")
    print(f"model {MODEL}, effort {EFFORT}, max_tokens {MAX_TOKENS}, workers at most {MAX_WORKERS}")
    print(f"key: read from {KEY_ENV} at call time; "
          f"{'present' if os.environ.get(KEY_ENV) else 'not present'} in this environment")
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        for name, b in (("plain", plain), ("prefix", pbody), ("tools", tbody)):
            p = os.path.join(save_dir, f"deepseek.{name}.request.json")
            with open(p, "w", encoding="utf-8") as f:
                f.write(request_text(b))
            print(f"  wrote {p} ({len(request_text(b))} characters, no key in it)")
    print(f"\n{len(ok)} checks passed, {len(fail)} failed. Nothing sent.")
    return 1 if fail else 0


def _raises(fn, kind=Exception):
    try:
        fn()
    except kind:
        return True
    except Exception:
        return False
    return False


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="DeepSeek V4.1 Flash client for plan W10.")
    ap.add_argument("--dry", action="store_true",
                    help="build every request shape, parse a canned stream, send nothing")
    ap.add_argument("--save", metavar="DIR", default=None,
                    help="with --dry, write each request text to DIR")
    args = ap.parse_args()
    if not args.dry:
        raise SystemExit("this file is a library; the only command it runs is --dry. "
                         "Nothing sent.")
    sys.exit(_dry(args.save))
