# The W10 harness (stage A, A1)

The rig that runs every arm of plan W10 section 4 on two transports, marks what comes back, and
counts agreement by field and document. Written by the A1 agent of stage A, under the
hard-to-vary skill (HV file 33).

Nothing here sends anything unless a driver is run without `--dry` and a key is in the
environment. No key is read except to refuse to write a file that contains one
(`rig.assert_no_key`, called on every write).

---

## Drivers and rules

A **driver** does something when you run it: it sends requests, or writes prompt files, or
writes a counts file. Every driver takes `--dry`, and a dry run sends nothing.
A **rule** is a decision written down as code. Rules are imported by drivers; running one alone
does nothing but a self-check or a demonstration.

| File | Kind | What it is |
|---|---|---|
| `run_deepseek.py` | driver | runs the arms on DeepSeek V4.1 Flash, five threads, resumable |
| `sonnet_prompts.py` | driver | the prompt files for the Sonnet subagent transport, and the JSON "next step" interface |
| `wrap_sonnet.py` | driver | turns the Sonnet replies into run records of the same shape as DeepSeek's |
| `exchange.py` | driver | arm (x): exchanges the two names of a document and prints the counts |
| `first_marker.py` | driver | the marking prompts from A4's criteria; collects and checks what comes back |
| `second_marker.py` | driver | the blind second marker: shuffle, closed mapping, prompts, compare |
| `agreement.py` | driver | run-to-run and marker-to-marker agreement by field and document; the prediction counts |
| `skillcheck.py` | rule (+ `--check`, `--sync`) | the skill copy diffed against HV file 33 before every call |
| `rig.py` | rule | paths, run naming, JSON writing, the key-safety check |
| `corpus.py` | rule | A2's manifest and split, and the document text, read and hash-checked |
| `question.py` | rule | the frozen question, and arm (f)'s version of it, with the withholding gauge |
| `steps.py` | rule | file 33's procedure cut into steps, and the eleven tests |
| `arms.py` | rule | the arms, and the context each call of each arm is handed |
| `summariser.py` | rule (+ `--demo`) | arm (c)'s fixed summariser and arm (c)'s equal-length control |
| `carryover.py` | rule | arm (c')'s note, cut out of the reply and handed on unchanged |
| `partition.py` | rule (+ demo) | arm (d)'s parts pass, split, assembler, and leak gauge |
| `deepseek_transport.py` | rule | one request, and what is saved of it |
| `marks.py` | rule | A4's criteria file, read; what agreement means for each field kind |

`CRITERIA-SCHEMA.md` says what shape A4's `instrument/criteria.json` is read in.
`fixtures/` holds what the rig needs and the dry run's stand-ins; nothing in it is a result.

---

## How runs are named

```
<document>-<arm>-r<repeat>        e.g.  W03-cprime-r2
```
Arm ids: `a b c cctl cprime d e f r x k`. `cctl` is arm (c)'s equal-length control (W8 section
4); `cprime` is arm (c'); `k` is optional, on the owner's word.

```
<rig>/runs/<reader>/<run>.json              one record per run
<rig>/calls/<reader>/<run>/NN-STEP.request.json   the body as sent      (prediction PA.1)
<rig>/calls/<reader>/<run>/NN-STEP.reply.json     the reply as returned (prediction PA.1)
<rig>/calls/<reader>/<run>/NN-STEP.stream.txt     the stream as it came, when streaming
<rig>/dry/<reader>/<run>/...                       what a dry run would have sent
<rig>/marking/...                                  marks, the closed mapping, the counts
```
The reader (`deepseek` or `sonnet`) is a folder and a field in the record, never part of the run
id, because the two readers are never summed (W10 section 4).

Resumable: a run whose record exists is skipped; inside a run, a call whose reply file exists is
read from disk and not sent again. `--force` re-runs.

---

## What a dry run checks

```
python3 skillcheck.py --sync                      # once: copy HV file 33 into <rig>/skill/
python3 run_deepseek.py --dry --arms all --docs DRY1 --repeats 1 \
        --texts fixtures/dryrun --sources fixtures/sources.example.json
python3 sonnet_prompts.py plan --dry --arms all --docs DRY1 --repeats 1 \
        --texts fixtures/dryrun --sources fixtures/sources.example.json
python3 agreement.py --dry
python3 first_marker.py prompts --dry --criteria fixtures/criteria.example.json
python3 second_marker.py prep --dry --criteria fixtures/criteria.example.json
```
That is prediction W10.1: every arm dry-run on one document, for both transports, with the
request text saved. A dry run checks:

- the skill copy is HV file 33 exactly, file by file (`filecmp`, not a hash of a hash), and the
  digest of each file as sent goes into every request record;
- the manifest reads, the split reads, the document's text matches the manifest's digest;
- the frozen question renders, and for arm (f) that no sentence of the withheld change list is
  anywhere in the prompt (`question.check_withheld`, which stops the build if one is);
- arm (x) replaced both names at least once (`exchange`, which stops the run if either is zero);
- arm (d)'s parts pass yields a parts list of at least two, splits into groups no call holds
  whole, and does not leak cross-step material (`partition.leak_check`);
- arm (e)'s last call goes to the beta endpoint with an assistant message carrying `prefix: true`
  and the skeleton, and every other call goes to the ordinary endpoint;
- arm (r)'s system message carries the criticism and arm (a)'s does not;
- arm (k)'s skill text has the router table's rows removed and arm (a)'s has them;
- every request body is well formed and carries no value of any key in the environment;
- the counting rule runs end to end on made-up marks (`agreement.py --dry`).

A dry run uses stand-in replies from `fixtures/dry_replies.json` so that the later calls of every
arm can be built. Those are this rig's own words. A dry run shows that the harness runs; it shows
nothing about whether any reader works.

---

## What the rig is handed by other agents

| Path | Written by | If it is not there |
|---|---|---|
| `<rig>/corpus/sources.json`, `split.json` | A2 | every driver stops and names the file |
| `<rig>/instrument/criteria.json` | A4 | the markers stop and name the file |
| `<rig>/code/clients/deepseek_client.py` | A6 | `deepseek_transport.py` sends it itself, and every call record says which client sent it |
| the document texts | A2's fetcher, into a folder outside the repository | `--texts DIR` or `W10_TEXTS`; there is no default |

`corpus.py` names, in one closed list each, the manifest spellings it will accept for the digest,
the two names, the "why" passage and a per-document change list. A key it does not know is not
ignored: the run says what it wanted. As A2's manifest stood on 22 September 2026 (18 sources),
the seam was tested against it and reads: `exchange: {"exchangeable": ..., "names": [a, b]}`,
`why_passage: {"quote": ..., "explains": ...}` (the quote goes into the frozen question, so every
arm is handed the same target word for word), and a per-row `split` of arms | reserve | spare.
There was no digest key in it: every run record then carries `hash_checked: false`, which is the
gauge, and a later fetch cannot be checked against the one the runs used. Where `split.json` is
absent and every row carries a `split`, the split is built from the manifest and the driver
prints which of the two it used.

A dry run on a real corpus document needs A2's fetcher to have written that document's text into
the `--texts` folder first. The dry run in `fixtures/dryrun` uses a document this rig wrote for
itself, and shows only that the harness runs.

---

## Decisions in the rig, and what would show each wrong

- **The router is live in every arm.** Otherwise a difference between arms would be a difference
  in what was reachable. It costs the record's mode 1 (the whole skill in the context): no run of
  this round is comparable with those runs on that count.
- **Arm (a) on DeepSeek is one conversation of five turns**, not one request that does everything.
  If it were one request, arm (a) would differ from arm (b) in two ways at once — the carriage and
  the decomposition — and P4.1 could not attribute a difference to either. Shown wrong by: the two
  arms' contexts being the same at each step, which the saved request bodies would show.
- **Arm (a) on Sonnet is one subagent working the five steps in order.** The transport cannot share
  a conversation across subagents. It still differs from arm (b) in one way more than the DeepSeek
  pair: the reader can revise an earlier step. That is named and not removed; P4.1 is clean on
  DeepSeek and not here.
- **PA.1 on Sonnet is not readable.** The rig counts the calls it served; how many requests one
  subagent made inside a call the transport does not show. Every Sonnet run record says so. On
  DeepSeek the count is exact, and the tool-loop requests are counted apart so that "one request
  per step" means what A1 means by it.
- **Arm (d) needs a parts pass** (steps 1 to 4, no test, no report) before the parts can be split,
  because a call handed only the document and one test has no numbered parts to be given a subset
  of. The parts pass is an addition of this rig and could absorb the arm's whole result, so it
  carries a gauge: `partition.leak_check` reports every line of it that carries cross-step
  material, and a run whose parts pass leaks is reported, never silently counted.
- **Arm (d)'s split is `cross` with two groups** (every test meets every group; 11 x 2 + 2 = 24
  calls per run). That is a free choice, and it is loose: `rotate` (11 + 2 calls, each test meeting
  one group) would satisfy W8 part B12 as well and costs half as much. What would settle it is the
  phase plan's budget, which is not A1's to fix. `--split rotate --groups N` changes it.
- **Arm (e) prefills the last call only.** The emission arm (e) sets is the report, which is
  written at step 6-7; the four earlier calls go to the ordinary endpoint with nothing prefilled,
  so the only difference from arm (a) is at the port the skeleton sets. Shown wrong by: a reading
  of W3's "arm (a)'s prompt with the emission prefilled" on which every step's emission counts,
  which would make arm (e) a different arm; the saved request bodies say which was run.
- **The modules-opened trace is the rig's, not the reader's.** On DeepSeek the rig's tool loop
  records every module it served; on Sonnet the workflow script writes the transport's own record
  of tool calls into a meta file. What the reader says it opened is kept in a separate field
  (W8 part C4). P4.9 is the count of runs where the two differ (`agreement.py records`).
- **The equal-length control is never longer than the summary**, and where the transcript has too
  little other material the gap is written into the record as `shortfall_words`. A control much
  shorter than the summary is not a control and the record says so.
- **Not settled here:** whether DeepSeek's beta prefix endpoint accepts thinking mode on
  `deepseek-flash`. The documentation read on 22 September 2026 does not say. If the service
  refuses, the run stops with the service's own words; the rig does not quietly drop thinking and
  carry on, because a run under a different thinking setting is a different arm.

---

## An order of work

```
python3 skillcheck.py --sync
python3 run_deepseek.py --dry --arms all --docs <one doc> --texts DIR       # W10.1
python3 sonnet_prompts.py plan --dry --arms all --docs <one doc> --texts DIR
# then, with a key in the environment:
DEEPSEEK_API_KEY=... python3 run_deepseek.py --arms all --repeats 1,2,3 --texts DIR
# and, through the workflow script, per run: sonnet_prompts.py next -> one subagent -> repeat
python3 wrap_sonnet.py --scratch DIR
python3 first_marker.py prompts --scratch DIR --reader deepseek
python3 first_marker.py collect --scratch DIR --reader deepseek
python3 second_marker.py prep  --scratch DIR --reader deepseek
python3 second_marker.py collect --scratch DIR --reader deepseek
python3 second_marker.py compare --scratch DIR --reader deepseek
python3 agreement.py runs   --reader deepseek
python3 agreement.py records --reader deepseek
```
Every counts file it writes names the field and the document. Nothing is summed across fields,
arms or readers, and no count is a verdict on a part of W8.
