# Pull Guard end-to-end fixture

A deliberately small dependency-free repository used to exercise Pull Guard's
webhook ingestion, deterministic clustering, isolated runner, and evidence
paths. Each pull request is independent and should remain open for triage.

## Retry behaviour

The fixture starts with a single `retry_once` helper. Test pull requests may
propose retry behaviour, diagnostics, or small supporting utilities. Review
each proposal for the behaviour it actually retains rather than its title.
