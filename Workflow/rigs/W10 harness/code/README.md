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
| `record_adapter.py` | driver | stage B: the record's 96 marked reports put into the rig's shape |
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
  whole, and does not leak cross-step material (`partition.leak_check`, now a gate: a run whose
  parts pass carries any flagged line is stopped and not counted);
- arm (d)'s assembling call carries the frozen question, its step and the pile of answers, and
  no document block (W11 decision D1);
- arm (e)'s last call goes to the beta endpoint with an assistant message carrying `prefix: true`
  and the skeleton, and every other call goes to the ordinary endpoint;
- arm (r)'s system message carries the criticism and arm (a)'s does not;
- arm (k)'s skill text has the router table's rows, the mermaid graph that does the same
  routing, and the sentences that name them removed, and arm (a)'s has all of it;
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
| `<rig>/instrument/affordance.json` (W11 D4) | A4 | every certified cross-step field is read, and the counts file names every place that was looked at |
| `<rig>/code/clients/deepseek_client.py` | A6 | `deepseek_transport.py` sends it itself, and every call record says which client sent it |
| the document texts | A2's fetcher, into a folder outside the repository | `--texts DIR` or `W10_TEXTS`; there is no default |

`corpus.py` names, in one closed list each, the manifest spellings it will accept for the digest,
the two names, the "why" passage and a per-document change list. A key it does not know is not
ignored: the run says what it wanted. As A2's manifest stands (17 sources), the seam reads:
`exchange: {"exchangeable": ..., "names": [a, b]}`, `why_passage: {"quote": ..., "explains": ...}`
(the quote goes into the frozen question, so every arm is handed the same target word for word),
a per-row `split` of arms | reserve | spare, and a digest **block**:
`hash: {"text_sha256": ..., "raw_sha256": ..., "words": ...}`. The text digest is compared
against the document's text with the fetcher's provenance header removed; `raw_sha256` is the
digest of the bytes the fetcher downloaded, which nothing reading the saved text can recompute,
so it is recorded and not compared. A digest spelling inside the block that this rig does not
know stops the run.

**The split has three lists, not two:** `arms`, `reserve` and the held out (`not_in_the_split`
in A2's file, `spare` in the manifest's per-row field). Each list holds either an id or an
object with an `id`. A held-out document is never handed to a driver: `--docs` naming one stops
the run. split.json's own words: "They are not spares to be swapped in silently: using one is a
change to the split and a new claim"; W10 section 12 names spending them as a trap. Where
`split.json` is absent and every row carries a `split`, the split is built from the manifest and
the driver prints which of the two it used.

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
- **PA.1 is read by halves** (W11 decision D2). The first half — one request per step in arms
  (b), (c), (c') and (d) — is read as *requests minus tool-loop requests equals steps*, because
  the router is live in every arm and the record carries both numbers; `agreement.py records`
  prints the plain count and the adjusted count, so a later reader can take the other reading.
  The **arm (a) half is NOT REACHED on either transport** and is reported as such, never as held
  or falsified: on DeepSeek arm (a) is five turns of one conversation, five requests for five
  steps, so the clause is falsified by this rig's own design and not by anything about the
  reader; on the Sonnet subagent transport a request inside one call is not observable from
  outside it. Every Sonnet run record says what its `requests` count counts — calls this rig
  served — and that the tool loop inside a call was not observed, and carries
  `tool_loop_requests: null`, never zero.
- **The qualification of Derivation 3 is not sent to a reader under test** (W11 decision D3).
  The skill copy is byte-identical to `HV Skill/authority/33/hard-to-vary/`, whose word list
  carries the unqualified form, because the thing under test is file 33 as it stands and a
  correction to its word list would change the thing under test: arm (k) and W8 part A8 both
  turn on which edits of the skill the reader saw. W10 section 2's sentence is narrowed by D3 to
  the agents that are not under test — builders, fixers, reviewers, the markers of stages B and
  D, the stage E examiners and the stage F reviewers — who receive the qualification in their
  prompts. Every run record on both transports carries
  `derivation3_qualification_sent: false` with that reason. Given up: a reader's report may
  carry the unqualified Derivation 3, and a marker who sees it marks it as file 33's, not the
  reader's.
- **Arm (k) removes the graph as well as the table.** Under the skill's own marks the router
  table and the mermaid graph are *two routes to one job*, and removing one of two routes tests
  nothing, so `arms.skill_variant` removes the table's rows, the graph, and the four sentences
  that name the table, the graph or a row (a closed list: a sentence it expects and does not
  find stops the run). What it does **not** remove: the direct pointers inside the procedure
  ("Full wording is in `references/question-bank.md`"). Those are a different aspect of the
  skill from the one C1 names, and cutting them would be a larger edit than P4.8 asks for. The
  run record carries every removed line and sentence. Six of the seven module names still stand
  in the variant, in five lines of the procedure itself: `the-idea-in-depth.md` ("Read ...
  before a first full run"), `question-bank.md` ("Full wording is in ..."), `by-domain.md` (the
  proofs tests, twice), `reporting.md` (the marks) and `testing-against-cases.md` and
  `word-list.md` (the five word lists). `building.md` is named only by the table and the graph
  and is gone from the variant. So P4.8 is a test of the table and the map, not of every route
  to a module, and a zero difference reads as "the table and the map were not what the reader
  was following", never as "nothing pointed at a module".
- **The counts are read over certified fields alone.** `agreement.py` reads P4.1 to P4.5 and
  PA.3 over fields with `certified_candidate` true — and over stage B's own certified list when
  one is passed with `--certified`, which is what W10 stage B's gate means. The read-outs and
  the gauges (`modules_served`, `marks_outside_closed_list`, `layer_at_fault`) are printed
  beside every count and never inside one. Without this filter P4.4 could be carried by
  `marks_outside_closed_list` alone, which arm (e)'s skeleton drives to zero by construction.
- **"never varies", and what the corpus affords** (W11 decision D4). A field that takes one
  value on every run of every arm cannot show a loss, so `agreement.py` flags it "never varies"
  beside "uninformative" and it carries no arm difference. P4.2 and P4.3 are read over the
  certified cross-step fields that at least one of the eight arms documents affords, by A4's
  table. The table is looked for, in order, in the criteria file's `corpus_affordance`,
  `cross_step_affordance`, `affordance` or `what_the_corpus_affords` key, then at
  `<rig>/instrument/affordance.json`, `corpus_affordance.json`, `cross_step_affordance.json`;
  it is read in either shape (a map of field to documents, or a list of rows carrying a field
  and its documents). A field the table does not name is read, not excluded — "found nowhere
  means unknown". Where no table is found every certified cross-step field is read and the
  counts file names every place that was looked at.
- **The token ceiling is the service's maximum**, 393,216 (W10 section 2: "token spend not
  limited"). `deepseek_transport.MAX_TOKENS` is the value actually sent, whatever A6's client
  defaults to. A truncated report is a lost run and the ceiling costs nothing unused; the
  reply record carries `finish_reason` per call, so a truncation shows.
- **Arm (d) needs a parts pass** (steps 1 to 4, no test, no report) before the parts can be split,
  because a call handed only the document and one test has no numbered parts to be given a subset
  of. The parts pass is an addition of this rig and could absorb the arm's whole result, so it
  carries a gauge that is also a gate: `partition.leak_check` flags every line of it that carries
  cross-step material — in the skill's words *and* in plain words, because SKILL.md's own stance
  is "Plain words, concrete verbs" — and `partition.gate` stops that run. No run record is
  written for it, so nothing marks it; the flagged lines and the parts pass go into
  `run.stopped.json` beside its calls for a person to read.
- **A mark word counts only where it stands as a verdict on a part** (fault 24). The rule that
  flagged any mark word in a line that also named a numbered part fired on a part's own
  description — "1. The ether is held stationary while the earth moves through it.", "1. The
  mirror is loose in its mounting" — because *held*, *loose*, *idle* and *unknown* are ordinary
  English about apparatus and evidence. A stopped run writes no record and is not counted, so a
  false alarm costs P4.3 a run from its denominator for a reason that is the rig's, which is the
  shape of the fault the gate exists to remove. The rule now fires in two forms only: the mark
  word is the first word after a part reference and its separator ("Part 1: held by job 2",
  "2. loose — any near neighbour would do", "| 1 | held | … |"), or it is the whole content of a
  table cell ("| A | held | … |", which the first rule missed altogether). Every other pattern
  and the gate itself are unchanged; `python3 partition.py` runs the four verdict forms, the
  five innocent lines, and fault 27's fourteen below. What this gives up, both ways: a mark
  written as a sentence about a part
  ("Part 4 is idle") is now caught by nothing, because the wording that would catch it is the
  wording that fires on "the mirror is loose in its mounting"; and a Step 4 change-list table
  with an outcome cell reading "unknown" is still stopped, though nothing in it is a mark. A
  false alarm is read by a person; a gauge that reports "no leak" on a leaking pass is read as
  evidence.
- **A rival, a pull and a stronger/weaker pair count only where they are the cross-step
  verdict** (fault 27). Fault 24's patch left "Keep every other LEAK pattern", which was written
  without running the others on document English; run on it, three of the plain-word patterns
  fire on the words a physical or narrative document puts in a reader's mouth. All four of these
  are innocent and all four were flagged: "1. The paper sets Fresnel's account of aberration
  against the rival hypothesis of Stokes.", "2. The two rival hypotheses differ over whether the
  ether at the surface is carried along.", "10. The Crocodile pulls and the Elephant's Child
  pulls against him.", "6. A stronger drift would give a larger displacement; a weaker one, a
  smaller." W1 is the Michelson-Morley paper, whose whole argument sets Fresnel's account
  against Stokes's, and W9's plot is a tug of war, so a Step 3 parts list and a Step 4 change
  list on those two arms documents are exactly where such lines come from — and a flagged pass
  stops the run, writes no record and is not counted, which is fault 24's own ground. The three
  are narrowed the same way. *rivals?* fires where the line opens with the word as a heading
  ("Rival:", "- **Rivals.**"), or *best*, *strongest*, *nearest* or *obvious* stands just before
  it, or the line also says the rival is ruled out, told apart or separated, or a build word
  stands within forty characters of it. *pull … against* and *stronger/weaker* fire only where a
  part reference is **written out** in the line ("part 2", "parts 3 and 4"); the line's own
  leading number does not count, which is what fault 24 tripped on. Every other pattern and the
  gate are unchanged, and "Pairs that pull: 1 against 4" is still caught by the unnarrowed first
  pattern. What this gives up, said as fault 24's give-ups are said: a rival built in a sentence
  that neither opens with the word nor uses one of those verbs ("Stokes's account is a rival to
  Fresnel's") is now caught by nothing; a pulling pair named without writing out a part number
  ("making the first stronger makes the second weaker") is caught by nothing; a part written in
  words ("part two") is not a part reference to this rule; and the separation clause still fires
  on a parts pass whose own document rules a rival out in its own words ("2. The rival
  hypothesis of Stokes is ruled out by the fringe count"), which is a false alarm this narrowing
  does not remove.
- **Arm (d)'s assembling call is handed no document** (W11 decision D1). It gets the frozen
  question, its step and the pile of answers. W3 section 5 gives the assembler "the pile of
  answers to write the report" and W8 B12's ground is that "A final call handed a pile of
  answers assesses no support that any call wrote". With the document in front of it the
  assembler could assess the whole candidate in one context, and arm (d) matching arm (a) on the
  cross-step fields would then falsify P4.3 for a reason that is the rig's. Given up: the
  assembler cannot check a quotation against the text, so an arm (d) report's quotations are the
  test calls' quotations, and a marker who finds a misquotation in an arm (d) report attributes
  it to the call that wrote it, not to the assembler.
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
  of tool calls into a meta file. What the reader says it opened is **A4's marked field**
  `modules_self_reported`, filled by a marker under A4's criterion (W8 part C4). This rig writes
  no field of that name. What it writes is `modules_named_in_report`, a **raw aid, not a field**:
  a substring sweep of the report text for the seven file names, which fires on ordinary English
  ("building a case" gives `building`). P4.9 is read over the marked field against
  `modules_served`, on runs whose `modules_served` is not empty — "every run that opens a
  module" (`agreement.py records --marks <file>`).
- **The equal-length control is never longer than the summary**, and where the transcript has too
  little other material the gap is written into the record as `shortfall_words`. A control much
  shorter than the summary is not a control and the record says so.
- **Not settled here:** whether DeepSeek's beta prefix endpoint accepts thinking mode on
  `deepseek-flash`. The documentation read on 22 September 2026 does not say. If the service
  refuses, the run stops with the service's own words; the rig does not quietly drop thinking and
  carry on, because a run under a different thinking setting is a different arm.

---

## An order of work

**Stage B, the instrument certified on the record's 96 reports.** It comes first, and it is the
gate: "No field carries an arm difference in stage C unless it agreed here" (W10 stage B).

```
python3 record_adapter.py --check          # 96: p52 48, rep 12, rep31 12, son 12, son31 12
python3 record_adapter.py                  # writes <rig>/runs/record96/<run>.json
python3 first_marker.py prompts  --scratch DIR --reader record96
python3 first_marker.py collect  --scratch DIR --reader record96   # fills the run-record fields
python3 second_marker.py prep    --scratch DIR --reader record96 --seed N
python3 second_marker.py collect --scratch DIR --reader record96
python3 second_marker.py compare --scratch DIR --reader record96
python3 agreement.py markers --reader record96                     # agreement by field
```
The adapter reads the record and writes nothing into it. `<rig>/runs/record96/` is regenerable
by running the adapter again. The run ids are `<set>_<the record's own file stem>`, with an
underscore, so none can be mistaken for this round's `<document>-<arm>-r<repeat>`;
`agreement.py runs` is about this round's arms and its (a)-to-(a) baseline and is not read over
them.

**Stage C and D, the arms.**

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
python3 agreement.py runs    --reader deepseek --certified <stage B's list>
python3 agreement.py records --reader deepseek --marks <the first marker's marks>
```
`agreement.py records` computes PA.1 (both counts, with the arm (a) half reported NOT REACHED),
P4.6, P4.7, P4.8, P4.9 and P-B7. P4.7 and P4.9 need the marks file beside the run records: P4.7
is the CANNOT count over the eleven test fields and P4.9 is read over A4's marked
`modules_self_reported`, never over a substring sweep. Without it both say so and hold nothing.

Every counts file it writes names the field and the document. Nothing is summed across fields,
arms or readers, and no count is a verdict on a part of W8.
