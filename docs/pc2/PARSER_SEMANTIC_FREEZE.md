# PC2 Standard-Aligned Parser Semantic Freeze

Status: reconciled and frozen against Lattice Standard 0.3 on 2026-07-22.

The controlling source is `docs/standard/LATTICE_STANDARD_0.3.md`, SHA-256 `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379`. This freeze supersedes the original PC2 parser freeze where the two differ. It does not alter Foundation or PC1 identity and authority boundaries.

## Lifecycle boundary

```text
UTF-8 YAML source
        |
        v
PC2 restricted YAML parse and JSON projection
        |
        v
NFC-normalized JSON-shaped value tree
        |
        v
PC3 Source validate (not implemented here)
```

`threadsmith-compiler` owns parsing. `threadsmith-schema` continues to own schemas and data structures only.

PC2 returns parsed data. It does not establish that the root is a Blueprint, validate root keys or declarations, apply source defaults, enforce a profile, create a digest or identity, scan or resolve packages, create a Lockfile or Manifest, qualify, bind, compile, or execute.

The public boundary remains:

```rust
parse_blueprint_source(&[u8]) -> Result<serde_json::Value, SourceDiagnostic>
```

The function name is retained for API continuity. A successful return is not a validated Blueprint.

## Source encoding and document form

- Input is UTF-8 without a BOM.
- LF, CRLF, and CR line endings are accepted and normalized to LF before YAML parsing.
- Raw C0 characters outside YAML 1.2's permitted input character set are rejected. Non-C0 characters remain permitted inside quoted scalars, including NEL (`U+0085`) as a non-break character.
- Exactly one YAML document is accepted.
- A bare document or explicit `---` and `...` markers are accepted.
- An optional `%YAML 1.2` directive is accepted. Other version directives, repeated YAML directives, and tag directives are rejected.
- Comments are discarded.

## Restricted YAML 1.2 surface

Block and flow mappings and sequences are accepted. Plain, single-quoted, double-quoted, and literal `|` scalars are accepted. Folded `>` scalars are rejected.

Anchors, aliases, merge keys, custom tags, multiple documents, floating-point values, binary-tagged values, and non-string mapping keys are rejected. YAML core tags `!!str`, `!!null`, `!!bool`, `!!int`, `!!seq`, and `!!map` are accepted only on the matching node kind and construct the named JSON category; other or mismatched tags are rejected. Tabs used as indentation are rejected by YAML parsing. Explicit-key syntax is permitted when the key resolves to a string; collection keys and scalar keys resolving to null, boolean, or integer are not string keys and are rejected.

## Scalar construction

Without an explicit YAML core tag, quoted and literal scalars are strings. Plain scalars use the YAML 1.2 Core resolution order, restricted to the Standard's JSON-shaped types:

| Plain form | Output |
|---|---|
| Empty, `null`, `Null`, `NULL`, `~` | JSON null |
| YAML 1.2 Core boolean forms | JSON boolean |
| YAML 1.2 Core decimal, `0o` octal, or `0x` hexadecimal integer | JSON integer when its resolved value fits signed `i64` |
| YAML 1.2 Core floating-point form | `SOURCE_INVALID_SCALAR` |
| Any other plain scalar | String |

Integer spelling is presentation only. `-0`, leading-zero decimal forms, a leading `+`, octal, and hexadecimal forms resolve to one signed integer value. Values outside `-9223372036854775808..=9223372036854775807` are rejected. Date- and timestamp-looking plain scalars remain strings because this profile does not resolve a timestamp type.

Valid YAML 1.2 escapes in double-quoted strings are decoded and preserved as JSON string content, including escaped C0, DEL, C1, NEL, and non-breaking-space values. The raw source character restrictions do not become a second decoded-value restriction.

## Unicode, keys, and ordering

Every string value and mapping key is normalized to Unicode NFC after YAML escape and scalar processing.

Within each mapping:

1. a repeated decoded pre-NFC string key is `SOURCE_DUPLICATE_KEY`;
2. two distinct decoded keys with the same NFC form are `SOURCE_NFC_COLLISION`.

These checks apply at every depth. Arrays preserve source order. Object source order is not semantic; normalized object entries are sorted by ascending UTF-8 key bytes before insertion into the returned `serde_json::Value`, independent of `serde_json` map features. Comments, scalar spelling, and mapping presentation order do not create authority or identity.

## Information preservation

PC2 performs no default insertion. Therefore:

- an absent field remains absent;
- an explicitly empty list remains present as `[]`;
- an explicitly supplied value remains present as parsed;
- unknown root keys and missing required root keys are preserved for PC3;
- unsupported unit kinds and declaration-shape defects are preserved for later validation.

The PC2 tree intentionally retains the distinction required by the Standard's later `Source validate` and `Default` phases.

## Deterministic diagnostics

The stable diagnostic contains only `code`, RFC 6901 `path`, and optional one-based `line` and `column`. Upstream dependency prose is not stable API.

Parser-level precedence is:

1. UTF-8 and forbidden source-character checks;
2. directive, YAML syntax, document-count, and forbidden-feature checks;
3. scalar-category, signed-range, and key-category checks;
4. duplicate-key and NFC-collision checks during source traversal.

| Code | Meaning |
|---|---|
| `SOURCE_INVALID_UTF8` | Input is not permitted UTF-8 source. |
| `SOURCE_FORBIDDEN_YAML` | Syntax or a YAML feature lies outside the restricted profile. |
| `SOURCE_INVALID_SCALAR` | A float or out-of-range integer was encountered. |
| `SOURCE_NON_STRING_KEY` | A mapping key resolves to a non-string JSON category. |
| `SOURCE_DUPLICATE_KEY` | One decoded string key occurs twice in a mapping. |
| `SOURCE_NFC_COLLISION` | Distinct decoded keys normalize to the same NFC key. |

Root and declaration diagnostic codes belong to PC3 or later phases and are not emitted by PC2.

## Dependency boundary

The accepted parser dependency remains exactly `saphyr-parser =0.0.11` with default features disabled and the existing locked graph. Reconciliation adds no dependency and does not change licence, native-code, system-libyaml, Python, FFI, offline, or reproducibility findings from the accepted intake.

## Explicit non-goals

PC3 Source validation, source defaults, Blueprint identity, Manifest identity, artifact hashes, package scanning or resolution, Lockfile generation, import expansion, normalization, gate insertion, static checking, declaration identity, Manifest generation, persistence, qualification, Binding, runtime, builder, planner, providers, package storage, UI, CLI, MCP, Android, and release work are outside this freeze.
