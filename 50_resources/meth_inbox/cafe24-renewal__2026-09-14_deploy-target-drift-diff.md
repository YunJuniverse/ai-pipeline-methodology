---
id: cafe24-renewal__2026-09-14_deploy-target-drift-diff
origin_repo: cafe24-renewal
type: pattern
target: "catalog"
refs:
  - "6389ce2"
  - "32bb7d5"
  - "20_guides/30_동시_세션_git_격리.md"
friction_ref: 2026-09-07_alpha-review-widgets-empty
created: 2026-09-14T07:06:45Z
---

## 제안
배포 대상(원격 서버·CMS·테마 저장소)에 우리 외 쓰기 주체(서드파티 앱·타 팀)가 있으면 '로컬=정본' push 배포가 남의 변경을 조용히 덮는다. 업로드 전 원격본 다운로드 diff(또는 mtime·해시 비교)로 드리프트를 감지하고, 드리프트가 있으면 로컬로 병합 후 배포하는 절차 제안(지침 30 인접)

## 근거
- 서드파티 앱이 '설치'를 서버 파일 2개 직접 수정으로 수행 — 로컬 저장소엔 흔적 0. 다음 업로드였다면 앱 설치분 전량 소실
- 표본 6파일만 대조해 '1개 파일'로 오보고 → 템플릿 전수+mtime 으로 2개·설치 시각까지 특정

