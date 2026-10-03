# S109 Part B round 1: the scope runs (section Bn runs/scope.json) as tables for the section files and the map.
#   python3 -B s109b_scope_tables.py Bn     -> prints markdown; writes `section Bn runs/scope tables.json`
# A case counts as moved only where Acc, a conjunct's value, or Expl on a hand-set history differs (a conjunct the variant adds
# and that holds, such as 'question T', is not a move).
import json, os, re, sys

sec = sys.argv[1]
C = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "section %s runs" % sec)
d = json.load(open(os.path.join(C, "scope.json"), encoding="utf-8"))
OWNER = {"sign two parts (edit)": "S44 the shop sign, two parts (red on Mon, blue on Tue)",
         "sign two parts (boundary)": "owner's sign, change as boundary: two parts",
         "sign two parts (mixed)": "owner's sign, change as mixed: two parts",
         "vane M13 (edit)": "M13: the owner's weathervane (S41 Q15)",
         "vane Γ={cW} (boundary)": "owner's vane, change as boundary: D_vane Γ = {cW} (the wind's commitment)",
         "vane ℰ_mix (mixed)": "owner's vane, change as mixed: D_vane^mix Γ = {cW} (the reply's ℰ_mix)"}
base = {b["label"]: b for b in d["base"]}


def norm(s):
    return s.replace(" question T", "")


def real(m):
    return norm(m["off"]) != norm(m["on"])


def st(acc, expl):
    return "Acc %s, Expl %s" % ("T" if acc else "F", "/".join("T" if x else "F" for x in expl))


out = {"section": sec, "n_cases": len(d["cases"]), "n_worked": d["n_worked"], "worlds_n": d["worlds_n"], "worlds_acc_base": d["worlds_acc_base"],
       "worlds_expl_sel_base": d["worlds_expl_sel_base"], "readings": {}}
lines = ["cases: %d (%d worked, %d encodings of the owner's two cases); generated %d (Acc T under none: %d; Expl on a Sel history: %d)"
         % (len(d["cases"]), d["n_worked"], len(d["cases"]) - d["n_worked"], d["worlds_n"], d["worlds_acc_base"], d["worlds_expl_sel_base"]), ""]
lines.append("| reading | worked and owner's-case encodings moved (Acc in / out / Expl only) | owner's cases (off → on, Expl on Dec/Con/Sel histories) | student's copy | generated: Acc in/out, Expl(Sel) in/out | FC-E, CT scripts |")
lines.append("|---|---|---|---|---|---|")
for lab, r in d["variants"].items():
    mv = [m for m in r["moved"] if real(m)]
    ain = [m["label"] for m in mv if m["acc"] == [False, True]]
    aout = [m["label"] for m in mv if m["acc"] == [True, False]]
    eonly = [m["label"] for m in mv if m["acc"][0] == m["acc"][1]]
    own = {}
    for k, lab2 in OWNER.items():
        m = [x for x in mv if x["label"] == lab2]
        b = base[lab2]
        if m:
            own[k] = "%s → %s" % (st(m[0]["acc"][0], [e[0] for e in m[0]["expl"]]), st(m[0]["acc"][1], [e[1] for e in m[0]["expl"]]))
        else:
            own[k] = "stays (%s)" % st(b["acc"], [b["prov"][h][3] for h in ("Dec", "Con", "Sel")])
    stu = r["student"]
    stxt = "moves: %s" % "; ".join("%s: Dec %s → %s" % (h, d["student_base"]["rows"][h]["dec"], stu["rows"][h]["dec"]) for h in stu["rows"]) if r["student_moves"] else "stays (Acc %s, Dec at o2 %s)" % (stu["acc"], stu["rows"]["H={(1,b1_45)}"]["dec"])
    w = r.get("worlds")
    wtxt = ("%d / %d, %d / %d" % (w["acc_in"], w["acc_out"], w["expl_in"], w["expl_out"])) if w else "not run"
    sc = [s for s, v in r["scripts"].items() if not v["same"]]
    rec = dict(ain=ain, aout=aout, eonly=eonly, owner=own, student=stxt, worlds=w, scripts={s: r["scripts"][s] for s in sc},
               chains=r.get("chains"), bridge=r.get("bridge"))
    out["readings"][lab] = rec
    lines.append("| %s | %d (%d / %d / %d) | %s | %s | %s | %s |" % (lab, len(mv), len(ain), len(aout), len(eonly),
                                                             "; ".join("%s: %s" % kv for kv in own.items() if not kv[1].startswith("stays")) or "all stay",
                                                             stxt, wtxt, ", ".join(sc) or "same"))
lines.append("")
for lab, rec in out["readings"].items():
    w_ = rec["worlds"] or {}
    if rec["ain"] or rec["aout"] or rec["eonly"] or any(w_.get(k) for k in ("acc_in", "acc_out", "expl_in", "expl_out")) or rec["scripts"] or rec["chains"] or rec["bridge"]:
        lines.append("**%s**: Acc in: %s. Acc out: %s. Expl only: %s." % (lab, "; ".join(rec["ain"]) or "none", "; ".join(rec["aout"]) or "none", "; ".join(rec["eonly"]) or "none"))
    if rec["worlds"] and (rec["worlds"]["acc_in"] or rec["worlds"]["acc_out"] or rec["worlds"]["expl_in"] or rec["worlds"]["expl_out"]):
        lines.append("   generated, by kind: %s; conjunct moved: %s" % (rec["worlds"]["kinds"], rec["worlds"]["conj_moved"]))
    if rec["chains"]:
        lines.append("   chains: %s of %s differ; output Dec → not Dec %s, not Dec → Dec %s; fixed-point count changed %s" % (
            rec["chains"]["differ"], rec["chains"]["total"], rec["chains"]["output_dec_to_not"], rec["chains"]["output_not_to_dec"], rec["chains"]["fixed_point_count_changed"]))
    if rec["bridge"]:
        lines.append("   bridge: off %s; on %s" % (rec["bridge"]["off"], rec["bridge"]["on"]))
    for s, v in rec["scripts"].items():
        lines.append("   %s differs: off-only lines %d, on-only lines %d; first on-only: %s" % (s, len(v.get("lines_only_off", [])), len(v.get("lines_only_on", [])), (v.get("lines_only_on") or [""])[0][:200]))
json.dump(out, open(os.path.join(C, "scope tables.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\n".join(lines))
