---
id: P-011
title: "repo 밖 스프레드시트 정본을 브라우저로 편집할 때는 다운로드 diff 로 끝낸다"
domain: external-sot
status: pending
source_observations:
  - drip-chat-planning__2026-10-29_tier-names-sheet-redo
  - drip-chat-planning__2026-11-02_closed-beta-rolling-access-30k
  - drip-chat-planning__2026-10-29_tier-names-nobility-guild
  - lifeManager__2026-10-23_n2n-sheet-feed
  - lifeManager__2026-10-27_n2n-sheet-last4-col
signature: "Google Sheet|스프레드시트|이름 상자|Name box|IME.*첫 글자|자동완성|IMPORTRANGE|셀 입력|열 삽입"
created: 2026-11-09
last_seen: 2026-11-06
promotion_rule: "2개 repo 재현(250분) — 승급 조건 충족. 사람 승인 후 active 등재. 절차는 standing SOP 로 이미 배포."
---

## 패턴 (Pattern)

편집 커넥터 없이 브라우저 UI 로 시트를 고치면 **오류 없이 값을 잃는다** — 한글 IME 첫 글자 유실 · 자동완성 끼어듦 · 이름 상자 포커스 실패로 A1 에 입력 · `%` 이중 서식 · 열 삽입이 체크박스·조건부 규칙을 복제 · 동시 편집으로 행이 밀림.

절차는 `00_briefs/standing/SOP_external-sheet-edit.md`. 핵심: 편집 전 수정 시각 확인 → 입력 → **xlsx 내려받아 «바뀐 칸 수 = 의도한 칸 수, 그 밖 0칸»** 대조(지침 23 §2-8).

## 근거 (Evidence)

drip-chat-planning 12건 155분(마찰의 53%, repeat_of 4회 — 동시 편집 충돌 30여 칸 미반영 포함) · lifeManager 6건 95분. 입력 절차가 두 repo 모두 checkpoint 의 «다음 사람에게» 메모에만 있었다.
