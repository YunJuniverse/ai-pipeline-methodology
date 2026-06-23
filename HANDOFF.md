# HANDOFF.md

> Live state file for methodology.
> Keep this file under 150 lines.
> Date initialized: 2026-05-07

- **Working on**: METH-043 icons-ip 경량 문서 craft 역주입 — PRD/ARCHITECTURE/CONTEXT 템플릿 + ADR 강화 + 경량 모드. 브랜치 `claude/inject-lean-doc-craft-from-icons-ip`, **PR #32 대기**. PR #31(METH-040/041/042) 머지 후 origin/main 머지로 라이브 파일 충돌 해소 완료.
- **Current mode**: fullstack
- **Next TODO**: ① **PR #32 머지** → ② **다운스트림 sync**(METH-039~043 합산: icons·ai-icons·gamblescan `sync --apply`, cafe24 경로 미확인) → ③ **METH-044**(모드별 템플릿 카탈로그 capstone — TODO Backlog에 설계 확정).
- **Blockers**: none

## Active Links

- Current PR: #32 (METH-043)
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

- 2026-06-23: **METH-043 icons-ip 경량 문서 craft 역주입 (PR #32)** — icons-ip(방법론 미적용 lean 코드베이스)의 PRD 작성 craft 중 순수 doc craft 7종 채택(GitHub-Issues 트래커는 file-based 설계 충돌이라 제외). 신규 템플릿 3종(`prd.md`·`architecture.md`·`context-glossary.md`) + `ADR-template.md` 강화(결정문장 제목·Considered Options·되돌리기 비용) + `requirements-spec.md`(M/S+Pn) + 지침 00 §11.5~11.7(경량 모드·문서 충돌 surfacing·작업유형 라우팅). Class A. PR #31 머지 후 origin/main 머지로 라이브 파일 충돌 해소.
- 2026-06-23: **METH-042 원본 기획 학습 코퍼스 직접 정독 (PR #31 머지)** — ICONS 학습 *원본*(다운로드 사업기획학습·서비스기획학습 510종) 직접 정독 → 정제본이 흘린 craft 회수. office 84종 변환·6 클러스터 병렬. **신규 템플릿 12종**(제안·검수·운영·수익관리) + 지침 10/11/13/15 §19 대량 보강 + 16 §15 신설.
- 2026-06-23: **METH-041 ICONS §19 압축 누락 보충 (PR #31 머지)** — METH-039 압축 시 "이름만 남고 본문 증발"한 체크리스트 6건 복원(지침 10/11/15: 협업·커뮤니케이션·Exec Summary 8칸·서비스정의 3종·UIUX 7루브릭·WBS 3계층·제안서 3 Style·품질검토 8항목).
- 2026-06-23: **METH-040 GambleScan 기획 craft 역주입 (PR #31 머지)** — 실전 풀 기획 코퍼스 6 영역 병렬 학습 → 일반 craft만. **§19 없던 지침 12·14 §19 신설 + 18 §18 신설** + 10/11/13/15 §19 보강 + 개발명세 템플릿 4종. 관통: 다면 시장 + 거버넌스/추적.
- 2026-06-23: **METH-039 기획 craft 역주입 — PR #30 머지 완료** — ICONS 기획 학습 정제본(`icons:40_dev/knowledge/` 6종) 환류. 지침 10/11/13/15 §19 "실무 craft 부록" + 기획 양식 템플릿 6종 신설. Class A. [PR #30](https://github.com/YunJuniverse/methodology/pull/30) 머지. **잔여**: 다운스트림 sync(METH-039~043 합산).
