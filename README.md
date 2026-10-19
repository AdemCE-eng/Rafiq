# Rafiq

A learning companion that helps you understand, practice, and gradually learn more independently.

## What is Rafiq?

Rafiq starts with your goal and what you already know. It explains a useful idea,
invites you to try, gives feedback, and chooses the next step from your response.

**Good information ≠ good learning.** Reading an excellent answer is different
from explaining or applying the idea yourself.

Rafiq is an **Agent Skill**: a folder of instructions and supporting files that
a compatible AI assistant reads. You use it inside Codex or Claude Code; it is
not a separate app or a new AI model. You do not need to understand its files to start.

## What makes it different?

- Start from a goal, rather than automatically assigning a whole course.
- Use your existing knowledge and separate what matters now from what can wait.
- Offer hints and practice before solving the whole task; give a direct answer when requested.
- Change the explanation or medium when you are stuck; use visuals only when useful.
- Save useful progress in files you own, when you request it and file access is available.
- Gradually let you choose sources, plan, test ideas, and verify answers yourself.

Courses and books still matter. Broad subjects, exams, and missing foundations
may need structured study. A small project is not always the best starting point.

## Quick Start

You need access to one supported host below. Its account, installation, tools,
and permissions are separate from Rafiq. Start with **only Rafiq**; the other
four skills are optional.

### Codex

Open Codex in the project where you want to learn. Paste into **Codex chat**,
not your terminal:

~~~text
$skill-installer Install Rafiq from:
https://github.com/AdemCE-eng/Rafiq/tree/main/skills/rafiq
~~~

Then select Rafiq using the skill picker or type `$rafiq` before your learning
request. If it is not visible, restart Codex.
[Official Codex instructions](https://learn.chatgpt.com/docs/build-skills).

Prefer a local installation or need this checkout's unpublished edits?
Use the [manual installation steps](docs/INSTALLATION.md).

### Claude / Claude Code

For **Claude Code**, download this repository from
[GitHub](https://github.com/AdemCE-eng/Rafiq) using **Code → Download ZIP** and
extract it. Open a folder for your learning project.

1. Inside that project, create `.claude/skills/`.
2. Copy the **whole** `skills/rafiq` folder from the extracted repository into it.
3. Confirm the result is `.claude/skills/rafiq/SKILL.md`, with `references/` and
   `assets/` beside that file.
4. Open Claude Code in the learning project and type `/rafiq` followed by your request.

These are the documented Claude Code folder and invocation conventions.
[Official Claude Code instructions](https://code.claude.com/docs/en/skills).

Using **Claude in the browser** instead? It has a separate custom-skill ZIP upload
route. Follow [installation and memory limits](docs/INSTALLATION.md); it does not
automatically gain access to your computer's learning folder.

Compatibility here means the format and installation layout match current official
documentation. It does **not** mean identical model behavior or a completed live
Claude test. See [verification details](docs/portability.md).

## Start Learning

After selecting Rafiq, use your own words or fill this in:

~~~text
I want to learn [topic].
Why: [reason]
I already know: [background, or "I'm new to this"]
By the end, I want to: [observable goal]
I have [time] and prefer [how you like to learn].
~~~

For example:

~~~text
I want to learn Digital Twins.
Why: I want to know whether they could help monitor energy usage in a university building.
I already know basic IoT concepts.
By the end, I want to decide whether a Digital Twin is appropriate for this use case.
I have 30 minutes. Explain unfamiliar terms and let me try a small example.
~~~

For saved progress, add:

~~~text
Keep useful learning state in ./learning-workspaces/digital-twins.
Explain what you save so I can inspect and edit it.
~~~

If you only want a conversation, say "No saved state today." A vague interest
should not create a pile of files. Rafiq may ask for a clearer goal or location.

## What happens next?

~~~text
Goal → current knowledge → learn → try → feedback or hint → retry
                                                        ↓
                                     evidence of understanding → next step
~~~

Rafiq chooses the activities you need, rather than running every stage every time.
It might ask one focused question, explain one distinction, or invite a prediction.
It should then wait for your answer.

If you are stuck, say what feels unclear. Rafiq can simplify the task, use another
example, change medium, or teach a missing prerequisite. If you need a full worked
answer, ask for it. Seeing that answer does not count as independently solving it.

## Memory / Learning Progress

Rafiq's learning memory is **ordinary files in the folder you choose**.
It is a project convention, not a built-in memory database.

| File in your learning folder | What it holds |
| --- | --- |
| MISSION.md | Why you are learning, your goal, constraints, and what is out of scope |
| CHECKPOINT.md | Where to resume, the current gap, evidence links, and your next action |
| LEARNER.md, when useful | Relevant background you report and preferences you supply |
| learning-records/, when justified | Short records of specific attempts, reasoning, help used, and implications |
| GLOSSARY.md / RESOURCES.md, when justified | Demonstrated meanings / useful sources with trust and freshness context |

The first two files may be enough to start. Optional lessons and references are
teaching material, not proof that you learned them. A click, confidence statement,
or explanation you only read must not become a mastery record.

Open these files in any text editor. Correct them yourself or ask Rafiq to correct
a specific claim. To reset, delete the chosen learning folder or ask Rafiq to
remove that exact folder after confirming its location. Start the next session
with "Start fresh; do not reconstruct my deleted state."

To resume in a new chat, select Rafiq and say:

~~~text
Continue using ./learning-workspaces/digital-twins. I have 20 minutes.
~~~

There is no automatic cross-chat folder search. Without file access, supply the
state and save clearly labeled proposed updates yourself.

Rafiq does not need a full conversation transcript, personality profile, credentials,
or unrelated personal history. Files may nevertheless contain personal information.
The host processes prompts and files under its own policies; local files do not
mean an offline or private model. Deleting them does not erase chat logs, backups,
cloud sync, or Git history. Prefer a private folder. This repository ignores
`learning-workspaces/`; other projects need their own protection.

[State schema and rules](skills/rafiq/references/workspace-state.md).

## Examples

All examples are authored illustrations, not measured learning outcomes.

- [Technical beginner: Digital Twins](examples/learn-digital-twins.md): decide what to investigate, then change medium when a distinction remains confusing.
- [Academic study: fractions](examples/learn-fractions.md): receive a hint, attempt the reasoning, and explain a changed example.
- [Practical skill: a short presentation](examples/learn-presentation.md): draft, get feedback, revise, and distinguish a written draft from observed delivery.

Developer examples remain available:
[MCP](examples/learn-mcp.md), [Docker](examples/learn-docker.md),
[WebGPU](examples/learn-webgpu.md), and
[continuing sessions](examples/companion-sessions.md).

## How Rafiq Works

The host selects a skill from its name and description, then reads its instructions
and relevant supporting files. Rafiq performs research, planning, and coaching
itself. It **does not call the other skills**.

| Skill | Use it for |
| --- | --- |
| [rafiq](skills/rafiq/SKILL.md) | A continuing learning mission with optional learner-owned state |
| [tech-research](skills/tech-research/SKILL.md) | A concise technology research or suitability brief |
| [learning-roadmap](skills/learning-roadmap/SKILL.md) | A sensible path with NOW, LATER, and excluded topics |
| [learning-coach](skills/learning-coach/SKILL.md) | A focused teaching and practice interaction |
| [learn-new-tech](skills/learn-new-tech/SKILL.md) | A technology-learning journey without an automatic persistent workspace |

Each installs independently. The overlap keeps standalone installation working;
there is no shared runtime or automatic state transfer.

Read [how Rafiq works](docs/HOW_RAFIQ_WORKS.md) for responsibilities, a diagram,
and state flow. Presenting it? Use the [presenter guide](docs/PRESENTER_GUIDE.md)
or the [workshop quickstart](WORKSHOP_QUICKSTART.md).

## Customize and contribute

Say "Fundamentals first," "Use primary sources," "No HTML today," or "Check only
at milestones." No configuration is required. For reusable preferences, adapt
[the example](config/learner-preferences.example.md) and explicitly ask Rafiq to
read your copy. [Preference convention](config/README.md).

Fork the repository and edit the canonical skill or its references for reusable
behavior changes. Updating this checkout does not update an installed copy:
compare and deliberately reinstall it. Avoid keeping competing copies of one skill.

With Python 3.10+, run:

~~~text
python tests/validate_repo.py
python -m unittest discover -s tests -p "test_*.py"
~~~

Then exercise relevant [behavioral cases](tests/behavioral/README.md) in the target
client. Structural checks do not prove tutoring quality, native selection, or
long-term retention. See [review and validation](docs/FINAL_REVIEW.md),
[contribution guidance](CONTRIBUTING.md), and [research history](docs/research-and-design.md).

Rafiq cannot guarantee factual correctness, learning outcomes, tool availability,
or persistent storage in every host. No scheduler, background activity, proprietary
model, or remote learner database is included. Original content is [MIT licensed](LICENSE).
