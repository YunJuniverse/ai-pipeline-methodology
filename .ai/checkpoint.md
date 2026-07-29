# Checkpoint — 2026-07-29 (METH-117 구현 — 캡슐 outbox 역방향 루프)

> ✅ 구현·테스트 완료 — capsule/collect 명령+가시성+안전 가드+문서, tests 13종·E2E 스모크 통과. branch `feat/meth-117-capsule-outbox`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `feat/meth-117-capsule-outbox` (base=main 57cfb7d, branch-first)

## 방금 한 것 (이번 세션 — 사용자 Ready 승격·착수 지시)

- `60_tools/methodology.py`:
  - 상수: `OUTBOX_DIR`(50_resources/meth_outbox)·`INBOX_DIR`(meth_inbox)·`CAPSULE_TYPES` 4종·본문 120줄 가드.
  - `cmd_capsule`: 1제안=1캡슐=1파일 생성(id=`<repo>__<date>_<slug>`)·`--validate`·`--dry-run`·restricted 정책(.methodology-version `capsule_policy`) 거부+`--allow-restricted`.
  - `cmd_collect`: 다운스트림 발견(sync-all 재사용)→로컬+origin(fetch·ls-tree·show) 병합→원장(`_inbox/_ledger.json`) 중복 skip→`_inbox/<repo>__<file>` 적재. 기본 dry-run·`--apply`. 커버리지 리포트(원격 없음/fetch 실패/repo 아님). 다운스트림 무변경.
  - 가시성: boot [4b](자기 outbox 잔량 + 상류(70_meta 보유)면 전 다운스트림 미수거 총계)·sync-all 표 outbox 컬럼+총계 경고.
  - 안전: `_detect_sensitive`가 outbox .md 변경분의 *내용* 시크릿 패턴(_CAPSULE_SECRET_RES) 검사. MANIFEST: shared에 `meth_outbox/_README.md`만, init_paths에 outbox 디렉터리, init_path_excludes로 캡슐 본체 격리. _inbox는 어디에도 미전파(상류 전용).
  - thinktank: `_thinktank_capsule_section` — _inbox target별 집계, `CROSS-REPO`/`DUP-TARGET` 마킹.
- 문서: `50_resources/meth_outbox/_README.md`(원칙·트리거 표·CLI·민감정보·수거 이후), `50_resources/meth_inbox/_README.md`(원장·트리아지 유효/이미 반영/만료), catalog `_README.md` §3 캡슐 트랙, CLAUDE.md·AGENTS.md §2 캡슐 규칙 불릿(명시 요청=의무).
- 테스트: `tests/test_capsule_collect.py` 13종(roundtrip·검증 거부 4종·원장 dedupe·폴백 id·파일 필터·정책·시크릿 스캔). 기존 sync-all 9·boot 5 회귀 통과. E2E 스모크: 임시 repo 캡슐 생성→restricted 거부→collect dry-run/apply→재수거 0건→thinktank 섹션·sync-all 컬럼·boot 확인. 테스트 산출물 정리 완료(_inbox엔 _README만).

## 다음 구체 행동

1. 이 PR(`feat/meth-117-capsule-outbox` → main) 머지 → METH-117 Done 이동.
2. **머지 후 sync-all 전파** — shared 변경: methodology.py·meth_outbox/_README·catalog _README·CLAUDE/AGENTS. 절차는 07-29 전파와 동일(main 직접 + 비-main worktree, ai-icons·invest-ops는 --no-verify).
3. 후속 백로그 후보(안 만듦): methodology-graph.json에 outbox/collect 노드 추가(대시보드 그래프 정합, METH-099 계보).
4. invest-ops에 `capsule_policy: restricted` 실제 부여는 그 repo 세션에서 결정(ADR-0001 Class C 근거).

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765. pytest 없음(자체 러너).
