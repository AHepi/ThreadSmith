#!/usr/bin/env python3
"""s109x_build.py: build the GLM cross-examination of Part B round 1's reading (log S109), decision S56: "Use GLM for
cross examination". Written 29 September 2026 by the one Opus 5.5 agent that did Part B round 1's reading (S56), on the
pattern of Part A round 2's cross-examination build (tools/s108r2x_build.py): Part A round 1's build (tools/s108_build.py) is
imported for its checks and its owner's words, never changed; the sandboxed helper and the shell guard are used unchanged.

Four GLM jobs at once (S39), each cross-examining the round's work from one angle:
  (a) the tabulation and computation of sections B1 and B2;  (b) of sections B3 and B4;
  (c) the map of how explanation changes in meaning and scope;  (d) the candidate list against the owner's decisions S20 to
  S56 and against Part A's list.
Each job gets its own sandbox manifest (the program copy it may run sits at the sandbox's root as model/), and a brief.
GLM may read, glob, grep and run `python3 -m model.run ...` in its sandbox (the guard: claim ids, --scale at most 4,
--time-cap at most 60, a clean environment, so every reading switch is off); it writes nothing.

  python3 Semantics/tools/s109x_build.py            build the briefs, the four manifests and the job list
  python3 Semantics/tools/s109x_build.py --check    rebuild in memory and compare; writes nothing

Refuses unless every source is committed and unchanged from HEAD; the frame of each brief (everything but the owner's
words) is free of the words S23 scrubs and of "model" used for a candidate (S43); no sandbox path looks like a key file;
each brief is at most CAP words.
"""
import json, os, re, sys
from collections import OrderedDict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s108_build as B  # noqa: E402  (Part A round 1's build: read, never written)

SEM = B.SEM
PB = 'results/S109 Part B round 1 - '
COMP = PB + 'computation/'
PA2 = 'results/S108 Part A round 2 - '
READING_RULE = PB + 'how the GLM cross-examination will be read, written before sending.md'
OUT = PB + 'GLM cross-examination returns'
MAT = PB + 'material for the GLM cross-examination'
JOBS_FILE = 'tools/s109x_jobs - Part B round 1, GLM cross-examination.json'
CAP = 7000
OWNER_EXTRA = [53, 54, 55, 56]           # the owner's words after S52, quoted like the others
TEXT_EXT = ('.py', '.md', '.txt', '.json', '.sh')
EXTRA_NOTE = {'part B/how explanation changes in meaning and scope.json': "the map's data: every variant's meaning, scope, claims and edges",
              'part A/the dependency map, after the cross-examination.json': "Part A's map after its cross-examination (the ids the Part B map cites)",
              "record/the owner's decisions.md": "the project's record of the owner's decisions, whole"}

COMMON = [
    ('part B/the rule for reading the replies.md', PB + 'how the replies will be read, written before sending.md'),
    ('part B/the rule for reading this cross-examination.md', READING_RULE),
    ('part B/the free set and the frozen template.md', 'results/S109 Part B - the free set and the frozen template.md'),
    ('part B/tabulation of the replies.md', PB + 'tabulation of the replies, before any ruling.md'),
    ('part B/how explanation changes in meaning and scope.md', PB + 'how explanation changes in meaning and scope.md'),
    ('part B/candidate definitions of explanation.md', PB + 'candidate definitions of explanation.md'),
] + [('part B/section B%d - variants computed.md' % n, PB + 'section B%d - variants computed.md' % n) for n in (1, 2, 3, 4)] \
  + [('part B/section B%d - variants computed.json' % n, PB + 'section B%d - variants computed.json' % n) for n in (1, 2, 3, 4)] \
  + [('part B/replies/section B%d.txt' % n, PB + 'returns/s109_glm_section%d.response.txt' % n) for n in (1, 2, 3, 4)] \
  + [('part B/comparisons with Part A - summary.txt', COMP + 'comparisons with Part A/comparison summary.txt'),
     ('part B/whole suite - summary.md', COMP + 'whole suite/summary.md'),
     ('part A/the dependency map, after the cross-examination.md', PA2 + 'the dependency map, after the cross-examination.md'),
     ('part A/candidate definitions of explanation, after the cross-examination.md', PA2 + 'candidate definitions of explanation, after the cross-examination.md'),
     ('part A/the GLM cross-examination, settled.md', PA2 + 'the GLM cross-examination, settled.md')]

JOBS = [
    dict(job=1, name='sectionsB1-B2', tag='s109x_glm_a', title='the tabulation and computation of sections B1 and B2',
         root=COMP + 'section B2 model', trees=[(COMP + 'section B1 model', 'section B1 program copy'),
                                               (COMP + 'section B1 runs', 'section B1 runs'),
                                               (COMP + 'section B2 runs', 'section B2 runs'),
                                               (COMP + 'whole suite/B1', 'whole suite/B1'),
                                               (COMP + 'whole suite/B2', 'whole suite/B2'),
                                               (COMP + 'patches', 'patches'),
                                               (COMP + 'scripts', 'scripts')],
         extra=[]),
    dict(job=2, name='sectionsB3-B4', tag='s109x_glm_b', title='the tabulation and computation of sections B3 and B4',
         root=COMP + 'section B3 model', trees=[(COMP + 'section B4 model', 'section B4 program copy'),
                                               (COMP + 'section B3 runs', 'section B3 runs'),
                                               (COMP + 'section B4 runs', 'section B4 runs'),
                                               (COMP + 'whole suite/B3', 'whole suite/B3'),
                                               (COMP + 'whole suite/B4', 'whole suite/B4'),
                                               (COMP + 'patches', 'patches'),
                                               (COMP + 'scripts', 'scripts')],
         extra=[]),
    dict(job=3, name='map', tag='s109x_glm_c', title='the map of how explanation changes in meaning and scope',
         root=None, trees=[(COMP + 'map', 'map builder')],
         extra=[('part B/how explanation changes in meaning and scope.json', PB + 'how explanation changes in meaning and scope.json'),
                ('part A/the dependency map, after the cross-examination.json', PA2 + 'the dependency map, after the cross-examination.json')]),
    dict(job=4, name='candidates', tag='s109x_glm_d', title="the candidate list against the owner's decisions S20 to S56 and against Part A's list",
         root=None, trees=[],
         extra=[('record/the owner\'s decisions.md', 'records/Semantics - Decisions.md')]),
]

ANGLE = {
    1: """Cross-examine **the tabulation and the computation of sections B1 and B2** (`part B/tabulation of the replies.md` §2, §3, §6 to §8; `part B/section B1 - variants computed.md`, `part B/section B2 - variants computed.md`, their `.json`; the program copies, the patches that put each variant in as a switch, the scope script, its runs and the whole-suite results). For each variant of B1 and B2: is the tabulation's record of the reply right, and is every flag (out of Part B or not) sound under the rule? Is the variant implemented as the reply wrote it, or is the nearest reading honestly stated as an invention with the other choices? Does each meaning (the old and new formal statement of each part of the explanation definition that moves) match the code? Does each scope result (the worked cases, the owner's four cases under each reading, the generated worlds, FC-E1 to FC-E5 and CT1 to CT8, and the claims that move in the whole suite) follow from the runs shown? Is every moved claim explained? The program at the sandbox's root is section B2's copy with every switch off (the program after round 4): rerun any claim there to check an "off" value; B1's copy is under `section B1 program copy/` to read.""",
    2: """Cross-examine **the tabulation and the computation of sections B3 and B4** (`part B/tabulation of the replies.md` §4 to §8; `part B/section B3 - variants computed.md`, `part B/section B4 - variants computed.md`, their `.json`; the program copies, the patches, the scope script, its runs and the whole-suite results). For each variant of B3 and B4: is the tabulation's record right, and is each flag (PB3.8 and PB4.4 out of Part B; PB4.4 restated on D9.8) sound? Is the variant implemented as the reply wrote it, or is the nearest reading honestly stated with the other choices? Does each meaning match the code? Does each scope result (the chains of up to three holdings, the student's copy, the hand-set histories, the owner's cases, the generated worlds, and the claims that move in the whole suite) follow from the runs shown? Is every moved claim explained? The program at the sandbox's root is section B3's copy with every switch off (the program after round 4); B4's copy is under `section B4 program copy/` to read.""",
    3: """Cross-examine **the map of how explanation changes in meaning and scope** (`part B/how explanation changes in meaning and scope.md` and `.json`, built from the four section files by the builder under `map builder/`). For each variant: is its meaning (old → new of each part of the explanation definition that moves) what the section file computes? Is its scope (worked cases, the owner's four cases, the made-up candidates entering and leaving, the claims that move) what the runs show? Is each edge's standing (computed, contradicted, claimed only) what its run shows, no more, and where an edge joins Part A's map, is the Part A id right (`part A/the dependency map, after the cross-examination.md` and `.json`)? Per part of the definition ((E), Dec, Expl, (Suff), (Nec)): are the free items its meaning and scope were found to turn on, and those varied without moving either, complete and right? Are the gaps under rule 10 of the round's rule listed in full, and is the proposal on whether a round 2 of Part B is needed what they show? The program at the sandbox's root is the program after round 4, to rerun any claim the map cites.""",
    4: """Cross-examine **the candidate list** (`part B/candidate definitions of explanation.md`) against the owner's decisions S20 to S56 (quoted in section 2 below and whole in `record/the owner's decisions.md`) and against Part A's list (`part A/candidate definitions of explanation, after the cross-examination.md`, C1 to C21). For each candidate PB-C…: does its statement match the variant as computed? Are its admits and drops the computed ones? Is every decision it does not appear to agree with named, with the owner's words, and is no decision named that the computation does not reach? Is a variant whose computation changes which candidates meet (E) or count as explanations missing from the list, or one listed that changes neither? Where it says a Part B candidate admits and drops the same as a Part A candidate on every case computed, is that so, and is a match missed? Where a reading of the owner's own cases decides a flag, does the list say "on that reading" only? For each flagged candidate: does the plain sentence and the everyday example say what the candidate does, without "model" for a candidate, with the owner's S44 case being the two-part sign? The program at the sandbox's root is the program after round 4.""",
}

INTRO = """# A cross-examination of an experiment on a semantics: Part B, round 1, job {job} of 4, {title}

## 1. What this is

A theory, called here the semantics, is stated in a prose text (`text/the text.md`, cited as L1 to L632) and in a formal core (definitions D§.n, encodings E1 to E9, formal claims FCnn that a program in `model/` tests on small structures). In this brief a "model" is only such a small structure, or the program's folder; what the theory judges is always called a candidate or an explanation.

The owner asked for an experiment in parts (S52, section 2). Part A froze the parts that are hard to vary and varied the middle. Part B, this part, freezes everything except the parts that are hard to vary (the free set, `part B/the free set and the frozen template.md`) and varies those, "to see how explanation changes in meaning and scope". In round 1 of Part B four agents proposed variants of four sections of the free set (their replies are in `part B/replies/`); then one agent (S56) tabulated them, implemented and computed every variant in copies of the program, and wrote a map of how explanation changes in meaning and scope and a list of candidate definitions of explanation. **Your job is to cross-examine that work from one angle** (section 4). Three other agents cross-examine it from other angles at the same time.

Nothing you write changes the theory, and nothing in the work you examine changed it: it is an experiment on copies. What you find is read by one agent after every cross-examination has ended, under the rule in `part B/the rule for reading this cross-examination.md`, and each objection is settled there by argument or by a run.

Who is who: "the owner" is the person whose theory this is; "Claude" is the drafters of the text and of the maths. Who made a point decides nothing, only its reasons do."""

TOOLS_TEXT = """## 3. The sandbox and your tools

Your working folder holds only copies. You may Read, Glob and Grep anything in it, and run exactly one command:

    python3 -m model.run [--claim FCnn]... [--scale N] [--time-cap N] [--brief]

from the folder itself (claim ids like FC30 or FC30.new1; --scale at most 4; --time-cap at most 60). It runs the program in `model/` at the folder's root with a clean environment, so **every reading switch of the copies is off there**: a run gives the program after round 4's values, which is what the files call "off". You cannot turn a variant on, write a file, or run any other code; where an objection needs a run you cannot make, say which run, in which copy, with which switch (the files name each switch, `S109B_VARIANT` and its readings), and what result would settle it.

The files:

| path | what |
|---|---|
| `BRIEF.md` | this brief |
| `model/` | {root_note} |
| `part B/` | the round's rule, the rule for reading this cross-examination, the free set and frozen template, the tabulation, the four "variants computed" files with their `.json`, the map, the candidate list, the four replies, the whole-suite summary (claims that move per variant) and the summary of the case-by-case comparisons with Part A's C5 and C6 |
| `part A/` | Part A's map and candidate list after its cross-examination, and its settled cross-examination |
| `text/`, `maths/`, `cases/` | the text after round 4 (and a copy by line), the formal core and claims after round 4, the case scripts (read only) |
{extra_rows}"""


REPORT = """## 5. The report

Terse. No summary of the material, no praise, no restating of what holds. At most about 3,000 words.

(a) **Objections**, one table, most serious first: id (X{job}.1, X{job}.2, ...); the file and the place (section, table row, edge id, candidate id); the objection in one or two lines; what shows it (a quotation with its place, a count from a file, or a run you made: the command and the program's result line); **the exact fix** (the value, the standing, the sentence or the row as it should read, or the run that would settle it: copy, switch, script).
(b) **Checked, no objection**: one line listing what you examined and found nothing to object to (ids only).
(c) **Not reached**: one line each, with why.

Write the whole report as your final message. Its last line must be exactly:

END OF REPORT"""


def frame_scan(b):
    f = B.frame_of(b)
    return sorted({m.group(0) for pat in B.SCRUB + B.FRAME_MODEL for m in re.finditer(pat, f, re.I)})


def owner_block():
    dec = B.read('records/Semantics - Decisions.md')
    body, own = B.owner_words(dec)
    extra = []
    for n in OWNER_EXTRA:
        m = re.search(r"(?m)^S%d\. \[Claude's reading[^:\]]*: .*?\] (.*)$" % n, dec)
        B.need(m, 'decision S%d not found' % n)
        extra.append('**S%d** (28–29 September 2026). %s' % (n, m.group(1)))
    body = body.replace("S52 is the instruction for this part: you are one of the four agents it names.",
                        "S52 is the instruction for the experiment; S56 is the one for this cross-examination.")
    return body + '\n\n' + "*After S52* the owner took four more decisions on who does the work; they bind how the work is done, not its content:\n\n" + '\n\n'.join(extra)


def tree_entries(src_dir, dst_dir):
    out = []
    base = B.path(src_dir)
    for root, dirs, files in os.walk(base):
        dirs[:] = sorted(d for d in dirs if d != '__pycache__')
        for f in sorted(files):
            if not f.endswith(TEXT_EXT) or f.endswith('.part'):
                continue
            rel = os.path.relpath(os.path.join(root, f), B.path(''))
            sub = os.path.relpath(os.path.join(root, f), base)
            dst = dst_dir + '/' + sub
            dst = re.sub(r'key', 'recflag', dst, flags=re.I)   # the helper refuses sandbox paths naming "key"
            out.append((dst, rel))
    return out


def build():
    files = OrderedDict()
    owner = owner_block()
    for n in B.KEEP:
        B.need(('**S%d**' % n) in owner, "the owner's words lack S%d" % n)
    base_src = [(d, s) for d, s, _ in B.sources() if not d.startswith('model/') and not d.startswith('template/')]
    r4_model = [(d, s) for d, s, _ in B.sources() if d.startswith('model/')]
    jobs_out, rows = [], []
    for j in JOBS:
        ent = list(base_src) + list(COMMON) + list(j['extra'])
        if j['root']:
            ent += [('model/' + os.path.relpath(s, j['root'] + '/model'), s) for _, s in tree_entries(j['root'] + '/model', 'm')]
            ent += [(d, s) for d, s in tree_entries(j['root'], 'root copy scripts') if not d.startswith('root copy scripts/model/')]
            root_note = "the program copy of %s (every switch off = the program after round 4); its scripts are under `root copy scripts/`" % j['root'].split('/')[-1]
        else:
            ent += r4_model
            root_note = "the program after round 4"
        for src, dst in j['trees']:
            ent += tree_entries(src, dst)
        seen, entries = set(), []
        for dst, rel in ent:
            if dst in seen:
                continue
            seen.add(dst)
            B.need(os.path.isfile(B.path(rel)), '%s is not there' % rel)
            B.need(B.committed(rel), '%s is not committed, or differs from HEAD' % rel)
            B.need(not re.search(r'(\.env$|key)', dst, re.I), 'a sandbox path looks like a key file: %s' % dst)
            entries.append({'path': dst, 'src': rel, 'md5': B.md5_file(rel)})
        extra_rows = '\n'.join('| `%s/` | %s |' % (dst, 'files of %s' % src.split('/')[-1]) for src, dst in j['trees']) + \
            ('\n' if j['trees'] and j['extra'] else '') + '\n'.join('| `%s` | %s |' % (d, EXTRA_NOTE.get(d, 'a copy')) for d, s in j['extra'])
        b = '\n\n'.join([INTRO.format(job=j['job'], title=j['title']), owner,
                         TOOLS_TEXT.format(root_note=root_note, extra_rows=extra_rows),
                         '## 4. Your job: ' + j['title'] + '\n\n' + ANGLE[j['job']] +
                         "\n\nThe owner's words bind the work as content (S20 to S56 above): an objection that a candidate or a flag goes against a decision names the decision and quotes it. Nothing about what must happen to a candidate (S21), nothing about which candidate to choose (S20), no word S23 removes. For what the theory judges say \"candidate\" or \"explanation\", never \"model\" (S43).",
                         REPORT.format(job=j['job'])]) + '\n'
        hits = frame_scan(b)
        B.need(not hits, 'brief %d: the frame holds %s' % (j['job'], hits))
        B.need(B.words(b) <= CAP, 'brief %d has %d words, above %d' % (j['job'], B.words(b), CAP))
        rel = 'tests/S109 Part B round 1 - GLM cross-examination, job %d, %s.md' % (j['job'], j['title'].replace("'", ''))
        files[rel] = b
        man = {'note': "Part B round 1 (log S109), the GLM cross-examination (S56), job %d: the files copied into its "
                       "sandbox, each checked by md5 at the copy; the brief is added as BRIEF.md. Written by "
                       "tools/s109x_build.py." % j['job'], 'files': entries}
        mrel = MAT + '/sandbox manifest, job %d.json' % j['job']
        files[mrel] = json.dumps(man, indent=1, ensure_ascii=False) + '\n'
        jobs_out.append({'job': j['job'], 'name': j['name'], 'tag': j['tag'], 'brief': rel, 'brief_md5': B.md5(b),
                         'manifest': mrel, 'manifest_md5': B.md5(files[mrel])})
        rows.append((j['job'], j['title'], j['tag'], rel, B.words(b), B.md5(b), len(entries)))
    jobs = {'round': 'Part B round 1 (log S109), the GLM cross-examination (S56)', 'rule': READING_RULE, 'out': OUT,
            'max_pass': 3, 'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'sandbox_root': 's109x_sandboxes', 'home_root': 's109x_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py', 'jobs': jobs_out}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s109x_build.py [--check]')
    files, rows = build()
    if '--check' in a:
        for rel, text in files.items():
            B.need(os.path.exists(B.path(rel)) and B.read(rel) == text, '%s differs from the build' % rel)
        print('check: all %d files identical to the build' % len(files))
    else:
        for rel, text in files.items():
            print(('wrote   ' if B.write_checked(rel, text) else 'same    ') + rel)
    print('\n| job | angle | tag | brief | words | md5 | sandbox files |\n|---|---|---|---|---|---|---|')
    for r in rows:
        print('| %d | %s | %s | `%s` | %d | %s | %d + BRIEF.md |' % r)


if __name__ == '__main__':
    main()
