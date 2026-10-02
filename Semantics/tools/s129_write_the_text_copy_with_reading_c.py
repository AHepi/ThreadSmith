#!/usr/bin/env python3
"""s129_write_the_text_copy_with_reading_c.py

What it does, in plain words: for log S129 (decisions S83 and S84), writes a COPY of the latest text of the semantics,
tests/107 The semantics, standing alone, after round 4.md, as
tests/129 The semantics, standing alone, after round 4, with Reading C.md,
with the owner's two decisions of 2 October 2026 written in at three lines (text 107's L193, L195, L522) and a dated
note at the top saying what was changed and why. Each change must match exactly once or the script stops. Text 107
is read, never written. The script then checks, line by line, that apart from the note and the three changed lines
the copy is text 107 unchanged, and prints both md5s.

  python3 -B Semantics/tools/s129_write_the_text_copy_with_reading_c.py

Written 2 October 2026 by the one Opus 5.5 agent of log S129.
"""
import hashlib, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'tests', '107 The semantics, standing alone, after round 4.md')
DST = os.path.join(ROOT, 'tests', '129 The semantics, standing alone, after round 4, with Reading C.md')

# S127, the hinge file, section 7, "For C" (text, L195, after the formula), word for word.
C_SENTENCES = (' The history of a holding is read inside the system boundary declared for the claim (Part XII). A process '
               'inside the boundary whose correspondence entered it whole from outside has, there, neither a selected nor a '
               'constructed history, and represents nothing there; what it carries is a contribution from outside the '
               'boundary (Part X, Ownership). A provenance is relative to the boundary declared, as a capability is, and the '
               'boundary is declared before the attribution, not chosen after it.')

CHANGES = [
    # (text-107 line, old, new, label)
    (193, 'determined by its history in the physical module:',
     'determined by its history in the physical module inside the declared boundary:', 'S83-L193'),
    (195, 'and a survival condition requiring fidelity on \\(H\\).',
     'and a survival condition under which fidelity on \\(H\\) changes which members persist or are copied (a requirement '
     'is one such condition; a higher rate of copying for members faithful on \\(H\\) is another).', 'S84-L195'),
    (195, '\\land\\neg[\\exists h\'\\subseteq h(t):\\ \\operatorname{CT}(h\',t)]\\) (D12.1).',
     '\\land\\neg[\\exists h\'\\subseteq h(t):\\ \\operatorname{CT}(h\',t)]\\) (D12.1).' + C_SENTENCES, 'S83-L195'),
    (522, 'the system boundary and continuity of an attribution (Part XII);',
     'the system boundary and continuity of an attribution (Part XII); the boundary of a provenance claim (Part IV);', 'S83-L522'),
]

NOTE = """> **A copy, not the theory.** Log S129, 2 October 2026. This file is an exact copy of `tests/107 The semantics, standing alone, after round 4.md` (md5 {md5_src}; not written to) with the owner's two decisions of 2 October 2026 written in at three of its lines; nothing else is altered. The theory itself stays text 107 until the owner's word. This note is the first {k} lines: every line of text 107 stands here {k} lines lower (text 107's L195 is this file's line {l195}). Written by `tools/s129_write_the_text_copy_with_reading_c.py`, which checks that only the three lines below differ.
>
> **Change 1, decision S83 ("Oh clearly C."), at text 107's L195 (this file's line {l195}).** After "(D12.1)." three sentences are written in, word for word as S127 proposed them for Reading C (`results/S127 The Avida findings turned back on the semantics - the hinge.md`, section 7): "The history of a holding is read inside the system boundary declared for the claim (Part XII). A process inside the boundary whose correspondence entered it whole from outside has, there, neither a selected nor a constructed history, and represents nothing there; what it carries is a contribution from outside the boundary (Part X, Ownership). A provenance is relative to the boundary declared, as a capability is, and the boundary is declared before the attribution, not chosen after it." Why: S83 decides that the history in the definition of a selected correspondence is read inside the system boundary declared for the claim.
>
> **Change 2, decision S83, at text 107's L193 (this file's line {l193}).** "determined by its history in the physical module" becomes "determined by its history in the physical module inside the declared boundary" (S127, section 7). Why: under Reading C a provenance is relative to the boundary declared.
>
> **Change 3, decision S83, at text 107's L522 (this file's line {l522}).** In the list of declared inputs, after "the system boundary and continuity of an attribution (Part XII);" the words "the boundary of a provenance claim (Part IV);" are added (S127, section 7, gives the words; the pointer "(Part IV)" is this copy's, in the list's own style). Why: under Reading C a provenance claim takes its boundary as a stated input; where it is missing, the assessment is left open, as for every declared input.
>
> **Change 4, decision S84 ("Well yes. That is how selected is defined."), at text 107's L195 (this file's line {l195}).** "a survival condition requiring fidelity on \\(H\\)" becomes "a survival condition under which fidelity on \\(H\\) changes which members persist or are copied (a requirement is one such condition; a higher rate of copying for members faithful on \\(H\\) is another)", S127's proposed wording in its smaller form (hinge file, section 7); the companion file's "at each stage of the history" is not written in, because with \\(H\\) a set of pairs there are no stages to quantify over (S128, P1), and S128's P1 is not applied. Why: S84 decides that being copied more often counts as surviving, because that is how selection is defined.
>
> Not written in, though proposed elsewhere: S127's sentence for L481 (an environment that copies some members faster than others); S128's P1 to P3; any change that Reading C asks of other lines (Deploy at L403, Enable at L495, the defeat conditions at L536): what it asks of them is set out in `results/S129 Reading C carried into copies - what changes.md`. L195 is in Part A's frozen set (S108); Part B stays held (S57).
"""


def md5(b):
    return hashlib.md5(b).hexdigest()


def main():
    raw = open(SRC, 'rb').read()
    lines = raw.decode('utf-8').split('\n')
    new = list(lines)
    for ln, old, rep, lab in CHANGES:
        s = new[ln - 1]
        if s.count(old) != 1:
            sys.exit('%s: expected exactly one match at L%d, found %d' % (lab, ln, s.count(old)))
        new[ln - 1] = s.replace(old, rep)
    # the note's length is fixed before the numbers are filled in (they do not change its line count)
    probe = NOTE.format(md5_src=md5(raw), k=0, l193=0, l195=0, l522=0)
    k = probe.count('\n') + 1          # the note's lines and one blank line after it
    note = NOTE.format(md5_src=md5(raw), k=k, l193=193 + k, l195=195 + k, l522=522 + k)
    assert note.count('\n') + 1 == k
    out = note + '\n' + '\n'.join(new)
    open(DST, 'w', encoding='utf-8').write(out)
    # check: drop the note, compare line by line
    got = open(DST, encoding='utf-8').read().split('\n')
    body = got[k:]
    assert len(body) == len(lines), (len(body), len(lines))
    diff = [i + 1 for i, (a, b) in enumerate(zip(lines, body)) if a != b]
    assert diff == [193, 195, 522], diff
    print('text 107 md5 %s (%d bytes, %d lines)' % (md5(raw), len(raw), len(lines)))
    print('copy     md5 %s (%d bytes, %d lines; note %d lines)' % (md5(open(DST, 'rb').read()), os.path.getsize(DST), len(got), k))
    print('lines that differ from text 107, in its numbering:', diff)
    print('text 107 unchanged on disk:', md5(open(SRC, 'rb').read()) == md5(raw))


if __name__ == '__main__':
    main()
