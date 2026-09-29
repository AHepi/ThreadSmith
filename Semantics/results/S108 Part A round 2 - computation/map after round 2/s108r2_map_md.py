"""Fill the generated tables of the map's .md (between <!-- x --> and <!-- /x -->) from the map's .json and the section
files' expected suite moves. Run after s108r2_map_build.py.  python3 -B s108r2_map_md.py"""
import json, re

RES = "/home/user/ThreadSmith/Semantics/results/"
MD = RES + "S108 Part A round 2 - the dependency map, after round 2.md"
M = json.load(open(RES + "S108 Part A round 2 - the dependency map, after round 2.json", encoding="utf-8"))
S1EXP = json.load(open(RES + "S108 Part A round 2 - computation/section 1 runs/suite - expected moves.json", encoding="utf-8"))["runs"]
# expected moves (claim ids) from the section files: section 2 §6 (single-claim runs; lower bounds where marked), section 3
# §9 (single-claim runs), section 4 (what each variant reads)
EXP = {
    "section 2/s00": [], "section 2/s01": ["FC26", "FC34"], "section 2/s02": ["FC34"], "section 2/s03": ["FC34"],
    "section 2/s04": "≥ FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC25.new2, FC26, FC27.new1, FC34, FC72.new2",
    "section 2/s05": "≥ as s04", "section 2/s06": "≥ as s04", "section 2/s07": [], "section 2/s08": [], "section 2/s09": [],
    "section 2/s10": [], "section 2/s11": ["FC12.new2", "FC30.new1", "FC83", "FC98", "FC98.new1"], "section 2/s12": [],
    "section 2/s13": ["FC22", "FC23.new1", "FC23.new2", "FC23.new5"],
    "section 2/s14": "≥ FC22, FC23, FC23.new1, FC23.new2, FC23.new3, FC23.new5, FC25.new2, FC26, FC27.new1, FC34, FC72.new2, FC74",
    "section 2/s15": ["FC31"], "section 2/s16": [], "section 2/s17": "none; FC21.v1, FC21.v2 new (both hold)",
    "section 3/off": [], "section 3/R2V3.1": ["FC90.new1"], "section 3/R2V3.2-contract": [], "section 3/R2V3.4-ports": [],
    "section 3/R2V3.4-edits": [], "section 3/R2V3.5": ["FC102.new1", "FC104.new1", "FC12.new1", "FC12.new2", "FC30.new1", "FC77", "FC80.new1", "FC83"],
    "section 3/R2V3.6": [], "section 3/R2V3.7": [], "section 3/R2V3.8": ["FC72", "FC72.new1"], "section 3/R2V3.9": ["FC68"],
    "section 3/R2V3.10": ["FC32.new1"], "section 4/off": [],
    "section 4/R2V4.1-some": "the claims that form being an explanation under V4.1 (round 1's 'every' co-varied: 1–2 claims)",
    "section 4/R2V4.1-some-exempt": "as R2V4.1-some", "section 4/R2V4.1-some-exempt-set": "as R2V4.1-some",
    "section 4/R2V4.5": ["FC102.new1", "FC103.new1"], "section 4/R2V4.7": "the claims that read usable / X_j",
}
for k, v in S1EXP.items():
    EXP["section 1/" + k] = v["moved"]
LABEL = {"section 2/s%02d" % i: l for i, l in enumerate(
    ["off", "'some' ((E) as it is)", "'some-exempt'", "'some-exempt-set'", "V2.4 × 'some'", "V2.4 × 'some-exempt'",
     "V2.4 × 'some-exempt-set'", "R2V2.3a", "R2V2.5", "R2V2.6 written", "R2V2.6 HS", "R2V2.6 reply", "R2V2.8 target",
     "R2V2.8 program", "R2V2.8 widest", "R2V2.9", "R2V2.10", "R2V2.11"])}


def fill(md, key, text):
    return re.sub(r"(<!-- %s -->\n).*?(<!-- /%s -->)" % (key, key), lambda m: m.group(1) + text + "\n" + m.group(2), md, flags=re.S)


md = open(MD, encoding="utf-8").read()
rows = ["| edge | round-1 standing | after round 2 | what changed it | what shows it (cut) |", "|---|---|---|---|---|"]
for c in M["round2"]["changes"]:
    rows.append("| %s | %s | %s | %s | %s |" % (c["edge"], c["round1_standing"], c["after_round2"], c["what_changed_it"],
                                              c["why"].replace("|", "/").replace("\n", " ")[:420]))
md = fill(md, "changes", "\n".join(rows))

rows = ["| run | setting | H / CEX / NT of | moved (status or a part) | of them parts only | expected (section file) | as expected |",
        "|---|---|---|---|---|---|---|"]
done = pend = 0
for k, v in M["round2"]["suite"].items():
    exp = EXP.get(k, "–")
    if "counts" not in v:
        rows.append("| %s | %s | not yet run | – | – | %s | – |" % (k, LABEL.get(k, k.split("/")[1]), exp if isinstance(exp, str) else ", ".join(exp) or "none"))
        pend += 1
        continue
    done += 1
    c = v["counts"]
    extra = v["not_in_record"]
    if isinstance(exp, list):
        same = "yes" if sorted(exp) == v["moved"] else ("no: + %s; − %s" % (", ".join(sorted(set(v["moved"]) - set(exp))) or "–",
                                                                          ", ".join(sorted(set(exp) - set(v["moved"]))) or "–"))
        exps = ", ".join(exp) or "none"
    else:
        same, exps = "see the section file", exp
    rows.append("| %s | %s | %d / %d / %d of %d%s | %s | %s | %s | %s |" % (
        k, LABEL.get(k, k.split("/")[1]), c["H"], c["CEX"], c["NT"], c["of"], (" (+ %s)" % ", ".join(extra)) if extra else "",
        ", ".join(v["moved"]) or "none", ", ".join(v["parts_only"]) or "–", exps, same))
rows.append("")
rows.append("%d runs in; %d not yet run when this table was generated. No run timed out%s; no run changed its program folder%s." % (
    done, pend, "" if not any(v.get("timed_out") for v in M["round2"]["suite"].values()) else " (EXCEPT the runs marked)",
    "" if not any(v.get("folder_changed") for v in M["round2"]["suite"].values()) else " (EXCEPT the runs marked)"))
md = fill(md, "suite", "\n".join(rows))

rows = ["| stretch | FROZEN: computed / claimed only / untouched | middle: computed / claimed only / untouched |", "|---|---|---|"]
t = M["gaps"]["touched_by_stretch"]
for s in ("S1", "S2", "S3", "S4"):
    f, m = t.get(s + " FROZEN", {}), t.get(s + " middle", {})
    rows.append("| %s | %d / %d / %d | %d / %d / %d |" % (s, f.get("computed", 0), f.get("claimed only", 0), f.get("untouched", 0),
                                                        m.get("computed", 0), m.get("claimed only", 0), m.get("untouched", 0)))
rows.append("\n(After round 1: S1 7 / 7 / 43, 18 / 4 / 132; S2 28 / 5 / 62, 39 / 6 / 108; S3 9 / 1 / 39, 17 / 0 / 120; S4 7 / 0 / 30, 17 / 3 / 113.)")
md = fill(md, "stretch", "\n".join(rows))
open(MD, "w", encoding="utf-8").write(md)
print("filled; suite runs in %d, pending %d" % (done, pend))
