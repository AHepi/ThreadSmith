#!/usr/bin/env python3
"""frame_edits.py - bring the frame of the change list up to draft 4 (header, counts, what the checks changed,
the build, findings carried forward), on the list with the six draft-4 blocks spliced in (cl_final.md).

It first runs tools/s89_apply_changes.py on cl_final.md (output to the rivals folder, never authority/) to read
the build numbers the frame quotes, then writes cl_draft4.md. Every replacement asserts a single occurrence.
"""
import hashlib
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
RIV = HERE.parent
REPO = pathlib.Path('/home/user/ThreadSmith')
TOOL = REPO / 'Semantics/tools/s89_apply_changes.py'
FULL = RIV / 'file13_draft4.md'
THEORY = RIV / 'file13_draft4_theory.md'
DATE = 'draft of 25 September 2026, not frozen'
D3 = REPO / 'Semantics/tests/Revision 2 - file 13 draft 3, theory text.md'

run = subprocess.run([sys.executable, str(TOOL), str(FULL), '--change-list', str(HERE / 'cl_final.md'),
                      '--theory-output', str(THEORY), '--date', DATE, '--self-test'],
                     capture_output=True, text=True, cwd=str(REPO))
print(run.stdout)
if run.returncode != 0:
    sys.exit('the program refused')
out = run.stdout
full_md5 = re.search(r'^md5: ([0-9a-f]{32})$', out, re.M).group(1)
words_full, words_theory = map(int, re.search(r'^words: (\d+) \(theory text alone: (\d+)\)$', out, re.M).groups())
hunks = int(re.search(r'(\d+) diff hunks', out).group(1))
theory_md5 = hashlib.md5(THEORY.read_bytes()).hexdigest()
wc_theory = len(THEORY.read_text(encoding='utf-8').split())
wc_full = len(FULL.read_text(encoding='utf-8').split())
def shell_wc(path):
    # `wc -w` as the shell runs it (its locale), which is how draft 3's counts were taken
    return int(subprocess.run(['wc', '-w', str(path)], capture_output=True, text=True, env={'PATH': '/usr/bin:/bin', 'LC_ALL': 'POSIX'}).stdout.split()[0])
wc_theory = shell_wc(THEORY)
wc_full = shell_wc(FULL)
d3_md5 = hashlib.md5(D3.read_bytes()).hexdigest()
nums = dict(full_md5=full_md5, words_full=words_full, words_theory=words_theory, hunks=hunks, theory_md5=theory_md5,
            wc_theory=wc_theory, wc_full=wc_full)
print(nums)

cl = (HERE / 'cl_final.md').read_text(encoding='utf-8')


def one(text, old, new, what):
    n = text.count(old)
    if n != 1:
        sys.exit('frame replacement %s: old text occurs %d times' % (what, n))
    return text.replace(old, new)


# header
old_head = [l for l in cl.split('\n') if l.startswith('**DRAFT 3 — after the S90 cross-examination')][0]
cl = one(cl, old_head,
         "**DRAFT 4 — hard to vary restated through rivals and problems; correction-sticks result added; not frozen**\n\n"
         "Made from file 11, md5 5e494c1095d920d128b9a79de378f923. Draft 3 (24 September) applied every S90 ruling: 10 "
         "entries fixed, 14 kept, none dropped. Draft 4 (25 September) adds two entries and edits four on the owner's "
         "position of 24–25 September on hard-to-vary, rivals and problems, and on correction without a record. No "
         "outside reader has seen the texts and declarations the S90 fixes or the draft-4 entries wrote.", 'header')
cl = one(cl, "It opened no S90 reply, receipt, reasoning file or attempt file, wrote no ruling, and wrote nothing into "
             "`authority/`.*",
         "It opened no S90 reply, receipt, reasoning file or attempt file, wrote no ruling, and wrote nothing into "
         "`authority/`. On 25 September 2026 another Claude subagent made draft 4 on the owner's position of 24–25 "
         "September: it drafted W59.1 and W60.1, edited W34.1, W33.1, W36.1 and W38.1, had the drafts tested on finite "
         "models and attacked from the text and with counterexamples, applied every fix, and brought this frame up to "
         "date. The drafts, the models and the attacks are summed up in `tests/Revision 2 - hard to vary restated through "
         "rivals and problems, 25 September.md`, and the scripts are in `tests/Revision 2 - rivals and problems - "
         "scripts/`. It wrote nothing into `authority/`.*", 'italic')
cl = one(cl, "The list is withheld from every test brief (D6), as are the note, the sources note and the record it puts "
             "into file 13.",
         "Draft 4 restates hard-to-vary through rivals and problems and adds the correction-sticks result, on the owner's "
         "position of 24–25 September (\"After the owner's position of 24–25 September (draft 4)\", below). The six "
         "entries it adds or edits form one unit, group H, for plan 1.5's cap.\n\n"
         "The list is withheld from every test brief (D6), as are the note, the sources note and the record it puts "
         "into file 13.", 'what this is')
# counts
cl = one(cl, "- **Entries that change the theory text: 55.** Expected ruling CLAIM 49, WORDING 4, ORDER 2. By group: A 14 "
             "of 18, B1 14 of 15, B2 11 of 11, C 10 of 11. The note reads \"49 of the 55 changes\". Before the S90 rulings",
         "- **Entries that change the theory text: 57.** Expected ruling CLAIM 51, WORDING 4, ORDER 2. By group: A 14 "
         "of 18, B1 14 of 15, B2 11 of 11, C 10 of 11, H 2 of 2. The note reads \"51 of the 57 changes\". In draft 3 it "
         "read \"49 of the 55 changes\"; W59.1 and W60.1 (group H) each add one line. W34.1, W33.1 and W36.1 stay in "
         "group C, edited. Before the S90 rulings", 'counts')
cl = one(cl, "Every S90 ruling is applied below; see \"What the checks changed\".\n",
         "Every S90 ruling is applied below; see \"What the checks changed\". **Draft 4 (25 September):** two entries "
         "added (W59.1, W60.1) and four edited (W34.1, W33.1, W36.1, W38.1), each checked by its drafter, tested on "
         "finite models, and attacked twice, from the text and with counterexamples; every fix of both attacks is "
         "applied, and what the attacks refuted is dropped. None has been cross-examined.\n", 'checks')
# what the checks changed: new subsection before "## Checked, with no change entry"
sub = """**After the owner's position of 24–25 September (draft 4): 2 entries added, 4 edited.** The owner's position, agreed in conversation on 24–25 September: hard-to-vary is not a count over a listed set of versions; a variation is a competitor; two discovered rival explanations that both fit constitute a problem; rivals must differ in what they claim, not only in wording; "fit" means fit the whole question, which splits problems into those a test the question admits can solve and those it cannot, the mark of an easily varied explanation; the criticism is the producing of the rival; and a correction sticks without any record. The entries were drafted, tested on six finite models, attacked from the text and with counterexamples, and fixed. The drafted rival test ("not one account on \\(C\\) in the sense of Derivation 2") was refuted both ways and is replaced by conflict at some admitted pair. The record of the pass is `tests/Revision 2 - hard to vary restated through rivals and problems, 25 September.md`.

| entry | line | R2 | what changed | after the attacks |
|---|---|---|---|---|
| W34.1 | 315 | R2-23 | OLD widened to the label and the Pres lemma; NEW is the label "Commitments that do no work."; the definition of reach goes | GAIN, one REASON sentence and the N4 row corrected |
| W33.1 | 315 | R2-24 | the sentence on reach, containment and jobs, and the sentence on Pres, go; the three sentences on commitments that do no work stay | the definition is scoped to "a commitment \\(d\\) of a candidate that has a support"; O2's "This derives L275 s2's rule." struck |
| W59.1 | 317–319 | R2-25 | new: "Rivals" and "Problems" at the end of Part VI | the rival test replaced by conflict at some admitted pair; the physics' quantifier; "has been offered"; the narrowing sentence; "for an assessor"; kind (i)'s "at most one of them is an account"; relations tested where the answers agree; the finer contract scoped; the "asked" clause corrected; the obligation marked as declared |
| W60.1 | 365 | R2-29 | new: "A failed answer stays failed" after "Historical index" | the assessor named; "from the candidate's own answer there"; under (K3) the establishing lapses, not the fact (K2); "or a changed query" |
| W36.1 | 71 | R2-06 | companion edit: "whether an account is easy to vary is a separate matter (Part VI)" | required by the text attack |
| W38.1 | 7–9 | meta | *Explanation*, *Idle parts* and *Reach* rewritten, *Hard to vary* added, *Surprise and problems* narrowed; the fallback table recut to the group-H unit | four departures recorded; three wording points against the pages corrected |

**Group H is one unit.** W34.1 and W33.1 as edited, W59.1, W60.1 and the W36.1 companion edit stand or fall together under plan 1.5's cap. If the unit is dropped, W34.1, W33.1 and W36.1 revert to their text in draft 3 and W38.1's lines to their fallbacks.

**The build (draft 4).** `tools/s89_apply_changes.py --self-test` applies this list with no refusal: 65 entries parsed, 60 applied (57 theory, 3 meta), 5 record-only, none held; CLAIM 51, WORDING 4, ORDER 2; N = 51 of M = 57, K = 42; @@HUNKS@@ diff hunks, each inside an entry; both planted edits refused. The theory text of draft 4 is committed as `tests/Revision 2 - file 13 draft 4, theory text.md` (md5 @@TMD5@@, @@TWR@@ words by the runner's count and @@TWC@@ by `wc -w`). The full draft 4, with its meta blocks and the date text "draft of 25 September 2026, not frozen", has md5 @@FMD5@@ and @@FWR@@ words by the runner's count (@@FWC@@ by `wc -w`). Against draft 3's theory text (md5 @@D3MD5@@) it differs in exactly three places, each inside a draft-4 entry: line 69 (W36.1), line 313, which becomes five lines (W34.1, W33.1 and W59.1), and two lines added after line 363 (W60.1). Nothing was written into `authority/`.

"""
fill = {'@@HUNKS@@': str(hunks), '@@TMD5@@': theory_md5, '@@TWR@@': '{:,}'.format(words_theory),
        '@@TWC@@': '{:,}'.format(wc_theory), '@@FMD5@@': full_md5, '@@FWR@@': '{:,}'.format(words_full),
        '@@FWC@@': '{:,}'.format(wc_full), '@@D3MD5@@': d3_md5}
for k, v in fill.items():
    sub = sub.replace(k, v)
cl = one(cl, "\n## Checked, with no change entry\n", "\n" + sub + "## Checked, with no change entry\n", 'subsection')
# findings carried forward
cl = one(cl, "Before the freeze the plan should move these rows into P2(b)'s aimed set, or record that a change toward on "
             "them traces to these entries.",
         "Before the freeze the plan should move these rows into P2(b)'s aimed set, or record that a change toward on "
         "them traces to these entries. After draft 4, O54 (N2) and O57 (N5) move toward on the reason under W59.1, N4's "
         "watch moves from W34.1 to W59.1's sentence on questions (\"not by when anyone first asks the question\"), and "
         "under W59.1 the sun god of N1 is no rival of Tomas's account on any reading.", 'P2d')
anchor = "\n## Carried forward after S90\n"
new_find = """- **Found in draft 4 (25 September).** None is an entry.
  - *The dependence order does not place the new terms.* Rivals, conflict, established, fits and problem for \\(p\\) are defined from (F1), (F2), (A), (E), histories ("offered") and receipts, with no new primitive or declared input, so Derivation 6 still holds; the order at L518 does not list them, as it already omits Result, ProducesVia, Cap and Enable (finding 9 above). The file-11 sentence "(S), (B), (D) depend on (E)." is still free, and could read "(S), (B), (D) depend on (E); rivals and the problems they pose (Part VI) on (F1), (F2), (A), (E), histories and receipts."
  - *The relations the adopted physics admits at a pair.* W59.1's conflict quantifies over them, as Derivation 3's proof quantifies over "another admitted relation". Part I fixes them by the adopted physics; Part XIV does not list them.
  - *Port translations and values.* Part IV's port translation does not say whether it may carry a map of values. If it may not, a recoding of \\(E\\) alone is not an account, and Derivation 8 covers only the recoding of everything together (model attack, A3 (c)).
  - *Failures derivable from the candidate alone.* Whether a derivation from the candidate alone (non-circular dependence, or a component anchored to nothing) is an established result, so that the candidate no longer fits, is not said. A myth tied to nothing is a rival of the tilt on the Greek question, since their answers differ in the far south, and poses a problem with it or not according to this.
  - *The family \\(\\mathcal V\\) of (D)* is still not among Part XIV's declared inputs (W34.1).
  - *W35.3's REASON* ("The word 'problem' is not defined in the theory") is dated: "problem for \\(p\\)" is now defined; the bare word is not.
"""
cl = one(cl, anchor, "\n" + new_find + anchor, 'findings')
cl = one(cl, "- **W33.1's CASES AT RISK** still ends its O2 item with \"this derives L275 s2's rule\", which check 2 struck, and "
             "does not name O19, which check 2 added as watched (the R24 ruling). The theory text is unaffected.",
         "- **W33.1's CASES AT RISK** still ends its O2 item with \"this derives L275 s2's rule\", which check 2 struck, and "
         "does not name O19, which check 2 added as watched (the R24 ruling). The theory text is unaffected. **Draft 4:** "
         "the O2 sentence is struck; O19 is still not named.", 'options')
cl = one(cl, "\n| entry | line | R2 | calls and points | ruling | what the fix changed |\n",
         "\nThe column R2 gives each entry's number in draft 3, which the S90 parts use as R01–R55. Draft 4 renumbers from "
         "R2-25 on (\"After the owner's position of 24–25 September (draft 4)\", below; the revision note, section 5).\n"
         "\n| entry | line | R2 | calls and points | ruling | what the fix changed |\n", 'S90 table note')
cl = one(cl, "Read S90's replies through the entry ids.",
         "Read S90's replies through the entry ids. Draft 4 adds two entries, W59.1 (R2-25) and W60.1 (R2-29), and shifts "
         "the numbers after each; the note's map gives both.", 'S90 ids')
(HERE / 'cl_draft4.md').write_text(cl, encoding='utf-8')
print('written', HERE / 'cl_draft4.md')
