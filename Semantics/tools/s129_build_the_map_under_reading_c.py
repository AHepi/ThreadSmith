#!/usr/bin/env python3
"""s129_build_the_map_under_reading_c.py

What it does, in plain words: for log S129 (decisions S83 and S84). Recomputes S117's map of how the Avida work lines up
with the semantics, now that the owner has decided the two points S117 and S127 left open, and writes a corrected map
data file BESIDE S117's (S117's files are read, never written):
  results/S117 The Avida work against the semantics - relationship map, under Reading C.json
The units whose verdict S117 marked as turning on a reading are moved only where the model's own verdicts, computed by
tools/s129_feed_avida_cases_to_the_copy_under_reading_c.py on the S129 copy of the model, say they move (each move names
the computed value it rests on). The counts are recomputed for four settings: S117 as published; Reading C alone (S83);
the graded survival condition alone (S84); both (the map file carries both); and, for comparison only, Reading C at a
boundary that takes in Avida's authors (B's verdicts). They are checked against S127's hand count and S117's.

  python3 -B Semantics/tools/s129_build_the_map_under_reading_c.py

Written 2 October 2026 by the one Opus 5.5 agent of log S129.
"""
import copy, json, os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, 'results')
S117_RESULTS = os.path.join(RES, 'S117 The Avida work against the semantics - results.json')
S117_MAP = os.path.join(RES, 'S117 The Avida work against the semantics - relationship map.json')
FEED = os.path.join(RES, 'S129 Reading C carried into copies', 'map feeding under Reading C.json')
OUT = os.path.join(RES, 'S117 The Avida work against the semantics - relationship map, under Reading C.json')
EXACT, PART, NOT, NONE = 'LINES UP EXACTLY', 'LINES UP IN PART', 'DOES NOT LINE UP', 'NOTHING IN AVIDA'
VERDICTS = [EXACT, PART, NOT, NONE]
PLAIN = {EXACT: 'lines up exactly', PART: 'lines up in part', NOT: 'does not line up', NONE: 'nothing in Avida'}
MC1 = 'MC1 (graded-pay run: doing NOT raised the rate of copying)'
MC1B = 'MC1b (the run that paid for nothing: doing NOT changed nothing)'
ROW_A, ROW_B = 'A (S117)', 'B (S117)'
ROW_72, ROW_WIDE = 'C at the S72 boundary', 'C at a wide boundary'

# What matches, in plain words, for each unit that moves to EXACT (S129's sentences; S117's wording kept where it holds)
MATCH = {
    'D12.1': 'Avida has the population, the variation and the history the semantics asks for; doing the task raises a '
             'program\'s rate of copying, which is the survival condition as the owner has read it (S84: being copied more '
             'counts as surviving); and inside the boundary of the whole execution environment (S72) the task-checking code, '
             'written outside it, stands for nothing (S83, Reading C). So a program\'s correspondence with its task is '
             'selected; in the run that paid for nothing it is not, since doing NOT changed nothing about copying there.',
    'D12.3': 'Avida\'s task list and checking code are declared in the semantics\' sense: inside the execution environment their '
             'correspondence with the task arrived whole from the people who wrote them, so they stand for nothing there; the '
             'programs\' own correspondences are selected, not declared (S83, Reading C).',
    'D12.5': 'An Avida program that does a task stands for that task on the numbers the world hands in: its correspondence is '
             'faithful there and selected inside the execution environment\'s boundary (S83); on a wider set of changes, '
             'programs tied to the world\'s order fail.',
    'D11.4': 'The routes read from Avida\'s step-by-step record are active routes in the semantics\' sense: paths through '
             'executed instructions from a represented input (the program\'s selected correspondence takes in the numbers '
             'handed in) to the number handed out (S83).',
    'T10': 'An evolved circuit is exactly the kind of inexplicit representation the text means: nothing in it is stated, and '
           'inside the execution environment\'s boundary it stands for its task (S83).',
    'D16.XV': 'Taken as one block, the NOT program meets every condition of the test of an explanation on the numbers the world '
              'hands in, and its correspondence is selected inside the execution environment\'s boundary, so the semantics '
              'calls it an explanation of NOT in its narrow sense, never a created one; cut into its instructions it fails. An '
              'assessor who holds, by an argument not using the test, that it is no explanation holds an argument against '
              '(Suff) at that boundary; at a boundary that takes in Avida\'s authors it is declared and, by S41, no explanation.',
}
MATCH['FC75'] = MATCH['D11.4']
MATCH['FC30.new1'] = MATCH['D16.XV']
WHY_WIDE = {
    'D12.1': 'At a boundary that takes in the people who wrote Avida, the task-checking code is a record of their '
             'representation of the task, earlier than the program\'s holding, so selection\'s condition fails (B\'s verdict).',
    'D12.5': 'At a boundary that takes in Avida\'s authors the program\'s correspondence is declared, so it stands for nothing.',
    'D11.4': 'At a boundary that takes in Avida\'s authors nothing in the program stands for its input, so no route is active.',
    'T10': 'At a boundary that takes in Avida\'s authors the circuit stands for nothing, explicitly or not.',
    'FC80': 'The underdetermination is computed (16 of 18 populations), but Argument 3 is about a selected correspondence, '
            'which these programs are not at a boundary that takes in Avida\'s authors.',
}
WHY_WIDE['FC75'] = WHY_WIDE['D11.4']
HINGE = ['D11.4', 'D12.1', 'D12.3', 'D12.5', 'D16.XV', 'FC30.new1', 'FC75', 'T10']


def g(feed, setting, case, row):
    rows = feed['settings'][setting][case]['provenance and (Suff)']
    return next(v for k, v in rows.items() if k.startswith(row))


def moves(feed, setting, boundary='S72'):
    """The units that move under one setting of the copy's switches, each with the computed values it rests on."""
    if setting is None:
        return {}
    a, b = g(feed, setting, MC1, ROW_A), g(feed, setting, MC1, ROW_B)
    c = g(feed, setting, MC1, ROW_72 if boundary == 'S72' else ROW_WIDE)
    cb_ = g(feed, setting, MC1B, ROW_72 if boundary == 'S72' else ROW_WIDE)
    block = feed['settings'][setting][MC1]['(E) of the program as one block']
    c_on = setting.startswith('C on')
    graded = setting.endswith('graded on')
    out = {}
    if not c_on:
        return out                        # S117's A and B still differ: the hinge is open, nothing moves
    ev = ('S129, the copy of the model, MC1 at the %s boundary (setting "%s"): Sel %s, Con %s, Dec %s; the task-check code '
          'stands for the task there: %s; the program as one block meets (E): %s; in the run that paid for nothing (MC1b): Sel %s'
          % ('S72' if boundary == 'S72' else 'wide', setting, c['Sel'], c['Con'], c['Dec'],
             c['the task-check code represents (survival condition, task) at this boundary'], block, cb_['Sel']))
    rep = c['Rep: the program stands for NOT (faithful on the task and Sel or Con)']
    if boundary == 'S72' and c['Sel'] and not c['Dec'] and not c['the task-check code represents (survival condition, task) at this boundary']:
        out['D12.3'] = (EXACT, ev)
        if rep:
            for u in ('D12.5', 'T10', 'D11.4', 'FC75'):
                out[u] = (EXACT, ev)
        if block and not c['Dec']:
            for u in ('D16.XV', 'FC30.new1'):
                out[u] = (EXACT, ev)
        if graded and not cb_['Sel']:
            out['D12.1'] = (EXACT, ev)    # selected where doing NOT raised copying, not where it changed nothing
    if boundary == 'wide' and c['Dec'] and not c['Sel'] and c['the task-check code represents (survival condition, task) at this boundary']:
        out['D12.3'] = (EXACT, ev)
        if block:
            for u in ('D16.XV', 'FC30.new1'):
                out[u] = (EXACT, ev)
        if not rep:
            for u in ('D12.1', 'D12.5', 'D11.4', 'FC75', 'T10'):
                out[u] = (NOT, ev)
            out['FC80'] = (PART, ev)
    return out


def count(units, mv):
    return Counter(mv.get(u['id'], (u['verdict'],))[0] for u in units)


def main():
    res = json.load(open(S117_RESULTS, encoding='utf-8'))
    mp = json.load(open(S117_MAP, encoding='utf-8'))
    feed = json.load(open(FEED, encoding='utf-8'))
    units = res['units']
    scen = [('S117 as published (the hinge and the survival condition open)', None, 'S72'),
            ('Reading C alone (S83), the S72 boundary', 'C on, graded off', 'S72'),
            ('the graded survival condition alone (S84), the hinge left open', 'C off, graded on', 'S72'),
            ('both (S83 and S84), the S72 boundary: this map', 'C on, graded on', 'S72'),
            ('for comparison: both, at a boundary that takes in Avida\'s authors (B\'s verdicts)', 'C on, graded on', 'wide')]
    counts, moved = {}, {}
    for lab, setting, bnd in scen:
        mv = moves(feed, setting, bnd)
        c = count(units, mv)
        counts[lab] = {v: c[v] for v in VERDICTS}
        moved[lab] = {u: {'from': next(x['verdict'] for x in units if x['id'] == u), 'to': v, 'computed': e} for u, (v, e) in sorted(mv.items())}
    s127 = {'Reading C alone (S83), the S72 boundary': (121, 29, 18, 116),
            'both (S83 and S84), the S72 boundary: this map': (122, 28, 18, 116),
            'S117 as published (the hinge and the survival condition open)': (114, 36, 18, 116),
            'for comparison: both, at a boundary that takes in Avida\'s authors (B\'s verdicts)': (116, 29, 23, 116)}
    check = {k: {'by program': tuple(counts[k][v] for v in VERDICTS), 'S127 by hand (S117 for the first)': s127[k],
                 'agree': tuple(counts[k][v] for v in VERDICTS) == s127[k]} for k in s127}

    # ---- the map with both decisions -------------------------------------------------------------------------------
    final = moves(feed, 'C on, graded on', 'S72')
    m = copy.deepcopy(mp)
    vby = {u['id']: final.get(u['id'], (u['verdict'],))[0] for u in units}
    for r in m['relations']:
        us = r['units']
        vs = set(vby[u] for u in us)
        assert len(vs) == 1, (r['id'], vs)
        v = vs.pop()
        if v != r['verdict']:
            r['verdict_in_S117'] = r['verdict']
            r['verdict'], r['plain_verdict'] = v, PLAIN[v]
            r['why_in_S117'] = r['why']
            r['why'] = '' if v == EXACT else r['why']
            r['what_matches'] = MATCH[us[0]] if v == EXACT else r['what_matches']
            r['technical']['evidence'] = r['technical']['evidence'] + ' S129: ' + final[us[0]][1] + '.'
        if r['turns_on_a_reading']:
            r['turns_on_a_reading'] = False
            r['decided_by'] = 'S83 (Reading C, the S72 boundary)' + (' and S84 (being copied more counts as surviving)' if 'D12.1' in us else '')
    lines = defaultdict(list)
    for r in m['relations']:
        lines[(r['from_group'], r['to'], r['verdict'])].append(r)
    m['lines'] = [{'from_group': a, 'to': b, 'verdict': v, 'units': sum(len(r['units']) for r in rs), 'relations': [r['id'] for r in rs]}
                  for (a, b, v), rs in lines.items()]
    by_group = defaultdict(Counter)
    for u in units:
        by_group[u['group']][vby[u['id']]] += 1
    for gr in m['groups']:
        c = by_group[gr['id']]
        gr['counts_in_S117'] = gr['counts']
        gr['counts'] = {v: c[v] for v in VERDICTS}
        gr['most_units'] = max(VERDICTS, key=lambda v: (c[v], -VERDICTS.index(v)))
    m['counts_by_verdict_in_S117'] = m['counts_by_verdict']
    m['counts_by_verdict'] = counts['both (S83 and S84), the S72 boundary: this map']
    m['counts_by_scenario'] = counts
    m['checked_against_the_hand_counts'] = check
    m['units_moved'] = moved
    m['readings_in_S117'] = m.pop('readings')
    m['decisions'] = {
        'S83': 'Reading C ("Oh clearly C."): the history in the definition of a selected correspondence (D12.1) is read inside the '
               'system boundary declared for the claim. With the owner\'s boundary (S72: the whole Avida execution environment is '
               'the selector), the task-checking code, written by people outside that boundary, stands for nothing inside it, so an '
               'evolved program\'s correspondence with its task can be selected; at a boundary that takes in Avida\'s authors it is '
               'declared (B\'s verdict). Written into copies only: tests/129, and results/S129 Reading C carried into copies/.',
        'S84': 'Being copied more often counts as surviving ("Well yes. That is how selected is defined."): D12.1\'s survival '
               'condition asks that fidelity on the history changes which members persist or are copied. Written into the same copies.'}
    for b in m['main_breaks']:
        if b['id'] == 'B1':
            b['under_S83_and_S84'] = ('Decided by S83. At the S72 boundary the NOT program\'s correspondence is selected, stands for '
                                      'NOT, and, as one block, is an explanation of NOT in the semantics\' narrow sense, never a '
                                      'created one; at a boundary that takes in Avida\'s authors it is declared and no explanation. '
                                      'Computed: MC1 in results/S129 Reading C carried into copies/map feeding under Reading C.json.')
        if b['id'] == 'B4':
            b['under_S83_and_S84'] = ('Decided by S84. A graded advantage counts: where doing the task raised a program\'s rate of '
                                      'copying, the program survived on its history; in the run that paid for nothing, doing NOT '
                                      'changed nothing, and the 11 programs doing NOT there are not selected for NOT (MC1b: Sel '
                                      'false with the graded condition, true without it). The break stays as a fact about Avida '
                                      '(lasting does not require the task) and no longer stops the semantics\' definition applying.')
    m['about'] = ('S129 corrected relationship map (decisions S83 and S84), written beside S117\'s map, which is unchanged. It is S117\'s map '
                  'with the eight units S117 marked as turning on a reading moved where the S129 copy of the model says they move '
                  '(each moved relation keeps its S117 verdict and wording under verdict_in_S117 and why_in_S117, and names the '
                  'computed values it rests on); counts by group and lines recomputed; counts for Reading C alone, the graded '
                  'condition alone, both, and B\'s boundary for comparison, under counts_by_scenario, checked against S127\'s hand '
                  'count. The theory itself is unchanged: the decisions are carried in copies only. Built by '
                  'tools/s129_build_the_map_under_reading_c.py from ' + os.path.relpath(S117_RESULTS, ROOT) + ', ' +
                  os.path.relpath(S117_MAP, ROOT) + ' and ' + os.path.relpath(FEED, ROOT) + '.')
    json.dump(m, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    for k, v in counts.items():
        print('%-95s %s' % (k, ' / '.join(str(v[x]) for x in VERDICTS)))
    print('checked:', json.dumps(check, ensure_ascii=False))
    for k, v in moved.items():
        print(k, {u: '%s -> %s' % (x['from'][:12], x['to'][:12]) for u, x in v.items()})


if __name__ == '__main__':
    main()
