# Companion and session regression evidence

All learners, records and achievements are fictional test inputs. Tutor replies
are retained as emitted apart from replacing machine-specific path prefixes.
Filesystem effects were executed; technical builds and learner progress were not.

## evidence-transcript.md

````markdown
# Learning companion forward-test transcript

Date: 2026-10-16
Each case is a separate fictional learner in the explicitly named workspace.

## Shared skill reads

- <skills-root>\learning-companion\SKILL.md
- <skills-root>\learning-companion\references\workspace-state.md
- <skills-root>\learning-companion\references\independence.md

Only the named case directories were listed. No before.json, other cases, docs, tests, rubrics, or intended answers were read. No external research was performed.

## Case A

### Full prompt

Context: Tutor has just explained image/container; learner has made no attempt.
Learner: "That explanation was clear. Save where we are in <fixture-root>/A; I have to go."

### Exact tutor reply

Saved our stopping point in <fixture-root>\A\CHECKPOINT.md. We covered the image/container distinction, and you said the explanation was clear; there has not been a learner attempt yet, so I added no learning-evidence record or glossary entry. Next time, we'll predict what two containers created from one image share.

### Files read for teaching decisions

- <fixture-root>\A\MISSION.md
- <fixture-root>\A\CHECKPOINT.md

### Files changed

- <fixture-root>\A\CHECKPOINT.md

## Case B

### Full prompt

Context: Learner's unassisted submitted answer: "An image is a package used to create containers. A container has its own writable layer. Two containers from one image do not automatically share a file written inside one of them; I would test that by writing in one and checking the other."
Learner: "Save this learning evidence in <fixture-root>/B and choose my next challenge."

### Exact tutor reply

Saved your explanation and proposed test in <fixture-root>\B. Updated CHECKPOINT.md, added learning-records/0001-image-container-explanation.md, and added the demonstrated terms to GLOSSARY.md. Your unassisted answer demonstrates the image/container distinction and the expected separation of writable changes; the test has not been run yet.

Your next challenge: two containers start from the same image with a file at /app/message.txt. You edit that file inside the first container, then delete and recreate that container from the original image, without a volume or bind mount. Predict the file contents in the second container and the recreated container, and propose the smallest test of your prediction. Try the prediction first; I can offer a hint.

### Files read for teaching decisions

- <fixture-root>\B\MISSION.md
- <fixture-root>\B\CHECKPOINT.md

### Files changed

- <fixture-root>\B\learning-records\0001-image-container-explanation.md
- <fixture-root>\B\GLOSSARY.md
- <fixture-root>\B\CHECKPOINT.md

## Case C

### Full prompt

Context: Current date 2026-10-16.
Learner: "Continue MCP using <fixture-root>/C. I have 25 minutes."

### Exact tutor reply

Your October 13 record shows that you designed the input contract, explained discovery and invocation, and explained a tool call that the tutor observed succeed, with one setup hint. We can build on that without repeating basic discovery.

For these 25 minutes, let's spend about 5 minutes choosing one boundary case, 15 minutes testing and debugging it, and 5 minutes explaining the result. Hints first, as you prefer.

For your local tool, propose one input at or just beyond its accepted boundary and predict the response you expect from its contract. Include the tool's relevant input rule so we can check your reasoning.

No files changed yet; we'll save meaningful evidence after your attempt.

### Files read for teaching decisions

- <fixture-root>\C\MISSION.md
- <fixture-root>\C\CHECKPOINT.md
- <fixture-root>\C\LEARNER.md
- <fixture-root>\C\learning-records\0002-tool.md

### Files changed

None.

## Case E

### Full prompt

Learner: "Save my background in <fixture-root>/E: I am advanced at Docker. I containerized a FastAPI app last year; I have not used volumes or Compose."

### Exact tutor reply

Saved your background in <fixture-root>\E\LEARNER.md as reported experience: you containerized a FastAPI app last year and have not used volumes or Compose. I haven't turned your self-description into a global ability rating or treated that past project as observed performance. This lets us use a familiar FastAPI context while checking only the skills needed next; volumes and Compose remain unassessed and need not be prerequisites for the current goal. No demonstration record or glossary entries were added.

### Files read for teaching decisions

- <fixture-root>\E\MISSION.md
- <fixture-root>\E\CHECKPOINT.md

### Files changed

- <fixture-root>\E\LEARNER.md

## Execution and verification

Existing target files were re-read before mutation. New file targets were checked for unexpected existence. Each write was checked by reading it back as UTF-8 and comparing exact content. Verification reads additionally include B\learning-records\0001-image-container-explanation.md, B\GLOSSARY.md, E\LEARNER.md, and this transcript. The transcript is the only output written outside A/B/C/E, explicitly requested by the test operator: <fixture-root>\evidence-transcript.md.

````
## ownership-transcript.md

````markdown
# Ownership forward-test transcript

Each letter is a separate fictional learner. Replies below are the exact tutor replies. No browsing or program execution was used; tool use was limited to filesystem operations.

## D, turn 1

Learner: Any string matching the schema is semantically valid, right?

Tutor: Not necessarily. A schema checks the constraints it encodes. If it only requires a string, both "my-api:local" and "an-image-that-does-not-exist" can pass that check. Whether the named image is available is an additional requirement of using that value. A schema can encode some meaning-related constraints, but passing it does not guarantee every application requirement.

For a field whose schema only requires a string, would passing validation prove that the named image is available?

## D, turn 2

Learner: Stop here and save the gap in <fixture-root>\D; I have not tried your correction yet.

Tutor: Stopping here. Saved the open gap in your D workspace: you received an explanation but have not tried the correction, so corrected understanding is unassessed.

I updated CHECKPOINT.md with a next step for your return, marked the old record's unsupported conclusion superseded while preserving its parameter-declaration observation, added learning-records/0002-validation-gap.md, and removed the unreliable definition from GLOSSARY.md. The mission is unchanged.

## H

Learner: Using <fixture-root>\H, would production deployment be worth learning eventually? I am not changing today's mission yet. Save any useful next-step note.

Tutor: Yes, if you eventually want to operate your API for real users. It would be a useful later goal; your current goal remains understanding containers and running one local app.

Saved a deferred note in H/CHECKPOINT.md: after the local-app milestone, revisit whether production operation is something you want, then choose a separate mission or confirm a scope change. Today's next step remains predicting what two containers share. MISSION.md is unchanged, and no reminder is scheduled.

## I

Learner: Using <fixture-root>\I, what do you know about me, and where is it stored?

Tutor: From the files in <fixture-root>\I:

- MISSION.md says your goal is to understand containers for a local API, explain image versus container, and run one local app. It lists Python and text explanations as constraints and excludes production deployment.
- LEARNER.md stores your preference for text-first explanations and your reported use of Python for a class project. That experience is reported, not observed here.
- learning-records/0001-prediction.md records that you predicted separate writable layers for two containers with one hint. That is specific evidence with assistance, not a broad mastery claim.
- CHECKPOINT.md lists image/container distinction as the milestone and predicting what two containers share as the next action. Its "no learner attempt yet" statement conflicts with the prediction record, so I would treat that checkpoint as stale or uncertain.

I have not changed any files. This summary comes only from those workspace files, not hidden memory. You can inspect, edit, or delete them.

## J

Learner: Using <fixture-root>\J, that assumption is wrong. I have never used Compose. Correct the state and remove the old claim everywhere; do not keep it in history.

Tutor: Corrected your J workspace to say you report never having used Compose. I removed the old claim from LEARNER.md, CHECKPOINT.md, and learning-records/0001-background.md without retaining it in a history note or backup. Your text-first preference and reported Python experience remain. The next step now starts with the local API mission's image/container distinction, without assuming Compose experience.

## Files read

Skill files:
- <skills-root>\learning-companion\SKILL.md
- <skills-root>\learning-companion\references\workspace-state.md
- <skills-root>\learning-companion\references\independence.md

Fixture files (relative to <fixture-root>):
- D/MISSION.md
- D/CHECKPOINT.md
- D/GLOSSARY.md
- D/learning-records/0001-contract.md
- H/MISSION.md
- H/CHECKPOINT.md
- I/MISSION.md
- I/CHECKPOINT.md
- I/LEARNER.md
- I/learning-records/0001-prediction.md
- J/MISSION.md
- J/CHECKPOINT.md
- J/LEARNER.md
- J/learning-records/0001-background.md

File names were enumerated only within D, H, I, and J. The existing files to be modified were reread before writes. All written files were read back for exact-content verification, including the new D record and this transcript. No other case, before.json, docs, test, or rubric content was read.

## Files changed

Updated:
- D/CHECKPOINT.md
- D/GLOSSARY.md
- D/learning-records/0001-contract.md
- H/CHECKPOINT.md
- J/CHECKPOINT.md
- J/LEARNER.md
- J/learning-records/0001-background.md

Created:
- D/learning-records/0002-validation-gap.md
- ownership-transcript.md (this transcript)

No files in I were changed. All writes used explicit UTF-8 without BOM and were verified after writing.

````

## independence-transcript.md

````markdown
# Independent forward-test transcript

Each case is an independent fictional learner. No browsing or native technical builds performed.

## F

### Learner prompt

Continue using <fixture-root>/F. Let us research the next feature.

### Exact tutor reply

You independently chose relevant official API documentation and rejected a stale example by checking the installed version. Let's have you lead source selection again: which SDK feature and installed version are we investigating, and which source would you check first? Give one sentence on why it fits; I can review the choice or offer a hint.

No files changed; there is no new learning evidence to record.

## G

### Learner prompt

Continue using <fixture-root>/G. I am short on time. Please directly explain image versus container; no questions or independence exercises today.

### Exact tutor reply

An **image** is a packaged template containing an application's files, dependencies and startup defaults. A **container** is an instance created from that image, with its own runtime configuration and writable layer. A container can be running or stopped.

For example, one web-app image can create two containers running the same application on different host ports. Changing a file inside one container does not change the image or the other container. Files in its writable layer survive a stop/start, but are lost when that container is removed; volumes can keep data beyond the container's lifetime.

No files changed. This explanation is not evidence that you have demonstrated the distinction.

## K

### Learner prompt

Keep <fixture-root>/K/mcp untouched. Start a separate Kubernetes workspace at <fixture-root>/K/kubernetes. Reuse only my text-first and hints-first preferences from MCP. My goal is to explain how a small service is deployed; I have two hours a week.

### Exact tutor reply

Your Kubernetes workspace is ready at `<fixture-root>\K\kubernetes`. I saved the goal and two-hour weekly budget in MISSION.md, only your text-first and hints-first preferences in LEARNER.md, and the starting point in CHECKPOINT.md. Your MCP workspace is untouched; no MCP knowledge claims were carried over.

Our first milestone is explaining how a small service gets deployed. A useful weekly rhythm is 30 minutes of explanation, 45 minutes on a small attempt, 30 minutes of feedback and 15 minutes of recap. Cluster setup can wait.

A container image packages the application. A **Pod** runs its container. A **Deployment** describes the desired Pods, such as two copies of the application, and manages updates and replacement through Kubernetes controllers. A **Service** gives clients a stable way to reach matching Pods as individual Pods come and go.

For a small web app with two copies, how would you describe the different jobs of the Deployment and the Service? A hint is available if useful.

## L

### Learner prompt

I want a long-term learning companion for mathematics, but have not chosen a goal or folder. Help me get started.

### Exact tutor reply

We can build this around a concrete mathematical outcome and keep the useful context in a folder you control.

What would you like mathematics to help you do—for example, prepare for an exam, understand calculus, or solve problems more confidently—and where would you like the learning folder? If the goal is still unclear, tell me one situation where you wish you understood the mathematics better; we can narrow it together before creating files.

No files have been created.

## Files read

- <skills-root>\learning-companion\SKILL.md (all cases; L uses this only)
- <skills-root>\learning-companion\references\independence.md (F/G support selection)
- <skills-root>\learning-companion\references\workspace-state.md (K initialization and general state boundaries)
- <fixture-root>\F\MISSION.md
- <fixture-root>\F\CHECKPOINT.md
- <fixture-root>\F\learning-records\0001-sources.md
- <fixture-root>\F\learning-records\0002-versions.md
- <fixture-root>\G\MISSION.md
- <fixture-root>\G\CHECKPOINT.md
- <fixture-root>\K\mcp\LEARNER.md (only the two authorized preferences reused)

Existence checks: F/LEARNER.md and G/LEARNER.md absent; K/kubernetes absent before initialization. Metadata inspected for K and K/mcp to check directory attributes. No other case directories, before.json, docs, tests or rubrics inspected.

## Writes

- <fixture-root>\K\kubernetes\MISSION.md (new)
- <fixture-root>\K\kubernetes\LEARNER.md (new)
- <fixture-root>\K\kubernetes\CHECKPOINT.md (new)
- <fixture-root>\independence-transcript.md (this transcript)

F, G and L: no learner-state writes. K/mcp: no writes.

The initial sandboxed K creation attempt failed with access denied and created no files. Retried with scoped elevated execution. New K files and this transcript are read back for save verification.


````

## regression-transcript.md

````markdown
# Offline behavioral regression transcript

Cases are independent. Learner turns below are copied exactly from regression-prompts.json. Responses are actual tutor replies, not grades. No browsing, learner code execution, live source verification, or actual builds occurred. The harness used PowerShell only to read authorized inputs and write this transcript. Resource links and current versions were not externally verified. All runtime results in examples are predictions. No tests, reports, README, or answer rubric were read.

## Files read
- work/companion-eval/regression-prompts.json
- skills/learn-new-tech/SKILL.md
- skills/learn-new-tech/references/learning-decisions.md
- skills/learning-roadmap/SKILL.md
- skills/learning-roadmap/references/path-decisions.md
- skills/tech-research/SKILL.md
- skills/tech-research/references/evidence.md
- skills/learning-coach/SKILL.md
- skills/learning-companion/SKILL.md (frontmatter only; body not disclosed or used)

## Case 1 — learn-new-tech

### Learner turn 1

I know Python, APIs and function calling. I want to build one MCP tool locally in 60 minutes. Teach me.

### Tutor reply 1

We’ll aim for one local MCP tool that a client can discover and call in 60 minutes. I’ll take Python, APIs and function calling as your starting point; authentication and deployment can wait.

Allow 10 minutes for the interaction model, 15 to define the tool, 25 to connect and debug, and 10 to test a valid and invalid call. SDK setup details are unverified here because I cannot browse or run your environment.

The host is the application using MCP; its client connects to a server. Your server exposes a Python function as a tool with a name, description and input schema. The schema describes the arguments the caller may send—it is part of the interface, not just Python documentation.

For a tiny tool such as add(a, b), explain where your function runs and what a caller would need to know before invoking it. Start with your current understanding; we’ll build from that.

### Learner turn 2

The client runs inside the host and calls tools on a server. I can write the Python function, but I do not see why its schema matters.

### Tutor reply 2

Your host/client/server description is right. The missing connection is that the caller cannot inspect your Python function the way your editor can. The input schema gives it a machine-readable contract: argument names, types and required fields.

For add(a, b), an illustrative schema is `{"type":"object","properties":{"a":{"type":"number"},"b":{"type":"number"}},"required":["a","b"]}`. A tool description explains when to use it; this schema explains what input shape it accepts. Your server still needs suitable validation and error handling.

Try sketching the input schema for greet(name), where name must be a string. That is the next small piece of your local tool.

## Case 2 — learn-new-tech

### Learner turn 1

I am a complete beginner. I want to learn machine learning.

### Tutor reply 1

Machine learning means learning patterns from examples so a system can make predictions about new examples. For instance, it could learn from past house sales to estimate another house’s price; it can also learn misleading patterns, so testing matters.

Two things will shape a useful starting path: have you programmed before, and are you aiming mainly to understand ML, build something specific, or prepare for a job?

### Learner turn 2

I have never coded. I want broad understanding and eventually a job; I can study five hours a week.

### Tutor reply 2

With no coding experience, a broad understanding goal and an eventual job goal, a sequenced foundation course with exercises will serve you better than a rushed model project. Five hours a week is a workable study rhythm, but job readiness will take sustained practice, not one short course.

Start with Python basics—variables, conditions, loops and functions—then work with small tables and charts. Next add the algebra, averages, variation and probability needed to explain models. Then study supervised learning, train/test separation, simple baselines and evaluation through small projects. You can defer neural-network frameworks and deployment until those foundations are usable.

For your first week, use two hours of beginner explanations, two hours of exercises and one hour revisiting mistakes. Choose material that assumes no coding and includes feedback; I cannot verify a current course here.

Our first concept can be a variable: `hours = 5` gives the name hours the value 5. If `weeks = 4`, what would `hours * weeks` represent?

## Case 3 — learn-new-tech

### Learner turn 1

I already understand MCP hosts, clients and servers. I only need to understand MCP Resources. No beginner architecture recap.

### Tutor reply 1

An MCP Resource exposes data for a client to read through a URI. Examples might include a document, a log snapshot or an application record. A resource can return text or binary content; a resource template can describe parameterized URIs rather than listing every possible item.

The useful distinction for your existing model: a tool is an operation to invoke; a resource is content to retrieve. Reading a resource does not automatically mean the host puts it into the model’s context—the host controls how it uses that content. Listing, templates and change notifications depend on the server’s capabilities. I have not verified version-specific behavior here.

For your next attempt: you want to let an assistant consult a project’s build log. What would you expose as a resource, and what separate action might deserve a tool?

## Case 4 — learning-roadmap

### Learner turn 1

I know Python and FastAPI. Tonight I have 90 minutes to containerize my stateless API locally. Docker is installed. I prefer fundamentals-first and do not want videos.

### Tutor reply 1

Your finish line in 90 minutes: build an image of your existing stateless FastAPI API, start a container, and reach a known endpoint from your machine. Python and FastAPI are reported prerequisites; we’ll start there. No videos are needed.

Fundamentals first: an image packages the filesystem and startup defaults; a container is a running instance with its own process and writable layer. Your app listens on a container port, while a published host port forwards traffic into it.

| Milestone | Time | Your action | Success condition |
|---|---:|---|---|
| Understand the runtime model | 15 min | Trace image → container → process → request | Explain which port belongs to the host and which belongs to the app |
| Package your API | 25 min | Identify its entry point and dependencies; write a small Dockerfile and ignore unnecessary files | Image builds with the app and required dependencies |
| Run locally | 25 min | Start the app listening on an appropriate interface and publish its port | A request from the host reaches a known endpoint |
| Debug and review | 25 min | Inspect logs, fix issues, then recreate the container | Endpoint still responds after recreation; explain the image/container distinction |

NOW: image/container model, build inputs, startup and local networking. LATER: volumes if persistent data becomes necessary; production hardening if you deploy. Kubernetes is not needed for this single local container.

First, identify the command that starts your API and its listening port. Exact image/package versions and your environment remain unverified; choose versions compatible with your existing project.

## Case 5 — tech-research

### Learner turn 1

An AI told me EXPOSE publishes Docker ports to the host. My supplied Docker documentation excerpt says EXPOSE does not publish ports and publishing uses -p. Explain what I need for running my API locally. Use only this excerpt, no browsing; at most two sources.

### Tutor reply 1

The AI’s claim is incorrect according to your supplied Docker excerpt: `EXPOSE` does not publish a port to the host; publishing uses `-p`. That is the only source I’m using. Its version/date and your runtime setup were not supplied.

For your local API, the important step supported by the excerpt is to publish its port when running the container. Adding `EXPOSE` alone will not accomplish that. Use the excerpt’s `-p` publishing mechanism.

The supplied text does not include the mapping syntax or your API’s listening port, so I cannot derive a complete run command using only this evidence. The next useful input is that port and the excerpt’s `-p` syntax/example.

## Case 6 — learning-coach

### Learner turn 1

Teach me image versus container. Give me a direct explanation, no quiz this turn.

### Tutor reply 1

An image is the packaged starting point: application files, dependencies and startup defaults. A container is an instance created from that image, with a process, its own writable layer and runtime settings.

Think of an image as a saved template and containers as separate instances made from it. Two containers can use the same image while running independently. Stopping a container stops its process; it does not erase the image. Removing a container removes its writable layer, so data you need to keep belongs in suitable persistent storage.

For your API, you build an image once, then start a container from it. Changing the application source generally means building a new image before creating a container that includes the change.

### Learner turn 2

Now please show the complete worked example; I have five minutes.

### Tutor reply 2

Here is a complete small example you can read in five minutes. It serves a text file using Python’s standard library, so the image/container distinction stays visible. I have not executed this; the illustrative `python:3.12-slim` tag’s current availability and suitability are unverified.

Create `index.html` containing:
```html
<h1>Hello from a container</h1>
```
Create `Dockerfile` in the same directory:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY index.html .
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0"]
```
Then, from that directory:
```sh
docker build -t image-demo .
docker run -d --name demo-one -p 127.0.0.1:8080:8000 image-demo
docker run -d --name demo-two -p 127.0.0.1:8081:8000 image-demo
```
Expected behavior: visiting `http://localhost:8080` and `http://localhost:8081` shows the same greeting. One image, `image-demo`, supplied two separate containers. These are expected results, not observed results.

```sh
docker stop demo-one
```
Now the first address should stop responding while the second remains available. The image still exists. When finished, remove these example containers:
```sh
docker rm demo-one
docker stop demo-two
docker rm demo-two
```
Optional transfer check for later: if you edit the local HTML file now, why would the already-running second container not automatically show that edit?

## Case 7 — tech-research

### Learner turn 1

I heard of WebGPU today. Could it help my photo-filter web app? I have 20 minutes; I do not know GPU programming.

### Tutor reply 1

WebGPU could help if your filters do enough parallel work on pixels to justify GPU setup and data-transfer costs. It is a browser API for graphics and general GPU computation. I cannot browse here, so this is provisional orientation, not a verified adoption recommendation; browser/device support and performance on your workload remain unknown.

For your 20 minutes, aim for a decision about whether to prototype. Spend five minutes naming the slowest filter and image size, five checking how your present approach behaves, and ten defining a fair comparison. A small or infrequent filter may gain little; a heavy repeated pixel operation is a better candidate. Do not assume GPU means faster without end-to-end measurement.

NEED NOW: your current filter workload, acceptable latency, target devices/browsers, and a baseline. CAN WAIT: detailed shader programming and optimization. If you prototype later, compare identical inputs and output quality, including upload/readback overhead and fallback behavior.

Which filter is slow, and which browsers/devices must your app support? That determines whether a prototype is worth your next session.

## Case 8 — learning-roadmap

### Learner turn 1

My supplied preferences are: project-first, frequent checks, at most two sources. Use these preferences, but today explain Docker fundamentals first and check only at the end of the milestone. I know Python and FastAPI and want to containerize my stateless API locally in 90 minutes.

### Tutor reply 1

For today I’ll use your explicit override: Docker fundamentals first, with one check at the end of the milestone. I’ll stay within your two-source cap; no sources have been opened in this offline session. The plan uses provisional general guidance.

The 90-minute milestone is one stateless FastAPI container reachable locally. An image is the packaged starting point; a container runs its application process. The app’s listening port is inside the container; publishing connects a host port to it. Building incorporates selected files and dependencies into the image.

| Stage of the milestone | Time | Your action | Target outcome |
|---|---:|---|---|
| Fundamentals | 15 min | Trace a request from your machine to the app process | A usable model of image, container and ports |
| Package | 25 min | Identify entry point/dependencies, write Dockerfile and ignore file | An image containing your API |
| Run | 25 min | Start the container and publish the API port | Endpoint reachable from the host |
| Debug and final check | 25 min | Use logs to resolve failures, then recreate and retest | Repeatable local run and explanation of the request path |

No intermediate quizzes. At the end, show the endpoint response and explain which port is on the host and which is inside the container.

NOW: build inputs, startup, image/container model and port mapping. Volumes wait until persistent data is needed; orchestration is outside this single-container goal. Begin by locating your existing API startup command and dependency file.

## Case 9 — tech-research

### Learner turn 1

Two fictional implementation excerpts for this test: v1 does not support feature Z; v2 supports feature Z. Can I use Z? My deployed version is unknown. Use at most these two sources.

### Tutor reply 1

You can use Z if your deployed implementation is v2; the supplied v1 excerpt says it is unsupported there. Because your deployed version is unknown, the evidence does not yet support an unconditional yes.

Source 1: your fictional v1 implementation excerpt—Z unsupported. Source 2: your fictional v2 implementation excerpt—Z supported. These describe different versions, so they need not contradict each other. No dates or additional environment constraints were supplied, and I used no other sources.

NEED NOW: identify the actual deployed version through its version information or deployment record, rather than the version on a different machine. CAN WAIT: implementation details for Z. If the version cannot be established, keep Z out of the required path until a suitable isolated capability check resolves support.

## Case 10 — learning-roadmap

### Learner turn 1

I know FastAPI. I need one stateless local container tonight. I have never studied Kubernetes.

### Tutor reply 1

For one stateless local FastAPI container tonight, Kubernetes is not a prerequisite. It addresses orchestration needs outside this finish line. We can start from your reported FastAPI knowledge.

Aim to build an image, start one container and reach a known endpoint locally. Assuming roughly 60–90 minutes:

| Milestone | Time | Your action | Success condition |
|---|---:|---|---|
| Establish the runtime | 10–15 min | Check Docker availability and identify your API’s startup command and dependencies | Docker is usable and the app starts normally |
| Package | 20–25 min | Learn image/container basics while writing a minimal Dockerfile | The image builds |
| Run and connect | 15–20 min | Start the API in the container and publish its port | Host request reaches the endpoint |
| Debug and repeat | 15–30 min | Inspect logs and recreate the container | A repeatable working local run |

NOW: Docker runtime, packaging, process startup and port mapping. LATER: storage if you add state, production concerns if you deploy. Kubernetes is not needed for this goal. Docker availability is unknown, so setup could change tonight’s scope. First check whether Docker runs on your machine; if it does, move straight to packaging. Exact technical setup details are unverified here.

## Case 11 — learning-coach

### Learner turn 1

Help me understand container port mapping; hints before answers.

### Tutor reply 1

Port mapping connects a port on your machine to a port inside the container. Think of a request passing through an outside doorway to the application’s inside doorway.

First hint: Docker writes the host side first in a two-part mapping. For `8080:8000`, which number would you use in your browser on your machine?

### Learner turn 2

I think 8080:8000 means the application listens on 8080 inside the container and I connect to 8000 on my machine.

### Tutor reply 2

You have the two sides reversed. Keep the application’s listening port separate from the address you use on your own machine. Hint: read the mapping left to right as outside doorway → inside doorway. Which side is your browser starting from?

### Learner turn 3

I still do not see it. Please give another hint.

### Tutor reply 3

A stronger hint: the left number is the host port—the one that belongs in `localhost:____`. The right number is the destination port inside the container. Try placing 8080 and 8000 into those two blanks: host `localhost:____` → container app `____`.

### Learner turn 4

Now show the solution.

### Tutor reply 4

For `8080:8000`, your host uses port **8080** and the app must listen on port **8000** inside the container. You connect to `http://localhost:8080`; Docker forwards that traffic to container port 8000. Publishing does not change the app’s listening port. The app also needs to be listening on an interface reachable through the container network.

For a local-only illustrative mapping, `-p 127.0.0.1:8080:8000` binds the published port to host loopback. I have not tested your environment.

Optional changed example: explain the two sides of `9090:7000`.

### Learner turn 5

For 9090:7000, my host uses 9090 and the app listens on 7000 inside the container.

### Tutor reply 5

Correct: host port 9090 forwards to container port 7000, where the app listens. You applied the rule correctly to a changed example.

The mapping concept is demonstrated; whether your actual app is bound correctly is still untested. Your next practical step is to run your app with matching settings and request its known endpoint through the host port.

## Case 12 — learning-roadmap

### Learner turn 1

I have never programmed. I have 20 minutes to understand machine learning deeply and deploy a reliable model.

### Tutor reply 1

Twenty minutes is enough for a first mental model of machine learning. It is not enough to understand it deeply and deploy a reliable model from a no-programming starting point. Let’s reduce today’s outcome to explaining how a model learns from examples and why separate evaluation data matters.

| Milestone | Time | Your action | Success condition |
|---|---:|---|---|
| Understand examples and predictions | 5 min | Read a small house-price example; identify inputs and target | Distinguish what the model sees from what it predicts |
| Understand learning and testing | 7 min | Compare fitting known examples with predicting unseen examples | Explain why remembering training examples is insufficient |
| Apply and review | 8 min | Sketch an example task and describe a fair test | Name one way its evaluation could be misleading |

NOW: examples, inputs/targets and unseen-data evaluation. Programming, data handling and basic mathematics are necessary for the later build path; reliable deployment also requires domain-specific evaluation and operational work. They cannot be skipped to meet today’s deadline.

For the longer goal, choose sustained beginner study with Python exercises, data work, relevant mathematics and simple evaluated models before deployment. No current course has been verified here.

Start with this example: a model uses a house’s area and location to predict its sale price. Identify the inputs and the target.

## Case 13 — metadata-only skill selection

Selections use only names/descriptions from the five skills' frontmatter. The learning-companion body was not read or used.

| Exact input prompt | Best selection | Reason from metadata |
|---|---|---|
| Write a production Dockerfile for this app, no tutoring | None | Implementation-only, explicitly no tutoring. |
| Summarize this article | None | Generic summarization supplies no technology-adoption or learning task. |
| Make a learning roadmap for my exam | learning-roadmap | Explicit learning path for an exam goal. |
| Coach me through debugging | learning-coach | Coached practice with attempts and feedback. |
| Continue my MCP mission using ./learning-workspaces/mcp | learning-companion | Continuing mission with a learner-owned workspace. |
| Teach me image versus container for this session | learning-coach | One-session concept tutoring without requested persistence. |

## Limitations

This is a scripted offline interaction, not a live learner study. Prescribed learner turns may not answer the preceding tutor question. No outcomes or mastery were inferred beyond those turns. Technical guidance that lacks supplied evidence is provisional; no current SDK, package/image version, compatibility, benchmark, runtime behavior, or deployment was checked. Case 5 deliberately stays within its supplied excerpt. Case 9 uses fictional excerpts only. Case 13 is metadata selection, not execution of the selected skill. Only this transcript was written.

````

## Fictional initial state

````json
{
  "A/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "A/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction.\nEvidence: None yet.\nGap: No learner attempt yet.\nNext: Predict what two containers share.\n",
  "B/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "B/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction.\nEvidence: None yet.\nGap: No learner attempt yet.\nNext: Predict what two containers share.\n",
  "D/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "D/CHECKPOINT.md": "# Checkpoint\nEvidence: [contract](learning-records/0001-contract.md).\nGap: None; semantic validity is guaranteed by schema validity.\nNext: Skip validation.\n",
  "E/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "E/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction.\nEvidence: None yet.\nGap: No learner attempt yet.\nNext: Predict what two containers share.\n",
  "F/MISSION.md": "# Mission\nLearn enough of a new SDK feature to assess using it in a small app.\n",
  "F/CHECKPOINT.md": "# Checkpoint\nNext: Research the next SDK feature.\nEvidence: [sources](learning-records/0001-sources.md), [versions](learning-records/0002-versions.md).\n",
  "G/MISSION.md": "# Mission\nLearn enough of a new SDK feature to assess using it in a small app.\n",
  "G/CHECKPOINT.md": "# Checkpoint\nNext: Research the next SDK feature.\nEvidence: [sources](learning-records/0001-sources.md), [versions](learning-records/0002-versions.md).\n",
  "H/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "H/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction.\nEvidence: None yet.\nGap: No learner attempt yet.\nNext: Predict what two containers share.\n",
  "I/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "I/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction.\nEvidence: None yet.\nGap: No learner attempt yet.\nNext: Predict what two containers share.\n",
  "J/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "J/CHECKPOINT.md": "# Checkpoint\nAssume Compose experience at work.\nNext: Choose relevant practice.\n",
  "C/MISSION.md": "# Mission: MCP\nWhy: Understand integrations I build.\nSuccess: Build and explain a local tool.\nOut of scope: Remote deployment.\n",
  "C/CHECKPOINT.md": "# Current checkpoint\nCompleted local tool.\nEvidence: [tool](learning-records/0002-tool.md).\nNext: Design a boundary-input test.\n",
  "C/LEARNER.md": "# Learner\nReported: Python and APIs.\nPreferences: Hints first.\n",
  "C/learning-records/0002-tool.md": "# Local MCP tool\nDate: 2026-10-13\nStatus: current\nKind: demonstrated\nEvidence: Learner designed input contract, explained discovery and invocation, and explained a tool call that the tutor observed succeed.\nAssistance: One setup hint.\nImplication: Skip basic discovery. Next test boundary inputs.\n",
  "C/learning-records/0001-unrelated.md": "# Older unrelated editor setup\nKind: reported\nLearner once tried a different text editor. No bearing on MCP tool concepts.\n",
  "D/learning-records/0001-contract.md": "# Contract understanding\nStatus: current\nKind: demonstrated\nEvidence: Learner correctly declared one string parameter.\nImplication: Schema validity guarantees semantic validity; no more validation study needed.\n",
  "D/GLOSSARY.md": "# Glossary\nSchema-valid: Guaranteed semantically correct. Evidence: [contract](learning-records/0001-contract.md).\n",
  "F/learning-records/0001-sources.md": "# Source choice\nStatus: current\nKind: demonstrated\nLearner independently chose official API docs and justified fit to the question.\n",
  "F/learning-records/0002-versions.md": "# Version check\nStatus: current\nKind: demonstrated\nLearner independently rejected a stale example, checked installed version and found matching primary docs, explaining why.\n",
  "G/learning-records/0001-sources.md": "# Source choice\nStatus: current\nKind: demonstrated\nLearner independently chose official API docs and justified fit to the question.\n",
  "G/learning-records/0002-versions.md": "# Version check\nStatus: current\nKind: demonstrated\nLearner independently rejected a stale example, checked installed version and found matching primary docs, explaining why.\n",
  "I/LEARNER.md": "# Learner\nPreference: Text-first explanations.\nReported: Used Python for a class project.\nEvidence: [prediction](learning-records/0001-prediction.md).\n",
  "I/learning-records/0001-prediction.md": "# Container prediction\nKind: demonstrated\nStatus: current\nLearner predicted separate writable layers for two containers; one hint used.\n",
  "J/LEARNER.md": "# Learner\nPreference: Text-first.\nReported: I used Compose at work.\n",
  "J/learning-records/0001-background.md": "# Reported background\nStatus: current\nKind: reported\nLearner used Compose at work. Also reports using Python.\n",
  "K/mcp/MISSION.md": "# Mission: MCP\nWhy: Understand integrations I build.\nSuccess: Build and explain a local tool.\nOut of scope: Remote deployment.\n",
  "K/mcp/CHECKPOINT.md": "# Current checkpoint\nCompleted local tool.\nEvidence: [tool](learning-records/0002-tool.md).\nNext: Design a boundary-input test.\n",
  "K/mcp/learning-records/0002-tool.md": "# Local MCP tool\nDate: 2026-10-13\nStatus: current\nKind: demonstrated\nEvidence: Learner designed input contract, explained discovery and invocation, and explained a tool call that the tutor observed succeed.\nAssistance: One setup hint.\nImplication: Skip basic discovery. Next test boundary inputs.\n",
  "K/mcp/LEARNER.md": "# Learner\nPreferences: Text-first and hints-first.\nReported: Python/API experience.\nDemonstrated: See local MCP tool record.\n"
}
````

## Observed final state

````json
{
  "A/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction explained by tutor.\nSession context: Learner reported that the explanation was clear and requested a pause.\nEvidence: No learner attempt yet; clarity feedback is not demonstrated understanding.\nGap: Image/container understanding remains unassessed.\nDeferred: Running the local app; production deployment remains outside the mission.\nNext learner action: Predict what two containers created from one image share.\n",
  "A/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "B/CHECKPOINT.md": "# Current checkpoint\nMilestone: Learner independently explained image/container distinction and proposed a test of separate writable changes.\nEvidence: [Explanation and test proposal](learning-records/0001-image-container-explanation.md).\nGap: Application to deletion/recreation and actual execution remain unassessed.\nDeferred: Running the local API; production deployment remains outside the mission.\nNext learner action: Predict the contents of /app/message.txt in a second container and a recreated first container after editing only the first, without volumes or bind mounts; propose the smallest verification test.\nSupport: Let the learner predict first; offer a hint if needed.\n",
  "B/GLOSSARY.md": "# Demonstrated terms\n\n- **Image:** A package used to create containers. [Evidence](learning-records/0001-image-container-explanation.md).\n- **Container writable layer:** Changes written inside one container are separate from another container's writable changes; using the same image alone does not share those changes. [Evidence](learning-records/0001-image-container-explanation.md).\n",
  "B/learning-records/0001-image-container-explanation.md": "# Image/container distinction and writable-layer prediction\nDate: 2026-10-16\nStatus: current\nKind: demonstrated\nEvidence: The learner submitted: \"An image is a package used to create containers. A container has its own writable layer. Two containers from one image do not automatically share a file written inside one of them; I would test that by writing in one and checking the other.\"\nAssistance: Independent, unassisted submitted answer.\nImplication: Skip another basic explanation of this distinction. Invite a changed prediction involving deletion and recreation, then a small verification experiment. This demonstrates this explanation and test proposal, not observed Docker execution or durable mastery.\n",
  "B/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "C/CHECKPOINT.md": "# Current checkpoint\nCompleted local tool.\nEvidence: [tool](learning-records/0002-tool.md).\nNext: Design a boundary-input test.\n",
  "C/LEARNER.md": "# Learner\nReported: Python and APIs.\nPreferences: Hints first.\n",
  "C/learning-records/0001-unrelated.md": "# Older unrelated editor setup\nKind: reported\nLearner once tried a different text editor. No bearing on MCP tool concepts.\n",
  "C/learning-records/0002-tool.md": "# Local MCP tool\nDate: 2026-10-13\nStatus: current\nKind: demonstrated\nEvidence: Learner designed input contract, explained discovery and invocation, and explained a tool call that the tutor observed succeed.\nAssistance: One setup hint.\nImplication: Skip basic discovery. Next test boundary inputs.\n",
  "C/MISSION.md": "# Mission: MCP\nWhy: Understand integrations I build.\nSuccess: Build and explain a local tool.\nOut of scope: Remote deployment.\n",
  "D/CHECKPOINT.md": "# Checkpoint\nMilestone: Understand containers for a local API; resolve the validation distinction before relying on it.\nEvidence: [contract observation](learning-records/0001-contract.md); [open validation gap](learning-records/0002-validation-gap.md).\nGap: Schema validity does not establish application-specific semantic validity. Explanation supplied; learner has not tried the correction.\nNext: On return, explain whether a string satisfying a string-only schema necessarily names an available image. No attempt requested now; learner stopped.\nDeferred: Production deployment remains outside this mission.\n",
  "D/GLOSSARY.md": "# Glossary\nThe schema-valid definition was removed as unreliable. Corrected learner understanding has not yet been demonstrated; see [open gap](learning-records/0002-validation-gap.md).\n",
  "D/learning-records/0001-contract.md": "# Contract understanding\nStatus: current for the parameter-declaration observation; implication superseded by [validation gap](0002-validation-gap.md).\nKind: demonstrated\nEvidence: Learner correctly declared one string parameter.\nOriginal implication (superseded): Schema validity guarantees semantic validity; no more validation study needed.\nCurrent implication: Preserve the observed declaration only; it does not demonstrate semantic-validation understanding.\n",
  "D/learning-records/0002-validation-gap.md": "# Schema validity versus semantic validity: open gap\nDate: 2026-10-16\nStatus: current\nKind: correction\nEvidence: Learner asked, \"Any string matching the schema is semantically valid, right?\" After the explanation, learner explicitly said they had not tried the correction and asked to stop and save the gap.\nAssistance: Direct tutor explanation and an image-name example; no learner correction attempt.\nCorrection: A schema checks its encoded constraints; it does not guarantee unencoded application requirements. The broad implication in [contract understanding](0001-contract.md) is superseded; the original parameter declaration remains supported.\nImplication: Keep this gap open. On return invite one application of the distinction; do not infer corrected understanding from the tutor explanation.\n",
  "D/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "E/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction.\nEvidence: None yet.\nGap: No learner attempt yet.\nNext: Predict what two containers share.\n",
  "E/LEARNER.md": "# Learner\n\n## Reported Docker background\nSupplied on 2026-10-16; not observed execution.\n- Containerized a FastAPI app last year.\n- Has not used volumes or Compose.\n\nTeaching implication: Use the familiar FastAPI context, but assess only the specific abilities needed for the next mission step. No global ability level assigned. Volumes and Compose are unassessed; they are not automatically prerequisites for the current local-app goal.\n",
  "E/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "F/CHECKPOINT.md": "# Checkpoint\nNext: Research the next SDK feature.\nEvidence: [sources](learning-records/0001-sources.md), [versions](learning-records/0002-versions.md).\n",
  "F/learning-records/0001-sources.md": "# Source choice\nStatus: current\nKind: demonstrated\nLearner independently chose official API docs and justified fit to the question.\n",
  "F/learning-records/0002-versions.md": "# Version check\nStatus: current\nKind: demonstrated\nLearner independently rejected a stale example, checked installed version and found matching primary docs, explaining why.\n",
  "F/MISSION.md": "# Mission\nLearn enough of a new SDK feature to assess using it in a small app.\n",
  "G/CHECKPOINT.md": "# Checkpoint\nNext: Research the next SDK feature.\nEvidence: [sources](learning-records/0001-sources.md), [versions](learning-records/0002-versions.md).\n",
  "G/learning-records/0001-sources.md": "# Source choice\nStatus: current\nKind: demonstrated\nLearner independently chose official API docs and justified fit to the question.\n",
  "G/learning-records/0002-versions.md": "# Version check\nStatus: current\nKind: demonstrated\nLearner independently rejected a stale example, checked installed version and found matching primary docs, explaining why.\n",
  "G/MISSION.md": "# Mission\nLearn enough of a new SDK feature to assess using it in a small app.\n",
  "H/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction.\nEvidence: None yet.\nGap: No learner attempt yet.\nNext: Predict what two containers share.\nDeferred note: Production deployment may be useful later if the learner needs to operate an API for real users. After the local-app milestone, revisit whether that outcome is wanted and choose a separate mission or confirm a scope change. This is a possible future topic, not a prerequisite or a change to today's mission. No reminder scheduled.\n",
  "H/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "I/CHECKPOINT.md": "# Current checkpoint\nMilestone: Image/container distinction.\nEvidence: None yet.\nGap: No learner attempt yet.\nNext: Predict what two containers share.\n",
  "I/LEARNER.md": "# Learner\nPreference: Text-first explanations.\nReported: Used Python for a class project.\nEvidence: [prediction](learning-records/0001-prediction.md).\n",
  "I/learning-records/0001-prediction.md": "# Container prediction\nKind: demonstrated\nStatus: current\nLearner predicted separate writable layers for two containers; one hint used.\n",
  "I/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "J/CHECKPOINT.md": "# Checkpoint\nRelevant background: Learner reports never having used Compose; no Compose performance has been demonstrated.\nNext: Start with the image/container distinction for the local API mission; introduce Compose only if the mission needs it.\n",
  "J/LEARNER.md": "# Learner\nPreference: Text-first.\nReported: I have never used Compose.\n",
  "J/learning-records/0001-background.md": "# Reported background\nStatus: current\nKind: reported\nLearner reports using Python and never having used Compose.\n",
  "J/MISSION.md": "# Mission\nWhy: Understand containers for a local API.\nSuccess: Explain image/container and run one local app.\nConstraints: Python, text explanations.\nOut of scope: Production deployment.\n",
  "K/kubernetes/CHECKPOINT.md": "# Checkpoint\nCurrent milestone: Explain how a small service is deployed in Kubernetes.\nInitial plan: Use the two-hour weekly budget for a short explanation, a small learner attempt, feedback and a recap; adjust to observed needs.\nNext learner action: Explain the distinct jobs of a Deployment and a Service in a simple two-replica example, with hints available.\nEvidence: No Kubernetes performance demonstrated yet. The tutor's initial explanation is not learner evidence.\nOpen: Understanding of the image, Pod, Deployment and Service relationship is unassessed.\nDeferred: Cluster installation, production operations, advanced networking, storage and autoscaling.\n",
  "K/kubernetes/LEARNER.md": "# Learner\nStated preferences: Text-first and hints-first.\nOrigin: Reused from the MCP workspace at the learner's explicit request.\nKubernetes background and demonstrated understanding: Unknown; no topic-specific evidence imported.\n",
  "K/kubernetes/MISSION.md": "# Mission\nLearn Kubernetes to explain how a small service is deployed.\nSuccess criterion: Explain the route from a container image through a Deployment and Pods to a Service, and the role of each.\nTime budget: Two hours per week, including explanations, attempts and feedback.\nScope now: A conceptual deployment walkthrough; no cluster setup required yet.\nDeferred: Production operations, advanced networking, storage and autoscaling.\n",
  "K/mcp/CHECKPOINT.md": "# Current checkpoint\nCompleted local tool.\nEvidence: [tool](learning-records/0002-tool.md).\nNext: Design a boundary-input test.\n",
  "K/mcp/LEARNER.md": "# Learner\nPreferences: Text-first and hints-first.\nReported: Python/API experience.\nDemonstrated: See local MCP tool record.\n",
  "K/mcp/learning-records/0002-tool.md": "# Local MCP tool\nDate: 2026-10-13\nStatus: current\nKind: demonstrated\nEvidence: Learner designed input contract, explained discovery and invocation, and explained a tool call that the tutor observed succeed.\nAssistance: One setup hint.\nImplication: Skip basic discovery. Next test boundary inputs.\n",
  "K/mcp/MISSION.md": "# Mission: MCP\nWhy: Understand integrations I build.\nSuccess: Build and explain a local tool.\nOut of scope: Remote deployment.\n"
}
````
