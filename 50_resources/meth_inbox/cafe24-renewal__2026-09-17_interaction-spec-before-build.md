---
id: cafe24-renewal__2026-09-17_interaction-spec-before-build
origin_repo: cafe24-renewal
type: guide-update
target: "catalog"
refs:
  - "40_dev/research/2026-09-17_cafe24-renewal-retrospective.md"
friction_ref: 2026-08-21_story2-flow-boundary-tiling
created: 2026-09-17T08:38:27Z
---

## 제안
정적 디자인 도구(Figma 등)에 없는 스크롤 고정·등장 타이밍·전환 연출은 착수 전에 수치 스펙(트리거 위치, 고정·해제 좌표, 지속시간, 겹침 허용 여부)을 합의하고, 검증은 스크롤 N px·프레임 단위 기계 스캔으로 한다. 값 조정으로 못 없애는 구조적 부작용은 되돌리고 선택지를 수치와 함께 제시한다.

## 근거
- 스크롤·고정·애니메이션 마찰 20건 638분(14%) — 고정 레이어 튐 75분, 핀 지연 부작용 60분, 잔상 45분
- 5px 스크롤 스캔·40ms 겹침 스캔 도입 후 수렴

