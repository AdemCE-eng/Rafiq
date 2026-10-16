# Research and design record

Research date: 2026-10-16. Official sources were inspected before implementation.
Links to moving branches/pages describe what was inspected, not immutable releases.
No vendor prose or scripts were copied into the skills.

## Sources and resulting choices

| Official source | Observation used |
| --- | --- |
| [Agent Skills specification](https://agentskills.io/specification) | Directory + YAML frontmatter + Markdown; name/description required; optional resources. Names match directories, max 64 characters; descriptions max 1024. |
| [Codex / OpenAI skills](https://learn.chatgpt.com/docs/build-skills) | Progressive disclosure, local discovery locations, explicit invocation, optional OpenAI metadata. |
| [OpenAI skill-creator](https://github.com/openai/skills/blob/main/skills/.system/skill-creator/SKILL.md) | Concise self-contained instructions, detail only when useful, scripts for reliable repeated operations. |
| [OpenAI gh-fix-ci](https://github.com/openai/skills/blob/main/skills/.curated/gh-fix-ci/SKILL.md) | Narrow scope, concrete workflow, script for an actual integration problem and an explicit fallback. We do not inherit its task-specific approval process. |
| [Anthropic Claude Code skills](https://code.claude.com/docs/en/skills) | Standard format plus client extensions; installation and slash invocation differ. |
| [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | Evaluate realistic prompts, inspect outputs and iterate; test selection as well as task completion. |
| [Anthropic mcp-builder](https://github.com/anthropics/skills/blob/main/skills/mcp-builder/SKILL.md) | A larger procedural skill can route to language-specific references and evaluation guidance. Its full production workflow is not appropriate for every learning session. |

The Agent Skills specification also describes optional license, compatibility,
metadata and experimental allowed-tools fields. This repository needs none of
them to function. We intentionally keep the frontmatter smaller than the full
supported vocabulary. The project validator is stricter than the official
format, not an alternative specification.

## Architecture

The original four independent folders remain unchanged. The session skill repeats a small amount of essential
research, scope and tutoring logic so it survives being installed alone.
References are selected by need, not loaded as a whole manual. No shared
repository-relative dependency is required by a skill.

| Skill | Input | Observable output / stopping point |
| --- | --- | --- |
| tech-research | Goal or suitability decision, context, optional evidence | Decision-sized brief; stop at diminishing returns or budget |
| learning-roadmap | Goal, ability, time, research if available | Small milestones, scope buckets, next action |
| learning-coach | Goal or concept, learner attempt if available | One teaching/check turn; wait for the learner |
| learn-new-tech | Any stage of learning | The next necessary activity, then learner interaction |

A prose preference file fits the task better than a parser: the agent already
receives language, and there is no portable automatic configuration discovery
contract. Explicitly supplying a file also avoids ambiguous paths after a skill
is copied into another client. Default behavior needs no file.

## Long-term companion extension (2026-10-16)

A fifth independent skill adds learner-owned Markdown state. The official
specification and client docs above were rechecked: ordinary references and
bundled template assets suffice. The reviewed four skill bundles remain unchanged.

Templates live inside rafiq/assets/workspace-template so a single
copied folder works; no duplicate root template is needed. Two references separate
workspace/evidence policy from responsibility-transfer decisions.

Keep CHECKPOINT.md as a bounded resume point without scanning the archive.
Initialize only necessary files. Records, glossary and resources appear only
when justified. One mission per workspace avoids a global learner database.
Reuse stable preferences explicitly, not through hidden profile discovery.

Record evidence scope and assistance. Supersession preserves meaningful corrections;
explicit deletion overrides historical preservation. Independence is specific to
an activity and reversible. Direct help stays available. Review targets are
unscheduled recommendations.

New scenarios inspect state changes and tutor replies. See the
[companion evaluation report](../tests/behavioral/results/companion-2026-10-16.md)
for structural, simulated, native and retention coverage.

## Changes from the original proposed tree

Added docs for research provenance and client differences, a contribution guide,
and a standard-library validation script under tests. Omitted empty reference
folders: learning-coach is short enough to be self-contained. Replaced the
suggested YAML config with an optional Markdown example. Added no runtime scripts,
SDK, plugin manifest, tool dependency, package manager or fabricated skill runner.

## Evaluation strategy

Structural checks protect names, frontmatter, links and independently copyable
bundles. Behavioral cases examine decisions, waiting for attempts, hint escalation,
source honesty, realistic scope and preference adaptation. Fresh-context tests
receive prompts and skill files without answer rubrics. Human review grades their
actual replies. Results must distinguish simulations from live learner outcomes,
native client loading and delayed retention.

The initial development process is research → design → implementation → evaluation
and revision → finished documentation. The teaching process itself does not require
every stage on every request.
