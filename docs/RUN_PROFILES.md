# Run Profiles

TwinBench documents three practical run profiles.

## 1. Local Reference

Best for a locally running runtime with direct access to internal auth and diagnostics.

Use when:

- you are developing the runtime locally
- you can read the runtime token or config directly
- you want the fastest path to a trusted artifact

Example:

```bash
python3.10 -m harness.runner \
  --url http://127.0.0.1:3000 \
  --token-from-nullalis-config \
  --user-id 1 \
  --name "Local Reference Runtime"
```

## 2. SaaS Runtime

Best for a remotely hosted runtime that still exposes the benchmark contract.

Use when:

- the runtime is deployed as a service
- internal auth is available to the operator
- health and diagnostics are reachable over the benchmark surface

Example:

```bash
python3.10 -m harness.runner \
  --url https://runtime.example.com \
  --token YOUR_TOKEN \
  --user-id 1 \
  --name "Hosted Runtime"
```

## 3. Multi-Tenant-Ready

Best for runtimes that support fair benchmark fanout across provisioned users.

Use when:

- the runtime can provision benchmark users
- tenant identity is real, not simulated
- you want multi-user scale claims to be treated as measured evidence

Requirements:

- user provisioning works for benchmark users
- tenant routing is stable
- multi-user fanout is not blocked by missing identity bootstrap

## Timeout Guidance

- `--timeout 0`: open-ended race style; faster is better, but a blocked turn can hang forever
- bounded timeout: safer for CI and public comparison
- adaptive timeout: useful for mixed-latency runtimes

## Recommended Public Artifact

For public comparison, prefer:

- one full run
- attached diagnostics and metrics
- one short incident note
- one run profile label in the submission
