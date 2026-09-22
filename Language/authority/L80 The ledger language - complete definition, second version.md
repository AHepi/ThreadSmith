# The ledger language

**Second version.** This is the second version of "38 The ledger language - complete definition.md" (SHA-256 5f0f54c2f6af60e5), made under the frozen plan "L79 Test plan - Arm A, the ledgers in hand on the old rig and the new, third version". Six things are changed in the text below, and nothing else; this paragraph is the only other addition. One: a sentence in "What it is for" saying that rig 1 answers the commitment question and that the world question is rig 2's. Two: the told-world and named-case paragraphs extended to every finding the checker makes inside a world or a case, with the count of the findings there that would not stand if the actual ledger's general lines were available; this is the driver's change D2. *Gives up:* each case runs twice; false alarms inside worlds, which N is there to show. Three: a sentence in "What-ifs" on what a what-if answers. Four: the outcomes block among the report's promised contents; this is D5. *Gives up:* the one-line header. Five: F15's rule, in "How arguments are tested", restated as D8 states it. *Gives up:* a denial "in a different respect" is flagged; 38 has no respect field yet. Six: rule 3 for the translator restated as required. Changes one, three and six carry no D-number of their own; they write down the picks of decision L10, and the give-up line for each of them, and for this version as a whole, is the plan's: *Gives up:* one report section becomes two; the world half is not built this round. The first version stays as it was, and the checker it describes still runs.

## What it is for

The ledger language is a way of writing down what a piece of everyday prose commits its writer to. Once written down, a program that follows fixed rules can find where those commitments clash, where one is missing, and where one does no work. It then says so in plain words that point back at the writer's own sentences.

Three roles are involved, and they stay apart.

- The **translator** turns prose into ledger lines. It is the only step that guesses, and every guess it makes is marked.
- The **checker** reads the ledger and applies fixed rules. It never guesses, and it gives the same finding for the same ledger every time.
- The **read-back** turns findings into plain prose by fixed wording.

One ledger is asked two questions, and rig 1, the checker described here, answers the first of them: the commitment question, which is what the writer has committed to and whether those commitments hang together, while the world question, which is whether the stated cause could in fact produce the stated effect under the laws below, is rig 2's.

## What a line means

The language never says whether a line is true of the world. A line means the difference it makes: what stops following, or what starts to clash, when the line is taken out, or when what fills one of its slots is changed. Two lines that make no difference under any such change are, to this language, the same line.

So a clean report means only that the lines fit together. A ledger of false lines that fit together passes.

## The line

Example first:

    6 | CLAIMED | sally MOVES away from wall, as a result of happening p1 | said | sentence 2

Every line has five fixed parts.

| Part | Choices | What it is for |
| --- | --- | --- |
| Number | 1, 2, 3, or a short name such as p1 for a happening | So other lines can point at this one. A happening's name is its number; it has no second one |
| Standing | CLAIMED, GIVEN, SUPPOSED in case NAME, or TOLD in world NAME | CLAIMED is what the sentence asserts. GIVEN is what it takes for granted along the way. SUPPOSED belongs to a named what-if case. TOLD is what a story, a report, a note or a dream says, and belongs to a named world of its own. Supposed and told lines are kept out of the actual ledger |
| Content | one of the fourteen kinds below | What is being recorded |
| Source mark | said, filled in, usual case | said: the writer wrote it. filled in: the translator added it as a reading or a missing step. usual case: the translator added it as something everyone assumes |
| Sentence | the number of the sentence it came from | An added line points at the sentence that prompted it |

**NOT.** Put NOT on exactly what is denied, in square brackets. NOT [the jar broke]. The jar broke, NOT [because it was dropped]. Denying a cause leaves its effect standing. Leaving a thing unsaid is different from denying it.

**Mentioning.** A goal, or the thing a what-if asks about, is only mentioned. Naming it makes no claim that it came about.

## The fourteen kinds of content

| # | Kind | Shape of the line | What the checker does with it |
| --- | --- | --- | --- |
| 1 | Thing | NAME is a KIND; it answers a press as one of the six response classes; it may be a DOER | The response class is checked by the laws of pressing. The kind is checked wherever another line speaks about that kind |
| 2 | Fact | THING plus any plain description ("sat on the mat", "is in the study") | Checked for clashes and for what follows. The description is a free name; the checker only asks whether two facts are the same fact |
| 3 | Habit | THING usually DOES VERB THING on occasions of KIND | Checked as a USUALLY line over occasions, of the SHOWS kind. It is not an event |
| 4 | Happening | NAME: DOER VERB THING [DIRECTION] | Checked through the verb's shape. A verb missing from the shape book is reported "not checked" and counted |
| 5 | Result | THING MOVES direction, STAYS, TOUCHES thing, or BECOMES [description], as a result of happening NAME | MOVES and STAYS are checked by the laws. TOUCHES is checked through links and what-ifs. BECOMES is carried and not yet checked |
| 6 | Link | happening B NEEDS result line R of happening A | Checked. It must name A and which of A's results |
| 7 | General line | ALWAYS or USUALLY: when [content], then [content]; and it MAKES or SHOWS | Checked. MAKES: this produces that. SHOWS: this is how we can tell |
| 8 | Only-ways line | [content] NEEDS ONE OF: [content], [content], ... | Written out as a general line: when every listed way is denied, the content is denied |
| 9 | Exception | THING is an exception to USUALLY line N: either the line DID NOT APPLY to it, or it applied and THE OPPOSITE HAPPENED [because of line M] | Checked, both kinds. Aimed at an ALWAYS line, the first is reported and the second is a contradiction |
| 10 | Causal word | INFLUENCE MAKES, LETS, HELPS or STOPS THING [content]; or [content] happened DESPITE INFLUENCE | Checked against a stated tendency |
| 11 | Tendency | THING was, or was NOT, already heading for [content] | Checked together with kind 10 |
| 12 | Depends | [content] DEPENDS ON [content]; doing ACTION CHANGES [content] | Checked when a plan is tested |
| 13 | A claim about other lines | line E BECAUSE line C. line E SINCE line C. NOT [line E BECAUSE line C]. Do line A SO THAT [goal]. Event X is LIKE event Y. WHAT IF [a change]: THEN line T would, or would not, be so | Each is checked as described below. These lines point at other lines by number and never restate them |
| 14 | Event | EVENT NAME is happenings NAME, NAME, ... | Used to line up two events and say what they share |

## The short fixed lists

- **Response classes:** fixed (a wall); heavy and standing (a person); heavy and loose; light and loose (a ball, a coin); not a body (wind, cold, heat, and only when the text makes that clear); not stated (the text does not say).
- **Directions:** toward X, away from X, up, down, across.
- **Strength of a general line:** ALWAYS, USUALLY.
- **Kind of a general line:** MAKES, SHOWS.
- **Shapes of a verb:** press; release; hold; press then release. The shape book lists which shape each verb has: throw, toss and hurl are press then release; push, pull, lean on and hit are press; drop, let go of and open a fist on are release; hold and close a fist on are hold. Nothing more about a verb is ever defined. Its particular flavour stays a plain name.

## How strength works

The writer never states the strength of a press, and the translator never writes one. "So hard that" goes to the bin. The checker works strength out from the response classes, on three levels: small for a light loose thing, large for a heavy one, unbeatable for a fixed one. It compares levels and never measures. The one comparison that matters is "far smaller than".

## The laws the checker applies to happenings

- **You cannot press hard on something that gives way.** A press is never bigger than what the pressed thing resists.
- **Every press is pressed back,** equally, the other way.
- **Making.** A press can move a thing only if the press is not far smaller than what the thing resists.
- **Letting.** Releasing a hold can only produce what the thing was already heading for. Loose things head downward.
- **Direction.** A thing moves the way of the winning press or of its own tendency, never across it.
- **Staying.** Nothing changes unless some happening changes it.

When a stated movement breaks a law, the checker says which slot failed: strength, direction, a letting that produced something new, or a change from nothing. When a thing's response is not stated, or the influence is not a body, it says "cannot tell".

For people, groups and rules, only the causal words are tested. LETS, HELPS and STOPS fit only where the thing was already heading that way. MAKES fits only where it was not. Where the text gives no tendency, the checker says the word rests on something nobody stated.

## How arguments are tested

- **BECAUSE** claims that C produced E. It is tested only on lines that MAKE. The checker sets aside any line that simply states E, asks whether E is still produced, and then takes C out to see whether C did any work. It can answer: follows; follows only on assumptions nobody stated; the cause is idle; a jump, with candidate missing lines; or a circle, where the only support for C is E. Where cause and effect are a happening and its result, the laws above do the testing.
- **SINCE** claims that C is a reason to expect or believe E. It is tested on what follows by any route, and always reported with its unstated assumptions.
- **A chain** of such claims is followed step by step. The final conclusion is the one argued for last. A conclusion stands if any one step for it holds. A reason that does not connect is named as doing no work.
- **NOT [E BECAUSE C]** is fine unless the ledger's own lines make C produce E. That test of the denial itself does not change, and where the denial passes it the report still says so, in the words it used before. Where the writer's own BECAUSE line claims the same effect from the same cause, a further finding is printed beside that one: the writer claims and denies the same cause, however the test of the claim itself came out. A SINCE claim about the same pair does not count. The language has no way to deny a cause in one respect while claiming it in another, so a denial meant in another respect is reported too.
- **SO THAT** asks whether the action changes anything the goal depends on. Where the ledger says nothing about what the action changes, or about what the goal depends on, the answer is "cannot tell". Reaching the goal never shows, by itself, that the action brought it about.
- **Two USUALLY lines pulling opposite ways** are both kept, and nothing is settled between them.
- **A route through a USUALLY line** stays a "usually" all the way down.
- **Added lines** are tested by taking out every line the writer wrote. If the conclusion still follows, the added lines are doing the writer's work, and the report says so.
- **LIKE** lists what the two events share: the same kinds of doing between the same classes of thing, and the same kinds of finding. It is offered as a question.

## What-ifs

A what-if names one change and asks whether some line would then be so. What it answers is the commitment question and no other: taking the writer's own stated causes at their word, does that line still stand once the change is made?

- **WITHDRAW line N:** as if nobody had said it.
- **MAKE a fact NOT SO:** as if it did not happen.
- **Change what fills a slot:** for example, a light ball becomes a heavy one.

The checker makes the change, keeps everything that led up to it, and works out afresh what follows. A result that the ledger itself ties to the changed thing is set aside, so that it cannot answer the question merely by still being written there. If other lines still produce a fact that is to be made not so, the checker declines to run the what-if and names those lines.

**Told worlds.** What a story, a report, a note or a dream says is TOLD, in a named world. A told world is looked at alone. It does not inherit the actual ledger, and nothing in it is claimed about the actual one: the door can stand open in Nora's story while it stays shut in the room where she tells it. A contradiction inside one told world is still reported. Every check the checker makes of commitments is asked inside the world, on the world's own lines: contradiction, BECAUSE, SINCE, the chain, a plan, an exception, likeness, two USUALLY lines pulling opposite ways, an exemption, added lines, and a denied BECAUSE. What-ifs are not asked inside a world. Because the world is looked at alone, a finding inside it can rest on the absence of the actual ledger's general lines, so the checker asks again with those general lines added, counts the findings of the first asking that the second does not give, and prints that count under the world.

**Named cases.** Lines that are only supposed belong to a named case. Each case is looked at alone, on top of the actual ledger. A contradiction that was already in the actual ledger is reported once and is not blamed on the case. A contradiction that arises only inside a case is reported under that case, and the report says whether the supposition undoes itself or clashes with lines the writer claims outright. The same checks are asked inside a named case, on the case's own lines above the actual ledger and no other case's, and the same count is printed under the case. What-ifs are not asked inside a case.

## What the checker can say

Contradiction, with the smallest set of lines. Follows. Follows only on assumptions nobody stated. Idle cause. Jump, with candidate missing lines. Circle. No connection. The chain, step by step, and whether the final conclusion stands. A plan that cannot work. A plan that acts on a circle. Exception with no reason. Departure from the usual, no reason given. Exemption from an ALWAYS line. Two USUALLY lines pull opposite ways. You deny a cause that your own lines supply. Added lines alone give the conclusion. The strength slot fails. The direction slot fails. A letting produced something new. A change from nothing. It could not have stayed. The word does not fit the slots. Rests on a tendency nobody stated. Cannot tell. Not checked. A what-if holds, fails, or cannot be run as stated. Under a supposition: no new contradiction, or a new one. Inside a told world: no contradiction, or one. Cannot tell whether a plan can work. A proposed abstraction, as a question. Same facts, different point.

Every report also carries an outcomes block, which names every check in a fixed order and says of each that it was asked and nothing was found, or asked and so many found, or not asked because the ledger has no line of that kind, or not asked because there was nothing to ask, or that it ran out of time. The fourth of those five forms belongs to the checks that have no query of their own: the chain, two USUALLY lines, added lines and what-ifs. Each of those four says it was not asked because there was nothing to ask whenever its own input is empty, no SINCE claim, no USUALLY line, no conclusion line, no what-if entry, and says it was asked otherwise. The report also carries: a note wherever a finding leans on a line the writer did not write; the count of lines said, filled in and usual case; the verbs with no shape; and the bin.

## Rules for the translator

1. Every line carries all five fixed parts: one standing, one source mark, one sentence.
2. One name, one thing. Use plain lower-case words. When the text uses one word in two senses, split it into two names.
3. Every thing in a happening must have a thing line of its own. This is required, not a choice: a happening whose things have no lines of their own is an incomplete translation. If the text does not say how it answers a press, write "not stated". A class you guess is a filled-in line.
4. Standing follows what the sentence asserts and what it takes for granted. Grammar is the usual clue: the main clause is CLAIMED; "who", "which", "as", "while" and "-ing" descriptions are GIVEN. When a sentence plainly asserts two new things, both are CLAIMED.
5. Never write a strength for a press. From "she pushed so hard that the box moved", keep the push, the movement and the BECAUSE between them. Only "so hard" goes to the bin.
6. A line that depends on an earlier happening names that happening and which of its results it needs.
7. Every general line says MAKES or SHOWS. If the text does not settle it, the choice is a filled-in line.
8. Never fill in a tendency from the causal word itself. "Let" does not prove they wanted to. A tendency line needs its own words in the text, which may be a clause of the same sentence.
9. An added line, whatever its mark, may not be the claimed line in other words, may not take the place of the reason the writer actually gives, and may not let the opposite follow just as well.
10. Claims about lines point; they do not restate.
11. Choose BECAUSE or SINCE by what is meant. Words such as "so" and "therefore" are only a clue. If a sentence claims both, write both lines.
12. An exception attaches to a USUALLY line only, and says which of its two kinds it is.
13. When a thing's state changes in the text, put the stage in the fact: the door open in the morning, the door open in the evening.
14. What the text only supposes is SUPPOSED, in a named case. What a story, a report, a note or a dream says is TOLD, in a named world of its own. A quoted command or question goes to the bin, and nothing is claimed from it.
15. One line, one source mark. Where part was said and part is your choice, split the line if you can. If you cannot, mark the whole line filled in and say in it which part you added.
16. Nothing is dropped silently. Whatever cannot be written goes in the bin with the reason. So do the translator's own readings of slips, and every word that was split, with both senses.

## Outside the language

How much, how fast, how hard. Where things are; inside, outside and openings. When, beyond the order of a chain and the stage named in a fact. Who believes, knows or wants what. Whether someone acted on purpose. Some, most, few, and numbers. May, must, should, can, obliged, optional. Several causes acting together. Figures of speech, tone, irony. Questions and commands.

All of these go to the bin, and the report lists them as not checked.

## Traps

- **Reading a clean report as "the reasoning is right".** It means only that the lines fit together.
- **Trusting a finding without reading its note.** A finding that leans on an added line is about the translator's guess until the writer confirms that line.
- **Reading "cannot tell" or "not checked" as "fine".**
- **Taking a suggested missing line as advice.** It is a candidate. Some are nonsense, because the checker knows nothing about a thing beyond its lines.
- **Expecting it to catch a wrong amount.** It sees a wrong direction, a wrong winner, and a change from nothing. A ball that bounces back faster than it was thrown will pass.
- **Withdrawing one of two stated causes.** The result is set aside even though the second cause remains, so the what-if may hold when it should not.
- **Writing a told story as a what-if.** It then inherits the actual ledger and clashes with it.
- **A told world that leans on everyday background.** It is looked at alone, so general lines from the actual ledger are not available inside it.
- **A case inside a case.** Named cases sit on the actual ledger only, one level deep.
- **Letting the bin grow unnoticed.** A clean report on a text that mostly went to the bin covers almost nothing.
- **Names that end in an underscore and a number.** The checker's printout merges them. Use words.
