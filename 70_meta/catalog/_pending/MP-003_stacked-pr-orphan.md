---
id: MP-003
title: "스택 PR — base PR 먼저 머지 시 stacked PR이 stale 브랜치로 머지돼 main 미도달(고아화)"
domain: meta-methodology
status: pending
seen_in:
  - 2026-07-08
signature: "stacked PR.*base.*먼저 머지.*orphan|스택 PR.*고아|PR.*MERGED.*main 미도달"
verified_with:
  - claude-opus-4-8
deps_implicated:
  - gh CLI (pr create --base)
  - 60_tools/methodology.py ship
created: 2026-07-08
last_hit: 2026-07-08
---

## 증상

두 산출물을 관심사별 2개 PR로 나누며 **스택 구조**(PR2 base = PR1 브랜치)로 올림.
- PR1(#41, base=main), PR2(#42, base=`meth-051` 브랜치).
- #41이 먼저 main으로 머지됨 → `meth-051` 브랜치는 이미 소진.
- #42 머지 시 GitHub이 #42를 *stale한 `meth-051` 브랜치*로 머지 → 그 병합 커밋이 main에 도달하지 못함.
- **`gh pr view 42` 는 `MERGED` 로 표시하지만 main에 파일(RFC-002) 부재.** 다음 세션 sync에서야 발견.

## 근본 원인

스택 PR에서 **base PR을 먼저 머지하면** stacked PR의 base 브랜치가 갱신되지 않은 채 남아, 머지가 main이 아닌 그 stale 브랜치로 흡수된다. GitHub은 auto-retarget을 항상 하지 않으며, `MERGED` 상태는 *어딘가로* 머지됐음만 보장하지 main 도달을 보장하지 않는다.

## 솔루션 (2026-07-08 적용)

- 고아 파일을 원 커밋에서 복원(`git checkout <sha> -- <path>`) → **main 직접 PR**(스택 아님)에 재포함(METH-053/#43).

## 안티패턴 (피할 것)

- **관심사 분리를 위해 스택 PR을 쓰는 것** — 1인 워크플로에서는 이득보다 고아화 위험이 크다.
- `MERGED` 표시만 보고 main 반영을 가정하는 것.

## 예방 규칙 (권장)

- **main 직접 PR을 순차로.** 관심사가 여럿이면 첫 PR 머지를 *확인*한 뒤 다음 PR을 갱신된 main에서 분기.
- 머지 후 항상 `git checkout main && git pull` → 기대 파일 존재를 **grep/ls로 실검증**.
- (도구 후보) `ship`/PR 흐름에 "base가 main인지" 경고, 또는 머지 후 main-도달 검증 스텝.

## 관련 자료

- RFC-002 (같은 세션), 2026-Q3 회고 §3, ADR 없음(도구 가드는 N≥2 재발 시 검토)
