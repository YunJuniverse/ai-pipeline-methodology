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

### METH-065 · 서비스기획서 자식 산출물 8종 최신화 (2025-26 웹리서치)
- **notes**: 2026-07-08. Class A. PR 대기(main 직접). 문서별 심화 3번 — 064에서 정한 자식 산출물 8종을 4개 병렬 리서치 에이전트(1차 소스)로 최신화. **user-story**(Job Story·**Gherkin AC**·INVEST·DoR/DoD·SPIDR) · **functional-spec**(**EARS 표기**·상태전이·측정 NFR·추적표) · **service-policy**(**의사결정 표+hit policy**·effective-dating·변경이력·AI 가드레일) · **ia-spec**(Screen-ID 규약·메뉴트리·RBAC·IA 검증) · **user-flow**(**Mermaid**·엣지케이스 체크리스트·actor) · **wireframe**(**5-state** Empty/Loading/Partial/Error/Success·콜아웃·a11y/반응형·Figma) · **api-contract**(**RFC 9457** Problem Details·RFC 9745/8594 deprecation·cursor 페이지네이션·OpenAPI 3.1) · **microcopy**(콘텐츠원칙·Voice/Tone·에러패턴·용어사전·i18n·AI 스캐폴드). _CATALOG 한줄 8개 갱신. 공통 수렴: **사람 표 + 기계판독/추적 미러 + AI가 빠뜨리는 "불행 경로" 강제.**

### METH-064 · 서비스기획서 = 부모(인덱스) 모델
- **notes**: 2026-07-08. Class A. **PR #54 머지 완료.** 문서별 심화 2번. 사용자 통찰("서비스기획서는 여러 문서의 총합 아닌가")이 지침11 내부 모순(§2/§6=컨테이너 vs §19.2="12 중 한 장")을 드러냄. 웹리서치(GitHub Spec Kit spec.md·Cagan·Amazon PR/FAQ·Shape Up No-gos·한국 화면설계서 해체) → **결정적으로 index(컨테이너 아님)**. 반영: §2.2 위상 재정의(부모=의도·결정·경계 소유 / 자식=상세·열거) · §6 각 항목 [원본]/[인덱스→자식] 재라벨 · §6.0 산출물 인덱스(척추, 자식 링크+상태) · §8.1 척추 재정렬 · 비목표(Non-Goals) 1급화 · §16 인덱스 모델 체크 · §19.14 환류 · 스켈레톤 `30_planning/11` 재작성. **프로세스 사고: stale local main 기준 브랜치→복구(pull 후 재베이스).**

### METH-063 · 사업기획서 문서 디벨롭 (problem-first 척추 + 청중 변형)
- **notes**: 2026-07-08. Class A. **PR #53 머지 완료.** 문서별 심화 1번 대상. 웹리서치(YC·Sequoia·SBA·Lean/BM Canvas·K-Startup PSST 1차 소스) → 우리 사업기획서 고찰 → 제안 P1~P4 전체 반영. **핵심 명제: 지식(craft §19)이 구조(스켈레톤·§8 목차)보다 앞서 있어, craft를 1급 섹션으로 승격.** P1 §8.1 problem-first 척추 재정렬 + 왜지금(§6.16)·트랙션(§6.17)·팀-as-thesis(§6.19)·Exec Summary 선두 신설 + TAM/SAM/SOM bottom-up 강제(§6.2). P2 청중 변형 PSST 정부지원사업(§8.4)·IR(§8.5). P3 품질 5대 크로스체크(§16)+비목표. P4 1페이지 캔버스 옵션(§18.4). 스켈레톤 `30_planning/10` 척추 정합 재작성. §9.11~9.13 작성기준 + §19.14 근거우위 + 환류 노트.

### METH-062 · API 계약 템플릿 + 개발명세 작성 지침
- **notes**: 2026-07-08. Class A. PR 대기(main 직접, 신규). 커밋 `169a3c2`가 선행 PR #51에 미포함돼 main 기준 새 브랜치로 cherry-pick 복구(작업 손실 0). 사용자 질문("개발기획서 필요?")에서 도출. **결론: 단일 개발기획서=반대(architecture+wbs+master_plan+adr 재번들=단일출처 위반).** 대신 진짜 공백 2개 채움: ① 신규 템플릿 `api-contract.md`(엔드포인트·요청/응답·에러·버전·인증 — 개발리드→개발자 FE/BE 병렬 조율축, functional-spec의 상위 시스템 레벨) → dev/fullstack/agency 세트+매트릭스 편입. ② 신규 지침 `20_guides/21_개발명세_작성_지침.md`(개발명세 6종 조합·원본경계·개발자용 "여기서 시작" 읽는 순서·게이트·재번들 금지 근거) → README §3.5. 방법론 기획-헤비/개발명세-라이트 보정. METH-061 09(핸드오프 재포맷)와 짝.

> 최근 완료 ~4건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

<!-- Archived: METH-001~056 (2026-05~07). 055 RFC-002 accepted(#45)·056 Compaction R2(#46) 포함. 상세는 git log --grep="METH-" 및 PR #5~#49, 40_dev/snapshots/ 참조. -->
