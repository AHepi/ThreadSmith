# FW0 REV from M0 - Creative revision events

## Where this belongs

**Role:** earlier semantic revision. **Predecessors and inputs:** [M0](../00%20ORIGINS%20-%20Sources%20and%20missing%20links/M0%20MISSING%20-%20Earlier%20event%20semantics%20and%20audit.md).

Separates what holds in a semantic model from what a finite evidence record supports. This Revision E answers an earlier audit by making occurrence, contribution, and dependency contracts explicit.

Earlier surviving manuscript. The route from this family to M1 is not documented by the supplied files.

**Where it leads:** [M1](../00%20ORIGINS%20-%20Sources%20and%20missing%20links/M1%20MISSING%20-%20Semantics%20before%20hardening.md), [Q1](../FW1%20REV%20-%20Recursive%20semantics%20after%20hardening/01%20REPAIR%20-%20The%20audit%20and%20its%20replacements/Q1%20AUDIT%20of%20M1%2BM2%20-%20Hardening%20repairs.md).

**Basis for this placement:** Reading guide, opening paragraphs: Revision D and its second audit are the stated immediate predecessors. Those inputs are not supplied.

[Naming key and family tree](../layout.md). The navigation above is editorial. The manuscript below is a renamed reading edition, not a new scientific revision. Original hashes, case identifiers, mathematical symbols, quoted locators, and execution commands retain their historical meaning. Hashes bind the unchanged originals, not this reading copy.

---

## Revision E — recursive evidence kernel, occurrence and dependency contracts

---

## Part I. Reading guide

### What the document is for

A system proposes a theory, receives a criticism, and revises. Did it create knowledge? CR-1.0 answers with a typed schema whose decisive relations — explains, authors, uses the reason, improves the situation — are primitives. CR-2.0 keeps those relations as primitives but gives each one a witness: a record someone can inspect, and a record someone can attack. The formal object is then not a verdict but two things that must never be confused: what holds in a model, and what a finite record of evidence currently supports.

Revision C separated those two judgments and was audited; Revision D made the evidence layer recursive and was audited again, this time with an executable harness whose thirty checks reproduce. This revision answers the second audit. It is smaller in ambition than it looks: the recursive design is unchanged, and what changed are the contracts around it — what an occurrence is, what a judgment is about, which prior objects it depends on, and which rule version evaluated it.

### What this revision does

Revision D made one design move: **the kernel is applied to its own evidence.** A certificate is a content version, so it can be criticised. Admitting a certificate is an event, so the record of evidence is a history with the same configuration semantics as the system it describes, and "present at this cut" is well defined. Rejecting a certificate is a criticism of it — an attack — and an attack is itself content, so a pretext rejection is as criticisable as a bad theory. The raw ledger stays four-valued and records what evidence exists. The adjudicated view keeps only the certificates that survive attack.

Revision D was audited, with an executable harness. Its findings were of four kinds, and this revision answers each.

*Missing clauses with large consequences.* The public originative-act predicate never equated the query with its witness, so one valid witness answered every question. Newness sent initial content through "some strictly earlier event," which an entry with no predecessor cannot supply. The criticism constructor quantified over an already-created criticism and demanded a second creator, because a criticism *template* and an immutable *occurrence* were the same symbol. And criticism was declared globally conflict-free, which heredity forbids the moment a conjecture sits on one branch of an alternative. Each is now one clause: the query is bound (§13), initial content has its own deployability branch (§9), the constructor produces a fresh occurrence of an eligible template (§5), and criticism is excluded from alternative sets so that recordability is *relative to the current configuration* — which is what fallibility needs and all that heredity permits (§5).

*A semantic gap.* The seasons fixture said that defeating an adequacy certificate makes the improvement claim that cited it OPEN. Nothing in the displayed rules could do that. §7.3 now propagates attacks backward along **essential-dependency** edges before the grounded extension is computed, with a two-line well-definedness argument: dependencies lie in the causal past, so the propagated attack relation is a fixed relation on a finite set and Dung's operator is unchanged. Completeness guards on universal derivations become dependency leaves by the same rule (§7.4).

*A gift.* Every attack created by a `Criticize` event targets something already in its causal past, and every essential dependency does too. The attack graph of any legitimate history is therefore **acyclic**, on which grounded, preferred, stable, and complete semantics coincide and no argument is undecided (§7.3). The semantics choice that Revision D labelled an encoding decision disappears for the first slice; the cycle fixture it promised cannot be realised and is withdrawn.

*A scope declaration.* In-kernel recursion covers content, certificates, attacks, and standards, the last as dependency nodes. Revising the rules or the evaluator is a versioned external act. Every reported judgment carries the kernel and profile versions and the cut digest, so a re-evaluation under new rules is a new judgment linked to the old, never a rewrite (§7.7). No infinite stack; no self-modifying evaluator.

The rest of the audit — external criticism must be represented by the responder, the self-critical flag needs a witness, every improvement constructor needs a response-indexed envelope, capacity needs an applicable perturbation and a new continuation, reach needs a bound witness and non-empty obligations, contrast classes must not define non-creativity into themselves, and the core gate must not import success machinery — is repaired where each lives and mapped in §28.

### What is still non-negotiable

Nothing closes. No response, retention, certificate, standard, source, or policy makes anything immune. Section 5 states this as constraints on the event space and the dossier rather than as a promise that events will occur. A creator that acts once and stops has still acted. A recorder can criticise a theory after its author is gone.

### What is claimed and what is not

The first implementation slice (`cr2/0.1-recursive-kernel`) is Part II: sorts, content identity, the event structure, the fallibility contract, spans and cuts, the two-layer evidence calculus with dependency propagation, newness, criticism and response, authorship, and the originative-act and critical-process classifiers with lineage. Part III specifies success, capacity, hard-to-vary, reach, contrast classes, and physical realization in closed form but does not claim them for the slice. Part IV gives theorems, non-entailments, mutation tests, a seasons fixture split into a core part (cuts `r0`, `r1c`) and a success part (cuts `r1`, `r2`, `r3`), a consistency witness containing an alternative branch, and the acceptance gates. Part V attaches origin, inferential status, and dependencies to every symbol.

This is a proposed class. CR-1.0 remains the authority for what it says. Adoption is a human act, per entry of the change register.

---

## Part II. The kernel

## 1. Sorts

```text
Actor            = Sys ⊎ Recorder            who performs an event: the target system s, or a recorder/auditor a
Sys              bounded target systems
Recorder         recorders, auditors, dossier-keepers
Event            possible occurrences; a record is a configuration of them
EventKind        §4
VersionId        immutable identity of an event-created record
ContentId        identity of content at a chosen semantic grain
ContentVersion   §2
Role             problem | background | standard | conjecture | criticism | response | explanation |
                 observation | rejection | reason | certificate | attack | comparison | operation
Tension          candidate discrepancies a system may attend to
Organisation     causal organisations: recognition, priority (values), stable organisation
Defect           defect descriptors supplied by the domain
Merit            merit / material-commitment descriptors supplied by the domain
Outcome          §4.2
Formula          claims of the kernel's language (the objects certificates bear on)
Polarity         pos | neg
Scope, Provenance, Integrity, Channel
Boundary         predeclared system/environment boundaries, with declared channels
EqLevel          content-equivalence levels ℓ
Span             §6
Config           finite configurations, §3; Run := Config; Cut := a Config designated for reporting
ExplanationObject §10
Mode             construct | reconstruct | adopt
Template         repeatable criticism content, §5; an occurrence of a template is a ContentVersion with a fresh VersionId
Perturbation     declared perturbations, §17; includes the identity perturbation γ₀
KernelVersion, ProfileVersion, Digest   identities of the rules, the profile, and a configuration, §7.7
Judgment         a reported evaluation, §7.7
```

Problems, backgrounds, standards, criticisms, responses, certificates, and attacks are all content versions with the corresponding role. Nothing with a role is exempt from criticism.

Cross-sort inference requires a named bridge. Tokens are not their contents; prediction is not explanation; retention is not truth; supported is not true; physical information is not explanatory knowledge; an event is not a certificate and a certificate is not an event, though admitting one is.

## 2. Content versions and identity

```text
ContentVersion = ⟨ vid : VersionId, cid : ContentId, surface, normal?, roles : Finset Role,
                   parents : Finset VersionId, anchors, object? : ExplanationObject ⟩
```

`surface` retains the full prose, diagram, formula, artefact, or inexplicit-state locator. `normal` is an optional formal interpretation and never overwrites the surface. `object` is the optional explanation object of §10, present only for versions that carry the role `explanation`.

```text
creator(x)         the unique event with x ∈ created(e), for every x ∉ R₀ ; initial versions have no creator
contentParent(x,y) iff (x, y) ∈ declaredParents(creator(y))
                   declaredParents(e) ⊆ inputs(e) × created(e) is fixed per kind and outcome in §4:
                     EnterConjecture reconstruct: inputs(e) × {x};  Respond revise: {(target, y)};
                     Respond reframe: {(problem(crit), p')};  Respond restandardize: {(standard(crit), k')};  every other kind or outcome: ∅
Axioms
  freshness:   x ∈ created(e) → vid(x) does not occur in Versions(⇓e \ {e})
  uniqueness:  every non-initial version has exactly one creator
  agreement:   parents(y) = { vid(x) | contentParent(x,y) }
Derived
  contentParent(x,y) → creator(x) ≺ creator(y) or x initial      (by freshness and causal closure)
  contentParent is irreflexive and acyclic                        (follows from the above)
DescEq  := reflexive-transitive closure of contentParent
x <_c y := contentParent⁺(x,y)
sameContent_ℓ(x,y)   an equivalence relation at each level ℓ (reflexivity, symmetry, transitivity are profile obligations)
```

Reactivating standing content creates no version (§4, `Activate`). Reconstructing it creates a fresh version with the source as parent. Adopting an independently entered rival creates no ancestry. A lineage may stop receiving successors; nothing requires or forbids continuation.

## 3. Event structure and configurations

```text
ES = ⟨ Event, ≼, #, kind, actor, inputs, created, referenced, activated, prov ⟩

Axioms
  ≼ partial order;   finite causes: ∀ e, ⇓e := { e' | e' ≼ e } is finite
  # irreflexive, symmetric;   heredity: e # e' ∧ e' ≼ e'' → e # e''
  # is generated: # is the hereditary symmetric closure of a declared family AltSets of finite pairwise-alternative event sets
  typing: inputs(e), created(e), referenced(e), activated(e) : Finset ContentVersion, constrained by kind(e) (§4)
  payload references: refs(e) := inputs(e) ∪ referenced(e) ∪ activated(e) ∪ payloadRefs(e), where payloadRefs(e) is fixed per kind in §4
                      and contains every content version named anywhere in the payload of e
  causal grounding: refs(e) ⊆ Versions(⇓e \ {e})
  branching leaves criticism and admission alone: no AltSet contains an event of kind Criticize or Admit (§5)

Config r ⊆ Event : finite ∧ conflict-free ∧ downward-closed under ≼
Versions(r) := R₀ ∪ ⋃_{e ∈ r} created(e)              R₀ : the set of all initial versions (system-relative access is §9)
Cut          : a Config designated for reporting by a recorder; the designation is not an event and is not caused by any actor
```

The event space is the space of what can happen; a record is a configuration of it. There is no axiom that any configuration has an extension. Events of the target system and events of recorders live in the same structure and are ordered by the same causal relation; that is what lets the evidence layer (§7) use the same cuts as the target history.

## 4. Event kinds and payloads

### 4.1 Kinds

```text
Attend(e; s, τ, ω?)                  s attends to tension τ; ω an optional OpenProblem witness
                                     ω = ⟨ p, b, r_org, v ⟩ with Recognises(s, r_org, τ, p) ∧ Matters(s, v, τ, p) ∧ Represents(s, p, e)
                                     an Attend without ω is a legitimate event; it cannot root an originative act
EnterConjecture(e; s, x, p, b, mode, τ?) created(e) = {x}; mode ∈ Mode; τ? an optional tension the entry answers; for mode ∈ {reconstruct, adopt}, inputs(e) ≠ ∅
                                     reconstruct: contentParent(inputs, x); adopt: no ancestry, referenced(e) = inputs(e)
Activate(e; s, x)                    activated(e) = {x}; created(e) = ∅; makes standing content deployable again; creates no ancestry
Criticize(e; a, c)                   a : Actor (the system or a recorder); created(e) = {c}; c an occurrence with templ(c) a Template (§5);
                                     payloadRefs(e) = {target(c), problem(c), background(c), standard(c)} ∪ versions named in reason(c) or discriminator(c)
InterpretEvidence(e; a, o, c?)       created(e) = {o} with role observation; c the criticism whose discriminator o bears on; payloadRefs(e) = {c} ∪ versions named in o
CompareRivals(e; s, κ)               created(e) = {κ} with role comparison; κ = ⟨ p, b, standards : Finset Standard, A : Finset ContentVersion, pref : ContentVersion ∈ A, reasons ⟩;
                                     payloadRefs(e) = {p, b} ∪ standards ∪ A
Respond(e; s, σ)                     created(e) = created(σ); referenced(e) = referenced(σ); inputs(e) = {crit(σ), target(σ), problem(crit(σ)), standard(crit(σ))} ∪ referenced(σ); §4.2
Retain(e; s, y)                      referenced(e) = {y}; y ∈ Versions(⇓e \ {e})
RepertoireExpand(e; s, op)           created(e) = {op} with role operation
Admit(e; a, w)                       a recorder admits certificate w; created(e) = {w}; w has role certificate; payloadRefs(e) = dependencies(w) ∪ versions named in claim(w); §7
Merge(e; q_from, q_into)             a provenance link between spans; §6.5
AttentionShift(e; s, from : Span, τ) a target-system event: attention moves; not a stop, not a verdict
```

There is no closing, deciding, or terminal kind. Reframing and restandardising are `Respond` outcomes when they answer a criticism and `EnterConjecture` of a version with role `problem` or `standard` otherwise.

### 4.2 Response records

```text
Response σ = ⟨ crit : Criticism, target : ContentVersion, outcome : Outcome,
               created : Finset ContentVersion, referenced : Finset ContentVersion,
               result : Option ContentVersion, situation : Problem × Background ⟩

Outcome and typing
  revise          created = {y}, result = some y, contentParent(target, y)
  reject          created = {ρ}, role(ρ) = rejection, ρ names target; result = some ρ
  retainReasoned  created = {u}, role(u) = reason; referenced = {target}; result = some target
  rejectCriticism created = {c'}, c' a criticism with target(c') = crit; result = some c'
  requestEvidence created = {req}, req names discriminator(crit); result = some req
  reframe         created = {p'}, role(p') = problem, contentParent(problem(crit), p'); result = some p'
  restandardize   created = {k'}, role(k') = standard, contentParent(standard(crit), k'); result = some k'
  suspend         created = {u}, role(u) = reason, u records what remains unresolved; result = none
  ignore          created = {u}, role(u) = reason, u states why crit is set aside; referenced = {target}; result = none
  adoptRival      created = ∅; referenced = {z}; z ∈ Versions(⇓e \ {e}); ¬DescEq(target, z); result = some z
```

`result` is the response outcome: what CR-1.0 called the endpoint of a critical lineage — the outcome within one span, never the last member of anything. `ignore` must create a reason record; a content-insensitive refusal has nothing to put in it, and §11 is what tests whether the record is reason-specific.

## 5. Fallibility contract

Fallibility is a constraint on rules, not a guarantee of events. The following hold of every admissible event space, profile, and dossier; §25 rejects any extension that violates one.

```text
Templates and occurrences
  Template t = ⟨ target, p, b, δ, k, reason, discriminator, merits ⟩            repeatable criticism content
  a criticism occurrence c is a ContentVersion with role criticism, templ(c) = t, and a fresh vid; it is created by exactly one Criticize event
  eligible(t, r)  iff  target(t) ∈ Versions(r) ∧ WellFormedTemplate(t)                                (§11)
  Theorem: eligible(t, r) ∧ r ⊆ r' → eligible(t, r')

Constructor (criticism)
  ∀ r : Config, ∀ t with eligible(t, r), ∃ e ∉ r, ∃ c :
      kind(e) = Criticize ∧ created(e) = {c} ∧ templ(c) = t ∧ vid(c) ∉ vids(Versions(r)) ∧ ⇓e \ {e} ⊆ r
  (a fresh occurrence of every eligible template can be added to every configuration; the actor may be any actor;
   an occurrence already in r does not need a second creator, because eligibility is of the template, not of the occurrence)

Constructor (admission)
  ∀ r : Config, ∀ w with WellFormedCertificate(w) ∧ refs(w) ⊆ Versions(r) ∧ ScopeCompatible(w, r), ∃ e ∉ r :
      kind(e) = Admit ∧ created(e) = {w'} ∧ w' a fresh occurrence of w ∧ ⇓e \ {e} ⊆ r

Branching leaves criticism and admission alone
  no AltSet contains an event of kind Criticize or Admit
  Theorem (relative recordability): if e is given by either Constructor at r, then r ∪ {e} is a Config.
  Proof: e's conflicts are all inherited: e # f only if ∃ (a, b) alternatives with a ≼ e and b ≼ f. Then a ∈ ⇓e \ {e} ⊆ r.
         If f ∈ r, down-closure gives b ∈ r, and a # b with both in r contradicts conflict-freeness of r. So no f ∈ r conflicts with e.
  (A criticism on one branch remains incompatible with the other branch. That is heredity doing its job, not immunity;
   the property fallibility needs is recordability relative to the record, and that is what the theorem gives.)

Certificates are content
  every certificate, attack, and standard is a ContentVersion; Templates, the criticism Constructor, and relative recordability apply to them
  Challenge schema: for every argument type the profile exhibits a generic template
      ⟨ target, δ ∈ {unsound, outOfScope, provenanceBroken, dependencyMissing, obligationUnmet, premiseDefeated, forged}, reason, discriminator ⟩
  so that every admitted argument has a constructible eligible challenge

Admission is status-blind, with noninterference
  eligibleAdmit(w, r) iff WellFormedCertificate(w) ∧ refs(w) ⊆ Versions(r) ∧ ScopeCompatible(w, r)
  ScopeCompatible(w, r) is a function of declaredScope(profile) and refs(w) only
  Theorem obligation: eligibleAdmit is invariant under any change to J_raw, J_adj, responses, retentions, or other certificates
  A scope exclusion is recorded as a claim Excluded(w, reason), which is content and attackable
  A recorder who wishes to reject w does so by a Criticize occurrence targeting w (§7.3), never by declining to admit

Inhabitation
  for every relation the profile evidences (§8), the negative witness type has at least one well-formed inhabitant template,
  exhibited in the profile; a profile whose negative type is empty is invalid

No stored status; every judgment stamped
  every status is a function of a configuration (§7); nothing stores, caches, or carries a status forward;
  every reported judgment carries its kernel version, profile version, and cut digest (§7.7)
```

What the contract does not say: that the target system will act again, recover, or retain anything. Those are capacity claims (§17), made under declared enabling conditions. The recordability theorem does not require the target system to be the actor; a recorder can criticise after the author is gone. It excludes the lock event that defeated Revision C, because a lock would have to share an alternative set with the criticism, and it no longer contradicts heredity, because it asks only that the criticism be compatible with the record it is added to.

## 6. Spans, current versions, dispositions, lapse

### 6.1 Spans

```text
Span q = ⟨ roots : Finset Event, events : Finset Event ⟩
Axioms: roots ⊆ events; every root has kind Attend; every e ∈ events is connected to a root by a path in (≼ ∪ ≽) within events
q ∩ r            := q.events ∩ r
Versions(q, r)   := ⋃_{e ∈ q ∩ r} created(e)
RootProblem(q, p, b) iff ∃ e ∈ q.roots carrying an OpenProblem witness for (p, b)
```

Spans overlap when they share events. Span membership is a reporting structure; it establishes no lineage (§14 requires a provenance path).

### 6.2 Current versions (reporting only)

```text
current(x, q, r) := <_c-maximal elements of { y ∈ Versions(q, r) ∪ {x} | DescEq(x, y) }
```

Possibly several under concurrency. Classifiers do not use it; they use `result` of a response.

### 6.3 Disposition set

```text
Dispositions(x, q, r) := { outcome(σ) | Respond(e; s, σ) ∈ q ∩ r, DescEq(x, target(σ)), e maximal under ≼ among such events }
```

Reported with every classification; required by none. Several incompatible members are reported as contested.

### 6.4 Diversion, lapse, cut

```text
ObservedDiversion(s, q, r)   prefix fact: ∃ e ∈ r \ q.events, kind(e) ∈ {Attend, AttentionShift}, actor(e) = s, e not ≼-below any event of q ∩ r
LapseCertificate(q, r)    a certificate (§7) whose claim is Lapsed(q, r, cause), cause ∈ {abandoned, interrupted, exhausted, unknown}
```

Diversion proves attention elsewhere, not abandonment. `unknown` is legitimate. The cut is external and inert (§21). The value organisation causes `Attend` and `AttentionShift` events; it is a causal priority organisation and is not labelled physical knowledge anywhere before §20.

### 6.5 Merge

A `Merge(e; q_from, q_into)` event creates a provenance link and nothing else. Span membership is never rewritten. The merged view at a cut is computed and is *forward-only*: it forwards the source span's events that come after the merge into the receiving span's view, and leaves the source span's earlier history where it was.

```text
mergedEvents(q_into, r) := (q_into.events ∩ r) ∪ ⋃ { e' ∈ q_from.events ∩ r | Merge(e; q_from, q_into) ∈ r ∧ e ≼ e' }
```

An absorption reading that pulled the source's earlier events into the receiver would rewrite history and is not provided.

## 7. Evidence: the kernel applied to itself

### 7.1 Certificates

```text
Certificate w = ContentVersion with role certificate and
  payload(w) = ⟨ claim : Formula, polarity : Polarity, body : WitnessPayload(claim, polarity),
                 scope : Scope, provenance : Provenance, dependencies : Finset VersionId, essential : Finset VersionId,
                 annotations : Finset VersionId, integrity : Integrity ⟩
WellFormedCertificate(w) iff every payload field is typed, body has the witness type declared for (claim, polarity) in §8,
                             essential ⊆ dependencies, annotations ∩ essential = ∅,
                             and dependencies ∪ annotations name versions in Versions(⇓creator(w) \ {creator(w)})
Admitted(w, r)           iff  ∃ e ∈ r, kind(e) = Admit, w ∈ created(e)
```

Because the admission is an event, "the certificate is present at cut r" means its `Admit` event is in `r`. No timestamp is needed; the causal order of the shared event structure is the clock. Recorders' events and the system's events are compared by that order and by nothing else.

`essential` names the premises without which the body does not establish its claim — the adequacy certificate an improvement body relies on, the standard a criticism applies, the completeness guard a universal derivation needs. `annotations` name cited material that is historical provenance only. Defeating an essential premise defeats the certificate (§7.3); defeating an annotation does not. A body's schema (§§11–12, §16) says which of its fields are essential, which are annotations, and which are sub-claims with their own witnesses.

### 7.2 Raw ledger (Belnap)

```text
W⁺_raw(φ, r) := { w | Admitted(w, r) ∧ claim(w) = φ ∧ polarity(w) = pos }
W⁻_raw(φ, r) := { w | Admitted(w, r) ∧ claim(w) = φ ∧ polarity(w) = neg }
J_raw(φ, r)  := ⟨ W⁺_raw(φ, r), W⁻_raw(φ, r) ⟩

state⟨W⁺, W⁻⟩ = OPEN if both empty | SUPPORTED if only W⁺ nonempty | REFUTED if only W⁻ nonempty | CONTESTED if both nonempty
```

Represent a state as the pair of bits `(pos ≠ ∅, neg ≠ ∅)`. Both Belnap orders are then defined extensionally and their four cover edges each are derived, not drawn:

```text
(a⁺, a⁻) ≤_k (b⁺, b⁻)  iff  a⁺ ≤ b⁺ ∧ a⁻ ≤ b⁻        knowledge:  OPEN ≤ SUPPORTED, OPEN ≤ REFUTED, SUPPORTED ≤ CONTESTED, REFUTED ≤ CONTESTED
(a⁺, a⁻) ≤_t (b⁺, b⁻)  iff  a⁺ ≤ b⁺ ∧ b⁻ ≤ a⁻        truth:      REFUTED ≤ OPEN, REFUTED ≤ CONTESTED, OPEN ≤ SUPPORTED, CONTESTED ≤ SUPPORTED
Theorem: r ⊆ r' → J_raw(φ, r) ≤_k J_raw(φ, r')         (Admitted is monotone in r)
```

The raw state of a claim can reach CONTESTED and stay there under further evidence. That is not immunity. It is the projection forgetting multiplicity. Openness is the contract of §5: a further attack is always eligible.

### 7.3 Attacks, dependency propagation, and adjudication

```text
Attack c     := a criticism occurrence whose target is a certificate, an attack, or a standard, alleging a defect in it:
                unsound (its claim fails), out of scope, provenance broken, dependency missing, obligation unmet, forged
Arguments(r) := { w | Admitted(w, r) } ∪ { c | ∃ e ∈ r, c ∈ created(e), role(c) = criticism }
Standards(r) := { k ∈ Versions(r) | role(k) = standard }
Nodes(r)     := Arguments(r) ∪ Standards(r)
essential(x) := for a certificate, its essential field; for a criticism occurrence or a standard, ∅ for the purposes of propagation
                (a criticism's standard is recorded in its template; see below for why it does not propagate)

attacks(c, t)   iff  c ∈ Arguments(r) ∧ t ∈ Nodes(r) ∧ target(c) = t                                         (direct)
attacks*(c, t)  iff  attacks(c, t) ∨ ∃ d ∈ essential(t), attacks*(c, d)                                      (propagated along essential dependencies)
```

Theories and conjectures are not nodes. A criticism of a theory is an argument, and other criticisms may attack it, but its target is not thereby "out": whether a theory survives criticism is what the response events and the classifiers of §14 are about, not what adjudication decides. Standards *are* nodes, because certificates use them as premises; an unanswered criticism of a standard defeats every certificate that essentially relies on it.

Propagation runs through the essential premises of **certificates only**. It does not run automatically into criticisms that used a defeated standard, and this is a deliberate restriction: if two criticisms each attacked the other's standard, automatic propagation would make each attack the other and the graph would have a cycle. To defeat a criticism whose standard has been defeated, attack the criticism directly with δ = premiseDefeated, citing the standard's defeat; the challenge schema of §5 provides the template. This keeps the attack graph acyclic (below) at the cost of one explicit event, which is the right trade: the event is itself content and can be answered.

Positive and negative certificates for the same claim do **not** attack each other by default; their coexistence is exactly what CONTESTED reports. Only an explicit attack, or its propagation along an essential edge, is an attack.

```text
F_r(S)   := { x ∈ Arguments(r) | ∀ c, attacks*(c, x) → ∃ d ∈ S, attacks*(d, c) }       (defence)
G(r)     := least fixed point of F_r                                                   (grounded extension)
Labels   : in (∈ G(r)) | out (attacked* by a member of G(r))
```

Adjudicated ledger and state:

```text
W⁺_adj(φ, r) := W⁺_raw(φ, r) ∩ G(r)
W⁻_adj(φ, r) := W⁻_raw(φ, r) ∩ G(r)
J_adj(φ, r)  := ⟨ W⁺_adj(φ, r), W⁻_adj(φ, r) ⟩ ;  state as in §7.2
```

Every report shows both `J_raw` and `J_adj`. A claim supported in the raw ledger and open in the adjudicated one is a claim whose only witness is under an unanswered attack, directly or through a premise it essentially relies on. A claim that was adjudicated SUPPORTED and becomes OPEN or REFUTED at a later cut has had its positive witness defeated: this is how a certificate turns out to have been wrong, which §5 requires to remain possible. Being out of `G(r)` is loss of the selected form of support, not falsity; being in `G(r)` is survival of recorded attack, not truth (§7.6).

```text
Theorem (well-definedness of propagation): the essential-dependency graph on Nodes(r) is acyclic, because every essential premise
         lies in the strict causal past of the certificate or criticism that names it (§7.1, §3). Hence attacks* is the least
         fixed point of a monotone closure on a finite relation, and is itself a fixed relation on Nodes(r).
Theorem (acyclicity of attack): attacks* restricted to Arguments(r) is acyclic. Certificates never attack, so they are sinks;
         every edge into a criticism is a direct attack, whose target lies in the strict causal past of the attacker (§3 grounding);
         so a cycle would consist of criticisms alone and would order one of them strictly before itself.
Corollary: on an acyclic framework the grounded, complete, preferred, and stable extensions coincide, G(r) is the unique complete
         extension, and every argument is labelled in or out. There is no undecided label and no semantics choice for the slice.
Theorem: G(r) is well defined for every finite r (F_r is monotone on a finite powerset lattice).
Fact:    J_adj is not monotone in r under ≤_k or ≤_t; expected, and exhibited by the fixture at r₂ and r₃.
Theorem: no argument is unattackable — every x ∈ Nodes(r) is the target of an eligible template by the challenge schema of §5.
```

A logical mutual attack — two arguments each attacking the other — cannot be created by two `Criticize` events, since each must target something already in its past. If a profile needs to represent mutual opposition, it does so as a *recorded relation between propositions*, which is content, not as two occurrences; the first slice does not provide this and does not need it.

The policy view of Revision C is gone. Admissibility decisions are attacks; attacks are content; content is criticisable. What remains a declared choice is which edges exist — targets and essential dependencies — and both are stated in the certificate and template schemas rather than chosen by an evaluator.

### 7.4 Derivations for compound claims

Witness sets for compound formulas are defined by derivations, which denote elements of the product without enumerating it:

```text
Pos(φ)          ::= atom(w)           w ∈ W⁺_·(φ, r)
Pos(φ ∧ ψ)      ::= andIntro(Pos φ, Pos ψ)
Pos(φ ∨ ψ)      ::= orLeft(Pos φ) | orRight(Pos ψ)
Pos(¬φ)         ::= negIntro(Neg φ)
Pos(∃x∈R. φ x)  ::= exIntro(a, Pos(φ a))                  a ∈ R named in the dossier
Pos(∀x∈R. φ x)  ::= allIntro(CompleteRange(R, snapshot), { Pos(φ a) | a ∈ R })

Neg(φ)          ::= atom(w)           w ∈ W⁻_·(φ, r)
Neg(φ ∧ ψ)      ::= andLeft(Neg φ) | andRight(Neg ψ)
Neg(φ ∨ ψ)      ::= orBoth(Neg φ, Neg ψ)
Neg(¬φ)         ::= negElim(Pos φ)
Neg(∃x∈R. φ x)  ::= exRefute(CompleteRange(R, snapshot), { Neg(φ a) | a ∈ R })
Neg(∀x∈R. φ x)  ::= allRefute(a, Neg(φ a))
```

`W⁺(Φ, r)` for a compound `Φ` is the set of derivations; `state` uses non-emptiness only.

```text
leaves(d) := every atom certificate in d ∪ every CompleteRange certificate used as a guard in d
usable(d, r) iff ∀ w ∈ leaves(d), w ∈ G(r)
```

A derivation is in the adjudicated set iff it is usable. The completeness guard is a leaf, not a constructor argument that vanishes from adjudication: defeat the guard and the universal derivation is unusable while every instance still stands. Heterogeneous witnesses are never unioned; a derivation tags which side it came from. The ledger stores atoms once and derivations as references. Independent alternative derivations remain available: one usable derivation suffices for SUPPORTED.

Quantifiers in `J` range over a dossier-named finite range `R`; quantifiers in `M` (§7.6) range over the model domain. The two agree only under a completeness certificate.

### 7.5 Completeness certificates

```text
CompleteRange(R, sort, scope, snapshot : Config, digest, lossModel, provenance)
  claim: the named range R exhausts, within scope, the elements of the sort present in the immutable snapshot
Instances required by the slice
  EventRecordCompleteness(kinds K, span q, snapshot)     licenses: absence of an event of kind ∈ K in q ∩ snapshot is a negative atom for span-indexed existence claims
  RepertoireCompleteness(s, e_x, ℓ, β, snapshot)         licenses: absence of an ℓ-equivalent in the audited pre-entry repertoire is a positive atom for NewBefore
  VariantFamilyCompleteness(V, X, snapshot)              licenses: allIntro over V(X) for HTV (§18)
```

A completeness certificate is itself a certificate: content, admitted by an event, attackable. Its snapshot is a configuration fixed by digest; it never certifies a record that contains its own admission. Without the certificate, absence yields OPEN and a universal yields OPEN. Its claim is exactly what it says — that the named range exhausts the sort *within the snapshot* — and it never promotes snapshot coverage to a claim about the model domain or about variants no one has imagined.

### 7.6 Model truth and soundness

```text
M = ⟨ D, ES, R₀, β, I ⟩         I interprets every relation of §8 classically over the sorts of §1
M, r ⊨ φ                        ordinary sorted first-order truth at configuration r; quantifiers over the model domain
sound_M(w, r)  iff  (polarity(w) = pos → M, r ⊨ claim(w)) ∧ (polarity(w) = neg → M, r ⊨ ¬claim(w))
```

Soundness is never required for admission (§5). A negative certificate can be wrong while the relation holds; a relation can fail while no negative certificate exists. Non-entailment is proved by a model that satisfies the premises and falsifies the conclusion (§22), never by an evidence state.

### 7.7 Judgments and versions

```text
Judgment j = ⟨ claim, cut : Digest, kernel : KernelVersion, profile : ProfileVersion, raw : state, adj : state,
               leavesUsed : Finset VersionId, supersedes : Option Judgment ⟩
```

A judgment is a report, not a status; it is recomputed from the configuration whenever asked. Its version stamp records which rules and which profile produced it. Re-evaluating a claim under a revised kernel or profile produces a new judgment that names the old one in `supersedes`; the old judgment remains reproducible as the evaluation it was.

Scope of recursion, declared. In-kernel recursion covers content, certificates, attacks, and standards: each is a version, each can be criticised, and the criticism has effect through §7.3. Revising the rules of §§2–7 or the evaluator that computes `G` is a *versioned external act*: it changes `kernel`, and every later judgment says so. Nothing here requires an evaluator that rewrites itself while running, and nothing makes the current rules final.



## 8. Domain profile

A profile supplies, for each relation below, a classical interpretation in `M` and an inhabited witness type in each polarity. A validity predicate for a witness body is stated in the section that uses it; **every field of a body is either checked by that predicate, marked annotation and excluded from validity, or a sub-claim with its own witnesses.**

| Relation in M | Meaning | Positive body | Negative body |
|---|---|---|---|
| `Job(x,p,b)` | `x` purports to address `p` against `b` | the system's own deployment of `x` as an answer to `p` | analyst-imposition record |
| `Represents(s,z,e)` | at `e`, `s` carries `z` in a discriminable, causally used state | discriminability and use record | idle-label record |
| `Deployable(s,y,e)` | `s` could use `y` in a problem-bearing operation at `e` | deployment or reconstruction trace | inaccessibility record |
| `Deployable₀(s,y)` | `s` could use initial content `y` before any recorded event | initial deployment audit | initial inaccessibility record |
| `Recognises(s,r_org,τ,p)` | recognition organisation `r_org` of `s` takes tension `τ` as problem `p` | recognition record under intervention | mis-recognition record |
| `Matters(s,v,τ,p)` | priority organisation `v` of `s` allocates resources to `τ` as `p` | allocation record | indifference record |
| `Crossed(y,β,ch,e)` | `y` entered through declared channel `ch` of `β` at `e` | channel log | no-crossing audit |
| `BearsOn(k,p,b)` | standard `k` bears on `p` against `b` | bearing argument | irrelevance argument |
| `Defect(c,x,p,b,k,δ)` | `c` alleges `δ` in `x` under `k` | structured criticism | ill-formedness record |
| `RoleUsed(s,X,ρ,e)` | link role `ρ` of object `X` is causally used by `s` at `e` | role-sensitive intervention record | idle-role record |
| `Addresses(y,δ)` | `y` addresses `δ` | addressing record | persistence record |
| `Preserves(y,x,m)` | merit `m` of `x` survives in `y` | preservation record | loss record |
| `MaterialCommitment(x,m,p,b)` | `m` is a material commitment or merit of `x` relevant to `(p,b)` | commitment inventory | irrelevance record |
| `Adeq(x,p,b)` | `x` is currently adequate for `p` against `b` (one relation, two polarities) | adequacy certificate | refutation certificate |
| `SameJob(x,x',p,b)` | same explanatory job | same-job record | different-job record |
| `MaterialVariant_V(x,x')` | `x'` alters a content-bearing part of `x` within `V` | variant construction | triviality record |
| `AdditionalRepair(x,x')` | `x'` needs new explanatory work to hold | repair inventory | no-repair record |
| `Authors(s,x,p,b,β)` | causal credit for the problem-specific organisation of `x` lies inside `β` | OriginBody (§12) | transfer-provenance body |
| `UsesReason(s,c,σ)` | the reason content of `c` makes a defect-appropriate difference to `σ` | ReasonUseBody (§11) | generic-compliance body |
| `K_E(y,p0,b0,p1,b1)` | `y` is a fallible improvement of the situation from `(p0,b0)` to `(p1,b1)` | ImprovementBody (§16) | worse-situation body |
| `Accessible(s,y,r)` | a token or reconstructible disposition for `y` is available to a later operation of `s` at `r` | retention body | loss body |
| `StableOrg(s,Q,χ,Ω)` | organisation `Ω` of `s` is causally stable over `Q` under `χ` | stability body over declared perturbations | destruction or exhaustion body |
| `SameOrg(Ω,Ω',s,e,e')` | `Ω'` at `e'` is the same or a reconstruction of `Ω` at `e` | reconstruction body | divergence body |
| `Lapsed(q,r,cause)` | span `q` lapsed at `r` for `cause` | lapse body | continuation body |
| `True(x,p,b)` | optional independent correspondence relation | if supplied: truth body | if supplied: falsity body |
| `sameContent_ℓ` | equivalence at level `ℓ` | equivalence proof or audit | distinctness proof |

`Adeq` is one relation with two witness polarities, not two relations. `Explains` does not appear; §10 divides its work.

## 9. Newness

Newness is measured against what the system could deploy, through its boundary, before the entry event.

```text
R₀(s, β) ⊆ R₀                declared initial content accessible to s at boundary β; a subset of the global initial set of §3
Available(s, y, β, e_x)      iff  y ∈ R₀(s, β) ∨ (∃ e ≺ e_x, y ∈ created(e) ∧ actor(e) = s) ∨ (∃ e ≺ e_x, ∃ ch, Crossed(y, β, ch, e))
AccessibleBefore(s, y, e_x, β) iff Available(s, y, β, e_x)
                                   ∧ ( (y ∈ R₀(s, β) ∧ Deployable₀(s, y)) ∨ ∃ e' ≺ e_x, Deployable(s, y, e') )
R_before(s, e_x, β)          := { y | AccessibleBefore(s, y, e_x, β) }
NewBefore(s, x, ℓ, e_x, β)    iff  ∀ y ∈ R_before(s, e_x, β), ¬ sameContent_ℓ(y, x)
NewHistory(x, ℓ, H)           iff  ∀ y ∈ H, ¬ sameContent_ℓ(y, x)
```

Initial content has its own deployability branch, so an entry with no strict predecessor is still measured against what the system could already deploy. Later content is tested for deployability at *any* prior event, so content that became usable after it was first emitted counts. Changing the boundary changes the baseline through `R₀(s, β)` and `Crossed`.

Negative atom: exhibit `y ∈ R_before` with `sameContent_ℓ(y, x)`. Positive atom: `RepertoireCompleteness(s, e_x, ℓ, β, snapshot)` plus distinctness audits. Creative reconstruction can satisfy `NewBefore` and fail `NewHistory`.

## 10. Explanation objects

```text
ExplanationObject X = ⟨ O_X : obligations, C_X : commitments, Λ_X : typed link hypergraph, S_X : scope, A_X : auxiliaries ⟩
Realizes(x, X)          iff  object(x) = some X                                        (a version carries at most one object)
WellFormed_D(X)         iff  every obligation reaches a route ∧ every material commitment is on a route or marked auxiliary ∧ all links well typed
Nondegenerate_D(X,p,b)  iff  ∃ o ∈ O_X tied to p ∧ ∃ m ∈ C_X material ∧ ∃ route in Λ_X from a material commitment to an obligation
                             whose role is not bare output association under D
Anchored(s, X, e)       iff  ∀ ρ ∈ roles(Λ_X), RoleUsed(s, X, ρ, e)
```

Two attempted-explanation predicates are kept during migration; choosing between them is a human adoption decision (gate D10):

```text
Attempted_CR1(s, x, p, b, e)  iff  Represents(s, x, e) ∧ Represents(s, p, e) ∧ Job(x, p, b)
ExpCandidate(s, x, p, b, e)   iff  Attempted_CR1(s, x, p, b, e) ∧ ∃ X, Realizes(x, X) ∧ WellFormed_D(X) ∧ Nondegenerate_D(X, p, b) ∧ Anchored(s, X, e)
```

An empty object fails `Nondegenerate`. An oracle with no commitment graph fails it because it has no route. A graph drawn by an analyst and causally idle for the system fails `Anchored`. A false, poorly structured, or tacit conjecture that purports to explain a represented problem passes `Attempted_CR1` and may fail `ExpCandidate`; whether the strong predicate replaces or refines the weak one is exactly the decision the migration defers.

## 11. Criticism, response, reason use

```text
Criticism c = occurrence of Template ⟨ target, p, b, δ, k, reason, discriminator, merits : Finset Merit ⟩ with an optional coverage certificate
WellFormedTemplate(t)           iff  every field typed; target(t) a ContentVersion; k has role standard; reason nonempty
WellFormedCriticism(c)          iff  WellFormedTemplate(templ(c))
StructuredCriticism_D(c,x,p,b)  iff  WellFormedCriticism(c) ∧ target(c) = x ∧ (p(c), b(c)) = (p, b) ∧ Defect(c, x, p, b, k, δ) ∧ BearsOn(k, p, b)
MeritCoverage(c)                := the claim  ∀ m, MaterialCommitment(target(c), m, p(c), b(c)) → m ∈ merits(c) ∨ excluded(c, m, reason)
```

`merits` is fixed by the criticism, never after the response. `MeritCoverage` is a claim with its own witnesses: its negative atom exhibits a material commitment omitted without a reason. Predeclaration blocks post-hoc deletion; coverage blocks strategic undercoverage; coverage is itself fallible and attackable. `standard(c)` is recorded in the template. A criticism whose standard has been defeated is not automatically defeated; it is attacked directly with δ = premiseDefeated (§7.3), so that the attack graph stays acyclic.

Responses are §4.2. Reason use is the relation `UsesReason(s, c, σ)` with this positive body and validity:

```text
ReasonUseBody u = ⟨ e_r, σ, c,
                    paraphrase : (variants of c preserving reason content, responses under each, sameResponse : Bool),
                    defectChange : (variants of c altering δ, responses under each, redirected : Bool),
                    irrelevantSignal : (negative signals lacking c's reason content, responses, noRepair : Bool),
                    invalidCriticism : (invalid variants of c, responses, reasonedRejection : Bool),
                    matching : MatchingConditions, scope, provenance ⟩
ValidReasonUse(u, r)  iff  Respond(e_r; s, σ) ∈ r ∧ crit(σ) = c ∧ each intervention family is nonempty and admitted by r
                           ∧ sameResponse ∧ redirected ∧ noRepair ∧ reasonedRejection ∧ matching conditions met
```

The four Booleans are conjuncts, each derived by a declared comparison over the recorded responses in its family — a flag is not entered by hand. Essential: the four families and their comparisons. Annotations: `matching`'s narrative and `provenance`'s free text. Sub-claims: each family's recorded responses are themselves observation content and may be attacked. A body that records failed interventions is well-formed and invalid. Where tacit cognition cannot be discriminated under interventions, the state is OPEN, not REFUTED. For `outcome = ignore`, the same body applies to the reason record `u` the response created; a content-insensitive refusal fails `defectChange`.

## 12. Authorship

`Authors(s, x, p, b, β)` is a relation in `M`. Its positive body and validity:

```text
OriginBody o = ⟨ β, channels : Finset Channel, provGraph, organisation : problem-specific organisation extracted from x,
                 path : internal construction or reconstruction path, interventions : matched interventions on path,
                 externals : stores, prompts, tools, evaluators, selectors, alternatives : alternative provenance explanations,
                 crossings : complete list of boundary crossings bearing on x, scope, ℓ, evidence ⟩
ValidOrigin(o, r)  iff  path is nonempty and every step is an event of actor s in r
                        ∧ interventions on path change organisation in the declared contrasts (recorded outcomes, not fields)
                        ∧ crossings is certified complete by a CompleteRange over the crossing records of β within the snapshot
                        ∧ no crossing in crossings carries a deployable organisation sameContent_ℓ-equivalent to organisation
                        ∧ each alternative in alternatives is answered by a recorded discriminating intervention
```

Essential: `path`, `interventions`, `crossings` with its completeness certificate, and `alternatives` with their answers. Annotations: `provGraph`, `externals`, `channels` (they locate the audit; they do not decide it). Sub-claims: each intervention outcome and each crossing record. Prior knowledge, training, communication, search, imitation, deduction, and randomness are not disqualifiers. What disqualifies is a crossing that already carried the deployable organisation. The certificate may be attacked like any other.

## 13. Originative creative act

OCA returns a witness so that later classifiers can use its entry event.

```text
OCAWitness ow = ⟨ s, x, p, b, q, e_p, e_x, mode, ℓ, β ⟩
ValidOCAWitness_weak(ow, r)  iff
    e_p ∈ q.roots ∩ r ∧ e_p carries an OpenProblem witness for (p, b)
    e_x ∈ q ∩ r ∧ EnterConjecture(e_x; s, x, p, b, mode)
    ¬(e_x ≺ e_p)
    (e_p ∥ e_x → tension(e_x) = some τ(e_p))                 concurrency requires co-constitution: the entry names the tension the problem-opening attends to
    Represents(s, p, e_x)
    Attempted_CR1(s, x, p, b, e_x)
    NewBefore(s, x, ℓ, e_x, β)
    Authors(s, x, p, b, β)
ValidOCAWitness_strong(ow, r) iff  ValidOCAWitness_weak(ow, r) ∧ ExpCandidate(s, x, p, b, e_x)

OCA_weak(s, x, p, b, q, r)   iff  ∃ ow, ValidOCAWitness_weak(ow, r)   ∧ (ow.s, ow.x, ow.p, ow.b, ow.q) = (s, x, p, b, q)
OCA_strong(s, x, p, b, q, r) iff  ∃ ow, ValidOCAWitness_strong(ow, r) ∧ (ow.s, ow.x, ow.p, ow.b, ow.q) = (s, x, p, b, q)

The boundary β and level ℓ are carried by the witness and reported with it; a caller's attribution context is never silently replaced.
```

No criticism, success, truth, retention, generality, or historical firstness. A system that acts once and stops can satisfy both. Evidence: `Attempted_CR1` and `ExpCandidate` by their bodies; `NewBefore` by repertoire completeness; `Authors` by a valid origin body admitted by `r`.

## 14. Critical creative process, lineage-connected

```text
ProvPath(ow, x1, r)  iff  ∃ x_0 … x_n with x_0 = ow.x, x_n = x1, ∀ i < n, contentParent(x_i, x_{i+1}) ∧ creator(x_{i+1}) ∈ r
                          (n = 0 allowed: the criticised version is the originating one)

CCPWitness cw = ⟨ ow, x1, c, σ, a, e_c, e_r, y, p1, b1 ⟩
ValidCCPWitness(cw, r)  iff
    ValidOCAWitness_weak(ow, r)
    ProvPath(ow, x1, r)
    e_c ∈ ow.q ∩ r ∧ Criticize(e_c; a, c) ∧ StructuredCriticism_D(c, x1, ow.p, ow.b)
    e_r ∈ ow.q ∩ r ∧ Respond(e_r; ow.s, σ) ∧ crit(σ) = c ∧ target(σ) = x1 ∧ e_c ≺ e_r
    result(σ) = some y ∧ situation(σ) = (p1, b1)
    Represents(ow.s, c, e_r)                                   the responder carries the criticism, whoever authored it
    UsesReason(ow.s, c, σ)
    Represents(ow.s, y, e_r) ∧ Represents(ow.s, p1, e_r) ∧ Deployable(ow.s, y, e_r)

CCPResult(s, y, p0, b0, p1, b1, q, r)  iff  ∃ cw, ValidCCPWitness(cw, r) ∧ (cw.ow.s, cw.ow.p, cw.ow.b, cw.ow.q, cw.y, cw.p1, cw.b1) = (s, p0, b0, q, y, p1, b1)
CCP(s, p0, b0, q, r)                    iff  ∃ y p1 b1, CCPResult(s, y, p0, b0, p1, b1, q, r)
SelfCritical(cw)                        iff  actor(cw.e_c) = cw.ow.s
AnySelfCritical(s, q, r)                iff  ∃ cw, ValidCCPWitness(cw, r) ∧ cw.ow.s = s ∧ cw.ow.q = q ∧ SelfCritical(cw)
```

Lemma: `ow.e_x ≼ e_c`. The originating version is created at `ow.e_x`; `ProvPath` orders creators along ancestry; the criticised target lies in the strict causal past of `e_c` by grounding. The inequality is therefore derived, not assumed; an implementation may check it as a sanity condition but no fixture depends on it as a separate guard.

The criticism may come from the system or from a recorder; the response must be the system's, and the system must represent the criticism it answers — inexplicitly is fine, but a response to a criticism the system never carried is not a critical process. Outcomes with `result = none` (`suspend`, `ignore`) do not yield a `CCPResult`; they are reported as dispositions. A CCP can end worse than it began. Span membership contributes nothing to lineage; `ProvPath` does.

## 15. Three claims at a later cut

At `r2 ⊃ r1`, three claims about a correction certificate `κ` issued at `r1` (§16.4) are distinct in type:

```text
CorrectedAt(y, q, r1)                    prefix fact in M: the Criticize, Respond, and Admit(κ) events are in r1     (monotone)
M, r2 ⊨ ValidCorrection_D(κ)            model truth about κ's obligations                                           (fixed by M)
state(J_adj(ValidCorrection_D(κ), r2))   adjudicated evidence about that validity                                      (may move)
state(J_adj(Adeq(y, p1, b1), r2))        adjudicated evidence about current adequacy                                   (may move)
```

A later `Criticize` of `y` is content. It changes the fourth only when an `InterpretEvidence` event and a negative adequacy certificate are admitted; it changes the third only if it is an attack on `κ` that is not itself defeated; it never changes the first. The content of `y` is unchanged throughout.

---

## Part III. Later slices, specified in closed form

These sections are written to type-check but are not claimed for `cr2/0.1`.

## 16. Success

### 16.1 The judgment

`K_E(y, p0, b0, p1, b1)` is a domain relation in `M`. No local repair defines it; the audit's destructive-local-repair model (fix the notation, wreck the mechanism, disclose everything) is a model where `Addresses` holds and `K_E` fails.

### 16.2 Rival comparison, preference, defeat

```text
Comparisons(p, b, r)  := { κ | CompareRivals(e; s, κ) ∈ r, (p(κ), b(κ)) = (p, b), e maximal under ≼ among such events }
Preferred(x, p, b, r) := { κ ∈ Comparisons(p, b, r) | pref(κ) = x }                    a set; several maximal comparisons are reported, not collapsed
Defeated(x, r)        iff  ∃ Respond(e; s, σ) ∈ r with outcome(σ) = reject ∧ target(σ) = x ∧ crit(σ) ∈ G(r)
                           (the rejecting criticism survives adjudication; a rejectCriticism response creates a criticism occurrence targeting it, which is an attack)
GoodNow_V(s, x, p, b, r)  iff  ∃ ow, ValidOCAWitness_weak(ow, r) ∧ (ow.s, ow.x, ow.p, ow.b) = (s, x, p, b)
                               ∧ Adeq(x, p, b) ∧ ¬Defeated(x, r) ∧ HTV_V(x, p, b) ∧ Preferred(x, p, b, r) ≠ ∅
```

`GoodNow` does not entail `True`, finality, or wide reach.

### 16.3 Target-correct correction certificate

```text
CorrectionBody κ = ⟨ x_origin, x_target, c, σ, y, p0, b0, p1, b1, e_c, e_r, Δk : Finset Standard,
                     addressing : witness for Addresses(y, δ(c)),
                     preservation : ∀ m ∈ merits(c), witness for Preserves(y, x_target, m) ∨ tradeoff(m) : comparability argument,
                     coverage : witness for MeritCoverage(c),
                     standardComparison : Option comparability argument, required iff Δk ≠ ∅ (Δk lists standards used to assess y beyond k(c)),
                     openProblems : Finset Problem ⟩                        annotation: reported, never checked
ValidCorrection_D(κ)  iff  DescEq(x_origin, x_target) ∧ target(c) = x_target ∧ target(σ) = x_target ∧ crit(σ) = c
                           ∧ (∃ a, Criticize(e_c; a, c)) ∧ Respond(e_r; s, σ) ∧ e_c ≺ e_r ∧ outcome(σ) = revise ∧ result(σ) = some y ∧ situation(σ) = (p1, b1)
                           ∧ Defect(c, x_target, p0, b0, k(c), δ(c))
                           ∧ addressing valid ∧ every preservation entry valid (a bare loss disclosure is neither) ∧ coverage valid
                           ∧ (Δk ≠ ∅ → standardComparison = some arg ∧ arg valid)
```

Every stored field is either consumed by the predicate or, for `openProblems`, declared an annotation. Essential: `addressing`, `preservation`, `coverage`, `standardComparison`, and the adequacy body the improvement envelope adds.

### 16.4 Outcome-indexed improvement witnesses

The positive body for `K_E` is a sum over outcomes. Every constructor shares a **response-indexed envelope**, and the envelope, not the constructor, fixes which response, result, situations, and comparison the claim is about.

```text
Envelope ε = ⟨ σ, e_r, y, p0, b0, p1, b1, standards, κ_cmp : comparison, adequacy : certificate for Adeq(y, p1, b1), scope, provenance ⟩
EnvelopeValid(ε, r) iff
    Respond(e_r; s, σ) ∈ r ∧ result(σ) = some y ∧ situation(σ) = (p1, b1) ∧ (problem(crit(σ)), background(crit(σ))) = (p0, b0)
    ∧ κ_cmp ∈ Comparisons(p1, b1, r) ∧ standards(κ_cmp) = standards ∧ y ∈ A(κ_cmp)
    ∧ adequacy admitted by r ∧ claim(adequacy) = Adeq(y, p1, b1)
essential(body) ⊇ {adequacy, κ_cmp} ∪ the constructor's own essential premises

ImprovementBody ::=
    RevisionBetter(ε, κ)            outcome(σ) = revise ∧ κ.σ = ε.σ ∧ ValidCorrection_D(κ) ∧ pref(κ_cmp) = y ;              essential ∋ κ
  | RejectionBetter(ε, z)           outcome(σ) = reject ∧ Defeated(target(σ), r) ∧ z ∈ A(κ_cmp) ∧ pref(κ_cmp) = z ∧ target(σ) ∈ A(κ_cmp)
                                    (y is the rejection record; the improvement is the situation in which z is preferred over the defeated target)
  | RivalAdoptionBetter(ε)          outcome(σ) = adoptRival ∧ pref(κ_cmp) = y ∧ (Defeated(target(σ), r) ∨ state(J_adj(Adeq(target(σ), p0, b0), r)) = REFUTED)
  | ReasonedRetentionBetter(ε, c′)  outcome(σ) = retainReasoned ∧ pref(κ_cmp) = y ∧ c′ ∈ G(r) ∧ target(c′) = crit(σ) ;                  essential ∋ c′
  | ReframeBetter(ε, arg)           outcome(σ) = reframe ∧ y = the created problem p1 ∧ arg shows (p1, b1) better posed than (p0, b0) under standards ;   essential ∋ arg
  | RestandardizationBetter(ε, arg) outcome(σ) = restandardize ∧ y = the created standard ∧ arg shows comparability and improvement under y ;           essential ∋ arg
ValidImprovement(body, r) iff EnvelopeValid(ε, r) ∧ the constructor's side conditions hold at r
```

`requestEvidence` and `suspend` yield no improvement body. `ignore` never does. `rejectCriticism` has no constructor of its own in this revision: rejecting a criticism and keeping the theory is `ReasonedRetentionBetter` once a `retainReasoned` response follows; a case in which rejecting a criticism is knowledge growth with no retention to point at is a declared unsupported outcome and a falsification point (§26). These bodies are evidence for `K_E`; they do not define it.

### 16.5 Explanatory knowledge creation

```text
EKC(s, y, p0, b0, p1, b1, q, r)  iff  CCPResult(s, y, p0, b0, p1, b1, q, r) ∧ K_E(y, p0, b0, p1, b1) ∧ Accessible(s, y, r)
```

Retention is availability, not endorsement. `K_E`, not retention, supplies success.

### 16.6 Physical knowledge is a different sort

`K_CT` is declared as a separate relation whose interpretation and bridge belong to §20 and are deferred. Its non-equivalence with `K_E` is a theorem *obligation* for that section and is not counted as discharged here.

## 17. Capacity and disposition, non-vacuous

```text
Chi(s, χ, r)                enabling conditions χ hold for s at r
Applicable(γ, r)            perturbation γ can be applied at r; the identity perturbation γ₀ is applicable everywhere and Perturb(γ₀, r, r)
Perturb(γ, r, r_γ)          a typed transition applying γ to base r; total on applicable pairs: Applicable(γ, r) → ∃ r_γ, Perturb(γ, r, r_γ)

OCap(s, Q, χ, Ω)      iff  Q ≠ ∅ ∧ (∃ r, Chi(s, χ, r)) ∧ StableOrg(s, Q, χ, Ω)
                           ∧ ∀ (p,b) ∈ Q, ∀ r, Chi(s, χ, r) → ∃ r' ⊇ r, r' a Config, ∃ ow,
                                 ValidOCAWitness_weak(ow, r') ∧ (ow.s, ow.p, ow.b) = (s, p, b) ∧ ow.e_x ∈ r' \ r ∧ Supports(Ω, ow, r')

Cap_CR(s, Q, Γ, χ, Ω)  iff  |Q| ≥ 2 ∧ γ₀ ∈ Γ ∧ OCap(s, Q, χ, Ω)
                           ∧ ∀ (p,b) ∈ Q, ∀ γ ∈ Γ, ∀ r, Chi(s, χ, r) ∧ Applicable(γ, r) →
                                 ∀ r_γ, Perturb(γ, r, r_γ) → ∃ r' ⊇ r_γ, ∃ cw,
                                     ValidCCPWitness(cw, r') ∧ (cw.ow.s, cw.ow.p, cw.ow.b) = (s, p, b)
                                     ∧ cw.e_c ∈ r' \ r_γ ∧ cw.e_r ∈ r' \ r_γ                       a new criticism and a new response, after the base
                                     ∧ ∃ e ∈ r, ∃ e' ∈ r' \ r_γ, SameOrg(Ω, Ω, s, e, e')

GCD(s, Q, Γ, χ, Ω)    iff  Cap_CR(s, Q, Γ, χ, Ω) ∧ the same Ω supports, across Q, problem formation, criticism, revision, and transformation of
                           problems or standards, each stated as a continuation pattern in r' \ r_γ and quantified as above
OpenProcess(s, χ)     optional profile: ∀ r, Chi(s, χ, r) → ∃ e ∉ r, actor(e) = s ∧ r ∪ {e} is a Config
```

Because `γ₀ ∈ Γ` and `γ₀` is applicable everywhere, the critical-continuation clause is never vacuous: at minimum the unperturbed base must admit a new critical continuation. `Supports(Ω, ow, r')` is a profile relation with a witness body. Positive evidence accumulates per `(p, b, γ)` from observed continuations plus a stability body. A negative atom must establish that under `Chi` no required continuation exists — destruction or exhaustion of `Ω`, or an exhaustive continuation search under a declared finite branching with a `CompleteRange` certificate over continuations. A failed trajectory is not a negative atom. `UED` stays outside the core.

## 18. Hard to vary and reach

```text
FreeVariant_V(x, x', p, b)  iff  MaterialVariant_V(x, x') ∧ SameJob(x, x', p, b) ∧ Adeq(x', p, b) ∧ ¬AdditionalRepair(x, x')
HTV_V(x, p, b)              iff  ∀ x' ∈ V(x), MaterialVariant_V(x, x') → ¬FreeVariant_V(x, x', p, b)
```

In `M` these are classical. In `J`, `allIntro` over `V(x)` needs `VariantFamilyCompleteness(V, x, snapshot)`; a variant whose `AdditionalRepair` is OPEN leaves `FreeVariant` OPEN. `HTV` is a result for the declared family only. A hard-to-vary candidate is one on which criticism can bind; empirical content is what makes it testable.

```text
ReachBody ρ = ⟨ X, p', b', transported : subgraph of Λ_X, added : background facts, discharged : Finset Obligation ⟩
Obligations_D(p', b')   the profile's obligations for (p', b'); nonempty for any well-posed problem
ValidReach(ρ)   iff  transported ⊆ Λ_X unchanged ∧ discharged = Obligations_D(p', b') ∧ discharged ≠ ∅
                     ∧ every obligation in discharged is reached by a route within transported ∪ added
XReach(X)       := { (p',b') | ∃ ρ, ValidReach(ρ) ∧ (ρ.X, ρ.p', ρ.b') = (X, p', b') }
WideReach_D(X)  iff  ∃ CompleteRange(C, ProblemBackground, scope, snapshot), C ⊆ XReach(X) ∧ C meets the profile's declared coverage predicate
```

## 19. Contrast classes

Model classes over the same signature, to be given full typed definitions in `cr2/0.4`. The classes are defined by what a mechanism *is*, not by what it lacks; the non-creativity properties belong to the particular countermodels of §22, so that each non-entailment tests the difference between being a mechanism of that kind and being a creative one, rather than being definitional.

```text
Generator            a mechanism that emits candidate versions
Predictor            a mechanism that maps conditions to outcome claims
MechanicalDeductor   a mechanism that applies a fixed consequence relation to supplied premises
FixedSearch(D,N,V)   a mechanism that visits D by successor N and evaluator V
Learner(μ,m)         a mechanism whose experience causes persistent change improving performance under μ by metric m
Computer(f) / UniversalComputer(F)   a mechanism that physically realizes encoded relation f / every f ∈ F under a suitable program
NaturalSelection(P,E) heritable variants in P with differential replication in E
```

Each may be a component of a creator. The countermodel for "Computer ⇏ OCA" is *a particular* computer with `Authors` false; it is not the class.

## 20. Physical realization (deferred)

```text
Realization R = ⟨ Θ, β, ctx, tol, ρ_C ⊆ PhysAttr × ContentVersion, ρ_E ⊆ PhysEvent × Event, ρ_I ⊆ PhysIntervention × SemanticIntervention ⟩
```

One indexed structure carries all three component relations, so none can be switched between interventions. Commuting obligations (event occurrence and order; content distinctions; span, ancestry, and result edges; provenance and crossings; reason-specific intervention effects; memory where `Accessible` is claimed; resources, tolerance, noise, repair; the exact predicate attributed) are checked across the declared intervention family. Retained capacity to continue is an obligation only for `PhysOCap`, `PhysCap_CR`, and `PhysGCD`. `PhysOCA` accepts a halting realization. `K_CT`, its adaptation bridge, and the `K_CT`/`K_E` non-equivalence theorem are defined and proved here and nowhere earlier; until this section is built, TH-10 and TH-15 are not counted as replayed.

---

## Part IV. Results and tests

## 21. Theorems about the kernel

| Theorem | Statement | Proof shape |
|---|---|---|
| Eligibility persists | `eligible(t, r) ∧ r ⊆ r' → eligible(t, r')` | presence of the target persists under extension |
| Relative recordability (criticism) | `eligible(t, r) → ∃ e ∉ r, ∃ c, kind(e) = Criticize ∧ templ(c) = t ∧ created(e) = {c} ∧ r ∪ {e} ∈ Config` | Constructor gives `e` with `⇓e \ {e} ⊆ r`; §5's proof shows no `f ∈ r` conflicts with `e` |
| Relative recordability (admission) | `eligibleAdmit(w, r) → ∃ e ∉ r, kind(e) = Admit ∧ r ∪ {e} ∈ Config` | the admission Constructor and the same conflict argument |
| No unattackable argument, constructively | every `x ∈ Nodes(r)` is the target of an eligible template | the challenge schema of §5 instantiates one |
| Admission is status-blind | `eligibleAdmit(w, r)` is invariant under any change to `J_raw`, `J_adj`, responses, retentions, or other certificates | it is a function of `refs(w)` and the declared scope only |
| Ancestry is acyclic | `contentParent` is irreflexive and `<_c` is a strict order | freshness + uniqueness + grounding give `creator(x) ≺ creator(y)` |
| Propagation is well defined | `attacks*` is a fixed relation on `Nodes(r)` | essential edges point into the causal past, so the dependency graph is acyclic and the closure is finite |
| Attack graph is acyclic; semantics coincide | `attacks*` on `Arguments(r)` has no cycle; grounded = complete = preferred = stable; no argument undecided | every direct attack and every essential edge targets the strict causal past |
| Raw ledger is knowledge-monotone | `r ⊆ r' → J_raw(φ, r) ≤_k J_raw(φ, r')` | `Admitted` is monotone in `r`; pair-of-bits order |
| Grounded extension exists | `G(r)` is the least fixed point of `F_r` for every finite `r` | `F_r` monotone on a finite powerset lattice |
| Prefix facts are monotone | any claim "event of kind k with payload θ ∈ r" is preserved under `⊆` | immediate |
| Cut inertness | if `r` and `r'` differ only in which is designated the cut, every `ContentVersion` and every relation of §8 agrees | the cut is not an event and enters no definition except as the evaluation index |
| Terminal creator admissible | there is a model with one valid weak OCA witness and no further event of `s` | §3 has no extension axiom; the recorder may still criticise |
| Empty creative model | a model with `Attend` events only satisfies no OCA, CCP, EKC, or capacity claim | no `EnterConjecture`, so no witness; capacity claims fail because `StableOrg` is false |
| Consistency witness | the fixture of §24 satisfies every axiom of §§2–7 and contains an originative act, an alternative branch, external criticism, and a criticism of a criticism | exhibited, with every event's `refs` listed and every conflict inherited from the one declared alternative set |
| Origin precedes criticism | for every valid CCP witness, `ow.e_x ≼ e_c` | lemma of §14; derived from `ProvPath` and grounding |

Stated facts that are not theorems: `J_adj` is not monotone in `r` (the fixture exhibits SUPPORTED → OPEN → CONTESTED for one claim across `r1`, `r2`, `r3`); the raw state can be absorbed at CONTESTED (multiplicity loss, not immunity); being in `G(r)` is not truth and being out of it is not falsity (§7.6).

## 22. Non-entailments, as countermodels in M

| Claim | Countermodel |
|---|---|
| OCA_weak ⇏ OCap, CCP, EKC, GCD | one `EnterConjecture` with a valid weak witness, then no event of `s`; `StableOrg` false; no `Criticize`; `K_E` false |
| OCA_weak ⇏ OCA_strong | the same model with `object(x) = none` |
| OCap ⇏ CCP, EKC, GCD | `StableOrg` true over a singleton `Q` with OCA continuations; criticism occurrences exist (recorders may add them) but `s` never produces a `Respond` with `UsesReason`, so no CCP witness |
| CCP ⇏ EKC, True | a `revise` outcome with `UsesReason` true and `K_E` false: `Addresses` true, `Preserves` false for a covered merit |
| CCPResult ∧ Accessible ⇏ EKC | the same model with `Accessible` true |
| Generator, Predictor, MechanicalDeductor, FixedSearch, Learner, Computer ⇏ OCA_weak | a particular member of each class with `Job` or `Authors` false; the Predictor countermodel additionally fails `Nondegenerate` |
| UniversalComputer ⇏ GCD | a universal interpreter running a constant program; `Authors` false; no `Respond` by it to any criticism |
| NaturalSelection ⇏ OCA_weak, CCP, K_E | a population in which `Represents` of any problem is false |
| Finite behaviour ⇏ Authors | two models agreeing on every event of every finite configuration; `Authors` true in one, false in the other |
| Finite runs ⇏ OCap, GCD | two models agreeing on every observed configuration and differing in which extensions are configurations |
| GoodNow ⇏ True; HTV ⇏ WideReach; WideReach ⇏ HTV, True | relations independently interpreted; no bridge postulated |
| Correction ⇏ final truth | `ValidCorrection_D(κ)` true and `Adeq(y, p1, b1)` false at a later configuration |
| OCA_weak ⇏ NewHistory | `NewBefore` true with an earlier equivalent in `H` |
| Raw SUPPORTED ⇏ adjudicated SUPPORTED | one positive certificate under an unanswered attack, or whose essential premise is |
| Adjudicated SUPPORTED at r ⇏ adjudicated SUPPORTED at r' ⊃ r | a later attack in `G(r')` on the only positive witness or on one of its essential premises |

Each row must be replayed with a concrete typed model, all §3 axioms checked, and the conclusion explicitly false; the table is the index, not the proof.

## 23. Mutation tests for the slice

| Component | Mutation | Fixture | Expected change | Necessity or encoding? |
|---|---|---|---|---|
| Criticism outside AltSets | admit an AltSet {lock, a Criticize occurrence of the template of `c12`} | Lock fixture | after the lock, no occurrence of that template is recordable; relative recordability fails | Necessity |
| Constructor (criticism) | remove it | Empty-space fixture | eligibility holds, no Criticize event exists | Necessity |
| Constructor over occurrences | quantify the constructor over occurrences instead of templates | Any recorded criticism | a second creator of an existing occurrence is demanded; uniqueness violated | Necessity of the template form |
| Constructor (admission) | remove it | Unrecordable-certificate fixture | an eligible negative certificate has no admission event | Necessity |
| Inhabitation | profile with an empty negative type for `Authors` | Lookup fixture | no origin certificate can ever be refuted | Necessity |
| Admission status-blind | condition `eligibleAdmit` on `J_raw` | Pretext fixture | a negative certificate is unrecordable; the pretext leaves no attack to criticise | Necessity |
| Attack-based rejection | allow a "reject" flag instead of a Criticize event | Pretext fixture | the flag is not an argument; `G(r)` unaffected; rejection unfalsifiable | Necessity |
| Grounded adjudication | use raw ledger only | Seasons `r₂` | a defeated positive witness still counts | Necessity |
| Dependency propagation | use direct attacks only | Seasons `r₂` | `K_E` stays SUPPORTED after its adequacy premise is defeated | Necessity |
| Guard as leaf | drop `CompleteRange` from `leaves` | Defeated-guard fixture | a universal derivation survives the defeat of its completeness guard | Necessity |
| Freshness | let `Activate` create a version with the input's `vid` | Seasons `e0` | freshness violated; the reported invariant is freshness, not a self-parent | Necessity |
| Boundary in newness | drop `Crossed` from `Available` | Boundary-swap fixture | two boundaries classify identically despite an external store | Necessity |
| Deployability at any prior event | test only at the creating event | Late-deployability fixture | `x` counted new though `y` was usable before entry | Necessity |
| Nondegenerate | drop it | Empty-object fixture | an empty object is an explanatory candidate | Necessity for `OCA_strong` |
| Anchored | drop it | Idle-graph fixture | an analyst's graph anchors an oracle | Necessity for `OCA_strong` |
| Public binding | drop the equality in `OCA_weak` | Seasons `r0` | `OCA(XP)` becomes true from the `XA0` witness | Necessity |
| Initial deployability branch | drop it | Initial-content fixture | a copy of initial content counts as new when the entry has no predecessor | Necessity |
| `Represents(s, c, e_r)` | drop it | Unrepresented-criticism fixture | CCP with a criticism the system never carried | Necessity |
| ProvPath | replace with span co-membership | Span-splicing fixture | two causal stories spliced through a shared ancestor pass CCP | Necessity |
| Respond in CCPResult | drop it | Criticism-only fixture | CCP with no response | Necessity |
| ReasonUse Booleans as conjuncts | check presence only | Failed-intervention fixture | a body recording failed contrasts validates | Necessity |
| Origin crossing completeness | drop it | Hidden-channel fixture | a transferred organisation passes | Necessity |
| Merit coverage | drop it | Undercoverage fixture | `merits = ∅` passes preservation vacuously | Necessity |
| Correction target | require `Defect(c, x_origin)` | Proper-descendant fixture | a valid criticism of `XA0.1` cannot be certified | Necessity |
| Envelope identities | drop `κ_cmp ∈ Comparisons(p1,b1,r)` | Unrelated-comparison fixture | a comparison from another controversy validates | Necessity |
| `Q ≠ ∅`, `Chi` inhabited | drop them | Vacuous-capacity fixture | an organisation with no problem class has capacity | Necessity |
| Attention events | remove `Attend`; keep `Represents`, `Recognises`, `Matters` | Noise fixture | no change to the noise result; span rooting lost | Encoding |
| Partial-order events | linearise with interleaving equivalence | Overlap fixture | same classifications at higher cost | Encoding |
| Cut as external index | replace with an inert `Observe` event of a recorder | All | no change | Encoding; the invariant is inertness |
| Four evidence states | another paraconsistent encoding preserving OPEN and CONTESTED | All | no change | Encoding |
| Semantics choice | replace grounded with preferred or stable semantics | All | no change: attack graphs of legitimate histories are acyclic, so the extensions coincide | Encoding; moot for the slice |
| Origin-precedes-criticism check | drop the sanity check | Criticism-before-entry fixture | no change: `ProvPath` and grounding already exclude it | Redundant guard; recorded as a lemma, not a necessity |

## 24. Worked fixture — explanations of seasons

The fixture is also the consistency witness of §21: it contains an originative act, an alternative branch, external criticism, and a criticism of a criticism, and every event lists its references. Admissions are singleton events. Every judgment is stamped `⟨kernel = E, profile = seasons-1, cut⟩`.

### 24.1 Events

| Event | Actor | Kind and payload | `refs` | Purpose |
|---|---|---|---|---|
| `e0` | `s` | `Activate(XP)`, `XP ∈ R₀(s, β)`, `Deployable₀(s, XP)` | `{XP}` | standing conjecture made deployable; no version created |
| `e1` | `s` | `Attend(τ; ω for (p, b))` | `{XP}` (τ names the conflict with `XP`) | opens `p`; root of `q` |
| `e2` | `s` | `EnterConjecture(XA0, p, b, construct)` | `{p, b}` | the tilt account; `object(XA0)` links tilt, orbit, insolation angle, rotational orientation |
| `e2′` | `s` | `EnterConjecture(XB0, p, b, construct)` | `{p, b}` | the alternative the system did not take: a distance-from-Sun account. `AltSets = {{e2, e2′}}`; `e2 # e2′` and every descendant of `e2` inherits conflict with `e2′` |
| `a1` | `rec` | `Admit(w_anchor)` for `Anchored(s, object(XA0), e2)` | `{XA0}` | anchoring body |
| `a2` | `rec` | `Admit(w_rep)` = `RepertoireCompleteness(s, e2, ℓ, β, snapshot {e0, e1})` | `{XP}` | pre-entry repertoire audit |
| `a3` | `rec` | `Admit(w_origin)` for `Authors(s, XA0, p, b, β)` | `{XA0}` ∪ crossing records | origin body |
| `e3` | `s` | `Criticize(c3)`: template ⟨`XP`, `p`, `b`, δ = no constrained mechanism for opposite phases, `k_mech`, reason, discriminator, merits = {annual regularity}⟩; `XP`'s object declares global simultaneity | `{XP, p, b, k_mech}` | scope explicit, so the southern hemisphere refutes rather than exposes missing reach |
| `e4` | `s` | `InterpretEvidence(o4, c3)` | `{c3}` | hemispheric observations bear on `c3`'s discriminator |
| `e5` | `s` | `Respond(σ5)`: crit `c3`, target `XP`, `adoptRival`, referenced `{XA0}`, result `some XA0`, situation `(p, b)` | `{c3, XP, p, k_mech, XA0}` | rejects `XP` by adopting a rival; no ancestry |
| `e5′` | `s` | `Criticize(c5′)`: template ⟨`XA0`, `p`, `b`, δ = ambiguous orbital notation, `k_mech`, …, merits = {phase opposition}⟩ | `{XA0, p, b, k_mech}` | self-criticism of the rival; inherits `# e2′` |
| `e6` | `s` | `Respond(σ6)`: crit `c5′`, target `XA0`, `revise`, created `{XA0.1}`, result `some XA0.1`, situation `(p, b)`; `contentParent(XA0, XA0.1)` | `{c5′, XA0, p, k_mech}` | a minor revision, so the next criticism targets a proper descendant |
| `e7` | `rec` | `Criticize(c7)`: template ⟨`XA0.1`, `p`, `b`, δ = conflates insolation maxima with temperature maxima, `k_time`, …, merits = {phase opposition, annual regularity, reach to tropics and poles}⟩ | `{XA0.1, p, b, k_time}` | external criticism of a descendant |
| `a4` | `rec` | `Admit(w_cov)` for `MeritCoverage(c7)` | `{c7, XA0.1}` | coverage claim |
| `a5` | `rec` | `Admit(w_repc)` for `Represents(s, c7, e9)` | `{c7}` (forward-named event `e9` is bound at admission time by its digest) | the responder carries the criticism |
| `e8` | `s` | `InterpretEvidence(o8, c7)` | `{c7}` | thermal-lag evidence |
| `e9` | `s` | `Respond(σ9)`: crit `c7`, target `XA0.1`, `revise`, created `{XA1}`, result `some XA1`, situation `(p, b′)` | `{c7, XA0.1, p, k_time}` | reason-specific revision of the descendant |
| `e10` | `s` | `CompareRivals(κ10)`: `(p, b′)`, standards `{k_mech, k_time}`, `A = {XA1, XA0.1, XP}`, `pref = XA1` | `{p, b′, k_mech, k_time, XA1, XA0.1, XP}` | actual-rival comparison |
| `e11` | `s` | `Retain(XA1)` | `{XA1}` | availability |
| `a6` | `rec` | `Admit(w_reason)` for `UsesReason(s, c7, σ9)` | `{c7, σ9}` | reason-use body |
| `a7` | `rec` | `Admit(κ)`: correction body `x_origin = XA0`, `x_target = XA0.1`, `σ = σ9`, `y = XA1`; essential `{w_cov}` | `{XA0, XA0.1, c7, σ9, XA1, w_cov}` | correction evidence |
| `a8` | `rec` | `Admit(w_adeq)` for `Adeq(XA1, p, b′)` | `{XA1, p, b′}` | adequacy body |
| `a9` | `rec` | `Admit(w_better)` = `RevisionBetter(ε, κ)` with `ε.σ = σ9`, `κ_cmp = κ10`, `adequacy = w_adeq`; essential `{w_adeq, κ10, κ}` | `{σ9, XA1, κ10, w_adeq, κ}` | improvement evidence for `K_E` |
| `e12` | `rec` | `Criticize(c12)`: target `XA1`, δ = mistimed extreme-temperature predictions, `k_time` | `{XA1, p, b′, k_time}` | later criticism of the theory: content, not yet evidence |
| `e13` | `rec` | `InterpretEvidence(o13, c12)` | `{c12}` | |
| `a10` | `rec` | `Admit(w_adeq⁻)` for `Adeq(XA1, p, b′)`, negative | `{XA1, p, b′}` | negative adequacy body |
| `e12′` | `rec` | `Criticize(att)`: target `w_adeq`, δ = outOfScope (polar data excluded), `k_scope` | `{w_adeq, k_scope}` | attack on a certificate |
| `e14` | `s` | `Criticize(c14)`: target `att`, δ = unsound (the polar data were within scope), `k_scope` | `{att, k_scope}` | criticism of a criticism |

Every direct attack and every essential edge points to an earlier event; the graph is acyclic (§21). All conflicts are inherited from `{e2, e2′}`; every listed configuration below omits `e2′` and is conflict-free.

### 24.2 Core cuts (slice `0.1`)

- `r0 = {e0, e1, e2, a1, a2, a3, e3, e4}`. `OCA_weak(s, XA0, p, b, q, r0)` and `OCA_strong` hold in `M` given `Authors` true and are adjudicated SUPPORTED: `w_anchor`, `w_rep`, `w_origin` are admitted and unattacked. `OCA_weak(s, XP, p, b, q, r0)` is **false**: the only valid witness has `ow.x = XA0`, and the public predicate binds `x`. `CCP` is OPEN in `J` (a criticism of `XP` exists, no response) and false in `M` at this configuration. `Dispositions(XP) = ∅`. Nothing is REFUTED. Judgment stamp: `⟨E, seasons-1, digest(r0)⟩`.
- `r1c = r0 ∪ {e5, e5′, e6, e7, a4, a5, e8, e9, a6, e11}`. `CCPResult(s, XA1, p, b, p, b′, q, r1c)` with witness `cw₁ = ⟨ow(XA0), XA0.1, c7, σ9, rec, e7, e9, XA1, p, b′⟩`; `ProvPath` of length 1 through `e6`; `Represents(s, c7, e9)` by `w_repc`; `SelfCritical(cw₁)` false. A second witness `cw₂ = ⟨ow(XA0), XA0, c5′, σ6, s, e5′, e6, XA0.1, p, b⟩` is self-critical, so `AnySelfCritical(s, q, r1c)` holds. `Dispositions(XP) = {adoptRival}`. No success claim is evaluated at this cut.

### 24.3 Success cuts (slice `0.3`)

- `r1 = r1c ∪ {e10, a7, a8, a9}`. `κ` valid with `x_target = XA0.1 = target(c7)`. `w_better` valid: its envelope's response is `σ9`, its comparison `κ10 ∈ Comparisons(p, b′, r1)` with `pref = XA1`. `EKC(s, XA1, …, r1)` holds in `M` if `K_E` holds and is adjudicated SUPPORTED. `GCD` is OPEN: one span, one problem.
- `r2 = r1 ∪ {e12, e13, a10, e12′}`. `CorrectedAt(XA1, q, r1)` holds; `M, r2 ⊨ ValidCorrection_D(κ)` unchanged. `J_raw(Adeq(XA1, p, b′))` is CONTESTED. `att ∈ G(r2)` (nothing attacks it), so `w_adeq ∉ G(r2)` and `J_adj(Adeq(XA1, p, b′))` is REFUTED. `w_adeq ∈ essential(w_better)`, so `attacks*(att, w_better)` holds and `w_better ∉ G(r2)`: `J_adj(K_E(XA1, p, b, p, b′))` is OPEN — its only positive witness lost an essential premise and no negative improvement body exists. `EKC` in `J_adj` is OPEN. The content of `XA1` is unchanged. `c12` is content: it changes no status until `a10` is admitted, and it attacks nothing (its target is a theory, not a node). `e12` and `e12′` were recordable by relative recordability regardless of `e11`.
- `r3 = r2 ∪ {e14}`. `c14 ∈ G(r3)` (unattacked), so `att ∉ G(r3)`, `w_adeq ∈ G(r3)` again, `w_better ∈ G(r3)` again. `J_adj(Adeq(XA1, p, b′))` returns to CONTESTED (`w_adeq` and `w_adeq⁻` both in `G`); `J_adj(K_E(…))` returns to SUPPORTED. Nothing was stored; every judgment was recomputed and carries `digest(r3)`, with `supersedes` pointing at the `r2` judgment.

Hard-to-vary: `XP`'s object has free variants under a declared family (other gods, other motives, no repair); `XA1`'s does not (remove the tilt or swap the Sun for the Moon and constrained links break). Relative to that family `XA1` is hard to vary; its empirical content is what makes it testable.

## 25. Construction process and gates

| Tag | Active question | Pass condition |
|---|---|---|
| `authority/cr1-frozen` | Preserve CR-1.0 and accepted EIB artefacts | hashes and anchors reproduce |
| `cr2/0.1-recursive-kernel` | Part II | machine-generated symbol table with zero undeclared or free identifiers; §21 theorems proved, including the consistency witness; §24.2 replays at `r0` and `r1c` from definitions alone with version-stamped judgments; every "Necessity" mutation in §23 that touches Part II flips its fixture |
| `cr2/0.2-explanation-profile` | §10 strong predicate | empty, idle, oracle, myth, partial, tacit, and axial-tilt fixtures receive distinct states; migration decision recorded |
| `cr2/0.3-success` | §16 | §24.3 replays at `r1`–`r3`, including the OPEN-then-SUPPORTED movement of `K_E` through dependency propagation; destructive-local-repair model yields `EKC` false in `M`; every field of correction and improvement bodies consumed or declared an annotation; outcome-indexed fixtures pass or stay OPEN |
| `cr2/0.4-provenance-and-contrasts` | §12, §19 | trace-equivalent countermodels differ only in `Authors`; contrast classes fully typed |
| `cr2/0.5-capacity` | §17 | empty `Q`, empty `Chi`, empty `Γ`, and an inapplicable `Γ` cannot satisfy a capacity; a continuation reusing only base events fails; paired-extension countermodels pass; a failed trajectory does not refute |
| `cr2/0.6-physical` | §20 | commuting obligations checked; `PhysOCA` accepts a halting realization; TH-10 and TH-15 replayed here |
| `cr2/0.7-domain-adapters` | profiles | conservative extension passes; **any profile or event space violating §5 is rejected** |

The Revision C audit's gates D0–D13 map onto these: D0–D5 and D7 are `0.1`; D6 is `0.2`; D8 is `0.3`; D9 is `0.5`; D10 (source compatibility: a translation classifying every CR-1.0 core model as expandable, deliberately excluded, or outside the adopted profile) and D11 (exact TH-1–TH-17 replay with transitive dependencies) are obligations of `0.1` through `0.5` collectively and gate D13.

**Verification shape.** In Lean: sorts as types; `≼`, `#`, `contentParent` as relations with the §2–§3 axioms; `Config` as a predicate on finsets; `⊨` as propositions over an interpretation record; the raw ledger as a function from configuration and formula to a pair of finsets; `G` by iteration of `F_r` on a finset, with the fixed-point theorem proved once; derivations as an inductive type. No fixture is phrased as "the run returns v," and no axiom asserts that any configuration has an extension. A harness's output is the pair of ledgers at a cut with its lapse certificate.

## 26. Falsification points

| Conjecture | Revision trigger |
|---|---|
| Configurations of one shared event structure represent both the target history and the evidence history | a case requires evidence ordering that cannot be expressed as causal order among admission events |
| §5 is jointly sufficient for fallibilism | a rule-level immunity is constructible that passes every clause |
| §5 excludes no genuine creative history | a defensible history requires a criticism or admission event to be in an alternative set |
| Essential-dependency propagation is the right propagation | a fixture where a defeated annotation should have defeated its dependent, or a defeated essential premise should not have |
| Attack graphs of legitimate histories are acyclic | a legitimate history whose criticism occurrences form a directed cycle |
| Propagation through certificates only is enough | a fixture in which a defeated standard must automatically defeat the criticisms that used it, so that cycles and the semantics choice return |
| Content-level recursion plus versioned rule revision suffices | a case requires the evaluator to be replaced from inside a judgment |
| Certificates-as-content makes rejection criticisable | a pretext rejection is constructible that no attack can target |
| The cut is inert for content | a case where the stop, not an event, alters a content version |
| Stops need no reason | a classification depends on the system's reason for stopping |
| Nondegenerate and Anchored block empty and idle objects | an empty or idle object passes both |
| `ProvPath` blocks splicing | a spliced history passes CCP |
| `rejectCriticism` needs no improvement constructor | a case where rejecting a criticism is knowledge growth with no retention to attach it to |
| Merit coverage blocks undercoverage | an undercovered merit set passes with coverage valid |
| Outcome-indexed improvement witnesses are the right family | a knowledge-creating outcome fits no constructor and cannot be added conservatively |
| Capacity negatives require destruction or exhaustive search | a single failed trajectory is shown to refute an existential modal capacity |
| The strong OCA is a refinement, not a replacement | the migration test finds a genuine originative act that fails `ExpCandidate` and the project decides to keep only the strong predicate |

---

## Part V. Ledgers

## 27. Declaration ledger, per symbol

Origin: `source` (via CR-1.0's registry), `user_adopted`, or `model_conjecture`. Status: DEF, IMP, DER. Direct dependencies by section; the transitive closure is generated from this table.

| Symbol | § | Origin | Status | Direct deps |
|---|---|---|---|---|
| `Actor`, `Sys`, `Recorder` | 1 | model_conjecture (refines CR-1.0 TY) | DEF | — |
| `Event`, `EventKind` | 1 | model_conjecture | DEF | — |
| `VersionId`, `ContentId` | 1 | model_conjecture | DEF | — |
| `Role` | 1 | model_conjecture | DEF | — |
| `Tension`, `Organisation`, `Defect`, `Merit`, `Outcome` | 1 | model_conjecture; `Organisation` refines CR-1.0 StableOrg vocabulary | DEF | — |
| `Formula`, `Polarity`, `Scope`, `Provenance`, `Integrity`, `Channel` | 1 | model_conjecture | DEF | — |
| `Boundary`, `EqLevel` | 1 | source (CR-1.0 MS-2, TY-2) | DEF | — |
| `Span`, `Config`, `Cut`, `Mode` | 1 | model_conjecture | DEF | 3, 6 |
| `ContentVersion` | 2 | model_conjecture | DEF | 1 |
| `creator`, freshness, uniqueness, agreement | 2 | model_conjecture | IMP | 3 |
| `contentParent`, `DescEq`, `<_c` | 2 | model_conjecture | DEF | 2, 4 |
| acyclicity of `contentParent` | 2 | — | DER | 2, 3 |
| `sameContent_ℓ` | 2 | source (CR-1.0 ≡_ℓ) | DEF; equivalence axioms IMP on the profile | 1 |
| `ES`, `≼`, `#`, `AltSets`, heredity, finite causes, causal grounding | 3 | model_conjecture (Winskel-style) | IMP | 1 |
| `Config`, `Versions(r)`, `R₀` | 3 | model_conjecture | DEF | 3 |
| `Template`, `templ`, occurrence | 1, 5 | model_conjecture | DEF | 2 |
| `Perturbation`, `γ₀` | 1, 17 | model_conjecture | DEF | — |
| `KernelVersion`, `ProfileVersion`, `Digest`, `Judgment` | 1, 7.7 | model_conjecture | DEF | 7 |
| `refs`, `payloadRefs` | 3, 4 | model_conjecture | DEF | 4 |
| `Attend`, `ω` | 4 | source (CR-1.0 OM-1) for the move; model_conjecture for the witness | DEF | 1, 8 |
| `EnterConjecture`, `Activate` | 4 | source (OM-2); `Activate` model_conjecture | DEF | 2 |
| `Criticize`, `InterpretEvidence`, `CompareRivals`, `Respond`, `Retain`, `RepertoireExpand` | 4 | source (OM-3 – OM-9) | DEF | 2, 11 |
| `Admit` | 4 | model_conjecture | DEF | 7 |
| `Merge`, `AttentionShift` | 4 | user_adopted (stops are resource reallocation) | DEF | 6 |
| `Response`, `Outcome` typing, `result` | 4 | source (OM-6 – OM-8); typing model_conjecture | DEF | 2 |
| Eligibility (of templates) | 5 | source (CR-1.0 DP-4 fallibility) | DEF | 3, 11 |
| Constructor (criticism), Constructor (admission) | 5 | user_adopted (fallibility non-negotiable); form model_conjecture | IMP | 3, 7 |
| Criticism and admission outside AltSets; relative recordability | 3, 5 | user_adopted; form model_conjecture | IMP; DER for the theorem | 3 |
| Challenge schema | 5 | model_conjecture | DEF | 11 |
| Certificates are content | 5 | model_conjecture | IMP | 7 |
| Admission status-blind | 5 | model_conjecture | IMP | 7 |
| Inhabitation | 5 | model_conjecture | IMP | 8 |
| No stored status | 5 | model_conjecture | IMP | 7 |
| `Span`, `q ∩ r`, `Versions(q,r)`, `RootProblem` | 6 | model_conjecture | DEF | 3, 4 |
| `current` | 6 | model_conjecture | DEF | 2, 6 |
| `Dispositions` | 6 | model_conjecture | DEF | 4 |
| `ObservedDiversion`, `LapseCertificate` | 6 | user_adopted; form model_conjecture | DEF | 3, 7 |
| `Merge` view | 6 | model_conjecture | DEF | 4 |
| `Certificate`, `WellFormedCertificate`, `Admitted` | 7 | model_conjecture | DEF | 2, 4, 8 |
| `J_raw`, `state`, `≤_k`, `≤_t` | 7 | model_conjecture (Belnap) | DEF | 7 |
| raw monotonicity | 7 | — | DER | 3, 7 |
| `essential`, `annotations` | 7.1 | model_conjecture | DEF | 7 |
| `Attack`, `Arguments`, `Standards`, `Nodes`, `attacks`, `attacks*`, `F_r`, `G`, labels | 7.3 | model_conjecture (Dung grounded with dependency propagation) | DEF | 4, 7, 11 |
| propagation well-defined; attack acyclicity; semantics coincide | 7.3 | — | DER | 3, 7 |
| `leaves`, `usable` | 7.4 | model_conjecture | DEF | 7 |
| `Judgment`, version stamps, scope of recursion | 7.7 | model_conjecture | DEF | 7 |
| `J_adj` | 7 | model_conjecture | DEF | 7 |
| existence of `G(r)`; no unattackable argument | 7 | — | DER | 5, 7 |
| `Pos`, `Neg` derivations | 7 | model_conjecture | DEF | 7 |
| `CompleteRange` and instances | 7 | model_conjecture | DEF | 3, 7 |
| `M`, `⊨`, `sound_M` | 7 | source (CR-1.0 IR-1 – IR-4) for `⊨`; soundness model_conjecture | DEF | 1, 8 |
| profile relations (each row of §8) | 8 | `Job`, `Represents`, `Authors`, `UsesReason`, `K_E`, `Accessible`, `StableOrg`, `True`, `≡` source; the rest model_conjecture | DEF | 1 |
| `R₀(s,β)`, `Deployable₀`, `Available`, `AccessibleBefore`, `R_before`, `NewBefore`, `NewHistory` | 9 | source (DF-3, TH-17); repaired form model_conjecture | DEF | 3, 8 |
| `ExplanationObject`, `Realizes`, `WellFormed`, `Nondegenerate`, `Anchored` | 10 | model_conjecture | DEF | 2, 8 |
| `Attempted_CR1` | 10 | source (DF-2, Purports) | DEF | 8 |
| `ExpCandidate` | 10 | model_conjecture (NON-CONSERVATIVE; migration gate D10) | DEF | 10 |
| `Criticism`, `WellFormedCriticism`, `StructuredCriticism`, `MeritCoverage` | 11 | source (DF-5); `merits`, `coverage` model_conjecture | DEF | 8 |
| `ReasonUseBody`, `ValidReasonUse` | 11 | source (SC-3, DF-6); body model_conjecture | DEF | 4, 8 |
| `OriginBody`, `ValidOrigin` | 12 | source (SC-4, DP-3, BR-6); body model_conjecture | DEF | 7, 8 |
| `OCAWitness`, `ValidOCAWitness_weak`, `OCA_weak` | 13 | source (DF-4); witness form model_conjecture | DEF | 4, 9, 10, 12 |
| `ValidOCAWitness_strong`, `OCA_strong` | 13 | model_conjecture (NON-CONSERVATIVE) | DEF | 10, 13 |
| `ProvPath`, `CCPWitness`, `ValidCCPWitness`, `CCPResult`, `CCP`, `SelfCritical`, `AnySelfCritical` | 14 | source (DF-7a, DF-7, SC-8, SC-2 for representation of the criticism); witness form model_conjecture | DEF | 2, 11, 13 |
| three claims at a later cut | 15 | model_conjecture | DEF | 7, 16 |
| `K_E` | 16 | source (MS-8, RC-1) | DEF | 8 |
| `Comparisons`, `Preferred`, `Defeated`, `GoodNow` | 16 | source (OM-5, DF-9); set-valued preference and grounded defeat model_conjecture | DEF | 4, 7, 18 |
| `CorrectionBody`, `ValidCorrection` | 16 | model_conjecture | DEF | 8, 11 |
| `Envelope`, `ImprovementBody`, `ValidImprovement` | 16 | model_conjecture | DEF | 16 |
| `EKC` | 16 | source (DF-10) | DEF | 14, 16 |
| `K_CT` declaration | 16 | source (CT-7) | DEF, deferred | 20 |
| `Chi`, `Applicable`, `Perturb`, `γ₀`, `OCap`, `Cap_CR`, `GCD`, `OpenProcess`, `Supports` | 17 | source (DF-4a, DF-11, DF-12, BR-8); non-vacuity, applicability, and `OpenProcess` model_conjecture | DEF | 13, 14, 8 |
| `FreeVariant`, `HTV` | 18 | source (DF-8, DP-6) | DEF | 8 |
| `ReachBody`, `Obligations_D`, `ValidReach`, `XReach`, `WideReach` | 18 | source (DF-14); body model_conjecture | DEF | 10 |
| contrast classes | 19 | source (DF-15 – DF-21) | DEF, outline | 8 |
| `Realization` structure and obligations | 20 | source (BR-1 – BR-8, CT-1 – CT-7); indexed form model_conjecture | DEF, deferred | 3, 13, 17 |
| §21 theorems | 21 | — | DER | as listed |
| §22 countermodels | 22 | source (TH-1 – TH-17 shapes) | DER obligations | as listed |

## 28. Audit finding → repair (Revision D audit)

| Finding | Repair |
|---|---|
| RD-A: a criticism is required to be created twice | §5: templates distinguished from occurrences; the constructor produces a fresh occurrence of an eligible template |
| RD-B: global conflict-freedom contradicts heredity | §3, §5: criticism and admission events are excluded from alternative sets; recordability is proved *relative to the configuration*; heredity untouched |
| RD-C: dependency loss asserted in prose, absent from the rules | §7.1 `essential`; §7.3 `attacks*` propagates along essential edges before `G`; well-definedness theorem; fixture `r2` now follows from the rules |
| RD-D: completeness guard not an operative premise | §7.4 `leaves` include guards; `usable` requires every leaf in `G` |
| RD-E: no admission construction; no noninterference | §5 admission Constructor; `ScopeCompatible` a function of `refs` and declared scope; `Excluded` as an attackable claim; §21 theorem |
| RD-F: public OCA ignores the query | §13 equality binding; same in `GoodNow` (§16.2), `OCap` (§17), `XReach` (§18) |
| RD-G: initial content vanishes from the baseline; `Available` lacks `s` | §9 initial branch with `Deployable₀`; `Available(s, …)`; `R₀(s,β) ⊆ R₀` |
| RD-H: rule-level revisability vs recursive evaluation | §7.3 standards as dependency nodes; §7.7 judgments with version stamps; scope of recursion declared |
| RD-I: cycles and ancestry not separated; `Respond` inputs omit the criticism | §4 `Respond` inputs include `crit(σ)`; §3 `payloadRefs` policy; §7.3 acyclicity theorem; cycle fixture withdrawn |
| RD-J: external criticism not represented by the responder; `SelfCritical` unindexed | §14 `Represents(ow.s, c, e_r)`; `CCPWitness`; `SelfCritical(cw)`, `AnySelfCritical` |
| RD-K: witness fields still overclaimed; `openProblems` unused | §7.1 essential / annotation / sub-claim classification; §11, §12, §16.3 bodies classified; `openProblems` an annotation |
| RD-L: success constructors underbound; `RejectionBetter` mistyped; `rejectCriticism` uncovered | §16.4 response-indexed envelope; per-constructor preference conditions; `rejectCriticism` declared unsupported with a falsification point |
| RD-M: `Cap_CR` vacuous over `Γ`; no new continuation; `ow.s` unbound | §17 `γ₀ ∈ Γ`, `Applicable`, total `Perturb`, `e_c, e_r ∈ r' \ r_γ`, `ow.s = s` |
| RD-N: reach unbound; empty obligations | §18 binding and `discharged = Obligations_D(p′, b′) ≠ ∅` |
| RD-O: contrast classes define non-creativity in | §19 neutral classes; negative properties in countermodels |
| RD-P: signature not closed (`Available`, `ObservedDiversion`, `Recognises`, `Matters`, `operation`, `Merge`, payload references) | §1, §3, §4, §6.4, §6.5, §8 |
| RD-Q: mutation suite overstates; OCap witness inadmissible; core gate imports success | §23 rows corrected and the origin-precedes-criticism check recorded as a lemma; §22 OCap row; §24 split into core and success cuts; §25 gates |
| RD-R: grounded semantics as profile choice | §7.3: acyclicity makes the choice moot for the slice; the remaining choices (targets, essential edges) are stated in schemas |
| Audit's self-corrections (no-fixpoint; formal work not to be postponed) | §7.2 retained as stated; §25 verification shape permits fragment implementation now |

## 29. Change register

Each entry `origin: model_conjecture` unless marked; status **proposed**; adoption per entry is a human act.

| # | Change | Reason | Reverts if |
|---|---|---|---|
| 1 | Criticism templates distinguished from occurrences; constructor over templates | the occurrence form demanded a second creator | a genuine case needs the same occurrence recorded twice |
| 2 | Criticism and admission outside alternative sets; recordability relative to the configuration | global conflict-freedom contradicts heredity; relative recordability is what fallibility needs (`user_adopted`: non-negotiable) | a defensible history needs a criticism inside an alternative set |
| 3 | Admission constructor; noninterference for scope; `Excluded` as a claim | eligibility alone produced no admission event; scope could hide status | — |
| 4 | Essential-dependency propagation of attacks before `G` | the fixture's intended result was not derivable | a defeated annotation should defeat, or a defeated essential premise should not |
| 5 | Completeness guards as derivation leaves | a defeated guard left the universal usable | — |
| 6 | Acyclicity theorem; semantics choice withdrawn for the slice; cycle fixture withdrawn | attack occurrences target the past; `Respond` now grounds the criticism | a legitimate history yields a cycle |
| 7 | Standards as dependency nodes; judgments version-stamped; scope of recursion declared | criticism of a standard had no effect; re-evaluation could masquerade as the old judgment | a case needs in-judgment evaluator replacement |
| 8 | Public classifiers bound to their witnesses (`OCA`, `GoodNow`, `OCap`, `XReach`) | one witness answered every query | — |
| 9 | Initial deployability branch; `Available(s, …)`; `R₀(s, β) ⊆ R₀` | initial content vanished from the baseline | — |
| 10 | `Represents(ow.s, c, e_r)` in the CCP witness; `CCPWitness`; indexed `SelfCritical` | CR-1.0 requires the responder to carry the criticism; the flag was not unique | a source reading lets uptake proceed without representation |
| 11 | Response-indexed improvement envelope; per-constructor preference; `rejectCriticism` declared unsupported | constructors could pair with unrelated responses | a knowledge-creating rejection of a criticism has no retention to attach to |
| 12 | Capacity: `γ₀ ∈ Γ`, applicability, total `Perturb`, new critical continuation, `ow.s = s` | vacuity over perturbations and reuse of base events | — |
| 13 | Reach bound and obligation coverage nonempty | one body witnessed every query; empty obligations passed | — |
| 14 | Contrast classes made neutral | non-entailments had become definitional | — |
| 15 | Body fields classified as essential, annotation, or sub-claim | mandatory-but-inert fields | — |
| 16 | Fixture: singleton admissions, alternative branch, `refs` per event, core/success split, version stamps | consistency witness required; core gate imported success machinery | — |
| 17 | Mutation rows corrected; origin-precedes-criticism recorded as a lemma | the row could not produce its stated flip | — |

## 30. Source map

| Topic | Location |
|---|---|
| Explanation is not prediction; definition difficult | *The Fabric of Reality*, supplied PDF pp. 14–25 |
| Problem-led conjecture, criticism, replacement, new problems; backtracking | *Fabric*, pp. 74–83 |
| Knowledge cannot appear authorless; physical criterion open | *Fabric*, pp. 327–329 |
| Conjecture not derived from observation; hard-to-vary; testability necessary not sufficient; reach | *The Beginning of Infinity*, pp. 15–20, 30–40 |
| Behaviour does not settle origin; reconstruction of meaning; creativity's mechanism unknown | *Beginning*, pp. 166–168, 413–427 |
| Constructor as retained capacity; task as transformation | CR-1.0 constructor dossier, pp. 117–141 |
| Typed model, satisfaction, theorems, non-derivability boundary | CR-1.0, pp. 215–234 |
| Application gaming | CR-1.0, pp. 278–283 |
| Grounded argumentation semantics | Dung (1995), as used in deutsch-loop; `model_conjecture` as applied here |

Fallibilism as the denial of any terminus and any immunity is source-backed through CR-1.0's fallibility postulate. Its encoding as constraints on the event space and dossier, the shared-history recursion, grounded adjudication, and the witness bodies are this document's reconstruction: `model_conjecture`.

## Final criterion

The class succeeds when every disputed attribution is answerable by a finite object at a cut — an event path, an explanation object, an origin body, a reason-use body, a correction body, an improvement body, a countermodel, or an explicit pair of raw and adjudicated evidence states — and when every such object is itself something a later criticism can attack.

It fails if any relation reappears as an unexplained label behind a cleaner type signature; if any certificate field is mandatory in the record and neither checked nor declared an annotation; if any admissible event space can lock a target against criticism relative to its own record; if any status is stored rather than recomputed; if any judgment is reported without its version stamp; or if any classification requires the system to say why it stopped.
