# PC5 Digest-Phase Scope Reconciliation

Reconciliation date: 2026-07-22.

## Controlling evidence

| Evidence | Role |
|---|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | Controlling lifecycle, canonical-data, Blueprint-preimage, identity-format, and authority rules; recovered SHA-256 `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| `docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md` | Controlling post-default source representation and identity-preimage participation |
| `docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md` | Controlling exact canonical JSON byte encoding where the original Standard allowed multiple valid JSON escape spellings |
| `docs/pc2/PC2_STANDARD_RECONCILIATION.md`, `docs/pc2/PARSER_SEMANTIC_FREEZE.md`, and `docs/compliance/PORTABLE_CORE_PRE_PC4_COMPLIANCE.md` | Accepted restricted-YAML projection, NFC string preservation, signed-`i64` domain, and decoded-control boundary |
| `docs/pc3/PC3_SCOPE_RECONCILIATION.md` and `docs/pc3/PC3_SEMANTIC_FREEZE.md` | Accepted Core root envelope, exact profile selector, unchanged-value, and deferred-declaration boundary |
| `docs/pc4/PC4_SCOPE_RECONCILIATION.md` and `docs/pc4/PC4_SEMANTIC_FREEZE.md` | Accepted `DefaultedSource` payload, explicit-value preservation, order, and non-authority boundary |
| `crates/threadsmith-compiler/src/lib.rs` and `tests/pc4_default.rs` | Accepted public PC2-to-PC4 path and private `DefaultedSource` construction boundary |
| `crates/threadsmith-canonical/src/lib.rs`, `crates/threadsmith-schema/src/lib.rs`, and Foundation/PC1 conformance vectors | Existing single-core canonical machinery, generic typed identity vocabulary, and frozen non-authority meanings |
| `docs/adr/0001-portable-core-language.md` | Accepted rule that Rust owns canonical serialization and identity calculation once the Standard preimage is resolved |
| `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md` | Current state, bounded sequence, and durable decisions |

Foundation and PC1 remain controlling for generic canonical claims, typed
identity representation, native/legacy separation, migration, and authority.
PC5 resolves only the Standard-defined Blueprint preimage that PC1 correctly
left unresolved before the Standard was recovered. It does not resolve the
Manifest preimage or reinterpret an existing PC1 identity as authority.

## Lifecycle reconciliation

The controlling compiler pipeline remains:

```text
Read -> Parse -> Source validate -> Default -> Digest -> Package scan ->
Resolve -> Lock -> Expand -> Normalize -> Insert -> Static check ->
Identify -> Sort -> Manifest -> Persist
```

PC4 owns `Default` and returns `DefaultedSource`. The immediately following
responsibility is therefore:

```text
PC5 = Digest
PC5 output = Blueprint identity bound to the exact DefaultedSource
```

Package scanning has not yet occurred. Imports have not been resolved or
expanded. Declarations have not been normalized, statically checked,
identified, or sorted.

## Exact PC5 ownership

PC5 owns exactly these operations:

1. consume one accepted `DefaultedSource`;
2. encode the complete contained root value using Standard 0.3 canonical JSON
   as closed by the Canonical JSON Erratum;
3. calculate SHA-256 over exactly those canonical bytes;
4. create one `BlueprintDigest` with kind `blueprint`; and
5. return one opaque `DigestedSource` that binds that digest to the exact
   consumed `DefaultedSource`.

`threadsmith-compiler` owns the phase boundary and source-to-digest binding.
The accepted `threadsmith-canonical` crate remains the sole Rust owner of
canonical JSON and SHA-256 mechanics; PC5 must reuse that core rather than
introduce a second encoder or hash path. `threadsmith-schema` retains the
generic `ArtifactKind`, `Sha256Digest`, and `NativeLatticeId` vocabulary. The
future opaque `BlueprintDigest` may wrap that accepted vocabulary but may not
change its format or authority meaning.

PC1 deliberately permits callers to construct or parse a generic
`NativeLatticeId` claim. Such a caller-created claim is not a PC5-produced
`BlueprintDigest`, does not prove that `digest_source` ran, and cannot construct
a `DigestedSource`. PC5 adds a phase-origin distinction without revoking or
reinterpreting the accepted generic PC1 claim API.

The existing reconstructed generic canonical API is not, by existence alone,
evidence that PC5 is implemented or that every newly closed string vector
passes. PC5 implementation must separately qualify the exact erratum bytes.

## Exact preimage

The Blueprint preimage is exactly:

```text
canonical_json(DefaultedSource root value)
```

The entire root value participates. PC5 removes no field, inserts no field,
repairs no field, wraps no value, and adds no provenance. The Rust wrapper
name, memory layout, source path, YAML bytes, comments, formatting, file
metadata, diagnostics, compiler version, Rust version, operating system, and
cache state are absent unless the source value itself contains corresponding
Standard-permitted data.

The preimage is post-default and pre-import-expansion. It is not original YAML,
a file, an AST, a Rust memory representation, a compiler-stage envelope, a
Lockfile, a Manifest, or an expanded import graph.

Object presentation order does not affect the bytes because canonical JSON
sorts object keys. Existing array order remains identity-bearing because PC5
does not sort arrays and no prior accepted phase normalized declaration-array
order.

## Identity created

PC5 creates exactly one identity:

```text
lattice:blueprint:sha256:<64 lowercase hexadecimal characters>
```

This is content identity for the exact post-default source representation. It
does not prove that declarations are valid, that imports resolve, that the
source compiles, that a Lockfile or Manifest exists, that qualification passed,
or that execution is authorized.

PC5 does not create package, resource, contract, unit, link, policy, scenario,
Lockfile, Manifest, qualification, Binding, envelope, event, activation, or
construction identities. Later phases may create only the identities assigned
to them after their complete Standard preimages exist.

## Output boundary

The frozen conceptual output is:

```rust
pub struct DigestedSource {
    defaulted_source: DefaultedSource,
    blueprint_digest: BlueprintDigest,
}
```

Both fields are private. `DigestedSource` is constructible only by the PC5
digest operation. The public operation consumes the PC4 wrapper:

```rust
fn digest_source(source: DefaultedSource) -> DigestedSource
```

The contained `DefaultedSource` is value-for-value the exact input. The digest
is calculated from that contained value. No public constructor, field, or
replacement operation may pair a digest calculated for source A with source B
inside a `DigestedSource`.

Public deserialization into `DigestedSource` would be another mismatched-pair
constructor and is therefore outside the initial PC5 API.

`BlueprintDigest` is an opaque Blueprint-kind view over the accepted native
identity vocabulary. Its textual form is exact. Its internal constructor is
not a public substitute for `digest_source`. Public read-only formatting,
comparison, serialization, and borrowing do not create authority.

`DigestedSource` itself is not hashed, serialized into the Blueprint preimage,
persisted by PC5, or treated as authority. No canonical-preimage byte accessor
is added to the initial PC5 public API. Exact bytes remain observable through
conformance tests and the already accepted generic canonical boundary, not as
stored PC5 metadata.

## Diagnostic ownership and totality

PC5 owns no user-source diagnostic. Every value constructible as an accepted
`DefaultedSource` is an object composed recursively of collision-free NFC
strings, signed `i64` integers, booleans, nulls, arrays, and objects. Canonical
JSON and SHA-256 are therefore semantically total over the public PC5 input.

The public PC5 operation does not return declaration, profile, resolution,
package, reference, static-check, identity-format, or source diagnostics. An
internal inability to encode an accepted `DefaultedSource` is a compiler defect
or violated invariant, not a normal diagnostic for the user's source.

In particular, PC5 must not emit `SOURCE_DUPLICATE_NAME`. Duplicate declaration
names, invalid unit kinds, malformed declarations, unknown references,
wrong-type explicit values, and unresolved imports may all receive a
Blueprint digest. They remain available for later validation or static-check
allocation. Digestibility is not semantic acceptance.

## Identity equivalence and distinction

Sources that PC2 projects to equal values and PC4 expands to equal
`DefaultedSource` values have equal canonical bytes and equal Blueprint
digests. This includes comments, indentation, root-key order, permitted quoting
differences, equivalent YAML scalar spellings, NFC-equivalent strings, and
omitted versus explicitly equal Standard defaults.

Different `DefaultedSource` values produce distinct canonical byte sequences.
SHA-256 collision resistance is the Standard identity mechanism; a
conformance test proves distinct preimages and the expected test-vector
digests, not a mathematical proof that SHA-256 can never collide. Changes to
module, version, purpose, declarations, explicit non-default values, and array
order all change the preimage.

The root `profile` member also participates in the preimage. Under the accepted
PC3 Core boundary, however, only `lattice-core-0.1` can reach PC5. A changed
root profile is therefore tested as a canonical-preimage distinction plus a
separate proof that PC3 rejects the alternate profile. Tests must not forge a
`DefaultedSource` merely to exercise an unreachable public PC5 input.

## Responsibilities deliberately left later

| Concern | Owner after PC5 |
|---|---|
| Package descriptor discovery, validity, and package identities | `Package scan` scope intake |
| Version selection and import cycles | `Resolve` |
| Lockfile content and identity | `Lock` |
| Namespace assignment and import flattening | `Expand` |
| Declaration forms, fields, names, and local validity | Later `Normalize` or another explicit allocation consistent with the Standard |
| Duplicate declaration names | A later validation/static-check allocation; never PC5 |
| Cross-declaration references, contracts, ports, links, routes, policies, controls, budgets, secrets, and profile semantics | `Static check` or their later accepted allocations |
| Declaration identities and semantic collection order | `Identify` and `Sort` |
| Complete machine identity and persistence | `Manifest` and `Persist` |
| Qualification, Binding, execution, record, and replay | Their named later layers |

Deferral is not acceptance. The Blueprint digest remains useful as the exact
content identity of a source that a later phase rejects.

## Acceptance criteria

This scope is acceptable only when:

- the Canonical JSON Erratum uniquely selects bytes for every PC5 string;
- the input is exactly accepted `DefaultedSource` and the output binds it to
  exactly one Blueprint digest;
- the complete post-default root and every preserved array order participate;
- the digest format is exactly the Standard Blueprint identity format;
- canonical bytes are not added as PC5 payload metadata or a new initial
  public PC5 accessor;
- duplicate-name and every other later semantic diagnostic remain deferred;
- later identities, artifacts, and authority remain absent;
- exact canonical-byte and digest fixtures cover every required encoding,
  equivalence, distinction, later-invalid, and binding case;
- Foundation and PC1 through PC4 remain unchanged and green; and
- no PC5 product implementation, dependency mutation, commit, push, package,
  Builder, runtime, provider, or user-surface work occurs in this freeze.
