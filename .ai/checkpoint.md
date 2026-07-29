# Checkpoint — 2026-07-29 (지침 23·24 신설 — METH-123·124)

> ✅ 검증 규범·착수 게이트 지침 신설 완료. branch `docs/guides-23-24-verification-kickoff`, PR 대기. 머지 후 sync-all 전파(20_guides shared).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `docs/guides-23-24-verification-kickoff` (base=main, branch-first)

## 방금 한 것

- **지침 23 검증 규범**(`20_guides/23_검증_규범.md`, METH-123 — P4+P9+P12): §1 무음 실패 프로토콜 4규칙(0건 처리=실패·검사 못 함≠깨끗함·금지형 가드 negative case 증명·빌드 통과≠산출물 정상/리드백) §2 내용 기준 검증 3기준(비어있지 않은 데이터·최대 표시 크기·존재 아닌 내용/가시성 + 역방향 테스트) §3 검증불가 등록부(4필드·우회 사다리 4단·비-포인터 대안 동반) §4 적용 지점(wrap 자기 점검·Blocked 연결). 각 규칙에 실사고 계보(어느 repo 몇 분) 명기.
- **지침 24 착수 게이트**(`20_guides/24_착수_게이트.md`, METH-124 — P5): §1 정본 확인(과거 사실 기록물은 사용자에게·예외 박제·축 변경 시 파생 전수 재해석) §2 조사 진단 재검증(문서는 낡는다·반증 대조군·부재≠미포착) §3 해석 계약(정확구현 vs 참고·모호 요청 범위 질의·표면 진단 반증) §4 사용자 경계 원문 검증(거절 전 1차 출처) §5 상황별 착수 전 질문표.
- README: §3.6 표에 23·24 행 추가, 변경 이력 v4.2.
- TODO: METH-123·124 → InProgress(AC 전부 체크, 구현 완료 노트).

## 다음 구체 행동

1. 이 PR(`docs/guides-23-24-verification-kickoff` → main) 머지 → sync-all 전파(20_guides·README = shared) → METH-123·124 Done(maincheck 후).
2. 잔여 트리아지 산출: METH-125(스크래핑 SOP 승급+폴백 사다리)·126(CI 정합 — 지침 19 보강+스캐폴드)·127(사실주장 출처 — 지침 05 보강)·128(지침 22 보강 — _inbox 캡슐 대기). 125~127은 한 사이클로 묶을 수 있는 크기.
3. RFC-003 관찰 중 · repo 과제(비대 5곳 rotate·invest-ops restricted 등) · grooman sync.

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765.
