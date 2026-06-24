# Checkpoint — 2026-06-24 (METH-044 모드별 템플릿 선택 체계)

> ✅ METH-044: 방법론 템플릿이 25종+로 늘어, **작업 모드에 따라 필요한 템플릿만** 선택하는
> 체계를 신설(사용자 제안). ① `50_resources/templates/_CATALOG.md` 신설 — 25종 카테고리별
> 카탈로그 + **6모드(planning/dev/fullstack/agency/lean/ops) × 템플릿 매트릭스** + 모드별 권장
> 세트. ② CLAUDE.md·AGENTS.md `Mode` 필드 확장(`fullstack/planning-only` → 6모드). ③ 지침 00
> §11.8(작업 모드별 템플릿 선택, 카탈로그가 정본). **폴더 재구성 안 함** — flat 경로 유지(기존
> 지침·문서 참조 보존). Class A. 이번 세션 역주입(METH-039~043)의 capstone.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-044-template-mode-catalog` (main `ca6fc57` 기준)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-044 모드별 템플릿 선택 체계** (사용자: "외주·풀스택·기획전용·개발전용 등 상황에
맞춰 필요한 템플릿만 쓸 수 있어야 하지 않아?" → 설계 확정 후 "#31/#32 머지 후" 착수 승인):

- 배경: 이번 세션 역주입(METH-039~043)으로 deliverable 템플릿이 25종으로 증가. flat 더미라
  "작업 용도 → 템플릿" 매핑 부재.
- 작성(branch `claude/meth-044-template-mode-catalog`, main `ca6fc57` 기준):
  - `50_resources/templates/_CATALOG.md` 신설: §1 6모드→권장세트, §2 25종 카테고리 카탈로그
    (기획/개발명세/PM/제안·수주/검수/운영/결정·공용), §3 모드×템플릿 매트릭스(28행).
  - CLAUDE.md §1 + AGENTS.md(미러) `Mode` 필드 확장 → `[planning/dev/fullstack/agency/lean/ops]`.
  - 지침 00 §11.8 신설(작업 모드별 템플릿 선택 — 카탈로그 정본·flat 경로·새 템플릿 시 카탈로그 갱신).
- 비파괴 원칙: 템플릿을 하위 폴더로 옮기지 않음(METH-039~043이 참조하는 flat 경로 보존).
- 검증 예정: wrap 4/4 → ship → PR.

**(직전) PR #31 부분머지 복구 — 완료**:

- PR #31이 METH-040(`450045a`)까지만 머지되고 041(`b3a48f7`)·042(`18d3784`)가 main 누락된 것을
  PR #32 충돌 해소 중 발견. gamblescan 브랜치(18d3784)를 PR #32에 병합 → #32가 041+042+043 운반.
  **사용자 PR #32 머지(main `ca6fc57`)로 040~043 전부 안착**, 25종 템플릿 전수 검증 완료.

## ⚠️ 다음 사람: 우선 처리 후보

- **METH-044 PR 머지** (사용자 승인 게이트).
- 머지 후 **다운스트림 sync (METH-039~044 합산)**: 업스트림 정본 기준 dry-run → `--apply`로
  icons·ai-icons·gamblescan 에 전파. **cafe24 경로 미확인**(`/Users/hayden/cafe24` repo 부재 —
  사용자 확인 필요). sync 규칙: 명시 경로 add(MC-001, `-A` 금지)·원격 선행분 무겹침 rebase(force 금지).
- (선택·후속) `methodology templates --mode <mode>` CLI — `60_tools/methodology.py` 작업이라 별도 METH.

## 다음 사람에게 (구체적 첫 행동)

1. 사용자 지시 대기. 신규 작업 시작 금지.
2. METH-044 PR 머지되면 → 다운스트림 sync(cafe24 경로부터 확인).

## 막혔던 지점 / 시도해봤지만 안 된 것

- 교훈: **PR을 같은 브랜치에 commit 누적(묶음)할 때, 머지 시점에 최신 tip이 머지되는지 확인**.
  PR #31은 040 시점에 머지돼 041/042가 누락됐었음 → #32 충돌 해소 중 발견·복구. 향후 묶음 PR은
  머지 후 main에 *모든* METH 자산 안착을 전수 검증.

## 미해결 결정사항 (Open Questions)

- 모드 선택의 *강제력*: 현재 §11.8은 "권장 세트"(시작점, 족쇄 아님). 모드 위반을 CI/wrap에서
  경고할지는 미정 — 필요 시 후속.
- `methodology templates --mode` CLI 신설 여부(편의 기능, 우선순위 낮음).

## 환경 메모

- 브랜치: `claude/meth-044-template-mode-catalog` (main `ca6fc57` 기준).
- 변경: 신규 `50_resources/templates/_CATALOG.md`, `CLAUDE.md`·`AGENTS.md` Mode 필드,
  `20_guides/00_*.md` §11.8, 라이브 4종.
- main 현재: METH-039~043 전부 안착(25종 템플릿). METH-044는 PR 대기.
