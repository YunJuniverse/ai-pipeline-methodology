# Checkpoint — 2026-07-29 (METH-117 설계 확정 — 캡슐 outbox + 수동 일괄 수거)

> ✅ 설계 확정 완료 — 사용자와 시각화·문답으로 초안(pull 스캔)을 캡슐 outbox 안으로 교체, 리스크 완화책 포함 AC 전면 재작성. branch `chore/meth-117-capsule-outbox-design`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `chore/meth-117-capsule-outbox-design` (base=main 469ad17, branch-first)

## 방금 한 것 (이번 세션, 07-28~29 연속 대화)

- 07-28: 역방향 루프 갭 분석 → METH-117 백로그 등록(#113 머지됨). 이후 #112(METH-116 지침 22)도 머지 확인 — **sync-all 전파는 미실행(잔여)**.
- 07-29: 사용자 요청으로 역방향 루프를 SVG 2장으로 시각화(현행 구조 → 조정안). 설계 문답:
  - 사용자 제안: 방법론 repo로 자동 직행 대신 **다운스트림에 캡슐(제안+근거 ref) 적재 공간을 두고 상류가 나중에 수동 일괄 수거**.
  - 캡슐화 정의 확인: **1 제안 = 1 캡슐 = 1 파일**(통합·혼합 금지) — catalog 1문제 1엔트리와 동일 granularity.
  - 리스크 6종 검토: 수거 잊음(최대)·트리아지 병목·sensitive 반경·stale·원격 전제·결과 피드백 부재. 앞 5종 완화책 합의, 결과 피드백은 v1 제외.
  - 사용자 "확정" → `TODO.md` METH-117 AC 전면 교체(캡슐 스키마·작성 트리거·collect 명령·boot/sync-all 잔량 가시성·sensitive/sync 제외·트리아지 정형화·§8-2 유지).

## 다음 구체 행동

1. 이 PR(`chore/meth-117-capsule-outbox-design` → main) 머지 — TODO·라이브 파일만, Class A.
2. **잔여: METH-116(지침 22·스켈레톤 ir-deck-build) sync-all 다운스트림 전파** — #112 머지됨, 전파만 남음. 다음 세션 착수 후보 1순위.
3. METH-117 구현 착수는 사람이 Backlog→Ready 승격 시. 진입점: `60_tools/methodology.py` `observation_files()`(L756)·`cmd_thinktank()`(L763)·`cmd_sync_all()`(L1491)·boot·ship sensitive 스캔. 구현 시 catalog `_README.md` §3 파이프라인 문구에 캡슐 트랙 추가 잊지 말 것.

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765 서빙 중.
