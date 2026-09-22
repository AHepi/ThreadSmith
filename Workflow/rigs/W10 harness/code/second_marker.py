"""DRIVER. The blind second marker: the reports shuffled, numbered afresh, the mapping closed
until the marks are saved, then agreement with the first marker by field.

  python3 second_marker.py prep    --scratch DIR --reader deepseek [--criteria F] [--seed N]
  python3 second_marker.py collect --scratch DIR --reader deepseek
  python3 second_marker.py compare --scratch DIR --reader deepseek --first <marks file>
  python3 second_marker.py prep --dry --criteria code/fixtures/criteria.example.json

It sends nothing. It is the old rig's arrangement (plan 49 rig, second_marker.py: "set 2: the 48
repeat reports, hidden ... random.Random().shuffle(recs) ... mapping saved"), with three changes:
the mapping is written into the rig's marking folder and never into the marker's own folder, so
the marker cannot read it; the shuffle takes a seed so the shuffle itself can be repeated; and
the fields come from A4's criteria rather than from the code.

The second marker sees a report and the document's id, and nothing that says which arm, which
repeat, which reader or which report of the first marker's set it is.
"""
import os, sys, json, random, argparse
import rig, marks as M, first_marker as FM
from rig import MARKING, write_json, write_text, read_json, stamp


def main():
    p = argparse.ArgumentParser()
    p.add_argument("cmd", choices=["prep", "collect", "compare"])
    p.add_argument("--scratch", default=os.environ.get("W10_SCRATCH", ""))
    p.add_argument("--reader", default="deepseek")
    p.add_argument("--criteria", default=None)
    p.add_argument("--first", default="")
    p.add_argument("--seed", type=int, default=None)
    p.add_argument("--runs", default="")
    p.add_argument("--dry", action="store_true")
    o = p.parse_args()
    crit = M.load(o.criteria)
    base = (os.path.join(o.scratch, "w10", "marking2") if not o.dry
            else os.path.join(rig.RIG, "dry", "marking2"))
    mapping_path = os.path.join(MARKING if not o.dry else os.path.join(rig.RIG, "dry"),
                                f"secret_mapping_{o.reader}.json")

    if o.cmd == "prep":
        only = [r.strip() for r in o.runs.split(",") if r.strip()]
        recs = FM.run_records(o.reader, only) if not o.dry else [
            {"run_id": "DRY1-a-r1", "document": "DRY1", "report": "## Report\n1. held. 2. loose."},
            {"run_id": "DRY1-b-r1", "document": "DRY1", "report": "## Report\n1. loose. 2. held."}]
        seed = o.seed if o.seed is not None else random.randrange(1 << 30)
        random.Random(seed).shuffle(recs)
        mapping = {}
        for i, r in enumerate(recs, 1):
            num = f"R{i:03d}"
            mapping[num] = {"run": r["run_id"], "document": r["document"], "reader": o.reader}
            out_path = os.path.join(base, "marks", f"{num}.json")
            write_text(os.path.join(base, "prompts", f"{num}.txt"),
                       FM.prompt_for(num, r["document"], r.get("report", ""), crit, out_path))
        write_json(mapping_path, {"made_at": stamp(), "seed": seed, "reader": o.reader,
                                  "criteria_version": crit.get("version"), "mapping": mapping})
        print(f"{len(mapping)} report(s) hidden as R001..R{len(mapping):03d} under {base}/prompts; "
              f"the mapping is closed in {mapping_path} (seed {seed}), which the marker's folder "
              f"does not contain" + ("  (dry)" if o.dry else ""))
        return

    if o.cmd == "collect":
        mp = read_json(mapping_path, "the closed mapping")["mapping"]
        out, missing = {}, []
        for num, meta in mp.items():
            f = os.path.join(base, "marks", f"{num}.json")
            if not os.path.exists(f):
                missing.append(num); continue
            out[meta["run"]] = read_json(f)
        f = os.path.join(MARKING, f"marks_second_{o.reader}.json")
        write_json(f, {"marker": "second", "reader": o.reader, "criteria_version": crit.get("version"),
                       "made_at": stamp(), "marks": out})
        print(f"{len(out)} marked, {len(missing)} missing {missing[:5]}; written {f}. "
              f"The mapping was opened only now, after the marks were saved.")
        return

    # compare: marker to marker, by field and document
    import agreement as A
    first = read_json(o.first or os.path.join(MARKING, f"marks_first_{o.reader}.json"), "the first marker's marks")
    second = read_json(os.path.join(MARKING, f"marks_second_{o.reader}.json"), "the second marker's marks")
    rows = A.marker_agreement(crit, first, second)
    A.print_marker_table(rows, len(set(first["marks"]) & set(second["marks"])))
    write_json(os.path.join(MARKING, f"agreement_markers_{o.reader}.json"),
               {"made_at": stamp(), "reader": o.reader, "criteria_version": crit.get("version"),
                "rows": rows})


if __name__ == "__main__":
    main()
