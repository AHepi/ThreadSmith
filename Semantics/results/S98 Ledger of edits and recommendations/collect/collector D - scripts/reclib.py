"""Helpers for recommendation records: verbatim extraction from a source file by anchors, and
placing a proposal in its target text (old_sentence, new_sentence)."""
import re
from lib import *


class Src:
    def __init__(self, rel):
        self.rel = rel
        self.text = open(SEM + rel, encoding="utf-8").read()

    def between(self, start, end, after=None, after2=None):
        """Verbatim text between the first `start` (searched from `after`, then `after2`) and the next `end`."""
        p0 = 0
        for a in (after, after2):
            if a:
                k = self.text.find(a, p0)
                if k < 0:
                    raise ValueError("anchor not found: %r" % a)
                p0 = k + len(a) if a != start else k
        i = self.text.find(start, p0)
        if i < 0:
            raise ValueError("start not found: %r (after %r)" % (start, after))
        i += len(start)
        j = self.text.find(end, i)
        if j < 0:
            raise ValueError("end not found: %r after %r" % (end, start))
        return self.text[i:j]


def sentences_of(line):
    st = sentence_starts(line)
    b = st[1:] + [len(line)]
    return [line[a:c].strip() for a, c in zip(st, b)]


def place(texts, tname, line, old, new, anchor=None):
    """Return (old_sentence, new_sentence, found) for a proposal on `line` of text `tname`."""
    L = texts[tname][line - 1] if line else ""
    if not L:
        return "", "", False
    buildable = new and "…" not in new and not new.startswith("[no wording given]")
    if old and L.count(old) >= 1:
        os_ = locate_sentence(L, old)
        ns_ = ""
        if buildable and L.count(old) == 1:
            nl, spans = apply_line(L, [(old, new, 0)])
            ns_ = sentences_for(L, nl, spans, 0)[1]
        return os_, ns_, True
    if not old and anchor and L.count(anchor) == 1:
        os_ = locate_sentence(L, anchor)
        ns_ = ""
        if buildable:
            nl, spans = apply_line(L, [(anchor, anchor + " " + new, 0)])
            ns_ = sentences_for(L, nl, spans, 0)[1]
        return os_, ns_, True
    return "", "", False


def rec(rid, rnd, src, ref, kind, status, applied_in, tname, line, H, old, new, os_, ns_, scope):
    return {"rid": rid, "round": rnd, "source_file": src, "source_ref": ref, "kind": kind,
            "status": status, "applied_in": applied_in, "target_text": tname, "target_line": line,
            "target_part": H.get(line, "") if line else "", "old": old, "new": new, "old_sentence": os_,
            "new_sentence": ns_, "scope": scope, "same_as": []}
