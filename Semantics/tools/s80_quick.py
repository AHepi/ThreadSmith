#!/usr/bin/env python3
"""s80_quick.py: round S80 cut to a quick verdict (plan S80, third version, decided by Claude on the owner's word of
23 September 2026: "HV isn't the central job ... Just a quick verdict is enough. And you are the authority").
Three API readers (atria, mimo, deepseek), thinking on, three conditions (ST skill, PT placebo, NT nothing), the seeded
document only, three repetitions: 27 reports. One marker per report, never the reader's own model; Claude reads every
mark against the report and the key and settles the verdict.
  python Semantics/tools/s80_quick.py readers
  python Semantics/tools/s80_quick.py mark KEY_FILE
  python Semantics/tools/s80_quick.py table KEY_FILE
Reuses s80_common (texts, key slicer, mark validator) and s80_call (the caller) of the second version.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import s80_common as C
from s80_call import call
from s80_run import run_pool, system_text, reader_user_text, check_methods, marker_user_text

OUT = os.path.join(C.S, "results", "S80 Quick verdict - outputs")
RD, MD = os.path.join(OUT, "readers"), os.path.join(OUT, "marks")
MODELS, CONDS, REPS = ["atria", "mimo", "deepseek"], {"ST": "S", "PT": "P", "NT": "N"}, 3
MARKER = {"atria": ["mimo"] * 3, "mimo": ["atria"] * 3, "deepseek": ["atria", "mimo", "atria"]}


def tags():
    return [(m, c, r) for m in MODELS for c in CONDS for r in range(1, REPS + 1)]


def readers():
    if os.path.isdir(MD) and os.listdir(MD):
        raise SystemExit("marks exist; readers refuse to run")
    C.check_documents(); check_methods()
    systems = {k: system_text(k) for k in "SPN"}
    user = reader_user_text("seeded")
    jobs = [dict(tag=f"{m}_{c}_seeded_r{r}", model=m, method=CONDS[c], out=RD) for m, c, r in tags()]
    run_pool(jobs, lambda j: call(j["model"], systems[j["method"]], user, RD, j["tag"], True, C.READER_LADDER))


def mark(key_file):
    key = C.load_key(key_file)
    task = C.read(os.path.join(C.PR, "marker task.md"))
    jobs = []
    for m, c, r in tags():
        t = f"{m}_{c}_seeded_r{r}"
        p = os.path.join(RD, t + ".response.txt")
        if not os.path.exists(p):
            print("missing", t); continue
        mk = MARKER[m][r - 1]
        rid = "Q%02d" % (len(jobs) + 1)   # neutral id; the tag is kept in marks/MAP.json only
        jobs.append(dict(tag=f"{rid}_by_{mk}", model=mk, t=t, rid=rid, out=MD,
                         user=marker_user_text(task, key, "seeded", rid, C.read(p))))
    os.makedirs(MD, exist_ok=True)
    C.write_atomic(os.path.join(MD, "MAP.json"), json.dumps({j["rid"]: j["t"] for j in jobs}, indent=1))
    acc = lambda res: ((res["finish"] == "stop" and C.validate_mark(res["content"], C.KEY_IDS_SEEDED)[0] is not None),
                       "not a valid mark")
    run_pool(jobs, lambda j: call(j["model"], None, j["user"], MD, j["tag"], True, C.MARKER_LADDER, accept=acc))


def table(key_file):
    key = C.load_key(key_file)
    mp = json.load(open(os.path.join(MD, "MAP.json")))
    rows = []
    for rid, t in sorted(mp.items()):
        m, c, _, r = t.split("_")
        f = [x for x in os.listdir(MD) if x.startswith(rid + "_by_") and x.endswith(".response.txt")]
        if not f:
            rows.append((m, c, r, None)); continue
        mk, _ = C.validate_mark(C.read(os.path.join(MD, f[0])), C.KEY_IDS_SEEDED)
        found = {k: v["verdict"] for k, v in mk["key"].items()}
        hv = sum(found[k] == "FOUND" for k in found if key["kinds"][k] == "HV")
        gen = sum(found[k] == "FOUND" for k in found if key["kinds"][k] == "GEN")
        others = [o["verdict"] for o in mk["others"]]
        rows.append((m, c, r, dict(hv=hv, gen=gen, d3=found["D3"] == "FOUND", items=mk["report_items_total"],
                                   mistaken=others.count("MISTAKEN"), found=found, marker=f[0].split("_by_")[1][:-13])))
    out = ["| reader | cond | rep | marker | HV of 4 | GEN of 4 | D3 | items | mistaken | per error |", "|" + "---|" * 10]
    for m, c, r, d in rows:
        if d is None:
            out.append(f"| {m} | {c} | {r} | - | missing | | | | | |"); continue
        pe = " ".join(k + ("+" if v == "FOUND" else "~" if v == "PARTIAL" else "-") for k, v in d["found"].items())
        out.append(f"| {m} | {c} | {r} | {d['marker']} | {d['hv']} | {d['gen']} | {'yes' if d['d3'] else 'no'} | "
                   f"{d['items']} | {d['mistaken']} | {pe} |")
    out += ["", "| reader | cond | mean HV | mean GEN | mean mistaken | mean items |", "|---|---|---|---|---|---|"]
    for m in MODELS:
        for c in CONDS:
            ds = [d for mm, cc, _, d in rows if mm == m and cc == c and d]
            if ds:
                mean = lambda k: sum(d[k] for d in ds) / len(ds)
                out.append(f"| {m} | {c} | {mean('hv'):.2f} | {mean('gen'):.2f} | {mean('mistaken'):.2f} | {mean('items'):.1f} |")
    C.write(os.path.join(OUT, "TABLE.md"), "\n".join(out) + "\n")
    print("\n".join(out))


if __name__ == "__main__":
    {"readers": lambda: readers(), "mark": lambda: mark(sys.argv[2]), "table": lambda: table(sys.argv[2])}[sys.argv[1]]()
