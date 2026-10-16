"""Negative fixtures ensure packaging defects really fail validation."""
import shutil
import tempfile
import unittest
from pathlib import Path

from validate_repo import validate

ROOT = Path(__file__).resolve().parents[1]


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        (ROOT / "work").mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=ROOT / "work")
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT / "skills", self.root / "skills")
        self.entry = self.root / "skills" / "learning-coach" / "SKILL.md"

    def tearDown(self):
        self.temp.cleanup()

    def alter(self, old, new):
        self.entry.write_text(self.entry.read_text(encoding="utf-8").replace(old, new),
                              encoding="utf-8")

    def test_valid_independent_bundles(self):
        self.assertEqual(validate(self.root)[0], [])

    def test_nested_fenced_bundle_links_are_ignored(self):
        (self.root / "REVIEW_BUNDLE.md").write_text(
            "# Snapshot\n\n````markdown\n```text\nexample\n```\n"
            "[Copied relative link](missing-at-bundle-root.md)\n````\n",
            encoding="utf-8")
        self.assertEqual(validate(self.root)[0], [])

    def test_companion_installs_alone(self):
        isolated = self.root / "standalone"
        shutil.copytree(self.root / "skills" / "learning-companion",
                        isolated / "skills" / "learning-companion")
        self.assertEqual(validate(isolated, expected={"learning-companion"})[0], [])

    def test_personal_detail_in_template_rejected(self):
        template = self.root / "skills/learning-companion/assets/workspace-template/LEARNER.md"
        template.write_text(template.read_text(encoding="utf-8") +
                            "\nContact: fictional@example.invalid\n", encoding="utf-8")
        self.assertTrue(any("personal data" in e for e in validate(self.root)[0]))

    def test_missing_template_rejected(self):
        (self.root / "skills/learning-companion/assets/workspace-template/MISSION.md").unlink()
        self.assertTrue(any("missing or unexpected" in e for e in validate(self.root)[0]))

    def test_unsupported_frontmatter_rejected(self):
        self.alter("name: learning-coach", "name: learning-coach\nmemory: automatic")
        self.assertTrue(any("unsupported" in e for e in validate(self.root)[0]))

    def test_path_escape_rejected(self):
        self.entry.write_text(self.entry.read_text(encoding="utf-8") +
                              "\n[Escape](../../../../outside.md)\n", encoding="utf-8")
        self.assertTrue(any("escaping" in e for e in validate(self.root)[0]))

    def test_mismatched_name_rejected(self):
        self.alter("name: learning-coach", "name: other")
        self.assertTrue(any("mismatched" in e for e in validate(self.root)[0]))

    def test_duplicate_field_rejected(self):
        self.alter("name: learning-coach", "name: learning-coach\nname: learning-coach")
        self.assertTrue(any("duplicate" in e for e in validate(self.root)[0]))

    def test_missing_reference_rejected(self):
        self.entry.write_text(self.entry.read_text(encoding="utf-8") +
                              "\n[Missing](references/missing.md)\n", encoding="utf-8")
        self.assertTrue(any("missing or escaping" in e for e in validate(self.root)[0]))

    def test_sibling_dependency_rejected(self):
        self.entry.write_text(self.entry.read_text(encoding="utf-8") +
                              "\n[Sibling](../tech-research/SKILL.md)\n", encoding="utf-8")
        self.assertTrue(any("leaves independent" in e for e in validate(self.root)[0]))


if __name__ == "__main__":
    unittest.main()
