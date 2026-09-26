"""Step 3 and 4: the wordings of the S90 and S93 rulings (FIX wordings, and wordings the readers proposed
that a ruling kept out), the findings the change list carries forward with wording, and the worklist items
whose wording never became an entry. Reads step1.jsonl (for the change-list rids) and writes step2.jsonl.
Every quoted wording is cut from its source file by program (cut/fence/lit), never retyped; each 'old' is
checked to occur in the text it is written against."""
import sys, os, re, json, difflib
sys.path.insert(0, os.path.dirname(__file__))
from lib_c import *

S1 = [json.loads(l) for l in open(SP + '/step1.jsonl', encoding='utf-8')]
START = int(S1[-1]['rid'].split('-')[1]) + 1
vers = {c: {e['id']: e for e in parse_changelist(open(SP + '/cl/' + c + '.md', encoding='utf-8').read())} for c, *_ in CL_VERSIONS}

# ---------- texts ----------
T = {lab: Text(p, lab) for lab, p in TEXTS}
TX = {
    'f11': ('file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923)', Text(F11)),
    'd2': ('file 13 draft 2 (as sent), theory text (md5 9aecf2f30ce0b4523606b2b8409fdf37)', T['file 13 draft 2 (as sent)']),
    'd4': ('file 13 draft 4, theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17)', T['file 13 draft 4']),
    'f12': ('file 12 (authority/12 Claude Fable Semantics - causality, standalone theory.md)', Text('authority/12 Claude Fable Semantics - causality, standalone theory.md')),
}
NOTE = {
    'note2': ('the note of file 13, its list of changes of claim (full file 13 draft 2; the DECLARATION fields of change list draft 2)',
              '\n'.join(e['fields'].get('DECLARATION', '') for e in vers['587eebf'].values())),
    'note4': ('the note of file 13, its list of changes of claim (full file 13 draft 4; the DECLARATION fields of change list draft 4)',
              '\n'.join(e['fields'].get('DECLARATION', '') for e in vers['3f7c3ab'].values())),
    'src2': ('the note of sources and departures (full file 13 draft 2, meta block; W38.1 NEW in change list draft 2)', vers['587eebf']['W38.1']['NEW']),
    'src4': ('the note of sources and departures (full file 13 draft 4, meta block; W38.1 NEW in change list draft 4)', vers['3f7c3ab']['W38.1']['NEW']),
}
NOTE_PART = {'note2': 'Front matter (before Part 0) / the note of file 13, the declaration of %s',
             'note4': 'Front matter (before Part 0) / the note of file 13, the declaration of %s',
             'src2': 'Front matter (before Part 0) / the note of sources and departures%s',
             'src4': 'Front matter (before Part 0) / the note of sources and departures%s'}

problems = []
srcs_used = {}

# ---------- cutting helpers ----------

def src(path):
    srcs_used[path] = md5(path)
    return read(path)


def cut(path, before, after, line=None):
    t = src(path)
    if line:
        t = t.split('\n')[line - 1]
    i = t.find(before)
    if i < 0 or t.count(before) != 1:
        problems.append('cut: marker %r found %d times in %s' % (before[:40], t.count(before), path))
        if i < 0:
            return None
    i += len(before)
    j = t.find(after, i) if after else len(t)
    if j < 0:
        problems.append('cut: end marker %r not found in %s' % (after[:40], path))
        return None
    return t[i:j]


def fence(path, line):
    lines = src(path).split('\n')
    m = re.match(r'^(\s*)(~~~~+|````+)(\w*)\s*$', lines[line - 1])
    if not m:
        problems.append('fence: no fence at %s L%d' % (path, line))
        return None
    ind, ticks = m.group(1), m.group(2)
    buf = []
    j = line
    while j < len(lines) and lines[j].strip() != ticks:
        buf.append(lines[j][len(ind):] if lines[j].startswith(ind) else lines[j])
        j += 1
    return '\n'.join(buf)


def lit(path, s):
    if s not in src(path):
        problems.append('lit: %r not found in %s' % (s[:60], path))
    return s


# ---------- rids of the change-list records ----------

def rid_for(eid, commit):
    """The step-1 record whose new is the entry's NEW in that change-list version."""
    e = vers[commit].get(eid)
    if not e:
        return None
    for r in S1:
        if r['new'] == e.get('NEW') and ('entry %s' % eid) in r['source_ref'] and r['kind'] == 'edit':
            return r['rid']
    return None


rid_n = [START]
recs = []


def nrid():
    r = 'C-%d' % rid_n[0]
    rid_n[0] += 1
    return r


def carried(s):
    if not s:
        return []
    return [lab for lab, t in T.items() if t.count(s) >= 1]


def locate(tkey, old, anchor):
    """target_line, target_part, old_sentence for a theory text key."""
    label, tx = TX[tkey]
    probe = old or anchor
    if not probe:
        return None, '', ''
    n = tx.count(probe)
    if n == 0:
        problems.append('%s: %r not found in %s' % ('old' if old else 'anchor', probe[:70], tkey))
        return None, '', ''
    r = tx.sentences_around(probe) if n == 1 else None
    if r is None:
        line = tx.line_of(tx.raw.index(probe))
        sent = ''
    else:
        line, _, sent, _, _ = r
    part = tx.part.get(line, '')
    if part.startswith('Front matter'):
        part = 'Front matter (before Part 0)'
    return line, part, sent if old else ''


def add(round_, source_file, ref, kind, status, applied_in, tkey, old, new, scope, anchor=None, same_as=(), part_note='', new_sentence=None):
    if old is None or new is None:
        problems.append('record skipped (cut failed): ' + ref[:80])
        return None
    if tkey in TX:
        label = TX[tkey][0]
        line, part, osent = locate(tkey, old, anchor)
        nsent = ''
        if osent and old and not new.startswith('[no wording given]'):
            nsent = osent.replace(old, new, 1)
        if new_sentence is not None:
            nsent = new_sentence
    else:
        label, body = NOTE[tkey]
        line, osent, nsent = None, '', ''
        probe = old or anchor
        if probe and probe not in body:
            problems.append('note: %r not found in %s' % (probe[:70], tkey))
        if old:
            # the whole declaration or note line containing old
            for para in body.split('\n'):
                if old in para:
                    osent = para
                    break
            if osent and not new.startswith('[no wording given]'):
                nsent = osent.replace(old, new, 1)
        part = NOTE_PART[tkey] % part_note
    r = {'rid': nrid(), 'round': round_, 'source_file': source_file, 'source_ref': ref, 'kind': kind,
         'status': status, 'applied_in': applied_in, 'target_text': label, 'target_line': line,
         'target_part': part, 'old': old, 'new': new, 'old_sentence': osent, 'new_sentence': nsent,
         'scope': scope, 'same_as': [s for s in same_as if s]}
    recs.append(r)
    return r['rid']


# ---------- 3a. FIX wordings, read off the drafts they changed ----------
RS = 'results/S90 reading rulings/'
R93 = 'results/S93 reading rulings/'
FIX90 = {  # entry -> list of (ruling file, ref)
    'W37.1': [(RS + 'ruling s90_xexam_mimo_A1 R01.md', 'S90 ruling R01 (W37.1) on s90_xexam_mimo_A1 point 3: FIX (batch 1)'),
              (RS + 'ruling s90_xexam_atria_A1 item 1 R01.md', 'S90 ruling R01 (W37.1) on s90_xexam_atria_A1 point 1: FIX, the same text as batch 1 (batch 3)')],
    'W19.1': [(RS + 'ruling s90_xexam_mimo_A1 R08.md', 'S90 ruling R08 (W19.1) on s90_xexam_mimo_A1 point 1: FIX (batch 1)')],
    'W20.1': [(RS + 'ruling s90_xexam_mimo_A1 R15.md', 'S90 ruling R15 (W20.1) on s90_xexam_mimo_A1 point 2: FIX (batch 1)')],
    'W22.1': [(RS + 'ruling s90_xexam_mimo_A2 R28.md', 'S90 ruling R28 (W22.1) on s90_xexam_mimo_A2 point 1: FIX (batch 1)')],
    'W24.1': [(RS + 'ruling s90_xexam_mimo_A2 R26.md', 'S90 ruling R26 (W24.1) on s90_xexam_mimo_A2 point 4: FIX, wording only (batch 1)')],
    'W35.1': [(RS + 'ruling s90_xexam_mimo_C item 1 R12.md', 'S90 ruling R12 (W35.1) on s90_xexam_mimo_C point 1: FIX (batch 3)')],
    'W35.2': [(RS + 'ruling s90_xexam_mimo_C item 4 R13.md', 'S90 ruling R13 (W35.2) on s90_xexam_mimo_C point 4: FIX; the batch-3 reading takes this text over Atria C item 1\'s (Reconciliation, item 3)')],
    'W7.5': [(RS + 'ruling s90_xexam_mimo_B1 item 3 R48.md', 'S90 ruling R48 (W7.5) on s90_xexam_mimo_B1 point 3: FIX (batch 2)')],
}
FIX93 = {
    'W19.1': (R93 + 'ruling S93 X03 W19.1.md', 'S93 ruling X03 (W19.1), challenge 2 (Mimo F point 2): FIX'),
    'W35.2': (R93 + 'ruling S93 X05 W35.2.md', 'S93 ruling X05 (W35.2) on Mimo G point 1: FIX'),
    'W20.1': (R93 + 'ruling S93 X06 W20.1.md', 'S93 ruling X06 (W20.1), ruling 1 and the "boundary conditions" fix: FIX'),
    'W59.1': (R93 + 'ruling S93 X09 W59.1 Rivals.md', 'S93 ruling X09 (W59.1, "Rivals"), ruling 2 (Mimo A point 2): FIX'),
    'W61.1': (R93 + 'ruling S93 X11 proposed.md', 'S93 ruling X11 (proposed; entered as W61.1): FIX, entered as CLAIM with OLD and NEW as proposed'),
    'W7.5': (R93 + 'ruling S93 X17 W7.5.md', 'S93 ruling X17 (W7.5), point 2 (Atria K point 1, Mimo K point 2): FIX'),
    'W35.5': (R93 + 'ruling S93 X04 W35.1.md', 'S93 ruling X04 (W35.1): KEEP, with the companion entry W35.5 proposed by the checker on Mimo G point 2'),
}


def word_span(a, b):
    ta = re.findall(r'\S+|\s+', a)
    tb = re.findall(r'\S+|\s+', b)
    p = 0
    while p < len(ta) and p < len(tb) and ta[p] == tb[p]:
        p += 1
    q = 0
    while q < len(ta) - p and q < len(tb) - p and ta[-1 - q] == tb[-1 - q]:
        q += 1
    return ''.join(ta[:p]), ''.join(ta[p:len(ta) - q]), ''.join(tb[p:len(tb) - q]), ''.join(ta[len(ta) - q:])


def sent_cover(line, s0, s1):
    """The whole sentences of 'line' that overlap [s0, s1)."""
    spans = split_spans(line)
    lo = hi = None
    for x, y in spans:
        if y + 1 > s0 and x <= max(s0, s1 - 1):
            lo = x if lo is None else lo
            hi = y
    if lo is None:
        return ''
    return line[lo:hi]


def line_fix_records(dA, dB, fixmap, round_, entry_commit, tkey):
    A, B = T[dA].lines, T[dB].lines
    sm = difflib.SequenceMatcher(None, A, B, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            continue
        if not (op == 'replace' and i2 - i1 == j2 - j1):
            problems.append('line diff %s->%s: %s %d-%d / %d-%d not a one-for-one replacement' % (dA, dB, op, i1 + 1, i2, j1 + 1, j2))
            continue
        for k in range(i2 - i1):
            la, lb = A[i1 + k], B[j1 + k]
            pre, so, sn, suf = word_span(la, lb)
            # which entry: the entry whose NEW (after) contains the changed new span with its context
            probe = lb[max(0, len(pre) - 40): len(pre) + len(sn) + 40]
            ents = [eid for eid in fixmap if vers[entry_commit].get(eid) and probe.strip() and probe.strip()[:60] in vers[entry_commit][eid]['NEW']]
            if len(ents) != 1:
                ents = [eid for eid in fixmap if vers[entry_commit].get(eid) and sn.strip() and sn.strip() in vers[entry_commit][eid]['NEW'] and (so.strip() == '' or so.strip() in (vers[entry_commit][eid]['NEW'] + vers[entry_commit][eid].get('OLD', '')) or True)]
            if len(ents) != 1:
                problems.append('line diff %s->%s L%d: entry not identified (%s)' % (dA, dB, i1 + k + 1, ents))
                continue
            eid = ents[0]
            osent = sent_cover(la, len(pre), len(pre) + max(len(so), 1))
            nsent = sent_cover(lb, len(pre), len(pre) + max(len(sn), 1))
            so_s, sn_s = so.strip(), sn.strip()
            scope = 'span'
            if so_s == '' or sn_s == '':
                scope = 'sentence' if re.search(r'[.;:]$', (sn_s or so_s)) else 'span'
            if so_s and so_s == osent.strip():
                scope = 'sentence'
            now_in = carried(nsent)
            status = 'applied' if 'file 13 draft 5' in now_in else 'superseded'
            same = rid_for(eid, entry_commit)
            tlab = TX[tkey][0]
            part = T[dA].part.get(i1 + k + 1, '')
            fixes = fixmap[eid] if isinstance(fixmap[eid], list) else [fixmap[eid]]
            for path, ref in fixes:
                src(path)
                recs.append({'rid': nrid(), 'round': round_, 'source_file': path,
                             'source_ref': '%s; the wording as applied in %s (entry %s, %s); read off the line diff %s -> %s at line %d' % (ref, dB, eid, same, dA, dB, i1 + k + 1),
                             'kind': 'recommendation', 'status': status,
                             'applied_in': '; '.join(now_in) if now_in else 'none',
                             'target_text': tlab, 'target_line': i1 + k + 1, 'target_part': part,
                             'old': so_s, 'new': sn_s, 'old_sentence': osent, 'new_sentence': nsent,
                             'scope': scope, 'same_as': [same] if same else []})


line_fix_records('file 13 draft 2 (as sent)', 'file 13 draft 3', FIX90, 'S90', '99e9cd0', 'd2')
line_fix_records('file 13 draft 4', 'file 13 draft 5', FIX93, 'S93', '8816fcf', 'd4')

# X18: the one line of the sources note the S93 fix changed
a4, a5 = vers['3f7c3ab']['W38.1']['NEW'].split('\n'), vers['8816fcf']['W38.1']['NEW'].split('\n')
for x, y in zip(a4, a5):
    if x != y:
        pre, so, sn, suf = word_span(x, y)
        add('S93', R93 + 'ruling S93 X18 W38.1.md', 'S93 ruling X18 (W38.1), ruling 3 (Mimo E points 1 and 2): FIX, one line of the note (*Surprise and problems*); the wording as applied in change list draft 5 (W38.1, C-2)',
            'recommendation', 'applied', 'full file 13 draft 5, meta block (the note of sources and departures)', 'src4', so.strip(), sn.strip(), 'span',
            same_as=[rid_for('W38.1', '8816fcf')], part_note=' / *Surprise and problems*')
        src(R93 + 'ruling S93 X18 W38.1.md')

# declaration-only FIX wordings of the S90 rulings (the note)
C89 = next(r['rid'] for r in S1 if 'entry W40.1, DECLARATION' in r['source_ref'])
C90 = next(r['rid'] for r in S1 if 'entry W6.3, DECLARATION' in r['source_ref'])
d40_2, d40_3 = vers['587eebf']['W40.1']['fields']['DECLARATION'], vers['99e9cd0']['W40.1']['fields']['DECLARATION']
pre, so, sn, suf = word_span(d40_2, d40_3)
add('S90', RS + 'ruling s90_xexam_atria_C item 5 R25.md', 'S90 ruling R25 (W40.1) on s90_xexam_atria_C point 3: FIX, declaration only; the batch-3 reading takes this FIX over Mimo C item 5\'s KEEP (Reconciliation, item 4)',
    'recommendation', 'applied', 'full file 13 drafts 3 to 5, the note (its list of changes of claim)', 'note2', so.strip(), sn.strip(), 'span', same_as=[C89], part_note='W40.1 (file-11 L337, Part VII / Explanations that remove structure)')
d63 = vers['99e9cd0']['W6.3']['fields']['DECLARATION']
for path, ref in ((RS + 'ruling s90_xexam_atria_B1 R39.md', 'S90 ruling R39 (W6.3) on s90_xexam_atria_B1 point 1: FIX, KIND WORDING -> CLAIM and declaration added (batch 1)'),
                  (RS + 'ruling s90_xexam_mimo_B1 item 2 R39.md', 'S90 ruling R39 (W6.3) on s90_xexam_mimo_B1 point 2: FIX, one ruling with batch 1\'s (batch 2)')):
    lit(path, d63)
    add('S90', path, ref, 'recommendation', 'applied', 'full file 13 drafts 3 to 5, the note (its list of changes of claim)', 'note2', '', d63, 'sentence',
        anchor=None, same_as=[C90], part_note='W6.3 (file-11 L447 s3, Part XI)')

# Atria C item 1's own text for R13, not taken
atria_r13 = fence(RS + 'ruling s90_xexam_atria_C item 1 R13.md', 106)
old13 = vers['587eebf']['W35.2']['NEW']
pre, so, sn, suf = word_span(old13, atria_r13 or '')
add('S90', RS + 'ruling s90_xexam_atria_C item 1 R13.md', 'S90 ruling R13 (W35.2) on s90_xexam_atria_C point 1: FIX with this text ("NEW (corrected)"); the batch-3 reading takes Mimo C item 4\'s text instead (Reconciliation, item 3: "to the simulation layer" and "a constructed one")',
    'recommendation', 'declined', 'none', 'd2', so.strip(), sn.strip(), 'span')

# ---------- 3b. wordings the readers proposed (S90) ----------
P = 'results/S90 Cross-examination - revision 2 draft - returns/parts/'
B1 = 'results/S90 Reading of the replies - batch 1 (Mimo A1, Mimo A2, Atria B1).md'
B2 = 'results/S90 Reading of the replies - batch 2 (Atria A2, Mimo B1).md'
B3 = 'results/S90 Reading of the replies - batch 3 (Mimo B2, Mimo C, Atria B2, Atria A1, Atria C).md'
ma1, ma2, mb1, mb2, mc = P + 's90_xexam_mimo_A1.response.txt', P + 's90_xexam_mimo_A2.response.txt', P + 's90_xexam_mimo_B1.response.txt', P + 's90_xexam_mimo_B2.response.txt', P + 's90_xexam_mimo_C.response.txt'
aa1, ab1, ac = P + 's90_xexam_atria_A1.response.txt', P + 's90_xexam_atria_B1.response.txt', P + 's90_xexam_atria_C.response.txt'
W19_2 = vers['587eebf']['W19.1']['NEW']
fix_rid = {}
for r in recs:
    m = re.search(r'\(entry (\S+(?: \+ \S+)?), ', r['source_ref'])
    if m:
        fix_rid.setdefault((m.group(1), r['round']), []).append(r['rid'])

add('S90', RS + 'ruling s90_xexam_mimo_A1 R08.md', 'S90 ruling R08 (W19.1): the reply\'s first repair (s90_xexam_mimo_A1 point 1), refused: the two OLDs would overlap and the kind definition would leave (K) (batch 1)',
    'recommendation', 'declined', 'none', 'd2', '', '[no wording given] move the two new sentences after (K) to Part V, immediately after the transport t=(π,τ,σ,λ) is defined', 'paragraph',
    anchor='are of one kind on \\(C\\) when their signatures, read on \\(C\\) through \\(\\tau\\) and \\(\\tau\'\\), coincide')
g = cut(ma1, 'or gloss inline: "', '".', line=23)
add('S90', ma1, 's90_xexam_mimo_A1 point 1, second repair (a gloss inline); ruling R08 (W19.1) inserted a typing sentence in Part IV\'s and Part V\'s own words instead (batch 1); the checker\'s wording is ' + ','.join(fix_rid.get(('W19.1', 'S90'), [])),
    'recommendation', 'declined', 'none', 'd2', '', g, 'span', anchor='through \\(\\tau\\) and \\(\\tau\'\\), coincide')
add('S90', ma1, 's90_xexam_mimo_A1 point 2, proposed repair; ruling R15 (W20.1) takes only its second half, in the words of file-11 L309 s3, and refuses "identifies as active" ("active" is undefined, and Γ would be circular) (batch 1)',
    'recommendation', 'declined', 'none', 'd2', lit(ma1, 'those the candidate offers as doing the work'), cut(ma1, 'with "', '."', line=33), 'span',
    same_as=fix_rid.get(('W20.1', 'S90'), []))
add('S90', ma1, 's90_xexam_mimo_A1 point 3, proposed repair (delete "blind"); taken by ruling R01 (W37.1) (batch 1), and by the R01 ruling on Atria A1 (batch 3)',
    'recommendation', 'superseded', 'file 13 draft 3; file 13 draft 4; file 13 draft 5; scrubbed copy; repaired copy; latest text',
    'd2', 'produced by blind variation and survival on a history of encountered changes, with no represented target in that history', cut(ma1, 'leaving: "', '." This', line=43), 'span',
    same_as=fix_rid.get(('W37.1', 'S90'), []))
recs[-1]['status'] = 'applied'
add('S90', RS + 'ruling s90_xexam_atria_A1 item 1 R01.md', 'S90 ruling R01 (W37.1): s90_xexam_atria_A1 point 1, second repair (write blindness into Part IV\'s Selected), refused as an undeclared change of claim to the body (batch 3)',
    'recommendation', 'declined', 'none', 'd2', '', '[no wording given] add blindness (of the variation) to Part IV\'s definition of a selected transport', 'sentence',
    anchor='No member of the history represents \\(t\\), \\(H\\), or the survival condition')
add('S90', ma1, 's90_xexam_mimo_A1 point 4 (task (c)), not ruled (Parts rule 2): passed to the orchestrator as a notation point (batch 1); carried forward after S90 in the change list ("The letter G"). The reply: "' + lit(ma1, "Rename R17's block to a fresh symbol (e.g. \\(\\mathcal G\\) or \\(g_0\\)).") + '"',
    'recommendation', 'not applied', 'none', 'd2', 'a nonempty block \\(G\\subseteq\\Gamma\\)', '[no wording given] a fresh symbol for the block G of non-circular dependence, for example \\(\\mathcal G\\) or \\(g_0\\)', 'term')
add('S90', RS + 'ruling s90_xexam_atria_A1 item 2 R17.md', 'S90 ruling R17 (W20.2), on s90_xexam_atria_A1 point 3: passed to the orchestrator as an optional notation point, "a possible wording"; if adopted, a new entry (batch 3); carried forward after S90 ("Revised L339 names no block")',
    'recommendation', 'not applied', 'none', 'd2', 'witnessed by \\(I_3\\) under removal of skewness', lit(RS + 'ruling s90_xexam_atria_A1 item 2 R17.md', 'witnessed by \\(I_3\\) under removal of skewness, with the skewness commitment as the deleted block, …'), 'span')
add('S90', ma2, 's90_xexam_mimo_A2 point 1, repair; refused by ruling R28 (W22.1): a fifth part for every criticism, p used before it is bound, and a conflict with W22.2 (batch 1)',
    'recommendation', 'declined', 'none', 'd2',
    'A criticism has target \\(z\\), alleged defect \\(\\delta\\), grounds \\(g\\), and a connection. ' + vers['587eebf']['W22.1']['NEW'],
    cut(ma2, 'relatum: "', '"', line=7), 'sentence',
    same_as=fix_rid.get(('W22.1', 'S90'), []))
add('S90', ma2, 's90_xexam_mimo_A2 point 2 (R55 with R51), not ruled (Parts rule 2): an inserted clause exhibiting the bijection, passed to the orchestrator (batch 1); Atria A2 point 1 exhibits the same bijection with no words (batch 2); carried forward after S90 ("R55\'s bijection"). The words are to go after "the second transport (Derivation 8);"',
    'recommendation', 'not applied', 'none', 'd2', '', src(ma2).split('\n')[10].split('insert: "', 1)[1].rstrip().rstrip('"'), 'span',
    anchor='carries the fidelity and the answers of \\(t_1\\) over to the second transport (Derivation 8);', new_sentence='')
add('S90', RS + 'ruling s90_xexam_mimo_A2 R51.md', 'S90 ruling R51 (W19.2), "Not ruled, and outside the argument": the orchestrator\'s option, a one-word change to the declaration (batch 1); batch 2 kept it as an option; carried forward after S90 ("W19.2\'s declaration")',
    'recommendation', 'not applied', 'none', 'note2', 'Its Consequence now covers only candidates that differ in which component carries which anchor.',
    lit(RS + 'ruling s90_xexam_mimo_A2 R51.md', 'Its Consequence now covers only candidates that differ in nothing but which component carries which anchor.'), 'span', part_note='W19.2 (file-11 L552-558, Part XVI / 2. Same anchors, one account)')
add('S90', ab1, 's90_xexam_atria_B1 point 1, repair; ruling R39 (W6.3) upholds the kind and refuses both repairs: folding would renumber and merge two disjoint OLDs, and R38\'s declaration says "primitive 2", which R39\'s NEW does not (batch 1)',
    'recommendation', 'declined', 'none', 'note2', '', '[no wording given] ' + lit(ab1, 're-declare R39 as CLAIM with R38\'s declaration, or fold R39 into R38'), 'sentence',
    part_note='W6.3 (file-11 L447 s3, Part XI)')
add('S90', mb1, 's90_xexam_mimo_B1 point 2, repair (a declaration); refused by ruling R39 (W6.3) in favour of batch 1\'s declaration (batch 2)',
    'recommendation', 'declined', 'none', 'note2', '', cut(mb1, 'declaration: *"', '"*', line=25), 'sentence', same_as=[C90], part_note='W6.3 (file-11 L447 s3, Part XI)')
add('S90', mb1, 's90_xexam_mimo_B1 point 1, first repair (retype R04 as CLAIM, with this declaration); refused by ruling R04 (W58(ii).1): KEEP (batch 2)',
    'recommendation', 'declined', 'none', 'note2', '', cut(mb1, 'declaration: *"', '"*', line=15), 'sentence', part_note='W58(ii).1 (file-11 L33 s4, Part 0 / What is primitive, what is an index, and what is derived)')
add('S90', mb1, 's90_xexam_mimo_B1 point 1, second repair (keep WORDING and strengthen the wording); refused by ruling R04 (W58(ii).1): "exists in the theory" is false against the text\'s own definitions (batch 2)',
    'recommendation', 'declined', 'none', 'd2', 'No predicate meaning "really explains", "is a cause" or "is knowledge" is taken as primitive, and no definition depends on one (Derivation 6).',
    cut(mb1, 'Derivation 6: *"', '"*', line=15), 'sentence')
add('S90', mb1, 's90_xexam_mimo_B1 point 3, suggested repair for the shared clause; ruling R48 (W7.5) refuses the rewording for (P) (it would drop (G), (E) and Deploy from (P)) and takes only "(EK) also on (P)" in its own words (batch 2)',
    'recommendation', 'declined', 'none', 'd2', '(P), (EK) depend on (G), (E), Deploy; (P) also on ProducedBy and on the declared obligations with their occasions, and ProducedBy on histories and their active routes.',
    cut(mb1, 'shared clause: *"', '"*', line=37), 'sentence', same_as=fix_rid.get(('W7.5', 'S90'), []))
add('S90', mb1, 's90_xexam_mimo_B1 point 4 (R10, W57.1 + W32(b).1), a gloss; not contested and not ruled: passed to the orchestrator (batch 2); carried forward after S90 ("The ground of its restriction")',
    'recommendation', 'not applied', 'none', 'd2', 'Where the claim states the ground of its restriction, a verdict on the restriction is given with that ground; where it states none and a verdict turns on one, the ground is a missing declared input (Part XIV).',
    cut(mb1, '**Repair:** *"', '"*', line=43), 'sentence')
add('S90', mb1, 's90_xexam_mimo_B1 point 5 (R03, W7.1), a minimal gloss; not contested and not ruled: passed to the orchestrator (batch 2); carried forward after S90 ("Bolded declared inputs at revised L31")',
    'recommendation', 'not applied', 'none', 'd2', 'and the **declared inputs**, in the order Part XIV states.', cut(mb1, 'indices sentence: *"', '"*', line=47), 'span', new_sentence='')
add('S90', mb2, 's90_xexam_mimo_B2 point 1, proposed repair; refused by ruling R31 (W21.1): KEEP, the repair would make c new whenever an earlier content commits beyond c (batch 3)',
    'recommendation', 'declined', 'none', 'd2', 'both faithful on \\(c\\)\'s contract at grain \\(\\ell\\)', cut(mb2, 'with "', '." This', line=21), 'span')
add('S90', mb2, 's90_xexam_mimo_B2 point 1, the declaration as the reply would reword it; refused with the repair by ruling R31 (W21.1) (batch 3)',
    'recommendation', 'declined', 'none', 'note2', '', src(mb2).split('\n')[20].split('would then read: "', 1)[1].rstrip().rstrip('"'), 'sentence', part_note='W21.1 (file-11 L405, Part X / Newness)')
add('S90', RS + 'ruling s90_xexam_mimo_B2 item 1 R31.md', 'S90 ruling R31 (W21.1), "Noted for the owner, not ruled": a sentence at Part IV (L189) or at (R) (L205-208); outside the 55 changes (batch 3); carried forward after S90 ("When a transport into c is faithful on c\'s contract")',
    'recommendation', 'open for the owner', 'none', 'd2', '',
    lit(RS + 'ruling s90_xexam_mimo_B2 item 1 R31.md', 'a transport into c is faithful on c\'s contract when it is faithful on the pairs it carries into that contract'), 'sentence',
    anchor='**Representation.**' if TX['d2'][1].count('**Representation.**') == 1 else 'Representation')
add('S90', mb2, 's90_xexam_mimo_B2 point 2 (R52, W17.3), a one-line addition to the declaration; not taken by ruling R52: KEEP, it would declare a weakening the text does not make (batch 3)',
    'recommendation', 'declined', 'none', 'note2', '', lit(mb2, '—the separate realizability condition is dropped.'), 'span', part_note='W17.3 (file-11 L562 s3, Part XVI / 3.)')
add('S90', mc, 's90_xexam_mimo_C point 1, first repair (restrict the declaration); ruling R12 (W35.1) adopts the scoping, and its declaration reads "for every transport to the simulation layer, whatever its provenance" (batch 3)',
    'recommendation', 'superseded', 'full file 13 drafts 3 to 5, the note', 'note2', '', cut(mc, 'declaration ("', '")', line=13), 'sentence', part_note='W35.1 (file-11 L219-223, Part IV / Expectation, surprise, violation)')
add('S90', mc, 's90_xexam_mimo_C point 1, second repair; refused by ruling R12 (W35.1): a general E supplies no query, and L177 says S is where expectation lives (batch 3)',
    'recommendation', 'declined', 'none', 'd2', '\\(\\operatorname{Ans}_S(\\tau(a),\\sigma(b))\\)', lit(mc, '\\(\\operatorname{Ans}_E(\\tau(a),\\sigma(b))\\)'), 'term')
add('S90', ac, 's90_xexam_atria_C point 1, second repair (on R13); refused by both R13 rulings and by the R12 ruling (batch 3)',
    'recommendation', 'declined', 'none', 'd2', '\\operatorname{Ans}_S', lit(ac, '\\operatorname{Ans}_E'), 'term')
add('S90', ac, 's90_xexam_atria_C point 1, first repair (on R13); taken in substance, in Mimo C item 4\'s words "to the simulation layer" (batch 3, Reconciliation item 3)',
    'recommendation', 'superseded', 'none', 'd2', 'Expectation and violation are defined for every transport, surprise only for a selected one', cut(ac, '*Repair:* “', '”', line=3), 'span',
    same_as=fix_rid.get(('W35.2', 'S90'), []))
add('S90', mc, 's90_xexam_mimo_C point 2 (R07, W45.1), repair to the declaration; refused by ruling R07: KEEP, it would present as new what file 11 already holds (batch 3)',
    'recommendation', 'declined', 'none', 'note2', '', cut(mc, 'declaration: "', '"', line=27), 'span', part_note='W45.1 (file-11 L77, Part I)')
add('S90', mc, 's90_xexam_mimo_C point 3 (R30, W41.1), first repair (copy Part IX\'s clause verbatim); refused by ruling R30: KEEP, it would lose N21 and Derivation 10\'s binding (batch 3)',
    'recommendation', 'declined', 'none', 'd2', 'content changes to the changes the binding specifies', cut(mc, 'verbatim ("', '")', line=51), 'span')
add('S90', mc, 's90_xexam_mimo_C point 3 (R30, W41.1), second repair (the pointer); refused by ruling R30: "in the manner of" already says "modelled on" (batch 3)',
    'recommendation', 'declined', 'none', 'd2', 'as reason use asks of an objection (Part IX)', lit(mc, 'in a manner modelled on reason use (Part IX)'), 'span')
add('S90', mc, 's90_xexam_mimo_C point 3 (R30, W41.1), second repair (the declaration); refused with it by ruling R30 (batch 3)',
    'recommendation', 'declined', 'none', 'note2', 'in the manner of reason use', lit(mc, 'in a manner modelled on reason use'), 'span', part_note='W41.1 (file-11 L401, Part X)')
add('S90', mc, 's90_xexam_mimo_C point 4 (R13, W35.2), repair to the declaration; taken in the checker\'s words, whose declaration states the scoped clause (batch 3)',
    'recommendation', 'superseded', 'none', 'note2', '', cut(mc, 'declaration: "', '" If', line=59), 'span', part_note='W35.2 (file-11 L225, Part IV / Expectation, surprise, violation)')
add('S90', mc, 's90_xexam_mimo_C point 5 (R25, W40.1), repair to the declaration; refused by both R25 rulings (restrictive, a paraphrase, and it drops "bare"); the pass takes Atria C item 5\'s declaration, which quotes NEW\'s clause (batch 3)',
    'recommendation', 'declined', 'none', 'note2', 'of which a bare denial is not an account', cut(mc, 'to "', '."', line=67), 'span', same_as=[C89], part_note='W40.1 (file-11 L337, Part VII / Explanations that remove structure)')
add('S90', B1, 'S90 batch 1, Atria B1 R39 ruling, "Loose end, not ruled": revised L51 is the one place left that calls N "declared"; passed to the orchestrator; carried forward after S90 ("Revised L51")',
    'recommendation', 'not applied', 'none', 'd2', 'as a declared normative relation', '[no wording given] L51 still calls the normative relation "declared"; no entry changes it', 'span')
add('S90', RS + 'ruling s90_xexam_mimo_B1 item 3 R48.md', 'S90 ruling R48 (W7.5), "Carried forward, not ruled": what an active route depends on (batch 2); carried forward after S90 ("What an active route depends on")',
    'recommendation', 'not applied', 'none', 'd2', '', '[no wording given] place active routes in the dependence order, and list the declared contrasts they are defined under (L369) among the declared inputs (L514)', 'sentence',
    anchor='(RC), (U1)–(U3) depend on all of the above.')
add('S90', B1, 'S90 batch 1, pending edit 1, "Optional, outside the ruling" (both R01 rulings); carried forward after S90 ("W38.1\'s line on selection")',
    'recommendation', 'not applied', 'none', 'src2', 'Here selection is blind: its history holds no represented target (Parts 0 and IV).',
    lit(B1, 'Here selection has no represented target in its history (Parts 0 and IV)') + '.', 'sentence', part_note=' / *Selection*')

# ---------- 3c. wordings the readers proposed (S93), cut from the tabulation ----------
TB = 'results/S93 Tabulation of the replies, before any ruling.md'
v4 = vers['3f7c3ab']
x03 = fence(TB, 270)
add('S93', TB, 'X03.6 (s93_xexam_mimo_F point 1), proposed wording, whole; ruling S93 X03 (W19.1): the replacement is not adopted; the FIX takes only "an active component" and the restored "up to the port translation" (challenge 2), KEEP on challenges 1 and 3',
    'recommendation', 'declined', 'none', 'd4', v4['W19.1']['NEW'], x03, 'paragraph', same_as=fix_rid.get(('W19.1', 'S93'), []))
add('S93', TB, 'X03.6 (s93_xexam_mimo_F point 1), proposed declaration; ruling S93 X03 (W19.1) writes its own declaration (challenge 2)',
    'recommendation', 'declined', 'none', 'note4', v4['W19.1']['fields']['DECLARATION'], fence(TB, 274), 'paragraph', part_note='W19.1 (file-11 L121, Part II / Kinds are edit-signatures)')
add('S93', TB, 'X05.6 (s93_xexam_mimo_G point 1), proposed wording; ruling S93 X05 (W35.2) takes the occurrence condition as "at an actually occurring pair", and does not adopt "whose fidelity fails"',
    'recommendation', 'declined', 'none', 'd4', v4['W35.2']['NEW'], fence(TB, 346), 'sentence', same_as=fix_rid.get(('W35.2', 'S93'), []))
add('S93', TB, 'X05.6 (s93_xexam_mimo_G point 1), proposed declaration; ruling S93 X05: its rephrasing of the third clause is not adopted (not the smallest change)',
    'recommendation', 'declined', 'none', 'note4', v4['W35.2']['fields']['DECLARATION'], fence(TB, 350), 'paragraph', part_note='W35.2 (file-11 L225, Part IV / Expectation, surprise, violation)')
add('S93', TB, 'X06.6 (s93_xexam_mimo_H point 1), proposed replacement, whole; ruling S93 X06 (W20.1): Mimo\'s exception ("never one of them") is ruled out as a change of claim; the FIX keeps the candidate\'s offer as deciding membership',
    'recommendation', 'declined', 'none', 'd4', v4['W20.1']['NEW'], fence(TB, 382), 'paragraph', same_as=fix_rid.get(('W20.1', 'S93'), []))
add('S93', TB, 'X06.9 (s93_xexam_mimo_H point 4), proposed declaration; ruling S93 X06: not taken, the declaration follows ruling 1',
    'recommendation', 'declined', 'none', 'note4', v4['W20.1']['fields']['DECLARATION'], fence(TB, 402), 'paragraph', part_note='W20.1 (file-11 L233, Part V)')
add('S93', TB, 'X06.7 (a) (s93_xexam_mimo_H point 2), proposed replacement of L245\'s sentence; ruling S93 X06: not taken in X06; carried forward after S93 as a candidate for a later entry ("L245 and L558 against (F1)"; the X03 ruling, finding 1)',
    'recommendation', 'not applied', 'none', 'd4', 'By (K), (F1) entails that every component of \\(E\\) has the signature of its anchor; there is no further condition about kinds to state (Derivation 1).',
    fence(TB, 390), 'sentence')
add('S93', TB, 'X06.7 (b) (s93_xexam_mimo_H point 2), L299; ruling S93 X06: "L299 is not taken"',
    'recommendation', 'declined', 'none', 'd4', 'commitments outside \\(\\Gamma\\)', lit(TB, '`components outside \\(\\Gamma\\)`').strip('`'), 'span')
add('S93', TB, 'X06.7 (b) (s93_xexam_mimo_H point 2), Derivation 1\'s Corollary at L558; ruling S93 X06: not taken in X06; carried forward after S93 as a candidate ("each active component" at L558)',
    'recommendation', 'not applied', 'none', 'd4', 'each component must anchor', 'each active component must anchor', 'span')
recs[-1]['source_ref'] += '; the reply\'s words: "should read `' + lit(TB, '`each active component`').strip('`') + '`"'
add('S93', TB, 'X06.3 (s93_xexam_atria_H point 3), optional phrase; ruling S93 X06: KEEP, the present wording stands without it (Mimo\'s "that Part VI holds fixed in E|W" is not taken either)',
    'recommendation', 'declined', 'none', 'd4', 'the named background of Part VI', lit(TB, '`what Part VI calls the named background`').strip('`'), 'span')
add('S93', TB, 'X09.1 (s93_xexam_atria_A point 1, (c2)), proposed insertion after the "fits" sentence of L315; ruling S93 X09, ruling 5: the owner\'s choice (rule 6); none of the six (c2) proposals applied (the S93 reading, section 9)',
    'recommendation', 'open for the owner', 'none', 'd4', '', fence(TB, 420), 'sentence', anchor='shows it failing a condition of (E). No list of all rivals is supposed')
add('S93', TB, 'X09.14 (s93_xexam_mimo_A, (c2)), words to add after the "fits" sentence; ruling S93 X09, ruling 5: the owner\'s choice (rule 6)',
    'recommendation', 'open for the owner', 'none', 'd4', '', fence(TB, 472), 'span', anchor='shows it failing a condition of (E). No list of all rivals is supposed')
add('S93', TB, 'X09.17 (s93_xexam_atria_B point 1 and (c2)), proposed clause for X09 or Part IX; ruling S93 X09, ruling 5, and X10: the owner\'s choice (rule 6)',
    'recommendation', 'open for the owner', 'none', 'd4', '', fence(TB, 488), 'sentence', anchor='shows it failing a condition of (E). No list of all rivals is supposed')
add('S93', TB, 'X09.18 (s93_xexam_mimo_B point 3 and (c2)), optional words to insert after "…shows it failing a condition of (E)" (L315); the owner\'s choice (rule 6)',
    'recommendation', 'open for the owner', 'none', 'd4', '', lit(TB, "A result may show this from the candidate's own content, by analysis; it need not come from a test."), 'sentence',
    anchor='shows it failing a condition of (E). No list of all rivals is supposed')
add('S93', TB, 'X09.19 (s93_xexam_atria_C, (c2)), no wording; the owner\'s choice (rule 6)',
    'recommendation', 'open for the owner', 'none', 'd4', '', '[no wording given] settle "established" in favour of the inspection reading for candidate-side facts, with receipts reserved for target-side and world-side claims', 'sentence',
    anchor='shows it failing a condition of (E). No list of all rivals is supposed')
x0920 = cut(TB, 'Words for Part IX (Receipts), which is not an item: `', '`')
add('S93', TB, 'X09.20 (s93_xexam_mimo_C point 1 and (c2)), words for Part IX (Receipts); the owner\'s choice (rule 6)',
    'recommendation', 'open for the owner', 'none', 'd4', '', x0920, 'sentence', anchor='**Receipts.** An evidence leaf is a reference to an event with an interpreted claim.')
add('S93', TB, 'X09.11 (s93_xexam_mimo_A point 3), exact additions to the declaration; ruling S93 X09: ruling 4 puts the bijection condition into the declaration\'s third sentence in the checker\'s words; ruling 3 keeps the declaration silent on "offered for the whole of p"; ruling 5 leaves the inspection sentence to the owner',
    'recommendation', 'declined', 'none', 'note4', '', fence(TB, 455), 'paragraph', part_note='W59.1 (file-11 L317-319, Part VI / Rivals)')
rv4 = [l for l in v4['W59.1']['NEW'].split('\n') if l.startswith('**Rivals.**')][0]
add('S93', TB, 'X09.13 (s93_xexam_mimo_A), replacement wording for the whole paragraph "Rivals"; ruling S93 X09, ruling 7: not adopted (the "nor" rewording not needed, ruling 1; the separate anchor-clash disjunct declined for the fix of ruling 2; the inspection clause the owner\'s, ruling 5)',
    'recommendation', 'declined', 'none', 'd4', rv4, fence(TB, 466), 'paragraph', same_as=fix_rid.get(('W59.1', 'S93'), []))
add('S93', TB, 'X09.22 = X17.7 (s93_xexam_mimo_K point 2), words offered for the dependence order; ruling S93 X17: "Mimo\'s offered words are not taken"; the FIX places the terms in the checker\'s sentence',
    'recommendation', 'declined', 'none', 'd4', '', cut(TB, 'Words offered for the order: `', '`'), 'sentence',
    anchor='(RC), (U1)–(U3) depend on all of the above.', same_as=fix_rid.get(('W7.5', 'S93'), []))
add('S93', TB, 'X17.6 (s93_xexam_mimo_K point 1), proposed wording; ruling S93 X17: KEEP on the (EK) omissions (O_ep, ProducesVia): "Mimo\'s offered words are not taken"',
    'recommendation', 'declined', 'none', 'd4', v4['W7.5']['NEW'], fence(TB, 692), 'sentence')
add('S93', TB, 'X17.6 (s93_xexam_mimo_K point 1), proposed declaration; not taken with the wording (ruling S93 X17)',
    'recommendation', 'declined', 'none', 'note4', v4['W7.5']['fields']['DECLARATION'], fence(TB, 696), 'paragraph', part_note='W7.5 (file-11 L518, Part XIV / Dependence order)')
add('S93', TB, 'X10.14 (s93_xexam_mimo_B point 5), optional phrase; ruling S93 X10: KEEP, "For that assessor" is not needed (the index is inherited through "fits")',
    'recommendation', 'declined', 'none', 'd4', '', lit(TB, '`For that assessor`').strip('`'), 'span', anchor='A candidate is **easy to vary**, in the sense used here,', new_sentence='')
add('S93', TB, 'X11.4 (s93_xexam_mimo_I point 1), proposed kind and declaration; ruling S93 X11 upholds the kind (CLAIM) and writes its own declaration',
    'recommendation', 'declined', 'none', 'note4', '', fence(TB, 604), 'paragraph', same_as=[rid_for('W61.1', '8816fcf')], part_note='the proposed X11 (file-11 L323, Part VII / Production and direction)')
add('S93', TB, 'X14.10 (s93_xexam_mimo_C point 2), optional exact wording; ruling S93 X14: KEEP, "Mimo\'s offer, which is not taken"; the clause is not false, incoherent or misleading',
    'recommendation', 'declined', 'none', 'd4', 'an account on it does not answer \\(p\\)', lit(TB, '`being an account of it is not thereby an account of \\(p\\)`').strip('`'), 'span')
add('S93', TB, 'X14.12 (s93_xexam_mimo_C point 4 (i)), the exact word offered; ruling S93 X14: KEEP, "the exclusion" is fixed by its antecedent',
    'recommendation', 'declined', 'none', 'd4', 'the exclusion ceases to be established', 'the result ceases to be established', 'span')
recs[-1]['source_ref'] += '; the reply\'s words: `' + lit(TB, 'Exact word offered for (i): `the result`').split('`')[1] + '` for "the exclusion"'
add('S93', R93 + 'ruling S93 X04 W35.1.md', 'S93 ruling X04 (W35.1): the words Mimo proposed for L582 (s93_xexam_mimo_G point 2); the first clause is entered as the companion entry W35.5; the second clause is not adopted',
    'recommendation', 'declined', 'none', 'd4', 'Surprise is defined as a violation at \\((a,b)\\notin H\\).',
    lit(R93 + 'ruling S93 X04 W35.1.md', 'Surprise is defined as a violation of a selected transport at \\((a,b)\\notin H\\); a transport that is not selected is not subject to surprise at all.'), 'sentence',
    same_as=fix_rid.get(('W35.5', 'S93'), []))
reach4 = [l for l in v4['W38.1']['NEW'].split('\n') if l.startswith('- *Reach.*')][0]
x181 = fence(TB, 725)
add('S93', TB, 'X18.1 (s93_xexam_atria_E point 1), proposed wording in place of the *Reach* sentence; ruling S93 X18, ruling 1: KEEP on the pointer "(Parts I and VI)"',
    'recommendation', 'declined', 'none', 'src4', reach4.split('. ', 1)[1] if '. ' in reach4 else reach4, x181, 'sentence', part_note=' / *Reach*')
add('S93', TB, 'X18.7 (s93_xexam_mimo_E point 3), proposed replacement for the parenthetical; ruling S93 X18, ruling 1: KEEP',
    'recommendation', 'declined', 'none', 'src4', 'the candidate against it (Parts I and VI)', 'the candidate against it (Parts I and V)', 'span', part_note=' / *Reach*')
recs[-1]['source_ref'] += '; the reply\'s words: ' + lit(TB, 'Proposed replacement for the parenthetical: `(Parts I and V)`').split(': ')[1]
add('S93', R93 + 'ruling S93 X18 W38.1.md', 'S93 ruling X18, ruling 1: "(Parts I, V and VI)" would also be true; "It is not required and is not ruled here"; carried forward after S93 ("The sources note")',
    'recommendation', 'not applied', 'none', 'src4', '(Parts I and VI)', lit(R93 + 'ruling S93 X18 W38.1.md', '(Parts I, V and VI)'), 'span', part_note=' / *Reach*')
hv4 = [l for l in v4['W38.1']['NEW'].split('\n') if l.startswith('- *Hard to vary.*')][0]
x182 = fence(TB, 733)
add('S93', TB, 'X18.2 (s93_xexam_atria_E point 2), proposed wording (the change is "is easy to vary" to "would be easy to vary"); ruling S93 X18: KEEP on the *Hard to vary* application',
    'recommendation', 'declined', 'none', 'src4', 'is easy to vary relative to the myth', 'would be easy to vary relative to the myth', 'span', part_note=' / *Hard to vary*')
recs[-1]['source_ref'] += '; the reply\'s whole sentence begins "' + (x182 or '')[:60] + '…"'
x185 = fence(TB, 747)
add('S93', TB, 'X18.5 (s93_xexam_mimo_E point 1), proposed replacement for the whole sentence; taken by ruling S93 X18, ruling 3 ("L429\'s words")',
    'recommendation', 'applied', 'full file 13 draft 5, meta block (the note of sources and departures)', 'src4',
    'A problem in his wider sense can be a recognized difficulty (Part X): a failure of a claimed obligation, or a conflict in which meeting a claimed obligation fails a protected one (Part XI), when the system represents it.',
    x185, 'sentence', same_as=[rid_for('W38.1', '8816fcf')], part_note=' / *Surprise and problems*')
if x185 and x185 not in vers['8816fcf']['W38.1']['NEW']:
    problems.append('X18.5 wording not found verbatim in W38.1 draft 5 NEW')
x524 = cut(TB, 'gives words to close it: `', '`')
add('S93', TB, 'section 4 of the tabulation, flagged, not an item: s93_xexam_mimo_K point 7, "Residual, outside this item"; carried forward after S93 ("L524 and N")',
    'recommendation', 'not applied', 'none', 'd4', '', x524, 'span', anchor='a declared input is something a claim takes as stated, which the semantics records and does not supply.', new_sentence='')
add('S93', R93 + 'ruling S93 X11 proposed.md', 'S93 ruling X11, point 6: file 12 carries the same slip at its L325; file 12 is under no round and nothing was written into authority/; carried forward after S93 ("File 12 carries the same pole-sentence slip")',
    'recommendation', 'not applied', 'none', 'f12', "but not the calculation's \\(H\\)", "but not the calculation's \\(L\\)", 'span', same_as=[rid_for('W61.1', '8816fcf')])
# findings for later entries (S93), no wording
for ref, desc, anchor in (
    ('S93 ruling X03 (W19.1), finding 1, and X06, finding 1; carried forward after S93 ("L245 and L558 against (F1)")', 'define "active component", or narrow L245 and L558 to active components; whether an anchoring condition on named-background components would then add to (F1) and (F2) needs its own check', '(F1) entails that every component of \\(E\\) has the signature of its anchor'),
    ('S93 ruling X03 (W19.1), finding 2; carried forward after S93 ("Port translations and values")', 'Part IV should say once whether a port translation may carry a map of values, which governs "footprint bijection" at L119 (twice) and L564', 'and \\(\\lambda\\) assigns each component of \\(E\\) a subnetwork of \\(D\\) with a port translation.'),
    ('S93 ruling X17 (W7.5), finding 1; carried forward after S93', 'define (K2)\'s Lic_j, Scope_j and Live_j (L390 only), so that Derivation 6 can be followed through receipts to the primitives', '\\operatorname{Lic}_j'),
    ('S93 ruling X17 (W7.5), findings 2 and 3, and X10, ruling 4; carried forward after S93 ("Receipts, (K2) and (K3)"; "L598 over-states the order")', 'place receipts, (K2) and (K3) in the dependence order ((K3) after "what is established"), or let W7.6\'s wording say that Derivation 6\'s proof follows unplaced definitions through their own text to placed ones', 'By the dependence order of Part XIV'),
    ('S93 ruling X17 (W7.5), finding 6; carried forward after S93 ("Conflict is used in two senses")', 'mark the difference between "conflict" in the defined sense of L315 and the ordinary sense of L429 and of L317\'s gloss "a conflict between ideas"', 'Two candidates **conflict**'),
    ('S93 ruling X17 (W7.5), finding 7; carried forward after S93 ("O_ep and resource contract")', 'a clause for L522 giving "resource contract" a place among the declared inputs', '**Declared inputs.**'),
    ('the S93 tabulation, section 4, flagged; "Found in draft 4" and carried forward after S93 ("V")', 'list the family \\(\\mathcal V\\) of (D) (L299, L302) among Part XIV\'s declared inputs', 'For a declared family \\(\\mathcal V\\) of organization edits'),
):
    src_file = TB if 'tabulation' in ref else (R93 + ('ruling S93 X03 W19.1.md' if 'X03' in ref else 'ruling S93 X17 W7.5.md'))
    add('S93', src_file, ref, 'recommendation', 'not applied', 'none', 'd4', '', '[no wording given] ' + desc, 'sentence', anchor=anchor)

# ---------- 3d. the change list's own findings with wording (drafters, S90 and S91) ----------
add('S90', CL, 'change list draft 5, "Findings carried forward", the item on the declared inputs (L514) and Part VI\'s restriction operation (from the settled S88 positions, "Found in settling", point 4): "The candidate clause for L514 ... It is not an entry."',
    'recommendation', 'not applied', 'none', 'f11', '', lit(CL, 'the restriction operation of Part VI (\\(E|W\\))'), 'span', anchor='**Declared inputs.**')
add('S90', CL, 'change list draft 5, "Findings carried forward": U_c and A_p in (U1)-(U2) undefined (group A, C3); "Defining them is one clause at L489 and a CLAIM, outside every item taken"',
    'recommendation', 'not applied', 'none', 'f11', '', '[no wording given] one clause at L489 defining \\(U_c\\) and \\(A_p\\) of (U1)-(U2)', 'sentence', anchor='U_c')
add('S90', CL, 'change list draft 5, "Findings carried forward", Part II uses the notation of Parts IV and V before they introduce it (W19.1, read in place): a pointer "would close it", left for X1; closed after the S90 cross-examination by W19.1\'s typing sentence',
    'recommendation', 'superseded', 'none', 'f11', '', lit(CL, '"(Parts IV and V)"').strip('"'), 'span', anchor='A kind is an equivalence class of components under this relation.',
    same_as=[rid_for('W19.1', '99e9cd0')])
add('S91', CL, 'change list draft 5, "Found in draft 4 (25 September)", first bullet: the candidate at the free sentence; after the S93 cross-examination the placement is made in W7.5 instead, and "The candidate at the free sentence is not taken"',
    'recommendation', 'superseded', 'none', 'd4', '(S), (B), (D) depend on (E).', lit(CL, '(S), (B), (D) depend on (E); rivals and the problems they pose (Part VI) on (F1), (F2), (A), (E), histories and receipts.'), 'sentence',
    same_as=[rid_for('W7.5', '8816fcf')])

# ---------- 4. the worklist ----------
WL = 'tests/Revision 2 - worklist, draft of 23 September.md'
wl = src(WL)
D = 'decision %s of the change list ("The decisions D1-D11")'
W = [
    ('W4 (L204), handling (b), a general default stated in advance; recommended (a), with (b) as the owner\'s call; ' + (D % 'D3') + ': no default inputs', 'declined',
     '', lit(WL, 'A protected condition stated without occasions covers the occasions of the use it protects.'), 'sentence', 'each as a stated condition over stated occasions'),
    ('W6 (L252), evidence and handling: an addition to L514; the entries W6.1-W6.4 + W14.1 word the normative relation otherwise', 'superseded',
     '', lit(WL, '… and, for a claim of worth, the normative relation (primitive 2), under the same rule'), 'span', '**Declared inputs.**'),
    ('W6 (L252): L27\'s second sentence narrows to worth, or the other items are named in L514 as this; the entries W6.1 and W6.4 + W14.1 word it otherwise', 'superseded',
     '', lit(WL, 'not supplied; a claim that needs one is unsettled'), 'span', '**Declared inputs.**'),
    ('W8 (L293), handling, erratum; entry W8.1 words it "at unseen changes where their population admits a differing survivor"', 'superseded',
     '', lit(WL, 'where the population admits a differing survivor'), 'span', '(D) the two provenances and the underdetermination of selected transports'),
    ('W11 (L334), handling, clarification; entry W11.1 words it otherwise', 'superseded',
     '', lit(WL, 'is not excluded by the table clause, and is an account when the other conditions hold'), 'span', 'A table that genuinely encodes'),
    ('W12 (L350), handling (a), a general rule stated in advance; entry W12.1 (after check 1) words the boundary rule otherwise', 'superseded',
     '', lit(WL, 'a boundary may be stated by the situation: where one agent acts and no outside work enters the history, the agent\'s own processes are the declared boundary'), 'sentence', '**System boundary and continuity.**'),
    ('W16 (L426), handling, the restatement option (file 12\'s framing of Derivation 4); ' + (D % 'D4') + ': from Derivation 3\'s family, W17 only', 'declined',
     '', lit(WL, 'a value fixed at an unseen pair by H alone, through \\(\\mu\\), where \\(\\mathcal T\\) admits a differing survivor'), 'span', '## 3. Selected transports are underdetermined'),
    ('W18 (L456), handling, clarification or new claim; ' + (D % 'D4') + ': from Derivation 3\'s family, W17 only', 'declined',
     '', lit(WL, 'where \\(\\mathcal T\\) is fixed by a stated construction, what \\(\\mathcal T\\) fixes at an unseen change is owed to that construction and carries its provenance; selection on H contributes only what H decides'), 'sentence', 'realized transports'),
    ('W22 (L536), handling: change "represents how it bears"; entry W22.2 (after check 1) reads "represents it as grounds for an alleged defect in a target"', 'superseded',
     'represents how it bears', lit(WL, 'represents its alleged connection'), 'span', None),
    ('W26 (L606), handling, erratum, second option; drafted as W26.1 (L327) and dropped by check 1 under decision D9 ("Dropped: 1 entry"; the drafted entry is not in any committed change list)', 'declined',
     '(I4)', '(I3)', 'term', None),
    ('W27 (L618), handling, erratum: relabel the attacks and update every pointer; ' + (D % 'D9') + ': the attack labels are kept and only wrong pointers fixed ("Checked, with no change entry")', 'declined',
     '', '[no wording given] relabel the Part XV attacks, for example "Attack 1" to "Attack 5", and update every pointer (F11 L337, L63)', 'term', '# Part XV — What defeats this class'),
    ('W29 (L646), handling, a clarification in non-circular dependence; no entry', 'not applied',
     '', lit(WL, 'a component whose value is defined as the outcome in question, observed through another carrier, is the target\'s answer at the declared grain; its measurement signature (Part II) shows it'), 'sentence', '**Non-circular dependence.**'),
    ('W31 (L679), handling, erratum: the general bound; entry W31.1 takes the erratum and "the general bound waits" ("The held items")', 'not applied',
     '', lit(WL, 'from matching initial states (\\(e_0=0\\)); with initial discrepancy \\(e_0\\), \\(e_n\\le L^n e_0+\\varepsilon\\sum_{k<n}L^k\\)'), 'span', 'e_n\\le\\varepsilon\\sum_{k<n}L^k'),
    ('W33 (L727), handling, clarification; entry W33.1 words it otherwise, and draft 4 drops the hard-to-vary measure', 'superseded',
     '', lit(WL, '(E) is fidelity; an idle commitment passes (E) and (B) reports it as non-critical; hard-to-vary (Part VI) is a separate, non-grading measure'), 'sentence', '**Hard-to-vary.**'),
    ('W34 (L746), handling, first option: restore 00:383; entry W34.1 took the second option (reach by jobs) in drafts 1-3, and draft 4 drops the definition of reach', 'not applied',
     '', lit(WL, 'Reach occurs when an unchanged organizational core participates in an account of another question through a stated anchor and additional background'), 'sentence', '**Hard-to-vary.**'),
    ('W39 (L828), "What is missing": file 00\'s 00:210 sentence; entry W39.1 restores it as "Identity of that assertion with the target\'s answer ..." (after check 1)', 'superseded',
     '', lit(WL, 'Identity of that assertion is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical truths'), 'sentence', 'moving an assertion from an input slot into a component named'),
    ('W41 (L856), "What is missing": file 00\'s paragraph; entry W41.1 restores it with edits (after check 2, "A system\'s realization ...")', 'superseded',
     '', lit(WL, 'Inexplicit representation is not absent representation'), 'sentence', 'Build'),
    ('W44 (L894), handling, optional derived notion; no entry', 'not applied',
     '', lit(WL, 'a quasi-autonomous level exists when an Account whose anchors all lie at grain \\(\\ell\\) exists'), 'sentence', None),
    ('W47 (L944), 12:273, a new derived claim carried from file 12; deferred; ' + (D % 'D5') + ': from file 12, only the missing-input sentence pattern', 'declined',
     '', lit(WL, 'A collateral effect offered as a cause fails (F1)'), 'sentence', None),
    ('W48 (L962), new claim: adopt (AC) and define ProducedBy by it (12:451); ' + (D % 'D5'), 'declined',
     '', '[no wording given] adopt (AC) and define ProducedBy by it, as "' + lit(WL, '(AC) applied to the repair as result') + '" (12:451); defer the pre-emption episode', 'sentence', 'ProducedBy'),
]
for ref, status, old, new, scope, anchor in W:
    m = re.match(r'W(\d+)', ref)
    add('S90', WL, 'worklist item ' + ref, 'recommendation', status, 'none', 'f11', old, new, scope, anchor=anchor if (old or anchor) else None)

# ---------- write ----------
write_jsonl(SP + '/step2.jsonl', recs)
json.dump({'problems': problems, 'sources': srcs_used}, open(SP + '/step2_info.json', 'w'), ensure_ascii=False, indent=1)
print(len(recs), 'records;', len(problems), 'problems')
for p in problems:
    print(' -', p)
