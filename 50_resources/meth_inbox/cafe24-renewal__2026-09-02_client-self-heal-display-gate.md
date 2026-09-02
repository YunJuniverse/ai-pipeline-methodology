---
id: cafe24-renewal__2026-09-02_client-self-heal-display-gate
origin_repo: cafe24-renewal
type: pattern
target: "skeleton/cafe24-skin"
refs:
  - "3ded436"
  - "73acbec"
  - "skin-download/skin184/24d/add_part/js/ts-plp-timedeal.js"
  - "40_dev/snapshots/2026-09-02_timedeal-logic-audit.md"
friction_ref: 2026-09-02_verdict-majority-symmetric
created: 2026-09-02T06:38:35Z
---

## 제안
캐시 계층을 못 고치는 플랫폼에서 시간 민감 UI(타임딜류)를 정확히 표시하는 클라이언트 자가치유 게이트 패턴: ①원본 판정이 로컬 문서를 항상 덮어씀 ②첫 판정도 2/3 다수결(방향 비대칭 금지 — 낡은 사본은 양방향으로 거짓말) ③재검증 루프는 연속 2회 합의+탭 복귀 리셋 ④예약은 판정마다 재무장(원샷 가드 금지) ⑤전환은 전부 가역 토글 ⑥마크업 재료가 없는 사본에는 원본 값으로 되살리기 ⑦실패는 fail-open(매출 차단이 최악)

## 근거
- 부정 판정만 합의받던 비대칭 규칙이 반나절 만에 역효과(옛 기간 사본 'run' 복권이 시작 전 딜을 켬) — 방향 무관 다수결로 교체

