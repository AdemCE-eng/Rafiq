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
| 11 Persistent structural confusion | Give a concise MCP host/client/server explanation. Learner attempts a trace, then reports that host and client still feel like the same thing; a visual preference is known. | Change medium to a focused visual/interactive boundary model, then request a meaningful changed-scenario explanation. | Repeat prose, ASCII, analogy, or another text-only quiz as the sole response; generate an entire MCP course. |
| 12 Reverse routing after a visual | Learner returns from the focused artifact with a sound host/client distinction. The remaining gap is implementing `search_notes()` in Python. | Evaluate the reasoning, use concise chat for any small correction, then prefer authentic Python practice. Do not treat artifact interaction alone as evidence. | Generate another artifact merely because visual learning helped earlier, or keep reteaching the resolved structural gap. |

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
