# Architecture Snapshot Prompt

Use this when a dated architecture description is needed.

## Instructions

- Read the relevant code, tests, and ADRs for the target area.
- Prefer what the code actually does over what older documents say.
- Call out assumptions and unknowns instead of smoothing them over.
- Write the result to `docs/snapshots/architecture-YYYY-MM-DD.md`.
- Add a header that says the document is a snapshot and not a live source.

## Include

- system boundaries
- major modules and responsibilities
- data flow
- external integrations
- known constraints
- links to ADRs and PRs
