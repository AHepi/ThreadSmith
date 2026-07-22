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
