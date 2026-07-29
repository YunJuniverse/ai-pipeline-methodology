# Checkpoint — 2026-07-29 (METH-118 백로그 등록 + TODO 손상 복구)

> ✅ METH-118(프롬프팅 코칭 루프) Backlog 등록 + #117에 혼입됐던 TODO.md 손상 정본 복구. branch `chore/backlog-meth-118-prompt-coaching`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `chore/backlog-meth-118-prompt-coaching` (base=main 1e6f1cd, branch-first)

## 방금 한 것 (이번 세션 마지막 구간)

- **METH-118 등록**: 사용자 요청(프롬프팅 자가 교정 데이터·리포트) → 설계 방향 확정: 온디맨드가 아닌 **상시 자동 기록**(wrap 의무 — observe `prompting:` 블록: 총 라운드·교환별 intent/rounds/모호 지시 발췌+교정안/용어/상황 태그/재지시 패턴) + **prompt-report 자동 갱신**(wrap 파이프라인이 재생성, boot 헤드라인 표시). 한계 합의: 토큰 실측은 세션 내 불가 → v1 프록시(라운드·재지시 수), PostHog `llma-cc-setup` 연동은 옵션 게이트. 원문 전체 저장 금지(발췌만). 교차-repo 통합 v1 제외(collect 확장 후속). 사용자 선호는 도구 메모리(`prompting-feedback-preference`) 저장.
- **TODO.md 손상 복구**: #117 커밋에 혼입 — 직전 세션의 섹션 이동 파이썬 스크립트가 `text.index("## Blocked")`로 검색해 6행 안내문 속 문자열(`` `## Blocked`, `## Done`) ``)에 오매칭 → METH-117 위 전체가 중복되고 Done의 METH-117 헤딩·필드가 유실. 정본 재작성으로 복구(칸반 5헤더 정합 검증·중복 0). 라이브 파일이라 다운스트림 무영향. **교훈(friction 기록): 라이브 파일 섹션 조작은 문자열 index() 금지 — `^## ` 행 시작 앵커 정규식으로.**

## 다음 구체 행동

1. 이 PR(`chore/backlog-meth-118-prompt-coaching` → main) 머지 — TODO(복구+118)·라이브 파일만, Class A.
2. METH-118 착수는 Backlog→Ready 승격 시. 진입점: `cmd_observe`/`render_observation`(prompt_patterns 확장)·`cmd_wrap`(리포트 재생성 훅)·`cmd_boot`(헤드라인).
3. 기존 후속 후보 유지: graph.json outbox/collect 노드·invest-ops restricted 부여·pre-push 훅 sync 면제(3회 재발)·grooman sync(타 호스트).

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.
