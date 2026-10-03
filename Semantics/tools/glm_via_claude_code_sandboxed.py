#!/usr/bin/env python3
"""glm_via_claude_code_sandboxed.py: one call to GLM 5.3 (Z.ai) through Claude Code, WITH TOOLS, inside a sandbox folder
(round 3 of the review rounds, log S105; written 28 September 2026 by a Claude subagent for the orchestrator).

It is tools/glm_via_claude_code.py (decision S29: GLM only through Claude Code; decision S17: effort medium) with four
differences, and that file is imported, not changed: its callers get what they got before.

1. A sandbox. Each attempt runs in a fresh folder, <--sandbox-root>/<tag>.a<N>, in the scratchpad (refused inside the
   repository, inside ~/.claude, or outside SEMANTICS_RUN_DIR), holding only copies of the files a manifest names
   (--manifest: each file's source under Semantics/, its path in the sandbox and its md5, checked after the copy) and
   the brief itself as BRIEF.md. Before sending, every file in it is scanned: no symbolic link, no file holding the key
   or anything shaped like a key (the repository's key pattern). After the attempt, every file is compared with what
   was copied; the receipt says whether the sandbox came back unchanged. HOME, CLAUDE_CONFIG_DIR and TMPDIR of the child
   are a fresh folder <--home-root>/<tag>.a<N>, outside the sandbox, in the scratchpad, never ~/.claude.
2. Tools. Arguments: -p --model glm-5.3 --effort medium --restricted --tools Read,Glob,Grep,Bash
   --allowedTools "Read,Glob,Grep,Bash(python3 -m model.run:*)" --permission-mode dontAsk --permission-prompts none
   --settings {"includeGitInstructions":false} --system-prompt "" --output-format stream-json --verbose
   --no-session-persistence --strict-mcp-config --disable-slash-commands. --restricted confines Read, Glob and Grep to
   the working folder (the sandbox) and ignores user, project and local settings; dontAsk with no permission prompts
   refuses every tool use not allowed. CLAUDE_CODE_SIMPLE is not set (in simple mode Claude Code 2.1.283 offers no Glob
   or Grep); includeGitInstructions false drops the git-attribution reminder the CLI otherwise adds.
3. A second lock on commands. CLAUDE_CODE_SHELL_PREFIX is tools/glm_sandbox_shell_guard.py: every command the Bash
   tool would run is handed to it, and it runs none but `python3 -m model.run` with claim ids and numbers only (no
   shell), from the sandbox, with a clean environment that does not hold the key, and --no-write. Claude Code alone
   lets some read-only commands run in the working folder (cat, ls, ps -ef, ...) and a glob inside the allowed command;
   the guard refuses them. Every command handed to the guard is logged (<tag>.aN.guard.jsonl in the returns).
4. What is kept. The whole stream of every attempt (<tag>.aN.stdout.jsonl, accepted or not), the guard's log, and in
   the receipt each tool call (name, input, refused or not), the sandbox's manifest md5 and whether it came back
   unchanged. The init event must show exactly the tools Bash, Glob, Grep, Read, no MCP server, permission mode dontAsk
   and the sandbox as cwd; otherwise the attempt is stopped at once, as final, and nothing is accepted.

Tested before use (results/S105 Round 3 - how the replies will be read, written before sending.md, "Tools"): decoy runs
against a local stand-in server with a dummy token, and one real GLM call told to try each escape.
Everything else is as glm_via_claude_code.py: the key from GLM_API_KEY only into the child's ANTHROPIC_AUTH_TOKEN, a
guard replacing it in anything written, acceptance by END OF REPORT on the reply's last non-blank line, 6 attempts,
at most 3 answers without the sentinel, the retry rules, --rule and --brief-md5 (lesson S12), one "glm" provider slot
held per attempt (four at once from decision S39), a deadline per attempt that stops the child by its own PID. Files,
all under --tag in --out, never overwritten; on acceptance <tag>.response.txt is written last.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, threading, time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s80_common as C  # noqa: E402
import glm_via_claude_code as G  # noqa: E402
from s96_glm_call import check_rule, write_new  # noqa: E402

SEM = os.path.dirname(HERE)
GUARD = os.path.join(HERE, "glm_sandbox_shell_guard.py")
TOOLS = ["Bash", "Glob", "Grep", "Read"]
ALLOWED = "Read,Glob,Grep,Bash(python3 -m model.run:*)"
SETTINGS = '{"includeGitInstructions":false}'
KEY_SHAPES = re.compile(r"(sk-[A-Za-z0-9_-]{16,}|tp-[a-z0-9]{20,}|api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"
                        r"|[0-9a-f]{32}\.[A-Za-z0-9]{16})")


def argv_for(model, effort):
    return [G.CLAUDE, "-p", "--model", model, "--effort", effort, "--restricted", "--tools", "Read,Glob,Grep,Bash",
            "--allowedTools", ALLOWED, "--permission-mode", "dontAsk", "--permission-prompts", "none",
            "--settings", SETTINGS, "--system-prompt", G.SYSTEM_PROMPT, "--output-format", "stream-json", "--verbose",
            "--no-session-persistence", "--strict-mcp-config", "--disable-slash-commands"]


def child_env(key, home, model, base_url, sandbox, guard_log):
    env = G.child_env(key, home, model, base_url)
    env.pop("CLAUDE_CODE_SIMPLE", None)
    tmp = os.path.join(home, "tmp")
    env.update({"CLAUDE_CODE_SHELL_PREFIX": GUARD, "GLM_SANDBOX_DIR": sandbox, "GLM_SANDBOX_GUARD_LOG": guard_log,
                "GLM_SANDBOX_TMP": tmp, "TMPDIR": tmp, "PYTHONDONTWRITEBYTECODE": "1"})
    return env


def md5_bytes(b):
    return hashlib.md5(b).hexdigest()


def snapshot(root):
    out = {}
    for d, dirs, files in os.walk(root):
        for n in dirs + files:
            p = os.path.join(d, n)
            if os.path.islink(p):
                out[os.path.relpath(p, root)] = "symlink"
        for n in files:
            p = os.path.join(d, n)
            if not os.path.islink(p):
                with open(p, "rb") as f:
                    out[os.path.relpath(p, root)] = md5_bytes(f.read())
    return out


def build_sandbox(manifest, brief, sandbox, key):
    """Copy the manifest's files and the brief into a fresh folder; check every md5; scan for links and keys."""
    os.makedirs(sandbox, mode=0o700)
    for e in manifest["files"]:
        src = os.path.join(SEM, e["src"])
        dst = os.path.join(sandbox, e["path"])
        if not C._inside(src, SEM) or not C._inside(dst, sandbox) or os.path.islink(src):
            raise SystemExit("manifest entry %r lies outside Semantics/ or the sandbox, or is a link; nothing sent" % e)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
        if C.md5_file(dst) != e["md5"]:
            raise SystemExit("%s has md5 %s in the sandbox, the manifest gives %s; nothing sent"
                             % (e["src"], C.md5_file(dst), e["md5"]))
    shutil.copyfile(brief, os.path.join(sandbox, "BRIEF.md"))
    snap = snapshot(sandbox)
    for rel, h in snap.items():
        if h == "symlink":
            raise SystemExit("the sandbox holds a link, %s; nothing sent" % rel)
        with open(os.path.join(sandbox, rel), "rb") as f:
            data = f.read()
        if key and key.encode() in data:
            raise SystemExit("a file in the sandbox, %s, holds the key; nothing sent" % rel)
        if KEY_SHAPES.search(data.decode("utf-8", "replace")) or re.search(r"(\.env$|key)", rel, re.I):
            raise SystemExit("a file in the sandbox, %s, is or holds something shaped like a key; nothing sent" % rel)
    return snap


def init_problems(init, sandbox):
    bad = []
    if sorted(init.get("tools") or []) != TOOLS:
        bad.append("tools %s" % init.get("tools"))
    if init.get("mcp_servers"):
        bad.append("MCP servers %s" % init.get("mcp_servers"))
    if init.get("permissionMode") != "dontAsk":
        bad.append("permission mode %s" % init.get("permissionMode"))
    if os.path.realpath(init.get("cwd") or "/nonexistent") != os.path.realpath(sandbox):
        bad.append("cwd %s" % init.get("cwd"))
    return bad


def run_once(argv, env, cwd, brief, deadline, label):
    """One attempt, as glm_via_claude_code.run_once, plus: the init event is checked as it arrives (the child is stopped
    at once on a mismatch), and every tool call and its result are collected."""
    out = dict(stdout="", stderr="", exit=None, killed=False, init=None, assistant=[], result=None, other=[],
               texts=[], thinking=[], tool_calls=[], init_bad=None)
    calls = {}
    t0 = time.time()
    with open(brief, "rb") as fin:
        proc = subprocess.Popen(argv, stdin=fin, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env, cwd=cwd)
    err_chunks = []
    t_err = threading.Thread(target=lambda: err_chunks.append(proc.stderr.read()), daemon=True)
    t_err.start()
    done = threading.Event()
    lines = []

    def watchdog():
        next_note = t0 + G.PROGRESS_EVERY
        while not done.wait(5):
            if time.time() - t0 > deadline and proc.poll() is None:
                out["killed"] = True
                proc.kill()   # the child this tool started, by its own PID
                return
            if time.time() > next_note:
                C.log("%s: still running, %d s, %d event(s), %d tool call(s)"
                      % (label, time.time() - t0, len(lines), len(calls)))
                next_note += G.PROGRESS_EVERY
    threading.Thread(target=watchdog, daemon=True).start()
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
            bad = init_problems(out["init"], cwd)
            if bad:
                out["init_bad"] = bad
                proc.kill()   # the child this tool started, by its own PID
        elif typ == "assistant":
            m = d.get("message") or {}
            out["assistant"].append({"model": m.get("model"), "id": m.get("id"), "stop_reason": m.get("stop_reason"),
                                     "usage": m.get("usage")})
            for b in m.get("content") or []:
                if b.get("type") == "text":
                    out["texts"].append(b.get("text") or "")
                elif b.get("type") == "thinking":
                    out["thinking"].append(b.get("thinking") or "")
                elif b.get("type") == "tool_use":
                    calls[b.get("id")] = {"name": b.get("name"),
                                          "input": json.dumps(b.get("input"), ensure_ascii=False)[:400],
                                          "refused_or_error": None, "result_head": None}
                    out["tool_calls"].append(calls[b.get("id")])
        elif typ == "user":
            for b in (d.get("message") or {}).get("content") or []:
                if isinstance(b, dict) and b.get("type") == "tool_result" and b.get("tool_use_id") in calls:
                    c = b.get("content")
                    if isinstance(c, list):
                        c = " ".join(x.get("text", "") for x in c if isinstance(x, dict))
                    calls[b["tool_use_id"]].update(refused_or_error=bool(b.get("is_error")),
                                                   result_head=str(c)[:200])
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
    if o["init_bad"]:
        return "sandbox_init_mismatch", True
    o2 = dict(o, init=(dict(o["init"], tools=[], mcp_servers=[]) if o["init"] else None))
    return G.classify(o2)


def fresh_dir(root, name, what):
    path = os.path.join(root, name)
    if os.path.exists(path):
        raise SystemExit("%s %s exists already; nothing sent, nothing overwritten" % (what, path))
    return path


def check_root(path, what):
    path = os.path.abspath(path)
    if (G.inside(path, C.REPO) or G.inside(path, "/root/.claude") or G.inside(os.path.expanduser("~/.claude"), path)
            or not G.inside(path, C.RUN_DIR)):
        raise SystemExit("%s %s is inside the repository or ~/.claude, or outside %s; nothing sent"
                         % (what, path, C.RUN_DIR))
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--brief", required=True, help="the file sent, whole, as the one prompt (also BRIEF.md in the sandbox)")
    ap.add_argument("--manifest", required=True, help="JSON: the files copied into the sandbox, with their md5s")
    ap.add_argument("--manifest-md5", help="refuse unless the manifest has this md5")
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True, help="the folder the files go to")
    ap.add_argument("--effort", default="medium", choices=G.EFFORTS, help="medium: the owner's rule (decision S17)")
    ap.add_argument("--context-1m", action="store_true", help='send the model as "glm-5.3[1m]" (1,000,000-token window)')
    ap.add_argument("--attempts", type=int, default=6)
    ap.add_argument("--max-rejects", type=int, default=3)
    ap.add_argument("--deadline", type=int, default=7200, help="seconds of wall clock per attempt")
    ap.add_argument("--sandbox-root", default=os.path.join(C.RUN_DIR, "glm_sandboxes"))
    ap.add_argument("--home-root", default=os.path.join(C.RUN_DIR, "glm_sandbox_homes"))
    ap.add_argument("--base-url", default=G.BASE_URL, help="only for a test against a local stand-in server")
    ap.add_argument("--rule", help="the note written before sending; must be committed and unchanged")
    ap.add_argument("--brief-md5", help="refuse unless the brief has this md5")
    a = ap.parse_args()

    sroot = check_root(a.sandbox_root, "--sandbox-root")
    hroot = check_root(a.home_root, "--home-root")
    if G.inside(sroot, hroot) or G.inside(hroot, sroot):
        raise SystemExit("the sandbox root and the home root overlap; nothing sent")
    key = os.environ.get(G.KEYNAME)
    if not key:
        raise SystemExit("%s is not set in the environment; nothing sent" % G.KEYNAME)
    for exe in (G.CLAUDE, GUARD):
        if not os.access(exe, os.X_OK):
            raise SystemExit("%s is not there or not executable; nothing sent" % exe)
    brief_md5 = C.md5_file(a.brief)
    if a.brief_md5 and brief_md5 != a.brief_md5:
        raise SystemExit("the brief has md5 %s, expected %s; nothing sent" % (brief_md5, a.brief_md5))
    man_md5 = C.md5_file(a.manifest)
    if a.manifest_md5 and man_md5 != a.manifest_md5:
        raise SystemExit("the manifest has md5 %s, expected %s; nothing sent" % (man_md5, a.manifest_md5))
    manifest = json.loads(C.read(a.manifest))
    rule = check_rule(a.rule) if a.rule else None
    os.makedirs(a.out, exist_ok=True)
    taken = sorted(n for n in os.listdir(a.out) if n.startswith(a.tag + "."))
    if taken:
        raise SystemExit("%d file(s) of tag %s already in %s; nothing sent, nothing overwritten"
                         % (len(taken), a.tag, a.out))
    with C.tag_lock(a.out, a.tag) as mine:
        if not mine:
            raise SystemExit("another sender holds %s in this folder now; nothing sent" % a.tag)
        return run(a, key, sroot, hroot, brief_md5, man_md5, manifest, rule)


def run(a, key, sroot, hroot, brief_md5, man_md5, manifest, rule):
    guard = G.Guard(key)
    p = lambda ext: os.path.join(a.out, a.tag + ext)
    new = lambda path, text: write_new(path, guard(text))
    model = G.MODEL + ("[1m]" if a.context_1m else "")
    argv = argv_for(model, a.effort)
    user = C.read(a.brief)
    probe_home = fresh_dir(hroot, a.tag + ".version", "home")
    os.makedirs(os.path.join(probe_home, "config"), mode=0o700)
    version = G.cli_version(G.child_env(key, probe_home, model, a.base_url), probe_home)
    request = {
        "tool": "Semantics/tools/glm_via_claude_code_sandboxed.py", "claude": G.CLAUDE, "claude_version": version,
        "argv": argv, "stdin": "the brief file, opened and given as standard input",
        "env": G.shown_env(child_env(key, "<home of the attempt>", model, a.base_url, "<sandbox of the attempt>",
                                     "<home of the attempt>/guard.jsonl")),
        "sandbox": os.path.join(sroot, a.tag + ".a<N>"), "home": os.path.join(hroot, a.tag + ".a<N>"),
        "manifest": os.path.relpath(os.path.abspath(a.manifest), C.REPO), "manifest_md5": man_md5,
        "manifest_files": len(manifest["files"]), "guard": os.path.relpath(GUARD, C.REPO),
        "guard_md5": C.md5_file(GUARD), "model_requested": model, "effort": a.effort,
        "system_prompt_given": G.SYSTEM_PROMPT, "brief": os.path.relpath(os.path.abspath(a.brief), C.REPO),
        "brief_md5": brief_md5, "brief_sha256": C.sha256(user), "brief_bytes": os.path.getsize(a.brief),
        "brief_words": C.words(user), "deadline_seconds": a.deadline, "base_url": a.base_url}
    new(p(".request.json"), json.dumps(request, indent=1, ensure_ascii=False))
    started, started_utc = time.time(), G.now()
    C.log("start %s: %s via Claude Code %s, sandboxed, effort %s, brief md5 %s, %d words, %d sandbox files"
          % (a.tag, model, version, a.effort, brief_md5, C.words(user), len(manifest["files"]) + 1))
    history, rejects, accepted, o, why = [], 0, False, None, ""
    for n in range(1, a.attempts + 1):
        label = "%s attempt %d" % (a.tag, n)
        sandbox = fresh_dir(sroot, "%s.a%d" % (a.tag, n), "sandbox")
        home = fresh_dir(hroot, "%s.a%d" % (a.tag, n), "home")
        snap = build_sandbox(manifest, a.brief, sandbox, key)
        os.makedirs(os.path.join(home, "config"), mode=0o700)
        os.makedirs(os.path.join(home, "tmp"), mode=0o700)
        glog = os.path.join(home, "guard.jsonl")
        env = child_env(key, home, model, a.base_url, sandbox, glog)
        t0_utc = G.now()
        with C.provider_slot("glm", label=a.tag) as slot:
            C.log("%s: sent" % label)
            o = run_once(argv, env, sandbox, a.brief, a.deadline, label)
        after = snapshot(sandbox)
        changed = sorted(k for k in set(snap) | set(after) if snap.get(k) != after.get(k))
        guard_lines = C.read(glog).splitlines() if os.path.exists(glog) else []
        decisions = [json.loads(x).get("decision") for x in guard_lines if x.strip()]
        text = "".join(o["texts"]) if o["result"] is None else str(o["result"].get("result") or "")
        r = o["result"] or {}
        tc = o["tool_calls"]
        h = {"attempt": n, "started_utc": t0_utc, "ended_utc": G.now(), "seconds": o["seconds"],
             "slot": slot.get("slot"), "slot_wait_seconds": slot.get("waited_seconds"), "exit": o["exit"],
             "killed_at_deadline": o["killed"], "init": o["init"], "init_problems": o["init_bad"],
             "sandbox": sandbox, "sandbox_files": len(snap), "sandbox_unchanged": not changed,
             "sandbox_changes": changed[:50],
             "tool_calls_by_name": {k: sum(1 for c in tc if c["name"] == k) for k in sorted({c["name"] for c in tc})},
             "tool_calls_refused_or_error": sum(1 for c in tc if c["refused_or_error"]),
             "guard_commands_run": decisions.count("run"), "guard_commands_refused": decisions.count("refused"),
             "tool_calls": tc[:400],
             "models_reported": sorted({x["model"] for x in o["assistant"] if x.get("model")}),
             "stop_reasons": [x["stop_reason"] for x in o["assistant"]][-20:],
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
        new(p(".a%d.stdout.jsonl" % n), o["stdout"])
        new(p(".a%d.guard.jsonl" % n), "\n".join(guard_lines) + ("\n" if guard_lines else ""))
        if accepted:
            h.update(accepted=True, error_class=None)
            history.append(h)
            C.log("%s: accepted (%s s, %d tool call(s), sandbox unchanged: %s)"
                  % (label, o["seconds"], len(tc), not changed))
            break
        new(p(".a%d.stderr.txt" % n), o["stderr"])
        if not cls:
            cls = "rejected_answer"
            rejects += 1
            h["rejected_because"] = why
            new(p(".a%d.truncated.txt" % n), text)
            if o["thinking"]:
                new(p(".a%d.reasoning.txt" % n), "\n\n".join(o["thinking"]))
        else:
            h["error"] = guard((str(r.get("result") or "") or o["stderr"] or
                                ("; ".join(o["init_bad"]) if o["init_bad"] else ""))[:1500]) or None
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
        "tool": "Semantics/tools/glm_via_claude_code_sandboxed.py", "provider": "glm (Z.ai) through Claude Code",
        "base_url": a.base_url, "claude_version": version, "model_requested": model,
        "model_reported": history[-1]["models_reported"] if history else [], "tag": a.tag, "accepted": accepted,
        "accept_rule": "the reply's last non-blank line carries END OF REPORT", "effort": a.effort,
        "tools": TOOLS, "allowed": ALLOWED, "guard": os.path.relpath(GUARD, C.REPO), "guard_md5": C.md5_file(GUARD),
        "manifest": os.path.relpath(os.path.abspath(a.manifest), C.REPO), "manifest_md5": man_md5,
        "max_output_tokens": int(G.MAX_OUTPUT_TOKENS), "api_timeout_ms": int(G.API_TIMEOUT_MS),
        "system_prompt_given": G.SYSTEM_PROMPT, "brief": os.path.relpath(os.path.abspath(a.brief), C.REPO),
        "brief_md5": brief_md5, "request_sha256": C.sha256(json.dumps(request, sort_keys=True)),
        "rule": rule and {"path": rule[0], "head_at_send": rule[1]},
        "usage": r.get("usage"), "model_usage_by_cli": r.get("modelUsage"), "usage_missing": not r.get("usage"),
        "cost_usd_estimated_by_cli": r.get("total_cost_usd"), "duration_ms": r.get("duration_ms"),
        "duration_api_ms": r.get("duration_api_ms"), "num_turns": r.get("num_turns"),
        "session_id": r.get("session_id"), "response_sha256": C.sha256(text), "response_chars": len(text),
        "reasoning_chars": sum(map(len, o["thinking"])) if o else 0, "attempts": len(history),
        "connection_failures": conn, "rejected_answers": rejects, "attempt_history": history,
        "started_utc": started_utc, "ended_utc": G.now(), "total_seconds": round(time.time() - started, 1)}
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
