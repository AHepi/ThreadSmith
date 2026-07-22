# PC2 Parser Semantic Freeze

Status: frozen for PC2 parser implementation on 2026-07-22.

This is a new PC2 source-language freeze derived from the accepted Foundation/PC1 model. It is not a recovered historical grammar and does not alter Foundation identities, canonical bytes, or Blueprint/Manifest authority boundaries.

## Boundary and ownership

| Boundary | Frozen rule |
|---|---|
| Input | One UTF-8 YAML source document |
| Output | One JSON-shaped value tree whose strings and object keys are NFC-normalized |
| Owner | Future `threadsmith-compiler` source parser |
| Schema crate | `threadsmith-schema` continues to own schemas and data structures only |
| Identity and authority | The parser creates no identity, digest, Manifest, package resolution, qualification, Binding, execution authority, or executable artifact |

The parser is a source projection and structural validation boundary. Compilation begins only after this boundary returns a valid tree. The parser output is not a Blueprint identity preimage and is not authoritative by itself.

## Accepted YAML subset

The source is decoded strictly as UTF-8. A UTF-8 BOM, NUL, bare carriage return, and disallowed Unicode control character are rejected. LF and CRLF line endings are accepted. Exactly one implicit document is accepted; YAML directives, explicit `---` or `...` document markers, and additional documents are forbidden.

Block and flow mappings and sequences are accepted. Comments are accepted and discarded. Plain, single-quoted, and double-quoted scalars are accepted. Literal and folded block scalars are forbidden. Mapping keys must be simple scalar strings; explicit complex keys and collection keys are forbidden.

Anchors, aliases, explicit tags, tag directives, merge keys, and any node carrying anchor or tag metadata are forbidden even when the dependency could parse them. The dependency's accepted language is therefore a strict superset of ThreadSmith source.

## Scalar interpretation

Quoted scalars are always strings. Plain scalars are interpreted by this exact, case-sensitive order:

| Form | Output |
|---|---|
| `null` | JSON null |
| `true` | JSON boolean true |
| `false` | JSON boolean false |
| `0`, or an optional `-` followed by a non-zero decimal digit and then decimal digits | JSON integer if representable as signed `i64` or non-negative `u64` |
| Any other plain scalar not reserved below | String |

Empty implicit scalar values are forbidden; null must be written as `null`. Floats, decimal points, exponents, `.inf`, `.nan`, hexadecimal, octal, leading `+`, numeric underscores, and decimal integers with a leading zero are invalid scalar categories when unquoted. They may be represented only as quoted strings. YAML 1.1 words such as `yes`, `no`, `on`, and `off` are strings. Timestamp-looking plain text is a string because no timestamp tag is permitted.

Mapping keys must resolve to strings before NFC normalization. Null, boolean, integer, sequence, and mapping keys are rejected. All strings must exclude NUL and disallowed control characters after escape processing.

## Unicode, keys, and ordering

Every string value and mapping key is normalized to Unicode NFC after YAML quote and escape processing and before root validation or default injection. Arrays preserve source order exactly. Mapping source order is used only for deterministic validation; object member order is not semantic and consumers must not infer authority or identity from it.

Each mapping tracks decoded pre-NFC keys and normalized keys. A repeated decoded key is `SOURCE_DUPLICATE_KEY`. Two distinct decoded keys that normalize to the same NFC key are `SOURCE_NFC_COLLISION`. Detection applies at every mapping depth and occurs before unknown-key validation. Values that normalize to equal strings are allowed.

## Blueprint root envelope

The root must be a mapping with exactly these permitted keys after NFC normalization:

| Key | Presence | Parser shape |
|---|---|---|
| `profile` | Required | Non-empty string exactly `lattice-core-0.1` |
| `module` | Required | Non-empty string |
| `version` | Required | Non-empty string |
| `purpose` | Required | Non-empty string |
| `imports` | Optional | Sequence; defaults to `[]` |
| `resources` | Optional | Sequence; defaults to `[]` |
| `contracts` | Optional | Sequence; defaults to `[]` |
| `units` | Optional | Sequence; defaults to `[]` |
| `links` | Optional | Sequence; defaults to `[]` |
| `policies` | Optional | Sequence; defaults to `[]` |
| `scenarios` | Optional | Sequence; defaults to `[]` |

No other root key is accepted. A source `defaults` root is specifically rejected as `SOURCE_ILLEGAL_DEFAULT_OVERRIDE`; PC1 defaults are profile-owned and cannot be replaced by source text. Missing optional lists are injected only after the document has otherwise validated. Explicit `null` is not an empty-list default.

Empty-list injection is a parser shape rule, not a compiler acceptance rule. In particular, an injected or explicit empty `scenarios` list does not satisfy the accepted PC1 `scenario_required=true` semantic; the later compiler tranche must enforce that rule. A fixture called a valid Blueprint is valid only at this parser boundary.

The parser performs one PC1 profile gate required by its source boundary: when an item in `units` has a string `kind`, the accepted values are `program`, `model`, `gate`, `controller`, and `broker`. `adapter`, `store`, `subharness`, and any other value are `PROFILE_UNSUPPORTED_UNIT_KIND`. The parser does not validate unit wiring, contracts, policy meaning, routes, names, packages, or execution completeness; those are later compiler concerns.

## Deterministic diagnostics

Parsing stops at the first diagnostic. The normative diagnostic value contains only `code`, RFC 6901 `path`, and a one-based `line` and `column`; missing-token diagnostics use null positions. Human prose and upstream dependency messages are non-normative and must not be exposed as stable API fields.

Validation order is fixed:

1. UTF-8 and source-character checks.
2. YAML syntax and forbidden-feature checks in source event order.
3. Scalar, key-category, duplicate-key, and NFC-collision checks in source traversal order.
4. Root mapping check.
5. Illegal `defaults`, then unknown root keys in source order.
6. Missing required keys in `profile`, `module`, `version`, `purpose` order.
7. Root value shapes and exact profile value in the permitted-key table order.
8. Unit-kind profile checks in array order.
9. Optional-list default injection.

| Code | Meaning |
|---|---|
| `SOURCE_INVALID_UTF8` | Input is not strict UTF-8 or contains a forbidden source character. |
| `SOURCE_FORBIDDEN_YAML` | A forbidden YAML feature or YAML syntax outside the accepted subset was encountered. |
| `SOURCE_INVALID_SCALAR` | A scalar uses a forbidden category or cannot fit the frozen integer range. |
| `SOURCE_NON_STRING_KEY` | A mapping key does not resolve to a string. |
| `SOURCE_DUPLICATE_KEY` | The same decoded key occurs twice in one mapping. |
| `SOURCE_NFC_COLLISION` | Distinct decoded keys normalize to the same NFC key. |
| `SOURCE_ROOT_TYPE` | The document root is not a mapping. |
| `SOURCE_ILLEGAL_DEFAULT_OVERRIDE` | Source attempts to declare the profile-owned `defaults` root. |
| `SOURCE_UNKNOWN_KEY` | A normalized root key is not permitted. |
| `SOURCE_REQUIRED_KEY_MISSING` | A required root key is absent. |
| `SOURCE_INVALID_ROOT_VALUE` | A root value has the wrong JSON shape, is empty where forbidden, or carries a wrong profile value. |
| `PROFILE_UNSUPPORTED_UNIT_KIND` | A unit kind is outside the PC1 portable-core set. |

## Explicit non-goals

This freeze does not define Blueprint identity, Manifest identity, artifact hashes, canonical identity preimages, package resolution, qualification, Binding, compiler output, runtime behavior, event/replay behavior, builder behavior, planning, providers, model management, package storage, desktop, CLI, MCP, Android, or release behavior. It adds no product code and cannot make `PC2_ACCEPTED` true.
