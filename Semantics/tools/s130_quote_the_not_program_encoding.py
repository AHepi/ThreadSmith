#!/usr/bin/env python3
"""s130_quote_the_not_program_encoding.py

What it does, in plain words: for log S130 (decision S85), READ ONLY. It prints how S117 and S129 encoded the
evolved NOT program (MC1) for the theory's test of an explanation: the target, the contract, the candidate taken whole,
the selection history, and the verdicts S129 computed under each setting and boundary. It reads two committed files
and writes nothing:
  tools/s129_feed_avida_cases_to_the_copy_under_reading_c.py   (the encoding, quoted line by line)
  results/S129 Reading C carried into copies/map feeding under Reading C.json   (the computed verdicts)
It runs no model, no Avida and no experiment.

  python3 -B Semantics/tools/s130_quote_the_not_program_encoding.py

Written 2 October 2026 by the one Opus 5.5 agent of log S130.
"""
import json, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FEED = os.path.join(ROOT, 'tools', 's129_feed_avida_cases_to_the_copy_under_reading_c.py')
DATA = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'map feeding under Reading C.json')

lines = open(FEED, encoding='utf-8').read().splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith('def not_program'))
print('== The encoding of MC1 (%s, lines %d to %d)' % (os.path.basename(FEED), start + 1, start + 13))
for i in range(start, start + 13):
    print('%4d  %s' % (i + 1, lines[i]))
h = next(i for i, l in enumerate(lines) if "H = [(ONE, 'u0'), (ONE, 'u1')]" in l)
print('%4d  %s   <- the selection history H used for MC1' % (h + 1, lines[h].strip()))

d = json.load(open(DATA, encoding='utf-8'))
for setting, cases in d['settings'].items():
    for case in ('MC1 (graded-pay run: doing NOT raised the rate of copying)',
                 'MC1b (the run that paid for nothing: doing NOT changed nothing)'):
        m = cases[case]
        print('\n== %s | %s' % (setting, case.split(' (')[0]))
        print('   (E) taken whole: %s; cut into instructions: %s (F1 %s)' % (
            m['(E) of the program as one block'], m['(E) of the program cut into its instructions'],
            m['conditions (instructions)']['F1']))
        for nm, r in m['provenance and (Suff)'].items():
            print('   %-12s Sel %-5s Con %-5s Dec %-5s stands for NOT %-5s (Suff) defeated at L536 %s' % (
                nm.split(':')[0][:12], r['Sel'], r['Con'], r['Dec'],
                r['Rep: the program stands for NOT (faithful on the task and Sel or Con)'],
                r['(Suff) defeated, by reading']['L536']))
