# ThreadSmith Restoration Plan

Document status: reconstructed on 2026-07-22 for the Foundation/PC1 recovery only.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Inventory | Every supplied artifact is hashed, classified, and assigned an exact, inferred, or unresolved path. | 0 | Complete |
| Minimum reconstruction | Only the recovered two-crate Rust workspace, PC1 vectors, ADR, and durable recovery state exist. | 2 | Complete |
| Verification | Format, workspace check, Clippy with denied warnings, locked/offline checks, Foundation tests, PC1 tests, conformance vectors, and recovered-byte hashes pass. | 2 | Complete |
| Read-only acceptance | A separate reviewer finds no P0 or P1 restoration defect and confirms Foundation/PC1 boundaries. | 2 | Complete after repair cycle 1 |
| Provenance anchor | The commit containing this accepted tree and tag `threadsmith-foundation-pc1-reconstructed-0.1` form the new anchor; remote ref verification is recorded outside this self-referential tree. | 0 | Delivery gate |

The active scope excludes PC2 and every parser, YAML, compiler, runtime, builder, planner, provider, UI, CLI/MCP, and Android concern. The next bounded task after this baseline is `PC2 parser-dependency intake and semantic freeze`; it is not authorized within this restoration.

## PC2 parser intake tranche

This later tranche was authorized separately and completed as preparation only. It does not reopen or reinterpret the completed restoration gates above.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Dependency intake | Rust YAML 1.2 candidates, exact selection, provenance, licences, transitive risk, and offline rule recorded without workspace dependency mutation. | 2 | Complete |
| Semantic freeze | UTF-8 YAML to NFC JSON-shaped tree boundary, subset, scalars, collisions, ordering, root envelope, defaults, and diagnostics frozen. | 2 | Complete |
| Fixture design | Required valid and invalid parser-only cases carry exact expected trees or diagnostics. | 2 | Complete |
| Regression and evidence verification | Accepted Foundation/PC1 suites pass; provenance, licence, checksum, offline probe, and fixture integrity pass. | 2 | Complete |
| Read-only intake review | Separate read-only pass classifies P0–P3 findings and accepts only with no open P0/P1. | 2 | Complete; no open P0/P1 |

The active allowlist is `docs/pc2/**`, `conformance/pc2/parser/**`, and additive PC2 state entries in `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`. Production crates, root Cargo files, Foundation/PC1 conformance, identities, compilation, package resolution, runtime, builder, planner, providers, user surfaces, and delivery actions remain excluded.

If intake is accepted, the next bounded task is `PC2 parser implementation against the frozen intake and fixtures`. That statement records sequence only; it does not itself authorize implementation.

## PC2 parser implementation tranche

This tranche was authorized separately after the intake was accepted. It implements only the frozen source projection boundary.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Parser package | `threadsmith-compiler` projects one accepted UTF-8 YAML document into the frozen NFC JSON-shaped tree without compiling or creating authority. | 2 | Complete |
| Focused conformance | All frozen valid/invalid fixtures and deterministic edge cases pass through the public parser API. | 2 | Complete |
| Dependency qualification | Exact selected pin and resolved lock match intake; locked/offline graph, checksums, licences, and no-native boundary pass. | 2 | Complete |
| Regression qualification | Formatting, all-target workspace check, Clippy with warnings denied, Foundation, PC1, and PC2 suites pass offline and locked. | 2 | Complete |
| Read-only acceptance | Separate implementation and closure passes have no open P0/P1 finding. | 2 | Complete after repair cycles 1 and 2 |
| Publication | Accepted PC2 tree is committed to and fetched back from remote `main`; remote and local tree identities match. | 0 | Delivery gate |

The next bounded task is `PC3 scope intake and semantic freeze`; it is not authorized by this plan entry. PC2 acceptance does not authorize compiler semantics, resolution, identities, runtime, builder, providers, user surfaces, or release work.

## PC2 Standard reconciliation tranche

This bounded corrective tranche was authorized after the recovered Lattice Standard 0.3 exposed incompatibilities in the accepted PC2 parser boundary. The Standard supersedes the earlier reconstructed PC2 source assumptions where they conflict.

| Gate | Definition of done | Repair limit | State |
|---|---|---:|---|
| Normative reconciliation | Preserve the recovered Standard exactly and classify every accepted-PC2 deviation by lifecycle phase. | 2 | Complete |
| Parser correction | PC2 returns only an NFC JSON-shaped restricted-YAML tree, without source validation or defaults. | 2 | Complete |
| Focused conformance | Standard syntax, information preservation, signed scalars, forbidden YAML, duplicates, collisions, and deterministic output pass through the public API. | 2 | Complete |
| Regression qualification | Formatting, all-target checks, Clippy, Foundation, PC1, PC2, locked/offline, provenance, and documentation consistency pass. | 2 | Complete |
| Read-only acceptance | Separate implementation and closure passes have no open P0/P1 finding. | 2 | Complete after repair cycle 1 |
| Publication | Accepted reconciliation is committed and remote/local `main` tree identities match. | 0 | Delivery gate |

The implementation allowlist is `crates/threadsmith-compiler/src/lib.rs`, its PC2 focused test, `conformance/pc2/parser/**`, `docs/standard/LATTICE_STANDARD_0.3.md`, `docs/pc2/**`, and additive state entries in `PROJECT_STATE.md`, `IMPLEMENTATION_PLAN.md`, and `DECISIONS.md`. Cargo manifests, the lockfile, schema/canonical crates, Foundation/PC1 conformance, identities, package resolution, Lockfiles, Manifests, qualification, Binding, runtime, builder, providers, and user surfaces remain excluded.

Only after this tranche is accepted and published may the next bounded task return to `PC3 scope reconciliation and semantic freeze`. This plan entry does not authorize PC3 implementation.
