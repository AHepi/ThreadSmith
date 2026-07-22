# PC3 Source-Validation Semantic Freeze

Freeze date: 2026-07-22.

Status: frozen for implementation intake; PC3 product code is not implemented or accepted.

## Boundary

```text
PC2 NFC-normalized JSON-shaped value
                    |
                    v
PC3 Source validate: Core root envelope only
                    |
                    v
non-authoritative ValidatedSource carrying the unchanged value
                    |
                    v
later Default phase
```

`ValidatedSource` is a conceptual boundary, not a frozen Rust API or schema type. Its representation may vary provided it cannot be constructed without the PC3 checks and exposes the unchanged PC2 value to the next phase.

## Input and preservation

PC3 receives one owned or borrowed `serde_json::Value` produced by accepted PC2. PC2 has established UTF-8 decoding, restricted-YAML syntax, signed-`i64` scalar projection, NFC normalization, string keys, duplicate and NFC-collision rejection, deterministic object ordering, and array-order preservation.

PC3 must not repeat YAML parsing, renormalize Unicode, reorder arrays, alter members, coerce scalar types, inject fields, or erase the distinction between absent and explicitly supplied values.

On success, the wrapped JSON value equals the PC3 input value. This is value equality, not a canonical-byte or identity claim.

## Root rules

### Permitted keys

```text
lattice
profile
module
version
purpose
imports
inputs
contracts
resources
units
links
policies
exports
scenarios
```

### Required keys

```text
lattice
profile
module
version
purpose
units
```

### Root value rules

| Key | PC3 rule |
|---|---|
| `lattice` | string exactly `0.3` |
| `profile` | string exactly `lattice-core-0.1` |
| `module` | string matching `^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$` |
| `version` | string matching `^[0-9]+\.[0-9]+\.[0-9]+$` |
| `purpose` | string; no additional content rule |
| all nine declaration keys | array when present |

PC3 validates no array element. An empty list, a list containing objects, or a list containing a value that will later fail declaration validation all have the same PC3 root shape.

## Defaults and normalization

PC3 applies no defaults:

- an omitted optional root list remains absent;
- an explicit empty root list remains present and empty;
- nested omitted and explicit values remain distinguishable;
- no mode, cardinality, predicate, repair, fallback, link, or scenario default is inserted.

All Standard section 16 defaults belong to the next `Default` phase. Declaration normalization and canonical collection ordering belong to later named phases. PC3 performs no identity-affecting transformation.

## Diagnostics

PC3 emits one primary diagnostic and makes no partial validated result available.

The stable surface is:

```text
code: stable string
path: RFC 6901 JSON Pointer; empty string denotes the root
```

PC3 cannot promise line or column positions because the accepted PC2 value boundary does not retain source locations. Message prose, if added, is non-normative and fixtures must not depend on it.

### Codes

| Code | Frozen PC3 meaning |
|---|---|
| `SOURCE_ROOT_TYPE` | PC2 output is not an object |
| `SOURCE_UNKNOWN_KEY` | A root member is outside the Standard section 10 allowlist |
| `SOURCE_REQUIRED_KEY_MISSING` | A required root member is absent |
| `SOURCE_INVALID_ROOT_VALUE` | A present root member violates its PC3 type, compatibility, local-name, or version-form rule |

The first, third, and fourth codes are additive ThreadSmith diagnostics. They do not reinterpret Foundation/PC1 or Standard Core codes. The Standard-reserved `SOURCE_DUPLICATE_NAME` and `PROFILE_UNSUPPORTED_UNIT_KIND` are not emitted by PC3.

### Deterministic precedence

The primary diagnostic is selected in this order:

1. root object type;
2. unknown root keys, selecting the smallest by ascending UTF-8 bytes;
3. missing required keys in `lattice`, `profile`, `module`, `version`, `purpose`, `units` order;
4. invalid present values in the full permitted-key order in `PC3_SCOPE_RECONCILIATION.md`.

Validation is side-effect free. Repeating it for the same value produces the same result, code, and path.

## Fail-closed behavior

Any PC3-owned failure prevents construction of `ValidatedSource` and entry to `Default`. Unknown root fields are never ignored. An unrecognized lattice version or profile is rejected rather than treated as Core.

Nested content is not silently approved: it is carried unchanged with no semantic status. Callers must not expose PC3 success as “Blueprint valid”, “compile succeeded”, “Manifest ready”, or any authority claim.

## Ordering

PC3 preserves all array order and does not sort declaration or nested arrays. It relies on PC2 deterministic object representation but uses explicit Standard order for validation precedence. Canonical collection sorting remains the later `Sort` phase.

## Compatibility

PC3 accepts only Standard `lattice: 0.3` with `profile: lattice-core-0.1`. No Extended profile or ThreadSmith-only root key is introduced. Future Standard/profile support requires a new semantic intake.

## Explicit non-ownership

PC3 does not validate declaration fields, declaration names, duplicates, imports, references, contracts, resources, ports, units, links, policy expressions, routes, controller graphs, budgets, secrets, completeness, qualification, or execution authority. It creates no Blueprint identity, Lockfile, Manifest, Binding, or runtime state.

## Dependencies

No dependency is required or approved. Existing `serde_json::Value` data and standard Rust operations are sufficient for the planned boundary. Any proposed dependency reopens dependency and licence intake before addition.
