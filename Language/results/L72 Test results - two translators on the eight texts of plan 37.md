# L72 Test results - two translators on the eight texts of plan 37

Plan: "L72 Test plan - two translators on the eight texts of plan 37.md", frozen before the bundle was sent; not edited since. Worker: Astra Ultra, fresh, no repository. Return: "L72_Astra_Ultra_Return.zip", 117 files, kept whole as "L72 Return - Astra Ultra". My reruns and the sameness outputs are in "L72 Reruns by the orchestrator". The earlier translator is me, on 20 September (log 37), ledgers `ledger_T05B` to `ledger_T11D` in rig 1.

## Checks before reading (plan step 1 and 2)
- Manifest: 116 entries, every hash matches, nothing on disk outside it but the manifest itself. The return names the input zip by hash; it is the zip I sent (93606b71...).
- Source identity: the eight texts byte for byte the ones sent; the corpus questions unchanged (the return checked this too).
- Runtime: SWI-Prolog 9.0.4, s(CASP) 1.1.4, the same as here; the driver, the checker rules and the consequences program byte-identical to the repository's; smoke run on ledger A matches the expected report.
- Reruns here: all eight checker reports and all eight consequences outputs identical to the returned ones once timing lines are set aside; no stderr.
- Translation order: the sequence receipt shows the eight completed in the required order, one to two minutes apart, each frozen by hash before the next; no correction afterwards.
- E7 (the worker): met. One zip, everything the handoff listed, a draft with no verdict on the texts, no word about records or repositories, no sign of the earlier ledgers.

## The two sets of ledgers, side by side
| Text | Mine (Sept 20) | Astra Ultra | Ultra's lines that are Thing lines ("X is an X; response to a press not stated") |
| --- | ---: | ---: | ---: |
| T05-B | 2 | 5 | 3 |
| T05-D | 1 | 4 | 3 |
| T07-B | 3 | 8 | 5 |
| T07-D | 2 | 3 | 1 |
| T10-B | 3 | 8 | 4 |
| T10-D | 3 | 6 | 3 |
| T11-B | 4 | 10 | 4 |
| T11-D | 3 | 6 | 2 |
| total | 21 | 50 | 25 |

Half of Astra Ultra's lines are Thing lines, kind 1 of file 38 ("NAME is a KIND; it answers a press as one of the six response classes"), one per named thing, with the response "not stated". I wrote none. File 38 allows them and does not say whether every named thing needs one; the six example translations in the bundle (the L62 return) write them, and Astra Ultra took the form from there. Set them aside and the counts are 2, 1, 3, 2, 4, 3, 6, 4 against my 2, 1, 3, 2, 3, 3, 4, 3.

## The sameness program, then the hand
The program (wording, not meaning) found little: 4 "both" lines in 21, 1 "same content, different standing", 2 "near", the rest one side only. The reason is form, not content: Astra Ultra writes "folding: ada folded note; direction not stated" where I wrote "Ada folded the note", and the Thing lines match nothing. Read by hand, every one of my 21 lines has a line of the same content on Astra Ultra's side (the hand pairing is listed at the end). Astra Ultra has, beyond the Thing lines, four lines with no counterpart of mine: T10-B "account gives no reason for letter's dryness" (my ledger has nothing for sentence 3, neither a line nor a bin entry: my lapse, see below); T11-B "visitor returned" GIVEN in the actual ledger (it read sentence 2's "the visitor return" as taking the return for granted; I left the return inside the inspector's conclusion and the denied BECAUSE); T11-D splits my one BECAUSE line into a happening "lamp drew visitor back" and "return BECAUSE drawing" (same content, two lines).

**Where the two translators part: attribution.** On three texts Astra Ultra put the reported content into a told world and sent the attribution to the bin: "Nora described ..." (T07-D, world nora_description), "The account says ..." (T10-D, world account_world), "the inspector's reason for concluding ..." (T11-B, world inspector_world). I wrote those as actual lines (CLAIMED by Nora; GIVEN and CLAIMED; the inspector's conclusion as a line with SINCE). File 39's translator task says, in so many words: "Who believes, wants or concludes what. Send the attribution to the bin, and write the content as TOLD in that person's world." Astra Ultra followed 39; my September 20 ledgers did not. Every standing difference between the two sets comes from this one rule, plus the T10-B plan line, which I wrote with no standing at all.

## The expectations, marked
| | Expected | Found | Mark |
| --- | --- | --- | --- |
| E1 shared content | at least one matched line on every text; at least half of my lines matched | by program: 4 of 21 "both", 2 near, three texts with no match at all; by hand: 21 of 21 matched, every text | **met by hand, not by the program**. The program's wording test is defeated by Astra Ultra's line form; the plan foresaw a hand reading of the near bucket, not of the whole |
| E2 standing | differs on at least half the matched lines | differs on 9 of 21 (T07-D: 2; T10-D: 3; T11-B: 3; T10-B: 1); the same on 12 | **not met, narrowly** (43%). Where standing differs it is always the told-world rule of 39 |
| E3 line counts | equal on at least four; no text differs by three or more | equal on none; seven of eight differ by three or more | **not met; the "against" column**. Cause: the Thing lines. With those set aside, equal on four, the rest differ by one or two, Astra Ultra always the longer, which is what the plan expected |
| E4 the bin | the quoted commands binned on both sides; T07-D's "no difference of context or respect" binned; T11-B's inference a SINCE line, not a BECAUSE | commands binned on both sides; T11-B a SINCE line on both sides and BECAUSE denied on both; T07-D's phrase: binned by me, folded by Astra Ultra into the NOT line ("in the same context and respect as line open") and the attribution binned instead | met on three of four; the T07-D phrase differs |
| E5 the checker | the same kind of report on at least six; T10-B and T11-B most likely to differ | the same on five: T05-B, T05-D nothing found; T07-B nothing, told world clean; T10-B CANNOT TELL on the plan; T11-D JUMP. T07-D: both a contradiction, mine actual, Astra Ultra's inside the told world. Different on two: T10-D (mine JUMP; Astra Ultra's BECAUSE sits inside the told world and is never tested); T11-B (mine SINCE with no connecting line; Astra Ultra's SINCE inside the told world, never tested; both report the denied BECAUSE as fine) | **not met by the strict count** (five, or six counting T07-D); not in the "against" column. The two that differ are the two the plan named, but for a reason the plan did not foresee (below) |
| E6 consequences | 0 derived on at least six; never more than 2; no `produced` on T10-D or T11-D | 0 on six; 1 on T07-B and T07-D; no `produced` anywhere | met. But T07-B's one derived fact is a tool fault (below) |
| E7 the worker | clean return | as above | met |
| E8 near pairs | at most three, each a wording difference with the same meaning | two: T07-B "the door is open" / "door stood open" (same meaning); T07-D "the same door at the same moment is NOT open" / "door is open at stage described_moment", a line beside its own negation, scored 0.50 | **the "against" column on one pair**: the near score ignores NOT |

Four met (E1 by hand, E4 mostly, E6, E7); four not met (E2 narrowly, E3 and E8 in the "against" column, E5 by one).

## What the run showed that the plan did not ask
1. **Under 39, a reported argument is never checked.** 39's rule sends attributed content into a told world; patch 12 looks at a told world for contradictions only. So T10-D's "the account says opening the window caused the dryness" and T11-B's "the inspector's reason for concluding" carry a BECAUSE and a SINCE that no query touches. Astra Ultra saw this and parked it ("a coverage limit of the prescribed run, left visible rather than repaired"). The corpus question on T10-D, whether achieved dryness establishes the cause, cannot be answered under 39 as it stands, because the claim to be tested is put where the checker does not look. This is the strongest finding of the test, and it is a finding about the language, not about either translator. It sits beside F09 (what-ifs) as a second case of a standing that hides a claim from the checker. Held for the owner's word, like F09 and F15.
2. **The consequences program ignores worlds.** `tools/consequences.py` calls the driver's `run_query` without setting the driver's list of lines outside the world looked at, so told and supposed lines pool with the actual ledger. On T07-B, mine and Astra Ultra's alike, it derives a contradiction between the story's open door and the room's shut one, which the checker rightly does not report. Astra Ultra found this by reading the program; I confirmed it on my own T07-B ledger. My fault, in a tool written at L65 on a ledger with no worlds. Lesson L7. The fix is mine to make (a tool, not a rig), as a new version beside the old, after the owner has seen this.
3. **The checker's wording for a contradiction inside a told world is wrong.** Patch 12 prints "UNDER THE SUPPOSITION ... THE SUPPOSITION UNDOES ITSELF" for a told world with a contradiction, as T07-D shows, although its clean-world wording says "INSIDE ... a told world". A wording fault in the rig, a one-line patch; held with the other rig changes for the owner's word.
4. **The sameness near score ignores negation.** A line and its NOT scored 0.50. Lesson L8. Fix in the tool: NOT on one side and not the other breaks a near pair, or is printed as "opposite".
5. **Thing lines are a convention 38 leaves open**, and the bundle's examples decided it. A translator who follows the examples writes one per named thing; one who follows 38 alone need not. The count of lines said, which the gauge and L64's thresholds use, moves by a factor of two on this convention alone. To be decided in 38 or 39, not left to the examples.
6. **My own lapse.** My T10-B ledger of September 20 has no line and no bin entry for sentence 3 ("The account gives no reason for its dryness"). The sentence was dropped without a trace. Astra Ultra wrote it as a line. Log 37's gauge for T10-B, "0 of 3 sentences to the bin", was therefore wrong on that text.
7. **Astra Ultra's draft parked four things and proposed nothing.** All four (the world pooling, the untested told-world claims, the supposition wording, the unnoted filled-in endpoint in T11-D's jump) check out against the code and the outputs. It proposed no repair, no threshold and no verdict, as the brief asked.

## What this test does not show
Which translation is right; two translators agreeing may both be wrong. The comparison is not with the answer keys of plan 37. Astra Ultra's line form copies the bundle's examples (the L62 return, by the same harness), so the two "independent" translators are not independent of the examples. Rig 2 was not run.

## Held for the owner's word
- Whether BECAUSE and SINCE inside a told world are to be tested (finding 1), and how: inside the world alone, as contradictions are, is the obvious form.
- The one-line wording patch to the checker (finding 3).
- Whether every named thing gets a Thing line (finding 5).
- The two tool fixes (findings 2 and 4) I propose to make next, as new versions beside the old.

## The hand pairing (my line, Astra Ultra's line; standing noted where it differs)
T05-B: 1 folded / folding; 2 gate NOT open / gate remained shut. T05-D: 1 / opening. T07-B: 1 told a story / telling; 2 told, door open / storyopen (told); 3 door NOT open / actualshut. T07-D: 1 (CLAIMED by Nora) / open (TOLD); 2 (CLAIMED by Nora) / notopen (TOLD). T10-B: 1 / opening; 2 PLAN (no standing) / plan (CLAIMED); 3 NOT wet / dry. T10-D: 1 (GIVEN) / opening (TOLD); 2 (GIVEN) / dry (TOLD); 3 BECAUSE (CLAIMED) / because (TOLD). T11-B: 1 / burning; 2 inspector's conclusion (no standing) / toldreturn (TOLD); 3 SINCE (no standing) / since (TOLD); 4 NOT BECAUSE (no standing) / notbecause (CLAIMED). T11-D: 1 / burning; 2 / return; 3 BECAUSE / drawing + because.

## Traps
- Reading the program's four matches as the result. The program measures wording; the hand pairing above is the result, and it is mine, so it can be checked line by line against the two ledgers.
- Taking Astra Ultra's told worlds as over-reading. They are what 39 says to do.
