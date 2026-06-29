# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

### METH-049
- **title**: 프론트엔드 디자인 토큰 시스템 — 지침 20 신설 + 스켈레톤 + P-002
- **notes**: 작업 완료(로컬), **커밋/PR 대기**. Class A. 사용자 지시(A/B/C 트리거 블록 → "Full system" 선택). ① 지침 20 `20_프론트엔드_디자인_토큰_시스템_규칙.md` 신설 — 4기둥(시맨틱 토큰·프리미티브·색 가드레일·제약문서)·이름=역할·A/B/C 운영 트리거. 17 §4.2를 *시각 품질*에 인스턴스화. ② 스켈레톤 `50_resources/skeletons/frontend-design-tokens/`(base: theme/tokens.css @theme, lib/cn.ts, components/primitives Card·Button·Badge, guardrails/check-no-arbitrary-color.sh + wiring.md, design-system.md / bakes-in.json / README). ③ Pending Lesson `P-002_frontend-design-tokens`(P-001은 git-write-lock이라 충돌 회피). ④ 가드레일 3케이스 실검증(clean pass / hex+gray fail / allowlist pass). 가이드 README 카탈로그·현황 행 추가. 다음: 브랜치 + ship.

### METH-048
- **title**: 백서·온보딩 가이드에 코드 품질 가드레일 통합 (지침 19 → 방법론 표준 서사)
- **notes**: 작업 완료, **PR 대기**(브랜치 `claude/meth-048-whitepaper-guide-codequality`, main 기준). 사용자 지시("백서·가이드라인을 클린코드·클린아키텍처 기반으로 업데이트"). 지침 19(METH-047)가 standalone이라, 백서·온보딩에 통합해 *방법론 표준 서사*로. ① `10_foundation/방법론_백서_가이드.md` §5에 "코드 품질 craft(Guardrails by Construction)" 추가 + §7 워크플로에 day-1 가드레일·lint 게이트. ② **`10_foundation/WHITEPAPER.md`(헌법) §8-5 "Guardrails-by-Construction" 신규 운영 원칙**(AI 안전+코드 품질 횡단) + 부록 A 지침 19 행 + 버전 v0.2.0→v0.3.0. ③ `10_foundation/HOW_TO_APPLY.md` §5 Fullstack에 day-1 가드레일·lint·typecheck·build·test 게이트. **Class C(백서 변경) — `40_dev/adr/ADR-003` 신설(사용자 지시=승인 증빙)**. 머지 후 다운스트림 sync(10_foundation은 shared 아님 → 백서는 미전파, 지침 19만 이미 전파).

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-047
- **notes**: Completed 2026-06-24. **PR #36 머지 완료**. Class A. 클린아키텍처·클린코드 지침 19 신설 (GambleScan REFACTOR-CLEAN 역주입) — 4-레이어 의존성 규칙·4 코드 가드레일(레이어경계·no-explicit-any·no-console·max-lines=400)·래칫·god파일 분할·day-1 체크리스트. 지침 17 §4.2 Guardrails-by-Construction의 코드 품질 인스턴스화. README/v4 + CLAUDE/AGENTS §7 포인터.

### METH-046
- **notes**: Completed 2026-06-24. **PR #35 머지 완료**(main `626b48a`). Class A. sync mirror-delete 버그 픽스 — `copy_path` prune_report 추가 + `cmd_sync` prune을 `--prune` opt-in으로(기본 보존+경고). 다운스트림 고유 파일(ai-icons guide 04)이 조용히 삭제되던 데이터손실 차단.

### METH-045
- **notes**: Completed 2026-06-24. **PR #34 머지 완료**(main `7ed86f1`). Class A. 방법론 백서 겸 가이드 — 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + Notion In-spire 하위 페이지 업로드.

<!-- Archived: METH-001~044 (2026-05~06). 상세는 git log --grep="METH-" 및 PR #5~#36, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
