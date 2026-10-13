#!/usr/bin/env python3
"""Group unit handoff formula candidates by result key for editorial selection."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED = {"key", "name", "formula", "conditions", "body_label"}


def collect(paths: list[Path]) -> dict:
    groups: dict[str, list[dict]] = {}
    errors: list[str] = []
    for path in paths:
        try:
            record = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path}: {exc}")
            continue
        unit_id = record.get("unit_id")
        if not isinstance(unit_id, str) or not unit_id.strip():
            errors.append(f"{path}: missing unit_id")
            continue
        for index, item in enumerate(record.get("formula_candidates", []), 1):
            if not isinstance(item, dict) or REQUIRED - item.keys():
                errors.append(f"{path}: formula candidate {index} lacks {sorted(REQUIRED - set(item) if isinstance(item, dict) else REQUIRED)}")
                continue
            if any(not isinstance(item[field], str) or not item[field].strip() for field in REQUIRED):
                errors.append(f"{path}: formula candidate {index} has an empty field")
                continue
            key = item["key"].strip()
            groups.setdefault(key, []).append({"unit_id": unit_id, **item})

    conflicts = []
    for key, items in groups.items():
        formulas = {"".join(item["formula"].split()) for item in items}
        if len(formulas) > 1:
            conflicts.append(key)
    return {
        "status": "fail" if errors or conflicts else "pass",
        "distinct_candidates": len(groups),
        "duplicate_keys": sorted(key for key, items in groups.items() if len(items) > 1),
        "formula_conflicts": sorted(conflicts),
        "errors": errors,
        "groups": groups,
    }


def main() -> int:
    # Windows consoles often default to a legacy code page (GBK here) that cannot
    # encode characters such as U+015C, so printing a report could crash the run.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("records", type=Path, nargs="+", help="unit handoff JSON files")
    parser.add_argument("--out", type=Path, help="optional JSON report path")
    args = parser.parse_args()
    report = collect(args.records)
    output = json.dumps(report, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    sys.exit(main())
