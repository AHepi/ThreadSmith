"""Step 4b: the anchoring summary (markdown), written from the anchored ledger by program."""
import json, sys, os, re
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib_anchor import *

A = [json.loads(l) for l in open(GROUP + '/anchored.jsonl', encoding='utf-8')]
IDX = [json.loads(l) for l in open(GROUP + '/sentence index of the latest text.jsonl', encoding='utf-8')]
ID = {u['id']: u for u in IDX}
MAPS = json.load(open(GROUP + '/line maps.json', encoding='utf-8'))
SIDE = json.load(open(GROUP + '/anchor - scripts/step3 side data.json', encoding='utf-8'))
PARTS = []
for u in IDX:
    if u['part'] not in PARTS:
        PARTS.append(u['part'])
COLL = {'A': 'the earliest rounds, before file 11', 'B': 'file 10 to file 11, and the checks on file 11',
        'C': 'the revision 2 change list and its rulings', 'D': 'the scrub, the repairs and the last cross-examination',
        'E': 'recommendations never applied, and the decision record'}
STATUSES = ['anchored', 'removed', 'never applied', 'not locatable']
out = []
w = out.append


def row(*cells):
    w('| ' + ' | '.join(str(c) for c in cells) + ' |')


def opening(t, n=12):
    t = t.replace('\n', ' ').replace('|', '\\|')
    words = t.split()
    return ' '.join(words[:n]) + (' …' if len(words) > n else '')


n = len(A)
changes = len({a['change_id'] for a in A})
st = Counter(a['latest_status'] for a in A)
w('# S98 — the anchoring summary: every collected record placed on the latest text')
w('')
w('*Log S98, 26 September 2026, under the owner\'s instruction of that day (decision S30). This is the anchor step of the '
  'ledger: it takes the five collectors\' records in `collect/`, places each on the sentences of the latest text that it '
  'touches, names the theory\'s terms in its wording, and joins the records that are one change seen in several sources. '
  'Nothing in `collect/` was changed; every collector field is carried into `anchored.jsonl` byte for byte. '
  'The files were written by the programs in `anchor - scripts/`, and this page by `step4_summary.py`.*')
w('')
w('## In brief')
w('')
w('- **Records:** %d, from five collectors. **Changes:** %d, after joining duplicates.' % (n, changes))
w('- **Placed on sentences of the latest text:** %d (%.0f%%). The rest have an empty `latest_sentences`: removed %d, never applied %d, not locatable %d.'
  % (st['anchored'], 100.0 * st['anchored'] / n, st['removed'], st['never applied'], st['not locatable']))
nyes = sum(1 for a in A if a['new_in_latest'] == 'yes')
w('- **Wording still standing:** in %d records the new wording (or the whole new sentence) is found word for word in the latest text.' % nyes)
near = sum(1 for a in A if a.get('latest_nearest'))
w('- **Records with no place but a Part:** every record with an empty anchor keeps `latest_part` and `latest_parts` from the Part its source names (Part numbers are the same in every version). '
  '%d of them also carry `latest_nearest`: the latest-text sentence sharing most content words with the record, in that Part. It is offered to the grouping step as a lead and is not an anchor.' % near)
w('- **Latest text:** `%s`, md5 %s, %d lines.' % (VPATH['latest'].split('/')[-1], md5(VPATH['latest']), MAPS['versions']['latest']['lines']))
w('')
w('## The three files')
w('')
kinds = Counter(u['kind'] for u in IDX)
w('- **`sentence index of the latest text.jsonl`** — %d units: %d sentences, %d headings, %d displayed formulas (each one unit, however many lines), %d list items (each one unit). '
  'Fields: `id` (`L<line>.s<n>`), `line`, `line_end`, `n`, `kind`, `part`, `heading` (the `##` heading above it), `label` (the bold run-in label of its paragraph), `text`, and `start`/`end` (character offsets in its line). '
  'Sentences are cut as collector A cut them (mathematics and code never cut; a bare bold label joins the sentence after it), with two additions: a numbered bold label such as `**1.` does not end a sentence, and a closing tag such as `(K3)` stays with the sentence before it.'
  % (len(IDX), kinds['sentence'], kinds['heading'], kinds['display'], kinds['list item']))
w('- **`line maps.json`** — maps between consecutive versions: file 10 → file 11 → draft 1 → draft 2 → draft 3 → draft 4 → draft 5 → scrubbed copy → repaired copy → latest text, and each version composed to the latest text (`to_latest`). '
  'It also holds the sentence-level map file 10 → file 11 and the check of the change list\'s FILE-11 LINE fields.')
w('- **`anchored.jsonl`** — the %d records, in collector order, each with the collector\'s fields unchanged and these added: '
  '`latest_sentences`, `latest_status`, `latest_reason` (only when the anchor is empty), `latest_part`, `latest_heading`, `latest_parts`, `latest_lines`, '
  '`latest_nearest` (only for some records with no anchor), `anchor_method`, `anchor_ratio`, `new_in_latest` (yes / no / n/a), `target_version`, `terms`, `change_id`, `change_members`.' % n)
w('')
w('## How the line maps were made')
w('')
row('pair', 'method', 'equal', 'changed', 'moved', 'removed', 'lines new in the later text')
row(*['---'] * 7)
for k, v in MAPS['pairs'].items():
    c = v['counts']
    moved = sum(x for kk, x in c.items() if kk.startswith('moved'))
    meth = 'line for line' if v['method'].startswith('line for line') else 'difflib' + (' + sentence map' if 'sentence-level' in v['method'] else '')
    row(k.replace('->', ' → '), meth, c.get('equal', 0), c.get('changed', 0), moved, c.get('removed', 0), len(v['inserted_lines_in_later']))
w('')
cl = MAPS['change_list_file11_lines']
agree = Counter(str(x.get('agree')) for x in cl)
w('Draft 5, the scrubbed copy, the repaired copy and the latest text keep the same 632 lines, so those three maps send each line to itself. '
  'The other maps use difflib on lines; inside a changed block, lines are paired by similarity (ratio 0.3 or more), and lines left over are paired across the text as moved (ratio 0.6 or more). '
  'Between file 10 and file 11, %d lines that difflib could not place were placed through the sentence-level map (the file-11 line of their most similar sentence). '
  % len(MAPS['pairs']['f10->f11'].get('lines_placed_by_the_sentence_map', [])))
w('')
w('The change list has %d entries. For each, the program found the first line of its NEW text in each draft and compared that line with where the difflib maps send its FILE-11 LINE: '
  '%d agree, %d differ, and %d have no FILE-11 LINE or no NEW line to find (record-only entries and meta blocks). The %d that differ are entries whose NEW stands before or after the anchor lines their FILE-11 LINE names '
  '(W59.1 and W60.1 insert next to their anchor; W7.2 and W10a.1 add lines before the changed one; W30.1\'s NEW stands at draft 5 line 119, away from its OLD at file-11 line 161). They are listed in the file.'
  % (len(cl), agree['True'], agree['False'], agree['None'], agree['False']))
w('')
w('## How each record was placed')
w('')
w('The program tries these in order and stops at the first that gives a place. The `anchor_method` field says which one was used.')
w('')
w('1. **Notes and other texts.** A change to a note (file 11\'s revision note, file 13\'s note and record, the note of sources and departures) is not in any theory text after file 11. If the note entry declares a change at a named place ("file-11 line 337", "draft 5 L317"), the record is placed on that place; otherwise it is left empty as *not locatable*. The one change to file 12 is *not locatable* (a separate text). Changes to the whole text are *not locatable*.')
w('2. **The place of the change.** A line in the latest text, found from: the new wording\'s line in the text that first carried it (for applied records); the file-11 line in collector B\'s source reference; the line named in `applied_in`; the record\'s `target_line` in its target text; or its old wording\'s line in the target text. Each is carried to the latest text by the line maps. The stage-1 text of S96 is not on disk; it keeps the repaired copy\'s lines, so its line numbers are read as the repaired copy\'s.')
w('3. **Vocabulary entries** (scope `term`): the lines the entry names ("l. 317"), then a phrase the entry quotes as its new wording found in the latest text, then the places where its old words stood in the target text, carried to the latest text.')
w('4. **New wording, word for word** (whitespace and quotation marks normalised): the whole new sentence, then the new span. A span under 25 characters is only looked for within two lines of the place. Where the place is known, a span, and any wording of a record that was not applied, counts only within five lines of it, so that a phrase a proposal borrowed from elsewhere in the text does not move it. Where the wording stands in several places, the one nearest the place is taken.')
w('5. **Old wording, word for word:** the place still reads as it did (a recommendation not taken, or an old sentence kept).')
w('6. **The mapped line:** the sentence on that line most similar to the record (difflib ratio for whole sentences; for a span, the ratio against the window of the sentence that matches it most closely). Applied records are compared by their new wording first, the others by their old wording first. If nothing on the line comes to 0.5, the two lines each side are tried, then the whole Part (a sentence at 0.6 or more that is at least 0.15 closer is taken). Below 0.25 the whole paragraph on the line is taken. A record with no wording to compare takes the paragraph.')
w('7. **The whole Part:** with no place at all, the most similar sentence in the Part the source names, at a ratio of 0.6 or more.')
w('8. **A record of the same change:** a record still without a place takes the place of the most similar record of its change group.')
w('')
w('What is left is empty, with the reason in `latest_reason`: *removed* when the place of the change was last present in an earlier text and is gone after it; *never applied* when a proposal that was not taken has no place the program can find; *not locatable* otherwise.')
w('')
w('### Placed records by method')
w('')
mcount = Counter()
for a in A:
    m = a['anchor_method'] or ''
    if not m:
        continue
    prev = None
    while prev != m:
        prev = m
        m = re.sub(r'\([^()]*\)', '\u27e8\u2026\u27e9', m)
    m = m.replace('\u27e8\u2026\u27e9', '(…)')
    m = re.sub(r'the \d+ places', 'the N places', m)
    m = re.sub(r'line \d+', 'line N', m)
    m = re.sub(r'same change as [A-E]-N', 'same change as another record', m)
    mcount[m] += 1
row('method', 'records')
row('---', '---')
for m, c in mcount.most_common():
    row(m.replace('|', '/'), c)
w('')
ratios = [a['anchor_ratio'] for a in A if a['anchor_ratio'] is not None and (a['anchor_method'] or '').startswith(('line map', 'most similar', 'a declaration'))]
bands = Counter(min(int(r * 10), 9) for r in ratios)
w('Similarity of the sentences placed by a line map or by similarity (%d records): ' % len(ratios) +
  ', '.join('%.1f–%.1f: %d' % (b / 10, (b + 1) / 10, bands[b]) for b in range(10) if bands[b]) + '. Records below 0.4 are the ones to read first when checking.')
w('')
w('## Counts')
w('')
w('### By collector')
w('')
row('collector', 'records', *STATUSES, 'new wording in the latest text', 'changes')
row(*['---'] * 8)
for c in 'ABCDE':
    rs = [a for a in A if a['rid'].startswith(c + '-')]
    s = Counter(a['latest_status'] for a in rs)
    row('%s — %s' % (c, COLL[c]), len(rs), *[s[x] for x in STATUSES], sum(1 for a in rs if a['new_in_latest'] == 'yes'), len({a['change_id'] for a in rs}))
s = Counter(a['latest_status'] for a in A)
row('**all**', n, *[s[x] for x in STATUSES], nyes, changes)
w('')
w('### By the record\'s own status')
w('')
row('status', 'records', *STATUSES)
row(*['---'] * 6)
for k, v in Counter(a['status'] for a in A).most_common():
    s = Counter(a['latest_status'] for a in A if a['status'] == k)
    row(k, v, *[s[x] for x in STATUSES])
w('')
w('### By kind')
w('')
row('kind', 'records', *STATUSES)
row(*['---'] * 6)
for k, v in Counter(a['kind'] for a in A).most_common():
    s = Counter(a['latest_status'] for a in A if a['kind'] == k)
    row(k, v, *[s[x] for x in STATUSES])
w('')
w('### By Part of the latest text')
w('')
w('A record placed on sentences in two Parts is counted in each (third column). The fourth column counts each placed record once, by its first sentence. The fifth counts records with no anchor, by the Part their source names.')
w('')
row('Part of the latest text', 'sentences in it', 'placed records touching it', 'placed records, first sentence here', 'records with no anchor, Part named', 'changes touching it')
row(*['---'] * 6)
nsent = Counter(u['part'] for u in IDX)
for p in PARTS + ['']:
    touch = [a for a in A if a['latest_status'] == 'anchored' and p in a['latest_parts']]
    first = [a for a in A if a['latest_status'] == 'anchored' and a['latest_part'] == p]
    un = [a for a in A if a['latest_status'] != 'anchored' and (p in a['latest_parts'] if p else not a['latest_parts'])]
    if not p and not un:
        continue
    ch = {a['change_id'] for a in touch + un}
    row(p or '(no Part named)', nsent.get(p, 0), len(touch), len(first), len(un), len(ch))
w('')
w('### By heading inside each Part (placed records, by first sentence)')
w('')
byh = Counter((a['latest_part'], a['latest_heading']) for a in A if a['latest_status'] == 'anchored')
row('Part', 'heading or run-in label', 'records')
row('---', '---', '---')
for p in PARTS:
    for (pp, h), c in sorted(byh.items(), key=lambda x: -x[1]):
        if pp == p and c >= 8:
            row(p, h or '(opening of the Part)', c)
w('')
w('Headings with fewer than 8 placed records are left out of this table; `anchored.jsonl` has them all.')
w('')
w('## The records with no anchor, and why')
w('')
reasons = defaultdict(list)
for a in A:
    if a['latest_status'] == 'anchored':
        continue
    r = a['latest_reason'] or ''
    r = re.sub(r'\(highest ratio [0-9.]+\)', '(ratio under the threshold)', r)
    r = re.sub(r'its place \(.*?\) was last present in (.*?) and', r'its place was last present in \1 and', r)
    reasons[(a['latest_status'], r)].append(a['rid'])
row('empty as', 'why', 'records', 'which')
row('---', '---', '---', '---')
for (s, r), rids in sorted(reasons.items(), key=lambda x: (STATUSES.index(x[0][0]), -len(x[1]))):
    by = Counter(x[0] for x in rids)
    if len(rids) > 30:
        which = '; '.join('%s: %d' % (c, by[c]) for c in 'ABCDE' if by[c]) + ' (listed in the file by `latest_reason`)'
    else:
        which = ', '.join(rids)
    row(s, r.replace('|', '/'), len(rids), which)
w('')
na = [a for a in A if a['latest_status'] == 'never applied']
ba = Counter(a['rid'][0] for a in na)
w('Most records never applied are collector A\'s: the R2 amendments and Stage B phrases were written against file 20, which is not held, and give no old wording or line; the file 10 Part they name is kept in `latest_part`. '
  'Collector A\'s S72 Stage 2 lines (W01 to W12), carried into file 11 in other wording, have no line either and are *not locatable*; most of them have a `latest_nearest`. '
  'By collector, never applied: ' + ', '.join('%s %d' % (c, ba[c]) for c in 'ABCDE' if ba[c]) + '.')
w('')
w('## Duplicates joined')
w('')
joins = Counter(re.sub(r' \(.*', '', j[2]) for j in SIDE['joins'])
sizes = Counter(len(set(a['change_members'])) for a in {a['change_id']: a for a in A}.values())
w('Records are one change when a collector linked them (`same_as`, by record id, or by a change-list entry id that collector C holds), or when they have the same old and new wording after normalising whitespace and quotation marks **and** the same place (overlapping latest sentences, or the same target line). '
  'The place is required because one wording can be changed the same way at many places (the scrub turned `*Proof.*` into `*Why this and not its denial.*` at eleven lines, and these stay eleven changes). '
  'Vocabulary entries with the same old and new cells are joined without a place. A record with the same wording but no place joins only a group that has one place.')
w('')
w('Links made: ' + ', '.join('%s %d' % (k, v) for k, v in joins.most_common()) + '. '
  'Groups by size: ' + ', '.join('%d record%s: %d' % (k, '' if k == 1 else 's', v) for k, v in sorted(sizes.items())) + '.')
w('')
ext = Counter(s.split('#')[0].split('/')[-1] for r, s in SIDE['external_same_as'])
w('%d `same_as` pointers name a place in a file no collector recorded entry by entry (%s). They point to a worklist item, a plan item or a row of the revision note\'s layer 2, each of which can cover several changes, so they are kept in the record and not joined.'
  % (len(SIDE['external_same_as']), '; '.join('%s: %d' % (k, v) for k, v in ext.most_common())))
w('')
big = sorted({a['change_id']: a for a in A}.values(), key=lambda a: -len(a['change_members']))[:8]
w('The largest groups come from collectors\' links between a proposal and its later restatements (collector A), or between a ruling and the several edits that carry it (collector D). The grouping step may want to split them:')
w('')
row('change', 'records', 'members')
row('---', '---', '---')
for a in big:
    row(a['change_id'], len(a['change_members']), ', '.join(a['change_members']))
w('')
w('## The 40 latest-text sentences touched by the most records')
w('')
w('Counted over placed records. A vocabulary entry (scope `term`) touches every place its words stood, so the table also gives the count without them.')
w('')
cnt, cnt_nt, chs = Counter(), Counter(), defaultdict(set)
for a in A:
    for x in a['latest_sentences']:
        cnt[x] += 1
        chs[x].add(a['change_id'])
        if a['scope'] != 'term':
            cnt_nt[x] += 1
row('sentence', 'Part / heading', 'records', 'without vocabulary entries', 'changes', 'opening words')
row(*['---'] * 6)
for x, c in sorted(cnt.items(), key=lambda kv: (-kv[1], IDX.index(ID[kv[0]])))[:40]:
    u = ID[x]
    h = u['heading'] + (' / ' if u['heading'] and u['label'] else '') + u['label']
    row(x, u['part'].split(' — ')[0] + (' / ' + h if h else ''), c, cnt_nt[x], len(chs[x]), '"' + opening(u['text']).replace('"', "'") + '"')
w('')
w('Sentences of the latest text touched by at least one record: %d of %d units.' % (len(cnt), len(IDX)))
w('')
w('## The 40 terms met in the most records')
w('')
w('The term list (%d terms) is in `anchor - scripts/step3 side data.json`. It holds the bold defined terms of the latest text, the run-in labels that name a defined notion, the tagged conditions with names of two or more characters, and the old names the S95 vocabulary replaced (the draft 5 column of `tests/S95 Scrub - vocabulary, as used.md`, plus the old names it gives in prose). '
  'A term is matched in a record\'s `old` and `new` wording, ignoring case and allowing a plural or past ending. Old names are shown in backticks: they are quoted words, not this page\'s own.' % len(SIDE['terms']))
w('')
tc, tch = Counter(), defaultdict(set)
for a in A:
    for t in a['terms']:
        tc[t] += 1
        tch[t].add(a['change_id'])
row('term', 'kind', 'records', 'changes')
row(*['---'] * 4)
for t, c in tc.most_common(40):
    k = SIDE['terms'].get(t, '')
    shown = ('`%s`' % t) if k.startswith('old') else t
    row(shown, 'old name (S95)' if k.startswith('old') else k.replace('defined in the latest text', 'defined'), c, len(tch[t]))
w('')
w('Records with no term in their wording: %d.' % sum(1 for a in A if not a['terms']))
w('')
w('## Where the program needed judgement')
w('')
w('- **Paragraph anchors.** Where no sentence on the mapped line comes to 0.25, the whole paragraph is the anchor (%d records). Declarations placed on a named line take the paragraph when their text is a paraphrase.' % sum(1 for a in A if 'whole paragraph' in (a['anchor_method'] or '')))
w('- **Vocabulary entries.** Their cells mix words, quoted phrases and descriptions; the program reads the quoted phrases, the words before any bracket, and any line numbers. %d entries are placed; %d could not be (listed above).' % (sum(1 for a in A if a['scope'] == 'term' and a['latest_status'] == 'anchored'), sum(1 for a in A if a['scope'] == 'term' and a['latest_status'] != 'anchored')))
w('- **Removals.** A record that deleted a sentence is placed on the sentence of the same paragraph most similar to what was deleted, or on the paragraph.')
w('- **Anchors taken from the group.** %d records took the place of another record of their change; `anchor_method` names it.' % sum(1 for a in A if (a['anchor_method'] or '').startswith('same change as')))
w('- **`latest_nearest`** is a lead, not a place: it is the sentence sharing most content words with the record in the Part its source names (word overlap of 0.15 or more).')
w('- **Parts and headings** for records with no anchor come from the Part number their source gives; the Part titles changed (for example Part VI\'s), the numbers did not.')
w('')
w('## Rerun')
w('')
w('From `group/anchor - scripts/`: `PYTHONDONTWRITEBYTECODE=1 python3 step1_index.py`, then `step2_maps.py`, `step3_anchor.py`, `step4_summary.py` and `step4_check.py`. '
  'The check confirms that every collector field is unchanged, every sentence id exists, the status agrees with the anchor, every "yes" in `new_in_latest` is found in the latest text and in the anchored sentences, the change groups agree, and that the words of decision S23 are absent from this step\'s own prose.')
w('')
open(GROUP + '/anchoring summary.md', 'w', encoding='utf-8').write('\n'.join(out))
print('written', len(out), 'lines')
