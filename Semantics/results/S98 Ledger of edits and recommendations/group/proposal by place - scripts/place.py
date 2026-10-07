"""Lens: where in the latest text. Groups the S98 records by the part of the
latest text their sentences sit in: Part, then section (heading or run-in
label), then sentence.

Run:  PYTHONDONTWRITEBYTECODE=1 python3 place.py v1   (the first cut, measured)
      PYTHONDONTWRITEBYTECODE=1 python3 place.py v2   (the adjusted cut; writes the outputs)

Reads only group/anchored.jsonl and group/sentence index of the latest text.jsonl.
Writes (v2 only): group/proposal by place - scripts/assignment.jsonl and
measures.json; the page group/proposal by place.md is written by page.py.
"""
import json, sys, os, re, itertools, random
from collections import Counter, defaultdict, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
GROUP = os.path.dirname(HERE)
VERSION = sys.argv[1] if len(sys.argv) > 1 else 'v2'

recs = [json.loads(l) for l in open(os.path.join(GROUP, 'anchored.jsonl'), encoding='utf-8')]
units = [json.loads(l) for l in open(os.path.join(GROUP, 'sentence index of the latest text.jsonl'), encoding='utf-8')]
uid = {u['id']: u for u in units}
order = {u['id']: i for i, u in enumerate(units)}

ROMAN = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI']
def part_key(part):
    if part.startswith('Front'):
        return 'FM'
    m = re.match(r'Part ([0IVX]+) ', part)
    return m.group(1) if m else None
def part_short(part):
    return part.split(' — ')[0] if ' — ' in part else part
PART_NAME = OrderedDict()
for u in units:
    PART_NAME.setdefault(part_key(u['part']), u['part'])

# ---------------------------------------------------------------- sections
# v1: heading if any; else run-in label; else the labelled paragraph before it
#     in the same Part; else the Part's opening.
# v2 adjustments (one pass, after measuring v1) are listed in ADJUST below.

ADJUST = {
    # 1. Unlabelled paragraphs that open a new matter get their own section
    #    instead of joining the labelled paragraph before them. Named by what
    #    they define (read from the sentence index, first words of the line).
    'own_section_lines': {
        259: 'The conjunction (E)',        # Part V "Thus ... Account iff ..." to line 265
        407: 'Representation in use; construction is not selection',   # Part X 407-411
        425: 'What a new content may be',   # Part X 425
        441: 'The aims of a repair',            # Part XI 441
        453: 'Result, and the index of (EX)',  # Part XI 453
        520: 'What everything else is defined from',     # Part XIV 520
    },
    # 2. The eleven grievances of Part 0 are sections of their own
    #    (Grievances, anticipated is one heading with 46 sentences).
    'split_by_label_under_heading': ['Grievances, anticipated'],
    # 3. Term-wide changes whose sentences sit in three or more Parts go to one
    #    group for the whole text; with fewer Parts they follow the majority rule.
    'term_wide_parts': 3,
    # 4. Records with no sentence: the section their source names, if that
    #    heading or label still stands in the same Part; else the lead sentence
    #    (latest_nearest) in the Part named; else the Part's own residue group.
    'use_named_section': True,
    'use_lead': True,
    # 5. Sections holding fewer than MIN changes are merged into the section
    #    before them in the same Part (or after, for the first).
    'min_changes': 4,
}

def section_of_units(version):
    sec = {}
    last_label = {}
    for u in units:
        pk = part_key(u['part'])
        if u['kind'] == 'heading' and u['text'].startswith('# '):
            sec[u['id']] = (pk, 'Opening of the Part'); last_label[pk] = None; continue
        if u['heading']:
            name = u['heading']
            if version == 'v2' and name in ADJUST['split_by_label_under_heading']:
                if u['label']:
                    name = name + ' / ' + u['label']
                    last_label[(pk, u['heading'])] = name
                else:
                    name = last_label.get((pk, u['heading'])) or name + ' / introduction'
                    # heading line and the paragraph before the first grievance
            sec[u['id']] = (pk, name); continue
        if u['label']:
            last_label[pk] = u['label']
            sec[u['id']] = (pk, u['label']); continue
        if version == 'v2' and u['line'] in ADJUST['own_section_lines']:
            last_label[pk] = ADJUST['own_section_lines'][u['line']]
        name = last_label.get(pk) or 'Opening of the Part'
        sec[u['id']] = (pk, name)
    return sec

def section_order(sec):
    o = OrderedDict()
    for u in units:
        o.setdefault(sec[u['id']], len(o))
    return o

# ------------------------------------------------------------ helpers
def terms_of(r):
    return set(r.get('terms') or [])

def named_section(r, sec_names_by_part):
    """The heading or label the source names in target_part (after ' / ', or a
    quoted paragraph name), if it still stands in the same Part of the latest text."""
    tp = r.get('target_part') or ''
    for chunk in tp.split(';'):
        chunk = chunk.strip()
        pk = part_key(chunk + ' ')
        if pk is None or pk not in sec_names_by_part:
            continue
        names = sec_names_by_part[pk]
        cands = []
        if ' / ' in chunk:
            tail = re.sub(r'\[.*?\]|\(.*?\)', '', chunk.split(' / ', 1)[1]).strip().lower()
            if tail:
                cands.append(tail)
        cands += [q.lower() for q in re.findall(r'"([^"]{4,})"', chunk)]
        for tail in cands:
            exact = [n for n in names if n.lower() == tail]
            if exact:
                return (pk, exact[0])
            based = [n for n in names if n.split(' / ')[0].lower() == tail]
            if based:
                return (pk, based[0])
            pref = [n for n in names if len(tail) >= 6 and (n.lower().startswith(tail) or tail.startswith(n.lower()))]
            if pref:
                return (pk, pref[0])
    return None

# section-level lead: the section of the named Part(s) whose words the record's
# wording shares most, weighted by how rare each word is among sections.
STOP = set(("this that with from have which when what there their they them than then into only does each such "
            "other more most also been were will would these those some over under must your about where while "
            "being because between within without whose same very just like here both either neither whether upon "
            "onto after before since until below above ever even much many any all its not nor for and the are was "
            "one two who how can may has had but our out").split())
def words(t):
    t = re.sub(r'\\\(.*?\\\)|\\\[.*?\\\]', ' ', t or '', flags=re.S)
    return {w for w in re.findall(r'[a-z][a-z\-]{3,}', t.lower()) if w not in STOP}
LEAD_MIN = 0.5
def make_lead(sec):
    import math
    secw = defaultdict(set)
    for u in units:
        secw[sec[u['id']]] |= words(u['text'])
    df = Counter(w for ws in secw.values() for w in ws)
    N = len(secw)
    idf = {w: math.log(N / c) for w, c in df.items()}
    def lead(members, pks):
        rw = set()
        for r in members:
            rw |= words((r.get('new') or '') + ' ' + (r.get('old') or ''))
        rw = {w for w in rw if w in idf}
        tot = sum(idf[w] for w in sorted(rw))
        if not tot:
            return None, 0.0
        sc = sorted(((sum(idf[w] for w in sorted(rw & ws)) / tot, k) for k, ws in secw.items() if k[0] in pks), key=lambda x: -round(x[0], 9))
        return (sc[0][1], round(sc[0][0], 3)) if sc else (None, 0.0)
    return lead

# ------------------------------------------------------------ assignment
SEC2GROUP = {}
def assign(version):
    global LEAD
    SEC2GROUP.clear()
    sec = section_of_units(version)
    sord = section_order(sec)
    LEAD = make_lead(sec)
    sec_names_by_part = defaultdict(list)
    for (pk, n) in sord:
        sec_names_by_part[pk].append(n)

    changes = OrderedDict()
    for r in recs:
        changes.setdefault(r['change_id'], []).append(r)

    out = OrderedDict()
    rec_sections = {}
    for r in recs:
        rec_sections[r['rid']] = [sec[s] for s in r['latest_sentences'] if s in sec]

    for cid, members in changes.items():
        cnt = Counter()
        sents = []
        for r in members:
            for s in r['latest_sentences']:
                cnt[sec[s]] += 1
                sents.append(s)
        is_term = any(r['scope'] in ('term',) for r in members)
        parts_touched = {k[0] for k in cnt}
        how = None
        if cnt:
            if version == 'v2' and is_term and len(parts_touched) >= ADJUST['term_wide_parts']:
                g = ('ALL', 'Vocabulary across the text'); how = 'term-wide (sentences in %d Parts)' % len(parts_touched)
            else:
                most = max(cnt.values())
                cands = [k for k in cnt if cnt[k] == most]
                g = min(cands, key=lambda k: sord[k])
                how = 'sentence' if len(cnt) == 1 else 'majority of its sentences (%d sections)' % len(cnt)
            home = min((s for s in set(sents) if sec[s] == g), key=lambda s: order[s], default=None) if g[0] != 'ALL' else min(set(sents), key=lambda s: order[s])
            also = sorted({k for k in cnt if k != g}, key=lambda k: sord[k])
        else:
            home = None; also = []
            pks = []
            for r in members:
                for p in (r.get('latest_parts') or []) + [r.get('latest_part') or '']:
                    k = part_key(p + ' ') if p else None
                    if k and k not in pks:
                        pks.append(k)
            pk = pks[0] if pks else None
            status = Counter(r['latest_status'] for r in members).most_common(1)[0][0]
            scope_whole = all(r['scope'] in ('whole text', 'term') for r in members)
            g = None
            if version == 'v2' and scope_whole and not pk:
                g = ('ALL', 'Vocabulary across the text'); how = 'term-wide, no line named (%s)' % status
            if g is None and pk is None:
                g = ('OUT', 'Notes outside the Parts'); how = 'no Part named (%s)' % status
            if g is None and version == 'v2' and ADJUST['use_named_section']:
                for r in members:
                    ns = named_section(r, sec_names_by_part)
                    if ns:
                        g = ns; how = 'section its source names (%s)' % status; break
            if g is None and version == 'v2' and ADJUST['use_lead']:
                k, score = LEAD(members, set(pks))
                if k is not None and score >= LEAD_MIN:
                    g = k; how = 'section lead %.2f, not an anchor (%s)' % (score, status); lead_sec = k
            if g is None:
                g = (pk, 'Not in the latest text'); how = 'Part its source names (%s)' % status
        out[cid] = dict(change_id=cid, group=g, how=how, home=home,
                        also=also, members=[r['rid'] for r in members],
                        n_sent=len(set(sents)), section=g)
    if version == 'v2':
        # notes outside the Parts join the front matter: both stand before Part 0
        for v in out.values():
            if v['group'][0] in ('OUT', 'FM'):
                v['group'] = ('FM', 'Front matter and notes')
        # merge sections holding fewer than min_changes changes into the section
        # before them in the same Part (the first ones carry forward to the next)
        size = Counter(v['group'] for v in out.values())
        merged = {}
        for pk in PART_NAME:
            secs = [k for k in sord if k[0] == pk and size.get(k, 0) > 0]
            kept = [k for k in secs if size[k] >= ADJUST['min_changes']]
            if not kept:
                continue
            for i, k in enumerate(secs):
                if k in kept:
                    continue
                before = [x for x in secs[:i] if x in kept]
                after = [x for x in secs[i + 1:] if x in kept]
                merged[k] = before[-1] if before else after[0]
        for v in out.values():
            g = v['group']
            if g in merged:
                v['merged_from'] = g[1]
                v['group'] = merged[g]
        # every section of the text, empty or not, to the group that holds its place
        for pk in PART_NAME:
            secs = [k for k in sord if k[0] == pk]
            kept = [k for k in secs if k not in merged and size.get(k, 0) >= ADJUST['min_changes']]
            for i, k in enumerate(secs):
                if k in kept:
                    SEC2GROUP[k] = k
                elif k in merged:
                    SEC2GROUP[k] = merged[k]
                else:
                    before = [x for x in secs[:i] if x in kept]
                    after = [x for x in secs[i + 1:] if x in kept]
                    SEC2GROUP[k] = before[-1] if before else (after[0] if after else k)
        for k in list(SEC2GROUP):
            if k[0] == 'FM':
                SEC2GROUP[k] = ('FM', 'Front matter and notes')
        names = defaultdict(list)
        for k, t in merged.items():
            names[t].append(k[1])
        for v in out.values():
            g = v['group']
            if g in names:
                parts = [g[1]] + names[g]
                parts.sort(key=lambda n: sord.get((g[0], n), 0))
                v['group_name'] = ' + '.join(parts)
        # keep names honest: a group that took in others lists them
    return out, sec, sord

# ------------------------------------------------------------ measures
def measure(out, sec, sord, version):
    groups = defaultdict(list)
    for v in out.values():
        groups[v['group']].append(v)
    rec_by_id = {r['rid']: r for r in recs}
    # records in more than one group (by their own sentences' sections)
    multi_rec = 0; multi_change = 0; none_rec = 0
    for r in recs:
        ss = {sec[s] for s in r['latest_sentences']}
        if len(ss) > 1: multi_rec += 1
        if not ss: none_rec += 1
    for v in out.values():
        if v['also']: multi_change += 1
    sizes_c = sorted((len(vs) for vs in groups.values()), reverse=True)
    sizes_r = sorted((sum(len(v['members']) for v in vs) for vs in groups.values()), reverse=True)
    # coherence: term overlap inside groups vs the same group sizes drawn at random
    cterms = {cid: set().union(*[terms_of(rec_by_id[m]) for m in v['members']]) for cid, v in out.items()}
    df = Counter(t for ts in cterms.values() for t in ts)
    N = len(cterms)
    common = {t for t, c in df.items() if c > 0.15 * N}
    def jac(a, b):
        a = a - common; b = b - common
        if not a and not b: return None
        return len(a & b) / len(a | b)
    def mean_within(assign_lists):
        tot = 0; n = 0
        for ids in assign_lists:
            ids = [i for i in ids if cterms[i] - common]
            if len(ids) < 2: continue
            pairs = list(itertools.combinations(ids, 2))
            if len(pairs) > 3000:
                random.seed(1); pairs = random.sample(pairs, 3000)
            vals = [jac(cterms[a], cterms[b]) for a, b in pairs]
            vals = [x for x in vals if x is not None]
            if vals:
                tot += sum(vals) / len(vals) * len(ids); n += len(ids)
        return tot / n if n else 0
    within = mean_within([[v['change_id'] for v in vs] for vs in groups.values()])
    within_sections = mean_within([[v['change_id'] for v in vs] for g, vs in groups.items()
                                   if g[0] not in ('ALL', 'OUT', 'FM') and g[1] != 'No sentence in the latest text' and g[1] != 'Not in the latest text'])
    random.seed(7)
    ids = list(out.keys()); random.shuffle(ids)
    shuffled = []; i = 0
    for vs in groups.values():
        shuffled.append(ids[i:i + len(vs)]); i += len(vs)
    baseline = mean_within(shuffled)
    # per group: the most shared distinctive term and its share
    per = []
    for g, vs in groups.items():
        tc = Counter(t for v in vs for t in sorted(cterms[v['change_id']] - common))
        most = sorted(tc.items(), key=lambda x: (-x[1], x[0]))[:1]
        per.append(dict(group=g, changes=len(vs), records=sum(len(v['members']) for v in vs),
                        shared_term=most[0][0] if most else '', shared_term_share=round(most[0][1] / len(vs), 2) if most else 0,
                        no_sentence=sum(1 for v in vs if v['home'] is None)))
    # the section lead, tried on placed records whose new wording is not word for
    # word in the latest text: how often it names the section they are placed in
    lead_try = Counter()
    for r in recs:
        if not r['latest_sentences'] or r['new_in_latest'] == 'yes':
            continue
        truth = Counter(sec[s] for s in r['latest_sentences']).most_common(1)[0][0]
        k, score = LEAD([r], {truth[0]})
        band = 'at or above %.1f' % LEAD_MIN if score >= LEAD_MIN else 'below %.1f' % LEAD_MIN
        lead_try[band + ' n'] += 1
        lead_try[band + ' same section'] += (k == truth)
    # for changes placed by the section lead: does the anchoring step's lead
    # sentence (latest_nearest), where there is one, sit in the same section?
    agree = Counter()
    for v in out.values():
        if v['how'] and v['how'].startswith('section lead'):
            for m in v['members']:
                ln = rec_by_id[m].get('latest_nearest')
                if ln:
                    agree['with a lead sentence'] += 1
                    agree['same section'] += (sec.get(ln['sentence']) == (v.get('section') or v['group']))
                    break
    # changes touching several sections: share of their sentences in their own group
    shares = []
    for v in out.values():
        if v['also'] and v['group'][0] != 'ALL':
            ss = [s for m in v['members'] for s in rec_by_id[m]['latest_sentences']]
            gmap = SEC2GROUP if version == 'v2' else {}
            inside = sum(1 for s in ss if gmap.get(sec[s], sec[s]) == v['group'])
            shares.append(inside / len(ss))
    how = Counter(re.sub(r'\d+(\.\d+)?', 'N', v['how']) for v in out.values())
    return dict(version=version, groups=len(groups),
                lead_try=dict(lead_try), lead_agreement=dict(agree),
                multi_section_changes_placed_by_majority=len(shares),
                multi_section_mean_share_inside=round(sum(shares) / len(shares), 3) if shares else None,
                multi_section_all_inside_after_merge=sum(1 for x in shares if x == 1.0),
                placement=dict(how), sizes_changes=sizes_c, sizes_records=sizes_r,
                singletons=sum(1 for s in sizes_c if s == 1), over_40=sum(1 for s in sizes_c if s > 40),
                records_multi_section=multi_rec, changes_multi_section=multi_change,
                records_no_sentence=none_rec,
                changes_no_sentence=sum(1 for v in out.values() if v['home'] is None),
                term_jaccard_within=round(within, 3), term_jaccard_within_sections=round(within_sections, 3), term_jaccard_random=round(baseline, 3),
                common_terms=sorted(common), per_group=per)

if __name__ == '__main__':
    out, sec, sord = assign(VERSION)
    m = measure(out, sec, sord, VERSION)
    brief = {k: v for k, v in m.items() if k not in ('per_group',)}
    print(json.dumps(brief, ensure_ascii=False))
    gorder = {k: i for i, k in enumerate(sord)}
    def gkey(p):
        g = p['group']
        pk = g[0]
        pi = list(PART_NAME).index(pk) if pk in PART_NAME else (98 if pk == 'ALL' else 99)
        return (pi, gorder.get(g, 999))
    for p in sorted(m['per_group'], key=gkey):
        print('%-4s %-62s c=%-3d r=%-3d nosent=%-3d term=%s (%.2f)' % (p['group'][0], p['group'][1][:62], p['changes'], p['records'], p['no_sentence'], p['shared_term'], p['shared_term_share']))
    if VERSION == 'v2':
        with open(os.path.join(HERE, 'assignment.jsonl'), 'w', encoding='utf-8') as f:
            for v in out.values():
                d = dict(v); d['group'] = list(v['group']); d['also'] = [list(a) for a in v['also']]
                f.write(json.dumps(d, ensure_ascii=False) + '\n')
        lines = defaultdict(list)
        for u in units:
            lines[sec[u['id']]].append((u['line'], u['line_end']))
        with open(os.path.join(HERE, 'sections.json'), 'w', encoding='utf-8') as f:
            json.dump([dict(section=list(k), group=list(SEC2GROUP.get(k, k)),
                            first_line=min(a for a, b in lines[k]), last_line=max(b for a, b in lines[k]),
                            units=len(lines[k])) for k in sord], f, ensure_ascii=False, indent=1)
        # each v2 adjustment left out in turn, to see what it does to the measures
        import copy
        base = copy.deepcopy(ADJUST)
        ablation = []
        for label, kw in [('v2 as made', {}), ('without the grievance split', dict(split_by_label_under_heading=[])),
                          ('without the own sections', dict(own_section_lines={})),
                          ('without the vocabulary group', dict(term_wide_parts=99)),
                          ('without named section and lead', dict(use_named_section=False, use_lead=False)),
                          ('without joining small sections', dict(min_changes=0))]:
            ADJUST.clear(); ADJUST.update(copy.deepcopy(base)); ADJUST.update(kw)
            mm = measure(*assign('v2'), 'v2')
            ss = mm['sizes_changes']
            ablation.append(dict(label=label, groups=mm['groups'], within=mm['term_jaccard_within'],
                                 within_sections=mm['term_jaccard_within_sections'],
                                 small=sum(1 for x in ss if x <= 3), largest=max(ss)))
        ADJUST.clear(); ADJUST.update(base)
        with open(os.path.join(HERE, 'measures.json'), 'w', encoding='utf-8') as f:
            json.dump(dict(v2=m, v1=measure(*assign('v1'), 'v1'), ablation=ablation), f, ensure_ascii=False, indent=1, default=list)
