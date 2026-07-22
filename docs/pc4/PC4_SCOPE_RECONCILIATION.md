# PC4 Default-Phase Scope Reconciliation

Reconciliation date: 2026-07-22.

## Controlling evidence

| Evidence | Role |
|---|---|
| `docs/standard/LATTICE_STANDARD_0.3.md` | Controlling lifecycle and original default table; recovered SHA-256 `33e3e5606cdabfce86dbef2895608ba6b2bb4d3daf3ce711dc91c62ae17e5379` |
| `docs/standard/LATTICE_STANDARD_0.3_DEFAULT_SEMANTICS_ERRATUM.md` | Controlling clarification of exact PC4 targets, representations, invalid-data behavior, determinism, identity participation, and fixture obligations |
| `docs/pc2/PC2_STANDARD_RECONCILIATION.md` and `docs/compliance/PORTABLE_CORE_PRE_PC4_COMPLIANCE.md` | Accepted allocation of restricted-YAML parsing to PC2 and evidence that no default behavior remains there |
| `docs/pc3/PC3_SCOPE_RECONCILIATION.md` and `docs/pc3/PC3_SEMANTIC_FREEZE.md` | Accepted PC3 input/output, preservation, diagnostic, and non-authority boundary |
| `crates/threadsmith-compiler/src/lib.rs` and `tests/pc3_source_validate.rs` | Accepted public `ValidatedSource` implementation boundary and regression route |
| `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md` | Current state, bounded sequence, and durable decisions |
| `docs/adr/0001-portable-core-language.md` | Accepted Rust ownership and single canonical-core boundary |

Foundation and PC1 continue to control existing canonical-byte, identity-claim,
native/legacy, migration, and authority semantics. PC4 does not reopen them.

## Lifecycle reconciliation

The controlling pipeline remains:

```text
Read -> Parse -> Source validate -> Default -> Digest -> Package scan ->
Resolve -> Lock -> Expand -> Normalize -> Insert -> Static check ->
Identify -> Sort -> Manifest -> Persist
```

PC2 owns `Parse`. PC3 owns `Source validate` and returns `ValidatedSource`.
The immediately following responsibility is therefore:

```text
PC4 = Default
PC4 output = Expanded source defaults
```

The next consumer is PC5 `Digest`. PC4 prepares the post-default value used by
later identity preimages, but it does not canonicalize bytes, hash the value,
or issue an identity.

## Ownership

| Item | Frozen allocation |
|---|---|
| Owning crate | `threadsmith-compiler` |
| Input type | Accepted PC3 `ValidatedSource` |
| PC4 responsibility | Deterministically insert only Standard-and-erratum defaults at exact absent targets |
| Output type | Non-authoritative `DefaultedSource` containing only the expanded JSON-shaped value |
| Immediate consumer | PC5 `Digest` |
| Schema crate | `threadsmith-schema` remains schemas and data structures; it does not own compiler phase control |

`DefaultedSource` is a frozen semantic type boundary, not implemented by this
tranche. Its future representation must prevent construction without PC4 and
must expose the expanded value to PC5 without adding identity-bearing data.

No new crate or dependency is selected.

## Exact PC4 responsibility

PC4 owns only these transformations:

1. insert the eight absent optional root arrays;
2. insert input defaults at root inputs and unit input ports;
3. insert output cardinality at root exports and unit output ports;
4. insert exact unit-mode defaults for recognized Core kinds;
5. insert model repair and fallback defaults for an exact model kind;
6. insert link mode, delivery, and `when` defaults;
7. insert policy `when` defaults;
8. insert scenario `required` defaults; and
9. preserve every present, malformed, ambiguous, or non-target value as
   required by the erratum.

PC4 performs the erratum's fixed traversal, preserves all array order, and is
idempotent. It does not search arbitrary nested objects for matching names.

## Output and information boundary

The identity-bearing payload of `DefaultedSource` is exactly one JSON-shaped
value after default insertion. It contains no source-presence ledger, default
marker, provenance member, sidecar, compiler metadata, source location, or
other non-Standard field.

For a defaulted target, omitted and explicitly supplied default values converge
to the same output value. This loss of source-presence distinction is required
for identity equivalence. Explicit non-default, empty, null, wrong-type, and
later-invalid values remain present and unchanged. Absence remains absence for
every field without a Standard default or without an unambiguous erratum
target.

The Rust wrapper type itself is phase-state information only. Its type name and
in-memory layout are not serialized and never enter an identity preimage.

## Diagnostic ownership

PC4 is a total semantic transformation over an accepted `ValidatedSource` and
owns no source or compiler diagnostic code. It cannot receive a PC3-invalid
root through the accepted type boundary. Malformed declaration elements and
invalid explicit values are preserved for later phases rather than diagnosed.

Consequently PC4 has no competing semantic errors and no primary-error ordering
to select. Determinism is expressed by exact output equality. PC4 must not emit
PC2 parser errors, PC3 root errors, declaration/profile errors, resolution
errors, or static semantic errors, and it must not return a partially expanded
value as success.

## Responsibilities deliberately left later

| Concern | Owner after PC4 |
|---|---|
| Canonical bytes and Blueprint identity | PC5 `Digest` scope intake |
| Package discovery and validity | `Package scan` |
| Version selection | `Resolve` |
| Lockfile creation | `Lock` |
| Import namespaces and flattening | `Expand` |
| Declaration forms, field types, names, and local validity | `Normalize` or a later scope allocation consistent with the Standard |
| Cross-declaration references, ports, contracts, links, routes, policies, controls, budgets, secrets, and profile semantics | `Static check` or their later accepted allocations |
| Declaration identities and collection sorting | `Identify` and `Sort` |
| Complete machine construction and persistence | `Manifest` and `Persist` |
| Qualification, Binding, runtime, record, and replay | Their named later layers |

Deferral is not acceptance. PC4 may add an unambiguous default to an otherwise
invalid declaration, but its output remains non-authoritative and unvalidated.

## Authority boundary

PC4 creates no Blueprint identity, declaration identity, package identity,
Lockfile, Manifest, Qualification Record, Run Binding, executable object,
permission, provider configuration, event, or runtime state. A caller must not
describe `DefaultedSource` as validated declarations, compiled, identified,
qualified, bound, executable, or authoritative.

## Acceptance criteria

This scope is acceptable only when:

- ownership remains in `threadsmith-compiler`;
- the input is exactly PC3 `ValidatedSource` and the next consumer is PC5;
- the output contains only the expanded JSON-shaped value;
- every erratum target and value has an exact fixture;
- explicit and malformed values are preserved without PC4 diagnostics;
- deterministic equality, idempotence, array preservation, non-recursive
  targeting, identity equivalence, and identity distinction are fixture-bound;
- Foundation, PC1, PC2, and PC3 regressions remain green;
- the original Standard and accepted erratum remain unchanged; and
- no product implementation, dependency, identity, authority, or later-phase
  behavior is introduced.
