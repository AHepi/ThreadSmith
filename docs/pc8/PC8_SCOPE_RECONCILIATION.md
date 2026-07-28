# PC8 Lock Scope Reconciliation

Reconciliation date: 2026-07-28.

Acceptance date: 2026-07-28.

Status: accepted and frozen PC8 Lock scope reconciliation. The governing
superseding independent re-review closed `PC8-RR-P2-01` with P0=0, P1=0,
P2=0, no refuted, underdetermined, or unverified claim, and final disposition
`PASS`. The substantive reconciliation region is byte-identical to the
reviewed candidate. PC8 implementation has not started and overall PC8 product
acceptance remains false.

## 1. Authenticated baseline and authoring boundary

The pre-write gate authenticated branch `main`, commit
`54b8b2b380606428f0d41f33d5d32c985c18c7ea`, tree `0f578dcd1f9ac01ed01a32286020e11338f04f04`, local `main`, cached
`origin/main`, and fresh remote `main` at the same commit. No fetch occurred.
The index and tracked differences were empty. The untracked overlay was
exactly the four candidate paths listed below. The prior author report and
independent review were authenticated before substantive reading; the review
was read first and supplied only the three-defect repair allowlist.

The mutation allowlist is exactly:

```text
docs/standard/LATTICE_STANDARD_0.3_LOCK_SEMANTICS_ERRATUM.md
docs/pc8/PC8_SCOPE_RECONCILIATION.md
docs/pc8/PC8_SEMANTIC_FREEZE.md
docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST.json
```

No accepted authority, durable state, product code, test, Cargo file, generated
plan, existing conformance artifact, PC1-PC7 path, Git index, ref, or remote is
part of this gate.

## 2. Authority order

The accepted material was authenticated and read in the following controlling
order. Existing Rust structures were examined only afterward and only as
compatibility evidence.

| Order | Path | Bytes | SHA-256 | Role |
|---:|---|---:|---|---|
| 1 | `docs/standard/LATTICE_STANDARD_0.3.md` | 66657 | `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` | `primary_standard` |
| 2 | `docs/standard/LATTICE_STANDARD_0.3_CANONICAL_JSON_ERRATUM.md` | 6173 | `ac772adc17a98bb9ecd6f9916717d696a1614918e79fc996546742f0cd6015b7` | `canonical_encoding` |
| 3 | `docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md` | 152906 | `235ae8026676905b9f410167b18a902cd63dc449ecf073a96821e5d2d40e6c25` | `pc6_record_boundary` |
| 4 | `docs/standard/LATTICE_STANDARD_0.3_RESOLVE_SEMANTICS_ERRATUM.md` | 1413209 | `a0ab4b4eaa0e06d0105fd43b06e684c7581e7b359d6a89cc76eb44b9057fc72e` | `pc7_resolved_source_boundary` |
| 5 | `docs/pc7/PC7_SCOPE_RECONCILIATION.md` | 38667 | `4cee5f0beacd663ee9ab3bb9c05060342de18c1d6d7b56d3a477c46c15d80243` | `pc7_phase_allocation` |
| 6 | `docs/pc7/PC7_SEMANTIC_FREEZE.md` | 30129 | `47f2b65f3807e0fe4940c7c6c15475fa472f0a578dba2bccaaba670e43654169` | `pc7_frozen_output` |
| 7 | `docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json` | 1306575 | `da33daef1526e21a921c8b7bb847045f6e137567f2c0b3b3e6f2af9a796c123c` | `pc7_provenance_shapes` |
| 8 | `docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json` | 2041 | `7f39265be8bfd6db9fc93cedf357572eb5fab960000b9d6897ef983021112161` | `pc7_authority_closure` |
| 9 | `docs/pc7/PC7_IMPLEMENTATION_ACCEPTANCE_AND_PUBLICATION.md` | 13782 | `422136de3b07231d5f55155adae99b6171f1ed19309720f8d4e854dbffea7258` | `pc7_acceptance` |
| 10 | `/workspace/ThreadSmith/PC7/handoffs/implementation-acceptance-publication/output/THREADSMITH_PC7_IMPLEMENTATION_ACCEPTANCE_PUBLICATION_AND_DURABLE_STATE_UPDATE.txt` | 24874 | `7064a32177e39b8ee6dd5a39faca8e93c5511a03b9e7c7df8715b50e9ca79cce` | `publication_evidence` |

The Standard is primary. The Canonical JSON Erratum controls the one-to-one
encoding of an already selected JSON-shaped value. The Package Scan Erratum
controls retained PC6 records and identities. The Resolve Erratum and PC7
freeze control the exact immutable `ResolvedSource`, its converged selected
packages, and its applicable requirement provenance. This focused PC8
candidate controls only Lock if later independently reviewed and accepted.

## 3. Reconciled phase allocation

```text
accepted immutable PC7 ResolvedSource
                 |
                 v
               Lock
  pure canonical construction and lock_id
                 |
                 v
   source-bound LockedSource for Expand
```

`Resolve -> Lock -> Expand` remains fixed. Resolve owns package scanning
results, existing-Lockfile intake and validation, reuse, selection, fixed-point
processing, selected-module parsing, applicable requirements, retraction, and
cycle detection. Lock does not repeat or alter any of those operations.

Lock owns exactly one new canonical Lockfile value, its five-member identity
preimage, its `lock_id`, its complete emitted bytes, and the source-bound
successful phase result. Expand retains namespace assignment, import
flattening, imported declaration expansion, and later declaration processing.

## 4. Exact conceptual input

The operation consumes exactly one immutable accepted PC7 `ResolvedSource`.
The entire accepted object is preserved in success, but Lock reads only its
already-bound active profile, root Blueprint digest, converged selected PC6
records, and converged applicable requirement provenance for construction.

No independently paired root, digest, package list, requirement list, prior
Lockfile, path, mutable bytes, environment variable, clock, locale, random
value, filesystem observation, network state, host-width integer, map
iteration order, or implementation metadata is an input. PC7 history remains
part of the preserved source but is not an independent selection source.

The operation is total over this authenticated domain. A value forged by
bypassing PC7 is outside the domain rather than a Lock diagnostic input.

Every current manifest source expands to all twelve accepted conceptual
members:

```text
scanned_source
active_profile
existing_lock
resolution_passes
selected_packages
selected_modules
applicable_requirements
import_graph
created_identities
created_artifacts
authority
phase_status
```

Nineteen current rows bind an exact successful-output recipe in the
authenticated PC7 specified-conformance manifest. The twentieth is a complete
public PC2-through-PC7 alias reconstruction: it changes the root aliases,
recomputes the PC5 root identity, retains exact PC6 records and bytes, and
propagates the correlated values through the PC7 trace, graph, and provenance.
No string domain label, nine-member Lock projection, implementation-produced
value, or actual Resolve result substitutes for the source.

## 5. Exact successful output

The conceptual result is named `LockedSource` without prescribing a Rust
representation. It contains exactly:

```text
resolved_source
lockfile
canonical_lockfile_bytes
lock_id
created_identities
created_artifacts
authority
phase_status
```

`resolved_source` is the exact consumed object. `lockfile` is the complete
six-member value. `canonical_lockfile_bytes` are the emitted bytes.
`created_identities` contains exactly `lock_id`. `created_artifacts` contains
exactly the canonical Lockfile. `authority` is `none`.
`phase_status` is `non_authoritative_locked_source`.

The wrapper has no identity. It creates no competing phase-state identity.

## 6. Closed Lockfile construction

The Lockfile has exactly `lock_version`, `lattice`, `profile`,
`root_blueprint_digest`, `packages`, and `lock_id`.

`lock_version` is integer `1`. `lattice` is string `0.3`. `profile` is the
exact active profile inside the consumed source. `root_blueprint_digest` is
the exact bound Blueprint identity inside the consumed source. `packages`
contains one entry for each and only each converged selected PC6 record.

Every package entry copies `name`, `version`, and `package_id` from one exact
selected PC6 record. No value is reparsed from a file, recomputed from package
bytes, or copied from an existing Lockfile.

For each converged applicable PC7 requirement targeting that selected package,
Lock emits one `requested_by` occurrence. Root provenance maps
`contributor.module` to `module`. Package provenance maps
`contributor.package` to `module`; PC7 already binds that selected module name
to the package name. In both cases `requirement` is the exact original
canonical `constraint` string.

Alias, interval, source path, contributor version, and contributor package
identity do not become members of a `requested_by` row. They still determine
which PC7 contribution occurrence exists. Projection is occurrence-preserving:
two applicable contributions mapping to equal rows produce two equal rows.
The multiplicity of an equal row is exactly the number of converged applicable
records that project to it. Retracted or inapplicable records are absent.

## 7. Ordering

Packages are sorted by ascending unsigned NFC UTF-8 bytes of package name.
Package names remain unique. Proper prefixes sort shorter first. The accepted
current package grammar is ASCII-only, so a non-ASCII package-name vector is
truthfully future-only rather than forged through PC7.

The authenticated accepted PC7 fixture corpus has no selected package-name
pair where one name is a proper prefix of the other. Current
`FIX-PACKAGE-PREFIX` is therefore rebound to the accepted three-package chain
and proves canonical multi-package tuple ordering, not literal
proper-prefix-specific coverage. The latter is explicitly future-only until
an authenticated public-PC7 construction supplies such a pair. This coverage
limitation does not reopen the already-required shorter-first rule.

Each `requested_by` array is sorted by module unsigned NFC UTF-8 bytes and then
requirement unsigned NFC UTF-8 bytes. Proper prefixes sort shorter first.
Equal rows compare equal, remain repeated, and require no hidden tie-break.
Lock owns both sorts and does not inherit presentation, map, PC7 provenance,
or existing-Lockfile order.

The empty selected set produces the exact empty `packages` array.

## 8. Identity and byte domains

The identity preimage is the canonical JSON encoding of the exact five-member
Lockfile object obtained by omitting `lock_id` as a semantic object member.
Null, empty string, zero, placeholder, retained identity, and recursive
replacement are different values and forbidden preimages.

The digest is SHA-256 of exactly those bytes. The final identity is
`lattice:lock:sha256:` plus 64 lowercase hexadecimal digest characters.

Emitted Lockfile bytes are canonical JSON for the complete six-member object
including final `lock_id`. Object keys use accepted canonical UTF-8 ordering;
arrays retain the Lock-owned semantic order. There is no insignificant
whitespace, BOM, or trailing newline.

Textual deletion from a complete serialization is not a normative operation.
An implementation may optimize only if it independently proves byte equality
with canonical serialization of the specified five-member value.

## 9. Round-trip admission

A generated Lockfile supplied to public PC7 `ExistingLockfileInput` with the
same source context passes source intake, the exact six-member closed schema,
`lock_id` verification, and context admission. Generation and intake agree on
member domains, fixed values, package order, `requested_by` order and
multiplicity, identity spelling, canonical JSON, and the omission preimage.

## 10. Diagnostic and resource boundary

Lock has no semantic diagnostic over an authenticated accepted
`ResolvedSource`. Allocation exhaustion, stack or scheduling failure,
permission failure, interrupted persistence, storage exhaustion, and platform
failure are operational non-results. They cannot replace Lock success, create
a different `lock_id`, or produce a partial semantic result.

## 11. Atomic persistence reconciliation

This candidate selects reading B: PC8 Lock is the portable pure construction
phase. The physical atomic replacement adapter is explicitly named the
`PC8 Lockfile Persistence Adapter` and deferred to a later compiler
persistence tranche.

This reading is required by the exact one-member semantic input and the
portable-core boundary: no destination, current directory, filename,
installation layout, path grammar, or filesystem capability is available to
Lock. Inventing any would widen the input and create product behavior.

The Standard obligation remains binding. A compiler cannot claim durable
Lockfile replacement until the future adapter atomically replaces its
separately selected destination. This authoring task performs no physical
replacement. Persistence failure cannot change the already-created canonical
bytes or identity.

## 12. Artifact and authority status

The canonical Lockfile is one deterministic compiler artifact carrying one
`lock_id`. It becomes durable compiler state only when the future atomic
replacement succeeds. Durability is storage status, not execution authority.

Lock creates no Manifest, `manifest_id`, declaration identity, namespace,
expanded import, normalized declaration, generated gate, static-check result,
qualification record, Binding, runtime object, event, or replay state. It
grants no Builder, runtime, provider, filesystem, network, secret, model,
installation, or execution authority.

## 13. Ambiguity, absence, and contradiction inventory

| ID | Class | Pre-candidate gap | Closure |
|---|---|---|---|
| `LOCK-GAP-01` | absence | Exact Lock input and totality were not closed. | `LOCK-NC-01` |
| `LOCK-GAP-02` | absence | Source-bound success and wrapper identity status were absent. | `LOCK-NC-02` |
| `LOCK-GAP-03` | absence | Exact profile and root-digest projection were unstated. | `LOCK-NC-03` |
| `LOCK-GAP-04` | absence | Complete selected-record projection was unstated. | `LOCK-NC-04` |
| `LOCK-GAP-05` | ambiguity | `requested_by.module` and root/package contributors admitted multiple readings. | `LOCK-NC-05` |
| `LOCK-GAP-06` | ambiguity | Equal-row multiplicity could be preserved or deduplicated. | `LOCK-NC-06` |
| `LOCK-GAP-07` | ambiguity | Lock-owned sorting could be confused with incidental input order. | `LOCK-NC-07` |
| `LOCK-GAP-08` | absence | Empty Lock output was not golden-bound. | `LOCK-NC-08` |
| `LOCK-CLAR-09` | inherited requirement | Accepted authority already requires semantic identity omission and canonical five-member preimage serialization. | `LOCK-C-09`; exact golden and rejected-alternative criteria clarify conformance. |
| `LOCK-CLAR-10` | inherited requirement | Accepted authority already requires final identity insertion and canonical complete six-member emission. | `LOCK-C-10`; exact golden and rejected-alternative criteria clarify conformance. |
| `LOCK-GAP-11` | absence | Semantic versus operational failure was not allocated. | `LOCK-NC-11` |
| `LOCK-GAP-12` | ambiguity | Prior Lock and Resolve history could be treated as independent inputs. | `LOCK-NC-12` |
| `LOCK-GAP-13` | apparent tension, no contradiction | Atomic write is required, but portable Lock has no destination capability. | `LOCK-NC-13` and explicit named deferral retain the obligation. |
| `LOCK-GAP-14` | absence | Artifact durability was conflated with authority. | `LOCK-NC-14` and `LOCK-NC-15` |
| `LOCK-GAP-15` | absence | Durable specified criteria and population closure were absent. | `LOCK-NC-16` |

No accepted-authority contradiction remains. The atomic-write tension is
resolved without changing PC7 or inventing a product path.

## 14. Complete rule-provenance ledger

| Rule | Class | Complete reconciled rule bundle |
|---|:---:|---|
| `LOCK-S-01` | `[S]` | The accepted compiler allocation is Resolve then Lock then Expand. |
| `LOCK-S-02` | `[S]` | The Lockfile closed schema has exactly lock_version, lattice, profile, root_blueprint_digest, packages, and lock_id with the accepted fixed values and domains. |
| `LOCK-S-03` | `[S]` | Selected package name, version, and package_id originate in exact selected PC6 records retained by ResolvedSource. |
| `LOCK-S-04` | `[S]` | Packages sort by package-name bytes and requested_by sorts by module then requirement; equal requested_by rows are admitted and identity-bearing. |
| `LOCK-S-05` | `[S]` | Canonical JSON is the accepted NFC UTF-8 encoding with sorted object keys, semantic array order, no insignificant whitespace, BOM, or final newline. |
| `LOCK-S-06` | `[S]` | lock_id uses the lattice:lock:sha256 prefix and SHA-256 of canonical Lockfile content with identity omitted. |
| `LOCK-S-07` | `[S]` | A generated Lockfile must remain admissible through PC7 ExistingLockfileInput under the same context. |
| `LOCK-S-08` | `[S]` | Lock does not own Resolve selection or Expand namespace and declaration behavior. |
| `LOCK-S-09` | `[S]` | The Standard retains an atomic Lockfile replacement obligation. |
| `LOCK-S-10` | `[S]` | A Lockfile is a non-executable compiler artifact and does not grant runtime authority. |
| `LOCK-C-01` | `[C]` | Lock consumes the exact accepted PC7 ResolvedSource, not independently paired fields or prior inputs. |
| `LOCK-C-02` | `[C]` | Existing-Lockfile observations inside PC7 history are not a second Lock input. |
| `LOCK-C-03` | `[C]` | LockedSource preserves the exact consumed ResolvedSource and carries derived Lock value, bytes, and identity. |
| `LOCK-C-04` | `[C]` | Generation and PC7 later intake use one schema, ordering, canonicalization, and identity meaning. |
| `LOCK-C-05` | `[C]` | Proper-prefix comparison is shorter-first and equality is permitted only within requested_by, never package names. |
| `LOCK-C-06` | `[C]` | Resource or persistence failure is separate from semantic Lock construction. |
| `LOCK-C-07` | `[C]` | No semantic diagnostic exists because forged phase state is outside the authenticated input domain. |
| `LOCK-C-08` | `[C]` | Current Rust types and canonicalization are compatibility evidence only and cannot create missing rules. |
| `LOCK-C-09` | `[C]` | Accepted authority requires semantic omission of lock_id and canonical serialization of the exact five-member preimage; candidate vectors clarify the exact bytes and rejected substitutions. |
| `LOCK-C-10` | `[C]` | Accepted authority requires insertion of final lock_id and canonical serialization of the complete six-member emitted value; candidate vectors clarify the exact bytes and rejected alternatives. |
| `LOCK-N-01` | `[N]` | Lock is total over exactly one authenticated immutable accepted PC7 ResolvedSource and has no other semantic input. |
| `LOCK-N-02` | `[N]` | Success is one source-bound LockedSource with exactly the declared eight conceptual members and no wrapper identity. |
| `LOCK-N-03` | `[N]` | profile and root_blueprint_digest project from the exact bound ResolvedSource fields. |
| `LOCK-N-04` | `[N]` | Each and only each selected PC6 record projects one package row with exact name, version, and package_id. |
| `LOCK-N-05` | `[N]` | Each converged applicable requirement projects one requested_by row; module is root contributor.module or package contributor.package, and requirement is exact constraint text. |
| `LOCK-N-06` | `[N]` | Projection is occurrence-preserving; equal rows remain with multiplicity equal to contributing PC7 records. |
| `LOCK-N-07` | `[N]` | Lock owns package and requested_by sorting with unsigned NFC UTF-8 comparators and no incidental-order inheritance. |
| `LOCK-N-08` | `[N]` | The empty selected-package set produces packages as the exact empty array. |
| `LOCK-N-11` | `[N]` | Authenticated-domain construction cannot emit a Lock diagnostic; resource and forged-state failures are operational non-results. |
| `LOCK-N-12` | `[N]` | Only the final Lock-relevant projection is consumed; resolution route, prior Lockfile content, aliases, retracted contributions, and ambient state do not independently affect output. |
| `LOCK-N-13` | `[N]` | PC8 uses the portable pure-construction reading and names the deferred physical writer PC8 Lockfile Persistence Adapter. |
| `LOCK-N-14` | `[N]` | The canonical Lockfile is a deterministic compiler artifact and becomes durable compiler state only after the future atomic replacement succeeds. |
| `LOCK-N-15` | `[N]` | Lock creates one lock_id and one canonical Lockfile, grants no authority, and creates none of the enumerated later artifacts or states. |
| `LOCK-N-16` | `[N]` | The specified conformance manifest has closed populations, complete references, expected structures and bytes, and self-validation obligations without an executability claim. |
| `LOCK-D-01` | `[D]` | Physical atomic replacement is deferred to the named PC8 Lockfile Persistence Adapter tranche. |
| `LOCK-D-02` | `[D]` | Expand retains namespace assignment, imported declaration expansion, and flattening. |
| `LOCK-D-03` | `[D]` | Normalize, Insert, Static check, Identify, Sort, Manifest, and Manifest persistence remain later compiler phases. |
| `LOCK-D-04` | `[D]` | Implementation, executable planning, qualification, independent review, acceptance, and publication remain later gates. |
| `LOCK-D-05` | `[D]` | Builder, runtime, providers, installation, product surfaces, network, secrets, models, execution, events, and replay remain unauthorized. |
| `LOCK-D-06` | `[D]` | Non-ASCII package-name ordering remains future-only because the accepted PC7 package-name grammar is ASCII-only. |

The exact totals are `[S]=10`, `[C]=10`, `[N]=14`, and `[D]=6`, for 40 rule
bundles. Every new choice is separately registered:

| Choice | New normative choice | Principal discriminators |
|---|---|---|
| `LOCK-NC-01` | Lock is total over exactly one authenticated immutable accepted PC7 ResolvedSource and has no other semantic input. | `DISC-AMBIENT`, `DISC-TOTALITY` |
| `LOCK-NC-02` | Success is one source-bound LockedSource with exactly the declared eight conceptual members and no wrapper identity. | `DISC-NO-WRAPPER-ID` |
| `LOCK-NC-03` | profile and root_blueprint_digest project from the exact bound ResolvedSource fields. | `DISC-PROFILE`, `DISC-ROOT-DIGEST` |
| `LOCK-NC-04` | Each and only each selected PC6 record projects one package row with exact name, version, and package_id. | `DISC-PACKAGE-ID`, `DISC-ROUNDTRIP`, `DISC-VERSION` |
| `LOCK-NC-05` | Each converged applicable requirement projects one requested_by row; module is root contributor.module or package contributor.package, and requirement is exact constraint text. | `DISC-ALIAS`, `DISC-MODULE`, `DISC-ONE-ROOT`, `DISC-REQUIREMENT`, `DISC-RETRACTION`, `DISC-ROOT-TRANSITIVE`, `DISC-ROUNDTRIP` |
| `LOCK-NC-06` | Projection is occurrence-preserving; equal rows remain with multiplicity equal to contributing PC7 records. | `DISC-EQUAL-MULTIPLICITY`, `DISC-MULTIPLICITY` |
| `LOCK-NC-07` | Lock owns package and requested_by sorting with unsigned NFC UTF-8 comparators and no incidental-order inheritance. | `DISC-NONASCII-FUTURE`, `DISC-PACKAGE-ORDER`, `DISC-PROPER-PREFIX-FUTURE`, `DISC-REQUEST-ORDER` |
| `LOCK-NC-08` | The empty selected-package set produces packages as the exact empty array. | `DISC-EMPTY` |
| `LOCK-NC-11` | Authenticated-domain construction cannot emit a Lock diagnostic; resource and forged-state failures are operational non-results. | `DISC-AMBIENT`, `DISC-TOTALITY` |
| `LOCK-NC-12` | Only the final Lock-relevant projection is consumed; resolution route, prior Lockfile content, aliases, retracted contributions, and ambient state do not independently affect output. | `DISC-AMBIENT`, `DISC-PRIOR-RB`, `DISC-RETRACTION`, `DISC-ROUTE` |
| `LOCK-NC-13` | PC8 uses the portable pure-construction reading and names the deferred physical writer PC8 Lockfile Persistence Adapter. | `DISC-PERSISTENCE`, `DISC-PERSISTENCE-FUTURE` |
| `LOCK-NC-14` | The canonical Lockfile is a deterministic compiler artifact and becomes durable compiler state only after the future atomic replacement succeeds. | `DISC-PERSISTENCE`, `DISC-PERSISTENCE-FUTURE` |
| `LOCK-NC-15` | Lock creates one lock_id and one canonical Lockfile, grants no authority, and creates none of the enumerated later artifacts or states. | `DISC-NO-WRAPPER-ID` |
| `LOCK-NC-16` | The specified conformance manifest has closed populations, complete references, expected structures and bytes, and self-validation obligations without an executability claim. | `DISC-MANIFEST-CLOSURE` |

## 15. Conformance coverage and limitations

The standalone manifest has 10 authorities, 40 rules, 16 recursively closed
schemas, 14 genuine normative choices, 20 current complete sources, 20 current
fixtures, 19 relations, 41 discriminators, four preimage registries, four
future-only criteria, and 12 schema-mutation criteria. The identifier arrays
in `populations` are the exact UTF-8-sorted sets; no historical count is
retained.

`SCHEMA-MANIFEST` recursively reaches every value. The finite schema language
defines primitive JSON categories, closed objects, required and optional
members, additional-member rejection, constants, enums, arrays and item
schemas, references, tagged and structural unions, nullable versus absent
values, and a defined cross-field operator. `SCHEMA-SCHEMA` binds the finite
bootstrap row and node grammar. All 16 traversals terminate, all 15 child
references resolve exactly once, and every union has deterministic dispatch.

All twelve complete mutation sources admit, all twelve exact mutations reject
at their deterministic locators, and all twelve otherwise unchanged mutations
admit when only the named mechanism is bypassed or removed. Rejection alone is
not credited. The cross-field row changes admitted authority cardinality
`10` to independently admitted `40` while retaining ten IDs; removal of only
`SCHEMA-POPULATION$.cross_field_constraints[0]` then admits it. The nullable
row names the exact finite input-ref enum that rejects integer `7`. The union
row selects only
`SCHEMA-RESOLVED-SOURCE$.admission_rule.members.expected_value.members.applicable_requirements.items.members.interval`;
its kind-only exact-to-caret mutation retains lower `1.0.0`, so only the caret
upper constant rejects null. The Boolean-string row identifies the exact
`const false` node and its structural rejection of string `"false"`. The
other eight mutations retain their isolated wrong-category, constant, enum,
child, array-item, unknown-member, missing-required, and optional-member
mechanisms.

All 20 current source criteria materialize complete twelve-member values. The
current and future-only dispositions are exact in the manifest. In particular,
`RS-PROFILE-CHANGED` and `FIX-PROFILE-CHANGED` are removed from current
populations. `FUT-PROFILE-ALTERNATIVE` activates only when accepted public PC7
authority supplies a successful non-Core source; `lattice-builder-0.1` is not
used.

Every fixture preserves its exact source through a closed authenticated
expansion reference and recomputes its complete preimage, identity, emitted
value, created populations, authority absence, wrapper-identity absence, and
PC7 structural re-admission. Exact golden results are:

| Fixture | Selected packages | Preimage bytes | Preimage SHA-256 | `lock_id` | Emitted bytes | Emitted SHA-256 |
|---|---:|---:|---|---|---:|---|
| `FIX-ALIAS-A` | 1 | 437 | `441474e4170cc3aaf74ac7f25edec3fab4012c36d64f2cb93b000154c7b7d5d5` | `lattice:lock:sha256:441474e4170cc3aaf74ac7f25edec3fab4012c36d64f2cb93b000154c7b7d5d5` | 534 | `ce9ff9c0dc7b69fe30ac74d13ca68aeadf68c16a088cc9dff5eca6360ae9d2d1` |
| `FIX-ALIAS-B` | 1 | 437 | `55e1e23876b13de5beb5e3d7ef08c64b4934067df3c1f99ac1a9e0818ccdb440` | `lattice:lock:sha256:55e1e23876b13de5beb5e3d7ef08c64b4934067df3c1f99ac1a9e0818ccdb440` | 534 | `3297b5b6f15a1609b6319d9fb4296be5ce345c4643867643d9b9658607ca0b46` |
| `FIX-DUPLICATE-ROWS` | 1 | 437 | `441474e4170cc3aaf74ac7f25edec3fab4012c36d64f2cb93b000154c7b7d5d5` | `lattice:lock:sha256:441474e4170cc3aaf74ac7f25edec3fab4012c36d64f2cb93b000154c7b7d5d5` | 534 | `ce9ff9c0dc7b69fe30ac74d13ca68aeadf68c16a088cc9dff5eca6360ae9d2d1` |
| `FIX-EMPTY` | 0 | 193 | `ec6b48665f346ae4fbc96ae17cc1b4ae117bd89325a0a1f4b3b0044d94bcb284` | `lattice:lock:sha256:ec6b48665f346ae4fbc96ae17cc1b4ae117bd89325a0a1f4b3b0044d94bcb284` | 290 | `200983274432864025cb8554ae543af102dd851dbccad4920f77b81731eb7292` |
| `FIX-ID-CHANGED` | 1 | 393 | `e917bd602348545a75d5bdd5659779e404cf531f4a63a7f40bf3899339f93185` | `lattice:lock:sha256:e917bd602348545a75d5bdd5659779e404cf531f4a63a7f40bf3899339f93185` | 490 | `9a1b7964f97f4760dd0c2c64d915a644a28722932a6939dbff6d420c88010a67` |
| `FIX-MODULE-CHANGED` | 1 | 395 | `5a3b7a980fae443d824308dc5ed157f9580679648085318ee80c30e12a4f3b33` | `lattice:lock:sha256:5a3b7a980fae443d824308dc5ed157f9580679648085318ee80c30e12a4f3b33` | 492 | `b3412eaea5c4a09ada9c960abcea2baf6d11ba14820dc9a47a7611ba1a075ec1` |
| `FIX-MULTIPLICITY-ONE` | 1 | 392 | `bd53541e29bbd1f78c361c501d4e646ef68e4dc00fb03b76930184051021205c` | `lattice:lock:sha256:bd53541e29bbd1f78c361c501d4e646ef68e4dc00fb03b76930184051021205c` | 489 | `be57b0132b953ae118e332a39d7835daf69a51d8443d8dea216ae1682009f804` |
| `FIX-MULTIPLICITY-TWO` | 1 | 437 | `441474e4170cc3aaf74ac7f25edec3fab4012c36d64f2cb93b000154c7b7d5d5` | `lattice:lock:sha256:441474e4170cc3aaf74ac7f25edec3fab4012c36d64f2cb93b000154c7b7d5d5` | 534 | `ce9ff9c0dc7b69fe30ac74d13ca68aeadf68c16a088cc9dff5eca6360ae9d2d1` |
| `FIX-ONE-ROOT` | 1 | 391 | `44ca76221d735f26624b245b8d34f5bcae72c7f847e3d070bc66833962416bad` | `lattice:lock:sha256:44ca76221d735f26624b245b8d34f5bcae72c7f847e3d070bc66833962416bad` | 488 | `90938eaf2ae9bdad6c7bb7a711c99826330fac7d791f032da22157ba2de0da99` |
| `FIX-PACKAGE-PREFIX` | 3 | 793 | `c7b3704924e0cba0e992b894dd69bc73ccc6ad93e6383c1d6a2fa122bed7fb7f` | `lattice:lock:sha256:c7b3704924e0cba0e992b894dd69bc73ccc6ad93e6383c1d6a2fa122bed7fb7f` | 890 | `30b8fe68932b6a047fbc0da248532462f2d1a91f7ea3c4416fcdb0927ea41bf7` |
| `FIX-PRIOR-RB-A` | 1 | 392 | `744347baa6dc480dc1988594471b84813e6227714aad5b9adf981e211a52cac9` | `lattice:lock:sha256:744347baa6dc480dc1988594471b84813e6227714aad5b9adf981e211a52cac9` | 489 | `f3144ae4c25aacf64f7f022aca382d014dc87bae751fb6ca8733adff8bd2b60a` |
| `FIX-PRIOR-RB-B` | 1 | 392 | `744347baa6dc480dc1988594471b84813e6227714aad5b9adf981e211a52cac9` | `lattice:lock:sha256:744347baa6dc480dc1988594471b84813e6227714aad5b9adf981e211a52cac9` | 489 | `f3144ae4c25aacf64f7f022aca382d014dc87bae751fb6ca8733adff8bd2b60a` |
| `FIX-REQUEST-ORDER` | 2 | 633 | `190252deb013605b6f9c1632847a7e8edd83fcf746289f800d4897b1ac803e99` | `lattice:lock:sha256:190252deb013605b6f9c1632847a7e8edd83fcf746289f800d4897b1ac803e99` | 730 | `55077070041d98b4463d8e118fa715c64930229388f20c03e9f2e0d6ad812c50` |
| `FIX-REQUIREMENT-CHANGED` | 1 | 392 | `bd53541e29bbd1f78c361c501d4e646ef68e4dc00fb03b76930184051021205c` | `lattice:lock:sha256:bd53541e29bbd1f78c361c501d4e646ef68e4dc00fb03b76930184051021205c` | 489 | `be57b0132b953ae118e332a39d7835daf69a51d8443d8dea216ae1682009f804` |
| `FIX-RETRACTED` | 3 | 833 | `2afda213cf11bb6bd49e95d4ace649c89eb85d0c0385c2f57af92dda91d4abb1` | `lattice:lock:sha256:2afda213cf11bb6bd49e95d4ace649c89eb85d0c0385c2f57af92dda91d4abb1` | 930 | `2b83a4dfb8175c904d54d76ed004289f61707b03a9d800542bccbb5415619602` |
| `FIX-ROOT-CHANGED` | 2 | 591 | `1e974a02697fd8509fdcf2e287c786cf8cf6d813bf7bbf82c8e1ee54f39777b9` | `lattice:lock:sha256:1e974a02697fd8509fdcf2e287c786cf8cf6d813bf7bbf82c8e1ee54f39777b9` | 688 | `ac3016e2834dc9719873306be7884ea0ecdf8cbac8ca09dbaec94d04fa76e777` |
| `FIX-ROUTE-FRESH` | 1 | 392 | `bd53541e29bbd1f78c361c501d4e646ef68e4dc00fb03b76930184051021205c` | `lattice:lock:sha256:bd53541e29bbd1f78c361c501d4e646ef68e4dc00fb03b76930184051021205c` | 489 | `be57b0132b953ae118e332a39d7835daf69a51d8443d8dea216ae1682009f804` |
| `FIX-ROUTE-LOCK-MISSING` | 1 | 392 | `bd53541e29bbd1f78c361c501d4e646ef68e4dc00fb03b76930184051021205c` | `lattice:lock:sha256:bd53541e29bbd1f78c361c501d4e646ef68e4dc00fb03b76930184051021205c` | 489 | `be57b0132b953ae118e332a39d7835daf69a51d8443d8dea216ae1682009f804` |
| `FIX-TRANSITIVE` | 2 | 587 | `71a5b2f0dea61f55e326191d7756d3e2add73aeda9a9173d325eceb5ef7c3589` | `lattice:lock:sha256:71a5b2f0dea61f55e326191d7756d3e2add73aeda9a9173d325eceb5ef7c3589` | 684 | `907302911cdff1bdad2d1a74389e06baa85d1fe3845a7b26397731a2e553564b` |
| `FIX-VERSION-CHANGED` | 1 | 393 | `3b6b27c1492c68e161a9eb29902dfc453f9bd6ad0d5e93d498a14bdd3ebabb7b` | `lattice:lock:sha256:3b6b27c1492c68e161a9eb29902dfc453f9bd6ad0d5e93d498a14bdd3ebabb7b` | 490 | `e3acc97f08e1532faba8ad735126598d53b773cd5d2b572b71ca91a231e1e11a` |

`REL-ROUTE-EQUIVALENCE` and
`REL-PRIOR-LOCK-REQUESTED-BY-IGNORED` explicitly record equal Lock artifact
projection and unequal complete source-bound `LockedSource`. The alias pair
in `REL-ALIAS-NONMEMBER` has equal `requested_by` projection but unequal
complete Lock artifact because correlated public reconstruction changes the
root digest; it also has unequal complete `LockedSource`. No distinction
relation claims raw-path minimality
when correlated source, digest, graph, trace, or provenance fields also differ.

The non-ASCII package-name relation, literal proper-prefix fixture, non-Core
profile alternative, and physical persistence adapter are future-only at
their exact activation boundaries. None is dispatchable now.

These are specified candidate criteria only. No generator, interpreter,
dispatcher, Rust test, executable plan, qualification, review, acceptance, or
publication claim is made.

## 16. Accepted reconciliation disposition

All selection-, byte-, identity-, ordering-, output-, authority-, and
diagnostic-affecting Lock choices within the authenticated PC7 boundary are
closed. Physical persistence is explicitly and narrowly deferred without
weakening the Standard obligation.

```text
PC8_IR_P2_01_REPAIR_CANDIDATE_COMPLETE=true
PC8_IR_P2_02_REPAIR_CANDIDATE_COMPLETE=true
PC8_IR_P2_03_REPAIR_CANDIDATE_COMPLETE=true
PC8_RR_P2_01_REPAIR_CANDIDATE_COMPLETE=true
PC8_SCOPE_RECONCILIATION_CANDIDATE_COMPLETE=true
PC8_SEMANTIC_FREEZE_CANDIDATE_COMPLETE=true
PC8_REPAIR_CANDIDATE_COMPLETE=true
PRIOR_PC8_SEMANTIC_REVIEW_DISPOSITION=FAIL
PRIOR_PC8_SEMANTIC_REREVIEW_DISPOSITION=FAIL
GOVERNING_PC8_SEMANTIC_REREVIEW_DISPOSITION=PASS
PC8_RR_P2_01_CLOSED=true
PC8_SEMANTICS_ACCEPTED=true
PC8_SPECIFIED_CONFORMANCE_ACCEPTED=true
PC8_SEMANTIC_FREEZE_COMPLETE=true
PC8_SEMANTICS_FROZEN=true
PC8_DOCUMENTATION_PUBLISHED=true
PC8_IMPLEMENTATION_STARTED=false
PC8_ACCEPTED=false
FIXTURE_MATURITY=specified
BUILDER_AUTHORIZED=false
RUNTIME_AUTHORIZED=false
PUSH_COMPLETE=true
FINAL_DISPOSITION=PASS
NEXT_BOUNDED_TASK=separate read-only PC8 implementation and executable-conformance impact assessment against the newly frozen authority
```
