# Rafiq

Learn how to learn.

[github.com/AdemCE-eng/Rafiq](https://github.com/AdemCE-eng/Rafiq)

An Agent Skill is a folder of instructions your AI assistant can use.
Rafiq helps you learn a useful idea, try it, get feedback, and continue.

## Install once

**Codex chat:**

~~~text
$skill-installer Install Rafiq from:
https://github.com/AdemCE-eng/Rafiq/tree/main/skills/rafiq
~~~

Then select `$rafiq`; restart if it is not visible.

**Claude Code:** Copy the complete skills/rafiq folder into your learning project's
.claude/skills/ folder, then use `/rafiq`.
[Step-by-step installation, including browser Claude](docs/INSTALLATION.md).

## Start

After selecting Rafiq, paste:

~~~text
I want to understand adding fractions so I can explain it to a classmate.
I can add whole numbers. I have 20 minutes.
Use hints before answers and let me try.
Keep useful learning state in ./learning-workspaces/fractions so I can inspect it.
~~~

~~~text
Goal → learn → your attempt → feedback → retry → evidence → next step
~~~

Show your reasoning. Ask for a different explanation if stuck. A direct worked
answer is available when you ask. For a later session, name the same workspace.

## Make it yours

Say "Fundamentals first," "Use primary sources," "No HTML today," or
"Check only at milestones." No configuration is required.

Advanced options are independent skills:
tech-research (brief), learning-roadmap (path), learning-coach (practice),
and learn-new-tech (current technology journey). Rafiq does not call them.

Fork the repository to edit reusable rules; reinstall deliberately after edits.
Keep personal learning files private. [Preferences](config/README.md) /
[full README](README.md) / [presenter guide and live demo](docs/PRESENTER_GUIDE.md).
