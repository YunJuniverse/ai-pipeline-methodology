# Checkpoint — 2026-06-24 (METH-048 백서·온보딩에 코드 품질 가드레일 통합)

> ✅ METH-048: 지침 19(클린아키텍처·클린코드, METH-047)를 standalone에서 *방법론 표준 서사*로
> 통합(사용자 지시: "백서·가이드라인을 클린코드·클린아키텍처 기반으로 업데이트"). 백서 겸 가이드
> §5/§7 + **WHITEPAPER(헌법) §8-5 신규 운영 원칙 "Guardrails-by-Construction"**(AI 안전+코드 품질
> 횡단) + HOW_TO_APPLY §5. 백서 변경이라 **Class C — `40_dev/adr/ADR-003` 신설**(사용자 지시=승인).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-048-whitepaper-guide-codequality` (main 기준)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-048 백서·온보딩 코드 품질 통합** (사용자: "이걸 바탕으로 방법론 백서와 가이드라인도
업데이트해" — 직전 "앞으로 코드는 클린코드·클린아키텍처 규칙으로"에 이어):

- 배경: METH-047로 지침 19를 신설했으나 *standalone 가이드*라, 백서·온보딩의 표준 서사엔 미반영.
  → 코드 품질 가드레일을 방법론 일급 원칙으로 통합.
- 변경:
  - `10_foundation/방법론_백서_가이드.md` §5: "코드 품질 craft — Guardrails by Construction(지침 19)"
    소절 추가(4-레이어·4 가드레일·래칫·any=버그은폐). §7 워크플로: day-1 가드레일 + lint·typecheck·
    build·test 게이트.
  - `10_foundation/WHITEPAPER.md`(헌법): **§8-5 "Guardrails-by-Construction" 신규 운영 원칙**
    (강제=시스템/fail-closed/래칫/AI안전·코드품질 동일 적용) + 부록 A 지침 19 행 + 버전
    v0.2.0→v0.3.0(§12: 메커니즘 변경=MINOR).
  - `10_foundation/HOW_TO_APPLY.md` §5 Fullstack: day-1 가드레일 안내 + 구현 게이트.
  - **`40_dev/adr/ADR-003`** 신설 — 백서는 헌법(§12)이라 변경=Class C → ADR로 근거 고정(사용자
    지시=승인 증빙). Considered Options 3안 중 "§8-5 격상" 채택.
- 전파 메모: `10_foundation/`은 shared 아님 → 백서·온보딩은 다운스트림 미전파(업스트림 전용).
  지침 19(`20_guides`)는 METH-047로 이미 shared·전파 대상.
- 검증 예정: wrap 4/4 → ship → PR.

## ⚠️ 다음 사람: 우선 처리 후보

- **METH-048 PR 머지**(사용자 승인 게이트).
- 머지 후 다운스트림 sync는 *불필요*(변경이 10_foundation·40_dev = shared 아님). 지침 19는
  이미 전파됨. 다음 다운스트림 sync 시 METH-046 픽스 덕에 고유 파일 보존됨.

## 다음 사람에게 (구체적 첫 행동)

1. 사용자 지시 대기.
2. METH-048 PR 머지되면 백서·온보딩까지 코드 품질 통합 완료.

## 막혔던 지점 / 시도해봤지만 안 된 것

- 없음. 백서 헌법 변경이라 방법론 자체 규칙(§12 Class C)을 따라 ADR-003 동반 — 방법론이 자기
  거버넌스를 스스로 적용한 사례.

## 미해결 결정사항 (Open Questions)

- 백서 2종 관계(WHITEPAPER 헌법 vs 방법론_백서_가이드 종합본) — 둘 다 §8-5/§5에 같은 원리 기술.
  중복 누적 시 정본 정리 검토(METH-045 때 기록된 open question 유지).

## 환경 메모

- 브랜치: `claude/meth-048-whitepaper-guide-codequality` (main 기준).
- 변경: `10_foundation/{방법론_백서_가이드,WHITEPAPER,HOW_TO_APPLY}.md` + `40_dev/adr/ADR-003` +
  라이브 4종. (코드/지침/템플릿 변경 없음 — 문서 통합 한정.)
