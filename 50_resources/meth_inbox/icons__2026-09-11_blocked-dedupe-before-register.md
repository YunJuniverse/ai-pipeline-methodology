---
id: icons__2026-09-11_blocked-dedupe-before-register
origin_repo: icons
type: guide-update
target: "guide-live-files"
refs:
  - "https://github.com/icons-hq/icons/pull/921"
  - "40_dev/snapshots/2026-08-24_구매실적-구매규칙-PM판정요청.md"
friction_ref: null
created: 2026-09-11T03:23:00Z
---

## 제안
외부 게이트를 TODO Blocked 에 올리기 전에 기존 Blocked 와 HANDOFF Blockers 를 grep 해 같은 건이 PM 판정과 함께 이미 있는지 확인한다(CI 결제 건을 판정 있는 08-20 항목이 있는데도 중복 등재해 PM 에게 다시 물음). 판정 요청서는 뒤의 ADR 이 같은 결론을 세우면 스스로 닫힌다 — 월 1회 Blocked 를 후속 결정과 대조해 stale 항목을 종결(구매규칙 요청서가 ADR-0025 부칙 2 로 16일간 stale).

## 근거
- (refs 참조 — 원문 정본은 이 repo)

