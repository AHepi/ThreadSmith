#!/usr/bin/env python3
"""Build and mechanically verify the closed PC6 executable-fixture plan."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
from typing import Any


REPO = Path(__file__).resolve().parents[3]
MANIFEST_PATH = REPO / "conformance/pc6/package_scan/fixture_manifest.json"
PLAN_PATH = REPO / "conformance/pc6/package_scan/executable_fixture_plan.json"
AUTHORITY_PATH = (
    REPO
    / "docs/standard/LATTICE_STANDARD_0.3_PACKAGE_SCAN_SEMANTICS_ERRATUM.md"
)

DS_A = """lattice: "0.3"
profile: lattice-core-0.1
module: root
version: "1.0.0"
purpose: fixture root
units: []
"""

DS_B = """lattice: "0.3"
profile: lattice-core-0.1
module: root
version: "1.0.0"
purpose: fixture root b
units: []
"""

MODULE_DIGEST = "900dd3893a719ec7ea1cb5acff8ec799223d6b8d3f3c6dea3eb09f2d06b67b55"
EMPTY_DIGEST = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
DATA_DIGEST = "c0ef28aa04fc0e12e57ea295ae9f356b09271cd19a6b7996ab3a365a2d88ee73"
DATA_CHANGED_DIGEST = (
    "792ef13d8b723ba31c6e2c37865aa3fc7d027ea2b04a23969ba9aa63e487e9b2"
)
DP = "packages/alpha/1.0.0/package.yaml"
MP = "packages/alpha/1.0.0/module.yaml"


def sha256_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def const(name: str) -> dict[str, Any]:
    return {"kind": "constant", "name": name}


def exact_hex(value: str) -> dict[str, Any]:
    return {"kind": "hex", "value": value}


def utf8(value: str) -> dict[str, Any]:
    return {"kind": "utf8", "value": value}


def concat(*parts: dict[str, Any]) -> dict[str, Any]:
    return {"kind": "concat", "parts": list(parts)}


def replace(
    source: dict[str, Any], old: str, new: str
) -> dict[str, Any]:
    return {
        "kind": "replace_utf8",
        "source": source,
        "old": old,
        "new": new,
    }


def insert_after(
    source: dict[str, Any], anchor: str, text: str
) -> dict[str, Any]:
    return {
        "kind": "insert_utf8_after",
        "source": source,
        "anchor": anchor,
        "text": text,
    }


def delete(source: dict[str, Any], text: str) -> dict[str, Any]:
    return {"kind": "delete_utf8_exact", "source": source, "text": text}


def bd(
    package: str,
    version: str,
    profiles: list[str],
    module_file: str,
    files: list[tuple[str, str]],
) -> dict[str, Any]:
    return {
        "kind": "bd",
        "package": package,
        "version": version,
        "profiles": profiles,
        "module_file": module_file,
        "files": [
            {"path": path, "sha256": digest} for path, digest in files
        ],
    }


def bdp(path_scalar_source: str) -> dict[str, Any]:
    return {"kind": "bdp", "path_scalar_source": path_scalar_source}


def bdf(
    module_file_scalar_source: str,
    files: list[tuple[str, str]],
) -> dict[str, Any]:
    return {
        "kind": "bdf",
        "module_file_scalar_source": module_file_scalar_source,
        "files": [
            {
                "path_scalar_source": path,
                "sha256_scalar_source": digest,
            }
            for path, digest in files
        ],
    }


def directory() -> dict[str, Any]:
    return {"kind": "directory", "children": []}


def directory_unreadable() -> dict[str, Any]:
    return {"kind": "directory_unreadable"}


def regular(
    bytes_expression: dict[str, Any], hardlink_group: str | None = None
) -> dict[str, Any]:
    return {
        "kind": "regular",
        "bytes": bytes_expression,
        "hardlink_group": hardlink_group,
    }


def regular_unreadable() -> dict[str, Any]:
    return {"kind": "regular_unreadable"}


def link(target: str) -> dict[str, Any]:
    return {"kind": "link", "target": target}


def special(kind: str) -> dict[str, Any]:
    return {"kind": "special", "special_kind": kind}


def add(path: str, node: dict[str, Any]) -> dict[str, Any]:
    return {"op": "add", "path": path, "node": node}


def remove(path: str) -> dict[str, Any]:
    return {"op": "remove", "path": path}


def replace_node(path: str, node: dict[str, Any]) -> dict[str, Any]:
    return {"op": "replace_node", "path": path, "node": node}


def replace_hex(path: str, value: dict[str, Any]) -> dict[str, Any]:
    return {"op": "replace_hex", "path": path, "bytes": value}


def set_descriptor(
    value: dict[str, Any], path: str = DP
) -> dict[str, Any]:
    return {"op": "set_descriptor", "path": path, "bytes": value}


def rename(path: str, new_final_component: str) -> dict[str, Any]:
    return {
        "op": "rename",
        "path": path,
        "new_final_component": new_final_component,
    }


def enumerate_children(path: str, names: list[str]) -> dict[str, Any]:
    return {"op": "set_child_enumeration", "path": path, "names": names}


def share_hardlink(
    path_a: str, path_b: str, group_id: str
) -> dict[str, Any]:
    return {
        "op": "share_hardlink",
        "path_a": path_a,
        "path_b": path_b,
        "group_id": group_id,
    }


def run(
    *,
    source: str = "DS-A",
    base: str = "T-MINIMAL",
    operations: list[dict[str, Any]] | None = None,
    timing: str = "normal",
    live_operations: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    return {
        "source": source,
        "base": base,
        "operations": operations or [],
        "timing": timing,
        "live_operations": live_operations or [],
    }


def expected_file(
    path: str, digest: str, byte_constant: str
) -> dict[str, Any]:
    return {
        "path": path,
        "sha256": digest,
        "byte_constant": byte_constant,
    }


def expected_package(
    identity: str,
    package: str,
    version: str,
    profiles: list[str],
    module_file: str,
    files: list[dict[str, Any]],
    canonical_vector: str | None = None,
) -> dict[str, Any]:
    return {
        "identity": identity,
        "package": package,
        "version": version,
        "lattice": "0.3",
        "profiles": profiles,
        "module_file": module_file,
        "files": files,
        "canonical_vector": canonical_vector,
    }


def base_snapshots() -> dict[str, list[dict[str, Any]]]:
    minimal = [
        add("packages", directory()),
        add("packages/alpha", directory()),
        add("packages/alpha/1.0.0", directory()),
        add(DP, regular(const("D_MIN"))),
        add(MP, regular(const("M_ALPHA_100"))),
    ]
    multiple_packages = copy.deepcopy(minimal) + [
        add("packages/beta", directory()),
        add("packages/beta/2.0.0", directory()),
        add(
            "packages/beta/2.0.0/package.yaml",
            regular(const("D_BETA_200")),
        ),
        add(
            "packages/beta/2.0.0/module.yaml",
            regular(const("M_BETA_200")),
        ),
    ]
    multiple_versions = copy.deepcopy(minimal) + [
        add("packages/alpha/1.1.0", directory()),
        add(
            "packages/alpha/1.1.0/package.yaml",
            regular(const("D_ALPHA_110")),
        ),
        add(
            "packages/alpha/1.1.0/module.yaml",
            regular(const("M_ALPHA_110")),
        ),
    ]
    multi_file = [
        add("packages", directory()),
        add("packages/text_tools", directory()),
        add("packages/text_tools/1.3.1", directory()),
        add(
            "packages/text_tools/1.3.1/package.yaml",
            regular(const("D_MULTI")),
        ),
        add(
            "packages/text_tools/1.3.1/module.yaml",
            regular(const("M_TEXT_TOOLS")),
        ),
        add(
            "packages/text_tools/1.3.1/empty.txt",
            regular(const("EMPTY")),
        ),
        add("packages/text_tools/1.3.1/validators", directory()),
        add(
            "packages/text_tools/1.3.1/validators/no_bullets.py",
            regular(const("V_NO_BULLETS")),
        ),
    ]
    hardlink = [
        add("packages", directory()),
        add("packages/alpha", directory()),
        add("packages/alpha/1.0.0", directory()),
        add(DP, regular(const("D_HARDLINK"))),
        add(MP, regular(const("M_ALPHA_100"))),
        add(
            "packages/alpha/1.0.0/a.txt",
            regular(const("DATA")),
        ),
        add(
            "packages/alpha/1.0.0/b.txt",
            regular(const("DATA")),
        ),
        share_hardlink(
            "packages/alpha/1.0.0/a.txt",
            "packages/alpha/1.0.0/b.txt",
            "h1",
        ),
    ]
    version_order = [
        add("packages", directory()),
        add("packages/alpha", directory()),
        add("packages/alpha/2.0.0", directory()),
        add(
            "packages/alpha/2.0.0/package.yaml",
            regular(const("D_ALPHA_2_0_0")),
        ),
        add(
            "packages/alpha/2.0.0/module.yaml",
            regular(const("M_ALPHA_100")),
        ),
        add("packages/alpha/10.0.0", directory()),
        add(
            "packages/alpha/10.0.0/package.yaml",
            regular(const("D_ALPHA_10_0_0")),
        ),
        add(
            "packages/alpha/10.0.0/module.yaml",
            regular(const("M_ALPHA_100")),
        ),
    ]
    return {
        "T-ABSENT": [],
        "T-EMPTY": [add("packages", directory())],
        "T-MINIMAL": minimal,
        "T-MULTIPLE-PACKAGES": multiple_packages,
        "T-MULTIPLE-VERSIONS": multiple_versions,
        "T-MULTI-FILE": multi_file,
        "T-HARDLINK": hardlink,
        "T-VERSION-ORDER": version_order,
    }


def expected_packages() -> dict[str, dict[str, Any]]:
    core = ["lattice-core-0.1"]
    module = [expected_file("module.yaml", MODULE_DIGEST, "M_ALPHA_100")]
    return {
        "minimal": expected_package(
            "lattice:package:sha256:bc7d7188c96584fee6acac5686f621199fc4bb64f15fa598392543b439e6053b",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            module,
            "minimal",
        ),
        "alpha_1_1_0": expected_package(
            "lattice:package:sha256:10cb5b7f8f6d9074d1bb625770af63fa84573dce7f356db9f1a51829e0e9f399",
            "alpha",
            "1.1.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "module.yaml",
                    "bcf3b8591ddedb2f578fb75ec773abea499b82b6baaaee9f4a5fcb0e60efe551",
                    "M_ALPHA_110",
                )
            ],
        ),
        "alpha_2_0_0": expected_package(
            "lattice:package:sha256:0a31f8322ed848d6323494da7cb09d3fda11d9b4a9fd3af8c1bc7ea8d5d29752",
            "alpha",
            "2.0.0",
            core,
            "module.yaml",
            module,
            "numeric_2",
        ),
        "alpha_10_0_0": expected_package(
            "lattice:package:sha256:842fa7fd5f1adcbd0e5e49bf0f4417cb99cf85fe6cd8bf78773f7032f0c6f407",
            "alpha",
            "10.0.0",
            core,
            "module.yaml",
            module,
            "numeric_10",
        ),
        "beta_2_0_0": expected_package(
            "lattice:package:sha256:9621803973e05eb15944c11533c5eaf2c4a65d578323d8e6730a822e877b9ef4",
            "beta",
            "2.0.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "module.yaml",
                    "80d80984355a2fce54a4b9c03c75ff4f880e155bd0c668efbf7404183f353e85",
                    "M_BETA_200",
                )
            ],
        ),
        "multi_file": expected_package(
            "lattice:package:sha256:ba06b60802e90ec39f691566ee0a30785711c8e5816799ec9c0abe7e1fbc92b8",
            "text_tools",
            "1.3.1",
            ["lattice-builder-0.1", "lattice-core-0.1"],
            "module.yaml",
            [
                expected_file("empty.txt", EMPTY_DIGEST, "EMPTY"),
                expected_file(
                    "module.yaml",
                    "bfeaac869e4dffdda7420438e2ee780adcd958d0c67acda9a717c78e0d177a6d",
                    "M_TEXT_TOOLS",
                ),
                expected_file(
                    "validators/no_bullets.py",
                    "94a10cbfdc1bf4260ba3ef1ce611b45bd8243d3b362b116ee7dc819b34565060",
                    "V_NO_BULLETS",
                ),
            ],
            "multi_file",
        ),
        "hard_link": expected_package(
            "lattice:package:sha256:403906116513b9c432a9f9558d7af747286b5539ee95563fba019d38584a1dc7",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file("a.txt", DATA_DIGEST, "DATA"),
                expected_file("b.txt", DATA_DIGEST, "DATA"),
                *module,
            ],
            "hard_link",
        ),
        "beta_minimal_bytes": expected_package(
            "lattice:package:sha256:b6705fd7774024451a41bccd82dae7f7ead5c998341a10afbff2c77a6dac20e1",
            "beta",
            "1.0.0",
            core,
            "module.yaml",
            module,
        ),
        "alpha_1_0_1": expected_package(
            "lattice:package:sha256:9f305028f064ace9b8d839ad48f8dcd62281e3bc5ba081177d85e143232a098e",
            "alpha",
            "1.0.1",
            core,
            "module.yaml",
            module,
        ),
        "both_profiles": expected_package(
            "lattice:package:sha256:934a9bc2921a91d1d1145956389a4b3a0dcc887756e33f909d00cf3e00287576",
            "alpha",
            "1.0.0",
            ["lattice-builder-0.1", "lattice-core-0.1"],
            "module.yaml",
            module,
        ),
        "two_modules_module": expected_package(
            "lattice:package:sha256:6e7bc9698250aaa255189f5a8d8e74b91b52547deb7e66a9e602393bd5d8c476",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file("entry.yaml", MODULE_DIGEST, "M_ALPHA_100"),
                *module,
            ],
        ),
        "two_modules_entry": expected_package(
            "lattice:package:sha256:9031644cb03fe56a568c6635f88cda9130ca89e97f91723a710215e27da8f37b",
            "alpha",
            "1.0.0",
            core,
            "entry.yaml",
            [
                expected_file("entry.yaml", MODULE_DIGEST, "M_ALPHA_100"),
                *module,
            ],
        ),
        "data_root": expected_package(
            "lattice:package:sha256:51b4317223471152bf1e81041a58edb10507a6be370317b49b3cf5c7f93aa80a",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file("data.txt", DATA_DIGEST, "DATA"),
                *module,
            ],
        ),
        "data_docs": expected_package(
            "lattice:package:sha256:676636785015758fc969e33b6f153f7787e507742547509d84b9f6c9e83bc495",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file("docs/data.txt", DATA_DIGEST, "DATA"),
                *module,
            ],
        ),
        "data_changed": expected_package(
            "lattice:package:sha256:b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "data.txt", DATA_CHANGED_DIGEST, "DATA_CHANGED"
                ),
                *module,
            ],
        ),
        "empty_added": expected_package(
            "lattice:package:sha256:5acd1d6ab712dd052ad942bff1f7f840e7215d44fc479fba29492d0b75097778",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file("empty.txt", EMPTY_DIGEST, "EMPTY"),
                *module,
            ],
        ),
        "module_changed": expected_package(
            "lattice:package:sha256:c100d984afe465b06fd525f42a519651e094ff63a15a29f315a4ca3ff1047ef6",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "module.yaml",
                    "9b9f2b1e36beaad57c6436ad62b9bef6e01db6203d5567ac3afd0b1a0785acff",
                    "M_ALPHA_CHANGED",
                )
            ],
        ),
        "module_invalid_yaml": expected_package(
            "lattice:package:sha256:67615ce7c1071eb92ade638f888c1bd0fa866716849e72813635eb7c1b9c3d4b",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "module.yaml",
                    "7b8412cfb68dc835e7ccbdba401b79052a99f8f9e6dd3c955e47358506232945",
                    "M_INVALID_YAML",
                )
            ],
        ),
        "module_unresolved_import": expected_package(
            "lattice:package:sha256:b7a30c594bc90b58cc0127d350ae942d657415c1a234fdfc418bd0954f13b16e",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "module.yaml",
                    "43332c30f07a88388a60f93b9f76b21ed16f8d40ed130af788474d9017184916",
                    "M_UNRESOLVED_IMPORT",
                )
            ],
        ),
        "module_unsatisfied_version": expected_package(
            "lattice:package:sha256:037b2e0b64dccd3f890923d393b73c0dc56807d0149468791412bd98d20accfb",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "module.yaml",
                    "25628abdc47ca14733a318bf3007e15689efa276e8a60fc55a459080fde165e2",
                    "M_UNSATISFIED_VERSION",
                )
            ],
        ),
        "module_later_invalid": expected_package(
            "lattice:package:sha256:ede26ac500571dae4a6d00717d04ced75c2fdd070de95e620dda8731256e5f9f",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "module.yaml",
                    "87d252d0ef0f72f94eecbd7bb30ab17a8d24940e4bd1ca227f77ac1871c502e4",
                    "M_LATER_INVALID_BODY",
                )
            ],
        ),
        "module_opaque": expected_package(
            "lattice:package:sha256:981b422eb124556f4c00f102c000708c8f0ca596682f31a40bcf5ff49d3c970a",
            "alpha",
            "1.0.0",
            core,
            "module.yaml",
            [
                expected_file(
                    "module.yaml",
                    "7d92f51ef5701e0e78e1bb5ded05de427c6818dd6cbc9822fd95a949a0e8e10d",
                    "M_OPAQUE",
                )
            ],
            "opaque",
        ),
    }


def build_cases(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    fixtures = {fixture["id"]: fixture for fixture in manifest["fixtures"]}
    cases: dict[str, dict[str, Any]] = {}
    module_bytes = authoritative_byte_constant(manifest, "M_ALPHA_100")
    crlf_module_bytes = module_bytes.replace(b"\n", b"\r\n")
    bom_module_bytes = decode_hex("efbbbf", "FILE-BOM prefix") + module_bytes

    def bind(
        fixture_id: str,
        program: dict[str, Any],
        outcome: dict[str, Any],
    ) -> None:
        if fixture_id in cases:
            raise AssertionError(f"duplicate executable case {fixture_id}")
        fixture = fixtures.get(fixture_id)
        if fixture is None:
            raise AssertionError(f"unknown authoritative fixture {fixture_id}")
        cases[fixture_id] = {
            "id": fixture_id,
            "fixture_class": fixture["fixture_class"],
            "input_sha256": sha256_text(fixture["exact_input"]),
            "expected_sha256": sha256_text(fixture["expected"]),
            "program": program,
            "outcome": outcome,
        }

    def scan_case(
        fixture_id: str,
        runs: list[dict[str, Any]],
        expected_runs: list[list[str]] | None = None,
        relation: str = "none",
    ) -> None:
        diagnostic = fixtures[fixture_id]["expected_diagnostic"]
        if diagnostic is None:
            if expected_runs is None or len(expected_runs) != len(runs):
                raise AssertionError(
                    f"incomplete successful outcome for {fixture_id}"
                )
            outcome = {
                "kind": "success",
                "run_packages": expected_runs,
                "relation": relation,
            }
        else:
            if expected_runs is not None or len(runs) != 1:
                raise AssertionError(
                    f"invalid diagnostic program for {fixture_id}"
                )
            outcome = {
                "kind": "diagnostic",
                "code": diagnostic["code"],
                "path": diagnostic["path"],
            }
        bind(fixture_id, {"kind": "scan", "runs": runs}, outcome)

    def acquisition_case(
        fixture_id: str,
        acquisition: dict[str, Any],
        expected_error: str,
    ) -> None:
        bind(
            fixture_id,
            {"kind": "acquisition", "acquisition": acquisition},
            {
                "kind": "acquisition_failure",
                "error": expected_error,
            },
        )

    scan_case(
        "VAL-ROOT-ABSENT",
        [run(base="T-ABSENT")],
        [[]],
    )
    scan_case(
        "VAL-ROOT-EMPTY",
        [run(base="T-EMPTY")],
        [[]],
    )
    scan_case("VAL-MINIMAL", [run()], [["minimal"]])
    scan_case(
        "VAL-MULTIPLE-PACKAGES",
        [run(base="T-MULTIPLE-PACKAGES")],
        [["minimal", "beta_2_0_0"]],
    )
    scan_case(
        "VAL-MULTIPLE-VERSIONS",
        [run(base="T-MULTIPLE-VERSIONS")],
        [["minimal", "alpha_1_1_0"]],
    )
    scan_case(
        "VAL-NUMERIC-VERSION-ORDER",
        [run(base="T-VERSION-ORDER")],
        [["alpha_2_0_0", "alpha_10_0_0"]],
    )
    scan_case(
        "VAL-MULTIPLE-FILES",
        [run(base="T-MULTI-FILE")],
        [["multi_file"]],
    )
    scan_case(
        "VAL-EMPTY-FILE",
        [run(base="T-MULTI-FILE")],
        [["multi_file"]],
        "empty_file_exact",
    )
    enumeration_operations = [
        enumerate_children("packages", ["beta", "alpha"]),
        enumerate_children("packages/alpha", ["1.0.0"]),
        enumerate_children(
            "packages/alpha/1.0.0", ["module.yaml", "package.yaml"]
        ),
        enumerate_children("packages/beta", ["2.0.0"]),
        enumerate_children(
            "packages/beta/2.0.0", ["module.yaml", "package.yaml"]
        ),
    ]
    scan_case(
        "VAL-DISCOVERY-ORDER",
        [
            run(
                base="T-MULTIPLE-PACKAGES",
                operations=copy.deepcopy(enumeration_operations),
            )
        ],
        [["minimal", "beta_2_0_0"]],
        "physical_enumeration_irrelevant",
    )
    scan_case(
        "VAL-HARDLINK",
        [run(base="T-HARDLINK")],
        [["hard_link"]],
        "hardlink_paths_distinct",
    )
    scan_case(
        "VAL-UNLISTED-REGULAR",
        [run(operations=[add("packages/alpha/1.0.0/ignored.bin", regular(const("EMPTY")))])],
        [["minimal"]],
        "unlisted_not_retained",
    )
    scan_case(
        "VAL-UNLISTED-SPECIAL",
        [run(operations=[add("packages/alpha/1.0.0/ignored.sock", special("socket"))])],
        [["minimal"]],
        "unlisted_not_retained",
    )
    scan_case(
        "VAL-UNICODE-UNLISTED",
        [
            run(
                operations=[
                    add(
                        "packages/alpha/1.0.0/café.txt",
                        regular(const("EMPTY")),
                    )
                ]
            )
        ],
        [["minimal"]],
        "unlisted_not_retained",
    )
    scan_case(
        "VAL-PERCENT-UNLISTED",
        [
            run(
                operations=[
                    add(
                        "packages/alpha/1.0.0/100%.txt",
                        regular(const("EMPTY")),
                    )
                ]
            )
        ],
        [["minimal"]],
        "unlisted_not_retained",
    )

    acquisition_case(
        "SNAP-NONUTF8-UNIX-NAME",
        {
            "mode": "node",
            "node": {
                "kind": "directory",
                "children": [
                    {
                        "name": {"kind": "unix_bytes", "hex": "ff"},
                        "node": directory(),
                    }
                ],
            },
            "evidence": "included native filename bytes ff",
        },
        "UnrepresentableNativeName",
    )
    acquisition_case(
        "SNAP-MALFORMED-UTF16-NAME",
        {
            "mode": "node",
            "node": {
                "kind": "directory",
                "children": [
                    {
                        "name": {
                            "kind": "windows_utf16",
                            "units": [0xD800],
                        },
                        "node": directory(),
                    }
                ],
            },
            "evidence": "included unpaired high surrogate D800",
        },
        "MalformedUtf16Name",
    )
    acquisition_case(
        "SNAP-NFC-COLLISION",
        {
            "mode": "reported_error",
            "error": "NfcNameCollision",
            "evidence": "U+00E9 and U+0065 U+0301",
        },
        "NfcNameCollision",
    )
    acquisition_case(
        "SNAP-HOST-CASE-ALIAS",
        {
            "mode": "reported_error",
            "error": "NamespaceAlias",
            "evidence": "exact names a and A",
        },
        "NamespaceAlias",
    )
    acquisition_case(
        "SNAP-TRAILING-DOT-ALIAS",
        {
            "mode": "reported_error",
            "error": "NamespaceAlias",
            "evidence": "exact names name and name.",
        },
        "NamespaceAlias",
    )
    acquisition_case(
        "SNAP-CONCURRENT-MUTATION",
        {
            "mode": "reported_error",
            "error": "ConcurrentMutation",
            "evidence": "host cannot produce one immutable point-in-time view",
        },
        "ConcurrentMutation",
    )
    acquisition_case(
        "SNAP-ABA-MUTATION",
        {
            "mode": "reported_error",
            "error": "ConcurrentMutation",
            "evidence": "exact A to B to A",
        },
        "ConcurrentMutation",
    )
    acquisition_case(
        "SNAP-RESOURCE-EXHAUSTION",
        {
            "mode": "reported_error",
            "error": "ResourceExhaustion",
            "evidence": "storage fails during exact packages acquisition",
        },
        "ResourceExhaustion",
    )
    scan_case(
        "SNAP-UNRELATED-ROOT-NAME",
        [run()],
        [["minimal"]],
        "unrelated_root_excluded",
    )

    name_cases = {
        "NAME-UNICODE-STRUCTURAL": [
            add("packages/café", directory())
        ],
        "NAME-PERCENT-STRUCTURAL": [
            add("packages/100%", directory())
        ],
        "NAME-SPACE-STRUCTURAL": [add("packages/a b", directory())],
        "NAME-UTF8-ORDER": [
            add("packages/z!", directory()),
            add("packages/é", directory()),
        ],
        "NAME-PERCENT-ORDER": [
            add("packages/%", directory()),
            add("packages/a", directory()),
        ],
        "NAME-UNICODE-UNLISTED-SYMLINK": [
            add("packages/alpha/1.0.0/café", link("target"))
        ],
    }
    for fixture_id, operations in name_cases.items():
        scan_case(fixture_id, [run(operations=operations)])

    presentation_constants = {
        "EQ-KEY-ORDER": ("T-MINIMAL", DP, "D_MIN_REVERSED"),
        "EQ-COMMENTS": ("T-MINIMAL", DP, "D_MIN_COMMENTED"),
        "EQ-INDENTATION": ("T-MINIMAL", DP, "D_MIN_INDENT4"),
        "EQ-QUOTING": ("T-MINIMAL", DP, "D_MIN_QUOTED"),
        "EQ-LINE-ENDINGS-LF": ("T-MINIMAL", DP, "D_MIN"),
        "EQ-LINE-ENDINGS-CRLF": ("T-MINIMAL", DP, "D_MIN_CRLF"),
        "EQ-LINE-ENDINGS-CR": ("T-MINIMAL", DP, "D_MIN_CR"),
        "EQ-FILES-ORDER": (
            "T-MULTI-FILE",
            "packages/text_tools/1.3.1/package.yaml",
            "D_MULTI_FILES_ALT",
        ),
        "EQ-PROFILES-ORDER": (
            "T-MULTI-FILE",
            "packages/text_tools/1.3.1/package.yaml",
            "D_MULTI_PROFILES_ALT",
        ),
    }
    for fixture_id, (base, path, constant_name) in presentation_constants.items():
        expected = "multi_file" if base == "T-MULTI-FILE" else "minimal"
        scan_case(
            fixture_id,
            [
                run(
                    base=base,
                    operations=[set_descriptor(const(constant_name), path)],
                )
            ],
            [[expected]],
            "canonical_presentation_equivalent",
        )
    scan_case(
        "EQ-PHYSICAL-ENUMERATION",
        [
            run(
                base="T-MULTIPLE-PACKAGES",
                operations=copy.deepcopy(enumeration_operations),
            )
        ],
        [["minimal", "beta_2_0_0"]],
        "physical_enumeration_irrelevant",
    )

    scan_case(
        "ID-PACKAGE",
        [
            run(
                operations=[
                    rename("packages/alpha", "beta"),
                    set_descriptor(
                        bd(
                            "beta",
                            "1.0.0",
                            ["lattice-core-0.1"],
                            "module.yaml",
                            [("module.yaml", MODULE_DIGEST)],
                        ),
                        "packages/beta/1.0.0/package.yaml",
                    ),
                ]
            )
        ],
        [["beta_minimal_bytes"]],
    )
    scan_case(
        "ID-VERSION",
        [
            run(
                operations=[
                    rename("packages/alpha/1.0.0", "1.0.1"),
                    set_descriptor(
                        bd(
                            "alpha",
                            "1.0.1",
                            ["lattice-core-0.1"],
                            "module.yaml",
                            [("module.yaml", MODULE_DIGEST)],
                        ),
                        "packages/alpha/1.0.1/package.yaml",
                    ),
                ]
            )
        ],
        [["alpha_1_0_1"]],
    )
    scan_case(
        "ID-LATTICE",
        [
            run(
                operations=[
                    set_descriptor(
                        replace(
                            const("D_MIN"),
                            'lattice: "0.3"\n',
                            'lattice: "0.4"\n',
                        )
                    )
                ]
            )
        ],
    )
    scan_case(
        "ID-PROFILES-MEMBERSHIP",
        [
            run(
                operations=[
                    set_descriptor(
                        bd(
                            "alpha",
                            "1.0.0",
                            [
                                "lattice-core-0.1",
                                "lattice-builder-0.1",
                            ],
                            "module.yaml",
                            [("module.yaml", MODULE_DIGEST)],
                        )
                    )
                ]
            )
        ],
        [["both_profiles"]],
    )
    two_module_files = [
        ("entry.yaml", MODULE_DIGEST),
        ("module.yaml", MODULE_DIGEST),
    ]
    two_module_operations = [
        add(
            "packages/alpha/1.0.0/entry.yaml",
            regular(const("M_ALPHA_100")),
        ),
    ]
    scan_case(
        "ID-MODULE-FILE",
        [
            run(
                operations=copy.deepcopy(two_module_operations)
                + [
                    set_descriptor(
                        bd(
                            "alpha",
                            "1.0.0",
                            ["lattice-core-0.1"],
                            "module.yaml",
                            two_module_files,
                        )
                    )
                ]
            ),
            run(
                operations=copy.deepcopy(two_module_operations)
                + [
                    set_descriptor(
                        bd(
                            "alpha",
                            "1.0.0",
                            ["lattice-core-0.1"],
                            "entry.yaml",
                            two_module_files,
                        )
                    )
                ]
            ),
        ],
        [["two_modules_module"], ["two_modules_entry"]],
        "distinct_identities",
    )
    scan_case(
        "ID-DECLARED-PATH",
        [
            run(
                operations=[
                    add(
                        "packages/alpha/1.0.0/data.txt",
                        regular(const("DATA")),
                    ),
                    set_descriptor(
                        bd(
                            "alpha",
                            "1.0.0",
                            ["lattice-core-0.1"],
                            "module.yaml",
                            [
                                ("module.yaml", MODULE_DIGEST),
                                ("data.txt", DATA_DIGEST),
                            ],
                        )
                    ),
                ]
            ),
            run(
                operations=[
                    add("packages/alpha/1.0.0/docs", directory()),
                    add(
                        "packages/alpha/1.0.0/docs/data.txt",
                        regular(const("DATA")),
                    ),
                    set_descriptor(
                        bd(
                            "alpha",
                            "1.0.0",
                            ["lattice-core-0.1"],
                            "module.yaml",
                            [
                                ("module.yaml", MODULE_DIGEST),
                                ("docs/data.txt", DATA_DIGEST),
                            ],
                        )
                    ),
                ]
            ),
        ],
        [["data_root"], ["data_docs"]],
        "distinct_identities",
    )
    scan_case(
        "ID-DECLARED-HASH-REJECTED",
        [run(operations=[set_descriptor(const("D_DIGEST_F64"))])],
    )
    scan_case(
        "ID-DECLARED-FILE-SET",
        [
            run(
                operations=[
                    add(
                        "packages/alpha/1.0.0/empty.txt",
                        regular(const("EMPTY")),
                    ),
                    set_descriptor(
                        bd(
                            "alpha",
                            "1.0.0",
                            ["lattice-core-0.1"],
                            "module.yaml",
                            [
                                ("module.yaml", MODULE_DIGEST),
                                ("empty.txt", EMPTY_DIGEST),
                            ],
                        )
                    ),
                ]
            )
        ],
        [["empty_added"]],
    )
    changed_descriptor = bd(
        "alpha",
        "1.0.0",
        ["lattice-core-0.1"],
        "module.yaml",
        [
            (
                "module.yaml",
                "9b9f2b1e36beaad57c6436ad62b9bef6e01db6203d5567ac3afd0b1a0785acff",
            )
        ],
    )
    scan_case(
        "ID-RAW-BYTES-AND-DIGEST",
        [
            run(
                operations=[
                    replace_node(MP, regular(const("M_ALPHA_CHANGED"))),
                    set_descriptor(copy.deepcopy(changed_descriptor)),
                ]
            )
        ],
        [["module_changed"]],
    )

    parser_expressions = {
        "PARSE-INVALID-UTF8": exact_hex("ff"),
        "PARSE-BOM": concat(exact_hex("efbbbf"), const("D_MIN")),
        "PARSE-RAW-CONTROL": concat(exact_hex("00"), const("D_MIN")),
        "PARSE-DIRECTIVE-YAML": concat(
            utf8("%YAML 1.1\n---\n"), const("D_MIN")
        ),
        "PARSE-DIRECTIVE-TAG": concat(
            utf8("%TAG !e! tag:example.com,2026:\n---\n"),
            const("D_MIN"),
        ),
        "PARSE-SYNTAX": exact_hex("756e6974733a205b0a"),
        "PARSE-MULTIPLE-DOCUMENTS": concat(
            const("D_MIN"), utf8("---\n"), const("D_MIN")
        ),
        "PARSE-ANCHOR": replace(
            const("D_MIN"), "package: alpha\n", "package: &p alpha\n"
        ),
        "PARSE-ALIAS": replace(
            const("D_MIN"), "package: alpha\n", "package: *p\n"
        ),
        "PARSE-MERGE": concat(
            utf8("<<: {package: alpha}\n"), const("D_MIN")
        ),
        "PARSE-TAG": replace(
            const("D_MIN"), "package: alpha\n", "package: !custom alpha\n"
        ),
        "PARSE-TAG-MISMATCH": replace(
            const("D_MIN"), "package: alpha\n", "package: !!int alpha\n"
        ),
        "PARSE-FOLDED": replace(
            const("D_MIN"), "package: alpha\n", "package: >\n  alpha\n"
        ),
        "PARSE-BINARY": replace(
            const("D_MIN"),
            "package: alpha\n",
            "package: !!binary YQ==\n",
        ),
        "PARSE-FLOAT": replace(
            const("D_MIN"), "package: alpha\n", "package: 1.5\n"
        ),
        "PARSE-I64-RANGE": replace(
            const("D_MIN"),
            "package: alpha\n",
            "package: 9223372036854775808\n",
        ),
        "PARSE-DATE-LIKE-STRING": replace(
            const("D_MIN"),
            "package: alpha\n",
            "package: 2026-07-23\n",
        ),
        "PARSE-NONSTRING-KEY": replace(
            const("D_MIN"), "package: alpha\n", "1: alpha\n"
        ),
        "PARSE-DUPLICATE-KEY": insert_after(
            const("D_MIN"), "package: alpha\n", "package: alpha\n"
        ),
        "PARSE-NFC-COLLISION": concat(
            exact_hex("c3a93a20747275650a65cc813a2066616c73650a"),
            const("D_MIN"),
        ),
        "PARSE-MULTI-DEFECT": utf8(
            "%YAML 1.1\n---\npackage: 1.5\n"
        ),
    }
    for fixture_id, expression in parser_expressions.items():
        scan_case(
            fixture_id,
            [run(operations=[set_descriptor(expression)])],
        )

    descriptor_expressions = {
        "DESC-NONOBJECT": exact_hex("5b5d0a"),
        "DESC-UNKNOWN-FIELD": insert_after(
            const("D_MIN"), 'lattice: "0.3"\n', "extra: true\n"
        ),
        "DESC-MISSING-FIELD": delete(
            const("D_MIN"), 'lattice: "0.3"\n'
        ),
        "DESC-WRONG-TYPE": replace(
            const("D_MIN"), "package: alpha\n", "package: [alpha]\n"
        ),
        "DESC-INVALID-PACKAGE": replace(
            const("D_MIN"), "package: alpha\n", "package: Alpha\n"
        ),
        "DESC-INVALID-VERSION": replace(
            const("D_MIN"),
            'version: "1.0.0"\n',
            'version: "01.0.0"\n',
        ),
        "DESC-INVALID-LATTICE": replace(
            const("D_MIN"),
            'lattice: "0.3"\n',
            'lattice: "0.4"\n',
        ),
        "DESC-INVALID-PROFILE": replace(
            const("D_MIN"),
            "  - lattice-core-0.1\n",
            "  - lattice-extended-0.2\n",
        ),
        "DESC-PROFILE-WRONG-TYPE": replace(
            const("D_MIN"), "  - lattice-core-0.1\n", "  - true\n"
        ),
        "DESC-DUPLICATE-PROFILE": insert_after(
            const("D_MIN"),
            "  - lattice-core-0.1\n",
            "  - lattice-core-0.1\n",
        ),
        "DESC-EMPTY-PROFILES": replace(
            const("D_MIN"),
            "profiles:\n  - lattice-core-0.1\n",
            "profiles: []\n",
        ),
        "DESC-FILES-WRONG-TYPE": replace(
            const("D_MIN"),
            "files:\n"
            "  - path: module.yaml\n"
            f"    sha256: {MODULE_DIGEST}\n",
            "files: {}\n",
        ),
        "DESC-FILE-NONOBJECT": replace(
            const("D_MIN"),
            "  - path: module.yaml\n"
            f"    sha256: {MODULE_DIGEST}\n",
            "  - module.yaml\n",
        ),
        "DESC-FILE-UNKNOWN": insert_after(
            const("D_MIN"),
            f"    sha256: {MODULE_DIGEST}\n",
            "    size: 105\n",
        ),
        "DESC-FILE-MISSING-SHA": delete(
            const("D_MIN"), f"    sha256: {MODULE_DIGEST}\n"
        ),
        "DESC-DUPLICATE-FILE": insert_after(
            const("D_MIN"),
            f"    sha256: {MODULE_DIGEST}\n",
            "  - path: module.yaml\n"
            f"    sha256: {MODULE_DIGEST}\n",
        ),
        "DESC-EMPTY-FILES": replace(
            const("D_MIN"),
            "files:\n"
            "  - path: module.yaml\n"
            f"    sha256: {MODULE_DIGEST}\n",
            "files: []\n",
        ),
        "DESC-MODULE-UNLISTED": replace(
            const("D_MIN"),
            "module_file: module.yaml\n",
            "module_file: entry.yaml\n",
        ),
        "DESC-PACKAGE-YAML-LISTED": insert_after(
            const("D_MIN"),
            f"    sha256: {MODULE_DIGEST}\n",
            "  - path: package.yaml\n"
            f"    sha256: {EMPTY_DIGEST}\n",
        ),
    }
    for fixture_id, expression in descriptor_expressions.items():
        scan_case(
            fixture_id,
            [run(operations=[set_descriptor(expression)])],
        )

    pointer_fragments = {
        "PTR-SOLIDUS": utf8('"a/b": true\n'),
        "PTR-TILDE": utf8('"a~b": true\n'),
        "PTR-PERCENT": utf8('"a%b": true\n'),
        "PTR-NUMBER-SIGN": utf8('"a#b": true\n'),
        "PTR-C0": exact_hex("22615c78303162223a20747275650a"),
        "PTR-NONASCII": exact_hex(
            "22636166c3a9223a20747275650a"
        ),
    }
    for fixture_id, fragment in pointer_fragments.items():
        scan_case(
            fixture_id,
            [
                run(
                    operations=[
                        set_descriptor(
                            {
                                "kind": "insert_bytes_after",
                                "source": const("D_MIN"),
                                "anchor": utf8('lattice: "0.3"\n'),
                                "bytes": fragment,
                            }
                        )
                    ]
                )
            ],
        )

    layout_cases = {
        "LAYOUT-PACKAGES-FILE": [
            replace_node("packages", regular(const("EMPTY")))
        ],
        "LAYOUT-PACKAGES-SYMLINK": [
            replace_node("packages", link("target"))
        ],
        "LAYOUT-PACKAGES-UNREADABLE": [
            replace_node("packages", directory_unreadable())
        ],
        "LAYOUT-PACKAGE-DIRECTORY-UNREADABLE": [
            replace_node("packages/alpha", directory_unreadable())
        ],
        "LAYOUT-VERSION-DIRECTORY-UNREADABLE": [
            replace_node("packages/alpha/1.0.0", directory_unreadable())
        ],
        "LAYOUT-PACKAGE-NAME-MISMATCH": [
            set_descriptor(
                replace(
                    const("D_MIN"),
                    "package: alpha\n",
                    "package: beta\n",
                )
            )
        ],
        "LAYOUT-VERSION-MISMATCH": [
            set_descriptor(
                replace(
                    const("D_MIN"),
                    'version: "1.0.0"\n',
                    'version: "1.0.1"\n',
                )
            )
        ],
        "LAYOUT-STRAY-PACKAGE-FILE": [
            add("packages/notes.txt", regular(const("EMPTY")))
        ],
        "LAYOUT-STRAY-VERSION-FILE": [
            add("packages/alpha/readme.txt", regular(const("EMPTY")))
        ],
        "LAYOUT-MISSING-DESCRIPTOR": [remove(DP)],
        "LAYOUT-WRONG-DEPTH-DESCRIPTOR": [
            add(
                "packages/alpha/package.yaml",
                regular(const("D_MIN")),
            )
        ],
        "LAYOUT-PACKAGE-SYMLINK": [
            replace_node("packages/alpha", link("target"))
        ],
        "LAYOUT-VERSION-SYMLINK": [
            replace_node("packages/alpha/1.0.0", link("target"))
        ],
    }
    for fixture_id, operations in layout_cases.items():
        scan_case(fixture_id, [run(operations=operations)])

    scan_case(
        "PREC-INVALID-NAME-SYMLINK",
        [run(operations=[add("packages/Bad", link("target"))])],
    )
    scan_case(
        "PREC-INVALID-NAME-REGULAR",
        [
            run(
                operations=[
                    add("packages/Bad", regular(const("EMPTY")))
                ]
            )
        ],
    )
    scan_case(
        "PREC-DESCRIPTOR-SYMLINK",
        [run(operations=[replace_node(DP, link("target"))])],
    )
    scan_case(
        "PREC-DESCRIPTOR-DIRECTORY",
        [run(operations=[replace_node(DP, directory())])],
    )
    scan_case(
        "PREC-DESCRIPTOR-UNREADABLE",
        [run(operations=[replace_node(DP, regular_unreadable())])],
    )
    scan_case(
        "PREC-NESTED-TRAVERSAL",
        [
            run(
                operations=[
                    remove(DP),
                    add("packages/bad!", directory()),
                ]
            )
        ],
    )
    scan_case(
        "PREC-STRUCTURAL-VERSION-UTF8",
        [
            run(
                base="T-VERSION-ORDER",
                operations=[
                    remove("packages/alpha/10.0.0/package.yaml"),
                    remove("packages/alpha/2.0.0/package.yaml"),
                ],
            )
        ],
    )
    scan_case(
        "PREC-GLOBAL-DESCRIPTOR-PASS",
        [
            run(
                base="T-MULTIPLE-PACKAGES",
                operations=[
                    replace_node(MP, regular(const("DATA"))),
                    replace_node(
                        "packages/beta/2.0.0/package.yaml",
                        regular(const("M_INVALID_YAML")),
                    ),
                ],
            )
        ],
    )
    scan_case(
        "PREC-GLOBAL-PARSER-BEFORE-SHALLOW",
        [
            run(
                base="T-MULTIPLE-PACKAGES",
                operations=[
                    set_descriptor(
                        replace(
                            const("D_MIN"),
                            "package: alpha\n",
                            "package: [alpha]\n",
                        )
                    ),
                    set_descriptor(
                        const("M_INVALID_YAML"),
                        "packages/beta/2.0.0/package.yaml",
                    ),
                ],
            )
        ],
    )
    scan_case(
        "PREC-GLOBAL-SHALLOW-BEFORE-COLLECTION",
        [
            run(
                base="T-MULTIPLE-PACKAGES",
                operations=[
                    set_descriptor(
                        replace(
                            const("D_MIN"),
                            "  - lattice-core-0.1\n",
                            "  - lattice-extended-0.2\n",
                        )
                    ),
                    set_descriptor(
                        replace(
                            const("D_BETA_200"),
                            "package: beta\n",
                            "package: [beta]\n",
                        ),
                        "packages/beta/2.0.0/package.yaml",
                    ),
                ],
            )
        ],
    )
    scan_case(
        "PREC-GLOBAL-COLLECTION-BEFORE-METADATA",
        [
            run(
                base="T-MULTIPLE-PACKAGES",
                operations=[
                    add(
                        "packages/alpha/1.0.0/ignored-link",
                        link("target"),
                    ),
                    set_descriptor(
                        replace(
                            const("D_BETA_200"),
                            "  - lattice-core-0.1\n",
                            "  - lattice-extended-0.2\n",
                        ),
                        "packages/beta/2.0.0/package.yaml",
                    ),
                ],
            )
        ],
    )
    scan_case(
        "PREC-GLOBAL-METADATA-BEFORE-DECLARED",
        [
            run(
                base="T-MULTIPLE-PACKAGES",
                operations=[
                    set_descriptor(const("D_DIGEST_F64")),
                    add(
                        "packages/beta/2.0.0/ignored-link",
                        link("target"),
                    ),
                ],
            )
        ],
    )
    shallow_before_agreement = replace(
        replace(
            const("D_MIN"), "package: alpha\n", "package: beta\n"
        ),
        "profiles:\n  - lattice-core-0.1\n",
        "profiles: {}\n",
    )
    scan_case(
        "PREC-SHALLOW-BEFORE-AGREEMENT",
        [
            run(
                operations=[
                    set_descriptor(shallow_before_agreement)
                ]
            )
        ],
    )
    agreement_before_profile = replace(
        replace(
            const("D_MIN"), "package: alpha\n", "package: beta\n"
        ),
        "  - lattice-core-0.1\n",
        "  - lattice-extended-0.2\n",
    )
    scan_case(
        "PREC-AGREEMENT-BEFORE-PROFILE-CONTENT",
        [
            run(
                operations=[
                    set_descriptor(agreement_before_profile)
                ]
            )
        ],
    )

    path_scalar_sources = {
        "PATH-EMPTY": '""',
        "PATH-LEADING-SLASH": '"/module.yaml"',
        "PATH-TRAILING-SLASH": '"module.yaml/"',
        "PATH-REPEATED-SLASH": '"sub//module.yaml"',
        "PATH-DOT": '"./module.yaml"',
        "PATH-PARENT": '"../module.yaml"',
        "PATH-BACKSLASH": bytes.fromhex(
            "227375625c5c6d6f64756c652e79616d6c22"
        ).decode("utf-8"),
        "PATH-DRIVE": '"c:/module.yaml"',
        "PATH-UNC": '"//server/share/module.yaml"',
        "PATH-COLON": '"a:b"',
        "PATH-NUL": bytes.fromhex("225c3022").decode("utf-8"),
        "PATH-CONTROL": bytes.fromhex("225c78303122").decode(
            "utf-8"
        ),
        "PATH-UNICODE": bytes.fromhex(
            "22636166c3a92e74787422"
        ).decode("utf-8"),
        "PATH-NON-NFC": bytes.fromhex(
            "2263616665cc812e74787422"
        ).decode("utf-8"),
        "PATH-UPPERCASE": '"Module.yaml"',
        "PATH-RESERVED": '"con.txt"',
        "PATH-TRAILING-DOT": '"module."',
        "PATH-TRAILING-SPACE": bytes.fromhex(
            "226d6f64756c652e79616d6c2022"
        ).decode("utf-8"),
    }
    for fixture_id, scalar_source in path_scalar_sources.items():
        scan_case(
            fixture_id,
            [
                run(
                    operations=[
                        set_descriptor(bdp(scalar_source))
                    ]
                )
            ],
        )
    scan_case(
        "PATH-DUPLICATE",
        [
            run(
                operations=[
                    set_descriptor(
                        bdf(
                            "module.yaml",
                            [
                                ("module.yaml", MODULE_DIGEST),
                                ("module.yaml", MODULE_DIGEST),
                            ],
                        )
                    )
                ]
            )
        ],
    )
    scan_case(
        "PATH-NFC-DUPLICATE",
        [
            run(
                operations=[
                    set_descriptor(
                        bdf(
                            "module.yaml",
                            [
                                ("module.yaml", MODULE_DIGEST),
                                (
                                    bytes.fromhex("22c3a922").decode(
                                        "utf-8"
                                    ),
                                    EMPTY_DIGEST,
                                ),
                                (
                                    bytes.fromhex("2265cc8122").decode(
                                        "utf-8"
                                    ),
                                    EMPTY_DIGEST,
                                ),
                            ],
                        )
                    )
                ]
            )
        ],
    )
    scan_case(
        "PATH-PREFIX-COLLISION",
        [
            run(
                operations=[
                    set_descriptor(
                        bdf(
                            "module.yaml",
                            [
                                ("a", EMPTY_DIGEST),
                                ("a/b", EMPTY_DIGEST),
                                ("b", EMPTY_DIGEST),
                                ("b/c", EMPTY_DIGEST),
                                ("module.yaml", MODULE_DIGEST),
                            ],
                        )
                    )
                ]
            )
        ],
    )
    scan_case(
        "PATH-PREFIX-SELECTION",
        [
            run(
                operations=[
                    set_descriptor(
                        bdf(
                            "module.yaml",
                            [
                                ("b", EMPTY_DIGEST),
                                ("b/c", EMPTY_DIGEST),
                                ("a", EMPTY_DIGEST),
                                ("a/z", EMPTY_DIGEST),
                                ("a/y", EMPTY_DIGEST),
                                ("module.yaml", MODULE_DIGEST),
                            ],
                        )
                    )
                ]
            )
        ],
    )

    sub_descriptor = bd(
        "alpha",
        "1.0.0",
        ["lattice-core-0.1"],
        "sub/module.yaml",
        [("sub/module.yaml", MODULE_DIGEST)],
    )
    file_cases = {
        "FILE-MISSING": [remove(MP)],
        "FILE-DIRECTORY": [replace_node(MP, directory())],
        "FILE-DIRECTORY-UNREADABLE": [
            replace_node(MP, directory_unreadable())
        ],
        "FILE-FINAL-SYMLINK": [replace_node(MP, link("target"))],
        "FILE-INTERMEDIATE-MISSING": [
            set_descriptor(copy.deepcopy(sub_descriptor))
        ],
        "FILE-INTERMEDIATE-SYMLINK": [
            set_descriptor(copy.deepcopy(sub_descriptor)),
            add("packages/alpha/1.0.0/sub", link("target")),
        ],
        "FILE-INTERMEDIATE-REGULAR": [
            set_descriptor(copy.deepcopy(sub_descriptor)),
            add(
                "packages/alpha/1.0.0/sub",
                regular(const("EMPTY")),
            ),
        ],
        "FILE-INTERMEDIATE-SPECIAL": [
            set_descriptor(copy.deepcopy(sub_descriptor)),
            add("packages/alpha/1.0.0/sub", special("FIFO")),
        ],
        "FILE-INTERMEDIATE-UNREADABLE-DIRECTORY": [
            set_descriptor(copy.deepcopy(sub_descriptor)),
            add(
                "packages/alpha/1.0.0/sub",
                directory_unreadable(),
            ),
        ],
        "FILE-SPECIAL": [replace_node(MP, special("FIFO"))],
        "FILE-UNREADABLE": [replace_node(MP, regular_unreadable())],
        "FILE-DIGEST-SHORT": [
            set_descriptor(const("D_DIGEST_F63"))
        ],
        "FILE-DIGEST-UPPERCASE": [
            set_descriptor(
                replace(
                    const("D_MIN"),
                    MODULE_DIGEST,
                    "900DD3893A719EC7EA1CB5ACFF8EC799223D6B8D3F3C6DEA3EB09F2D06B67B55",
                )
            )
        ],
        "FILE-DIGEST-PREFIXED": [
            set_descriptor(
                replace(
                    const("D_MIN"),
                    MODULE_DIGEST,
                    f"sha256:{MODULE_DIGEST}",
                )
            )
        ],
        "FILE-HASH-MISMATCH": [
            set_descriptor(const("D_DIGEST_F64"))
        ],
        "FILE-LINE-ENDINGS": [
            replace_hex(MP, exact_hex(crlf_module_bytes.hex()))
        ],
        "FILE-BOM": [
            replace_hex(MP, exact_hex(bom_module_bytes.hex()))
        ],
        "FILE-UNLISTED-SYMLINK": [
            add(
                "packages/alpha/1.0.0/ignored-link",
                link("ignored-target"),
            )
        ],
        "FILE-UNLISTED-UNREADABLE-DIR": [
            add(
                "packages/alpha/1.0.0/ignored",
                directory_unreadable(),
            )
        ],
    }
    for fixture_id, operations in file_cases.items():
        scan_case(fixture_id, [run(operations=operations)])

    phase_records = {
        "PHASE-MALFORMED-MODULE-YAML": (
            "M_INVALID_YAML",
            "7b8412cfb68dc835e7ccbdba401b79052a99f8f9e6dd3c955e47358506232945",
            "module_invalid_yaml",
        ),
        "PHASE-UNRESOLVED-IMPORT": (
            "M_UNRESOLVED_IMPORT",
            "43332c30f07a88388a60f93b9f76b21ed16f8d40ed130af788474d9017184916",
            "module_unresolved_import",
        ),
        "PHASE-UNSATISFIED-VERSION": (
            "M_UNSATISFIED_VERSION",
            "25628abdc47ca14733a318bf3007e15689efa276e8a60fc55a459080fde165e2",
            "module_unsatisfied_version",
        ),
        "PHASE-LATER-INVALID-BODY": (
            "M_LATER_INVALID_BODY",
            "87d252d0ef0f72f94eecbd7bb30ab17a8d24940e4bd1ca227f77ac1871c502e4",
            "module_later_invalid",
        ),
    }
    for fixture_id, (
        constant_name,
        digest,
        record_name,
    ) in phase_records.items():
        scan_case(
            fixture_id,
            [
                run(
                    operations=[
                        replace_node(MP, regular(const(constant_name))),
                        set_descriptor(
                            bd(
                                "alpha",
                                "1.0.0",
                                ["lattice-core-0.1"],
                                "module.yaml",
                                [("module.yaml", digest)],
                            )
                        ),
                    ]
                )
            ],
            [[record_name]],
            "pc6_does_not_parse_module",
        )
    scan_case(
        "PHASE-NO-MODULE-PARSE",
        [
            run(
                operations=[
                    replace_node(MP, regular(const("M_OPAQUE"))),
                    set_descriptor(const("D_OPAQUE")),
                ]
            )
        ],
        [["module_opaque"]],
        "pc6_does_not_parse_module",
    )
    for fixture_id in [
        "PHASE-NO-LOCKFILE",
        "PHASE-NO-EXPANSION",
        "PHASE-NO-DECLARATION-ID",
        "PHASE-NO-MANIFEST",
        "PHASE-NO-BINDING",
        "PHASE-NO-AUTHORITY",
    ]:
        scan_case(
            fixture_id,
            [run()],
            [["minimal"]],
            "pc6_only_surface",
        )

    scan_case(
        "BIND-EXACT-SOURCE",
        [run(source="DS-A"), run(source="DS-B")],
        [["minimal"], ["minimal"]],
        "exact_source_binding",
    )
    scan_case(
        "BIND-SOURCE-SWAP",
        [run()],
        [["minimal"]],
        "source_swap_unavailable",
    )
    scan_case(
        "BIND-ID-CONTENT-SWAP",
        [run()],
        [["minimal"]],
        "identity_content_swap_unavailable",
    )
    scan_case(
        "BIND-REPEAT-SCAN",
        [run(), run()],
        [["minimal"], ["minimal"]],
        "repeat_equal",
    )
    scan_case(
        "BIND-LIVE-MUTATION-AFTER-SNAPSHOT",
        [
            run(
                timing="mutate_after_acquisition",
                live_operations=[
                    replace_node(MP, regular(const("DATA")))
                ],
            )
        ],
        [["minimal"]],
        "live_snapshot_stable",
    )
    scan_case(
        "BIND-NEW-SNAPSHOT-UNUPDATED-DIGEST",
        [
            run(
                operations=[
                    replace_node(
                        MP, regular(const("M_ALPHA_CHANGED"))
                    )
                ]
            )
        ],
    )
    scan_case(
        "BIND-NEW-SNAPSHOT-UPDATED-DIGEST",
        [
            run(
                operations=[
                    replace_node(
                        MP, regular(const("M_ALPHA_CHANGED"))
                    ),
                    set_descriptor(copy.deepcopy(changed_descriptor)),
                ]
            )
        ],
        [["module_changed"]],
    )
    scan_case(
        "BIND-LATER-CONSUMPTION",
        [
            run(
                timing="mutate_after_scan",
                live_operations=[
                    replace_node(MP, regular(const("DATA")))
                ],
            )
        ],
        [["minimal"]],
        "later_consumes_retained",
    )
    scan_case(
        "BIND-CANONICAL-BYTES-DERIVED",
        [run()],
        [["minimal"]],
        "canonical_bytes_derived",
    )
    scan_case(
        "BIND-NO-CANONICAL-CACHE",
        [run()],
        [["minimal"]],
        "canonical_cache_not_semantic",
    )
    scan_case(
        "BIND-NO-MUTABLE-BYTES",
        [run()],
        [["minimal"]],
        "verified_bytes_immutable",
    )

    missing = set(fixtures).difference(cases)
    extra = set(cases).difference(fixtures)
    if missing or extra:
        raise AssertionError(
            f"fixture dispatch mismatch missing={sorted(missing)} "
            f"extra={sorted(extra)}"
        )
    return [cases[fixture["id"]] for fixture in manifest["fixtures"]]


def make_plan(manifest: dict[str, Any]) -> dict[str, Any]:
    packages = expected_packages()
    return {
        "fixture_plan_version": "pc6-package-scan-executable-plan-1",
        "authority": copy.deepcopy(manifest["authority"]),
        "source_vocabulary": {
            "DS-A": {
                "yaml": DS_A,
                "byte_constant": "DS-A",
            },
            "DS-B": {
                "yaml": DS_B,
                "byte_constant": "DS-B",
            },
        },
        "base_snapshots": base_snapshots(),
        "operation_vocabulary": [
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
        "byte_expression_vocabulary": [
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
        "node_vocabulary": [
            "directory",
            "directory_unreadable",
            "regular",
            "regular_unreadable",
            "link",
            "special",
        ],
        "relation_vocabulary": [
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
        "expected_packages": packages,
        "golden_record_ids": list(packages),
        "cases": build_cases(manifest),
    }


def require_keys(
    value: dict[str, Any], required: set[str], context: str
) -> None:
    actual = set(value)
    if actual != required:
        raise AssertionError(
            f"{context} keys differ: "
            f"missing={sorted(required - actual)} "
            f"unknown={sorted(actual - required)}"
        )


def decode_hex(value: str, context: str) -> bytes:
    if len(value) % 2 or any(
        character not in "0123456789abcdef" for character in value
    ):
        raise AssertionError(f"{context} is not lowercase even-length hex")
    return bytes.fromhex(value)


def authoritative_byte_constant(
    manifest: dict[str, Any], name: str
) -> bytes:
    matches = [
        record
        for record in manifest["authoritative_byte_constants"]
        if record.get("name") == name
    ]
    if len(matches) != 1:
        raise AssertionError(
            f"expected exactly one authoritative byte constant {name}"
        )
    record = matches[0]
    context = f"authoritative byte constant {name}"
    require_keys(record, {"name", "hex", "length", "sha256"}, context)
    value = decode_hex(record["hex"], context)
    if len(value) != record["length"]:
        raise AssertionError(f"length mismatch for {name}")
    if hashlib.sha256(value).hexdigest() != record["sha256"]:
        raise AssertionError(f"SHA-256 mismatch for {name}")
    return value


def exact_once_replace(
    source: bytes, old: bytes, new: bytes, context: str
) -> bytes:
    if not old:
        raise AssertionError(f"{context} has an empty match")
    if source.count(old) != 1:
        raise AssertionError(
            f"{context} matched {source.count(old)} times instead of once"
        )
    return source.replace(old, new, 1)


def eval_bytes(
    expression: dict[str, Any],
    constants: dict[str, bytes],
    referenced_constants: set[str],
    context: str,
) -> bytes:
    kind = expression.get("kind")
    if kind == "constant":
        require_keys(expression, {"kind", "name"}, context)
        name = expression["name"]
        if name not in constants:
            raise AssertionError(f"{context} references missing constant {name}")
        referenced_constants.add(name)
        return constants[name]
    if kind == "hex":
        require_keys(expression, {"kind", "value"}, context)
        return decode_hex(expression["value"], context)
    if kind == "utf8":
        require_keys(expression, {"kind", "value"}, context)
        return expression["value"].encode("utf-8")
    if kind == "concat":
        require_keys(expression, {"kind", "parts"}, context)
        if not expression["parts"]:
            raise AssertionError(f"{context} has empty concatenation")
        return b"".join(
            eval_bytes(
                part,
                constants,
                referenced_constants,
                f"{context}.parts[{index}]",
            )
            for index, part in enumerate(expression["parts"])
        )
    if kind == "replace_utf8":
        require_keys(
            expression, {"kind", "source", "old", "new"}, context
        )
        source = eval_bytes(
            expression["source"],
            constants,
            referenced_constants,
            f"{context}.source",
        )
        return exact_once_replace(
            source,
            expression["old"].encode("utf-8"),
            expression["new"].encode("utf-8"),
            context,
        )
    if kind == "insert_utf8_after":
        require_keys(
            expression,
            {"kind", "source", "anchor", "text"},
            context,
        )
        source = eval_bytes(
            expression["source"],
            constants,
            referenced_constants,
            f"{context}.source",
        )
        anchor = expression["anchor"].encode("utf-8")
        return exact_once_replace(
            source,
            anchor,
            anchor + expression["text"].encode("utf-8"),
            context,
        )
    if kind == "insert_bytes_after":
        require_keys(
            expression,
            {"kind", "source", "anchor", "bytes"},
            context,
        )
        source = eval_bytes(
            expression["source"],
            constants,
            referenced_constants,
            f"{context}.source",
        )
        anchor = eval_bytes(
            expression["anchor"],
            constants,
            referenced_constants,
            f"{context}.anchor",
        )
        inserted = eval_bytes(
            expression["bytes"],
            constants,
            referenced_constants,
            f"{context}.bytes",
        )
        return exact_once_replace(
            source, anchor, anchor + inserted, context
        )
    if kind == "delete_utf8_exact":
        require_keys(expression, {"kind", "source", "text"}, context)
        source = eval_bytes(
            expression["source"],
            constants,
            referenced_constants,
            f"{context}.source",
        )
        return exact_once_replace(
            source, expression["text"].encode("utf-8"), b"", context
        )
    if kind == "bd":
        require_keys(
            expression,
            {
                "kind",
                "package",
                "version",
                "profiles",
                "module_file",
                "files",
            },
            context,
        )
        output = (
            f"package: {expression['package']}\n"
            f'version: "{expression["version"]}"\n'
            'lattice: "0.3"\n'
            "profiles:\n"
        )
        output += "".join(
            f"  - {profile}\n" for profile in expression["profiles"]
        )
        output += (
            f"module_file: {expression['module_file']}\nfiles:\n"
        )
        output += "".join(
            f"  - path: {file['path']}\n"
            f"    sha256: {file['sha256']}\n"
            for file in expression["files"]
        )
        return output.encode("ascii")
    if kind == "bdp":
        require_keys(
            expression, {"kind", "path_scalar_source"}, context
        )
        scalar = expression["path_scalar_source"]
        return (
            "package: alpha\n"
            'version: "1.0.0"\n'
            'lattice: "0.3"\n'
            "profiles:\n"
            "  - lattice-core-0.1\n"
            f"module_file: {scalar}\n"
            "files:\n"
            f"  - path: {scalar}\n"
            f"    sha256: {MODULE_DIGEST}\n"
        ).encode("utf-8")
    if kind == "bdf":
        require_keys(
            expression,
            {
                "kind",
                "module_file_scalar_source",
                "files",
            },
            context,
        )
        output = (
            "package: alpha\n"
            'version: "1.0.0"\n'
            'lattice: "0.3"\n'
            "profiles:\n"
            "  - lattice-core-0.1\n"
            f"module_file: {expression['module_file_scalar_source']}\n"
            "files:\n"
        )
        output += "".join(
            f"  - path: {file['path_scalar_source']}\n"
            f"    sha256: {file['sha256_scalar_source']}\n"
            for file in expression["files"]
        )
        return output.encode("utf-8")
    raise AssertionError(f"{context} has undeclared byte expression {kind}")


def validate_node(
    node: dict[str, Any],
    constants: dict[str, bytes],
    referenced_constants: set[str],
    context: str,
) -> dict[str, Any]:
    kind = node.get("kind")
    if kind == "directory":
        require_keys(node, {"kind", "children"}, context)
        if node["children"]:
            raise AssertionError(
                f"{context} ordinary directory must start exactly empty"
            )
        return copy.deepcopy(node)
    if kind == "directory_unreadable":
        require_keys(node, {"kind"}, context)
        return copy.deepcopy(node)
    if kind == "regular":
        require_keys(
            node, {"kind", "bytes", "hardlink_group"}, context
        )
        evaluated = eval_bytes(
            node["bytes"],
            constants,
            referenced_constants,
            f"{context}.bytes",
        )
        return {
            "kind": "regular",
            "bytes_value": evaluated,
            "hardlink_group": node["hardlink_group"],
        }
    if kind == "regular_unreadable":
        require_keys(node, {"kind"}, context)
        return copy.deepcopy(node)
    if kind == "link":
        require_keys(node, {"kind", "target"}, context)
        if not node["target"]:
            raise AssertionError(f"{context} has empty link target evidence")
        return copy.deepcopy(node)
    if kind == "special":
        require_keys(node, {"kind", "special_kind"}, context)
        if not node["special_kind"]:
            raise AssertionError(f"{context} has empty special kind")
        return copy.deepcopy(node)
    raise AssertionError(f"{context} has undeclared node kind {kind}")


def directory_entries(node: dict[str, Any], context: str) -> list[dict[str, Any]]:
    if node.get("kind") != "directory":
        raise AssertionError(f"{context} is not a readable directory")
    return node["children"]


def split_path(path: str, context: str) -> list[str]:
    parts = path.split("/")
    if not path or any(not part for part in parts):
        raise AssertionError(f"{context} has malformed mutation path {path!r}")
    return parts


def find_entry(
    entries: list[dict[str, Any]], name: str, context: str
) -> tuple[int, dict[str, Any]] | None:
    matches = [
        (index, entry)
        for index, entry in enumerate(entries)
        if entry["name"] == name
    ]
    if len(matches) > 1:
        raise AssertionError(f"{context} has duplicate child {name}")
    return matches[0] if matches else None


def parent_for_path(
    root: dict[str, Any], path: str, context: str
) -> tuple[list[dict[str, Any]], str]:
    parts = split_path(path, context)
    node = root
    for part in parts[:-1]:
        entries = directory_entries(node, context)
        match = find_entry(entries, part, context)
        if match is None:
            raise AssertionError(
                f"{context} targets nonexistent ancestor {part}"
            )
        node = match[1]["node"]
    return directory_entries(node, context), parts[-1]


def apply_operation(
    root: dict[str, Any],
    operation: dict[str, Any],
    constants: dict[str, bytes],
    referenced_constants: set[str],
    context: str,
) -> None:
    op = operation.get("op")
    if op == "add":
        require_keys(operation, {"op", "path", "node"}, context)
        entries, name = parent_for_path(
            root, operation["path"], context
        )
        if find_entry(entries, name, context) is not None:
            raise AssertionError(f"{context} ADD target already exists")
        entries.append(
            {
                "name": name,
                "node": validate_node(
                    operation["node"],
                    constants,
                    referenced_constants,
                    f"{context}.node",
                ),
            }
        )
        return
    if op == "remove":
        require_keys(operation, {"op", "path"}, context)
        entries, name = parent_for_path(
            root, operation["path"], context
        )
        match = find_entry(entries, name, context)
        if match is None:
            raise AssertionError(f"{context} REMOVE target is absent")
        entries.pop(match[0])
        return
    if op == "replace_node":
        require_keys(operation, {"op", "path", "node"}, context)
        entries, name = parent_for_path(
            root, operation["path"], context
        )
        match = find_entry(entries, name, context)
        if match is None:
            raise AssertionError(
                f"{context} REPLACE_NODE target is absent"
            )
        match[1]["node"] = validate_node(
            operation["node"],
            constants,
            referenced_constants,
            f"{context}.node",
        )
        return
    if op in {"replace_hex", "set_descriptor"}:
        expected = (
            {"op", "path", "bytes"}
            if op == "replace_hex"
            else {"op", "path", "bytes"}
        )
        require_keys(operation, expected, context)
        bytes_expression = operation["bytes"]
        if op == "replace_hex":
            if (
                not isinstance(bytes_expression, dict)
                or bytes_expression.get("kind") != "hex"
            ):
                raise AssertionError(
                    f"{context} REPLACE_HEX requires "
                    "an exact hex byte expression"
                )
            require_keys(
                bytes_expression,
                {"kind", "value"},
                f"{context}.bytes",
            )
            bytes_value = decode_hex(
                bytes_expression["value"], f"{context}.bytes"
            )
        else:
            bytes_value = eval_bytes(
                bytes_expression,
                constants,
                referenced_constants,
                f"{context}.bytes",
            )
        entries, name = parent_for_path(
            root, operation["path"], context
        )
        match = find_entry(entries, name, context)
        if match is None or match[1]["node"].get("kind") != "regular":
            raise AssertionError(
                f"{context} byte replacement target is not regular"
            )
        if op == "set_descriptor" and name != "package.yaml":
            raise AssertionError(
                f"{context} SET_DESCRIPTOR target is not package.yaml"
            )
        match[1]["node"] = {
            "kind": "regular",
            "bytes_value": bytes_value,
            "hardlink_group": None,
        }
        return
    if op == "rename":
        require_keys(
            operation,
            {"op", "path", "new_final_component"},
            context,
        )
        entries, name = parent_for_path(
            root, operation["path"], context
        )
        match = find_entry(entries, name, context)
        if match is None:
            raise AssertionError(f"{context} RENAME target is absent")
        new_name = operation["new_final_component"]
        if "/" in new_name or not new_name:
            raise AssertionError(f"{context} has invalid rename component")
        if find_entry(entries, new_name, context) is not None:
            raise AssertionError(f"{context} RENAME target already exists")
        match[1]["name"] = new_name
        return
    if op == "set_child_enumeration":
        require_keys(operation, {"op", "path", "names"}, context)
        parts = split_path(operation["path"], context)
        node = root
        for part in parts:
            entries = directory_entries(node, context)
            match = find_entry(entries, part, context)
            if match is None:
                raise AssertionError(
                    f"{context} enumeration target is absent"
                )
            node = match[1]["node"]
        entries = directory_entries(node, context)
        names = operation["names"]
        if len(names) != len(set(names)):
            raise AssertionError(
                f"{context} enumeration contains duplicates"
            )
        if sorted(names) != sorted(entry["name"] for entry in entries):
            raise AssertionError(
                f"{context} enumeration is not the exact child map"
            )
        by_name = {entry["name"]: entry for entry in entries}
        entries[:] = [by_name[name] for name in names]
        return
    if op == "share_hardlink":
        require_keys(
            operation,
            {"op", "path_a", "path_b", "group_id"},
            context,
        )
        nodes = []
        for key in ["path_a", "path_b"]:
            entries, name = parent_for_path(
                root, operation[key], context
            )
            match = find_entry(entries, name, context)
            if match is None or match[1]["node"].get("kind") != "regular":
                raise AssertionError(
                    f"{context} hard-link target is not regular"
                )
            nodes.append(match[1]["node"])
        if nodes[0]["bytes_value"] != nodes[1]["bytes_value"]:
            raise AssertionError(
                f"{context} hard-link targets have different bytes"
            )
        for node in nodes:
            node["hardlink_group"] = operation["group_id"]
        return
    raise AssertionError(f"{context} has undeclared operation {op}")


def validate_acquisition_node(node: dict[str, Any], context: str) -> None:
    kind = node.get("kind")
    if kind == "directory":
        require_keys(node, {"kind", "children"}, context)
        names: list[tuple[Any, ...]] = []
        for index, child in enumerate(node["children"]):
            child_context = f"{context}.children[{index}]"
            require_keys(child, {"name", "node"}, child_context)
            name = child["name"]
            name_kind = name.get("kind")
            if name_kind == "unicode":
                require_keys(name, {"kind", "value"}, f"{child_context}.name")
                identity = ("unicode", name["value"])
            elif name_kind == "unix_bytes":
                require_keys(name, {"kind", "hex"}, f"{child_context}.name")
                identity = (
                    "unix_bytes",
                    decode_hex(name["hex"], f"{child_context}.name"),
                )
            elif name_kind == "windows_utf16":
                require_keys(
                    name, {"kind", "units"}, f"{child_context}.name"
                )
                if any(
                    not isinstance(unit, int) or not 0 <= unit <= 0xFFFF
                    for unit in name["units"]
                ):
                    raise AssertionError(
                        f"{child_context}.name has invalid UTF-16 unit"
                    )
                identity = ("windows_utf16", *name["units"])
            else:
                raise AssertionError(
                    f"{child_context}.name has unknown representation"
                )
            if identity in names:
                raise AssertionError(
                    f"{context} contains duplicate raw name evidence"
                )
            names.append(identity)
            validate_acquisition_node(child["node"], f"{child_context}.node")
        return
    if kind in {
        "directory_unreadable",
        "regular_unreadable",
    }:
        require_keys(node, {"kind"}, context)
        return
    if kind == "regular":
        require_keys(node, {"kind", "bytes", "hardlink_group"}, context)
        return
    if kind == "link":
        require_keys(node, {"kind", "target"}, context)
        return
    if kind == "special":
        require_keys(node, {"kind", "special_kind"}, context)
        return
    raise AssertionError(f"{context} has unknown acquisition node {kind}")


def canonical_descriptor(record: dict[str, Any]) -> bytes:
    value = {
        "package": record["package"],
        "version": record["version"],
        "lattice": record["lattice"],
        "profiles": record["profiles"],
        "module_file": record["module_file"],
        "files": [
            {"path": file["path"], "sha256": file["sha256"]}
            for file in record["files"]
        ],
    }
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def validate_plan(plan: dict[str, Any], manifest: dict[str, Any]) -> None:
    require_keys(
        plan,
        {
            "fixture_plan_version",
            "authority",
            "source_vocabulary",
            "base_snapshots",
            "operation_vocabulary",
            "byte_expression_vocabulary",
            "node_vocabulary",
            "relation_vocabulary",
            "expected_packages",
            "golden_record_ids",
            "cases",
        },
        "plan",
    )
    if plan["fixture_plan_version"] != "pc6-package-scan-executable-plan-1":
        raise AssertionError("unknown executable fixture-plan version")
    if plan["authority"] != manifest["authority"]:
        raise AssertionError("plan authority differs from fixture manifest")
    authority_hash = hashlib.sha256(AUTHORITY_PATH.read_bytes()).hexdigest()
    if authority_hash != manifest["authority"]["sha256"]:
        raise AssertionError("accepted erratum hash differs from authority")

    expected_counts = {
        "authoritative_byte_constants": 34,
        "canonical_package_vectors": 6,
        "package_identities": 19,
        "descriptor_presentations": 18,
        "path_scalar_vectors": 18,
        "pointer_vectors": 6,
        "fixtures": 184,
        "diagnostic_expectations": 124,
        "diagnostic_codes": 31,
    }
    if manifest["counts"] != expected_counts:
        raise AssertionError("frozen population counts changed")

    constants: dict[str, bytes] = {}
    constant_hashes: dict[str, str] = {}
    for index, record in enumerate(manifest["authoritative_byte_constants"]):
        context = f"authoritative_byte_constants[{index}]"
        require_keys(record, {"name", "hex", "length", "sha256"}, context)
        name = record["name"]
        if name in constants:
            raise AssertionError(f"duplicate byte constant {name}")
        value = decode_hex(record["hex"], context)
        if len(value) != record["length"]:
            raise AssertionError(f"length mismatch for {name}")
        digest = hashlib.sha256(value).hexdigest()
        if digest != record["sha256"]:
            raise AssertionError(f"SHA-256 mismatch for {name}")
        constants[name] = value
        constant_hashes[name] = digest
    if len(constants) != 34:
        raise AssertionError("authoritative byte-constant count changed")

    vectors: dict[str, dict[str, Any]] = {}
    for index, vector in enumerate(manifest["canonical_package_vectors"]):
        context = f"canonical_package_vectors[{index}]"
        require_keys(
            vector,
            {"name", "canonical_hex", "length", "sha256", "identity"},
            context,
        )
        name = vector["name"]
        if name in vectors:
            raise AssertionError(f"duplicate canonical vector {name}")
        value = decode_hex(vector["canonical_hex"], context)
        digest = hashlib.sha256(value).hexdigest()
        if (
            len(value) != vector["length"]
            or digest != vector["sha256"]
            or vector["identity"]
            != f"lattice:package:sha256:{digest}"
        ):
            raise AssertionError(f"canonical vector mismatch for {name}")
        vectors[name] = {**vector, "bytes_value": value}
    if len(vectors) != 6:
        raise AssertionError("canonical vector count changed")

    referenced_constants: set[str] = set()
    referenced_vectors: set[str] = set()
    source_names = set(plan["source_vocabulary"])
    if source_names != {"DS-A", "DS-B"}:
        raise AssertionError("source vocabulary is not exact")
    for source_name, source in plan["source_vocabulary"].items():
        require_keys(
            source, {"yaml", "byte_constant"}, f"source {source_name}"
        )
        constant_name = source["byte_constant"]
        if constant_name not in constants:
            raise AssertionError(
                f"source {source_name} references missing constant"
            )
        referenced_constants.add(constant_name)
        canonical_source = json.loads(constants[constant_name])
        if not isinstance(canonical_source, dict):
            raise AssertionError(f"source {source_name} is not an object")
        if canonical_source["purpose"] not in {
            "fixture root",
            "fixture root b",
        }:
            raise AssertionError(f"source {source_name} purpose differs")

    expected_operation_vocabulary = [
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
    ]
    if plan["operation_vocabulary"] != expected_operation_vocabulary:
        raise AssertionError("operation vocabulary is not exact")

    base_states: dict[str, dict[str, Any]] = {}
    used_operation_kinds: set[str] = set()
    for base_name, operations in plan["base_snapshots"].items():
        if base_name in base_states:
            raise AssertionError(f"duplicate base snapshot {base_name}")
        root = directory()
        for index, operation in enumerate(operations):
            used_operation_kinds.add(operation["op"])
            apply_operation(
                root,
                operation,
                constants,
                referenced_constants,
                f"base {base_name}[{index}]",
            )
        base_states[base_name] = root
    expected_bases = {
        "T-ABSENT",
        "T-EMPTY",
        "T-MINIMAL",
        "T-MULTIPLE-PACKAGES",
        "T-MULTIPLE-VERSIONS",
        "T-MULTI-FILE",
        "T-HARDLINK",
        "T-VERSION-ORDER",
    }
    if set(base_states) != expected_bases:
        raise AssertionError("base-snapshot vocabulary is not exact")

    records = plan["expected_packages"]
    if set(plan["golden_record_ids"]) != set(records):
        raise AssertionError("unreachable expected package record")
    record_identities: set[str] = set()
    for record_name, record in records.items():
        require_keys(
            record,
            {
                "identity",
                "package",
                "version",
                "lattice",
                "profiles",
                "module_file",
                "files",
                "canonical_vector",
            },
            f"expected package {record_name}",
        )
        if record["identity"] in record_identities:
            raise AssertionError(
                f"duplicate expected identity {record['identity']}"
            )
        record_identities.add(record["identity"])
        if record["lattice"] != "0.3":
            raise AssertionError(f"{record_name} lattice differs")
        if record["profiles"] != sorted(record["profiles"]):
            raise AssertionError(f"{record_name} profiles are not canonical")
        paths = [file["path"] for file in record["files"]]
        if paths != sorted(paths) or len(paths) != len(set(paths)):
            raise AssertionError(f"{record_name} file order differs")
        for file_index, file in enumerate(record["files"]):
            require_keys(
                file,
                {"path", "sha256", "byte_constant"},
                f"{record_name}.files[{file_index}]",
            )
            constant_name = file["byte_constant"]
            if constant_name not in constants:
                raise AssertionError(
                    f"{record_name} references missing bytes"
                )
            referenced_constants.add(constant_name)
            if constant_hashes[constant_name] != file["sha256"]:
                raise AssertionError(
                    f"{record_name} retained-byte hash differs"
                )
        canonical = canonical_descriptor(record)
        digest = hashlib.sha256(canonical).hexdigest()
        if record["identity"] != f"lattice:package:sha256:{digest}":
            raise AssertionError(
                f"{record_name} identity is not reproducible"
            )
        vector_name = record["canonical_vector"]
        if vector_name is not None:
            if vector_name not in vectors:
                raise AssertionError(
                    f"{record_name} references missing vector"
                )
            referenced_vectors.add(vector_name)
            if vectors[vector_name]["bytes_value"] != canonical:
                raise AssertionError(
                    f"{record_name} canonical vector differs"
                )

    manifest_identities = set(manifest["package_identities"])
    if len(manifest_identities) != 19:
        raise AssertionError("package identity population changed")
    if not manifest_identities.issubset(record_identities):
        raise AssertionError("unreachable package identity record")
    data_changed = canonical_descriptor(records["data_changed"])
    if len(data_changed) != 318:
        raise AssertionError("DATA_CHANGED canonical vector is not 318 bytes")
    required_data_changed = (
        "lattice:package:sha256:"
        "b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b"
    )
    if records["data_changed"]["identity"] != required_data_changed:
        raise AssertionError("DATA_CHANGED identity differs")

    manifest_fixtures = manifest["fixtures"]
    fixture_ids = [fixture["id"] for fixture in manifest_fixtures]
    if len(fixture_ids) != 184 or len(set(fixture_ids)) != 184:
        raise AssertionError("fixture IDs are not 184 unique values")
    case_ids = [case["id"] for case in plan["cases"]]
    if case_ids != fixture_ids or len(set(case_ids)) != 184:
        raise AssertionError("fixture dispatch is not exact and ordered")
    fixture_by_id = {
        fixture["id"]: fixture for fixture in manifest_fixtures
    }

    flattened_expectations: list[tuple[str, str, str]] = []
    for fixture in manifest_fixtures:
        for expectation in fixture["diagnostic_expectations"]:
            flattened_expectations.append(
                (
                    fixture["id"],
                    expectation["code"],
                    expectation["path"],
                )
            )
    top_expectations = [
        (entry["id"], entry["code"], entry["path"])
        for entry in manifest["diagnostic_expectations"]
    ]
    if sorted(flattened_expectations) != sorted(top_expectations):
        raise AssertionError("diagnostic expectation ledger is unreachable")
    if len(top_expectations) != 124:
        raise AssertionError("diagnostic expectation count changed")

    used_bases: set[str] = set()
    used_sources: set[str] = set()
    used_records: set[str] = set()
    used_relations: set[str] = set()
    primary_codes: set[str] = set()
    executed_ids: set[str] = set()
    for case_index, case in enumerate(plan["cases"]):
        context = f"cases[{case_index}]"
        require_keys(
            case,
            {
                "id",
                "fixture_class",
                "input_sha256",
                "expected_sha256",
                "program",
                "outcome",
            },
            context,
        )
        fixture = fixture_by_id[case["id"]]
        if case["id"] in executed_ids:
            raise AssertionError(f"duplicate case execution {case['id']}")
        executed_ids.add(case["id"])
        if case["fixture_class"] != fixture["fixture_class"]:
            raise AssertionError(f"{case['id']} fixture class differs")
        if case["input_sha256"] != sha256_text(fixture["exact_input"]):
            raise AssertionError(f"{case['id']} input binding differs")
        if case["expected_sha256"] != sha256_text(fixture["expected"]):
            raise AssertionError(f"{case['id']} expectation binding differs")
        program = case["program"]
        outcome = case["outcome"]
        program_kind = program.get("kind")
        if program_kind == "scan":
            require_keys(program, {"kind", "runs"}, f"{context}.program")
            if not program["runs"]:
                raise AssertionError(f"{case['id']} has no public scan run")
            if outcome["kind"] == "diagnostic":
                require_keys(
                    outcome, {"kind", "code", "path"}, f"{context}.outcome"
                )
                if fixture["expected_diagnostic"] != {
                    "code": outcome["code"],
                    "path": outcome["path"],
                }:
                    raise AssertionError(
                        f"{case['id']} diagnostic expectation differs"
                    )
                primary_codes.add(outcome["code"])
                if len(program["runs"]) != 1:
                    raise AssertionError(
                        f"{case['id']} diagnostic has multiple runs"
                    )
            elif outcome["kind"] == "success":
                require_keys(
                    outcome,
                    {"kind", "run_packages", "relation"},
                    f"{context}.outcome",
                )
                if fixture["expected_diagnostic"] is not None:
                    raise AssertionError(
                        f"{case['id']} suppresses expected diagnostic"
                    )
                if len(outcome["run_packages"]) != len(program["runs"]):
                    raise AssertionError(
                        f"{case['id']} has incomplete success results"
                    )
                relation = outcome["relation"]
                if relation not in plan["relation_vocabulary"]:
                    raise AssertionError(
                        f"{case['id']} has undeclared relation {relation}"
                    )
                used_relations.add(relation)
                for run_records in outcome["run_packages"]:
                    for record_name in run_records:
                        if record_name not in records:
                            raise AssertionError(
                                f"{case['id']} references missing record"
                            )
                        used_records.add(record_name)
            else:
                raise AssertionError(f"{case['id']} has unknown outcome")

            for run_index, run_spec in enumerate(program["runs"]):
                run_context = f"{context}.program.runs[{run_index}]"
                require_keys(
                    run_spec,
                    {
                        "source",
                        "base",
                        "operations",
                        "timing",
                        "live_operations",
                    },
                    run_context,
                )
                source_name = run_spec["source"]
                base_name = run_spec["base"]
                if source_name not in source_names:
                    raise AssertionError(
                        f"{case['id']} references missing source"
                    )
                if base_name not in base_states:
                    raise AssertionError(
                        f"{case['id']} references missing base"
                    )
                used_sources.add(source_name)
                used_bases.add(base_name)
                state = copy.deepcopy(base_states[base_name])
                for operation_index, operation in enumerate(
                    run_spec["operations"]
                ):
                    used_operation_kinds.add(operation["op"])
                    apply_operation(
                        state,
                        operation,
                        constants,
                        referenced_constants,
                        f"{run_context}.operations[{operation_index}]",
                    )
                timing = run_spec["timing"]
                if timing not in {
                    "normal",
                    "mutate_after_acquisition",
                    "mutate_after_scan",
                }:
                    raise AssertionError(
                        f"{case['id']} has undeclared timing {timing}"
                    )
                if timing == "normal" and run_spec["live_operations"]:
                    raise AssertionError(
                        f"{case['id']} has unreachable live operations"
                    )
                if timing != "normal" and not run_spec["live_operations"]:
                    raise AssertionError(
                        f"{case['id']} omits required live mutation"
                    )
                for operation_index, operation in enumerate(
                    run_spec["live_operations"]
                ):
                    used_operation_kinds.add(operation["op"])
                    apply_operation(
                        state,
                        operation,
                        constants,
                        referenced_constants,
                        f"{run_context}.live_operations[{operation_index}]",
                    )
        elif program_kind == "acquisition":
            require_keys(
                program, {"kind", "acquisition"}, f"{context}.program"
            )
            require_keys(
                outcome,
                {"kind", "error"},
                f"{context}.outcome",
            )
            if outcome["kind"] != "acquisition_failure":
                raise AssertionError(
                    f"{case['id']} acquisition does not fail"
                )
            if fixture["expected_diagnostic"] is not None:
                raise AssertionError(
                    f"{case['id']} invents semantic diagnostic"
                )
            acquisition = program["acquisition"]
            mode = acquisition.get("mode")
            if mode == "node":
                require_keys(
                    acquisition,
                    {"mode", "node", "evidence"},
                    f"{context}.acquisition",
                )
                validate_acquisition_node(
                    acquisition["node"], f"{context}.acquisition.node"
                )
            elif mode == "reported_error":
                require_keys(
                    acquisition,
                    {"mode", "error", "evidence"},
                    f"{context}.acquisition",
                )
                if acquisition["error"] != outcome["error"]:
                    raise AssertionError(
                        f"{case['id']} acquisition error differs"
                    )
            else:
                raise AssertionError(
                    f"{case['id']} has undeclared acquisition mode"
                )
            if not acquisition["evidence"]:
                raise AssertionError(
                    f"{case['id']} omits acquisition evidence"
                )
        else:
            raise AssertionError(
                f"{case['id']} has undeclared program kind {program_kind}"
            )

    if executed_ids != set(fixture_ids):
        raise AssertionError("not every fixture is executed exactly once")
    if primary_codes != set(manifest["diagnostic_codes"]):
        raise AssertionError("not all 31 diagnostic codes are exercised")
    if used_sources != source_names:
        raise AssertionError("unreachable source vector")
    if used_bases != expected_bases:
        raise AssertionError("unreachable base snapshot")
    if used_records.difference(records):
        raise AssertionError("unreachable result reference")
    if referenced_vectors != set(vectors):
        raise AssertionError("unreachable canonical vector")
    if referenced_constants != set(constants):
        missing_constants = sorted(set(constants) - referenced_constants)
        raise AssertionError(
            f"unreachable byte constants {missing_constants}"
        )
    if set(plan["golden_record_ids"]) != set(records):
        raise AssertionError("unreachable golden record")
    if not {"add", "remove", "replace_node", "replace_hex", "set_descriptor",
            "rename", "set_child_enumeration", "share_hardlink"}.issubset(
        used_operation_kinds
    ):
        raise AssertionError("not every concrete snapshot operation is used")
    expected_relations = set(plan["relation_vocabulary"])
    if used_relations != expected_relations:
        raise AssertionError(
            f"relation vocabulary unreachable: "
            f"{sorted(expected_relations - used_relations)}"
        )


def main() -> None:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true")
    mode.add_argument("--check", action="store_true")
    args = parser.parse_args()

    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    plan = make_plan(manifest)
    validate_plan(plan, manifest)
    rendered = (
        json.dumps(
            plan,
            ensure_ascii=False,
            sort_keys=True,
            indent=2,
        )
        + "\n"
    )
    if args.write:
        PLAN_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    else:
        if not PLAN_PATH.exists():
            raise AssertionError("executable fixture plan is absent")
        committed = PLAN_PATH.read_text(encoding="utf-8")
        if committed != rendered:
            raise AssertionError(
                "executable fixture plan is stale or hand-modified"
            )

    print("authority_sha256=" + manifest["authority"]["sha256"])
    print("fixture_ids=184 unique=184 dispatched=184")
    scan_cases = sum(
        case["program"]["kind"] == "scan" for case in plan["cases"]
    )
    acquisition_cases = len(plan["cases"]) - scan_cases
    scan_runs = sum(
        len(case["program"]["runs"])
        for case in plan["cases"]
        if case["program"]["kind"] == "scan"
    )
    diagnostic_cases = sum(
        case["outcome"]["kind"] == "diagnostic" for case in plan["cases"]
    )
    success_cases = sum(
        case["outcome"]["kind"] == "success" for case in plan["cases"]
    )
    print(
        f"scan_cases={scan_cases} scan_runs={scan_runs} "
        f"diagnostic_cases={diagnostic_cases} "
        f"success_cases={success_cases} "
        f"acquisition_cases={acquisition_cases}"
    )
    print("diagnostic_expectations=124 diagnostic_codes_exercised=31")
    print("byte_constants=34 canonical_vectors=6 package_identities=19")
    print(
        "data_changed_canonical_bytes=318 "
        "data_changed_identity="
        "lattice:package:sha256:"
        "b84865cb448e61f64f9cd5e685f85c1e88d24ef2fa29100943ea4d60d3da101b"
    )
    print("all_references_resolved=true all_operations_constructible=true")


if __name__ == "__main__":
    main()
