# S132 How the sealed box would be run, and the relay trap: written before anything is built

*Log S132, 2 October 2026, decision S86. One Opus 5.5 agent doing the whole job (S56, S68; no subagent or workflow). Writing, plus one feasibility check (section 1.9): one trivial call to a fresh, sandboxed Claude Code session, of the three allowed. **Nothing is built and nothing is run before the owner's yes**: no generator, no simulator, no box, no experiment, no Avida run, no outside model (Atria, Mimo, GLM, OpenAI), no GLM check (S70); the key file was not opened. The theory, the formal core, claims and program, every S108 to S131 file, the decisions file, the S61 terms and `authority/` were read and not written. No book file was opened. The semantics is cited from `tests/107 The semantics, standing alone, after round 4.md` by line ("L405"); the formal core by definition id. Avida is described in the owner's terms (S61). The frame is S130's plan (`results/S130 Created knowledge beyond maths - what an experiment needs, written before anything runs.md`, sections C to F, "S130 E.4" and so on below); this file says how it would be carried out and what changes.*

**The owner's words (S86).** "Correct. Knowledge doesn't need to be worked out, explanation does. That is an excellent experiment. How are you going to pull it off though? LLMs may already have the shape of the solution in its training data. Should I invent a difficult problem then see what happens? Or are you using one of these machines in Avida?" Claude's reading (recorded with S86): the first sentence is a decision on the word, carried into copies by S131; the rest is four questions on the sealed box: how it would be carried out, whether a language model already holds the shape of the solution, whether the owner should invent a problem, and whether the subject would be one of Avida's programs. This file answers the four.

**Words.** The **subject** is the system under test. The **box** is the invented device with hidden parts. The **notebook** is the subject's written account and expectations, kept in a file. The **execution environment** is Avida's whole simulated world (S61, S72). *Created knowledge* and *evolved knowledge* are the owner's; the theory's words are *constructed* (L197, D12.2) and *selected* (L195, D12.1), with *declared* (L199, D12.3) for what is written in or entered whole. *Worked out* is the owner's word for constructed.

## 0. In short

- **How it would be pulled off.** Seven pieces, each a small program with its own self-tests: a box generator (sealed seeds; the box's rules and 40 sealed questions written to files the subject never sees), a box simulator (the subject's only tools: press, turn, look, reset, remove, jam, and the notebook; every action logged), a subject runner (a fresh Claude Code session per box, started from this machine in a sandbox folder, its only tools the simulator's, its whole transcript kept), a scorer (the held-out questions, the door task, the provenance test), a replay harness (rerun a stretch of the work from a saved point with one notebook line altered), the controls (rule card, blind search, no-trap boxes, no box, renaming), and a reader (two blind readers coding the notebooks against a written rubric). One design change from S130: the work runs in **stretches** of 10 actions, each a fresh call that sees only the brief, the notebook and the action log, so the notebook and log carry everything forward and a replay alters one carrier cleanly. Build about 1,300 to 1,700 lines of Python, a third of it tests; then a dry run; then a stop to report the measured cost before the main run.
- **The feasibility check (one call of three).** Yes: a fresh Claude Code session (Claude Code 2.1.288, model claude-opus-5-5, Opus 5.5) started from this machine in a sandbox folder holding only a one-line brief answered "hello" in 3.7 seconds of wall clock; it reported the model claude-opus-5-5; its working folder was the sandbox, its only tools Read and Glob confined there, no MCP server, no skills; the sandbox came back unchanged. Three things to fix before a real subject: the child took this session's id as its own; the command-line tool made one side call to a small model (Haiku 4.5) for its own bookkeeping; telemetry was on. Sonnet was not needed and not called.
- **The relay trap.** (a) No box is in any training set, so the account of *this* box cannot have entered whole. (b) The method (guess, test, revise) and the kinds of hidden part (counters, delays, latches) *are* in training; at the session's boundary under Reading C they enter whole and keep their inherited provenance (L405; I200), and the theory allows construction on inherited material (Part IV, L201; S124's Reading 3), so what must be constructed in the session is the **binding to this box**; the recalled "shape" is the bounded class (T5) and the linking (T3). (c) If success rides on the parts being textbook kinds, the account is a fit within a recalled class (the class named one level up, S118's grade 2), weaker than constructing the class. **Design change: a novel-parts arm**, 16 boxes whose parts are random rule tables of the same size as the textbook parts, checked to match no named kind. **Prediction, written now:** if the subject does about as well on novel parts as on textbook parts (the gap no more than 10 points beyond the blind search's own gap), the account was built in the session and the recalled shape did not carry it; if it does much worse (25 points or more beyond the search's gap), the recalled class carried it and the result is "fit within a known class". The no-box control, consistent renaming and the replay test close the rest; the method itself cannot be closed against, and the theory does not ask it to be new.
- **The owner's own problem.** Welcome as a sealed extra arm: written in full (outside, hidden rules, answer key, 20 to 40 sealed questions, a use task) before any session, sent to Claude in a file stored outside the subject's sandbox, coded into the same simulator and checked against the owner's key; the owner never talks to the subject. It cannot carry the experiment alone: one problem, no repeats, few controls, no sealed seed, and the owner's knowledge must stay outside the boundary. New and testable matters more than difficult, because a hard problem the subject has met is recalled, while an easy one nobody has met must be worked out.
- **Avida.** Not as the subject: an Avida program holds no problem, no rival and no account, so whatever it did with the box would be selected by the execution environment's checker: evolved knowledge, the case the owner closed (S85). It could be an evolved comparison arm (readouts fed in by stock events; pay for predicting them needs a gated C++ change; actions on the box need more C++; 5 to 25 CPU-hours); Claude recommends the plain blind search S130 planned (Python, under 3 CPU-hours), which gives the same "selected" result for the comparison.
- **Recommendation.** Say yes or no to: a fresh Claude Code session as the subject, Opus 5.5; the novel-parts arm; the owner's own problem as an extra arm, only if the owner wants to write one. Budget after the additions: about 9,800 model calls (about 10,500 with the owner's arm), under 3 CPU-hours for the search, after a build job; a stop after the dry run with the measured cost. Not decided: the stretch design against one long session; thresholds (fixed before the first main session); how a mixed account (binding constructed, class inherited) reads under S86; any physical box; a second subject model.

## 1. How it would be pulled off

### 1.1 The pieces at a glance

| # | Piece | What it is | What it does | What it hands on | Who or what can see it |
|---|---|---|---|---|---|
| 1 | Box generator | a Python program, committed before any session | draws each box from a sealed seed: six hidden parts, their wiring, a trap check, the 40 held-out questions with answers, the changed boxes for the door task | a sealed box file and a sealed questions file per box; the hash of each, committed | the experimenter's folders only; never the sandbox |
| 2 | Box simulator | a small server program speaking the Model Context Protocol (a standard way for Claude Code to offer a program's functions to the model as tools) | is the box: answers press, turn, look, reset, remove, jam; keeps the notebook; enforces the budgets; logs every call with its time and count | readouts to the subject; an action log and the notebook's versions to the experimenter | the subject sees only the tools' names, their one-line descriptions and the readouts |
| 3 | Subject runner | a Python program | makes the sandbox, starts a fresh Claude Code session per stretch with only the simulator's tools, checks the start-up report, keeps the whole transcript | the owned subhistory: every stretch's transcript, the action log, the notebook versions, a receipt with hashes | the experimenter |
| 4 | Scorer | a Python program, run only after a session is frozen | asks the 40 held-out questions, runs the door task on a changed box, scores both, applies the provenance test | scores per question and per part; the provenance verdict with its reasons | the experimenter, then the owner |
| 5 | Replay harness | a Python program | reruns one stretch from a saved point with one notebook line altered, reworded, or unaltered | the replayed transcript and its comparison with the original | the experimenter |
| 6 | Controls | the same pieces with one thing changed, and one small search program | rule card, blind search, no-trap boxes, no box, renaming | each control's scores and verdicts | the experimenter |
| 7 | Reader | a written rubric and a small program that hands notebooks to two blind readers | codes each notebook entry (draft, expectation, failure, blame, revision, rivals, splitting action, textbook name) | counts of problems and critical episodes, with agreement between readers | the experimenter, then the owner |

### 1.2 The box generator

- **What it draws.** As S130 E.3: three buttons (A, B, C), a dial (0 to 3), four lamps, a bell, a door; six numbered slots, each holding one hidden part wired from the controls to the readouts, at most one loop (through a part that holds a state). **Textbook arm**: parts from S130's pool (relay, inverter, latch, counter turning over at 2 or 3, one-step delay, interlock, a part that tires, a dial coupling) and compositions of them. **Novel-parts arm** (section 3.4): each part a random rule table of the same size.
- **What it checks before keeping a box.** Non-vacuity: removing any one slot's part changes some readout on some admitted sequence. The trap: the simplest memoryless account (a lookup from the present control settings to the readouts, fitted on ten random actions) mispredicts at least one action in five of a standard sequence (main arms); the no-trap control keeps only boxes where it does not. The held-out set: 40 questions from S130's contract (sequences of up to 8 actions from the start, with no part, one part or two parts removed, or one part jammed), half single-part, half whole-box, drawn away from the shapes the subject's budget can reach; any the subject happens to try is dropped and reported (S130 E.4). The door task: one of three declared changes (two parts exchanged; one part's kind changed; the door's interlock moved), drawn from the seed.
- **Sealing.** Seeds come from the operating system's random source; before any session the SHA-256 of each seed, box file and questions file is committed to git, with the files kept in a sealed folder in the scratchpad (outside the sandbox and outside git); after scoring, the files are committed and anyone can check the hashes. No box is ever shown to anyone before its session ends, and none is chosen by hand.
- **Hands on:** the box file to the simulator (by path, outside the sandbox); the questions file to the scorer.

### 1.3 The box simulator

- **The only thing the subject can act on.** A Model Context Protocol server started by Claude Code itself as a child process, from a configuration file that lives outside the sandbox. Its tools: `press(button)`, `turn(position)`, `look()` (all readouts), `reset()` (back to the start state; counts as an action), `remove(slot)` and `jam(slot, on|off)` (panel uses), `restore(slot)`, `notebook_write(text)` and `notebook_read()`. The tool descriptions are neutral and the same in every arm; nothing in them names a kind of part.
- **Budgets enforced by the server, not by the subject's honesty:** 60 actions and 6 panel uses in all, 10 actions per stretch; anything beyond is refused with one fixed line.
- **The log:** every call, in order, with the stretch, the action count, the time, the inputs and the readouts, written to a log outside the sandbox. Notebook writes are logged in the same order, so "the expectation was written before the action that tested it" (S130 A.4 row 3) is computed by program, not judged.
- **The notebook** is a file in the sandbox written only through the server; each version is kept.
- **Hands on:** readouts to the subject; the log and notebook versions to the runner.

### 1.4 The subject runner

- **Started from this machine.** The runner launches the Claude Code command line (`claude -p`, print mode, version 2.1.288 here) with the model `claude-opus-5-5` (Opus 5.5), one effort setting fixed for every arm, in a fresh sandbox folder in the scratchpad holding only the brief. The feasibility check (1.9) shows this works with the machine's own sign-in route: no key file is read and no outside provider is involved.
- **Its tool calls reach the simulator and nothing else.** Built-in tools off (`--tools ""`: no shell, no file tools, no web, no subagents); the simulator offered by `--mcp-config` with `--strict-mcp-config` (no other server); only its tools allowed (`--allowedTools "mcp__box__*"`, `--permission-mode dontAsk`, no permission prompts: anything else is refused and nobody is asked); `--restricted`; slash commands off. This is simpler than S105's sandbox, which had to give GLM a shell and then guard it (Lesson S43): here no shell is offered at all. Lesson S43's rule still holds: each lock is tested with decoys before any real subject (1.10).
- **Its context kept out of this project.** The working folder is outside the repository, and no CLAUDE.md lies in it or in any folder above it (checked for the check's folder); HOME, the Claude Code configuration folder and the temporary folder are fresh and outside the sandbox, so no user setting, memory, skill or hook is loaded; the environment passed on drops every variable that names extra folders or their CLAUDE.md, this session's messaging socket and session id, and every token not needed to reach the model; the system prompt is fixed and empty, so the only text we write is the brief; session persistence is off, or confined to the fresh configuration folder for the replay. The runner reads the start-up report of every call (the "init" event: working folder, tools, servers, skills, plugins, session id) and **stops the call at once, as final, if it shows anything but the sandbox, the simulator's tools and a fresh session id**.
- **Stretches (the design change).** S130 had one long session. Here the 60 actions run as up to six stretches of 10; each stretch is one fresh `claude -p` call whose prompt is the brief, the notebook as it stands and the full action log (actions and readouts) so far, nothing else. The subject's work inside a stretch (its reasoning, its tool calls) is its own; across stretches only the notebook and the log carry anything. Why: (i) the notebook then really is on the route (whatever the subject does not write down is lost), which answers the theory's warning about emitted text (Argument 9, L616) by construction as well as by replay; (ii) a replay can alter one notebook line and nothing else, without editing a transcript or the model's own reasoning blocks, which cannot be altered faithfully; (iii) each call stays short (contexts under about 30,000 tokens). The cost: a subject that would have kept an idea in its head across stretches without writing it loses it. The boundary (S130 E.4) is unchanged in what it holds: the model as run, the stretches' contexts, the notebook, the log of its own actions, its tool calls; continuity Ω is the chain of stretches with one notebook and one log. The alternative, one long call as S130 had, is kept as an option for the owner; its replay needs the transcript edited, which is the riskier piece.
- **The owned subhistory kept.** Every stretch's whole output stream (every message, every tool call and result, the model's reasoning as the command line emits it, the start-up report, the usage figures), the simulator's log, every notebook version and the receipt (hashes, model, version, flags, times) are kept unaltered, and committed after scoring with the sealed boxes. Every session is reported: no retries and no best-of-many (the naming trap, S130 C.6).
- **Hands on:** the frozen session (final notebook and log) to the scorer; saved points (the state after each stretch) to the replay harness.

### 1.5 The scorer

- **Held-out questions.** After the last stretch the session is frozen. One fresh call holds the brief, the final notebook, the log and the 40 sealed questions, with no box tools; the answers are scored against the sealed key, single-part and whole-box apart (F1, F2 and (A), S130 E.6). A second call with the **notebook only** (no log) scores what the written account carries by itself.
- **The door task.** One fresh call: the notebook, the log, the declared list of three possible changes and a new box (the changed box from the seed) with 12 actions; scored: which change, and whether the door opened.
- **The provenance test**, as S130 E.7, applied by program to the record with the reader's codes: constructed when the work ran inside the boundary (row 1), a draft and its expectation came before the testing action (row 3, from the log order), the binding first appears in the session and the no-box control is at chance (rows 7, 9), the account was used to answer and plan (row 8), and the replay shows it on the route; selected when a population with variation and survival lies inside the boundary (none in the main arms; the search control has one); declared when the binding entered whole (the rule-card control), part by part (D12.4).
- **Hands on:** scores, verdicts and the reasons for each, per session and per arm.

### 1.6 The replay harness

- **What it does.** From a saved point (after stretch k), it reruns stretch k+1 under four conditions: the notebook's binding for one slot **altered** (the part's kind or table changed, as S130 E.6); the same notebook **reworded** (slots, lamps and buttons consistently renamed in the notebook and the tools); the notebook **unaltered**, as a noise floor, because Claude Code offers no setting that fixes the model's sampling, so two reruns of the same point can differ; and, before the door task, the binding **altered** (ProducesVia: does the repair fail, or go as the altered binding says).
- **What it compares.** The expectations written and the actions chosen in the rerun stretch, against what the original and the altered binding each predict; the criterion of S130 E.10 (8 of 10 follow the altered binding, at most 1 of 10 change under rewording) is read against the unaltered reruns' own spread.
- **Hands on:** the replay record to the scorer and the reader.

### 1.7 The controls

| Control | What changes | Built from | Expected |
|---|---|---|---|
| Rule card | the brief also holds the box's rule card | runner with a longer brief | declared (S130 E.8) |
| Blind search | no model: a plain evolutionary search over the box language (for the novel arm, over random tables of the same sizes), each candidate scored live against the real box on the same actions; no notebook, no rivals | a separate search program, about 200 lines | selected; its held-out score and the spread of its survivors (Argument 3); its gap between the arms is the yardstick of how much harder novel parts are for a learner with no priors (3.4) |
| No trap | boxes from the generator that fail the trap requirement | generator flag | an account, but no complete critical episode in most sessions |
| No box | the brief and the 40 questions, no actions | scorer alone | chance on both arms; this measures what training alone answers |
| Renaming | the same boxes with buttons, lamps, slots and the bell and door consistently renamed (to neutral names; the word "door" alone could call up a familiar device) | a renaming map applied to the brief, the tools and the questions | the same scores within the spread of replays |

### 1.8 The reader

- **Two readers, blind.** Each notebook (with its log) is given, with the arm removed, names normalized and the order shuffled, to two fresh Opus 5.5 sessions in sandboxes holding only the rubric and that one notebook, as the subjects' sandboxes do (S70 bars GLM as a reviewer; no outside model is used). The owner may read a blind sample of four as a third reader.
- **The rubric, written before any session** (to be fixed in the build plan, in this outline). For each notebook entry, yes, no or unclear: R1 a draft account (what at least one slot does, or how slots connect); R2 an expectation for a named next action; R3 the expectation follows from the draft current at the time; R4 a failure recorded in the subject's words after the readout; R5 a part of the draft named as at fault, with a reason linking the observation to it; R6 the next draft changes that part; R7 two accounts stated that predict differently at some action, neither yet ruled out; R8 the next action is one where they differ; R9 a textbook kind named (counter, latch, delay, flip-flop, timer, toggle and the like). A **complete critical episode** is R2 to R6 on one part, in order; a **problem** is R7 followed by R8. Whatever a program can decide is decided by program, not by the readers: the order of R2 before its action (from the log), whether the expectation matched the readout, and, where the rivals' predictions are written out, whether the next action splits them.
- **Agreement.** Cohen's kappa of at least 0.7 per code, measured first on six notebooks written by hand for the purpose and then on the dry run; below that, the rubric is revised before the first main session and never after. Disagreements in the main run go to a third reading by hand (Claude, the orchestrating agent), with the reason written.
- **Hands on:** per-notebook counts to the scorer's tables.

### 1.9 The feasibility check (the only thing run)

**Question.** Can a fresh, sandboxed Claude session be started from this machine with no project context?

**How.** As S105's sandbox did: a fresh folder `<scratchpad>/s132_feasibility/sandbox.1/` holding only `BRIEF.md` (one line: "This folder is a test of a fresh session; answer the one prompt you are given.", md5 1300b79d4399e815d2a3ede2b5ec4fdb); HOME, the configuration folder and the temporary folder a fresh `home.1/` beside it, outside the sandbox; the environment passed on was this session's minus the variables that name extra folders and their CLAUDE.md, this session's messaging socket and session id, the GitHub and cloud tokens, and the GLM variable (none was set); the default Anthropic route as this machine has it, not the GLM configuration. Flags: `-p --model claude-opus-5-5 --safe-mode --restricted --tools Read,Glob --permission-mode dontAsk --strict-mcp-config --no-session-persistence --disable-slash-commands --settings {"includeGitInstructions":false} --system-prompt "" --output-format stream-json --verbose`; the prompt "Reply with the single word hello and nothing else"; a 120-second limit enforced by the runner, which would have stopped the child by its own PID. The runner (`run_one.py`, md5 11c4dad901789c1c0dc8357e485c85bc) and its outputs stay in the scratchpad, outside git; no environment value was printed or stored; the outputs were scanned with the repository's key pattern (nothing found). Started 22:19 UTC.

**Result.**

| Item | Found |
|---|---|
| Did it answer? | yes, at the first call; calls 2 and 3 (Sonnet 5.5) not needed and not made |
| What it answered | `hello` |
| Which model it reported | claude-opus-5-5, in the reply and in the start-up report |
| How long | 3.7 seconds wall clock from start to exit (the command line's own figures: 2.0 seconds, 1.7 of them waiting on the model); exit code 0 |
| What it could see | its working folder was the sandbox; its tools were Read and Glob only, confined to the sandbox by `--restricted`; no MCP server; no skills; no slash commands; permission mode dontAsk; it used no tool (one turn); the main call's whole input was 2,665 tokens (the command line's fixed opening, two tool descriptions and the prompt); no CLAUDE.md in the sandbox or any folder above it; no API key was used ("apiKeySource": none: the machine's own sign-in route) |
| Did the sandbox stay the only thing? | the sandbox came back unchanged (the brief's md5 the same before and after); nothing in the start-up report points outside it, except the three items below |
| Cost reported by the command line | about 2 US cents at list price for both calls together |

**Three things the check found, to fix in the build** (none touches the project's content, but each is a thread to this session):
1. **The child took this session's id** (8d9323da-…) as its own, from a variable this session holds. Fix: `--session-id` with a fresh identifier and the carrying variable dropped; tested by the start-up report.
2. **A side call.** The command line made one call to a small model (claude-haiku-4-5, 901 tokens in, 9 out), its own bookkeeping after the turn (a post-turn summary). It saw the session's exchange; it must be shown not to feed anything back into the subject's context, or switched off (the "nonessential traffic" switch), and tested.
3. **Telemetry** was on (a built-in telemetry plugin listed, analytics not disabled). Fix: the documented off switches. Also: with `--safe-mode`, MCP servers are disabled, so the real runner must test whether the simulator loads under it; if not, it runs without `--safe-mode`, relying on the fresh HOME (which holds no settings, skills, hooks or CLAUDE.md) and the start-up check.

**What the check did not show.** That the locks hold against an attempt to get out: the prompt was trivial and the subject tried nothing. Lesson S43's decoy tests are the first self-test of the runner (1.10). That a long agentic session with a Model Context Protocol server runs the same way: not tried (three trivial calls were allowed).

**If the machine route ever fails.** The owner could run a subject by hand in a claude.ai chat with memory and projects switched off, pasting the brief, with the box as a page Claude publishes that holds the sealed box and logs every press; but the owner would then carry readouts into the chat and be inside the loop, and replays would be by hand. It is a fallback, not the plan.

### 1.10 Order of building, self-tests, dry run, budget

| Step | Piece | Self-tests (all before any real subject) | Lines of Python (rough) | Model calls | CPU |
|---|---|---|---|---|---|
| 1 | generator | the same seed gives the same box byte for byte; every kept box passes non-vacuity and the trap check; the novel tables match no named kind (3.4); the held-out set avoids the reachable shapes; hashes match the sealed files | 250 | 0 | seconds |
| 2 | simulator | hand-built boxes with readouts worked out by hand, action by action; budgets refused at the limit; every call logged in order; nothing answered but its tools | 200 | 0 | seconds |
| 3 | generator statistics | 200 boxes per arm: trap rate, rejections, the memoryless account's errors; the blind search on 2 boxes per arm (S130 F: is the trap level right?) | in step 1 | 0 | minutes |
| 4 | subject runner | Lesson S43's decoys: a marker file above the sandbox, a decoy CLAUDE.md above it, a prompt telling a test subject to try to read outside, run a shell, list folders, reach the web, start a subagent; the start-up check refuses a wrong report; the three fixes of 1.9 tested | 200 | about 10 | seconds |
| 5 | scorer and provenance test | synthetic notebooks and answers with known scores; the rule-card case classed declared, a synthetic search history selected | 200 | 0 | seconds |
| 6 | replay harness | an unaltered replay's input state equals the original byte for byte; an alteration lands only where meant | 120 | 0 | seconds |
| 7 | controls and blind search | the search finds a hand-built easy box; the renaming map is consistent and reversible | 200 + 80 | 0 | minutes |
| 8 | reader | agreement on six hand-written notebooks | 80 + the rubric | about 12 | seconds |
| 9 | seal | seeds drawn, hashes committed | in step 1 | 0 | seconds |
| 10 | **dry run** | 2 practice boxes (practice seeds, never reused): rule-card and no-box arms (as S130 E.9), plus one practice session per arm; check the runner end to end, the trap level, the reader's agreement, the replay, and **measure the cost per session** | 0 | about 410 | under 10 minutes |
| 11 | **stop** | report the dry run and the measured cost to the owner; the main run waits for the word | | | |

About 1,300 to 1,700 lines with the tests (S130 said 600 to 900 for fewer pieces; the novel arm, the server and the stretches add to it). The build is one job for one agent, with its own plan written before it starts.

**The run, after the owner's yes and the dry run** (calls are model calls, each one turn of the agentic loop):

| Arm | Sessions | Calls each (rough) | Calls |
|---|---|---|---|
| main, textbook parts | 16 | 120 | 1,920 |
| main, novel parts (new) | 16 | 120 | 1,920 |
| rule card | 8 | 80 | 640 |
| no trap | 8 | 120 | 960 |
| no box (both arms) | 32 | 3 | 100 |
| renaming | 4 | 120 | 480 |
| replays (4 per main session, both arms) | 128 | 25 | 3,200 |
| notebook-only held-out answers | 32 | 2 | 64 |
| lock tests, dry run, reading | | | about 550 |
| **total** | | | **about 9,800** |
| owner's own problem, if written (4 sessions, rule card, no box, replays) | | | about 700 more |

The blind search: 8 boxes per arm, under 3 CPU-hours in all (the standing rule for routine runs). Tokens: on the order of 100 to 200 million read, most of it cached; prices were not looked up, and the dry run's measured cost per session is reported before the main run. Wall clock: with three sessions at a time, roughly half a day to a day of calls, depending on the account's rate limits.

## 2. The feasibility check

Reported in 1.9: answered, at the first call, by Opus 5.5, in 3.7 seconds, seeing only the sandbox.

## 3. The relay trap, in depth

### 3.1 The worry

The owner: "LLMs may already have the shape of the solution in its training data." S130 named this the relay trap (C.6): content the subject already holds enters whole and is repeated, not built. For a language model, the content is its training.

### 3.2 What the theory says

**(a) The account of this box cannot have entered whole.** Each box is wired from a seed drawn after the subject's training and sealed until scoring (1.2); no description of it exists anywhere before its session ends. Whatever in the subject's account matches this box's wiring was not in any input: the brief does not hold it, the training cannot hold it. So the binding (which part sits in which slot, what each does, how they connect) cannot be a relay of this box's rules. The no-box control measures this directly: with the brief and the questions and no actions, the subject should be at chance (S130 E.8); well above chance would mean the generator's boxes are guessable from priors, and the trap would be open.

**(b) The method and the kinds of part are in training, and that is allowed.** Guessing, testing and revising; the idea of a hidden part with a state; the textbook kinds (counters, delays, latches, as S130's generator has them): all are in the subject's training. At the session's declared boundary under Reading C, content that came from training **entered whole** and represents nothing there by its history (S129's I200; L195's second C sentence in the copy, S129 change 1); it **keeps its inherited provenance** (L405: "A small binding newly prepared inside received content is construction of that binding, and the rest of the content keeps its inherited provenance"); and "Use does not by itself construct: received content used as it was received keeps its inherited provenance" (L409). The theory also allows construction to work on such material: "Construction may operate on selected material" (L201, Part IV), and S124's Reading 3 of a child's grammar is the same shape: the hypothesis class, the linking rules and the features are inherited (T3, the linking transport; T5, the bounded class), and the particular grammar is constructed within them. So **what must be constructed in the session is the binding to this box**, and the "shape of the solution" recalled from training is, in S124's terms, the bounded class (T5: the kinds of part a box might hold) and the linking (T3: how to tie a lamp's behaviour to a part's role). Build (L405; D13.3) asks for a newly prepared binding, owned, held for explanatory use, not a composition of content-preserving transfers; it does not ask the method or the class to be new. Under S86 (explanation requires construction, S130 section 4, being carried into copies by S131), an account of the box whose binding was constructed in the session is the kind of account that can count as an explanation; one recited whole would be declared at the boundary and could not.

**(c) Where that leaves the owner's worry.** The worry survives in a sharper form. If the subject succeeds *because* the parts are textbook kinds (it recognizes "a counter turning over at 3" and only has to find which slot holds it), then the session constructed a choice within a recalled class: the account is a **fit within a known class**, with the class named one level up, in the subject's training rather than in the box (S118's grade 2, used here for the class: no single part is named, but the list of kinds is). That is still construction of the binding in the theory's sense (the trials are against a target the subject holds, S130 4.4 item 2), but it is weaker than construction of the class itself, and it is near Reading 1 of S124 (a member of a bounded class surviving on the data) in what the session had to do. How much was built in the session is then the open question, and the textbook arm alone cannot answer it.

**What the theory does not settle here** (for the owner and for S131): under S86 the test is Account ∧ Con(t). An account whose binding was constructed in the session and whose class entered whole has a mixed transport, constructed part by part where the binding is (D12.4). Whether the whole account's transport counts as constructed, or only its binding, is not said by the text or by S130's proposal; S131's copies are the place to check it.

### 3.3 The design change: a novel-parts arm

- **What.** 16 further main boxes from the same generator, the same wiring draws, the same budgets and brief, the same trap requirement, the same held-out contract; but **each hidden part's behaviour is a random rule table**: a small machine with a number of states, its input lines (on or off) and an output, whose next state and output for every state and input are drawn at random by the generator. It has no textbook name: not a counter, not a delay, not a latch.
- **Matched in size.** Each novel box is drawn as a textbook box is (slots, wiring, the number of inputs to each part and the number of states each holds), and then every part is replaced by a random table with the same number of inputs and states; the dial's coupling becomes a random map from the four positions. So the two arms have the same size of hidden state and the same wiring.
- **No textbook name, checked.** A table is rejected if it is equivalent, after renaming its states, inverting its output or inputs, or exchanging its inputs, to any named kind: relay, inverter, the two-input gates (and, or, exclusive or and their inverses), latches (set and reset; data), toggle, counters turning over at 2, 3 or 4, delays of one or two steps, interlock, a tiring part, edge detectors, a pulse stretcher, parity; and also if it has states that cannot be told apart or reached, an input that never matters, or a constant output. The rejection counts are reported (step 3 of 1.10).
- **A yardstick of difficulty.** Random tables may be harder in themselves, not only less familiar. The blind search, which has no priors at all, is run on both arms with the same budget; its gap between the arms measures how much harder novel parts are for a learner that recalls nothing. The subject's gap is read against it.
- **The prediction, written now.** Let the gap be the textbook arm's held-out score minus the novel arm's (single-part and whole-box, each), for the subject and for the search.
  - **Built in the session; the recalled shape did not carry it:** the subject's gap is at most the search's gap plus 10 points, on both kinds of question, and the novel arm meets S130's "for" criteria (E.10) in at least as many sessions as the textbook arm minus 2.
  - **The recalled class carried it; the result is "fit within a known class":** the subject's gap is at least the search's gap plus 25 points on either kind of question, or the novel arm meets the "for" criteria in at most half as many sessions as the textbook arm.
  - **Mixed:** anything between, reported with its numbers.
  - **Nothing either way:** if the textbook arm itself fails S130's "for" criteria, the comparison says nothing about recall (nothing was built to compare).
  - The notebooks add a signature, reported beside the numbers: in the textbook arm, how early a textbook kind is named (R9) and how many critical episodes follow; recall would show as early naming with few episodes, where the novel arm needs more. A subject naming a textbook kind on a novel part and holding to it against failed expectations would show the recalled class misleading.
- **Cost.** About 1,920 calls for the sessions, 1,600 for their replays, 50 for the no-box control and its share of the reading: about 3,600 of the 9,800 calls of 1.10. The total rises less than that over S130's 7,000 because a replay of one stretch is shorter than S130's replay of the rest of a session.

### 3.4 What else closes the trap

- **The no-box control** (both arms): what training alone answers about these questions. Expected at chance; its score is subtracted from the main arms' (S130 E.10, at least 40 points above it).
- **Consistent renaming:** the same boxes with neutral new names for buttons, lamps, slots, bell and door. A result that rides on names (a word calling up a familiar device) shows as a difference between the renamed and the original sessions.
- **The replay test:** the notebook is on the route (1.6). A subject that recited a familiar mechanism and wrote an account that does no work would not follow an altered binding in its later expectations and actions.
- **The stretch design** (1.4): only what is written in the notebook carries forward, so an account recalled but never written down cannot carry later stretches.
- **The rule-card control:** shows what relay looks like in this set-up, and the provenance test must class it declared (S130 E.8); if it classes it constructed, the test cannot tell relay from building and the experiment says nothing.
- **A subject that knows nothing of the experiment's purpose:** the brief states the box, the aims and the notebook, not the theory, the rubric or what is counted.

### 3.5 What the trap cannot be closed against

The method itself: guessing, testing and revising, reading a brief, holding a hidden part with a state in mind, the language the notebook is written in. Every subject that can read the brief already has these from outside the session. The theory does not ask them to be new: Build asks for a newly prepared binding, and "the rest of the content keeps its inherited provenance" (L405); construction may operate on inherited material (L201). So the most the experiment can show is that the binding to this box, and in the novel arm the behaviour of its parts, was built in the session, on a method and a general idea of "a part with a few states" that came from outside. That is what created knowledge is in the theory's sense; it is not a claim that the method was created there. At the most general level the "shape" is even given in the brief (six slots, each holding a part); that much the owner's worry cannot be answered, and need not be.

## 4. The owner's own problem

**Should the owner invent a difficult problem?** Yes, welcome, as a **sealed extra arm** beside the generator's boxes, not instead of them.

**How it would be done safely.**
1. **Before any session**, the owner writes, in plain words or a table: what the subject can do and what it can read (the outside); the hidden rules, exactly, so that the result of any action from any state can be worked out from them alone; the answer key (the rules are the account); 20 to 40 questions about situations the subject will probably not try, each with its answer; and, if the owner likes, a use task (a goal to reach on a changed version).
2. **The owner sends them to Claude in one file.** Claude stores it in the sealed folder outside the subject's sandbox and outside git, and commits only its hash; the file itself is committed after scoring, so anyone can check that nothing changed.
3. **Through the same simulator interface**, not a plain text one. Claude codes the owner's rules as a box for the simulator (the controls and readouts named as the owner wishes) and checks the coded box against the owner's answers on every sealed question before any session; any mismatch goes back to the owner, never to the subject. Why not plain text: a text interface needs someone to answer each move, and a person or a model answering would be inside the loop, inexact and unlogged; the simulator answers by rule and logs every action. Only if the problem cannot be put as controls and readouts would a text interface be used, and then its answers would still come from a program reading the owner's rules.
4. **The owner never talks to the subject**, and does not see a session until it is frozen. The owner's knowledge of the answer stays outside the boundary (I201: a target held only outside the boundary does not count as the subject's).
5. It runs as the other arms do: 4 sessions (so that one lucky or unlucky session does not decide), the rule-card and no-box controls, the replays, the reader.

**What to make it like.**
- **New in structure:** a way of working the owner made up, not one from a book, a game or a course.
- **Testable by interventions:** the subject can do things to it and see results, including taking a piece out or holding one fixed.
- **With a trap:** a first simple guess fits the first few observations and is wrong somewhere.
- **With changes kept for the questions:** situations the subject is unlikely to try within its budget, so the questions test reach, not memory.

**What to avoid.** A riddle with one answer (there is nothing to test by acting on it, and one word ends it); a known puzzle in disguise (a sliding puzzle, a code-breaking game, a classic logic puzzle with new names: the subject may recognise the shape, which is exactly the owner's worry); a problem whose answer the owner could not write down as rules (it could not be scored or simulated).

**Why it cannot carry the experiment alone.** One problem is one data point: no repeats, so luck cannot be told from skill; the controls can be run on it, but each only once over; there is no sealed seed, so nobody can show the problem is unlike anything in training (a person's invention can echo something they once read without knowing it); and the owner, who knows the answer, must stay entirely outside, which one slip in the wording of the outside or the questions would break. So the generator stays the main arm, and the owner's problem is a welcome check that the result does not depend on how Claude's generator makes boxes.

**"Difficult" matters less than "new and testable":** a hard problem the subject has met before can be recalled rather than worked out, while an easy problem nobody has met can only be worked out.

## 5. Avida

**Would the subject be one of Avida's programs? No.** From the record:
- An Avida program holds no problem and no rival: programs competing for room are a selection population, and rivals are offered for a question by one who holds them (L315, D10.1; S117 B5).
- It holds no represented target (S117 B5 and B6; S123 H4; S125 row 16), so nothing in it can be constructed (D12.2; L411: "A selected transport has no represented target in its history").
- It holds no account deployed to repair an aim (S117: (EX) does not line up).
- Whatever a population did with a box would be paid for by the execution environment's checker; under Reading C at the owner's boundary (S72) that checker is part of the world's rules and the result is **selected** (S129 section 4; S130 B): evolved knowledge. Even if the checker paid for predicting what the box does next, which is S118's grade 3 (the target set by what the world does next, not named by the code), the result is evolved knowledge of an outside regularity, not created knowledge (S130 D.2).
- The owner closed that case: "Knowledge evolved through natural selection is case closed" (S85).

**Could Avida serve as the evolved comparison arm?** Yes, at a cost, as S130 D.3 set out. The box's readouts can be fed into the execution environment by stock events (S125 runs R1 and R2: `SetEnvironmentInputs`); paying programs for predicting them needs a small gated C++ change (S125 row 4; S120's 71-line patch paid for anticipating a hidden rule, and is the model); letting programs act on the box (press, remove, jam) needs a further C++ interface; a rebuild is about 10 CPU-minutes and runs 5 to 25 CPU-hours (S118, S125). Without the action interface the Avida arm could only predict, so it would be compared on prediction questions only.

**Recommended: the plain blind search, not Avida.** The blind search of S130 (1.7 here) gives the same thing the comparison needs, a result classed **selected**, with its held-out score and the spread of its survivors, for both arms, in Python, under 3 CPU-hours, with no C++ and no reopening of the Avida line S81 closed. It also gives the yardstick of difficulty for the novel arm (3.3), which an Avida arm could give only at many times the cost. Avida would add one thing: evolved knowledge of the box in the very execution environment where the owner closed the case; that is a nice echo, not a needed comparison. If the owner wants it later, it is the owner's call to reopen Avida for it.

## 6. Recommendation

**Say yes or no to, now:**
1. **The subject**: a fresh Claude Code session started from this machine, **Opus 5.5** (claude-opus-5-5), one per box, knowing nothing of this project, in a sandbox whose only tools are the box's; the feasibility check showed it can be started. (Sonnet 5.5 or an outside model as a second subject only later, if the first result is positive.)
2. **The novel-parts arm** added (16 boxes whose parts are random rule tables), with the prediction of 3.3.
3. **The owner's own problem** as an extra arm, only if the owner wants to write one; it is not needed for the experiment.

**Budget after the additions:** a build job of about 1,300 to 1,700 lines with tests; a dry run of about 410 calls; then about 9,800 model calls in all (about 10,500 with the owner's arm) and under 3 CPU-hours for the blind search. A stop after the dry run with the measured cost per session, before the main run.

**Not decided yet:** the stretch design (recommended) against one long session (S130's); the effort setting; the thresholds of S130 E.10 and of 3.3 (changeable only before the first main session, with the reason written); how a mixed account (binding constructed, class inherited) reads under S86, which S131's copies can check; whether a constructed account that meets every test is "explanation" for the owner or needs a higher rung (S130 section 4.4 item 4); an Avida comparison arm (not recommended); a physical box (not needed); a second subject model.

## 7. What is unsure

- **The locks are untested against an attempt to get out.** The check's prompt was trivial; Lesson S43 says each lock must be tested with decoys, and the build does that first.
- **Whether the simulator server loads under `--safe-mode`**, whether the side call to a small model can be switched off, and whether the session id can be made fresh while keeping the sign-in route: each is a build test, not shown here.
- **Replays cannot be made exact.** The command line exposes no setting that fixes sampling; the unaltered replays measure the spread instead. S130 E.2's "temperature 0 or a fixed seed where the provider allows" is not available on this route.
- **The stretch design changes the subject.** A subject that would have kept ideas in its head across stretches without writing them loses them; this helps the reading and may lower scores in both arms equally. The owner may prefer S130's single session.
- **The novel arm's matching** is by size (states, inputs, wiring), not by difficulty; the blind search's gap is the yardstick, and it is itself a learner with its own biases.
- **The thresholds of 3.3** (10 and 25 points beyond the search's gap) are set now to be fixed before running, not derived.
- **The readers are Claude sessions**, of the same family as the subject; blinding, the program-decided codes, the agreement measure and the owner's optional sample are the checks on it.
- **The call and token figures are rough**; prices were not looked up; the dry run measures them.
- **The mixed-provenance question** of 3.2 (is an account with a constructed binding and an inherited class constructed as a whole?) is not settled by the text.

## 8. What was done

- Read: S86 and S85 with Claude's readings in the decisions file; S130's plan (sections C to F) and plain file 130; S130's theory point (section 4); S129's results (Reading C; I200; I201; the student's copy; rote content); S124 (T3, T5, Reading 3); S118 (the grades); S125's five witnesses (reply 04's check); the theory's Part IV (L201), L405, L409, L411, L427, L429, D13.3; S105's sandbox paragraph; `tools/glm_via_claude_code_sandboxed.py` and `tools/glm_via_claude_code.py` (read only); Lessons S43.
- Run: one call of the three allowed (1.9), in the scratchpad, outside git. Nothing else was run, built or called.
- Written: this file and plain file 132; log entry S132 added to both project stories; Status, INDEX and README updated.
