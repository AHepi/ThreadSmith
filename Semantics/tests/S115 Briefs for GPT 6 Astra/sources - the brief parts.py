# Holds the task part and return part of each S115 brief for GPT 6 Astra.
# The assembling script joins each with the shared context into one self-contained file.

COMMON_RETURN_TAIL = """
Every section must follow the wording rules above. At most {words} words in all, plus any appendix of configuration or code. End the document with the line `END OF REPORT`.
"""

BRIEFS = [
    {
        "number": "01",
        "title": "Measuring what is learned, with stock Avida only",
        "why": "Uses a strength the earlier reviewer showed (reading Avida's source exactly) and avoids its weakness (designs that need thousands of lines of unwritten C++). Everything asked for here must run on unmodified Avida 2.14.0, so it can be run the same day.",
        "task": """## Your task

Design a set of measurements of **what a program population has learned, and whether it keeps learning**, that runs on **unmodified Avida 2.14.0**. Use only its analyze mode, its event and print actions, its saved population files, and its task library. The measurements will be applied to saved program populations like those described above, which are saved every 1,000 or 10,000 updates.

Cover at least these:

1. **Capabilities never rewarded.** Use Avida's own task library as a probe battery. It has 214 task names, including the 68 three-input logic tasks and 56 arithmetic tasks (`math_1AA` …, `math_2AA` …, `math_3AA` …), besides `echo`, `add`, `sub` and others. Specify:
   - how to test every living distinct instruction sequence of a saved population against the whole battery, on several sets of input numbers;
   - how to keep the rewarded tasks separate from the never-rewarded ones.
2. **Retention.** For snapshots at several updates, specify:
   - which capabilities present earlier are still present later;
   - how to tell a capability being kept from one being re-found.
3. **First appearance and program ancestry.** Specify how to find, from saved data (for example with `save_historic`, the parent IDs and phylogenetic depth in `.spop` files, or Avida's lineage outputs), the line of ancestors that led to the first program performing a task, and the instruction changes along it. State exactly what must be switched on in `avida.cfg` or `events.cfg` before a run for this to be possible.
4. **Reuse.** Specify how to test, by instruction ablation along an ancestor–descendant line, whether a later capability depends on instructions that an earlier capability already required.
5. **Standard measures of open-ended dynamics.** For example, Bedau and Packard's evolutionary activity statistics, or the change, novelty, complexity and ecology measures of the MODES toolbox (Dolson, Vostinar, Wiser and Ofria), both from memory and so to be checked. Say which can be computed from stock Avida outputs, and how.

For each measurement give:
- the exact analyze-mode script, or event lines;
- the exact `avida.cfg` settings it needs;
- the output columns it produces;
- how to compute the measure from them;
- its cost in CPU time, estimated from how much work it does;
- what could make it mislead.

Check every command, argument and column name against Avida's source (github.com/devosoft/avida, `avida-core/source/analyze/cAnalyze.cc`, `cAnalyzeGenotype.cc`, `source/actions/PrintActions.cc`, `SaveLoadActions.cc`, `source/main/cTaskLib.cc`, `cEnvironment.cc`), and give the file and function for each. Mark anything you could not check.
""",
        "return": """## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **The measurements.** One subsection per measurement, with everything listed above.
3. **What must be switched on before a run.** A single `avida.cfg` and `events.cfg` fragment that makes all the measurements possible on future runs.
4. **What can be measured on runs already saved without those settings, and what cannot.**
5. **Source locations checked.** File and function per command used.
6. **Assumptions and what you are unsure of.**

**Appendix.** Every script, complete and ready to paste.
""",
        "words": 5000,
    },
    {
        "number": "02",
        "title": "Evaluation inside the program population, with stock Avida features",
        "why": "The owner's open question is how the choosing can happen inside, rather than only in the execution environment. The earlier reviewer's design for this needed new C++. This brief asks whether Avida already has the parts, which suits a reader of source code.",
        "task": """## Your task

In every run so far, all the choosing is done by the Avida execution environment: instruction changes plus the removal of programs that do not replicate or earn less. No program evaluates anything.

**Find every mechanism already present in Avida 2.14.0** by which Avida programs act on, test, choose among, or respond to other programs or their outputs. Search the source for at least the following, and report what you find, including absences:
- sexual reproduction and recombination, and any mate-choice or mate-preference instructions;
- demes and group-level selection (for example deme competition and replication events);
- parasites or code injection between programs;
- predator–prey instructions;
- messaging or communication instructions between programs;
- opinions or sensing of other programs' states;
- cooperative or public-good tasks;
- any instruction sets other than the standard "heads" set that enable these.

For each mechanism give:
- the source files and functions;
- the instruction set it needs;
- the configuration switches it needs;
- whether it runs with the standard heads instruction set or needs another;
- what "one program evaluates another" would mean with it, concretely.

Then **design two or three experiments**, using only stock Avida 2.14.0, in which evaluation of candidates is carried out by programs, and those evaluators can themselves change by instruction change and computational selection. For each, give:
- the exact `avida.cfg`, `environment.cfg`, `events.cfg` and instruction-set files;
- the starting program(s). If the default ancestor cannot use the mechanism, say what minimal hand-written ancestor would be needed, written in the instruction set's own mnemonics;
- controls, at minimum:
  - evaluators frozen at a given update;
  - evaluators' decisions shuffled;
  - the mechanism switched off;
- the measurement that would distinguish "evaluation inside" from plain computational selection;
- the result that would count against it adding anything;
- the cost in CPU-hours on the machine described.

If Avida 2.14.0 has no mechanism that can do this without source changes, say so plainly, and give the smallest source change that would, as a unified diff against the named files at commit 47f13dad, with its size in lines.
""",
        "return": """## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **Mechanisms found in Avida 2.14.0.** One entry per mechanism, including those searched for and not found.
3. **Experiments.** One subsection per design, with every item listed above.
4. **If source changes are needed.** The smallest change, as a diff, with its size.
5. **Source locations checked.**
6. **Assumptions and what you are unsure of.**

**Appendix.** Complete configuration files, instruction-set files and ancestor sequences, ready to paste.
""",
        "words": 5000,
    },
    {
        "number": "03",
        "title": "The execution environment as a knowledge creator, in constructor theory's terms",
        "why": "Uses the model's strength at careful reasoning. It guards against the weakness of drifting into abstraction by requiring predictions that can be run in Avida, and a plain summary.",
        "task": """## Your task

**Constructor theory, briefly** (from Deutsch and Marletto; check against their writing where you can):
- It describes the world by which **tasks** (transformations of physical systems) are possible or impossible.
- A **constructor** is something that can cause a task and stay able to cause it again.
- **Information** is carried by a medium whose states can be set and copied.
- **Knowledge** is information that can act as a constructor and cause itself to remain instantiated: in the owner's words, information that can cause itself to be copied, to resist change, and to remain.
- Marletto tests for knowledge by asking what one would ultimately have to eliminate to stop a particular transformation from being performed reliably.
- On this account, the laws of physics contain no design, so knowledge arises only by processes such as variation and selection, or by thinking. Error correction is what keeps anything complex from wearing away.

**The task.** Using that framework precisely:

1. **The pieces of Avida.** Describe the Avida set-up above as constructor theory would:
   - What are the tasks, the constructors, the information media and the knowledge?
   - What is the execution environment's role: constructor, substrate, or something else?
   - Where is error correction, and who does it?

   Stay with the measurements given.
2. **What such an environment would need.** State, as precisely as you can, what an execution environment would have to be able to do for it to create new knowledge **progressively**: new tasks becoming possible for the program population over time, rather than a fixed list being exhausted.
3. **Two kinds of creation.** Distinguish knowledge creation by variation and computational selection, which Avida's runs show, from the kind Deutsch calls creative or explanatory. Say what, in constructor theory's terms, the second would add, and whether anything in an Avida-like system could have it.
4. **Things to try in Avida.** For each condition you state in 2 and 3, derive at least one prediction that Claude can test in stock Avida 2.14.0, or with a change you specify. Give:
   - the exact set-up;
   - what result would count against the condition.
5. **Where it cannot be settled.** Say where constructor theory, as published, does not settle the question.
""",
        "return": """## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **The Avida set-up in constructor theory's terms.**
3. **What a progressive knowledge-creating execution environment would need.** Each condition numbered.
4. **Evolutionary and explanatory knowledge creation.**
5. **Predictions to test.** One per condition, each with its set-up and the result that would count against it.
6. **Where constructor theory, as published, does not settle it.**
7. **Sources.** Each labelled "checked" or "from memory". Book quotations at most 25 words each.
8. **Assumptions and what you are unsure of.**
""",
        "words": 5000,
    },
    {
        "number": "04",
        "title": "Testing the owner's claim that the execution environment is the clue",
        "why": "A fresh instance has no stake in the owner's framing, so it can argue both sides fairly. The earlier reviewer already called the claim 'loose as an exclusive claim' without testing it. This brief asks for the test.",
        "task": """## Your task

The owner wrote: "The execution environment is an important clue. Looking inside the machines is the wrong direction."

1. **Argue for it.** Make the strongest case that what the program population learns, and whether it keeps learning, is decided by the Avida execution environment, not by anything inside the programs. Use the measurements above.
2. **Argue against it.** Make the strongest case that what happens inside the programs matters too. For example:
   - how their circuits are built;
   - how robust they are to instruction changes;
   - whether earlier circuits can be reused.

   Use the measurements above too.
3. **Where the two part.** Say where the two accounts predict **different** results in Avida, not just describe them differently.
4. **Experiments that tell them apart.** Design two or three experiments, runnable on stock Avida 2.14.0, that would tell the accounts apart. For example:
   - transplant evolved programs into new environments;
   - start identical environments from programs with different internal structure;
   - swap environments mid-run using continuous events rather than save and reload.

   For each, give:
   - the exact configuration and event files;
   - seeds and length;
   - its cost on the machine described;
   - what each account predicts;
   - the result that would count against each.
5. **What would be left open.** Say what these experiments would not decide.
""",
        "return": """## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **The case for the environment.**
3. **The case for the programs.**
4. **Where they predict different results.**
5. **Experiments.** Each with every item listed above.
6. **What the experiments would leave open.**
7. **Assumptions and what you are unsure of.**

**Appendix.** Complete configuration and event files.
""",
        "words": 4500,
    },
    {
        "number": "05",
        "title": "Open-endedness research, checked, and mapped to these runs",
        "why": "Uses the strength of checking references with their DOIs. It fills a gap in the earlier reviewer's list, which left out the standard measures of open-ended dynamics.",
        "task": """## Your task

Survey the research on **open-ended evolution and open-ended learning in artificial-life and evolutionary-computation systems**, and map it onto this project's question and runs. Include at least the following, if they exist. Each is from memory and must be checked:
- Bedau and Packard's evolutionary activity statistics (1990s);
- Bedau and colleagues' classes of evolutionary dynamics;
- Channon's work applying activity statistics to Geb;
- Taylor and colleagues, "Open-ended evolution: perspectives from the OEE workshop in York" (Artificial Life, 2016);
- Packard and colleagues' overview of open-ended evolution (Artificial Life, 2019);
- Dolson, Vostinar, Wiser and Ofria, "The MODES toolbox: measurements of open-ended dynamics in evolving systems" (Artificial Life, 2019);
- Soros and Stanley on minimal criteria and open-endedness (ALIFE 2014);
- Stanley, Lehman and Soros, "Open-endedness: the last grand challenge you've never heard of" (2017);
- Banzhaf and colleagues' definitions of novelty, innovation and emergence (Theory in Biosciences, 2016);
- any Avida studies of open-endedness or of the accumulation of new capabilities.

For each work:
- the full reference with its DOI or a stable link, labelled "checked" or "from memory";
- two or three lines on what it claims or measures;
- **how its measure could be computed on the runs described above**, from Avida's saved outputs, as an exact procedure, and whether stock Avida 2.14.0 outputs suffice;
- what the measure could mislead about in this set-up.

Then say which of the six running environments, and which of the earlier reviewer's proposals, each measure would bear on. Say what, if anything, the literature already reports about environments like "growing list" and "common tasks pay less". Do not rank the measures.
""",
        "return": """## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **The works.** One entry each, with every item listed above.
3. **Which measure bears on which environment or proposal.** A table.
4. **What the literature already reports about growing and depleting environments.**
5. **Works searched for and not found.**
6. **Assumptions and what you are unsure of.**
""",
        "words": 5000,
    },
    {
        "number": "06",
        "title": "An independent review of the earlier reviewer's report",
        "why": "Fresh instances are independent, which is their strength here. One can check another's work without anchoring on it. The earlier report is attached in full below the task.",
        "task": """## Your task

Below this task is the **complete report of the earlier, independent reviewer**, another instance of a model, answering a brief much like the context above. Review it adversarially and fairly:

1. **Its claims about Avida's source.** For each checkable claim about Avida 2.14.0 (what saving and reloading a population keeps and loses; reward semantics; task recording; resource products; configuration defaults; command syntax), check it against the source at github.com/devosoft/avida. Mark it "holds", "holds in part" or "does not hold", with file and function.
2. **Its critique of the six environments.** Which points are sound? Which are overstated? Which were missed?
3. **Its designs B1, B2, B3 and C.** For each, give:
   - whether the design does what it claims;
   - where a designer-fixed rule still decides what counts as a new problem;
   - whether its controls separate what they are meant to separate;
   - whether its cost estimate is plausible.
4. **Smaller versions.** For each design, propose the smallest version that could run on stock Avida 2.14.0, or with a source change of at most about 200 lines. Specify it exactly, including files, and give its cost.
5. **Its measures and references.** Check the references it labels "checked", and note important work it left out.
6. **What the owner should take from it.** State what the report adds and what it does not, without ranking.
""",
        "return": """## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **Source claims checked.** A table: claim, verdict, file and function.
3. **The critique of the six environments, reviewed.**
4. **Designs B1, B2, B3 and C, reviewed.**
5. **Smaller versions.** Exact specifications and costs.
6. **Measures and references, reviewed.**
7. **What the report adds, and what it does not.**
8. **Assumptions and what you are unsure of.**

**Appendix.** Configuration files and diffs for the smaller versions.
""",
        "words": 5500,
        "attach": "S114 Return from GPT 6 Astra - execution environments report.md",
    },
    {
        "number": "07",
        "title": "A small source patch: a bounded test runner for Avida's analyze mode",
        "why": "Many proposed measures, such as testing programs on problems nobody rewarded, need a way to run one program on given inputs and read all its outputs. This brief asks for that one piece as a small, reviewable patch. It plays to the model's source-reading strength and keeps the unbuildable part small. Claude will compile it and report back.",
        "task": """## Your task

Write a **small C++ patch** to Avida at commit 47f13dad (github.com/devosoft/avida). It adds an **analyze-mode command** that does the following:
- takes the currently loaded batch of distinct instruction sequences;
- for each sequence, and for each of a list of input triples read from a file, executes the sequence on Avida's test CPU:
  - with fresh CPU state;
  - with no instruction changes;
  - with no births into any population;
  - with no rewards;
  - up to a given instruction budget;
- feeds the inputs through the ordinary `IO` instruction, three numbers in the order given, repeating in rotation as Avida normally does;
- records, per sequence and per triple:
  - every output value in order;
  - the number of reads;
  - the number of instructions executed;
  - whether it divided;
  - whether it hit the budget;
- writes one line per sequence and triple to a named output file, with the columns documented.

**Requirements:**
- Keep it as small as possible, and reuse `cTestCPU` and `cCPUTestInfo` where they already provide this.
- Deliver a unified diff against the exact files at that commit.
- Include:
  - build instructions (Avida builds with cmake; say whether `avida-core/CMakeLists.txt` needs a change);
  - a test: an analyze script and an input file that runs the command on Avida's default ancestor and on two hand-written sequences whose outputs you work out by hand;
  - the expected output lines.
- Say precisely how this command differs from Avida's existing `RECALCULATE` with manual inputs, and why that is not enough, or, if it is enough, say so and stop.
- If you cannot compile, say so. Claude will compile it and send the compiler's messages to a fresh instance if it fails, so make the diff easy to read and each change self-explanatory in a one-line comment.
""",
        "return": """## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 150 words, everyday language: what the tool does, with an example.
2. **Why `RECALCULATE` is or is not enough.**
3. **The design.** Which existing classes are reused, and the output format.
4. **The diff.** Complete, unified, against commit 47f13dad.
5. **Build instructions.**
6. **The test.** Script, input file, the two hand-written sequences in mnemonics, and the expected output lines with how they were worked out.
7. **Assumptions and what you are unsure of.** Including whether you compiled it.
""",
        "words": 4000,
    },
    {
        "number": "08",
        "title": "A growing supply of problems, using only stock Avida",
        "why": "The earlier reviewer's designs for problems that come from the program population needed new C++. This asks what can be done with Avida's own resources, products, requisites, cascades and events, which can be run at once and compared with the six environments now running.",
        "task": """## Your task

Design **two to four Avida execution environments**, runnable on **unmodified Avida 2.14.0**, in which the set of problems that pay grows or changes **as a result of what the program population does**, not on a schedule and not from a list the designer ranks in advance. Use only Avida's own machinery, for example:
- resources that deplete and flow in (`RESOURCE`);
- reactions that produce resources other reactions use (`process:product=...`);
- requisites on earlier reactions (`requisite:reaction=...`, `requisite:noreaction=...`);
- cascade environments (Avida ships example files such as `environment-cascade.cfg`: check them);
- spatial resources, gradients and cell-local resources;
- demes;
- events that fire at updates, including any that respond to population statistics.

Save-and-reload between pieces may not carry resources across. Prefer designs that run **continuously**.

For each design, give:
- a plain description with an everyday example first;
- the complete `environment.cfg` and `events.cfg` (plus any `avida.cfg` changes), with every line checked against `avida-core/source/main/cEnvironment.cc`, `cTaskLib.cc` and `source/actions/*.cc`;
- how the population's own activity changes which problems pay, step by step, and where the designer's own choices still decide what counts;
- what a new capability means in it, and how to count capabilities that were never rewarded, using the 77 logic tasks and Avida's arithmetic tasks as a probe battery;
- its prediction, and the result that would count against it;
- how to compare it fairly with the six environments above (same ancestor, world, copy error rate, length, seeds);
- its cost in CPU-hours on the machine described.
""",
        "return": """## Return exactly this

A single document with these sections in this order:

1. **Summary for the owner.** At most 250 words, everyday language, one concrete example first.
2. **The designs.** One subsection each, with every item listed above.
3. **How they would be compared with the six running environments.**
4. **Source locations checked.** File and function per keyword used.
5. **Assumptions and what you are unsure of.**

**Appendix.** Complete `avida.cfg` changes, `environment.cfg` and `events.cfg` for each design, ready to paste.
""",
        "words": 5000,
    },
]
