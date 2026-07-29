#!/usr/bin/env python3
"""Strict PC8 Lock manifest admission and deterministic executable-plan generation."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any, NoReturn


ROOT = Path(__file__).resolve().parents[3]
PLAN_PATH = ROOT / "conformance/pc8/lock/executable_fixture_plan.json"
REGISTRY_PATH = Path("docs/pc8/PC8_AUTHORITY_REGISTRY_V2.json")
MANIFEST_PATH = Path("docs/pc8/PC8_LOCK_SPECIFIED_CONFORMANCE_MANIFEST_V2.json")
PC7_REGISTRY_PATH = Path("docs/pc7/PC7_AUTHORITY_REGISTRY_V1.json")
PC7_MANIFEST_PATH = Path("docs/pc7/PC7_RESOLVE_SPECIFIED_CONFORMANCE_MANIFEST.json")
PC7_GENERATOR_PATH = ROOT / "conformance/pc7/resolve/build_executable_fixture_plan.py"

REGISTRY_FORMAT = "threadsmith-pc8-authority-registry-2"
REGISTRY_BYTES = 21_344
REGISTRY_SHA256 = "b442f1acb4a7eb316ed9d61da02af3c1e5c60c34f55cf6eefefa751339d0a2c6"
MANIFEST_BYTES = 1_053_112
MANIFEST_SHA256 = "314e1cd73f23c07067e167d37e84782c7a301b13b4c6458d62a37d0423c4482a"
PC7_REGISTRY_BYTES = 2_041
PC7_REGISTRY_SHA256 = "7f39265be8bfd6db9fc93cedf357572eb5fab960000b9d6897ef983021112161"
PC7_MANIFEST_BYTES = 1_306_575
PC7_MANIFEST_SHA256 = "da33daef1526e21a921c8b7bb847045f6e137567f2c0b3b3e6f2af9a796c123c"
PC7_PUBLICATION_REPORT = Path(
    "/workspace/ThreadSmith/PC7/handoffs/implementation-acceptance-publication/"
    "output/THREADSMITH_PC7_IMPLEMENTATION_ACCEPTANCE_PUBLICATION_AND_"
    "DURABLE_STATE_UPDATE.txt"
)
PC7_PUBLICATION_BYTES = 24_874
PC7_PUBLICATION_SHA256 = (
    "7064a32177e39b8ee6dd5a39faca8e93c5511a03b9e7c7df8715b50e9ca79cce"
)

EXPECTED_STATUS = {
    "OPEN_CONFORMANCE_CRITERIA_DEFECTS": 0,
    "OPEN_IMPLEMENTATION_DEFECTS": 2,
    "OPEN_IMPLEMENTATION_DEFECT_IDS": ["PC8-T2-SM-02", "PC8-T2-SC-03"],
    "PC8_ACCEPTED": False,
    "PC8_IMPLEMENTATION_STARTED": True,
    "PC8_SEMANTICS_ACCEPTED": True,
    "PC8_SEMANTICS_FROZEN": True,
    "PC8_SPECIFIED_CONFORMANCE_V1_CURRENT": False,
    "PC8_SPECIFIED_CONFORMANCE_V2_ACCEPTED": True,
    "PC8_SPECIFIED_CONFORMANCE_V2_PUBLISHED": True,
    "PC8_SPECIFIED_CONFORMANCE_V2_REVIEWED": True,
    "PC8_TASK_1_ACCEPTED": True,
    "PC8_TASK_2_ACCEPTED": False,
    "PC8_TASK_3_AUTHORIZED": False,
    "POST_FREEZE_PC8_LOCK_NORMATIVE_SUPERSESSIONS": 0,
    "POST_FREEZE_PC8_SPECIFIED_CRITERIA_SUPERSESSIONS": 1,
}
EXPECTED_DISPATCH = {
    "external_evidence_is_dispatchable": False,
    "external_evidence_is_normative": False,
    "normative_authority_keys": [
        "lattice_standard",
        "canonical_json_erratum",
        "package_scan_semantics_erratum",
        "resolve_semantics_erratum",
        "pc8_lock_semantics_erratum",
    ],
    "procedural_records_are_dispatchable": False,
    "procedural_records_are_normative": False,
    "specified_criteria_key": "pc8_lock_specified_conformance_manifest_v2",
    "superseded_specified_criteria_key": "pc8_lock_specified_conformance_manifest_v1",
}
EXPECTED_CANDIDATE_STATUS = {
    "maturity": "candidate_specified",
    "executable": False,
    "qualified": False,
    "implementation_verified": False,
    "independently_reviewed": False,
    "accepted": False,
    "published": False,
}
EXPECTED_POPULATIONS = {
    "authority": 10,
    "rule_provenance": 40,
    "schemas": 16,
    "normative_choices": 14,
    "resolved_sources": 20,
    "fixtures": 20,
    "relations": 19,
    "discriminators": 41,
    "preimage_registry": 4,
    "future_only": 4,
    "schema_mutations": 12,
}
EXPECTED_RULE_COUNTS = {"S": 10, "C": 10, "N": 14, "D": 6}
EXPECTED_PREIMAGE_SPANS = 235
RELATION_KINDS = {
    "admission",
    "byte_domain_distinction",
    "direct_projection_nonmembership",
    "distinction",
    "encoding",
    "equivalence",
    "identity_preimage",
    "membership",
    "nondependence",
    "ordering",
    "phase_ownership",
    "totality",
}
EXPECTED_FUTURE_IDS = {
    "FUT-NONASCII-PACKAGE-ORDER",
    "FUT-PHYSICAL-PERSISTENCE-ADAPTER",
    "FUT-PROFILE-ALTERNATIVE",
    "FUT-PROPER-PREFIX-PACKAGE-VECTOR",
}
EXPECTED_MUTATION_FAILURES = {
    "DISC-SCHEMA-ARRAY-ITEM-MISMATCH": "object required",
    "DISC-SCHEMA-CHILD-MISMATCH": "child rejected",
    "DISC-SCHEMA-CONST-VIOLATION": "constant mismatch",
    "DISC-SCHEMA-CROSS-FIELD": "cross-field mismatch",
    "DISC-SCHEMA-ENUM-VIOLATION": "enum mismatch",
    "DISC-SCHEMA-MISSING-REQUIRED": "missing ['executable']",
    "DISC-SCHEMA-NULLABLE-MISMATCH": "enum mismatch",
    "DISC-SCHEMA-OPTIONAL-ABSENT-MISMATCH": "primitive category",
    "DISC-SCHEMA-UNION-VARIANT-MISMATCH": "constant mismatch",
    "DISC-SCHEMA-UNKNOWN-MEMBER": "unknown ['unexpected']",
    "DISC-SCHEMA-WRONG-BOOLEAN-STRING": "constant mismatch",
    "DISC-SCHEMA-WRONG-OBJECT-CATEGORY": "object required",
}


@dataclass
class PlanError(Exception):
    code: str
    path: str
    reason: str

    def __str__(self) -> str:
        return f"{self.code} at {self.path}: {self.reason}"


@dataclass
class AuthorityPreflightError(Exception):
    gate: str
    path: str
    reason: str
    fixture_dispatch_started: bool = False

    def __str__(self) -> str:
        return (
            "PC8_AUTHORITY_PREFLIGHT_REJECTED "
            f"gate={self.gate} path={self.path} reason={self.reason} "
            "fixture_dispatch_started=false"
        )


@dataclass
class AdmissionError(Exception):
    schema_path: str
    value_path: str
    reason: str

    def __str__(self) -> str:
        return (
            f"PC8_MANIFEST_SCHEMA_REJECTED schema={self.schema_path} "
            f"value={self.value_path} reason={self.reason}"
        )


class Pairs(list):
    """Distinguish a JSON object from an array during duplicate detection."""


def fail(code: str, path: str, reason: str) -> NoReturn:
    raise PlanError(code, path, reason)


def preflight_fail(gate: str, path: str, reason: str) -> NoReturn:
    raise AuthorityPreflightError(gate, path, reason)


def sha256(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read_exact(path: Path, size: int, digest: str, gate: str) -> bytes:
    try:
        raw = path.read_bytes()
    except OSError as error:
        preflight_fail(gate, str(path), f"unreadable: {error}")
    if len(raw) != size:
        preflight_fail(gate, str(path), f"bytes {len(raw)} != {size}")
    actual = sha256(raw)
    if actual != digest:
        preflight_fail(gate, str(path), f"sha256 {actual} != {digest}")
    return raw


def reject_float(_: str) -> NoReturn:
    fail("PC8_JSON_NUMBER_INVALID", "", "non-integer JSON number")


def pairs_to_value(value: Any, path: str = "$") -> Any:
    if isinstance(value, Pairs):
        result: dict[str, Any] = {}
        for key, child in value:
            if key in result:
                fail("PC8_JSON_DUPLICATE_MEMBER", f"{path}.{key}", "duplicate member")
            result[key] = pairs_to_value(child, f"{path}.{key}")
        return result
    if isinstance(value, list):
        return [pairs_to_value(child, f"{path}[{index}]") for index, child in enumerate(value)]
    return value


def strict_loads(raw: bytes, label: str) -> dict[str, Any]:
    if raw.startswith(b"\xef\xbb\xbf"):
        fail("PC8_JSON_BOM", label, "BOM forbidden")
    try:
        text = raw.decode("utf-8", errors="strict")
        parsed = json.loads(
            text,
            object_pairs_hook=Pairs,
            parse_float=reject_float,
            parse_constant=reject_float,
        )
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        fail("PC8_JSON_INVALID", label, str(error))
    value = pairs_to_value(parsed)
    if not isinstance(value, dict):
        fail("PC8_JSON_ROOT_INVALID", label, "root must be object")
    return value


def normalized(value: Any) -> Any:
    if isinstance(value, str):
        return unicodedata.normalize("NFC", value)
    if isinstance(value, list):
        return [normalized(child) for child in value]
    if isinstance(value, dict):
        return {normalized(key): normalized(child) for key, child in value.items()}
    if isinstance(value, float):
        fail("PC8_CANONICAL_JSON_INVALID", "$", "float forbidden")
    return value


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        normalized(value),
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def plan_bytes(value: Any) -> bytes:
    return (
        json.dumps(
            normalized(value),
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            indent=2,
        )
        + "\n"
    ).encode("utf-8")


def exact_equal(left: Any, right: Any) -> bool:
    return canonical_bytes(left) == canonical_bytes(right)


def utf8_sorted(values: list[str]) -> list[str]:
    return sorted(values, key=lambda value: value.encode("utf-8"))


def expect_exact_keys(
    value: Any,
    required: set[str],
    optional: set[str],
    path: str,
) -> dict[str, Any]:
    if not isinstance(value, dict):
        fail("PC8_SHAPE_INVALID", path, "expected object")
    missing = required - set(value)
    unknown = set(value) - required - optional
    if missing:
        fail("PC8_MEMBER_MISSING", path, f"missing {utf8_sorted(list(missing))}")
    if unknown:
        fail("PC8_MEMBER_UNKNOWN", path, f"unknown {utf8_sorted(list(unknown))}")
    return value


def authority_preflight(
    authority_root: Path, registry_path: Path
) -> tuple[dict[str, Any], bytes, bytes]:
    if authority_root.resolve() != ROOT.resolve():
        preflight_fail("authority_root", "authority#/root", "root differs from repository")
    required_registry = authority_root / REGISTRY_PATH
    if registry_path.resolve() != required_registry.resolve():
        preflight_fail("registry_binding", "authority#/registry", "wrong fixed registry path")
    registry_raw = read_exact(
        registry_path, REGISTRY_BYTES, REGISTRY_SHA256, "pc8_registry"
    )
    registry = strict_loads(registry_raw, "authority#/registry")
    if registry.get("format") != REGISTRY_FORMAT:
        preflight_fail("pc8_registry", "authority#/registry/format", "format mismatch")
    if registry.get("status_after_operative_publication") != EXPECTED_STATUS:
        preflight_fail("pc8_registry", "authority#/registry/status", "status mismatch")
    if registry.get("dispatch") != EXPECTED_DISPATCH:
        preflight_fail("pc8_registry", "authority#/registry/dispatch", "dispatch mismatch")
    current = [
        row
        for row in registry.get("specified_criteria", [])
        if row.get("pc8_dispatchable_after_operative_publication") is True
    ]
    if (
        len(current) != 1
        or current[0].get("key") != EXPECTED_DISPATCH["specified_criteria_key"]
        or current[0].get("path") != str(MANIFEST_PATH)
        or current[0].get("bytes") != MANIFEST_BYTES
        or current[0].get("sha256") != MANIFEST_SHA256
    ):
        preflight_fail(
            "pc8_registry",
            "authority#/registry/specified_criteria",
            "current V2 dispatch closure mismatch",
        )
    for population in (
        "normative_authority",
        "specified_criteria",
        "procedural_records",
        "external_evidence",
    ):
        rows = registry.get(population)
        if not isinstance(rows, list):
            preflight_fail("pc8_registry", f"authority#/registry/{population}", "not array")
        keys: set[str] = set()
        for index, record in enumerate(rows):
            key = record.get("key")
            if not isinstance(key, str) or key in keys:
                preflight_fail(
                    "pc8_registry",
                    f"authority#/registry/{population}[{index}]/key",
                    "missing or duplicate",
                )
            keys.add(key)
            bound = {"path", "bytes", "sha256"} <= set(record)
            if bound:
                path = Path(record["path"])
                read_exact(
                    path if path.is_absolute() else authority_root / path,
                    record["bytes"],
                    record["sha256"],
                    f"{population}[{index}]",
                )
            elif "identity_binding" not in record:
                preflight_fail(
                    "pc8_registry",
                    f"authority#/registry/{population}[{index}]",
                    "unbound record",
                )

    pc7_registry_raw = read_exact(
        authority_root / PC7_REGISTRY_PATH,
        PC7_REGISTRY_BYTES,
        PC7_REGISTRY_SHA256,
        "pc7_registry",
    )
    manifest_raw = read_exact(
        authority_root / MANIFEST_PATH,
        MANIFEST_BYTES,
        MANIFEST_SHA256,
        "pc8_manifest",
    )
    read_exact(
        authority_root / PC7_MANIFEST_PATH,
        PC7_MANIFEST_BYTES,
        PC7_MANIFEST_SHA256,
        "pc7_manifest",
    )
    read_exact(
        PC7_PUBLICATION_REPORT,
        PC7_PUBLICATION_BYTES,
        PC7_PUBLICATION_SHA256,
        "pc7_publication_evidence",
    )
    return registry, manifest_raw, pc7_registry_raw


def json_category(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return "invalid"


class SchemaRuntime:
    def __init__(self, manifest: dict[str, Any]) -> None:
        self.manifest = manifest
        rows = manifest.get("schemas")
        if not isinstance(rows, list):
            fail("PC8_SCHEMA_BOOTSTRAP_INVALID", "$.schemas", "schemas must be array")
        self.schemas: dict[str, dict[str, Any]] = {}
        for index, row in enumerate(rows):
            if not isinstance(row, dict) or not isinstance(row.get("id"), str):
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"$.schemas[{index}]", "bad row")
            if row["id"] in self.schemas:
                fail("PC8_SCHEMA_DUPLICATE", f"$.schemas[{index}].id", row["id"])
            self.schemas[row["id"]] = row
        self.ref_hits: set[str] = set()
        for schema_id, row in self.schemas.items():
            self._bootstrap_row(row, f"$.schemas[{schema_id}]")
        self.schema_closure = self._validate_static_schema_graph()

    def _validate_static_schema_graph(self) -> dict[str, Any]:
        edges: list[dict[str, str]] = []
        census: dict[str, int] = {
            "array": 0,
            "const": 0,
            "enum": 0,
            "nullable": 0,
            "object": 0,
            "primitive": 0,
            "ref": 0,
            "union": 0,
        }
        union_dispatch = {
            "json_category": 0,
            "structural_exactly_one": 0,
            "tagged_member": 0,
        }

        def walk(node: dict[str, Any], source: str, path: str) -> None:
            kind = node["kind"]
            census[kind] += 1
            if kind == "ref":
                target = node["schema"]
                edges.append({"source": source, "target": target, "locator": path})
                return
            if kind == "object":
                for name in utf8_sorted(list(node["members"])):
                    walk(node["members"][name], source, f"{path}.members.{name}")
                return
            if kind == "array":
                if node["items"] is not None:
                    walk(node["items"], source, f"{path}.items")
                return
            if kind == "nullable":
                walk(node["value_schema"], source, f"{path}.value_schema")
                return
            if kind != "union":
                return
            dispatch = node["dispatch"]
            union_dispatch[dispatch] += 1
            if dispatch == "tagged_member":
                for tag in utf8_sorted(list(node["mapping"])):
                    walk(node["mapping"][tag], source, f"{path}.mapping.{tag}")
            elif dispatch == "json_category":
                for index, variant in enumerate(node["variants"]):
                    walk(variant["schema"], source, f"{path}.variants[{index}].schema")
            else:
                for index, variant in enumerate(node["variants"]):
                    walk(variant, source, f"{path}.variants[{index}]")

        for schema_id in utf8_sorted(list(self.schemas)):
            walk(self.root_node(schema_id), schema_id, f"{schema_id}$")

        non_bootstrap = [
            edge for edge in edges if not edge["target"].startswith("@BOOTSTRAP-")
        ]
        missing = {
            edge["target"] for edge in non_bootstrap if edge["target"] not in self.schemas
        }
        if missing:
            fail(
                "PC8_SCHEMA_REFERENCE_INVALID",
                "$.schemas",
                f"missing targets {utf8_sorted(list(missing))}",
            )
        graph = {schema_id: set() for schema_id in self.schemas}
        for edge in non_bootstrap:
            graph[edge["source"]].add(edge["target"])
        active: list[str] = []
        complete: set[str] = set()

        def visit(schema_id: str) -> None:
            if schema_id in active:
                cycle = active[active.index(schema_id) :] + [schema_id]
                fail(
                    "PC8_SCHEMA_REFERENCE_CYCLE",
                    f"schema:{schema_id}",
                    " -> ".join(cycle),
                )
            if schema_id in complete:
                return
            active.append(schema_id)
            for target in utf8_sorted(list(graph[schema_id])):
                visit(target)
            active.pop()
            complete.add(schema_id)

        for schema_id in utf8_sorted(list(self.schemas)):
            visit(schema_id)

        declared = self.manifest["self_validation"]["recursive_schema_node_census"]
        observed_census = {
            "schema_rows": len(self.schemas),
            "total_nodes": sum(census.values()),
            "by_kind": census,
            "union_dispatch": union_dispatch,
        }
        for key in ("schema_rows", "total_nodes", "by_kind", "union_dispatch"):
            if declared.get(key) != observed_census[key]:
                fail(
                    "PC8_SCHEMA_CENSUS_MISMATCH",
                    f"$.self_validation.recursive_schema_node_census.{key}",
                    f"{observed_census[key]} != {declared.get(key)}",
                )
        if len(edges) != census["ref"]:
            fail("PC8_SCHEMA_REFERENCE_INVALID", "$.schemas", "reference census mismatch")
        return {
            **observed_census,
            "reference_edge_count": len(edges),
            "non_bootstrap_reference_edge_count": len(non_bootstrap),
            "reference_edges": edges,
            "reference_targets": utf8_sorted(
                list({edge["target"] for edge in non_bootstrap})
            ),
            "acyclic": True,
        }

    def _strings(self, value: Any, path: str, minimum: int = 0) -> list[str]:
        if not isinstance(value, list) or len(value) < minimum:
            fail("PC8_SCHEMA_BOOTSTRAP_INVALID", path, "expected string array")
        if any(not isinstance(item, str) for item in value):
            fail("PC8_SCHEMA_BOOTSTRAP_INVALID", path, "non-string array item")
        if len(set(value)) != len(value):
            fail("PC8_SCHEMA_BOOTSTRAP_INVALID", path, "duplicate array item")
        return value

    def _bootstrap_row(self, row: dict[str, Any], path: str) -> None:
        expect_exact_keys(row, {"id", "consumer", "admission_rule"}, set(), path)
        if not isinstance(row["consumer"], str):
            fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.consumer", "not string")
        self._bootstrap_node(row["admission_rule"], f"{path}.admission_rule")

    def _bootstrap_node(self, node: Any, path: str) -> None:
        if not isinstance(node, dict) or not isinstance(node.get("kind"), str):
            fail("PC8_SCHEMA_BOOTSTRAP_INVALID", path, "node must have string kind")
        kind = node["kind"]
        if kind == "primitive":
            expect_exact_keys(node, {"kind", "category"}, set(), path)
            if node["category"] not in {"null", "boolean", "integer", "string", "array", "object"}:
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.category", "unknown category")
        elif kind == "const":
            expect_exact_keys(node, {"kind", "value"}, set(), path)
        elif kind == "enum":
            expect_exact_keys(node, {"kind", "values"}, set(), path)
            values = node["values"]
            if not isinstance(values, list) or not values:
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.values", "empty enum")
            if len({canonical_bytes(value) for value in values}) != len(values):
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.values", "duplicate enum")
        elif kind == "object":
            expect_exact_keys(
                node,
                {
                    "kind",
                    "required_members",
                    "optional_members",
                    "additional_members",
                    "members",
                    "cross_field_constraints",
                },
                set(),
                path,
            )
            required = self._strings(node["required_members"], f"{path}.required_members")
            optional = self._strings(node["optional_members"], f"{path}.optional_members")
            if set(required) & set(optional):
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", path, "required/optional overlap")
            if node["additional_members"] != "reject":
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.additional_members", "must reject")
            members = node["members"]
            if not isinstance(members, dict) or set(members) != set(required) | set(optional):
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.members", "member closure")
            for name, child in members.items():
                self._bootstrap_node(child, f"{path}.members.{name}")
            constraints = node["cross_field_constraints"]
            if not isinstance(constraints, list):
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.cross_field_constraints", "not array")
            for index, constraint in enumerate(constraints):
                expect_exact_keys(
                    constraint,
                    {"operator", "array_member", "integer_member"},
                    set(),
                    f"{path}.cross_field_constraints[{index}]",
                )
                if constraint["operator"] != "array_length_equals_integer_member":
                    fail("PC8_SCHEMA_BOOTSTRAP_INVALID", path, "unknown cross-field operator")
                if constraint["array_member"] not in members or constraint["integer_member"] not in members:
                    fail("PC8_SCHEMA_BOOTSTRAP_INVALID", path, "undeclared operand")
        elif kind == "array":
            expect_exact_keys(
                node,
                {"kind", "min_items", "max_items", "unique_items", "items"},
                set(),
                path,
            )
            minimum = node["min_items"]
            maximum = node["max_items"]
            if isinstance(minimum, bool) or not isinstance(minimum, int) or minimum < 0:
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.min_items", "bad bound")
            if maximum is not None and (
                isinstance(maximum, bool) or not isinstance(maximum, int) or maximum < minimum
            ):
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.max_items", "bad bound")
            if not isinstance(node["unique_items"], bool):
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.unique_items", "not boolean")
            if node["items"] is None:
                if maximum != 0:
                    fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.items", "null item schema")
            else:
                self._bootstrap_node(node["items"], f"{path}.items")
        elif kind == "ref":
            expect_exact_keys(node, {"kind", "schema"}, set(), path)
            target = node["schema"]
            if target not in self.schemas and target not in {
                "@BOOTSTRAP-SCHEMA-ROW",
                "@BOOTSTRAP-NODE",
            }:
                fail("PC8_SCHEMA_REFERENCE_INVALID", f"{path}.schema", str(target))
        elif kind == "nullable":
            expect_exact_keys(node, {"kind", "value_schema"}, set(), path)
            self._bootstrap_node(node["value_schema"], f"{path}.value_schema")
        elif kind == "union":
            dispatch = node.get("dispatch")
            if dispatch == "json_category":
                expect_exact_keys(node, {"kind", "dispatch", "variants"}, set(), path)
                variants = node["variants"]
                if not isinstance(variants, list) or not variants:
                    fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.variants", "empty")
                categories: list[str] = []
                for index, variant in enumerate(variants):
                    expect_exact_keys(
                        variant,
                        {"category", "schema"},
                        set(),
                        f"{path}.variants[{index}]",
                    )
                    categories.append(variant["category"])
                    self._bootstrap_node(variant["schema"], f"{path}.variants[{index}].schema")
                if len(set(categories)) != len(categories):
                    fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.variants", "category duplicate")
            elif dispatch == "tagged_member":
                expect_exact_keys(
                    node, {"kind", "dispatch", "tag_member", "mapping"}, set(), path
                )
                if not isinstance(node["tag_member"], str) or not isinstance(node["mapping"], dict) or not node["mapping"]:
                    fail("PC8_SCHEMA_BOOTSTRAP_INVALID", path, "bad tagged union")
                for tag, child in node["mapping"].items():
                    self._bootstrap_node(child, f"{path}.mapping.{tag}")
            elif dispatch == "structural_exactly_one":
                expect_exact_keys(node, {"kind", "dispatch", "variants"}, set(), path)
                variants = node["variants"]
                if not isinstance(variants, list) or len(variants) < 2:
                    fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.variants", "need two")
                for index, child in enumerate(variants):
                    self._bootstrap_node(child, f"{path}.variants[{index}]")
            else:
                fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.dispatch", "unknown union")
        else:
            fail("PC8_SCHEMA_BOOTSTRAP_INVALID", f"{path}.kind", f"unknown {kind}")

    def root_node(self, schema_id: str) -> dict[str, Any]:
        try:
            return self.schemas[schema_id]["admission_rule"]
        except KeyError:
            fail("PC8_SCHEMA_REFERENCE_INVALID", schema_id, "unknown schema")

    def deref(self, node: dict[str, Any]) -> dict[str, Any]:
        seen: set[str] = set()
        while node.get("kind") == "ref":
            target = node["schema"]
            if target.startswith("@"):
                return node
            if target in seen:
                fail("PC8_SCHEMA_REFERENCE_CYCLE", target, "cycle")
            seen.add(target)
            node = self.root_node(target)
        return node

    def member_node(self, schema_id: str, chain: list[str]) -> dict[str, Any]:
        node = self.root_node(schema_id)
        for name in chain:
            node = self.deref(node)
            if name == "items":
                if node.get("kind") != "array" or node["items"] is None:
                    fail("PC8_SCHEMA_LOCATOR_INVALID", schema_id, f"no items at {name}")
                node = node["items"]
            else:
                if node.get("kind") != "object" or name not in node["members"]:
                    fail("PC8_SCHEMA_LOCATOR_INVALID", schema_id, f"no member {name}")
                node = node["members"][name]
        return node

    def validate(
        self,
        schema_id: str,
        value: Any,
        *,
        schema_path: str | None = None,
        disabled: set[str] | None = None,
    ) -> None:
        self._admit(
            self.root_node(schema_id),
            value,
            schema_path or f"{schema_id}$",
            "$",
            [],
            disabled or set(),
        )

    def validate_node(
        self,
        node: dict[str, Any],
        value: Any,
        schema_path: str,
        disabled: set[str] | None = None,
    ) -> None:
        self._admit(node, value, schema_path, "$", [], disabled or set())

    def _reject(
        self,
        schema_path: str,
        value_path: str,
        reason: str,
        disabled: set[str],
    ) -> None:
        if schema_path not in disabled:
            raise AdmissionError(schema_path, value_path, reason)

    def _admit(
        self,
        node: dict[str, Any],
        value: Any,
        schema_path: str,
        value_path: str,
        ref_stack: list[str],
        disabled: set[str],
    ) -> None:
        kind = node["kind"]
        if kind == "primitive":
            if json_category(value) != node["category"]:
                self._reject(schema_path, value_path, "primitive category", disabled)
        elif kind == "const":
            if not exact_equal(value, node["value"]):
                self._reject(schema_path, value_path, "constant mismatch", disabled)
        elif kind == "enum":
            if not any(exact_equal(value, candidate) for candidate in node["values"]):
                self._reject(schema_path, value_path, "enum mismatch", disabled)
        elif kind == "object":
            if not isinstance(value, dict):
                self._reject(schema_path, value_path, "object required", disabled)
                return
            required = set(node["required_members"])
            optional = set(node["optional_members"])
            missing = required - set(value)
            if missing:
                self._reject(
                    f"{schema_path}.required_members",
                    value_path,
                    f"missing {utf8_sorted(list(missing))}",
                    disabled,
                )
            unknown = set(value) - required - optional
            if unknown:
                self._reject(
                    f"{schema_path}.additional_members",
                    value_path,
                    f"unknown {utf8_sorted(list(unknown))}",
                    disabled,
                )
            for name in utf8_sorted(list(set(value) & (required | optional))):
                child_path = f"{schema_path}.members.{name}"
                if name in optional:
                    child_path = f"{schema_path}.optional_members.{name}"
                self._admit(
                    node["members"][name],
                    value[name],
                    child_path,
                    f"{value_path}.{name}",
                    ref_stack,
                    disabled,
                )
            for index, constraint in enumerate(node["cross_field_constraints"]):
                locus = f"{schema_path}.cross_field_constraints[{index}]"
                array_value = value.get(constraint["array_member"])
                integer_value = value.get(constraint["integer_member"])
                if (
                    not isinstance(array_value, list)
                    or isinstance(integer_value, bool)
                    or not isinstance(integer_value, int)
                    or len(array_value) != integer_value
                ):
                    self._reject(locus, value_path, "cross-field mismatch", disabled)
        elif kind == "array":
            if not isinstance(value, list):
                self._reject(schema_path, value_path, "array required", disabled)
                return
            minimum = node["min_items"]
            maximum = node["max_items"]
            if len(value) < minimum or (maximum is not None and len(value) > maximum):
                self._reject(schema_path, value_path, "array length", disabled)
            if node["unique_items"] and len({canonical_bytes(item) for item in value}) != len(value):
                self._reject(schema_path, value_path, "array uniqueness", disabled)
            if node["items"] is not None:
                for index, child in enumerate(value):
                    self._admit(
                        node["items"],
                        child,
                        f"{schema_path}.items",
                        f"{value_path}[{index}]",
                        ref_stack,
                        disabled,
                    )
        elif kind == "ref":
            target = node["schema"]
            if target == "@BOOTSTRAP-SCHEMA-ROW":
                try:
                    self._bootstrap_row(value, value_path)
                except PlanError as error:
                    self._reject(schema_path, value_path, str(error), disabled)
                return
            if target == "@BOOTSTRAP-NODE":
                try:
                    self._bootstrap_node(value, value_path)
                except PlanError as error:
                    self._reject(schema_path, value_path, str(error), disabled)
                return
            locus = f"{schema_path}->{target}"
            if locus in disabled:
                return
            if target in ref_stack:
                self._reject(locus, value_path, "reference cycle", disabled)
                return
            self.ref_hits.add(target)
            try:
                self._admit(
                    self.root_node(target),
                    value,
                    locus,
                    value_path,
                    [*ref_stack, target],
                    disabled,
                )
            except AdmissionError as error:
                self._reject(locus, value_path, f"child rejected: {error.reason}", disabled)
        elif kind == "nullable":
            if value is not None:
                self._admit(
                    node["value_schema"],
                    value,
                    schema_path,
                    value_path,
                    ref_stack,
                    disabled,
                )
        elif kind == "union":
            dispatch = node["dispatch"]
            if dispatch == "json_category":
                matches = [
                    variant
                    for variant in node["variants"]
                    if variant["category"] == json_category(value)
                ]
                if len(matches) != 1:
                    self._reject(schema_path, value_path, "category dispatch", disabled)
                    return
                self._admit(
                    matches[0]["schema"],
                    value,
                    schema_path,
                    value_path,
                    ref_stack,
                    disabled,
                )
            elif dispatch == "tagged_member":
                tag_member = node["tag_member"]
                if not isinstance(value, dict) or not isinstance(value.get(tag_member), str):
                    self._reject(schema_path, value_path, "tag missing", disabled)
                    return
                tag = value[tag_member]
                if tag not in node["mapping"]:
                    self._reject(schema_path, value_path, "tag unknown", disabled)
                    return
                self._admit(
                    node["mapping"][tag],
                    value,
                    schema_path,
                    value_path,
                    ref_stack,
                    disabled,
                )
            else:
                admitted = 0
                for variant in node["variants"]:
                    try:
                        self._admit(
                            variant,
                            value,
                            schema_path,
                            value_path,
                            ref_stack,
                            set(),
                        )
                        admitted += 1
                    except AdmissionError:
                        pass
                if admitted != 1:
                    self._reject(
                        schema_path,
                        value_path,
                        f"structural union admitted {admitted}",
                        disabled,
                    )
        else:
            self._reject(schema_path, value_path, f"unknown node {kind}", disabled)


def collect_ids(rows: list[dict[str, Any]], label: str) -> list[str]:
    ids: list[str] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict) or not isinstance(row.get("id"), str):
            fail("PC8_POPULATION_INVALID", f"$.{label}[{index}]", "missing ID")
        ids.append(row["id"])
    if len(ids) != len(set(ids)):
        fail("PC8_POPULATION_DUPLICATE", f"$.{label}", "duplicate ID")
    if ids != utf8_sorted(ids):
        fail("PC8_POPULATION_ORDER", f"$.{label}", "IDs not byte sorted")
    return ids


def validate_populations(manifest: dict[str, Any]) -> dict[str, int]:
    if manifest.get("candidate_status") != EXPECTED_CANDIDATE_STATUS:
        fail("PC8_CANDIDATE_STATUS_INVALID", "$.candidate_status", "historical status drift")
    actual_ids = {
        "authority": [row["id"] for row in manifest["authority"]["documents"]],
        "rule_provenance": collect_ids(manifest["rule_provenance"], "rule_provenance"),
        "schemas": collect_ids(manifest["schemas"], "schemas"),
        "normative_choices": collect_ids(manifest["normative_choices"], "normative_choices"),
        "resolved_sources": collect_ids(manifest["resolved_sources"], "resolved_sources"),
        "fixtures": collect_ids(manifest["fixtures"], "fixtures"),
        "relations": collect_ids(manifest["relations"], "relations"),
        "discriminators": collect_ids(manifest["discriminators"], "discriminators"),
        "preimage_registry": collect_ids(manifest["preimage_registry"], "preimage_registry"),
        "future_only": collect_ids(manifest["future_only"], "future_only"),
        "schema_mutations": utf8_sorted(
            [
                row["id"]
                for row in manifest["discriminators"]
                if row["criterion_kind"] == "schema_mutation"
            ]
        ),
    }
    rows = manifest["populations"]
    if not isinstance(rows, list) or len(rows) != len(EXPECTED_POPULATIONS):
        fail("PC8_POPULATION_INVALID", "$.populations", "population row count")
    population_rows = {row["name"]: row for row in rows}
    if set(population_rows) != set(EXPECTED_POPULATIONS):
        fail("PC8_POPULATION_INVALID", "$.populations", "population names")
    for name, expected in EXPECTED_POPULATIONS.items():
        ids = actual_ids[name]
        row = population_rows[name]
        if len(ids) != expected or row["cardinality"] != expected or row["ordered_ids"] != ids:
            fail("PC8_POPULATION_MISMATCH", f"$.populations.{name}", "identity/count mismatch")
    counts = {key: 0 for key in EXPECTED_RULE_COUNTS}
    for row in manifest["rule_provenance"]:
        classification = row["classification"]
        if classification not in counts:
            fail("PC8_RULE_CLASS_INVALID", f"$.rule_provenance.{row['id']}", classification)
        counts[classification] += 1
    if counts != EXPECTED_RULE_COUNTS:
        fail("PC8_RULE_COUNT_MISMATCH", "$.rule_provenance", str(counts))
    spans = sum(len(row["spans"]) for row in manifest["preimage_registry"])
    if spans != EXPECTED_PREIMAGE_SPANS:
        fail("PC8_PREIMAGE_SPAN_COUNT", "$.preimage_registry", str(spans))
    future_ids = set(actual_ids["future_only"])
    if future_ids != EXPECTED_FUTURE_IDS or any(row["dispatchable"] for row in manifest["future_only"]):
        fail("PC8_FUTURE_BOUNDARY_INVALID", "$.future_only", "future set/dispatch")
    return {name: len(ids) for name, ids in actual_ids.items()} | {
        "preimage_spans": spans,
        "rules_S": counts["S"],
        "rules_C": counts["C"],
        "rules_N": counts["N"],
        "rules_D": counts["D"],
    }


def resolve_consumer_expression(manifest: dict[str, Any], expression: str) -> list[Any]:
    if re.fullmatch(
        r"manifest(?:\.[A-Za-z_][A-Za-z0-9_]*)*(?:\[\*\])?",
        expression,
    ) is None:
        fail(
            "PC8_SCHEMA_CONSUMER_EXPRESSION_INVALID",
            expression,
            "unsupported consumer grammar",
        )
    wildcard = expression.endswith("[*]")
    path = expression[:-3] if wildcard else expression
    value: Any = manifest
    for member in path.split(".")[1:]:
        if not isinstance(value, dict) or member not in value:
            fail(
                "PC8_SCHEMA_CONSUMER_EXPRESSION_INVALID",
                expression,
                f"missing member {member}",
            )
        value = value[member]
    if wildcard:
        if not isinstance(value, list):
            fail(
                "PC8_SCHEMA_CONSUMER_EXPRESSION_INVALID",
                expression,
                "wildcard target is not array",
            )
        return value
    return [value]


def validate_references(
    manifest: dict[str, Any], runtime: SchemaRuntime
) -> dict[str, Any]:
    rules = {row["id"] for row in manifest["rule_provenance"]}
    choices = {row["id"] for row in manifest["normative_choices"]}
    sources = {row["id"] for row in manifest["resolved_sources"]}
    fixtures = {row["id"] for row in manifest["fixtures"]}
    relations = {row["id"] for row in manifest["relations"]}
    discriminators = {row["id"] for row in manifest["discriminators"]}
    future = {row["id"] for row in manifest["future_only"]}
    schemas = set(runtime.schemas)

    def subset(values: list[str], allowed: set[str], path: str) -> None:
        if len(values) != len(set(values)) or not set(values) <= allowed:
            fail("PC8_REFERENCE_INVALID", path, str(values))

    for row in manifest["rule_provenance"]:
        ref = row["normative_choice_ref"]
        if ref is not None and ref not in choices:
            fail("PC8_REFERENCE_INVALID", f"rule:{row['id']}", ref)
    for row in manifest["normative_choices"]:
        if row["rule_ref"] not in rules:
            fail("PC8_REFERENCE_INVALID", f"choice:{row['id']}.rule_ref", row["rule_ref"])
        subset(row["discriminator_refs"], discriminators, f"choice:{row['id']}")
    for row in manifest["fixtures"]:
        if row["resolved_source_ref"] not in sources:
            fail("PC8_REFERENCE_INVALID", f"fixture:{row['id']}", row["resolved_source_ref"])
        subset(row["normative_choice_refs"], choices, f"fixture:{row['id']}.choices")
        subset(row["clarification_rule_refs"], rules, f"fixture:{row['id']}.rules")
    if {row["resolved_source_ref"] for row in manifest["fixtures"]} != sources:
        fail("PC8_REFERENCE_UNUSED", "$.resolved_sources", "not exactly fixture-reachable")
    for row in manifest["relations"]:
        subset(row["resolved_source_refs"], sources, f"relation:{row['id']}.sources")
        subset(row["fixture_refs"], fixtures, f"relation:{row['id']}.fixtures")
        if row["resolved_source_refs"] != [
            next(
                fixture["resolved_source_ref"]
                for fixture in manifest["fixtures"]
                if fixture["id"] == fixture_id
            )
            for fixture_id in row["fixture_refs"]
        ]:
            fail("PC8_REFERENCE_INVALID", f"relation:{row['id']}", "source/fixture pairing")
        subset(row["normative_choice_refs"], choices, f"relation:{row['id']}.choices")
        subset(row["clarification_rule_refs"], rules, f"relation:{row['id']}.rules")
    for row in manifest["discriminators"]:
        subset(row["normative_choice_refs"], choices, f"discriminator:{row['id']}.choices")
        subset(row["clarification_rule_refs"], rules, f"discriminator:{row['id']}.rules")
        target = row["target_ref"].split("$", 1)[0]
        if target not in fixtures | relations | future | schemas:
            fail("PC8_REFERENCE_INVALID", f"discriminator:{row['id']}.target", target)
    for row in manifest["preimage_registry"]:
        if row["fixture_ref"] not in fixtures:
            fail("PC8_REFERENCE_INVALID", f"registry:{row['id']}", row["fixture_ref"])
        for span in row["spans"]:
            subset(span["rule_refs"], rules, f"registry:{row['id']}.span")
    for row in manifest["future_only"]:
        subset(row["normative_choice_refs"], choices, f"future:{row['id']}")
    used_choices = {
        ref
        for row in manifest["rule_provenance"]
        for ref in [row["normative_choice_ref"]]
        if ref is not None
    }
    used_choices.update(
        ref
        for population in ("fixtures", "relations", "discriminators", "future_only")
        for row in manifest[population]
        for ref in row["normative_choice_refs"]
    )
    if used_choices != choices:
        fail("PC8_REFERENCE_UNUSED", "$.normative_choices", "reverse closure")
    used_discriminators = {
        ref
        for row in manifest["normative_choices"]
        for ref in row["discriminator_refs"]
    }
    unbound_discriminators = discriminators - used_discriminators
    if any(
        not row["clarification_rule_refs"]
        for row in manifest["discriminators"]
        if row["id"] in unbound_discriminators
    ):
        fail("PC8_REFERENCE_UNUSED", "$.discriminators", "reverse closure")
    consumers = manifest["self_validation"]["schema_consumers"]
    if set(consumers) != schemas:
        fail("PC8_REFERENCE_UNUSED", "$.schemas", "consumer closure")
    schema_rows = {row["id"]: row for row in manifest["schemas"]}
    consumer_values: dict[str, list[Any]] = {}
    consumer_counts: dict[str, int] = {}
    for schema_id in utf8_sorted(list(schemas)):
        declared_expression = schema_rows[schema_id]["consumer"]
        if declared_expression != consumers[schema_id]:
            fail(
                "PC8_SCHEMA_CONSUMER_DECLARATION_MISMATCH",
                f"schema:{schema_id}.consumer",
                f"{declared_expression} != {consumers[schema_id]}",
            )
        values = resolve_consumer_expression(manifest, declared_expression)
        consumer_values[schema_id] = values
        consumer_counts[schema_id] = len(values)
        if not values:
            fail("PC8_REFERENCE_UNUSED", f"$.schemas.{schema_id}", "empty consumer")
        for index, value in enumerate(values):
            runtime.validate(
                schema_id,
                value,
                schema_path=f"{schema_id}$consumer[{index}]",
            )
    declared_admissions = manifest["self_validation"]["recursive_schema_node_census"][
        "declared_consumer_admissions"
    ]
    if sum(consumer_counts.values()) != declared_admissions:
        fail(
            "PC8_SCHEMA_CONSUMER_POPULATION_MISMATCH",
            "$.self_validation.recursive_schema_node_census.declared_consumer_admissions",
            f"{sum(consumer_counts.values())} != {declared_admissions}",
        )
    return runtime.schema_closure | {
        "declared_consumer_expressions": {
            schema_id: schema_rows[schema_id]["consumer"]
            for schema_id in utf8_sorted(list(schemas))
        },
        "resolved_consumer_populations": consumer_counts,
        "declared_consumer_admissions": sum(consumer_counts.values()),
    }


def load_pc7(
    authority_root: Path, registry_bytes: bytes
) -> tuple[Any, dict[str, Any], dict[str, Any]]:
    spec = importlib.util.spec_from_file_location("threadsmith_pc7_generator", PC7_GENERATOR_PATH)
    if spec is None or spec.loader is None:
        fail("PC8_PC7_GENERATOR_LOAD", str(PC7_GENERATOR_PATH), "no loader")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    inputs = module.PC7AuthorityInputsV1(
        authority_root=authority_root,
        registry_path=authority_root / PC7_REGISTRY_PATH,
        registry_bytes=registry_bytes,
    )
    manifest, _, chain_output, _ = module.load_and_validate(inputs)
    expanded = {
        name: module.expand_output(name, value, chain_output)
        for name, value in manifest["successful_outputs"].items()
    }
    return module, manifest, expanded


def pc7_inline_bytes(pc7_manifest: dict[str, Any], locator: str) -> dict[str, str]:
    constant = pc7_manifest["byte_constants"][locator]
    return {"encoding": "lowercase_hex", "hex": constant["hex"]}


def pc7_materialized_record(
    pc7_manifest: dict[str, Any], locator: str
) -> dict[str, Any]:
    if locator not in pc7_manifest["package_records"]:
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", locator, "unsupported package record")
    record = copy.deepcopy(pc7_manifest["package_records"][locator])
    for file in record["verified_files"]:
        reference = file.pop("bytes_ref")
        file["bytes"] = pc7_inline_bytes(pc7_manifest, reference)
    return record


def pc7_materialized_scanned_source(
    pc7_manifest: dict[str, Any], scanned_plan: dict[str, Any]
) -> dict[str, Any]:
    return {
        "active_profile": scanned_plan["active_profile"],
        "blueprint_digest": scanned_plan["blueprint_digest"],
        "defaulted_root": copy.deepcopy(scanned_plan["defaulted_root"]),
        "packages": [
            pc7_materialized_record(pc7_manifest, locator)
            for locator in scanned_plan["package_records"]
        ],
    }


def pc7_materialize_output(
    value: Any,
    input_ref: str,
    pc7_manifest: dict[str, Any],
    scanned_source: dict[str, Any],
) -> Any:
    if isinstance(value, list):
        return [
            pc7_materialize_output(child, input_ref, pc7_manifest, scanned_source)
            for child in value
        ]
    if not isinstance(value, dict):
        return copy.deepcopy(value)
    result = copy.deepcopy(value)
    if "scanned_source_ref" in result:
        if result.pop("scanned_source_ref") != input_ref:
            fail("PC8_SOURCE_CONSTRUCTION_INVALID", input_ref, "scanned source ref")
        result["scanned_source"] = copy.deepcopy(scanned_source)
    if "record_ref" in result:
        result["record"] = pc7_materialized_record(
            pc7_manifest, result.pop("record_ref")
        )
    if "retained_bytes_ref" in result:
        result["retained_bytes"] = pc7_inline_bytes(
            pc7_manifest, result.pop("retained_bytes_ref")
        )
    for member, terminal in (
        ("parsed_module_ref", "parsed_value"),
        ("imports_ref", "imports"),
    ):
        if member in result:
            locator = result.pop(member)
            match = re.fullmatch(rf"module_oracles\.([^.]+)\.{terminal}", locator)
            if match is None:
                fail("PC8_SOURCE_CONSTRUCTION_INVALID", locator, member)
            result[member.removesuffix("_ref")] = copy.deepcopy(
                pc7_manifest["module_oracles"][match.group(1)][terminal]
            )
    if (
        "input_ref" in result
        and "package_decisions" in result
        and "unreferenced_entries" in result
    ):
        locator = result.pop("input_ref")
        if locator is None:
            result["input"] = None
        else:
            bytes_ref = pc7_manifest["lock_inputs"][locator]["bytes_ref"]
            result["input"] = pc7_inline_bytes(pc7_manifest, bytes_ref)
    return {
        key: pc7_materialize_output(child, input_ref, pc7_manifest, scanned_source)
        for key, child in result.items()
    }


def reconstruct_source(
    row: dict[str, Any],
    pc7_manifest: dict[str, Any],
    expanded_outputs: dict[str, Any],
) -> dict[str, Any]:
    construction = row["construction"]
    if construction["authority_path"] != str(PC7_MANIFEST_PATH) or construction["authority_sha256"] != PC7_MANIFEST_SHA256:
        fail("PC8_SOURCE_AUTHORITY_INVALID", f"source:{row['id']}", "PC7 binding")
    method = construction["method"]
    if method == "accepted_pc7_fixture_output_expansion":
        input_id = construction["resolve_input_id"]
        output_id = construction["successful_output_id"]
        output = copy.deepcopy(expanded_outputs[output_id])
        if output.pop("scanned_source_ref") != input_id:
            fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "source ref")
        output["scanned_source"] = copy.deepcopy(
            pc7_manifest["resolve_inputs"][input_id]["scanned_source"]
        )
        return output
    if method == "public_pc2_pc6_plus_pc7_correlated_recipe":
        base_input = construction["base_resolve_input_id"]
        base_output = construction["base_successful_output_id"]
        output = copy.deepcopy(expanded_outputs[base_output])
        if output.pop("scanned_source_ref") != base_input:
            fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "base ref")
        output["scanned_source"] = copy.deepcopy(
            pc7_manifest["resolve_inputs"][base_input]["scanned_source"]
        )
        replacements = construction["exact_root_alias_replacements"]

        def replace_aliases(value: Any) -> Any:
            if isinstance(value, str):
                return replacements.get(value, value)
            if isinstance(value, list):
                return [replace_aliases(child) for child in value]
            if isinstance(value, dict):
                return {key: replace_aliases(child) for key, child in value.items()}
            return value

        output = replace_aliases(output)
        root = output["scanned_source"]["defaulted_root"]
        output["scanned_source"]["blueprint_digest"] = (
            "lattice:blueprint:sha256:" + sha256(canonical_bytes(root))
        )
        return output
    if method != "public_pc2_pc7_root_module_correlated_recipe":
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", method)

    expected_pipeline = [
        {"phase": "PC2", "operation": "parse_blueprint_source"},
        {"phase": "PC3", "operation": "validate_blueprint_source"},
        {"phase": "PC4", "operation": "apply_blueprint_defaults"},
        {"phase": "PC5", "operation": "digest_source"},
        {"phase": "PC6", "operation": "scan_packages"},
        {"phase": "PC7", "operation": "resolve_source"},
    ]
    if construction["public_pipeline"] != expected_pipeline:
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "public pipeline")
    base_input = construction["base_resolve_input_id"]
    base_output = construction["base_successful_output_id"]
    output = copy.deepcopy(expanded_outputs[base_output])
    if output.pop("scanned_source_ref") != base_input:
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "base ref")
    scanned_plan = pc7_manifest["resolve_inputs"][base_input]["scanned_source"]
    output["scanned_source"] = copy.deepcopy(scanned_plan)
    public_output = pc7_materialize_output(
        expanded_outputs[base_output],
        base_input,
        pc7_manifest,
        pc7_materialized_scanned_source(pc7_manifest, scanned_plan),
    )
    before = copy.deepcopy(output)
    change = construction["exact_root_blueprint_change"]
    if change != {
        "json_path": "$.module",
        "from": "root_app",
        "to": "root_alt",
        "changed_member_count": 1,
    }:
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "root change")
    root = output["scanned_source"]["defaulted_root"]
    if root.get("module") != change["from"]:
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "root preimage")
    root["module"] = change["to"]
    root_raw = canonical_bytes(root)
    if (
        root_raw.decode("utf-8") != construction["root_blueprint_source_utf8"]
        or len(root_raw) != construction["root_blueprint_source_bytes"]
        or sha256(root_raw) != construction["root_blueprint_source_sha256"]
    ):
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "root bytes")
    digest = f"lattice:blueprint:sha256:{sha256(root_raw)}"
    if digest != construction["expected_root_blueprint_digest"]:
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "root digest")
    output["scanned_source"]["blueprint_digest"] = digest

    correlated = [
        output["applicable_requirements"][0]["contributor"],
        output["resolution_passes"][0]["active_requirements"][0]["contributor"],
        output["resolution_passes"][1]["active_requirements"][0]["contributor"],
    ]
    for contributor in correlated:
        if contributor != {"kind": "root", "module": change["from"]}:
            fail(
                "PC8_SOURCE_CONSTRUCTION_INVALID",
                f"source:{row['id']}",
                "root contributor preimage",
            )
        contributor["module"] = change["to"]
    graph_node = output["import_graph"]["nodes"][0]
    if graph_node.get("module") != change["from"]:
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{row['id']}", "graph preimage")
    graph_node["module"] = change["to"]
    public_root = public_output["scanned_source"]["defaulted_root"]
    if public_root.get("module") != change["from"]:
        fail(
            "PC8_SOURCE_CONSTRUCTION_INVALID",
            f"source:{row['id']}",
            "public root preimage",
        )
    public_root["module"] = change["to"]
    public_output["scanned_source"]["blueprint_digest"] = digest
    public_correlated = [
        public_output["applicable_requirements"][0]["contributor"],
        public_output["resolution_passes"][0]["active_requirements"][0]["contributor"],
        public_output["resolution_passes"][1]["active_requirements"][0]["contributor"],
    ]
    for contributor in public_correlated:
        if contributor != {"kind": "root", "module": change["from"]}:
            fail(
                "PC8_SOURCE_CONSTRUCTION_INVALID",
                f"source:{row['id']}",
                "public contributor preimage",
            )
        contributor["module"] = change["to"]
    public_graph_node = public_output["import_graph"]["nodes"][0]
    if public_graph_node.get("module") != change["from"]:
        fail(
            "PC8_SOURCE_CONSTRUCTION_INVALID",
            f"source:{row['id']}",
            "public graph preimage",
        )
    public_graph_node["module"] = change["to"]
    difference_paths = json_difference_paths(before, output)
    if difference_paths != construction["exact_resolved_source_difference_paths"]:
        fail(
            "PC8_SOURCE_CONSTRUCTION_INVALID",
            f"source:{row['id']}",
            f"correlated paths {difference_paths}",
        )
    criteria_raw = canonical_bytes(output)
    if (
        len(criteria_raw) != construction["criteria_form_canonical_bytes"]
        or sha256(criteria_raw) != construction["criteria_form_canonical_sha256"]
    ):
        fail(
            "PC8_SOURCE_CONSTRUCTION_INVALID",
            f"source:{row['id']}",
            "criteria-form identity",
        )
    public_raw = canonical_bytes(public_output)
    if (
        len(public_raw) != construction["public_expanded_canonical_bytes"]
        or sha256(public_raw) != construction["public_expanded_canonical_sha256"]
    ):
        fail(
            "PC8_SOURCE_CONSTRUCTION_INVALID",
            f"source:{row['id']}",
            (
                "public-expanded identity "
                f"{len(public_raw)}/{sha256(public_raw)}"
            ),
        )
    preserved = construction["preserved_projection"]
    if (
        output["active_profile"] != preserved["active_profile"]
        or output["authority"] != preserved["authority"]
        or output["created_artifacts"] != preserved["created_artifacts"]
        or output["created_identities"] != preserved["created_identities"]
        or output["phase_status"] != preserved["phase_status"]
        or output["existing_lock"]["input_ref"] != preserved["existing_lock_input_ref"]
        or output["selected_packages"][0]["name"] != preserved["selected_package_name"]
        or output["selected_packages"][0]["version"] != preserved["selected_package_version"]
        or output["selected_packages"][0]["package_id"] != preserved["selected_package_id"]
        or output["applicable_requirements"][0]["constraint"]
        != preserved["requested_by_requirement"]
    ):
        fail(
            "PC8_SOURCE_CONSTRUCTION_INVALID",
            f"source:{row['id']}",
            "preserved projection",
        )
    return output


def requested_by_for(source: dict[str, Any], package: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for requirement in source["applicable_requirements"]:
        if requirement["package"] != package:
            continue
        contributor = requirement["contributor"]
        if contributor["kind"] == "root":
            module = contributor["module"]
        elif contributor["kind"] == "package":
            module = contributor["package"]
        else:
            fail("PC8_LOCK_PROJECTION_INVALID", "$.contributor.kind", contributor["kind"])
        result.append({"module": module, "requirement": requirement["constraint"]})
    return sorted(
        result,
        key=lambda row: (
            row["module"].encode("utf-8"),
            row["requirement"].encode("utf-8"),
        ),
    )


def recompute_expected(source_id: str, source: dict[str, Any]) -> dict[str, Any]:
    packages = []
    for selected in sorted(
        source["selected_packages"], key=lambda row: row["name"].encode("utf-8")
    ):
        packages.append(
            {
                "name": selected["name"],
                "version": selected["version"],
                "package_id": selected["package_id"],
                "requested_by": requested_by_for(source, selected["name"]),
            }
        )
    preimage = {
        "lock_version": 1,
        "lattice": "0.3",
        "profile": source["active_profile"],
        "root_blueprint_digest": source["scanned_source"]["blueprint_digest"],
        "packages": packages,
    }
    preimage_raw = canonical_bytes(preimage)
    preimage_digest = sha256(preimage_raw)
    lock_id = f"lattice:lock:sha256:{preimage_digest}"
    lockfile = copy.deepcopy(preimage)
    lockfile["lock_id"] = lock_id
    emitted_raw = canonical_bytes(lockfile)
    return {
        "identity_preimage_value": preimage,
        "identity_preimage_utf8": preimage_raw.decode("utf-8"),
        "identity_preimage_hex": preimage_raw.hex(),
        "identity_preimage_bytes": len(preimage_raw),
        "identity_preimage_sha256": preimage_digest,
        "lock_id": lock_id,
        "lockfile_value": lockfile,
        "emitted_lockfile_utf8": emitted_raw.decode("utf-8"),
        "emitted_lockfile_hex": emitted_raw.hex(),
        "emitted_lockfile_bytes": len(emitted_raw),
        "emitted_lockfile_sha256": sha256(emitted_raw),
        "emitted_format": {
            "utf8": True,
            "bom": False,
            "insignificant_whitespace": False,
            "trailing_newline": False,
        },
        "locked_source": {
            "resolved_source": {
                "binding": "closed_authenticated_construction",
                "source_ref": source_id,
                "expansion": f"resolved_sources[id={source_id}].expected_value",
                "required_member_count": 12,
                "authority_path": str(PC7_MANIFEST_PATH),
                "authority_sha256": PC7_MANIFEST_SHA256,
            },
            "lockfile": lockfile,
            "canonical_lockfile_bytes_hex": emitted_raw.hex(),
            "lock_id": lock_id,
            "created_identities": [lock_id],
            "created_artifacts": ["canonical_lockfile"],
            "authority": "none",
            "phase_status": "non_authoritative_locked_source",
            "wrapper_identity": None,
        },
        "pc7_existing_lock_roundtrip": {
            "same_source_context": True,
            "source_intake": "admitted",
            "closed_schema": "admitted",
            "lock_id_verification": "admitted",
            "context": "admitted",
        },
    }


def validate_roundtrip(expected: dict[str, Any], source: dict[str, Any]) -> None:
    lockfile = expected["lockfile_value"]
    if set(lockfile) != {
        "lock_version",
        "lattice",
        "profile",
        "root_blueprint_digest",
        "packages",
        "lock_id",
    }:
        fail("PC8_PC7_ROUNDTRIP_INVALID", "$.lockfile", "closed members")
    if (
        lockfile["lock_version"] != 1
        or lockfile["lattice"] != "0.3"
        or lockfile["profile"] != source["active_profile"]
        or lockfile["root_blueprint_digest"] != source["scanned_source"]["blueprint_digest"]
    ):
        fail("PC8_PC7_ROUNDTRIP_INVALID", "$.lockfile", "context")
    without_id = {key: value for key, value in lockfile.items() if key != "lock_id"}
    actual = "lattice:lock:sha256:" + sha256(canonical_bytes(without_id))
    if actual != lockfile["lock_id"]:
        fail("PC8_PC7_ROUNDTRIP_INVALID", "$.lock_id", "identity")
    if canonical_bytes(lockfile).hex() != expected["emitted_lockfile_hex"]:
        fail("PC8_PC7_ROUNDTRIP_INVALID", "$.lockfile", "bytes")


def all_equal(values: list[Any]) -> bool | None:
    if len(values) < 2:
        return None
    first = canonical_bytes(values[0])
    return all(canonical_bytes(value) == first for value in values[1:])


def requested_projection(expected: dict[str, Any]) -> list[Any]:
    return [
        row["requested_by"]
        for row in expected["identity_preimage_value"]["packages"]
    ]


def json_difference_paths(left: Any, right: Any, path: str = "$") -> list[str]:
    if type(left) is not type(right):
        return [path]
    if isinstance(left, dict):
        result: list[str] = []
        for key in utf8_sorted(list(set(left) | set(right))):
            child_path = f"{path}.{key}"
            if key not in left or key not in right:
                result.append(child_path)
            else:
                result.extend(json_difference_paths(left[key], right[key], child_path))
        return result
    if isinstance(left, list):
        result = [f"{path}.length"] if len(left) != len(right) else []
        for index, (left_child, right_child) in enumerate(zip(left, right)):
            result.extend(
                json_difference_paths(
                    left_child,
                    right_child,
                    f"{path}[{index}]",
                )
            )
        return result
    return [] if exact_equal(left, right) else [path]


def validate_single_source_relation(
    relation_id: str,
    fixture_ids: list[str],
    source_values: list[dict[str, Any]],
    expected_values: list[dict[str, Any]],
) -> None:
    if relation_id == "REL-AMBIENT-INDEPENDENCE":
        first = recompute_expected(fixture_ids[0].replace("FIX-", "RS-"), source_values[0])
        second = recompute_expected(fixture_ids[0].replace("FIX-", "RS-"), copy.deepcopy(source_values[0]))
        if not exact_equal(first, second):
            fail("PC8_RELATION_CRITERION_FAILED", relation_id, "ambient recomputation")
    elif relation_id == "REL-PC7-ROUNDTRIP":
        for expected, source in zip(expected_values, source_values):
            validate_roundtrip(expected, source)
    elif relation_id == "REL-PERSISTENCE-BOUNDARY":
        locked = expected_values[0]["locked_source"]
        if (
            locked["authority"] != "none"
            or locked["phase_status"] != "non_authoritative_locked_source"
            or locked["created_artifacts"] != ["canonical_lockfile"]
            or any("persist" in key for key in locked)
        ):
            fail("PC8_RELATION_CRITERION_FAILED", relation_id, "persistence boundary")
    elif relation_id == "REL-PREIMAGE-MEMBER-OMISSION":
        expected = expected_values[0]
        preimage = expected["identity_preimage_value"]
        lockfile = expected["lockfile_value"]
        if (
            set(preimage)
            != {
                "lock_version",
                "lattice",
                "profile",
                "root_blueprint_digest",
                "packages",
            }
            or set(lockfile) != set(preimage) | {"lock_id"}
            or {key: value for key, value in lockfile.items() if key != "lock_id"} != preimage
        ):
            fail("PC8_RELATION_CRITERION_FAILED", relation_id, "preimage omission")
    elif relation_id == "REL-PREIMAGE-VERSUS-EMITTED":
        expected = expected_values[0]
        if (
            expected["identity_preimage_hex"] == expected["emitted_lockfile_hex"]
            or expected["identity_preimage_sha256"] == expected["emitted_lockfile_sha256"]
            or "lock_id" in expected["identity_preimage_value"]
            or "lock_id" not in expected["lockfile_value"]
        ):
            fail("PC8_RELATION_CRITERION_FAILED", relation_id, "byte domains")
    elif relation_id == "REL-PRESENTATION-PERMUTATION":
        permuted = copy.deepcopy(source_values[0])
        permuted["selected_packages"].reverse()
        permuted["applicable_requirements"].reverse()
        source_id = fixture_ids[0].replace("FIX-", "RS-")
        if not exact_equal(recompute_expected(source_id, permuted), expected_values[0]):
            fail("PC8_RELATION_CRITERION_FAILED", relation_id, "presentation order")
    elif relation_id == "REL-REQUESTED-BY-REORDER":
        source = source_values[0]
        lock_packages = {
            row["name"]: row["requested_by"]
            for row in expected_values[0]["lockfile_value"]["packages"]
        }
        unsorted_projection: dict[str, list[dict[str, str]]] = {}
        for selected in source["selected_packages"]:
            rows: list[dict[str, str]] = []
            for requirement in source["applicable_requirements"]:
                if requirement["package"] != selected["name"]:
                    continue
                contributor = requirement["contributor"]
                module = (
                    contributor["module"]
                    if contributor["kind"] == "root"
                    else contributor["package"]
                )
                rows.append(
                    {
                        "module": module,
                        "requirement": requirement["constraint"],
                    }
                )
            unsorted_projection[selected["name"]] = rows
        if (
            all(
                exact_equal(unsorted_projection[name], rows)
                for name, rows in lock_packages.items()
            )
            or any(
                rows
                != sorted(
                    rows,
                    key=lambda item: (
                        item["module"].encode("utf-8"),
                        item["requirement"].encode("utf-8"),
                    ),
                )
                for rows in lock_packages.values()
            )
        ):
            fail("PC8_RELATION_CRITERION_FAILED", relation_id, "requested_by ordering")
    elif relation_id == "REL-RETRACTION-EXCLUSION":
        source = source_values[0]
        passes = source["resolution_passes"]
        retraction_passes = [
            pass_row
            for pass_row in passes
            if isinstance(pass_row["changes"].get("orphan"), dict)
            and pass_row["changes"]["orphan"].get("to") is None
        ]
        if len(retraction_passes) != 1:
            fail("PC8_RELATION_CRITERION_FAILED", relation_id, "retraction pass")
        retraction_pass = retraction_passes[0]
        orphan_inputs = [
            row["package_id"]
            for row in retraction_pass["input_selection"]
            if row["name"] == "orphan"
        ]
        package_names = {row["name"] for row in expected_values[0]["lockfile_value"]["packages"]}
        request_names = {row["package"] for row in source["applicable_requirements"]}
        if (
            len(orphan_inputs) != 1
            or "orphan" in {row["name"] for row in retraction_pass["output_selection"]}
            or retraction_pass["changes"].get("orphan") != {
                "from": orphan_inputs[0] if orphan_inputs else None,
                "to": None,
            }
            or "orphan" in package_names
            or "orphan" in request_names
        ):
            fail("PC8_RELATION_CRITERION_FAILED", relation_id, "retraction exclusion")
    else:
        fail("PC8_RELATION_OPERATION_UNKNOWN", relation_id, "single-source criterion")


def validate_relations(
    manifest: dict[str, Any],
    sources: dict[str, dict[str, Any]],
    expectations: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    fixture_by_id = {row["id"]: row for row in manifest["fixtures"]}
    result: list[dict[str, Any]] = []
    for row in manifest["relations"]:
        if row["kind"] not in RELATION_KINDS:
            fail("PC8_RELATION_OPERATION_UNKNOWN", f"relation:{row['id']}.kind", row["kind"])
        source_values = [sources[source_id] for source_id in row["resolved_source_refs"]]
        expected_values = [
            expectations[fixture_id] for fixture_id in row["fixture_refs"]
        ]
        raw_comparisons = {
            "public_pc7_source_equal": all_equal(source_values),
            "lock_artifact_projection_equal": all_equal(
                [value["lockfile_value"] for value in expected_values]
            ),
            "identity_preimage_equal": all_equal(
                [value["identity_preimage_value"] for value in expected_values]
            ),
            "lock_id_equal": all_equal([value["lock_id"] for value in expected_values]),
            "emitted_bytes_equal": all_equal(
                [value["emitted_lockfile_hex"] for value in expected_values]
            ),
            "complete_locked_source_equal": all_equal(
                [value["locked_source"] for value in expected_values]
            ),
        }
        computed = {
            key: None if row["scope_results"][key] is None else value
            for key, value in raw_comparisons.items()
        }
        if "requested_by_projection_equal" in row["scope_results"]:
            computed["requested_by_projection_equal"] = all_equal(
                [requested_projection(value) for value in expected_values]
            )
        if computed != row["scope_results"]:
            fail(
                "PC8_RELATION_RECOMPUTATION_MISMATCH",
                f"relation:{row['id']}.scope_results",
                f"{computed} != {row['scope_results']}",
            )
        if len(source_values) == 2 and len(expected_values) == 2:
            source_paths = json_difference_paths(source_values[0], source_values[1])
            lock_paths = json_difference_paths(
                expected_values[0]["lockfile_value"],
                expected_values[1]["lockfile_value"],
            )
            if source_paths != row["public_pc7_source_difference_paths"]:
                fail(
                    "PC8_RELATION_RECOMPUTATION_MISMATCH",
                    f"relation:{row['id']}.public_pc7_source_difference_paths",
                    "path set differs",
                )
            if lock_paths != row["lock_artifact_difference_paths"]:
                fail(
                    "PC8_RELATION_RECOMPUTATION_MISMATCH",
                    f"relation:{row['id']}.lock_artifact_difference_paths",
                    "path set differs",
                )
        else:
            if row["public_pc7_source_difference_paths"] or row["lock_artifact_difference_paths"]:
                fail(
                    "PC8_RELATION_RECOMPUTATION_MISMATCH",
                    f"relation:{row['id']}",
                    "unpaired relation claims difference paths",
                )
            validate_single_source_relation(
                row["id"],
                row["fixture_refs"],
                source_values,
                expected_values,
            )
        for fixture_id in row["fixture_refs"]:
            if fixture_id not in fixture_by_id:
                fail("PC8_RELATION_REFERENCE_INVALID", f"relation:{row['id']}", fixture_id)
        result.append(copy.deepcopy(row))
    return result


def validate_preimage_registry(
    manifest: dict[str, Any], expectations: dict[str, dict[str, Any]]
) -> None:
    for row in manifest["preimage_registry"]:
        expected = expectations[row["fixture_ref"]]
        raw = bytes.fromhex(row["preimage_hex"])
        if (
            raw.hex() != row["preimage_hex"]
            or len(raw) != row["preimage_bytes"]
            or raw.hex() != expected["identity_preimage_hex"]
        ):
            fail("PC8_PREIMAGE_REGISTRY_INVALID", f"registry:{row['id']}", "bytes")
        cursor = 0
        for index, span in enumerate(row["spans"]):
            if span["start"] != cursor or span["end"] <= span["start"] or not span["rule_refs"]:
                fail(
                    "PC8_PREIMAGE_REGISTRY_INVALID",
                    f"registry:{row['id']}.spans[{index}]",
                    "gap/overlap/rule",
                )
            cursor = span["end"]
        if cursor != len(raw):
            fail("PC8_PREIMAGE_REGISTRY_INVALID", f"registry:{row['id']}", "coverage end")
        if row["coverage"] != {
            "starts_at_zero": True,
            "ends_at_preimage_length": True,
            "gap_free": True,
            "overlap_free": True,
            "every_span_has_controlling_rule": True,
        }:
            fail("PC8_PREIMAGE_REGISTRY_INVALID", f"registry:{row['id']}", "claims")


def apply_mutation(value: Any, operation: dict[str, Any]) -> Any:
    result = copy.deepcopy(value)
    locator = operation["locator"]
    if locator == "$":
        if operation["operation"] != "replace":
            fail("PC8_SCHEMA_MUTATION_OPERATION", locator, operation["operation"])
        return copy.deepcopy(operation["value"])
    tokens = re.findall(r"\.([A-Za-z0-9_]+)|\[([0-9]+)\]", locator[1:])
    current = result
    for member, index in tokens[:-1]:
        current = current[int(index)] if index else current[member]
    member, index = tokens[-1] if tokens else ("", "")
    key: Any = int(index) if index else member
    if operation["operation"] in {"replace", "add"}:
        current[key] = copy.deepcopy(operation["value"])
    elif operation["operation"] == "remove":
        del current[key]
    else:
        fail("PC8_SCHEMA_MUTATION_OPERATION", locator, operation["operation"])
    return result


def mutation_subject(
    runtime: SchemaRuntime, mutation_id: str
) -> tuple[dict[str, Any], str]:
    mapping: dict[str, tuple[str, list[str], str]] = {
        "DISC-SCHEMA-ARRAY-ITEM-MISMATCH": (
            "SCHEMA-RESOLVED-SOURCE",
            ["expected_value", "selected_packages"],
            "SCHEMA-RESOLVED-SOURCE$.expected_value.selected_packages",
        ),
        "DISC-SCHEMA-CHILD-MISMATCH": (
            "SCHEMA-MANIFEST",
            ["rule_provenance"],
            "SCHEMA-MANIFEST$.members.rule_provenance",
        ),
        "DISC-SCHEMA-CONST-VIOLATION": (
            "@PROJECTED-MANIFEST-VERSION",
            [],
            "SCHEMA-MANIFEST$",
        ),
        "DISC-SCHEMA-CROSS-FIELD": ("SCHEMA-POPULATION", [], "SCHEMA-POPULATION$"),
        "DISC-SCHEMA-ENUM-VIOLATION": ("SCHEMA-RULE", [], "SCHEMA-RULE$"),
        "DISC-SCHEMA-MISSING-REQUIRED": (
            "SCHEMA-CANDIDATE-STATUS",
            [],
            "SCHEMA-CANDIDATE-STATUS$",
        ),
        "DISC-SCHEMA-NULLABLE-MISMATCH": (
            "SCHEMA-RESOLVED-SOURCE",
            ["expected_value", "existing_lock", "input_ref"],
            "SCHEMA-RESOLVED-SOURCE$.expected_value.existing_lock.input_ref",
        ),
        "DISC-SCHEMA-OPTIONAL-ABSENT-MISMATCH": (
            "SCHEMA-CANDIDATE-STATUS",
            [],
            "SCHEMA-CANDIDATE-STATUS$",
        ),
        "DISC-SCHEMA-UNION-VARIANT-MISMATCH": (
            "SCHEMA-RESOLVED-SOURCE",
            ["expected_value", "applicable_requirements", "items", "interval"],
            (
                "SCHEMA-RESOLVED-SOURCE$.admission_rule.members.expected_value."
                "members.applicable_requirements.items.members.interval"
            ),
        ),
        "DISC-SCHEMA-UNKNOWN-MEMBER": (
            "SCHEMA-CANDIDATE-STATUS",
            [],
            "SCHEMA-CANDIDATE-STATUS$",
        ),
        "DISC-SCHEMA-WRONG-BOOLEAN-STRING": (
            "SCHEMA-CANDIDATE-STATUS",
            [],
            "SCHEMA-CANDIDATE-STATUS$",
        ),
        "DISC-SCHEMA-WRONG-OBJECT-CATEGORY": (
            "SCHEMA-CANDIDATE-STATUS",
            [],
            "SCHEMA-CANDIDATE-STATUS$",
        ),
    }
    if mutation_id not in mapping:
        fail("PC8_SCHEMA_MUTATION_UNKNOWN", mutation_id, "not declared")
    schema_id, chain, base = mapping[mutation_id]
    if schema_id == "@PROJECTED-MANIFEST-VERSION":
        manifest_root = runtime.root_node("SCHEMA-MANIFEST")
        return (
            {
                "kind": "object",
                "required_members": ["manifest_version"],
                "optional_members": [],
                "additional_members": "reject",
                "members": {
                    "manifest_version": copy.deepcopy(
                        manifest_root["members"]["manifest_version"]
                    )
                },
                "cross_field_constraints": [],
            },
            base,
        )
    node = runtime.member_node(schema_id, chain) if chain else runtime.root_node(schema_id)
    return node, base


def run_schema_mutations(
    manifest: dict[str, Any], runtime: SchemaRuntime
) -> list[dict[str, Any]]:
    mutations = [
        row
        for row in manifest["discriminators"]
        if row["criterion_kind"] == "schema_mutation"
    ]
    results = []
    for row in mutations:
        if row["expected_result"] != "reject" or row["target_ref"] != row["deterministic_schema_locator"]:
            fail("PC8_SCHEMA_MUTATION_DECLARATION", row["id"], "declaration mismatch")
        node, base = mutation_subject(runtime, row["id"])
        source_value = row["complete_source_value"]
        if row["id"] == "DISC-SCHEMA-NULLABLE-MISMATCH":
            parent = runtime.member_node(
                "SCHEMA-RESOLVED-SOURCE",
                ["expected_value", "existing_lock"],
            )
            runtime.validate_node(
                parent,
                source_value,
                "SCHEMA-RESOLVED-SOURCE$.expected_value.existing_lock",
            )
            source_value = source_value["input_ref"]
        runtime.validate_node(node, source_value, base)
        mutated = apply_mutation(row["complete_source_value"], row["exact_mutation"])
        mutated_value = mutated
        if row["id"] == "DISC-SCHEMA-NULLABLE-MISMATCH":
            mutated_value = mutated_value["input_ref"]
        try:
            runtime.validate_node(node, mutated_value, base)
        except AdmissionError as error:
            expected_failure = EXPECTED_MUTATION_FAILURES.get(row["id"])
            if expected_failure is None or expected_failure not in error.reason:
                fail(
                    "PC8_SCHEMA_MUTATION_REASON_MISMATCH",
                    row["id"],
                    error.reason,
                )
            isolation_locator = row["deterministic_schema_locator"]
            if row["id"] == "DISC-SCHEMA-UNION-VARIANT-MISMATCH":
                isolation_locator = (
                    f"{row['deterministic_schema_locator']}.members.upper_exclusive"
                )
            if error.schema_path != isolation_locator:
                fail(
                    "PC8_SCHEMA_MUTATION_LOCATOR_MISMATCH",
                    row["id"],
                    f"{error.schema_path} != {isolation_locator}",
                )
            runtime.validate_node(
                node,
                mutated_value,
                base,
                {isolation_locator},
            )
            dual_defect_control: dict[str, Any] | None = None
            if row["id"] == "DISC-SCHEMA-UNION-VARIANT-MISMATCH":
                dual = copy.deepcopy(mutated_value)
                dual["lower_inclusive"] = "9.9.9"
                lower_locator = (
                    f"{row['deterministic_schema_locator']}.members.lower_inclusive"
                )
                try:
                    runtime.validate_node(node, dual, base, {isolation_locator})
                except AdmissionError as dual_error:
                    if (
                        dual_error.schema_path != lower_locator
                        or dual_error.reason != "constant mismatch"
                    ):
                        fail(
                            "PC8_SCHEMA_MUTATION_DUAL_CONTROL_MISMATCH",
                            row["id"],
                            (
                                f"{dual_error.schema_path}: {dual_error.reason} != "
                                f"{lower_locator}: constant mismatch"
                            ),
                        )
                    dual_defect_control = {
                        "cooccurring_mutation": {
                            "operation": "replace",
                            "locator": "$.lower_inclusive",
                            "value": "9.9.9",
                        },
                        "disabled_only_locator": isolation_locator,
                        "observed_locator": dual_error.schema_path,
                        "observed_reason": dual_error.reason,
                        "outcome": "REJECTED_BY_REMAINING_LOWER_CONSTANT",
                    }
                else:
                    fail(
                        "PC8_SCHEMA_MUTATION_FALSE_GREEN",
                        row["id"],
                        "dual defect admitted with only upper constant disabled",
                    )
            results.append(
                {
                    "id": row["id"],
                    "declared_locator": row["deterministic_schema_locator"],
                    "declared_reason": row["reason"],
                    "observed_internal_locator": error.schema_path,
                    "observed_internal_reason": error.reason,
                    "isolation_disabled_only_locator": isolation_locator,
                    "rejection": "PASS",
                    "single_mechanism_isolation": "PASS",
                    "dual_defect_control": dual_defect_control,
                }
            )
        else:
            fail("PC8_SCHEMA_MUTATION_FALSE_GREEN", row["id"], "mutation admitted")
    if len(results) != EXPECTED_POPULATIONS["schema_mutations"]:
        fail("PC8_SCHEMA_MUTATION_COUNT", "$.discriminators", str(len(results)))
    return results


def validate_plan(plan: dict[str, Any]) -> None:
    expect_exact_keys(
        plan,
        {
            "fixture_plan_version",
            "authority",
            "criteria",
            "cases",
            "relations",
            "excluded_future_ids",
            "self_validation",
        },
        set(),
        "plan",
    )
    cases = plan["cases"]
    relations = plan["relations"]
    if not isinstance(cases, list) or not isinstance(relations, list):
        fail("PC8_PLAN_SHAPE", "plan", "cases/relations arrays")
    self_validation = expect_exact_keys(
        plan["self_validation"],
        {
            "schema_mutations",
            "rejection_checks",
            "defined_fixture_ids",
            "generated_case_ids",
        },
        set(),
        "plan.self_validation",
    )
    case_ids = [row["fixture_id"] for row in cases]
    if case_ids != utf8_sorted(case_ids) or len(case_ids) != 20 or len(set(case_ids)) != 20:
        fail("PC8_PLAN_POPULATION", "plan.cases", "case closure")
    if any(case_id in EXPECTED_FUTURE_IDS or case_id.startswith("FUT-") for case_id in case_ids):
        fail("PC8_PLAN_FUTURE_DISPATCH", "plan.cases", "future case")
    if (
        case_ids != self_validation["defined_fixture_ids"]
        or case_ids != self_validation["generated_case_ids"]
    ):
        fail("PC8_PLAN_POPULATION", "plan.cases", "defined/generated/executable closure")
    relation_ids = [row["id"] for row in relations]
    if (
        relation_ids != utf8_sorted(relation_ids)
        or len(relation_ids) != 19
        or len(set(relation_ids)) != 19
    ):
        fail("PC8_PLAN_POPULATION", "plan.relations", "relation closure")
    if any(row["kind"] not in RELATION_KINDS for row in relations):
        fail("PC8_PLAN_OPERATION_UNKNOWN", "plan.relations", "unknown relation operation")
    if (
        plan["excluded_future_ids"] != utf8_sorted(list(EXPECTED_FUTURE_IDS))
        or len(plan["excluded_future_ids"]) != 4
    ):
        fail("PC8_PLAN_FUTURE_CLOSURE", "plan.excluded_future_ids", "future closure")


def run_rejection_self_tests(
    manifest: dict[str, Any], runtime: SchemaRuntime, plan: dict[str, Any]
) -> dict[str, str]:
    results: dict[str, str] = {}
    try:
        strict_loads(b'{"member":1,"member":2}', "self-test")
    except PlanError as error:
        if error.code != "PC8_JSON_DUPLICATE_MEMBER":
            raise
        results["duplicate_member"] = "PASS"
    else:
        fail("PC8_SELF_TEST_FALSE_GREEN", "duplicate_member", "admitted")

    unknown = copy.deepcopy(manifest["candidate_status"])
    unknown["unexpected"] = True
    try:
        runtime.validate("SCHEMA-CANDIDATE-STATUS", unknown)
    except AdmissionError:
        results["unknown_member"] = "PASS"
    else:
        fail("PC8_SELF_TEST_FALSE_GREEN", "unknown_member", "admitted")

    unused = copy.deepcopy(manifest)
    unused["fixtures"][0]["resolved_source_ref"] = unused["fixtures"][1][
        "resolved_source_ref"
    ]
    try:
        validate_references(unused, SchemaRuntime(unused))
    except PlanError as error:
        if error.code != "PC8_REFERENCE_UNUSED":
            raise
        results["unused_current_data"] = "PASS"
    else:
        fail("PC8_SELF_TEST_FALSE_GREEN", "unused_current_data", "admitted")

    unknown_operation = copy.deepcopy(plan)
    unknown_operation["relations"][0]["kind"] = "unknown_operation"
    try:
        validate_plan(unknown_operation)
    except PlanError as error:
        if error.code != "PC8_PLAN_OPERATION_UNKNOWN":
            raise
        results["unknown_operation"] = "PASS"
    else:
        fail("PC8_SELF_TEST_FALSE_GREEN", "unknown_operation", "admitted")

    future_dispatch = copy.deepcopy(plan)
    future_dispatch["cases"][0] = (
        {
            "fixture_id": "FUT-NONASCII-PACKAGE-ORDER",
            "resolved_source_id": "FUT-NONASCII-PACKAGE-ORDER",
            "construction": {},
            "resolved_source": {},
            "expected": {},
        }
    )
    future_dispatch["cases"] = sorted(
        future_dispatch["cases"], key=lambda row: row["fixture_id"].encode("utf-8")
    )
    try:
        validate_plan(future_dispatch)
    except PlanError as error:
        if error.code != "PC8_PLAN_FUTURE_DISPATCH":
            raise
        results["future_dispatch"] = "PASS"
    else:
        fail("PC8_SELF_TEST_FALSE_GREEN", "future_dispatch", "admitted")

    wrong_consumer = copy.deepcopy(manifest)
    next(
        row for row in wrong_consumer["schemas"] if row["id"] == "SCHEMA-FIXTURE"
    )["consumer"] = "manifest.relations[*]"
    try:
        wrong_runtime = SchemaRuntime(wrong_consumer)
        validate_references(wrong_consumer, wrong_runtime)
    except PlanError as error:
        if (
            error.code != "PC8_SCHEMA_CONSUMER_DECLARATION_MISMATCH"
            or error.path != "schema:SCHEMA-FIXTURE.consumer"
        ):
            raise
        results["wrong_schema_fixture_consumer"] = "PASS"
    else:
        fail(
            "PC8_SELF_TEST_FALSE_GREEN",
            "wrong_schema_fixture_consumer",
            "admitted",
        )

    dormant_cycle = copy.deepcopy(manifest)
    semantic_schema = next(
        row
        for row in dormant_cycle["schemas"]
        if row["id"] == "SCHEMA-SEMANTIC-CONTRACT"
    )
    original_operation = semantic_schema["admission_rule"]["members"]["operation"]
    semantic_schema["admission_rule"]["members"]["operation"] = {
        "kind": "union",
        "dispatch": "json_category",
        "variants": [
            {"category": "string", "schema": original_operation},
            {
                "category": "null",
                "schema": {
                    "kind": "ref",
                    "schema": "SCHEMA-SEMANTIC-CONTRACT",
                },
            },
        ],
    }
    try:
        SchemaRuntime(dormant_cycle)
    except PlanError as error:
        if (
            error.code != "PC8_SCHEMA_REFERENCE_CYCLE"
            or error.path != "schema:SCHEMA-SEMANTIC-CONTRACT"
        ):
            raise
        results["dormant_schema_self_cycle"] = "PASS"
    else:
        fail("PC8_SELF_TEST_FALSE_GREEN", "dormant_schema_self_cycle", "admitted")
    return results


def generate(
    registry: dict[str, Any],
    manifest: dict[str, Any],
    runtime: SchemaRuntime,
    pc7_manifest: dict[str, Any],
    expanded_outputs: dict[str, Any],
    populations: dict[str, int],
    schema_closure: dict[str, Any],
    mutation_results: list[dict[str, Any]],
) -> dict[str, Any]:
    sources: dict[str, dict[str, Any]] = {}
    source_rows = {row["id"]: row for row in manifest["resolved_sources"]}
    construction_counts = {
        "accepted_pc7_fixture_output_expansion": 0,
        "public_pc2_pc6_plus_pc7_correlated_recipe": 0,
        "public_pc2_pc7_root_module_correlated_recipe": 0,
    }
    for source_id, row in source_rows.items():
        method = row["construction"]["method"]
        if method not in construction_counts:
            fail("PC8_SOURCE_CONSTRUCTION_INVALID", f"source:{source_id}", method)
        construction_counts[method] += 1
        reconstructed = reconstruct_source(row, pc7_manifest, expanded_outputs)
        if not exact_equal(reconstructed, row["expected_value"]):
            fail("PC8_SOURCE_RECOMPUTATION_MISMATCH", f"source:{source_id}", "PC7 expansion")
        sources[source_id] = reconstructed
    if construction_counts != {
        "accepted_pc7_fixture_output_expansion": 18,
        "public_pc2_pc6_plus_pc7_correlated_recipe": 1,
        "public_pc2_pc7_root_module_correlated_recipe": 1,
    }:
        fail("PC8_SOURCE_CONSTRUCTION_INVALID", "$.resolved_sources", str(construction_counts))

    expectations: dict[str, dict[str, Any]] = {}
    cases = []
    for fixture in manifest["fixtures"]:
        source_id = fixture["resolved_source_ref"]
        expected = recompute_expected(source_id, sources[source_id])
        validate_roundtrip(expected, sources[source_id])
        if not exact_equal(expected, fixture["expected"]):
            fail("PC8_LOCK_RECOMPUTATION_MISMATCH", f"fixture:{fixture['id']}", "expected")
        expectations[fixture["id"]] = expected
        cases.append(
            {
                "fixture_id": fixture["id"],
                "resolved_source_id": source_id,
                "construction": copy.deepcopy(source_rows[source_id]["construction"]),
                "resolved_source": copy.deepcopy(sources[source_id]),
                "expected": expected,
            }
        )
    cases.sort(key=lambda row: row["fixture_id"].encode("utf-8"))
    defined = {row["id"] for row in manifest["fixtures"]}
    generated = {row["fixture_id"] for row in cases}
    if defined != generated or len(generated) != len(cases):
        fail("PC8_PLAN_POPULATION", "plan.cases", "defined/generated mismatch")

    relations = validate_relations(manifest, sources, expectations)
    validate_preimage_registry(manifest, expectations)
    criteria = {
        "rule_ids": [row["id"] for row in manifest["rule_provenance"]],
        "schema_ids": [row["id"] for row in manifest["schemas"]],
        "normative_choice_ids": [row["id"] for row in manifest["normative_choices"]],
        "discriminator_ids": [row["id"] for row in manifest["discriminators"]],
        "preimage_registry_ids": [row["id"] for row in manifest["preimage_registry"]],
        "population_closure": populations,
        "schema_closure": schema_closure,
    }
    plan = {
        "fixture_plan_version": "threadsmith-pc8-lock-executable-plan-1",
        "authority": {
            "registry_path": str(REGISTRY_PATH),
            "registry_bytes": REGISTRY_BYTES,
            "registry_sha256": REGISTRY_SHA256,
            "manifest_path": str(MANIFEST_PATH),
            "manifest_bytes": MANIFEST_BYTES,
            "manifest_sha256": MANIFEST_SHA256,
            "pc7_registry_path": str(PC7_REGISTRY_PATH),
            "pc7_registry_bytes": PC7_REGISTRY_BYTES,
            "pc7_registry_sha256": PC7_REGISTRY_SHA256,
            "pc7_manifest_path": str(PC7_MANIFEST_PATH),
            "pc7_manifest_bytes": PC7_MANIFEST_BYTES,
            "pc7_manifest_sha256": PC7_MANIFEST_SHA256,
            "pc7_publication_report_path": str(PC7_PUBLICATION_REPORT),
            "pc7_publication_report_bytes": PC7_PUBLICATION_BYTES,
            "pc7_publication_report_sha256": PC7_PUBLICATION_SHA256,
            "dispatch": copy.deepcopy(registry["dispatch"]),
        },
        "criteria": criteria,
        "cases": cases,
        "relations": relations,
        "excluded_future_ids": utf8_sorted(list(EXPECTED_FUTURE_IDS)),
        "self_validation": {
            "schema_mutations": mutation_results,
            "rejection_checks": {},
            "defined_fixture_ids": utf8_sorted(list(defined)),
            "generated_case_ids": [row["fixture_id"] for row in cases],
        },
    }
    validate_plan(plan)
    rejection = run_rejection_self_tests(manifest, runtime, plan)
    plan["self_validation"]["rejection_checks"] = rejection
    validate_plan(plan)
    return plan


class UniqueStore(argparse.Action):
    def __call__(
        self,
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: Any,
        option_string: str | None = None,
    ) -> None:
        if getattr(namespace, self.dest, None) is not None:
            preflight_fail("invocation", option_string or self.dest, "argument repeated")
        setattr(namespace, self.dest, values)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pc8-authority-root", action=UniqueStore, default=None)
    parser.add_argument("--pc8-authority-registry", action=UniqueStore, default=None)
    parser.add_argument("--output", action=UniqueStore, default=None)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--print-summary", action="store_true")
    try:
        args = parser.parse_args()
        if args.pc8_authority_root is None or args.pc8_authority_registry is None:
            preflight_fail("invocation", "authority", "root and registry required")
        authority_root = Path(args.pc8_authority_root)
        registry_path = Path(args.pc8_authority_registry)
        registry, manifest_raw, pc7_registry_raw = authority_preflight(
            authority_root, registry_path
        )
        manifest = strict_loads(manifest_raw, str(MANIFEST_PATH))
        runtime = SchemaRuntime(manifest)
        runtime.validate("SCHEMA-MANIFEST", manifest)
        populations = validate_populations(manifest)
        schema_closure = validate_references(manifest, runtime)
        mutation_results = run_schema_mutations(manifest, runtime)
        _, pc7_manifest, expanded_outputs = load_pc7(authority_root, pc7_registry_raw)
        generated = generate(
            registry,
            manifest,
            runtime,
            pc7_manifest,
            expanded_outputs,
            populations,
            schema_closure,
            mutation_results,
        )
        raw = plan_bytes(generated)
        output = Path(args.output) if args.output is not None else PLAN_PATH
        if args.check:
            if args.output is not None:
                fail("PC8_INVOCATION_INVALID", "--output", "cannot combine with --check")
            if not PLAN_PATH.exists() or PLAN_PATH.read_bytes() != raw:
                fail("PC8_CHECKED_PLAN_MISMATCH", str(PLAN_PATH), "bytes differ")
        else:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_bytes(raw)
        if args.print_summary:
            print(
                json.dumps(
                    {
                        "defined_current_fixture_ids": len(manifest["fixtures"]),
                        "generated_current_plan_ids": len(generated["cases"]),
                        "relations": len(generated["relations"]),
                        "excluded_future_ids": len(generated["excluded_future_ids"]),
                        "schema_mutations": len(mutation_results),
                        "plan_bytes": len(raw),
                        "plan_sha256": sha256(raw),
                        "populations": populations,
                        "rejection_checks": generated["self_validation"][
                            "rejection_checks"
                        ],
                    },
                    sort_keys=True,
                )
            )
        return 0
    except (PlanError, AuthorityPreflightError, AdmissionError) as error:
        print(str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
