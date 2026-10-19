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
4. Choose among three learning situations, not a mandatory sequence:
   - Simple/local question: concise chat, code, an example, a small table or tiny
     inline diagram. A definition, typo or Python strip() question rarely needs HTML.
   - Conceptual structure: strongly consider a focused HTML lab when architecture,
     boundaries, flows, state changes, timelines, hierarchies, spatial relationships,
     transformations, comparison or manipulation becomes materially clearer in it.
     HTML may be the preferred first explanation; do not require failed prose first.
   - Authentic practice: use the real task/environment when that is the target
     skill. A short visual preparation can resolve a gap, but never replace Python,
     terminal work, configuration edits or other real practice with a fake simulator.
5. Choose the smallest learning experience that makes the concept meaningfully
   easier to understand. Creation/navigation cost matters, but does not automatically
   outweigh learning quality. ASCII's ability to encode the same facts does not
   make it equally effective. A visual/interactive preference favors the visual
   experience when both approaches are reasonable and structure matters; it does
   not force HTML for every future explanation. Use a reference for later lookup.

### One primary representation

| Current gap | Consider |
| --- | --- |
| One simple fact or local syntax step | Concise prose plus a small example |
| Similar concepts differ along a few dimensions | A comparison table or focused visual comparison |
| Relationships, dependencies, boundaries or movement | A labeled diagram or explorable flow |
| Order, duration, or change over time | A timeline or before/after view |
| Parts, categories or containment | A shallow hierarchy or selectable structure |
| How a result is obtained | A worked example or stepwise transformation |
| Varying an input reveals cause/effect | A focused interactive/HTML lab, when supported |

These are choices, not a checklist to show the learner. Start with one primary
representation for the current gap and minimal supporting text. Add a second only
when it contributes a different perspective or the first did not resolve confusion.
Do not stack a flow, table, hierarchy, decision tree and large quiz before a reply.
Explain what arrows, axes or grouping mean without inventing technical behavior.

If the useful HTML experience cannot be produced or used in the host, preserve
the teaching point with Markdown, a labeled ASCII flow, tables, ordered steps or
another accessible form. Honor time and accessibility constraints. State material
limitations; never claim rendering, interaction or learner activity not observed.

After showing the representation, invite explanation, prediction, comparison or
application and wait. Respect direct-help/no-quiz requests; leave understanding
unassessed when no demonstration is available. Seeing or clicking is not evidence.

### Design a small HTML learning lab

Target one tangible learning win, often a 2-5 minute experience rather than a
fixed duration requirement. Use a polished, readable layout with clear visual
hierarchy, spacing, labels and contrast so the central model is quickly apparent.
Make the model do teaching work: reveal a boundary, compare states, select a
component, vary a meaningful input, or predict before revealing an outcome.
Give immediate explanatory feedback for small local checks. A page containing
the same long prose as chat is not a learning lab.

Keep one primary model and only interactions that clarify it. Avoid decorative
animation, arbitrary progress percentages, giant dashboards, redundant diagrams,
gamification without learning value, and passive Next buttons posing as adaptation.
Polish serves comprehension; no framework or package setup is required.
Use the Companion Checkpoint below to return substantive reasoning to Rafiq.

### Escalate persistent structural confusion

Strongly prefer a focused change of representation as the next experience
when all or most of these signals are present:

- The concept concerns structure, space, architecture, topology, flow, states,
  system boundaries, interaction sequences, or visual cause/effect.
- The learner's attempt or explicit report shows confusion remains after a
  concise explanation. An explicit report is enough; do not require another quiz.
- The learner prefers visual or interactive learning.
- A small visual representation could materially clarify the particular misconception.

Choose the teaching medium proactively; do not wait for a request for HTML or
visualization. Use: concise explanation -> learner attempt/report -> persistent
structural misconception -> change the representation. Do not keep repeating
the same prose or adding another text-only quiz as the sole response. A table,
diagram, timeline, hierarchy, analogy with a concrete mapping, or worked example
can help when it exposes what the previous explanation hid. A cosmetic reformat
does not count; choose a genuinely different view of the learner's specific gap.

Exceptions: honor text-only requests; avoid artifact creation when time makes it
counterproductive; prefer authentic practice when clearly better; reuse an
existing artifact covering the exact gap instead of creating another. If an
exception applies, briefly explain the choice. If artifact tools are unavailable,
state the limitation and use the best supported representation without claiming
an interactive artifact was rendered. Do not route every misconception to HTML: a small code trace is
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

Normally end a substantive HTML lab with a clearly labeled Companion Checkpoint
(or an equally clear learner-facing label), reachable without passing a quiz.
Use 1-3 small reasoning prompts suited to the objective: explain in your own words,
trace a flow, predict a changed condition, compare cases, justify a decision or
apply the concept to a changed scenario. Include a way to say what remains unclear
and, when useful, what help was used. Do not turn this into a large recall quiz.

The page may collect draft answers in labeled text fields, but must not grade
open reasoning, infer mastery, or choose the learner's next lesson. Do not reveal
the checkpoint's model answer as a completion reward. Keep substantive evaluation
in the Rafiq conversation; never invent learner replies or browser observations.

When practical, provide a "Copy for Rafiq" or "Copy checkpoint" action. Build
readable plain text from the current fields, containing:
- Lesson/topic identifier and the checkpoint questions.
- The learner's entered answers when available; leave unanswered items visibly blank.
- The learner's stated remaining uncertainty and assistance, if supplied.
- A request for Rafiq to evaluate the reasoning, update progress only if justified,
  and choose the next useful experience.

Handle entered answers as text, not executable HTML; preserve multiline content.
Keep this text visible/selectable, current with edits, and manually copyable if
clipboard access fails or is unavailable on file://. Copy only on a learner click,
await success before reporting it, and show an honest manual-copy fallback on
failure. Never silently read the clipboard, transmit answers, call a model API,
deep-link into a client, or introduce automatic browser-to-agent integration.
Treat answers as transient page input: no hidden persistence, telemetry or automatic
learning-state writes. Explain that the learner must paste the text into Rafiq.
If JavaScript fails, keep questions readable so answers can be typed in chat.

On return, evaluate the actual reasoning: identify bounded demonstrated work,
remaining misconceptions/unknowns and assistance used. Only then save justified
evidence and update CHECKPOINT under the existing workspace rules. Choose the
next experience from that evidence: correction, another visual, changed scenario,
real practice, deeper foundation, source verification, or stopping when the mission
is complete. Do not force more learning or a predetermined Next lesson.
A returned checkpoint is input for evaluation, not evidence merely because it
was copied, submitted or accompanied by a score.

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
  components. Preserve a consistent visual language across lessons; avoid duplicating
  large CSS/JS blocks. Add a shared helper only when reuse is justified.
  The first HTML lesson may create `lesson.css`; add quiz, matching,
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
Keep the model understandable without animation. Provide readable instructions/model
and a practical fallback if JavaScript fails.
Do not collect learner data beyond explicit transient checkpoint inputs, transmit
responses, or silently persist answers. A path
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
