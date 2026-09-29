# S109 Part B round 1 (rules 5 and 6): builds the four "section Bn - variants computed" files (.md, .json) and the map of how
# explanation changes in meaning and scope (.md, .json) from the hand record (s109b_data.py), the scope runs (section Bn
# runs/scope tables.json) and the whole-suite results (whole suite/summary.json).
#   python3 -B s109b_map_build.py
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
COMP = os.path.dirname(HERE)
RES = os.path.dirname(COMP)
sys.path.insert(0, HERE)
from s109b_data import V, PARTS  # noqa: E402

PB = "S109 Part B round 1 - "
suite = json.load(open(os.path.join(COMP, "whole suite", "summary.json"), encoding="utf-8"))
scope = {}
for s in ("B1", "B2", "B3"):
    scope[s] = json.load(open(os.path.join(COMP, "section %s runs" % s, "scope tables.json"), encoding="utf-8"))
b4 = json.load(open(os.path.join(COMP, "section B4 runs", "scope.json"), encoding="utf-8"))
TITLES = {"B1": "organizations, kinds, questions and contracts", "B2": "transports, fidelity, the account, routes and the exact constructions",
          "B3": "provenance, histories, representation, construction, repair and the physical module",
          "B4": "rivals, problems, criticism, the class, what would rule it out, and the Arguments"}


def moved_claims(v):
    out = {}
    for key in v["suite"]:
        for c, m in suite[key]["moved"].items():
            out.setdefault(c, []).append("%s%s" % (m["status"] or "parts: " + " / ".join(m["parts"][:2]), "" if len(v["suite"]) == 1 else " (%s)" % key.split(" ", 1)[1]))
    return out


def scope_rows(v):
    rows = []
    for lab in v["readings"]:
        if v["section"] == "B4":
            r = b4["variants"][lab]
            mv = [m for m in r["moved"] if m["off"].replace(" question T", "") != m["on"].replace(" question T", "")]
            rows.append(dict(reading=lab, moved=len(mv), acc_in=[], acc_out=[], expl_only=[m["label"] for m in mv], owner="all stay (B4 reads neither (E) nor Dec)",
                             student="stays" if not r["student_moves"] else "moves", worlds="not run (B4 code reads neither Acc nor Dec)",
                             scripts=[s for s, x in r["scripts"].items() if not x["same"]], chains=None, bridge=None))
            continue
        r = scope[v["section"]]["readings"][lab]
        w = r["worlds"]
        own = "; ".join("%s: %s" % kv for kv in r["owner"].items() if not kv[1].startswith("stays")) or "all stay"
        rows.append(dict(reading=lab, moved=len(r["ain"]) + len(r["aout"]) + len(r["eonly"]), acc_in=r["ain"], acc_out=r["aout"], expl_only=r["eonly"],
                         owner=own, student=r["student"],
                         worlds=("Acc in %d, out %d; Expl (Sel history) in %d, out %d" % (w["acc_in"], w["acc_out"], w["expl_in"], w["expl_out"])) if w else "not run",
                         scripts=list(r["scripts"].keys()), chains=r["chains"], bridge=r["bridge"]))
    return rows


def md_section(sec):
    vs = [v for v in V.values() if v["section"] == sec]
    L = ["# S109 Part B round 1 - section %s (%s) - variants computed" % (sec, TITLES[sec]), "",
         "*Rule 5 of `S109 Part B round 1 - how the replies will be read, written before sending.md`. The one Opus 5.5 agent of decision S56 (effort high). "
         "Works only in `S109 Part B round 1 - computation/section %s model/` (a copy of `S107 Round 4 - maths after the reading/model after round 4/`, 26 files md5-identical at the copy; "
         "the original and Part A's copies never written). Read with the reply (`returns/s109_glm_section%s.response.txt`) and the tabulation (`S109 Part B round 1 - tabulation of the replies, before any ruling.md`). "
         "Built by `computation/map/s109b_map_build.py` from the hand record `computation/map/s109b_data.py`, the scope runs and the whole-suite results. "
         "Nothing here changes the theory (rule 13). \"Candidate\" or \"explanation\" for what the theory judges; \"model\" only for the program or a small structure it builds (S43).*" % (sec, sec[1]), "",
         "Status: complete, 29 September 2026.", "",
         "## 0. Setup", "",
         "| item | state |", "|---|---|",
         "| copy | `model after round 4/`, 26 files identical at the copy (md5 list compared) |",
         "| switches | `S109B_VARIANT` in the environment (a case script sets `core.S109B`); readings: %s; every change is guarded by the switch, the patch is `computation/patches/patch_%s.py` |" % (
             {"B1": "`S109B_THETA` (all, strict)", "B2": "`S109B_NC0` (bg, bg-input), `S105_SLOT_QUANTIFIER` (the program's)", "B3": "none beyond the variant", "B4": "`S109B_HELD` (all, no-records)"}[sec], sec),
         "| default unchanged | the whole suite in the B3 copy with every switch off equals the record after round 4 (142 of 142 claims, `whole suite/B3/none.json`); the scope script's 'none' values equal Part A's section 2 copy's on all 17,329 cases (`comparisons with Part A/`) |",
         "| scope | `computation/scripts/s109b_scope.py` → `section %s runs/scope.json`, `scope.txt`, `scope tables.md` / `.json`: the 27 worked cases and 22 encodings of the owner's sign and vane (edit, boundary, mixed; E_enc on each question), the student's copy (FC30.new1 (d)), %s FC-E1-E5 (`s104_external.py`) and CT1-CT8 (`s104_creative_transport.py`) against their output under 'none'%s |" % (
             sec, "the generated worlds (SMALL, 160 per size, seed 109001: 17,280 candidates, 999 meeting (E)), " if sec != "B4" else "", "; every chain of 1 to 3 holdings (584) and the bridge's chains (FC84.new1 (a1), (a2))" if sec == "B3" else ""),
         "| the replies' small cases | `computation/scripts/s109b_small_cases.py` → `section %s runs/small cases.txt` (B1, B2) |" % sec,
         "| whole suite | `tools/sonnet_harness/run_claims.py` per variant and reading, scale 4, time cap 45, PYTHONHASHSEED=0, from the copy's parent, under `timeout`, output in the scratchpad, results copied to `whole suite/%s/` and summarized in `whole suite/summary.md` / `.json` (the moved claims' printouts kept there) |" % sec,
         "", "## 1. What is implemented, and the inventions it forced (S36)", "",
         "| id | free item(s) | kind | carry-over | implemented | switch | inventions (other choices) |", "|---|---|---|---|---|---|---|"]
    for v in vs:
        L.append("| %s | %s | %s | %s | %s | %s | %s |" % (v["id"], ", ".join(v["free"]), v["kind"], v["carry"], v["impl"], v["switch"], "; ".join(v["inventions"]) or "none"))
    L += ["", "## 2. Meaning: the changed formal statement, old beside new, of each part of the explanation definition that moves", "",
          "| id | part | old | new |", "|---|---|---|---|"]
    for v in vs:
        for part, old, new in v["meaning"]:
            L.append("| %s | %s | %s | %s |" % (v["id"], part, old, new))
    L += ["", "## 3. Scope: computed, the variant off against on", ""]
    for v in vs:
        L.append("### %s" % v["id"])
        L.append("")
        L.append(v["scope_note"])
        L.append("")
        rows = scope_rows(v)
        if rows:
            L.append("| reading | cases moved (Acc in / out / Expl only) | the owner's sign and vane (off → on; Expl on Dec/Con/Sel histories) | the student's copy | generated | FC-E, CT |")
            L.append("|---|---|---|---|---|---|")
            for r in rows:
                L.append("| %s | %d (%d / %d / %d) | %s | %s | %s | %s |" % (r["reading"], r["moved"], len(r["acc_in"]), len(r["acc_out"]), len(r["expl_only"]), r["owner"], r["student"], r["worlds"], ", ".join(r["scripts"]) or "same"))
            for r in rows:
                if r["acc_in"] or r["acc_out"]:
                    L.append("")
                    L.append("%s: enter: %s. Leave: %s." % (r["reading"], "; ".join(r["acc_in"]) or "none", "; ".join(r["acc_out"]) or "none"))
                if r["chains"]:
                    L.append("")
                    L.append("%s, chains: %d of %d differ; at the output Dec → not Dec %d, not Dec → Dec %d; number of fixed points changed %d. The bridge: %s." % (
                        r["reading"], r["chains"]["differ"], r["chains"]["total"], r["chains"]["output_dec_to_not"], r["chains"]["output_not_to_dec"], r["chains"]["fixed_point_count_changed"],
                        "stays (Con and Build at the output under (a1) and (a2))" if r["bridge"] and r["bridge"]["on"] == r["bridge"]["off"] else r["bridge"]))
        mc = moved_claims(v)
        L.append("")
        L.append("Claims that move (whole suite): %s." % ("; ".join("%s %s" % (c, ", ".join(x)) for c, x in sorted(mc.items())) if v["suite"] and mc else ("none" if v["suite"] else "the whole suite was not run: " + ("no code changes" if "no code" in v["impl"] else "no claim reads the changed code" if v["id"] == "PB1.5" else "flagged out"))))
        L.append("")
    L += ["## 4. Edges", "", "| id | kind | item | standing | Part A id | why |", "|---|---|---|---|---|---|"]
    for v in vs:
        for e in v["edges"]:
            L.append("| %s | %s | %s | %s | %s | %s |" % (v["id"], e[0], e[1], e[2], e[3] or "–", e[4]))
    L += ["", "Nothing here is a change to the theory (rule 13). Written by one Opus 5.5 agent under rule 5 and decision S56, 29 September 2026."]
    return "\n".join(L) + "\n"


def rec_json(v):
    return dict(id=v["id"], section=v["section"], free=v["free"], kind=v["kind"], carry=v["carry"], implemented=v["impl"], switch=v["switch"],
                inventions=v["inventions"], meaning=[dict(part=p, old=o, new=n) for p, o, n in v["meaning"]], scope_note=v["scope_note"],
                scope=scope_rows(v), claims_moved=moved_claims(v), suite_runs=v["suite"],
                edges=[dict(kind=e[0], item=e[1], standing=e[2], part_A=e[3], why=e[4]) for e in v["edges"]])


for sec in ("B1", "B2", "B3", "B4"):
    open(os.path.join(RES, PB + "section %s - variants computed.md" % sec), "w", encoding="utf-8").write(md_section(sec))
    json.dump(dict(section=sec, status="complete", variants=[rec_json(v) for v in V.values() if v["section"] == sec]),
              open(os.path.join(RES, PB + "section %s - variants computed.json" % sec), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("four section files written")
