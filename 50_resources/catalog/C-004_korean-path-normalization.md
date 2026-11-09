---
id: C-004
title: "한글 경로·파일명은 NFD/NFC 정규화와 셸 인용을 먼저 의심한다"
domain: tooling
status: active
seen_in:
  - invest-ops__2026-09-07_zenith-namecard-roster
  - invest-ops__2026-10-20_zenith-namecard-order-package
  - invest-ops__2026-10-23_kopan-master-dd
  - ai-icons__2026-10-15_workorder-item-reclassify
  - icons-ax PR #102 (unzip 한글 파일명 정지)
  - methodology METH-145 (core.quotePath)
signature: "한글.*(경로|파일명)|NFD|NFC|unzip.*한글|quotePath|octal|자모 분리|glob.*안 맞"
created: 2026-11-09
last_hit: 2026-10-23
promoted_from: P-010
verified_with:
  - claude-opus-5-5
deps_implicated: []
---

> **승급 (2026-11-09, METH-151)**: P-010 → C-004. 2개 이상 repo 재현 — 사람 승인 methodology:ADR-006 D6.

## 패턴 (Pattern)

macOS 파일시스템·zip·git 은 한글 파일명을 **NFD(자모 분리)** 로 돌려주는 경우가 있고, 셸에 타이핑한 문자열은 **NFC** 다. 겉보기엔 같은 이름인데 `grep`·`sed`·`test -f`·glob 이 조용히 실패한다.

1. 한글 경로가 «없다»고 나오면 **정규화 차이부터** 확인한다 — `python3 -c "import unicodedata,sys; print(unicodedata.normalize('NFC', sys.argv[1]))"` 또는 `ls | grep` 글로브로 실제 바이트를 잡는다.
2. git 출력은 `-c core.quotePath=false` 로 본다(octal 이스케이프 grep 오탐).
3. 배포용 zip·인계 묶음은 **내부 경로를 ASCII 로** 짓는다 — macOS unzip·구형 윈도우가 한글 파일명에서 깨지거나 멈춘다.
4. 스크립트는 경로를 비교하기 전에 `unicodedata.normalize("NFC", …)` 로 맞춘다.

## 근거 (Evidence)

invest-ops 3회 18분(repeat_of 모두 null — 매번 재발견) · ai-icons NFD 재분류 · icons-ax 직원 배포 가이드 리허설에서 unzip 정지 · 상류 METH-145 quotePath 판정 구멍. 4개 repo, 우회책이 매번 새로 발견됐다.
