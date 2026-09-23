# send_w16.py - plan W16's driver (sections 4.1 to 4.4). It sends the six requests of section 3
# (atria-L1..L3, mimo-L1..L3) through the two clients in code/clients/, used unchanged, and saves
# every send whole under sends/. It holds no key: ATRIA_API_KEY and MIMO_API_KEY are read from
# the environment of the one command that runs it, and no file, prompt or line of output carries
# either value.
#
#   ATRIA_API_KEY=... MIMO_API_KEY=... /home/user/.venvs/threadsmith/bin/python send_w16.py PLAN
#   /home/user/.venvs/threadsmith/bin/python send_w16.py PLAN --preflight   # every check before the first send; sends and writes nothing
#   /home/user/.venvs/threadsmith/bin/python send_w16.py PLAN --check   # re-reads sends/, prints the check, writes nothing
#   /home/user/.venvs/threadsmith/bin/python send_w16.py PLAN --scan    # key scan of questioning/, prints, writes nothing
#
# Standard library, the two clients, rig.py (for its key check) and build_w16.py (Appendix B of
# the plan, saved byte for byte beside this file) only.
#
# What it does, in order, refusing (and sending nothing) at the first thing that is not as the
# plan fixes it:
#   1. the two clients' sha256 against plan 4.1; the endpoint and model variables of 4.2 unset;
#      both keys present in the environment;
#   2. the messages built by build_w16.build() against the hashes the plan froze (2.4), and against
#      the builder's own output in built/; the draft's sha256 against 2.1;
#   3. the two families' bodies (4.2): Atria build_body(messages, max_tokens=65536, stream=True);
#      MiMo build_body(messages, max_completion_tokens=131072, stream=True, thinking=True,
#      include_usage=False); the messages inside each body hashed again;
#   4. the size of each request against the model's documented context, estimated from characters
#      (2.5). Nothing is cut to fit, whatever the estimate says: plan 2.5, "nothing is cut to fit";
#   5. the sends: MiMo on three threads, one per lens, so at most three in flight; Atria on one
#      thread taking L1, L2, L3 in order, one in flight (its client's own lock would hold it so too). A send whose return is not an answer (4.3) is re-sent once,
#      as -s2, at the same ceiling, after the first has ended. Never a third send;
#   6. every file written through the key check (the values of DEEPSEEK_API_KEY, ATRIA_API_KEY and
#      MIMO_API_KEY, read by name: rig.assert_no_key for the first two, and each client's own
#      assert_no_key for its own key); after the sends, every file under questioning/ re-read through
#      the same check and scanned for the three key patterns;
#   7. sends/check.txt (4.4) and manifest.json, by program, from the saved files alone.
import hashlib
import json
import os
import re
import sys
import threading
import time
import traceback

HERE = os.path.dirname(os.path.abspath(__file__))                      # .../stage-B/questioning
RIG = os.path.normpath(os.path.join(HERE, "..", ".."))                  # .../W10 harness
CODE = os.path.join(RIG, "code")
SENDS = os.path.join(HERE, "sends")
BUILT = os.path.join(HERE, "built")
MANIFEST = os.path.join(HERE, "manifest.json")
CHECK = os.path.join(SENDS, "check.txt")
LOG = os.path.join(SENDS, "log.txt")

FAMILIES = ("atria", "mimo")
LENSES = ("L1", "L2", "L3")
CLIENT_SHA = {  # plan 4.1, at freezing
    "atria_client.py": "d6f4986609390924f77b7240f736cfef0b7278005be305278d72e60ed75e0f2d",
    "mimo_client.py": "9e03e285d2e8cb2fddf3f76eefa7922febd6b8e02b0ad3162f54973d5cb214b6",
}
DRAFT = "W15-draft-as-questioned.md"
DRAFT_SHA = "cff3373b23ec4a91f2ca7266b9c4edc2430d221c26caf8c8cf0f3e84b85138c8"   # plan 2.1
DRAFT_BYTES = 52216
MUST_BE_UNSET = ("ATRIA_BASE_URL", "ATRIA_MODEL", "MIMO_BASE_URL", "MIMO_MODEL",
                 "MIMO_REGION", "MIMO_AUTH_STYLE")                      # plan 4.2
KEY_OF = {"atria": "ATRIA_API_KEY", "mimo": "MIMO_API_KEY"}
KEY_ENV = ("DEEPSEEK_API_KEY", "ATRIA_API_KEY", "MIMO_API_KEY")
CEILING = {"atria": 65536, "mimo": 131072}                              # plan 4.2, the documented maxima
URL = {"atria": "https://api.atria-asi.ai/v1/chat/completions",
       "mimo": "https://token-plan-sgp.xiaomimimo.com/v1/chat/completions"}
MODEL = {"atria": "Atria-Dawn-Preview", "mimo": "mimo-v2.6-pro"}
CONTEXT = {"atria": 256000, "mimo": 1048576}   # Atria: "256K" (docs), 256,000 (its repository); MiMo: the client's CONTEXT
BODY_KEYS = {"atria": {"model", "messages", "max_tokens", "stream", "stream_options"},
             "mimo": {"model", "messages", "max_completion_tokens", "stream", "thinking"}}
PATTERNS = [("atr_", re.compile(r"atr_[A-Za-z0-9_-]{20,}")),
            ("tp-", re.compile(r"tp-[a-z0-9]{30,}")),
            ("sk-", re.compile(r"sk-[A-Za-z0-9]{20,}"))]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def stamp():
    return time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())


# ---------------------------------------------------------------- the key check, by name

class KeyInText(Exception):
    pass


_rig = None
_clients = {}


def key_check(text, where):
    """Refuse any text that carries the value of one of the three keys. The values are read
    from the environment by name, by rig.assert_no_key (DEEPSEEK_API_KEY, ATRIA_API_KEY) and by
    each client's own assert_no_key (ATRIA_API_KEY, MIMO_API_KEY). Never prints a value."""
    try:
        if _rig is not None:
            _rig.assert_no_key(text, where)
        if "atria" in _clients:
            _clients["atria"].assert_no_key(text, os.environ.get("ATRIA_API_KEY", ""))
        if "mimo" in _clients:
            _clients["mimo"].assert_no_key(text, os.environ.get("MIMO_API_KEY", ""))
    except SystemExit:
        raise KeyInText(f"{where}: the text carries the value of a key read from the environment")
    for name in KEY_ENV:                      # the same test once more, covering a client not imported
        v = os.environ.get(name, "")
        if len(v) >= 12 and v in text:
            raise KeyInText(f"{where}: the text carries the value of {name}")
    return True


# ---------------------------------------------------------------- the log

class Tee:
    """Everything printed goes to the terminal and to sends/log.txt, each write through the key
    check. A write that fails the check is not written; a line saying so is written instead."""

    def __init__(self, stream, fh, lock):
        self.stream, self.fh, self.lock = stream, fh, lock

    def write(self, s):
        if not s:
            return 0
        try:
            key_check(s, "a line of the log")
        except KeyInText:
            s = "[a line of output was refused: it carried the value of a key]\n"
        with self.lock:
            self.stream.write(s)
            self.fh.write(s)
            self.fh.flush()
        return len(s)

    def flush(self):
        with self.lock:
            self.stream.flush()
            self.fh.flush()


def say(s):
    print(s, flush=True)


def refuse(why):
    say(f"REFUSED: {why}. Nothing sent.")
    sys.exit(2)


# ---------------------------------------------------------------- writing a file

def write_bytes(path, data):
    text = data.decode("utf-8", "replace")
    key_check(text, os.path.relpath(path, HERE))
    if os.path.exists(path):
        raise FileExistsError(f"{path} exists; nothing saved is edited afterwards")
    with open(path, "wb") as f:
        f.write(data)
    return path


def write_text(path, text):
    return write_bytes(path, text.encode("utf-8"))


# ---------------------------------------------------------------- reading a return

def done_came(raw):
    if not isinstance(raw, list):
        return False
    for line in raw:
        s = line.strip() if isinstance(line, str) else ""
        if s.startswith("data:") and s[5:].strip() == "[DONE]":
            return True
    return False


def models_seen(raw):
    """The `model` field the reply carries, read from the raw return: every distinct value
    across the stream's chunks, in order of first appearance."""
    seen = []
    if isinstance(raw, list):
        for line in raw:
            if not isinstance(line, str) or not line.startswith("data:"):
                continue
            d = line[5:].strip()
            if d == "[DONE]":
                continue
            try:
                m = json.loads(d).get("model")
            except (ValueError, AttributeError):
                continue
            if m is not None and m not in seen:
                seen.append(m)
    elif isinstance(raw, dict) and raw.get("model") is not None:
        seen.append(raw["model"])
    return seen


def classify(rec):
    """Plan 4.3. Returns (verdict, why): 'answer', 'ceiling fault' or 'other fault'."""
    if rec is None or rec.get("record_missing"):
        return "other fault", "no record: the send raised before the client built one"
    if rec.get("error") is not None or rec.get("http_status") != 200:
        e = rec.get("error") or {}
        return "other fault", (f"HTTP {rec.get('http_status')}; {e.get('type', '')}: "
                               f"{(e.get('message') or '')[:300]}")
    msg = rec.get("message") or {}
    content = msg.get("content") or ""
    finish = rec.get("finish_reason")
    done = done_came(rec.get("raw"))
    if not content.strip():
        return "ceiling fault", f"content empty (finish reason {finish!r})"
    if finish in ("length", "repetition_truncation"):
        return "ceiling fault", f"finish reason {finish!r}"
    if finish == "stop":
        return "answer", "HTTP 200, content not empty, finish reason 'stop'"
    if finish is None and done:
        return "answer", "HTTP 200, content not empty, no finish reason, the [DONE] line came (G4)"
    return "other fault", f"finish reason {finish!r}; [DONE] line {'came' if done else 'did not come'}"


# ---------------------------------------------------------------- one send

RESULTS = []
RESULTS_LOCK = threading.Lock()
KEY_REFUSALS = []


def one_send(fam, lens, s, body):
    mod = _clients[fam]
    tag = f"W16-{fam}-{lens}-s{s}"
    stream_path = os.path.join(SENDS, f"{tag}.stream.txt")
    key = os.environ[KEY_OF[fam]]
    say(f"{stamp()}  {tag}: calling the client (ceiling {CEILING[fam]:,})")
    t0 = time.time()
    rec, err = None, None
    try:
        rec = mod.call(body, key, tag=tag, stream_path=stream_path, keep_raw=True)
    except SystemExit as e:                         # a client's own key check refused its record
        err = {"type": "SystemExit", "message": str(e), "status": None, "body": None}
    except Exception as e:                          # AtriaError, MiMoError, anything else
        rec = getattr(e, "record", None)
        err = {"type": type(e).__name__, "message": str(e),
               "status": getattr(e, "status", None), "body": getattr(e, "body", None),
               "retryable": getattr(e, "retryable", None)}
    del key
    wall = round(time.time() - t0, 1)
    if rec is None:
        saved = {"client": f"clients.{fam}_client", "tag": tag, "record_missing": True,
                 "request_text": mod.request_text(body), "error": err}
    else:
        saved = dict(rec)
        if err is not None:
            saved["error"] = err
    verdict, why = classify(saved)
    # the files of this send (4.4)
    files = {}
    try:
        files["request"] = write_text(os.path.join(SENDS, f"{tag}.request.json"), saved["request_text"])
        files["record"] = write_text(os.path.join(SENDS, f"{tag}.record.json"),
                                     json.dumps(saved, ensure_ascii=False, indent=1) + "\n")
        content = ((saved.get("message") or {}).get("content") or "")
        head = (f"# {tag} - the content of the reply, as extracted by program\n\n"
                f"Extracted by send_w16.py from `{tag}.record.json` (the record's `message.content`), "
                f"unchanged below the rule. Family {fam}, lens {lens}, send {s}. Verdict under plan W16 "
                f"section 4.3: {verdict} ({why}).")
        if verdict != "answer":
            head += (" This send is NOT an answer and is never read as one, not even in part "
                     "(plan W16 section 4.3).")
        head += " The reply's `reasoning_content`, if any, is kept in the record and is not reproduced here.\n\n---\n\n"
        files["answer"] = write_text(os.path.join(SENDS, f"{tag}.answer.md"), head + content)
    except KeyInText as e:
        KEY_REFUSALS.append(str(e))
        say(f"{stamp()}  {tag}: REFUSED TO SAVE: {e}")
    except FileExistsError as e:
        say(f"{stamp()}  {tag}: NOT SAVED: {e}")
    msg = saved.get("message") or {}
    say(f"{stamp()}  {tag}: {verdict} - {why}; HTTP {saved.get('http_status')}; "
        f"attempts {len(saved.get('attempts') or [])}; client seconds {saved.get('seconds')}; "
        f"driver seconds {wall}; content {len(msg.get('content') or ''):,} characters; "
        f"reasoning {len(msg.get('reasoning_content') or ''):,} characters; usage {json.dumps(saved.get('usage') or {})}")
    with RESULTS_LOCK:
        RESULTS.append({"tag": tag, "family": fam, "lens": lens, "send": s, "verdict": verdict})
    return verdict


def one_request(fam, lens, body):
    try:
        v = one_send(fam, lens, 1, body)
        if v != "answer":
            say(f"{stamp()}  W16-{fam}-{lens}: the first send is not an answer ({v}); re-sent once as -s2 at the "
                f"same ceiling {CEILING[fam]:,} (plan 4.3)")
            v = one_send(fam, lens, 2, body)
            if v != "answer":
                say(f"{stamp()}  W16-{fam}-{lens}: no answer after the second send; nothing further "
                    f"is sent under this plan (4.3)")
    except Exception:
        say(f"{stamp()}  W16-{fam}-{lens}: the driver's thread failed:\n{traceback.format_exc()}")


# ---------------------------------------------------------------- the check (4.4) and the manifest

def read_saved():
    """Every saved send, read back from sends/ alone."""
    out = []
    if not os.path.isdir(SENDS):
        return out
    for name in sorted(os.listdir(SENDS)):
        m = re.fullmatch(r"W16-(atria|mimo)-(L[123])-s([12])\.record\.json", name)
        if m:
            out.append((m.group(1), m.group(2), int(m.group(3)), name[:-len(".record.json")]))
    return out


def check_and_manifest(expected):
    lines, rows = [], []
    lines.append("plan W16, sends/check.txt - written by send_w16.py after the sends, from the saved files alone")
    lines.append(f"written {stamp()}")
    lines.append("")
    per_request = {}
    for fam, lens, s, tag in read_saved():
        paths = {k: os.path.join(SENDS, f"{tag}.{ext}") for k, ext in
                 (("request", "request.json"), ("record", "record.json"),
                  ("stream", "stream.txt"), ("answer", "answer.md"))}
        rec = json.load(open(paths["record"], encoding="utf-8"))
        req_text = open(paths["request"], "rb").read() if os.path.exists(paths["request"]) else b""
        try:
            req = json.loads(req_text.decode("utf-8"))
            msg_sha = sha(json.dumps(req["messages"], ensure_ascii=False).encode("utf-8"))
        except (ValueError, KeyError):
            req, msg_sha = {}, None
        exp = expected[f"messages-{lens}"]
        verdict, why = classify(rec)
        msg = rec.get("message") or {}
        raw = rec.get("raw")
        ceiling = (req.get("max_tokens") if fam == "atria" else req.get("max_completion_tokens"))
        row = {
            "tag": tag, "family": fam, "lens": lens, "send": s,
            "verdict": verdict, "why": why,
            "messages_sha256": msg_sha, "messages_sha256_frozen": exp,
            "messages_equal_frozen": msg_sha == exp,
            "url": rec.get("url"), "model_sent": req.get("model"),
            "model_in_reply": models_seen(raw),
            "ceiling": ceiling, "ceiling_field": "max_tokens" if fam == "atria" else "max_completion_tokens",
            "http_status": rec.get("http_status"), "attempts": len(rec.get("attempts") or []),
            "attempt_statuses": [a.get("status") for a in (rec.get("attempts") or [])],
            "attempt_seconds": [a.get("seconds") for a in (rec.get("attempts") or [])],
            "attempt_errors": [a.get("error") for a in (rec.get("attempts") or []) if a.get("error")],
            "finish_reason": rec.get("finish_reason"), "done_line_came": done_came(raw),
            "usage": rec.get("usage") or {}, "truncated": rec.get("truncated"),
            "seconds": rec.get("seconds"), "started_at": rec.get("started_at"),
            "finished_at": rec.get("finished_at"),
            "content_characters": len(msg.get("content") or ""),
            "content_non_empty": bool((msg.get("content") or "").strip()),
            "reasoning_characters": len(msg.get("reasoning_content") or ""),
            "stream_lines": len(raw) if isinstance(raw, list) else None,
            "error": rec.get("error"),
            "files": {},
        }
        if fam == "mimo":
            row.update({"thinking_seen": rec.get("thinking_seen"),
                        "usage_missing": rec.get("usage_missing"),
                        "repetition_truncated": rec.get("repetition_truncated")})
        for k, p in paths.items():
            if os.path.exists(p):
                b = open(p, "rb").read()
                row["files"][os.path.relpath(p, HERE)] = {"bytes": len(b), "sha256": sha(b)}
        rows.append(row)
        per_request.setdefault((fam, lens), []).append(row)
        lines.append(f"{tag}")
        lines.append(f"  verdict (4.3)        {verdict}: {why}")
        lines.append(f"  messages sha256      {msg_sha}  {'EQUAL to' if msg_sha == exp else 'DIFFERS from'} "
                     f"the frozen messages-{lens} {exp}")
        lines.append(f"  endpoint             {rec.get('url')}")
        lines.append(f"  model sent           {req.get('model')}")
        lines.append(f"  model in the reply   {', '.join(map(str, row['model_in_reply'])) or '(none carried)'}")
        lines.append(f"  ceiling              {row['ceiling_field']} {ceiling}")
        lines.append(f"  HTTP                 {rec.get('http_status')}; attempts {row['attempts']} "
                     f"(statuses {row['attempt_statuses']}; seconds {row['attempt_seconds']})")
        for err_text in row["attempt_errors"]:
            lines.append(f"  attempt error        {str(err_text)[:300]}")
        lines.append(f"  finish reason        {rec.get('finish_reason')!r}")
        lines.append(f"  [DONE] line          {'came' if row['done_line_came'] else 'did not come'}")
        lines.append(f"  usage                {json.dumps(row['usage'], ensure_ascii=False)}")
        lines.append(f"  truncated            {rec.get('truncated')}")
        if fam == "mimo":
            lines.append(f"  thinking_seen        {rec.get('thinking_seen')}")
            lines.append(f"  usage_missing        {rec.get('usage_missing')}")
            lines.append(f"  repetition_truncated {rec.get('repetition_truncated')}")
        lines.append(f"  content              {row['content_characters']:,} characters"
                     f"{'' if row['content_non_empty'] else ' (empty once whitespace is stripped)'}")
        lines.append(f"  reasoning_content    {row['reasoning_characters']:,} characters")
        lines.append(f"  seconds              {rec.get('seconds')} (started {rec.get('started_at')}, "
                     f"finished {rec.get('finished_at')})")
        if rec.get("error"):
            e = rec["error"]
            lines.append(f"  error                {e.get('type')}: {(e.get('message') or '')[:400]}")
        lines.append("")
    requests_ = []
    for fam in FAMILIES:
        for lens in LENSES:
            sends = per_request.get((fam, lens), [])
            ans = [r["tag"] for r in sends if r["verdict"] == "answer"]
            requests_.append({"family": fam, "lens": lens, "sends": [r["tag"] for r in sends],
                              "answered": bool(ans), "answer": ans[0] if ans else None})
    w16_1 = all(r["answered"] for r in requests_) and len(requests_) == 6
    lines.append("Per request (plan W16 section 3; a request is answered when one of its at most two sends is an answer, 4.3)")
    for r in requests_:
        lines.append(f"  {r['family']}-{r['lens']}: {'answered by ' + r['answer'] if r['answered'] else 'NO ANSWER'}"
                     f"  (sends: {', '.join(r['sends']) or 'none'})")
    lines.append("")
    all_equal = all(r["messages_equal_frozen"] for r in rows) and bool(rows)
    lines.append(f"Every saved request's messages equal the frozen line for its lens: {'yes' if all_equal else 'NO'}")
    lines.append(f"W16.1 (all six requests return an answer within two sends each): "
                 f"{'HOLDS' if w16_1 else 'FAILS'}")
    ceiling_faults_first = [r["tag"] for r in rows if r["send"] == 1 and r["verdict"] == "ceiling fault"]
    lines.append(f"First sends that are ceiling faults (W16.5's count, read per family): "
                 f"{', '.join(ceiling_faults_first) or 'none'}")
    text = "\n".join(lines) + "\n"
    manifest = {"plan": "W16", "written": stamp(), "sends": rows, "requests": requests_,
                "messages_all_equal_frozen": all_equal, "W16.1": "holds" if w16_1 else "fails",
                "first_sends_ceiling_faults": ceiling_faults_first}
    return text, manifest


# ---------------------------------------------------------------- the key scan

def scan():
    """Every file under questioning/, re-read through the key check (values by name) and scanned
    for the three key patterns. Prints file names and counts, never a match."""
    hits = 0
    n = 0
    for root, _, names in os.walk(HERE):
        for name in sorted(names):
            p = os.path.join(root, name)
            text = open(p, "rb").read().decode("utf-8", "replace")
            n += 1
            rel = os.path.relpath(p, HERE)
            try:
                key_check(text, rel)
            except KeyInText as e:
                hits += 1
                say(f"  KEY VALUE FOUND: {e}")
            for label, rx in PATTERNS:
                c = len(rx.findall(text))
                if c:
                    hits += 1
                    say(f"  PATTERN {label} matched {c} time(s) in {rel}")
    names_present = [k for k in KEY_ENV if os.environ.get(k)]
    say(f"key scan: {n} files under questioning/; values checked by name for "
        f"{', '.join(names_present) or 'no variable (none in this environment)'}; the three patterns "
        f"atr_[A-Za-z0-9_-]{{20,}}, tp-[a-z0-9]{{30,}}, sk-[A-Za-z0-9]{{20,}}; hits: {hits}")
    return hits


# ---------------------------------------------------------------- main

def load_expected_and_build(plan):
    sys.path.insert(0, HERE)
    import build_w16
    repo = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(plan))))
    return build_w16, repo


def preflight(plan, require_keys):
    """Everything before the first send (plan 2.1, 2.4, 2.5, 4.1, 4.2). Refuses at the first
    thing that is not as the plan fixes it. Sends nothing and writes nothing."""
    say(f"plan      {plan}")
    say(f"          sha256 {sha(open(plan, 'rb').read())}")
    say(f"python    {sys.executable} {sys.version.split()[0]}")
    for name, h in CLIENT_SHA.items():
        got = sha(open(os.path.join(CODE, "clients", name), "rb").read())
        if got != h:
            refuse(f"code/clients/{name} is sha256 {got}, not {h} (plan 4.1)")
        say(f"client    code/clients/{name} sha256 {got}: equal to plan 4.1")
    bad = [v for v in MUST_BE_UNSET if os.environ.get(v)]
    if bad:
        refuse(f"{', '.join(bad)} set; plan 4.2 sends the clients' defaults with these unset")
    say(f"env       {', '.join(MUST_BE_UNSET)}: all unset (plan 4.2)")
    if require_keys:
        for fam, var in KEY_OF.items():
            if not os.environ.get(var):
                refuse(f"{var} is not in the environment")
    from clients import atria_client, mimo_client
    _clients.update({"atria": atria_client, "mimo": mimo_client})
    if require_keys:
        say(f"keys      ATRIA_API_KEY present (documented prefix: "
            f"{'yes' if os.environ['ATRIA_API_KEY'].startswith(atria_client.KEY_PREFIX) else 'no'}); "
            f"MIMO_API_KEY present (reads as: {mimo_client.key_kind(os.environ['MIMO_API_KEY'])}); "
            f"no value is printed or written")
    else:
        say("keys      not required in this mode: " + ", ".join(
            f"{v} {'present' if os.environ.get(v) else 'absent'}" for v in KEY_ENV))
    if atria_client.endpoint() != URL["atria"] or atria_client.MODEL != MODEL["atria"]:
        refuse(f"the Atria client's defaults are {atria_client.endpoint()} {atria_client.MODEL}")
    if mimo_client.endpoint() != URL["mimo"] or mimo_client.MODEL != MODEL["mimo"]:
        refuse(f"the MiMo client's defaults are {mimo_client.endpoint()} {mimo_client.MODEL}")
    if atria_client.MAX_TOKENS != CEILING["atria"] or mimo_client.MAX_TOKENS != CEILING["mimo"]:
        refuse("a client's documented maximum is not the plan's")
    say(f"atria     {atria_client.endpoint()}  model {atria_client.MODEL}  ceiling max {atria_client.MAX_TOKENS:,}  "
        f"one at a time (client lock)  rpm cap {atria_client.RPM_CAP}  timeout {atria_client.TIMEOUT}  tries {atria_client.TRIES}")
    say(f"mimo      {mimo_client.endpoint()}  model {mimo_client.MODEL}  ceiling max {mimo_client.MAX_TOKENS:,}  "
        f"auth {mimo_client.AUTH_STYLE}  three threads here  rpm cap {mimo_client.RPM_CAP}  "
        f"timeout {mimo_client.TIMEOUT}  tries {mimo_client.TRIES}  context {mimo_client.CONTEXT:,}")

    draft = open(os.path.join(HERE, DRAFT), "rb").read()
    if sha(draft) != DRAFT_SHA or len(draft) != DRAFT_BYTES:
        refuse(f"{DRAFT} is {len(draft)} bytes sha256 {sha(draft)}, not plan 2.1's")
    say(f"draft     {DRAFT}: {len(draft):,} bytes, sha256 {sha(draft)}: equal to plan 2.1")

    build_w16, repo = load_expected_and_build(plan)
    system, users, messages, sources = build_w16.build(repo, open(plan, encoding="utf-8").read())
    got = {"system": sha(system.encode("utf-8"))}
    for L in LENSES:
        got[f"user-{L}"] = sha(users[L].encode("utf-8"))
        got[f"messages-{L}"] = sha(json.dumps(messages[L], ensure_ascii=False).encode("utf-8"))
    if got != build_w16.EXPECTED:
        refuse(f"built messages differ from the plan's frozen hashes: "
               f"{[k for k in got if got[k] != build_w16.EXPECTED.get(k)]}")
    for L in LENSES:
        on_disk = open(os.path.join(BUILT, f"messages-{L}.json"), "rb").read()
        if on_disk != json.dumps(messages[L], ensure_ascii=False).encode("utf-8"):
            refuse(f"built/messages-{L}.json differs from what the builder builds now")
    say("builder   build_w16.build(): system, user-L1..L3, messages-L1..L3 all equal to the plan's frozen "
        "hashes (2.4), and equal byte for byte to built/messages-L*.json")

    bodies = {"atria": {}, "mimo": {}}
    for L in LENSES:
        bodies["atria"][L] = atria_client.build_body(messages[L], max_tokens=65536, stream=True)
        bodies["mimo"][L] = mimo_client.build_body(messages[L], max_completion_tokens=131072, stream=True,
                                                   thinking=True, include_usage=False)
        for fam in FAMILIES:
            b = bodies[fam][L]
            if set(b) != BODY_KEYS[fam]:
                refuse(f"the {fam} body carries {sorted(b)}, not {sorted(BODY_KEYS[fam])}")
            c = b["max_tokens"] if fam == "atria" else b["max_completion_tokens"]
            if c != CEILING[fam] or c < 65536:
                refuse(f"the {fam} ceiling is {c}")
            if b["model"] != MODEL[fam] or b["stream"] is not True:
                refuse(f"the {fam} body's model or stream is not the plan's")
            h = sha(json.dumps(b["messages"], ensure_ascii=False).encode("utf-8"))
            if h != build_w16.EXPECTED[f"messages-{L}"]:
                refuse(f"the {fam}-{L} body's messages hash {h}")
            try:
                key_check(_clients[fam].request_text(b), f"the {fam}-{L} request text")
            except KeyInText as e:
                refuse(str(e))
    if bodies["atria"]["L1"].get("stream_options") != {"include_usage": True} \
            or bodies["mimo"]["L1"].get("thinking") != {"type": "enabled"}:
        refuse("the fields each client adds are not the plan's (4.2)")
    say("bodies    atria: model, messages, max_tokens 65536, stream true, stream_options include_usage "
        "(the client's own); mimo: model, messages, max_completion_tokens 131072, stream true, thinking "
        "enabled; nothing else. Each body's messages hash equal to its lens's frozen line; no key in any request text")
    for L in LENSES:
        chars = len(system) + len(users[L])
        lo, hi = chars // 4, chars // 3
        for fam in FAMILIES:
            need = hi + CEILING[fam]
            fits = need <= CONTEXT[fam]
            say(f"size      {fam}-{L}: {chars:,} characters, about {lo:,} to {hi:,} tokens of input by the "
                f"plan's estimate (2.5); with the ceiling {CEILING[fam]:,}, at most {need:,} of the documented "
                f"{CONTEXT[fam]:,}: {'fits' if fits else 'DOES NOT FIT by the estimate'}"
                f"{'' if fits else '; sent whole all the same: plan 2.5, nothing is cut to fit, and a refusal for size is recorded as a fault and re-sent once'}")
    return build_w16, bodies


def main():
    global _rig
    args = sys.argv[1:]
    if not args or args[0].startswith("-") or len(args) > 2:
        print("usage: send_w16.py PLAN [--preflight | --check | --scan]")
        sys.exit(2)
    plan = os.path.abspath(args[0])
    mode = args[1] if len(args) == 2 else "send"
    if mode not in ("send", "--preflight", "--check", "--scan"):
        print(f"unknown mode {mode}")
        sys.exit(2)
    sys.path.insert(0, CODE)
    import rig
    _rig = rig
    if mode == "--preflight":
        say(f"send_w16.py --preflight: every check before the first send; sends nothing, writes nothing; {stamp()}")
        preflight(plan, require_keys=False)
        say("preflight passed. Nothing sent, nothing written.")
        return
    if mode in ("--check", "--scan"):
        from clients import atria_client, mimo_client
        _clients.update({"atria": atria_client, "mimo": mimo_client})
        build_w16, _ = load_expected_and_build(plan)
        if mode == "--scan":
            sys.exit(1 if scan() else 0)
        text, _ = check_and_manifest(build_w16.EXPECTED)
        sys.stdout.write(text)
        return

    # ------------------------------------------------ the send
    os.makedirs(SENDS, exist_ok=True)
    if any(n.startswith("W16-") for n in os.listdir(SENDS)) or os.path.exists(LOG):
        print("REFUSED: sends/ already holds a send or a log; nothing saved is edited afterwards. Nothing sent.")
        sys.exit(2)
    lock = threading.Lock()
    fh = open(LOG, "w", encoding="utf-8")
    sys.stdout = Tee(sys.__stdout__, fh, lock)
    sys.stderr = Tee(sys.__stderr__, fh, lock)
    say(f"send_w16.py - plan W16's driver; started {stamp()}")
    build_w16, bodies = preflight(plan, require_keys=True)

    say(f"{stamp()}  sending: six requests; MiMo on three threads, one per lens (at most three in flight); "
        f"Atria on one thread, its lenses in order L1, L2, L3 (one in flight, as its client's lock also holds)")
    # MiMo: one thread per lens, so at most three in flight. Atria: one thread that takes its three
    # lenses in order, each with its one re-send if needed; the client's lock would hold it to one
    # in flight whatever the threads, and one thread keeps the client's own `seconds` free of time
    # spent waiting on that lock.
    def atria_all():
        for L in LENSES:
            one_request("atria", L, bodies["atria"][L])
    threads = [threading.Thread(target=atria_all, name="atria")] + [
        threading.Thread(target=one_request, args=("mimo", L, bodies["mimo"][L]), name=f"mimo-{L}")
        for L in LENSES]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    say(f"{stamp()}  all sends ended")

    # ------------------------------------------------ after the sends
    hits = scan()
    text, manifest = check_and_manifest(build_w16.EXPECTED)
    try:
        write_text(CHECK, text)
        write_text(MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=1) + "\n")
    except (KeyInText, FileExistsError) as e:
        say(f"REFUSED TO WRITE the check or the manifest: {e}")
        hits += 1
    sys.stdout.write(text)
    say(f"key refusals while saving: {len(KEY_REFUSALS)}")
    say(f"finished {stamp()}")
    fh.flush()
    sys.exit(1 if (hits or KEY_REFUSALS) else 0)


if __name__ == "__main__":
    main()
