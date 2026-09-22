"""DRIVER. Stage B (plan W14): the thresholds of the marking plan's section 6 applied per set of
48 and pooled over 96, the split of W13 section 2, and the certified list written for
agreement.py --certified.

  python3 stage_b.py --reader record96 [--criteria F]

Reads <rig>/marking/marks_first_<reader>.json and marks_second_<reader>.json (written by
first_marker.py collect and second_marker.py collect), the instrument and the marking plan.
Writes <rig>/marking/stage_b_<reader>.json and prints the table. Sends nothing.

Rules fixed in W14 before any mark existed:
- a field is certified when it reaches its threshold in EACH set of 48 (p52 = the close-marked
  48; rep+rep31+son+son31 = the repeat 48); the pooled 96 is printed beside, never the gate;
- marks_per_part is read by document: a document agrees when every shared report of it agrees;
  its threshold per set is ceil(40/48 x the documents in that set);
- the read reports are the record files named anywhere in criteria.json or marking-plan.md
  (X.json placeholders excluded), mapped to run ids by set; the twice-reworded fields are
  reported over all, read and unread (W10.16: read minus unread over 10 points falsifies);
- W10.17: a field with fewer than 95 of 96 in-list values from either marker is unreadable.
"""
import os, re, sys, json, math, argparse
import rig, marks as M
from rig import MARKING, write_json, read_json, stamp

THRESH = {  # of 48, marking plan section 6
    "shape": 44, "turned_own_test": 44, "same_explanation": 44,
    "marks_per_part": 40, "pairs_that_pull": 40, "rivals_built": 40,
    "question_identity": 46, "test_swap": 42, "test_poke": 42,
}
DEFAULT = 39
TRIO = ("shape", "turned_own_test", "same_explanation")
REWORDED_TWICE = ("marks_per_part", "pairs_that_pull", "rivals_built")
SET_OF = {"p52": "close", "rep": "repeat", "rep31": "repeat", "son": "repeat", "son31": "repeat"}
FOLDER_TAG = {"runs": "p52", "runs_repeat": "rep", "runs_repeat_31": "rep31",
              "runs_sonnet5": "son", "runs_sonnet5_31": "son31"}


def read_reports():
    inst = os.path.join(rig.RIG, "instrument")
    text = ""
    for fn in ("criteria.json", "marking-plan.md"):
        text += open(os.path.join(inst, fn), encoding="utf-8").read()
    out = set()
    for folder, stem in re.findall(r"(runs[a-z0-9_]*)/([A-Za-z0-9_-]+)\.json", text):
        if stem == "X" or folder not in FOLDER_TAG:
            continue
        out.add(f"{FOLDER_TAG[folder]}_{stem}")
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--reader", default="record96")
    p.add_argument("--criteria", default=None)
    o = p.parse_args()
    crit = M.load(o.criteria)
    first = read_json(os.path.join(MARKING, f"marks_first_{o.reader}.json"), "the first marks")
    second = read_json(os.path.join(MARKING, f"marks_second_{o.reader}.json"), "the second marks")
    shared = sorted(set(first["marks"]) & set(second["marks"]))
    doc_of = {}
    for rid in shared:
        doc_of[rid] = (first["marks"][rid].get("_document") or
                       rig_document(rid))
    read = read_reports() & set(shared)
    sets = {"close": [r for r in shared if SET_OF.get(r.split("_")[0]) == "close"],
            "repeat": [r for r in shared if SET_OF.get(r.split("_")[0]) == "repeat"]}
    by = {f["name"]: f for f in crit["fields"]}
    out = {"made_at": stamp(), "reader": o.reader, "criteria_version": crit.get("version"),
           "shared_reports": len(shared), "sets": {k: len(v) for k, v in sets.items()},
           "read_reports": sorted(read), "fields": {}, "certified": [], "unreadable": [],
           "rule": "certified when the threshold (of 48) is reached in each set separately; "
                   "pooled 96 beside; marks_per_part by document"}
    for f in M.fields(crit, comparable_only=True):
        name = f["name"]
        def agree_set(rids):
            a = d = u = 0
            for rid in rids:
                s = M.same(f, first["marks"][rid].get(name), second["marks"][rid].get(name))
                if s is None: u += 1
                elif s: a += 1
                else: d += 1
            return a, d, u
        row = {"sort": f.get("sort"), "certified_candidate": f.get("certified_candidate") is True,
               "threshold_of_48": THRESH.get(name, DEFAULT), "per_set": {}, "pooled": {}}
        ok = True
        for sname, rids in sets.items():
            if name == "marks_per_part":
                docs = {}
                for rid in rids:
                    docs.setdefault(doc_of[rid], []).append(rid)
                agree_docs = sum(1 for d_, rr in docs.items()
                                 if all(M.same(f, first["marks"][r].get(name), second["marks"][r].get(name)) for r in rr))
                thr = math.ceil(THRESH[name] / 48 * len(docs))
                row["per_set"][sname] = {"documents": len(docs), "agree_documents": agree_docs, "threshold": thr,
                                         "reports": len(rids), "agree_reports": agree_set(rids)[0]}
                ok = ok and agree_docs >= thr
            else:
                a, d, u = agree_set(rids)
                thr = THRESH.get(name, DEFAULT)
                row["per_set"][sname] = {"reports": len(rids), "agree": a, "disagree": d, "unreadable": u, "threshold": thr}
                ok = ok and a >= thr
        a, d, u = agree_set(shared)
        row["pooled"] = {"reports": len(shared), "agree": a, "disagree": d, "unreadable": u}
        # W10.17 readability
        if f["kind"] == "enum":
            inlist = lambda mk: sum(1 for rid in shared if mk["marks"][rid].get(name) in f.get("values", []))
            row["in_list"] = {"first": inlist(first), "second": inlist(second)}
            if min(row["in_list"].values()) < 95:
                row["unreadable_W10_17"] = True
                out["unreadable"].append(name); ok = False
        if name in REWORDED_TWICE:
            rr = [r for r in shared if r in read]; ur = [r for r in shared if r not in read]
            ar, dr, _ = agree_set(rr); au, du, _ = agree_set(ur)
            pr = 100 * ar / max(1, ar + dr); pu = 100 * au / max(1, au + du)
            row["split"] = {"read": {"n": len(rr), "agree": ar}, "unread": {"n": len(ur), "agree": au},
                            "read_pct": round(pr, 1), "unread_pct": round(pu, 1),
                            "W10_16_falsified": (pr - pu) > 10}
        row["certified"] = bool(ok and row["certified_candidate"])
        out["fields"][name] = row
        if row["certified"]:
            out["certified"].append(name)
    trio = [n for n in TRIO if out["fields"].get(n, {}).get("certified")]
    out["P3.1"] = {"rule": "at least two of shape, turned_own_test, same_explanation at 44 of 48 in each set",
                   "held": len(trio) >= 2, "reached": trio}
    out["P3.2"] = {"rule": "marks_per_part, pairs_that_pull, rivals_built each 40 of 48 in each set",
                   "held": all(out["fields"].get(n, {}).get("certified") for n in REWORDED_TWICE)}
    out["P3.3"] = {"rule": "question_identity 46 of 48 in each set", "held": out["fields"].get("question_identity", {}).get("certified", False)}
    out["P3.5"] = {"rule": "test_swap and test_poke each 42 of 48 in each set",
                   "held": all(out["fields"].get(n, {}).get("certified") for n in ("test_swap", "test_poke"))}
    out["P3.4"] = {"rule": "at most one field a second rewording", "held": False,
                   "note": "failed on the count before any mark (marking plan 14.4; W13); recorded, not re-read"}
    out["W10.16"] = {"falsified_on": [n for n in REWORDED_TWICE if out["fields"].get(n, {}).get("split", {}).get("W10_16_falsified")]}
    out["W10.17"] = {"unreadable": out["unreadable"]}
    f = os.path.join(MARKING, f"stage_b_{o.reader}.json")
    write_json(f, out)
    print(f"stage B over {len(shared)} shared reports; sets {out['sets']}; read reports {len(read)}")
    print(f"  {'field':30} {'close a/thr':>12} {'repeat a/thr':>13} {'pooled':>8} {'cert':>5}")
    for name, row in out["fields"].items():
        c = row["per_set"]["close"]; r = row["per_set"]["repeat"]
        ca = c.get("agree_documents", c.get("agree")); cth = c["threshold"]
        ra = r.get("agree_documents", r.get("agree")); rth = r["threshold"]
        print(f"  {name:30} {str(ca)+'/'+str(cth):>12} {str(ra)+'/'+str(rth):>13} {row['pooled']['agree']:>8} {'yes' if row['certified'] else ('cand' if row['certified_candidate'] else '-'):>5}"
              + (f"   split read {row['split']['read_pct']}% unread {row['split']['unread_pct']}%" if 'split' in row else "")
              + ("   UNREADABLE (W10.17)" if row.get("unreadable_W10_17") else ""))
    for k in ("P3.1", "P3.2", "P3.3", "P3.5"):
        print(f"  {k}: held={out[k]['held']}")
    print(f"  certified: {out['certified']}\n  written {f}")


def rig_document(rid):
    p = os.path.join(rig.RUNS, "record96", rid + ".json")
    return read_json(p).get("document") if os.path.exists(p) else None


if __name__ == "__main__":
    main()
