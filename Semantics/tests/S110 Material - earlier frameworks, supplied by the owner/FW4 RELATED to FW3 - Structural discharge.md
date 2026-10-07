# FW4 RELATED to FW3 - Structural discharge

## Where this belongs

**Role:** standalone related framework. **Predecessors and inputs:** [FW3](../FW3%20AMEND%20of%20FW2%20-%20Introducing%20why-dependence/FW3%20AMEND%20of%20FW2%20via%20D1-D3%20-%20Why-dependence.md), [Q2](../FW3%20AMEND%20of%20FW2%20-%20Introducing%20why-dependence/Q2%20AUDIT%20of%20FW3%20-%20The%20closure%20gap.md).

Retains Because as a primitive while adding explicit supports, organizations, transport, and a domain-model discharge quadruple with anti-smuggling conditions. It is standalone rather than a patch requiring FW2 to be read alongside it.

RELATED is deliberate: the conceptual connection is visible, but the archive does not authenticate a direct FW3/Q2-to-FW4 production history.

**Where it leads:** [FW5](../FW5%20JUMP%20from%20FW2%2BFW3%2BFW4%20-%20Explanatory%20construction/FW5%20JUMP%20from%20FW2%2BFW3%2BFW4%20-%20Explanatory%20construction.md).

**Basis for this placement:** Purpose and Part IX; compare Q2 structural proposals; FW5 source S6.

[Naming key and family tree](../layout.md). The navigation above is editorial. The manuscript below is a renamed reading edition, not a new scientific revision. Original hashes, case identifiers, mathematical symbols, quoted locators, and execution commands retain their historical meaning. Hashes bind the unchanged originals, not this reading copy.

---

## A semantic theory of why-dependence, work, adequacy, and knowledge

### Purpose

This theory says what it is for a content to explain a feature of a problem, what it is for a commitment within that content to do explanatory work, what it is for the resulting content to be knowledge, and what it takes to account for a claim that any of these relations holds. It has one explanatory primitive, why-dependence, bounded by seven prohibitions and an open list of modes. Everything above the primitive is definition, index, projection, or exclusion; everything below it is a domain-specific dependence relation with its own formal semantics.

It is a semantic theory, not an execution procedure. No algorithm for deciding any of its relations is required or supplied. It is canonical for any specification that adopts it. Authority fixes meanings; it confers no immunity from criticism, and the theory applies to attempts to criticize it.

---

# Part I. Commitments

**Realism.** Whether a content explains a feature is a fact about the content and the feature, not about any judgment of it. Errors can be real when nobody has identified them; an objection can be mistaken when nobody has answered it. No authority, procedure, record, or successful history turns a fallible judgment into a guarantee.

**Fallibility without collapse.** That no explanation is certified does not make all explanations equally good or make knowledge impossible. Improvement is not final certification.

**Conjecture before criticism.** A content need not be justified before it is entertained. Criticism has something to criticize; a criticism is itself a conjecture that can be criticized.

**Generation confers no standing.** A content's being generated, by any route, does not make it available as a premise, an endorsed account, or an actual form. Standing is conferred by an appraisal in a specified respect, and the appraisal is itself content eligible for criticism. Denial of standing is not deletion: a content may be retained as a target while having no standing in any application.

**Recursion.** Anything deployed in an explanatory or adjudicative role in an inquiry is eligible to become the subject of further conjecture and criticism, and the result can revise the use of the target. No content is correct by position. No infinite chain of prior authorizations is required; at some point a rule is executed rather than consulted.

**Indexing.** Every explanatory claim displays its problem, feature, respect, scope, background, boundary, and grain. Closing existentially over an index hides what the claim depends on and is not permitted.

---

# Part II. The primitive: why-dependence

A feature `f` of a problem `p`, against background `b`, within scope `Σ`, has its character because of the content of a set of commitments `W`. Write

`Because(W, f; p, b, Σ)`.

This is not defined. It is bounded by seven prohibitions.

1. **It is not fit.** Not the observations `W` matches, the responses it produces, the predictions it yields, correlation, or symmetric counterfactual dependence.
2. **It is not a verdict or a count as warrant.** Not approval, preference, a check, a computed intersection of candidate sets, or a count that yields probability.
3. **It is not the vehicle.** Not wording, exposition, a proposed connection, a derivation, a lower-level redescription, or an occurrence.
4. **It is not enabling or presence.** Not fixing which inquiries can begin, supplying evidence or attention, causal involvement, background presence, standing, retention, self-preservation, or physical transformation.
5. **It is not the thinker.** Not inferential machinery, conscious use, deployment, recognition, or contribution.
6. **It is not a truth-surrogate or a modal-surrogate.** Not the truth of `W`'s ontology, uniqueness, necessity, non-free-variation, hard-to-vary, or sufficiency.
7. **It is not index-free.** It is at `p`, for `f`, in a respect, within `Σ`; it is not reach or a free consequence.

**Properties.** `Because` is asymmetric per feature and respect: `f` is as it is because of `W`, not the converse, and the direction is fixed by an organization, not by the relation among quantities. It is recognition-independent, wording-independent (preserved by content-preserving recoding, not by content-changing substitution), and ontology-tolerant: a commitment can carry a why-dependence in scope while stated in a false or idealized ontology.

**Modes.** `Because` may hold in any mode: production, determination, invariant, constitutive, selection, or another. The list is open because mode is posterior to work: a mode is appropriate for a feature iff commitments stated in it stand in `Because` to that feature. No prior criterion of appropriateness is needed. "Mood" is not an appropriate mode for the seasons because commitments in it reach nothing and constrain nothing, not because a rule excluded it in advance.

**Status.** Declaring a primitive is not emptiness. The prohibitions decide cases: explanatory asymmetry, overdetermination, dependence without role. And Part IX says what it takes to account for a `Because`-claim, which relocates the primitive, per claim, into a mode's dependence relation plus two refutable claims.

---

# Part III. Work

Let `e` be an interpreted content with commitments `Γ` and proposed connections `Δ`, and let `f` be the relevant feature of `p` in the stated respect. Contents are individuated by interpretation at a grain `ℓ`, in a context, relative to an attributed system; an occurrence is not a content.

## III.1 Supports and contribution

The **support family** is `Sup_f = {W ⊆ Γ : Because(W, f; p, b, Σ)}`. It is assumed upward closed within coherent sets: adding a commitment that does not interfere with a support leaves a support.

- **Work.** `Work(d, f)` iff `∃W ∈ Sup_f [d ∈ W ∧ W∖{d} ∉ Sup_f]`. A commitment does work iff it is critical for some support. Work is contributory, not necessary.
- **Indispensable.** `Indisp(d, f)` iff `Γ ∈ Sup_f ∧ Γ∖{d} ∉ Sup_f`.
- **Padding.** `Pad(d, f)` iff `¬Work(d, f)`.
- **Support-relative constraint.** `Constr_W(d, f)` iff `W ∈ Sup_f ∧ d ∈ W ∧ W∖{d} ∉ Sup_f`. A detail is constrained relative to a route.
- **Hard to vary.** `HTV(e, f)` iff every content-bearing commitment of `e` is indispensable for `f`.

**Lemma (finite case).** If `Γ` is finite and `Sup_f` is upward closed with `Γ ∈ Sup_f`, then `Work(·, f)` is the union of the minimal supports and `Indisp(·, f)` is their intersection. *Proof.* A member of a minimal support is critical for it. A commitment critical for a support `W` belongs to every minimal support inside `W`, since otherwise `W∖{d}` would contain one and be a support. `Γ∖{d}` is a support iff some minimal support omits `d`. ∎

**Consequences.** Two independently sufficient routes `Sup_f = {{a},{b}}`: both do work, neither is indispensable, the account is not hard to vary, and removing either leaves the set of features reached unchanged. Contribution and indispensability are different relations and are displayed separately. A minimal set whose removal destroys every route intersects every support and is not in general a support; padding can belong to one; membership in such a set never establishes contribution.

**Joint work without contributors.** Minimal supports need not exist. If `Γ = {d_1, d_2, …}` and `W ∈ Sup_f` iff `W` is unbounded, then removing any member of any support leaves a support, so `Work(·, f)` is empty while `Γ ∈ Sup_f`. The family `{|x| < 1/n : n ∈ ℕ}` forces `x = 0` though no single bound does. Contribution is therefore **grain-indexed**: at the fine grain no `d_i` contributes; at the grain where the family is one universally quantified commitment, that commitment is critical.

## III.2 Organizations and recoding

Supports are defined over the organization `⟨Γ, Δ⟩`, not over a bag of sentences. A recoding is a map between representations that commutes with the connection structure and preserves the feature map. Supports are defined up to such maps at fixed grain and are mapped across grains by coarsening (bundling `a, b` into `a ∧ b` sends the support `{a, b}` to `{a ∧ b}`). Work is preserved across recodings; it is not preserved across substitutions that change the organization. That substantive changes are not protected does not mean every substantive alternative loses all work: rival accounts and redundant routes are admitted.

## III.3 Reach

`Reach(e, p′; b′, Σ′)` iff some support of `e` for a feature of `p`, with commitments unchanged and background extended to `b′`, is a support for a feature of `p′` within `Σ′`. Reach can exist before any agent recognizes it and is not restricted to enumerated applications. An application claim must state the unchanged commitments, the added background, and the explanation of relevance; a bridge theory is an additional contribution, not a free consequence. Reach of an explanation is distinct from the reach of a thinker's inferential machinery.

**Monotonicity lemma.** Fix the content organization, its interpretation, and a variation family `V`. For each feature `f` let `A_f ⊆ V` be the variations preserving the organization's work for `f`, and for a family `F` of features let `A(F) = ⋂_{f∈F} A_f`. Then `F ⊆ F′ ⟹ A(F′) ⊆ A(F)`. *Proof.* A variation preserving every requirement in `F′` preserves those in `F`. ∎ Adding a preservation requirement cannot enlarge the permitted variation set; it need not shrink it strictly; changing the organization, background, or family defeats the comparison; counting reached features does not restore the missing premises. This is the sound direction of "reaches more, harder to vary." No comparative claim across different contents follows.

## III.4 The diagnostic

`FreeVariation_V(e, D; p, b)` for `D ⊆ Γ` holds when a change to `D` within family `V` preserves the claimed account without a new reason or compensating explanatory change. The family must contain informative contrasts and must range over subsets; an empty, renaming-only, or objection-excluding family establishes nothing; singleton variation calls each overdetermining commitment free. The diagnostic is comparative, respect-relative, and fallible. It is evidence about work; it is not work.

## III.5 Transport

Let `π : Z → X` map the target's states in scope to the representation's states, with operations `S_i` on `Z` and `T_i` on `X` such that `π(S_i z) = T_i(π z)` within scope, and let `F(z) = F̂(π z)`. Then every finite composition commutes and `F` is preserved. Three cases: **recoding**, `π` invertible; **idealization**, `π` many-to-one, preserving specified distinctions; **approximation**, exact equality replaced by a bounded discrepancy `|F − F̂∘π| ≤ ε` on the scope, with the assumptions under which the bound holds. Work survives a theory change iff a support's organization is carried by such a map. Work is the unit of transport: what a change of theory preserves, revises, or abandons.

## III.6 Type and token

`Sup_f` is defined over the organization and is type-level. Which route was active in a particular occurrence is token-level and is not recoverable from endpoint variation: two parallel routes that can each activate an output, and a priority arrangement in which the first route blocks the second while active, have identical input-output tables and differ in whether the second route is active when both inputs are on. A token-level account needs internal access or further interventions.

## III.7 Interference

Upward closure is assumed within coherent sets. Where a commitment defeats a support when added, the family is not monotone and the finite lemma does not apply. In structural models, interference is represented in the organization, not in the commitment set, which restores monotonicity at the commitment level. The general non-monotone case is open.

---

# Part IV. Adequacy

`Account(e, p, b; Σ)` holds iff:

- (A1) `Γ ∈ Sup_f` for the relevant feature `f` of `p` against `b` within `Σ`;
- (A2) the indices `p`, `b`, `Σ` are the ones stated, and `b` includes every standard, interpretation, observation model, or comparison essential to `e`;
- (A3) the work is distinguishable from associating an input with an output, which A1 guarantees by prohibition 1.

`Account` is a fact, independent of every judgment and vehicle. It is non-comparative: two independently reasoned explanations can both be in `Account` for one problem. It is recognition-independent and attempt-independent: it can hold for a problem nobody has posed and fail for one someone has deployed an account of. It is independent of standing and of progress in both directions. When `p` is ill-posed and has no relevant feature, `Account` fails rather than lapsing, and the available progress consists in exposing `p`.

**Factivity.** `Account` is factive over work and not over commitments. Three cases: (i) false surrounding ontology with a correctly represented scoped relation: work preserved, and the transport map may discard the ontology; (ii) approximate model for an explicitly approximate feature: work preserved with a bounded discrepancy, and the feature is re-indexed to the tolerance; (iii) a commitment false in the very respect alleged to do the work: no work, and A1 fails. Supersession is non-retroactive: a later theory that accounts for more, and for why the earlier one worked, does not make the earlier one not to have accounted within its scope.

**Circularity.** A commitment selected by the conclusion it serves has content; its grounds are defective. Adequacy is about content; grounds are a matter of discharge (Part IX). A circular attempt can be in `Account` if its commitments happen to be true; it can never be discharged, and it does not withstand the criticism, so it lacks merit.

**The interpreter's obligation.** That an admissible interpretation must identify the work done by the commitments is a condition at the attribution standpoint. It is not a condition on the relation; read that way, it would make adequacy depend on someone's having identified the work.

---

# Part V. Instances of adequacy with other explananda

Three further relations have the form of `Account` with a different explanandum. They are stated as conjectures, because adopting them leaves the theory with one explanatory primitive.

**Bearing.** `Bearing(g, δ, z, p, b)` iff `Account(⟨g, λ⟩, p_δ, b; Σ)`, where `p_δ` is the problem "why does target `z` have defect `δ`, relevantly to `p`?" A criticism is a conjecture about a defect; its bearing is the why-dependence of the defect on the grounds. Prediction-error repair, consensus by suppression, and blocking by an attested competitor fail `Bearing` for the same reason they fail `Account`: nothing in them stands in `Because` to a defect.

**Contribution.** `Contributes_β(s, x, h, e)` iff there is an account `a` with `Account(a, p_x, b; Σ)`, where `p_x` is "why does `x` have the problem-specific organization it has?", and `a` attributes that organization to the activity of `s` at boundary `β`. Mere causal involvement is prohibition 4.

**Progress.** `Progress(ξ, ξ′; Δ)` iff `ξ′` contains, attributably to `Δ`, an instance of `Account` or `Bearing` absent from `ξ`, or a reformulation of the live problems under a valid transport that preserves the difficulty and admits such an instance, with losses exposed and changed standards displayed. Replacing a false mechanism, explaining why an approximation worked, finding that a conflict was an artifact of interpretation, finding a better question, and recognizing a limit are each a gain of this form. No common scale is imposed.

**The single-primitive conjecture.** If all three hold, adequacy, bearing, progress, and authorship are why-dependence with stated relata. Capacity is modal and is not an instance; operative role (Part VII) is a record fact and is not an instance.

---

# Part VI. Merit and created knowledge

**Merit.** `Merit(e; ξ, Σ)` iff `Account(e, p_ξ, b_ξ; Σ)` and `e` withstands the criticism applicable in situation `ξ` sufficiently well to merit preference among the actual alternatives within `Σ`. Merit is comparative and situation-indexed: it changes when an alternative is invented, with no change in `e` or in the world. `Account` is one conjunct of it and does not change.

**Created knowledge.** `Created_β(x; ξ, ξ′, h, e)` iff there is a connected creative critical contribution `Δ` containing `x`, `Progress(ξ, ξ′; Δ)`, the attribution of `Δ` to the system at `β` is accounted for, and `x` is deployable in an explanatory role by the attributed system or identified community after `e`. Availability is deployability, not standing, not endorsement, and not perpetual: loss does not make creation not to have occurred.

**Three relations, one word.** "Knowledge" names adequacy, merit, or created knowledge, and the three come apart: "not comparative" holds of adequacy only; "can be lost" of created knowledge only; "can be false" of created knowledge and merit, and of adequacy only in the sense that its commitments need not be true. A specification states which relation each use of the word projects.

**Physical knowledge.** Information with a causal capacity to preserve its own instantiation is a one-place predicate on information. Explanatory knowledge is a relation with a problem argument. The two differ in logical type and are extensionally independent: a false belief spread by imitation preserves its instantiation and accounts for nothing; an explanation that accounted for its feature and was lost preserved nothing.

---

# Part VII. Standing, custody, deployability, operative role

**Standing.** `Standing_j(d; u)`: `d` is treated as an available premise for application `u` in appraisal `j`. Conferred by an appraisal act; indexed by use and respect; deontic, not epistemic. An appraisal act needs no prior standing to confer standing. Standing is never derived from `Account`, `Merit`, `Created`, or a record state, and none of those from standing. Preference, including preference licensed by a count of independent features reached, licenses standing in the next appraisal and nothing else.

**Custody.** `Custody(s, o, h, e)`: system `s` holds occurrence `o`. Transmission moves custody. Custody of an occurrence is not deployability of its content; storage of a string is not understanding.

**Deployability.** `Deployable(s, x, e)`: `s` can deploy `x` in a relevant explanatory role at `e`. This is the system's repertoire. Not all logical consequences of an accepted theory are in it; what could be acquired after further learning is not in it.

**Operative role.** `Deployed(d, κ, r)`: content `d` occupies role `r` (premise, standard, interpretation, comparison, method) in instance `κ` of inquiry. This is a record fact. Target closure ranges over `Deployed`, not over what the instance's outcome depends on. Write `DependsOn(κ, d)` for the latter; it is not a record fact and it is not what "operative" means.

**Generator constraints.** A standard, method, or practice whose withdrawal would change what the system can conjecture is a generator constraint. It satisfies `DependsOn` for the instances it shapes and is deployed in none of them. It escapes target closure unless converted into a content that can be copied, compared, and withdrawn, with return relevance to its standing. Executed rules and the boundary of an instance escape in the same way.

---

# Part VIII. Structural results

**R1.** No explanatory relation has a knower argument. `Because`, `Work`, `Account`, `Merit`, and `Created` have a problem or situation as an argument and no believer, endorser, or judge. The knower enters through attribution only.

**R2.** No explanatory relation collapses to a one-place predicate on contents. Explanatory knowledge is not a sortal; physical knowledge is.

**R3.** Acquisition is creation. Deployable explanatory understanding is reconstruction, reconstruction is authorship, and reconstructed content is new relative to the acquirer's own baseline. Transmission moves custody; it never moves knowledge.

**R4.** Knowledge and standing are orthogonal. A system may withdraw standing from `x` everywhere by mistaken appraisal and adopt a worse `x′`; `x` remains created knowledge and `x′` is not.

**R5.** Explanatory and physical knowledge are extensionally independent.

**R6.** `Account` is independent of attempt, progress, and standing in both directions.

**R7.** `Account` is non-comparative; merit is comparative. A "best current explanation" record is a merit record and changes with no change in the explanation.

**R8.** `Account` is factive over work, not over commitments; supersession is non-retroactive.

**R9.** `Because` is asymmetric per feature and respect, with direction fixed by a production structure. The flagpole's height and the sun's elevation account for the shadow's length; the shadow's length and the elevation entail the height but do not account for it, since nothing in them says why the flagpole has its height.

**R10.** Work is critical membership. Two independently sufficient routes both do work; neither is indispensable; the account is not hard to vary.

**R11.** The `Essential` bridge is conditional. `Essential(d, u)` is route-relative indispensability for an inferential application; `Essential(d, u) ∧ W_u ∈ Sup_f ⟹ Work(d, f)` where `W_u` is the route's support, and conversely `Work(d, f) ⟹ ∃u [W_u ∈ Sup_f ∧ Essential(d, u)]`. Without the restriction the bridge fails, as the flagpole inference shows. Shared membership in every support, not uniqueness of a support, is the indispensability condition.

**R12.** Reach and hardness are related by the monotonicity lemma and by nothing stronger.

**R13.** Mode is posterior to work.

**R14.** Target closure is closed over roles, not dependencies. Everything an instance depends on but does not deploy escapes closure; an organization that can convert its generator constraints into deployable contents with return relevance is one that can extend itself.

**R15.** Operative role is a record fact; work is not. A host can maintain the target-closure set and cannot maintain the working set.

**R16.** The licensed count. A count of conjecturally independent features reached orders accounts for preference and for nothing else. No other count has an effect.

**R17.** Warrant is eliminated. No relation tracks truth by degree. What survive are adequacy (fact), merit (comparative fact), standing (conferred), and preference (an attitude). Why to act on the preferred explanation is not a warrant question; any answer is itself an explanation subject to criticism.

**R18.** Occurrence-level questions are ill-formed until an interpretation is fixed, and fixing it is a conjecture.

**R19.** Roles do not sort knowledge. A problem, criticism, standard, method, or limitation is knowledge relative to the situation it improved.

**R20.** In finite monotone support families, critical membership coincides with membership in some minimal support, and indispensability with membership in every minimal support.

**R21.** `Account` can hold with `Work(·, f)` empty; contribution is grain-indexed.

**R22.** A discharge (Part IX) violates none of the seven prohibitions and can fail independently in each of its three claims.

**R23.** Within a discharge, `Because` is decomposed into a mode's dependence relation plus two refutable claims; the mode list is open and the entailment is one-way.

**R24.** Non-circularity is a condition on discharge, not on adequacy.

**R25.** `Account` is type-level; the active route in an occurrence is a further claim.

---

# Part IX. Discharging a why-claim

A `Because`-claim may be true without being accounted for. Calling a substantive relation true is not a substitute for explaining why it holds. A **discharge** is that explanation.

## IX.1 Domain models

A domain model for scope `Σ` is `D = ⟨Z, Ops, Org, π⟩`: a state space `Z` for the target in scope; a family `Ops` of admitted operations or variations; an organization `Org` that fixes the mode's dependence relation `Dep_D` (a production order, a preserved quantity, a constitutive rule set, a selection relation); and an interpretation map `π` from the target's states to the representation in which the explanation is stated. `Org` is one of the mode structures of Part X, each with its own semantics; it is not an arrow labeled "explains."

## IX.2 The discharge quadruple

A discharge of `Because(W, f; p, b, Σ)` is `⟨D, S, A, R⟩`:

- **S, the structural claim.** A theorem in `D`: under `Org` and `Ops`, the represented feature `F̂` is determined, constrained, or excluded by the `π`-image of `W`, with direction fixed by `Org`, and with the variations under which `W`'s organization is preserved and those under which it is not both displayed. `S` is provable or refutable as mathematics about `D`, independently of whether the target instantiates `D`.
- **A, the application claim.** The target instantiates `D` within `Σ`: its states are in `Z`, its admitted changes are `Ops`, its organization is `Org`. `A` is a conjecture about the target with refutation conditions of its own.
- **R, the relevance claim.** The feature posed in `p` is `F̂ ∘ π` at the stated respect and tolerance: not a different explanandum reached by sliding from exact to approximate, from production to inference, from effect to value, or from the feature to its representation.

The discharge accounts for the claim: `W` does work for `f` because, under an organization the target has, varying `W`'s organization within the admitted operations changes `F̂`, while the direction is fixed by the organization and not by the desired conclusion. Each of `S`, `A`, `R` is eligible for criticism, with return relevance to the use of the discharged claim.

## IX.3 Anti-smuggling conditions

A quadruple is a discharge only if:

- **N1.** The truth of `S` does not depend on the target. An `S` that says "`W` really explains `F̂`" is the primitive under another name.
- **N2.** `A` has at least one refutation condition that does not mention `f` or the desired conclusion. A calibration that never mentions the mass can refute an additive-response claim; "`b_B = 0`, because that gives `x = 12`" has no such condition and is not an application claim.
- **N3.** `R` is checked against `p` as posed, not against the conclusion.
- **N4.** `Org` belongs to a mode module with a stated semantics for `Dep_D`, so that "determined by," "preserved under," "counts as," or "selected by" has content independent of the case.

Under N1 to N4 the case-specific content enters only through `A` and `R`, and both are refutable without appeal to `f`.

## IX.4 Soundness, non-triviality, relocation

**Soundness.** A discharge violates no prohibition: `S` is a theorem, not fit or a verdict; the discharge is invariant under organization-preserving recoding, so it is not the vehicle; `W` participates in `Org`, so it is not mere presence; `S` holds whoever proves it; `π` may discard false ontology, and `Dep_D` is neither necessity nor sufficiency by construction; the indices are fixed in `A` and `R`.

**Non-triviality.** A discharge can fail in three independent ways: `S` false (rank 3, not 2); `A` false (the offsets are not additive); `R` false (the question was the exact value, the model delivers a tolerance). Each failure is independent of the `Because`-label, so a discharge is not the label relabeled.

**Relocation.** Within a discharge, `Because(W, f) ⟸ ∃D applicable [Dep_D(π(W), F̂)]`. The right-hand side is a disjunction over mode modules, each with a formal `Dep_D`; the list is open and the arrow is one-way. The residual "why" no longer sits in an undifferentiated label. It sits in `Dep_D`, formally characterized, in `A`, a conjecture about the target, and in `R`, an indexing claim.

**What a discharge is not.** Not a definition of `Because`, not a necessary condition for `Account`, not an admission test. An undischarged claim may be true; it is unaccounted. A machine may check `S`, record `A` and `R`, and never assert that the world satisfies them.

---

# Part X. Mode modules

Each module states `Org`, `Dep_D`, the form of `S`, the form of `A`, the typical failure of `R`, and a case. The list is open.

**M1. Production (structural models).** `Org`: variables with an assignment order; exogenous variables set upstream; endogenous variables assigned from their parents; admitted interventions set a variable and cut its assignment. `Dep_D(W, F̂)`: `F̂`'s variable is endogenous, `W`'s variables are among its transitive parents or fix its assignment, some intervention on `W`'s variables changes `F̂`, and interventions on `F̂`'s variable leave `W`'s assignments unchanged. `S`: the dependence and its direction, as a property of the equations. `A`: the target has this assignment structure in scope. `R` fails by sliding from production to inference, or from type to token. *Flagpole.* `H := U_H`, `θ := U_θ`, `L := H·cot θ`. `Dep_D({H, θ, geometry}, L)` holds; `Dep_D({L, θ}, H)` fails, since `H`'s assignment has no `L` among its parents and intervening on `L` leaves `H := U_H`. A pole built to cast a specified shadow is a different organization and a different question.

**M2. Determination and limitation (linear identifiability).** `Org`: a measurement map `y = Az` and a feature functional `q(z) = cᵀz`; `Ops`: changes of `z` within the measurement fibre. `Dep_D(W, F̂)`: the measurements determine `q` iff `ker A ⊆ ker cᵀ`, equivalently `cᵀ` lies in the row space of `A`; the null directions with `cᵀv ≠ 0` are why they do not. `S`: the criterion, as linear algebra. `A`: the instruments have additive response with constant offsets in scope. `R` fails by taking the feature to be "the mass is 12" when the account's feature is "the mass is undetermined by these readings, and the offset difference is 2." *Balances.* Readings 10 and 12; `A = [[1,1,0],[1,0,1]]`; null direction `(1, −1, −1)`; `c_mass·v = 1`, undetermined; `c_diff·v = 0`, determined, value 2. Repetition leaves rank 2; an independent calibration row raises it to 3. "`b_B = 0`" chooses a representative on the fibre and fails N2.

**M3. Invariant and obstruction.** `Org`: admitted operations and a quantity `I` preserved by every one. `Dep_D(W, F̂)`: no state with feature `F̂` is reachable because `I` takes a different value on every such state; `W` specifies `Ops` and `I`. `S`: preservation and value mismatch, as mathematics. `A`: the target's admitted changes are `Ops`. `R` fails by asking for the causal history of a particular attempt when the account is of the obstruction. *Tokens.* Twenty-three indivisible tokens, three recipients, redistribution preserves the total; equal division requires `3k = 23`; no integer `k`. Cutting a token changes the admitted operations and so the problem.

**M4. Constitutive.** `Org`: a rule set with application conditions. `Dep_D(W, F̂)`: the state counts as `F̂` under the rule, given the state description. `S`: the rule application, as a derivation within the rule set. `A`: this is the operative rule in the practice, refutable by the practice's own records and corrections, not by who likes the outcome. `R` fails by sliding from "counts as a win" to "was a good move" or "was intended." *Game.* A move occupies the third marked position and, under the stated rule, completes a winning configuration. Choosing the rule so that the preferred player wins fails N2.

**M5. Selection.** `Org`: an option set, an aim, and a selection relation. `Dep_D(W, F̂)`: the action was selected because it was the option that best satisfied the aim under the agent's representation. `S`: the selection, as a property of the option set and aim. `A`: the agent had that aim and that representation. `R` fails by sliding from "why selected" to "why it succeeded" or "why it was good."

**M6. Aesthetic (open).** Not supplied. A discharge here would need a feature that is aesthetic value rather than listener response (R), an `Org` that is a standard whose application is not fixed by the response (N2), and a `Dep_D` with a semantics (N4). The domain is preserved as an obligation; the modules above do not cover it.

---

# Part XI. Discriminating cases

**1. Seasons.** Axial orientation, orbital relations, and illumination geometry form a support for the seasons' phase: asymmetric, geometric mode, holding unrecognized, surviving recoding, destroyed by substituting mood, constraining "the hemispheres are out of phase," reaching the solstice dates and the polar day. Not fit, not a count, not the wording, not necessary alone, not true in every detail (circular orbits idealized). Every prohibition and every positive clause satisfied at once.

**2. Balances.** The readings do work for the offset difference and none for the mass: same commitments, two features, work for one. Repetition adds no work for the mass. "Trust B because its reading agrees with the proposed mass" is an attempt whose auxiliary has no ground independent of the conclusion; it may be in `Account` by luck and cannot be discharged. The invariance result, that the readings determine `b_B − b_A = 2` and not `x`, is an account of a limitation and a better problem.

**3. Flagpole.** Asymmetry decided by production structure; derivation runs both ways, work runs one.

**4. Two mechanisms.** One explanation offers `d` and `d′`, each sufficient for `f`. Singleton variation calls each free; subset variation finds `{d, d′}` jointly not free and each a minimal support. Both do work, neither is indispensable, and the explanation is easier to vary than one with a single mechanism.

**5. Generator constraint.** An instance's outcome depends on which conjectures could be formed; the constraint is deployed in no role within the instance. `DependsOn ∧ ¬Deployed`. Target closure does not reach it; conversion into a deployable content does.

**6. Mistaken appraisal.** The system withdraws standing from `x` everywhere and adopts `x′`, which makes the situation worse. `x` is retained without standing and is created knowledge; `x′` has standing and is not.

**7. Relay and reconstructor.** A relay emits a received explanation without reconstructing it and develops the understanding later. At the first time it has custody and not deployability; at the second it has deployability and an originative act at its own boundary.

**8. Superseded ontology.** The inverse-square dependence is a support for closed orbits within the weak-field scope; action at a distance is not in it. The successor theory's weak-field limit preserves the support and supersedes the ontology, and accounts for why the earlier account worked. The earlier account accounted for orbits in its scope and did not cease to.

**9. Spreading falsehood and lost explanation.** A false belief that spreads preserves its instantiation and accounts for nothing; an explanation that accounted and was lost preserved nothing.

**10. Mood for seasons.** The wording of an account is preserved; no support survives; the antipodal phase is unreached. "Mood" is not an appropriate mode because commitments in it do no work.

**11. Ill-posed problem.** An attempt is deployed as an account of a difficulty later shown to be an artifact of interpretation. There was no feature to do work on; A1 fails. The available progress is a bearing instance (the criticism of the problem) and a reformulation under transport.

**12. Priority wiring.** Parallel and priority arrangements agree on every endpoint assignment and differ in which route is active when both inputs are on. An account of a particular firing needs internal access; endpoint variation cannot supply it.

**13. Joint work.** An infinite family of bounds forces a value; no single bound contributes; the family, taken as one commitment at a coarser grain, does.

---

# Part XII. Specification discipline

A specification distinguishes a semantic assertion, an attribution judgment, a record fact, and a machine-check result.

**Record facts it may hold.** Custody of occurrences with provenance. Deployed roles per instance, which is the target-closure set. Standing per appraisal act, per use and respect. Record states (no case, positive, negative, both) as descriptions of the record. Expositions `⟨W, Γ, Δ, Σ, B_E⟩` as the proposer states them, with scope and essential standards recorded. Dependencies `Essential(d, u)` per application. Variation results over declared subsets with the family's informativeness argued. Independence conjectures behind any count of features reached. Transport accounts: which supports are claimed to survive, be revised, or be superseded. Structural claims `S`, checked as mathematics. Application and relevance claims `A`, `R`, recorded with their refutation conditions. Claims alleging `Account`, `Work`, `Bearing`, `Progress`, `Merit`, or `Contributes`, each without standing until appraised.

**Fields it may not hold.** `knowledge`, `accounts_for`, `does_work`, `warrant`, `probability_of_truth`, or any field whose truth would be a semantic assertion. Each such claim is projected through an explicit bridge whose adequacy is open to criticism.

**Rules.**
- A record state describes the record, never the content.
- No record state is promoted to standing without a named appraisal act.
- Standing is never derived from adequacy, merit, created knowledge, or a record state, and none of those from standing.
- A change in problem, background, scope, or an essential standard invalidates every claim indexed to the old values.
- "Shown to do no work" and "withdrawn as essential" are different operations with different effects on usability.
- A count of independent features reached licenses preference and nothing else.
- The target-closure set of an instance is its deployed set; the escaping dependencies at the adopted boundary are listed with their conversion status.
- An occurrence-level question is rejected until an interpretation is fixed as a conjecture.
- "Knowledge" in any projected claim names adequacy, merit, or created knowledge, and says which.
- A discharge is recorded as its quadruple; a machine may verify `S` and may not assert `A` or `R`.

---

# Part XIII. What would count against the theory

- **The primitive** would be withdrawn if a reduction of why-dependence to a displayed relation (counterfactual, probabilistic, derivational, or interventionist) were found that survives asymmetry, overdetermination, ontology-tolerance, and mode-openness.
- **Work as critical membership** would be revised if a commitment were shown to do work while critical for no support in a monotone family, or if a critical commitment were shown to be padding.
- **Grain-indexing of contribution** would be withdrawn if two grains disagreed about contribution in a way no organization-preserving map relates.
- **Factivity over work, not commitments** would be reconsidered if every apparently false working commitment were shown to preserve a true sub-commitment in the same mode.
- **The conditional `Essential` bridge** would be refuted by an explanatory route `W_u ∈ Sup_f` with `Essential(d, u)` and `¬Work(d, f)`.
- **Closure over roles** would be refuted by an organization that criticizes, with return relevance, a dependency it never deploys and never converts to a deployable content.
- **Acquisition is creation** would be refuted by deployable explanatory understanding acquired without reconstruction at the acquirer's boundary.
- **The independence results** would each be refuted by an entailment in either direction.
- **Bearing, contribution, and progress as instances of adequacy** would be refuted respectively by a criticism that bears without why-dependence of the defect on its grounds, an attribution of authorship with no account of why the content has its organization, and an improvement that is neither a gain in adequacy or bearing nor a reformulation admitting one.
- **The licensed count** would be refuted if a count of independent reach were preference-irrelevant, or if some other count licensed more than preference.
- **Mode posterior to work** would be refuted by an appropriate mode in which no commitment does work for any feature, or a feature for which commitments in an inappropriate mode do work.
- **The discharge schema** would be withdrawn if a quadruple satisfying N1 to N4 certified a claim false in the intended interpretation with `S`, `A`, `R` all true, or if some accounted `Because`-claim were shown undischargeable in principle by any quadruple of this form.
- **Relocation of circularity to discharge** would be withdrawn by a circular attempt that cannot be adequate even when its commitments are true.
- **Each mode module** would need revision if its `Dep_D` held with `S`, `A`, `R` true and no work done, or failed with work done.

Renaming an inconvenient case, changing scope silently, or declaring every negative case "not a real problem" would not answer any of these.

---

# Part XIV. Open questions

1. Is why-dependence primitive by design, or is a reduction available that meets the refutation condition above?
2. Do the mode modules cover every accounted `Because`-claim, or is there a defensible account, at a fixed feature and scope, whose organization no module can carry?
3. What is the feature, the organization, and the dependence relation in the aesthetic case?
4. Does every apparently false working commitment preserve a true sub-commitment in the same mode?
5. What are the structural claims for nonlinear or constrained measurement maps?
6. How are non-monotone (interfering) support families to be treated?
7. What does a token-level discharge require beyond internal access?
8. Which dependencies besides generator constraints, executed rules, and boundaries escape target closure at the boundaries of interest, and what converts each?
9. Do inexplicit contents satisfy the representational requirements of an organization that can criticize them, or is inexplicit inquiry always attributed at a boundary that includes explicit resources?
10. Is the count of independent features reached the only count that should license preference?

---

# Appendix: checked identities

| Check | Result |
|---|---|
| Nonconstant monotone Boolean functions on 2, 3, 4 variables | 4, 18, 166 |
| Union of minimal supports differs from intersection | 1, 11, 151 |
| Critical membership equals union of minimal supports | every case, each n |
| Intersection equals the individually deletion-sensitive set | every case, each n |
| Balances matrix `[[1,1,0],[1,0,1]]` | rank 2; null direction proportional to `(1, −1, −1)` |
| Same rows repeated three times | rank 2 |
| With calibration row `(0,1,0)` | rank 3 |
| `c_mass·v`, `c_diff·v` on the null direction | 1, 0 |
| Parallel versus priority wiring on all four input assignments | equal |
