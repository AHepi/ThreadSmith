"""Collector A: build the ledger of edits and recommendations made or proposed before file 11.
Writes only the JSONL named in OUT; everything else is read-only."""
import re, json, difflib, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *

OUT = os.environ.get('COLLECTOR_A_OUT', ROOT + '/results/S98 Ledger of edits and recommendations/collect/collector A.jsonl')
T10 = TextIndex(F10, 'file 10')

P = {
    'S62_01': 'results/S62 Stage D and report - return/01 Fix cards.md',
    'S62_03': 'results/S62 Stage D and report - return/03 The finding at its size.md',
    'S62_04': 'results/S62 Stage D and report - return/04 Two anchoring passages.md',
    'S62_06': 'results/S62 Stage D and report - return/06 Attack points and refutation entries.md',
    'S62_07': 'results/S62 Stage D and report - return/07 Quotations.md',
    'S62_08': 'results/S62 Stage D and report - return/08 Report.md',
    'S64_02': 'results/S64 Near cases - return/02 Tighter pairs and fix cards.md',
    'S64_05': 'results/S64 Near cases - return/05 Quotations.md',
    'S65_02': 'results/S65 Near cases - return/02 Tighter pairs and fix cards.md',
    'S65_05': 'results/S65 Near cases - return/05 Quotations.md',
    'S70_02': 'results/S70 Near cases - return/02 Tighter pairs and fix cards.md',
    'S70_05': 'results/S70 Near cases - return/05 Quotations.md',
    'S70_06': 'results/S70 Near cases - return/06 Report addendum.md',
    'S72a_03': 'results/S72 Stage 1 testing - return/03 Tighter pairs and fix cards.md',
    'S72a_05': 'results/S72 Stage 1 testing - return/05 Quotations.md',
    'S72b_02': 'results/S72 Stage 2 audit - return/02 Audit of the three cards and pairs.md',
    'S72b_03': 'results/S72 Stage 2 audit - return/03 Audit of the quotations.md',
    'S72b_04': 'results/S72 Stage 2 audit - return/04 Fix card for Derivation 3.md',
    'S72b_05': 'results/S72 Stage 2 audit - return/05 Report addendum.md',
    'R55': "results/55 Stage B return - the other model's finished table, near cases and tighter pairs.md",
    'R57': "results/57 Stage C return - the other model's seven case cards, O4 placed, phrases sorted.md",
    'S75': 'results/S75 Results - the bare version test, audited: what a new version of the theory is built from.md',
    'T28': 'tests/28 Next instruction for the other model - round 4, two change-based clauses.md',
    'T30': 'tests/30 Next instruction for the other model - workflow update and re-audit.md',
    'STORY': 'records/Semantics - project story.md',
}
SHORT = {k: v.split('/')[-2] + ' / ' + v.split('/')[-1][:2] if v.startswith('results/S') else v.split('/')[-1][:40] for k, v in P.items()}
TXT = {k: read(v) for k, v in P.items()}
NTXT = {k: norm(v) for k, v in TXT.items()}
LINES = {k: v.split('\n') for k, v in TXT.items()}

records = []
by_key = {}


def new_rid():
    return 'A-%d' % (len(records) + 1)


def add(**kw):
    base = dict(rid=new_rid(), round='', source_file='', source_ref='', kind='recommendation', status='unknown',
                applied_in='none', target_text='', target_line=None, target_part='', old='', new='',
                old_sentence='', new_sentence='', scope='sentence', same_as=[])
    base.update(kw)
    records.append(base)
    return base


def occurrences(sentence, keys, exclude=()):
    ns = norm(sentence)
    out = []
    for k in keys:
        if k in exclude:
            continue
        if ns and ns in NTXT[k]:
            ln = [i for i, l in enumerate(LINES[k], 1) if ns in norm(l)]
            out.append('%s%s' % (P[k].replace('results/', ''), (' line ' + ','.join(map(str, ln[:3]))) if ln else ''))
    return out


def line_of(key, text):
    nt = norm(text)
    for i, l in enumerate(LINES[key], 1):
        if nt in norm(l):
            return i
    return None


def parse_table_rows(key, start=1, end=10 ** 9):
    rows = []
    for i, l in enumerate(LINES[key], 1):
        if start <= i <= end and l.startswith('|') and not re.match(r'\|\s*-', l):
            rows.append((i, [c.strip() for c in l.strip().strip('|').split('|')]))
    return rows


# ---------------------------------------------------------------- G1: file 10 -> file 20 (declined)
q07 = {c[0]: dict(line=i, text=c[1], version=c[2], part=c[3], use=c[4], diff=c[5])
       for i, c in parse_table_rows('S62_07') if c[0] not in ('ID',)}
# the complete "Two grades" block as printed in S62/04
blk = []
on = False
for l in LINES['S62_04']:
    if l.startswith('## Revised Part V'):
        on = True
        continue
    if on and l.startswith('## '):
        break
    if on and l.startswith('>'):
        blk.append(l[2:] if l.startswith('> ') else l[1:])
TWO_GRADES = '\n'.join(blk).strip()

pairs = [('Q01', 'Q02'), ('Q03', 'Q04'), ('Q05', 'Q06'), ('Q07', 'Q08'), ('Q09', 'Q10'), ('Q11', 'Q12'),
         ('Q13', 'Q14'), ('Q15', 'Q16'), ('Q17', 'Q18'), ('Q19', 'Q20')]
pairs += [('ATT-earlier-%s' % x, 'ATT-revised-%s' % x) for x in 'ABCDE'] + [(None, 'ATT-revised-F')]
pairs += [('XV-earlier-%d' % n, 'XV-revised-%d' % n) for n in range(1, 6)]
pairs += [('XV-earlier-6', 'XV-revised-8'), (None, 'XV-revised-6'), (None, 'XV-revised-7')]
G1_IDENTICAL = []
G1_NOTES = []
F20_COMMON = dict(round='file 20 (before log 25)', source_file=P['S62_07'], kind='edit', status='declined',
                  applied_in='file 20 (not held; set aside by decision S4)', target_text='file 10')


G1_SEEN = {}


def add_g1(**kw):
    key = (kw.get('target_line'), norm(kw.get('old', '')), norm(kw.get('new', '')))
    if key in G1_SEEN:
        G1_SEEN[key]['source_ref'] += '; the same change is quoted again in ' + kw['source_ref'].split(', earlier sentence')[0]
        return G1_SEEN[key]
    rec = add(**kw)
    G1_SEEN[key] = rec
    return rec


def extra_refs_for(text):
    return occurrences(text, ['S62_03', 'S62_04', 'S62_06', 'R57'])


for e_id, r_id in pairs:
    r = q07[r_id]
    rtext = r['text'].replace('<br><br>', ' ').replace('<br>', ' ')
    r_s = split_sents(rtext)
    if e_id is None:
        # an added entry in file 20; locate the insertion point in file 10 by the heading of the revised row
        anchor = {'ATT-revised-F': 'ATT-earlier-E', 'XV-revised-6': 'XV-earlier-5', 'XV-revised-7': 'XV-earlier-5'}[r_id]
        a_s = split_sents(q07[anchor]['text'])
        s10, ln, rr = T10.match_sentence(a_s[-1])
        refs = extra_refs_for(r_s[0])
        add_g1(**F20_COMMON, source_ref='%s (revised, row line %d; no earlier counterpart; placed after %s)%s' % (
            r_id, r['line'], anchor, ('; also ' + '; '.join(refs)) if refs else ''),
            target_line=ln, target_part=T10.parts[ln], old='', new=rtext, old_sentence='', new_sentence=rtext,
            scope='paragraph')
        continue
    e = q07[e_id]
    etext = e['text'].replace('<br><br>', ' ').replace('<br>', ' ')
    if norm(etext) == norm(rtext):
        G1_IDENTICAL.append((e_id, r_id))
        continue
    e_s = split_sents(etext)
    mapped = [T10.match_sentence(s) for s in e_s]
    near = mapped[0][1]
    mapped = [T10.match_sentence(s, near=near) if m[2] < 0.85 else m for s, m in zip(e_s, mapped)]
    sm = difflib.SequenceMatcher(None, [norm(s) for s in e_s], [norm(s) for s in r_s], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        ref0 = '%s (earlier) / %s (revised), earlier sentence %s, revised sentence %s' % (
            e_id, r_id, ('%d-%d' % (i1 + 1, i2) if i2 > i1 else 'none'), ('%d-%d' % (j1 + 1, j2) if j2 > j1 else 'none'))
        if tag == 'replace' and (i2 - i1) == (j2 - j1):
            for k in range(i2 - i1):
                es, rs = e_s[i1 + k], r_s[j1 + k]
                s10, ln, rr = mapped[i1 + k]
                o, n = token_span(es, rs)
                if o and o not in s10:
                    o, n = token_span(s10, rs)
                small = len(o) < 0.7 * len(s10) and o
                refs = extra_refs_for(rs)
                add_g1(**F20_COMMON, source_ref=ref0 + ('' if (i2 - i1) == 1 else ' (pair %d)' % (k + 1)) + (('; also ' + '; '.join(refs)) if refs else ''),
                    target_line=ln, target_part=T10.parts[ln],
                    old=o if small else s10, new=n if small else rs,
                    old_sentence=s10, new_sentence=rs, scope='span' if small else 'sentence')
                if rr < 1.0:
                    G1_NOTES.append('%s sentence %d mapped to file 10 line %d at similarity %.2f' % (e_id, i1 + k + 1, ln, rr))
        else:
            olds = [mapped[k][0] for k in range(i1, i2)]
            lns = [mapped[k][1] for k in range(i1, i2)]
            if not lns:  # insertion: anchor on the previous earlier sentence
                idx = max(i1 - 1, 0)
                lns = [mapped[idx][1]]
            new_t = ' '.join(r_s[j1:j2])
            old_t = ' '.join(olds)
            refs = extra_refs_for(new_t) if new_t else []
            add_g1(**F20_COMMON, source_ref=ref0 + (('; also ' + '; '.join(refs)) if refs else ''),
                target_line=lns[0], target_part=T10.parts[lns[0]], old=old_t, new=new_t,
                old_sentence=old_t, new_sentence=new_t, scope='sentence')
            for k in range(i1, i2):
                if mapped[k][2] < 1.0:
                    G1_NOTES.append('%s sentence %d mapped to file 10 line %d at similarity %.2f' % (e_id, k + 1, mapped[k][1], mapped[k][2]))

# the anchoring passage: file 10's "Why there is no anchoring condition" and file 20's "Two grades"
q22 = q07['Q22']['text']
ln22 = T10.find(q22[:60])
line22 = T10.lines[ln22 - 1]
add(**dict(F20_COMMON, source_file=P['S62_04']), source_ref='"Revised Part V - quoted in full" and "Earlier Part V - Why there is no anchoring condition - quoted in full"; the same pair is Q21 (revised, cells joined by <br>) and Q22 (earlier) in results/S62 Stage D and report - return/07 Quotations.md',
    target_line=ln22, target_part=T10.parts[ln22], old=line22, new=TWO_GRADES, old_sentence=line22,
    new_sentence='', scope='paragraph')

# ---------------------------------------------------------------- G2: R2 amendment sentences
q64 = {c[0]: dict(line=i, text=c[1], part=c[3]) for i, c in parse_table_rows('S64_05', 110, 141)}
BENEFIT = {k: v for k, v in q64.items() if v['text'].startswith('Expected benefit')}
order = ['S64-R2-A01'] + ['R2-A-%d' % n for n in range(1, 14)] + ['S64-R2-B0%d' % n for n in (1, 2, 3)] + \
        ['S64-R2-C0%d' % n for n in range(1, 6)] + ['R2-extra-C'] + ['S64-R2-D0%d' % n for n in (1, 2, 3)] + \
        ['S64-R2-E0%d' % n for n in (1, 2, 3)] + ['S64-R2-F0%d' % n for n in (1, 2)] + \
        ['R2-G-%d' % n for n in range(14, 31)] + ['R2-H-%d' % n for n in range(31, 42)] + \
        ['S64-R2-I0%d' % n for n in (1, 2, 3)] + ['S64-R2-J0%d' % n for n in (1, 2)]
AMEND_DEFAULT = {'A': ['V'], 'B': ['V'], 'C': ['V'], 'D': ['II'], 'E': ['IV', 'X'], 'F': ['VI'], 'G': ['XVI.5', 'III'],
                 'H': ['XI'], 'I': ['XII'], 'J': ['VI']}
AMEND_TITLE = {}
for k, v in q64.items():
    mo = re.match(r'Amendment ([A-J]) — (.*)', v['part'])
    if mo:
        AMEND_TITLE[mo.group(1)] = mo.group(2)
AMEND_TITLE.setdefault('G', 'Questions may be scoped, and merit remains conditional')
PART_RE = re.compile(r"\bParts? ((?:[0IVXL]+(?:\.\d+)?)(?:(?:, | and |, and )(?:[0IVXL]+(?:\.\d+)?))*)(?=[\s'’:,.;]|$)")


def parts_in(s):
    out = []
    for mo in PART_RE.finditer(s):
        for p in re.split(r', and |, | and ', mo.group(1)):
            if p not in out:
                out.append(p)
    return out


def part_label(plist, amend):
    names = []
    for p in plist:
        if '.' in p:
            a, b = p.split('.')
            names.append(T10.part_name(a, b))
        else:
            names.append(T10.part_name(p))
    return '; '.join(names) + ' [R2 Amendment %s — %s; Part titles from file 10]' % (amend, AMEND_TITLE.get(amend, ''))


R2_COMMON = dict(round='R2 (log 25)', kind='recommendation', target_text='file 20 with R2 applied (file 20 not held); from log S69 read as amendments to file 10')
R2_REFKEYS = ['S62_01', 'S62_07', 'S62_08', 'S64_05', 'S72a_05', 'S72b_03', 'S72b_04', 'R57', 'S65_05', 'S70_05']
r2_sent_records = []  # (record, amend, norm sentence)
prev_part = {}
for pid in order:
    if pid.startswith('S64'):
        src, text, line = 'S64_05', q64[pid]['text'], q64[pid]['line']
        amend = pid.split('-')[2][0]
    else:
        src, text, line = 'S62_07', q07[pid]['text'], q07[pid]['line']
        amend = 'C' if pid == 'R2-extra-C' else pid.split('-')[1]
    sents = split_sents(text)
    for n, s in enumerate(sents, 1):
        found = parts_in(s)
        if found:
            plist = found
            prev_part[amend] = [found[0]] if amend == 'A' else found
        else:
            plist = prev_part.get(amend, AMEND_DEFAULT[amend])
        status, applied = 'not applied', 'none'
        if pid == 'S64-R2-J01':
            if s.startswith('In Part VI,'):
                status, applied = 'applied', 'file 11, in other wording (Part VI, line 301)'
            elif 'Part XVI.3' in s or s.startswith('Preserve the admitted-class'):
                status, applied = 'applied', 'file 11, in other wording (Part XVI, Derivation 3; logs S75, S76)'
        refs = occurrences(s, R2_REFKEYS, exclude=(src,))
        ref = '%s row %s (table line %d)%s%s' % (P[src].replace('results/', ''), pid, line,
                                                ', sentence %d of %d' % (n, len(sents)) if len(sents) > 1 else '',
                                                ('; also ' + '; '.join(refs)) if refs else '')
        rec = add(**R2_COMMON, source_file=P[src], source_ref=ref, status=status, applied_in=applied,
                  target_part=part_label(plist, amend), new=s, new_sentence=s, scope='sentence')
        r2_sent_records.append((rec, amend, norm(s), plist))
        by_key[norm(s)] = rec
R2_SKIPPED = sorted(BENEFIT)

# ---------------------------------------------------------------- G3: Stage B phrase rows 33-112
benefit_norm = {k: norm(v['text']) for k, v in BENEFIT.items()}
STAGEB_SKIPPED = []
STAGEB_UNFOUND = []
for i, c in parse_table_rows('R55', 15, 94):
    row = i + 18
    amend, cell = c[0], c[1]
    phrases = re.findall(r'<u>(.*?)</u>', cell)
    hits, in_benefit = [], []
    for ph in phrases:
        nph = norm(ph)
        h = [t for t in r2_sent_records if t[1] == amend and nph in t[2]] or \
            [t for t in r2_sent_records if nph in t[2]] or \
            [t for t in r2_sent_records if nph.lower() in t[2].lower()]
        if h:
            if h[0] not in hits:
                hits.append(h[0])
        else:
            b = [k for k, v in benefit_norm.items() if nph in v or nph.lower() in v.lower()]
            if b:
                in_benefit.append((ph, b[0]))
            else:
                STAGEB_UNFOUND.append((row, ph))
    if not hits and in_benefit:
        STAGEB_SKIPPED.append((row, amend, cell, in_benefit[0][1]))
        continue
    borrowed = 'BORROWED' in c[2]
    hits.sort(key=lambda h: int(h[0]['rid'].split('-')[1]))
    first = hits[0][0] if hits else None
    add(round='Stage B (logs 41, 55)', source_file=P['R55'], kind='recommendation',
        source_ref='Stage B table row %d (file line %d), Amendment %s, phrase cell%s%s' % (
            row, i, amend, '; marked BORROWED: JUDGEMENT' if borrowed else '',
            ('; part of the cell is in R2 reason text (%s)' % ', '.join(sorted(set(b for _, b in in_benefit)))) if in_benefit else ''),
        status=first['status'] if first else 'not applied', applied_in=first['applied_in'] if first else 'none',
        target_text=R2_COMMON['target_text'], target_part=first['target_part'] if first else part_label(AMEND_DEFAULT[amend], amend),
        new=cell, new_sentence=' '.join(h[0]['new'] for h in hits), scope='span',
        same_as=[h[0]['rid'] for h in hits])

# ---------------------------------------------------------------- G4/G5: A-prime, C-prime, A-second, C-second
def clause_sentences(key, lineno, prefix_re=None):
    t = LINES[key][lineno - 1]
    if prefix_re:
        t = re.sub(prefix_re, '', t)
    return split_sents(t.strip())


CL = {}
CL['A-prime'] = (clause_sentences('T28', 8), 'T28', 8, 'round 4 (log 28)', 'Part V — Account [R2 Amendment A — scope; proposed as a replacement clause for the R2 phrase "appropriate to the intended question"]')
CL['C-prime'] = (clause_sentences('T28', 11), 'T28', 11, 'round 4 (log 28)', 'Part V — Account; Part III — Questions / The respect is the query [R2 Amendment C; proposed as a replacement clause for the R2 phrase "independently grounded dependency"]')
CL['A-second'] = (clause_sentences('T30', 21, r'^\*\*Proposed clause A-second\.\*\* '), 'T30', 21, 'round 5 and Stage C (logs 29, 30)', 'Part V — Account [R2 Amendment A — scope; appended to A]')
CL['C-second'] = (clause_sentences('T30', 23, r'^\*\*Proposed clause C-second\.\*\* '), 'T30', 23, 'round 5 and Stage C (logs 29, 30)', 'Part V — Account; Part III — Questions / The respect is the query [R2 Amendment C]')
CL_REC = {}
CL_REFKEYS = ['S62_01', 'S62_08', 'S72a_05', 'S72b_03', 'R57']
for name, (sents, key, ln, rnd, part) in CL.items():
    CL_REC[name] = []
    for n, s in enumerate(sents, 1):
        refs = occurrences(s, CL_REFKEYS)
        rec = add(round=rnd, source_file=P[key], kind='recommendation',
                  source_ref='clause %s, line %d, sentence %d of %d%s' % (name, ln, n, len(sents), ('; also ' + '; '.join(refs)) if refs else ''),
                  status='superseded', applied_in='none', target_text='file 20 with R2 applied (not held)',
                  target_part=part, new=s, new_sentence=s, scope='sentence')
        CL_REC[name].append(rec)
        by_key[norm(s)] = rec

# ---------------------------------------------------------------- G6: S62 fix-card sentences of the other model's own
S62_YOURS = {}
sec = None
for i, l in enumerate(LINES['S62_01'], 1):
    if l.startswith('## '):
        sec = l[3:].strip()
    mo = re.match(r"^> \[yours\] (.*)$", l)
    if mo:
        S62_YOURS.setdefault(sec, []).append((i, mo.group(1).strip()))
S62_PART = {
    'A with A-second': 'Part V — Account [R2 Amendment A — scope, with A-second]',
    'C with C-second: revised question distinction': 'Part III — Questions / The respect is the query; Part V — Account [R2 Amendment C, local replacement for C-second]',
    'Amendment G': 'Part X — Understanding, construction, and origin [R2 Amendment G — merit condition]',
    'Amendment H': 'Part XI — Progress, knowledge, and the normative [R2 Amendment H — ProducedBy and Repair]',
}
S62_REC = {}
for secname, items in S62_YOURS.items():
    S62_REC[secname] = []
    for n, (ln, s) in enumerate(items, 1):
        refs = occurrences(s, ['S62_08', 'S72a_05', 'S72b_03'])
        rec = add(round='S62 (log S63)', source_file=P['S62_01'], kind='recommendation',
                  source_ref='fix card "%s", boxed clause, sentence tagged [yours], line %d%s' % (secname, ln, ('; also ' + '; '.join(refs)) if refs else ''),
                  status='not applied', applied_in='none', target_text='file 20 with R2 applied (not held)',
                  target_part=S62_PART[secname], new=s, new_sentence=s, scope='sentence')
        S62_REC[secname].append(rec)
        by_key[norm(s)] = rec

# ---------------------------------------------------------------- G7: H64, I64 (S64) and H65 (S65)
def tagged_in_section(key, head_prefix):
    out, on = [], False
    for i, l in enumerate(LINES[key], 1):
        if l.startswith('## '):
            on = l[3:].startswith(head_prefix)
            continue
        mo = re.match(r"^> \[yours\] (.*)$", l)
        if on and mo:
            out.append((i, mo.group(1).strip()))
    return out


CLAUSE64 = {'H64': ('S64_02', 'H64', 'S64 (log S65)', 'Part XI — Progress, knowledge, and the normative [R2 Amendment H, Stage B row 90; attribution]'),
            'I64': ('S64_02', 'I64', 'S64 (log S65)', 'Part XIII — Recursion and universality [R2 Amendment I, Stage B row 96; assisted inquiry and credit]'),
            'H65': ('S65_02', 'H65', 'S65 (log S70)', 'Part XI — Progress, knowledge, and the normative / Repair [R2 Amendment H, Stage B rows 82-83; protected obligations]')}
C64_REC = {}
for name, (key, head, rnd, part) in CLAUSE64.items():
    C64_REC[name] = []
    items = tagged_in_section(key, head)
    for n, (ln, s) in enumerate(items, 1):
        refs = occurrences(s, ['S65_02', 'S70_02', 'S72a_03', 'S72a_05', 'S72b_02', 'S72b_03'], exclude=(key,))
        rec = add(round=rnd, source_file=P[key], kind='recommendation',
                  source_ref='fix card %s, boxed clause, sentence %d of %d, line %d; retained verbatim in later rounds: %s' % (name, n, len(items), ln, '; '.join(refs) if refs else 'none found'),
                  status='superseded', applied_in='none', target_text='file 10, with R2 and the S62 clauses read in',
                  target_part=part, new=s, new_sentence=s, scope='sentence')
        C64_REC[name].append(rec)
        by_key[norm(s)] = rec

# ---------------------------------------------------------------- G8: S70 heading (11), the clarifying-draft list
s70_start = next(i for i, l in enumerate(LINES['S70_06'], 1) if l.startswith('## (11)'))
S70_PART = [
    'Part V — Account (question fidelity, fixed query)',
    'Part II — Organizations and their changes; Part III — Questions / The respect is the query; Part V — Account',
    'Part 0 — Read this first / Grievances, anticipated; Part III — Questions; Part XI — Progress, knowledge, and the normative',
    'Part V — Account / What (E) excludes',
    'Part IV — Layers, transports, and provenance / Three provenances; Part X — Understanding, construction, and origin',
    'Part X — Understanding, construction, and origin',
    'Part IV — Layers, transports, and provenance / Three provenances; Part IX — Criticism, use, and standing',
    'Part VIII — Transport results',
    'Part VI — Work, support, and interference',
    'Part VI — Work, support, and interference',
    'Part III — Questions',
    'Part III — Questions',
    'Part XI — Progress, knowledge, and the normative',
    'Part IX — Criticism, use, and standing; Part XI — Progress, knowledge, and the normative',
    'Part XI — Progress, knowledge, and the normative / Repair',
    'Part X — Understanding, construction, and origin; Part XII — The physical module; Part XIV — The class collected',
    'Part 0 — Read this first; Part III — Questions; Part X — Understanding, construction, and origin',
    'Part VI — Work, support, and interference',
    'Part XVI — Derivations / 3. Selected transports are underdetermined on unseen changes',
    'Part XII — The physical module; Part XIV — The class collected; Part XVI — Derivations / 6. There are two primitives',
    'Part XIV — The class collected; Part XVI — Derivations / 6. There are two primitives',
]
S70_REC = []
rows70 = [r for r in parse_table_rows('S70_06', s70_start) if r[1][0] in ('WORDING', 'CLAIM')]
for n, (ln, c) in enumerate(rows70):
    rec = add(round='S70 (log S71)', source_file=P['S70_06'], kind='recommendation',
              source_ref='heading (11), table row %d of %d (line %d), mark %s' % (n + 1, len(rows70), ln, c[0]),
              status='superseded', applied_in='none', target_text='file 10',
              target_part=S70_PART[n] + ' [part named from the cases, rows and clauses the row cites]', new=c[1], new_sentence=c[1], scope='sentence')
    S70_REC.append(rec)
    by_key[norm(c[1])] = rec

# ---------------------------------------------------------------- G9: S72 Stage 2 admitted list (D3-1, D3-2) and W01-W12
s72_start = next(i for i, l in enumerate(LINES['S72b_05'], 1) if l.startswith('## (11)'))
s72_end = next(i for i, l in enumerate(LINES['S72b_05'], 1) if l.startswith('### Held back'))
W_REC = {}
claim_line = T10.find('**Claim.** Let \\(t\\) be selected on a finite history')
cons_sent = [s for s, i in T10.sents if s.startswith('**Consequence.** A correspondence produced by selection')][0]
cons_line = T10.find(cons_sent)
ROMAN_LIST = re.compile(r'Parts? ([0IVXL]+(?:[–-][0IVXL]+)?(?:(?:, | and )[0IVXL]+(?:[–-][0IVXL]+)?)*)')


def expand_parts(txt):
    mo = ROMAN_LIST.search(txt)
    if not mo:
        return txt
    out = []
    for p in re.split(r', | and ', mo.group(1)):
        if re.search(r'[–-]', p):
            a, b = re.split(r'[–-]', p)
            romans = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI']
            for r in romans[romans.index(a):romans.index(b) + 1]:
                out.append(T10.part_name(r))
        else:
            out.append(T10.part_name(p))
    return '; '.join(out)


for ln, c in parse_table_rows('S72b_05', s72_start, s72_end):
    mo = re.match(r'(D3-\d|W\d\d) — (CLAIM|WORDING); yours', c[0])
    if not mo:
        continue
    wid, mark = mo.group(1), mo.group(2)
    if wid.startswith('D3'):
        box_ln = line_of('S72b_04', c[1])
        if wid == 'D3-1':
            old = T10.lines[claim_line - 1]
            rec = add(round='S72 (log S75)', source_file=P['S72b_05'], kind='recommendation',
                      source_ref='heading (11), admitted draft list, %s (line %d); boxed in %s line %s; order in heading (12)' % (wid, ln, P['S72b_04'].replace('results/', ''), box_ln),
                      status='applied', applied_in='file 11, in other wording (Part XVI, Derivation 3; logs S75, S76)', target_text='file 10',
                      target_line=claim_line, target_part=T10.parts[claim_line], old=old, new=c[1], old_sentence=old,
                      new_sentence=c[1], scope='sentence')
        else:
            rec = add(round='S72 (log S75)', source_file=P['S72b_05'], kind='recommendation',
                      source_ref='heading (11), admitted draft list, %s (line %d); boxed in %s line %s; heading (12) places it after the claim and in place of the consequence' % (wid, ln, P['S72b_04'].replace('results/', ''), box_ln),
                      status='applied', applied_in='file 11, in other wording (Part XVI, Derivation 3; logs S75, S76)', target_text='file 10',
                      target_line=cons_line, target_part=T10.parts[cons_line], old=cons_sent, new=c[1], old_sentence=cons_sent,
                      new_sentence=c[1], scope='sentence')
    else:
        parts = expand_parts(c[2])
        rec = add(round='S72 (log S75)', source_file=P['S72b_05'], kind='recommendation',
                  source_ref='heading (11), "Explicit already; every case agreed", %s (line %d), mark WORDING' % (wid, ln),
                  status='applied', applied_in='file 11, in other wording (log S76; log S78 point 6 on W08)', target_text='file 10',
                  target_part=parts + ' [Parts as the row names them]', new=c[1], new_sentence=c[1], scope='sentence')
    W_REC[wid] = rec
    by_key[norm(c[1])] = rec

# ---------------------------------------------------------------- G10: S75 proposed change to file 10
S75L = LINES['S75']
pt4 = next(l for l in S75L if l.startswith('4. **What the claim change is.**'))
restated = re.search(r'one claim in two sentences\): (.*)$', pt4).group(1).strip()
S75_COMMON = dict(round='S75', source_file=P['S75'], kind='recommendation', status='applied',
                  applied_in='file 11, in other wording (log S76: the four-sentence patch made first was not kept; the rewrite carries the change)',
                  target_text='file 10')
old_claim = T10.lines[claim_line - 1]
s75_1 = add(**S75_COMMON, source_ref='"The determination", point 4 (line %d); "Proposed change to file 10", bullet 1' % (S75L.index(pt4) + 1),
            target_line=claim_line, target_part=T10.parts[claim_line], old=old_claim, new=restated,
            old_sentence=old_claim, new_sentence=restated, scope='sentence',
            same_as=[W_REC['D3-1']['rid'], W_REC['D3-2']['rid']])
b1 = next(l for l in S75L if l.startswith('- Part XVI, Derivation 3:'))
o_span = 'unconstrained where it was not'
n_span = 'unconstrained wherever the population admits an alternative there'
assert o_span in b1 and n_span in b1
s75_2 = add(**S75_COMMON, source_ref='"Proposed change to file 10", bullet 1, the consequence (line %d)' % (S75L.index(b1) + 1),
            target_line=cons_line, target_part=T10.parts[cons_line], old=o_span, new=n_span,
            old_sentence=cons_sent, new_sentence=cons_sent.replace(o_span, n_span), scope='span')
b2 = next(l for l in S75L if l.startswith('- Part 0, grievance 3:'))
g3_sent = [s for s, i in T10.sents if '*always* underdetermined' in s][0]
g3_line = T10.find(g3_sent)
s75_3 = add(**S75_COMMON, source_ref='"Proposed change to file 10", bullet 2 (line %d)' % (S75L.index(b2) + 1),
            target_line=g3_line, target_part=T10.parts[g3_line], old='*always* underdetermined',
            new='underdetermined wherever its population admits an alternative at the unseen change',
            old_sentence=g3_sent, new_sentence='', scope='span')
b3 = next(l for l in S75L if l.startswith('- Part 0, attack (D):'))
attD = [s for s, i in T10.sents if s.startswith('**(D) Genesis.**')][0]
attD_line = T10.find(attD)
s75_4 = add(**S75_COMMON, source_ref='"Proposed change to file 10", bullet 3 (line %d)' % (S75L.index(b3) + 1),
            target_line=attD_line, target_part=T10.parts[attD_line],
            old='a selected transport can be non-underdetermined on unseen changes (against Derivation 3)',
            new='[no wording given] the first limb reads against the qualified Derivation 3',
            old_sentence=attD, new_sentence='', scope='span')
b4 = next(l for l in S75L if l.startswith('- Part XV, "A non-fallible selected transport"'))
xv_new = re.search(r': (a survivor determined .*)$', b4).group(1).strip()
xv_sents = [s for s, i in T10.sents if i == T10.find('**A non-fallible selected transport.**')]
xv_line = T10.find('**A non-fallible selected transport.**')
xv_old = ' '.join(xv_sents)
s75_5 = add(**S75_COMMON, source_ref='"Proposed change to file 10", bullet 4 (line %d); wording as the bullet gives it, the added words in italics' % (S75L.index(b4) + 1),
            target_line=xv_line, target_part=T10.parts[xv_line], old=xv_old, new=xv_new,
            old_sentence=xv_old, new_sentence='', scope='sentence')

# ---------------------------------------------------------------- G11: the four-sentence patch of log S76 (not kept)
story = LINES['STORY']
s76 = next(i for i, l in enumerate(story, 1) if l.startswith('S76. '))
add(round='S76', source_file=P['STORY'], kind='edit', status='superseded',
    source_ref='log S76 (line %d): "The four-sentence patch made first is superseded by the rewrite and is not kept"' % s76,
    applied_in='none (the patch was not kept; file 11 carries the change in other wording)', target_text='file 10',
    target_part='Part XVI — Derivations / 3. Selected transports are underdetermined on unseen changes; Part 0 — Read this first / Grievances, anticipated; Part 0 — Read this first / Where to attack this; Part XV — What defeats this class',
    new='[no wording given] a four-sentence patch to file 10 made from the S75 proposal (one claim and the three sentences that restate it)',
    scope='paragraph', same_as=[s75_1['rid'], s75_3['rid'], s75_4['rid'], s75_5['rid']])

# ---------------------------------------------------------------- lineage links named by the sources
def link(recs, targets):
    for r in recs:
        for t in targets:
            if t['rid'] not in r['same_as'] and t['rid'] != r['rid']:
                r['same_as'].append(t['rid'])


def best_link(src_recs, dst_recs, thr=0.45):
    for r in src_recs:
        best = max(dst_recs, key=lambda d: difflib.SequenceMatcher(None, norm(r['new']), norm(d['new'])).ratio())
        if difflib.SequenceMatcher(None, norm(r['new']), norm(best['new'])).ratio() >= thr:
            link([r], [best])


best_link(CL_REC['A-prime'], CL_REC['A-second'])
best_link(CL_REC['C-prime'], CL_REC['C-second'])
best_link(CL_REC['C-second'], S62_REC['C with C-second: revised question distinction'])
# S70 rows that name A-second, C-second, S62 H, H64, H65, I64 as their source; S72 W rows that name A-S62A or T-C03
S70 = {n + 1: r for n, r in enumerate(S70_REC)}
link(CL_REC['A-second'], [S70[3], W_REC['W01']])
link(S62_REC['A with A-second'], [S70[3], W_REC['W01']])
link(CL_REC['C-second'], [S70[2], S70[4]])
link(S62_REC['C with C-second: revised question distinction'], [S70[2], S70[4], W_REC['W02']])
link(S62_REC['Amendment H'], [S70[13]])
link(C64_REC['H64'], [S70[14], W_REC['W07']])
link(C64_REC['I64'], [S70[17], W_REC['W12']])
link(C64_REC['H65'], [S70[15], W_REC['W08']])
# S70 rows and S72 W rows on the same cases
for n, w in {2: 'W02', 3: 'W01', 5: 'W03', 6: 'W06', 9: 'W10', 10: 'W09', 14: 'W07', 15: 'W08', 16: 'W11', 17: 'W12'}.items():
    link([S70[n]], [W_REC[w]])
link([S70[19]], [W_REC['D3-1'], W_REC['D3-2']])
for r in r2_sent_records:
    if r[0]['status'] == 'applied' and 'Derivation 3' in r[0]['applied_in']:
        link([r[0]], [W_REC['D3-1'], W_REC['D3-2'], s75_1])
        link([S70[19]], [r[0]])
# statuses for the superseded clause families
for r in S62_REC['A with A-second'] + S62_REC['C with C-second: revised question distinction'] + S62_REC['Amendment H']:
    r['status'] = 'superseded'

# make every same_as link two-way
_by_rid = {r['rid']: r for r in records}
for r in records:
    for t in list(r['same_as']):
        o = _by_rid[t]
        if r['rid'] not in o['same_as']:
            o['same_as'].append(r['rid'])
for r in records:
    r['same_as'].sort(key=lambda x: int(x.split('-')[1]))

# ---------------------------------------------------------------- write
with open(OUT, 'w', encoding='utf-8') as fh:
    for r in records:
        fh.write(json.dumps(r, ensure_ascii=False) + '\n')

json.dump(dict(G1_IDENTICAL=G1_IDENTICAL, G1_NOTES=G1_NOTES, R2_SKIPPED=R2_SKIPPED,
               STAGEB_SKIPPED=[(a, b, c, d) for a, b, c, d in STAGEB_SKIPPED], STAGEB_UNFOUND=STAGEB_UNFOUND),
          open(os.environ.get('COLLECTOR_A_NOTES', os.devnull), 'w'), ensure_ascii=False, indent=1)
print('records', len(records))
