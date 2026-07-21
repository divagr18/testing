# Pull Guard end-to-end fixture

A deliberately small dependency-free repository used to exercise Pull Guard's
webhook ingestion, deterministic clustering, isolated runner, and evidence
paths. Each pull request is independent and should remain open for triage.

## Local verification

The fixture deliberately has no package-install step. Run its checks from the
repository root:

```bash
python -m unittest discover -s tests -v
```

Keep fixture changes small and focused so each pull request remains useful as a
distinct review item during a recorded Pull Guard walkthrough.
