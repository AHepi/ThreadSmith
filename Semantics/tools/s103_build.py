#!/usr/bin/env python3
"""s103_build.py: build round 1 of the review rounds of decision S35 (log S103): the outside readers try to vary the 29
strong candidates that no proposal has yet touched on their own (S100, section 3.2, "never challenged"), in the
stand-alone copy of the theory (tests/99, md5 74f4a4c7619345747f4fa976ddac9548). Written 27 September 2026 by a Claude
subagent for the orchestrator, on the model of tools/s96_build.py.

  python3 Semantics/tools/s103_build.py           build the three briefs and the two job lists; refuses to overwrite a
                                                  file whose content differs; prints the tables for the reading rule
  python3 Semantics/tools/s103_build.py --check   rebuild in memory and compare with the files; writes nothing

What it does, by program:
  1. Takes the 29 units whose strong_candidate_list is "never challenged" from the S100 data (their ids are those of
     the S98 sentence index of the latest text) and numbers them C01 to C29 in the order of the text.
  2. Maps each to the stand-alone copy: the unit's text, from the sentence index, must stand word for word on the same
     line (or lines, for a display) of file 99, and nowhere else in it; the result is printed, with the lines on which
     file 99 differs from the latest text.
  3. Proposes the defined terms each candidate uses by scanning its wording with the word patterns of the S101 graph's
     nodes (NODES in the S101 script, read with ast, not run), and requires that every node so proposed is either given
     (a DEFS entry names it, and one of its excerpts covers a line that holds one of that node's defining sentences in
     the S101 graph) or set aside in SCAN_ASIDE with the reason. DEFS, read from the text, adds what the scan does not
     find.
  4. Builds three parts, grouped by where the candidates stand: part 1, Parts 0 and II (C01-C12); part 2, Parts III and
     IV (C13-C20); part 3, Parts V to XIV (C21-C29). The same three parts go to both readers.
Each part carries: what the reader is asked to do; the owner's words of decisions S20, S21, S23, S25 to S28, S33 and
S34 (every quoted word unchanged; the connecting words outside the quotation marks the recorder's, with internal record
labels replaced by plain descriptions, REPLACE below); the candidates, each with the lines around it; the lines and
excerpts that give the definitions they use, each once, in text order; the task; and the report form, ending "END OF
REPORT". Withheld: the record's readings of the decisions, every result about the candidates (S100, S101, S102), the
decisions on how the work is run (S22, S24, S29 to S32, S35), every model name, and the books.
Sources are compared by md5 before anything is built. Every line given is compared with its line of file 99, every
excerpt with a run of its line. The frame of every brief (all but the owner's words and the lines of the text) is
scanned for the words decision S23 forbids and words near them; the build refuses on any hit outside the phrases
ALLOWED_IN_FRAME, and on any part over CAP words.
"""
import ast, csv, hashlib, json, os, re, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
SEM = os.path.dirname(HERE)
TESTS = os.path.join(SEM, "tests")
OUT_DIR = os.path.join(SEM, "results", "S103 Round 1 - returns")
JOBS_MIMO = os.path.join(HERE, "s103_jobs - round 1, Mimo.json")
JOBS_GLM = os.path.join(HERE, "s103_jobs - round 1, GLM.json")
READING_RULE = "results/S103 Round 1 - how the replies will be read, written before sending.md"
CAP = 9000   # words per brief, by the runner's count (the orchestrator's "at most about 9,000")

SRC = {
    "text": ("tests/99 The semantics, standing alone.md", "74f4a4c7619345747f4fa976ddac9548"),
    "latest": ("tests/Revision 2 - scrubbed copy, repaired (S96), after cross-examination, theory text.md",
               "ebca15a047f686b15d5f5766b69825c9"),
    "decisions": ("records/Semantics - Decisions.md", "71459192867b1ebcf1bae914c9297129"),
    "s100": ("results/S100 Strong candidates and the most altered sections - data.csv",
             "aafca7e15b1515e58161da95227ac354"),
    "index": ("results/S98 Ledger of edits and recommendations/group/sentence index of the latest text.jsonl",
              "fdaf069a0c1d71be4e17b38d2f6bce82"),
    "graph": ("results/S101 What the tested strong candidates depend on - graph.json",
              "ceb857cb76ebed0d464b1724398f2fe2"),
    "s101": ("results/S101 What the tested strong candidates depend on - script.py",
             "63c67c799745f978728c8c78ee4c6ae1"),
}


def read(rel):
    with open(os.path.join(SEM, rel), encoding="utf-8") as f:
        return f.read()


def md5(s):
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def need(ok, msg):
    if not ok:
        raise SystemExit("s103_build: " + msg)


def wc_words(s):
    """Runs of bytes that are not ASCII whitespace (the runner's count). The GNU wc -w of this machine counts a few
    fewer, since it does not count a lone dash or middle dot standing between spaces as a word."""
    return len(re.findall(rb"[^ \t\n\r\v\f]+", s.encode("utf-8")))


# ------------------------------------------------------------------ sources
T = {}
for k, (rel, want) in SRC.items():
    T[k] = read(rel)
    need(md5(T[k]) == want, "%s: md5 %s, expected %s" % (rel, md5(T[k]), want))


def lines_of(s):
    x = s.split("\n")
    return x[:-1] if x and x[-1] == "" else x


TX, LT = lines_of(T["text"]), lines_of(T["latest"])
N = len(TX)
need(N == 632 and len(LT) == 632, "file 99 has %d lines and the latest text %d, expected 632 each" % (N, len(LT)))
DIFFER = [i + 1 for i in range(N) if TX[i] != LT[i]]
HEADS = [(i + 1, TX[i]) for i in range(N) if TX[i].startswith("#")]

INDEX = {}
for ln in T["index"].split("\n"):
    if ln.strip():
        u = json.loads(ln)
        INDEX[u["id"]] = u
ROWS = [r for r in csv.DictReader(T["s100"].splitlines()) if r["strong_candidate_list"] == "never challenged"]
need(len(ROWS) == 29, "S100 lists %d never-challenged candidates, expected 29" % len(ROWS))
ROWS.sort(key=lambda r: (INDEX[r["unit_id"]]["line"], INDEX[r["unit_id"]]["n"]))
UNITS = [r["unit_id"] for r in ROWS]
CNUM = {u: "C%02d" % (i + 1) for i, u in enumerate(UNITS)}
TERMS = {r["unit_id"]: r["terms"] for r in ROWS}

# the S101 graph's nodes: word patterns from the S101 script (read with ast, not run); defining sentences from the graph
_tree = ast.parse(T["s101"])
NODES = None
for _n in _tree.body:
    if isinstance(_n, ast.Assign) and getattr(_n.targets[0], "id", None) == "NODES":
        NODES = ast.literal_eval(_n.value)
need(NODES and len(NODES) == 94, "the S101 script's NODES were not read")
GRAPH = json.loads(T["graph"])
NODE_LINES = {n["id"]: {int(s["id"][1:].split(".")[0]) for s in n["sentences"]} for n in GRAPH["nodes"]}
PAT = {n[0]: re.compile(n[4]) for n in NODES if n[4]}


# ------------------------------------------------------------------ 2. the map from the latest text's ids to file 99
def unit_text(u):
    return INDEX[u]["text"]


def map_unit(u):
    x = INDEX[u]
    a, b = x["line"], x["line_end"]
    here = "\n".join(TX[a - 1:b])
    whole = T["text"]
    found = here.count(x["text"])
    everywhere = whole.count(x["text"])
    changed = [n for n in range(a, b + 1) if n in DIFFER]
    if found == 1 and everywhere == 1:
        how = "same line, word for word" + (
            "; the line differs from the latest text elsewhere (what was removed there), the sentence does not"
            if changed else "; the line is the same as in the latest text")
    elif found >= 1:
        how = "same line, word for word; the same words also stand elsewhere in file 99 (%d times in all)" % everywhere
    else:
        how = "MOVED OR CHANGED: not found on its line (found %d times elsewhere)" % everywhere
    return dict(unit=u, c=CNUM[u], line=a, line_end=b, how=how, ok=(found >= 1))


MAP = [map_unit(u) for u in UNITS]
need(all(m["ok"] for m in MAP), "a candidate is not on its line in file 99: %s" % [m for m in MAP if not m["ok"]])

# ------------------------------------------------------------------ the excerpts
# A key names either whole lines ("L<a>-<b>", or "L<a>") or a run of words in one line: EXC[key] = (line, first
# words, last words), the run being from the first occurrence of the first words to the end of the first occurrence of
# the last words after them. Both must occur exactly once in the line.
EXC = {
    "8a": (8, "An **argument** is reasons why this and not that", "the arguments someone holds."),
    "31a": (31, "No undefined predicate that says", "not such a predicate."),
    "91a": (91, "\\(J\\) indexes components;", "footprint \\(V_j\\subseteq V\\)."),
    "109a": (109, "A port \\(v\\) is an **input** under", "sets \\(v\\) directly."),
    "159a": (159, "A contract is a stated subset of the changes its target admits", "is what makes it one."),
    "305a": (305, "**Finite monotone claim.**", "exactly when \\(d\\in\\bigcap\\min\\mathsf S\\)."),
    "307a": (307, "A route of the candidate is a route whether or not any history runs it;",
             "not to the routes a candidate contains."),
    "315a": (315, "A claim is **ruled out** for an assessor", "when no argument usable by \\(j\\) rules it out."),
    "317a": (317, "an answer that such an argument rules out stays ruled out", "stays usable (Part VIII)."),
    "369a": (369, "If a premise about them ceases to be live,", "no candidate becomes an account by that (E)."),
    "375a": (375, "**Histories.** A history \\(h\\) is a set of occurrences", "the connections actually instantiated."),
    "397a": (397, "**Arguments.** A record leaf is a reference to an event", "with an interpreted claim."),
    "397b": (397, "**Arguments.** A record leaf is a reference to an event",
             "that absence rules out nothing, neither \\(\\phi\\) nor \\(\\neg\\phi\\)."),
    "397c": (397, "**A premise that is the denial.**", "does not rule that claim out for anyone."),
    "409a": (409, "A construction trace may therefore identify a binding", "relay is not construction."),
    "429a": (429, "A complete critical episode contains", "a content-sensitive response."),
    "429c": (429, "A creative critical episode contains", "connected to its inquiry."),
    "441a": (441, "The aims are declared inputs:", "(P) puts no order on alternatives."),
    "441b": (441, "\\(\\operatorname{ProducedBy}\\) is met when", "that it does not contain."),
    "520a": (520, "Kinds, from signatures (K).", "Kinds, from signatures (K)."),
    "526a": (526, "(K) depends on (O) and a contract.", "(K) depends on (O) and a contract."),
    "526b": (526, "**Dependence order.** (O) and (Q) depend on nothing;", "(S), (B), (D) depend on (E)."),
    "536a": (536, "Part V says which of the four each classic attempt fails:",
             "conclusion-as-premise fails non-circular dependence."),
    "600a": (600, "**Consequence.** There is no residual, undefined predicate", "(EX) is defined (Part XI)."),
}


def span(key):
    n, first, last = EXC[key]
    s = TX[n - 1]
    need(s.count(first) == 1, "excerpt %s: its first words occur %d times on line %d" % (key, s.count(first), n))
    i = s.index(first)
    j = s.find(last, i)
    need(j >= 0 and s.count(last, i) >= 1, "excerpt %s: its last words are not after its first on line %d" % (key, n))
    return n, s[i:j + len(last)]


def rng(key):
    """(first line, last line) of a key naming whole lines."""
    m = re.fullmatch(r"L(\d+)(?:-(\d+))?", key)
    need(m, "bad key %r" % key)
    a = int(m.group(1))
    return a, int(m.group(2) or a)


def key_lines(key):
    if key in EXC:
        return {EXC[key][0]}
    a, b = rng(key)
    return set(range(a, b + 1))


def cite(key):
    if key in EXC:
        return "L%d (excerpt)" % EXC[key][0]
    a, b = rng(key)
    return "L%d" % a if a == b else "L%d–L%d" % (a, b)


# ------------------------------------------------------------------ the candidates: context and definitions
# CTX: the lines printed with the candidate (a key of whole lines); a candidate whose context was printed with an
# earlier one of the same part points to it. DEFS: (what it names, the S101 nodes it gives, the keys that give it).
CTX = {
    "L27.s2": "L19-27", "L41.s4": "L41", "L47.s2": "L47",
    "L113.s1": "L111-127", "L113.s2": "L111-127", "L115.s1": "L111-127", "L123.s1": "L111-127",
    "L124.s1": "L111-127", "L125.s1": "L111-127", "L127.s1": "L111-127", "L127.s2": "L111-127", "L127.s3": "L111-127",
    "L161.s1": "L157-161", "L161.s2": "L157-161", "L161.s3": "L157-161",
    "L217.s2": "L215-225", "L219.s1": "L215-225", "L220.s1": "L215-225", "L225.s1": "L215-225", "L225.s4": "L215-225",
    "L273.s1": "L267-277", "L311.s2": "L309-313", "L375.s2": "L375", "L383.s1": "L377-383", "L385.s1": "L385",
    "L393.s4": "L387-393", "L443.s2": "L443-453", "L471.s2": "L463-471", "L520.s7": "L513-520",
}
DEFS = {
    # ---- part 1
    "L27.s2": [("the classes defined, and their membership", [], ["L528"]),
               ("the class the title names", [], ["L3"]),
               ("an instance for the class, not a claim about an actual system", [], ["L632"])],
    "L41.s4": [("transport; faithful on C", ["transport"], ["L183-189"]),
               ("fidelity: (F1), (F2), (A)", ["fid"], ["L233-253"]),
               ("selected provenance; survival on H", ["prov"], ["L193-201"]),
               ("Argument 3", ["Arg3"], ["L572"]),
               ("faithfulness without assessors", [], ["L67"])],
    "L47.s2": [("the three provenances; constructed", ["prov"], ["L193-201"]),
               ("construction and the construction trace (Build)", ["build"], ["L405", "L411"]),
               ("creative attribution: newness (N) and origin (G)", ["N_new", "G"], ["L413-425"]),
               ("the creative critical episode", ["episode"], ["429c"]),
               ("where creativity lives", [], ["L13"]),
               ("the creative-episode class", [], ["L528"])],
    "L113.s1": [("organization (O)", ["O"], ["L85-105"]),
                ("contract", ["contract"], ["L141", "159a"]),
                ("what (K) depends on", [], ["526a"])],
    "L113.s2": [("organization, component, footprint, L_j", ["O"], ["L85-105"]),
                ("contract", ["contract"], ["L141"])],
    "L115.s1": [("L_j(a,b), admitted edits, boundaries", ["O"], ["L85-105"]),
                ("(K) where it is used: fidelity and kinds", ["fid"], ["L233-253", "L281"]),
                ("Argument 1", ["Arg1"], ["L554-558"]),
                ("kinds, from signatures", [], ["520a"])],
    "L123.s1": [("input, output, observation", ["roles"], ["L109"]),
                ("component, port, an edit that sets a port", ["O"], ["L85-105"]),
                ("a cause told from a correlation", [], ["L37"])],
    "L124.s1": [("observation, defined by a measurement's signature", ["roles"], ["L109"]),
                ("component, port", ["O"], ["L85-105"])],
    "L125.s1": [("a changed rule is a changed component", ["O"], ["L85-105"]),
                ("a rule and a cause", [], ["L57"]),
                ("constitutive rules", [], ["L347"])],
    "L127.s1": [("the data an interpretation supplies (membership)", [], ["L528"]),
                ("kind eliminable", ["Arg1"], ["L554-558"]),
                ("a kind is nothing over and above edit-response", [], ["L11"])],
    "L127.s2": [("no undefined predicate \"is a cause\"", [], ["31a", "600a"]),
                ("component", ["O"], ["L85-105"]),
                ("a cause told from a correlation; a rule and a cause", [], ["L37", "L57"])],
    "L127.s3": [("where signatures do work", ["fid"], ["L233-253", "L281"]),
                ("a kind is nothing over and above edit-response", [], ["L11"])],
    # ---- part 2
    "L161.s1": [("question: target, contract, baseline, query, aims, provenance", ["question", "contract", "Q"],
                 ["L133-147"]),
                ("the baseline and non-vacuity", ["nonvac"], ["L257"]),
                ("when two questions are different", [], ["L151"])],
    "L161.s2": [("the text's other uses of \"event\"", [], ["L55", "397a", "L604-608"]),
                ("occurrences and histories", ["occ", "hist"], ["L169", "375a"])],
    "L161.s3": [("question", ["question"], ["L133-147"]),
                ("contract, and the provenance of a contract", ["contract", "prov_c"], ["L133-147", "L155"]),
                ("a criticism's alleged defect, and the question p_δ", ["K1"], ["L377-381"]),
                ("finding a question", ["G", "Arg5"], ["L413-425", "L588-592"]),
                ("historical index", ["hist_index"], ["L367"])],
    "L217.s2": [("contract; admitted edit–boundary pairs", ["contract"], ["L133-147"]),
                ("transport", ["transport"], ["L183-189"]),
                ("simulation layer", ["layers"], ["L175-177"]),
                ("the history H of a selected transport", ["prov"], ["L193-201"]),
                ("occurrences and histories", ["occ", "hist"], ["L169", "375a"])],
    "L219.s1": [("the answer profile Ans", ["Q"], ["L133-147"]),
                ("τ and σ of a transport", ["transport"], ["L183-189"]),
                ("the simulation layer's queries are predictions", ["layers"], ["L175-177"]),
                ("question fidelity (A)", ["fid"], ["L233-253"])],
    "L220.s1": [("fidelity: (F1), (F2), (A)", ["fid"], ["L233-253"]),
                ("Argument 4", ["Arg4"], ["L580-584"])],
    "L225.s1": [("selected: population, variation operator μ, history H", ["prov"], ["L193-201"]),
                ("Argument 3", ["Arg3"], ["L572"]),
                ("construction trace (Build)", ["build"], ["L405"]),
                ("the two responses in the worked episode", [], ["L626"]),
                ("recognized difficulty", ["episode"], ["L429"])],
    "L225.s4": [("origin (G), newness (N), the originative act", ["G", "N_new"], ["L413-425"]),
                ("Build", ["build"], ["L405"]),
                ("creative critical episode", ["episode"], ["L429"]),
                ("Argument 4, and its consequence", ["Arg4"], ["L580-584"])],
    # ---- part 3
    "L273.s1": [("non-circular dependence", ["noncirc"], ["L255"]),
                ("explanatory candidate; Account (E)", ["cand", "E"], ["L231", "L259-265"]),
                ("an argument whose premise is the denial", ["arg"], ["397c"]),
                ("(Suff) on conclusion-as-premise", ["suff"], ["536a"])],
    "L311.s2": [("routes, (S), (B), (D)", ["SBD"], ["L287-303"]),
                ("finite monotone claim", ["fmc"], ["305a"]),
                ("\"contribution\" in Part XI", ["P", "prodby"], ["L435-439", "441b"])],
    "L375.s2": [("occurrence", ["occ"], ["L169"]),
                ("represents (R)", ["rep"], ["L205-209"]),
                ("input", ["roles"], ["109a"]),
                ("components", ["O"], ["91a"]),
                ("a route of a candidate, and where it meets an active route", ["SBD"], ["L287-303", "307a"]),
                ("ProducedBy, ProducesVia", ["prodby", "EX"], ["441b", "L443-453"])],
    "L383.s1": [("occurrence", ["occ"], ["L169"]),
                ("criticism", [], ["L71"]),
                ("explanatory candidate; Account (E)", ["cand", "E"], ["L231", "L259-265"])],
    "L385.s1": [("active route", ["aroute"], ["L375"]),
                ("content", ["content"], ["L169"]),
                ("represented", ["rep"], ["L205-209"]),
                ("recoding", ["Arg8"], ["L365", "L612"]),
                ("use of a binding in a construction trace", [], ["409a"]),
                ("a content-sensitive response in an episode", ["episode"], ["429a"]),
                ("(K1), (K2)", ["K1", "K2"], ["L377-383", "L387-393"])],
    "L393.s4": [("argument; usable; rules out; tentatively accept", ["arg", "rules_out", "tentative"],
                 ["8a", "397b"]),
                ("ruled out, not ruled out", ["ruled"], ["315a"]),
                ("a premise that ceases to be live", ["failed"], ["369a", "317a"])],
    "L443.s2": [("the aims O and P of a repair; repair (P)", ["in_aims", "P"], ["L435-439", "441a"]),
                ("explanatory candidate; Account (E)", ["cand", "E"], ["L231", "L259-265"]),
                ("deployable: Deploy and the repertoire", ["deploy"], ["L403"])],
    "L471.s2": [("tasks, attributes, possibility", ["tasks"], ["L461"]),
                ("(CT2) among what would rule the class out", ["C546"], ["L546"])],
    "L520.s7": [("Account (E)", ["E"], ["L259-265"]),
                ("fidelity: (F1), (F2), (A)", ["fid"], ["L233-253"]),
                ("non-circular dependence, non-vacuity", ["noncirc", "nonvac"], ["L255-257"]),
                ("the dependence order", [], ["526b"]),
                ("Argument 6", ["Arg6"], ["L596-600"]),
                ("indices, not imports", [], ["L524"])],
}
# nodes the scan proposes that no DEFS entry gives, with the reason
SCAN_ASIDE = {
    ("L113.s2", "K"): "the candidate is part of the definition of (K), given with it (L113-L117)",
    ("L123.s1", "K"): "(K) is given with the candidate's context (L113-L117)",
    ("L123.s1", "sigfam"): "the candidate is one of the sentences that define the families of signatures",
    ("L124.s1", "K"): "(K) is given with the candidate's context (L113-L117)",
    ("L125.s1", "K"): "(K) is given with the candidate's context (L113-L117)",
    ("L125.s1", "sigfam"): "the candidate is one of the sentences that define the families of signatures",
    ("L127.s1", "K"): "(K) is given with the candidate's context (L113-L117)",
    ("L127.s3", "K"): "(K) is given with the candidate's context (L113-L117)",
    ("L219.s1", "psv"): "the candidate is one of the sentences that define prediction, violation and surprise",
    ("L220.s1", "psv"): "the candidate is one of the sentences that define prediction, violation and surprise",
    ("L225.s1", "psv"): "violation is defined in the candidate's context (L220)",
    ("L375.s2", "aroute"): "the candidate is the definition of an active route",
    ("L383.s1", "K1"): "(K1) is given with the candidate's context (L377-L381)",
    ("L471.s2", "CT2"): "the candidate is (CT2) itself",
}

PARTS = [
    dict(key="1", title="Parts 0 and II", lines=(1, 130),
         where="the front matter's notes on what the document does not claim, two answers to grievances, and the "
               "section of Part II on kinds as edit-signatures"),
    dict(key="2", title="Parts III and IV", lines=(131, 228),
         where="the section of Part III on a question that can be in error, and the section of Part IV on "
               "prediction, violation and the two responses to a violation"),
    dict(key="3", title="Parts V to XIV", lines=(229, 632),
         where="single sentences from Parts V, VI, IX, XI, XII and XIV: circularity, routes, active routes, criticism "
               "and the use of a reason, withdrawing a premise, created explanation, retention, and the class "
               "collected"),
]
for p in PARTS:
    p["units"] = [u for u in UNITS if p["lines"][0] <= INDEX[u]["line"] <= p["lines"][1]]
need([len(p["units"]) for p in PARTS] == [12, 8, 9], "the parts hold %s candidates" % [len(p["units"]) for p in PARTS])
need(set(CTX) == set(UNITS) and set(DEFS) == set(UNITS), "CTX or DEFS does not name exactly the 29 candidates")
for u in UNITS:
    x = INDEX[u]
    need(set(range(x["line"], x["line_end"] + 1)) <= key_lines(CTX[u]), "%s: its context does not hold it" % u)

# ------------------------------------------------------------------ 3. the scan, and the check of DEFS against the graph
SCAN = {}
for u in UNITS:
    hits = [nid for nid, pat in PAT.items() if pat.search(unit_text(u))]
    SCAN[u] = hits
    given = {nid for _, nids, _ in DEFS[u] for nid in nids}
    for nid in hits:
        need(nid in given or (u, nid) in SCAN_ASIDE,
             "%s: the scan proposes node %s, which DEFS neither gives nor sets aside" % (u, nid))
    for label, nids, keys in DEFS[u]:
        covered = set().union(*[key_lines(k) for k in keys])
        for nid in nids:
            need(nid in NODE_LINES, "%s: %s is not a node of the S101 graph" % (u, nid))
            need(NODE_LINES[nid] & covered or not NODE_LINES[nid],
                 "%s: %s's excerpts (%s) cover none of its defining lines %s" % (u, nid, keys, sorted(NODE_LINES[nid])))
for (u, nid) in SCAN_ASIDE:
    need(nid in SCAN[u], "SCAN_ASIDE names %s for %s, which the scan does not propose" % (nid, u))

# ------------------------------------------------------------------ the owner's words
dec = T["decisions"]
KEEP = [20, 21, 23, 25, 26, 27, 28, 33, 34]
OWN = {}
for n in KEEP:
    m = re.search(r"(?m)^S%d\. \[Claude's reading: .*?\] (.*)$" % n, dec)
    need(m, "decision S%d not found" % n)
    OWN[n] = m.group(1)
REPLACE = [
    (21, "Answering file 93's choices (log S93): ", "Answering choices the drafters had put to the owner: "),
    (23, "Next step after log S94, in three paragraphs: ", "Next step, in three paragraphs: "),
    (25, "Claude's report that draft 5 ties", "Claude's report that an earlier draft ties"),
    (25, " (log S95): ", ": "),
    (26, " (log S95): ", ": "),
    (33, "After reading log S101 (file 101, what the tested strong candidates depend on), in three paragraphs: ",
     "After reading a study of what seven sentences of the text depend on, in three paragraphs: "),
    (34, "Then, after log S102 (file 102, every way hard to vary has been defined and used), in two paragraphs: ",
     "Then, after reading a summary of every way hard to vary had been defined and used, in two paragraphs: "),
]
OWNER_TEXT = dict(OWN)
for n, old, new in REPLACE:
    s = OWNER_TEXT[n]
    need(s.count(old) == 1, "S%d: %r occurs %d times" % (n, old, s.count(old)))
    i = s.index(old)
    need(s[:i].count('"') % 2 == 0 and s[i + len(old):].count('"') % 2 == 0, "S%d: %r lies inside a quotation" % (n, old))
    OWNER_TEXT[n] = s.replace(old, new)
for n in OWN:
    b = OWNER_TEXT[n]
    for _, old, new in [r for r in REPLACE if r[0] == n]:
        b = b.replace(new, old, 1)
    need(OWN[n] == b, "S%d: the owner's words changed" % n)
    need(not re.search(r"\blog S\d|\bfile \d{2,3}\b|\bdraft \d", OWNER_TEXT[n]), "S%d still names an internal record" % n)
need(OWN[27].rstrip().endswith("(26 September 2026)") and "It's also a detail that exists outside the process." in
     OWN[27], "S27 is not whole")
DATES = {20: "24 and 25 September 2026", 21: "25 September 2026", 23: "25 September 2026", 25: "26 September 2026",
         26: "26 September 2026", 27: "26 September 2026", 28: "26 September 2026", 33: "27 September 2026",
         34: "27 September 2026"}
OWNER = "\n\n".join(
    ["## 2. The owner's words",
     "The theory's owner took the decisions below, in this order; the task in section 5 is set against them. Each is "
     "quoted from the project's record of decisions. Words inside quotation marks are the owner's, word for word, "
     "typos included, except where the connecting words say that a quoted phrase is Claude's (in S26 and S28). The "
     "few connecting words outside the quotation marks are the recorder's; where the record names internal files or "
     "logs there, a plain description stands in their place. The record's own reading of each decision is not given "
     "here: the owner's words decide, and where section 5 is worded differently from them, the owner's words decide "
     "there too, and you should say so. Decisions on how the work is run, and not on the theory, are left out. In "
     "these words \"Claude\" is the drafters of the text; \"your agents\" and \"your explanation\" in S27 are "
     "addressed to them."] +
    ["**S%d** (%s). %s" % (n, DATES[n], OWNER_TEXT[n]) +
     ("\n\n*What S27 answers.* Between S26 and S27 the drafters gave the owner the five examples asked for: holding "
      "an explanation in a carrier (ink, a brain, a file); copying or teaching it; testing between two rival "
      "explanations, where the test changes the thing explained; building from an explanation (a perpetual-motion "
      "machine, a bridge); and performing music. The examples are the drafters' words, not the owner's, and are not "
      "a decision. S27 is the owner's reply to them." if n == 26 else "")
     for n in KEEP])


# ------------------------------------------------------------------ the parts
def heading_of(line):
    """The Part and the section heading a line stands under."""
    part = sec = ""
    for i, h in HEADS:
        if i > line:
            break
        lvl = len(h) - len(h.lstrip("#"))
        if lvl == 1:
            part, sec = h.lstrip("#").strip(), ""
        elif lvl == 2:
            sec = h.lstrip("#").strip()
    return part, sec


def label_of(u):
    """The bold run-in label a sentence stands under, if its line opens with one (for example "**Histories.**")."""
    m = re.match(r"\*\*([^*]+?)\.?\*\*", TX[INDEX[u]["line"] - 1])
    return m.group(1) if m else ""


def given_lines(a, b):
    return ["L%d| %s" % (i, TX[i - 1]) for i in range(a, b + 1) if TX[i - 1].strip()]


def candidate_block(u, printed):
    x = INDEX[u]
    part, sec = heading_of(x["line"])
    where = part + ("; " + sec if sec else "") + ("; " + label_of(u) if label_of(u) and label_of(u) != sec else "")
    lines_txt = "L%d" % x["line"] if x["line"] == x["line_end"] else "L%d–L%d" % (x["line"], x["line_end"])
    out = ["### %s · %s · %s" % (CNUM[u], lines_txt, where),
           "The sentence:",
           "\n".join("> " + s for s in unit_text(u).split("\n"))]
    ck = CTX[u]
    if ck in printed:
        out.append("Where it stands: %s, given above with %s." % (cite(ck), printed[ck]))
    else:
        a, b = rng(ck)
        out.append("Where it stands (%s):" % cite(ck))
        out.append("\n\n".join(given_lines(a, b)))
        printed[ck] = CNUM[u]
    out.append("Definitions and passages it uses (in section 4, or in section 3 where printed there): " + "; ".join(
        "%s: %s" % (label, ", ".join(cite(k) for k in keys)) for label, _, keys in DEFS[u]) + ".")
    return "\n\n".join(out)


def defs_section(units, printed):
    """Every key the part's candidates use, each once, in text order: whole lines, and excerpts of lines not given
    whole. Lines printed in section 3 as a candidate's context are not repeated: one bracketed line says where they
    are. Runs given nowhere are named by one bracketed line with the headings they hold."""
    ctx_lines = set().union(*[key_lines(k) for k in printed])
    whole, parts = set(), {}
    for u in units:
        for _, _, keys in DEFS[u]:
            for k in keys:
                if k in EXC:
                    parts.setdefault(EXC[k][0], set()).add(k)
                else:
                    a, b = rng(k)
                    whole |= set(range(a, b + 1))
    whole -= ctx_lines
    for n in list(parts):
        if n in whole or n in ctx_lines:
            del parts[n]
    items = []   # (first line, last line, order, text)
    for k, c in printed.items():
        a, b = rng(k)
        items.append((a, b, 0, "[%s: given in section 3, with %s]" % (cite(k), c)))
    for n in sorted(whole):
        if TX[n - 1].strip():
            items.append((n, n, 1, "L%d| %s" % (n, TX[n - 1])))
    for n in sorted(parts):
        spans = sorted({span(k) for k in parts[n]}, key=lambda s: TX[n - 1].index(s[1]))
        # an excerpt inside another is given once, as the longer
        keep = [sp for sp in spans if not any(sp != o and sp[1] in o[1] for o in spans)]
        for i, (_, sp) in enumerate(keep):
            items.append((n, n, 1 + i, "L%d, excerpt| %s" % (n, sp)))
    items.sort()
    out, prev = [], 0

    def gap(lo, hi):
        if any(TX[i - 1].strip() for i in range(lo, hi + 1)):
            hs = "; ".join(h.lstrip("#").strip() for k, h in HEADS if lo <= k <= hi)
            out.append("[L%d–L%d not given here%s]" % (lo, hi, (": " + hs) if hs else ""))
    for a, b, _, text in items:
        if a > prev + 1:
            gap(prev + 1, a - 1)
        out.append(text)
        prev = max(prev, b)
    if prev < N:
        gap(prev + 1, N)
    return "\n\n".join(out)


TASK = """For each candidate sentence, **try to vary it**.

1. **Rival wordings.** Offer one or more rival wordings that you think keep everything the theory needs from this sentence. If one works as well, say so: the sentence is then easy to vary on what the theory asks of it.
2. **Variations that break something.** Offer variations and show what each would break elsewhere in the theory: name the sentence or definition broken, and quote it with its line number.
3. **A failure of the sentence itself.** Look for a contradiction with another sentence, circularity, vacuity, a part that does no work, or a conflict with a case or a definition.
4. **Close each candidate with one line**, exactly one of:
   - `Cnn: HOLDS — …` when every variation you tried breaks something you named (say in a few words what);
   - `Cnn: VARIES — <the rival wording that works as well>`;
   - `Cnn: FAILS — <what fails> — <exact repair wording>`.

**Rules.**

- "Easy to vary" in step 1 is meant plainly: another wording would do the sentence's work as well. It is not the text's own defined term of that name (L317, not given here), which concerns candidate explanations and their rivals.
- Do not list, count, grade or rank rivals or variations, and do not argue from how many there are (decision S20). Each variation stands or falls on what it breaks.
- An argument here means reasons why this and not that (decision S23).
- Do not propose anything about what hard to vary covers: the owner has parked that question (decision S34). A proposal about it will be recorded as parked and not applied.
- Give the exact wording for every proposal: the whole sentence as it would stand, between fence lines. A wording you propose obeys decision S23 and keeps to what the owner's words in section 2 say.
- Quote the text exactly, with line numbers. Where you rely on a line not given here, say so.
- A HOLDS line records only that the variations you tried each broke something you named; it settles nothing (decision S28).
- Keep apart what the text forces and what a reader might take it to mean."""

REPORT = """- One section per candidate, in the order of section 3, headed `Cnn · L<n>`.
- In each section: your attempts under steps 1 to 3, with the exact wording of each proposal between fence lines; then the closing line of step 4, on a line of its own, in exactly one of its three forms.
- Keep the whole report under about 3,000 words. Depth where a candidate needs it counts for more than equal space for all.
- End the report with a line that reads exactly END OF REPORT."""


def build_part(p):
    units = p["units"]
    a, b = CNUM[units[0]], CNUM[units[-1]]
    title = "# Trying to vary the theory's sentences, part %s: %s" % (p["key"], p["title"])
    s1 = ["## 1. What you are asked to do",
          "Sections 3 and 4 give lines of a theory of explanation: a formal semantics of what an explanation is and "
          "of explanatory creativity, 632 lines in all, which calls itself \"the semantics\". Its owner took the "
          "decisions quoted in section 2.",
          "**The candidates.** The text has been revised many times. Some of its sentences stood unchanged in what "
          "they say through every revision while the sentences around them kept changing, and no one has yet made a "
          "proposal against any of them on its own. Twenty-nine such sentences are put to readers in three parts, "
          "each part read on its own. **This part gives %d of them, %s to %s: %s.** Why they were picked says nothing "
          "either way about whether they hold." % (len(units), a, b, p["where"]),
          "**Your task, in one line:** for each candidate sentence, try to vary it. Section 5 sets out the task step "
          "by step, and section 6 the form of the report.",
          "**Your stance.** Try as hard as you can, against the texts alone, to find another wording that does the "
          "sentence's work as well, a change that breaks nothing, or a fault in the sentence itself. A reply that "
          "finds nothing tells us something only when it shows the variations tried and what each one broke.",
          "**Who is who.** In the text and in section 2, \"the owner\" is the theory's owner, whose words are in "
          "section 2, and \"Claude\" is the drafters of the text.",
          "**Citing the text.** Line numbers are those of the whole text, with its title as line 1; sections 3 and 4 "
          "print each line's number before it. Quote the text exactly whenever you rely on it, with its line number."]
    printed = {}
    blocks = [candidate_block(u, printed) for u in units]
    s3 = ["## 3. The candidates",
          "Each candidate is given with its number, its line, where it stands (its Part and heading), the sentence "
          "exactly as it stands, the lines around it, and the definitions and passages it uses, named by the lines "
          "that give them. Where several candidates stand in one passage, the passage is printed once, with the first "
          "of them. Each line is given as `L<number>| ` followed by the line exactly as it stands; the prefix is not "
          "part of the text. Blank lines are left out."] + blocks
    s4 = ["## 4. Lines given for their definitions",
          "The lines named in section 3 that are not printed there, each once, in the order of the text. `L<number>| ` "
          "introduces a whole line exactly as it stands; `L<number>, excerpt| ` introduces a run of words taken from "
          "that line exactly as they stand, the rest of the line left out. A bracketed line says where lines printed "
          "in section 3 stand, or names a run of lines given nowhere here, with the headings it holds.",
          "=============== BEGIN LINES GIVEN FOR THEIR DEFINITIONS ===============",
          defs_section(units, printed),
          "=============== END LINES GIVEN FOR THEIR DEFINITIONS ==============="]
    s5 = ["## 5. The task", TASK]
    s6 = ["## 6. The report", REPORT]
    return "\n\n".join([title] + s1 + [OWNER] + s3 + s4 + s5 + s6) + "\n"


# ------------------------------------------------------------------ the scan of the frame (decision S23)
SCRUB = [r"\bfits?\b", r"\bfitt\w*", r"\bsupport\w*", r"\bverif\w*", r"\bcorroborat\w*", r"\bprov(e|es|ed|en|ing)\b",
         r"\bdisprov\w*", r"\bbelie\w*", r"better than", r"worse than", r"\btrue\b", r"\btruth\w*", r"\bestablish\w*",
         r"\bauthorit\w*", r"\bfoundation\w*", r"\bderiv\w*", r"\bjustif\w*", r"\brank\w*", r"\bvalid\w*",
         r"\bcorrect(ly|ness)?\b", r"\bevidence\b", r"\bconfirm\w*", r"\bcertain\w*", r"\bgrade[sd]?\b", r"\bwrong\b",
         r"\bAtria\b", r"\bMimo\b", r"\bGLM\b", r"\bFable\b", r"\bOpus\b", r"\bDeutsch\b", r"\bMarletto\b",
         r"\bPinker\b"]
ALLOWED_IN_FRAME = ["Do not list, count, grade or rank rivals or variations"]   # the task's rule from decision S20


def frame_of(text):
    f = re.sub(r"(?m)^L\d+(, excerpt)?\| .*$", "", text)
    f = re.sub(r"(?m)^> .*$", "", f)
    f = re.sub(r"(?m)^\[L\d+–L\d+ not given here(: .*)?\]$", "", f)   # the headings they name are the text's
    f = re.sub(r"(?s)## 2\. The owner's words.*?(?=## 3\. The candidates)", "", f)
    for s in ALLOWED_IN_FRAME:
        f = f.replace(s, "")
    return f


def scan(text):
    f = frame_of(text)
    return sorted({m.group(0) for pat in SCRUB for m in re.finditer(pat, f, re.I)})


def build():
    out, rows = {}, []
    for p in PARTS:
        text = build_part(p)
        hits = scan(text)
        need(not hits, "part %s: forbidden or withheld words in the frame: %s" % (p["key"], hits))
        for pat in (r"\bAtria\b", r"\bMimo\b", r"\bGLM\b", r"\bDeutsch\b", r"\bMarletto\b", r"\bPinker\b"):
            need(not re.search(pat, text), "part %s names %s" % (p["key"], pat))
        for m in re.finditer(r"(?m)^L(\d+)\| (.*)$", text):
            need(TX[int(m.group(1)) - 1] == m.group(2), "part %s: line %s differs from the text" % (p["key"],
                                                                                                  m.group(1)))
        for m in re.finditer(r"(?m)^L(\d+), excerpt\| (.*)$", text):
            need(m.group(2) in TX[int(m.group(1)) - 1], "part %s: the excerpt of line %s is not in it" % (
                p["key"], m.group(1)))
        for u in p["units"]:
            need("\n".join("> " + s for s in unit_text(u).split("\n")) in text, "part %s: %s not quoted" % (p["key"], u))
            need(("### %s · " % CNUM[u]) in text, "part %s: %s has no heading" % (p["key"], CNUM[u]))
        need(len(text.split()) <= CAP and wc_words(text) <= CAP, "part %s is over %d words (%d)" % (
            p["key"], CAP, wc_words(text)))
        fname = "S103 Round 1 - trying to vary the strong candidates - part %s, %s.md" % (p["key"], p["title"])
        out[os.path.join(TESTS, fname)] = text
        rows.append((p, fname, text))
    jobs, glm = [], []
    for p, fname, text in rows:
        units = p["units"]
        note = ("S103 round 1 (decision S35), part %s (%s): %s to %s; read under '%s', together with the other "
                "reader's reply to the same part" % (p["key"], p["title"], CNUM[units[0]], CNUM[units[-1]],
                                                     READING_RULE))
        jobs.append({"tag": "s103_vary_mimo_%s" % p["key"], "provider": "mimo", "brief": os.path.join(TESTS, fname),
                     "out": OUT_DIR, "effort": "medium", "ladder": [131072, 131072], "attempts": 6,
                     "max_rejects": 3, "max_pass": 3, "note": note})
        glm.append({"tag": "s103_vary_glm_%s" % p["key"], "part": p["key"], "brief": os.path.join(TESTS, fname),
                    "brief_md5": md5(text), "note": note})
    about = ("S103 round 1 of the review rounds of decision S35: the 29 never-challenged strong candidates of S100, in "
             "the stand-alone copy (tests/99 The semantics, standing alone.md, md5 %s), put to Mimo and to GLM in the "
             "same three parts (1: C01-C12, Parts 0 and II; 2: C13-C20, Parts III and IV; 3: C21-C29, Parts V to "
             "XIV), each part sent whole as the one user message at medium effort (decision S17), built by "
             "tools/s103_build.py. Up to three passes (max_pass 3), a later pass only for calls with no reply "
             "returned. Read under '%s'." % (SRC["text"][1], READING_RULE))
    out[JOBS_MIMO] = json.dumps({"purpose": "audit", "about": about, "jobs": jobs}, indent=1,
                                ensure_ascii=False) + "\n"
    out[JOBS_GLM] = json.dumps({"about": about, "rule": READING_RULE, "out": os.path.relpath(OUT_DIR, SEM),
                                "effort": "medium", "max_pass": 3, "jobs": [
                                    dict(j, brief=os.path.relpath(j["brief"], SEM)) for j in glm]},
                               indent=1, ensure_ascii=False) + "\n"
    return out, rows


def report(rows, out):
    print("## Map from the latest text's ids to file 99")
    print("| candidate | unit (latest text) | line in file 99 | part | check |")
    print("|---|---|---|---|---|")
    part_of = {u: p["key"] for p in PARTS for u in p["units"]}
    for m in MAP:
        ln = "%d" % m["line"] if m["line"] == m["line_end"] else "%d–%d" % (m["line"], m["line_end"])
        print("| %s | %s | %s | %s | %s |" % (m["c"], m["unit"], ln, part_of[m["unit"]], m["how"]))
    print("\nlines on which file 99 differs from the latest text: %s" % DIFFER)
    print("\n## Scan (S101 node patterns) and definitions given")
    for u in UNITS:
        print("%s %s: scan %s; S98 terms: %s; given: %s" % (CNUM[u], u, SCAN[u] or "none", TERMS[u] or "none",
                                                         "; ".join("%s (%s)" % (l, ", ".join(cite(k) for k in ks))
                                                                   for l, _, ks in DEFS[u])))
    print("\n## Parts")
    print("| part | candidates | lines of the candidates | file in `tests/` | words (runner / `wc -w`) | md5 |")
    print("|---|---|---|---|---|---|")
    for p, fname, text in rows:
        us = p["units"]
        print("| %s | %s–%s (%d) | %d–%d | `%s` | %d / %d | %s |" % (
            p["key"], CNUM[us[0]], CNUM[us[-1]], len(us), INDEX[us[0]]["line"], INDEX[us[-1]]["line_end"], fname,
            len(text.split()), wc_words(text), md5(text)))
    for path in (JOBS_MIMO, JOBS_GLM):
        print("job list %s, sha256 %s" % (os.path.relpath(path, SEM), hashlib.sha256(out[path].encode()).hexdigest()))


def main():
    check = "--check" in sys.argv[1:]
    out, rows = build()
    bad = []
    for path, text in out.items():
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                if f.read() != text:
                    bad.append(path)
        elif check:
            bad.append(path)
    if check:
        print("check: %d files, %d differ or are missing%s" % (len(out), len(bad), (": " + "; ".join(
            os.path.basename(b) for b in bad)) if bad else ""))
        sys.exit(1 if bad else 0)
    need(not [b for b in bad if os.path.exists(b)], "refusing to overwrite files whose content differs: %s" % bad)
    for path, text in out.items():
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
    report(rows, out)


if __name__ == "__main__":
    main()
