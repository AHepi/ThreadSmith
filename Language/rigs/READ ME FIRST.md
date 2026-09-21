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

## Inside the rigs - the names
- `rig 1 - arguments/`, `rig 2 - causes/`: the two checker set-ups. `frozen/` is untouched since the freeze, with `fingerprints.txt` (SHA-256 of the frozen files and the time). `patched/` is the working copy. `joined/` runs rig 1's driver with rig 2's laws and `bridge.pl` added.
- `run_check.py` (rig 1) and `check2.py` (rig 2) are the drivers; `checker_rules.pl` and `laws.pl` the fixed rules s(CASP) uses.
- `..._before_pile2.py`, `..._before_F.txt` and the like: a copy of a file as it stood before a named change, kept so reports can be compared.
- **Ledgers** come in pairs: `ledger_X.json` is the ledger as data (paragraph, sentences, lines with their marks, the bin, what-ifs); `ledger_X.pl` is the same ledger as s(CASP) facts, one `line(N).` per line so a line can be taken out.
- **Ledger letters.** Each ledger's `"paragraph"` field names its text, and rig 2's `"whose"` field says whose it was. The letters are per rig and do not line up across the two.
  - Rig 1: `A` tomato, `A2` tomato with "always" softened to "usually", `B` buses, `C` henhouse, `D` lateness, `E` letter, `F` ball and coin (the owner's), `G` Markus (the owner's), `H` abolish Mondays (the owner's), `J` the owner's ball sentences with both rigs joined. `K..` the other model's audit cases, numbered after its findings (K04 is finding F04; `b` marks a second form; KX and K22b are hostile cases added after the clean sweep). `T..` its literary texts by family and text: T05B is family 5, base text; T05D its contrasting text.
  - Rig 2: `A` ball and coin (the owner's, second form), `B` rope and cart, `C1` to `C4` four one-sentence pushes and drops, `D` people and rules, `E` the ball bounced back faster, `F` the owner's paragraph with three what-ifs added by Claude, `G` Markus (the happening only), `K01` the audit's F01 box case, `X1` and `X2` cases Claude added after the plan, chosen to break the rig.
- `raw_log.txt`: every question put to the checker and its full answer, in order. Leave out the GAUGE line when comparing runs; it carries timings.
