# Checkpoint — 2026-08-07 (CI validate 복구 + 자동머지/실험모드/자율주행 설계 착수)

> ⚠️ **CI가 #136·#137·#138 세 번 연속 main에서 red였다** — METH-132로 복구(로컬 린트 0 오류). 자동 머지 설계의 전제였다.
> 다음: METH-133/134/135 설계 — 사용자 결정 2건(자동 머지 범위·실험 모드 경계) 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `fix/ci-observation-lint-20260807` (base=main, branch-first — #138 머지 후 main에서 새로 분기)

## 방금 한 것

1. **캡슐 수거 종결**(#138 머지됨) — 15건 `_inbox` 적재·원장 16건·thinktank 재집계. 트리아지는 METH-131(Blocked).
2. **METH-132 CI 복구** — `gh run list --branch main`로 #136~#138 전부 `failure` 확인. 원인은 observation lint의 `repeat_of` 형식 위반 6건(5월 레거시 `70_meta/observations/` 5건 + `50_resources/ai_observations/2026-07-24_sync-all-meth-115-remainder.md` 1건). 자유서술을 `resolution`으로 옮기고 `repeat_of`는 허용형(session_id·null)으로. 로컬 전수 린트 exit=0.
3. 사용자 신규 요청 3건 조사 — 아래.

## 사용자 요청 3건 (설계 대기)

- **METH-133 자동 머지**: ship이 머지까지. 조사 결과 — main **브랜치 보호 없음**(즉시 머지 가능), `.github/workflows/methodology-auto-merge.yml` **이미 존재**(`auto-merge` 라벨 트리거), 단 repo 설정 `allow_auto_merge=false`라 `gh pr merge --auto` 불가. `delete_branch_on_merge=false`. 수거 캡슐 `invest-ops__2026-07-31_land-command-post-merge`(land 명령 신설안)가 이 요청과 **동일 설계** — 트리아지 유효 판정 후 흡수하면 됨.
- **METH-134 실험 모드(god mode)**: 경영 제약이 프로토타입 개발을 막는 문제. 핵심 논점 = 자유 구역의 **경계**. 무경계 시 invest-ops(조합원·금융 데이터)·운영 서비스까지 게이트 없이 열림.
- **METH-135 자율주행 8시간**: 가능하나 조건부 — 지침 07 §5.2가 이미 "wall-clock은 SDK 미강제, 운영 계약"이라 명시. 실질 blocker는 권한 프롬프트(settings.json 사전 allowlist 없으면 무인 실행 중단)·컴팩션(지침 06)·Class B/C 게이트(→ METH-134가 선결).

## 다음 구체 행동

1. 이 PR(`fix/ci-observation-lint-20260807` → main) 머지 → **Actions `validate` green 실측**(red 복구 확인이 acceptance).
2. 사용자 결정 2건 수령 → METH-133/134/135 ADR 작성(거버넌스 변경이라 Class C) → 구현.
3. METH-131 캡슐 트리아지 — METH-133이 `land` 캡슐을 흡수하므로 함께 처리.

## 현재 열린 트랙 (콜드스타트용)

- **METH-132**(InProgress): CI 복구, PR 대기.
- **METH-133/134/135**(미등록, 설계 대기): 자동 머지 · 실험 모드 · 자율주행.
- **METH-131**(Blocked): 캡슐 트리아지 15건.
- **METH-130**(Backlog): UI repo 6곳 방어층 설치. **METH-113**(Backlog): retrofit.
- 후속 후보: graph.json outbox/collect 노드 · invest-ops `capsule_policy: restricted` · RFC-003 관찰(8/12경) · grooman sync(타 호스트) · 월간 전수조사 2회차(8월 말).

## 막힌 것
- 없음. METH-133~135는 막힘이 아니라 사람 결정 대기.

## 환경
- macOS, python3. 대시보드 http://localhost:8768.
