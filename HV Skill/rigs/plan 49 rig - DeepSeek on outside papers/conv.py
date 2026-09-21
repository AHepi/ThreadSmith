"""Plan 49, phase 3: conversation mode. Two DeepSeek sessions. The reader holds SKILL.md and the open_module tool
(as mode 2) and questions the author. The author holds the document and defends it honestly, without the skill.
Six exchanges, then the reader writes its report. The key is read from the environment and written to no file.

  DEEPSEEK_API_KEY=... python3 conv.py C2 D1 ...      # named sources
"""
import os, sys, json, time, threading, concurrent.futures as cf
from run import post, module_text, source_text, TOOL, MODULES, SKILL, MAX_TOKENS, MODEL, EFFORT, FRAMING, _lock

HERE = os.path.dirname(os.path.abspath(__file__))
EXCHANGES = 6
MAX_TOOL_CALLS = 12

READER_SYS = (FRAMING.replace(
    "The document that follows in the next message is the thing to judge.",
    "The document that follows in the next message is the thing to judge, and its author is here to answer "
    "questions about it.")
  + "Conversation first, report after. You have six turns to question the author; each message you write goes "
    "straight to the author, so put your questions in it and nothing else, one or two questions at a time, in "
    "the way the method's 'How to ask' section describes. When you are told the conversation is over, write "
    "the report.\n\n"
  + f"=== FILE: hard-to-vary/SKILL.md ===\n{open(f'{SKILL}/SKILL.md', encoding='utf-8').read().strip()}\n")

AUTHOR_SYS = ("You are the author of the document below. A careful reader will ask you questions about it. "
  "Answer as its author would: honestly, defending what you believe and conceding what you must, from the "
  "document and from what you know of the subject. Where you do not know, say so; invent no evidence. "
  "Keep each answer under 250 words.\n\n=== THE DOCUMENT ===\n")

def reader_turn(messages, key, tag, state):
    """One reader turn, with the module tool available. Returns the reader's text."""
    body = {"model": MODEL, "messages": messages, "max_tokens": MAX_TOKENS,
            "thinking": {"type": "enabled"}, "reasoning_effort": EFFORT, "tools": TOOL}
    empties = 0
    while True:
        msg, finish, usage = post(body, key, tag)
        state["usages"].append(usage or {}); state["finishes"].append(finish); state["calls"] += 1
        tcs = msg.get("tool_calls") or []
        if tcs and state["tool_calls"] < MAX_TOOL_CALLS:
            messages.append({"role": "assistant", "content": msg.get("content") or "",
                             "reasoning_content": msg.get("reasoning_content") or "", "tool_calls": tcs})
            for tc in tcs:
                state["tool_calls"] += 1
                try: name = json.loads(tc["function"]["arguments"]).get("name", "")
                except Exception: name = ""
                state["opened"].append(name or "?")
                messages.append({"role": "tool", "tool_call_id": tc["id"],
                                 "content": module_text(name) if name in MODULES else f"no file named {name!r}"})
            continue
        text = (msg.get("content") or "").strip()
        if not text and finish != "length" and empties == 0:
            empties += 1; state["auto_retries"] += 1; continue
        messages.append({"role": "assistant", "content": text, "reasoning_content": msg.get("reasoning_content") or ""})
        return text

def author_turn(messages, key, tag, state):
    body = {"model": MODEL, "messages": messages, "max_tokens": 6000,
            "thinking": {"type": "enabled"}, "reasoning_effort": EFFORT}
    msg, finish, usage = post(body, key, tag)
    state["usages"].append(usage or {}); state["finishes"].append(finish); state["calls"] += 1
    text = (msg.get("content") or "").strip()
    messages.append({"role": "assistant", "content": text})
    return text

def dialogue(sid, key):
    tag = f"{sid}:conv"; out = f"{HERE}/conv/{sid}-conv.json"
    if os.path.exists(out): return "skip"
    t0 = time.time(); paper = source_text(sid)
    state = {"usages": [], "finishes": [], "calls": 0, "tool_calls": 0, "opened": [], "auto_retries": 0}
    reader = [{"role": "system", "content": READER_SYS}, {"role": "user", "content": paper}]
    author = [{"role": "system", "content": AUTHOR_SYS + paper}]
    transcript = []
    for k in range(1, EXCHANGES + 1):
        q = reader_turn(reader, key, f"{tag}:r{k}", state)
        transcript.append({"turn": k, "reader": q})
        author.append({"role": "user", "content": q})
        a = author_turn(author, key, f"{tag}:a{k}", state)
        transcript[-1]["author"] = a
        reader.append({"role": "user", "content": a if k < EXCHANGES else
                       a + "\n\n[The conversation is over. Write the report now.]"})
    report = reader_turn(reader, key, f"{tag}:report", state)
    rec = {"source": sid, "mode": "conversation", "model": MODEL, "effort": EFFORT, "exchanges": EXCHANGES,
           "transcript": transcript, "report": report, "modules_opened": state["opened"],
           "tool_calls": state["tool_calls"], "api_calls": state["calls"], "finish_reasons": state["finishes"],
           "automatic_retries": state["auto_retries"],
           "usage_total": {k: sum(u.get(k, 0) for u in state["usages"]) for k in
                           ("prompt_tokens", "completion_tokens", "prompt_cache_hit_tokens", "prompt_cache_miss_tokens")},
           "seconds": round(time.time() - t0, 1), "finished_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    json.dump(rec, open(out + ".tmp", "w", encoding="utf-8"), indent=1, ensure_ascii=False); os.replace(out + ".tmp", out)
    return "done"

if __name__ == "__main__":
    key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not key: raise SystemExit("DEEPSEEK_API_KEY not set. Nothing sent.")
    srcs = sys.argv[1:]
    print(f"{len(srcs)} dialogues, {EXCHANGES} exchanges each")
    with cf.ThreadPoolExecutor(max_workers=10) as ex:
        futs = {ex.submit(dialogue, s, key): s for s in srcs}
        for f in cf.as_completed(futs):
            print(f"  {futs[f]}: {f.result()}", flush=True)
    hit = miss = outt = 0
    for fn in os.listdir(f"{HERE}/conv"):
        if fn.endswith(".json"):
            u = json.load(open(f"{HERE}/conv/{fn}", encoding="utf-8"))["usage_total"]
            hit += u["prompt_cache_hit_tokens"]; miss += u["prompt_cache_miss_tokens"]; outt += u["completion_tokens"]
    print(f"conversation tokens: cache-hit {hit:,} miss {miss:,} out {outt:,} -> about ${hit/1e6*0.003+miss/1e6*0.15+outt/1e6*0.6:.2f}")
