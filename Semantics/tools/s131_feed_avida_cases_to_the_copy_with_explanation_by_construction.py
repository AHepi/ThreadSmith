#!/usr/bin/env python3
"""s131_feed_avida_cases_to_the_copy_with_explanation_by_construction.py

What it does, in plain words: for log S131 (decision S86, explanation kept for what was worked out). S129's feeding
script (tools/s129_feed_avida_cases_to_the_copy_under_reading_c.py, which is S117's, copied) pointed at the S131 copy
of the model program (results/S131 Explanation by construction carried into copies/model after Reading C and
explanation by construction/). S129's script is read, never written: its text is loaded with only its folder and output
names changed, so its cases (MC1 to MC4: the evolved NOT program taken whole and cut into its instructions, its four
histories, MC1b in the run that paid for nothing; two programs differing at an order the world never gives; the
two-place program; the fine-grain program) are built exactly as S129 built them. Two things are added:
  - the provenance rows pass Con to (Suff) and to the owner's condition (the S131 copy asks for it when S86 is on),
    and say in words what the semantics then says of the program: an explanation by (Suff)'s conjecture, no
    explanation by the owner's condition, or not an account;
  - the eight settings of the copy's three decision switches (S83 Reading C, S84 graded, S86 explanation by
    construction), so the map can be recounted under each.
Output: printed, and results/S131 Explanation by construction carried into copies/map feeding with explanation by
construction.json (S129's "map feeding under Reading C.json", extended; S129's file is not written).

  PYTHONHASHSEED=0 python3 -B Semantics/tools/s131_feed_avida_cases_to_the_copy_with_explanation_by_construction.py

Written 2 October 2026 by the one Opus 5.5 agent of log S131.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S129_SCRIPT = os.path.join(ROOT, 'tools', 's129_feed_avida_cases_to_the_copy_under_reading_c.py')
OUT_DIR = os.path.join(ROOT, 'results', 'S131 Explanation by construction carried into copies')
COPY = os.path.join(OUT_DIR, 'model after Reading C and explanation by construction')
OUTF = os.path.join(OUT_DIR, 'map feeding with explanation by construction.json')
S129_FEED = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'map feeding under Reading C.json')

# ---- S129's script, loaded with its folder and output names pointed here -------------------------------------------
src = open(S129_SCRIPT, encoding='utf-8').read()
for old, new in (("COPY = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'model after Reading C')",
                  'COPY = %r' % COPY),
                 ("OUTF = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'map feeding under Reading C.json')",
                  'OUTF = %r' % OUTF),
                 ("SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s129'",
                  "SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s131'")):
    assert src.count(old) == 1, old
    src = src.replace(old, new)
S = {'__name__': 's129_feed_pointed_at_s131', '__file__': S129_SCRIPT}
exec(compile(src, S129_SCRIPT + ' (pointed at the S131 copy)', 'exec'), S)
cb = S['cb']
assert os.path.dirname(os.path.dirname(os.path.abspath(cb.__file__))) == COPY, cb.__file__
from model.claims_s41 import suff_defeats, expl_ruled_out, expl_ok, SUFF_READINGS  # noqa: E402  (the S131 copy's)
from model.args import Assessor, Imp, Not  # noqa: E402
from model.core import faithful  # noqa: E402

SETTINGS = [('C on, graded on, S86 on', True, True, True), ('C on, graded on, S86 off', True, True, False),
            ('C off, graded off, S86 on', False, False, True), ('C off, graded off, S86 off', False, False, False),
            ('C on, graded off, S86 on', True, False, True), ('C off, graded on, S86 on', False, True, True),
            ('C on, graded off, S86 off', True, False, False), ('C off, graded on, S86 off', False, True, False)]


def says(acc, s, k, dec):
    """What the semantics says of the candidate under the switch in force (Θ by hand nowhere: computed values only)."""
    if not acc:
        return 'not an account: the test (E) fails, so neither (Suff) nor the owner\'s condition speaks'
    if cb.EXPL_BY_CONSTRUCTION:
        if k:
            return 'an explanation by (Suff)\'s conjecture (an account whose transport was constructed)'
        return ('no explanation, by the owner\'s condition (S41, S86: an account whose transport was not constructed); '
                + ('a representation of what it is faithful to: evolved knowledge' if s else 'declared: it represents nothing'))
    if dec:
        return 'no explanation, by the owner\'s condition (S41: an account whose transport was declared)'
    return 'an explanation by (Suff)\'s conjecture (an account whose transport was not declared)' + (', in the narrow sense, never a created one' if s else '')


def provenance_rows(c1, acc1, H, advantage):
    rows = {}
    for nm, h in S['histories'](set(H), advantage):
        s, k = cb.sel(c1, H, h), cb.con(h)
        dec = (not s) and (not k)
        j = Assessor(['MP'], ['r', Imp('r', Not('Expl_' + c1.name))])
        out, _ = expl_ruled_out(j, c1.name)
        code_reps = any(o == S['CODE'] for o, _ in cb.rep_at_beta(h))
        owner_applies = bool(acc1 and ((not k) if cb.EXPL_BY_CONSTRUCTION else dec))
        rows[nm] = {'Sel': s, 'Con': k, 'Dec': dec,
                    'the task-check code represents (survival condition, task) at this boundary': code_reps if S['CODE'] in h.occ else None,
                    'the task-check code entered the boundary whole': cb.entered_whole(h, S['CODE']) if S['CODE'] in h.occ else None,
                    'Rep: the program stands for NOT (faithful on the task and Sel or Con)': bool(faithful(c1)) and (s or k),
                    'argument not using (E) rules out Expl': out,
                    '(Suff) defeated, by reading': {r: suff_defeats(acc1, dec, out, r, con=k) for r in SUFF_READINGS},
                    'owner S41 condition Acc and Dec => not Expl, with Expl false': expl_ok(acc1, dec, False, con=k),
                    "the owner's condition rules out Expl (S86 on: Acc and not Con; off: Acc and Dec)": owner_applies,
                    "(Suff) conjectures Expl (S86 on: Acc and Con; off: Acc and not Dec)": bool(acc1 and (k if cb.EXPL_BY_CONSTRUCTION else not dec)),
                    'what the semantics says of the program taken whole': says(acc1, s, k, dec)}
    return rows


S['provenance_rows'] = provenance_rows      # mc1 looks this name up at call time


def main():
    out = {'about': 'S131: S117\'s Avida cases fed to the S131 copy of the model (S83 Reading C; S84 graded survival condition; S86 '
                    'explanation by construction), under the eight settings of its three switches, by S129\'s feeding script pointed at '
                    'the S131 copy (tools/s131_feed_avida_cases_to_the_copy_with_explanation_by_construction.py). Θ by hand (I90), as '
                    'S129 and S117 set it. S129\'s own file (' + os.path.relpath(S129_FEED, ROOT) + ') is unchanged.',
           'model copy': os.path.relpath(COPY, ROOT), 'settings': {}}
    for lab, c_on, g_on, x_on in SETTINGS:
        cb.READING_C, cb.GRADED, cb.EXPL_BY_CONSTRUCTION = c_on, g_on, x_on   # the functions read these at call time
        out['settings'][lab] = {
            'MC1 (graded-pay run: doing NOT raised the rate of copying)': S['mc1'](True),
            'MC1b (the run that paid for nothing: doing NOT changed nothing)': S['mc1'](False),
            'MC2': S['mc2'](), 'MC3': S['mc3'](), 'MC4': S['mc4']()}
    cb.READING_C, cb.GRADED, cb.EXPL_BY_CONSTRUCTION = True, True, True
    # check: with S86 off, every value S129 recorded is computed again here (S129's keys only)
    s129 = json.load(open(S129_FEED, encoding='utf-8'))
    same = {}
    for lab129 in s129['settings']:
        mine = out['settings'][lab129 + ', S86 off']
        a = json.dumps(s129['settings'][lab129], sort_keys=True, default=str)
        b = dict(mine)
        for case in ('MC1 (graded-pay run: doing NOT raised the rate of copying)', 'MC1b (the run that paid for nothing: doing NOT changed nothing)'):
            b[case] = dict(b[case])
            b[case]['provenance and (Suff)'] = {nm: {k: v for k, v in r.items() if k in s129['settings'][lab129][case]['provenance and (Suff)'][nm]}
                                                for nm, r in b[case]['provenance and (Suff)'].items()}
        same[lab129] = a == json.dumps(json.loads(json.dumps(b, default=str)), sort_keys=True, default=str)
    out['check: with S86 off, S129\'s recorded values computed again (S129\'s keys)'] = same
    json.dump(out, open(OUTF, 'w', encoding='utf-8'), indent=1, ensure_ascii=False, default=str)
    print('S129 values reproduced with S86 off:', same)
    for lab, v in out['settings'].items():
        print('==', lab)
        for case in ('MC1 (graded-pay run: doing NOT raised the rate of copying)', 'MC1b (the run that paid for nothing: doing NOT changed nothing)'):
            print('  ', case.split(' (')[0], '(E) one block', v[case]['(E) of the program as one block'], '| cut', v[case]['(E) of the program cut into its instructions'])
            for nm, r in v[case]['provenance and (Suff)'].items():
                print('     %-28s Sel %-5s Con %-5s Dec %-5s Rep %-5s (Suff) defeated (L536) %-5s | %s' % (
                    nm[:28], r['Sel'], r['Con'], r['Dec'], r['Rep: the program stands for NOT (faithful on the task and Sel or Con)'],
                    r['(Suff) defeated, by reading']['L536'], r['what the semantics says of the program taken whole'][:90]))


if __name__ == '__main__':
    main()
