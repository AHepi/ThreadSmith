# Audit B probes: what this folder holds

*Plain note: this folder holds the small test ledgers (probes) that Audit B wrote to see what the owner's ledger checker (`scripts/check_ledger.py` of the prove-it-wrong skill, version 5) accepts and refuses, with the checker's own output. Nothing here is the owner's material; the checker was run from a copy in the session's scratch folder, never from the owner's folder. Log entry S138.*

## Files

| File | What it is |
|---|---|
| `make_probes.py` | the script that wrote every `pass_*` and `fail_*` probe from one base ledger (two claims about a price cache), plus one three-claim ledger; `pass_09` was made from `pass_01` by writing each question's plain name beside its number |
| `worked_example_1_planner.md`, `_2_flaky_test.md`, `_3_well_tested.md` | the three ledgers of `references/worked-examples.md`, copied out one per file, unchanged |
| `pass_*.md` | ledgers that follow the skill's rules and should pass |
| `fail_*.md` | ledgers that break a rule the skill states and should be refused (two, `fail_14` and `fail_15`, test how the checker reacts to a layout slip) |
| `checker_output.txt` | the checker's self-test and its output on every file above, with exit codes |
| `run_suite_dry_run.txt` | a dry run of `evals/run_suite.sh` with a stand-in for `claude` that makes no model call |

The first line of each probe says what it tests and what result is expected.

## Results in one table

| Probe | Expected | Checker said | Verdict |
|---|---|---|---|
| worked examples 1, 2, 3 | pass | PASSED, 0 warnings each | right |
| pass_01 base ledger | pass | PASSED, 0 warnings | right |
| pass_02 range C1-C2 (two claims) | pass | PASSED | right |
| pass_02c three claims, `all` (control) | pass | PASSED, 1 warning: add a `Well-tested: C3` line, though C3's only row is *reported* | false warning |
| pass_02d three claims, range `C1-C3` | pass | FAILED, 13 errors "no answer for C2" | false alarm |
| pass_02e three claims, `C1 to C3` | pass | FAILED, 13 errors "no answer for C2" | false alarm |
| pass_03 well-tested claim, no missing rows, `Well-tested:` line | pass | PASSED, 0 warnings | right |
| pass_04 one row tests both claims (merged, as Step 3 asks) | pass | PASSED, 1 warning "C2 has no falsifier naming it alone" | false warning (the one agents chased) |
| pass_05 prose: "was not verified", "is not proven" | pass, no warning | PASSED, 3 warnings ("verified", "proven" while rows open; "proven" not in the claim as it stands) | false warnings |
| pass_06 prose quotes the dropped word "never" | pass, no warning | PASSED, 1 warning | false warning |
| pass_07 short form | pass | PASSED | right |
| pass_08 covered answer quotes "F2 score 0.91" | pass | FAILED: reads "F2" as falsifier row F2 | false alarm |
| pass_09 question cells "Q5 Worst single case" | pass | FAILED, 33 errors | false alarm |
| fail_01 reported receipt with no quote, only "the authors' own log summary" | refuse | PASSED | miss (the plural apostrophe counts as a quotation mark) |
| fail_02 reported receipt with no quote, plain | refuse | FAILED "quotes nothing" | caught |
| fail_03 covered answer cites a missing row plus another claim's survived row | refuse | PASSED | miss |
| fail_04 does-not-apply reason of five words | refuse | FAILED "at least six words" | caught |
| fail_05 does-not-apply reason "this question does not apply here" | refuse | PASSED | miss |
| fail_06 Q5 does-not-apply for a claim saying "never" (Q5's exemption says "Never when any of these is present") | refuse | PASSED | miss |
| fail_07 duplicate ID F2, one missing and one reported | refuse | FAILED, but with three messages about Q1, Q3, Q6 citing rows "not open", none naming the duplicate | caught by accident |
| fail_07b duplicate ID F2, both missing | refuse | PASSED, with a warning that every falsifier of C1 survived | miss |
| fail_08 missing answer for C1 cites only a row testing C2 | refuse | PASSED | miss |
| fail_09 short form names a survived row as missing | refuse | PASSED | miss |
| fail_10 falsifier "would be shown wrong if the cache did not work in any setting at all" | refuse or warn | PASSED, no warning | miss |
| fail_11 covered answer "Yes." | refuse (ledger-format: "Yes" ... "alone are refused") | PASSED with 1 warning | miss (warning only) |
| fail_12 survived receipt "ran it" | refuse or warn | PASSED, no warning | miss |
| fail_13 short form "missing: none" with two missing rows | refuse | PASSED | miss |
| fail_14 falsifier rows split into two tables | pass, or one clear message | FAILED, 10 errors, all about rows "not in the falsifier table" | brittle, misleading |
| fail_15 first column headed "ID" instead of "F" | one clear message | FAILED, 23 errors; the first says each falsifier's text "should look like F1" | brittle, misleading |

**Counts.** Of 15 ledgers that should pass, 7 passed cleanly, 4 were refused (false alarms) and 4 passed with 6 false warnings. Of 14 ledgers that should be refused, 2 were refused for the right reason, 1 was refused for a wrong reason, 1 drew only a warning, and 10 passed silently: 11 misses. The two layout slips drew 10 and 23 error lines that do not name the slip.
