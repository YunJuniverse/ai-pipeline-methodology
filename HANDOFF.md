# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-068 **KPI 단위경제 트리 심화**. 문서별 심화 6번 — `kpi-tree.md`(마켓플레이스 GMV 워터폴)를 웹리서치(a16z·Bessemer·Amplitude)로 강화. 추가: 비즈모델 top-line 토글·단위경제(LTV/CAC/payback)·NRR/GRR·자본효율(Rule40·burn multiple)·AI COGS·드라이버 트리(North Star). Class A. PR 대기(main 직접). **선행 061~066 PR #51~#56 머지 · 067 PRD는 main 직접(A).**
- **Current mode**: fullstack
- **Next TODO**: ① **문서별 심화 계속** — 남은 대상: context-glossary(기획 계열), 다른 기획서 지침(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17), 개발명세(architecture·data-model). ② 심화 산출물 실사용 시 craft 환류. ③ **누적 심화(063~068)를 다운스트림에 일괄 sync** 검토. ④ METH-060 잔여(ai-icons 번호 정리 등). **프로세스: branch-first 규율(메모리) — 착수 첫 커맨드 pull + `git checkout -b`, ship `branch:`가 main이면 정지.**
- **Blockers**: none

## Active Links

- Current PR: METH-067 PRD 심화 (신규) · 문서별 심화 063~066 = #53~#56 머지 완료
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

- 2026-07-09: **METH-068 KPI 단위경제 트리 심화 (Class A, PR 대기)** — 문서별 심화 6번. 웹리서치(a16z·Bessemer·Skok·Reforge·Amplitude 1차) → `kpi-tree.md` 강화(현행=마켓플레이스 GMV 워터폴). **§1 비즈모델 top-line 토글**(마켓/구독 MRR·ARR/거래 AOV/사용량 AI) → 공통 Gross→CM 워터폴 · **§2 단위경제**(CAC·**gross-margin LTV**·LTV:CAC 3~5:1[>5=성장 과소투자]·**CAC payback** on GM·CM/단위) · **§3 리텐션**(NRR ≥100/엘리트120·GRR ~90·로고vs매출 churn·코호트 평탄=PMF) · **§4 자본효율**(Rule of 40·Burn Multiple<2·Magic Number·Quick Ratio) · **§5 AI COGS**(추론/토큰비=변동, AI GM 50~60% vs SaaS 80%+·CPAU·워크플로우당 CM·추론비 연 10x 하락) · **§6 드라이버 트리**(North Star=입력레버 곱, *마진 워터폴과 상보·혼동 금지*) · 벤치마크 스트립. 지침 §19.11(10-패널·AAARR·LTV/CAC 벤치) 중복은 링크. _CATALOG 갱신. **branch-first 준수(067 사고 후 메모리 반영).**
- 2026-07-09: **METH-067 PRD 심화 — AI 시대 PRD + metric tree (Class A, main 직접·A)** — 문서별 심화 5번. 웹리서치(AI-era PRD[Innovation Mode·ideaplan]·HEART·North Star·가드레일 지표·RAT) → `prd.md` 강화(이미 11섹션 탄탄 → 진짜 공백만, lean 유지). **§9 AI 제품 요구**(핵심: AI는 확률적이라 이진 AC로 품질 표현 불가 → **eval 임계 3단**[launch/target/aspirational, 분포·신뢰구간] · **가드레일**[입력필터/출력검증/행동경계/에스컬레이션] · **실패모드→fallback**[품질실패/가용성실패] · 모델전략·비용, 상세는 16/17 링크) · **§4.3 불변식(DO-NOT-CHANGE)**(AI 구현자 보호 표면, Class B 짝) · §5 **테스트가능 AC + 입출력 예시**(에이전트 소비, 링크 복사금지) · **§11 성공지표 metric tree**(North Star + HEART input + **가드레일/카운터 지표** · AI는 모델품질/제품성과 분리) · **§12 가정 검증 레지스터**(검증계획·confidence·**RAT**). 리빙문서 버전 헤더. _CATALOG 갱신.
- 2026-07-09: **METH-066 요구사항정의서 심화 — ISO/IEC/IEEE 29148 (Class A, PR #56 머지)** — 문서별 심화 4번. 웹리서치(29148 SRS·BABOK 요구 계층·RTM·검증방법·우선순위 프레임) → `requirements-spec` 대장 강화. `functional-spec`(EARS)의 *상류 = shall 대장*. 추가: **범위·전제** 섹션 · 대장에 **유형(BABOK 계층: business/stakeholder/functional/NFR/transition/constraint)·인수기준·검증(I/A/D/T)·상태 생명주기(제안→검토→승인→구현→검증 / 보류·반려)·하위추적(FS-ID/US/TC)·변경등급(A/B/C)** 컬럼 · **작성 규율**(shall 규약·atomic·금지 모호어·개별 9특성+SET 5특성) · **우선순위 프레임**(MoSCoW+Pn / WSJF·RICE·Kano) · **RTM 양방향**(후방 출처↔전방 테스트, *링크 복사금지*). _CATALOG 한줄 갱신. 경량 최소 컬럼 명시(과설계 방지). 공통 원칙 재확인: 대장=SSOT, 하류는 요구ID 링크.
- 2026-07-08: **METH-065 서비스기획서 자식 산출물 8종 최신화 (Class A, PR #55 머지)** — 문서별 심화 3번. 064가 정한 자식 8종을 **4개 병렬 웹리서치 에이전트**(1차 소스)로 2025-26 최신화. **user-story**: Job Story 폼·**Gherkin(Given/When/Then) AC 블록**(AI 스펙+검증 오라클)·INVEST 체크·DoR/DoD·SPIDR 분할. **functional-spec**: **EARS 표기**(5패턴, NASA·Airbus 표준)·상태전이 표·측정가능 NFR·추적표(요구↔AC↔테스트↔코드). **service-policy**: **의사결정 표**(조건→액션·hit policy·Default 행)·effective-dating(과거 이력 보존)·변경이력·AI 가드레일 정책. **ia-spec**: Screen-ID 명명 규약·메뉴트리(global/local/utility)·RBAC(CRUD·default-deny·SoD)·IA 검증(카드소트/트리테스트 75%+). **user-flow**: **Mermaid** flowchart/sequence·3열 경로표·엣지케이스 체크리스트·actor 태그. **wireframe**: **5-state**(Empty/Loading/Partial/Error/Success — AI가 92% 누락)·번호 콜아웃·접근성/반응형·Figma 링크. **api-contract**: **RFC 9457 Problem Details**·RFC 9745/8594 deprecation·cursor 페이지네이션·OpenAPI 3.1. **microcopy**: 콘텐츠 원칙·Voice(상수)/Tone(맥락) 표·에러 패턴·용어사전·i18n·AI 프롬프트 스캐폴드. `_CATALOG` 한줄 8개 갱신. **공통 수렴: 사람 표 + 기계판독/추적 미러 + AI가 빠뜨리는 "불행 경로"(에러·상태) 강제.**
- 2026-07-08: **METH-064 서비스기획서 = 부모(인덱스) 모델 (Class A, PR #54 머지)** — 문서별 심화 2번. 사용자 통찰("서비스기획서는 여러 문서의 총합 아닌가")이 지침11 내부 모순을 드러냄 — §2/§6은 "구조·기능·정책의 *원본 컨테이너*"라 하는데 §19.2는 "12 산출물 중 *한 장*"이라 함(단일출처 붕괴, ia-spec·functional-spec·service-policy 등 자식 템플릿과 중복). 웹리서치(GitHub Spec Kit spec.md=WHAT/WHY·HOW배제 / Cagan=프로토타입이 화면스펙 / Amazon PR·FAQ / Shape Up No-gos / Atlassian·Figma link-don't-embed / 한국 화면설계서 모놀리스→Notion·Figma ID 인덱스 해체) → **결정적으로 index(컨테이너 아님)**. 반영: §2.2 위상 재정의(**부모=의도·결정·경계 소유 / 자식=상세·열거, 링크 not 복사**) · §6 각 항목 [원본]/[인덱스→자식] 재라벨 · **§6.0 산출물 인덱스**(척추: 자식 링크+상태+소유자) · §8.1 척추 재정렬 · **비목표(Non-Goals) 1급화** · §16 인덱스 모델 체크 · §19.14 환류. 스켈레톤 `30_planning/11` 인덱스 척추로 재작성. METH-062 개발기획서 "재번들 반대"와 동형. **프로세스 사고+복구**: stale local main(post-#52) 기준으로 브랜치→pull 후 재베이스로 복구(작업 손실 0).
