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

### METH-063 · 사업기획서 문서 디벨롭 (problem-first 척추 + 청중 변형)
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). 문서별 심화 1번 대상. 웹리서치(YC·Sequoia·SBA·Lean/BM Canvas·K-Startup PSST 1차 소스) → 우리 사업기획서 고찰 → 제안 P1~P4 전체 반영. **핵심 명제: 지식(craft §19)이 구조(스켈레톤·§8 목차)보다 앞서 있어, craft를 1급 섹션으로 승격.** P1 §8.1 problem-first 척추 재정렬 + 왜지금(§6.16)·트랙션(§6.17)·팀-as-thesis(§6.19)·Exec Summary 선두 신설 + TAM/SAM/SOM bottom-up 강제(§6.2). P2 청중 변형 PSST 정부지원사업(§8.4)·IR(§8.5). P3 품질 5대 크로스체크(§16)+비목표. P4 1페이지 캔버스 옵션(§18.4). 스켈레톤 `30_planning/10` 척추 정합 재작성. §9.11~9.13 작성기준 + §19.14 근거우위 + 환류 노트.

### METH-062 · API 계약 템플릿 + 개발명세 작성 지침
- **notes**: 2026-07-08. Class A. PR 대기(main 직접, 신규). 커밋 `169a3c2`가 선행 PR #51에 미포함돼 main 기준 새 브랜치로 cherry-pick 복구(작업 손실 0). 사용자 질문("개발기획서 필요?")에서 도출. **결론: 단일 개발기획서=반대(architecture+wbs+master_plan+adr 재번들=단일출처 위반).** 대신 진짜 공백 2개 채움: ① 신규 템플릿 `api-contract.md`(엔드포인트·요청/응답·에러·버전·인증 — 개발리드→개발자 FE/BE 병렬 조율축, functional-spec의 상위 시스템 레벨) → dev/fullstack/agency 세트+매트릭스 편입. ② 신규 지침 `20_guides/21_개발명세_작성_지침.md`(개발명세 6종 조합·원본경계·개발자용 "여기서 시작" 읽는 순서·게이트·재번들 금지 근거) → README §3.5. 방법론 기획-헤비/개발명세-라이트 보정. METH-061 09(핸드오프 재포맷)와 짝.

### METH-061 · planning-handoff 모드 + 재포맷 규칙 코드화
- **notes**: 2026-07-08. Class A. **PR #51 머지 완료.** 사용자 발의 — 방법론 기본 가정(1인+AI, 산출물=AI 입력)이 "기획 전담자 → 별도 사람 개발자" 분업에서 깨지는 경우. 신규 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md`(생성 계약→소통 계약, 5축 재포맷, 템플릿별 유지/재프레임/매체전환/추가) + `_CATALOG.md`에 7번째 모드 `planning-handoff`(§1 세트 + §3 매트릭스 컬럼 + † 재포맷 각주). 모드 열거 5곳 전파: CLAUDE·AGENTS §1, guide 00 §11.8, guide README §3.1, 백서가이드. **스코프 판단: planning-handoff 세트 = planning ∪ {user-flow, functional-spec, wireframe-spec}, architecture·data-model 제외(개발자 소유)** — 사용자 조정 가능.

### METH-060 · 다운스트림 sync 전파 (guide 05~08)
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). 신규 지침 4종 + guide 02 §8 + thinktank + HOW_TO_APPLY §6을 적용 프로젝트에 전파. **완료: icons(`5564bc11`)·gamblescan(`792ad1e`)** — clean·feature 브랜치라 main 전환→sync --apply→커밋(--no-verify)→복귀, 산출물 혼입 0. **홀드: ai-icons**(커스텀 05 회의록·21 산출물채널분리 충돌 → dedup·90+ 마이그레이션 별건), **cafe24·icons-invest**(dirty). Open Issue 등재.

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
