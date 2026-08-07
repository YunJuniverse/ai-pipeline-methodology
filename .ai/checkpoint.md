# Checkpoint — 2026-08-07 (자율 범위 확장 — land · 실험 모드 · 자율주행)

> ✅ METH-132 CI 복구 종결(main CI green 회복). METH-133/134/135 구현 완료, **PR 대기**.
> ⚠️ **Done 전이는 이 PR 머지 + maincheck 이후** — 지금은 InProgress가 정확한 상태다.

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `feat/land-lab-autopilot-20260807` (base=main, branch-first — #139 머지 후 main에서 새로 분기)

## 방금 한 것

1. **METH-132 종결** — CI `validate`가 #136~#138 main red였던 것 복구(#139 머지). `maincheck addfb63 ✓`, main CI `conclusion=success` 실측.
2. **사용자 결정 2건 수령** — 자동 머지 = *Class A + CI green 필수* / 실험 모드 = *샌드박스 경계 + 졸업 게이트*. 근거는 ADR-004에 박제(Class C 승인 증거).
3. **METH-133 `land` 구현** — `cmd_land` 6단계(PR 식별 → Class 판정 → CI green → squash 머지 → 기본 브랜치 동기화 → maincheck), 전부 fail-closed. `ship --land` 연결. Class B/C 경로 판정기 7종 더미 위반으로 실효 증명(지침 23 §1-3).
4. **METH-134 지침 28**(실험 모드) · **METH-135 지침 29**(자율주행) 신설 + CLAUDE.md/AGENTS.md §2 진입 규칙 + guides README 카탈로그.
5. **캡슐 1건 트리아지 종결** — `land-command-post-merge` 유효 → 반영 완료 → `_inbox` 정리(원장 유지). 잔여 14건.

## 알려진 한계 (다음 세션이 알아야 할 것)

- **Class 판정은 경로 패턴 기반이라 의미적 정책 변경을 못 잡는다.** 이 PR 자체가 거버넌스 변경인데 경로상으론 Class A로 보인다. land 는 "사람 판단의 대체"가 아니라 "기계로 확인 가능한 것만 자동화"다. 패턴을 넓힐 땐 **신규 적중분 전수 재측정 후**(캡슐 `measure-before-widening-a-guard`).
- **지침 29는 아직 실주행 검증 전.** 사이클 45~90분 환산치는 추정이다. 첫 실주행에서 실측해 v2로 환류.
- **무인 자율주행은 권한 allowlist 없이는 못 돈다** — settings.json 정리가 METH-135 잔여 항목.

## 다음 구체 행동

1. **`python3 60_tools/methodology.py land`** 로 이 PR 머지 — end-to-end 증명이자 METH-133 acceptance 마지막 항목.
2. 머지·maincheck 확인 후 **METH-133/134/135 Done 전이** + `sync-all` 로 12개 repo 전파(지침 28·29는 shared 경로).
3. METH-131 캡슐 14건 트리아지 — 우선순위: invest-ops `tool/ship`·`tool/hooks` 2건(land 와 한 세트였음) → CROSS-REPO 3묶음(guide-23 x4·07 x2·19 x2) → catalog 재발 건.
4. METH-135 첫 실주행 검증(사이클 환산 실측) · 권한 allowlist.

## 현재 열린 트랙 (콜드스타트용)

- **METH-133/134/135**(InProgress): 구현 완료, PR 머지 대기.
- **METH-131**(Blocked): 캡슐 트리아지 14건.
- **METH-130**(Backlog): UI repo 6곳 방어층 설치. **METH-113**(Backlog): retrofit.
- 후속 후보: graph.json 에 outbox/collect/land 노드 · invest-ops `capsule_policy: restricted` · RFC-003 관찰(8/12경) · grooman sync(타 호스트) · 월간 전수조사 2회차(8월 말).

## 막힌 것
- 없음.

## 환경
- macOS, python3. 대시보드 http://localhost:8768.
