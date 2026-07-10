# Checkpoint — 2026-07-10 (METH-102 라이브파일 경계 재분리 + 상시 브리프)

> ✅ **METH-102**: (b) HANDOFF(상태보드) ↔ checkpoint(서사) 경계 재분리로 중복 제거 + `00_briefs/standing/`(반복작업 SOP, boot이 ★ 항상 노출) 신설. Class A(7 repo).
> ⚠️ **#90(METH-101 boot)이 아직 OPEN**(미머지) — 이 브랜치는 #90 위에 얹혀 base=main PR에 boot+102 전부 포함. 이 PR 하나 머지하면 다 반영, #90은 close.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-102-livefile-boundary-standing-briefs` (#90/101 브랜치 위 스택, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것 (이번 세션)
**METH-102 — 라이브파일 경계 재분리(b) + 상시 브리프.** 사용자 질문("파일이 왜 이렇게 나뉘나 / 반복작업을 새 세션이 기억 못하나")에서 두 가지 도출:
- **(b) HANDOFF ↔ checkpoint 경계 재분리** (중복 제거): 둘 다 "현재 상태+인계"라 30~40% 겹쳐 이중 기입하던 것을 못박음. **HANDOFF = 누적 상태 보드**(현재포커스·오픈이슈/결정·링크·Recent terse 1줄·대시보드 파싱). **checkpoint = 이번 세션 서사 바통**(방금 한 것·다음 구체행동·막힌 것·환경, 콜드스타트·컴팩션 앵커). checkpoint의 "미해결 결정사항" 섹션 삭제(→HANDOFF Open Issues 참조). 반영처: 템플릿 2개 헤더 + CLAUDE/AGENTS §4에 checkpoint 행 신설·HANDOFF 행 타이트닝 + §2 세션종료 규칙 ②③ 경계 명기.
- **상시 브리프 신설** (반복작업 기억 구멍): 반복·정기 작업 SOP가 obs/커밋에만 흩어져 새 세션이 못 찾던 문제 → `00_briefs/standing/`(날짜없음·아카이브 안 됨) 신설, `SOP_template.md` 스캐폴드, `boot`이 ★로 항상 최상단 노출(템플릿은 필터). `00_briefs/_README`에 standing 규칙, boot 규칙·MANIFEST(shared+init) 반영.
- 검증: py_compile · boot 실행(standing ★ + current 분리 출력, 실제 SOP 뜨는 것까지) · manifest-check · managed block 동일(self-ref만 차이).

## 다음 사람에게
1. **METH-102 PR(base=main) 머지** = #90(boot)+101(사이즈린트)+102(경계+상시브리프) 전부 반영. 머지 후 #90 close.
2. ⚠️ **#90이 아직 OPEN** — 사용자가 "머지했다"고 했으나 gh 기준 미머지(#85~87에 이어 2번째). 사용자에게 실제 머지 여부 확인 권고.
3. **각 repo 세션**: 반복작업은 `00_briefs/standing/SOP_*`로 박제. ai-icons는 업무기술서 처리 SOP를 이걸로 만들면 재발 방지. + 비대 라이브파일 트리밍(101 린트).

## 환경 메모
- 브랜치: `claude/meth-102-livefile-boundary-standing-briefs` (#90/101 브랜치 위). branch-first.
- 누적 상태(오픈이슈·PR 목록)는 **HANDOFF 참조** — 여기 복제 안 함(이번 경계 규칙 dogfooding).
- 진척: 메타/dev(092-094)+agency/ops(095-098)+graph(099)+v3.2(100)+부팅/비대화(101)+**경계/상시브리프(102)**.
