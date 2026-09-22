"""DRIVER. The first marker: one marking prompt per report, from A4's frozen criteria; then the
marks collected and checked against the closed lists.

  python3 first_marker.py prompts  --scratch DIR --reader deepseek [--criteria F] [--runs a,b]
  python3 first_marker.py collect  --scratch DIR --reader deepseek --tag first
  python3 first_marker.py validate --marks <file> [--criteria F]
  python3 first_marker.py prompts  --dry --reader sonnet --criteria code/fixtures/criteria.example.json

It is a template, not a marker: it writes what a marker is asked and checks what a marker
returns. The marking itself is done by the agents the plan names (W10 stage D, Sonnet 5).

The marker never sees the run's arm, its repeat or its reader: the prompt carries a report
number and the document's id only. That is the first marker's blindness to the arm; the second
marker (second_marker.py) is blind to the report's identity as well.
"""
import os, sys, json, argparse
import rig, marks as M
from rig import RUNS, MARKING, write_json, write_text, read_json, stamp

HEAD = ("You are marking one report against criteria that were frozen before any report was read. "
        "You are not judging the report and you are not judging the document. You are recording, "
        "field by field, what the report does, by the criterion given for that field, in the words "
        "a stranger could apply.\n\n"
        "Read the report below. Then write one JSON object with one key per field, and nothing "
        "else, to the output path at the end of this file, using Write once. Where a field's "
        "values are a closed list, use one of them and nothing else. Where you cannot tell, use "
        "null: a guess is worse than a gap, and a gap is reported as unreadable, not as "
        "agreement.\n\n")


def field_block(f):
    lines = [f"### {f['name']} - {f.get('title', f['name'])}",
             f"kind: {f['kind']}; per: {f['per']}; layer: {f.get('layer','')}"]
    if f.get("values"):
        lines.append("one of, and nothing else: " + ", ".join(map(str, f["values"])))
    lines.append(f"criterion: {f['criterion']}")
    ex = f.get("example") or {}
    if ex.get("quote"):
        lines.append(f"the example that fixes the boundary: {ex.get('value')!r} because {ex['quote']}")
    return "\n".join(lines)


def prompt_for(num, doc, report, crit, out_path):
    body = [HEAD, f"Report number: {num}    Document: {doc}", "", "=== THE FIELDS ===", ""]
    for f in crit["fields"]:
        body.append(field_block(f)); body.append("")
    body += ["=== THE REPORT ===", "", report.strip(), "", "=== END OF THE REPORT ===", "",
             "Write one JSON object with these keys: " + ", ".join(f["name"] for f in crit["fields"]),
             f"Output path (use Write, once, the JSON only): {out_path}", ""]
    return "\n".join(body)


def run_records(reader, only=None):
    d = os.path.join(RUNS, reader)
    if not os.path.isdir(d):
        raise SystemExit(f"no run records at {d}. Nothing to mark.")
    out = []
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".json") and (not only or fn[:-5] in only):
            out.append(read_json(os.path.join(d, fn)))
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["prompts", "collect", "validate"])
    p.add_argument("--scratch", default=os.environ.get("W10_SCRATCH", ""))
    p.add_argument("--reader", default="deepseek")
    p.add_argument("--criteria", default=None)
    p.add_argument("--runs", default="")
    p.add_argument("--tag", default="first")
    p.add_argument("--marks", default="")
    p.add_argument("--dry", action="store_true")
    o = p.parse_args()
    crit = M.load(o.criteria)
    if o.cmd == "validate":
        data = read_json(o.marks, "a marks file")
        by = {f["name"]: f for f in crit["fields"]}
        bad = 0
        for rid, row in data["marks"].items():
            for name, val in row.items():
                if name not in by:
                    print(f"  {rid}: field {name!r} is not in the criteria"); bad += 1; continue
                c = M.check_value(by[name], val)
                if c and c != "missing":
                    print(f"  {rid}.{name}: {c}"); bad += 1
            for name in by:
                if name not in row:
                    print(f"  {rid}: no value for {name!r}")
        print(f"{len(data['marks'])} report(s) checked against criteria {crit.get('version')!r}; "
              f"{bad} value(s) outside the criteria")
        sys.exit(1 if bad else 0)

    base = (os.path.join(o.scratch, "w10", "marking1") if not o.dry
            else os.path.join(rig.RIG, "dry", "marking1"))
    only = [r.strip() for r in o.runs.split(",") if r.strip()]
    recs = run_records(o.reader, only) if not o.dry else [
        {"run_id": "DRY1-a-r1", "document": "DRY1", "report": "## Report\n1. held. 2. loose."}]
    if o.cmd == "prompts":
        index = {}
        for i, r in enumerate(recs, 1):
            num = f"M{i:03d}"
            out_path = os.path.join(base, "marks", f"{num}.json")
            text = prompt_for(num, r["document"], r.get("report", ""), crit, out_path)
            write_text(os.path.join(base, "prompts", f"{num}.txt"), text)
            index[num] = {"run": r["run_id"], "document": r["document"], "reader": o.reader}
        write_json(os.path.join(base, "index.json"),
                   {"made_at": stamp(), "criteria_version": crit.get("version"), "reports": index})
        print(f"{len(index)} marking prompt(s) under {base}/prompts; the report number to run "
              f"mapping is {base}/index.json" + ("  (dry)" if o.dry else ""))
        return
    if o.cmd == "collect":
        index = read_json(os.path.join(base, "index.json"))["reports"]
        out, missing = {}, []
        for num, meta in index.items():
            p_ = os.path.join(base, "marks", f"{num}.json")
            if not os.path.exists(p_):
                missing.append(num); continue
            out[meta["run"]] = read_json(p_)
        f = os.path.join(MARKING, f"marks_{o.tag}_{o.reader}.json")
        write_json(f, {"marker": o.tag, "reader": o.reader,
                       "criteria_version": crit.get("version"), "made_at": stamp(), "marks": out})
        print(f"{len(out)} marked, {len(missing)} missing {missing[:5]}; written {f}")


if __name__ == "__main__":
    main()
