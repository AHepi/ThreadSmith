"""The arms of W10 section 4, and the context each call of each arm is handed.

A RULE. Both drivers (run_deepseek.py, sonnet_prompts.py) build every call from here, so that
the only thing that differs between two arms is the thing W3 section 5 says differs.

The arms (W3 section 5, with W8's three changes and W10's new arm):
  a      one reader carrying its own history through every step
  b      fresh calls, one per step, each handed the whole transcript so far
  c      fresh calls, one per step, each handed a summary written by a fixed program
  cctl   arm (c) with an equal-length summary that omits the parts list  (W8 section 4's control)
  cprime arm (c'), each call handed a carry-over note the previous call wrote
  d      the partition harness: one call per test of Step 5, the parts split across calls
         (W8 part B12), and a final call handed the pile of answers
  e      the port-setting harness: the emission prefilled as a report skeleton whose marks come
         from a closed list  (DeepSeek beta prefix completion; on Sonnet a control, W10 s.10)
  f      arm (a) with the change list withheld from the context
  r      arm (a) with a criticism of the method's router table in its context before the run
  x      arm (a) on the same document with two names exchanged throughout  (W10 section 4)
  k      optional, on the owner's word: arm (a) under a copy of file 33 with the router table's
         rows removed  (W8 P4.8).  The copy on disk is never edited: the rows are removed in
         memory and the removed lines are written into the run record.

The router is live in every arm. That is a decision of this rig, and its reason: if the seven
reference files were behind a tool in arm (a) and not in arm (b), a difference between the arms
would be a difference in what was reachable, not in what was carried. What it costs: no arm here
reproduces the record's mode 1 (the whole skill in the context), so no run of this round is
comparable with those runs on that count.
"""
import os, re
from rig import MODULES, FIXTURES
from steps import STEP_ORDER, STEP_TITLE, STEP_TASK, TEST_BY_ID
import carryover

ARMS = {
  "a":      dict(carrier="own",             title="one reader carrying its own history"),
  "b":      dict(carrier="transcript",      title="fresh calls, the whole transcript so far"),
  "c":      dict(carrier="summary",         title="fresh calls, a summary by a fixed program"),
  "cctl":   dict(carrier="summary_control", title="arm (c)'s control: an equal-length summary with no parts list"),
  "cprime": dict(carrier="carryover",       title="fresh calls, the carry-over note the last call wrote"),
  "d":      dict(carrier="none",  partition=True, title="the partition harness, parts split across calls"),
  "e":      dict(carrier="own",   prefix=True,    title="the port-setting harness, the emission prefilled"),
  "f":      dict(carrier="own",   question="no_change_list", title="the change list withheld from the context"),
  "r":      dict(carrier="own",   insert="router_criticism", title="a criticism of the router table in the context"),
  "x":      dict(carrier="own",   document="exchanged",      title="two names exchanged throughout"),
  "k":      dict(carrier="own",   skill_variant="no_router_table", optional=True,
                 title="optional: file 33 with the router table's rows removed"),
}
for _a in ARMS.values():
    _a.setdefault("partition", False); _a.setdefault("prefix", False)
    _a.setdefault("question", "full"); _a.setdefault("document", "plain")
    _a.setdefault("insert", None); _a.setdefault("skill_variant", None); _a.setdefault("optional", False)

ARM_IDS = list(ARMS)

FRAMING = (
  "Below is a method for judging whether an explanation holds up. It is the tool. The document "
  "handed to you is the thing to judge. You will be asked for one part of the method's procedure "
  "at a time, or for the whole of it where the instruction says so; do the part you are asked for "
  "and no other. Use everyday words and concrete changes. Where the method refers to a source "
  "theory that is not supplied, work from the method's own words.\n\n")

ROUTER_API = (
  "The method's reference files are not in front of you. You open one by calling the tool "
  "open_module with its name, when the method's own table and map say to open it, and only then.\n\n")

ROUTER_SONNET = (
  "You are a reader under test. This file is your whole instruction. The method below names "
  "reference files; they are in the folder {refs} as <name>.md, and you open one with the Read "
  "tool when the method's own table and map say to open it, and only then. Use no other tool "
  "except Write, once, to save your answer at the output path named at the end of this file. "
  "Read no file outside that folder, run nothing, search nothing. Your working directory is "
  "irrelevant.\n\n")

TOOL = [{"type": "function", "function": {
    "name": "open_module",
    "description": ("Open one of this method's reference files and return its text. "
                    "The method's own table and map say which file to open and when."),
    "parameters": {"type": "object", "properties": {
        "name": {"type": "string", "enum": MODULES,
                 "description": "the reference file to open, without the .md"}},
        "required": ["name"]}}}]


def fixture(name):
    with open(os.path.join(FIXTURES, name), encoding="utf-8") as f:
        return f.read()


# Arm (k), P4.8 (fault 16 of the stage-A review). Removing the router table's rows alone leaves
# the mermaid graph, which does the same routing: under the skill's own marks the table and the
# graph are two routes to one job, and removing one of two routes tests nothing. The sentences
# below name the table, the graph or a row; left standing they both point at the removed rows
# and give the reader the routing back in words. The list is closed: a sentence this rig expects
# and does not find stops the run, so a later edit of file 33 cannot leave one in silently.
ROUTER_SENTENCES = [
    "Open one only when its row applies.",
    "When a module is added, split or changed, update the table and the graph in the same edit.",
    "A module with no row is unreachable: give it a row or remove it.",
    "Every module has a row there and a node in the graph.",
]


def skill_variant(skill_md, kind):
    """Arm (k), P4.8: the router table's rows, the mermaid graph that does the same routing,
    and the sentences that name them, removed in memory. Returns (text, removed), where
    removed is {"table_rows": [...], "graph_lines": [...], "sentences": [...]}."""
    if not kind:
        return skill_md, {"table_rows": [], "graph_lines": [], "sentences": []}
    if kind != "no_router_table":
        raise SystemExit(f"unknown skill variant {kind!r}")
    out, rows, graph, inside, in_graph = [], [], [], False, False
    for line in skill_md.split("\n"):
        if line.startswith("## "):
            inside = line.strip().lower().startswith("## where to look")
            in_graph = False
        fence = inside and line.strip().startswith("```")
        if inside and (in_graph or fence):
            graph.append(line)
            if fence:
                in_graph = not in_graph
            continue
        if inside and line.lstrip().startswith("|"):
            rows.append(line)
            continue
        out.append(line)
    missing = [s for s in ROUTER_SENTENCES if s not in "\n".join(out)]
    if missing:
        raise SystemExit(f"arm (k): SKILL.md does not contain the sentence(s) {missing} this "
                         f"variant removes; the edit is not the one P4.8 names. Nothing sent.")
    kept, gone = [], []
    for line in out:
        new = line
        for s in ROUTER_SENTENCES:
            if s in new:
                new = new.replace(s, "")
                gone.append(s)
        if new == line:
            kept.append(line)
            continue
        new = re.sub(r"[ \t]{2,}", " ", new).strip()
        # only a line a sentence was cut from is collapsed, and only when nothing of it is left
        if not new or re.fullmatch(r"\*\*[^*]+\*\*[.:]?", new):
            gone.append(line.strip())
            continue
        kept.append(new)
    text = "\n".join(kept)
    if not rows:
        raise SystemExit("arm (k): no router table rows found in SKILL.md; the variant would change nothing.")
    if not graph:
        raise SystemExit("arm (k): no router graph found in SKILL.md; the variant would leave the "
                         "second route to the same job. Nothing sent.")
    return text, {"table_rows": rows, "graph_lines": graph, "sentences": gone}


def steps_for(arm, transport):
    """The ordered step ids of one run. Arm (d)'s test calls are added at run time, once the
    parts pass has written the parts; see partition.py."""
    a = ARMS[arm]
    if a["partition"]:
        return ["S1234"]
    if a["carrier"] == "own":
        return ["ALL"] if transport == "sonnet" else list(STEP_ORDER)
    return list(STEP_ORDER)


def system_message(arm, transport, skill_md, refs_dir=None):
    a = ARMS[arm]
    head = ROUTER_SONNET.format(refs=refs_dir or "<refs>") if transport == "sonnet" else ROUTER_API
    body = head + FRAMING + f"=== FILE: hard-to-vary/SKILL.md ===\n{skill_md.strip()}\n"
    if a["insert"]:
        body += "\n\n" + fixture(a["insert"] + ".md").strip() + "\n"
    return body


def _carrier_block(carrier, text):
    if not text:
        return ""
    head = {"transcript": "=== EVERYTHING WRITTEN SO FAR (the whole transcript) ===",
            "summary": "=== A SUMMARY OF THE WORK SO FAR, WRITTEN BY A PROGRAM ===",
            "summary_control": "=== A SUMMARY OF THE WORK SO FAR, WRITTEN BY A PROGRAM ===",
            "carryover": "=== THE NOTE THE LAST READER LEFT YOU ==="}[carrier]
    return f"{head}\n{text.strip()}\n=== END ===\n\n"


# W11 decision D1 (fault 9 of the stage-A review): the assembling call of the partition arm is
# handed the frozen question, its step and the pile of answers, and no document block. W3
# section 5 gives the assembler "the pile of answers to write the report"; W8 B12's ground is
# that "A final call handed a pile of answers assesses no support that any call wrote". With the
# document in front of it the assembler could assess the whole candidate in one context, and
# arm (d) matching arm (a) on the cross-step fields would then falsify P4.3 for a reason that is
# the rig's. What this gives up, as D1 records it: an assembler that can check a quotation
# against the text, so an arm (d) report's quotations are the test calls' quotations, and a
# marker who finds a misquotation in an arm (d) report attributes it to the call that wrote it.
NO_DOCUMENT_STEPS = {"SASM"}


def user_message(arm, step, doc_text, question_block, carrier_text=None,
                 test=None, group_text=None, pile_text=None, skeleton=None):
    """The user turn of one call. The order is fixed for every arm: what is carried in,
    then the frozen question, then the document, then the step's task. The assembling step
    SASM is handed no document block (W11 D1)."""
    a = ARMS[arm]
    out = ""
    if a["carrier"] in ("transcript", "summary", "summary_control", "carryover"):
        out += _carrier_block(a["carrier"], carrier_text)
    out += question_block + "\n\n"
    if step not in NO_DOCUMENT_STEPS:
        out += f"=== THE DOCUMENT TO JUDGE ===\n\n{doc_text}\n\n=== END OF DOCUMENT ===\n\n"
    if step == "SONE":
        t = TEST_BY_ID[test]
        out += (f"=== YOUR STEP ===\n{STEP_TITLE['SONE']}\n\n"
                f"The one test: {t[1]}. {t[2]}\n\n"
                f"The parts it is to be run on, and no others:\n{group_text}\n\n"
                "Run that one test on those parts. Do not run any other test. Do not mark any part. "
                "Do not write a report. Say what you did and what happened.\n")
    elif step == "SASM":
        out += (f"=== YOUR STEP ===\n{STEP_TITLE['SASM']}\n\n{STEP_TASK['SASM']}\n\n"
                f"=== THE ANSWERS ===\n{pile_text}\n=== END OF THE ANSWERS ===\n")
    else:
        out += f"=== YOUR STEP ===\n{STEP_TITLE[step]}\n\n{STEP_TASK[step]}\n"
    if a["carrier"] == "carryover" and step != "S67":
        out += carryover.ASK
    if skeleton:
        out += ("\n\nUse this shape for your report, and these marks and no others:\n\n"
                + skeleton.strip() + "\n")
    return out

