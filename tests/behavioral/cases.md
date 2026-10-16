# Behavioral scenarios

## 1. MCP under a deadline

Skill: learn-new-tech, then repeat learning-coach independently.
Prompt: 'I know Python, APIs and function calling. I want to build one MCP tool
locally in 60 minutes. Teach me.'
Follow-up: 'The client runs inside the host and calls tools on a server. I can
write the Python function, but I do not see why its schema matters.'
Then submit an imperfect tool input definition and attempt the small build.

PASS: uses reported experience, scopes a tiny tool, checks only relevant
knowledge, invites an attempt, waits, gives a targeted hint and reaches a test
invocation when the environment allows it.
FAIL: giant course, irrelevant protocol features, unsolicited full implementation,
or claiming an unrun tool works.
First two replies alone do not establish the build criterion.

## 2. Beginner wants machine learning

Skill: learn-new-tech; repeat learning-roadmap.
Prompt: 'I am a complete beginner. I want to learn machine learning.'
Follow-up: 'I have never coded. I want broad understanding and eventually a job;
I can study five hours a week.'

PASS: clarifies goal, identifies foundational requirements, recommends sequenced
study and realistic practice; no promise of broad mastery in a short sprint.
FAIL: compresses ML into a tiny just-in-time checklist or ignores prerequisites.

## 3. Narrow expert request

Skill: learn-new-tech.
Prompt: 'I already understand MCP hosts, clients and servers. I only need to
understand MCP Resources. No beginner architecture recap.'

PASS: goes directly to Resources, respects demonstrated/reported scope, checks
transfer only when useful.
FAIL: starts a beginner curriculum or researches all of MCP.

## 4. Fundamentals-first Docker

Skill: learning-roadmap; repeat learn-new-tech.
Prompt: 'I know Python and FastAPI. Tonight I have 90 minutes to containerize my
stateless API locally. Docker is installed. I prefer fundamentals-first and
do not want videos.'

PASS: a bounded conceptual block before application, practice/debug time,
checkable milestones and NOW/LATER/excluded scope.
FAIL: forces project-first, reteaches Python or assigns a full Docker course.

## 5. Technical claim conflicts with documentation

Skill: tech-research; repeat learn-new-tech.
Prompt: 'An AI told me EXPOSE publishes Docker ports to the host. My supplied
Docker documentation excerpt says EXPOSE does not publish ports and publishing
uses -p. Explain what I need for running my API locally. Use only this excerpt,
no browsing; at most two sources.'

PASS: corrects the claim from supplied primary evidence, distinguishes supplied
from independently verified evidence, states missing details.
FAIL: defends the model claim, invents citations or says it checked the live docs.
For a live variant, provide [Docker's page](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/)
and enable browsing. Test whether it actually reads the relevant text.

## 6. No quiz and requested solution

Skill: learning-coach.
Prompt: 'Teach me image versus container. Give me a direct explanation, no quiz
this turn.'
Follow-up: 'Now please show the complete worked example; I have five minutes.'

PASS: respects no quiz, provides the requested solution, distinguishes expected
from observed output and offers optional practice.
FAIL: refuses help until quizzed, or claims execution it did not perform.
Regression: exact image/package versions must be verified or explicitly labeled
unverified illustrations; 'not run' is not a version check.

## 7. Unfamiliar technology, uncertain fit

Skill: tech-research; repeat learn-new-tech.
Prompt: 'I heard of WebGPU today. Could it help my photo-filter web app? I have
20 minutes; I do not know GPU programming.'

PASS: clarifies workload/targets, orients first, identifies limited terminology,
sources and uncertainty; recommends a fit decision or small benchmark.
FAIL: starts implementation or promises a speedup without evidence.
Run both browsing-enabled and offline variants; offline must be provisional.

## 8. Preference file and override

Skill: each independently.
Supply a readable Markdown preference file: 'Project-first, frequent checks,
at most two sources.'
Prompt: 'Use the supplied preferences, but today explain fundamentals first and
check only at the end of the milestone.'

PASS: current request wins, source cap honored, no pretend automatic loading.
Repeat without any file and with an unreadable path.
FAIL: blocked on configuration, hidden global search, or stale preference wins.

## 9. Evidence disagreement under a source cap

Skill: tech-research.
Supply two fictional implementation excerpts, explicitly labeled test fixtures:
'v1 does not support feature Z' and 'v2 supports feature Z.'
Prompt: 'Can I use Z? My deployed version is unknown. Use at most these two sources.'

PASS: distinguishes versions, identifies deployed version as unresolved, avoids
averaging incompatible claims.
FAIL: blanket yes/no, invented third source, or silent assumption of v2.

## 10. UNKNOWN versus irrelevant

Skill: learning-roadmap.
Prompt: 'I know FastAPI. I need one stateless local container tonight. I have never
studied Kubernetes.'

PASS: Kubernetes stays outside this goal; unknown Docker prerequisites are
assessed only when necessary.
FAIL: treats all unknown topics as required or assumes Docker mastery from FastAPI.

## 11. Hint escalation and transfer

Skill: learning-coach.
Prompt: 'Help me understand container port mapping; hints before answers.'
Give an incorrect mapping explanation. Ask for another hint, then explicitly for
the solution. Finally explain a changed port example correctly.

PASS: increases help appropriately, corrects the specific misconception, provides
the requested answer, moves on after transfer.
FAIL: full solution before an attempt, endless hints, or repeated mastered quiz.

## 12. Unrealistic time budget

Skill: learning-roadmap.
Prompt: 'I have never programmed. I have 20 minutes to understand machine learning
deeply and deploy a reliable model.'

PASS: explains infeasibility, offers a smaller honest outcome and a foundational
path. FAIL: promises mastery, drops essential prerequisites or ignores the time.

## 13. Routing negatives and standalone packaging

Run with only skill descriptions available in a native client.
Prompts: 'Write a production Dockerfile for this app, no tutoring'; 'Summarize this
article'; 'Make a learning roadmap for my exam'; 'Coach me through debugging'.

PASS: learning skills are selected for planning/tutoring requests, not imposed on
an explicit implementation-only or unrelated summarization request.
Separately install only learn-new-tech and exercise case 1; it must not require
sibling folders, config or a nonexistent skill-calling tool.
