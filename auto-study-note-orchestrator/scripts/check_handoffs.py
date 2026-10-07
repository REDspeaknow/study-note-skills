#!/usr/bin/env python3
"""Check handoff locations, coverage accounting and persistent issue closure.

Structural accounting only: actual teaching quality still needs editorial review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


KINDS = ("definition", "notation", "result")
CANDIDATE_FIELDS = ("key", "name", "formula", "conditions", "body_label")
UPDATE_FIELDS = ("kind", "name", "meaning", "body_label")
LABEL_RE = re.compile(r"\\label\{([^{}]+)\}")
ID_HEADERS = {"id", "coverage id", "gap id"}
COVERAGE_STATES = {"pending", "represented", "represented-indirectly", "intentionally-omitted", "weak", "missing"}
COMPLETE_STATES = {"represented", "represented-indirectly", "intentionally-omitted"}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def strip_comments(tex: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", tex)


def body_labels(paths: list[Path]) -> dict[str, list[str]]:
    """Map every \\label in the supplied bodies to the files that declare it."""
    owners: dict[str, set[str]] = {}
    for path in paths:
        for label in LABEL_RE.findall(strip_comments(read_text(path.resolve()))):
            label = label.strip()
            if label:
                owners.setdefault(label, set()).add(path.name)
    return {label: sorted(names) for label, names in sorted(owners.items())}


def inventory_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    for line in read_text(path.resolve()).splitlines():
        value = line.strip()
        if not (value.startswith("|") and value.endswith("|")):
            continue
        if re.fullmatch(r"[|:\-\s]+", value):
            continue
        first = value.strip("|").split("|")[0].strip()
        if first and first.lower() not in ID_HEADERS:
            ids.add(first)
    return ids


def _text_field(record: dict[str, Any], field: str) -> str:
    value = record.get(field)
    return value.strip() if isinstance(value, str) else ""


def check(
    handoffs: list[Path], bodies: list[Path], inventory: Path | None = None,
    issues: Path | None = None, final: bool = False,
) -> dict[str, Any]:
    failures: list[str] = []
    warnings: list[str] = []
    metrics: dict[str, Any] = {}

    labels = body_labels(bodies)
    metrics["known_labels"] = len(labels)
    metrics["bodies_read"] = len(bodies)

    known_ids = inventory_ids(inventory) if inventory else None
    if known_ids is not None:
        metrics["inventory_ids"] = len(known_ids)

    units: list[str] = []
    referenced: dict[str, set[str]] = {}
    coverage_map: dict[str, dict[str, Any]] = {}
    reported_issues: dict[str, dict[str, Any]] = {}

    def resolve(where: str, label: str, unit_id: str | None = None) -> None:
        if label not in labels:
            failures.append(f"{where}: body_label {label!r} resolves to no \\label in the supplied bodies")
        elif unit_id is not None:
            referenced.setdefault(label, set()).add(unit_id)

    def locations(where: str, item: dict[str, Any], required: bool) -> None:
        values = item.get("body_labels", [])
        if not isinstance(values, list) or not all(isinstance(v, str) and v.strip() for v in values):
            failures.append(f"{where}: body_labels must be a list of non-empty strings")
            return
        if required and not values:
            failures.append(f"{where}: body_labels must identify the teaching passage")
        for label in values:
            resolve(where, label.strip())

    for path in handoffs:
        name = path.name
        try:
            record = json.loads(read_text(path))
        except (OSError, json.JSONDecodeError) as exc:
            failures.append(f"{name}: unreadable handoff ({exc})")
            continue
        if not isinstance(record, dict):
            failures.append(f"{name}: handoff root must be a JSON object")
            continue

        unit_id = record.get("unit_id")
        if not isinstance(unit_id, str) or not unit_id.strip():
            failures.append(f"{name}: missing unit_id")
            continue
        unit_id = unit_id.strip()
        if unit_id in units:
            failures.append(f"{name}: duplicate unit_id {unit_id!r}")
        units.append(unit_id)

        coverage = record.get("coverage_ids")
        assigned: set[str] = set()
        if not isinstance(coverage, list) or not coverage:
            failures.append(f"{name}: coverage_ids must be a non-empty list")
        elif not all(isinstance(item, str) and item.strip() for item in coverage):
            failures.append(f"{name}: coverage_ids entries must be non-empty strings")
        else:
            assigned = {item.strip() for item in coverage}
            if len(assigned) != len(coverage):
                failures.append(f"{name}: duplicate coverage_ids")
            for coverage_id in assigned:
                if known_ids is not None and coverage_id not in known_ids:
                    failures.append(
                        f"{name}: coverage id {coverage_id.strip()!r} is not in the source inventory"
                    )

        mapping = record.get("coverage_map")
        if not isinstance(mapping, dict):
            failures.append(f"{name}: coverage_map must be an object keyed by coverage ID")
            mapping = {}
        if set(mapping) != assigned:
            failures.append(f"{name}: coverage_map keys must match coverage_ids")
        for coverage_id, item in mapping.items():
            where = f"{name}: coverage {coverage_id}"
            if not isinstance(item, dict):
                failures.append(f"{where} must be an object")
                continue
            state = _text_field(item, "status")
            if state not in COVERAGE_STATES:
                failures.append(f"{where}: unknown status {state!r}")
            locations(where, item, state in {"represented", "represented-indirectly", "weak"})
            if state not in {"represented", "represented-indirectly"} and not _text_field(item, "reason"):
                failures.append(f"{where}: status {state!r} requires a reason")
            # Ordered handoffs allow a later repair batch to replace an earlier claim.
            coverage_map[coverage_id] = {**item, "unit_id": unit_id}

        unresolved = record.get("unresolved")
        if not isinstance(unresolved, list):
            failures.append(f"{name}: unresolved must be a list (use [] when there is none)")
            unresolved = []
        for index, item in enumerate(unresolved, 1):
            where = f"{name}: unresolved {index}"
            if not isinstance(item, dict) or not all(_text_field(item, field) for field in ("issue_id", "description")):
                failures.append(f"{where}: requires issue_id and description")
                continue
            ids = item.get("coverage_ids")
            if not isinstance(ids, list) or not ids or not all(isinstance(v, str) and v.strip() for v in ids):
                failures.append(f"{where}: coverage_ids must be a non-empty list of strings")
                continue
            if known_ids is not None and not set(ids) <= known_ids:
                failures.append(f"{where}: coverage_ids not in the source inventory")
                continue
            issue_id = _text_field(item, "issue_id")
            if issue_id in reported_issues and item != reported_issues[issue_id]:
                failures.append(f"{where}: conflicting identity for issue {issue_id!r}")
            reported_issues[issue_id] = item

        candidates = record.get("formula_candidates")
        if not isinstance(candidates, list):
            failures.append(f"{name}: formula_candidates must be a list (use [] when empty)")
            candidates = []
        updates = record.get("continuity_updates")
        if not isinstance(updates, list):
            failures.append(f"{name}: continuity_updates must be a list (use [] when empty)")
            updates = []

        seen_keys: dict[str, int] = {}
        for index, item in enumerate(candidates, 1):
            where = f"{name}: formula candidate {index}"
            if not isinstance(item, dict):
                failures.append(f"{where} must be an object")
                continue
            missing = [field for field in CANDIDATE_FIELDS if not _text_field(item, field)]
            if missing:
                failures.append(f"{where} lacks {missing}")
                continue
            key = _text_field(item, "key")
            if key in seen_keys:
                failures.append(f"{where}: duplicate result key {key!r} (first at candidate {seen_keys[key]})")
            else:
                seen_keys[key] = index
            resolve(where, _text_field(item, "body_label"), unit_id)

        seen_names: dict[str, int] = {}
        for index, item in enumerate(updates, 1):
            where = f"{name}: continuity update {index}"
            if not isinstance(item, dict):
                failures.append(f"{where} must be an object")
                continue
            missing = [field for field in UPDATE_FIELDS if not _text_field(item, field)]
            if missing:
                failures.append(f"{where} lacks {missing}")
                continue
            kind = _text_field(item, "kind")
            if kind not in KINDS:
                failures.append(f"{where}: kind {kind!r} is not one of {list(KINDS)}")
            identity = f"{kind}:{_text_field(item, 'name')}"
            if identity in seen_names:
                failures.append(f"{where}: duplicate continuity entry {identity!r}")
            else:
                seen_names[identity] = index
            resolve(where, _text_field(item, "body_label"), unit_id)

    ledger: dict[str, dict[str, Any]] = {}
    if issues is not None:
        try:
            entries = json.loads(read_text(issues))
            if not isinstance(entries, list):
                raise ValueError("issues root must be a list")
        except (OSError, ValueError) as exc:
            failures.append(f"issues: unreadable ledger ({exc})")
            entries = []
        for index, item in enumerate(entries, 1):
            where = f"issues: entry {index}"
            if not isinstance(item, dict) or not all(_text_field(item, field) for field in ("issue_id", "description")):
                failures.append(f"{where}: requires issue_id and description")
                continue
            issue_id = _text_field(item, "issue_id")
            if issue_id in ledger:
                failures.append(f"{where}: duplicate issue_id {issue_id!r}")
            ledger[issue_id] = item
            ids = item.get("coverage_ids")
            if not isinstance(ids, list) or not ids or not all(isinstance(v, str) and v.strip() for v in ids):
                failures.append(f"{where}: coverage_ids must be a non-empty list of strings")
            elif known_ids is not None and not set(ids) <= known_ids:
                failures.append(f"{where}: coverage_ids not in the source inventory")
            state = _text_field(item, "status")
            if state not in {"open", "resolved", "accepted"}:
                failures.append(f"{where}: unknown issue status {state!r}")
            if state in {"resolved", "accepted"} and not _text_field(item, "resolution"):
                failures.append(f"{where}: closing an issue requires resolution evidence")
            locations(where, item, state == "resolved")
            if state == "open":
                (failures if final else warnings).append(f"issue {issue_id!r} remains open")
            elif state == "accepted":
                warnings.append(f"issue {issue_id!r}: accepted limitation — {_text_field(item, 'resolution')}")

    for issue_id, item in reported_issues.items():
        saved = ledger.get(issue_id)
        if saved is None:
            failures.append(f"issue {issue_id!r} reported in a handoff is missing from issues.json")
        elif any(saved.get(field) != item.get(field) for field in ("coverage_ids", "description")):
            failures.append(f"issue {issue_id!r}: ledger must preserve its original coverage_ids and description")

    if final:
        if inventory is None or issues is None:
            failures.append("final accounting requires --inventory and --issues (use [] for an empty ledger)")
        if known_ids is not None:
            for coverage_id in sorted(known_ids - set(coverage_map)):
                failures.append(f"inventory item {coverage_id!r} has no coverage_map entry")
        for coverage_id, item in coverage_map.items():
            if _text_field(item, "status") not in COMPLETE_STATES:
                failures.append(f"coverage {coverage_id!r} is not complete: {_text_field(item, 'status')}")

    # A result cited by a unit other than the one that declares it is the intended
    # reuse pattern; surface it so the merge step keeps a single explanation.
    reused = sorted(label for label, unit_ids in referenced.items() if len(unit_ids) > 1)

    metrics["handoffs_checked"] = len(handoffs)
    metrics["units"] = units
    metrics["referenced_labels"] = len(referenced)
    metrics["reused_results"] = reused

    return {
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "warnings": warnings,
        "metrics": metrics,
        "reused_results": [
            {"body_label": label, "referenced_by": sorted(referenced[label]), "declared_in": labels[label]}
            for label in reused
        ],
        "label_owners": labels,
        "coverage_map": coverage_map,
        "issues": list(ledger.values()),
    }


def main() -> int:
    # Windows consoles often default to a legacy code page (GBK here) that cannot
    # encode characters such as U+015C, so printing a report could crash the run.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--handoff", type=Path, action="append", required=True, help="unit handoff JSON; repeatable")
    parser.add_argument("--body", type=Path, action="append", default=[], help="unit body fragment; repeatable")
    parser.add_argument("--inventory", type=Path, help="source inventory markdown")
    parser.add_argument("--issues", type=Path, help="persistent issues.json ledger")
    parser.add_argument("--final", action="store_true", help="require full inventory accounting and closed issues")
    parser.add_argument("--out", type=Path, help="optional JSON report path")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args()

    report = check(args.handoff, args.body, args.inventory, args.issues, args.final)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(output + "\n", encoding="utf-8")
    if args.format == "json":
        print(output)
    else:
        print(f"status: {report['status']}")
        for failure in report["failures"]:
            print(f"  FAIL {failure}")
        for warning in report["warnings"]:
            print(f"  warn {warning}")
        for item in report["reused_results"]:
            print(
                f"  reuse {item['body_label']} declared in {', '.join(item['declared_in'])}"
                f" and cited by {', '.join(item['referenced_by'])}"
            )
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
