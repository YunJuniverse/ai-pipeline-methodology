---
id: cafe24-renewal__2026-09-17_friction-phase-split
origin_repo: cafe24-renewal
type: tool-change
target: "tool/observe"
refs:
  - "40_dev/research/2026-09-17_cafe24-renewal-retrospective.md"
  - "50_resources/ai_observations/"
friction_ref: null
created: 2026-09-17T08:38:26Z
---

## 제안
observe --friction 에 phase 필드(diagnose|fix|deploy|verify|communicate)를 추가 제안. 회고 집계에서 진단·확정 비용이 수정 비용을 넘었으나 현 스키마로는 키워드 추정만 가능했다. phase 가 있으면 '관측 부채'(진단 비중)를 프로젝트 간 비교하고 관측 인프라 투자 시점을 판단할 수 있다.

## 근거
- 204건을 키워드로 재분류해야 했고 한 건이 여러 성격이면 첫 매칭으로 떨어지는 한계를 문서에 명시

