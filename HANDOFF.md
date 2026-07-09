# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-066 **요구사항정의서 심화(ISO/IEC/IEEE 29148)**. 문서별 심화 4번 — `requirements-spec` 대장을 웹리서치(29148·BABOK·RTM·검증방법·우선순위)로 강화. 추가: 유형(BABOK 계층)·인수기준·검증방법(I/A/D/T)·상태 생명주기·하위추적·변경등급·shall 규약·품질특성·RTM 양방향. functional-spec(EARS)의 상류=shall 대장. Class A. PR 대기(main 직접). **선행 061~065 PR #51~#55 머지 완료.**
- **Current mode**: fullstack
- **Next TODO**: ① **문서별 심화 계속** — 남은 대상 선정. 기획 계열 남은 것: prd·kpi-tree·context-glossary. 또는 다른 기획서(운영 12·마케팅 13·브랜드 14 지침)·PM 15·AI기능 16. ② 심화 산출물 실사용 시 craft 환류. ③ 갱신 템플릿들을 다음 다운스트림 sync 대상에 포함. ④ METH-060 잔여(ai-icons 번호 정리 등). **프로세스 교훈 준수**: 착수 전 `git pull`/직전 PR 머지 확인.
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

- 2026-07-09: **METH-066 요구사항정의서 심화 — ISO/IEC/IEEE 29148 (Class A, PR 대기)** — 문서별 심화 4번. 웹리서치(29148 SRS·BABOK 요구 계층·RTM·검증방법·우선순위 프레임) → `requirements-spec` 대장 강화. `functional-spec`(EARS)의 *상류 = shall 대장*. 추가: **범위·전제** 섹션 · 대장에 **유형(BABOK 계층: business/stakeholder/functional/NFR/transition/constraint)·인수기준·검증(I/A/D/T)·상태 생명주기(제안→검토→승인→구현→검증 / 보류·반려)·하위추적(FS-ID/US/TC)·변경등급(A/B/C)** 컬럼 · **작성 규율**(shall 규약·atomic·금지 모호어·개별 9특성+SET 5특성) · **우선순위 프레임**(MoSCoW+Pn / WSJF·RICE·Kano) · **RTM 양방향**(후방 출처↔전방 테스트, *링크 복사금지*). _CATALOG 한줄 갱신. 경량 최소 컬럼 명시(과설계 방지). 공통 원칙 재확인: 대장=SSOT, 하류는 요구ID 링크.
- 2026-07-08: **METH-065 서비스기획서 자식 산출물 8종 최신화 (Class A, PR #55 머지)** — 문서별 심화 3번. 064가 정한 자식 8종을 **4개 병렬 웹리서치 에이전트**(1차 소스)로 2025-26 최신화. **user-story**: Job Story 폼·**Gherkin(Given/When/Then) AC 블록**(AI 스펙+검증 오라클)·INVEST 체크·DoR/DoD·SPIDR 분할. **functional-spec**: **EARS 표기**(5패턴, NASA·Airbus 표준)·상태전이 표·측정가능 NFR·추적표(요구↔AC↔테스트↔코드). **service-policy**: **의사결정 표**(조건→액션·hit policy·Default 행)·effective-dating(과거 이력 보존)·변경이력·AI 가드레일 정책. **ia-spec**: Screen-ID 명명 규약·메뉴트리(global/local/utility)·RBAC(CRUD·default-deny·SoD)·IA 검증(카드소트/트리테스트 75%+). **user-flow**: **Mermaid** flowchart/sequence·3열 경로표·엣지케이스 체크리스트·actor 태그. **wireframe**: **5-state**(Empty/Loading/Partial/Error/Success — AI가 92% 누락)·번호 콜아웃·접근성/반응형·Figma 링크. **api-contract**: **RFC 9457 Problem Details**·RFC 9745/8594 deprecation·cursor 페이지네이션·OpenAPI 3.1. **microcopy**: 콘텐츠 원칙·Voice(상수)/Tone(맥락) 표·에러 패턴·용어사전·i18n·AI 프롬프트 스캐폴드. `_CATALOG` 한줄 8개 갱신. **공통 수렴: 사람 표 + 기계판독/추적 미러 + AI가 빠뜨리는 "불행 경로"(에러·상태) 강제.**
- 2026-07-08: **METH-064 서비스기획서 = 부모(인덱스) 모델 (Class A, PR #54 머지)** — 문서별 심화 2번. 사용자 통찰("서비스기획서는 여러 문서의 총합 아닌가")이 지침11 내부 모순을 드러냄 — §2/§6은 "구조·기능·정책의 *원본 컨테이너*"라 하는데 §19.2는 "12 산출물 중 *한 장*"이라 함(단일출처 붕괴, ia-spec·functional-spec·service-policy 등 자식 템플릿과 중복). 웹리서치(GitHub Spec Kit spec.md=WHAT/WHY·HOW배제 / Cagan=프로토타입이 화면스펙 / Amazon PR·FAQ / Shape Up No-gos / Atlassian·Figma link-don't-embed / 한국 화면설계서 모놀리스→Notion·Figma ID 인덱스 해체) → **결정적으로 index(컨테이너 아님)**. 반영: §2.2 위상 재정의(**부모=의도·결정·경계 소유 / 자식=상세·열거, 링크 not 복사**) · §6 각 항목 [원본]/[인덱스→자식] 재라벨 · **§6.0 산출물 인덱스**(척추: 자식 링크+상태+소유자) · §8.1 척추 재정렬 · **비목표(Non-Goals) 1급화** · §16 인덱스 모델 체크 · §19.14 환류. 스켈레톤 `30_planning/11` 인덱스 척추로 재작성. METH-062 개발기획서 "재번들 반대"와 동형. **프로세스 사고+복구**: stale local main(post-#52) 기준으로 브랜치→pull 후 재베이스로 복구(작업 손실 0).
- 2026-07-08: **METH-063 사업기획서 문서 디벨롭 — problem-first 척추 (Class A, PR #53 머지)** — 문서별 심화 1번 대상. 웹리서치(YC=사업계획서 안 읽음·Lean Canvas 권장 / Sequoia 10파트 / SBA 9섹션 / Lean vs BM Canvas / K-Startup **PSST** 정부지원 표준) 1차 소스 비교 → 우리 사업기획서 고찰. **핵심 발견: 지식(craft §19)이 구조(스켈레톤·§8 목차)보다 앞서 있었음** → craft를 1급 섹션으로 승격. **P1** §8.1을 problem-first 척추(문제→왜지금→솔루션→시장→BM→경쟁→팀→재무→자금/로드맵)로 재정렬 + 왜지금(§6.16)·트랙션/검증(§6.17)·팀-as-thesis(§6.19)·Exec Summary 선두 신설 + TAM/SAM/SOM bottom-up 강제(§6.2). **P2** 청중 변형 PSST 정부지원(§8.4)·IR(§8.5) — 지원사업↔IR 강조점 차이 명시. **P3** 품질 5대 크로스체크(§16)+비목표. **P4** 1페이지 캔버스 옵션 Lean/BMC(§18.4). 스켈레톤 `30_planning/10` 척추 정합 재작성. §9.11~9.13 작성기준·§19.14 근거우위·환류 노트.
- 2026-07-08: **METH-062 API 계약 템플릿 + 개발명세 작성 지침 (Class A, PR #52 머지)** — 사용자 질문("개발리드가 개발자에게 던지는 개발기획서 필요?")에서 도출. **결론: 단일 개발기획서=반대** — 그것은 architecture+wbs+master_plan+adr의 재번들이라 단일출처·중복금지(File Roles) 위반. 그 질문이 드러낸 *진짜 공백 2개*를 대신 채움: ① 신규 템플릿 `50_resources/templates/api-contract.md` — 엔드포인트·요청/응답·에러포맷(code로 분기)·상태코드 규약·버전정책·공유스키마(data-model 링크, 중복금지)·Open 계약질문. **개발리드→개발자의 실제 조율축**(FE/BE 병렬), functional-spec(기능단위)의 상위 시스템 레벨. dev/fullstack/agency 세트+매트릭스 편입. ② 신규 지침 `20_guides/21_개발명세_작성_지침.md` — 개발명세 6종 원본경계·**개발자용 "여기서 시작" 읽는 순서**(무엇→접근→데이터→계약→기능규칙→화면→누가언제)·dev-spec-review 게이트·재번들 금지 근거·09/18/19와의 경계. README §3.5 등재. **방법론 기획-헤비(지침 10~17)/개발명세-라이트 보정.** METH-061 09(핸드오프 재포맷)와 짝 — 09가 "누가 읽나", 21이 "무엇을 어떻게 조합하나".
