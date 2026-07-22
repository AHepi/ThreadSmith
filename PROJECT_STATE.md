# ThreadSmith Project State

State record status: reconstructed. Updated 2026-07-22.

| Field | Value |
|---|---|
| Repository | `AHepi/ThreadSmith` |
| Branch | `main` |
| Historical state supplied by operator | `FOUNDATION_ACCEPTED=true`, `PC1_ACCEPTED=true`, `PC2_STARTED=false` |
| Restoration phase | Accepted Foundation/PC1 provenance tree; Git commit and tag identities are external to this self-referential state file |
| Exact original Git history available | false |
| Byte-exact repository restoration possible | false |
| Recovered workspace shape | Rust virtual workspace with `threadsmith-schema` and `threadsmith-canonical` |
| PC2 started | false |
| Foundation reconstructed baseline accepted | true |
| PC1 reconstructed baseline accepted | true |
| Verification complete | true |
| Separate read-only review complete | true |
| Reconstructed files | 15 |
| Missing or unresolved evidence categories | 9 |
| Current provenance name | `threadsmith-foundation-pc1-reconstructed-0.1` |
| PC2 parser intake started | true |
| PC2 parser semantics frozen | true |
| PC2 implementation started | false |
| PC2 accepted | false |
| Selected parser path | `saphyr-parser =0.0.11`, event API, dependency not yet added |
| Builder authorized | false |
| Runtime authorized | false |
| Next bounded task | PC2 parser implementation against the frozen intake and fixtures |

The recovered files are evidence, not a complete repository snapshot. No entry in this record claims that reconstructed files match the lost workspace byte for byte.

The PC2 intake adds documentation and conformance fixtures only. Foundation/PC1 crates, semantics, manifests, lockfile, identities, canonical-byte rules, and authority boundaries remain unchanged. The parser will be owned by a future `threadsmith-compiler`; `threadsmith-schema` remains limited to schemas and data structures.
