# Companion extension evaluation — 2026-10-16

## Scope and method

The original four skill bundles were compared byte-for-byte against a pre-change
snapshot and remained unchanged. The review bundle and historical evaluation
artifacts were preserved. This evaluation covers the new independent companion,
its templates and integration, plus regressions of the existing session skills.

Three fresh evaluator contexts exercised fictional companion cases A-L in groups
of four. They received the skill, only their relevant fixture folders and learner
prompts, without rubrics or this implementation conversation. Filesystem reads and
writes were real, but the learners and past achievements were synthetic. Several
cases share an evaluator context; this is not twelve independent repeated trials.
The authoring agent reviewed replies and inspected actual file changes.

A fourth fresh evaluator produced 19 tutor replies to prescribed learner turns
for existing cases 1-12. These are scripted offline conversations, not actual
learner builds. A separate fresh evaluator checked selection from metadata for
six prompts. Native client loading was not tested.

The host identifies evaluators as Codex based on GPT-6; an exact model identifier
was not exposed. Windows/PowerShell and Python 3.13 were available. No behavioral
test browsed live sources or ran MCP, Docker or Kubernetes. Fixture writes outside
the initial sandbox used scoped execution permission; that is host enforcement,
not a permission capability supplied by the skill.

[Prompts, actual replies and state snapshots](companion-transcripts-2026-10-16.md)
are retained with machine-specific path prefixes replaced by neutral labels.
The new [case rubrics](../companion-cases.md) and
[existing rubrics](../cases.md) define the observable criteria.

## Structural checks

- All five skill entrypoints passed the bundled OpenAI skill-creator validator.
- Repository frontmatter, relative references, local links and bundle boundaries passed.
- Eleven fixture tests passed, including all six previous tests plus a standalone
  companion copy, missing template, obvious personal data, unsupported frontmatter,
  and escaping-path tests.
- The three blank templates were manually inspected. Automated privacy detection
  is a heuristic for obvious identifiers/paths, not a comprehensive privacy audit.
- Generated fixture evidence links resolve within their case workspaces.
- Git ignore matching protects the repository's default learning-workspaces path.
  It does not protect arbitrary paths or untrack previously committed data.
- Source text was checked with strict UTF-8 decoding. The historical REVIEW_BUNDLE
  retains its previously documented mojibake; it was not regenerated.

Commands from repository root:

```text
python tests/validate_repo.py
python -m unittest discover -s tests -p test_validator.py -v
```

The bundled creator checker is environment-specific and is not copied here.
The standalone copy test proves local package completeness, not native discovery.

## Companion results

All twelve base scenarios met their observed criteria. PASS here applies to the
specified synthetic interaction and inspected state, not an entire future workflow.

| Case | Observation | Result |
| --- | --- | --- |
| A coverage | Checkpoint says unassessed; no record or glossary created | PASS |
| B demonstration | Bounded unassisted explanation/test-design record, linked glossary, next transfer task; no execution claim | PASS |
| C resume | Used linked Oct 13 record, skipped basic discovery, offered boundary test; unrelated archive record not read | PASS |
| D fragile understanding | Preserved parameter observation, superseded unsupported implication, removed false glossary definition, left correction unassessed | PASS |
| E evidence not labels | Stored reported FastAPI experience and unassessed volumes/Compose; no global Docker rating | PASS |
| F independence | Asked learner to lead feature/version/source selection based on two prior demonstrations | PASS |
| G direct help | Explained directly without questions, gating, or new mastery record | PASS |
| H mission mutation | Mission byte-identical; only a deferred future topic saved | PASS |
| I ownership | Identified exact files and evidence types; surfaced stale checkpoint conflict without hidden-profile claims | PASS |
| J deletion/correction | Removed false claim from all three affected files, retained unrelated preferences/Python, no replacement history repeating the claim | PASS |
| K new mission | Created only mission/learner/checkpoint; copied authorized preferences; MCP workspace byte-identical | PASS |
| L first run | Asked about mathematical outcome and location; no workspace files created | PASS |

H's later acceptance variant and L's no-filesystem variant were not run. Full
workspace deletion, concurrent edits, symlink attacks, resource aging, and review
target selection remain further tests. Test harness before-state snapshots retain
fictional inputs for reproducibility; the companion did not create those backups
or preserve deleted learner claims in its case-J state.

## Existing regressions

Cases 1-12 retained the intended observable teaching decisions: small MCP scope,
structured foundations for beginner ML, narrow-feature scope, fundamentals-first,
source honesty, requested solutions, provisional orientation, preference override,
version uncertainty, exclusion of irrelevant Kubernetes, escalating hints with
transfer feedback, and honest deadline limits.

Coverage limits:
- Case 1 stopped after the schema explanation/attempt request; no tool was built.
- Case 8 used preferences supplied in the prompt, not all readable/unreadable file variants.
- Case 7 was offline, not a live research or stopping-rule evaluation.
- Case 11 exercised all five scripted turns through a correct changed example.
- Examples of commands were not executed; expected outputs are not observed results.
- Case 4 called a container a "running instance", an imprecise simplification for
  stopped containers. The scope/learning-path criterion passed; technical wording
  still merits real-client review. No existing skill was rewritten from one sample.

## Fresh-context discovery simulation

| Prompt | Selection |
| --- | --- |
| Write a production Dockerfile for this app, no tutoring | None |
| Summarize this article | None |
| Make a learning roadmap for my exam | learning-roadmap |
| Coach me through debugging | learning-coach |
| Continue my MCP mission using ./learning-workspaces/mcp | learning-companion |
| Teach me image versus container for this session | learning-coach |

All six matched the intended routing. Only names/descriptions were returned to
that evaluator's model context. Its shell command read complete files internally
before filtering, so this is a model-visible metadata test, not strict file-read
isolation. No skill bodies entered that evaluator's context. The earlier case-13
selection in the regression transcript shared context with session skill bodies;
this separate check avoids that model-context contamination. Neither is native
client discovery.

## Native and long-term limits

No native Codex/Claude installation or automatic discovery was exercised. No
actual learner retention, independence gains, or real three-day gap was measured.
The resume fixture's date difference is simulated. No statistical baseline,
multiple repetitions, background scheduler, remote publication or deployment ran.

Next tests: install the companion alone in both clients; create/save/reopen a real
mission; revisit after several days with a changed task; check ability with hints
removed while still allowing direct help; test explicit correction/deletion and
mission transitions; test resource freshness, read-only fallback and concurrent
learner edits. Use real learners and delayed transfer before making learning claims.

No commits, remotes or pushes were created by this implementation.

## Snapshot hashes

SHA-256 values below identify the final skill files used in this run.

```text
skills/learn-new-tech/references/learning-decisions.md bf26420b6fff2c98c9a01eac970f74276533682f7a7f9416a77942ecbbe96f12
skills/learn-new-tech/SKILL.md 11a13bc8d7f22cb10617f6a85a9f796a95149b1f04d73cbfe26a15b23d901f75
skills/learning-coach/SKILL.md aa79aa6a3d33eef6ec5ad04c49e8427029b7a4dcc070d40810d6ca9cfafe30cd
skills/learning-companion/assets/workspace-template/CHECKPOINT.md 382df75e27469b3dd31fb0def8086613463c4d15451e06340aceab6f791bb122
skills/learning-companion/assets/workspace-template/LEARNER.md 65cb56382f8e2eca257daaaa47848e547e6dfb684216c7322dc7239a1c9f4b1e
skills/learning-companion/assets/workspace-template/MISSION.md d3fc6d6b816f531711ba0d3348cf78e3b7af9cbd9d3343540b8902d4778b74b0
skills/learning-companion/references/independence.md a95ccdf41e97b0f13c5ea483c68d17710f67a9522c24bf07ebc23b8d0ad9160a
skills/learning-companion/references/workspace-state.md 9df137780cf4652a76f9b4d430acf3c87b7b1a95f4c58f2a77593352fcd051d8
skills/learning-companion/SKILL.md 72c26415d4ff00ee2adcc727e26888620c094a3ff455539938d85e4e69c82b2d
skills/learning-roadmap/references/path-decisions.md b0e87c2110b0aeae5b4eb3f148b01658099cdaf5141f4dba3d964b2d1e33225a
skills/learning-roadmap/SKILL.md aca2761e2a053e7ed94f4abb106efe89dae34a634224e14cdc2f68c7756c508c
skills/tech-research/references/evidence.md db0bd7035dec5fca5cc502e112859073b90732af33bfd2e088bd37a1cf2cdbfb
skills/tech-research/SKILL.md e79eb0043b25fd8377d9739ab9ead535fd14256b8274553ce78f1b219cf75ad6
```
