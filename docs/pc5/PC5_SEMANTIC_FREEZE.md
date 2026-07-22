# PC5 Blueprint-Digest Semantic Freeze

Freeze date: 2026-07-22.

Status: frozen for implementation intake; PC5 product code is not implemented
or accepted.

## Boundary

```text
PC4 DefaultedSource
        |
        v
PC5 Digest: canonical JSON plus SHA-256
        |
        v
non-authoritative DigestedSource
        |
        v
Package scan
```

PC5 consumes only the accepted opaque `DefaultedSource`. A public PC5 entry
point that accepts arbitrary `serde_json::Value`, YAML bytes, `ValidatedSource`,
or a caller-supplied digest is non-conforming.

## Blueprint preimage

For an input `source`, define:

```text
root = the complete JSON-shaped value contained by source
canonical_bytes = canonical_json(root)
hash = SHA-256(canonical_bytes)
blueprint_digest = "lattice:blueprint:sha256:" + lowercase_hex(hash)
```

The preimage is exactly `canonical_bytes`. The `DefaultedSource` wrapper is not
encoded. PC5 does not add a field, remove a field, correct a field, apply a
default, normalize a declaration, sort an array, resolve an import, validate a
name, or attach source or compiler metadata.

Every root member and nested value in the accepted PC4 output participates,
including later-invalid values. Array order is preserved and participates.

## Exact canonical bytes

`docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md` is controlling.
For PC5, its requirements mean:

```text
UTF-8
no byte-order mark
no insignificant whitespace
no leading or trailing whitespace
no trailing newline
object keys ordered by ascending normalized UTF-8 bytes
array order unchanged
signed i64 integers in minimal base ten
true, false, and null in lowercase
NFC strings
non-ASCII scalars emitted directly as UTF-8
```

Object-key comparison occurs before string escaping. Canonical JSON performs
no collection-level semantic sort.

### Exact string escapes

Inside an NFC JSON string or object key:

| Input scalar | Canonical encoding |
|---|---|
| `U+0022` quotation mark | `\"` |
| `U+005C` reverse solidus | `\\` |
| `U+0008` backspace | `\b` |
| `U+0009` tab | `\t` |
| `U+000A` line feed | `\n` |
| `U+000C` form feed | `\f` |
| `U+000D` carriage return | `\r` |
| every other `U+0000..U+001F` | `\u00xx` with lowercase hexadecimal |
| `U+002F` solidus | `/` |
| every other Unicode scalar | direct UTF-8 |

No alternative spelling is permitted. `U+007F`, `U+0085`, `U+2028`,
`U+2029`, non-ASCII BMP scalars, and supplementary scalars are direct UTF-8.
Supplementary scalars are not rendered as UTF-16 surrogate-pair escapes.

The accepted PC2-to-PC4 path guarantees Unicode scalar strings, NFC, signed
`i64` numbers, and collision-free object keys. Consequently the PC5 operation
is semantically total. An unpaired surrogate or normalized-key collision would
be an unreachable internal invariant violation rather than a PC5 source error.

## Identity type

`BlueprintDigest` represents exactly one native identity whose kind is
`blueprint` and whose digest bytes are the SHA-256 result above. Its external
text is exactly:

```text
lattice:blueprint:sha256:<64 lowercase hexadecimal characters>
```

It must preserve the accepted PC1 `NativeLatticeId` representation and
non-authority meaning. The initial PC5 surface does not expose a public
constructor that lets a caller label arbitrary bytes as the result of
`digest_source`. Formatting, comparison, serialization of the textual claim,
and read-only access are permitted implementation details provided they do not
create a second identity meaning.

An existing caller-constructed or parsed PC1 `NativeLatticeId` of Blueprint
kind remains a generic claim. It is not a `BlueprintDigest`, does not prove
that PC5 ran, and cannot be promoted into `DigestedSource` through the public
PC5 API.

## Bound output

The semantic output is:

```rust
pub struct DigestedSource {
    defaulted_source: DefaultedSource,
    blueprint_digest: BlueprintDigest,
}
```

The fields are private. Only:

```rust
fn digest_source(source: DefaultedSource) -> DigestedSource
```

constructs the wrapper. The operation consumes `source`, preserves it exactly,
and calculates the contained digest from that same value. Public API design may
expose immutable borrows, textual formatting, and consuming access that cannot
construct or mutate a mismatched `DigestedSource`. It may not expose a public
`DigestedSource::new(source, digest)`, mutable field access, digest replacement,
or source replacement.

Public deserialization of caller-supplied source and digest fields into
`DigestedSource` is also forbidden because it would bypass the binding
operation.

The canonical byte stream is transient calculation state. It is not a field of
`DigestedSource`, not part of the Blueprint preimage, and not added as a new
PC5-specific public API. Golden-byte tests inspect the encoding through the
canonical implementation test boundary.

## Totality and diagnostics

The conceptual public signature has no source-error result:

```rust
fn digest_source(source: DefaultedSource) -> DigestedSource
```

PC5 emits no `SourceDiagnostic` and owns no Standard static error. It must not
reject or diagnose:

```text
duplicate declaration names
invalid or Extended-only unit kinds
malformed declaration bodies
unknown references
wrong-type explicit values
unresolved imports
unsupported later semantics
resource or package failures
```

An internal encoding or hashing failure over an accepted `DefaultedSource` is a
compiler defect, not a user-source diagnostic and not partial PC5 success.

## Equivalence rules

Equal `DefaultedSource` values produce byte-identical canonical preimages and
equal `BlueprintDigest` values. Therefore all of these source-presentation
differences converge when PC2 through PC4 produce the same value:

```text
omitted versus explicitly equal Standard defaults
YAML root-key order
permitted YAML quoting style
comments and indentation
equivalent YAML scalar spellings
canonically equivalent Unicode normalized by PC2
source path and file metadata
```

Repeated digestion of equal `DefaultedSource` values produces the same digest.
Process, platform, compiler, map insertion order, and cache state do not enter
the preimage.

## Distinction rules

Different values remain different canonical preimages. Exact fixtures bind
distinctions for:

```text
module
version
purpose
explicit non-default values
array order
explicit null versus an omitted defaulted member
explicit empty versus explicit non-empty arrays
```

The root `profile` value is also encoded without exclusion. Current PC3 admits
only `lattice-core-0.1`, so an alternate root profile is not a constructible
PC5 input. The fixture contract proves both the canonical-preimage distinction
and PC3 rejection, rather than bypassing the opaque phase boundary.

PC5 does not decide whether two later normalized Manifests could converge. The
Blueprint digest identifies the post-default source representation, including
its preserved arrays.

## Invalid but digestible source

Later-invalid content inside a valid root envelope remains digestible. The
digest identifies exactly what failed later. It does not imply acceptance,
resolution, normalization, static validity, qualification, or execution
authority.

`SOURCE_DUPLICATE_NAME` is explicitly not a pre-digest condition. Its exact
later lifecycle owner must be frozen in a later scope intake without moving the
check backward into PC2, PC3, PC4, or PC5.

## Fixture contract

`conformance/pc5/digest/fixture_manifest.json` is the controlling PC5 fixture
contract. It contains:

- exact canonical UTF-8 byte hex and SHA-256 vectors;
- public PC2-to-PC5 source equivalence cases;
- exact digest-distinction cases;
- a profile participation vector plus a PC3 rejection case;
- later-invalid but publicly digestible sources; and
- output-binding and non-authority requirements.

The byte hex is normative and avoids ambiguity when a golden byte is a control
or non-ASCII value. A readable canonical string, where present, is explanatory;
the decoded byte hex and SHA-256 are controlling.

Implementation tests must independently decode every byte vector, verify its
SHA-256, exercise every reachable source case through the public
PC2-to-PC3-to-PC4-to-PC5 path, and compare exact digest text. Tests may use an
internal canonical test seam but may not add canonical bytes to the public PC5
output.

## Deferred identities and authority

PC5 creates no identity except `BlueprintDigest`. It creates no package,
resource, contract, unit, link, policy, scenario, Lockfile, Manifest,
qualification, Binding, envelope, event, activation, or runtime identity.

`BlueprintDigest` and `DigestedSource` grant no execution permission. They do
not permit provider construction, package installation, filesystem or network
access, qualification, Binding, runtime state, Builder action, CLI, MCP, UI,
or Android behavior.

## Acceptance invariant

PC5 conforms only when:

> Two independent conforming implementations receiving the same
> `DefaultedSource` produce byte-identical canonical preimage bytes and the
> same Blueprint digest, without resolving packages, validating declaration
> bodies, creating later identities, creating a Lockfile or Manifest, or
> granting execution authority.

## Dependencies and implementation status

This freeze adds no Rust dependency and authorizes no production edit. A later
PC5 implementation tranche must explicitly intake the existing
`threadsmith-canonical` and `threadsmith-schema` path dependencies into
`threadsmith-compiler`, qualify any required canonical-encoder repair against
the new erratum vectors, and keep the external dependency graph pinned and
offline. That future sequence is not implementation authority in this freeze.
