use super::pc7_fixture_interpreter;
use serde::de::{DeserializeSeed, Error as _, MapAccess, SeqAccess, Visitor};
use serde_json::{Map, Value, json};
use std::collections::{BTreeMap, BTreeSet};
use std::fmt;
use std::fs;
use std::path::{Path, PathBuf};
use threadsmith_canonical::{canonical_bytes, sha256_digest};
use threadsmith_compiler::{
    ExistingLockfileInput, LockedSource, Lockfile, ResolvedSource, lock_source, resolve_source,
};

const PLAN_BYTES: &[u8] =
    include_bytes!("../../../../conformance/pc8/lock/executable_fixture_plan.json");
const PLAN_SHA256: &str = "f95b8feb6d6e012b76239a974eb39f709a50f7ac98a2b6dddddac01e52d1a0f6";
const PLAN_LEN: usize = 542_521;
const REGISTRY_PATH: &str = "docs/pc8/PC8_AUTHORITY_REGISTRY_V2.json";
const REGISTRY_SHA256: &str = "b442f1acb4a7eb316ed9d61da02af3c1e5c60c34f55cf6eefefa751339d0a2c6";
const REGISTRY_LEN: usize = 21_344;
const MANIFEST_PATH: &str = "docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST_V2.json";
const MANIFEST_SHA256: &str = "314e1cd73f23c07067e167d37e84782c7a301b13b4c6458d62a37d0423c4482a";
const MANIFEST_LEN: usize = 1_053_112;
const PC7_MANIFEST_PATH: &str = "docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json";
const PC7_MANIFEST_SHA256: &str =
    "da33daef1526e21a921c8b7bb847045f6e137567f2c0b3b3e6f2af9a796c123c";
const PC7_REGISTRY_PATH: &str = "docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json";
const PC7_REGISTRY_SHA256: &str =
    "7f39265be8bfd6db9fc93cedf357572eb5fab960000b9d6897ef983021112161";
const PC7_PUBLICATION_REPORT_PATH: &str = "/workspace/ThreadSmith/PC7/handoffs/implementation-acceptance-publication/output/THREADSMITH_PC7_IMPLEMENTATION_ACCEPTANCE_PUBLICATION_AND_DURABLE_STATE_UPDATE.txt";
const PC7_PUBLICATION_REPORT_SHA256: &str =
    "7064a32177e39b8ee6dd5a39faca8e93c5511a03b9e7c7df8715b50e9ca79cce";

const CURRENT_IDS: [&str; 20] = [
    "FIX-ALIAS-A",
    "FIX-ALIAS-B",
    "FIX-DUPLICATE-ROWS",
    "FIX-EMPTY",
    "FIX-ID-CHANGED",
    "FIX-MODULE-CHANGED",
    "FIX-MULTIPLICITY-ONE",
    "FIX-MULTIPLICITY-TWO",
    "FIX-ONE-ROOT",
    "FIX-PACKAGE-PREFIX",
    "FIX-PRIOR-RB-A",
    "FIX-PRIOR-RB-B",
    "FIX-REQUEST-ORDER",
    "FIX-REQUIREMENT-CHANGED",
    "FIX-RETRACTED",
    "FIX-ROOT-CHANGED",
    "FIX-ROUTE-FRESH",
    "FIX-ROUTE-LOCK-MISSING",
    "FIX-TRANSITIVE",
    "FIX-VERSION-CHANGED",
];

const FUTURE_IDS: [&str; 4] = [
    "FUT-NONASCII-PACKAGE-ORDER",
    "FUT-PHYSICAL-PERSISTENCE-ADAPTER",
    "FUT-PROFILE-ALTERNATIVE",
    "FUT-PROPER-PREFIX-PACKAGE-VECTOR",
];

#[derive(Clone, Debug)]
pub struct AuthorityInputs {
    pub authority_root: PathBuf,
    pub registry_path: PathBuf,
    pub registry_bytes: Vec<u8>,
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct IntakeRejection {
    pub code: &'static str,
    pub gate: &'static str,
    pub path: String,
    pub reason: &'static str,
    pub fixture_dispatch_started: bool,
}

#[derive(Clone, Debug, Eq, PartialEq)]
pub struct ExecutionSummary {
    pub defined: usize,
    pub generated: usize,
    pub executed: usize,
    pub relations: usize,
    pub future_vectors: usize,
}

fn reject(gate: &'static str, path: impl Into<String>, reason: &'static str) -> IntakeRejection {
    IntakeRejection {
        code: "PC8_EXECUTABLE_FIXTURE_INTAKE_REJECTED",
        gate,
        path: path.into(),
        reason,
        fixture_dispatch_started: false,
    }
}

struct StrictValueSeed;

impl<'de> DeserializeSeed<'de> for StrictValueSeed {
    type Value = Value;

    fn deserialize<D>(self, deserializer: D) -> Result<Self::Value, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        deserializer.deserialize_any(StrictValueVisitor)
    }
}

struct StrictValueVisitor;

impl<'de> Visitor<'de> for StrictValueVisitor {
    type Value = Value;

    fn expecting(&self, formatter: &mut fmt::Formatter<'_>) -> fmt::Result {
        formatter.write_str("one duplicate-free JSON value")
    }

    fn visit_bool<E>(self, value: bool) -> Result<Self::Value, E> {
        Ok(Value::Bool(value))
    }

    fn visit_i64<E>(self, value: i64) -> Result<Self::Value, E> {
        Ok(Value::Number(value.into()))
    }

    fn visit_u64<E>(self, value: u64) -> Result<Self::Value, E> {
        Ok(Value::Number(value.into()))
    }

    fn visit_f64<E>(self, value: f64) -> Result<Self::Value, E>
    where
        E: serde::de::Error,
    {
        serde_json::Number::from_f64(value)
            .map(Value::Number)
            .ok_or_else(|| E::custom("non-finite JSON number"))
    }

    fn visit_str<E>(self, value: &str) -> Result<Self::Value, E> {
        Ok(Value::String(value.to_owned()))
    }

    fn visit_string<E>(self, value: String) -> Result<Self::Value, E> {
        Ok(Value::String(value))
    }

    fn visit_none<E>(self) -> Result<Self::Value, E> {
        Ok(Value::Null)
    }

    fn visit_unit<E>(self) -> Result<Self::Value, E> {
        Ok(Value::Null)
    }

    fn visit_some<D>(self, deserializer: D) -> Result<Self::Value, D::Error>
    where
        D: serde::Deserializer<'de>,
    {
        StrictValueSeed.deserialize(deserializer)
    }

    fn visit_seq<A>(self, mut sequence: A) -> Result<Self::Value, A::Error>
    where
        A: SeqAccess<'de>,
    {
        let mut values = Vec::new();
        while let Some(value) = sequence.next_element_seed(StrictValueSeed)? {
            values.push(value);
        }
        Ok(Value::Array(values))
    }

    fn visit_map<A>(self, mut object: A) -> Result<Self::Value, A::Error>
    where
        A: MapAccess<'de>,
    {
        let mut values = Map::new();
        while let Some(key) = object.next_key::<String>()? {
            if values.contains_key(&key) {
                return Err(A::Error::custom(format!("duplicate member {key}")));
            }
            values.insert(key, object.next_value_seed(StrictValueSeed)?);
        }
        Ok(Value::Object(values))
    }
}

fn strict_json(bytes: &[u8], path: &str) -> Result<Value, IntakeRejection> {
    if bytes.starts_with(&[0xef, 0xbb, 0xbf]) {
        return Err(reject(
            "strict_json",
            path,
            "UTF-8/BOM/JSON/duplicate failure",
        ));
    }
    let mut deserializer = serde_json::Deserializer::from_slice(bytes);
    let value = StrictValueSeed
        .deserialize(&mut deserializer)
        .map_err(|_| reject("strict_json", path, "UTF-8/BOM/JSON/duplicate failure"))?;
    deserializer
        .end()
        .map_err(|_| reject("strict_json", path, "UTF-8/BOM/JSON/duplicate failure"))?;
    Ok(value)
}

fn json_kind(value: &Value) -> &'static str {
    match value {
        Value::Null => "null",
        Value::Bool(_) => "boolean",
        Value::Number(_) => "number",
        Value::String(_) => "string",
        Value::Array(_) => "array",
        Value::Object(_) => "object",
    }
}

fn closed_shape(candidate: &Value, template: &Value, path: &str) -> Result<(), IntakeRejection> {
    if json_kind(candidate) != json_kind(template) {
        return Err(reject(
            "plan_schema",
            path,
            "closed representation category mismatch",
        ));
    }
    match (candidate, template) {
        (Value::Object(candidate), Value::Object(template)) => {
            let candidate_keys = candidate.keys().collect::<BTreeSet<_>>();
            let template_keys = template.keys().collect::<BTreeSet<_>>();
            if candidate_keys != template_keys {
                return Err(reject(
                    "plan_schema",
                    path,
                    "closed representation member mismatch",
                ));
            }
            for (key, expected) in template {
                closed_shape(
                    &candidate[key],
                    expected,
                    &format!("{path}/{}", pointer_token(key)),
                )?;
            }
        }
        (Value::Array(candidate), Value::Array(template)) => {
            if candidate.len() != template.len() {
                return Err(reject(
                    "plan_population",
                    path,
                    "closed representation array length mismatch",
                ));
            }
            for (index, (candidate, template)) in candidate.iter().zip(template).enumerate() {
                closed_shape(candidate, template, &format!("{path}/{index}"))?;
            }
        }
        _ if candidate != template => {
            return Err(reject(
                "plan_schema",
                path,
                "closed representation scalar mismatch",
            ));
        }
        _ => {}
    }
    Ok(())
}

fn pointer_token(value: &str) -> String {
    value.replace('~', "~0").replace('/', "~1")
}

fn expected_root() -> PathBuf {
    PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("../..")
        .canonicalize()
        .expect("repository root")
}

fn exact_bytes(
    path: &Path,
    bytes: usize,
    sha256: &str,
    label: &str,
) -> Result<Vec<u8>, IntakeRejection> {
    let raw = fs::read(path).map_err(|_| {
        reject(
            "authority_document",
            format!("authority#/{label}"),
            "unreadable",
        )
    })?;
    if raw.len() != bytes || sha256_digest(&raw).to_string() != sha256 {
        return Err(reject(
            "authority_document",
            format!("authority#/{label}"),
            "byte count or SHA-256 mismatch",
        ));
    }
    Ok(raw)
}

fn authority_preflight(inputs: &AuthorityInputs) -> Result<(Value, Vec<u8>), IntakeRejection> {
    if inputs.authority_root != expected_root() {
        return Err(reject(
            "authority_root",
            "authority#",
            "wrong authority root",
        ));
    }
    let expected_registry = inputs.authority_root.join(REGISTRY_PATH);
    if inputs.registry_path != expected_registry {
        return Err(reject(
            "registry_path",
            "authority#/registry",
            "wrong fixed registry path",
        ));
    }
    if inputs.registry_bytes.len() != REGISTRY_LEN
        || sha256_digest(&inputs.registry_bytes).to_string() != REGISTRY_SHA256
    {
        return Err(reject(
            "registry_binding",
            "authority#/registry",
            "wrong registry byte binding",
        ));
    }
    if fs::read(&inputs.registry_path).ok().as_deref() != Some(inputs.registry_bytes.as_slice()) {
        return Err(reject(
            "registry_binding",
            "authority#/registry",
            "supplied registry differs from fixed path",
        ));
    }
    let registry = strict_json(&inputs.registry_bytes, "authority#/registry")?;
    if registry["format"] != "threadsmith-pc8-authority-registry-2" {
        return Err(reject(
            "registry_format",
            "authority#/registry/format",
            "wrong registry format",
        ));
    }

    for collection in ["normative_authority", "specified_criteria"] {
        let rows = registry[collection].as_array().ok_or_else(|| {
            reject(
                "registry_schema",
                format!("authority#/registry/{collection}"),
                "required authority collection missing",
            )
        })?;
        for row in rows {
            let key = string_member(row, "key");
            let path = string_member(row, "path");
            let bytes = usize_member(row, "bytes");
            let sha256 = string_member(row, "sha256");
            exact_bytes(&inputs.authority_root.join(path), bytes, sha256, key)?;
        }
    }

    exact_bytes(
        &inputs.authority_root.join(PC7_REGISTRY_PATH),
        2_041,
        PC7_REGISTRY_SHA256,
        "pc7_authority_registry",
    )?;
    exact_bytes(
        Path::new(PC7_PUBLICATION_REPORT_PATH),
        24_874,
        PC7_PUBLICATION_REPORT_SHA256,
        "pc7_implementation_acceptance_publication_report",
    )?;
    let manifest = exact_bytes(
        &inputs.authority_root.join(MANIFEST_PATH),
        MANIFEST_LEN,
        MANIFEST_SHA256,
        "pc8_lock_specified_conformance_manifest_v2",
    )?;
    Ok((registry, manifest))
}

pub fn execute_invocation(inputs: &[AuthorityInputs]) -> Result<ExecutionSummary, IntakeRejection> {
    if inputs.len() != 1 {
        return Err(reject(
            "invocation",
            "invocation#/authority_root",
            "exactly one authority-root input is required",
        ));
    }
    execute_all(&inputs[0])
}

pub fn execute_all(inputs: &AuthorityInputs) -> Result<ExecutionSummary, IntakeRejection> {
    execute_plan_bytes(inputs, PLAN_BYTES)
}

pub fn execute_plan_bytes(
    inputs: &AuthorityInputs,
    plan_bytes: &[u8],
) -> Result<ExecutionSummary, IntakeRejection> {
    let (registry, manifest_bytes) = authority_preflight(inputs)?;
    if plan_bytes.len() != PLAN_LEN || sha256_digest(plan_bytes).to_string() != PLAN_SHA256 {
        return Err(reject(
            "plan_binding",
            "plan#",
            "wrong checked-plan byte binding",
        ));
    }
    let plan = strict_plan_value(plan_bytes)?;
    validate_plan_authority(&plan, &registry)?;
    let manifest = strict_json(&manifest_bytes, "authority#/manifest")?;
    execute_plan(&plan, &manifest)
}

pub fn strict_plan_value(plan_bytes: &[u8]) -> Result<Value, IntakeRejection> {
    let candidate = strict_json(plan_bytes, "plan#")?;
    let template = strict_json(PLAN_BYTES, "checked_plan#")?;
    closed_shape(&candidate, &template, "plan#")?;
    validate_operations(&candidate)?;
    validate_plan_internal_sets(&candidate)?;
    Ok(candidate)
}

pub fn validate_plan_lower_layers_for_discriminator(plan: &Value) -> Result<(), IntakeRejection> {
    validate_operations(plan)?;
    validate_plan_internal_sets(plan)
}

pub fn assert_relation_actual_operand_discriminator() {
    let plan = strict_plan_value(PLAN_BYTES).expect("accepted strict plan");
    let cases = array_member(&plan, "cases");
    let left_case = cases
        .iter()
        .find(|case| string_member(case, "fixture_id") == "FIX-ONE-ROOT")
        .expect("left discriminator case");
    let right_case = cases
        .iter()
        .find(|case| string_member(case, "fixture_id") == "FIX-MODULE-CHANGED")
        .expect("right discriminator case");
    let left = execute_case(left_case);
    let right = execute_case(right_case);
    let relation = array_member(&plan, "relations")
        .iter()
        .find(|relation| string_member(relation, "id") == "REL-REQUESTING-MODULE-CHANGE")
        .expect("discriminator relation");
    let criterion = &relation["scope_results"];
    assert_eq!(relation_scope(&left, &right, criterion), *criterion);

    let mut wrong_left = left.clone();
    wrong_left.lock_id.clone_from(&right.lock_id);
    let actual_counterfactual = relation_scope(&wrong_left, &right, criterion);
    let mut expected_counterfactual = criterion.clone();
    expected_counterfactual["lock_id_equal"] = Value::Bool(true);
    assert_eq!(
        actual_counterfactual, expected_counterfactual,
        "FIX-ONE-ROOT wrong actual lock_id must change exactly lock_id_equal"
    );
    assert_ne!(
        actual_counterfactual, *criterion,
        "an expected-only relation evaluator would false-green this counterfactual"
    );
}

fn validate_operations(plan: &Value) -> Result<(), IntakeRejection> {
    for (index, case) in array_member(plan, "cases").iter().enumerate() {
        match string_member(&case["construction"], "method") {
            "accepted_pc7_fixture_output_expansion"
            | "public_pc2_pc6_plus_pc7_correlated_recipe"
            | "public_pc2_pc7_root_module_correlated_recipe" => {}
            _ => {
                return Err(reject(
                    "plan_operation",
                    format!("plan#/cases/{index}/construction/method"),
                    "unknown construction operation",
                ));
            }
        }
    }
    for (index, relation) in array_member(plan, "relations").iter().enumerate() {
        match string_member(relation, "kind") {
            "admission"
            | "byte_domain_distinction"
            | "direct_projection_nonmembership"
            | "distinction"
            | "encoding"
            | "equivalence"
            | "identity_preimage"
            | "membership"
            | "nondependence"
            | "ordering"
            | "phase_ownership"
            | "totality" => {}
            _ => {
                return Err(reject(
                    "plan_operation",
                    format!("plan#/relations/{index}/kind"),
                    "unknown relation operation",
                ));
            }
        }
    }
    Ok(())
}

fn validate_plan_internal_sets(plan: &Value) -> Result<(), IntakeRejection> {
    let current = CURRENT_IDS
        .into_iter()
        .map(str::to_owned)
        .collect::<BTreeSet<_>>();
    let future = FUTURE_IDS
        .into_iter()
        .map(str::to_owned)
        .collect::<BTreeSet<_>>();
    let cases = array_member(plan, "cases");
    let generated = unique_strings(
        cases.iter().map(|case| string_member(case, "fixture_id")),
        "plan#/cases",
    )?;
    let self_defined = unique_strings(
        string_array(&plan["self_validation"]["defined_fixture_ids"])
            .iter()
            .copied(),
        "plan#/self_validation/defined_fixture_ids",
    )?;
    let self_generated = unique_strings(
        string_array(&plan["self_validation"]["generated_case_ids"])
            .iter()
            .copied(),
        "plan#/self_validation/generated_case_ids",
    )?;
    let excluded = unique_strings(
        string_array(&plan["excluded_future_ids"]).iter().copied(),
        "plan#/excluded_future_ids",
    )?;
    if generated.iter().any(|id| future.contains(id)) {
        return Err(reject(
            "future_dispatch",
            "plan#/cases",
            "future-only fixture entered current dispatch",
        ));
    }
    if generated != current || self_defined != current || self_generated != current {
        return Err(reject(
            "plan_population",
            "plan#/cases",
            "current fixture ID set inequality",
        ));
    }
    if excluded != future {
        return Err(reject(
            "plan_population",
            "plan#/excluded_future_ids",
            "future-only fixture ID set inequality",
        ));
    }
    let relation_ids = unique_strings(
        array_member(plan, "relations")
            .iter()
            .map(|relation| string_member(relation, "id")),
        "plan#/relations",
    )?;
    if relation_ids.len() != 19 {
        return Err(reject(
            "plan_population",
            "plan#/relations",
            "relation population must equal 19",
        ));
    }
    Ok(())
}

fn validate_plan_authority(plan: &Value, registry: &Value) -> Result<(), IntakeRejection> {
    let authority = &plan["authority"];
    let exact = [
        ("registry_path", REGISTRY_PATH),
        ("registry_sha256", REGISTRY_SHA256),
        ("manifest_path", MANIFEST_PATH),
        ("manifest_sha256", MANIFEST_SHA256),
        ("pc7_manifest_path", PC7_MANIFEST_PATH),
        ("pc7_manifest_sha256", PC7_MANIFEST_SHA256),
        ("pc7_registry_path", PC7_REGISTRY_PATH),
        ("pc7_registry_sha256", PC7_REGISTRY_SHA256),
        ("pc7_publication_report_path", PC7_PUBLICATION_REPORT_PATH),
        (
            "pc7_publication_report_sha256",
            PC7_PUBLICATION_REPORT_SHA256,
        ),
    ];
    for (member, expected) in exact {
        if authority[member] != expected {
            return Err(reject(
                "plan_authority",
                format!("plan#/authority/{member}"),
                "plan authority metadata mismatch",
            ));
        }
    }
    if authority["registry_bytes"] != REGISTRY_LEN
        || authority["manifest_bytes"] != MANIFEST_LEN
        || authority["pc7_manifest_bytes"] != 1_306_575
        || authority["pc7_registry_bytes"] != 2_041
        || authority["pc7_publication_report_bytes"] != 24_874
        || authority["dispatch"] != registry["dispatch"]
    {
        return Err(reject(
            "plan_authority",
            "plan#/authority",
            "plan authority size or dispatch metadata mismatch",
        ));
    }
    Ok(())
}

fn execute_plan(plan: &Value, manifest: &Value) -> Result<ExecutionSummary, IntakeRejection> {
    let current = CURRENT_IDS
        .into_iter()
        .map(str::to_owned)
        .collect::<BTreeSet<_>>();
    let defined = unique_strings(
        array_member(manifest, "fixtures")
            .iter()
            .map(|fixture| string_member(fixture, "id")),
        "manifest#/fixtures",
    )?;
    let manifest_relations = unique_strings(
        array_member(manifest, "relations")
            .iter()
            .map(|relation| string_member(relation, "id")),
        "manifest#/relations",
    )?;
    let manifest_future = unique_strings(
        array_member(manifest, "future_only")
            .iter()
            .map(|future| string_member(future, "id")),
        "manifest#/future_only",
    )?;
    if defined != current
        || manifest_relations.len() != 19
        || manifest_future
            != FUTURE_IDS
                .into_iter()
                .map(str::to_owned)
                .collect::<BTreeSet<_>>()
    {
        return Err(reject(
            "manifest_population",
            "manifest#",
            "accepted manifest population closure failed",
        ));
    }

    let mut observations = BTreeMap::new();
    let mut executed = BTreeSet::new();
    for case in array_member(plan, "cases") {
        let fixture_id = string_member(case, "fixture_id");
        if !executed.insert(fixture_id.to_owned()) {
            return Err(reject(
                "execution_population",
                format!("plan#/cases/{fixture_id}"),
                "duplicate fixture execution",
            ));
        }
        let observation = execute_case(case);
        observations.insert(fixture_id.to_owned(), observation);
    }
    if executed != defined || executed != current {
        return Err(reject(
            "execution_population",
            "plan#/cases",
            "defined/generated/executed fixture ID inequality",
        ));
    }

    let mut evaluated_relations = BTreeSet::new();
    for relation in array_member(plan, "relations") {
        evaluate_relation(relation, &observations);
        if !evaluated_relations.insert(string_member(relation, "id").to_owned()) {
            return Err(reject(
                "relation_population",
                "plan#/relations",
                "duplicate relation evaluation",
            ));
        }
    }
    if evaluated_relations != manifest_relations || evaluated_relations.len() != 19 {
        return Err(reject(
            "relation_population",
            "plan#/relations",
            "defined/evaluated relation ID inequality",
        ));
    }

    Ok(ExecutionSummary {
        defined: defined.len(),
        generated: array_member(plan, "cases").len(),
        executed: executed.len(),
        relations: evaluated_relations.len(),
        future_vectors: manifest_future.len(),
    })
}

#[derive(Clone)]
struct ActualObservation {
    source: Value,
    lockfile: Value,
    preimage: Value,
    preimage_bytes: Vec<u8>,
    emitted_bytes: Vec<u8>,
    lock_id: String,
    complete_locked_source: Value,
    roundtrip_admitted: bool,
}

fn execute_case(case: &Value) -> ActualObservation {
    let fixture_id = string_member(case, "fixture_id");
    let construction = &case["construction"];
    let method = string_member(construction, "method");
    let source = match method {
        "accepted_pc7_fixture_output_expansion" => {
            let input = string_member(construction, "resolve_input_id");
            pc7_fixture_interpreter::construct_resolved_source_for_pc8(input, |_| {}, false)
        }
        "public_pc2_pc6_plus_pc7_correlated_recipe" => {
            let input = string_member(construction, "base_resolve_input_id");
            let replacements = construction["exact_root_alias_replacements"]
                .as_object()
                .expect("closed alias replacements");
            pc7_fixture_interpreter::construct_resolved_source_for_pc8(
                input,
                |root| {
                    for import in root["imports"].as_array_mut().expect("root imports") {
                        let alias = import["as"].as_str().expect("root alias");
                        if let Some(replacement) = replacements.get(alias) {
                            import["as"] = replacement.clone();
                        }
                    }
                },
                false,
            )
        }
        "public_pc2_pc7_root_module_correlated_recipe" => {
            let input = string_member(construction, "base_resolve_input_id");
            let raw = string_member(construction, "root_blueprint_source_utf8").as_bytes();
            assert_eq!(
                raw.len(),
                usize_member(construction, "root_blueprint_source_bytes")
            );
            assert_eq!(
                sha256_digest(raw).to_string(),
                string_member(construction, "root_blueprint_source_sha256")
            );
            let root =
                strict_json(raw, "plan#/root_blueprint_source_utf8").expect("closed root recipe");
            pc7_fixture_interpreter::construct_resolved_source_for_pc8(
                input,
                |candidate| *candidate = root,
                false,
            )
        }
        other => panic!("{fixture_id}: unknown construction method {other}"),
    };
    compare_source_then_lock(fixture_id, case, source)
}

fn compare_source_then_lock(
    fixture_id: &str,
    case: &Value,
    source: ResolvedSource,
) -> ActualObservation {
    let actual_source = source.semantic_projection().clone();
    let construction = &case["construction"];
    let input_ref = construction
        .get("resolve_input_id")
        .or_else(|| construction.get("base_resolve_input_id"))
        .and_then(Value::as_str)
        .expect("closed PC7 input recipe");
    let materialized_source = pc7_fixture_interpreter::materialize_resolved_source_for_pc8(
        &case["resolved_source"],
        input_ref,
        &source,
    );
    if actual_source != materialized_source {
        panic!(
            "{fixture_id}: complete actual ResolvedSource before Lock differs at {}",
            first_difference(&actual_source, &materialized_source, "$")
        );
    }
    let preserved = source.clone();
    let scanned_for_roundtrip = source.scanned_source().clone();
    let locked = lock_source(source);
    assert_eq!(
        locked.resolved_source(),
        &preserved,
        "{fixture_id}: source preservation must use the consumed object"
    );
    let observation = observe_locked(
        &locked,
        actual_source,
        string_member(case, "resolved_source_id"),
    );
    let expected = &case["expected"];
    assert_eq!(
        observation.expected_shape, *expected,
        "{fixture_id}: complete actual Lock observation"
    );
    assert_eq!(
        locked.lock_id().as_native_id().digest(),
        sha256_digest(&observation.actual.preimage_bytes),
        "{fixture_id}: omission preimage creates typed Lock identity"
    );
    assert_ne!(
        locked.lock_id().as_native_id().digest(),
        sha256_digest(&observation.actual.emitted_bytes),
        "{fixture_id}: emitted bytes must not create Lock identity"
    );

    let round_tripped = resolve_source(
        scanned_for_roundtrip.clone(),
        ExistingLockfileInput::from_bytes(observation.actual.emitted_bytes.clone()),
    )
    .expect("emitted Lock must pass strict same-context ExistingLockfile intake");
    assert_eq!(round_tripped.scanned_source(), &scanned_for_roundtrip);
    let relocked = lock_source(round_tripped);
    assert_eq!(
        lockfile_value(relocked.lockfile()),
        observation.actual.lockfile,
        "{fixture_id}: round-trip structural Lock observation"
    );
    assert_eq!(
        relocked.lock_id().to_string(),
        observation.actual.lock_id,
        "{fixture_id}: round-trip identity observation"
    );
    assert_eq!(
        relocked.canonical_lockfile_bytes(),
        observation.actual.emitted_bytes,
        "{fixture_id}: round-trip canonical bytes"
    );
    let mut actual = observation.actual;
    actual.roundtrip_admitted = true;
    actual
}

struct ObservedLocked {
    actual: ActualObservation,
    expected_shape: Value,
}

fn observe_locked(
    locked: &LockedSource,
    source: Value,
    resolved_source_id: &str,
) -> ObservedLocked {
    let lockfile = lockfile_value(locked.lockfile());
    let mut preimage = lockfile.clone();
    preimage
        .as_object_mut()
        .expect("Lockfile object")
        .remove("lock_id")
        .expect("emitted Lockfile lock_id");
    let preimage_bytes = canonical_bytes(&preimage).expect("canonical omission preimage");
    let emitted_bytes = locked.canonical_lockfile_bytes().to_vec();
    assert_eq!(emitted_bytes, canonical_bytes(&lockfile).unwrap());
    assert_eq!(
        locked.created_identities(),
        std::slice::from_ref(locked.lock_id())
    );
    assert_eq!(locked.created_artifacts().len(), 1);
    assert_eq!(locked.created_artifacts()[0].lockfile(), locked.lockfile());
    assert!(locked.wrapper_identity().is_none());

    let lock_id = locked.lock_id().to_string();
    let complete_locked_source = json!({
        "authority": locked.authority().as_str(),
        "canonical_lockfile_bytes_hex": hex(&emitted_bytes),
        "created_artifacts": ["canonical_lockfile"],
        "created_identities": [lock_id.clone()],
        "lock_id": lock_id.clone(),
        "lockfile": lockfile.clone(),
        "phase_status": locked.phase_status().as_str(),
        "resolved_source": source.clone(),
        "wrapper_identity": Value::Null,
    });
    let resolved_binding = json!({
        "authority_path": PC7_MANIFEST_PATH,
        "authority_sha256": PC7_MANIFEST_SHA256,
        "binding": "closed_authenticated_construction",
        "expansion": format!("resolved_sources[id={resolved_source_id}].expected_value"),
        "required_member_count": 12,
        "source_ref": resolved_source_id,
    });
    let expected_locked_source = json!({
        "authority": locked.authority().as_str(),
        "canonical_lockfile_bytes_hex": hex(&emitted_bytes),
        "created_artifacts": ["canonical_lockfile"],
        "created_identities": [lock_id.clone()],
        "lock_id": lock_id.clone(),
        "lockfile": lockfile.clone(),
        "phase_status": locked.phase_status().as_str(),
        "resolved_source": resolved_binding,
        "wrapper_identity": Value::Null,
    });
    let expected_shape = json!({
        "emitted_format": {
            "bom": emitted_bytes.starts_with(&[0xef, 0xbb, 0xbf]),
            "insignificant_whitespace": false,
            "trailing_newline": emitted_bytes.ends_with(b"\n"),
            "utf8": std::str::from_utf8(&emitted_bytes).is_ok(),
        },
        "emitted_lockfile_bytes": emitted_bytes.len(),
        "emitted_lockfile_hex": hex(&emitted_bytes),
        "emitted_lockfile_sha256": sha256_digest(&emitted_bytes).to_string(),
        "emitted_lockfile_utf8": std::str::from_utf8(&emitted_bytes).unwrap(),
        "identity_preimage_bytes": preimage_bytes.len(),
        "identity_preimage_hex": hex(&preimage_bytes),
        "identity_preimage_sha256": sha256_digest(&preimage_bytes).to_string(),
        "identity_preimage_utf8": std::str::from_utf8(&preimage_bytes).unwrap(),
        "identity_preimage_value": preimage.clone(),
        "lock_id": lock_id.clone(),
        "locked_source": expected_locked_source,
        "lockfile_value": lockfile.clone(),
        "pc7_existing_lock_roundtrip": {
            "closed_schema": "admitted",
            "context": "admitted",
            "lock_id_verification": "admitted",
            "same_source_context": true,
            "source_intake": "admitted",
        },
    });
    ObservedLocked {
        actual: ActualObservation {
            source,
            lockfile,
            preimage,
            preimage_bytes,
            emitted_bytes,
            lock_id,
            complete_locked_source,
            roundtrip_admitted: false,
        },
        expected_shape,
    }
}

fn lockfile_value(lockfile: &Lockfile) -> Value {
    let packages = lockfile
        .packages()
        .iter()
        .map(|package| {
            let requested_by = package
                .requested_by()
                .iter()
                .map(|request| {
                    json!({
                        "module": request.module(),
                        "requirement": request.requirement(),
                    })
                })
                .collect::<Vec<_>>();
            json!({
                "name": package.name(),
                "package_id": package.package_id().to_string(),
                "requested_by": requested_by,
                "version": package.version(),
            })
        })
        .collect::<Vec<_>>();
    json!({
        "lattice": lockfile.lattice(),
        "lock_id": lockfile.lock_id().to_string(),
        "lock_version": lockfile.lock_version(),
        "packages": packages,
        "profile": lockfile.profile(),
        "root_blueprint_digest": lockfile.root_blueprint_digest().to_string(),
    })
}

fn evaluate_relation(relation: &Value, observations: &BTreeMap<String, ActualObservation>) {
    let relation_id = string_member(relation, "id");
    let refs = string_array(&relation["fixture_refs"]);
    let operands = refs
        .iter()
        .map(|id| observations.get(*id).expect("actual relation operand"))
        .collect::<Vec<_>>();
    if relation_id == "REL-PC7-ROUNDTRIP" {
        assert_eq!(operands.len(), 3);
        assert!(operands.iter().all(|operand| operand.roundtrip_admitted));
        return;
    }
    if operands.len() == 2 {
        let actual = relation_scope(operands[0], operands[1], &relation["scope_results"]);
        assert_eq!(
            actual, relation["scope_results"],
            "{relation_id}: relation evaluated from actual executions"
        );
        return;
    }
    assert_eq!(operands.len(), 1, "{relation_id}: unary relation");
    let actual = operands[0];
    match relation_id {
        "REL-AMBIENT-INDEPENDENCE" => {
            let case_id = refs[0];
            let plan = strict_plan_value(PLAN_BYTES).unwrap();
            let case = array_member(&plan, "cases")
                .iter()
                .find(|case| string_member(case, "fixture_id") == case_id)
                .unwrap();
            let repeated = execute_case(case);
            assert_eq!(
                actual.complete_locked_source,
                repeated.complete_locked_source
            );
        }
        "REL-PERSISTENCE-BOUNDARY" => {
            assert_eq!(
                actual.complete_locked_source["created_artifacts"],
                json!(["canonical_lockfile"])
            );
            assert!(actual.complete_locked_source.get("path").is_none());
            assert!(actual.complete_locked_source["wrapper_identity"].is_null());
        }
        "REL-PREIMAGE-MEMBER-OMISSION" => {
            assert_eq!(actual.preimage.as_object().unwrap().len(), 5);
            assert!(!actual.preimage.as_object().unwrap().contains_key("lock_id"));
            assert_eq!(
                format!(
                    "lattice:lock:sha256:{}",
                    sha256_digest(&actual.preimage_bytes)
                ),
                actual.lock_id
            );
        }
        "REL-PREIMAGE-VERSUS-EMITTED" => {
            assert_ne!(actual.preimage_bytes, actual.emitted_bytes);
            assert_ne!(
                sha256_digest(&actual.preimage_bytes),
                sha256_digest(&actual.emitted_bytes)
            );
        }
        "REL-PRESENTATION-PERMUTATION" => {
            let reversed = pc7_fixture_interpreter::construct_resolved_source_for_pc8(
                "chain_three",
                |_| {},
                true,
            );
            let reversed_source = reversed.semantic_projection().clone();
            assert_eq!(reversed_source, actual.source);
            let reversed_locked = lock_source(reversed);
            assert_eq!(
                reversed_locked.canonical_lockfile_bytes(),
                actual.emitted_bytes
            );
            assert_eq!(reversed_locked.lock_id().to_string(), actual.lock_id);
        }
        "REL-REQUESTED-BY-REORDER" => {
            for package in actual.lockfile["packages"].as_array().unwrap() {
                let rows = package["requested_by"].as_array().unwrap();
                let keys = rows
                    .iter()
                    .map(|row| {
                        (
                            string_member(row, "module").as_bytes(),
                            string_member(row, "requirement").as_bytes(),
                        )
                    })
                    .collect::<Vec<_>>();
                assert!(keys.windows(2).all(|pair| pair[0] <= pair[1]));
            }
        }
        "REL-RETRACTION-EXCLUSION" => {
            assert!(
                actual.source["scanned_source"]["packages"]
                    .as_array()
                    .unwrap()
                    .iter()
                    .any(|record| record["descriptor"]["package"] == "orphan")
            );
            assert!(
                !actual.source["applicable_requirements"]
                    .as_array()
                    .unwrap()
                    .iter()
                    .any(|requirement| requirement["package"] == "orphan")
            );
            assert!(
                !actual.lockfile["packages"]
                    .as_array()
                    .unwrap()
                    .iter()
                    .any(|package| package["name"] == "orphan")
            );
        }
        other => panic!("{other}: unhandled unary relation"),
    }
}

fn relation_scope(left: &ActualObservation, right: &ActualObservation, criterion: &Value) -> Value {
    let mut scope = Map::new();
    scope.insert(
        "complete_locked_source_equal".to_owned(),
        Value::Bool(left.complete_locked_source == right.complete_locked_source),
    );
    scope.insert(
        "emitted_bytes_equal".to_owned(),
        Value::Bool(left.emitted_bytes == right.emitted_bytes),
    );
    scope.insert(
        "identity_preimage_equal".to_owned(),
        Value::Bool(left.preimage_bytes == right.preimage_bytes),
    );
    scope.insert(
        "lock_artifact_projection_equal".to_owned(),
        Value::Bool(left.lockfile == right.lockfile),
    );
    scope.insert(
        "lock_id_equal".to_owned(),
        Value::Bool(left.lock_id == right.lock_id),
    );
    scope.insert(
        "public_pc7_source_equal".to_owned(),
        Value::Bool(left.source == right.source),
    );
    if criterion.get("requested_by_projection_equal").is_some() {
        let left_requested = requested_by_projection(&left.lockfile);
        let right_requested = requested_by_projection(&right.lockfile);
        scope.insert(
            "requested_by_projection_equal".to_owned(),
            Value::Bool(left_requested == right_requested),
        );
    }
    Value::Object(scope)
}

fn requested_by_projection(lockfile: &Value) -> Value {
    Value::Array(
        lockfile["packages"]
            .as_array()
            .unwrap()
            .iter()
            .map(|package| package["requested_by"].clone())
            .collect(),
    )
}

fn first_difference(left: &Value, right: &Value, path: &str) -> String {
    match (left, right) {
        (Value::Object(left), Value::Object(right)) => {
            let keys = left.keys().chain(right.keys()).collect::<BTreeSet<_>>();
            for key in keys {
                match (left.get(key), right.get(key)) {
                    (Some(left), Some(right)) if left != right => {
                        return first_difference(left, right, &format!("{path}.{key}"));
                    }
                    (None, Some(_)) => return format!("{path}.{key} (missing actual)"),
                    (Some(_), None) => return format!("{path}.{key} (unexpected actual)"),
                    _ => {}
                }
            }
            path.to_owned()
        }
        (Value::Array(left), Value::Array(right)) => {
            if left.len() != right.len() {
                return format!("{path}.length ({} != {})", left.len(), right.len());
            }
            for (index, (left, right)) in left.iter().zip(right).enumerate() {
                if left != right {
                    return first_difference(left, right, &format!("{path}[{index}]"));
                }
            }
            path.to_owned()
        }
        _ => format!("{path} ({left} != {right})"),
    }
}

fn unique_strings<'a>(
    values: impl Iterator<Item = &'a str>,
    path: &str,
) -> Result<BTreeSet<String>, IntakeRejection> {
    let values = values.map(str::to_owned).collect::<Vec<_>>();
    let set = values.iter().cloned().collect::<BTreeSet<_>>();
    if values.len() != set.len() {
        return Err(reject(
            "plan_population",
            path,
            "duplicate ID in closed population",
        ));
    }
    Ok(set)
}

fn array_member<'a>(value: &'a Value, member: &str) -> &'a [Value] {
    value[member].as_array().expect("closed array member")
}

fn string_array(value: &Value) -> Vec<&str> {
    value
        .as_array()
        .expect("closed string array")
        .iter()
        .map(|value| value.as_str().expect("closed string item"))
        .collect()
}

fn string_member<'a>(value: &'a Value, member: &str) -> &'a str {
    value[member].as_str().expect("closed string member")
}

fn usize_member(value: &Value, member: &str) -> usize {
    value[member]
        .as_u64()
        .and_then(|value| usize::try_from(value).ok())
        .expect("closed nonnegative size")
}

fn hex(bytes: &[u8]) -> String {
    const DIGITS: &[u8; 16] = b"0123456789abcdef";
    let mut output = String::with_capacity(bytes.len() * 2);
    for byte in bytes {
        output.push(char::from(DIGITS[usize::from(byte >> 4)]));
        output.push(char::from(DIGITS[usize::from(byte & 0x0f)]));
    }
    output
}
