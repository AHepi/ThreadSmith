#!/usr/bin/env python3
"""Count and scan a text, or compare two line-aligned texts (before and after a change).

  python3 -B text_scan.py --file TEXT
  python3 -B text_scan.py --before OLD --after NEW

Counts: lines, words (split on white space), words outside formulas (\\( \\) and \\[ \\] stripped: round 2's rule).
Scans, reusing the project's own lists (nothing re-typed here):
  - the S95 residue families (FAMILIES and BIG of tests/S95 Scrub - scripts/scrub_apply.py): hits per line; with two
    texts, the hits NEW in the after text line by line, each with its family and whether it is on decision S23's list;
  - the S96 physical-tie words (PHYS of tests/S96 Repair - scripts/repair_apply.py): hits, and new ones;
  - headings, defined terms (**bold**) and labelled formulas (\\tag) of the before text missing from the after text.
A hit is a word found, not a finding: whether a new hit is allowed (e.g. the symbol Accepted_j, tentative by S23) is
decided by Opus. ok = no new S23-list hit, no heading/term/tag missing, and words outside formulas not grown.
"""
import argparse
import collections
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402

_M95 = _M96 = None


def m95():
    global _M95
    _M95 = _M95 or H.load_module(H.S95_SCRIPT, "s95_scrub_apply")
    return _M95


def m96():
    global _M96
    _M96 = _M96 or H.load_module(H.S96_SCRIPT, "s96_repair_apply")
    return _M96


def stats(lines):
    text = "\n".join(lines)
    return dict(lines_newline_count=text.count("\n"), words=len(text.split()), words_outside_formulas=len(H.prose(text)),
                s95_hits=sum(1 for l in lines for _ in m95().BIG.finditer(l)),
                s96_hits=sum(1 for l in lines for _ in m96().PHYS.finditer(l)),
                headings=sum(1 for l in lines if l.startswith("#")),
                defined_terms=sum(len(H.BOLD.findall(l)) for l in lines),
                labelled_formulas=sum(len(H.TAG.findall(l)) for l in lines))


def compare(old, new, deleted_terms=frozenset()):
    """old, new: lists of lines, aligned one to one. deleted_terms: {(line, term)} removed by a 'delete' change."""
    if len(old) != len(new):
        return dict(aligned=False, why="line counts differ: %d, %d" % (len(old), len(new)))
    s95_new, s96_new, missing = [], [], []
    for k, (a, b) in enumerate(zip(old, new), 1):
        ca = collections.Counter(x.group(0).lower() for x in m95().BIG.finditer(a))
        cb = collections.Counter(x.group(0).lower() for x in m95().BIG.finditer(b))
        for w, c in sorted((cb - ca).items()):
            fam = m95().family(w)
            s95_new.append(dict(line=k, word=w, count=c, family=fam, s23_list=fam in H.S23_FORBIDDEN))
        ca = collections.Counter(x.group(0).lower() for x in m96().PHYS.finditer(a))
        cb = collections.Counter(x.group(0).lower() for x in m96().PHYS.finditer(b))
        for w, c in sorted((cb - ca).items()):
            s96_new.append(dict(line=k, word=w, count=c))
        if a.startswith("#") and a != b:
            missing.append(dict(line=k, what="heading", text=a[:120]))
        bold_a = collections.Counter(m.group(1) for m in H.BOLD.finditer(a))
        bold_b = collections.Counter(m.group(1) for m in H.BOLD.finditer(b))
        for t in (bold_a - bold_b):
            if (k, t) not in deleted_terms:
                missing.append(dict(line=k, what="defined term", text=t))
        for t in (collections.Counter(H.TAG.findall(a)) - collections.Counter(H.TAG.findall(b))):
            missing.append(dict(line=k, what="labelled formula", text=t))
    sa, sb = stats(old), stats(new)
    return dict(aligned=True, lines_differing=sum(1 for a, b in zip(old, new) if a != b),
                before=sa, after=sb, words_delta=sb["words"] - sa["words"],
                words_outside_formulas_delta=sb["words_outside_formulas"] - sa["words_outside_formulas"],
                prose_not_grown=sb["words_outside_formulas"] <= sa["words_outside_formulas"],
                s95_new_hits=s95_new, s95_new_total=sum(h["count"] for h in s95_new),
                s95_new_on_s23_list=sum(h["count"] for h in s95_new if h["s23_list"]),
                s96_new=s96_new, s96_new_total=sum(h["count"] for h in s96_new), marks_missing=missing)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file")
    ap.add_argument("--before")
    ap.add_argument("--after")
    a = ap.parse_args()
    if a.file:
        t = H.read_text(a.file)
        H.emit(dict(ok=True, file=H.rel(a.file), md5=H.md5_file(a.file), **stats(t.split("\n"))))
    if not (a.before and a.after):
        H.refuse("give --file, or --before and --after")
    old, new = H.read_text(a.before).split("\n"), H.read_text(a.after).split("\n")
    c = compare(old, new)
    ok = c.get("aligned", False) and c["s95_new_on_s23_list"] == 0 and not c["marks_missing"] and c["prose_not_grown"]
    H.emit(dict(ok=ok, before_file=H.rel(a.before), before_md5=H.md5_file(a.before), after_file=H.rel(a.after),
                after_md5=H.md5_file(a.after), **c))


if __name__ == "__main__":
    main()
