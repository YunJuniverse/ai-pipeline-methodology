---
id: icons__2026-09-11_observe-friction-pipe-in-text
origin_repo: icons
type: tool-change
target: "tool/observe"
refs:
  - "50_resources/ai_observations/2026-09-09_button-registry-me-tabs.md"
friction_ref: null
created: 2026-09-11T03:22:35Z
---

## 제안
observe friction 인자는 where, cost, resolution, repeat_of 를 세로줄로 가르는데 본문에 세로줄이 들어가면 형식 오류로 관찰이 안 만들어지고 뒤의 wrap 이 실패한다. 마지막 3개 구분자 기준 rsplit 하거나 필드별 분리 옵션 제안.

## 근거
- 2026-09-09 friction 형식 오류 1회(grep 인용문 안의 세로줄)

