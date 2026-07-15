# Checkpoint — 2026-07-15 (METH-107 sync-all 헬퍼)

> ✅ `methodology sync-all` 구현·테스트 완료. feat/sync-all-helper, PR 대기.
> 이번 세션 앞부분: 다운스트림 sync 보류분(ai-icons·talmo) 처리 + 신규 3곳 init(lifeManager·icons-marketing·insta-toon) → 관리 10곳.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `feat/sync-all-helper` (updated main 기준, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
관리 다운스트림이 10곳으로 늘며 sync 팬아웃이 부담이 돼, 사용자 요청으로 **일괄 sync 헬퍼**를 만듦.
- **`methodology sync-all`** (`60_tools/methodology.py`): root(기본 `METHODOLOGY_ROOT.parent` = `~/`) 아래 `.methodology-version` 보유 폴더 자동 발견(방법론 원본 자신 제외) → 사전 스캔 표(project·version·branch·dirty·vs-upstream) → 각 프로젝트 `cmd_sync`에 위임(main-only, prune 전달) → 요약(대상/처리/skip).
- **--apply 안전 가드**(오늘 METH-106 교훈 박제): `_sync_all_skip_reason` — ① git repo 아님 skip ② dirty skip(진행 중 작업 보호) ③ 비-main(main/master) 브랜치 skip(피처브랜치 오염 방지). override: `--include-dirty`·`--allow-nonmain`. commit/push는 각 repo 개별(add -A 혼입 회피 — dry-run/apply 둘 다 파일만 건드림).
- 신규 헬퍼 함수: `_git_current_branch`·`_git_dirty_count`·`_discover_downstreams`·`_downstream_state`·`_is_behind`·`_print_downstream_table`·`cmd_sync_all`. 파서 `sync-all` 등록, 모듈 docstring 갱신.
- **테스트**: `tests/test_sync_all.py` — 의존성 없는 자체 러너(pytest 없음). 발견·정렬·원본제외·가드(dirty/비-main/override/우선순위)·behind 판정 9개. `python3 tests/test_sync_all.py` → 9/9 pass. `py_compile` OK.
- **실측**: `sync-all`(dry-run) 10곳 발견·표·위임 정상. `--help`·빈 root 처리 확인.

## 다음 사람에게
1. **METH-107 PR(base=main) 머지** — feat/sync-all-helper.
2. 머지 후 실제 일괄 갱신은 `methodology sync-all --apply` (dirty·비-main은 자동 skip되므로, cafe24·gamblescan·icons·tshome처럼 피처브랜치인 곳은 main 체크아웃 후 재실행하거나 개별 sync).
3. **주의**: `methodology.py`는 shared라 이 헬퍼 자체가 다음 sync 때 다운스트림으로 전파됨(정상).
4. (미해결, 별도 repo 몫) ai-icons 자체 라이브파일 비대(checkpoint 547줄·TODO Done 272건) 트리밍.

## 환경 메모
- 브랜치: `feat/sync-all-helper` (updated main). branch-first.
- 관리 다운스트림 10곳: icons·ai-icons·icons-invest·cafe24-renewal·gamblescan·tshome·talmo-com·lifeManager·icons-marketing·insta-toon.
- 누적 상태(오픈이슈·PR)는 **HANDOFF 참조** — 여기 복제 안 함.
