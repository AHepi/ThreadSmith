# The falsifier ledger

Every use of the skill ends with a ledger. `scripts/check_ledger.py` checks it: `python3 scripts/check_ledger.py ledger.md`.

## The parts, in order

1. **Claims, frozen.** One line per claim, starting `C1.`, `C2.` and so on, quoted word for word.
2. **`Source:`** where the claims were quoted from (file, page, message, section).
3. **The falsifier table.**
4. **The forcing-question table.** In the short form, the `Short form:` line replaces it.
5. **`Claim as it stands:`** the narrowed claim, with any *held if*.
6. **`Next test:`** one test, the one that could overturn the most for the least work.

Optional lines:
- **`Well-tested:`** naming the claims whose main falsifiers were all sought and survived or were reported. It tells the reader, and the checker, that a clean ledger is meant.
- **`Routine checks:`** generic checks nothing in the case points to.

## The falsifier table

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C2 | In at least one of three scenes outside the supplied model list, the planner answers a confident yes that turns out wrong | missing | none | C2 held only while the world obeys a supplied model |
| F2 | C1 | A ranker using the same force totals with no learning also needs 9 or fewer checks on the 8 cases | blocked | the engineer can add it as a sixth arm; pass if it needs 11 or more | credit to "learned" unmeasured |
| F3 | C1 | The gain over fixed order (3 checks) rests on 2 or fewer of the 8 cases | survived | counted case by case from the report's table: 4 wins, 1 loss, 3 ties; sign test p = 0.375 | C1 reported as "on these 8 cases", not as general |
| F4 | C2 | Planner forecasts differ from a separate run of the checker on at least one candidate | reported | report, "Every attempted planner forecast exactly matched its independent enumeration"; not rerun by us | none, as reported |

The columns:
- **F:** the falsifier ID: F1, F2 and so on.
- **Claim:** the ID of the claim it tests. A row may name several, such as `C1, C2`, but every claim needs at least one row naming it alone.
- **Falsifier:** at least eight words, saying:
  - what is observed;
  - where;
  - how it is measured;
  - the result that counts against the claim, with a threshold where possible.

  Someone else should be able to run it from these words alone.
- **Status:** one of the words in the table below.
- **Receipt:** as that table says.
- **Effect on claim:** what the result, or its absence, does to the claim. `survived` and `reported` may say "none".

| Status | Meaning | Receipt must hold |
|---|---|---|
| `survived` | you ran it, or watched it run, and the claim survived | what was run and what it printed, or where the output is |
| `reported` | someone else (usually the claimant) says it was run and the claim survived; you did not see it | where they say so, with their own words quoted |
| `failed` | it was run and showed the claim wrong | what was run and what it printed |
| `missing` | nobody sought it | "none" |
| `blocked` | cannot be sought here | who could run it, and its pass mark |
| `pending` | running now | what is running |
| `planned` | design mode: to be run | the prediction and the pass mark |
| `outside the claim` | a real limit of scope: tests something the claim never asserted | "none"; the effect says which part of the scope it lies outside |

## The forcing-question table

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C2 | missing | F1 |
| Q2 | C1 | missing | F2: the totals are supplied physics |
| Q3 | C1 | missing | F2 |
| Q4 | C1 | covered | from the definitions: zero-numbers arm = least-effort arm; counted as one |
| Q5 | C1 | missing | F3: "improves" rests on case-level wins |
| Q5 | C2 | covered | F4; 40/40 selections supported, per case, as reported |
| ... | | | |
| Q13 | all | covered | all 8 cases counted; error pooled over 672 coordinates, half trivially right (noted) |

The columns:
- **Q:** every question, Q1 to Q13. A `does not apply` row may list several questions that share one reason, such as `Q2, Q4, Q8`; every other answer gets its own row.
- **Claims:** the claim IDs the answer covers, or `all` (an empty cell also means all). Across a question's rows, every claim must be covered.
- **Answer:**
  - `covered`: cite a `survived`, `reported` or `outside the claim` row, or quote the evidence;
  - `missing`: cite the F-number of a `missing`, `blocked`, `failed`, `pending` or `planned` row;
  - `does not apply`: in at least six words, name the failure you considered and why the question's stated exemption rules it out here.
- **Where or why:** short, citing F-numbers rather than repeating them. A fact from the source is quoted word for word. "Yes", "ok", "fine" and "n/a" alone are refused.

## The short form

For a private, reversible, cheap claim only (see Step 0). The question table is replaced by one line:

`Short form: all 13 questions asked; missing: Q9 (F1), Q11 (F2)`

Every F-number named must exist in the falsifier table. If nothing came out missing, write `missing: none`.

## The design form

In design mode, before anything runs:
- every falsifier is `planned`;
- its receipt column holds the prediction and the pass mark;
- `Next test:` names the first test of the plan.

## What the check refuses

The script stops with an error when:
- the claim lines, the `Source:` line, the falsifier table, or the question table (or short-form line) is missing;
- a question from Q1 to Q13 is absent, or does not cover every claim;
- an answer or status word is not one of those allowed;
- a falsifier is shorter than eight words;
- a receipt does not hold what its status requires (a `reported` receipt must quote the source);
- a `failed`, `missing`, `blocked` or `outside the claim` row says nothing about its effect;
- a `missing` answer cites no row, or cites a row that is not open;
- a `covered` answer cites only open rows;
- a `does not apply` reason is shorter than six words;
- a claim has no falsifier row;
- the `Claim as it stands:` or `Next test:` line is absent.

It warns, without stopping, when:
- a falsifier has no number, threshold or comparison in it;
- a `covered` answer cites no row, quotes nothing and shows no working of your own;
- a survived or failed receipt names no command, file, number or quoted output;
- a blocked row's receipt names no one in particular;
- a row is still `pending`;
- a claim has more than eight falsifiers, or no falsifier naming it alone;
- two rows have the same receipt;
- the `Claim as it stands:` line has more than three *held if*;
- the `Routine checks:` line contains numbers or paths (case-specific items belong in the ledger);
- every falsifier of a claim is survived, reported or outside the claim, with no `Well-tested:` line;
- the report's prose uses a strength word that the `Claim as it stands:` line does not carry;
- the prose says verified, confirmed, proven, guaranteed or "is fixed" while a falsifier is open.
