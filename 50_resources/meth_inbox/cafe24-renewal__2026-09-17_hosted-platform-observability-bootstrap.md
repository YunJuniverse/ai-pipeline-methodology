---
id: cafe24-renewal__2026-09-17_hosted-platform-observability-bootstrap
origin_repo: cafe24-renewal
type: pattern
target: "skeleton/hosted-platform-customization"
refs:
  - "40_dev/research/2026-09-17_cafe24-renewal-retrospective.md"
  - "20_constraints/cafe24-limits.md"
friction_ref: null
created: 2026-09-17T08:38:25Z
---

## 제안
호스팅 플랫폼(SaaS 쇼핑몰·CMS·테마) 위 커스터마이즈 프로젝트는 기능 착수 전 첫 주에 '관측 인프라'를 먼저 세운다: ①렌더 파이프라인(번들러·optimizer가 무엇을 합치고 지우는지) ②캐시 계층과 반영 시간 실측 ③서드파티 앱 점유·쓰기 인벤토리 ④자격증명 없는 배포 경로 ⑤렌더 기반 검증 스크립트 세트. 플랫폼 선정 시에도 '관측·통제 가능성'을 평가 기준에 넣는다.

## 근거
- 마찰 204건·4,684분 중 약 49%가 측정 오판·진단 순서·캐시 불확실성 — 고치는 비용보다 '무엇이 실렸는지 확정'하는 비용이 컸다
- 캐시 계층·전파 시간을 컷오버 후에야 실측(타임딜 TODO 11개, 반영 10분+→전용 프로브로 3~5초)

