#!/usr/bin/env python3
"""s108r2x_build.py: build the GLM cross-examination of Part A round 2's reading (log S108), decision S56: "Use GLM for
cross examination". Written 29 September 2026 by the one Opus 5.5 agent that did round 2's reading (S56), on the pattern
of round 2's build (tools/s108r2_build.py): round 1's build (tools/s108_build.py) is imported for its checks and its
owner's words, never changed; the sandboxed helper and the shell guard are used unchanged.

Four GLM jobs at once (S39), each cross-examining the round-2 work from one angle:
  (a) the computations of sections 1 and 2;  (b) sections 3 and 4;  (c) the dependency map's edges and gaps;
  (d) the candidate list against the owner's decisions S20 to S56.
Each job gets its own sandbox manifest (the program copy it may run sits at the sandbox's root as model/), and a brief.
GLM may read, glob, grep and run `python3 -m model.run ...` in its sandbox (the guard: claim ids, --scale at most 4,
--time-cap at most 60, a clean environment, so every reading switch is off); it writes nothing.

  python3 Semantics/tools/s108r2x_build.py            build the briefs, the four manifests and the job list
  python3 Semantics/tools/s108r2x_build.py --check    rebuild in memory and compare; writes nothing

Refuses unless every source is committed and unchanged from HEAD; the frame of each brief (everything but the owner's
words) is free of the words S23 scrubs and of "model" used for a candidate (S43); no sandbox path looks like a key file;
each brief is at most CAP words.
"""
import json, os, re, sys
from collections import OrderedDict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s108_build as B  # noqa: E402  (round 1's build: read, never written)

SEM = B.SEM
R2 = 'results/S108 Part A round 2 - '
COMP = R2 + 'computation/'
READING_RULE = R2 + 'how the GLM cross-examination will be read, written before sending.md'
OUT = R2 + 'GLM cross-examination returns'
MAT = R2 + 'material for the GLM cross-examination'
JOBS_FILE = 'tools/s108r2x_jobs - Part A round 2, GLM cross-examination.json'
CAP = 7000
OWNER_EXTRA = [53, 54, 55, 56]           # the owner's words after S52, quoted like the others
TEXT_EXT = ('.py', '.md', '.txt', '.json', '.sh')

COMMON = [
    ('round 2/the rule for reading round 2.md', R2 + 'how the replies will be read, written before sending.md'),
    ('round 2/who computes, recorded before any reply was opened.md', R2 + 'who computes, recorded before any reply is opened.md'),
    ('round 2/the rule for reading this cross-examination.md', READING_RULE),
    ('round 2/tabulation of the replies.md', R2 + 'tabulation of the replies, before any ruling.md'),
    ('round 2/the dependency map, after round 2.md', R2 + 'the dependency map, after round 2.md'),
    ('round 2/candidate definitions of explanation, after round 2.md', R2 + 'candidate definitions of explanation, after round 2.md'),
] + [('round 2/section %d - variants computed.md' % n, R2 + 'section %d - variants computed.md' % n) for n in (1, 2, 3, 4)] \
  + [('round 2/section %d - variants computed.json' % n, R2 + 'section %d - variants computed.json' % n) for n in (1, 2, 3, 4)] \
  + [('round 2/replies/section %d.txt' % n, R2 + 'returns/s108r2_glm_section%d.response.txt' % n) for n in (1, 2, 3, 4)] \
  + [('round 1/the dependency map.md', 'results/S108 Part A - the dependency map.md'),
     ('round 1/candidate definitions of explanation.md', 'results/S108 Part A - candidate definitions of explanation.md'),
     ('round 1/review of the second computation of section 2.md', 'results/S108 Part A - Sonnet 5.5 trial/Opus review of the Sonnet 5.5 trial.md')]

JOBS = [
    dict(job=1, name='sections1-2', tag='s108r2x_glm_a', title='the computations of sections 1 and 2',
         root=COMP + 'section 2 model', trees=[(COMP + 'section 1 model', 'section 1 program copy'),
                                              (COMP + 'section 1 runs', 'section 1 runs'),
                                              (COMP + 'section 2 runs', 'section 2 runs'),
                                              (COMP + 'whole suite/section 1', 'whole suite/section 1'),
                                              (COMP + 'whole suite/section 2', 'whole suite/section 2')],
         extra=[]),
    dict(job=2, name='sections3-4', tag='s108r2x_glm_b', title='the computations of sections 3 and 4',
         root=COMP + 'section 3 model', trees=[(COMP + 'section 4 model', 'section 4 program copy'),
                                              (COMP + 'section 3 runs', 'section 3 runs'),
                                              (COMP + 'section 4 runs', 'section 4 runs'),
                                              (COMP + 'whole suite/section 3', 'whole suite/section 3'),
                                              (COMP + 'whole suite/section 4', 'whole suite/section 4')],
         extra=[]),
    dict(job=3, name='map', tag='s108r2x_glm_c', title="the dependency map's edges and gaps",
         root=None, trees=[(COMP + 'map after round 2', 'map builder')],
         extra=[('round 2/the dependency map, after round 2.json', R2 + 'the dependency map, after round 2.json'),
                ('round 1/the dependency map.json', 'results/S108 Part A - the dependency map.json')]),
    dict(job=4, name='candidates', tag='s108r2x_glm_d', title="the candidate list against the owner's decisions S20 to S56",
         root=None, trees=[],
         extra=[('record/the owner\'s decisions.md', 'records/Semantics - Decisions.md')]),
]

ANGLE = {
    1: """Cross-examine **the computations of sections 1 and 2** (`round 2/section 1 - variants computed.md`, `round 2/section 2 - variants computed.md`, their `.json`, the program copies, the runs and the whole-suite results). For each variant of these two sections: is it implemented as the reply wrote it (or, where the file says it could not be, is the nearest reading honestly stated)? Does each count, move and "0 moves" follow from the runs shown? Is each edge's standing (computed, contradicted, not settled) what its run shows, no more? Are the readings round 1's candidates rest on (C1, C2, C5, C6, C7, C11) computed under every choice the share names? Are the whole-suite results (`whole suite/`) the moves the file expects, and is every difference explained? The program at the sandbox's root is section 2's copy with every switch off (the program after round 4): you can rerun any claim there to check an "off" value; section 1's copy is under `section 1 program copy/` to read.""",
    2: """Cross-examine **the computations of sections 3 and 4** (`round 2/section 3 - variants computed.md`, `round 2/section 4 - variants computed.md`, their `.json`, the program copies, the runs and the whole-suite results). For each variant of these two sections: is it implemented as the reply wrote it, or is the nearest reading honestly stated? Does each count, move and "0 moves" follow from the runs shown (the chains, the generated worlds, the single-claim and whole-suite runs)? Is each edge's standing what its run shows, no more? Are the readings C8, C9, C10, C11, C12, C13 rest on computed under every choice the share names, and is each settlement of a round-1 edge (e3.30b, e3.34b, e4.22, e4.40) sound? The program at the sandbox's root is section 3's copy with every switch off (the program after round 4); section 4's copy is under `section 4 program copy/` to read.""",
    3: """Cross-examine **the dependency map after round 2** (`round 2/the dependency map, after round 2.md` and `.json`, built from round 1's corrected map, `round 1/the dependency map.md` and `.json`, by the builder under `map builder/`). Is every round-1 edge kept with its standing unless a round-2 computation changes it, and is each change recorded with the round-1 standing and what changed it? Is every new edge's standing what the section files show? Are the corrections from the review of the second computation of section 2 (`round 1/review of the second computation of section 2.md`, its O1 to O4) recorded where they belong? Are the gaps after round 2 listed in full: items still untouched that bear on the explanation definition, edges still unsettled, readings still computed one way only? Is the answer to "is a third round needed" what the gaps show? The program at the sandbox's root is the program after round 4, to rerun any claim the map cites.""",
    4: """Cross-examine **the candidate list after round 2** (`round 2/candidate definitions of explanation, after round 2.md`) against the owner's decisions S20 to S56, quoted in section 2 below and whole in `record/the owner's decisions.md`. For each candidate: does its statement match the variant as computed? Are its admits and drops the computed ones? Is every decision it does not appear to agree with named, with the owner's words, and is no decision named that the computation does not reach? Where a reading of the owner's own cases decides a flag (edit or boundary for the owner's changes; D6.3's quantifier), does the list say "on that reading" only, and leave the reading to the owner? For each flagged candidate: does the plain sentence and the everyday example say what the candidate does, without "model" for a candidate, with the owner's S44 case being the two-part sign? The program at the sandbox's root is the program after round 4.""",
}

INTRO = """# A cross-examination of an experiment on a semantics: job {job} of 4, {title}

## 1. What this is

A theory, called here the semantics, is stated in a prose text (`text/the text.md`, cited as L1 to L632) and in a formal core (definitions D§.n, encodings E1 to E9, formal claims FCnn that a program in `model/` tests on small structures). In this brief a "model" is only such a small structure, or the program's folder; what the theory judges is always called a candidate or an explanation.

The owner asked for an experiment (S52, section 2): freeze the parts that are hard to vary, change bits in the middle, and see how that changes how explanation is defined, to map dependencies. It ran in rounds. In round 2, four agents proposed variants of four sections of the middle (their replies are in `round 2/replies/`); then one agent (S56) tabulated them, implemented and computed every variant in copies of the program, and built a dependency map and a list of candidate definitions of explanation after round 2. **Your job is to cross-examine that work from one angle** (section 4). Three other agents cross-examine it from other angles at the same time.

Nothing you write changes the theory, and nothing in the work you examine changed it: it is an experiment on copies. What you find is read by one agent after every cross-examination has ended, under the rule in `round 2/the rule for reading this cross-examination.md`, and each objection is settled there by argument or by a run.

Who is who: "the owner" is the person whose theory this is; "Claude" is the drafters of the text and of the maths. Who made a point decides nothing, only its reasons do."""

TOOLS_TEXT = """## 3. The sandbox and your tools

Your working folder holds only copies. You may Read, Glob and Grep anything in it, and run exactly one command:

    python3 -m model.run [--claim FCnn]... [--scale N] [--time-cap N] [--brief]

from the folder itself (claim ids like FC30 or FC30.new1; --scale at most 4; --time-cap at most 60). It runs the program in `model/` at the folder's root with a clean environment, so **every reading switch of the copies is off there**: a run gives the program after round 4's values, which is what the files call "off". You cannot turn a variant on, write a file, or run any other code; where an objection needs a run you cannot make, say which run, in which copy, with which switch (the files name each switch), and what result would settle it.

The files:

| path | what |
|---|---|
| `BRIEF.md` | this brief |
| `model/` | {root_note} |
| `round 2/` | the rule for reading round 2, the record of who computes, the rule for reading this cross-examination, the tabulation of round 2's replies, the four "variants computed" files with their edge `.json`, the dependency map and the candidate list after round 2, and the four replies |
| `round 1/` | round 1's corrected dependency map and candidate list, and the review of a second computation of round 1's section 2 (its O1 to O4 are corrections the map after round 2 must carry) |
| `text/`, `maths/`, `template/`, `cases/` | the text after round 4 (and a copy by line), the formal core and claims after round 4, the frozen template and frozen set of Part A, the case scripts (read only) |
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
    base_src = [(d, s) for d, s, _ in B.sources() if not d.startswith('model/')]
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
            ('\n' if j['trees'] and j['extra'] else '') + '\n'.join('| `%s` | %s |' % (d, s.split('/')[-1]) for d, s in j['extra'])
        b = '\n\n'.join([INTRO.format(job=j['job'], title=j['title']), owner,
                         TOOLS_TEXT.format(root_note=root_note, extra_rows=extra_rows),
                         '## 4. Your job: ' + j['title'] + '\n\n' + ANGLE[j['job']] +
                         "\n\nThe owner's words bind the work as content (S20 to S56 above): an objection that a candidate or a flag goes against a decision names the decision and quotes it. Nothing about what must happen to a candidate (S21), nothing about which candidate to choose (S20), no word S23 removes. For what the theory judges say \"candidate\" or \"explanation\", never \"model\" (S43).",
                         REPORT.format(job=j['job'])]) + '\n'
        hits = frame_scan(b)
        B.need(not hits, 'brief %d: the frame holds %s' % (j['job'], hits))
        B.need(B.words(b) <= CAP, 'brief %d has %d words, above %d' % (j['job'], B.words(b), CAP))
        rel = 'tests/S108 Part A round 2 - GLM cross-examination, job %d, %s.md' % (j['job'], j['title'].replace("'", ''))
        files[rel] = b
        man = {'note': "Part A round 2 (log S108), the GLM cross-examination (S56), job %d: the files copied into its "
                       "sandbox, each checked by md5 at the copy; the brief is added as BRIEF.md. Written by "
                       "tools/s108r2x_build.py." % j['job'], 'files': entries}
        mrel = MAT + '/sandbox manifest, job %d.json' % j['job']
        files[mrel] = json.dumps(man, indent=1, ensure_ascii=False) + '\n'
        jobs_out.append({'job': j['job'], 'name': j['name'], 'tag': j['tag'], 'brief': rel, 'brief_md5': B.md5(b),
                         'manifest': mrel, 'manifest_md5': B.md5(files[mrel])})
        rows.append((j['job'], j['title'], j['tag'], rel, B.words(b), B.md5(b), len(entries)))
    jobs = {'round': 'Part A round 2 (log S108), the GLM cross-examination (S56)', 'rule': READING_RULE, 'out': OUT,
            'max_pass': 3, 'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'sandbox_root': 's108r2x_sandboxes', 'home_root': 's108r2x_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py', 'jobs': jobs_out}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s108r2x_build.py [--check]')
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
