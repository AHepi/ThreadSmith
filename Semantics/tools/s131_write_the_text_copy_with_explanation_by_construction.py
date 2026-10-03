#!/usr/bin/env python3
"""s131_write_the_text_copy_with_explanation_by_construction.py

What it does, in plain words: for log S131 (decision S86, "Knowledge doesn't need to be worked out, explanation does").
Writes a COPY of text 129 (the semantics after round 4 with Reading C and the graded survival condition written in,
itself a copy of text 107), as
  tests/131 The semantics, standing alone, after round 4, with Reading C and explanation by construction.md
with S130's smallest wording for the third decision written in (S130 results, section 4.1 and 4.3):
  "Account(E) and not Dec(t)" becomes "Account(E) and Con(t)" at text 107's L17, L49, L61 and L69;
  at L536 "with a transport whose provenance is not declared (Part IV)" becomes "... is constructed (Part IV)";
  at L47 (Argument 6) "every creative attribution requires it" becomes "every explanation and every creative
  attribution requires it".
A dated note is put at the top saying what was changed and why; text 129 follows it whole, its own note included. Each
change must match exactly once on its line or the script stops. Texts 107 and 129 are read, never written. The script
then checks, line by line, that apart from the new note only those six lines differ from text 129, and prints the md5s
of text 107 (which must stay c7af964c329ab7959243405d394e6574), text 129 and the new copy.

  python3 -B Semantics/tools/s131_write_the_text_copy_with_explanation_by_construction.py

Written 2 October 2026 by the one Opus 5.5 agent of log S131.
"""
import hashlib, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T107 = os.path.join(ROOT, 'tests', '107 The semantics, standing alone, after round 4.md')
T129 = os.path.join(ROOT, 'tests', '129 The semantics, standing alone, after round 4, with Reading C.md')
DST = os.path.join(ROOT, 'tests', '131 The semantics, standing alone, after round 4, with Reading C and explanation by construction.md')
MD5_107 = 'c7af964c329ab7959243405d394e6574'
OFFSET_129 = 12          # text 129's own note is its first 12 lines: text 107's line n is text 129's line n + 12

OLD_F = '\\(\\operatorname{Account}(\\mathcal E)\\land\\neg\\operatorname{Dec}(t)\\)'
NEW_F = '\\(\\operatorname{Account}(\\mathcal E)\\land\\operatorname{Con}(t)\\)'

CHANGES = [
    # (text-107 line, old, new, label)
    (17, OLD_F, NEW_F, 'S86-L17'),
    (47, 'and every creative attribution requires it.', 'and every explanation and every creative attribution requires it.', 'S86-L47'),
    (49, OLD_F, NEW_F, 'S86-L49'),
    (61, OLD_F, NEW_F, 'S86-L61'),
    (69, OLD_F, NEW_F, 'S86-L69'),
    (536, 'with a transport whose provenance is not declared (Part IV)', 'with a transport whose provenance is constructed (Part IV)', 'S86-L536'),
]

NOTE = """> **A copy, not the theory.** Log S131, 2 October 2026. This file is text 129, `tests/129 The semantics, standing alone, after round 4, with Reading C.md` (md5 {md5_129}; not written to), which is itself a copy of text 107 (`tests/107 The semantics, standing alone, after round 4.md`, md5 {md5_107}; not written to) with the owner's first two decisions written in (S83, Reading C; S84, the graded survival condition). Here the owner's third decision, S86, is written in at six of its lines, with the smallest wording S130 proposed (`results/S130 Knowledge, not explanation - the owner's objection against the sufficiency claim.md`, sections 4.1 and 4.3); nothing else is altered. The theory itself stays text 107 until the owner's word. This note is the first {k} lines; below it text 129 follows whole, its own 12-line note included, so text 129's line n is this file's line n + {k}, and text 107's line n is this file's line n + {k12}. The numbers inside text 129's own note count from its first line. Written by `tools/s131_write_the_text_copy_with_explanation_by_construction.py`, which checks that only the six lines below differ from text 129.
>
> **Why.** Decision S86, the owner's words: "Correct. Knowledge doesn't need to be worked out, explanation does." Said after plain file 130 put the choice: keep "explanation" for what was worked out, or keep the theory as it is. So "explanation" is kept for an account whose transport was constructed; an account whose transport was selected is a representation, what the owner calls knowledge (evolved knowledge where selected, created knowledge where constructed), and not an explanation; one whose transport was declared is no explanation, as before (S41, Q2). The test of an account, (E), is not touched and still takes no provenance.
>
> **Changes 1 to 4, at text 107's L17, L49, L61 and L69 (this file's lines {l17}, {l49}, {l61}, {l69}).** "\\(\\operatorname{{Account}}(\\mathcal E)\\land\\neg\\operatorname{{Dec}}(t)\\)" becomes "\\(\\operatorname{{Account}}(\\mathcal E)\\land\\operatorname{{Con}}(t)\\)", once on each line: in the constitutive conjecture (L17), in the answer to grievance 7 on mathematics (L49), in "where to attack" (L61), and in "Fallibility without error-as-work" (L69). S130 section 4.1 said "L17 (twice)"; L17 holds the formula once (its other mention of explanation, "the claim that it is an explanation there", has no formula), so it is changed once.
>
> **Change 5, at text 107's L536 (this file's line {l536}), (Suff).** "with a transport whose provenance is not declared (Part IV)" becomes "with a transport whose provenance is constructed (Part IV)".
>
> **Change 6, at text 107's L47 (this file's line {l47}), Argument 6, "You have replaced explanation with evolution."** "and every creative attribution requires it." becomes "and every explanation and every creative attribution requires it.", S130 section 4.3's wording (S130 called it two words; the words added are "every explanation and"). Why: with explanation reserved for what was constructed, the grievance is answered for explanation as well as for creativity.
>
> Not written in, though S130 named them: the formal core's D16.XV (the owner's condition as "Acc and not Con implies not Expl", and (Suff)'s defeat condition with "Acc and Con"), which is carried into the core copy in `results/S131 Explanation by construction carried into copies/`; the owner's two phrases as names of kinds (S130 section 4.2: not needed); any line Reading C asks of the defeat conditions ("explanation" read at the declared boundary, S129's proposal for L536, which the core copy carries but this text does not). Lines S86 reaches that are not changed (L13, L201, L211, L528, L538, L542) are set out in `results/S131 Explanation by construction carried into copies - what changes.md`. Part B stays held (S57).
"""


def md5(b):
    return hashlib.md5(b).hexdigest()


def main():
    raw107 = open(T107, 'rb').read()
    if md5(raw107) != MD5_107:
        sys.exit('text 107 is not the record (md5 %s)' % md5(raw107))
    raw129 = open(T129, 'rb').read()
    lines = raw129.decode('utf-8').split('\n')
    lines107 = raw107.decode('utf-8').split('\n')
    new = list(lines)
    changed129 = []
    for ln, old, rep, lab in CHANGES:
        i = ln + OFFSET_129 - 1
        # the line in text 129 must be text 107's line (none of the six was touched by S129)
        if new[i] != lines107[ln - 1]:
            sys.exit('%s: text 129 line %d is not text 107 L%d' % (lab, ln + OFFSET_129, ln))
        if new[i].count(old) != 1:
            sys.exit('%s: expected exactly one match at text 129 line %d, found %d' % (lab, ln + OFFSET_129, new[i].count(old)))
        new[i] = new[i].replace(old, rep)
        changed129.append(ln + OFFSET_129)
    # nowhere else in text 129 does the formula or the L536 phrase occur
    rest = '\n'.join(l for j, l in enumerate(new) if j + 1 not in changed129)
    assert OLD_F not in rest and 'provenance is not declared' not in rest
    probe = NOTE.format(md5_129=md5(raw129), md5_107=md5(raw107), k=0, k12=0, l17=0, l47=0, l49=0, l61=0, l69=0, l536=0)
    k = probe.count('\n') + 1          # the note's lines and one blank line after it
    f = lambda n: n + OFFSET_129 + k
    note = NOTE.format(md5_129=md5(raw129), md5_107=md5(raw107), k=k, k12=k + OFFSET_129,
                       l17=f(17), l47=f(47), l49=f(49), l61=f(61), l69=f(69), l536=f(536))
    assert note.count('\n') + 1 == k
    out = note + '\n' + '\n'.join(new)
    open(DST, 'w', encoding='utf-8').write(out)
    got = open(DST, encoding='utf-8').read().split('\n')
    body = got[k:]
    assert len(body) == len(lines), (len(body), len(lines))
    diff = [i + 1 for i, (a, b) in enumerate(zip(lines, body)) if a != b]
    assert diff == sorted(changed129), diff
    for n in (17, 47, 49, 61, 69, 536):
        assert got[f(n) - 1] == body[n + OFFSET_129 - 1]
    print('text 107 md5 %s (unchanged on disk: %s)' % (md5(raw107), md5(open(T107, 'rb').read()) == MD5_107))
    print('text 129 md5 %s (%d lines; unchanged on disk: %s)' % (md5(raw129), len(lines), md5(open(T129, 'rb').read()) == md5(raw129)))
    print('copy     md5 %s (%d bytes, %d lines; note %d lines)' % (md5(open(DST, 'rb').read()), os.path.getsize(DST), len(got), k))
    print('lines that differ from text 129, in its numbering:', diff)
    print('the same, in text 107 numbering:', [d - OFFSET_129 for d in diff])
    print('the same, in this copy:', [d + k for d in diff])


if __name__ == '__main__':
    main()
