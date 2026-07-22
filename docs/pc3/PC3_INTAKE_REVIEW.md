# PC3 Scope and Semantic-Freeze Read-Only Review

Review date: 2026-07-22.

Review boundary: PC3 scope/freeze documents, fixture manifest, verification evidence, and additive state/plan/decision entries. The review was performed as a separate read-only adversarial pass in the primary workspace; no independent agent context was available.

## Review criteria

- derive PC3 only from the Standard lifecycle;
- prevent `Default`, `Normalize`, `Static check`, identity, resolution, Manifest, qualification, Binding, runtime, and builder behavior from entering PC3;
- preserve the accepted PC2 value and absence information;
- make diagnostics deterministic and fail closed for PC3-owned failures;
- prevent deferred declaration content from being represented as semantically valid;
- cover the user-requested valid, invalid, boundary, regression, and compatibility fixture categories; and
- confirm no accepted code, dependency, conformance, Standard, or ADR file changed.

## Findings

| Severity | Finding | Resolution |
|---|---|---|
| P0 | None. | — |
| P1 | The first fixture manifest made later-phase invalid content explicit but did not explicitly pair it with valid-looking Core declarations or cover all requested deferred categories. This could let an implementation test root checks while overstating fixture completeness. | Repaired in cycle 1 by adding valid-looking and invalid deferred cases for declarations, names, duplicates, references, contracts, ports, links, policies, routes, controls, budgets, secrets, authority, and Extended-only kinds. Added metadata type, optional-list type, and JSON Pointer escaping cases. The 19-case oracle passes. |
| P2 | The Standard requires declaration-name uniqueness and Core profile unit-kind rejection but does not name the exact later lifecycle phase that owns each. | Correctly recorded as unresolved later-phase allocation. PC3 does not emit `SOURCE_DUPLICATE_NAME` or `PROFILE_UNSUPPORTED_UNIT_KIND`; their owning tranche must freeze allocation before implementation. This does not prevent freezing the explicit `Valid root shape` boundary. |
| P3 | None. | — |

## Closure review

The fresh post-repair pass confirmed:

- all 19 fixture outcomes match the frozen independent oracle;
- deferred cases return only `valid_unchanged` plus `semantic_status: deferred`;
- the four PC3 diagnostic codes exactly match the frozen surface;
- PC3 owns no declaration-element, default, identity, package, static-check, Manifest, Binding, runtime, or authority behavior;
- no Rust source, Cargo file, Foundation/PC1/PC2 conformance, Standard, PC2 document, or ADR changed; and
- `git diff --check` passes.

There are no open P0 or P1 findings. The PC3 scope reconciliation and semantic freeze are accepted for the purpose of authorizing a later, separately bounded PC3 implementation task. PC3 product code itself remains unimplemented and unaccepted.
