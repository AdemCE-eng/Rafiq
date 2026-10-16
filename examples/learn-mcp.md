# MCP: one tool in 60 minutes

Authored illustration, not a captured test run. Use with learn-new-tech.

**Learner:** 'I know Python, APIs and function calling. I want to build one MCP
tool locally. I have 60 minutes.'

**Tutor:** 'Target: a local server exposing one small tool that a compatible test
client can discover and call. We will use your Python knowledge. First, can you
explain which side calls the tool and which side runs its implementation?'

The tutor stops for an answer. It does not write a complete server yet.

**Learner:** 'The client requests it and the server runs my function. I do not
understand what describes the function.'

**Tutor:** 'That description is the next gap: the tool has a name, description and
input schema so a client can understand the callable interface. For a
word_count(text) tool, what input type would you declare, and what should happen
for an empty string?'

After the learner attempts this, use the official
[server tutorial](https://modelcontextprotocol.io/docs/develop/build-server)
to choose current SDK setup and test instructions. Check the installed SDK version
before presenting code; do not assume remembered imports match it.

A possible budget, adjusted for environment readiness:

| Minutes | Work | Evidence |
| --- | --- | --- |
| 0–8 | Minimal roles and tool contract | Learner explains call flow and input |
| 8–18 | Check setup and current official example | Local environment is ready |
| 18–40 | Learner implements one tool | Callable function and server registration |
| 40–52 | Discover and invoke it with a test client | Normal and empty input results inspected |
| 52–60 | Explain a changed input case | Learner predicts behavior and records next gap |

NOW: minimal call flow, tool contract, one transport needed locally, SDK registration,
a test invocation. LATER: Resources and Prompts if needed. NOT NEEDED FOR THIS GOAL:
remote deployment, a full authentication architecture and production operations.

If setup consumes the session, shrink to a function plus an explained tool contract
and reschedule connection testing. Do not claim an unrun server works.
