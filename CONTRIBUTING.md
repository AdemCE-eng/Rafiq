# Contributing

Contribute a behavior change with a motivating learner scenario. Explain what the
agent did before, what it should do instead, and how you observed the difference.

1. Edit the smallest relevant instruction or reference. Keep skill folders
   independently installable.
2. Keep portable frontmatter. Document client-specific packaging separately.
3. Add or update a behavioral scenario with observable pass/fail criteria.
4. Run python tests/validate_repo.py and the relevant fresh-chat scenarios.
5. Include the actual transcript, client/model, tool access, date, prompt,
   skill snapshot/hash, and outcome. Redact personal information.
6. Compare against a no-skill baseline when making improvement claims.

Do not count keyword matches, a self-assessment, or a nice-looking roadmap as
proof of learning. Include negative routing cases and multi-turn attempts.
Never label an authored example an executed evaluation.

For research changes, cite applicable primary documentation with version/date
context. Prefer narrow fixes over accumulating universal rules. Add scripts only
for repeatable reliability problems and keep runtime dependencies out of
instruction-only skills.

Use the existing MIT license for original contributions. External material retains
its own license; summarize design lessons instead of copying prose.
