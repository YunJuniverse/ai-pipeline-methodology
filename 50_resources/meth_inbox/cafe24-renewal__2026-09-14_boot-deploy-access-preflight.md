---
id: cafe24-renewal__2026-09-14_boot-deploy-access-preflight
origin_repo: cafe24-renewal
type: tool-change
target: "tool/boot"
refs:
  - "c62ae43"
  - "6ecb270"
  - "20_guides/24_착수_게이트.md"
friction_ref: 2026-09-14_todo482-tdbar-harness-verify-sftp-blocked
created: 2026-09-14T07:08:40Z
---

## 제안
gitignore 된 배포 접속 정보 파일이 새 체크아웃·원격 세션에 없어, 수정·검증을 끝낸 뒤에야 배포가 막히는 일이 월 4회 재발. boot 에 프로젝트가 선언한 배포 접속 파일의 존재 검사(내용은 읽지 않음)를 넣어 착수 시점에 경고하는 preflight 제안(지침 24 인접)

## 근거
- 배포 접속 파일 부재로 배포 차단 4회 — 마지막은 하네스 검증까지 끝낸 수정이 반나절 미배포
- 해당 파일은 비밀이라 AI 가 재생성 불가 — 사용자 개입이 필요하므로 작업 시작 전에 알려야 비용이 최소

