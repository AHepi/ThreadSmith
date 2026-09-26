#!/usr/bin/env python3
"""S98 line-up builder: the edits and recommendations lined up by part of the semantics.

Specification: ../group/grouping and structure, chosen.md (log S98, decision S30).
Python 3 standard library only. Deterministic: no timestamps, every sort has an explicit key.
Run from the line-up folder:
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/build.py
Reads only the five inputs named in INPUTS (under ../group/); writes only under line-up/.
Commits nothing.
"""
import csv
import hashlib
import io
import json
import os
import posixpath
import re
import sys
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
LINEUP = os.path.dirname(HERE)
LEDGER = os.path.dirname(LINEUP)
GROUPDIR = os.path.join(LEDGER, "group")

INPUTS = [
    ("anchored.jsonl", "9e14f5feb3f5e167af5f5c3f98631689"),
    ("sentence index of the latest text.jsonl", "fdaf069a0c1d71be4e17b38d2f6bce82"),
    ("proposal by place - scripts/sections.json", "432425d1a7449f78f268aa360e27a394"),
    ("proposal by place - scripts/assignment.jsonl", "a7277976d506cb5407f5a998ad29b693"),
    ("proposal by idea - assignment.jsonl", "d0d233264bf2cc2d3793233b8e167258"),
]

# ---------------------------------------------------------------- groups (spec section 3)
# The group names are the theory's own Part titles (data, not the builder's words).
GROUPS = [
    ("G01", "The document as a whole", "01 The document as a whole.md", None),
    ("G02", "Organizations and their changes", "02 Organizations and their changes (Part II).md", "II"),
    ("G03", "Questions", "03 Questions (Part III).md", "III"),
    ("G04", "Layers, transports, and provenance", "04 Layers, transports, and provenance (Part IV).md", "IV"),
    ("G05", "Account", "05 Account (Part V).md", "V"),
    ("G06", "Work, routes, and interference", "06 Work, routes, and interference (Part VI).md", "VI"),
    ("G07", "Exact constructions", "07 Exact constructions (Part VII).md", "VII"),
    ("G08", "Transport results", "08 Transport results (Part VIII).md", "VIII"),
    ("G09", "Criticism, use, and usable arguments", "09 Criticism, use, and usable arguments (Part IX).md", "IX"),
    ("G10", "Understanding, construction, and origin", "10 Understanding, construction, and origin (Part X).md", "X"),
    ("G11", "Repair, created explanation, and appraisal", "11 Repair, created explanation, and appraisal (Part XI).md", "XI"),
    ("G12", "The physical module", "12 The physical module (Part XII).md", "XII"),
    ("G13", "Recursion and universality", "13 Recursion and universality (Part XIII).md", "XIII"),
    ("G14", "The class collected", "14 The class collected (Part XIV).md", "XIV"),
    ("G15", "What would rule this class out", "15 What would rule this class out (Part XV).md", "XV"),
    ("G16", "Vocabulary across the text", "16 Vocabulary across the text.md", None),
]
GROUP_IDS = [g[0] for g in GROUPS]
GROUP_NAME = {g[0]: g[1] for g in GROUPS}
GROUP_FILE = {g[0]: "groups/" + g[2] for g in GROUPS}
GROUP_HOME = {g[0]: g[3] for g in GROUPS}
PART_GROUP = {g[3]: g[0] for g in GROUPS if g[3]}

PART_KEYS = ["FM", "0", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
             "XI", "XII", "XIII", "XIV", "XV", "XVI", "OUT"]

# Sections of Parts FM, 0, I and XVI, keyed by (first_line, last_line): (Part key, group).
FILING = {
    (1, 2): ("FM", "G01"), (3, 3): ("FM", "G01"),
    (7, 7): ("0", "G01"), (8, 8): ("0", "G09"), (9, 17): ("0", "G01"), (19, 27): ("0", "G01"),
    (29, 31): ("0", "G14"), (33, 35): ("0", "G01"), (37, 37): ("0", "G02"), (39, 39): ("0", "G02"),
    (41, 41): ("0", "G04"), (43, 43): ("0", "G03"), (45, 45): ("0", "G04"), (47, 47): ("0", "G04"),
    (49, 49): ("0", "G07"), (51, 51): ("0", "G11"), (53, 53): ("0", "G04"), (55, 55): ("0", "G03"),
    (57, 57): ("0", "G02"), (59, 61): ("0", "G15"),
    (65, 65): ("I", "G01"), (67, 67): ("I", "G05"), (69, 69): ("I", "G05"), (71, 71): ("I", "G09"),
    (73, 73): ("I", "G13"), (75, 75): ("I", "G12"), (77, 77): ("I", "G04"),
    (550, 550): ("XVI", "G01"), (552, 558): ("XVI", "G02"), (560, 568): ("XVI", "G05"),
    (570, 576): ("XVI", "G04"), (578, 584): ("XVI", "G04"), (586, 592): ("XVI", "G10"),
    (594, 600): ("XVI", "G14"), (602, 608): ("XVI", "G03"), (610, 612): ("XVI", "G08"),
    (614, 616): ("XVI", "G05"), (618, 632): ("XVI", "G10"),
}

# ---------------------------------------------------------------- order (spec section 5)
ROUND_ORDER = [
    "file 10 (before log 25)", "file 20 (before log 25)", "R2 (log 25)", "round 4 (log 28)", "round 5 and Stage C (logs 29, 30)",
    "Stage B (logs 41, 55)", "S62 (log S63)", "S64 (log S65)", "S65 (log S70)", "S70 (log S71)",
    "S72 (log S75)", "S75", "S76", "S77", "S81", "S88", "S89", "S90", "S91", "S93", "S94", "S95", "S96", "S97",
]
TV_ORDER = ["f00", "f10", "f11", "f12", "d2", "d3", "d4", "d5", "note", "scrubbed", "stage1", "repaired"]

IDEA_ORDER = ["frame", "organization", "question", "layers", "provenance", "surprise", "account", "work",
              "rivals", "ruling", "constructions", "argument", "criticism", "creativity", "appraisal",
              "physical", "recursion", "inputs", "ruleout", "form"]

STATUS_ORDER = ["applied", "not applied", "declined", "superseded", "open for the owner", "unknown"]
VOCAB_SCOPES = ("term", "whole text")
CL_POINTER = "tests/Revision 2 - change list, draft of 23 September.md#"
CL_ENTRY_RE = re.compile(r"change list draft 5, entry (W[^ ]+) ")

CSV_COLUMNS = [
    "group", "group_name", "section_id", "part", "section_name", "unit_id", "unit_line", "unit_kind",
    "display", "change_id", "rid", "lineup_order", "round", "kind", "status", "new_in_latest",
    "latest_status", "applied_in", "scope", "target_text", "target_line", "old", "new", "old_sentence",
    "new_sentence", "source_file", "source_ref", "idea", "form_only",
]

# ---------------------------------------------------------------- the builder's own words (spec section 10)
# Every fixed string of the views is here; scripts/check.py scans these values.
TEXT = {
    "part_label": "Part {key}",
    "part_label_FM": "Front matter",
    "part_label_OUT": "Notes outside the Parts",
    "record_1": "1 record",
    "record_n": "{n} records",
    "change_1": "1 change",
    "change_n": "{n} changes",
    "no_change": "no change recorded",
    "line_1": "line {a}",
    "line_n": "lines {a}–{b}",
    "stands": "wording stands",
    "not_stands": "wording not in the latest text",
    "written_against": "written against: {t}",
    "target_line": ", line {n}",
    "carried_by": "carried by: {a}",
    "source": "source: {f} — {r}",
    "nearest": "nearest latest-text sentence (a lead, not a place): [{u}]({link})",
    "linked": "linked (not joined): {ids}",
    "joined_entry": "joined through the change-list entry: {ids}",
    "shown_under": "shown in full under [{u}]({link})",
    "same_wording": "Records {ids} (same wording):",
    "before": "Before:",
    "after": "After:",
    "old_wording": "Old wording:",
    "new_wording": "New wording:",
    "addition": "*(nothing: an addition)*",
    "removed": "*(nothing: removed)*",
    "vocabulary": "vocabulary",
    "form_only": "form only",
    "also_at": "also at: {links}",
    "block_entry": "the entry not in the latest text",
    "g16_entry": "its entry in 16 Vocabulary across the text",
    "filed_from": "filed here from {part}",
    "block_heading": "##### Not in the latest text, placed with this section",
    "rest_heading": "## Not in the latest text, with no section: {part}",
    "rest_short": "Not in the latest text, with no section",
    "placed_by": "placed by: {how}",
    "home_part": "Home Part: {part}",
    "no_home_part": "No home Part",
    "head_counts": ("*{home}. Units shown: {units}; units touched: {touched}; changes placed here: {changes}; "
                    "records shown here in full under their home sentence: {full}; pointer lines: {ptr}; "
                    "vocabulary lines: {voc}; records in blocks: {blocks}. "
                    "Statuses of the records shown here in full: {statuses}.*"),
    "head_g16": ("*{home}. Changes placed here: {changes}; records shown here in full: {full}; pointer lines: {ptr}; "
                 "units of the latest text where its records stand: {places}. "
                 "Statuses of the records shown here in full: {statuses}.*"),
    "contents_section": "{part} · {name} · {lines} · {records}",
    "contents_rest": "Not in the latest text, with no section: {part} · {changes}, {records}",
    "section_heading": "## {part} · {name} · {lines}",
    "unit_heading": "#### {uid}{kind} · {lines} · {counts}",
    "unit_counts": "{changes}, {records}",
    "g16_heading": "## {cid} · {records} · {statuses}",
    "g16_places": "Places in the latest text ({n}):",
    "g16_none": "none",
    # index.md
    "index_title": "# S98 — The line-up of edits and recommendations, by part of the semantics",
    "index_note": ("*Log S98, 26 September 2026, under decision S30 and the specification "
                   "`../group/grouping and structure, chosen.md`. Inputs, all in `../group/`: {inputs}. "
                   "Made by program (`scripts/build.py`, checked by `scripts/check.py`).*"),
    "index_how_title": "## How it is lined up",
    "index_how": [
        "- The thing lined up is the unit of the latest text (`tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md`): {units} units, each a sentence, a heading, a displayed formula or a list item.",
        "- The units fall into {sections} sections, and the sections into sixteen groups: fifteen named by the theory's own Part titles (G02 to G15 for Parts II to XV, G01 for the document as a whole), and G16 for vocabulary changes that run across the text.",
        "- A section of Part 0, Part I or Part XVI that treats the matter of another Part is filed with that Part's group; it stays whole and keeps its own Part label.",
        "- Each group file shows its sections, each section all its units in text order, and under each unit every record that touches it, oldest first, with the records of one change kept together as one entry.",
        "- A record on several sentences is shown in full once, under its home sentence, with a pointer line at each other sentence; a vocabulary record is shown in full under every sentence it touches.",
        "- A record with no sentence in the latest text stands in a block at the end of its section, or at the end of its group under its Part.",
        "- Only the wording is shown, never the grounds given for a change; the source file and source reference on each record line are the one pointer to them.",
    ],
    "index_read_title": "## How to read an entry",
    "index_read": [
        "- **Entry header:** the change id (`CH-…`, one change seen in one or more sources), the number of its records shown there, their statuses, and the marks *vocabulary* (a record of the change has scope `term` or `whole text`), *form only* (the idea proposal files the change under punctuation, emphasis, pointers and labels) and *also at* (the other units where records of the change are shown, its entry not in the latest text, or its entry in G16).",
        "- **Record line:** record id · round · kind (`edit`: a change made to a theory text; `recommendation`: a proposed change) · status · whether the wording stands · written against (the text and line the change is written against) · carried by (the text that carries it) · source file — source reference.",
        "- **Wording:** *Before* is the old sentence (or the old wording when no sentence is given), *After* the new sentence (or the new wording). *Old wording* and *New wording* are added when a span differs from its sentence. All wording is verbatim, LaTeX included.",
        "- **Displays:** *in full* (under the record's home sentence); *pointer line* (at each other sentence the record touches, with a link to where it is in full); *vocabulary line* (a vocabulary record, in full under every sentence it touches); *block* (a record with no sentence in the latest text: removed, never applied or not locatable).",
        "- **Statuses:** applied, not applied, declined, superseded, open for the owner, unknown, as the collectors recorded them.",
        "- **Wording stands** means the record's new wording is in the latest text; **wording not in the latest text** means it is not; nothing is shown where the question does not arise.",
        "- **Same wording:** records of one change whose four wording fields are byte for byte the same are listed together, and the wording is shown once.",
        "- **Nearest latest-text sentence (a lead, not a place):** for a record with no sentence, the sentence sharing most content words with it; it is a lead for the reader, not where the record is filed.",
    ],
    "index_groups_title": "## The groups",
    "index_groups_head": ["group", "Parts drawn from", "units (touched / all)", "changes placed here",
                          "records shown here in full", "pointer lines", "vocabulary lines", "records in blocks",
                          "applied", "not applied", "declined", "superseded", "open for the owner", "unknown"],
    "index_groups_note": "In G16 the records shown in full are its vocabulary records and its records with no sentence; its units are those of G01 to G15.",
    "index_order_title": "## The text in order",
    "index_order_note": "Every section of the latest text, in text order, with the group file that shows it.",
    "index_order_head": ["Part", "section", "lines", "group", "units (touched / all)", "records shown"],
    "index_missing_title": "## What is not here",
    "index_missing": [
        "- **Whole texts made outside the chain of revisions.** File 10 was made as a new text from its predecessor, file 00; file 12 rewrote file 11 in terms of causality, as a separate text. Each has one record for the whole text, shown in G16; their sentences are not lined up one by one.",
        "- **Sources the repository never held, or holds only in part.** The file of R2's amendments (every sentence the returns quote from it is held); rows 1 to 32 of the Stage B table; file 20, the text R2 was written against (only its quoted passages); the S76 patch (a description only); and the change list's working files of 23 September, among them its entries as first drafted, before the two checks (only the table of what the checks changed survives, and its rows are held).",
        "- **Left out on purpose.** Two of the change list's fixes before draft 1, W37.1 and W58(ii).1, change only the expected ruling and no wording, so they have no record.",
        "- **Corrections after the two checks.** `../build/fixes after the checks.md` lists what was corrected and added after the two checks of the ledger (both in `../build/`), and what was left as it was.",
    ],
    "index_open_title": "## Records open for the owner",
    "index_open_note": "The {n} records whose status is `open for the owner`.",
    "index_open_head": ["record", "change", "round", "group", "shown in full at"],
    "index_files_title": "## Files and rerun",
    "index_files": [
        "- `groups/01 … 16 *.md`: one file per group.",
        "- `by idea.md`: the idea proposal's twenty ideas as a cross-index, with links to where each change is shown.",
        "- `data/records.jsonl`: the {records} records, each once, every field of `anchored.jsonl` first, then the `lineup_…` fields.",
        "- `data/tree.json`: groups, sections, units and entries, by reference.",
        "- `data/by sentence.csv`: one row per showing of a record, in the order of the views.",
        "- `scripts/build.py`, `scripts/check.py`: the builder and its checks.",
        "- Rerun from this folder: `PYTHONDONTWRITEBYTECODE=1 python3 scripts/build.py && PYTHONDONTWRITEBYTECODE=1 python3 scripts/check.py`.",
    ],
    "shown_block": "block entry",
    "shown_g16": "G16 entry",
    # by idea.md
    "idea_title": "# S98 — The line-up by idea: a cross-index",
    "idea_note": ("*Log S98. The idea proposal's twenty ideas (`../group/proposal by idea - assignment.jsonl`), "
                  "each with the changes it names and links to where they are shown in the group files. "
                  "Made by program.*"),
    "idea_heading": "## {n}. {name} (`{key}`)",
    "idea_count": "{changes}, {records}.",
    "idea_head": ["change", "shown in", "first place", "records", "statuses", "also"],
    "idea_also": "Also carrying this idea: {ids}",
    "idea_also_none": "Also carrying this idea: none.",
    "idea_contents": "- [{n}. {name}](#{anchor}) · {changes}",
}


# ---------------------------------------------------------------- helpers
def md5_file(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def die(msg):
    sys.stderr.write("build.py: " + msg + "\n")
    sys.exit(1)


def part_label(key):
    if key == "FM":
        return TEXT["part_label_FM"]
    if key == "OUT":
        return TEXT["part_label_OUT"]
    return TEXT["part_label"].format(key=key)


def n_records(n):
    return TEXT["record_1"] if n == 1 else TEXT["record_n"].format(n=n)


def n_changes(n):
    return TEXT["change_1"] if n == 1 else TEXT["change_n"].format(n=n)


def lines_label(a, b):
    return TEXT["line_1"].format(a=a) if a == b else TEXT["line_n"].format(a=a, b=b)


def anchor_of_unit(uid):
    return uid.replace(".", "-")


def link(from_file, to_file, anchor=None):
    """Relative, percent-encoded link from one output file to another (paths relative to line-up/)."""
    if to_file == from_file:
        target = ""
    else:
        rel = posixpath.relpath(to_file, posixpath.dirname(from_file) or ".")
        target = urllib.parse.quote(rel, safe="/")
    if anchor:
        target += "#" + anchor
    return target


def blockquote(text, indent):
    out = []
    for line in text.split("\n"):
        out.append(indent + ("> " + line if line != "" else ">"))
    return out


def distinct(seq):
    seen = []
    for x in seq:
        if x not in seen:
            seen.append(x)
    return seen


def status_counts(recs):
    c = {s: 0 for s in STATUS_ORDER}
    for r in recs:
        if r["status"] not in c:
            die("unknown status " + r["status"])
        c[r["status"]] += 1
    return c


def status_line(recs):
    c = status_counts(recs)
    return ", ".join("{} {}".format(s, c[s]) for s in STATUS_ORDER)


# ---------------------------------------------------------------- load
def load():
    got = {}
    for name, md5 in INPUTS:
        p = os.path.join(GROUPDIR, name)
        m = md5_file(p)
        if m != md5:
            die("md5 of {} is {}, expected {}".format(name, m, md5))
        got[name] = p
    with open(got["anchored.jsonl"], encoding="utf-8") as f:
        raw_lines = f.read().split("\n")
    if raw_lines[-1] != "":
        die("anchored.jsonl does not end with a newline")
    raw_lines = raw_lines[:-1]
    records = [json.loads(l) for l in raw_lines]
    with open(got["sentence index of the latest text.jsonl"], encoding="utf-8") as f:
        units = [json.loads(l) for l in f if l.strip()]
    with open(got["proposal by place - scripts/sections.json"], encoding="utf-8") as f:
        sections = json.load(f)
    with open(got["proposal by place - scripts/assignment.jsonl"], encoding="utf-8") as f:
        place = [json.loads(l) for l in f if l.strip()]
    with open(got["proposal by idea - assignment.jsonl"], encoding="utf-8") as f:
        idea = [json.loads(l) for l in f if l.strip()]
    return records, units, sections, place, idea


# ---------------------------------------------------------------- compute
def compute(records, units, sections, place, idea):
    M = {}
    # units, text order
    units = sorted(units, key=lambda u: (u["line"], u["n"]))
    unit_by_id = {u["id"]: u for u in units}
    if len(unit_by_id) != len(units):
        die("duplicate unit ids")
    upos = {u["id"]: i for i, u in enumerate(units)}

    # sections
    secs = []
    for i, s in enumerate(sections):
        key = s["section"][0]
        if key not in PART_KEYS:
            die("unknown Part key " + repr(key))
        if key in PART_GROUP:
            g = PART_GROUP[key]
        else:
            fk = (s["first_line"], s["last_line"])
            if fk not in FILING or FILING[fk][0] != key:
                die("section not named in the filing table: {} {}".format(key, fk))
            g = FILING[fk][1]
        secs.append({
            "idx": i, "id": "sec-L{}-{}".format(s["first_line"], s["last_line"]),
            "part_key": key, "name": s["section"][1], "pair": tuple(s["section"]),
            "first_line": s["first_line"], "last_line": s["last_line"], "group": g, "units": [],
        })
    order = sorted(secs, key=lambda s: s["first_line"])
    for a, b in zip(order, order[1:]):
        if a["last_line"] >= b["first_line"]:
            die("sections overlap: {} {}".format(a["id"], b["id"]))
    sec_by_pair = {s["pair"]: s for s in secs}
    if len(sec_by_pair) != len(secs):
        die("duplicate section pairs")
    sec_by_id = {s["id"]: s for s in secs}
    unit_sec = {}
    for u in units:
        hits = [s for s in secs if s["first_line"] <= u["line"] <= s["last_line"]]
        if len(hits) != 1:
            die("unit {} lies in {} sections".format(u["id"], len(hits)))
        unit_sec[u["id"]] = hits[0]["id"]
        hits[0]["units"].append(u["id"])
    for s in secs:
        s["part"] = unit_by_id[s["units"][0]]["part"] if s["units"] else part_label(s["part_key"])
    unit_group = {uid: sec_by_id[sid]["group"] for uid, sid in unit_sec.items()}

    # place of each change (spec 4.1)
    pl = {}
    for p in place:
        cid = p["change_id"]
        if p["group"][0] == "ALL":
            pl[cid] = {"group": "G16", "section": None, "rest": None, "how": p["how"]}
        elif tuple(p["section"]) in sec_by_pair:
            s = sec_by_pair[tuple(p["section"])]
            pl[cid] = {"group": s["group"], "section": s["id"], "rest": None, "how": p["how"]}
        else:
            key = p["section"][0]
            if key not in PART_KEYS:
                die("unknown Part key in place entry " + repr(key))
            g = PART_GROUP.get(key, "G01")
            pl[cid] = {"group": g, "section": None, "rest": key, "how": p["how"]}
    ideas = {i["change_id"]: i for i in idea}
    for i in idea:
        if i["group"] not in IDEA_ORDER:
            die("unknown idea " + i["group"])

    # records: order (spec 5)
    rid_set = set()
    for r in records:
        if r["round"] not in ROUND_ORDER:
            die("round not named in section 5: " + repr(r["round"]))
        if r["target_version"] not in TV_ORDER:
            die("target version not named in section 5: " + repr(r["target_version"]))
        if r["change_id"] not in pl or r["change_id"] not in ideas:
            die("change without place or idea: " + r["change_id"])
        if r["rid"] in rid_set:
            die("duplicate rid " + r["rid"])
        rid_set.add(r["rid"])
        for s in r["latest_sentences"]:
            if s not in unit_by_id:
                die("unknown unit " + s)

    def okey(r):
        letter, num = r["rid"].split("-", 1)
        return (ROUND_ORDER.index(r["round"]), TV_ORDER.index(r["target_version"]), letter, int(num))

    for i, r in enumerate(sorted(records, key=okey)):
        r["_order"] = i + 1
    rec = {r["rid"]: r for r in records}
    M["cl_entry"] = {}
    for r in records:
        mo = CL_ENTRY_RE.match(r["source_ref"]) if r["rid"].startswith("C-") else None
        if mo:
            M["cl_entry"].setdefault(mo.group(1), []).append(r["rid"])
    changes = {}
    for r in records:
        changes.setdefault(r["change_id"], []).append(r["rid"])
    for cid in changes:
        changes[cid].sort(key=lambda x: rec[x]["_order"])
    change_vocab = {cid: any(rec[x]["scope"] in VOCAB_SCOPES for x in rids) for cid, rids in changes.items()}

    # showings (spec 4.2)
    at_unit = {u["id"]: {} for u in units}      # uid -> cid -> [(rid, display)]
    sec_block = {s["id"]: {} for s in secs}     # sid -> cid -> [rid]
    rest = {g: {} for g in GROUP_IDS}           # gid -> part key -> cid -> [rid]
    g16 = {}                                     # cid -> [(rid, display)]
    for r in sorted(records, key=lambda r: r["_order"]):
        cid = r["change_id"]
        p = pl[cid]
        sents = sorted(r["latest_sentences"], key=lambda x: upos[x])
        vocab = r["scope"] in VOCAB_SCOPES
        r["_pointer"] = []
        r["_term"] = []
        r["_home"] = None
        if sents and not vocab:
            home = None
            if p["section"]:
                inside = [x for x in sents if unit_sec[x] == p["section"]]
                if inside:
                    home = inside[0]
            if home is None:
                home = sents[0]
            r["_home"] = home
            r["_pointer"] = [x for x in sents if x != home]
            r["_display"] = "full"
            r["_group"] = unit_group[home]
            r["_section"] = unit_sec[home]
            for x in sents:
                at_unit[x].setdefault(cid, []).append((r["rid"], "full" if x == home else "pointer"))
            if p["group"] == "G16":
                g16.setdefault(cid, []).append((r["rid"], "pointer"))
        elif sents and vocab:
            r["_term"] = list(sents)
            r["_display"] = "term line"
            r["_group"] = p["group"]
            r["_section"] = p["section"]
            for x in sents:
                at_unit[x].setdefault(cid, []).append((r["rid"], "term line"))
            if p["group"] == "G16":
                g16.setdefault(cid, []).append((r["rid"], "full"))
        else:
            r["_group"] = p["group"]
            if p["group"] == "G16":
                r["_display"] = "vocabulary only"
                r["_section"] = None
                g16.setdefault(cid, []).append((r["rid"], "full"))
            elif p["section"]:
                r["_display"] = "block"
                r["_section"] = p["section"]
                sec_block[p["section"]].setdefault(cid, []).append(r["rid"])
            else:
                r["_display"] = "block"
                r["_section"] = "rest-" + p["rest"]
                rest[p["group"]].setdefault(p["rest"], {}).setdefault(cid, []).append(r["rid"])
        touched = set()
        for x in r["latest_sentences"]:
            touched.add(unit_group[x])
        if r["_display"] in ("block",):
            touched.add(p["group"])
        if p["group"] == "G16":
            touched.add("G16")
        r["_groups_touched"] = sorted(touched)

    # where each change is shown (for "also at" and G16 places)
    change_units = {cid: [] for cid in changes}
    for u in units:
        for cid in at_unit[u["id"]]:
            change_units[cid].append(u["id"])
    change_block = {}   # cid -> (file, anchor) of its block entry
    for s in secs:
        for cid in sec_block[s["id"]]:
            change_block[cid] = (GROUP_FILE[s["group"]], cid)
    for g in GROUP_IDS:
        for key in rest[g]:
            for cid in rest[g][key]:
                if cid in change_block:
                    die("change in two blocks " + cid)
                change_block[cid] = (GROUP_FILE[g], cid)

    M.update(units=units, unit_by_id=unit_by_id, upos=upos, secs=secs, sec_by_id=sec_by_id,
             unit_sec=unit_sec, unit_group=unit_group, pl=pl, ideas=ideas, rec=rec, records=records,
             changes=changes, change_vocab=change_vocab, at_unit=at_unit, sec_block=sec_block, rest=rest,
             g16=g16, change_units=change_units, change_block=change_block)

    # group sections in order (spec 5)
    gsecs = {g: [] for g in GROUP_IDS}
    for s in secs:
        gsecs[s["group"]].append(s)
    for g in GROUP_IDS:
        home = GROUP_HOME[g]
        gsecs[g].sort(key=lambda s: (0 if (home is None or s["part_key"] == home) else 1, s["first_line"]))
    M["gsecs"] = gsecs
    return M


def entry_order(M, cid, rids):
    return (min(M["rec"][x]["_order"] for x in rids), cid)


def sorted_entries(M, d):
    """d: cid -> list of (rid, display) or list of rid. Returns [(cid, items)] in spec order."""
    out = []
    for cid, items in d.items():
        rids = [it[0] if isinstance(it, tuple) else it for it in items]
        out.append((entry_order(M, cid, rids), cid, sorted(items, key=lambda it: M["rec"][it[0] if isinstance(it, tuple) else it]["_order"])))
    out.sort(key=lambda t: t[0])
    return [(cid, items) for _, cid, items in out]


# ---------------------------------------------------------------- rendering
class Doc:
    def __init__(self, path):
        self.path = path   # relative to line-up/
        self.lines = []

    def add(self, *ls):
        self.lines.extend(ls)

    def text(self):
        while self.lines and self.lines[-1] == "":
            self.lines.pop()
        return "\n".join(self.lines) + "\n"


def unit_link(M, from_file, uid):
    return link(from_file, GROUP_FILE[M["unit_group"][uid]], anchor_of_unit(uid))


def record_line(M, r, from_file):
    parts = ["**{}**".format(r["rid"]), r["round"], r["kind"], r["status"]]
    if r["new_in_latest"] == "yes":
        parts.append(TEXT["stands"])
    elif r["new_in_latest"] == "no":
        parts.append(TEXT["not_stands"])
    wa = TEXT["written_against"].format(t=r["target_text"])
    if r["target_line"] is not None:
        wa += TEXT["target_line"].format(n=r["target_line"])
    parts.append(wa)
    parts.append(TEXT["carried_by"].format(a=r["applied_in"]))
    parts.append(TEXT["source"].format(f=r["source_file"], r=r["source_ref"]))
    ln = r.get("latest_nearest")
    if ln:
        u = ln["sentence"]
        parts.append(TEXT["nearest"].format(u=u, link=unit_link(M, from_file, u)))
    extra = [x for x in r["same_as"] if x not in r["change_members"]]
    # a pointer to a change-list entry whose record is already in this change is joined, not merely linked
    joined, rest = [], []
    for x in extra:
        if x.startswith(CL_POINTER):
            keys = [k.strip() for k in x[len(CL_POINTER):].split("+")]
            if any(c in r["change_members"] for k in keys for c in M["cl_entry"].get(k, [])):
                joined.append(x[len(CL_POINTER):])
                continue
        rest.append(x)
    if joined:
        parts.append(TEXT["joined_entry"].format(ids=", ".join(joined)))
    if rest:
        parts.append(TEXT["linked"].format(ids=", ".join(rest)))
    return " · ".join(parts)


def pointer_line(M, r, from_file):
    parts = ["**{}**".format(r["rid"]), r["round"], r["kind"], r["status"],
             TEXT["shown_under"].format(u=r["_home"], link=unit_link(M, from_file, r["_home"]))]
    return " · ".join(parts)


def wording_blocks(r):
    """[(label, text or None-for-placeholder, placeholder)] per spec 8.1."""
    old, new, osen, nsen = r["old"], r["new"], r["old_sentence"], r["new_sentence"]
    before = osen if osen != "" else old
    after = nsen if nsen != "" else new
    out = [(TEXT["before"], before, TEXT["addition"]), (TEXT["after"], after, TEXT["removed"])]
    if osen != "" and old != "" and osen != old:
        out.append((TEXT["old_wording"], old, None))
    if nsen != "" and nsen != new:
        out.append((TEXT["new_wording"], new, TEXT["removed"]))
    return out


def render_wording(r, indent):
    out = []
    for label, text, placeholder in wording_blocks(r):
        if text == "":
            out.append("{}- {} {}".format(indent, label, placeholder))
        else:
            out.append("{}- {}".format(indent, label))
            out.extend(blockquote(text, indent + "  "))
    return out


def wkey(r):
    return (r["old"], r["new"], r["old_sentence"], r["new_sentence"])


def render_records(M, items, indent, from_file):
    """items: list of (rid, display) with display in full / term line / pointer / block.
    Returns (lines, flat order of (rid, display))."""
    rec = M["rec"]
    buckets = {}
    border = []
    units_ = []
    for rid, disp in items:
        r = rec[rid]
        if disp == "pointer":
            units_.append((r["_order"], ("p", rid)))
        else:
            k = wkey(r)
            if k not in buckets:
                buckets[k] = []
                border.append(k)
            buckets[k].append(rid)
    for k in border:
        rids = sorted(buckets[k], key=lambda x: rec[x]["_order"])
        buckets[k] = rids
        units_.append((rec[rids[0]]["_order"], ("b", k)))
    units_.sort(key=lambda t: t[0])
    lines = []
    flat = []
    disp_of = {rid: d for rid, d in items}
    for _, (t, v) in units_:
        if t == "p":
            r = rec[v]
            lines.append(indent + "- " + pointer_line(M, r, from_file))
            flat.append((v, "pointer"))
        else:
            rids = buckets[v]
            if len(rids) == 1:
                r = rec[rids[0]]
                lines.append(indent + "- " + record_line(M, r, from_file))
                lines.extend(render_wording(r, indent + "  "))
            else:
                lines.append(indent + "- " + TEXT["same_wording"].format(ids=", ".join(rids)))
                for x in rids:
                    lines.append(indent + "  - " + record_line(M, rec[x], from_file))
                lines.extend(render_wording(rec[rids[0]], indent + "  "))
            for x in rids:
                flat.append((x, disp_of[x]))
    return lines, flat


def statuses_of(M, rids):
    return ", ".join(distinct(M["rec"][x]["status"] for x in sorted(rids, key=lambda x: M["rec"][x]["_order"])))


def also_links(M, cid, here_uid, from_file):
    if M["pl"][cid]["group"] == "G16":
        return [ "[{}]({})".format(TEXT["g16_entry"], link(from_file, GROUP_FILE["G16"], cid)) ]
    out = []
    for uid in M["change_units"][cid]:
        if uid != here_uid:
            out.append("[{}]({})".format(uid, unit_link(M, from_file, uid)))
    if here_uid is not None and cid in M["change_block"]:
        f, a = M["change_block"][cid]
        out.append("[{}]({})".format(TEXT["block_entry"], link(from_file, f, a)))
    return out


def entry_header(M, cid, rids, here_uid, from_file):
    parts = ["**{}**".format(cid), n_records(len(rids)), statuses_of(M, rids)]
    if M["change_vocab"][cid]:
        parts.append(TEXT["vocabulary"])
    if M["ideas"][cid]["group"] == "form":
        parts.append(TEXT["form_only"])
    al = also_links(M, cid, here_uid, from_file)
    if al:
        parts.append(TEXT["also_at"].format(links=", ".join(al)))
    return " · ".join(parts)


def block_header(M, cid, rids, from_file):
    ls = distinct(M["rec"][x]["latest_status"] for x in rids)
    parts = ['<a id="{}"></a>**{}**'.format(cid, cid), n_records(len(rids)), ", ".join(ls),
             TEXT["placed_by"].format(how=M["pl"][cid]["how"])]
    if M["ideas"][cid]["group"] == "form":
        parts.append(TEXT["form_only"])
    al = also_links(M, cid, None, from_file)
    if al:
        parts.append(TEXT["also_at"].format(links=", ".join(al)))
    return " · ".join(parts)


def build_group_file(M, g, rows, stats):
    path = GROUP_FILE[g]
    doc = Doc(path)
    rec = M["rec"]
    secs = M["gsecs"][g]
    num = g[1:]
    # counts
    units_all = [uid for s in secs for uid in s["units"]]
    touched = [uid for uid in units_all if M["at_unit"][uid]]
    full = [rec[rid] for uid in units_all for cid, its in M["at_unit"][uid].items() for rid, d in its if d == "full"]
    ptr = sum(1 for uid in units_all for cid, its in M["at_unit"][uid].items() for rid, d in its if d == "pointer")
    voc = sum(1 for uid in units_all for cid, its in M["at_unit"][uid].items() for rid, d in its if d == "term line")
    blocks = sum(len(v) for s in secs for v in M["sec_block"][s["id"]].values())
    blocks += sum(len(v) for key in M["rest"][g] for v in M["rest"][g][key].values())
    nchanges = sum(1 for cid in M["changes"] if M["pl"][cid]["group"] == g)
    home = GROUP_HOME[g]
    stats[g] = {"units": len(units_all), "touched": len(touched), "changes": nchanges, "full": len(full),
                "ptr": ptr, "voc": voc, "blocks": blocks, "full_recs": full,
                "parts": distinct(s["part_key"] for s in secs)}
    doc.add("# {} {}".format(num, GROUP_NAME[g]), "")
    doc.add(TEXT["head_counts"].format(
        home=TEXT["home_part"].format(part=part_label(home)) if home else TEXT["no_home_part"],
        units=len(units_all), touched=len(touched), changes=nchanges, full=len(full), ptr=ptr, voc=voc,
        blocks=blocks, statuses=status_line(full)), "")
    # contents
    for s in secs:
        rids = set()
        for uid in s["units"]:
            for cid, its in M["at_unit"][uid].items():
                rids.update(x for x, _ in its)
        for cid, xs in M["sec_block"][s["id"]].items():
            rids.update(xs)
        s["_nrecords"] = len(rids)
        s["_touched"] = sum(1 for uid in s["units"] if M["at_unit"][uid])
        doc.add("- [{}]({})".format(TEXT["contents_section"].format(
            part=part_label(s["part_key"]), name=s["name"], lines=lines_label(s["first_line"], s["last_line"]),
            records=n_records(len(rids))), link(path, path, s["id"])))
    rest_keys = [k for k in PART_KEYS if k in M["rest"][g] and M["rest"][g][k]]
    for k in rest_keys:
        nrec = sum(len(v) for v in M["rest"][g][k].values())
        doc.add("- [{}]({})".format(TEXT["contents_rest"].format(
            part=part_label(k), changes=n_changes(len(M["rest"][g][k])), records=n_records(nrec)),
            link(path, path, "rest-" + k)))
    doc.add("")
    tree_secs = []
    for s in secs:
        filed = "yes" if (home is not None and s["part_key"] != home) else "no"
        doc.add('<a id="{}"></a>'.format(s["id"]))
        head = TEXT["section_heading"].format(part=s["part"], name=s["name"],
                                              lines=lines_label(s["first_line"], s["last_line"]))
        if filed == "yes":
            head += " · " + TEXT["filed_from"].format(part=part_label(s["part_key"]))
        doc.add(head, "")
        tunits = []
        for uid in s["units"]:
            u = M["unit_by_id"][uid]
            ents = sorted_entries(M, M["at_unit"][uid])
            nrec = sum(len(its) for _, its in ents)
            counts = TEXT["unit_counts"].format(changes=n_changes(len(ents)), records=n_records(nrec)) if ents else TEXT["no_change"]
            kind = "" if u["kind"] == "sentence" else " · " + u["kind"]
            doc.add('<a id="{}"></a>'.format(anchor_of_unit(uid)))
            doc.add(TEXT["unit_heading"].format(uid=uid, kind=kind, lines=lines_label(u["line"], u["line_end"]), counts=counts))
            doc.add(*blockquote(u["text"], ""))
            doc.add("")
            tents = []
            for cid, its in ents:
                rids = [x for x, _ in its]
                doc.add("- " + entry_header(M, cid, rids, uid, path))
                lines, flat = render_records(M, its, "  ", path)
                doc.add(*lines)
                tents.append({"change_id": cid, "records": [{"rid": x, "display": d} for x, d in flat]})
                for x, d in flat:
                    rows.append(csv_row(M, g, s, u, d, rec[x]))
            if ents:
                doc.add("")
            tunits.append({"id": uid, "kind": u["kind"], "line": u["line"], "line_end": u["line_end"],
                           "text": u["text"], "entries": tents})
        bents = sorted_entries(M, M["sec_block"][s["id"]])
        tblock = []
        if bents:
            doc.add(TEXT["block_heading"], "")
            for cid, rids in bents:
                doc.add("- " + block_header(M, cid, rids, path))
                lines, flat = render_records(M, [(x, "block") for x in rids], "  ", path)
                doc.add(*lines)
                tblock.append({"change_id": cid, "placed_by": M["pl"][cid]["how"], "records": [x for x, _ in flat]})
                for x, d in flat:
                    rows.append(csv_row(M, g, s, None, "block", rec[x]))
            doc.add("")
        tree_secs.append({"id": s["id"], "part_key": s["part_key"], "part": s["part"], "name": s["name"],
                          "first_line": s["first_line"], "last_line": s["last_line"],
                          "filed_from_other_part": filed, "units": tunits, "block": tblock})
    trest = []
    for k in rest_keys:
        doc.add('<a id="rest-{}"></a>'.format(k))
        doc.add(TEXT["rest_heading"].format(part=part_label(k)), "")
        tch = []
        for cid, rids in sorted_entries(M, M["rest"][g][k]):
            doc.add("- " + block_header(M, cid, rids, path))
            lines, flat = render_records(M, [(x, "block") for x in rids], "  ", path)
            doc.add(*lines)
            tch.append({"change_id": cid, "placed_by": M["pl"][cid]["how"], "records": [x for x, _ in flat]})
            for x, d in flat:
                rows.append(csv_row(M, g, None, None, "block", rec[x], rest_key=k))
        doc.add("")
        trest.append({"part_key": k, "changes": tch})
    tree = {"id": g, "name": GROUP_NAME[g], "file": GROUP_FILE[g], "home_part": home,
            "sections": tree_secs, "rest": trest}
    return doc, tree


def build_g16(M, rows, stats):
    g = "G16"
    path = GROUP_FILE[g]
    doc = Doc(path)
    rec = M["rec"]
    ents = sorted_entries(M, M["g16"])
    full = [rec[x] for cid, its in ents for x, d in its if d == "full"]
    ptr = sum(1 for cid, its in ents for x, d in its if d == "pointer")
    places_all = set()
    for cid, _ in ents:
        places_all.update(M["change_units"][cid])
    stats[g] = {"units": 0, "touched": 0, "changes": len(ents), "full": len(full), "ptr": ptr, "voc": 0,
                "blocks": 0, "full_recs": full, "parts": [], "places": len(places_all)}
    doc.add("# 16 {}".format(GROUP_NAME[g]), "")
    doc.add(TEXT["head_g16"].format(home=TEXT["no_home_part"], changes=len(ents), full=len(full), ptr=ptr,
                                    places=len(places_all), statuses=status_line(full)), "")
    tch = []
    for cid, its in ents:
        rids = [x for x, _ in its]
        doc.add('<a id="{}"></a>'.format(cid))
        doc.add(TEXT["g16_heading"].format(cid=cid, records=n_records(len(rids)), statuses=statuses_of(M, rids)), "")
        lines, flat = render_records(M, its, "", path)
        doc.add(*lines)
        doc.add("")
        places = M["change_units"][cid]
        doc.add(TEXT["g16_places"].format(n=len(places)), "")
        if places:
            by_g = {}
            for uid in places:
                by_g.setdefault(M["unit_group"][uid], []).append(uid)
            for gg in GROUP_IDS:
                if gg in by_g:
                    doc.add("- {}: {}".format(GROUP_FILE[gg][len("groups/"):], ", ".join(
                        "[{}]({})".format(u, unit_link(M, path, u)) for u in by_g[gg])))
        else:
            doc.add("- " + TEXT["g16_none"])
        doc.add("")
        tch.append({"change_id": cid, "records": [{"rid": x, "display": d} for x, d in flat], "places": places})
        for x, d in flat:
            rows.append(csv_row(M, g, None, None, d, rec[x]))
    return doc, {"id": g, "name": GROUP_NAME[g], "file": GROUP_FILE[g], "changes": tch}


def csv_row(M, g, s, u, display, r, rest_key=None):
    i = M["ideas"][r["change_id"]]
    pointer = display == "pointer"
    if s is not None:
        sid, part, sname = s["id"], s["part"], s["name"]
    elif rest_key is not None:
        sid, part, sname = "rest-" + rest_key, part_label(rest_key), TEXT["rest_short"]
    else:
        sid, part, sname = "", "", ""
    return [g, GROUP_NAME[g], sid, part, sname,
            u["id"] if u else "", u["line"] if u else "", u["kind"] if u else "",
            display, r["change_id"], r["rid"], r["_order"], r["round"], r["kind"], r["status"],
            r["new_in_latest"], r["latest_status"], r["applied_in"], r["scope"], r["target_text"],
            "" if r["target_line"] is None else r["target_line"],
            "" if pointer else r["old"], "" if pointer else r["new"],
            "" if pointer else r["old_sentence"], "" if pointer else r["new_sentence"],
            r["source_file"], r["source_ref"], i["group"], "yes" if i["group"] == "form" else "no"]


def full_place(M, r, from_file):
    """Link to where the record is shown in full (for index lists)."""
    d = r["_display"]
    if d == "full":
        return "[{}]({})".format(r["_home"], unit_link(M, from_file, r["_home"]))
    if d == "term line":
        u = r["_term"][0]
        return "[{}]({})".format(u, unit_link(M, from_file, u))
    if d == "block":
        f, a = M["change_block"][r["change_id"]]
        return "[{} {}]({})".format(TEXT["shown_block"], r["change_id"], link(from_file, f, a))
    return "[{} {}]({})".format(TEXT["shown_g16"], r["change_id"], link(from_file, GROUP_FILE["G16"], r["change_id"]))


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "| " + " | ".join("---" for _ in head) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "\\|") for c in r) + " |")
    return out


def build_index(M, stats, md5s):
    path = "index.md"
    doc = Doc(path)
    doc.add(TEXT["index_title"], "")
    doc.add(TEXT["index_note"].format(inputs="; ".join("`{}` (md5 {})".format(n, m) for n, m in md5s)), "")
    doc.add(TEXT["index_how_title"], "")
    for l in TEXT["index_how"]:
        doc.add(l.format(units=len(M["units"]), sections=len(M["secs"])))
    doc.add("")
    doc.add(TEXT["index_read_title"], "")
    doc.add(*TEXT["index_read"])
    doc.add("")
    doc.add(TEXT["index_missing_title"], "")
    doc.add(*TEXT["index_missing"])
    doc.add("")
    doc.add(TEXT["index_groups_title"], "")
    rows = []
    for g in GROUP_IDS:
        st = stats[g]
        c = status_counts(st["full_recs"])
        name = "[{} {}]({})".format(g, GROUP_NAME[g], link(path, GROUP_FILE[g]))
        if g == "G16":
            rows.append([name, "—", "—", st["changes"], st["full"], st["ptr"], "—", "—"] + [c[s] for s in STATUS_ORDER])
        else:
            rows.append([name, ", ".join(st["parts"]), "{} / {}".format(st["touched"], st["units"]), st["changes"],
                         st["full"], st["ptr"], st["voc"], st["blocks"]] + [c[s] for s in STATUS_ORDER])
    doc.add(*table(TEXT["index_groups_head"], rows))
    doc.add("", TEXT["index_groups_note"], "")
    doc.add(TEXT["index_order_title"], "", TEXT["index_order_note"], "")
    rows = []
    for s in sorted(M["secs"], key=lambda s: s["first_line"]):
        rows.append([part_label(s["part_key"]), s["name"], lines_label(s["first_line"], s["last_line"]),
                     "[{}]({})".format(s["group"], link(path, GROUP_FILE[s["group"]], s["id"])),
                     "{} / {}".format(s["_touched"], len(s["units"])), s["_nrecords"]])
    doc.add(*table(TEXT["index_order_head"], rows))
    doc.add("")
    opens = sorted([r for r in M["records"] if r["status"] == "open for the owner"], key=lambda r: r["_order"])
    doc.add(TEXT["index_open_title"], "", TEXT["index_open_note"].format(n=len(opens)), "")
    rows = [[r["rid"], r["change_id"], r["round"], r["_group"], full_place(M, r, path)] for r in opens]
    doc.add(*table(TEXT["index_open_head"], rows))
    doc.add("")
    doc.add(TEXT["index_files_title"], "")
    for l in TEXT["index_files"]:
        doc.add(l.format(records=len(M["records"])))
    return doc


def first_place(M, cid):
    """(sort key, group, file, anchor, label) of the first place a change is shown."""
    us = M["change_units"][cid]
    if us:
        u = us[0]
        return ((0, M["upos"][u]), M["unit_group"][u], GROUP_FILE[M["unit_group"][u]], anchor_of_unit(u), u)
    if cid in M["change_block"]:
        f, a = M["change_block"][cid]
        g = [x for x in GROUP_IDS if GROUP_FILE[x] == f][0]
        return ((1, 0), g, f, a, TEXT["shown_block"])
    return ((1, 0), "G16", GROUP_FILE["G16"], cid, TEXT["shown_g16"])


def change_groups(M, cid):
    gs = set()
    for x in M["changes"][cid]:
        gs.update(M["rec"][x]["_groups_touched"])
    return [g for g in GROUP_IDS if g in gs]


def build_by_idea(M):
    path = "by idea.md"
    doc = Doc(path)
    doc.add(TEXT["idea_title"], "", TEXT["idea_note"], "")
    names = {}
    by = {k: [] for k in IDEA_ORDER}
    also = {k: [] for k in IDEA_ORDER}
    for cid in sorted(M["changes"]):
        i = M["ideas"][cid]
        names[i["group"]] = i["group_name"]
        by[i["group"]].append(cid)
        for a in i["also"]:
            if a not in also:
                die("unknown idea in also: " + a)
            also[a].append(cid)

    def ckey(cid):
        fp = first_place(M, cid)
        return (GROUP_IDS.index(fp[1]), fp[0], cid)

    for n, k in enumerate(IDEA_ORDER, 1):
        nrec = sum(len(M["changes"][c]) for c in by[k])
        doc.add(TEXT["idea_contents"].format(n=n, name=names[k], anchor="idea-" + k,
                                             changes=TEXT["idea_count"].format(changes=n_changes(len(by[k])), records=n_records(nrec)).rstrip(".")))
    doc.add("")
    for n, k in enumerate(IDEA_ORDER, 1):
        doc.add('<a id="idea-{}"></a>'.format(k))
        doc.add(TEXT["idea_heading"].format(n=n, name=names[k], key=k), "")
        nrec = sum(len(M["changes"][c]) for c in by[k])
        doc.add(TEXT["idea_count"].format(changes=n_changes(len(by[k])), records=n_records(nrec)), "")
        rows = []
        for cid in sorted(by[k], key=ckey):
            fp = first_place(M, cid)
            rids = M["changes"][cid]
            rows.append(["[{}]({})".format(cid, link(path, fp[2], fp[3])),
                         ", ".join("[{}]({})".format(g, link(path, GROUP_FILE[g])) for g in change_groups(M, cid)),
                         "[{}]({})".format(fp[4], link(path, fp[2], fp[3])),
                         len(rids), statuses_of(M, rids), ", ".join(M["ideas"][cid]["also"])])
        doc.add(*table(TEXT["idea_head"], rows))
        doc.add("")
        al = sorted(also[k], key=ckey)
        if al:
            doc.add(TEXT["idea_also"].format(ids=", ".join(
                "[{}]({})".format(c, link(path, first_place(M, c)[2], first_place(M, c)[3])) for c in al)))
        else:
            doc.add(TEXT["idea_also_none"])
        doc.add("")
    return doc


def records_jsonl(M, raw_order):
    out = []
    for r in raw_order:
        i = M["ideas"][r["change_id"]]
        o = {k: v for k, v in r.items() if not k.startswith("_")}
        o["lineup_order"] = r["_order"]
        o["lineup_display"] = r["_display"]
        o["lineup_group"] = r["_group"]
        o["lineup_group_name"] = GROUP_NAME[r["_group"]]
        o["lineup_section"] = r["_section"]
        o["lineup_home_sentence"] = r["_home"]
        o["lineup_pointer_sentences"] = r["_pointer"]
        o["lineup_term_sentences"] = r["_term"]
        o["lineup_groups_touched"] = r["_groups_touched"]
        o["lineup_change_group"] = M["pl"][r["change_id"]]["group"]
        o["lineup_change_placed_by"] = M["pl"][r["change_id"]]["how"]
        o["lineup_idea"] = i["group"]
        o["lineup_idea_name"] = i["group_name"]
        o["lineup_idea_also"] = i["also"]
        o["lineup_idea_near_tie"] = i["near_tie"]
        o["lineup_form_only"] = "yes" if i["group"] == "form" else "no"
        out.append(json.dumps(o, ensure_ascii=False))
    return "\n".join(out) + "\n"


def write(rel, text):
    p = os.path.join(LINEUP, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    records, units, sections, place, idea = load()
    raw_keys = [list(r.keys()) for r in records]
    M = compute(records, units, sections, place, idea)
    # records.jsonl first: the data, saved early
    write("data/records.jsonl", records_jsonl(M, records))
    for r, ks in zip(records, raw_keys):
        if [k for k in r.keys() if not k.startswith("_")] != ks:
            die("field order changed for " + r["rid"])
    rows = []
    stats = {}
    tree_groups = []
    docs = []
    for g in GROUP_IDS[:-1]:
        doc, t = build_group_file(M, g, rows, stats)
        docs.append(doc)
        tree_groups.append(t)
    doc, t = build_g16(M, rows, stats)
    docs.append(doc)
    tree_groups.append(t)
    md5s = [(n, m) for n, m in INPUTS]
    docs.append(build_index(M, stats, md5s))
    docs.append(build_by_idea(M))
    for d in docs:
        write(d.path, d.text())
    tree = {"about": {"log": "S98", "inputs": {n: m for n, m in INPUTS}, "records": len(M["records"]),
                      "changes": len(M["changes"]), "units": len(M["units"])},
            "groups": tree_groups}
    write("data/tree.json", json.dumps(tree, ensure_ascii=False, indent=1) + "\n")
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n", quoting=csv.QUOTE_MINIMAL)
    w.writerow(CSV_COLUMNS)
    for row in rows:
        w.writerow(row)
    write("data/by sentence.csv", buf.getvalue())
    # summary on stdout
    print("records {}, changes {}, units {}, sections {}".format(len(M["records"]), len(M["changes"]),
                                                                len(M["units"]), len(M["secs"])))
    for g in GROUP_IDS:
        st = stats[g]
        print("{} units {} touched {} changes {} full {} pointer {} vocabulary {} blocks {}".format(
            g, st["units"], st["touched"], st["changes"], st["full"], st["ptr"], st["voc"], st["blocks"]))
    print("csv rows {}".format(len(rows)))


if __name__ == "__main__":
    main()
