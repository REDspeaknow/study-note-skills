"""Acceptance/rejection checks for actual assembled review-note bodies."""

from argparse import Namespace
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_study_note import validate


class ReviewStructure(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        shutil.copy2(ROOT / "assets/study-note-style.sty", self.root)

    def tearDown(self):
        self.tmp.cleanup()

    def run_note(self, body, extra=None):
        entry = self.root / "main.tex"
        entry.write_text(
            "\\documentclass{ctexart}\n\\usepackage{study-note-style}\n"
            "\\begin{document}\n" + body + "\n\\end{document}\n", encoding="utf-8"
        )
        for name, content in (extra or {}).items():
            path = self.root / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return validate(Namespace(tex=entry, pdf=None, log=None, inventory=None, unit_fragment=[]))

    def test_compact_guide_without_frontmatter_or_handoffs_passes(self):
        report = self.run_note(
            r"\section{网络效应}\StudyTerm{\PriorityMust}{网络效应}{新增者改变其他用户的价值。}"
            r"\StudyPoint{\PriorityImportant}{收益分解}"
            r"\begin{proofbox}\begin{align*}W(N)&=NU(N)-cN\end{align*}\end{proofbox}"
            r"\StudyPoint{\PriorityKnow}{计算例题}"
            r"\begin{examplebox}求两单位成本。\[2c=2\times3=6\]\end{examplebox}"
        )
        self.assertEqual(report["failures"], [])
        self.assertEqual(report["metrics"]["knowledge_point_entries"], 3)

    def test_procedure_step_box_is_a_blue_content_box(self):
        report = self.run_note(
            r"\section{模型}\StudyPoint{\PriorityMust}{最优收费}"
            r"\begin{stepbox}[title=操作步骤]\begin{enumerate}\item 定总价。\end{enumerate}\end{stepbox}"
        )
        self.assertEqual(report["failures"], [])
        self.assertEqual(report["metrics"]["blue_content_boxes"], 1)

    def test_step_box_without_an_owning_point_is_rejected(self):
        report = self.run_note(
            r"\section{模型}\begin{stepbox}先算再看边界。\end{stepbox}"
        )
        self.assertTrue(any("no owning" in f for f in report["failures"]))

    def test_canonical_template_passes_with_title_line_spacing(self):
        entry = self.root / "template.tex"
        shutil.copy2(ROOT / "assets/通用笔记模板.tex", entry)
        report = validate(Namespace(tex=entry, pdf=None, log=None, inventory=None, unit_fragment=[]))
        self.assertEqual(report["failures"], [])

    def test_front_global_map_and_body_diagram_have_different_roles(self):
        report = self.run_note(
            r"\section*{全局思维导图}\begin{tikzpicture}\node{课程与主题};\end{tikzpicture}"
            r"\tableofcontents\section{均衡}\StudyPoint{\PriorityMust}{均衡交点}"
            r"\begin{tikzpicture}\draw (0,0)--(1,1);\end{tikzpicture}"
        )
        self.assertEqual(report["failures"], [])
        self.assertEqual(report["metrics"]["global_mind_maps"], 1)
        self.assertEqual(report["metrics"]["main_sections"], 1)
        self.assertEqual(report["metrics"]["tikz_diagrams"], 2)

    def test_global_map_after_contents_or_body_is_rejected(self):
        for prefix in [r"\tableofcontents", r"\section{正文}\StudyTerm{\PriorityMust}{定义}{说明。}"]:
            with self.subTest(prefix=prefix):
                report = self.run_note(prefix + r"\section*{全局思维导图}"
                    r"\begin{tikzpicture}\node{课程};\end{tikzpicture}"
                    r"\section{模型}\StudyTerm{\PriorityMust}{概念}{说明。}")
                self.assertTrue(any("must precede" in f or "before the main" in f for f in report["failures"]))

    def test_duplicate_global_maps_in_input_fragments_are_rejected(self):
        report = self.run_note(r"\input{build/maps}\section{正文}\StudyTerm{\PriorityMust}{概念}{说明。}", {
            "build/maps.tex": r"\section*{全局思维导图}\section*{课程框架导图}"
        })
        self.assertTrue(any("multiple relationship maps" in f for f in report["failures"]))

    def test_legend_cannot_substitute_for_knowledge_point_entries(self):
        report = self.run_note(r"\PriorityMust 必背\section{模型}这里有一个未标识的概念。")
        self.assertTrue(any("no star-marked" in f for f in report["failures"]))

    def test_build_input_is_inspected_not_just_entrypoint(self):
        report = self.run_note(r"\input{build/body_all}", {
            "build/body_all.tex": r"\section{模型}\StudyPoint{\PriorityMust}{定义}文字。\input{build/detail}",
            "build/detail.tex": r"\subsubsection{未标星推导}\[y=x+1\]"
        })
        self.assertEqual(len(report["metrics"]["tex_files_checked"]), 3)
        self.assertTrue(any("third-level" in f for f in report["failures"]))
        # Auxiliary display math is allowed; the deep heading remains invalid.
        self.assertFalse(any("outside a blue box" in f for f in report["failures"]))

    def test_auxiliary_formula_does_not_force_an_extra_box(self):
        report = self.run_note(
            r"\section{模型}\StudyTerm{\PriorityMust}{需求}{给定费用下愿意参与的规模。}"
            r"固定总费用时，\[p^S=p-p^B.\]"
        )
        self.assertEqual(report["failures"], [])
        self.assertEqual(report["metrics"]["blue_content_boxes"], 0)
        self.assertEqual(report["content_review"], "not_assessed")

    def test_fragmented_chain_is_a_review_candidate_not_automatic_failure(self):
        report = self.run_note(
            r"\section{模型}\StudyPoint{\PriorityMust}{均衡计算}"
            + r"\begin{formulabox}\[x=1\]\end{formulabox}" * 3
        )
        self.assertEqual(report["failures"], [])
        candidates = report["metrics"]["box_fragmentation_review_candidates"]
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["boxes"], 3)
        self.assertFalse(report["metrics"]["content_quality_assessed"])

    def test_missing_and_cyclic_inputs_fail(self):
        missing = self.run_note(r"\input{build/missing}")
        self.assertTrue(any("missing TeX input" in f for f in missing["failures"]))
        cycle = self.run_note(r"\input{build/loop}", {"build/loop.tex": r"\input{main}"})
        self.assertTrue(any("cyclic" in f for f in cycle["failures"]))

    def test_bad_point_priority_is_rejected(self):
        report = self.run_note(r"\section{概念}\StudyPoint{}{独立概念}定义。")
        self.assertTrue(any("lacks a valid" in f for f in report["failures"]))

    def test_chapter_reset_prevents_inherited_point_for_unmarked_math(self):
        report = self.run_note(
            r"\section{一}\StudyPoint{\PriorityMust}{定义}定义。"
            r"\section{二}\begin{examplebox}题面\[y=1\]\end{examplebox}"
        )
        self.assertTrue(any("no owning" in f for f in report["failures"]))

    def test_old_summary_boxes_and_numbering_are_rejected(self):
        report = self.run_note(
            r"\section{1.1.1 主题}\StudyPoint{\PriorityMust}{定义}定义。"
            r"\begin{takeawaybox}重述。\end{takeawaybox}\setcounter{secnumdepth}{3}"
        )
        self.assertTrue(any("legacy takeawaybox" in f for f in report["failures"]))
        self.assertTrue(any("numbering" in f for f in report["failures"]))

    def test_formula_tables_in_included_unit_cannot_evade_ownership_check(self):
        report = self.run_note(r"\input{build/body}", {
            "build/body.tex": r"\section{主题}\StudyPoint{\PriorityMust}{定义}定义。"
            r"\begin{FormulaSummaryTable}\FormulaSummaryRow{名}{式}{条件}\end{FormulaSummaryTable}"
        })
        self.assertTrue(any("without a document-level" in f for f in report["failures"]))


if __name__ == "__main__":
    unittest.main()
