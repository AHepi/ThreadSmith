# PC9 Expand Semantic Freeze

Freeze-candidate date: 2026-07-29.

Acceptance date: 2026-07-29.

Status: semantic freeze accepted and published after the governing independent
re-review closed all four original findings with P0=P1=P2=P3=0 and final
disposition `PASS`. The frozen semantic region is byte-identical to the
reviewed candidate. PC9 implementation has not started and overall PC9 product
acceptance remains false.

## 1. Bound baseline

```text
Repository=/workspace/ThreadSmith/repository
Branch=main
HEAD=630b664af272afaffb514b9dde8275cfc95357e9
Tree=f0d0303b3734da350f423f8ad146bcd4f32b5eee
Parent=eb6f1e35d314f3c436402f122f4752e4ecc34073
Subject=Implement and accept PC8 Lock
Remote_main=630b664af272afaffb514b9dde8275cfc95357e9
Initial_index=empty
Initial_tracked_differences=absent
Initial_untracked_paths=absent
Applicable_AGENTS.md=none
```

The exact accepted authority hierarchy and identities are bound in
`PC9_SCOPE_RECONCILIATION.md` and the standalone PC9 manifest. The focused
Expand candidate does not modify any accepted PC1-PC8 byte.

## 2. Frozen-candidate boundary

```text
accepted immutable PC8 LockedSource
        |
        v
PC9 Expand
  retained-graph traversal
  alias namespaces
  imported defaults
  flattened declaration records
  NAMESPACE_COLLISION
        |
        v
non-authoritative ExpandedSource
        |
        v
Normalize
```

Physical Lockfile persistence is not required to enter this boundary.

## 3. Exact input

Expand consumes exactly one accepted immutable `LockedSource`. There is no
second semantic input.

The following enter only through that object and remain exact:

```text
ResolvedSource and ScannedSource
root DefaultedSource and blueprint_digest
selected package records and package identities
retained module bytes, declared hashes, and parsed module values
admitted import projections, source indexes, graph, and edge provenance
canonical Lockfile value, emitted bytes, and lock_id
```

No path, snapshot, descriptor input, prior Lockfile input, host capability,
clock, random value, locale, environment variable, network, provider, cache,
compiler identity, or physical persistence state is an input.

## 4. Frozen-candidate module-instance construction

One module instance exists for each directed root-to-selected-node edge path
in the accepted acyclic Resolve graph.

For each path:

```text
namespace_segments = incoming aliases in root-to-terminal order
namespace = namespace_segments joined by "::"
selected_module = exact retained selected-module record at terminal node
import_chain = exact retained edge records in root-to-terminal order
```

A selected package reached by different paths produces different module
instances. Selection is not repeated.

Instance order is source-index depth-first pre-order: append each child before
its descendants, fully traverse that subtree, then continue with the next
sibling. Root and module child edges use increasing original imports-array
index. Selected-package and canonical graph presentation order do not control
instance order.

The graph is finite and cycle-free by accepted Resolve success. Expand never
emits `RESOLVE_IMPORT_CYCLE`.

## 5. Frozen-candidate imported defaults

Before flattening one instance, apply the exact accepted PC4 algorithm to a
copy of its retained parsed module value:

```text
eight optional root arrays
root input defaults
root export cardinality
recognized unit-kind defaults
unit input and output defaults
link mode, delivery, and true predicate
policy true predicate
scenario required
```

Present and malformed values, non-object elements, invalid containers, array
order, and non-target fields obey the exact accepted PC4 preservation rules.
No new default exists.

The root `DefaultedSource`, Blueprint digest, retained selected-module parsed
value, package identity, Lockfile, and `lock_id` do not change. The copied
value contains no default marker or provenance member and creates no
`DefaultedSource`.

## 6. Frozen-candidate collection registry

| Rank | Collection | Discriminator |
|---:|---|---|
| 1 | `inputs` | `input` |
| 2 | `contracts` | `contract` |
| 3 | `resources` | `resource` |
| 4 | `units` | `unit` |
| 5 | `links` | `link` |
| 6 | `policies` | `policy` |
| 7 | `exports` | `export` |
| 8 | `scenarios` | `scenario` |

`imports` is not a declaration collection. Module metadata remains in the
module-instance copied value.

All imported declaration elements move into their collection. Imported inputs
and exports remain explicit boundaries. Expand performs no visibility filter,
merge, deduplication, implicit link, gate, or adapter insertion.

## 7. Frozen-candidate expanded declaration record

Every record has exactly:

```text
collection
namespace_segments
namespace
effective_name
source_value
provenance
```

For root records, namespace segments are `[]`, namespace is `""`, and
`source_value` is the exact element inside the root `DefaultedSource`. For
imported records, namespace comes from the module instance and `source_value`
is the exact element inside its imported copied value.

If the source value is an object and the collection discriminator is a valid
local-name string:

```text
root effective_name     = local name
imported effective_name = namespace + "::" + local name
```

Otherwise `effective_name=null` and the unchanged element remains for
Normalize.

Root provenance contains kind, root module, collection, numeric source index,
and logical root pointer. Imported provenance contains kind, package, version,
package identity, module file, retained-byte hash, namespace path, complete
import chain, collection, source index, and selected-module logical pointer.

## 8. Frozen-candidate flattened order

Each collection is ordered:

1. every root element in existing root array order;
2. each module instance in frozen instance order; and
3. each element in that copied module collection's existing array order.

No collection is sorted by name or identity in Expand. The later `Sort` phase
retains canonical post-identity collection sorting.

## 9. Frozen-candidate reference contexts

Expand leaves declaration body strings value-for-value unchanged except for
the exact imported defaults.

The root context binds each direct root alias `a` to namespace `[a]`.
Instance context `P` binds each direct child alias `a` to `P + [a]`. Bindings
preserve source import order.

Normalize receives these contexts. It remains responsible for admitting
declaration forms, interpreting local and direct-import reference spelling,
checking targets and existence, and producing resolved forms. Expand does not
rewrite references or infer a cross-module link.

## 10. Frozen-candidate collision

A collision key is:

```text
(collection, non-null effective_name)
```

At least two equal keys and at least one imported participant form a collision
group. Equal names in different collections do not collide. Root-only
duplicates and malformed names remain later declaration-validation concerns.

For each group, the first two occurrences are taken from frozen collection
order. A record's collection ordinal is its zero-based position in the
complete frozen collection order: the first record has ordinal `0`, the next
has ordinal `1`, and each following record's ordinal is one greater. This
ordinal is distinct from provenance `source_index` and can differ from it when
root records or earlier module instances precede the record. The selected
records at those zero-based ordinals supply `first_provenance` and
`second_provenance`. Select the primary group by:

```text
collection rank
effective-name unsigned NFC UTF-8 bytes
numeric second collection ordinal
numeric first collection ordinal
```

The exact path is:

```text
expand#/declarations/<collection>/<second-ordinal>/<discriminator>
```

The detail object has exactly:

```text
collection
effective_name
first_provenance
second_provenance
```

`NAMESPACE_COLLISION` is the only Expand semantic diagnostic. Failure returns
one diagnostic and no partial `ExpandedSource`.

## 11. Frozen-candidate successful output

Success contains exactly:

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

The first member is the exact consumed object. The two created populations are
exactly empty. `authority=none`.
`phase_status=non_authoritative_expanded_source`.

No namespace, instance, copied value, declaration record, provenance record,
reference context, or wrapper receives a Lattice identity or becomes a
standalone artifact.

## 12. Frozen-candidate preservation and distinction relations

The specified criteria require:

```text
exact LockedSource preservation
exact retained selected-module parsed-value preservation
exact Lockfile, emitted-byte, and lock_id preservation
omitted and explicitly equal imported defaults -> equal copied values
different aliases -> different namespaces and effective names
different root import order -> different DFS order
same selected package on two paths -> two instances
body reference strings -> byte/value equality before and after Expand
same valid local name in different collections -> success
root-only duplicates -> success at Expand and later deferral
imported equal collision keys -> exact NAMESPACE_COLLISION
ambient variation -> equal semantic projection
```

These relations do not claim a declaration identity, normalized form, static
validity, Manifest identity, qualification, or execution authority.

## 13. Manifest populations and closure

| Population | Cardinality |
|---|---:|
| `authority` | 21 |
| `rule_provenance` | 49 |
| `normative_choices` | 19 |
| `collections` | 8 |
| `schemas` | 23 |
| `public_constructions` | 20 |
| `fixtures` | 20 |
| `relations` | 15 |
| `selector_probes` | 7 |
| `boundary_probes` | 2 |
| `validators` | 1 |
| `discriminators` | 32 |
| `schema_mutations` | 10 |
| `future_only` | 5 |

The manifest's exact ordered identifier arrays are the ascending unsigned UTF-8
orders of their defined sets. Count equality alone is insufficient.

`SCHEMA-MANIFEST` reaches the complete manifest. `SCHEMA-SCHEMA` closes the
finite schema-row language. Its recursive node grammar permits exactly
primitive, constant, enum, array, object, reference, nullable, and union
forms. Every reference resolves exactly once and every schema traversal
terminates.

Every current construction supplies exact public root bytes and exact portable
snapshot bytes and must reach Expand through PC2-PC8. Expected semantic
projections are complete and independently fixed. Every relation names exact
fixture operands and comparison projection. Every discriminator cites one or
more rules or choices.

All ten schema mutations begin with an admitted complete value, change one
named occurrence, reject at the named schema mechanism, and admit when only
that mechanism is bypassed or removed. A rejection for any other reason does
not satisfy isolation.

Structural schema validation completes before declared post-schema validators
run in ascending validator identifier order. Every discriminator names a
concrete rejected algorithm and exact changed observable. Selector probes
retain complete normative and rejected diagnostics; boundary probes contain a
publicly derived negative operand or two controlled ambient operands.

`construction_sha256` is non-normative criteria provenance only. Its declared
canonical three-member preimage does not create a Lattice identity, Expand
operation preimage, artifact, input member, or output member.

## 14. Maturity and future-only boundary

Current maturity is exactly:

```text
specified=true
dispatchable=false
executable=false
qualified=false
implementation_verified=false
independently_reviewed=false
accepted=false
published=false
```

The five future-only rows cover non-ASCII/different alias grammar,
multi-segment source import references, cyclic import semantics, a future
ScannedSource composition seam, and physical Lockfile persistence. Each row
is non-dispatchable until its named accepted activation condition exists.

## 15. Explicit non-ownership

PC9 Expand does not:

```text
repeat Resolve or Lock
reparse selected module bytes
write or persist a Lockfile
validate complete declaration forms or bodies
resolve references
normalize declarations
insert generated gates
perform static checks
create declaration identities
canonically sort identified declarations
create or persist a Manifest
qualify, bind, execute, record, or replay
authorize Builder, runtime, providers, installation, CLI, MCP, UI, or Android
```

## 16. Accepted freeze status

```text
PC8_ACCEPTED=true
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
PC9_FIXTURE_INTERPRETER_COMPLETE=false
PC9_FOCUSED_QUALIFICATION_COMPLETE=false
PC9_QUALIFIED=false
PC9_IMPLEMENTATION_VERIFICATION_COMPLETE=false
PC9_IMPLEMENTATION_REVIEW_COMPLETE=false
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
