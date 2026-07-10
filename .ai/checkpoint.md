# Checkpoint — 2026-07-10 (METH-100 v3.2 compat 정리)

> ✅ **METH-100**: v3.2 backward-compat 코드 제거(methodology.py·generate-dashboard.py 구조탐지·폴백 → v4.0 고정). migrations 스크립트·런처/훅 부트스트랩 탐지는 보존. py_compile·dashboard·wrap 검증.
> ⚠️ **미머지 스택 상태**: 이 브랜치는 #99(=096~099) 위에 100을 얹음. #88(OPEN)이 아직 안 머지됨. 이 PR(base=main)에 096+097+098+099+100 전부 포함 → 이거 하나 머지하면 다 반영(#88은 중복이라 close 가능).

---

> Live handoff for the next AI or person.
> Contract: keep this file under 200 lines, use repository-relative paths, and update it at session end.
> 형식 정의: `10_foundation/WHITEPAPER.md` §2-2.

## 작성자
- Agent: claude-opus-4-8 · Tool: claude-code-cli · Host: darwin-25.5
- Worktree: branch `claude/meth-100-v32-compat-cleanup` (#99 브랜치 기준=095~099 온전 보존, branch-first)

## 부팅 계약
1. `.ai/context.json` → 2. `must_read` 순서 → 3. 이 파일 인계 → 4. "다음 사람에게" 첫 항목.

## 방금 한 것
**METH-100 — v3.2 backward-compat 코드 정리.** 현존 repo 7곳 전부 v4.0이라 dead였던 v3.2 폴백 제거:
- **methodology.py**: `_LAYOUT_V32`+`methodology_layout()` 구조탐지 삭제(→v4.0 고정). `_observation_dir`/`_wrap_obs_dirs`를 50_resources/70_meta 하드코딩(40_resources/60_meta 폴백 삭제).
- **generate-dashboard.py**: `_LAYOUT_V32`+`dash_layout`+`resolve_methodology_py` 3-tier 탐지 삭제(→v4.0 고정). `_count_observations`·`assemble`의 `docs/`·`40_resources`·`60_meta`·legacy-root 폴백 삭제(v4.0 유효한 `50_resources/templates` 폴백만 유지). 푸터 "v3.2"→"v4.0"·stale 도크스트링 수정.
- **의도적 보존**: `migrations/v3.2_to_v4.0.py`(v3.2→v4.0 이관=유일 escape hatch) · 런처(_start/*)·pre-push 훅의 3-tier 탐지(Python 실행 전 툴을 찾는 부트스트랩 tolerance, 트래킹 이슈 범위 밖·synced 7곳 리스크).
- 검증: py_compile 2개 · dashboard 재생성(nodes=42, obs 카운트 107=50_resources 87+70_meta 21 양쪽 정상) · wrap.

**직전(099)**: methodology-graph.json 노드 29→42·엣지 39→53(METH-079 Open Issue 종결) + 스택-PR 함정 복구.

## ⚠️ 미머지 스택 상태 (중요)
- **#88(OPEN, base=main)**: 096+097+098+099 복구 PR. 아직 안 머지됨.
- 이 브랜치(100)는 #99 브랜치 위에 얹혀 있어 **096+097+098+099+100 전부 포함**. base=main PR 하나 머지하면 다 반영 → **#88은 중복이므로 close 가능**.
- 095만 main에 있음(#84). 나머지는 전부 이 PR에 담김.

## 다음 사람에게
1. **METH-100 PR(base=main) 머지** = 096~100 한 번에 반영. 머지 후 #88 close + origin 중간 스택 브랜치(095/096/097/099 deepen) 삭제.
2. 남은 것: 079~100 점검·정비 사이클 **완료**. 다른 repo(별도 세션): ai-icons 92 환류·talmo-com.
3. **교훈(반영됨)**: 스택-PR 재타깃 취약 → main 직행 단일 PR 선호([[prefer-main-direct-pr]] 메모리).

## 환경 메모
- 브랜치: `claude/meth-100-v32-compat-cleanup` (#99 기준=095~099 온전). branch-first.
- 진척: 메타/dev(092-094) + agency/ops(095-098) + graph(099) + **v3.2 compat 정리(100)**. 점검·정합·구조·전파·정비 사이클(079~100) **마무리**.
