"""Collector D: build 'collector D.jsonl' from the S95-S97 sources.

Run: PYTHONDONTWRITEBYTECODE=1 python3 build_D.py
Writes only ../collector D.jsonl and ../collector D - build report.json (both collector D's own files).
"""
import itertools, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import edits

OUT_DIR = "/home/user/ThreadSmith/Semantics/results/S98 Ledger of edits and recommendations/collect/"
OUT = OUT_DIR + "collector D.jsonl"
REPORT = OUT_DIR + "collector D - build report.json"
FIELDS = ["rid", "round", "source_file", "source_ref", "kind", "status", "applied_in", "target_text",
          "target_line", "target_part", "old", "new", "old_sentence", "new_sentence", "scope", "same_as"]

counter = itertools.count(1)


def next_rid():
    return "D-%d" % next(counter)


def main():
    recs, report, texts = edits.build(next_rid)
    parts = [("edits", len(recs))]
    try:
        import vocab
        v = vocab.build(next_rid, recs, texts)
        recs += v
        parts.append(("vocabulary", len(v)))
    except ImportError:
        pass
    try:
        import recs_s95
        v = recs_s95.build(next_rid, recs, texts)
        recs += v
        parts.append(("S95 recommendations", len(v)))
    except ImportError:
        pass
    try:
        import recs_s96
        v = recs_s96.build(next_rid, recs, texts)
        recs += v
        parts.append(("S96 recommendations", len(v)))
    except ImportError:
        pass
    # symmetric same_as
    by = {r["rid"]: r for r in recs}
    for r in recs:
        for o in r["same_as"]:
            if o in by and r["rid"] not in by[o]["same_as"]:
                by[o]["same_as"].append(r["rid"])
    for r in recs:
        r["same_as"] = sorted(set(r["same_as"]), key=lambda x: int(x.split("-")[1]))
    with open(OUT, "w", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps({k: r[k] for k in FIELDS}, ensure_ascii=False) + "\n")
    report["parts"] = parts
    report["records"] = len(recs)
    json.dump(report, open(REPORT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps(report, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
