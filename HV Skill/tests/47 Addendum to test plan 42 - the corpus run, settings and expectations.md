# 47 Addendum to test plan 42 - the corpus run, settings and expectations

Written before any run, on 20 September 2026. Once the run starts, this file stays as it is.
Authority document: "Claude Fable Semantics - standalone theory" (file 10). Frozen.
Plan 42 stays as it is. File 43 said an addendum would go with it before the run; this is it. Where this file and plan 42 differ, this file is the one the run follows, and every difference is listed here.

## What is different from plan 42
- **The cases.** The twenty-five in file 43 (twenty contested theories, five controls) replace plan 42's ten. The Mondays paragraph is out.
- **The marks for the twenty.** NAMED (the reply names the weak point the critics name), PARTLY, MISSED. The five controls keep LEFT STANDING and FALSE ALARM. The extra mark on every reply stays: is its reason given as a change someone could make (Y), or as a story (N)?
- **The change that should leave the marks as they are.** Plan 42 renamed people, places and objects in three cases. A real theory cannot be renamed: string theory with the strings called something else is still string theory. So the change becomes **rewording**: the same claims in other words, nothing added and nothing dropped. Three cases, one of each kind plan 42 chose: case 10 (in the starting point), case 8 (the label) and control C4. Each goes once under each setup. Rewording is a larger change than renaming, and can move a mark for its own reasons; a moved mark is read with that in view.
- **Number of runs.** 25 cases x 4 setups x 3 repeats = 300, plus 3 reworded x 4 setups = 12. Total 312.
- **Cost.** Worked out from DeepSeek's price list as read on 20 September: 0.15 dollars per million pieces in, 0.003 when the same opening text is served again from its cache, 0.60 per million out, off-peak. The skill is about 18,000 pieces and is the same opening text in every setup 2 and setup 3 run, so most of it is served from the cache. Expected: under two dollars for all 312 runs. Not yet seen.

## Settings, decided before the run and the same for every run
- Model: `deepseek-flash` on DeepSeek's own service, which the price list names DeepSeek-V4.1-Flash.
- Thinking on. Effort `high`. Plan 42 said "the middle setting"; DeepSeek offers three, low, high and max, so high is the middle one. (Its service maps a request for "medium" to high as well.)
- One message, from the user, with no system message. Setup 0: the passage, then the plan's bare question. Setup 1: the passage, then the report shape. Setups 2 and 3: one framing line ("Below is a skill, as a set of files, and after it a case. Use the skill on the case."), then the eight skill files one after another, each under a line naming it, then the passage, then the report shape. The framing line is the same in setups 2 and 3.
- Setup 3's skill differs from setup 2's in exactly two places, made by program and checked by diff: the two sentences added to the poke test, and the one trap. Thirty-six words.
- Every run a fresh conversation. Nothing carried over. An upper limit of 16,000 pieces on any one reply, thinking included, so no single run can run away with the budget.
- The order of the 312 runs is shuffled once with a fixed seed and saved, so the run can be stopped and resumed without repeating or skipping anything. Related cases (1 and 2; 3 and 4) are separate runs; since every run is a fresh conversation, no reply is written with its partner in view whatever the order.
- The rig: `run.py` sends and saves; `hide.py` strips the setup labels, shuffles with an unrecorded seed and numbers the replies; the marker fills one sheet; `restore.py` puts the labels back and prints the table. Tested end to end on a stub reply with no network: 312 runs, 312 hidden, a full sheet, the table printed. What the stub cannot test: the service's real replies, and the marking.

## What I expect, written first
1. **Recall will carry the well-known cases.** Cases 1, 6, 7, 9, 10, 12, 14, 17 and 18 have criticisms that are famous (the landscape, the replication failures, the spreadsheet error, just-so stories, the failed plaque drugs). DeepSeek will reach NAMED in most runs under every setup, and mostly by remembering the record rather than by testing the passage. These cases show the reader knows the field; they cannot tell the setups apart.
2. **The setups can only be told apart where the criticism has to be built.** Case 5 (many worlds): setups 0 and 1 mostly pick a winner or call it a matter of philosophy; setups 2 and 3 say in most runs that no change separates them at this level. Case 19 (test-first): setups 0 and 1 mostly stop at "correlation is not cause" (PARTLY); setups 2 and 3 more often reach "the part doing the work is not the part named". Cases 2, 3 and 4 (patched cosmology and astrophysics): all setups reach at least PARTLY; setups 2 and 3 more often say what a limit is held by, and what result would count against it.
3. **The one line shows, if at all, on the label cases: 8, 16 and 20.** Setup 3 names a close change (same pupil, same lesson, only the channel changed; the same group counted under two definitions of "stable relationship"; the same module judged before and after it proved hard to change) in more runs than setup 2. If setup 2 already does this in most runs, the skill's existing trap about labels is enough and the line stays out.
4. **Controls.** C1 and C2: LEFT STANDING in every setup. C4: LEFT STANDING in every setup; a reply faulting it for lacking numbers is a FALSE ALARM and I expect at most one, from setup 0 or 1. C3 is the live risk: the skill's "hunt the answer in the starting points" could make setups 2 and 3 endorse the circle. I expect at least one FALSE ALARM on C3 from setups 2 or 3, and no more from them than from setups 0 and 1. C5: mixed under every setup; the setups will not be told apart on it.
5. **Reason given as a change.** Y in nearly every run of setups 1 to 3; under half in setup 0.
6. **Reworded cases.** The same marks as the cases they reword, under every setup.

## What would count as failure
All six from plan 42 stand (the skill is idle; the line is idle; the line costs something; the skill makes a prosecutor; the cases are too easy; the test is noise). One is added:
- **Recall does the work.** If every setup reaches NAMED on the well-known cases by citing the record, those cases carry no weight either way. The reading then rests on cases 5, 8, 16, 19 and 20 and the five controls. If those too cannot tell the setups apart, the test says nothing about the skill's words, and the next test needs cases whose criticism is not on the record.

## What this test cannot show
As plan 42, and one more: that the critics are right. NAMED means the reply found what the critics name, not that the theory is wrong.

## What is needed before the run
- A key for DeepSeek's service, set as `DEEPSEEK_API_KEY` where the rig runs. None travelled with the file set, and this computer holds none. Everything else is built.
- A few dollars on the account. Delete the key at DeepSeek once the run is done.

## Traps
- Showing DeepSeek this file, plan 42, file 43 or keys.json. All hold the answer key.
- Editing this file, or any key, after seeing a reply.
- Reading NAMED on a famous case as the skill's doing. See expectation 1.
- Reading a moved mark on a reworded case as noise before asking whether the rewording changed the claim.
- Running the rig from a folder that still holds stub replies. `replies/` and `marking/` must be empty at the start.
