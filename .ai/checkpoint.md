# Checkpoint — 2026-07-29 (METH-120+121 구현 — maincheck·observe 강제)

> ✅ 구현·테스트 완료 — P1(스택-PR)·P2(관찰로그 무신호) 구조적 차단. branch `feat/meth-120-121-guards`, PR 대기. 머지 후 sync-all 전파.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `feat/meth-120-121-guards` (base=main 787311e, branch-first)

## 방금 한 것

- **METH-120 `maincheck`**: `cmd_maincheck` — fetch(옵션)→`_git_remote_default_ref`(origin main/master)→다건 sha `merge-base --is-ancestor` 대조, 미도달 exit 1 + "스택-PR 금지·Done 처리 금지" 안내. usage 헤더·argparse 등록. CLAUDE.md·AGENTS.md §2에 "스택-PR 금지·Done 검증 (의무)" 불릿(컴팩션 불릿 위).
- **METH-121 observe 강제**: `normalize_repeat_of`(REPEAT_OF_RE: session_id|kebab|C-NNN; "repeat_of:" 접두 반복 제거; yes/repeat류·자유 텍스트 ValueError) → parse_friction_item·validate_observation_file 양쪽 적용. 메타: ctx "unknown"을 미기입 취급 후 env 추정(ANTHROPIC_MODEL·CLAUDECODE·CODEX_SANDBOX)·host_os 상시 실측. domain 기본 "meta" 제거 — 미해석 시 exit 2. prompt_patterns 자동 상용구 제거(기본 []). `observation_quality_warnings`(unknown·domain=meta·상용구) — 생성·--validate 시 출력. 부수 수정: `parse_observation_frontmatter`가 repo 밖 절대경로에서 죽던 것 견고화.
- 테스트: `tests/test_maincheck_observe.py` 11종 — repeat_of 정규화/거부 5종·다건 friction id·빈 prompt_patterns 검증·오염 파일 거부·품질 경고·**임시 git repo(bare remote+clone)로 maincheck exit 0/1 실검증**. 회귀: capsule 13·sync-all 9·boot 5 전부 통과. E2E: 이 repo에서 maincheck HEAD~1 도달 ✓·오염 friction 생성 거부 ✓.
- **마찰(기록함)**: TODO 섹션 이동에서 `index("## InProgress")`가 6행 안내문에 오매칭 — **오늘 세 번째 같은 유형**(#117 손상과 동일 원인). 이번엔 write 전 assert가 잡아 git checkout 복구, `^## ` 행 앵커 정규식으로 재작업. "규칙이 아니라 강제"의 자기 실증 — observe friction에 repeat_of 체인 기록.

## 다음 구체 행동

1. 이 PR(`feat/meth-120-121-guards` → main) 머지.
2. **머지 후 sync-all 전파** — shared 변경: methodology.py·CLAUDE/AGENTS. 절차 동일(main 6곳 직접 + 비-main worktree, 훅 차단 2곳 --no-verify). 전파되면 전 repo에서 maincheck 사용 가능 + observe가 오염 기록을 거부.
3. 전파 후 METH-120·121 → Done(maincheck로 자가 검증하고 이동 — dogfood).
4. 다음 구현 후보: METH-122(라이브 파일 fail-closed + build 가드) 또는 METH-118+121 잔여(prompting 블록). 사람 지정 대기.
5. 참고: 다운스트림 `.ai/context.json`의 stale last_session(예: 이 repo ctx가 gpt-5)이 자동 채움에 실릴 수 있음 — 세션 시작 시 ctx 갱신이 안 되는 repo는 --agent/--tool 명시가 정확.

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.
