# PC4 Default-Expansion Semantic Freeze

Freeze date: 2026-07-22.

Status: frozen for implementation intake; PC4 product code is not implemented
or accepted.

## Boundary

```text
PC3 ValidatedSource
        |
        v
PC4 Default: exact absent-field insertion
        |
        v
non-authoritative DefaultedSource
        |
        v
PC5 Digest
```

The future PC4 boundary consumes accepted `ValidatedSource` and produces
`DefaultedSource`. Both types belong to `threadsmith-compiler`.
`DefaultedSource` carries one expanded `serde_json::Value` and no serialized
metadata. It proves only that the deterministic Default transformation ran; it
does not prove declaration validity or grant authority.

## Root defaults

Only these absent root members are inserted, each as `[]`, in this order:

```text
imports
inputs
contracts
resources
links
policies
exports
scenarios
```

`units` is required by PC3 and is never root-defaulted. No metadata root and no
other convenience root is permitted.

## Port defaults

Each JSON object in `/inputs` and `/units/*/inputs` receives these members only
when absent:

| Member | Exact JSON value |
|---|---|
| `required` | `true` |
| `cardinality` | `"one"` |
| `on_absence` | `"block"` |

Each JSON object in `/exports` and `/units/*/outputs` receives absent
`cardinality` as the exact JSON string `"one"`.

No other `inputs`, `outputs`, or similarly named member is traversed.

## Unit and model defaults

For each object in `/units`, an exact recognized `kind` string controls only
these absent-field insertions:

| `kind` | Member | Exact JSON value |
|---|---|---|
| `program` | `mode` | `"stateless"` |
| `model` | `mode` | `"stateless"` |
| `gate` | `mode` | `"stateless"` |
| `controller` | `mode` | `"event_sourced"` |
| `broker` | `mode` | `"external"` |
| `model` | `repair_attempts` | `0` |
| `model` | `fallback` | `false` |

Missing, non-string, and unknown kinds receive none of these kind-dependent
defaults. Their traversable input and output port arrays still receive the
context-independent port defaults.

The model `fallback` value remains non-authoritative source data. Neither its
default nor an explicit value creates a fallback route or weakens the later Run
Binding requirement.

## Predicate, link, policy, and scenario defaults

Each object in `/links` receives these absent members:

| Member | Exact JSON value |
|---|---|
| `mode` | `"data"` |
| `delivery` | `"multicast"` |
| `when` | `{"all":[]}` |

Each object in `/policies` receives absent `when` as exactly `{"all":[]}`.
This is the existing Core constant-true expression. It is not inserted into
controller transitions or any other location.

Each object in `/scenarios` receives absent `required` as JSON `true`.

No policy decision, permission, route group, transition, controller bound,
budget, contract, resource, or authority value is defaulted.

## Explicit-value precedence

JSON object membership alone determines presence. Any present target member is
copied unchanged and receives no replacement default. This includes an
explicit Standard default, a valid non-default, an empty string, empty array,
empty object, `null`, a wrong JSON type, a contradictory value, or any value
that later validation rejects.

Explicit root empty arrays remain explicit empty arrays. PC4 does not erase,
merge, sort, coerce, repair, or interpret explicit data.

## Malformed and ambiguous elements

A declaration-list or port-list element that is not a JSON object remains
unchanged. A unit `inputs` or `outputs` member that is not an array remains
unchanged and untraversed. Missing, non-string, and unknown unit kinds receive
no kind-dependent defaults. Unambiguous defaults elsewhere in the same object
still apply.

These cases produce successful `DefaultedSource`, not a diagnostic. Success
means only that default expansion completed. Later phases retain the original
invalid or ambiguous data and remain responsible for rejecting it.

## Traversal and determinism

The exact logical order is:

1. insert the eight root arrays in their frozen order;
2. traverse root inputs, then root exports, in existing array order;
3. traverse units in existing order, applying kind-dependent defaults before
   traversing that unit's inputs and outputs in their existing order; and
4. traverse links, policies, and scenarios, in that order and in existing
   array order.

Traversal never recursively searches arbitrary content. Object-member order
does not carry source semantics and is left to later canonical JSON. Array
order is preserved exactly.

For every accepted input `x`:

```text
default(default(x)) == default(x)
```

Repeated application, process restarts, map insertion order, and conforming
implementation language cannot alter output value equality.

## Output representation

`DefaultedSource` contains only the expanded JSON-shaped value. It contains no:

```text
default provenance
source-presence ledger
default marker
source span
diagnostic
compiler metadata
identity
authority marker
sidecar data
```

The wrapper's Rust type state is not serialized or identity-bearing. The
identity preimage visible to PC5 is only the expanded JSON value.

For default targets, omission and an explicit equal default converge. Source
presence for those fields is intentionally not retained. Explicit non-default
values remain distinct. Non-target absence remains absence.

## Identity boundary

Defaults participate in identity preimages because Standard sections 15 and 16
place default expansion before Blueprint and declaration hashing. PC4 supplies
the post-default preimage value but performs no canonical serialization, hash,
typed identity construction, comparison, persistence, or authority decision.

Identity-equivalence fixtures compare post-default JSON values. They do not
claim that PC5 identity machinery exists or is accepted.

## Diagnostics

PC4 owns no semantic diagnostic code. Its accepted type boundary excludes PC3
root failures, while the erratum requires later-invalid declaration data to be
preserved. There is therefore no PC4 semantic-error precedence list.

PC4 must not emit or reinterpret parser, root-validation, declaration,
profile, resolution, reference, static-check, identity, qualification,
Binding, or runtime errors. It must never report partial expansion as success.

## Fixture contract

`conformance/pc4/default/fixture_manifest.json` is the controlling fixture set
for implementation intake. Every case supplies an exact input value and exact
post-default output. Boundary/deferred cases assert preservation and default
targeting only; they do not assert declaration validity.

An implementation test must run every case through the public PC4 boundary at
least three times, apply the transformation again to every expected output,
and prove exact JSON value equality, array-order preservation, and absence of
unlisted fields. Equivalence groups compare post-default values without
invoking PC5.

## Explicit non-ownership

PC4 does not parse YAML, repeat PC3 validation, validate declaration names or
forms, interpret unit kinds beyond exact default dispatch, validate contracts,
ports, links, routes, policies, controllers, resources, budgets, or secrets,
resolve packages, create a Lockfile, expand imports, normalize declarations,
perform static checking, canonicalize bytes, calculate identities, sort
collections, create or persist a Manifest, qualify, bind, execute, record,
replay, build, plan, call providers, or expose a UI, CLI, MCP, or Android
surface.

## Dependencies

No dependency is required or approved. The future implementation may use only
the accepted `serde_json::Value` representation and standard Rust operations
unless a separate dependency intake is authorized.
