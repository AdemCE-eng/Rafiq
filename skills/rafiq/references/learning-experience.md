# Choose an experience that serves the objective

Ask: what would make this concept easiest to understand and hardest to
misunderstand? Choose after reading the mission and relevant evidence, before
teaching. Aim for one tangible learning win, not a miniature course. A short
lesson can combine a visual prediction with a real build; avoid extra prerequisites.

## Select the medium

Apply these decisions in order, using judgment rather than a fixed lesson format:

1. Honor the learner's current medium, time, accessibility, and artifact constraints.
   No HTML means no HTML. A one-time preference is not automatically permanent.
2. Use evidence to decide who designs the experience. When prior behavior supports
   source choice, modeling, or experiment design, invite the learner's proposal
   first and offer critique. New subject matter does not reset every responsibility.
   Requested direct help stays available; no fixed independence levels.
3. Prefer an authentic coding, terminal, build, or debugging task when it practices
   the target skill appropriately. Do not replace available real practice with a
   browser imitation. A brief visual preparation may resolve a specific prior gap.
4. Apply the structural-confusion escalation rule below before defaulting to chat.
   Otherwise choose a visual or interactive artifact when spatial structure, contrasting
   states/flows, manipulable cause/effect, explanatory feedback over several
   examples, or a reusable mental model materially improves understanding. Consider
   creation and learner navigation cost; availability alone is not a reason.
5. Otherwise use concise conversation/code, a worked example, or a small retrieval
   prompt. Use a reference sheet for likely future lookup, not initial acquisition.
   If artifact tools are unavailable, describe a compact model honestly in chat.

### Escalate persistent structural confusion

Strongly prefer a focused visual or interactive artifact as the next experience
when all or most of these signals are present:

- The concept concerns structure, space, architecture, topology, flow, states,
  system boundaries, interaction sequences, or visual cause/effect.
- The learner's attempt or explicit report shows confusion remains after a
  concise explanation. An explicit report is enough; do not require another quiz.
- The learner prefers visual or interactive learning.
- A small artifact could materially clarify the particular misconception.

Choose the teaching medium proactively; do not wait for a request for HTML or
visualization. Use: concise explanation -> learner attempt/report -> persistent
structural misconception -> change the medium. Another paragraph, ASCII diagram,
verbal analogy, or text-only question is not a medium change. Do not keep using
those as the sole response when a focused visual/interactive representation would
likely help more.

Exceptions: honor text-only requests; avoid artifact creation when time makes it
counterproductive; prefer authentic practice when clearly better; reuse an
existing artifact covering the exact gap instead of creating another. If an
exception applies, briefly explain the choice. If artifact tools are unavailable,
state the limitation and use the best available fallback without claiming a medium
change occurred. Do not route every misconception to HTML: a small code trace is
usually enough for confusion about Python `strip()` versus `lower()`.

For example, after concise MCP orientation, a visual learner with basic Python
and no API/MCP experience says, "Host and client feel like the same thing to me."
Create or reuse a small host/client lesson, not a full MCP course. Show one host
containing model/application logic, UI/orchestration, and two MCP clients, each
connected to its own external server (notes and weather). Let the learner reveal
or trace connections, place clients inside the host, or predict the client count
with immediate explanatory feedback. Keep the Companion Checkpoint available:
ask how many hosts and client connections this scenario has, why a client belongs
to the host but is not the whole host, and what remains unclear. Evaluate the
returned open reasoning before choosing the next task; page interaction is not
learning evidence.

| Learning need | Useful experience | Avoid |
| --- | --- | --- |
| MCP host/client/server boundaries | Manipulable visual flow; changed reasoning scenario returned to companion | An entire protocol course |
| Docker image/container distinction | Compare states and predict a change | Animation without a prediction |
| Python comprehension | Trace values, then write a small variation | A web app for a short expression |
| Git conflicts | Real conflict in an isolated local practice folder | A simulator replacing available terminal practice |
| Classification threshold | Manipulate threshold and explain tradeoffs | Unexplained moving charts |
| API authentication | Scenario decision with reasons | Unsupported security claims |
| Command syntax | Compact reference followed by real use | A giant lesson |
| `strip().lower()` | Short chat/code example | HTML by default |

These are choices, not mandatory mappings. A learner-created explanation or
diagram, matching/sorting task, quiz, trace, or debugging challenge may fit better.
State the intended win and briefly explain the medium when that helps the learner.

## Artifact = lab; companion = teacher/coach

The artifact primarily supports visualization, manipulation, exploration,
immediate low-level feedback and short closed-form checks. Local feedback can
explain an expected placement or result and offer a hint/retry; it does not
diagnose the learner's overall understanding or evaluate their open reasoning.

The companion handles explanations in the learner's own words, misconception
diagnosis, meaningful transfer questions, evidence evaluation and the next useful
experience. Keep substantive reasoning in the conversation, not an auto-graded
essay field or a self-contained linear HTML course.

A useful short pattern is:

Visualize -> Manipulate -> 1–2 quick local checks -> Companion Checkpoint
-> learner returns with reasoning -> companion evaluates -> next experience.

Adapt this pattern to the objective; do not add meaningless interaction just to
fill a stage. A flow stepper supports exploration, not lesson progression. Let
the learner revisit states and manipulate a small model. Prefer accessible native
controls to drag-only reconstruction. Keep instructions short and feedback local.
Hints can strengthen into a partial or requested full answer without gatekeeping.
Avoid arbitrary equal-length choices, completion scores and passive Next buttons
masquerading as practice. Fade scaffolding for the particular activity when prior
evidence supports letting the learner construct or verify their own model.

## Companion Checkpoint: explicit, portable handoff

End an interactive lab with a clearly labeled Companion Checkpoint, reachable
without passing a quiz. Ask the learner to bring back:

1. An explanation or request/result trace in their own words.
2. Reasoning about one meaningful changed scenario, chosen for the mission.
3. What remains unclear (and, when useful, which hints/answers they used).

The artifact can present the changed scenario but should leave its open-ended
reasoning and evaluation to the companion. Do not reveal its model answer as a
completion reward or treat a local score as a transfer assessment. Never invent
the learner's response or pretend to observe their browser activity.

Where useful, offer a Copy checkpoint button that copies a plain-text prompt
with blank answer slots, a lesson identifier, and an explicit request for companion
review. Keep the text visible/selectable for manual copying when clipboard access
is denied or unavailable on file://. Copy only on the learner's action; report
success only after the copy succeeds. Do not silently read the clipboard, transmit
responses, call Codex/Claude APIs, deep-link into a particular client, or introduce
an automatic integration. No automatic learning-state writes from the page.

On return, read the learner's actual reasoning, probe a specific ambiguity only
if useful, diagnose the gap and evaluate bounded evidence under the existing
rules. Then choose another small artifact, concise explanation, authentic
coding/build task, debugging exercise, deeper foundation or immediate progress.
Do not promise a fixed Next lesson or automatically advance to coding because
the learner clicked through or answered a local check correctly. The checkpoint
is a request for evaluation, not evidence and not a predetermined learning path.

For MCP 0001, let the learner step through request and result, reconstruct where
client/tool belong, and try at most two quick MCQs. The companion handoff asks for
their trace, a changed weather-tool scenario and remaining uncertainty. Evaluate
that response before choosing architecture correction, another visual, or the real
`search_notes()` Python implementation; the page does not make that choice.

## Workspace conventions (create lazily)

- `lessons/0001-short-topic.html` (or another suitable format): choose the next
  unused number from filenames; never overwrite a learner's lesson. A lesson
  supports acquisition, not permanent evidence.
- `assets/`: reuse appropriate existing CSS and vanilla JavaScript before adding
  components. The first HTML lesson may create `lesson.css`; add quiz, matching,
  diagram, or tracing helpers only when needed. Keep code student-readable.
- `reference/`: compressed verified material worth revisiting, in Markdown when
  HTML adds little. Keep one canonical glossary: link to the workspace's existing
  `GLOSSARY.md` if present, and retain its evidence rules rather than prefill terms.

Keep generated lessons in the learner workspace, not the installed skill. No
generic generation engine, frontend framework, or package manager is needed.
Keep a consistent small visual system without decorative polish. Link a useful
artifact and its next learner action from CHECKPOINT; leave the memory model intact.

For ordinary HTML use semantic elements, labeled native controls, visible focus,
keyboard operation, readable contrast, and explanatory text as well as color.
Avoid drag-only interactions. Use relative local assets without CDNs, remote fonts,
or mandatory network requests; open in a normal browser without a build step.
Provide readable instructions/model and a practical fallback if JavaScript fails.
Do not collect or transmit learner data or silently persist quiz answers. A path
is sufficient for opening; use a supported safe opener only when useful. Do not
depend on auto-opening or automate a browser merely to display the artifact.

Verify consequential, version-sensitive, protocol/API, security, and compatibility
claims against applicable official sources; open sources before citing. Reuse
curated sources when appropriate; disclose unverified version-sensitive details
when offline. Timeless syntax examples need no decorative research. Cite important
sources in the artifact with checked date/version when actually checked.

## Keep interaction separate from evidence

Opened pages, completion badges, animations watched, and one correct guessed
choice do not justify a learning record or mastery claim. Do not wire completion
events to Markdown state writes. Local feedback is for practice, not assessment. MCQ success, reconstruction success
or reaching/copying the Companion Checkpoint alone is not demonstrated understanding.
The companion evaluates actual returned reasoning before choosing what comes next.

An explained prediction, correct construction, debugging outcome, application in
a build, or success with reasoning on a changed scenario can justify bounded
evidence under the existing workspace rules. Record the actual behavior and help
used; distinguish observed work from learner-reported results. If no such evidence
arrives, keep the checkpoint at the pending attempt, without inventing progress.
Generated verified references are instructional material, not learner-understood
glossary evidence. Never create a glossary entry just because a lesson used a term.
