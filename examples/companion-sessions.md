# Companion sessions: fictional MCP learning history

These are authored examples, not test logs or claims about a real learner.
All folders below are learner-selected, local workspaces. The companion skill
is installed separately and needs no other skill.

## 1. First MCP session

Learner: "Initialize learning-workspaces/mcp. I know Python, APIs and tool calling.
I want to build and explain one local MCP tool for my agent project. Three hours
a week, hints first. Save meaningful learning evidence there."

Create MISSION.md and CHECKPOINT.md; create LEARNER.md for the reported background
and preferences. Do not create a mastery record or prefilled glossary.

After a focused lesson the fictional learner submits their own typed text-tool
function, explains its input contract, and predicts an empty-input case. In this
illustration the tutor also observes a successful discovery and invocation in a
test client, and the learner explains the result. This is stronger evidence than
a learner merely saying "it worked."

Save learning-records/0001-local-tool.md:

```markdown
# Local MCP tool contract and invocation
Date: 2026-10-16
Status: current
Kind: demonstrated
Evidence: Learner designed a text input contract, explained discovery versus
execution, predicted the empty-input result, and explained an observed successful
local invocation of their implementation.
Assistance: One setup hint; contract reasoning and implementation were learner-led.
Implication: Skip basic tool discovery next time. Remote transport and
authentication remain unassessed and outside the current milestone.
```

CHECKPOINT links to that record and proposes a changed-input validation exercise.
Only after the learner accurately compresses "tool contract" into their own
short explanation, add the term to GLOSSARY.md with the record link.
If an official SDK example was actually consulted, add its direct link, purpose,
trust basis and checked version/date to RESOURCES.md. Do not invent a version.

If instead the learner only reports a successful invocation, record that execution
as reported; their submitted reasoning may separately demonstrate understanding.
If they only read the lesson, no learning-evidence record is justified.

## 2. Resume three days later

Learner on 2026-10-19: "Continue MCP using learning-workspaces/mcp."

The companion reads MISSION and CHECKPOINT, then 0001-local-tool and relevant
preferences. It does not reopen every historical record or ask what a host is.

Tutor: "Last time you designed and explained one tool contract. Next, choose a
boundary input and predict how the tool should respond. What would you test?"

A relevant delayed transfer check serves the next milestone. It is not a full
quiz or a scheduled reminder. If the learner demonstrates the variation, record
the new capability only if it changes the next teaching decision.

## 3. Correct fragile understanding

Suppose an earlier fictional record overgeneralized the learner's ability:
"Input contracts are understood; they guarantee every semantic rule."

The learner later says any string matching the schema must be semantically
valid. The tutor exposes the distinction with a concrete counterexample. Until
the learner attempts a corrected explanation, do not claim the gap is fixed.

Add a correction record citing the earlier record; mark its overbroad conclusion
superseded, while retaining the observation that the learner designed one contract.
Update CHECKPOINT to "semantic validation distinction not yet demonstrated."
Mark any misleading glossary definition unreliable.

After the learner explains the distinction and designs a suitable boundary test,
add that evidence, update the glossary concisely and retire the current gap.
History reflects both the earlier assumption and the later correction.

## 4. Transfer responsibility

Early: the companion models one primary-source search and explains why it helps.

Later, two records show the learner independently chose version-appropriate
official docs, spotted a stale example and justified the replacement.

Tutor: "For the next feature, which source would you consult first, and what
version check would you make? Propose a small experiment; I can review it."

This transfers source selection and experiment design, not every activity.
A new protocol concept may still need explanation. If the learner says
"I need a direct answer today," provide it and leave an optional review target;
do not erase their prior independent performance or claim new independent skill.

## 5. Start a separate mission

Learner: "Pause MCP. Start learning-workspaces/kubernetes so I can understand
deploying a small service. Reuse only my text-first and hints-first preferences."

Keep MCP's mission and records intact. Initialize Kubernetes's own MISSION and
CHECKPOINT after establishing its outcome; copy only the authorized preferences
into its LEARNER file. Python/MCP knowledge is not a Kubernetes ability label.

A topic-specific prerequisite such as networking remains reported, demonstrated,
or unknown according to relevant evidence. Link/copy evidence across missions
only with the learner's authorization and when it actually matters.
