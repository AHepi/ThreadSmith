use serde_json::{Value, json};
use std::fs;
use std::path::{Path, PathBuf};
use threadsmith_compiler::{
    apply_blueprint_defaults, parse_blueprint_source, validate_blueprint_source,
};

fn repository_root() -> PathBuf {
    Path::new(env!("CARGO_MANIFEST_DIR")).join("../..")
}

fn fixture_manifest() -> Value {
    serde_json::from_slice(
        &fs::read(repository_root().join("conformance/pc4/default/fixture_manifest.json")).unwrap(),
    )
    .unwrap()
}

fn fixture_case<'manifest>(manifest: &'manifest Value, id: &str) -> &'manifest Value {
    manifest["cases"]
        .as_array()
        .unwrap()
        .iter()
        .find(|case| case["id"] == id)
        .unwrap_or_else(|| panic!("missing fixture case {id}"))
}

#[test]
fn frozen_fixtures_match_the_public_pc4_boundary() {
    let manifest = fixture_manifest();
    let cases = manifest["cases"].as_array().unwrap();
    let minimum_runs = manifest["implementation_test_requirements"]["minimum_runs_per_case"]
        .as_u64()
        .unwrap();
    assert_eq!(cases.len(), 9);
    assert_eq!(minimum_runs, 3);

    for case in cases {
        let id = case["id"].as_str().unwrap();
        let input = case["input"].clone();
        let expected = &case["expected"]["output"];

        for _ in 0..minimum_runs {
            let validated = validate_blueprint_source(input.clone())
                .unwrap_or_else(|error| panic!("{id}: PC3 rejected fixture: {error:?}"));
            let defaulted = apply_blueprint_defaults(validated);
            assert_eq!(defaulted.as_value(), expected, "{id}");
            assert_eq!(defaulted.clone().into_value(), expected.clone(), "{id}");
        }

        let validated_expected = validate_blueprint_source(expected.clone())
            .unwrap_or_else(|error| panic!("{id}: PC3 rejected expected output: {error:?}"));
        let repeated = apply_blueprint_defaults(validated_expected);
        assert_eq!(repeated.as_value(), expected, "{id}: not idempotent");

        let applications = case["applications"].as_u64().unwrap_or(1);
        let mut repeatedly_defaulted = expected.clone();
        for _ in 0..applications {
            repeatedly_defaulted =
                apply_blueprint_defaults(validate_blueprint_source(repeatedly_defaulted).unwrap())
                    .into_value();
        }
        assert_eq!(
            repeatedly_defaulted, *expected,
            "{id}: repeated application"
        );
    }
}

#[test]
fn frozen_identity_preimage_groups_compare_as_declared() {
    let manifest = fixture_manifest();

    for group in manifest["equivalence_groups"].as_array().unwrap() {
        let ids = group["cases"].as_array().unwrap();
        let first = &fixture_case(&manifest, ids[0].as_str().unwrap())["expected"]["output"];
        for id in &ids[1..] {
            let output = &fixture_case(&manifest, id.as_str().unwrap())["expected"]["output"];
            assert_eq!(output, first, "{}", group["id"]);
        }
    }

    for group in manifest["distinction_groups"].as_array().unwrap() {
        let equal =
            &fixture_case(&manifest, group["equal_case"].as_str().unwrap())["expected"]["output"];
        let distinct = &fixture_case(&manifest, group["distinct_case"].as_str().unwrap())["expected"]
            ["output"];
        assert_ne!(equal, distinct, "{}", group["id"]);
    }
}

#[test]
fn public_pc2_pc3_pc4_path_expands_without_identity_or_diagnostics() {
    let source = b"lattice: '0.3'\nprofile: lattice-core-0.1\nmodule: public_path\nversion: '1.0.0'\npurpose: Defaults only\nunits:\n  - unit: writer\n    kind: model\nlinks:\n  - link: draft\n";
    let parsed = parse_blueprint_source(source).unwrap();
    let validated = validate_blueprint_source(parsed).unwrap();
    let defaulted = apply_blueprint_defaults(validated);

    assert_eq!(defaulted.as_value()["imports"], json!([]));
    assert_eq!(defaulted.as_value()["inputs"], json!([]));
    assert_eq!(defaulted.as_value()["exports"], json!([]));
    assert_eq!(defaulted.as_value()["units"][0]["mode"], "stateless");
    assert_eq!(defaulted.as_value()["units"][0]["repair_attempts"], 0);
    assert_eq!(defaulted.as_value()["units"][0]["fallback"], false);
    assert_eq!(defaulted.as_value()["links"][0]["mode"], "data");
    assert_eq!(defaulted.as_value()["links"][0]["delivery"], "multicast");
    assert_eq!(defaulted.as_value()["links"][0]["when"], json!({"all": []}));
}
