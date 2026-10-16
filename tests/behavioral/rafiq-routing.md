# Rafiq discovery regressions

Use only the five skill names/descriptions in a fresh native client, then inspect
which skill is actually loaded. Do not count this expected-selection table as a run.

| Request | Expected selection / boundary |
| --- | --- |
| I want Rafiq to help me learn MCP and keep editable progress here. | rafiq |
| Continue my learning mission using ./learning-workspaces/mcp. | rafiq |
| Help me learn calculus over this term, adapt practice from evidence, and gradually let me plan. | rafiq |
| I want an ongoing visual learning journey for networking, with saved progress. | rafiq; visuals remain conditional on the objective |
| Write a production Dockerfile for this app, no tutoring. | No learning skill |
| What does HTTP stand for? | No learning skill |
| Summarize this article. | No learning skill unless learning intent is supplied |
| Teach me image versus container in one short session; no saved state. | learning-coach or learn-new-tech; no persistence |
| Make a learning roadmap for my exam. | learning-roadmap |
| Research whether WebGPU could help my project; I need orientation. | tech-research |
| Coach me through debugging; hints before the solution. | learning-coach |

Then explicitly invoke $rafiq and run the applicable [state cases](companion-cases.md)
and [experience cases](experience-cases.md). Preserve their rubrics unchanged.
Test native selection separately from explicitly loading the skill.
