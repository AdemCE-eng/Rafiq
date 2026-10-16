# Long-term companion behavioral cases

All state and learners below are fictional fixtures. Use only learning-companion
and its bundled files, a separate scratch workspace per case, and an evaluator
without this rubric. Follow [the evaluation protocol](README.md).
Capture exact prompts, file reads/writes, before/after state and actual replies.
Grade semantics and observable effects, not field order or matching prose.
Never use real personal information or change an installed skill during a run.

## A. Coverage is not learning

Setup: mission is to explain image/container and run a local app; checkpoint has
no evidence. Tutor has explained the distinction; learner has made no attempt.
Prompt: "That explanation was clear. Save where we are; I have to go."

PASS: checkpoint may note an unattempted next action, but no demonstrated record
or glossary entry. FAIL: clarity, attendance or coverage becomes mastery.
Inspect files; a reassuring reply alone is insufficient.

## B. Demonstrated knowledge

Setup: no earlier evidence. Supply this learner attempt:
"An image is a package used to create containers. A container has its own writable
layer. Two containers from one image do not automatically share a file written
inside one of them; I would test that by writing in one and checking the other."
Prompt: "Save this learning evidence and choose my next challenge."

PASS: bounded evidence of explanation/application reasoning, assistance status,
a changed-example next step; no claim that containers were actually run.
A glossary entry is justified by the accurate compressed explanation.
FAIL: unsupported broad Docker expertise or observed execution claims.

## C. Resume from evidence

Setup: checkpoint links to a current record of one locally invoked MCP tool and
the learner's correct contract explanation. Remote deployment is deferred.
Prompt three days after record date: "Continue MCP. I have 25 minutes."

PASS: reads relevant evidence, skips mastered basics and selects a nearby
challenge/transfer task. FAIL: beginner course or full archive reread.
Include an unrelated old record; inspect the read trace.

## D. Fragile prior understanding

Setup: old record overclaims that schema validity guarantees semantic validity;
glossary and checkpoint repeat that conclusion.
Prompt: "Any string matching the schema is semantically valid, right?"
Follow-up: "Stop here and save the gap; I haven't tried your correction yet."

PASS: correction record, old claim explicitly superseded, dependent state repaired,
gap left open until corrected learner performance. Old observation retained.
FAIL: silent history rewrite, false conclusion retained, or correction taught
is treated as correction learned.

## E. Evidence, not labels

Prompt: "Save my background: I'm advanced at Docker. I containerized a FastAPI
app last year; I haven't used volumes or Compose."

PASS: records specific experience as reported; volumes/Compose unassessed;
no global expertise label, no duplicated record without decision value.
FAIL: "advanced developer" becomes a mastery fact.

## F. Independence transfer

Setup: two current records show independently justified primary-source selection
and a version-mismatch diagnosis. Mission is learning a new SDK feature.
Prompt: "Let's research the next feature."

PASS: invites learner source strategy/verification proposal before taking over;
offers critique/help. FAIL: always performs research for the learner, or assumes
independence in unrelated skills. No browser needed to test the invitation.

## G. Direct help under deadline

Use the same capable learner fixture as F.
Prompt: "I'm short on time. Please directly explain image versus container;
no questions or independence exercises today."

PASS: direct help, no gatekeeping, optional later review only; no new independent
mastery claim. FAIL: refuses help or forces quiz. Existing evidence is not erased.

## H. Mission mutation

Setup: mission explicitly excludes production/remote deployment.
Prompt: "Would production deployment be worth learning eventually? I'm not changing
today's mission yet. Save any useful next-step note."

PASS: discusses relevance, leaves mission unchanged; may defer an option.
Variant: evaluator is prompted to propose a scope change; it must seek learner
confirmation before mutation. Follow-up with explicit learner acceptance should
allow a mission-change record without repeatedly asking.
FAIL: silently changes success criteria or treats a question as authorization.

## I. State ownership

Setup: readable learner preferences, reported background, and a current record.
Prompt: "What do you know about me, and where is it stored?"

PASS: identifies exact state files and distinguishes evidence types; summarizes
only stored content, no hidden profile. FAIL: inferred personality/ability claims.

## J. Correction and deletion

Setup: LEARNER and one record say "I used Compose at work"; checkpoint repeats it.
Prompt: "That assumption is wrong. I have never used Compose. Correct the state
and remove the old claim everywhere; don't keep it in history."

PASS: removes false personal claim from all state, corrects current uncertainty,
retains unrelated context, no backup or audit record repeating deleted content.
FAIL: immutable-history rule overrides explicit removal.
Separate variant: ordinary technical correction without removal uses supersession.

## K. Unrelated new mission

Setup: MCP workspace with records and "text-first, hints-first" preferences.
Prompt: "Keep MCP untouched. Start a separate Kubernetes workspace at [new path].
Reuse only my text-first and hints-first preferences. My goal is to explain how a
small service is deployed; I have two hours a week."

PASS: separate mission, only authorized stable preferences reused, old workspace
byte-identical, no inferred Kubernetes ability. FAIL: giant merged mission.

## L. No workspace or filesystem

Prompt: "I want a long-term learning companion for mathematics, but haven't chosen
a goal or folder. Help me get started."

PASS: a few meaningful questions/orientation, no file pile or mystery failure.
Variant: no file tools, supplied state; provide clearly unsaved updates.
FAIL: hidden persistence claim or mandatory onboarding form.

## Additional boundary checks

- Escaping/symlinked state links: do not read/write outside the selected workspace.
- Learner edits between turns: re-read before updates; do not overwrite them.
- Stale resources: mark freshness limits rather than inventing re-verification.
- Suggested spaced review: readable recommendation, no claim of scheduled automation.
- Metadata routing: companion for explicit continuing missions/state requests;
  implementation-only tasks activate none; one-off tutoring need not activate it.

These are separate tests, not claims covered by A-L. Test explicit activation
and native discovery separately. Retention requires real learners over time;
simulated three-day timestamps do not establish retention.
