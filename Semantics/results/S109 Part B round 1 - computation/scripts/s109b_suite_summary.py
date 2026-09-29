# S109 Part B round 1: the whole-suite runs, per variant, against the record after round 4 (the claims that move).
#   python3 -B s109b_suite_summary.py   (reads `whole suite/<section>/*.json`, writes `whole suite/summary.json` and `.md`)
import glob, json, os
W = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "whole suite")
rows, out = [], {}
for f in sorted(glob.glob(os.path.join(W, "B*", "*.json"))):
    d = json.load(open(f, encoding="utf-8"))
    sec, tag = f.split(os.sep)[-2], os.path.basename(f)[:-5]
    diffs = d.get("differences", [])
    out["%s %s" % (sec, tag)] = dict(exit=d["exit"], timed_out=d["timed_out"], seconds=d["seconds"], counts=d["counts"], ok=d["ok"],
                                     claims_with_error=d["claims_with_error"], model_folder_changed=d["model_folder_changed"],
                                     pycache_new=d["pycache_new"], differences=diffs, raw_md5=d["raw_md5"])
    AB = {"HOLDS ON ALL MODELS TRIED": "H", "COUNTEREXAMPLE FOUND": "CEX", "NOT TESTED": "NT"}
    per = {}
    for x in diffs:
        c = per.setdefault(x["id"], {"status": None, "parts": []})
        if x["what"] == "status":
            c["status"] = "%s→%s" % (AB.get(x["recorded"], x["recorded"]), AB.get(x["got"], x["got"]))
        elif x["what"] == "parts":
            rec = {p[0]: p[2] for p in (x["recorded"] or [])}
            got = {p[0]: p[2] for p in (x["got"] or [])}
            c["parts"] = [l[:48] for l in sorted(set(rec) | set(got)) if rec.get(l) != got.get(l)]
        else:
            c["parts"].append(x["what"])
    out["%s %s" % (sec, tag)]["moved"] = per
    # the printout of every moved claim, kept (the whole printout stays in the scratchpad: d["raw"])
    blocks = {}
    try:
        raw = open(d["raw"], encoding="utf-8").read().split("\n" + "=" * 100 + "\n")
        for b in raw:
            fl = [l for l in b.strip().split("\n") if l.startswith("FC")]
            head = fl[0].split("  ")[0] if fl else ""
            if head in per:
                blocks[head] = b.strip()[:6000]
    except OSError:
        pass
    out["%s %s" % (sec, tag)]["printouts_of_moved_claims"] = blocks
    moved = ["%s %s" % (k, v["status"] or ("parts: " + " / ".join(v["parts"][:2]))) for k, v in sorted(per.items())]
    rows.append("| %s | %s | %s | %d s | H %d, CEX %d, NT %d | %s | %s |" % (sec, tag, d["exit"], d["seconds"], d["counts"]["H"], d["counts"]["CEX"], d["counts"]["NT"],
                                                                     "; ".join(map(str, moved)) or "none", "error: %s" % d["claims_with_error"] if d["claims_with_error"] else ""))
json.dump(out, open(os.path.join(W, "summary.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
md = ["# S109 Part B round 1 - the whole suite per variant", "", "Each run: `tools/sonnet_harness/run_claims.py` on the section's copy with `S109B_VARIANT` (and its reading) set, scale 4, time cap 45 s, compared with `formal claims, after round 4.json` (key after_round4). Moved = claims whose status or a part's status differs from the record.", "",
      "| section | variant | exit | time | counts (of 142) | claims that move | note |", "|---|---|---|---|---|---|---|"] + rows
open(os.path.join(W, "summary.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
print("\n".join(md))
