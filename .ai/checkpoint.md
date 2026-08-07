# Checkpoint — 2026-08-07 (캡슐 수거 2026-08 — 15건/3 repo)

> ✅ `_inbox` 적재·원장 16건·thinktank 재집계 완료. **다음은 사람 트리아지(METH-131, Blocked)** — 판정 없이는 반영 착수 금지(백서 §8-2).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-5 · Tool: claude-code-desktop · Host: darwin 25.5.0
- Branch `chore/collect-capsules-20260807` (base=main, branch-first — 직전 브랜치는 #137로 머지 완료라 main에서 새로 분기)

## 방금 한 것

- `collect` dry-run으로 12개 repo 전수 확인 → **미수거 15건/3 repo**(gamblescan 8·lifeManager 4·invest-ops 3). icons-invest 1건은 원장에 있어 skip(중복 방지 정상 작동).
- `collect --apply` 적재 — `50_resources/meth_inbox/` 15파일, 원장 1→16건.
- `thinktank` 재실행 → `40_dev/snapshots/insights/2026-W32_thinktank.md`. 캡슐 교차 집계: **CROSS-REPO** guide-23 x4(gamblescan·lifeManager)·guide-07 x2·guide-19 x2, **DUP-TARGET** catalog x2, single 5.
- METH-131 등록(**Blocked** — 판정 주체가 사람).

## 수거분 요지 (트리아지 입력)

- **도구 3건(invest-ops, 한 세트)**: `tool/ship` Done 주장 감지+pending 원장(maincheck를 push 게이트로 넣는 안은 반대 — 브랜치 push는 항상 미도달) · `tool/land` ship의 대칭짝 신설(maincheck→Done 확정→브랜치 안전 삭제) · `tool/hooks` pre-push가 브랜치 삭제 push까지 차단해 `--no-verify` 상습화.
- **guide-23(검증) 4건**: 가드 '통과' 판정은 약함(거부 86 전부 타당 vs 통과 10 중 5 가짜) · 탐지 규칙 확장 전 신규 적중분 전수 재측정 · 성능 A/B는 워밍 후 다회 중앙값 · 픽스처에 스키마가 만드는 특이값(null→기본값) 포함.
- **guide-07(자율 정지조건) 2건**: 열린 PR 브랜치에 커밋 축적 → 고아 커밋(4회 재발) · 내가 만들지 않은 프로세스·포트 kill 금지.
- **guide-19(클린코드) 2건**: 판정 원시함수 중복 금지(가드 2개 동시 무력화 위험) · 일괄 치환은 범위 최소화+카나리.
- **catalog 2건**: "대리 신호 말고 원본 검증" — 07-31 제안이 08-07에 새 기제 2종으로 재발(누적 5실사례). 중복 아님, 승급 근거.
- **기타**: `60_tools/ship-build-guard`(--no-build 우회가 빌드 파손 은폐) · `guide-24`(이식 요청은 입력 축 실측 → 부재 크면 Class C).

## 다음 구체 행동

1. 이 PR(`chore/collect-capsules-20260807` → main) 머지 — 수거·집계 기록만, 규칙 변경 없음.
2. **사용자 트리아지**: 15건 각각 유효/이미 반영/만료 판정. 시작점 권장 = CROSS-REPO 3묶음(guide-23·07·19) → invest-ops 도구 3건 한 세트 → catalog 재발 건.
3. 유효분 반영은 main 직행 단일 PR로, maincheck 확인 후 Done 전이.

## 현재 열린 트랙 (콜드스타트용)

- **METH-131**(Blocked): 캡슐 트리아지 15건.
- **METH-130**(Backlog): UI repo 6곳 방어층 설치(axe·간격 린트·절대색 차단·프리미티브) — 더미 위반 실효 증명 필수.
- **METH-113**(Backlog): retrofit. **스켈레톤 ai-asset-pipeline**: 첫 이미지/영상 실작업 시.
- 후속 후보: graph.json에 outbox/collect 노드 · invest-ops `capsule_policy: restricted`(그 repo 세션) · RFC-003 관찰(8/12경) · grooman sync(타 호스트) · AI 디자인 도구 지형 재검증(10월) · 월간 전수조사 2회차(8월 말).

## 막힌 것
- 없음(METH-131은 막힘이 아니라 사람 판정 대기 — Blocked로 명시).

## 환경
- macOS, python3. 대시보드 http://localhost:8768.
