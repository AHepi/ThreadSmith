# run_check_3.py
# What this file does: the same as run_check_2.py, and under every JUMP and every NO CONNECTION
# it also names the general lines it examined and what each of them needed.
#
# Made from run_check_2.py (SHA-256 begins 9a4b21cf771b1208), beside it and leaving it untouched,
# under plan L86 fourth version (SHA-256 begins 32a064ccbfe54359), sections D1 to D8, with these
# changes and no others. Each change is followed by the give-up line the plan records for it.
#
#   D1. A general clause: from the ledger's .pl text with % comments removed, a clause
#       `Head :- Body.` whose head is produced(T) or holds(T), whose body has line(<id>) and at
#       least one other goal; MAKES when the head is produced, SHOWS when holds. A clause of a
#       line removed in the current run is not examined.
#       Gives up: other heads (depends, changes, denied) and bare facts are not examined; a full
#       stop inside a quoted atom would split a clause.
#   D2. Terms and matching: both the checker's effect string and a clause's head term are parsed
#       as terms; they match when they unify (names and arity equal throughout, a head variable
#       binding to the sub-term at its position, a constant equal only to itself).
#       Gives up: a head the parser cannot read is not examined.
#   D3. peek(query, removed): run_query with the check's removed list and the battery's
#       world_removed, no extra; touches none of slowest, report, first_raw, out_of_time,
#       current or the raw log.
#       Gives up: one checker run per goal (time).
#   D4. The goal line: open (<variables>) if a variable remains; else the checker ran out of
#       time; else holds (line <ids>) from the first answer; else no line says so.
#       Gives up: a goal the checker does not know reads "no line says so".
#   D5. Under a JUMP, after Effect's direct lines and before the abduction: the block
#       "General lines that could produce <effect>, and what each needs:" (or ": (none)"), one
#       entry per matching clause in ledger text order, its goal lines, and for a SHOWS clause
#       the line "a SHOWS clause: it shows <effect> and does not produce it".
#       Gives up: report length.
#   D6. Under a NO CONNECTION, after Expected's direct lines and before "It would take a line
#       nobody wrote": "Reached without the reason:" with one "- lines <ids>" per route (or
#       ": (no route)"), then the D5 block with "reach" for "produce", each clause followed by
#       "the reason's atom, <reason>, is among these conditions" or "... is not among these
#       conditions" (the reason's term against the inner term of each holds/produced goal).
#       Gives up: report length.
#   D7. Indentation two, four and eight spaces before indented() adds two inside a world; the
#       blocks are built in both of a world's battery runs and stripped (the L86_strip rule)
#       from each finding before the count line compares the two runs.
#       Gives up: none.
#   D8. Nowhere else.
#       Gives up: none.
#
# The run_check_2.py header follows, unchanged, for the lineage.
#
# run_check_2.py
# What this file does: takes a ledger, runs the s(CASP) checker on it several times
# (taking lines out to see what changes), and writes a plain-prose report that points
# at the writer's own sentences. It never guesses: every sentence in the report is built
# from fixed templates plus the ledger's own wording.
#
# Made from run_check.py (SHA-256 begins eff1dee15bebc977), beside it and leaving it
# untouched, under plan L79 third version (SHA-256 begins 2e97300690dc39f7), sections
# D1 to D8, with these changes and no others. Each change is followed by the give-up
# line the plan records for it.
#
#   D1. run_query(ledger_text, query, removed_lines, world_removed): world_removed is
#       required and the module global WORLD_REMOVED goes. smallest_set and every helper
#       that reaches run_query take and forward world_removed. check()'s ask supplies the
#       actual world's list (every case line) by default and, inside the case loop, the
#       case's complement (told: every line outside the case; supposed: every other
#       case's lines).
#       Gives up: every caller changes.
#   D2. Inside every named case, told or supposed, after the actual ledger's findings, a
#       section opens with the old one-line heading kept as its first line, followed,
#       indented two spaces, by the findings of checks 1, 2, 2b, 3, 4, 5, the chain
#       (patch 7), patches 8, 9, 10 and 14, run with the world looked at alone; what-ifs
#       (patches 11 and 13) are not run inside a case. Then the count line, N being the
#       findings of that run absent from a second run with the actual ledger's general
#       lines added to the world. Then the outcomes block of D5 for the world.
#       Gives up: each case runs twice; false alarms inside worlds, which N is there to show.
#   D3. In the what-if block, after the old "Set aside, because ..." line, which stays,
#       one line per set-aside line naming the line that ties it to what THIS what-if
#       changed and that line's verdict above; and, where any tying line or set-aside
#       line is filled in or usual case, a note that the block leans on lines the writer
#       did not write.
#       Gives up: report length.
#   D4. The heads of the BECAUSE-claim, SINCE-claim, PLAN and DENIED BECAUSE findings
#       carry the line's mark and sentence; a JUMP, a NO CONNECTION and a CANNOT TELL
#       name the lines they rest on; chain rows carry the mark and sentence; a what-if
#       head carries its own line when the ledger's whatifs entry names one.
#       Gives up: report length; a JUMP may over-name.
#   D5. An OUTCOMES: block after the actual ledger's findings and at the end of each
#       world section, one line per check. The "NO FAULT FOUND in the lines that were
#       checked." line is removed.
#       Gives up: the one-line header.
#   D6. A contradiction inside a told world is printed as the world's own, with the
#       INSIDE heading and "Every line needed is inside the world."; the three
#       supposition phrases are not used for a told case. Supposed cases are unchanged.
#       (The plan records no give-up line for D6.)
#   D7. The gauge line keeps its marks prefix and reads "N bin entries over M sentences
#       (not checked)" where it read "N of M sentences went to the leftover bin (not
#       checked)", and four counts are printed below it.
#       Gives up: all rest on the translator's fields, unchecked.
#   D8. Where a claim_because and a denied_because share both effect and cause, a line
#       saying so is printed after the DENIED BECAUSE block, whose "Fine." text stays.
#       Gives up: a denial "in a different respect" is flagged; 38 has no respect field yet.
#
# Choices recorded under rule 7, where the plan leaves the reading open or where two of
# its own requirements pull apart. In each the old findings' text stays byte-identical.
#
#   C1 (D5, and expectation A7). D5 decides "no line of that kind" by the check's first
#       query's raw output carrying `existence_error(scasp_predicate, ...)`. That message
#       cannot appear when the only line of that kind is one the world has taken out:
#       run_query takes out the `line(x).` fact and leaves the clause it carries, so the
#       predicate is still defined and s(CASP) answers "Warning: s(CASP): No models".
#       On Ultra's T10-D that made the actual ledger read "because claims: asked, nothing
#       found", where A7 and the plan's own frozen mock (tests/L79 Normaliser mocks/
#       T10D_new.txt, line 5) require "because claims: not asked, no line of that kind".
#       The test here is D5's message OR: the ledger carries clauses of that kind and
#       every one of them is carried by a line this world has taken out. The removal
#       itself is untouched, so no query and no old finding moves.
#   C2 (D4). D4 fixes `  - (no line supports the cause)` for an empty Cause's lines and
#       `  - (none)` for an empty Effect's direct lines, and fixes no empty-case wording
#       for Reason's lines, Expected's direct lines, Claim line or Plan line. Where it
#       fixes none, the title stands alone: no wording is invented and none is borrowed
#       from another block. `  - (none)` is not printed either, because the frozen A1
#       instrument (tools/L79_normalise.py) matches described lines with
#       `^\s*- (?:line \S+ \[[^\]]*\]:|\(no line supports)`, which does not match
#       `- (none)`; outside a world section that line is classified "text" and reported
#       as an unlisted addition, and A1 requires HOLDS on all 76 files. D4's wording and
#       A1 cannot both be met, and A1 is the instrument the plan marks by.
#   C3 (D2). D2 has the world section open with the old one-line heading and the findings
#       follow it indented two spaces. A told world's contradiction (D6) is already
#       written that way. A supposed world's contradiction ends at column 0 ("It cannot
#       stand together with line(s) ... that you claim outright." or "THE SUPPOSITION
#       UNDOES ITSELF: ..."), and the A1 instrument closes an open world section at any
#       column-0 line that is not a world heading, so every D2 finding indented below it
#       would be read as an addition outside a world. Those lines are therefore moved to
#       two spaces exactly when findings follow them inside the section (ledger_H), and
#       left where the old driver put them when nothing follows (ledger_N25B, whose old
#       "It cannot stand together ..." line the instrument requires to reappear
#       unchanged). Of the 76 ledgers only H, K06, K09, N25B and P18 carry a supposed
#       case, and only H and N25B reach a contradiction inside one.
import json, re, subprocess, sys, os, tempfile, time

SCASP = "/home/claude/sCASP/scasp"
RULES = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "checker_rules.pl")).read()
TIME_LIMIT_SECONDS = 20
# D1: WORLD_REMOVED is gone. Every caller passes world_removed, so nothing is carried between runs.
# D5: the s(CASP) message that says the ledger has no line of that kind at all (Lesson L2).
NO_SUCH_PREDICATE = "existence_error(scasp_predicate"
# D5: a ledger clause and the line that carries it, as the ledgers write them:
#   claim_because(because, stayed_dry(letter), opened(window)) :- line(because).
LEDGER_CLAUSE = re.compile(r"^\s*(\w+)\(.*?:-\s*line\((\w+)\)\s*[,.]", re.M)
# D5: the predicate each check asks about, for the checks that only a ledger line defines.

# ---- L86 D1, D2: general clauses, terms, unification ----
BLOCK_HEAD = re.compile(r"^(\s*)(General lines that could (produce|reach) .*|Reached without the reason:.*)$")

def strip_blocks(text):
    """D7: a finding with the two L86 blocks removed, by the rule of tools/L86_strip.py."""
    out, depth = [], None
    for line in text.split("\n"):
        m = BLOCK_HEAD.match(line)
        if m: depth = len(m.group(1)); continue
        if depth is not None and line.strip() and (len(line) - len(line.lstrip(" "))) > depth: continue
        depth = None; out.append(line)
    return "\n".join(out)

def split_top(text, sep=","):
    """Split at separators outside parentheses."""
    parts, depth, cur = [], 0, ""
    for ch in text:
        if ch == "(": depth += 1
        elif ch == ")": depth -= 1
        if ch == sep and depth == 0: parts.append(cur); cur = ""
        else: cur += ch
    if cur.strip(): parts.append(cur)
    return [p.strip() for p in parts if p.strip()]

def parse_term(text):
    """D2: a term is a name, a variable (upper-case or underscore first), or name(term, ...)."""
    text = text.strip()
    m = re.match(r"^([A-Za-z0-9_]+)\s*\((.*)\)$", text, re.S)
    if m: return ("f", m.group(1), [parse_term(a) for a in split_top(m.group(2))])
    if re.match(r"^[A-Z_]\w*$", text): return ("v", text)
    if re.match(r"^\w+$", text): return ("f", text, [])
    return None

def render(term):
    """A term as the checker prints it (no spaces)."""
    if term[0] == "v": return term[1]
    return term[1] + ("(" + ",".join(render(a) for a in term[2]) + ")" if term[2] else "")

def unify(head, effect, bindings):
    """D2: head (may hold variables) against effect; bindings filled; returns True on a match."""
    if head is None or effect is None: return False
    if head[0] == "v":
        if head[1] in bindings: return render(bindings[head[1]]) == render(effect)
        bindings[head[1]] = effect; return True
    if effect[0] == "v": return False
    if head[1] != effect[1] or len(head[2]) != len(effect[2]): return False
    return all(unify(a, b, bindings) for a, b in zip(head[2], effect[2]))

def general_clauses(ledger_text, excluded):
    """D1: [(line_id, kind, head_term_text, [body goals other than line(id)], clause text)] in text order."""
    text = re.sub(r"%[^\n]*", "", ledger_text)
    out = []
    for clause in re.split(r"\.(?:\s|$)", text):
        clause = " ".join(clause.split())
        if ":-" not in clause: continue
        head, body = clause.split(":-", 1); head = head.strip()
        m = re.match(r"^(produced|holds)\((.*)\)$", head, re.S)
        if not m: continue
        goals = split_top(body)
        ids = [re.match(r"^line\((\w+)\)$", g).group(1) for g in goals if re.match(r"^line\((\w+)\)$", g)]
        others = [g for g in goals if not re.match(r"^line\((\w+)\)$", g)]
        if not ids or not others: continue
        line_id = ids[0]
        if str(line_id) in {str(x) for x in excluded}: continue
        out.append((line_id, "MAKES" if m.group(1) == "produced" else "SHOWS", m.group(2).strip(), others, clause))
    return out

def apply_bindings(goal, bindings):
    """D2: the goal as written, each bound variable replaced by its sub-term as the checker prints it; and the variables left."""
    left = []
    def sub(m):
        name = m.group(0)
        if name in bindings: return render(bindings[name])
        if name not in left: left.append(name)
        return name
    return re.sub(r"\b[A-Z_]\w*\b", sub, goal), left

def inner_term(goal):
    m = re.match(r"^(holds|produced)\((.*)\)$", goal.strip(), re.S)
    return (m.group(2) if m else goal).replace(" ", "")

CHECK_PREDICATE = {"because claims": "claim_because", "since claims": "claim_since",
                   "plans": "claim_plan", "likeness": "claim_like",
                   "exemptions": "exempt", "denied because": "denied_because"}
OUTCOME_NAMES = ["contradictions", "because claims", "since claims", "the chain", "plans",
                 "exceptions", "likeness", "two usually lines", "exemptions", "added lines",
                 "what-ifs", "denied because"]
ALWAYS_ASKED = ("contradictions", "exceptions")                                   # D5: the rules define these predicates
INPUT_DRIVEN = ("the chain", "two usually lines", "added lines", "what-ifs")      # D5: no query of their own

def run_query(ledger_text, query, removed_lines, world_removed, extra=""):
    """Run one question against the ledger with some lines taken out. Returns (list of answers, seconds, timed_out)."""
    kept = ledger_text
    for line_id in list(dict.fromkeys(list(removed_lines) + list(world_removed))):
        kept = re.sub(r"\bline\(%s\)\.\s*" % re.escape(str(line_id)), "", kept, count=1)
    program = RULES + "\n" + kept + "\n" + extra + "\n?- " + query + ".\n"
    with tempfile.NamedTemporaryFile("w", suffix=".pl", delete=False) as handle:
        handle.write(program); path = handle.name
    started = time.time()
    try:
        done = subprocess.run([SCASP, "--tree", "--human", "-s0", "--unknown=fail", path], stdin=subprocess.DEVNULL,
                              capture_output=True, text=True, timeout=TIME_LIMIT_SECONDS,
                              env=dict(os.environ, LANG="C.UTF-8"))
        output = done.stdout + done.stderr
        timed_out = False
    except subprocess.TimeoutExpired:
        output, timed_out = "", True
    seconds = time.time() - started
    os.unlink(path)
    answers = []
    for block in re.split(r"%\s+Answer \d+.*\n", output)[1:]:
        tree = block.split("% Model")[0].replace("% Justification", "").strip("\n")
        lines_used = sorted(set(re.findall(r"line (\w+) is in the ledger", tree)), key=str)
        assumptions = sorted(set(a.strip().rstrip(",").replace(", and","").replace(", because","")
                                 for a in re.findall(r"there is no evidence that ([^\n]+)", tree)
                                 if "is in the ledger" not in a and "far_smaller" not in a))   # the checker's own comparisons of strength are not the writer's assumptions
        bindings = dict((k, v.rstrip(",").strip()) for k, v in re.findall(r"^(\w+) = (.+?)\s*$", block.split("% Bindings")[-1], re.M)) if "% Bindings" in block else {}
        answers.append({"tree": tree, "lines": lines_used, "assumptions": assumptions, "bindings": bindings})
    return answers, seconds, timed_out, output

def describe_lines(meta, line_ids):
    parts = []
    for line_id in line_ids:
        info = meta["lines"][line_id]
        parts.append('  - line %s [%s, sentence %s]: %s' % (line_id, info["mark"], info["sentence"], info["text"]))
    return "\n".join(parts)

def named_line(meta, line_id):
    """PATCH D4: a line id with the mark and sentence the translator gave it."""
    info = meta["lines"][line_id]
    return "line %s [%s, sentence %s]" % (line_id, info["mark"], info["sentence"])

def listed_lines(meta, title, line_ids, empty=None):
    """PATCH D4: one of the named blocks under a JUMP, a NO CONNECTION or a CANNOT TELL.
    D4 fixes one empty-case wording, `  - (no line supports the cause)`, that the A1
    instrument reads; where D4 fixes none (Reason's lines, Expected's direct lines,
    Claim line, Plan line) the title stands alone rather than borrowing another block's
    wording, and D4's `  - (none)` is not printed (see the choices at the head of this
    file)."""
    if line_ids: return "\n  %s:\n%s" % (title, describe_lines(meta, line_ids))
    if empty: return "\n  %s:\n  - %s" % (title, empty)
    return "\n  %s:" % title

def guessed_lines(meta, line_ids):
    return [l for l in line_ids if meta["lines"][l]["mark"] != "said"]

def smallest_set(ledger_text, query, line_ids, world_removed):
    """Take lines out one at a time. A line stays in the set only if taking it out makes the finding go away."""
    needed = []
    for line_id in line_ids:
        answers, _, _, _ = run_query(ledger_text, query, [line_id], world_removed)
        if not answers:
            needed.append(line_id)
    return needed

def indented(text):
    """PATCH D2: a finding as it reads inside a world section."""
    return "\n".join(("  " + line) if line else line for line in text.split("\n"))

def world_body(block, joined):
    """PATCH D2: a world's contradiction finding, used as the section's opening.
    Its first line is the old one-line heading and stays at column 0. A told world's
    block (D6) is already written at two spaces below that line. A supposed world's
    block ends at column 0 ("It cannot stand together with line(s) ... that you claim
    outright." or "THE SUPPOSITION UNDOES ITSELF: ..."), and a column-0 line closes the
    section for any reader that goes by indentation; so those lines are moved to two
    spaces exactly when findings follow them inside the section. With nothing following,
    the old block is left byte-identical (rule 7)."""
    if not joined: return block
    lines = block.split("\n")
    return "\n".join(lines[:1] + [("  " + l if l and not l.startswith(" ") else l) for l in lines[1:]])

def check(ledger_path, log):
    ledger_text = open(ledger_path).read()
    meta = json.load(open(ledger_path.replace(".pl", ".json")))
    cases = {}
    for line_id, info in meta["lines"].items():
        if info.get("case"): cases.setdefault(info["case"], []).append(line_id)
    all_case_lines = [l for ls in cases.values() for l in ls]
    # D2: the actual ledger's general lines - the ones a world does not have while it is looked at alone.
    general_lines = [l for l, v in meta["lines"].items()
                     if not v.get("case") and ("ALWAYS" in v.get("text", "") or "USUALLY" in v.get("text", ""))]
    usually_lines = [l for l, v in meta["lines"].items() if "USUALLY" in v.get("text", "")]
    ledger_clauses = LEDGER_CLAUSE.findall(ledger_text)   # D5: (predicate, the line that carries it)
    slowest = [0.0]

    def battery(world_removed, world=None, seen_already=frozenset()):
        """Run the checks once. world is None for the actual ledger, else (case name, told, the case's lines).
        Returns (the contradiction blocks, the other findings, the outcomes block)."""
        report, counts, first_raw, out_of_time, empty_input = [], {}, {}, {}, {}
        current = [None]
        # D5: a kind of line the ledger has, but only on lines this world does not have,
        # is a kind of line this world has none of. The raw output cannot say so on its
        # own: run_query takes out the `line(x).` fact and leaves the clause it carries,
        # so s(CASP) finds the predicate defined and answers "No models" instead of
        # existence_error. Both readings together are the test (see the head of this file).
        taken_out = set(world_removed)
        kinds_gone = {pred for pred, carried_by in ledger_clauses if carried_by in taken_out}
        kinds_here = {pred for pred, carried_by in ledger_clauses if carried_by not in taken_out}
        no_such_kind = kinds_gone - kinds_here

        def ask(query, removed=(), extra=""):
            answers, seconds, timed_out, raw = run_query(ledger_text, query, removed, world_removed, extra)
            slowest[0] = max(slowest[0], seconds)
            log.write("\n=== %s | query: %s | removed: %s | %.2fs | timed out: %s ===\n%s\n" % (meta["paragraph"], query, list(removed), seconds, timed_out, raw))
            if timed_out: report.append("RAN OUT OF TIME on the question: " + query)
            if current[0]:
                first_raw.setdefault(current[0], raw)
                if timed_out: out_of_time[current[0]] = True
            return answers

        def begin(name): current[0] = name
        def done(name, count): counts[name] = count; current[0] = None

        def peek(query, removed=()):
            """L86 D3: the checker asked without touching slowest, report, first_raw, out_of_time, current or the log."""
            answers, _, timed_out, _ = run_query(ledger_text, query, removed, world_removed)
            return answers, timed_out

        def goal_lines(goals, bindings, removed):
            """L86 D4: one status line per body goal, judged open, then timed out, then holds, then no line."""
            rows = []
            for goal in goals:
                g, left = apply_bindings(goal, bindings)
                if left: rows.append("\n        %s: open (%s)" % (g, ", ".join(left))); continue
                answers, timed_out = peek(g, removed)
                if timed_out: rows.append("\n        %s: the checker ran out of time" % g)
                elif answers: rows.append("\n        %s: holds (line %s)" % (g, ", ".join(str(l) for l in answers[0]["lines"])))
                else: rows.append("\n        %s: no line says so" % g)
            return "".join(rows)

        def general_block(verb, target, removed, reason=None):
            """L86 D5, D6: the block over the general clauses whose head matches the target."""
            target_term = parse_term(target); entries = []
            for line_id, kind, head_text, goals, _ in general_clauses(ledger_text, list(removed) + list(world_removed)):
                bindings = {}
                if not unify(parse_term(head_text), target_term, bindings): continue
                entry = "\n    - line %s [%s, sentence %s]: %s" % (line_id, meta["lines"][line_id]["mark"], meta["lines"][line_id]["sentence"], meta["lines"][line_id]["text"]) if line_id in meta["lines"] else "\n    - line %s" % line_id
                entry += goal_lines(goals, bindings, removed)
                if reason is None and kind == "SHOWS": entry += "\n        a SHOWS clause: it shows %s and does not produce it" % target
                if reason is not None:
                    among = any(inner_term(apply_bindings(g, bindings)[0]) == reason.replace(" ", "") for g in goals)
                    entry += "\n        the reason's atom, %s, is %samong these conditions" % (reason, "" if among else "not ")
                entries.append(entry)
            if not entries: return "\n  General lines that could %s %s: (none)" % (verb, target)
            return "\n  General lines that could %s %s, and what each needs:" % (verb, target) + "".join(entries)

        def routes_block(expected, direct, reason_lines):
            """L86 D6: the routes that reach the expectation without the reason's lines."""
            answers, _ = peek("holds(%s)" % expected, direct)
            seen, routes = set(), []
            for a in answers:
                ids = tuple(str(l) for l in a["lines"])
                if set(ids) & {str(l) for l in reason_lines} or ids in seen: continue
                seen.add(ids); routes.append(", ".join(ids))
            if not routes: return "\n  Reached without the reason: (no route)"
            return "\n  Reached without the reason:" + "".join("\n    - lines %s" % r for r in sorted(routes))

        # ---- check 1: contradictions ----
        begin("contradictions")
        heading, extra_worlds, seen, fresh = None, [], set(seen_already), []
        if world is None:
            for answer in ask("contradiction(F)"):
                fact = answer["bindings"].get("F", "?")
                if fact in seen: continue
                seen.add(fact)
                needed = smallest_set(ledger_text, "contradiction(%s)" % fact, answer["lines"], world_removed)
                text = "CONTRADICTION about %s.\nThese lines cannot all hold (each one was taken out in turn; the contradiction went away every time):\n%s" % (fact, describe_lines(meta, needed))
                extra = [l for l in answer["lines"] if l not in needed]
                if extra: text += "\nAlso used, but the contradiction survives without them:\n" + describe_lines(meta, extra)
                if guessed_lines(meta, needed): text += "\nNOTE: this finding leans on lines you did not write: %s. If they are wrong, ignore it." % ", ".join(guessed_lines(meta, needed))
                report.append(text)
            done("contradictions", len(seen))
        else:
            case_name, told, its_lines = world
            for answer in ask("contradiction(F)"):
                fact = answer["bindings"].get("F", "?")
                if fact in seen_already or fact in [f for f, _ in fresh]: continue
                fresh.append((fact, smallest_set(ledger_text, "contradiction(%s)" % fact, answer["lines"], world_removed)))
            if not fresh:
                heading = ("INSIDE '%s' (a told world, looked at alone): no contradiction.%s" if told else "UNDER THE SUPPOSITION '%s': no new contradiction.%s") % (
                    case_name, " The contradiction listed above was there already and is not this supposition's doing." if seen_already else "")
            for fact, needed in fresh:
                seen.add(fact)
                if told:
                    # D6: a told world's contradiction is the world's own, and every line it needs is inside the world.
                    text = "INSIDE '%s' (a told world, looked at alone): CONTRADICTION about %s, which the world's own lines give.\n%s\n  Every line needed is inside the world." % (case_name, fact, describe_lines(meta, needed))
                else:
                    outside = [l for l in needed if l not in its_lines and meta["lines"][l]["mark"] == "said"]
                    verdict = "It cannot stand together with line(s) %s that you claim outright." % ", ".join(outside) if outside else "THE SUPPOSITION UNDOES ITSELF: every line needed comes from the supposition or from usual-case lines."
                    text = "UNDER THE SUPPOSITION '%s': CONTRADICTION about %s, which arises only once the supposed lines are added.\n%s\n%s" % (case_name, fact, describe_lines(meta, needed), verdict)
                if guessed_lines(meta, needed): text += "\nNOTE: leans on lines you did not write: %s." % ", ".join(guessed_lines(meta, needed))
                extra_worlds.append(text)
            done("contradictions", len(fresh))
        world_blocks = list(extra_worlds)
        lines_in_contradiction = set()
        for item in (extra_worlds if world else report):
            lines_in_contradiction |= set(re.findall(r"- line (\w+) \[", item.split("Also used")[0]))

        # ---- check 2: "because" claims (PATCHED: patches 1, 2, 3) ----
        begin("because claims")
        circle_causes, observed_claims, verdicts, because_claims, found = set(), [], {}, [], 0
        for claim in ask("claim_because(N, E, C)"):
            n, effect, cause = claim["bindings"]["N"], claim["bindings"]["E"], claim["bindings"]["C"]
            because_claims.append((n, effect, cause))
            head = 'BECAUSE-claim on %s: "%s".' % (named_line(meta, n), meta["lines"][n]["text"])   # D4
            direct = sorted({r["lines"][0] for r in ask("holds(%s)" % effect) if len(r["lines"]) == 1})   # lines that simply state the effect
            routes = ask("produced(%s)" % effect, removed=direct)
            cause_routes = ask("holds(%s)" % cause)
            cause_lines = sorted({l for r in cause_routes for l in r["lines"]})
            if routes:
                route = routes[0]
                text = head + "\nFOLLOWS, using:\n" + describe_lines(meta, route["lines"])
                if route["assumptions"]:
                    text += "\nBUT ONLY ON ASSUMPTIONS NOBODY STATED:\n" + "\n".join("  - there is no evidence that " + a for a in route["assumptions"])
                if ask("produced(%s)" % effect, removed=direct + cause_lines): text += "\nIDLE CAUSE: with the stated cause taken out (%s), it is still produced. The cause is doing no work." % ", ".join(cause_lines)
                else: text += "\nThe stated cause does work: with it taken out (%s), this is no longer produced." % ", ".join(cause_lines)
                bad = [l for l in route["lines"] if l in lines_in_contradiction]
                if bad: text += "\nCANNOT BE LEANED ON YET: it uses line(s) %s, which are part of a contradiction above." % ", ".join(bad)
                if guessed_lines(meta, route["lines"]): text += "\nNOTE: leans on lines you did not write: %s." % ", ".join(guessed_lines(meta, route["lines"]))
                if direct: observed_claims.append((n, route["lines"]))
                verdicts[n] = "FOLLOWS"
                report.append(text); found += 1; continue
            # PATCH 2: is the only support for the cause the effect itself?
            if cause_routes and not ask("holds(%s)" % cause, removed=direct):
                circle_causes.add(cause)
                verdicts[n] = "CIRCLE"
                report.append(head + "\nCIRCLE. The only reason the ledger gives for %s is %s, and the only thing said to produce %s is %s. Take out the line(s) that simply state the effect (%s) and both fall together. Lines in the circle:\n%s" % (
                    cause, effect, effect, cause, ", ".join(direct), describe_lines(meta, sorted(set(cause_lines) | {n}))))
                found += 1
                continue
            # suppose the cause is true, and see whether the effect is then produced
            supposed = "" if cause_routes else "holds(%s).\n" % cause
            if ask("produced(%s)" % effect, removed=direct, extra=supposed):
                verdicts[n] = "FOLLOWS ONLY IF THE CAUSE IS GRANTED"
                report.append(head + "\nFOLLOWS ONLY IF THE CAUSE IS GRANTED. Nothing else in the ledger supports: %s." % cause); found += 1; continue
            verdicts[n] = "JUMP"
            text = head + "\nJUMP. Even granting the stated cause, nothing in the ledger produces %s." % effect
            # D4: the lines the jump was measured against, so the reader can see what was searched
            text += listed_lines(meta, "Claim line", [n])
            text += listed_lines(meta, "Cause's lines", cause_lines, "(no line supports the cause)")
            text += listed_lines(meta, "Effect's direct lines", direct)
            text += general_block("produce", effect, direct)   # L86 D5
            # name the missing line: let the checker assume lines nobody wrote, and report which ones it needed
            abduce = supposed + "#abducible missing(X).\nholds(X) :- missing(X).\n"
            candidates = sorted({m for r in ask("produced(%s)" % effect, removed=direct, extra=abduce)
                                   for m in re.findall(r"would be needed: (\w+\((?:[^()]|\([^()]*\))*\)|\w+)", r["tree"])})
            good, rejected = [], []
            for candidate in candidates:
                if re.search(r"\b[A-Z_]\w*", candidate): continue                     # not a definite line (still has a blank in it)
                if ask("denied(%s)" % candidate): rejected.append(candidate); continue    # limit on filling in: must not contradict the ledger
                if ask("produced(%s)" % effect, removed=direct, extra=supposed + "holds(%s).\n" % candidate): good.append(candidate)
            if good: text += "\nA single line that would close the jump, which nobody wrote: " + "; or: ".join(good)
            if rejected: text += "\nLines that would also close it but are ruled out, because the ledger denies them: " + "; ".join(rejected)
            report.append(text); found += 1
        done("because claims", found)

        # ---- check 2b (PATCH 6, forced by the owner's Markus paragraph): SINCE. A reason to EXPECT something, not a cause of it.
        # Tested on what follows by ANY route (what SHOWS as well as what MAKES), and reported with its unstated assumptions.
        begin("since claims")
        supports, found = [], 0
        for claim in ask("claim_since(N, E, C)"):
            n, expected, reason = claim["bindings"]["N"], claim["bindings"]["E"], claim["bindings"]["C"]
            head = 'SINCE-claim on %s: "%s". (A reason to expect, not a cause.)' % (named_line(meta, n), meta["lines"][n]["text"])   # D4
            direct = sorted({r["lines"][0] for r in ask("holds(%s)" % expected) if len(r["lines"]) == 1})
            reason_lines = sorted({l for r in ask("holds(%s)" % reason) for l in r["lines"] if len(r["lines"]) <= 2})
            routes = [r for r in ask("holds(%s)" % expected, removed=direct) if set(reason_lines) & set(r["lines"])]
            if routes:
                route = min(routes, key=lambda r: len(r["lines"]))
                text = head + "\nTO BE EXPECTED, using:\n" + describe_lines(meta, route["lines"])
                if route["assumptions"]: text += "\nBUT ONLY ON ASSUMPTIONS NOBODY STATED:\n" + "\n".join("  - there is no evidence that " + a for a in route["assumptions"])
                text += "\nA habit or a pattern tells you about the occasions it was drawn from. Whether this occasion is like them is for you to judge."
                if guessed_lines(meta, route["lines"]): text += "\nNOTE: leans on lines you did not write: %s." % ", ".join(guessed_lines(meta, route["lines"]))
                supports.append((n, expected, reason, True, direct, route["lines"]))
            else:
                text = head + "\nNO CONNECTION. Nothing in the ledger leads from the reason to what is expected."
                # D4: the lines the search ran over
                text += listed_lines(meta, "Claim line", [n])
                text += listed_lines(meta, "Reason's lines", reason_lines)
                text += listed_lines(meta, "Expected's direct lines", direct)
                text += routes_block(expected, direct, reason_lines)              # L86 D6
                text += general_block("reach", expected, direct, reason=reason)   # L86 D6
                abduce = "#abducible missing(X).\nholds(X) :- missing(X).\n"
                cands = sorted({m for r in ask("holds(%s)" % expected, removed=direct + [l for l in meta["lines"] if l not in reason_lines and meta["lines"][l].get("habit")], extra=abduce)
                                for m in re.findall(r"would be needed: (\w+\((?:[^()]|\([^()]*\))*\)|\w+)", r["tree"])})
                text += "\nIt would take a line nobody wrote, of this kind: a general line saying that someone who %s does %s." % (reason, expected)
                supports.append((n, expected, reason, False, direct, []))
            report.append(text); found += 1
        done("since claims", found)
        # PATCH 7 (forced by the owner's Mondays paragraph; corrected after it broke the Markus report): a CHAIN of reasons.
        # The final conclusion is the one argued for last. A conclusion stands if ANY step for it holds (two routes to one job).
        # A step that connects, but only by leaning on the bare statement of an earlier conclusion that failed, inherits the break.
        begin("the chain")
        empty_input["the chain"] = not supports
        if supports:
            ordered = sorted(supports, key=lambda s: int(s[0]) if s[0].isdigit() else 0)
            final = ordered[-1][1]
            stands, failed_direct, rows, first_break, held = {}, set(), [], None, 0
            for n, e, c, ok, direct, route_lines in ordered:
                if not ok: state = "NO CONNECTION"
                elif set(route_lines) & failed_direct: state = "connects, BUT ONLY BY LEANING ON A CONCLUSION THAT ALREADY FAILED (line %s)" % ", ".join(sorted(set(route_lines) & failed_direct))
                else: state = "holds"
                if state == "holds": held += 1; stands[e] = True
                else:
                    stands.setdefault(e, False)
                    if first_break is None: first_break = n
                rows.append("  %s: %s  ->  %s" % (named_line(meta, n), meta["lines"][n]["text"], state))   # D4
                if not stands[e]: failed_direct |= set(direct)
                else: failed_direct -= set(direct)
            text = "THE CHAIN, step by step:\n" + "\n".join(rows)
            text += "\nTHE FINAL CONCLUSION, the one argued for last: %s.\n%d of %d steps hold. " % (final, held, len(ordered))
            if first_break: text += "The first step that fails is line %s. " % first_break
            text += "The final conclusion %s." % ("STANDS" if stands.get(final) else "DOES NOT STAND on this chain")
            spare = [n for n, e, _, ok, _, _ in ordered if e == final and not ok]
            if stands.get(final) and spare: text += "\n  Line(s) %s offer a reason that does not connect. Take it out and the conclusion stands exactly as before. It may be true, and it may matter to you, but it is doing no work in this argument." % ", ".join(spare)
            report.append(text)
        done("the chain", 1 if supports else 0)

        # ---- check 3: plans ----
        begin("plans")
        found = 0
        for claim in ask("claim_plan(N, A, F)"):
            n, action, fact = claim["bindings"]["N"], claim["bindings"]["A"], claim["bindings"]["F"]
            head = 'PLAN on %s: "%s".' % (named_line(meta, n), meta["lines"][n]["text"])   # D4
            works = ask("achieves(%s, %s)" % (action, fact))
            if works:
                text = head + "\nThe action does touch something the goal depends on, using:\n" + describe_lines(meta, works[0]["lines"])
                touched = {c["bindings"]["X"] for c in ask("changes(%s, X)" % action)}
                if touched & circle_causes: text += "\nBUT the plan acts on %s, whose only support is the CIRCLE found above." % ", ".join(sorted(touched & circle_causes))
                if guessed_lines(meta, works[0]["lines"]): text += "\nNOTE: leans on lines you did not write: %s." % ", ".join(guessed_lines(meta, works[0]["lines"]))
                report.append(text); found += 1
            else:
                why = ask("not achieves(%s, %s)" % (action, fact))
                changed = ask("changes(%s, X)" % action)
                reaches = ask("depends_on(%s, X)" % fact)
                if not changed or not reaches:
                    report.append(head + "\nCANNOT TELL whether the plan can work. The ledger says nothing about %s. The text gives the aim, and leaves the route from the action to the aim unstated." % ("what the action changes" if not changed else "what the aim depends on")
                                  + listed_lines(meta, "Plan line", [n]))   # D4
                    found += 1
                    continue
                text = head + "\nKIND MISTAKE (the plan cannot work as written). "
                text += "Doing %s changes only: %s. " % (action, ", ".join(sorted({c["bindings"]["X"] for c in changed})) or "nothing the ledger knows of")
                text += "But %s depends only on: %s. These do not meet." % (fact, ", ".join(sorted({r["bindings"]["X"] for r in reaches})) or "nothing the ledger knows of")
                used = sorted({l for c in changed + reaches for l in c["lines"]})
                text += "\nLines used:\n" + describe_lines(meta, used)
                if guessed_lines(meta, used): text += "\nNOTE: leans on lines you did not write: %s. If they are wrong, ignore it." % ", ".join(guessed_lines(meta, used))
                text += "\n(The checker's own proof that the plan fails was %s.)" % ("found" if why else "NOT found")
                report.append(text); found += 1
        done("plans", found)

        # ---- check 4: an exception to a "usually" line, with no reason given ----
        begin("exceptions")
        shortest, found = {}, 0
        for answer in ask("exception(N, X)"):                                   # keep one answer per exception: the one using fewest lines
            key = (answer["bindings"]["N"], answer["bindings"]["X"])
            if key not in shortest or len(answer["lines"]) < len(shortest[key]["lines"]): shortest[key] = answer
        for answer in shortest.values():
            n, thing = answer["bindings"]["N"], answer["bindings"]["X"]
            explains_something_observed = any(n in lines for _, lines in observed_claims)
            has_reason = bool(ask("exception_reason(%s, %s, R)" % (n, thing)))
            if meta["lines"][n]["mark"] == "usual case" and not has_reason:
                # PATCH 4 (forced by paragraph F): the writer's own sentence goes against what usually happens
                said = [l for l in answer["lines"] if meta["lines"][l]["mark"] == "said"]
                report.append('DEPARTURE FROM THE USUAL, NO REASON GIVEN. You said:\n%s\nThis goes against usual-case line %s ("%s"), and nothing in the ledger says why it happened here. In a story this may be exactly what you intend. If so, ignore it.\nNOTE: line %s is a usual-case line you did not write. If it is wrong, ignore this.' % (describe_lines(meta, said), n, meta["lines"][n]["text"], n))
                found += 1
            elif explains_something_observed and not has_reason:
                report.append('UNEXPLAINED EXCEPTION: line %s ("%s") is a "usually" line, and %s is an exception to it, but the ledger gives no reason why. Until there is a reason, nothing tells %s apart from the other cases line %s is used for.' % (n, meta["lines"][n]["text"], thing, thing, n))
                found += 1
        done("exceptions", found)

        # ---- check 5 (PATCH 5, forced by paragraph F, fitted to that one paragraph): likeness between two events ----
        begin("likeness")
        found = 0
        for claim in ask("claim_like(N, A, B)"):
            n, first, second = claim["bindings"]["N"], claim["bindings"]["A"], claim["bindings"]["B"]
            kinds_found = {first: set(), second: set()}
            for item in world_blocks + report:
                kind_of_finding = re.match(r"[A-Z][A-Z ,\-]+", item)
                if not kind_of_finding or item.startswith(("BECAUSE", "PLAN", "LIKENESS")): continue
                for line_id in re.findall(r"line (\w+)", item):
                    event = meta["lines"].get(line_id, {}).get("event")
                    if event in kinds_found: kinds_found[event].add(kind_of_finding.group(0).strip(" ,"))
            shared = kinds_found[first] & kinds_found[second]
            text = 'LIKENESS claimed on line %s: "%s". You do not say what the two have in common.\n' % (n, meta["lines"][n]["text"])
            if shared: text += "What the checker finds in both: " + "; ".join(sorted(shared)) + ".\nIf that is the likeness you mean, the paragraph never says so. If you mean something else, the ledger cannot see it."
            else: text += "The checker finds nothing the two have in common."
            report.append(text); found += 1
        done("likeness", found)

        # ---- PATCH 8 (pile 2, F12): two "usually" lines pulling opposite ways. Neither wins unless the text says so.
        begin("two usually lines")
        empty_input["two usually lines"] = not usually_lines
        found = 0
        for fact in sorted({a["bindings"]["F"] for a in ask("holds(F)") if "F" in a["bindings"]}):
            if fact in seen or re.search(r"\b[A-Z_]\w*", fact): continue
            against = ask("denied(%s)" % fact)
            if not against: continue
            in_favour = ask("holds(%s)" % fact)
            if any(r["assumptions"] for r in in_favour) and any(r["assumptions"] for r in against):
                used = sorted(set(in_favour[0]["lines"]) | set(against[0]["lines"]))
                report.append("TWO 'USUALLY' LINES PULL OPPOSITE WAYS about %s. One gives it and one denies it, and the text gives neither the upper hand. The checker keeps both and settles nothing.\n%s" % (fact, describe_lines(meta, used)))
                found += 1
        done("two usually lines", found)

        # ---- PATCH 9 (pile 2, F14): an exemption may switch off a USUALLY line only
        begin("exemptions")
        found = 0
        for answer in ask("exempt(N, X)"):
            n = answer["bindings"]["N"]
            if "ALWAYS" in meta["lines"].get(n, {}).get("text", ""):
                report.append("EXEMPTION FROM AN 'ALWAYS' LINE: %s is said to be exempt from line %s, but line %s says ALWAYS. Either the line is really a USUALLY, or this is a case against it." % (answer["bindings"]["X"], n, n))
                found += 1
        done("exemptions", found)

        # ---- PATCH 10 (pile 2, F19): the limits on added lines now cover the translator's own lines, whatever their mark
        begin("added lines")
        said_lines = [l for l, v in meta["lines"].items() if v["mark"] == "said"]
        found, conclusions = 0, 0
        for kind_of_claim in ("claim_because", "claim_since"):
            for claim in ask("%s(N, E, C)" % kind_of_claim):
                conclusions += 1
                conclusion = claim["bindings"]["E"]
                alone = ask("holds(%s)" % conclusion, removed=said_lines)
                if alone:
                    report.append("ADDED LINES ALONE GIVE THE CONCLUSION %s. With every line you wrote taken out, it still follows, from:\n%s\nSo the added lines are doing the writer's work. Check them before trusting anything above." % (conclusion, describe_lines(meta, alone[0]["lines"])))
                    found += 1
        empty_input["added lines"] = not conclusions
        done("added lines", found)

        # ---- PATCH 11 and 13: what-ifs. WITHDRAW: nobody said it. MAKE NOT SO: it did not happen.
        # PATCH 13 (F22): results the ledger itself ties to the changed thing are set aside, so they cannot answer the question by simply still being there.
        # D2: what-ifs are not run inside a case.
        if world is None:
            begin("what-ifs")
            empty_input["what-ifs"] = not meta.get("whatifs", [])
            found = 0
            ties = {}
            def results_tied_to(fact):
                tied = []
                for c in ask("claim_because(N, E, C)"):
                    if c["bindings"]["C"] == fact:
                        for r in ask("holds(%s)" % c["bindings"]["E"]):
                            if len(r["lines"]) == 1:
                                tied.append(r["lines"][0])
                                if c["bindings"]["N"] not in ties.setdefault(r["lines"][0], []):
                                    ties[r["lines"][0]].append(c["bindings"]["N"])   # D3: the line that ties this result to what was changed
                return sorted(set(tied))
            for w in meta.get("whatifs", []):
                ties.clear()   # D3: the tying line is the one that ties a set-aside line to what THIS what-if changed
                # D4: a what-if head names its own line when the ledger gives one
                whose = 'WHAT-IF [%s]' % w.get("whose", "?")
                if w.get("line") in meta["lines"]:
                    whose = 'WHAT-IF [%s] (line %s, sentence %s)' % (w.get("whose", "?"), w["line"], meta["lines"][w["line"]]["sentence"])
                if "withdraw" in w:
                    stated = [a["bindings"]["F"] for a in ask("holds(F)") if a["lines"] == [w["withdraw"]]]
                    aside = sorted({l for f in stated for l in results_tied_to(f)})
                    result = bool(ask(w["ask"], removed=[w["withdraw"]] + aside)); how = "WITHDRAW line %s (as if nobody had said it)" % w["withdraw"]
                else:
                    fact = w["make_not_so"]
                    direct = sorted({r["lines"][0] for r in ask("holds(%s)" % fact) if len(r["lines"]) == 1})
                    aside = results_tied_to(fact)
                    still = ask("holds(%s)" % fact, removed=direct)
                    if still:
                        report.append('%s: "%s"\n  THIS WHAT-IF CANNOT BE RUN AS STATED. You ask for %s to be not so, but these lines still produce it:\n%s\n  Say which of them gives way.' % (whose, w["text"], fact, describe_lines(meta, still[0]["lines"])))
                        found += 1
                        continue
                    result = bool(ask(w["ask"], removed=direct + aside, extra="denied(%s).\n" % fact)); how = "MAKE NOT SO: %s (as if it did not happen)" % fact
                text = '%s: "%s"\n  The change made: %s.' % (whose, w["text"], how)
                if aside:
                    text += "\n  Set aside, because your ledger says they came from what was changed: line(s) %s." % ", ".join(aside)
                    # D3: which line ties each set-aside line to what was changed, and how that line fared above
                    not_written = []
                    for line_id in aside:
                        tying = ties.get(line_id, [])
                        text += "\n  Set aside: %s (tied by %s)." % (named_line(meta, line_id), " and ".join(
                            "%s, whose verdict above is %s" % (named_line(meta, t), verdicts.get(t, "not reached")) for t in tying))
                        for x in [line_id] + tying:
                            if meta["lines"][x]["mark"] != "said" and x not in not_written: not_written.append(x)
                    if not_written: text += "\n  NOTE: leans on lines you did not write: %s." % ", ".join(not_written)
                report.append(text + "\n  Your what-if %s." % ("HOLDS" if result == w["claims"] else "FAILS"))
                found += 1
            done("what-ifs", found)

        # ---- PATCH 14 (F08): NOT on part of a line. "The jar broke, NOT [because it was dropped]."
        begin("denied because")
        found = 0
        for d in ask("denied_because(N, E, C)"):
            n, effect, cause = d["bindings"]["N"], d["bindings"]["E"], d["bindings"]["C"]
            direct = sorted({r["lines"][0] for r in ask("holds(%s)" % effect) if len(r["lines"]) == 1})
            cause_lines = sorted({l for r in ask("holds(%s)" % cause) for l in r["lines"]})
            through = [r for r in ask("produced(%s)" % effect, removed=direct) if set(cause_lines) & set(r["lines"])]
            head = 'DENIED BECAUSE on %s: "%s".' % (named_line(meta, n), meta["lines"][n]["text"])   # D4
            if through: text = head + "\nYOU DENY A CAUSE THAT YOUR OWN LINES SUPPLY. These lines make %s produce %s:\n%s" % (cause, effect, describe_lines(meta, through[0]["lines"]))
            else: text = head + "\nFine. Nothing in the ledger makes %s produce %s. The effect itself still stands; only the cause is denied." % (cause, effect)
            # D8: the same cause claimed and denied, effect and cause both the same
            for claimed_n, claimed_effect, claimed_cause in because_claims:
                if claimed_effect == effect and claimed_cause == cause:
                    text += "\nYOU CLAIM AND DENY THE SAME CAUSE: %s claims %s BECAUSE %s, and %s denies it." % (
                        named_line(meta, claimed_n), effect, cause, named_line(meta, n))
            report.append(text); found += 1
        done("denied because", found)

        # ---- D5: the outcomes block ----
        def reading(name):
            if out_of_time.get(name): return "ran out of time"
            if name in INPUT_DRIVEN:
                if empty_input.get(name): return "not asked, nothing to ask"
            elif name not in ALWAYS_ASKED and (NO_SUCH_PREDICATE in first_raw.get(name, "")
                                               or CHECK_PREDICATE.get(name) in no_such_kind):
                return "not asked, no line of that kind"
            return "asked, nothing found" if not counts.get(name) else "asked, %d found" % counts[name]
        outcomes = "\n".join(["OUTCOMES:"] + ["  %s: %s" % (name, reading(name))
                                              for name in OUTCOME_NAMES if not (world and name == "what-ifs")])
        return heading, world_blocks, report, outcomes, seen

    # ---- the actual ledger, with every case line taken out (D1) ----
    _, _, report, outcomes, seen = battery(all_case_lines)
    report.append(outcomes)

    # ---- PATCH 12 (F06, F09): named what-if cases. Each is looked at alone, on top of the actual ledger.
    for case_name, its_lines in cases.items():
        told = any(meta["lines"][l].get("case_kind") == "told" for l in its_lines)
        world_removed = [l for l in meta["lines"] if l not in its_lines] if told else [l for l in all_case_lines if l not in its_lines]
        heading, blocks, inside, world_outcomes, _ = battery(world_removed, (case_name, told, its_lines), seen)
        # D2: the same checks again with the actual ledger's general lines put back, to show what the world's
        # findings owe to being looked at alone. With no general lines to restore the second run cannot differ.
        restored = [l for l in world_removed if l not in general_lines]
        if len(restored) != len(world_removed):
            _, blocks_again, inside_again, _, _ = battery(restored, (case_name, told, its_lines), seen)
            again = [strip_blocks(f) for f in blocks_again + inside_again]   # L86 D7
            would_go = len([f for f in blocks + inside if strip_blocks(f) not in again])
        else:
            would_go = 0   # nothing to put back: the second run is the first one
        joined = bool(inside)   # D2: findings follow the contradiction inside this section
        section = heading if heading else world_body(blocks[0], joined)
        for block in (blocks if heading else blocks[1:]):
            section += "\n\n" + world_body(block, joined)
        for position, finding in enumerate(inside):
            section += ("\n" if position == 0 else "\n\n") + indented(finding)
        section += "\n  %d findings inside '%s' would not stand if the actual ledger's general lines were available." % (would_go, case_name)
        section += "\n" + indented(world_outcomes)
        report.append(section)

    # ---- the gauge ----
    marks = [v["mark"] for v in meta["lines"].values()]
    gauge = "GAUGE: %d lines said, %d filled in, %d usual case; %d bin entries over %d sentences (not checked)%s. Slowest question: %.2f seconds." % (
        marks.count("said"), marks.count("filled in"), marks.count("usual case"), len(meta["leftover"]), len(meta["sentences"]),
        (": " + "; ".join(meta["leftover"])) if meta["leftover"] else "", slowest[0])
    # D7: four counts below the gauge line, all of them the translator's own fields
    structured = meta.get("bin") if isinstance(meta.get("bin"), list) else None
    binned = sorted({e["sentence"] for e in structured if isinstance(e.get("sentence"), int) and not isinstance(e.get("sentence"), bool)}) if structured is not None else []
    gauge += "\n  bin sentences: %s" % (len(binned) if structured is not None else "not recorded (free-text bin)")
    carried = {str(v["sentence"]) for v in meta["lines"].values()}
    no_line = [s for s in meta["sentences"] if s not in carried]
    gauge += "\n  sentences with no line: %d" % len(no_line)
    gauge += "\n  sentences with no line and no bin entry: %s" % (
        len([s for s in no_line if s not in {str(b) for b in binned}]) if structured is not None else "not recorded")
    gauge += "\n  filled in against said: %d/%d" % (marks.count("filled in"), marks.count("said"))
    # D5: the NO FAULT FOUND line is gone; the outcomes block says what was asked and what was found.
    return "REPORT for paragraph %s\n\n" % meta["paragraph"] + "\n\n".join(report) + "\n\n" + gauge + "\n"

if __name__ == "__main__":
    with open(sys.argv[2], "a") as log:
        print(check(sys.argv[1], log))
