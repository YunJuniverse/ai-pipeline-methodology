# API Spec Snapshot Prompt

Use this when a dated API description is needed.

## Instructions

- Read route handlers, request/response validators, tests, and relevant ADRs.
- Prefer actual contracts and test evidence over assumptions.
- If behavior differs by environment or auth state, call that out.
- Write the result to `docs/snapshots/api-spec-YYYY-MM-DD.md`.
- Add a header that says the document is a snapshot and not a live source.

## Include

- endpoint list
- auth requirements
- request and response shape
- error behavior
- external contract dependencies
- links to tests and PRs
