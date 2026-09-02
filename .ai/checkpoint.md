# 세션 체크포인트

> 세션 서사 바통. 누적 상태는 `HANDOFF.md`.

## 방금 한 것 (2026-09-02 · METH-146)

**pre-push 훅의 wrap 을 읽기 전용으로 바꿨다.** 오늘 두 번 `git restore` 로 치운 그 부작용이다.

- 원인: 훅이 돌리는 `wrap --strict` 가 검사만 하는 게 아니라 `prompting-report.md` 를 재생성하고, wrap-state 가 없으면 부트스트랩까지 **써 버린다**. push 가 실패해도 파일이 남고, 다음 `sync-all` 이 그걸 «진행 중 작업»으로 오인해 skip 한다.
- 수정: `wrap --read-only` — 두 쓰기를 생략. baseline 이 없으면 「pass + 다음 ship 이 저장」으로 밝힌다. 훅 템플릿은 `wrap --strict --read-only`. **ship 의 wrap 은 그대로** — 거기선 리포트 갱신이 의도된 산출물이다.
- 증명: 대조군(플래그 없음 → `wrap-state.json` 생성) vs 실험군(생성 안 함) · 임시 repo 에 훅 설치 후 sync 아닌 커밋 push → `git status` 비어 있음 · 단위 3테스트. **91/91.**

## 다음 구체 행동

1. ship → PR → land → `methodology.py` 전파 11 repo → **훅 3 repo 재설치** → origin 대조(`--read-only` 블롭 grep) → 재설치 후 훅 repo 의 `git status` 가 비어 있는지 확인(그게 실전 증명).
2. 끝나면 Working-on 「다음 작업 대기」. 후속 후보는 이걸로 없다.

## 막힌 것

- 없음.

## 환경

- repo: `/Users/hayden/methodology` · branch `fix/hook-wrap-readonly`
