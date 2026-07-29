# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **지침 20 v3 — 기본 실수 3층 방어** (2026-07-29) — 사용자 반복 실수(다크 대비·간격 붙음) 환류: §4 절대색 차단(fail)·§9.5 3층 방어(토큰 강제·프리미티브 내장 간격·axe/간격 린트·양모드). METH-130(UI repo 6곳 실설치) 등록. #135 기록 커밋은 cherry-pick 통합(스택-PR 회피, #135 close). branch `docs/guide-20-v3-defense`, PR 대기.
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

- 2026-07-29: **지침 20 v3 — 기본 실수 3층 방어 (Class A)** — 사용자 반복 실수 환류(다크 배경+검은 텍스트 / 패딩 누락 붙음): §4 가드레일에 절대색(`text-black` 등) 차단 추가, §9.5 신설 — 1층 구조(시맨틱 토큰 자동 반전·프리미티브 내장 간격, 기본 패딩 0 구조 금지) 2층 기계(axe 대비 차단·bounding box 간격 린트·양모드 스크린샷·computed 확인) 3층 friction 기록. METH-130(UI repo 6곳 실설치 과제) 등록. #135는 cherry-pick 통합 후 close(스택-PR 금지 준수).
- 2026-07-29: **METH-129 전파 종결 11/11 — AI 디자인 방법론 가동 (Class A)** — #134 머지 후 sync-all: main 5곳 직접·비-main/dirty 6곳 worktree, 전부 origin 대조. 지침 25(공통 규범)·26(이미지)·27(영상)·20 v2·22 v3가 전 repo 반영 — 이제 어느 repo의 AI든 시각 산출물 작업 전 이 규범을 로드한다. 리서치(오전)→구성안 확정(사용자)→작성→전파까지 당일 완결.
- 2026-07-29: **METH-129 작성 — AI 디자인 방법론 5종 (Class A)** — 사용자 확정(5개 전부): **지침 25 AI 디자인 공통 규범**(9원칙 — 모델 추상화·캐논 우선·provenance=저작권 증빙·2단 생성·게이트 3위치·2층 검증·텍스트 오버레이·slop 금지·법무), **26 이미지·캐릭터**(역할 매트릭스·시트→레퍼런스→LoRA 사다리·검수 2단), **27 영상**(샷 스펙 YAML·5부 프롬프트·비용 공식·QA 8항), **20 v2**(§9 DESIGN.md 의무·금지 기본값·3안 픽·AI 티 테스트), **22 v3**(§7b 레이아웃 린트·taxonomy·Vega-Lite·HTML 경유 금지). README v4.3.
- 2026-07-29: **AI 디자인 방법론 리서치 (Class A, planning)** — 웹리서치 에이전트 4기 병렬(1차 출처 확인): 영상(Kling·Veo 양강, Sora 소멸 — 모델 추상화 교훈)·이미지(레퍼런스→LoRA 사다리·Midjourney 소송·Firefly 유일 면책·AI기본법 표시 의무)·PPT(Deck-as-Code 학계 검증·결정론 레이아웃 린트·Vega-Lite 차트 계층)·웹(slop 마커 규명·DESIGN.md+금지목록+3안 픽·DTCG/shadcn registry). 교차 공통 원칙 9종 + 구성안(지침 25~27 신설, 20 v2·22 v3 보강, 스켈레톤 ai-asset-pipeline). 정본: `40_dev/snapshots/2026-07-29_AI디자인-방법론-리서치.md`. METH-129(확정 대기).
- 2026-07-29: **METH-128 전파 종결 — 트리아지 12/12 전량 완결 (Class A)** — #131 머지 후 sync-all 11/11: 지침 22 v2·08 §7이 전 repo 반영, 발신 repo(icons-invest)에도 회귀 — **캡슐 루프 풀 사이클 실증**(발신→수거→트리아지→반영→전파). 오늘 하루: 역방향 루프 설계·구현·가동 + 전수조사(마찰 302건/90h+) + 채택 12건 전량 구현·전파(도구 4·지침 4·SOP 1·사용자 요청 1·복구 1·조사 1). Done 섹션은 rotate로 회전(live-archive 이관 — rotate 첫 실전 dogfood).