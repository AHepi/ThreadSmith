#!/usr/bin/env python3
"""s111x_build.py: build the GLM cross-examination of log S111 (decision S59: Avida's digital organisms measured for the
owner's three properties of knowledge; decision S56: "Use GLM for cross examination"). Written 29 September 2026 by the
one Opus 5.5 agent of log S111, on the pattern of log S110's cross-examination build (tools/s110x_build.py): round 1's
build (tools/s108_build.py) is imported for its helpers only, never changed; the sandboxed helper
(tools/glm_via_claude_code_sandboxed.py) and the shell guard (tools/glm_sandbox_shell_guard.py) are used unchanged by the
runner (tools/s111x_glm_loop.py).

Four GLM jobs at once (S39), each cross-examining the S111 work from one angle:
  (a) do the measures measure the three properties as the owner stated them;
  (b) the scripts and the numbers;
  (c) what the program causes and what the simulated world does;
  (d) the plain-words file against the results.
Each sandbox holds copies of the S111 plan, the results (.md and .json), the plain-words file, the configuration files,
the build notes, the exact commands, the summary tables and the seven S111 scripts, plus, per job, the records its angle needs;
NEVER the Avida source or binary, and no raw run output (those stay in the scratch space and are not under Semantics/).
There is no program in the sandbox, so the guard refuses every command: GLM only reads (Read, Glob, Grep) and writes
nothing.

  python3 Semantics/tools/s111x_build.py            build the briefs, the four manifests and the job list
  python3 Semantics/tools/s111x_build.py --check    rebuild in memory and compare; writes nothing

Refuses unless every source is committed and unchanged from HEAD; the frame of each brief (everything but the owner's
words) holds none of the words decision S23 removes and no "model" for a candidate (S43); no sandbox path looks like a key
file or a program folder; no source lies outside Semantics/; each brief is at most CAP words.
"""
import json, os, re, sys
from collections import OrderedDict

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import s108_build as B  # noqa: E402  (round 1's build: read, never written; helpers only)

PRE = 'results/S111 Avida - '
READING_RULE = PRE + 'how the GLM cross-examination will be read, written before sending.md'
OUT = PRE + 'GLM cross-examination returns'
MAT = PRE + 'material for the GLM cross-examination'
JOBS_FILE = 'tools/s111x_jobs - S111, GLM cross-examination.json'
CAP = 7000
OWNER = [19, 20, 21, 23, 28, 43, 56, 57, 59]
RUNS = PRE + 'the runs/'
PLAN = PRE + 'how the three properties will be measured, written before running.md'
RES = PRE + 'the three properties measured.md'
RESJ = PRE + 'the three properties measured.json'
PLAIN = "plain words/111 A program with the three properties - Avida's digital organisms measured, in plain words.md"
SUMMARIES = ['copying and knockouts', 'the worlds over time', 'mutational robustness', 'Marletto test on the logic tasks']
SCRIPTS = ['s111_run_the_avida_worlds.py', 's111_avida_test_processor.py', 's111_measure_copying_and_knockouts.py',
           's111_measure_the_worlds_over_time.py', 's111_measure_mutational_robustness.py',
           's111_marletto_test_on_the_logic_tasks.py', 's111_summarise_the_three_properties.py']

COMMON = [('S111/1 the plan, written before running.md', PLAN),
          ('S111/2 the three properties measured.md', RES),
          ('S111/2 the three properties measured.json', RESJ),
          ('S111/3 plain words.md', PLAIN),
          ('S111/the rule for reading this cross-examination.md', READING_RULE)] + \
         [('runs/configuration/' + f, RUNS + 'configuration/' + f)
          for f in ['avida.cfg', 'environment.cfg', 'instset-heads.cfg', 'default-heads.org']] + \
         [('runs/build notes and Avida\'s rules as read from its source.md', RUNS + "build notes and Avida's rules as read from its source.md"),
          ('runs/the exact commands.txt', RUNS + 'the exact commands.txt')] + \
         [('runs/%s.%s' % (s, e), RUNS + '%s.%s' % (s, e)) for s in SUMMARIES for e in ('md', 'json')] + \
         [('scripts/' + s, 'tools/' + s) for s in SCRIPTS]
EXTRA = {
    1: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md'),
        ("records/S110 Error correction from constructor theory's perspective.md",
         "results/S110 Error correction from constructor theory's perspective.md"),
        ('records/S110 When something in a creative agent is knowledge - what the sources offer.md',
         'results/S110 When something in a creative agent is knowledge - what the sources offer.md')],
    4: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md'),
        ('records/plain words 110, an earlier plain-words file, for its style.md',
         'plain words/110 Error correction in constructor theory, and how the earlier attempts changed, in plain words.md')],
}
JOBS = [
    dict(job=1, name='measures-and-properties', tag='s111x_glm_a',
         title='whether the measures measure the three properties as the owner stated them'),
    dict(job=2, name='scripts-and-numbers', tag='s111x_glm_b', title='the scripts and the numbers'),
    dict(job=3, name='program-or-world', tag='s111x_glm_c',
         title='what the program causes and what the simulated world does'),
    dict(job=4, name='plain-words', tag='s111x_glm_d', title='the plain-words file against the results'),
]

ANGLE = {
    1: """Cross-examine **whether the measures measure the three properties as the owner stated them** (section 2, S59: information that "Can cause itself to be copied", "Can cause itself to resist change", "Can cause itself to remain"). Read `S111/1 the plan ...` and `S111/2 the three properties measured.md` (and `.json`). For each property: does each measure (C1 to C5; R1 to R4; M1 to M3; the controls K1 to K5) measure that property, or something nearby (for instance: a share of one-change programs that still copy themselves is about what the program does staying the same, not about its instructions staying the same; conservation of sites may be the world's removal of failures, not the information causing anything)? What reading of "cause itself" does the work use, and is it stated where it matters? Were the "counts as shown" and "counts against" lines of the plan written before the numbers, and does the results file apply them as written, or move them? Does any sentence of the results say more than its numbers show? Is Marletto's test (the quotation in `records/S110 Error correction ...`, section on what the book leaves open) applied to the logic tasks faithfully: which instructions one "would ultimately have to eliminate", in every copy, to stop a task being done "reliably"? Is every departure from the plan recorded, with its reason, and is anything planned left out without saying so? Does the last section (what these organisms have and lack, set beside the explanation kind) state observations only, settle nothing (S28), and keep to the owner's words (S23 in Claude's own sentences)?""",
    2: """Cross-examine **the scripts and the numbers**. Read the seven scripts under `scripts/`, the summary tables under `runs/` (each `.md` beside its `.json`), `runs/the exact commands.txt`, `runs/configuration/`, and `S111/2 the three properties measured.md` and `.json`. For each script: does it compute what its note at the top, the plan and the results file say it computes (the knockout with `nop-X`; "viable"; the shares viable, neutral, within 1%, lethal; the global alignment and the per-site conservation weighted by the number of organisms; the essential and non-essential sites; the fidelity expectations; births identical to the parent; the tasks at 10%; the joint knockouts in one genotype and in every genotype; the rule that a difference between conditions counts only if every seed of one lies beyond every seed of the other)? Look for arithmetic slips, wrong columns of Avida's data files (the column lists are in the build notes and in the scripts), off-by-one sites, weighting errors, a cap or threshold applied differently from what is said, and numbers in the results file that differ from the summary tables. The runs themselves are not in your folder, so judge the numbers by their consistency with each other and with the scripts, not by rerunning.""",
    3: """Cross-examine **what the program causes and what the simulated world does**. The work claims, measure by measure, which part is caused by the organism's own instructions and which by the simulated world (the scheduler that hands out processor time by merit; memory; the copy errors the world applies when an instruction is copied; the removal of organisms by age or by an offspring taking their cell). Read `S111/1 the plan ...`, `S111/2 the three properties measured.md`, `runs/build notes and Avida's rules as read from its source.md` (the rules, with the source lines they come from), `runs/configuration/` and the scripts. For each attribution: is it shown by a contrast (a knockout, a control world, a condition) or only asserted? Does the knockout test separate the program's part in copying from the world's? Do the controls K1 to K5 separate what they are said to separate (for instance K3: a program that cannot copy remains when nothing dies of age)? What confounds are left: the analysis instruction set holds a 27th instruction the main runs lack; the control worlds allow `nop-X` in copies; tasks change merit and so processor time; the test processor has fixed inputs and no neighbours. Is any "resisting" or "remaining" credited to the program that the world's rules alone would produce?""",
    4: """Cross-examine **the plain-words file** (`S111/3 plain words.md`) against the results (`S111/2 ...` and the summary tables under `runs/`). The owner is not a programmer. Check: every number and every statement in the plain file is in the results, with the same meaning (no rounding that changes a comparison, no statement stronger than the results); what was tested, what was not and what is unsure are all said; everyday language, with every unavoidable technical word explained in one plain sentence before its first use; one word for each thing throughout (for instance not "copy", "offspring" and "child" for the same thing without saying so); a concrete example before each general point; it starts with what happened and what it means for the owner's idea; it is marked as written before the GLM check; it ends with one next step; no word decision S23 removes in Claude's own sentences (quotations excepted); nothing settled (S28); nothing chosen for the owner (S21). Set it beside `records/plain words 110 ...` for style only.""",
}

INTRO = """# A cross-examination of a measuring job: job {job} of 4, {title}

## 1. What this is

The owner of a theory of explanation and creativity states knowledge by three properties (section 2, S59): information that can cause itself to be copied, can cause itself to resist change, and can cause itself to remain; the owner asked for a type of program with exactly those properties, and said the explanation kind comes next. Claude named digital organisms (self-copying programs of artificial-life research) and proposed to run Avida, an existing research simulator, and measure the three properties on its organisms, as a working case of knowledge without explanation. The owner said to do it.

One agent did the job: it wrote the plan before running (`S111/1 ...`), built Avida, ran nine simulated worlds (three copy error rates, three seeds each, 50,000 updates) and five control worlds, measured, and wrote the results (`S111/2 ...`, `.md` and `.json`) and a plain-words version for the owner (`S111/3 plain words.md`). The configuration, the exact commands, the build notes (with Avida's rules as read from its source), the summary tables and the scripts are under `runs/` and `scripts/`. Avida itself and the raw output of the runs are not in your folder. **Your job is to cross-examine that work from one angle** (section 4). Three other agents cross-examine it from other angles at the same time.

Nothing you write changes the theory. What you find is read by one agent after every cross-examination has ended, under the rule in `S111/the rule for reading this cross-examination.md`, and each objection is settled there by argument or by rerunning; findings that stand are applied to corrected copies of the S111 files and to the plain-words file.

Who is who: "the owner" is the person whose theory this is; "Claude" is the agent that did the job. Who made a point decides nothing, only its reasons do."""

TOOLS_TEXT = """## 3. The sandbox and your tools

Your working folder holds only copies. You may Read, Glob and Grep anything in it. **No command runs here**: there is no program in this folder, and every shell command is refused. You write nothing. Avida's source, its binary and the raw output of the runs are not here: judge the numbers from the scripts, the configuration and the summary tables.

The files:

| path | what |
|---|---|
| `BRIEF.md` | this brief |
| `S111/1 the plan, written before running.md` | the plan, committed before any measuring run |
| `S111/2 the three properties measured.md`, `.json` | the results |
| `S111/3 plain words.md` | the plain-words version for the owner, written before this cross-examination |
| `S111/the rule for reading this cross-examination.md` | how your report will be read |
| `runs/configuration/` | Avida's default configuration files as used (the runs change only what `runs/the exact commands.txt` shows) |
| `runs/build notes and Avida's rules as read from its source.md` | the build, and the rules of Avida the measures lean on, with source lines |
| `runs/the exact commands.txt` | every world run's command |
| `runs/*.md`, `runs/*.json` | the four summary tables, each written by one script |
| `scripts/` | the seven S111 scripts |
{extra_rows}"""

REPORT = """## 5. The report

Terse. No summary of the material, no praise, no restating of what holds. At most about 3,000 words.

(a) **Objections**, one table, most serious first: id (X{job}.1, X{job}.2, ...); the file and the place (section, table row, script and line); the objection in one or two lines; what shows it (a quotation from a file in this folder, with its place); **the exact fix** (the sentence, the number, the line of code as it should read, or the rerun that would settle it).
(b) **Checked, no objection**: one line listing what you examined and found nothing to object to (ids or sections only).
(c) **Not reached**: one line each, with why.

Write the whole report as your final message. Its last line must be exactly:

END OF REPORT"""

S23 = [r"\bfits?\b", r"\bfitting\b", r"\bsupport(s|ed)?\b", r"\bverif\w*", r"\bcorroborat\w*", r"\bprov(e|es|ed|en|ing)\b",
       r"\bdisprov\w*", r"reason to (believe|reject)", r"\bbelie\w*", r"better than", r"worse than", r"\btrue\b",
       r"\bestablish\w*", r"\bauthorit\w*", r"\bfoundation\w*", r"\bderiv\w*"]


def frame_scan(b):
    f = re.sub(r"(?s)## 2\. The owner's words.*?(?=## 3\. The sandbox)", "", b)
    f = re.sub(r'"[^"\n]*"', ' ', f)   # quoted words are the owner's or the files', not the frame's
    f = re.sub(r'`[^`\n]*`', ' ', f)
    return sorted({m.group(0) for pat in S23 + B.MODEL_FOR_CANDIDATE for m in re.finditer(pat, f, re.I)})


def owner_block():
    dec = B.read('records/Semantics - Decisions.md')
    out = []
    for n in OWNER:
        m = re.search(r"(?m)^S%d\. \[Claude's reading[^:\]]*: .*?\] (.*)$" % n, dec)
        B.need(m, 'decision S%d not found' % n)
        out.append('**S%d.** %s' % (n, m.group(1)))
    return ("## 2. The owner's words\n\nThe owner's decisions that bind this work, in the owner's words as the project's record "
            "keeps them (each record entry also holds Claude's reading, in square brackets, left out here; the whole record "
            "is in `records/the owner's decisions.md` where your job has it). They bind as content: an objection that the "
            "work goes against one names it and quotes it.\n\n" + '\n\n'.join(out))


def build():
    files = OrderedDict()
    owner = owner_block()
    jobs_out, rows = [], []
    for j in JOBS:
        ent = list(COMMON) + EXTRA.get(j['job'], [])
        entries = []
        for dst, rel in ent:
            B.need(os.path.isfile(B.path(rel)), '%s is not there' % rel)
            B.need(B.committed(rel), '%s is not committed, or differs from HEAD' % rel)
            B.need(not re.search(r'(\.env$|key)', dst, re.I), 'a sandbox path looks like a key file: %s' % dst)
            B.need(not re.match(r'model(/|$)', dst), 'a sandbox path would make a program folder: %s' % dst)
            B.need('scratchpad' not in rel and not rel.startswith('/') and '..' not in rel,
                   'a source lies outside Semantics/: %s' % rel)
            B.need(os.path.getsize(B.path(rel)) < 400000, '%s is too large for a summary' % rel)
            entries.append({'path': dst, 'src': rel, 'md5': B.md5_file(rel)})
        extra_rows = '\n'.join('| `%s` | %s |' % (d, 'a copy of the project record `%s`' % s) for d, s in EXTRA.get(j['job'], []))
        b = '\n\n'.join([INTRO.format(job=j['job'], title=j['title']), owner, TOOLS_TEXT.format(extra_rows=extra_rows),
                         '## 4. Your job: ' + j['title'] + '\n\n' + ANGLE[j['job']] +
                         "\n\nThe owner's words bind the work as content (section 2): nothing settled (S28), nothing chosen "
                         "for the owner (S21), no ranking (S20), no word S23 removes in Claude's own sentences. For what "
                         "the theory judges say \"candidate\" or \"explanation\", never \"model\" (S43).",
                         REPORT.format(job=j['job'])]) + '\n'
        hits = frame_scan(b)
        B.need(not hits, 'brief %d: the frame holds %s' % (j['job'], hits))
        B.need(B.words(b) <= CAP, 'brief %d has %d words, above %d' % (j['job'], B.words(b), CAP))
        rel = 'tests/S111 - GLM cross-examination, job %d, %s.md' % (j['job'], j['title'].replace("'", ''))
        files[rel] = b
        man = {'note': "Log S111, the GLM cross-examination (S56), job %d: the files copied into its sandbox, each checked by "
                       "md5 at the copy; the brief is added as BRIEF.md. No Avida source or binary, no raw run output. "
                       "Written by tools/s111x_build.py." % j['job'],
               'files': entries}
        mrel = MAT + '/sandbox manifest, job %d.json' % j['job']
        files[mrel] = json.dumps(man, indent=1, ensure_ascii=False) + '\n'
        jobs_out.append({'job': j['job'], 'name': j['name'], 'tag': j['tag'], 'brief': rel, 'brief_md5': B.md5(b),
                         'manifest': mrel, 'manifest_md5': B.md5(files[mrel])})
        rows.append((j['job'], j['title'], j['tag'], rel, B.words(b), B.md5(b), len(entries)))
    jobs = {'round': 'log S111, the GLM cross-examination (S56)', 'rule': READING_RULE, 'out': OUT,
            'max_pass': 3, 'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'sandbox_root': 's111x_sandboxes', 'home_root': 's111x_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py', 'jobs': jobs_out}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s111x_build.py [--check]')
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
