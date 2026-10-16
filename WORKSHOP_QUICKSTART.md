# Rafiq

Learn how to learn.

[github.com/AdemCE-eng/Rafiq](https://github.com/AdemCE-eng/Rafiq)

Rafiq is an adaptive learning companion. An Agent Skill is a folder of instructions
that helps your AI follow a workflow. Start with Rafiq; no knowledge of the
supporting skills is needed.

## Install in Codex

Paste into Codex chat:

~~~text
$skill-installer Install Rafiq from:
https://github.com/AdemCE-eng/Rafiq/tree/main/skills/rafiq
~~~

Try it on your next turn; restart Codex if discovery has not refreshed.

## Start a mission

~~~text
I want Rafiq to help me learn MCP.
My goal is to build and explain one local tool.
I already know Python and APIs. I have 60 minutes today.
I prefer hints and visual explanations when they help.
Keep my learning state in ./learning-workspaces/mcp where I can inspect and edit it.
Let's start.
~~~

Later, say: "Rafiq, continue from ./learning-workspaces/mcp. I have 30 minutes."

Rafiq chooses what matters now, invites an attempt, and adapts from evidence.
It can switch between chat, visuals, and real practice. A clicked answer is not
proof of learning. You can inspect, correct, or delete your Markdown state.

~~~text
Rafiq: goal -> research -> small path -> practice/build -> evidence -> resume
                          ^                                   |
                          +---------- learn the gap <---------+

Advanced standalone options:
tech-research -> learning-roadmap -> learning-coach
learn-new-tech: one learning journey without persistent state
~~~

These are learning activities, not automatic calls between skills.

## Make it fit you

No configuration needed. Tell Rafiq:

- Research: "Prefer official docs and papers when relevant; at most three sources."
- Roadmap: "Fundamentals first, three initial topics, and show what can wait."
- Coaching: "Hints first; check at milestones. Today I need a worked example."

For reusable preferences, adapt [the example](config/learner-preferences.example.md)
and ask Rafiq to read your copy. Your current request takes priority.

## Make it yours

Use GitHub's **Fork** button, then clone your fork. Start with preferences; edit
skills/rafiq/SKILL.md or its references for reusable behavior changes. Reinstall
from your fork after changes. The four standalone skills remain independent.

Run python tests/validate_repo.py before sharing. Keep personal learning state
private: this repository ignores learning-workspaces/, but check staged files.
See the [README](README.md) for manual installation and client differences.
