# PC8 Lock Semantic Freeze

Freeze-candidate date: 2026-07-28.

Acceptance date: 2026-07-28.

Status: semantic freeze accepted and published after the governing superseding
independent re-review closed `PC8-RR-P2-01` and returned final disposition
`PASS`. The frozen semantic region is byte-identical to the reviewed
candidate. PC8 implementation has not started and overall PC8 product
acceptance remains false.

## 1. Bound baseline and authority

```text
Branch=main
HEAD=54b8b2b380606428f0d41f33d5d32c985c18c7ea
TREE=0f578dcd1f9ac01ed01a32286020e11338f04f04
Required_remote_main=54b8b2b380606428f0d41f33d5d32c985c18c7ea
```

The controlling authority order and exact hashes are bound in
`PC8_SCOPE_RECONCILIATION.md` and the standalone manifest. This freeze is
co-bound with the focused Lock Semantics Erratum and does not modify PC7.

## 2. Frozen phase boundary

```text
accepted PC7 ResolvedSource
        |
        v
portable pure Lock construction
        |
        v
source-bound LockedSource
        |
        v
Expand
```

Resolve remains complete and unopened. Expand remains later.

## 3. Frozen input contract

Lock consumes exactly one immutable authenticated accepted PC7
`ResolvedSource`. It accepts no independently supplied root, digest, package
record, requirement, prior Lockfile, path, byte source, host capability,
clock, randomness, environment variable, filesystem state, network state,
locale, map order, integer width, or implementation metadata.

The operation is total over that domain and has no semantic diagnostic.

Every current criterion materializes the exact twelve-member public-PC7
`ResolvedSource`. Nineteen bind authenticated PC7 fixture-output expansions;
one binds a complete correlated public PC2-through-PC7 alias reconstruction.
No symbolic ID or Lock-only projection substitutes for the consumed value.

## 4. Frozen construction

The complete Lockfile has exactly:

```text
lock_version=1
lattice=0.3
profile=the exact active profile in ResolvedSource
root_blueprint_digest=the exact bound root Blueprint digest
packages=one row for each and only each selected PC6 package
lock_id=lattice:lock:sha256:<SHA-256 of canonical five-member value>
```

Every package row copies exact `name`, `version`, and `package_id` from one
selected PC6 record. Each converged applicable requirement targeting that
package contributes one occurrence:

```text
root contributor    -> module = contributor.module
package contributor -> module = contributor.package
all contributors    -> requirement = exact constraint text
```

Alias, interval, source path, contributor version, and contributor identity
are not output members. They distinguish PC7 contribution occurrences.
Equal projected rows remain repeated with exact occurrence multiplicity.
Retracted and inapplicable contributions produce no output.

Packages sort by unsigned NFC UTF-8 package-name bytes. `requested_by` sorts
by module bytes and then requirement bytes. Proper prefixes sort shorter
first. Equal requested_by rows remain equal and repeated.

## 5. Frozen identity and emitted bytes

The identity preimage is canonical JSON for the five-member semantic object
with `lock_id` absent. It never contains null, empty, placeholder, retained, or
recursively modified identity.

The emitted bytes are canonical JSON for the complete six-member object.
They include final `lock_id`, preserve Lock-owned array order, and contain no
insignificant whitespace, BOM, or final newline.

The two byte domains are distinct.

## 6. Exact empty Lockfile golden

Identity preimage UTF-8:

```json
{"lattice":"0.3","lock_version":1,"packages":[],"profile":"lattice-core-0.1","root_blueprint_digest":"lattice:blueprint:sha256:cf45903bf4fe32708c2cb6f9edd1cfba1004c216bebe20142acc29733d049343"}
```

```text
Preimage_bytes=193
Preimage_SHA256=ec6b48665f346ae4fbc96ae17cc1b4ae117bd89325a0a1f4b3b0044d94bcb284
lock_id=lattice:lock:sha256:ec6b48665f346ae4fbc96ae17cc1b4ae117bd89325a0a1f4b3b0044d94bcb284
Emitted_bytes=290
Emitted_SHA256=200983274432864025cb8554ae543af102dd851dbccad4920f77b81731eb7292
```

Emitted Lockfile UTF-8:

```json
{"lattice":"0.3","lock_id":"lattice:lock:sha256:ec6b48665f346ae4fbc96ae17cc1b4ae117bd89325a0a1f4b3b0044d94bcb284","lock_version":1,"packages":[],"profile":"lattice-core-0.1","root_blueprint_digest":"lattice:blueprint:sha256:cf45903bf4fe32708c2cb6f9edd1cfba1004c216bebe20142acc29733d049343"}
```

## 7. Exact one-root-requested golden

Identity preimage UTF-8:

```json
{"lattice":"0.3","lock_version":1,"packages":[{"name":"alpha","package_id":"lattice:package:sha256:cab3e435497175f5b42cab078cfd6424d30ad5aba6e0d3886d56c8949397a250","requested_by":[{"module":"root_app","requirement":"1.0.0"}],"version":"1.0.0"}],"profile":"lattice-core-0.1","root_blueprint_digest":"lattice:blueprint:sha256:9db58baa8f7b01eab1ab7598402567997299ad7d229b03dec892b1d3b7598df4"}
```

```text
Preimage_bytes=391
Preimage_SHA256=44ca76221d735f26624b245b8d34f5bcae72c7f847e3d070bc66833962416bad
lock_id=lattice:lock:sha256:44ca76221d735f26624b245b8d34f5bcae72c7f847e3d070bc66833962416bad
Emitted_bytes=488
Emitted_SHA256=90938eaf2ae9bdad6c7bb7a711c99826330fac7d791f032da22157ba2de0da99
```

Emitted Lockfile UTF-8:

```json
{"lattice":"0.3","lock_id":"lattice:lock:sha256:44ca76221d735f26624b245b8d34f5bcae72c7f847e3d070bc66833962416bad","lock_version":1,"packages":[{"name":"alpha","package_id":"lattice:package:sha256:cab3e435497175f5b42cab078cfd6424d30ad5aba6e0d3886d56c8949397a250","requested_by":[{"module":"root_app","requirement":"1.0.0"}],"version":"1.0.0"}],"profile":"lattice-core-0.1","root_blueprint_digest":"lattice:blueprint:sha256:9db58baa8f7b01eab1ab7598402567997299ad7d229b03dec892b1d3b7598df4"}
```

## 8. Frozen successful phase state

`LockedSource` preserves the exact consumed `ResolvedSource` through a closed
authenticated expansion reference whose recursion yields all twelve members.
It contains the complete Lockfile value, emitted bytes, and `lock_id`.

```text
Created_identity=exactly one lock_id
Created_artifact=exactly one canonical Lockfile
Created_runtime_authority=none
Created_builder_authority=none
Created_network_authority=none
Created_provider_authority=none
```

The wrapper creates no identity. Lock creates no Manifest, `manifest_id`,
declaration identity, namespace, expanded import, normalized declaration,
generated gate, static-check result, qualification record, Binding, runtime
object, event, or replay state.

## 9. Frozen round-trip condition

Every generated Lockfile is admitted by the public PC7
`ExistingLockfileInput` boundary under the same source context. Strict source,
closed schema, identity, and context gates all pass. Package order,
`requested_by` order and multiplicity, member domains, fixed values, canonical
bytes, and identity verification are identical on generation and intake.

## 10. Frozen persistence allocation

PC8 Lock is portable pure construction. The named `PC8 Lockfile Persistence
Adapter` is a later compiler persistence tranche and retains the Standard's
physical atomic replacement obligation.

No destination or host capability is invented here. The Lockfile becomes
durable compiler state only when that future adapter succeeds. This task does
not physically write a Lockfile. Operational failure is not a semantic result
and cannot change canonical bytes or `lock_id`.

## 11. Frozen authority boundary

The Lockfile is deterministic compiler output and is not executable. It grants
no filesystem, installation, Builder, runtime, provider, network, secret,
model, or execution authority. Durability and authority remain distinct.

## 12. Manifest populations

| Population | Cardinality | Ordered identifiers |
|---|---:|---|
| `authority` | 10 | `AUTH-01`, `AUTH-02`, `AUTH-03`, `AUTH-04`, `AUTH-05`, `AUTH-06`, `AUTH-07`, `AUTH-08`, `AUTH-09`, `AUTH-10` |
| `rule_provenance` | 40 | `LOCK-C-01`, `LOCK-C-02`, `LOCK-C-03`, `LOCK-C-04`, `LOCK-C-05`, `LOCK-C-06`, `LOCK-C-07`, `LOCK-C-08`, `LOCK-C-09`, `LOCK-C-10`, `LOCK-D-01`, `LOCK-D-02`, `LOCK-D-03`, `LOCK-D-04`, `LOCK-D-05`, `LOCK-D-06`, `LOCK-N-01`, `LOCK-N-02`, `LOCK-N-03`, `LOCK-N-04`, `LOCK-N-05`, `LOCK-N-06`, `LOCK-N-07`, `LOCK-N-08`, `LOCK-N-11`, `LOCK-N-12`, `LOCK-N-13`, `LOCK-N-14`, `LOCK-N-15`, `LOCK-N-16`, `LOCK-S-01`, `LOCK-S-02`, `LOCK-S-03`, `LOCK-S-04`, `LOCK-S-05`, `LOCK-S-06`, `LOCK-S-07`, `LOCK-S-08`, `LOCK-S-09`, `LOCK-S-10` |
| `schemas` | 16 | `SCHEMA-AUTHORITY`, `SCHEMA-AUTHORITY-ROOT`, `SCHEMA-CANDIDATE-STATUS`, `SCHEMA-DISCRIMINATOR`, `SCHEMA-FIXTURE`, `SCHEMA-FUTURE-ONLY`, `SCHEMA-MANIFEST`, `SCHEMA-NORMATIVE-CHOICE`, `SCHEMA-POPULATION`, `SCHEMA-PREIMAGE-REGISTRY`, `SCHEMA-RELATION`, `SCHEMA-RESOLVED-SOURCE`, `SCHEMA-RULE`, `SCHEMA-SCHEMA`, `SCHEMA-SELF-VALIDATION`, `SCHEMA-SEMANTIC-CONTRACT` |
| `normative_choices` | 14 | `LOCK-NC-01`, `LOCK-NC-02`, `LOCK-NC-03`, `LOCK-NC-04`, `LOCK-NC-05`, `LOCK-NC-06`, `LOCK-NC-07`, `LOCK-NC-08`, `LOCK-NC-11`, `LOCK-NC-12`, `LOCK-NC-13`, `LOCK-NC-14`, `LOCK-NC-15`, `LOCK-NC-16` |
| `resolved_sources` | 20 | `RS-ALIAS-A`, `RS-ALIAS-B`, `RS-DUPLICATE-ROWS`, `RS-EMPTY`, `RS-ID-CHANGED`, `RS-MODULE-CHANGED`, `RS-MULTIPLICITY-ONE`, `RS-MULTIPLICITY-TWO`, `RS-ONE-ROOT`, `RS-PACKAGE-PREFIX`, `RS-PRIOR-RB-A`, `RS-PRIOR-RB-B`, `RS-REQUEST-ORDER`, `RS-REQUIREMENT-CHANGED`, `RS-RETRACTED`, `RS-ROOT-CHANGED`, `RS-ROUTE-FRESH`, `RS-ROUTE-LOCK-MISSING`, `RS-TRANSITIVE`, `RS-VERSION-CHANGED` |
| `fixtures` | 20 | `FIX-ALIAS-A`, `FIX-ALIAS-B`, `FIX-DUPLICATE-ROWS`, `FIX-EMPTY`, `FIX-ID-CHANGED`, `FIX-MODULE-CHANGED`, `FIX-MULTIPLICITY-ONE`, `FIX-MULTIPLICITY-TWO`, `FIX-ONE-ROOT`, `FIX-PACKAGE-PREFIX`, `FIX-PRIOR-RB-A`, `FIX-PRIOR-RB-B`, `FIX-REQUEST-ORDER`, `FIX-REQUIREMENT-CHANGED`, `FIX-RETRACTED`, `FIX-ROOT-CHANGED`, `FIX-ROUTE-FRESH`, `FIX-ROUTE-LOCK-MISSING`, `FIX-TRANSITIVE`, `FIX-VERSION-CHANGED` |
| `relations` | 19 | `REL-ALIAS-NONMEMBER`, `REL-AMBIENT-INDEPENDENCE`, `REL-CANONICAL-BYTE-FORM`, `REL-MULTIPLICITY-CHANGE`, `REL-NO-SEMANTIC-DIAGNOSTIC`, `REL-PACKAGE-ID-CHANGE`, `REL-PC7-ROUNDTRIP`, `REL-PERSISTENCE-BOUNDARY`, `REL-PREIMAGE-MEMBER-OMISSION`, `REL-PREIMAGE-VERSUS-EMITTED`, `REL-PRESENTATION-PERMUTATION`, `REL-PRIOR-LOCK-REQUESTED-BY-IGNORED`, `REL-REQUESTED-BY-REORDER`, `REL-REQUESTING-MODULE-CHANGE`, `REL-REQUIREMENT-TEXT-CHANGE`, `REL-RETRACTION-EXCLUSION`, `REL-ROOT-DIGEST-CHANGE`, `REL-ROUTE-EQUIVALENCE`, `REL-VERSION-CHANGE` |
| `discriminators` | 41 | `DISC-ALIAS`, `DISC-AMBIENT`, `DISC-BYTE-DOMAINS`, `DISC-CANONICAL-FORM`, `DISC-EMPTY`, `DISC-EQUAL-MULTIPLICITY`, `DISC-MANIFEST-CLOSURE`, `DISC-MODULE`, `DISC-MULTIPLICITY`, `DISC-NO-WRAPPER-ID`, `DISC-NONASCII-FUTURE`, `DISC-ONE-ROOT`, `DISC-PACKAGE-ID`, `DISC-PACKAGE-ORDER`, `DISC-PERSISTENCE`, `DISC-PERSISTENCE-FUTURE`, `DISC-PREIMAGE-OMISSION`, `DISC-PRIOR-RB`, `DISC-PROFILE`, `DISC-PROPER-PREFIX-FUTURE`, `DISC-REQUEST-ORDER`, `DISC-REQUIREMENT`, `DISC-RETRACTION`, `DISC-ROOT-DIGEST`, `DISC-ROOT-TRANSITIVE`, `DISC-ROUNDTRIP`, `DISC-ROUTE`, `DISC-SCHEMA-ARRAY-ITEM-MISMATCH`, `DISC-SCHEMA-CHILD-MISMATCH`, `DISC-SCHEMA-CONST-VIOLATION`, `DISC-SCHEMA-CROSS-FIELD`, `DISC-SCHEMA-ENUM-VIOLATION`, `DISC-SCHEMA-MISSING-REQUIRED`, `DISC-SCHEMA-NULLABLE-MISMATCH`, `DISC-SCHEMA-OPTIONAL-ABSENT-MISMATCH`, `DISC-SCHEMA-UNION-VARIANT-MISMATCH`, `DISC-SCHEMA-UNKNOWN-MEMBER`, `DISC-SCHEMA-WRONG-BOOLEAN-STRING`, `DISC-SCHEMA-WRONG-OBJECT-CATEGORY`, `DISC-TOTALITY`, `DISC-VERSION` |
| `preimage_registry` | 4 | `REG-DUPLICATE-ROWS`, `REG-EMPTY`, `REG-ONE-ROOT`, `REG-PACKAGE-PREFIX` |
| `future_only` | 4 | `FUT-NONASCII-PACKAGE-ORDER`, `FUT-PHYSICAL-PERSISTENCE-ADAPTER`, `FUT-PROFILE-ALTERNATIVE`, `FUT-PROPER-PREFIX-PACKAGE-VECTOR` |
| `schema_mutations` | 12 | `DISC-SCHEMA-ARRAY-ITEM-MISMATCH`, `DISC-SCHEMA-CHILD-MISMATCH`, `DISC-SCHEMA-CONST-VIOLATION`, `DISC-SCHEMA-CROSS-FIELD`, `DISC-SCHEMA-ENUM-VIOLATION`, `DISC-SCHEMA-MISSING-REQUIRED`, `DISC-SCHEMA-NULLABLE-MISMATCH`, `DISC-SCHEMA-OPTIONAL-ABSENT-MISMATCH`, `DISC-SCHEMA-UNION-VARIANT-MISMATCH`, `DISC-SCHEMA-UNKNOWN-MEMBER`, `DISC-SCHEMA-WRONG-BOOLEAN-STRING`, `DISC-SCHEMA-WRONG-OBJECT-CATEGORY` |

All populations are exact, not estimated. The manifest self-validation
recomputed all 20 current complete sources, fixture preimages, hashes,
identities, emitted bytes, source-preservation results, and PC7 structural
round trips. All four representative preimage registries are gap-free,
overlap-free, completely attributed, and use `LOCK-C-09`, never
the superseded new-choice classification.

The non-ASCII comparator, literal proper-prefix package vector, non-Core
profile alternative, and physical persistence vector are future-only at their
exact activation boundaries. `lattice-builder-0.1` is not treated as a current
accepted PC7 Core output.

The recursive schema language has 1,266 schema nodes: 208 objects, 187 arrays,
159 primitives, 457 constants, 203 enums, 16 nullable nodes, 15 references,
and 21 unions. All 16 schema traversals terminate. The 21 unions dispatch by
three JSON categories, nine tagged members, and nine exactly-one structural
forms. All 204 declared consumers admit. All 12 complete mutation sources
admit, all 12 exact mutations reject at their one deterministic locator, and
all 12 otherwise unchanged mutations admit under the recorded single-target
bypass or mechanism-removal counterfactual. For the repaired four, this
isolates the population length-versus-admitted-cardinality cross-field
operator, the nullable finite input-ref enum, the single selected interval
occurrence's caret upper constant, and the executable `const false` structural
mismatch.

`REL-ROUTE-EQUIVALENCE` and
`REL-PRIOR-LOCK-REQUESTED-BY-IGNORED` freeze equal Lock artifact projection
but unequal complete source-bound `LockedSource`. `REL-ALIAS-NONMEMBER`
freezes equal `requested_by` projection, unequal complete Lock artifact due to
the correlated root digest, and unequal complete `LockedSource`. No
distinction relation claims minimal raw-path isolation where public-PC7
correlation requires additional digest, trace, graph, or provenance changes.

## 13. Accepted freeze status

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
