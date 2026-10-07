#!/usr/bin/env python3
"""The records job's mechanical half: fill a template from facts Opus wrote, and check a draft against those facts.

  python3 -B records.py render --template T.md --values V.json --out OUT.md
      Fills every {{name}} slot of the template from V.json. Refuses a slot with no value and a value with no slot.
  python3 -B records.py check --draft D.md --facts F.json [--max-words 250]
      Takes from the draft every token that states a fact: md5s and commit hashes (hex runs of 7 or more), numbers,
      line numbers (L17), claim, invention, decision and log ids (FC30.new1, I165, S41, S104), quoted file names in
      backticks. Each must stand in the facts file (anywhere in its JSON). A token that does not is listed as
      UNSUPPORTED: the draft says something the facts do not give. Also: S95 residue hits on decision S23's list,
      and the word count. ok = nothing unsupported, no S23-list hit, not over the limit.
The facts, and whether the draft says what matters, are Opus's; this only catches a draft that adds a fact or alters
one into a value the facts do not hold anywhere. A fact moved to the wrong place ("6 not tested" where the facts say 7,
and 6 stands elsewhere in them) is not caught: Opus reads every draft.
"""
import argparse
import json
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import hcommon as H  # noqa: E402
import text_scan  # noqa: E402

SLOT = re.compile(r"\{\{\s*([A-Za-z0-9_]+)\s*\}\}")
TOKENS = [
    ("hex", re.compile(r"\b[0-9a-f]{7,40}\b")),
    ("id", re.compile(r"\b(?:FC\d+(?:\.new\d+|\.\d+)?|FC-E\d+|CT\d+|I\d{2,3}|S\d{1,3}|L\d{1,3}|D\d+\.\w+|Q\d+|O\d)\b")),
    ("number", re.compile(r"(?<![\w.])\d(?:[\d,]*\d)?(?:\.\d+)?(?![\w])")),
    ("file", re.compile(r"`([^`]+\.(?:md|json|py|txt))`")),
]


def flat(obj):
    return json.dumps(obj, ensure_ascii=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["render", "check"])
    ap.add_argument("--template")
    ap.add_argument("--values")
    ap.add_argument("--out")
    ap.add_argument("--draft")
    ap.add_argument("--facts")
    ap.add_argument("--max-words", type=int, default=250)
    a = ap.parse_args()
    if a.cmd == "render":
        t = H.read_text(a.template)
        v = H.load_json(a.values)
        slots = SLOT.findall(t)
        missing = sorted({s for s in slots if s not in v})
        unused = sorted(set(v) - set(slots))
        if missing or unused:
            H.emit(dict(ok=False, job="records_render", slots_without_value=missing, values_without_slot=unused))
        out = SLOT.sub(lambda m: str(v[m.group(1)]), t)
        H.write_text(a.out, out)
        H.emit(dict(ok=True, job="records_render", out=H.rel(a.out), slots_filled=len(slots), words=len(out.split())))
    d = H.read_text(a.draft)
    facts = flat(H.load_json(a.facts))
    # the facts' own tokens, found by the same patterns: a draft's token must be one of them (not a piece of one)
    have = {kind: {(m.group(1) if m.groups() else m.group(0)).replace(",", "") for m in rx.finditer(facts)}
            for kind, rx in TOKENS}
    have["number"] |= {x for x in have["hex"]}
    unsupported, seen = [], set()
    for kind, rx in TOKENS:
        for m in rx.finditer(d):
            tok = m.group(1) if m.groups() else m.group(0)
            if (kind, tok) in seen:
                continue
            seen.add((kind, tok))
            if tok.replace(",", "") in have[kind] or (kind == "file" and tok in facts):
                continue
            unsupported.append(dict(kind=kind, token=tok))
    lines = d.split("\n")
    hits = [dict(line=k, word=x.group(0), family=text_scan.m95().family(x.group(0).lower()))
            for k, l in enumerate(lines, 1) for x in text_scan.m95().BIG.finditer(l)]
    s23 = [h for h in hits if h["family"] in H.S23_FORBIDDEN]
    words = len(d.split())
    H.emit(dict(ok=not unsupported and not s23 and words <= a.max_words, job="records_check", draft=H.rel(a.draft),
                words=words, max_words=a.max_words, unsupported=unsupported, s23_list_hits=s23,
                s95_hits_other=len(hits) - len(s23)))


if __name__ == "__main__":
    main()
