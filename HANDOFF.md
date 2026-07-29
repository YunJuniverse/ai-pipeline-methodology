# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **METH-120+121 종결 — 전파 11/11** (2026-07-29) — #121 머지 후 sync-all: 전 repo가 maincheck·observe 강제 획득(dirty 3곳도 worktree로 무방해 반영). Done 이동은 maincheck 자가 검증 후(dogfood). branch `chore/sync-propagate-meth-120-121`, PR 대기. 다음 구현 후보: METH-122(라이브 파일 가드) 또는 METH-118+121 잔여(prompting 블록) — 사람 지정 대기. 직전: METH-120·121 구현(#121 머지).
- **Current mode**: fullstack
- **Next TODO**: 후속 후보(백로그 미등록): graph.json에 outbox/collect 노드·invest-ops `capsule_policy: restricted` 부여(그 repo 세션·ADR-0001 근거)·pre-push 훅 vs sync push 충돌 3회 재발 → thinktank 승급 후보. 다른 repo(별도 세션): ai-icons 92 환류·비대 라이브파일 트리밍·grooman sync(타 호스트). **프로세스: branch-first · 스택-PR 지양(main 직행) · 세션 시작 = `methodology boot`.** 상세는 checkpoint.
- **Blockers**: none

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

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-29: **METH-120+121 전파 종결 11/11 (Class A)** — #121 머지 후 sync-all: main+clean 5곳 직접, 비-main 3곳+dirty 3곳(icons·icons-invest·lifeManager — 활성 세션 무방해)은 임시 worktree로 origin/main만 반영, 전부 ls-remote 대조. 전 repo가 `maincheck`(Done 전이·배포 게이트)와 observe 스키마 강제(repeat_of enum·메타 자동 채움·domain 필수)를 획득 — 전수조사 P1·P2 결함이 전 다운스트림에서 구조적으로 차단됨. Done 이동은 maincheck 자가 검증(04535d0d ✓, dogfood). 훅 차단 2곳(ai-icons·invest-ops) --no-verify 확립 절차.
- 2026-07-29: **METH-120+121 구현 (Class A)** — ① `maincheck`: 커밋의 origin main 도달을 merge-base로 기계 검증(미도달 exit 1 + 스택-PR 금지 안내) — Done 전이·배포 판정 게이트. CLAUDE/AGENTS §2에 스택-PR 금지·Done 검증 의무 불릿(개인 메모리→전 repo 규칙 승급). ② observe 강제: repeat_of enum(접두 오염 정규화·자유 텍스트 거부)·메타 자동 채움(ctx unknown 무시·env 추정)·domain 기본값 meta 제거·prompt_patterns 상용구 제거·품질 경고 3종. 부수: parse_observation_frontmatter repo 밖 경로 견고화. tests/test_maincheck_observe.py 11종(임시 git repo로 maincheck exit 실검증)+회귀 전부 통과.
- 2026-07-29: **METH-119 트리아지 종결 (Class A)** — 사용자 판정: P1~P9·P11·지침22 갭 **전부 채택** → METH-120(main 도달 검증)·121(observe 강제, 118 통합)·122(라이브파일+build 가드)·123(지침23 검증규범)·124(지침24 착수게이트)·125(스크래핑 SOP)·126(CI 정합)·127(사실주장 출처)·128(지침22 보강) 분배 등록. P10은 RFC-003 초안(결정 대기, B+C 혼합 잠정 권고). insta-toon 스택-PR 미도달 즉시 복구(그 repo PR #7 — 무충돌·64/64). **캡슐 루프 첫 실전 왕복**: icons-invest에서 guide-22 갭 캡슐 발신→push→collect --apply 수거→_inbox·원장 기록→유효 판정. 착수 순서: 120·121(Ready).
- 2026-07-29: **2026-07 월간 전수조사 (Class A, planning)** — 11개 repo 최근 한 달을 병렬 에이전트 11기로 읽기 전용 전수조사(관찰로그 1,006·friction 302·기록 비용 90h+·커밋 1,294). 교차 반복 패턴 12종 식별: 스택-PR 사고 6곳(P1)·observe 스키마 결함 전 repo(P2)·라이브 파일 규칙 미작동 7곳(P3)·무음 실패 6곳(P4)·정본 미확인 5곳(P5)·dev-build 충돌 7회 반복(P6) 등. cafe24는 friction 0/112(스키마 미기입 실증). 즉시 주의: insta-toon 스택-PR 미도달(main에 코드 없음)·invest-ops 민감정보 평문. 스냅샷 `40_dev/snapshots/2026-07-29_전레포-월간-전수조사-마찰-인사이트.md` 정본, 트리아지 METH-119.
- 2026-07-29: **METH-118 백로그 등록 + TODO 손상 복구 (Class A)** — 프롬프팅 코칭 루프 백로그화: 사용자 확정 방향 = 온디맨드 아닌 **상시 자동 기록(wrap 의무, prompting 블록: 라운드·모호 지시 발췌+교정안·용어·상황 태그) + prompt-report 자동 갱신(wrap 파이프라인)**. 토큰은 v1 프록시(PostHog 실측은 옵션 게이트)·원문 저장 금지(발췌만)·교차-repo 통합 v1 제외. TODO 손상(#117 혼입 — 섹션 이동 스크립트 `index("## Blocked")`가 6행 안내문 문자열에 오매칭 → 중복+Done 헤딩 유실) 정본 재작성 복구, friction 기록(교훈: 섹션 조작은 `^## ` 행 앵커 정규식).