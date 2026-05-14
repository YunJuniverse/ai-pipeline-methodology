---
id: RFC-001
title: methodology status에 upstream commit 격차 검출 추가
status: accepted
proposed_by: claude-sonnet-4-6
proposed_at: 2026-05-12
target_class: A
supersedes: null
relates_to: [MP-001]
---

# RFC-001 — status에 upstream commit 격차 검출 추가

## Context

본 저장소가 v3.1 → v3.2 로 진화하는 과정에서, 외부 적용 프로젝트(icons/gamblescan/talmocom) 세 곳 모두 `methodology status`가 "최신 ✓"으로 표시되었지만 실제로는 옛 v3.1 commit이라 *MANIFEST 확장·새 디렉터리·구조 재편*이 빠져 있었다.

근본 원인: `cmd_status`가 *메이저 버전 문자열*(`v3.1` vs `v3.2`)만 비교. 같은 버전 안에서의 *upstream commit 격차*는 검출하지 않는다.

기록: `70_meta/catalog/_pending/MP-001_*.md`, `70_meta/observations/2026-05-12_*.md` §F-001.

## Proposal

`cmd_status`에 다음 로직 추가:

1. `.methodology-version`에서 `upstream_commit` 추출
2. 현재 본 저장소의 `upstream_commit()` 결과(=git short SHA)와 비교
3. *같은 버전*이고 *commit이 다르면*: "최신 ✓" 대신 `behind upstream: <local>..<upstream>` 표시
4. 출력 라인 한 줄 추가 + sync 호출 권유 메시지

영향: 단일 함수 수정. CLI 출력 형식 1줄 추가. 호환성 영향 없음 (출력 기반 자동화는 없는 것으로 가정).

## Alternatives Considered

| 대안 | 트레이드오프 |
|---|---|
| **(채택)** commit hash 비교 | 가볍고 정확. 단, *의미 있는 변경인지*는 모름 — 작은 typo만 있어도 "behind" 표시. |
| sync dry-run 자동 실행하여 *실측 변경 건수* 표시 | 가장 정확하지만 status 호출 비용이 큼 (수 초). 빈번한 status 호출에 부적합. |
| MANIFEST 의 모든 shared_paths 의 mtime/hash 비교 | 정확하나 복잡도 큼. 첫 단계에 과함. |

채택한 대안은 *가장 단순한 신호 추가* — 사용자가 "behind" 보면 dry-run으로 실측 확인하는 흐름 유도.

## Risks

- **출력 형식 변경** — status 출력을 파싱하는 외부 스크립트가 깨질 수 있음. *현재 없는 것으로 가정*. 깨지면 ADR로 후속.
- **upstream_commit이 unknown인 경우** — 옛 .methodology-version에 필드가 없으면 표시 skip (graceful fallback).
- **사용자가 origin과 사이가 안 맞는 환경** — 본 저장소가 detached HEAD 등인 경우 upstream_commit() 결과가 신뢰성 떨어짐. *최선 노력*으로 처리.

## Rollout

1. 본 RFC 머지 후 `cmd_status` 수정 — 단일 커밋
2. 본 저장소(`/Users/hayden/methodology`)에서 동작 검증 — 같은 v3.2이라도 commit 진척되면 "behind"
3. 다음 외부 프로젝트 sync 시점에 자동 효과 — 별도 마이그레이션 불필요
4. 검증 통과하면 본 RFC `status: accepted` (이미 accepted로 기록)

## Open Questions

- "behind"를 *몇 commit 차이까지* 무시할지 — 현재는 *임의의 차이*에 표시. 1~2 commit 정도는 noise라 무시할 옵션은 추후.
- ADR 후속 필요성 — 본 변경은 단순 출력 추가라 Class A. ADR 없이도 가능. 향후 *비교 알고리즘 변경* 시점에 ADR 신설.
