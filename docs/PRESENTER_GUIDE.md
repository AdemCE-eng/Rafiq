# Presenter guide

Prepared for the 2026-10-20 presentation. Suggested wording, not claims about
measured learning outcomes. Use the local reviewed files for rehearsal; unpublished
changes are not in the GitHub installer until you choose to publish them.

## Rafiq in 20 seconds

"Rafiq is a learning companion that runs inside an AI assistant. You tell it your
goal and what you already know. It helps you learn a little, try, get feedback,
and improve. When you choose to save progress, it keeps readable evidence and a
next step so you can continue later."

## Rafiq in 1 minute

"There is plenty of information available, but a good answer does not guarantee
learning. Rafiq starts with what you want to be able to do and what you already
know. It chooses a useful next step instead of automatically producing a full
course. You try something, and it uses your reasoning to decide whether to give
a hint, explain differently, or move on. It can use a visual when that helps, or
stay with a simple conversation. Progress can live in files you can read, correct,
and delete. Over time, the aim is for you to choose more of the sources, practice,
and verification yourself. It is instructions for an existing AI host, not a new model."

### Why I built it

Suggested first-person wording:

"I wanted help with the learning process, not just more content. Learners still
struggle to choose what matters, where to start, and how deep to go. When we get
stuck, another long answer may not help. Reading can feel like understanding,
and AI can make it too easy to outsource the thinking. Rafiq asks for a useful
goal and an actual attempt so feedback has something concrete to respond to."

### The core idea

~~~text
Your goal → what you know → one useful idea → your attempt
          → feedback or hint → retry → evidence → next step
~~~

"Not every stage happens every time. If you already understand the background,
we start at the gap. Sometimes a course or book is the sensible path."

### What “adaptive” means

"Two people learning Digital Twins need not follow the same path. Someone
deciding whether the idea fits a building-monitoring problem needs orientation
and decision criteria. Someone already working with a model may need help
testing one assumption. Rafiq changes scope and teaching approach from the
goal, preferences, and actual attempts."

### What memory means

"Rafiq's own learning memory is a folder I choose. It should not just write
'this person understands Digital Twins.' It can record the specific distinction
they explained, what help they used, and what remains uncertain. Those files
help a later session choose a useful next step. They are not a hidden profile."

### Why hints before answers?

"A hint gives you room to make the reasoning step yourself. Your attempt also
shows the tutor where the difficulty is. But this is a default, not a punishment:
if you ask for the answer, Rafiq should give it."

### What the supporting skills do

- **rafiq:** Continue a learning mission with evidence, optional saved state, and gradually less help.
- **tech-research:** Find enough trustworthy information for a technology question or decision.
- **learning-roadmap:** Choose what to learn now, later, or not for this goal.
- **learning-coach:** Teach one concept through attempts, hints, and feedback.
- **learn-new-tech:** Combine the necessary activities for a current technology-learning journey.

"These are independent options. Rafiq does not call the other four skills.
Most learners can install Rafiq alone."

### How Codex loads it

"Codex sees the skill's name and description. When selected, it reads SKILL.md,
then the supporting files it needs. I can select it explicitly with $rafiq."
See [installation](INSTALLATION.md) for the checked paths and commands.

### How Claude loads it

"Claude Code uses its own skills folder and /rafiq command, but reads the same
canonical instruction package. Browser Claude has a separate ZIP upload route."
The format is documented; a live Claude run was not performed in this review.
See [compatibility](portability.md).

### Is Rafiq an app?

"No. This repository contains instructions, references, and templates.
Codex or Claude Code is the application running them."

### Is Rafiq a model?

"No. It uses the model provided by the host. It does not train or ship a model."

### Is Rafiq an AI Agent?

"You can describe the host following Rafiq as a learning agent, but the skill
itself is not an autonomous process. It supplies a workflow to an existing agent.
Nothing in this repository runs between conversations."

### Where is learner memory stored?

"In the learner-selected folder, such as ./learning-workspaces/fractions.
MISSION.md holds the goal; CHECKPOINT.md holds where to resume; optional
LEARNER.md holds useful supplied context; learning-records/ holds bounded evidence.
Optional glossary, sources, and lessons appear only when useful."

### What happens if I delete the learner state?

"Later sessions cannot read those deleted files. Ask to start fresh rather than
reconstructing them from an existing chat. Deleting local files does not erase
the host's chat logs, backups, synced copies, or Git history."

### Does Rafiq need the internet?

"The instructions are local text. The AI host usually needs its service
connection, and current research needs available source access. Generated
ordinary HTML lessons are intended to work locally without a CDN.
Local lesson playback is not the same as an offline AI tutor."

### Does it work for non-programming topics?

"The main skill's workflow can be used for academic and practical topics:
fractions, explaining a scientific concept, or rehearsing a short presentation.
The research and learn-new-tech standalone skills are technology-focused.
Non-programming effectiveness still needs real learner testing."

### What happens when the learner is stuck?

"It diagnoses the specific gap, offers a more useful hint, simplifies the task,
or changes the example or medium. Persistent structural confusion can call for
a focused visual. Missing foundations may call for deeper study. It should not
repeat the same paragraph indefinitely."

### What if the learner just asks for the answer?

"It should give direct help, even if the learner was previously practicing
independently. It can offer an optional changed example afterward."

### What does “evidence of understanding” mean?

"A specific observation: explaining in your own words, applying an idea to a
changed example, predicting with reasons, comparing alternatives, debugging a
mistake, or designing something and explaining the choices. We record how much
help was used. Confidence, a click, or copied AI code is not enough."

## Ten points to remember before presenting

1. Say "instruction package," not new model or standalone app.
2. Start with the learner's goal, not a five-skill architecture tour.
3. Install/select Rafiq explicitly before the demo.
4. Use a disposable fictional workspace; show no personal learning history.
5. Supply an actual attempt; do not let the AI invent a learner reply.
6. Explain that hints are a default and direct answers remain available.
7. Show what was saved, including uncertainty and assistance.
8. Say "documented format compatibility," not "identical behavior on every client."
9. Local state does not imply private/offline inference or erasure of host logs.
10. Have a prepared screenshot or authored example as a clearly labeled fallback.
    A scripted demonstration is not proof of long-term learning.

## Likely audience questions

| Question | Concise answer |
| --- | --- |
| Is this just a prompt? | It is packaged reusable instructions plus references/templates, selected by a Skills-aware host. There is no separate tutoring runtime. |
| Is it an agent? | The host is the agent; Rafiq supplies its learning workflow. It is not independently running software. |
| Does it remember me? | It can use the readable state you authorize and supply. There is no hidden Rafiq profile or automatic search for it. |
| Where does memory live? | In your chosen folder, or in explicitly supplied/exported state when local files are unavailable. |
| Does it send my data anywhere? | Rafiq includes no separate transmission service. The host processes conversation and files under its own data policies; tools may access networks. |
| Can I delete memory? | Yes, the files or selected claims. That does not erase chat logs, backups, sync copies, or published history. |
| Does it work with Claude? | The same format and documented Claude Code layout fit; browser upload is separate. Live Claude behavior was not tested here. |
| Does it work with ChatGPT? | Do not assume a local Codex installation appears in ChatGPT. Product-specific packaging/tools are needed; this repo does not ship a ChatGPT plugin. Pasting instructions is a manual fallback. |
| Why not use ChatGPT normally? | You can ask for similar behavior manually. Rafiq packages repeatable decisions about scope, attempts, evidence, and resuming. It is not a guarantee of better outcomes. |
| Why multiple skills? | Advanced users may want only research, a plan, or tutoring. Beginners need only Rafiq. |
| Can I use it for math? | Yes as a workflow: explain, attempt, get feedback, and apply a changed example; verify correctness and use structured study when needed. |
| Can I use it for programming? | Yes. It emphasizes small real builds and debugging rather than generating the whole solution immediately. |
| Can I use it for non-technical topics? | Yes, for example drafting and rehearsing a short presentation. Domain accuracy and teaching effectiveness need checking. |
| What if it teaches something wrong? | Challenge it with evidence. It should check sources, correct the explanation, repair affected state, and leave understanding unconfirmed until demonstrated. |
| Why does it refuse to give the full solution? | It should not refuse merely to enforce tutoring. Ask directly; hints are the default, not a gate. |
| Does it create a visual for everything? | No. Use visuals when they help a specific gap; otherwise chat, paper, or real practice may be better. |
| Is saved progress a mastery score? | No. Records describe bounded observations and assistance, not global ability or guaranteed retention. |
| Does it run reminders or track me in the background? | No. Suggested review intervals are notes for your return, not scheduled jobs. |
| Is it free? | Repository content is MIT licensed. Host accounts, model use, and external tools can have separate costs. |
| Can I customize it? | Say your preferences, supply a readable preferences file, or fork/edit the skill and reinstall deliberately. |
| Can I switch from Codex to Claude Code? | Use the same authorized workspace if both can access it, and name it explicitly. Avoid simultaneous conflicting edits. |

## A 3–5 minute live demonstration

Rehearse before the presentation on 2026-10-20. Use the locally reviewed skill,
an unused demo folder, and one host already signed in. Do not spend the live
slot installing software or researching a complex technology.

**0:00–0:30 — State the purpose.** Use the 20-second explanation.

**0:30–1:15 — Start.** In Codex chat paste the following; in Claude Code replace
the first token with /rafiq:

~~~text
$rafiq I want to understand adding fractions well enough to explain it to a classmate.
I can add whole numbers. I have four minutes. Hints first, short replies, no HTML.
Keep useful state in ./learning-workspaces/demo-fractions-20261020.
Start with why 1/2 + 1/3 is not 2/5, but let me try the reasoning.
~~~

**1:15–2:15 — Make an attempt.** Respond to the actual question. You may use
"I don't understand why the piece size matters" to show targeted adaptation.
Use a genuinely uncertain answer or disclose that you are acting out a fictional
learner. Let the audience suggest the next step. Do not read a supplied answer
and describe it as independent learning.

**2:15–3:00 — Try again.** Explain the reasoning in your own words. Ask for one
small changed example if time permits; leave it pending if it is not attempted.

**3:00–4:00 — Inspect state.** Say "Save where we are. Show the exact files changed,
what I demonstrated, what help I used, and what remains untested." Open MISSION,
CHECKPOINT, and any justified record. Point out that no record is better than
inventing progress.

**4:00–5:00 — Resume.** In a new chat select Rafiq and say:
"Continue using ./learning-workspaces/demo-fractions-20261020. Read the checkpoint
and choose one next attempt." Show continuity; explain that this is file access,
not proof of long-term retention.

If generation or permissions stall, use the authored fractions example and
explain it is a fallback, not a live result. For a three-minute slot, omit the
new chat and finish by opening the checkpoint.
