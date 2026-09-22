"""Quote check for a plan against a theory file (second version, log W5).

Changes from the W3 version, forced by the W5 file-11 judge: quotation marks are paired
in order over the whole text before any length filter is applied (the first version
applied the length filter inside the pairing regex, so a short quotation could shift the
pairing and the program then reported the gap between two quotations instead of the
quotations); every label names the theory file actually checked; and the output ends with
what the program does not reach (a quotation nested inside another, a quotation of the
record, the width of a reading).

For every passage inside straight double quotes, 25 characters or longer, look for it in
the theory file (whitespace normalised; a trailing ellipsis or full stop tolerated as a cut
mark). For each hit report the Part heading it sits under, and the Parts the plan names
within 400 characters of it, so that a wrong attribution can be seen.
"""
import re, sys, json, os

plan_path, theory_path, out_json = sys.argv[1], sys.argv[2], sys.argv[3]
theory_name = os.path.basename(theory_path).split(" ")[0]
plan = open(plan_path, encoding="utf-8").read()
theory = open(theory_path, encoding="utf-8").read()

def norm(s): return re.sub(r"\s+", " ", s).strip()

parts = [(m.start(), norm(m.group(1))) for m in re.finditer(r"^# (Part [^\n]+)$", theory, re.M)]
ders = [(m.start(), norm(m.group(1))) for m in re.finditer(r"^## (\d+\. [^\n]+)$", theory, re.M)]
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
    last_part_start=max([st for (st,_) in parts if st<=orig_pos] or [0])
    d=[name for (st,name) in ders if last_part_start<st<=orig_pos]
    return (p[-1] if p else "?") + ((" / Derivation " + d[-1]) if d else "")

# pair the quotation marks in order over the whole text, no length filter
marks=[m.start() for m in re.finditer(r'"', plan)]
spans=[]
for i in range(0, len(marks)-1, 2):
    a,b=marks[i],marks[i+1]
    q=plan[a+1:b]
    if "\n" in q:               # a mark left open across a line: resync on the next mark
        continue
    spans.append((a,q))
odd = len(marks) % 2
seen=set(); rows=[]
for a,q in spans:
    if len(q) < 25 or q in seen: continue
    seen.add(q)
    qn=re.sub(r"\s*\.\.\.$","",norm(q)).rstrip(".")
    idx=tnorm.find(qn); found = idx>=0
    if not found and " ... " in qn:
        pieces=[p for p in qn.split(" ... ") if len(p)>=15]
        if pieces and all(tnorm.find(p)>=0 for p in pieces):
            found=True; idx=tnorm.find(pieces[0])
    if not found:
        rows.append({"quote":q[:120],"status":f"not in file {theory_name}"}); continue
    part=part_at(pos[idx])
    window=plan[max(0,a-400):a+len(q)+400]
    named=sorted(set(re.findall(r"Part (?:0|[IVX]+)|Derivation \d+", window)))
    rows.append({"quote":q[:120],"status":"found",f"in_file_{theory_name}_under":part,"plan_names_nearby":named})

n_found=sum(1 for r in rows if r["status"]=="found")
print(f"Checked against file {theory_name}. {len(rows)} distinct quotations of 25+ characters; {n_found} found in file {theory_name}; {len(rows)-n_found} not in file {theory_name} (quotations of the record, or the plan's own phrases). {len(marks)} quotation marks in the plan{' (an odd count: one span is unpaired)' if odd else ''}.")
for r in rows:
    if r["status"]=="found":
        print(f"FOUND  [{r[f'in_file_{theory_name}_under']}]  nearby: {r['plan_names_nearby']}\n       \"{r['quote']}\"")
for r in rows:
    if r["status"]!="found":
        print(f"NOT IN FILE {theory_name}  \"{r['quote']}\"")
print("\nWhat this program does not reach: a quotation nested inside another (the inner marks split the outer span); whether a quotation of the record is verbatim (it checks the theory file only); whether the plan reads a found sentence wider than written; a quotation shorter than 25 characters.")
json.dump(rows, open(out_json,"w"), indent=1, ensure_ascii=False)
