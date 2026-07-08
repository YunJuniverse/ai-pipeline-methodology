# Checkpoint — 2026-07-08 (METH-063 사업기획서 문서 디벨롭)

> ✅ METH-063: "문서 하나하나 고찰·디벨롭" 프로그램의 1번 대상 = 사업기획서. 웹리서치 → 고찰 → 제안 P1~P4 전체 반영.
> 핵심 발견: **지식(craft §19)이 구조(스켈레톤·§8 목차)보다 앞서 있었음** → craft를 1급 섹션으로 승격.
> 🏁 다음: PR 리뷰·머지. 이후 문서별 심화 계속(서비스기획서 등 다음 대상 선정).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자

- Agent: claude-opus-4-8
- Tool: claude-code-cli
- Host: darwin-25.5
- Worktree: branch `claude/meth-063-business-plan-revamp` (main 직접 PR — 스택 금지)

## 부팅 계약

1. Read `.ai/context.json`.
2. Read every path in `must_read` in order.
3. Use `last_session.checkpoint_file` (= 이 파일)를 즉시 인계로.
4. "다음 사람에게" 첫 항목부터 시작.

## 방금 한 것 (정확히)

**METH-063 — 사업기획서 문서 디벨롭** (사용자: "이제부터 문서 하나하나 고찰·디벨롭"):

- **방법**: 웹리서치 서브에이전트로 1차 소스 비교(YC=사업계획서 안 읽음, Lean Canvas 권장 / Sequoia 10파트 / SBA 9섹션 / Lean vs BM Canvas / K-Startup **PSST** 정부지원 표준 4부) → 우리 지침10(738줄)+스켈레톤 고찰 → 갭 가설 8개 검증 → 제안 P1~P4.
- **핵심 발견**: 우리 craft §19(단위경제 트리·검증게이트·bottom-up TAM·Exec Summary 8칸·N-sided)는 이미 강함. 문제는 **스켈레톤·§8 목차가 그걸 강제하지 않음** → 대부분 "승격"이지 "발명"이 아님.
- **변경 (지침 `20_guides/10_사업기획서_작성_지침.md`)**:
  - **P1 척추**: §8.1을 problem-first(문제→왜지금→솔루션→시장→BM→경쟁→팀→재무→자금/로드맵)로 재정렬. 신설 §6.16 왜지금·§6.17 트랙션/검증·§6.19 팀-as-thesis, §6.2 TAM/SAM/SOM bottom-up 강제, Exec Summary를 §0로 선두화.
  - **P2 청중 변형**: §8.4 PSST(정부지원 — 문제인식/실현가능성/성장전략[자금집행]/팀, §8.1과 1:1 매핑) + §8.5 IR(트랙션·회수 강조). 지원사업↔IR 강조점 차이 명시.
  - **P3**: §16 품질 5대 크로스체크(bottom-up 시장·명명된 why-now·실제 마진·트랙션·가정/비목표) + §9.10 비목표.
  - **P4**: §18.4 1페이지 캔버스 옵션(Lean Canvas=PMF전 / BMC=운영·소통).
  - 부속: §6.18 자금조달(조건부)·§9.11~9.13 작성기준·§19.14 근거우위·§19 환류 노트.
  - **스켈레톤 `30_planning/10_사업기획서.md`**: 척추에 정합하도록 16섹션 재작성(각 섹션에 지침 §참조 주석).

## 다음 사람에게 (구체적 첫 행동)

1. METH-063 PR 리뷰·머지.
2. **문서별 심화 프로그램 계속** — 다음 대상 사용자와 합의(후보: 서비스기획서·요구사항정의서·정책정의서). 같은 패턴(현행 고찰 → 웹리서치 → 제안 → 반영).
3. guide 09·21 + api-contract를 다음 다운스트림 sync 대상에 포함(shared_paths 확인).
4. METH-060 잔여: ai-icons 번호 정리(별건 repo 세션) + cafe24·icons-invest clean 후 sync.

## 미해결 결정사항 (Open Questions)

- 사업기획서에 캔버스(P4)를 *별도 템플릿 파일*로 뽑을지 vs 지침 내 옵션으로 둘지 — 현재는 지침 §18.4 옵션. 실사용에서 캔버스 수요 잦으면 `lean-canvas.md` 템플릿 신설 검토.
- 문서별 심화의 산출물 표준: 지침 개정 + 스켈레톤 정합이 이번 패턴 — 다음 문서도 동일 적용할지 확정.

## 환경 메모

- 브랜치: `claude/meth-063-business-plan-revamp` (main 기준). main 직접 PR(스택 금지).
- 변경: `20_guides/10_사업기획서_작성_지침.md`(§6·§8·§9·§16·§18·§19) + `30_planning/10_사업기획서.md`(재작성) + 라이브 4종.
- 선행 061·062는 PR #51·#52로 머지 완료(main 반영).
