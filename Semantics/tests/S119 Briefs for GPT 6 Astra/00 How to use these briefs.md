# How to use these briefs

*For the owner. Written by Claude on 1 October 2026 (log S119, decision S73).*

## What they are for

You said the execution environment is the thing under test: it does the selecting, as an autonomous agent does (S72). You asked whether it can have an instinct to solve problems without being given exact targets (S71).

The four briefs below each take one side of that question. The S118 pilots are still running and their results are not in, so no brief assumes how they come out.

## Each brief carries everything a fresh Astra needs

Each brief includes:
- your three statements (S63, S71, S72), in your words;
- your Avida terms, the full table;
- what the earlier runs found;
- the three grades of "naming a target", used to say how far each idea really leaves the target unnamed;
- what to send back, section by section, ending with `END OF REPORT`.

Each brief also tells Astra:
- to say plainly if it cannot run Avida;
- to paste the output of anything it does run;
- never to claim a result it did not run;
- never to write self-replicating code that runs on a real machine.

## The four briefs

| Brief | What it asks | Why | Run it as |
|---|---|---|---|
| 01 | A small change to Avida's code: the world hands in numbers that follow a hidden rule, and pays a program whose output matches the next number. The rule is never named to the selector. | It is the one kind of selector that stock Avida cannot make (S118). It copies the form of the last brief whose code worked. | **Single agent at maximum**: one small patch must fit together. |
| 02 | A selector with a memory: it pays most for what the programs are getting better at fastest, or for behaviour it has not seen before. First stock Avida, then the smallest code change. Includes controls and enough runs to tell a difference. | It is your "selection as an agent does it" in its simplest working form. | **Ultra, every helper at maximum**: the stock design, the code alternative and the sizing can be done side by side. |
| 03 | Research, every source checked: what is known about selectors driven without a fixed target, and what each would cost in Avida. | So that nothing already known is reinvented, and so we know where nothing is known. | **Ultra, every helper at maximum**: each line of research can be checked separately. |
| 04 | What an autonomous agent's selection has and Avida's lacks, item by item. For each item: the smallest addition and a test in Avida. | It takes your comparison literally and makes each part testable. | **Single agent at maximum**: one line of reasoning whose items depend on one another. |

## How to run them

1. Open each file in this folder.
2. Copy **everything below the line** (the `---` near the top) into a fresh Astra.
3. They can all go at once. None depends on another's answer.

## What to send back

- Save each reply **unchanged** as a file.
- Put the brief's number in the file name, if you can.
- Upload the files here.

Claude will check each reply against Avida's code before anything is run.
