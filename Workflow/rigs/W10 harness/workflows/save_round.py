#!/usr/bin/env python3
"""Save one fix-loop round (addendum W13): the returns unchanged, the tool audit from the
transcripts, a key scan, and a summary of the review. Usage:
  save_round.py <task output json> <workflow transcript dir> <round n>
Writes under Workflow/rigs/W10 harness/fix-round returns/round-<n>/ and appends to
tool_audit.txt there. Prints the review's faults and predictions. Sends nothing."""
import json, sys, os, glob, collections, re

KEY_MARKS = ("sk-1a31", "atr_FKws", "tp-sqzn4")   # the first characters of the three key values, never the values
ROOT = "/home/user/ThreadSmith"
OUT = os.path.join(ROOT, "Workflow/rigs/W10 harness/fix-round returns")

def main(task_out, tdir, n):
    d = json.load(open(task_out, encoding="utf-8"))
    res = d["result"] if "result" in d else d
    rd = os.path.join(OUT, f"round-{n}"); os.makedirs(rd, exist_ok=True)
    for role, fx in (res.get("fixes") or {}).items():
        json.dump(fx, open(os.path.join(rd, f"{role}.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump(res.get("review"), open(os.path.join(rd, "A5-reviewer.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    # audit
    tot = collections.Counter(); outside = set(); net = []; keyhits = 0; per = []
    meta = {}
    for m in glob.glob(tdir + "/agent-*.meta.json"):
        try: meta[os.path.basename(m).split(".")[0]] = json.load(open(m))
        except Exception: pass
    for f in sorted(glob.glob(tdir + "/agent-*.jsonl")):
        aid = os.path.basename(f).split(".")[0]; c = collections.Counter(); w = set()
        for line in open(f, encoding="utf-8"):
            if any(k in line for k in KEY_MARKS): keyhits += 1
            try: j = json.loads(line)
            except Exception: continue
            msg = j.get("message") or j
            content = msg.get("content") if isinstance(msg, dict) else None
            if not isinstance(content, list): continue
            for b in content:
                if isinstance(b, dict) and b.get("type") == "tool_use":
                    nm = b.get("name"); c[nm] += 1; tot[nm] += 1; i = b.get("input", {})
                    if nm in ("Write", "Edit"):
                        p = i.get("file_path", ""); w.add(p)
                        if "Workflow/rigs/W10 harness" not in p: outside.add(p)
                    if nm in ("WebFetch", "WebSearch"): net.append(nm + ": " + str(i.get("url") or i.get("query")))
                    if nm == "Bash":
                        cmd = i.get("command", "")
                        if re.search(r"\bcurl\b|\bwget\b|fetch\.py", cmd): net.append("bash: " + cmd[:120].replace("\n", " "))
        per.append(f"  {(meta.get(aid) or {}).get('label') or aid}: {dict(c)}; files written by tool: {len(w)}")
    # key scan of the saved returns
    saved_hits = [p for p in glob.glob(rd + "/*.json") if any(k in open(p, encoding="utf-8").read() for k in KEY_MARKS)]
    with open(os.path.join(OUT, "tool_audit.txt"), "a", encoding="utf-8") as a:
        a.write(f"\n\nRound {n} (transcripts {os.path.basename(tdir)}): tools {dict(tot)}.\n" + "\n".join(per) +
                f"\nWrites by tool outside the harness folder: {sorted(outside) or 'none'}.\nNetwork-looking calls: {len(net)}" +
                ("\n  " + "\n  ".join(net) if net else "") +
                f"\nKey values in transcripts: {keyhits}; in the saved returns: {len(saved_hits)}.\n")
    rv = res.get("review") or {}
    print(f"ROUND {n}: fixers {list((res.get('fixes') or {}).keys())}")
    for role, fx in (res.get("fixes") or {}).items():
        print(f"  {role}: fixed {[x['fault'] for x in fx.get('fixed', [])]} declined {[x['fault'] for x in fx.get('declined', [])]}")
    print("  verified fixed:", [x["fault"] for x in rv.get("verified_fixed", [])])
    for f in rv.get("faults", []):
        print(f"  FAULT [{f['severity']}] #{f['fault']} {f['deliverable']} {f['file'].split('/')[-1]}:\n     {f['fault_text'][:600]}\n     FIX: {f['forced_fix'][:400]}")
    for p in rv.get("predictions_ticked", []):
        print(f"  PRED {p['prediction'][:60]} -> {p['verdict'][:160]} | {p['count'][:160]}")
    print("  writes outside harness:", sorted(outside) or "none", "| key hits:", keyhits, len(saved_hits))
    blocking = [f["fault"] for f in rv.get("faults", []) if str(f.get("severity", "")).startswith("blocks")]
    print(f"  SUMMARY: {len(rv.get('faults', []))} faults returned, {len(blocking)} blocking")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
