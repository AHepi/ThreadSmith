# Ruling: s90_xexam_atria_C, item 1, R13 (W35.2)

*A fresh Claude checker, 24 September 2026. It worked under the S90 rule, "S90 Parts - how they will be read, written before sending.md" and "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (rule 4 there: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list. It did not write the part briefs, and it wrote no ruling of batch 1 or batch 2.*

*File name.* The name the task asked for is 287 bytes long, over the file system's limit of 255. This file uses the short form that the committed rulings use.

*The reply.* `results/S90 Cross-examination - revision 2 draft - returns/parts/s90_xexam_atria_C.response.txt`. The task named the reply by its call label, and this is the file that label points to.
- Receipt: pass 2, accepted on attempt 6 of 6. Attempts 1–5 had status 0. Attempt 6 had status 200 with finish "stop" and 0 bad chunks.
- The sha256 is bd51b78593b3ac9e7d194d7f0b62e43e223f8c487d6e611a6118999d50d7a72f and matches the receipt. The md5 is 5efafef16046aa63c8cd736ea4c6d939.
- It has 1,227 words by `wc -w`, and END OF REPORT is its last line.
- The checker read all of the reply. It also read Mimo C's reply (sha256 9ea0342f…, which matches its receipt), because Mimo C's point 4 contests R13 as well (Parts rule 3).
- It opened no reasoning file and no other checker's ruling.

*Sources:*
- *the change list, md5 a5c92adc9f1e3806c0f9c6394cffde1e;*
- *the revised text ("file 13 draft 2"), md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11, md5 5e494c1095d920d128b9a79de378f923, read only;*
- *the part C brief, md5 2183faa5005b112347f484b6c8ace196;*
- *the S81 case book, md5 4f488d149e44669240d5db546c8e946a;*
- *the S89 case book, md5 b2e535777976a511935430bd089ba500;*
- *D3-T `final.md`, md5 6b211dea40d735abf50426e56344f161.*

## 1. The entry, its checkers' history, and earlier rulings

W35.2 is R13 (= R2-13). Its title is "Part IV: a constructed transport is violated, not surprised". It sits at file-11 L225 and revised L223, and it adds one sentence after s4. KIND: CLAIM. REASON WORD: clarification. Group C.

- **OLD:**

````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3).
````

- **NEW (as drafted):**

````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport, surprise only for a selected one: a constructed transport that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````

- **DECLARATION:** "Part IV now says that a constructed transport that fails at a pair of its contract is violated, that the failure is not surprise, and that a violation the system represents can be a recognized difficulty."
- **CHECK (its checkers' history):** "check 2, FIX. File 11 says a system is surprised and a transport is violated, never surprised; NEW reads "is violated, and the failure is not surprise". N18 Q3's Dov half stays watched (his transport need not be read as selected). Companion entry W35.4 added."
- **Cases at risk given in part C:** O23 and N18.
- **Earlier rulings:** none. Batch 1 and batch 2 contain no ruling on R12, R13, R14 or any W35 entry. A search for "R12", "R13", "R14" and "W35." in both batch files and in `S90 reading rulings/` found nothing.
- **The related entry, W35.1 (R12).** Its NEW keeps the expectation bullet "\(\operatorname{Ans}_S(\tau(a),\sigma(b))\)" and opens with "Let \(t\) be a transport with contract \(C\) and, where \(t\) is selected, history \(H\)". Its declaration reads "defines expectation and violation for every transport". Its REASON says: "The expectation keeps \(\operatorname{Ans}_S\): S is the organization the transport serves in this section, and constructed transports sit there too (L203)."

## 2. The replies' arguments

**Atria C, point 1 (R13: FALLS).** Task (c), with a (d) check:

> "R13's added sentence (line 223) reads: "Expectation and violation are defined for every transport, surprise only for a selected one …". But the definition it rests on (lines 217–221) fixes the expectation as "\(\operatorname{Ans}_S(\tau(a),\sigma(b))\)." Since \(\tau,\sigma\) are the transport \(t\)'s own translations, that expression is well typed only when \(t\)'s target organization is the simulation layer \(S\). Part IV says explicitly … "A physical system may hold selected transports at the primitive layer and constructed transports at the simulation layer," and (R)'s transports run from a carrier to a content. For a transport whose target is not \(S\), \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is undefined, so "defined for every transport" is false as written. … R13's sentence then turns a latent looseness into an explicit contradiction with unchanged text. *(d) check:* no verdict moves — in N18 both designers' transports are simulation-layer … *Repair:* "Expectation and violation are defined for every transport into the simulation layer, surprise only for a selected one," or replace \(\operatorname{Ans}_S\) with \(\operatorname{Ans}_E\) … I hold R13 to fall: its sentence is the false statement. R12 stands … but the same repair must touch it."

Its closing line: "R13: FALLS — "defined for every transport" contradicts the section's \(\operatorname{Ans}_S\) formula and Part IV's primitive-layer transports." In point 2 it adds that N18's fixed verdict is exactly the distinction R12–R14 declare.

**Mimo C, point 4 (closing line R13: STANDS, but the point contests the declaration under task (a)).** It says the declaration "omits the opening clause" "Expectation and violation are defined for every transport, surprise only for a selected one". It says that clause "largely restates R12's preamble change" but "inherits R12's defect (point 1)" and "is also false as written". Its repair is to add the clause to the declaration, scoped "(to the simulation layer)", and to have it "track" any repair of R12. Its point 1, on R12, makes Atria's typing argument: "Unless \(E = S\), \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) does not type-check."

**Quotations checked.** Every quotation the two replies rely on for R13 was found verbatim.
- Atria's "~203" and "~179" are file-11 line numbers. In the revised text the two sentences are at L201 and L177.
- Mimo's "(line 203)" for "A transport from an organization \(D\) to an organization \(E\)" is at revised L183.
- These are line references only. No wording differs.

## 3. The texts and the cases

**The typing point holds.**
- **Where Ans is defined.** Ans is the answer profile of an organization's query (Q, L144: \(\operatorname{Ans}_p(a,b)=\mathcal Q(D,a,b)\)).
- **What a transport's translations do.** In a transport \(t=(\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\) (L183–189), \(\tau\) and \(\sigma\) carry \(D\)'s edits and boundaries into \(E\). The text uses exactly this form in (A), L250: \(\operatorname{Ans}_E(\tau(a),\sigma(b))=\operatorname{Ans}_p(a,b)\).
- **So the expectation is typed only for transports into \(S\).** The expectation \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) (L219) is well formed only when \(t\)'s target is the simulation layer.
- **The text has transports that do not target \(S\):**
  - selected transports "at the primitive layer" (L201);
  - (R)'s carrier-to-content transports \(t:\operatorname{Org}_\ell(o)\to c\), selected or constructed (L205–211);
  - every Part V candidate transport \(D\to E\) (L231).
- **Violation is general.** "Fidelity fails at \((a,b)\)" (L220) is defined for any transport.

**The looseness is older than R13.** File 11 already had it in latent form. Its "Let \(t\) be selected on history \(H\)" did not exclude a selected carrier-to-content transport or a transport into \(P\). The section was read as being about \(S\) because of "\(S\) is where expectation lives" (L177), and W35.1's REASON says that is the intended scope. R13's sentence is the first place where the text *states* a scope, and the scope it states, "every transport", is wider than the formula it summarizes. On that point Atria is right. The sentence says the theory defines something it does not define. The repair is a matter of wording, and no case needs to move.

**Which repair.**
- **Replacing \(\operatorname{Ans}_S\) with \(\operatorname{Ans}_E\) is rejected here.** It would:
  - edit R12's bullet, not R13;
  - contradict L177 ("\(S\) is where expectation lives");
  - go against W35.1's stated reason for keeping \(\operatorname{Ans}_S\);
  - give an undeclared "expectation" to every Part V candidate transport and every carrier-to-content transport under (R), which is a new claim that nobody drafted or checked.
- **Narrowing the sentence to transports into the simulation layer is adopted.** It keeps the intended content, that the widening is by provenance: selected, constructed and declared transports into \(S\) all have an expectation and a violation. It also fits the unchanged texts:
  - Derivation 4's proof ties violation to expectation: "If there is no transport there is no expectation and hence no violation" (L576).
  - Derivation 10's \(t_0\) and \(t_1\) both run from \(P\) into a simulation layer (\(S_0\), \(S_1\)).
- **The words "the simulation layer" are used, not "\(S\)",** so that \(S_0\) and \(S_1\) are covered without a subscript.

**The cases.**
- **N18 (S89 book).**
  - Rhea's transport is her worked-out theory, a constructed transport whose queries are predictions, so it runs into the simulation layer.
  - Dov's transport is his copy of the village bridge's design, read as selected on that bridge's record (watched, as CHECK says). His "expected his bridge to be as trouble-free" is also a prediction, into the simulation layer.
  - Under the fixed wording both still have an expectation and a violation, so Q2's "went against what both expected" stands.
  - Rhea's failure is at a pair inside her contract. That is a violation and not surprise, so her grounds were contradicted (Q3, first half). Dov's large crowd is outside his \(H\). That is surprise, and nothing he had grounds for was contradicted (Q3, second half, still watched).
  - Q1 ("a problem for both") runs through the "recognized difficulty" clause, which the fix does not touch.
  - Between the drafted NEW and the fixed NEW, no mark moves. Atria's (d) finding agrees.
- **O23 (S81 book), "The seal was tight".** It turns on adding a dimension by measuring. It involves no expectation, violation or surprise, and the fix does not reach it.
- **O3.** Nadia predicts with a selected transport into the simulation layer, so W35.1's reading holds.
- **D3-T (`final.md`).** It turns on which designs survive the test (Derivation 3 and the survival condition). It has no expectation and no surprise, and it is not reached.
- **Derivations 4 and 10.** They are unchanged and stay true word for word.

**Mimo's declaration point.** The opening clause restates a claim that R12's declaration already makes. It is not a new undeclared claim against file 11. Once the clause carries a scope, though, R13's own declaration should state it, because each entry's declaration stands alone in layer 1 of the record. This ruling adds it.

## 4. Ruling: FIX

KIND stays CLAIM, and the REASON WORD stays clarification. OLD is unchanged.

- **NEW (corrected):**

````text
Whether the correspondence could have been otherwise at such a change is a fact about its population (Derivation 3). Expectation and violation are defined for every transport into the simulation layer, surprise only for a selected one: a constructed transport that fails at a pair of its contract is violated, and the failure is not surprise; a violation the system represents can be a recognized difficulty (Part X).
````

- **DECLARATION (corrected):** "Part IV now says that expectation and violation are defined for every transport into the simulation layer and surprise only for a selected one, that a constructed transport that fails at a pair of its contract is violated, that the failure is not surprise, and that a violation the system represents can be a recognized difficulty."
- **Reason, to go in the entry and be marked "after the cross-examination" (S90 Atria C point 1; Mimo C point 4).** The expectation \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is well typed only for a transport whose target is the simulation layer, as (A) at L250 shows. Part IV also has transports into the primitive layer (L201) and carrier-to-content transports under (R). So "every transport" said more than the formula defines. The sentence is narrowed to the scope that W35.1's REASON and L177 already give. No case moves: N18 holds as CHECK states it, and O23, O3 and D3-T are not reached.
- **Passed to R12's checker (not ruled here).**
  - R12's declaration, "defines expectation and violation for every transport", has the same overreach. It should read "for every transport into the simulation layer".
  - The Let-sentence or the expectation bullet may be scoped to match, for example "the **expectation**, for a transport into the simulation layer, is …".
  - If R12 is instead repaired with \(\operatorname{Ans}_E\), this ruling's NEW must be revisited.
  - R14 (W35.4) is not affected.
