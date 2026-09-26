#!/usr/bin/env python3
"""regen_note.py - regenerate the revision note for draft 4 from the full draft the program wrote
(rivals/file13_draft4.md) and the draft-4 change list (final/cl_draft4.md).

Section 1 (the note and its declarations) is taken from the draft's NOTE block as the program filled it.
Section 2's column "in revision 2" is taken from the draft's layer-2 table, which the program computes.
Section 5's map is rebuilt from the change list in file-11 order, as the program numbers it. The other sections
are edited in place. Every replacement asserts a single occurrence. Output: final/note_draft4.md.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
RIV = HERE.parent
REPO = pathlib.Path('/home/user/ThreadSmith')
sys.path.insert(0, str(REPO / 'Semantics/tools'))
import s89_apply_changes as T  # noqa: E402

NOTE = REPO / 'Semantics/tests/Revision 2 - revision note, draft of 23 September.md'
FULL = (RIV / 'file13_draft4.md').read_text(encoding='utf-8')
import subprocess
# the base is draft 3 of the note, as committed (HEAD), not the working copy
note = subprocess.run(['git', 'show', 'HEAD:Semantics/tests/Revision 2 - revision note, draft of 23 September.md'], cwd=str(REPO), capture_output=True, text=True, check=True).stdout
cl_text = (HERE / 'cl_draft4.md').read_text(encoding='utf-8')


def one(text, old, new, what):
    n = text.count(old)
    if n != 1:
        sys.exit('note replacement %s: old text occurs %d times' % (what, n))
    return text.replace(old, new)


# ------------------------------------------------------------------ header, italic, what this is
old_head = [l for l in note.split('\n') if l.startswith('**DRAFT 3 — after the S90 cross-examination')][0]
note = one(note, old_head,
           "**DRAFT 4 — hard to vary restated through rivals and problems; correction-sticks result added; not frozen**\n\n"
           "Made from file 11, md5 5e494c1095d920d128b9a79de378f923, and from the draft-4 change list. Draft 3 (24 "
           "September) applied every S90 ruling: 10 entries fixed, 14 kept, none dropped. Draft 4 (25 September) adds two "
           "entries and edits four on the owner's position of 24–25 September.", 'head')
note = one(note, "N = 49 of M = 55, K = 42. It opened no S90 reply and wrote nothing into `authority/`.*",
           "N = 49 of M = 55, K = 42. It opened no S90 reply and wrote nothing into `authority/`. On 25 September 2026 "
           "another Claude subagent made draft 4 of the change list (W59.1 and W60.1 added; W34.1, W33.1, W36.1 and W38.1 "
           "edited) and regenerated this note from it with the same program: N = 51 of M = 57, K = 42. It wrote nothing "
           "into `authority/`.*", 'italic')
note = one(note, "\nIn file 13 the note, the note of sources and departures and the record stand between marker lines,",
           "\nDraft 4 restates hard-to-vary through rivals and problems and adds the correction-sticks result, on the "
           "owner's position of 24–25 September. W59.1 (file 11, lines 317–319) and W60.1 (line 365) are new changes of "
           "claim, so two lines join the list, and N and M each rise by two. Three declared lines change: W36.1's (line "
           "71), W34.1's and W33.1's (both line 315). The sources note (W38.1) changes too; it is not counted. The record "
           "of the pass is `tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md`.\n"
           "\nIn file 13 the note, the note of sources and departures and the record stand between marker lines,",
           'what this is')

# ------------------------------------------------------------------ section 1
b = FULL.index('<!-- META:NOTE BEGIN -->\n') + len('<!-- META:NOTE BEGIN -->\n')
e = FULL.index('\n<!-- META:NOTE END -->')
note_block = FULL[b:e]
N = re.search(r'below: (\d+) of the (\d+) changes', note_block)
s1_start = note.index('The date slot is filled with')
s1_end = note.index('## 2. The second layer')
new_s1 = ("The date slot is filled with \"draft of 25 September 2026, not frozen\". At the freeze it takes the date, "
          "written as file 11 wrote its date. N = %s of M = %s changes; K = 42 places.\n\n" % (N.group(1), N.group(2))
          + note_block.strip('\n') + "\n\n")
note = note[:s1_start] + new_s1 + note[s1_end:]

# ------------------------------------------------------------------ section 2: the column "in revision 2"
col = {}
for m in re.finditer(r'(?m)^\| (L2-\d\d) \|.*\| ([^|]+) \|$', FULL[FULL.index('## Layer 2'):]):
    col[m.group(1)] = m.group(2).strip()
lines = note.split('\n')
changed, beside = [], []
for i, l in enumerate(lines):
    m = re.match(r'^\| (L2-\d\d) \|', l)
    if not m:
        continue
    cells = l.split(' | ')
    # cells: '| L2-xx', 03 place, Part and heading, file 10, file 11, conclude, in revision 2, 'declared by |'
    cells[6] = col[m.group(1)]
    lines[i] = ' | '.join(cells)
    if col[m.group(1)].startswith('changed'):
        changed.append(m.group(1))
    elif 'beside' in col[m.group(1)]:
        beside.append(m.group(1))
note = '\n'.join(lines)
old_sum = [l for l in note.split('\n') if l.startswith('In revision 2, 9 of the 42 places')][0]
kept = 42 - len(changed) - len(beside)
note = one(note, old_sum,
           "In revision 2, %d of the 42 places are changed again by layer-1 entries (%s), %d are kept with text added "
           "beside them (%s), and the other %d stand word for word. Draft 4 moves no place between these groups; it "
           "renumbers the layer-1 entries from R2-25 on." % (len(changed), ', '.join(changed), len(beside),
                                                               ', '.join(beside), kept), 'summary')

# ------------------------------------------------------------------ section 4
note = one(note, "- **Read by both outside readers (S90).** All 55 changes,",
           "- **Draft 4, read by no outside reader.** The two new changes, W59.1 (file 11, lines 317–319) and W60.1 (line "
           "365), the edited W34.1 and W33.1 (line 315) and W36.1 (line 71), and the sources note (W38.1). They were "
           "tested on finite models and attacked twice by fresh subagents, and every fix was applied; neither Atria nor "
           "Mimo has seen them. A cross-examination should carry them before the freeze.\n"
           "- **Read by both outside readers (S90).** The 55 changes of draft 3,", 'sec4')

# ------------------------------------------------------------------ section 5: the map
old_rows = {}
for l in note.split('\n'):
    m = re.match(r'^\| (R2-\d\d) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|$', l)
    if m:
        old_rows[m.group(2).strip()] = dict(old_r=m.group(1), brief=m.group(3).strip(), ruling=m.group(8).strip())
file_11 = T.find_file_11()
entries = T.parse_change_list(cl_text)
applied, _, _ = T.check_entries(file_11, entries)
theory = [x for x in applied if x['ruling'] != 'META']
rows = ["| R2 | entry | S90 brief | S90 parts | file-11 line | reason | expected ruling | declared in the note | S90 ruling |",
        "|---|---|---|---|---|---|---|---|---|"]
DRAFT4_EDITED = {'W34.1', 'W33.1', 'W36.1'}
for n, x in enumerate(theory, 1):
    o = old_rows.get(x['id'])
    if o is None:
        brief, parts, ruling = '—', '—', 'not read (new in draft 4)'
    else:
        brief, parts = o['brief'], 'R' + o['old_r'][3:]
        ruling = o['ruling'] + ('; edited in draft 4, not read' if x['id'] in DRAFT4_EDITED else '')
    rows.append('| R2-%02d | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        n, x['id'], brief, parts, x['FILE-11 LINE'], x['REASON WORD'].strip(), x['ruling'],
        'yes' if x['ruling'] == 'CLAIM' else 'no', ruling))
ts = note.index('| R2 | entry | S90 brief |')
te = note.index('\n\n**Counts.**', ts)
note = note[:ts] + '\n'.join(rows) + note[te:]
note = one(note, "The S90 parts cite every entry as R01–R55, which is its R2 number.",
           "The S90 parts cite every entry as R01–R55, which was its R2 number in draft 3; the column \"S90 parts\" keeps "
           "that id. Draft 4 inserts W59.1 after W33.1 and W60.1 after W31.1, so every entry from W40.1 on has a higher R2 "
           "number than in draft 3: one higher from W40.1 to W31.1 (R2-26 to R2-28), two higher from W22.1 on (R2-30 to "
           "R2-57).", 'layer-1 numbers')
old_counts = [l for l in note.split('\n') if l.startswith('**Counts.** N = 49 of M = 55.')][0]
note = one(note, old_counts,
           "**Counts.** N = 51 of M = 57. By drafting group: A 14 of 18; B1 14 of 15; C 10 of 11; B2 11 of 11; H 2 of 2. "
           "K = 42. In draft 3, N was 49 of M = 55; before the S90 rulings were applied, N was 48 and B1 was 13 of 15: W6.3 "
           "was then expected WORDING. The column \"S90 ruling\" gives the ruling after reconciliation: FIX for the 10 "
           "entries fixed, KEEP for the 14 kept, and \"not contested\" for the 31 that neither reply contested; none was "
           "dropped. W34.1, W33.1 and W36.1 were edited in draft 4 after their S90 ruling, and W34.1's and W33.1's reason "
           "is now change of claim; W59.1 and W60.1 are new and were read by neither reply.", 'counts')
(HERE / 'note_draft4.md').write_text(note, encoding='utf-8')
print('written', HERE / 'note_draft4.md', 'changed', len(changed), 'beside', len(beside), 'rows', len(rows) - 2)
