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

### METH-070 · 아키텍처 문서 심화 (arc42 + C4 + fitness functions)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 8번(개발명세 계열 시작). 웹리서치(arc42·C4/Simon Brown·Richards&Ford·ThoughtWorks fitness functions·OWASP·AI 게이트웨이) → `architecture.md` 강화(현행 14섹션 탄탄, arc42 매핑으로 gap 도출). 추가: **§2 품질 속성 우선순위 top3**(least-worst·측정 시나리오·트레이드오프) · **§16 적합성 함수**(CI 가드레일, 지침19 연결) · **§4 C4 다이어그램**(Context+Container, Mermaid) · **§6 런타임 뷰**(핵심 시나리오 sequence) · **§11 신뢰경계·위협**(STRIDE-lite, 경계별) · **§14 배포 뷰** · **§15 AI 아키텍처**(게이트웨이·폴백·RAG·가드레일/eval 배치·예산, 조건부) · **§20 리스크/기술부채 register**(미해결 결정과 구분). risk-driven "just enough" + docs-as-AI-context 프리앰블. _CATALOG 갱신. branch-first 준수.

### METH-069 · 도메인 용어집 심화 (유비쿼터스 언어 + SKOS)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 7번(기획 계열 마지막). 웹리서치(Evans/Fowler DDD·W3C SKOS·업계 glossary 표준·2026 AI 그라운딩 논문) → `context-glossary.md` 강화. 위상 재정의: **유비쿼터스 언어 계약**(표준어가 코드·UI에 그대로). SKOS 매핑(표준어=prefLabel·동의어=altLabel·`_Avoid_`=hiddenLabel). 추가(전부 용어당 선택): **바운디드 컨텍스트**(같은 단어 맥락별 다른 뜻, false unification 금지) · 상태(Draft/Approved/Deprecated)/Owner · See also(관련어) · **Code/UI 식별자 매핑**(린트 타깃) · 약어(다의어 AI 위험) · **AI 스티어링 훅**(CLAUDE/AGENTS/llms.txt 링크) · **린트 훅**(`_Avoid_`=CI 가드레일). _CATALOG 갱신. branch-first 준수.

### METH-068 · KPI 단위경제 트리 심화 (unit economics + 드라이버 트리)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 6번. 웹리서치(a16z·Bessemer·Skok·Reforge·Amplitude 1차) → `kpi-tree.md` 강화(현행=마켓플레이스 GMV 워터폴). 추가: **§1 비즈모델 top-line 토글**(마켓/구독 MRR·NRR/GRR/거래 AOV/사용량 AI) · **§2 단위경제**(CAC·**gross-margin LTV**·LTV:CAC 3~5:1[>5=과소투자]·**CAC payback**·CM/단위) · **§3 리텐션**(NRR/GRR·로고vs매출 churn·코호트 평탄=PMF) · **§4 자본효율**(Rule of 40·Burn Multiple·Magic Number·Quick Ratio) · **§5 AI COGS**(추론/토큰비·AI GM 50~60%·CPAU·워크플로우당 CM) · **§6 드라이버 트리**(North Star→입력레버, 워터폴과 구분) · 벤치마크 스트립. 지침 §19.11 중복은 링크. _CATALOG 갱신. **branch-first 준수(메모리 반영).**

### METH-067 · PRD 심화 (AI 시대 PRD + metric tree)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 5번. 웹리서치(AI-era PRD·HEART·North Star·가드레일 지표·RAT) → `prd.md` 강화(이미 11섹션 탄탄 → 진짜 공백만). 추가: **§9 AI 제품 요구**(확률적이라 이진 AC로 표현 불가 → eval 임계 3단[launch/target/aspirational]·가드레일[입력필터/출력검증/행동경계/에스컬레이션]·실패모드→fallback[품질/가용성]·모델전략·비용, 상세는 16/17 링크) · **§4.3 불변식(DO-NOT-CHANGE)**(AI 구현자 보호표면) · §5 **테스트가능 AC+예시**(에이전트 소비) · **§11 성공지표 metric tree**(North Star+HEART+가드레일/카운터·AI는 모델품질/제품성과 분리) · **§12 가정 검증 레지스터**(검증계획·confidence·RAT). 리빙문서 버전 헤더. lean 유지(2-3p). _CATALOG 갱신.


> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
