# 02 Organizations and their changes

*Home Part: Part II. Units shown: 66; units touched: 27; changes placed here: 52; records shown here in full under their home sentence: 51; pointer lines: 28; vocabulary lines: 24; records in blocks: 7. Statuses of the records shown here in full: applied 35, not applied 2, declined 5, superseded 8, open for the owner 0, unknown 1.*

- [Part II · Opening of the Part · line 81 · 0 records](#sec-L81-81)
- [Part II · Organizations · lines 83–105 · 5 records](#sec-L83-105)
- [Part II · Roles are defined, not supplied · lines 107–109 · 4 records](#sec-L107-109)
- [Part II · Kinds are edit-signatures · lines 111–127 · 34 records](#sec-L111-127)
- [Part 0 · Grievances, anticipated / 1. "Without declared kinds you cannot tell a cause from a correlation." · line 37 · 4 records](#sec-L37-37)
- [Part 0 · Grievances, anticipated / 2. "So this is operationalism: a thing is what you can do to it." · line 39 · 4 records](#sec-L39-39)
- [Part 0 · Grievances, anticipated / 11. "Kinds exist. A rule is not a cause." · line 57 · 5 records](#sec-L57-57)
- [Part XVI · 1. Kind preservation needs no condition of its own · lines 552–558 · 13 records](#sec-L552-558)
- [Not in the latest text, with no section: Part II · 6 changes, 7 records](#rest-II)

<a id="sec-L81-81"></a>
## Part II — Organizations and their changes · Opening of the Part · line 81

<a id="L81-s1"></a>
#### L81.s1 · heading · line 81 · no change recorded
> # Part II — Organizations and their changes

<a id="sec-L83-105"></a>
## Part II — Organizations and their changes · Organizations · lines 83–105

<a id="L83-s1"></a>
#### L83.s1 · heading · line 83 · no change recorded
> ## Organizations

<a id="L85-s1"></a>
#### L85.s1 · line 85 · no change recorded
> An organization is

<a id="L87-s1"></a>
#### L87.s1 · display · lines 87–89 · no change recorded
> \[
> D=(V,(X_v)_{v\in V},J,B,A,L).
> \]

<a id="L91-s1"></a>
#### L91.s1 · line 91 · no change recorded
> \(V\) is a set of ports, each with a nonempty value domain \(X_v\).

<a id="L91-s2"></a>
#### L91.s2 · line 91 · no change recorded
> A valuation is an element of \(X_D=\prod_v X_v\).

<a id="L91-s3"></a>
#### L91.s3 · line 91 · no change recorded
> \(J\) indexes components; each component \(j\) has a footprint \(V_j\subseteq V\).

<a id="L91-s4"></a>
#### L91.s4 · line 91 · no change recorded
> \(B\) is a set of boundary conditions.

<a id="L91-s5"></a>
#### L91.s5 · line 91 · no change recorded
> \(A\) is a set of admitted edits, closed under a partial associative composition with identity \(1\).

<a id="L91-s6"></a>
#### L91.s6 · line 91 · no change recorded
> For each \(j\), edit \(a\), and boundary \(b\), the interpretation supplies

<a id="L93-s1"></a>
#### L93.s1 · display · lines 93–95 · no change recorded
> \[
> L_j(a,b)\subseteq\prod_{v\in V_j}X_v .
> \]

<a id="L97-s1"></a>
#### L97.s1 · line 97 · no change recorded
> The compatible valuations are

<a id="L99-s1"></a>
#### L99.s1 · display · lines 99–101 · no change recorded
> \[
> \operatorname{Sol}_D(a,b)=\{z\in X_D:\forall j\in J,\ z|_{V_j}\in L_j(a,b)\}. \tag{O}
> \]

<a id="L103-s1"></a>
#### L103.s1 · line 103 · no change recorded
> A deleted component imposes the full relation on its ports.

<a id="L103-s2"></a>
#### L103.s2 · line 103 · no change recorded
> An edit that sets a port replaces the component assigning that port; it does not add an equation beside an incompatible one.

<a id="L103-s3"></a>
#### L103.s3 · line 103 · no change recorded
> A changed rule is a changed component.

<a id="L105-s1"></a>
#### L105.s1 · line 105 · 4 changes, 5 records
> Values of ports may be paths, functions, fields, mathematical structures or histories.

- **CH-0250** · 1 record · applied · form only
  - **B-76** · S76 · edit · applied · wording not in the latest text · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 122 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L122 s1 -> f11 L107 s1
    - Before:
      > Values of ports may be paths, functions, fields, proofs, or histories.
    - After:
      > Values of ports may be paths, functions, fields, proofs or histories.
    - Old wording:
      > proofs, or
    - New wording:
      > proofs or
- **CH-0635** · 1 record · applied
  - **D-54** · S95 · edit · applied · wording not in the latest text · written against: draft 5, line 105 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[53]; line 105; swap; LISTED
    - Before:
      > Values of ports may be paths, functions, fields, proofs or histories.
    - After:
      > Values of ports may be paths, functions, fields, mathematical arguments or histories.
    - Old wording:
      > fields, proofs or histories
    - New wording:
      > fields, mathematical arguments or histories
- **CH-1061** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1061)
  - **D-519** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 43 (section: Proofs and arguments)
    - Before:
      > *Proof.*
    - After:
      > *Why this and not its denial.*
- **CH-1001** · 2 records · superseded, applied · also at: [L49.s3](07%20Exact%20constructions%20%28Part%20VII%29.md#L49-s3), [L49.s4](07%20Exact%20constructions%20%28Part%20VII%29.md#L49-s4), [L343.s9](07%20Exact%20constructions%20%28Part%20VII%29.md#L343-s9)
  - **D-899** · S96 · recommendation · superseded · wording not in the latest text · written against: repaired copy, line 105 · carried by: none · source: results/S96 Cross-examination - repaired copy - returns/s96_xexam_mimo_1.response.txt — finding 7, proposed wording (code block 11); ruling 'mimo 1 7' in results/S96 Reading of the replies.md, section 3
    - Before:
      > Values of ports may be paths, functions, fields, mathematical arguments or histories.
    - After:
      > Values of ports may be paths, functions, fields, mathematical constructions or histories.
  - **D-428** · S97 · edit · applied · wording stands · written against: repaired copy, line 105 · carried by: latest text · source: tests/S96 Repair - scripts/replacements_stage3.json — entries[21]; line 105; group X; ruling: mimo 1 7
    - Before:
      > Values of ports may be paths, functions, fields, mathematical arguments or histories.
    - After:
      > Values of ports may be paths, functions, fields, mathematical structures or histories.
    - Old wording:
      > mathematical arguments or histories.
    - New wording:
      > mathematical structures or histories.

<a id="L105-s2"></a>
#### L105.s2 · line 105 · no change recorded
> Cyclic constraints are admitted.

<a id="L105-s3"></a>
#### L105.s3 · line 105 · no change recorded
> Several solutions remain several.

<a id="sec-L107-109"></a>
## Part II — Organizations and their changes · Roles are defined, not supplied · lines 107–109

<a id="L107-s1"></a>
#### L107.s1 · heading · line 107 · 2 changes, 2 records
> ## Roles are defined, not supplied

- **CH-0636** · 1 record · applied
  - **D-55** · S95 · edit · applied · wording stands · written against: draft 5, line 107 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[54]; line 107; swap; LISTED
    - Before:
      > ## Roles are derived
    - After:
      > ## Roles are defined, not supplied
- **CH-1127** · 1 record · superseded · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1127)
  - **D-665** · S95 · recommendation · superseded · written against: draft 5 · carried by: none · source: tests/S95 Scrub - vocabulary, proposed.md — section 2.4, table row at file line 87; sceptic's row 32
    - Before:
      > "Roles are derived"; "Representation is derived" (section titles)
    - After:
      > "Roles are defined, not supplied"; "Representation is defined, not supplied"

<a id="L109-s1"></a>
#### L109.s1 · line 109 · no change recorded
> No role assignment is supplied.

<a id="L109-s2"></a>
#### L109.s2 · line 109 · no change recorded
> A port \(v\) is an **input** under \(A\) when \(A\) contains an edit that sets \(v\) directly.

<a id="L109-s3"></a>
#### L109.s3 · line 109 · no change recorded
> A port is an **output** of component \(j\) when its value is determined by \(L_j\) given the other ports of \(V_j\) across \(B\).

<a id="L109-s4"></a>
#### L109.s4 · line 109 · 1 change, 2 records
> A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below).

- **CH-1003** · 2 records · superseded, applied
  - **D-898** · S96 · recommendation · superseded · wording not in the latest text · written against: repaired copy, line 109 · carried by: none · source: results/S96 Cross-examination - repaired copy - returns/s96_xexam_mimo_1.response.txt — finding 6, proposed wording (code block 10); ruling 'mimo 1 6' in results/S96 Reading of the replies.md, section 3
    - Before:
      > A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports.
    - After:
      > A port \(v\) is an **observation** when some component \(j\) has \(v\in V_j\) and \(A\) contains an edit \(a\) and a boundary \(b\) with \(L_j(a,b)\neq L_j(1,b)\), while \(\{z(v):z\in\operatorname{Sol}_D(a,b)\}=\{z(v):z\in\operatorname{Sol}_D(1,b)\}\).
  - **D-429** · S97 · edit · applied · wording stands · written against: repaired copy, line 109 · carried by: latest text · source: tests/S96 Repair - scripts/replacements_stage3.json — entries[22]; line 109; group X; ruling: mimo 1 6
    - Before:
      > A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports.
    - After:
      > A port is an **observation** when \(A\) contains an edit that alters the relation reporting it without altering what it reports, that is, when the component assigning it has a measurement's signature (below).

<a id="L109-s5"></a>
#### L109.s5 · line 109 · no change recorded
> The direction of an organization is a consequence of which edits it admits, not a stipulation about which way an equation is read.

<a id="sec-L111-127"></a>
## Part II — Organizations and their changes · Kinds are edit-signatures · lines 111–127

<a id="L111-s1"></a>
#### L111.s1 · heading · line 111 · no change recorded
> ## Kinds are edit-signatures

<a id="L113-s1"></a>
#### L113.s1 · line 113 · no change recorded
> Fix an organization \(D\) and a contract \(C\subseteq A\times B\) (Part III).

<a id="L113-s2"></a>
#### L113.s2 · line 113 · no change recorded
> The **signature** of component \(j\) on \(C\) is

<a id="L115-s1"></a>
#### L115.s1 · display · lines 115–117 · no change recorded
> \[
> \operatorname{sig}_C(j)=\{(a,b,L_j(a,b)):(a,b)\in C\}. \tag{K}
> \]

<a id="L119-s1"></a>
#### L119.s1 · line 119 · 3 changes, 3 records
> Two components \(j,j'\) are **of one kind on \(C\)** when there is a bijection of their footprints under which \(\operatorname{sig}_C(j)\) and \(\operatorname{sig}_C(j')\) coincide.

- **CH-0480** · 1 record · superseded · also at: [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-86** · S90 · recommendation · superseded · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923), line 121 · carried by: none · source: tests/Revision 2 - change list, draft of 23 September.md — change list draft 1 (git 12e73da), held placeholder "W19 (held) — Derivation 2, with the sentence after (K), Derivation 10 and W10(b) (held under D2)", FILE-11 LINE 121, 554, 620; replaced in change list draft 2 (587eebf) by the drafted entries C-10 (W19.1), C-62 (W19.2), C-66 (W19.3 + W10(b).1)
    - Before: *(nothing: an addition)*
    - After:
      > [no wording given] held under D2: nothing drafted; the placeholder names the S88 candidate wordings then in view for file-11 lines 121, 554, 620
- **CH-0486** · 1 record · declined · also at: [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-112** · S90 · recommendation · declined · written against: file 13 draft 2 (as sent), theory text (md5 9aecf2f30ce0b4523606b2b8409fdf37), line 119 · carried by: none · source: results/S90 reading rulings/ruling s90_xexam_mimo_A1 R08.md — S90 ruling R08 (W19.1): the reply's first repair (s90_xexam_mimo_A1 point 1), refused (batch 1)
    - Before: *(nothing: an addition)*
    - After:
      > [no wording given] move the two new sentences after (K) to Part V, immediately after the transport t=(π,τ,σ,λ) is defined
- **CH-1254** · 1 record · not applied · also at: [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **E-36** · S93 · recommendation · not applied · written against: file 13 draft 4, theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17), line 119 · carried by: none · source: tests/Revision 2 - change list, draft of 23 September.md — change list, "Carried forward after S93", "Findings for later entries", item "Classes across candidates"; ruling S93 X03 (W19.1), "Findings for later entries", finding 3
    - Before: *(nothing: an addition)*
    - After:
      > [no wording given] if a later revision wants classes of components across candidates, state the relation's domain (components of candidates with transports from one \(D\), read on one \(C\)) and its transitivity, as a CLAIM

<a id="L119-s2"></a>
#### L119.s2 · line 119 · 5 changes, 8 records
> A kind is an equivalence class of components under this relation.

- **CH-0411** · 4 records · superseded, applied · also at: [L119.s5](#L119-s5)
  - **B-264** · S88 · recommendation · superseded · wording not in the latest text · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md), line 121 · carried by: none (superseded by the settled sentence after (K), S88 F1 change 2) · source: results/S88 Claude's checks of the three defects/02 Derivation 2 and non-circular dependence.md — §1.7, 'Two supporting edits', After (K) (line 169): one sentence added after F11 L121
    - Before:
      > A kind is an equivalence class of components under this relation.
    - After:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivations 1 and 2 use kinds in this sense.
    - New wording:
      > A kind is an equivalence class of components under this relation. A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivations 1 and 2 use kinds in this sense.
  - **B-280** · S88 · recommendation · applied · wording not in the latest text · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md), line 121 · carried by: verbatim in: draft 2 to draft 4; carried as change-list entry W19.1, whose NEW text (as fixed later) is verbatim in: draft 5 · source: results/S88 Reading of Mimo's reply in three parts, and the settled positions.md — F1, final repair wording, change 2, the sentence after (K), inserted in F11 L121 after sentence 2 (lines 134-138) · linked (not joined): tests/Revision 2 - change list, draft of 23 September.md#W19.1
    - Before:
      > A kind is an equivalence class of components under this relation.
    - After:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - New wording:
      > A kind is an equivalence class of components under this relation. A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
  - **C-72** · S90 · edit · superseded · wording not in the latest text · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923), line 121 · carried by: file 13 draft 2 (as sent) · source: tests/Revision 2 - change list, draft of 23 September.md — change list entry W19.1, OLD/NEW as in change list draft 2 (git 587eebf); replaced in change list draft 3; the draft-5 wording is C-10; carried as S90 part A1 R08
    - Before:
      > A kind is an equivalence class of components under this relation.
    - After:
      > A kind is an equivalence class of components under this relation. A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
  - **C-10** · S93 · edit · applied · wording not in the latest text · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923), line 121 · carried by: file 13 draft 5 · source: tests/Revision 2 - change list, draft of 23 September.md — change list draft 5, entry W19.1 ("The sentence after (K): kinds across two candidates"), STATUS applied, KIND CLAIM, FILE-11 LINE 121; wording first in change list draft 5 (8816fcf)
    - Before:
      > A kind is an equivalence class of components under this relation.
    - After:
      > A kind is an equivalence class of components under this relation. For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV). A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
- **CH-0467** · 1 record · superseded · also at: [L119.s3](#L119-s3)
  - **C-73** · S90 · edit · superseded · wording not in the latest text · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923), line 121 · carried by: file 13 draft 3; file 13 draft 4 · source: tests/Revision 2 - change list, draft of 23 September.md — change list entry W19.1, OLD/NEW as in change list draft 3 and change list draft 4 (git 99e9cd0, 3f7c3ab); replaced in change list draft 5; the draft-5 wording is C-10; carried as S93 part F X03
    - Before:
      > A kind is an equivalence class of components under this relation.
    - After:
      > A kind is an equivalence class of components under this relation. For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV). A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
- **CH-0480** · 1 record · superseded · also at: [L119.s1](#L119-s1), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-86** · S90 · recommendation · superseded · shown in full under [L119.s1](#L119-s1)
- **CH-0486** · 1 record · declined · also at: [L119.s1](#L119-s1), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-112** · S90 · recommendation · declined · shown in full under [L119.s1](#L119-s1)
- **CH-1254** · 1 record · not applied · also at: [L119.s1](#L119-s1), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **E-36** · S93 · recommendation · not applied · shown in full under [L119.s1](#L119-s1)

<a id="L119-s3"></a>
#### L119.s3 · line 119 · 11 changes, 12 records
> For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\pi\) translates valuations, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV).

- **CH-0480** · 1 record · superseded · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-86** · S90 · recommendation · superseded · shown in full under [L119.s1](#L119-s1)
- **CH-0560** · 1 record · superseded
  - **C-188** · S90 · recommendation · superseded · wording not in the latest text · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923), line 121 · carried by: none · source: tests/Revision 2 - change list, draft of 23 September.md — change list draft 5, "Findings carried forward", Part II uses the notation of Parts IV and V before they introduce it (W19.1, read in place): a pointer "would close it", left for X1; closed after the S90 cross-examination by W19.1's typing sentence; wording taken instead, or the related change: C-73
    - Before: *(nothing: an addition)*
    - After:
      > (Parts IV and V)
- **CH-0467** · 1 record · applied · also at: [L119.s2](#L119-s2)
  - **C-93** · S90 · recommendation · applied · wording not in the latest text · written against: file 13 draft 2 (as sent), theory text (md5 9aecf2f30ce0b4523606b2b8409fdf37), line 119 · carried by: file 13 draft 3; file 13 draft 4; file 13 draft 5 · source: results/S90 reading rulings/ruling s90_xexam_mimo_A1 R08.md — S90 ruling R08 (W19.1) on s90_xexam_mimo_A1 point 1: FIX (batch 1); the wording as applied in file 13 draft 3 (entry W19.1, C-73); read off the line diff file 13 draft 2 (as sent) -> file 13 draft 3 at line 119
    - Before:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense.
    - After:
      > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV).
- **CH-0486** · 1 record · declined · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-112** · S90 · recommendation · declined · shown in full under [L119.s1](#L119-s1)
- **CH-0487** · 1 record · declined
  - **C-113** · S90 · recommendation · declined · wording not in the latest text · written against: file 13 draft 2 (as sent), theory text (md5 9aecf2f30ce0b4523606b2b8409fdf37), line 119 · carried by: none · source: results/S90 Cross-examination - revision 2 draft - returns/parts/s90_xexam_mimo_A1.response.txt — s90_xexam_mimo_A1 point 1, second repair (a gloss inline); ruling R08 (W19.1) inserted a typing sentence in Part IV's and Part V's own words instead (batch 1); the checker's wording is C-93
    - Before: *(nothing: an addition)*
    - After:
      > …through \(\tau\) and \(\tau'\), the edit translations of the transports to \(E\) and \(E'\) (Part IV)… and its anchor \(\lambda(k)\), the subnetwork of \(D\) assigned to \(k\) (Part IV)…
- **CH-0519** · 1 record · declined
  - **C-146** · S93 · recommendation · declined · wording not in the latest text · written against: file 13 draft 4, theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17), line 119 · carried by: none · source: results/S93 Tabulation of the replies, before any ruling.md — X03.6 (s93_xexam_mimo_F point 1), proposed wording, whole; ruling S93 X03 (W19.1): the replacement is not adopted; the FIX takes only "an active component" and the restored "up to the port translation" (challenge 2), KEEP on challenges 1 and 3; wording taken instead, or the related change: C-100
    - Before:
      > A kind is an equivalence class of components under this relation. For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV). A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - After:
      > A kind is an equivalence class of components under this relation. For two explanatory candidates for one question (Part V), with one target \(D\), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV). A component \(k\) of \(E\) and a component \(k'\) of \(E'\) are of one kind on \(C\) when, for every \((a,b)\in C\), \(L_k(\tau(a),\sigma(b))\) and \(L_{k'}(\tau'(a),\sigma'(b))\) correspond under one bijection of \(V_k\) onto \(V_{k'}\) that carries the value domain of each port of one onto the value domain of the other; this is their signatures read on \(C\) through \(\tau\) and \(\tau'\), and it extends the relation above to components of different organizations, whose classes are kinds in the same sense; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
- **CH-1254** · 1 record · not applied · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **E-36** · S93 · recommendation · not applied · shown in full under [L119.s1](#L119-s1)
- **CH-0637** · 1 record · applied
  - **D-56** · S95 · edit · applied · wording stands · written against: draft 5, line 119 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[55]; line 119; swap; TRUTH-OR-FOUNDATION
    - Before:
      > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its anchor, with a port translation (Part IV).
    - After:
      > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV).
    - Old wording:
      > its anchor, with a port translation (Part IV)
    - New wording:
      > its counterpart, with a port translation (Part IV)
- **CH-1070** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1070)
  - **D-528** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 57 (section: Definition and dependence)
    - Before:
      > anchor, anchored, anchoring condition
    - After:
      > counterpart; counterpart-kind condition
- **CH-1128** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1128)
  - **D-587** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, sceptic's rulings.md — section 2, row 35 (KEEP), file line 59
    - Before:
      > anchor / anchored / "anchoring condition" / "Same anchors, one account" → counterpart / "tied to" / "counterpart-kind condition" / "Same counterparts, one account"
    - After:
      > Where possible use "counterpart" alone ("k's counterpart λ(k)") rather than also "tied to".
- **CH-1004** · 2 records · superseded, applied
  - **D-905** · S96 · recommendation · superseded · wording not in the latest text · written against: repaired copy, line 119 · carried by: none · source: results/S96 Cross-examination - repaired copy - returns/s96_xexam_mimo_1.response.txt — finding 9 (b), L119-L120, wording given inline; ruling 'mimo 1 9 (b)' in results/S96 Reading of the replies.md, section 3
    - Before:
      > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV).
    - After:
      > where \(\pi\) translates ports, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with \(\pi\) restricted to its ports (Part IV).
  - **D-430** · S97 · edit · applied · wording stands · written against: repaired copy, line 119 · carried by: latest text · source: tests/S96 Repair - scripts/replacements_stage3.json — entries[23]; line 119; group X; ruling: mimo 1 9 (b)
    - Before:
      > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV).
    - After:
      > For two explanatory candidates (Part V), let \(E\) and \(E'\) be their organizations and \(t=(\pi,\tau,\sigma,\lambda)\) and \(t'=(\pi',\tau',\sigma',\lambda')\) their transports from \(D\), where \(\pi\) translates valuations, \(\tau\) translates edits, \(\sigma\) translates boundaries, and \(\lambda\) assigns each component of \(E\) a subnetwork of \(D\), its counterpart, with a port translation (Part IV).
    - Old wording:
      > where \(\tau\) translates edits,
    - New wording:
      > where \(\pi\) translates valuations, \(\tau\) translates edits,

<a id="L119-s4"></a>
#### L119.s4 · line 119 · 7 changes, 7 records
> A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense.

- **CH-0480** · 1 record · superseded · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-86** · S90 · recommendation · superseded · shown in full under [L119.s1](#L119-s1)
- **CH-0486** · 1 record · declined · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-112** · S90 · recommendation · declined · shown in full under [L119.s1](#L119-s1)
- **CH-1254** · 1 record · not applied · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **E-36** · S93 · recommendation · not applied · shown in full under [L119.s1](#L119-s1)
- **CH-0520** · 1 record · declined
  - **C-147** · S93 · recommendation · declined · written against: the note of file 13, its list of changes of claim (full file 13 draft 4; the DECLARATION fields of change list draft 4) · carried by: none · source: results/S93 Tabulation of the replies, before any ruling.md — X03.6 (s93_xexam_mimo_F point 1), proposed declaration; ruling S93 X03 (W19.1) writes its own declaration (challenge 2)
    - Before:
      > Part II now defines when a component of one candidate's organization and a component of another's are of one kind on C: their signatures, read on C through the two candidates' transports, coincide under a footprint bijection. It says that Derivation 2 uses kinds in this sense, and that Derivation 1 makes the like comparison between a component, read through its transport, and its anchor, read on C directly with its hidden ports projected away.
    - After:
      > Part II now defines when a component of one candidate's organization and a component of another's, the two candidates for one question with one target, are of one kind on C: their relations at every (a,b) of C, read through the two candidates' transports, correspond under a bijection of their footprints that carries the value domain of each port of one onto that of the other. It says that Derivation 2 uses kinds in this sense, and that Derivation 1 makes the like comparison between an active component, read through its transport, and its anchor, read on C directly with its hidden ports projected away, up to the port translation.
- **CH-0638** · 1 record · applied · also at: [L119.s5](#L119-s5)
  - **D-57** · S95 · edit · applied · wording stands · written against: draft 5, line 119 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[56]; line 119; swap; TRUTH-OR-FOUNDATION
    - Before:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - After:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense. Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - Old wording:
      > and its anchor \(\lambda(k)\), read on
    - New wording:
      > and its counterpart \(\lambda(k)\), read on
- **CH-0639** · 1 record · applied · form only · also at: [L119.s5](#L119-s5)
  - **D-58** · S95 · edit · applied · wording stands · written against: draft 5, line 119 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[57]; line 119; swap; LISTED; generated by an AUTO rule of replacements_source.py
    - Before:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - After:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense. Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - Old wording:
      > bijection; Derivation 2
    - New wording:
      > bijection; Argument 2
- **CH-0640** · 1 record · applied · form only · also at: [L119.s5](#L119-s5)
  - **D-59** · S95 · edit · applied · wording stands · written against: draft 5, line 119 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[58]; line 119; swap; LISTED; generated by an AUTO rule of replacements_source.py
    - Before:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Derivation 2 uses kinds in this sense. Derivation 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - After:
      > A component of \(E\) and a component of \(E'\) are of one kind on \(C\) when their signatures, read on \(C\) through \(\tau\) and \(\tau'\), coincide under a footprint bijection; Argument 2 uses kinds in this sense. Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - Old wording:
      > sense. Derivation 1
    - New wording:
      > sense. Argument 1

<a id="L119-s5"></a>
#### L119.s5 · line 119 · 9 changes, 9 records
> Argument 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its counterpart \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.

- **CH-0480** · 1 record · superseded · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-86** · S90 · recommendation · superseded · shown in full under [L119.s1](#L119-s1)
- **CH-0486** · 1 record · declined · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-112** · S90 · recommendation · declined · shown in full under [L119.s1](#L119-s1)
- **CH-0411** · 1 record · applied · also at: [L119.s2](#L119-s2)
  - **C-100** · S93 · recommendation · applied · wording stands · written against: file 13 draft 4, theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17), line 119 · carried by: file 13 draft 5 · source: results/S93 reading rulings/ruling S93 X03 W19.1.md — S93 ruling X03 (W19.1), challenge 2 (Mimo F point 2): FIX; the wording as applied in file 13 draft 5 (entry W19.1, C-10); read off the line diff file 13 draft 4 -> file 13 draft 5 at line 119
    - Before:
      > Derivation 1 makes the like comparison between a component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - After:
      > Derivation 1 makes the like comparison between an active component \(k\) of \(E\), read on \(C\) through \(\tau\), and its anchor \(\lambda(k)\), read on \(C\) directly with its hidden ports projected away, up to the port translation.
    - Old wording:
      > between a component
    - New wording:
      > between an active component
- **CH-1254** · 1 record · not applied · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s6](#L119-s6), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **E-36** · S93 · recommendation · not applied · shown in full under [L119.s1](#L119-s1)
- **CH-0638** · 1 record · applied · also at: [L119.s4](#L119-s4)
  - **D-57** · S95 · edit · applied · shown in full under [L119.s4](#L119-s4)
- **CH-0639** · 1 record · applied · form only · also at: [L119.s4](#L119-s4)
  - **D-58** · S95 · edit · applied · shown in full under [L119.s4](#L119-s4)
- **CH-0640** · 1 record · applied · form only · also at: [L119.s4](#L119-s4)
  - **D-59** · S95 · edit · applied · shown in full under [L119.s4](#L119-s4)
- **CH-1070** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1070)
  - **D-528** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 57 (section: Definition and dependence)
    - Before:
      > anchor, anchored, anchoring condition
    - After:
      > counterpart; counterpart-kind condition
- **CH-1128** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1128)
  - **D-587** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, sceptic's rulings.md — section 2, row 35 (KEEP), file line 59
    - Before:
      > anchor / anchored / "anchoring condition" / "Same anchors, one account" → counterpart / "tied to" / "counterpart-kind condition" / "Same counterparts, one account"
    - After:
      > Where possible use "counterpart" alone ("k's counterpart λ(k)") rather than also "tied to".

<a id="L119-s6"></a>
#### L119.s6 · line 119 · 5 changes, 6 records
> Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract.

- **CH-0251** · 1 record · applied
  - **B-77** · S76 · edit · applied · wording stands · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 136 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L136 s3 -> f11 L121 s3
    - Before:
      > Kinds are therefore relative to the contract; a coarser contract identifies more components.
    - After:
      > Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract.
    - Old wording:
      > components.
    - New wording:
      > components, and two components of one kind on \(C\) may separate on a finer contract.
- **CH-0366** · 2 records · unknown, applied · also at: [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **B-216** · S81 · recommendation · unknown · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md) · carried by: none named; the worklist item for O10 is W30 (change-list entry W30.1, at L121) · source: results/S81 File 11 against every case - outputs/determination/04 Step 3 and the determination - file 11 against file 10.md — §7.10 'Findings about the readers', third bullet, line 391; carried to S81 Results (shared text read against the fixed verdict on O10) · linked (not joined): tests/Revision 2 - worklist, draft of 23 September.md#W30, tests/Revision 2 - change list, draft of 23 September.md#W30.1
    - Before: *(nothing: an addition)*
    - After:
      > [no wording given] reading hazard in text both files carry (case O10); no place or wording named
  - **C-11** · S90 · edit · applied · wording stands · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923), line 121 · carried by: file 13 draft 1 (as sent); file 13 draft 2 (as sent); file 13 draft 3; file 13 draft 4; file 13 draft 5; scrubbed copy; repaired copy; latest text · source: tests/Revision 2 - change list, draft of 23 September.md — change list draft 5, entry W30.1 ("A difference in port values is not a difference of kind"), STATUS applied, KIND CLAIM, FILE-11 LINE 121; wording first in change list draft 1 (12e73da); carried as S90 brief (first 48 changes) C08, S90 part A1 R09
    - Before:
      > Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract.
    - After:
      > Kinds are therefore relative to the contract; a coarser contract identifies more components, and two components of one kind on \(C\) may separate on a finer contract. A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called. An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal does not separate the components.
    - Old wording:
      > and two components of one kind on \(C\) may separate on a finer contract.
    - New wording:
      > and two components of one kind on \(C\) may separate on a finer contract. A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called. An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal does not separate the components.
- **CH-0480** · 1 record · superseded · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-86** · S90 · recommendation · superseded · shown in full under [L119.s1](#L119-s1)
- **CH-0486** · 1 record · declined · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **C-112** · S90 · recommendation · declined · shown in full under [L119.s1](#L119-s1)
- **CH-1254** · 1 record · not applied · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s7](#L119-s7), [L119.s8](#L119-s8)
  - **E-36** · S93 · recommendation · not applied · shown in full under [L119.s1](#L119-s1)

<a id="L119-s7"></a>
#### L119.s7 · line 119 · 4 changes, 5 records
> A signature is built from a component's relation under each \((a,b)\in C\), not from the values its ports take in a solution; two components that differ only in those values are of one kind on \(C\), whatever the difference is called.

- **CH-0366** · 2 records · unknown, applied · also at: [L119.s6](#L119-s6), [L119.s8](#L119-s8)
  - **B-216** · S81 · recommendation · unknown · shown in full under [L119.s6](#L119-s6)
  - **C-11** · S90 · edit · applied · shown in full under [L119.s6](#L119-s6)
- **CH-0480** · 1 record · superseded · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s8](#L119-s8)
  - **C-86** · S90 · recommendation · superseded · shown in full under [L119.s1](#L119-s1)
- **CH-0486** · 1 record · declined · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s8](#L119-s8)
  - **C-112** · S90 · recommendation · declined · shown in full under [L119.s1](#L119-s1)
- **CH-1254** · 1 record · not applied · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s8](#L119-s8)
  - **E-36** · S93 · recommendation · not applied · shown in full under [L119.s1](#L119-s1)

<a id="L119-s8"></a>
#### L119.s8 · line 119 · 5 changes, 6 records
> An edit that sets a port replaces only the component that assigns the port (above), not the relations of the components that read it, and an edit under which the two relations stay equal does not separate the components.

- **CH-0366** · 2 records · unknown, applied · also at: [L119.s6](#L119-s6), [L119.s7](#L119-s7)
  - **B-216** · S81 · recommendation · unknown · shown in full under [L119.s6](#L119-s6)
  - **C-11** · S90 · edit · applied · shown in full under [L119.s6](#L119-s6)
- **CH-0480** · 1 record · superseded · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7)
  - **C-86** · S90 · recommendation · superseded · shown in full under [L119.s1](#L119-s1)
- **CH-0486** · 1 record · declined · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7)
  - **C-112** · S90 · recommendation · declined · shown in full under [L119.s1](#L119-s1)
- **CH-1254** · 1 record · not applied · also at: [L119.s1](#L119-s1), [L119.s2](#L119-s2), [L119.s3](#L119-s3), [L119.s4](#L119-s4), [L119.s5](#L119-s5), [L119.s6](#L119-s6), [L119.s7](#L119-s7)
  - **E-36** · S93 · recommendation · not applied · shown in full under [L119.s1](#L119-s1)
- **CH-1126** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1126)
  - **D-661** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, proposed.md — section 2.4, table row at file line 83; sceptic's row 31
    - Before:
      > **primitive**, the two **primitives**, "primitive 2" (Θ and N)
    - After:
      > **import**, the two **imports**, "import 2"

<a id="L121-s1"></a>
#### L121.s1 · line 121 · 2 changes, 2 records
> What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:

- **CH-0252** · 1 record · applied · form only
  - **B-78** · S76 · edit · applied · wording stands · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 138 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L138 s1 -> f11 L123 s1
    - Before:
      > What ordinary language calls a cause, a measurement, a rule, or a constitutive status are families of signatures:
    - After:
      > What ordinary language calls a cause, a measurement, a rule or a constitutive status are families of signatures:
    - Old wording:
      > rule, or
    - New wording:
      > rule or
- **CH-0580** · 1 record · declined
  - **C-208** · S90 · recommendation · declined · wording not in the latest text · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md, md5 5e494c1095d920d128b9a79de378f923), line 123 · carried by: none · source: tests/Revision 2 - worklist, draft of 23 September.md — worklist item W47 (L944), 12:273, a new claim carried from file 12; deferred; decision D5 of the change list ("The decisions D1-D11"): from file 12, only the missing-input sentence pattern
    - Before: *(nothing: an addition)*
    - After:
      > A collateral effect offered as a cause fails (F1)

<a id="L123-s1"></a>
#### L123.s1 · list item · line 123 · no change recorded
> - a **causal assignment** has a signature that changes under intervention on its output port and under replacement of the component, and is invariant under observation edits;

<a id="L124-s1"></a>
#### L124.s1 · list item · line 124 · no change recorded
> - a **measurement** has a signature invariant under interventions on the measured port and variable under edits to the measuring relation;

<a id="L125-s1"></a>
#### L125.s1 · list item · line 125 · no change recorded
> - a **rule application** has a signature invariant under interventions on the world and variable under edits to the rule.

<a id="L127-s1"></a>
#### L127.s1 · line 127 · no change recorded
> These are descriptions of patterns in (K), not additional data.

<a id="L127-s2"></a>
#### L127.s2 · line 127 · no change recorded
> The semantics never asks whether a component "is" a cause.

<a id="L127-s3"></a>
#### L127.s3 · line 127 · no change recorded
> It asks what its signature is.

<a id="L127-s4"></a>
#### L127.s4 · line 127 · 2 changes, 2 records
> In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows.

- **CH-0253** · 1 record · applied
  - **B-79** · S76 · edit · applied · wording stands · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 144 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: added at f11 L129 s4, after f10 L144 s3; S81 det 03 §1 place M13
    - Before: *(nothing: an addition)*
    - After:
      > In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows.
- **CH-0371** · 1 record · applied
  - **B-221** · S81 · recommendation · applied · written against: file 11 (authority/11 Claude Fable Semantics - standalone theory, revision 1.md), line 129 · carried by: revision 2 note draft (tests/Revision 2 - revision note, draft of 23 September.md), layer 2 of the record, row L2-05; record only, not in any theory text · source: results/S81 Results - file 11 against file 10, determined.md — S81 Results, Next step: 'a declaration of the 41 undeclared CLAIM places (and M7) in the second layer of the revision's record'; place M13 (determination 03 §1, row M13; file-11 locator 'L129, sentences 4–5', file-10 'none; compare L126, L138–L144'); the file-11 sentences are edit records B-79, B-80 · linked (not joined): tests/Revision 2 - revision note, draft of 23 September.md#L2-05
    - Before:
      > In particular, a part that reads or reports another part has a measurement's signature: change only the reading and the part it reports stays as it was; change the part and the reading follows. Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording.
    - After:
      > [no wording given] declare this place in the revision's record as a change of claim not declared by file 11's note

<a id="L127-s5"></a>
#### L127.s5 · line 127 · 5 changes, 5 records
> Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording.

- **CH-0254** · 1 record · applied
  - **B-80** · S76 · edit · applied · wording not in the latest text · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 144 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: added at f11 L129 s5, after f10 L144 s3; S81 det 03 §1 place M13
    - Before: *(nothing: an addition)*
    - After:
      > Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording.
- **CH-0641** · 1 record · applied
  - **D-60** · S95 · edit · applied · wording stands · written against: draft 5, line 127 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[59]; line 127; swap; TRUTH-OR-FOUNDATION
    - Before:
      > Which of the two an account offers as producing an outcome is settled by that signature, not by the account's wording.
    - After:
      > Which of the two an account offers as producing an outcome is fixed by that signature, not by the account's wording.
    - Old wording:
      > is settled by that signature
    - New wording:
      > is fixed by that signature
- **CH-1046** · 1 record · applied · vocabulary
  - **D-504** · S95 · edit · applied · written against: draft 5, line 127 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 23 (section: Status, arguments and acceptance)
    - Before:
      > l. 127 "settled by that signature"
    - After:
      > fixed by that signature
- **CH-1163** · 1 record · applied · vocabulary · also at: [L317.s1](06%20Work%2C%20routes%2C%20and%20interference%20%28Part%20VI%29.md#L317-s1)
  - **D-628** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, proposed.md — section 2.1, table row at file line 35; sceptic's row 6
    - Before:
      > settled (l. 317), settles (l. 269), "is settled by that signature" (l. 127)
    - After:
      > decided (l. 317, 269); "is fixed by that signature" (l. 127)
- **CH-1126** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1126)
  - **D-661** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, proposed.md — section 2.4, table row at file line 83; sceptic's row 31
    - Before:
      > **primitive**, the two **primitives**, "primitive 2" (Θ and N)
    - After:
      > **import**, the two **imports**, "import 2"

<a id="sec-L37-37"></a>
## Part 0 — Read this first · Grievances, anticipated / 1. "Without declared kinds you cannot tell a cause from a correlation." · line 37 · filed here from Part 0

<a id="L37-s1"></a>
#### L37.s1 · line 37 · no change recorded
> **1. "Without declared kinds you cannot tell a cause from a correlation."** You can, and only this way.

<a id="L37-s2"></a>
#### L37.s2 · line 37 · no change recorded
> A correlation has no component that responds to an intervention on its supposed input; a cause does.

<a id="L37-s3"></a>
#### L37.s3 · line 37 · 3 changes, 3 records
> That is a difference in edit-response, which is what the semantics asks about (Part II, "Kinds are edit-signatures").

- **CH-0201** · 1 record · applied
  - **B-27** · S76 · edit · applied · wording not in the latest text · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 32 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L32 s3 -> f11 L39 s5
    - Before:
      > The difference is a difference in edit-response, which is exactly what the semantics checks.
    - After:
      > That is a difference in edit-response, which is what the semantics checks (Part II, "Kinds are edit-signatures").
- **CH-0603** · 1 record · applied
  - **D-22** · S95 · edit · applied · wording stands · written against: draft 5, line 37 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[21]; line 37; swap; MISSED
    - Before:
      > That is a difference in edit-response, which is what the semantics checks (Part II, "Kinds are edit-signatures").
    - After:
      > That is a difference in edit-response, which is what the semantics asks about (Part II, "Kinds are edit-signatures").
    - Old wording:
      > which is what the semantics checks
    - New wording:
      > which is what the semantics asks about
- **CH-1086** · 1 record · applied · vocabulary
  - **D-544** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 78 (section: Truth, fact and error)
    - Before:
      > checked, checks, checkable
    - After:
      > tested, testable; l. 37 "asks about"

<a id="L37-s4"></a>
#### L37.s4 · line 37 · 1 change, 1 record
> A declared label adds no discriminating power: where a separating change exists, fidelity finds it; where none exists, the label asserts a distinction the level does not contain.

- **CH-0202** · 1 record · applied
  - **B-28** · S76 · edit · applied · wording stands · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 32 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L32 s4 -> f11 L39 s6
    - Before:
      > Declared kind-labels added no discriminating power; where a separating change exists, edit-fidelity already finds it, and where none exists, the label was asserting a distinction the level does not contain.
    - After:
      > A declared label adds no discriminating power: where a separating change exists, fidelity finds it; where none exists, the label asserts a distinction the level does not contain.

<a id="sec-L39-39"></a>
## Part 0 — Read this first · Grievances, anticipated / 2. "So this is operationalism: a thing is what you can do to it." · line 39 · filed here from Part 0

<a id="L39-s1"></a>
#### L39.s1 · line 39 · no change recorded
> **2. "So this is operationalism: a thing is what you can do to it."** A *kind* is what a level's admitted changes can distinguish.

<a id="L39-s2"></a>
#### L39.s2 · line 39 · 3 changes, 3 records
> A *content* is a whole organization, which can contain components that no change at that level separates, and then they are one kind *at that level*, which is what that level contains, not a loss.

- **CH-0203** · 1 record · applied · form only
  - **B-29** · S76 · edit · applied · wording stands · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 35 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L35 s2 -> f11 L41 s4
    - Before:
      > A *content* is a whole organization, which can contain components that no change at that level separates — and then they are one kind *at that level*, which is correct rather than a loss.
    - After:
      > A *content* is a whole organization, which can contain components that no change at that level separates, and then they are one kind *at that level*, which is correct rather than a loss.
    - Old wording:
      > —
    - New wording:
      > ,
- **CH-0604** · 1 record · applied
  - **D-23** · S95 · edit · applied · wording stands · written against: draft 5, line 39 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[22]; line 39; swap; TRUTH-OR-FOUNDATION
    - Before:
      > A *content* is a whole organization, which can contain components that no change at that level separates, and then they are one kind *at that level*, which is correct rather than a loss.
    - After:
      > A *content* is a whole organization, which can contain components that no change at that level separates, and then they are one kind *at that level*, which is what that level contains, not a loss.
    - Old wording:
      > which is correct rather than a loss
    - New wording:
      > which is what that level contains, not a loss
- **CH-1083** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1083)
  - **D-541** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 75 (section: Truth, fact and error)
    - Before:
      > correct, correctly
    - After:
      > dropped; "what that level contains"; "faithful locally"; "typing as declared"; "predict the displacements that occur"

<a id="L39-s3"></a>
#### L39.s3 · line 39 · no change recorded
> At a finer level with more admitted changes they may separate.

<a id="L39-s4"></a>
#### L39.s4 · line 39 · 1 change, 1 record
> Every kind-claim is indexed to its level.

- **CH-0204** · 1 record · applied
  - **B-30** · S76 · edit · applied · wording stands · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 35 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L35 s4 -> f11 L41 s6
    - Before:
      > The semantics indexes every kind-claim to its level.
    - After:
      > Every kind-claim is indexed to its level.

<a id="L39-s5"></a>
#### L39.s5 · line 39 · no change recorded
> That is scoping, not operationalism.

<a id="sec-L57-57"></a>
## Part 0 — Read this first · Grievances, anticipated / 11. "Kinds exist. A rule is not a cause." · line 57 · filed here from Part 0

<a id="L57-s1"></a>
#### L57.s1 · line 57 · 3 changes, 3 records
> **11. "Kinds exist. A rule is not a cause."** A rule and a cause differ in how they respond to changes: a rule's application changes when the rule is edited and not when the world is intervened on; a cause's assignment changes under intervention.

- **CH-0621** · 1 record · applied
  - **D-40** · S95 · edit · applied · wording stands · written against: draft 5, line 57 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[39]; line 57; swap; MISSED
    - Before:
      > **11. "Kinds obviously exist.
    - After:
      > **11. "Kinds exist.
- **CH-1087** · 1 record · applied · vocabulary · also at: [L17.s4](01%20The%20document%20as%20a%20whole.md#L17-s4), [L536.s1](15%20What%20would%20rule%20this%20class%20out%20%28Part%20XV%29.md#L536-s1)
  - **D-545** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 79 (section: Truth, fact and error)
    - Before:
      > plainly, obviously
    - After:
      > dropped
- **CH-1160** · 1 record · declined · vocabulary
  - **D-619** · S95 · recommendation · declined · written against: draft 5, line 57 · carried by: none · source: tests/S95 Scrub - vocabulary, sceptic's rulings.md — section 3 (3. Occurrences the proposal does not cover), row at file line 119
    - Before:
      > "Kinds obviously exist"
    - After:
      > "Kinds exist whatever anyone's model says"

<a id="L57-s2"></a>
#### L57.s2 · line 57 · 1 change, 1 record
> That is a difference in edit-signature (Part II), and the semantics represents it exactly.

- **CH-0230** · 1 record · applied · form only
  - **B-56** · S76 · edit · applied · wording stands · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 62 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L62 s2 -> f11 L59 s5
    - Before:
      > That is a difference in edit-signature, and the semantics represents it exactly.
    - After:
      > That is a difference in edit-signature (Part II), and the semantics represents it exactly.
    - Old wording:
      > signature,
    - New wording:
      > signature (Part II),

<a id="L57-s3"></a>
#### L57.s3 · line 57 · 1 change, 1 record
> What it denies is that the difference is available before the admitted changes are fixed, or independently of them.

- **CH-0231** · 1 record · applied
  - **B-57** · S76 · edit · applied · wording stands · written against: file 10 (authority/10 Claude Fable Semantics - standalone theory.md), line 62 · carried by: file 11 · source: authority/11 Claude Fable Semantics - standalone theory, revision 1.md — sentence diff, file 10 -> file 11: changed f10 L62 s3 -> f11 L59 s6
    - Before:
      > What the semantics denies is that the difference is available *before* the admitted changes are fixed, or independently of them.
    - After:
      > What it denies is that the difference is available before the admitted changes are fixed, or independently of them.
    - Old wording:
      > the semantics denies is that the difference is available *before*
    - New wording:
      > it denies is that the difference is available before

<a id="sec-L552-558"></a>
## Part XVI — Arguments · 1. Kind preservation needs no condition of its own · lines 552–558 · filed here from Part XVI

<a id="L552-s1"></a>
#### L552.s1 · heading · line 552 · 3 changes, 4 records
> ## 1. Kind preservation needs no condition of its own

- **CH-0826** · 1 record · applied
  - **D-245** · S95 · edit · applied · wording stands · written against: draft 5, line 552 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[244]; line 552; swap; TRUTH-OR-FOUNDATION
    - Before:
      > ## 1. Kind preservation is a theorem, not a condition
    - After:
      > ## 1. Kind preservation needs no condition of its own
- **CH-1062** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1062)
  - **D-520** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 44 (section: Proofs and arguments)
    - Before:
      > theorem; Corollary
    - After:
      > claim; Consequence
- **CH-1124** · 2 records · applied · vocabulary
  - **D-583** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, sceptic's rulings.md — section 2, row 28 (KEEP), file line 52
    - Before:
      > "Kind preservation is a theorem, not a condition" → "Argument 1. Kind preservation needs no condition of its own"
    - After:
      > In the body, not "(F1) already rules out every component …" but "no component whose signature differs from its counterpart's meets (F1)" (row 52).
  - **D-652** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, proposed.md — section 2.3, table row at file line 69; sceptic's row 28
    - Before:
      > "1. Kind preservation is a theorem, not a condition"
    - After:
      > "Argument 1. Kind preservation needs no condition of its own"

<a id="L554-s1"></a>
#### L554.s1 · line 554 · 3 changes, 3 records
> **Claim.** If a transport meets (F1) on \(C\), no active component \(k\) of \(E\) has a signature on \(\tau[C]\) that differs from the one its counterpart \(\lambda(k)\) has on \(C\), up to the port translation.

- **CH-0827** · 1 record · applied
  - **D-246** · S95 · edit · applied · wording stands · written against: draft 5, line 554 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[245]; line 554; rewording; TRUTH-OR-FOUNDATION
    - Before:
      > **Claim.** If a transport satisfies (F1) on \(C\), then every active component \(k\) of \(E\) has the same signature on \(\tau[C]\) as its anchor \(\lambda(k)\) has on \(C\), up to the port translation.
    - After:
      > **Claim.** If a transport meets (F1) on \(C\), no active component \(k\) of \(E\) has a signature on \(\tau[C]\) that differs from the one its counterpart \(\lambda(k)\) has on \(C\), up to the port translation.
- **CH-1070** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1070)
  - **D-528** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 57 (section: Definition and dependence)
    - Before:
      > anchor, anchored, anchoring condition
    - After:
      > counterpart; counterpart-kind condition
- **CH-1128** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1128)
  - **D-587** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, sceptic's rulings.md — section 2, row 35 (KEEP), file line 59
    - Before:
      > anchor / anchored / "anchoring condition" / "Same anchors, one account" → counterpart / "tied to" / "counterpart-kind condition" / "Same counterparts, one account"
    - After:
      > Where possible use "counterpart" alone ("k's counterpart λ(k)") rather than also "tied to".

<a id="L556-s1"></a>
#### L556.s1 · line 556 · 1 change, 1 record
> *Why this and not its denial.*

- **CH-0828** · 1 record · applied · form only
  - **D-247** · S95 · edit · applied · wording stands · written against: draft 5, line 556 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[246]; line 556; swap; LISTED; generated by an AUTO rule of replacements_source.py
    - Before:
      > *Proof.*
    - After:
      > *Why this and not its denial.*

<a id="L556-s2"></a>
#### L556.s2 · line 556 · 1 change, 1 record
> By (K), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\) and \(\operatorname{sig}_{\tau[C]}(k)=\{(\tau(a),\sigma(b),L_k(\tau(a),\sigma(b)))\}\).

- **CH-1009** · 1 record · applied · also at: [L233.s1](05%20Account%20%28Part%20V%29.md#L233-s1), [L235.s1](05%20Account%20%28Part%20V%29.md#L235-s1)
  - **D-479** · S97 · edit · applied · wording stands · written against: repaired copy, line 556 · carried by: latest text · source: tests/S96 Repair - scripts/replacements_stage3.json — entries[72]; line 556; group X; ruling: glm A 1
    - Before:
      > By (K), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\) and \(\operatorname{sig}_{\tau[C]}(k)=\{(\tau(a),\sigma(b),L_k(\tau(a),\sigma(b)))\}\).
    - After:
      > By (K), \(\operatorname{sig}_C(\lambda(k))=\{(a,b,\operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b))\}\) and \(\operatorname{sig}_{\tau[C]}(k)=\{(\tau(a),\sigma(b),L_k(\tau(a),\sigma(b)))\}\).
    - Old wording:
      > \operatorname{proj}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b)
    - New wording:
      > \operatorname{proj}^{\lambda}_{V_k}\operatorname{Sol}_{\lambda(k)}(a,b)

<a id="L556-s3"></a>
#### L556.s3 · line 556 · 1 change, 1 record
> (F1) equates the third coordinates pointwise. ∎

- **CH-1061** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1061)
  - **D-519** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 43 (section: Proofs and arguments)
    - Before:
      > *Proof.*
    - After:
      > *Why this and not its denial.*

<a id="L558-s1"></a>
#### L558.s1 · line 558 · 6 changes, 6 records
> **Consequence.** A condition "each component's counterpart must be a component of the same kind" adds nothing to (F1) on any contract.

- **CH-0527** · 1 record · not applied
  - **C-154** · S93 · recommendation · not applied · wording not in the latest text · written against: file 13 draft 4, theory text (md5 fc55b470c63cd4b3c27d6aa64d8d8c17), line 558 · carried by: none · source: results/S93 Tabulation of the replies, before any ruling.md — X06.7 (b) (s93_xexam_mimo_H point 2), Derivation 1's Corollary at L558; ruling S93 X06: not taken in X06; carried forward after S93 as a candidate ("each active component" at L558); the reply's words: "should read `each active component`"
    - Before:
      > **Corollary.** A condition "each component must anchor to a component of the same kind" adds nothing to (F1) on any contract.
    - After:
      > **Corollary.** A condition "each active component must anchor to a component of the same kind" adds nothing to (F1) on any contract.
    - Old wording:
      > each component must anchor
    - New wording:
      > each active component must anchor
- **CH-0829** · 1 record · applied
  - **D-248** · S95 · edit · applied · wording stands · written against: draft 5, line 558 · carried by: scrubbed copy · source: tests/S95 Scrub - scripts/replacements.json — entries[247]; line 558; swap; TRUTH-OR-FOUNDATION
    - Before:
      > **Corollary.** A condition "each component must anchor to a component of the same kind" adds nothing to (F1) on any contract.
    - After:
      > **Consequence.** A condition "each component's counterpart must be a component of the same kind" adds nothing to (F1) on any contract.
    - Old wording:
      > **Corollary.** A condition "each component must anchor to a component of the same kind"
    - New wording:
      > **Consequence.** A condition "each component's counterpart must be a component of the same kind"
- **CH-1062** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1062)
  - **D-520** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 44 (section: Proofs and arguments)
    - Before:
      > theorem; Corollary
    - After:
      > claim; Consequence
- **CH-1070** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1070)
  - **D-528** · S95 · edit · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, as used.md — table row at file line 57 (section: Definition and dependence)
    - Before:
      > anchor, anchored, anchoring condition
    - After:
      > counterpart; counterpart-kind condition
- **CH-1128** · 1 record · applied · vocabulary · also at: [its entry in 16 Vocabulary across the text](16%20Vocabulary%20across%20the%20text.md#CH-1128)
  - **D-587** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, sceptic's rulings.md — section 2, row 35 (KEEP), file line 59
    - Before:
      > anchor / anchored / "anchoring condition" / "Same anchors, one account" → counterpart / "tied to" / "counterpart-kind condition" / "Same counterparts, one account"
    - After:
      > Where possible use "counterpart" alone ("k's counterpart λ(k)") rather than also "tied to".
- **CH-1175** · 1 record · applied · vocabulary
  - **D-653** · S95 · recommendation · applied · written against: draft 5 · carried by: scrubbed copy · source: tests/S95 Scrub - vocabulary, proposed.md — section 2.3, table row at file line 70; sceptic's row 27
    - Before:
      > Corollary (Derivation 1)
    - After:
      > Consequence

<a id="L558-s2"></a>
#### L558.s2 · line 558 · no change recorded
> Where the contract separates two kinds, (F1) already distinguishes them; where it does not, they are one kind on that contract.

<a id="L558-s3"></a>
#### L558.s3 · line 558 · no change recorded
> The word "kind" is therefore eliminable from the definition of an account, and its elimination loses no case.

<a id="rest-II"></a>
## Not in the latest text, with no section: Part II

- <a id="CH-0067"></a>**CH-0067** · 1 record · never applied · placed by: Part its source names (never applied)
  - **A-67** · R2 (log 25) · recommendation · not applied · written against: file 20 with R2 applied (file 20 not held); from log S69 read as amendments to file 10 · carried by: none · source: results/S64 Near cases - return/05 Quotations.md — S64 Near cases - return/05 Quotations.md row S64-R2-D01 (table line 122), sentence 1 of 6; also S72 Stage 1 testing - return/05 Quotations.md line 224; S72 Stage 2 audit - return/03 Audit of the quotations.md line 506 · nearest latest-text sentence (a lead, not a place): [L119.s4](#L119-s4)
    - Before: *(nothing: an addition)*
    - After:
      > Clarify Part II's distinction between a component's state and its forward kind.
- <a id="CH-0068"></a>**CH-0068** · 2 records · never applied · placed by: Part its source names (never applied)
  - **A-68** · R2 (log 25) · recommendation · not applied · written against: file 20 with R2 applied (file 20 not held); from log S69 read as amendments to file 10 · carried by: none · source: results/S64 Near cases - return/05 Quotations.md — S64 Near cases - return/05 Quotations.md row S64-R2-D01 (table line 122), sentence 2 of 6; also S72 Stage 1 testing - return/05 Quotations.md line 224; S72 Stage 2 audit - return/03 Audit of the quotations.md line 506
    - Before: *(nothing: an addition)*
    - After:
      > Deleting only the identity entry from a change list does not remove state information: an unrelated change may leave different baseline states intact.
  - **A-164** · Stage B (logs 41, 55) · recommendation · not applied · written against: file 20 with R2 applied (file 20 not held); from log S69 read as amendments to file 10 · carried by: none · source: results/55 Stage B return - the other model's finished table, near cases and tighter pairs.md — Stage B table row 33 (file line 15), Amendment D, phrase cell; part of the cell is in R2 reason text (S64-R2-D04)
    - Before: *(nothing: an addition)*
    - After:
      > Deleting only the identity entry from a change list does not remove state information: an unrelated change may leave different baseline states intact.
    - New wording:
      > <u>an unrelated change</u>; <u>share a working kind</u>; <u>an irrelevant alteration elsewhere</u>
- <a id="CH-0069"></a>**CH-0069** · 1 record · never applied · placed by: Part its source names (never applied)
  - **A-69** · R2 (log 25) · recommendation · not applied · written against: file 20 with R2 applied (file 20 not held); from log S69 read as amendments to file 10 · carried by: none · source: results/S64 Near cases - return/05 Quotations.md — S64 Near cases - return/05 Quotations.md row S64-R2-D01 (table line 122), sentence 3 of 6; also S72 Stage 1 testing - return/05 Quotations.md line 224; S72 Stage 2 audit - return/03 Audit of the quotations.md line 506
    - Before: *(nothing: an addition)*
    - After:
      > A claim that two different states have the same forward kind therefore requires a declared correspondence between those states and between the changes being compared.
- <a id="CH-0070"></a>**CH-0070** · 1 record · never applied · placed by: Part its source names (never applied)
  - **A-70** · R2 (log 25) · recommendation · not applied · written against: file 20 with R2 applied (file 20 not held); from log S69 read as amendments to file 10 · carried by: none · source: results/S64 Near cases - return/05 Quotations.md — S64 Near cases - return/05 Quotations.md row S64-R2-D01 (table line 122), sentence 4 of 6; also S72 Stage 1 testing - return/05 Quotations.md line 224; S72 Stage 2 audit - return/03 Audit of the quotations.md line 506
    - Before: *(nothing: an addition)*
    - After:
      > The correspondence must preserve the relations at the claimed grain; it cannot be chosen separately for each inconvenient outcome.
- <a id="CH-0071"></a>**CH-0071** · 1 record · never applied · placed by: Part its source names (never applied)
  - **A-71** · R2 (log 25) · recommendation · not applied · written against: file 20 with R2 applied (file 20 not held); from log S69 read as amendments to file 10 · carried by: none · source: results/S64 Near cases - return/05 Quotations.md — S64 Near cases - return/05 Quotations.md row S64-R2-D01 (table line 122), sentence 5 of 6; also S72 Stage 1 testing - return/05 Quotations.md line 224; S72 Stage 2 audit - return/03 Audit of the quotations.md line 506
    - Before: *(nothing: an addition)*
    - After:
      > Where the question distinguishes the states or locations, that distinction must remain.
- <a id="CH-0072"></a>**CH-0072** · 1 record · never applied · placed by: Part its source names (never applied)
  - **A-72** · R2 (log 25) · recommendation · not applied · written against: file 20 with R2 applied (file 20 not held); from log S69 read as amendments to file 10 · carried by: none · source: results/S64 Near cases - return/05 Quotations.md — S64 Near cases - return/05 Quotations.md row S64-R2-D01 (table line 122), sentence 6 of 6; also S72 Stage 1 testing - return/05 Quotations.md line 224; S72 Stage 2 audit - return/03 Audit of the quotations.md line 506
    - Before: *(nothing: an addition)*
    - After:
      > Without such a correspondence, report equality of full indexed responses rather than claiming state-independent kind identity.
