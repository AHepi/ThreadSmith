"""Independent recomputation of stage B's counts (plan W14), from the frozen texts and the raw
marks alone. Standard library only.

    /home/user/.venvs/threadsmith/bin/python recompute.py

Reads (and nothing else):
  instrument/criteria.json                     the fields, kinds, closed lists, sources
  instrument/marking-plan.md                   only to find the record files it names (the split)
  stage-B/w10/marking1/index.json              M### -> run id (first marker)
  stage-B/w10/marking1/marks/M###.json         first marker's marks
  stage-B/w10/marking1/prompts/M###.txt        only to check the criteria sent were the frozen ones
  marking/secret_mapping_record96.json         R### -> run id (second marker)
  stage-B/w10/marking2/marks/R###.json         second marker's marks
  stage-B/w10/marking2/prompts/R###.txt        as for the first marker's prompts
  stage-B/tool_audit.json                      W10.18 (reads seen in the transcripts)
  stage-B/returns.json, returns_M085_rerun.json  the markers' own list of files read (claimed;
                                               a cross-check on the audit, never a substitute)

Writes output.json and output.txt beside this file. Writes nothing else.

Every number here is a count of reports, by field, per set of 48. Nothing is summed across
fields or sets. The rule, as the texts state it:
  - pairing: each run id's first mark (index.json) with its second mark (the mapping);
  - agreement (marking plan section 5; criteria.json agreement.per_kind): enum, int and bool
    agree when equal; a set when the sets are equal; a map_enum when the whole map is equal;
    text is never compared; a report where either side has no value is unreadable, named, and
    never agreement;
  - thresholds (marking plan section 6; W14 section 2): a field is certified when its count of
    agreeing reports reaches its threshold in each set of 48 separately (p52; and rep + rep31 +
    son + son31). The pooled 96 is printed beside and is never the gate;
  - the split (W14 section 3; W13 section 2): for every field reworded twice or more, agreement
    over all 96, over the read reports and over the unread reports;
  - W10.17: closed-list values, nulls and off-list values per enum field per marker;
  - W10.18: from the audit; a struck mark is removed (its report becomes unreadable on every
    field for that marker).
Where the texts can be read two ways, both readings are computed and both are written out; the
reading chosen is marked "primary".
"""
import json
import math
import os
import re
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
RIG = os.path.abspath(os.path.join(HERE, "..", ".."))            # .../rigs/W10 harness
STAGE_B = os.path.join(RIG, "stage-B")
P = {
    "criteria": os.path.join(RIG, "instrument", "criteria.json"),
    "marking_plan": os.path.join(RIG, "instrument", "marking-plan.md"),
    "index1": os.path.join(STAGE_B, "w10", "marking1", "index.json"),
    "marks1": os.path.join(STAGE_B, "w10", "marking1", "marks"),
    "prompts1": os.path.join(STAGE_B, "w10", "marking1", "prompts"),
    "mapping2": os.path.join(RIG, "marking", "secret_mapping_record96.json"),
    "marks2": os.path.join(STAGE_B, "w10", "marking2", "marks"),
    "prompts2": os.path.join(STAGE_B, "w10", "marking2", "prompts"),
    "audit": os.path.join(STAGE_B, "tool_audit.json"),
    "returns": os.path.join(STAGE_B, "returns.json"),
    "returns_rerun": os.path.join(STAGE_B, "returns_M085_rerun.json"),
}
SKILL_DIR = "/home/user/ThreadSmith/HV Skill/authority/33/hard-to-vary/"
SKILL_FILES = ["SKILL.md"] + ["references/" + x for x in (
    "building.md", "by-domain.md", "question-bank.md", "reporting.md",
    "testing-against-cases.md", "the-idea-in-depth.md", "word-list.md")]

SETS = OrderedDict([("p52", ("p52",)), ("repeat", ("rep", "rep31", "son", "son31"))])
SET_NAMES = {"p52": "the close-marked 48 (set p52)",
             "repeat": "the repeat 48 (sets rep, rep31, son, son31)"}
COMPARABLE = ("enum", "int", "bool", "set", "map_enum")

# Marking plan section 6 table (W3 P3.1 to P3.5, and the instrument's added 39).
P31 = ("shape", "turned_own_test", "same_explanation")
P32 = ("marks_per_part", "pairs_that_pull", "rivals_built")
P33 = ("question_identity",)
P35 = ("test_swap", "test_poke")
AT39_NAMED = ("test_flip", "test_reverse", "test_hunt", "test_addjob", "test_rival", "test_pull",
              "test_patches", "test_inside", "remove_in_groups", "shape_elements",
              "modules_self_reported", "attributions")
# Fields reworded twice or more (W14 section 3; marking plan 13.5, 14.4, 15.1: no later addendum
# adds one).
TWICE_REWORDED = ("marks_per_part", "pairs_that_pull", "rivals_built")
WITHIN_STEP_IF_P35_FAILS = ("test_remove", "shape", "shape_elements", "marks_per_part",
                            "question_identity", "modules_self_reported", "attributions")


def rj(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def rt(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


# --------------------------------------------------------------------------- loading and pairing

def load():
    crit = rj(P["criteria"])
    fields = OrderedDict((f["name"], f) for f in crit["fields"])
    idx = rj(P["index1"])
    mp = rj(P["mapping2"])
    first = {}   # run -> (marker id, marks)
    second = {}
    for mid, v in sorted(idx["reports"].items()):
        first[v["run"]] = (mid, v["document"], rj(os.path.join(P["marks1"], mid + ".json")))
    for rid, v in sorted(mp["mapping"].items()):
        second[v["run"]] = (rid, v["document"], rj(os.path.join(P["marks2"], rid + ".json")))
    checks = OrderedDict()
    checks["first_marker_reports"] = len(first)
    checks["second_marker_reports"] = len(second)
    checks["same_96_runs_on_both_sides"] = set(first) == set(second) and len(first) == 96
    checks["document_mismatches"] = sorted(r for r in first if r in second
                                           and first[r][1] != second[r][1])
    checks["criteria_version"] = crit.get("version")
    checks["index_criteria_version"] = idx.get("criteria_version")
    checks["mapping_criteria_version"] = mp.get("criteria_version")
    checks["versions_all_equal"] = (crit.get("version") == idx.get("criteria_version")
                                    == mp.get("criteria_version"))
    checks["mapping_seed"] = mp.get("seed")
    per_set = Counter(set_of(r) for r in first)
    checks["reports_per_set_tag"] = dict(sorted(per_set.items()))
    return crit, fields, first, second, checks


def set_of(run):
    return run.split("_", 1)[0]


def group_of(run):
    t = set_of(run)
    for g, tags in SETS.items():
        if t in tags:
            return g
    raise SystemExit(f"run {run} is in no set of 48")


# --------------------------------------------------------------------------- the freeze check

def prompts_carry_frozen_criteria(fields, first, second):
    """Every marker-read field's criterion, as criteria.json words it, verbatim in every prompt."""
    marker_fields = [f for f in fields.values() if f.get("source", "the report") == "the report"]
    missing = []
    for folder, side in ((P["prompts1"], first), (P["prompts2"], second)):
        for run, (mid, _doc, _m) in side.items():
            txt = rt(os.path.join(folder, mid + ".txt"))
            for f in marker_fields:
                if f["criterion"] not in txt:
                    missing.append((mid, f["name"]))
                head = (f"### {f['name']} - {f['title']}\nkind: {f['kind']}; per: {f['per']}; "
                        f"layer: {f['layer']}")
                if head not in txt:
                    missing.append((mid, f["name"] + " (heading, kind, per or layer)"))
                if f.get("values") and ("### " + f["name"] + " ") in txt:
                    block = txt.split("### " + f["name"] + " ", 1)[1].split("\n### ", 1)[0]
                    if ("one of, and nothing else: " + ", ".join(f["values"])) not in block:
                        missing.append((mid, f["name"] + " (closed list)"))
            for f in fields.values():
                if f.get("source") == "the run record" and ("### " + f["name"] + " ") in txt:
                    missing.append((mid, "run-record field asked of the marker: " + f["name"]))
    return {"prompts_checked": len(first) + len(second),
            "marker_fields": len(marker_fields),
            "criterion_not_verbatim_or_record_field_asked": missing}


def prompts_carry_a_handed_in_question(first, second):
    """question_identity compares the report's frozen question with 'the one handed in'. Is any
    question handed in anywhere in the prompts, outside the criterion text itself?"""
    heads = Counter()
    for folder, side in ((P["prompts1"], first), (P["prompts2"], second)):
        for run, (mid, _d, _m) in side.items():
            for line in rt(os.path.join(folder, mid + ".txt")).splitlines():
                if line.startswith("=== "):
                    heads[line.strip()] += 1
    return {"section_headings_across_all_prompts": dict(heads),
            "a_question_section_present": any("QUESTION" in h.upper() for h in heads)}


# --------------------------------------------------------------------------- W10.18: the audit

def audit_strikes():
    a = rj(P["audit"])
    rerun = a.get("M085_rerun") or {}
    per = a.get("per_marker", {})
    struck = set(a.get("strikes") or [])
    other_reads = {k: v for k, v in per.items() if v.get("other", 0)}
    struck |= set(other_reads)
    if rerun.get("reads_outside"):
        struck.add("M085")
    # The mark in M085.json was written by the rerun; the per_marker M085 row is the first run,
    # which wrote nothing (writes 0). The audit that governs the mark in hand is the rerun's.
    out = OrderedDict()
    out["markers_in_audit"] = a.get("markers")
    out["per_marker_rows"] = len(per)
    out["first_marker_rows"] = sum(1 for k in per if k.startswith("M"))
    out["second_marker_rows"] = sum(1 for k in per if k.startswith("R"))
    out["audit_strikes_list"] = a.get("strikes")
    out["rows_with_other_reads"] = other_reads
    out["key_hits"] = a.get("key_hits")
    out["tools"] = a.get("tools")
    out["rows_not_8_reads_7_skill_1_write_0_other"] = {
        k: v for k, v in per.items()
        if v != {"reads": 8, "skill_files": 7, "writes": 1, "other": 0}}
    out["M085_rerun"] = rerun
    out["struck_marks"] = sorted(struck)
    out["markers_reading_another_file"] = len(struck)
    out["read_all_seven_skill_files"] = a.get("read_all_seven_skill_files")
    return out, struck


def returns_crosscheck():
    """The markers' own list of files read (claimed, not seen). Used for one thing only: which of
    the eight skill files were read, which the audit counts but does not name."""
    r = rj(P["returns"])["results"]
    rr = rj(P["returns_rerun"])["results"]
    missing = Counter()
    outside = []
    with_list = 0
    no_result = []
    for x in list(r) + list(rr):
        res = x.get("result")
        if not res or res.get("files_read") is None:
            no_result.append(os.path.basename(x.get("prompt", "?")))
            continue
        with_list += 1
        s = set(res["files_read"])
        for k in SKILL_FILES:
            if SKILL_DIR + k not in s:
                missing[k] += 1
        for f in res["files_read"]:
            if not f.startswith(SKILL_DIR) and f != res.get("prompt_file"):
                outside.append((os.path.basename(res.get("prompt_file", "?")), f))
    return {"returns_with_a_files_read_list": with_list,
            "returns_with_no_result": no_result,
            "skill_files_not_in_files_read": dict(missing),
            "files_read_outside_skill_and_own_prompt": outside}


# --------------------------------------------------------------------------- agreement

def has_value(v):
    return v is not None


def agree(kind, a, b):
    if kind in ("enum", "int", "bool"):
        return a == b
    if kind == "set":
        return set(a) == set(b)
    if kind == "map_enum":
        return dict(a) == dict(b)
    raise ValueError(kind)


def value_of(side, run, field, struck):
    mid, _doc, marks = side[run]
    if mid in struck:
        return None
    return marks.get(field)          # a key the marker did not write is no value


def count_field(fields, first, second, struck, name, runs, empty_map_is_value=True):
    kind = fields[name]["kind"]
    res = {"n": len(runs), "agree": 0, "disagree": 0, "unreadable": 0,
           "disagree_runs": [], "unreadable_runs": []}
    for run in runs:
        a = value_of(first, run, name, struck)
        b = value_of(second, run, name, struck)
        if not empty_map_is_value and kind == "map_enum":
            a = a if a else None
            b = b if b else None
        if not (has_value(a) and has_value(b)):
            res["unreadable"] += 1
            res["unreadable_runs"].append(run)
        elif agree(kind, a, b):
            res["agree"] += 1
        else:
            res["disagree"] += 1
            res["disagree_runs"].append(run)
    res["readable"] = res["agree"] + res["disagree"]
    return res


def thresholds(test_remove_reading):
    t = {}
    for f in P31:
        t[f] = 44
    for f in P32:
        t[f] = 40
    for f in P33:
        t[f] = 46
    for f in P35:
        t[f] = 42
    for f in AT39_NAMED:
        t[f] = 39
    if test_remove_reading == "A":
        t["test_remove"] = 39
    return t


# --------------------------------------------------------------------------- the split

NAME_RE_FILE = re.compile(r"\b(runs|runs_repeat|runs_repeat_31|runs_sonnet5|runs_sonnet5_31)/"
                          r"([A-Za-z0-9]+b?-m[0-9](?:-r[0-9])?|X)(?:\.json)?")
NAME_RE_RUNID = re.compile(r"(?<![A-Za-z0-9_])(p52|rep31|rep|son31|son)_"
                           r"([A-Z][0-9]+b?-m[0-9](?:-r[0-9])?)")
NAME_RE_BARE = re.compile(r"(?<![/_A-Za-z0-9])([A-Z][0-9]+b?-m[0-9](?:-r[0-9])?)(?![A-Za-z0-9])")
FOLDER_TO_SET = {"runs": "p52", "runs_repeat": "rep", "runs_repeat_31": "rep31",
                 "runs_sonnet5": "son", "runs_sonnet5_31": "son31"}


def read_reports(all_runs):
    crit_txt = rt(P["criteria"])
    plan_txt = rt(P["marking_plan"])
    plan_lines = plan_txt.splitlines()
    sec13 = next(i for i, l in enumerate(plan_lines) if l.startswith("## 13."))
    plan_late = "\n".join(plan_lines[sec13:])
    out = OrderedDict()
    placeholders = set()
    not_in_96 = set()

    def by_file(texts):
        s = set()
        for t in texts:
            for m in NAME_RE_FILE.finditer(t):
                folder, stem = m.group(1), m.group(2)
                if stem == "X":
                    placeholders.add(m.group(0))
                    continue
                run = FOLDER_TO_SET[folder] + "_" + stem
                if run in all_runs:
                    s.add(run)
                else:
                    not_in_96.add(m.group(0))
        return s

    def by_runid(texts):
        s = set()
        for t in texts:
            for m in NAME_RE_RUNID.finditer(t):
                run = m.group(1) + "_" + m.group(2)
                if run in all_runs:
                    s.add(run)
                else:
                    not_in_96.add(m.group(0))
        return s

    def by_bare(texts):
        s = set()
        for t in texts:
            for m in NAME_RE_BARE.finditer(t):
                stem = m.group(1)
                for tag in ("p52", "rep", "rep31", "son", "son31"):
                    if tag + "_" + stem in all_runs:
                        s.add(tag + "_" + stem)
        return s

    A = by_file([crit_txt, plan_txt])
    B = A | by_runid([crit_txt, plan_txt])
    C = B | by_bare([crit_txt, plan_txt])
    D = by_file([plan_late]) | by_runid([plan_late])
    # E: W14's purpose sentence ("the reports any maker or reviewer read") against its
    # operational one ("named"): the marking plan says A4 read all 24 of runs_sonnet5 and
    # runs_repeat (section 10: "Read all 24 for the strict pattern"; "Ran the scan on all 24").
    E = B | {r for r in all_runs if set_of(r) in ("rep", "son")}
    out["A_record_file_names_only"] = sorted(A)
    out["B_record_file_names_and_run_ids (primary)"] = sorted(B)
    out["C_B_plus_bare_stems_in_every_set"] = sorted(C)
    out["D_W13_marking_plan_sections_13_to_15_only"] = sorted(D)
    out["E_B_plus_all_24_of_rep_and_son"] = sorted(E)
    meta = {"placeholders_excluded": sorted(placeholders),
            "names_not_among_the_96": sorted(not_in_96)}
    return out, meta


def split_field(fields, first, second, struck, name, runs, read):
    r = [x for x in runs if x in read]
    u = [x for x in runs if x not in read]
    out = OrderedDict()
    for label, rs in (("all_96", runs), ("read", r), ("unread", u)):
        c = count_field(fields, first, second, struck, name, rs)
        c["pct_of_n"] = round(100.0 * c["agree"] / c["n"], 2) if c["n"] else None
        c["pct_of_readable"] = (round(100.0 * c["agree"] / c["readable"], 2)
                                if c["readable"] else None)
        out[label] = c
    for basis in ("pct_of_n", "pct_of_readable"):
        a, b = out["read"][basis], out["unread"][basis]
        out["read_minus_unread_pp_" + basis[4:]] = (None if a is None or b is None
                                                    else round(a - b, 2))
    return out


# --------------------------------------------------------------------------- W10.17

def w10_17(fields, first, second, include_map_enum):
    out = OrderedDict()
    for name, f in fields.items():
        if f.get("source") == "the run record":
            continue
        if f["kind"] != "enum" and not (include_map_enum and f["kind"] == "map_enum"):
            continue
        vals = set(f.get("values") or [])
        row = OrderedDict()
        for label, side in (("first", first), ("second", second)):
            c = Counter()
            off = []
            for run, (mid, _d, marks) in side.items():
                v = marks.get(name)
                if v is None:
                    c["null"] += 1
                elif f["kind"] == "enum":
                    if v in vals:
                        c["closed_list"] += 1
                    else:
                        c["off_list"] += 1
                        off.append((mid, v))
                else:
                    bad = [x for x in v.values() if x not in vals]
                    if bad:
                        c["off_list"] += 1
                        off.append((mid, bad))
                    else:
                        c["closed_list"] += 1
            row[label] = {"closed_list": c["closed_list"], "null": c["null"],
                          "off_list": c["off_list"], "off_list_values": off,
                          "at_least_95_of_96": c["closed_list"] >= 95}
        row["certified_candidate"] = f.get("certified_candidate")
        row["holds_on_this_field"] = row["first"]["at_least_95_of_96"] and \
            row["second"]["at_least_95_of_96"]
        out[name] = row
    return out


# --------------------------------------------------------------------------- diagnostics

def map_disagreement_kinds(first, second, runs, name):
    kinds = Counter()
    for run in runs:
        a = first[run][2].get(name)
        b = second[run][2].get(name)
        if a is None or b is None or a == b:
            continue
        if set(a) != set(b):
            kinds["key sets differ"] += 1
        else:
            kinds["same keys, a value differs"] += 1
    return dict(kinds)


def set_sensitivity(first, second, runs, name):
    """Not a reading of the text: how many disagreements vanish if members are compared
    case-insensitively with whitespace collapsed, and (pairs) with the pair's order ignored."""
    def norm(s, unordered):
        out = set()
        for x in s:
            y = " ".join(x.split()).casefold()
            if unordered and "|" in y:
                y = "|".join(sorted(p.strip() for p in y.split("|", 1)))
            out.add(y)
        return out
    res = {"disagree_exact": 0, "disagree_casefold": 0, "disagree_casefold_unordered": 0}
    for run in runs:
        a = first[run][2].get(name)
        b = second[run][2].get(name)
        if a is None or b is None:
            continue
        if set(a) != set(b):
            res["disagree_exact"] += 1
        if norm(a, False) != norm(b, False):
            res["disagree_casefold"] += 1
        if norm(a, True) != norm(b, True):
            res["disagree_casefold_unordered"] += 1
    return res


def by_source_document(fields, first, second, struck, name, runs):
    """The other reading of 'a count of documents': a source document agrees when every report
    on it is readable and agrees. Diagnostic; the thresholds 'of 48' cannot be applied to it."""
    docs = OrderedDict()
    for run in runs:
        docs.setdefault(first[run][1], []).append(run)
    n_ok = 0
    for d, rs in docs.items():
        c = count_field(fields, first, second, struck, name, rs)
        if c["agree"] == len(rs):
            n_ok += 1
    return {"documents": len(docs), "documents_all_reports_agree": n_ok}


# --------------------------------------------------------------------------- rival checks
#
# Two explanations offered by the texts are checked against their best rivals here. None of
# this changes a tick; it says what a tick can and cannot be read as.
#
# (1) W10.16's own reading of a gap: "the criterion was fitted to what its makers read". Rival:
#     the read reports are mostly repeat-set reports (P3 and F4 only), and the repeat set agrees
#     more on nearly every field, reworded or not; with n_read about 26, one report is about
#     4 points. Checks: the same gap on the fields never reworded twice (a placebo: if the gap
#     is composition, it shows there too); the gap inside each set; and a permutation that
#     keeps each set's number of read reports and asks how often a random read set of that
#     shape gives a gap as large.
# (2) Derivation 3, qualified: the criteria were tested on the 24 reports of runs_sonnet5 and
#     runs_repeat (sets son and rep; marking plan, preamble and section 10: "Read all 24"), so
#     they are faithful there and, wherever the population admits an alternative,
#     unconstrained elsewhere. Rival for "lower agreement off the fitting set": the p52
#     reports are harder to mark whatever the criteria's history (sixteen documents, three
#     modes). Check: rep+son (fitted) against rep31+son31 (the same two documents, the same
#     transports, a later skill file, never named by the instrument).

def fitting_checks(fields, first, second, struck, comparable, runs_all, runs_by_set, read_sets,
                   primary_label, seed=20260923, draws=20000):
    import random
    out = OrderedDict()
    groups = OrderedDict([
        ("rep+son (the 24 the criteria were tested on)",
         [r for r in runs_all if set_of(r) in ("rep", "son")]),
        ("rep31+son31 (same documents, not named by the instrument)",
         [r for r in runs_all if set_of(r) in ("rep31", "son31")]),
        ("p52 mode 0", [r for r in runs_all if set_of(r) == "p52" and r.endswith("-m0")]),
        ("p52 mode 1", [r for r in runs_all if set_of(r) == "p52" and r.endswith("-m1")]),
        ("p52 mode 2", [r for r in runs_all if set_of(r) == "p52" and r.endswith("-m2")]),
    ])
    tab = OrderedDict()
    for n in comparable:
        tab[n] = {g: f"{count_field(fields, first, second, struck, n, rs)['agree']}/{len(rs)}"
                  for g, rs in groups.items()}
    out["agreement_by_subgroup"] = tab
    fitted_better = [n for n in comparable if int(tab[n][list(groups)[0]].split("/")[0])
                     > int(tab[n][list(groups)[1]].split("/")[0])]
    unfitted_better = [n for n in comparable if int(tab[n][list(groups)[0]].split("/")[0])
                       < int(tab[n][list(groups)[1]].split("/")[0])]
    out["fields_where_rep+son_agree_more_than_rep31+son31"] = fitted_better
    out["fields_where_rep31+son31_agree_more_than_rep+son"] = unfitted_better

    # (1) placebo, stratified gaps, permutation
    read = set(read_sets[primary_label])
    placebo = OrderedDict()
    for n in comparable:
        if n in TWICE_REWORDED:
            continue
        s = split_field(fields, first, second, struck, n, runs_all, read)
        placebo[n] = s["read_minus_unread_pp_of_n"]
    out["placebo_gap_pp_on_fields_not_reworded_twice (primary read set)"] = placebo
    out["placebo_fields_with_gap_over_10pp"] = [n for n, v in placebo.items()
                                                if v is not None and v > 10]
    strat = OrderedDict()
    for n in TWICE_REWORDED:
        strat[n] = {}
        for g, rs in runs_by_set.items():
            s = split_field(fields, first, second, struck, n, rs, read)
            strat[n][g] = {"read": f"{s['read']['agree']}/{s['read']['n']}",
                           "unread": f"{s['unread']['agree']}/{s['unread']['n']}",
                           "gap_pp": s["read_minus_unread_pp_of_n"]}
    out["gap_inside_each_set (primary read set)"] = strat

    rng = random.Random(seed)
    agree_flag = {n: {r: None for r in runs_all} for n in TWICE_REWORDED}
    for n in TWICE_REWORDED:
        for r in runs_all:
            c = count_field(fields, first, second, struck, n, [r])
            agree_flag[n][r] = c["agree"] == 1
    perm = OrderedDict()
    for label, rs_read in read_sets.items():
        rset = set(rs_read)
        k_by_set = {g: sum(1 for r in v if r in rset) for g, v in runs_by_set.items()}
        perm[label] = {}
        for n in TWICE_REWORDED:
            def gap(sel):
                a_r = sum(agree_flag[n][r] for r in sel)
                rest = [r for r in runs_all if r not in sel]
                a_u = sum(agree_flag[n][r] for r in rest)
                return 100.0 * a_r / len(sel) - 100.0 * a_u / len(rest)
            obs = gap(rset)
            ge = 0
            for _ in range(draws):
                sel = set()
                for g, v in runs_by_set.items():
                    sel.update(rng.sample(v, k_by_set[g]))
                if gap(sel) >= obs - 1e-9:
                    ge += 1
            perm[label][n] = {"observed_gap_pp": round(obs, 2),
                              "share_of_random_read_sets_with_gap_at_least_as_large":
                                  round(ge / draws, 4),
                              "draws": draws, "seed": seed,
                              "read_reports_per_set_kept": k_by_set}
    out["permutation_keeping_each_sets_share_of_read_reports"] = perm

    # (3) the anatomy of every disagreement on a map or set field: does it sit on how a key or
    # member is written (the quoted text), or on what the report was read to contain (the
    # rule)? Marking plan 13.5: "If stage B's disagreements on these four fields turn out to sit
    # on the quoted text rather than on the rule, the patches bought agreement at the price of
    # meaning, and that is what to look for first in the stage B numbers."
    import unicodedata

    def norm(s):
        s = unicodedata.normalize("NFKC", s)
        for x, y in (("“", '"'), ("”", '"'), ("‘", "'"), ("’", "'"),
                     ("′", "'")):
            s = s.replace(x, y)
        s = re.sub(r"[^\w\s]", "", s).casefold()
        return " ".join(s.split())

    anatomy = OrderedDict()
    for n in comparable:
        kind = fields[n]["kind"]
        if kind not in ("set", "map_enum"):
            continue
        rows = OrderedDict()
        tally = Counter()
        for r in runs_all:
            a, b = first[r][2].get(n), second[r][2].get(n)
            if a is None or b is None:
                continue
            if (kind == "map_enum" and a == b) or (kind == "set" and set(a) == set(b)):
                continue
            if kind == "map_enum":
                na = {norm(k): v for k, v in a.items()}
                nb = {norm(k): v for k, v in b.items()}
                shared = set(na) & set(nb)
                if na == nb:
                    k = "transcription only (keys equal once quotes, punctuation, case dropped)"
                elif set(na) == set(nb):
                    k = "same keys, a value differs"
                elif (set(na) < set(nb) or set(nb) < set(na)) and all(
                        na[x] == nb[x] for x in shared):
                    k = "inclusion (one map is the other plus rows)"
                else:
                    k = "keys differ"
            else:
                na, nb = {norm(x) for x in a}, {norm(x) for x in b}
                if na == nb:
                    k = "transcription only"
                elif na < nb or nb < na:
                    k = "inclusion (one set is the other plus members)"
                else:
                    k = "members differ"
            tally[k] += 1
            rows[r] = {"kind": k, "first": a, "second": b} if kind == "set" else {
                "kind": k,
                "first_only": sorted(set(a) - set(b)),
                "second_only": sorted(set(b) - set(a)),
                "values_differ_on": sorted(x for x in set(a) & set(b) if a[x] != b[x])}
        anatomy[n] = {"tally": dict(tally), "per_report": rows}
    out["disagreement_anatomy"] = anatomy

    # (4) shape: how much element-level disagreement the PART bin absorbs
    absorbed = 0
    se_dis = 0
    for r in runs_all:
        a, b = first[r][2], second[r][2]
        if a.get("shape_elements") is None or b.get("shape_elements") is None:
            continue
        if a["shape_elements"] != b["shape_elements"]:
            se_dis += 1
            if a.get("shape") == b.get("shape"):
                absorbed += 1
    out["shape_elements_disagreements_with_the_same_shape"] = {
        "shape_elements_disagreements": se_dis, "of_which_shape_agrees": absorbed}
    return out


# --------------------------------------------------------------------------- main

def main():
    crit, fields, first, second, checks = load()
    runs_all = sorted(first)
    runs_by_set = OrderedDict((g, [r for r in runs_all if group_of(r) == g]) for g in SETS)
    checks["reports_per_set_of_48"] = {g: len(v) for g, v in runs_by_set.items()}
    checks["prompts"] = prompts_carry_frozen_criteria(fields, first, second)
    checks["question_handed_in"] = prompts_carry_a_handed_in_question(first, second)
    checks["shape_follows_elements"] = {}
    for label, side in (("first", first), ("second", second)):
        bad = []
        for run, (mid, _d, m) in side.items():
            se = m.get("shape_elements")
            if not isinstance(se, dict):
                continue
            ny = sum(1 for v in se.values() if v == "Y")
            exp = "FULL" if ny == 7 else ("NONE" if ny == 0 else "PART")
            if m.get("shape") != exp or set(se) != {f"E{i}" for i in range(1, 8)}:
                bad.append((mid, m.get("shape"), ny))
        checks["shape_follows_elements"][label] = bad

    audit, struck = audit_strikes()
    returns = returns_crosscheck()

    program_filled = [n for n, f in fields.items() if f.get("source") == "the run record"]
    comparable = [n for n, f in fields.items() if f["kind"] in COMPARABLE
                  and f.get("source", "the report") == "the report"]
    text_fields = [n for n, f in fields.items() if f["kind"] == "text"]

    # ---- agreement per field, per set, pooled
    thr_A = thresholds("A")
    thr_B = thresholds("B")
    per_field = OrderedDict()
    for name in comparable:
        f = fields[name]
        row = OrderedDict()
        row["kind"] = f["kind"]
        row["sort"] = f["sort"]
        row["certified_candidate"] = f.get("certified_candidate")
        row["threshold_of_48"] = thr_A.get(name)
        for g, rs in runs_by_set.items():
            row[g] = count_field(fields, first, second, struck, name, rs)
        row["pooled_96"] = count_field(fields, first, second, struck, name, runs_all)
        t = thr_A.get(name)
        if t is None or not f.get("certified_candidate"):
            row["reaches_threshold"] = None
            row["certified"] = None
            row["note"] = ("not a certified candidate: reported, no threshold"
                           if not f.get("certified_candidate") else "no threshold")
        else:
            row["reaches_threshold"] = {g: row[g]["agree"] >= t for g in runs_by_set}
            row["certified"] = all(row["reaches_threshold"].values())
            # the other reading of a threshold 'of 48': a proportion of the readable reports
            row["reaches_threshold_as_proportion_of_readable"] = {
                g: (row[g]["readable"] > 0 and row[g]["agree"] >= math.ceil(
                    t / 48.0 * row[g]["readable"] - 1e-9)) for g in runs_by_set}
        per_field[name] = row

    # ---- the P3 predictions, read per set of 48
    def cert(n):
        return per_field[n]["certified"]

    p31_fieldwise = [n for n in P31 if cert(n)]
    p31_per_set = {g: [n for n in P31 if per_field[n][g]["agree"] >= 44] for g in runs_by_set}
    predictions = OrderedDict()
    predictions["P3.1"] = {
        "rule": "shape, turned_own_test, same_explanation: at least two of the three at 44 of 48, "
                "in each set of 48",
        "counts": {n: {g: per_field[n][g]["agree"] for g in runs_by_set} for n in P31},
        "fields_reaching_44_in_both_sets (primary)": p31_fieldwise,
        "holds (primary: each field in both sets, then two of three)": len(p31_fieldwise) >= 2,
        "fields_reaching_44_per_set (other reading)": p31_per_set,
        "holds (other reading: two of three in each set, any two)":
            all(len(v) >= 2 for v in p31_per_set.values()),
    }
    predictions["P3.2"] = {
        "rule": "marks_per_part, pairs_that_pull, rivals_built each 40 of 48, in each set",
        "counts": {n: {g: per_field[n][g]["agree"] for g in runs_by_set} for n in P32},
        "certified": {n: cert(n) for n in P32},
        "holds": all(cert(n) for n in P32),
    }
    predictions["P3.3"] = {
        "rule": "question_identity 46 of 48, in each set",
        "counts": {g: per_field["question_identity"][g]["agree"] for g in runs_by_set},
        "unreadable": {g: per_field["question_identity"][g]["unreadable"] for g in runs_by_set},
        "holds": cert("question_identity"),
    }
    predictions["P3.4"] = {
        "rule": "at most one field needs a second rewording",
        "counts": {"marks_per_part": 2, "pairs_that_pull": 2,
                   "rivals_built": "2, or 3 on the marking plan 13.5 stricter reading"},
        "holds": False,
        "note": "failed on the count before any mark existed (marking plan 14.4; W13 section 2); "
                "recorded, not re-read (W14 section 4). Not computed from marks.",
    }
    predictions["P3.5"] = {
        "rule": "test_swap and test_poke each 42 of 48, in each set",
        "counts": {n: {g: per_field[n][g]["agree"] for g in runs_by_set} for n in P35},
        "certified": {n: cert(n) for n in P35},
        "holds": all(cert(n) for n in P35),
    }
    others = [n for n in comparable if thr_A.get(n) == 39]
    predictions["other_fields_at_39"] = {
        "rule": "every other certified-candidate field at 39 of 48, in each set (the "
                "instrument's addition); test_remove included on the primary reading",
        "counts": {n: {g: per_field[n][g]["agree"] for g in runs_by_set} for n in others},
        "certified": {n: cert(n) for n in others},
        "failing": [n for n in others if not cert(n)],
        "holds": all(cert(n) for n in others),
        "test_remove_other_reading": ("the table's 'the other eight tests' read literally as "
                                      "the eight cross-step tests leaves test_remove with no "
                                      "threshold: counts unchanged, test_remove uncertifiable"),
    }

    # ---- the split and W10.16
    read_sets, read_meta = read_reports(set(runs_all))
    split = OrderedDict()
    w1016 = OrderedDict()
    for label, rs in read_sets.items():
        rset = set(rs)
        split[label] = OrderedDict()
        split[label]["n_read"] = len(rset)
        split[label]["n_read_per_set"] = {g: sum(1 for r in v if r in rset)
                                          for g, v in runs_by_set.items()}
        for name in TWICE_REWORDED:
            split[label][name] = split_field(fields, first, second, struck, name, runs_all, rset)
        verdicts = {}
        for basis in ("of_n", "of_readable"):
            gaps = {n: split[label][n]["read_minus_unread_pp_" + basis] for n in TWICE_REWORDED}
            verdicts[basis] = {"gaps_pp": gaps,
                               "falsified_on": [n for n, v in gaps.items()
                                                if v is not None and v > 10.0],
                               "holds": all(v is not None and v <= 10.0 for v in gaps.values())}
        w1016[label] = verdicts

    # W10.16's consequence, where falsified: certified on the unread reports only, per set,
    # at the field's threshold as a proportion of the unread reports in that set.
    def unread_certification(rset, name):
        t = thr_A[name]
        out = {}
        for g, rs in runs_by_set.items():
            u = [r for r in rs if r not in rset]
            c = count_field(fields, first, second, struck, name, u)
            need = math.ceil(t / 48.0 * len(u) - 1e-9)
            out[g] = {"n_unread": len(u), "agree": c["agree"], "needed": need,
                      "reaches": c["agree"] >= need}
        return out
    primary_label = "B_record_file_names_and_run_ids (primary)"
    w1016_consequence = {}
    for label in read_sets:
        fals = set(w1016[label]["of_n"]["falsified_on"]) | set(
            w1016[label]["of_readable"]["falsified_on"])
        w1016_consequence[label] = {n: unread_certification(set(read_sets[label]), n)
                                    for n in sorted(fals)}

    predictions["W10.16"] = {
        "rule": "on the twice-reworded fields, agreement over the read reports does not exceed "
                "agreement over the unread reports by more than 10 percentage points",
        "primary": w1016[primary_label],
        "all_readings": w1016,
        "consequence_where_falsified (unread only, per set, threshold scaled)":
            w1016_consequence,
    }

    # ---- W10.17
    e17 = w10_17(fields, first, second, include_map_enum=False)
    e17m = w10_17(fields, first, second, include_map_enum=True)
    predictions["W10.17"] = {
        "rule": "both markers return a closed-list value on at least 95 of 96 reports on every "
                "enum field",
        "primary (kind enum, all 17)": {
            "failing_fields": [n for n, v in e17.items() if not v["holds_on_this_field"]],
            "holds": all(v["holds_on_this_field"] for v in e17.values())},
        "other reading (enum and map_enum)": {
            "failing_fields": [n for n, v in e17m.items() if not v["holds_on_this_field"]],
            "holds": all(v["holds_on_this_field"] for v in e17m.values())},
        "other reading (certified-candidate enum only)": {
            "failing_fields": [n for n, v in e17.items() if v["certified_candidate"]
                               and not v["holds_on_this_field"]],
            "holds": all(v["holds_on_this_field"] for v in e17.values()
                         if v["certified_candidate"])},
        "per_field": e17m,
    }

    # ---- W10.18
    predictions["W10.18"] = {
        "rule": "every marker's audit shows Reads of the skill and its prompt only; a marker "
                "reading any other file strikes its mark; more than three and the stage re-runs",
        "markers_reading_another_file": audit["markers_reading_another_file"],
        "struck_marks": audit["struck_marks"],
        "holds": audit["markers_reading_another_file"] == 0,
        "rerun_needed": audit["markers_reading_another_file"] > 3,
    }

    # ---- consequences of section 6, as written
    consequences = OrderedDict()
    consequences["P3.1"] = ("holds: the cross-step fields may carry an arm difference where "
                            "certified" if predictions["P3.1"][
                                "holds (primary: each field in both sets, then two of three)"]
                            else "fails: the cross-step fields cannot carry an arm difference; "
                                 "stage C runs on the certified fields and the two marker-free "
                                 "read-outs alone, and says so")
    swap_ok, poke_ok = cert("test_swap"), cert("test_poke")
    consequences["P3.5"] = {
        "test_swap_certified": swap_ok, "test_poke_certified": poke_ok,
        "within_step_set_if_both_leave": list(WITHIN_STEP_IF_P35_FAILS),
        "reading_each_leaves_alone": [n for n in P35 if not cert(n)],
        "reading_both_leave_if_either_fails": list(P35) if not (swap_ok and poke_ok) else [],
        "reading_only_if_both_fail": list(P35) if not (swap_ok or poke_ok) else [],
        "P4.4_read_on (as section 6 writes it)": list(WITHIN_STEP_IF_P35_FAILS),
        "P4.4_read_on (other reading: only those of the seven that stage B certified)":
            [n for n in WITHIN_STEP_IF_P35_FAILS if cert(n)],
    }
    consequences["P3.2"] = {n: ("certified" if cert(n) else "kept as quotes only")
                            for n in P32}
    consequences["P3.4"] = "failed before marking; recorded, not re-read (W13, W14)"
    cross = [n for n in comparable if fields[n]["sort"] == "cross-step"
             and fields[n].get("certified_candidate")]
    certified_fields = [n for n in comparable if per_field[n]["certified"]]
    if not predictions["P3.1"]["holds (primary: each field in both sets, then two of three)"]:
        carries = [n for n in certified_fields if n not in cross]
    else:
        carries = list(certified_fields)
    consequences["certified_fields"] = certified_fields
    consequences["certified_and_able_to_carry_an_arm_difference"] = carries
    consequences["struck_fields"] = [n for n in comparable
                                     if per_field[n]["certified"] is False]

    # ---- the other readings and sensitivities
    alt = OrderedDict()
    alt["test_remove_threshold"] = {
        "A (primary): 39, W14 section 4 'the other fields at 39'":
            per_field["test_remove"]["certified"],
        "B: none, the table's 'the other eight tests' as the eight cross-step tests":
            "no threshold; uncertifiable; counts unchanged"}
    alt["threshold_as_proportion_of_readable"] = {
        n: per_field[n].get("reaches_threshold_as_proportion_of_readable")
        for n in comparable if per_field[n]["certified"] is not None}
    alt["empty_map_as_no_value"] = {
        n: {g: count_field(fields, first, second, struck, n, rs, empty_map_is_value=False)
            ["agree"] for g, rs in runs_by_set.items()}
        for n in comparable if fields[n]["kind"] == "map_enum"}
    alt["count_of_source_documents"] = {
        n: {g: by_source_document(fields, first, second, struck, n, rs)
            for g, rs in runs_by_set.items()} for n in comparable}
    alt["set_member_sensitivity (diagnostic, not a reading)"] = {
        n: {g: set_sensitivity(first, second, rs, n) for g, rs in runs_by_set.items()}
        for n in comparable if fields[n]["kind"] == "set"}
    alt["map_disagreement_kinds (diagnostic)"] = {
        n: {g: map_disagreement_kinds(first, second, rs, n) for g, rs in runs_by_set.items()}
        for n in comparable if fields[n]["kind"] == "map_enum"}
    qi = OrderedDict()
    for g, rs in runs_by_set.items():
        both = [r for r in rs if first[r][2].get("question_identity") is not None
                and second[r][2].get("question_identity") is not None]
        onlyone = [r for r in rs if (first[r][2].get("question_identity") is None)
                   != (second[r][2].get("question_identity") is None)]
        qi[g] = {"both_null": sum(1 for r in rs if first[r][2].get("question_identity") is None
                                  and second[r][2].get("question_identity") is None),
                 "one_null": len(onlyone),
                 "both_valued": len(both),
                 "both_valued_and_equal": sum(1 for r in both if first[r][2][
                     "question_identity"] == second[r][2]["question_identity"])}
    alt["question_identity_nulls (the check between 'no target handed in' and 'markers "
        "disagree')"] = qi

    rivals = fitting_checks(fields, first, second, struck, comparable, runs_all, runs_by_set,
                            read_sets, primary_label)

    out = OrderedDict()
    out["made_by"] = "stage-B/independent-check/recompute.py (standard library only)"
    out["inputs"] = {k: v for k, v in P.items()}
    out["checks"] = checks
    out["fields_filled_by_program_not_by_a_marker"] = {
        "fields": program_filled,
        "why_not_counted": "both sides are filled from one run record by program "
                           "(record_adapter.py; first_marker.py collect), so any agreement on "
                           "them is by construction and not a marker agreement; none is "
                           "certified_candidate"}
    out["text_fields_never_compared"] = text_fields
    out["comparable_marker_fields"] = comparable
    out["per_field"] = per_field
    out["predictions"] = predictions
    out["consequences"] = consequences
    out["read_reports"] = read_sets
    out["read_reports_meta"] = read_meta
    out["split"] = split
    out["audit"] = audit
    out["returns_crosscheck (claimed, not seen)"] = returns
    out["other_readings"] = alt
    out["rival_checks"] = rivals

    with open(os.path.join(HERE, "output.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    with open(os.path.join(HERE, "output.txt"), "w", encoding="utf-8") as f:
        f.write(render(out, runs_by_set))
    print(render_head(out))


# --------------------------------------------------------------------------- the readable file

def yn(b):
    return {True: "yes", False: "NO", None: "-"}[b]


def render_head(o):
    pr = o["predictions"]
    lines = ["independent recompute: " + ("ok" if o["checks"]["same_96_runs_on_both_sides"]
                                          else "PAIRING FAILED")]
    lines.append("certified: " + ", ".join(o["consequences"]["certified_fields"]))
    lines.append("struck: " + ", ".join(o["consequences"]["struck_fields"]))
    for k in ("P3.2", "P3.3", "P3.5", "other_fields_at_39"):
        lines.append(f"{k}: holds={pr[k]['holds']}")
    lines.append("P3.1: holds=" + str(
        pr["P3.1"]["holds (primary: each field in both sets, then two of three)"]))
    lines.append("W10.16 (primary): " + json.dumps(pr["W10.16"]["primary"]))
    lines.append("W10.17: " + json.dumps(pr["W10.17"]["primary (kind enum, all 17)"]))
    lines.append("W10.18: holds=" + str(pr["W10.18"]["holds"]))
    return "\n".join(lines)


def render(o, runs_by_set):
    L = []
    w = L.append
    c = o["checks"]
    w("STAGE B, RECOMPUTED INDEPENDENTLY (W14)")
    w("=" * 78)
    w("Counts of reports, by field, per set of 48. Nothing is summed across fields or sets.")
    w("")
    w("Pairing and freeze checks")
    w(f"  reports: first {c['first_marker_reports']}, second {c['second_marker_reports']}; "
      f"same 96 runs on both sides: {yn(c['same_96_runs_on_both_sides'])}; "
      f"document mismatches: {len(c['document_mismatches'])}")
    w(f"  per set tag: {c['reports_per_set_tag']}; per set of 48: {c['reports_per_set_of_48']}")
    w(f"  criteria version: criteria.json {c['criteria_version']}, index "
      f"{c['index_criteria_version']}, mapping {c['mapping_criteria_version']} "
      f"(all equal: {yn(c['versions_all_equal'])}); mapping seed {c['mapping_seed']}")
    pc = c["prompts"]
    w(f"  prompts checked: {pc['prompts_checked']}; each of {pc['marker_fields']} marker fields' "
      f"criterion verbatim in every prompt, no run-record field asked: "
      f"{yn(not pc['criterion_not_verbatim_or_record_field_asked'])}")
    q = c["question_handed_in"]
    w(f"  prompt sections across all 192: {q['section_headings_across_all_prompts']}; a question "
      f"handed in: {yn(q['a_question_section_present'])}")
    w(f"  shape follows shape_elements: first {len(c['shape_follows_elements']['first'])} "
      f"breaches, second {len(c['shape_follows_elements']['second'])} breaches")
    w("")
    w("Fields filled by program, not by a marker (not counted): "
      + ", ".join(o["fields_filled_by_program_not_by_a_marker"]["fields"]))
    w("Text fields, never compared: " + ", ".join(o["text_fields_never_compared"]))
    w("")
    w("Agreement by field (agree / disagree / unreadable), per set of 48, pooled 96 beside")
    w("  threshold: the count of agreeing reports needed in EACH set of 48; the pooled 96 is "
      "never the gate")
    hdr = (f"  {'field':24s} {'thr':>3s}  {'p52 a/d/u':>11s}  {'repeat a/d/u':>12s}  "
           f"{'pooled a/d/u':>12s}  certified")
    w(hdr)
    for n, r in o["per_field"].items():
        def t(x):
            return f"{x['agree']}/{x['disagree']}/{x['unreadable']}"
        thr = "" if r["threshold_of_48"] is None or not r["certified_candidate"] else \
            str(r["threshold_of_48"])
        cert = "not a candidate" if not r["certified_candidate"] else yn(r["certified"])
        w(f"  {n:24s} {thr:>3s}  {t(r['p52']):>11s}  {t(r['repeat']):>12s}  "
          f"{t(r['pooled_96']):>12s}  {cert}")
    w("")
    w("Unreadable reports, named (either marker left no value)")
    for n, r in o["per_field"].items():
        u = r["pooled_96"]["unreadable_runs"]
        if u:
            w(f"  {n}: {len(u)}: " + ", ".join(u))
    w("")
    w("Disagreeing reports, named")
    for n, r in o["per_field"].items():
        d = r["pooled_96"]["disagree_runs"]
        if d:
            w(f"  {n} ({len(d)}): " + ", ".join(d))
    w("")
    pr = o["predictions"]
    w("Predictions of W14 section 4, ticked from these counts")
    p = pr["P3.1"]
    w(f"  W3 P3.1  {p['counts']}")
    w(f"           reaching 44 in both sets: {p['fields_reaching_44_in_both_sets (primary)']} -> "
      f"holds: {yn(p['holds (primary: each field in both sets, then two of three)'])}; other "
      f"reading (two of three per set, any two): "
      f"{yn(p['holds (other reading: two of three in each set, any two)'])}")
    p = pr["P3.2"]
    w(f"  W3 P3.2  {p['counts']} -> holds: {yn(p['holds'])}")
    p = pr["P3.3"]
    w(f"  W3 P3.3  agree {p['counts']}, unreadable {p['unreadable']} -> holds: {yn(p['holds'])}")
    p = pr["P3.4"]
    w(f"  W3 P3.4  {p['counts']} -> holds: NO ({p['note']})")
    p = pr["P3.5"]
    w(f"  W3 P3.5  {p['counts']} -> holds: {yn(p['holds'])}")
    p = pr["other_fields_at_39"]
    w(f"  other fields at 39: failing {p['failing']} -> holds: {yn(p['holds'])}")
    p = pr["W10.16"]
    w(f"  W10.16 (read reports, primary reading B): {json.dumps(p['primary'])}")
    for lab, v in p["all_readings"].items():
        w(f"          {lab}: of n {v['of_n']['gaps_pp']} holds {yn(v['of_n']['holds'])}; "
          f"of readable {v['of_readable']['gaps_pp']} holds {yn(v['of_readable']['holds'])}")
    p = pr["W10.17"]
    w(f"  W10.17 primary: {p['primary (kind enum, all 17)']}")
    w(f"         with map_enum: {p['other reading (enum and map_enum)']}")
    w(f"         certified-candidate enum only: {p['other reading (certified-candidate enum only)']}")
    for n, v in p["per_field"].items():
        a, b = v["first"], v["second"]
        w(f"         {n:24s} first {a['closed_list']:>2d} closed / {a['null']:>2d} null / "
          f"{a['off_list']} off;  second {b['closed_list']:>2d} / {b['null']:>2d} / "
          f"{b['off_list']}")
    p = pr["W10.18"]
    w(f"  W10.18   markers reading another file: {p['markers_reading_another_file']}; struck: "
      f"{p['struck_marks']} -> holds: {yn(p['holds'])}; re-run needed: {yn(p['rerun_needed'])}")
    w("")
    w("Consequences of the marking plan section 6, as written")
    for k, v in o["consequences"].items():
        w(f"  {k}: {v}")
    w("")
    w("The split (W14 section 3), twice-reworded fields: agree / n (pct of n; pct of readable)")
    for lab, s in o["split"].items():
        w(f"  {lab}: {s['n_read']} read reports {s['n_read_per_set']}")
        for n in TWICE_REWORDED:
            x = s[n]
            parts = []
            for k in ("all_96", "read", "unread"):
                y = x[k]
                parts.append(f"{k} {y['agree']}/{y['n']} ({y['pct_of_n']}%; "
                             f"{y['pct_of_readable']}%)")
            w(f"    {n:16s} " + "; ".join(parts)
              + f"; read-unread {x['read_minus_unread_pp_of_n']} pp "
                f"({x['read_minus_unread_pp_of_readable']} pp of readable)")
    w("  read reports, primary reading: "
      + ", ".join(o["read_reports"]["B_record_file_names_and_run_ids (primary)"]))
    w(f"  placeholders excluded: {o['read_reports_meta']['placeholders_excluded']}; named but "
      f"not among the 96: {o['read_reports_meta']['names_not_among_the_96']}")
    w("")
    a = o["audit"]
    w("The audit (W10.18)")
    w(f"  audited transcripts {a['markers_in_audit']} ({a['first_marker_rows']} first, "
      f"{a['second_marker_rows']} second), tools {a['tools']}, key hits {a['key_hits']}")
    w(f"  strikes list {a['audit_strikes_list']}; rows with other reads "
      f"{a['rows_with_other_reads']}")
    w(f"  rows off the common pattern: {a['rows_not_8_reads_7_skill_1_write_0_other']}")
    w(f"  M085 rerun: reads {a['M085_rerun'].get('reads')}, outside "
      f"{a['M085_rerun'].get('reads_outside')}, writes {a['M085_rerun'].get('writes')}")
    rc = o["returns_crosscheck (claimed, not seen)"]
    w(f"  markers' own files_read lists: {rc['returns_with_a_files_read_list']}; no result: "
      f"{rc['returns_with_no_result']}; skill files not in the list: "
      f"{rc['skill_files_not_in_files_read']}; outside the skill and own prompt: "
      f"{len(rc['files_read_outside_skill_and_own_prompt'])}")
    w("")
    rv = o["rival_checks"]
    w("Rival checks (they change no tick; they say what a tick can be read as)")
    w("  agreement by subgroup: rep+son = the 24 the criteria were tested on; rep31+son31 = "
      "same documents, never named")
    gs = list(next(iter(rv["agreement_by_subgroup"].values())).keys())
    w("  " + f"{'field':24s} " + "  ".join(f"{g.split(' (')[0]:>12s}" for g in gs))
    for n, row in rv["agreement_by_subgroup"].items():
        w("  " + f"{n:24s} " + "  ".join(f"{row[g]:>12s}" for g in gs))
    w(f"  rep+son agree more than rep31+son31 on: "
      f"{rv['fields_where_rep+son_agree_more_than_rep31+son31']}")
    w(f"  rep31+son31 agree more than rep+son on: "
      f"{rv['fields_where_rep31+son31_agree_more_than_rep+son']}")
    w(f"  placebo (fields not reworded twice), read-unread gap in pp, primary read set: "
      f"{rv['placebo_gap_pp_on_fields_not_reworded_twice (primary read set)']}")
    w(f"  placebo fields over 10 pp: {rv['placebo_fields_with_gap_over_10pp']}")
    w(f"  gap inside each set: {rv['gap_inside_each_set (primary read set)']}")
    for lab, v in rv["permutation_keeping_each_sets_share_of_read_reports"].items():
        w(f"  permutation, {lab}: " + "; ".join(
            f"{n} gap {x['observed_gap_pp']} pp, share of random read sets >= it "
            f"{x['share_of_random_read_sets_with_gap_at_least_as_large']}"
            for n, x in v.items()))
    w(f"  shape: {rv['shape_elements_disagreements_with_the_same_shape']}")
    w("  disagreement anatomy (map and set fields; see output.json for each report):")
    for n, v in rv["disagreement_anatomy"].items():
        w(f"    {n}: {v['tally']}")
    w("")
    w("Other readings and diagnostics (see README)")
    for k, v in o["other_readings"].items():
        w(f"  {k}:")
        w("    " + json.dumps(v, ensure_ascii=False))
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    main()
