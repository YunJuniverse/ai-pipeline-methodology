---
id: P-007
title: "다른 쓰기 주체가 있는 배포 대상은 업로드 전 원격본 diff 로 드리프트를 감지한다"
domain: cache-hostile-platform
status: pending
source_observations:
  - cafe24-renewal__2026-09-14_deploy-target-drift-diff (capsule)
signature: "SFTP.*덮어씀|원격.*로컬.*불일치|서드파티.*서버 파일.*수정|mtime.*diff"
created: 2026-09-15
last_seen: 2026-09-14
promotion_rule: "Promote to active Catalog after N>=2 observations or explicit human approval."
---

## 패턴 (Pattern)

배포 대상(원격 서버·CMS·테마 저장소)에 **우리 외 쓰기 주체**(서드파티 앱·타 팀)가 있으면 «로컬 = 정본» push 배포가 남의 변경을 조용히 덮는다. 업로드 전 **원격본 다운로드 diff(또는 mtime·해시 비교)** 로 드리프트를 감지하고, 드리프트가 있으면 로컬로 병합한 뒤 배포한다.

## 근거 (Evidence)

서드파티 앱이 «설치»를 서버 파일 2개 직접 수정으로 수행 — 로컬 저장소엔 흔적 0. 다음 업로드였다면 앱 설치분 전량 소실. 표본 6파일만 대조해 «1개 파일»로 오보고 → 템플릿 전수 + mtime 으로 2개·설치 시각까지 특정(cafe24-renewal).

## 안티패턴 (Anti-Pattern)

- 로컬 저장소만 보고 «변경 없음»으로 판단.
- 표본 몇 파일 대조로 전수 판정(지침 23 §2-6 부재 판정의 관측 조건).

## 관련 자료

- P-005(캐시 적대 플랫폼 표시 게이트) 와 같은 계열 · 지침 30 §3(배포 링크 파일) 인접.

## 승급 조건

타 플랫폼(다른 SaaS·공유 서버)에서 재현(N≥2)되면 active 등재.
