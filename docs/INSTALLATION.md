# Install one canonical Rafiq skill

Checked against official documentation on 2026-10-19.
Install only the skill folder, not the entire repository as a skill. The required
layout is rafiq/SKILL.md with references/ and assets/ alongside it.

## Codex

The [official guide](https://learn.chatgpt.com/docs/build-skills) supports asking
the built-in installer for a repository skill:

~~~text
$skill-installer Install Rafiq from:
https://github.com/AdemCE-eng/Rafiq/tree/main/skills/rafiq
~~~

Invoke with `$rafiq`. Restart if discovery has not refreshed.

For a manual project install, copy the entire source skills/rafiq folder into
your learning project's .agents/skills/ folder. The final file must be
.agents/skills/rafiq/SKILL.md. Personal manual location: ~/.agents/skills/rafiq/.

The bundled installer manages its own destination; do not assume it uses the same
location as a manual copy. Check its completion message. Do not install duplicate
copies just because a skill picker has not refreshed.

## Claude Code

The [official guide](https://code.claude.com/docs/en/skills) documents
.claude/skills/rafiq/SKILL.md for a project, or ~/.claude/skills/rafiq/SKILL.md
for personal use. Copy the whole rafiq folder, then start Claude Code in the
learning project and invoke `/rafiq`.

If it is missing, check spelling and nesting, restart the session, and check
whether another installed skill has the same name. A copied SKILL.md without
its references/assets is incomplete.

## Exact local copy commands

Download and extract the repository ZIP, or use your existing checkout. Run
these commands **from its root**, not from inside skills/rafiq. They create a
project-scoped installation in that checkout, useful for rehearsal and local edits.
For another learning project, change only the destination to its absolute path.
The guards refuse to overwrite an existing installation.

PowerShell — Claude Code:

~~~powershell
$destination = Join-Path (Get-Location) '.claude/skills/rafiq'
if (Test-Path -LiteralPath $destination) { throw 'Already installed; compare before updating.' }
New-Item -ItemType Directory -Force -Path (Split-Path $destination) | Out-Null
Copy-Item -LiteralPath './skills/rafiq' -Destination $destination -Recurse
~~~

For Codex, replace `.claude/skills/rafiq` with `.agents/skills/rafiq`.

macOS/Linux shell — Claude Code:

~~~sh
destination='.claude/skills/rafiq'
if [ -e "$destination" ] || [ -L "$destination" ]; then
  echo 'Already installed; compare before updating.'
else
  mkdir -p .claude/skills
  cp -R skills/rafiq "$destination"
fi
~~~

For Codex, change both .claude paths to .agents. Installed copies are deployment
outputs, not another source implementation. Edit skills/rafiq, then compare and
replace your installation intentionally. Personal learning state belongs elsewhere.

## Claude browser / account skills

This is a separate product route, not the Claude Code folder installation.
The [official upload guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
describes this route: enable Code execution and file creation, open Customize →
Skills → + → Create skill → Upload a skill, select the ZIP, and enable it.
Organization policy may restrict availability; check the linked prerequisites.

Zip only the canonical rafiq folder, keeping rafiq/SKILL.md, references/, and assets/
inside it. Do not upload the repository ZIP, local learning-workspaces/, or work/.
For example, in PowerShell from the repository root, to an unused archive path:

~~~powershell
New-Item -ItemType Directory -Force -Path './work' | Out-Null
if (Test-Path -LiteralPath './work/rafiq-skill.zip') { throw 'Archive already exists.' }
Compress-Archive -LiteralPath './skills/rafiq' -DestinationPath './work/rafiq-skill.zip'
~~~

The [packaging guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
describes the containing skill folder. Uploading instructions is not uploading
your learner state or granting access to a local folder. Provide state explicitly,
download useful updates, and bring them to later sessions unless the actual host
offers and authorizes persistent file access. No browser upload or cross-session
persistence was live-tested here.

## Confirm a useful installation

1. Check that the host can select Rafiq and read a bundled reference.
2. Start with a harmless fictional topic and an unused workspace.
3. Ask for a hint and supply your own attempt; check that it waits for you.
4. Save, inspect the actual files, and start a new chat naming the same workspace.
5. Ask for a direct answer; it should not force a quiz.

This is a rehearsal checklist, not a claim those tests ran. See
[compatibility and verification boundaries](portability.md).
