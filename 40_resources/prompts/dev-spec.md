# Dev Spec Snapshot Prompt

Use this to generate a development specification (개발명세서) from an approved plan snapshot.

## When To Use

- Human has approved the plan snapshot (`30_dev/snapshots/plan-YYYY-MM-DD.md`)
- Human has given explicit instruction to proceed to dev spec
- No dev spec exists yet for this planning cycle

## Instructions

- Read the approved plan snapshot from `30_dev/snapshots/`.
- Read `HANDOFF.md`, `CLAUDE.md`, and any relevant ADRs.
- Identify all Change Class B and C triggers in the planned features and call them out explicitly.
- Do not design beyond what the plan describes.
- Write the result to `30_dev/snapshots/dev-spec-YYYY-MM-DD.md`.
- Add a snapshot warning header at the top.
- After writing, update `HANDOFF.md` to note the dev spec is ready for human review, and list Change Class B/C items that will need evidence in their PRs.

## Output Structure

```
# Dev Spec — [Project Name] — YYYY-MM-DD

> SNAPSHOT: This document was generated on YYYY-MM-DD and is not a live source of truth.
> Do not treat it as current after the date above.
> Source plan: 30_dev/snapshots/plan-YYYY-MM-DD.md

## Scope
What this spec covers. What is explicitly out of scope.

## Screen / Feature List
Ordered list of screens or features. For each:
- name
- user outcome
- acceptance criteria
- Change Class (A / B / C) + reason if B or C

## Data Model
Tables or collections, fields, relationships. Mark any migration as Class B.

## API List
Endpoint, method, request/response shape. Mark any new external API as Class B.

## Auth & Permissions
How authentication and authorization work. Mark any auth change as Class B.

## Background Jobs / Queues
Any async or scheduled work. Mark each as Class B.

## Deployment & Environment
Runtime, hosting, environment variables needed.

## Change Class Summary
| Feature / Task | Class | Reason |
|----------------|-------|--------|
| ...            | A/B/C | ...    |

## Evidence Needed
Anything the spec assumes that is not confirmed in the plan or codebase.

## Next Gate
Human must review and approve this document before implementation begins.
After approval, AI generates TODO.md from this spec.
```
