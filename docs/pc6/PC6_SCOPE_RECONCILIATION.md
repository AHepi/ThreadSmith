# PC6 Package-Scan Scope Reconciliation and Ambiguity Report

Reconciliation date: 2026-07-23.

Status: preserved pre-erratum reconciliation record. Its substantive
conclusions are unchanged. The ambiguities identified here were subsequently
closed by the accepted Package Scan Semantics Erratum, permitting a separate
PC6 semantic freeze while leaving implementation unstarted.

## Repository baseline

| Field | Required and observed value |
|---|---|
| Repository | `AHepi/ThreadSmith` |
| Branch | `main` |
| Local commit | `3d56efb3e42f0d0cf35d4731273dd3f106eb43f0` |
| Local tree | `47ceeb56de77b4f025ba8b997d130219cbbdd982` |
| `origin/main` | `3d56efb3e42f0d0cf35d4731273dd3f106eb43f0` |
| Remote tree | `47ceeb56de77b4f025ba8b997d130219cbbdd982` |
| Initial worktree | Clean |

## Controlling material

| Material | Relevance |
|---|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | Controlling project layout, source encoding, names, packages, resolution, canonical identity, compiler pipeline, diagnostics, filesystem, and security rules |
| `docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md` | Confirms PC4 does not traverse package content and imported defaults remain later |
| `docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md` | Closes byte encoding only after a package descriptor preimage has been selected |
| `docs/adr/0001-portable-core-language.md` | Assigns package verification and canonical identities to the single Rust core when their normative semantics are closed |
| Foundation and PC1 evidence | Preserves generic canonical and typed identity vocabulary as non-authoritative claims |
| PC2 reconciliation, freeze, verification, and review | Restricts PC2 to root-source YAML parsing and the signed-`i64`, NFC JSON-shaped value domain |
| PC3 reconciliation, freeze, verification, and review | Restricts PC3 to the root Blueprint envelope |
| PC4 reconciliation, freeze, verification, and review | Restricts PC4 to root-source defaults and explicitly excludes package traversal |
| PC5 reconciliation, freeze, verification, and review | Supplies opaque `DigestedSource`, creates only `BlueprintDigest`, and defers package validity and package identity to PC6 intake |
| `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md` | Current accepted state and phase sequencing |
| `crates/threadsmith-schema/src/lib.rs` | Existing recovered logical package types; compatibility evidence, not authority to fill Standard omissions |
| `crates/threadsmith-compiler/src/lib.rs` | Accepted private construction chain through `DigestedSource` |
| Current conformance material | No normative PC6 fixture exists; Foundation package examples test only the recovered logical schema |

The original Standard and both accepted errata remain unchanged. The current
`PackageDescriptor` cannot close the gaps by precedent: it omits the example's
`lattice` field, normalizes caller paths rather than defining filesystem
admission, requires exactly one Core profile, requires `module_file` to occur
in `files`, and rejects duplicate normalized paths without those rules being
stated exhaustively in Standard section 12. Those are potentially sensible
rules, but treating recovered code as normative would reverse the accepted
authority order.

## Phase position and broad ownership

The controlling pipeline fixes this position:

```text
PC5 Digest
    |
    v
PC6 Package scan
    |
    v
Resolve
    |
    v
Lock
    |
    v
Expand and later compiler phases
```

PC6 owns local package discovery, package-descriptor intake, declared-file
verification, and construction of the non-authoritative valid-local-package
set. It does not select versions or expand imports. `threadsmith-compiler` is
the phase owner. Canonical JSON and SHA-256 mechanics must remain in
`threadsmith-canonical`; accepted generic identity vocabulary remains in
`threadsmith-schema`.

The host must supply an explicit project-root or package-root capability. PC6
cannot derive filesystem authority from `DigestedSource`, ambient current
directory, a package declaration, or a package's contents. This is bounded
compile-time read capability only. It grants no runtime or broker authority.

## Candidate input and output boundary

The scope supports this conceptual input:

```text
accepted opaque DigestedSource
+ explicit host-supplied project/package-root read capability
```

The source must remain bound to the exact package scan that follows it. A
future output should therefore have the semantic shape:

```text
ScannedSource {
    digested_source,
    valid_local_packages,
    verified_package_content_snapshot
}
```

All fields would be private, with construction restricted to the PC6 scan
operation. Public construction, deserialization, source replacement, package
set replacement, or mutable snapshot access would be forbidden because each
could pair source A with a package set scanned for source B.

This representation is not frozen. The Standard does not say whether verified
bytes are retained directly, retained through content-addressed immutable
blobs, held through stable handles, or re-read and reverified. The behavioral
invariant must be that later phases consume exactly the bytes PC6 verified or
fail without partial compilation, but normative authority for that invariant's
phase representation is missing.

## Rules closed directly by the Standard

The following scope rules are sufficiently explicit and do not depend on a new
identity interpretation:

- package resolution is local only;
- a conforming package occupies
  `packages/<package-name>/<version>/package.yaml` with declared files under
  that package version directory;
- Scan parses and validates every local package descriptor, not only packages
  reachable from root imports;
- consequently a discovered invalid descriptor cannot be silently ignored
  merely because it is unused;
- package file paths are relative, use `/`, contain no `.` or `..` segment,
  and designate regular files;
- every listed file must match its declared digest;
- unlisted files have no semantic existence and must not be read;
- symlinks inside the package tree are rejected;
- canonical package-descriptor normalization sorts `files` by `path`;
- timestamps, ownership, permissions, directory enumeration order, and
  absolute filesystem location do not enter package identity;
- canonical JSON itself preserves array order unless a package rule explicitly
  sorts that collection;
- package identity text, once its exact preimage exists, is
  `lattice:package:sha256:<64 lowercase hexadecimal characters>`; and
- a package and its identity are non-authoritative compile-time content. They
  grant no filesystem, network, model, provider, secret, Binding, or runtime
  permission.

“Every local package descriptor” makes the scan reachability-independent, but
it does not define which malformed directory entries count as attempted local
packages. That discovery-edge question remains open below.

## Scan universe

### Reconciled

The normal descriptor location is layout-exact and two levels below
`packages/`; PC6 must not recursively treat arbitrary nested `package.yaml`
files as packages. Nested directories are meaningful only as parents of files
declared by a valid package descriptor. Every descriptor discovered in the
local package universe is validated before Resolve, independent of root-import
reachability. Enumeration order cannot affect the resulting valid set.

Ordinary unlisted files inside a valid package have no semantic existence and
must not be opened to inspect, classify, hash, parse, or execute them.

### Unresolved

The Standard does not define:

- whether a `<package-name>/<version>/` directory without `package.yaml` is a
  scan error or a non-package directory;
- whether stray entries directly under `packages/` are ignored or invalid;
- whether a descriptor at another depth is ignored or makes the layout
  invalid;
- whether a non-directory entry occupying a package-name or version slot is a
  package-path error; or
- the deterministic first diagnostic when several discovery entries fail.

No fixture may assign expected success or failure to those cases before a
normative clarification.

## Directory and descriptor agreement

Package and version directory components select the candidates presented to
Resolve, so their relationship to descriptor fields affects both resolution
and final identities. The Standard supplies the directory placeholders and
descriptor fields but does not state that:

- descriptor `package` must equal the package-directory component;
- descriptor `version` must equal the version-directory component;
- a version-directory component follows the Core version grammar, including
  whether leading zeroes are allowed;
- directory components must already be NFC rather than normalized by the
  implementation;
- comparison is by raw bytes, Unicode scalar values, or a platform-normalized
  path representation; or
- case-folding filesystems must reject colliding spellings rather than merge
  them.

Package-name grammar is ASCII and therefore inherently NFC once it is required
for directory names, but the Standard has not explicitly applied that grammar
to the directory component or defined mismatch behavior. These rules require
normative closure.

## Package descriptor grammar

Section 12 shows these apparent members:

```text
package
version
lattice
profiles
module_file
files[] { path, sha256 }
```

The example and surrounding prose establish intended concepts, not an
exhaustive schema comparable to section 10's explicit root allowlist. The
Standard does not state:

- the exact required and optional key sets;
- whether unknown descriptor or file-entry keys are rejected or participate
  in identity;
- whether the descriptor uses the complete restricted YAML profile from
  section 8, including duplicate-key, scalar-domain, NFC, and presentation
  rules;
- whether each example member's JSON type is mandatory;
- whether `lattice` must be exactly the string `0.3`;
- whether `profiles` must be non-empty, unique, contain only
  `lattice-core-0.1`, or may list multiple compatible profiles;
- whether profile order is semantic beyond the general canonical rule that an
  unsorted array preserves order;
- whether `module_file` must occur exactly once in `files`;
- whether `files` may be empty;
- whether file-entry mappings permit exactly `path` and `sha256`; or
- whether duplicate paths and post-NFC path collisions are descriptor errors.

The package-name grammar and Core three-component version form are normative
when those fields are admitted. The Standard does not say whether numeric
version components permit leading zeroes; accepted PC3 correctly did not add a
prohibition absent from the Standard, while the recovered Foundation
`PackageDescriptor` currently prohibits them. PC6 cannot silently choose one.

Because unknown-key behavior determines the canonical mapping and therefore
the package ID, this missing grammar is an identity-blocking ambiguity.

## Declared files and filesystem objects

The Standard closes regular-file and symlink rejection, digest matching, and
non-reading of unlisted files. It does not close:

- whether `module_file` must be listed in `files`;
- whether `package.yaml` may, must, or must not appear in `files`;
- unique-path and normalized-collision behavior;
- whether hard links are accepted as regular files or rejected as aliases;
- whether intermediate path components are checked independently for
  symlinks;
- the exact behavior for missing, disappearing, unreadable, or concurrently
  replaced entries;
- whether directory, socket, FIFO, device, and other special-file failures
  share one category or distinct categories; or
- whether PC6 must read and retain every declared file during scan or may
  postpone reading some verified content.

Section 7's blanket rejection of symlinks inside package trees supports
rejection at both final and intermediate components. The race-free inspection
mechanism and diagnostic precedence still require a portable behavioral rule.

## Portable path grammar

The closed path core is: relative, `/`-separated, no `.` or `..` segment, and
a regular-file target contained by its package root without following a
symlink.

The Standard does not decide:

- leading, trailing, repeated separators, or other empty segments;
- whether reverse solidus is forbidden as a character as well as unavailable
  as a separator;
- NUL, C0/C1 controls, DEL, and other filesystem-sensitive characters;
- NFC admission versus normalization and post-NFC collisions;
- Windows drive prefixes, drive-relative forms, rooted forms, and UNC forms;
- host case folding and Unicode filesystem normalization;
- maximum path component or complete path length; or
- the portable comparison used for deterministic path order and diagnostic
  selection.

Host convenience normalization cannot safely fill these gaps: it could make
two conforming implementations discover different files or produce different
package identities.

## File digest semantics

The field is named `sha256` and every listed file must match its digest, but
the package section uses only the placeholder `<hex>`. Unlike native identity
text, it does not explicitly state:

- exactly 64 lowercase hexadecimal characters;
- SHA-256 over the exact raw file bytes;
- that newline bytes and any BOM participate without normalization;
- the empty-file digest;
- invalid-character and length behavior;
- whether a mismatch is a package-scan diagnostic distinct from
  `RESOURCE_HASH_MISMATCH`; or
- whether the verified bytes are read once and retained or may later be read
  again.

The ordinary interpretation is SHA-256 over raw bytes, but an identity-bearing
freeze cannot substitute ordinary convention for normative text.

## Filesystem snapshot and mutation

The fixed-input determinism guarantee requires the package content used by
later compilation to be the content verified by PC6. The Standard does not
specify a logical snapshot contract. Without one, this sequence is possible:

```text
PC6 verifies declared file A
file is replaced after verification
Resolve or Expand reads unverified file B
```

A conforming clarification must require one of these equivalent outcomes:

- PC6 retains immutable verified bytes;
- PC6 retains content-addressed immutable blobs and later phases consume those
  blobs;
- PC6 retains handles that provably identify the same immutable content; or
- a later read is reverified against the frozen descriptor and compilation
  fails before semantic consumption if it differs.

The implementation mechanism may vary, but successful later compilation must
never consume bytes different from the verified snapshot. Descriptor mutation
and file mutation during scanning also need deterministic failure or exact
snapshot rules. This is a mandatory freeze blocker.

## Package identity and exact preimage

The Standard states:

```text
package_id = SHA-256(canonical package descriptor)
```

and requires `files` to sort by path. It also excludes timestamps, ownership,
permissions, directory order, and absolute paths. Canonical JSON excludes YAML
presentation once a parsed descriptor value is established. Declared file
bytes would ordinarily participate through the `sha256` members rather than
being inserted directly into the descriptor.

The exact preimage nevertheless remains unresolved because the descriptor's
closed mapping is unresolved. In particular:

- unknown fields may be forbidden, included, or ignored;
- `lattice` is present in the Standard example but absent from the recovered
  `PackageDescriptor` type;
- `profiles` has no package-specific sort or uniqueness rule, so the general
  canonical rule preserves its supplied order, but the admissible profile
  collection is not defined;
- duplicate or post-NFC-colliding `files` paths are not normatively classified;
- directory/descriptor agreement is not defined; and
- descriptor source parsing and normalization are not assigned to an existing
  parser boundary.

Directory names should not enter the canonical descriptor merely because they
locate it; the Standard says the descriptor is the preimage and excludes
absolute path. They can still be mandatory validation inputs whose values must
agree with descriptor fields. That validation rule is missing.

No package identity, golden descriptor bytes, or golden package digest may be
frozen from the current text. A clarification must also assign the sole
phase-produced `PackageDigest`/package-ID constructor to PC6; generic PC1
`NativeLatticeId` claims must remain non-authoritative and must not prove a
package was scanned.

## Imported-module intake

The compiler pipeline contains no named imported-module Parse, Source validate,
Default, or Digest phase. PC2 through PC5 apply only to the root Blueprint, and
the Default Semantics Erratum explicitly says PC4 does not traverse package
content. Yet Resolve must discover transitive requirements from selected
packages, and Expand must consume `module_file` declarations.

The Standard does not define:

- when `module_file` bytes are read as source rather than merely hash-verified;
- whether the restricted YAML parser is reused and which source root schema an
  imported module follows;
- which existing phase validates imported module root shape and profile
  compatibility;
- where the Standard defaults are applied to imported declarations;
- whether an imported module has a distinct digest or relies only on its
  package identity;
- whether Resolve may parse only imports before Expand; or
- which phase owns imported declaration-body validation.

PC6 must not absorb root PC2-PC5 semantics merely because it already has file
bytes. Resolve and Expand also cannot invent incompatible imported-source
pipelines. This ownership gap independently blocks PC6 semantic freeze under
the authorized stop conditions.

## Duplicate packages and Resolve boundary

`RESOLVE_DUPLICATE_VERSION` is explicitly a Resolve diagnostic: the resolver's
Deduplicate step follows Scan and rejects one package name/version associated
with different identities. PC6 must therefore retain all otherwise valid
candidates needed by Resolve and must not emit that diagnostic.

Whether identical identities deduplicate before or within Resolve, and how
multiple physical copies arise under one layout-exact root, depends on the
unresolved directory, case, and normalization rules. Candidate order must be
deterministic but may not be frozen until portable path comparison is closed.

PC6 also does not collect version constraints, choose versions, reuse a lock,
restart to a fixed point, report `RESOLVE_NO_COMMON_VERSION`, or detect import
cycles unless a later normative allocation explicitly places a necessary
subcheck there.

## Diagnostics

PC6 must eventually own failures for invalid discovery paths, descriptors,
descriptor/directory mismatch, declared-file intake, symlinks and special
files, digest mismatch, canonical-descriptor failure, and snapshot mutation.
Those failures must prevent `ScannedSource`; no partial valid set may be
reported as success.

The Standard supplies no package-scan diagnostic vocabulary or deterministic
precedence. `RESOURCE_HASH_MISMATCH` is defined for a resource declaration and
must not be silently reinterpreted as a package-file or package-descriptor
digest error. `RESOLVE_DUPLICATE_VERSION`, `RESOLVE_NO_COMMON_VERSION`, and
`RESOLVE_IMPORT_CYCLE` remain Resolve-owned.

A future clarification or accepted freeze must define exact PC6 codes and
first-error ordering across at least:

```text
discovery and package path
descriptor source parsing
descriptor schema
directory-field agreement
portable declared paths and duplicates
filesystem object and symlink inspection
missing or unreadable files
declared digest syntax
content hash mismatch
canonical descriptor and package identity
snapshot mutation
```

Within categories, package candidates, descriptor keys, and file paths need a
portable byte-order rule plus deterministic depth/index traversal. No codes or
precedence are frozen by this report.

## Resource bounds

The controlling material defines no maximum package count, descriptor bytes,
declared files per package, declared path length, package file bytes, or scan
directory depth beyond the logical layout. This leaves memory, descriptor,
filesystem, and hashing resource-exhaustion risks.

PC6 semantics must not manufacture rejection limits because limits change
which package sets are valid. A future operational implementation may need
host safety limits, but any semantic limit requires normative authority and
must distinguish safety failure from content identity.

## Non-authority and deferred ownership

A successfully scanned package remains local, compile-time,
non-authoritative, non-executable, unqualified, and unbound. Package identity
proves only the identity of the closed canonical descriptor and the verified
declared hashes. It does not grant access to any declared path or content.

PC6 explicitly defers:

- root and transitive version-constraint collection;
- exact version selection and greatest-version comparison;
- existing-lock reuse;
- resolution restarts and the 256-pass bound;
- `RESOLVE_DUPLICATE_VERSION` and `RESOLVE_NO_COMMON_VERSION`;
- import-cycle allocation pending imported-module clarification;
- Lockfile body, persistence, and `lock_id`;
- namespace creation and import flattening;
- declaration normalization and validation;
- resource, contract, unit, link, policy, scenario, and other declaration
  identities;
- generated intake gates;
- cross-declaration static checking;
- Manifest sorting, construction, identity, and persistence;
- qualification, Run Binding, runtime, events, replay, Builder, providers,
  package installation, CLI, MCP, UI, Android, and every execution surface.

## Fixture plan after normative closure

No PC6 fixture manifest or golden package identity is created now. A future
freeze must include exact portable directory trees, descriptor source bytes,
declared file bytes, expected diagnostics, canonical descriptor byte hex, and
package digest text.

### Valid and equivalent

- minimal valid package;
- multiple declared regular files;
- descriptor key-order and permitted YAML-presentation variation;
- `files` declaration-order variation converging through path sorting;
- package discovery-order variation;
- an empty raw file with its exact SHA-256;
- a valid non-ASCII NFC path if the clarified path grammar permits it; and
- repeated scanning of one immutable logical snapshot.

### Identity distinctions

- package name;
- version;
- lattice version;
- profiles value or order as clarified;
- module file;
- declared path;
- declared file digest; and
- declared file set.

### Invalid package intake

- malformed descriptor source;
- unknown descriptor and file-entry keys;
- package and version directory mismatch;
- missing descriptor or module file according to the clarified universe;
- module file absent from `files` if prohibited;
- duplicate and post-NFC-colliding file paths;
- uppercase, wrong-length, non-hex, and mismatching digests;
- absolute, dot, parent, empty, repeated-separator, reverse-solidus, Windows
  drive, rooted, and UNC paths;
- NUL/control and non-NFC paths;
- file or intermediate symlink;
- directory, device, socket, FIFO, hard-link, and other special entries as
  clarified;
- missing, unreadable, disappearing, and concurrently changing files;
- package-root escape; and
- mutation between PC6 verification and later consumption.

### Phase boundary

- unresolved imports and incompatible requirements remain for Resolve;
- same name/version with different package identities is assigned to Resolve;
- invalid declaration bodies are not PC6 package validity checks;
- an unused invalid package blocks or does not block exactly as the clarified
  scan universe requires, with the current “every descriptor” rule preserving
  reachability independence;
- no Lockfile, Manifest, Binding, qualification, or authority is created; and
- imported module parsing/default/validation follows its clarified later
  owner rather than being smuggled into PC6.

Ambiguous cases above deliberately have no expected output, diagnostic code,
canonical byte stream, or package digest in this report.

## Required normative clarification

A narrow Lattice Standard 0.3 Package Scan Semantics Erratum is required before
PC6 can be frozen. It should resolve only existing package-scan omissions and
must not add a registry, package manager, declaration, unit kind, authority
mechanism, compiler phase, runtime behavior, or product surface.

The erratum must close:

1. the exact local discovery universe and directory/descriptor agreement;
2. the restricted descriptor source encoding and exhaustive descriptor/file
   entry schemas;
3. the portable path and filesystem-object grammar;
4. raw-file SHA-256 syntax and byte participation;
5. immutable verified-content continuity across later compiler consumption;
6. the exact canonical package descriptor value and Package identity owner;
7. imported-module intake ownership within existing compiler phases; and
8. package-scan diagnostic categories and deterministic precedence.

Resource limits may remain explicitly unspecified with a recorded exhaustion
risk, but no identity- or validity-affecting limit may be invented locally.

## Reconciliation result

PC6's phase position, broad responsibility, non-authority boundary, root-source
binding requirement, and later-phase exclusions are reconciled. The meaning of
“Valid local package set” is not sufficiently closed to support an identity-
bearing semantic freeze. Creating a semantic-freeze document or guessed
package vectors would produce a ThreadSmith-specific package language while
claiming Standard conformance.

```text
PC6_SCOPE_RECONCILED=true
PACKAGE_SCAN_ERRATUM_ACCEPTED=true
PC6_SEMANTICS_FROZEN=true
PC6_FREEZE_VERIFICATION_COMPLETE=true
PC6_IMPLEMENTATION_STARTED=false
PC6_ACCEPTED=false
NEXT_BOUNDED_TASK=PC6 Package Scan implementation only
```
