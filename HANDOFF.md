# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

## Current Focus

- Working on: post-merge follow-up after repository structure normalization
- Current mode: fullstack
- Next TODO: decide git policy for local tool metadata and implement first L1 observation capture flow
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
| - | Some legacy/archive docs may still mention pre-`30_dev` or pre-`50_tools` paths | Low | Sweep only if those docs become live references again |

## Recent Changes

- 2026-05-07: merged repository structure normalization to `main` (`00_foundation`, `10_guides`, `20_planning`, `30_dev`, `40_resources`, `50_tools`, `90_archive`)
- 2026-05-07: reserved numeric slot `50` for tools and aligned implementation paths to `50_tools/` per Whitepaper Appendix C
- 2026-05-07: created `40_resources/catalog/`, `40_resources/skeletons/`, and `40_resources/ai_observations/` with schema `_README.md` files
- 2026-05-07: added `10_guides/03_AI_관찰_로그_작성_규칙.md` as the single-source rule for L1 observation logs
- 2026-05-07: moved onboarding docs into `40_resources/onboarding/` and evaluation notes into `90_archive/evaluation/`
