# PC7 Resolve Semantic Freeze

Freeze date: 2026-07-25.

Status: Resolve semantics are frozen for a separately bounded PC7
implementation gate. PC7 implementation has not started and PC7 is not
accepted.

## Normative authority

`docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md` is the
accepted normative companion that closes the Resolve omissions in Lattice
Standard 0.3. It is controlling only for Resolve and the validation of an
optionally supplied existing Lockfile needed by Resolve. Lattice Standard 0.3
remains primary; the accepted Default Semantics, Canonical JSON, and Package
Scan Semantics errata remain authoritative only within their stated scopes.

This freeze records the completed independent review; it is not another
semantic review. The reviewed second-repair candidate had SHA-256
`96b791052be2231f25e2e0cf05ef7e0bd769e811a5947f31c538d205fe5c95b9`.
The final independent review had SHA-256
`3d635bda4e9aec9aaf5147e0fcd579f35cfe176f068627b9cb4169f0cbec1ee9`
and reported P0=0, P1=0, P2=0, P3=1 with
`INDEPENDENCE_COMPROMISED=false`. All five previous P1 findings were
independently recomputed closed.

The sole P3 is retained as non-blocking provenance debt. One nonnormative
rule-provenance cell in the reviewed second-repair bytes says “unaccepted
first repair.” It changes no Resolve result, fixture, identity, authority, or
acceptance outcome and is not repaired by this gate.

## Bound artifact identities

| Artifact | SHA-256 |
|---|---|
| PC7 scope reconciliation | `4cee5f0beacd663ee9ab3bb9c05060342de18c1d6d7b56d3a477c46c15d80243` |
| Reviewed second-repair candidate | `96b791052be2231f25e2e0cf05ef7e0bd769e811a5947f31c538d205fe5c95b9` |
| Final independent review | `3d635bda4e9aec9aaf5147e0fcd579f35cfe176f068627b9cb4169f0cbec1ee9` |
| Accepted Resolve Semantics Erratum | `4507fdfe2147f460c2f791b494517878c0d04620d020a6b8c512294aab868b24` |
| Specified conformance manifest | `1fb0c0588310a32c4a5c4fa7ff9d9a268ab940a61ae913d00bb465eb2a83ef10` |

The durable manifest path is
`docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json`. Its maturity is
exactly `specified`. It is not dispatchable, executable, or qualified.

## Lifecycle boundary

```text
exact opaque ScannedSource
        +
optional ExistingLockfileInput
        |
        v
PC7 Resolve
        |
        v
opaque non-authoritative ResolvedSource
        |
        v
Lock (deferred)
```

Resolve begins only after successful PC6 Package Scan and ends before Lock.

## Exact conceptual input

PC7 consumes exactly:

```text
one exact opaque ScannedSource
+
ExistingLockfileInput = Absent or one immutable supplied byte sequence
```

No other member or capability exists. Absent Lockfile input and a supplied
zero-byte sequence are distinct. Resolve derives the root source, active
profile, Blueprint digest, package candidates, descriptors, package
identities, declared module paths, and verified immutable bytes only through
the exact ScannedSource. It does not repeat PC6, read a live path, inspect a
package directory, use a network, fetch or install a package, invoke a
provider, consult a clock, use randomness, or receive a host capability.

The current candidate universe is exactly `ScannedSource.packages()`. The
three duplicate-composition vectors remain future criteria and are
non-dispatchable through the current accepted ScannedSource boundary. This
freeze creates no composition seam.

## Exact Resolve ownership

Resolve owns the accepted erratum's exhaustive import admission, canonical
constraint grammar, arbitrary-size numeric comparison, requirement
conjunction, candidate grouping, identical-record collapse, active-profile
eligibility, existing-Lockfile intake and validation, per-package reuse,
greatest-compatible fallback, requirement provenance, retraction,
reachability, deterministic fixed-point passes, selected-module intake,
import-graph construction, cycle rejection, and total primary diagnostic
order.

Root and selected-module imports use the same closed three-field schema.
Applicable requirements retain exact constraint text, interval, alias,
logical source path, and contributor. Text ordering uses unsigned NFC UTF-8
bytes except where the erratum assigns arbitrary-size numeric version order.

## Existing Lockfile intake and reuse

Optional Lockfile input is immutable bytes, never a path. Supplied bytes pass
the exact source, six-member closed-schema, existing `lock_id`, and context
gates in that order. Resolve verifies an existing `lock_id` but never creates
one.

Context binds lattice `0.3`, the exact active profile, and the root Blueprint
digest inside ScannedSource. Reuse is decided independently for each required
package. Stale version, stale identity, missing entry, profile ineligibility,
and constraint incompatibility are nonfatal per-package misses followed by
the ordinary greatest eligible satisfying selection. Valid extra entries are
retained as sorted unreferenced entries and create no selection.

## Candidate grouping and numeric selection

Candidate groups are keyed by package name and arbitrary-size numeric
`major.minor.patch` version. Byte-identical semantic records collapse.
Different package identities for one name and version fail under the accepted
duplicate rule, although that condition is not constructible through the
current public ScannedSource boundary.

For every required package, Resolve distinguishes no package group, no
active-profile-eligible candidate, and no candidate satisfying all applicable
constraints. A compatible reusable Lockfile entry is preferred; otherwise
the numerically greatest eligible satisfying candidate is selected.

## Replacement, contribution retraction, and passes

Every pass computes its complete next selection simultaneously from the
pass-start contribution state. Root contributions always apply. Selected
package contributions apply only when reachable from root through pass-start
selections.

Reachability and contributions are recomputed from root on every pass.
Contributions from replaced or unreachable selections retract before the next
pass. Names not required in the current pass are absent from the next
selection.

Passes are numbered 1 through 256. Success requires one complete unchanged
pass under the exact selection-state equality rule. An unchanged pass 256 may
succeed. If pass 256 changes, pass 257 is not started and
`RESOLVE_PASS_LIMIT` is returned at `resolve#/passes/257`. A repeated
non-adjacent historical state is not success.

## Selected-module continuity

Resolve locates each selected descriptor's `module_file` only in that
candidate's immutable verified-file mapping. It applies the accepted PC2
restricted-YAML parser to those exact retained bytes and uses the accepted
six-code Resolve crosswalk.

The selected module uses the exact full Core root envelope and metadata
binding frozen by the erratum. A missing `imports` member contributes no
requirement but is not inserted into the retained parsed value. Declaration
elements remain opaque. Resolve performs no imported declaration defaulting,
namespace expansion, normalization, generated-structure insertion, or static
checking.

Every successful selected-module record binds the selected PC6 package
record, `module_file`, exact retained bytes, declared byte digest, one PC2
parsed value, and admitted imports projection. Later phases must consume that
retained representation and must not parse another byte source.

## Envelope admission, graph, and cycles

The selected-module envelope, independently reachable import defects, and
metadata binding follow the erratum's gathering and total-order rules.
Multiple selected-module intake failures reachable in one pass are compared
under the accepted diagnostic order; no partial output exists.

After an unchanged pass, Resolve constructs the exact root and selected
package graph. Every applicable requirement creates one labeled directed
edge. Parallel edges remain distinct. Cycle selection enumerates simple
directed edge cycles, rotates but never reverses each sequence, and selects
the bytewise least normalized token sequence. Cycle detection occurs only
after convergence and therefore follows module-intake failures and the pass
limit.

Traversal implementation form is nonnormative. Iteration, recursion,
call-stack use, caching, and internal scheduling have no conformance
significance when all required observations are identical.

## Diagnostics and paths

The accepted erratum binds 21 Resolve diagnostic codes: three existing
Standard codes plus 18 newly specified Resolve codes. The durable manifest
contains 62 diagnostic fixture rows. These are different populations:
`21` counts unique phase diagnostic codes, while `62` counts current
diagnostic fixtures, including multiple paths, precedence comparisons, and
boundary discriminators that reuse codes.

Diagnostics use exactly the `root#`, `packages/`, `lock#`, and
`resolve#/passes/` logical anchors with the accepted pointer and
percent-encoding rules. Lower numeric rank controls only among candidates
simultaneously reachable inside one gate; mandatory earlier gates prevent
later diagnostics from existing. Complete canonical path breaks same-rank
ties.

Failure returns one primary object containing code and path, plus canonical
cycle detail only for `RESOLVE_IMPORT_CYCLE`. It returns no ResolvedSource and
no partial selection.

## Exact successful output

Successful `ResolvedSource` binds exactly the accepted twelve conceptual
members:

```text
scanned_source
active_profile
existing_lock
resolution_passes
selected_packages
selected_modules
applicable_requirements
import_graph
created_identities
created_artifacts
authority
phase_status
```

The first member is the exact consumed ScannedSource. The output retains every
semantically relevant pass, reuse, selected-record, selected-module,
requirement, provenance, and graph observation required by the erratum.
`created_identities` and `created_artifacts` are empty, `authority` is
`none`, and `phase_status` is
`non_authoritative_resolved_source`.

PC7 creates no identity. ResolvedSource, its trace, selected set, and graph
remain non-authoritative phase state. Existing package identities remain PC6
identities; an existing `lock_id` is verified input only.

## Operational resource treatment

Resolve semantics are finite and deterministic over finite accepted input.
The 256-pass rule is the sole semantic convergence bound. Memory, stack,
cache, scheduling, platform, locale, clock, randomness, filesystem, and
network state cannot select a semantic result.

Operational resource failure is a non-result outside `ResolveOutcome`. It
cannot substitute for a success or Resolve diagnostic and produces no partial
ResolvedSource.

## Strict deferral

PC7 does not generate, canonicalize for generation, identify, write, or
persist a Lockfile. Lock exclusively owns new canonical Lockfile content, new
`lock_id`, and atomic persistence.

PC7 does not own namespace expansion, import flattening, imported declaration
defaults, declaration validation, normalization, generated intake gates,
static checking, declaration identities, later collection sorting, Manifest,
qualification, Binding, Builder, runtime, providers, installation, CLI, MCP,
UI, Android, filesystem effects, network effects, secrets, models, events,
replay, or any product surface.

## Durable conformance criteria

The exact machine-readable manifest retains every authoritative schema,
construction rule, generator vocabulary, input, expected output, canonical
byte and hash, diagnostic code and path, precedence criterion, relation
selector, projection rule, chain-255 constructor, reference-expansion rule,
pass-boundary case, coverage ledger, and reference-closure datum reviewed for
PC7.

It contains 96 current fixtures and three separately recorded
non-dispatchable future vectors. Its closed schema has 118 categories. Its 43
registered new choices are NC-01 through NC-39 and NC-41 through NC-44.
NC-40 remains intentionally absent.

The current criteria are sufficient for a later implementation worker to
construct a strict deterministic plan generator and public-boundary
interpreter without consulting the authoring or review reports. That later
gate must still prove:

```text
defined_fixture_ids == generated_plan_ids == executed_fixture_ids
```

and compare complete results through the public PC7 boundary before maturity
can advance.

## Implementation boundary

This freeze creates no Rust type, function, diagnostic implementation,
fixture interpreter, deterministic plan generator, production test, Cargo
change, dependency, artifact, or product behavior. It authorizes only the
later PC7 Resolve implementation gate against the accepted erratum and
specified criteria.

```text
PC7_SCOPE_RECONCILED=true
RESOLVE_ERRATUM_CANDIDATE_COMPLETE=true
RESOLVE_ERRATUM_CANDIDATE_REVIEW_COMPLETE=true
RESOLVE_ERRATUM_REPAIR_COMPLETE=true
RESOLVE_ERRATUM_REPAIR_REVIEW_COMPLETE=true
RESOLVE_ERRATUM_SECOND_REPAIR_COMPLETE=true
RESOLVE_ERRATUM_SECOND_REPAIR_REVIEW_COMPLETE=true
RESOLVE_ERRATUM_REVIEW_P0=0
RESOLVE_ERRATUM_REVIEW_P1=0
RESOLVE_ERRATUM_REVIEW_P2=0
RESOLVE_ERRATUM_REVIEW_P3=1
RESOLVE_ERRATUM_ACCEPTED=true
PC7_SEMANTICS_FROZEN=true
PC7_IMPLEMENTATION_STARTED=false
PC7_ACCEPTED=false
PUSH_COMPLETE=true
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
NEXT_BOUNDED_TASK=PC7 Resolve implementation only
```
