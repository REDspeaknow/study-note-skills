"""Regression examples for document-level formula ownership. Not run during drafting."""

from argparse import Namespace
from pathlib import Path
import sys
import unittest


TESTS = Path(__file__).resolve().parent
SCRIPTS = TESTS.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))

from collect_formula_candidates import collect  # noqa: E402
from validate_study_note import validate  # noqa: E402


def structural_failures(name, *unit_fragments):
    fixture = TESTS / "fixtures"
    report = validate(
        Namespace(
            tex=fixture / name,
            pdf=None,
            log=None,
            inventory=None,
            unit_fragment=[fixture / item for item in unit_fragments],
        )
    )
    return [item for item in report["failures"] if "formula" in item or "unit fragment" in item]


class FormulaBoundaryRegression(unittest.TestCase):
    def test_clean_unit_and_one_global_section(self):
        self.assertEqual(
            structural_failures("merged-one-global.tex", "unit-body-clean.tex"), []
        )

    def test_unit_cannot_emit_formula_table(self):
        failures = structural_failures(
            "merged-one-global.tex", "unit-body-with-summary.tex"
        )
        self.assertTrue(any("unit fragment" in item and "formula summary table" in item for item in failures))

    def test_pure_concept_guide_can_omit_formula_section(self):
        self.assertEqual(structural_failures("concept-only-no-summary.tex"), [])

    def test_two_global_sections_and_early_summary_are_rejected(self):
        failures = structural_failures("merged-two-global.tex")
        self.assertTrue(any("more than one formula summary" in item for item in failures))
        self.assertTrue(any("formula summary must follow" in item for item in failures))

    def test_two_units_submit_one_semantic_candidate(self):
        fixture = TESTS / "fixtures"
        report = collect(
            [fixture / "duplicate-u01.json", fixture / "duplicate-u02.json"]
        )
        self.assertEqual(report["distinct_candidates"], 1)
        self.assertEqual(report["duplicate_keys"], ["network_pairs"])
        self.assertEqual(report["formula_conflicts"], [])


if __name__ == "__main__":
    unittest.main()
