"""Send every run to DeepSeek and save each reply. Resumable: a run whose file exists is skipped.

  DEEPSEEK_API_KEY=... python3 run.py            # the full 312 runs
  python3 run.py --fake                          # no network: a stub reply, to test the pipeline
  DEEPSEEK_API_KEY=... python3 run.py --limit 4  # a pilot: the first 4 runs of the fixed order
  DEEPSEEK_API_KEY=... python3 run.py --only c08-s2-r1

Settings, the same for every run (from plan 42): model deepseek-flash on DeepSeek's own service;
thinking enabled at effort "high", which is the middle of DeepSeek's three levels (low / high / max;
"medium" is mapped to high by the service); every run a fresh conversation; no system message.
"""
import os, sys, json, time, random, argparse, concurrent.futures as cf
import requests
from setups import prompt

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-flash"
EFFORT = "high"
SEED = 4243          # plans 42 and 43
REPEATS = 3
MAX_TOKENS = 16000   # bounds the cost of one runaway reply; thinking counts toward it

def build_run_list():
    passages = json.load(open(os.path.join(HERE, "passages.json"), encoding="utf-8"))
    reworded = json.load(open(os.path.join(HERE, "reworded.json"), encoding="utf-8"))
    runs = []
    for c in passages:
        for s in range(4):
            for r in range(1, REPEATS + 1):
                runs.append({"run_id": f"c{c['id']}-s{s}-r{r}", "case": c["id"], "setup": s, "repeat": r,
                             "passage": c["passage"]})
    for c in reworded:
        for s in range(4):
            runs.append({"run_id": f"c{c['id']}-s{s}-r1", "case": c["id"], "setup": s, "repeat": 1,
                         "passage": c["passage"], "reworded_of": c["of"]})
    random.Random(SEED).shuffle(runs)   # fixed shuffled order: partners never sent side by side
    return runs

def call(messages, key):
    body = {"model": MODEL, "messages": messages, "stream": False,
            "thinking": {"type": "enabled"}, "reasoning_effort": EFFORT, "max_tokens": MAX_TOKENS}
    delay = 2
    for attempt in range(6):
        try:
            r = requests.post(URL, json=body, timeout=600,
                              headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
            if r.status_code == 200:
                return r.json()
            if r.status_code in (401, 402, 400):
                raise SystemExit(f"stopped: HTTP {r.status_code} {r.text[:300]}")
            err = f"HTTP {r.status_code} {r.text[:200]}"
        except requests.RequestException as e:
            err = repr(e)
        print("  retry after", err, file=sys.stderr)
        time.sleep(delay); delay = min(delay * 2, 60)
    raise RuntimeError("gave up: " + err)

def fake(messages):
    words = len(messages[0]["content"].split())
    return {"choices": [{"message": {"content": f"FAKE REPLY. Prompt had {words} words. "
                                                 "(1) parts (2) holds (3) weakest (4) RELY ON IT",
                                     "reasoning_content": "fake thinking"}}],
            "usage": {"prompt_tokens": words, "completion_tokens": 20, "prompt_cache_hit_tokens": 0}}

def do_run(run, key, use_fake):
    out = os.path.join(HERE, "replies", run["run_id"] + ".json")
    if os.path.exists(out):
        return "skip"
    messages = [{"role": "user", "content": prompt(run["setup"], run["passage"])}]
    t0 = time.time()
    resp = fake(messages) if use_fake else call(messages, key)
    msg = resp["choices"][0]["message"]
    rec = {**run, "model": MODEL, "effort": EFFORT, "reply": msg.get("content", ""),
           "reasoning": msg.get("reasoning_content", ""), "usage": resp.get("usage", {}),
           "seconds": round(time.time() - t0, 1), "finished_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    tmp = out + ".tmp"
    json.dump(rec, open(tmp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    os.replace(tmp, out)
    return "done"

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fake", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--only", default="")
    ap.add_argument("--workers", type=int, default=6)
    a = ap.parse_args()
    key = os.environ.get("DEEPSEEK_API_KEY", "")
    if not a.fake and not key:
        raise SystemExit("DEEPSEEK_API_KEY is not set. Nothing sent.")
    runs = build_run_list()
    json.dump(runs, open(os.path.join(HERE, "run_list.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    if a.only:
        runs = [r for r in runs if r["run_id"] == a.only]
    if a.limit:
        runs = runs[:a.limit]
    print(f"{len(runs)} runs in the list;", "FAKE" if a.fake else "LIVE")
    os.makedirs(os.path.join(HERE, "replies"), exist_ok=True)
    done = skipped = 0
    with cf.ThreadPoolExecutor(max_workers=a.workers) as ex:
        futs = {ex.submit(do_run, r, key, a.fake): r for r in runs}
        for f in cf.as_completed(futs):
            r = futs[f]
            res = f.result()
            if res == "skip": skipped += 1
            else:
                done += 1
                if done % 10 == 0 or a.limit: print(f"  {done} done ({r['run_id']})")
    print(f"finished: {done} new, {skipped} already there")
    # cost so far, from the saved usage
    pin = pout = phit = 0
    for fn in os.listdir(os.path.join(HERE, "replies")):
        if fn.endswith(".json"):
            u = json.load(open(os.path.join(HERE, "replies", fn), encoding="utf-8")).get("usage", {})
            pin += u.get("prompt_tokens", 0); pout += u.get("completion_tokens", 0)
            phit += u.get("prompt_cache_hit_tokens", 0)
    miss = pin - phit
    print(f"tokens so far: in {pin} (cache hit {phit}), out {pout}; "
          f"worked-out cost at off-peak flash prices: ${miss/1e6*0.15 + phit/1e6*0.003 + pout/1e6*0.6:.2f}")
