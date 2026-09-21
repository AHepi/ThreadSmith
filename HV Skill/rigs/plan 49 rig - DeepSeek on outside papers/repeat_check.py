"""Plan H56: shape by program for every repeat run, and the passages the marker must read.
Prints, per run in runs_repeat/ and runs_sonnet5/ (or the folders named on the command line): words, shape, finish reasons, modules opened, then every sentence
containing 'flip' (break 1) and every table row or sentence containing 'fixed' (break 2). Marks nothing."""
import os, re, json, sys
HERE = os.path.dirname(os.path.abspath(__file__))
HEAD = [r"question,? frozen|frozen question|the question\b.*frozen", r"explanation in parts|the parts\b", r"part by part",
        r"whole[- ]explanation checks|flip|reverse|starting points", r"harder to vary|tighten", r"does not show|not the same as true", r"next step"]
MARKS = ["held if", "two routes", "held", "loose", "idle", "borrowed", "fixed", "unknown"]
def shape(rep):
    low = rep.lower()
    heads = sum(1 for h in HEAD if re.search(h, low))
    marks = [m for m in MARKS if re.search(r"\b" + m + r"\b", low)]
    return ("FULL" if heads >= 6 and len(marks) >= 3 else ("PART" if heads >= 3 or marks else "NONE")), heads, marks
def passages(rep, word):
    out = []
    for line in rep.split("\n"):
        if re.search(r"\b" + word, line, re.I):
            out.append(line.strip())
    return out
rows = []
folders = [a for a in sys.argv[1:] if not a.startswith("--")] or ["runs_repeat", "runs_sonnet5"]
for d in [f"{HERE}/{f}" for f in folders]:
  if not os.path.isdir(d): continue
  for fn in sorted(os.listdir(d)):
      if not fn.endswith(".json"): continue
      r = json.load(open(f"{d}/{fn}", encoding="utf-8")); rep = r["reply"]
      sh, heads, marks = shape(rep)
      rows.append(dict(run=fn[:-5], folder=os.path.basename(d), model=r.get("model"), words=len(rep.split()), shape=sh, headings=heads, marks=marks,
                       finish=r.get("finish_reasons"), retries=r.get("automatic_retries"),
                       modules=r.get("modules_opened", []), seconds=r["seconds"],
                       thinking_words=len(r["reasoning"].split())))
      print(f"=== {os.path.basename(d)}/{fn[:-5]} ({r.get('model')}): {len(rep.split())} words, {sh} ({heads} headings, marks {marks}), "
            f"finish {r.get('finish_reasons')}, retries {r.get('automatic_retries')}, modules {r.get('modules_opened', [])} ===")
      for w, label in (("flip", "break 1, flip"), ("fixed", "break 2, fixed")):
          ps = passages(rep, w)
          print(f"  -- {label}: {len(ps)} line(s)")
          for p in ps: print("     ", p[:700])
      print()
json.dump(rows, open(f"{HERE}/repeat_shape_by_program.json", "w"), indent=1) if rows else None
print(f"{len(rows)} repeat runs on disk")
