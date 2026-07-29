---
doc_id: meth-inbox-readme
title: 캡슐 _inbox — 수거함·트리아지 (상류 전용)
version: v1.0.0
status: active
last_updated: 2026-07-29
ai_relevance: schema
---

# meth_inbox (캡슐 수거함 — 상류 전용, METH-117)

> `methodology collect --apply`가 다운스트림 outbox 캡슐을 여기로 적재한다.
> 파일명 `<origin_repo>__<YYYY-MM-DD_slug>.md`. 이 디렉터리는 **상류 전용** — shared/init 어디에도 전파되지 않는다.

## 원장 (_ledger.json)

- 수거된 캡슐 id의 유일한 정본. 다운스트림 캡슐에는 아무 표시도 하지 않는다(무변경 원칙).
- 재수거 시 원장에 있는 id는 자동 skip — 같은 제안이 두 번 들어오지 않는다.

## 트리아지 — 사람 (주기: Catalog Review 시간 합류)

캡슐마다 첫 판정을 셋 중 하나로:

| 판정 | 의미 | 처리 |
|---|---|---|
| **유효** | 지금도 반영 가치 있음 | 목적지 분배: TODO 백로그 / `catalog/_pending/P-NNN` / 지침 보강 PR / skeleton |
| **이미 반영** | 다른 경로로 해소됨 | 캡슐 삭제(원장은 유지 — 재수거 방지) |
| **만료** | 맥락 변경으로 무의미(stale) | 캡슐 삭제(원장 유지). 판단 근거 한 줄을 커밋 메시지에 |

- 처리(분배·삭제) 후 커밋은 ship으로. **자동 승급 절대 없음**(백서 §8-2) — collect·thinktank는 적재·집계·마킹까지만.
- `thinktank`가 이 디렉터리를 target별로 집계해 교차-repo 중복 제안(`CROSS-REPO`)을 마킹한다 — 우선 검토 신호.
