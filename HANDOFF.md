# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

## Current Focus

- Working on: repository structure normalization and path consistency cleanup
- Current mode: fullstack
- Next TODO: verify moved onboarding/archive paths and decide whether to ignore local tool folders in git
- Blockers: none

## Active Links

- Current PR:
- Current issue:
- Relevant ADRs:
- Relevant snapshots:

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | Whether `.claude/worktrees/` and `.codex/` should be gitignored | Next cleanup pass | Open |

## Open Issues

| ID | Issue | Severity | Next Step |
|----|-------|----------|-----------|
| - | Some legacy/archive docs may still mention pre-`30_dev` paths | Low | Sweep archive only if those docs become live references again |

## Recent Changes

- 2026-05-07: moved onboarding docs into `40_resources/onboarding/`
- 2026-05-07: moved evaluation notes into `90_archive/evaluation/`
- 2026-05-07: aligned live docs and prompts to `30_dev/adr/` and `30_dev/snapshots/`
