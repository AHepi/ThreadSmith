#!/usr/bin/env python3
"""s113x_build.py: build the GLM cross-examination of log S113 (decisions S62 to S64: which Avida execution
environments make a program population progressively learn to do new things, starting every run from the same Avida
program and changing only the Avida execution environment; decision S61: the owner's Avida terms; decision S56: "Use
GLM for cross examination"). Written 30 September 2026 by the one Opus 5.5 agent of log S113: log S112's
cross-examination build (tools/s112x_build.py) with its names, files and briefs changed, and nothing else: round 1's
build (tools/s108_build.py) is imported for its helpers only, never changed; the sandboxed helper
(tools/glm_via_claude_code_sandboxed.py) and the shell guard (tools/glm_sandbox_shell_guard.py) are used unchanged by
the runner (tools/s113x_glm_loop.py).

Four GLM jobs at once (S39), each cross-examining the S113 work from one angle:
  (a) does the design answer the owner's question, and are the environments comparable;
  (b) the measures and the scripts;
  (c) the results against the summaries and the plan;
  (d) the plain-words file against the results.
Each sandbox holds copies of the S113 plan, the results (.md and .json), the plain-words file 113, the reading rule,
the owner's Avida terms, the exact commands, the S113 configuration files and task ranking, S111's configuration files
and build notes (Avida's rules as read from its source), and the six S113 scripts, plus, per job, the records its
angle needs; NEVER the Avida source or binary, and no raw output (Avida's data files and saved program populations stay
in the scratch space and are not under Semantics/). There is no program in the sandbox, so the guard refuses every
command: GLM only reads (Read, Glob, Grep) and writes nothing.

  python3 Semantics/tools/s113x_build.py            build the briefs, the four manifests and the job list
  python3 Semantics/tools/s113x_build.py --check    rebuild in memory and compare; writes nothing

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

PRE = 'results/S113 Which execution environments learn - '
READING_RULE = PRE + 'how the GLM cross-examination will be read, written before sending.md'
OUT = PRE + 'GLM cross-examination returns'
MAT = PRE + 'material for the GLM cross-examination'
JOBS_FILE = 'tools/s113x_jobs - S113, GLM cross-examination.json'
CAP = 7000
OWNER = [20, 21, 23, 28, 43, 56, 61, 62, 63, 64]
RUNS111 = 'results/S111 Avida - the runs/'
RUNS = PRE + 'the runs/'
PLAN = PRE + 'how it will be tested, written before running.md'
RES = PRE + 'results.md'
RESJ = PRE + 'results.json'
PLAIN = 'plain words/113 Which execution environments learn new things, in plain words.md'
TERMS = 'records/Semantics - Avida terms, given by the owner.md'
SCRIPTS = ['s113_rank_the_tasks_by_the_fewest_nand_steps_they_need.py', 's113_run_the_avida_execution_environments.py',
           's113_count_new_capabilities_over_time.py', 's113_measure_capabilities_in_the_saved_program_populations.py',
           's113_measure_reuse_of_task_circuits.py', 's113_print_the_results_tables.py']
CONF113 = ['environment - %s, first piece.cfg' % e for e in
           ['fixed_graded', 'equ_only', 'no_rewards', 'growing', 'common_pays_less', 'fixed_large']] + \
          ['environment - growing, all ten levels rewarded.cfg', 'events - first piece.cfg', 'events - every later piece.cfg']

COMMON = [('S113/1 the plan, written before running.md', PLAN),
          ('S113/2 results.md', RES),
          ('S113/2 results.json', RESJ),
          ('S113/3 plain words.md', PLAIN),
          ('S113/the rule for reading this cross-examination.md', READING_RULE),
          ("S113/the owner's Avida terms.md", TERMS),
          ('runs/the exact commands.txt', RUNS + 'the exact commands.txt'),
          ('runs/the 77 tasks ranked by the fewest nand steps.json', RUNS + 'the 77 tasks ranked by the fewest nand steps.json')] + \
         [('runs/configuration/' + f, RUNS + 'configuration/' + f) for f in CONF113] + \
         [('runs/configuration from log S111/' + f, RUNS111 + 'configuration/' + f)
          for f in ['avida.cfg', 'environment.cfg', 'instset-heads.cfg', 'default-heads.org']] + \
         [("runs/build notes and Avida's rules as read from its source (from log S111).md",
           RUNS111 + "build notes and Avida's rules as read from its source.md")] + \
         [('scripts/' + s, 'tools/' + s) for s in SCRIPTS]
EXTRA = {
    1: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md'),
        ('records/S111 results, after its cross-examination.md',
         'results/S111 Avida - the three properties measured, after the cross-examination.md')],
    4: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md'),
        ('records/plain words 112, an earlier plain-words file, for its style.md',
         'plain words/112 What the evolved sums actually are, in plain words.md')],
}
JOBS = [
    dict(job=1, name='the-design-and-the-owners-question', tag='s113x_glm_a',
         title="whether the design answers the owner's question and the environments are comparable"),
    dict(job=2, name='the-measures-and-scripts', tag='s113x_glm_b',
         title='the measures and the scripts'),
    dict(job=3, name='the-results-against-the-plan', tag='s113x_glm_c',
         title='the results against the summaries and the plan'),
    dict(job=4, name='plain-words', tag='s113x_glm_d', title='the plain-words file against the results'),
]

ANGLE = {
    1: """Cross-examine **whether the design answers the owner's question, and whether the Avida execution environments are comparable**. The owner's question (section 2, S63): "what kind of execution environment can use these machines to progressively learn how to do new things"; the test the owner approved (S64): start every run from the same Avida program, change only the Avida execution environment, count how many new computational capabilities appear over time. Read `S113/1 the plan ...` (sections 0 to 4), `runs/configuration/`, `runs/configuration from log S111/`, `scripts/s113_run_the_avida_execution_environments.py`, `runs/the exact commands.txt` and the results (`S113/2 ...`). Check: does each environment answer "what kind of execution environment" in the way the plan says; is everything but the environment the same in every run (starting program, instruction set, world, instruction-change rate, program replication rules, the pieces of 1,000 updates, the Avida seeds), and where it is not, is it said; does listing unrewarded tasks at value 0 leave a run unchanged, and is the check of that enough; does cutting runs into pieces (saving and loading the program population) change what is measured, and does the comparison with S111's unbroken runs show what the results say; is the growing list's rule a fair reading of "adds harder tasks as easier ones become common"; do COMMON TASKS PAY LESS's resources make a common task pay less, as the configuration and Avida's rule give it; is the difficulty ranking (fewest `nand` steps) a sound order for the growing list and the reward values; are the expectations and what counts against each stated before running and applied as stated; does any sentence of the last section of the results say more than the numbers show, or settle what the owner left open (S28)? Set it beside `records/S111 results ...` only for the settings the runs share.""",
    2: """Cross-examine **the measures and the scripts**. Read `scripts/s113_count_new_capabilities_over_time.py`, `scripts/s113_measure_reuse_of_task_circuits.py`, `scripts/s113_run_the_avida_execution_environments.py`, `scripts/s113_rank_the_tasks_by_the_fewest_nand_steps_they_need.py`, `runs/the exact commands.txt`, `runs/configuration/` and the results (`S113/2 ...`, `.md` and `.json`), against the plan (`S113/1 ...`, sections 2, 5 and 6). Check: does the code compute each measure as the plan defines it (M1 present by any program and common at 10%; M2 first appearance; M3 keeping, and the count of a common task falling to no program; M4 the last new high and "levels off" at or before 40,000; M5 the spread; M6 required instructions by single instruction ablation with `nop-X`, the pairs ordered by first appearance, the random expectation); does the comparison rule ("more" only if every seed of one environment is above every seed of the other) match the plan and is it applied to each expectation as written; does the growing list's rule in the runner match the plan (the level, the 10% share read from `tasks.dat` and `count.dat` at a piece's end, one level per piece); does the ranking script find the fewest `nand` steps (the search, its cut at 9 steps and the lower bound for the one task not found); the columns read from Avida's `tasks.dat`, `count.dat`, `resource.dat` and the saved population, as the scripts read them; the undercount of task performances just after a load, and how it is measured. What do the limits leave open (samples every 250 updates; three seeds; one program per run for reuse; the test processor's fixed inputs; the random expectation's assumption)? Is each limit stated where a result leans on it? The runs are not in your folder: judge the numbers by their consistency with the code and with each other.""",
    3: """Cross-examine **the results against the summaries and the plan**. Read the results (`S113/2 results.md` and `S113/2 results.json`) and the plan (`S113/1 ...`), with `runs/the exact commands.txt`. Check: is every number in the `.md` the number in the `.json` (per environment, per seed, over time, first appearances, keeping, levelling off, reuse); are the spreads across seeds given where the plan asks; is each comparison the plan named (sections 6 and 7: one hard task against graded; no rewards; growing against fixed graded; growing against fixed large, "a growing list learns more new capabilities than a fixed list"; levelling off; common tasks pay less; keeping; reuse) reported with the plan's rule and its "against" stated before running, and is any comparison reported with a rule other than the plan's; is every departure from the plan recorded, with its reason; is what was not measured said; does any sentence say more than its numbers show (a difference inside the seeds' spread read as a difference; a count at one time read as a trend); in the last section, is what the results say about the owner's question given as observations, settling nothing (S28), in the owner's Avida terms (S61), with none of the words S23 removes in Claude's own sentences? The runs are not in your folder: judge the numbers by their agreement with each other and with the scripts.""",
    4: """Cross-examine **the plain-words file** (`S113/3 plain words.md`) against the results (`S113/2 ...`, `.md` and `.json`). The owner is not a programmer. Check: it starts with the direct answer to the owner's question (section 2, S63: "what kind of execution environment can use these machines to progressively learn how to do new things"); every number and statement in it is in the results with the same meaning (no rounding that changes a comparison, nothing stronger than the results, no difference inside the seeds' spread told as a difference); what was tested, what was not and what is unsure are all said; everyday language, every unavoidable technical word explained in one plain sentence before its first use, no codes; the owner's Avida terms used (S61, `S113/the owner's Avida terms.md`), one word for each thing throughout; a concrete example before each general point; it is marked as written before the GLM check; it ends with one next step; no word decision S23 removes in Claude's own sentences (quotations excepted); nothing settled (S28); nothing chosen for the owner (S21). Set it beside `records/plain words 112 ...` for style only.""",
}

INTRO = """# A cross-examination of a measuring job: job {job} of 4, {title}

## 1. What this is

The owner of a theory of explanation and creativity, after logs S111 and S112 ran Avida (a research platform for digital evolution in which Avida programs, each an instruction sequence, execute and replicate on Avida's virtual CPU), asked what kind of Avida execution environment can use these programs to progressively learn how to do new things (section 2, S62 to S64), and approved a test: start every run from the same Avida program, change only the Avida execution environment, and count how many new computational capabilities (Avida's logic tasks) appear in the program population over time. The owner also gave the terms in which the work is to be described (S61; `S113/the owner's Avida terms.md`). All entities are digital programs executing on Avida's virtual CPU; nothing biological is involved.

One agent did the job: it wrote the plan before running (`S113/1 ...`), ran six Avida execution environments with three seeds each for 50,000 updates, counted the computational capabilities over time and measured reuse by instruction ablation, and wrote the results (`S113/2 ...`, `.md` and `.json`) and a plain-words version for the owner (`S113/3 plain words.md`). The exact commands and the scripts are under `runs/` and `scripts/`; the configuration of every environment under `runs/configuration/`; S111's configuration and its build notes (Avida's rules as read from its source) under `runs/`. Avida itself and the raw output (Avida's data files, the saved program populations) are not in your folder. **Your job is to cross-examine that work from one angle** (section 4). Three other agents cross-examine it from other angles at the same time.

Nothing you write changes the theory. What you find is read by one agent after every cross-examination has ended, under the rule in `S113/the rule for reading this cross-examination.md`, and each objection is settled there by argument or by rerunning; findings that stand are applied to corrected copies of the S113 files and to the plain-words file.

Who is who: "the owner" is the person whose theory this is; "Claude" is the agent that did the job. Who made a point decides nothing, only its reasons do."""

TOOLS_TEXT = """## 3. The sandbox and your tools

Your working folder holds only copies. You may Read, Glob and Grep anything in it. **No command runs here**: there is no program in this folder, and every shell command is refused. You write nothing. Avida's source, its binary and the raw output are not here: judge the numbers from the scripts, the configuration and the results.

The files:

| path | what |
|---|---|
| `BRIEF.md` | this brief |
| `S113/1 the plan, written before running.md` | the plan, committed before any measuring run |
| `S113/2 results.md`, `.json` | the results |
| `S113/3 plain words.md` | the plain-words version for the owner, written before this cross-examination |
| `S113/the rule for reading this cross-examination.md` | how your report will be read |
| `S113/the owner's Avida terms.md` | the terms the owner gave (S61) |
| `runs/the exact commands.txt` | every command run, with departures from the plan |
| `runs/the 77 tasks ranked by the fewest nand steps.json` | the difficulty of each task, as the ranking script found it |
| `runs/configuration/` | each environment's environment file (first piece; the growing list also with all levels rewarded) and the events of the pieces |
| `runs/configuration from log S111/` | S111's Avida configuration files, which every S113 run uses unchanged (its `environment.cfg` is S111's, for comparison) |
| `runs/build notes and Avida's rules as read from its source (from log S111).md` | the build, and the rules of Avida, with source lines |
| `scripts/` | the six S113 scripts (the test-processor reading was added after the runs; the table printer copies the results tables from the `.json`) |
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
        rel = 'tests/S113 - GLM cross-examination, job %d, %s.md' % (j['job'], j['title'].replace("'", ''))
        files[rel] = b
        man = {'note': "Log S113, the GLM cross-examination (S56), job %d: the files copied into its sandbox, each checked by "
                       "md5 at the copy; the brief is added as BRIEF.md. No Avida source or binary, no raw output. "
                       "Written by tools/s113x_build.py." % j['job'],
               'files': entries}
        mrel = MAT + '/sandbox manifest, job %d.json' % j['job']
        files[mrel] = json.dumps(man, indent=1, ensure_ascii=False) + '\n'
        jobs_out.append({'job': j['job'], 'name': j['name'], 'tag': j['tag'], 'brief': rel, 'brief_md5': B.md5(b),
                         'manifest': mrel, 'manifest_md5': B.md5(files[mrel])})
        rows.append((j['job'], j['title'], j['tag'], rel, B.words(b), B.md5(b), len(entries)))
    jobs = {'round': 'log S113, the GLM cross-examination (S56)', 'rule': READING_RULE, 'out': OUT,
            'max_pass': 3, 'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'sandbox_root': 's113x_sandboxes', 'home_root': 's113x_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py', 'jobs': jobs_out}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s113x_build.py [--check]')
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
