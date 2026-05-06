# Plan Snapshot Prompt

Use this to generate a planning document (기획서) from brief files in `briefs/`.

## When To Use

- Human has placed idea notes, PDFs, or rough planning docs in `briefs/`
- Project is starting and no formal plan exists yet
- Human requests a planning pass before dev spec or implementation

## Instructions

- Read all files in `briefs/` first.
- Read `HANDOFF.md` and `CLAUDE.md`.
- Do not infer market facts, user needs, or business viability without evidence from the briefs.
- If evidence is missing, add an `Evidence Needed` section instead of inventing.
- Write the result to `docs/snapshots/plan-YYYY-MM-DD.md`.
- Add a snapshot warning header at the top.
- After writing, update `HANDOFF.md` to note that the plan snapshot is ready for human review.

## Output Structure

```
# Plan — [Project Name] — YYYY-MM-DD

> SNAPSHOT: This document was generated on YYYY-MM-DD and is not a live source of truth.
> Do not treat it as current after the date above.

## Purpose
Why this product or service exists.

## Problem Statement
The specific problem being solved, sourced from briefs.

## Target Users
Who the product is for, with any evidence from briefs.

## Core Features
Prioritized list of features derived from briefs. Mark each as Must / Should / Could.

## Business Model
Revenue or sustainability hypothesis. Mark as assumption if unverified.

## Competitive Landscape
Known alternatives or analogues mentioned in briefs. Mark gaps as Evidence Needed.

## Constraints
Time, budget, team, or technical constraints from briefs.

## Assumptions
List of assumptions that must hold for this plan to be valid.

## Evidence Needed
List facts that were assumed or missing from briefs, and would change the plan if wrong.

## Next Gate
Human must review and approve this document before dev spec work begins.
```
