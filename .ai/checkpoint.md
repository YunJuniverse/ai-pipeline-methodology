# 세션 체크포인트
> 세션 서사 바통. 누적 상태는 `HANDOFF.md`.

## 방금 한 것 (2026-09-01 · METH-138)
**`land` 의 Class B 과금 스캐너가 `plan-viewer` 를 요금제로 오판하던 것을 고쳤다.**

- 발단: icons 레포에서 `50_apps/plan-viewer/` 아래 한 줄짜리 속성 추가 PR(#664)이 Class B 로 걸려 자동 머지가 거부됐다. 원인은 `CLASS_BC_PATTERNS` 과금 항의 `plan` 대안 — 경계가 `[./_-]` 라 폴더명 `plan-viewer` 의 `plan-` 을 문다. **해당 앱 디렉터리 아래 모든 변경이 영구히 Class B** 였다(문서 본문 단어 오탐과 달리 경로라 회피 불가).
- 수정: `plan` 만 분리해 `(^|/)plans?[./]` — 세그먼트·파일명 **전체**가 plan 일 때만. 나머지 6낱말(billing·payment·pricing·checkout·invoice·subscription)은 경계 불변.
- **테스트 선행**: `tests/test_land_class_patterns.py` 신설. 수정 전 3/5 fail 로 오탐을 먼저 재현하고, 수정 후 6/6. 미탐 방지(진짜 과금 8종·타 트리거 10종)를 오탐 방지와 같은 무게로 고정했다.
- **감수한 대가를 테스트로 박제**: `config/plan_limits.json` 류 복합어는 이제 놓친다. 대조군(`billing/plan_limits.json`·`src/pricing/plan_limits.json`)이 계속 걸림을 함께 고정해, 나중에 경계를 넓히려는 사람이 무엇을 사고 파는지 알고 결정하도록 했다.
- 실사고 재판정: 수정된 `_classify_change` 로 PR #664 의 실제 diff → **Class A, 트리거 없음**.
- 회귀: 상류 8파일 64테스트 전부 pass.

## 판단 근거 (fail-closed 를 깬 게 아니다)
설계 주석의 비대칭(오탐 싸고 미탐 비쌈)은 그대로 둔다. 다만 **앱 디렉터리 하나를 통째로 오판하는 오탐**은 성격이 다르다 — 사람을 `--no-ci-check`·수동 머지 습관으로 밀어내 오히려 안전을 깎는다. 늘 우는 늑대는 무시된다. `plan` 은 목록 7낱말 중 유일하게 요금제 밖에서도 흔한 수식어라 이 항만 좁혔다.

## 다음 구체 행동
- PR 머지 후 **11 repo 전파**(`sync-all`) — icons 계열 worktree 는 origin 공유로 자동 커버. 전파 후 icons 에서 `land` 재시도해 plan-viewer PR 이 Class A 로 통과하는지 실측.
- icons 발신 캡슐(`2026-09-01_land-billing-pattern-path-false-positive.md`)은 이 반영으로 종결 — 다음 `collect` 때 정리.

## 막힌 것
- 없음.

## 환경
- `~/methodology` · 브랜치 `fix/land-class-plan-false-positive`(base=origin/main `86f6874`).
