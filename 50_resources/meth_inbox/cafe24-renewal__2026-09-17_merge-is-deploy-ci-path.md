---
id: cafe24-renewal__2026-09-17_merge-is-deploy-ci-path
origin_repo: cafe24-renewal
type: pattern
target: "catalog"
refs:
  - "8ed0150"
  - "https://github.com/YunJuniverse/cafe24-renewal/pull/22"
  - "40_dev/decisions/2026-09-17_github-actions-skin-deploy.md"
friction_ref: 2026-09-17_github-actions-skin-deploy
created: 2026-09-17T08:38:25Z
---

## 제안
배포 자격증명이 로컬 파일에만 있으면 클라우드·모바일·새 체크아웃 세션에서 배포가 막힌다. 'main 머지 = 배포' CI 경로를 두고 시크릿은 CI 저장소에만 둔다. 가드: 변경분만 업로드, N개 초과 차단(수동 force), 삭제 미반영, 부분 실패 시 비0 종료, PR 트리거에서 시크릿 비노출, 수동 재실행·dry_run. 로컬 즉시 배포와 공존(멱등).

## 근거
- 자격증명 부재로 배포 지연·미배포 재발 4회(08-22, 09-02, 09-14, 09-17) — 클라우드 세션은 HTTP 프록시 뒤라 SFTP 자체가 불가
- 업로드 스크립트가 실패해도 exit 0 이던 결함을 CI 도입 때 발견

