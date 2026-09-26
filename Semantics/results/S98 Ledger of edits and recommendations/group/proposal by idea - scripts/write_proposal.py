# Writes "proposal by idea.md" and "proposal by idea - assignment.jsonl" from group_by_idea.run().
# Usage: PYTHONDONTWRITEBYTECODE=1 python3 write_proposal.py
import sys, os, json, collections, hashlib
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import group_by_idea as GB
GROUP = GB.GROUP

o1, p1, X1 = GB.run("v1"); m1 = GB.measure(o1, p1, X1)
o2, p2, X2 = GB.run("v2"); m2 = GB.measure(o2, p2, X2)
ORDER = ["frame", "organization", "question", "layers", "provenance", "surprise", "account", "work", "rivals", "ruling",
         "constructions", "argument", "criticism", "creativity", "appraisal", "physical", "recursion", "inputs", "ruleout", "form"]
NAME = {k: n for k, n, r, c in X2.IDEAS}; RULE = {k: r for k, n, r, c in X2.IDEAS}
NUMBER = {k: i + 1 for i, k in enumerate(ORDER)}
g1 = {o["change_id"]: o["group"] for o in o1}
def part_reach(out, part, grp):
    xs = [o for o in out if (o["first_part"] or "").strip() == part]
    return sum(1 for o in xs if o["group"] == grp), len(xs)
xv1, xvn = part_reach(o1, "Part XV", "ruleout"); xiv1, xivn = part_reach(o1, "Part XIV", "inputs")
noplace = collections.Counter(o["place"] for o in o2)
byweight = {k: g for k, g in m2["groups"].items() if k not in ("form", "ruleout", "inputs", "frame")}
lowest = min(byweight, key=lambda k: byweight[k]["mean_share"])
moved = [o for o in o2 if o["group"] != g1[o["change_id"]]]
md5 = lambda p: hashlib.md5(open(p, "rb").read()).hexdigest()

# ---- assignment jsonl
with open(os.path.join(GROUP, "proposal by idea - assignment.jsonl"), "w") as f:
    for o in o2:
        f.write(json.dumps({"change_id": o["change_id"], "group": o["group"], "group_name": NAME[o["group"]],
                            "also": o["also"], "near_tie": o["near_tie"], "rule": o["rule"], "shares": o["shares"],
                            "records": o["records"], "records_alone": {r: p2[r] for r in o["records"]},
                            "placed_by": o["placed_by"], "place": o["place"], "latest_sentences": o["latest_sentences"],
                            "parts": o["parts"], "statuses": o["statuses"], "kinds": o["kinds"]}, ensure_ascii=False) + "\n")

L = []
w = L.append
w("# S98 — a proposal for lumping the ledger: by idea")
w("")
w("*Log S98, 26 September 2026, under the owner's instruction of that day (decision S30). This is one proposal for the grouping step of the ledger. It reads the 1850 records of `anchored.jsonl` (1275 changes after the anchor step joined duplicates) and places each change in the idea of the semantics that its sentences carry, across Parts. Nothing in `anchored.jsonl`, `collect/` or any theory text was changed, and nothing was committed. The page and `proposal by idea - assignment.jsonl` were written by `proposal by idea - scripts/write_proposal.py`, from `group_by_idea.py`, `ideas.py` (the lens as first tried) and `ideas_v2.py` (the one adjustment).*")
w("")
w("## The metric")
w("")
w("A change goes to the idea its sentences carry. The idea of a sentence is read by program from two things: the words it uses that name an idea of the theory (the defined terms, tagged conditions and their near words, each weighted by how rare it is in the ledger's sentences and the latest text), and the heading or run-in label it stands under in the latest text. A change's sentences are its records' old and new sentences, its own old and new wording, and the latest-text sentences it is placed on, and the idea with the most weight over them is its group. Sizes below count changes; records are given beside them.")
w("")
w("## The groups")
w("")
w("The ideas follow the order in which the theory first takes them up. *Also* counts the changes of the group whose sentences give a second idea at least half the weight of the first; *where its changes stand* counts each change once, by the Part of its first latest-text sentence (or the Part its source names when it has none).")
w("")
w("| # | idea | rule | changes | records | also | where its changes stand |")
w("| --- | --- | --- | --- | --- | --- | --- |")
for k in ORDER:
    g = m2["groups"][k]
    w(f"| {NUMBER[k]} | **{NAME[k]}** (`{k}`) | {RULE[k]} | {g['changes']} | {g['records']} | {g['also']} | " +
      ", ".join(f"{p} {c}" for p, c in g["parts"][:5]) + (" …" if len(g["parts"]) > 5 else "") + " |")
w(f"| | **all** | | {m2['changes']} | {m2['records']} | {m2['also_changes']} | |")
w("")
w("## How a change that touches several places is placed")
w("")
w("Every change has one group. Its weight is summed over all its sentences: the mean idea profile of its records' sentences, plus the mean profile of the latest-text sentences it stands on (each carrying the idea of its heading or label), plus half the profile of its own old and new wording. A vocabulary entry (scope `term`) has no sentence of its own, so its own wording counts three times the weight of its places. The group is the idea with the most weight; every other idea with at least half that weight (and at least 0.15 of the whole) is listed in *also* in the assignment, so a reader of one idea can find the changes it shares with another. Two exceptions come first. A change all of whose sentences stand in a place that speaks of the other ideas as a whole (the front matter; Part 0, *What is imported, what is an index, and what is defined*; Part XIV; Part XV) goes to that place's idea, and the idea its words name goes to *also*. A change that alters only punctuation, emphasis, a pointer, a tag number or a label goes to *Form only*, with the idea of its sentence in *also*. A change with no place in the latest text uses the sentence named in `latest_nearest`, if any, and the idea of the Part its source names, at equal weight. The records of one change stay together; `records_alone` in the assignment file gives the group each record would take by itself.")
w("")
w("## How the lens was tried and adjusted once")
w("")
w("**First try (version 1).** Nineteen ideas, each with a list of words and a home among the headings and labels of the latest text (the examples in the task, with the Part 0 grievances, the Part I commitments and the numbered arguments of Part XVI sent to the idea each discusses). Measured on all 1275 changes:")
w("")
w(f"- changes with a second idea at half the weight of the first or more: {m1['also_changes']} ({m1['also_records']} records); near ties, a second idea at three quarters or more: {m1['near_tie_changes']};")
w(f"- changes whose first idea has under 0.30 of the weight: {m1['weak_changes']};")
w(f"- changes placed by their place alone, their wording naming no idea: {m1['placed_by'].get('its place only', 0)}; by nothing at all: {m1['placed_by'].get('nothing', 0)};")
w(f"- three faults a reader following the theory would meet. The words the theory now uses everywhere (\"argument\", \"rules out\", \"record\", \"contract\", \"declared\") pulled sentences about rivals, problems and prediction into *Arguments* and *Ruling out*. The old words the S95 scrub replaced (`true`, `established`, `fits`, `proves` …) stood in sentences of every idea, so a scrub edit went to *Ruling out* whatever its sentence said. The sentences that speak of the ideas as a whole (the dependence order of Part XIV, the cases of Part XV) were scattered over the ideas they name: only {xv1} of the {xvn} changes standing in Part XV reached *What would rule the class out*, and {xiv1} of the {xivn} in Part XIV reached *Imports, declared inputs and the dependence order*. Pointer and punctuation edits sat in whichever idea their sentence had, among edits of wording.")
w("")
w("**The adjustment (version 2), made once, in four parts** (`ideas_v2.py`):")
w("")
w("1. Each word's weight is scaled by how rare it is (the logarithm of the number of sentences over the number holding it, divided by the median, kept between 0.4 and 1.6). The first word of each idea, the one that names it, keeps at least its full weight.")
w("2. The list of old scrub words in *Ruling out* is narrowed to the ones about ruling out and holding a claim (`refute`, `reject`, `verdict`, `justification`, `certify`).")
w("3. The places that speak of the ideas as a whole carry their own idea with double weight, and a change standing only there goes to that idea.")
w("4. A twentieth group, *Form only*, takes the changes that alter no wording of an idea.")
w("")
w(f"Version 2 moved {len(moved)} changes. The largest moves: " + ", ".join(f"{a} → {b} {c}" for (a, b), c in collections.Counter((g1[o['change_id']], o['group']) for o in moved).most_common(8)) + ".")
w("")
w("| idea | v1 changes | v2 changes |")
w("| --- | --- | --- |")
for k in ORDER:
    w(f"| {NAME[k]} | {m1['groups'].get(k, {'changes': 0})['changes'] if k in m1['groups'] else 0} | {m2['groups'][k]['changes']} |")
w("")
w("## Measures of the final lens")
w("")
w(f"- **Groups:** 20. Sizes from {min(g['changes'] for g in m2['groups'].values())} to {max(g['changes'] for g in m2['groups'].values())} changes; the two middle sizes are {sorted(g['changes'] for g in m2['groups'].values())[9]} and {sorted(g['changes'] for g in m2['groups'].values())[10]}.")
w(f"- **In more than one group.** None by assignment: each change has one group. {m2['also_changes']} changes ({m2['also_records']} records) name a second idea in *also* at half the weight or more, and {m2['near_tie_changes']} are near ties (three quarters or more). The theory's sentences often carry two ideas at once (a conflict defined through (F1), (F2) and (A); an argument about kinds), and *also* keeps that visible.")
w(f"- **In no group.** None: every change is placed. {m2['placed_by'].get('its place only', 0)} changes have wording that names no idea and are placed by where they stand alone; {m2['placed_by'].get('its wording only', 0)} have no place and no Part (notes and whole-text changes) and are placed by their wording alone. {m2['weak_changes']} changes placed by weight give their first idea under 0.30 of the whole: these are the first to read when reviewing.")
w(f"- **Rules used:** " + ", ".join(f"{k} {v}" for k, v in m2["rule"].items()) + ".")
w(f"- **Changes of several records:** {m2['multi_record_changes']}. In {m2['split_changes']} of them the records, placed one by one, would go to more than one idea ({m2['split_records_off']} records would leave their change's group). The large chains the anchor step flagged cross ideas in this way:")
w("")
w("| change | records | group | the records placed alone |")
w("| --- | --- | --- | --- |")
d2 = {o["change_id"]: o for o in o2}
for c in ["CH-0152", "CH-1018", "CH-0244", "CH-0148", "CH-0997", "CH-0143", "CH-1131", "CH-0437"]:
    o = d2[c]
    w(f"| {c} | {len(o['records'])} | {o['group']} | " + ", ".join(f"{k} {v}" for k, v in collections.Counter(p2[r] for r in o["records"]).most_common()) + " |")
w("")
w("- **Does each group read as one part of the semantics?** Read by sampling changes of each group with their sentences (ten for most groups; all 77 of *Form only*). Groups that come out as one idea: *Organizations, roles and kinds*, *Questions, contracts and scope*, *Prediction, surprise and violation*, *What an account requires*, *Work, routes and commitments that do no work*, *Exact constructions*, *Creativity, understanding and origin*, *Aims, values and appraisal*, *Physical possibility*, *Recursion*, *Imports, declared inputs and the dependence order*, *What would rule the class out*, *Form only*. Groups with a seam: *Arguments, premises and tests* holds both what an argument is (Part IX) and scrub edits that put arguments into sentences about rivals and problems (24 changes stand in Part VI); *Ruling out and tentative acceptance* and *Rivals, conflict and problems* share the sentences of Part VI that define each through the other, which is where most near ties fall; " + f"*{NAME[lowest]}* has the lowest mean weight share of the groups placed by weight ({byweight[lowest]['mean_share']:.2f}), because its sentences also speak of layers, transports and construction. A few strays sit in each group, most often scrub vocabulary entries whose new words name one idea while their places stand in another.")
w("")
w("## Strengths")
w("")
w("- It follows what a sentence says, not where it stands: a grievance in Part 0, a commitment in Part I, the numbered arguments of Part XVI and the dependence order's sentences each join the idea they discuss, so a reader of one idea sees every change to it across the text in one place.")
w("- It is made by program from the sentences only, with no use of the reasons in the sources, and every choice leaves its weights in the assignment file (`shares`, `also`, `near_tie`, `rule`), so any placement can be reread and moved by hand.")
w("- The records that never reached a text (collector A's proposals against file 20, notes) still get an idea from their own wording, where a grouping by place has only the Part their source names.")
w("- *Form only* keeps 77 pointer, punctuation and label edits out of the idea groups, and *also* shows where one sentence carries two ideas instead of hiding it.")
w("")
w("## Weaknesses")
w("")
w("- The word lists are Claude's reading of the theory's vocabulary; a different reader would draw some lines elsewhere, most of all between *Ruling out*, *Arguments* and *Rivals*, whose sentences in Part VI define each idea through the others.")
w(f"- Many changes carry two ideas ({m2['also_changes']} have a second at half weight or more), so a one-group assignment hides part of what they touch unless *also* is read.")
w("- A change is placed as a whole. Where the anchor step joined a chain of restatements (CH-0152, CH-1018, CH-1131), its records sit in one idea although, read alone, they spread over several; these chains would be split before the line-up.")
w(f"- Changes with no place in the latest text ({noplace['nearest sentence and Part named'] + noplace['Part named'] + noplace['none']}: {noplace['nearest sentence and Part named']} with a nearest sentence, {noplace['Part named']} with only the Part their source names, {noplace['none']} with neither) are placed by their own wording and a Part, and are the least sure; " + str(sum(1 for o in o2 if not o["latest_sentences"] and o["records"][0].startswith("A-"))) + " of them are collector A's, most of these proposals against file 20. Some requirements on an account written with the word *question* went to *Questions* rather than *What an account requires*.")
w("- The exceptions for Part XIV and Part XV make those two groups mostly Part-shaped; a reader who wants a Part XV case under the idea it tests must use *also*.")
w("")
w("## Files and rerun")
w("")
w("- `proposal by idea - assignment.jsonl`: one line per change: `change_id`, `group`, `group_name`, `also`, `near_tie`, `rule`, `shares` (the four heaviest ideas and their shares), `records`, `records_alone`, `placed_by`, `place`, `latest_sentences`, `parts`, `statuses`, `kinds`.")
w("- `proposal by idea - scripts/`: `ideas.py` (the lexicon and the homes), `ideas_v2.py` (the adjustment), `group_by_idea.py` (the placing and the measures), `write_proposal.py` (this page).")
w("- Rerun: `PYTHONDONTWRITEBYTECODE=1 python3 write_proposal.py` in the scripts folder; the output is the same bytes.")
w(f"- Inputs read: `anchored.jsonl` md5 {md5(os.path.join(GROUP, 'anchored.jsonl'))}; `sentence index of the latest text.jsonl` md5 {md5(os.path.join(GROUP, 'sentence index of the latest text.jsonl'))}.")
w("")
w("## The assignment: change → group")
w("")
w("In change order. *Idea* is the group's number and key from the table above; *also* lists the second ideas; *sentences* gives up to three latest-text sentences the change stands on (`—` when it has none; then *Part* is the one its source names).")
w("")
w("| change | idea | also | records | Part | sentences |")
w("| --- | --- | --- | --- | --- | --- |")
for o in o2:
    ls = o["latest_sentences"]
    sent = (", ".join(ls[:3]) + (f" +{len(ls) - 3}" if len(ls) > 3 else "")) if ls else "—"
    parts = ", ".join(o["parts"][:2]) + (" …" if len(o["parts"]) > 2 else "") if o["parts"] else "—"
    w(f"| {o['change_id']} | {NUMBER[o['group']]} `{o['group']}` | {', '.join(o['also']) or '—'} | {' '.join(o['records'])} | {parts} | {sent} |")
w("")
open(os.path.join(GROUP, "proposal by idea.md"), "w").write("\n".join(L))
print("written", len(L), "lines")
