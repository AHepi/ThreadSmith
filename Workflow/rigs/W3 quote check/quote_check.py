"""Quote check for a plan against Semantics file 10.

For every passage in the plan that sits inside straight double quotes and is at least
25 characters long, look for it in file 10 (after normalising whitespace). For each hit,
report the Part heading it sits under (the nearest preceding "# Part ..." heading), and
the Part names the plan mentions within 400 characters before or after the quotation, so
that a wrong attribution can be seen. Quotations not found in file 10 are listed as
"not in file 10" (they may be quotations of the record, which this program does not check).
"""
import re, sys, json

plan_path, theory_path = sys.argv[1], sys.argv[2]
plan = open(plan_path, encoding="utf-8").read()
theory = open(theory_path, encoding="utf-8").read()

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

# Part headings with positions
parts = [(m.start(), norm(m.group(1))) for m in re.finditer(r"^# (Part [^\n]+)$", theory, re.M)]
# derivation headings (Part XVI)
ders = [(m.start(), norm(m.group(1))) for m in re.finditer(r"^## (\d+\. [^\n]+)$", theory, re.M)]
tn = theory  # keep positions; search on a normalised copy with a position map
# build normalised theory with map back to original positions
buf=[]; pos=[]; prev_space=False
for i,ch in enumerate(theory):
    if ch.isspace():
        if prev_space: continue
        buf.append(" "); pos.append(i); prev_space=True
    else:
        buf.append(ch); pos.append(i); prev_space=False
tnorm="".join(buf)

def part_at(orig_pos):
    p=[name for (st,name) in parts if st<=orig_pos]
    d=[name for (st,name) in ders if st<=orig_pos and st> (max([st2 for (st2,_) in parts if st2<=orig_pos] or [0]))]
    return (p[-1] if p else "?") + ((" / Derivation " + d[-1]) if d else "")

quotes = re.findall(r'"([^"\n]{25,}?)"', plan)
seen=set(); rows=[]
for q in quotes:
    if q in seen: continue
    seen.add(q)
    qn=norm(q)
    qn=re.sub(r"\s*\.\.\.$","",qn).rstrip(".")  # a trailing ellipsis or full stop marks a cut, not a word
    idx=tnorm.find(qn)
    if idx<0:
        # try trimming a trailing ellipsis fragment " ..." splits
        found=False
        if " ... " in qn:
            pieces=[p for p in qn.split(" ... ") if len(p)>=15]
            found=all(tnorm.find(p)>=0 for p in pieces)
            if found:
                idx=tnorm.find(pieces[0])
        if not found:
            rows.append({"quote":q[:120],"status":"not in file 10"}); continue
    origin=pos[idx]
    part=part_at(origin)
    # parts named in the plan near the quote
    qpos=plan.find(q)
    window=plan[max(0,qpos-400):qpos+len(q)+400]
    named=sorted(set(re.findall(r"Part (?:0|[IVX]+)|Derivation \d+|\(\w{1,3}\d?\)", window)))
    rows.append({"quote":q[:120],"status":"found","in_file_10_under":part,"plan_names_nearby":named})

n_found=sum(1 for r in rows if r["status"]=="found")
print(f"{len(rows)} distinct quotations of 25+ characters; {n_found} found in file 10; {len(rows)-n_found} not in file 10 (record quotations or plan's own phrases).")
for r in rows:
    if r["status"]=="found":
        print(f"FOUND  [{r['in_file_10_under']}]  nearby: {r['plan_names_nearby']}\n       \"{r['quote']}\"")
for r in rows:
    if r["status"]!="found":
        print(f"NOT IN FILE 10  \"{r['quote']}\"")
json.dump(rows, open(sys.argv[3],"w"), indent=1, ensure_ascii=False)
