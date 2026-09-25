#!/usr/bin/env python3
"""s93_frame.py - stage B: bring the frame of the change list up to draft 5 (header, the italic record, What this
is, Counts, What the checks changed with the S93 table and the build, the held items, and a section "Carried
forward after S93"), on the list with the S93 entry edits applied (cl_entries.md, stage A).

It first runs tools/s89_apply_changes.py --self-test on cl_entries.md (output to this scratch folder, never
authority/) to read the numbers the frame quotes, then writes cl_draft5.md. Every replacement asserts one
occurrence. The frame lies before "## The entries", so it does not change what the program builds; stage C checks
that the md5s are the same on cl_draft5.md.
"""
import difflib
import hashlib
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s93_lib import REPO, TOOL, one  # noqa: E402

sys.path.insert(0, str(REPO / 'Semantics/tools'))
import s89_apply_changes as T  # noqa: E402

DATE = 'draft of 25 September 2026, not frozen'
FULL = HERE / 'b_full.md'
THEORY = HERE / 'b_theory.md'
D4 = REPO / 'Semantics/tests/Revision 2 - file 13 draft 4, theory text.md'

run = subprocess.run([sys.executable, str(TOOL), str(FULL), '--change-list', str(HERE / 'cl_entries.md'),
                      '--theory-output', str(THEORY), '--date', DATE, '--self-test'],
                     capture_output=True, text=True, cwd=str(REPO), env={'PYTHONDONTWRITEBYTECODE': '1',
                                                                          'PATH': '/usr/bin:/bin'})
print(run.stdout)
if run.returncode != 0:
    sys.exit('the program refused')
out = run.stdout
full_md5 = re.search(r'^md5: ([0-9a-f]{32})$', out, re.M).group(1)
words_full, words_theory = map(int, re.search(r'^words: (\d+) \(theory text alone: (\d+)\)$', out, re.M).groups())
hunks = int(re.search(r'(\d+) diff hunks', out).group(1))
theory_md5 = hashlib.md5(THEORY.read_bytes()).hexdigest()


def shell_wc(path):
    return int(subprocess.run(['wc', '-w', str(path)], capture_output=True, text=True,
                              env={'PATH': '/usr/bin:/bin', 'LC_ALL': 'POSIX'}).stdout.split()[0])


wc_theory, wc_full = shell_wc(THEORY), shell_wc(FULL)
d4_md5 = hashlib.md5(D4.read_bytes()).hexdigest()
assert d4_md5 == 'fc55b470c63cd4b3c27d6aa64d8d8c17', d4_md5
d4_lines = D4.read_text(encoding='utf-8').split('\n')
d5_lines = THEORY.read_text(encoding='utf-8').split('\n')
changed_d4_lines = []
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, d4_lines, d5_lines, autojunk=False).get_opcodes():
    if tag == 'equal':
        continue
    assert tag == 'replace' and i2 - i1 == 1 and j2 - j1 == 1, (tag, i1, i2, j1, j2)
    changed_d4_lines.append(i1 + 1)
print('theory md5', theory_md5, 'full md5', full_md5, 'changed draft-4 lines', changed_d4_lines)
EXPECTED = [119, 223, 231, 315, 325, 526, 582]
assert changed_d4_lines == EXPECTED, changed_d4_lines

# R2 numbers in draft 5, as the program numbers them
file_11 = T.find_file_11()
entries = T.parse_change_list((HERE / 'cl_entries.md').read_text(encoding='utf-8'))
applied, _, _ = T.check_entries(file_11, entries)
theory_entries = [x for x in applied if x['ruling'] != 'META']
R2 = {x['id']: 'R2-%02d' % n for n, x in enumerate(theory_entries, 1)}
counts = {}
for x in theory_entries:
    counts[x['ruling']] = counts.get(x['ruling'], 0) + 1
assert (len(entries), len(applied), len(theory_entries), counts) == (67, 62, 59, {'CLAIM': 52, 'WORDING': 5, 'ORDER': 2}), \
    (len(entries), len(applied), len(theory_entries), counts)

cl = (HERE / 'cl_entries.md').read_text(encoding='utf-8')

# ------------------------------------------------------------------ header
old_head = '**DRAFT 4 — hard to vary restated through rivals and problems; correction-sticks result added; not frozen**'
cl = one(cl, old_head, '**DRAFT 5 — the S93 rulings on draft 4 applied; not frozen**', 'header')
cl = one(cl, "on correction without a record. No outside reader has seen the texts and declarations the S90 fixes or the "
             "draft-4 entries wrote.",
         "on correction without a record. Draft 5 (25 September) applies every S93 ruling on draft 4: seven rulings FIX "
         "(one of them enters the proposed X11 as W61.1), three KEEP and none DROP, and the eight items neither reader "
         "challenged are recorded as upheld by both readers, not thereby confirmed; one KEEP adds the companion entry "
         "W35.5. The file keeps its name; this is draft 5. The S93 cross-examination carried the ten S90 fixes and the "
         "six draft-4 entries to both outside readers. No outside reader has seen the texts and declarations the S93 "
         "fixes wrote, or the two entries added after it.", 'header paragraph')

# ------------------------------------------------------------------ italic record
old_end = ("The drafts, the models and the attacks are summed up in `tests/Revision 2 - hard to vary restated through "
           "rivals and problems, 25 September.md`, and the scripts are in `tests/Revision 2 - rivals and problems - "
           "scripts/`. It wrote nothing into `authority/`.*")
cl = one(cl, old_end, old_end[:-1] + " Later on 25 September 2026 another Claude subagent applied every S93 ruling to "
         "this list in one pass, which makes this draft 5; the file name still says \"draft of 23 September\". It read "
         "the S93 reading rule (`results/S93 How the cross-examination of draft 4 will be read - written before "
         "sending.md`), the tabulation of the replies (its receipts, its summary, its sections 4, 6 and 7) and the ten "
         "rulings in `results/S93 reading rulings/`, took every ruled text from them by script, byte for byte, and "
         "recorded the eight items no reply challenged in the words of the tabulation's section 4. It wrote "
         "`results/S93 Reading of the replies.md`. It opened no S93 reply, receipt, reasoning file or attempt file, "
         "wrote no ruling, and wrote nothing into `authority/`. Its scripts are in `tests/Revision 2 - S93 rulings "
         "applied - scripts/`.*", 'italic')

# ------------------------------------------------------------------ what this is
anchor = "The list is withheld from every test brief (D6), as are the note, the sources note and the record it puts " \
         "into file 13."
cl = one(cl, anchor,
         "Draft 5 applies the rulings of the S93 cross-examination of draft 4 (\"After the cross-examination (S93)\", "
         "below; the reading is `results/S93 Reading of the replies.md`). Eighteen items were put to both readers. Ten "
         "went to a fresh checker each: seven rulings FIX an entry or enter one, three KEEP, and none DROP. The eight "
         "items neither reply challenged are recorded as upheld by both readers, not thereby confirmed. Two entries "
         "join the list: W61.1, the proposed X11, entered as CLAIM because its ruling sets the kind, and W35.5, the "
         "companion entry the X04 ruling gives for Derivation 4's proof. What the rulings pass on without an edit is "
         "in \"Carried forward after S93\".\n\n" + anchor, 'what this is')

# ------------------------------------------------------------------ counts
old_counts = ("- **Entries that change the theory text: 57.** Expected ruling CLAIM 51, WORDING 4, ORDER 2. By group: A "
              "14 of 18, B1 14 of 15, B2 11 of 11, C 10 of 11, H 2 of 2. The note reads \"51 of the 57 changes\". In "
              "draft 3 it read")
cl = one(cl, old_counts,
         "- **Entries that change the theory text: 59.** Expected ruling CLAIM 52, WORDING 5, ORDER 2. By group: A 14 of "
         "18, B1 14 of 15, B2 11 of 11, C 10 of 12, H 2 of 2, S93 1 of 1. The note reads \"52 of the 59 changes\". In "
         "draft 4 it read \"51 of the 57 changes\"; after the S93 cross-examination W61.1 (the proposed X11, CLAIM) adds "
         "one line, and W35.5 (group C, WORDING) adds a change and no line. In draft 3 it read", 'counts')
cl = one(cl, "every fix of both attacks is applied, and what the attacks refuted is dropped. None has been "
             "cross-examined.",
         "every fix of both attacks is applied, and what the attacks refuted is dropped. None had been cross-examined "
         "when draft 4 was made. **After the cross-examination (S93):** 22 calls, all accepted on pass 1; eighteen "
         "items, X01–X18. Ten went to a fresh checker each, who ruled FIX on seven (X03, X05, X06, X09, X11, X17, X18) "
         "and KEEP on three (X04, X10, X14), and dropped none; the other eight were challenged by neither reply and are "
         "recorded as upheld by both readers, not thereby confirmed. Two entries are added (W61.1 and W35.5). Every S93 "
         "ruling is applied below; see \"What the checks changed\".", 'counts, the checks')

# ------------------------------------------------------------------ the S90 paragraph: now read by S93
cl = one(cl, "beginning \"S90 cross-examination:\". No outside reader has seen the texts and declarations the ten fixes "
             "wrote.",
         "beginning \"S90 cross-examination:\". No outside reader has seen the texts and declarations the ten fixes "
         "wrote. (After S93: all ten went to both outside readers, as X01, X03–X06, X12, X13 and X15–X17; see \"After "
         "the cross-examination (S93)\" below.)", 'S90 paragraph')

# ------------------------------------------------------------------ the S93 section of "What the checks changed"
rows = [
    ('X03', 'W19.1', 'FIX', "NEW reports Derivation 1 for \"an active component \\(k\\) of \\(E\\)\"; the declaration "
     "reads \"an active component\" and ends \"up to the port translation\"; KIND CLAIM unchanged"),
    ('X04', 'W35.1', 'KEEP', "OLD, NEW, KIND and DECLARATION stand; the companion entry W35.5 is added for Derivation "
     "4's proof (file-11 L572), and W35.1's REASON sentence on Derivation 4 follows it"),
    ('X05', 'W35.2', 'FIX', "\"fails at an actually occurring pair of its contract\", in NEW and in the declaration; "
     "the ruling's LOSS sentence, offered as optional, is added"),
    ('X06', 'W20.1', 'FIX', "\"including any of them that assigns an input\"; \"boundary conditions\" for \"boundary "
     "values\"; the declaration follows; O7's line, REASON's bullet on the two readings, and the findings carried "
     "forward on \"active\" and on the two readings (now closed) follow"),
    ('X09', 'W59.1, "Rivals"', 'FIX', "\"as none do when two of their active components with one anchor have "
     "different relations there\"; the declaration's third sentence carries NEW's bijection clause"),
    ('X10', 'W59.1, "Problems"', 'KEEP', "no change"),
    ('X11', 'W61.1 (new)', 'FIX: entered as CLAIM', "OLD and NEW as proposed (\"but not the calculation's "
     "\\(L\\)\"); KIND CLAIM, REASON WORD erratum, declaration added"),
    ('X14', 'W60.1', 'KEEP', "no change"),
    ('X17', 'W7.5', 'FIX', "OLD extended by the unchanged \"(RC), (U1)–(U3) depend on all of the above.\"; one "
     "sentence placing Part VI's conflict, rivals, what is established, fits, a problem for \\(p\\) and easy to vary "
     "follows it; the declaration, heading and WHERE follow; a REASON bullet, a CASES AT RISK line, and a sentence "
     "each in GAIN and LOSS are added"),
    ('X18', 'W38.1', 'FIX', "*Surprise and problems*: \"a conflict in which what the system holds meets a claimed "
     "obligation only by failing a protected one\", L429's words"),
]
lines_of = {}
for x in entries:
    lines_of[x['id']] = x.get('FILE-11 LINE', '')
table = ['| item | entry | file-11 line | R2 (draft 5) | ruling | what changed |', '|---|---|---|---|---|---|']
for item, entry, ruling_word, what in rows:
    entry_id = entry.split(',')[0].split(' (')[0]
    r2 = 'meta' if entry_id == 'W38.1' else R2[entry_id]
    table.append('| %s | %s | %s | %s | %s | %s |' % (item, entry, lines_of[entry_id], r2, ruling_word, what))
s93_section = '\n'.join([
    "**After the cross-examination (S93): 7 rulings FIX, 3 KEEP, none DROP; 8 items upheld by both readers; 2 entries "
    "added.** The eleven parts of the S93 cross-examination of draft 4 went to Atria and to Mimo, 22 calls in all, and "
    "every call was accepted on pass 1 (`results/S93 Tabulation of the replies, before any ruling.md`, section 1). Each "
    "of the ten items a reply challenged under the reading rule went to one fresh Claude checker, who ruled keep, fix "
    "or drop; the rulings are in `results/S93 reading rulings/`. The eight items neither reply challenged went to no "
    "checker and are recorded as upheld by both readers, not thereby confirmed. The reading that records all eighteen "
    "is `results/S93 Reading of the replies.md`. Every edit is made in its entry, its ruled texts cut from the ruling "
    "by script, and every one of the eighteen items has its line in its entry's CHECK field, beginning \"S93 "
    "cross-examination:\", in the checker's words where a checker ruled (rule 12). No outside reader has seen the texts "
    "and declarations the fixes wrote, or the two added entries.",
    '',
    'The column R2 gives each entry\'s number in draft 5.',
    '',
    '\n'.join(table),
    '',
    "**Upheld by both readers; not thereby confirmed: 8 items.** Their texts do not change, and each CHECK field "
    "records the line \"S93 cross-examination: upheld by both readers (s93_xexam_atria_<part>, s93_xexam_mimo_<part>); "
    "not thereby confirmed.\": X01 W37.1 (part F), X02 W36.1 (D), X07 W34.1 (D), X08 W33.1 (D), X12 W40.1 (I), X13 "
    "W24.1 (J), X15 W22.1 (J) and X16 W6.3 (K).",
    '',
    "**Added after the cross-examination: 2 entries.** W61.1 (X11; file-11 L323; CLAIM, erratum; group S93), placed "
    "between W59.1 and W40.1, and W35.5 (the X04 ruling's companion entry; file-11 L572; WORDING, clarification; group "
    "C), placed after W35.4. The program numbers them %s and %s, so W40.1 to W17.3 each have a number one higher than "
    "in draft 4 (%s to %s), and W7.6, W10a.1 and W19.3 + W10(b).1 two higher (%s to %s)."
    % (R2['W61.1'], R2['W35.5'], R2['W40.1'], R2['W17.3'], R2['W7.6'], R2['W19.3 + W10(b).1']),
    '',
    "**Dropped after the cross-examination: none.**",
    '',
    "**Also changed with the rulings.** W35.1's REASON sentence on Derivation 4 (the X04 ruling, finding 2). W20.1's "
    "O7 line and its REASON bullet on the two readings, and the findings carried forward on \"active\" and on the two "
    "readings, which is closed (X06). W7.5's heading and WHERE, a REASON bullet, a CASES AT RISK line, a sentence each "
    "in GAIN and LOSS, and the first bullet of \"Found in draft 4 (25 September)\" (X17). W35.2's LOSS (X05). "
    "**Bookkeeping, 25 September 2026:** W34.1's and W59.1's CASES AT RISK wrote \"N7 (O59)\"; under D8 N7 is O58 and "
    "O59 is N8. Both now read \"N7 (O58)\", each with a dated note. The draft-4 pass record (`tests/Revision 2 - hard "
    "to vary restated through rivals and problems, 25 September.md`) keeps its wording, as the record of that pass.",
    '',
    "**X17 re-read against the X09 and X10 rulings.** The X17 ruling asks that its sentence be re-read against the "
    "fixed L315 and L317 before the edit is made (its finding 5). Done: X09's fix changes the illustration of conflict "
    "(\"as when\" becomes \"as none do when\"), which now illustrates only the second conjunct and adds no condition, "
    "and the declaration's sentence on candidates that are not rivals; X10's ruling changes nothing. Neither changes "
    "what conflict, rivals, what is established, fits, a problem for \\(p\\) or easy to vary rest on (answers under "
    "(A), (F1), (F2), (A) and the relations the adopted physics admits; the offer; usable receipts; (E)), so the "
    "sentence stands as ruled.",
    '',
    "**The build (draft 5).** `tools/s89_apply_changes.py --self-test` applies this list with no refusal: %d entries "
    "parsed, %d applied (%d theory, %d meta), 5 record-only, none held; CLAIM %d, WORDING %d, ORDER %d; N = %d of M = "
    "%d, K = 42; %d diff hunks, each inside an entry; both planted edits refused. The theory text of draft 5 is "
    "committed as `tests/Revision 2 - file 13 draft 5, theory text.md` (md5 %s, %s words by the runner's count and %s "
    "by `wc -w`). The full draft 5, with its meta blocks and the date text \"%s\", has md5 %s and %s words by the "
    "runner's count (%s by `wc -w`). Against draft 4's theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17) it differs "
    "in exactly seven lines and nothing else, each inside an entry a ruling changed: draft-4 line 119 (W19.1, X03), 223 "
    "(W35.2, X05), 231 (W20.1, X06), 315 (W59.1, X09), 325 (W61.1, X11), 526 (W7.5, X17) and 582 (W35.5, X04). X18 "
    "changes the sources note only, which is not part of the theory text. Nothing was written into `authority/`."
    % (len(entries), len(applied), len(theory_entries), len(applied) - len(theory_entries), counts['CLAIM'],
       counts['WORDING'], counts['ORDER'], counts['CLAIM'], len(theory_entries), hunks, theory_md5,
       format(words_theory, ','), format(wc_theory, ','), DATE, full_md5, format(words_full, ','),
       format(wc_full, ',')),
    '',
    ''])
cl = one(cl, '\n## Checked, with no change entry\n', '\n' + s93_section + '## Checked, with no change entry\n',
         'S93 section')

# ------------------------------------------------------------------ the held items: W19.1 and W20.1 after S93
cl = one(cl, "W19.1 and W20.1 were then fixed after the cross-examination, and no outside reader has seen their fixed "
             "wordings.",
         "W19.1 and W20.1 were then fixed after the cross-examination, and no outside reader has seen their fixed "
         "wordings. (After S93: both readers read those fixed wordings, as X03 and X06, and both entries were fixed "
         "again after the S93 cross-examination; no outside reader has seen the S93 fixes.)", 'held items')

# ------------------------------------------------------------------ carried forward after S93
carried = (HERE / 'carried_forward_s93.md').read_text(encoding='utf-8').rstrip('\n')
cl = one(cl, '\n## The entries\n', '\n' + carried + '\n\n## The entries\n', 'carried forward after S93')

(HERE / 'cl_draft5.md').write_text(cl, encoding='utf-8')
print('written', HERE / 'cl_draft5.md')
print(dict(full_md5=full_md5, theory_md5=theory_md5, words_full=words_full, words_theory=words_theory,
           wc_full=wc_full, wc_theory=wc_theory, hunks=hunks, R2_W611=R2['W61.1'], R2_W355=R2['W35.5']))
