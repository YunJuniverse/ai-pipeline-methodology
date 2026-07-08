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

### METH-061 · planning-handoff 모드 + 재포맷 규칙 코드화
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). 사용자 발의 — 방법론 기본 가정(1인+AI, 산출물=AI 입력)이 "기획 전담자 → 별도 사람 개발자" 분업에서 깨지는 경우. 신규 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md`(생성 계약→소통 계약, 5축 재포맷, 템플릿별 유지/재프레임/매체전환/추가) + `_CATALOG.md`에 7번째 모드 `planning-handoff`(§1 세트 + §3 매트릭스 컬럼 + † 재포맷 각주). 모드 열거 5곳 전파: CLAUDE·AGENTS §1, guide 00 §11.8, guide README §3.1, 백서가이드. **스코프 판단: planning-handoff 세트 = planning ∪ {user-flow, functional-spec, wireframe-spec}, architecture·data-model 제외(개발자 소유)** — 사용자 조정 가능.

### METH-060 · 다운스트림 sync 전파 (guide 05~08)
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). 신규 지침 4종 + guide 02 §8 + thinktank + HOW_TO_APPLY §6을 적용 프로젝트에 전파. **완료: icons(`5564bc11`)·gamblescan(`792ad1e`)** — clean·feature 브랜치라 main 전환→sync --apply→커밋(--no-verify)→복귀, 산출물 혼입 0. **홀드: ai-icons**(커스텀 05 회의록·21 산출물채널분리 충돌 → dedup·90+ 마이그레이션 별건), **cafe24·icons-invest**(dirty). Open Issue 등재.

### METH-059 · 로드맵 잔여 마감 (RFC-002 R3·R4 구현)
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). Class A로 즉시 구현 가능한 로드맵 항목 마무리. R3 `20_guides/07_자율진행_예산_및_정지조건.md` + R4 `20_guides/08_서브에이전트_오케스트레이션.md` 신설, CLAUDE/AGENTS 예산 규칙 + README 07·08. RFC-002: R3·R4 ✅, **R1(a)·R5·R6 ⏸보류(임베딩 어댑터 인프라 / Class C 게이트 대기)** + 로드맵 상태표. 잔여는 active 백로그 아닌 선행조건 있는 미래 항목 — 급조 금지. 남은 것: guide 05~08 다운스트림 sync.

### METH-058 · 온보딩 밴드 다이어트 (무게 감사 MED, P3)
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). 회고 P3. `HOW_TO_APPLY §6` Change Class 전문(35줄, CLAUDE §3 재서술·드리프트)을 요지 3줄 + **CLAUDE §3 단일출처 포인터**(8줄)로 축약. 앵커 참조 0(안전), shared_paths라 하류 무게 동시 감소. USER_GUIDE §8·WHITEPAPER §8-2·AGENTS·DIAGRAM은 load-bearing이라 미변경(감사 판정 준수). **회고 3대 우선순위(P1·P2·P3) 전부 실제 구현 완료.**

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
