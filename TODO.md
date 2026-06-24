# TODO.md

> Active backlog only.
> Use stable IDs.
> Completed detail belongs in git history, PRs, or dated snapshots — not here.
> 칸반보드(대시보드)가 아래 5개 섹션 헤더(`## Backlog`, `## Ready`, `## InProgress`, `## Blocked`, `## Done`)를 그대로 파싱한다. 헤더 이름을 바꾸지 마라.

## Backlog

## Ready

## InProgress

### METH-046
- **title**: sync mirror-delete 버그 픽스 — 다운스트림 고유 파일 보존 (`--prune` opt-in)
- **notes**: 작업 완료, **PR #35 대기**(브랜치 `claude/meth-046-sync-no-mirror-delete`, main 기준). Class A. 발견: 다운스트림 sync 중 `methodology.py`의 `copy_path(prune=src.is_dir())`가 shared 디렉터리를 mirror 해, *상류에 없는 다운스트림 고유 파일*(ai-icons `20_guides/04_문서보관규칙`)을 조용히 삭제. 수정: ① `copy_path`에 `prune_report` 추가 — prune 후보를 *보고만* 하고 기본은 삭제 안 함. ② `cmd_sync`에서 prune을 `--prune` opt-in으로(기본 보존), 상류에 없는 고유 파일은 "보존" 경고로 표시, `--prune` 시 삭제 목록 표시. ③ sync `--prune` 플래그 신설 + worktree 서브sync에 전파. 검증: ai-icons dry-run — 기본=guide 04 "보존", `--prune`=`would delete`. init은 prune=False라 무영향. py_compile 통과.

## Blocked

## Done

> 최근 완료 3건만 유지. 이전 완료 항목은 `git log --grep="METH-"` 및 `40_dev/snapshots/` 참조.
> (CLAUDE.md §파일 역할: "Full completion archives — move historical detail to git, PRs, or dated snapshots — not here.")

### METH-045
- **notes**: Completed 2026-06-24. **PR #34 머지 완료**(main `7ed86f1`). Class A. 방법론 백서 겸 가이드 — 레포 `10_foundation/방법론_백서_가이드.md`(11섹션) + Notion In-spire 하위 페이지 업로드. 기존 WHITEPAPER.md(메타 헌법)와 상보, 콘텐츠(craft·템플릿·모드)까지 포함한 현행 종합본.

### METH-044
- **notes**: Completed 2026-06-24. **PR #33 머지 완료**(main `6d3d4e8`). Class A. 모드별 템플릿 선택 체계 — `_CATALOG.md`(25종 + 6모드 매트릭스) + CLAUDE/AGENTS Mode 확장 + 지침 00 §11.8. **다운스트림 sync 완료**(icons·gamblescan·ai-icons, cafe24 제외).

### METH-043
- **notes**: Completed 2026-06-24. **PR #32 머지 완료**(main `ca6fc57`). Class A. icons-ip 경량 문서 craft 7종 — 신규 템플릿 3종(prd·architecture·context-glossary) + ADR 강화 + requirements(M/S+Pn) + 지침 00 §11.5~11.7.

<!-- Archived: METH-001~042 (2026-05~06). 상세는 git log --grep="METH-" 및 PR #5~#34, 40_dev/snapshots/ 참조. CLAUDE.md 파일역할: Done 은 최근 ~3건만. -->
