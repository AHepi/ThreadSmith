"""Assemble draft model W7 from the three builders' returns (log W6), keeping their words."""
import json, os, re
D="Workflow/rigs/W6 builders"
A=json.load(open(f"{D}/builder_A-the-call.json",encoding="utf-8"))
B=json.load(open(f"{D}/builder_B-the-arrangement.json",encoding="utf-8"))
C=json.load(open(f"{D}/builder_C-the-practice-and-the-map.json",encoding="utf-8"))
out=[]
w=out.append

w("""# W7 Model - an LLM agent in the language of the semantics, file 11 (draft)

Assembled 22 September 2026 by Claude from the three builders' returns of log W6 (`rigs/W6 builders/`, kept unchanged), under plan W6 and its addendum, on the owner's word (decision W3: "11 is the new authority. Also, if the research is done and corpus compiled, time to describe LLMs within the language of 11. Use 5 Opus 5 agents with extra effort armed with current hard to vary to help."; decision W4: internet research permitted). This is the draft the two judges of plan W6 read; the frozen model is the numbered file that follows, with every edit their evidence forces. Nothing a builder marked loose, idle or unknown is promoted here; every place the builders disagreed is recorded in section 4; the assembly's own sentences are marked "assembly" and are the likeliest place for a seam to be papered over (W6 section 8).

The authority is Semantics file 11, read beside file 10 (decision W3; W5 section 1). Every quotation carries its Part and a file mark: "10 and 11", "10 and 11 (reworded)", "11 only". The model claims no class membership, no creativity, no knowledge and no Deploy for any agent (W3 section 4, last paragraph; file 11, Part 0: "It does not prove that any human, machine, institution or lineage belongs to the classes defined. It defines the classes."). The grain is text: what is in the context, what is emitted, and what changes in the emission when the context is changed.

## 1. The question the model answers, and the indices it is relative to

**The question** (W3 section 1). Which of the theory's objects does an agent built on a large language model instantiate at one call, which across calls, which only with a record or a harness around it, and which never; so that the skills the workflow needs, and the boundaries between them, can be drawn from it. The owner's six unknowns Q1 to Q6 are quoted in W3 section 1 and are the given jobs; each builder's added jobs are listed in section 2 under its slice, tagged as the builder's own, and a part held only by an added job is held if that job is real (file 33, Step 2).

**The grain, the boundary, the continuity: declared before any attribution.** File 11, Part XIV: "Grain \\(\\ell\\), boundary \\(\\beta\\), continuity \\(\\Omega\\), and the contract \\(C\\) are declared indices. Every claim is relative to them; none is a predicate that could be true or false." (10 and 11). Part XII: "A capability is attributed to a system under a declared boundary (which processes and resources are the system's) and a declared continuity \\(\\Omega\\) (what makes it the same system through change). ... Both are declared before the attribution, not chosen after it." (11 only). The grain is text (part A2 says what organization that adopts). The boundary: the system is the reader together with the program that builds and hands it its context; the record, the corpus and the owner are outside it; the skill's text once in the context is inside, and the work of writing it is outside (part B1). The continuity: what persists from one execution to the next, which differs by arm of phase 4 and is declared there (part B1).

**The unit.** One request to the language model is one execution; the context is what it reads and the emission what it writes (part A1). An agent turn with tool calls and a session are several executions; "across calls" below means across requests.

## 2. The parts

Thirty-four parts in three slices, in the builders' words. Each carries the sentences of file 11 it rests on (the first two are printed here; every one is in the builder's return), whether it is a construction, its mark with the holder quoted, its provenance, what would count against it, and the prediction it rests on. Marks are never added up; one part with no holder is one part unheld.
""")

def part_block(p, slice_name):
    w(f"### {p['id']} {p['name']}\n")
    w(f"**Statement ({slice_name}).** {p['statement']}\n")
    for r in p['rests_on'][:3]:
        w(f"- rests on [{r['file_mark']}; {r['part_heading']}]: \"{r['quote']}\"")
    if len(p['rests_on'])>3:
        w(f"- (and {len(p['rests_on'])-3} more sentence(s) in the builder's return)")
    w(f"\n**Construction.** {p['construction']}\n")
    w(f"**Mark.** {p['mark']}. **Provenance.** {p['provenance']}. **Holder.** {p['holder']}\n")
    w(f"**Would count against it.** {p['would_count_against']}\n")
    w(f"**Prediction.** {p['prediction']}\n")

for slice_name, v, title in (("builder A, the call", A, "2.1 The call (slice A)"), ("builder B, the arrangement", B, "2.2 The arrangement (slice B)"), ("builder C, the practice and the map", C, "2.3 The practice and the map (slice C)")):
    w(f"\n## {title}\n")
    w("**Jobs.**")
    for j in v['jobs']:
        w(f"- [{j['tag']}] {j['job']}")
    w("")
    for p in v['parts']:
        part_block(p, slice_name)

w("""
## 3. The table: every operation of the dependence order, placed

Builder C's placement rule (part C11) and its two riders govern the placement column; builder C placed all twenty-one operations with a quoted holder and none unknown (its count against W6.7, which said twenty rows; W3 section 6 lists twenty-one, and the correction is builder C's). Builders A and B placed the operations their parts touch. Where a builder's placement differs from builder C's, the difference is a difference of sense, which builder C's job J-C4 names: a column can say what *instantiating* the operation needs, or what *establishing* it needs, and "a row placed in one sense and read in the other is two claims". So the table carries both, and the assembly promotes neither: "To instantiate" is builder C's column; "To establish" is the column the other builders' placements turn out to be about, and where no builder placed the establishing sense, the cell is left empty rather than filled by the assembly.

| Operation (file 11) | To instantiate (builder C) | To establish (builders A and B, where placed, with their notes) | Holder quoted by C | Builder C's note, with what would move it |
|---|---|---|---|---|
""")
# merge: map C's rows by a key; attach A/B placements
def key(op):
    k=op.lower()
    for tag in ["(o)","(q)","contract","(k)","(e)","(s), (b), (d)","(r)","provenance","(k1)","deploy","build","(n), (g)","index","(p)","(ek)","receipts","(ct1), (ct2), can","(rc)","(u1)","rule","normative"]:
        if tag in k: return tag
    return k
ab={}
for v,name in ((A,"A"),(B,"B")):
    for r in v['operations_table']:
        ab.setdefault(key(r['operation']),[]).append((name,r))
for r in C['operations_table']:
    k=key(r['operation'])
    est=""
    if k in ab:
        est="; ".join(f"{n}: {rr['column']} ({rr['note']})" for n,rr in ab[k])
    holder=r['holder']
    move=r['note']
    w(f"| {r['operation']} | {r['column']} | {est} | {holder} | {move} |")

w("""
**Builder C's result (part C12).** Of the twenty-one operations, exactly one is placed by continuity alone: retention, (CT1) and (CT2). Every other operation that ranges over a history either carries an index the system cannot declare of itself (the boundary, the continuity) or needs a check made from outside the carriers. So the line phase 5 has to draw between skills is not chiefly between a stateful and a stateless agent; it is between what a call carries and what only a record or a program carries. Builder C marks this held if the placements stand, by P4.1 and P4.2.

**Builder C's strongest attack on its own table** (its report, "hunt the answer in the starting points"): the record column is defined to include a declared input from outside, and nearly every predicate about the agent carries a declared index, so the conclusion could be sitting in the rule; what stops it is C11's first rider, drawn between two failing swaps. A judge is asked to press there first.

## 4. Seams and disagreements, recorded (prediction W6.5)

The three builders worked apart on one sketch. Where their slices touch, each said what it assumed of the other; where they disagree, the assembly records it and promotes neither reading. The judges are told to press on each.

- **(R): unknown or at one call.** Builder A places (R) *unknown* ("the record's evidence is fitting and shows two responses the method does not license") and marks A8 held if; builder C places it *at one call* in the instantiating sense ("The fact obtains at the call if the transport's provenance obtains; nothing in the call makes it obtain and nothing in the call shows it") and says establishing it moves it to the record column. Two senses of one row; both stand in section 3. Builder A adds what C's row does not: (R) needs the skill's method written as an organization before it can be stated of a reader, and no slice built that.
- **(K): across calls or at one call.** Builder A: "A signature is a set over the whole contract and one call supplies one triple, so no kind is instantiated at one call" (part A3; across calls). Builder C: "on a document the admitted edits are edits to the text, which a call can make" (at one call, as an operation the agent performs on material handed to it). The difference is again J-C4's: a kind *of a component of the agent* is exhibited across calls; a kind-claim *about a document's parts* is an operation a call performs. Both stand.
- **Provenance of a transport: at one call or only with a record.** Builder A places the reader's own transport's provenance at one call ("present at every call ... held if the fourth clause holds"); builder B places the retrieval transports' provenance at one call; builder C places the row in the record column ("what it needs, of the three: a history"). C's sense is establishing (a provenance is "determined by its history in the physical module"), A's and B's is obtaining. Both stand.
- **(CT1), (CT2), Can: across calls, or split.** Builder B places (CT1) at one call for a task whose whole input is the context, (CT2) and Can in the record column ("what returns into the constructor attribute is only what the harness wrote down"); builder C places the row across calls by its first two tags and says Can needs the declared boundary. The disagreement is on (CT2): B reads the constructor attribute as fixed by what the rig re-sends (a harness), C reads retention as instantiated by continuity. The assembly leaves it to the judges; it bears on C12's result, which turns on this one row.
- **Deploy: unknown or only with a record.** Builder B: unknown, with the test named (a retained-use test across sessions with a declared use task); builder C: the record column (needs a declared input and a history). Not a contradiction: both say no phase reaches it; they differ on whether "unknown" is a placement (W6 section 4 says it is).
- **Build: unknown or only with a record.** Builder A places only the negative (relay is not construction; "the row is slice C's to carry"); builder C places it in the record column with two of the witness's four items supplied by the rigs. Both stand.
- **M7's "no physical interpretation" clause.** Builder B carries the clause as W5 left it (the record supplies no physical interpretation); builder C restates it (part C6): the instrumented runs supply "process occurrences, their ports, and the connections actually instantiated" through the run records and the tool audits, and the prose entries do not. Builder C's reading is narrower and cites the files; builder B's seam note anticipates the disagreement. The assembly keeps C6 as the part and records B's form as the reading it replaces.
- **M9: one part or five.** Builder C split M9 into C1 to C5, because it fused a claim about the theory with a claim about an arrangement; builder B's B1 assumes W5's single restatement. No contradiction; the split stands and B1's boundary line is the one C3 reads under.
- **Arm (d) as specified does not test M8b** (builder B, part B12): W3's arm (d) hands each call the document, the frozen question and one test, so a call handed the pull test can name its own pairs; B12 restricts P4.3 to an arm that splits the parts under test across calls. Builder C's table row for (S), (B), (D) names arm (d) as what would move the row. The restriction is carried into phase 4's plan as a change of the arm's design before it is frozen; P4.3's shape is unchanged.
- **Arm (c) confounds length with content** (builder B): an equal-length summary omitting the parts list is proposed as the arm's control. Carried to phase 4's plan.
- **The modules-opened trace** (builder C, part C4): in the transport phase 4 will use, the field is the reader's own report (`"modules_self_reported": True`), and P4.6 as written could be satisfied by a change in what the reader says it opened. Builder B's B7 uses the same trace as the record's holder for the router being live. C4's condition (the trace for arm (r) is taken from the transport's own record of tool calls) is carried into phase 4's plan; P4.6's shape is unchanged and P4.9 is added.
- **The W2 judging round as a partition observation** (W3 section 3): builder B drops it as evidence for M8b, with the quotation that forced it; the assembly follows, and phase 2's coverage map carries it only as a fact about that round.

## 5. The predictions

The model rests on W3's P4.1 to P4.7 as W5 leaves them, unchanged in count and shape, and on P5.1 and P5.2. The builders proposed the following new predictions, each a count that could fail, each marked with its builder; they are frozen here before the judges read the model, and phase 4's plan fixes their numbers:
""")
newp=[]
for v,name in ((A,"A"),(B,"B"),(C,"C")):
    for p in v['parts']:
        pr=p['prediction']
        if pr.lower().startswith("new") or "P-B" in pr[:12] or "P4.8" in pr[:60] or "P4.9" in pr[:60] or "P5.3" in pr[:60] or "PA." in pr[:40]:
            newp.append((name,p['id'],pr))
for name,pid,pr in newp:
    w(f"- **({name}, {pid})** {pr}")
w("""
Recorded as not reached by this programme (W3 P1.2; W6.2): the attention half of Q1 (part B11: no attention port at the grain of text; borrowed from the physical module); the generation half of Q5 (Build, part A9: no construction witness is supplied by any phase); the fourth clause of a selected provenance (part A6: the membership of a training history is not in this repository).

## 6. The word list

One row per term, merged from the three builders' lists (the builder is named; where two builders gave rows for one term, both plain words are kept and the term appears once). Every row quotes file 11 at the Part named with its file mark. Row marks follow W3 section 7: holds, loose, construction, contradicts.

| Plain word | Term | Part | File mark | Row mark | Meaning | Builder |
|---|---|---|---|---|---|---|
""")
seen={}
for v,name in ((A,"A"),(B,"B"),(C,"C")):
    for r in v['word_list']:
        t=re.sub(r"\s+"," ",r['term']).strip().lower()
        if t in seen:
            seen[t]['plain_word']+= f"; {r['plain_word']} ({name})"
            continue
        row=dict(r); row['builder']=name; seen[t]=row
for row in seen.values():
    w(f"| {row['plain_word']} | {row['term']} | {row['part_heading']} | {row['file_mark']} | {row['row_mark']} | {row['meaning']} | {row['builder']} |")

w("""
### Word list quotations (one per row, as the builders gave them)
""")
for row in seen.values():
    w(f"- **{row['plain_word'].split(';')[0]}** [{row['part_heading']}; {row['file_mark']}]: \"{row['quote']}\"")

w("""
### The eleven notions of file 10 the HV word list uses without a row (H69), each given a row or declined (W6.3)

Numbered as the H68 scout's `left_out` list numbers them.
1. **What an explanation is, the theory's one-sentence definition.** Row added by the assembly: *what the reader is asked to judge* — "An explanation is a **question-relevant organization of dependencies**, held to a target by a **transport** that is checked only by **what changes when things are changed**." (Part 0, 10 and 11). Used by the (E) row of the table.
2. **Obligations, and protected obligations.** Row: *what is to be mended and what must not be broken* (builder C).
3. **Repair, and that losses outside the protected set must be exposed.** Row: *every patch records what it gives up* (builder C).
4. **The finite monotone theorem, and the condition it needs.** Row added by the assembly, required: *when removing one part at a time settles anything* — "**Finite monotone theorem.** If \\(\\Gamma\\) is finite, \\(\\mathsf S\\) is upward closed, and \\(\\Gamma\\in\\mathsf S\\), then the critical singletons are exactly \\(\\bigcup\\min\\mathsf S\\) and the globally indispensable ones are exactly \\(\\bigcap\\min\\mathsf S\\)." and "The theorem applies only where its assumptions hold; an addition to \\(\\Gamma\\) that destroys a support is the interference case below, and there upward closure fails." (Part VI, 10 and 11; the second sentence 11 only). Used by the (S), (B), (D) row and by every mark of *held* and *idle* the judges give under W6.4.
5. **A substantive contrast must be one some admitted edit realizes.** Declined: the model makes no account claim with a contrast of its own; the notion belongs to the skill's word list and is in the HV ask (W3 section 12).
6. **Explanatory realism.** Row added by the assembly: *a system can be wrong about itself* — "Systems can be wrong about their transports, their observations, their criticisms and their own capacities." (Part I, 10 and 11 (reworded)). Used by parts A7, C4 and by W3 section 10's first weakness.
7. **A question can be wrong, including by combining incompatible requirements.** Row: *the question, and changing it mid-assessment* (builder B) covers the first two limbs; the third (incompatible requirements) is declined: no part of the model tests a job list against itself; it is the skill's and is in the HV ask.
8. **Grain, a declared index.** Row: *the grain of text* (builder A).
9. **Fallibility without falsehood-as-work.** Row added by the assembly, required: *a part can be wrong while another does the work* — "A theory may contain an accurate scoped dependence together with errors elsewhere. What cannot count as explanation is an error in the very dependence alleged to do the work." (Part I, 10 and 11). Used by the part-by-part shape of this model and of every report under it: parts are marked, the whole is not scored.
10. **The three provenances are told apart by history, not by output.** Row added by the assembly: *history, not output, tells the three apart* — "The three are told apart by their histories, not their outputs, and the semantics keeps them apart (Part IV)." (Part 0, 10 and 11 (reworded)). Used by parts A5, A6, B7, B9.
11. **Functional transport: fidelity on each generator gives fidelity on compositions.** Declined: the model tests no composed change; the licence for one-change-at-a-time is the skill's and is in the HV ask.

## 7. What the model does not claim

That any agent belongs to the theory's classes (Part 0, quoted above). That any agent is creative or creates knowledge: (N), (G) and (EK) are placed "never" at this grain in the table, with what would move them, and the placement is not a barrier claim ("A finite list of failures is not a barrier proof; a bypass refutes a proposed barrier.", Part XIII, 10 and 11). That any reader represents the skill's method (part A8: the record's evidence runs both ways and is fitting). That any reader deploys anything (Deploy: no phase reaches it). That a report in the skill's words shows construction (part A9: "Reconstruction by a learner is construction; relay is not.", Part X, 10 and 11).

## 8. What would make it harder to vary (the builders' own lists, merged)

- Record the request as sent and the number of requests per run (PA.1): three of slice A's parts turn on what a call actually read, and for the runs in the record that is an inference from code (builder A).
- Run arm (k), the one test that bears on A8 directly (builder A).
- Add the re-identification arm (PA.3): the one of Part IV's three primitive-layer edits that no arm runs (builder A).
- Give arm (c) an equal-length summary omitting the parts list, and make arm (d) split the parts and not only the tests (builder B).
- Take arm (r)'s trace from the transport's own record of tool calls, and run C4's poke pair: delete a module file; separately, change only the reporting instruction (builder C).
- Declare a protected set for one change in the repository and check preservation on its occasions (builder C).

## 9. What this does not show

Nothing here is a test of the model: every recorded run cited was read before the model was written and cannot confirm a part fitted on it. Hard to vary is not true. Every source read on the web is claimed, quoted with its address and the date, and a part held only by one is marked held if. File 11 is under test in the Semantics project's round S76; every quotation carries its file mark so that what rests on 11 alone can be found. Agreement between arms, when it comes, settles nothing about what any arrangement instantiates (parts A7, B3).

## 10. Traps

- Reading the table's "To instantiate" column as "shown": builder C's second rider separates them, and the "To establish" column is where the other builders' placements sit.
- Reading a "never" as a barrier claim.
- Reading a builder's "held if" as held: the job it is held on is named in each case, and most of slice C's rest on the plan's added job J-C2.
- Promoting a seam: section 4 records every disagreement, and the assembly resolved none.
- Reading agreement between arms as sameness of organization (Derivation 9, parts A7 and B3).
""")
os.makedirs("Workflow/authority", exist_ok=True)
path="Workflow/authority/W7 Model - an LLM agent in the language of the semantics, file 11 (draft).md"
open(path,"w",encoding="utf-8").write("\n".join(out))
print(path, len(" ".join(out).split()), "words;", len(seen), "word-list rows;", len(newp), "new predictions")
