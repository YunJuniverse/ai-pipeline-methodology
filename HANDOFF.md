# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-062 **API 계약 템플릿 + 개발명세 작성 지침**. "개발기획서 필요?" 질문에서 도출 — 단일 개발기획서=반대(재번들=단일출처 위반), 대신 진짜 공백 2개 채움: 신규 템플릿 `api-contract.md`(FE/BE 병렬 조율축) + 신규 지침 21(개발명세 6종 조합·개발자용 읽는 순서). Class A. PR 대기(main 직접).
- **Current mode**: fullstack
- **Next TODO**: ① METH-060 잔여 — **ai-icons 번호 정리**(별건, 그 repo 세션): 커스텀 21_산출물채널분리→상류 05로 dedup + 레거시 04·05 회의록을 guide 02 §8 예약범위(90+)로 마이그레이션 → 그 후 sync. ② cafe24·icons-invest clean 후 sync. ③ guide 09·21 + api-contract를 다음 다운스트림 sync 대상에 포함. ④ dev 계열 실사용 craft 축적 시 guide 21 §3 읽는 순서·§4 게이트 보강.
- **Blockers**: none

## Active Links

- Current PR: #35 (METH-046 sync 픽스)
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

- 2026-07-08: **METH-062 API 계약 템플릿 + 개발명세 작성 지침 (Class A, PR 대기)** — 사용자 질문("개발리드가 개발자에게 던지는 개발기획서 필요?")에서 도출. **결론: 단일 개발기획서=반대** — 그것은 architecture+wbs+master_plan+adr의 재번들이라 단일출처·중복금지(File Roles) 위반. 그 질문이 드러낸 *진짜 공백 2개*를 대신 채움: ① 신규 템플릿 `50_resources/templates/api-contract.md` — 엔드포인트·요청/응답·에러포맷(code로 분기)·상태코드 규약·버전정책·공유스키마(data-model 링크, 중복금지)·Open 계약질문. **개발리드→개발자의 실제 조율축**(FE/BE 병렬), functional-spec(기능단위)의 상위 시스템 레벨. dev/fullstack/agency 세트+매트릭스 편입. ② 신규 지침 `20_guides/21_개발명세_작성_지침.md` — 개발명세 6종 원본경계·**개발자용 "여기서 시작" 읽는 순서**(무엇→접근→데이터→계약→기능규칙→화면→누가언제)·dev-spec-review 게이트·재번들 금지 근거·09/18/19와의 경계. README §3.5 등재. **방법론 기획-헤비(지침 10~17)/개발명세-라이트 보정.** METH-061 09(핸드오프 재포맷)와 짝 — 09가 "누가 읽나", 21이 "무엇을 어떻게 조합하나".
- 2026-07-08: **METH-061 planning-handoff 모드 + 재포맷 규칙 코드화 (Class A, PR #51)** — 사용자 발의. 방법론 기본 가정(1인+AI, 산출물=AI 입력)이 "기획 전담자 → 별도 *사람* 개발자" 분업에서 깨지는 경우. 핵심 통찰: **AI용 명세=생성 계약(빈틈 0), 사람용 명세=소통 계약(의도 공유 + 생산적 마찰)** — 재포맷은 전면 재작성이 아니라 얇은 변환(뼈대 유지 + AI 전용 인코딩만 재포맷 + 사람 레이어 추가). 신규 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md`(5축 표·템플릿별 유지/재프레임/매체전환/추가·agency 모드와의 관계). `_CATALOG.md`에 7번째 모드 `planning-handoff`(§1 세트 + §3 매트릭스 컬럼 + † 재포맷 각주). 모드 열거 5곳 전파(CLAUDE·AGENTS §1, guide 00 §11.8, README §3.1, 백서가이드). ai_observations 2곳은 역사 기록이라 미변경. **스코프 판단(사용자 조정 가능): planning-handoff = planning ∪ {user-flow·functional-spec·wireframe-spec}, architecture·data-model 제외.**
- 2026-07-08: **METH-060 다운스트림 sync 전파 (guide 05~08) (Class A)** — 신규 지침 4종(산출물채널분리 05·컴팩션 06·예산 07·서브에이전트 08) + guide 02 §8 + thinktank 재구성 + HOW_TO_APPLY §6 축약을 적용 프로젝트에 전파. **완료 2곳**: icons(`5564bc11`)·gamblescan(`792ad1e`) — 둘 다 clean·feature 브랜치라 main 전환→sync --apply→커밋(`--no-verify` 순수 sync)→원 브랜치 복귀, 프로젝트 산출물 혼입 0 확인. **홀드 3곳**: ai-icons(커스텀 `05_회의록`과 상류 신규 05 번호 충돌 + 커스텀 `21_산출물채널분리`가 상류 05와 내용 중복 → 원천 dedup·90+ 마이그레이션 별건 필요), cafe24-renewal·icons-invest(dirty — clean 후).
- 2026-07-08: **METH-059 로드맵 잔여 마감 — RFC-002 R3·R4 구현 (Class A, PR #49 머지)** — Class A로 즉시 구현 가능한 로드맵 항목 마무리. R3 `20_guides/07_자율진행_예산_및_정지조건.md`(예산 선언·no-progress 2회 정지·반복 캡·침묵 절단 금지, "예산 내 자율 초과 시 보고") + R4 `20_guides/08_서브에이전트_오케스트레이션.md`(언제 쓰나·요약 반환/격리/적대적 검증 규약·스케일 매칭) 신설. CLAUDE/AGENTS에 예산 규칙 편입 + README 07·08. RFC-002: R3·R4 ✅구현, **R1(a)·R5·R6 ⏸보류(사유 명시: 임베딩 어댑터 인프라 / Class C 게이트)** + 로드맵 상태표. 잔여는 미완 작업 아닌 *선행조건 있는 미래 항목* — active 백로그 아님. 급조 금지(아스피레이셔널 함정 회피).
- 2026-07-08: **METH-058 온보딩 밴드 다이어트 — 무게 감사 MED P3 (Class A, PR #48 머지)** — `HOW_TO_APPLY §6` Change Class 전문(트리거·요구증거·프로세스 35줄)이 `CLAUDE §3`을 재서술하며 드리프트(B/C 무단강등 금지 누락 등)한 것을 **요지 3줄 + CLAUDE §3 단일출처 포인터**(8줄)로 축약. 앵커 참조 0 확인(안전). shared_paths라 하류 무게 동시 감소. USER_GUIDE §8·WHITEPAPER §8-2·AGENTS·DIAGRAM은 load-bearing이라 미변경(감사 판정 준수). **회고 3대 우선순위 P1(#47)·P2(#46)·P3(이번) 전부 실제 구현 완료.**
