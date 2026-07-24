use serde_json::Value;
use std::sync::Arc;
use threadsmith_canonical::sha256_digest;
use threadsmith_compiler::{
    PackageScanDiagnostic, ScannedSource, SnapshotAcquisitionError, SnapshotEntry, SnapshotName,
    SnapshotNode, acquire_project_snapshot, apply_blueprint_defaults, digest_source,
    package_scan_diagnostic_codes as codes, parse_blueprint_source, scan_packages,
    validate_blueprint_source,
};

#[path = "support/pc6_fixture_interpreter.rs"]
mod pc6_fixture_interpreter;

const ROOT: &[u8] = br#"lattice: "0.3"
profile: lattice-core-0.1
module: root
version: "1.0.0"
purpose: fixture root
units: []
"#;

const M_ALPHA_100: &[u8] = b"lattice: \"0.3\"\nprofile: lattice-core-0.1\nmodule: alpha\nversion: \"1.0.0\"\npurpose: alpha package\nunits: []\n";
const M_ALPHA_110: &[u8] = b"lattice: \"0.3\"\nprofile: lattice-core-0.1\nmodule: alpha\nversion: \"1.1.0\"\npurpose: alpha package\nunits: []\n";

const D_MIN: &[u8] = b"package: alpha\nversion: \"1.0.0\"\nlattice: \"0.3\"\nprofiles:\n  - lattice-core-0.1\nmodule_file: module.yaml\nfiles:\n  - path: module.yaml\n    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n";

fn source() -> threadsmith_compiler::DigestedSource {
    let parsed = parse_blueprint_source(ROOT).unwrap();
    let validated = validate_blueprint_source(parsed).unwrap();
    digest_source(apply_blueprint_defaults(validated))
}

fn name(value: &str) -> SnapshotName {
    SnapshotName::unicode(value)
}

fn entry(name_value: &str, node: SnapshotNode) -> SnapshotEntry {
    SnapshotEntry::new(name(name_value), node)
}

fn dir(children: Vec<SnapshotEntry>) -> SnapshotNode {
    SnapshotNode::directory(children)
}

fn version(version: &str, descriptor: Vec<u8>, module: Vec<u8>) -> SnapshotEntry {
    entry(
        version,
        dir(vec![
            entry("module.yaml", SnapshotNode::regular(module)),
            entry("package.yaml", SnapshotNode::regular(descriptor)),
        ]),
    )
}

fn minimal_packages() -> SnapshotNode {
    dir(vec![entry(
        "alpha",
        dir(vec![version("1.0.0", D_MIN.to_vec(), M_ALPHA_100.to_vec())]),
    )])
}

fn scan(packages: Option<SnapshotNode>) -> Result<ScannedSource, PackageScanDiagnostic> {
    scan_packages(source(), acquire_project_snapshot(Ok(packages)).unwrap())
}

fn descriptor(package: &str, version: &str, digest: &str) -> Vec<u8> {
    format!(
        "package: {package}\nversion: \"{version}\"\nlattice: \"0.3\"\nprofiles:\n  - lattice-core-0.1\nmodule_file: module.yaml\nfiles:\n  - path: module.yaml\n    sha256: {digest}\n"
    )
    .into_bytes()
}

fn assert_diagnostic(
    result: Result<ScannedSource, PackageScanDiagnostic>,
    code: &'static str,
    path: &str,
) {
    let diagnostic = result.unwrap_err();
    assert_eq!(diagnostic.code(), code);
    assert_eq!(diagnostic.path(), path);
}

#[test]
fn absent_empty_and_minimal_vectors_match_the_freeze() {
    assert!(scan(None).unwrap().packages().is_empty());
    assert!(scan(Some(dir(Vec::new()))).unwrap().packages().is_empty());

    let scanned = scan(Some(minimal_packages())).unwrap();
    assert_eq!(scanned.packages().len(), 1);
    let package = &scanned.packages()[0];
    assert_eq!(
        package.identity().to_string(),
        "lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b"
    );
    assert_eq!(package.descriptor().package(), "alpha");
    assert_eq!(package.descriptor().version(), "1.0.0");
    assert_eq!(package.descriptor().lattice(), "0.3");
    assert_eq!(
        package
            .descriptor()
            .profiles()
            .iter()
            .map(String::as_str)
            .collect::<Vec<_>>(),
        ["lattice-core-0.1"]
    );
    assert_eq!(package.descriptor().module_file(), "module.yaml");
    assert_eq!(package.verified_files()[0].path(), "module.yaml");
    assert_eq!(package.verified_files()[0].bytes(), M_ALPHA_100);
    assert_eq!(
        package.canonical_descriptor_bytes(),
        br#"{"files":[{"path":"module.yaml","sha256":"900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55"}],"lattice":"0.3","module_file":"module.yaml","package":"alpha","profiles":["lattice-core-0.1"],"version":"1.0.0"}"#
    );
}

#[test]
fn successful_candidates_use_arbitrary_precision_numeric_version_order() {
    let d2 = descriptor(
        "alpha",
        "2.0.0",
        "900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55",
    );
    let d10 = descriptor(
        "alpha",
        "10.0.0",
        "900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55",
    );
    let huge_a = "999999999999999999999999999999999999999.0.0";
    let huge_b = "1000000000000000000000000000000000000000.0.0";
    let scanned = scan(Some(dir(vec![entry(
        "alpha",
        dir(vec![
            version("10.0.0", d10, M_ALPHA_100.to_vec()),
            version("2.0.0", d2, M_ALPHA_100.to_vec()),
            version(
                huge_b,
                descriptor(
                    "alpha",
                    huge_b,
                    "900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55",
                ),
                M_ALPHA_100.to_vec(),
            ),
            version(
                huge_a,
                descriptor(
                    "alpha",
                    huge_a,
                    "900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55",
                ),
                M_ALPHA_100.to_vec(),
            ),
        ]),
    )])))
    .unwrap();
    let versions = scanned
        .packages()
        .iter()
        .map(|package| package.descriptor().version())
        .collect::<Vec<_>>();
    assert_eq!(versions, ["2.0.0", "10.0.0", huge_a, huge_b]);
}

#[test]
fn structural_order_and_global_stage_precedence_are_exact() {
    let missing_both = dir(vec![entry(
        "alpha",
        dir(vec![
            entry(
                "2.0.0",
                dir(vec![entry(
                    "module.yaml",
                    SnapshotNode::regular(M_ALPHA_100.to_vec()),
                )]),
            ),
            entry(
                "10.0.0",
                dir(vec![entry(
                    "module.yaml",
                    SnapshotNode::regular(M_ALPHA_100.to_vec()),
                )]),
            ),
        ]),
    )]);
    assert_diagnostic(
        scan(Some(missing_both)),
        codes::DESCRIPTOR_MISSING,
        "packages/alpha/10.0.0/package.yaml",
    );

    let alpha_bad_bytes = version("1.0.0", D_MIN.to_vec(), b"different bytes".to_vec());
    let beta_invalid_yaml = version("2.0.0", b"units: [\n".to_vec(), b"beta".to_vec());
    let packages = dir(vec![
        entry("alpha", dir(vec![alpha_bad_bytes])),
        entry("beta", dir(vec![beta_invalid_yaml])),
    ]);
    assert_diagnostic(
        scan(Some(packages)),
        codes::DESCRIPTOR_YAML_FORBIDDEN,
        "packages/beta/2.0.0/package.yaml#",
    );
}

#[test]
fn parser_crosswalk_schema_and_pointer_rendering_are_exact() {
    let cases = [
        (
            vec![0xff],
            codes::DESCRIPTOR_SOURCE_INVALID,
            "packages/alpha/1.0.0/package.yaml#",
        ),
        (
            b"units: [\n".to_vec(),
            codes::DESCRIPTOR_YAML_FORBIDDEN,
            "packages/alpha/1.0.0/package.yaml#",
        ),
        (
            b"[]\n".to_vec(),
            codes::DESCRIPTOR_ROOT_INVALID,
            "packages/alpha/1.0.0/package.yaml#",
        ),
    ];
    for (descriptor, code, path) in cases {
        let packages = dir(vec![entry(
            "alpha",
            dir(vec![version("1.0.0", descriptor, M_ALPHA_100.to_vec())]),
        )]);
        assert_diagnostic(scan(Some(packages)), code, path);
    }

    let mut descriptor = String::from_utf8(D_MIN.to_vec()).unwrap();
    descriptor = descriptor.replace("lattice: \"0.3\"\n", "lattice: \"0.3\"\n\"a/b\": true\n");
    let packages = dir(vec![entry(
        "alpha",
        dir(vec![version(
            "1.0.0",
            descriptor.into_bytes(),
            M_ALPHA_100.to_vec(),
        )]),
    )]);
    assert_diagnostic(
        scan(Some(packages)),
        codes::DESCRIPTOR_UNKNOWN_KEY,
        "packages/alpha/1.0.0/package.yaml#/a~1b",
    );
}

#[test]
fn portable_names_paths_objects_and_raw_bytes_follow_the_frozen_boundaries() {
    assert_eq!(
        acquire_project_snapshot(Ok(Some(dir(vec![SnapshotEntry::new(
            SnapshotName::unix_bytes(vec![0xff]),
            dir(Vec::new()),
        )]))))
        .unwrap_err(),
        SnapshotAcquisitionError::UnrepresentableNativeName
    );
    assert_eq!(
        acquire_project_snapshot(Ok(Some(dir(vec![SnapshotEntry::new(
            SnapshotName::windows_utf16(vec![0xd800]),
            dir(Vec::new()),
        )]))))
        .unwrap_err(),
        SnapshotAcquisitionError::MalformedUtf16Name
    );
    assert_eq!(
        acquire_project_snapshot(Err(SnapshotAcquisitionError::ConcurrentMutation)).unwrap_err(),
        SnapshotAcquisitionError::ConcurrentMutation
    );

    assert_diagnostic(
        scan(Some(dir(vec![entry("café", dir(Vec::new()))]))),
        codes::LAYOUT_ENTRY_INVALID,
        "packages/caf%C3%A9",
    );
    assert_diagnostic(
        scan(Some(SnapshotNode::link_like())),
        codes::SYMLINK_FORBIDDEN,
        "packages",
    );
    assert_diagnostic(
        scan(Some(SnapshotNode::regular(Vec::new()))),
        codes::PACKAGES_ROOT_INVALID,
        "packages",
    );

    let unreadable = dir(vec![entry(
        "alpha",
        dir(vec![entry(
            "1.0.0",
            dir(vec![
                entry("module.yaml", SnapshotNode::regular_unreadable()),
                entry("package.yaml", SnapshotNode::regular(D_MIN.to_vec())),
            ]),
        )]),
    )]);
    assert_diagnostic(
        scan(Some(unreadable)),
        codes::DECLARED_FILE_UNREADABLE,
        "packages/alpha/1.0.0/module.yaml",
    );

    let mut crlf = Vec::new();
    for byte in M_ALPHA_100 {
        if *byte == b'\n' {
            crlf.extend_from_slice(b"\r\n");
        } else {
            crlf.push(*byte);
        }
    }
    let changed = dir(vec![entry(
        "alpha",
        dir(vec![version("1.0.0", D_MIN.to_vec(), crlf)]),
    )]);
    assert_diagnostic(
        scan(Some(changed)),
        codes::FILE_HASH_MISMATCH,
        "packages/alpha/1.0.0/module.yaml",
    );
}

#[test]
fn metadata_audit_precedes_declared_files_and_ignores_unlisted_regular_bytes() {
    let packages = dir(vec![entry(
        "alpha",
        dir(vec![entry(
            "1.0.0",
            dir(vec![
                entry("ignored", SnapshotNode::directory_unreadable()),
                entry("module.yaml", SnapshotNode::regular(b"wrong".to_vec())),
                entry("package.yaml", SnapshotNode::regular(D_MIN.to_vec())),
            ]),
        )]),
    )]);
    assert_diagnostic(
        scan(Some(packages)),
        codes::DISCOVERY_UNREADABLE,
        "packages/alpha/1.0.0/ignored",
    );

    let packages = dir(vec![entry(
        "alpha",
        dir(vec![entry(
            "1.0.0",
            dir(vec![
                entry("ignored.bin", SnapshotNode::regular(vec![0xff, 0x00])),
                entry("module.yaml", SnapshotNode::regular(M_ALPHA_100.to_vec())),
                entry("package.yaml", SnapshotNode::regular(D_MIN.to_vec())),
            ]),
        )]),
    )]);
    let scanned = scan(Some(packages)).unwrap();
    assert_eq!(scanned.packages()[0].verified_files().len(), 1);
    assert_eq!(
        scanned.packages()[0].verified_files()[0].path(),
        "module.yaml"
    );
}

#[test]
fn hard_links_remain_distinct_logical_verified_paths() {
    let shared: Arc<[u8]> = Arc::from(b"alpha data\n".as_slice());
    let descriptor = b"package: alpha\nversion: \"1.0.0\"\nlattice: \"0.3\"\nprofiles:\n  - lattice-core-0.1\nmodule_file: module.yaml\nfiles:\n  - path: a.txt\n    sha256: c0ef28aa04fc0e12e57ea295ae9f356b09271cd19a6b7996ab3a365a2d88ee73\n  - path: b.txt\n    sha256: c0ef28aa04fc0e12e57ea295ae9f356b09271cd19a6b7996ab3a365a2d88ee73\n  - path: module.yaml\n    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n".to_vec();
    let packages = dir(vec![entry(
        "alpha",
        dir(vec![entry(
            "1.0.0",
            dir(vec![
                entry("a.txt", SnapshotNode::regular_shared(Arc::clone(&shared))),
                entry("b.txt", SnapshotNode::regular_shared(shared)),
                entry("module.yaml", SnapshotNode::regular(M_ALPHA_100.to_vec())),
                entry("package.yaml", SnapshotNode::regular(descriptor)),
            ]),
        )]),
    )]);
    let scanned = scan(Some(packages)).unwrap();
    let package = &scanned.packages()[0];
    assert_eq!(
        package.identity().to_string(),
        "lattice:package:sha256:403906116513b9c432a9f9558d7af747286b5539ee95563fba019d38584a1dc7"
    );
    assert_eq!(
        package
            .verified_files()
            .iter()
            .map(|file| file.path())
            .collect::<Vec<_>>(),
        ["a.txt", "b.txt", "module.yaml"]
    );
}

#[test]
fn results_are_source_bound_immutable_and_repeatable() {
    let first = scan(Some(minimal_packages())).unwrap();
    let second = scan(Some(minimal_packages())).unwrap();
    assert_eq!(first, second);
    assert_eq!(
        first.digested_source().blueprint_digest().to_string(),
        "lattice:blueprint:sha256:196ff00d07966e5e60f787fc91fd4e9d1a7b52c8b7bb8ced93cc2d86443fe4b5"
    );
    assert_eq!(first.packages()[0].verified_files()[0].bytes(), M_ALPHA_100);

    let replacement = M_ALPHA_110.to_vec();
    assert_ne!(replacement, first.packages()[0].verified_files()[0].bytes());
    assert_eq!(first.packages()[0].verified_files()[0].bytes(), M_ALPHA_100);
}

#[test]
fn data_changed_vector_and_portable_path_population_are_exact() {
    let data_changed = b"alpha data changed\n";
    let descriptor = b"package: alpha\nversion: \"1.0.0\"\nlattice: \"0.3\"\nprofiles:\n  - lattice-core-0.1\nmodule_file: module.yaml\nfiles:\n  - path: module.yaml\n    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n  - path: data.txt\n    sha256: 792ef13d8b723ba31c6e2c37865aa3fc7d027ea2b04a23969ba9aa63e487e9b2\n".to_vec();
    let packages = dir(vec![entry(
        "alpha",
        dir(vec![entry(
            "1.0.0",
            dir(vec![
                entry("data.txt", SnapshotNode::regular(data_changed.to_vec())),
                entry("module.yaml", SnapshotNode::regular(M_ALPHA_100.to_vec())),
                entry("package.yaml", SnapshotNode::regular(descriptor)),
            ]),
        )]),
    )]);
    let scanned = scan(Some(packages)).unwrap();
    assert_eq!(
        scanned.packages()[0].identity().to_string(),
        "lattice:package:sha256:b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b"
    );

    let invalid_paths = [
        "",
        "/module.yaml",
        "module.yaml/",
        "sub//module.yaml",
        "./module.yaml",
        "../module.yaml",
        r"sub\module.yaml",
        "c:/module.yaml",
        "//server/share/module.yaml",
        "a:b",
        "\0",
        "\u{0001}",
        "café.txt",
        "cafe\u{0301}.txt",
        "Module.yaml",
        "con.txt",
        "module.",
        "module.yaml ",
    ];
    for invalid_path in invalid_paths {
        let scalar = serde_json::to_string(invalid_path).unwrap();
        let descriptor = format!(
            "package: alpha\nversion: \"1.0.0\"\nlattice: \"0.3\"\nprofiles:\n  - lattice-core-0.1\nmodule_file: {scalar}\nfiles:\n  - path: {scalar}\n    sha256: 900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55\n"
        );
        let packages = dir(vec![entry(
            "alpha",
            dir(vec![version(
                "1.0.0",
                descriptor.into_bytes(),
                M_ALPHA_100.to_vec(),
            )]),
        )]);
        assert_diagnostic(
            scan(Some(packages)),
            codes::DECLARED_PATH_INVALID,
            "packages/alpha/1.0.0/package.yaml#/module_file",
        );
    }
}

#[test]
fn all_six_pointer_vectors_use_rfc6901_before_percent_encoding() {
    let cases = [
        ("a/b", "a~1b"),
        ("a~b", "a~0b"),
        ("a%b", "a%25b"),
        ("a#b", "a%23b"),
        ("a\u{0001}b", "a%01b"),
        ("café", "caf%C3%A9"),
    ];
    for (key, rendered) in cases {
        let quoted = serde_json::to_string(key).unwrap();
        let mut descriptor = String::from_utf8(D_MIN.to_vec()).unwrap();
        descriptor = descriptor.replace(
            "lattice: \"0.3\"\n",
            &format!("lattice: \"0.3\"\n{quoted}: true\n"),
        );
        let packages = dir(vec![entry(
            "alpha",
            dir(vec![version(
                "1.0.0",
                descriptor.into_bytes(),
                M_ALPHA_100.to_vec(),
            )]),
        )]);
        assert_diagnostic(
            scan(Some(packages)),
            codes::DESCRIPTOR_UNKNOWN_KEY,
            &format!("packages/alpha/1.0.0/package.yaml#/{rendered}"),
        );
    }
}

#[test]
fn diagnostic_vocabulary_is_exact_and_unique() {
    let all = codes::ALL;
    assert_eq!(all.len(), 31);
    let unique = all.into_iter().collect::<std::collections::BTreeSet<_>>();
    assert_eq!(unique.len(), 31);
}

fn decode_hex(value: &str) -> Result<Vec<u8>, String> {
    if !value.len().is_multiple_of(2) || !value.bytes().all(|byte| byte.is_ascii_hexdigit()) {
        return Err("malformed hex".to_owned());
    }
    value
        .as_bytes()
        .chunks_exact(2)
        .map(|pair| {
            let text = std::str::from_utf8(pair).map_err(|_| "malformed hex".to_owned())?;
            u8::from_str_radix(text, 16).map_err(|_| "malformed hex".to_owned())
        })
        .collect()
}

fn validate_fixture_manifest(value: &Value) -> Result<(), String> {
    let root = value.as_object().ok_or("manifest root is not an object")?;
    for key in [
        "fixture_manifest_version",
        "authority",
        "counts",
        "fixture_class_vocabulary",
        "diagnostic_codes",
        "diagnostic_expectations",
        "authoritative_byte_constants",
        "canonical_package_vectors",
        "package_identities",
        "populations",
        "golden",
        "fixtures",
    ] {
        if !root.contains_key(key) {
            return Err(format!("missing manifest member {key}"));
        }
    }
    if root["fixture_manifest_version"].as_str()
        != Some("pc6-package-scan-fourth-repaired-candidate-5")
    {
        return Err("unknown manifest version".to_owned());
    }

    let counts = root["counts"]
        .as_object()
        .ok_or("counts is not an object")?;
    let expected_counts = [
        ("authoritative_byte_constants", 34_u64),
        ("canonical_package_vectors", 6),
        ("package_identities", 19),
        ("descriptor_presentations", 18),
        ("path_scalar_vectors", 18),
        ("pointer_vectors", 6),
        ("fixtures", 184),
        ("diagnostic_expectations", 124),
        ("diagnostic_codes", 31),
    ];
    for (key, expected) in expected_counts {
        if counts.get(key).and_then(Value::as_u64) != Some(expected) {
            return Err(format!("count mismatch for {key}"));
        }
    }

    let fixture_classes = root["fixture_class_vocabulary"]
        .as_array()
        .ok_or("fixture class vocabulary is not an array")?
        .iter()
        .map(|value| value.as_str().ok_or("fixture class is not a string"))
        .collect::<Result<std::collections::BTreeSet<_>, _>>()?;
    let expected_fixture_classes = [
        "bind", "desc", "eq", "file", "id", "layout", "name", "parse", "path", "phase", "prec",
        "ptr", "snap", "val",
    ]
    .into_iter()
    .collect::<std::collections::BTreeSet<_>>();
    if fixture_classes != expected_fixture_classes {
        return Err("unknown or incomplete fixture class vocabulary".to_owned());
    }

    let diagnostics = root["diagnostic_codes"]
        .as_array()
        .ok_or("diagnostic codes is not an array")?;
    if diagnostics.len() != 31 {
        return Err("diagnostic code count mismatch".to_owned());
    }
    let diagnostics = diagnostics
        .iter()
        .map(|value| value.as_str().ok_or("diagnostic code is not a string"))
        .collect::<Result<std::collections::BTreeSet<_>, _>>()?;
    if diagnostics
        != codes::ALL
            .into_iter()
            .collect::<std::collections::BTreeSet<_>>()
    {
        return Err("diagnostic vocabulary mismatch".to_owned());
    }

    let constants = root["authoritative_byte_constants"]
        .as_array()
        .ok_or("byte constants is not an array")?;
    if constants.len() != 34 {
        return Err("byte constant count mismatch".to_owned());
    }
    let mut constant_names = std::collections::BTreeSet::new();
    for constant in constants {
        let constant = constant
            .as_object()
            .ok_or("byte constant is not an object")?;
        for key in ["name", "hex", "length", "sha256"] {
            if !constant.contains_key(key) {
                return Err(format!("incomplete byte constant member {key}"));
            }
        }
        let name = constant["name"].as_str().ok_or("constant name invalid")?;
        if !constant_names.insert(name) {
            return Err(format!("duplicate byte constant {name}"));
        }
        let bytes = decode_hex(constant["hex"].as_str().ok_or("constant hex invalid")?)?;
        if constant["length"].as_u64() != Some(bytes.len() as u64) {
            return Err(format!("byte length mismatch for {name}"));
        }
        let expected = constant["sha256"].as_str().ok_or("constant hash invalid")?;
        if expected.len() != 64
            || !expected
                .bytes()
                .all(|byte| byte.is_ascii_digit() || matches!(byte, b'a'..=b'f'))
            || sha256_digest(&bytes).to_hex() != expected
        {
            return Err(format!("byte hash mismatch for {name}"));
        }
    }

    let vectors = root["canonical_package_vectors"]
        .as_array()
        .ok_or("canonical vectors is not an array")?;
    if vectors.len() != 6 {
        return Err("canonical vector count mismatch".to_owned());
    }
    for vector in vectors {
        let vector = vector.as_object().ok_or("canonical vector invalid")?;
        let bytes = decode_hex(
            vector["canonical_hex"]
                .as_str()
                .ok_or("canonical vector hex invalid")?,
        )?;
        let digest = sha256_digest(&bytes).to_hex();
        let identity = format!("lattice:package:sha256:{digest}");
        if vector["length"].as_u64() != Some(bytes.len() as u64)
            || vector["sha256"].as_str() != Some(digest.as_str())
            || vector["identity"].as_str() != Some(identity.as_str())
        {
            return Err("canonical vector arithmetic mismatch".to_owned());
        }
    }

    if root["package_identities"]
        .as_array()
        .is_none_or(|values| values.len() != 19)
    {
        return Err("package identity count mismatch".to_owned());
    }
    if root["diagnostic_expectations"]
        .as_array()
        .is_none_or(|values| values.len() != 124)
    {
        return Err("diagnostic expectation count mismatch".to_owned());
    }

    let fixtures = root["fixtures"]
        .as_array()
        .ok_or("fixtures is not an array")?;
    if fixtures.len() != 184 {
        return Err("fixture count mismatch".to_owned());
    }
    let mut fixture_ids = std::collections::BTreeSet::new();
    for fixture in fixtures {
        let fixture = fixture.as_object().ok_or("fixture is not an object")?;
        for key in [
            "id",
            "fixture_class",
            "exact_input",
            "expected",
            "expected_diagnostic",
            "diagnostic_expectations",
        ] {
            if !fixture.contains_key(key) {
                return Err(format!("incomplete fixture member {key}"));
            }
        }
        let id = fixture["id"].as_str().ok_or("fixture ID invalid")?;
        if !fixture_ids.insert(id) {
            return Err(format!("duplicate fixture ID {id}"));
        }
        let fixture_class = fixture["fixture_class"]
            .as_str()
            .ok_or("fixture class invalid")?;
        if !fixture_classes.contains(fixture_class) {
            return Err(format!("unknown fixture class {fixture_class}"));
        }
        if fixture["exact_input"].as_str().is_none_or(str::is_empty)
            || fixture["expected"].as_str().is_none_or(str::is_empty)
        {
            return Err(format!("incomplete fixture notation {id}"));
        }
        if let Some(expected) = fixture["expected_diagnostic"].as_object() {
            let code = expected["code"]
                .as_str()
                .ok_or("expected diagnostic code invalid")?;
            let path = expected["path"]
                .as_str()
                .ok_or("expected diagnostic path invalid")?;
            if !diagnostics.contains(code) || path.is_empty() {
                return Err(format!("incomplete expected diagnostic {id}"));
            }
        } else if !fixture["expected_diagnostic"].is_null() {
            return Err(format!("malformed expected diagnostic {id}"));
        }
        let mentioned = fixture["diagnostic_expectations"]
            .as_array()
            .ok_or("diagnostic expectations are not an array")?;
        for expectation in mentioned {
            let expectation = expectation
                .as_object()
                .ok_or("diagnostic expectation is not an object")?;
            let code = expectation["code"]
                .as_str()
                .ok_or("mentioned diagnostic code invalid")?;
            let path = expectation["path"]
                .as_str()
                .ok_or("mentioned diagnostic path invalid")?;
            if !diagnostics.contains(code) || path.is_empty() {
                return Err(format!("incomplete mentioned diagnostic {id}"));
            }
        }
    }
    Ok(())
}

#[test]
fn fixture_population_manifest_is_fail_closed_and_matches_all_frozen_populations() {
    let bytes = include_bytes!("../../../conformance/pc6/package_scan/fixture_manifest.json");
    let manifest: Value = serde_json::from_slice(bytes).unwrap();
    validate_fixture_manifest(&manifest).unwrap();

    let mut missing_field = manifest.clone();
    missing_field
        .as_object_mut()
        .unwrap()
        .remove("diagnostic_codes");
    assert!(validate_fixture_manifest(&missing_field).is_err());

    let mut duplicate_id = manifest.clone();
    let fixtures = duplicate_id["fixtures"].as_array_mut().unwrap();
    let first_id = fixtures[0]["id"].clone();
    fixtures[1]["id"] = first_id;
    assert!(validate_fixture_manifest(&duplicate_id).is_err());

    let mut unknown_fixture_class = manifest.clone();
    unknown_fixture_class["fixtures"][0]["fixture_class"] = Value::String("unknown".to_owned());
    assert!(validate_fixture_manifest(&unknown_fixture_class).is_err());

    let mut malformed_hash = manifest;
    malformed_hash["authoritative_byte_constants"][0]["sha256"] = Value::String("00".to_owned());
    assert!(validate_fixture_manifest(&malformed_hash).is_err());
}

#[test]
fn all_184_authoritative_fixtures_execute_through_the_public_pc6_boundary() {
    pc6_fixture_interpreter::execute_all();
}
