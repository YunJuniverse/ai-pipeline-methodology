# Checkpoint — 2026-07-25 (METH-116 IR·사업기획 덱 제작 지침 신설)

> ✅ 지침 22 신설 완료 — `icons-invest` IR 덱 v1→v4 제작 회고를 방법론으로 환류. Deck-as-Code 파이프라인 + 재사용 스켈레톤 `ir-deck-build`. branch `docs/guide-22-ir-deck-methodology`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `docs/guide-22-ir-deck-methodology` (base=main d235975, branch-first)

## 방금 한 것 (이번 세션)

- 사용자 요청: `icons-invest`의 대량 IR/사업기획 작업을 읽고 "IR·사업기획 PPT 제작 방법론"으로 디벨롭.
- `icons-invest/40_dev/snapshots/IR/` 통독: 리서치 3종(AI-PPT-방법론·PPT-시각디자인·트렌드), python-pptx 빌드 시스템(43장 v4 — 디자인 토큰 상단 고정+헬퍼+차트 xlsx→PNG), 멀티에이전트 실사 패널(토론결과 4렌즈), 100여 관찰/마찰 로그.
- 사용자 선택(AskUserQuestion): **이 repo 정식 가이드 + 실행 플레이북 깊이**.
- 신설: `20_guides/22_IR_사업기획_덱_제작_지침.md` — Deck-as-Code 5단계(P0 정본화·P1 아웃라인 게이트·P2 디자인 계약·P3 코드 주입·P4 렌더검증)·디자인 계약(색3·타입6·강조예산)·검증 게이트 4종+실사 패널·정직성 규율·함정 체크리스트. 지침 20의 덱 레이어 자매.
- 신설: 스켈레톤 `50_resources/skeletons/ir-deck-build/`(base: contract.py·build.py·textbook.template.md·panel-prompt.md·_data). 스크래치 실행 검증 — 2장 빌드·geometry check 통과(전면 배경 오탐 제외 수정)·soffice 미설치 시 우아하게 skip.
- 인덱스 갱신: `20_guides/README.md` §3.6 산출물 craft 카테고리 신설·현황표·변경이력 v4.1.

## 다음 구체 행동

1. 이 PR(`docs/guide-22-ir-deck-methodology` → main) 머지 → METH-116 종료.
2. 머지 후 sync-all로 다운스트림 전파(가이드 22·스켈레톤 = 상류 00-89 소유 shared). `icons-invest`에도 역으로 들어가 그 repo IR 작업이 방법론 정본을 참조.
3. (선택) `icons-invest` IR 마찰이 반복 검증(N≥2)되면 Catalog 엔트리 C-NNN 승급 → 스켈레톤 bakes-in 합류.

## 막힌 것
- 없음.

## 환경
- macOS, python3 + python-pptx 설치됨. soffice(LibreOffice) 미설치 — 렌더 검증은 그 환경에서. pytest 없음(자체 러너).
