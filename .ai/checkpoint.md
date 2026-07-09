# Checkpoint — 2026-07-09 (METH-082 운영원칙 정합 점검)

> ✅ METH-082: 헌법(지침00) 정합 점검 — 12~17 심화·신규 문서(16·17·18)·현행화(079~081) 후 헌법이 이를 모르던 drift 교정.
> 핵심 원칙(세션 관통 SSOT): **헌법은 원칙 수준 유지 — 심화 내용을 복제하지 않고 하위 지침(10~17)·라우터(01)·_CATALOG로 포인터**.
> 🏁 다음: PR 리뷰·머지 → 남은 후보(agency/ops 템플릿·메타 지침 02~09·19~20) 또는 **누적 다운스트림 sync(073~082)**.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-082-operating-principles-review` (#70 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-082 — 운영원칙(지침00, 최상위 헌법) 정합 점검** (사용자 지시 "운영원칙 점검"):

- **진단**: 헌법이 12~17 심화·신규 문서(AI기능16·평가17·마스터플랜18)·라우터/prompts 현행화를 모른 채 6종+오케 시절 상태. §5.7 frontmatter에 prompts와 *동일한* stale 경로(`briefs/updates/`).
- **핵심 판단**: 심화 내용을 헌법에 복붙하면 또 중복(이번 세션 관통 안티패턴). → **헌법은 원칙 수준 유지 + 인벤토리 완성 + stale 수정 + 정본 소스로 포인터**.
- **변경 (`20_guides/00_...운영_원칙.md`)**:
  - §1.3 문서 체계 완성 — 16·17·18·01 명시 + "작성 표준은 지침이 정본, 헌법은 복제 안 함".
  - §3.1 분류자 — AI기능(16)/평가(17)/PM(15) 추가 + **라우터 01 §5.9~5.10 disambiguation을 분류·경계 정본으로 포인터**(AI 주제 3중 경계).
  - §3.5 연계 — AI 기능 시 16+17 동시 제안(Eval-First).
  - §4.3 역할요약 — 16·17 추가 + "심화 정본=지침10~17, 헌법 복제 금지" 명문화.
  - §5.7 frontmatter — stale 경로 `briefs/updates/`→`00_briefs/current/`.
  - §11.5 — stale 카운트("개발명세 8종") 완화.
  - §17 변경이력 신설(헌법에 이력 섹션 없었음).

## 다음 사람에게 (구체적 첫 행동)

1. METH-082 PR 리뷰·머지.
2. **심화 프로그램 현황**: 템플릿 13종(063~071)·기획서 지침군 6종(073~078)·오케(079)·마스터플랜(080)·prompts(081)·운영원칙(082). **핵심·메타 문서 정합 사이클 사실상 완결.** 남은 후보 — agency/ops 템플릿(proposal-go-nogo·qa-*·operation-spec·profitability-sheet·execution-plan·work-request-ticket·wbs·glossary), 메타/dev 지침(02~09·19~20). 19(클린아키)·21(개발명세)는 이미 심화됨.
3. **누적 다운스트림 sync(2차)** — gamblescan·icons 072까지 반영 → **073~082 추가 필요**. 홀드 3곳(ai-icons·cafe24·icons-invest) clean 후.
4. **graph.json 노드 완성**(별건) — guide 02~09·19~21.

## 미해결 결정사항 (Open Questions)

- 심화 프로그램을 여기서 일단락할지(핵심+메타 완결) vs agency/ops·나머지 메타 지침까지 이어갈지 — 사용자 판단.
- 2차 다운스트림 sync 타이밍(073~082 누적).

## 환경 메모

- 브랜치: `claude/meth-082-operating-principles-review` (#70 머지된 main tip 기준). branch-first 준수.
- 변경: `20_guides/00_...운영_원칙.md`(§1.3·§3.1·§3.5·§4.3·§5.7·§11.5·§17) + 라이브 4종.
- 진척: 063~071 템플릿 + 072 sync(#61) + 073~078 지침군(#62~#67) + 079 오케(#68) + 080 마스터플랜(#69) + 081 prompts(#70) + **082 운영원칙(이번)**.
