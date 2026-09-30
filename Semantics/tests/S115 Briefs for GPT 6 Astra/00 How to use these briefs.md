# How to use these briefs

*For the owner. Written by Claude on 30 September 2026 (log S115, decision S66).*

## What Astra's first reply showed

**Where it was strong:**
- **It read Avida's code closely.** It found something that may matter for the runs going on now: saving the program population and loading it again between pieces does not carry everything across. Resource levels, for example, may be lost. A worker is checking that right now with a small test.
- **It spotted a gap in our own descriptions.** Our Avida runs also added or deleted one instruction at 5% of divisions, and our write-ups never said so. It was right. A correction is being recorded.
- **It designed careful controls,** such as freezing a part at a set time, replaying another run's history, and shuffling decisions. These separate real effects from coincidences.
- **It checked its references** and gave links for them.
- **It was honest** about what it had not checked.

**Where it was weak:**
- **It could not run anything.** It could not build Avida, so none of its designs has a result yet.
- **Its best designs need a lot of new code:** about 1,000 to 2,000 lines of C++ added to Avida's source. Nobody has written that code, compiled it or tested it.
- **Its writing is dense** and hard to read without a programming background.
- **It missed standard ways of measuring "keeps learning".** For example, it left out the research on measuring open-ended change.
- **It didn't know the project's wording rules,** and slipped into verdicts in places.

## How the new briefs use that

**Every brief is self-contained.** Each carries:
- all our Avida results so far;
- your question in your own words;
- your Avida terms and the wording rules;
- a note that the model is a fresh agent that cannot see other replies.

Paste everything below the line in each file into a fresh Astra.

**Most ask for things that run on Avida as it is,** with no new code. That way Claude can run them the same day.

**The one brief that asks for code (07)** asks for a single small piece that others depend on. Claude will compile it and report back.

**Brief 06** has the first reply built into it, so a fresh Astra can check it independently.

## The eight briefs

| Brief | What it asks for | Why this one |
|---|---|---|
| 01 | Ways to measure what a program population has learned, and whether it keeps learning, using Avida as it is | Runs today; uses its code-reading strength |
| 02 | Whether Avida already has ways for programs to judge other programs, and experiments using them | Your "choosing inside" question, without new code if possible |
| 03 | Your question in constructor theory's own terms, with predictions to test in Avida | Its reasoning strength, kept concrete |
| 04 | The best case for and against "the execution environment is the clue", and experiments that tell them apart | A fresh agent has no stake in your framing |
| 05 | The research on measuring open-ended change, checked, and how each measure applies to our runs | Fills the gap in the first reply |
| 06 | An independent check of the first reply, with smaller versions of its designs | Fresh agents check each other without being led |
| 07 | One small piece of new Avida code: a tool that runs a program on given inputs and records all its outputs | Many measures need it; kept small |
| 08 | Execution environments whose problems grow from what the programs do, using Avida as it is | The first reply's main idea, without new code |

## How to run them

- **Order:** they can all go at once, one fresh agent each. None depends on another's answer.
- **Max or Ultra:** the owner explained that Ultra means several helper agents working at once, each of which can be set to max. So use Ultra, with every helper at max, for the briefs that split into separate pieces that can be checked side by side: 01, 02, 04, 05, 06 and 08. Use a single agent at max for 03 (one line of reasoning that must hang together) and 07 (one small piece of code that must fit together). Leave these two out of Ultra, because pieces done separately may not join up.
- **What to bring back:** upload each reply here as it comes. Put the brief's number in the file name if you can.

Claude will check each reply's statements about Avida against its code before running anything. Replies can propose runs, but nothing is run without being checked first.
