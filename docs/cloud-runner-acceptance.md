# Cloud runner acceptance probe

This fixture-only documentation update creates a new immutable pull-request
version for Pull Guard's disposable Compute runner acceptance test. It does not
change the retry implementation or its test contract.

Probe revision 2 records keyless signed-artifact dispatch validation.

Probe revision 3 records the Compute provider diagnostic.

Probe revision 4 verifies the explicit Compute insert request.

Probe revision 5 verifies that scoped VM metadata retains the bootstrap script.

Probe revision 6 records a redacted bootstrap failure signal if the agent cannot start.
