# PC6 Package-Scan Semantic Freeze

Freeze date: 2026-07-23.

Status: Package Scan semantics frozen for a separately bounded implementation
task. PC6 implementation has not started and PC6 is not accepted.

## Normative authority

`docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md` is the
accepted normative companion that closes the Package Scan omissions in Lattice
Standard 0.3. It is controlling for PC6 discovery, descriptor admission,
portable snapshot behavior, declared-file verification, canonical package
construction, package identity, retained-byte continuity, diagnostics, and
phase boundaries.

The reviewed fourth repaired candidate had SHA-256
`d3569fc4de0c7e87fdc33c90b3fe427c7032cdd76c462c0696bfb3bd0740007d`.
Its independent read-only review reported P0=0, P1=0, P2=0, and P3=0.
Acceptance records that evidence; this freeze is not another independent
review.

The original Standard, Default Semantics Erratum, Canonical JSON Erratum, ADR
0001, and accepted PC1 through PC5 authority remain unchanged.

## Lifecycle boundary

```text
PC5 DigestedSource
        +
explicit bounded PortableProjectSnapshot
        |
        v
PC6 Package scan
        |
        v
source-bound, non-authoritative ScannedSource
        |
        v
Resolve (deferred)
```

Package scan occurs immediately after `Digest` and immediately before
`Resolve`.

## Exact conceptual input

PC6 consumes exactly:

```text
the accepted opaque DigestedSource
+
an explicitly supplied, complete, immutable PortableProjectSnapshot
```

The snapshot capability is bounded to exact lookup of the optional project-root
child named `packages` and, when that child exists, its complete immutable
subtree. It is supplied by the host before semantic Package scan. It is not
derived from `DigestedSource`, an ambient current directory, an environment
variable, Blueprint content, package content, a prior identity, or runtime
authority.

Snapshot acquisition must either produce one complete immutable portable view
or fail before a semantic `PackageScanOutcome`. PC6 never reopens or compares a
live filesystem after that boundary.

## Exact PC6 ownership

PC6 owns:

- exact local package discovery at
  `packages/<package-name>/<version>/package.yaml`;
- structural traversal, candidate ordering, and directory/descriptor
  agreement;
- accepted-PC2 restricted-YAML parsing of every discovered descriptor;
- exhaustive descriptor and file-entry schema admission;
- canonical profile and declared-file collection normalization defined by the
  accepted erratum;
- portable declared-path grammar and exact snapshot traversal;
- metadata-only no-link auditing of admitted version subtrees;
- verification of every declared file against its declared SHA-256;
- retention of the exact immutable bytes that were verified;
- construction of the exact six-member canonical package descriptor;
- creation of the exact
  `lattice:package:sha256:<64 lowercase hexadecimal>` package identity;
- deterministic primary Package Scan diagnostics and their canonical paths;
  and
- construction of a source-bound, non-authoritative scanned result.

`threadsmith-compiler` owns the future phase boundary and source/package
binding. `threadsmith-canonical` remains the sole owner of accepted canonical
JSON and SHA-256 mechanics. `threadsmith-schema` retains the accepted generic
identity vocabulary without treating a caller-created identity claim as proof
that Package scan ran.

## Output and source binding

A successful conceptual output is:

```text
ScannedSource {
    digested_source,
    ordered_scanned_packages
}
```

Each scanned-package record inseparably binds:

```text
admitted canonical descriptor value
package identity
declared logical path -> exact verified immutable bytes
```

All fields are private semantic state. No public constructor, deserializer,
replacement operation, mutable accessor, or independent pairing may substitute
the source, package sequence, descriptor, identity, declared path, or retained
bytes. Later phases must consume only the retained immutable content.

The successful output is source-bound and non-authoritative. It contains no
live path, host read capability, mutation capability, provider capability,
execution capability, or permission.

## Canonical package and identity ownership

After complete admission and byte verification, PC6 constructs exactly the
accepted erratum's six-member descriptor containing:

```text
package
version
lattice
profiles
module_file
files
```

Profiles and files use only the accepted semantic ordering rules. Canonical
JSON then follows the accepted Canonical JSON Erratum without any wrapper,
filename, type tag, length prefix, NUL, or trailing newline.

PC6 is the sole phase-produced package-identity owner. Package identities prove
content identity only: the exact admitted canonical descriptor and the
declared raw-file digests whose retained bytes were verified. They do not prove
import reachability, imported-module validity, resolution, compilation,
qualification, Binding, installation, permission, or execution authority.

## Diagnostics and precedence

PC6 owns exactly the 31-code diagnostic vocabulary and complete target-path
rules in the accepted erratum. It returns one deterministic primary diagnostic
and no partial `ScannedSource`.

Structural discovery uses nested NFC UTF-8 traversal. Successful candidates use
package-name ASCII order and numeric canonical-version order. Global descriptor
parse, shallow schema, collection, metadata audit, declared-file verification,
and canonical derivation stages execute in the accepted precedence. The six
accepted PC2 parser outcomes are mapped one-to-one without finer
reclassification.

Snapshot-acquisition and operational resource failures occur outside semantic
`PackageScanOutcome`; they produce no package identity or partial package set.

## Explicit deferral

PC6 does not own and explicitly defers:

- Resolve, constraint collection, version selection, lock reuse, resolution
  restarts, duplicate-version handling, no-common-version handling, and import
  cycles;
- Lockfile behavior, Lockfile persistence, and `lock_id`;
- imported-module parsing beyond descriptor intake, import expansion,
  namespace assignment, and flattening;
- declaration validation, duplicate declaration names, profile compatibility,
  normalization, generated-gate insertion, and static checking;
- resource, contract, unit, link, policy, scenario, and other declaration
  identities;
- collection sorting outside the exact PC6 descriptor rules;
- Manifest creation, Manifest identity, persistence, and qualification;
- Run Binding, runtime, events, replay, providers, installation, networking,
  filesystem effects, secrets, and authority;
- Builder, CLI, MCP, UI, Android, package-product, and every execution or
  distribution surface.

Deferral is not acceptance. In particular, PC6 verifies and retains
`module_file` bytes but does not parse or validate their imported declaration
meaning.

## Acceptance invariant

> Two conforming implementations receiving the same DigestedSource and the
> same portable immutable project snapshot produce identical discovered
> candidates, identical primary diagnostics, byte-identical package preimages,
> identical package identities, identical retained verified content, and an
> equivalent source-bound non-authoritative scanned result.

## Implementation boundary

This freeze creates no Rust type, function, diagnostic implementation,
conformance fixture file, dependency, Cargo mutation, package product, or
runtime behavior. The accepted candidate's embedded exact fixtures are the
semantic contract for the separately bounded implementation task.

```text
PC6_SCOPE_RECONCILED=true
PACKAGE_SCAN_ERRATUM_ACCEPTED=true
PC6_SEMANTICS_FROZEN=true
PC6_FREEZE_VERIFICATION_COMPLETE=true
PC6_IMPLEMENTATION_STARTED=false
PC6_ACCEPTED=false
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
NEXT_BOUNDED_TASK=PC6 Package Scan implementation only
```
