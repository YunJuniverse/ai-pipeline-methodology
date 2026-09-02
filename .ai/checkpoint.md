# 세션 체크포인트

> 세션 서사 바통. 누적 상태는 `HANDOFF.md`.

## 방금 한 것 (2026-09-02 · METH-142 반영)

**판정 초안의 16건을 반영했다.** 사람 판단 3지점에 걸리는 3건만 남겼다.

**도구 3건 (전부 negative case 로 실효 증명)**
- `rotate`: `_rotate_todo_done` 이 아카이브 경계에서 **날짜 역전을 감지하면 중단**(`RotateOrderError`). 날짜 없는 항목은 판정에서 빠지고 그 건수를 보고한다(검사 못 함 ≠ 깨끗함). `--force-order` 로만 통과.
- `build-guard.sh`: 셸이 판정을 직접 하지 않고 **`methodology.py dev-check` 를 호출**한다. METH-131 의 lsof cwd 스코프가 파이썬 경로에만 들어가 있던 갈라짐을 해소 — 판정 원시함수가 한 벌이 됐다(지침 19 §8b.1 자기적용). `pkill`·`build-guard` 자기적중도 배제.
- `ship`: `--no-add-all` 인데 인덱스에 작업트리 변경이 아닌 스테이징이 있으면 **목록을 보이고 중단**한다. `--index-verified` 로만 통과.

**지침 5갈래** — 05 v4(§9b 7항 대시 금지 + 「예외는 형태로 한정」 전제) · 19 v4(§8b.2 확장 + §8b.3 구조 편집·배포 원자성) · 23 v4(§1-4 curl≠브라우저 · §1-5 리드백 타이밍 · §2-3 가시성 · §3-4 미해결 전제 · §4-5 판정 오라클) · 24 v3(§2 진단 생성 + §4b 규칙 저술 전 정본 독해) · 25 v2(§5 게이트 ② 저비용 대리물·폐기·예산).

**catalog** `_pending/P-003`(헤드리스 검증 가능 게임 로직)·`P-004`(임베디드 캔버스·측정 기법)·`P-005`(캐시 적대 플랫폼 표시 게이트).

**검증**: 전 테스트 **80/80**. build-guard 는 실제 프로세스로 A/B/C 증명(같은 repo 차단=1 · 타 디렉터리 통과=0 · 자기적중 배제=0). 표 편집 후 열 수 대조도 돌렸다(새로 쓴 §8b.3 자기적용).

## 다음 구체 행동

1. **사람 판단 3지점**을 받은 뒤 잔여 3건 반영 — `_inbox` 에 그 3건만 남아 있다(`land-classifier-cries-wolf`·`isolated-worktree-for-concurrent-sessions`·`shared-checkout-path-add-not-safe`).
2. **전 repo 전파** — 이번 변경은 지침 5개 + `methodology.py` + `build-guard.sh` 라 sync 대상이 넓다. `sync-all` 후 origin 실내용 대조(지침 23 §1-4).
3. 전파 시 주의: 활성 세션이 있는 repo 는 브랜치 전환 레이스(2026-08-22 icons 이력 오염) — 비-main/dirty 는 worktree 경유.

## 막힌 것

- 없음. 판단 3지점만 외부 게이트 — TODO `## Blocked` METH-142.

## 환경

- repo: `/Users/hayden/methodology` · branch `feat/capsule-triage-round4-reflect`
- 새 명령: `methodology.py dev-check [--path]` (exit 1 = 이 프로젝트 dev 실행 중)
- 새 플래그: `rotate --force-order` · `ship --index-verified`
