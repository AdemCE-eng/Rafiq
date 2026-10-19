# Behavioral evaluation protocol

Session cases are in [cases.md](cases.md); persistent-state scenarios are in
[companion-cases.md](companion-cases.md). Use fictional state in isolated workspaces.

Experience-selection scenarios are in [experience-cases.md](experience-cases.md).

These are human-reviewed scenarios, not executable assertions or an official
Agent Skills evaluation format. The structural script does not run them.

Use a fresh conversation per case. Give the tester only the named skill folder,
the learner prompt and declared source/tool access; withhold the rubric until
grading. Install only that skill when testing independence. Follow up with the
specified learner turn after the tutor responds. Save exact prompts and replies.

Record date, client and model (unknown if not exposed), skill file hashes, tools,
source access, native vs manual loading, preferences supplied and all deviations.
Do not treat a synthetic learner response as evidence that a real learner learned.

Grade every applicable criterion PASS / FAIL / NOT OBSERVED with transcript
evidence. A critical failure (fabricated evidence, unsolicited full target
solution, ignored scope or forced learning style) fails that case. If a required
behavior has not been reached, mark the case incomplete rather than inferring a
pass. Score behavior, not exact headings or phrasing.

Run [cases](cases.md) both with and without the skill using equivalent conditions,
ideally three repetitions per client/model. Review blind where possible. Test
explicit activation first, then natural-language routing with only descriptions
available. A structural pass is not a routing pass.

Prioritize real multi-turn attempts and delayed transfer after first-turn tests:
does the learner solve a changed problem later without the solution visible?

For revisions, rerun affected cases; retain the original result and explain why
the change addresses the observed problem. Use [the result template](result-template.md).

Rafiq discovery boundaries: [routing regressions](rafiq-routing.md).
Archived results preserve the skill names and paths used during their original runs.

Beginner and state-growth scenarios: [cases](beginner-cases.md).
