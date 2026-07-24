use serde::Deserialize;
use serde_json::{Map, Value};
use std::collections::{BTreeMap, BTreeSet};
use std::sync::Arc;
use threadsmith_canonical::{canonical_bytes, sha256_digest};
use threadsmith_compiler::{
    DigestedSource, ScannedPackage, ScannedSource, SnapshotAcquisitionError, SnapshotEntry,
    SnapshotName, SnapshotNode, acquire_project_snapshot, apply_blueprint_defaults, digest_source,
    package_scan_diagnostic_codes as codes, parse_blueprint_source, scan_packages,
    validate_blueprint_source,
};

const PLAN_BYTES: &[u8] =
    include_bytes!("../../../../conformance/pc6/package_scan/executable_fixture_plan.json");
const MANIFEST_BYTES: &[u8] =
    include_bytes!("../../../../conformance/pc6/package_scan/fixture_manifest.json");
const AUTHORITY_BYTES: &[u8] = include_bytes!(
    "../../../../docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md"
);
const AUTHORITY_PATH: &str = "docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md";
const AUTHORITY_SHA256: &str = "235ae8026676905b9f410167b18a902cd63dc449ecf073a96821e5d2d40e6c25";
const DATA_CHANGED_IDENTITY: &str =
    "lattice:package:sha256:b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b";
const MODULE_DIGEST: &str = "900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55";

#[derive(Debug, Deserialize, Eq, PartialEq)]
#[serde(deny_unknown_fields)]
struct Authority {
    path: String,
    sha256: String,
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct Plan {
    authority: Authority,
    base_snapshots: BTreeMap<String, Vec<Operation>>,
    byte_expression_vocabulary: Vec<String>,
    cases: Vec<Case>,
    expected_packages: BTreeMap<String, ExpectedPackage>,
    fixture_plan_version: String,
    golden_record_ids: Vec<String>,
    node_vocabulary: Vec<String>,
    operation_vocabulary: Vec<String>,
    relation_vocabulary: Vec<String>,
    source_vocabulary: BTreeMap<String, SourceSpec>,
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct SourceSpec {
    byte_constant: String,
    yaml: String,
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct Case {
    expected_sha256: String,
    fixture_class: String,
    id: String,
    input_sha256: String,
    outcome: Outcome,
    program: Program,
}

#[derive(Debug, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case", deny_unknown_fields)]
enum Program {
    Scan { runs: Vec<Run> },
    Acquisition { acquisition: Acquisition },
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct Run {
    base: String,
    live_operations: Vec<Operation>,
    operations: Vec<Operation>,
    source: String,
    timing: Timing,
}

#[derive(Clone, Copy, Debug, Deserialize, Eq, PartialEq)]
#[serde(rename_all = "snake_case")]
enum Timing {
    Normal,
    MutateAfterAcquisition,
    MutateAfterScan,
}

#[derive(Debug, Deserialize)]
#[serde(tag = "mode", rename_all = "snake_case", deny_unknown_fields)]
enum Acquisition {
    Node { evidence: String, node: NodeSpec },
    ReportedError { error: String, evidence: String },
}

#[derive(Debug, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case", deny_unknown_fields)]
enum Outcome {
    Diagnostic {
        code: String,
        path: String,
    },
    Success {
        relation: Relation,
        run_packages: Vec<Vec<String>>,
    },
    AcquisitionFailure {
        error: String,
    },
}

#[derive(Clone, Copy, Debug, Deserialize, Eq, Ord, PartialEq, PartialOrd)]
#[serde(rename_all = "snake_case")]
enum Relation {
    None,
    EmptyFileExact,
    PhysicalEnumerationIrrelevant,
    HardlinkPathsDistinct,
    UnlistedNotRetained,
    UnrelatedRootExcluded,
    CanonicalPresentationEquivalent,
    DistinctIdentities,
    Pc6DoesNotParseModule,
    Pc6OnlySurface,
    ExactSourceBinding,
    SourceSwapUnavailable,
    IdentityContentSwapUnavailable,
    RepeatEqual,
    LiveSnapshotStable,
    LaterConsumesRetained,
    CanonicalBytesDerived,
    CanonicalCacheNotSemantic,
    VerifiedBytesImmutable,
}

impl Relation {
    fn as_str(self) -> &'static str {
        match self {
            Self::None => "none",
            Self::EmptyFileExact => "empty_file_exact",
            Self::PhysicalEnumerationIrrelevant => "physical_enumeration_irrelevant",
            Self::HardlinkPathsDistinct => "hardlink_paths_distinct",
            Self::UnlistedNotRetained => "unlisted_not_retained",
            Self::UnrelatedRootExcluded => "unrelated_root_excluded",
            Self::CanonicalPresentationEquivalent => "canonical_presentation_equivalent",
            Self::DistinctIdentities => "distinct_identities",
            Self::Pc6DoesNotParseModule => "pc6_does_not_parse_module",
            Self::Pc6OnlySurface => "pc6_only_surface",
            Self::ExactSourceBinding => "exact_source_binding",
            Self::SourceSwapUnavailable => "source_swap_unavailable",
            Self::IdentityContentSwapUnavailable => "identity_content_swap_unavailable",
            Self::RepeatEqual => "repeat_equal",
            Self::LiveSnapshotStable => "live_snapshot_stable",
            Self::LaterConsumesRetained => "later_consumes_retained",
            Self::CanonicalBytesDerived => "canonical_bytes_derived",
            Self::CanonicalCacheNotSemantic => "canonical_cache_not_semantic",
            Self::VerifiedBytesImmutable => "verified_bytes_immutable",
        }
    }
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct ExpectedPackage {
    canonical_vector: Option<String>,
    files: Vec<ExpectedFile>,
    identity: String,
    lattice: String,
    module_file: String,
    package: String,
    profiles: Vec<String>,
    version: String,
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct ExpectedFile {
    byte_constant: String,
    path: String,
    sha256: String,
}

#[derive(Debug, Deserialize)]
#[serde(tag = "op", rename_all = "snake_case", deny_unknown_fields)]
enum Operation {
    Add {
        node: NodeSpec,
        path: String,
    },
    Remove {
        path: String,
    },
    ReplaceNode {
        node: NodeSpec,
        path: String,
    },
    ReplaceHex {
        bytes: ByteExpression,
        path: String,
    },
    SetDescriptor {
        bytes: ByteExpression,
        path: String,
    },
    Rename {
        new_final_component: String,
        path: String,
    },
    SetChildEnumeration {
        names: Vec<String>,
        path: String,
    },
    ShareHardlink {
        group_id: String,
        path_a: String,
        path_b: String,
    },
}

impl Operation {
    fn vocabulary_name(&self) -> &'static str {
        match self {
            Self::Add { .. } => "ADD",
            Self::Remove { .. } => "REMOVE",
            Self::ReplaceNode { .. } => "REPLACE_NODE",
            Self::ReplaceHex { .. } => "REPLACE_HEX",
            Self::SetDescriptor { .. } => "SET_DESCRIPTOR",
            Self::Rename { .. } => "RENAME",
            Self::SetChildEnumeration { .. } => "SET_CHILD_ENUMERATION",
            Self::ShareHardlink { .. } => "SHARE_HARDLINK",
        }
    }
}

#[derive(Debug, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case", deny_unknown_fields)]
enum NodeSpec {
    Directory {
        children: Vec<RawEntry>,
    },
    DirectoryUnreadable,
    Regular {
        bytes: ByteExpression,
        hardlink_group: Option<String>,
    },
    RegularUnreadable,
    Link {
        target: String,
    },
    Special {
        special_kind: String,
    },
}

impl NodeSpec {
    fn vocabulary_name(&self) -> &'static str {
        match self {
            Self::Directory { .. } => "directory",
            Self::DirectoryUnreadable => "directory_unreadable",
            Self::Regular { .. } => "regular",
            Self::RegularUnreadable => "regular_unreadable",
            Self::Link { .. } => "link",
            Self::Special { .. } => "special",
        }
    }
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct RawEntry {
    name: NameSpec,
    node: NodeSpec,
}

#[derive(Debug, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case", deny_unknown_fields)]
enum NameSpec {
    Unicode { value: String },
    UnixBytes { hex: String },
    WindowsUtf16 { units: Vec<u16> },
}

#[derive(Debug, Deserialize)]
#[serde(tag = "kind", rename_all = "snake_case", deny_unknown_fields)]
enum ByteExpression {
    Constant {
        name: String,
    },
    Hex {
        value: String,
    },
    Utf8 {
        value: String,
    },
    Concat {
        parts: Vec<ByteExpression>,
    },
    ReplaceUtf8 {
        new: String,
        old: String,
        source: Box<ByteExpression>,
    },
    InsertUtf8After {
        anchor: String,
        source: Box<ByteExpression>,
        text: String,
    },
    InsertBytesAfter {
        anchor: Box<ByteExpression>,
        bytes: Box<ByteExpression>,
        source: Box<ByteExpression>,
    },
    DeleteUtf8Exact {
        source: Box<ByteExpression>,
        text: String,
    },
    Bd {
        files: Vec<BdFile>,
        module_file: String,
        package: String,
        profiles: Vec<String>,
        version: String,
    },
    Bdp {
        path_scalar_source: String,
    },
    Bdf {
        files: Vec<BdfFile>,
        module_file_scalar_source: String,
    },
}

impl ByteExpression {
    fn vocabulary_name(&self) -> &'static str {
        match self {
            Self::Constant { .. } => "constant",
            Self::Hex { .. } => "hex",
            Self::Utf8 { .. } => "utf8",
            Self::Concat { .. } => "concat",
            Self::ReplaceUtf8 { .. } => "replace_utf8",
            Self::InsertUtf8After { .. } => "insert_utf8_after",
            Self::InsertBytesAfter { .. } => "insert_bytes_after",
            Self::DeleteUtf8Exact { .. } => "delete_utf8_exact",
            Self::Bd { .. } => "bd",
            Self::Bdp { .. } => "bdp",
            Self::Bdf { .. } => "bdf",
        }
    }
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct BdFile {
    path: String,
    sha256: String,
}

#[derive(Debug, Deserialize)]
#[serde(deny_unknown_fields)]
struct BdfFile {
    path_scalar_source: String,
    sha256_scalar_source: String,
}

#[derive(Clone, Debug)]
enum VirtualNode {
    Directory(VirtualDirectory),
    DirectoryUnreadable,
    Regular {
        bytes: Vec<u8>,
        hardlink_group: Option<String>,
    },
    RegularUnreadable,
    Link,
    Special,
}

#[derive(Clone, Debug)]
struct VirtualDirectory {
    children: BTreeMap<String, VirtualNode>,
    enumeration: Vec<String>,
}

impl VirtualDirectory {
    fn empty() -> Self {
        Self {
            children: BTreeMap::new(),
            enumeration: Vec::new(),
        }
    }
}

#[derive(Default)]
struct Coverage {
    bases: BTreeSet<String>,
    byte_expressions: BTreeSet<String>,
    cases: BTreeSet<String>,
    constants: BTreeSet<String>,
    diagnostic_codes: BTreeSet<String>,
    expected_packages: BTreeSet<String>,
    result_packages: BTreeSet<String>,
    nodes: BTreeSet<String>,
    operations: BTreeSet<String>,
    relations: BTreeSet<String>,
    sources: BTreeSet<String>,
    vectors: BTreeSet<String>,
}

pub fn execute_all() {
    let manifest: Value = serde_json::from_slice(MANIFEST_BYTES)
        .expect("the accepted PC6 fixture manifest must remain valid JSON");
    super::validate_fixture_manifest(&manifest)
        .expect("the accepted PC6 fixture manifest must remain fail-closed");
    validate_manifest_shape(&manifest);

    let plan: Plan = serde_json::from_slice(PLAN_BYTES)
        .expect("the executable PC6 fixture plan must match its closed schema");
    validate_plan_header(&plan, &manifest);

    let constants = load_constants(&manifest);
    let vectors = load_vectors(&manifest);
    let mut coverage = Coverage::default();
    validate_expected_package_catalogue(&plan, &manifest, &constants, &vectors, &mut coverage);
    validate_manifest_expectations(&manifest);

    let fixtures = manifest["fixtures"]
        .as_array()
        .expect("fixtures must be an array");
    let mut cases = BTreeMap::new();
    for case in &plan.cases {
        assert!(
            cases.insert(case.id.as_str(), case).is_none(),
            "duplicate executable fixture case {}",
            case.id
        );
    }
    assert_eq!(cases.len(), 184, "executable fixture case count changed");

    for fixture in fixtures {
        let fixture = fixture
            .as_object()
            .expect("every authoritative fixture must be an object");
        assert_exact_keys(
            fixture,
            &[
                "diagnostic_expectations",
                "exact_input",
                "expected",
                "expected_diagnostic",
                "fixture_class",
                "id",
            ],
            "authoritative fixture",
        );
        let id = required_str(fixture, "id", "fixture");
        let case = cases
            .remove(id)
            .unwrap_or_else(|| panic!("authoritative fixture {id} has no executable case"));
        bind_case_to_authoritative_row(case, fixture);
        assert!(
            coverage.cases.insert(id.to_owned()),
            "fixture {id} was executed more than once"
        );
        execute_case(case, &plan, &constants, &vectors, &mut coverage);
    }
    assert!(
        cases.is_empty(),
        "unreachable executable fixture cases remain"
    );

    assert_complete_coverage(&plan, &constants, &vectors, &coverage);
}

fn validate_manifest_shape(manifest: &Value) {
    let root = manifest
        .as_object()
        .expect("fixture manifest root must be an object");
    assert_exact_keys(
        root,
        &[
            "authority",
            "authoritative_byte_constants",
            "canonical_package_vectors",
            "counts",
            "diagnostic_codes",
            "diagnostic_expectations",
            "fixture_class_vocabulary",
            "fixture_manifest_version",
            "fixtures",
            "golden",
            "package_identities",
            "populations",
        ],
        "fixture manifest",
    );
    let authority = root["authority"]
        .as_object()
        .expect("manifest authority must be an object");
    assert_exact_keys(authority, &["path", "sha256"], "manifest authority");
    let counts = root["counts"]
        .as_object()
        .expect("manifest counts must be an object");
    assert_exact_keys(
        counts,
        &[
            "authoritative_byte_constants",
            "canonical_package_vectors",
            "descriptor_presentations",
            "diagnostic_codes",
            "diagnostic_expectations",
            "fixtures",
            "package_identities",
            "path_scalar_vectors",
            "pointer_vectors",
        ],
        "manifest counts",
    );
    let golden = root["golden"]
        .as_object()
        .expect("manifest golden values must be an object");
    assert_exact_keys(
        golden,
        &[
            "data_changed_identity",
            "hard_link_identity",
            "minimal_identity",
            "multi_file_identity",
            "numeric_10_identity",
            "numeric_2_identity",
            "opaque_identity",
        ],
        "manifest golden values",
    );

    let populations = root["populations"]
        .as_object()
        .expect("manifest populations must be an object");
    assert_exact_keys(
        populations,
        &[
            "descriptor_presentations",
            "path_scalar_vectors",
            "pointer_vectors",
        ],
        "manifest populations",
    );
    assert_population_ids(manifest, "descriptor_presentations", 18);
    assert_population_ids(manifest, "path_scalar_vectors", 18);
    assert_population_ids(manifest, "pointer_vectors", 6);
}

fn validate_plan_header(plan: &Plan, manifest: &Value) {
    assert_eq!(
        plan.fixture_plan_version, "pc6-package-scan-executable-plan-1",
        "unknown executable fixture-plan version"
    );
    let manifest_authority = Authority {
        path: manifest["authority"]["path"]
            .as_str()
            .expect("manifest authority path invalid")
            .to_owned(),
        sha256: manifest["authority"]["sha256"]
            .as_str()
            .expect("manifest authority hash invalid")
            .to_owned(),
    };
    assert_eq!(
        plan.authority, manifest_authority,
        "plan authority differs from manifest authority"
    );
    assert_eq!(plan.authority.path, AUTHORITY_PATH);
    assert_eq!(plan.authority.sha256, AUTHORITY_SHA256);
    assert_eq!(
        sha256_digest(AUTHORITY_BYTES).to_hex(),
        AUTHORITY_SHA256,
        "accepted Package Scan erratum bytes changed"
    );

    assert_vocabulary(
        &plan.byte_expression_vocabulary,
        &[
            "constant",
            "hex",
            "utf8",
            "concat",
            "replace_utf8",
            "insert_utf8_after",
            "insert_bytes_after",
            "delete_utf8_exact",
            "bd",
            "bdp",
            "bdf",
        ],
        "byte-expression",
    );
    assert_vocabulary(
        &plan.node_vocabulary,
        &[
            "directory",
            "directory_unreadable",
            "regular",
            "regular_unreadable",
            "link",
            "special",
        ],
        "node",
    );
    assert_vocabulary(
        &plan.operation_vocabulary,
        &[
            "USE_SOURCE",
            "USE_BASE",
            "ADD",
            "REMOVE",
            "REPLACE_NODE",
            "REPLACE_HEX",
            "REPLACE_UTF8",
            "INSERT_UTF8_AFTER",
            "DELETE_UTF8_EXACT",
            "SET_DESCRIPTOR",
            "RENAME",
            "SET_CHILD_ENUMERATION",
            "SHARE_HARDLINK",
            "SNAPSHOT_ACQUISITION_FAILURE",
            "LIVE_MUTATION",
        ],
        "operation",
    );
    assert_vocabulary(
        &plan.relation_vocabulary,
        &[
            "none",
            "empty_file_exact",
            "physical_enumeration_irrelevant",
            "hardlink_paths_distinct",
            "unlisted_not_retained",
            "unrelated_root_excluded",
            "canonical_presentation_equivalent",
            "distinct_identities",
            "pc6_does_not_parse_module",
            "pc6_only_surface",
            "exact_source_binding",
            "source_swap_unavailable",
            "identity_content_swap_unavailable",
            "repeat_equal",
            "live_snapshot_stable",
            "later_consumes_retained",
            "canonical_bytes_derived",
            "canonical_cache_not_semantic",
            "verified_bytes_immutable",
        ],
        "relation",
    );

    assert_eq!(
        plan.source_vocabulary
            .keys()
            .map(String::as_str)
            .collect::<Vec<_>>(),
        ["DS-A", "DS-B"],
        "source vocabulary changed"
    );
    assert_eq!(
        plan.base_snapshots
            .keys()
            .map(String::as_str)
            .collect::<Vec<_>>(),
        [
            "T-ABSENT",
            "T-EMPTY",
            "T-HARDLINK",
            "T-MINIMAL",
            "T-MULTI-FILE",
            "T-MULTIPLE-PACKAGES",
            "T-MULTIPLE-VERSIONS",
            "T-VERSION-ORDER",
        ],
        "base-snapshot vocabulary changed"
    );
}

fn assert_population_ids(manifest: &Value, population: &str, expected_count: usize) {
    let fixtures = manifest["fixtures"]
        .as_array()
        .expect("fixtures must be an array")
        .iter()
        .map(|fixture| fixture["id"].as_str().expect("fixture ID must be a string"))
        .collect::<BTreeSet<_>>();
    let values = manifest["populations"][population]
        .as_array()
        .unwrap_or_else(|| panic!("{population} must be an array"));
    assert_eq!(values.len(), expected_count, "{population} count changed");
    let mut unique = BTreeSet::new();
    for value in values {
        let id = value
            .as_str()
            .unwrap_or_else(|| panic!("{population} member must be a fixture ID"));
        assert!(unique.insert(id), "duplicate {population} member {id}");
        assert!(
            fixtures.contains(id),
            "{population} references missing fixture {id}"
        );
    }
}

fn assert_vocabulary(actual: &[String], expected: &[&str], name: &str) {
    assert_eq!(
        actual.iter().map(String::as_str).collect::<Vec<_>>(),
        expected,
        "{name} vocabulary changed"
    );
    assert_eq!(
        actual.iter().collect::<BTreeSet<_>>().len(),
        actual.len(),
        "{name} vocabulary contains duplicates"
    );
}

fn load_constants(manifest: &Value) -> BTreeMap<String, Vec<u8>> {
    let records = manifest["authoritative_byte_constants"]
        .as_array()
        .expect("authoritative byte constants must be an array");
    assert_eq!(records.len(), 34, "byte-constant count changed");
    let mut constants = BTreeMap::new();
    for record in records {
        let record = record
            .as_object()
            .expect("byte-constant record must be an object");
        assert_exact_keys(
            record,
            &["hex", "length", "name", "sha256"],
            "byte-constant record",
        );
        let name = required_str(record, "name", "byte-constant record");
        let bytes = decode_lower_hex(required_str(record, "hex", name), name);
        assert_eq!(
            record["length"].as_u64(),
            Some(bytes.len() as u64),
            "{name} byte length changed"
        );
        assert_eq!(
            sha256_digest(&bytes).to_hex(),
            required_str(record, "sha256", name),
            "{name} byte hash changed"
        );
        assert!(
            constants.insert(name.to_owned(), bytes).is_none(),
            "duplicate byte constant {name}"
        );
    }
    constants
}

fn load_vectors(manifest: &Value) -> BTreeMap<String, Vec<u8>> {
    let records = manifest["canonical_package_vectors"]
        .as_array()
        .expect("canonical package vectors must be an array");
    assert_eq!(records.len(), 6, "canonical-vector count changed");
    let mut vectors = BTreeMap::new();
    for record in records {
        let record = record
            .as_object()
            .expect("canonical-vector record must be an object");
        assert_exact_keys(
            record,
            &["canonical_hex", "identity", "length", "name", "sha256"],
            "canonical-vector record",
        );
        let name = required_str(record, "name", "canonical-vector record");
        let bytes = decode_lower_hex(required_str(record, "canonical_hex", name), name);
        let digest = sha256_digest(&bytes).to_hex();
        assert_eq!(
            record["length"].as_u64(),
            Some(bytes.len() as u64),
            "{name} canonical length changed"
        );
        assert_eq!(required_str(record, "sha256", name), digest);
        assert_eq!(
            required_str(record, "identity", name),
            format!("lattice:package:sha256:{digest}")
        );
        assert!(
            vectors.insert(name.to_owned(), bytes).is_none(),
            "duplicate canonical vector {name}"
        );
    }
    vectors
}

fn validate_expected_package_catalogue(
    plan: &Plan,
    manifest: &Value,
    constants: &BTreeMap<String, Vec<u8>>,
    vectors: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
) {
    assert_eq!(
        plan.expected_packages.len(),
        22,
        "complete expected-package catalogue changed"
    );
    let record_ids = plan
        .expected_packages
        .keys()
        .map(String::as_str)
        .collect::<BTreeSet<_>>();
    let golden_ids = plan
        .golden_record_ids
        .iter()
        .map(String::as_str)
        .collect::<BTreeSet<_>>();
    assert_eq!(
        golden_ids.len(),
        plan.golden_record_ids.len(),
        "duplicate golden record ID"
    );
    assert_eq!(
        golden_ids, record_ids,
        "unreachable or unlisted expected-package record"
    );

    for (record_id, record) in &plan.expected_packages {
        coverage.expected_packages.insert(record_id.clone());
        let canonical = canonical_expected_descriptor(record);
        let digest = sha256_digest(&canonical).to_hex();
        assert_eq!(
            record.identity,
            format!("lattice:package:sha256:{digest}"),
            "{record_id} package identity is not reproducible"
        );
        for file in &record.files {
            coverage.constants.insert(file.byte_constant.clone());
            let bytes = constants.get(&file.byte_constant).unwrap_or_else(|| {
                panic!(
                    "{record_id} references missing byte constant {}",
                    file.byte_constant
                )
            });
            assert_eq!(
                sha256_digest(bytes).to_hex(),
                file.sha256,
                "{record_id} file digest differs at {}",
                file.path
            );
        }
        if let Some(vector_name) = &record.canonical_vector {
            coverage.vectors.insert(vector_name.clone());
            let vector = vectors.get(vector_name).unwrap_or_else(|| {
                panic!("{record_id} references missing canonical vector {vector_name}")
            });
            assert_eq!(
                canonical.as_slice(),
                vector.as_slice(),
                "{record_id} differs from canonical vector {vector_name}"
            );
        }
    }

    let canonical_records = ["minimal", "multi_file", "hard_link"];
    let additional = plan
        .expected_packages
        .iter()
        .filter(|(record_id, _)| !canonical_records.contains(&record_id.as_str()))
        .map(|(_, record)| record.identity.as_str())
        .collect::<BTreeSet<_>>();
    let manifest_identities = manifest["package_identities"]
        .as_array()
        .expect("package identities must be an array")
        .iter()
        .map(|value| value.as_str().expect("package identity must be a string"))
        .collect::<BTreeSet<_>>();
    assert_eq!(manifest_identities.len(), 19);
    assert_eq!(
        additional, manifest_identities,
        "the 19 additional package identities are not reproduced"
    );

    let data_changed = &plan.expected_packages["data_changed"];
    assert_eq!(data_changed.identity, DATA_CHANGED_IDENTITY);
    let data_changed_vector = canonical_expected_descriptor(data_changed);
    assert_eq!(
        data_changed_vector.len(),
        318,
        "DATA_CHANGED canonical byte length changed"
    );
    let data_changed_digest = DATA_CHANGED_IDENTITY
        .strip_prefix("lattice:package:sha256:")
        .expect("DATA_CHANGED identity prefix changed");
    assert_eq!(
        sha256_digest(&data_changed_vector).to_hex(),
        data_changed_digest
    );

    let golden = manifest["golden"]
        .as_object()
        .expect("golden records must be an object");
    assert_eq!(
        required_str(golden, "data_changed_identity", "golden"),
        DATA_CHANGED_IDENTITY
    );
    for (golden_key, record_id) in [
        ("minimal_identity", "minimal"),
        ("multi_file_identity", "multi_file"),
        ("hard_link_identity", "hard_link"),
        ("numeric_2_identity", "alpha_2_0_0"),
        ("numeric_10_identity", "alpha_10_0_0"),
        ("opaque_identity", "module_opaque"),
    ] {
        assert_eq!(
            required_str(golden, golden_key, "golden"),
            plan.expected_packages[record_id].identity.as_str()
        );
    }
}

fn validate_manifest_expectations(manifest: &Value) {
    let fixtures = manifest["fixtures"]
        .as_array()
        .expect("fixtures must be an array");
    let fixture_by_id = fixtures
        .iter()
        .map(|fixture| (fixture["id"].as_str().expect("fixture ID invalid"), fixture))
        .collect::<BTreeMap<_, _>>();
    let expectations = manifest["diagnostic_expectations"]
        .as_array()
        .expect("diagnostic expectations must be an array");
    assert_eq!(
        expectations.len(),
        124,
        "diagnostic-expectation count changed"
    );
    let valid_codes = manifest["diagnostic_codes"]
        .as_array()
        .expect("diagnostic codes must be an array")
        .iter()
        .map(|value| value.as_str().expect("diagnostic code invalid"))
        .collect::<BTreeSet<_>>();
    let mut unique = BTreeSet::new();
    for expectation in expectations {
        let expectation = expectation
            .as_object()
            .expect("diagnostic expectation must be an object");
        assert_exact_keys(
            expectation,
            &["code", "id", "path"],
            "diagnostic expectation",
        );
        let id = required_str(expectation, "id", "diagnostic expectation");
        let code = required_str(expectation, "code", id);
        let path = required_str(expectation, "path", id);
        assert!(!path.is_empty(), "diagnostic expectation {id} has no path");
        assert!(
            valid_codes.contains(code),
            "diagnostic expectation {id} has unknown code {code}"
        );
        assert!(
            unique.insert((id, code, path)),
            "duplicate diagnostic expectation for {id}"
        );
        let fixture = fixture_by_id
            .get(id)
            .unwrap_or_else(|| panic!("diagnostic expectation references missing fixture {id}"));
        assert!(
            fixture["diagnostic_expectations"]
                .as_array()
                .expect("fixture diagnostic expectations must be an array")
                .iter()
                .any(|candidate| {
                    let candidate = candidate
                        .as_object()
                        .expect("fixture diagnostic expectation must be an object");
                    assert_exact_keys(
                        candidate,
                        &["code", "path"],
                        "fixture diagnostic expectation",
                    );
                    candidate["code"].as_str() == Some(code)
                        && candidate["path"].as_str() == Some(path)
                }),
            "diagnostic expectation for {id} is unreachable"
        );
    }
    let mut local_expectations = BTreeSet::new();
    let mut local_count = 0;
    for fixture in fixtures {
        let id = fixture["id"].as_str().expect("fixture ID invalid");
        for expectation in fixture["diagnostic_expectations"]
            .as_array()
            .expect("fixture diagnostic expectations must be an array")
        {
            let expectation = expectation
                .as_object()
                .expect("fixture diagnostic expectation must be an object");
            assert_exact_keys(
                expectation,
                &["code", "path"],
                "fixture diagnostic expectation",
            );
            let code = required_str(expectation, "code", id);
            let path = required_str(expectation, "path", id);
            assert!(!path.is_empty(), "{id} has an empty diagnostic path");
            assert!(
                valid_codes.contains(code),
                "{id} has an undeclared diagnostic code {code}"
            );
            assert!(
                local_expectations.insert((id, code, path)),
                "{id} contains a duplicate diagnostic expectation"
            );
            local_count += 1;
        }
    }
    assert_eq!(local_count, 124, "fixture diagnostic ledger count changed");
    assert_eq!(
        local_expectations, unique,
        "fixture and top-level diagnostic ledgers differ"
    );
}

fn bind_case_to_authoritative_row(case: &Case, fixture: &Map<String, Value>) {
    let id = required_str(fixture, "id", "fixture");
    assert_eq!(case.id, id);
    assert_eq!(
        case.fixture_class,
        required_str(fixture, "fixture_class", id),
        "{id} fixture class changed"
    );
    let exact_input = required_str(fixture, "exact_input", id);
    let expected = required_str(fixture, "expected", id);
    assert_eq!(
        case.input_sha256,
        sha256_digest(exact_input.as_bytes()).to_hex(),
        "{id} executable input is not bound to its authoritative notation"
    );
    assert_eq!(
        case.expected_sha256,
        sha256_digest(expected.as_bytes()).to_hex(),
        "{id} executable outcome is not bound to its authoritative notation"
    );
    match &case.outcome {
        Outcome::Diagnostic { code, path } => {
            assert!(!path.is_empty(), "{id} diagnostic path is incomplete");
            let expected_diagnostic = fixture["expected_diagnostic"]
                .as_object()
                .unwrap_or_else(|| panic!("{id} is missing its expected diagnostic"));
            assert_exact_keys(
                expected_diagnostic,
                &["code", "path"],
                "primary expected diagnostic",
            );
            assert_eq!(expected_diagnostic["code"].as_str(), Some(code.as_str()));
            assert_eq!(expected_diagnostic["path"].as_str(), Some(path.as_str()));
        }
        Outcome::Success { .. } | Outcome::AcquisitionFailure { .. } => {
            assert!(
                fixture["expected_diagnostic"].is_null(),
                "{id} unexpectedly discards a diagnostic expectation"
            );
        }
    }
}

fn execute_case(
    case: &Case,
    plan: &Plan,
    constants: &BTreeMap<String, Vec<u8>>,
    vectors: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
) {
    match (&case.program, &case.outcome) {
        (Program::Acquisition { acquisition }, Outcome::AcquisitionFailure { error }) => {
            coverage
                .operations
                .insert("SNAPSHOT_ACQUISITION_FAILURE".to_owned());
            execute_acquisition_failure(&case.id, acquisition, error, constants, coverage);
        }
        (Program::Scan { runs }, Outcome::Diagnostic { code, path }) => {
            assert_eq!(
                runs.len(),
                1,
                "{} diagnostic fixture must have exactly one run",
                case.id
            );
            let result = execute_scan_run(&case.id, &runs[0], plan, constants, coverage);
            match result {
                Ok(scanned) => panic!(
                    "{} unexpectedly returned {} successful packages instead of {code} at {path}",
                    case.id,
                    scanned.packages().len()
                ),
                Err(diagnostic) => {
                    assert_eq!(
                        diagnostic.code(),
                        code,
                        "{} diagnostic code changed",
                        case.id
                    );
                    assert_eq!(
                        diagnostic.path(),
                        path,
                        "{} complete rendered diagnostic path changed",
                        case.id
                    );
                    coverage.diagnostic_codes.insert(code.clone());
                }
            }
        }
        (
            Program::Scan { runs },
            Outcome::Success {
                relation,
                run_packages,
            },
        ) => {
            assert_eq!(
                runs.len(),
                run_packages.len(),
                "{} has incomplete successful run expectations",
                case.id
            );
            coverage.relations.insert(relation.as_str().to_owned());
            let mut results = Vec::with_capacity(runs.len());
            let comparison_inputs = ScannedSourceComparisonInputs {
                plan,
                constants,
                vectors,
            };
            for (index, (run, expected_ids)) in runs.iter().zip(run_packages).enumerate() {
                let result = execute_scan_run(&case.id, run, plan, constants, coverage);
                let scanned = result.unwrap_or_else(|diagnostic| {
                    panic!(
                        "{} run {index} unexpectedly returned {} at {}",
                        case.id,
                        diagnostic.code(),
                        diagnostic.path()
                    )
                });
                compare_scanned_source(
                    &case.id,
                    index,
                    &scanned,
                    expected_ids,
                    &comparison_inputs,
                    coverage,
                );
                results.push(scanned);
            }
            assert_relation(&case.id, *relation, &results, constants);
        }
        (Program::Acquisition { .. }, _) => {
            panic!(
                "{} acquisition program has a non-acquisition outcome",
                case.id
            )
        }
        (Program::Scan { .. }, Outcome::AcquisitionFailure { .. }) => {
            panic!("{} scan program has an acquisition outcome", case.id)
        }
    }
}

fn execute_acquisition_failure(
    fixture_id: &str,
    acquisition: &Acquisition,
    expected_error: &str,
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
) {
    let expected = acquisition_error(expected_error);
    let result = match acquisition {
        Acquisition::Node { evidence, node } => {
            assert!(
                !evidence.is_empty(),
                "{fixture_id} acquisition evidence is empty"
            );
            let mut hardlinks = BTreeMap::new();
            let snapshot_node = materialize_raw_node(node, constants, coverage, &mut hardlinks);
            acquire_project_snapshot(Ok(Some(snapshot_node)))
        }
        Acquisition::ReportedError { error, evidence } => {
            assert!(
                !evidence.is_empty(),
                "{fixture_id} acquisition evidence is empty"
            );
            let reported = acquisition_error(error);
            assert_eq!(
                reported, expected,
                "{fixture_id} reported and expected acquisition errors differ"
            );
            acquire_project_snapshot(Err(reported))
        }
    };
    match result {
        Ok(_) => panic!("{fixture_id} unexpectedly acquired a snapshot"),
        Err(actual) => assert_eq!(actual, expected, "{fixture_id} acquisition failure changed"),
    }
}

fn acquisition_error(value: &str) -> SnapshotAcquisitionError {
    match value {
        "UnrepresentableNativeName" => SnapshotAcquisitionError::UnrepresentableNativeName,
        "MalformedUtf16Name" => SnapshotAcquisitionError::MalformedUtf16Name,
        "InvalidPortableName" => SnapshotAcquisitionError::InvalidPortableName,
        "NfcNameCollision" => SnapshotAcquisitionError::NfcNameCollision,
        "NamespaceAlias" => SnapshotAcquisitionError::NamespaceAlias,
        "IncompleteImmutableView" => SnapshotAcquisitionError::IncompleteImmutableView,
        "ConcurrentMutation" => SnapshotAcquisitionError::ConcurrentMutation,
        "ResourceExhaustion" => SnapshotAcquisitionError::ResourceExhaustion,
        "InconsistentObjectReference" => SnapshotAcquisitionError::InconsistentObjectReference,
        other => panic!("undeclared acquisition error {other}"),
    }
}

fn execute_scan_run(
    fixture_id: &str,
    run: &Run,
    plan: &Plan,
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
) -> Result<ScannedSource, threadsmith_compiler::PackageScanDiagnostic> {
    coverage.operations.insert("USE_SOURCE".to_owned());
    coverage.operations.insert("USE_BASE".to_owned());
    coverage.sources.insert(run.source.clone());
    coverage.bases.insert(run.base.clone());
    let source = build_source(fixture_id, &run.source, plan, constants, coverage);

    let base = plan
        .base_snapshots
        .get(&run.base)
        .unwrap_or_else(|| panic!("{fixture_id} references missing base {}", run.base));
    let mut root = VirtualNode::Directory(VirtualDirectory::empty());
    for (index, operation) in base.iter().enumerate() {
        apply_operation(
            &mut root,
            operation,
            constants,
            coverage,
            &format!("{fixture_id}.base[{index}]"),
        );
    }
    for (index, operation) in run.operations.iter().enumerate() {
        apply_operation(
            &mut root,
            operation,
            constants,
            coverage,
            &format!("{fixture_id}.operations[{index}]"),
        );
    }

    let packages = exact_packages_lookup(&root);
    let snapshot = acquire_project_snapshot(Ok(packages))
        .unwrap_or_else(|error| panic!("{fixture_id} unexpected acquisition failure: {error}"));

    match run.timing {
        Timing::Normal => assert!(
            run.live_operations.is_empty(),
            "{fixture_id} normal run contains a live mutation"
        ),
        Timing::MutateAfterAcquisition => {
            coverage.operations.insert("LIVE_MUTATION".to_owned());
            apply_live_operations(
                fixture_id,
                &mut root,
                &run.live_operations,
                constants,
                coverage,
            );
        }
        Timing::MutateAfterScan => {
            coverage.operations.insert("LIVE_MUTATION".to_owned());
        }
    }

    let expected_source = source.clone();
    let result = scan_packages(source, snapshot);
    if let Ok(scanned) = &result {
        assert_eq!(
            scanned.digested_source(),
            &expected_source,
            "{fixture_id} successful result is not bound to its exact source"
        );
    }
    if run.timing == Timing::MutateAfterScan {
        apply_live_operations(
            fixture_id,
            &mut root,
            &run.live_operations,
            constants,
            coverage,
        );
    }
    result
}

fn apply_live_operations(
    fixture_id: &str,
    root: &mut VirtualNode,
    operations: &[Operation],
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
) {
    assert!(
        !operations.is_empty(),
        "{fixture_id} live-mutation timing has no mutation"
    );
    for (index, operation) in operations.iter().enumerate() {
        apply_operation(
            root,
            operation,
            constants,
            coverage,
            &format!("{fixture_id}.live_operations[{index}]"),
        );
    }
}

fn assert_relation(
    fixture_id: &str,
    relation: Relation,
    results: &[ScannedSource],
    constants: &BTreeMap<String, Vec<u8>>,
) {
    match relation {
        Relation::None
        | Relation::PhysicalEnumerationIrrelevant
        | Relation::UnlistedNotRetained
        | Relation::UnrelatedRootExcluded
        | Relation::CanonicalPresentationEquivalent
        | Relation::Pc6DoesNotParseModule
        | Relation::Pc6OnlySurface
        | Relation::SourceSwapUnavailable
        | Relation::IdentityContentSwapUnavailable => {
            assert_eq!(
                results.len(),
                1,
                "{fixture_id} relation requires one fully compared result"
            );
        }
        Relation::EmptyFileExact => {
            assert_eq!(results.len(), 1);
            let empty = results[0].packages()[0]
                .verified_files()
                .iter()
                .find(|file| file.path() == "empty.txt")
                .unwrap_or_else(|| panic!("{fixture_id} did not retain empty.txt"));
            assert!(empty.bytes().is_empty(), "{fixture_id} empty bytes changed");
        }
        Relation::HardlinkPathsDistinct => {
            assert_eq!(results.len(), 1);
            let files = results[0].packages()[0].verified_files();
            let a = files
                .iter()
                .find(|file| file.path() == "a.txt")
                .unwrap_or_else(|| panic!("{fixture_id} did not retain a.txt"));
            let b = files
                .iter()
                .find(|file| file.path() == "b.txt")
                .unwrap_or_else(|| panic!("{fixture_id} did not retain b.txt"));
            assert_eq!(a.bytes(), b.bytes());
            assert_ne!(a.path(), b.path());
        }
        Relation::DistinctIdentities => {
            assert_eq!(results.len(), 2);
            assert_ne!(
                results[0].packages()[0].identity(),
                results[1].packages()[0].identity(),
                "{fixture_id} distinct complete inputs produced one identity"
            );
        }
        Relation::ExactSourceBinding => {
            assert_eq!(results.len(), 2);
            assert_ne!(
                results[0].digested_source(),
                results[1].digested_source(),
                "{fixture_id} did not retain distinct exact sources"
            );
            assert_eq!(results[0].packages(), results[1].packages());
        }
        Relation::RepeatEqual => {
            assert_eq!(results.len(), 2);
            assert_eq!(results[0], results[1], "{fixture_id} is not repeatable");
        }
        Relation::LiveSnapshotStable => {
            assert_eq!(results.len(), 1);
            let expected = constants
                .get("M_ALPHA_100")
                .expect("M_ALPHA_100 constant is missing");
            assert_eq!(
                results[0].packages()[0].verified_files()[0].bytes(),
                expected,
                "{fixture_id} observed a post-acquisition mutation"
            );
        }
        Relation::LaterConsumesRetained => {
            assert_eq!(results.len(), 1);
            assert_eq!(
                results[0].packages()[0].verified_files()[0].bytes(),
                constants["M_ALPHA_100"],
                "{fixture_id} did not expose exact retained bytes"
            );
        }
        Relation::CanonicalBytesDerived => {
            assert_eq!(results.len(), 1);
            let package = &results[0].packages()[0];
            assert_eq!(
                package.canonical_descriptor_bytes(),
                package.canonical_descriptor_bytes(),
                "{fixture_id} canonical derivation is unstable"
            );
        }
        Relation::CanonicalCacheNotSemantic => {
            assert_eq!(results.len(), 1);
            let package = &results[0].packages()[0];
            let mut first = package.canonical_descriptor_bytes();
            let second = package.canonical_descriptor_bytes();
            first.clear();
            assert!(!second.is_empty());
            assert_eq!(second, package.canonical_descriptor_bytes());
        }
        Relation::VerifiedBytesImmutable => {
            assert_eq!(results.len(), 1);
            fn requires_immutable_slice(_: &[u8]) {}
            requires_immutable_slice(results[0].packages()[0].verified_files()[0].bytes());
        }
    }
}

fn apply_operation(
    root: &mut VirtualNode,
    operation: &Operation,
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
    context: &str,
) {
    coverage
        .operations
        .insert(operation.vocabulary_name().to_owned());
    match operation {
        Operation::Add { node, path } => {
            let (parent_parts, name) = split_parent_path(path, context);
            let parent = directory_at_mut(root, &parent_parts, context);
            assert!(
                !parent.children.contains_key(name),
                "{context} ADD target {path} already exists"
            );
            let node = virtual_node_from_spec(node, constants, coverage, context);
            assert!(parent.children.insert(name.to_owned(), node).is_none());
            parent.enumeration.push(name.to_owned());
        }
        Operation::Remove { path } => {
            let (parent_parts, name) = split_parent_path(path, context);
            let parent = directory_at_mut(root, &parent_parts, context);
            assert!(
                parent.children.remove(name).is_some(),
                "{context} REMOVE target {path} does not exist"
            );
            let positions = parent
                .enumeration
                .iter()
                .enumerate()
                .filter(|(_, candidate)| candidate.as_str() == name)
                .map(|(index, _)| index)
                .collect::<Vec<_>>();
            assert_eq!(
                positions.len(),
                1,
                "{context} REMOVE target {path} does not match exactly once"
            );
            parent.enumeration.remove(positions[0]);
        }
        Operation::ReplaceNode { node, path } => {
            let (parent_parts, name) = split_parent_path(path, context);
            let replacement = virtual_node_from_spec(node, constants, coverage, context);
            let parent = directory_at_mut(root, &parent_parts, context);
            let target = parent
                .children
                .get_mut(name)
                .unwrap_or_else(|| panic!("{context} REPLACE_NODE target {path} is absent"));
            *target = replacement;
        }
        Operation::ReplaceHex { bytes, path } => {
            assert!(
                matches!(bytes, ByteExpression::Hex { .. }),
                "{context} REPLACE_HEX requires an exact hex byte expression"
            );
            replace_regular_bytes(root, path, bytes, constants, coverage, context);
        }
        Operation::SetDescriptor { bytes, path } => {
            assert!(
                path.rsplit('/').next() == Some("package.yaml"),
                "{context} SET_DESCRIPTOR does not target package.yaml"
            );
            replace_regular_bytes(root, path, bytes, constants, coverage, context);
        }
        Operation::Rename {
            new_final_component,
            path,
        } => {
            assert!(
                !new_final_component.is_empty() && !new_final_component.contains('/'),
                "{context} RENAME has an invalid final component"
            );
            let (parent_parts, name) = split_parent_path(path, context);
            let parent = directory_at_mut(root, &parent_parts, context);
            assert!(
                !parent.children.contains_key(new_final_component),
                "{context} RENAME destination already exists"
            );
            let node = parent
                .children
                .remove(name)
                .unwrap_or_else(|| panic!("{context} RENAME target {path} is absent"));
            assert!(
                parent
                    .children
                    .insert(new_final_component.clone(), node)
                    .is_none()
            );
            let positions = parent
                .enumeration
                .iter()
                .enumerate()
                .filter(|(_, candidate)| candidate.as_str() == name)
                .map(|(index, _)| index)
                .collect::<Vec<_>>();
            assert_eq!(
                positions.len(),
                1,
                "{context} RENAME target does not match exactly once"
            );
            parent.enumeration[positions[0]] = new_final_component.clone();
        }
        Operation::SetChildEnumeration { names, path } => {
            let parts = split_path(path, context);
            let directory = directory_at_mut(root, &parts, context);
            let supplied = names.iter().collect::<BTreeSet<_>>();
            assert_eq!(
                supplied.len(),
                names.len(),
                "{context} enumeration contains duplicate children"
            );
            let actual = directory.children.keys().collect::<BTreeSet<_>>();
            assert_eq!(
                supplied, actual,
                "{context} enumeration is not the exact child map"
            );
            directory.enumeration.clone_from(names);
        }
        Operation::ShareHardlink {
            group_id,
            path_a,
            path_b,
        } => {
            assert!(!group_id.is_empty(), "{context} hard-link group is empty");
            assert_ne!(path_a, path_b, "{context} hard-link paths are identical");
            let bytes_a = regular_bytes_at(root, path_a, context).to_vec();
            let bytes_b = regular_bytes_at(root, path_b, context).to_vec();
            assert_eq!(
                bytes_a, bytes_b,
                "{context} hard-link targets have different bytes"
            );
            set_hardlink_group(root, path_a, group_id, context);
            set_hardlink_group(root, path_b, group_id, context);
        }
    }
}

fn replace_regular_bytes(
    root: &mut VirtualNode,
    path: &str,
    expression: &ByteExpression,
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
    context: &str,
) {
    let replacement = evaluate_bytes(expression, constants, coverage, context);
    let target = node_at_mut(root, &split_path(path, context), context);
    match target {
        VirtualNode::Regular {
            bytes,
            hardlink_group,
        } => {
            *bytes = replacement;
            *hardlink_group = None;
        }
        _ => panic!("{context} byte replacement target {path} is not regular"),
    }
}

fn virtual_node_from_spec(
    spec: &NodeSpec,
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
    context: &str,
) -> VirtualNode {
    coverage.nodes.insert(spec.vocabulary_name().to_owned());
    match spec {
        NodeSpec::Directory { children } => {
            assert!(
                children.is_empty(),
                "{context} ordinary mutation directory must start exactly empty"
            );
            VirtualNode::Directory(VirtualDirectory::empty())
        }
        NodeSpec::DirectoryUnreadable => VirtualNode::DirectoryUnreadable,
        NodeSpec::Regular {
            bytes,
            hardlink_group,
        } => VirtualNode::Regular {
            bytes: evaluate_bytes(bytes, constants, coverage, context),
            hardlink_group: hardlink_group.clone(),
        },
        NodeSpec::RegularUnreadable => VirtualNode::RegularUnreadable,
        NodeSpec::Link { target } => {
            assert!(
                !target.is_empty(),
                "{context} link target evidence is empty"
            );
            VirtualNode::Link
        }
        NodeSpec::Special { special_kind } => {
            assert!(
                !special_kind.is_empty(),
                "{context} special-object evidence is empty"
            );
            VirtualNode::Special
        }
    }
}

fn evaluate_bytes(
    expression: &ByteExpression,
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
    context: &str,
) -> Vec<u8> {
    coverage
        .byte_expressions
        .insert(expression.vocabulary_name().to_owned());
    match expression {
        ByteExpression::Constant { name } => {
            coverage.constants.insert(name.clone());
            constants
                .get(name)
                .unwrap_or_else(|| panic!("{context} references missing byte constant {name}"))
                .clone()
        }
        ByteExpression::Hex { value } => decode_lower_hex(value, context),
        ByteExpression::Utf8 { value } => value.as_bytes().to_vec(),
        ByteExpression::Concat { parts } => {
            assert!(!parts.is_empty(), "{context} has an empty concatenation");
            let mut output = Vec::new();
            for part in parts {
                output.extend(evaluate_bytes(part, constants, coverage, context));
            }
            output
        }
        ByteExpression::ReplaceUtf8 { new, old, source } => {
            coverage.operations.insert("REPLACE_UTF8".to_owned());
            let source = evaluate_bytes(source, constants, coverage, context);
            exact_once_replace(&source, old.as_bytes(), new.as_bytes(), context)
        }
        ByteExpression::InsertUtf8After {
            anchor,
            source,
            text,
        } => {
            coverage.operations.insert("INSERT_UTF8_AFTER".to_owned());
            let source = evaluate_bytes(source, constants, coverage, context);
            let mut replacement = anchor.as_bytes().to_vec();
            replacement.extend_from_slice(text.as_bytes());
            exact_once_replace(&source, anchor.as_bytes(), &replacement, context)
        }
        ByteExpression::InsertBytesAfter {
            anchor,
            bytes,
            source,
        } => {
            let source = evaluate_bytes(source, constants, coverage, context);
            let anchor = evaluate_bytes(anchor, constants, coverage, context);
            let inserted = evaluate_bytes(bytes, constants, coverage, context);
            let mut replacement = anchor.clone();
            replacement.extend(inserted);
            exact_once_replace(&source, &anchor, &replacement, context)
        }
        ByteExpression::DeleteUtf8Exact { source, text } => {
            coverage.operations.insert("DELETE_UTF8_EXACT".to_owned());
            let source = evaluate_bytes(source, constants, coverage, context);
            exact_once_replace(&source, text.as_bytes(), &[], context)
        }
        ByteExpression::Bd {
            files,
            module_file,
            package,
            profiles,
            version,
        } => {
            let mut output = format!(
                "package: {package}\nversion: \"{version}\"\nlattice: \"0.3\"\nprofiles:\n"
            );
            for profile in profiles {
                output.push_str(&format!("  - {profile}\n"));
            }
            output.push_str(&format!("module_file: {module_file}\nfiles:\n"));
            for file in files {
                output.push_str(&format!(
                    "  - path: {}\n    sha256: {}\n",
                    file.path, file.sha256
                ));
            }
            assert!(
                output.is_ascii(),
                "{context} BD helper unexpectedly produced non-ASCII bytes"
            );
            output.into_bytes()
        }
        ByteExpression::Bdp { path_scalar_source } => format!(
            "package: alpha\nversion: \"1.0.0\"\nlattice: \"0.3\"\nprofiles:\n  - lattice-core-0.1\nmodule_file: {path_scalar_source}\nfiles:\n  - path: {path_scalar_source}\n    sha256: {MODULE_DIGEST}\n"
        )
        .into_bytes(),
        ByteExpression::Bdf {
            files,
            module_file_scalar_source,
        } => {
            let mut output = format!(
                "package: alpha\nversion: \"1.0.0\"\nlattice: \"0.3\"\nprofiles:\n  - lattice-core-0.1\nmodule_file: {module_file_scalar_source}\nfiles:\n"
            );
            for file in files {
                output.push_str(&format!(
                    "  - path: {}\n    sha256: {}\n",
                    file.path_scalar_source, file.sha256_scalar_source
                ));
            }
            output.into_bytes()
        }
    }
}

fn exact_once_replace(source: &[u8], old: &[u8], new: &[u8], context: &str) -> Vec<u8> {
    assert!(!old.is_empty(), "{context} has an empty exact match");
    let matches = source
        .windows(old.len())
        .enumerate()
        .filter(|(_, window)| *window == old)
        .map(|(index, _)| index)
        .collect::<Vec<_>>();
    assert_eq!(
        matches.len(),
        1,
        "{context} exact replacement matched {} times",
        matches.len()
    );
    let index = matches[0];
    let mut output = Vec::with_capacity(source.len() - old.len() + new.len());
    output.extend_from_slice(&source[..index]);
    output.extend_from_slice(new);
    output.extend_from_slice(&source[index + old.len()..]);
    output
}

fn split_path<'a>(path: &'a str, context: &str) -> Vec<&'a str> {
    let parts = path.split('/').collect::<Vec<_>>();
    assert!(
        !path.is_empty() && parts.iter().all(|part| !part.is_empty()),
        "{context} has malformed mutation path {path:?}"
    );
    parts
}

fn split_parent_path<'a>(path: &'a str, context: &str) -> (Vec<&'a str>, &'a str) {
    let mut parts = split_path(path, context);
    let name = parts.pop().expect("a nonempty path has a final component");
    (parts, name)
}

fn directory_at_mut<'a>(
    node: &'a mut VirtualNode,
    parts: &[&str],
    context: &str,
) -> &'a mut VirtualDirectory {
    if let Some((first, rest)) = parts.split_first() {
        let directory = match node {
            VirtualNode::Directory(directory) => directory,
            _ => panic!("{context} ancestor is not a readable directory"),
        };
        let child = directory
            .children
            .get_mut(*first)
            .unwrap_or_else(|| panic!("{context} targets nonexistent ancestor {first}"));
        directory_at_mut(child, rest, context)
    } else {
        match node {
            VirtualNode::Directory(directory) => directory,
            _ => panic!("{context} target is not a readable directory"),
        }
    }
}

fn node_at_mut<'a>(
    node: &'a mut VirtualNode,
    parts: &[&str],
    context: &str,
) -> &'a mut VirtualNode {
    if let Some((first, rest)) = parts.split_first() {
        let directory = match node {
            VirtualNode::Directory(directory) => directory,
            _ => panic!("{context} ancestor is not a readable directory"),
        };
        let child = directory
            .children
            .get_mut(*first)
            .unwrap_or_else(|| panic!("{context} target component {first} is absent"));
        node_at_mut(child, rest, context)
    } else {
        node
    }
}

fn node_at<'a>(node: &'a VirtualNode, parts: &[&str], context: &str) -> &'a VirtualNode {
    if let Some((first, rest)) = parts.split_first() {
        let directory = match node {
            VirtualNode::Directory(directory) => directory,
            _ => panic!("{context} ancestor is not a readable directory"),
        };
        let child = directory
            .children
            .get(*first)
            .unwrap_or_else(|| panic!("{context} target component {first} is absent"));
        node_at(child, rest, context)
    } else {
        node
    }
}

fn regular_bytes_at<'a>(root: &'a VirtualNode, path: &str, context: &str) -> &'a [u8] {
    match node_at(root, &split_path(path, context), context) {
        VirtualNode::Regular { bytes, .. } => bytes,
        _ => panic!("{context} hard-link target {path} is not regular"),
    }
}

fn set_hardlink_group(root: &mut VirtualNode, path: &str, group: &str, context: &str) {
    match node_at_mut(root, &split_path(path, context), context) {
        VirtualNode::Regular { hardlink_group, .. } => {
            *hardlink_group = Some(group.to_owned());
        }
        _ => panic!("{context} hard-link target {path} is not regular"),
    }
}

fn exact_packages_lookup(root: &VirtualNode) -> Option<SnapshotNode> {
    let directory = match root {
        VirtualNode::Directory(directory) => directory,
        _ => panic!("the interpreter's project root is not a directory"),
    };
    assert_eq!(
        directory.enumeration.len(),
        directory.children.len(),
        "project-root enumeration is incomplete"
    );
    assert_eq!(
        directory.enumeration.iter().collect::<BTreeSet<_>>(),
        directory.children.keys().collect::<BTreeSet<_>>(),
        "project-root enumeration is not its exact child map"
    );
    let packages = directory.children.get("packages")?;
    let mut hardlinks = BTreeMap::new();
    Some(materialize_virtual_node(packages, &mut hardlinks))
}

fn materialize_virtual_node(
    node: &VirtualNode,
    hardlinks: &mut BTreeMap<String, Arc<[u8]>>,
) -> SnapshotNode {
    match node {
        VirtualNode::Directory(directory) => {
            assert_eq!(
                directory.enumeration.len(),
                directory.children.len(),
                "directory enumeration is incomplete"
            );
            assert_eq!(
                directory.enumeration.iter().collect::<BTreeSet<_>>().len(),
                directory.enumeration.len(),
                "directory enumeration contains duplicates"
            );
            let children = directory
                .enumeration
                .iter()
                .map(|name| {
                    let child = directory.children.get(name).unwrap_or_else(|| {
                        panic!("directory enumeration references missing child {name}")
                    });
                    SnapshotEntry::new(
                        SnapshotName::unicode(name.clone()),
                        materialize_virtual_node(child, hardlinks),
                    )
                })
                .collect();
            SnapshotNode::directory(children)
        }
        VirtualNode::DirectoryUnreadable => SnapshotNode::directory_unreadable(),
        VirtualNode::Regular {
            bytes,
            hardlink_group,
        } => {
            if let Some(group) = hardlink_group {
                let shared = if let Some(existing) = hardlinks.get(group) {
                    assert_eq!(
                        existing.as_ref(),
                        bytes.as_slice(),
                        "hard-link group {group} contains different bytes"
                    );
                    Arc::clone(existing)
                } else {
                    let shared: Arc<[u8]> = Arc::from(bytes.clone());
                    hardlinks.insert(group.clone(), Arc::clone(&shared));
                    shared
                };
                SnapshotNode::regular_shared(shared)
            } else {
                SnapshotNode::regular(bytes.clone())
            }
        }
        VirtualNode::RegularUnreadable => SnapshotNode::regular_unreadable(),
        VirtualNode::Link => SnapshotNode::link_like(),
        VirtualNode::Special => SnapshotNode::special(),
    }
}

fn materialize_raw_node(
    node: &NodeSpec,
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
    hardlinks: &mut BTreeMap<String, Arc<[u8]>>,
) -> SnapshotNode {
    coverage.nodes.insert(node.vocabulary_name().to_owned());
    match node {
        NodeSpec::Directory { children } => {
            let mut raw_names = BTreeSet::new();
            let entries = children
                .iter()
                .map(|child| {
                    let (name, identity) = materialize_name(&child.name);
                    assert!(
                        raw_names.insert(identity),
                        "acquisition node contains duplicate raw name evidence"
                    );
                    SnapshotEntry::new(
                        name,
                        materialize_raw_node(&child.node, constants, coverage, hardlinks),
                    )
                })
                .collect();
            SnapshotNode::directory(entries)
        }
        NodeSpec::DirectoryUnreadable => SnapshotNode::directory_unreadable(),
        NodeSpec::Regular {
            bytes,
            hardlink_group,
        } => {
            let bytes = evaluate_bytes(bytes, constants, coverage, "acquisition node");
            if let Some(group) = hardlink_group {
                let shared = if let Some(existing) = hardlinks.get(group) {
                    assert_eq!(existing.as_ref(), bytes.as_slice());
                    Arc::clone(existing)
                } else {
                    let shared: Arc<[u8]> = Arc::from(bytes);
                    hardlinks.insert(group.clone(), Arc::clone(&shared));
                    shared
                };
                SnapshotNode::regular_shared(shared)
            } else {
                SnapshotNode::regular(bytes)
            }
        }
        NodeSpec::RegularUnreadable => SnapshotNode::regular_unreadable(),
        NodeSpec::Link { target } => {
            assert!(!target.is_empty(), "raw link target evidence is empty");
            SnapshotNode::link_like()
        }
        NodeSpec::Special { special_kind } => {
            assert!(
                !special_kind.is_empty(),
                "raw special-object evidence is empty"
            );
            SnapshotNode::special()
        }
    }
}

fn materialize_name(name: &NameSpec) -> (SnapshotName, String) {
    match name {
        NameSpec::Unicode { value } => (
            SnapshotName::unicode(value.clone()),
            format!("unicode:{value}"),
        ),
        NameSpec::UnixBytes { hex } => {
            let bytes = decode_lower_hex(hex, "Unix native name");
            (SnapshotName::unix_bytes(bytes), format!("unix-bytes:{hex}"))
        }
        NameSpec::WindowsUtf16 { units } => (
            SnapshotName::windows_utf16(units.clone()),
            format!("windows-utf16:{units:?}"),
        ),
    }
}

fn canonical_expected_descriptor(record: &ExpectedPackage) -> Vec<u8> {
    let files = record
        .files
        .iter()
        .map(|file| {
            let mut value = Map::new();
            value.insert("path".to_owned(), Value::String(file.path.clone()));
            value.insert("sha256".to_owned(), Value::String(file.sha256.clone()));
            Value::Object(value)
        })
        .collect::<Vec<_>>();
    let mut value = Map::new();
    value.insert("package".to_owned(), Value::String(record.package.clone()));
    value.insert("version".to_owned(), Value::String(record.version.clone()));
    value.insert("lattice".to_owned(), Value::String(record.lattice.clone()));
    value.insert(
        "profiles".to_owned(),
        Value::Array(record.profiles.iter().cloned().map(Value::String).collect()),
    );
    value.insert(
        "module_file".to_owned(),
        Value::String(record.module_file.clone()),
    );
    value.insert("files".to_owned(), Value::Array(files));
    canonical_bytes(&Value::Object(value))
        .expect("complete expected descriptor must be canonically encodable")
}

fn assert_complete_coverage(
    plan: &Plan,
    constants: &BTreeMap<String, Vec<u8>>,
    vectors: &BTreeMap<String, Vec<u8>>,
    coverage: &Coverage,
) {
    assert_eq!(coverage.cases.len(), 184, "not every fixture was executed");
    assert_eq!(
        coverage.diagnostic_codes,
        codes::ALL
            .into_iter()
            .map(str::to_owned)
            .collect::<BTreeSet<_>>(),
        "not all 31 diagnostics were exercised through Package Scan"
    );
    assert_eq!(
        coverage.constants,
        constants.keys().cloned().collect::<BTreeSet<_>>(),
        "unused or unreachable authoritative byte constant"
    );
    assert_eq!(
        coverage.vectors,
        vectors.keys().cloned().collect::<BTreeSet<_>>(),
        "unused or unreachable canonical package vector"
    );
    assert_eq!(
        coverage.expected_packages,
        plan.expected_packages
            .keys()
            .cloned()
            .collect::<BTreeSet<_>>(),
        "unused or unreachable complete package expectation"
    );
    let referenced_result_packages = plan
        .cases
        .iter()
        .filter_map(|case| match &case.outcome {
            Outcome::Success { run_packages, .. } => Some(run_packages),
            Outcome::Diagnostic { .. } | Outcome::AcquisitionFailure { .. } => None,
        })
        .flat_map(|runs| runs.iter())
        .flat_map(|packages| packages.iter().cloned())
        .collect::<BTreeSet<_>>();
    assert_eq!(
        coverage.result_packages, referenced_result_packages,
        "a fixture package expectation was not executed"
    );
    assert_eq!(
        coverage.sources,
        plan.source_vocabulary
            .keys()
            .cloned()
            .collect::<BTreeSet<_>>(),
        "unused or unreachable source"
    );
    assert_eq!(
        coverage.bases,
        plan.base_snapshots.keys().cloned().collect::<BTreeSet<_>>(),
        "unused or unreachable base snapshot"
    );
    assert_eq!(
        coverage.operations,
        plan.operation_vocabulary
            .iter()
            .cloned()
            .collect::<BTreeSet<_>>(),
        "an operation is undeclared or unreachable"
    );
    assert_eq!(
        coverage.byte_expressions,
        plan.byte_expression_vocabulary
            .iter()
            .cloned()
            .collect::<BTreeSet<_>>(),
        "a byte expression is undeclared or unreachable"
    );
    assert_eq!(
        coverage.nodes,
        plan.node_vocabulary
            .iter()
            .cloned()
            .collect::<BTreeSet<_>>(),
        "a node kind is undeclared or unreachable"
    );
    assert_eq!(
        coverage.relations,
        plan.relation_vocabulary
            .iter()
            .cloned()
            .collect::<BTreeSet<_>>(),
        "a success relation is undeclared or unreachable"
    );
}

fn required_str<'a>(object: &'a Map<String, Value>, key: &str, context: &str) -> &'a str {
    object
        .get(key)
        .and_then(Value::as_str)
        .unwrap_or_else(|| panic!("{context} member {key} must be a string"))
}

fn assert_exact_keys(object: &Map<String, Value>, expected: &[&str], context: &str) {
    let actual = object.keys().map(String::as_str).collect::<BTreeSet<_>>();
    let expected = expected.iter().copied().collect::<BTreeSet<_>>();
    assert_eq!(
        actual, expected,
        "{context} contains a missing or undeclared field"
    );
}

fn decode_lower_hex(value: &str, context: &str) -> Vec<u8> {
    assert!(
        value.len().is_multiple_of(2)
            && value
                .bytes()
                .all(|byte| byte.is_ascii_digit() || matches!(byte, b'a'..=b'f')),
        "{context} is not lowercase even-length hexadecimal"
    );
    value
        .as_bytes()
        .chunks_exact(2)
        .map(|pair| {
            let text = std::str::from_utf8(pair).expect("ASCII hex must be UTF-8");
            u8::from_str_radix(text, 16).expect("validated hexadecimal must decode")
        })
        .collect()
}

fn build_source(
    fixture_id: &str,
    source_name: &str,
    plan: &Plan,
    constants: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
) -> DigestedSource {
    let source = plan
        .source_vocabulary
        .get(source_name)
        .unwrap_or_else(|| panic!("{fixture_id} references missing source {source_name}"));
    let expected_canonical = constants
        .get(&source.byte_constant)
        .unwrap_or_else(|| panic!("{source_name} references missing byte constant"));
    coverage.constants.insert(source.byte_constant.clone());
    let parsed = parse_blueprint_source(source.yaml.as_bytes())
        .unwrap_or_else(|diagnostic| panic!("{source_name} failed PC2: {diagnostic}"));
    let validated = validate_blueprint_source(parsed)
        .unwrap_or_else(|diagnostic| panic!("{source_name} failed PC3: {diagnostic}"));
    let defaulted = apply_blueprint_defaults(validated);
    let actual_canonical = canonical_bytes(defaulted.as_value())
        .expect("an accepted source must be canonically encodable");
    assert_eq!(
        actual_canonical.as_slice(),
        expected_canonical.as_slice(),
        "{source_name} canonical source bytes changed"
    );
    let digested = digest_source(defaulted);
    assert_eq!(
        digested.blueprint_digest().to_string(),
        format!(
            "lattice:blueprint:sha256:{}",
            sha256_digest(expected_canonical).to_hex()
        ),
        "{source_name} Blueprint digest changed"
    );
    digested
}

struct ScannedSourceComparisonInputs<'a> {
    plan: &'a Plan,
    constants: &'a BTreeMap<String, Vec<u8>>,
    vectors: &'a BTreeMap<String, Vec<u8>>,
}

fn compare_scanned_source(
    fixture_id: &str,
    run_index: usize,
    scanned: &ScannedSource,
    expected_ids: &[String],
    inputs: &ScannedSourceComparisonInputs<'_>,
    coverage: &mut Coverage,
) {
    assert_eq!(
        scanned.packages().len(),
        expected_ids.len(),
        "{fixture_id} run {run_index} package count changed"
    );
    for (package_index, (actual, record_id)) in
        scanned.packages().iter().zip(expected_ids).enumerate()
    {
        let expected = inputs
            .plan
            .expected_packages
            .get(record_id)
            .unwrap_or_else(|| {
                panic!("{fixture_id} references missing expected package {record_id}")
            });
        coverage.expected_packages.insert(record_id.clone());
        coverage.result_packages.insert(record_id.clone());
        compare_package(
            fixture_id,
            run_index,
            package_index,
            actual,
            expected,
            inputs.constants,
            inputs.vectors,
            coverage,
        );
    }
}

#[allow(clippy::too_many_arguments)]
fn compare_package(
    fixture_id: &str,
    run_index: usize,
    package_index: usize,
    actual: &ScannedPackage,
    expected: &ExpectedPackage,
    constants: &BTreeMap<String, Vec<u8>>,
    vectors: &BTreeMap<String, Vec<u8>>,
    coverage: &mut Coverage,
) {
    let context = format!("{fixture_id} run {run_index} package {package_index}");
    let descriptor = actual.descriptor();
    assert_eq!(
        descriptor.package(),
        expected.package.as_str(),
        "{context} package"
    );
    assert_eq!(
        descriptor.version(),
        expected.version.as_str(),
        "{context} version"
    );
    assert_eq!(
        descriptor.lattice(),
        expected.lattice.as_str(),
        "{context} lattice"
    );
    assert_eq!(
        descriptor.profiles(),
        expected.profiles.as_slice(),
        "{context} profiles"
    );
    assert_eq!(
        descriptor.module_file(),
        expected.module_file.as_str(),
        "{context} module_file"
    );
    assert_eq!(
        descriptor.files().len(),
        expected.files.len(),
        "{context} descriptor file count"
    );
    assert_eq!(
        actual.verified_files().len(),
        expected.files.len(),
        "{context} verified file count"
    );
    for ((descriptor_file, verified_file), expected_file) in descriptor
        .files()
        .iter()
        .zip(actual.verified_files())
        .zip(&expected.files)
    {
        assert_eq!(
            descriptor_file.path(),
            expected_file.path.as_str(),
            "{context} descriptor path ordering"
        );
        assert_eq!(
            descriptor_file.sha256(),
            expected_file.sha256.as_str(),
            "{context} declared digest"
        );
        assert_eq!(
            verified_file.path(),
            expected_file.path.as_str(),
            "{context} verified logical path"
        );
        let expected_bytes = constants
            .get(&expected_file.byte_constant)
            .unwrap_or_else(|| {
                panic!(
                    "{context} references missing byte constant {}",
                    expected_file.byte_constant
                )
            });
        coverage
            .constants
            .insert(expected_file.byte_constant.clone());
        assert_eq!(
            verified_file.bytes(),
            expected_bytes.as_slice(),
            "{context} retained raw bytes at {}",
            expected_file.path
        );
        assert_eq!(
            sha256_digest(verified_file.bytes()).to_hex(),
            expected_file.sha256,
            "{context} retained-byte digest at {}",
            expected_file.path
        );
    }
    assert_eq!(
        actual.identity().to_string(),
        expected.identity.as_str(),
        "{context} exact package identity"
    );
    let canonical = actual.canonical_descriptor_bytes();
    assert_eq!(
        canonical,
        canonical_expected_descriptor(expected),
        "{context} canonical descriptor bytes"
    );
    if let Some(vector_name) = &expected.canonical_vector {
        let vector = vectors
            .get(vector_name)
            .unwrap_or_else(|| panic!("{context} missing canonical vector {vector_name}"));
        coverage.vectors.insert(vector_name.clone());
        assert_eq!(
            canonical.as_slice(),
            vector.as_slice(),
            "{context} canonical golden bytes"
        );
    }
}
