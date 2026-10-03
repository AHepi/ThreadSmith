# The Sonnet harness

Decision S42 asks how and when to use Sonnet. Decision S16 still stands: "Use Sonnet when running a harness or a workflow. Analysis is not it's strength". This folder is that harness. The reasons, the test results and the rules from round 4 are in `results/S105 note - how and when to use Sonnet, with a harness.md`.

## What Sonnet does here

Sonnet runs **one narrow job at a time**, from a written task spec. It:

- runs the scripts the spec names;
- copies what a spec asks it to copy;
- fills in a sheet the program has already laid out;
- hands back the JSON the scripts print.

A second agent then re-runs the spec's checks by script. Anything that fails, or does not match, goes to Opus.

## What Sonnet never does

- Judge whether a finding holds, rule on an item, or weigh two arguments.
- Write maths, code for the model, a fix, or a text change.
- Review anything, including the critical review of a round.
- Write into the theory texts, `authority/`, `records/`, or any file of a round. It writes only in the scratchpad, unless a spec names a new file.
- Open a key file, call GLM or any other outside model, or relaunch a run that needs a key.
- Commit or push, unless the job is the commit job and Opus has written the message and the file list.

## Which jobs are Sonnet's

| job | who | the harness |
|---|---|---|
| run the claim suite and compare it with a record | Sonnet | `run_claims.py` |
| apply text changes, check each byte for byte, compare md5s | Sonnet | `apply_changes.py`, `md5_check.py` |
| count words outside formulas; scan for the owner's forbidden words | Sonnet runs the scan; Opus rules on any new hit | `text_scan.py` |
| check quotations against the text | Sonnet | `tabulation.py quote` |
| key grep before a commit | Sonnet | `key_grep.py` |
| commit and push the files named | Sonnet; Opus writes the message and the file list | `git_commit.py` |
| watch a run | Sonnet | `watch_run.py` |
| relaunch a run after a restart | Sonnet if the run needs no key; the orchestrator if it does | `watch_run.py` says which |
| check md5s | Sonnet | `md5_check.py` |
| three-way merge of the model copies | Sonnet merges; every conflict goes to Opus | `merge_models.py` |
| build briefs from templates | Sonnet runs the build and its `--check`; Opus writes what a brief asks | the round's build script; `records.py render` |
| tabulate the replies (extraction) | the program lays out and pre-fills the sheet from the replies' headers; Sonnet marks each row and corrects the blocks; Opus checks every row not marked "challenges" | `tabulation.py` |
| draft a log entry, Status, README or INDEX lines | Sonnet drafts from facts Opus wrote; Opus reads every draft before it goes in | `records.py` |
| checkers, integration decisions, critical review, second checker, reading rules, owner questions, plain-words files, lessons | Opus only | none |

## How to run a job

1. **Pick or write a task spec.** The examples are in `specs/`: the tests on round 2.
2. **Make its brief.** This runs nothing; it prints the exact commands and the agent's part:

   ```
   python3 -B Semantics/tools/sonnet_harness/run_task.py "<spec>" --phase brief --run <label>
   ```

3. **Run the Workflow.** Give `workflow/sonnet_jobs.workflow.js` to the Workflow tool with `args: {jobs: [<brief>, ...], after: [<brief>, ...]}`. For each job it runs:
   - one Sonnet worker;
   - one Sonnet verifier, which re-runs the checks by script;
   - one Opus agent when the job fails, or the worker's and the verifier's digests differ;
   - one Opus check for every extraction sheet.

   Specs under `after` run once every job has ended, for example a comparison with known answers.
4. **Read the result.** Each job leaves `result.<phase>.json` in its folder under the scratchpad's `sonnet_harness_tests/<label>/`. Earlier results are kept, numbered, and so is each version the agent handed in (`.attemptN`).

**Without the Workflow tool**, a job with no agent part runs by hand:

```
python3 -B run_task.py "<spec>" --phase all --run <label>
```

A long job starts with `--background`, then `--wait 540`.

## The scripts

Each prints one JSON object. It exits 0 when that object's `ok` is true, 1 when it is false, and 2 when it refused to run.

- `hcommon.py`: what the scripts share.
  - Paths: a script may read anything but a key file, and writes only in the scratchpad, or a new file where a flag allows it.
  - The rule for words outside formulas: `\( \)` and `\[ \]` are stripped, as round 2's appliers do.
- `run_task.py`: runs one spec, in the phases brief, validate, run, check and all.
- `run_claims.py`: runs the suite with `PYTHONHASHSEED=0 python3 -B -m model.run --no-write --brief` from the model's folder. It:
  - reads each claim and each part;
  - compares them with a record;
  - checks by md5 that nothing in the model's folder changed.
- `apply_changes.py`: applies text changes with round 2's rules. Only the kinds delete, formal and pointer are allowed. It:
  - refuses a change whose span is not unique, and two changes that overlap;
  - holds a change marked as waiting;
  - checks each change byte for byte, and undoes it to check that the line comes back;
  - never writes over a file;
  - runs the scans afterwards.
- `text_scan.py`: counts words, and words outside formulas. It runs:
  - the S95 residue families (from `tests/S95 Scrub - scripts/scrub_apply.py`);
  - the S96 physical words (from `tests/S96 Repair - scripts/repair_apply.py`);
  - a check that no heading, defined term or tag is lost.
- `md5_check.py`: checks files against md5s.
- `key_grep.py`: the key grep the orchestrator gives. It prints only the names of the files that match.
- `git_commit.py`: in this order:
  - the key grep;
  - waits while `.git/index.lock` exists;
  - `git add -- <paths>`, then `git commit -- <paths>`;
  - checks that the commit holds only those paths;
  - pushes;
  - if the push is refused, `git pull --no-rebase` and one more push.

  It never resolves a merge conflict.
- `merge_models.py`: `git merge-file`, file by file, against the committed program. It lists conflicts and never resolves them.
- `watch_run.py`: shows whether a run's process is alive, and only its progress lines.
- `tabulation.py`: the mechanical half of tabulating. Its commands:
  - `items` reads the items from a brief;
  - `blocks` numbers the fenced proposal blocks of a reply and copies their text byte for byte;
  - `quote` finds each quotation in the text;
  - `sheet` lays out the rows to fill; with `--prefill` it fills what the replies' bold headers give (passages, blocks, 'nothing to add');
  - `check` checks a filled sheet;
  - `fill` puts in the wordings by program, and every quotation with the lines where it stands;
  - `opus` reads a tabulation in round 2's form;
  - `compare` compares a sheet with Opus's rows.
- `records.py`:
  - `render` fills a template;
  - `check` lists every number, id, md5, commit or file name in a draft that is not in the facts file. It also checks the S23 words and the word count.

## The task spec

A task spec is a JSON file with `"spec": "sonnet-harness task v1"`, and these fields:

- `id`, `job`, `purpose`.
- `kind`: `mechanical`, `extraction` or `records`.
- `out_dir`: always under `{TEST_ROOT}/{RUN}/`.
- `inputs`: each path with its md5. The run stops if one differs.
- `steps`: the commands run before the agent's part.
- `agent` (extraction and records only):
  - `read`: the only files it may open;
  - `write`: the one file it writes;
  - `instructions`: short and concrete;
  - `output_schema`: the JSON schema of that file.
- `check_steps`: the commands run after the agent's part.
- `checks`: each has `name`, `file` and `path`, and one of `equals`, `in`, `lte`, `gte`, `empty`, `nonempty` or `length_equals`.
- `on_fail`.
- `never`: the list of what the agent must not do.

Each command is an `argv` list, never a shell line, with its own `timeout_s`, and its JSON is saved under `save`.

Placeholders: `{PY}`, `{H}`, `{SEM}`, `{REPO}`, `{OUT}`, `{TEST_ROOT}`, `{RUN}`.

A known answer that the agent must not see goes in a separate spec, run under `after` (lesson S2).

## What Opus still checks

- **Tabulation:** every row not marked "challenges". A missed challenge keeps an item from its checker; an extra one costs a checker a paragraph. Also every block cited under more than one item.
- **Records:** every draft, before it goes into the records. The check catches an added fact. It does not catch a fact from the file put in the wrong place.
- **Scans:** every new hit.
- **Merges:** every conflict.
- **Any failure or mismatch:** the Workflow sends it to Opus.
