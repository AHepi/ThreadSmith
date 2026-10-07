# Author 2-1: prompt2 case

*Second pair, author 1: one of two fresh Claude subagents that fixed D3-T's verdict on 23 September 2026 from the reworded case (`prompt2.md`), without having read the theory. Moved into the repository on 23 September 2026 from the session scratchpad, where it was `d3t/author2-1.md`, with only this paragraph added.*

**Thoughtful person's verdict.** No. The discarded design differs from the kept one at a setting the tester does try (A on, B off), so it is not a controller that passes. It tells you nothing about what a passing controller could do at the untried setting. With only two designs in existence and only one of them passing, passing tells you which design you have, and so it also tells you how that controller behaves with A and B both on. To show that passing leaves this open, Ivo would need two designs that both pass and still differ at the untried setting, and no such pair exists.

**Confidence.** High. One reasonable alternative reading: "leaves open" could mean only that the tester never looks at that setting, so its records alone say nothing about it. Even on that reading the answer to the question stays No. That gap comes from the tester never trying the setting, not from the discarded design, and once you know that only two designs exist the gap is closed. A reader might also say the discarded design shows that behaviour at the untried setting varies among controllers in general. That is true, but it does not reach controllers that pass, which is what Ivo claims.

**Fix needed.** None substantive. Optional tightening: in the failure clause, write "its lamp stayed dark with A on and B off". That makes plain that the design failed at a tested setting, not at the untried one.
