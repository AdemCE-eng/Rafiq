"""Validate this repository's deliberately small format, not all Agent Skills YAML.

Standard library only. Does not evaluate pedagogy or fetch remote links.
"""
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

EXPECTED = {"tech-research", "learning-roadmap", "learning-coach", "learn-new-tech", "rafiq"}


def validate(root, expected=EXPECTED):
    root = Path(root).resolve()
    errors = []
    found = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    if found != expected:
        errors.append(f"Expected {len(expected)} skill folders; found {sorted(found)}")
    for name in sorted(found):
        skill = root / "skills" / name
        entry = skill / "SKILL.md"
        if not entry.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = entry.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n(.+)\Z", text, re.S)
        if not match:
            errors.append(f"{name}: missing frontmatter or body")
            continue
        fields = {}
        for line in match[1].splitlines():
            key, sep, value = line.partition(": ")
            if not sep or key in fields or key not in {"name", "description"}:
                errors.append(f"{name}: unsupported or duplicate frontmatter line")
                continue
            if key == "description":
                try:
                    value = json.loads(value)
                except json.JSONDecodeError:
                    errors.append(f"{name}: description must be a JSON-quoted YAML string")
                    continue
            fields[key] = value
        value = fields.get("name", "")
        if (value != name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value)
                or len(value) > 64):
            errors.append(f"{name}: invalid or mismatched name")
        desc = fields.get("description")
        if not isinstance(desc, str) or not 1 <= len(desc.strip()) <= 1024:
            errors.append(f"{name}: invalid description")
        if len(text.splitlines()) > 160:
            errors.append(f"{name}: exceeds project's 160-line entrypoint budget")

    template = root / "skills" / "rafiq" / "assets" / "workspace-template"
    if "rafiq" in found:
        expected_templates = {"MISSION.md", "LEARNER.md", "CHECKPOINT.md"}
        actual = {p.name for p in template.glob("*") if p.is_file()}
        if actual != expected_templates:
            errors.append("companion: missing or unexpected workspace template")
        for file in template.rglob("*"):
            if not file.is_file():
                continue
            text = file.read_text(encoding="utf-8")
            # Heuristic only; human review must still check for personal details.
            if "Template only:" not in text or re.search(
                    r"[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}|[A-Za-z]:[\\/]|/Users/|/home/", text):
                errors.append(f"{file.name}: template may contain personal data or lacks template marker")

    # Historical transcripts retain original paths/hashes; current instructions must not.
    old_skill = "learning-" + "companion"
    old_repo = "modern-learning-" + "skills"
    for file in root.rglob("*"):
        if not file.is_file() or file.suffix not in {".md", ".py", ".json"}:
            continue
        rel = file.relative_to(root)
        if (any(part in {".git", ".agents", ".claude", "work", ".venv",
                        "__pycache__", "learning-workspaces"} for part in rel.parts)
                or rel.as_posix().startswith("tests/behavioral/results/")
                or rel.name == "REVIEW_BUNDLE.md"):
            continue
        content = file.read_text(encoding="utf-8")
        normalized = content.replace(chr(92), "/")
        if ("skills/" + old_skill in normalized
                or "github.com/AdemCE-eng/" + old_repo in normalized):
            errors.append(f"{rel}: obsolete public installation path")

    count = 0
    for file in sorted(root.rglob("*.md")):
        rel = file.relative_to(root)
        if any(p in {".git", ".agents", ".claude", "work", ".venv", "learning-workspaces"} for p in rel.parts):
            continue
        count += 1
        text = file.read_text(encoding="utf-8")
        if re.search(r"\[TODO:[^\n]*\]", text):
            errors.append(f"{rel}: unfinished scaffold")
        # Repository links use simple inline Markdown; code examples are excluded.
        text = re.sub(r"(?ms)^(`{3,}|~{3,})[^\n]*\n.*?^\1[ \t]*$", "", text)
        for target in re.findall(r"\[[^\]\n]+\]\(([^)\s]+)\)", text):
            parsed = urlsplit(target)
            if parsed.scheme in {"https", "http", "mailto"} or target.startswith("#"):
                continue
            if parsed.scheme or target.startswith(("/", "\\")):
                errors.append(f"{rel}: nonportable link {target}")
                continue
            dest = (file.parent / unquote(parsed.path)).resolve()
            if not dest.is_relative_to(root) or not dest.exists():
                errors.append(f"{rel}: missing or escaping link {target}")
            if rel.parts[0] == "skills":
                bundle = root / "skills" / rel.parts[1]
                if not dest.is_relative_to(bundle):
                    errors.append(f"{rel}: link leaves independent skill bundle")
    return errors, count


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    errors, count = validate(root)
    for error in errors:
        print("FAIL:", error)
    if errors:
        sys.exit(1)
    print(f"PASS: {len(EXPECTED)} skill bundles; {count} Markdown files; local links and project format.")
    print("Behavior, remote URLs and native client discovery require separate evaluation.")
