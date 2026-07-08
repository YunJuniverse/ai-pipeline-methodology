# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-063 **사업기획서 문서 디벨롭**. 문서별 심화 1번 대상 — 웹리서치(YC·Sequoia·SBA·Lean/BM Canvas·PSST) 기반으로 지침10+스켈레톤을 problem-first 척추로 재정렬 + 왜지금·트랙션·팀·Exec Summary 승격 + PSST/IR 청중 변형 + 5대 크로스체크 + 캔버스 옵션(P1~P4 전체). Class A. PR 대기(main 직접). **선행 061·062는 PR #51·#52로 머지 완료.**
- **Current mode**: fullstack
- **Next TODO**: ① **문서별 심화 계속** — 사업기획서(063) 다음 대상 선정(서비스기획서·요구사항정의서 등). ② guide 09·21 + api-contract를 다음 다운스트림 sync 대상에 포함. ③ METH-060 잔여 — ai-icons 번호 정리(별건 repo 세션) + cafe24·icons-invest clean 후 sync. ④ 사업기획서 실사용 시 problem-first 척추·PSST 변형 craft 축적 → §19 보강.
- **Blockers**: none

## Active Links

- Current PR: METH-062 (신규, api-contract + guide 21) · METH-061 #51 머지 완료
- Current issue:
- Relevant ADRs:
- Relevant snapshots: `40_dev/snapshots/implementation-plan-2026-05-07.md`, `40_dev/snapshots/transfer-drill-2026-05-08.md`

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | `.claude/worktrees/` and `.codex/` are local tool metadata and should be gitignored | 2026-05-07 | Closed |

## Open Issues

| ID | Issue | Severity | Next Step |
|----|-------|----------|-----------|
| - | ~~sync가 다운스트림 고유 파일 mirror-delete~~ | — | **Closed** — METH-046(PR #35)로 prune을 --prune opt-in화(기본 보존) |
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |
| - | ai-icons 레거시 커스텀 guide 번호 충돌 (04 문서보관·05 회의록·21 산출물채널분리) — 상류 05와 번호/내용 충돌로 sync 홀드 | Med | ai-icons 세션: 21→상류 05 dedup + 04·05를 guide 02 §8 예약범위(90+) 마이그레이션 → sync 재개. cafe24·icons-invest는 dirty 정리 후 sync |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-08: **METH-063 사업기획서 문서 디벨롭 — problem-first 척추 (Class A, PR 대기)** — 문서별 심화 1번 대상. 웹리서치(YC=사업계획서 안 읽음·Lean Canvas 권장 / Sequoia 10파트 / SBA 9섹션 / Lean vs BM Canvas / K-Startup **PSST** 정부지원 표준) 1차 소스 비교 → 우리 사업기획서 고찰. **핵심 발견: 지식(craft §19)이 구조(스켈레톤·§8 목차)보다 앞서 있었음** → craft를 1급 섹션으로 승격. **P1** §8.1을 problem-first 척추(문제→왜지금→솔루션→시장→BM→경쟁→팀→재무→자금/로드맵)로 재정렬 + 왜지금(§6.16)·트랙션/검증(§6.17)·팀-as-thesis(§6.19)·Exec Summary 선두 신설 + TAM/SAM/SOM bottom-up 강제(§6.2). **P2** 청중 변형 PSST 정부지원(§8.4)·IR(§8.5) — 지원사업↔IR 강조점 차이 명시. **P3** 품질 5대 크로스체크(§16)+비목표. **P4** 1페이지 캔버스 옵션 Lean/BMC(§18.4). 스켈레톤 `30_planning/10` 척추 정합 재작성. §9.11~9.13 작성기준·§19.14 근거우위·환류 노트.
- 2026-07-08: **METH-062 API 계약 템플릿 + 개발명세 작성 지침 (Class A, PR #52 머지)** — 사용자 질문("개발리드가 개발자에게 던지는 개발기획서 필요?")에서 도출. **결론: 단일 개발기획서=반대** — 그것은 architecture+wbs+master_plan+adr의 재번들이라 단일출처·중복금지(File Roles) 위반. 그 질문이 드러낸 *진짜 공백 2개*를 대신 채움: ① 신규 템플릿 `50_resources/templates/api-contract.md` — 엔드포인트·요청/응답·에러포맷(code로 분기)·상태코드 규약·버전정책·공유스키마(data-model 링크, 중복금지)·Open 계약질문. **개발리드→개발자의 실제 조율축**(FE/BE 병렬), functional-spec(기능단위)의 상위 시스템 레벨. dev/fullstack/agency 세트+매트릭스 편입. ② 신규 지침 `20_guides/21_개발명세_작성_지침.md` — 개발명세 6종 원본경계·**개발자용 "여기서 시작" 읽는 순서**(무엇→접근→데이터→계약→기능규칙→화면→누가언제)·dev-spec-review 게이트·재번들 금지 근거·09/18/19와의 경계. README §3.5 등재. **방법론 기획-헤비(지침 10~17)/개발명세-라이트 보정.** METH-061 09(핸드오프 재포맷)와 짝 — 09가 "누가 읽나", 21이 "무엇을 어떻게 조합하나".
- 2026-07-08: **METH-061 planning-handoff 모드 + 재포맷 규칙 코드화 (Class A, PR #51)** — 사용자 발의. 방법론 기본 가정(1인+AI, 산출물=AI 입력)이 "기획 전담자 → 별도 *사람* 개발자" 분업에서 깨지는 경우. 핵심 통찰: **AI용 명세=생성 계약(빈틈 0), 사람용 명세=소통 계약(의도 공유 + 생산적 마찰)** — 재포맷은 전면 재작성이 아니라 얇은 변환(뼈대 유지 + AI 전용 인코딩만 재포맷 + 사람 레이어 추가). 신규 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md`(5축 표·템플릿별 유지/재프레임/매체전환/추가·agency 모드와의 관계). `_CATALOG.md`에 7번째 모드 `planning-handoff`(§1 세트 + §3 매트릭스 컬럼 + † 재포맷 각주). 모드 열거 5곳 전파(CLAUDE·AGENTS §1, guide 00 §11.8, README §3.1, 백서가이드). ai_observations 2곳은 역사 기록이라 미변경. **스코프 판단(사용자 조정 가능): planning-handoff = planning ∪ {user-flow·functional-spec·wireframe-spec}, architecture·data-model 제외.**
- 2026-07-08: **METH-060 다운스트림 sync 전파 (guide 05~08) (Class A)** — 신규 지침 4종(산출물채널분리 05·컴팩션 06·예산 07·서브에이전트 08) + guide 02 §8 + thinktank 재구성 + HOW_TO_APPLY §6 축약을 적용 프로젝트에 전파. **완료 2곳**: icons(`5564bc11`)·gamblescan(`792ad1e`) — 둘 다 clean·feature 브랜치라 main 전환→sync --apply→커밋(`--no-verify` 순수 sync)→원 브랜치 복귀, 프로젝트 산출물 혼입 0 확인. **홀드 3곳**: ai-icons(커스텀 `05_회의록`과 상류 신규 05 번호 충돌 + 커스텀 `21_산출물채널분리`가 상류 05와 내용 중복 → 원천 dedup·90+ 마이그레이션 별건 필요), cafe24-renewal·icons-invest(dirty — clean 후).
- 2026-07-08: **METH-059 로드맵 잔여 마감 — RFC-002 R3·R4 구현 (Class A, PR #49 머지)** — Class A로 즉시 구현 가능한 로드맵 항목 마무리. R3 `20_guides/07_자율진행_예산_및_정지조건.md`(예산 선언·no-progress 2회 정지·반복 캡·침묵 절단 금지, "예산 내 자율 초과 시 보고") + R4 `20_guides/08_서브에이전트_오케스트레이션.md`(언제 쓰나·요약 반환/격리/적대적 검증 규약·스케일 매칭) 신설. CLAUDE/AGENTS에 예산 규칙 편입 + README 07·08. RFC-002: R3·R4 ✅구현, **R1(a)·R5·R6 ⏸보류(사유 명시: 임베딩 어댑터 인프라 / Class C 게이트)** + 로드맵 상태표. 잔여는 미완 작업 아닌 *선행조건 있는 미래 항목* — active 백로그 아님. 급조 금지(아스피레이셔널 함정 회피).
