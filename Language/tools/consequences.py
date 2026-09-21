#!/usr/bin/env python3
"""Consequences: what follows from a ledger, and what changes when a line is taken out.

Uses the rig-1 driver's own run_query (same rules, flags, time limit). Asks each
predicate with a variable, keeps every binding, subtracts the facts that a line
states directly (clause heads guarded by line(N)), and reports the rest as
derived. Then repeats with each line removed and prints the difference.

Usage: consequences.py <ledger.pl> <raw_log_path> [--out DIR]
Nothing is written to the ledger or the rig.
"""
import importlib.util, json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
RIG1 = os.path.join(HERE, "..", "rigs", "rig 1 - arguments", "patched")
QUERIES = ["holds(X)", "produced(X)", "denied(X)", "contradiction(X)",
           "depends(X, Y)", "depends_on(X, Y)", "changes(X, Y)", "achieves(X, Y)",
           "kind(X, Y)", "exception(X, Y)"]

def load_driver():
    spec = importlib.util.spec_from_file_location("run_check", os.path.join(RIG1, "run_check.py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def stated_facts(pl_text):
    """Facts a line states directly: clause heads whose only body goal is line(N)."""
    out = set()
    for head, body in re.findall(r"^\s*([a-z_]+\([^:]*?\))\s*:-\s*([^.]+)\.", pl_text, re.M):
        if re.fullmatch(r"\s*line\(\w+\)\s*", body): out.add(norm(head))
    return out

def norm(t): return re.sub(r"\s+", "", t)

def bindings_to_fact(query, b):
    fact = query
    for var, val in b.items(): fact = re.sub(r"\b%s\b" % var, val, fact)
    return norm(fact)

def ask_all(rig, ledger_text, removed, log):
    facts = {}
    for q in QUERIES:
        answers, seconds, timed_out, raw = rig.run_query(ledger_text, q, removed_lines=removed)
        log.write("\n=== consequences | query: %s | removed: %s | %.2fs | timed out: %s ===\n%s\n" % (q, list(removed), seconds, timed_out, raw))
        if timed_out: facts[norm(q)] = "TIMED OUT"; continue
        for a in answers:
            if a["bindings"]: facts[bindings_to_fact(q, a["bindings"])] = a["lines"]
    return facts

def main():
    ledger_path, log_path = sys.argv[1], sys.argv[2]
    rig = load_driver()
    pl = open(ledger_path).read()
    meta = json.load(open(ledger_path.replace(".pl", ".json")))
    lines = list(meta["lines"].keys())
    said = stated_facts(pl)
    started = time.time()
    with open(log_path, "a") as log:
        full = ask_all(rig, pl, [], log)
        derived = {f: v for f, v in full.items() if f not in said}
        print("LEDGER %s: %d lines; %d facts stated directly; %d facts found; %d derived (not stated by any line)\n" % (meta["paragraph"], len(lines), len(said), len(full), len(derived)))
        print("DERIVED, ON THE FULL LEDGER:")
        for f, used in sorted(derived.items()): print("  %s   <- lines %s" % (f, ", ".join(used) if isinstance(used, list) else used))
        print("\nWHAT CHANGES WHEN ONE LINE IS TAKEN OUT:")
        total_delta = 0
        for lid in lines:
            without = ask_all(rig, pl, [lid], log)
            gone = sorted(set(full) - set(without)); new = sorted(set(without) - set(full))
            total_delta += len(gone) + len(new)
            info = meta["lines"][lid]
            print("  take out line %s [%s]: %s" % (lid, info["mark"], info["text"]))
            for f in gone: print("      no longer: %s" % f)
            for f in new: print("      now:       %s" % f)
            if not gone and not new: print("      nothing changes")
        print("\nTOTAL delta lines over %d removals: %d. Time: %.0f s." % (len(lines), total_delta, time.time() - started))

if __name__ == "__main__": main()
