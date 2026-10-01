# What Astra's timing replies offer, in plain words

*Log S122, 1 October 2026. The three replies came with no words from you. The second reply first arrived as an empty file; its second copy is being checked separately and will be added here.*

## The main point

Astra designed an execution environment that remembers: it keeps track of what the programs have been able to do lately and sets its pay from that memory, much as a nerve cell's answer depends on what it heard a moment ago. It works exactly as written, but in a short first trial its memory made no difference you could see in what the programs learned, and the part meant to hold a problem open never switched on.

## One example, step by step

Two words first. A **job** is one of the 77 small logic tasks Avida can check a program for, such as "not" (turn every 0 into 1 and every 1 into 0). **Pay** is extra running time, so a program that does a paid job copies itself faster.

1. **What the execution environment does.** Every 1,000 updates it stops, tests every program on three numbers given in each of their six possible orders, and writes down what share of programs can do each job. Then it sets the pay for the next 1,000 updates. The total pay is fixed; only how it is shared changes. A few jobs are never paid, to see whether they appear anyway.
2. **One of its parts: tiring.** It keeps a fading memory of each job's share: each time, it keeps about four fifths of what it remembered and adds one fifth of what it sees now. The more common a job has been lately, the less it pays; as the memory fades, the pay comes back. This is like a nerve cell that answers less to a sound it keeps hearing.
3. **The comparison.** The same execution environment with its memory wiped before every step, so it sees only the present.
4. **What happened.** Two tries of each, 20,000 updates. In all four the simplest jobs ("not", "not both") became common after about 5,000 updates. The remembering execution environment then cut their pay to about half that of rare jobs, and those jobs stayed less common than in the wiped one. But at the end the remembering one had 2 and 6 jobs common, the wiped one 4 and 5. No unpaid job became common.
5. **The part that holds a problem open** switches on when a job works in the world's one order of numbers but almost never in the others, or when a common job is suddenly lost. Neither happened, so that part was never tested.

The pay was weak (each job was worth about a fifth more running time), and at that strength memory changed the pay a little but not what the programs learned.

## Each reply

**Reply 1, the remembering execution environment.** A complete design with working code, seven small parts and four kinds of comparison. Every claim about Avida's code held, and everything it said it ran came out the same here, number for number. Its weaknesses: weak pay, a comparison that removes more than memory, and a part that pays any surprise, good or bad.

**Reply 3, research.** Nine ways that living and artificial systems use timing to judge or choose, each turned into a way of paying Avida programs. Thirteen of its sources were looked up; every one said what it said. It also checked your report's sources: one points at the wrong article, one is called a review but is an experiment, one does not support what it is cited for; the report's main line still stands. Its most useful point: Avida already has a remembering kind of pay, food that runs down when many programs use it and refills over time.

**Reply 4, does timing close the gaps.** It goes through eleven things the execution environment lacks, such as keeping a question open or being surprised, and says what a small timing part could supply for each. Its answer: timing gives persistence, forecasts and alarms cheaply, but never says what they are about, and that "what" is still a written list. Its sums matched; its proposed experiment is sound, but its extra pay is too small to expect a difference.

## Tested, not tested, unsure

**Tested:** every claim about Avida's code in the three replies; everything reply 1 ran; that the remembering execution environment pays differently after two different pasts ending the same way (the wiped one cannot); a short trial against the wiped one, two tries each.

**Not tested:**
- Stronger pay, or a start from programs that already do many jobs.
- A comparison that removes only memory.
- The long experiments the replies propose (20 to over 400 hours of computer time).

**Unsure:**
- Whether a fixed way of choosing, even one with memory, counts for you as an instinct.
- Whether a chooser that runs between stretches of Avida counts as part of the execution environment.

## One next step

Run the remembering execution environment again with pay strong enough to matter, against two comparisons: memory wiped, and memory removed but everything else kept. That would show whether the parts that need a past ever switch on, and whether memory changes what the programs learn. It takes about two hours of computer time, but it changes Astra's design, so it waits for your word.
