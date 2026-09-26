#!/usr/bin/env python3
"""s93_edit_entries.py - stage A: apply the ten S93 rulings, the eight "upheld by both readers" lines and the
bookkeeping to the entries of the revision 2 change list (draft 4, as committed at HEAD).

Output: cl_entries.md in this folder (the frame is brought up to date by stage B). Every ruled text is cut from
its ruling file by program; every replacement asserts one occurrence.
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s93_lib import (CHANGE_LIST_REL, append_to_check, entry_span, fence_after, git_show, line_with, one,  # noqa
                     quoted_on_line, replace_in_entry, ruling)

cl = git_show(CHANGE_LIST_REL)
log = []


def note(message):
    log.append(message)
    print(message)


def entry_field_value(text, entry_id, field):
    start, end = entry_span(text, entry_id)
    return line_with(text[start:end], '- **%s:**' % field)


# ============================================================ X03 · W19.1 · FIX
r = ruling('X03')
new_new = fence_after(r, '- **The fix.** OLD is unchanged. NEW (132 words):')
new_decl = fence_after(r, 'KIND: CLAIM (unchanged). DECLARATION:')
check = quoted_on_line(r, 'S93 cross-examination: part F (X03).', '"', '"', from_line_start=True)
old_new = fence_after(cl, '- **NEW:**', start_marker='\n### W19.1 — ')
cl = replace_in_entry(cl, 'W19.1', '````text\n' + old_new + '\n````', '````text\n' + new_new + '\n````', 'NEW')
old_decl = entry_field_value(cl, 'W19.1', 'DECLARATION')
cl = replace_in_entry(cl, 'W19.1', old_decl, '- **DECLARATION:** ' + new_decl, 'DECLARATION')
cl = append_to_check(cl, 'W19.1', check)
note('X03 W19.1: NEW and DECLARATION replaced; CHECK line added')

# ============================================================ X04 · W35.1 · KEEP, with W35.5 and a REASON edit
r = ruling('X04')
check_block = fence_after(r, 'Words ready to paste:')
assert check_block.startswith('  - S93 cross-examination:'), check_block[:40]
cl = append_to_check(cl, 'W35.1', check_block[len('  - '):])
reason_old = quoted_on_line(r, "- OLD (inside W35.1's REASON): ", '`', '`')
reason_new = quoted_on_line(r, "- NEW: `Derivation 4's Claim", '`', '`')
cl = replace_in_entry(cl, 'W35.1', reason_old, reason_new, 'REASON (bookkeeping)')
w355 = fence_after(r, '- Text ready to paste:', fence='`````')
assert w355.startswith('### W35.5 — '), w355[:30]
start, end = entry_span(cl, 'W35.4')
cl = cl[:end] + w355 + '\n\n' + cl[end:]
note('X04 W35.1: CHECK line added; REASON sentence on Derivation 4 replaced; W35.5 inserted after W35.4')

# ============================================================ X05 · W35.2 · FIX
r = ruling('X05')
new_new = fence_after(r, '- **NEW:**', start_marker='### The FIX, ready to paste')
new_decl = fence_after(r, '- **DECLARATION:**', start_marker='### The FIX, ready to paste')
check = fence_after(r, '- **For the CHECK field (rule 12):**')
loss_add = fence_after(r, '- **For the LOSS field (optional, to keep the record whole):**')
old_new = fence_after(cl, '- **NEW:**', start_marker='\n### W35.2 — ')
cl = replace_in_entry(cl, 'W35.2', '````text\n' + old_new + '\n````', '````text\n' + new_new + '\n````', 'NEW')
old_decl = entry_field_value(cl, 'W35.2', 'DECLARATION')
cl = replace_in_entry(cl, 'W35.2', old_decl, '- **DECLARATION:** ' + new_decl, 'DECLARATION')
old_loss = entry_field_value(cl, 'W35.2', 'LOSS')
cl = replace_in_entry(cl, 'W35.2', old_loss, old_loss + ' ' + loss_add, 'LOSS')
cl = append_to_check(cl, 'W35.2', check)
note('X05 W35.2: NEW and DECLARATION replaced; LOSS sentence added; CHECK line added')

# ============================================================ X06 · W20.1 · FIX, with record edits
r = ruling('X06')
new_new = fence_after(r, '- **NEW:**', start_marker='### The FIX, exact')
new_decl = fence_after(r, '- **DECLARATION:**', start_marker='### The FIX, exact')
check_line = line_with(r, '  > S93 cross-examination: s93_xexam_mimo_H')
check = check_line[len('  > '):]
old_new = fence_after(cl, '- **NEW:**', start_marker='\n### W20.1 — ')
cl = replace_in_entry(cl, 'W20.1', '````text\n' + old_new + '\n````', '````text\n' + new_new + '\n````', 'NEW')
old_decl = entry_field_value(cl, 'W20.1', 'DECLARATION')
cl = replace_in_entry(cl, 'W20.1', old_decl, '- **DECLARATION:** ' + new_decl, 'DECLARATION')
cl = append_to_check(cl, 'W20.1', check)
# record edits (ruling, "Record edits that go with it")
assert 'in O7\'s CASES AT RISK, after "assigns an input and is named background", add "where the candidate does not ' \
       'offer it as doing the work; offered, it is a commitment, and O7 holds on both identifications (W20.2)"' in r
o7_add = 'where the candidate does not offer it as doing the work; offered, it is a commitment, and O7 holds on both ' \
         'identifications (W20.2)'
cl = replace_in_entry(cl, 'W20.1', 'assigns an input and is named background, and the salt',
                      'assigns an input and is named background ' + o7_add + ', and the salt', "O7's CASES AT RISK")
assert '"puts the components that assign inputs in the named background" becomes "puts the components outside Γ, ' \
       'including any that assign inputs, in the named background"' in r
cl = one(cl, 'W20.1 makes Γ a set of components and puts the components that assign inputs in the named background.',
         'W20.1 makes Γ a set of components and puts the components outside Γ, including any that assign inputs, in '
         'the named background.', 'finding on "active"')
closed_finding = (' **Closed after the S93 cross-examination:** NEW now reads "including any of them that assigns an '
                  'input", so only the second reading is left: the candidate\'s offer decides membership for every '
                  'component, as S88 settled (ruling S93 X06 W20.1, ruling 1).')
cl = one(cl, 'On the other, any such component that the candidate leaves out of Γ is named background. The named '
             'verdicts are the same on both (the F3 reading\'s models 1a and 1b).',
         'On the other, any such component that the candidate leaves out of Γ is named background. The named '
         'verdicts are the same on both (the F3 reading\'s models 1a and 1b).' + closed_finding,
         'finding on the two readings')
cl = replace_in_entry(cl, 'W20.1', 'The named verdicts are the same on both (models 1a and 1b). Carried forward below.',
                      'The named verdicts are the same on both (models 1a and 1b). Carried forward below. **Closed after '
                      'the S93 cross-examination:** NEW reads "including any of them that assigns an input", which '
                      'leaves only the second reading (ruling S93 X06 W20.1, ruling 1).', 'REASON, read in place')
note('X06 W20.1: NEW and DECLARATION replaced; CHECK line added; O7 line, the "active" finding, the two-readings '
     'finding and REASON bullet updated')

# ============================================================ X09 · W59.1 "Rivals" · FIX (NEW and DECLARATION)
r = ruling('X09')
phrase_old = fence_after(r, 'In NEW (the paragraph "Rivals"), replace', fence='```')
phrase_new = fence_after(r, '\nwith\n', fence='```', start_marker='In NEW (the paragraph "Rivals"), replace')
whole_rivals = fence_after(r, 'The paragraph "Rivals" of NEW then reads, whole:')
decl_old = fence_after(r, 'In DECLARATION, replace', fence='```')
decl_new = fence_after(r, '\nwith\n', fence='```', start_marker='In DECLARATION, replace')
whole_decl = fence_after(r, 'The whole DECLARATION then reads:')
check_line = line_with(r, '> S93 cross-examination: s93_xexam_atria_A (point 1, (c2))')
check = check_line[len('> '):]
start, end = entry_span(cl, 'W59.1')
section = cl[start:end]
section = one(section, phrase_old, phrase_new, 'X09 phrase in NEW')
section = one(section, decl_old, decl_new, 'X09 declaration sentence')
cl = cl[:start] + section + cl[end:]
# checks against the whole texts the ruling gives
w59_new = fence_after(cl, '- **NEW:**', start_marker='\n### W59.1 — ')
assert w59_new.split('\n')[0] == whole_rivals, 'Rivals paragraph differs from the ruling\'s whole text'
w59_decl = entry_field_value(cl, 'W59.1', 'DECLARATION')
assert w59_decl == '- **DECLARATION:** ' + whole_decl, 'declaration differs from the ruling\'s whole text'
cl = append_to_check(cl, 'W59.1', check)
note('X09 W59.1: "as when" -> "as none do when" in Rivals; declaration sentence 3 carries the bijection clause; '
     'both checked against the ruling\'s whole texts; CHECK line added')

# ============================================================ X10 · W59.1 "Problems" · KEEP
r = ruling('X10')
check = quoted_on_line(r, '**For the CHECK field (rule 12), a line the orchestrator may use:**',
                       '"', '"')
assert check.startswith('S93 cross-examination: X10'), check[:40]
cl = append_to_check(cl, 'W59.1', check)
note('X10 W59.1: KEEP; CHECK line added')

# ============================================================ X11 · new entry W61.1 · FIX (CLAIM)
r = ruling('X11')
x11_old = fence_after(r, '- **OLD:**', start_marker='## The proposed entry')
x11_new = fence_after(r, '- **NEW:**', start_marker='## The proposed entry')
x11_decl = fence_after(r, '- **DECLARATION:**', start_marker='**5. The entry as fixed.**')
x11_cases = line_with(r, '- **CASES AT RISK:** none moves.')[len('- **CASES AT RISK:** '):]
x11_where = line_with(r, '- **WHERE:** Part VII, "Production and direction" (L323), sentence 5.')[len('- **WHERE:** '):]
x11_check = quoted_on_line(r, '- **CHECK line** (rule 12), suggested:', '"', '"')
assert x11_check.startswith('S93 cross-examination: s93_xexam_mimo_I, point 1'), x11_check[:50]
assert '- **STATUS:** applied.' in r and '- **FILE-11 LINE:** 323.' in r and '- **REASON WORD:** erratum.' in r \
    and '- **KIND:** CLAIM.' in r
w611 = '\n'.join([
    '### W61.1 — L323 s5: the reversed calculation leaves the calculation\'s \\(L\\) unchanged, not its \\(H\\)',
    '',
    '- **STATUS:** applied',
    '- **GROUP:** S93 (entered after the S93 cross-examination; not one of the drafting groups)',
    '- **ITEM:** W61 (new: the slip log S92 recorded, proposed in the S93 reading rule and put to both readers as X11)',
    '- **FILE-11 LINE:** 323',
    '- **WHERE:** ' + x11_where,
    '- **REASON WORD:** erratum',
    '- **KIND:** CLAIM',
    '- **CHECK:** entered after the S93 cross-examination, as the ruling `results/S93 reading rulings/ruling S93 X11 '
    'proposed.md` gives its fields (its ruling 5). The reading rule proposed it as WORDING (its "What is '
    'cross-examined", third bullet, and rule 12); under rule 4 the checker\'s FIX sets the kind.',
    '  - ' + x11_check,
    '- **OLD:**',
    '````text',
    x11_old,
    '````',
    '- **NEW:**',
    '````text',
    x11_new,
    '````',
    '- **DECLARATION:** ' + x11_decl,
    '- **REASON:** Proposed in the S93 reading rule (`results/S93 How the cross-examination of draft 4 will be read - '
    'written before sending.md`, "What is cross-examined", third bullet) from the slip log S92 recorded, and ruled '
    'by `results/S93 reading rulings/ruling S93 X11 proposed.md`. The sentence names the wrong port: an edit that '
    'sets a port replaces the component assigning that port (file 11 L105), so intervening on \\(H\\) sets the '
    'reversed calculation\'s \\(H\\), and the mismatch that breaks (F2) is in \\(L\\), as Part V says of every reversed '
    'calculation (file 11 L273; the ruling, ruling 1). KIND CLAIM, not WORDING: OLD asserts a statement about a '
    'named port that is false in the theory\'s own terms and that NEW withdraws, as W6.1, W7.1 and W10a.1 are CLAIM '
    '(the ruling, ruling 2). REASON WORD erratum: a symbol is corrected (plan 1.1). OLD occurs once in file 11 (L323) '
    'and also stands in file 10 (L338), so no layer-2 row is affected; no other entry touches file-11 L323. File 12 '
    '(L325) carries the same slip; it is under no round, and nothing was written into `authority/`.',
    '- **CASES AT RISK:** ' + x11_cases,
    '- **GAIN / LOSS:** GAIN: Part VII names the port in which the reversed calculation fails (F2), as Part V does. '
    'LOSS: None; the verdict that the reversed calculation is not faithful under the production contract is '
    'unchanged (the ruling, rulings 1 and 3).',
    '',
    ''])
heading_w401 = '\n### W40.1 — '
assert cl.count(heading_w401) == 1
cl = cl.replace(heading_w401, '\n' + w611 + heading_w401[1:], 1)
note('X11: new entry W61.1 (CLAIM) inserted before W40.1')

# ============================================================ X14 · W60.1 · KEEP
r = ruling('X14')
check = quoted_on_line(r, 'S93 cross-examination: upheld by both readers (part C)', '"', '"', from_line_start=True)
assert check.startswith('S93 cross-examination: upheld by both readers (part C)')
cl = append_to_check(cl, 'W60.1', check)
note('X14 W60.1: KEEP; CHECK line added')

# ============================================================ X17 · W7.5 · FIX, with bookkeeping
r = ruling('X17')
x17_old = fence_after(r, '- **OLD:**', start_marker='**The FIX** (OLD, NEW and DECLARATION replaced')
x17_new = fence_after(r, '- **NEW:**', start_marker='**The FIX** (OLD, NEW and DECLARATION replaced')
x17_decl = fence_after(r, '- **DECLARATION:**', start_marker='**The FIX** (OLD, NEW and DECLARATION replaced')
x17_heading = quoted_on_line(r, '  - The heading becomes `', '`', '`')
x17_where = quoted_on_line(r, '  - WHERE becomes `', '`', '`')
x17_check = quoted_on_line(r, '- *CHECK, a new line:*', '"', '"')
x17_reason = quoted_on_line(r, '- *REASON, a new bullet:*', '"', '"')
x17_cases = quoted_on_line(r, '- *CASES AT RISK, a new line:*', '"', '"')
x17_gain = quoted_on_line(r, '- *GAIN, added:*', '"', '"')
x17_loss = quoted_on_line(r, '- *LOSS, added:*', '"', '"')
start, end = entry_span(cl, 'W7.5')
section = cl[start:end]
old_heading = section.split('\n')[0]
section = one(section, old_heading, x17_heading, 'X17 heading')
section = one(section, line_with(section, '- **WHERE:**'), x17_where, 'X17 WHERE')
old_old = fence_after(section, '- **OLD:**')
section = one(section, '````text\n' + old_old + '\n````', '````text\n' + x17_old + '\n````', 'X17 OLD')
old_new = fence_after(section, '- **NEW:**')
section = one(section, '````text\n' + old_new + '\n````', '````text\n' + x17_new + '\n````', 'X17 NEW')
section = one(section, line_with(section, '- **DECLARATION:**'), '- **DECLARATION:** ' + x17_decl, 'X17 DECLARATION')
# REASON: a new bullet at the end of the REASON block
at = section.index('\n- **CASES AT RISK:**') + 1
section = section[:at] + '  - ' + x17_reason + '\n' + section[at:]
# CASES AT RISK: a new line at the end of its block
at = section.index('\n- **GAIN:**') + 1
section = section[:at] + '  - ' + x17_cases + '\n' + section[at:]
gain_line = line_with(section, '- **GAIN:**')
section = one(section, gain_line, gain_line + ' After the S93 cross-examination: ' + x17_gain, 'X17 GAIN')
loss_line = line_with(section, '- **LOSS:**')
section = one(section, loss_line, loss_line + ' After the S93 cross-examination: ' + x17_loss, 'X17 LOSS')
cl = cl[:start] + section + cl[end:]
cl = append_to_check(cl, x17_heading[4:].split(' — ')[0], x17_check)
# "Found in draft 4", first bullet (the ruling: "can say that the placement is now made, in W7.5, after the (RC)
# sentence. The candidate at the free sentence is not taken, and the free sentence stays free.")
found_first = ('(S), (B), (D) depend on (E); rivals and the problems they pose (Part VI) on (F1), (F2), (A), (E), '
               'histories and receipts."')
cl = one(cl, found_first, found_first + ' **After the S93 cross-examination:** the placement is now made, in W7.5, '
         'after the (RC) sentence (ruling S93 X17 W7.5). The candidate at the free sentence is not taken, and the free '
         'sentence stays free.', '"Found in draft 4", first bullet')
note('X17 W7.5: heading, WHERE, OLD, NEW and DECLARATION replaced; REASON bullet, CASES AT RISK line, GAIN and LOSS '
     'added; CHECK line added; "Found in draft 4" first bullet updated')

# ============================================================ X18 · W38.1 · FIX (one line of the sources note)
r = ruling('X18')
x18_old = fence_after(r, 'OLD:', start_marker='**FIX.** In W38.1\'s NEW')
x18_new = fence_after(r, 'NEW:', start_marker='**FIX.** In W38.1\'s NEW')
x18_check = quoted_on_line(r, '*For the CHECK field (rule 12), if wanted:*', '"', '"')
cl = replace_in_entry(cl, 'W38.1', '\n' + x18_old + '\n', '\n' + x18_new + '\n', 'X18 line of NEW')
cl = append_to_check(cl, 'W38.1', x18_check)
note('X18 W38.1: the Surprise-and-problems line of NEW replaced; CHECK line added')

# ============================================================ the eight items upheld by both readers
UPHELD = [('X01', 'W37.1', 'F'), ('X02', 'W36.1', 'D'), ('X07', 'W34.1', 'D'), ('X08', 'W33.1', 'D'),
          ('X12', 'W40.1', 'I'), ('X13', 'W24.1', 'J'), ('X15', 'W22.1', 'J'), ('X16', 'W6.3', 'K')]
for item, entry_id, part in UPHELD:
    line = ('S93 cross-examination: upheld by both readers (s93_xexam_atria_%s, s93_xexam_mimo_%s); not thereby '
            'confirmed.' % (part, part))
    cl = append_to_check(cl, entry_id, line)
    note('%s %s: upheld-by-both line added (part %s)' % (item, entry_id, part))

# ============================================================ bookkeeping: N7 is O58 under D8
dated = (' (Corrected on 25 September 2026, after the S93 cross-examination, from "N7 (O59)": under D8 N7 is O58 and '
         'O59 is N8. Bookkeeping; no verdict or reading changes.)')
assert cl.count('N7 (O59)') == 2
cl = replace_in_entry(cl, 'W34.1', '  - **N7 (O59).** ', '  - **N7 (O58).**' + dated + ' ', 'N7 in W34.1')
cl = replace_in_entry(cl, 'W59.1', '  - **N7 (O59): holds; the watch is narrowed.** ',
                      '  - **N7 (O58): holds; the watch is narrowed.**' + dated + ' ', 'N7 in W59.1')
assert 'N7 (O59)' not in cl.replace('from "N7 (O59)"', '')
note('bookkeeping: "N7 (O59)" -> "N7 (O58)" in W34.1 and W59.1, with a dated note')

(HERE / 'cl_entries.md').write_text(cl, encoding='utf-8')
print('written', HERE / 'cl_entries.md')
