# NOTE (added by Claude, log S115): this file is 'ancestry-helper.py', copied unchanged from the appendix of
# GPT 6 Astra's reply 01 ('tests/S115 Returns from GPT 6 Astra/01 Return - measuring what is learned,
# with stock Avida only.md'). Only these note lines were added. It has not been run on S113's data;
# see 'results/S115 Checking the Astra returns/01 Check of reply 01 - measuring what is learned.md'.
#!/usr/bin/env python3
"""Extract recorded sequence-group origins within ONE uninterrupted Avida segment.

Call with snapshots in time order. A shared --segment label is the caller's
assertion, not an automatic check that IDs survived a restart. Recurrent births
can merge into an active group; this output is not individual-program genealogy.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path


def read_spop(path):
    columns = None
    for lineno, raw in enumerate(path.read_text().splitlines(), 1):
        line = raw.strip()
        if line.startswith("#format "):
            columns = line.split()[1:]
        elif line and not line.startswith("#"):
            if columns is None:
                raise ValueError(f"{path}:{lineno}: no #format header")
            row = dict(zip(columns, line.split()))
            try:
                if "parents" not in row and "parent_id" not in row:
                    raise ValueError("missing parents column")
                parents = row.get("parents", row.get("parent_id", ""))
                if parents in ("", "(none)", "-1"):
                    parent_ids = ()
                else:
                    parent_ids = tuple(int(x) for x in parents.split(","))
                record = dict(id=int(row["id"]), parents=parent_ids,
                              depth=int(row["depth"]),
                              update_born=int(row["update_born"]),
                              sequence=row["sequence"],
                              num_units=int(row.get("num_units", row.get("num_cpus", "-1"))))
                if record["num_units"] < 0:
                    raise ValueError("missing/negative living count")
                record["hw_type"] = row.get("hw_type", "")
                record["inst_set"] = row.get("inst_set", "")
                yield record
            except (KeyError, ValueError) as exc:
                raise ValueError(f"{path}:{lineno}: invalid record: {exc}") from exc


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--segment", required=True, help="one uninterrupted process label")
    parser.add_argument("--target", required=True, type=int)
    parser.add_argument("--output", type=Path, default=Path("selected-lineage.spop"))
    parser.add_argument("snapshots", nargs="+", type=Path, help="same-segment files in time order")
    args = parser.parse_args()
    records, provenance = {}, []
    identity = ("parents", "depth", "update_born", "sequence", "hw_type", "inst_set")
    for path in args.snapshots:
        provenance.append(dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        for record in read_spop(path):
            old = records.get(record["id"])
            if old and any(old[k] != record[k] for k in identity):
                raise ValueError(f"ID {record['id']}: conflicting identity across supplied snapshots")
            records[record["id"]] = record  # abundance comes from its last supplied record
    lineage, seen, current = [], set(), args.target
    while current is not None:
        if current in seen:
            raise ValueError(f"cycle at ID {current}")
        if current not in records:
            raise ValueError(f"missing target or parent ID {current}")
        seen.add(current)
        record = records[current]
        lineage.append(record)
        if len(record["parents"]) > 1:
            raise ValueError(f"ID {current}: multiple parents; this helper requires asexual paths")
        current = record["parents"][0] if record["parents"] else None
    lineage.reverse()
    if lineage[0]["depth"] != 0:
        raise ValueError("root has nonzero depth: path is truncated despite an empty parents field")
    for parent, child in zip(lineage, lineage[1:]):
        if child["depth"] != parent["depth"] + 1:
            raise ValueError(f"depth mismatch at edge {parent['id']} -> {child['id']}")
        if child["update_born"] < parent["update_born"]:
            raise ValueError(f"birth-update reversal at ID {child['id']}")
    fields = ("id", "parents", "depth", "update_born", "sequence", "num_units")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as out:
        out.write("#filetype genotype_data\n#format " + " ".join(fields) + "\n")
        out.write("# Recorded group-origin path; counts are last supplied observations.\n")
        for record in lineage:
            row = dict(record, parents=",".join(map(str, record["parents"])) or "(none)")
            out.write(" ".join(str(row[k]) for k in fields) + "\n")
    edges = args.output.with_suffix(".edges.tsv")
    with edges.open("w", newline="") as out:
        writer = csv.writer(out, delimiter="\t")
        writer.writerow(("parent_id", "child_id", "parent_update", "child_update", "parent_sequence", "child_sequence"))
        for parent, child in zip(lineage, lineage[1:]):
            writer.writerow((parent["id"], child["id"], parent["update_born"], child["update_born"], parent["sequence"], child["sequence"]))
    audit = dict(segment=args.segment, inputs=provenance, target=args.target,
                 ids_root_to_target=[r["id"] for r in lineage],
                 meaning="recorded group origins; active matching sequences can merge independent births",
                 counts="last supplied record per group; not a single contemporaneous population",
                 hardware="minimal output assumes the matching single instruction set in analyze config")
    args.output.with_suffix(".audit.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(f"Wrote {len(lineage)} group records to {args.output}; edges to {edges}")


if __name__ == "__main__":
    try:
        main()
    except (ValueError, OSError) as exc:
        raise SystemExit(str(exc))
