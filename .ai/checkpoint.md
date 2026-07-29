# Checkpoint — 2026-07-29 (METH-128 구현 — 트리아지 마지막 항목)

> ✅ 캡슐 첫 수거분을 지침 22 v2·지침 08 §7로 반영 — **캡슐 루프 풀 사이클 완결**. branch `docs/meth-128-guide-22-capsule`, PR 대기. 머지·전파 시 트리아지 12/12 전량 종결.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `docs/meth-128-guide-22-capsule` (base=main, branch-first)

## 방금 한 것

- **지침 22 v2** — 캡슐(`icons-invest__2026-07-29_guide-22-audit-gaps`) 15건 분배 반영:
  - 불변규율 3→5개: ④ 텍스트본 *파일*=유일 소스(대화본 빌드 금지·충돌 시 파일 우선·빌드 직전 재확인) ⑤ 안정 슬라이드 ID(순번은 렌더 시 계산 — 재번호 연쇄 8회+ 계보)
  - P0 게이트: 흡수 대상 원자료 전수 목록 확정(빌드 후 역방향 흡수 방지) / P3 게이트: 패치마다 리드백 필수(무증상 실패)
  - §4.2 패널 결함 해소 루프: 치명 결함 TODO 승격 + 다음 패널이 해소 여부 명시 판정(1차 치명 5건 중 2건만 해소된 실측)
  - §7 함정 체크 8종 추가: 무증상 빌드 실패·차트 글리프·검산 전 셰이프·인덱스 하드코딩 금지·에셋 문맥 소실·이미지 소싱 2단·대용량 백그라운드
- **지침 08 §7 신설(교차)** — 장시간 에이전트 스톨 감지: mtime/size 정체 판정 → TaskStop 후 동기 재실행, 지침 07 no-progress를 백그라운드에도 적용(48분 단일 최대 friction 계보). 격상 이력 §8로 재번호.
- 반영 완료 캡슐 `_inbox`에서 삭제(git rm) — **원장은 유지**라 재수거 안 됨(inbox README 규칙대로).

## 다음 구체 행동

1. 이 PR(`docs/meth-128-guide-22-capsule` → main) 머지 → sync-all 전파(지침 22·08 shared) → METH-128 Done → **트리아지 12/12 전량 종결 보고**.
2. 이후 방법론 백로그: METH-113(retrofit)만 잔류. 별도 트랙: RFC-003 관찰(8/12경)·repo 과제 5건·grooman sync.
3. 다음 달 루프 운용: 다운스트림 캡슐 발신 축적 → boot 미수거 경고 시 collect → Catalog Review에서 트리아지 — 이번에 실증된 사이클 그대로.

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.
