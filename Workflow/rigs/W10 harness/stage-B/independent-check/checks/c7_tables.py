"""c7: the comparison tables of comparison.md, printed from c1_field_by_field.json (run c1 first).

  /home/user/.venvs/threadsmith/bin/python c7_tables.py > tables.md   (or read on screen)

Every number in the tables is taken from c1's rows, which are taken from the two programs' output
files; nothing is typed by hand. Writes nothing.
"""
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
d = json.load(open(os.path.join(HERE, "c1_field_by_field.json")))
R = {r["item"]: r for r in d["rows"]}
ok = lambda b: "yes" if b else "**no**"
fields = [k[:-len(" certified")] for k in R if k.endswith(" certified") and R[k]["section"] == "primary"]

print("#### Agreement per field, per set of 48 and pooled (agree / disagree / unreadable)\n")
print("| field | set | harness (stage_b.py) | independent (recompute.py) | threshold: harness / independent | disagreeing and unreadable reports named alike | match |")
print("|---|---|---|---|---|---|---|")
for f in fields:
    for s in ("p52", "repeat"):
        if f == "marks_per_part":
            a = R[f"{f} {s} agreeing reports"]; g = R[f"{f} {s} the gate count (harness: documents all agreeing; independent: reports)"]
            t = R[f"{f} {s} threshold"]
            hv = f"reports agreeing {a['harness']}; gate: {g['harness']}"
            iv = f"reports agreeing {a['independent']}; gate: {g['independent']}"
            tv = f"{t['harness']} / {t['independent']}"
            m = a["match"] and g["match"] and t["match"]
        else:
            a, dd, u, t = (R[f"{f} {s} {k}"] for k in ("agree", "disagree", "unreadable", "threshold"))
            hv = f"{a['harness']} / {dd['harness']} / {u['harness']}"
            iv = f"{a['independent']} / {dd['independent']} / {u['independent']}"
            tv = f"{t['harness']} / {t['independent'] if t['independent'] is not None else 'none'}"
            m = a["match"] and dd["match"] and u["match"] and t["match"]
        nm = R[f"{f} {s} disagreeing reports named"]["match"] and R[f"{f} {s} unreadable reports named"]["match"]
        print(f"| {f} | {s} | {hv} | {iv} | {tv} | {ok(nm)} | {ok(m)} |")
    pa, pd, pu = (R[f"{f} pooled {k}"] for k in ("agree", "disagree", "unreadable"))
    c = R[f"{f} certified"]
    print(f"| {f} | pooled 96 | {pa['harness']} / {pd['harness']} / {pu['harness']} | {pa['independent']} / {pd['independent']} / {pu['independent']} | (never the gate) | | {ok(pa['match'] and pd['match'] and pu['match'])} |")
    print(f"| {f} | **certified** | {c['harness']} | {c['independent'] if c['independent'] is not None else 'none (not a candidate)'} | | | {ok(c['match'])} |")
nc = [r for r in d["rows"] if r["section"] == "not compared"][0]
h = nc["harness"]
print(f"| modules_served | p52 / repeat / pooled | {h['p52']['agree']}/{h['p52']['disagree']}/{h['p52']['unreadable']}, "
      f"{h['repeat']['agree']}/{h['repeat']['disagree']}/{h['repeat']['unreadable']}, {h['pooled']['agree']}/{h['pooled']['disagree']}/{h['pooled']['unreadable']} "
      f"| not counted | 39 printed / none | | not compared |")

print("\n#### W10.17: closed-list values per enum field, per marker (of 96)\n")
print("| field | first marker: harness / independent | second marker: harness / independent | match |")
print("|---|---|---|---|")
for k, r in R.items():
    if k.startswith("W10.17 ") and k.endswith("first marker in-list"):
        name = k[len("W10.17 "):-len(" first marker in-list")]
        r2 = R[f"W10.17 {name} second marker in-list"]
        print(f"| {name} | {r['harness']} / {r['independent']} | {r2['harness']} / {r2['independent']} | {ok(r['match'] and r2['match'])} |")
r = R["W10.17 fields named unreadable"]
print(f"| fields named unreadable | {r['harness']} | {r['independent']} | {ok(r['match'])} |")

print("\n#### W10.16: the split on the twice-reworded fields\n")
print("Harness: stage_b.py (read set = folder-qualified record file names; percentages over readable reports). "
      "Independent, primary: reading B (those plus the run ids named in section 14.1; percentages over all reports in the subset). "
      "Independent, reading A over readable: the harness's reading, as the independent also computed it.\n")
print("| field | quantity | harness | independent, primary (B, of n) | match | independent, reading A over readable | match |")
print("|---|---|---|---|---|---|---|")
for f in ("marks_per_part", "pairs_that_pull", "rivals_built"):
    for q, qa in (("read n", "read n, harness = independent's reading A"), ("read agree", "read agree, reading A"),
                  ("unread n", "unread n, reading A"), ("unread agree", "unread agree, reading A"),
                  ("read %", "read %, reading A over readable"), ("unread %", "unread %, reading A over readable"),
                  ("gap, points", "gap, reading A over readable")):
        p = R[f"W10.16 {f} {q}"]; c = R[f"cause: W10.16 {f} {qa}"]
        print(f"| {f} | {q} | {p['harness']} | {p['independent']} | {ok(p['match'])} | {c['independent']} | {ok(c['match'])} |")
for k in ("W10.16 the read reports (the set)", "W10.16 falsified on"):
    r = R[k]
    hv = f"{len(r['harness'])} reports" if k.endswith("(the set)") else r["harness"]
    iv = f"{len(r['independent'])} reports" if k.endswith("(the set)") else r["independent"]
    c = R["cause: W10.16 the read reports = the independent's reading A" if k.endswith("(the set)")
          else "cause: W10.16 falsified on, harness = independent's reading A over readable"]
    cv = f"{len(c['independent'])} reports (A)" if k.endswith("(the set)") else c["independent"]
    print(f"| all three | {k[7:]} | {hv} | {iv} | {ok(r['match'])} | {cv} | {ok(c['match'])} |")
r = R["cause: W10.16 pairs_that_pull (the one certified field of the three) falsified under any of the independent's ten reading-and-basis pairs"]
print(f"| pairs_that_pull | falsified under any of the independent's 5 readings x 2 bases | harness: {r['harness']} (its one reading) | {r['independent']} | {ok(r['match'])} | | |")

print("\n#### The certified list and the predictions\n")
print("| item | harness | independent | match |")
print("|---|---|---|---|")
for k in ("certified list", "P3.1 holds", "P3.1 fields reaching 44 in both sets", "P3.2 holds", "P3.3 holds", "P3.4 holds",
          "P3.5 holds", "other fields at 39: the fields failing (harness: implied by its certified list)", "W10.16 holds", "W10.17 holds"):
    r = R[k]
    hv = r["harness"]; iv = r["independent"]
    if isinstance(hv, list) and len(hv) > 5:
        hv = f"{len(hv)} fields"; iv = f"{len(iv)} fields" + (" (the same names)" if r["match"] else "")
    print(f"| {k} | {hv} | {iv} | {ok(r['match'])} |")
p = d["primary"]
print(f"\nTotals (never a score, only the size of the comparison): {p['items_compared']} items, {p['items_matching']} matching; numbers {p['numbers_compared']} compared, "
      f"{p['numbers_matching']} matching; verdicts {p['verdicts_compared']} compared, {p['verdicts_matching']} matching; "
      f"lists {p['lists_compared']} compared, {p['lists_matching']} matching. Cause checks {d['cause_checks']['compared']}, "
      f"matching {d['cause_checks']['matching']}.")
