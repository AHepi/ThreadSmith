#!/usr/bin/env python3
"""Self-check for the A3 fourth-clause collection. Sends nothing anywhere.

Two jobs:
  1. evidence.json parses, and its W10.3 counts agree with the per-record levels.
  2. every quotation this collection tags *seen* (a sentence of a file in this
     repository) is present in that file verbatim, byte for byte.

Job 2 is the one that matters. A collector who quotes a repository file from memory
is running on *recalled* evidence and calling it *seen*; this program is what stops
that. Run:  python3 check.py
Exit code 0 only if every check passes.
"""

import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))

F11 = os.path.join(
    REPO, "Semantics", "authority",
    "11 Claude Fable Semantics - standalone theory, revision 1.md")
W8 = os.path.join(
    REPO, "Workflow", "authority",
    "W8 Model - an LLM agent in the language of the semantics, file 11 (frozen).md")
W10 = os.path.join(
    REPO, "Workflow", "tests",
    "W10 Plan - getting the LLM theory right; the harness, the corpus, "
    "the fourth clause, the instrument, the arms, the cross-examination.md")
SKILL = os.path.join(
    REPO, "HV Skill", "authority", "33", "hard-to-vary", "SKILL.md")
WORDLIST = os.path.join(
    REPO, "HV Skill", "authority", "33", "hard-to-vary", "references", "word-list.md")
CASES = os.path.join(
    REPO, "HV Skill", "authority", "33", "hard-to-vary", "references",
    "testing-against-cases.md")

# Every *seen* quotation used in evidence.md / evidence.json / predictions.md,
# with the file it is claimed to come from.
SEEN = [
    (F11, r"No member of the history represents \(t\), \(H\), or the survival condition."),
    (F11, r"The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over"),
    (F11, r"\(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\)."),
    (F11, r"\(B\) is a set of boundary conditions."),
    (F11, r"An **occurrence** is a physically located carrier."),
    (F11, r"a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered"),
    (F11, r"A selected provenance \(\operatorname{Sel}(t;\mathcal T,\mu,H)\) is a claim about a physical history: a population of realized transports, a physically admitted variation operator, and a survival condition enacted by the environment. It is fallible and checkable as any physical claim is."),
    (F11, r"Neither provenance is reducible to the other: a selected transport has no represented target and no criticism in its history; a constructed one has both."),
    (F11, r"A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does."),
    (F11, r"The carrier–content relation is thus a fidelity fact with a history."),
    (F11, r"**Constructed.** There is an episode (Part X) whose construction witness prepares \(t\), and in which \(t\), or the organization it targets, is available as a represented target."),
    (F11, r"A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \(\Omega\) (what makes it the same system through change)."),
    (F11, r"An occurrence \(o\) **represents** content \(c\) at grain \(\ell\) when the organization that \(o\) instantiates under the physical module, at grain \(\ell\), admits a transport to \(c\) that is faithful on \(c\)'s contract and whose provenance is selected or constructed"),
    (F11, "Selection is a physical history: a population, a variation operator, a survival condition and a sequence of events (Parts IV, XII)."),

    (W8, "If the clause fails, the provenance is neither selected nor constructed, so by the trichotomy it is declared, and a declared transport makes no occurrence represent anything."),
    (W8, "a showing that the strict reading is right, in which case the clause does no work anywhere in the theory and the finding is an ask for the Semantics project, never a change made from here"),
    (W8, "Held if the fourth clause of the same definition holds (A6), and held if the independence premise of Derivation 3's proof is read as file 11 now reads it."),
    (W8, "a trainer's record showing the corpus contains no such occurrence, in which case A6 collapses into A5"),
    (W8, "Neither check is a run this repository can make."),
    (W8, "the record, the corpus and the owner are outside it"),
    (W8, "A target may come from the weights, and a rival may be built from the problem in the context"),

    (W10, "at least one open trainer's record states that its corpus contains texts of the kind the fourth clause forbids, with the sentence quoted; zero falsifies the physical reading's reach from here and the clause stays unknown."),

    (SKILL, "run it on the very thing it is meant to catch, and on that thing's nearest innocent neighbour. A test that both pass is measuring something else."),
    (SKILL, "Looking before writing down what would count against you.** Research done with no predictions written first can only ever agree with you."),
    (WORDLIST, "fitted | selected provenance | Part IV"),
    (CASES, '**"Found nowhere" means unknown.**'),
]


def check_quotations():
    cache, bad = {}, []
    for path, quote in SEEN:
        if path not in cache:
            if not os.path.exists(path):
                bad.append((os.path.basename(path), "FILE MISSING", quote[:60]))
                cache[path] = ""
                continue
            with open(path, encoding="utf-8") as fh:
                cache[path] = fh.read()
        if quote not in cache[path]:
            bad.append((os.path.basename(path), "NOT FOUND VERBATIM", quote[:90]))
    return bad


def check_json():
    faults = []
    with open(os.path.join(HERE, "evidence.json"), encoding="utf-8") as fh:
        d = json.load(fh)
    w = d["w10_3"]
    for key, level in [
        ("level_A_universal_quantification_over_a_named_source", "A"),
        ("level_B_names_a_source_without_quantifying_its_contents", "B"),
    ]:
        listed = set(w[key]["records"])
        actual = {r["id"] for r in d["records"] if r.get("level") == level}
        if listed != actual:
            faults.append(
                "w10_3 %s lists %s but records carry %s"
                % (key, sorted(listed), sorted(actual)))
        if w[key]["count"] != len(listed):
            faults.append("w10_3 %s count %d != %d listed"
                          % (key, w[key]["count"], len(listed)))
    if w["level_C_states_that_a_NAMED_DOCUMENT_of_that_kind_is_in_the_corpus"]["count"] != 0:
        faults.append("level C count is not 0; the text of evidence.md says it is")
    excluded = {e["record"] for e in w.get("excluded_from_the_count_and_why", [])}
    for r in d["records"]:
        if r.get("level") == "B-subsumed" and r["id"] not in excluded:
            faults.append("record %s is B-subsumed but not listed as excluded" % r["id"])
    ids = [r["id"] for r in d["records"]]
    if len(ids) != len(set(ids)):
        faults.append("duplicate record ids")
    for r in d["records"]:
        if r.get("tag") == "claimed" and not (
                r.get("address") or any("address" in q for q in r.get("quotations", []))):
            faults.append("record %s is claimed with no address" % r["id"])
    return faults


def main():
    bad = check_quotations()
    faults = check_json()
    for f, why, q in bad:
        print("QUOTATION FAULT  %-22s %s  ::  %s" % (why, f, q))
    for f in faults:
        print("JSON FAULT       %s" % f)
    if not bad and not faults:
        print("all %d seen-quotations found verbatim; evidence.json consistent"
              % len(SEEN))
        return 0
    print("\n%d quotation fault(s), %d json fault(s)" % (len(bad), len(faults)))
    return 1


if __name__ == "__main__":
    sys.exit(main())
