# Checkpoint — [PROJECT_NAME] 초기 부팅

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: (next-session-will-fill)
- Tool: (next-session-will-fill)
- Host: (next-session-will-fill)
- Workspace: repository root

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` as the immediate handoff.
4. Start from the first actionable item in "다음 사람에게".

## 방금 한 것 (정확히)

- 본 프로젝트에 방법론 적용 ([YYYY-MM-DD]).
- L0 이식성 코어(`.ai/`) 생성 — `context.json`, `schema/`, `adapters/`.
- 70_meta 격리 보장 — 외부 주입 안 됨.

## 다음 사람에게 (구체적 첫 행동)

1. `.ai/context.json` 의 `project.domain` 을 실제 값으로 채울 것 (예: `webapp-next`, `data-pipeline`).
2. `HANDOFF.md` 의 *Current Focus* 를 본 프로젝트의 실제 첫 작업으로 갱신.
3. `TODO.md` 에 첫 `<PREFIX>-001` 항목 추가 (acceptance criteria 포함).
4. 첫 작업이 끝나면 본 checkpoint 를 갱신 — 형식: `10_foundation/WHITEPAPER.md` §2-2.

## 막혔던 지점 / 시도해봤지만 안 된 것

(없음 — 초기 부팅 단계)

## 미해결 결정사항 (Open Questions)

- 도메인 식별자 (`project.domain`) — `50_resources/skeletons/_README.md` §4 컨벤션 참조.
- 적용할 Skeleton 도메인 (있으면).

## 환경 메모

- 본 프로젝트는 방법론 [PROJECT_MODE] 모드로 시작됨.
- `.methodology-version` 의 upstream commit 을 git 으로 추적.
