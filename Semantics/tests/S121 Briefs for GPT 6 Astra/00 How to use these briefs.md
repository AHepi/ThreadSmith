# How to use these briefs

*For the owner. Written by Claude on 1 October 2026 (log S121, decision S75).*

## Where I think you are going

Yes, I think I see it. Every Avida program studied so far gives its answer from the numbers it is handed at that moment. It has no "before". What we found missing (prediction, surprise, holding a problem open) all needs a "before": something earlier changes how the system responds now. Your report shows cheap units that do exactly that: a fading trace, a response that tires with use, a switch that stays on, a detector for "A then B".

So the idea is: build the selector (the execution environment, S72) out of units like these, so that its instinct is the way it behaves over time, not a list of targets someone wrote. And give the programs tasks that need a "before" too.

Your report's own caution is kept in every brief: timing adds nothing that ordinary logic with memory cannot do. Any gain is in how cheaply and simply it does it, and that has to be measured.

## The four briefs

| Brief | What it asks | Why | Run it as |
|---|---|---|---|
| 01 | Design the selector as a small system of fading traces, tiring responses, switches that hold a problem open, and "A then B" units, with controls that wipe its memory. | It is your idea most directly: an instinct made of behaviour over time. | **Ultra, every helper at maximum**: the units, the driver, the controls and the sizes can be worked side by side. |
| 02 | A small change to Avida's code: tasks only a program with a memory can do ("A then B", "two events close together", "A, B, C in order"). Builds on Astra's last patch. | So the programs, not only the selector, have something that needs a "before". | **Single agent at maximum**: one small patch must fit together. |
| 03 | Research, every source checked: where traces, tiring and surprise are already used to judge or select; and a check of your report's 22 sources. | So nothing known is reinvented, and so we know which of the report's sources hold. | **Ultra, every helper at maximum**: each mechanism and each source can be checked separately. |
| 04 | Gap by gap: can a selector built of these units supply what we found missing? What still needs something written down? And the one test that would tell a selector with a memory from one without. | It tests whether the idea really closes the gaps, before costly runs. | **Single agent at maximum**: one line of reasoning whose parts depend on one another. |

## If you run only one

**Run brief 01.** It is the one that tests your idea itself: the selector with an instinct made of its own behaviour over time, against the same selector with its memory wiped. The others support it (02 gives the programs harder material, 03 checks what is known, 04 checks the reasoning). None needs another's answer.

## How to run them

1. Open each file in this folder.
2. Copy **everything below the line** (the `---` near the top) into a fresh Astra.
3. **Attach your report** (`Temporal_Neuron_Computation_Report.docx`) to every brief. For brief 02, also attach Astra's earlier reply `01 Return - paying for anticipating what the world hands in next.md` if you can.
4. They can all go at once.

## What to send back

- Save each reply **unchanged** as a file, with the brief's number in the name if you can.
- Upload the files here.

Claude will check each reply against Avida's code before anything is run. The two small pilots now running (from Astra's earlier replies) are not assumed in any brief.
