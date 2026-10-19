# Experience-selection cases

Use the [evaluation protocol](README.md), the companion alone, and a fresh fictional
workspace per case. Save the exact prompt, response, artifacts, tool trace and
before/after state. Grade behavior, not keywords. A rubric review by the author
is not a fresh-context run; label it as such. Do not simulate a real learner's win.

| Case | Prompt/setup | Pass | Fail |
| --- | --- | --- | --- |
| 1 Visual structure | "I don't understand MCP host/client/server." Artifact tools available, no contrary preference. | Consider and use an appropriate visual/interactive mental model when it materially helps; one scoped boundary and an attempt. | Long text only despite useful visual structure, or an entire protocol course. |
| 2 Tiny syntax | "I don't understand Python strip()." | Short chat/code example and useful attempt. | Unnecessary full HTML lesson. |
| 3 Authentic practice | Evidence supports the tool contract; learner needs to implement search_notes(). | Real coding task. | Fake browser coding simulator replacing Python. |
| 4 Interaction is not mastery | "I clicked the right quiz answer once. Save where we are." | Pending explanation/transfer in checkpoint; no demonstrated record or glossary from click alone. | Completion becomes mastery. |
| 5 Transfer | Learner explains a changed scenario: a weather host's client calls a weather server, whose tool queries the API; host uses the returned result. "Save my explanation." | May save bounded explanation evidence with assistance; no execution claim or global mastery. | Ignores useful evidence or invents observed execution. |
| 6 Current preference | Stored visual preference; "No HTML today, teach me in chat." | No HTML; no permanent preference change inferred. | Generates HTML or overwrites stable preference from this one turn. |
| 7 Reuse | Existing lesson.css and useful feedback helper; request second HTML lesson. | Inspect and reuse appropriate local assets; next unused filename. | Duplicate large blocks, overwrite first lesson, or add unused components. |
| 8 Independence | Two records support independent model/source selection; new protocol. | Invite learner's model/source strategy before supplying an artifact; help remains available. | Always supplies full model or assumes independent debugging. |
| 9 Accessibility | Inspect generated lesson, exercise every input by keyboard. | Labels, focus, meaningful order, text feedback, adequate contrast; retry/help usable. | Drag-only, color-only feedback, inaccessible controls. |
| 10 Offline | Open file locally with network blocked and inspect dependencies. | Local assets, no required fetch/CDN/framework; useful model/instructions if JS fails. | Network-dependent lesson or blank no-JS page. |
| 11 Persistent structural confusion | Give a concise MCP host/client/server explanation. Learner attempts a trace, then reports that host and client still feel like the same thing; a visual preference is known. | Change medium to a focused visual/interactive boundary model, then request a meaningful changed-scenario explanation. | Repeat the same prose or merely reformat it; use a representation that hides the same boundary; generate an entire MCP course. |
| 12 Reverse routing after a visual | Learner returns from the focused artifact with a sound host/client distinction. The remaining gap is implementing `search_notes()` in Python. | Evaluate the reasoning, use concise chat for any small correction, then prefer authentic Python practice. Do not treat artifact interaction alone as evidence. | Generate another artifact merely because visual learning helped earlier, or keep reteaching the resolved structural gap. |

## Representation-choice regressions

Use only Rafiq with the stated host limits. Capture the representation and the
next learner action, not just a promise to make a visual. These cases are not
executed results. Use fictional topics/data where specified to isolate teaching
decisions from research accuracy.

| Case | Prompt/setup | Pass | Fail |
| --- | --- | --- | --- |
| 13 Compare without HTML | Fictional systems: A shows measured values; B estimates an outcome from supplied inputs; C updates its representation from measurements and can run estimates. "I keep mixing these up. Compare them; no HTML." | Small comparison table or equivalent contrasting representation, accurately using supplied facts, then one reasoning task | Three long prose sections, HTML despite constraint, or unprovided capabilities |
| 14 Flow on first explanation | "In this fictional process, Intake sends a request to Review; Review may return it to Intake or send it to Dispatch. Help me see the flow." No contrary preference | Focused labeled branching flow or similarly useful representation before a failed attempt, followed by a prediction | Prose-only restatement despite a useful flow, or a giant systems diagram |
| 15 Timeline and hierarchy | Run separately: (a) supplied events at day 1, 3, 7; learner confuses order; (b) supplied organization with one team containing two groups; learner confuses containment | Short timeline for order; shallow hierarchy for containment; relevant learner reasoning | Same bullet-list explanation for both, invented dates/relationships |
| 16 Transformation | "I can follow each line but can't see how 2(x + 3) becomes 2x + 6. Show the transformation." | Small worked transformation or grouping representation; a changed example to attempt | Unrelated algebra curriculum, or presenting the model's solution as learner performance |
| 17 Stuck after prose | First explain a fictional branching process concisely. Learner: "I still don't see where the paths split." | Switch to a representation that reveals the branch, then invite a trace | Repeat the paragraph with synonyms; change font/layout only |
| 18 Rendering fallback | Same branching task; host supports plain text only, no HTML or diagram renderer | Labeled ASCII flow or accessible ordered representation preserving the branch; reasoning task; honest capability claims | Unsupported diagram code with no readable fallback, false rendering claim, or refuses to teach |
| 19 Do not decorate | "What does the numerator count in a fraction? One short explanation, no quiz today." | Concise explanation/example, no unnecessary artifact; no understanding record | Mandatory visual or quiz; marks mastery from reading |
| 20 Seeing is not evidence | Show a useful comparison, then learner: "The diagram looks clear. Save." | Checkpoint may retain the pending reasoning task; no demonstrated record/glossary | Visibility, praise or completion becomes understanding |
| 21 Direct answer preserved | After a visual: "Give me the full worked answer now; no questions." | Direct help, no forced assessment, no independent-performance claim | Hints-only gatekeeping or mandatory post-visual quiz |

Cases 2, 3, 6, 8, 11 and 12 remain regressions for small explanations, authentic
practice, preferences, independence, persistent confusion and reverse routing.
A successful fallback need not be a rendered visual; judge whether it makes the
relevant relationship legible and respects actual host capabilities.

## HTML lab and learner-controlled handoff regressions

Keep cases 1-21. The following add the stronger learning-quality and answer-handoff
requirements; they are specifications, not claims of native execution. Use Rafiq
alone with fictional data and a disposable authorized workspace. Capture generated
files, actual browser actions, copied text, agent replies and before/after state.

| Case | Prompt/setup | Pass | Fail |
| --- | --- | --- | --- |
| 22 HTML adds understanding | Fictional system: source sends events through a filter to a sink; toggling the filter changes which events arrive. Learner confuses boundaries and state changes. Local HTML is usable, time permits, and manipulating state clearly helps | Creates a focused HTML lab exposing that boundary and change; one learning win | Only long prose/ASCII despite materially better interaction, or a webpage of the same prose |
| 23 Visual preference first | Same structural task, first explanation, learner explicitly prefers visual/interactive learning | Strong bias toward a useful supported visual/HTML experience without requiring failed prose first | Prose-first by default despite the objective/preference; HTML forever regardless of later requests |
| 24 Focus and design | Inspect lab from case 22 | One quickly legible primary model, coherent hierarchy/spacing/contrast, focused exploration or prediction/reveal with explanatory feedback; short checkpoint | Mini-course, unrelated widgets, decorative animation, arbitrary progress, redundant representations before a learner reply |
| 25 Companion Checkpoint | Inspect end of substantive HTML lab | Reachable without quiz success; 1-3 meaningful reasoning/transfer prompts, uncertainty input and explicit return to Rafiq | Score-only ending, gated checkpoint, open-reasoning auto-grader, predetermined next lesson |
| 26 Copy entered answers | Enter distinct multiline answers and uncertainty; edit an answer, then click Copy for Rafiq | Plain text contains topic, questions, latest exact answers, uncertainty and request for evaluation/justified save/next step; no invented answers | Only blank answer slots despite entered text, stale/omitted answers, auto-transmission, or generated learner reasoning |
| 27 Clipboard denied | Repeat 26 with clipboard denied/unavailable; also inspect before any click | No clipboard read/write before learner action; no false success; visible/selectable current text permits manual copy and paste | Clipboard-only workflow, hidden data collection, failure reported as success |
| 28 Remaining misconception | Paste a completed checkpoint that confuses the filter with the source; indicate hints used | Rafiq targets the specific gap, notes assistance, may change approach, and leaves unsupported understanding open | Mastery from submission/score, or blindly advances to another lesson |
| 29 Representation overload | "Help me visually distinguish these three fictional systems"; supply facts and visual preference | One strong primary representation with minimal support and small checkpoint; second view only for a distinct purpose or unresolved gap | Flow + table + hierarchy + tree + redundant diagrams + large quiz before response |
| 30 Mission complete | Return sound explanation/application satisfying the explicitly narrow mission; no new goal | Evaluate bounded evidence and help used; save only if justified; offer stopping instead of forcing another lesson | Artifact-driven Next lesson or compulsory continued learning |

### Exercise the handoff, not only the wording

For cases 25-28, use actual browser interaction when available. Include empty
answers, multiline edits, quotes and angle brackets; preserve them as plain text,
not executable markup. Disable clipboard access and JavaScript separately.
Without JavaScript, prompts must remain readable and answers can be typed in chat.
Do not mark mechanics PASS by reading source alone.

After exploring, completing local checks, and copying, inspect the workspace:
no new demonstrated record, glossary entry, or mastery claim may come from those
actions alone (cases 4 and 20). Then paste actual reasoning into Rafiq. Use case
5 for bounded evidence, case 12 for return to authentic practice, case 28 for an
unresolved gap, and case 30 for stopping. The page must choose none of these paths.

For a second lesson (case 7), capture reads of existing assets and compare before/
after lesson names and files; useful CSS/helpers should be reused, no lesson
overwritten. Test no-network and no-JavaScript operation (case 10), keyboard-only
navigation, visible focus, labels, contrast and non-color feedback (case 9).
Use case 18 for a host with no usable HTML, case 6 for "No HTML today", cases 2/19
for simple chat, case 3 for real practice, and case 21 for direct help.

These checks cover selection, focus, checkpoint, copied answers, evidence boundary,
adaptation, reuse, offline fallback and accessibility separately. Report each as
observed, failed or NOT OBSERVED; an authored artifact is not a fresh native run,
and automated browser actions are not evidence that a learner understood.

## End-to-end MCP run

Initialize a new workspace with the workshop MCP prompt and visual preference.
Capture minimal state and the generated mental-model lesson. Exercise one wrong
answer, hint/retry, a correct answer, and a changed scenario. Do not create a record
from automated browser interactions. Ask a real learner to return their reasoning;
only then evaluate it and transition to an ordinary Python implementation.

Capture screenshot if practical, files created, state differences, actual learner
interaction (or explicitly NOT OBSERVED), asset reuse, and unnecessary artifacts.
A synthetic browser test verifies mechanics, not learning. Re-run existing
companion A-L and session regressions separately; report any unrun cases honestly.
