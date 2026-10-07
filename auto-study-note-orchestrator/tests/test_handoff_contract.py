"""Regression examples for the handoff contract. Not run during drafting."""

from argparse import Namespace
from pathlib import Path
import json
import shutil
import sys
import tempfile
import unittest


TESTS = Path(__file__).resolve().parent
ROOT = TESTS.parent
SCRIPTS = ROOT / "scripts"
EXAMPLES = ROOT / "examples" / "ols-and-r-squared"
sys.path.insert(0, str(SCRIPTS))

from check_handoffs import check  # noqa: E402
from validate_study_note import validate  # noqa: E402


def example_report():
    return check(
        [EXAMPLES / "u01_handoff.json", EXAMPLES / "u02_handoff.json"],
        [EXAMPLES / "merged.tex"],
        EXAMPLES / "source_inventory.md",
        EXAMPLES / "issues.json",
        final=True,
    )


class ExampleRun(unittest.TestCase):
    def test_example_run_satisfies_the_handoff_contract(self):
        report = example_report()
        self.assertEqual(report["failures"], [])
        self.assertEqual(report["status"], "pass")

    def test_a_result_reused_by_another_batch_is_surfaced(self):
        report = example_report()
        reused = {item["body_label"]: item for item in report["reused_results"]}
        self.assertIn("eq:ols-slope", reused)
        self.assertEqual(reused["eq:ols-slope"]["referenced_by"], ["U01", "U02"])
        self.assertEqual(reused["eq:ols-slope"]["declared_in"], ["merged.tex"])

    def test_existing_fixtures_still_satisfy_the_contract(self):
        fixtures = TESTS / "fixtures"
        report = check(
            [fixtures / "duplicate-u01.json", fixtures / "duplicate-u02.json"],
            [fixtures / "unit-body-clean.tex"],
        )
        self.assertEqual(report["failures"], [])


class ContractViolations(unittest.TestCase):
    """Each case mutates the U01 example handoff and expects a specific failure."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.record = json.loads((EXAMPLES / "u01_handoff.json").read_text(encoding="utf-8"))

    def tearDown(self):
        self._tmp.cleanup()

    def report(self, with_inventory: bool = False):
        path = self.tmp / "u01_handoff.json"
        path.write_text(json.dumps(self.record, ensure_ascii=False), encoding="utf-8")
        inventory = EXAMPLES / "source_inventory.md" if with_inventory else None
        return check([path], [EXAMPLES / "u01_body.tex"], inventory)

    def test_body_label_naming_nothing_fails(self):
        self.record["formula_candidates"][0]["body_label"] = "eq:not-emitted"
        failures = self.report()["failures"]
        self.assertTrue(any("resolves to no" in item for item in failures), failures)

    def test_continuity_body_label_naming_nothing_fails(self):
        self.record["continuity_updates"][0]["body_label"] = "sec:not-emitted"
        failures = self.report()["failures"]
        self.assertTrue(any("resolves to no" in item for item in failures), failures)

    def test_unknown_continuity_kind_fails(self):
        self.record["continuity_updates"][0]["kind"] = "formula"
        failures = self.report()["failures"]
        self.assertTrue(any("is not one of" in item for item in failures), failures)

    def test_absent_continuity_updates_fails(self):
        del self.record["continuity_updates"]
        failures = self.report()["failures"]
        self.assertTrue(any("continuity_updates must be a list" in item for item in failures), failures)

    def test_absent_formula_candidates_fails(self):
        del self.record["formula_candidates"]
        failures = self.report()["failures"]
        self.assertTrue(any("formula_candidates must be a list" in item for item in failures), failures)

    def test_repeating_a_result_key_inside_one_handoff_fails(self):
        self.record["formula_candidates"].append(dict(self.record["formula_candidates"][0]))
        failures = self.report()["failures"]
        self.assertTrue(any("duplicate result key" in item for item in failures), failures)

    def test_coverage_id_missing_from_the_inventory_fails(self):
        self.record["coverage_ids"] = ["L1-01", "L1-99"]
        failures = self.report(with_inventory=True)["failures"]
        self.assertTrue(any("not in the source inventory" in item for item in failures), failures)

    def test_empty_coverage_ids_fails(self):
        self.record["coverage_ids"] = []
        failures = self.report()["failures"]
        self.assertTrue(any("coverage_ids must be a non-empty list" in item for item in failures), failures)


class CoverageAndClosure(unittest.TestCase):
    """Accounting gaps and issue loss should fail independently of prose quality."""

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.tmp = Path(self._tmp.name)
        self.records = [json.loads((EXAMPLES / f"u0{i}_handoff.json").read_text(encoding="utf-8")) for i in (1, 2)]
        self.issues = json.loads((EXAMPLES / "issues.json").read_text(encoding="utf-8"))

    def tearDown(self):
        self._tmp.cleanup()

    def report(self, final=True):
        paths = []
        for i, record in enumerate(self.records):
            path = self.tmp / f"u{i}_handoff.json"
            path.write_text(json.dumps(record, ensure_ascii=False), encoding="utf-8")
            paths.append(path)
        ledger = self.tmp / "issues.json"
        ledger.write_text(json.dumps(self.issues, ensure_ascii=False), encoding="utf-8")
        return check(paths, [EXAMPLES / "u01_body.tex", EXAMPLES / "u02_body.tex"],
                     EXAMPLES / "source_inventory.md", ledger, final=final)

    def test_unassigned_inventory_item_fails_only_at_final_accounting(self):
        self.records[1]["coverage_ids"].remove("L1-05")
        del self.records[1]["coverage_map"]["L1-05"]
        self.assertEqual(self.report(final=False)["failures"], [])
        self.assertTrue(any("has no coverage_map entry" in f for f in self.report()["failures"]))

    def test_coverage_claim_requires_an_existing_body_location(self):
        self.records[0]["coverage_map"]["L1-01"]["body_labels"] = ["sec:absent"]
        self.assertTrue(any("resolves to no" in f for f in self.report()["failures"]))

    def test_pending_coverage_blocks_final_completion(self):
        self.records[0]["coverage_map"]["L1-01"] = {"status": "missing", "reason": "尚未起草"}
        self.assertTrue(any("is not complete" in f for f in self.report()["failures"]))

    def test_omission_needs_a_reason(self):
        self.records[0]["coverage_map"]["L1-01"] = {"status": "intentionally-omitted"}
        self.assertTrue(any("requires a reason" in f for f in self.report()["failures"]))

    def test_reported_issue_cannot_disappear_from_ledger(self):
        self.issues = []
        self.assertTrue(any("missing from issues.json" in f for f in self.report()["failures"]))

    def test_later_empty_handoff_does_not_close_an_open_issue(self):
        self.issues[0].update(status="open", resolution="", body_labels=[])
        self.records.append({"unit_id": "U03", "coverage_ids": ["L1-05"],
                             "coverage_map": {"L1-05": self.records[1]["coverage_map"]["L1-05"]},
                             "unresolved": [], "formula_candidates": [], "continuity_updates": []})
        self.assertEqual(self.report(final=False)["status"], "pass")
        self.assertTrue(any("remains open" in f for f in self.report()["failures"]))

    def test_closure_needs_evidence_and_a_real_correction_location(self):
        self.issues[0].update(resolution="", body_labels=["sec:absent"])
        failures = self.report()["failures"]
        self.assertTrue(any("resolution evidence" in f for f in failures))
        self.assertTrue(any("resolves to no" in f for f in failures))

    def test_accepted_limitation_stays_visible(self):
        self.issues[0].update(status="accepted", resolution="原资料缺失，交付说明明确本项依据现有笔记", body_labels=[])
        report = self.report()
        self.assertEqual(report["status"], "pass")
        self.assertTrue(any("accepted limitation" in w for w in report["warnings"]))


class MergedExample(unittest.TestCase):
    def test_merged_output_and_fragments_pass_the_structural_validator(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            shutil.copy(ROOT / "assets" / "study-note-style.sty", tmp / "study-note-style.sty")
            shutil.copy(EXAMPLES / "merged.tex", tmp / "merged.tex")
            report = validate(
                Namespace(
                    tex=tmp / "merged.tex",
                    pdf=None,
                    log=None,
                    inventory=None,
                    unit_fragment=[EXAMPLES / "u01_body.tex", EXAMPLES / "u02_body.tex"],
                )
            )
            self.assertEqual(report["failures"], [])

if __name__ == "__main__":
    unittest.main()
