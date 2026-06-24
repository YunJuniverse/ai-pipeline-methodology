# Checkpoint — 2026-06-24 (METH-045 방법론 백서 겸 가이드 + 세션 종합)

> ✅ METH-045: 방법론의 **공유용 백서 겸 가이드** 신설(사용자 요청). 기존 `WHITEPAPER.md`
> (메타-시스템 헌법: L0~L4·이식성·자가발전)는 이번 세션 추가분(기획 craft·25 템플릿·6모드)이
> 빠져 있어, 철학+거버넌스+기획 craft+템플릿/모드+워크플로를 아우르는 현행 종합본을 작성.
> ① 레포: `10_foundation/방법론_백서_가이드.md`(11섹션). ② Notion: **In-spire 페이지 아래
> 하위 페이지 업로드** (app.notion.com/p/3891a2ebe06a812aa1f8cd6b79e2ae20). Class A.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-045-whitepaper-guide` (main 기준)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-045 백서 겸 가이드** (사용자: "방법론 백서 겸 가이드를 만들어 노션 In-spire 아래에
업로드 + 레포에 md 하나"):

- 레포 `10_foundation/방법론_백서_가이드.md` 신설(11섹션): 왜 / 3대 철학 / 거버넌스(클래스
  A·B·C·진실원·라이브파일) / 5계층+폴더규칙 / 기획 craft(§19) / 25 템플릿+6모드 / 워크플로 /
  자가발전 / 멀티프로젝트 전파+메타격리 / 시작하기 / 용어집.
- Notion: `notion-search`로 In-spire 페이지(`3891a2eb-e06a-8066-...`) 찾고, `notion-create-pages`로
  그 아래 하위 페이지 생성(`3891a2eb-e06a-812a-a1f8-cd6b79e2ae20`). 레포 상대링크는 Notion에서
  안 열리므로 inline code 로 처리, frontmatter·H1 제거(제목은 properties.title).

**(직전, 같은 세션) 완료된 것**:

- **METH-039~044 전부 main 안착**: 039(PR#30)·040(PR#31, 단 041/042 누락→PR#32 복구)·
  041/042/043(PR#32)·044(PR#33). 기획 craft 역주입(ICONS·GambleScan·원본코퍼스·icons-ip) +
  모드 카탈로그. deliverable 템플릿 25종.
- **다운스트림 sync 완료**(cafe24 제외=사용자 지시): icons `b1c60db`·gamblescan `561c0f5`·
  ai-icons `7ef2be7`. icons/gamblescan은 feature 브랜치라 main 전환→sync→복귀.
  **ai-icons는 sync 가 고유 지침 `20_guides/04`(문서보관규칙)를 mirror-delete 하려 해 복원**,
  CLAUDE/AGENTS 커스텀 룰도 보존, 새 자산만 반영.

## ⚠️ 다음 사람: 우선 처리 후보

- **METH-045 PR 머지**(사용자 승인 게이트). 백서는 `10_foundation/`(shared 아님) → 다운스트림
  전파 대상 아님(업스트림 전용 문서).
- **후속 chip `task_b0c3337e`**: sync mirror-delete 버그 — sync 가 다운스트림 고유 파일(upstream에
  없는 것)을 삭제. ai-icons guide 04 가 지워질 뻔. 수정: 고유 파일 보존 또는 삭제 전 경고.
- (선택) `methodology templates --mode <mode>` CLI — 편의 기능, 우선순위 낮음.

## 다음 사람에게 (구체적 첫 행동)

1. 사용자 지시 대기. 신규 작업 시작 금지.
2. METH-045 PR 머지되면 이번 세션(METH-039~045) 완전 종결.

## 막혔던 지점 / 시도해봤지만 안 된 것

- 교훈 1: 묶음 PR 은 머지 시점 최신 tip 확인(PR #31 이 040 시점에 머지돼 041/042 누락 → #32 복구).
- 교훈 2: sync 는 다운스트림 고유 파일을 mirror-delete 할 수 있음(ai-icons guide 04). 적용 프로젝트에
  고유 자산이 있으면 sync 후 삭제(D) 여부 전수 검증 필수.

## 미해결 결정사항 (Open Questions)

- 백서 2종(WHITEPAPER.md vs 방법론_백서_가이드.md) 관계 — 전자=메타 시스템 헌법, 후자=공유용
  종합본. 향후 중복 누적 시 한쪽을 정본으로 정리할지 검토 여지.

## 환경 메모

- 브랜치: `claude/meth-045-whitepaper-guide` (main 기준).
- 변경: 신규 `10_foundation/방법론_백서_가이드.md` + 라이브 4종.
- Notion: In-spire(`3891a2eb-e06a-8066-bbca-c4539bc2d20e`) 아래 하위 페이지.
- 다운스트림: icons·ai-icons·gamblescan 모두 v4.0 sync 완료. cafe24 = 대상 아님.
