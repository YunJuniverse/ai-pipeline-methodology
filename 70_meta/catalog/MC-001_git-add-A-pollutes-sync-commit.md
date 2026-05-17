---
id: MC-001
title: "방법론 sync/migration commit 시 git add -A 가 빌드 산출물·OS 캐시 오염"
domain: meta-methodology
status: active
seen_in:
  - 2026-05-12
  - 2026-05-14
  - 2026-05-17
signature: "git add -A.*(\\.sanity|dist|node_modules|\\.DS_Store|build).*sync|migration.*add -A"
verified_with:
  - claude-sonnet-4-6
  - claude-opus-4-7
deps_implicated:
  - 60_tools/methodology.py
created: 2026-05-17
last_hit: 2026-05-17
---

## 증상 (Symptom)

방법론 자산을 적용 프로젝트로 전파하거나 v3.2→v4.0 마이그레이션 후 커밋할 때
`git add -A` 를 쓰면 프로젝트의 *빌드 산출물·도구 캐시* 가 함께 staging 됨:

- talmocom: 이미지/빌드 산출물 (2026-05-12, F-series)
- tshome: `.sanity/`, `dist/` (gitignore 미등록) 가 마이그레이션 커밋에 섞일 뻔함 (2026-05-17)

`.gitignore` 에 없는 산출물은 `git add -A` 가 무차별 포함 → 방법론 sync
커밋이 비대해지고 빌드 캐시가 저장소 오염.

## 근본 원인 (Root Cause)

방법론 sync/migration 은 *방법론 경로* (NN_ 폴더 + `_start` + managed
파일 + `.methodology-version`) 만 건드린다. 그러나 적용 프로젝트는 동시에
자체 빌드 산출물 (`dist/`, `.next/`, `.sanity/`, `node_modules/`) 을 가질 수
있고, 이들이 항상 `.gitignore` 에 등록돼 있지는 않다. `git add -A` 는
working tree 전체를 보므로 *방법론과 무관한 변경* 까지 commit 에 끌어온다.

## 솔루션 (Solution)

방법론 sync/migration 커밋은 **방법론 경로를 명시적으로만 add**:

```sh
git add -A 00_briefs 10_foundation 20_guides 30_planning 40_dev \
  50_resources 60_tools _start open-dashboard.command \
  CLAUDE.md AGENTS.md .methodology-version .ai .github
git add -u    # 추적 파일의 삭제/rename 만 추가 포착
# git add -A (단독) 회피 — 빌드 산출물 오염
```

커밋 전 검증:

```sh
git status --short | grep -E '\.sanity|dist/|node_modules' | grep -E '^[MARD]' \
  && echo "오염 — staged 취소 필요" || echo "clean"
```

## 안티패턴 (Anti-Pattern)

- 방법론 sync 후 `git add -A && git commit` (working tree 전체 무차별)
- `.gitignore` 가 빌드 산출물을 다 막아줄 거라 가정 (적용 프로젝트마다 다름)

## 자동화 후보

`methodology ship` / sync 흐름이 방법론 경로 화이트리스트를 내장해
명시 add 를 대행. 적용 프로젝트의 빌드 산출물은 절대 staging 안 함.
(METH-019 acceptance — ship/sync 자동화 반영 후보)
