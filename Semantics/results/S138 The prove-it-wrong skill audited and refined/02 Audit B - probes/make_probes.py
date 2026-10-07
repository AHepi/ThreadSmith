"""Writes the probe ledgers for Audit B (S138). Each probe is a small change to one base ledger."""
import os, sys
out = sys.argv[1]

BASE = '''{note}
C1. "The new price cache makes checkout pages load faster: median 310 ms against 420 ms over one week."
C2. "The cache never serves a stale price."
Source: the team's release note, "Results" paragraph.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | Rerun of the same week's traffic replay shows a median gap of less than 50 ms between cache on and cache off | survived | ran replay_compare.py on the saved week; printed "median 312 ms on, 418 ms off" | none |
| F2 | C1 | With the cache on for half the servers and off for the other half in the same week, the median gap is under 50 ms | missing | none | C1 held if no other change in that week sped pages up |
| F3 | C2 | At least one stale price is found in the 9-day log of price reads checked against the price table | reported | release note: "no stale price was seen in 9 days of logs" | none, as reported |
| F4 | C2 | A price changed on purpose during a load test is served stale at least once in 1,000 reads | missing | none | C2 held only for the price changes that happened to occur |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | missing | F2: one week only, no peak season |
| Q1 | C2 | missing | F4: only the price changes that happened |
| Q2 | all | does not apply | considered a supplied answer in the replay; the replay holds raw traffic only, nothing handed in |
| Q3 | C1 | missing | F2: a release in the same week could explain the gain |
| Q3 | C2 | missing | F4: no planted change, so absence of stale reads may be luck |
| Q4 | C1 | covered | F1: worked out, the two arms differ in the cache switch only |
| Q4 | C2 | does not apply | considered two measures agreeing by construction; there is one measure and no arms |
| Q5 | C1 | covered | F1: counted per page type from replay output |
| Q5 | C2 | missing | F4 |
| Q6 | C1 | missing | F2 |
| Q6 | C2 | covered | F3: "9 days of logs" of the same build, as reported |
| Q7 | all | covered | worked out: both claims are about outputs, load time and served price |
| Q8 | all | does not apply | considered a fitted part meeting new traffic; nothing in the cache was fitted or learned |
| Q9 | C1 | covered | F1: replay of a full week, about 2 million page loads, counted |
| Q9 | C2 | missing | F4: 9 days may hold too few price changes to expect a stale read |
| Q10 | all | missing | F2, F4: the release note does not say whether the pass mark was fixed before the week |
| Q11 | C1 | covered | F1: we ran the replay ourselves |
| Q11 | C2 | covered | F3: reported, not rerun by us |
| Q12 | all | missing | F4: a stale price would be charged to customers |
| Q13 | all | covered | F1: every page load in the week counted, none excluded |

Claim as it stands: on one week of replayed traffic, the cache cut the median checkout load from 418 ms to 312 ms. No stale price was reported in 9 days; held if a planted price change is also served fresh.

Next test: change 20 prices on purpose during a load test and count stale reads (F4).
'''

def write(name, note, text):
    with open(os.path.join(out, name), "w", encoding="utf-8") as f:
        f.write(text.replace("{note}", "# " + note))

base = BASE
probes = []
def probe(name, note, text): probes.append((name, note, text))

# ---------- should pass ----------
probe("pass_01_base.md", "Probe pass 01: the base ledger, two claims, written by the format. Expected: passes.", base)
probe("pass_02_claim_range.md", "Probe pass 02: the Claims cell names a range, C1-C2, instead of all. Expected: passes.",
      base.replace("| Q2 | all |", "| Q2 | C1-C2 |").replace("| Q8 | all |", "| Q8 | C1–C2 |"))
probe("pass_03_well_tested.md", "Probe pass 03: a well-tested claim, no missing rows, with a Well-tested line. Expected: passes.",
'''{note}
C1. "The new date parser reads every timestamp in our 2023 to 2025 archive as the reference library does."
Source: release notes, "Parser" section, written by us.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | At least one timestamp in the archive is read differently by the new parser and the reference library | survived | ran compare_all.py over all 41,207,113 timestamps; printed "0 differences" | none |
| F2 | C1 | A colleague who did not write the parser reruns the comparison on another machine and finds at least one difference | survived | watched the rerun; output runs/compare_rerun.txt shows "0 differences" | none |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | C1 | covered | F1: the claim is scoped to the archive by its own words |
| Q2, Q4, Q8 | C1 | does not apply | considered a supplied or fitted answer; the reference library is independent, there is one comparison, nothing was fitted |
| Q3 | C1 | covered | F1: the reference library is the rival, run on every item |
| Q5 | C1 | covered | F1: every timestamp compared one by one |
| Q6 | C1 | covered | F1: same inputs and same build for both parsers |
| Q7 | C1 | covered | worked out: "as the reference library does" is a claim about outputs only |
| Q9 | C1 | covered | F1, F2: the whole population, and a second run by someone else |
| Q10 | C1 | covered | design note dated before the run: "compare every archive timestamp" |
| Q11 | C1 | covered | F2: rerun by someone else and watched |
| Q12 | C1 | covered | release benchmark: "speed within 2%" |
| Q13 | C1 | covered | F1: every timestamp counted, malformed lines included |

Well-tested: C1. Its main falsifiers were sought and survived.

Claim as it stands: unchanged; the parser reads every archive timestamp as the reference library does.

Next test: a sample from each new log source before the parser is used on it.
''')
probe("pass_04_merged_row.md", "Probe pass 04: one falsifier tests both claims, merged as Step 3 asks, and C2 has no row of its own. Expected: passes, with at most advice.",
      base.replace("| F3 | C2 |", "| F3 | C1, C2 |").replace("| F4 | C2 |", "| F4 | C1, C2 |"))
probe("pass_05_not_verified.md", "Probe pass 05: plain prose under the ledger says the price claim was not verified. Expected: passes with no warning about the word.",
      base + "\nNote for the reader: the stale-price claim was not verified by us, and the speed claim is not proven beyond this one week.\n")
probe("pass_06_quoted_original.md", "Probe pass 06: prose quotes the original strength word in order to report that it was dropped. Expected: passes with no warning.",
      base + "\nWhat changed: the release note's word \"never\" is dropped from the claim as it stands, because no planted price change was tried.\n")
probe("pass_07_short_form.md", "Probe pass 07: the short form, correctly written. Expected: passes.",
      base.split("| Q | Claims")[0] + "Short form: all 13 questions asked; missing: Q3 (F2), Q5 (F4)\n\nClaim as it stands: on one replayed week, a median of 312 ms against 418 ms.\n\nNext test: change 20 prices on purpose and count stale reads (F4).\n")
probe("pass_08_f1_score.md", "Probe pass 08: a covered answer quotes the model's F1 score, a common measure name. Expected: passes.",
      base.replace("| Q7 | all | covered | worked out: both claims are about outputs, load time and served price |",
                   "| Q7 | all | covered | worked out: outputs only; the note's quality check, \"F2 score 0.91 on stale detection\", is about outputs too |"))

# ---------- should fail ----------
probe("fail_01_reported_no_quote_possessive.md", "Probe fail 01: a reported row whose receipt quotes nothing, but holds a plural possessive. Expected: refused.",
      base.replace('release note: "no stale price was seen in 9 days of logs"', "the authors' own log summary, section 3"))
probe("fail_02_reported_unquoted_plain.md", "Probe fail 02: a reported row whose receipt quotes nothing, plain words. Expected: refused.",
      base.replace('release note: "no stale price was seen in 9 days of logs"', "the release note says so in section 3"))
probe("fail_03_covered_cites_missing_row.md", "Probe fail 03: a covered answer cites a missing row together with an unrelated survived row. Expected: refused.",
      base.replace("| Q5 | C2 | missing | F4 |", "| Q5 | C2 | covered | F4, F1 |"))
probe("fail_04_dna_five_words.md", "Probe fail 04: a does-not-apply reason of five words. Expected: refused.",
      base.replace("| Q8 | all | does not apply | considered a fitted part meeting new traffic; nothing in the cache was fitted or learned |",
                   "| Q8 | all | does not apply | nothing here was ever fitted |"))
probe("fail_05_dna_generic_six_words.md", "Probe fail 05: a does-not-apply reason of six generic words that name no failure and no exemption. Expected: refused.",
      base.replace("| Q8 | all | does not apply | considered a fitted part meeting new traffic; nothing in the cache was fitted or learned |",
                   "| Q8 | all | does not apply | this question does not apply here |"))
probe("fail_06_q5_dna_with_never.md", "Probe fail 06: Q5 answered does-not-apply for a claim with the strength word never, which Q5's exemption forbids. Expected: refused.",
      base.replace("| Q5 | C2 | missing | F4 |", "| Q5 | C2 | does not apply | considered a worst single case; the stale-price claim has no average in it |"))
probe("fail_07_duplicate_ids.md", "Probe fail 07: two rows share the ID F2, one missing and one survived. Expected: refused.",
      base.replace("| F3 | C2 |", "| F2 | C2 |").replace("F3", "F2"))
probe("fail_08_missing_cites_other_claims_row.md", "Probe fail 08: a missing answer for C1 cites only a row that tests C2. Expected: refused.",
      base.replace("| Q6 | C1 | missing | F2 |", "| Q6 | C1 | missing | F4 |"))
probe("fail_09_shortform_cites_survived.md", "Probe fail 09: the short form names a survived row as the missing condition. Expected: refused.",
      base.split("| Q | Claims")[0] + "Short form: all 13 questions asked; missing: Q3 (F1)\n\nClaim as it stands: on one replayed week, a median of 312 ms against 418 ms.\n\nNext test: change 20 prices on purpose and count stale reads (F4).\n")
probe("fail_10_empty_falsifier.md", "Probe fail 10: a falsifier that would fit any claim, of the kind Step 2 calls no falsifier. Expected: refused, or at least a warning.",
      base.replace("At least one stale price is found in the 9-day log of price reads checked against the price table",
                   "The claim would be shown wrong if the cache did not work in any setting at all"))
probe("fail_11_covered_yes.md", "Probe fail 11: a covered answer whose evidence is Yes. with a full stop. Expected: refused, as the format says.",
      base.replace("| Q13 | all | covered | F1: every page load in the week counted, none excluded |", "| Q13 | all | covered | Yes. |"))
probe("fail_12_survived_ran_it.md", "Probe fail 12: a survived row whose receipt is two words, with no output. Expected: refused.",
      base.replace('ran replay_compare.py on the saved week; printed "median 312 ms on, 418 ms off"', "ran it"))
probe("fail_13_shortform_none_with_open.md", "Probe fail 13: the short form says missing: none while two rows are missing. Expected: refused.",
      base.split("| Q | Claims")[0] + "Short form: all 13 questions asked; missing: none\n\nClaim as it stands: on one replayed week, a median of 312 ms against 418 ms.\n\nNext test: change 20 prices on purpose and count stale reads (F4).\n")
probe("fail_14_two_falsifier_tables.md", "Probe fail 14 (brittleness): the falsifier rows split into two tables, one per claim. Expected: either passes, or a clear message that one table is needed.",
      base.replace("| F3 | C2 |", "\n| F | Claim | Falsifier | Status | Receipt | Effect on claim |\n|---|---|---|---|---|---|\n| F3 | C2 |", 1))
probe("fail_15_id_header.md", "Probe fail 15 (brittleness): the falsifier table's first column is headed ID instead of F. Expected: a clear message about the column name.",
      base.replace("| F | Claim | Falsifier |", "| ID | Claim | Falsifier |"))

for name, note, text in probes:
    write(name, note, text)
print(len(probes), "probes written")

# ---------- second batch ----------
probes.clear()
dup = base.replace("| F4 | C2 |", "| F2 | C2 |").replace("F4", "F2")
probe("fail_07b_duplicate_ids_same_status.md", "Probe fail 07b: two different rows share the ID F2, both missing, one for each claim. Expected: refused.", dup)
for name, note, text in probes:
    write(name, note, text)
print(len(probes), "more probes written")

# ---------- third batch: a clean three-claim pair ----------
probes.clear()
T = '''{note}
C1. "Version 7 answers the support questions correctly 92% of the time on our 500-question set."
C2. "Version 7 is better than version 6 on that set."
C3. "Version 7 costs less per answer than version 6."
Source: the model team's weekly note, "Evaluation" section.

| F | Claim | Falsifier | Status | Receipt | Effect on claim |
|---|---|---|---|---|---|
| F1 | C1 | A grader who did not build version 7 marks at least 60 of the 500 answers wrong | missing | none | C1 held if the team's own marking is right |
| F2 | C2 | On the same 500 questions, version 6 wins at least as many questions as version 7, counted one by one | missing | none | C2 held if the gain is not luck |
| F3 | C3 | The billing log for one day shows a cost per answer for version 7 at or above version 6's | reported | weekly note: "cost per answer down 18%" | none, as reported |

| Q | Claims | Answer | Where or why |
|---|---|---|---|
| Q1 | {R} | missing | F1, F2: one question set, one week |
| Q2 | {R} | does not apply | considered answers handed in with the questions; the note says the set has "no reference answers shown to the model" |
| Q3 | {R} | missing | F2: version 6 run under the same conditions is not reported |
| Q4 | {R} | does not apply | considered two measures agreeing by construction; correctness and cost are measured apart |
| Q5 | {R} | missing | F1: 92% hides the worst topic |
| Q6 | {R} | missing | F2: same set, but versions may differ in prompt as well |
| Q7 | {R} | missing | F1: correct by the team's marking, not by the customer |
| Q8 | {R} | missing | F1: version 7 was tuned on questions like these |
| Q9 | {R} | missing | F2: 500 questions, one run each |
| Q10 | {R} | missing | F1: the note does not say when the pass mark was set |
| Q11 | {R} | missing | F1: marking done by the team that built version 7 |
| Q12 | {R} | covered | F3: "cost per answer down 18%", as reported |
| Q13 | {R} | missing | F1: the note does not say whether questions were dropped |

Claim as it stands: on one set of 500 questions marked by the builders, version 7 scored 92%; held if an outside grader agrees.

Next test: an outside grader marks a random 100 of the 500 answers (F1).
'''
probe("pass_02c_three_claims_all.md", "Probe pass 02c (control): three claims, every question row covers all. Expected: passes.", T.replace("{R}", "all"))
probe("pass_02d_three_claims_range.md", "Probe pass 02d: the same ledger, every question row names the range C1-C3 instead of all. Expected: passes.", T.replace("{R}", "C1-C3"))
probe("pass_02e_three_claims_range_dash.md", "Probe pass 02e: the same ledger with the range written C1 to C3. Expected: passes.", T.replace("{R}", "C1 to C3"))
for name, note, text in probes:
    write(name, note, text)
print(len(probes), "more probes written")

# ---------- pass_09: plain question names beside the numbers (made from pass_01) ----------
import re
names = {1: "Scope", 2: "Supplied answer", 3: "Rivals", 4: "Same by construction", 5: "Worst single case",
         6: "Premise match", 7: "Same question", 8: "Unseen changes", 9: "Draws and size", 10: "Order of events",
         11: "Receipts", 12: "Consequences", 13: "What is counted"}
text = BASE.replace("{note}", "# Probe pass 09: the base ledger with each question's plain name written beside its number, as the owner prefers full plain-word names. Expected: passes.")
text = re.sub(r"^\| Q(\d+) \|", lambda m: f"| Q{m.group(1)} {names[int(m.group(1))]} |", text, flags=re.M)
with open(os.path.join(out, "pass_09_question_names.md"), "w", encoding="utf-8") as f:
    f.write(text)
