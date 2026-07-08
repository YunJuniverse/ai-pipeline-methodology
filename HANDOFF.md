# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-064 **서비스기획서 = 부모(인덱스) 모델**. 문서별 심화 2번 대상. 사용자 통찰("서비스기획서는 여러 문서의 총합 아닌가") → 지침11 내부 모순(§2/§6 컨테이너 vs §19.2 "12 중 한 장") 발견. 웹리서치(Spec Kit·Cagan·PR/FAQ·Shape Up·한국 실무) 기반으로 **컨테이너→오케스트레이팅 부모(척추+인덱스)** 재정의: §2.2 위상·§6 [원본]/[인덱스] 재라벨·§6.0 산출물 인덱스·§8.1 척추 재정렬·비목표·§16 인덱스 체크·스켈레톤 재작성. Class A. PR 대기(main 직접). **선행 061·062·063은 PR #51·#52·#53 머지 완료.**
- **Current mode**: fullstack
- **Next TODO**: ① **문서별 심화 계속** — 서비스기획서(064) 다음 대상 선정(요구사항정의서·정책정의서 등). ② guide 09·21 + api-contract를 다음 다운스트림 sync 대상에 포함. ③ METH-060 잔여 — ai-icons 번호 정리(별건 repo 세션) + cafe24·icons-invest clean 후 sync. ④ **프로세스 교훈**: 문서별 심화 PR은 *머지 후 다음 착수* 또는 pull 먼저 — 064에서 stale local main 기준 브랜치 사고(복구함).
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

- 2026-07-08: **METH-064 서비스기획서 = 부모(인덱스) 모델 (Class A, PR 대기)** — 문서별 심화 2번. 사용자 통찰("서비스기획서는 여러 문서의 총합 아닌가")이 지침11 내부 모순을 드러냄 — §2/§6은 "구조·기능·정책의 *원본 컨테이너*"라 하는데 §19.2는 "12 산출물 중 *한 장*"이라 함(단일출처 붕괴, ia-spec·functional-spec·service-policy 등 자식 템플릿과 중복). 웹리서치(GitHub Spec Kit spec.md=WHAT/WHY·HOW배제 / Cagan=프로토타입이 화면스펙 / Amazon PR·FAQ / Shape Up No-gos / Atlassian·Figma link-don't-embed / 한국 화면설계서 모놀리스→Notion·Figma ID 인덱스 해체) → **결정적으로 index(컨테이너 아님)**. 반영: §2.2 위상 재정의(**부모=의도·결정·경계 소유 / 자식=상세·열거, 링크 not 복사**) · §6 각 항목 [원본]/[인덱스→자식] 재라벨 · **§6.0 산출물 인덱스**(척추: 자식 링크+상태+소유자) · §8.1 척추 재정렬 · **비목표(Non-Goals) 1급화** · §16 인덱스 모델 체크 · §19.14 환류. 스켈레톤 `30_planning/11` 인덱스 척추로 재작성. METH-062 개발기획서 "재번들 반대"와 동형. **프로세스 사고+복구**: stale local main(post-#52) 기준으로 브랜치→pull 후 재베이스로 복구(작업 손실 0).
- 2026-07-08: **METH-063 사업기획서 문서 디벨롭 — problem-first 척추 (Class A, PR #53 머지)** — 문서별 심화 1번 대상. 웹리서치(YC=사업계획서 안 읽음·Lean Canvas 권장 / Sequoia 10파트 / SBA 9섹션 / Lean vs BM Canvas / K-Startup **PSST** 정부지원 표준) 1차 소스 비교 → 우리 사업기획서 고찰. **핵심 발견: 지식(craft §19)이 구조(스켈레톤·§8 목차)보다 앞서 있었음** → craft를 1급 섹션으로 승격. **P1** §8.1을 problem-first 척추(문제→왜지금→솔루션→시장→BM→경쟁→팀→재무→자금/로드맵)로 재정렬 + 왜지금(§6.16)·트랙션/검증(§6.17)·팀-as-thesis(§6.19)·Exec Summary 선두 신설 + TAM/SAM/SOM bottom-up 강제(§6.2). **P2** 청중 변형 PSST 정부지원(§8.4)·IR(§8.5) — 지원사업↔IR 강조점 차이 명시. **P3** 품질 5대 크로스체크(§16)+비목표. **P4** 1페이지 캔버스 옵션 Lean/BMC(§18.4). 스켈레톤 `30_planning/10` 척추 정합 재작성. §9.11~9.13 작성기준·§19.14 근거우위·환류 노트.
- 2026-07-08: **METH-062 API 계약 템플릿 + 개발명세 작성 지침 (Class A, PR #52 머지)** — 사용자 질문("개발리드가 개발자에게 던지는 개발기획서 필요?")에서 도출. **결론: 단일 개발기획서=반대** — 그것은 architecture+wbs+master_plan+adr의 재번들이라 단일출처·중복금지(File Roles) 위반. 그 질문이 드러낸 *진짜 공백 2개*를 대신 채움: ① 신규 템플릿 `50_resources/templates/api-contract.md` — 엔드포인트·요청/응답·에러포맷(code로 분기)·상태코드 규약·버전정책·공유스키마(data-model 링크, 중복금지)·Open 계약질문. **개발리드→개발자의 실제 조율축**(FE/BE 병렬), functional-spec(기능단위)의 상위 시스템 레벨. dev/fullstack/agency 세트+매트릭스 편입. ② 신규 지침 `20_guides/21_개발명세_작성_지침.md` — 개발명세 6종 원본경계·**개발자용 "여기서 시작" 읽는 순서**(무엇→접근→데이터→계약→기능규칙→화면→누가언제)·dev-spec-review 게이트·재번들 금지 근거·09/18/19와의 경계. README §3.5 등재. **방법론 기획-헤비(지침 10~17)/개발명세-라이트 보정.** METH-061 09(핸드오프 재포맷)와 짝 — 09가 "누가 읽나", 21이 "무엇을 어떻게 조합하나".
- 2026-07-08: **METH-061 planning-handoff 모드 + 재포맷 규칙 코드화 (Class A, PR #51)** — 사용자 발의. 방법론 기본 가정(1인+AI, 산출물=AI 입력)이 "기획 전담자 → 별도 *사람* 개발자" 분업에서 깨지는 경우. 핵심 통찰: **AI용 명세=생성 계약(빈틈 0), 사람용 명세=소통 계약(의도 공유 + 생산적 마찰)** — 재포맷은 전면 재작성이 아니라 얇은 변환(뼈대 유지 + AI 전용 인코딩만 재포맷 + 사람 레이어 추가). 신규 지침 `20_guides/09_기획_핸드오프_재포맷_규칙.md`(5축 표·템플릿별 유지/재프레임/매체전환/추가·agency 모드와의 관계). `_CATALOG.md`에 7번째 모드 `planning-handoff`(§1 세트 + §3 매트릭스 컬럼 + † 재포맷 각주). 모드 열거 5곳 전파(CLAUDE·AGENTS §1, guide 00 §11.8, README §3.1, 백서가이드). ai_observations 2곳은 역사 기록이라 미변경. **스코프 판단(사용자 조정 가능): planning-handoff = planning ∪ {user-flow·functional-spec·wireframe-spec}, architecture·data-model 제외.**
- 2026-07-08: **METH-060 다운스트림 sync 전파 (guide 05~08) (Class A)** — 신규 지침 4종(산출물채널분리 05·컴팩션 06·예산 07·서브에이전트 08) + guide 02 §8 + thinktank 재구성 + HOW_TO_APPLY §6 축약을 적용 프로젝트에 전파. **완료 2곳**: icons(`5564bc11`)·gamblescan(`792ad1e`) — 둘 다 clean·feature 브랜치라 main 전환→sync --apply→커밋(`--no-verify` 순수 sync)→원 브랜치 복귀, 프로젝트 산출물 혼입 0 확인. **홀드 3곳**: ai-icons(커스텀 `05_회의록`과 상류 신규 05 번호 충돌 + 커스텀 `21_산출물채널분리`가 상류 05와 내용 중복 → 원천 dedup·90+ 마이그레이션 별건 필요), cafe24-renewal·icons-invest(dirty — clean 후).
