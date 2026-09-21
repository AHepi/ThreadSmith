"""Plan 49, phases 1 and 2: send a source to DeepSeek V4.1 Flash under one of three modes.
The key is read from the environment and is written to no file.

  DEEPSEEK_API_KEY=... python3 run.py --pilot          # 3 sources x 3 modes = 9 runs
  DEEPSEEK_API_KEY=... python3 run.py --all            # every source x modes 0,1,2
  DEEPSEEK_API_KEY=... python3 run.py S7:2             # one run
  DEEPSEEK_API_KEY=... python3 run.py P3:1:1 P3:1:2     # repeat runs (plan H56): a third field k
                                                       #   writes runs_repeat/<sid>-m<mode>-r<k>.json
  python3 run.py --dry P3:1:1                           # sends nothing: checks skill, corpus, paths

Patch (plan H58): SKILL_FILE=31 in the environment selects authority/31/, the copy skill_31/, and runs_repeat_31/.
Patch (plan H56): repeat runs go to runs_repeat/ so the skip rule never hides a repeat behind an original;
the skill copy is diffed against ../../authority/hard-to-vary before any call (Lesson 44, now in code);
--dry runs every check and sends nothing. Gives up nothing: a job with no k runs exactly as before.

Modes. 0: no skill, a bare instruction (the fair rival). 1: the whole skill in the system message.
2: SKILL.md only, with a tool the reader calls to open a reference file, so the router is live.
Resumable: a run whose file exists is skipped. Ten at a time, as the service allows.
"""
import os, sys, json, time, re, threading, filecmp, concurrent.futures as cf
try:
    import requests
except ImportError:
    requests = None

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"
EFFORT = "high"
MAX_TOKENS = 24000
MAX_TOOL_CALLS = 12
SKILL_FILE = os.environ.get("SKILL_FILE", "30")          # plan H58: SKILL_FILE=31 selects authority/31/
_SUF = "" if SKILL_FILE == "30" else f"_{SKILL_FILE}"
SKILL = f"{HERE}/skill{_SUF}/hard-to-vary"
AUTHORITY = os.path.normpath(f"{HERE}/../../authority/hard-to-vary" if SKILL_FILE == "30"
                             else f"{HERE}/../../authority/{SKILL_FILE}/hard-to-vary")
MODULES = ["the-idea-in-depth", "question-bank", "by-domain", "building",
           "testing-against-cases", "reporting", "word-list"]

FRAMING = ("Below is a method for judging whether an explanation holds up. It is the tool. "
  "The document that follows in the next message is the thing to judge. Work through the method's "
  "procedure on that document: freeze the question the document answers (where it answers several, "
  "take the one its title or opening makes central, and say so); list the jobs and the parts; write "
  "the change list; run the tests; say where each part came from; then write the report in the form "
  "the method gives, with one of the method's marks on every part. Use everyday words and concrete "
  "changes. Keep the report under 1,200 words. Where the method refers to a source theory that is "
  "not supplied, work from the method's own words.\n\n")

BARE = ("The document in the next message gives an explanation. Judge whether its explanation holds up. "
  "Say which parts do the work, which are loose, and what would test it. Keep your reply under 1,200 words.")

def check_skill():
    """The copy sent to the reader must be file 30 exactly (Lesson 44)."""
    if not os.path.isdir(SKILL):
        raise SystemExit(f"no skill copy at {SKILL}; copy {AUTHORITY} there first. Nothing sent.")
    files = ["SKILL.md"] + [f"references/{m}.md" for m in MODULES]
    bad = [f for f in files if not filecmp.cmp(f"{SKILL}/{f}", f"{AUTHORITY}/{f}", shallow=False)]
    if bad:
        raise SystemExit(f"skill copy differs from authority in {bad}. Nothing sent.")
    return files

def out_path(sid, mode, k=None):
    if k is None:
        return f"{HERE}/runs/{sid}-m{mode}.json"
    os.makedirs(f"{HERE}/runs_repeat{_SUF}", exist_ok=True)
    return f"{HERE}/runs_repeat{_SUF}/{sid}-m{mode}-r{k}.json"

def module_text(name):
    return open(f"{SKILL}/references/{name}.md", encoding="utf-8").read()

def skill_all():
    out = [f"=== FILE: hard-to-vary/SKILL.md ===\n{open(f'{SKILL}/SKILL.md',encoding='utf-8').read().strip()}\n"]
    for m in MODULES:
        out.append(f"=== FILE: hard-to-vary/references/{m}.md ===\n{module_text(m).strip()}\n")
    return "\n".join(out)

def source_text(sid):
    t = open(f"{HERE}/corpus/{sid}.txt", encoding="utf-8").read()
    return t.split("\n\n", 1)[1].strip()          # provenance header stripped; never sent

TOOL = [{"type": "function", "function": {
    "name": "open_module",
    "description": ("Open one of this method's reference files and return its text. "
                    "The method's own table and map say which file to open and when."),
    "parameters": {"type": "object", "properties": {
        "name": {"type": "string", "enum": MODULES,
                 "description": "the reference file to open, without the .md"}},
        "required": ["name"]}}}]

_lock = threading.Lock()

def post(body, key, tag):
    """Streamed request. Returns a message dict {content, reasoning_content, tool_calls}, the finish reason,
    and usage. Streaming captures partial output and the finish reason even when the service ends early."""
    delay = 4
    body = dict(body, stream=True, stream_options={"include_usage": True})
    for attempt in range(7):
        try:
            r = requests.post(URL, json=body, timeout=(30, 900), stream=True,
                              headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
            if r.status_code in (400, 401, 402):
                raise SystemExit(f"{tag}: stopped, HTTP {r.status_code} {r.text[:300]}")
            if r.status_code != 200:
                raise RuntimeError(f"HTTP {r.status_code} {r.text[:160]}")
            content, reasoning, finish, usage = [], [], None, {}
            tcs = {}
            for raw in r.iter_lines():
                if not raw: continue
                line = raw.decode("utf-8", "ignore")
                if not line.startswith("data:"): continue
                data = line[5:].strip()
                if data == "[DONE]": break
                ch = json.loads(data)
                if ch.get("usage"): usage = ch["usage"]
                for c in ch.get("choices", []):
                    d = c.get("delta", {}) or {}
                    if d.get("content"): content.append(d["content"])
                    if d.get("reasoning_content"): reasoning.append(d["reasoning_content"])
                    for tc in d.get("tool_calls") or []:
                        i = tc.get("index", 0)
                        slot = tcs.setdefault(i, {"id": "", "type": "function", "function": {"name": "", "arguments": ""}})
                        if tc.get("id"): slot["id"] = tc["id"]
                        f = tc.get("function") or {}
                        if f.get("name"): slot["function"]["name"] += f["name"]
                        if f.get("arguments"): slot["function"]["arguments"] += f["arguments"]
                    if c.get("finish_reason"): finish = c["finish_reason"]
            msg = {"content": "".join(content), "reasoning_content": "".join(reasoning),
                   "tool_calls": [tcs[i] for i in sorted(tcs)] or None}
            return msg, finish, usage
        except SystemExit:
            raise
        except Exception as e:
            err = repr(e)[:160]
        with _lock: print(f"  {tag}: retry after {err}", file=sys.stderr, flush=True)
        time.sleep(delay); delay = min(delay * 2, 90)
    raise RuntimeError(f"{tag}: gave up, {err}")

def do_run(sid, mode, key, k=None):
    tag = f"{sid}:{mode}" + (f":r{k}" if k else "")
    out = out_path(sid, mode, k)
    if os.path.exists(out): return "skip"
    t0 = time.time()
    paper = source_text(sid)
    if mode == 0:
        sysmsg = BARE
    elif mode == 1:
        sysmsg = FRAMING + skill_all()
    else:
        sysmsg = FRAMING + f"=== FILE: hard-to-vary/SKILL.md ===\n{open(f'{SKILL}/SKILL.md',encoding='utf-8').read().strip()}\n"
    messages = [{"role": "system", "content": sysmsg}, {"role": "user", "content": paper}]
    body = {"model": MODEL, "messages": messages, "stream": False, "max_tokens": MAX_TOKENS,
            "thinking": {"type": "enabled"}, "reasoning_effort": EFFORT}
    opened, usages, calls, finishes, attempts = [], [], 0, [], 0
    if mode == 2:
        body["tools"] = TOOL
    while True:
        msg, finish, usage = post(body, key, tag)
        usages.append(usage or {}); finishes.append(finish)
        tcs = msg.get("tool_calls") or []
        if not tcs and not (msg.get("content") or "").strip() and finish != "length" and attempts == 0:
            attempts += 1
            with _lock: print(f"  {tag}: empty reply (finish {finish!r}); one automatic retry", file=sys.stderr, flush=True)
            continue
        if mode == 2 and tcs and calls < MAX_TOOL_CALLS:
            body["messages"].append({"role": "assistant", "content": msg.get("content") or "",
                                     "reasoning_content": msg.get("reasoning_content") or "",
                                     "tool_calls": tcs})
            for tc in tcs:
                calls += 1
                try:
                    name = json.loads(tc["function"]["arguments"]).get("name", "")
                except Exception:
                    name = ""
                text = module_text(name) if name in MODULES else f"no file named {name!r}"
                opened.append(name or "?")
                body["messages"].append({"role": "tool", "tool_call_id": tc["id"], "content": text})
            continue
        break
    rec = {"source": sid, "mode": mode, "repeat": k, "skill_file": SKILL_FILE, "model": MODEL, "effort": EFFORT,
           "reply": msg.get("content", ""), "reasoning": msg.get("reasoning_content", ""),
           "modules_opened": opened, "tool_calls": calls, "finish_reasons": finishes,
           "automatic_retries": attempts,
           "usage_total": {k: sum(u.get(k, 0) for u in usages)
                           for k in ("prompt_tokens", "completion_tokens", "prompt_cache_hit_tokens",
                                     "prompt_cache_miss_tokens", "total_tokens")},
           "api_calls": len(usages), "seconds": round(time.time() - t0, 1),
           "finished_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    tmp = out + ".tmp"
    json.dump(rec, open(tmp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    os.replace(tmp, out)
    return "done"

def cost_so_far():
    hit = miss = outt = 0
    for fn in os.listdir(f"{HERE}/runs"):
        if not fn.endswith(".json"): continue
        u = json.load(open(f"{HERE}/runs/{fn}", encoding="utf-8"))["usage_total"]
        hit += u.get("prompt_cache_hit_tokens", 0)
        miss += u.get("prompt_cache_miss_tokens", 0) or (u.get("prompt_tokens", 0) - u.get("prompt_cache_hit_tokens", 0))
        outt += u.get("completion_tokens", 0)
    return hit, miss, outt, hit/1e6*0.003 + miss/1e6*0.15 + outt/1e6*0.6

if __name__ == "__main__":
    args = sys.argv[1:]
    dry = "--dry" in args
    key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not key and not dry: raise SystemExit("DEEPSEEK_API_KEY not set. Nothing sent.")
    srcs = [s["id"] for s in json.load(open(f"{HERE}/sources.json"))]
    if "--pilot" in args:
        jobs = [(s, m, None) for s in ("S7", "F1", "R1") for m in (0, 1, 2)]
    elif "--all" in args:
        jobs = [(s, m, None) for s in srcs for m in (0, 1, 2)]
    else:
        jobs = []
        for a in args:
            if ":" in a:
                parts = a.split(":")
                jobs.append((parts[0], int(parts[1]), int(parts[2]) if len(parts) > 2 else None))
    files = check_skill()
    print(f"skill copy checked against authority (file {SKILL_FILE}): {len(files)} files identical")
    for s, m, k in jobs:
        if s not in srcs: raise SystemExit(f"unknown source {s}. Nothing sent.")
        if not os.path.exists(f"{HERE}/corpus/{s}.txt"): raise SystemExit(f"no corpus text for {s}; run fetch.py {s}. Nothing sent.")
    if dry:
        for s, m, k in jobs:
            out = out_path(s, m, k)
            print(f"  would run {s} mode {m}" + (f" repeat {k}" if k else "") +
                  f" ({len(source_text(s).split())} words) -> {os.path.relpath(out, HERE)}" +
                  (" [exists, would skip]" if os.path.exists(out) else ""))
        raise SystemExit("dry run: nothing sent.")
    if requests is None: raise SystemExit("the requests package is not installed. Nothing sent.")
    print(f"{len(jobs)} runs; model {MODEL}, effort {EFFORT}")
    done = 0
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(do_run, s, m, key, k): (s, m, k) for s, m, k in jobs}
        for f in cf.as_completed(futs):
            s, m, k = futs[f]
            res = f.result(); done += 1
            print(f"  [{done}/{len(jobs)}] {s} mode {m}" + (f" repeat {k}" if k else "") + f": {res}", flush=True)
    h, mi, o, usd = cost_so_far()
    print(f"\ntokens: cache-hit {h:,}, cache-miss {mi:,}, out {o:,}  ->  about ${usd:.2f} at off-peak prices")
