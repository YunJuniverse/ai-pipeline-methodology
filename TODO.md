# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-049
- **notes**: Completed 2026-06-29. **PR #38 머지 완료**(main `5fc822f`). Class A. 프론트엔드 디자인 토큰 시스템 — 지침 20 신설(4기둥: 시맨틱 토큰·프리미티브·색 가드레일·제약문서, 이름=역할, A/B/C 트리거) + 스켈레톤 `frontend-design-tokens`(base/guardrails 포함) + Pending Lesson P-002. 가드레일 3케이스 실검증. **다운스트림 전파 3/5**(ai-icons·icons·cafe24, `--no-verify` 순수 sync) — icons-invest(dirty)·gamblescan(작업중) 보류. 17 §4.2의 시각 품질 인스턴스화(19=구조).

### METH-048
- **notes**: Completed 2026-06-29. **PR #37 머지 완료**. Class C(백서 변경, ADR-003). 백서·온보딩에 코드 품질 가드레일 통합 — `방법론_백서_가이드.md` §5/§7 + `WHITEPAPER.md` §8-5 신규 운영 원칙(v0.3.0) + `HOW_TO_APPLY.md` §5. 10_foundation은 shared 아님 → 백서 미전파(지침 19만 전파됨).

### METH-047
- **notes**: Completed 2026-06-24. **PR #36 머지 완료**. Class A. 클린아키텍처·클린코드 지침 19 신설 (GambleScan REFACTOR-CLEAN 역주입) — 4-레이어 의존성 규칙·4 코드 가드레일(레이어경계·no-explicit-any·no-console·max-lines=400)·래칫·god파일 분할·day-1 체크리스트. 지침 17 §4.2 Guardrails-by-Construction의 코드 품질 인스턴스화. README/v4 + CLAUDE/AGENTS §7 포인터.

<!-- Archived: METH-001~044 (2026-05~06). 상세는 git log --grep="METH-" 및 PR #5~#36, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
