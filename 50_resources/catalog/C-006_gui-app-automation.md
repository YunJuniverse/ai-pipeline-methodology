---
id: C-006
title: "GUI 네이티브 앱 자동화는 타임아웃을 실패로 보지 않고 결과를 재조회한다"
domain: design-automation
status: active
seen_in:
  - ai-icons__2026-10-16_workorder-zh-cells
  - ai-icons__2026-10-21_n2n-v8-song-copy-angle
  - ai-icons__2026-10-19_loop138-native-preview-final-v008
  - invest-ops (Illustrator jsx 10분)
signature: "AppleEvent|-1712|-2741|osacompile|Illustrator.*(응답 없음|타임아웃|바쁨)|jsx"
created: 2026-11-09
last_hit: 2026-10-30
promoted_from: P-013
verified_with:
  - claude-opus-5-5
deps_implicated: []
---

> **승급 (2026-11-09, METH-151)**: P-013 → C-006. 2개 이상 repo 재현 — 사람 승인 methodology:ADR-006 D6.

## 패턴 (Pattern)

1. AppleEvent 타임아웃(-1712)·앱 바쁨(-2741)은 **명령이 실패했다는 뜻이 아니다** — 앱이 아직 처리 중일 수 있다. 결과(문서 상태·내보낸 파일)를 **재조회**하고, 없을 때만 10초 간격 3회 재시도.
2. 화면 잠금·GUI 세션 부재에서는 네이티브 미리보기 검증이 불가 — 자율 루프 기획에서 GUI 의존 검증을 별도 단계로 두고 잠금 시 대기·보고(지침 29).
3. `where` 는 원인 앵커 `illustrator-appleevent-timeout` 으로 통일(지침 03 §5.2) — 같은 원인이 7종 문장으로 흩어져 한 번도 승급 집계되지 않았다.

## 근거 (Evidence)

ai-icons C2 약 300분 25건(타임아웃 계열 7건 59분 · 네이티브 미리보기 검증 154분 · 좌표·그라데이션·잠금 96분), invest-ops Illustrator jsx 10분.
