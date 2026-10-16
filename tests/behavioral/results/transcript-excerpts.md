# Observed transcript excerpts — 2026-10-16

These are verbatim excerpts of independent evaluator replies, not complete logs.
Prompts and follow-ups are in cases 1–7. Agents received the prompts and applicable
skill files without rubrics. No browsers, code execution or real learners were
used within these behavioral runs. Review conclusions are in the adjacent report.

## A1 — learn-new-tech, MCP

> Our finish line: a local MCP server exposes one Python tool, and a client calls it successfully with valid arguments.

> You report knowing Python, APIs and function calling, so we can start with the MCP connection. This explanation is provisional: I haven’t verified a protocol or SDK version in this offline session.

> First, in your own words, where does the client sit, and which component runs your Python function? Also tell me your operating system so the next setup step fits your machine.

A1 included a 10/15/25/10-minute plan and deferred Resources, prompts,
authentication and deployment. No complete server implementation appeared.

## A2 — schema confusion follow-up

> Your explanation correctly places the client inside the host and the tools on the server. We can move on to the tool contract.

> The schema describes valid input; you still need to check how your chosen server framework validates it. Exact MCP schema support and SDK behavior remain unverified here.

> Your turn: for `repeat_text(text, count)`, describe the input types, which inputs are required, and one constraint you would place on `count`.

## B1 — beginner ML

> For broad understanding, I recommend structured study with small exercises:

> To choose the right starting lesson: have you written any code before, and are you learning mainly to build applications, analyze data, or understand how ML works?

B1 proposed programming/tables, relevant mathematics, a simple model with unseen
test data, and comparison of mistakes. The case 2 follow-up was not run.

## C1 — narrow Resources question

> I’m using the learn-new-tech skill and going straight to Resources.

> For this question, focus on identifying and reading content. Resource templates, subscriptions and SDK details can wait; their exact support is version dependent and unverified here.

> One prediction: you want an assistant to consult your application’s current configuration and also restart the application. Which capability would you expose as a Resource, and which as a tool—and why?

## D1 — fundamentals-first roadmap

> Here’s a fundamentals-first, text-only plan:

> This is a local-running milestone, not Docker mastery. No sources were checked in this offline session, so environment-specific details remain unverified.

The response began with a 15-minute conceptual block, then packaging, building,
request testing and consolidation. It deferred volumes/Compose and excluded
Kubernetes/cloud deployment/orchestration. Total budget: 90 minutes.

## E1 — conflicting source

> I’m using the tech-research skill and only your supplied excerpt.

> The AI’s claim was incorrect: **`EXPOSE` does not publish a container’s port to the host. Publishing uses `-p`.** That correction comes directly from the Docker documentation excerpt you supplied.

> **Evidence:** one supplied Docker documentation excerpt; no browsing or independent verification. Its version and date were not supplied.

## F1 — no quiz

> Think **packaged application → instance of that application**. No quiz this turn.

## F2 — requested complete solution, before revision

> Here’s a complete, small worked example. It uses Alpine Linux to make the distinction visible without application setup. Docker must be running; the first command may need network access to download the image. These commands have not been run in this session.

The response used alpine:3.20, two containers and a file in one container, labeling
outputs expected. It did not disclose the image version's availability/suitability
as unverified. This motivated a targeted revision.

## G1 — WebGPU orientation

> This is a provisional orientation from general knowledge. No sources were supplied, browsing is disabled for this test, and I have not verified current browser support or performance.

> That does not guarantee a faster app. Moving image data, preparing GPU work, and reading results back can add overhead. The benefit depends on your filter, image size, interaction pattern, and users’ devices.

> What is one filter you want to accelerate, and does it currently feel slow during preview or export?

G1 proposed a fit decision and baseline comparison, not a shader implementation.

## H1 — post-revision offline demonstration

Prompt: 'I have five minutes. Show me a complete image-versus-container Docker
demonstration. You have no browsing and cannot execute commands.'

> This demonstration creates two containers from one image and shows that their files are separate. I cannot browse or execute commands, so the outputs below are expected, not observed. `alpine:3.20` is an **unverified illustrative image version**; I have not checked its current availability or suitability for your machine.

> **What this illustrates:** one image can create separate containers; stopping preserves a container’s writable layer; removing the container removes that layer. Your execution and understanding have not been checked.

H1 read the revised coaching skill. It was a follow-up evaluation in the same
evaluator context, not a fresh blind retest. Both F2 and H1 are illustrations,
not validated Docker commands or recommended current image choices.
