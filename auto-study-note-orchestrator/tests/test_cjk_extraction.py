"""Regression examples for judging whether a PDF text read actually landed.

A bundled Poppler without Adobe CMap language packs can read a Chinese note
as Latin noise, and the read is not always empty: a partially mapped file may
leak a stray CJK codepoint or two.  Treating that as a successful extraction
is how a broken text layer used to pass validation.
"""

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_study_note import cjk_count, cjk_is_plausible


class CjkExtraction(unittest.TestCase):
    def test_real_chinese_body_is_plausible(self):
        body = "平台经济学复习笔记：网络效应、双边收费与新旧网络竞争。" * 8
        self.assertTrue(cjk_is_plausible(body))
        self.assertGreater(cjk_count(body), 20)

    def test_latin_noise_with_a_stray_codepoint_is_not_plausible(self):
        # Reproduces the platform-economics PDF: 2 Chinese chars out of ~200k.
        noise = "o/po/p b a ba b\n\n### OLS\n" * 400 + "啰略"
        self.assertEqual(cjk_count(noise), 2)
        self.assertFalse(cjk_is_plausible(noise))

    def test_latin_only_read_is_not_plausible(self):
        self.assertFalse(cjk_is_plausible("o/po/p b a ba b\n\n### OLS\n"))

    def test_empty_read_is_not_plausible(self):
        self.assertFalse(cjk_is_plausible(""))
        self.assertFalse(cjk_is_plausible("   \n\t "))

    def test_short_but_genuine_read_is_not_plausible(self):
        # Below the absolute floor: a handful of characters is not a note.
        self.assertFalse(cjk_is_plausible("网络效应"))

    def test_ratio_guard_catches_diluted_reads(self):
        # Enough characters in absolute terms, but swamped by Latin noise, so
        # the extractor clearly did not map the body.
        diluted = "网络效应" * 20 + "x" * 20000
        self.assertGreaterEqual(cjk_count(diluted), 20)
        self.assertFalse(cjk_is_plausible(diluted))


if __name__ == "__main__":
    unittest.main()
