#!/usr/bin/env python3
"""s129_run_the_suites_on_the_copy_and_compare.py

What it does, in plain words: for log S129 (decisions S83 and S84). Runs the model program's whole claim suite and its
worked-case scripts on the COPY of the program (results/S129 Reading C carried into copies/model after Reading C/)
under four settings of its two switches, and compares every claim's status and every part's status, and the printed
results, with the ORIGINAL program run the same way (a byte-equal copy of results/S107 Round 4 - maths after the
reading/model after round 4/ in the scratch space, laid out as the original expects, so the original is never run in
place) and with the record
(formal claims, after round 4.json, key after_round4):
  C off, graded off   the copy with both decisions switched off (must compute what the original does)
  C on,  graded off   Reading C alone (S83)
  C off, graded on    the graded survival condition alone (S84)
  C on,  graded on    both, the copy as the owner has now decided it
Suite: python3 -B -m model.run --scale 4 --time-cap 45 --no-write --brief, PYTHONHASHSEED=0 (the record's settings),
two settings at a time, under nice. Case scripts: s106_cases.py, s104_external.py, s104_creative_transport.py.
Output: printouts in the scratch space s129/; the comparison in results/S129 Reading C carried into copies/suite runs.json.

  python3 -B Semantics/tools/s129_run_the_suites_on_the_copy_and_compare.py            (runs what is missing, then compares)
  python3 -B Semantics/tools/s129_run_the_suites_on_the_copy_and_compare.py --compare  (compares only)

Written 2 October 2026 by the one Opus 5.5 agent of log S129.
"""
import json, os, re, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SC = '/tmp/claude-0/-home-user-ThreadSmith/8d9323da-c0ec-57ec-91fd-8f99ca99320a/scratchpad/s129'
SRC_DIR = os.path.join(ROOT, 'results', 'S107 Round 4 - maths after the reading')
# The original, copied byte for byte into the scratch space with the layout it expects around it (the formal core beside
# its folder; a link from tests/ to the project's tests/, which s104_external.py and s104_creative_transport.py read
# text 103 and the owner's case from), so that it is never run in place. (The original's whole-suite printout was first
# made from a plain copy, s129/baseline/; the suite does not read tests/, and that printout is kept.)
BASE = os.path.join(SC, 'base')
ORIG_DIR = os.path.join(BASE, 'results', 'S107 Round 4 - maths after the reading', 'model after round 4')


def ensure_baseline():
    import hashlib, shutil
    if not os.path.isdir(ORIG_DIR):
        shutil.copytree(os.path.join(SRC_DIR, 'model after round 4'), ORIG_DIR, ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copy(os.path.join(SRC_DIR, 'formal core, after round 4.md'), os.path.dirname(ORIG_DIR))
    if not os.path.exists(os.path.join(BASE, 'tests')):
        os.symlink(os.path.join(ROOT, 'tests'), os.path.join(BASE, 'tests'))
    h = lambda d: {os.path.relpath(os.path.join(r, f), d): hashlib.md5(open(os.path.join(r, f), 'rb').read()).hexdigest()
                   for r, _, fs in os.walk(d) if '__pycache__' not in r for f in fs}
    assert h(ORIG_DIR) == h(os.path.join(SRC_DIR, 'model after round 4')), 'the baseline copy is not byte-equal'
COPY_DIR = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'model after Reading C')
RECORD = os.path.join(ROOT, 'results', 'S107 Round 4 - maths after the reading', 'formal claims, after round 4.json')
OUT = os.path.join(ROOT, 'results', 'S129 Reading C carried into copies', 'suite runs.json')
SETTINGS = [('C off, graded off', '0', '0'), ('C on, graded off', '1', '0'), ('C off, graded on', '0', '1'), ('C on, graded on', '1', '1')]
CASES = ['s106_cases.py', 's104_external.py', 's104_creative_transport.py']
HEAD = re.compile(r'^(FC\S+)\s+(HOLDS ON ALL MODELS TRIED|COUNTEREXAMPLE FOUND|NOT TESTED)\s+\(')
PART = re.compile(r'^-- (.*) \[([^\]]*)\] ([^\[\]]*)$')


def env(c, g):
    e = dict(os.environ, PYTHONHASHSEED='0', PYTHONDONTWRITEBYTECODE='1', S129_READING_C=c, S129_GRADED=g)
    return e


def suite_file(tag):
    return os.path.join(SC, 'suite %s.txt' % tag)


def case_file(tag, script):
    return os.path.join(SC, 'case %s %s.txt' % (tag, script))


def start_suite(folder, tag, c='0', g='0'):
    out = open(suite_file(tag), 'w')
    return subprocess.Popen(['nice', '-n', '5', 'timeout', '2400', sys.executable, '-B', '-m', 'model.run', '--scale', '4',
                             '--time-cap', '45', '--no-write', '--brief'], cwd=folder, env=env(c, g), stdout=out,
                            stderr=subprocess.STDOUT)


def run_cases(folder, tag, c='0', g='0'):
    for s in CASES:
        with open(case_file(tag, s), 'w') as out:
            subprocess.run(['timeout', '1200', sys.executable, '-B', s], cwd=folder, env=env(c, g), stdout=out,
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


def main():
    compare_only = '--compare' in sys.argv
    if not compare_only:
        ensure_baseline()
        jobs = []
        if not os.path.exists(suite_file('original')):
            jobs.append((ORIG_DIR, 'original', '0', '0'))
        for lab, c, g in SETTINGS:
            if not os.path.exists(suite_file(lab)):
                jobs.append((COPY_DIR, lab, c, g))
        t0 = time.time()
        while jobs:
            batch, jobs = jobs[:2], jobs[2:]
            ps = [start_suite(*j) for j in batch]
            for p in ps:
                p.wait()
            print('ran %s (%.0f s so far)' % ([j[1] for j in batch], time.time() - t0))
        if not os.path.exists(case_file('original', CASES[0])):
            run_cases(ORIG_DIR, 'original')
        for lab, c, g in SETTINGS:
            if not os.path.exists(case_file(lab, CASES[0])):
                run_cases(COPY_DIR, lab, c, g)
    rec = record()
    orig = parse(suite_file('original'))
    counts = lambda r: {s: sum(1 for v in r.values() if v['status'] == s) for s in ('HOLDS ON ALL MODELS TRIED', 'COUNTEREXAMPLE FOUND', 'NOT TESTED')}
    res = {'about': 'S129: the model program\'s whole claim suite (scale 4, time cap 45 s, PYTHONHASHSEED=0, --no-write) and its three '
                    'worked-case scripts, run on the original (a byte-equal scratch copy) and on the S129 copy under four settings of its '
                    'switches; statuses and part statuses compared with the original and with the record (after_round4). Built by '
                    'tools/s129_run_the_suites_on_the_copy_and_compare.py.',
           'original': {'counts': counts(orig), 'claims': len(orig), 'against the record': compare(rec, orig)}}
    no = normalized(suite_file('original'))
    for lab, c, g in SETTINGS:
        r = parse(suite_file(lab))
        nr = normalized(suite_file(lab))
        printed = sorted(k for k in set(no) | set(nr) if no.get(k) != nr.get(k))
        cases = {}
        for s in CASES:
            a = open(case_file('original', s), encoding='utf-8').read()
            b = open(case_file(lab, s), encoding='utf-8').read()
            cases[s] = {'equal': a == b, 'lines': len(b.splitlines()),
                        'lines that differ': [(i + 1, x, y) for i, (x, y) in enumerate(zip(a.splitlines(), b.splitlines())) if x != y][:20]}
        res[lab] = {'switches': {'S129_READING_C': c, 'S129_GRADED': g}, 'counts': counts(r), 'claims': len(r),
                    'flips against the original (status or part status)': compare(orig, r),
                    'against the record': compare(rec, r),
                    'claims whose printed results differ from the original (times and time-capped counts left out)': printed,
                    'case scripts against the original': cases}
    json.dump(res, open(OUT, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
    print(json.dumps({k: (v['counts'] if 'counts' in v else None) for k, v in res.items() if isinstance(v, dict)}, ensure_ascii=False))
    for lab, _, _ in SETTINGS:
        v = res[lab]
        print('%s: flips %d; against the record %d; printouts differing %s; case scripts equal %s' % (
            lab, len(v['flips against the original (status or part status)']), len(v['against the record']),
            v['claims whose printed results differ from the original (times and time-capped counts left out)'],
            {s: x['equal'] for s, x in v['case scripts against the original'].items()}))
    print('original against the record:', res['original']['against the record'])


if __name__ == '__main__':
    main()
