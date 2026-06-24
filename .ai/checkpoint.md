# Checkpoint — 2026-06-24 (METH-046 sync mirror-delete 버그 픽스)

> ✅ METH-046: `60_tools/methodology.py`의 `sync`가 shared 디렉터리를 mirror 하면서
> *상류(방법론 정본)에 없는 다운스트림 고유 파일*을 조용히 삭제하던 데이터 손실 버그 픽스.
> (METH-039~044 다운스트림 sync 중 ai-icons 고유 지침 `20_guides/04_문서보관규칙`이 지워질
> 뻔해 수동 복원했던 그 문제 — 후속 chip `task_b0c3337e`.) 수정: prune을 `--prune` opt-in으로,
> 기본은 보존 + 경고. Class A.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-046-sync-no-mirror-delete` (main 기준)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-046 sync mirror-delete 픽스** (사용자: "sync mirror-delete 수정 칩 지금 이어서 고쳐"):

- 근본 원인: `cmd_sync`(`methodology.py`) line ~1215 `copy_path(..., prune=src.is_dir())` —
  shared *디렉터리*를 무조건 mirror → `copy_path`의 prune 블록이 *dst 에 있으나 src 에 없는*
  파일(다운스트림 고유)을 `dp.unlink()` 로 삭제. `_excluded_from_copy`(캐시/생성물)만 빠지고
  적용 프로젝트 고유 지침/문서는 보호 안 됨.
- 수정:
  1. `copy_path` 에 `prune_report: list[Path] | None` 추가 — prune 후보를 *보고만* 수집,
     prune=False 면 삭제 안 함. prune 블록에 `skip` 체크도 추가(일관성).
  2. `cmd_sync` shared_paths 루프: prune 을 `--prune` opt-in 으로(`do_prune and src.is_dir()`).
     기본(미지정): 상류에 없는 고유 파일을 "보존: …삭제 안 함 (정리하려면 --prune)" 경고로 표시.
     `--prune`: "would delete/deleted … (상류에 없음 — prune)" 으로 삭제 목록 표시.
  3. sync 서브파서에 `--prune` 플래그 신설. worktree 서브sync Namespace 에 `prune=do_prune` 전파.
- 검증: `py_compile` 통과. ai-icons dry-run — 기본=`20_guides/04_*` "보존"(삭제 안 함),
  `--prune`=`would delete`. init 은 이미 `copy_path(dry_run=False)`(prune 기본 False)라 무영향.
- 잔여(경미·별개): CLAUDE/AGENTS `merge_managed` 가 관리블록 *안에* 다운스트림이 추가한 라인을
  제거하는 건 본 픽스 범위 밖(파일 삭제가 아닌 1라인). 필요 시 후속 — 관리블록은 본래 상류 소유.

## ⚠️ 다음 사람: 우선 처리 후보 (병렬 PR 2개)

- **PR #34**(METH-045 백서) + **METH-046 PR**(본 sync 픽스) — 둘 다 main 기준 병렬. 코드/문서
  파일은 비충돌(백서=10_foundation, 픽스=60_tools). 라이브 파일(HANDOFF/TODO/checkpoint)은
  둘째 머지 PR 에서 합류 필요. 권장: 하나 머지 → 다른 하나 rebase(라이브 파일만 수동 합류).
- 머지 후 이번 세션(METH-039~046) 완전 종결. 다운스트림은 이미 sync 완료(METH-046 픽스는 본
  저장소 코드라 다음 다운스트림 sync 때 자연 수령).

## 다음 사람에게 (구체적 첫 행동)

1. 사용자 지시 대기.
2. PR #34 / METH-046 PR 머지 순서·라이브 파일 합류는 위 참조.

## 막혔던 지점 / 시도해봤지만 안 된 것

- 없음. 단일 진단(prune=src.is_dir() mirror) → copy_path/cmd_sync 2곳 + 플래그 1개 픽스.

## 미해결 결정사항 (Open Questions)

- CLAUDE/AGENTS 관리블록 내 다운스트림 추가 라인 보존 여부(설계상 관리블록=상류 소유 → 현 동작이
  "맞음"이나 사용자엔 의외). 정책 결정 필요 시 ADR.

## 환경 메모

- 브랜치: `claude/meth-046-sync-no-mirror-delete` (main 기준).
- 변경: `60_tools/methodology.py`(copy_path·cmd_sync·sync 서브파서·worktree sub_args) + 라이브 4종.
- 검증 대상: ai-icons(고유 `20_guides/04` 보유) — dry-run 으로만 확인(비파괴).
