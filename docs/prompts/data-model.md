# Data Model Snapshot Prompt

Use this when a dated schema or domain model document is needed.

## Instructions

- Read actual schema files, migrations, ORM models, tests, and relevant ADRs.
- Do not rely on stale planning docs.
- If the schema is inconsistent across code paths, state that explicitly.
- Write the result to `docs/snapshots/data-model-YYYY-MM-DD.md`.
- Add a header that says the document is a snapshot and not a live source.

## Include

- current entities and key fields
- relationships
- migrations or recent schema changes
- auth or permissions implications
- data risks and follow-up questions
