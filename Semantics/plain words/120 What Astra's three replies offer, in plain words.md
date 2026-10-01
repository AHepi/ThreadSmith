# What Astra's three replies offer, in plain words

*Log S120, 1 October 2026. Your words with the replies: "First 3 in." The fourth reply came later and is checked separately.*

## The main point

An execution environment that pays programs for guessing the next number the world will hand them makes them learn to guess it, fast, starting from programs that could not read a number at all. But the rule behind the numbers is still one the designer wrote, so the execution environment's standard still comes from inside its own code.

## One example, step by step

A word first. A **stream** is the line of numbers the world hands one program, one at a time, each time it reads.

1. **What the execution environment pays for.** Astra's first reply changed Avida's code so that each program gets its own stream. In the version tried here, the stream starts at a random number and each next number is one more than the last: 7, 8, 9, 10, and so on. Whenever a program hands back a number, the execution environment checks it against the number that program is about to be handed. If they are equal, the program gets twice the running time for that copy. The checking code never contains the rule "add one"; it only compares two numbers.
2. **What a program has to do.** Read a number, add one to it, and hand that back just before reading again. In Avida's instructions that is three steps: read, add one, read. The first program in every run cannot read or write at all.
3. **What happened.** In two tries of 20,000 updates each, programs that do this appeared within a few hundred updates. By the end, 95 of every 100 programs did it.
4. **Was it really "adding one"?** Every saved program was tested again with fresh streams under three rules. With numbers that go up by one, about three quarters of them matched. With a number that only repeats, about a third matched. With random numbers, none did. Programs from a world that repeats one number almost never matched the "add one" stream. So they had learned the step, not a trick.
5. **Was it the pay?** The same try with the match counted but not paid: never more than 3 programs in 100 did it.

So the pressure works, and fast. What the programs found is one short fixed step. It is not a harder problem each time, and the rule was still written by a person.

## Each reply

**Reply 1, paying for what comes next.** A small change to Avida's code, with tests. Everything it said it ran was rerun here and came out the same, number for number, and with the new part switched off Avida behaves exactly as before. Its weakness is the one in the example: when the rule is fixed, "guess the next number" is just one function, named in disguise.

**Reply 2, a chooser with a memory.** Two ways for the execution environment to change its pay as it goes: pay most for what the programs are getting better at, or pay most for what it has seen least. All its small checks were rerun and matched exactly. But a short trial showed that its pay is too weak to get started. In 20,000 updates no task became common, and the "getting better" version stopped paying almost at once, because nothing was getting better yet.

**Reply 3, research.** Sixteen known ways to choose without a final goal, from novelty-seeking to systems that set themselves new tasks. Eight of its sources were looked up. Seven said exactly what it said, and one could not be checked. Every claim about Avida's code held. It finds no method anywhere whose standard is free of written rules. It also found that in Avida's usual setup programs cannot be infected by parasites, which closes one route the last report hoped for.

## Tested, not tested, unsure

**Tested:** all three replies' claims about Avida's code; everything replies 1 and 2 said they ran; the guessing environment from the starting program, with and without pay; reply 2's two choosers against a fixed one; eight of reply 3's sources.

**Not tested:**
- A world whose rule changes partway through.
- A world whose next number comes from something no one wrote, such as another program.
- Reply 2's choosers with stronger pay.
- The long experiments the replies propose. They would take 150 to over 1,000 hours of computer time.

**Unsure:**
- Whether learning a fixed step like "add one" counts, for you, as an instinct to solve problems.
- Whether a world whose standard comes from other programs would count as having no named target. That is close to the question about the task list you left open.

## One next step

The cheapest test that bears on your question is the rule change. The execution environment repeats one number for a while, then switches to adding one, and we watch whether the programs pick up the new step without being told. It takes under two hours of computer time and is ready to run. A test of whether reply 2's choosers do better with stronger pay is about as cheap, but it changes reply 2's design, so it waits for your word. Nothing is run until you say.
