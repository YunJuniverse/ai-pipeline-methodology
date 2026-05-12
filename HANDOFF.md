# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

## Current Focus

- **Working on**: 세션·작업 종료 자동화(`methodology wrap`) + GitHub Actions CI 워크플로 도입 완료. CLAUDE.md/AGENTS.md에 (α) 패턴 규칙 명문화.
- **Current mode**: fullstack
- **Next TODO**: 적용 프로젝트 3개에 *다음 sync 시* applied-ci 워크플로 자동 주입 검증 (METH-015), 회고(2026-Q2) 후보 트리거 (관찰 누적 임계치 모니터링)
- **Blockers**: none

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

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `30_dev/snapshots/` 참조.

- 2026-05-12: **세션 종료 자동화 + GitHub Actions CI** — `methodology wrap` CLI 신설(4개 라이브 파일 갱신 검증), CLAUDE/AGENTS에 (α) 패턴 규칙 명문화, `.github/workflows/methodology-{source,applied}-ci.yml` 워크플로 2종, MANIFEST에 applied-ci 추가(source-ci 격리 실측 ✅), `.ai/adapters/claude.md`에 SessionEnd hook 가이드.
- 2026-05-12: MP-001/MP-002 메타 카탈로그 pending 시드 + RFC-001 (accepted) + `cmd_status` upstream commit 격차 검출 구현. 3개 적용 프로젝트 모두 "behind upstream" 정확 표시 검증. icons/gamblescan/talmocom `.ai/context.json` domain → webapp-next 설정·푸시.
- 2026-05-12: v3.1 → v3.2 마이그레이션 작성 + 3개 외부 프로젝트(icons/gamblescan/talmocom) 적용 완료 — `migrations/v3.1_to_v3.2.py` (이동·디렉터리·`_materialize_l0` 임베디드 템플릿) + MANIFEST 확장 + 60_meta 격리 실측 ✅. 본 작업의 메타 관찰 5건(F-001~005)을 `60_meta/observations/2026-05-12_*.md`에 기록.
- 2026-05-12: `60_meta/` 메타-방법론 격리 인프라 신설 — `_README` + rfc/retrospectives/experiments/observations/catalog + `methodology.py` MANIFEST `excluded_paths` 안전망 + `manifest-check` CLI + 백서 §13/§부록 C·A 갱신. `init` 격리 동작 검증 완료.
- 2026-05-08: `METH-008`~`METH-012` v0 — Catalog/Skeleton/Thinktank/Dashboard CLI + transfer drill #2 (Pass for v0)
- 2026-05-07: `WHITEPAPER` v0.2.0 — executable constitution으로 개정 + ADR-001 신설
- 2026-05-07: `METH-007` L1 observation CLI flow (`methodology observe` + validation)
- 2026-05-07: `METH-006` L0 portable boot context (`.ai/context.json`, schema, checkpoint, adapters)
