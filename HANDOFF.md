# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: **다음 작업 대기.** 직전 완결: METH-148 캡슐 6회차 — 10건 반영(도구 2·지침 6·ADR-005·C-003·P-009)·전파 11/11(#178~#182).
- **Current mode**: fullstack
- **Next TODO**: **METH-135 첫 실주행 검증**(사이클 45~90분 환산 실측 → 지침 29 v2 환류) · 무인 권한 allowlist(settings.json) · METH-134 실험 모드 첫 실전 적용. 다음 캡슐 수거는 다운스트림 축적 후(주기 약 1주). 후속 후보: capsule 발신 시점 id 검증(워크트리 접두어 경고 — METH-140 이전 발행분이 이번 수거에도 1건) · 월간 전수조사 2회차(8월 말). **프로세스: branch-first · 세션 종료 = ship → land.** 상세는 checkpoint.
- **Blockers**: none. (METH-148 판단 3지점·법무 안내 변경 2026-09-21 사용자 승인.)

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
- 2026-09-21 — **METH-148 종결·전파 11/11**: 재시도는 bash 스크립트로 SHA 검증. 알릴 것 2: ① ai-icons 로컬 main 이 미푸시 커밋 3개로 원격과 갈라져 있음(다른 세션) ② ai-icons 리서치의 HunyuanVideo «Apache-2.0» 은 오기(원문은 한국 제외 라이선스) — 그 repo 문서는 그 세션 몫.
- 2026-09-21 — **METH-148 첫 전파 실패·복구**: zsh 가 `$P` 를 나누지 않아 11곳 모두 커밋 0건(오류는 `2>/dev/null` 에 묻힘). 진단 중 cafe24-renewal HEAD 를 실수로 한 칸 되감았다가 즉시 복구(soft, 작업 손실 0). 6곳 작업 트리 원복. 재시도 전 ADR 인용 표기도 정리.
- 2026-09-21 — **METH-148 지침·catalog**: 지침 26·27 수치를 `20_guides/_data/2026-Q3_design-tool-landscape.md` 로 분리 · **지침 26 FLUX 라이선스 문장 교체(Class C, ADR-005)** · HunyuanVideo-1.5 는 라이선스상 한국 제외(원문) · 23 §1-6 문장→도구 승급 기준 · **C-003 승급**(머지=배포 CI) · P-009(호스팅 플랫폼 관측 우선).
- 2026-09-21 — **METH-148 도구**: friction `phase` 선택 필드 · thinktank `--path`+마찰 비용 회고. cafe24 회고 수치(204건·4,684분·21%)를 표준 명령이 정확히 재현.
- 2026-09-18 — **캡슐 6회차 판정 초안(METH-148)**: 10건 실측 대조 — 유효 9·부분 이미 반영 1. 1차 출처 확인으로 **상류 지침 26 의 FLUX [dev] «출력만 상업 OK» 문장이 라이선스 원문과 어긋남** 발견(모델 구동 자체가 비상업 한정) · Sora 는 앱 04-26·API 09-24 로 양쪽 다 정확 · 머지=배포 CI 는 4개 날짜 재현으로 C-003 승급 후보.
