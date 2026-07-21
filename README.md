# Pull Guard demo fixture

A deliberately small dependency-free repository used to exercise Pull Guard's
webhook ingestion, deterministic clustering, isolated runner, and evidence
paths.

It now includes a deliberately modest, dependency-free task-board domain. The
open pull requests are designed as a safe, repeatable review queue: some are
complementary improvements, while a few overlap or supersede earlier approaches
so that grouping and decision flows can be shown in a demo.

Run the test suite with:

```bash
python -m unittest discover -s tests -v
```
