# Checkpoint — 2026-07-28 (METH-117 백로그 등록 — 다운스트림 관찰 역수거)

> ✅ 백로그 등록 완료 — 역방향 학습 루프 갭 분석을 METH-117로 TODO 백로그화. branch `chore/backlog-meth-117-reverse-harvest`, PR 대기.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-fable-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `chore/backlog-meth-117-reverse-harvest` (base=main d0bfde4, branch-first)

## 방금 한 것 (이번 세션)

- 사용자 질문: "실제 작업 레포에서 방법론을 역으로 업데이트하는 과정이 있나?" → 분석 보고.
- 확인 결과: 설계상 루프는 존재(observe --friction → thinktank → _pending → 사람 PR → catalog → skeleton, `50_resources/catalog/_README.md` §3·백서 §6). 실작동 사례도 있음(지침 05 §유래: ai-icons N≥2 격상, 지침 22: icons-invest 회고 환류) — 그러나 둘 다 **수동**.
- 갭: `methodology.py`의 `observation_files()`(L756)가 로컬 repo `ai_observations/`만 읽음 → 다운스트림 thinktank는 자기 repo 안에서만 집계, 교차-레포 재발(repo A 1회+repo B 1회=사실상 N≥2)은 사람 기억 의존. 순방향 sync-all의 역방향(수거)이 없음.
- 사용자 지시로 **METH-117** 백로그 등록(`TODO.md` §Backlog): 역수거 명령(읽기-전용·session_id 중복 방지·출처 태그) + thinktank 교차-레포 집계(repo별 출처 표기) + 저장 위치·수명 규칙 + 자동 승급 없음 유지(백서 §8-2). METH-116은 IR 덱 지침 세션이 선점 → 117 부여.

## 다음 구체 행동

1. 이 PR(`chore/backlog-meth-117-reverse-harvest` → main) 머지 — TODO만 변경, Class A.
2. METH-117 착수는 사람이 Backlog→Ready 승격 시. 구현 진입점: `60_tools/methodology.py` `observation_files()`·`cmd_thinktank()`(L763)·`cmd_sync_all()`(L1491) 참조.
3. 별개 대기: METH-116 지침 22 PR(`docs/guide-22-ir-deck-methodology`) 머지 → sync-all 전파.

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8765 서빙 중.
