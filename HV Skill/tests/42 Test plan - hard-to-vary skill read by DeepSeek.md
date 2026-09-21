# 42 Test plan - hard-to-vary skill read by DeepSeek

Written before any run. Once the run starts, this file stays as it is.
Authority document: "Claude Fable Semantics - standalone theory" (file 10). Frozen.
Reader under test: DeepSeek V4.1 Flash (released 10 September 2026; checked by web search). Not run yet.

## The question, frozen
When Claude uses the hard-to-vary skill, Claude helped write it and has read the theory behind it. So good results might come from Claude and not from the words of the skill. This test swaps the reader for one that has never seen any of it, and asks two things.

1. Do the words of the skill do any work in a reader other than Claude?
2. Does the one proposed line (pick a poke's two changes close together) do any work?

## How the pieces fit
Example first. Take one case: a café owner says her café failed for lack of "atmosphere". DeepSeek gets that case four times, each time with a little more help than the time before. Its four replies are marked against an answer key written here, in advance. If the reply with the skill is no better than the reply without it, the skill did no work on that case.

- **Case:** a short explanation someone gives. Ten of them, below.
- **Planted fault:** the weakness deliberately built into a case.
- **Control:** a case whose explanation is sound. It is there to catch a reader that criticises everything.
- **Answer key:** what a good reply must say about each case. Written below, before the run.
- **Setup:** what DeepSeek is given along with the case. Four setups, below.
- **Run:** one case sent once under one setup. Each is repeated three times, because the same question can get different replies.
- **Marker:** whoever compares replies with the answer key. Claude, with the setup labels hidden.

Each part hands on: cases and setups go to DeepSeek; its replies go to a program that hides the labels and shuffles them; the shuffled replies go to the marker; the marks go back to the program, which restores the labels and prints the table.

## The four setups
Each differs from the one before in one thing only. That is the proposed line applied to this test itself.

| Setup | What DeepSeek is given | What it adds to the one before |
| --- | --- | --- |
| 0 | The case, and: "Is this a good explanation? Say why, in under 250 words." | nothing; the starting point |
| 1 | The case, and the report shape below | the report shape |
| 2 | The whole skill as it stands, then the case and the report shape | the skill |
| 3 | The same, with the proposed line added to the poke test and to the traps | the one line |

**The report shape** (given word for word in setups 1, 2 and 3): "Reply in this shape, in everyday words, in under 250 words. (1) The parts of the explanation that are claimed to do the work. (2) For each part, one sentence: what holds it in place, or what could take its place just as well. (3) The weakest part, and one change to the situation that would show whether it does any work. (4) Your verdict, one of: RELY ON IT / RELY ON IT FOR A NARROWER QUESTION, and say which / SET IT ASIDE."

Setup 1 is there as the best rival. It hands DeepSeek a sensible way to answer without the skill, so the skill has to beat something fair.

**The proposed line** (setup 3 only), added to the poke test: "Pick the two changes as close together as you can, differing in one feature. Far-apart changes can be found for any label, so they test nothing." Added to the traps: "Accepting a poke whose two halves sit far apart."

**Settings, the same for every run:** the model named deepseek-flash on DeepSeek's own service; thinking effort at the middle setting; every run a fresh conversation with nothing carried over.

## The ten cases and their answer key
Written by Claude, except case 10, written by the owner. The skill's own worked examples (the seasons, the old web page) are kept out, because setups 2 and 3 would have seen the answers.

**Case 1 - the redesign. Planted fault: covers both outcomes.** Why did the shop's sales rise after the redesign? Lena: "The new design is bolder. Bold designs stir strong feelings, and strong feelings change what people do." *Key:* had sales fallen, the same three sentences would cover it. FOUND when the reply says so in any words.

**Case 2 - the guard dog. Planted fault: the answer sits in the starting point.** Why does Rex bark at strangers and stay quiet with the family? Oskar: "He is a loyal breed. Loyal breeds are protective of their own. Being protective of his own, he raises the alarm at anyone else." *Key:* "loyal" and "protective" restate the barking, and the barking is the only evidence for them. FOUND when the reply says the explanation is the behaviour under another name.

**Case 3 - the sales rule. Planted fault: quiet narrowing after each failure.** A sales manager's rule says that calling a customer within an hour of their enquiry wins the sale. It failed all through March; he says it holds outside the end of the tax year. It failed for the big accounts; he says it holds for small buyers. It failed in the northern region; he says it holds where his own team makes the calls. Inside those limits it has been right so far. *Key:* three limits after three failures, and nothing in his account says why the tax year, the size of the account or the region would matter. FOUND when the reply says the limits are fitted to the failures, or asks what part of the account holds each limit.

**Case 4 - the greenhouse dial. Planted fault: the instrument taken for the cause.** Why do the seedlings wilt? Petra: "They wilt because the humidity dial drops below forty. Whenever it reads low, wilting follows within the day. So I have asked for the dial to be reset to read ten points higher." *Key:* the dial reports the air; the dry air does the wilting. Reset the dial and the seedlings wilt as before. FOUND when the reply separates the dial from what it reads.

**Case 5 - the café. Planted fault: a label that passes a far-apart test.** Why did the Harbour Street café fail while the one on Mill Lane thrives? Marta: "Harbour Street had no atmosphere. Here is my test. Gut the Mill Lane café to bare concrete and strip lights and it would fail too. Repaint its door a different green and it would carry on as before." *Key:* both halves of her test are right, and any label at all would pass them: charm, soul, good management. Make a close change (same room, different music; same room, the old owner behind the counter) and "atmosphere" has nothing to say. FOUND when the reply says her test is too easy, or asks for a closer change, or shows that a different label passes the same test. PARTLY when it says only that "atmosphere" is vague.

**Case 6 - the two teams. Planted fault: the same, in other clothes.** Why does team A deliver on time and team B late? Anders, their director: "Team A has ownership. Here is my test. Replace all of team A with day-rate contractors and they would deliver late. Move their desks up one floor and nothing would change." *Key and marks:* as for case 5.

**Case 7 - the thorn. Control: coarse and sound.** Why did the bike tyre go flat? Noor: "There is a thorn through it. Pull the thorn and patch the hole and it holds air. Leave the thorn in and it is flat again by morning." She can say nothing about rubber or air pressure. *Key:* sound. The thorn is held in place by both changes. LEFT STANDING when the verdict is RELY ON IT. FALSE ALARM when the reply faults it for lacking finer detail.

**Case 8 - the passing loop. Control: sound, with a free choice inside it.** Why do trains on this line pass each other only at Alder? "The line is single track except at Alder, where there is a loop. Two trains cannot share a single track. So the timetable has them meet at Alder. The up train takes the left-hand side of the loop; that is just the custom here." *Key:* sound. Left or right is a free choice and is presented as one. LEFT STANDING when the verdict is RELY ON IT. FALSE ALARM when the custom is counted against the explanation.

**Case 9 - the glue. Control: an honest narrowing; the twin of case 3.** Emil's rule says his glue sets in ten minutes. It failed in the cold shed. He restated it for above fifteen degrees, and his account says why: the hardener reacts more slowly in the cold. The same account says the glue should set faster in the hot van, and it does. *Key:* sound. The limit is held by a part of the account, and that part does a second job. LEFT STANDING when the verdict is RELY ON IT or RELY ON IT FOR A NARROWER QUESTION with Emil's own limit. FALSE ALARM when the reply calls it a retreat.

**Case 10 - abolish Mondays. Written by the owner. Planted by the owner: a chain that slides.** The owner's paragraph, word for word, beginning "To understand why we must abolish Mondays" and ending "we save civilization." *Key, taken from log entry 22:* "command" is used in two senses (having the right to be obeyed; giving an order), "Monday" slides from the day to the order it gives, and the supposition undoes itself (Monday goes, Tuesday becomes Monday, so there is a Monday). FOUND when the reply names any one of these three.

**The change that should leave the marks as they are.** Cases 2, 5 and 7 are also sent once under each setup with the people, places and objects renamed (a different dog, a different street, a different puncture). The marks should stay the same.

**Number of runs:** 10 cases x 4 setups x 3 repeats = 120, plus 12 renamed = 132.

## How replies are marked
- A program strips the setup labels, shuffles the replies and numbers them. Claude marks each against the answer key: FOUND, PARTLY or MISSED for planted faults; LEFT STANDING or FALSE ALARM for controls. One more mark on every reply: is its reason given as a change someone could make, or as a story?
- The marks are saved. Only then does the program restore the labels and print one table: case by setup, three marks in each box.
- Replies from setup 0 have no fixed shape, so the marker can tell them apart. Setups 1, 2 and 3 share a shape and stay hidden.
- The table is read box by box. Marks are left as they are and are not added into a single score.

## What I expect, written first
1. Cases 2, 3, 4 and 10: every setup finds the planted fault in most runs. These faults are well known and DeepSeek is a strong reader. These cases show the reader is competent; they cannot tell the setups apart.
2. Case 1: setups 2 and 3 find it in more runs than setups 0 and 1.
3. Cases 5 and 6: setup 3 reaches FOUND in most runs; setup 2 in some; setups 0 and 1 mostly stop at PARTLY.
4. Controls: setups 2 and 3 give no more false alarms than setup 1. Case 8 draws at least one false alarm from setup 0 or 1 and none from setups 2 and 3, because the skill says some things are allowed to be loose.
5. Reasons given as a change: nearly always in setups 1 to 3; under half the time in setup 0.
6. Renamed cases: the same marks.

## What would count as failure
- **The skill is idle here.** Setup 2's marks match setup 1's in every box. Then, for a reader answering in one go, 10,000 words of skill add nothing to a 70-word report shape.
- **The line is idle.** Setup 3's marks match setup 2's on cases 5 and 6. The skill already has a trap about labels ("if no change could tell the label from a different one, it does no work") and that may be enough. Then the line stays out.
- **The line costs something.** Setup 3 gives more false alarms on the controls than setup 2.
- **The skill makes a prosecutor.** Setups 2 and 3 give false alarms on two or more controls in most runs.
- **The cases are too easy.** Every setup reaches FOUND on every planted fault. Then only the controls and cases 5 and 6 carry any weight.
- **The test is noise.** Renamed cases change their marks, or three repeats of one run disagree with each other more than the setups do. Then the table is reported as unreadable, and nothing is concluded from it.

## What this test cannot show
- That an explanation which passes is true.
- How the skill does in a conversation with a person. The "how to ask" part, which is most of its use, gets no test here.
- Anything about the skill's router. Pasting the whole skill in at once gives the reader every module, so the router has nothing to do.
- Any reader other than DeepSeek V4.1 Flash.
- That the marker is fair. The marker wrote the skill and nine of the cases.

## What is needed before the run
- The owner's current skill file ("30 Skill - hard-to-vary - modular, with router and map.skill"), uploaded. The copy on Claude's computer in this chat is an older one.
- A key for DeepSeek's service. Claude carries none. Checked from this computer without a key: DeepSeek's own service answers and asks for a key; a reseller lists the model at 0.15 dollars per million word-pieces in and 0.60 out.
- Cost, worked out and not yet seen: between one and two dollars for all 132 runs at DeepSeek's or the reseller's listed prices.

## Traps
- Showing DeepSeek this file. It contains the answer key.
- Editing the answer key after seeing replies.
- Reading "setup 2 did better" as "the skill is right". It shows only that the skill's words changed what this reader did.
- Pasting a key into the chat and leaving it live. Put a few dollars on the account, paste the key for the one run, then delete the key on DeepSeek's site.
- Forgetting what is sent. The skill's full text and all ten cases, the Mondays paragraph included, go to DeepSeek's computers.
- Using the old copy of the skill. The run waits for file 30.
