- **Working on**: **캡슐 수거 4회차(METH-142)** — 전 repo `collect --apply` 완료(신규 24건·원장 21→45). 다음은 **사람 판정**(유효/이미 반영/만료) — TODO `## Blocked`.# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **지침 22 v4 전파 종결**(branch `chore/guide-22-propagation`) — sync-all 7/8 적용·origin 대조 6/6 ✓. 잔여: cafe24-renewal(진행중 작업으로 skip). 직전: #148 정련 land · #149 README 정합 land.
- **Current mode**: fullstack
- **Next TODO**: **METH-142 트리아지 판정**(24건 — 선반영 의심 4건 먼저 걸러내면 실판정 20건) · **METH-135 첫 실주행 검증**(사이클 45~90분 환산 실측 → 지침 29 v2 환류) · 무인 권한 allowlist(settings.json) · METH-134 실험 모드 첫 실전 적용. 다음 캡슐 수거는 다운스트림 축적 후(주기 약 1주). 후속 후보: capsule 발신 시점 id 검증(워크트리 접두어 경고 — METH-140 이전 발행분이 이번 수거에도 1건) · 월간 전수조사 2회차(8월 말). **프로세스: branch-first · 세션 종료 = ship → land.** 상세는 checkpoint.
- **Blockers**: METH-142 캡슐 24건 사람 판정 대기(2026-09-02~).

## Active Links

- Current PR: METH-106 다운스트림 sync (신규, base=main) · 095~105 = #84~#94 머지 완료 · 063~094 = #53~#83 머지
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
| - | ~~sync가 다운스트림 고유 파일 mirror-delete~~ | — | **Closed** — METH-046(PR #35)로 prune을 --prune opt-in화(기본 보존) |
| - | ~~legacy/archive docs pre-v4 경로 언급~~ | — | **Closed(METH-091)** — 라이브 문서 sweep: `10_foundation/` 3건(`docs/snapshots/`→`40_dev/snapshots/`) 수정. 나머지는 정당(정확한 인용·예시)·90_archive는 히스토리 보존 |
| - | ~~v3.2 backward-compat 코드 폴백~~ | — | **Closed(METH-100)** — methodology.py·generate-dashboard.py의 v3.2 구조탐지·폴백(40_resources/60_meta/docs/legacy-root) 제거→v4.0 고정. `migrations/v3.2_to_v4.0.py`(이관)·런처/훅 부트스트랩 탐지는 보존. py_compile·dashboard 재생성·wrap 검증 |
| - | ~~ai-icons·icons-invest guide 번호 충돌~~ | — | **Closed(METH-089)** — 커스텀 04/05/21→90/91/92 이관·doc_id·참조 갱신, origin/main 검증. 잔여: ai-icons 92_LOCAL(구 21)은 상류 05 정본과 149줄 차이=로컬 발전분 → 각 repo 세션에서 상류 05로 환류·재조정 검토 |
| - | ~~sync 홀드 3곳(dirty)~~ | — | **Closed(METH-088)** — ai-icons·cafe24·icons-invest dirty 해소 후 086 sync 완료. **관리 다운스트림 6곳 전부 086 반영** |
| - | ~~`methodology-graph.json` 노드 불완전~~ | — | **Closed(METH-099)** — guide 10종(02·03·05·06·07·08·09·19·20·21) + 학습루프(observations·catalog·skeletons) + checkpoint 노드 추가, stale ai-log 제거. 노드 29→42·엣지 39→53. dashboard 렌더 검증(nodes=42)·JSON 정합 0 오류. (04는 미존재라 제외) |
| - | ⚠️ **스택-PR 재타깃 함정** — #85/#86/#87이 main 아닌 중간 브랜치로 머지됨(096/097/098 main 미반영) | — | **복구중(METH-099)** — 099 브랜치가 095-098 온전 보존 브랜치 기준 → base=main 단일 PR로 096+097+098+099 한 번에 복구. 교훈: 스택-PR은 순서·브랜치 삭제 타이밍 취약 → **main 직행 단일 PR 선호** |
| - | ~~`.claude/skills` 레거시 3종~~ | — | **Closed(METH-090)** — ai-planning·ai-relay·vibe-coding 삭제. 기능은 guide 01/08/19+prompts가 정본. 90_archive 히스토리는 보존 |
| - | icons-invest sync 커밋(f4e6605)에 `30_planning/10_사업기획서.md` 3줄 WIP 혼입 | Low | METH-106 sync 시 `git add -A`가 미커밋 WIP 쓸어담음. 내용 정당(미정 placeholder·Class C 미침범)·main 보존·유실 없음. 히스토리 재작성 안 함. **교훈: sync 커밋은 타깃 스테이징**(observe friction 기록) |
| - | **grooman이 이 머신 sync-all에서 미발견** — `/Users/hayden` 아래 `.methodology-version` 스캔에 없음(2026-07-23 확인). 등록 세션은 타 호스트(codex, darwin-26.4.1) 추정 | Low | grooman 작업 세션에서 실제 경로/호스트 확인 — 타 머신이면 sync-all 커버리지 한계로 HANDOFF에 명시, 이 머신이면 경로 복구 |
| - | ~~init 스캐폴드 HANDOFF `- Working on:` ↔ boot 파서 볼드 기대 불일치~~ | — | **Closed(METH-114)** — 파서 `_handoff_working_on` 헬퍼로 양쪽 허용 + 템플릿 볼드화 + 회귀 테스트(`tests/test_boot_handoff.py`). 둘 다 shared_paths라 다음 sync-all에서 전 다운스트림 자동 전파 |
| - | ~~ai-icons·talmo-com 다운스트림 sync 미적용~~ | — | **Closed(2026-07-15)** — 두 곳 clean 재확인 후 v4.0 sync·push(각 29파일). ai-icons push는 자체 라이브파일 비대로 pre-push 훅 차단→established 절차대로 --no-verify 우회. **잔여**: ai-icons 자체 checkpoint(547줄)·TODO Done(272건) 비대 트리밍은 그 repo 세션 몫 |

## Recent Changes
- 2026-09-02 — **캡슐 수거 4회차(METH-142)**: 16 repo 순회 `collect --apply` — 신규 **24건**(icons 14·cafe24-renewal 5·ai-icons 1·선반영 의심 4), 원장 21→45. icons 워크트리 5곳이 전부 dedup 돼 **METH-140 수정이 첫 실전에서 효과 확인**(직전 dry-run 105건 → 실적재 24건). 판정은 사람 몫 — TODO Blocked.
- 2026-09-01 — **METH-141 트리거 자산 제외**: 이미지·영상·폰트를 Class B/C 경로 검사에서 제외(문서 확장자는 유지 — 법무·과금 미탐 방지). icons 인증 적중 25→9건. 하류 icons#670 역주입으로 경합 패치 3건 전부 상류 안착.
- 2026-09-01 — **METH-140 캡슐 `origin_repo` 워크트리 갈라짐 수정**: `_repo_name` 을 `--git-common-dir` 기준으로 — 워크트리 발행 캡슐이 중복 수거되던 원인(METH-137 미해소 건). 하류 icons#668 역주입.
- 2026-09-01 — **METH-139 `plan` 규칙 정련**: METH-138 과 icons 병렬 수정이 상보적이라 합집합 채택 — 과금낱말 복합어 + **복수형만**. icons 실측 824→2건(잔여 전부 진짜 checkout). 단수 `plan` 은 기획 용법이라 제외.
- 2026-09-01 — **METH-138 land `plan` 오탐 수정**: 과금 트리거의 `plan` 경계를 `[./_-]`→`[./]` 로 축소(`plan-viewer` 오판 해소 · 나머지 6낱말 불변). `tests/test_land_class_patterns.py` 신설 6케이스 — 상류 64테스트 green. 전파 필요(11 repo).

- 2026-08-22: **지침 22 v4 — 정련 land + README 정합 + 다운스트림 전파 7/8 (Class A)** — 정련 브랜치를 main(61커밋 앞섬) 위로 리베이스해 v2(METH-128) 불변규율 4·5 와 P3 리드백 게이트를 승계 통합(규율 6개)·변경이력 v1~v3 보존 + v4 → #148 land(6f6aec5a). `20_guides/README.md` §3.6·현황표(v1→v4, 3릴리스 연속 미반영분 소급)·변경이력 v4.4 → #149 land(4f573de5). sync-all 전파 **7/8**(ai-icons·gamblescan·grooman·icons-invest·talmo-com·tshome + icons) · **origin 실내용 대조 6/6 ✓**(블롭 grep, 지침 23 §1-4) · skip 1(cafe24-renewal 진행중 작업 보호). **icons 이력 오염 1건**: 브랜치 전환 레이스로 sync 커밋이 피처 브랜치에 유입 → PR #386 squash 로 main 도달(내용 정상, 존치 판단).
> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

