#!/usr/bin/env python3
"""s112x_build.py: build the GLM cross-examination of log S112 (decision S60: of the Avida programs that performed the
logic tasks, what instruction ablation had to remove for the task performance to stop, and what those instructions are
when executed on Avida's virtual CPU, relative to the Avida execution environment; decision S61: the owner's Avida
terms; decision S56: "Use GLM for cross examination"). Written 30 September 2026 by the one Opus 5.5 agent of log S112:
log S111's cross-examination build (tools/s111x_build.py) with its names, files and briefs changed, and nothing else:
round 1's build (tools/s108_build.py) is imported for its helpers only, never changed; the sandboxed helper
(tools/glm_via_claude_code_sandboxed.py) and the shell guard (tools/glm_sandbox_shell_guard.py) are used unchanged by
the runner (tools/s112x_glm_loop.py).

Four GLM jobs at once (S39), each cross-examining the S112 work from one angle:
  (a) does the answer answer the owner's two questions exactly;
  (b) the minimal-removal search (instruction ablation) and its limits;
  (c) the circuits and their canonical forms against the traces;
  (d) the plain-words file against the results.
Each sandbox holds copies of the S112 plan, the results (.md and .json), the plain-words file 112, the reading rule,
the owner's Avida terms, the exact commands, S111's configuration files and build notes (Avida's rules as read from its
source), and the five S112 scripts, plus, per job, the records its angle needs; NEVER the Avida source or binary, and
no raw output (traces, ablation lists: those stay in the scratch space and are not under Semantics/). There is no
program in the sandbox, so the guard refuses every command: GLM only reads (Read, Glob, Grep) and writes nothing.

  python3 Semantics/tools/s112x_build.py            build the briefs, the four manifests and the job list
  python3 Semantics/tools/s112x_build.py --check    rebuild in memory and compare; writes nothing

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

PRE = 'results/S112 What the evolved sums are - '
READING_RULE = PRE + 'how the GLM cross-examination will be read, written before sending.md'
OUT = PRE + 'GLM cross-examination returns'
MAT = PRE + 'material for the GLM cross-examination'
JOBS_FILE = 'tools/s112x_jobs - S112, GLM cross-examination.json'
CAP = 7000
OWNER = [20, 21, 23, 28, 43, 56, 60, 61]
RUNS111 = 'results/S111 Avida - the runs/'
RUNS = PRE + 'the runs/'
PLAN = PRE + 'how it will be found, written before running.md'
RES = PRE + 'what had to be removed and what it is.md'
RESJ = PRE + 'what had to be removed and what it is.json'
PLAIN = 'plain words/112 What the evolved sums actually are, in plain words.md'
TERMS = 'records/Semantics - Avida terms, given by the owner.md'
SCRIPTS = ['s112_run_programs_in_avidas_test_processor.py', 's112_read_what_the_programs_compute_from_avidas_traces.py',
           's112_find_minimal_removals.py', 's112_test_what_the_sums_depend_on_in_the_environment.py',
           's112_summarise_what_had_to_be_removed_and_what_it_is.py']

COMMON = [('S112/1 the plan, written before running.md', PLAN),
          ('S112/2 what had to be removed and what it is.md', RES),
          ('S112/2 what had to be removed and what it is.json', RESJ),
          ('S112/3 plain words.md', PLAIN),
          ('S112/the rule for reading this cross-examination.md', READING_RULE),
          ("S112/the owner's Avida terms.md", TERMS),
          ('runs/the exact commands.txt', RUNS + 'the exact commands.txt')] + \
         [('runs/configuration/' + f, RUNS111 + 'configuration/' + f)
          for f in ['avida.cfg', 'environment.cfg', 'instset-heads.cfg', 'default-heads.org']] + \
         [("runs/build notes and Avida's rules as read from its source (from log S111).md",
           RUNS111 + "build notes and Avida's rules as read from its source.md")] + \
         [('scripts/' + s, 'tools/' + s) for s in SCRIPTS]
EXTRA = {
    1: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md'),
        ('records/S111 results, after its cross-examination.md',
         'results/S111 Avida - the three properties measured, after the cross-examination.md')],
    4: [("records/the owner's decisions.md", 'records/Semantics - Decisions.md'),
        ('records/plain words 111, an earlier plain-words file, for its style.md',
         "plain words/111 A program with the three properties - Avida's digital organisms measured, in plain words.md")],
}
JOBS = [
    dict(job=1, name='the-owners-two-questions', tag='s112x_glm_a',
         title="whether the answer answers the owner's two questions exactly"),
    dict(job=2, name='the-minimal-removal-search', tag='s112x_glm_b',
         title='the minimal-removal search (instruction ablation) and its limits'),
    dict(job=3, name='circuits-and-canonical-forms', tag='s112x_glm_c',
         title='the circuits and their canonical forms against the traces'),
    dict(job=4, name='plain-words', tag='s112x_glm_d', title='the plain-words file against the results'),
]

ANGLE = {
    1: """Cross-examine **whether the answer answers the owner's two questions exactly** (section 2, S60): "Of the of machines that could do rudimentary math, what needed to be removed in order for them to stop doing that math", and "what that evolved information actually is, given the environment it was instantiated in", setting aside that the Avida programs were produced by digital evolution to earn Avida fitness. Read `S112/1 the plan ...`, `S112/2 what had to be removed and what it is.md` (and `.json`) and `S112/the owner's Avida terms.md`. For each of the nine logic tasks: is "what had to be removed" given exactly (per Avida program, the minimal instruction ablations that stop the task performance while program replication continues; across programs, what those required instructions share), or only approximately, and where it is approximate is that said? Is "what it is" given as it stands in the Avida execution environment (the instruction set's meanings, the input and output channel, the numbers handed in), without leaning on the digital evolution or Avida fitness that produced it? Do the execution-environment tests show what the results say they show? Does any sentence say more than its numbers show, or settle what the owner left open (S28)? Is every departure from the plan recorded with its reason? Does the file keep to the owner's Avida terms (S61) and, in its own sentences, to S23? Set it beside `records/S111 results ...` only for what S111 left open (single instruction ablations missing some routes; instruction counts without what they do).""",
    2: """Cross-examine **the minimal-removal search (instruction ablation) and its limits**. Read `scripts/s112_find_minimal_removals.py`, `scripts/s112_run_programs_in_avidas_test_processor.py`, `scripts/s112_summarise_...`, `runs/the exact commands.txt`, `runs/configuration/`, and the results (`S112/2 ...` `.md` and `.json`), against the plan (`S112/1 ...`, section 2). Check: does the code do what the plan and the results say (ablation by `nop-X`; "stops the task" meaning the program still replicates in the test processor and no longer performs the task; exhaustive single sites; exhaustive pairs among sites whose single ablation leaves replication, kept only when neither site alone stops the task; the irreducible-set search from the routes' sites, its random orders and passes, its fall-back start; the triples of the most common sequence per run; the traces with a replication-required site ablated)? Are the counts in the results consistent with each other and with the code (by distinct instruction sequence and by Avida program)? What do the limits leave open: sets of three or more found only by a greedy search, not all of them and not surely the smallest; ablation by `nop-X` only (not deletion, which shifts positions); task performance judged only in the test processor on its fixed inputs; replication-required instructions, whose ablation stops every task by stopping replication, set apart. Is each limit stated where a result leans on it? The runs are not in your folder: judge the numbers by their consistency with the code and with each other.""",
    3: """Cross-examine **the circuits and their canonical forms against the traces**. Read `scripts/s112_read_what_the_programs_compute_from_avidas_traces.py` (how Avida's TRACE is followed: which registers and stack places each instruction reads and writes, with the Avida source functions it names; the check of every step against the trace; the logic id rule of Avida's task check; the routes; the circuit as a table of distinct parts with movers skipped and constant parts folded; the reduced form; the canonical renaming of the three inputs; the generality check; the predictions for the execution-environment tests), `runs/build notes and Avida's rules as read from its source (from log S111).md`, `runs/configuration/instset-heads.cfg`, and the results (`S112/2 ...`, with the worked examples in the `.json`). Check: are the register and stack effects of each instruction as Avida's source gives them (as far as the build notes and the script's own citations let you judge), and does the zero count of steps where the replay differs from the trace bear that out? Is the logic id computation Avida's rule? Does each worked example, step by step, compute what it is said to compute (recompute the values from the instructions and the three inputs given)? Is the canonical form canonical (two Avida programs executing the same circuit on renamed inputs get the same form; two different circuits never do)? Do the reduced forms change only what their rules say? Is counting "distinct circuits" and "distinct instruction sequences realising the same circuit" done as stated, and are circuits with arithmetic (add, sub, inc, dec) described correctly as what they compute bit by bit? The traces themselves are not in your folder.""",
    4: """Cross-examine **the plain-words file** (`S112/3 plain words.md`) against the results (`S112/2 ...`, `.md` and `.json`). The owner is not a programmer. Check: it starts with the direct answer to the owner's two questions (section 2, S60); every number and statement in it is in the results with the same meaning (no rounding that changes a comparison, nothing stronger than the results); what was tested, what was not and what is unsure are all said; everyday language, every unavoidable technical word explained in one plain sentence before its first use, no codes; the owner's Avida terms used (S61, `S112/the owner's Avida terms.md`), one word for each thing throughout; a concrete example before each general point; it is marked as written before the GLM check; it ends with one next step; no word decision S23 removes in Claude's own sentences (quotations excepted); nothing settled (S28); nothing chosen for the owner (S21). Set it beside `records/plain words 111 ...` for style only.""",
}

INTRO = """# A cross-examination of a measuring job: job {job} of 4, {title}

## 1. What this is

The owner of a theory of explanation and creativity asked, after log S111 ran Avida (a research platform for digital evolution in which Avida programs, each an instruction sequence, execute and replicate on Avida's virtual CPU): of the Avida programs that performed small logic tasks, what had to be removed for them to stop performing them, and what that evolved information actually is, given the Avida execution environment it was instantiated in, setting aside that it was produced by digital evolution (section 2, S60). The owner also gave the terms in which the work is to be described (S61; `S112/the owner's Avida terms.md`). All entities are digital programs executing on Avida's virtual CPU; nothing biological is involved.

One agent did the job: it wrote the plan before running (`S112/1 ...`), ran instruction ablations and Avida's own traces on every distinct instruction sequence alive at the end of the nine S111 runs, and execution-environment tests, and wrote the results (`S112/2 ...`, `.md` and `.json`) and a plain-words version for the owner (`S112/3 plain words.md`). The exact commands and the scripts are under `runs/` and `scripts/`; S111's configuration and its build notes (Avida's rules as read from its source) under `runs/`. Avida itself and the raw output (traces, ablation lists) are not in your folder. **Your job is to cross-examine that work from one angle** (section 4). Three other agents cross-examine it from other angles at the same time.

Nothing you write changes the theory. What you find is read by one agent after every cross-examination has ended, under the rule in `S112/the rule for reading this cross-examination.md`, and each objection is settled there by argument or by rerunning; findings that stand are applied to corrected copies of the S112 files and to the plain-words file.

Who is who: "the owner" is the person whose theory this is; "Claude" is the agent that did the job. Who made a point decides nothing, only its reasons do."""

TOOLS_TEXT = """## 3. The sandbox and your tools

Your working folder holds only copies. You may Read, Glob and Grep anything in it. **No command runs here**: there is no program in this folder, and every shell command is refused. You write nothing. Avida's source, its binary and the raw output are not here: judge the numbers from the scripts, the configuration and the results.

The files:

| path | what |
|---|---|
| `BRIEF.md` | this brief |
| `S112/1 the plan, written before running.md` | the plan, committed before any measuring run (with a dated note on the terms at its top) |
| `S112/2 what had to be removed and what it is.md`, `.json` | the results |
| `S112/3 plain words.md` | the plain-words version for the owner, written before this cross-examination |
| `S112/the rule for reading this cross-examination.md` | how your report will be read |
| `S112/the owner's Avida terms.md` | the terms the owner gave (S61) |
| `runs/the exact commands.txt` | every command run, with departures from the plan |
| `runs/configuration/` | Avida's configuration files as used in log S111 (the S112 scripts change only what they say) |
| `runs/build notes and Avida's rules as read from its source (from log S111).md` | the build, and the rules of Avida, with source lines |
| `scripts/` | the five S112 scripts |
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
        rel = 'tests/S112 - GLM cross-examination, job %d, %s.md' % (j['job'], j['title'].replace("'", ''))
        files[rel] = b
        man = {'note': "Log S112, the GLM cross-examination (S56), job %d: the files copied into its sandbox, each checked by "
                       "md5 at the copy; the brief is added as BRIEF.md. No Avida source or binary, no raw output. "
                       "Written by tools/s112x_build.py." % j['job'],
               'files': entries}
        mrel = MAT + '/sandbox manifest, job %d.json' % j['job']
        files[mrel] = json.dumps(man, indent=1, ensure_ascii=False) + '\n'
        jobs_out.append({'job': j['job'], 'name': j['name'], 'tag': j['tag'], 'brief': rel, 'brief_md5': B.md5(b),
                         'manifest': mrel, 'manifest_md5': B.md5(files[mrel])})
        rows.append((j['job'], j['title'], j['tag'], rel, B.words(b), B.md5(b), len(entries)))
    jobs = {'round': 'log S112, the GLM cross-examination (S56)', 'rule': READING_RULE, 'out': OUT,
            'max_pass': 3, 'effort': 'medium', 'context_1m': True, 'attempts': 6, 'max_rejects': 3, 'deadline': 7200,
            'sandbox_root': 's112x_sandboxes', 'home_root': 's112x_homes',
            'helper': 'tools/glm_via_claude_code_sandboxed.py', 'jobs': jobs_out}
    files[JOBS_FILE] = json.dumps(jobs, indent=1, ensure_ascii=False) + '\n'
    return files, rows


def main():
    a = sys.argv[1:]
    B.need(set(a) <= {'--check'}, 'usage: s112x_build.py [--check]')
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
