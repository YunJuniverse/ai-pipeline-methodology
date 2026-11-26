# checkpoint 세션 절 아카이브 — 2026-11-26 rotate (1절)

## 2026-11-09 · meth-151-decisions

### 방금 한 것
- 사용자가 전수조사 판단 7지점(METH-150) 전부 권고안 채택 → **ADR-006**. 반영(METH-151, 브랜치 `chore/meth-151-decisions`): D1 checkpoint 절 모델(이 파일이 첫 적용) · D2 land 머지 기록 직접 커밋 · D3 같은 날 관찰로그 갱신 · D4 공유 가드 미추적 신규만(+`-uall` 결함) · D5 `required_checks` · D6 C-004~006.
- land 가 이미 머지된 PR 은 Class 판정을 건너뛰게 함 — Class C PR 을 사람이 머지한 뒤에도 기록(D2)이 돌도록.
- METH-149 는 #185 로 main 도달(`86a11ed7`).

### 다음 구체 행동
1. ship → land: Class C 라 자동 머지 거부가 정상(T8 실증). 사용자 머지 후 land 재실행 → METH-151 이 Done 으로 자동 이동하면 D2 실증.
2. D7 전파: ai-icons TODO.md 29행 헤더 선복구 → `sync-all --apply`(Personal) + ICONS 루트 개별 sync → origin 대조.

### 막힌 것
- 없음(머지는 사람 몫).
