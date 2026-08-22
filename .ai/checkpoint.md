# Checkpoint — 2026-08-22 (지침 22 v4 land + README 정합 정정 · sync-all 전파)

> ✅ METH-116 정련을 리베이스(v2·v3 승계 통합)해 #148 land(squash 6f6aec5a). 후속으로 `20_guides/README.md` 가 본문 v4 를 못 따라간 갭(3릴리스 연속 v1 표기)을 소급 정정하고 다운스트림 전파.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `docs/guide-22-readme-v4` (base=main, branch-first)

## 방금 한 것

- **METH-116 정련 리베이스 → land**: 브랜치(정련 1커밋)가 v1 기준 §2 전면 재작성이라, 그 사이 main 에 들어온 **v2(METH-128)·v3(METH-129)** 와 정면 충돌. 한쪽 채택 시 **불변규율 4(파일=유일 소스)·5(안정 슬라이드 ID)와 P3 리드백 게이트가 조용히 유실**되는 구조여서 승계 병합으로 해소 — 6단계 모델은 브랜치 것 채택, v2 규율 승계해 **규율 6개 통합**, 리드백 게이트는 **신 P4 행으로 이관**, 변경이력 v1~v3 보존 + **v4(2026-08-22)** 추가. `wrap` 4/4 → force-push → PR #148 → CI green → `land`(squash **6f6aec5a**, maincheck 도달 ✓).
- **README 정합 정정**(본 브랜치): `20_guides/README.md` 3곳 — ① §3.6 역할 설명 5단계 → **콘텐츠·디자인 분리 6단계** ② 현황표 22 항목 **v1 → v4 · 2026-07 → 2026-08**(v2·v3 누락분 소급) ③ 변경이력 **v4.4** 추가.
- **마찰 기록**: 본문 개정(v2·v3·v4)이 인덱스(README)에 3릴리스 연속 미반영 — 관찰로그 `2026-08-22_guide-22-rebase-and-readme-v4.md` 에 friction 등록(교정안: 본문 개정 시 README 3곳 동시 정정).
- HANDOFF Recent Changes 5건으로 정리(07-25 정련 항목은 08-22 land 항목이 승계).

## 다음 구체 행동

1. 본 브랜치 `ship` → `land` (Class A).
2. **`sync-all --apply` 다운스트림 전파** — `20_guides` 가 shared_paths 라 지침 22 v4 + README 가 함께 전파된다. 비-main/dirty repo 는 기본 skip 이니 **착수 전 각 repo 상태 재확인**(METH-137 교훈 — 실행 시점에 clean 으로 바뀌어 있으면 worktree 우회 절약). 전파 후 **origin 실내용 대조**(push rc 아닌 블롭 grep, 지침 23 §1-4).
3. 스켈레톤 `ir-deck-build` 는 shared_paths 아님(`50_resources/skeletons/_README.md` 만 공유) — 다운스트림에 필요하면 별도 경로 결정 필요.

## 현재 열린 트랙 (콜드스타트용)

- **METH-134/135 잔여**: 실험 모드 첫 실전 적용 · 자율주행 첫 실주행 + 권한 allowlist.
- **METH-130**(Backlog): UI repo 6곳 방어층 설치. **METH-113**(Backlog): retrofit.
- 후속 후보: capsule 발신 시점 id 검증 · 월간 전수조사 2회차(8월 말) · graph.json outbox/collect/land 노드 · **인덱스(README) 자동 정합 검사**(본 세션 friction 파생).

## 막힌 것
- 없음. (지침 22 §1.2 서술 "디자인 계약 고정 후 콘텐츠 주입"이 신 6단계 모델과 어긋남 — 사람 확인 후 문구 정리 권장, 이전 세션에서 이월.)

## 환경
- macOS, python3. 대시보드 http://localhost:8768.
