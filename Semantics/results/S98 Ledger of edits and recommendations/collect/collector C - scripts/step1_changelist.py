"""Step 1 and 2: every change-list entry (draft 5) and every earlier wording of it (drafts 1-4),
with the S90 and S93 brief ids that carried each wording. Writes step1.jsonl in the scratchpad."""
import sys, json, re
sys.path.insert(0, __import__('os').path.dirname(__file__))
from lib_c import *

f11 = Text(F11, 'file 11')
texts = [(lab, Text(p, lab)) for lab, p in TEXTS]
T = dict(texts)
vers = {}
for c, lab, dr, rnd in CL_VERSIONS:
    vers[c] = parse_changelist(open(SP + '/cl/' + c + '.md', encoding='utf-8').read())
final = vers['8816fcf']
byid = {c: {e['id']: e for e in vers[c]} for c in vers}
TARGET = 'file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923)'

# ---- briefs ----
BRIEFS = [
    ('S90 brief (first 48 changes)', 'tests/S90 Cross-examination - revision 2 draft, the first 48 changes.md', '12e73da'),
] + [(p.split(' - ')[1].split(',')[0].replace('part ', 'S90 part '), 'tests/' + p, '587eebf') for p in sorted(os.listdir(ROOT + '/tests')) if p.startswith('S90 Cross-examination - part ')] \
  + [('S93 ' + p.split(' - ')[2].split(',')[0], 'tests/' + p, '3f7c3ab') for p in sorted(os.listdir(ROOT + '/tests')) if p.startswith('S93 Cross-examination - draft 4 - part ')]
brief_items = []
for lab, path, c in BRIEFS:
    for it in parse_brief(read(path)):
        it['brief'] = lab
        it['brief_path'] = path
        it['version'] = c
        brief_items.append(it)

problems = []


def locate_brief(it):
    """Find the entry whose OLD/NEW in some change-list version equals the brief's."""
    hits = []
    for c, lab, dr, rnd in CL_VERSIONS:
        for e in vers[c]:
            if e.get('OLD') == it.get('old') and e.get('NEW') == it.get('new'):
                hits.append((c, e['id']))
    return hits


MANUAL = {'X09': 'W59.1', 'X10': 'W59.1', 'X18': 'W38.1'}
brief_map = {}  # (entry id, OLD, NEW) -> list of brief labels
for it in brief_items:
    hits = locate_brief(it)
    ids = sorted(set(h[1] for h in hits))
    it['entry'] = ids
    if not hits and it['id'] in MANUAL:
        # the brief gives the new wording by reference to its excerpt (X09, X10) or cuts the anchor (X18);
        # the wording it refers to is the entry's NEW in the version the brief was built on (checked below)
        eid = MANUAL[it['id']]
        e = byid[it['version']][eid]
        if (it.get('old') or '') in e['OLD'] and (it.get('new') or '') in e['NEW']:
            it['entry'] = [eid]
            brief_map.setdefault((eid, e.get('OLD'), e.get('NEW')), []).append('%s %s' % (it['brief'], it['id']))
            problems.append('brief item %s %s: mapped to %s by hand (the brief refers to its excerpt or cuts the anchor; its text is contained in the entry)' % (it['brief'], it['id'], eid))
            continue
    if not hits:
        # try NEW contained in an entry's NEW (meta blocks may be trimmed)
        for e in byid[it['version']].values():
            if e.get('NEW') and it.get('new') and (it['new'] in e['NEW'] or e['NEW'] in it['new']) and it.get('old') and e.get('OLD') and (it['old'] in e['OLD'] or e['OLD'] in it['old']):
                ids.append(e['id'])
        it['entry'] = ids
        if not ids:
            problems.append('brief item %s %s: no change-list entry has the same OLD and NEW' % (it['brief'], it['id']))
        else:
            problems.append('brief item %s %s: matched %s only by containment' % (it['brief'], it['id'], ids))
    for eid in it['entry']:
        e = byid[it['version']].get(eid) or byid['8816fcf'].get(eid)
        key = (eid, it.get('old'), it.get('new'))
        brief_map.setdefault(key, []).append('%s %s' % (it['brief'], it['id']))
    if hits and it['version'] not in [h[0] for h in hits]:
        problems.append('brief item %s %s: wording matches change-list versions %s, not the version the brief was built on (%s)' % (it['brief'], it['id'], sorted(set(h[0] for h in hits)), it['version']))


def carried(new):
    labs = [lab for lab, t in texts if new and t.count(new) >= 1]
    return labs


def fmt_in(labs):
    return '; '.join(labs) if labs else 'none of the theory texts (a meta block of the full draft)'


def sentence_fields(old, new):
    r = f11.sentences_around(old)
    if not r:
        return None, '', '', 'span'
    la, lb, sent, sa, sb = r
    new_sent = sent.replace(old, new, 1)
    # scope
    a = 0
    while a < min(len(old), len(new)) and old[a] == new[a]:
        a += 1
    b = 0
    while b < min(len(old), len(new)) - a and old[-1 - b] == new[-1 - b]:
        b += 1
    dold, dnew = old[a:len(old) - b], new[a:len(new) - b]
    if '\n' in dold or '\n' in dnew:
        scope = 'paragraph'
    elif sent.strip() == old.strip() or re.fullmatch(r'[\s\S]*[.:;?!∎]\s*', dold + ' ') and (dnew.strip() == '' or dold.strip() == ''):
        scope = 'sentence'
    else:
        scope = 'span'
    return la, sent, new_sent, scope


def part_at(line):
    p = f11.part.get(line, '')
    if p.startswith('Front matter'):
        return 'Front matter (before Part 0)'
    return p


recs = []


def base_record(e, old, new, c_label):
    la, sent, nsent, scope = sentence_fields(old, new) if old else (None, '', '', 'sentence')
    line = la
    if line is None:
        m = re.match(r'(\d+)', e['fields'].get('FILE-11 LINE', ''))
        line = int(m.group(1)) if m else None
    return line, sent, nsent, scope


rid = [0]


def nrid():
    rid[0] += 1
    return 'C-%d' % rid[0]


final_rids = {}
for e in final:
    eid = e['id']
    st = e['fields'].get('STATUS')
    fl = e['fields'].get('FILE-11 LINE', '')
    kind_w = e['fields'].get('KIND', '')
    # first version with the final wording
    first = None
    for c, lab, dr, rnd in CL_VERSIONS:
        x = byid[c].get(eid)
        if x and x.get('OLD') == e.get('OLD') and x.get('NEW') == e.get('NEW') and x.get('LOCATOR') == e.get('LOCATOR'):
            first = (c, lab, dr, rnd)
            break
    if st == 'record-only':
        old = e.get('LOCATOR')
        row = re.search(r'row (L2-\d+)', e['heading'])
        new = '[no wording given] record-only entry: this file-11 text is declared in layer 2 of the revision record (row %s) as a change of claim file 11 made against file 10; the theory text is unchanged' % (row.group(1) if row else '?')
        line, sent, nsent, scope = base_record(e, old, old, None)
        nsent = ''
        applied_in = 'revision record of file 13, layer 2 (no change to the theory text)'
        status = 'applied'
    else:
        old, new = e.get('OLD'), e.get('NEW')
        line, sent, nsent, scope = base_record(e, old, new, None)
        labs = carried(new)
        applied_in = fmt_in(labs)
        status = 'applied'
        if kind_w == 'META':
            applied_in = 'full file 13 drafts 1 to 5, meta block (cut from every theory text)'
            if eid == 'W38.1':
                scope = 'whole text'
    briefs = []
    for (k, o, n), bl in brief_map.items():
        if k == eid and o == e.get('OLD') and n == e.get('NEW'):
            briefs += bl
    sref = 'change list draft 5, entry %s ("%s"), STATUS %s, KIND %s, FILE-11 LINE %s; wording first in %s' % (
        eid, e['title'], st, kind_w, fl, first[1] if first else '?')
    if briefs:
        sref += '; carried as ' + ', '.join(briefs)
    r = {'rid': nrid(), 'round': first[3] if first else 'S90', 'source_file': CL, 'source_ref': sref,
         'kind': 'edit', 'status': status, 'applied_in': applied_in, 'target_text': TARGET,
         'target_line': line, 'target_part': part_at(line) if line else '',
         'old': old or '', 'new': new or '', 'old_sentence': sent, 'new_sentence': nsent,
         'scope': scope, 'same_as': []}
    if fl and line and not fl.startswith(str(line)):
        problems.append('%s: FILE-11 LINE %s, OLD begins at file-11 line %s' % (eid, fl, line))
    recs.append(r)
    final_rids[eid] = r['rid']

# ---- step 2: superseded wordings ----
for e in final:
    eid = e['id']
    runs = []  # list of [ (OLD,NEW), [versions] ]
    for c, lab, dr, rnd in CL_VERSIONS:
        x = byid[c].get(eid)
        if not x or x['fields'].get('STATUS') != 'applied':
            continue
        key = (x.get('OLD'), x.get('NEW'))
        if runs and runs[-1][0] == key:
            runs[-1][1].append((c, lab, dr, rnd))
        else:
            runs.append([key, [(c, lab, dr, rnd)]])
    for key, vs in runs:
        if key == (e.get('OLD'), e.get('NEW')):
            continue
        old, new = key
        line, sent, nsent, scope = base_record(e, old, new, None)
        drafts = [v[2] for v in vs]
        # verify carried by those drafts
        if e['fields'].get('KIND') != 'META':
            for d in drafts:
                if T[d].count(new) < 1:
                    problems.append('%s: superseded NEW of %s not found verbatim in %s' % (eid, vs[0][1], d))
            carried_other = [lab for lab, t in texts if t.count(new) >= 1 and lab not in drafts]
            if carried_other:
                problems.append('%s: superseded NEW also found in %s' % (eid, carried_other))
            applied_in = '; '.join(drafts)
        else:
            applied_in = '; '.join('full ' + d + ', meta block' for d in drafts)
            scope = 'whole text'
        briefs = []
        for (k, o, n), bl in brief_map.items():
            if k == eid and o == old and n == new:
                briefs += bl
        sref = 'change list entry %s, OLD/NEW as in %s (git %s); replaced in %s; the draft-5 wording is %s' % (
            eid, ' and '.join(v[1].split(' (')[0] for v in vs), ', '.join(v[0] for v in vs),
            'change list draft %d' % (CL_VERSIONS.index(vs[-1]) + 2), final_rids[eid])
        if briefs:
            sref += '; carried as ' + ', '.join(briefs)
        recs.append({'rid': nrid(), 'round': vs[0][3], 'source_file': CL, 'source_ref': sref,
                     'kind': 'edit', 'status': 'superseded', 'applied_in': applied_in, 'target_text': TARGET,
                     'target_line': line, 'target_part': part_at(line) if line else '',
                     'old': old or '', 'new': new or '', 'old_sentence': sent, 'new_sentence': nsent,
                     'scope': scope, 'same_as': []})

# ---- held placeholders of change list draft 1 ----
for x in vers['12e73da']:
    if x['fields'].get('STATUS') == 'held':
        fl = x['fields'].get('FILE-11 LINE', '')
        line = int(re.match(r'(\d+)', fl).group(1))
        drafted = [e['id'] for e in vers['587eebf'] if e['id'].startswith(x['id'].split(' ')[0] + '.') or ' + ' in e['id'] and x['id'].split(' ')[0] + '.' in e['id']]
        recs.append({'rid': nrid(), 'round': 'S90', 'source_file': CL,
                     'source_ref': 'change list draft 1 (git 12e73da), held placeholder "%s", FILE-11 LINE %s; replaced in change list draft 2 (587eebf) by the drafted entries %s' % (x['heading'], fl, ', '.join(final_rids.get(d, d) + ' (' + d + ')' for d in drafted)),
                     'kind': 'recommendation', 'status': 'superseded', 'applied_in': 'none',
                     'target_text': TARGET, 'target_line': line, 'target_part': part_at(line),
                     'old': '', 'new': '[no wording given] held under D2: nothing drafted; the placeholder names the S88 candidate wordings then in view for file-11 lines ' + fl,
                     'old_sentence': '', 'new_sentence': '', 'scope': 'paragraph', 'same_as': []})

# ---- declaration-only edits made by the S90 rulings (the note of file 13, not the theory text) ----
v2, v3 = byid['587eebf'], byid['99e9cd0']
for eid, ref in (('W40.1', 'S90 ruling R25 (Atria C item 5, Mimo C point 5; batch 3): FIX, declaration only'),
                 ('W6.3', 'S90 rulings R39 (Atria B1 point 1, batch 1; Mimo B1 item 2, batch 2): KIND WORDING -> CLAIM, declaration added')):
    d2, d3 = v2[eid]['fields']['DECLARATION'], v3[eid]['fields']['DECLARATION']
    line = int(re.match(r'(\d+)', v3[eid]['fields']['FILE-11 LINE']).group(1))
    recs.append({'rid': nrid(), 'round': 'S90', 'source_file': CL,
                 'source_ref': 'change list entry %s, DECLARATION as in change list draft 2 (587eebf) and draft 3 (99e9cd0); %s; the entry\'s theory wording is %s' % (eid, ref, final_rids[eid]),
                 'kind': 'edit', 'status': 'applied', 'applied_in': 'full file 13 drafts 3 to 5, the note (its list of changes of claim)',
                 'target_text': 'the note of file 13, its list of changes of claim (full file 13 draft 2)', 'target_line': None,
                 'target_part': 'Front matter (before Part 0) / the note of file 13; the declaration of the change at file-11 line %d (%s)' % (line, part_at(line)),
                 'old': '' if d2.startswith('None') else d2, 'new': d3, 'old_sentence': '' if d2.startswith('None') else d2, 'new_sentence': d3,
                 'scope': 'sentence', 'same_as': []})

json.dump({'problems': problems, 'brief_items': [(i['brief'], i['id'], i['entry']) for i in brief_items],
           'final_rids': final_rids}, open(SP + '/step1_info.json', 'w'), ensure_ascii=False, indent=1)
write_jsonl(SP + '/step1.jsonl', recs)
print(len(recs), 'records;', len(problems), 'problems')
for p in problems:
    print(' -', p)
