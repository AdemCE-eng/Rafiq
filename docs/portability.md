# Portability and client boundaries

Checked 2026-10-16 against the [format specification](https://agentskills.io/specification),
[OpenAI documentation](https://learn.chatgpt.com/docs/build-skills), and
[Claude Code documentation](https://code.claude.com/docs/en/skills).

| Concern | Portable core | Codex | Claude Code |
| --- | --- | --- | --- |
| Definition | Folder with SKILL.md | Supported | Supported |
| Discovery metadata | name and description | Used for selection | Used for selection |
| Supporting files | Relative references/resources | Host reads when needed | Host reads when needed |
| Local project discovery | Host-specific | .agents/skills | .claude/skills |
| Personal local discovery | Host-specific | ~/.agents/skills | ~/.claude/skills |
| Explicit use | Host-specific | $skill-name | /skill-name |
| Extra controls | Not needed here | Optional agents/openai.yaml | Frontmatter extensions such as context: fork and disable-model-invocation |
| Tools/network | Not supplied by a Markdown skill | Host capabilities and policy | Host capabilities and policy |

Claude Code has a Skill tool and subagent-related extensions; they do not establish
a portable cross-skill RPC contract. Codex metadata and Claude context/argument
features are intentionally absent from these skills. 'Orchestrator' here means
instructional routing within one skill, not an executable multi-agent scheduler.

OpenAI's current docs recommend plugins for broader distribution. This repository
deliberately remains a locally installable source toolkit for review; a plugin can
be added later as a separate, client-tested packaging layer. It has no marketplace
registration or remote installation requirement.

The table describes local Codex and Claude Code. Do not assume local personal
folders sync to web products, cloud sessions, Cowork, or API containers. Consult
the relevant product's current documentation before packaging for those targets.

The config folder is entirely our convention. Neither client is expected to parse
it or load it automatically. Explicitly attach/paste the preferences or name a
readable path. Source links, ordinary textual handoffs, learning checkpoints and
evaluation formats in this repository are not new Skill protocol fields.

The Rafiq workspace is a project convention, not official Skill
functionality. Persistence requires authorized read/write access to a learner-named
folder. With no filesystem, supply state and save proposed updates yourself.
No hidden memory, profile discovery, scheduler or sibling skill is assumed.
Templates are bundled inside the skill. Official conventions were rechecked on
2026-10-16; this design needs no client-specific extensions.

Native discovery and automatic trigger behavior must be tested separately from
manual loading. Updating source folders does not update installed copies.
