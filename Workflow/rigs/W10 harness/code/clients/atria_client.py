"""The Atria Asi client for plan W10, stage A, task A6.

A LIBRARY. Nothing is sent on import. `--dry` sends nothing at all.

  python3 atria_client.py --dry                 # builds every request shape, sends nothing
  python3 atria_client.py --dry --save DIR      # and writes each request text to DIR

The key is read from ATRIA_API_KEY. It goes in one place, the Authorization header of a live
request, and in no other: no record this file returns contains it, and `assert_no_key` is run
over every record before it is handed back.

WHAT ATRIA ASI IS, AS FAR AS THE WEB SAYS (all of this is CLAIMED; read 22 September 2026)

  https://api.atria-asi.ai/docs - the model page's own integration documentation.
    Base URL "https://api.atria-asi.ai/v1". Model ID "Atria-Dawn-Preview" (case-sensitive).
    Context window 256K. Three interfaces: Chat Completions "/v1/chat/completions"
    (OpenAI-compatible, `messages`), Messages "/v1/messages" (Anthropic-compatible,
    `x-api-key`), Responses "/v1/responses" (`input`). Authentication
    "Authorization: Bearer <ATRIA_API_KEY>"; the key is set as an environment variable and
    the page's own line is `export ATRIA_API_KEY=atr_xxx`, so the key prefix is "atr_".
    Output length: chat completions takes "max_completion_tokens" or "max_tokens", and the
    page's sentence is "接受 1-65,536 的整数，用于限制本次生成长度" - accepts an integer from
    1 to 65,536, to limit the length of this generation. Rate limit: the response carries
    "x-rpm-limit: 60" and "x-rpm-remaining"; over the limit the service returns 429 with a
    "Retry-After" header giving the seconds to wait. Errors listed: 401 "API Key 无效或已吊销"
    (invalid or revoked key), 429 "请求频率过高或额度不足" (too frequent, or out of quota),
    5xx "服务暂时不可用，请稍后重试" (temporarily unavailable, retry later). Streaming:
    "流式响应使用 SSE" - SSE, read line by line, concatenating until "[DONE]". Text only:
    images and PDFs are refused with a "not a multimodal model" error. Reply paths:
    chat completions `choices[0].message.content`, `usage.prompt_tokens` /
    `completion_tokens`, stream delta `choices[0].delta.content`. The page's curl sample:
      curl -X POST https://api.atria-asi.ai/v1/chat/completions \\
        -H "Authorization: Bearer $ATRIA_API_KEY" -H "Content-Type: application/json" \\
        -d '{"model": "Atria-Dawn-Preview", "messages": [{"role": "user", "content": "hi"}]}'
  https://github.com/atria-asi/Atria-Dawn-Preview - the model's repository.
    "max_output_size = 65536"; max context 256,000; a client config listing efforts
    ["low", "medium", "high", "xhigh", "max"] with default "max", and "thinking" as the
    capability that turns reasoning on. That config is a client's, not the HTTP API's.
  https://llmgateway.io/providers/atria - a gateway's listing. Model id
    "atria-dawn-preview"; "an OpenAI-compatible inference API"; context 262.1k; supports
    streaming, tools and reasoning; provider headquarters CN.
  https://huggingface.co/internlm/Atria-Dawn-Preview - the weights. 256K context, text only.
  Search result, https://api.atria-asi.ai/ (the model page): "Atria Dawn Preview is a
    preview version of a new-generation agentic model developed by the Shanghai Artificial
    Intelligence Laboratory, trained on a 744B-parameter MoE foundation model".

  So: Atria Asi is a hosted agentic model with an OpenAI-compatible chat endpoint. The base
  URL was found, so ATRIA_BASE_URL is an override here and not a requirement. What is still
  unknown is listed in clients/README.md, as the task for A6 asks; the short of it is that
  the page says nothing about a default max_tokens, about reasoning_effort on the HTTP API,
  or about a reasoning field in the reply.

THE OWNER'S TWO RULES, AND HOW THEY ARE KEPT
  "Only 1 at a time." A module-level lock is held across the whole exchange, the streamed
    read included, so a request counts as in flight until its reply is complete. The lock is
    in this file rather than in the caller, because a caller that forgets is exactly the
    failure the rule is against. `each()` runs a list in sequence; there is no `many()`.
  "Make its token ceilings significantly larger because it tends to fail otherwise."
    MAX_TOKENS = 65536, the documented maximum, is the default, and the ceiling is a
    parameter on the client and on every call. The gauge on that decision: every record
    carries "truncated", true when the service's finish reason is "length". If the owner's
    failure is truncation, a ceiling at the maximum should drive that count to zero; if
    "truncated" is still true at 65,536, the ceiling was not the cause and the read-me's
    question for the owner is the live one.

WHAT IS NOT SENT, AND WHY. No reasoning_effort, no thinking object: the documentation at
the addresses above does not say the HTTP API takes either, and an undocumented parameter is
a way to earn a 400 on every call. The effort list above belongs to a client config. Pass
`extra={"reasoning_effort": "max"}` when a live call has shown the service accepts it, and
record that it did.

RETRIES AND PA.1. As in deepseek_client.py: one record per request, every transport attempt
listed inside it under "attempts". Count records for PA.1; count attempts to see the service.

TWO THINGS THE DOCUMENTATION SETTLES AGAINST THIS CLIENT, AND ARE LEFT AS THEY ARE.
  A 429 here means either "too frequent" or "out of quota" - the page's own line covers both.
    This client retries a 429, which is useless when the quota is gone. It is kept because
    the two cannot be told apart without reading the body, and the body is in the record, so
    a reader can see which it was. The cost is at most seven attempts against a dead quota.
  Streaming is on by default. The reason is carried over from the DeepSeek rig, not tested
    here: plan 49 rig, run.py, "Streaming captures partial output and the finish reason even
    when the service ends early." That is fitted on another service. Atria's page says SSE is
    supported and says nothing about partial output. Pass stream=False to test the other way.
"""
import argparse
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

BASE = os.environ.get("ATRIA_BASE_URL", "https://api.atria-asi.ai/v1")
PATH = "/chat/completions"
MODEL = os.environ.get("ATRIA_MODEL", "Atria-Dawn-Preview")
MAX_TOKENS = 65536               # the documented maximum, and the default here
KEY_ENV = "ATRIA_API_KEY"
KEY_PREFIX = "atr_"
RPM = 60                         # x-rpm-limit, as the documentation shows it
TIMEOUT = (30, 1800)             # connect, read
TRIES = 7
DELAY0 = 4.0
DELAY_CAP = 120.0
RETRY_AFTER_CAP = 300.0          # a Retry-After is honoured up to here, above the backoff cap

NO_RETRY = (400, 401, 403, 404, 422)
RETRY_STATUS = (408, 409, 425, 429, 500, 502, 503, 504)

ONE_AT_A_TIME = threading.Lock()     # the owner's rule, kept here and not in the caller
_print_lock = threading.Lock()
_SLEEP = time.sleep                  # named so the dry run can hold the clock still
SENDS = 0                            # live HTTP attempts made by this process; --dry asserts 0


class AtriaError(RuntimeError):
    """A request that did not come back as a reply. `retryable` says whether trying again
    could help; `status` and `body` carry the service's own words, unedited."""

    def __init__(self, message, status=None, body="", retryable=False, tag=""):
        super().__init__(message)
        self.status, self.body, self.retryable, self.tag = status, body, retryable, tag


def key_from_env(required=True):
    """Read the key from the environment. Never written to a file, never returned inside a
    record, never printed. A key that does not start with atr_ is not refused - the prefix is
    what the documentation shows, not a rule the service is known to enforce - but it is
    reported by --dry so a pasted wrong key is seen before a run, not after."""
    k = os.environ.get(KEY_ENV, "")
    if not k and required:
        raise SystemExit(f"{KEY_ENV} not set. Nothing sent.")
    return k


def assert_no_key(obj, key):
    if not key:
        return obj
    if key in json.dumps(obj, ensure_ascii=False, default=str):
        raise SystemExit("the API key appears in a record. Nothing saved, nothing returned.")
    return obj


def endpoint(base=None):
    return (base or BASE).rstrip("/") + PATH


def build_body(messages, *, model=MODEL, max_tokens=MAX_TOKENS, stream=True,
               temperature=None, top_p=None, tools=None, stop=None, extra=None):
    """The request body. max_tokens defaults to the documented maximum and is checked against
    the documented range 1-65,536 before anything is sent. Nothing undocumented is added."""
    if not isinstance(max_tokens, int) or not (1 <= max_tokens <= MAX_TOKENS):
        raise ValueError(f"max_tokens must be an integer in 1..{MAX_TOKENS}; got {max_tokens!r}")
    body = {"model": model, "messages": list(messages), "max_tokens": max_tokens,
            "stream": bool(stream)}
    if stream:
        body["stream_options"] = {"include_usage": True}
    if temperature is not None:
        body["temperature"] = temperature
    if top_p is not None:
        body["top_p"] = top_p
    if tools:
        body["tools"] = tools
    if stop:
        body["stop"] = list(stop)
    if extra:
        body.update(extra)
    return body


def request_text(body):
    """The exact bytes that go on the wire, as text: this module serialises the body itself
    and posts those bytes, so the text saved is the text sent."""
    b = dict(body)
    b.pop("_endpoint", None)
    return json.dumps(b, ensure_ascii=False)


def assemble_stream(lines):
    """Assemble an SSE reply from an iterable of lines (bytes or str). Pure: no network, so
    --dry can run it on canned lines. Blank lines and comment lines are skipped. Any
    reasoning field the service happens to send is collected under whichever of the two
    names it uses, since the documentation names neither; the raw lines are kept either way.
    Returns (message, finish_reason, usage, raw_lines)."""
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
            for name in ("reasoning_content", "reasoning"):
                if isinstance(d.get(name), str) and d[name]:
                    reasoning.append(d[name])
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
    """Assemble a non-streamed reply: choices[0].message.content, as the documentation's own
    reply-path line has it."""
    ch = (doc.get("choices") or [{}])[0]
    m = ch.get("message") or {}
    reasoning = m.get("reasoning_content") or m.get("reasoning") or ""
    msg = {"content": m.get("content") or "",
           "reasoning_content": reasoning if isinstance(reasoning, str) else json.dumps(reasoning),
           "tool_calls": m.get("tool_calls") or None}
    return msg, ch.get("finish_reason"), doc.get("usage") or {}


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


def _rpm(resp):
    out = {}
    for h in ("x-rpm-limit", "x-rpm-remaining"):
        try:
            v = resp.headers.get(h)
        except Exception:
            v = None
        if v is not None:
            out[h] = v
    return out


def call(body, key, *, tag="", url=None, stream_path=None, tries=TRIES, timeout=TIMEOUT,
         keep_raw=True, verbose=True):
    """Send one request, one at a time, and return the whole of both sides as a record.

    The lock is taken for the whole exchange, the streamed read included, so only one Atria
    request is ever in flight from this process. The record carries the body as sent and its
    exact text, the endpoint, the headers with the key redacted, every attempt, the rate-limit
    headers the service returned, the assembled message, the finish reason, the usage, the raw
    return, and `truncated` (the gauge on the ceiling). It carries no key."""
    global SENDS
    if requests is None:
        raise SystemExit("the requests package is not installed. Nothing sent.")
    url = url or body.get("_endpoint") or endpoint()
    text = request_text(body)
    payload = text.encode("utf-8")
    headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
    stream = bool(body.get("stream"))
    rec = {"client": "clients.atria_client", "tag": tag, "url": url,
           "model": body.get("model"), "max_tokens": body.get("max_tokens"),
           "one_at_a_time": True,
           "request": {k: v for k, v in body.items() if k != "_endpoint"},
           "request_text": text, "request_bytes": len(payload),
           "headers_sent": {"Authorization": "Bearer <redacted>",
                            "Content-Type": "application/json"},
           "attempts": [], "rate_headers": {}, "started_at": _stamp(), "seconds": None,
           "message": None, "finish_reason": None, "usage": {}, "raw": None,
           "http_status": None, "truncated": None}
    t0 = time.time()
    delay, last = DELAY0, None
    with ONE_AT_A_TIME:
        for n in range(1, tries + 1):
            a = {"n": n, "at": _stamp(), "status": None, "error": None, "seconds": None}
            ta = time.time()
            try:
                SENDS += 1
                r = requests.post(url, data=payload, headers=headers, timeout=timeout,
                                  stream=stream)
                a["status"] = r.status_code
                rec["rate_headers"] = _rpm(r) or rec["rate_headers"]
                if r.status_code in NO_RETRY:
                    a["error"] = r.text[:2000]
                    a["seconds"] = round(time.time() - ta, 1)
                    rec["attempts"].append(a)
                    rec.update({"http_status": r.status_code,
                                "seconds": round(time.time() - t0, 1), "finished_at": _stamp()})
                    raise _with_record(
                        AtriaError(f"{tag}: HTTP {r.status_code}, not retryable",
                                   status=r.status_code, body=r.text[:4000],
                                   retryable=False, tag=tag), rec, key)
                if r.status_code != 200:
                    a["error"] = r.text[:600]
                    a["seconds"] = round(time.time() - ta, 1)
                    rec["attempts"].append(a)
                    last = AtriaError(f"{tag}: HTTP {r.status_code}", status=r.status_code,
                                      body=r.text[:4000],
                                      retryable=r.status_code in RETRY_STATUS, tag=tag)
                    if r.status_code not in RETRY_STATUS or n == tries:
                        rec.update({"http_status": r.status_code,
                                    "seconds": round(time.time() - t0, 1),
                                    "finished_at": _stamp()})
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
                rec.update({"message": msg, "finish_reason": finish, "usage": usage or {},
                            "http_status": 200, "truncated": finish == "length",
                            "seconds": round(time.time() - t0, 1), "finished_at": _stamp()})
                if rec["truncated"]:
                    _say(f"  {tag}: finish reason 'length' at max_tokens "
                         f"{body.get('max_tokens')}: the reply is cut off", verbose)
                return assert_no_key(rec, key)
            except AtriaError:
                raise
            except Exception as e:
                a["error"] = repr(e)[:600]
                a["seconds"] = round(time.time() - ta, 1)
                rec["attempts"].append(a)
                last = AtriaError(f"{tag}: {a['error']}", retryable=True, tag=tag)
                if n == tries:
                    break
                _say(f"  {tag}: retry after {a['error']}", verbose)
                delay = _sleep(delay, None)
        rec["seconds"] = round(time.time() - t0, 1)
        rec["finished_at"] = _stamp()
        raise _with_record(last or AtriaError(f"{tag}: gave up with no attempt recorded",
                                              tag=tag), rec, key)


def _with_record(err, rec, key):
    """Every failure carries the whole record out with it. A failed request is the one whose
    record is most needed - and with Atria it is the one the owner's rule is about."""
    err.record = assert_no_key(rec, key)
    return err


def send(body, key, tag="", stream_path=None, tries=TRIES):
    """The same seam shape as clients/deepseek_client.send, so a driver can hold either:
    (message, finish_reason, usage, http). The caller's body is sent as given."""
    rec = call(body, key, tag=tag, stream_path=stream_path, tries=tries, keep_raw=False)
    http = {"status": rec["http_status"], "attempts": len(rec["attempts"]),
            "url": rec["url"], "seconds": rec["seconds"], "truncated": rec["truncated"],
            "rate_headers": rec["rate_headers"],
            "stream_lines": (rec["raw"] or {}).get("stream_lines")
            if isinstance(rec["raw"], dict) else None,
            "saved": stream_path}
    return rec["message"], rec["finish_reason"], rec["usage"], http


class AtriaClient:
    """One request at a time, a ceiling at the service's maximum, and both sides kept whole.

    There is no `many`: the owner's rule is one at a time, so the only list method is
    `each`, which runs jobs in sequence and returns one record per job in the order given.
    A failure is returned as {"tag":..., "error":..., "record":...} rather than raised, so
    one bad job does not throw away the replies that did come back."""

    def __init__(self, key=None, *, model=MODEL, max_tokens=MAX_TOKENS, stream=True,
                 base=None, tries=TRIES, timeout=TIMEOUT, keep_raw=True, verbose=True,
                 min_gap=0.0):
        # min_gap does nothing at the documented 60 requests a minute: one at a time, an
        # agentic model cannot reach 60 replies in a minute. It is here for the case the
        # documentation leaves open (read-me question 6): an account whose real cap is lower.
        self.key = key if key is not None else key_from_env(required=False)
        self.model, self.max_tokens, self.stream = model, max_tokens, stream
        self.base, self.tries, self.timeout = base, tries, timeout
        self.keep_raw, self.verbose, self.min_gap = keep_raw, verbose, min_gap
        self._last = 0.0

    def body(self, messages, **kw):
        kw.setdefault("model", self.model)
        kw.setdefault("max_tokens", self.max_tokens)
        kw.setdefault("stream", self.stream)
        return build_body(messages, **kw)

    def chat(self, messages, *, tag="", stream_path=None, **kw):
        if not self.key:
            raise SystemExit(f"{KEY_ENV} not set. Nothing sent.")
        gap = self.min_gap - (time.time() - self._last)
        if self.min_gap and gap > 0:
            _SLEEP(gap)
        b = self.body(messages, **kw)
        try:
            return call(b, self.key, tag=tag, url=endpoint(self.base), stream_path=stream_path,
                        tries=self.tries, timeout=self.timeout, keep_raw=self.keep_raw,
                        verbose=self.verbose)
        finally:
            self._last = time.time()

    def each(self, jobs, *, stream_dir=None):
        out = []
        for i, job in enumerate(list(jobs)):
            job = dict(job)
            tag = job.pop("tag", str(i))
            msgs = job.pop("messages")
            sp = os.path.join(stream_dir, f"{tag}.stream.txt") if stream_dir else None
            try:
                out.append(self.chat(msgs, tag=tag, stream_path=sp, **job))
            except AtriaError as e:
                out.append({"tag": tag, "error": str(e), "status": e.status, "body": e.body,
                            "record": getattr(e, "record", None)})
        return out


# ---------------------------------------------------------------- the dry run

CANNED = [
    b": ping",
    b"",
    b'data: {"choices":[{"delta":{"reasoning_content":"think "}}]}',
    b'data: {"choices":[{"delta":{"content":"A held part"}}]}',
    b'data: {"choices":[{"delta":{"content":" carries its reason."}}]}',
    b'data: {"choices":[{"finish_reason":"stop"}]}',
    b'data: {"usage":{"prompt_tokens":9,"completion_tokens":6,"total_tokens":15}}',
    b"data: [DONE]",
]
CANNED_CUT = [
    b'data: {"choices":[{"delta":{"content":"half a rep"}}]}',
    b'data: {"choices":[{"finish_reason":"length"}]}',
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
    requests were in flight at once, which is how --dry checks the one-at-a-time rule."""

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
            q = self.script[tag]
            r = q.pop(0) if len(q) > 1 else q[0]
        time.sleep(0.02)          # the service taking its time, OUTSIDE the stub's own lock,
        with self.lock:           # so two callers overlap here if nothing else stops them
            self.inflight -= 1
        return r


def _stub_checks(check):
    global requests, _SLEEP, SENDS
    real_requests, real_sleep, sends0 = requests, _SLEEP, SENDS
    waited = []
    good = _StubResponse(200, lines=CANNED, headers={"x-rpm-limit": "60",
                                                     "x-rpm-remaining": "59"})
    script = {
        "fine": [good],
        "busy": [_StubResponse(429, text="slow down", headers={"Retry-After": "0"}), good],
        "cut": [_StubResponse(200, lines=CANNED_CUT)],
        "nokey": [_StubResponse(401, text='{"error":"API Key invalid"}')],
        "plainjson": [_StubResponse(200, doc={
            "choices": [{"message": {"content": "no stream here"}, "finish_reason": "stop"}],
            "usage": {"total_tokens": 5}})],
    }
    try:
        requests = _StubRequests(script)
        _SLEEP = lambda s: waited.append(s)
        SENDS = 0
        c = AtriaClient(key="atr_not-a-real-key", verbose=False, keep_raw=True)
        jobs = [{"tag": t, "messages": [{"role": "user", "content": t}]}
                for t in ("fine", "busy", "cut", "nokey")]
        out = c.each(jobs)
        check("each: one record per job, in the order given",
              [r.get("tag") for r in out] == ["fine", "busy", "cut", "nokey"])
        check("each: the good job carries the assembled reply",
              out[0]["message"]["content"] == "A held part carries its reason.")
        check("each: the rate-limit headers are kept",
              out[0]["rate_headers"] == {"x-rpm-limit": "60", "x-rpm-remaining": "59"})
        check("each: max_tokens sent is the documented maximum",
              out[0]["request"]["max_tokens"] == MAX_TOKENS == 65536)
        check("each: a 429 is retried, and the retry is an attempt, not a second request",
              out[1].get("message") is not None and len(out[1]["attempts"]) == 2)
        check("each: Retry-After was honoured rather than the backoff", waited == [0.0], str(waited))
        check("the truncation gauge fires on finish reason 'length'",
              out[2]["truncated"] is True and out[0]["truncated"] is False)
        check("each: a 401 stops at once, is returned, and keeps its record",
              out[3].get("status") == 401 and out[3]["record"]["attempts"][0]["status"] == 401)
        check("each: the service's own words are kept unedited",
              out[3]["body"] == '{"error":"API Key invalid"}')
        check("the record keeps the request and the reply whole",
              out[0]["request"]["messages"][-1]["content"] == "fine"
              and out[0]["raw"] == [s.decode() for s in CANNED if s.strip()])
        check("the key went in the header and in no record",
              requests.seen[0][2] == "Bearer atr_not-a-real-key"
              and "atr_not-a-real-key" not in json.dumps(out, default=str))
        check("only one request was ever in flight", requests.peak == 1,
              f"peak={requests.peak}")
        ns = c.chat([{"role": "user", "content": "plainjson"}], tag="ns", stream=False)
        check("the non-streamed path assembles the reply and keeps the whole document",
              ns["message"]["content"] == "no stream here" and ns["finish_reason"] == "stop"
              and ns["raw"]["usage"]["total_tokens"] == 5 and ns["truncated"] is False)

        # Five threads all calling at once: the lock in this file, not the caller, must keep
        # it to one. The same run is made twice, once with the lock and once with it taken
        # out, because a check that passes either way measures nothing.
        def hammer_five():
            global requests
            requests = _StubRequests({"t": [_StubResponse(200, lines=CANNED)]})
            errs = []

            def one(i):
                try:
                    c.chat([{"role": "user", "content": "t"}], tag=f"t{i}")
                except Exception as e:
                    errs.append(repr(e))

            ths = [threading.Thread(target=one, args=(i,)) for i in range(5)]
            for t in ths:
                t.start()
            for t in ths:
                t.join()
            return requests.peak, errs

        peak_with, errs = hammer_five()
        check("five callers at once are still served one at a time",
              peak_with == 1 and not errs, f"peak={peak_with} {errs}")

        class _NoLock:
            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        global ONE_AT_A_TIME
        real_lock = ONE_AT_A_TIME
        try:
            ONE_AT_A_TIME = _NoLock()
            peak_without, _ = hammer_five()
        finally:
            ONE_AT_A_TIME = real_lock
        check("the control: with the lock taken out, the same check fails",
              peak_without > 1, f"peak without the lock = {peak_without}; if this is 1 the "
                                f"one-at-a-time check above is measuring nothing")

        m, fin, us, http = send({"model": MODEL, "stream": True, "max_tokens": MAX_TOKENS,
                                 "messages": [{"role": "user", "content": "t"}]},
                                "atr_not-a-real-key", tag="seam")
        check("send() returns the four values a driver unpacks",
              m["content"] == "A held part carries its reason." and fin == "stop"
              and us["total_tokens"] == 15 and http["status"] == 200
              and http["truncated"] is False)
    finally:
        requests, _SLEEP, SENDS = real_requests, real_sleep, sends0


def _raises(fn, kind=Exception):
    try:
        fn()
    except kind:
        return True
    except Exception:
        return False
    return False


def _dry(save_dir=None):
    ok, fail = [], []

    def check(name, cond, note=""):
        (ok if cond else fail).append(f"{name}{(' - ' + note) if note else ''}")

    msgs = [{"role": "system", "content": "the method"},
            {"role": "user", "content": "the analysis"}]
    b = build_body(msgs)
    check("body: max_tokens is the documented maximum", b["max_tokens"] == 65536,
          str(b["max_tokens"]))
    check("body: the model id is the case-sensitive one", b["model"] == "Atria-Dawn-Preview",
          b["model"])
    check("body: nothing undocumented is sent",
          set(b) == {"model", "messages", "max_tokens", "stream", "stream_options"},
          ", ".join(sorted(b)))
    check("body: the ceiling is a parameter", build_body(msgs, max_tokens=8192)["max_tokens"] == 8192)
    check("body: a ceiling above the maximum raises",
          _raises(lambda: build_body(msgs, max_tokens=MAX_TOKENS + 1)))
    check("body: a ceiling of zero raises", _raises(lambda: build_body(msgs, max_tokens=0)))
    check("body: extra carries an undocumented field only when asked",
          build_body(msgs, extra={"reasoning_effort": "max"})["reasoning_effort"] == "max")
    check("endpoint is the documented one", endpoint() == "https://api.atria-asi.ai/v1/chat/completions",
          endpoint())
    check("ATRIA_BASE_URL overrides the endpoint",
          endpoint("https://example.invalid/v9") == "https://example.invalid/v9/chat/completions")

    m, fin, us, raw = assemble_stream(CANNED)
    check("stream: content assembled", m["content"] == "A held part carries its reason.")
    check("stream: any reasoning field is kept", m["reasoning_content"] == "think ")
    check("stream: finish reason and usage read", fin == "stop" and us["total_tokens"] == 15)
    check("stream: comment and blank lines skipped, raw kept", len(raw) == len(CANNED) - 1)
    doc = {"choices": [{"message": {"content": "hi"}, "finish_reason": "stop"}],
           "usage": {"total_tokens": 3}}
    m2, f2, u2 = message_from_json(doc)
    check("non-stream: choices[0].message.content read", m2["content"] == "hi" and f2 == "stop")

    check("the request text is the bytes sent",
          request_text(b) == json.dumps(b, ensure_ascii=False))
    check("assert_no_key fires on a key in a record",
          _raises(lambda: assert_no_key({"p": "atr_secret"}, "atr_secret"), SystemExit))

    _stub_checks(check)

    k = os.environ.get(KEY_ENV, "")
    check("no key needed to build anything; key not in environment now", not k,
          "set" if k else "unset")
    if k:
        check(f"the key in the environment starts with {KEY_PREFIX!r}", k.startswith(KEY_PREFIX),
              "it does not; check it was pasted whole")
    check("nothing was sent to any address", SENDS == 0, f"SENDS={SENDS}")

    print("dry run of clients/atria_client.py - sends nothing\n")
    for line in ok:
        print("  ok    " + line)
    for line in fail:
        print("  FAIL  " + line)
    print(f"\nendpoint  {endpoint()}   (override with ATRIA_BASE_URL)")
    print(f"model     {MODEL}   (override with ATRIA_MODEL)")
    print(f"ceiling   max_tokens {MAX_TOKENS}, the documented maximum; a parameter everywhere")
    print(f"threads   one at a time, held by a lock in this file; documented limit {RPM} rpm")
    print(f"key       read from {KEY_ENV} at call time; "
          f"{'present' if k else 'not present'} in this environment")
    if save_dir:
        os.makedirs(save_dir, exist_ok=True)
        for name, body in (("plain", b), ("small", build_body(msgs, max_tokens=8192)),
                           ("tools", build_body(msgs, tools=[{"type": "function",
                                                              "function": {"name": "open_module",
                                                                           "parameters": {}}}]))):
            p = os.path.join(save_dir, f"atria.{name}.request.json")
            with open(p, "w", encoding="utf-8") as f:
                f.write(request_text(body))
            print(f"  wrote {p} ({len(request_text(body))} characters, no key in it)")
    print(f"\n{len(ok)} checks passed, {len(fail)} failed. Nothing sent.")
    return 1 if fail else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Atria Asi client for plan W10.")
    ap.add_argument("--dry", action="store_true",
                    help="build every request shape, parse a canned stream, send nothing")
    ap.add_argument("--save", metavar="DIR", default=None,
                    help="with --dry, write each request text to DIR")
    args = ap.parse_args()
    if not args.dry:
        raise SystemExit("this file is a library; the only command it runs is --dry. "
                         "Nothing sent.")
    sys.exit(_dry(args.save))
