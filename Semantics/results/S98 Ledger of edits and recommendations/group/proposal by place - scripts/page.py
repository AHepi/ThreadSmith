"""Writes group/proposal by place.md from assignment.jsonl, sections.json and
measures.json (made by place.py v2). Run after place.py:
    PYTHONDONTWRITEBYTECODE=1 python3 place.py v2 > /dev/null && PYTHONDONTWRITEBYTECODE=1 python3 page.py
"""
import json, os, re, hashlib
from collections import Counter, defaultdict, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
GROUP = os.path.dirname(HERE)
A = [json.loads(l) for l in open(os.path.join(HERE, 'assignment.jsonl'), encoding='utf-8')]
S = json.load(open(os.path.join(HERE, 'sections.json'), encoding='utf-8'))
M = json.load(open(os.path.join(HERE, 'measures.json'), encoding='utf-8'))
recs = {json.loads(l)['rid']: json.loads(l) for l in open(os.path.join(GROUP, 'anchored.jsonl'), encoding='utf-8')}
TERMS = json.load(open(os.path.join(GROUP, 'anchor - scripts', 'step3 side data.json'), encoding='utf-8'))['terms']
def md5(p):
    return hashlib.md5(open(p, 'rb').read()).hexdigest()

units = [json.loads(l) for l in open(os.path.join(GROUP, 'sentence index of the latest text.jsonl'), encoding='utf-8')]
sec_part = {u['id']: u['part'] for u in units}
uorder = {u['id']: i for i, u in enumerate(units)}
PART_NAME = OrderedDict()
for u in units:
    k = 'FM' if u['part'].startswith('Front') else re.match(r'Part ([0IVX]+) ', u['part']).group(1)
    PART_NAME.setdefault(k, u['part'])
PORDER = list(PART_NAME) + ['ALL']

# ---- groups in text order, with ids
sec2grp = {tuple(x['section']): tuple(x['group']) for x in S}
grp_secs = defaultdict(list)
for x in S:
    grp_secs[tuple(x['group'])].append(x)
used = Counter(tuple(a['group']) for a in A)
gorder = []
for x in S:
    g = tuple(x['group'])
    if g in used and g not in gorder:
        gorder.append(g)
for pk in PORDER:
    r = (pk, 'Not in the latest text')
    if r in used:
        # the residue goes after the Part's sections
        idx = max([i for i, g in enumerate(gorder) if g[0] == pk], default=len(gorder) - 1)
        gorder.insert(idx + 1, r)
if ('ALL', 'Vocabulary across the text') in used:
    gorder.append(('ALL', 'Vocabulary across the text'))
assert set(gorder) == set(used), set(used) - set(gorder)

gid = {}
n_in_part = Counter()
for g in gorder:
    pk = g[0]
    if pk in ('FM', 'ALL'):
        gid[g] = pk
    elif g[1] == 'Not in the latest text':
        gid[g] = pk + '.x'
    else:
        n_in_part[pk] += 1
        gid[g] = '%s.%d' % (pk, n_in_part[pk])

def secname(n, pk):
    if n == 'Opening of the Part':
        return 'opening of Part %s' % pk
    return n
def gname(g):
    pk = g[0]
    if pk == 'ALL':
        return 'Vocabulary across the text'
    if pk == 'FM':
        return 'Front matter and notes before Part 0'
    if g[1] == 'Not in the latest text':
        return 'Part %s, not in the latest text' % pk
    names = [secname(x['section'][1], pk) for x in grp_secs[g]]
    # a heading split into labelled parts: say the heading once
    if all(' / ' in n for n in names):
        head = names[0].split(' / ')[0]
        names = [head + ' / ' + ' · '.join(n.split(' / ', 1)[1] for n in names)]
    return ' · '.join(names)
def glines(g):
    xs = grp_secs.get(g)
    if not xs:
        return ''
    a, b = min(x['first_line'] for x in xs), max(x['last_line'] for x in xs)
    return '%d' % a if a == b else '%d–%d' % (a, b)
def partname(pk):
    return PART_NAME.get(pk, '')

# ---- per-group facts
per = {tuple(p['group']): p for p in M['v2']['per_group']}
gch = defaultdict(list)
for a in A:
    gch[tuple(a['group'])].append(a)

def term_q(t):
    if not t:
        return ''
    kind = TERMS.get(t, '')
    return '“%s”%s' % (t, ' (old name)' if kind.startswith('old name') else '')

def rule(g):
    pk = g[0]
    if pk == 'ALL':
        return ('Vocabulary changes (scope term or whole text) whose sentences in the latest text sit in three or more Parts, '
                'or that name no line at all.')
    if pk == 'FM':
        return ('The title, the note under it, and the notes that stood before Part 0 in earlier texts '
                '(file 11\'s revision note, the note of sources and departures, the change list\'s fallback table).')
    if g[1] == 'Not in the latest text':
        return ('Changes to Part %s with no sentence in the latest text that name no section still standing and share '
                'too few words with any section of the Part (section lead under 0.5).' % pk)
    nsec = len(grp_secs[g])
    ln = glines(g)
    txt = 'Changes whose sentences sit wholly or mostly in %s %s' % ('lines' if '–' in ln else 'line', ln)
    if nsec > 1:
        txt += ' (%d sections of the text; those holding fewer than four changes are joined to a neighbour)' % nsec
    if any(a['home'] is None for a in gch[g]):
        txt += '; with them, changes with no sentence that name this section or share most words with it'
    return txt + '.'

# ---- short 'placed by'
def placed(a):
    h = a['how']
    st = re.search(r'\((never applied|not locatable|removed)\)', h)
    st = ' (%s)' % st.group(1) if st else ''
    if h == 'sentence':
        return 'its sentences, one section'
    m = re.match(r'majority of its sentences \((\d+) sections\)', h)
    if m:
        return 'most of its sentences (%s sections)' % m.group(1)
    m = re.match(r'term-wide \(sentences in (\d+) Parts\)', h)
    if m:
        return 'term-wide, %s Parts' % m.group(1)
    if h.startswith('term-wide, no line'):
        return 'term-wide, no line named' + st
    if h.startswith('section its source names'):
        return 'section its source names' + st
    m = re.match(r'section lead ([\d.]+)', h)
    if m:
        return 'section lead %s' % m.group(1) + st
    if h.startswith('Part its source names'):
        return 'Part only' + st
    if h.startswith('no Part named'):
        return 'note before Part 0' + st
    return h

def also(a):
    out = []
    for s in a['also']:
        g = sec2grp.get(tuple(s), tuple(s))
        if g != tuple(a['group']):
            out.append('%s (%s)' % (gid.get(g, g[0]), secname(s[1], s[0])))
    return '; '.join(out)

mv1, mv2 = M['v1'], M['v2']
def sizes_line(m):
    s = m['sizes_changes']
    s2 = sorted(s)
    med = s2[len(s2) // 2]
    return len(s), med, max(s), sum(1 for x in s if x <= 3), sum(1 for x in s if x > 40)

L = []
w = L.append
w('# S98 — Proposal: the records lumped by place in the latest text')
w('')
w('*Log S98, 26 September 2026, under the owner\'s instruction of that day (decision S30). One of the proposals for how to lump the ledger\'s records together; this one groups by **where in the text** their sentences sit. '
  'Made by program from `anchored.jsonl` (md5 %s) and `sentence index of the latest text.jsonl` (md5 %s), both read only. '
  'Programs and their outputs are in `proposal by place - scripts/`: `place.py` makes the groups and the measures (`assignment.jsonl`, `sections.json`, `measures.json`), `page.py` writes this page and `groups.json` (each group with its rule and its change ids). '
  'A rerun (`PYTHONDONTWRITEBYTECODE=1 python3 place.py v2 > /dev/null && PYTHONDONTWRITEBYTECODE=1 python3 page.py`) gives the same bytes. Nothing is committed.*'
  % (md5(os.path.join(GROUP, 'anchored.jsonl')), md5(os.path.join(GROUP, 'sentence index of the latest text.jsonl'))))
w('')
w('## The metric')
w('')
w('A change belongs to the stretch of the latest text its sentences sit in: the Part, then the section inside the Part (a `##` heading, or where a Part has none, a paragraph with a bold run-in label, with the unlabelled paragraphs after it), then the sentence. '
  'A change whose sentences sit in several sections goes to the section holding most of them, and a vocabulary change spread over three or more Parts goes to one group for the whole text. '
  'A change with no sentence in the latest text goes to the section its source names, or else to the section whose wording it shares most (only at a share of 0.5 or more), or else to its Part\'s group of wording not in the latest text.')
w('')
w('The unit placed is the **change** (`change_id`, 1275 of them), so the records that are one change seen in several sources stay together; each record goes with its change. Sections holding fewer than four changes are joined to the section before them in the same Part.')
w('')
w('## How it was measured, and the one adjustment')
w('')
w('The first cut (v1) used the sections as the text draws them: headings, run-in labels, unlabelled paragraphs joined to the label before them, every change with no sentence put in its Part\'s residue, and vocabulary changes treated like any other. The adjusted cut (v2) made these changes, all at once, after reading the v1 figures:')
w('')
w('1. **Grievances split.** "Grievances, anticipated" held 81 changes in one group with no shared term above a tenth of them; each of the eleven numbered grievances is now its own section.')
w('2. **Unlabelled paragraphs that start a new matter** get their own section instead of riding with the label before them: Part V line 259 (the conjunction (E)), Part X lines 407–411 (representation in use; construction is not selection) and 425 (what a new content may be), Part XI lines 441 (the aims of a repair) and 453 (Result, and the index of (EX)), Part XIV line 520 (what everything else is defined from).')
w('3. **Term-wide changes.** A change of scope term (or whole text) whose sentences sit in three or more Parts has no one place; it goes to the group *Vocabulary across the text* (46 changes). With one or two Parts it follows the majority rule.')
w('4. **Changes with no sentence.** First the section its source names (`target_part` after " / ", or a quoted paragraph name), if that heading or label still stands in the same Part; then the *section lead*: the section of the Part(s) named whose words the change\'s old and new wording share most, weighted by how rare each word is among sections, taken only at a share of 0.5 or more; otherwise the Part\'s residue. Notes with no Part join the front matter.')
w('5. **Small sections joined.** v1 had %d groups of one change and %d of three or fewer; a section with fewer than four changes now joins the section before it in its Part (the first ones join the next).' % (mv1['singletons'], sum(1 for x in mv1['sizes_changes'] if x <= 3)))
w('')
s1, s2 = sizes_line(mv1), sizes_line(mv2)
lt = mv2['lead_try']
w('| measure | v1 | v2 |')
w('| --- | --- | --- |')
w('| groups | %d | %d |' % (s1[0], s2[0]))
w('| changes per group: median / largest | %d / %d | %d / %d |' % (s1[1], s1[2], s2[1], s2[2]))
w('| groups of 3 or fewer changes | %d | %d |' % (s1[3], s2[3]))
w('| groups of more than 40 changes | %d | %d |' % (s1[4], s2[4]))
w('| changes in no group | 0 | 0 |')
w('| changes whose sentences sit in more than one section (records: %d) | %d | %d |' % (mv2['records_multi_section'], mv1['changes_multi_section'], mv2['changes_multi_section']))
p1 = mv1['placement']; p2 = mv2['placement']
def cnt(p, pre):
    return sum(v for k, v in p.items() if k.startswith(pre))
w('| changes with no sentence (181) placed in a section | 0 | %d |' % (cnt(p2, 'section')))
w('| changes with no sentence left in a Part residue | %d | %d |' % (cnt(p1, 'Part its source'), cnt(p2, 'Part its source')))
w('| term overlap inside groups (mean Jaccard of the changes\' terms) against the same group sizes drawn at random | %.3f against %.3f | %.3f against %.3f |' % (mv1['term_jaccard_within'], mv1['term_jaccard_random'], mv2['term_jaccard_within'], mv2['term_jaccard_random']))
w('')
w('Reading the figures:')
w('')
w('- **Term overlap.** Changes in one group share their theory terms %.1f times as much as changes drawn at random in v1 and %.1f times in v2. The table below leaves out each adjustment in turn: splitting the grievances and giving new matters their own sections raise the overlap; the vocabulary group and the joining of small sections lower it, the first because it gathers renames of different terms, the second because joined neighbours share fewer terms. The joining was kept because 26 groups of one to three changes line up little; the step that joins the proposals can switch it off (`min_changes` 0 in `place.py`) and have 130 groups on the text\'s own sections.' % (mv1['term_jaccard_within'] / mv1['term_jaccard_random'], mv2['term_jaccard_within'] / mv2['term_jaccard_random']))
w('')
w('| cut | groups | term overlap, all groups | term overlap, section groups only | groups of 3 or fewer | largest |')
w('| --- | --- | --- | --- | --- | --- |')
for ab in M['ablation']:
    w('| %s | %d | %.3f | %.3f | %d | %d |' % (ab['label'], ab['groups'], ab['within'], ab['within_sections'], ab['small'], ab['largest']))
w('')
w('- **The section lead** was tried on the %d placed records whose new wording is not word for word in the latest text: at a share of 0.5 or more it named the section they are placed in for %d of %d (%.0f%%); under 0.5 for %d of %d (%.0f%%). Hence the cut at 0.5. For the changes it placed that also carry the anchoring step\'s lead sentence (`latest_nearest`), the two leads name the same section in %d of %d.'
  % (lt['at or above 0.5 n'] + lt['below 0.5 n'], lt['at or above 0.5 same section'], lt['at or above 0.5 n'], 100 * lt['at or above 0.5 same section'] / lt['at or above 0.5 n'],
     lt['below 0.5 same section'], lt['below 0.5 n'], 100 * lt['below 0.5 same section'] / lt['below 0.5 n'],
     mv2['lead_agreement'].get('same section', 0), mv2['lead_agreement'].get('with a lead sentence', 0)))
w('- **Several places.** %d changes touch more than one section. %d of them are vocabulary changes that went to the whole-text group; the other %d are placed by the majority rule, and on average %.0f%% of their sentences sit in the group they are placed in. The table gives the other groups each one touches.'
  % (mv2['changes_multi_section'], mv2['changes_multi_section'] - mv2['multi_section_changes_placed_by_majority'], mv2['multi_section_changes_placed_by_majority'], 100 * mv2['multi_section_mean_share_inside']))
w('- **Does each group read as one part of the semantics?** The section groups do: each is a heading or a labelled paragraph the theory itself draws, so someone following the theory finds the group where they are reading. Three kinds of group read less well and are marked below: the joined groups (two to five short sections side by side), the Part residues (proposals the text never took, one bucket per Part; Part V\'s holds %d changes from three R2 amendments written against file 20: A on scope, B on dependence, C "Anchor the relevant parts"), and the vocabulary group (one matter, the renaming of terms, but no one place).'
  % len(gch[('V', 'Not in the latest text')]))
w('')
w('## How a change that touches several places is placed')
w('')
w('Count the change\'s sentences (over all its records) by section; it goes to the section holding most of them, and a tie goes to the one that comes first in the text. If the change is a vocabulary change (scope term or whole text) and its sentences sit in three or more Parts, it goes to *Vocabulary across the text* instead. Every other section it touches is listed in the column *also touches* of the assignment table, so reading by place can still find it there; the change itself is counted once.')
w('')
w('## The groups')
w('')
w('Ids run in text order: `V.3` is the third group of Part V, `V.x` Part V\'s residue, `FM` the front matter, `ALL` the vocabulary group. *No sentence* counts the changes in the group that have no sentence in the latest text. *Most shared term* is the theory term found in most of the group\'s changes, with the share of changes carrying it; old names are the ones the S95 vocabulary replaced.')
w('')
w('| id | group | lines | rule | changes | records | no sentence | most shared term |')
w('| --- | --- | --- | --- | --- | --- | --- | --- |')
cur = None
for g in gorder:
    p = per[g]
    w('| %s | %s | %s | %s | %d | %d | %d | %s (%.2f) |' % (
        gid[g], gname(g).replace('|', '\\|'), glines(g), rule(g).replace('|', '\\|'), p['changes'], p['records'], p['no_sentence'],
        term_q(p['shared_term']), p['shared_term_share']))
w('')
w('Part totals (changes): ' + '; '.join('%s %d' % ('Part ' + pk if pk not in ('FM', 'ALL') else pk, sum(len(gch[g]) for g in gorder if g[0] == pk)) for pk in PORDER if any(g[0] == pk for g in gorder)) + '.')
w('')
w('## Strengths and weaknesses')
w('')
w('**Strengths.**')
w('')
w('- The groups are the theory\'s own divisions, so a reader can lay each group beside the paragraph it concerns and read the old and new sentences in place; nothing depends on a judgment about what a change is about.')
w('- Every change has exactly one group, found by a stated rule from the anchors; %d of the %d changes sit in one section only, and the rule for the rest is mechanical.' % (p2.get('sentence', 0), len(A)))
w('- The Part numbers are the same in every version, so even the proposals written against file 20 or file 10 find their Part.')
w('- Term overlap inside groups is %.1f times that of random groups of the same sizes, so place and matter largely coincide.' % (mv2['term_jaccard_within'] / mv2['term_jaccard_random']))
w('')
w('**Weaknesses.**')
w('')
w('- A change is only as well placed as its anchor: the anchoring summary counts 582 records placed by similarity, 91 of them with a ratio under 0.4, and a wrong anchor puts its change in the wrong group.')
w('- %d changes (%d records) have no place in the latest text and sit in Part residues; the residue of Part V mixes several matters. The section lead places %d more, and about one in ten of those may belong in another section of the same Part.' % (
    cnt(p2, 'Part its source'), sum(p['records'] for g, p in per.items() if g[1] == 'Not in the latest text'), cnt(p2, 'section lead')))
w('- The same matter written in several places is split by place: counterparts are treated in Part V (why there is no counterpart-kind condition) and in Part XVI (arguments 1 and 2), the frozen question in grievance 10 and argument 7; each change goes to its own place, and only the *also touches* column and the vocabulary group gather such a matter.')
allp = set()
for a in gch[('ALL', 'Vocabulary across the text')]:
    for m in a['members']:
        for s_ in recs[m]['latest_sentences']:
            allp.add(sec_part[s_])
w('- The vocabulary group gathers the renames by kind of change, not by place; its %d changes reach %d of the 18 divisions of the text (front matter and Parts 0 to XVI).' % (len(gch[('ALL', 'Vocabulary across the text')]), len(allp)))
big = [gid[g] for g in gorder if len(grp_secs.get(g, [])) >= 3]
w('- Joining small sections gives groups whose sections are neighbours rather than one matter; %d groups join three or more sections (%s), and Part II is a single group.' % (len(big), ', '.join(big)))
szs = [len(gch[g]) for g in gorder]
w('- Group sizes stay uneven (from %d to %d changes), because the text\'s sections are uneven and the changes gather where the rounds worked hardest (the rivals and problems of Part VI, (E)\'s exclusions in Part V, Part XIV\'s dependence order).' % (min(szs), max(szs)))
w('')
w('## The full assignment: change → group')
w('')
w('One row per change, in the order of the text: by group, then by the position of its home sentence (changes with no sentence last in their group, then by change id). *Home sentence* is the first sentence of the change in its group (for a change with no sentence, empty). *Also touches* lists the other groups (and sections) its sentences reach. The records of each change are in `anchored.jsonl` under the same `change_id`; `proposal by place - scripts/assignment.jsonl` gives the same table with the record ids.')
w('')
w('| change | group | placed by | records | home sentence | also touches |')
w('| --- | --- | --- | --- | --- | --- |')
gpos = {g: i for i, g in enumerate(gorder)}
for a in sorted(A, key=lambda a: (gpos[tuple(a['group'])], uorder.get(a['home'], 10**6), a['change_id'])):
    g = tuple(a['group'])
    w('| %s | %s | %s | %d | %s | %s |' % (a['change_id'], gid[g], placed(a), len(a['members']), a['home'] or '', also(a).replace('|', '\\|')))
w('')
open(os.path.join(GROUP, 'proposal by place.md'), 'w', encoding='utf-8').write('\n'.join(L))

# also a plain map for whoever joins the proposals
with open(os.path.join(HERE, 'groups.json'), 'w', encoding='utf-8') as f:
    json.dump([dict(id=gid[g], name=gname(g), part=g[0], lines=glines(g), rule=rule(g), changes=len(gch[g]),
                    records=per[g]['records'], change_ids=[a['change_id'] for a in gch[g]]) for g in gorder], f, ensure_ascii=False, indent=1)
print('groups', len(gorder), 'rows', len(A))
