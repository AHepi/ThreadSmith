#!/usr/bin/env python3
"""s93_regen_note.py - stage D: regenerate the revision note for draft 5, as the draft-4 pass did
(tests/working files/rivals/final/regen_note.py), from the full draft the program wrote (d5_full.md) and the draft-5
change list (cl_draft5.md).

Section 1 (the note and its declarations) is taken from the draft's NOTE block as the program filled it. Section 2's
column "in revision 2" is taken from the draft's layer-2 table, which the program computes. Section 5's map is rebuilt
from the change list in file-11 order, as the program numbers it, with a column for the S93 cross-examination. The
other sections are edited in place. Every replacement asserts one occurrence. The base is the note as committed
(HEAD). Output: note_draft5.md.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s93_lib import NOTE_REL, REPO, git_show, one  # noqa: E402

sys.path.insert(0, str(REPO / 'Semantics/tools'))
import s89_apply_changes as T  # noqa: E402

FULL = (HERE / 'd5_full.md').read_text(encoding='utf-8')
note = git_show(NOTE_REL)
cl_text = (HERE / 'cl_draft5.md').read_text(encoding='utf-8')
DATE = 'draft of 25 September 2026, not frozen'

# ------------------------------------------------------------------ header, italic, what this is
note = one(note, '**DRAFT 4 — hard to vary restated through rivals and problems; correction-sticks result added; not '
                 'frozen**', '**DRAFT 5 — the S93 rulings on draft 4 applied; not frozen**', 'head')
note = one(note, "Made from file 11, md5 5e494c1095d920d128b9a79de378f923, and from the draft-4 change list. Draft 3 (24 "
                 "September) applied every S90 ruling: 10 entries fixed, 14 kept, none dropped. Draft 4 (25 September) adds "
                 "two entries and edits four on the owner's position of 24–25 September.",
           "Made from file 11, md5 5e494c1095d920d128b9a79de378f923, and from the draft-5 change list. Draft 3 (24 "
           "September) applied every S90 ruling: 10 entries fixed, 14 kept, none dropped. Draft 4 (25 September) adds "
           "two entries and edits four on the owner's position of 24–25 September. Draft 5 (25 September) applies every "
           "S93 ruling on draft 4: seven FIX, three KEEP, none DROP, and two entries added (W61.1 and W35.5).", 'made from')
old_italic_end = ("regenerated this note from it with the same program: N = 51 of M = 57, K = 42. It wrote nothing into "
                  "`authority/`.*")
note = one(note, old_italic_end, old_italic_end[:-1] + " Later on 25 September 2026 another Claude subagent applied every "
           "S93 ruling to the change list (draft 5; W61.1 and W35.5 added; W19.1, W35.2, W20.1, W59.1, W7.5 and W38.1 "
           "fixed) and regenerated this note from it with the same program: N = 52 of M = 59, K = 42. It wrote nothing "
           "into `authority/`.*", 'italic')
anchor = "\nIn file 13 the note, the note of sources and departures and the record stand between marker lines,"
note = one(note, anchor,
           "\nDraft 5 applies the rulings of the S93 cross-examination of draft 4 (`results/S93 Reading of the "
           "replies.md`). W61.1 (file 11, line 323), the proposed correction of the pole sentence, is entered as a "
           "change of claim because its ruling sets the kind, so one line joins the list and N and M each rise by one. "
           "W35.5 (line 572), the companion entry for Derivation 4's proof, is expected WORDING, so M rises by one more "
           "and the list does not change. Five declared lines change: W19.1's (line 121), W35.2's (line 225), W20.1's "
           "(line 233), W59.1's (line 317) and W7.5's (line 518). The sources note (W38.1) changes in one line; it is "
           "not counted.\n" + anchor, 'what this is')

# ------------------------------------------------------------------ section 1
b = FULL.index('<!-- META:NOTE BEGIN -->\n') + len('<!-- META:NOTE BEGIN -->\n')
e = FULL.index('\n<!-- META:NOTE END -->')
note_block = FULL[b:e]
N = re.search(r'below: (\d+) of the (\d+) changes', note_block)
assert (N.group(1), N.group(2)) == ('52', '59'), N.groups()
s1_start = note.index('The date slot is filled with')
s1_end = note.index('## 2. The second layer')
new_s1 = ("The date slot is filled with \"%s\". At the freeze it takes the date, written as file 11 wrote its date. "
          "N = %s of M = %s changes; K = 42 places.\n\n" % (DATE, N.group(1), N.group(2))
          + note_block.strip('\n') + "\n\n")
note = note[:s1_start] + new_s1 + note[s1_end:]

# ------------------------------------------------------------------ section 2: the column "in revision 2"
col = {}
for m in re.finditer(r'(?m)^\| (L2-\d\d) \|.*\| ([^|]+) \|$', FULL[FULL.index('## Layer 2'):]):
    col[m.group(1)] = m.group(2).strip()
assert len(col) == 42
lines = note.split('\n')
changed, beside = [], []
for i, line in enumerate(lines):
    m = re.match(r'^\| (L2-\d\d) \|', line)
    if not m:
        continue
    cells = line.split(' | ')
    cells[6] = col[m.group(1)]
    lines[i] = ' | '.join(cells)
    if col[m.group(1)].startswith('changed'):
        changed.append(m.group(1))
    elif 'beside' in col[m.group(1)]:
        beside.append(m.group(1))
note = '\n'.join(lines)
assert changed == ['L2-01', 'L2-12', 'L2-13', 'L2-16', 'L2-26', 'L2-31', 'L2-37', 'L2-39', 'L2-42'], changed
assert beside == ['L2-07', 'L2-11', 'L2-24', 'L2-27', 'L2-33'], beside
old_sum = [l for l in note.split('\n') if l.startswith('In revision 2, 9 of the 42 places')][0]
kept = 42 - len(changed) - len(beside)
note = one(note, old_sum,
           "In revision 2, %d of the 42 places are changed again by layer-1 entries (%s), %d are kept with text added "
           "beside them (%s), and the other %d stand word for word. Neither draft 4 nor draft 5 moves a place between "
           "these groups; draft 4 renumbers the layer-1 entries from R2-25 on, and draft 5 from R2-26 on."
           % (len(changed), ', '.join(changed), len(beside), ', '.join(beside), kept), 'summary')

# ------------------------------------------------------------------ section 4
old_d4 = [l for l in note.split('\n') if l.startswith('- **Draft 4, read by no outside reader.**')][0]
note = one(note, old_d4,
           "- **Draft 4, read by both outside readers (S93).** The draft-4 entries (W59.1, W60.1, the edited W34.1, W33.1 "
           "and W36.1, and the sources note W38.1) and the ten S90 fixes went to Atria and Mimo in eleven parts, 22 calls, "
           "all accepted on pass 1: eighteen items, X01–X18, the proposed correction of the pole sentence (file 11, line "
           "323) among them. The rulings are applied in the change list (draft 5): seven FIX (W19.1, W35.2, W20.1, W59.1's "
           "\"Rivals\", W7.5 and the sources note, and the pole sentence entered as W61.1), three KEEP (W35.1, W59.1's "
           "\"Problems\" and W60.1), none dropped; the eight items no reply challenged are recorded as upheld by both "
           "readers, not thereby confirmed. The texts and declarations the S93 fixes wrote, and the two added entries "
           "W61.1 and W35.5, have been read by no outside reader: file 11, lines 7–9 (the sources note's *Surprise and "
           "problems* line), 121, 225, 233, 317–319, 323, 518 and 572.", 'sec4 draft 4')
note = one(note, "The texts and declarations the ten fixes wrote have been read by no outside reader: file 11, lines 15, "
                 "121, 219–223, 225, 233, 337, 351, 373, 447 and 518.",
           "The texts and declarations the ten fixes wrote were read by no outside reader until the S93 cross-examination, "
           "which carried all ten: file 11, lines 15, 121, 219–223, 225, 233, 337, 351, 373, 447 and 518.", 'sec4 S90')
note = one(note, "  - W24.1 (file 11, line 351): expected WORDING.\n",
           "  - W24.1 (file 11, line 351): expected WORDING.\n"
           "  - W35.5 (file 11, line 572): expected WORDING (added after the S93 cross-examination).\n", 'sec4 W35.5')

# ------------------------------------------------------------------ section 5: the map
old_rows = {}
for line in note.split('\n'):
    m = re.match(r'^\| (R2-\d\d) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| ([^|]+) \| '
                 r'([^|]+) \|$', line)
    if m:
        old_rows[m.group(2).strip()] = dict(brief=m.group(3).strip(), parts=m.group(4).strip(),
                                            ruling=m.group(9).strip())
assert len(old_rows) == 57, len(old_rows)
S93 = {'W37.1': 'X01: upheld by both', 'W36.1': 'X02: upheld by both', 'W19.1': 'X03: FIX', 'W35.1': 'X04: KEEP',
       'W35.2': 'X05: FIX', 'W20.1': 'X06: FIX', 'W34.1': 'X07: upheld by both', 'W33.1': 'X08: upheld by both',
       'W59.1': 'X09: FIX; X10: KEEP', 'W61.1': 'X11: FIX, entered as CLAIM', 'W40.1': 'X12: upheld by both',
       'W24.1': 'X13: upheld by both', 'W60.1': 'X14: KEEP', 'W22.1': 'X15: upheld by both',
       'W6.3': 'X16: upheld by both', 'W7.5': 'X17: FIX', 'W35.5': '— (added after S93, from the X04 ruling)'}
file_11 = T.find_file_11()
entries = T.parse_change_list(cl_text)
applied, _, _ = T.check_entries(file_11, entries)
theory = [x for x in applied if x['ruling'] != 'META']
rows = ["| R2 | entry | S90 brief | S90 parts | file-11 line | reason | expected ruling | declared in the note | "
        "S90 ruling | S93 |",
        "|---|---|---|---|---|---|---|---|---|---|"]
for n, x in enumerate(theory, 1):
    o = old_rows.get(x['id'])
    if o is None:
        brief, parts, ruling = '—', '—', '— (new in draft 5)'
    else:
        brief, parts = o['brief'], o['parts']
        ruling = o['ruling'].replace('; edited in draft 4, not read', '; edited in draft 4').replace(
            'not read (new in draft 4)', '— (new in draft 4)')
    rows.append('| R2-%02d | %s | %s | %s | %s | %s | %s | %s | %s | %s |' % (
        n, x['id'], brief, parts, x['FILE-11 LINE'], x['REASON WORD'].strip(), x['ruling'],
        'yes' if x['ruling'] == 'CLAIM' else 'no', ruling, S93.get(x['id'], '—')))
assert len(rows) - 2 == 59
assert sum(1 for x in theory if x['id'] in S93) == 17
ts = note.index('| R2 | entry | S90 brief |')
te = note.index('\n\n**Counts.**', ts)
note = note[:ts] + '\n'.join(rows) + note[te:]
old_numbers = ("two higher from W22.1 on (R2-30 to R2-57).")
note = one(note, old_numbers, old_numbers + " Draft 5 inserts W61.1 after W59.1 and W35.5 after W17.3, in file-11 order, "
           "so W40.1 to W17.3 are one higher than in draft 4 (R2-27 to R2-55), and W7.6, W10a.1 and W19.3 + W10(b).1 two "
           "higher (R2-57 to R2-59). The column \"S93\" gives each entry's item in the S93 cross-examination of draft 4 "
           "and its outcome, a checker's ruling or \"upheld by both\" (upheld by both readers, not thereby confirmed); "
           "\"—\" marks an entry that was not an item. The eighteenth item, X18, is the sources note (W38.1), a meta "
           "entry with no R2 number: FIX.", 'layer-1 numbers')
old_counts = [l for l in note.split('\n') if l.startswith('**Counts.** N = 51 of M = 57.')][0]
note = one(note, old_counts,
           "**Counts.** N = 52 of M = 59. By drafting group: A 14 of 18; B1 14 of 15; C 10 of 12; B2 11 of 11; H 2 of 2; "
           "S93 1 of 1. K = 42. In draft 4, N was 51 of M = 57; W61.1 (group S93) adds one to each, and W35.5 (group C, "
           "WORDING) one to M. In draft 3, N was 49 of M = 55; before the S90 rulings were applied, N was 48 and B1 was 13 "
           "of 15: W6.3 was then expected WORDING. The column \"S90 ruling\" gives the ruling after reconciliation: FIX "
           "for the 10 entries fixed, KEEP for the 14 kept, and \"not contested\" for the 31 that neither reply "
           "contested; none was dropped. W34.1, W33.1 and W36.1 were edited in draft 4 after their S90 ruling, and "
           "W34.1's and W33.1's reason is now change of claim; W59.1 and W60.1 are new in draft 4, and W61.1 and W35.5 "
           "new in draft 5. The S93 rulings: 7 FIX, six of them in the map (W19.1, W35.2, W20.1, W59.1, W61.1 and W7.5) "
           "and one on the sources note; 3 KEEP (W35.1, W59.1's \"Problems\" and W60.1); and 8 items upheld by both "
           "readers.", 'counts')
(HERE / 'note_draft5.md').write_text(note, encoding='utf-8')
print('written', HERE / 'note_draft5.md', 'changed', len(changed), 'beside', len(beside), 'rows', len(rows) - 2)
