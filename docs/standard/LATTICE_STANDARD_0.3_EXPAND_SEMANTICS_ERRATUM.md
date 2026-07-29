# Lattice Standard 0.3 Expand Semantics Erratum

Candidate and acceptance date: 2026-07-29.

Status: accepted and frozen normative companion for PC9 Expand after the
governing independent re-review closed `PC9-SEM-001`, `PC9-CRI-001`,
`PC9-CRI-002`, and `PC9-CRI-003` with P0=P1=P2=P3=0 and final disposition
`PASS`. Normative Sections 1 through 18 and the `EXPAND-N-19` rule bundle are
byte-identical to the reviewed candidate. Acceptance performs no
implementation, executable qualification, physical Lockfile persistence,
Normalize or later phase, Builder, runtime, provider, or product action.

Only clauses carrying an inline `[S]`, `[C]`, `[N]`, or `[D]` tag are
normative rule bundles. Headings, examples, definitions, explanatory text,
registers, and status statements are not additional rule bundles.

## Normative Section 1 — Authority, scope, and precedence

[S, `EXPAND-S-01`] Lattice Standard 0.3 remains primary authority. The
accepted Default, Canonical JSON, Package Scan, Resolve, and Lock companions
control only their declared domains. The accepted compiler allocation remains:

```text
Resolve -> Lock -> Expand -> Normalize -> Insert -> Static check ->
Identify -> Sort -> Manifest -> Persist
```

[C, `EXPAND-C-01`] If this candidate is later independently reviewed,
accepted, and published, it controls only the Standard's sparse Expand
allocation: namespace assignment, imported-declaration expansion, import
flattening, and `NAMESPACE_COLLISION`. It does not amend an earlier phase or
allocate a later one.

[D, `EXPAND-D-05`] This candidate does not accept or freeze itself. Separate
independent semantic review, any correctly classified repair, explicit
acceptance and publication, implementation impact assessment, implementation,
executable-conformance construction, qualification, independent
implementation review, product acceptance, and publication remain later
gates.

Rules are classified as `[S]` accepted-authority restatements, `[C]`
clarifications selecting an already-required reading, `[N]` new normative
choices closing an absence or ambiguity, and `[D]` explicit deferrals. Every
new choice is registered in Normative Section 17.

## Normative Section 2 — Exact operation and domain

[N, `EXPAND-N-01`, `EXPAND-NC-01`] Expand is the partial operation:

```text
expand(locked_source: accepted PC8 LockedSource)
    -> ExpandedSource | NAMESPACE_COLLISION
```

Its semantic input contains exactly one immutable accepted `LockedSource`.
There is no separately supplied root, package set, graph, module byte source,
parsed module, namespace map, Lockfile, path, host capability, or option.

[S, `EXPAND-S-02`] The exact consumed `LockedSource` is the sole source of the
accepted `ResolvedSource`, root `DefaultedSource`, selected packages, selected
modules, retained module bytes, admitted parsed representations, admitted
import projections, converged import graph, canonical Lockfile value, emitted
Lockfile bytes, and `lock_id`.

[C, `EXPAND-C-02`] Expand MUST preserve the exact consumed `LockedSource` as
one immutable member of every success. It MUST NOT reconstruct, independently
pair, replace, or override any nested source, package, module, graph, Lockfile,
byte sequence, or identity.

## Normative Section 3 — Preserved earlier ownership

[S, `EXPAND-S-03`] Resolve exclusively owns candidate discovery, package
selection, active-profile eligibility, existing-Lockfile intake and reuse,
fixed-point convergence, requirement reachability and retraction,
selected-module parsing, module-envelope admission, applicable requirements,
retained import edges, graph construction, and import-cycle rejection.

[C, `EXPAND-C-03`] Expand traverses only the converged retained graph and
admitted import projections in the consumed `LockedSource`. A package name is
looked up only in the already selected package mapping. Expand MUST NOT scan a
snapshot, inspect a descriptor, parse or reparse source bytes, collect or
intersect a version requirement, select or replace a version, consult a prior
Lockfile, or rediscover an edge.

[S, `EXPAND-S-04`] Lock exclusively owns the complete canonical Lockfile
value, its omission preimage, `lock_id`, emitted bytes, source binding, created
identity, and created artifact.

[C, `EXPAND-C-04`] Expand MUST leave the Lockfile value, omission-preimage
meaning, `lock_id`, emitted bytes, and `LockedSource` binding unchanged. The
physical `PC8 Lockfile Persistence Adapter` is neither an Expand prerequisite
nor an Expand operation.

[C, `EXPAND-C-08`] `RESOLVE_IMPORT_CYCLE` is unreachable in the authenticated
Expand domain because accepted Resolve success has already rejected every
cycle. Expand MUST NOT emit, reinterpret, or inherit that code. A forged cyclic
phase object is outside the domain rather than a new Expand input.

## Normative Section 4 — Namespace paths and module instances

Namespace segment means one exact admitted Resolve import alias. Namespace
path means a nonempty ordered sequence of namespace segments. Its rendering is
the segments joined by the two ASCII characters `::`, with no leading or
trailing separator.

[S, `EXPAND-S-05`] A directly imported module receives its incoming root-edge
alias as namespace. A declaration with local name `x` reached through root
alias `a` therefore has effective name `a::x`.

[S, `EXPAND-S-06`] A transitive import receives an internal chained namespace.
For a parent namespace path `P` and an outgoing admitted edge whose alias is
`a`, the child namespace path is exactly `P` followed by `a`.

[N, `EXPAND-N-02`, `EXPAND-NC-02`] Expand creates one module-instance record
for every finite directed edge path beginning at the Resolve graph root. The
record binds the exact selected-module record at the path's terminal node to
that path's alias sequence and complete retained edge provenance. A selected
package reached by two different root-to-node paths produces two module
instances; package selection remains singular while namespace instantiation
is per path.

[N, `EXPAND-N-03`, `EXPAND-NC-03`] Namespace segments are exact alias strings,
never package names, module names, versions, identities, source paths, array
indexes, or implementation-generated abbreviations. Rendering performs no
case conversion, escaping, normalization beyond already accepted NFC, or
separator collapse.

[N, `EXPAND-N-04`, `EXPAND-NC-04`] Module-instance order is deterministic
depth-first pre-order over admitted import occurrences:

1. begin with root imports in increasing source-array index;
2. for an edge, append its child module instance;
3. recursively visit that child's admitted imports in increasing source-array
   index; and
4. after the complete child subtree, continue with the next sibling edge.

The retained import projection and edge provenance supply source indexes.
Resolve's canonical graph-edge presentation order and selected-package order
do not replace this traversal order.

[N, `EXPAND-N-05`, `EXPAND-NC-05`] The accepted graph is finite and acyclic,
so the traversal terminates. It does not memoize a selected package as
"already expanded" across different paths. Cache use, recursion, iteration,
and work scheduling are unobservable only when the exact module-instance
sequence remains identical.

## Normative Section 5 — Imported-module default materialization

[S, `EXPAND-S-10`] The accepted Default semantics define the only Standard
default values and exact insertion algorithm. Root default expansion occurred
before the Blueprint digest, and PC4 explicitly did not traverse package
content.

[N, `EXPAND-N-06`, `EXPAND-NC-06`] Before declarations are taken from a
selected module, Expand constructs a non-authoritative copied module value by
applying the accepted PC4 insertion algorithm exactly to the retained PC2
parsed module representation. This imported-module application:

1. inserts the eight absent optional root arrays `imports`, `inputs`,
   `contracts`, `resources`, `links`, `policies`, `exports`, and `scenarios`;
2. applies the exact root-input, root-export, unit-kind, unit-port, link,
   policy, and scenario defaults;
3. preserves every present, malformed, ambiguous, non-object, or non-target
   value under the accepted explicit-value rules;
4. preserves all array order and performs no arbitrary recursive search; and
5. is idempotent and produces no diagnostic.

The traversal graph still comes only from Resolve's admitted imports. An
inserted empty `imports` array does not discover an edge.

[C, `EXPAND-C-05`] This operation does not rerun PC4, create a second
`DefaultedSource`, alter the root `DefaultedSource`, alter
`blueprint_digest`, or replace the exact parsed representation retained by
Resolve. The retained bytes and parsed value remain unchanged inside the
preserved `LockedSource`; the copied value exists only in the corresponding
module-instance record and its flattened declaration records.

[C, `EXPAND-C-06`] The imported copied value contains no default-provenance
member, source-presence ledger, marker, sentinel, sidecar, compiler metadata,
identity, or authority field. Omitted and explicitly equal imported defaults
converge exactly as they do at the accepted root Default boundary.

## Normative Section 6 — Closed declaration collections

[N, `EXPAND-N-07`, `EXPAND-NC-07`] Expand recognizes exactly these eight
ordered declaration collections and discriminator members:

| Rank | Collection | Local-name discriminator |
|---:|---|---|
| 1 | `inputs` | `input` |
| 2 | `contracts` | `contract` |
| 3 | `resources` | `resource` |
| 4 | `units` | `unit` |
| 5 | `links` | `link` |
| 6 | `policies` | `policy` |
| 7 | `exports` | `export` |
| 8 | `scenarios` | `scenario` |

`imports` is composition control, not a flattened declaration collection.
Module metadata `lattice`, `profile`, `module`, `version`, and `purpose` is
retained in the module-instance copied value and is not moved into a
declaration collection.

[S, `EXPAND-S-07`] Every declaration element from every imported module is
flattened. No visibility filter, export list, same-name merge, deduplication,
or inferred cross-module link exists.

[S, `EXPAND-S-08`] Imported module `inputs` and `exports` remain explicit
boundaries. They are flattened into their respective collections with
namespace and provenance; they are not merged with root boundaries and do not
cause an implicit link, gate, adapter, or value transfer.

## Normative Section 7 — Expanded declaration records

[N, `EXPAND-N-08`, `EXPAND-NC-08`] One expanded declaration record has exactly
these conceptual members:

```text
collection
namespace_segments
namespace
effective_name
source_value
provenance
```

`collection` is one of the eight collection strings. `namespace_segments` is
`[]` for root declarations and the module-instance namespace path for imported
declarations. `namespace` is the empty string for root declarations and the
exact rendered namespace for imported declarations. `source_value` is the
exact root post-PC4 element or the exact element from the imported copied
module value.

[N, `EXPAND-N-11`, `EXPAND-NC-11`] `effective_name` is derived without
validating any other declaration field. If `source_value` is an object whose
collection discriminator is a string matching the accepted local-name grammar,
then:

```text
root effective name     = local name
imported effective name = namespace + "::" + local name
```

Otherwise `effective_name` is JSON null. The declaration remains present and
unchanged for Normalize. Expand MUST NOT repair a discriminator or treat an
invalid discriminator string as an expanded name.

[N, `EXPAND-N-14`, `EXPAND-NC-14`] Root provenance has exactly kind `root`,
root module name, source collection, numeric source index, and logical source
path `root#/<collection>/<index>`. Imported provenance has exactly kind
`import`, package name, selected version, package identity, module-file
logical path, declared retained-byte SHA-256, namespace path, complete ordered
incoming import-chain edge records, source collection, numeric source index,
and the accepted selected-module logical path ending
`#/<collection>/<index>`.

The import chain is ordered root-to-terminal and each edge record retains its
contributor, target selected package, alias, exact constraint text, and exact
Resolve source path. No host path, timestamp, cache key, compiler version, or
runtime datum enters provenance.

## Normative Section 8 — Flattened collection order

[N, `EXPAND-N-09`, `EXPAND-NC-09`] In each declaration collection, every root
element appears first in its existing root array order. Root elements are not
sorted, deduplicated, rewritten, or copied from any post-PC4 reconstruction.

[N, `EXPAND-N-10`, `EXPAND-NC-10`] Imported records then appear by
module-instance order from Normative Section 4 and, within each instance and
collection, by the copied module array's existing index order. Empty
collections contribute no record. Expand performs no identity sort; the later
`Sort` phase remains the owner of canonical identity-bearing collection order.

## Normative Section 9 — Alias and reference treatment

[C, `EXPAND-C-07`] Namespace assignment does not rewrite arbitrary strings in
a declaration body. Source discriminator spelling and every reference,
endpoint, resource, route, policy path, controller label, and other body value
remain value-for-value except for the exact imported defaults in Normative
Section 5.

[N, `EXPAND-N-16`, `EXPAND-NC-16`] Every success supplies a deterministic
reference context for Normalize. In root context, a direct import alias `a`
maps to namespace path `[a]`. In module-instance context `P`, each direct
admitted child alias `a` maps to `P + [a]`. The bindings preserve source import
array order. They neither resolve a declaration nor assert that a referenced
local name exists.

[D, `EXPAND-D-02`] Normalize owns declaration-form and body admission plus
symbol interpretation. Given a valid source local reference `x`, its current
namespace context supplies the candidate effective name `P::x` for a nonempty
`P` and `x` at root. Given the Standard direct-import source spelling
`a::x`, the context supplies child namespace `P + [a]` and candidate effective
name `P::a::x`. Validation of spelling, target class, existence, endpoint
syntax, ambiguity, and compatibility remains Normalize or a later explicitly
accepted allocation.

## Normative Section 10 — Namespace collision

[S, `EXPAND-S-09`] `NAMESPACE_COLLISION` means an expanded declaration
collision and is owned by Expand.

[N, `EXPAND-N-12`, `EXPAND-NC-12`] A collision key is the ordered pair
`(collection, effective_name)` for records whose `effective_name` is not null.
A collision group exists when at least two records have one equal key and at
least one record in the group is imported. Collections are distinct collision
domains: equal names in `inputs` and `exports`, or in any two different
collections, do not collide. Equal root-only records are not introduced by
expansion and therefore remain outside `NAMESPACE_COLLISION`.

[D, `EXPAND-D-01`] A non-object declaration, missing discriminator, non-string
discriminator, invalid local name, duplicate root-only name, unknown
declaration member, wrong field type, unsupported form, or invalid reference
is retained for Normalize. Existing `SOURCE_DUPLICATE_NAME` meaning is not
reallocated to root-only duplicates.

[N, `EXPAND-N-13`, `EXPAND-NC-13`] Collision selection occurs after complete
module-instance and declaration construction. For each group, the first and
second records are its first two records in the frozen collection order.
The collection ordinal of a record is its zero-based position in that complete
frozen collection order: the first record has ordinal `0`, the next has
ordinal `1`, and each following record's ordinal is one greater. A collection
ordinal is not a declaration provenance `source_index`; the two can differ
when root records or earlier module instances contribute to the collection.
The diagnostic's `first_provenance` and `second_provenance` are copied from
the records at the selected zero-based first and second collection ordinals.
Choose the primary group by collection rank, then effective-name unsigned NFC
UTF-8 bytes, then second record's numeric collection ordinal, then first
record's numeric collection ordinal.

The primary path is:

```text
expand#/declarations/<collection>/<second-ordinal>/<discriminator>
```

Ordinals are minimal unsigned decimal and are compared numerically for
selection, not as rendered path bytes. The diagnostic detail contains exactly
`collection`, `effective_name`, `first_provenance`, and `second_provenance`.

[N, `EXPAND-N-17`, `EXPAND-NC-17`] Expand has one semantic diagnostic code:
`NAMESPACE_COLLISION`. On collision it returns exactly one primary diagnostic
with `code`, `path`, and the four-member detail above, and no `ExpandedSource`
or partial success. If no collision exists, it returns the one complete
success in Normative Section 11.

## Normative Section 11 — Exact successful output

[N, `EXPAND-N-14`, `EXPAND-NC-14`] Success returns one opaque
`ExpandedSource` containing exactly these conceptual members:

```text
locked_source
root_reference_context
module_instances
declarations
created_identities
created_artifacts
authority
phase_status
```

`locked_source` is the exact consumed object. `root_reference_context` is the
ordered direct-root alias binding sequence. `module_instances` is the complete
ordered sequence from Normative Sections 4 and 5. `declarations` is an object
with exactly the eight collections in Normative Section 6, each containing its
complete ordered expanded records.

[N, `EXPAND-N-15`, `EXPAND-NC-15`] `created_identities` and
`created_artifacts` are both empty sequences. `authority` is the literal
`none`. `phase_status` is the literal
`non_authoritative_expanded_source`. The wrapper, namespace paths,
module-instance sequence, imported copied values, expanded declaration
records, provenance, and reference contexts receive no Lattice identity and
are not standalone artifacts.

[S, `EXPAND-S-11`] Existing `blueprint_digest`, package identities, Lockfile,
and `lock_id` retain their earlier meanings and exact bytes. Expand creates no
resource, contract, unit, link, policy, scenario, Manifest, qualification,
Binding, envelope, event, activation, or runtime identity.

## Normative Section 12 — Determinism and resource treatment

[N, `EXPAND-N-18`, `EXPAND-NC-18`] Expand is deterministic and finite over its
authenticated finite acyclic input. Filesystem state, network state, physical
Lockfile presence, locale, object-map iteration, selected-package
presentation, graph-edge presentation, stack availability, cache state,
thread scheduling, clock, randomness, compiler identity, and host-width
integers MUST NOT select a different traversal, namespace, copied value,
record, order, provenance, collision, path, diagnostic, or success.

[C, `EXPAND-C-09`] Allocation failure, stack exhaustion, process interruption,
or another implementation resource failure is an operational non-result. It
cannot substitute for `NAMESPACE_COLLISION`, return partial phase state, or
change an otherwise successful semantic result.

## Normative Section 13 — Next-consumer contract

[S, `EXPAND-S-12`] Normalize is the immediate consumer and remains the owner of
resolved declaration forms.

[N, `EXPAND-N-16`, `EXPAND-NC-16`] Normalize MUST consume the exact
`ExpandedSource`, including its root and per-instance reference contexts,
effective-name candidates, complete source values, collection membership,
order, and provenance. It MUST NOT re-expand imports, choose another namespace
path, reapply imported defaults, reparse module bytes, or reconstruct
provenance from a live source.

[D, `EXPAND-D-03`] Normalize, Insert, Static check, Identify, Sort, Manifest,
and Persist retain their named later operations. Expand creates no normalized
declaration, generated intake gate, cross-declaration validity result,
declaration identity, canonical post-identity order, Manifest, or Manifest
persistence result.

[D, `EXPAND-D-04`] The separately named `PC8 Lockfile Persistence Adapter`
remains later and independent. Expand consumes the in-memory source-bound
`LockedSource` and MUST NOT require or claim physical Lockfile persistence.

## Normative Section 14 — Authority and product exclusions

[N, `EXPAND-N-15`, `EXPAND-NC-15`] `ExpandedSource` is non-authoritative
compiler phase state. Namespace assignment and imported default
materialization grant no permission and do not make a declaration valid,
identified, executable, qualified, or bound.

[D, `EXPAND-D-06`] Builder, runtime, providers, package installation, network,
filesystem effects, secrets, models, execution, qualification, events,
replay, CLI, MCP, UI, Android, and every other product surface remain
unauthorized.

[D, `EXPAND-D-07`] A future language version that admits non-ASCII or otherwise
different alias grammar, multi-segment source import references, package
composition outside the accepted Resolve boundary, or cyclic import semantics
requires separately accepted authority. This candidate does not fabricate
current public inputs for those domains.

[D, `EXPAND-D-08`] Expand does not settle the later identity preimage or
canonical sorting of normalized declarations. Criteria may prove that Expand
preserves distinctions that later identities must be able to observe, but
they MUST NOT claim a declaration identity before Identify.

## Normative Section 15 — Specified conformance criteria

[N, `EXPAND-N-19`, `EXPAND-NC-19`] The standalone PC9 manifest is
machine-readable specified criteria. It has a finite closed schema language,
a recursively closed manifest schema, exact populations, exact identifier
orders, complete reference resolution, current public PC2-through-PC8
constructions, complete expected Expand semantic projections, success and
failure relations, negative discriminators, isolated schema mutations,
authority attribution, and explicit future-only activation conditions.

Every current input MUST be constructed through the public accepted phase
sequence from exact root bytes and an exact portable snapshot. No forged
`LockedSource`, selected-module injection, alternate parser, opaque fixture,
or current use of a future-only row is admitted. Every expected value MUST be
derived without consulting actual Expand output.

Every schema mutation starts from a complete admitted manifest value at one
named schema occurrence. The exact mutation MUST reject at the named
mechanism, and bypassing or removing only that mechanism MUST admit the
otherwise unchanged value. Rejection for a second reason is not isolation.
Structural schema validation is followed by each declared post-schema
validator in ascending validator identifier order; a mutation naming such a
validator is not isolated unless structural validation first admits both
values, the named validator alone rejects the mutant at its declared path,
and omitting only that validator admits it.

Each discriminator names a concrete rejected algorithm, an exact changed
observable, and at least one closed vector. Collision-selector vectors retain
both the normative complete diagnostic and the complete diagnostic selected
by the rejected algorithm. Boundary vectors use a publicly constructed phase
intermediate, not an opaque forged object, and ambient vectors name both
controlled environments over one exact LockedSource.

The manifest's `construction_sha256` is non-normative criteria provenance,
not a Lattice identity or an Expand operation input, output, artifact, or
preimage. Its criteria-only construction protocol declares the exact member
set, Canonical JSON encoding, UTF-8 byte treatment, and SHA-256 operation.

The criteria distinguish `specified`, `dispatchable`, `executable`,
`qualified`, and `future_only`. At this gate only `specified=true`; all current
dispatch, execution, and qualification claims are false.

## Normative Section 16 — Observable inventory

[C, `EXPAND-C-10`] The complete Expand observables are: success versus
failure; the exact preserved `LockedSource`; root reference context;
module-instance membership and order; namespace segments and rendering;
imported copied module values; declaration collection membership and order;
effective-name candidates including null; complete source values; provenance
and import chains; `NAMESPACE_COLLISION` code, path, detail, and precedence;
empty created identity and artifact populations; literal authority and phase
status; and the exact next-consumer boundary. No canonical byte sequence or
new identity preimage is created by Expand, so no Expand identity-preimage
registry exists.

## Normative Section 17 — Exhaustive new-choice register

| Choice | New normative choice | Principal discriminators |
|---|---|---|
| `EXPAND-NC-01` | Expand consumes exactly one accepted LockedSource and returns complete success or NAMESPACE_COLLISION. | `DISC-INPUT-BOUNDARY`, `DISC-COLLISION-FAILURE` |
| `EXPAND-NC-02` | One module instance exists per rooted import-edge path, not per selected package. | `DISC-DAG-REINSTANTIATION` |
| `EXPAND-NC-03` | Namespace segments are exact aliases and render only by `::` joining. | `DISC-ALIAS-NAMESPACE`, `DISC-CHAINED-NAMESPACE` |
| `EXPAND-NC-04` | Instance traversal is source-index depth-first pre-order. | `DISC-DFS-PREORDER`, `DISC-ROOT-IMPORT-ORDER` |
| `EXPAND-NC-05` | Different paths to one selected package remain separate instances and traversal terminates on the accepted acyclic graph. | `DISC-DAG-REINSTANTIATION`, `DISC-NO-RESOLVE-CYCLE` |
| `EXPAND-NC-06` | Imported copied modules receive the exact PC4 default algorithm without changing root or retained parsed values. | `DISC-IMPORTED-DEFAULTS`, `DISC-EXPLICIT-DEFAULT-EQUIVALENCE`, `DISC-PARSED-PRESERVATION` |
| `EXPAND-NC-07` | Exactly eight declaration collections and their exact discriminators are flattened. | `DISC-EIGHT-COLLECTIONS`, `DISC-IMPORTS-NOT-DECLARATION` |
| `EXPAND-NC-08` | Every expanded declaration has the exact six-member record. | `DISC-RECORD-CLOSURE` |
| `EXPAND-NC-09` | Root records precede imported records and preserve root array order. | `DISC-ROOT-FIRST`, `DISC-ROOT-ORDER` |
| `EXPAND-NC-10` | Imported records use instance order then source array order; Sort remains later. | `DISC-IMPORTED-ORDER`, `DISC-SOURCE-INDEX-10` |
| `EXPAND-NC-11` | Effective names derive only from valid collection discriminators; invalid headers remain with null names. | `DISC-MALFORMED-DEFER`, `DISC-INVALID-NAME-DEFER` |
| `EXPAND-NC-12` | Collision keys are collection plus effective name, require imported participation, and never cross collections. | `DISC-COLLISION`, `DISC-CROSS-COLLECTION`, `DISC-ROOT-DUPLICATE-DEFER` |
| `EXPAND-NC-13` | Collision precedence and path use collection rank, name bytes, zero-based numeric collection ordinals, and the second record. | `DISC-COLLISION-PRECEDENCE`, `DISC-SOURCE-INDEX-10` |
| `EXPAND-NC-14` | Success has the exact eight-member source-bound structure and complete root/import provenance. | `DISC-OUTPUT-CLOSURE`, `DISC-PROVENANCE` |
| `EXPAND-NC-15` | Expand creates no identity, artifact, or authority. | `DISC-NO-CREATED-STATE` |
| `EXPAND-NC-16` | Reference contexts map direct aliases to child namespace paths while body interpretation remains Normalize-owned. | `DISC-REFERENCE-CONTEXT`, `DISC-NO-BODY-REWRITE` |
| `EXPAND-NC-17` | NAMESPACE_COLLISION is the only semantic failure and returns no partial success. | `DISC-COLLISION-FAILURE`, `DISC-NO-RESOLVE-CYCLE` |
| `EXPAND-NC-18` | Ambient and resource state cannot change a semantic Expand result. | `DISC-AMBIENT-INDEPENDENCE` |
| `EXPAND-NC-19` | The specified manifest has closed schemas, populations, references, constructions, discriminators, mutations, and maturity claims. | `DISC-MANIFEST-CLOSURE`, `DISC-SCHEMA-ISOLATION` |

The exact new-choice population is 19.

## Normative Section 18 — Rule-provenance ledger

| Rule | Class | Complete rule bundle |
|---|:---:|---|
| `EXPAND-S-01` | `[S]` | Accepted pipeline position and phase order. |
| `EXPAND-S-02` | `[S]` | LockedSource is the sole route to exact accepted earlier state. |
| `EXPAND-S-03` | `[S]` | Resolve retains selection, intake, graph, and cycle ownership. |
| `EXPAND-S-04` | `[S]` | Lock retains Lockfile bytes, identity, artifact, and binding ownership. |
| `EXPAND-S-05` | `[S]` | Direct imports use incoming aliases as namespaces. |
| `EXPAND-S-06` | `[S]` | Transitive imports use chained internal namespaces. |
| `EXPAND-S-07` | `[S]` | Imported declarations flatten without merge or visibility inference. |
| `EXPAND-S-08` | `[S]` | Imported inputs and exports remain explicit boundaries. |
| `EXPAND-S-09` | `[S]` | Expand owns NAMESPACE_COLLISION. |
| `EXPAND-S-10` | `[S]` | Accepted PC4 values and insertion algorithm are the only defaults. |
| `EXPAND-S-11` | `[S]` | Existing identities and Lock artifact remain earlier-phase identities. |
| `EXPAND-S-12` | `[S]` | Normalize is the immediate consumer and resolved-form owner. |
| `EXPAND-C-01` | `[C]` | Candidate precedence is limited to Expand. |
| `EXPAND-C-02` | `[C]` | Exact LockedSource preservation forbids reconstruction or field pairing. |
| `EXPAND-C-03` | `[C]` | Traversal consumes retained admitted edges without rediscovery. |
| `EXPAND-C-04` | `[C]` | Lock projection and physical persistence remain unchanged and separate. |
| `EXPAND-C-05` | `[C]` | Imported default materialization neither reruns PC4 nor changes root digest or retained parse. |
| `EXPAND-C-06` | `[C]` | Imported copied values contain no default-provenance metadata. |
| `EXPAND-C-07` | `[C]` | Body strings and references are not rewritten by namespace assignment. |
| `EXPAND-C-08` | `[C]` | RESOLVE_IMPORT_CYCLE is outside successful Expand intake. |
| `EXPAND-C-09` | `[C]` | Resource failures are operational non-results. |
| `EXPAND-C-10` | `[C]` | Observable inventory is closed and contains no new byte preimage. |
| `EXPAND-N-01` | `[N]` | Exact operation, sole input, and success/failure variant. |
| `EXPAND-N-02` | `[N]` | One module instance per root-to-node edge path. |
| `EXPAND-N-03` | `[N]` | Alias-only namespace construction and rendering. |
| `EXPAND-N-04` | `[N]` | Source-index depth-first pre-order traversal. |
| `EXPAND-N-05` | `[N]` | Path-sensitive re-instantiation, termination, and cache non-observability. |
| `EXPAND-N-06` | `[N]` | Exact imported-module default materialization. |
| `EXPAND-N-07` | `[N]` | Closed declaration collections and discriminator registry. |
| `EXPAND-N-08` | `[N]` | Six-member expanded declaration record. |
| `EXPAND-N-09` | `[N]` | Root-first, root-array-order flattening. |
| `EXPAND-N-10` | `[N]` | Instance-order and source-index imported flattening. |
| `EXPAND-N-11` | `[N]` | Effective-name derivation and null deferral. |
| `EXPAND-N-12` | `[N]` | Collection-scoped collision key and imported-participation rule. |
| `EXPAND-N-13` | `[N]` | Collision precedence, zero-based numeric collection ordinals, path, and detail. |
| `EXPAND-N-14` | `[N]` | Exact successful structure and complete provenance. |
| `EXPAND-N-15` | `[N]` | Empty created populations and no authority. |
| `EXPAND-N-16` | `[N]` | Root and per-instance reference contexts plus exact Normalize intake. |
| `EXPAND-N-17` | `[N]` | Single diagnostic vocabulary and no partial result. |
| `EXPAND-N-18` | `[N]` | Finite ambient-independent determinism. |
| `EXPAND-N-19` | `[N]` | Closed specified-conformance criteria and maturity distinction. |
| `EXPAND-D-01` | `[D]` | Malformed declarations and root-only duplicates remain Normalize-owned. |
| `EXPAND-D-02` | `[D]` | Reference spelling, target, existence, and compatibility remain Normalize or later. |
| `EXPAND-D-03` | `[D]` | Normalize through Persist retain their named later operations. |
| `EXPAND-D-04` | `[D]` | Physical Lockfile persistence remains a separate PC8 adapter tranche. |
| `EXPAND-D-05` | `[D]` | Review, acceptance, implementation, qualification, and publication remain later gates. |
| `EXPAND-D-06` | `[D]` | Builder, runtime, providers, installation, effects, and user surfaces remain unauthorized. |
| `EXPAND-D-07` | `[D]` | Future alias, source-reference, composition, and cycle domains require new authority. |
| `EXPAND-D-08` | `[D]` | Declaration identities and canonical post-identity sorting remain later. |

The exact rule population is 49: 12 `[S]`, 10 `[C]`, 19 `[N]`, and 8 `[D]`.

## Normative Section 19 — Candidate disposition

[N, `EXPAND-N-19`, `EXPAND-NC-19`] Two conforming implementations applying
this candidate and its closed specified criteria to the same accepted
`LockedSource` MUST derive the same success/failure branch, module instances,
namespaces, imported copied values, declaration records, orders, effective
names, provenance, reference contexts, collision diagnostic and path, empty
created populations, authority, phase status, and next-consumer state.

```text
PC9_SCOPE_RECONCILIATION_CANDIDATE_COMPLETE=true
PC9_SEMANTIC_FREEZE_CANDIDATE_COMPLETE=true
PC9_SPECIFIED_CONFORMANCE_CANDIDATE_COMPLETE=true
PC9_SCOPE_RECONCILIATION_REPAIR_COMPLETE=true
PC9_SEMANTIC_REPAIR_COMPLETE=true
PC9_CRITERIA_REPAIR_COMPLETE=true
PC9_GOVERNING_FINDINGS_CLOSED=4
PC9_REVIEW_P0=0
PC9_REVIEW_P1=0
PC9_REVIEW_P2=0
PC9_REVIEW_P3=0
PC9_SEMANTICS_ACCEPTED=true
PC9_SPECIFIED_CONFORMANCE_ACCEPTED=true
PC9_SEMANTIC_FREEZE_COMPLETE=true
PC9_SEMANTICS_FROZEN=true
PC9_DOCUMENTATION_PUBLISHED=true
PC9_IMPLEMENTATION_STARTED=false
PC9_EXECUTABLE_CONFORMANCE_COMPLETE=false
PC9_QUALIFIED=false
PC9_ACCEPTED=false
OPEN_PC9_NORMATIVE_DEFECTS=0
OPEN_PC9_CONFORMANCE_CRITERIA_DEFECTS=0
OPEN_PC9_IMPLEMENTATION_DEFECTS=0
OPEN_PC9_PROCEDURAL_DEFECTS=0
OPEN_NORMATIVE_DEFECTS=0
OPEN_CONFORMANCE_CRITERIA_DEFECTS=0
OPEN_IMPLEMENTATION_DEFECTS=0
OPEN_PROCEDURAL_DEFECTS=0
FIXTURE_MATURITY=specified
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
PUSH_COMPLETE=true
FINAL_DISPOSITION=PASS
NEXT_BOUNDED_TASK=separate read-only PC9 implementation and executable-conformance impact assessment against the newly frozen authority
```
