# S103 Round 1 — tabulation of the replies, before any ruling

*Written on 27 September 2026 by a fresh Opus 5.5 subagent that built nothing of this round and had read no reply before this task, under rule 4 of `results/S103 Round 1 - how the replies will be read, written before sending.md` (the reading rule, read first; unchanged from HEAD when this was written). It tabulates; it rules on nothing. No sentence of the text is kept, changed or dropped here, and no closing line settles anything (rules 3 and 4; decision S28). This file obeys decision S23 except where it quotes a reply or the owner.*

**Where this file stands.** The orchestrator's task named this path, `results/S103 Round 1 - reading/tabulation.md`. The reading rule, rule 4, names `results/S103 Round 1 - tabulation of the replies, before any ruling.md`. The task's path was used; no second copy was written. The orchestrator may move or copy it.

## What was read, and what was not

- **The text under review:** `tests/99 The semantics, standing alone.md`, md5 74f4a4c7619345747f4fa976ddac9548 (checked before reading). Not written to.
- **The briefs:** the three part briefs in `tests/`, md5 9c46307c5dc62368327e8a34c184a83d, 387f826f93ba0922458007feefc6bd61 and 44ef4fbdb179963c3e76fcdaf60ecf27, as the reading rule's table gives them.
- **The replies:** the six `.response.txt` files only. No `.reasoning.txt` file was opened. The three Mimo `.request.json` files were opened by program only to hash their user message against the receipts (the contents were not printed or read).
- **The runs were over** (rule 1): the Mimo log ends `loop ended 2026-09-27T14:14:58Z` and the GLM log ends `s103_glm_loop: every pass ended; accepted 3 of 3 parts` then `loop ended 2026-09-27T12:52:50Z`; neither process in the pid files was running.

## Receipts: every reply counts (rule 2)

| tag | part | pass / attempts | what the receipt records | last non-blank line of the reply | response sha256 (receipt; the file hashes the same) | brief the reply answers |
|---|---|---|---|---|---|---|
| s103_vary_mimo_1 | 1 (C01–C12) | pass 1, 1 attempt | `finish_reason` "stop", `saw_done` `true`, attempt 1 `accepted` `true`, status 200 | END OF REPORT | 05225511e381c2ab591a612e1af471b37e1d8c9eeb9ae0c4bedb5c2687858495 | user message sha256 7dfae3b516e92f7bfd4da03ad9447733a299f00014edec25bc58f8a48b9f2c72, the sha256 of the part 1 brief |
| s103_vary_mimo_2 | 2 (C13–C20) | pass 1, 1 attempt | `finish_reason` "stop", `saw_done` `true`, attempt 1 `accepted` `true`, status 200 | END OF REPORT | e574a8889ed6fb73296004c7a261afa21626cbe09442c7d0ec94cd71b2186680 | user message sha256 7e83cb09a84d61fbbc7e77375622944a67d1980a57128c07a77969c6a2418d07, the sha256 of the part 2 brief |
| s103_vary_mimo_3 | 3 (C21–C29) | pass 1, 1 attempt | `finish_reason` "stop", `saw_done` `true`, attempt 1 `accepted` `true`, status 200 | END OF REPORT | d54a8c9987e21da743a8844a6c2ffae59050888c06777c7c2e515a1b9ad836e6 | user message sha256 01de8ba796dee52a82f455ea2ce96b3ec894ef1518ac34e41be416b67f802f58, the sha256 of the part 3 brief |
| s103_vary_glm_1 | 1 (C01–C12) | pass 1, 1 attempt, 0 connection failures | `accepted` `true` ("the reply's last non-blank line carries END OF REPORT"), model reported glm-5.3 | END OF REPORT | cdf265cd504ad067a15818ab3505e650e2ec6d8d9f3a9d0c9428e8ab9b446ab0 | `brief_md5` 9c46307c5dc62368327e8a34c184a83d |
| s103_vary_glm_2 | 2 (C13–C20) | pass 1, 1 attempt, 0 connection failures | `accepted` `true` ("the reply's last non-blank line carries END OF REPORT"), model reported glm-5.3 | END OF REPORT | 996f8b6cca59843ac3e75a1af1eac7a6a3b623e7caffcc5a32b60c1c0db72612 | `brief_md5` 387f826f93ba0922458007feefc6bd61 |
| s103_vary_glm_3 | 3 (C21–C29) | pass 1, 1 attempt, 0 connection failures | `accepted` `true` ("the reply's last non-blank line carries END OF REPORT"), model reported glm-5.3 | END OF REPORT | 332e2abb875338d8e37c3e3f00300078b2c656a56e52a058abe0a3b2b3c90fd5 | `brief_md5` 44ef4fbdb179963c3e76fcdaf60ecf27 |

Every one of the 29 candidates was examined by both readers; no candidate is "not examined" (rule 6). Each reply has one section per candidate, headed `Cnn · L<n>`, in the order of the brief, each with a closing line in one of the three forms. Where a Mimo closing line is wrapped in backticks, the backticks are the reply's and are kept.

## How the rows are made

- **Closing lines** are copied byte for byte by program from the replies, with their line numbers.
- **Wordings** (every rival, every variation and every repair a reader wrote out) are copied byte for byte by program from the replies, with their reply line numbers; the label after each line number is this file's short record of what the reader said the wording does (offered as working, said to break a named line, or offered as a repair). Variations a reader described without writing them out are listed as described.
- **Points** are a digest, one or two sentences each, of every point a reader made on the candidate, under steps 1 to 3; they say what the reader claims, not whether it holds.
- **Quotations**: each quotation a reader relies on was searched for in file 99 by program (LaTeX delimiters, bold marks and quotation-mark styles set aside; a quotation with "…" searched piece by piece) and, for the owner's words, in section 2 of the brief. "Found at L<n>" gives the line found; where it differs from the line the reader cited, both are given. Single words and a reader's own phrases in quotation marks are not listed as quotations. No quotation of any reader was not found in file 99 or the brief; one was found on a line other than the one cited (C21, GLM: "it fails (F1)" cited as L267, found at L269).
- **To a checker** marks the candidate under rule 5 (either reader closes VARIES or FAILS; a point of either shows a defect; or it is in doubt whether a point does) and names rule 7 where the readers differ. A candidate both readers close HOLDS with no point showing a defect is marked under rule 6.
- **Parked (S34)**: no point of either reader proposes anything about what hard to vary covers. One GLM point (C29) mentions S34 only to avoid a word that it says would touch the parked question; that is recorded there.

## Candidates held under both readers' attempts (rule 6)

Both readers closed HOLDS, and no point of either shows a defect, on **C06, C14, C16 and C17**. They go to no checker and are to be recorded "held under both readers' attempts; not thereby final". On C14, Mimo's step 3 raised, and itself answered, a question about L397 ("the sentence claims event-status only"), and GLM's fault search raised, and itself answered, a misreading of "Its formulation"; neither names a defect. The orchestrator may read those two remarks otherwise and send C14 to a checker.

**C18** was closed HOLDS by both readers but is marked for a checker under rule 5's clause on doubt: Mimo's step 3 records that the text forces a transport's faithfulness to be the component and global conditions (L189), while "Question fidelity" heads (A) (L247) and the sentence's uses attribute (A) to a violation, and GLM reads the sentence's "fidelity" as including (A). Neither reader calls this a failure; whether it shows one is in doubt.

## Candidates for a checker

C01, C02, C03, C04, C05, C07, C08, C09, C10, C11, C12, C13, C15, C18, C19, C20, C21, C22, C23, C24, C25, C26, C27, C28 and C29: twenty-five candidates, each to a checker of its own (rule 5). Where the readers differ, the checker states each side's argument and rules between them (rule 7). On C27 both readers close FAILS on the same fault with different repair wordings, and Mimo's own section gives two further wordings of its repair (see C27).

## The candidates, one by one

## Part 1: C01–C12 (Part 0 and Part II)

### C01 · L27 · Part 0 — Read this first; What this document does not claim

**The sentence** (as the brief gives it; found word for word in file 99 at L27):

> It defines the classes.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 26): VARIES

```
`C01: VARIES — It does define the classes.`
```

- GLM (`s103_vary_glm_1.response.txt`, line 27): HOLDS

```
C01: HOLDS — every rival either blurred the define/decide contrast or downgraded the classes from defined (L528) to described.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ, HOLDS against VARIES (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 3–27)

*Points (digest):*

- Rival: an emphatic 'It does define the classes.' keeps the boundary the line draws (defines classes, declines membership of actual systems) and points where L528 points; nothing quotes the sentence. A longer rival adding 'and their membership conditions' also breaks nothing Mimo can name.
- Break: 'It defines the class.' breaks the plural of its own line and L528's five classes; 'It decides the classes' membership.' breaks the line's first sentence and L632.
- Fault check: the preceding words 'the classes defined' already attribute definition to the document; the sentence's work is the explicit contrast, 'a role, not new content'. A reader may take it to cover actual systems; L632 excludes that. No failure claimed.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 7, rival offered as working (the closing line's rival):

```
It does define the classes.
```

- reply line 11, second rival, said to break nothing:

```
It defines the classes and their membership conditions.
```

- reply line 16, variation said to break the plural and L528:

```
It defines the class.
```

- reply line 20, variation said to break L27's first sentence and L632:

```
It decides the classes' membership.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L528 "**Membership.** The base class: interpretations supplying these data with typing as declared…" — found at L528
- (its own line) "belongs to the classes defined", "the classes defined" — found at L27
- L632 "It is not a claim that any actual infant, animal, or program instantiates it." — found at L632

#### GLM (`s103_vary_glm_1.response.txt`, lines 3–28)

*Points (digest):*

- Rival 'It fixes what the classes are.': 'fixes' neighbours 'decides', the act L27's first sentence disowns; the whole work of the sentence is the contrast decide/define, which the verb re-blurs.
- Rival 'It says what the classes are.': weaker; a class can be said by description, but the document's mode is definition (the heading at L28–L30 names 'what is defined'; L528 states membership as definitional data).
- Rival 'It defines them.': drops the deliberate echo of 'the classes defined' that makes the affirmation land against the denial.
- Faults sought: none; the affirmation is backed by L528 and L632; no circularity.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 8, rival said to blur the define/decide contrast:

```
It fixes what the classes are.
```

- reply line 14, rival said to downgrade defined to described:

```
It says what the classes are.
```

- reply line 20, rival said to drop the echo:

```
It defines them.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L28–L30 "what is defined" — found at L29 (the heading)
- L528 "The base class: interpretations supplying these data with typing as declared" — found at L528
- (its own line) "the classes defined" — found at L27
- L632 "It is not a claim that any actual infant, animal, or program instantiates it." — found at L632

### C02 · L41 · Part 0 — Read this first; Grievances, anticipated; 3. "If correspondences are selected, you have made fidelity a matter of survival."

**The sentence** (as the brief gives it; found word for word in file 99 at L41):

> Survival is how the transport got there; fidelity is what it is.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 48): VARIES

```
`C02: VARIES — Survival is how the transport got there; fidelity is what the transport is on the contract.`
```

- GLM (`s103_vary_glm_1.response.txt`, line 47): HOLDS

```
C02: HOLDS — rivals lost the grip on the grievance's word "survival" or miscast survival against L193/L195; the compression is licensed in context.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 28–49)

*Points (digest):*

- Rival: '…fidelity is what the transport is on the contract.' keeps the split between provenance and property and carries the index L189 requires, since (F1), (F2) and (A) range over (a,b)∈C; breaks nothing Mimo can name.
- Break: 'Survival is fidelity on the history.' breaks L195 ('fidelity on H without membership in T is not survival'); 'Fidelity is what survived.' breaks L572 and L67.
- Fault check: 'it' in 'fidelity is what it is' can be read as the transport (forced by the parallel) or as 'fidelity', which would make the clause do no work; read as the transport, the clause alone invites an absolute reading of fidelity, which the preceding sentence and L189 exclude. 'Readerly risk, not a forced failure.'

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 32, rival offered as working (the closing line's rival):

```
Survival is how the transport got there; fidelity is what the transport is on the contract.
```

- reply line 38, variation said to break L195:

```
Survival is fidelity on the history.
```

- reply line 42, variation said to break L572 and L67:

```
Fidelity is what survived.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L189 "A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V." — found at L189
- L195 "fidelity on \(H\) without membership in \(\mathcal T\) is not survival" — found at L195
- L572 "survival on \(H\) does not distinguish \(t\) from \(t'\) there" — found at L572
- L67 "Whether a transport is faithful on a contract is independent of whether anyone tentatively accepts it." — found at L67
- (the candidate) "fidelity is what it is" — found at L41

#### GLM (`s103_vary_glm_1.response.txt`, lines 29–48)

*Points (digest):*

- Rival 'Selection is how the transport got there; …' loses the grievance's own word ('survival', L41) and misassigns: selection is the package of L195, survival the condition the grievance names and Argument 3 isolates (L572).
- Rival 'Survival concerns provenance; fidelity concerns the transport.' miscasts survival (provenance classifies transports, L193) and 'concerns' is too weak for fidelity as a property of the transport on its contract (L189).
- Faults sought: the colloquial fatalist reading of 'fidelity is what it is' is blocked by the preceding sentence; the compression 'survival' for selection by survival is licensed by 'Selection produces a transport'. No fault stands.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 34, rival said to lose the grievance's word:

```
Selection is how the transport got there; fidelity is what it is.
```

- reply line 40, rival said to miscast survival (L193) and to be too weak (L189):

```
Survival concerns provenance; fidelity concerns the transport.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L41 "you have made fidelity a matter of **survival**" — found at L41 (the bold on 'survival' is the reader's)
- L572 "survival on \(H\) does not distinguish \(t\) from \(t'\) there" — found at L572
- L193 "has exactly one of three provenances" — found at L193
- L189 "A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V" — found at L189
- L41 "turns on the transport and the target alone, not on whether it survived", "Selection produces a transport" — found at L41
- "it is what it is", "selection by survival" — the reader's own words, not offered as quotations; not in file 99

### C03 · L47 · Part 0 — Read this first; Grievances, anticipated; 6. "You have replaced explanation with evolution."

**The sentence** (as the brief gives it; found word for word in file 99 at L47):

> Construction is a separate provenance with a separate trace, and every creative attribution requires it.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 74): VARIES

```
`C03: VARIES — Constructed correspondence is a separate provenance with a separate trace, and every creative attribution requires construction.`
```

- GLM (`s103_vary_glm_1.response.txt`, line 73): HOLDS

```
C03: HOLDS — rivals broke L199/L13 (declared transports), the attribution unit (G) at L422/L528, or the provenance classification at L193.
```

**To a checker:** yes: Mimo VARIES (rule 5); Mimo's fault check alleges a looseness ('is a separate provenance' against L193) that GLM's third rival contests; the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 50–75)

*Points (digest):*

- Rival: 'Constructed correspondence is … and every creative attribution requires construction.' L13 puts provenance on correspondence, L193–L201 on transports; (G) (L421–L422) puts Build in every creative attribution and L425 lets the content be 'an organization, a transport, or a contract', so what every attribution requires is construction, not a transport with that provenance. Breaks nothing Mimo can name.
- Break: 'Construction is a kind of selection' breaks L411; 'A constructed transport is a separate provenance …' breaks L425 (an attribution on a contract has no transport); '… requires selection' breaks (G), which has no selection term.
- Fault check (alleges a defect of wording): 'it' can be read as 'a separate provenance' or as 'Construction'; the provenance reading would demand a transport of every attribution and clash with L425, though the text forces the Build reading (L405, L421–L422). 'Construction is a separate provenance' is loose against L193, where the provenance belongs to a transport; L13 licenses the shorthand.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 54, rival offered as working (the closing line's rival):

```
Constructed correspondence is a separate provenance with a separate trace, and every creative attribution requires construction.
```

- reply line 60, variation said to break L411:

```
Construction is a kind of selection, and every creative attribution requires it.
```

- reply line 64, variation said to break L425:

```
A constructed transport is a separate provenance with a separate trace, and every creative attribution requires it.
```

- reply line 68, variation said to break (G):

```
Construction is a separate provenance with a separate trace, and every creative attribution requires selection.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L13 "A correspondence can be *selected*… or *constructed*… or merely *declared*" — found at L13
- L425 "an organization, a transport, or a contract" — found at L425
- L411 "Construction is not selection. A selected transport has no represented target in its history; a constructed one does." — found at L411
- (the candidate) "Construction is a separate provenance" — found at L47

#### GLM (`s103_vary_glm_1.response.txt`, lines 49–74)

*Points (digest):*

- Rival '… every explanation requires it.' breaks L199 and L13: declared transports serve explanations; only claims about creativity cannot rest on declaration.
- Rival '… creativity requires it.' overclaims: 'creative attribution' is the theory's unit ((G) at L422, the creative-episode class at L528, L429).
- Rival 'Construction has a separate provenance …' is a category error: construction is one of the three provenances (L193, L197), it does not have one.
- Faults sought: none; 'separate trace' is backed by L405 and L411; the requirement matches (G).

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 54, rival said to break L199/L13:

```
Construction is a separate provenance with a separate trace, and every explanation requires it.
```

- reply line 60, rival said to overclaim against (G), L528, L429:

```
Construction is a separate provenance with a separate trace, and creativity requires it.
```

- reply line 66, rival said to be a category error (L193, L197):

```
Construction has a separate provenance with a separate trace, and every creative attribution requires it.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L199 "**Declared.** Neither of the above. The transport is entered into the model by its author." — found at L199
- L13 "Declaration is used only as a modelling convenience, and a claim about creativity cannot depend on it" — found at L13
- L528 "base interpretations with an instance of (G)" — found at L528
- L429 (excerpt) "an instance of (G) connected to its inquiry" — found at L429
- L197 "Write \(\operatorname{Con}(t;h,e)\)." — found at L197
- L405 "A construction trace identifies the controlled processes, the incoming carriers, the bindings constructed, and the resulting representation." — found at L405
- L411 "the traces differ" — found at L411

### C04 · L113 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 at L113):

> Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 96): VARIES

```
`C04: VARIES — Take an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).`
```

- GLM (`s103_vary_glm_1.response.txt`, line 89): VARIES

```
C04: VARIES — Let \(D\) be an organization and \(C\subseteq A\times B\) a contract (Part III).
```

**To a checker:** yes: both readers close VARIES, with different rivals (rules 5 and 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 76–97)

*Points (digest):*

- Rival 'Take an organization D and a contract C⊆A×B (Part III).' keeps D as an (O)-organization, the typing (K) needs, the pointer to Part III (L141) and D, C as the section's fixed parameters (L526). Breaks nothing.
- Break: 'a set C of changes' breaks L141 ('edit–boundary pairs') and (K)'s pairs; 'C⊆A' breaks L91's boundaries in L_j(a,b) and (K).
- Point (alleges part of the sentence does no work): dropping the typing altogether breaks nothing, since L141 supplies it through the pointer; 'the typing clause is the sentence's only strict content'.
- Fault check: 'Fix' is register; L119 later varies C, so the sentence fixes D, C for the definitions that follow only. Nothing fails.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 80, rival offered as working (the closing line's rival):

```
Take an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).
```

- reply line 86, variation said to break L141 and (K):

```
Fix an organization \(D\) and a set \(C\) of changes (Part III).
```

- reply line 90, variation said to break L91 and (K):

```
Fix an organization \(D\) and a contract \(C\subseteq A\) (Part III).
```

- described in prose, no wording written out: Dropping the typing altogether (no wording written out): said to break nothing, since L141 supplies it through the pointer.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L141 "The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over" — found at L141
- L526 "(K) depends on (O) and a contract" — found at L526
- L141 "edit–boundary pairs" — found at L141
- L119 "two components of one kind on \(C\) may separate on a finer contract" — found at L119

#### GLM (`s103_vary_glm_1.response.txt`, lines 75–90)

*Points (digest):*

- Rival 'Let D be an organization and C⊆A×B a contract (Part III).': nothing downstream depends on the imperative 'Fix'; the relativity claims of L119 hold under either wording; both hold D and C as parameters.
- Break: dropping '(Part III)' would orphan the contract's definition site (L141); replacing ⊆ with ⊂ would contradict L141 and exclude the full contract.
- Faults sought: the forward reference is standing practice (L119 cites Parts IV and V); the quantification is well-founded (A and B belong to D's data, L91).

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 80, rival offered as working (the closing line's rival):

```
Let \(D\) be an organization and \(C\subseteq A\times B\) a contract (Part III).
```

- described in prose, no wording written out: Dropping the parenthetical "(Part III)" (not written out): said to orphan L141.
- described in prose, no wording written out: Replacing "\(\subseteq\)" with "\(\subset\)" (not written out): said to contradict L141 and exclude the full contract.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L119 "Kinds are therefore relative to the contract; a coarser contract identifies more components" — found at L119
- L141 "The **contract** \(C\subseteq A\times B\) is the set of admitted edit–boundary pairs the claim ranges over" — found at L141

### C05 · L113 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 at L113):

> The **signature** of component \(j\) on \(C\) is

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 118): VARIES

```
`C05: VARIES — For a component \(j\) of \(D\), its **signature** on \(C\) is`
```

- GLM (`s103_vary_glm_1.response.txt`, line 109): HOLDS

```
C05: HOLDS — rivals departed from the definitional display idiom shared with L97 and L141, or suggested a supply relation the text reserves for the interpretation's data (L91).
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 98–119)

*Points (digest):*

- Rival 'For a component j of D, its **signature** on C is' with (K) unchanged keeps the bold term, the component parameter and the contract index L119 needs. Breaks nothing.
- Break: dropping 'on C' breaks L119 and L526 and no longer matches the subscript in (K); '**kind** … on C' breaks L119 (a kind is a class built from signatures) and L558.
- Fault check: the lead-in carries only a term and two parameters. Nothing fails.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 102, rival offered as working (the closing line's rival):

```
For a component \(j\) of \(D\), its **signature** on \(C\) is
```

- reply line 108, variation said to break L119, L526 and (K)'s subscript:

```
The **signature** of component \(j\) is
```

- reply line 112, variation said to break L119 and L558:

```
The **kind** of component \(j\) on \(C\) is
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L119 "Kinds are therefore relative to the contract" — found at L119
- L558 "The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case." — found at L558

#### GLM (`s103_vary_glm_1.response.txt`, lines 91–110)

*Points (digest):*

- Rivals '… is given by' and 'Define the … as' depart from the display convention by which the text marks a definition by form alone ('The compatible valuations are', L97; 'The answer profile is', L141); varying this one display breaks the uniform convention.
- 'Is given by' also suggests a supplier, which the text reserves for the interpretation's data (L91, 'the interpretation supplies').
- Faults sought: none; 'on C' is load-bearing and is the idiom of L554 and L119.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 96, rival said to depart from the display idiom and suggest a supplier:

```
The **signature** of component \(j\) on \(C\) is given by
```

- reply line 102, rival said to depart from the display idiom:

```
Define the **signature** of component \(j\) on \(C\) as
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L97 "The compatible valuations are" — found at L97
- L141 "The answer profile is" — found at L141
- L91 "the interpretation supplies" — found at L91
- L554 "a signature on \(\tau[C]\)" — found at L554

### C06 · L115–L117 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 as L115–L117):

> \[
> \operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K}
> \]

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 150): HOLDS

```
`C06: HOLDS — each variation above loses a named clause of L556, L119 or L57.`
```

- GLM (`s103_vary_glm_1.response.txt`, line 135): HOLDS

```
C06: HOLDS — the graph form is used verbatim at L556 and acted on by L119; function-form, coordinate-free, and baseline rivals each broke a named use.
```

**To a checker:** no: both readers close HOLDS and no point of either shows a defect (rule 6).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 120–151)

*Points (digest):*

- Variation (a) sig=L_j|_C breaks L556 (a restriction has no third coordinate for '(F1) equates the third coordinates pointwise').
- Variation (b) dropping (a,b) breaks the same pointwise clause and L57, which needs each relation tied to its edit.
- Variation (c) putting the footprint V_j inside breaks L119's footprint bijection (coincidence would demand literal port-set equality).
- Variation (d) Sol_D(a,b)|V_j as third coordinate breaks L556's second display and (F1).
- Fault check: the triple is typed by L94; its data are exactly (O) and a contract (L526); L245 rests on it. No fault.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 124, variation (a), said to break L556:

```
\[
\operatorname{sig}_C(j)=L_j|_C. \tag{K}
\]
```

- reply line 130, variation (b), said to break L556 and L57:

```
\[
\operatorname{sig}_C(j)=\{L_j(a,b):(a,b)\in C\}. \tag{K}
\]
```

- reply line 136, variation (c), said to break L119:

```
\[
\operatorname{sig}_C(j)=(V_j,\{(a,b,L_j(a,b)):(a,b)\in C\}). \tag{K}
\]
```

- reply line 142, variation (d), said to break L556 and (F1):

```
\[
\operatorname{sig}_C(j)=\{(a,b,\operatorname{Sol}_D(a,b)|_{V_j}):(a,b)\in C\}. \tag{K}
\]
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L556 "By (K), \(\operatorname{sig}_C(\lambda(k))=…\) … (F1) equates the third coordinates pointwise." — found at L556
- L57 "a rule's application changes when the rule is edited and not when the world is intervened on; a cause's assignment changes under intervention" — found at L57
- L119 "there is a bijection of their footprints under which … coincide" — found at L119
- L94 "\(L_j(a,b)\subseteq\prod_{v\in V_j}X_v\)" — found at L94
- L245 "By (K), no component of \(E\) whose signature on \(C\) differs from its counterpart's meets (F1)" — found at L245

#### GLM (`s103_vary_glm_1.response.txt`, lines 111–136)

*Points (digest):*

- Function form breaks L556, which writes the signature in the set-builder form (K) instantiates and argues '(F1) equates the third coordinates pointwise'.
- Dropping the first two coordinates breaks L119's comparison 'read on C through τ and τ′' and L554.
- Baseline profile L_j(1,b_0) destroys the coarseness content of L119.
- Faults sought: the comprehension is well-defined (L91 supplies L_j(a,b) for every pair); L526 records its dependence; no circularity.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 116, function-form variation, said to break L556:

```
\(\operatorname{sig}_C(j):C\to\bigcup_j\{L_j(a,b)\},\quad (a,b)\mapsto L_j(a,b)\)
```

- reply line 122, coordinate-free variation, said to break L119 and L554:

```
\(\operatorname{sig}_C(j)=\{L_j(a,b):(a,b)\in C\}\)
```

- reply line 128, baseline variation, said to break L119:

```
\(\operatorname{sig}_C(j)=L_j(1,b_0)\)
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L556 both displays and "(F1) equates the third coordinates pointwise" — found at L556
- L119 "read on \(C\) through \(\tau\) and \(\tau'\)" — found at L119
- L119 "a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract" — found at L119
- L526 "(K) depends on (O) and a contract" — found at L526

### C07 · L123 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 at L123):

> - a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 176): VARIES

```
`C07: VARIES — - a **causal assignment** has a signature that moves when an edit sets its output port or replaces the component, and that observation edits leave unchanged;`
```

- GLM (`s103_vary_glm_1.response.txt`, line 161): HOLDS

```
C07: HOLDS — polarity and port swaps broke L127, L37, and L103's replacement structure; dropping the replacement clause untied the assignment from the component.
```

**To a checker:** yes: Mimo VARIES (rule 5); Mimo alleges the replacement clause is inert (a part that does no work) while GLM argues it ties the assignment to the component; the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 152–177)

*Points (digest):*

- Rival '… a signature that moves when an edit sets its output port or replaces the component, and that observation edits leave unchanged;' uses L103's and L109's 'an edit that sets'; all three clauses stay. Breaks nothing.
- Break: 'input port' breaks L103 with L109 (a port whose setting moves j's signature is one j assigns, its output) and loses the contrast with C08's measured port; 'variable under observation edits' breaks L109 and L127.
- Fault check (alleges a part that does no work): 'and under replacement of the component' applies to every component, since (K) builds the signature from L_j (L119); dropping it breaks nothing (wording at line 172). But L127 allows descriptions that include general features, and C08, C09 carry the same general clause: 'Inertness, not contradiction.'

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 156, rival offered as working (the closing line's rival):

```
- a **causal assignment** has a signature that moves when an edit sets its output port or replaces the component, and that observation edits leave unchanged;
```

- reply line 162, variation said to break L103 with L109:

```
- a **causal assignment** has a signature that changes under intervention on its input port and under replacement of the component, and is invariant under observation edits;
```

- reply line 166, variation said to break L109 and L127:

```
- a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is variable under observation edits;
```

- reply line 172, variation (replacement clause dropped), said to break nothing:

```
- a **causal assignment** has a signature that changes under intervention on its output port, and is invariant under observation edits;
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L103 "An edit that sets a port replaces the component assigning that port" — found at L103
- L109 "A port is an **output** of component \(j\) when its value is determined by \(L_j\)…" — found at L109
- L109 "an edit that alters the relation reporting it without altering what it reports" — found at L109
- L127 "change only the reading and the part it reports stays as it was" — found at L127
- L119 "A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution" — found at L119
- L127 "These are descriptions of patterns in (K), not additional data." — found at L127

#### GLM (`s103_vary_glm_1.response.txt`, lines 137–162)

*Points (digest):*

- Polarity swap breaks L127's test and 'Which of the two … is fixed by that signature, not by the account's wording', and L37.
- 'input port' misdescribes: an edit setting an input replaces the component assigning that input (L103), not the causal component; breaks the responsiveness L37 makes the cause/correlation difference.
- Dropping the replacement clause: a signature sensitive only positionally (the output-setting edit replaces the occupant, L103) would count as causal while the relation depended on nothing about the component; L127 needs the assignment tied to the component; L57/L103 pair cause with rule in component-sensitivity.
- Faults sought: the first clause might look idle given L103 but it locates the sensitivity at the output port (contrast with L124's measured port) and the pattern obtains only where C contains such pairs (L37). No circularity (observation edits fixed by L109 via the measurement's signature).

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 142, polarity-swap variation, said to break L127 and L37:

```
- a **causal assignment** has a signature that is invariant under intervention on its output port and under replacement of the component, and changes under observation edits;
```

- reply line 148, input-port variation, said to break L103 and L37:

```
- a **causal assignment** has a signature that changes under intervention on its input port and under replacement of the component, and is invariant under observation edits;
```

- reply line 154, replacement clause dropped, said to untie the assignment from the component:

```
- a **causal assignment** has a signature that changes under intervention on its output port and is invariant under observation edits;
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L127 "change only the reading and the part it reports stays as it was; change the part and the reading follows" — found at L127
- L127 "Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording." — found at L127
- L37 "A correlation has no component that responds to an intervention on its supposed input; a cause does." — found at L37
- L103 "An edit that sets a port replaces the component assigning that port" — found at L103
- L103 "A changed rule is a changed component" — found at L103
- L37 "where a separating change exists, fidelity finds it; where none exists, the label asserts a distinction the level does not contain" — found at L37

### C08 · L124 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 at L124):

> - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 198): VARIES

```
`C08: VARIES — - a **measurement** has a signature that interventions on the measured port leave unchanged and edits to the measuring relation change;`
```

- GLM (`s103_vary_glm_1.response.txt`, line 187): HOLDS

```
C08: HOLDS — polarity swap broke L127; tracking idiom broke L109's definitional use; "observation edits" would circle with L109.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 178–199)

*Points (digest):*

- Rival '… a signature that interventions on the measured port leave unchanged and edits to the measuring relation change;' keeps both clauses and both roles, which L109 and L127 need. Breaks nothing.
- Break: swapping the roles breaks L109's clause; swapping the polarities breaks L127 with L119.
- Fault check: L109's 'that is' gloss points forward at this bullet — definitional, not circular. The bullet's second clause, like C07's replacement clause, applies to any component under (K); its discriminating partner is the first (a point that the second clause does not discriminate).

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 182, rival offered as working (the closing line's rival):

```
- a **measurement** has a signature that interventions on the measured port leave unchanged and edits to the measuring relation change;
```

- reply line 188, role-swap variation, said to break L109:

```
- a **measurement** has a signature that interventions on the measuring relation leave unchanged and edits to the measured port change;
```

- reply line 192, polarity-swap variation, said to break L127 with L119:

```
- a **measurement** has a signature variable under interventions on the measured port and invariant under edits to the measuring relation;
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L109 "when the component assigning it has a measurement's signature (below)" — found at L109
- L127 "change the part and the reading follows" — found at L127
- L109 "that is" — found at L109

#### GLM (`s103_vary_glm_1.response.txt`, lines 163–188)

*Points (digest):*

- Polarity swap breaks L127 outright.
- Tracking idiom ('is one whose reading follows …') breaks L109, which needs the measurement's signature statable as an edit-response pattern in (K)'s coordinates.
- Using 'observation edits' creates a circle with L109 (observation is defined by the measurement's signature); the standing wording avoids it with 'measured port' and 'measuring relation'.
- Faults sought: the circularity probed is absent as the line stands; consistent with L109 and L127.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 168, polarity-swap variation, said to break L127:

```
- a **measurement** has a signature variable under interventions on the measured port and invariant under edits to the measuring relation;
```

- reply line 174, tracking-idiom variation, said to break L109:

```
- a **measurement** is one whose reading follows what it reports and changes when its own relation is edited;
```

- reply line 180, 'observation edits' variation, said to circle with L109:

```
- a **measurement** has a signature invariant under observation edits and variable under edits to the measuring relation;
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L127 "change the part and the reading follows", "change only the reading and the part it reports stays as it was." — found at L127
- L109 "when the component assigning it has a measurement's signature (below)" — found at L109
- L127 "descriptions of patterns in (K), not additional data" — found at L127

### C09 · L125 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 at L125):

> - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 220): VARIES

```
`C09: VARIES — - a **rule application** has a signature that interventions on the world leave unchanged and edits to the rule change.`
```

- GLM (`s103_vary_glm_1.response.txt`, line 207): HOLDS

```
C09: HOLDS — rivals lost the world/rule contrast of L57 and L347, or conflated the rule family with the observation notion defined at L109.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ (rule 7); Mimo's fault check also notes that C08 and C09 have the same profile shape under (K).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 200–221)

*Points (digest):*

- Rival '… a signature that interventions on the world leave unchanged and edits to the rule change.' keeps both clauses and matches L347 and L57. Breaks nothing.
- Break: swapping rule and world breaks L57 and L347; 'output port' breaks L347 (the invariant side is Z, the rule's input side) and collapses the rule into C07's pattern.
- Fault check: 'the world' is ordinary language whose formal reading is L347's Z; the word is not pinned. Kept apart from a reader's take: under (K), C08 and C09 have the same profile shape (invariant on the worldly input, variable on the relation), and L121 does not claim the families are distinct. No failure.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 204, rival offered as working (the closing line's rival):

```
- a **rule application** has a signature that interventions on the world leave unchanged and edits to the rule change.
```

- reply line 210, swap variation, said to break L57 and L347:

```
- a **rule application** has a signature that interventions on the rule leave unchanged and edits to the world change.
```

- reply line 214, output-port variation, said to break L347 and collapse into C07:

```
- a **rule application** has a signature invariant under interventions on the output port and variable under edits to the rule.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L347 "Its signature under (K) is invariant under interventions on \(Z\) and variable under edits to \(C_r\)" — found at L347

#### GLM (`s103_vary_glm_1.response.txt`, lines 189–208)

*Points (digest):*

- Dropping the world side breaks L57 (the world/rule contrast is the content) and L347.
- Swapping polarities breaks L57 and L347.
- Substituting 'observation edits' breaks the parallel with L347's Z and imports 'observation', which L109 fixes by the measurement's signature, mixing two families L127 keeps apart.
- Faults sought: none; consistent with L57, L347 and L103.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 194, world side dropped, said to break L57 and L347:

```
- a **rule application** has a signature invariant under interventions and variable under edits to the rule.
```

- reply line 200, 'observation edits' variation, said to break L347 and mix families:

```
- a **rule application** has a signature invariant under observation edits and variable under edits to the rule.
```

- described in prose, no wording written out: Swapping polarities (not written out): said to break L57 and L347.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L57 "a rule's application changes when the rule is edited and not when the world is intervened on" — found at L57
- L347 "invariant under interventions on \(Z\) and variable under edits to \(C_r\)" — found at L347
- L103 "A changed rule is a changed component" — found at L103
- "edit to the rule" — the reader's own phrase for the candidate's 'edits to the rule' (L125)

### C10 · L127 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 at L127):

> These are descriptions of patterns in (K), not additional data.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 242): VARIES

```
`C10: VARIES — These describe patterns in (K); they add no data.`
```

- GLM (`s103_vary_glm_1.response.txt`, line 233): HOLDS

```
C10: HOLDS — "derived" is forbidden (S23), "consequences" overclaims against L558 and L11, "inputs" collides with the defined port notion at L109.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 222–243)

*Points (digest):*

- Rival 'These describe patterns in (K); they add no data.' keeps both halves; 'data' points at L528. Breaks nothing.
- Break: 'These are additional data for (K).' breaks L528 and L558; 'patterns in Sol_D, not in (K)' breaks L119 ('not from the values its ports take in a solution').
- Fault check: 'These' takes in the three bullets; L121 names four ordinary things and the fourth gets its pattern at L347, likewise a description. Nothing fails.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 226, rival offered as working (the closing line's rival):

```
These describe patterns in (K); they add no data.
```

- reply line 232, variation said to break L528 and L558:

```
These are additional data for (K).
```

- reply line 236, variation said to break L119:

```
These are descriptions of patterns in \(\operatorname{Sol}_D\), not in (K).
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L558 "The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case." — found at L558
- L119 "not from the values its ports take in a solution" — found at L119

#### GLM (`s103_vary_glm_1.response.txt`, lines 209–234)

*Points (digest):*

- 'derived from (K)' is on the owner's forbidden list (S23: 'derived, derived from').
- 'consequences of (K)' overclaims formal status: the text's consequences are theorem-styled (L558); GLM says it would put 'causal assignment' "on a par with proved claims", weakening what L11 requires.
- 'not additional inputs' collides with the defined port notion (L109); 'data' is right because membership runs on data supplied (L528).
- Faults sought: none; the sentence keeps the bullets off the membership list, backing L554–L558.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 214, rival said to use a word S23 forbids:

```
These are derived from (K), not additional data.
```

- reply line 220, rival said to overclaim against L558 and L11:

```
These are consequences of (K), not additional data.
```

- reply line 226, rival said to collide with L109:

```
These are descriptions of patterns in (K), not additional inputs.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- S23 "derived, derived from" — found in the owner's words (brief section 2, S23)
- L558 "**Consequence.** A condition 'each component's counterpart must be a component of the same kind' adds nothing to (F1) on any contract." — found at L558 (the reader gives the inner double quotation marks as single ones)
- L11 "a *kind* is nothing over and above how a component responds to the changes that level admits" — found at L11
- L109 "A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly." — found at L109
- L528 "The base class: interpretations supplying these data with typing as declared" — found at L528

### C11 · L127 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 at L127):

> The semantics never asks whether a component "is" a cause.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 264): VARIES

```
`C11: VARIES — The semantics never asks an "is a cause" question of a component.`
```

- GLM (`s103_vary_glm_1.response.txt`, line 253): HOLDS

```
C11: HOLDS — rivals weakened the L11 parallel and its level-relativity, or destroyed the ask/ask structure that carries into the next sentence.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 244–265)

*Points (digest):*

- Rival 'The semantics never asks an "is a cause" question of a component.' uses the quoted phrase of L31 and L600 and keeps 'never' parallel with L11. Breaks nothing.
- Break: dropping the scare quotes breaks L37 and C07's causal family; 'The semantics asks whether a component "is" a cause.' breaks L31 and L600.
- Fault check: read alone, the sentence can be taken to deny that the semantics classifies causes at all; the passage forbids that reading (C07, C12, L57). Reader's risk, not the text's.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 248, rival offered as working (the closing line's rival):

```
The semantics never asks an "is a cause" question of a component.
```

- reply line 254, variation (scare quotes dropped), said to break L37 and C07:

```
The semantics never asks whether a component is a cause.
```

- reply line 258, variation said to break L31 and L600:

```
The semantics asks whether a component "is" a cause.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L31 "…or "is a cause", is taken as an import…" — found at L31
- L600 "There is no residual, undefined predicate meaning "explains," "represents," or "is a cause"…" — found at L600
- L11 "The definition never asks whether a piece of the explanation "is the same kind of thing" as a piece of the world." — found at L11
- L37 "You can, and only this way. A correlation has no component that responds to an intervention on its supposed input; a cause does." — found at L37
- L57 "represents it exactly" — found at L57

#### GLM (`s103_vary_glm_1.response.txt`, lines 235–254)

*Points (digest):*

- 'does not ask' is weaker than 'never': L11's parallel uses 'never' for a standing refusal at every level of detail and for any contract; the echo tells a reader the two denials are one.
- 'contains no predicate "is a cause"' shifts the claim from the question asked to the vocabulary (made at L600 already); the 'asks whether …' framing licenses the reply 'It asks what its signature is.', which the rival orphans.
- Faults sought: none; consistent with L31.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 240, rival said to weaken the L11 parallel:

```
The semantics does not ask whether a component "is" a cause.
```

- reply line 246, rival said to shift the claim and orphan C12:

```
The semantics contains no predicate "is a cause".
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L11 "The definition never asks whether a piece of the explanation 'is the same kind of thing' as a piece of the world" — found at L11 (inner quotation marks given as single)
- L11 "at any level of detail" — found at L11
- L600 (excerpt) "There is no residual, undefined predicate meaning 'explains,' 'represents,' or 'is a cause'" — found at L600 (inner quotation marks given as single)

### C12 · L127 · Part II — Organizations and their changes; Kinds are edit-signatures

**The sentence** (as the brief gives it; found word for word in file 99 at L127):

> It asks what its signature is.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_1.response.txt`, line 286): VARIES

```
`C12: VARIES — It asks what the component's signature on \(C\) is.`
```

- GLM (`s103_vary_glm_1.response.txt`, line 269): VARIES

```
C12: VARIES — It asks what its signature on \(C\) is.
```

**To a checker:** yes: both readers close VARIES, with near-identical rivals ('its' against 'the component's') (rules 5 and 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_1.response.txt`, lines 266–288)

*Points (digest):*

- Rival 'It asks what the component's signature on C is.' does the same work and carries the index L119 makes necessary, fixed at C04. Breaks nothing.
- Break: 'what kind the component is' breaks L558 and L11; 'its signature on the history' breaks L67 and L572's split of survival from behaviour on unseen pairs.
- Fault check: 'It' is the semantics, carried from C11; nothing fails.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 270, rival offered as working (the closing line's rival):

```
It asks what the component's signature on \(C\) is.
```

- reply line 276, variation said to break L558 and L11:

```
It asks what kind the component is.
```

- reply line 280, variation said to break L67 and L572:

```
It asks what its signature on the history is.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L119 "Kinds are therefore relative to the contract" — found at L119
- L11 "a *kind* is nothing over and above how a component responds to the changes that level admits" — found at L11
- L67 "Whether a transport is faithful on a contract is independent of whether anyone tentatively accepts it." — found at L67

#### GLM (`s103_vary_glm_1.response.txt`, lines 255–271)

*Points (digest):*

- Rival 'It asks what its signature on C is.': signatures are contract-relative by (K) and L119, C is in scope from L113; making it explicit states what context already fixes, breaks nothing, and matches the contract-indexed downstream uses (L233–L253, L281, L554–L558).
- Break: 'It asks how it responds to changes.' breaks the tie to (K) and to L11; 'It asks what kind it is.' is circular against the order of definition (L119).
- Faults sought: the implicit contract is fixed by L113 and (K); no vacuity.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 260, rival offered as working (the closing line's rival):

```
It asks what its signature on \(C\) is.
```

- reply line 265, variation said to break the tie to (K) and L11:

```
It asks how it responds to changes.
```

- reply line 265, variation said to be circular against L119:

```
It asks what kind it is.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L119 "Kinds are therefore relative to the contract" — found at L119
- L11 "nothing over and above how a component responds" — found at L11


## Part 2: C13–C20 (Parts III and IV)

### C13 · L161 · Part III — Questions; Scope, and a question that can be in error

**The sentence** (as the brief gives it; found word for word in file 99 at L161):

> A question may fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_2.response.txt`, line 25): VARIES

```
`C13: VARIES — A question may fail to pick out its alleged target, assume a baseline incompatible with its remaining terms, or combine requirements that cannot be met together.`
```

- GLM (`s103_vary_glm_2.response.txt`, line 25): HOLDS

```
C13: HOLDS — every rival either presupposes a target ("wrong about", "miss"), imports physical impossibility against S25/S26 and L159, or collapses the three distinct failure modes into one graded verdict.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ on the same point, whether 'incompatible' should be given its relatum (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_2.response.txt`, lines 1–26)

*Points (digest):*

- Rival: '… assume a baseline incompatible with its remaining terms, or combine requirements that cannot be met together.' keeps the three defect-loci (D, b0, the requirements carried by C, Q, O_p; L141–L147) and 'may'. Giving 'incompatible' its relatum, the question's own terms, matches where the text puts the cases (L141, the baseline in C; L257, Sol_D(1,b0)≠∅); nothing makes a question defective by failing the world (S28, S21). 'Requirements that cannot be met together' keeps 'combine' and L257's case.
- Break: 'must' breaks L159 (an ordinary question is answerable at its scope); 'identify' breaks L151, where 'identify' is a question-type word.
- Step 3: the three stand under 'may', so no exhaustiveness is forced; a reader may take them as the whole catalogue, while L257 words its case differently. 'Alleged' carries the tentativeness S21 requires; dropping it fails.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 6, rival offered as working (the closing line's rival):

```
A question may fail to pick out its alleged target, assume a baseline incompatible with its remaining terms, or combine requirements that cannot be met together.
```

- reply line 14, variation said to break L159:

```
A question must fail to pick out its alleged target, assume an incompatible baseline, or combine incompatible requirements.
```

- reply line 19, variation said to break L151:

```
A question may fail to identify its alleged target, assume an incompatible baseline, or combine incompatible requirements.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L141 "it contains the baseline \((1,b_0)\)" — found at L141
- L257 "\(\operatorname{Sol}_D(1,b_0)\neq\varnothing\)" — found at L257
- S28 "A theory is never settled." — found in the owner's words (S28)
- S21 "'matches the problem' is always tentative and may be wrong." — found in the owner's words (S21; the reader gives the curly quotation marks as straight single ones)
- L257 "admits no candidate that meets non-circular dependence" — found at L257
- L159 "An account at a stated scope answers the question asked at that scope" — found at L159
- L151 "An identification question has a \(\mathcal Q\) that computes a fibre and a \(C\) containing edits to the observed value" — found at L151

#### GLM (`s103_vary_glm_2.response.txt`, lines 7–26)

*Points (digest):*

- Rival (a) 'can be wrong about its target, its baseline, or its requirements' "grades the question by a correctness it does not locate", where the original's three failures are structural; 'wrong about its target' presupposes a target, where 'fail to pick out its alleged target' does not ('alleged' does work: a question about nothing still alleges a target).
- Rival (b) 'aim at a nonexistent target, demand a physically impossible change, or contradict itself' imports into the theory of explanation what S25 and S26 exclude (the boundary L159 keeps), and conflates a single change with requirements, which are pairs in C.
- Fault sought and set aside: 'assume an incompatible baseline' does not say incompatible with what. Not a fault: L257 gives one form, and the line leaves it unlocalized because exposing it is another question (L159: the semantics 'supplies no rule that decides it'); spelling it out would decide by rule what the theory leaves to a question.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 13, rival (a), said to judge the question by a correctness it does not locate and to presuppose a target:

```
A question can be wrong about its target, its baseline, or its requirements.
```

- reply line 19, rival (b), said to import physical impossibility against S25/S26 and L159:

```
A question may aim at a nonexistent target, demand a physically impossible change, or contradict itself.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- S25 "It has nothing to do with explanation" — found in the owner's words (S25)
- S26 "Physical possibility comes in only when something is instantiated or transformed" — found in S26 (the words are Claude's sentence, which the owner quoted and answered "This is correct.")
- L159 "whether anyone could carry a change out, or whether it could come about, is a matter of instantiation and transformation (Part XII)" — found at L159
- L257 "$\operatorname{Sol}_D(1,b_0)\neq\varnothing$" — found at L257
- L159 "the semantics records the restriction and supplies no rule that decides it" — found at L159

### C14 · L161 · Part III — Questions; Scope, and a question that can be in error

**The sentence** (as the brief gives it; found word for word in file 99 at L161):

> Its formulation is still an event.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_2.response.txt`, line 50): HOLDS

```
`C14: HOLDS — every change of "event" breaks L55, L397, L592 or S23, and dropping the concession loses the error case.`
```

- GLM (`s103_vary_glm_2.response.txt`, line 47): HOLDS

```
C14: HOLDS — every rival severs the tie to "event" at L397, L55 and L604, or drops the concession that a defective question still counts.
```

**To a checker:** no: both readers close HOLDS and no point of either shows a defect (rule 6); Mimo's step-3 question and GLM's misreading note are each answered by the reader who raised it (see the note under 'Candidates held under both readers' attempts').

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_2.response.txt`, lines 27–51)

*Points (digest):*

- Break: 'occurrence' breaks L169 and L397 (a carrier alone carries no interpreted claim, and the next sentence's record names a claim); 'input' breaks L592; 'fact' breaks S23 and L397.
- Dropping the concession keeps less than the theory needs: the sentence answers the error case of L161's first sentence, and 'event' must stay for L55. Only re-spellings ('nonetheless', word order) survive, which alter nothing.
- Step 3: no contradiction. A reader might ask whether a formulation whose query has no meaning is an event with an interpreted claim (L397); the sentence claims event-status only.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 32, variation said to break L169 and L397:

```
Its formulation is still an occurrence.
```

- reply line 37, variation said to break L592:

```
Its formulation is still an input.
```

- reply line 42, variation said to break S23 and L397:

```
Its formulation is still a fact.
```

- described in prose, no wording written out: Dropping the concession (no wording written out): said to lose the error case.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L169 "An **occurrence** is a physically located carrier. A **content** is an organization together with its contract-relative commitments." — found at L169
- L397 "A record leaf is a reference to an event with an interpreted claim" — found at L397
- L592 "A semantics that takes questions as inputs cannot represent this; the present one does, by giving contracts provenance." — found at L592
- S23 "Anything that could imply some sort of foundational truth or authority" — found in the owner's words (S23)
- L55 "An assessment is an event with a frozen contract." — found at L55 (also at L161)

#### GLM (`s103_vary_glm_2.response.txt`, lines 27–48)

*Points (digest):*

- Rival (a) 'Asking it still happens.' drops 'event', the text's running term (L397, L55, L604): what merely happens is not yet what a record leaf can reference or an assessment can be; it stops supporting the freezing machinery two sentences later.
- Rival (b) 'occurrence' (L169, L375) leaves open whether a formulation can be a record leaf, since the record and assessment machinery speaks of events (L397, L604), and blurs the carrier/content line of L169.
- Rival (c) deleting 'still': the concession is the point; without it the sentence no longer answers the doubt the previous sentence raises.
- Fault sought: 'Its formulation' could be misread as the formulated text rather than the act; 'event' forces the act reading, so the ambiguity is not live. No circularity.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 33, rival (a), said to sever the tie to 'event':

```
Asking it still happens.
```

- reply line 39, rival (b), said to blur L169 and the record machinery:

```
Its formulation is still an occurrence.
```

- reply line 43, rival (c), 'still' deleted, said to drop the concession:

```
Its formulation is an event.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L397 "A record leaf is a reference to an event with an interpreted claim" — found at L397
- L55 "An assessment is an event with a frozen contract" — found at L55 (also at L161)
- L604 "An assessment event with contract $C$" — found at L604
- L169 "An **occurrence** is a physically located carrier" — found at L169

### C15 · L161 · Part III — Questions; Scope, and a question that can be in error

**The sentence** (as the brief gives it; found word for word in file 99 at L161):

> Exposing the defect is another question with its own contract.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_2.response.txt`, line 81): VARIES

```
`C15: VARIES — Exposing the defect poses another question, with a contract of its own.`
```

- GLM (`s103_vary_glm_2.response.txt`, line 73): HOLDS

```
C15: HOLDS — dropping "its own contract" breaks L151 and the line's final sentence; fixing the target breaks L377; shifting to "alleged" untethers the sentence from the defects just listed and duplicates Part IX.
```

**To a checker:** yes: Mimo VARIES (rule 5), and Mimo alleges that 'is' is loose against L377; the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_2.response.txt`, lines 52–82)

*Points (digest):*

- Rival 'Exposing the defect poses another question, with a contract of its own.' keeps the question machinery (L135–L147), a question distinct from the defective one, a contract of its own (hence its own index, L367, and provenance, L155), and the link to L377's p_δ.
- Point on the identity 'is' (alleges a looseness): 'is' adds a deflation (exposure is nothing over a question), which pairs with L377's 'alleged' and S28; 'poses' settles nothing either, and Mimo could name no line that requires the identity. 'Is' is also loose against L377, which gives the exposing a premise and a connection beyond the question.
- Break: 'the same contract' breaks L367 and C13's loci (the defect can sit in b0, C or Q, so the exposing question cannot inherit them); dropping the contract breaks L367 (no contract, no index); 'an answer to the original question' breaks L161's last sentence.
- Step 3: that exposure settles the defect, the text forces neither wording to say; L377 keeps δ 'alleged'.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 57, rival offered as working (the closing line's rival):

```
Exposing the defect poses another question, with a contract of its own.
```

- reply line 65, variation said to break L367 and C13's loci:

```
Exposing the defect is another question with the same contract.
```

- reply line 70, variation said to break L367:

```
Exposing the defect is another question.
```

- reply line 75, variation said to break L161's last sentence:

```
Exposing the defect is an answer to the original question.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L367 "A new index is a new claim." — found at L367
- L377 "Let \(p_\delta\) be the question whether \(z\) has \(\delta\) in respect of \(p\)" — found at L377
- L377 "alleged defect \(\delta\)" — found at L377
- S28 "A theory is never settled." — found in the owner's words (S28)
- L377 "A criticism has target \(z\), alleged defect \(\delta\), premise \(g\), and a connection." — found at L377
- L367 "A proposition indexed to a contract remains that proposition when a later theory changes the current contract. A new index is a new claim." — found at L367
- L161 "Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one." — found at L161

#### GLM (`s103_vary_glm_2.response.txt`, lines 49–74)

*Points (digest):*

- Rival (a) 'Exposing the defect is another question.' breaks on 'own contract': L151 (without its own contract nothing marks the exposing question as a different question), L161's last sentence (the replacement's coherence must not leak back onto the original), and L55's frozen contract.
- Rival (b) '… a further question about the same target.' breaks L377, where the exposing question's subject is the criticized content z, not the original target D.
- Rival (c) 'Exposing an alleged defect …': 'alleged' is Part IX's word for criticism (L377); under the previous sentence's 'may' the defect is actual when it occurs, and 'the defect' ties each listed failure to its exposure; the variant redoes L377's job and leaves the three failures without their link.
- Fault sought: 'Another' is not idle; it marks the exposing question as distinct, which the following sentence presupposes.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 55, rival (a), said to break L151, L161 and L55:

```
Exposing the defect is another question.
```

- reply line 61, rival (b), said to break L377:

```
Exposing the defect is a further question about the same target.
```

- reply line 67, rival (c), said to duplicate L377 and untether the sentence:

```
Exposing an alleged defect is another question with its own contract.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L151 "Two questions with the same $D$ and different $(C,\mathcal Q)$ are different questions, and an answer to one is not an answer to the other." — found at L151
- L161 "Supplying a meaning for a replacement query can make a coherent new question; it does not answer the original one" — found at L161
- L377 "the question whether $z$ has $\delta$ in respect of $p$" — found at L377
- L377 "alleged defect $\delta$" — found at L377

### C16 · L217 · Part IV — Layers, transports, and provenance; Prediction, surprise, violation

**The sentence** (as the brief gives it; found word for word in file 99 at L217):

> For an edit–boundary pair \((a,b)\in C\) actually occurring:

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_2.response.txt`, line 106): HOLDS

```
`C16: HOLDS — admitted, encountered and coming about each break L159, L195, L223, L582 or S25.`
```

- GLM (`s103_vary_glm_2.response.txt`, line 99): HOLDS

```
C16: HOLDS — removing "actually occurring" breaks L582 and L159; "encountered" breaks L223 and L195; "physically realized" crosses the S25/S26 boundary and mismatches L582.
```

**To a checker:** no: both readers close HOLDS and no point of either shows a defect (rule 6).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_2.response.txt`, lines 83–107)

*Points (digest):*

- Break: 'admitted' breaks L159 (admitting a change is not a claim that it can be carried out or come about), L223 ('one of them must occur') and L582: admission is not occurrence.
- Break: 'actually encountered' breaks L195 (the history term of a selected transport) and L223 (prediction and violation are defined for every transport).
- Break: 'actually coming about' breaks L159 and S25.
- Break: replacing C by H in the pair breaks L572 and L221.
- Step 3: 'actually' is forced by the admission/occurrence split; the notation (a,b)∈C is forced by L572 and L221.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 88, variation said to break L159, L223 and L582:

```
For an admitted edit–boundary pair \((a,b)\in C\):
```

- reply line 93, variation said to break L195 and L223:

```
For an edit–boundary pair \((a,b)\in C\) actually encountered:
```

- reply line 98, variation said to break L159 and S25:

```
For an edit–boundary pair \((a,b)\in C\) actually coming about:
```

- described in prose, no wording written out: Replacing \(C\) by \(H\) in the pair (no wording written out): said to break L572 and L221.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L159 "admitting a change is not a claim that it can be carried out or come about" — found at L159
- L223 "one of them must occur" — found at L223
- L582 "at an occurring \((a,b)\in C\) with \((a,b)\notin H\)" — found at L582
- L195 "a finite history \(H\subseteq C\) of edit–boundary pairs actually encountered" — found at L195
- L223 "Prediction and violation are defined for every transport to the simulation layer" — found at L223
- L159 "whether anyone could carry a change out, or whether it could come about, is a matter of instantiation and transformation (Part XII)" — found at L159
- S25 "'Physically possible or impossible' has to do with instantiation and transformation of information and knowledge. It has nothing to do with explanation." — found in the owner's words (S25; quotation marks inside given as single)
- L572 "For every \((a,b)\in C\setminus H\)" — found at L572
- L221 "at \((a,b)\notin H\)" — found at L221

#### GLM (`s103_vary_glm_2.response.txt`, lines 75–100)

*Points (digest):*

- Rival (a) dropping the qualifier defines prediction and violation on pairs that never occur; breaks L582, which restates this sentence, and undoes what L159 keeps apart.
- Rival (b) 'encountered' is the history term (L195); L223 defines prediction and violation for every transport, including declared ones (L199) held by no encountering system.
- Rival (c) 'physically realized': occurrence is the right notion, but the wording invites reading physical realization as a precondition inside the theory, against S26, and moves away from the phrase L582 quotes.
- Fault sought: none; 'actually' contrasts occurrence with mere admission.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 81, rival (a), qualifier dropped, said to break L582 and L159:

```
For an edit–boundary pair $(a,b)\in C$:
```

- reply line 87, rival (b), said to break L223 and L195:

```
For an encountered edit–boundary pair $(a,b)\in C$:
```

- reply line 93, rival (c), said to cross S25/S26 and mismatch L582:

```
For a physically realized edit–boundary pair $(a,b)\in C$:
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L582 "Surprise is defined (Part IV) as a violation of a selected transport at an occurring $(a,b)\in C$" — found at L582
- L159 "is not a claim that it can be carried out or come about" — found at L159
- L195 "a finite history $H\subseteq C$ of edit–boundary pairs actually encountered" — found at L195
- L223 "Prediction and violation are defined for every transport to the simulation layer, surprise only for a selected one" — found at L223
- S26 "Physical possibility comes in only when something is instantiated or transformed" — found in S26 (Claude's sentence, which the owner answered "This is correct.")

### C17 · L219 · Part IV — Layers, transports, and provenance; Prediction, surprise, violation

**The sentence** (as the brief gives it; found word for word in file 99 at L219):

> - the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_2.response.txt`, line 129): HOLDS

```
`C17: HOLDS — dropping the translations, changing whose answer it is, or adding a faithfulness condition each break (A) at L250, L189, L177 or L223.`
```

- GLM (`s103_vary_glm_2.response.txt`, line 121): HOLDS

```
C17: HOLDS — the formula's positions are fixed by L189 and mirrored by (A) at L250; the verbal rival uncouples it from (A), and defining the prediction as $\operatorname{Ans}_p(a,b)$ abolishes violation.
```

**To a checker:** no: both readers close HOLDS and no point of either shows a defect (rule 6).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_2.response.txt`, lines 108–130)

*Points (digest):*

- Break: Ans_S(a,b) (translations dropped) breaks L189 and (A) at L250.
- Break: Ans_p(a,b) breaks L177 and L144, which make Ans_p the question's profile, not the simulation's.
- Break: adding 'when t is faithful' breaks L223 and L582: a violated transport must still have made a prediction.
- Step 3: the equation fixes the value (A) compares and the value L223 and L582 presuppose; only re-spellings of the same expression survive.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 113, variation said to break L189 and (A):

```
- the **prediction** is \(\operatorname{Ans}_S(a,b)\);
```

- reply line 118, variation said to break L177 and L144:

```
- the **prediction** is \(\operatorname{Ans}_p(a,b)\);
```

- reply line 123, variation said to break L223 and L582:

```
- the **prediction** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) when \(t\) is faithful;
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L189 "\(\tau\) translates edits, \(\sigma\) translates boundaries" — found at L189 (also at L119)
- L250 "\(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)\)" — found at L250
- L177 "whose components are dependencies among things and whose queries are predictions" — found at L177
- L223 "Prediction and violation are defined for every transport to the simulation layer" — found at L223
- L582 "If there is no transport there is no prediction and hence no violation" — found at L582

#### GLM (`s103_vary_glm_2.response.txt`, lines 101–122)

*Points (digest):*

- Rival (a), a verbal surrogate, loses the compositional form: L189 fixes the positions and (A) at L250 states them; the prediction no longer pairs with (A).
- Rival (b) Ans_p(a,b) makes the prediction correct by definition, so violation has nothing to be a failure of; the reader says this is against S20 and S23 (paraphrased, no quotation).
- Rival (c) swapping the translations is a type error against L189.
- Fault sought: none; L177 matches the form exactly.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 107, rival (a), said to uncouple the prediction from (A):

```
- the **prediction** is what $S$ answers at the translated edit and boundary;
```

- reply line 113, rival (b), said to abolish violation:

```
- the **prediction** is $\operatorname{Ans}_p(a,b)$;
```

- reply line 117, rival (c), translations swapped, said to be a type error against L189:

```
$\operatorname{Ans}_S(\sigma(a),\tau(b))$
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L189 "$\tau$ translates edits, $\sigma$ translates boundaries" — found at L189
- L250 "$\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)$" — found at L250
- L177 "whose queries are predictions: what a port of $P$ will take under an admitted edit" — found at L177
- S20 and S23 are cited by paraphrase ('error correction is the next thing to check'; 'nothing verified, nothing absolute'), not quoted

### C18 · L220 · Part IV — Layers, transports, and provenance; Prediction, surprise, violation

**The sentence** (as the brief gives it; found word for word in file 99 at L220):

> - a **violation** occurs when fidelity fails at \((a,b)\);

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_2.response.txt`, line 152): HOLDS

```
`C18: HOLDS — prediction-failure and breakdown break S27, L189, L233–L245 and L582; what survives re-spells the same criterion.`
```

- GLM (`s103_vary_glm_2.response.txt`, line 147): HOLDS

```
C18: HOLDS — "wrong prediction" drops (F1)/(F2) against L245; "reality falsifies" violates S23; globalizing over $C$ breaks L221 and L582.
```

**To a checker:** yes, under rule 5's clause on doubt: both readers close HOLDS, but Mimo records that the text forces faithfulness to be the component and global conditions (L189) while the sentence's uses attribute (A) to a violation and Part V heads (A) 'Question fidelity' (L247), and GLM reads the sentence's 'fidelity' as including (A); neither calls this a failure.

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_2.response.txt`, lines 131–153)

*Points (digest):*

- Break: 'when the prediction fails' breaks the separation the owner fixes in S27 and leaves (F1)–(F2) (L233–L245) with no role; L582 reads violation off the transport.
- Break: 'when the transport breaks down' breaks L189 and L626, which name the criterion.
- '(F1) or (F2) fails' is a re-spelling, not a rival: L245 makes it the same criterion, 'and where it would differ it drops question fidelity (A) at L247–L253, which this sentence's uses attribute to it'.
- Step 3, kept apart (bears on the scope of the sentence's word): the text forces a transport's faithfulness to be the component and global conditions (L189), while a reader may take 'fidelity' to cover (A) as well, since the passage heads it 'Question fidelity'; 'the sentence's word covers the passage either way'.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 136, variation said to break S27, L233–L245 and L582:

```
- a **violation** occurs when the prediction fails at \((a,b)\);
```

- reply line 141, variation said to break L189 and L626:

```
- a **violation** occurs when the transport breaks down at \((a,b)\);
```

- reply line 146, wording called a re-spelling of the same criterion, not a rival:

```
- a **violation** occurs when (F1) or (F2) fails at \((a,b)\);
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- S27 "Explanations can contradict each other at the level of explanation without ever having to be tested against reality." — found in the owner's words (S27)
- L582 "If there is no transport there is no prediction and hence no violation." — found at L582
- L189 "A transport is **faithful on \(C\)** when it meets the component and global fidelity conditions of Part V" — found at L189
- L626 "the fidelity failure is structural, not parametric" — found at L626
- L245 "Together they are fidelity at every level the contract reaches" — found at L245
- L247 "**Question fidelity**" — found at L247

#### GLM (`s103_vary_glm_2.response.txt`, lines 123–148)

*Points (digest):*

- Rival (a) 'a wrong prediction' under-defines: fidelity has parts, (F1) and (F2) at L233–L243 and (A) at L247–L251; a transport whose answer is right while a component relation is wrong ((F1) failing) is violated on the original and not on the rival.
- Rival (b) 'reality falsifies the prediction' is falsification in an absolute sense, which S23 forbids, and relocates the failure from fidelity to an unmediated comparison with reality.
- Rival (c) 'somewhere in C' breaks the localization that L221 and Argument 4 (L580–L582) need.
- Fault sought: none; this sentence does the localization, since fidelity is defined over all of C (L233) and L221, L582 use the pair-local notion it creates.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 129, rival (a), said to drop (F1)/(F2):

```
- a **violation** is a wrong prediction;
```

- reply line 135, rival (b), said to use language S23 forbids:

```
- a violation occurs when reality falsifies the prediction;
```

- reply line 141, rival (c), said to break L221 and L582:

```
- a violation holds where fidelity fails somewhere in $C$;
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L245 "(F1) prevents an assembled match from hiding a decomposition in error." — found at L245
- S23 "Anything that could be interpreted as needing verification or falsification in any absolute sense" — found in the owner's words (S23)
- L221 "a violation of a selected transport at $(a,b)\notin H$" — found at L221
- L233 "every $(a,b)\in C$" — found at L233 (also at L247, L564, L572)

### C19 · L225 · Part IV — Layers, transports, and provenance; Prediction, surprise, violation

**The sentence** (as the brief gives it; found word for word in file 99 at L225):

> Two responses to a violation are distinguished.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_2.response.txt`, line 183): VARIES

```
`C19: VARIES — The semantics distinguishes two responses to a violation.`
```

- GLM (`s103_vary_glm_2.response.txt`, line 173): HOLDS

```
C19: HOLDS — exhaustivity breaks S21 and L429; prescription breaks S21 and L429; outcome-naming breaks L584's "by their traces, not by their outcomes".
```

**To a checker:** yes: Mimo VARIES (rule 5); GLM holds that Mimo's rival wording (which GLM also names) is a recasting that changes no term and no dependency, not a variation; the readers differ (rule 7), and the checker's rule 5 question for a VARIES (a rewording that changes nothing the theory needs, or a different claim) is argued by both.

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_2.response.txt`, lines 154–184)

*Points (digest):*

- Rival 'The semantics distinguishes two responses to a violation.' is licensed by L584 and L626; it keeps the non-exhaustive claim the owner requires (S21; L429) and the two definitions that follow.
- Break: 'Two kinds of response' breaks the edit-signature word 'kinds' (heading L111; L245); 'There are two ways to respond' claims exhaustivity against S21 and L429; 'A violation admits two responses' breaks the admission vocabulary (L141, L257).
- Step 3: the passive leaves the distinguisher open; L584 names it. That both responses are open for every violation, the text does not force: L225 gives the selection response only 'of a selected transport'.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 159, rival offered as working (the closing line's rival):

```
The semantics distinguishes two responses to a violation.
```

- reply line 167, variation said to break the word 'kinds':

```
Two kinds of response to a violation are distinguished.
```

- reply line 172, variation said to claim exhaustivity against S21 and L429:

```
There are two ways to respond to a violation.
```

- reply line 177, variation said to break the admission vocabulary:

```
A violation admits two responses.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L584 "the semantics distinguishes them by their traces, not by their outcomes." — found at L584
- L626 "Two responses." — found at L626
- S21 "Notice I never once claimed what must happen." — found in the owner's words (S21)
- L429 "no argument makes the choice" — found at L429
- "Kinds are edit-signatures" (the heading, placed by the reader in the brief's bracket for L56–L132) — found at L111
- L245 "there is no further condition about kinds to state (Argument 1)" — found at L245
- S21 "If the person decides the problem is a low priority, then this whole process may be abandoned." — found in the owner's words (S21)
- L429 "an argument can rule out some ways of closing it for the person choosing" — found at L429
- L141 "the set of admitted edit–boundary pairs the claim ranges over" — found at L141
- L257 "every edit the target admits" — found at L257
- L225 "of a selected transport" — found at L225

#### GLM (`s103_vary_glm_2.response.txt`, lines 149–174)

*Points (digest):*

- Standing note (applies to all of part 2): a recasting that keeps every term and every dependency and changes only voice or synonym does not show a sentence easy to vary; a variation changes what the sentence says, relies on or leaves out.
- Rival (a) 'There are two responses …' reads as exhaustive, against S21 and L429; abandoning or doing nothing is also possible.
- Rival (b) 'A violation demands one of two responses.' is normative; same breaks (S21, L429).
- Rival (c) 'The two responses are learning and creating.' inverts definition and ground; L584 distinguishes them by traces, not outcomes.
- On the active recasting 'The semantics distinguishes two responses to a violation': it changes no term and no dependency; it is L584's own next move, not a variation.
- Fault sought: the agentless passive is not slack; it names no responder and claims no exhaustiveness.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 155, rival (a), said to be exhaustive:

```
There are two responses to a violation.
```

- reply line 161, rival (b), said to be normative:

```
A violation demands one of two responses.
```

- reply line 167, rival (c), said to invert definition and ground:

```
The two responses are learning and creating.
```

- reply line 169, the active recasting, named in a parenthesis and said not to be a variation (the same words as Mimo's rival, without the full stop):

```
The semantics distinguishes two responses to a violation
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- S21 "this entire episode may never resolve"; "Notice I never once claimed what must happen" — found in the owner's words (S21)
- L429 "Closing an episode is a choice" — found at L429
- L429 "an argument can rule out some ways of closing it… no argument makes the choice" — found at L429
- L584 "the semantics distinguishes them by their traces, not by their outcomes." — found at L584

### C20 · L225 · Part IV — Layers, transports, and provenance; Prediction, surprise, violation

**The sentence** (as the brief gives it; found word for word in file 99 at L225):

> Only the second can be originative under Part X.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_2.response.txt`, line 211): HOLDS

```
`C20: HOLDS — is, dropping Only, creative and must each break (G)/(N), L201/L405/L584, L425/L429 or S21/L429.`
```

- GLM (`s103_vary_glm_2.response.txt`, line 199): VARIES

```
C20: VARIES — Only a construction response can be originative under Part X.
```

**To a checker:** yes: GLM VARIES (rule 5); Mimo holds that 'the second' is fixed by the two definitions and L584, GLM that the defined term does the work at least as well; the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_2.response.txt`, lines 185–213)

*Points (digest):*

- Break: 'is originative' drops the modality and breaks (G) (L421–L422) and (N) (L413–L417): a construction response can fail New or Attempt.
- Break: dropping 'Only' breaks L201, L405 and L584.
- Break: 'creative' breaks the act/episode split (L425; L429).
- Break: 'must be' breaks S21 and L429.
- Step 3: 'can be' is forced by (G)'s three conjuncts; 'Only' by the selection response's history (L225), which has neither Build nor a represented target; 'the second' is fixed by the two definitions above and L584.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 190, variation said to break (G) and (N):

```
Only the second is originative under Part X.
```

- reply line 195, variation said to break L201, L405 and L584:

```
The second can be originative under Part X.
```

- reply line 200, variation said to break L425 and L429:

```
Only the second can be creative under Part X.
```

- reply line 205, variation said to break S21 and L429:

```
Only the second must be originative under Part X.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L421–L422 "\(\operatorname{Origin}_{\beta,\ell}(s,c,p,h,e)\iff\operatorname{Attempt}(s,c,p,h,e)\land\operatorname{New}(s,c,h,e)\land\operatorname{Build}_{\beta,\ell}(s,c,h,e)\)" — found at L422
- L201 "a selected transport has no represented target and no criticism in its history; a constructed one has both" — found at L201
- L405 "contains a nontrivial binding construction relevant to that use, and is not a composition of content-preserving transfers" — found at L405
- L584 "the difference between learning and creating" — found at L584
- L425 "the originative act is the finding of a question" — found at L425
- L429 "A creative critical episode contains an instance of (G) connected to its inquiry." — found at L429
- S21 "Notice I never once claimed what must happen" — found in the owner's words (S21)
- L429 "no argument makes the choice" — found at L429
- L225 "extends the history \(H\) of a selected transport and lets \(\mu\) act" — found at L225
- L584 "The two responses, extend \(H\) and re-tune, or construct a new transport" — found at L584

#### GLM (`s103_vary_glm_2.response.txt`, lines 175–201)

*Points (digest):*

- Load-bearing parts: 'Only', 'can be', 'under Part X'. The exclusion is sound: the selection response re-tunes within the population (L225); a selection history contains no representation (L195), so no construction trace can exist there, and Build (L405) requires one; the reader adds that L626 'confirms the failure the selection response answers is "structural, not parametric"'.
- Rival (a) 'is originative' breaks (G) at L422: a construction response that rebuilds an already available transport fails New (L413–L416). The modality is load-bearing.
- Rival (b) 'Only construction is creative.' has the same modal break, and 'creative' is not the defined term; L592 ties creativity to (G).
- Rival (c) 'Only a construction response can be originative under Part X.' keeps 'only', 'can be' and 'under Part X', names the response by the term defined earlier in the same line (L225), and breaks nothing: L584 refers to the pair by content, not position, and nothing else in the given lines cites 'the second'. It stands on the defined term instead of the order of the two definitions, and so does the sentence's work at least as well.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 183, rival (a), said to break (G):

```
Only the second is originative under Part X.
```

- reply line 189, rival (b), said to break the modality and use a term not defined:

```
Only construction is creative.
```

- reply line 195, rival (c), offered as working (the closing line's rival):

```
Only a construction response can be originative under Part X.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L225 "extends the history $H$ … and lets $\mu$ act: the transport is re-tuned within the population" — found at L225
- L195 "No member of the history represents $t$, $H$, or the survival condition" — found at L195
- L405 "contains a nontrivial binding construction … and is not a composition of content-preserving transfers" — found at L405
- L626 "structural, not parametric" — found at L626 (in the worked episode's selection response)
- L225 "A **construction response** introduces a new organization or a new transport with a construction trace" — found at L225
- L584 "extend $H$ and re-tune, or construct a new transport" — found at L584


## Part 3: C21–C29 (Parts V to XIV)

### C21 · L273 · Part V — Account; What (E) excludes, and what it does not

**The sentence** (as the brief gives it; found word for word in file 99 at L273):

> "\(p\) because \(p\)" fails non-circular dependence.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 31): VARIES

```
C21: VARIES — Conclusion-as-premise fails non-circular dependence.
```

- GLM (`s103_vary_glm_3.response.txt`, line 15): HOLDS

```
C21: HOLDS — every variation broke the verbatim echo at L397 or the "fails" usage at L275 and L536.
```

**To a checker:** yes: Mimo VARIES (rule 5); GLM argues that dropping the formula '\(p\) because \(p\)' from L273 breaks its tie to L397, which Mimo's rival drops while saying L397 keeps its own anchor; the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 1–32)

*Points (digest):*

- Rival 'Conclusion-as-premise fails non-circular dependence.' names the case exactly as the recap at L536 names it and names the same conjunct; L273's next sentence still extends from it; the instance string keeps its own anchor at L397.
- Break: '"p because p" is not an account.' and '… fails (E).' each break L536's demand that Part V say 'which of the four each classic attempt fails': (E) is a conjunction of five (L262).
- Break: '… premise is logically equivalent to its answer …' breaks L255 (identity is structural, not the identification of all logically equivalent statements).
- Step 3: no contradiction, no vacuity; a reader might take the shown shape to be the only one excluded; L255 and the next sentence reach further. The text forces the classification only.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 6, rival offered as working (the closing line's rival):

```
Conclusion-as-premise fails non-circular dependence.
```

- reply line 14, variation said to break L536 and L262:

```
"\(p\) because \(p\)" is not an account.
```

- reply line 18, variation said to break L536 and L262:

```
"\(p\) because \(p\)" fails (E).
```

- reply line 24, variation said to break L255:

```
An account whose premise is logically equivalent to its answer fails non-circular dependence.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L536 (excerpt) "Part V says which of the four each classic attempt fails: … conclusion-as-premise fails non-circular dependence." — found at L536
- L273 "So does an account whose only substantive component restates the answer it was asked for" — found at L273
- L397 (excerpt) "Such an argument, as one against that claim, has its conclusion among its premises, as in "\(p\) because \(p\)", and does not rule that claim out for anyone." — found at L397
- L536 "which of the four each classic attempt fails" — found at L536
- L262 "\(\operatorname{Account}(\mathcal E)\iff \text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}\)" — found at L262
- L255 "Identity of that assertion with the target's answer is structural at the declared grain, not the indiscriminate identification of all logically equivalent mathematical statements." — found at L255

#### GLM (`s103_vary_glm_3.response.txt`, lines 3–16)

*Points (digest):*

- The sentence's work: give the canonical circular case, name the conjunct of (E) it fails, and stand as the account-level twin of the argument-level rule in Part IX.
- 'violates' splits the text's verb for not meeting a condition ('fails': L275, 'L267' as the reader cites it, the quoted words standing at L269, L271, and L536's summary) without gain.
- 'An explanation whose premise is its own conclusion …' drops the formula; the identical formula in L273 and L397 is what makes the parallel between Part V's structural reading of identity and Part IX's reading of a premise that is the denial visible; dropping it breaks that tie.
- '"The answer because the answer" …' loses the match with L397's verbatim quotation.
- Fault sought: non-circular dependence (L255) is a conjunction; 'p because p' fails its first part, so the sentence is correct; the case is the one L536 names.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 9, variation said to split the 'fails' usage (L275, L536):

```
"\(p\) because \(p\)" violates non-circular dependence.
```

- reply line 10, variation said to break the verbatim tie to L397:

```
An explanation whose premise is its own conclusion fails non-circular dependence.
```

- reply line 11, variation said to lose the match with L397:

```
"The answer because the answer" fails non-circular dependence.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L275 "and fails non-circular dependence" — found at L275
- L267 "it fails (F1)" — found at L269, not at L267 (L267 is the heading "## What (E) excludes, and what it does not")
- L271 "fails (F2)" — found at L271
- L536 "conclusion-as-premise fails non-circular dependence" — found at L536
- L397 "Such an argument, as one against that claim, has its conclusion among its premises, as in "\(p\) because \(p\)"" — found at L397
- L255 "The target's answer does not appear… as a component" — found at L255

### C22 · L311 · Part VI — Work, routes, and interference; Infinitary routes

**The sentence** (as the brief gives it; found word for word in file 99 at L311):

> (B) records the collective contribution.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 65): VARIES

```
C22: VARIES — (B) records the contribution of a block.
```

- GLM (`s103_vary_glm_3.response.txt`, line 29): HOLDS

```
C22: HOLDS — replacements of "contribution" broke the ties to L305, L307 and L435, and "defines" misstates what (B) is.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ (rule 7); GLM's fault search also notes that 'contribution' is used in two senses in the text and sets that aside.

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 33–66)

*Points (digest):*

- Rival '(B) records the contribution of a block.': (B) (L296) assesses blocks, and a block is the collection whose contribution the sentence marks (L313); 'contribution' keeps the reach to Part XI (L435).
- Break: '(S) records …' breaks L290 ((S) is a list of routes only) and leaves L313's pointer '{d} is critical in no route (B)' with nothing that records criticality.
- Break: '… each commitment's contribution' breaks L311 and L313.
- Break: 'Each commitment is contributory.' breaks L305, whose assumptions L311 withholds.
- Step 3: no fault; 'collective' blocks the individual reading L313 denies, and the word 'block' carries that in the rival.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 38, rival offered as working (the closing line's rival):

```
(B) records the contribution of a block.
```

- reply line 46, variation said to break L290 and L313:

```
(S) records the collective contribution.
```

- reply line 52, variation said to break L311 and L313:

```
(B) records each commitment's contribution.
```

- reply line 58, variation said to break L305:

```
Each commitment is contributory.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L295–L297 "\(\operatorname{CriticalBlock}(B;W,p)\iff W\in\mathsf S_{E,p}\land W\setminus B\notin\mathsf S_{E,p}\)" — found at L296
- L313 "When \(\Gamma\) is infinite, a block of such commitments can still be critical (Infinitary routes)." — found at L313
- L435 "The contribution \(\Delta\) of a repair is a subhistory together with the changes of content it makes." — found at L435
- L290 "\(\mathsf S_{E,p}=\{W\subseteq\Gamma:\operatorname{Account}(E|W,p)\}\)" — found at L290
- L313 "\(\{d\}\) is critical in no route (B)" — found at L313
- L311 "no minimal route, and no route of one commitment, exists" — found at L311
- L305 (excerpt) "**Finite monotone claim.** If \(\Gamma\) is finite, \(\mathsf S\) is upward closed, and \(\Gamma\in\mathsf S\), then \(d\in\Gamma\) is critical for some route (**contributory**)" — found at L305

#### GLM (`s103_vary_glm_3.response.txt`, lines 17–30)

*Points (digest):*

- The sentence's work: state that in the infinitary example no commitment is critical alone and that (B) carries the block's credit.
- '(B) records that the work can be collective.': 'work' is the Part's title word, but 'contribution' links L311 to L305 ('contributory') and to Part XI (L307, L435, L441); 'work' severs both links.
- 'Only blocks are critical here; (B) says so.': granted by GLM as far as it goes, but said to lose the named definition and 'contribution'; 'here' points at the example, whereas the original states the general role of (B).
- '(B) defines the collective contribution.': (B) defines criticality of blocks (L296), not a contribution; 'records' is the right verb.
- Fault sought and set aside: 'contribution' is used in two senses in the text (L305's per-commitment sense, L435's subhistory sense); L307 separates route-criticality from ProducedBy attribution, so the sentence does not trespass on Part XI. No conflict found.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 23, variation said to sever 'contribution' from L305, L307, L435:

```
(B) records that the work can be collective.
```

- reply line 24, variation said to lose the named definition and 'contribution':

```
Only blocks are critical here; (B) says so.
```

- reply line 25, variation said to misstate what (B) is (L296):

```
(B) defines the collective contribution.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L296 `CriticalBlock(B;W,p) ⟺ W∈S ∧ W∖B∉S` — found at L296 in substance (written in Unicode, with the subscript E,p of \(\mathsf S\) left out)
- L305 "**contributory**" — found at L305
- L307 "attributes a repair to the contributions whose active routes ran to it" — found at L307

### C23 · L375 · Part IX — Criticism, use, and usable arguments; Histories

**The sentence** (as the brief gives it; found word for word in file 99 at L375):

> An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 95): VARIES

```
C23: VARIES — An active route is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and whose result varies with the represented distinction under the declared contrasts.
```

- GLM (`s103_vary_glm_3.response.txt`, line 44): HOLDS

```
C23: HOLDS — every removal contradicted L307, L375's own following sentence, L255, or L524.
```

**To a checker:** yes: Mimo VARIES (rule 5); Mimo's step 3 notes that reading the definition as exhaustive would clash with the exclusion of a route 'already at rest when the result occurred' (in doubt whether a defect); the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 67–96)

*Points (digest):*

- Rival: 'which has nonconstant dependence on the represented distinction' becomes 'whose result varies with the represented distinction': the same property, bound to the operative result the definition names; the four conditions and every named term stay.
- Note: 'Operative result', 'applicable relations' and 'structural map' (C25) are not defined in the lines given.
- Break: dropping 'under the declared contrasts' breaks L231 and L255; 'possible occurrences' breaks L375's third sentence, L307 and L441; dropping the dependence clause admits a route that 'started and did no work', which L375 excludes.
- Step 3: a reader might take 'is' as exhaustive, which would clash with the exclusion of a route 'already at rest when the result occurred'; the text forces no exhaustiveness (compare L231's 'exactly when'), so the exclusion is read inside the definition.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 72, rival offered as working (the closing line's rival):

```
An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and whose result varies with the represented distinction under the declared contrasts.
```

- reply line 80, variation said to break L231 and L255:

```
An **active route** is a connected subnetwork of actual occurrences joining a represented input to an operative result, whose components meet the applicable relations and whose result varies with the represented distinction.
```

- reply line 86, variation said to break L375, L307 and L441:

```
An **active route** is a connected subnetwork of possible occurrences joining a represented input to an operative result, whose components meet the applicable relations and which has nonconstant dependence on the represented distinction under the declared contrasts.
```

- described in prose, no wording written out: Dropping the dependence clause (no wording written out): said to admit a route that "started and did no work", which L375 excludes.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- (the candidate) "has nonconstant dependence on the represented distinction", "applicable relations", "under the declared contrasts", "started and did no work" — found at L375
- L231 "each a condition on supplied relations under the changes in \(C\)" — found at L231
- L255 "There exist \((a,b)\in C\) and a nonempty block \(G\subseteq\Gamma\) such that" — found at L255
- L375 "whether a route is active is read from the history, not from the result" — found at L375
- L307 (excerpt) "a subnetwork of actual occurrences in the system's history" — found at L307
- L441 (excerpt) "\(\operatorname{ProducedBy}\) is met when an active route (Part IX) runs from \(\Delta\) to the repair" — found at L441
- "structural map" — found at L385; "already at rest when the result occurred" — found at L375

#### GLM (`s103_vary_glm_3.response.txt`, lines 31–45)

*Points (digest):*

- Removing 'connected' lets a scattered set of occurrences qualify, contradicting L307; routes of a candidate are arbitrary subsets of Γ (L299) and connectedness is what an active route adds.
- Removing 'actual' breaks L307 likewise.
- Removing the dependence clause counts as active a route that ran without the distinction making any difference, contradicting L375's next sentence; the clause mirrors L255's contrast condition.
- Removing 'under the declared contrasts' reads dependence grain-free, against L524 and the contract-relativity of L255.
- Fault sought: each ingredient is defined earlier (L169, L205–L209, L109, L91); 'read from the history, not from the result' matches; no circularity (the two kinds of route are joined only at L307). The reader cannot check 'applicable relations' and 'operative result' against lines not given, and finds nothing in the given lines that conflicts.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 37, clause removed ('Drop'), said to contradict L307:

```
connected
```

- reply line 38, clause removed, said to break L307:

```
actual
```

- reply line 39, clause removed, said to contradict L375 and L255:

```
which has nonconstant dependence on the represented distinction under the declared contrasts
```

- reply line 40, clause removed, said to break L524 and L255:

```
under the declared contrasts
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L307 "it is active in a system when occurrences that realize it form an active route (Part IX), a subnetwork of actual occurrences in the system's history." — found at L307
- L307 "actual occurrences" — found at L307
- L375 "A route that started and did no work… is not active for that result" — found at L375
- L255 "this contrast is lost when the components of G are deleted" — found at L255
- L375 "Read from the history, not from the result" — found at L375 (capital R the reader's)

### C24 · L383 · Part IX — Criticism, use, and usable arguments

**The sentence** (as the brief gives it; found word for word in file 99 at L383):

> A criticism occurrence can exist when (K1) fails.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 129): VARIES

```
C24: VARIES — A criticism occurrence can exist whether or not (K1) holds.
```

- GLM (`s103_vary_glm_3.response.txt`, line 58): VARIES

```
C24: VARIES — `A criticism occurrence need not meet (K1).`
```

**To a checker:** yes: both readers close VARIES, with different rivals (rules 5 and 7); both discuss the idiom '(K1) fails' for a biconditional.

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 97–130)

*Points (digest):*

- Rival 'A criticism occurrence can exist whether or not (K1) holds.' keeps 'can exist' and the (K1) pointer (L380); it says existence is possible with and without bearing, which is the separation the sentence draws.
- Break: 'exists when (K1) fails' breaks L383's second sentence (existence keeps that condition); 'cannot exist' breaks L71 and turns a bearing condition into an existence condition; '(E) fails' breaks L377–L380's separation (what fails is (K1), not (E) of some other candidate).
- Step 3: '(K1) fails' reads as 'the condition (K1) states is unmet', the idiom of L269's 'it fails (F1)'; read as the biconditional coming apart it would be nonsense, but nothing forces that reading.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 102, rival offered as working (the closing line's rival):

```
A criticism occurrence can exist whether or not (K1) holds.
```

- reply line 110, variation said to break L383's second sentence:

```
A criticism occurrence exists when (K1) fails.
```

- reply line 116, variation said to break L71:

```
A criticism occurrence cannot exist when (K1) fails.
```

- reply line 122, variation said to break L377–L380:

```
A criticism occurrence can exist when (E) fails.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L380 "\(\operatorname{Bearing}(c,z,p)\iff\operatorname{Account}(\mathcal E_c)\)" — found at L380
- L383 "An adverse signal is not a criticism until an organization represents it as the premise of a criticism alleging a defect in a target" — found at L383
- L71 "A criticism has a target and is itself conjectural." — found at L71
- L269 "it fails (F1)" — found at L269

#### GLM (`s103_vary_glm_3.response.txt`, lines 46–59)

*Points (digest):*

- The sentence's work: block the inference from 'a criticism occurred' to 'it had bearing' — the point of S27 (an agent may use 'perpetual motion is impossible' as a given, without containing the explanation) and of L71.
- 'A criticism occurrence can exist while it lacks bearing (K1).': same content, slightly longer; the tag placement differs from L385 but does not break it.
- 'A criticism occurrence need not meet (K1).': 'meet' is the text's verb for satisfying a condition (L277); it states the same non-necessity, pairs unchanged with the next sentence, and breaks nothing the reader can find (L377–L381 define Bearing only; L385 presupposes this independence).
- 'A criticism can be mistaken.' imports an appraisal the semantics does not define, and "mistaken" "trends toward the forbidden truth-language of S23" (GLM's words).
- Fault sought: '(K1) fails' follows the text's usage (L267, L271, L273); K1 can fail for c only by ¬Account(E_c), so the sentence is coherent; no contradiction with L71 or S27.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 52, variation said to have the same content, longer:

```
A criticism occurrence can exist while it lacks bearing (K1).
```

- reply line 53, rival offered as working (the closing line's rival):

```
A criticism occurrence need not meet (K1).
```

- reply line 54, variation said to import an appraisal and trend toward S23's forbidden language:

```
A criticism can be mistaken.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- S27 "perpetual motion is impossible" — found in the owner's words (S27; also at L315); the rest of the S27 point is a paraphrase
- L71 "A criticism has a target and is itself conjectural." — found at L71
- L385 "does not give it bearing (K1)" and "Using an objection does not give it bearing (K1)" — found at L385
- L277 "a mechanism meets (E) or fails it" — found at L277
- L383 "An adverse signal is not a criticism until an organization represents it as the premise of a criticism…" — found at L383

### C25 · L385 · Part IX — Criticism, use, and usable arguments; Reason use

**The sentence** (as the brief gives it; found word for word in file 99 at L385):

> **Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 159): VARIES

```
C25: VARIES — Reason use. A response uses a reason when there is a structural map from the represented objection into the response suborganization that lands on an active route, preserves role bindings, sends content-preserving recodings to the same transition, and sends content changes to the changes the operative deliberative rule specifies.
```

- GLM (`s103_vary_glm_3.response.txt`, line 72): HOLDS

```
C25: HOLDS — each clause-drop contradicted L409's cited paraphrase, and loosening the structural-map head stranded it.
```

**To a checker:** yes: Mimo VARIES (rule 5), and Mimo's step 3 alleges that 'the same transition' has no antecedent in the line; the readers differ on what L409's paraphrase matches (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 131–160)

*Points (digest):*

- Rival: the existential made explicit ('when there is a structural map … that …') and the four clauses reordered; each clause, each term and the direction of the map stay.
- Break: dropping 'content-preserving' breaks L365 and L409; dropping 'preserves role bindings' or 'lands on an active route' breaks L409, which lists those clauses as reason use's requirements.
- Break: '… changes specified by the role bindings' breaks the division of labour the sentence states (clause one preserves role bindings, clause three is about the operative deliberative rule); L409's 'the changes the binding specifies' is in the construction-trace context, where a binding constructed in the subhistory is what is identified.
- Step 3 (alleges a defect of wording): 'the same transition' has no antecedent in the line; it reads as the transition the mapped content reaches. 'Operative deliberative rule' and 'structural map' are not defined in the lines given.
- Note: the closing line's rival drops the bold markup of 'Reason use.' that the fenced rival (reply line 136) carries.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 136, rival offered as working (the closing line gives it without the bold on 'Reason use.'):

```
**Reason use.** A response uses a reason when there is a structural map from the represented objection into the response suborganization that lands on an active route, preserves role bindings, sends content-preserving recodings to the same transition, and sends content changes to the changes the operative deliberative rule specifies.
```

- reply line 144, variation ('content-preserving' dropped), said to break L365 and L409:

```
**Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends recodings to the same transition, sends content changes to the changes specified by the operative deliberative rule, and lands on an active route.
```

- reply line 152, variation said to break the division of labour between clauses:

```
**Reason use.** A response uses a reason when a structural map from the represented objection into the response suborganization preserves role bindings, sends content-preserving recodings to the same transition, sends content changes to the changes specified by the role bindings, and lands on an active route.
```

- described in prose, no wording written out: Dropping "preserves role bindings" or "lands on an active route" (no wording written out): said to break L409.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L365 "A declared, invertible recoding of a carrier preserves the content when a reader who applies the declared convention recovers every pairing (Argument 8)" — found at L365
- L409 (excerpt) "send content-preserving recodings to the same transition" — found at L409
- L409 (excerpt) "as reason use asks of an objection (Part IX)" — found at L409
- L409 "the changes the binding specifies"; "a binding constructed in the subhistory" — found at L409

#### GLM (`s103_vary_glm_3.response.txt`, lines 60–73)

*Points (digest):*

- Every clause of the definition is paraphrased, with an explicit citation, at L409 ('as reason use asks of an objection (Part IX)').
- Dropping any one of the four clauses contradicts the corresponding item of L409's paraphrase.
- Replacing the structural-map head with 'a correspondence of the objection to the response' strands the paraphrase; the structural-map form is what the equivariance result rests on (L612).
- 'lands on' → 'lies on': a map lands on a route, responses lie on it (L409); possible but not better; the original keeps map and responses distinct.
- Fault sought: GLM says "'Uses a reason'" where the reason is the objection "fits S23's 'reasons why this and not that'"; the second sentence separates use from bearing and usability. 'Operative deliberative rule' is not defined in the lines given; no conflict found.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 66, clause removed ('Drop', each in turn), said to contradict L409's paraphrase:

```
preserves role bindings
```

- reply line 66, clause removed ('Drop', each in turn), said to contradict L409's paraphrase:

```
sends content-preserving recodings to the same transition
```

- reply line 66, clause removed ('Drop', each in turn), said to contradict L409's paraphrase:

```
sends content changes to the changes specified by the operative deliberative rule
```

- reply line 66, clause removed ('Drop', each in turn), said to contradict L409's paraphrase:

```
lands on an active route
```

- reply line 67, words replaced:

```
a structural map from the represented objection into the response suborganization
```

- reply line 67, replacement, said to strand L409's paraphrase and L612:

```
a correspondence of the objection to the response
```

- reply line 68, words replaced:

```
lands on
```

- reply line 68, replacement, said to be possible but not better:

```
lies on
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L409 "by responses that preserve its role bindings, send content-preserving recodings to the same transition and content changes to the changes the binding specifies, and lie on an active route, as reason use asks of an objection (Part IX)." — found at L409
- L612 "Transporting all carriers, relations, transports… along structure-preserving bijections preserves (E), (G), (P), (EX)" — found at L612
- S23 "reasons why this and not that" — found in the owner's words (S23; also at L8)

### C26 · L393 · Part IX — Criticism, use, and usable arguments

**The sentence** (as the brief gives it; found word for word in file 99 at L393):

> Withdrawing a premise makes the step unusable; it does not rule the conclusion out.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 189): VARIES

```
C26: VARIES — Withdrawing a premise makes the step unusable and rules out no claim.
```

- GLM (`s103_vary_glm_3.response.txt`, line 87): HOLDS

```
C26: HOLDS — alternatives lost the named conclusion, contradicted L8/L315/L369, or imported wording S23 forbids.
```

**To a checker:** yes: Mimo VARIES (rule 5); GLM rejects, as ambiguous, a wording close to Mimo's rival ('rules nothing out' against Mimo's 'rules out no claim'); the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 161–190)

*Points (digest):*

- Rival 'Withdrawing a premise makes the step unusable and rules out no claim.': the second clause covers the first (the conclusion is a claim), so the guarded misreading is blocked, and the wider statement matches L8.
- Break: 'leaves the step usable' breaks L390 and L393's Live clause; 'rules the conclusion out' breaks L8 and L315.
- Break: dropping the second clause leaves the step's collapse unseparated from the conclusion's standing, where L369 states both halves for candidates.
- Step 3: the unqualified 'a premise' is read in context as one of Prem(u), 'the premises its inference form uses' (L387); withdrawing a premise outside that set is not covered by (K2). A reader might take it that any dropped sentence in a record has this effect; the text forces the essential-premise reading only.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 166, rival offered as working (the closing line's rival):

```
Withdrawing a premise makes the step unusable and rules out no claim.
```

- reply line 174, variation said to break L390 and L393:

```
Withdrawing a premise leaves the step usable.
```

- reply line 180, variation said to break L8 and L315:

```
Withdrawing a premise rules the conclusion out.
```

- described in prose, no wording written out: Dropping the second clause (no wording written out): said to leave the step's collapse unseparated from the conclusion's standing (L369).

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L8 "An argument rules out a claim when the claim is inconsistent with its conclusion and the claim's denial is not among its premises" — found at L8
- L390 "\(\operatorname{Usable}_j(u)\iff\operatorname{Form}_j(u)\land\operatorname{Scope}_j(u)\land\forall d\in\operatorname{Prem}(u),\operatorname{Live}_j(d;u)\)" — found at L390
- L393 "or a premise \(j\) tentatively accepts, having taken it up, for whatever reason, and not withdrawn it" — found at L393
- L315 (excerpt) "A claim is **ruled out** for an assessor \(j\) when an argument usable by \(j\) (Part IX) rules it out" — found at L315
- L369 (excerpt) "If a premise about them ceases to be live, the argument is not usable (K2) and those candidates are no longer ruled out by it, every such candidate alike" — found at L369
- L387 "the premises its inference form uses" — found at L387

#### GLM (`s103_vary_glm_3.response.txt`, lines 74–88)

*Points (digest):*

- Dropping the second half: nothing in Part IX then says that withdrawal is not itself a ruling-out; the sentence is the local anchor for L8 and L369, which need 'un-usable ≠ ruled out' stated.
- '… makes the step unusable and rules nothing out.' is ambiguous between 'the step rules nothing out' (trivial once unusable) and 'the withdrawal rules nothing out' (too broad), and loses the named claim at stake, the step's conclusion, which L315's definition is about.
- '… undermines the step; the conclusion is not thereby refuted.' uses what GLM calls "belief/verification language of the kind S23 forbids"; 'rule out' is the defined term (L315).
- '… either way.': the added words do no work.
- Fault sought: withdrawal removes Live (L393), so (K2) fails; an unusable argument rules out nothing (L8). No circularity or vacuity.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 81, variation said to be ambiguous and to lose the named conclusion (L315):

```
Withdrawing a premise makes the step unusable and rules nothing out.
```

- reply line 82, variation said to use language S23 forbids:

```
Withdrawing a premise undermines the step; the conclusion is not thereby refuted.
```

- reply line 83, variation said to add words that do no work:

```
Withdrawing a premise makes the step unusable; it does not rule the conclusion out either way.
```

- described in prose, no wording written out: Dropping the second half (no wording written out): said to lose the anchor for L8 and L369.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L8 "A claim that no argument rules out is only not ruled out, and gets nothing from that" — found at L8
- L369 "those candidates are no longer ruled out by it… no candidate becomes an account by that (E)" — found at L369
- L393 "not withdrawn it" — found at L393
- L8 "only while it stays usable (K2)"; "gets nothing from that" — found at L8

### C27 · L443 · Part XI — Repair, created explanation, and appraisal; Created explanation

**The sentence** (as the brief gives it; found word for word in file 99 at L443):

> An explanatory aim requires an account, or the correction of a use through one, to be deployable.

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 221): FAILS

```
C27: FAILS — "to be deployable" governs both disjuncts, so a correction of a use is made deployable, though Deploy is a relation on contents (L403; L449) — An explanatory aim requires an account to be deployable, or a use to be corrected through one.
```

- GLM (`s103_vary_glm_3.response.txt`, line 108): FAILS

```
C27: FAILS — "to be deployable" cannot apply to "the correction of a use": Deploy takes a content (L403), a correction is a repair on histories (L438), and (EX) deploys the account (L449) — `An explanatory aim requires an account to be deployable, whether the aim is that account or the correction of a use through it.`
```

**To a checker:** yes: both readers close FAILS on the same fault, with different repair wordings (rules 5 and 7); within Mimo's section the rival it calls 'the repair' (reply line 200) differs from the repair its closing line gives.

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 191–222)

*Points (digest):*

- Fault (FAILS): in the sentence, 'to be deployable' governs the disjunction 'an account, or the correction of a use through one', so a correction is made deployable; Deploy is a relation on contents (L403; L449 deploys c), and a correction of a use is a change, not a content. The charitable reading needs the complement moved onto 'an account' alone; the words do not do that.
- Rival 1 '… an account, or a use corrected through one, to be deployable.' keeps the sentence's grammar and keeps the fault.
- Rival 2 '… requires a deployable account, or the correction of a use through one.' 'types correctly, and is the repair'.
- Break: '… requires an account to be deployable.' drops the alternative the sentence marks; '… requires the correction of a use through one to be deployable.' breaks L403 and L449, where the deployable item is the created content c.
- Repair in the closing line: 'An explanatory aim requires an account to be deployable, or a use to be corrected through one.' (a third wording, not either rival above).

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 196, rival 1, said to keep the fault:

```
An explanatory aim requires an account, or a use corrected through one, to be deployable.
```

- reply line 200, rival 2, said to type correctly and to be 'the repair':

```
An explanatory aim requires a deployable account, or the correction of a use through one.
```

- reply line 208, variation said to drop the alternative:

```
An explanatory aim requires an account to be deployable.
```

- reply line 214, variation said to break L403 and L449:

```
An explanatory aim requires the correction of a use through one to be deployable.
```

- reply line 221, repair wording given only in the closing line:

```
An explanatory aim requires an account to be deployable, or a use to be corrected through one.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L403 "The repertoire \(R_{\beta,\ell}(s,\xi)\) is the set of contents deployable in some nontrivial use respect" — found at L403
- L449 "\(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi';U_c)\)" — found at L449
- L403 "\(\operatorname{Deploy}_{\beta,\ell}(s,c,\xi;U)\) is met when \(s\) at \(\xi\) holds a representation of \(c\)" — found at L403
- (the candidate) "to be deployable", "an account, or the correction of a use through one" — found at L443

#### GLM (`s103_vary_glm_3.response.txt`, lines 89–109)

*Points (digest):*

- Fault (FAILS): 'to be deployable' attaches by the sentence's grammar to both disjuncts, but Deploy is defined only for contents (L403); a correction of a use is not a content — correction is repair, a relation on histories and contributions (L438) — so the second disjunct cannot be deployable on the repair-event reading.
- On the charitable reading ('the correction of a use' denotes a corrected content), (EX) still deploys the account, not a corrected use (L449, with U_c the declared use task for c, L453). Either reading leaves one disjunct ill-typed or mismatched to (EX); what (EX) requires is a deployable account that runs to the repair (ProducesVia, L453).
- Variation 'requires a deployable account.' drops the correction-of-a-use coverage, which S20 ('Once the explanation is rescued, the mistake shouldn't be able to creep back in') and (P)'s protected aims exist for; '… an account, or a corrected use, to be deployable.' has the same type fault.
- Repair: 'An explanatory aim requires an account to be deployable, whether the aim is that account or the correction of a use through it.' keeps both kinds of aim, keeps 'deployable' where Deploy applies (L403), and matches (EX) (L449, L453).

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 97, variation said to drop the correction-of-a-use coverage:

```
An explanatory aim requires a deployable account.
```

- reply line 98, variation said to keep the type fault:

```
An explanatory aim requires an account, or a corrected use, to be deployable.
```

- reply line 103, repair wording (the closing line's repair):

```
An explanatory aim requires an account to be deployable, whether the aim is that account or the correction of a use through it.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L403 "Deploy_{β,ℓ}(s,c,ξ;U) is met when s at ξ holds a representation of c" — found at L403 (written in Unicode, not LaTeX)
- L438 "Repair_{O,P}(ξ,ξ';Δ) ⟺ …" — found at L438 (Unicode)
- L449 `Account((c,p_c,t_c,Γ_c)) ∧ … ∧ Deploy_{β,ℓ}(s,c,ξ';U_c)` — found at L449 (Unicode)
- L453 "the declared use task for c" — found at L453
- L453 `ProducesVia(Δ,c,o;ξ,ξ')`, "an active route that runs from Δ to the repair of o contains the relevant binding of c" — found at L453 (Unicode)
- S20 "Once the explanation is rescued, the mistake shouldn't be able to creep back in" — found in the owner's words (S20)

### C28 · L471 · Part XII — The physical module; Retention fixed point

**The sentence** (as the brief gives it; found word for word in file 99 at L471):

> \(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 251): VARIES

```
C28: VARIES — F is monotone; C ⊆ F(C) is the invariant form; the greatest fixed point is the union of the sets D with D ⊆ F(D). (CT2)
```

- GLM (`s103_vary_glm_3.response.txt`, line 123): HOLDS

```
C28: HOLDS — merging lost the separately citable claims that L546 targets, "an invariant" broke the tie to (CT1)'s `z'∈C` (L466), and "pre-fixed" is false.
```

**To a checker:** yes: Mimo VARIES (rule 5); the readers differ (rule 7).

**Parked (S34):** no; no point of either reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 223–252)

*Points (digest):*

- Rival: '… the greatest fixed point is the union of the sets D with D⊆F(D). (CT2)': 'post-fixed sets' is not defined in the lines given; spelling out the class names the same sets; the three claims and the label stay.
- Break: 'C = F(C)' breaks (CT1) at L466, which asks only that states of C return into C, not that nothing outside returns in.
- Break: 'least fixed point' breaks the third clause itself (the union of post-fixed sets is the greatest of them), and L546 lists (CT2) among the claims a counterexample to which would rule the class out.
- Break: dropping 'F is monotone' leaves the union clause with nothing to stand on.
- Step 3: no fault; monotonicity is met (C⊆D makes 'returns into C' the stronger demand); L469 keeps the quantification from being vacuous.
- Note: the closing line gives the rival in plain Unicode ('C ⊆ F(C)', 'D ⊆ F(D)') where the fenced rival (reply line 228) is in LaTeX.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 228, rival offered as working (the closing line gives it in plain Unicode):

```
\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the greatest fixed point is the union of the sets \(D\) with \(D\subseteq F(D)\). (CT2)
```

- reply line 236, variation said to break (CT1) at L466:

```
\(F\) is monotone; \(C = F(C)\) is the invariant form; the union of post-fixed sets is the greatest fixed point. (CT2)
```

- reply line 242, variation said to break the third clause and L546:

```
\(F\) is monotone; \(C\subseteq F(C)\) is the invariant form; the union of post-fixed sets is the least fixed point. (CT2)
```

- described in prose, no wording written out: Dropping "F is monotone" (no wording written out): said to leave the union clause with nothing to stand on.

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L466 "\(\forall z\in C\ \forall i\in\operatorname{dom}T\ \forall\eta\in\operatorname{Exec}(\pi,z,i;\chi),\ \eta\text{ completes with }o\in T[i]\text{ and }z'\in C\)" — found at L466
- L546 "A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3 under their stated assumptions." — found at L546
- L469 "Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task." — found at L469

#### GLM (`s103_vary_glm_3.response.txt`, lines 110–124)

*Points (digest):*

- The sentence is a three-part mathematical claim tagged (CT2), and (CT2) is itself a counterexample target (L546).
- Merging the clauses entangles three separable claims; as a named target of L546 the flat triple lets each part be attacked or held on its own; no gain in content, a loss in citability.
- 'C ⊆ F(C) is an invariant' (dropping 'the invariant form') breaks the tie to (CT1), whose return condition is exactly z'∈C (L466).
- Replacing 'post-fixed' with 'pre-fixed' is false for F as defined (L471).
- Dropping 'F is monotone' leaves the third clause unsupported; monotonicity licenses the union claim.
- Fault sought: F is monotone as required; the powerset of states is complete, so the union of post-fixed sets is the greatest fixed point; L469 rules out the empty-execution reading.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 117, variation ('the invariant form' dropped), said to break the tie to (CT1):

```
C ⊆ F(C) is an invariant
```

- reply line 118, words replaced:

```
post-fixed
```

- reply line 118, replacement, said to be false for F as defined:

```
pre-fixed
```

- reply line 119, words dropped, said to leave the third clause unsupported:

```
F is monotone
```

- reply line 116, merged variation, said to entangle three separately citable claims:

```
F is monotone, so post-fixed sets C ⊆ F(C) are closed under union and their union is the greatest fixed point.
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L546 "A counterexample to the finite monotone claim, (I2), (O1), (T2), (CT2), or Arguments 1–3" — found at L546
- L466 `z'∈C` — found at L466 (Unicode)
- L471 "F(C) = states whose executions all complete and return into C" — found at L471 (LaTeX delimiters set aside)
- (the candidate) "the invariant form" — found at L471
- L469 "Execution families are nonempty on admitted inputs; deadlock is not a vacuous performance of the task." — found at L469

### C29 · L520 · Part XIV — The class collected

**The sentence** (as the brief gives it; found word for word in file 99 at L520):

> Account, from fidelity under change (E).

**Closing lines, as written:**

- Mimo (`s103_vary_mimo_3.response.txt`, line 279): FAILS

```
C29: FAILS — the gloss names only the fidelity conjuncts, though (E) also requires non-circular dependence and non-vacuity (L262; L255; L257) — Account, from fidelity under change, non-circular dependence and non-vacuity (E).
```

- GLM (`s103_vary_glm_3.response.txt`, line 138): HOLDS

```
C29: HOLDS — the bare tag lost L265's characterization, enumeration broke the list's pattern and L265, "the contract's edits" under-described L255, and "variation" touched the parked question of S34.
```

**To a checker:** yes: Mimo FAILS (rule 5); GLM holds, and argues directly against enumerating the conjuncts; the readers differ (rule 7).

**Parked (S34):** no; GLM mentions S34 only to set aside the word 'variation', which it says would risk taking a position on the parked question; neither reader proposes anything about what hard to vary covers.

#### Mimo (`s103_vary_mimo_3.response.txt`, lines 253–281)

*Points (digest):*

- Fault (FAILS): the list's pattern enumerates the sources exactly (R, L208, is glossed 'from fidelity and provenance'); (E) has five conjuncts (L262), and 'fidelity' names only the first group (L245: 'Together they are fidelity …'); non-circular dependence (L255) and non-vacuity (L257) are not fidelity, so the gloss names one of three groups and omits two. A reader might take 'fidelity under change' as a four-word name for (E), which the parenthetical would then repair; the list's own pattern forces the enumerating reading.
- Repair: 'Account, from fidelity under change, non-circular dependence and non-vacuity (E).' A rival that keeps the gloss, 'Account, from fidelity across the contract's changes (E)', keeps the same omission.
- Break: 'Account, from (E).' keeps the pointer but drops the description every other item of the list carries (L520).
- Break: 'Account, from fidelity under change (F1), (F2), (A).' breaks L526: the item must name the definition (E).

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 258, repair wording (the closing line's repair):

```
Account, from fidelity under change, non-circular dependence and non-vacuity (E).
```

- reply line 266, variation said to drop the description the other items carry:

```
Account, from (E).
```

- reply line 272, variation said to break L526:

```
Account, from fidelity under change (F1), (F2), (A).
```

- reply line 261, rival that keeps the gloss, said to keep the same omission:

```
Account, from fidelity across the contract's changes (E)
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L520 "Roles, from admitted edits (Part II). Kinds, from signatures (K). The respect of a question, from its query (Part III). Representation, from fidelity and provenance (R). Provenance, from physical history (Parts IV, XII)." — found at L520
- L526 (excerpt) "(F1), (F2), (A) depend on (O), (Q), (K). (E) depends on those." — found at L526
- L208 "\(\operatorname{Rep}_\ell(o,c)\iff\exists t\,[\operatorname{Faithful}_C(t:\operatorname{Org}_\ell(o)\to c)\land(\operatorname{Sel}(t)\lor\operatorname{Con}(t))]\)" — found at L208
- "from fidelity and provenance" (the item for R) — found at L520
- L262 "\(\text{(F1)}\land\text{(F2)}\land\text{(A)}\land\text{NonCircular}\land\text{NonVacuous}\)" — found at L262
- L245 "Together they are fidelity at every level the contract reaches" — found at L245

#### GLM (`s103_vary_glm_3.response.txt`, lines 125–140)

*Points (digest):*

- 'Account, from (E).': the tag fixes the extension but drops the characterization, whose words are earned: L265 'Every conjunct is a condition on how supplied relations behave under the changes in C'; 'under change' summarizes that, the theory's signature idea stated once.
- 'Account, from (F1), (F2), (A), non-circular dependence and non-vacuity.' is a list, not a gloss; it suggests the conjuncts are independent sources, against L265's single characterization, and breaks the pattern of the neighbouring entries, each of which names a source by sense, not by enumeration.
- '… from fidelity under the contract's edits (E).' narrows 'change': non-circular dependence speaks of deletions of components (L255), which are not edits in C, so it under-describes (E).
- '… from fidelity under variation (E).': 'variation' is a loaded word in this project (S20: 'A variation is a competitor'), and the owner has parked what hard to vary covers (S34); using it here risks taking a position on that parked question.
- Fault sought: 'fidelity' appears in two entries (R and this one); not equivocation, since transport faithfulness and (E)'s fidelity are both 'fidelity under change' in the sense of L265 and the tag fixes which. Consistent with Argument 6 (L596) and L526.

*Wordings, copied exactly from the reply (fence lines added here where the reply wrote the wording inline):*

- reply line 131, variation said to drop L265's characterization:

```
Account, from (E).
```

- reply line 132, variation (enumeration) said to break the list's pattern and L265:

```
Account, from (F1), (F2), (A), non-circular dependence and non-vacuity.
```

- reply line 133, variation said to under-describe (E) against L255:

```
Account, from fidelity under the contract's edits (E).
```

- reply line 134, variation said to touch the question parked by S34:

```
Account, from fidelity under variation (E).
```

*Quotations checked against file 99 (or, for the owner's words, against section 2 of the brief):*

- L265 "Every conjunct is a condition on how supplied relations behave under the changes in C" — found at L265
- L520 "Roles, from admitted edits (Part II)", "Representation, from fidelity and provenance (R)" — found at L520
- S20 "A variation is a competitor" — found in the owner's words (S20)
- L526 "(E) depends on those" — found at L526
- (the candidate) "fidelity under change" — found at L520


## Passages that name a candidate outside its own section (for the checkers, rule 5)

- **Standing notes.** Mimo's part 1 reply opens with a standing note (`s103_vary_mimo_1.response.txt`, line 1) on S23, S34, S20 and S28 that applies to C01–C12. GLM's part 2 reply opens with "A note on what counts as a variation" (`s103_vary_glm_2.response.txt`, lines 1–3) that applies to C13–C20 and bears directly on C19 and C20: a recasting that keeps every term and dependency does not show a sentence easy to vary.
- `s103_vary_mimo_1`, line 164 (in C07) names C08's measured port; line 174 (in C07) says C08 and C09 carry the same general clause as C07's replacement clause; line 196 (in C08) compares C08's second clause with C07's replacement clause; line 216 (in C09) says a variation would collapse the rule into C07's pattern; line 218 (in C09) says C08 and C09 have the same profile shape under (K).
- `s103_vary_mimo_1`, lines 256 and 262 (in C11) rely on C07 and C12; line 272 (in C12) says the contract index was already fixed at C04; line 284 (in C12) says "It" is carried from C11.
- `s103_vary_glm_1`, line 185 (in C08) relies on C10's sentence; line 249 (in C11) says the rival orphans C12's sentence ("It asks what its signature is.").
- `s103_vary_mimo_2`, line 67 (in C15) relies on C13's three loci.
- `s103_vary_mimo_3`, line 75 (in C23) says "structural map" (C25) is not defined in the lines given.

## Points that allege a defect, whatever the closing line (for the checkers)

Recorded here so that no such point is lost behind a closing line; each is given in full in its candidate's rows. Whether any shows a defect is for the checker.

- **C01**, Mimo: the sentence's work is the contrast, "a role, not new content", since the preceding words already say the classes are defined.
- **C02**, Mimo: "it" in "fidelity is what it is" can be read so that the clause does no work, and read as the transport it invites an unindexed reading of fidelity ("Readerly risk, not a forced failure").
- **C03**, Mimo: "Construction is a separate provenance" is loose against L193, where provenance belongs to a transport; "it" can be read as "a separate provenance". GLM (third rival) holds that construction is one of the three provenances.
- **C04**, Mimo: the typing clause is the sentence's only strict content, and dropping it breaks nothing.
- **C07**, Mimo: the replacement clause is inert ("Inertness, not contradiction"); GLM argues it ties the assignment to the component.
- **C08**, Mimo: the second clause, like C07's replacement clause, applies to any component; its discriminating partner is the first.
- **C09**, Mimo: under (K), C08 and C09 have the same profile shape, and L121 does not claim the families are distinct ("No failure").
- **C13**, GLM (set aside by GLM): "incompatible" does not say with what; Mimo's rival supplies the relatum.
- **C15**, Mimo: "is" is loose against L377, which gives the exposing a premise and a connection beyond the question.
- **C18**, Mimo: the text forces faithfulness to be the component and global conditions (L189), while the sentence's uses attribute (A) to a violation; GLM reads the sentence's "fidelity" as including (A).
- **C22**, GLM (set aside by GLM): "contribution" is used in two senses in the text (L305, L435).
- **C23**, Mimo: read as exhaustive, the definition would clash with the exclusion of a route "already at rest when the result occurred"; "operative result", "applicable relations" and "structural map" are not defined in the lines given (GLM likewise could not check the first two).
- **C24**, Mimo and GLM: the idiom "(K1) fails" for a biconditional; both read it as the condition being unmet.
- **C25**, Mimo: "the same transition" has no antecedent in the line; "operative deliberative rule" and "structural map" are not defined in the lines given (GLM likewise for the first).
- **C26**, Mimo: the unqualified "a premise" is to be read as one of Prem(u); a reader might take it more widely.
- **C27**, Mimo and GLM (FAILS): "to be deployable" governs both disjuncts, and Deploy is a relation on contents.
- **C29**, Mimo (FAILS): the gloss names only the fidelity conjuncts of (E); GLM argues the gloss names the source by sense and holds.

## Notes

- **File name.** Written to the task's path, `results/S103 Round 1 - reading/tabulation.md`, not to the reading rule's `results/S103 Round 1 - tabulation of the replies, before any ruling.md`; the difference is the orchestrator's to settle.
- **C14 and C18.** Both are held by both readers. C14 is listed as held (rule 6) and C18 is marked for a checker under rule 5's clause on doubt; the reasons are given above, in "Candidates held under both readers' attempts". The orchestrator may read either otherwise.
- **C27.** Mimo's section holds three wordings of the repair: the rival it calls "the repair" (reply line 200), the wording of its closing line (line 221), and a rival that keeps the fault (line 196). GLM's repair is a fourth wording. The checker has all four.
- **Markup in closing lines.** Mimo's closing lines for C25 and C28 give the rival with different markup from the fenced rival above them (C25 without the bold on "Reason use."; C28 in plain Unicode where the fence is LaTeX). Both are copied as written.
- **C19.** GLM names, in a parenthesis, the same words as Mimo's rival (without the full stop) and says they are a recasting, "not a variation".
- **Quotations.** Every quotation of file 99 or of the owner's words that either reader relies on was found. One was cited to a wrong line: GLM, C21, "it fails (F1)", cited as L267, stands at L269. GLM writes some formulas in Unicode rather than LaTeX (C22, C27, C28); their content matches the lines cited. GLM's two quotations given as S26's ("Physical possibility comes in only when something is instantiated or transformed") are Claude's sentence, which the owner quoted and answered "This is correct."; GLM's appeals to S20 and S23 at C17 are paraphrases, not quotations. No reply quotes a book.
- **Parked.** No candidate is parked (S34). The only mention of S34 on a candidate is GLM's at C29, where it declines the word "variation".
- **Nothing ruled.** Nothing here says whether any rival works as well, whether any variation breaks what the reader says it breaks, or whether any fault is shown. Those are the checkers' (rule 5), under the owner's words (rule 9).
