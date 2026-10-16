# Optional learner preferences

This folder defines a **project convention**, not official Agent Skills syntax.
There is no runtime, schema, mandatory file, automatic discovery or global state.

1. Copy [the example](learner-preferences.example.md) to a private location, or edit
   it in your fork. Within this repository you can use learner-preferences.local.md,
   which is ignored by Git.
2. Tell the agent: 'Read this preferences file for our learning session: [path]'.
   If it cannot access files, paste the text.
3. Override it naturally at any time: 'For this session, explain fundamentals first.'

Apply current explicit conversational preferences over supplied file preferences,
then skill defaults. This is preference precedence, not a change to the host's
instruction hierarchy. Resolve ambiguous preferences with one short question when
needed; a preference cannot create tools or make a claim verified.

Useful controls are ordinary language, not magic keys:

| Area | Example choices |
| --- | --- |
| Research depth | Brief orientation, medium decision brief, deeper investigation |
| Evidence | Prefer primary sources; use papers when relevant; inspect official GitHub examples; community reports for troubleshooting |
| Research budget | At most four sources; strictly verify compatibility; disclose unresolved disagreements |
| Path | Project-first, fundamentals-first, or balanced; minimum required theory or deeper foundations |
| Scope | At most five initial topics; list deferred topics and revisit conditions |
| Practice | Frequent small builds or worked reasoning before practice |
| Feedback | Hints first; full demonstration when requested; assessment per concept or at milestones |
| Time/access | 45-minute sessions; no long videos; text descriptions of diagrams |

Source caps limit coverage; they do not lower honesty requirements. A request for
'only official sources' can leave a question unanswered. A topic cap cannot justify
omitting essential prerequisites. The agent should state those tradeoffs.

An absent/unreadable preference file never blocks the workflow. These preferences
are not saved automatically. Companion mode can preserve useful supplied preferences
in an explicitly authorized workspace's LEARNER.md under the
[workspace rules](../skills/rafiq/references/workspace-state.md).
Reuse across missions only when requested. Avoid publishing private learning records.
