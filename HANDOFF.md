# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-070 **아키텍처 문서 심화(#59) 충돌 해소**. 071(#60)이 먼저 머지돼 #59가 라이브파일 충돌 → `git merge main`으로 해소(architecture.md 무충돌, _CATALOG 두 줄 병합, 라이브=main/071 채택 + 070 기록 추가). 병합 push 후 #59 머지 가능. **문서별 심화 063~071 = 기획+개발명세 템플릿 계열 전부 최신화(070만 머지 대기).** Class A.
- **Current mode**: fullstack
- **Next TODO**: ① **개발명세 계열 완료** — 남은 심화 축: 기획서 *지침*군(운영 12·마케팅 13·브랜드 14·PM 15·AI기능 16·평가 17), agency/ops 템플릿(proposal·qa·operation·profitability 등). ② **누적 심화(063~071)를 다운스트림에 일괄 sync** — 여러 PR 쌓였으니 세트로(강력 권장 타이밍). ③ 심화 산출물 실사용 시 craft 환류. ④ METH-060 잔여(ai-icons 번호 정리 등). **프로세스: branch-first 준수. #59(070) 먼저 머지 후 071 머지 시 라이브 파일 사소 충돌만 해소.**
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

- 2026-07-09: **METH-070 아키텍처 문서 심화 — arc42+C4+fitness functions (Class A, PR #59 · 충돌 해소 병합)** — 071(#60) 선머지로 라이브파일 충돌 → `git merge main` 해소(architecture.md 무충돌·_CATALOG 두 줄 병합·라이브=main/071 채택+070 기록). 웹리서치(arc42·C4/Simon Brown·Richards&Ford·fitness functions·OWASP·LLM 게이트웨이) → `architecture.md` 14→21섹션: **§2 품질속성 top3**(least-worst·측정 시나리오) · **§16 적합성 함수**(CI, 지침19) · **§4 C4**(Mermaid) · **§6 런타임 뷰** · **§11 신뢰경계/위협**(STRIDE-lite) · **§14 배포 뷰** · **§15 AI 아키텍처**(게이트웨이·폴백·RAG·가드레일/eval 배치·예산, 조건부) · **§20 리스크/기술부채**. _CATALOG 갱신.
- 2026-07-09: **METH-071 데이터 모델 심화 — ERD·키·무중단 마이그레이션 (Class A, PR #60 머지)** — 문서별 심화 9번(개발명세 계열 마무리). 웹리서치(PostgreSQL·AWS·pgvector·OWASP LLM·RFC 9562) → `data-model.md` 강화. **§1 Mermaid ERD**(crow's foot) · **키 전략**(surrogate 기본·분산/외부노출은 **UUIDv7**·ULID·opaque public ID, UUIDv4 PK 비권장) · Fields에 Key/Constraints/Indexed 컬럼 · **§4 cascade**(CASCADE 일회용부품/RESTRICT 독립중요/SET NULL, 고아 방지) · 제약(NOT NULL·UNIQUE·CHECK·enum) · **history 전략 태그**(soft-delete[GDPR 삭제 불충족]·SCD2·append-only·bi-temporal + 감사컬럼) · 인덱스 원칙(FK 명시·복합·covering·partial) · **§7 expand-contract 무중단 마이그레이션**(Expand→Backfill 청크→Contract, 단계별 가역·lock-safe = Class B rollback 증거) · **§6 PII 분류/보존/GDPR 삭제**(파생 벡터·캐시·백업 포함) · **§8 벡터/pgvector**(조건부, HNSW). 3NF 기본·비정규화 사유 명기. _CATALOG 갱신. **(070 architecture와 disjoint — 라이브만 2차 머지 시 사소 충돌.)**
- 2026-07-09: **METH-069 도메인 용어집 심화 — 유비쿼터스 언어 + SKOS (Class A, PR #58 머지)** — 문서별 심화 7번(기획 템플릿 계열 마지막). 웹리서치(Evans/Fowler DDD·W3C SKOS·업계 glossary 표준·2026 AI 그라운딩 arXiv) → `context-glossary.md` 강화. **위상 재정의: 유비쿼터스 언어 계약**(표준어가 코드·UI에 그대로 흐름, 사전 아님). **SKOS 매핑**(표준어=prefLabel·동의어=altLabel·`_Avoid_`=hiddenLabel). 추가(전부 용어당 선택 → 소규모 최소형 유지): **바운디드 컨텍스트**(같은 단어 맥락별 다른 뜻, Fowler meter 사례, false unification 금지) · 상태(Draft/Approved/Deprecated)/Owner · See also(관련어, 혼동쌍과 구분) · **Code/UI 식별자 매핑**(유비쿼터스 언어 핵심·린트 타깃) · 약어(다의어 AI 오해석 위험) · **AI 스티어링 훅**(CLAUDE/AGENTS/llms.txt 링크=그라운딩) · **린트 훅**(`_Avoid_`=Vale/CI 가드레일). _CATALOG 갱신.
- 2026-07-09: **METH-068 KPI 단위경제 트리 심화 (Class A, PR #57 머지)** — 문서별 심화 6번. 웹리서치(a16z·Bessemer·Skok·Reforge·Amplitude 1차) → `kpi-tree.md` 강화(현행=마켓플레이스 GMV 워터폴). **§1 비즈모델 top-line 토글**(마켓/구독 MRR·ARR/거래 AOV/사용량 AI) → 공통 Gross→CM 워터폴 · **§2 단위경제**(CAC·**gross-margin LTV**·LTV:CAC 3~5:1[>5=성장 과소투자]·**CAC payback** on GM·CM/단위) · **§3 리텐션**(NRR ≥100/엘리트120·GRR ~90·로고vs매출 churn·코호트 평탄=PMF) · **§4 자본효율**(Rule of 40·Burn Multiple<2·Magic Number·Quick Ratio) · **§5 AI COGS**(추론/토큰비=변동, AI GM 50~60% vs SaaS 80%+·CPAU·워크플로우당 CM·추론비 연 10x 하락) · **§6 드라이버 트리**(North Star=입력레버 곱, *마진 워터폴과 상보·혼동 금지*) · 벤치마크 스트립. 지침 §19.11(10-패널·AAARR·LTV/CAC 벤치) 중복은 링크. _CATALOG 갱신. **branch-first 준수(067 사고 후 메모리 반영).**
- 2026-07-09: **METH-067 PRD 심화 — AI 시대 PRD + metric tree (Class A, main 직접·A)** — 문서별 심화 5번. 웹리서치(AI-era PRD[Innovation Mode·ideaplan]·HEART·North Star·가드레일 지표·RAT) → `prd.md` 강화(이미 11섹션 탄탄 → 진짜 공백만, lean 유지). **§9 AI 제품 요구**(핵심: AI는 확률적이라 이진 AC로 품질 표현 불가 → **eval 임계 3단**[launch/target/aspirational, 분포·신뢰구간] · **가드레일**[입력필터/출력검증/행동경계/에스컬레이션] · **실패모드→fallback**[품질실패/가용성실패] · 모델전략·비용, 상세는 16/17 링크) · **§4.3 불변식(DO-NOT-CHANGE)**(AI 구현자 보호 표면, Class B 짝) · §5 **테스트가능 AC + 입출력 예시**(에이전트 소비, 링크 복사금지) · **§11 성공지표 metric tree**(North Star + HEART input + **가드레일/카운터 지표** · AI는 모델품질/제품성과 분리) · **§12 가정 검증 레지스터**(검증계획·confidence·**RAT**). 리빙문서 버전 헤더. _CATALOG 갱신.
