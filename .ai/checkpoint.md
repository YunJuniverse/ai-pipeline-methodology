# Checkpoint — 2026-07-08 (METH-065 서비스기획서 자식 산출물 8종 최신화)

> ✅ METH-065: 문서별 심화 3번. 064가 정한 서비스기획서 자식 8종을 4개 병렬 웹리서치(1차 소스)로 2025-26 최신화.
> 공통 수렴: **사람이 읽는 표 + 기계판독/추적 미러 + AI가 빠뜨리는 "불행 경로"(에러·상태) 강제.**
> 🏁 다음: PR 리뷰·머지 → 문서별 심화 계속(대상 선정).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-065-child-templates-refresh` (fresh main 기준 — 064 머지 후 pull → 브랜치, 프로세스 교훈 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-065 — 서비스기획서 자식 산출물 8종 최신화** (사용자: "산출물 전체를 최신 방법론·양식·샘플로 업데이트"):

- **방법**: 4개 병렬 웹리서치 서브에이전트(그룹: story+func / policy+ia / flow+wireframe / api+microcopy), 1차 소스
  (INVEST·Gherkin·EARS·DMN·OPA·NN/g·OpenAPI 3.1·RFC 9457·Mailchimp·GOV.UK 등) → 각 문서 gap 도출 → 적용.
- **8종 변경 (`50_resources/templates/`)**:
  - `user-story`: Job Story 폼 · **Gherkin(G/W/T) AC 블록**(```gherkin, AI 스펙+검증) · INVEST 6체크 · DoR/DoD · SPIDR · Story ID/링크.
  - `functional-spec`: **EARS 표기**(5패턴) · State Transition 표 · 측정가능 NFR 표 · 추적표(요구↔AC↔테스트↔코드).
  - `service-policy`: **의사결정 표**(조건→액션·**hit policy**·Default 행) · **effective-dating**(버전·시행일, 이력 보존) · 예외=우선순위 행 · 변경이력 · **AI 가드레일 정책** 시트.
  - `ia-spec`: **Screen-ID 명명 규약** · 화면 인벤토리(Parent-ID) · 메뉴트리(global/local/utility) · **RBAC**(CRUD·default-deny·SoD) · 라벨링/택소노미 · **IA 검증**(카드소트/트리테스트 75%+).
  - `user-flow`: **Mermaid** flowchart/sequence 블록 · 3열 경로표(해피+불행) · Decision Y/N · **엣지케이스 체크리스트** · actor 태그.
  - `wireframe-spec`: **5-state**(Empty/Loading/**Partial**/Error/Success — AI 92% 누락) · 번호 콜아웃 표 · 접근성·반응형 · **Figma 링크·Ready-for-dev**.
  - `api-contract`: **RFC 9457 Problem Details**(`application/problem+json`) · RFC 9745/8594 Deprecation/Sunset · **cursor 페이지네이션** · 표준 RateLimit-* · Idempotency 상태규칙 · OpenAPI 3.1 정본.
  - `microcopy`: 콘텐츠 원칙 · **Voice(상수)/Tone(맥락) 표** · 에러 패턴(무엇+왜+복구) · 상태별 인벤토리 · 용어사전 · 포용/i18n 체크 · **AI 프롬프트 스캐폴드**.
  - `_CATALOG.md` §2 한줄 8개 갱신(특히 wireframe 3-state→5-state 팩트 수정).

## 다음 사람에게 (구체적 첫 행동)

1. METH-065 PR 리뷰·머지.
2. **문서별 심화 계속** — 대상 사용자와 합의. 후보: 요구사항정의서(requirements-spec)·prd·kpi-tree·context-glossary, 또는 다른 기획서(운영/마케팅/브랜드).
3. 자식 8종 실사용 시 EARS/의사결정표/Mermaid 실전 예를 지침 §19 craft로 환류.
4. guide 09·21 + api-contract + 갱신 8종을 다음 다운스트림 sync 대상에 포함.
5. METH-060 잔여: ai-icons 번호 정리 + cafe24·icons-invest clean 후 sync.

## 미해결 결정사항 (Open Questions)

- 서비스기획서 §6.0 산출물 인덱스 자동 생성 도구화 여부(064 open) — 유지.
- 캔버스(P4, 063)·Lean Canvas 별도 템플릿화 여부 — 유지.
- 갱신된 자식 템플릿이 커져도 lean 유지 원칙과 충돌 없는지 — 각 여전히 1스크린 내. 실사용 피드백으로 재점검.

## 환경 메모

- 브랜치: `claude/meth-065-child-templates-refresh` (fresh main 기준, 064 포함). main 직접 PR.
- 변경: `50_resources/templates/` 8종(user-story·functional-spec·service-policy·ia-spec·user-flow·wireframe-spec·api-contract·microcopy) + `_CATALOG.md` + 라이브 4종.
- 선행 061·062·063·064 = PR #51·#52·#53·#54 머지 완료(main 반영).
