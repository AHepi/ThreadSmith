#!/usr/bin/env python3
"""S103 records: quotation check.

Checks the S103 record files written after the reading (the results file, the
plain-words file 103, and the S103 entries of the two project stories) against
their sources:

1. every code span that gives a reader's closing line stands, byte for byte, on
   the reply line it is cited to;
2. every "Old (Lnnn)" / "New (Lnnn)" wording, and every "Old:" / "New:" whole
   line, stands on that line of file 99 / file 103;
3. every stretch in straight double quotes of three words or more (a stretch
   with an ellipsis piece by piece; the name of a heading of the same file is
   skipped as a cross-reference) is searched for in the sources (file 99, file 103, the six replies, the owner's decisions,
   the reading rule, the tabulation, the rulings, the critical review, the cases
   file, the apply output, and the list of what was removed for file 99); a stretch not found is listed for reading by eye (a nested quotation,
   a label or a stretch quoted from a record outside this list).

It reads only; it writes nothing. Run from anywhere: python3 "records - quotation check.py"
"""
import glob, hashlib, os, re, sys

SEM = '/home/user/ThreadSmith/Semantics'
RD = SEM + '/results/S103 Round 1 - reading'
RET = SEM + '/results/S103 Round 1 - returns'
F99 = SEM + '/tests/99 The semantics, standing alone.md'
F103 = SEM + '/tests/103 The semantics, standing alone, after round 1.md'
TARGETS = [
    SEM + '/results/S103 Round 1 - what the readers found and what changed.md',
    SEM + '/plain words/103 Round 1 - what the readers found and what changed, in plain words.md',
]
STORIES = [SEM + '/records/Semantics - project story.md',
           SEM + '/records/Semantics - project story, in plain words.md']

def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

def read(p):
    return open(p, encoding='utf-8').read()

assert md5(F99) == '74f4a4c7619345747f4fa976ddac9548', 'file 99 changed'
assert md5(F103) == 'f31ebb1f050783f1a84f6136cec20fcd', 'file 103 changed'
L99 = read(F99).split('\n')
L103 = read(F103).split('\n')
REPLY = {os.path.basename(p).replace('.response.txt', ''): read(p).split('\n')
         for p in glob.glob(RET + '/*.response.txt')}
SOURCES = [read(F99), read(F103)] + ['\n'.join(v) for v in REPLY.values()]
SOURCES += [read(SEM + '/records/Semantics - Decisions.md'),
            read(SEM + '/results/S103 Round 1 - how the replies will be read, written before sending.md'),
            read(RD + '/tabulation.md'), read(RD + '/critical review.md'), read(RD + '/cases.md'),
            read(RD + '/apply - output.txt'),
            read(SEM + '/tests/99 The semantics, standing alone - what was removed.md')]
SOURCES += [read(p) for p in sorted(glob.glob(RD + '/rulings/*.md'))]
ALL = '\n'.join(SOURCES)

def s103_block(text):
    """The S103 entry of a story file: from its first line to the next heading or entry."""
    m = re.search(r'^(\*\*)?S103\. .*?(?=^(\*\*)?S10[4-9]\. |^## |\Z)', text, re.S | re.M)
    return m.group(0) if m else ''

fails = 0
unfound = []
checked = 0
for path in TARGETS + STORIES:
    if not os.path.exists(path):
        print('missing:', path); fails += 1; continue
    text = read(path)
    if path in STORIES:
        text = s103_block(text)
        if not text:
            print('no S103 entry yet in', os.path.basename(path)); continue
    # 1. closing lines
    for m in re.finditer(r'\((`)?(s103_vary_(?:mimo|glm)_\d)(`)?, line (\d+)\): (``? ?)(.*?)( ?``?)$', text, re.M):
        tag, n, body = m.group(2), int(m.group(4)), m.group(6)
        checked += 1
        if REPLY[tag][n - 1] != body:
            print('CLOSING LINE NOT ON ITS LINE:', tag, n, body[:80]); fails += 1
    # 2. old / new wordings
    for m in re.finditer(r'\*\*(Old|New) \(L(\d+)\):\*\* `(.*?)`$', text, re.M):
        which, n, body = m.group(1), int(m.group(2)), m.group(3)
        lines = L99 if which == 'Old' else L103
        checked += 1
        if body not in lines[n - 1]:
            print('WORDING NOT ON ITS LINE:', which, n, body[:80]); fails += 1
    for m in re.finditer(r'- \*\*(C\d\d), line (\d+)\.\*\*\n  - Old: `(.*?)`\n  - New: `(.*?)`', text):
        n = int(m.group(2)); checked += 2
        if m.group(3) != L99[n - 1] or m.group(4) != L103[n - 1]:
            print('WHOLE LINE NOT AS IN THE TEXTS:', m.group(1), n); fails += 1
    # 3. quoted stretches
    for m in re.finditer(r'"([^"\n]+?)"', text):
        q = m.group(1)
        if len(q.split()) < 3 or re.search(r'\.(md|py|txt|json)$', q):
            continue  # short, or a file path
        if re.search(r'^#+ ' + re.escape(q) + r'\s*$', text, re.M) or re.search(r'^#+ .*' + re.escape(q), read(path), re.M):
            continue  # a cross-reference to a heading of the same file, not a quotation
        checked += 1
        pieces = [x.strip() for x in q.split('…') if x.strip()]
        if not all(x in ALL for x in pieces):
            unfound.append((os.path.basename(path), q))

print('checked:', checked)
print('failures (closing lines, wordings):', fails)
print('quoted stretches of three words or more not found in the sources, for reading by eye:', len(unfound))
for f, q in unfound:
    print('  [%s] "%s"' % (f[:40], q[:160]))
sys.exit(1 if fails else 0)
