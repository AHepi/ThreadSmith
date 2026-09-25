#!/usr/bin/env python3
"""s93_verify.py - stage E: verify draft 5 by program.

1. Every entry whose OLD, NEW, KIND or DECLARATION differs between the draft-4 list (HEAD) and the draft-5 list (the
   working copy), and every added or removed entry, is one a ruling changed; no other entry's fields differ.
2. The ruled texts stand in the draft-5 list byte for byte as the rulings give them (cut again from the rulings).
3. Draft 4's theory text against draft 5's: every differing line is one hunk, each lies inside exactly one entry a
   ruling changed, and nothing else differs. Each hunk is listed with its words and its ruling.
4. The full drafts: outside the theory text, only the three meta blocks differ.
5. Every one of the eighteen items has its "S93 cross-examination:" line in its entry's CHECK field.
"""
import difflib
import hashlib
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s93_lib import CHANGE_LIST_REL, REPO, fence_after, git_show, ruling  # noqa: E402

sys.path.insert(0, str(REPO / 'Semantics/tools'))
import s89_apply_changes as T  # noqa: E402

D4 = REPO / 'Semantics/tests/Revision 2 - file 13 draft 4, theory text.md'
D5 = REPO / 'Semantics/tests/Revision 2 - file 13 draft 5, theory text.md'
CL5 = (REPO / CHANGE_LIST_REL).read_text(encoding='utf-8')
CL4 = git_show(CHANGE_LIST_REL)
RULING_OF = {'W19.1': 'X03', 'W35.2': 'X05', 'W20.1': 'X06', 'W59.1': 'X09', 'W61.1': 'X11', 'W7.5': 'X17',
             'W35.5': 'X04 (companion entry)', 'W38.1': 'X18'}
problems = []

# 1 ------------------------------------------------------------------------------------------------
e4 = {x['id']: x for x in T.parse_change_list(CL4)}
e5 = {x['id']: x for x in T.parse_change_list(CL5)}
added, removed = sorted(set(e5) - set(e4)), sorted(set(e4) - set(e5))
changed = sorted(i for i in set(e4) & set(e5)
                 if any(e4[i].get(f) != e5[i].get(f) for f in ('OLD', 'NEW', 'KIND', 'DECLARATION', 'FILE-11 LINE',
                                                               'REASON WORD', 'STATUS')))
print('1. entries added:', added, '; removed:', removed, '; fields changed:', changed)
if added != ['W35.5', 'W61.1'] or removed or set(changed) != {'W19.1', 'W35.2', 'W20.1', 'W59.1', 'W7.5', 'W38.1'}:
    problems.append('entry set differs from the rulings')

# 2 ------------------------------------------------------------------------------------------------
checks = [
    ('W19.1', 'NEW', fence_after(ruling('X03'), '- **The fix.** OLD is unchanged. NEW (132 words):')),
    ('W19.1', 'DECLARATION', fence_after(ruling('X03'), 'KIND: CLAIM (unchanged). DECLARATION:')),
    ('W35.2', 'NEW', fence_after(ruling('X05'), '- **NEW:**', start_marker='### The FIX, ready to paste')),
    ('W35.2', 'DECLARATION', fence_after(ruling('X05'), '- **DECLARATION:**', start_marker='### The FIX, ready to paste')),
    ('W20.1', 'NEW', fence_after(ruling('X06'), '- **NEW:**', start_marker='### The FIX, exact')),
    ('W20.1', 'DECLARATION', fence_after(ruling('X06'), '- **DECLARATION:**', start_marker='### The FIX, exact')),
    ('W59.1', 'DECLARATION', fence_after(ruling('X09'), 'The whole DECLARATION then reads:')),
    ('W61.1', 'OLD', fence_after(ruling('X11'), '- **OLD:**', start_marker='## The proposed entry')),
    ('W61.1', 'NEW', fence_after(ruling('X11'), '- **NEW:**', start_marker='## The proposed entry')),
    ('W61.1', 'DECLARATION', fence_after(ruling('X11'), '- **DECLARATION:**', start_marker='**5. The entry as fixed.**')),
    ('W7.5', 'OLD', fence_after(ruling('X17'), '- **OLD:**', start_marker='**The FIX** (OLD, NEW and DECLARATION')),
    ('W7.5', 'NEW', fence_after(ruling('X17'), '- **NEW:**', start_marker='**The FIX** (OLD, NEW and DECLARATION')),
    ('W7.5', 'DECLARATION', fence_after(ruling('X17'), '- **DECLARATION:**',
                                        start_marker='**The FIX** (OLD, NEW and DECLARATION')),
]
for entry_id, field, want in checks:
    ok = e5[entry_id][field].strip() == want.strip()
    print('2. %-6s %-11s byte for byte as ruled: %s' % (entry_id, field, ok))
    if not ok:
        problems.append('%s %s differs from its ruling' % (entry_id, field))
rivals = fence_after(ruling('X09'), 'The paragraph "Rivals" of NEW then reads, whole:')
ok = e5['W59.1']['NEW'].split('\n')[0] == rivals and e5['W59.1']['NEW'].split('\n', 1)[1] == \
    e4['W59.1']['NEW'].split('\n', 1)[1]
print('2. W59.1  NEW         "Rivals" as ruled, the rest byte for byte as draft 4: %s' % ok)
if not ok:
    problems.append('W59.1 NEW')
x18_new = fence_after(ruling('X18'), 'NEW:', start_marker="**FIX.** In W38.1's NEW")
x18_old = fence_after(ruling('X18'), 'OLD:', start_marker="**FIX.** In W38.1's NEW")
ok = e5['W38.1']['NEW'] == e4['W38.1']['NEW'].replace(x18_old, x18_new) and e4['W38.1']['NEW'].count(x18_old) == 1
print('2. W38.1  NEW         one line replaced as ruled, the rest byte for byte: %s' % ok)
if not ok:
    problems.append('W38.1 NEW')
w355 = fence_after(ruling('X04'), '- Text ready to paste:', fence='`````')
start = CL5.index('### W35.5 — ')
ok = CL5[start:start + len(w355)] == w355
print('2. W35.5  the whole entry as the X04 ruling gives it: %s' % ok)
if not ok:
    problems.append('W35.5 entry')

# 3 ------------------------------------------------------------------------------------------------
d4, d5 = D4.read_text(encoding='utf-8'), D5.read_text(encoding='utf-8')
print('3. draft 4 md5 %s; draft 5 md5 %s' % (hashlib.md5(d4.encode()).hexdigest(), hashlib.md5(d5.encode()).hexdigest()))
file_11 = T.find_file_11()
applied5, _, _ = T.check_entries(file_11, list(T.parse_change_list(CL5)))
theory5 = [x for x in applied5 if x['ruling'] != 'META']
# where each entry's NEW stands in draft 5's theory text: rebuild it as the program does, keeping offsets
spans, pieces, position, built = {}, [], 0, 0
for x in theory5:
    pieces.append(file_11[position:x['start']]); built += x['start'] - position
    spans[x['id']] = (built, built + len(x['NEW'])); pieces.append(x['NEW']); built += len(x['NEW'])
    position = x['end']
pieces.append(file_11[position:])
theory_only = ''.join(pieces)
note_entry = [x for x in applied5 if x['ruling'] == 'META' and T.MARKERS['NOTE'][0] in x['NEW']][0]
removed_at = theory_only.index(note_entry['OLD'] + '\n\n'); removed_len = len(note_entry['OLD']) + 2
assert theory_only[:removed_at] + theory_only[removed_at + removed_len:] == d5
spans = {k: (a - removed_len, b - removed_len) if a > removed_at else (a, b) for k, (a, b) in spans.items()}
d4_lines, d5_lines = d4.split('\n'), d5.split('\n')
line_start = [0]
for line in d5_lines:
    line_start.append(line_start[-1] + len(line) + 1)
hunks = [op for op in difflib.SequenceMatcher(None, d4_lines, d5_lines, autojunk=False).get_opcodes()
         if op[0] != 'equal']
for tag, i1, i2, j1, j2 in hunks:
    old_line, new_line = '\n'.join(d4_lines[i1:i2]), '\n'.join(d5_lines[j1:j2])
    base = line_start[j1]
    changed_ranges = []
    for t2, a1, a2, b1, b2 in difflib.SequenceMatcher(None, old_line, new_line, autojunk=False).get_opcodes():
        if t2 == 'equal':
            continue
        placements = [(base + b1, base + max(b2, b1 + 1))]
        if t2 == 'insert':
            # an insertion may be aligned one way or another where the characters beside it repeat its ends
            c1, c2 = base + b1, base + b2
            while c1 > 0 and d5[c1 - 1] == d5[c2 - 1]:
                c1, c2 = c1 - 1, c2 - 1
                placements.append((c1, c2))
            c1, c2 = base + b1, base + b2
            while c2 < len(d5) and d5[c1] == d5[c2]:
                c1, c2 = c1 + 1, c2 + 1
                placements.append((c1, c2))
        changed_ranges.append(placements)
    owners = sorted({k for k, (a, b) in spans.items() for placements in changed_ranges
                     if any(a <= c1 and c2 <= b for c1, c2 in placements)})
    outside = [pl[0] for pl in changed_ranges if not any(a <= c1 and c2 <= b for a, b in spans.values() for c1, c2 in pl)]
    words_old, words_new = old_line.split(' '), new_line.split(' ')
    sm = difflib.SequenceMatcher(None, words_old, words_new, autojunk=False)
    pieces_w = []
    for t2, a1, a2, b1, b2 in sm.get_opcodes():
        if t2 != 'equal':
            pieces_w.append('"%s" -> "%s"' % (' '.join(words_old[a1:a2]), ' '.join(words_new[b1:b2])))
    print('3. hunk %s: draft-4 line %s, draft-5 line %s; entry %s; ruling %s; %s' % (
        tag, i1 + 1 if i2 - i1 == 1 else '%d-%d' % (i1 + 1, i2), j1 + 1 if j2 - j1 == 1 else '%d-%d' % (j1 + 1, j2),
        owners, [RULING_OF.get(o, 'NONE') for o in owners], '; '.join(p[:400] for p in pieces_w)))
    if len(owners) != 1 or owners[0] not in RULING_OF or outside:
        problems.append('hunk at draft-4 line %d: owners %s, outside %s' % (i1 + 1, owners, outside))
print('3. hunks: %d' % len(hunks))
if len(hunks) != 7:
    problems.append('expected 7 hunks, found %d' % len(hunks))

# 4 ------------------------------------------------------------------------------------------------
f4 = (HERE / 'd4_full.md').read_text(encoding='utf-8')
f5 = (HERE / 'd5_full.md').read_text(encoding='utf-8')
cut4, cut5 = T.cut_meta_blocks(f4), T.cut_meta_blocks(f5)
print('4. full drafts md5: draft 4 %s, draft 5 %s; cut of the meta blocks gives each theory text: %s, %s' % (
    hashlib.md5(f4.encode()).hexdigest(), hashlib.md5(f5.encode()).hexdigest(), cut4 == d4, cut5 == d5))
if cut4 != d4 or cut5 != d5:
    problems.append('meta cut')
for name, (begin, end) in T.MARKERS.items():
    b4, b5 = f4[f4.index(begin):f4.index(end)], f5[f5.index(begin):f5.index(end)]
    print('4. meta block %-7s differs: %s' % (name, b4 != b5))

# 5 ------------------------------------------------------------------------------------------------
ITEMS = {'X01': 'W37.1', 'X02': 'W36.1', 'X03': 'W19.1', 'X04': 'W35.1', 'X05': 'W35.2', 'X06': 'W20.1',
         'X07': 'W34.1', 'X08': 'W33.1', 'X09': 'W59.1', 'X10': 'W59.1', 'X11': 'W61.1', 'X12': 'W40.1',
         'X13': 'W24.1', 'X14': 'W60.1', 'X15': 'W22.1', 'X16': 'W6.3', 'X17': 'W7.5', 'X18': 'W38.1'}
sections = re.split(r'(?m)^### ', CL5.split('\n## The entries\n', 1)[1])
by_id = {s.split(' — ', 1)[0]: s for s in sections if ' — ' in s.split('\n', 1)[0]}
count_lines = {}
for item, entry_id in ITEMS.items():
    section = by_id[entry_id]
    check_block = section[section.index('\n- **CHECK:**'):section.index('\n- **OLD:**')]
    count_lines[entry_id] = len(re.findall(r'(?m)^  - S93 cross-examination:', check_block)) + \
        len(re.findall(r'(?m)^- \*\*CHECK:\*\* S93 cross-examination:', check_block))
for entry_id in sorted(set(ITEMS.values())):
    want = list(ITEMS.values()).count(entry_id)
    print('5. %-6s S93 CHECK lines: %d (items: %d)' % (entry_id, count_lines[entry_id], want))
    if count_lines[entry_id] != want:
        problems.append('%s has %d S93 lines, wants %d' % (entry_id, count_lines[entry_id], want))
section = by_id['W35.5']
print('5. W35.5  CHECK begins "S93 cross-examination:": %s' % ('\n- **CHECK:** S93 cross-examination:' in section))

print('PROBLEMS:', problems if problems else 'none')
sys.exit(1 if problems else 0)
