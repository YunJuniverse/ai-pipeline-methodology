# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-070 **아키텍처 문서 심화**. 문서별 심화 8번(개발명세 계열 시작) — `architecture.md`를 웹리서치(arc42·C4·fitness functions·OWASP·AI 게이트웨이)로 강화. 추가: 품질속성 top3·적합성 함수(CI)·C4 다이어그램·런타임/배포 뷰·신뢰경계/위협(STRIDE)·AI 아키텍처(조건부)·리스크/기술부채. Class A. PR 대기(main 직접). **선행 061~066 #51~#56·068 #57·069 #58 머지 · 067 main직접(A).**
- **Current mode**: fullstack
- **Next TODO**: ① **문서별 심화 계속** — 개발명세 남은 것: `data-model`. 기획서 *지침*군(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17), agency/ops 템플릿(proposal·qa·operation 등). ② 심화 산출물 실사용 시 craft 환류. ③ **누적 심화(063~070)를 다운스트림에 일괄 sync** 검토(여러 PR 쌓임). ④ METH-060 잔여(ai-icons 번호 정리 등). **프로세스: branch-first 규율 준수 중.**
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

- 2026-07-09: **METH-070 아키텍처 문서 심화 — arc42 + C4 + fitness functions (Class A, PR 대기)** — 문서별 심화 8번(개발명세 계열 시작). 웹리서치(arc42 12섹션·C4/Simon Brown·Richards&Ford 아키텍처 특성·ThoughtWorks fitness functions·OWASP STRIDE·LLM 게이트웨이) → `architecture.md` 강화(현행 14섹션 탄탄, arc42 매핑으로 gap 도출). **§2 품질 속성 우선순위 top3**(least-worst·측정 시나리오·트레이드오프·의도적 제외) · **§16 적합성 함수**(특성→지표→검사→임계→CI 위치, 지침19 연결) · **§4 C4**(Context+Container, Mermaid diagrams-as-code) · **§6 런타임 뷰**(핵심 시나리오 sequence) · **§11 신뢰경계·위협**(STRIDE-lite, 경계별·완화는 §8/§9 재사용) · **§14 배포 뷰** · **§15 AI 아키텍처**(게이트웨이·폴백·RAG·가드레일/eval 배치·예산, 조건부→16/17 링크) · **§20 리스크/기술부채 register**(§21 미해결 결정과 구분). risk-driven "just enough" + docs-as-AI-context 프리앰블. _CATALOG 갱신.
- 2026-07-09: **METH-069 도메인 용어집 심화 — 유비쿼터스 언어 + SKOS (Class A, PR #58 머지)** — 문서별 심화 7번(기획 템플릿 계열 마지막). 웹리서치(Evans/Fowler DDD·W3C SKOS·업계 glossary 표준·2026 AI 그라운딩 arXiv) → `context-glossary.md` 강화. **위상 재정의: 유비쿼터스 언어 계약**(표준어가 코드·UI에 그대로 흐름, 사전 아님). **SKOS 매핑**(표준어=prefLabel·동의어=altLabel·`_Avoid_`=hiddenLabel). 추가(전부 용어당 선택 → 소규모 최소형 유지): **바운디드 컨텍스트**(같은 단어 맥락별 다른 뜻, Fowler meter 사례, false unification 금지) · 상태(Draft/Approved/Deprecated)/Owner · See also(관련어, 혼동쌍과 구분) · **Code/UI 식별자 매핑**(유비쿼터스 언어 핵심·린트 타깃) · 약어(다의어 AI 오해석 위험) · **AI 스티어링 훅**(CLAUDE/AGENTS/llms.txt 링크=그라운딩) · **린트 훅**(`_Avoid_`=Vale/CI 가드레일). _CATALOG 갱신.
- 2026-07-09: **METH-068 KPI 단위경제 트리 심화 (Class A, PR #57 머지)** — 문서별 심화 6번. 웹리서치(a16z·Bessemer·Skok·Reforge·Amplitude 1차) → `kpi-tree.md` 강화(현행=마켓플레이스 GMV 워터폴). **§1 비즈모델 top-line 토글**(마켓/구독 MRR·ARR/거래 AOV/사용량 AI) → 공통 Gross→CM 워터폴 · **§2 단위경제**(CAC·**gross-margin LTV**·LTV:CAC 3~5:1[>5=성장 과소투자]·**CAC payback** on GM·CM/단위) · **§3 리텐션**(NRR ≥100/엘리트120·GRR ~90·로고vs매출 churn·코호트 평탄=PMF) · **§4 자본효율**(Rule of 40·Burn Multiple<2·Magic Number·Quick Ratio) · **§5 AI COGS**(추론/토큰비=변동, AI GM 50~60% vs SaaS 80%+·CPAU·워크플로우당 CM·추론비 연 10x 하락) · **§6 드라이버 트리**(North Star=입력레버 곱, *마진 워터폴과 상보·혼동 금지*) · 벤치마크 스트립. 지침 §19.11(10-패널·AAARR·LTV/CAC 벤치) 중복은 링크. _CATALOG 갱신. **branch-first 준수(067 사고 후 메모리 반영).**
- 2026-07-09: **METH-067 PRD 심화 — AI 시대 PRD + metric tree (Class A, main 직접·A)** — 문서별 심화 5번. 웹리서치(AI-era PRD[Innovation Mode·ideaplan]·HEART·North Star·가드레일 지표·RAT) → `prd.md` 강화(이미 11섹션 탄탄 → 진짜 공백만, lean 유지). **§9 AI 제품 요구**(핵심: AI는 확률적이라 이진 AC로 품질 표현 불가 → **eval 임계 3단**[launch/target/aspirational, 분포·신뢰구간] · **가드레일**[입력필터/출력검증/행동경계/에스컬레이션] · **실패모드→fallback**[품질실패/가용성실패] · 모델전략·비용, 상세는 16/17 링크) · **§4.3 불변식(DO-NOT-CHANGE)**(AI 구현자 보호 표면, Class B 짝) · §5 **테스트가능 AC + 입출력 예시**(에이전트 소비, 링크 복사금지) · **§11 성공지표 metric tree**(North Star + HEART input + **가드레일/카운터 지표** · AI는 모델품질/제품성과 분리) · **§12 가정 검증 레지스터**(검증계획·confidence·**RAT**). 리빙문서 버전 헤더. _CATALOG 갱신.
- 2026-07-09: **METH-066 요구사항정의서 심화 — ISO/IEC/IEEE 29148 (Class A, PR #56 머지)** — 문서별 심화 4번. 웹리서치(29148 SRS·BABOK 요구 계층·RTM·검증방법·우선순위 프레임) → `requirements-spec` 대장 강화. `functional-spec`(EARS)의 *상류 = shall 대장*. 추가: **범위·전제** 섹션 · 대장에 **유형(BABOK 계층: business/stakeholder/functional/NFR/transition/constraint)·인수기준·검증(I/A/D/T)·상태 생명주기(제안→검토→승인→구현→검증 / 보류·반려)·하위추적(FS-ID/US/TC)·변경등급(A/B/C)** 컬럼 · **작성 규율**(shall 규약·atomic·금지 모호어·개별 9특성+SET 5특성) · **우선순위 프레임**(MoSCoW+Pn / WSJF·RICE·Kano) · **RTM 양방향**(후방 출처↔전방 테스트, *링크 복사금지*). _CATALOG 한줄 갱신. 경량 최소 컬럼 명시(과설계 방지). 공통 원칙 재확인: 대장=SSOT, 하류는 요구ID 링크.
