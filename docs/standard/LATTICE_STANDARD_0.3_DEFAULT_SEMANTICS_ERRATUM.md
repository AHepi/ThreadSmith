# Lattice Standard 0.3 Default Semantics Erratum

Erratum date: 2026-07-22.

Status: normative companion to Lattice Standard 0.3.

## Authority and scope

This erratum resolves only ambiguities in sections 10, 15, 16, 20, 25, 26,
35, and 37 concerning the Standard `Default` phase. The recovered bytes of
`LATTICE_STANDARD_0.3.md` remain unchanged. Where this erratum defines an exact
default target or representation, it is controlling for Lattice Standard 0.3.
Every other Standard rule remains unchanged.

This erratum adds no declaration, unit kind, runtime behavior, authority
mechanism, compiler phase, or default value. It does not move parsing from
`Parse`, root-envelope validation from `Source validate`, declaration validity
from later normalization and static-check phases, or identity creation from
`Digest` and later identity phases.

## Default-phase boundary

The `Default` phase consumes one value that passed `Source validate` and emits
one JSON-shaped value containing the expanded source defaults. The output is
non-authoritative source data. The phase creates no digest, identity, Lockfile,
Manifest, Qualification Record, Run Binding, execution permission, or runtime
state.

The phase is a deterministic, idempotent transformation. It inserts members
only at the exact targets in this erratum and only when the target member is
absent. It never removes, replaces, coerces, validates, or infers a present
member.

## Exact root-list defaults

“Missing root list” means exactly these optional root members:

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

Each absent member is inserted as the JSON array `[]`. The required `units`
member is not defaulted. No other root member is defaulted.

## Exact input and output targets

Input defaults apply to each JSON object at either of these source locations:

```text
/inputs/*
/units/*/inputs/*
```

The exact inserted members and JSON values are:

| Member | JSON value |
|---|---|
| `required` | `true` |
| `cardinality` | `"one"` |
| `on_absence` | `"block"` |

Output defaults apply to each JSON object at either of these source locations:

```text
/exports/*
/units/*/outputs/*
```

The exact inserted member is `cardinality` with JSON value `"one"`.

No similarly named field elsewhere is an input or output default target.
Default expansion occurs before import expansion, so this phase does not
traverse package content or invented imported declarations.

## Exact unit and model targets

For each JSON object in `/units`, `kind` selects only the following
kind-dependent defaults:

| Exact `kind` string | Absent member | JSON value |
|---|---|---|
| `program` | `mode` | `"stateless"` |
| `model` | `mode` | `"stateless"` |
| `gate` | `mode` | `"stateless"` |
| `controller` | `mode` | `"event_sourced"` |
| `broker` | `mode` | `"external"` |
| `model` | `repair_attempts` | `0` |
| `model` | `fallback` | `false` |

The Standard phrase “Model fallback” therefore owns the source field
`/units/*/fallback` only when that unit's exact `kind` value is the string
`model`. Its canonical expanded value is the JSON boolean `false`.

This source field does not grant fallback authority and does not alter the Run
Binding rules in sections 24 and 34. A present source value, including `true`,
is preserved for later declaration validation and Binding reconciliation.

## Exact predicate targets and encoding

“Missing predicate” means exactly an absent `when` member on a JSON object at
either of these source locations:

```text
/links/*/when
/policies/*/when
```

The canonical expanded JSON value for constant `true` is:

```json
{"all":[]}
```

This uses the existing Core `all` operator and its existing rule that `all`
over an empty list is true. Controller transition `on` members and every other
field are not predicate-default targets.

## Exact link and scenario targets

For each JSON object in `/links`, these absent members are inserted:

| Member | JSON value |
|---|---|
| `mode` | `"data"` |
| `delivery` | `"multicast"` |
| `when` | `{"all":[]}` |

For each JSON object in `/scenarios`, an absent `required` member is inserted
with JSON value `true`.

For each JSON object in `/policies`, only the absent `when` member defined
above is inserted. No policy decision or permission is defaulted by source
expansion; deny-by-default policy evaluation remains a later concern.

## Present, invalid, and ambiguous data

Presence is determined only by JSON object membership. A present member always
wins over its default, even when its value is `null`, empty, the wrong JSON
type, unsupported, contradictory, or later invalid. Such a member is preserved
value-for-value and receives no replacement default.

Declaration elements that are not JSON objects remain unchanged. A nested
`inputs` or `outputs` member that is not an array remains unchanged and is not
traversed. A nested port-array element that is not an object remains unchanged.

When a unit's `kind` member is absent, is not a string, or is not one of the
five Core kind strings above, no kind-dependent `mode`, `repair_attempts`, or
`fallback` default is inserted. Context-independent input and output defaults
still apply when that unit has traversable `inputs` or `outputs` arrays.

No Default-phase diagnostic is produced for these cases. The data remains
available unchanged, apart from other unambiguous insertions at exact targets,
for the later declaration-normalization, profile, reference, and static-check
phases. Default expansion never makes malformed or ambiguous source valid.

## Deterministic application algorithm

For one Source-validated root object, a conforming compiler performs these
steps in order:

1. Insert the eight absent optional root lists in the order stated above.
2. Visit root `inputs`, then root `exports`, in array order and apply their
   exact port defaults to object elements.
3. Visit `units` in array order. For each object, apply its exact
   kind-dependent defaults, then visit its `inputs` and `outputs` arrays in
   array order and apply port defaults to object elements.
4. Visit `links`, `policies`, and `scenarios`, in that order and in each
   array's existing order, and apply their exact defaults to object elements.

The algorithm does not recursively search arbitrary objects for matching field
names. Object-member ordering has no semantic effect and is handled by the
existing canonical-JSON rules after defined defaults. Array order is never
changed.

Applying the algorithm twice produces a JSON value equal to applying it once.
Compilers may use a different internal traversal only when it produces exactly
the same JSON-shaped value for every Source-validated input.

## Canonical representation and identity

The expanded source representation contains the inserted fields and exact JSON
values defined above. It contains no default-provenance member, sidecar marker,
implicit sentinel, implementation metadata, or convenience field.

An omitted defaulted member and the same explicitly supplied default value
therefore produce equal expanded source values. Explicit non-default values
remain distinct. Absence remains distinguishable from presence only for fields
that have no Standard default or are not unambiguous targets under this
erratum.

Defaults participate in identity preimages exactly as already required by
sections 15 and 16. The root Blueprint used for `blueprint_digest` is the
post-default value, before import expansion. Every later declaration identity
uses the applicable expanded default values before declaration hashing. PC4
produces the preimage value but does not calculate an identity.

## Required conformance fixtures

Any PC4 semantic freeze and implementation claiming this erratum MUST include
exact input and output fixtures covering at least these cases:

| Fixture class | Required proof |
|---|---|
| Minimal root | All eight and only eight optional root lists are inserted. |
| Root ports | Root inputs receive all three input defaults; exports receive only output cardinality. |
| Unit ports | Unit inputs and outputs receive the same respective port defaults. |
| Unit kinds | Every Core kind receives exactly its mode; only model receives repair and fallback defaults. |
| Predicates | Missing link and policy `when` become exactly `{"all":[]}`; controller transitions do not. |
| Link and scenario | Link mode/delivery and scenario required values are exact. |
| Explicit values | Explicit default, non-default, empty, `null`, wrong-type, and contradictory values are preserved. |
| Already expanded | A completely default-expanded source is unchanged. |
| Repeated application | One and multiple applications produce equal output. |
| Non-object elements | Non-object declaration and port elements remain unchanged. |
| Invalid containers | Non-array nested input/output containers remain unchanged and untraversed. |
| Ambiguous unit kind | Missing, non-string, and unknown kinds receive no kind-dependent defaults. |
| No convenience defaults | Fields not listed by this erratum remain absent. |
| Identity equivalence | Omitted and explicitly supplied default values produce equal post-default identity preimages. |
| Identity distinction | Explicit non-default values produce distinct post-default identity preimages. |

Fixtures for malformed or later-invalid declarations prove only Default-phase
preservation and deferral. They MUST NOT describe those declarations as valid,
compiled, identified, qualified, bound, or executable.

## Preserved boundaries

PC2 remains restricted-YAML parsing into an NFC-normalized JSON-shaped value.
PC3 remains Core root-envelope validation over the unchanged PC2 value. PC4
owns only the transformation specified here. Declaration validation, profile
checks, package resolution, Lockfiles, import expansion, normalization, static
checking, identities, Manifests, qualification, Binding, runtime, replay,
builder behavior, providers, and user surfaces remain outside this erratum.
