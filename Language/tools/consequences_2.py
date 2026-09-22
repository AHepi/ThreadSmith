#!/usr/bin/env python3
"""Consequences, second version: what follows from a ledger, world by world, and what
changes when a line is taken out.

Uses the rig-1 driver's own run_query (same rules, flags, time limit). Asks each
predicate with a variable, keeps every binding, sets aside the facts a single line
states, and reports the rest as derived. Then repeats with each line removed and
prints the difference. Then, for each named case in the ledger, prints that world's
facts under the case's own name.

Made from consequences.py (SHA-256 begins 782047f829cf6b39), beside it and leaving it
untouched, under plan L79 third version (SHA-256 begins 2e97300690dc39f7), the
`tools/consequences_2.py` paragraph and D1 for the run_query signature, with these
changes and no others. Each change is followed by the give-up line the plan records
for it.

  D1. The driver's question is now run_query(ledger_text, query, removed_lines,
      world_removed): world_removed is required and the module global WORLD_REMOVED is
      gone. This file loads the new driver, rigs/rig 1 - arguments/patched/run_check_2.py,
      and every call passes world_removed; ask_all takes it and forwards it.
      Gives up: every caller changes.
  W1. world_removed is every case line for the actual section, and per case as check()
      does: told, every line outside the case; supposed, every other case's lines.
      Gives up: the old regex; the old wording.
  W2. One section per world, under the case's own name, after the actual section.
      Gives up: the old regex; the old wording.
  W3. A found fact is "stated" when some justification for it uses exactly one line.
      The clause-head regex over the ledger's .pl text is gone.
      Gives up: the old regex; the old wording.
  W4. A fact under both `depends` and `depends_on` is printed once, as `depends`.
      Gives up: the old regex; the old wording.
  W5. The removal lines read `no change in the reported fact set` where they read
      `nothing changes`.
      Gives up: the old regex; the old wording.
  W6. Every line cited is cited in the fixed form with its sentence,
      `  - line g [mark, sentence N]: text`, the driver's own describe_lines.
      Gives up: the old regex; the old wording.

Choices recorded under rule 7, where the plan leaves the reading open. In each the
reading taken is the one that keeps the old findings' text as it was.

  C1 (W3, the test for "stated"). "Some justification for it uses exactly one line"
      reads two ways. Counting the distinct lines named anywhere in a justification
      makes depends_on(reading(thermometer),reached(the_cold,thermometer)) stated - its
      tree is depends_on because depends because line 11 - and leaves ledger A with
      seven derived facts. A4 requires eight, the old ten with the two depends_on twins
      gone and otherwise identical, so the other reading is taken: a fact is stated when
      some answer's justification has, below the fact itself, exactly one reason and
      that reason is "line N is in the ledger" with nothing under it. On ledger A that
      returns the old regex's set fact for fact, so every old derived line stands.
  C2 (W4, where the once-only rule bites). It is applied to the derived list a section
      prints, which is what A4 measures (the old ten less the two twins, exactly eight).
      The take-out block compares the whole reported fact set of two runs, as the old
      tool did, so its old lines stay byte-identical; a fact that goes there goes under
      both names, as before.
  C3 (W2, what a world section holds). A4 asks for "the story's facts" in the world
      section, and inside nora_story every fact is stated by one line, so a derived-only
      list would be empty. The section prints both lists: the world's facts stated by a
      line, then the world's derived facts.
  C4 (W2, the take-out walk inside a world). It is not run inside a world. D2 does not
      run the driver's take-out checks (patches 11 and 13) inside a case either, and the
      plan asks the tool only for one section per world. The walk stays the actual
      ledger's, over every ledger line, as it was.
  C5 (W6, where the fixed form goes). The old `   <- lines 1, 5` tail stays and the
      fixed form is printed under it, indented two further spaces; the take-out head
      keeps its old shape and gains `, sentence N` inside its brackets. The old text
      stands and every cited line carries its sentence.
  C6 (rule 7, the shape of the actual section). Its counts line, its take-out walk and
      its TOTAL line keep their old wording and their old order, and the world sections
      follow the TOTAL line. A ledger with no named case therefore reads as it did,
      apart from the changes above.

Usage: consequences_2.py <ledger.pl> <raw_log_path>
Nothing is written to the ledger or the rig.
"""
import importlib.util, json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
RIG1 = os.path.join(HERE, "..", "rigs", "rig 1 - arguments", "patched")
QUERIES = ["holds(X)", "produced(X)", "denied(X)", "contradiction(X)",
           "depends(X, Y)", "depends_on(X, Y)", "changes(X, Y)", "achieves(X, Y)",
           "kind(X, Y)", "exception(X, Y)"]
# W3: the whole reason under a fact, when one line is all there is to it.
ONE_LINE_REASON = re.compile(r"\s*line \w+ is in the ledger\s*[,.]?\s*")

def load_driver():
    """D1: the second driver, whose run_query takes world_removed."""
    spec = importlib.util.spec_from_file_location("run_check_2", os.path.join(RIG1, "run_check_2.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def states_directly(tree):
    """W3 (choice C1): a justification that is one line and nothing else.
    The driver hands back the answer's block with s(CASP)'s own rules kept, so the
    fact itself is the first line that is neither blank nor one of s(CASP)'s `%` lines;
    a fact a line states has exactly one reason under it, `line N is in the ledger`."""
    body = [l for l in tree.split("\n") if l.strip() and not l.lstrip().startswith("%")]
    return len(body) == 2 and ONE_LINE_REASON.fullmatch(body[1]) is not None

def norm(t): return re.sub(r"\s+", "", t)

def bindings_to_fact(query, b):
    fact = query
    for var, val in b.items(): fact = re.sub(r"\b%s\b" % var, val, fact)
    return norm(fact)

def once_only(facts):
    """W4: a fact under both `depends` and `depends_on` is printed once, as `depends`."""
    kept = {}
    for fact, used in facts.items():
        if fact.startswith("depends_on(") and fact.replace("depends_on(", "depends(", 1) in facts: continue
        kept[fact] = used
    return kept

def ask_all(rig, ledger_text, removed, world_removed, log, label):
    """D1: world_removed goes to every question. Returns (fact -> the lines used, the facts a line states)."""
    facts, said = {}, set()
    for q in QUERIES:
        answers, seconds, timed_out, raw = rig.run_query(ledger_text, q, removed, world_removed)
        log.write("\n=== consequences_2 | %s | query: %s | removed: %s | world removed: %s | %.2fs | timed out: %s ===\n%s\n"
                  % (label, q, list(removed), list(world_removed), seconds, timed_out, raw))
        if timed_out: facts[norm(q)] = "TIMED OUT"; continue
        for a in answers:
            if not a["bindings"]: continue
            fact = bindings_to_fact(q, a["bindings"])
            facts[fact] = a["lines"]
            if states_directly(a["tree"]): said.add(fact)
    return facts, said

def cited(rig, meta, line_ids, pad):
    """W6: every line cited in the fixed form with its sentence."""
    out = []
    for line_id in line_ids:
        if line_id in meta["lines"]: out.append(pad + rig.describe_lines(meta, [line_id]))
        else: out.append(pad + "  - line %s [not in the ledger's index]" % line_id)
    return out

def print_facts(rig, meta, facts, pad):
    for fact, used in sorted(facts.items()):
        print("%s  %s   <- lines %s" % (pad, fact, ", ".join(used) if isinstance(used, list) else used))
        if isinstance(used, list):
            for line in cited(rig, meta, used, pad + "  "): print(line)

def main():
    ledger_path, log_path = sys.argv[1], sys.argv[2]
    rig = load_driver()
    pl = open(ledger_path).read()
    meta = json.load(open(ledger_path.replace(".pl", ".json")))
    lines = list(meta["lines"].keys())
    # W1: the named cases, as check() reads them.
    cases = {}
    for line_id, info in meta["lines"].items():
        if info.get("case"): cases.setdefault(info["case"], []).append(line_id)
    all_case_lines = [l for ls in cases.values() for l in ls]
    started = time.time()
    with open(log_path, "a") as log:
        # ---- the actual ledger, with every case line taken out (D1, W1) ----
        full, said = ask_all(rig, pl, [], all_case_lines, log, "the actual ledger")
        derived = once_only({f: v for f, v in full.items() if f not in said})
        print("LEDGER %s: %d lines; %d facts stated directly; %d facts found; %d derived (not stated by any line)\n"
              % (meta["paragraph"], len(lines), len(said), len(full), len(derived)))
        print("DERIVED, ON THE FULL LEDGER:")
        print_facts(rig, meta, derived, "")
        print("\nWHAT CHANGES WHEN ONE LINE IS TAKEN OUT:")
        total_delta = 0
        for lid in lines:
            without, _ = ask_all(rig, pl, [lid], all_case_lines, log, "without line %s" % lid)
            gone = sorted(set(full) - set(without)); new = sorted(set(without) - set(full))
            total_delta += len(gone) + len(new)
            info = meta["lines"][lid]
            print("  take out line %s [%s, sentence %s]: %s" % (lid, info["mark"], info["sentence"], info["text"]))
            for f in gone: print("      no longer: %s" % f)
            for f in new: print("      now:       %s" % f)
            # W5: the removal lines read "no change in the reported fact set".
            if not gone and not new: print("      no change in the reported fact set")
        print("\nTOTAL delta lines over %d removals: %d. Time: %.0f s." % (len(lines), total_delta, time.time() - started))
        # ---- W2: one section per world, under the case's own name ----
        for case_name, its_lines in cases.items():
            told = any(meta["lines"][l].get("case_kind") == "told" for l in its_lines)
            # W1: the case's complement, as check() builds it.
            world_removed = [l for l in meta["lines"] if l not in its_lines] if told else [l for l in all_case_lines if l not in its_lines]
            here, here_said = ask_all(rig, pl, [], world_removed, log, "inside '%s'" % case_name)
            here_derived = once_only({f: v for f, v in here.items() if f not in here_said})
            here_stated = {f: v for f, v in here.items() if f in here_said}
            print("\n" + ("INSIDE '%s' (a told world, looked at alone): WHAT FOLLOWS FROM THE WORLD'S OWN LINES" % case_name
                          if told else
                          "UNDER THE SUPPOSITION '%s': WHAT FOLLOWS ONCE THE SUPPOSED LINES ARE ADDED" % case_name))
            print("  %d lines in the world; %d facts stated directly; %d facts found; %d derived (not stated by any line)"
                  % (len([l for l in lines if l not in world_removed]), len(here_said), len(here), len(here_derived)))
            print("  THE WORLD'S FACTS, EACH STATED BY ONE LINE:")
            if here_stated: print_facts(rig, meta, here_stated, "  ")
            else: print("    (none)")
            print("  DERIVED INSIDE '%s' (not stated by any line):" % case_name)
            if here_derived: print_facts(rig, meta, here_derived, "  ")
            else: print("    (none)")

if __name__ == "__main__": main()
