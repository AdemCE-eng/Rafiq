# Docker: containerize an API tonight

Authored illustration. Use learning-roadmap for the plan, learning-coach for
teaching, or learn-new-tech for both. Each works independently.

**Learner:** 'I know Python and FastAPI. I have 90 minutes tonight to containerize
my stateless API locally. Docker is installed. I prefer fundamentals first.'

**Tutor:** 'Finish line: your existing endpoint responds through a locally
published container port. Start with the image/container model, then apply it.
We do not need to reteach Python or FastAPI.'

| Scope | Topics | Why |
| --- | --- | --- |
| NOW | Image vs container; Dockerfile; build/run; app listening address and port publishing | Required for an endpoint reachable from the host |
| LATER / NOT NEEDED YET | Volumes, Compose, registries | Revisit for persisted data, multiple services or distribution |
| NOT NEEDED FOR THIS GOAL | Swarm, orchestration, advanced networking | Not required for one stateless local API |

Suggested budget: 10 minutes mental model; 20 Dockerfile and dependencies;
25 build/run; 25 request testing and debugging; 10 explanation and checkpoint.
If the API uses persistent files or a database, revisit the assumptions and
move the relevant storage/network prerequisite into NOW.

**Tutor:** 'An image is the packaged template used to create a container. Before
we write the Dockerfile, which pieces of your API need to exist inside that
environment? List them from your current project.'

Wait for the attempt. A missing dependency earns a targeted hint, not an entire
ready-to-paste solution. Respect a later request for a full demonstration.

A common misconception to correct: EXPOSE does not publish a port to the host;
publishing is configured when running the container. Verify the actual command
against [Docker's port publishing documentation](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/).
For a local-only exercise, use a loopback-bound host mapping rather than silently
exposing the service to other machines. Check application binding separately.
