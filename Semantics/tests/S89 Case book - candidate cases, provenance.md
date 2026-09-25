# S89 Case book - candidate cases, provenance

*Written on 23 September 2026 from the working files of the candidate cases, which Claude subagents made that day, and moved into the repository from the session scratchpad the same day. The companion of `tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md`. Like the S81 provenance file, this file is Claude's record and travels in no brief: from round 2 on, case authors saw only situations and questions, and a tested agent would see only an adopted case book. It holds what a case author must not see: the book, chapter and page each case was drawn from, the observation of the source audit each was chosen to test, and what changed between rounds. Parts 1 to 3 are the working files `sketches.md`, `sketches - why each was chosen.md` and `round2 - what changed.md`, as written, with their headings moved down one level and their pointers changed to the committed copies. The authors' returns are in the folder `tests/S89 Case book - candidate cases, author rounds/`.*

## How the cases were made

- **The sketches.** A Claude subagent that had read the theory and the two books chose twenty-five sketches, N1 to N25, from the observations of the source audit (`results/S89 The theory against its sources - Deutsch and Marletto.md`). Twenty are drawn from the books and five were made for the set (N5, N7, N10, N11, N18). Each gives a situation and a question, with a source line naming the book, chapter and printed page (Part 1). Why each was chosen is Part 2.
- **Round 1.** Two Claude subagents that never read the theory (`author1.md`, `author2.md`) each judged all twenty-five sketches as a careful person would in ordinary reasoning. They could read the cited book passages, but only to check each sketch against its source. A third Claude subagent, which read neither the theory nor the books, reconciled the two (`cases - reconciled.md`): 18 AGREED, 6 DISPUTED (N4, N9, N17, N18, N21, N22) and 1 UNUSABLE (N14), where both authors flagged the sketch as leading.
- **Round 2.** Book passages withheld. Fourteen prompts (`round2 - prompts.md`) carried only titles, situations and questions: no sources, no author names and no earlier verdicts. They were the seven disputed or unusable cases, rewritten, and seven book-derived AGREED cases, to see whether their verdicts held without the book. Two new theory-blind Claude subagents judged them (`round2 - author1.md`, `round2 - author2.md`). The seven re-judged verdicts (N3, N13, N16, N20, N23, N24, N25) all held. Of the seven rewritten cases, six were agreed (N4, N9, N17, N18, N21, N22) and N14 stayed disputed, so it was set aside. What changed from round 1 is Part 3.
- **Round 3.** Book passages withheld. Two more new theory-blind Claude subagents judged the other seven book-derived cases (N1, N2, N6, N8, N12, N15, N19) from their situations and questions alone, printed by a script from the case book (`round3 - author1.md`, `round3 - author2.md`). Every verdict held in substance, and the two authors disagreed on none. Four cases were rated lower than in round 1 (N2, N6, N12, N19); on N6 round-3 author 2 rated the Leon half "low to medium", which under the rounds' rule for agreement would count as low, and the case book leaves N6 AGREED until that is decided.
- **The outcome** (`tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md`): AGREED in round 1, 18 (7 held in round 2 without the book, 7 held in round 3 without the book, and 4 made for the set); AGREED in round 2, 6; BOOK-DEPENDENT, 0; SET ASIDE, 1 (N14). Every one of the twenty book-derived cases has been judged afresh without the book passages. The ids stay provisional until a round adopts a case into the O series (O53 onwards).
- **Who read what.** The sketches were chosen by a reader of the theory and the books; the verdicts were fixed by authors who read neither the theory nor, after round 1, the books. The revision-2 worklist used the candidates to choose items, so these cases are not held out from a revision 2.

## Where the files are

| Working file (session scratchpad, `source_cases/`) | Now |
|---|---|
| `cases - final candidates.md` | `tests/S89 Case book - candidate cases N1 to N25 drawn from the sources.md` |
| `sketches.md` | Part 1 below |
| `sketches - why each was chosen.md` | Part 2 below |
| `round2 - what changed.md` | Part 3 below |
| `author1.md`, `author2.md`, `cases - reconciled.md`, `round2 - prompts.md`, `round2 - author1.md`, `round2 - author2.md`, `round3 - author1.md`, `round3 - author2.md` | `tests/S89 Case book - candidate cases, author rounds/`, same names |

Book pages are cited as in the source audit: D is Deutsch, *The Beginning of Infinity* (2011), and M is Marletto, *The Science of Can and Can't* (2021), by printed page. Chapters of the pages cited: D Ch.1 "The Reach of Explanations" (pp.1–33), Ch.3 "The Spark" (pp.42–77), Ch.4 "Creation" (pp.78–106), Ch.5 "The Reality of Abstractions" (pp.107–124), Ch.6 "The Jump to Universality" (pp.125–147), Ch.7 "Artificial Creativity" (pp.148–163), Ch.8 "A Window on Infinity" (pp.164–195), Ch.12 "A Physicist’s History of Bad Philosophy" (pp.305–325), Ch.14 "Why are Flowers Beautiful?" (pp.353–368), Ch.16 "The Evolution of Creativity" (pp.398–417); M Ch.1 "Such Stuff As Dreams Are Made On" (pp.1–35), Ch.2 "Beyond Laws of Motion?" (pp.42–68), Ch.3 "Information" (pp.76–98), Ch.5 "Knowledge" (pp.139–157), Ch.6 "Work and Heat" (pp.165–196), Ch.7 "A Journey There and Back Again" (pp.204–226). No quotation from the books in this file or the rounds folder is longer than 25 words; two in the rounds folder were cut to their first 25 words on moving in.

## Part 1. The sketches, as the round-1 authors received them (`sketches.md`)

Twenty-five cases, N1 to N25. Each has a title, a situation and a question. Each situation is meant to be complete on its own: it says who was involved, what happened, and what was said or offered as an explanation. Where a case is drawn from a book, the entry names the book, chapter and printed page, so that the passage can be read. Where a case differs from the book's version, the case as written here is the one to judge.

Books: Deutsch = David Deutsch, *The Beginning of Infinity* (2011). Marletto = Chiara Marletto, *The Science of Can and Can't* (2021).

### N1 - The seasons and the sun god

**Situation.** Asked why there are seasons, Tomas explains that the Earth's axis is tilted and keeps pointing the same way in space while the Earth travels round the sun, as a spinning body keeps its axis steady. For half the year the northern half of the Earth leans towards the sun: the sun's rays strike it more directly and the days are longer, so it warms. Half a year later it leans away, the rays strike it at a slant, and it cools. Each piece can be checked on its own: a lamp warms a card that faces it more than a card tilted away from it, and a spinning top keeps its axis pointing one way. The same tilt also tells how high the noon sun will stand at each time of year. Then Tomas adds one sentence: "And the sun god, who approves of this arrangement, keeps the tilt steady." He says nothing more about the sun god, and the rest of what he says is unchanged.

**Question.** Does Tomas explain why there are seasons? Is the sentence about the sun god part of what explains them?

**Source.** Adapted from Deutsch, Ch.1 "The Reach of Explanations", pp.24–25.

### N2 - The myth amended

**Situation.** A storyteller tells the old Greek myth of the seasons. Hades, god of the underworld, carried off Persephone. Her mother Demeter, goddess of the harvest, won her release, but on terms that bind Persephone to go back to Hades for part of every year. While Persephone is away, Demeter grieves and makes the world cold and bare so that nothing grows: that is winter. When Persephone returns, Demeter rejoices and the world grows warm again. A sailor then tells the storyteller that in lands far to the south, summer comes at the very time the Greeks have winter, and winter when they have summer. The storyteller changes the myth: when Demeter grieves, she does not put out the warmth of the world but sends it south across the sea, and when Persephone comes back, Demeter calls the warmth home. The changed myth agrees with everything the sailor reported, north and south.

**Question.** Does the changed myth explain the seasons in both the north and the south?

**Source.** The myth: Deutsch, Ch.1 "The Reach of Explanations", pp.19–20. The myth set against the southern seasons: pp.19 and 24–25. The storyteller's change is made for this set.

### N3 - Persephone at home

**Situation.** In ancient Greece a farmer asks why winter comes every year. He is told the myth of Persephone. Hades, god of the underworld, carried her off; her mother Demeter, goddess of the harvest, won her release on terms that bind Persephone to go back to Hades for part of every year. While she is away, Demeter grieves and in her grief makes the world cold so that nothing grows. Consider the myth only as it stood for the Greeks. Every land they knew had its winter at the same time of year, and they knew of no other lands. The myth agrees with all of that: winter comes once a year, at the same season, in every land they knew. Nobody has ever seen Persephone leave or return, or seen Demeter grieve.

**Question.** Does the myth explain why winter comes every year? Is it an explanation of winter?

**Source.** Deutsch, Ch.1 "The Reach of Explanations", p.19 (the myth) and p.24.

### N4 - The tilt and the midnight sun

**Situation.** Over two thousand years ago, an astronomer on a Mediterranean island proposes that the Earth's axis is tilted and keeps pointing the same way in space as the Earth goes round the sun. She proposes it to explain one thing: why the noon sun stands higher in the sky in summer than in winter. Put together with what was known about heat and about spinning bodies, it also explains the seasons she knows. She and everyone she knows have seen only the lands around the Mediterranean, and nobody has heard of the far north or the far south. It follows from her idea, though nobody at the time works it out, that far enough north the summer sun never sets, that near the middle of the Earth there are no seasons, and that far to the south the seasons are reversed. Centuries later, travellers find all three.

**Question.** When she proposed it, did her explanation already explain the midnight sun of the far north, before anyone had seen it or thought of it? Or did it come to explain it only later, when someone worked out the connection or when travellers found it?

**Source.** Deutsch, Ch.1 "The Reach of Explanations", pp.26–29.

### N5 - A farmer's rule carried south

**Situation.** In a village on the northern shore of the Mediterranean, farmers follow a rule handed down for generations: "Sow the wheat after the first autumn rains, in October, and it ripens in early summer, in June." Nobody in the village knows why it works. It has held year after year, and fields sown at other times have done worse. A family from the village settles in a land far south of the equator. There the seasons fall in the opposite months: the cool rains begin in April and May, and the hottest months are December and January. The father means to farm by the village rule.

**Question.** What, if anything, does the village rule tell him about when to sow and when his wheat will ripen in the new land?

**Source.** Made for this set.

### N6 - Two astronomers and the unknown world

**Situation.** Two astronomers on a Mediterranean island, over two thousand years ago, hold that the tilt of the Earth's axis causes the seasons: the axis leans and keeps pointing the same way in space, so each half of the Earth leans towards the sun for part of the year and away from it for another part. Neither has any evidence about places beyond Europe, North Africa and the nearer parts of Asia. The tilt idea, taken as it stands, implies strange things about places far beyond: days and nights six months long in the far north, and seasons reversed in the far south. Each astronomer states the idea with a limit. Iras says: "The tilt causes the seasons in the Mediterranean and the lands around it. I make no claim about anywhere else." Leon says: "The tilt causes the seasons in the Mediterranean and the lands around it; everywhere else on Earth, the seasons also come at the same times of year as they do here." Each statement agrees with everything either of them has seen or heard.

**Question.** Does Iras explain the seasons in the Mediterranean? Does Leon?

**Source.** Adapted from Deutsch, Ch.1 "The Reach of Explanations", pp.26–28. Leon's statement is the book's; Iras's is made for this set.

### N7 - Two bakers

**Situation.** Two bakers in the same town each explain why their bread dough rises. Yeast in the dough feeds on sugars in the flour and gives off gas; the gas is trapped in the stretchy dough, which swells. Maya adds: "This holds when the dough is kept between 18 and 35 degrees." She found those limits by experience and says nothing about why they are where they are. Bea gives the same explanation with the same limits, and adds why: below about 18 degrees the yeast works so slowly that the dough hardly rises in the usual time, and above about 35 degrees the yeast begins to be harmed, and nearer 50 it dies. Between those temperatures both doughs rise just as described.

**Question.** Does each baker explain why her dough rises?

**Source.** Made for this set.

### N8 - The machine that runs forever

**Situation.** At a fair, an inventor shows drawings of a wheel that would keep turning and driving a water pump forever, with no fuel, no wind, no flowing water and nobody pushing it. Visitors ask why no such machine exists. Pia answers: "Nobody has found the right design yet. Hundreds of designs have been tried, and every one has come to a stop. Perhaps someone will find one that works." Quentin answers: "A machine that keeps doing work with nothing going into it would be making energy out of nothing. The energy anything gives out must be matched by energy put in or used up somewhere. That holds for any design, including ones nobody has tried."

**Question.** Does each answer explain why there is no machine that runs forever without fuel?

**Source.** Marletto, Ch.2 "Beyond Laws of Motion?", p.61; Ch.6 "Work and Heat", p.167.

### N9 - Dark moths

**Situation.** A species of moth rests by day on tree bark. In a district where smoke has blackened the bark, the moths change over many generations until most of them have dark wings. Pale moths stand out on the dark bark and birds eat more of them, and moths get their wing colour from their parents. In a clean district nearby, where the bark is pale, most moths of the same species are pale. No moth has any idea of the colour of the bark or of its own wings, and nobody planned the change.

**Question.** Is there knowledge of the colour of the bark anywhere in this story? If so, where is it, and what holds it?

**Source.** Marletto, Ch.1 "Such Stuff As Dreams Are Made On", p.13; Ch.5 "Knowledge", p.155. Deutsch, Ch.4 "Creation", p.78.

### N10 - The burned notebook

**Situation.** Halima, an engineer, spends a month working out why a proposed design for a long bridge would fail in strong wind: gusts of a certain speed would make the deck twist a little further with each swing until it broke. She writes the whole explanation, with her calculations, in a notebook, and tells no one. Before anyone reads it, a fire destroys the notebook, and she dies soon afterwards. Nobody else has worked it out.

**Question.** Did Halima create knowledge? Does that knowledge exist now?

**Source.** Made for this set.

### N11 - Two students, ten drafts each

**Situation.** Two students each write ten drafts of an essay on the same topic. Jana hands each draft to her teacher, who returns it with a mark and no comment. She writes each new draft without knowing what the teacher liked or disliked in the earlier ones, and in the end hands in whichever draft received the highest mark. Kasia shows her drafts to nobody. After each one, she writes down what she thinks is wrong with it (a claim with no support, a paragraph that repeats another, an ending that does not follow) and writes the next draft to fix those faults. She hands in the draft that best survives her own criticism. The two final essays are good, and about equally good.

**Question.** Did each student create what is good in her final essay?

**Source.** Made for this set.

### N12 - Consent by rephrasing

**Situation.** Before a knee operation, a surgeon reads two patients the same list of risks: infection, a blood clot in the leg, stiffness, and numbness around the scar. Asked to repeat the list, each does so word for word. The surgeon then asks each of them the same thing in other words: "Suppose your calf is swollen and sore a week after the operation. What might that be?" Then a question about a slightly different operation: "If we were operating on your elbow instead of your knee, which of these would you still need to worry about?" Mr Okafor answers each question by reciting the list again, in the same words. Ms Varga says the swollen calf could be the clot and that she would call at once; and that with the elbow, infection, stiffness and numbness would still apply, and a clot in the leg less so.

**Question.** Does each patient understand the risks of the knee operation?

**Source.** Adapted from Deutsch, Ch.7 "Artificial Creativity", p.155.

### N13 - Popper's parrot

**Situation.** A parrot lives in the hall where the philosopher Karl Popper gives a course of lectures. It learns several of his favourite sentences by heart and repeats them, word for word, to visitors. A student who missed the lectures later learns some of Popper's ideas by listening to the parrot and working out what the sentences mean. When a visitor asks the parrot a question about what it has said, it answers with another of its sentences, or with a squawk. Had the lectures been recipes, it would have repeated those just as readily.

**Question.** Has the parrot acquired Popper's ideas? What part did the parrot play in the student's learning them?

**Source.** Deutsch, Ch.16 "The Evolution of Creativity", pp.405–406.

### N14 - The robot that learned to walk

**Situation.** Dr Ferreira spends months designing a walking robot: its legs, joints and motors, its sensors, and a programming language for its control program. The language has commands such as "veer left by so many degrees", "lengthen stride" and "step over". She wrote each of them by hand from what she knows of balance, levers and the geometry of legs, keeping in mind throughout the sorts of walking the robot would need to do. She then writes only one simple program in the language: "walk forward; stop at an obstacle". From there a computer takes over. It makes thousands of slightly random variants of the program, tries each on a simulated robot over courses she chose (flat ground, slopes, small obstacles), keeps the one that walks best, makes variants of that, and repeats. After many rounds the program walks well on those courses. Put on rough, rocky ground unlike any of the test courses, the robot also walks well.

**Question.** The robot walks well on ground it was never tested on. Whose knowledge makes it do so?

**Source.** Deutsch, Ch.7 "Artificial Creativity", pp.159–161.

### N15 - The miscopied notes

**Situation.** Salma misses a class and borrows a friend's copy of the teacher's explanation of why a hot-air balloon rises: heating the air inside the balloon makes it take up more room, so the air in the balloon is lighter than the same volume of the cooler air outside, and the cooler air pushes the balloon up. The copy contains one slip: it says heated air takes up less room. Salma notices that with "less" the rest does not hang together, since the balloon's air would then be heavier than the air outside and the balloon would sink, and she changes it to "more". She then explains the idea to the teacher in her own words, and he agrees it is exactly what he taught.

**Question.** Does Salma now have the teacher's explanation? In coming to have it, did she create anything herself?

**Source.** Adapted from Deutsch, Ch.4 "Creation", p.94; see also Ch.16 "The Evolution of Creativity", pp.403–404.

### N16 - The domino that never falls

**Situation.** A huge network of dominoes is built as a calculating machine. Each domino is spring-loaded: when knocked over, it knocks over its neighbour and then springs back up, so waves of falling dominoes travel along the network's branching and looping lines. This network is set up to test whether a number is prime. The number is fed in as a row of exactly that many dominoes, and one particular domino somewhere in the network falls only if the number turns out to have a divisor. The network is fed 641 and started. An observer who does not know what the network is for watches for hours and asks: "Why does that domino there never fall?" Answer A: that domino never falls because none of its neighbours ever falls; they never fall because none of theirs does; and so on, back through billions of steps to the first domino, so that none of the waves set off by knocking the first domino over ever reaches it. Answer B: "Because 641 is prime. The network tests whether its input is prime, and that domino falls only when a divisor is found." Both answers are true.

**Question.** Does each answer explain why that domino never falls?

**Source.** Deutsch, Ch.5 "The Reality of Abstractions", pp.115–118, retelling an example of Douglas Hofstadter's.

### N17 - The transistor at the end of the run

**Situation.** A computer runs a program that finds the factors of 15. At the end of the run, one particular transistor is on. Someone asks: "Why is this transistor on at the end of the run?" Answer A: the electrons in the computer started out in such-and-such a state, and the laws that govern their motion carried them to a state in which this transistor is on. Answer B: the computer was finding the factors of 15, and this transistor is part of how it holds the answer, 3 and 5. Both answers are true.

**Question.** Are A and B two answers to one question, or answers to two different questions? Does each explain why the transistor is on?

**Source.** Marletto, Ch.1 "Such Stuff As Dreams Are Made On", pp.28–29.

### N18 - Two footbridges on opening day

**Situation.** Two footbridges of similar length open on the same day in two towns. Rhea designed hers from a worked-out theory of how loads, stiffness and sway interact; by her calculations, the bridge would stay steady under any crowd she expected. She never tested it with a crowd before it opened. Dov designed his by copying, as closely as he could, a village footbridge that had stood for eighty years; he did not know why its design worked, only that it had never given trouble. The village bridge had never carried more than a few dozen people at once. On opening day a large crowd walks onto each bridge, and each bridge sways badly.

**Question.** On opening day, did each designer meet a problem? Was each of them surprised?

**Source.** Made for this set.

### N19 - The novelist's two demands

**Situation.** Odile is writing a novel and wants two things from every chapter: prose that is rich and lyrical, and a story that keeps readers turning the pages. Planning chapter five, she sees, before writing it and before anyone has read any of it, that the long description of a valley at dawn, which she wants for its language, would stall the story at its tensest point. She drafts the chapter two ways. In the first, she cuts the description to one plain sentence: the chapter moves fast, and the lyrical passage is gone. In the second, the heroine flees across the valley at dawn, and the valley is described through what she sees as she runs: the language stays rich, and the chapter moves fast.

**Question.** Did Odile have a problem before anyone read the chapter? Does either draft solve it?

**Source.** Adapted from Marletto, Ch.1 "Such Stuff As Dreams Are Made On", pp.14–15.

### N20 - Keeping count with string

**Situation.** Two groups of goatherds keep count of their flocks with string. Nobody can measure string exactly: every measurement is off by up to a tenth of an inch. In the first group, as each goat leaves the pen in the morning, a herder reels out a length of string equal to the length of that goat; in the evening, as each goat returns, its length is reeled back in, and when all the string is back, all the goats are home. In the second group, each goat stands for exactly one inch of string, and after every goat the herder trims or lengthens the string to the nearest whole inch. Both groups also add flocks together by joining strings, and split flocks by cutting a string in two.

**Question.** Can each method keep count of a flock of any size, through any number of such joinings and splittings? What, if anything, limits it?

**Source.** Deutsch, Ch.6 "The Jump to Universality", pp.140–141.

### N21 - A rule she cannot state

**Situation.** Ngozi is a native speaker of English. She says "a lovely little old green French knife" and would never say "a green French little old lovely knife". She puts adjectives in this order in sentences she has never heard before, and gets it right every time. Asked why, she cannot state any rule; the other order "just sounds wrong". Nobody ever taught her such a rule; she picked it up as a small child from hearing people talk.

**Question.** Does Ngozi know the rule? Did learning it involve creating anything?

**Source.** Adapted from Deutsch, Ch.16 "The Evolution of Creativity", p.405; see also p.412.

### N22 - Denying the inner experience

**Situation.** People commonly report that there is something it is like to see blue: an inner experience over and above the light entering the eye and the word "blue". Two theorists deny that any such inner experiences exist. Wren says only: "There are no inner experiences. People are mistaken about this." Yuri says: "There are no inner experiences. When people look inwards, they are consulting memories of what they have just perceived, and the machinery that does this evolved to report inner experiences that never took place. People have false memories of experiences, not experiences."

**Question.** Has either theorist explained why people seem to have inner experiences?

**Source.** Deutsch, Ch.7 "Artificial Creativity", pp.153–154. Yuri's view is the one the book attributes to Daniel Dennett.

### N23 - The planets run backwards

**Situation.** Priya, an astronomer, knows exactly where each planet is tonight and how fast it is moving. The laws of motion work equally well run forwards or backwards in time, so she calculates where every planet was on this date a thousand years ago, and old records match her figures. She says: "The planets were where they were a thousand years ago because they are where they are tonight." Her colleague starts from the old records, calculates tonight's positions just as exactly, and says the reverse.

**Question.** Does tonight's arrangement of the planets explain where they were a thousand years ago? Does their arrangement a thousand years ago explain where they are tonight?

**Source.** Marletto, Ch.2 "Beyond Laws of Motion?", pp.58–59; Deutsch, Ch.5 "The Reality of Abstractions", p.118.

### N24 - Two sealed sorts of matter

**Situation.** Imagine a universe with two sorts of matter. Each sort can make atoms, machines and living things, but the two pass through each other without effect: nothing made of one sort can push, see, signal to or record anything made of the other. People made of the first sort have built a computer that, given enough time and memory, can carry out any calculation their sort of matter allows. People made of the second sort have built one that can carry out any calculation theirs allows. Some calculations can be carried out only in the first sort of matter, and some only in the second. Asha says: "Take the two computers together, and this universe has a machine that can carry out any calculation its laws allow." Bram says: "No machine in this universe can do that. A question written in one sort of matter can never be read by a computer made of the other."

**Question.** Which of them is right about whether any machine in that universe can carry out every calculation its laws allow? Does Bram's reason explain why or why not?

**Source.** Marletto, Ch.3 "Information", pp.93–95.

### N25 - What holds the universe up

**Situation.** Three cosmologies each say what holds the universe up. The first: the universe rests, forever unmoving, on the head of a dog that stands outside it; the dog is eternal and will never change. The second is the same in every respect, except that it says a turtle. The third: a turtle holds the universe up, that turtle stands on another turtle, and so on down without end. In all three, nothing inside the universe can reach, see or affect whatever holds it up.

**Question.** Does any of the three explain what holds the universe up? Do the dog story and the turtle story say different things?

**Source.** Marletto, Ch.2 "Beyond Laws of Motion?", pp.47–48 and 55; Deutsch, Ch.8 "A Window on Infinity", p.174.

## Part 2. Why each sketch was chosen (`sketches - why each was chosen.md`)

**Not for case authors.** This file maps each sketch in `sketches.md` (Part 1 above) to the observation it tests in `results/S89 The theory against its sources - Deutsch and Marletto.md` (cited as "obs 1–15" and "M1–M11"). Theory citations follow that note: `10:330` is file 10, line 330. Nothing under `Semantics/results/S81 …` or any S81 return was read. The Pinker extraction was not opened. The S81 case book was read for its format only, plus a check for overlap. Book pages were checked in the Deutsch (D) and Marletto (M) extractions.

### Coverage at a glance

| Observation (verdict) | Sketches |
|---|---|
| 2 Hard-to-vary is a lemma; idle parts (PARTLY CONFIRMED) | N1, N2 |
| 4 Two senses of "explanation" (CONFIRMED) | N3 (N2 also bears on it) |
| 5 Reach, positive and negative (PARTLY CONFIRMED) | N4, N5 |
| 6 Stated scope against a limit that must be explained (PARTLY CONFIRMED) | N6, N7 |
| 7 Impossible against never happened (CONFIRMED) | N8 |
| 8 Knowledge as self-preserving information (CONFIRMED) | N9, N10 |
| 9 Selection against construction (CONFIRMED) | N11 |
| 10 Unattributed parallels with D Ch.7 and Ch.16 (CONFIRMED) | N12, N13, N14, N15 |
| 11 Question fidelity; the right level (PARTLY CONFIRMED) | N16, N17 |
| 12 Regress (REFUTED as a gap; same-form regress NOT ESTABLISHED) | N25 (third cosmology); N16 in passing |
| 13 Surprise is narrower than "problem" (PARTLY CONFIRMED) | N18, N19 |
| 14 Error-correction; inexplicit knowledge (PARTLY CONFIRMED) | N20, N21 |
| 15 Absence cases; Attack B (PARTLY CONFIRMED) | N8, N22 |
| M1 Derived direction | N23 |
| M2 Problem as clashing criteria, close to Repair | N19 |
| M3 Whose knowledge the evolved program's reach is | N14 |
| M4 Interoperability against "any carrier" | N24 |
| M5 Testability as a counterfactual; the dog-or-turtle label | N25 |
| M6 Eliminative explanation must explain the appearance | N22 |
| M7 Idle parts | N1 |
| M8 The positive side of reach | N4 |
| M9 Hard-to-vary as error-correction in transmission | N15 |

Not testable, so no sketch: obs 1 and obs 3 (attribution), M10 (a deliberate abstention: 10:27, 10:510), M11 (the skill's attribution), and obs 14's aesthetics (left empty on purpose: 10:25, 10:458).

### Per sketch

**N1 - The seasons and the sun god.** Obs 2 and M7. D p.25 calls superfluous features a way to be bad. File 10's (E) accepts an idle commitment, and Part VI reports it without rejecting it (10:330; the lemma is not a condition). This is the verification's *Seasons with a flourish*. It adds D p.24's independent checks of the tilt, so the rest of the explanation is plainly good. The sun-god clause claims the same work that the spin clause already does ("keeps the tilt steady"), so the case also shows whether a redundant claim is treated as idle or as damaging. What it tests: whether a thoughtful verdict matches the split between fidelity, which (E) grants, and hard-to-vary, which Part VI measures only.

**N2 - The myth amended.** Obs 2, the verification's *The myth amended*. It draws on D pp.19–20 (easily varied myths) and D pp.24–25 (the southern seasons refute the myth). It tests whether an explanation that is easy to vary, repaired after the evidence to fit it, passes (E). If so, the only objection left sits in Part VI, which is not a condition. It also touches non-circular dependence, since Demeter's moods are known only through the seasons, and narrowing after a failure (Derivation 7; 10:456).

**N3 - Persephone at home.** Obs 4. D p.19 says the false myth "does constitute an explanation". The theory says "What cannot count as explanation is an error in the very dependence alleged to do the work" (10:86), while its *explanatory candidate* (10:246) is Deutsch's broad sense. The two questions let the author split "is an explanation" from "explains". The verification's note for the author (D p.24: no way to know Demeter is sad "other than the onset of winter itself", which bears on non-circular dependence) is **not** given as a hint. The situation states only the plain fact that nobody has seen Persephone or Demeter.

**N4 - The tilt and the midnight sun.** Obs 5 and M8. The positive side of reach: D p.28 (found "only after we have the explanation") and D p.29 ("determined by the content of the explanation itself"). Theory side: reach is undefined in 10/11/12; 00:383 had a definition; the contract ranges over unperformed changes (10:158, 00:208); 11:401. It tests whether Account(E, f) for an unforeseen job f is fixed by the content and the world, or depends on anyone's working it out. This is the verification's *Tilt beyond its brief*.

**N5 - A farmer's rule carried south.** Obs 5, negative side. A rule fitted by selection, taken outside its history. File 10's Derivation 3 (10:567–573) makes a selected transport underdetermined at every unseen pair. File 11's Derivation 3 (11:560–566) lets "a population restriction, a physical relation, or another stated constraint" fix a value never tested. D p.78 has "limited reach", not none. The rule is worded on purpose with an event anchor ("first autumn rains") and month anchors (October, June), which agree at home and conflict in the south. This is where "the rule already fixes a value" and "the rule is silent" come apart. This is the verification's *A fitted rule abroad*.

**N6 - Two astronomers and the unknown world.** Obs 6. Non-vacuity accepts any stated exclusion (10:272; Grievance 4, 10:41). File 11 leaves the appropriateness of a restriction open (11:161, 11:514). This sketch merges two things. Iras is the verification's *Seasons, known world only*: a limit on the claim. Leon is D p.27's own modified theory: a limit on the content, which asserts something different elsewhere and which D p.28 calls "no longer an explanation of seasons, just a (purported) rule of thumb". The pair tests the verification's finding that the tension is narrower than claimed, because the theory limits the claim and Deutsch's example limits the content.

**N7 - Two bakers.** Obs 6, the verification's *Bread between two temperatures*. M p.24: a limited theory is "problematic" because "one still has to explain why they hold only at that scale". The owner's skill ("Check the patches": a held limit comes with its reason) takes the books' side. It tests whether a stated limit with no reason (Maya) still leaves an explanation, against the same limit with its reason (Bea). The temperatures were changed from the sketch's 18–25 to 18–35: yeast is not harmed at 25 °C, so the sketch's "dies well above" would have given Bea a false reason. Maya's limit is said to come from experience, so it is honest but unexplained. On overlap: S81 O5 (Greta: a reasoned limit against "Tuesdays") and O8 (Petra: an honest scope) do not isolate an experience-based limit given without a reason.

**N8 - The machine that runs forever.** Obs 7 (impossible against merely absent) and obs 15. M p.61: "that a perpetual motion machine is impossible does not mean it does not happen under a particular initial condition!" M p.167 gives conservation as an impossibility. Theory side: Part VII Obstruction (10:346–348, invariants); edits must be "physically admitted" (10:41, 10:272); file 12's explicit link (12:491). Pia gives a history-of-absence answer, and Quentin an invariant-for-every-design answer. This is the verification's *No machine that runs forever*. The chess draw (M pp.64–65) was left out because it tests the same Obstruction distinction; the verification notes that such cases "aim at Obstruction more than at Attack B".

**N9 - Dark moths.** Obs 8. M p.13 ("does not have to be known by anyone: the moth does not know its wings are black") and M p.155 (knowledge as information "capable of remaining instantiated"). File 10 has no such notion: Derivation 6 excludes an "is knowledge" predicate, and "information" occurs 0 times. 00:995–1011 had a conditional bridge that was dropped. The question was reworded from the verification's "do the moths, as a population, hold knowledge" to "is there knowledge … where … what holds it", so that it does not suggest the population answer.

**N10 - The burned notebook.** Obs 8, the verification's own sketch. File 10's (EK) (10:446–456) is explanatory knowledge held by a system. Marletto's knowledge must be able to remain instantiated. The case separates *created* from *persisting*. It shows whether thoughtful judgement ties knowledge to persistence (the books) or to the episode of creation (file 10).

**N11 - Two students, ten drafts each.** Obs 9. File 10:216: "a selected transport has no represented target and no criticism in its history; a constructed one has both". D p.78 counts criticism as selection in the broad sense. File 11 dropped "blind" from Part 0 (11:15). Jana keeps whatever an outside judge scores highest, without knowing why. Kasia keeps what survives criticism aimed at stated faults. It tests whether "create" follows the theory's mark (criticism and a represented target in the student's own history) or Deutsch's broad sense. It also tests whether the teacher's knowledge is credited to Jana. The verification's sketch left open how Jana produced new drafts. The sketch now says only that she wrote them without knowing what the teacher liked.

**N12 - Consent by rephrasing.** Obs 10. D p.155 (rephrase the question, or ask a different question with similar words, and "check whether the replies change accordingly") matches Part IX Reason use. The verification's sketch had one patient and did not say what the answers were, so nothing could be judged. Two patients now give opposite response patterns under the same probes.

**N13 - Popper's parrot.** Obs 10. D p.406: the parrot transmits "no more than the air in the lecture theatre does". This matches "relay is not" construction (10:414). The second question (what part the parrot played in the student's learning) was added to test relay directly, beyond whether the parrot acquired the ideas.

**N14 - The robot that learned to walk.** Obs 10 and M3. D pp.160–161: "a much more obvious explanation of their abilities, namely the creativity of the programmer", and knowledge "packed into that language … will have reach". Theory side: file 11's Ownership (11:419) and New (N); declared provenance. Most important is file 11's Derivation 3, where a population may fix a selected transport's value on unseen changes (11:197, 11:473, 11:566). That is the claim under test in S76, and the case asks whose knowledge that fixing is. D p.156 (utterances tell nothing without an explanation of how they were created, matching Derivation 9's last sentence) is touched here and was not given a case of its own.

**N15 - The miscopied notes.** M9 and obs 10's deliberate departure. The verification has no sketch for this; it is new. D p.94: "random errors in the transmission of a good explanation are easier for the receiver to detect and correct". No theory file links this to Part X or file 11's Recoding (11:363). The same page, D p.94 ("Those meanings are conjectured by the listener or reader"), with D pp.403–404, holds that grasping any idea is creative. File 00 rejected "every acquisition is creation" (00:1304–1306). The second question tests that departure.

**N16 - The domino that never falls.** Obs 11. D p.116: the domino-by-domino answer addresses "a different question – predictive rather than explanatory" and asks "at the wrong level of emergence". D p.117: the physics answer "is true as well". Theory side: (A) and Part III (10:168); grain is a declared index (10:523); 11:279. It also bears on obs 12 (D p.116, "passing the buck"). This is the verification's sketch with the book's details.

**N17 - The transistor at the end of the run.** Obs 11. M pp.28–29 treats this as one question with "at least two answers", both "essential". The theory would count two questions with different targets or contracts. The first question asks the author to count questions, which is the exact point where the verification found a difference in counting.

**N18 - Two footbridges on opening day.** Obs 13. Surprise is defined only for a selected transport (10:232–238; 11:219–225; Derivation 4, 10:577). A refuted constructed theory is handled by K1/K3 and an undefined "recognized difficulty" (10:432). File 12 widened surprise to any tested history (12:217–225). This merges the verification's *The engineer's bridge* (Rhea) with a selected design for contrast (Dov: a copied bridge meeting crowd loads outside its eighty-year history), so one case separates the two. "Surprised" is left in its ordinary sense on purpose.

*25 September: chained quotes shortened to keep within the 25-word rule (decision S19); meanings and page references kept. The places: N19 and N22 below.*

**N19 - The novelist's two demands.** M2 and obs 13. M pp.14–15: the author "has to find a way of meeting both these criteria". D p.17: a problem can arise from theory alone, with no observation involved, and solving one means creating an explanation in which the conflict is gone (paraphrased). Theory side: Repair_{O,P} (10:441), meeting o without losing any protected r; 00:785, 00:804. Draft one meets the pace demand and gives up the protected lyrical demand. Draft two meets both. The problem is seen before any reader or test. The verification's *Two theories at odds* (a physicist's two theories disagree about an experiment not yet run) was folded in here to keep the set at 25. If the owner wants a clash between theories about the world, not between criteria, that sketch should be restored.

**N20 - Keeping count with string.** Obs 14, error-correction. D pp.140–141, taken almost unchanged. Theory side: (T2) "Without a modulus, no accumulated bound follows" (10:376), (RC), and the accuracy grades of CT3/CT4. The candidate lemma is that unbounded processing at a fixed accuracy needs a correction step. The measurement tolerance is given the same for both methods, so the only difference is the rounding step.

**N21 - A rule she cannot state.** Obs 14, inexplicit knowledge. D p.405 ("We know the rules … largely inexplicitly, yet we pass its rules on with remarkable fidelity") and D p.412. The text 00:855–861 ("Inexplicit representation is not absent representation") was dropped by file 10. Build asks for "the bindings constructed" (10:414). An English adjective-order example was added so the rule is concrete.

**N22 - Denying the inner experience.** Obs 15 and M6. D p.154: "simply to deny their existence is a bad explanation: anything at all could be denied by that method". A denial must be backed by a good explanation of why the mistaken beliefs appear so different in kind (paraphrased). Theory side: Part VII removal (10:350–352), the exposed case in Attack B; file 12's absence and prevention (12:341–347). Part VII does not ask for the appearance to be explained. The verification's *The dismissed feeling* is split into a bare denial (Wren) and the view D attributes to Dennett (Yuri), so the case separates "deny" from "deny and give a story of the appearance". Deutsch's own further criterion (why this false belief seems unlike other false beliefs) is not stated in the situation.

**N23 - The planets run backwards.** M1. M p.59: the laws are reversible, so one may explain the sequence "in terms of the final snapshot". D p.118: "at that level of explanation, cause and effect are interchangeable". Theory side: direction derived from admitted edits (10:126; pole and shadow, 10:338); file 12's Derivation 3, with time entering "as a restriction on which edits are admitted" (12:45, 12:580–584). No one can move a planet, so the case tests whether direction still comes out. Not written, to stay within 25: the verification's other suggestion, a case with edits allowed at both ends (file 12's "mutual dependence"). A candidate is two syringes joined by a water-filled tube, where either plunger can be pushed and one was.

**N24 - Two sealed sorts of matter.** M4. M pp.93–95: "A universe where the interoperability property is violated would not have universal computers". Theory side: Part I "Any carrier may bear an organization" (10:92); 00:912 [R3], which file 10 dropped; Part XIII's physical barrier. The verification's *two sealed sectors* is recast with two speakers, so there is an explanation on offer to judge.

**N25 - What holds the universe up.** M5, and obs 12. M p.48: "how can one even check whether it is a dog or something else?" Where no admitted change separates dog from turtle, the kinds clause and Derivation 2 make them one kind, and the label does nothing (the second question). M p.47 makes testability a counterfactual, which matches non-vacuity's physically admitted contrast (10:290). The third cosmology is D p.174's turtles all the way down, with M p.55's "dogs all the way down". The verification found this same-form regress NOT ESTABLISHED: it is caught only if "the target's answer" is read structurally at the grain (10:270; 00:210). It is included for that reason, although obs 12 as a whole was refuted.

### Left out, and why

- *The confident wrong diagnosis* (obs 4, the mechanic): dropped to stay within 25. N3 carries obs 4. Restore it if a case is wanted that tests the dependence error without the myth's circularity.
- *Two theories at odds* (obs 13): folded into N19 (see there).
- *A king and a knight against a king* (obs 15, M pp.64–65): the same Obstruction distinction as N8.
- *A starting state chosen to fit* (obs 12, M p.56): obs 12 was refuted, and Part VII already covers it (10:344).
- *Turtles* (obs 12): folded into N25 as the third cosmology.
- The program's joke (D pp.155–156, Derivation 9): touched through N14 only.
- A both-ends direction case (M1): see N23.

### A caution for the owner

Several sketches retell a book passage in which the book's author gives his or her own verdict: N3 (D p.19), N13 (D p.406), N16 (D pp.116–118), N17 (M pp.28–29), N20 (D pp.140–141), N22 (D p.154), N23 (M p.59), N24 (M p.95) and N25 (M p.48). An author who reads the cited passage will meet that verdict. If verdicts are to be independent of the books as well as of the theory, withhold the "Source" lines on a first pass and release them afterwards.

## Part 3. Round 2, what changed (`round2 - what changed.md`)

23 September 2026. Internal record. The case authors will not see this file.

This file compares `round2 - prompts.md` with `cases - reconciled.md`, the two authors' FIX NEEDED notes (`author1.md`, `author2.md`) and `sketches.md` (Part 1 above). The first four are in `tests/S89 Case book - candidate cases, author rounds/`. It lists, for each id, what was changed and why.

### Changes made to every prompt

- **Removed:** every Source line (book, chapter, page), every status, verdict, confidence and "Fix before use" block, and the reconciler's bracketed notes (such as N16's "(Reconciled: Answer A is restated ...)"). A prompt now holds only its id, title, Situation and Question(s).
- **Checked:** the prompts file contains no author name (Deutsch, Marletto, Popper, Dennett, Hofstadter), no mention of books, chapters or pages, and does not say where any case comes from. The header does not say which cases were disputed or rewritten.
- **Headings:** "Question" when there is one question and "Questions" when there are more.
- **Order:** the cases appear in the order the task listed them.
- **Verified by script:** the Situation and Question of N3, N16, N20, N23, N24 and N25 match `cases - reconciled.md` exactly. The Situation of N9 and N21 matches the sketch exactly.

### Per id

#### N3 - A myth about winter (was "Persephone at home")
- **Situation and question:** word for word as reconciled.
- **Title:** changed. "At home" only makes sense beside N2 ("The myth amended"), and the new title is neutral.
- **Kept on purpose:** the myth's own names (Persephone, Demeter, Hades). They are the content of the case, a public Greek myth, and do not point to the book. Renaming them would turn the case into an invented myth.
- **Not applied:** the reconciled file's proposed split of the question into (a), (b) and (c). The task said to keep this case word for word. The two senses of "explain" remain in the question. Both authors rated it medium, so expect answers to split on that word.

#### N13 - The parrot in the lecture hall (was "Popper's parrot")
- **Title:** changed, because it named the philosopher.
- **Situation:** "the philosopher Karl Popper" is now "Professor Marsh", and "Popper's ideas" is now "Professor Marsh's ideas". "Philosopher" was dropped too, because a parrot in a philosopher's lecture hall is the recognisable anecdote. The recipes line still gives the contrast between ideas and mere sounds, so nothing else changed.
- **Question:** "Popper's ideas" is now "Professor Marsh's ideas". The rest is word for word.
- **Effect on the verdict:** none expected. Both authors' reasoning never depended on who the lecturer was.

#### N16 - The domino that never falls
- **Situation and question:** word for word as reconciled, with Answer A in its summary form. The title was already neutral and is kept.
- **Residual risk, not changed:** a network of dominoes testing whether 641 is prime is a well-known example, and a reader who knows it may recognise the source. The task said to keep this case word for word, and the number is load-bearing (641 is prime; 640 is not).
- **Not applied (single-author note):** A1's "it runs until it stops".

#### N17 - The transistor at the end of the run (DISPUTED; rewritten)
- **Answer A:** now the full version. The sketch's placeholder ("started out in such-and-such a state") is replaced by the full calculation of the electrons' motion from their exact starting state. It has been done in full, is correct, and would fill libraries. This follows the reconciled proposal (a), which says to use A1's wording if A is to be a real rival to B. The rewrite settles which A is meant, which is what split the authors: A2 judged A as an empty placeholder, while A1 allowed it as a full physical account. "Both answers are true" is kept.
- **Question:** "Are A and B two answers to one question, or answers to two different questions?" is dropped, since both authors found it partly a matter of words. It is replaced with A2's pair, minus "as stated", which no longer fits a full A: "Does Answer A tell the asker anything that Answer B does not? Does Answer B tell the asker anything that Answer A does not?" "Does each explain why the transistor is on?" is kept last, as proposal (c) allows once A is fixed.
- **Rejudge:** neither author's verdict carries over. A2 said a full A "would be a real physical account ... an explanation of a sort", so the round must judge this case afresh.
- **Contrast with N16:** N16 uses the summary form of its Answer A, and N17 now uses the full form. If the round wants the two cases to test the same thing, align them. As they stand, they test different things.

#### N20 - Keeping count with string
- **Situation and question:** word for word as reconciled. The title was already neutral.
- **Not applied (optional notes):** A1's alternative question and A2's clarifications (how the second group tallies, whether the error limit holds for long strings).

#### N22 - Denying the inner experience (DISPUTED; rewritten)
- **Question:** now "Does either theorist give any reason why people believe and say that they have inner experiences?" This is the reconciled proposal (a), minus "would", as the task worded it. Part (b), whether Yuri's reason satisfyingly accounts for the seeming, was set aside, as the reconciled file says. The word "seem", on which the dispute turned, is gone.
- **Situation:** "there is something it is like to see blue:" is now "seeing blue involves an inner experience,". "Something it is like" is a stock phrase from a famous philosophy paper and a term of art in that field, so it both signals a source and acts as a theory term. The meaning is unchanged: an inner experience over and above the light and the word.
- **Kept on purpose:** Yuri's statement is word for word. It matches a known philosopher's view, but it names nobody, and it is the substance of the case.

#### N23 - The planets tonight and a thousand years ago (was "The planets run backwards")
- **Situation and question:** word for word as reconciled.
- **Title:** changed. "Run backwards" echoes the situation's point about laws working both ways in time, which invites the symmetric answer. It also suggests the planets physically reverse. The new title only names the two times being compared.

#### N24 - Two sealed sorts of matter
- **Situation and question:** word for word as reconciled. The title was already neutral.
- **Not fixed:** the second question, "Does Bram's reason explain why or why not?", which A2 called garbled. It was kept word for word as the task instructed. A2 suggested "Does Bram's reason explain why no such machine can exist?", but that states that no machine can exist, which would hint at the answer. If the round rewrites it, a neutral form is "Does Bram's reason explain why his answer is right or wrong?"
- **Not applied:** the definition of "a machine that can carry out any calculation", which both authors asked for, because of the word-for-word instruction. Expect some answers to treat the question as partly about words.

#### N25 - What holds the universe up
- **Situation and question:** word for word as reconciled. The title was already neutral.
- **Residual risk, not changed:** the endless stack of turtles recalls a famous anecdote. The reconciled text avoids the anecdote's catchphrase, and the stack is load-bearing.
- **Not applied (optional notes):** A1's "suppose it needs holding up" and A2's split of the second question.

#### N4 - The tilt and the midnight sun (DISPUTED; rewritten)
- **Question:** split into two plain questions. The first is from the reconciled proposal: "did her idea already account for the midnight sun, or did it come to account for it only once someone worked out the connection?" It uses "account for" of the idea. The second is also from the proposal: "Had anyone, she included, explained the midnight sun before someone worked out the connection?" It uses "explained" only of people. That separates the two uses of "explain" that made A2 mark the wording low. The optional third question, about the travellers, was dropped, since the task asked for two questions. For the same reason, "or when travellers found it" is gone from the first question.
- **Situation: A1's two FIX NEEDED changes applied.**
  - Added "She knows the Earth is a sphere." The midnight sun follows from the tilt only for a round Earth.
  - Changed "near the middle of the Earth there are no seasons" to "the seasons are slight". The original is inaccurate, and a careful reader could object to it.
  - These fix accuracy, not wording. A2 judged the case without them, but A2's verdict does not depend on either.
- **Situation: A2's note applied lightly.** "Nobody has heard of the far north or the far south" is now "none of them has heard of ...". It now describes only her circle, which is fiction, rather than making a false claim about history.
- **Kept:** "It follows from her idea, though nobody at the time works it out". Both authors say the case needs this fact, although it leans towards "already".

#### N9 - Dark moths (DISPUTED; rewritten)
- **Question:** replaced with the reconciled proposal, which never uses the word "knowledge": "Leaving aside the birds' eyesight and any person who studies the moths: is there anything in the moths from which an observer could tell the colour of the bark in their district? If so, where is it, what holds it, and how did it get there?"
- **Departure from the reconciled wording:** "what carries it from one generation to the next" is now "what holds it", which is the sketch's own phrase. The proposal's wording takes for granted that the thing is passed down the generations, which is the heart of the expected answer (heredity, not any single moth).
- **Kept:** the "leaving aside" clause. It removes the birds' eyesight, which A1 found to be an unintended candidate answer.
- **Situation:** unchanged from the sketch.
- **Not added:** any follow-up about knowledge (A1's "would you call it knowledge?", A2's "do the moths know?"), which the reconciled file says would bring the dispute back.

#### N14 - The walking robot (UNUSABLE; rewritten; was "The robot that learned to walk")
- **Title:** changed. "Learned" gives the robot, and so the search, the credit in advance.
- **Situation: leading clause removed.** A2 flagged "keeping in mind throughout the sorts of walking the robot would need to do" as pointing to her, so it is gone.
- **Situation: starting program described.** Both authors found the case underspecified without this. The new sentence: "Run on its own, that program walks on flat ground, but it slips and falls on slopes, halts at every obstacle, and on rough, rocky ground falls within a few steps." It merges A1's "fell over on the slopes and at most obstacles" with A2's "falls within a few steps" on rocky ground. "Halts at every obstacle" replaces A1's "fell over ... at most obstacles", because the program as written ("stop at an obstacle") would halt, not fall. The low-performing version was chosen over A1's opposite ("already walked tolerably"). It makes the search's contribution real, so the question is a fair contest between design and search.
- **Question:** "Whose knowledge makes it do so?" is replaced with the merged proposal: "What accounts for the robot walking well on the rocky ground: Dr Ferreira's design, the computer's search, or both? If both, in what share? How could you tell?" This removes "whose", which assumed a person, and "knowledge".
- **Not added:** A2's optional comparison with a general-purpose command language. It would answer "How could you tell?" inside the situation, and it points towards her design.
- **Rejudge:** the reconciled file says neither old verdict carries over. The case must be judged afresh.

#### N18 - Two footbridges on opening day (DISPUTED; rewritten)
- **Situation: Dov's expectation and knowledge added,** in A1's wording, split into two sentences: "but Dov did not know how many people it had ever carried. He expected his bridge to be as trouble-free as the original." A2's "confident it would be as trouble-free" says the same about his expectation.
- **Situation: Rhea's range added,** from A2's point 1: "The crowd on Rhea's bridge is no larger than the crowds she had calculated for." Her calculations are therefore contradicted.
- **Question on "problem":** "problem" is now defined in A1's sense: "did each designer meet a problem, meaning something he or she must now understand and fix?" That settles which of the two senses the authors noted is meant.
- **Question on "surprised":** "Was each of them surprised?" is replaced with A1's two questions about expectation and reason: "Did the swaying go against what each designer expected? Did it contradict anything either of them had reason to expect?" In A1's wording, "a reason to expect" is shortened to "reason to expect".
- **Rejudge:** the facts the split rested on are now given, so this must be judged afresh.

#### N21 - The order of adjectives (DISPUTED; rewritten; was "A rule she cannot state")
- **Title:** changed. The old title stressed her inability, which bears on the first question ("Does she know the rule?").
- **Question:** the second question is now "Was her grasp of it handed to her, or did she form it herself?", as the task asked. This is a shortened form of the authors' shared rewrite. It drops "Since nobody ever stated the rule to her" (a restatement of the situation) and "did she have to ... from what she heard", which both lean towards "herself". "Creating" is gone.
- **Kept:** the first question ("Does Ngozi know the rule?") and the situation, unchanged from the sketch.
- **Not applied:** A2's optional split of the first question.

### Not in this round
- N6 is not redone, so its source-line fix is not needed here.
