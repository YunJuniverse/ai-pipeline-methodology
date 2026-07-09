# Checkpoint — 2026-07-09 (METH-080 마스터플랜 SSOT 정합)

> ✅ METH-080: 마스터플랜(지침18) 역할 재점검 → **슬롯은 고유(폐기 아님)**, 단 v2 "11 기능 정의 인라인 복제"를 **ID 참조 + 페이즈 오버레이(v5)**로 완화. 15↔18 경계 재조정(METH-076 반영). 내부 정합성(리서치 없음).
> 핵심 통찰: 인라인 복제 = 개발기획서 재번들·서비스기획서 컨테이너 논쟁과 *동형 안티패턴* → SSOT("각 내용은 집 하나")로 교정.
> 🏁 다음: PR 리뷰·머지 → 남은 후보(agency/ops 템플릿·메타 지침 00·02~09·19~20) 또는 **누적 다운스트림 sync(073~080)**.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-080-master-plan-ssot-refactor` (#68 머지된 main tip 기준, branch-first 준수)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-080 — 마스터플랜(지침18) SSOT 정합** (사용자 요청: "마스터플랜 안 건드린 이유 + 역할·필요성 다시 점검"):

- **왜 안 건드렸었나**: 18은 dev-transition 밴드(18~20)라 체계적으로 심화한 *기획서 지침군(12~17)* 순번 밖 + 이미 v4로 성숙(공백 작음). 의도적 배제 아님.
- **역할 재점검 결론**: **마스터플랜 슬롯은 고유 — 폐기 아님.** "빌드 순서·페이즈(M0/M1/M2)·MVP 확정·게이트 인스턴스" 층은 10(비즈니스)·11(기능)·15(PM 표준)·16(AI명세)·SPRINTS(스프린트 일정) 어디도 소유하지 않음. HANDOFF(live churn)·SPRINTS(스프린트)·TODO(태스크) 사이 durable 빌드 전략 슬롯을 18만 채움.
- **고친 것 (설계 냄새 1건)**: v2 "11 기능 정의 *인라인 복제*" → 11↔18 이중관리·동기화 부담 = SSOT 위반. 개발기획서 재번들·서비스기획서 컨테이너 논쟁과 동형. **v5: ID 참조 + 얇은 페이즈 요약 + 11번 링크**로 완화.
  - `20_guides/18_...md`: §0 인트로 · §1 목적 · §14.1(11경계) · §16(실수 1·2) · §17 프롬프트(OUTPUT#3·RULES·BOUNDARY) · 변경이력 v5.
  - **§14.2(15경계) 재조정**: METH-076으로 15에 딜리버리 모델·플로우·DORA·OKR 추가됨 → "15=표준 정의 → 18=프로젝트 인스턴스" 4항목 명문화.
  - `50_resources/templates/MASTER_PLAN.md`: SSOT 주석 추가 + stale 경로(`docs/archive/planning-guides`→`20_guides`) 수정. (템플릿 본문은 이미 ID 참조 기반이라 구조 변경 불필요.)

## 다음 사람에게 (구체적 첫 행동)

1. METH-080 PR 리뷰·머지.
2. **심화 프로그램 현황**: 템플릿 13종(063~071)·기획서 지침군 6종(073~078)·오케스트레이션(079)·마스터플랜 SSOT(080). 남은 후보 — agency/ops 템플릿(proposal-go-nogo·qa-*·operation-spec·profitability-sheet·execution-plan·work-request-ticket·wbs·glossary), 메타/dev 지침(00·02~09·19~20). 19(클린아키)·21(개발명세)는 이미 심화됨.
3. **누적 다운스트림 sync(2차)** — gamblescan·icons 072까지 반영 → **073~080 추가 필요**. 홀드 3곳(ai-icons·cafe24·icons-invest) clean 후.
4. **graph.json 노드 완성**(별건) — guide 02~09·19~21.

## 미해결 결정사항 (Open Questions)

- 심화 프로그램을 여기서 일단락할지 vs agency/ops·메타 지침까지 이어갈지 — 사용자 판단.
- 2차 다운스트림 sync 타이밍(073~080 누적).

## 환경 메모

- 브랜치: `claude/meth-080-master-plan-ssot-refactor` (#68 머지된 main tip 기준). branch-first 준수.
- 변경: `20_guides/18_...md` + `50_resources/templates/MASTER_PLAN.md` + 라이브 4종.
- 진척: 063~071 템플릿 + 072 sync(#61) + 073~078 지침군(#62~#67) + 079 오케스트레이션(#68) + **080 마스터플랜 SSOT(이번)**.
