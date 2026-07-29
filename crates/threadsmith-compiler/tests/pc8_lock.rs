use serde_json::{Value, json};
use std::any::TypeId;
use std::path::PathBuf;
use threadsmith_canonical::{canonical_bytes, sha256_digest};
use threadsmith_compiler::{
    ExistingLockfileInput, LockAuthority, LockIdentity, LockPhaseStatus, LockedSource, Lockfile,
    ResolvedSource, SnapshotEntry, SnapshotName, SnapshotNode, acquire_project_snapshot,
    apply_blueprint_defaults, digest_source, lock_source, parse_blueprint_source, resolve_source,
    scan_packages, validate_blueprint_source,
};
use threadsmith_schema::{ArtifactKind, NativeLatticeId};

#[path = "support/pc7_fixture_interpreter.rs"]
#[allow(dead_code)]
mod pc7_fixture_interpreter;
#[path = "support/pc8_fixture_interpreter.rs"]
mod pc8_fixture_interpreter;

const EMPTY_ROOT: &[u8] = br#"{"contracts":[],"exports":[],"imports":[],"inputs":[],"lattice":"0.3","links":[],"module":"root_app","policies":[],"profile":"lattice-core-0.1","purpose":"PC7 specified Resolve criterion","resources":[],"scenarios":[],"units":[],"version":"1.0.0"}"#;
const ONE_ROOT: &[u8] = br#"{"contracts":[],"exports":[],"imports":[{"as":"alpha","use":"alpha","version":"1.0.0"}],"inputs":[],"lattice":"0.3","links":[],"module":"root_app","policies":[],"profile":"lattice-core-0.1","purpose":"PC7 specified Resolve criterion","resources":[],"scenarios":[],"units":[],"version":"1.0.0"}"#;
const ALPHA_100_MODULE: &[u8] = b"lattice: \"0.3\"\nprofile: lattice-core-0.1\nmodule: alpha\nversion: \"1.0.0\"\npurpose: \"alpha package\"\nimports: []\nunits: []\n";

const EMPTY_PREIMAGE: &[u8] = br#"{"lattice":"0.3","lock_version":1,"packages":[],"profile":"lattice-core-0.1","root_blueprint_digest":"lattice:blueprint:sha256:cf45903bf4fe32708c2cb6f9edd1cfba1004c216bebe20142acc29733d049343"}"#;
const EMPTY_EMITTED: &[u8] = br#"{"lattice":"0.3","lock_id":"lattice:lock:sha256:ec6b48665f346ae4fbc96ae17cc1b4ae117bd89325a0a1f4b3b0044d94bcb284","lock_version":1,"packages":[],"profile":"lattice-core-0.1","root_blueprint_digest":"lattice:blueprint:sha256:cf45903bf4fe32708c2cb6f9edd1cfba1004c216bebe20142acc29733d049343"}"#;
const ONE_ROOT_PREIMAGE: &[u8] = br#"{"lattice":"0.3","lock_version":1,"packages":[{"name":"alpha","package_id":"lattice:package:sha256:cab3e435497175f5b42cab078cfd6424d30ad5aba6e0d3886d56c8949397a250","requested_by":[{"module":"root_app","requirement":"1.0.0"}],"version":"1.0.0"}],"profile":"lattice-core-0.1","root_blueprint_digest":"lattice:blueprint:sha256:9db58baa8f7b01eab1ab7598402567997299ad7d229b03dec892b1d3b7598df4"}"#;
const ONE_ROOT_EMITTED: &[u8] = br#"{"lattice":"0.3","lock_id":"lattice:lock:sha256:44ca76221d735f26624b245b8d34f5bcae72c7f847e3d070bc66833962416bad","lock_version":1,"packages":[{"name":"alpha","package_id":"lattice:package:sha256:cab3e435497175f5b42cab078cfd6424d30ad5aba6e0d3886d56c8949397a250","requested_by":[{"module":"root_app","requirement":"1.0.0"}],"version":"1.0.0"}],"profile":"lattice-core-0.1","root_blueprint_digest":"lattice:blueprint:sha256:9db58baa8f7b01eab1ab7598402567997299ad7d229b03dec892b1d3b7598df4"}"#;

trait AmbiguousIfFromNative<Marker> {
    fn marker();
}

impl<T> AmbiguousIfFromNative<()> for T {
    fn marker() {}
}

impl<T: From<NativeLatticeId>> AmbiguousIfFromNative<u8> for T {
    fn marker() {}
}

fn name(value: &str) -> SnapshotName {
    SnapshotName::unicode(value)
}

fn entry(value: &str, node: SnapshotNode) -> SnapshotEntry {
    SnapshotEntry::new(name(value), node)
}

fn directory(children: Vec<SnapshotEntry>) -> SnapshotNode {
    SnapshotNode::directory(children)
}

fn package_entry(name: &str, version: &str, module: Vec<u8>) -> SnapshotEntry {
    let module_digest = sha256_digest(&module).to_hex();
    let descriptor = format!(
        "package: {name}\nversion: \"{version}\"\nlattice: \"0.3\"\nprofiles:\n  - lattice-core-0.1\nmodule_file: module.yaml\nfiles:\n  - path: module.yaml\n    sha256: {module_digest}\n"
    )
    .into_bytes();
    entry(
        name,
        directory(vec![entry(
            version,
            directory(vec![
                entry("package.yaml", SnapshotNode::regular(descriptor)),
                entry("module.yaml", SnapshotNode::regular(module)),
            ]),
        )]),
    )
}

fn module_source(name: &str, version: &str, imports: Vec<Value>) -> Vec<u8> {
    canonical_bytes(&json!({
        "imports": imports,
        "lattice": "0.3",
        "module": name,
        "profile": "lattice-core-0.1",
        "purpose": format!("{name} package"),
        "units": [],
        "version": version,
    }))
    .unwrap()
}

fn root_source(module: &str, purpose: &str, imports: Vec<Value>) -> Vec<u8> {
    canonical_bytes(&json!({
        "contracts": [],
        "exports": [],
        "imports": imports,
        "inputs": [],
        "lattice": "0.3",
        "links": [],
        "module": module,
        "policies": [],
        "profile": "lattice-core-0.1",
        "purpose": purpose,
        "resources": [],
        "scenarios": [],
        "units": [],
        "version": "1.0.0",
    }))
    .unwrap()
}

fn resolve_public(
    root: &[u8],
    packages: Option<SnapshotNode>,
    existing_lockfile: ExistingLockfileInput,
) -> ResolvedSource {
    let parsed = parse_blueprint_source(root).unwrap();
    let validated = validate_blueprint_source(parsed).unwrap();
    let defaulted = apply_blueprint_defaults(validated);
    let digested = digest_source(defaulted);
    let snapshot = acquire_project_snapshot(Ok(packages)).unwrap();
    let scanned = scan_packages(digested, snapshot).unwrap();
    resolve_source(scanned, existing_lockfile).unwrap()
}

fn empty_source() -> ResolvedSource {
    resolve_public(EMPTY_ROOT, None, ExistingLockfileInput::absent())
}

fn one_root_source() -> ResolvedSource {
    resolve_public(
        ONE_ROOT,
        Some(directory(vec![package_entry(
            "alpha",
            "1.0.0",
            ALPHA_100_MODULE.to_vec(),
        )])),
        ExistingLockfileInput::absent(),
    )
}

fn preimage_value(lockfile: &Lockfile) -> Value {
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
        "lock_version": lockfile.lock_version(),
        "packages": packages,
        "profile": lockfile.profile(),
        "root_blueprint_digest": lockfile.root_blueprint_digest().to_string(),
    })
}

fn emitted_value(lockfile: &Lockfile) -> Value {
    let mut emitted = preimage_value(lockfile);
    emitted.as_object_mut().unwrap().insert(
        "lock_id".to_owned(),
        Value::String(lockfile.lock_id().to_string()),
    );
    emitted
}

fn assert_exact_byte_domains(
    locked: &LockedSource,
    expected_preimage: &[u8],
    expected_preimage_hash: &str,
    expected_id: &str,
    expected_emitted: &[u8],
    expected_emitted_hash: &str,
) {
    let preimage = preimage_value(locked.lockfile());
    assert_eq!(preimage.as_object().unwrap().len(), 5);
    assert!(!preimage.as_object().unwrap().contains_key("lock_id"));
    let preimage_bytes = canonical_bytes(&preimage).unwrap();
    let preimage_hash = sha256_digest(&preimage_bytes);
    assert_eq!(preimage_bytes, expected_preimage);
    assert_eq!(preimage_bytes.len(), expected_preimage.len());
    assert_eq!(preimage_hash.to_hex(), expected_preimage_hash);
    assert_eq!(locked.lock_id().to_string(), expected_id);
    assert_eq!(
        locked.lock_id().as_native_id().digest(),
        preimage_hash,
        "Lock identity must be the omission-preimage digest"
    );

    let emitted = emitted_value(locked.lockfile());
    assert_eq!(emitted.as_object().unwrap().len(), 6);
    let emitted_bytes = canonical_bytes(&emitted).unwrap();
    let emitted_hash = sha256_digest(&emitted_bytes);
    assert_eq!(emitted_bytes, expected_emitted);
    assert_eq!(emitted_bytes.len(), expected_emitted.len());
    assert_eq!(emitted_hash.to_hex(), expected_emitted_hash);
    assert_eq!(locked.canonical_lockfile_bytes(), expected_emitted);
    assert_ne!(preimage_bytes, emitted_bytes);
    assert_ne!(preimage_hash, emitted_hash);
    assert_ne!(
        locked.lock_id().as_native_id().digest(),
        emitted_hash,
        "hashing the emitted object must not produce lock_id"
    );
}

#[test]
fn empty_selection_matches_the_exact_frozen_golden_and_complete_observation() {
    let boundary: fn(ResolvedSource) -> LockedSource = lock_source;
    let source = empty_source();
    let preserved = source.clone();
    let projected_root = source
        .scanned_source()
        .digested_source()
        .blueprint_digest()
        .as_native_id()
        .clone();
    let locked = boundary(source);

    assert_eq!(locked.resolved_source(), &preserved);
    assert_eq!(locked.lockfile().lock_version(), 1);
    assert_eq!(locked.lockfile().lattice(), "0.3");
    assert_eq!(locked.lockfile().profile(), preserved.active_profile());
    assert_eq!(locked.lockfile().root_blueprint_digest(), &projected_root);
    assert!(locked.lockfile().packages().is_empty());
    assert_eq!(locked.lockfile().lock_id(), locked.lock_id());
    assert_exact_byte_domains(
        &locked,
        EMPTY_PREIMAGE,
        "ec6b48665f346ae4fbc96ae17cc1b4ae117bd89325a0a1f4b3b0044d94bcb284",
        "lattice:lock:sha256:ec6b48665f346ae4fbc96ae17cc1b4ae117bd89325a0a1f4b3b0044d94bcb284",
        EMPTY_EMITTED,
        "200983274432864025cb8554ae543af102dd851dbccad4920f77b81731eb7292",
    );

    assert_eq!(
        locked.created_identities(),
        std::slice::from_ref(locked.lock_id())
    );
    assert_eq!(locked.created_artifacts().len(), 1);
    assert_eq!(locked.created_artifacts()[0].lockfile(), locked.lockfile());
    assert_eq!(locked.authority(), LockAuthority::None);
    assert_eq!(locked.authority().as_str(), "none");
    assert_eq!(
        locked.phase_status(),
        LockPhaseStatus::NonAuthoritativeLockedSource
    );
    assert_eq!(
        locked.phase_status().as_str(),
        "non_authoritative_locked_source"
    );
    assert!(locked.wrapper_identity().is_none());
}

#[test]
fn one_root_request_matches_the_exact_golden_and_strict_pc7_round_trip() {
    let source = one_root_source();
    let preserved = source.clone();
    let scanned_for_round_trip = source.scanned_source().clone();
    let locked = lock_source(source);

    assert_eq!(locked.resolved_source(), &preserved);
    let packages = locked.lockfile().packages();
    assert_eq!(packages.len(), 1);
    assert_eq!(packages[0].name(), "alpha");
    assert_eq!(packages[0].version(), "1.0.0");
    assert_eq!(
        packages[0].package_id().to_string(),
        "lattice:package:sha256:cab3e435497175f5b42cab078cfd6424d30ad5aba6e0d3886d56c8949397a250"
    );
    assert_eq!(packages[0].requested_by().len(), 1);
    assert_eq!(packages[0].requested_by()[0].module(), "root_app");
    assert_eq!(packages[0].requested_by()[0].requirement(), "1.0.0");
    assert_exact_byte_domains(
        &locked,
        ONE_ROOT_PREIMAGE,
        "44ca76221d735f26624b245b8d34f5bcae72c7f847e3d070bc66833962416bad",
        "lattice:lock:sha256:44ca76221d735f26624b245b8d34f5bcae72c7f847e3d070bc66833962416bad",
        ONE_ROOT_EMITTED,
        "90938eaf2ae9bdad6c7bb7a711c99826330fac7d791f032da22157ba2de0da99",
    );

    let round_tripped = resolve_source(
        scanned_for_round_trip,
        ExistingLockfileInput::from_bytes(locked.canonical_lockfile_bytes().to_vec()),
    )
    .expect("generated bytes must pass strict same-context ExistingLockfile intake");
    assert_ne!(
        round_tripped,
        *locked.resolved_source(),
        "the round trip retains distinct PC7 existing-Lockfile history"
    );
    let relocked = lock_source(round_tripped);
    assert_eq!(
        relocked.canonical_lockfile_bytes(),
        locked.canonical_lockfile_bytes(),
        "prior ExistingLockfile history does not alter Lock projection"
    );
    assert_eq!(relocked.lock_id(), locked.lock_id());
}

#[test]
fn ordering_and_requested_by_projection_preserve_every_occurrence() {
    let root = root_source(
        "z_root",
        "ordering and multiplicity",
        vec![
            json!({"as": "driver", "use": "driver", "version": "1.0.0"}),
            json!({"as": "alpha_caret", "use": "alpha", "version": "^1.0.0"}),
            json!({"as": "alpha_exact_two", "use": "alpha", "version": "1.0.0"}),
            json!({"as": "alpha_exact_one", "use": "alpha", "version": "1.0.0"}),
        ],
    );
    let alpha_module = module_source("alpha", "1.0.0", Vec::new());
    let driver_module = module_source(
        "driver",
        "1.0.0",
        vec![json!({
            "as": "alpha_from_driver",
            "use": "alpha",
            "version": "1.0.0",
        })],
    );
    let source = resolve_public(
        &root,
        Some(directory(vec![
            package_entry("driver", "1.0.0", driver_module),
            package_entry("alpha", "1.0.0", alpha_module),
        ])),
        ExistingLockfileInput::absent(),
    );
    let preserved = source.clone();
    let locked = lock_source(source);

    assert_eq!(locked.resolved_source(), &preserved);
    let packages = locked.lockfile().packages();
    assert_eq!(
        packages
            .iter()
            .map(|package| package.name())
            .collect::<Vec<_>>(),
        ["alpha", "driver"]
    );
    assert_eq!(
        packages[0]
            .requested_by()
            .iter()
            .map(|request| (request.module(), request.requirement()))
            .collect::<Vec<_>>(),
        [
            ("driver", "1.0.0"),
            ("z_root", "1.0.0"),
            ("z_root", "1.0.0"),
            ("z_root", "^1.0.0"),
        ],
        "package contributors use their exact package name and equal root rows remain repeated"
    );
    assert_eq!(
        packages[1]
            .requested_by()
            .iter()
            .map(|request| (request.module(), request.requirement()))
            .collect::<Vec<_>>(),
        [("z_root", "1.0.0")]
    );
    for package in packages {
        let selected = preserved
            .scanned_source()
            .packages()
            .iter()
            .find(|record| record.descriptor().package() == package.name())
            .unwrap();
        assert_eq!(package.version(), selected.descriptor().version());
        assert_eq!(
            package.package_id(),
            selected.identity().as_native_id(),
            "name, version, and package_id come from the same exact selected PC6 record"
        );
    }
}

#[test]
fn profile_and_root_digest_are_projected_from_each_exact_source() {
    let first = empty_source();
    let second = resolve_public(
        &root_source("other_root", "different exact root", Vec::new()),
        None,
        ExistingLockfileInput::absent(),
    );
    let first_profile = first.active_profile().to_owned();
    let second_profile = second.active_profile().to_owned();
    let first_root = first
        .scanned_source()
        .digested_source()
        .blueprint_digest()
        .as_native_id()
        .clone();
    let second_root = second
        .scanned_source()
        .digested_source()
        .blueprint_digest()
        .as_native_id()
        .clone();
    assert_ne!(first_root, second_root);

    let first_locked = lock_source(first);
    let second_locked = lock_source(second);
    assert_eq!(first_locked.lockfile().profile(), first_profile);
    assert_eq!(second_locked.lockfile().profile(), second_profile);
    assert_eq!(first_locked.lockfile().root_blueprint_digest(), &first_root);
    assert_eq!(
        second_locked.lockfile().root_blueprint_digest(),
        &second_root
    );
    assert_ne!(first_locked.lock_id(), second_locked.lock_id());
}

#[test]
fn lock_identity_remains_opaque_against_arbitrary_generic_ids() {
    let locked = lock_source(empty_source());
    let generic = NativeLatticeId::from_canonical_digest(
        ArtifactKind::Lock,
        locked.lock_id().as_native_id().digest(),
    );
    assert_eq!(locked.lock_id().as_native_id(), &generic);
    assert_ne!(
        TypeId::of::<LockIdentity>(),
        TypeId::of::<NativeLatticeId>(),
        "LockIdentity must not be a generic native-ID alias"
    );

    let _ = <LockIdentity as AmbiguousIfFromNative<_>>::marker;
}

fn pc8_authority_inputs() -> pc8_fixture_interpreter::AuthorityInputs {
    let authority_root = PathBuf::from(env!("CARGO_MANIFEST_DIR"))
        .join("../..")
        .canonicalize()
        .expect("repository authority root");
    let registry_path = authority_root.join("docs/pc8/PC8_AUTHORITY_REGISTRY_V2.json");
    let registry_bytes = std::fs::read(&registry_path).expect("accepted V2 registry bytes");
    pc8_fixture_interpreter::AuthorityInputs {
        authority_root,
        registry_path,
        registry_bytes,
    }
}

fn checked_pc8_plan_value() -> Value {
    let inputs = pc8_authority_inputs();
    let bytes = std::fs::read(
        inputs
            .authority_root
            .join("conformance/pc8/lock/executable_fixture_plan.json"),
    )
    .expect("checked PC8 plan");
    serde_json::from_slice(&bytes).expect("checked plan JSON")
}

fn strict_plan_from_value(
    value: &Value,
) -> Result<Value, pc8_fixture_interpreter::IntakeRejection> {
    pc8_fixture_interpreter::strict_plan_value(
        &serde_json::to_vec(value).expect("disposable plan serialization"),
    )
}

#[test]
fn all_current_pc8_fixtures_and_relations_execute_through_public_boundaries() {
    let summary = pc8_fixture_interpreter::execute_all(&pc8_authority_inputs())
        .expect("strict intake and complete public-boundary execution");
    assert_eq!(summary.defined, 20);
    assert_eq!(summary.generated, 20);
    assert_eq!(summary.executed, 20);
    assert_eq!(summary.relations, 19);
    assert_eq!(summary.future_vectors, 4);
}

#[test]
fn preflight_rejects_wrong_root_path_plan_binding_and_repeated_input() {
    let inputs = pc8_authority_inputs();
    let mut wrong_root = inputs.clone();
    wrong_root.authority_root = std::env::temp_dir();
    let rejection = pc8_fixture_interpreter::execute_all(&wrong_root)
        .expect_err("wrong authority root must reject");
    assert_eq!(rejection.gate, "authority_root");
    assert_eq!(rejection.path, "authority#");
    assert_eq!(rejection.reason, "wrong authority root");
    assert!(!rejection.fixture_dispatch_started);

    let mut wrong_path = inputs.clone();
    wrong_path.registry_path = inputs.authority_root.join("wrong-registry.json");
    let rejection = pc8_fixture_interpreter::execute_all(&wrong_path)
        .expect_err("wrong registry path must reject");
    assert_eq!(rejection.gate, "registry_path");
    assert_eq!(rejection.path, "authority#/registry");
    assert!(!rejection.fixture_dispatch_started);

    let mut changed_plan = std::fs::read(
        inputs
            .authority_root
            .join("conformance/pc8/lock/executable_fixture_plan.json"),
    )
    .unwrap();
    changed_plan.push(b' ');
    let rejection = pc8_fixture_interpreter::execute_plan_bytes(&inputs, &changed_plan)
        .expect_err("wrong checked-plan bytes must reject");
    assert_eq!(rejection.gate, "plan_binding");
    assert_eq!(rejection.path, "plan#");
    assert!(!rejection.fixture_dispatch_started);

    for invocation in [Vec::new(), vec![inputs.clone(), inputs]] {
        let rejection = pc8_fixture_interpreter::execute_invocation(&invocation)
            .expect_err("invocation requires exactly one authority root");
        assert_eq!(rejection.gate, "invocation");
        assert_eq!(rejection.path, "invocation#/authority_root");
        assert!(!rejection.fixture_dispatch_started);
    }
}

#[test]
fn strict_plan_intake_rejects_duplicate_unknown_missing_and_malformed_variants() {
    let inputs = pc8_authority_inputs();
    let plan_path = inputs
        .authority_root
        .join("conformance/pc8/lock/executable_fixture_plan.json");
    let mut duplicate = std::fs::read_to_string(plan_path).unwrap();
    let needle = "  \"fixture_plan_version\": ";
    assert_eq!(duplicate.matches(needle).count(), 1);
    duplicate = duplicate.replacen(
        needle,
        "  \"fixture_plan_version\": \"duplicate\",\n  \"fixture_plan_version\": ",
        1,
    );
    let rejection = pc8_fixture_interpreter::strict_plan_value(duplicate.as_bytes())
        .expect_err("duplicate JSON member must reject");
    assert_eq!(rejection.gate, "strict_json");
    assert_eq!(rejection.path, "plan#");

    let mut unknown = checked_pc8_plan_value();
    unknown
        .as_object_mut()
        .unwrap()
        .insert("unexpected".to_owned(), Value::Null);
    let rejection = strict_plan_from_value(&unknown).expect_err("unknown member must reject");
    assert_eq!(rejection.gate, "plan_schema");
    assert_eq!(rejection.path, "plan#");

    let mut missing = checked_pc8_plan_value();
    missing
        .as_object_mut()
        .unwrap()
        .remove("fixture_plan_version");
    let rejection = strict_plan_from_value(&missing).expect_err("missing member must reject");
    assert_eq!(rejection.gate, "plan_schema");
    assert_eq!(rejection.path, "plan#");

    let mut wrong_scalar = checked_pc8_plan_value();
    assert_eq!(
        wrong_scalar["cases"][0]["expected"]["emitted_lockfile_bytes"],
        Value::from(534_u64)
    );
    wrong_scalar["cases"][0]["expected"]["emitted_lockfile_bytes"] = Value::from(535_u64);
    let rejection = match strict_plan_from_value(&wrong_scalar) {
        Ok(_) => panic!("wrong expected scalar must reject during strict semantic plan intake"),
        Err(rejection) => rejection,
    };
    assert_eq!(rejection.gate, "plan_schema");
    assert_eq!(
        rejection.path,
        "plan#/cases/0/expected/emitted_lockfile_bytes"
    );
    assert!(!rejection.fixture_dispatch_started);

    let mut operation = checked_pc8_plan_value();
    operation["relations"][0]["kind"] = Value::String("future_relation_kind".to_owned());
    let rejection =
        strict_plan_from_value(&operation).expect_err("unknown relation variant must reject");
    assert_eq!(rejection.gate, "plan_schema");
    assert_eq!(rejection.path, "plan#/relations/0/kind");
    assert!(!rejection.fixture_dispatch_started);
    let rejection =
        pc8_fixture_interpreter::validate_plan_lower_layers_for_discriminator(&operation)
            .expect_err("unknown relation variant must fail closed at the operation layer");
    assert_eq!(rejection.gate, "plan_operation");
    assert_eq!(rejection.path, "plan#/relations/0/kind");
    assert!(!rejection.fixture_dispatch_started);

    let mut construction = checked_pc8_plan_value();
    construction["cases"][0]["construction"]["method"] =
        Value::String("future_construction".to_owned());
    let rejection =
        strict_plan_from_value(&construction).expect_err("unknown construction must reject");
    assert_eq!(rejection.gate, "plan_schema");
    assert_eq!(rejection.path, "plan#/cases/0/construction/method");
    assert!(!rejection.fixture_dispatch_started);
    let rejection =
        pc8_fixture_interpreter::validate_plan_lower_layers_for_discriminator(&construction)
            .expect_err("unknown construction must fail closed at the operation layer");
    assert_eq!(rejection.gate, "plan_operation");
    assert_eq!(rejection.path, "plan#/cases/0/construction/method");
    assert!(!rejection.fixture_dispatch_started);
}

#[test]
fn plan_population_closure_rejects_duplicate_skip_future_and_relation_loss() {
    let mut duplicate = checked_pc8_plan_value();
    duplicate["cases"][1]["fixture_id"] = duplicate["cases"][0]["fixture_id"].clone();
    let rejection = strict_plan_from_value(&duplicate).expect_err("duplicate ID must reject");
    assert_eq!(rejection.gate, "plan_schema");
    assert_eq!(rejection.path, "plan#/cases/1/fixture_id");
    assert!(!rejection.fixture_dispatch_started);
    let rejection =
        pc8_fixture_interpreter::validate_plan_lower_layers_for_discriminator(&duplicate)
            .expect_err("duplicate ID must fail closed at the population layer");
    assert_eq!(rejection.gate, "plan_population");
    assert_eq!(rejection.path, "plan#/cases");
    assert!(!rejection.fixture_dispatch_started);

    let mut skipped = checked_pc8_plan_value();
    skipped["cases"].as_array_mut().unwrap().remove(0);
    let rejection = strict_plan_from_value(&skipped).expect_err("skipped case must reject");
    assert_eq!(rejection.gate, "plan_population");
    assert_eq!(rejection.path, "plan#/cases");

    let mut future = checked_pc8_plan_value();
    future["cases"][0]["fixture_id"] = Value::String("FUT-NONASCII-PACKAGE-ORDER".to_owned());
    let rejection = strict_plan_from_value(&future).expect_err("future dispatch must reject");
    assert_eq!(rejection.gate, "plan_schema");
    assert_eq!(rejection.path, "plan#/cases/0/fixture_id");
    assert!(!rejection.fixture_dispatch_started);
    let rejection = pc8_fixture_interpreter::validate_plan_lower_layers_for_discriminator(&future)
        .expect_err("future fixture must fail closed at the future-dispatch layer");
    assert_eq!(rejection.gate, "future_dispatch");
    assert_eq!(rejection.path, "plan#/cases");
    assert!(!rejection.fixture_dispatch_started);

    let mut relation = checked_pc8_plan_value();
    relation["relations"].as_array_mut().unwrap().remove(0);
    let rejection = strict_plan_from_value(&relation).expect_err("relation loss must reject");
    assert_eq!(rejection.gate, "plan_population");
    assert_eq!(rejection.path, "plan#/relations");
}

#[test]
fn relation_counterfactual_is_rejected_by_actual_execution_operands() {
    pc8_fixture_interpreter::assert_relation_actual_operand_discriminator();
}
