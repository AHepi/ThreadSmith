#!/usr/bin/env python3
"""s131_run_the_suites_on_the_copy_and_compare.py

What it does, in plain words: for log S131 (decision S86, explanation kept for what was worked out). Runs the model
program's whole claim suite and its three worked-case scripts on the S131 COPY of the program
(results/S131 Explanation by construction carried into copies/model after Reading C and explanation by construction/)
under every setting of its three decision switches (Reading C, S83; the graded survival condition, S84; explanation by
construction, S86: eight settings), plus one more: all three on with the claims checking their round-4 wording
(S131_CLAIMS_REWORDED=0), to show which claims would flip as written. It compares every claim's status and every
part's status, and the printed results, with S129's copy under "both" (S129's own printout of its run, kept in the
scratch space s129/, the baseline this job compares against), with the S131 copy's own run at the same S129 setting
and S86 off, and with the record (formal claims, after round 4.json, key after_round4).
Suite: python3 -B -m model.run --scale 4 --time-cap 45 --no-write --brief, PYTHONHASHSEED=0 (the record's settings, as
S129 ran them), three settings at a time, under nice. Case scripts: s106_cases.py, s104_external.py,
s104_creative_transport.py. Output: printouts in the scratch space s131/; the comparison in
results/S131 Explanation by construction carried into copies/suite runs.json.

  python3 -B Semantics/tools/s131_run_the_suites_on_the_copy_and_compare.py            (runs what is missing, then compares)
  python3 -B Semantics/tools/s131_run_the_suites_on_the_copy_and_compare.py --compare  (compares only)

Written 2 October 2026 by the one Opus 5.5 agent of log S131.
"""
import json, os, re, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCR = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad'
SC = os.path.join(SCR, 's131')
SC129 = os.path.join(SCR, 's129')
OUT_DIR = os.path.join(ROOT, 'results', 'S131 Explanation by construction carried into copies')
COPY_DIR = os.path.join(OUT_DIR, 'model after Reading C and explanation by construction')
RECORD = os.path.join(ROOT, 'results', 'S107 Round 4 - maths after the reading', 'formal claims, after round 4.json')
OUT = os.path.join(OUT_DIR, 'suite runs.json')
S129_BOTH = 'C on, graded on'   # S129's tag for its run with both decisions
# (tag, Reading C, graded, explanation by construction, claims reworded)
SETTINGS = [
    ('C on, graded on, S86 off (S129 both)', '1', '1', '0', '1'),
    ('C on, graded on, S86 on (all three)', '1', '1', '1', '1'),
    ('C off, graded off, S86 on (S86 alone)', '0', '0', '1', '1'),
    ('C off, graded off, S86 off (none)', '0', '0', '0', '1'),
    ('C on, graded off, S86 on', '1', '0', '1', '1'),
    ('C off, graded on, S86 on', '0', '1', '1', '1'),
    ('C on, graded off, S86 off', '1', '0', '0', '1'),
    ('C off, graded on, S86 off', '0', '1', '0', '1'),
    ('C on, graded on, S86 on, claims as written in round 4', '1', '1', '1', '0'),
]
CASES = ['s106_cases.py', 's104_external.py', 's104_creative_transport.py']
HEAD = re.compile(r'^(FC\S+)\s+(HOLDS ON ALL MODELS TRIED|COUNTEREXAMPLE FOUND|NOT TESTED)\s+\(')
PART = re.compile(r'^-- (.*) \[([^\]]*)\] ([^\[\]]*)$')


def env(c, g, x, w):
    return dict(os.environ, PYTHONHASHSEED='0', PYTHONDONTWRITEBYTECODE='1', S129_READING_C=c, S129_GRADED=g,
                S131_EXPL_BY_CONSTRUCTION=x, S131_CLAIMS_REWORDED=w)


def suite_file(tag):
    return os.path.join(SC, 'suite %s.txt' % tag)


def case_file(tag, script):
    return os.path.join(SC, 'case %s %s.txt' % (tag, script))


def start_suite(tag, c, g, x, w):
    out = open(suite_file(tag), 'w')
    return subprocess.Popen(['nice', '-n', '5', 'timeout', '2400', sys.executable, '-B', '-m', 'model.run', '--scale', '4',
                             '--time-cap', '45', '--no-write', '--brief'], cwd=COPY_DIR, env=env(c, g, x, w), stdout=out,
                            stderr=subprocess.STDOUT)


def run_cases(tag, c, g, x, w):
    for s in CASES:
        with open(case_file(tag, s), 'w') as out:
            subprocess.run(['timeout', '1200', sys.executable, '-B', s], cwd=COPY_DIR, env=env(c, g, x, w), stdout=out,
                           stderr=subprocess.STDOUT)


def parse(path):
    claims, cur = {}, None
    for line in open(path, encoding='utf-8'):
        line = line.rstrip('\n')
        m = HEAD.match(line)
        if m:
            cur = m.group(1)
            claims[cur] = {'status': m.group(2), 'parts': []}
            continue
        m = PART.match(line)
        if m and cur:
            claims[cur]['parts'].append((m.group(1), m.group(3).strip()))
    return claims


def normalized(path):
    """The printout with run times and time-capped counts taken out, per claim."""
    per, cur = {}, None
    skip = re.compile(r'^\s+(models_tried|stopped|seed|smallest_size|hypothesis_met|space):')
    for line in open(path, encoding='utf-8'):
        m = HEAD.match(line)
        if m:
            cur = m.group(1)
            per[cur] = [m.group(1) + ' ' + m.group(2)]
            continue
        if cur and not skip.match(line) and not line.startswith('total ') and not line.startswith('====='):
            per[cur].append(re.sub(r'\(\d+\.\d s\)', '', line.rstrip('\n')))
    return per


def record():
    d = json.load(open(RECORD, encoding='utf-8'))
    rec = {}
    for c in d['claims']:
        a = c.get('after_round4')
        if a:
            rec[c['id']] = {'status': a['status'], 'parts': [(p['label'], p['status']) for p in a.get('parts', [])]}
    return rec


def compare(a, b):
    out = []
    for cid in sorted(set(a) | set(b)):
        x, y = a.get(cid), b.get(cid)
        if x is None or y is None:
            out.append({'claim': cid, 'what': 'missing in one run'})
            continue
        if x['status'] != y['status']:
            out.append({'claim': cid, 'what': 'status', 'from': x['status'], 'to': y['status']})
        px, py = dict(x['parts']), dict(y['parts'])
        for lab in px:
            if lab in py and px[lab].lower() != py[lab].lower():
                out.append({'claim': cid, 'what': 'part status', 'part': lab, 'from': px[lab], 'to': py[lab]})
        if [l for l, _ in x['parts']] != [l for l, _ in y['parts']]:
            out.append({'claim': cid, 'what': 'part labels differ'})
    return out


def printed_diff(a_path, b_path):
    na, nb = normalized(a_path), normalized(b_path)
    keys = sorted(k for k in set(na) | set(nb) if na.get(k) != nb.get(k))
    det = {}
    for k in keys:
        xa, xb = na.get(k, []), nb.get(k, [])
        det[k] = {'lines only in the baseline': [l for l in xa if l not in xb][:12],
                  'lines only in this run': [l for l in xb if l not in xa][:12]}
    return keys, det


def main():
    os.makedirs(SC, exist_ok=True)
    if '--compare' not in sys.argv:
        jobs = [s for s in SETTINGS if not os.path.exists(suite_file(s[0]))]
        t0 = time.time()
        while jobs:
            batch, jobs = jobs[:3], jobs[3:]
            ps = [start_suite(*j) for j in batch]
            for p in ps:
                p.wait()
            print('ran %s (%.0f s so far)' % ([j[0] for j in batch], time.time() - t0), flush=True)
        for s in SETTINGS:
            if not os.path.exists(case_file(s[0], CASES[0])):
                run_cases(*s)
    rec = record()
    base_path = os.path.join(SC129, 'suite %s.txt' % S129_BOTH)
    base = parse(base_path)
    own_base_tag = SETTINGS[0][0]
    counts = lambda r: {s: sum(1 for v in r.values() if v['status'] == s) for s in ('HOLDS ON ALL MODELS TRIED', 'COUNTEREXAMPLE FOUND', 'NOT TESTED')}
    res = {'about': 'S131: the model program\'s whole claim suite (scale 4, time cap 45 s, PYTHONHASHSEED=0, --no-write) and its three '
                    'worked-case scripts, run on the S131 copy under the eight settings of its three decision switches (S83 Reading C, '
                    'S84 graded survival condition, S86 explanation by construction) and once more with all three on and the claims '
                    'checking their round-4 wording; statuses and part statuses compared with S129\'s run of its copy under both '
                    'decisions (the baseline: S129\'s printout ' + base_path.replace(SCR, 'scratchpad') + '), with this copy at the '
                    'same setting and S86 off, and with the record (after_round4). Built by '
                    'tools/s131_run_the_suites_on_the_copy_and_compare.py.',
           'baseline (S129, C on, graded on)': {'counts': counts(base), 'claims': len(base), 'against the record': compare(rec, base)}}
    for tag, c, g, x, w in SETTINGS:
        r = parse(suite_file(tag))
        keys, det = printed_diff(base_path, suite_file(tag))
        cases = {}
        for s in CASES:
            a = open(os.path.join(SC129, 'case %s %s.txt' % (S129_BOTH, s)), encoding='utf-8').read()
            b = open(case_file(tag, s), encoding='utf-8').read()
            cases[s] = {'equal to S129 both': a == b, 'lines': len(b.splitlines()),
                        'lines that differ': [(i + 1, xx, yy) for i, (xx, yy) in enumerate(zip(a.splitlines(), b.splitlines())) if xx != yy][:20]}
        res[tag] = {'switches': {'S129_READING_C': c, 'S129_GRADED': g, 'S131_EXPL_BY_CONSTRUCTION': x, 'S131_CLAIMS_REWORDED': w},
                    'counts': counts(r), 'claims': len(r),
                    'flips against S129 both (status or part status)': compare(base, r),
                    'flips against this copy with S86 off at the same S129 setting': compare(parse(suite_file(own_base_tag)), r) if (c, g) == ('1', '1') else 'not compared (another S129 setting)',
                    'against the record': compare(rec, r),
                    'claims whose printed results differ from S129 both (times and time-capped counts left out)': keys,
                    'printed differences in detail': det,
                    'case scripts against S129 both': cases}
    json.dump(res, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print('baseline', res['baseline (S129, C on, graded on)']['counts'])
    for tag, *_ in SETTINGS:
        v = res[tag]
        print('%-55s %s | flips vs S129 both %d %s | vs record %d | printouts differing %s | cases equal %s' % (
            tag, '/'.join(str(n) for n in v['counts'].values()), len(v['flips against S129 both (status or part status)']),
            sorted(set(f['claim'] for f in v['flips against S129 both (status or part status)'])), len(v['against the record']),
            v['claims whose printed results differ from S129 both (times and time-capped counts left out)'],
            {s: xx['equal to S129 both'] for s, xx in v['case scripts against S129 both'].items()}))


if __name__ == '__main__':
    main()
