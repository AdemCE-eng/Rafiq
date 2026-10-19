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

    def test_rafiq_installs_alone(self):
        isolated = self.root / "standalone"
        shutil.copytree(self.root / "skills" / "rafiq",
                        isolated / "skills" / "rafiq")
        self.assertEqual(validate(isolated, expected={"rafiq"})[0], [])

    def test_obsolete_install_path_rejected(self):
        old = "skills/learning-" + "companion"
        (self.root / "README.md").write_text("Copy " + old, encoding="utf-8")
        self.assertTrue(any("obsolete public" in e for e in validate(self.root)[0]))

    def test_obsolete_repository_url_rejected(self):
        old = "https://github.com/AdemCE-eng/modern-learning-" + "skills"
        (self.root / "README.md").write_text(old, encoding="utf-8")
        self.assertTrue(any("obsolete public" in e for e in validate(self.root)[0]))

    def test_historical_paths_allowed(self):
        results = self.root / "tests/behavioral/results"
        results.mkdir(parents=True)
        (results / "past.md").write_text("skills/learning-" + "companion", encoding="utf-8")
        self.assertEqual(validate(self.root)[0], [])

    def test_each_skill_in_both_client_layouts(self):
        # Packaging test only: no native client invocation is implied.
        for client in (".agents", ".claude"):
            for source in sorted((ROOT / "skills").iterdir()):
                if not source.is_dir():
                    continue
                with self.subTest(client=client, skill=source.name):
                    project = self.root / ("install-" + client[1:] + "-" + source.name)
                    destination = project / client / "skills" / source.name
                    shutil.copytree(source, destination)
                    source_files = {p.relative_to(source): p.read_bytes()
                                    for p in source.rglob("*") if p.is_file()}
                    installed_files = {p.relative_to(destination): p.read_bytes()
                                       for p in destination.rglob("*") if p.is_file()}
                    self.assertEqual(source_files, installed_files)
                    self.assertEqual(validate(project / client, expected={source.name})[0], [])

    def test_personal_detail_in_template_rejected(self):
        template = self.root / "skills/rafiq/assets/workspace-template/LEARNER.md"
        template.write_text(template.read_text(encoding="utf-8") +
                            "\nContact: fictional@example.invalid\n", encoding="utf-8")
        self.assertTrue(any("personal data" in e for e in validate(self.root)[0]))

    def test_missing_template_rejected(self):
        (self.root / "skills/rafiq/assets/workspace-template/MISSION.md").unlink()
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
