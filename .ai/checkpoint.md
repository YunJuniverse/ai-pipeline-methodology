# Checkpoint — 2026-06-29 (METH-049 프론트엔드 디자인 토큰 시스템)

> ✅ METH-049: 지침 20(프론트엔드 디자인 토큰 시스템) 신설 + 스켈레톤 `frontend-design-tokens`(4기둥)
> + Pending Lesson P-002. 색 하드코딩·드리프트를 day-1 가드레일로 fail-closed 차단. 지침 17 §4.2를
> *시각 품질*에 인스턴스화(19=구조 품질, 20=시각 품질 자매 가드레일). **로컬 완료, 브랜치+ship 대기.**

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `main` (아직 브랜치 미생성 — ship 시 분기 필요)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-049 프론트엔드 디자인 토큰 시스템** (사용자: A/B/C 트리거 블록 제시 → AskUserQuestion에서
"Full system" + "New P-002" 선택):

- 배경: 사용자가 design-token 시스템의 A(greenfield)/B(retrofit)/C(학습훅) 트리거 템플릿을 제시했으나
  그 토대(지침 20·스켈레톤·패턴)가 레포에 미존재. 또 블록이 패턴을 "P-001"로 칭했는데 P-001은 이미
  git-write-lock → P-002로 배정.
- 변경:
  - `20_guides/20_프론트엔드_디자인_토큰_시스템_규칙.md` 신설 — 4기둥(① @theme 시맨틱 토큰
    surfaces/text/border/brand/semantic + 디자인 언어 ② cn+프리미티브 ③ 색 가드레일 ④ 제약문서).
    원칙 "이름=역할". §5에 A/B/C 운영 트리거 내장. 17 §4.2 인스턴스화(시각 품질).
  - `50_resources/skeletons/frontend-design-tokens/` 스켈레톤 — base/{theme/tokens.css(@theme,
    라이트+다크), lib/cn.ts, components/primitives/{Card,Button,Badge,index}, guardrails/
    {check-no-arbitrary-color.sh, wiring.md}, design-system.md} + bakes-in.json + README.
  - `50_resources/catalog/_pending/P-002_frontend-design-tokens.md` — Pending Lesson(N≥2 시 C-NNN 승급).
  - `20_guides/README.md` — 카탈로그(3.5)·현황(6) 행 추가.
- 검증(실측): 가드레일 스크립트 3케이스 — clean=exit0 pass / arbitrary hex+off-system 회색=exit1 fail
  (3건 모두 검출) / ALLOW_HEX 등록 hex=pass. **초안의 file-glob 버그(grep -o 출력에 `$`앵커 적용)를
  발견·수정**(--include 글롭으로 교체) 후 재검증 통과.
- 검증 완료: observe 로그 작성·라이브 4종 갱신. wrap → (사용자 검토 후) ship 대기.

## ⚠️ 다음 사람: 우선 처리 후보

- **METH-049 브랜치 생성 + ship + PR**(현재 main 워크트리에 untracked 상태 — `매 슬라이스 브랜치 먼저`
  규칙대로 분기 후 ship). Class A.
- 별도로 METH-048 PR 머지 대기(다른 브랜치).
- 전파 메모: 지침 20(`20_guides`)·스켈레톤·catalog는 shared → 다음 다운스트림 sync 대상.

## 다음 사람에게 (구체적 첫 행동)

1. 사용자 검토/승인 대기.
2. 승인 시: `git switch -c claude/meth-049-frontend-design-tokens` → `methodology.py ship -m "feat(guides): METH-049 ..."`.

## 막혔던 지점 / 시도해봤지만 안 된 것

- 가드레일 스크립트 초안이 위반을 못 잡음 — 원인: `grep -rno` 출력(`path:line:match`)에 파일확장자
  `$` 앵커 필터를 적용해 전부 탈락. → `grep --include='*.tsx' ...` 글롭으로 교체해 해결. 교훈:
  가드레일은 *반드시 더미 위반으로 실검증*(지침 20 §4 자기 규칙대로).

## 미해결 결정사항 (Open Questions)

- 스켈레톤 `base/`는 Tailwind v4 `@theme` + React 전제. Svelte/Vue 등 비-React 스택용 변종은
  *옵션 플래그*로 처리할지(스켈레톤 README §6 안티패턴: 도메인 과분리 금지) 차기 검토.

## 환경 메모

- 브랜치: `main` (미분기). ship 전 분기 필수.
- 변경: `20_guides/20_*.md`(신규) + `20_guides/README.md` + `50_resources/skeletons/frontend-design-tokens/`(신규) + `50_resources/catalog/_pending/P-002_*.md`(신규) + `50_resources/ai_observations/2026-06-29_*.md` + 라이브 4종.
