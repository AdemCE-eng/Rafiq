# Experience-layer validation — 2026-10-16

## Change boundary

Only the companion's experience selection has been extended. Original mission,
evidence records, resume behavior, ownership, and independence policy remain in
place. Byte-for-byte SHA-256 comparisons confirm all files in the original four
skill bundles remain unchanged, with no added files in those bundles. Templates
and independence.md are unchanged. No commit, push, publication, repository, or
remote configuration was created.

Added distribution files:
- `skills/learning-companion/references/learning-experience.md`
- `tests/behavioral/experience-cases.md`
- `tests/behavioral/results/experience-author-replay-2026-10-16.md`
- This report.

Changed distribution files:
- `skills/learning-companion/SKILL.md`: route to experience guidance and explicitly exclude completion/guessed answers from evidence.
- `skills/learning-companion/references/workspace-state.md`: lazy artifact directories and distinct artifact/evidence checkpoint links.
- `README.md`: four layers, experience/memory loop, medium choices and workspace conventions.
- `WORKSHOP_QUICKSTART.md`: four layers, demo progression and visual MCP starting prompt.
- `tests/behavioral/README.md`: route to new experience scenarios.

## Decision rule

1. Honor current medium, time, accessibility and artifact constraints.
2. Use evidence to choose whether learner or companion proposes the model/source/experiment first; direct help remains available.
3. Prefer authentic coding, terminal, build or debugging practice for the target skill, with brief conceptual preparation only where useful.
4. Choose visual/interactive work when structure, comparing states/flows, cause/effect, explanatory feedback across examples or a reusable model materially improves learning enough to justify creation/navigation cost.
5. Otherwise use concise chat/code, a worked example or retrieval prompt. Create a reference for likely future lookup, not as a substitute for acquisition.

Lessons are sequential, scoped artifacts in `lessons/`. Shared local CSS/vanilla
JavaScript in `assets/` is created only for an actual need and reused where useful.
`reference/` holds compressed verified reusable material, preferably Markdown when
sufficient. Existing GLOSSARY.md stays canonical and keeps its learner-evidence
requirements. None of these directories is a mandatory initialization step.
No framework, package manager, generic lesson engine or tracking mechanism added.

## Tests and method

Windows/PowerShell; Python 3.13; Node 22.17.0; headless Edge 155.0.4283.45.
The implementing agent performed these checks with full task/rubric context.
No subagents, independent evaluator chats, or native skill-discovery runs were used.

Executed:

```text
python tests/validate_repo.py
python -B -m unittest discover -s tests -p test_validator.py -v
python <installed-skill-creator>/scripts/quick_validate.py skills/learning-companion
node <local-test-harness>/browser-check.cjs
python <local-test-harness>/author-replay.py
```

The existing 11 fixture tests pass, including independent companion packaging,
missing references/templates, path escapes and unsupported frontmatter. The
repository structural validator and all five skill-creator entrypoint checks
pass. These checks do not evaluate teaching quality. The local test harness and
raw snapshots are under ignored `work/experience-eval/`; do not treat them as a
new supported runtime. Generation scripts deliberately require a fresh output
directory and should not overwrite learner state on rerun.

An initial structural run found this then-unwritten report link; resolved by
creating this report and rerunning validation. The first un-escalated fixture
test run stalled at temporary writes outside the active chat workspace and was
stopped; a scoped authorized run completed all 11 tests. Two harness defects were
corrected before passing: CDP Enter needed its text field, and Windows newline
bytes required comparing real before-state hashes. Neither required a lesson or
skill behavior change. Failed scratch fixtures are retained only under ignored work/.

### Existing companion regressions

[Exact author responses and self-review](experience-author-replay-2026-10-16.md)
cover A-L against the existing fictional initial fixture map. Writes were executed
in a new isolated scratch copy; checks verify no evidence from coverage, no global
label record, unchanged missions where required, unchanged F/G/I state, preserved
MCP mission during K, explicit J removal, D supersession, and no unwanted HTML.

| Cases | Observed author-run outcome |
| --- | --- |
| A / E | Coverage creates no record; reported specific experience creates no global label |
| B | Bounded explanation evidence with assistance uncertainty; no execution claim |
| C | Nearby real boundary-input test selected; no basic discovery recap |
| D | Old observation preserved, false implication superseded, dependent state repaired, gap open |
| F / G | Learner leads source choice when supported; direct-help override honored |
| H / K | Deferred production scope; separate minimal mission with authorized preferences only |
| I / J | Stored evidence distinguished from reported context; explicit removal honored |
| L | Goal/location clarification; no empty workspace creation |

This is an author-driven regression exercise, **not** an autonomous, blind,
fresh-context behavioral pass. The author loaded the whole initial fixture map
for setup; C therefore does not establish narrow-read isolation. H's acceptance
variant, L's no-filesystem variant, native routing, concurrency and symlink cases
were not exercised. Original session cases 1-13 were not rerun; their skill bundles
are byte-identical and previous reports remain historical evidence only.

### New experience cases

| Case | Observed check | Limit |
| --- | --- | --- |
| 1 Visual concept | Actual MCP lesson generated with responsibility diagram and predictions | Author selected medium; not an independent routing test |
| 2 Tiny syntax | Author reply uses chat/code for strip(), no HTML | Shared-context review |
| 3 Authentic task | Real Python implementation selected after contract understanding | Learner implementation/run not observed |
| 4 Interaction | Browser answers leave all four state Markdown files byte-identical; no record/glossary created | Does not establish all future tutor behavior |
| 5 Transfer | Author review permits bounded reasoning evidence, with no execution claim | Supplied scenario is fictional; no real learner transfer yet |
| 6 Preference | Chat-only reply honors today's override without changing stable preference | Shared-context review |
| 7 Reuse | Separate second-lesson fixture links the existing CSS/helper; unchanged asset hashes; feedback works | Authored fixture, not autonomous second-lesson generation |
| 8 Independence | Source/model proposal invited before artifact generation | Prior evidence is fictional |
| 9 Accessibility | Keyboard radio/submit use, visible focus, semantic controls, textual feedback; desktop/mobile screenshots inspected | No screen-reader or comprehensive accessibility audit |
| 10 Portability | file:// loading with network blocked; no HTTP requests; no-JS model/instructions/reference readable | Tested in Edge only |

## Fresh MCP local test

Starting fictional prompt:

> I want you to be my long-term learning companion for MCP. I know Python, REST
> APIs, and tool calling. I want to understand MCP well enough to use it confidently
> in my AI-agent projects. I prefer interactive and visual learning when it helps.

Created under `learning-workspaces/mcp-experience-demo/` (ignored, local only):
- `MISSION.md`, `LEARNER.md`, `CHECKPOINT.md`, `RESOURCES.md`
- `lessons/0001-mcp-mental-model.html`
- `assets/lesson.css`, `assets/quiz.js`

The lesson gives one conceptual request/result path, nests client inside host and
tool inside server, practices deciding/communicating/executing, then changes to a
weather scenario. It cites the [official MCP architecture overview](https://modelcontextprotocol.io/docs/2026-07-28/learn/architecture),
opened 2026-10-16; no SDK installation, transport trace or full protocol lesson is
implied. A direct expandable answer is available without forcing quiz completion.

Twenty-two browser checks passed. They cover empty and wrong responses, retry,
small/strong hints and worked answer, all responsibility feedback, weather return
path, keyboard controls, narrow-screen overflow, local stylesheet loading, no-JS
fallback, second-lesson helper reuse, no HTTP requests and unchanged learning state.
The helper has no storage, telemetry, network requests or Markdown-write integration.

Actual learner interaction: **NOT OBSERVED**. Scripted browser selections are
mechanics checks, not learner responses. No learning record, glossary, mastery,
or demonstrated progress was saved. The checkpoint links the pending explanation
and subsequent real `search_notes()` task. A live learner Python implementation
and MCP round trip remain pending; none has been simulated or claimed.

Screenshots and raw browser output (local, ignored):
- `work/experience-eval/mcp-lesson-desktop.png`
- `work/experience-eval/mcp-lesson-mobile.png`
- `work/experience-eval/browser-results.json`
- `work/experience-eval/demo-state-before-browser.json`
- `work/experience-eval/reuse-assets.json`
- `work/experience-eval/original-four-hashes.json`
- `work/experience-eval/replay-state.json`

Asset reuse is demonstrated in a separate synthetic fixture under
`work/experience-eval/reuse-fixture/`; the fresh MCP workspace contains only one
lesson. No empty reference directory, duplicate glossary, command sheet, simulator,
or extra lesson was generated there. No mandatory artifact-per-topic policy added.

## Next real-user test and limits

Have a university student open the MCP lesson without coaching. Observe one wrong
prediction, their use of hints, and their explanation of a changed architecture.
Then ask them to implement the ordinary Python function and identify the boundary
they would expose through MCP. Save only the actual explanation/build evidence
with assistance used. Return after several days with a changed integration and
compare how much help is needed. Separately rerun A-L and the new cases in fresh
native client chats with rubrics withheld and a reviewer other than the author.

No claim of scientific visual effectiveness, retention, reduced dependence,
cross-model reliability or completed real learner learning is made by these tests.
