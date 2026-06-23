# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-040(GambleScan) + METH-041(ICONS §19 보충) + METH-042(원본 코퍼스 직접 정독 — 신규 템플릿 12종+§19 대량보강) — 같은 브랜치 `claude/inject-planning-craft-from-gamblescan` / PR #31에 묶음. 머지 전.
- **Current mode**: fullstack
- **Next TODO**: METH-040 PR 머지 후 다운스트림 `sync --apply` 전파(icons·ai-icons·gamblescan, cafe24 경로 미확인). METH-039 전파와 합쳐 1회 처리 가능.
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

- 2026-06-23: **METH-040 기획 craft 역주입 (GambleScan→방법론)** — METH-039(ICONS) 패턴의 GambleScan판. 적용 프로젝트 GambleScan 실전 풀 기획 코퍼스(methodology-v1/planning·development·docs/planning·research, ~9천 줄)를 6개 영역 병렬 학습 → 일반 craft만 역주입. **§19 없던 지침 12(운영)·14(브랜드) §19 신설 + 18(마스터플랜) §18 신설** + 기존 §19 보강(10·11·13·15) + **개발명세 템플릿 4종 신설**(data-model·user-flow·wireframe-spec·functional-spec — 기획↔빌드 빈 층). 관통 주제: 다면(N-sided) 시장 기획 + 거버넌스/추적. ICONS와 비중복. 지침 7종 +122줄 + 템플릿 4종. Class A(shared). 브랜치 `claude/inject-planning-craft-from-gamblescan` → PR #31. 머지 후 다운스트림 sync(METH-039 전파와 합산).
- 2026-06-23: **METH-042 원본 기획 학습 코퍼스 직접 정독 역주입** — 사용자 "ICONS가 학습한 *원본*(다운로드 사업기획학습·서비스기획학습 510종)을 너도 직접 학습하라". ICONS 정제본(2차 lossy)이 흘린 craft를 원본 직접 정독으로 회수(office 84종 변환, 6 클러스터 병렬). **신규 템플릿 12종**(제안·검수·운영·수익관리 — proposal-go-nogo·profitability-sheet·qa 3종·operation-spec·post-launch-monitoring·work-request-ticket·research-collection·glossary·execution-plan·microcopy) + 지침 10/11/13/15 §19 대량 보강 + 16 §15 신설. 방법론에 거의 빈 영역(제안/검수/수익) 채움. 지침 5종+템플릿 12종 ~538줄. Class A. PR #31에 METH-040/041과 묶음. 머지 후 다운스트림 sync.
- 2026-06-23: **METH-041 ICONS §19 압축 누락 보충 (METH-039 후속)** — 사용자 "icons에서도 역주입" 지시. 확인 결과 ICONS 기획 학습(`icons:40_dev/knowledge/` 01~05 + 학습보고서)은 **이미 METH-039(PR #30)로 주입 완료**된 출처. 단 압축 시 "이름만 남고 본문 증발"한 체크리스트 6건 발견 → 지침 10/11/15 §19에 보충(협업·커뮤니케이션 KJ법·블루캡, Exec Summary 8칸, 서비스정의 3종·UIUX 7루브릭·용어사전/페이퍼목업, WBS 3계층·제안서 3 Style·품질검토 8항목). 마케팅 13 완전 커버라 제외. PR #31에 METH-040과 묶음(동일 §19 섹션 충돌 회피). Class A.
- 2026-06-23: **METH-039 기획 craft 역주입 — PR #30 머지 완료** — 적용 프로젝트 ICONS의 기획 학습 정제본(`icons:40_dev/knowledge/` 6종)을 방법론으로 환류. 지침 10/11/13/15에 §19 "실무 craft 부록" 추가(핵심가치 도출·검증 우선순위 게이트·KPI 트리·ASIS→TOBE·12단계 산출물·데이터 무결성·Triple Media·4유발 퍼널·WBS·제안 5단계) + `50_resources/templates/` 기획 양식 6종(requirements/ia/service-policy/user-story/kpi-tree/wbs) 신설. 일반 craft만(프로젝트 특화 제외)·출처 명시. Class A(shared). [PR #30](https://github.com/YunJuniverse/methodology/pull/30) 머지(2026-06-23 05:25 UTC, main `2c6e60c`), `origin/main` 동기. **잔여**: 다운스트림 `sync --apply` 전파(icons·ai-icons·gamblescan, cafe24 경로 미확인).
- 2026-05-18: **Human 잔여 종결 — METH-036/038 완전 마감** — 사용자 보고 "휴먼작업 모두 완료" → 검증: gamblescan `_start/.cache/dashboard.html` ✅ untracked(`git rm --cached` 완료, METH-036 마감), talmocom methodology.py 픽스 2/2·`build:"next build"` 확인(ship 실측 정상 전제 충족, METH-038 마감). PR #27(픽스)·#28(기록) 머지·pull 완료, 브랜치 origin/main 동기(ahead 0). 이번 세션 작업(METH-038/037/036/018) 전부 main 안착·종결. 활성 백로그 비움 — 다음 후보 S-021 코드 sprint.
