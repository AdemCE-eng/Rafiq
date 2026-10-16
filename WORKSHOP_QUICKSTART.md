# Your first learning session

An Agent Skill is a folder of instructions that helps an AI follow a workflow.
Choose how much continuity you want:

```text
QUICK SESSION                       LONG-TERM COMPANION
learn-new-tech                      learning-companion
one current journey                 your workspace across sessions
                                    mission -> evidence -> next session

Three focused options: tech-research | learning-roadmap | learning-coach
```

All five skills work independently. There are no automatic calls between them.

## Four companion layers

1. Learning engine: Research -> Roadmap -> Coach -> Build.
2. Learning memory: Mission -> Evidence -> Records -> Resume.
3. Learning experience: choose Chat / Visual / Interactive / Build / Reference.
4. Independence: Teacher -> Coach -> Reviewer -> Verifier, by evidence rather than levels.

Good information ≠ good learning. What the learner sees, manipulates, attempts,
builds, and revisits matters too. The medium should fit the learning objective.

## Install your mode in Codex

You need Codex and a local copy of this repository. In PowerShell, from the
repository folder, run:

```powershell
$skillName = 'learn-new-tech' # Or 'learning-companion' for saved learning state
$destination = Join-Path (Get-Location) ".agents/skills/$skillName"
if (Test-Path -LiteralPath $destination) { throw 'Already installed; compare before updating.' }
New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
Copy-Item -LiteralPath "./skills/$skillName" -Destination $destination -Recurse
```

Open this project in Codex and check the skill selector; restart if needed.
Copy the whole folder, including references and assets. For another project,
use its `.agents/skills/` folder. [Codex guidance](https://learn.chatgpt.com/docs/build-skills).

## Try it in Codex chat, not PowerShell

Quick session:

```text
$learn-new-tech Teach me how to containerize my FastAPI API locally. I know Python and FastAPI, have 60 minutes, and want hints before a full solution.
```

Long-term companion:

```text
$learning-companion Initialize ./learning-workspaces/mcp. I want to build and explain one local MCP tool. I know Python and APIs and have three hours a week. Save meaningful learning state here.
```

Later:

```text
$learning-companion Continue MCP using ./learning-workspaces/mcp. I have 30 minutes.
```

The companion records evidence, not everything it explains. It starts with a
small mission/checkpoint and adds files only when useful. Open, correct or delete
your Markdown state whenever you want. Use a separate folder for a new mission.
`learning-workspaces/` is ignored here; check other locations before publishing.
No hidden memory or automatic reminders are required.

## Demonstrate the MCP progression

Use comparable goals and make the differences visible without promising outcomes:

| Mode | What to look for |
| --- | --- |
| Ordinary AI: "Teach me MCP" | May give a polished generated mini-course; compare actual behavior |
| learn-new-tech | Goal-aware scope, attempts and adaptive feedback for this session |
| learning-companion | Readable records of demonstrated learning and a resume point |
| Experience layer | A short responsibility-flow lesson when useful, followed by real Python |
| Over time | Learner proposes sources, models, plans, and verification when evidence supports it |

In a fresh workspace, try:

```text
$learning-companion Initialize ./learning-workspaces/mcp-demo. I want to understand
MCP well enough to use it confidently in my AI-agent projects. I know Python,
REST APIs, and tool calling. I prefer interactive and visual learning when it helps.
```

Look for a small mental-model artifact in `lessons/`, a shared stylesheet in
`assets/`, and a checkpoint linking the pending learner action. Open the HTML in a
normal browser. Predict who decides, communicates, and executes, then try a changed
scenario. Bring your explanation back to the companion before building the Python
function. A completion click alone should create no learning record.

The folders are created only when useful. Later lessons should reuse appropriate
assets; lookup material belongs in `reference/` only when future use warrants it.
No CDN, framework, or package manager is required for an ordinary lesson. If you
prefer text today, say so. Real coding should follow the conceptual preparation,
not be replaced by a fake browser coding exercise.

Use the [experience cases](tests/behavioral/experience-cases.md) and
[local validation report](tests/behavioral/results/experience-2026-10-16.md)
to separate observed behavior from untested teaching effectiveness. The purpose
remains increasing the learner's ability to learn without AI.

## Make it fit you

No configuration is required. Say:

- Research: "Use official docs and repositories, at most three sources; flag uncertainty."
- Roadmap: "Fundamentals first, three initial topics, and show what can wait."
- Coaching: "Hints first; check at milestones. Today I need a direct worked example."

For reusable preferences, adapt [the example](config/learner-preferences.example.md)
and explicitly ask the agent to read it. Companion mode can keep supplied useful
preferences in LEARNER.md. Your current request takes priority.

As evidence grows, you can choose sources and propose plans while the AI reviews
them. Direct help stays available. The aim is to need less help over time.

## Make your own version

Once published, use GitHub's Fork button and clone your fork; for now customize
this local copy without publishing. Start with preferences. Edit the relevant
`SKILL.md` and references for reusable behavior changes. Each skill is independent:
edits to the small skills do not automatically change either main mode.
Re-copy changed folders into the client discovery location.

Run `python tests/validate_repo.py` before sharing. Never publish personal history
by accident. See [companion examples](examples/companion-sessions.md) and
[contributing](CONTRIBUTING.md).
