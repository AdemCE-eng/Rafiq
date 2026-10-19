# Portability and verification boundaries

Checked 2026-10-19. One canonical implementation under skills/; installation copies
and ZIPs are packaging outputs, not separately maintained instructions.

## Official sources

- [Agent Skills specification](https://agentskills.io/specification): required
  name/description, directory format, optional resources, progressive disclosure.
- [OpenAI skills documentation](https://learn.chatgpt.com/docs/build-skills):
  local discovery, explicit/implicit selection, installer, optional metadata.
- [Claude Code skills documentation](https://code.claude.com/docs/en/skills):
  skill folders, frontmatter, invocation, nested project discovery and extensions.
- [Claude custom upload](https://support.claude.com/en/articles/12512180-use-skills-in-claude):
  account upload requirements and UI; separate from local filesystem installation.

## Shared format and differences

| Concern | Rafiq / shared core | Codex | Claude Code |
| --- | --- | --- | --- |
| Entrypoint | Folder containing SKILL.md | name and description for discovery | Current docs permit omitted fields; Rafiq supplies both |
| Portable metadata | Specification requires name and description; matching lowercase folder name | Supported | Supported; no additional field needed here |
| Resources | Relative links inside each bundle; no sibling dependency | Read as needed | Read as needed |
| Project path | Installation detail | .agents/skills/rafiq/ | .claude/skills/rafiq/ |
| Personal manual path | Installation detail | ~/.agents/skills/rafiq/ | ~/.claude/skills/rafiq/ |
| Explicit selection | Host-specific | $rafiq | /rafiq |
| Optional extensions | Not used by Rafiq | agents/openai.yaml | context: fork, allowed-tools, invocation controls and argument substitutions |
| Tools and persistence | Not granted by SKILL.md | Host tools/permissions | Host tools/permissions |

No platform-specific adaptation file is required for these instructions.
OpenAI recommends plugins for broader distribution; this repository retains
documented local skill installation without introducing a plugin runtime.

## Discovery is not delegation

Codex scans project skill locations from the working directory toward the repo
root. Claude Code supports project and nested-project skill locations. These
discovery mechanisms do not mean a skill directory is a portable child-agent
system. Rafiq's references/ directory is supporting text, not nested skills.

Clients may support invocation tools or subagents; Rafiq does not rely on them.
Its research, planning, and coaching are activities within the selected skill.
The four supporting skill folders remain optional, independent entrypoints.
Explicit selection is useful when descriptions overlap.

## State and other product surfaces

A local workspace is a Rafiq convention. Neither installation path creates a
learner database. State requires authorized files that remain available across
sessions. A shared filesystem allows Codex and Claude Code to use the same
learner-owned folder; read current edits and avoid concurrent overlapping writes.

Claude browser uploads use the same bundle in a ZIP but do not establish access
to a chosen local folder. Supply/download state explicitly when durable files
are unavailable. See [installation](INSTALLATION.md) for the supported upload route.

ChatGPT, Cowork, cloud runs, and API containers have their own packaging and
storage arrangements. A local copy is not evidence it is installed on those
surfaces. Rafiq includes no hosted service or plugin integration for them.

Preferences in config/ are optional prose supplied by the user. No automatic
config parser or shared state handoff is assumed. Host instruction priority,
tool permissions, and data policies still apply.

## What has actually been verified?

- Current format and documented installation conventions: inspected against the sources above.
- Local structure, complete resources, and independent installation layouts: checked by repository tests.
- Previous public Codex installer download: recorded in the earlier release work;
  it verifies packaging, not tutoring quality.
- Claude Code runtime: NOT TESTED here; no Claude executable is installed.
- Claude account upload, account synchronization, and persistence: NOT TESTED.
- Native routing, changed state behavior, and real delayed learning: require separate live tests.

No claim of identical client behavior follows from a shared format. In Claude,
tool access, working directory, approval settings, account skill collisions, and
available browser/file capabilities may change what Rafiq can do. Use an explicit
workspace and validate the actual installation before a presentation.
