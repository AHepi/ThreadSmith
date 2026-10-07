#!/usr/bin/env python3
"""glm_via_claude_code.py: one call to GLM 5.3 (Z.ai) through Claude Code, with a receipt (27 September 2026).

Why through Claude Code: the key is a GLM Coding Plan key, and Z.ai's usage policy lets it be used only within officially
supported tools; Z.ai's page https://docs.z.ai/devpack/tool/claude names Claude Code as one (decision S29). This tool
replaces s96_glm_call.py (which sent to Z.ai's OpenAI-compatible Coding Plan URL directly) for every further GLM call.

The call. `claude -p` runs as a separate process, with a fresh environment built here (nothing of this session's own
environment is passed on except the proxy and CA settings the network needs, so this session's model, effort, thinking
budget and tokens never reach it), its own HOME and CLAUDE_CONFIG_DIR in the scratchpad (--home, by default
<SEMANTICS_RUN_DIR>/glm_claude_code_home; refused if inside the repository or inside ~/.claude), and a working folder
there with nothing in it. The brief, whole, is the one prompt: the brief file is opened and given to the process as its
standard input (piped explicitly from the file; the argument list has a size limit per argument that a brief can pass).
  Environment: ANTHROPIC_BASE_URL https://api.z.ai/api/anthropic; ANTHROPIC_AUTH_TOKEN from GLM_API_KEY (the key goes
  only into that variable of the child process, never into a file, an argument or a log); ANTHROPIC_MODEL and
  ANTHROPIC_DEFAULT_OPUS_MODEL / _SONNET_MODEL / _HAIKU_MODEL all glm-5.3 (the full model, never Flash); API_TIMEOUT_MS
  3000000; CLAUDE_CODE_MAX_OUTPUT_TOKENS 64000; CLAUDE_CODE_MAX_RETRIES 0 (every failure comes back to this tool, which
  retries and records it); CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC 1, DISABLE_AUTOUPDATER 1, DISABLE_TELEMETRY 1,
  DISABLE_ERROR_REPORTING 1; CLAUDE_CODE_SIMPLE 1 (drops the environment block the CLI otherwise adds; unlike --bare it
  keeps the Bearer token Z.ai documents); CLAUDE_CODE_ATTRIBUTION_HEADER 0 (drops the billing line from the system text).
  Arguments: -p --model glm-5.3 --effort medium --tools "" --system-prompt "" --output-format stream-json --verbose
  --no-session-persistence --strict-mcp-config --disable-slash-commands.
  Effort: --effort medium, the owner's rule for outside readers (decision S17). What the CLI sends for it, and what it
  adds, was observed on 27 September 2026 with Claude Code 2.1.283 by pointing the same command at a local stand-in
  server with a dummy token (WHAT_THE_CLI_SENDS below): "thinking": {"type": "adaptive"}, "output_config": {"effort":
  "medium"} (beta effort-2025-11-24), "max_tokens": 64000, "model": "glm-5.3", no tools; system text "You are a Claude
  agent, built on Anthropic's Claude Agent SDK." (the CLI adds it to any system prompt, the empty one included); after
  the brief, a system message "Today's date is <date>." Whether Z.ai acts on output_config.effort is not known.
  --context-1m sends the model as "glm-5.3[1m]", the form Z.ai's page gives: the same model id goes on the wire, with the
  context-1m beta header, and Claude Code counts a 1,000,000-token window instead of 200,000 (for a brief near 200,000
  tokens). A run whose CLI version is not 2.1.283 says so in its receipt: what that version sends was not observed.
  The init event must show no tools and no MCP servers, or the attempt is stopped as final and nothing is accepted.

Files, in --out, all under --tag, none ever overwritten (the call refuses to start if any file of the tag exists, and
every file is written whole to a temporary name and then linked into place, which fails if the name is taken):
  <tag>.request.json   the command, the environment (the key as "[GLM_API_KEY, withheld]"), the brief's hashes and what
                       the CLI was observed to send; written before the first attempt
  <tag>.aN.stdout.jsonl / <tag>.aN.stderr.txt   the CLI's own output, for every attempt not accepted
  <tag>.aN.truncated.txt / <tag>.aN.reasoning.txt   an answer that came back but was not accepted
  on acceptance: <tag>.reasoning.txt (if thinking came back), then <tag>.receipt.json, then <tag>.response.txt last;
  on failure: <tag>.error.txt, then <tag>.receipt.json with "accepted": false.
Receipt: the model the reply reports (message.model of each assistant event), usage and the CLI's modelUsage, the CLI's
durations, start and end times, every attempt, and "accepted" by the rule: the reply's last non-blank line carries
END OF REPORT (s80_common.report_complete).
Retries: up to --attempts (6). Connection failures, timeouts, a process that ends without a result, HTTP 429 (other than
Z.ai codes 1113, no balance, and 1309, package expired) and 5xx -> the same call again after min(120, 10 * 2**n)
seconds. HTTP 400, 401, 403, 404, 413, 422, 1113 and 1309 are final. An answer that comes back without the sentinel is
sent again, at most --max-rejects (3) such answers in all.
Lesson S12: with --rule, nothing is sent unless that file is tracked by git and unchanged from HEAD; with --brief-md5,
nothing is sent unless the brief has that md5. Every attempt holds the "glm" provider slot (s80_common.provider_slot;
one GLM call at a time from 27 September 2026, decision S35). Progress goes to stdout as counts and times only.
A deadline (--deadline, 7200 s per attempt) stops the child process this tool started, by its own PID.
"""
import argparse, datetime, json, os, re, subprocess, sys, threading, time

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s80_common as C  # noqa: E402
from s96_glm_call import check_rule, write_new  # noqa: E402

CLAUDE = "/opt/node22/bin/claude"
CAPTURED_VERSION = "2.1.283"
BASE_URL = "https://api.z.ai/api/anthropic"
MODEL = "glm-5.3"
KEYNAME = "GLM_API_KEY"
KEY_SHOWN = "[GLM_API_KEY, withheld]"
EFFORTS = ("low", "medium", "high", "xhigh", "max")   # the values the CLI's --effort takes
SYSTEM_PROMPT = ""                                   # the CLI takes an empty --system-prompt
MAX_OUTPUT_TOKENS = "64000"
API_TIMEOUT_MS = "3000000"
PASS_THROUGH = ("HTTPS_PROXY", "https_proxy", "NO_PROXY", "no_proxy", "NODE_EXTRA_CA_CERTS", "SSL_CERT_FILE")
FINAL_STATUS = {400, 401, 403, 404, 413, 422}
FINAL_CODES = {"1113", "1309"}                       # Z.ai: no balance; package expired
PROGRESS_EVERY = 300
WHAT_THE_CLI_SENDS = {
    "observed": "27 September 2026, Claude Code 2.1.283, this command against a local stand-in server, dummy token",
    "request": "POST <base>/v1/messages?beta=true, stream true, Authorization: Bearer <token>",
    "model": "glm-5.3 (also with --context-1m, which adds the beta context-1m-2025-08-07)",
    "max_tokens": 64000, "thinking": {"type": "adaptive"}, "output_config": {"effort": "<--effort>"},
    "context_management": {"edits": [{"type": "clear_thinking_20251015", "keep": "all"}]}, "tools": [],
    "system": ["You are a Claude agent, built on Anthropic's Claude Agent SDK."],
    "messages": ["user: the brief, whole", "system: Today's date is <date>."],
    "anthropic_beta": "claude-code-20250219, interleaved-thinking-2025-05-14, thinking-token-count-2026-05-13, "
                      "context-management-2025-06-27, prompt-caching-scope-2026-01-05, "
                      "mid-conversation-system-2026-04-07, effort-2025-11-24",
    "before_it": "HEAD <base>/api/hello (a reachability check)"}


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def inside(path, root):
    path, root = os.path.realpath(path), os.path.realpath(root)
    return path == root or path.startswith(root + os.sep)


class Guard:
    """Every text written or printed passes through here: the key, if it ever appears, is replaced and noted."""
    def __init__(self, key):
        self.key, self.hits = key, 0

    def __call__(self, text):
        if self.key and text and self.key in text:
            self.hits += 1
            return text.replace(self.key, "[key withheld]")
        return text


def child_env(key, home, model, base_url):
    env = {"PATH": "/opt/node22/bin:/usr/local/bin:/usr/bin:/bin", "HOME": home,
           "CLAUDE_CONFIG_DIR": os.path.join(home, "config"), "LANG": "C.UTF-8", "TERM": "dumb"}
    env.update({k: os.environ[k] for k in PASS_THROUGH if os.environ.get(k)})
    env.update({"ANTHROPIC_BASE_URL": base_url, "ANTHROPIC_AUTH_TOKEN": key, "ANTHROPIC_MODEL": model,
                "ANTHROPIC_DEFAULT_OPUS_MODEL": model, "ANTHROPIC_DEFAULT_SONNET_MODEL": model,
                "ANTHROPIC_DEFAULT_HAIKU_MODEL": model, "API_TIMEOUT_MS": API_TIMEOUT_MS,
                "CLAUDE_CODE_MAX_OUTPUT_TOKENS": MAX_OUTPUT_TOKENS, "CLAUDE_CODE_MAX_RETRIES": "0",
                "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1", "DISABLE_AUTOUPDATER": "1", "DISABLE_TELEMETRY": "1",
                "DISABLE_ERROR_REPORTING": "1", "CLAUDE_CODE_SIMPLE": "1", "CLAUDE_CODE_ATTRIBUTION_HEADER": "0"})
    return env


def shown_env(env):
    return {k: (KEY_SHOWN if k == "ANTHROPIC_AUTH_TOKEN" else v) for k, v in sorted(env.items())}


def argv_for(model, effort):
    return [CLAUDE, "-p", "--model", model, "--effort", effort, "--tools", "", "--system-prompt", SYSTEM_PROMPT,
            "--output-format", "stream-json", "--verbose", "--no-session-persistence", "--strict-mcp-config",
            "--disable-slash-commands"]


def cli_version(env, cwd):
    try:
        r = subprocess.run([CLAUDE, "--version"], env=env, cwd=cwd, stdin=subprocess.DEVNULL, capture_output=True,
                           text=True, timeout=60)
        return (r.stdout.strip().split() or ["?"])[0]
    except Exception as e:
        return "unknown (%s)" % type(e).__name__


def run_once(argv, env, cwd, brief, deadline, label):
    """One attempt: the CLI with the brief file as its standard input. Returns a dict of what came back."""
    out = dict(stdout="", stderr="", exit=None, killed=False, init=None, assistant=[], result=None, other=[],
               texts=[], thinking=[])
    t0 = time.time()
    with open(brief, "rb") as fin:
        proc = subprocess.Popen(argv, stdin=fin, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, cwd=cwd)
    err_chunks = []
    t_err = threading.Thread(target=lambda: err_chunks.append(proc.stderr.read()), daemon=True)
    t_err.start()
    done = threading.Event()

    def watchdog():
        next_note = t0 + PROGRESS_EVERY
        while not done.wait(5):
            if time.time() - t0 > deadline and proc.poll() is None:
                out["killed"] = True
                proc.kill()   # the child this tool started, by its own PID
                return
            if time.time() > next_note:
                C.log("%s: still running, %d s, %d event(s)" % (label, time.time() - t0, len(lines)))
                next_note += PROGRESS_EVERY
    lines = []
    t_dog = threading.Thread(target=watchdog, daemon=True)
    t_dog.start()
    for raw in proc.stdout:
        line = raw.decode("utf-8", "replace")
        lines.append(line)
        try:
            d = json.loads(line)
        except Exception:
            continue
        typ = d.get("type")
        if typ == "system" and d.get("subtype") == "init":
            out["init"] = {k: d.get(k) for k in ("model", "tools", "mcp_servers", "apiKeySource", "permissionMode",
                                                 "claude_code_version", "cwd")}
        elif typ == "assistant":
            m = d.get("message") or {}
            out["assistant"].append({"model": m.get("model"), "id": m.get("id"), "stop_reason": m.get("stop_reason"),
                                     "usage": m.get("usage")})
            for b in m.get("content") or []:
                if b.get("type") == "text":
                    out["texts"].append(b.get("text") or "")
                elif b.get("type") == "thinking":
                    out["thinking"].append(b.get("thinking") or "")
        elif typ == "result":
            out["result"] = d
        else:
            out["other"].append({k: d.get(k) for k in ("type", "subtype", "attempt", "error_status", "error")
                                 if k in d})
    proc.wait()
    done.set()
    t_err.join(timeout=30)
    out["exit"] = proc.returncode
    out["stdout"] = "".join(lines)
    out["stderr"] = (err_chunks[0] if err_chunks else b"").decode("utf-8", "replace")
    out["seconds"] = round(time.time() - t0, 1)
    return out


def classify(o):
    """(error class, final?) for an attempt that was not accepted; ("", False) for an answer to judge."""
    if o["killed"]:
        return "deadline", False
    init = o["init"] or {}
    if o["init"] and (init.get("tools") or init.get("mcp_servers")):
        return "tools_or_mcp_present", True
    r = o["result"]
    if r is None:
        return "no_result_exit_%s" % o["exit"], False
    if r.get("subtype") == "success" and not r.get("is_error"):
        return "", False
    text = str(r.get("result") or "") + " " + json.dumps(r.get("errors") or "")
    status = r.get("api_error_status")
    m = re.search(r"API Error: (\d{3})", text)
    status = int(status) if isinstance(status, int) or (isinstance(status, str) and status.isdigit()) else (
        int(m.group(1)) if m else None)
    code = re.search(r'"code"\s*:\s*"?(\d{4})', text)
    code = code and code.group(1)
    if code in FINAL_CODES:
        return "http_%s_code_%s" % (status, code), True
    if status in FINAL_STATUS:
        return "http_%d" % status, True
    if status == 429 or (status and status >= 500):
        return "http_%d" % status, False
    if re.search(r"connection|timed out|timeout|ECONNRESET|socket|network|overloaded|fetch failed", text, re.I):
        return "connection", False
    return "cli_error_%s" % (r.get("subtype") or "unknown"), False


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--brief", required=True, help="the file sent, whole, as the one prompt")
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True, help="the folder the files go to")
    ap.add_argument("--effort", default="medium", choices=EFFORTS, help="medium: the owner's rule (decision S17)")
    ap.add_argument("--context-1m", action="store_true", help='send the model as "glm-5.3[1m]" (see the docstring)')
    ap.add_argument("--attempts", type=int, default=6)
    ap.add_argument("--max-rejects", type=int, default=3)
    ap.add_argument("--deadline", type=int, default=7200, help="seconds of wall clock per attempt")
    ap.add_argument("--home", default=os.path.join(C.RUN_DIR, "glm_claude_code_home"),
                    help="HOME and CLAUDE_CONFIG_DIR (under it) for the child; must be outside the repository")
    ap.add_argument("--base-url", default=BASE_URL, help="only for a test against a local stand-in server")
    ap.add_argument("--rule", help="the note written before sending; must be committed and unchanged")
    ap.add_argument("--brief-md5", help="refuse unless the brief has this md5")
    a = ap.parse_args()

    home = os.path.abspath(a.home)
    if inside(home, C.REPO) or inside(home, "/root/.claude") or inside(os.path.expanduser("~/.claude"), home):
        raise SystemExit("--home %s is inside the repository or holds/is inside ~/.claude; nothing sent" % home)
    key = os.environ.get(KEYNAME)
    if not key:
        raise SystemExit("%s is not set in the environment; nothing sent" % KEYNAME)
    if not os.access(CLAUDE, os.X_OK):
        raise SystemExit("%s is not there; nothing sent" % CLAUDE)
    brief_md5 = C.md5_file(a.brief)
    if a.brief_md5 and brief_md5 != a.brief_md5:
        raise SystemExit("the brief has md5 %s, expected %s; nothing sent" % (brief_md5, a.brief_md5))
    rule = check_rule(a.rule) if a.rule else None
    os.makedirs(a.out, exist_ok=True)
    taken = sorted(n for n in os.listdir(a.out) if n.startswith(a.tag + "."))
    if taken:
        raise SystemExit("%d file(s) of tag %s already in %s; nothing sent, nothing overwritten"
                         % (len(taken), a.tag, a.out))
    with C.tag_lock(a.out, a.tag) as mine:
        if not mine:
            raise SystemExit("another sender holds %s in this folder now; nothing sent" % a.tag)
        return run(a, key, home, brief_md5, rule)


def run(a, key, home, brief_md5, rule):
    guard = Guard(key)
    p = lambda ext: os.path.join(a.out, a.tag + ext)
    new = lambda path, text: write_new(path, guard(text))
    model = MODEL + ("[1m]" if a.context_1m else "")
    work = os.path.join(home, "work")
    os.makedirs(os.path.join(home, "config"), mode=0o700, exist_ok=True)
    os.makedirs(work, mode=0o700, exist_ok=True)
    env = child_env(key, home, model, a.base_url)
    argv = argv_for(model, a.effort)
    version = cli_version(env, work)
    user = C.read(a.brief)
    brief_rel = os.path.relpath(os.path.abspath(a.brief), C.REPO)
    request = {
        "tool": "Semantics/tools/glm_via_claude_code.py", "claude": CLAUDE, "claude_version": version,
        "argv": argv, "stdin": "the brief file, opened and given as standard input",
        "env": shown_env(env), "cwd": work, "model_requested": model, "effort": a.effort,
        "system_prompt_given": SYSTEM_PROMPT, "brief": brief_rel, "brief_md5": brief_md5,
        "brief_sha256": C.sha256(user), "brief_bytes": os.path.getsize(a.brief), "brief_words": C.words(user),
        "what_the_cli_sends": WHAT_THE_CLI_SENDS,
        "what_the_cli_sends_observed_for_this_version": version == CAPTURED_VERSION}
    new(p(".request.json"), json.dumps(request, indent=1, ensure_ascii=False))
    started, started_utc = time.time(), now()
    C.log("start %s: %s via Claude Code %s, effort %s, brief md5 %s, %d words"
          % (a.tag, model, version, a.effort, brief_md5, C.words(user)))
    history, rejects, accepted, o, why = [], 0, False, None, ""
    for n in range(1, a.attempts + 1):
        label = "%s attempt %d" % (a.tag, n)
        t0_utc = now()
        with C.provider_slot("glm", label=a.tag) as slot:
            C.log("%s: sent" % label)
            o = run_once(argv, env, work, a.brief, a.deadline, label)
        text = "".join(o["texts"]) if o["result"] is None else str(o["result"].get("result") or "")
        r = o["result"] or {}
        h = {"attempt": n, "started_utc": t0_utc, "ended_utc": now(), "seconds": o["seconds"],
             "slot": slot.get("slot"), "slot_wait_seconds": slot.get("waited_seconds"), "exit": o["exit"],
             "killed_at_deadline": o["killed"], "init": o["init"],
             "models_reported": sorted({x["model"] for x in o["assistant"] if x.get("model")}),
             "stop_reasons": [x["stop_reason"] for x in o["assistant"]],
             "result_subtype": r.get("subtype"), "is_error": r.get("is_error"),
             "api_error_status": r.get("api_error_status"), "duration_ms": r.get("duration_ms"),
             "duration_api_ms": r.get("duration_api_ms"), "num_turns": r.get("num_turns"),
             "usage": r.get("usage"), "other_events": o["other"][:20],
             "content_chars": len(text), "thinking_chars": sum(map(len, o["thinking"]))}
        cls, final = classify(o)
        if not cls:
            accepted, why = C.report_complete(text), ""
            if not accepted:
                why = "the last non-blank line does not carry %s" % C.SENTINEL
        if accepted:
            h.update(accepted=True, error_class=None)
            history.append(h)
            C.log("%s: accepted (%s s)" % (label, o["seconds"]))
            break
        new(p(".a%d.stdout.jsonl" % n), o["stdout"])
        new(p(".a%d.stderr.txt" % n), o["stderr"])
        if not cls:
            cls = "rejected_answer"
            rejects += 1
            h["rejected_because"] = why
            new(p(".a%d.truncated.txt" % n), text)
            if o["thinking"]:
                new(p(".a%d.reasoning.txt" % n), "\n\n".join(o["thinking"]))
        else:
            h["error"] = guard((str(r.get("result") or "") or o["stderr"])[:1500]) or None
        h.update(accepted=False, error_class=cls, final=final)
        history.append(h)
        C.log("%s: not accepted, %s (%s s)" % (label, cls, o["seconds"]))
        if final or n == a.attempts or rejects >= a.max_rejects:
            break
        wait = min(120, 10 * 2 ** n)
        C.log("%s: next attempt in %d s" % (label, wait))
        time.sleep(wait)

    r = (o and o["result"]) or {}
    text = "".join(o["texts"]) if o and o["result"] is None else str(r.get("result") or "")
    conn = sum(1 for h in history if h["error_class"] not in (None, "rejected_answer") and not h.get("final"))
    receipt = {
        "tool": "Semantics/tools/glm_via_claude_code.py", "provider": "glm (Z.ai) through Claude Code",
        "base_url": a.base_url, "claude_version": version,
        "what_the_cli_sends_observed_for_this_version": version == CAPTURED_VERSION,
        "model_requested": model, "model_reported": history[-1]["models_reported"] if history else [],
        "tag": a.tag, "accepted": accepted, "accept_rule": "the reply's last non-blank line carries END OF REPORT",
        "effort": a.effort, "effort_sent_as": {"thinking": {"type": "adaptive"}, "output_config": {"effort": a.effort}},
        "effort_note": "sent as observed; whether Z.ai acts on output_config.effort is not known",
        "max_output_tokens": int(MAX_OUTPUT_TOKENS), "api_timeout_ms": int(API_TIMEOUT_MS),
        "system_prompt_given": SYSTEM_PROMPT, "brief": os.path.relpath(os.path.abspath(a.brief), C.REPO),
        "brief_md5": brief_md5, "request_sha256": C.sha256(json.dumps(request, sort_keys=True)),
        "rule": rule and {"path": rule[0], "head_at_send": rule[1]},
        "usage": r.get("usage"), "model_usage_by_cli": r.get("modelUsage"),
        "usage_missing": not r.get("usage"), "cost_usd_estimated_by_cli": r.get("total_cost_usd"),
        "duration_ms": r.get("duration_ms"), "duration_api_ms": r.get("duration_api_ms"),
        "num_turns": r.get("num_turns"), "session_id": r.get("session_id"),
        "response_sha256": C.sha256(text), "response_chars": len(text),
        "reasoning_chars": sum(map(len, o["thinking"])) if o else 0,
        "attempts": len(history), "connection_failures": conn, "rejected_answers": rejects,
        "attempt_history": history, "started_utc": started_utc, "ended_utc": now(),
        "total_seconds": round(time.time() - started, 1)}
    if accepted:
        if o["thinking"]:
            new(p(".reasoning.txt"), "\n\n".join(o["thinking"]))
        receipt["key_found_in_output_and_replaced"] = guard.hits
        new(p(".receipt.json"), json.dumps(receipt, indent=1, ensure_ascii=False))
        new(p(".response.txt"), text)
        C.log("done: ok %s after %d attempt(s), %d connection failure(s), %s s, model reported %s"
              % (a.tag, len(history), conn, receipt["total_seconds"], ", ".join(receipt["model_reported"]) or "none"))
        return 0
    new(p(".error.txt"), "%s after %d attempt(s) (%d came back without the sentinel; %d connection failures)\n%s\n%s"
        % (history[-1]["error_class"] if history else "nothing ran", len(history), rejects, conn, why,
           (history[-1].get("error") or "") if history else ""))
    receipt["key_found_in_output_and_replaced"] = guard.hits
    new(p(".receipt.json"), json.dumps(receipt, indent=1, ensure_ascii=False))
    C.log("done: failed %s after %d attempt(s), %d connection failure(s), %d rejected answer(s), %s s"
          % (a.tag, len(history), conn, rejects, receipt["total_seconds"]))
    return 1


if __name__ == "__main__":
    sys.exit(main())
