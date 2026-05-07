# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

## Current Focus

- Working on: L0~L4 v0 implementation complete; waiting for real repeated friction evidence
- Current mode: fullstack
- Next TODO: none in Ready; next candidate is a real active Catalog promotion when N>=2 evidence exists
- Blockers: none

## Active Links

- Current PR:
- Current issue:
- Relevant ADRs:
- Relevant snapshots: `30_dev/snapshots/implementation-plan-2026-05-07.md`, `30_dev/snapshots/transfer-drill-2026-05-08.md`

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | `.claude/worktrees/` and `.codex/` are local tool metadata and should be gitignored | 2026-05-07 | Closed |

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
- 2026-05-07: revised `00_foundation/WHITEPAPER.md` to v0.2.0 as an executable constitution
- 2026-05-07: added implementation roadmap snapshot for L0/L1 first execution path
- 2026-05-07: completed `METH-006` L0 portable boot context refresh (`.ai/context.json`, schema, checkpoint, adapters)
- 2026-05-07: completed `METH-007` L1 observation CLI flow (`methodology observe`, validation, sample log)
- 2026-05-07: completed `METH-002` by ignoring local tool metadata paths while keeping `.ai/` tracked
- 2026-05-08: completed `METH-008` through `METH-012` v0 flows for Catalog, Skeleton, Thinktank, Dashboard assets, and transfer drill
