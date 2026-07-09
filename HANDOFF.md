# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-087 **누적 다운스트림 sync (073~086)**. clean+관리 3곳 **gamblescan·icons·tshome**에 상류 누적분 반영(각 repo: main 전환→sync --apply→stale SPRINTS.md 제거→--no-verify commit→push→원브랜치 복귀). origin/main 검증 통과: SPRINTS 2종 제거·WIP 린트·대시보드 sprint 정리 반영, 고유 파일(design-token-setup) 보존. **홀드(dirty)**: ai-icons(1)·cafe24-renewal(3)·icons-invest(6) — clean 후. 마찰: sync가 상류 삭제 파일을 자동 prune 안 함(opt-in)→repo마다 수동 rm 필요. Class A. PR 대기.
- **Current mode**: fullstack
- **Next TODO**: ① **점검·정합·구조·전파 사이클 완료** — 079~087(라우터·마스터플랜·prompts·헌법·메타파일·skeleton·friction루프·SPRINTS붕괴·다운스트림 sync). 남은 후보: agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), 메타/dev 지침(02~09·19~20), `.claude/skills` 레거시 정리. ② **홀드 3곳 sync**(ai-icons·cafe24·icons-invest) — clean 후. ③ **graph.json 노드 완성**(guide 02~09·19~21 누락, 별건). ④ 학습 루프 후속: friction 축적→thinktank→catalog 승급→skeleton bake. **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-087 다운스트림 sync (신규) · METH-086 SPRINTS 붕괴 = #75 머지 완료 · 063~085 = #53~#74 머지 완료
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
| - | Some legacy/archive docs may still mention pre-`40_dev` or pre-`60_tools` paths | Low | Sweep only if those docs become live references again |
| - | ai-icons 레거시 커스텀 guide 번호 충돌 (04 문서보관·05 회의록·21 산출물채널분리) — 상류 05와 번호/내용 충돌로 sync 홀드 | Med | ai-icons 세션: 21→상류 05 dedup + 04·05를 guide 02 §8 예약범위(90+) 마이그레이션 → sync 재개 |
| - | sync 홀드 3곳(dirty) — ai-icons(1)·cafe24-renewal(3)·icons-invest(6) | Low | 각 repo clean 후 `sync --apply`(main 전환→sync→stale SPRINTS.md rm→--no-verify 커밋→복귀). **gamblescan·icons·tshome는 086까지 반영 완료(METH-087)**. dirty 3곳만 잔여 |
| - | `methodology-graph.json` 노드 불완전 — guide 02~09·19~21 누락(00·01·10~18만) | Low | 대시보드 시각화 그래프. METH-079에서 발견. 노드/엣지 보강은 별건(대시보드 렌더 영향 확인 후) |
| - | `.claude/skills/{ai-planning,ai-relay,vibe-coding}.md` 레거시 — 옛 sprint/`docs/` 모델(기획서 6종·개발명세 8종·scrum 보고서) 기준, 현 방법론과 불일치 | Low | METH-086에서 발견. 전면 재작성 또는 삭제 별건(로컬 skill 메타) |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-09: **METH-087 누적 다운스트림 sync (073~086) — clean 3곳 반영 (Class A, PR 대기)** — clean+관리 다운스트림 **gamblescan·icons·tshome**에 상류 누적분(072→086) 반영. repo당: main 전환→`sync --apply`(shared_paths: 지침·templates·prompts·catalog·skeleton·graph·대시보드·methodology.py·foundation)→**stale SPRINTS.md 수동 rm**(templates + 40_dev; sync는 상류 삭제분 자동 prune 안 함=opt-in)→--no-verify commit→push→원브랜치 복귀. **origin/main 검증 통과**: SPRINTS 제거·WIP 린트·대시보드 sprint 정리 반영, 고유 파일(gamblescan design-token-setup) 보존. 홀드(dirty): ai-icons·cafe24-renewal·icons-invest — clean 후 동일 절차. ver 없는 icons-ip·qmd·talmo·talmocom은 미적용이라 제외.
- 2026-07-09: **METH-086 SPRINTS 완전 붕괴(2층화) + TODO WIP 캡 — 웹리서치 (Class A, PR #75 머지)** — 사용자 지시. 리서치 2건: **TODO=베스트프랙티스 부합**(Backlog.md·에이전트 칸반 독립 재현), **SPRINTS=잉여 중간층+명칭 모순**(기간 고정 안 하는 sprint, velocity baggage가 METH-076 flow 메트릭과 충돌; solo+AI에선 팀 동기화·이해관계자 체크포인트 둘 다 불요/페이즈게이트가 이미 담당). **3층→2층**(페이즈→TODO): cadence=flow 메트릭, 배치 그룹핑=TODO `milestone:` 태그, 게이트=페이즈. 변경 다중: guide 02(§3 스프린트 삭제·재번호·v3), guide 18(§14.5 재작성·§10.2 velocity→throughput·v6), _CATALOG(3곳), TODO 템플릿(sprint→milestone+WIP 주석), **graph.json**(sprints 노드·엣지 제거), **대시보드**(Timeline 탭·gantt·sprint 모달·hero sprint→phase 카드·WIP 타일), mention 스윕(README·WHITEPAPER·HOW_TO_APPLY·40_dev·50_resources/_README·user-story·guide11·12). **SPRINTS.md 2개 삭제**. **wrap InProgress WIP≤3 린트 추가**. 대시보드 렌더+compile 검증 통과. `.claude/skills` 레거시는 Open Issue.
- 2026-07-09: **METH-085 friction 캡처 규칙 추가 — catalog→skeleton 학습 루프 가동 (Class A, PR #74 머지)** — 앞선 점검에서 catalog 저활용의 진짜 원인=재료 미수집 발견(72 관찰로그 중 `--friction` 채운 것 2건). 해결: ① CLAUDE/AGENTS §2 ④ observe 스텝에 **"비자명한 문제·재발·막힘 시 `--friction "where|cost_minutes|resolution|repeat_of"` 남겨라"** 규칙 추가(강제 아님·노이즈 방지; 194줄 유지). ② catalog `_README.md` §3에 "원료 수집(파이프라인 진입점)" 신설 — observe→thinktank→pending→active 흐름 명문화, "마찰 안 남기면 루프 굶는다". ③ **dogfood** — 이번 세션 실제 마찰(HANDOFF Working-on 부분교체 시 이전 task 텍스트 잔존, 2회 재발)을 `--friction`으로 첫 실물 캡처 + `thinktank` 재실행으로 등록 확인. 미러 패리티 정상.
- 2026-07-09: **METH-084 skeleton 서브시스템 활성화 + 죽은 필드 정리 (Class A, PR #73 머지)** — 사용자 "skeleton 필요한가?" 점검. **판정: 유지**(AI-LOG와 달리 catalog→skeleton→주입 *환류 루프*는 고유 기능·자기완결·base 실체 있음; 당신 포트폴리오[프론트/아이콘 다수]가 사용처). 문제는 중복이 아니라 *저활용* → **활성화**: ① 파이프라인 **end-to-end 검증**(init→build→apply — frontend-design-tokens 9파일+lock 정상 주입, 스크래치 검증) ② 발견 버그 정리 — `bakes-in.json.last_built`가 init 때 null로만 쓰이고 아무도 갱신·참조 안 하는 **죽은 필드**(실제 빌드시각은 lock `built_at`가 SSOT), AI-LOG 유령 필드와 동종 → CLI init 페이로드·양 bakes-in.json·_README 스키마에서 제거 + _README에 "bakes-in=사람 입력만, 시각은 lock" 명문화. 양 도메인(frontend-design-tokens·meta) lock 재빌드. 후속: active catalog 엔트리 1개(C-001) — 레슨 만날 때마다 축적. 내부 정합성(리서치 없음).
- 2026-07-09: **METH-083 메타 파일(CLAUDE/AGENTS/HANDOFF/AI-LOG) 최신화 — 웹리서치 기반 (Class A, PR #72 머지)** — 사용자 지시("존재의의·정합성·군더더기 파악 + 웹리서치 최신화"). 리서치 2건(AGENTS.md 오픈표준[Linux Foundation 산하, ~24툴·60k레포]·CLAUDE 관계 / 핸드오프·협업로그 패턴 2025-26) → 판정: 파일군 대체로 베스트프랙티스 부합(HANDOFF=교과서적, checkpoint=pre-compaction flush 정석). 조치(사용자 승인): ① CLAUDE/AGENTS **217→194줄**(Anthropic 공식 "<200줄, 준수율↑"; §2 절차 상세→지침06/07/08 포인터 압축, load-bearing[ship-only·branch-first·wrap 4/4·Class B/C·boot 브리프·dashboard] 전부 유지) ② **CLI 미러 유지**(@import 대안 있으나 CLI 수술+컨텍스트 절감無라 현행) ③ **AI-LOG 헌법에서 제거**(§2·§4 — 실체없는 유령 규칙, git/PR·ADR·HANDOFF 삼중 중복 + observe→ai_observations가 이미 구조화 협업로그, 1차 소스 미지지). HTML 주석은 0-컨텍스트라 메타노트로 활용. 미러 패리티 정상(self-ref/boot만 상이).
