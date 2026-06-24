# Checkpoint — 2026-06-24 (METH-047 클린아키텍처·클린코드 개발 규칙 — 지침 19 신설)

> ✅ METH-047: 적용 프로젝트 GambleScan의 Clean Code/Architecture 리팩토링(REFACTOR-CLEAN,
> R0~R4 ~50 PR)의 회고+신설 가이드를 방법론으로 역환류. 핵심 통찰: 백서/지침 17 §4.2
> **Guardrails-by-Construction**(원래 AI 안전용)이 *코드 품질*에도 유효 — "첫날부터 4 가드레일이
> `error`였다면 부채가 안 쌓인다". `20_guides/19_클린아키텍처_클린코드_개발규칙.md` 신설 +
> README 카탈로그/v4 + CLAUDE/AGENTS §7 포인터. fullstack/dev 트랙. Class A.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-047-clean-architecture-guide` (main 기준)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-047 클린아키텍처·클린코드 지침 19 신설** (사용자: "갬블스캔에서 클린코드/클린아키텍처
리팩토링 했어 → 확인 → 역주입해"):

- 출처: GambleScan `docs/snapshots/2026-06-24-refactor-clean-retrospective.md` +
  `20_guides/19_*`(GambleScan이 자체 신설). REFACTOR-CLEAN = R0(토대·가드레일)~R4(안전망),
  ~50 PR(#53~#112). 결과: lint 0/0, 4 ESLint 가드레일 전부 `error`, 도메인 순수로직 100% 테스트,
  god파일 15→0, 레이어위반 75→0, any 206→0. (eslint.config 실제 `error` 확인.)
- 작성(일반 craft만·GambleScan 도박/카지노 도메인 특화 제외·출처 명시):
  - `20_guides/19_클린아키텍처_클린코드_개발규칙.md` 신설(11절): Guardrails-by-Construction(코드
    품질)·4-레이어 의존성 규칙·**4 코드 가드레일(레이어경계·no-explicit-any·no-console·
    max-lines=400)**·래칫 원리·타입 정직성(any=버그은폐)·god파일 분할 패턴·네이밍·테스트·day-1
    체크리스트·안티패턴.
  - 교차참조 검증: 지침 17 §4.2 Guardrails-by-Construction *실재 확인*(line 136). CLAUDE.md §7
    Code And Review Rules ↔ 지침 19(강제 메커니즘) 양방향 포인터.
  - `20_guides/README.md` §3.5 카탈로그 + §6 현황 + §9 변경이력 v4 등재.
  - `CLAUDE.md`·`AGENTS.md` §7 에 지침 19 포인터 1줄.
- 검증 예정: wrap 4/4 → ship → PR.

## ⚠️ 다음 사람: 우선 처리 후보

- **METH-047 PR 머지**(사용자 승인 게이트).
- 머지 후 **다운스트림 sync** — 지침 19가 shared(`20_guides`)라 전파됨. CLAUDE/AGENTS §7 포인터는
  managed-merge(다운스트림 고유 §7 내용 보존되는지 확인). sync 는 METH-046 픽스로 이제 고유 파일
  보존 — 안전. cafe24 제외.

## 다음 사람에게 (구체적 첫 행동)

1. 사용자 지시 대기.
2. METH-047 PR 머지되면 → 다운스트림 sync(지침 19 전파).

## 막혔던 지점 / 시도해봤지만 안 된 것

- 없음. GambleScan 가이드가 이미 잘 일반화돼 있어, 방법론 파일로 교차참조 정렬 + 도메인 예시만
  일반화(예: supabase→`<db>`)하면 됐다.

## 미해결 결정사항 (Open Questions)

- 지침 19 의 max-lines=400·4-레이어는 *fullstack/dev 트랙* 기본값 — 스택/규모에 따라 ADR 로 조정
  가능(가이드에 명시). planning-only 트랙 비적용.

## 환경 메모

- 브랜치: `claude/meth-047-clean-architecture-guide` (main 기준).
- 변경: 신규 `20_guides/19_클린아키텍처_클린코드_개발규칙.md` + README + `CLAUDE.md`·`AGENTS.md` §7
  포인터 + 라이브 4종.
- 출처 프로젝트: GambleScan `/Users/hayden/gamblescan` (REFACTOR-CLEAN 회고 브랜치
  `docs/refactor-clean-retro-and-methodology`).
