# Rafiq

An adaptive learning companion that helps you learn new technologies and topics
through goal-first learning, real practice, evidence-based progress, and gradually
reduced AI scaffolding.

**Good information ≠ good learning.**

A polished answer is not evidence that you can apply it. Rafiq starts with your
goal and current ability, chooses what matters now versus later, and adapts from
your attempts. It can use concise chat, visual or interactive lessons, coding,
building, debugging, and reference material when each helps the current objective.

Your learning state stays in readable files you can inspect, edit, or delete.
Rafiq records demonstrated evidence instead of vague ability labels, helps you
resume later, and gradually returns planning, research, debugging, and verification
to you. Its goal is to make you increasingly capable of learning without it.

## Quick Start - Codex

### 1. Install the skill

Codex includes `$skill-installer`. Paste this into Codex:

```text
$skill-installer Install Rafiq from:
https://github.com/AdemCE-eng/Rafiq/tree/main/skills/rafiq
```

Or ask in natural language:

~~~text
Install the Rafiq skill from:
https://github.com/AdemCE-eng/Rafiq/tree/main/skills/rafiq
~~~

The installed skill is available on your next turn. If it does not appear, restart
Codex. This workflow follows the current [official Codex skills guidance](https://learn.chatgpt.com/docs/build-skills).

### 2. Start learning

Paste this into Codex and replace the bracketed text:

```text
I want Rafiq to help me learn [topic].

My goal is:
[goal]

I already know:
[background]

I prefer:
[learning preferences]

Keep my learning state in this project where I can inspect and edit it.

Let's start.
```

The companion can adapt to what you already know, choose chat, visual lessons,
interactive work, coding, or references, save learner-owned state, resume later,
record demonstrated evidence instead of vague mastery labels, and gradually give
you more responsibility.

## How Rafiq works

| Layer | What it does |
| --- | --- |
| Learning Engine | Research -> Roadmap -> Coach -> Build |
| Learning Memory | Mission -> Evidence -> Records -> Resume |
| Learning Experience | Chat / Visual / Interactive / Build / Reference, chosen for the current concept |
| Independence | Teacher -> Coach -> Reviewer -> Verifier |

The [experience decision rules](skills/rafiq/references/learning-experience.md)
add a choice of medium to the companion; the four original session skills remain unchanged.

## Goal-first, not automatically course-first

Goal → assess relevant knowledge → learn necessary prerequisites → research when
needed → practice and build → detect gaps → learn those gaps → continue.

This is a decision loop, not a mandatory pipeline. Already know the architecture
and need one feature? Start with the feature. Unsure whether a technology fits?
Investigate before implementing.

**The goal is not to avoid courses.** It is to avoid automatically treating a
complete course as the only way to learn every technology. Courses, books and
structured curricula are often better for broad competence, cumulative
foundations, exam preparation and sustained practice. Fundamentals-first is a
supported preference, not a mistake to correct.

## Advanced / standalone skills

Start with **Rafiq** for the complete student experience. The other
skills are useful when you want one specific part of the workflow.

| Skill | Use it for | Expected behavior |
| --- | --- | --- |
| [tech-research](skills/tech-research/SKILL.md) | Orientation or a technology decision | A brief with claim-linked evidence, relevant terms, limits and a stopping rule |
| [learning-roadmap](skills/learning-roadmap/SKILL.md) | Choosing what to learn | NOW / LATER / NOT NEEDED FOR THIS GOAL, realistic milestones and prerequisite decisions |
| [learning-coach](skills/learning-coach/SKILL.md) | Interactive teaching and practice | One meaningful concept, a learner attempt, targeted feedback and adaptive hints |
| [learn-new-tech](skills/learn-new-tech/SKILL.md) | One current journey | Choose only the activities needed; research, plan and coach directly |

Install only the folder you need. Each skill works independently;
`rafiq` does not programmatically invoke the others.

## Manual installation

Advanced users can copy a whole individual skill folder, including its references
and assets, to a supported client location.

| Client | Project location | Personal location | Explicit invocation |
| --- | --- | --- | --- |
| Codex | `.agents/skills/<name>/` | `~/.agents/skills/<name>/` | `$rafiq` |
| Claude Code | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` | `/rafiq` |

Verified against [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills)
and [Claude Code documentation](https://code.claude.com/docs/en/skills) on
2026-10-16. These are local CLI/project instructions; web/API products may require
different packaging. See [portability notes](docs/portability.md).

For example, from this repository root, install one skill into this project's
Codex discovery folder with PowerShell:

```powershell
$destination = Join-Path (Get-Location) '.agents/skills/rafiq'
if (Test-Path -LiteralPath $destination) { throw 'Destination already exists; compare before updating.' }
New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
Copy-Item -LiteralPath './skills/rafiq' -Destination $destination -Recurse
```

For Claude Code, change `.agents` to `.claude`. For another project, use that
project's absolute destination. Repeat for other skill names if wanted. Copies
do not update automatically: compare and replace deliberately after source edits.
These local installation copies are ignored by this repository's Git configuration.

Open the client in the destination project. Confirm the skill appears in its skill
selector; restart if discovery has not refreshed. Then invoke it explicitly:

```text
$rafiq I want to understand MCP by building one local tool. I know
basic Python, prefer hints, and want my progress saved in this project.
```

In Claude Code use `/rafiq` instead. Natural-language selection can also
work, depending on the client and available skill descriptions.

Without a Skills-aware client, supply the contents of the relevant `SKILL.md`
and any requested reference files as ordinary instructions. This is a manual
fallback, not a native installation or a guarantee of equivalent behavior.

## A companion that helps less over time

The best learning assistant should need to help you less over time. Technologies
change; the ability to choose sources, plan, verify and learn remains. The goal is
to become better at learning without an AI tutor, while keeping help available.

`learn-new-tech` optimizes the current journey without a persistent learner store.
`rafiq` uses a folder you own to continue a substantial mission.
It performs learning activities directly, without calling sibling skills.

```text
                  Learner state
                       |
                       v
                     Mission
                       |
                       v
Research -> Roadmap -> Experience -> Build
    ^                      |
    |                      v
    +--------- gaps <- Evidence
                       |
                       v
                 Learning records
                       |
                       v
                  Next session
```

Teacher -> coach -> reviewer -> verifier -> optional companion is a direction,
not fixed levels. Good source choices can justify letting you propose sources;
they do not prove independent debugging ability. Direct help and fundamentals-first
learning remain available.

### Start and resume

Install `rafiq` using the copy instructions above with that skill
name. In Codex chat:

```text
$rafiq Initialize ./learning-workspaces/mcp. I want to build and
explain one local MCP tool for my agent project. I know Python and APIs, have
three hours a week, and prefer hints. Save meaningful learning state here.
```

Later:

```text
$rafiq Continue MCP using ./learning-workspaces/mcp. I have 30 minutes.
```

Paths are relative to your project, not the installed skill; use an absolute path
when ambiguous. No workspace yet? Clarify the mission and location first.
Without file access, supply state and save clearly labeled proposed updates yourself.

### Your learning files

Start small: MISSION.md, CHECKPOINT.md, and LEARNER.md only when supplied context
is useful. Evidence creates learning-records/; demonstrated terms and useful
sources create GLOSSARY.md and RESOURCES.md later.
[Templates and state rules](skills/rafiq/references/workspace-state.md)
live inside the independently installable skill.

Records distinguish demonstrated performance, reported experience and unknowns,
including assistance used. Coverage is not learning: hearing an explanation
does not earn a mastery record. Later evidence can supersede earlier conclusions.
CHECKPOINT is a short resume point, not a duplicate of the whole archive.

When a concept benefits from a visual flow or immediate feedback, the companion
may create `lessons/0001-short-topic.html` with shared files in `assets/`. Later
lessons reuse appropriate components. Compressed lookup material goes in
`reference/` only when useful; the existing glossary remains canonical. None of
these folders is required at initialization. Ordinary lessons use local HTML,
CSS, and vanilla JavaScript, without a build step or mandatory network access.
Keyboard controls and explanatory feedback matter more than decorative polish.
Opening or completing a lesson is not automatically learning evidence.

For example, MCP responsibility boundaries may benefit from a short interactive
flow and a changed scenario. Implementing `search_notes()` then belongs in real
Python. A tiny `strip()` explanation usually needs only chat/code. Say "No HTML
today" or "Let me draw the model first" to steer the experience.

Open the Markdown files in any editor. Ask the companion to show what it knows,
correct a claim, or remove state. You can edit or delete the files yourself.
Explicit deletion overrides preserving history; removed facts must not be secretly
restored. Local deletion does not erase host chat logs, backups or published Git history.

Use one folder per substantial mission, such as MCP and Kubernetes. Keep old
folders when pausing; reuse only explicitly supplied/authorized stable preferences.
Review targets are suggestions for your return, not scheduled reminders.
Nothing runs between sessions.

Use a private location for personal state. This repository ignores
`learning-workspaces/`; custom paths need their own protection. Gitignore does
not untrack previously committed files. Inspect staged changes before publishing
a fork so you do not expose personal learning history.

See [five fictional companion sessions](examples/companion-sessions.md) and the
[workshop quickstart](WORKSHOP_QUICKSTART.md).

## Customize how you learn

No configuration is required. Say:

> I learn better through projects and don't want long videos.

Or:

> When researching AI topics, prioritize papers and official repositories.
> Give me a fundamentals-first explanation and assess me at milestones.

For reusable preferences, adapt [the Markdown example](config/learner-preferences.example.md)
and explicitly ask the agent to read your copy. See [the convention](config/README.md).
There is no YAML parser, automatic config discovery, schema extension, or hidden
memory. Latest explicit session preferences override a supplied preference file.

## Examples

- [MCP in 60 minutes](examples/learn-mcp.md): one local tool, a tiny path and an actual attempt.
- [Docker tonight](examples/learn-docker.md): containerize a stateless FastAPI API; defer orchestration.
- [WebGPU fit assessment](examples/learn-webgpu.md): orient and investigate before writing shaders.

Examples are authored illustrations, not execution logs or proof of learning.
They avoid pinning an SDK implementation that will silently become stale.

## Fork and contribute

Edit the relevant skill's decision rules and optional references. Keep each skill
independently installable; avoid links to sibling skills or repository-only config
files from inside a skill. Change the preference example for personal style;
change a skill when you want a reusable behavioral rule.

Run the local structural check with Python 3.10+ (standard library only):

```text
python tests/validate_repo.py
```

Then run [behavioral scenarios](tests/behavioral/cases.md) in fresh chats. Compare
actual learner interactions, not matching headings or keywords. Read
[CONTRIBUTING.md](CONTRIBUTING.md) for the review process and
[the initial evaluation report](tests/behavioral/results/2026-10-16.md) for what
has and has not been tested.

## Design and limits

- Portable YAML frontmatter contains only name and description. Supporting
  Markdown stays inside each skill; tools and cross-skill calls are not assumed.
- UNKNOWN knowledge is not the same as NOT NEEDED YET.
- Hints are the default, but direct answers and complete demonstrations remain
  available when requested.
- Browsing and code execution depend on the host. Without evidence, technical
  guidance must be labeled provisional; the skills cannot make a model infallible.
- Time estimates are planning aids, not mastery guarantees. Real learning needs
  learner effort and delayed transfer checks.
- No account system or remote learner database is included. Companion mode writes
  learner-authorized readable local state; the host has its own data handling.
  The session skills do not silently create that state.
- Local evaluations do not certify every model, client or native installation.
  Structural checks do not measure pedagogy or real long-term retention.
  See [companion evaluation](tests/behavioral/results/companion-2026-10-16.md).

See [research and design decisions](docs/research-and-design.md) and
[client differences](docs/portability.md). Original repository content is
[MIT licensed](LICENSE). External references keep their own licenses.
