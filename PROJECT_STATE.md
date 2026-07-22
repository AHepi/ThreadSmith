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
| PC2 implementation started | true |
| PC2 accepted | true |
| Selected parser path | `saphyr-parser =0.0.11`, event API, exact pin committed in the workspace lock |
| Builder authorized | false |
| Runtime authorized | false |
| Next bounded task | PC3 scope intake and semantic freeze; not authorized by PC2 acceptance |

The recovered files are evidence, not a complete repository snapshot. No entry in this record claims that reconstructed files match the lost workspace byte for byte.

The accepted PC2 implementation adds `threadsmith-compiler` solely as the owner of UTF-8 restricted-YAML source projection into an NFC-normalized JSON-shaped tree. It adds no compilation, resolution, identity, digest, Manifest, execution, runtime, or builder behavior. Foundation/PC1 code, semantics, identities, canonical-byte rules, authority boundaries, and conformance evidence remain unchanged; `threadsmith-schema` remains limited to schemas and data structures.
