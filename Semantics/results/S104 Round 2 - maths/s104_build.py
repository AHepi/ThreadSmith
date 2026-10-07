# S104 round 2 (maths): builds the inventions register and the formal claims (.md and .json)
# from s104_inventions.py and s104_claims.py, after checking every quotation against the text
# under review (md5 checked in s104_check.py). Run: python3 s104_build.py
import json, os, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from s104_check import check, MD5, check_markdown  # noqa: E402
from s104_inventions import INVENTIONS  # noqa: E402
from s104_claims import CLAIMS, STRONG, NOT_FORMALIZED  # noqa: E402

TEXT_NAME = "tests/103 The semantics, standing alone, after round 1.md"
DATE = "27 September 2026"

# ---- checks -------------------------------------------------------------------------------
errors = []
inv_ids = [i["id"] for i in INVENTIONS]
fc_ids = [c["id"] for c in CLAIMS]
if len(set(inv_ids)) != len(inv_ids):
    errors.append("duplicate invention id")
if len(set(fc_ids)) != len(fc_ids):
    errors.append("duplicate claim id")
for i in INVENTIONS:
    for l, q in i["quotes"]:
        m = check(l, q)
        if m:
            errors.append("%s %s" % (i["id"], m))
for c in CLAIMS:
    for l, q in c["quotes"]:
        m = check(l, q)
        if m:
            errors.append("%s %s" % (c["id"], m))
    for x in c["inventions"]:
        if x not in inv_ids:
            errors.append("%s names unknown invention %s" % (c["id"], x))
for n in NOT_FORMALIZED:
    m = check(n[1], n[2])
    if m:
        errors.append("%s %s" % (n[0], m))
for s in STRONG:
    for f in s[4]:
        if f not in fc_ids:
            errors.append("%s names unknown claim %s" % (s[0], f))
if len(STRONG) != 36:
    errors.append("strong candidates: %d, expected 36" % len(STRONG))
if errors:
    print("\n".join(errors))
    sys.exit("stopped: %d errors" % len(errors))

# invention -> sections of the formal core that mark it (read from formal core.md)
import re as _re
_marked, _sec = {}, None
for _row in open(os.path.join(HERE, "formal core.md"), encoding="utf-8").read().split("\n"):
    _m = _re.match(r"^## (§\d+)", _row)
    if _m:
        _sec = _m.group(1)
    for _grp in _re.findall(r"\[(I\d\d(?:, I\d\d)*)\]", _row):
        for _i in _grp.split(", "):
            _marked.setdefault(_i, [])
            if _sec not in _marked[_i]:
                _marked[_i].append(_sec)
for i in INVENTIONS:
    if i["id"] in _marked:
        i["core"] = sorted(_marked[i["id"]], key=lambda x: int(x[1:]))
    else:
        errors.append("%s is marked nowhere in formal core.md" % i["id"])
for _i in _marked:
    if _i not in inv_ids:
        errors.append("formal core.md marks unregistered %s" % _i)
if errors:
    print("\n".join(errors))
    sys.exit("stopped: %d errors" % len(errors))

# invention -> claims that use it (read from the claims, so the two cannot drift apart)
uses = OrderedDict((i, []) for i in inv_ids)
for c in CLAIMS:
    for x in c["inventions"]:
        uses[x].append(c["id"])
unused = [i for i, v in uses.items() if not v]


def q_md(l, q):
    return "> L%d | %s" % (l, q)


# ---- inventions register ------------------------------------------------------------------
inv_json = OrderedDict()
inv_json["about"] = OrderedDict([
    ("log", "S104"), ("round", "review round 2 (maths)"), ("date", DATE), ("decision", "S36"),
    ("text_under_review", TEXT_NAME), ("md5", MD5),
    ("rule", "if implementation forces invention, that needs to be recorded (decision S36)"),
    ("note", "Every entry is a choice the text leaves open. Nothing here is the text's own content. "
             "Results: none yet; this register is written before any test, and every future result on a listed claim depends on the listed inventions."),
])
inv_json["inventions"] = []
for i in INVENTIONS:
    inv_json["inventions"].append(OrderedDict([
        ("id", i["id"]), ("title", i["title"]),
        ("fills_in_for", [OrderedDict([("line", l), ("quote", q)]) for l, q in i["quotes"]]),
        ("invented", i["invented"]), ("other_choices", i["others"]),
        ("formal_core_sections", i["core"]), ("claims", uses[i["id"]]), ("results", []),
    ]))
json.dump(inv_json, open(os.path.join(HERE, "inventions register.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

L = []
L.append("# S104 Round 2 — inventions register")
L.append("")
L.append("*Log S104, review round 2 (the maths round), %s. Decision S36: \"Also, if implementation forces invention, that needs to be recorded.\" The text under review is `%s`, md5 %s (checked by `s104_check.py` before every build; not written to). Built by `s104_build.py` from `s104_inventions.py`; the claims each invention is used by are read from `s104_claims.py`, so the two lists cannot drift apart. Every quotation below was compared by program with the line it names.*" % (DATE, TEXT_NAME, MD5))
L.append("")
L.append("**What this is.** Every choice the formal core or the claims make that the text does not fix: a missing definition, a default, a domain, a choice between two readings of a sentence, a finite bound, an encoding. Each entry quotes the sentence it fills in for, says what was invented and what else could have been chosen, and names the sections of `formal core.md` and the claims of `formal claims.md` that use it. Nothing invented is the text's own content, and no entry is offered as what the text means; each is the choice this formalization made so that the text could be written as mathematics, open to replacement.")
L.append("")
L.append("**Results.** None yet. This register is written before any test or program is run. Every result later reported on a claim depends on the inventions that claim lists, and says so.")
L.append("")
L.append("**Counts.** %d inventions; %d claims; %d of the inventions are used by at least one claim%s." % (
    len(INVENTIONS), len(CLAIMS), len(INVENTIONS) - len(unused),
    "" if not unused else " (not used by a claim: %s; used by the formal core only)" % ", ".join(unused)))
L.append("")
L.append("## Index")
L.append("")
L.append("| id | invention | lines | claims that use it |")
L.append("| --- | --- | --- | --- |")
for i in INVENTIONS:
    lines = ", ".join("L%d" % l for l in OrderedDict((l, 1) for l, _ in i["quotes"]))
    L.append("| %s | %s | %s | %s |" % (i["id"], i["title"], lines, ", ".join(uses[i["id"]]) or "—"))
L.append("")
L.append("## The entries")
for i in INVENTIONS:
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
    L.append("**Used by.** Formal core %s. Claims: %s." % (", ".join(i["core"]), ", ".join(uses[i["id"]]) or "none"))
    L.append("")
    L.append("**Results that depend on it.** None yet.")
open(os.path.join(HERE, "inventions register.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")

# ---- formal claims ------------------------------------------------------------------------
cl_json = OrderedDict()
cl_json["about"] = OrderedDict([
    ("log", "S104"), ("round", "review round 2 (maths)"), ("date", DATE), ("decision", "S36"),
    ("text_under_review", TEXT_NAME), ("md5", MD5),
    ("types", ["definition-consequence", "stated result", "strong candidate"]),
    ("note", "Each claim is to be tested; none is tested here. 'look' is a first reading of where a counterexample might lie, not a result. "
             "Every claim that uses an invention lists it; a result on that claim depends on it."),
])
cl_json["claims"] = []
for c in CLAIMS:
    cl_json["claims"].append(OrderedDict([
        ("id", c["id"]), ("title", c["title"]),
        ("source", [OrderedDict([("line", l), ("quote", q)]) for l, q in c["quotes"]]),
        ("formal", c["formal"]), ("type", c["type"]), ("s100_units", c["s100"]),
        ("round1", c["round1"]), ("inventions", c["inventions"]), ("formal_core_sections", c["core"]),
        ("look", c["look"]), ("results", []),
    ]))
cl_json["strong_candidates"] = [OrderedDict([("unit", s[0]), ("line", s[1]), ("before_round_1", s[2]), ("status", s[3]), ("claims", s[4]), ("why", s[5])]) for s in STRONG]
cl_json["not_formalized"] = [OrderedDict([("id", n[0]), ("line", n[1]), ("quote", n[2]), ("why", n[3])]) for n in NOT_FORMALIZED]
json.dump(cl_json, open(os.path.join(HERE, "formal claims.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

count = lambda t: sum(1 for c in CLAIMS if t in c["type"])
with_inv = sum(1 for c in CLAIMS if c["inventions"])
status_counts = OrderedDict()
for s in STRONG:
    status_counts[s[3]] = status_counts.get(s[3], 0) + 1

G = [("A", "Organizations, roles, families, kinds", "FC01", "FC14"),
     ("B", "Questions, transports, fidelity, account", "FC15", "FC36"),
     ("C", "Part VI: routes, conflict, rivals, problems", "FC37", "FC56"),
     ("D", "Parts VII and VIII: exact constructions and transport results", "FC57", "FC68"),
     ("E", "Part IX: arguments, usability, bearing, reason use, active routes", "FC69", "FC76"),
     ("F", "Parts IV and X–XIII: provenance, prediction, construction, repair, the physical module", "FC77", "FC95"),
     ("G", "Arguments 2 and 5–10, the dependence order, and matters from round 1", "FC96", "FC110")]

M = []
M.append("# S104 Round 2 — formal claims")
M.append("")
M.append("*Log S104, review round 2 (the maths round), %s, under decision S36 (\"maybe exploring the math a bit more might help instead of words. Since words are vague\"). The text under review is `%s`, md5 %s (checked before every build; not written to). Built by `s104_build.py` from `s104_claims.py`; every quotation was compared by program with the line it names. The notation is fixed in `formal core.md` §0; the inventions are in `inventions register.md`.*" % (DATE, TEXT_NAME, MD5))
M.append("")
M.append("**What this is.** Each claim the formal core lets one state and test: its source sentences quoted, its formal statement, and its type — a *definition-consequence* (it follows from the definitions as formalized), a *stated result* (one of Arguments 1–10, or a sentence of the text that says something follows, entails or is so), or a *strong candidate* of S100 (the 36 sentences that stood longest). Every claim lists the inventions it uses; any result on it depends on them, and a counterexample that rests on an invention is a counterexample to this formalization, not to the text. No claim is tested here. Where a line under *Look* says where a counterexample might lie, that is a first reading, not a result. Nothing is settled (S28).")
M.append("")
M.append("**Counts.** %d claims: %d definition-consequences, %d stated results, %d strong-candidate claims (types overlap: a claim can be more than one). %d claims use at least one invention. %d claims of the text are recorded as not formalized (below). Of the 36 strong candidates: %s." % (
    len(CLAIMS), count(DC := "definition-consequence"), count("stated result"), count("strong candidate"), with_inv, len(NOT_FORMALIZED),
    "; ".join("%d %s" % (v, k) for k, v in status_counts.items())))
M.append("")
M.append("**The owner's decisions kept.** No claim lists, counts, grades or records rivals (S20); none says what must happen (S21); the prose here uses no word S23 scrubs; physical possibility enters only in §§12–16 of the formal core, where a content is held, built or carried out, and as the content of a claim a candidate can conflict with (S25–S27); nothing is settled, and a ruling out is a choice (S28). What hard to vary covers is parked (S33–S34): the only related claims are about the text's own 'easy to vary' at L317 (FC43), and they add nothing about what hard to vary covers. The appraisal relation appears only as a typed input (NF16, NF19); where values are placed is the owner's question.")
M.append("")
M.append("## Index")
M.append("")
M.append("| id | claim | type | lines | inventions |")
M.append("| --- | --- | --- | --- | --- |")
for c in CLAIMS:
    lines = ", ".join("L%d" % l for l in OrderedDict((l, 1) for l, _ in c["quotes"]))
    M.append("| %s | %s | %s | %s | %s |" % (c["id"], c["title"], "; ".join(c["type"]), lines, ", ".join(c["inventions"]) or "—"))
for gid, gname, a, b in G:
    M.append("")
    M.append("## %s. %s" % (gid, gname))
    on = False
    for c in CLAIMS:
        if c["id"] == a:
            on = True
        if not on:
            continue
        M.append("")
        M.append("### %s · %s" % (c["id"], c["title"]))
        M.append("")
        for l, q in c["quotes"]:
            M.append(q_md(l, q))
            M.append("")
        M.append("**Formal.** %s" % c["formal"])
        M.append("")
        M.append("**Type.** %s.%s%s" % ("; ".join(c["type"]),
                                        (" S100 unit%s: %s." % ("s" if len(c["s100"]) > 1 else "", ", ".join(c["s100"]))) if c["s100"] else "",
                                        (" Round 1: %s." % "; ".join(c["round1"])) if c["round1"] else ""))
        M.append("")
        M.append("**Uses.** Inventions: %s. Formal core %s." % (", ".join(c["inventions"]) or "none", ", ".join(c["core"])))
        if c["look"]:
            M.append("")
            M.append("**Look.** %s" % c["look"])
        if c["id"] == b:
            break
M.append("")
M.append("## The 36 strong candidates of S100, and how far each is formal")
M.append("")
M.append("Line numbers are those of file 103, which file 99 shares (round 1 changed four lines one for one). A display unit is given by the line that holds its formula. 'Tested' are the seven challenged and kept before round 1; 'never challenged' are the twenty-nine round 1 put to the readers. This table records how far each sentence can be written as mathematics; it grades nothing (S20).")
M.append("")
M.append("| unit | line | before round 1 | status | claims | why |")
M.append("| --- | --- | --- | --- | --- | --- |")
for s in STRONG:
    M.append("| %s | L%d | %s | %s | %s | %s |" % (s[0], s[1], s[2], s[3], ", ".join(s[4]) or "—", s[5]))
M.append("")
M.append("## Claims of the text not formalized, and why")
M.append("")
for n in NOT_FORMALIZED:
    M.append("### %s · L%d" % (n[0], n[1]))
    M.append("")
    M.append(q_md(n[1], n[2]))
    M.append("")
    M.append("**Why not.** %s" % n[3])
    M.append("")
M.append("## The four round-1 changes and the matters round 1 left for this round, where each is taken up")
M.append("")
r1 = OrderedDict()
for c in CLAIMS:
    for r in c["round1"]:
        r1.setdefault(r, []).append(c["id"])
for k in sorted(r1, key=lambda s: (0 if s.startswith("round-1 change") else 1 if s.startswith("matter") else 2, s)):
    M.append("- %s: %s" % (k[0].upper() + k[1:], ", ".join(r1[k])))
open(os.path.join(HERE, "formal claims.md"), "w", encoding="utf-8").write("\n".join(M) + "\n")

# ---- final check of every quotation in the .md files of this folder -------------------------
tot, bad = 0, []
for name in sorted(os.listdir(HERE)):
    if name.endswith(".md"):
        n, b = check_markdown(os.path.join(HERE, name))
        tot += n
        bad += b
print("inventions: %d (unused by claims: %s)" % (len(INVENTIONS), ", ".join(unused) or "none"))
print("claims: %d (definition-consequence %d, stated result %d, strong candidate %d; with inventions %d)" % (
    len(CLAIMS), count("definition-consequence"), count("stated result"), count("strong candidate"), with_inv))
print("strong candidates:", dict(status_counts))
print("not formalized: %d" % len(NOT_FORMALIZED))
print("quotations in .md files: %d checked, %d not found" % (tot, len(bad)))
for b in bad:
    print("  BAD", b)
