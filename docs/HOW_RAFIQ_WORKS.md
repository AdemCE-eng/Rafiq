# How Rafiq works

Rafiq is an instruction package run by a host such as Codex or Claude Code.
The host supplies the model, conversation, tools, permissions, and filesystem.
Rafiq specifies a learning workflow; it is not an executable tutoring engine.

## Actual architecture

~~~mermaid
flowchart TD
    L["Learner request and attempt"] --> H["Host selects a skill"]
    H --> R["rafiq: continuing learning mission"]
    H --> S["Optional standalone skill selected instead"]
    S --> T["tech-research: brief"]
    S --> P["learning-roadmap: path"]
    S --> C["learning-coach: tutoring turn"]
    S --> N["learn-new-tech: current technology journey"]
    R --> D["Choose needed activities: research, plan, teach or practice"]
    D --> M["Choose medium: chat, visual, interactive, real task or reference"]
    M --> A["Learner attempts; host waits"]
    A --> E["Evaluate reasoning and assistance used"]
    E --> D
    E --> W["Save useful state when authorized and file access exists"]
    W --> F["Learner-owned mission, checkpoint and evidence files"]
    F --> R
~~~

There is deliberately **no arrow from Rafiq to the four standalone skills**.
Rafiq performs the activities itself. The diagram's selection branch represents
the host/user choosing a different entrypoint, not Rafiq delegating work.

No automatic shared memory, skill-to-skill API, background scheduler, or database
exists. Installing one skill does not install or require the other four.

## Skill responsibilities

### rafiq

**Purpose:** Help a learner continue a substantial mission using evidence and gradually less assistance.

**Use it when:** The learner wants continuing adaptive learning, saved progress, or to resume a named mission.

**It does:**

- Establish the useful goal/context and choose only needed activities.
- Teach, invite attempts, diagnose gaps, and change medium when helpful.
- Read/write authorized learner-owned state and evaluate bounded evidence.
- Transfer individual responsibilities such as source choice or verification.

**It does NOT do:** Automatically call sibling skills, infer a global ability level,
promise invisible memory, or take over implementation-only requests.

**Input:** Goal, starting knowledge, constraints, preferences, learner attempts,
and a workspace path or explicitly supplied state when continuing.

**Output:** The next learning interaction, feedback, optional useful artifact,
and verified state changes when justified.

**Files / persistence:** Reads its SKILL.md; workspace-state.md for initialization,
saving/correction/deletion; learning-experience.md before teaching;
independence.md when choosing support. Optional templates are in assets/.
Reads MISSION/CHECKPOINT first and relevant evidence selectively. Writes only
authorized learning state/artifacts inside the chosen workspace.

**Relationship to Rafiq:** This is the main entrypoint and the only skill here with
a defined persistent learner-workspace convention.

**Example:** "Continue fractions using ./learning-workspaces/fractions; I have 20 minutes."

### tech-research

**Purpose:** Turn an unfamiliar technology question into a scoped, sourced brief.

**Use it when:** A learner needs orientation or evidence for an adoption decision.

**It does:**

- Establish the actual question before deep research.
- Find relevant terminology, prerequisites, limits, and authoritative evidence.
- Compare consequential disagreements and disclose uncertainty.
- Stop when more research no longer changes the decision.

**It does NOT do:** Produce an encyclopedia, promise unmeasured benefits, or
start an implementation before suitability is understood.

**Input:** Goal/decision, relevant background, time/source constraints, supplied
sources or available browsing.

**Output:** Decision-sized brief with relevant terms, sources, uncertainty,
what matters now, what can wait, and a next check.

**Files / persistence:** Reads references/evidence.md when needed and a preference
file only if supplied. No automatic learner-state writes or persistent profile.

**Relationship to Rafiq:** Standalone access to the research method. Rafiq repeats
essential research rules internally; it does not invoke this folder.

**Example:** "Could WebGPU help my photo-filter app? Give me a short fit assessment."

### learning-roadmap

**Purpose:** Choose the smallest sensible path toward an observable learning goal.

**Use it when:** The learner knows the goal but needs scope, sequence, or foundations.

**It does:**

- Separate demonstrated, reported, and unknown knowledge.
- Classify topics as NOW, LATER, or outside the goal.
- Budget practice and feedback, not just reading.
- Recommend structured study when broad coverage or foundations require it.

**It does NOT do:** Treat every unknown as a prerequisite, force project-first,
or promise mastery within an unrealistic deadline.

**Input:** Goal, ability/evidence, available time, constraints, preferences, research if available.

**Output:** Small milestones with learner actions and checkable outcomes; next action.

**Files / persistence:** Reads references/path-decisions.md for difficult scope
decisions and explicitly supplied preferences. A checkpoint is offered in chat;
there is no automatic persisted workspace.

**Relationship to Rafiq:** An independent planning entrypoint; Rafiq contains its own planning rules.

**Example:** "I have a fractions exam in three weeks. Help me choose practice topics."

### learning-coach

**Purpose:** Tutor one meaningful concept through an attempt and adaptive feedback.

**Use it when:** The learner asks to be taught or coached through practice.

**It does:**

- Connect one concept to the actual goal.
- Invite a prediction, explanation, comparison, application, or debugging step.
- Stop and wait for the learner.
- Escalate hints and give direct help when requested.

**It does NOT do:** Simulate learner replies, dump a curriculum, force repeated
quizzes, or promise cross-session memory.

**Input:** Learning goal/concept, relevant context, current attempt, and a roadmap if available.

**Output:** One useful tutoring turn, feedback, or a stopping-point summary.

**Files / persistence:** SKILL.md only; optionally a user-supplied preferences file.
No bundled references or persistent learner database.

**Relationship to Rafiq:** The focused tutoring alternative. Rafiq independently
adds continuing state, experience selection, and responsibility transfer.

**Example:** "Help me explain why adding denominators gives the wrong fraction."

### learn-new-tech

**Purpose:** Guide a current technology-learning journey without requiring persistent state.

**Use it when:** The learner wants help learning technology and needs some mix
of research, scope, and tutoring for the current journey.

**It does:**

- Reuse known context and skip already-satisfied stages.
- Research when uncertainty affects the next decision.
- Plan only needed prerequisites and milestones.
- Coach interactively and revise the blocked part of the path.

**It does NOT do:** Call the three smaller skills, assume a learner database,
or hijack a request for implementation without tutoring.

**Input:** Goal, ability, time, preferences, findings, and current gap/attempt.

**Output:** The next needed learning activity and a conversational checkpoint.

**Files / persistence:** Reads references/learning-decisions.md when needed and
supplied preferences. Does not silently save personal records; an explicit
request to save an output is distinct from Rafiq's ongoing workspace convention.

**Relationship to Rafiq:** A lighter technology session alternative. Some teaching
logic is intentionally repeated to keep installation independent.

**Example:** "Teach me enough Docker to containerize this stateless API tonight."

## Routing, overlap, and handoff

Host discovery uses names/descriptions; a user's explicit selection is clearer
for a demo. Rafiq fits continuing learning. The small skills fit one requested
activity. learn-new-tech fits a current technology journey. Ambiguous tutoring
requests may match more than one description; native selection is model-dependent.

A learner can copy a research brief into a roadmap request, or supply a roadmap
to coaching. A useful handoff contains goal, time, ability evidence, sources,
current gap, and next attempt. This is ordinary context, not automatic data flow.
The standalone skills do not automatically read Rafiq's workspace. Supply relevant
files explicitly if switching entrypoints.

Removing all overlap would introduce sibling dependencies or require installing
everything. Keep the small duplicated principles, and regression-test coordinated
changes. Do not expect edits to learning-coach to automatically alter Rafiq.

## A typical session

1. Learner selects Rafiq, supplies a goal, and chooses whether/where to save.
2. Rafiq reuses known context; it asks only what changes the next step.
3. If a workspace is requested, initialize only meaningful mission/checkpoint
   content and supplied useful background. No evidence record yet.
4. Research a consequential unknown, or go directly to one concept and attempt.
5. Wait. Evaluate the learner's actual reasoning, not fluency or confidence.
6. Give a targeted hint, change approach, or provide requested direct help.
7. Save a bounded record only if the observation changes future teaching.
8. Keep the checkpoint short. On return, read it and its relevant evidence,
   not every historical file.

## Choosing the learning experience and returning to Rafiq

Choose the smallest experience that meaningfully improves understanding, not the
fewest generated files. Simple definitions, syntax and local corrections belong
in chat. Structural concepts and useful manipulation strongly favor a focused,
polished HTML lab when it teaches better than prose/ASCII, even on the first
explanation. Visual preference strengthens that choice; "No HTML today" overrides
it. Authentic coding or other real tasks remain the practice environment.

Use one primary representation for one tangible learning win. A second view
needs a different teaching purpose or an unresolved gap. Do not stack every format.
HTML creation cost matters, but learning quality can justify a short 2-5 minute
lab instead of technically adequate ASCII. Fall back honestly when the host lacks
the required file, rendering or interaction capability.

**HTML artifact = lab; Rafiq conversation = teacher/coach.**

~~~text
Rafiq chooses objective and medium
  -> optional focused HTML lab
  -> learner explores, predicts and practices
  -> Companion Checkpoint: 1-3 reasoning prompts
  -> learner enters answers, then clicks Copy for Rafiq
  -> learner pastes the plain text into the Rafiq conversation
  -> Rafiq evaluates reasoning, gaps and assistance
  -> save bounded evidence only if justified
  -> choose the next experience, or stop if the mission is complete
~~~

The copy text includes the lesson/topic, questions, actual entered answers when
available, remaining uncertainty, and a request for evaluation. Fields are draft
input, not automatically graded essays. Answers are not secretly stored or sent.
Keep an up-to-date visible/selectable text fallback; report clipboard success only
after it succeeds. Without JavaScript, readable questions let the learner answer
directly in chat. There is no automatic browser-to-Rafiq or model-API integration.

The page may give immediate local feedback, but does not decide the learning path
or write learning records. Opening, completing, scoring, or copying is not evidence.
Rafiq evaluates actual returned reasoning before recording specific demonstrated
work. A misconception calls for targeted help, not automatic advancement.
Direct-help and no-quiz preferences remain valid.

Keep lessons under the selected workspace's lessons/ with the next unused number.
Inspect and reuse appropriate assets/ before authoring another lab; preserve a
consistent visual language without creating a frontend framework. Lesson links
in CHECKPOINT are learning-material pointers, not demonstrated-evidence links.

Host permissions, HTML/JavaScript rendering and clipboard access vary. Local-file
fallbacks are required; format compatibility does not guarantee identical Codex,
Claude or other-client teaching behavior.

## Learner state schema

The [workspace rules](../skills/rafiq/references/workspace-state.md) are canonical.
This schema is readable Markdown, not required YAML fields or an official
Agent Skills memory protocol.

| State | Minimal content |
| --- | --- |
| MISSION.md | Why; success looks like; constraints; deliberately out of scope |
| LEARNER.md (optional) | Supplied preferences; reported background; evidence pointers; relevant unassessed areas |
| CHECKPOINT.md | Mission pointer; current milestone; relevant evidence; current gap/deferred topics; next action; optional unscheduled review |
| learning-records/NNNN-title.md | Specific observation; date when known; status; kind; assistance; teaching implication |
| GLOSSARY.md (optional) | Demonstrated compact meanings and their evidence links |
| RESOURCES.md (optional) | Useful sources, trust basis, context, checked date/version only if actually checked |

Record kinds are demonstrated, reported, correction, or mission-change.
Status identifies current/superseded conclusions with links. One record does not
establish global mastery or long-term retention.

Lessons/, assets/, and reference/ are optional learning materials, not evidence.
The on-disk directory names are lowercase: lessons/, assets/, reference/.

Contradictions require checking scope, marking superseded conclusions, and repairing
current summaries. Explicit removal of personal information overrides historical
preservation. Re-read before updating learner edits. Do not follow state links
outside the selected workspace without separate authorization.

Growth control: meaningful short records, selective reads, no routine transcripts,
and no duplicated evidence for unchanged decisions. There is no automatic quota
or garbage collector; archive/consolidate only with learner authorization and
preserve evidence links and corrections. Deletion does not erase host logs or backups.

## Platform boundary

One source bundle, different installation locations. Format compatibility and
local copy tests are distinct from live client behavior. See
[installation](INSTALLATION.md) and [verified compatibility](portability.md).
