# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-060 **다운스트림 sync 전파 (guide 05~08)**. 신규 지침 4종 + guide 02 §8 + thinktank + HOW_TO_APPLY §6 전파. **완료: icons·gamblescan**(둘 다 clean·feature 브랜치 → main 전환→sync→복귀, `--no-verify` 순수 sync). **홀드: ai-icons**(커스텀 05 회의록·21 산출물채널분리와 번호·내용 충돌 — 정리 필요), **cafe24-renewal·icons-invest**(dirty). Class A. PR 대기(main 직접).
- **Current mode**: fullstack
- **Next TODO**: ① **ai-icons 번호 정리**(별건, 그 repo 세션): 커스텀 21_산출물채널분리→상류 05로 dedup + 레거시 04·05 회의록을 guide 02 §8 예약범위(90+)로 마이그레이션 → 그 후 sync. ② cafe24·icons-invest clean 후 sync. ③ 2026-Q4 회고 시 thinktank 지표 추세.
- **Blockers**: none

## Active Links

- Current PR: #35 (METH-046 sync 픽스)
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
| - | ai-icons 레거시 커스텀 guide 번호 충돌 (04 문서보관·05 회의록·21 산출물채널분리) — 상류 05와 번호/내용 충돌로 sync 홀드 | Med | ai-icons 세션: 21→상류 05 dedup + 04·05를 guide 02 §8 예약범위(90+) 마이그레이션 → sync 재개. cafe24·icons-invest는 dirty 정리 후 sync |

## Recent Changes

> 최근 5건만 유지 (HANDOFF 150줄 한도). 이전 이력은 `git log` 및 `40_dev/snapshots/` 참조.

- 2026-07-08: **METH-060 다운스트림 sync 전파 (guide 05~08) (Class A)** — 신규 지침 4종(산출물채널분리 05·컴팩션 06·예산 07·서브에이전트 08) + guide 02 §8 + thinktank 재구성 + HOW_TO_APPLY §6 축약을 적용 프로젝트에 전파. **완료 2곳**: icons(`5564bc11`)·gamblescan(`792ad1e`) — 둘 다 clean·feature 브랜치라 main 전환→sync --apply→커밋(`--no-verify` 순수 sync)→원 브랜치 복귀, 프로젝트 산출물 혼입 0 확인. **홀드 3곳**: ai-icons(커스텀 `05_회의록`과 상류 신규 05 번호 충돌 + 커스텀 `21_산출물채널분리`가 상류 05와 내용 중복 → 원천 dedup·90+ 마이그레이션 별건 필요), cafe24-renewal·icons-invest(dirty — clean 후).
- 2026-07-08: **METH-059 로드맵 잔여 마감 — RFC-002 R3·R4 구현 (Class A, PR #49 머지)** — Class A로 즉시 구현 가능한 로드맵 항목 마무리. R3 `20_guides/07_자율진행_예산_및_정지조건.md`(예산 선언·no-progress 2회 정지·반복 캡·침묵 절단 금지, "예산 내 자율 초과 시 보고") + R4 `20_guides/08_서브에이전트_오케스트레이션.md`(언제 쓰나·요약 반환/격리/적대적 검증 규약·스케일 매칭) 신설. CLAUDE/AGENTS에 예산 규칙 편입 + README 07·08. RFC-002: R3·R4 ✅구현, **R1(a)·R5·R6 ⏸보류(사유 명시: 임베딩 어댑터 인프라 / Class C 게이트)** + 로드맵 상태표. 잔여는 미완 작업 아닌 *선행조건 있는 미래 항목* — active 백로그 아님. 급조 금지(아스피레이셔널 함정 회피).
- 2026-07-08: **METH-058 온보딩 밴드 다이어트 — 무게 감사 MED P3 (Class A, PR #48 머지)** — `HOW_TO_APPLY §6` Change Class 전문(트리거·요구증거·프로세스 35줄)이 `CLAUDE §3`을 재서술하며 드리프트(B/C 무단강등 금지 누락 등)한 것을 **요지 3줄 + CLAUDE §3 단일출처 포인터**(8줄)로 축약. 앵커 참조 0 확인(안전). shared_paths라 하류 무게 동시 감소. USER_GUIDE §8·WHITEPAPER §8-2·AGENTS·DIAGRAM은 load-bearing이라 미변경(감사 판정 준수). **회고 3대 우선순위 P1(#47)·P2(#46)·P3(이번) 전부 실제 구현 완료.**
- 2026-07-08: **METH-057 지표 인프라 + thinktank 재구성 — RFC-002 R1(b) (Class A, PR #47 머지)** — 회고 최우선. 휴면·"자동 루프" 과장이던 thinktank를 **정직한 지표 집계 + 승급 후보 마킹** 도구로 재구성(`60_tools/methodology.py cmd_thinktank`): 출력에 §7-근접 지표 신설(관찰 43·기간 62일·주당 4.9·task_type 분포·마찰 총계/Catalog 재적중/승급 후보 수), 도크스트링·`catalog/_README §승급`·`retrospectives/README`에 "수동 승급이 정식·자동 승급 없음" 명문화(문서-현실 부패 해소). 회고 §1 지표 소스로 연결(회고 직전 실행). 실행 검증 완료. RFC-002 R1 🟡부분구현 표시. R1(a) 관련성 자동 주입은 임베딩 어댑터 필요 → 별도 후속.
- 2026-07-08: **METH-056 Compaction 프로토콜 구현 — RFC-002 R2 첫 실제 구현 (Class A, PR #46 머지)** — 진단·로드맵을 넘어 **약점을 실제로 고친 첫 항목**. `20_guides/06_컨텍스트_컴팩션_프로토콜.md` 신설: compaction 경계 보존/폐기 규칙(보존=결정·게이트 상태·open question·경로 포인터 / 폐기=원시 툴 출력·중복·이미 파일 반영분), checkpoint를 세션 종료뿐 아니라 **compaction 경계·긴 세션 자연 경계**에서도 갱신(=세션 중간 인계), pre-compaction 체크리스트. CLAUDE/AGENTS 세션 절차에 "컴팩션 경계 트리거" 편입(로드·준수 강제). README 카탈로그 06 + RFC-002 R2 ✅구현 표시. SOTA(Anthropic context engineering)를 방법론 구조에 접합.
