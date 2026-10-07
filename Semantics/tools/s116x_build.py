#!/usr/bin/env python3
"""s116x_build.py: build the GLM cross-examination of log S116 (the routine runs from GPT 6 Astra's replies: batches 2
and 3 of S115's plan of runs, and FIXED LARGE LIST seed 2 continued from 50,000 to 75,000 updates, as the S113
settlement proposed; decision S61: the owner's Avida terms; decision S56: "Use GLM for cross examination"). Written 30
September 2026 by the one Opus 5.5 agent of log S116: log S113's cross-examination build (tools/s113x_build.py) with its
names, files and briefs changed, and nothing else: round 1's build (tools/s108_build.py) is imported for its helpers only,
never changed; the sandboxed helper (tools/glm_via_claude_code_sandboxed.py) and the shell guard
(tools/glm_sandbox_shell_guard.py) are used unchanged by the runner (tools/s116x_glm_loop.py).

Four GLM jobs at once (S39), each cross-examining the S116 work from one angle:
  (a) whether the runs answer what the plan says they test, and whether the comparisons with S113 are fair;
  (b) the measures and the scripts;
  (c) the results against the plan;
  (d) the plain-words file against the results.
Each sandbox holds copies of the S116 plan, the results (.md and .json), the plain-words file 116, the reading rule, the
owner's Avida terms, the exact commands, S115's plan of runs and its checks of replies 01, 02 and 05, S113's corrected
results and settlement, the S114 restart audit's results, S111's configuration and build notes, the S116 scripts, the
S113 scripts they import, and the reply scripts they run (unchanged copies), plus, per job, the records its angle needs;
NEVER the Avida source or binary, and no raw output (Avida's data files, saved program populations and probe results stay
in the scratch space and are not under Semantics/). There is no program in the sandbox, so the guard refuses every
command: GLM only reads (Read, Glob, Grep) and writes nothing.

  python3 Semantics/tools/s116x_build.py            build the briefs, the four manifests and the job list
  python3 Semantics/tools/s116x_build.py --check    rebuild in memory and compare; writes nothing

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

PRE = "results/S116 Routine runs from Astra's replies - "
READING_RULE = PRE + 'how the GLM cross-examination will be read, written before sending.md'
OUT = PRE + 'GLM cross-examination returns'
MAT = PRE + 'material for the GLM cross-examination'
JOBS_FILE = 'tools/s116x_jobs - S116, GLM cross-examination.json'
CAP = 7000
OWNER = [20, 21, 23, 28, 43, 56, 61, 62, 63, 64, 66, 68]
RUNS111 = 'results/S111 Avida - the runs/'
RUNS = PRE + 'the runs/'
PLAN = PRE + 'how they will be tested, written before running.md'
RES = PRE + 'results.md'
RESJ = PRE + 'results.json'
PLAIN = "plain words/116 What the routine runs from Astra's replies found, in plain words.md"
TERMS = 'records/Semantics - Avida terms, given by the owner.md'
S115 = 'results/S115 Checking the Astra returns/'
S113 = 'results/S113 Which execution environments learn - '
SCRIPTS = ['s116_probe_the_saved_program_populations.py', 's116_count_the_instructions_whose_ablation_lowers_avida_fitness.py',
           's116_read_the_evaluation_banks.py', 's116_compete_a_rare_and_a_common_kind.py',
           's116_continue_fixed_large_list_seed_2.py', 's116_gather_the_results.py',
           's113_run_the_avida_execution_environments.py', 's113_measure_capabilities_in_the_saved_program_populations.py']
REPLY_SCRIPTS = [('reply 01, probe_task_audit.py', 'tools/s115/01/probe_task_audit.py'),
                 ('reply 01, summarize_probes.py', 'tools/s115/01/summarize_probes.py'),
                 ('reply 02, make_experiments.py', 'tools/s115/02/make_experiments.py')]

COMMON = [('S116/1 the plan, written before running.md', PLAN),
          ('S116/2 results.md', RES),
          ('S116/2 results.json', RESJ),
          ('S116/3 plain words.md', PLAIN),
          ('S116/the rule for reading this cross-examination.md', READING_RULE),
          ("S116/the owner's Avida terms.md", TERMS),
          ('runs/the exact commands.txt', RUNS + 'the exact commands.txt'),
          ('S115/00 the plan of runs.md', S115 + '00 What the eight replies offer, and a plan of runs.md'),
          ('S115/01 check of reply 01.md', S115 + '01 Check of reply 01 - measuring what is learned.md'),
          ('S115/02 check of reply 02.md', S115 + '02 Check of reply 02 - evaluation inside the program population.md'),
          ('S115/05 check of reply 05.md', S115 + '05 Check of reply 05 - open-endedness research.md'),
          ('S113/results, after the cross-examination.md', S113 + 'results, after the cross-examination.md'),
          ('S113/the cross-examination, settled.md', S113 + 'the GLM cross-examination, settled.md'),
          ('S114/restart audit, results.md', 'results/S114 Restart audit - results.md'),
          ('runs/the 77 tasks ranked by the fewest nand steps.json',
           S113 + 'the runs/the 77 tasks ranked by the fewest nand steps.json')] + \
         [('runs/configuration from log S111/' + f, RUNS111 + 'configuration/' + f)
          for f in ['avida.cfg', 'environment.cfg', 'instset-heads.cfg', 'default-heads.org']] + \
         [("runs/build notes and Avida's rules as read from its source (from log S111).md",
           RUNS111 + "build notes and Avida's rules as read from its source.md")] + \
         [('scripts/' + s, 'tools/' + s) for s in SCRIPTS] + \
         [('scripts/' + d, src) for d, src in REPLY_SCRIPTS]
EXTRA = {
    1: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md')],
    4: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md'),
        ('records/plain words 113, an earlier plain-words file, for its style.md',
         'plain words/113 Which execution environments learn new things, in plain words.md')],
}
JOBS = [
    dict(job=1, name='the-runs-and-the-comparisons', tag='s116x_glm_a',
         title='whether the runs answer what the plan says they test, and whether the comparisons with S113 are fair'),
    dict(job=2, name='the-measures-and-scripts', tag='s116x_glm_b',
         title='the measures and the scripts'),
    dict(job=3, name='the-results-against-the-plan', tag='s116x_glm_c',
         title='the results against the plan'),
    dict(job=4, name='plain-words', tag='s116x_glm_d', title='the plain-words file against the results'),
]

ANGLE = {
    1: """Cross-examine **whether the runs answer what the plan says they test, and whether the comparisons with S113 are fair**. The owner's question (section 2, S63): "what kind of execution environment can use these machines to progressively learn how to do new things". Read `S116/1 the plan ...`, `S115/00 the plan of runs.md` (sections 3 and 4) and the checks of replies 01, 02 and 05 (section 4 of each), `S113/results, after the cross-examination.md`, `S113/the cross-examination, settled.md` (section 5, the proposed continuation), `S114/restart audit, results.md` (section 5), `runs/the exact commands.txt`, the scripts and the results (`S116/2 ...`). Check, for each batch and the continuation: does what was run measure what the plan says it tests in the owner's question (the probe of every saved S113 program population, its retention tables and reply 05's K; reply 02's six runs and 36 bank assays; the rare-kind competition under COMMON TASKS PAY LESS; FIXED LARGE LIST seed 2 continued to 75,000 in S113's pieces); was each "counts for" and "counts against" fixed before running and applied as fixed, and is any of them too weak to fail (a rule that could not have come out against); is every comparison with S113 fair (the same saved program populations, the same counting as S113 where the plan says so, the S114 cautions carried: COMMON TASKS PAY LESS possibly lowered by the pieces, generations not used, three seeds read through their spread, the continuation's reload caveats); are the two kinds of the competition chosen by the rule written before running, and does a result for one pair say anything about S113's E6; does any sentence say more than the numbers, or settle what the owner left open (S28)?""",
    2: """Cross-examine **the measures and the scripts**. Read the S116 scripts in `scripts/` (the probe driver, the K count, the bank reader, the competition, the continuation), the S113 scripts they import (unchanged), and the reply scripts they run unchanged (`scripts/reply 01, probe_task_audit.py`, `scripts/reply 01, summarize_probes.py`, `scripts/reply 02, make_experiments.py`, which writes reply 02's suite, bank preparer and bank summariser), with `runs/the exact commands.txt` and the plan (`S116/1 ...`). Check: does each script compute what the plan defines (a task performed on all 8 probe inputs and viable; present and common at 10%; the never-rewarded arithmetic set; ever seen, kept at every save, present after a gap; the reward history made from S113's environments; logic_high summarised by the same rule; K as lethal plus detrimental single instruction ablations under S113's FIXED GRADED environment on the 100 most common sequences, weighted by programs; the response patterns and shares read from reply 02's bank summaries; A and B chosen by the written rule, the world filled at the written shares, instruction changes off, resources started at S113's levels, A's share counted from the saves; the continuation calling S113's runner and measuring function unchanged, with only their output folders redirected); the columns read from Avida's files as the scripts read them; that every Avida process runs under a time limit at the lowest priority; that nothing is written into S113's folder. What do the limits leave open (8 inputs; 10 saves 5,000 updates apart; 100 sequences for K; one pair, 2,000 updates, three placements for the competition; one seed for the continuation)? Is each stated where a result leans on it? The raw output is not in your folder: judge the numbers by their consistency with the code and with each other.""",
    3: """Cross-examine **the results against the plan**. Read the results (`S116/2 results.md` and `S116/2 results.json`) and the plan (`S116/1 ...`), with `runs/the exact commands.txt`, and S113's results where the results compare with them. Check: is every number in the `.md` the number in the `.json`; is each reading of the plan (B2.1 to B2.5, B3a.1 and B3a.2, B3b.1 and B3b.2, E.1 and E.2) reported with the plan's rule and the verdict its rule gives; is any verdict reached by a rule other than the plan's, or any "for" claimed where the plan's rule gives "unclear"; is every departure from the plan recorded, with its reason; is the CPU time reported and within the stated limit; is what was not tested said; does any sentence say more than its numbers (a difference inside the seeds' spread read as a difference; one pair or one seed read as a general finding); in the section on the owner's question, is everything given as observations, settling nothing (S28), in the owner's Avida terms (S61), with none of the words S23 removes in Claude's own sentences? The raw output is not in your folder: judge the numbers by their agreement with each other and with the scripts.""",
    4: """Cross-examine **the plain-words file** (`S116/3 plain words.md`) against the results (`S116/2 ...`, `.md` and `.json`). The owner is not a programmer. Check: it starts with what happened and what it means for the owner's question (section 2, S63); every number and statement in it is in the results with the same meaning (no rounding that changes a comparison, nothing stronger than the results, no difference inside the seeds' spread told as a difference); what was tested, what was not and what is unsure are all said; everyday language, every unavoidable technical word explained in one plain sentence before its first use, no codes; the owner's Avida terms used (S61, `S116/the owner's Avida terms.md`), one word for each thing throughout; a concrete example before each general point; it is marked as written before the GLM check; it ends with one next step; no word decision S23 removes in Claude's own sentences (quotations excepted); nothing settled (S28); nothing chosen for the owner (S21). Set it beside `records/plain words 113 ...` for style only.""",
}

INTRO = """# A cross-examination of a measuring job: job {job} of 4, {title}

## 1. What this is

The owner of a theory of explanation and creativity asked what kind of Avida execution environment can use Avida programs to progressively learn how to do new things (section 2, S63). Avida is a research platform for digital evolution in which Avida programs, each an instruction sequence, execute and replicate on Avida's virtual CPU. Log S113 ran six Avida execution environments (three seeds each, 50,000 updates, in pieces of 1,000 updates with the program population saved and reloaded between pieces) and counted the computational capabilities (Avida's logic tasks) in the program population over time; its results were cross-examined and corrected (`S113/...`). Log S114 audited what the pieces do (`S114/...`). Log S115 checked eight replies of another model, GPT 6 Astra, and wrote a plan of runs (`S115/00 ...`). The owner gave the terms in which the work is described (S61; `S116/the owner's Avida terms.md`). All entities are digital programs executing on Avida's virtual CPU; nothing biological is involved.

One agent did log S116: it wrote the plan before running (`S116/1 ...`), then ran the routine part of S115's plan: (batch 2) a probe of every program population S113 saved, with one reply's probe battery, its retention tables and another reply's count of instructions whose ablation lowers Avida fitness; (batch 3) one reply's six runs where programs choose whom to give energy to, with their 36 assays, and a competition between two kinds of program from S113's COMMON TASKS PAY LESS, one rare and one common; and (the continuation) S113's one run still rising at 50,000 updates, continued to 75,000 in S113's own pieces. It wrote the results (`S116/2 ...`, `.md` and `.json`) and a plain-words version for the owner (`S116/3 plain words.md`). The exact commands and the scripts are under `runs/` and `scripts/`. Avida itself and the raw output (Avida's data files, saved program populations, probe results) are not in your folder. **Your job is to cross-examine that work from one angle** (section 4). Three other agents cross-examine it from other angles at the same time.

Nothing you write changes the theory. What you find is read by one agent after every cross-examination has ended, under the rule in `S116/the rule for reading this cross-examination.md`, and each objection is settled there by argument or by rerunning; findings that stand are applied to corrected copies of the S116 files and to the plain-words file.

Who is who: "the owner" is the person whose theory this is; "Claude" is the agent that did the job. Who made a point decides nothing, only its reasons do."""

TOOLS_TEXT = """## 3. The sandbox and your tools

Your working folder holds only copies. You may Read, Glob and Grep anything in it. **No command runs here**: there is no program in this folder, and every shell command is refused. You write nothing. Avida's source, its binary and the raw output are not here: judge the numbers from the scripts, the configuration and the results.

The files:

| path | what |
|---|---|
| `BRIEF.md` | this brief |
| `S116/1 the plan, written before running.md` | the plan, committed before any measuring run |
| `S116/2 results.md`, `.json` | the results |
| `S116/3 plain words.md` | the plain-words version for the owner, written before this cross-examination |
| `S116/the rule for reading this cross-examination.md` | how your report will be read |
| `S116/the owner's Avida terms.md` | the terms the owner gave (S61) |
| `runs/the exact commands.txt` | every command run, with departures from the plan |
| `S115/` | S115's plan of runs and its checks of replies 01, 02 and 05 |
| `S113/` | S113's results after its cross-examination, and the settlement of that cross-examination |
| `S114/restart audit, results.md` | what S113's pieces do, measured against unbroken runs for two environments |
| `runs/the 77 tasks ranked by the fewest nand steps.json` | S113's task levels (its reward values) |
| `runs/configuration from log S111/` | S111's Avida configuration files, used by S113 and by the S116 runs that use S113's settings |
| `runs/build notes and Avida's rules as read from its source (from log S111).md` | the build, and the rules of Avida, with source lines |
| `scripts/` | the S116 scripts, the two S113 scripts they import, and the reply scripts they run unchanged |
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
        rel = 'tests/S116 - GLM cross-examination, job %d, %s.md' % (j['job'], j['title'].replace("'", ''))
        files[rel] = b
        man = {'note': "Log S116, the GLM cross-examination (S56), job %d: the files copied into its sandbox, each checked by "
                       "md5 at the copy; the brief is added as BRIEF.md. No Avida source or binary, no raw output. "
                       "Written by tools/s116x_build.py." % j['job'],
               'files': entries}
        mrel = MAT + '/sandbox manifest, job %d.json' % j['job']
        files[mrel] = json.dumps(man, indent=1, ensure_ascii=False) + '\n'
        jobs_out.append({'job': j['job'], 'name': j['name'], 'tag': j['tag'], 'brief': rel, 'brief_md5': B.md5(b),
                         'manifest': mrel, 'manifest_md5': B.md5(files[mrel])})
        rows.append((j['job'], j['title'], j['tag'], rel, B.words(b), B.md5(b), len(entries)))
    jobs = {'round': 'log S116, the GLM cross-examination (S56)', 'rule': READING_RULE, 'out': OUT,
            'max_pass': 3, 'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'sandbox_root': 's116x_sandboxes', 'home_root': 's116x_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py', 'jobs': jobs_out}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s116x_build.py [--check]')
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
