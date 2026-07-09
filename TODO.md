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

### METH-068 · KPI 단위경제 트리 심화 (unit economics + 드라이버 트리)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 6번. 웹리서치(a16z·Bessemer·Skok·Reforge·Amplitude 1차) → `kpi-tree.md` 강화(현행=마켓플레이스 GMV 워터폴). 추가: **§1 비즈모델 top-line 토글**(마켓/구독 MRR·NRR/GRR/거래 AOV/사용량 AI) · **§2 단위경제**(CAC·**gross-margin LTV**·LTV:CAC 3~5:1[>5=과소투자]·**CAC payback**·CM/단위) · **§3 리텐션**(NRR/GRR·로고vs매출 churn·코호트 평탄=PMF) · **§4 자본효율**(Rule of 40·Burn Multiple·Magic Number·Quick Ratio) · **§5 AI COGS**(추론/토큰비·AI GM 50~60%·CPAU·워크플로우당 CM) · **§6 드라이버 트리**(North Star→입력레버, 워터폴과 구분) · 벤치마크 스트립. 지침 §19.11 중복은 링크. _CATALOG 갱신. **branch-first 준수(메모리 반영).**

### METH-067 · PRD 심화 (AI 시대 PRD + metric tree)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 5번. 웹리서치(AI-era PRD·HEART·North Star·가드레일 지표·RAT) → `prd.md` 강화(이미 11섹션 탄탄 → 진짜 공백만). 추가: **§9 AI 제품 요구**(확률적이라 이진 AC로 표현 불가 → eval 임계 3단[launch/target/aspirational]·가드레일[입력필터/출력검증/행동경계/에스컬레이션]·실패모드→fallback[품질/가용성]·모델전략·비용, 상세는 16/17 링크) · **§4.3 불변식(DO-NOT-CHANGE)**(AI 구현자 보호표면) · §5 **테스트가능 AC+예시**(에이전트 소비) · **§11 성공지표 metric tree**(North Star+HEART+가드레일/카운터·AI는 모델품질/제품성과 분리) · **§12 가정 검증 레지스터**(검증계획·confidence·RAT). 리빙문서 버전 헤더. lean 유지(2-3p). _CATALOG 갱신.

### METH-066 · 요구사항정의서 심화 (ISO/IEC/IEEE 29148)
- **notes**: 2026-07-09. Class A. PR 대기(main 직접). 문서별 심화 4번. 웹리서치(29148·BABOK·RTM·검증방법·우선순위 프레임) → `requirements-spec` 대장 강화(functional-spec EARS의 상류=shall 대장). 추가: 범위·전제 섹션 · **유형(BABOK 계층: business/stakeholder/functional/NFR/transition/constraint)** · **인수기준·검증방법(I/A/D/T)** 컬럼 · **상태 생명주기**(제안→검토→승인→구현→검증 / 보류·반려) · **하위추적(FS-ID/US/TC)** · **변경등급(A/B/C)** · 작성 규율(shall 규약·atomic·금지 모호어·9+5 품질특성) · 우선순위(MoSCoW+Pn / WSJF·RICE·Kano) · **RTM 양방향(링크 복사금지)**. _CATALOG 한줄 갱신. 경량 최소 컬럼 명시(과설계 방지).

### METH-065 · 서비스기획서 자식 산출물 8종 최신화 (2025-26 웹리서치)
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). 문서별 심화 3번 — 064에서 정한 자식 산출물 8종을 4개 병렬 리서치 에이전트(1차 소스)로 최신화. **user-story**(Job Story·**Gherkin AC**·INVEST·DoR/DoD·SPIDR) · **functional-spec**(**EARS 표기**·상태전이·측정 NFR·추적표) · **service-policy**(**의사결정 표+hit policy**·effective-dating·변경이력·AI 가드레일) · **ia-spec**(Screen-ID 규약·메뉴트리·RBAC·IA 검증) · **user-flow**(**Mermaid**·엣지케이스 체크리스트·actor) · **wireframe**(**5-state** Empty/Loading/Partial/Error/Success·콜아웃·a11y/반응형·Figma) · **api-contract**(**RFC 9457** Problem Details·RFC 9745/8594 deprecation·cursor 페이지네이션·OpenAPI 3.1) · **microcopy**(콘텐츠원칙·Voice/Tone·에러패턴·용어사전·i18n·AI 스캐폴드). _CATALOG 한줄 8개 갱신. 공통 수렴: **사람 표 + 기계판독/추적 미러 + AI가 빠뜨리는 "불행 경로" 강제.**

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
