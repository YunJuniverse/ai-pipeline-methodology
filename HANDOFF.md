# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **다음 작업 대기.** 직전 완결: METH-143(wrap 구조 검증, 전파 11/11) · METH-142 캡슐 루프 4회차 — 수거 24건→판정→반영→전파 2회를 한 세션에 완주(#155·#157·#158·#159·#160·#161, maincheck 전건 ✓).
- **Current mode**: fullstack
- **Next TODO**: **METH-135 첫 실주행 검증**(사이클 45~90분 환산 실측 → 지침 29 v2 환류) · 무인 권한 allowlist(settings.json) · METH-134 실험 모드 첫 실전 적용. 다음 캡슐 수거는 다운스트림 축적 후(주기 약 1주). 후속 후보: capsule 발신 시점 id 검증(워크트리 접두어 경고 — METH-140 이전 발행분이 이번 수거에도 1건) · 월간 전수조사 2회차(8월 말). **프로세스: branch-first · 세션 종료 = ship → land.** 상세는 checkpoint.
- **Blockers**: none.

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
- 2026-09-02 — **METH-143 전파 11/11 종결**: main 직접 8·격리 워크트리 3, origin 대조 ✓, 훅 3 repo 재설치. 전파 후 다운스트림 실측 **error 0 · warn 11** — 착수 전 예측과 일치(오탐 0).
- 2026-09-02 — **METH-143 wrap 라이브 파일 구조 검증**: Working-on·섹션·칸반 **중복을 error**(모호성 = 파서가 조용히 하나를 고름), 부재는 warn. 착수 전 12 repo 전수 실측으로 경계 확정(**error 0건** — 오탐 없이 사고만 잡는다). 87/87 green.
- 2026-09-02 — **METH-142 종결**: 캡슐 루프 4회차 완주. 산출 = 지침 5개 개정 + **지침 30 신설**(동시 세션 git 격리) · 도구 4건(rotate 순서 검사 · build-guard `dev-check` 단일화 · ship 스테이징 확인 · 훅 sync 판정 경로 기준) · `_pending` 3건 · `_inbox` 비움(원장 45). 전파 2회 각 11/11 + origin 실내용 대조. 테스트 82/82.
- 2026-09-02 — **METH-142 2차 전파 11/11 종결**: 지침 30·훅 경로판정·outbox 규칙 전파(main 직접 8·격리 워크트리 3). origin 대조 4항목 × 11 repo ✓. 훅 3 repo 재설치로 **새 경로 판정이 실제로 걸린 것까지 확인**. invest-ops 는 1차를 워크트리에서 push 해 로컬 main 이 뒤처져 있었고 rebase 로 해소(워크트리 push 의 부작용 — 지침 30 후속 후보).
- 2026-09-02 — **METH-142 잔여 3건 + 판단 4지점 확정**: **지침 30 신설**(동시 세션 git 격리 — 캡슐 2건 병합 승급, 트리거를 01 §5.11·CLAUDE.md 양쪽에 등록) · land 콘텐츠 판정 **비채택 박제** · outbox 발신 규칙에 「다른 곳에서도 참인 규율만」 · **훅 sync 면제를 변경 경로 기준으로 교체**(3회 재발 마찰 종결, `shared-paths` 단일 소스). 실 push A/B/C 증명 · 테스트 82/82 · `_inbox` 비움(원장 45).
- 2026-09-02 — **METH-142 전파 종결 11/11**: main 직접 7 · 격리 워크트리 4(진행 중 작업 보호). origin 실내용 대조 11/11 ✓. **훅 sync 면제가 커밋 메시지 패턴 매칭이라** `chore: 방법론 sync` 는 안 걸리고 `chore(methodology): sync` 만 통과 — 2 repo push 차단 후 메시지 교정으로 해소(3회째 재발, 후속 후보).
- 2026-09-02 — **캡슐 트리아지 4회차 반영 16건(METH-142)**: 지침 5갈래(05 v4 대시 금지 · 19 v4 §8b.3 구조 편집 · 23 v4 전제 이월·판정 오라클 · 24 v3 진단 생성·규칙 저술 게이트 · 25 v2 게이트 ② 대리물) · 도구 3(rotate 순서 검사 fail-closed · **build-guard 를 `dev-check` 단일 판정으로 통합** — METH-131 이 파이썬 경로만 고쳤던 갈라짐 해소 · ship 스테이징 확인) · `_pending` P-003~005. 테스트 80/80. `_inbox` 21건 정리·원장 45 유지.
- 2026-09-02 — **캡슐 트리아지 판정 초안(METH-142)**: 24건 전량을 상류 코드·지침과 실측 대조 — **유효 19·이미 반영 5·만료 0**. 발견 2건: `build-guard.sh` 는 METH-131 의 cwd 스코프가 **셸 경로에만 미반영**(사람이 실제 지나는 경로) · `_rotate_todo_done` 의 미정렬 가정이 **이 repo TODO 에서도 재현**(116 이 131 보다 위). icons·cafe24 가 같은 편집 사고를 재현해 지침 19 §8b 확장이 N≥2 로 정당화.
- 2026-09-02 — **캡슐 수거 4회차(METH-142)**: 16 repo 순회 `collect --apply` — 신규 **24건**(icons 14·cafe24-renewal 5·ai-icons 1·선반영 의심 4), 원장 21→45. icons 워크트리 5곳이 전부 dedup 돼 **METH-140 수정이 첫 실전에서 효과 확인**(직전 dry-run 105건 → 실적재 24건). **16건 반영 완료**(도구 3·지침 5·pending 3·존치 1, 테스트 80/80). **24건 전량 종결** — 판단 4지점 확정(권고안 채택)·잔여 3건 반영·`_inbox` 비움. **전파 2회 모두 11/11 종결**(origin 실내용 대조 ✓). METH-142 완결.
- 2026-09-01 — **METH-141 트리거 자산 제외**: 이미지·영상·폰트를 Class B/C 경로 검사에서 제외(문서 확장자는 유지 — 법무·과금 미탐 방지). icons 인증 적중 25→9건. 하류 icons#670 역주입으로 경합 패치 3건 전부 상류 안착.
- 2026-09-01 — **METH-140 캡슐 `origin_repo` 워크트리 갈라짐 수정**: `_repo_name` 을 `--git-common-dir` 기준으로 — 워크트리 발행 캡슐이 중복 수거되던 원인(METH-137 미해소 건). 하류 icons#668 역주입.
- 2026-09-01 — **METH-139 `plan` 규칙 정련**: METH-138 과 icons 병렬 수정이 상보적이라 합집합 채택 — 과금낱말 복합어 + **복수형만**. icons 실측 824→2건(잔여 전부 진짜 checkout). 단수 `plan` 은 기획 용법이라 제외.
- 2026-09-01 — **METH-138 land `plan` 오탐 수정**: 과금 트리거의 `plan` 경계를 `[./_-]`→`[./]` 로 축소(`plan-viewer` 오판 해소 · 나머지 6낱말 불변). `tests/test_land_class_patterns.py` 신설 6케이스 — 상류 64테스트 green. 전파 필요(11 repo).

- 2026-08-22: **지침 22 v4 — 정련 land + README 정합 + 다운스트림 전파 7/8 (Class A)** — 정련 브랜치를 main(61커밋 앞섬) 위로 리베이스해 v2(METH-128) 불변규율 4·5 와 P3 리드백 게이트를 승계 통합(규율 6개)·변경이력 v1~v3 보존 + v4 → #148 land(6f6aec5a). `20_guides/README.md` §3.6·현황표(v1→v4, 3릴리스 연속 미반영분 소급)·변경이력 v4.4 → #149 land(4f573de5). sync-all 전파 **7/8**(ai-icons·gamblescan·grooman·icons-invest·talmo-com·tshome + icons) · **origin 실내용 대조 6/6 ✓**(블롭 grep, 지침 23 §1-4) · skip 1(cafe24-renewal 진행중 작업 보호). **icons 이력 오염 1건**: 브랜치 전환 레이스로 sync 커밋이 피처 브랜치에 유입 → PR #386 squash 로 main 도달(내용 정상, 존치 판단).
> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

