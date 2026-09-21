---
id: C-003
title: "배포 자격증명이 로컬 파일에만 있으면 새 체크아웃·클라우드 세션에서 배포가 막힌다 — 머지=배포 CI 경로"
domain: deployment
status: active
seen_in:
  - 2026-08-22
  - 2026-09-02
  - 2026-09-14
  - 2026-09-17
signature: "배포 접속|자격증명.*없|SFTP.*불가|deploy.*credential|로컬에만.*시크릿|업로드.*exit 0"
verified_with:
  - claude-opus-5
deps_implicated: []
created: 2026-09-21
last_hit: 2026-09-17
---

> **승급 (2026-09-21, METH-148)**: 같은 원인이 4개 날짜에 재현(cafe24-renewal) — seen_in N≥2 로 active. 5회차 캡슐
> `boot-deploy-access-preflight` 도 같은 원인이었고 상류는 그때 **증상 경고**(boot `required_local_files`)만 넣었다.
> 이 엔트리는 **근본 해법**이다.

## 증상 (Symptom)

- 새 체크아웃·클라우드 세션·모바일에서 수정과 검증을 끝낸 뒤에야 배포가 막힌다(반나절 미배포 실례).
- 클라우드 세션은 HTTP 프록시 뒤라 SFTP 자체가 불가능하다.
- 업로드 스크립트가 실패해도 exit 0 이라 «배포됐다»고 믿는다.

## 근본 원인 (Root Cause)

배포 자격증명이 gitignore 된 **로컬 파일에만** 있다. 비밀이라 AI 가 재생성할 수 없고, 로컬이 없는 모든 실행 환경에서 배포 경로가 끊긴다.

## 솔루션 (Solution)

**`main 머지 = 배포` CI 경로**를 두고 시크릿은 **CI 저장소에만** 둔다. 로컬 즉시 배포와 공존한다(멱등).

가드 6종 — 없으면 CI 배포가 사고 증폭기가 된다:
1. **변경분만** 업로드(전체 재업로드 금지)
2. **N개 초과 차단** — 수동 `force` 로만 통과
3. **삭제는 반영하지 않는다**(원격 파일 삭제는 사람)
4. **부분 실패 시 비0 종료** — 실패해도 exit 0 이던 결함이 CI 도입 때 드러났다(지침 23 §1-1·§1-4)
5. **PR 트리거에서 시크릿 비노출** — 포크·PR 워크플로에 시크릿이 들어가지 않게 배포 잡은 main push 에서만
6. **수동 재실행·dry_run** 입력

배포 대상에 다른 쓰기 주체가 있으면 P-007(업로드 전 원격본 diff)을 함께 건다.

## 채택 절차 — Class B

다운스트림에서 채택하면 `.github/workflows/` 변경이라 **Class B** 다(land 가 자동 머지를 거부한다). 채택 PR 에 결정 근거 · 영향 범위 · 롤백 계획 · **시크릿 리스크** 4항을 적는다. 상류는 패턴만 두고 워크플로 파일은 배포하지 않는다 — 배포 대상이 repo 마다 다르다.

## 안티패턴 (Anti-Pattern)

- 자격증명 파일을 채팅으로 받아 로컬에 다시 만든다(비밀 노출 경로가 늘어난다).
- CI 배포에 가드 없이 전체 업로드 — 한 번의 잘못된 머지가 운영 전체를 덮는다.
- boot 경고(`required_local_files`)만 두고 끝낸다 — 증상 알림이지 해법이 아니다.

## 관련 자료

- 출처 캡슐: cafe24-renewal `merge-is-deploy-ci-path`(2026-09-17, 결정 기록 `40_dev/decisions/2026-09-17_github-actions-skin-deploy.md`) · `boot-deploy-access-preflight`(2026-09-14)
- CLAUDE.md §3 Class B · ADR-004(land)
