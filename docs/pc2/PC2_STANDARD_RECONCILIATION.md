# PC2 Standard Reconciliation Report

Reconciliation date: 2026-07-22.

## Controlling evidence

| Evidence | Role | SHA-256 |
|---|---|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | Controlling normative specification | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| `docs/pc2/PARSER_SEMANTIC_FREEZE.md` at baseline `d49017e` | Superseded PC2 freeze | `040bc580f2e37a0a2547a89d9e56ad43c1c43671bb6c8019e726418bd14eb2ee` |
| `crates/threadsmith-compiler/src/lib.rs` at baseline `d49017e` | Accepted incompatible implementation | `5a3b17d18171c6f70ab4337c7db05f07d222d82645701b80379eb270489feab3` |
| `crates/threadsmith-compiler/tests/pc2_parser.rs` at baseline `d49017e` | Accepted incompatible tests | `79047f5d54d3b8e341c70803e81cb52481b60d53e01c50a9aa72202e5af3e323` |

The recovered Standard bytes are preserved exactly. The supplied recovered `PROJECT_STATE(1).md` is historical Foundation evidence and does not describe the published Rust PC2 tree. The supplied directive and the tracked directive are both empty with SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

## Lifecycle reconciliation

Lattice Standard 0.3 defines distinct phases:

```text
Read -> Parse -> Source validate -> Default -> Digest -> Package scan ->
Resolve -> Lock -> Expand -> Normalize -> Insert -> Static check ->
Identify -> Sort -> Manifest -> Persist
```

PC2 owns only `Parse`. The accepted PC2 implementation had absorbed pieces of `Source validate`, `Default`, and profile checking. This reconciliation removes those later-phase behaviors rather than assigning them a new meaning.

## Deviations and corrections

| Accepted PC2 behavior | Standard classification | Required correction | Compatibility impact |
|---|---|---|---|
| Rejected a non-mapping root. | `Source validate`: valid root shape. | Return any restricted-YAML JSON-shaped root; PC3 decides whether it is a Blueprint mapping. | Inputs such as sequences now parse successfully but remain unvalidated. |
| Permitted only 11 ThreadSmith root keys and rejected `lattice`, `inputs`, and `exports`. | `Source validate`: permitted Blueprint keys. | Remove root-key validation from PC2; Standard keys and unknown keys survive parsing. | Prior `SOURCE_UNKNOWN_KEY` results move to PC3. |
| Required only `profile`, `module`, `version`, and `purpose`; Standard also requires `lattice` and `units`. | `Source validate`: required keys. | Remove required-key checks from PC2. | Missing fields now remain absent and must be rejected by PC3. |
| Validated root value shapes and the exact profile. | `Source validate` and later profile validation. | Remove root-value and profile checks from PC2. | These diagnostics move to later phases. |
| Injected seven optional empty lists and erased absent-versus-explicit state. | Separate `Default` phase. | Perform no insertion; preserve object membership exactly. | Successful output trees change; downstream callers must not depend on injected lists. |
| Rejected a source `defaults` key with a PC2-only diagnostic. | Root-key validation, then Standard-defined `Default`; source has no authority to redefine compiler defaults. | Preserve the key in PC2; PC3 later rejects it as an unknown root key. | `SOURCE_ILLEGAL_DEFAULT_OVERRIDE` is retired from PC2. |
| Rejected Extended-only and unknown unit kinds while parsing. | Profile/static validation after parse. | Preserve unit declarations without interpreting `kind`. | `PROFILE_UNSUPPORTED_UNIT_KIND` moves to a later compiler phase. |
| Rejected literal `|` and folded `>` block strings. | Standard permits literal strings and forbids folded strings. | Accept literal strings; continue rejecting folded strings. | Previously rejected Standard source now parses. |
| Rejected explicit document markers and every directive. | Parse/presentation syntax; Standard forbids multiple documents, not a single marked document. | Accept a single bare or marked document and optional `%YAML 1.2`; reject multiple documents, other versions, and tag directives. | Previously rejected equivalent presentations now parse identically. |
| Rejected explicit scalar-key syntax. | Parser concern: only non-string mapping keys are forbidden. | Accept explicit keys that resolve to strings; reject collection and non-string scalar keys. | Standard string-key syntax is restored. |
| Rejected every explicit tag, including deterministic YAML core tags. | Parser concern: the Standard forbids custom tags and non-JSON categories, not the core tags for permitted JSON categories. | Honor matching `!!str`, `!!null`, `!!bool`, `!!int`, `!!seq`, and `!!map`; reject custom, forbidden-category, and mismatched tags. | Standard-tagged JSON values now parse without permitting custom semantics. |
| Accepted positive integers through `u64`. | Parser scalar construction: signed 64-bit integer only. | Bound every resolved integer to `i64`. | Values `9223372036854775808..=18446744073709551615` now fail. |
| Used a custom lowercase decimal-only scalar resolver and rejected empty nulls, Core case forms, signs, octal, hexadecimal, and leading-zero decimal forms. | Restricted YAML 1.2 scalar construction. | Use YAML 1.2 Core resolution, remove floats, and bind integers to `i64`. | Standard-equivalent scalar spellings now produce the same JSON category and value. |
| Treated date-looking plain text as a string. | Core resolution has no timestamp type; the Standard forbids implicit date typing. | Preserve behavior. | No compatibility change. |
| Rejected anchors, aliases, merge keys, custom tags, floats, non-string keys, duplicate keys, NFC collisions, multiple documents, BOM, and forbidden controls. | Parser concern explicitly constrained by the Standard. | Preserve and expand focused coverage. | Supported fail-closed behavior remains. |
| NFC-normalized keys/strings and preserved array order. | Parser output boundary and canonical-data preparation. | Preserve. | No compatibility change. |
| Accepted LF/CRLF but rejected bare CR instead of normalizing every YAML line break. | Source encoding: line endings normalize to LF. | Normalize LF, CRLF, and CR before parsing. | Equivalent line-ending presentations now project identically. |

## Public API and ownership

The existing public Rust signature remains unchanged. Its semantic contract is corrected from “parser plus shallow Blueprint validation and defaults” to “parser only.” `threadsmith-compiler` remains the owner. No parsing behavior moves to `threadsmith-schema`.

This is intentionally a breaking semantic correction for callers that treated a PC2 success as source validation or relied on injected lists. Retaining those behaviors would create a ThreadSmith-only language and prevent the Standard lifecycle from being implemented faithfully.

## Dependency and licensing impact

No parser dependency change is required. `saphyr-parser =0.0.11`, default features disabled, is sufficient through its event API. The lockfile, resolved graph, licences, offline-cache requirement, build scripts, Rust `unsafe` inventory, native/FFI finding, and system-libyaml exclusion remain exactly as recorded by the accepted intake.

## Acceptance criteria

PC2 reconciliation is acceptable only when:

1. the recovered Standard hash matches the tracked copy;
2. the public parser performs no root, declaration, profile, or default-phase behavior;
3. absent and explicitly empty members remain distinguishable;
4. Standard-permitted syntax and signed scalar behavior pass focused fixtures;
5. forbidden YAML, duplicate keys, and NFC collisions remain deterministic and fail closed;
6. Foundation and PC1 regressions pass unchanged;
7. the dependency graph and lockfile remain unchanged;
8. a separate read-only review finds no open P0 or P1 defect;
9. no PC3 or later compiler behavior is implemented.
