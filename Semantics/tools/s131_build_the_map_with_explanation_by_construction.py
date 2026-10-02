#!/usr/bin/env python3
"""s131_build_the_map_with_explanation_by_construction.py

What it does, in plain words: for log S131 (decision S86, explanation kept for what was worked out). Recounts S117's
map of how the Avida work lines up with the semantics under the owner's three decisions (S83 Reading C, S84 the graded
survival condition, S86 explanation by construction), by program, from the values the S131 copy of the model computes
for S117's Avida cases (tools/s131_feed_avida_cases_to_the_copy_with_explanation_by_construction.py), and writes the
map BESIDE S117's and S129's (both read, never written):
  results/S117 The Avida work against the semantics - relationship map, under Reading C and explanation by construction.json
How units move:
  - every unit S129 moved, by S129's own rule (tools/s129_build_the_map_under_reading_c.py, whose function "moves" is
    loaded unchanged and fed the S131 values for the same S129 setting), except the two units of the defeat conditions
    (D16.XV and FC30.new1) when S86 is on;
  - with S86 on, D16.XV and FC30.new1 move to LINES UP EXACTLY when the NOT program taken whole meets the test (E) and,
    under every reading in force (S117's A and B when Reading C is off; the declared boundary when it is on), the
    semantics gives the same verdict on whether it is an explanation; S117 had them LINES UP IN PART only because A and
    B gave opposite verdicts (an explanation, against the owner's reading of Avida; declared, with it).
Counts for: S117 as published; S129's four settings (S86 off); the four with S86 on; and, for comparison, all three
decisions at a boundary that takes in Avida's authors. Checked against S117's and S129's counts and S130's hand move.

  python3 -B Semantics/tools/s131_build_the_map_with_explanation_by_construction.py

Written 2 October 2026 by the one Opus 5.5 agent of log S131.
"""
import copy, json, os
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RES = os.path.join(ROOT, 'results')
S129_BUILDER = os.path.join(ROOT, 'tools', 's129_build_the_map_under_reading_c.py')
S117_RESULTS = os.path.join(RES, 'S117 The Avida work against the semantics - results.json')
S129_MAP = os.path.join(RES, 'S117 The Avida work against the semantics - relationship map, under Reading C.json')
FEED = os.path.join(RES, 'S131 Explanation by construction carried into copies', 'map feeding with explanation by construction.json')
OUT = os.path.join(RES, 'S117 The Avida work against the semantics - relationship map, under Reading C and explanation by construction.json')

S129 = {'__name__': 's129_builder', '__file__': S129_BUILDER}
exec(compile(open(S129_BUILDER, encoding='utf-8').read(), S129_BUILDER, 'exec'), S129)
EXACT, PART, NOT, NONE, VERDICTS, PLAIN = (S129[k] for k in ('EXACT', 'PART', 'NOT', 'NONE', 'VERDICTS', 'PLAIN'))
MC1, ROW_A, ROW_B, ROW_72, ROW_WIDE = (S129[k] for k in ('MC1', 'ROW_A', 'ROW_B', 'ROW_72', 'ROW_WIDE'))
OWNER = "the owner's condition rules out Expl (S86 on: Acc and not Con; off: Acc and Dec)"
SUFF = "(Suff) conjectures Expl (S86 on: Acc and Con; off: Acc and not Dec)"
SUFF_UNITS = ('D16.XV', 'FC30.new1')

MATCH_S86 = ('Taken as one block, the NOT program meets every condition of the test of an account on the question S117 declared '
             'for it (one input bit, two input pairs, no admitted change, its contract equal to its selection history), and its '
             'correspondence was selected inside the execution environment\'s boundary, not worked out. Under the owner\'s third '
             'decision (S86: explanation is kept for what was worked out) the semantics therefore says it is no explanation: an '
             'account whose transport was not constructed is none (the owner\'s condition, Acc and not Con implies not Expl). It '
             'stands for NOT there, a representation: what the owner calls evolved knowledge. This is the owner\'s reading of '
             'Avida (knowledge without the explanation kind). Cut into its instructions it fails the test. At a boundary that takes '
             'in Avida\'s authors it is declared, and no explanation either.')
WHY_T01_S86 = ('The conjecture is about explanatory creativity, and nothing in Avida creates an explanation. Under the owner\'s third '
               'decision (S86) nothing in Avida is an explanation at all, since nothing in an Avida program\'s history works anything '
               'out: the NOT program, which meets the test of an account, is evolved knowledge and no counterexample to the '
               'conjecture, which now names accounts whose transport was constructed.')


def view(feed, s86):
    """S129's setting names over the S131 values with S86 on or off, so that S129's rule reads them unchanged."""
    tag = ', S86 on' if s86 else ', S86 off'
    return {'settings': {k[:-len(tag)]: v for k, v in feed['settings'].items() if k.endswith(tag)}}


def moves(feed, setting, s86, boundary='S72'):
    if setting is None:
        return {}
    fv = view(feed, s86)
    mv = dict(S129['moves'](fv, setting, boundary))
    if not s86:
        return mv
    for u in SUFF_UNITS:
        mv.pop(u, None)
    rows = feed['settings'][setting + ', S86 on'][MC1]['provenance and (Suff)']
    get = lambda pre: next(v for k, v in rows.items() if k.startswith(pre))
    if setting.startswith('C on'):
        in_force = [(ROW_72 if boundary == 'S72' else ROW_WIDE, get(ROW_72 if boundary == 'S72' else ROW_WIDE))]
    else:
        in_force = [(ROW_A, get(ROW_A)), (ROW_B, get(ROW_B))]
    block = feed['settings'][setting + ', S86 on'][MC1]['(E) of the program as one block']
    verdicts = set((r[OWNER], r[SUFF]) for _, r in in_force)
    if block and len(verdicts) == 1:
        owner_rules_out, suff_says = verdicts.pop()
        ev = ('S131, the copy of the model with S86 on, MC1 taken whole (setting "%s, S86 on"; %s): the program meets (E): %s; %s' % (
            setting, 'the %s boundary' % boundary if setting.startswith('C on') else "S117's readings A and B, no boundary declared", block,
            '; '.join('%s: Sel %s, Con %s, Dec %s, the owner\'s condition rules out Expl %s, (Suff) conjectures Expl %s'
                      % (n.split(':')[0], r['Sel'], r['Con'], r['Dec'], r[OWNER], r[SUFF]) for n, r in in_force)))
        if owner_rules_out and not suff_says:
            for u in SUFF_UNITS:
                mv[u] = (EXACT, ev)
    return mv


def count(units, mv):
    return Counter(mv.get(u['id'], (u['verdict'],))[0] for u in units)


def main():
    res = json.load(open(S117_RESULTS, encoding='utf-8'))
    m129 = json.load(open(S129_MAP, encoding='utf-8'))
    feed = json.load(open(FEED, encoding='utf-8'))
    units = res['units']
    scen = [('S117 as published (the hinge and the survival condition open)', None, False, 'S72'),
            ('S129: Reading C alone (S83), the S72 boundary', 'C on, graded off', False, 'S72'),
            ('S129: the graded survival condition alone (S84), the hinge left open', 'C off, graded on', False, 'S72'),
            ('S129: both (S83 and S84), the S72 boundary', 'C on, graded on', False, 'S72'),
            ('S131: explanation by construction alone (S86), the hinge left open', 'C off, graded off', True, 'S72'),
            ('S131: Reading C and S86, the S72 boundary', 'C on, graded off', True, 'S72'),
            ('S131: the graded condition and S86, the hinge left open', 'C off, graded on', True, 'S72'),
            ('S131: all three (S83, S84, S86), the S72 boundary: this map', 'C on, graded on', True, 'S72'),
            ('for comparison: all three, at a boundary that takes in Avida\'s authors', 'C on, graded on', True, 'wide'),
            ('for comparison: S129 both, at a boundary that takes in Avida\'s authors', 'C on, graded on', False, 'wide')]
    counts, moved = {}, {}
    for lab, setting, s86, bnd in scen:
        mv = moves(feed, setting, s86, bnd)
        c = count(units, mv)
        counts[lab] = {v: c[v] for v in VERDICTS}
        moved[lab] = {u: {'from': next(x['verdict'] for x in units if x['id'] == u), 'to': v, 'computed': e} for u, (v, e) in sorted(mv.items())}
    known = {'S117 as published (the hinge and the survival condition open)': ((114, 36, 18, 116), 'S117'),
             'S129: Reading C alone (S83), the S72 boundary': ((121, 29, 18, 116), 'S129 by program, S127 by hand'),
             'S129: the graded survival condition alone (S84), the hinge left open': ((114, 36, 18, 116), 'S129 by program'),
             'S129: both (S83 and S84), the S72 boundary': ((122, 28, 18, 116), 'S129 by program, S127 by hand'),
             'S131: all three (S83, S84, S86), the S72 boundary: this map': ((122, 28, 18, 116), 'S130 section 4.3, by hand: "the counts 122 / 28 / 18 / 116 unchanged"'),
             'for comparison: S129 both, at a boundary that takes in Avida\'s authors': ((116, 29, 23, 116), 'S129 by program, S127 by hand (B)')}
    check = {k: {'by program': tuple(counts[k][v] for v in VERDICTS), 'earlier count': n, 'from': who,
                 'agree': tuple(counts[k][v] for v in VERDICTS) == n} for k, (n, who) in known.items()}
    # which units move between S129 both and each S86 setting, and why
    base = moves(feed, 'C on, graded on', False, 'S72')
    diffs = {}
    for lab, setting, s86, bnd in scen:
        if not s86:
            continue
        mv = moves(feed, setting, s86, bnd)
        diffs[lab] = {'against S117 as published': sorted(mv), 'against S129 both': sorted(u for u in set(mv) | set(base) if mv.get(u, (None,))[0] != base.get(u, (None,))[0])}

    # ---- the map with all three decisions, at the S72 boundary --------------------------------------------------------
    final = moves(feed, 'C on, graded on', True, 'S72')
    assert {u: v for u, (v, _) in final.items()} == {u: v for u, (v, _) in base.items()}, 'a verdict moved between S129 both and all three'
    m = copy.deepcopy(m129)
    for r in m['relations']:
        if r['id'] == 'R117':
            assert set(r['units']) == set(SUFF_UNITS)
            r['what_matches_in_S129'] = r['what_matches']
            r['what_matches'] = MATCH_S86
            r['technical']['evidence'] = r['technical']['evidence'] + ' S131: ' + final['D16.XV'][1] + '.'
            r['decided_by'] = r.get('decided_by', '') + ' and S86 (explanation kept for what was worked out)'
            r['wording_moved_by_S86'] = True
        if r['id'] == 'R003':
            assert r['units'] == ['T01']
            r['why_in_S129'] = r['why']
            r['why'] = WHY_T01_S86
            r['wording_moved_by_S86'] = True
    m['counts_by_verdict_in_S129'] = m['counts_by_verdict']
    m['counts_by_verdict'] = counts['S131: all three (S83, S84, S86), the S72 boundary: this map']
    m['counts_by_scenario_in_S129'] = m.pop('counts_by_scenario')
    m['counts_by_scenario'] = counts
    m['checked_against_the_hand_counts_in_S129'] = m.pop('checked_against_the_hand_counts')
    m['checked_against_earlier_counts'] = check
    m['units_moved_in_S129'] = m.pop('units_moved')
    m['units_moved'] = moved
    m['units_that_move_with_S86'] = diffs
    m['decisions']['S86'] = ('Explanation is kept for what was worked out ("Correct. Knowledge doesn\'t need to be worked out, explanation '
                             'does."): an account whose transport was selected is a representation, the owner\'s knowledge, and not an '
                             'explanation; one whose transport was declared is no explanation either (S41). Written into copies only: '
                             'tests/131, and results/S131 Explanation by construction carried into copies/.')
    for b in m['main_breaks']:
        if b['id'] == 'B1':
            b['under_S86'] = ('With S86, the NOT program taken whole is evolved knowledge of NOT at the S72 boundary (selected, faithful '
                              'on its two input pairs) and no explanation; at a boundary that takes in Avida\'s authors it is declared and '
                              'no explanation. The semantics now agrees with the owner\'s reading of Avida at every boundary, and needs '
                              'no reading of the hinge to do so: with S86 alone, S117\'s readings A and B both give "no explanation". '
                              'Computed: MC1 in results/S131 Explanation by construction carried into copies/map feeding with '
                              'explanation by construction.json.')
    m['about'] = ('S131 relationship map (decisions S83, S84 and S86), written beside S117\'s map and S129\'s, which are unchanged. It is '
                  'S129\'s map (S117\'s with the units S117 marked as turning on a reading moved where the model says they move) with the '
                  'third decision carried in: no unit\'s verdict moves between S129\'s map and this one at the S72 boundary; the '
                  'wording of R117 (D16.XV, FC30.new1) and R003 (T01) moves, each keeping S129\'s wording under what_matches_in_S129 '
                  'or why_in_S129. Counts for S117, S129\'s four settings, the four settings with S86, and two wide-boundary '
                  'comparisons under counts_by_scenario, checked against S117, S129 and S130 (checked_against_earlier_counts); '
                  'units_that_move_with_S86 lists, for each S86 setting, the units that move against S117 and against S129 both. '
                  'The theory itself is unchanged: the decisions are carried in copies only. Built by '
                  'tools/s131_build_the_map_with_explanation_by_construction.py from ' + os.path.relpath(S117_RESULTS, ROOT) + ', ' +
                  os.path.relpath(S129_MAP, ROOT) + ' and ' + os.path.relpath(FEED, ROOT) + '.')
    json.dump(m, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    for k, v in counts.items():
        print('%-80s %s' % (k, ' / '.join(str(v[x]) for x in VERDICTS)))
    print('checked:', json.dumps({k: v['agree'] for k, v in check.items()}, ensure_ascii=False))
    for k, v in diffs.items():
        print(k, json.dumps(v, ensure_ascii=False))


if __name__ == '__main__':
    main()
