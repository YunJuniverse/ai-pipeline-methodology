# Checkpoint — 2026-07-29 (METH-122 구현 — 라이브 파일·빌드 가드)

> ✅ 구현·테스트 완료 — P3(라이브 파일 규칙 미작동)·P6(dev-build 충돌) 구조적 차단. branch `feat/meth-122-livefile-build-guards`, PR 대기. 머지 후 sync-all 전파.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `feat/meth-122-livefile-build-guards` (base=main, branch-first)

## 방금 한 것

- **`rotate` 명령**: `_rotate_todo_done`(Done 최신 4건 유지, 초과분 아카이브 md)·`_rotate_recent_changes`(Recent 5건) 순수 함수 + `cmd_rotate`(dry-run 기본·--apply·--checkpoint=전체 사본 아카이브+상단 40줄 스텁). 아카이브는 `40_dev/snapshots/live-archive/YYYY-MM-DD_*.md` — 같은 날 재실행 시 append. **삭제 없음.**
- **wrap 경성 한도**: `live_file_hard_violations`(규정 2배: HANDOFF 300·checkpoint 400·Done 20건) — --strict에서 fail로 계상 + "rotate --apply" 안내. 연성 경고(METH-101)는 유지. 기존 비대 다운스트림 ship은 --no-verify 관례가 있어 즉시 마비는 없음 — rotate가 정도.
- **boot [4a] 신선도**: `staleness_warnings` — HANDOFF Working on 날짜·wrap-state last_validated_at이 최근 커밋 날짜보다 7일+ 뒤처지면 경고.
- **build 가드**: ship build 단계에 `_dev_server_running`(pgrep "next dev") 감지 시 차단. `60_tools/build-guard.sh` 신설(shared_paths 등록 — sync로 전 repo 배포, BUILD_GUARD_FORCE=1 탈출구, 머신 전체 감지라 보수적임을 스크립트에 명시).
- **규칙**: CLAUDE/AGENTS §2 "외부 게이트=Blocked 강제 (의무)" 불릿(+rotate·build-guard 안내).
- 테스트: `tests/test_rotate_guards.py` 6종(회전 보존·noop·경성 임계 분류·비-git 안전) — 안내문 오매칭 계보 방지 어서션 포함. 회귀 44종(maincheck 11·capsule 13·sync 9·boot 5+신규 6) 통과. E2E: 이 repo rotate no-op·build-guard 통과/차단(시뮬 프로세스) 확인.

## 다음 구체 행동

1. 이 PR(`feat/meth-122-livefile-build-guards` → main) 머지 → sync-all 전파(payload: methodology.py·build-guard.sh(신규 shared)·CLAUDE/AGENTS) → METH-122 Done(maincheck 검증 후).
2. 전파 후 실효 후보: 비대 repo(cafe24·gamblescan·ai-icons·icons·icons-invest)에서 각 repo 세션이 `rotate --apply --checkpoint` 실행하면 전수조사 P3 잔여가 즉시 해소됨 — 각 repo 과제로 전달.
3. 다음 구현: METH-118+121 잔여(prompting 블록) 또는 지침 123·124 — 사람 지정 대기.
4. RFC-003 2주 관찰 중 · grooman sync(타 호스트) · repo 과제 4건 잔여.

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.
