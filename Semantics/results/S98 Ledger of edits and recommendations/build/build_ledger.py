#!/usr/bin/env python3
"""S98 ledger: one command that builds the line-up, checks it, and writes the ledger's front page.

    PYTHONDONTWRITEBYTECODE=1 python3 build/build_ledger.py      (from the ledger folder, or any folder)

1. Runs line-up/scripts/build.py: reads the inputs in group/ (anchored.jsonl, the sentence index of the
   latest text, the place proposal's sections.json and assignment.jsonl, the idea proposal's assignment) and
   writes the data files and views under line-up/, as the specification
   group/grouping and structure, chosen.md lays down.
2. Runs line-up/scripts/check.py (the eight checks of the specification, section 11).
3. Writes "00 Index.md" in the ledger folder from line-up/data/tree.json and line-up/data/records.jsonl.

Python 3 standard library only; deterministic; commits nothing.
"""
import json
import os
import subprocess
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.dirname(HERE)
LINEUP = os.path.join(LEDGER, "line-up")
SCRIPTS = os.path.join(LINEUP, "scripts")
sys.path.insert(0, SCRIPTS)
sys.dont_write_bytecode = True
import build  # noqa: E402
import check  # noqa: E402

TEXT00 = {
    "title": "# S98 — Ledger of edits and recommendations",
    "note": "*Log S98, 26 September 2026, under decision S30. Made by program (`build/build_ledger.py`), nothing committed.*",
    "what": [
        ("This ledger holds every edit made to the theory texts and every recommendation for one, from file 20 "
         "to the S97 cross-examination ({records} records of {changes} changes), each lined up under the sentence "
         "of the latest text it touches, and the sentences grouped by the part of the semantics they belong to."),
        ("It leaves out the reasons given for each change: only the sentences and wordings are copied, byte for byte, "
         "and each record's source file and source reference are the only pointer to why it was made or proposed."),
    ],
    "groups_title": "## The groups",
    "groups_head": ["group", "units (touched / all)", "changes placed here", "records shown in the group",
                    "records in full under their home sentence", "pointer lines", "vocabulary lines", "records in blocks"],
    "groups_note": ("G16 holds vocabulary changes that run across the text; its records also stand, as vocabulary lines, "
                    "under the sentences of G01 to G15 they touch. A record on sentences of several groups is counted "
                    "in each group where it is shown."),
    "where_title": "## Where things are",
    "where": [
        "- [`line-up/index.md`]({index}): how the line-up is made, how to read an entry, every section of the text in order with its group, and the {open} records open for the owner.",
        "- `line-up/groups/`: the sixteen group files; `line-up/by idea.md`: the idea proposal's twenty ideas as a cross-index.",
        "- `line-up/data/`: `records.jsonl` (every record once), `tree.json` (the structure), `by sentence.csv` (one row per showing).",
        "- `collect/`: the five collectors' records and coverage notes; `group/`: the anchoring to the latest text, the two proposals, and the chosen structure (`grouping and structure, chosen.md`).",
        "- Rerun: `PYTHONDONTWRITEBYTECODE=1 python3 build/build_ledger.py` (runs `line-up/scripts/build.py`, then `line-up/scripts/check.py`, then writes this page).",
    ],
}


def run(script):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    p = subprocess.run([sys.executable, os.path.join(SCRIPTS, script)], env=env, cwd=LINEUP,
                       stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    sys.stdout.write(p.stdout)
    if p.returncode != 0:
        sys.stderr.write("build_ledger.py: {} failed\n".format(script))
        sys.exit(1)


def main():
    run("build.py")
    run("check.py")
    with open(os.path.join(LINEUP, "data", "tree.json"), encoding="utf-8") as f:
        tree = json.load(f)
    with open(os.path.join(LINEUP, "data", "records.jsonl"), encoding="utf-8") as f:
        recs = [json.loads(l) for l in f if l.strip()]
    per_group_rids = {g: set() for g in build.GROUP_IDS}
    for r in recs:
        for g in r["lineup_groups_touched"]:
            per_group_rids[g].add(r["rid"])
    rows = []
    change_group = {r["change_id"]: r["lineup_change_group"] for r in recs}
    for g in tree["groups"]:
        gid = g["id"]
        name = "[{} {}]({})".format(gid, g["name"], urllib.parse.quote("line-up/" + g["file"], safe="/"))
        nchanges = sum(1 for cg in change_group.values() if cg == gid)
        if gid == "G16":
            rows.append([name, "—", nchanges, len(per_group_rids[gid]), "—", "—", "—", "—"])
            continue
        units = [u for s in g["sections"] for u in s["units"]]
        touched = sum(1 for u in units if u["entries"])
        full = ptr = voc = 0
        for u in units:
            for e in u["entries"]:
                for x in e["records"]:
                    if x["display"] == "full":
                        full += 1
                    elif x["display"] == "pointer":
                        ptr += 1
                    else:
                        voc += 1
        blocks = sum(len(e["records"]) for s in g["sections"] for e in s["block"])
        blocks += sum(len(e["records"]) for rb in g["rest"] for e in rb["changes"])
        rows.append([name, "{} / {}".format(touched, len(units)), nchanges, len(per_group_rids[gid]),
                     full, ptr, voc, blocks])
    lines = [TEXT00["title"], "", TEXT00["note"], ""]
    lines.append(" ".join(s.format(records=len(recs), changes=tree["about"]["changes"]) for s in TEXT00["what"]))
    lines.append("")
    lines += [TEXT00["groups_title"], ""]
    lines += build.table(TEXT00["groups_head"], rows)
    lines += ["", TEXT00["groups_note"], "", TEXT00["where_title"], ""]
    nopen = sum(1 for r in recs if r["status"] == "open for the owner")
    for w in TEXT00["where"]:
        lines.append(w.format(index=urllib.parse.quote("line-up/index.md", safe="/"), open=nopen))
    text = "\n".join(lines) + "\n"
    hits = []
    for v in TEXT00.values():
        for s in (v if isinstance(v, list) else [v]):
            hits += check.word_hits(s)
    for l in text.split("\n"):
        if not l.startswith("|"):
            hits += check.word_hits(l)
    if hits:
        sys.stderr.write("build_ledger.py: word scan found: {}\n".format(", ".join(sorted(set(hits)))))
        sys.exit(1)
    with open(os.path.join(LEDGER, "00 Index.md"), "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote 00 Index.md ({} groups, {} records, {} changes)".format(len(rows), len(recs), tree["about"]["changes"]))


if __name__ == "__main__":
    main()
