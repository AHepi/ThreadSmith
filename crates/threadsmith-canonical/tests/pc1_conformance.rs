use serde::{Deserialize, Serialize};
use serde_json::{Value, json};
use threadsmith_canonical::{
    canonical_bytes, canonical_sha256, identity_claim_from_resolved_preimage,
};
use threadsmith_schema::{ArtifactKind, error_code};

const CANONICAL_VECTORS: &str =
    include_str!("../../../conformance/foundation/canonical_vectors.json");
const CORE_MODEL: &str = include_str!("../../../conformance/pc1/core_model.json");

#[derive(Debug, Deserialize)]
struct VectorSet {
    valid: Vec<ValidVector>,
    invalid: Vec<InvalidVector>,
}

#[derive(Debug, Deserialize)]
struct ValidVector {
    name: String,
    artifact_kind: String,
    input: Value,
    canonical_utf8: String,
    sha256: String,
    identity_claim: String,
}

#[derive(Debug, Deserialize)]
struct InvalidVector {
    name: String,
    input: Value,
    error_code: String,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct PortableCoreModel {
    model_profile: String,
    semantic_profile: String,
    profile_values: ProfileValues,
    source_defaults: SourceDefaults,
    unit_kind_modes: Vec<UnitKindMode>,
    unsupported_unit_kinds: Vec<UnsupportedUnitKind>,
    artifact_roles: Vec<ArtifactRole>,
    blueprint_metadata: BlueprintMetadata,
    manifest_provenance_claims: ManifestProvenanceClaims,
    identity_preimage_status: IdentityPreimageStatus,
    required_static_error_codes: Vec<StaticErrorCode>,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct ProfileValues {
    profile: String,
    contract_max_bytes: u64,
    declaration_max_bytes: u64,
    untrusted_payload_max_bytes: u64,
    model_repair_max: u64,
    control_loop_max_default: u64,
    policy_default: PolicyDefault,
    model_fallback_default: bool,
    commit_order: CommitOrder,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct SourceDefaults {
    input_required: bool,
    input_cardinality: Cardinality,
    input_on_absence: InputAbsence,
    output_cardinality: Cardinality,
    model_repair_attempts: u64,
    link_mode: LinkMode,
    link_delivery: LinkDelivery,
    missing_predicate: bool,
    model_fallback: bool,
    scenario_required: bool,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct UnitKindMode {
    kind: UnitKind,
    mode: UnitMode,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct ArtifactRole {
    role: ArtifactRoleName,
    editable_before_compilation: bool,
    immutable: bool,
    executable_by_itself: bool,
    grants_execution_authority: bool,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct BlueprintMetadata {
    module: String,
    version: String,
    purpose_input: String,
    purpose_normalized: String,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct ManifestProvenanceClaims {
    blueprint_digest: String,
    lock_id: String,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(deny_unknown_fields)]
struct IdentityPreimageStatus {
    blueprint: PreimageState,
    manifest: PreimageState,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum PolicyDefault {
    Deny,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum CommitOrder {
    ActivationIdThenLocalSequence,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum Cardinality {
    One,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum InputAbsence {
    Block,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum LinkMode {
    Data,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum LinkDelivery {
    Multicast,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum UnitKind {
    Program,
    Model,
    Gate,
    Controller,
    Broker,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum UnitMode {
    Stateless,
    EventSourced,
    External,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum UnsupportedUnitKind {
    Adapter,
    Store,
    Subharness,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "snake_case")]
enum ArtifactRoleName {
    Blueprint,
    Manifest,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
enum PreimageState {
    #[serde(rename = "IDENTITY_PREIMAGE_UNRESOLVED")]
    Unresolved,
}

#[derive(Debug, PartialEq, Eq, Serialize, Deserialize)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
enum StaticErrorCode {
    SourceUnknownKey,
    SourceForbiddenYaml,
    SourceDuplicateName,
    ProfileUnsupportedUnitKind,
    ResolveDuplicateVersion,
    ResolveNoCommonVersion,
    ResolveImportCycle,
    NamespaceCollision,
    ContractTooLarge,
    ContractInvalidShape,
    PortUnboundRequired,
    PortTooManyProducers,
    LinkContractIncompatible,
    LinkLabelFlowDenied,
    RouteAmbiguous,
    ControlUnboundedCycle,
    PolicyUnknownOperator,
    ModelDirectEffect,
    BrokerUnsupportedEffect,
    ResourceHashMismatch,
    BudgetInvalid,
    SecretInSource,
    AbiIncompatible,
}

#[test]
fn resolved_preimage_vectors_match_bytes_hashes_and_non_authoritative_claims() {
    let vectors: VectorSet = serde_json::from_str(CANONICAL_VECTORS).unwrap();
    for vector in vectors.valid {
        let kind: ArtifactKind = vector.artifact_kind.parse().unwrap();
        assert_eq!(
            canonical_bytes(&vector.input).unwrap(),
            vector.canonical_utf8.as_bytes(),
            "canonical bytes for {}",
            vector.name
        );
        assert_eq!(
            canonical_sha256(&vector.input).unwrap().to_string(),
            vector.sha256,
            "digest for {}",
            vector.name
        );
        assert_eq!(
            identity_claim_from_resolved_preimage(kind, Some(&vector.input))
                .unwrap()
                .to_string(),
            vector.identity_claim,
            "identity claim for {}",
            vector.name
        );
    }
}

#[test]
fn invalid_canonical_vectors_fail_closed() {
    let vectors: VectorSet = serde_json::from_str(CANONICAL_VECTORS).unwrap();
    for vector in vectors.invalid {
        assert_eq!(
            canonical_bytes(&vector.input).unwrap_err().code(),
            vector.error_code,
            "error code for {}",
            vector.name
        );
    }
}

#[test]
fn recovered_pc1_model_matches_the_complete_strict_schema_vector() {
    let raw: Value = serde_json::from_str(CORE_MODEL).unwrap();
    let model: PortableCoreModel = serde_json::from_value(raw.clone()).unwrap();
    assert_eq!(serde_json::to_value(&model).unwrap(), raw);
    assert_eq!(model.model_profile, "threadsmith-portable-core-model-0.1");
    assert_eq!(model.semantic_profile, "lattice-core-0.1");
    assert_eq!(
        model.profile_values,
        ProfileValues {
            profile: "lattice-core-0.1".to_owned(),
            contract_max_bytes: 4096,
            declaration_max_bytes: 8192,
            untrusted_payload_max_bytes: 1_048_576,
            model_repair_max: 2,
            control_loop_max_default: 3,
            policy_default: PolicyDefault::Deny,
            model_fallback_default: false,
            commit_order: CommitOrder::ActivationIdThenLocalSequence,
        }
    );
    assert_eq!(
        model.source_defaults,
        SourceDefaults {
            input_required: true,
            input_cardinality: Cardinality::One,
            input_on_absence: InputAbsence::Block,
            output_cardinality: Cardinality::One,
            model_repair_attempts: 0,
            link_mode: LinkMode::Data,
            link_delivery: LinkDelivery::Multicast,
            missing_predicate: true,
            model_fallback: false,
            scenario_required: true,
        }
    );
    assert_eq!(
        model.unit_kind_modes,
        vec![
            UnitKindMode {
                kind: UnitKind::Program,
                mode: UnitMode::Stateless,
            },
            UnitKindMode {
                kind: UnitKind::Model,
                mode: UnitMode::Stateless,
            },
            UnitKindMode {
                kind: UnitKind::Gate,
                mode: UnitMode::Stateless,
            },
            UnitKindMode {
                kind: UnitKind::Controller,
                mode: UnitMode::EventSourced,
            },
            UnitKindMode {
                kind: UnitKind::Broker,
                mode: UnitMode::External,
            },
        ]
    );
    assert_eq!(
        model.unsupported_unit_kinds,
        vec![
            UnsupportedUnitKind::Adapter,
            UnsupportedUnitKind::Store,
            UnsupportedUnitKind::Subharness,
        ]
    );
    assert_eq!(
        model.artifact_roles,
        vec![
            ArtifactRole {
                role: ArtifactRoleName::Blueprint,
                editable_before_compilation: true,
                immutable: false,
                executable_by_itself: false,
                grants_execution_authority: false,
            },
            ArtifactRole {
                role: ArtifactRoleName::Manifest,
                editable_before_compilation: false,
                immutable: true,
                executable_by_itself: false,
                grants_execution_authority: false,
            },
        ]
    );
    assert_eq!(
        model.blueprint_metadata,
        BlueprintMetadata {
            module: "tiny_writer".to_owned(),
            version: "1.0.0".to_owned(),
            purpose_input: "Cafe\u{301} response".to_owned(),
            purpose_normalized: "Café response".to_owned(),
        }
    );
    assert_eq!(
        model.manifest_provenance_claims,
        ManifestProvenanceClaims {
            blueprint_digest:
                "lattice:blueprint:sha256:2222222222222222222222222222222222222222222222222222222222222222"
                    .to_owned(),
            lock_id:
                "lattice:lock:sha256:3333333333333333333333333333333333333333333333333333333333333333"
                    .to_owned(),
        }
    );
    assert_eq!(
        model.identity_preimage_status,
        IdentityPreimageStatus {
            blueprint: PreimageState::Unresolved,
            manifest: PreimageState::Unresolved,
        }
    );
    assert_eq!(
        model.required_static_error_codes,
        vec![
            StaticErrorCode::SourceUnknownKey,
            StaticErrorCode::SourceForbiddenYaml,
            StaticErrorCode::SourceDuplicateName,
            StaticErrorCode::ProfileUnsupportedUnitKind,
            StaticErrorCode::ResolveDuplicateVersion,
            StaticErrorCode::ResolveNoCommonVersion,
            StaticErrorCode::ResolveImportCycle,
            StaticErrorCode::NamespaceCollision,
            StaticErrorCode::ContractTooLarge,
            StaticErrorCode::ContractInvalidShape,
            StaticErrorCode::PortUnboundRequired,
            StaticErrorCode::PortTooManyProducers,
            StaticErrorCode::LinkContractIncompatible,
            StaticErrorCode::LinkLabelFlowDenied,
            StaticErrorCode::RouteAmbiguous,
            StaticErrorCode::ControlUnboundedCycle,
            StaticErrorCode::PolicyUnknownOperator,
            StaticErrorCode::ModelDirectEffect,
            StaticErrorCode::BrokerUnsupportedEffect,
            StaticErrorCode::ResourceHashMismatch,
            StaticErrorCode::BudgetInvalid,
            StaticErrorCode::SecretInSource,
            StaticErrorCode::AbiIncompatible,
        ]
    );
}

#[test]
fn pc1_schema_vector_rejects_unknown_missing_and_mistyped_fields() {
    let raw: Value = serde_json::from_str(CORE_MODEL).unwrap();

    let mut unknown = raw.clone();
    unknown
        .as_object_mut()
        .unwrap()
        .insert("pc2_parser".to_owned(), Value::Bool(true));
    assert!(serde_json::from_value::<PortableCoreModel>(unknown).is_err());

    let mut missing = raw.clone();
    missing.as_object_mut().unwrap().remove("source_defaults");
    assert!(serde_json::from_value::<PortableCoreModel>(missing).is_err());

    let mut mistyped = raw.clone();
    mistyped["profile_values"]["model_repair_max"] = json!("2");
    assert!(serde_json::from_value::<PortableCoreModel>(mistyped).is_err());

    let mut unsupported_value = raw;
    unsupported_value["unit_kind_modes"][0]["kind"] = json!("adapter");
    assert!(serde_json::from_value::<PortableCoreModel>(unsupported_value).is_err());
}

#[test]
fn pc1_model_keeps_blueprint_and_manifest_artifact_preimages_unresolved() {
    let model: PortableCoreModel = serde_json::from_str(CORE_MODEL).unwrap();
    assert_eq!(
        model.identity_preimage_status.blueprint,
        PreimageState::Unresolved
    );
    assert_eq!(
        model.identity_preimage_status.manifest,
        PreimageState::Unresolved
    );

    for kind in [ArtifactKind::Blueprint, ArtifactKind::Manifest] {
        assert_eq!(
            identity_claim_from_resolved_preimage(kind, None)
                .unwrap_err()
                .code(),
            error_code::IDENTITY_PREIMAGE_UNRESOLVED
        );
    }
}
