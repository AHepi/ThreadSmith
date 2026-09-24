# Ruling: s90_xexam_mimo_C, item 1, R12 (W35.1)

*A fresh Claude checker, 24 September 2026. It works under the S90 rule as extended by "S90 Parts - how they will be read, written before sending.md" (rule 3), and under the rerun note "S90 and S87 - seven calls rerun after the container restart - written before sending.md" (ruling 4: the pass-2 reply stands where the pass-1 reply would have stood). This checker did not draft, assemble or check the change list and did not write the part briefs.*

*The call counts. Pass 2, attempt 1 of 1: status 200, finish "stop", 0 bad chunks, accepted. END OF REPORT is on the last line. The reply's sha256 is 9ea0342fa8d813c269086400a6be74deaa4cecfdc372c9857faaabe1c954eb90 (md5 6e2307cd1d94caf8bc5d19363a060b1c), which matches the receipt. It is 1,321 words by `wc -w`.*

*Sources:*
- *change list md5 a5c92adc9f1e3806c0f9c6394cffde1e (as at 587eebf; no later commit touches it);*
- *revised text `tests/Revision 2 - file 13 draft 2, theory text, as sent for cross-examination.md`, md5 9aecf2f30ce0b4523606b2b8409fdf37;*
- *file 11 md5 5e494c1095d920d128b9a79de378f923, read only;*
- *S81 book md5 4f488d149e44669240d5db546c8e946a; S89 book md5 b2e535777976a511935430bd089ba500; D3-T `final.md`.*

*Map (part-rule table): "R12 | W35.1 | C11 | C | 219–223 | 217–221 | CLAIM | N18".*

*Earlier rulings.* Neither batch 1 (Mimo A1, Mimo A2, Atria B1) nor batch 2 (Atria A2, Mimo B1) rules R12, W35.1 or C11. No reply outside part C mentions R12. So there is nothing to reconcile. The other reply to part C (Atria C) contests the same point, and it is stated in section 2 as well.

## 1. The entry and its checkers' verdict

W35.1, "Part IV: expectation and violation for every transport; surprise kept for selected ones".
- Group C, item W35 (b′).
- Part IV, "Expectation, surprise, violation". File-11 L219–223, revised L217–221. L221–222 are carried unchanged inside the OLD block.
- REASON WORD: clarification. KIND: CLAIM.

**OLD:**
````text
Let \(t\) be selected on history \(H\) with contract \(C\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation at \((a,b)\notin H\).
````

**NEW:**
````text
Let \(t\) be a transport with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation of a selected transport at \((a,b)\notin H\).
````

**DECLARATION:** "Part IV now defines expectation and violation for every transport, and keeps surprise for a violation of a selected transport at a pair outside its history."

**Checkers' verdict (CHECK):** "check 2, SOUND. Widening violation leaves L227's selection response speaking of an H that a constructed transport lacks; the companion entry W35.4 fixes that. The diff shows two hunks for this one entry (L219 and L223)."

**The drafter's REASON on this point:** "The expectation keeps \(\operatorname{Ans}_S\): S is the organization the transport serves in this section, and constructed transports sit there too (L203)." So the drafter meant every *provenance* of a transport that serves \(S\), not every transport whatever its target.

**CASES AT RISK:**
- O3 holds.
- N18: toward on Q2.
- O5, O11, O24 and O48 are untouched.

**Companion entries:**
- W35.2 (R13) adds at L223: "Expectation and violation are defined for every transport, surprise only for a selected one: …".
- W35.4 (R14) types L225's selection response to a selected transport.

## 2. The replies' arguments

**Mimo C, point 1** (closing line: "R12: FALLS — expectation \(\operatorname{Ans}_S\) is not defined for every transport as the declaration claims"):

> Violation is indeed general — "a **violation** occurs when fidelity fails at \((a,b)\)" (line 220) — since fidelity (F1)–(F2) is defined for any transport \(D \to E\). But the expectation (line 219) is "\(\operatorname{Ans}_S(\tau(a),\sigma(b))\)": the answer profile of the simulation layer \(S\). In a transport \(t = (\pi,\tau,\sigma,\lambda)\) from \(D\) to \(E\), the edit-translation \(\tau(a)\) is an edit of \(E\). […] Unless \(E = S\), \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) does not type-check. […] So the expectation is well-defined only for transports whose target is \(S\) […], and the declaration's "for every transport" is false.
>
> The old preamble ("Let \(t\) be selected on history \(H\)") was implicitly confined to the selected \(P\)-to-\(S\) transport, where \(E = S\). The new preamble removes the restriction without adjusting the definition.
>
> **Repair.** Either restrict the declaration ("Part IV now defines expectation and violation for every transport to the simulation layer") or change the expectation to \(\operatorname{Ans}_E(\tau(a),\sigma(b))\), using the target organization's own answer profile.

The same reply's point 4 carries the defect into R13's L223 sentence. That point belongs to R13's checker and is not ruled here.

**Atria C, point 1**, the other reply to the same part (closing lines: "R12: STANDS", "R13: FALLS"). It makes the same typing point: "that expression is well typed only when \(t\)'s target organization is the simulation layer \(S\)". It adds that (R)'s transports "run from a carrier to a content". It offers the same two repairs, "every transport into the simulation layer" or \(\operatorname{Ans}_E\). It then puts the fall on R13: "R12 stands, because its declaration is satisfied and its setup line is still contextually scoppable — but the same repair must touch it."

**Quotations checked (rule 8).**
- Revised L217 (the new preamble), L219 (the expectation), L220 (the violation) and L223 ("Expectation and violation are defined for every transport") are all found as quoted. Mimo gives the preamble as "lines 217–218", but it is one line, L217.
- The declaration is quoted correctly, though the reply stops before its surprise clause.
- \(\operatorname{Ans}_p(a,b)=\mathcal Q(D,a,b)\) is found at revised L144 (Part III, (Q)).
- "A transport from an organization \(D\) to an organization \(E\)" is found at revised **L183**, not at line 203 as Mimo says. Revised L203 is the heading "Representation is derived".
- Atria's "S is where expectation lives" is at revised L177 (file-11 L179). Its sentence on selected and constructed transports is at revised L201 (file-11 L203).
- Mimo's phrase "the selected \(P\)-to-\(S\) transport" is **not in file 11**. It is the reply's reading of the context: see section 3.

## 3. The texts, and the cases

**The typing point is right.**
- The theory writes \(\operatorname{Ans}_X\), for an organization \(X\), as a query evaluated on \(X\) at \(X\)'s own edits and boundaries. The pattern is (A) at L250, \(\operatorname{Ans}_E(\tau(a),\sigma(b))\), read with (Q) at L144.
- For a transport \(D\to E\), \(\tau(a)\) is an edit of \(E\) and \(\sigma(b)\) is a boundary of \(E\) (L183–189).
- So \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) has a value only when \(t\)'s target is \(S\). \(S\) is also where the query comes from: its queries "are predictions" (L177).
- Many transports in the theory do not go to \(S\):
  - (R)'s carrier-to-content transports \(t:\operatorname{Org}_\ell(o)\to c\) (L208);
  - a Part V candidate's transport from \(D\) to \(E\) (L231);
  - any declared transport between two other organizations.
- For these, the expectation clause names nothing. The declaration's "defines expectation … for every transport" is therefore false as written. Its violation half is true, since fidelity (F1)–(F2) is stated for any transport.

**How much of this R12 introduces.**
- File 11's "Let \(t\) be selected on history \(H\)" did not name a target either. (R)'s selected carrier-to-content transports were already within its words. So the looseness is latent in file 11, and Mimo's "implicitly confined to the selected \(P\)-to-\(S\) transport" is a reading, not a quotation.
- That reading is supported:
  - L177 says "\(S\) is where expectation lives".
  - Derivation 10's surprised transport \(t_0\) goes from the primitive layer into a simulation layer \(S_0\), and so does its constructed \(t_1\) (L614–620). \(S_0\) "expects nothing there and is violated".
  - Derivation 4's proof reads violation through expectation: "If there is no transport there is no expectation and hence no violation" (L576).
- R12 does two things that turn the latent looseness into a stated error:
  - It drops "selected", so the preamble now takes in declared and constructed transports of every target. That includes every Part V candidate's transport.
  - Its declaration states the universal outright.
- The drafter's REASON already restricts the entry to transports that serve \(S\). The fault is that neither NEW nor the declaration says so. Atria's ground for letting R12 stand, "contextually scoppable", holds for the text's L177 context, but not for the declaration, which the record carries on its own. Atria itself says "the same repair must touch it".

**Repairs weighed.**
- **\(\operatorname{Ans}_E\) is not adopted**, for three reasons:
  - It needs a query that a general \(E\) does not supply. In (A) the query is a question's \(\mathcal Q\), held fixed, and this section has no question. \(S\) is the organization whose queries are given (L177).
  - It contradicts unchanged L177: "\(S\) is where expectation lives".
  - It is a larger change of claim than the defect needs.
- **Scoping only the expectation bullet is not adopted.** That would keep violation and surprise for every transport. It would leave surprise defined for selected transports that have no expectation, against Derivation 4's proof (L576) and Derivation 10's "expects … and is violated". It would also stretch "violation" to every Part V candidate, beyond the REASON's aim ("a constructed theory that fails").
- **Naming the target in the preamble is adopted.** It is Mimo's first repair and Atria's repair for R13. It states the drafter's own premise and types the expectation. The entry keeps its whole gain: every provenance, constructed included, has expectation and violation, and surprise stays with selected transports.
  - Against file 11, it names the target that file 11 left to context. A selected transport not going to \(S\) had no typed expectation in file 11 either, so nothing that was defined is lost.
  - Derivation 4's claim is an only-if and stays true. Derivation 3's consequence ("It is also why surprise is possible", L570) and Derivation 10 read unchanged.
  - Derivation 10's \(S_0\) and \(S_1\) are simulation layers, so "the simulation layer \(S\)" covers them as it already covers \(\operatorname{Ans}_S\) there.
  - The comma after \(S\) keeps "with contract \(C\)" attached to \(t\).

**Cases, worked on the fixed wording.**
- **N18 (S89): holds, as drafted.**
  - Rhea's worked-out theory is a constructed transport to her simulation layer. Her expectation (steady under the crowd) is \(\operatorname{Ans}_S\) at the translated crowd edit. The crowd lies inside her contract, so fidelity fails at a pair of \(C\). That is a violation, and not surprise.
  - Dov's copy, read as selected on the village bridge's record of a few dozen people, also goes to his simulation layer. His expectation is that the bridge will be trouble-free. The large crowd is \((a,b)\notin H\), so it is surprise.
  - Q2: against both expectations. Q3: Rhea's grounds were contradicted, and nothing Dov had grounds for was. The Dov half stays watched, as in W35.2, on reading his transport as selected. Naming the target does not touch that.
- **O3 (S81): holds.** Nadia's next-card prediction is a selected transport to her simulation layer, so "often surprised" stays surprise. The verdict turns on construction.
- **Not reached:**
  - O11 and O48 (the S90 brief's list for C11), and O5 and O24, raise no expectation.
  - D3-T (O76) turns on Derivation 3's population and survival, not on expectation or surprise.
  - O23 belongs to R13.
- No other case in the S81 or S89 books turns on the target of an expecting transport. The only uses of "expectation", "violation" and "surprise" in the revised text are at L177, L215–225, L570–578 and L618.

## 4. Ruling: FIX

**The argument partly succeeds.**
- It succeeds on the main point. The expectation \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is typed only for a transport to \(S\), so "defines expectation … for every transport" is false.
- It overstates two things. File 11 did not state a \(P\)-to-\(S\) restriction; it left the target to context and had the same latent gap. And the \(\operatorname{Ans}_E\) alternative is not a well-defined repair.

**The fix** names the target in the preamble and in the declaration. It keeps everything else in the entry.

- **OLD:** unchanged, file-11 L219–223 as above.
- **NEW:**
````text
Let \(t\) be a transport to the simulation layer \(S\), with contract \(C\) and, where \(t\) is selected, history \(H\). For an edit–boundary pair \((a,b)\in C\) actually occurring:

- the **expectation** is \(\operatorname{Ans}_S(\tau(a),\sigma(b))\);
- a **violation** occurs when fidelity fails at \((a,b)\);
- **surprise** is a violation of a selected transport at \((a,b)\notin H\).
````
- **KIND:** CLAIM (unchanged). **REASON WORD:** clarification (unchanged).
- **DECLARATION:**
````text
Part IV now defines expectation and violation for every transport to the simulation layer, whatever its provenance, and keeps surprise for a violation of a selected one at a pair outside its history.
````
- **For the CHECK field and the list of what the checks changed (after the cross-examination):** "S90, Mimo part C, R12 FALLS (Atria part C makes the same typing point but rules R12 STANDS and R13 FALLS); fresh checker FIX after the cross-examination. The preamble reads 'a transport to the simulation layer \(S\), with contract \(C\)', since \(\operatorname{Ans}_S(\tau(a),\sigma(b))\) is typed only when \(t\)'s target is \(S\). The declaration reads 'for every transport to the simulation layer, whatever its provenance'. The \(\operatorname{Ans}_E\) alternative is not adopted: a general \(E\) supplies no query, and L177 keeps expectation at \(S\)."
- **What is lost:** the unscoped "for every transport", which was false for expectation.
- **What is gained:**
  - The expectation is well typed wherever the section defines it.
  - The drafter's premise ("S is the organization the transport serves in this section") is now in the text.

**Conflicts with other entries.**
- **W35.2 (R13), which is not ruled here.** Its L223 clause "Expectation and violation are defined for every transport, surprise only for a selected one" has to follow this fix, as "… for every transport to the simulation layer, surprise only for a selected one". Both replies propose that repair for R13. This is passed to R13's checker.
- **W35.4 (R14):** unaffected. "The history \(H\) of a selected transport" still has a referent.
- **W35.3 (R34):** unaffected. It does not use "violation".
- No other entry has an OLD in L219–223.
