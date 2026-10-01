#!/usr/bin/env python3
"""s117_build_the_results_and_the_map.py

What it does, in plain words: for log S117, puts the line-up together. It reads the list of the semantics' units
(made by s117_list_the_units_of_the_semantics.py), the hand-written line-up (s117_the_line_up_unit_by_unit.py) and the
outputs of the four computations in the scratch space (C1 circuit_A.json, C2 alike_separated.json, C3 orders/summary.json,
C4 model_cases.json), and writes three files into the repository:
  results/S117 The Avida work against the semantics - results.json   every unit with its verdict, counterpart, evidence
  results/S117 The Avida work against the semantics - relationship map.json   groups, Avida things, relations, lines
  the per-unit tables and counts of results/S117 The Avida work against the semantics - results.md (the prose of that
  file is written by hand in the file itself, between markers this script leaves alone)
It changes nothing in the semantics.

  python3 -B Semantics/tools/s117_build_the_results_and_the_map.py

Written 1 October 2026 by the one Opus 5.5 agent of log S117.
"""
import importlib.util, json, os, re, subprocess
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s117'
RES = os.path.join(ROOT, 'results')
BASE = 'S117 The Avida work against the semantics - '


def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    subprocess.run(['python3', '-B', os.path.join(HERE, 's117_list_the_units_of_the_semantics.py')], check=True,
                   stdout=subprocess.DEVNULL)
    L = load('s117_the_line_up_unit_by_unit')
    units = json.load(open(SC + '/units.json', encoding='utf-8'))
    comp = {
        'C1 circuit as an explanation on ablations': json.load(open(SC + '/circuit_A.json')),
        'C2 alike programs separated by a finer change': json.load(open(SC + '/alike_separated.json')),
        'C3 unseen input orders': json.load(open(SC + '/orders/summary.json')),
        'C4 Avida-derived cases in a copy of the model': json.load(open(SC + '/model_cases.json')),
    }
    gname = {g: n for g, n, d in L.GROUPS}
    aname = {a: n for a, n, d in L.AVIDA}
    out_units = []
    for u in units:
        g, key, note = L.U[u['id']]
        p = L.P[key]
        plain = p['why'] if p['verdict'] != L.EXACT else L.MATCH[key]
        out_units.append({
            'id': u['id'], 'kind': u['kind'], 'name': u['name'], 'group': g, 'group_name': gname[g],
            'verdict': p['verdict'], 'avida_counterpart': p['avida'], 'avida_counterpart_name': aname[p['avida']],
            'plain': plain, 'example': L.EXAMPLE.get(key, ''), 'evidence': p['evidence'], 'note': note,
            'alternatives_considered': p['alternatives'], 'turns_on_a_reading': p['turns_on_a_reading'],
            'also_lines_up_with_the_people_studying_avida': p['also_lines_up_with_the_people_studying_avida'],
            'profile': key, 'formal_core_line': u.get('core_line'), 'text_lines': u.get('text_lines', []),
            'claims_md_line': u.get('claims_md_line'), 'status_after_round_4': u.get('status_after_round_4'),
        })
    by_v = Counter(x['verdict'] for x in out_units)
    by_kind = defaultdict(Counter)
    by_group = defaultdict(Counter)
    for x in out_units:
        by_kind[x['kind']][x['verdict']] += 1
        by_group[x['group']][x['verdict']] += 1
    def basis(x):
        if x['verdict'] == L.EXACT:
            if x['profile'] == 'kinds_math':
                return 'exact: holds by proof of the definition'
            return 'exact: computed' if 'Computed' in x['evidence'] else 'exact: argued from the Avida records'
        if x['verdict'] == L.NONE:
            if x['profile'] == 'text_only':
                return 'nothing: the unit is about the text\'s own wording'
            if x['group'] == 'G15':
                return 'nothing: one of the text\'s worked examples'
            return 'nothing: no Avida counterpart for something the semantics needs'
        return x['verdict'].lower()
    for x in out_units:
        x['basis'] = basis(x)
    by_basis = Counter(x['basis'] for x in out_units)
    reading = [x['id'] for x in out_units if x['turns_on_a_reading']]
    people = [x['id'] for x in out_units if x['also_lines_up_with_the_people_studying_avida']]
    explanatory = [g for g in ('G05', 'G06', 'G07', 'G08', 'G09', 'G10', 'G11', 'G12')]
    expl_counts = Counter(x['verdict'] for x in out_units if x['group'] in explanatory)

    results = {
        'about': 'S117: the Avida work (S111 to S116) lined up against the semantics after round 4, unit by unit. '
                 'Written 1 October 2026 by the one Opus 5.5 agent of log S117 (S69, S70); no GLM check (S70). '
                 'Method: results/' + BASE + 'how it will be lined up, written before mapping.md. Nothing in the semantics was changed.',
        'units_count': len(out_units),
        'counts_by_verdict': {v: by_v[v] for v in L.VERDICTS},
        'counts_by_kind': {k: {v: c[v] for v in L.VERDICTS} for k, c in by_kind.items()},
        'counts_by_group': {g: {'name': gname[g], **{v: by_group[g][v] for v in L.VERDICTS}} for g, _, _ in L.GROUPS},
        'counts_in_the_groups_about_explanation_G05_to_G12': {v: expl_counts[v] for v in L.VERDICTS},
        'counts_by_basis': dict(sorted(by_basis.items())),
        'units_whose_verdict_turns_on_a_reading': reading,
        'units_that_also_line_up_with_the_people_studying_avida': people,
        'readings': {
            'A': 'The code in Avida that checks a task is not an occurrence, in the history that selected a program, that represents the survival condition or the task (it belongs to the world\'s rules).',
            'B': 'That code is such an occurrence: it was written by people and computes the task, so it represents the task and the survival condition, earlier than the program that holds the correspondence.',
            'where_the_text_leaves_it_open': 'D12.1 (formal core line 454): "No member of the history represents t, H, or the survival condition"; the formal core marks the reading of "member of the history" as occurrences as invented (I52) and h(t) as "the history that produced that holding, its preparing episode included" (I167). Whether Avida\'s task-checking code is in h(t) is not settled by the text, nor here.',
        },
        'main_breaks': L.BREAKS,
        'reverse_list': L.REVERSE,
        'computations': comp,
        'units': out_units,
    }
    json.dump(results, open(os.path.join(RES, BASE + 'results.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

    # ---- the relationship map --------------------------------------------------------------------------------------
    relations = []
    for g, _, _ in L.GROUPS:
        keys = []
        for x in out_units:
            if x['group'] == g and x['profile'] not in keys:
                keys.append(x['profile'])
        for k in keys:
            us = [x for x in out_units if x['group'] == g and x['profile'] == k]
            p = L.P[k]
            relations.append({
                'id': 'R%03d' % (len(relations) + 1), 'from_group': g, 'to': p['avida'], 'verdict': p['verdict'],
                'plain_verdict': L.PLAIN_VERDICT[p['verdict']],
                'why': p['why'] if p['verdict'] != L.EXACT else '',
                'what_matches': L.MATCH.get(k, '') if p['verdict'] == L.EXACT else '',
                'example': L.EXAMPLE.get(k, ''),
                'turns_on_a_reading': p['turns_on_a_reading'],
                'also_lines_up_with_the_people_studying_avida': p['also_lines_up_with_the_people_studying_avida'],
                'units': [x['id'] for x in us],
                'technical': {'units': [{'id': x['id'], 'name': x['name'], 'formal_core_line': x['formal_core_line'],
                                         'text_lines': x['text_lines'], 'claims_md_line': x['claims_md_line'],
                                         'note': x['note']} for x in us],
                              'evidence': p['evidence'], 'alternatives_considered': p['alternatives'], 'profile': k},
            })
    lines = defaultdict(list)
    for r in relations:
        lines[(r['from_group'], r['to'], r['verdict'])].append(r)
    line_list = [{'from_group': g, 'to': a, 'verdict': v, 'units': sum(len(r['units']) for r in rs),
                  'relations': [r['id'] for r in rs]} for (g, a, v), rs in lines.items()]
    groups = []
    for g, n, d in L.GROUPS:
        c = by_group[g]
        main = max(L.VERDICTS, key=lambda v: (c[v], -L.VERDICTS.index(v)))
        groups.append({'id': g, 'name': n, 'plain': d, 'units': [x['id'] for x in out_units if x['group'] == g],
                       'counts': {v: c[v] for v in L.VERDICTS}, 'most_units': main,
                       'breaks': [b['id'] for b in L.BREAKS if g in b['groups']]})
    used = {r['to'] for r in relations}
    mp = {
        'about': 'S117 relationship map (decision S70): the semantics after round 4 (fifteen groups of its 284 units) and the Avida work (S111 to S116). '
                 'Each relation joins a group to an Avida thing, or to nothing, with its verdict, a plain sentence (why it does not line up, or what matches), '
                 'a concrete example where there is one, and the technical references kept apart. Built by tools/s117_build_the_results_and_the_map.py '
                 'from results/' + BASE + 'results.json.',
        'verdicts': [{'verdict': v, 'plain': L.PLAIN_VERDICT[v], 'meaning': m} for v, m in (
            (L.EXACT, 'Something in Avida plays the same part, and every condition holds of it (or fails of it) exactly as the semantics says.'),
            (L.PART, 'Something in Avida plays the part, but only some of the conditions match, or the semantics\' own answer flips on a reading it leaves open.'),
            (L.NOT, 'Something in Avida is in the nearest place, but a condition is false of it, or it does a different job.'),
            (L.NONE, 'Nothing in Avida plays this part.'))],
        'counts_by_verdict': results['counts_by_verdict'],
        'groups': groups,
        'avida_things': [{'id': a, 'name': n, 'plain': d} for a, n, d in L.AVIDA if a in used],
        'relations': relations,
        'lines': line_list,
        'main_breaks': L.BREAKS,
        'reverse_list': L.REVERSE,
        'readings': results['readings'],
    }
    json.dump(mp, open(os.path.join(RES, BASE + 'relationship map.json'), 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

    # ---- the generated part of the results .md -------------------------------------------------------------------
    md_path = os.path.join(RES, BASE + 'results.md')
    md = open(md_path, encoding='utf-8').read()
    gen = []
    gen.append('### Counts by verdict\n')
    gen.append('| verdict | units |\n|---|---|')
    for v in L.VERDICTS:
        gen.append('| %s | %d |' % (v, by_v[v]))
    gen.append('| **all** | **%d** |\n' % len(out_units))
    gen.append('### Counts by kind of unit\n')
    gen.append('| kind | ' + ' | '.join(L.VERDICTS) + ' | all |\n|---|---|---|---|---|---|')
    for k in ('definition', 'encoding', 'formal claim', 'named term of the text'):
        c = by_kind[k]
        gen.append('| %s | %s | %d |' % (k, ' | '.join(str(c[v]) for v in L.VERDICTS), sum(c.values())))
    gen.append('\n### Counts by group\n')
    gen.append('| group | ' + ' | '.join(L.VERDICTS) + ' | all |\n|---|---|---|---|---|---|')
    for g, n, _ in L.GROUPS:
        c = by_group[g]
        gen.append('| %s %s | %s | %d |' % (g, n, ' | '.join(str(c[v]) for v in L.VERDICTS), sum(c.values())))
    gen.append('\n### Counts by what the verdict rests on\n')
    gen.append('| basis | units |\n|---|---|')
    for k, v in sorted(by_basis.items()):
        gen.append('| %s | %d |' % (k, v))
    gen.append('\nIn the groups about explanation as such (G05 to G12, %d units): %s.' % (
        sum(expl_counts.values()), ', '.join('%s %d' % (v, expl_counts[v]) for v in L.VERDICTS)))
    gen.append('\nUnits whose verdict turns on a reading (%d): %s. Units that also line up with the people studying Avida (%d): %s.\n' % (
        len(reading), ', '.join(reading), len(people), ', '.join(people)))
    gen.append('### Every unit\n')
    gen.append('Columns: unit (id, line in the formal core or the claims file, text lines), name, verdict, Avida counterpart, what matches or why not (plain), evidence, alternatives. "R" marks a verdict that turns on a reading; "P" a unit that also lines up with the people studying Avida.\n')
    for g, n, _ in L.GROUPS:
        gen.append('#### %s %s\n' % (g, n))
        gen.append('| unit | name | verdict | counterpart | plain | evidence | alternatives |\n|---|---|---|---|---|---|---|')
        for x in out_units:
            if x['group'] != g:
                continue
            where = ('core L%s' % x['formal_core_line']) if x['formal_core_line'] else (('claims L%s' % x['claims_md_line']) if x['claims_md_line'] else '')
            tl = ('; text ' + ', '.join('L%d' % t for t in x['text_lines'][:4])) if x['text_lines'] else ''
            marks = ('R' if x['turns_on_a_reading'] else '') + ('P' if x['also_lines_up_with_the_people_studying_avida'] else '')
            cell = lambda s: (s or '').replace('|', '/').replace('\n', ' ')
            gen.append('| %s%s (%s%s) | %s | %s | %s | %s | %s | %s |' % (
                x['id'], (' ' + marks) if marks else '', where, tl, cell(x['name'])[:120], x['verdict'], cell(x['avida_counterpart_name']),
                cell(x['plain'] + ((' ' + x['note']) if x['note'] else '')), cell(x['evidence']), cell(x['alternatives_considered'])))
        gen.append('')
    start, end = '<!-- generated: start -->', '<!-- generated: end -->'
    assert start in md and end in md
    md = md.split(start)[0] + start + '\n\n' + '\n'.join(gen) + '\n' + end + md.split(end)[1]
    open(md_path, 'w', encoding='utf-8').write(md)
    print(dict(by_v), len(out_units), 'reading', len(reading), 'people', len(people), 'relations', len(relations), 'lines', len(line_list))
    print({g: dict(by_group[g]) for g in by_group})
    print('explanatory', dict(expl_counts))
    print(dict(by_basis))


if __name__ == '__main__':
    main()
