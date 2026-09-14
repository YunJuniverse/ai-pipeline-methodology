---
id: icons__2026-09-11_rebase-docs-ours-drops-checkpoint
origin_repo: icons
type: tool-change
target: "tool/land"
refs:
  - "https://github.com/icons-hq/icons/pull/913"
  - "https://github.com/icons-hq/icons/pull/934"
friction_ref: null
created: 2026-09-11T03:23:00Z
---

## 제안
리베이스 충돌에서 라이브 파일을 일괄 ours 로 풀면(리베이스 중 ours 는 upstream) 내 checkpoint 와 HANDOFF 줄이 사라지고 그대로 ship 하면 wrap 이 4/4 미달로 선다. 규칙: HANDOFF 줄은 재삽입, checkpoint 는 치환이 아니라 맨 위 prepend 로만(치환 대상 문자열이 사라져 있을 수 있다). land 가 리베이스 후 라이브 파일 sha 를 wrap-state 와 대조해 유실을 경고하는 것을 제안.

## 근거
- 2026-09-09 docs PR 2건에서 checkpoint 치환 실패 → wrap 실패 → prepend 로 재시도

