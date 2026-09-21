# Checker rigs - read me first

What this folder is: both rigs as they stand now, including the last two fixes (a told world stands alone; "cannot tell" for a plan the ledger knows nothing about).

- rig 1 - arguments: patched/run_check.py is the working driver. joined/run_joined.py runs the same driver with rig 2 laws and joined/bridge.pl added, so one ledger can hold arguments and pressing patterns together.
- rig 2 - causes: patched/check2.py with patched/laws.pl.
- frozen/ in each rig is untouched since it was frozen. Copies named "before_..." are kept so reports can be compared.
- Ledgers A to J are the paragraphs; K.. are the other model's audit cases; T.. are its literary texts.
- raw_log.txt holds every question put to the checker and its full answer.

## Traps
- Comparing reports without leaving out the GAUGE line; it carries timings that change run to run.
- Withdrawing one of two stated causes: the result is set aside and the what-if may wrongly hold.
- Named cases are one level deep.
- The joined script points at the folder these rigs were built in; change that one path to run it elsewhere.
