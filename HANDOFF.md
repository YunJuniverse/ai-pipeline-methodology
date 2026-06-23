# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-043 icons-ip 경량 문서 craft 역주입 — PRD/ARCHITECTURE/CONTEXT 템플릿 + ADR 강화 + 경량 모드. **별도 브랜치** `claude/inject-lean-doc-craft-from-icons-ip`(main 기준, PR #31과 비충돌). PR 대기.
- **Current mode**: fullstack
- **Next TODO**: METH-043 PR. ⚠️ **병렬 PR 2개**: PR #31(METH-040/041/042, 브랜치 `…from-gamblescan`) + METH-043. 라이브 파일은 두 브랜치가 각각 수정 → 둘째 머지 시 HANDOFF/TODO/checkpoint 합류 필요(craft 파일은 비충돌). 머지 후: ① 다운스트림 sync(METH-039~043 합산, cafe24 경로 미확인) ② **METH-044**(모드별 템플릿 카탈로그 — TODO Backlog에 설계 확정, capstone).
- **Blockers**: none

## Active Links

- Current PR:
- Current issue:
- Relevant ADRs:
- Relevant snapshots: `40_dev/snapshots/implementation-plan-2026-05-07.md`, `40_dev/snapshots/transfer-drill-2026-05-08.md`

## Open Decisions

| ID | Decision | Needed By | Status |
|----|----------|-----------|--------|
| - | `.claude/worktrees/` and `.codex/` are local tool metadata and should be gitignored | 2026-05-07 | Closed |

## Open Issues

| ID | Issue | Severity | Next Step |
|----|-------|----------|-----------|
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-06-23: **METH-043 icons-ip 경량 문서 craft 역주입** — 사용자: icons-ip(방법론 미적용 lean 코드베이스)의 PRD 작성 방식에서 받아들일 craft 검토. 순수 doc craft 7종 채택(GitHub-Issues 트래커는 file-based 설계 충돌이라 제외). 신규 템플릿 3종(`prd.md`·`architecture.md`·`context-glossary.md`) + `ADR-template.md` 강화(결정문장 제목·Considered Options·되돌리기 비용) + `requirements-spec.md`(M/S+Pn) + 지침 00 §11.5~11.7(경량 모드·문서 충돌 surfacing·작업유형 라우팅). Class A. **별도 PR**(main 기준, PR #31과 비충돌). 머지 후 다운스트림 sync.
- 2026-06-23: **METH-039 기획 craft 역주입 — PR #30 머지 완료** — 적용 프로젝트 ICONS의 기획 학습 정제본(`icons:40_dev/knowledge/` 6종)을 방법론으로 환류. 지침 10/11/13/15에 §19 "실무 craft 부록" 추가(핵심가치 도출·검증 우선순위 게이트·KPI 트리·ASIS→TOBE·12단계 산출물·데이터 무결성·Triple Media·4유발 퍼널·WBS·제안 5단계) + `50_resources/templates/` 기획 양식 6종(requirements/ia/service-policy/user-story/kpi-tree/wbs) 신설. 일반 craft만(프로젝트 특화 제외)·출처 명시. Class A(shared). [PR #30](https://github.com/YunJuniverse/methodology/pull/30) 머지(2026-06-23 05:25 UTC, main `2c6e60c`), `origin/main` 동기. **잔여**: 다운스트림 `sync --apply` 전파(icons·ai-icons·gamblescan, cafe24 경로 미확인).
- 2026-05-18: **Human 잔여 종결 — METH-036/038 완전 마감** — 사용자 보고 "휴먼작업 모두 완료" → 검증: gamblescan `_start/.cache/dashboard.html` ✅ untracked(`git rm --cached` 완료, METH-036 마감), talmocom methodology.py 픽스 2/2·`build:"next build"` 확인(ship 실측 정상 전제 충족, METH-038 마감). PR #27(픽스)·#28(기록) 머지·pull 완료, 브랜치 origin/main 동기(ahead 0). 이번 세션 작업(METH-038/037/036/018) 전부 main 안착·종결. 활성 백로그 비움 — 다음 후보 S-021 코드 sprint.
- 2026-05-18: **METH-018 pre-push hook 최신화 (stale→v4.0)** — 발견: icons/talmocom/gamblescan/tshome 모두 hook "활성"이나 구버전(v3.x) 템플릿 — `[ -f "50_tools/methodology.py" ]` 만 검사 → v4.0(`60_tools/`)에선 항상 else "검증 skip" → manifest-check·wrap --strict 안전망이 사실상 무력화. (TODO/HANDOFF 의 "미설치, Human 1회 대기" 프레이밍이 부정확했음 — 실제 stale 설치.) `hooks install --force` 4개 재설치 → 최신 템플릿(3-tier 60→50→root + `METHODOLOGY_SHIP_IN_PROGRESS` ship-skip + METH-022 sync-commit 면제) 반영, 4개 모두 검증. 정본 repo 는 이미 최신. git 공용 `.git/hooks` 공유라 repo당 1회면 worktree 전부 커버 — "worktree마다 별도" 메모 정정. Class A.
- 2026-05-18: **METH-038/037/036 4 프로젝트 sync 전파 완료** — PR #27(METH-038) 머지(origin/main `05c8bfa`) 후 icons/talmocom/gamblescan/tshome 에 `sync --apply` 일괄. 발견: 4개 모두 `HEAD==origin/main` 인데 METH-036/037 sync 가 `--apply`만 되고 미커밋 잔여(methodology.py·generate-dashboard.py·.gitignore·.methodology-version) — 위험 충돌 아닌 이전 세션 미완 전파로 판정. 명시 경로 add(MC-001, `-A` 금지)로 방법론 자산 4개만 커밋, 비-방법론 제외(talmocom `next-env.d.ts` stash·pop, gamblescan `_start/.cache/dashboard.html` 미스테이지 — METH-036 Human `git rm --cached` 잔여). icons 직접 push, talmocom/gamblescan/tshome 은 원격 2커밋(타 세션 dev-spec/관찰/앱) 선행 → 파일 무겹침 확인 후 rebase(force 금지). tshome 은 미추적 `ts-service-plan.html` 가 origin/main 추적본과 바이트 동일 확인 후 제거→rebase(백업 보관). 최종: 4개 픽스 2/2·origin/main 동기 검증. 잔여: talmocom `ship` 실측.
