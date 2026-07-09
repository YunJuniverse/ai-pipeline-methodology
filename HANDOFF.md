# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-085 **friction 캡처 규칙 추가 — catalog→skeleton 학습 루프 가동**. 앞선 점검(catalog가 C-001 1개에 머문 진짜 원인=재료 미수집: 72 로그 중 friction 2건)을 해결. ① CLAUDE/AGENTS §2 ④ observe 스텝에 **"비자명한 문제·재발·막힘 시 `--friction "where|cost_minutes|resolution|repeat_of"` 남겨라"** 규칙 추가(강제 아님·노이즈 방지, 194줄 유지) ② catalog `_README.md` §3에 "원료 수집(파이프라인 진입점)" 명문화(observe→thinktank→pending→active 흐름). ③ dogfood — 이번 세션 실제 마찰(HANDOFF Working-on 부분교체 시 이전 내용 잔존, 2회 재발)을 `--friction`으로 첫 실물 캡처 + thinktank 재집계로 등록 확인. 내부 정합성. Class A. PR 대기.
- **Current mode**: fullstack
- **Next TODO**: ① **심화·정합·활성화 사이클 완료** — 템플릿(063~071)+지침군(073~078)+오케(079)+마스터플랜(080)+prompts(081)+운영원칙(082)+메타파일(083)+skeleton(084)+friction루프(085). 남은 후보: agency/ops 템플릿(proposal·qa·operation·profitability·execution-plan·wbs), 메타/dev 지침(02~09·19~20). ② **누적 심화분(073~085) 다운스트림 sync** — gamblescan·icons(072까지 반영됨→073~ 추가) + 홀드 3곳 clean 후. ③ **graph.json 노드 완성**(guide 02~09·19~21 누락, 별건). ④ 학습 루프 후속: friction 축적→thinktank→catalog 승급→skeleton bake. **프로세스: branch-first 준수.**
- **Blockers**: none

## Active Links

- Current PR: METH-085 friction 캡처 규칙 (신규) · METH-084 skeleton 활성화 = #73 머지 완료 · 063~083 = #53~#72 머지 완료
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
| - | METH-072 sync 홀드 3곳(dirty) — ai-icons(6)·cafe24-renewal(7)·icons-invest(8) | Low | 각 repo working tree clean 후 `sync --apply`(main 전환→sync→--no-verify 커밋→복귀). gamblescan·icons는 072까지 반영 — 073~079 추가 sync 필요 |
| - | `methodology-graph.json` 노드 불완전 — guide 02~09·19~21 누락(00·01·10~18만) | Low | 대시보드 시각화 그래프. METH-079에서 발견. 노드/엣지 보강은 별건(대시보드 렌더 영향 확인 후) |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-09: **METH-085 friction 캡처 규칙 추가 — catalog→skeleton 학습 루프 가동 (Class A, PR 대기)** — 앞선 점검에서 catalog 저활용의 진짜 원인=재료 미수집 발견(72 관찰로그 중 `--friction` 채운 것 2건). 해결: ① CLAUDE/AGENTS §2 ④ observe 스텝에 **"비자명한 문제·재발·막힘 시 `--friction "where|cost_minutes|resolution|repeat_of"` 남겨라"** 규칙 추가(강제 아님·노이즈 방지; 194줄 유지). ② catalog `_README.md` §3에 "원료 수집(파이프라인 진입점)" 신설 — observe→thinktank→pending→active 흐름 명문화, "마찰 안 남기면 루프 굶는다". ③ **dogfood** — 이번 세션 실제 마찰(HANDOFF Working-on 부분교체 시 이전 task 텍스트 잔존, 2회 재발)을 `--friction`으로 첫 실물 캡처 + `thinktank` 재실행으로 등록 확인. 미러 패리티 정상.
- 2026-07-09: **METH-084 skeleton 서브시스템 활성화 + 죽은 필드 정리 (Class A, PR #73 머지)** — 사용자 "skeleton 필요한가?" 점검. **판정: 유지**(AI-LOG와 달리 catalog→skeleton→주입 *환류 루프*는 고유 기능·자기완결·base 실체 있음; 당신 포트폴리오[프론트/아이콘 다수]가 사용처). 문제는 중복이 아니라 *저활용* → **활성화**: ① 파이프라인 **end-to-end 검증**(init→build→apply — frontend-design-tokens 9파일+lock 정상 주입, 스크래치 검증) ② 발견 버그 정리 — `bakes-in.json.last_built`가 init 때 null로만 쓰이고 아무도 갱신·참조 안 하는 **죽은 필드**(실제 빌드시각은 lock `built_at`가 SSOT), AI-LOG 유령 필드와 동종 → CLI init 페이로드·양 bakes-in.json·_README 스키마에서 제거 + _README에 "bakes-in=사람 입력만, 시각은 lock" 명문화. 양 도메인(frontend-design-tokens·meta) lock 재빌드. 후속: active catalog 엔트리 1개(C-001) — 레슨 만날 때마다 축적. 내부 정합성(리서치 없음).
- 2026-07-09: **METH-083 메타 파일(CLAUDE/AGENTS/HANDOFF/AI-LOG) 최신화 — 웹리서치 기반 (Class A, PR #72 머지)** — 사용자 지시("존재의의·정합성·군더더기 파악 + 웹리서치 최신화"). 리서치 2건(AGENTS.md 오픈표준[Linux Foundation 산하, ~24툴·60k레포]·CLAUDE 관계 / 핸드오프·협업로그 패턴 2025-26) → 판정: 파일군 대체로 베스트프랙티스 부합(HANDOFF=교과서적, checkpoint=pre-compaction flush 정석). 조치(사용자 승인): ① CLAUDE/AGENTS **217→194줄**(Anthropic 공식 "<200줄, 준수율↑"; §2 절차 상세→지침06/07/08 포인터 압축, load-bearing[ship-only·branch-first·wrap 4/4·Class B/C·boot 브리프·dashboard] 전부 유지) ② **CLI 미러 유지**(@import 대안 있으나 CLI 수술+컨텍스트 절감無라 현행) ③ **AI-LOG 헌법에서 제거**(§2·§4 — 실체없는 유령 규칙, git/PR·ADR·HANDOFF 삼중 중복 + observe→ai_observations가 이미 구조화 협업로그, 1차 소스 미지지). HTML 주석은 0-컨텍스트라 메타노트로 활용. 미러 패리티 정상(self-ref/boot만 상이).
- 2026-07-09: **METH-082 운영원칙(지침00) 정합 점검 — 인벤토리·포인터 갱신 (Class A, PR #71 머지)** — 사용자 지시("운영원칙 점검"). 12~17 심화·신규 문서(16·17·18)·현행화(079~081) 후 헌법이 이를 모르던 drift 교정. **핵심 원칙 재확인: 헌법은 원칙 수준 유지 — 심화 내용을 복제하지 않고 하위 지침(10~17)·라우터(01)·_CATALOG로 포인터**(이번 세션 관통 SSOT 주제). 변경: §1.3 문서 체계 완성(16·17·18·01 명시), §3.1 분류자에 AI기능/평가/PM + **라우터 01 §5.9~5.10 disambiguation 정본 포인터**, §3.5 연계 16+17 동시 제안, §4.3 역할요약 16·17 추가 + "심화 정본=지침10~17, 헌법 복제 금지" 명문화, §5.7 frontmatter stale 경로(`briefs/updates/`→`00_briefs/current/`, prompts와 동일 drift) 수정, §11.5 stale 카운트 완화, §17 변경이력 신설. 내부 정합성(리서치 없음).
- 2026-07-09: **METH-081 prompts/ 층 전면 현행화 — drift 해소 + _README 신설 (Class A, PR #70 머지)** — 사용자 질문(운영원칙 지침00·prompts 역할)에서 프롬프트층이 나머지 방법론과 심하게 drift 발견(라우터 079 문제와 동종). **구모델→현모델**: 입력 `briefs/`→`00_briefs/current/`, 산출 `40_dev/snapshots/plans/xxx/vN`→`30_planning/NN_*.md`(라이브 in-place), "항상 6종"→모드 선택 로딩. **목차 복제 제거**(구조 SSOT=지침, METH-080과 동일 교정). 기획서 프롬프트 6종(business/service/ops/marketing/brand/pm) 재작성 + **ai-feature(16)·eval-guardrail(17) 신설**(기획서 8종 전체 커버) + 코드-역문서화 4종(architecture/data-model/api-spec/service-spec) 역할 명확화(전방 설계=템플릿 vs 역문서화=프롬프트) + dev-spec 현행화(지침21·개발명세 5종·planning-handoff) + plan-routing/re-plan/plan 현행화 + **`_README.md` 신설**(프롬프트↔지침↔템플릿↔모드 매핑, _CATALOG 대응). 상위 문서(README·50_resources/_README "스냅샷 생성"→"AI 실행 프롬프트") 정정. 17개 파일. 내부 정합성(리서치 없음).
