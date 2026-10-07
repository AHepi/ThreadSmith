# S104 round 2 (maths): adds the program's inventions (I77 onward) and every search result to the
# inventions register and to the formal claims. Idempotent: it first rebuilds the register and the
# claims from their sources with s104_build.py, then adds to them. Run after `python3 -m model.run`:
#   python3 -m model.register
import json
import os
import re
import subprocess
import sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, HERE)
from s104_check import check, MD5, check_markdown  # noqa: E402
from .inventions_model import INVENTIONS_MODEL  # noqa: E402

TEXT_NAME = "tests/103 The semantics, standing alone, after round 1.md"
DATE = "27 September 2026"


def q_md(l, q):
    return "> L%d | %s" % (l, q)


def fmt_results(rows):
    if not rows:
        return "none: no test used it"
    out = []
    for x in rows:
        if x["counterexample_parts"]:
            out.append("%s — counterexample (%s)" % (x["claim"], "; ".join(x["counterexample_parts"])))
        elif x["status"] == "COUNTEREXAMPLE FOUND":
            out.append("%s — counterexample in a part that does not use it; its other parts hold on all models tried" % x["claim"])
        else:
            out.append("%s — %s" % (x["claim"], x["status"].lower()))
    return "; ".join(out)


def main():
    r = subprocess.run([sys.executable, os.path.join(HERE, "s104_build.py")], capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        print(r.stderr)
        sys.exit("s104_build.py failed")
    SR = json.load(open(os.path.join(HERE, "search results.json"), encoding="utf-8"))
    inv_res = SR["inventions_results"]
    errors = []
    for i in INVENTIONS_MODEL:
        for l, q in i["quotes"]:
            m = check(l, q)
            if m:
                errors.append("%s %s" % (i["id"], m))
    if errors:
        sys.exit("\n".join(errors))
    # claims that use each program invention (from the tests' own tags)
    uses = OrderedDict()
    for res in SR["results"]:
        for i in res["program_inventions"] + [x for p in res["parts"] for x in p.get("inventions", [])]:
            uses.setdefault(i, [])
            if res["id"] not in uses[i]:
                uses[i].append(res["id"])

    # ---- the register, json ----------------------------------------------------------------------
    path = os.path.join(HERE, "inventions register.json")
    R = json.load(open(path, encoding="utf-8"), object_pairs_hook=OrderedDict)
    R["about"]["note"] = ("Every entry is a choice the text leaves open. Nothing here is the text's own content. I01-I76 were made by the formal core and the claims; "
                          "I77-I102 were forced by the program model/ that searched the claims on finite models (S104 round 2). Each entry lists the results of that search which depend on it (search results.md).")
    for e in R["inventions"]:
        e["source"] = "formal core and claims"
        e["results"] = inv_res.get(e["id"], [])
    for i in INVENTIONS_MODEL:
        R["inventions"].append(OrderedDict([
            ("id", i["id"]), ("title", i["title"]),
            ("fills_in_for", [OrderedDict([("line", l), ("quote", q)]) for l, q in i["quotes"]]),
            ("invented", i["invented"]), ("other_choices", i["others"]), ("formal_core_sections", []),
            ("source", "the program model/ (S104 round 2 search)"), ("code", i["code"]),
            ("claims", sorted(uses.get(i["id"], []), key=lambda s: int(s[2:]))), ("results", inv_res.get(i["id"], [])),
        ]))
    json.dump(R, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    # ---- the register, markdown (rewritten in the builder's format, with results) -----------------
    mpath = os.path.join(HERE, "inventions register.md")
    old = open(mpath, encoding="utf-8").read()
    old = old.replace("**Results.** None yet. This register is written before any test or program is run. Every result later reported on a claim depends on the inventions that claim lists, and says so.",
                      "**Results.** The claims were then searched for counterexamples on finite models by the program `model/` (`search results.md`). That program needed further choices the formal core leaves open; they are I77–I102 below, each tagged in the code where it is used. Each entry now lists the results of the search that depend on it: the claims whose results rest on it and, for a claim with a counterexample, the parts whose counterexample rests on it.")
    old = re.sub(r"\*\*Counts\.\*\* (\d+) inventions;", lambda m: "**Counts.** %d inventions (I01–I76 from the formal core and the claims, I77–I102 from the program);" % (int(m.group(1)) + len(INVENTIONS_MODEL)), old)
    # results per entry
    def repl(m):
        return m.group(0)
    blocks = old.split("\n### ")
    head, entries = blocks[0], blocks[1:]
    new_entries = []
    for b in entries:
        iid = b.split(" ", 1)[0]
        b = b.replace("**Results that depend on it.** None yet.", "**Results that depend on it.** %s." % fmt_results(inv_res.get(iid, [])))
        new_entries.append(b)
    # index rows for the new entries
    idx_rows = []
    for i in INVENTIONS_MODEL:
        lines = ", ".join("L%d" % l for l in OrderedDict((l, 1) for l, _ in i["quotes"]))
        idx_rows.append("| %s | %s | %s | %s |" % (i["id"], i["title"], lines, ", ".join(sorted(uses.get(i["id"], []), key=lambda s: int(s[2:]))) or "—"))
    head = head.replace("\n\n## The entries", "\n" + "\n".join(idx_rows) + "\n\n## The entries")
    L = [head.rstrip("\n")]
    for b in new_entries:
        L.append("### " + b.rstrip("\n"))
    L.append("")
    L.append("## Inventions forced by the program (I77–I102)")
    L.append("")
    L.append("These choices were made by the program `model/` that searched the formal claims on finite models (S104 round 2). None is marked in `formal core.md`, which the program does not change; each is tagged in the code, at the place named under 'Used by'. As with I01–I76, nothing here is the text's own content.")
    for i in INVENTIONS_MODEL:
        L.append("")
        L.append("### %s · %s" % (i["id"], i["title"]))
        L.append("")
        L.append("**The sentence it fills in for.**")
        L.append("")
        for l, q in i["quotes"]:
            L.append(q_md(l, q))
            L.append("")
        L.append("**What was invented.** %s" % i["invented"])
        L.append("")
        L.append("**Other choices that were possible.**")
        L.append("")
        for o in i["others"]:
            L.append("- %s" % o)
        L.append("")
        L.append("**Used by.** Code: %s. Claims: %s." % ("; ".join(i["code"]), ", ".join(sorted(uses.get(i["id"], []), key=lambda s: int(s[2:]))) or "none"))
        L.append("")
        L.append("**Results that depend on it.** %s." % fmt_results(inv_res.get(i["id"], [])))
    open(mpath, "w", encoding="utf-8").write("\n".join(L) + "\n")

    # ---- the formal claims: each claim's result --------------------------------------------------
    cpath = os.path.join(HERE, "formal claims.json")
    CJ = json.load(open(cpath, encoding="utf-8"), object_pairs_hook=OrderedDict)
    byid = OrderedDict((x["id"], x) for x in SR["results"])
    CJ["about"]["note"] = ("Each claim was searched for counterexamples on finite models by model/ (S104 round 2); its result is under 'results' and in search results.md. "
                           "'look' is a first reading of where a counterexample might lie, written before the search. Every claim that uses an invention lists it; a result on that claim depends on it.")
    for c in CJ["claims"]:
        x = byid.get(c["id"])
        if x:
            c["results"] = [OrderedDict([("status", x["status"]),
                                         ("parts", [OrderedDict([("label", p["label"]), ("kind", p["kind"]), ("status", p["status"])]) for p in x["parts"]]),
                                         ("rests_on", x["rests_on"]), ("reproduce", x["reproduce"])])]
    json.dump(CJ, open(cpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    mp = os.path.join(HERE, "formal claims.md")
    M = open(mp, encoding="utf-8").read()
    M = M.replace("No claim is tested here.", "Each claim's search result is added under it, from `search results.md`.")
    lines = M.split("\n")
    out = []
    cur = None
    for k, line in enumerate(lines):
        m = re.match(r"^### (FC\d+) · ", line)
        nxt_is_heading = line.startswith("## ") or line.startswith("### ")
        if nxt_is_heading and cur:
            x = byid.get(cur)
            if x:
                pc = OrderedDict()
                for p in x["parts"]:
                    pc[p["status"]] = pc.get(p["status"], 0) + 1
                while out and out[-1] == "":
                    out.pop()
                out.append("")
                out.append("**Search result (S104).** %s (%s). Rests on: %s. See `search results.md`; reproduce: `%s`." % (
                    x["status"], "; ".join("%d %s" % (v, s) for s, v in pc.items()), ", ".join(x["rests_on"]) or "no invention", x["reproduce"]))
                out.append("")
            cur = None
        if m:
            cur = m.group(1)
        out.append(line)
    open(mp, "w", encoding="utf-8").write("\n".join(out))
    tot, bad = 0, []
    for name in ("inventions register.md", "formal claims.md", "search results.md"):
        n, b = check_markdown(os.path.join(HERE, name))
        tot += n
        bad += b
    print("register: %d inventions; quotations checked in the three files: %d, not found: %d" % (len(R["inventions"]), tot, len(bad)))
    for b in bad:
        print("  BAD", b)


if __name__ == "__main__":
    main()
