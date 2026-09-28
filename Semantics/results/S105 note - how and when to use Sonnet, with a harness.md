# S105 note: how and when to use Sonnet, with a harness

*A fresh Opus 5.5 agent wrote this on 28 September 2026, answering decision S42 within decision S16. It is terse, by decision S40. It uses round 2's finished files only. No theory text, no round's file and no record was written; round 3's files were neither read nor touched.*

## 1. The rule

- **S16** stands: "Use Sonnet when running a harness or a workflow. Analysis is not it's strength".
- **S42**: "figure out how and when to use Sonnet. You may have to build it a harness to work effectively."

**Sonnet's work**: bounded jobs, done from a written spec by running scripts. A script or a second agent can check each result.

**Opus's work**:
- weighing arguments;
- deciding whether a finding holds;
- writing a fix, in maths, code or text;
- reviewing;
- writing what an agent is asked.

## 2. Job by job

The marks in the "who" column:

- **S**: Sonnet, through the harness.
- **S+O**: Sonnet, with an Opus check.
- **O**: Opus only.

| recurring job | kind | who | what the harness fixes | what Opus still does |
|---|---|---|---|---|
| run the claim suite, compare with the record | mechanical | S | `run_claims.py`: <br>• the fixed command (PYTHONHASHSEED=0, `-B`, `--no-write`); <br>• a comparison claim by claim and part by part; <br>• md5 of the model folder before and after | reads any difference |
| apply text changes, check each byte for byte | mechanical | S | `apply_changes.py`: round 2's rules, made general; never writes over a file | chooses the changes, and what is held |
| compare md5s | mechanical | S | `md5_check.py` | none |
| count words outside formulas; scan for forbidden words | mechanical | S+O | `text_scan.py`: reuses S95 FAMILIES and S96 PHYS; reports hits | rules on every new hit |
| check quotations against the text | mechanical | S | `tabulation.py quote` and `fill` | rules on a quotation that is not found |
| key grep before commits | mechanical | S | `key_grep.py`: file names only, never the match | none |
| commit and push | mechanical | S+O | `git_commit.py`: <br>• key grep; <br>• `index.lock` wait; <br>• `git commit -- <paths>`; <br>• the commit holds only the paths named; <br>• pull `--no-rebase` and push once more | writes the message and the file list; resolves any merge conflict |
| watch runs; relaunch after a restart | mechanical | S+O | `watch_run.py`: <br>• shows progress lines only; <br>• the state is running, ended, or stopped without ending | relaunches every run that needs a key (GLM): the orchestrator |
| three-way merge of the model copies | mechanical | S+O | `merge_models.py`: `git merge-file` per file; lists conflicts and never resolves them | every conflict |
| build briefs from templates | mechanical | S+O | the round's build script and its `--check`; `records.py render` | writes what the brief asks and the template |
| tabulate the replies | extraction | S+O | `tabulation.py`: <br>• items from the brief; <br>• blocks numbered and copied byte for byte; <br>• rows pre-filled from the replies' bold headers; <br>• quotations looked up; <br>• a check of the filled sheet | reads every row not marked "challenges"; every block cited under two items |
| log entry; Status, README and INDEX lines | records | S+O | `records.py check`: every number, id, md5, commit and file name must stand in the facts Opus wrote | writes the facts; reads every draft; commits it |
| the three area checkers; integration decisions; critical review; second checker; reading rules; owner questions; plain-words files; lessons | analysis | O | none | all |

## 3. The harness

It is in `tools/sonnet_harness/`; the README there is in plain words.

- **Scripts** (stdlib only; each prints one JSON object; exit 0 ok, 1 not ok, 2 refused):
  - `run_task`, `run_claims`, `apply_changes`, `text_scan`, `md5_check`, `key_grep`, `git_commit`;
  - `merge_models`, `watch_run`, `tabulation`, `records`, `workflow_args`, `report_tests`;
  - `hcommon`, what the scripts share.

  Every script:
  - writes only in the scratchpad, or, where a flag allows, a new file in `Semantics/`, never in `authority/` or `records/`;
  - refuses any path that looks like a key file;
  - passes no environment variable named key, token or secret to the programs it runs.
- **Task spec** (JSON, `"spec": "sonnet-harness task v1"`):
  - `id`, `job`, `kind`, `purpose`;
  - `out_dir`, under `{TEST_ROOT}/{RUN}/`;
  - `inputs`, each with its md5;
  - `steps`, then `agent` (`read`, `write`, `instructions`, `output_schema`), then `check_steps`, each command an argv list with a deadline;
  - `checks` (`equals`, `in`, `lte`, `gte`, `empty`, `nonempty`, `length_equals`);
  - `on_fail`, `never`.

  `run_task.py` has the phases brief, validate, run, check and all, and `--background` / `--wait` for long runs. It keeps every result, and every version the agent hands in.

  An answer the agent must not see goes in a separate spec (lesson S2).
- **Workflow**: `workflow/sonnet_jobs.workflow.js`. For each spec it runs:
  1. one Sonnet worker, given one job (`model: 'sonnet'`, schema-bound result);
  2. one fresh Sonnet verifier, which re-runs the spec's checks by script (`--as-verifier`). The job passes only if both are ok and their digests are equal.
  3. an Opus agent on any failure or mismatch, which says the cause and does not fix it;
  4. an Opus check of every extraction sheet (rows not marked "challenges", passages missed), written to `opus_check.json`.

  Specs under `after` run once every job has ended. The script was dry-run under node with stub hooks: it parses, and both the pass path and the escalation path work.

## 4. Tests on round 2's finished work

### 4.1 What this agent ran: the harness on known answers, no Sonnet

| test | known answer | result | time |
|---|---|---|---|
| (i) claim suite, `model after round 2/`, scale 4, cap 45 s | 105 hold, 3 counterexamples, 7 not tested, of 115 (answers record §2) | **matched**: <br>• 115 of 115 claims, every part (label, kind, status), equal to `formal claims, after round 2.json` `after_s41`; <br>• the counterexamples are FC18, FC23 and FC63; <br>• model folder unchanged (md5, no `__pycache__`); <br>• independent re-run of 9 claims: equal; <br>• worker and verifier digests equal | 409–414 s; re-run 34 s |
| (ii) text changes: `text changes after the review.json`, then `… for the owner's answers.json`, from tests/103 | 735ec1e8256cc6a251715a031944ea65, then bc14045aae3139df710d8339a9c1c81b | **matched** both: <br>• 43 applied on 32 lines, then 5 on 4; none refused or held; <br>• words outside formulas 15,611 → 15,409 → 15,388, as recorded; <br>• S95: 3 new hits (L393 "accepted", as the integration report says), 0 on S23's list; S96: 0 | 0.6 s |
| merge of the three area copies (additional) | integration report §1: one textual conflict, `claims_a.py` FC14 | **matched**: <br>• 14 files, 7 changed; <br>• `claims_a.py` has 1 conflict hunk (FC14 path fallback, areas 1 and 2); <br>• `core.py` and `claims_b.py` merge clean; <br>• `claims_area1.py`, `harness.py` and `run.py` come from area 1, `phys.py` from area 3 | < 1 s |
| (iii) part 12: the machinery | Opus's rows (tabulation §2, part 12) | <br>• 31 items read from the brief: every one of Opus's; <br>• 16 blocks (Mimo 9, GLM 7), with the same ids and reply lines as Opus's; <br>• Opus's 16 printed wordings are byte-exact with the replies; <br>• Opus's rows given back as a sheet: 62 of 62 equal | < 1 s |
| (iii) part 12: the program alone (pre-fill; every row where the reader says something marked "challenges", the doubt rule) | the same | <br>• passages 62/62; <br>• blocks 56/62; <br>• wordings 16/16; <br>• marks 52/62: 10 rows Opus marks "does not challenge"; <br>• items to a checker: all 25 of Opus's, plus 3 more (FC73, NF13, NF14); **none missed** | < 1 s |

Of the 6 block differences in the program's pre-fill:

- 2 are attached by the rule "under ⟨item⟩" where Opus did not attach them: D9.10 GLM "taken up under H12", and matter 9 Mimo "the entry under FC76".
- 4 are pointed to in other words, which Sonnet is asked to read: "see (e)", "in (e)", "as proposed in (c)", "(I40)".

Each checking script was also run on a copy it must catch:

- **tabulation check.** A corrupted sheet: a dropped row, a mark flipped, a wrong line, a wrong block, one character of a wording changed. Caught: all 5, and the uncited block the wrong block left.
- **applier.** Four copies:
  - one change altered: the md5 differs;
  - a change of kind "prose": refused;
  - a duplicate span: both refused;
  - a wrong source md5, or writing over tests/104: refused, nothing written.
- **key grep.** A fake key-shaped string in the scratchpad: its file named, the match not printed.
- **records check.** A draft with two invented numbers and "proof": all three caught. A number moved to the wrong place (7 → 6, where 6 stands elsewhere in the facts): **not caught**, so Opus reads every draft.

### 4.2 Sonnet through the harness: runs for the orchestrator

This agent has neither the Agent tool nor the Workflow tool, so no Sonnet agent was run. It did not start Sonnet any other way, such as a `claude -p` process or a new remote session, since the brief named only those two tools. These are the exact runs:

```
cd /home/user/ThreadSmith
H=Semantics/tools/sonnet_harness
python3 -B $H/workflow_args.py --run r2-sonnet-1 \
  --job "$H/specs/r2 claim suite.json" \
  --job "$H/specs/r2 text changes.json" \
  --job "$H/specs/r2 tabulation part 12, harnessed.json" \
  --job "$H/specs/r2 tabulation part 12, bare.json" \
  --job "$H/specs/r2 merge of the area models.json" \
  --job "$H/specs/r2 log entry draft.json" \
  --after "$H/specs/r2 tabulation part 12 - known answer.json" \
  --out <scratchpad>/sonnet_harness_tests/r2-sonnet-1.args.json
```

Then:

1. Call `Workflow({scriptPath: "/home/user/ThreadSmith/Semantics/tools/sonnet_harness/workflow/sonnet_jobs.workflow.js", args: <the object in that file>})`. Pass the object itself, not a string.
2. Then run `python3 -B $H/report_tests.py --run r2-sonnet-1 --out <scratchpad>/sonnet_harness_tests/r2-sonnet-1.report.json`.
3. Copy the numbers into the table below, and the tokens and time of each agent from the Workflow's own report.

Limits:

- The Workflow runs at most 2 agents at once on this 4-CPU machine. Count them within the limit of five Claude agents (decision S17).
- Launch it when round 3's claim runs are not using the CPUs, or the suite's 7 minutes stretch.
- The records draft stays in the scratchpad.

| test | Sonnet's result, first attempt | final | after the Opus check | tokens / time |
|---|---|---|---|---|
| (i) claim suite | — | pending | — | pending |
| (ii) text changes, md5s | — | pending | — | pending |
| (iii) part 12, harnessed: items found and missed; marks /62; to a checker /31; blocks /62; lines /62; wordings /16 | pending | pending | pending | pending |
| (iii) part 12, bare (Sonnet numbers and copies the blocks itself) | pending | pending | pending | pending |
| merge | — | pending | — | pending |
| (iv) log-entry draft: unsupported tokens; words | — | pending | Opus reads | pending |

**What to read in (iii):**

- For the harness to be worth using for tabulation, the harnessed sheet after the Opus check must:
  - miss none of the 25 items Opus sent to a checker;
  - equal Opus on at least the program-alone baseline (marks 52/62, blocks 56/62).
- The bare run shows what the pre-fill and the program copy fix: numbering, passages, and copying exact wordings.

### 4.3 What the harness had to fix while it was built

1. Removing environment variables whose names say "KEY" also removed git's `GIT_CONFIG_KEY_n` and left its `GIT_CONFIG_VALUE_n` behind. Git then stopped with exit 128, and the first merge test showed 128 "conflicts". Now all of `GIT_CONFIG_*` goes, and `git_commit.py` runs with the whole environment.
2. Wordings are copied by program from the fenced blocks, never by the agent. Opus's copies in round 2 were exact, 16 of 16; an agent's copy is where an error would enter.
3. The known answer (Opus's tabulation) is in a separate spec that no worker runs (lesson S2).
4. An agent's command is cut at 10 minutes; the suite takes about 7, and more under load. A long spec now runs detached (`--background`, then `--wait 540`), as lesson S14 asks: nothing ends the run when the agent's turn ends.
5. Results and the agent's files are never written over; they are numbered, so a first attempt can be read after a fix.
6. The records check at first read "106," with its comma, and took a number as present when it stood inside an md5. It now matches whole tokens.
7. Tabulation: a program finds all 62 passages from the replies' bold headers, because the brief asked for "one entry per item … headed by its id". A brief that asks for a report form a program can split makes most of a tabulation mechanical.

## 5. When Sonnet is used, from round 4

1. Sonnet runs only from a task spec, through the Workflow (or `run_task.py` by hand), one job per agent. It never judges a finding, writes maths or code for the model, writes a fix, or reviews (decision S16).
2. The mechanical jobs of §2 go to Sonnet at once:
   - the claim suite, and re-runs of single claims;
   - applying text changes;
   - md5s and the key grep;
   - word counts and scans, with every new hit to Opus;
   - the merge, with every conflict to Opus;
   - watching runs;
   - commit and push, with the message and the file list from Opus.
3. Every Sonnet result is checked by a second agent running the spec's checks by script. Any failure or mismatch goes to Opus, and Sonnet does not retry a job past its spec.
4. Tabulation goes to Sonnet only when both hold:
   - the orchestrator's run (§4.2) meets the bar in §4.2;
   - the round's reading rule, written before sending, says so. The rules of rounds 2 and 3 name "one fresh Opus 5.5 agent" for tabulation, and they stand for those rounds.

   Until then, the program's pre-fill with the doubt rule (every row where a reader says something marked "challenges") may be given to the Opus tabulator as a start. Each brief's report form keeps headers that name the items.
5. Records: Opus writes the facts; Sonnet may draft from them; Opus reads every draft and commits it. Nothing in `records/` is written by Sonnet.
6. Keys: no Sonnet job is given the key file, a GLM call, or a relaunch that needs a key. Those are the orchestrator's.
7. Every Sonnet agent counts in the limit of five Claude agents at a time (S17). The count is the orchestrator's, not the machine's (lesson S22).

## 6. Critical reviews, from round 4

- S42 ends Fable after round 3's review. Each later critical review is done by **a fresh Opus 5.5 agent** that built nothing of the round.
- The reviewer may give its mechanical re-runs to Sonnet through the harness:
  - a claim, or the whole suite (`run_claims.py`);
  - the applier and the md5s;
  - the scans and the quotations.
- It reads those results itself. What to doubt, what a result means and the review's text stay with the reviewer. A second checker on contested points is Opus too.

## 7. Unsure

- **Sonnet's quality is not measured yet**: no Sonnet agent ran here, and every "pending" cell waits on §4.2. A single run on one part is a small sample; a second part, such as part 13, would say more.
- **The mark "challenges"** is the one reading step in tabulation. On part 12, the doubt rule alone missed nothing and over-sent 3 items. Sonnet can only lower the over-sending, at a risk of misses, so it may add little; the run will tell.
- **Opus's own block attachments** are a convention, and in two places a reading. For example, GLM's FC76 says "proposal above", and Opus attached no block there. "Blocks as Opus" can therefore differ without an error.
- **The pre-fill reads round 2's report form**, bold headers naming items. Round 3's four jobs report findings, not items. Their sheet needs its own splitter, and the round-3 briefs were not read here.
- **The records check** catches added facts, not facts moved to the wrong place.
- **The alias `model: 'opus'`**: this note assumes the Workflow resolves it to Opus 5.5. If it does not, drop it, and the agents inherit the session's model.
- **Tokens**: none measured. The Workflow's report gives them.
