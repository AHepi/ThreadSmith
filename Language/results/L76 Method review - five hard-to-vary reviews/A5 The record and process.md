# A5 — The record and the process

Reviewer A5. Task: test the RECORD and PROCESS of the Language project, and its claim to be following the hard-to-vary skill and file 11.

How-I-know tags used throughout: **read** (in a named file), **seen** (a printed output or a command's result), **worked out** (my reasoning from tagged things), **assumed**.

---

## 1. The question, frozen

**What is being explained.** Why the Language project's results may be believed — not the results themselves, but the record-and-process that is offered as what makes them more than one model's say-so: a frozen plan, an append-only log, a Decisions file of the owner's words only, a Lessons file of failures only, a Status summary, numbered files never overwritten, outside agents doing the work, and the orchestrator checking returns by hash and rerun.

**Over what range.** The Language thread from L60 to L75 (21–22 September 2026), and the four record files in `Language/records/`, against the rules in `/home/user/ThreadSmith/RESEARCH-CONVENTIONS.md`.

**What is asked.** Kind of question: *does it achieve its purpose?* Specifically: can a reader who was not there recompute, from the record, what was done, by whom, on whose authority, and what each claim rests on — and would the record look different if the work had not been done that way?

**Not asked here.** Whether the ledger language works, whether the four findings of L75 are right, whether s(CASP) is the right checker. Those are other reviewers' ground.

---

## 2. The explanation in parts, and the jobs

### The parts (the project's own words)

From `/home/user/ThreadSmith/RESEARCH-CONVENTIONS.md` unless marked (**read**):

- **P1.** "The log is the record… The log is added to, never rewritten." (line 12)
- **P2.** "Decisions holds the owner's words as written, and nothing else." (line 13)
- **P3.** "Lessons holds only things that failed while being built or tested, and how each was fixed." (line 13)
- **P4.** "Status is the summary and drifts from the log at its peril." (line 13)
- **P5.** "Before any test or research: freeze the predictions as their own numbered file first. A test plan is written before the run and not edited after." (line 19)
- **P6.** "Every result names what it did not test." (line 20)
- **P7.** "Every patch records what it gives up as well as what it fixes." (line 22)
- **P8.** "To change a project file: check Decisions first; make the change as a new numbered file; never overwrite an old numbered file." (line 30)
- **P9.** "Start only after the owner's word. Work is planned, the plan is shown, and the run waits for the go-signal for each phase." (line 27)
- **P10.** The receipt discipline: "A return from another model or a reader is kept unchanged" (line 21), plus the orchestrator's checks — manifest hashes, reruns, source identity (`Language - project story.md`, L62, L69, L73, L74).
- **P11.** The split: the worker executes and returns drafts; the orchestrator checks the return and writes the results and the log (`Language - project story.md` L61; decision L3).
- **P12.** "A reader under test is never shown an answer key or a source's standing." (line 26)
- **P13.** L-numbered entries that cannot collide with the shared record (`Language/records/READ ME FIRST.md`; Lesson L1).
- **P14.** The four error sources as the frame findings are sorted into (decision L4: "the language is being applied out of scope, the translation from prose is applied incorrectly by an LLM, the parser is faulty, the translation from language back to prose is incorrect").

### The jobs

| | Job (as a contrast) | Tag | Source |
|---|---|---|---|
| **J1** | Tell an error of the language from an error of the translator, the checker or the text — not let the four blur | **given** | decision L4, owner's words quoted above |
| **J2** | A result reads as a test, not as a story fitted after the run | **fixed** | RESEARCH-CONVENTIONS line 19, "not edited after" |
| **J3** | The orchestrator, not the worker, owns the record | **given** | decision L3: "Ok but you're still orchestrator. I'm not handing the whole project over" |
| **J4** | A fresh agent picks the project up from the read-me and Status, not from the whole log | **fixed** | RESEARCH-CONVENTIONS line 15: "Starting a new chat: read the project's `records/` read-me and its Status first" |
| **J5** | Any claim in Status can be traced to a log entry and then to an artefact that could have come out otherwise | **added** (mine) | — |
| **J6** | The record tells what an outside party established from what the orchestrator established | **added** (mine) | — |
| **J7** | Two chats cannot collide on an entry number | **given** | decision L1 |

Parts held only by J5 or J6 are *held if* those jobs are real. I say so at each.

---

## 3. Part by part

Never added up. Provenance in its own column.

| Part | Mark | What holds it / what would settle it | Provenance |
|---|---|---|---|
| **P1** log append-only | **held** | J7 and J2. **Seen**: `git log --oneline -- Language` gives 18 commits touching the project story, all appends; L67 says in its own text "Earlier log entries retain what was known when they were written; this entry corrects the present-tense summary, not the historical record" (**read**, project story line 61). Remove the part and J7 and J2 both fail | fitted (inherited from the root conventions) |
| **P2** Decisions = owner's words only | **loose** | A near neighbour does every job better: "the owner's words as written, with Claude's reading beside them, marked as Claude's." That neighbour is what Lesson L3 already prescribes ("a paraphrase is marked as Claude's until the owner has read it", **read**, Lessons L3) and what the file already is in practice, unmarked. What is really held is the weaker thing: *the owner's words are quoted verbatim and are separable from the gloss*. See finding B1 | asserted |
| **P3a** Lessons = failures only | **held** | J1 and J6. It is the only place in the record where error is admitted at all; remove it and the record has no error column. **Read**: Lessons file, nine entries, all failures | asserted |
| **P3b** "and how each was fixed" | **loose**, and a **catch-all with a gauge that reads "swallowing"** | "Fix: …" can absorb any failure. A gauge exists and is cheap: read the next plan written after a lesson against that lesson's own obligation. **Seen**: Lesson 51's fix ("a forcing case's prediction quotes the text it will be run on") is violated by the L66 plan (frozen 21 Sept, after 51) and again by the L71 plan (frozen 22 Sept). See finding C1 | asserted |
| **P4** Status as the summary | **held** by J4, and **currently fails J4** | Remove it and a fresh agent must read eighteen long log entries, so J4 holds it in place. But it does not do the job: three internal contradictions and one pointer to a file not in the repository (finding A2, finding G1). What would settle: date every bullet and rebuild it from the log at each entry | fitted |
| **P5** frozen plans | **held** | J2. **Seen**: every plan file has exactly one commit — `git log --oneline` on the L65, L66, L71, L72 and 45 plan files returns one line each. The L66 plan also declares its own non-blindness in advance: "The predictions below were written knowing the plants" (**read**, L66 plan line 12). This is the strongest part in the set | built |
| **P6** results name what they did not test | **held** | J2. **Read**: "Not tested" sections present in L65, L66, L71 and L72 results, and each names something real (e.g. L72: "Which translation is right; two translators agreeing may both be wrong") | fitted |
| **P7** every patch records what it gives up | **loose** | A near neighbour — "patches record what they give up where someone remembered" — does exactly what the record does. **Seen**: rig 1 patches **2** and **5** exist in `Language/rigs/rig 1 - arguments/patched/run_check.py` (line 116 `# PATCH 2:`; line 233 `# ---- check 5 (PATCH 5, forced by paragraph F, fitted to that one paragraph)`) and have **no entry** in either "What each patch gave up" list. `grep -rn "Patch 2\b"` over `Language/*.md` returns nothing. What would hold it: a count check, give-up lines against patch numbers | fitted |
| **P8** never overwrite a numbered file | **held if** — held by J2 and J5, and breached once with a self-granted exception | **Seen**: `Language/tests/L60 Handoff - a new agent runs plan 45.md` has two commits (3b4b80c, 6563883) and the second changes who writes the results. The exception ("in the file itself since it had reached no one", project story L61) appears nowhere in the conventions, and the file carries no revision note — while `L66 Handoff … second version.md` does ("(Second version: the paragraph above was added after the first handover; nothing else changed.)"). Two treatments of one situation. What would settle: write the exception into the conventions, or put the note in the file | built |
| **P9** the run waits for the owner's word at each phase | **loose** | A near neighbour — "the orchestrator runs what the log parks and asks for the word before a *change*" — matches the record exactly. **Seen**: L71 (plan frozen, `tools/consequences.py` run on ledgers C and H) has no owner request in its log entry and no decision between L9 and L71 in `Language - Decisions.md`. L71 is not one of the five steps approved at decision L5; it is a follow-up the orchestrator parked at L65. Nothing in the record marks it as an exception | asserted |
| **P10a** receipts for the *checker* step (reruns, input byte-comparison) | **held** | J5 and J6. Reruns are a route the history supplies, reproducible by anyone. **Seen**: `L72 Reruns by the orchestrator/sameness/*.txt` and `reruns/*.txt`, 16 of 16; `L69 Reruns by the orchestrator/`, 13 files | built |
| **P10b** receipts for the *translation* step ("the worker did the work blind, in order") | **unknown** | No test run so far bears on it. The only evidence is the worker's own file, e.g. `L72 Return - Astra Ultra/Astra_Ultra_translation_sequence.jsonl`, whose every record begins `{"written_by": "Astra Ultra", …, "next_text_opened_after_completion": true, …}` (**seen**). What would settle it: a second worker on the same passages with the same freeze protocol, or a timestamped artefact the worker does not author. See finding D1 | asserted |
| **P10c** source identity of the agents | **two routes**, one weak | Route 1 (**seen**, L70): sandbox path, Python version, network capability, self-naming — real traces, and they do separate two harnesses. Route 2 (**read**, L74): "it names itself ChatGPT, which is Astra Pro by decision L9" — self-report alone. For L66 the claim that matters is not "two harnesses" but "the reader had not seen the corpus", and only P12's behavioural receipt reaches that | fitted |
| **P11** the split, worker executes / orchestrator writes | **held** for J3, and **wrong place** for J5 and J6 | Held: decision L3 is the owner's word, quoted, and Lesson L5 shows what happens without it (a worker with repository access wrote L67 and translated nothing). Wrong place: nobody checks the orchestrator's marking. See section (e) | built |
| **P12** the reader never sees the key | **held** | J5, and it is the one receipt in the whole set that could have come out otherwise. **Read**, L66 results line 39: the reader "named all seven findings correctly and traced the sentence for **none** with confidence, saying so each time". Sight of the passages would not predict that; blindness does | built |
| **P13** L-numbering | **held** | J7. **Read**, Lesson L1: two collisions in one day forced it; none since | built |
| **P14** four error sources as the frame | **held if** — held by J1, which is given, but the instruments cannot yet separate two of the four | The record says so itself. **Read**, L66 results line 59: "The blind test as designed measures the translator more than the checker." **Read**, L72 results line 31: "Every standing difference between the two sets comes from this one rule." What would settle it: a run that fixes the translation and varies the checker. None exists | asserted |

---

## 4. Whole-explanation checks

### (a) Read-back on the record itself — three claims from `Language - Status.md`

**Claim 1 — "all 21 of my lines matched by hand, 4 by the wording program" (Status, L72 bullet).**
Trail: Status → project story **L73**, "The program matched 4 of my 21 lines; the hand matched all 21" → `results/L72 Test results …` line 36 (E1) and the printed hand pairing at line 66 → the artefacts. **Seen**: `grep "BOTH SAY" "L72 Reruns by the orchestrator/sameness/"*.txt` gives 0,0,0,0,0,1,1,2 = **4**; "SAME CONTENT, DIFFERENT STANDING" totals 1; "NEAR" totals 2; three files have none of the three (T05B, T05D, T10B), matching the results file's "three texts with no match at all". **The trail holds end to end.** It holds because the hand judgement is printed line by line and the results file says it is the orchestrator's (line 69: "the hand pairing above is the result, and it is mine").

**Claim 2 — "one plant of six reached the checker, four were refused repair by the translator" (Status, L66 bullet).**
Trail: Status → **L74** → `results/L66 Test results …` E1 (line 33) → `KEY.json` (opened, plants named) → the worker's translations. **Seen**: the four quoted refusals are in `L69 Return …/translations/P09_…md:55`, `P02_…md:36`, `P13_…md:29` and P08. **The trail holds.** I also ran the skill's nearest-innocent-neighbour check, which the record did not: `grep` for the same phrasing across the twelve *unplanted* passages returns one hit (P04, "not repaired or softened"), and in context it is a different sense. So 4 of 6 planted carry the note and 0 of 12 unplanted do. The reading survives a test the record never ran.

**Claim 3 — "rig 1 patches 1 to 16, rig 2 patches 1 to 3, **each with what it gives up**" (Status line 5).**
Trail: Status → project story, "What each patch gave up (kept from log 21 on)" → the driver. **The trail breaks.** The list holds rig-1 patches 1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 — not 2 and not 5. Both exist in code (**seen**, `run_check.py` line 116 and line 233), and patch 5 is self-described there as "forced by paragraph F, **fitted to that one paragraph**", which is exactly the kind of part the skill says to check first. `grep -rn "Patch 2\b" --include=*.md Language/` returns nothing in either record. The claim "each" is false and cannot be repaired from the record.

**Two further breaks found while tracing (both in Status, both in the same file as the claims above):**

- **A1.** Status says, in one sentence, both `"L72 Return - Astra Ultra" (received, checked, unchanged)` and `"L72 Handoff - Astra Ultra translates the eight texts of plan 37.md" (bundle sent, no return yet)` (**read**, Status line 6). The second clause is stale by one log entry (L73).
- **A2.** Status line 20, "Next steps", says "obtain and check the L66 worker return, then the reader's answers from reports alone, then open the key and mark E1 to E8. Check the modern passages' sources before conclusions" — all four were done at L69 and L74, and Status says so two bullets earlier ("The blind run marked (L66, worker Astra Ultra at L69, reader Astra Pro at L74)"). The Next-steps bullet is L67's pointer, carried forward unrevised.

**A3.** The project story's own header (line 5) still reads "Authority document: 'Claude Fable Semantics - standalone theory' (**file 10**…)", while Status line 5 says "the theory they rest on is now **file 11**". The log's header was not updated at L75.

**A4 — the qualification is dropped between layers.** The L66 results file carries Trap 3: "Taking the two modern passages as the dispute itself. They are the corpus maker's words, checked at abstract level only." Status reproduces the finding — "the for and against passages share two stated facts and differ by MAKES against SHOWS on one sentence, which 38 has no rule to weigh" — **without** the trap. At the summary layer the finding reads as a fact about the group-selection dispute. It is a fact about two passages the marker wrote.

### (b) Decisions: the owner's words, or the orchestrator's reading?

The file quotes the owner verbatim and never fabricates a quote. **That part is kept.** What is not kept is the separation the file's own trap demands ("Treating a routine choice made by Claude as one of your decisions").

- **L7.** Headline: "L64 accepted without strikes; go on." Owner's words: **"Perfect. What next"**. "Accepted without strikes" is the orchestrator's reading, and the record contradicts it elsewhere: the L64 thresholds are still open at L66 ("The threshold and the gauge are the owner's to set", results line 63) and still listed as "Held" in Status. Two words are carrying a ratification of a 19,000-byte contract.
- **L8.** Headline: "The blind test folded onto a new corpus; two corpora named; structure left to Claude and **approved as proposed**." The owner named the two corpora and said "I don't know how to structure this though" — both held. "Approved as proposed" comes from a *separate later turn*, "Great. Generate test instructions", spliced into the same numbered decision with "Then:". What that one word is made to cover: eighteen passages, six program alterations at seed 45 (two of them ungrammatical), two MAKES/SHOWS flips, a sealed key held by the marker, two modern passages written by the orchestrator from memory without a source lookup, and eight expectations written knowing the plants. The owner saw none of that when saying "Great".
- **L9.** Headline: "The two agents named and the work split." Naming and "both are always fresh from now on" are the owner's. "The work split" is not: the owner said "I **suppose** splitting the workload is a good idea now" — a hedge, recorded as a decision — and said nothing about which agent does which. The allocation is the orchestrator's, from its own assessment at L70 ("On the record, Ultra is the better worker…"), including "with no repository attached", which comes from Lesson L5, not from the owner.

**B1.** So each entry is *quote + unmarked gloss*, and the gloss is what the record then cites. This is the failure Lesson L3 already named and fixed for one instance (the lead-in above decision L5) without turning the fix into the convention its own words describe. Under file 11 Part IV, "A declared transport does not make an occurrence represent anything; it makes a modeller assert that it does." The headlines are declared.

**B2 — done without a decision the conventions require.** P9 says "the run waits for the go-signal for each phase." **L71 had no go-signal**: no owner request in its log entry, no decision between L9 and L71, and it is not one of decision L5's five steps. It is the entry that produced Lesson L6.

**B3 — tool changes with neither a decision nor a give-up note.** `Language/tools/install_scasp.sh` was **overwritten in place** at commit 37e33da (**seen**, two commits on that file; the diff replaces the T05-B smoke lines with ledger-A lines). Disclosed in the L72 log entry, but no decision, no give-up line, and it is an overwrite where the project's own later rule says "new versions beside the old" (L72 results line 63). `tools/consequences.py` was likewise overwritten at 20bb00f for the Lesson L4 parser fix; Lesson L4's fix kept *both runs*, not both programs.

**B4 — what was *not* done without a decision, and this is the strongest thing in the whole process.** `git log` on `rigs/rig 1 - arguments/patched/run_check.py`, `checker_rules.pl`, `authority/38` and `authority/39` returns **one commit each — the original import, 2b66b40**. In two days of testing that produced four findings the orchestrator itself calls forcing, not one line of the language or the checker was changed. "Nothing in the language or rigs changes without the owner's word" is kept, and it is checkable in thirty seconds.

### (c) Lessons: failures of the method, or of attention?

Sorted (**worked out** from the Lessons text):

- *The method's design:* L1 (one record, two chats), L5 (a brief's rule stated too quietly, and a worker given repository access).
- *A defect found in the instrument:* L2 (NO FAULT FOUND cannot tell answered from unaskable), L7 (`consequences.py` ignores worlds), L8 (near score ignores NOT), L4 (head parser crosses a line break).
- *The orchestrator's attention:* 51, L3, L6, L9.

**C1. The file does not tell them apart.** There is no field for the kind, and the one field that would partly do it — who caught it — is present in four entries (L2 "Found by the worker", L3 "Found by the owner", L4 "Found by reading the output", L7 "Found by Astra Ultra") and absent in five (L1, L5, L6, L8, L9). That is the record's most useful discriminator, applied to fewer than half.

**C2. L2 is not a lesson under the file's own convention.** Its "Fix:" — "the report should list the kinds of claim the ledger had none of; until then, read the raw log beside any NO FAULT FOUND" — has not been made (**seen**: `run_check.py` unchanged since import). It is an open defect filed as a closed one.

**C3. 51, L6 and L9 are one failure, and file 11 says what that means.** All three are: *a prediction written from a description, a memory or a picture of the thing, instead of from the thing.* L9 says so itself: "the same rule as Lessons 51 and L6, now three times" (**read**).

File 11 Part XI, (P): a repair requires an obligation that fails at ξ and holds at ξ′, and `ProducedBy(Δ,ξ,ξ′;O)` requires an **active route** from Δ to the repair; Part IX adds that "a route that started and did no work… is not active for that result; whether a route is active is read from the history, not from the result." Read the history:

- Lesson 51 was recorded on 21 September (log 58).
- The **L66 plan**, frozen later on 21 September, states E2 from a picture of the corpus and names a planted passage as its unplanted false alarm (**seen**, L66 results line 34, Lesson L9).
- The **L71 plan**, frozen 22 September, states C's premise from memory of a phrase in log 07: "the recorded run at log 07 found nothing and needed no patch" (**read**, L71 plan line 5). Wrong, and it cost the test its fault-free half.

So Lesson 51's Δ has no active route to either later plan. Under (P) the obligation was **not repaired**; Part XI's clause "a protected condition is lost exactly when it fails on an occasion it covers" applies twice. What the Lessons file recorded was a *declaration of an obligation*, three times, in three wordings, and the declaration is the only artefact. Part XIV puts obligations among the **declared inputs**, "each as a stated condition over stated occasions" — and these fixes declare no occasions they cover, so nothing in the record can show whether they were ever applied.

**C4.** For completeness: the recurrence *stopped* at L72, whose plan states its predictions from the orchestrator's own twenty-one lines, which it holds, and adds a "Known exposure" section (**read**, L72 plan line 19). But nothing in the record says the fix was applied there, and no gauge would show it either way.

### (d) Receipts (file 11 Part IX)

Part IX: "A record reconstructed from the claim it is meant to support is not a receipt for that claim." Part IV adds the sharper version: "a later record derived from the carrier is not a second, independent witness to its history."

**What the receipts are sufficient for.**
- *The inputs are the ones sent.* Byte comparison against files the orchestrator holds. **Seen**, L69: "the eighteen passages byte for byte the sealed corpus, the key not in the return"; L72 results line 6: "The return names the input zip by hash; it is the zip I sent (93606b71…)", which I confirmed against `Astra_Ultra_source_receipt.json` (`"input_zip_sha256": "93606b71bd7d…"`). This is a genuine route: the orchestrator holds the other end.
- *The checker's outputs are the worker's.* Reruns on the orchestrator's machine. **Seen**: `L72 Reruns …`, 16 of 16; `L69 Reruns …`, 13 files. Anyone can repeat this, so the history supplies the route (Part IX, active route).
- *The reader was blind.* The best receipt in the set, and it is a **negative** one: E7 records that the reader traced the sentence for **none** of seven findings and said so each time, and traced all four where the driver prints the sentence. Sight of the passages does not predict that. **Read**, L66 results line 39 and line 53.

**What they are insufficient for.**

- **D1. "The worker translated blind, in order, each closed before the next was opened."** This is the claim the whole L66 and L72 design rests on, and its only receipt is `Astra_Ultra_translation_sequence.jsonl` (L72) and the close-out hashes of L69 — files whose every record reads `"written_by": "Astra Ultra"` and `"next_text_opened_after_completion": true` (**seen**). The hashes in that file are hashes *of the very files it attests*, written at the end of the run (validation stamped `02:22:28`, the eight completions `02:10:15` to roughly `02:18`). A worker that translated all eight with the key in view, or out of order, and then wrote this file, would produce a byte-identical receipt. This is Part IV's case exactly: a later record derived from the carrier, offered as a second witness to its history. It would have come out in the project's favour whatever the world was like. Note that the record half-knows this: L72 log says "Not tested: … whether a fresh Astra Ultra follows the first paragraph", and L72 results line 11 marks E7 met partly on "no sign of the earlier ledgers" — which, by `testing-against-cases.md`, is *unknown*, not *absent*.
- **D2. The rerun sample at L69 is unexplained, and it skips exactly the cases a marked expectation rests on.** Thirteen of eighteen (**seen**, file list): P01, P02, P03, P07, P08, P09, P10, P11, P13, P14, P15, P16, P18. The five not rerun are P04, P05, P06, P12, P17 — every one of them a clean report. Two of them, **P12 (Kropotkin) and P17 (Darwin)**, are two of the four passages that carry **E3**, whose mark in the results file is "met" (**read**, L66 results line 35). So E3 is marked on reports that were never reproduced. No reason for the selection appears in L69, in the reruns read-me, or in the results file. (L72 has no such gap: 16 of 16.)
- **D3. Agent identity at L74 is self-report.** "it names itself ChatGPT, which is Astra Pro by decision L9" (**read**, L74). L70's trace-sorting is real evidence and I do not doubt it, but it establishes that *two harnesses exist*, not that *this reader session had not seen the corpus*. Only D's behavioural receipt reaches that, and it does reach it.

### (e) The division of labour

The one hand does: writes the plan and its expectations → builds the corpus → writes two of the eighteen passages → plants six alterations and two flips → seals the key and holds the passphrase → sends the bundle → checks the return → opens the key → marks → writes the results → writes the log entry → writes Status.

The skill's test — *is the answer already sitting in the starting points under another name?* — bites in three places, and file 11 names what is wrong with each.

**E1. Writing the modern passages and marking E4 must not be the same hand.** The L66 plan's question 3 asks (**read**, plan line 18): "does the sameness test show the same facts with a different point (the group-level general line **MAKES on one side, SHOWS on the other**)". The two passages were written by the asker. The result (L66 results line 36, and again at line 56, and again in Status) is that the two differ by a MAKES against a SHOWS. That is a property of the author's own composition returned as a finding. It is worse in the flipped pair, where `KEY.json` shows GS-5 and GS-6 are literally defined as "one sentence flipped MAKES to SHOWS" — the starting point *is* the conclusion. The results file's Trap 3 sees this; Status does not carry it (finding A4). The same hand also performed the **source check** that declares "Both passages are fair statements of their side at this level" (line 56) — the author grading the author.

**E2. Sealing the key and writing predictions that name passages must not be the same hand** — or, cheaper, the predictions must not be allowed to name passages. Lesson L9 is the proof that one hand cannot do both: the plan named Emerson's consistency passage as its expected *unplanted* false alarm, and the key that the same hand had sealed an hour earlier marks it planted. File 11 Part XIV: "where the input is missing, the verdict is unsettled and the semantics says so rather than choosing the input from the verdict wanted." Here the input was present, in a file the same hand had just written, and was supplied from memory instead.

**E3. Nobody checks the marking.** This is the hole. Astra Ultra saw the texts and never the plan; Astra Pro saw the reports and never the texts, the plan or the key. **No outside party has ever seen a plan and its outputs together.** So the step where the record's conclusions are actually made — E1 to E8, met / below / against — has no reader but its author. The record shows the cost: of the nine lessons, **L4, L6 and L9 were caught by the orchestrator re-reading its own work**, all three after the fact. Had it not re-read, nothing in the process would have surfaced them. That is the best rival explanation of why this project looks sound — *one careful person wrote everything down* — and the change list contains nothing that tells it apart from *the process caught the errors*.

**What may stay one hand.** Sending the bundle; checking hashes; the reruns. These are reproducible by anyone from the artefacts kept, so the history supplies an active route (Part IX) and a second hand adds nothing. Writing the plan and writing the results may also stay one hand, **because** git fixes the plan first: `git log` shows one commit per plan file, so the "against" column cannot have been tidied afterwards (**seen**). That is the freeze earning its keep.

**Provenance, in file 11's terms.** Part XIV's dependence order ends: "a representation justified only by its own construction, or an ownership and a capability justified only by each other, has not supplied its place in it." The L66 corpus's claim to test the language is justified by the corpus-maker's account of what the corpus contains; the marks on that corpus are justified by the same hand's reading of the same corpus. E4 and the source check are the two places where that circle closes completely.

### (f) "Numbered files are never overwritten; nothing changes without the owner's word"

**Kept, and checkably so:**
- **Seen**: `git log --oneline` on each of the five plan files (45, L65, L66, L71, L72) and the L66 Reader brief returns **exactly one commit each**. No frozen plan was edited after the run.
- **Seen**: `git log` on `run_check.py`, `checker_rules.pl`, file 38 and file 39 returns **one commit each — the import, 2b66b40**. The language and the rigs have not moved.
- **Seen**: no numbered authority or results file has more than one commit, except as below.

**Breached:**
- **F1.** `Language/tests/L60 Handoff - a new agent runs plan 45.md` — **two commits** (3b4b80c → 6563883), and the change is substantive: it moves the writing of the results file and the log entry from the worker to the orchestrator (diff **seen**). Disclosed in the log at L61 with the reason "in the file itself since it had reached no one". That exception is written nowhere in `RESEARCH-CONVENTIONS.md`, and the file carries no revision note — while `L66 Handoff … second version.md` carries one in its fourth line. The same situation, two treatments.
- **F2.** `Language/tools/install_scasp.sh` — **two commits**; the second (37e33da) replaces the smoke-test lines rather than adding a version beside them. No decision, no give-up line.
- **F3.** `Language/tools/consequences.py` — **two commits**; the Lesson L4 parser fix overwrote the program. Lesson L4's own fix says "the first run kept beside the second" — the runs were kept, the program was not. So the program that produced the first, faulty run is recoverable from git alone, not from the record.
- **F4, minor and disclosed both ways.** `L71 Test results …` was appended to after publication (the rebase note), which the conventions would put in a log entry; it was put in both.

**A receipt weakened by a rebase.** The L71 plan's freeze is claimed by commit hash: L71's entry says "Plan frozen first (L71, commit 936ce21)". The rebase renumbered it to 2b39096, and the record says so at L72 and again in the results file. The order survives (`git log` shows 2b39096 before the run commit 37e33da), and 936ce21 is still reachable **in this clone** (**seen**, `git cat-file -t 936ce21` → `commit`). A reader with a fresh clone will find nothing at 936ce21. A commit hash is a receipt that a rebase can void; nothing in the conventions says so.

### (g) Readable by a fresh agent in one sitting?

I timed the whole review: **468 seconds** of wall clock from opening the brief to the last check (**seen**, two `date +%s` calls). READ ME FIRST (19 lines) and Status (24 lines) took under two minutes of that. So the two files are *short*. They are not *sufficient*. What I could not find from them alone:

- **G1. Status names an authority that is not in the repository.** Line 5: "the skill is 33 (hardened)". **Seen**: `find` over the repository returns only `HV Skill/authority/30 Skill - hard-to-vary - modular, with router and map.skill`. L75 discloses that 33 is "not yet on main"; Status does not.
- **G2. The read order in READ ME FIRST is stale.** It sends a fresh agent to "The frozen plan in `tests/45 …` and the two packages in `results/`" — the oldest plan in the folder. It never mentions **L64, the scope contract**, which is the document every later test is run under, nor L66, L71, L72, nor file 11.
- **G3. Neither file defines a single term it uses.** Status uses *standing*, *GIVEN / CLAIMED / TOLD*, *told world*, *the bin*, *the gauge*, *MAKES*, *SHOWS*, *BECAUSE*, *SINCE*, *Thing line*, *derived facts*, *delta lines*, *what-if* — none glossed, none pointed at. "Authority: file 38 (the language)" is the only pointer, and file 38 is 16 KB.
- **G4. The labels that carry the open questions are opaque.** Status lists as still held: "F15 and F09", "R06", "F04's scope", "what '02' is". F09 and F15 are defined in one clause deep inside the copied log entry 45, a single paragraph of roughly 700 words. R06 and "02" are defined nowhere I could find in the four record files.
- **G5. Neither file names the four error sources**, though Status says "four error sources; scope first". They are in decision L4.
- **G6. Neither file points at `RESEARCH-CONVENTIONS.md`.** The rules the whole method rests on are two folders up and are never named from inside the project's record.
- **G7. Who Astra Pro and Astra Ultra are, and which does what,** is in decision L9 and log L70. Status uses both names as if known.
- Plus **A1, A2, A3**: a fresh agent following Status's Next-steps bullet would go and commission the L66 worker return that L69 already delivered.

**Answer:** readable in one sitting, yes. Trustworthy as the one thing read first, no — on three of the seven substantive things I checked, Status is stale or self-contradicting, and it fails J4, the job that puts it there.

### Other whole-explanation checks

- **Flip.** Had the work *not* been done as claimed, would the record differ? For the plan freeze: yes, git would show it. For the reader's blindness: yes, E7 would have traced sentences. For the worker's blindness and ordering: **no** — the receipts would be byte-identical (D1).
- **Reverse.** Poke the cause (remove the frozen plan) and the effect moves: the L66 results could not print "below the expected 2, not in the 'against' column" without a pre-fixed against column. Poke the effect (a different outcome) and the cause does not move: **seen**, one commit per plan. Not running backwards.
- **Add a job.** Can an outsider recompute a marked expectation? For L72 E1, yes — the hand pairing is printed line by line (results line 66) and I checked its program half against the sameness files. For L66 E1, the "four refusals" reading is printed but its innocent-neighbour check is not; I ran it and it holds. For L66 E4, no: it turns on text the marker wrote.
- **Pairs that pull.** (i) *"Decisions holds only the owner's words"* against *"a decision must be actionable"*: an owner who writes "Perfect. What next" has not settled the twenty things the next step needs, so the orchestrator settles them, and the file has no place to mark that it did. The line gives way on the orchestrator's side, silently. Signs the line is wrong: L7's gloss contradicted by "thresholds still held". (ii) *"The log is added to, never rewritten"* against *"Status is the summary"*: the log only grows, so Status must be rewritten, and rewriting is the only place error can enter unnoticed. It has, three times (A1, A2, A4). (iii) *One hand, nothing lost in handover* against *the answer must not be in the starting points* (E1–E3).
- **Check the patches.** Lesson L5's patch — a first paragraph forbidding the repository — worked, and worked twice (L69 and L73 both clean returns). It gives up nothing I can find, and the record does not claim it does. Lesson 51's patch did not work, twice (C3). Lesson L2's patch was never made (C2). The catch-all is the Lessons file's "Fix:" line; the gauge I ran on it reads *swallowing*.
- **Look inside.** Reruns match *outputs*, not *workings*. Two workers could reach the same reports by different routes; the whole of the translation step is outside what any rerun reaches (P10b).
- **What the change list leaves out.** No case where a worker returns a wrong result on purpose. No case where the orchestrator's marking is checked by anyone. No second reader. No run where the record is handed cold to a fresh agent and that agent's questions are recorded — my (g) is a one-off sample of that, and it found seven gaps.

---

## 5. What would make it harder to vary

1. **Give the marking a reader.** One fresh agent, given a frozen plan and the run's outputs and nothing else, marks E1 to E8 independently; the two markings are compared. This is the single change that closes E3 and that would tell the rival ("one careful person") from the claim ("the process catches it"). It costs one bundle.
2. **Give the Lessons file a gauge.** Each lesson states the occasions its fix covers (Part XIV's "stated condition over stated occasions"), and every later plan opens with a line saying which lessons' obligations it met and where. Run backwards over 51 it reads *failed at L66, failed at L71, met at L72* — which is what the record should have been able to say by itself.
3. **Mark the gloss in Decisions.** Lesson L3 already wrote the rule; apply it to the headline of every entry, not to one lead-in. Two minutes of editing; it would have stopped L7's "accepted without strikes" from standing beside "thresholds still held".

---

## 6. Lessons

Failures only, each with a location.

1. **Status is stale in three places and self-contradicting in two.** `Language - Status.md` line 6 (`"no return yet"` beside `"received, checked"`), line 20 (Next steps still asking for work done at L69/L74), line 5 (names skill 33, absent from the repository). Its own trap — "Letting this file drift from the project story" — is the thing that happened.
2. **A claim in Status is false and cannot be repaired from the record.** Line 5, "rig 1 patches 1 to 16 … each with what it gives up". Patches 2 and 5 have no give-up entry anywhere; patch 5 is self-described in `run_check.py:233` as fitted to one paragraph.
3. **The same failure three times, recorded as fixed three times.** Lessons 51, L6, L9. The L66 plan and the L71 plan, both frozen after 51 was written, both broke 51's rule. Under file 11 Part XI (P), none of the three entries records a repair; they record a declared obligation with no active route to any later occasion.
4. **The receipt for the claim the design rests on is derived from the thing it attests.** `L72 Return - Astra Ultra/Astra_Ultra_translation_sequence.jsonl`, and the L69 close-out hashes. File 11 Part IV: "a later record derived from the carrier is not a second, independent witness to its history."
5. **A marked expectation rests on evidence that was not reproduced.** L66 E3 is marked "met" on four passages, two of which (P12, P17) are among the five the L69 reruns skipped. The selection of thirteen from eighteen is nowhere explained.
6. **The author of two passages marked the expectation about those passages and checked their sources.** L66 E4 and the source check, results lines 36 and 56. The plan's question 3 states the answer it later reports.
7. **A numbered file was overwritten,** `tests/L60 Handoff …`, under an exception the conventions do not contain, and unlike the L66 handoff it carries no in-file note. Two tools, `install_scasp.sh` and `consequences.py`, were overwritten rather than versioned, with no give-up line for either.
8. **A phase ran with no go-signal.** L71: no owner request in the entry, no decision between L9 and L71, not one of decision L5's five steps. It is the entry that produced Lesson L6.
9. **Lesson L2's fix has not been made** and the entry does not say so; `run_check.py` is unchanged since import.
10. **The "how I know" tags slip at exactly the places they matter.** L73 tags "all sixteen runs repeated here and identical" as **worked out**; L74 tags "its nineteen source copies byte-identical" as **worked out**. Both are hash comparisons the orchestrator ran — **seen**. The record's own tag vocabulary is being spent on the wrong column.

---

## 7. The three lists

**Parts that never met a hard case.**
P12 (the reader never sees the key) met exactly one reader, once. P13 (L-numbering) has not met a second concurrent chat since it was introduced. P1 (append-only) has never met a case where an earlier entry was *wrong on fact*, only ones where it was out of date — L67 and the 1,145/1,146 file-count correction are both present-tense corrections. P11's split has never met a worker that returned something false.

**Findings that fit no part.**
- The four *quiet* things the process does that no written rule covers and that did most of the work I could verify: the `git` history itself as the freeze receipt; the "Known exposure" section invented for the L72 plan; the "Who is blind to what" section invented for the L66 plan; and the Traps sections at the foot of every results file. None is in `RESEARCH-CONVENTIONS.md`. The best parts of this method are unwritten and therefore unenforced — which is why they appear in two plans and not in the other three.
- The negative receipt (E7's refusals) is the one piece of evidence in the record that could not have come out otherwise, and nothing in the method says to look for that kind.
- L72's results line 57 — "Astra Ultra's line form copies the bundle's examples (the L62 return, by the same harness), so the two 'independent' translators are not independent of the examples" — is a finding about the *bundle-building* step that no part of the process governs.

**What I did not look at.**
The shared record before log 45 (`Checked reasoning language - *`, 254 + 59 + 65 + 38 lines). File 38 and file 39 themselves. `tools/sameness.py` and `tools/consequences.py` as code. Rig 2 and the bridge. The `HV Skill` and `Semantics` projects' records. The L66 reader brief and the L66 worker handoff beyond their first paragraphs. The full L74 audit (`L66_AUDIT.md`, `audit_protocol.md`) — I read only its README and evidence index, so my reading of the reader's protocol change rests on the orchestrator's account of it. Whether s(CASP) or the drivers do what the reports say.

---

## 8. What this does not show

Hard to vary is not true. Nothing above says the L66 or L72 results are wrong; on the two claims I traced fully (L72's 4-of-21, L66's four refusals) the artefacts were there and matched, and on one of them the reading survived a check the record never ran. Nothing above says the orchestrator fabricated anything; every gap I found is a gap in what the record *could show*, not evidence that something was hidden. And a loose part is not a wrong one: P9's go-signal rule and P2's owner's-words rule may be exactly right — they are simply not held in place by anything, so the record would look the same if they were being followed carefully or not at all.

I did not test the alternative process. A record with a second marker and a versioned tools folder would cost bundles and days; whether that is worth it is the owner's call, not a finding.

---

## 9. What would change my mind

- **On D1 (the worker's receipts):** a returned artefact the worker does not author — a harness-side transcript, an externally timestamped log, or a provider receipt — that fixes the order of the eight translations. Or: show me that a worker with the key in hand would produce a *different* sequence file, and the file becomes a receipt.
- **On E3 (nobody checks the marking):** one run in which a second agent marks the same frozen plan from the same outputs and the two markings are compared. If they agree line for line, the rival explanation weakens sharply.
- **On C3 (the recurring repair):** the L72 plan is evidence the recurrence stopped. Two more plans written from the thing itself, with the record saying which lesson's obligation each one met, and I would call 51 repaired at L72 and say so.
- **On (g):** a Status file with dated bullets that does not contradict itself, and a READ ME FIRST whose read order reaches L64. I would then hand it cold to a fresh agent and count the questions again; under three would change my mark on P4.
- **On F1/F2/F3:** if `RESEARCH-CONVENTIONS.md` is amended to say when a not-yet-sent file may be corrected in place and when a tool may be, these stop being breaches and become declared inputs. That is a two-line edit, and it would move P8 from *held if* to *held*.

---

## 10. One next step

Take the L72 plan and the L72 outputs, hand them to a fresh agent with the reader-brief treatment (plan and outputs only, no results file, no log), and have it mark E1 to E8. Compare with the orchestrator's marking, line by line, in a numbered results file. It is one bundle, it uses machinery that already exists, and it is the only test on this list that bites on the step nobody currently checks.
