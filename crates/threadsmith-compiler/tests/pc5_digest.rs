use serde_json::Value;
use serde_json::{Map, json};
use std::collections::BTreeMap;
use threadsmith_compiler::{
    DigestedSource, apply_blueprint_defaults, digest_source, parse_blueprint_source,
    validate_blueprint_source,
};
use threadsmith_schema::ArtifactKind;

const FIXTURES: &str = include_str!("../../../conformance/pc5/digest/fixture_manifest.json");

fn fixture_manifest() -> Value {
    serde_json::from_str(FIXTURES).unwrap()
}

fn digest_yaml(source: &str) -> DigestedSource {
    let parsed = parse_blueprint_source(source.as_bytes()).unwrap();
    let validated = validate_blueprint_source(parsed).unwrap();
    let defaulted = apply_blueprint_defaults(validated);
    digest_source(defaulted)
}

fn expected_digest_text(sha256: &str) -> String {
    format!("lattice:blueprint:sha256:{sha256}")
}

fn raw_root() -> Value {
    json!({
        "lattice": "0.3",
        "profile": "lattice-core-0.1",
        "module": "raw_domain_probe",
        "version": "1.0.0",
        "purpose": "Boundary admission probe",
        "units": [{"unit": "probe", "kind": "program"}]
    })
}

fn assert_raw_domain_rejected_without_panic(value: Value, expected_path: &str) {
    let result = std::panic::catch_unwind(|| validate_blueprint_source(value));
    let diagnostic = result
        .expect("raw Value admission must fail closed without panicking")
        .expect_err("out-of-domain raw Value must not construct ValidatedSource");
    assert_eq!(diagnostic.code, "SOURCE_VALUE_DOMAIN_INVALID");
    assert_eq!(diagnostic.path, expected_path);
    assert_eq!((diagnostic.line, diagnostic.column), (None, None));
}

#[test]
fn public_pipeline_converges_for_every_equivalent_source_and_binds_exact_input() {
    let manifest = fixture_manifest();
    let minimum_runs =
        manifest["implementation_test_requirements"]["minimum_digest_runs_per_reachable_source"]
            .as_u64()
            .unwrap();
    assert_eq!(minimum_runs, 3);

    for group in manifest["source_equivalence_groups"].as_array().unwrap() {
        let expected_value = &group["expected_defaulted_value"];
        let expected_text = group["blueprint_digest"].as_str().unwrap();
        let mut observed = None;

        for case in group["cases"].as_array().unwrap() {
            let id = case["id"].as_str().unwrap();
            for _ in 0..minimum_runs {
                let source = case["source_yaml"].as_str().unwrap();
                let parsed = parse_blueprint_source(source.as_bytes())
                    .unwrap_or_else(|error| panic!("{id}: PC2 rejected fixture: {error:?}"));
                let validated = validate_blueprint_source(parsed)
                    .unwrap_or_else(|error| panic!("{id}: PC3 rejected fixture: {error:?}"));
                let defaulted = apply_blueprint_defaults(validated);
                assert_eq!(defaulted.as_value(), expected_value, "{id}: PC4 value");
                let exact_input = defaulted.clone();

                let digested = digest_source(defaulted);
                assert_eq!(digested.defaulted_source(), &exact_input, "{id}: binding");
                assert_eq!(
                    digested.blueprint_digest().to_string(),
                    expected_text,
                    "{id}"
                );
                assert_eq!(
                    digested.blueprint_digest().as_native_id().kind(),
                    ArtifactKind::Blueprint,
                    "{id}: kind"
                );
                assert_eq!(
                    digested.blueprint_digest().as_native_id().to_string(),
                    expected_text,
                    "{id}: native representation"
                );
                assert_eq!(
                    digested.clone().into_defaulted_source(),
                    exact_input,
                    "{id}: consuming source accessor"
                );

                if let Some(previous) = &observed {
                    assert_eq!(digested.blueprint_digest(), previous, "{id}: repeatability");
                } else {
                    observed = Some(digested.blueprint_digest().clone());
                }
            }
        }
    }
}

#[test]
fn every_reachable_distinction_has_its_exact_digest_and_preserved_array_order() {
    let manifest = fixture_manifest();
    let minimum_runs =
        manifest["implementation_test_requirements"]["minimum_digest_runs_per_reachable_source"]
            .as_u64()
            .unwrap();
    let mut digests = BTreeMap::new();

    for case in manifest["digest_distinction_cases"].as_array().unwrap() {
        let id = case["id"].as_str().unwrap();
        let expected = expected_digest_text(case["sha256"].as_str().unwrap());
        for _ in 0..minimum_runs {
            let digested = digest_yaml(case["source_yaml"].as_str().unwrap());
            assert_eq!(digested.blueprint_digest().to_string(), expected, "{id}");
            if id == "array_order_alpha_beta" {
                assert_eq!(
                    digested.defaulted_source().as_value()["units"][0]["unit"],
                    "alpha"
                );
                assert_eq!(
                    digested.defaulted_source().as_value()["units"][1]["unit"],
                    "beta"
                );
            }
            if id == "array_order_beta_alpha" {
                assert_eq!(
                    digested.defaulted_source().as_value()["units"][0]["unit"],
                    "beta"
                );
                assert_eq!(
                    digested.defaulted_source().as_value()["units"][1]["unit"],
                    "alpha"
                );
            }
        }
        digests.insert(id, expected);
    }

    let baseline = manifest["source_equivalence_groups"][0]["blueprint_digest"]
        .as_str()
        .unwrap();
    for case in manifest["digest_distinction_cases"].as_array().unwrap() {
        let id = case["id"].as_str().unwrap();
        let other = case["must_differ_from"].as_str().unwrap();
        let other_digest = if other == "presentation_and_default_equivalence" {
            baseline
        } else {
            digests.get(other).unwrap().as_str()
        };
        assert_ne!(
            digests.get(id).unwrap().as_str(),
            other_digest,
            "{id} versus {other}"
        );
    }
}

#[test]
fn alternate_profile_is_rejected_by_pc3_without_forging_pc5_input() {
    let manifest = fixture_manifest();
    let boundary = &manifest["profile_boundary"];
    let source = boundary["pc3_rejection_source_yaml"].as_str().unwrap();
    let parsed = parse_blueprint_source(source.as_bytes()).unwrap();
    let diagnostic = validate_blueprint_source(parsed).unwrap_err();
    assert_eq!(
        diagnostic.code,
        boundary["expected_pc3_diagnostic"]["code"]
            .as_str()
            .unwrap()
    );
    assert_eq!(
        diagnostic.path,
        boundary["expected_pc3_diagnostic"]["path"]
            .as_str()
            .unwrap()
    );
    assert_eq!((diagnostic.line, diagnostic.column), (None, None));
}

#[test]
fn every_later_invalid_source_is_digestible_without_pc5_diagnostics() {
    let manifest = fixture_manifest();
    let minimum_runs =
        manifest["implementation_test_requirements"]["minimum_digest_runs_per_reachable_source"]
            .as_u64()
            .unwrap();

    for case in manifest["later_invalid_but_digestible_cases"]
        .as_array()
        .unwrap()
    {
        let id = case["id"].as_str().unwrap();
        let expected = expected_digest_text(case["sha256"].as_str().unwrap());
        let mut previous = None;
        for _ in 0..minimum_runs {
            let digested = digest_yaml(case["source_yaml"].as_str().unwrap());
            assert_eq!(digested.blueprint_digest().to_string(), expected, "{id}");
            if let Some(previous) = &previous {
                assert_eq!(digested.blueprint_digest(), previous, "{id}: repeatability");
            } else {
                previous = Some(digested.blueprint_digest().clone());
            }
        }
    }
}

#[test]
fn raw_values_outside_the_pc2_domain_cannot_reach_pc5() {
    let mut floating = raw_root();
    floating["units"][0]["value"] = json!(1.5);
    assert_raw_domain_rejected_without_panic(floating, "/units/0/value");

    for integer in ["9223372036854775808", "-9223372036854775809"] {
        let mut out_of_range = raw_root();
        out_of_range["units"][0]["value"] = serde_json::from_str(integer).unwrap();
        assert_raw_domain_rejected_without_panic(out_of_range, "/units/0/value");
    }

    let mut non_nfc_string = raw_root();
    non_nfc_string["units"][0]["description"] = json!("Cafe\u{301}");
    assert_raw_domain_rejected_without_panic(non_nfc_string, "/units/0/description");

    let mut non_nfc_key = raw_root();
    non_nfc_key["units"][0]
        .as_object_mut()
        .unwrap()
        .insert("Cafe\u{301}".to_owned(), json!(true));
    assert_raw_domain_rejected_without_panic(non_nfc_key, "/units/0/Cafe\u{301}");

    let mut colliding = Map::new();
    colliding.insert("Cafe\u{301}".to_owned(), json!(1));
    colliding.insert("Café".to_owned(), json!(2));
    let mut collision = raw_root();
    collision["units"][0]["metadata"] = Value::Object(colliding);
    assert_raw_domain_rejected_without_panic(collision, "/units/0/metadata/Café");
}

#[test]
fn genuine_pc2_domain_admission_preserves_normalization_and_parser_rejections() {
    let normalized = digest_yaml(
        "lattice: '0.3'\nprofile: lattice-core-0.1\nmodule: normalized\nversion: '1.0.0'\npurpose: 'Cafe\u{301}'\nunits: []\n",
    );
    assert_eq!(normalized.defaulted_source().as_value()["purpose"], "Café");

    for source in [
        "lattice: '0.3'\nprofile: lattice-core-0.1\nmodule: rejected\nversion: '1.0.0'\npurpose: float\nunits:\n  - value: 1.5\n",
        "lattice: '0.3'\nprofile: lattice-core-0.1\nmodule: rejected\nversion: '1.0.0'\npurpose: integer\nunits:\n  - value: 9223372036854775808\n",
        "lattice: '0.3'\nprofile: lattice-core-0.1\nmodule: rejected\nversion: '1.0.0'\npurpose: collision\nunits:\n  - Café: 1\n    Cafe\u{301}: 2\n",
    ] {
        assert!(parse_blueprint_source(source.as_bytes()).is_err());
    }
}
