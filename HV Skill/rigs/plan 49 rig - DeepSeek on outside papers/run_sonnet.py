"""Plan H56, second reader: send a source to Claude Sonnet 5 under mode 1 or 2, same framing as run.py.
The key is read from the environment (ANTHROPIC_API_KEY) and is written to no file.

  ANTHROPIC_API_KEY=... python3 run_sonnet.py P3:1:1 P3:1:2 ...   # writes runs_sonnet5/<sid>-m<mode>-r<k>.json
  python3 run_sonnet.py --dry P3:1:1                              # sends nothing: checks skill, corpus, paths

Same modes as run.py (1: skill pasted whole in the system prompt; 2: SKILL.md only, with the open_module tool
so the router is live). Mode 0 is accepted but not part of plan H56. Adaptive thinking with the summary kept,
effort high, ceiling 24,000 as in plan 49, streamed. Resumable: a run whose file exists is skipped.
"""
import os, sys, json, time, threading, concurrent.futures as cf
from run import (HERE, MODULES, FRAMING, BARE, MAX_TOKENS, MAX_TOOL_CALLS, SKILL,
                 skill_all, module_text, source_text, check_skill)

MODEL = "claude-sonnet-5"
EFFORT = "high"
TOOLS = [{"name": "open_module",
          "description": ("Open one of this method's reference files and return its text. "
                          "The method's own table and map say which file to open and when."),
          "input_schema": {"type": "object", "properties": {
              "name": {"type": "string", "enum": MODULES,
                       "description": "the reference file to open, without the .md"}},
              "required": ["name"], "additionalProperties": False},
          "strict": True}]
_lock = threading.Lock()

def out_path(sid, mode, k):
    os.makedirs(f"{HERE}/runs_sonnet5", exist_ok=True)
    return f"{HERE}/runs_sonnet5/{sid}-m{mode}-r{k}.json"

def do_run(client, sid, mode, k):
    tag = f"{sid}:{mode}:r{k}"
    out = out_path(sid, mode, k)
    if os.path.exists(out): return "skip"
    t0 = time.time()
    paper = source_text(sid)
    if mode == 0:
        sysmsg = BARE
    elif mode == 1:
        sysmsg = FRAMING + skill_all()
    else:
        sysmsg = FRAMING + f"=== FILE: hard-to-vary/SKILL.md ===\n{open(f'{SKILL}/SKILL.md', encoding='utf-8').read().strip()}\n"
    messages = [{"role": "user", "content": paper}]
    kwargs = dict(model=MODEL, max_tokens=MAX_TOKENS, system=sysmsg, messages=messages,
                  thinking={"type": "adaptive", "display": "summarized"},
                  output_config={"effort": EFFORT})
    if mode == 2:
        kwargs["tools"] = TOOLS
    opened, usages, stops, calls, texts, thinking = [], [], [], 0, [], []
    while True:
        with client.messages.stream(**kwargs) as stream:
            resp = stream.get_final_message()
        usages.append(resp.usage.model_dump()); stops.append(resp.stop_reason)
        for b in resp.content:
            if b.type == "thinking" and b.thinking: thinking.append(b.thinking)
            elif b.type == "text": texts.append(b.text)
        tool_uses = [b for b in resp.content if b.type == "tool_use"]
        if resp.stop_reason == "tool_use" and tool_uses and mode == 2 and calls < MAX_TOOL_CALLS:
            messages.append({"role": "assistant", "content": resp.content})
            results = []
            for tu in tool_uses:
                calls += 1
                name = (tu.input or {}).get("name", "")
                text = module_text(name) if name in MODULES else f"no file named {name!r}"
                opened.append(name or "?")
                results.append({"type": "tool_result", "tool_use_id": tu.id, "content": text})
            messages.append({"role": "user", "content": results})
            continue
        if resp.stop_reason == "pause_turn":
            messages.append({"role": "assistant", "content": resp.content})
            continue
        break
    rec = {"source": sid, "mode": mode, "repeat": k, "model": MODEL, "effort": EFFORT,
           "reply": "\n".join(texts), "reasoning": "\n\n".join(thinking), "reasoning_is_summary": True,
           "modules_opened": opened, "tool_calls": calls, "finish_reasons": stops,
           "usage_total": {kk: sum((u.get(kk) or 0) for u in usages)
                           for kk in ("input_tokens", "output_tokens", "cache_read_input_tokens",
                                      "cache_creation_input_tokens")},
           "api_calls": len(usages), "seconds": round(time.time() - t0, 1),
           "finished_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    tmp = out + ".tmp"
    json.dump(rec, open(tmp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    os.replace(tmp, out)
    return "done"

if __name__ == "__main__":
    args = sys.argv[1:]
    dry = "--dry" in args
    jobs = []
    for a in args:
        if ":" in a:
            s, m, k = a.split(":"); jobs.append((s, int(m), int(k)))
    files = check_skill()
    print(f"skill copy checked against authority: {len(files)} files identical")
    for s, m, k in jobs:
        if not os.path.exists(f"{HERE}/corpus/{s}.txt"): raise SystemExit(f"no corpus text for {s}; run fetch.py {s}. Nothing sent.")
    if dry:
        for s, m, k in jobs:
            out = out_path(s, m, k)
            print(f"  would run {s} mode {m} repeat {k} ({len(source_text(s).split())} words) -> "
                  f"{os.path.relpath(out, HERE)}" + (" [exists, would skip]" if os.path.exists(out) else ""))
        raise SystemExit("dry run: nothing sent.")
    import anthropic
    if not os.environ.get("ANTHROPIC_API_KEY"): raise SystemExit("ANTHROPIC_API_KEY not set. Nothing sent.")
    client = anthropic.Anthropic()
    print(f"{len(jobs)} runs; model {MODEL}, effort {EFFORT}")
    done = 0
    with cf.ThreadPoolExecutor(max_workers=6) as ex:
        futs = {ex.submit(do_run, client, s, m, k): (s, m, k) for s, m, k in jobs}
        for f in cf.as_completed(futs):
            s, m, k = futs[f]
            try:
                res = f.result()
            except Exception as e:
                res = f"FAILED {type(e).__name__}: {str(e)[:200]}"
            done += 1
            print(f"  [{done}/{len(jobs)}] {s} mode {m} repeat {k}: {res}", flush=True)
